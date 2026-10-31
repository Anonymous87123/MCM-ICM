# P-C-2015-39160-2b8963a3

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #39160

<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->
Page 1 of 17

<!-- b000007 | furniture | pages [1] -->
Team Control Number

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
For office use only

<!-- b000010 | title | pages [1] -->
39160

<!-- b000011 | prose | pages [1] -->
T1 ________________ T2 ________________

<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | prose | pages [1] -->
T3 ________________

<!-- b000014 | prose | pages [1] -->
F1 ________________ F2 ________________ F3 ________________

<!-- b000015 | prose | pages [1] -->
Problem Chosen

<!-- b000016 | prose | pages [1] -->
T4 ________________

<!-- b000017 | title | pages [1] -->
C

<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
F4 ________________

<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | heading | pages [1] -->
2015 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000022 | heading | pages [1] -->
(Attach a copy of this page to your solution paper.)

<!-- b000023 | heading | pages [1] -->
Type a summary of your results on this page. Do not include

<!-- b000024 | prose | pages [1] -->
the name of your school, advisor, or team members on this page.

<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | prose | pages [1] -->
In the modern world, organizations face a number of complex issues related to the recruitment and retention of high-quality personnel with the knowledge, skills, and abilities required for the organization to compete. Network effects of personnel flow into and out of an organization affect day to day operations of that organization. Large organizations, in particular, need to understand these types of flows in order to maximize the potential of their human capital. The professional and personal relationships amongst the members of the organization will have an effect on the turnover, or churn, within that organization.

<!-- b000027 | prose | pages [1] -->
Tasked with modeling churn within Information Cooperative Manufacturing (ICM), we developed a network model of this rigidly hierarchical company. This model allowed us to answer questions from the Human Resources department regarding dynamic processes within the network, budgetary concerns, labor forecasting, and hiring decision support.

<!-- b000028 | prose | pages [1] -->
Using the software package called the Multilayer Networks Library, we built a data structure where we treated each layer of a multilayer network as a graph representing a different type of relationship within the company. The computer representation of these networks is comprised of a multidimensional array, or tensor. We took an object oriented approach to simulating interactions between employees, interactions between positions in the hierarchy, and interactions between employees and their positions within the hierarchy.

<!-- b000029 | prose | pages [1] -->
In the first of three phases, we used a purely stochastic approach to determining the behavior of the various pieces of the simulation. This allowed precise control over the variables in the model, particularly the churn rate, allowing us to hit the target churn rates specified in the problem statement.

<!-- b000030 | prose | pages [1] -->
In the next phase, we introduced a satisfaction function through which we gave each “employee” of the company the ability to “choose” whether to remain in the company or leave. Using this version of the model, we were able to analyze churn at ICM from the perspective of employee satisfaction.

<!-- b000031 | prose | pages [1] -->
The third phase of the model included a productivity function, satisfaction function, and smart promotion algorithm, resulting in a realistic simulation of both employee and HR decision making.

<!-- b000032 | prose | pages [1] -->
Based on analyses of our three phase model, we find that ICM must increase the effectiveness of its HR office so that it can actively hire more than 10% of positions at a time. Otherwise, the churn rates cannot reach 25% if ICM is to maintain an 80% full status. ICM must also find ways to increase employee satisfaction. ICM can avoid the network effect whereby an employee’s satisfaction is reduced by vacancies in his work group or office group by placing new employees in relatively full sections of the company. Furthermore, HR should switch to using employee performance ratings for promotion decisions.

<!-- b000033 | furniture | pages [2] -->
Team #39160

<!-- b000034 | furniture | pages [2] -->


<!-- b000035 | furniture | pages [2] -->
Page 2 of 17

<!-- b000036 | furniture | pages [2] -->


<!-- b000037 | furniture | pages [2] -->


<!-- b000038 | heading | pages [2] -->
1 Introduction

<!-- b000039 | prose | pages [2] -->
Organizational churn has been frequently studied by sociologists, as evidenced in [1], [2], [3], [4], [5], [6], [7].  While numerous definitions for churn exist in the literature, for this paper we will simply define the employee churn rate, or simply churn, to be the ratio of employees who leave an organization in a year to the total number of positions in that organization. In order to reduce churn within Information Cooperative Manufacturing (ICM), we create a Human Capital network model and use it to analyze both the productivity and churn within the organization.

<!-- b000040 | prose | pages [2] -->
One common way to represent a network model is through the use of a graph. Such a graph might consist of a node set representing people, organizations, or other structures which are connected to each other by edges. Based upon previous research concerning the “science of team science,” i.e., the study of how teams work together on scientific projects, we find that analyzing the dynamic relationships between people at ICM is a good way to predict churn within the company [1]. Churn in any company is related to multiple factors including hierarchy, friendships, and other types of relationships between employees. Thus, we utilize an object presented by Mikko Kivelä, Alexandre Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno, and Mason A. Porter called a multilayer network, which is a way of representing how “sets of entities interact with each other” with respect to considerations like relationships, time, and “other complications” [3].

<!-- b000041 | prose | pages [2] -->
For the purposes of our paper, we define a multilayer network as a set of layers, where each layer holds a directed or undirected graph. We refer to a multilayer network simply as a network throughout this paper when the meaning is clear from context.  Constructing a network with multiple layers allows us to represent different types of connections between nodes on different layers. This means we can assign various types of relationships between positions and employees at ICM to different layers of the network, thereby representing the structure of the organization.

<!-- b000042 | heading | pages [2] -->
2 Computer Representation of ICM

<!-- b000043 | prose | pages [2] -->
In this section, we outline the representation we use to describe the organizational structure of ICM.

<!-- b000044 | heading | pages [2] -->
2.1 Multilayer Network: Positions Filled with People

<!-- b000045 | prose | pages [2] -->
When creating this model, we first consider one main question; that is, what do the nodes in the multilayer network represent: people within the company or positions within the company which may or may not be filled with a person? For our model, we use nodes to represent positions within the company hierarchy, rather than people. Thus, instead of adding, moving, and removing nodes, we move objects (people) from one node to another within each increment of time. This approach allows an employee occupying node  to inherit the properties of , such as professional relationships, rank within the hierarchy, and salary. Combining this inheritance property with the perspective of considering each layer in the network to represent a different type of relationship between the nodes allows for the flexibility necessary to represent various factors that affect churn within ICM.

<!-- b000046 | furniture | pages [2] -->


<!-- b000047 | furniture | pages [2] -->


<!-- b000048 | furniture | pages [3] -->
Team #39160

<!-- b000049 | furniture | pages [3] -->


<!-- b000050 | furniture | pages [3] -->
Page 3 of 17

<!-- b000051 | furniture | pages [3] -->


<!-- b000052 | heading | pages [3] -->
2.1.1 The Multi-dimensional Adjacency Tensor

<!-- b000053 | prose | pages [3] -->
Spring-boarding off of [3], we define a tensor || × || × || × || in size to represent the multilayer network which in turn represents the structure of ICM. We denote this tensor by ||×||×|	|×|
|, with  being the node set,  the set of types of relationships, and  the set of integers representing time steps.

<!-- b000054 | prose | pages [3] -->
In our model, ||×||×|	|×|
| includes the following two-dimensional adjacency sub-tensors, each of which corresponds to a layer in the multilayer network:

<!-- b000055 | prose | pages [3] -->
• The hierarchical structure of the company (This includes relationships such as “is the boss of” between supervising and the supervised positions). These relationships are immutable. In other words, it does not matter which specific person is placed into a position; the relationship in this layer between a given position and the position one level above or below will not change.

<!-- b000056 | prose | pages [3] -->
• The relationships among positions within the same work group at the company. These relationships are also immutable.

<!-- b000057 | prose | pages [3] -->
• The relationships among positions within the same office, but differing work groups. These relationships are also immutable.

<!-- b000058 | prose | pages [3] -->
• Time (Each two-dimensional sub-tensor representing a relationship type will change with respect to this fourth dimension in the tensor).

<!-- b000059 | prose | pages [3] -->
Taking the perspective of considering the network to be a multidimensional tensor allows us to conveniently represent such an object in the computer for analysis.

<!-- b000060 | heading | pages [3] -->
2.1.2 Organizing the Structure of ICM

<!-- b000061 | prose | pages [3] -->
In the problem statement, we are given a tree showing the overall hierarchy of ICM and a table showing seven levels of employees with the specified number of employees at each level. The given tree structure shows five levels of offices and we assign the seven levels of positions to these offices in the following way:

<!-- b000062 | prose | pages [3] -->
• Assign to the position levels the ranks 1-7, with 7 being the highest.

<!-- b000063 | prose | pages [3] -->
• For each office shown on the given tree, initialize the specified number of positions with appropriate levels, ensuring that every office contains at least one administrative clerk and two positions at the inexperienced supervisor level or higher with one unique highest ranked position in the office.

<!-- b000064 | prose | pages [3] -->
In offices consisting of two seven-position divisions, we assign label  to one division and the • label  to the other. We then assign the highest level position in the office to  and a second highest level position to . Assign the other positions in the office to  and  evenly.

<!-- b000065 | prose | pages [3] -->
Next, we generate the direct command structure at ICM in the following way:

<!-- b000066 | prose | pages [3] -->
• For each office at ICM, we assign the title of office manager to the highest ranked position that was assigned to that office.

<!-- b000067 | prose | pages [3] -->
• In offices containing two divisions, such as the CIO office, we assign the title division manager to the highest ranked position in division .

<!-- b000068 | furniture | pages [4] -->
Team #39160

<!-- b000069 | furniture | pages [4] -->


<!-- b000070 | prose | pages [4] -->
•

<!-- b000071 | furniture | pages [4] -->
Page 4 of 17

<!-- b000072 | prose | pages [4] -->
n an office of four positions supervises every other p

<!-- b000073 | prose | pages [4] -->
Each office manager within

<!-- b000074 | prose | pages [4] -->
position within that

<!-- b000075 | prose | pages [4] -->
he office manager in every directly connected office

<!-- b000076 | prose | pages [4] -->
office and also supervises th

<!-- b000077 | prose | pages [4] -->
e one level down in

<!-- b000078 | prose | pages [4] -->
he problem statement.

<!-- b000079 | prose | pages [4] -->
the tree structure given in th

<!-- b000080 | prose | pages [4] -->
visions, the office manager of  supervises the six

<!-- b000081 | prose | pages [4] -->
If office  contains two div •

<!-- b000082 | prose | pages [4] -->
other positions in

<!-- b000083 | prose | pages [4] -->
ivision manager of division  within . The office

<!-- b000084 | prose | pages [4] -->
division  as well as the di

<!-- b000085 | prose | pages [4] -->
manager of  also own from  in the

<!-- b000086 | prose | pages [4] -->
ager in every directly connected office one level do

<!-- b000087 | prose | pages [4] -->
supervises the office mana given tree structure.

<!-- b000088 | prose | pages [4] -->
division  supervises the six other positions in .

<!-- b000089 | prose | pages [4] -->
• Each division manager of a

<!-- b000090 | prose | pages [4] -->
mple showing this hierarchical structure on a small

<!-- b000091 | prose | pages [4] -->
We turn our attention to an exam

<!-- b000092 | prose | pages [4] -->
ler scale. Figure 1

<!-- b000093 | prose | pages [4] -->
er network representing ICM. Specifically, we h

<!-- b000094 | prose | pages [4] -->
depicts a subset of our multilaye

<!-- b000095 | prose | pages [4] -->
have depicted the

<!-- b000096 | prose | pages [4] -->
n the research and networks offices given in the prob

<!-- b000097 | prose | pages [4] -->
connections between the positions i

<!-- b000098 | prose | pages [4] -->
Figure 1

<!-- b000099 | prose | pages [4] -->
blem statement.

<!-- b000100 | prose | pages [4] -->
The bottom layer of the figu

<!-- b000101 | prose | pages [4] -->
re shows a tree

<!-- b000102 | prose | pages [4] -->
representing the direct command s

<!-- b000103 | prose | pages [4] -->
structure described

<!-- b000104 | prose | pages [4] -->
above. The node labeled 0 rep

<!-- b000105 | prose | pages [4] -->
resents the office

<!-- b000106 | prose | pages [4] -->
manager of the research office.

<!-- b000107 | prose | pages [4] -->
Since this office

<!-- b000108 | prose | pages [4] -->
manager supervises the other

<!-- b000109 | prose | pages [4] -->
positions in the

<!-- b000110 | prose | pages [4] -->
research office, we draw edges to

<!-- b000111 | prose | pages [4] -->
nodes 1, 2, and 3,

<!-- b000112 | prose | pages [4] -->
which represent those positions. T

<!-- b000113 | prose | pages [4] -->
his office manager

<!-- b000114 | prose | pages [4] -->
also supervises the networks offic

<!-- b000115 | prose | pages [4] -->
ce manager, so we

<!-- b000116 | prose | pages [4] -->
draw an edge from node 0 to nod

<!-- b000117 | prose | pages [4] -->
de 4, where node 4

<!-- b000118 | prose | pages [4] -->
represents the networks office

<!-- b000119 | prose | pages [4] -->
e manager. The

<!-- b000120 | prose | pages [4] -->
networks office manager, in turn,

<!-- b000121 | prose | pages [4] -->
supervises the six

<!-- b000122 | prose | pages [4] -->
positions in division  within the

<!-- b000123 | prose | pages [4] -->
networks office as vision . Thus, we

<!-- b000124 | prose | pages [4] -->
well as the division manager of div draw edges from node 4 to nodes 5

<!-- b000125 | prose | pages [4] -->
5-11. Similarly, we

<!-- b000126 | prose | pages [4] -->
draw edges from node 11, whi

<!-- b000127 | prose | pages [4] -->
ich represents the

<!-- b000128 | prose | pages [4] -->
division manager of the network

<!-- b000129 | prose | pages [4] -->
ks office, to nodes

<!-- b000130 | prose | pages [4] -->
12-17.

<!-- b000131 | prose | pages [4] -->
The middle layer represents the “w

<!-- b000132 | prose | pages [4] -->
works loosely with”

<!-- b000133 | prose | pages [4] -->
re in an edge if and only if they are in the same off

<!-- b000134 | prose | pages [4] -->
relation. Two nodes in this layer ar

<!-- b000135 | prose | pages [4] -->
fice, but not in the

<!-- b000136 | prose | pages [4] -->
that this is a complete bipartite graph due to the nat

<!-- b000137 | prose | pages [4] -->
same division. Of mild interest is t being represented.

<!-- b000138 | prose | pages [4] -->
ture of the relation

<!-- b000139 | prose | pages [4] -->
ks closely with” relation. Two nodes in this layer ar

<!-- b000140 | prose | pages [4] -->
The top layer represents the “work

<!-- b000141 | prose | pages [4] -->
re connected by an

<!-- b000142 | prose | pages [4] -->
n the same four position office or in the same divisi

<!-- b000143 | prose | pages [4] -->
edge if and only if they are either in

<!-- b000144 | prose | pages [4] -->
on, so this layer of

<!-- b000145 | prose | pages [4] -->
of cliques. The cliques representing the two divisio

<!-- b000146 | prose | pages [4] -->
the network is the disjoint union o

<!-- b000147 | prose | pages [4] -->
ons of the fourteen

<!-- b000148 | prose | pages [4] -->
of the complete bipartite graph representing that offi

<!-- b000149 | prose | pages [4] -->
position office are the complement o

<!-- b000150 | heading | pages [4] -->
2.1.3 Treating Objects Lik

<!-- b000151 | prose | pages [4] -->
ke People

<!-- b000152 | prose | pages [4] -->
We now define a Person, for the pu

<!-- b000153 | prose | pages [4] -->
ice.

<!-- b000154 | prose | pages [4] -->
urpose of our models, as an instance of a Python cla

<!-- b000155 | prose | pages [4] -->
Each Person has some immutable at

<!-- b000156 | prose | pages [4] -->
ttributes:

<!-- b000157 | prose | pages [4] -->
ss called “Person.”

<!-- b000158 | furniture | pages [5] -->
Team #39160

<!-- b000159 | furniture | pages [5] -->


<!-- b000160 | furniture | pages [5] -->
Page 5 of 17

<!-- b000161 | furniture | pages [5] -->


<!-- b000162 | prose | pages [5] -->
• An employee ID

<!-- b000163 | prose | pages [5] -->
• A gender

<!-- b000164 | prose | pages [5] -->
• A randomly generated name

<!-- b000165 | prose | pages [5] -->
• A competence level, which comes from a random normal variable centered at 0.5 and represents the Person’s inherent abilities.

<!-- b000166 | prose | pages [5] -->
Furthermore, a Person has the following variable attributes, which may change each tick:

<!-- b000167 | prose | pages [5] -->
• The node in the multilayer network representing its position in ICM

<!-- b000168 | prose | pages [5] -->
• Current rank in the company, from 1 to 7, inherited from the position currently occupied by the Person

<!-- b000169 | prose | pages [5] -->
• A satisfaction level, which is a variable between 0 and 1

<!-- b000170 | prose | pages [5] -->
• A performance level, which is also a variable between 0 and 1

<!-- b000171 | prose | pages [5] -->
• The total time the Person has existed within the company

<!-- b000172 | prose | pages [5] -->
• The total time the Person has occupied its current work group, based on the Person’s position on the multilayer network.

<!-- b000173 | prose | pages [5] -->
• The current salary of the Person, based on the Person’s current rank.

<!-- b000174 | prose | pages [5] -->
Finally, a Person is responsible for tracking the costs given in the table in the problem statement associated with its current rank.

<!-- b000175 | heading | pages [5] -->
3 The Model

<!-- b000176 | heading | pages [5] -->
3.1 Background

<!-- b000177 | prose | pages [5] -->
Before modeling the dynamic processes within the network, it is useful to consider the many factors influencing churn rate at any given company. The structure of ICM is full of teams and sub-teams which must coordinate with each other. Some research has been done in the area of the “science of team science,” which is the study of how scientific teams work together under various conditions [1]. In this area, each team may be considered an “information processing unit” which encodes, stores, and retrieves information at both an individual and at a group level [2]. Based upon former work in this area, we identify some factors that influence the effectiveness of team work as it pertains to the ICM company structure. The following are five of these factors:

<!-- b000178 | heading | pages [5] -->
1. Team training is intended to train teams to coordinate and better understand one another’s roles

<!-- b000179 | prose | pages [5] -->
within a team [2].

<!-- b000180 | heading | pages [5] -->
2. Shared cognition is, in brief, the sum of knowledge about assigned tasks and collective

<!-- b000181 | prose | pages [5] -->
understanding of a situation, which is increased through interaction between team members [2].

<!-- b000182 | heading | pages [5] -->
3. Composition of the team includes the “abilities and styles of team leaders” and the extent to

<!-- b000183 | prose | pages [5] -->
which “team members have worked together previously” [1].

<!-- b000184 | heading | pages [5] -->
4. Communication is the ability of the team to effectively communicate. Factors such as

<!-- b000185 | prose | pages [5] -->
“technological resources” and “conflict-resolution strategies” may affect the quality of

<!-- b000186 | furniture | pages [6] -->
Team #39160

<!-- b000187 | furniture | pages [6] -->


<!-- b000188 | furniture | pages [6] -->
Page 6 of 17

<!-- b000189 | furniture | pages [6] -->


<!-- b000190 | prose | pages [6] -->
communication among team members [1].

<!-- b000191 | heading | pages [6] -->
5. Collective orientation is the tendency of team members to take care of “task inputs” and the

<!-- b000192 | prose | pages [6] -->
needs of other team members [2].

<!-- b000193 | prose | pages [6] -->
With the exception of “Composition of the team,” each of the factors listed is increased in a team that works together for a significant amount of time. Thus, we may predict the existence of these factors within offices at ICM by keeping track of variables such as average time people spend in the same office. Under the assumption that these factors increase productivity and reduce churn, we consider change in productivity as a function of average time spent in the same office, average experience of people within the office, and the percent of vacancies in the office, and let churn be related to this change.

<!-- b000194 | heading | pages [6] -->
3.2 Definitions:

<!-- b000195 | prose | pages [6] -->
• Tick: One repetition of the main loop in our simulation of ICM, representing a time interval of one month.

<!-- b000196 | prose | pages [6] -->
• Churn rate: the number of employees who have left the organization in the previous “year” divided by the number of positions at ICM.

<!-- b000197 | prose | pages [6] -->
• Person: a Python class, representing an employee of ICM. Throughout the paper, when we refer to a Person, we are referring to an instance of this class.

<!-- b000198 | prose | pages [6] -->
• Position: a Python class, representing a position within ICM. We associate each position instance with a node in our network.

<!-- b000199 | prose | pages [6] -->
• Satisfaction level: A value between 0 and 1 assigned to each Person, which changes with time.

<!-- b000200 | prose | pages [6] -->
• Office: A staff office, either containing four positions or containing two divisions of 7 positions.

<!-- b000201 | prose | pages [6] -->
• Division: a set of 7 positions within a staff office.

<!-- b000202 | prose | pages [6] -->
• External hire: when our algorithm initiates a new Person and places it in a vacant node.

<!-- b000203 | prose | pages [6] -->
• Internal promotion: when our algorithm moves a Person from one node to another (of higher rank) in the network.

<!-- b000204 | heading | pages [6] -->
3.3 Initial Phase

<!-- b000205 | prose | pages [6] -->
In this phase, we create a simple model using the computer representation of ICM described in the previous section as a framework, populate positions with Persons, and randomly mark positions as vacant (because the Person associated with that position was promoted or left) such that the median time to recruit a person to fill each position is correct according to the information given to us. In this initial phase, we utilize purely stochastic processes for hiring and leaving, with the goal of ensuring that our framework correctly associates the nodes of the network with Persons. We also check to make sure that we are able to simulate the correct churn and vacancy rates specified in the problem statement.

<!-- b000206 | heading | pages [6] -->
3.3.1 Assumptions:

<!-- b000207 | prose | pages [6] -->
• Assume the hierarchical structure described in the computer representation section.

<!-- b000208 | prose | pages [6] -->
• The probability of a Person leaving is 0.015 per tick (0.18/year divided by 12 months).

<!-- b000209 | furniture | pages [7] -->
Team #39160

<!-- b000210 | furniture | pages [7] -->


<!-- b000211 | furniture | pages [7] -->
Page 7 of 17

<!-- b000212 | furniture | pages [7] -->


<!-- b000213 | prose | pages [7] -->
• A vacant position of rank 1 or 2 is always filled by an external hire.

<!-- b000214 | prose | pages [7] -->
• Human Resources (HR) can work on 2/3 of the current vacancies, up to a maximum of 10% of the total company.

<!-- b000215 | prose | pages [7] -->
• Training costs are incurred as defined in the table in the problem description every tick for every filled position.

<!-- b000216 | prose | pages [7] -->
• Recruitment costs are incurred as defined in the table in the problem description every tick for every position currently being worked on by HR, regardless of whether the position is eventually filled by an internal promotion or external hire, but not positions which are vacant and not being worked on.

<!-- b000217 | heading | pages [7] -->
3.3.2 Initializing the Model

<!-- b000218 | prose | pages [7] -->
We will use a multilayer network represented by a 370 × 370 × 3 adjacency tensor, where 370 is the number of positions in ICM (given in the problem statement), and 3 is the number of types of relationships included. The network is initialized according to the structure of ICM.

<!-- b000219 | prose | pages [7] -->
We create instances of a Python class called Person with the following attributes: rank of position the Person is in, a unique employee ID, time spent at company, and time spent in a work group, which we define as either an office containing 4 positions or a division containing 7 positions. These attributes are tracked in a table. Each Person initially inherits the rank and location in the ICM hierarchy of the position to which it was assigned.

<!-- b000220 | prose | pages [7] -->
The network is initialized with 85% of the positions randomly filled with non-empty Persons. All of the vacant positions are stored in a queue which we will refer to as the vacancy list. Rather than emptying the node for a position if it is vacant, we create a placeholder Person, flagged as “Vacant,” so that each node is always full. These placeholder Persons also have a negative employee ID number, consecutive to non- vacant Persons. From the vacancy list, 2/3 of the positions are chosen which have been vacant the longest and are placed into a separate queue to be filled by the HR office, which we refer to as the HR attention list.

<!-- b000221 | heading | pages [7] -->
3.3.3 Running the Model

<!-- b000222 | prose | pages [7] -->
Each time the main loop of our program runs, it goes through 12 time ticks, each of which represents one month. In each time tick, the following happens:

<!-- b000223 | prose | pages [7] -->
• We update the time with company and time with work group attributes of each Person.

<!-- b000224 | prose | pages [7] -->
• We update the HR attention list. The positions in this list will be vacant for the prescribed number of ticks, and then filled by the hiring algorithm described in the next section.

<!-- b000225 | prose | pages [7] -->
• We go through each position and if the position is full, determine if the Person filling that instance will leave this tick.

<!-- b000226 | prose | pages [7] -->
• If the Person in a position quits, we append this position to the end of the vacancy list and add one for each vacated position to the current churn number for the year.

<!-- b000227 | prose | pages [7] -->
Throughout a group of 12 ticks, the current time (number of month, beginning with January at 0) is updated along with the current training cost in the year to date, the current recruitment cost in the

<!-- b000228 | furniture | pages [8] -->
Team #39160

<!-- b000229 | furniture | pages [8] -->


<!-- b000230 | furniture | pages [8] -->
Page 8 of 17

<!-- b000231 | furniture | pages [8] -->


<!-- b000232 | prose | pages [8] -->
year to date, and churn counter for the year to date (the number of empty positions). The variables current training cost and current recruitment cost are functions of the rates given in the problem statement and the current number of employees at the company. For time ticks congruent to 1 through 11 mod 12, we keep a running count of the number of employees who have left the organization that “year,” then divide by 370 in order to calculate churn for that year. The variables current training cost, current recruitment cost, and churn counter are reset each year, so that in any given time tick, these three pieces of information can be found in an updated list for the current year.

<!-- b000233 | prose | pages [8] -->
As each tick is completed, the lists of Persons who have been hired, been promoted, or have left are updated. Thus, at the end of the year, a list is printed with training cost as percentage of median salary, recruitment cost as percentage of median salary, total churn, and current number of vacancies for the entire year.

<!-- b000234 | heading | pages [8] -->
3.3.3.1 Hiring Algorithm

<!-- b000235 | prose | pages [8] -->
• Each position has a corresponding “time to recruit” and “cost of recruitment” that must be applied when hiring for that position.

<!-- b000236 | prose | pages [8] -->
After allowing the appropriate number of ticks to pass, a vacant position of rank  > 2 is filled • either with an external hire (with a 25% chance) or by an internal promotion of a Person in a position of rank   −1 .

<!-- b000237 | prose | pages [8] -->
If filling a position of rank  internally, choose a random, non-vacant position of rank  −1 and • move the Person in that position to the position being filled.

<!-- b000238 | prose | pages [8] -->
If there is no Person of rank  −1 to hire or we previously took the hire externally option, • initialize a new Person and place it in that position.

<!-- b000239 | heading | pages [8] -->
3.3.3.2 Quitting Algorithm

<!-- b000240 | prose | pages [8] -->
• Each Person has a 1.5% chance of leaving per tick.

<!-- b000241 | heading | pages [8] -->
3.3.4 Analysis of the Initial Phase:

<!-- b000242 | prose | pages [8] -->
The stochastic, rather than deterministic nature of this phase of our model construction allows us to test the framework upon which subsequent phases will be built, with less complexity than will be introduced in later phases.  Furthermore, because the variables controlling churn rate in this phase are random rather than functions of other variables, we were able to more precisely control churn rate, allowing us to answer some of the posed questions in the specified manner.

<!-- b000243 | heading | pages [8] -->
3.4 Intermediate Phase

<!-- b000244 | prose | pages [8] -->
With the intermediate phase, we begin to build upon the simple model from phase one. Rather than randomly choosing positions to be vacant, however, we introduce variables which effect the satisfaction of employees and thereby affect the churn in ICM.

<!-- b000245 | heading | pages [8] -->
3.4.1 Further Assumptions:

<!-- b000246 | prose | pages [8] -->
In this phase, we assume the satisfaction level in tick  + 1 of Person  is affected by the • satisfaction level of  as well as the satisfaction levels of all Persons in positions connected to the position of .

<!-- b000247 | furniture | pages [9] -->
Team #39160

<!-- b000248 | furniture | pages [9] -->


<!-- b000249 | furniture | pages [9] -->
Page 9 of 17

<!-- b000250 | furniture | pages [9] -->


<!-- b000251 | prose | pages [9] -->
The satisfaction of  is most strongly affected by the previous satisfaction of . •

<!-- b000252 | prose | pages [9] -->
The satisfaction of  is second most strongly affected by the satisfactions of Persons in the same • work group as .

<!-- b000253 | prose | pages [9] -->
The satisfaction of the direct supervisor of  and the satisfactions of Persons in the same office as • , but not in the same work group, weakly affect the satisfaction of .

<!-- b000254 | prose | pages [9] -->
The satisfaction of  is sharply increased each time  receives a promotion to a higher position in • the company.

<!-- b000255 | heading | pages [9] -->
3.4.2 Changes in Initializing the Model

<!-- b000256 | prose | pages [9] -->
The only change from our initial phase initialization is that we now initialize each Person instance with a default starting value of 0.5 for satisfaction, unless that Person is a placeholder representing an empty position, in which case it is assigned a satisfaction level of 0.

<!-- b000257 | heading | pages [9] -->
3.4.3 Satisfaction Function

<!-- b000258 | prose | pages [9] -->
With our new concept of satisfaction, we introduce the following variables that affect the satisfaction of a Person  in tick  + 1:

<!-- b000259 | prose | pages [9] -->
Satisfaction of  Person  in time tick , given by the function () •

<!-- b000260 | prose | pages [9] -->
Satisfaction of the direct supervisor of  in tick , given by the function (). •

<!-- b000261 | prose | pages [9] -->
Average satisfaction in tick  of Persons in the same work group as , given by the function • ().

<!-- b000262 | prose | pages [9] -->
Average satisfaction in tick  of Persons in the same office as , given by the function (). •

<!-- b000263 | prose | pages [9] -->
From these four variables, we get the function for satisfaction of  in tick  + 1; that is, () = !() +  () + () + (), with constants  !,  ,  ,  , that add up to 1. By choosing constants in this way, we compute a weighted average of the satisfaction level of the various positions directly connected to .

<!-- b000264 | prose | pages [9] -->
In addition to these basic factors of satisfaction, there are several variables that effect satisfaction in specific cases. These are as follows:

<!-- b000265 | prose | pages [9] -->
If Person  is promoted in tick  + 1, we calculate the value c(1 − ()) + () . We then set • the satisfaction of  to the mean of this value and () as calculated previously.

<!-- b000266 | prose | pages [9] -->
If Person  is in a position of rank 4, 5, or 6, we calculate (1 − ). We then set the satisfaction • of  to the mean of this value and () as calculated previously.

<!-- b000267 | heading | pages [9] -->
3.4.4 Differences in Running the Model

<!-- b000268 | prose | pages [9] -->
In the main loop, we add a new step which updates satisfaction according to the equations described in the previous section.

<!-- b000269 | heading | pages [9] -->
3.4.4.1 Additions to Hiring Algorithm

<!-- b000270 | prose | pages [9] -->
• Need 2 yrs experience to be promoted

<!-- b000271 | furniture | pages [10] -->
Team #39160

<!-- b000272 | furniture | pages [10] -->


<!-- b000273 | furniture | pages [10] -->
Page 10 of 17

<!-- b000274 | furniture | pages [10] -->


<!-- b000275 | heading | pages [10] -->
3.4.4.2 A New Quitting Algorithm

<!-- b000276 | prose | pages [10] -->
Generate a uniform random variable # ∈(0,1). •

<!-- b000277 | prose | pages [10] -->
Define ,  as in the previous section and define a new quitting constant '!. •

<!-- b000278 | prose | pages [10] -->
If  # > '!(), then Person  leaves the company. •

<!-- b000279 | heading | pages [10] -->
3.4.5 Analysis of the Intermediate Phase

<!-- b000280 | prose | pages [10] -->
In the problem statement, we are instructed to consider the effects of employee dissatisfaction on churn. The introduction of a satisfaction function in this phase allows us to do so.  Further, we introduced tracking managerial satisfaction and churn separately from the rest of the company in this phase, allowing us to see how total churn is affected by churn in this subset of the employees.

<!-- b000281 | furniture | pages [10] -->


<!-- b000282 | heading | pages [10] -->
3.5 Final Model

<!-- b000283 | heading | pages [10] -->
3.5.1 Further Assumptions

<!-- b000284 | prose | pages [10] -->
In this phase, we assume the performance level in tick  + 1 of Person  is affected by the competence level of , which was defined when we initialized , as well as the performance levels of all Persons in Positions connected to  in a similar manner to the satisfaction function.

<!-- b000285 | prose | pages [10] -->
Performance in our model is further affected by performance of the supervisor, under the assumption that a highly effective supervisor will cause a supervisee to perform at a higher level.

<!-- b000286 | prose | pages [10] -->
We assume that the length of time a Person has been at the company and in its specific work group will cause that Person to perform at a higher level.

<!-- b000287 | heading | pages [10] -->
3.5.2 Changes in Initializing the Model

<!-- b000288 | prose | pages [10] -->
Persons are now initialized with both a variable performance attribute and an immutable competence attribute, as defined in Section 2.1.3.

<!-- b000289 | heading | pages [10] -->
3.5.3 Performance Function

<!-- b000290 | prose | pages [10] -->
The following are the variable affecting the performance of a Person  at tick  + 1:

<!-- b000291 | furniture | pages [11] -->
Team #39160

<!-- b000292 | furniture | pages [11] -->


<!-- b000293 | prose | pages [11] -->
Competence level of , denoted by (() •

<!-- b000294 | furniture | pages [11] -->


<!-- b000295 | furniture | pages [11] -->


<!-- b000296 | furniture | pages [11] -->
Page 11 of 17

<!-- b000297 | prose | pages [11] -->
Performance of the direct supervisor of  in tick , given by )() •

<!-- b000298 | prose | pages [11] -->
Average performance in tick  of Persons in the same work group as , given by )() •

<!-- b000299 | prose | pages [11] -->
The time  has been at the company, given by *+() •

<!-- b000300 | prose | pages [11] -->
The time  has been at the work group, given by *,() •

<!-- b000301 | prose | pages [11] -->
The satisfaction level of  at tick , which is given by the function () as defined in Section • 3.4.3

<!-- b000302 | prose | pages [11] -->
From these six variables, we get the function for performance of  in tick  + 1, that is,

<!-- b000303 | prose | pages [11] -->
*+() *,() )() =  ! (() + )() + )() +  - *,() + 1. + 0(), *+() + 1. + / -

<!-- b000304 | prose | pages [11] -->
with ∑ 2 = 1. As in the satisfaction function, we chose the constants in this way and the various functions that we multiplied by the constants so that )() remains between 0 and 1 at each tick.

<!-- b000305 | heading | pages [11] -->
3.5.4 Further Differences in Running the Model

<!-- b000306 | prose | pages [11] -->
In the main loop, we add a new step which updates the performance function according to the equations described in section 3.5.3.

<!-- b000307 | heading | pages [11] -->
3.5.4.1 Additions to the Hiring Algorithm

<!-- b000308 | prose | pages [11] -->
• We now require the hire function to evaluate the quality of each employee before choosing. Specifically, the hire function chooses the highest performing Person of rank  −1 when filling a position of rank .

<!-- b000309 | heading | pages [11] -->
3.5.5 Analysis of the Final Model

<!-- b000310 | prose | pages [11] -->
Our main goal in the final model is to set up performance as strongly linearly influenced by employee satisfaction, under the assumption that an employee who is happy with their job will be more productive. Figure 3 shows that we achieve this goal even with the introduction of numerous other variables that we believe affect performance to a lesser extent than satisfaction.

<!-- b000311 | heading | pages [11] -->
4 Results

<!-- b000312 | heading | pages [11] -->
4.1 Budget Requirements for Talent Management

<!-- b000313 | caption | pages [11] -->
Figure 4 is a pie chart showing the average budget spent on recruiting versus training over a period of

<!-- b000314 | prose | pages [11] -->
thirty years, in terms of σ (the median income for ICM).

<!-- b000315 | furniture | pages [12] -->
Team #39160

<!-- b000316 | furniture | pages [12] -->


<!-- b000317 | furniture | pages [12] -->


<!-- b000318 | furniture | pages [12] -->


<!-- b000319 | furniture | pages [12] -->
Page 12 of 17

<!-- b000320 | prose | pages [12] -->
As our model maintains an average of almost 86% positions

<!-- b000321 | prose | pages [12] -->
Figure 4

<!-- b000322 | prose | pages [12] -->
filled in the company over the thirty years, the recruitment cost is very low. Training cost is present for all Persons within ICM, however, so this value remains about the same over thirty years, since the company has about the same number of employees to

<!-- b000323 | prose | pages [12] -->
Training Cost

<!-- b000324 | prose | pages [12] -->
continually train over these thirty

<!-- b000325 | prose | pages [12] -->
Recruitment Cost

<!-- b000326 | prose | pages [12] -->
years.

<!-- b000327 | caption | pages [12] -->
Figure 5 is a graph showing the

<!-- b000328 | prose | pages [12] -->
changes in training cost, recruitment cost, and number of churned employees over the course of thirty years. As expected, training cost remains relatively constant since the percent of vacant positions in ICM remains nearly constant year by year in our model.

<!-- b000329 | prose | pages [12] -->
Since we limit the number of vacancies in ICM that the HR office can work on filling per tick to 2/3 of the current vacancies up to 10% of the total number of positions in the company, there is less variance in the recruitment cost per year than there is in the number of vacant positions (churned employees) in the graph. The trend of churned employees as opposed to recruitment cost based upon this restriction indicates that the HR office does not have the capacity to keep up with the number of positions that need to be filled. We suggest that the HR office expand in order to recruit and hire for a greater percentage of vacant positions in each tick.

<!-- b000330 | prose | pages [12] -->
90

<!-- b000331 | prose | pages [12] -->
80

<!-- b000332 | prose | pages [12] -->
70

<!-- b000333 | prose | pages [12] -->
60

<!-- b000334 | prose | pages [12] -->
50

<!-- b000335 | prose | pages [12] -->
40

<!-- b000336 | prose | pages [12] -->
30

<!-- b000337 | prose | pages [12] -->
20

<!-- b000338 | prose | pages [12] -->
10

<!-- b000339 | prose | pages [12] -->
0

<!-- b000340 | prose | pages [12] -->
1 3 5 7 9 11 13 15 17 19

<!-- b000341 | prose | pages [12] -->
Year

<!-- b000342 | prose | pages [12] -->
Figure 5

<!-- b000343 | prose | pages [12] -->
Training Cost

<!-- b000344 | prose | pages [12] -->
Churned Employees

<!-- b000345 | prose | pages [12] -->
Recruitment Cost

<!-- b000346 | prose | pages [12] -->
21 23 25 27 29

<!-- b000347 | furniture | pages [12] -->


<!-- b000348 | heading | pages [12] -->
4.2 Sustainability of 80% Full Status

<!-- b000349 | prose | pages [12] -->
One important question to consider is whether or not ICM can maintain 80% full positions, even with a higher churn rate of 25 or 35 percent. We will first consider a churn rate of 25%.

<!-- b000350 | furniture | pages [13] -->
Team #39160

<!-- b000351 | furniture | pages [13] -->


<!-- b000352 | furniture | pages [13] -->


<!-- b000353 | furniture | pages [13] -->


<!-- b000354 | furniture | pages [13] -->
Page 13 of 17

<!-- b000355 | prose | pages [13] -->
As shown in figure 6, as long as the number of vacancies is below the maximum 10% of total positions

<!-- b000356 | prose | pages [13] -->
Figure 6

<!-- b000357 | prose | pages [13] -->
39

<!-- b000358 | prose | pages [13] -->
Positions HR is Working on

<!-- b000359 | prose | pages [13] -->
37

<!-- b000360 | prose | pages [13] -->
35

<!-- b000361 | prose | pages [13] -->
33

<!-- b000362 | prose | pages [13] -->
31

<!-- b000363 | prose | pages [13] -->
29

<!-- b000364 | prose | pages [13] -->
27

<!-- b000365 | prose | pages [13] -->
25

<!-- b000366 | prose | pages [13] -->
40 45 50 55 60

<!-- b000367 | prose | pages [13] -->
Vacancies

<!-- b000368 | prose | pages [13] -->
(37) that HR can work on filling, HR is able to increase the number of vacancies it is working on filling in proportion to empty positions. Thus, assuming HR does not get behind in its work filling vacant positions, ICM can maintain its 80% full status even with a 25%

<!-- b000369 | prose | pages [13] -->
65 70 75

<!-- b000370 | prose | pages [13] -->
churn rate.

<!-- b000371 | prose | pages [13] -->
As there are 370 positions in the company, HR is only able to work on filling up to 37 positions at once, regardless of how many positions are currently vacant. Thus, when there are more than 55 vacant positions in ICM, HR cannot work on filling 2/3 of these positions at once.

<!-- b000372 | prose | pages [13] -->
When HR is not able to work on at least 2/3 of

<!-- b000373 | prose | pages [13] -->
160

<!-- b000374 | prose | pages [13] -->
the current vacant

<!-- b000375 | prose | pages [13] -->
150

<!-- b000376 | prose | pages [13] -->
positions, the number

<!-- b000377 | prose | pages [13] -->
140

<!-- b000378 | prose | pages [13] -->
Number of Vacancies

<!-- b000379 | prose | pages [13] -->
of vacancies

<!-- b000380 | prose | pages [13] -->
130

<!-- b000381 | prose | pages [13] -->
compounds/increases

<!-- b000382 | prose | pages [13] -->
120

<!-- b000383 | prose | pages [13] -->
every year, as shown in

<!-- b000384 | prose | pages [13] -->
110

<!-- b000385 | caption | pages [13] -->
Figure 7.

<!-- b000386 | prose | pages [13] -->
100

<!-- b000387 | prose | pages [13] -->
As we can see in

<!-- b000388 | prose | pages [13] -->
90 80

<!-- b000389 | prose | pages [13] -->
Figure 8, this means

<!-- b000390 | prose | pages [13] -->
70

<!-- b000391 | prose | pages [13] -->
that ICM is not

<!-- b000392 | prose | pages [13] -->
60

<!-- b000393 | prose | pages [13] -->
necessarily able to

<!-- b000394 | prose | pages [13] -->
0 5

<!-- b000395 | prose | pages [13] -->
sustain its 80% full status with a churn rate at 25%.

<!-- b000396 | prose | pages [13] -->
Figure 7

<!-- b000397 | prose | pages [13] -->
10 15 20 25 30 35

<!-- b000398 | prose | pages [13] -->
Year number

<!-- b000399 | furniture | pages [14] -->
Team #39160

<!-- b000400 | furniture | pages [14] -->


<!-- b000401 | prose | pages [14] -->
100%

<!-- b000402 | prose | pages [14] -->
90%

<!-- b000403 | prose | pages [14] -->
80%

<!-- b000404 | prose | pages [14] -->
70%

<!-- b000405 | prose | pages [14] -->
60%

<!-- b000406 | prose | pages [14] -->
50%

<!-- b000407 | prose | pages [14] -->
40%

<!-- b000408 | prose | pages [14] -->
30%

<!-- b000409 | prose | pages [14] -->
20%

<!-- b000410 | prose | pages [14] -->
10%

<!-- b000411 | prose | pages [14] -->
0%

<!-- b000412 | prose | pages [14] -->
1 3 5 7 9 11 13 15 17

<!-- b000413 | furniture | pages [14] -->


<!-- b000414 | furniture | pages [14] -->


<!-- b000415 | furniture | pages [14] -->
Page 14 of 17

<!-- b000416 | prose | pages [14] -->
Figure 8

<!-- b000417 | prose | pages [14] -->
Pct Pos Vacant

<!-- b000418 | prose | pages [14] -->
Pct Pos Filled

<!-- b000419 | prose | pages [14] -->
19 21 23 25 27 29

<!-- b000420 | furniture | pages [14] -->


<!-- b000421 | prose | pages [14] -->
When introducing a 35% churn rate, ICM begins its very first year with less than 80% filled positions. Again, HR cannot work on more than 37 positions at once, and these vacancies compound to the point that ICM has an average of 51% filled positions over 30 years.

<!-- b000422 | prose | pages [14] -->
The gross cost of this high turnover at ICM is found in the increased recruiting cost (as HR is working on filling the maximum number of employees as possible at all times) and the reduced productivity as a result of high percentage of vacancies in ICM. However, with fewer employees, the training cost is reduced and the amount of money spent paying the salaries of all employees is also reduced. Thus, the net cost of turnover is some combination of these four factors.

<!-- b000423 | prose | pages [14] -->
In the case that churn rate remains high, we strongly recommend that the HR office expand so that it has a greater capacity for filling vacant positions. Without this capacity, there is no guarantee that ICM can maintain 80% full status with increasing churn rates.

<!-- b000424 | heading | pages [14] -->
4.3 Impact of High Supervisor Turnover

<!-- b000425 | prose | pages [14] -->
ICM has identified Junior Managers and Experienced Supervisors as “middle managers” whose churn rate tends to be higher than the churn in other positions. Thus, it is pertinent to analyze the impact of a high churn rate (30%) in these two positions while all other positions maintain an 18% churn rate.

<!-- b000426 | prose | pages [14] -->
In order to avoid low productivity, it is preferable for these positions to be filled by Persons in ICM which are qualified by a high level of experience within the company. Hence, we consider the aforementioned churn rates along with the following two criteria:

<!-- b000427 | prose | pages [14] -->
• No external recruiting is permitted for these rank 5 and rank 6 positions.

<!-- b000428 | prose | pages [14] -->
Only employees of rank  −1 with at least 2 years of experience are considered qualified for • promotion to a rank  position in ICM.

<!-- b000429 | prose | pages [14] -->
Running the model with these criteria, we find that a 30% churn rate in the positions of rank 5 and 6 with a churn rate of 18% in all other positions does not have a significant effect on the HR health, the ability of HR to fill vacant positions in a timely manner, at ICM. Since the set of all positions of rank 5 or 6 is small relative to the entire company, HR has the power to work on filling these positions with little difficulty.

<!-- b000430 | furniture | pages [15] -->
Team #39160

<!-- b000431 | furniture | pages [15] -->


<!-- b000432 | furniture | pages [15] -->
Page 15 of 17

<!-- b000433 | furniture | pages [15] -->


<!-- b000434 | heading | pages [15] -->
5 Conclusion

<!-- b000435 | heading | pages [15] -->
5.1 Recommendations

<!-- b000436 | prose | pages [15] -->
• The HR department needs to be expanded to keep pace with the projected vacancy levels of ICM.

<!-- b000437 | prose | pages [15] -->
• Find ways to increase employee satisfaction. Specifically, group employees in relatively full sections of the company, avoiding the network effect whereby an employee’s satisfaction is reduced by vacancies in his work group or office.

<!-- b000438 | prose | pages [15] -->
• HR should switch to using employee performance ratings for promotion decisions.

<!-- b000439 | heading | pages [15] -->
5.2 Further Work

<!-- b000440 | prose | pages [15] -->
The framework of our model is very flexible. With more time to work on it, we could easily take into consideration more factors effecting the churn and productivity at ICM. We are also able to see some interesting dynamic action using the final version of our model. It provides us with a reasonable approximation of both satisfaction and productivity as they affect churn at ICM. In fact, satisfaction levels feed into productivity levels in our model and vice versa, which realistically simulates the feedback between these two variables in real world situations.

<!-- b000441 | prose | pages [15] -->
The model is also quite realistic in the way sets of Persons interact within the company. For example, if Persons in a work group have high individual satisfaction levels, these cause the entire work group to have increased happiness. If Persons in a work group have low satisfaction levels, this too causes a feed- back loop and decreased satisfaction across the work group. The productivity of Persons in a work group is also compounded in this way, though the process is more complicated than the process for mere satisfaction. This is because productivity of a Person  is influenced not only by the productivity of Persons in the same work group as , but also by the level of experience of Persons in that work group and the volatility of churn in ICM. This is also realistic since a company containing high percentages of inexperienced employees will not be as productive as one with more experienced employees, and even an employee with high experience will not be as productive when moved to a new position (a result of churn).

<!-- b000442 | prose | pages [15] -->
Although our model is realistic and flexible in these regards, there are many things we would like to further improve. First and foremost, our model currently only includes a few factors which affect turnover. In real life, there are countless other factors which can be relevant to the resulting turnover in a company. Given more time, we would like to add a friendship relationship as a layer in our model so that friendships between employees follow Persons in the company regardless of the professional relationships between those Persons. This would allow us to simulate yet another effect of moving people to different positions in ICM. It may be that maintaining friendships across divisions would enhance productivity in ICM, even when two formerly closely related Persons are moved into separate professional groups at ICM, an effect that our current model does not track.

<!-- b000443 | prose | pages [15] -->
Another way in which the model could be improved would be to add another attribute to each Person to represent workplace skills and abilities possessed by those employees, and to the nodes in the hierarchy to represent the skillset required by those positions.  These additions would be useful to add another dimension to the model to better allow matching of employees to positions and provide another metric for simulation of employee performance.

<!-- b000444 | furniture | pages [16] -->
Team #39160

<!-- b000445 | furniture | pages [16] -->


<!-- b000446 | furniture | pages [16] -->
Page 16 of 17

<!-- b000447 | furniture | pages [16] -->


<!-- b000448 | prose | pages [16] -->
There are also several things that may occur in ICM according to our current model that do not necessarily happen in real life. For example, a Person could theoretically be promoted to a supervisor position that is supervising a group of empty positions. This would not likely happen in a real life company.

<!-- b000449 | heading | pages [16] -->
5.3 Other Approaches

<!-- b000450 | heading | pages [16] -->
5.3.1 The Tree: Positions Following People

<!-- b000451 | prose | pages [16] -->
Another way to model the ICM company is to create a tree that represents the hierarchical relationship between employees within ICM. In this initial graph, each person is represented by a node and each relationship between people is represented by an edge between the corresponding nodes. In order to properly represent all relationships in ICM, we need multiple graphs, including, but not limited to, a tree representing the hierarchical structure of the company and a graph representing relationships between employees within divisions. Just as in the model we created, other relationships may be tracked in more graphs, such as friendships between employees at ICM.

<!-- b000452 | prose | pages [16] -->
Since each position held by a person in ICM must be represented as an attribute of that person, the hierarchical structure of the company is mutable using this approach. Though we may create our graph with immutable connections between the positions, the model must assign attributes to Persons, which may include relationships between Persons that would otherwise have been represented with separate graphs using this approach.

<!-- b000453 | prose | pages [16] -->
This has the potential to make moving people to and from positions in the company quite tricky. However, this approach is not entirely separate from the approach we used. Aspects of both approaches must be implemented to create a cohesive model of the ICM company.

<!-- b000454 | heading | pages [16] -->
References

<!-- b000455 | references | pages [16] -->
[1] D. Stokols, K.L. Hall, B.K. Taylor, R.P. Moser. (2008). The Science of Team Science: Overview of

<!-- b000456 | references | pages [16] -->
the Field and Introduction to the Supplement, Am J Prev Med 2008; 35(2S): S277-S89.

<!-- b000457 | references | pages [16] -->
[2] E. Salas, N.J. Cooke, and M.A. Rosen. (2008). On Teams, Teamwork, and Team Performance:

<!-- b000458 | references | pages [16] -->
Discoveries and Developments. Human Factors: The Journal of the Human Factors and

<!-- b000459 | references | pages [16] -->
Ergonomics Society June 2008 vol. 50 no. 3 540-547.

<!-- b000460 | references | pages [16] -->
[3] Mikko Kivelä, Alexandre Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno, Mason A.

<!-- b000461 | references | pages [16] -->
Porter. (2013). Multilayer Networks, J. Complex Networks, 2(3): 203-271 (2014); arXiv preprint

<!-- b000462 | references | pages [16] -->
arXiv:1309.7233, 2013.

<!-- b000463 | references | pages [16] -->
[4] Kara L. Hall, Annie X. Feng, Richard P. Moser, Daniel Stokols, Brandie K. Taylor, Moving the

<!-- b000464 | references | pages [16] -->
Science of Team Science Forward: Collaboration and Creativity, American Journal of Preventive

<!-- b000465 | references | pages [16] -->
Medicine, Volume 35, Issue 2, Supplement, August 2008, Pages S243-S249, ISSN 0749-3797,

<!-- b000466 | references | pages [16] -->
http://0-dx.doi.org.skyline.ucdenver.edu/10.1016/j.amepre.2008.05.007.

<!-- b000467 | references | pages [16] -->
[5] Louise C. Mâsse, Richard P. Moser, Daniel Stokols, Brandie K. Taylor, Stephen E. Marcus, Glen D.

<!-- b000468 | references | pages [16] -->
Morgan, Kara L. Hall, Robert T. Croyle, William M. Trochim, Measuring Collaboration and

<!-- b000469 | references | pages [16] -->
Transdisciplinary Integration in Team Science, American Journal of Preventive Medicine,

<!-- b000470 | references | pages [16] -->
Volume 35, Issue 2, Supplement, August 2008, Pages S151-S160, ISSN 0749-3797, http://0-

<!-- b000471 | furniture | pages [17] -->
Team #39160

<!-- b000472 | furniture | pages [17] -->


<!-- b000473 | furniture | pages [17] -->
Page 17 of 17

<!-- b000474 | furniture | pages [17] -->


<!-- b000475 | references | pages [17] -->
dx.doi.org.skyline.ucdenver.edu/10.1016/j.amepre.2008.05.020.

<!-- b000476 | references | pages [17] -->
[6] Daniel Stokols, Shalini Misra, Richard P. Moser, Kara L. Hall, Brandie K. Taylor, The Ecology of

<!-- b000477 | references | pages [17] -->
Team Science: Understanding Contextual Influences on Transdisciplinary Collaboration,

<!-- b000478 | references | pages [17] -->
American Journal of Preventive Medicine, Volume 35, Issue 2, Supplement, August 2008, Pages

<!-- b000479 | references | pages [17] -->
S96-S115, ISSN 0749-3797, http://0-

<!-- b000480 | references | pages [17] -->
dx.doi.org.skyline.ucdenver.edu/10.1016/j.amepre.2008.05.003.

<!-- b000481 | references | pages [17] -->
[7] Kara L. Hall, Daniel Stokols, Richard P. Moser, Brandie K. Taylor, Mark D. Thornquist, Linda C.

<!-- b000482 | references | pages [17] -->
Nebeling, Carolyn C. Ehret, Matthew J. Barnett, Anne McTiernan, Nathan A. Berger, Michael I.

<!-- b000483 | references | pages [17] -->
Goran, Robert W. Jeffery, The Collaboration Readiness of Transdisciplinary Research Teams and

<!-- b000484 | references | pages [17] -->
Centers: Findings from the National Cancer Institute's TREC Year-One Evaluation Study,

<!-- b000485 | references | pages [17] -->
American Journal of Preventive Medicine, Volume 35, Issue 2, Supplement, August 2008, Pages

<!-- b000486 | references | pages [17] -->
S161-S172, ISSN 0749-3797, http://0-

<!-- b000487 | references | pages [17] -->
dx.doi.org.skyline.ucdenver.edu/10.1016/j.amepre.2008.03.035.

<!-- b000488 | furniture | pages [17] -->


<!-- b000489 | furniture | pages [17] -->

