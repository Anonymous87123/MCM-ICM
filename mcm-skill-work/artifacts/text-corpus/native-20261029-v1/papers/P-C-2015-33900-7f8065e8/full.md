# P-C-2015-33900-7f8065e8

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
33900

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
C

<!-- b000015 | heading | pages [1] -->
2015 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000016 | prose | pages [1] -->
Analyzing Employee Turnover Using Dynamic Network

<!-- b000017 | heading | pages [1] -->
Summary

<!-- b000018 | prose | pages [1] -->
In this paper, we build a dynamic network model and perform various simulations to study the behavior of Human Capital Network (HCN) under disturbance such as churns.

<!-- b000019 | prose | pages [1] -->
We detail the structure of HCN factors and continuing eﬀects of turnover and dy- namics of HCN utilizing given information and run simulations to examine the contagion of turnover and analyze the sustainability of HCN. We interpret and present our results along with robustness analysis and strengths and weaknesses of our model.

<!-- b000020 | prose | pages [1] -->
For Task 1, we build two networks (Personnel Relationship Network and Organiza- tional Network), which together form our Human Capital Network. We extract important information from problem material and make assumptions when necessary to deduce the detailed structure and assign employees with the oﬃces. We propose an evaluation function of assignments and use Genetic Algorithm to ﬁnd the optimal assignment. The assign- ment provides us with new information about employee relationship(co-oﬃce relationship etc.), together with the supervisory relationship form the edges in HCN and complete our network building.

<!-- b000021 | prose | pages [1] -->
For Task 2, we ﬁrst detail the turnover in terms of factors and impacts and evaluate the cost and productivity of HCN. We then dig into the dynamics in terms of turnover process, promotion process and recruitment process using probabilistic method and discrete time system simulation. The results show that organizational churn has both direct and indirect eﬀects on the organization’s productivity. The direct eﬀect is because it causes loss of employee and the indirect is because it will make other employee more likely to turnover.

<!-- b000022 | prose | pages [1] -->
For Task 3, we utilize our dynamic network model with our discrete time simulating system to calculate the budget. Our result is a budget requirement of 19.14σ for recruiting and 10.87σ for training in the next 2 years, adding up to 30.01σ.

<!-- b000023 | prose | pages [1] -->
For Task 4, we also run simulations and results show that ICM can’t sustain its 80% full status.

<!-- b000024 | prose | pages [1] -->
For Task 5, our results show that promotion increases the number of high-level em- ployee and improve the quality of staﬀbecause only those qualiﬁed can be promoted. Thus promotion increases the productivity.

<!-- b000025 | prose | pages [1] -->
We also make further discussions on Multi-layer Networks and HR issues which com- plete Task 6, 7 and other requirements that the problem material brought forth.

<!-- b000026 | furniture | pages [2] -->
Team # 33900

<!-- b000027 | prose | pages [2] -->
i

<!-- b000028 | heading | pages [2] -->
Contents

<!-- b000029 | contents | pages [2] -->
1

<!-- b000030 | heading | pages [2] -->
Introduction

<!-- b000031 | prose | pages [2] -->
1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Problem Statement 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Related Work

<!-- b000032 | prose | pages [2] -->
2

<!-- b000033 | heading | pages [2] -->
Assumptions and Notations

<!-- b000034 | prose | pages [2] -->
1

<!-- b000035 | prose | pages [2] -->
1

<!-- b000036 | prose | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 1

<!-- b000037 | prose | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000038 | prose | pages [2] -->
3

<!-- b000039 | heading | pages [2] -->
The Human Capital Network Model

<!-- b000040 | prose | pages [2] -->
2

<!-- b000041 | prose | pages [2] -->
2

<!-- b000042 | prose | pages [2] -->
Assigning Employees to Oﬃces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 2

<!-- b000043 | prose | pages [2] -->
Principles of Employee Assignment . . . . . . . . . . . . . . . . . . . . . . 3.1.1 2

<!-- b000044 | prose | pages [2] -->
Evaluation of Employee Assignment 3.1.2 . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | prose | pages [2] -->
3

<!-- b000046 | prose | pages [2] -->
Optimization Using Genetic Algorithm . . . . . . . . . . . . . . . . . . . . 3.1.3 3

<!-- b000047 | prose | pages [2] -->
Building The Human Capital Network . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 4

<!-- b000048 | prose | pages [2] -->
Building The Network of Personnel Relationship 3.2.1 . . . . . . . . . . . . . .

<!-- b000049 | prose | pages [2] -->
4

<!-- b000050 | prose | pages [2] -->
Building the Organizational Network . . . . . . . . . . . . . . . . . . . . . 3.2.2 5

<!-- b000051 | prose | pages [2] -->
Evaluating Turnover Intention of Employee . . . . . . . . . . . . . . . . . . . . . . 3.3 6

<!-- b000052 | prose | pages [2] -->
Factor of Turnover Contagion . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.1 6

<!-- b000053 | prose | pages [2] -->
Factor of Employee Centrality . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.2 7

<!-- b000054 | prose | pages [2] -->
Factors of Salary and Promotion Prospect . . . . . . . . . . . . . . . . . . 3.3.3 7

<!-- b000055 | prose | pages [2] -->
Evaluation using AHP] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.4 8

<!-- b000056 | prose | pages [2] -->
Productivity and Costs of HCM . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4

<!-- b000057 | prose | pages [2] -->
4 Dynamics of Human Capital Network

<!-- b000058 | prose | pages [2] -->
9

<!-- b000059 | prose | pages [2] -->
9

<!-- b000060 | prose | pages [2] -->
Process of Turnover . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 10 Process of Promotion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 10 Process of Recruitment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3

<!-- b000061 | prose | pages [2] -->
5

<!-- b000062 | heading | pages [2] -->
Simulation Results and Analysis

<!-- b000063 | prose | pages [2] -->
6

<!-- b000064 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000065 | prose | pages [2] -->
10

<!-- b000066 | prose | pages [2] -->
11

<!-- b000067 | prose | pages [2] -->
14

<!-- b000068 | prose | pages [2] -->
Improvements using Multi-layered Networks 7

<!-- b000069 | prose | pages [2] -->
8 Further Discussions on HR

<!-- b000070 | prose | pages [2] -->
9

<!-- b000071 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000072 | prose | pages [2] -->
15

<!-- b000073 | prose | pages [2] -->
16

<!-- b000074 | prose | pages [2] -->
16

<!-- b000075 | prose | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 16

<!-- b000076 | prose | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2

<!-- b000077 | heading | pages [2] -->
References

<!-- b000078 | references | pages [2] -->
16

<!-- b000079 | references | pages [2] -->
17

<!-- b000080 | furniture | pages [3] -->
Team # 33900

<!-- b000081 | furniture | pages [3] -->
Page 1 of 18

<!-- b000082 | references | pages [3] -->
1

<!-- b000083 | heading | pages [3] -->
Introduction

<!-- b000084 | prose | pages [3] -->
1.1 Problem Statement

<!-- b000085 | prose | pages [3] -->
Among various factors that inﬂuence a teamąŕs performance, the members of the team and the chemistry between them, i.e. teamwork, is an important one. The approach to this is to maintain a team of talented and well-trained people and keep them in proper positions. However, in modern companies employee turnover [5] often takes place and disturb the environments. This paper oﬀers a model of employee turnover and its impact based on the Human Capital Network. The HCN is extracted as a hierarchy structure of staﬀoﬃces and divisions as nodes and a list of 370 employees as nodes, then the turnover intention is analyzed by the AHP method, and divided as salary, promotion, importance and impacts from others. The importance of the nodes is given by the closeness centrality and the LeaderRank value of nodesąŕ departments. Salary and promotion are impacts indicators in consideration for diﬀerent levels. The impact is conducted through links and damps as time elapse. The promotion process and recruit process are also predicted by stochastic process methods, which make a part in the total dynamic process.

<!-- b000086 | prose | pages [3] -->
1.2 Related Work

<!-- b000087 | prose | pages [3] -->
In recent years, there has been tremendous interest in studying Team Science and de- veloping appropriate model of team and team performance. Salas et al. reviewed key discoveries and developments in the ﬁeld of team performance over the past 50 years [2]. They concluded that ‘team performance can be modeled’ and which are our motivation to model the productivity.Stokols et al. argued about [3] and Kivelä et al. studied the Multilayer Networks. which are incorporated into our paper for improvement of our model.

<!-- b000088 | prose | pages [3] -->
Many works have inspected the nature of rumor propagation etc. which is similar to[NOT good...] turnover propagation.

<!-- b000089 | prose | pages [3] -->
However, the methods they used are mainly mean-ﬁeld equations for homogeneous networks and ... for heterogenous networks. the underlying mechanism of how network structure inﬂuences the rumor spreading is still an open question.

<!-- b000090 | prose | pages [3] -->
There have been extensive study But limited work has been done in analyzing the turnover process using a mathematical model and quantifying (??) its impact on the overall team performance. We are concerned in this paper with the...

<!-- b000091 | prose | pages [3] -->
2

<!-- b000092 | heading | pages [3] -->
Assumptions and Notations

<!-- b000093 | prose | pages [3] -->
2.1

<!-- b000094 | heading | pages [3] -->
Assumptions

<!-- b000095 | prose | pages [3] -->
We make the following basic assumptions in order to simplify the problem. Each of our assumptions is justiﬁed and is consistent with the information given in [1].

<!-- b000096 | prose | pages [3] -->
• Turnover behavior of an employee is contagious. So the worker connected to other employees who have churned is more likely to churn [1].

<!-- b000097 | prose | pages [3] -->
• Similar individuals are more likely to aﬀect each other’s behavior. This is

<!-- b000098 | furniture | pages [4] -->
Team # 33900

<!-- b000099 | furniture | pages [4] -->
Page 2 of 18

<!-- b000100 | prose | pages [4] -->
an adopted assumption from previous work of Feeley et al. [15].

<!-- b000101 | prose | pages [4] -->
2.2

<!-- b000102 | heading | pages [4] -->
Notations

<!-- b000103 | prose | pages [4] -->
We use a list of symbols (cf. Table 1) for simpliﬁcation of expression.

<!-- b000104 | caption | pages [4] -->
Table 1. Notations (in the order of model)

<!-- b000105 | prose | pages [4] -->
Symbol Deﬁnition Notes

<!-- b000106 | heading | pages [4] -->
Human Capital Network Model

<!-- b000107 | prose | pages [4] -->
G cf. Figure 2 graph of Personnel Relationship Network of ICM g cf. Figure 3 graph of Organizational Network of ICM N number of nodes topological distance between node i and j dij

<!-- b000108 | prose | pages [4] -->
Rt employee turnover rate

<!-- b000109 | prose | pages [4] -->
T turnover intention CC Closeness Centrality

<!-- b000110 | prose | pages [4] -->
NELDY 1

<!-- b000111 | prose | pages [4] -->
(NEBY 2+NEEY 3)/2 × 100% [5]

<!-- b000112 | prose | pages [4] -->
Rt =

<!-- b000113 | prose | pages [4] -->
N

<!-- b000114 | prose | pages [4] -->
CCi = 1

<!-- b000115 | prose | pages [4] -->
di = PN

<!-- b000116 | prose | pages [4] -->
j=1 dij average annual salary(payment) of employee i Pi represents employee’s ability level of hierarchy of the oﬃce of employee i Li LCEO = 5 and LBranch = 1

<!-- b000117 | heading | pages [4] -->
The Second Model

<!-- b000118 | prose | pages [4] -->
Emu stuﬀed C frozen

<!-- b000119 | heading | pages [4] -->
The Human Capital Network Model

<!-- b000120 | prose | pages [4] -->
3

<!-- b000121 | prose | pages [4] -->
In this model, the HCN is extracted as a hierarchy structure of staﬀoﬃces and divisions as nodes and a list of 370 employees as nodes, then the turnover intention is analyzed by the AHP method, and divided as salary, promotion, importance and impacts from others. The importance of the nodes is given by the closeness centrality and the LeaderRank value of nodesąŕ departments.

<!-- b000122 | prose | pages [4] -->
3.1 Assigning Employees to Oﬃces

<!-- b000123 | prose | pages [4] -->
Due to limited given information on the personnel relationship of ICM in detail, we assume some basic rules of allocating oﬃces to complete our model. We apply these rules and form an AHP-based evaluation model, then we use Genetic Algorithm to ﬁnd the solution.

<!-- b000124 | prose | pages [4] -->
Principles of Employee Assignment 3.1.1

<!-- b000125 | prose | pages [4] -->
Our principles for allocating oﬃces is listed as follows:

<!-- b000126 | prose | pages [4] -->
1NELDY:Number of Employees who Left During the Year. 2NEBY:Number of Employees at the Beginning of the Year. 3NEEY:Number of Employees at the End of the Year.

<!-- b000127 | furniture | pages [5] -->
Team # 33900

<!-- b000128 | furniture | pages [5] -->
Page 3 of 18

<!-- b000129 | prose | pages [5] -->
• Employees with higher level of position should occupy oﬃces of higher centrality and higher hierarchy in the structure diagram given in [1].

<!-- b000130 | prose | pages [5] -->
• Supervisors and executives should distribute as broadly as possible to ensure widespread supervisory and to maximally utilize the manager resource.

<!-- b000131 | prose | pages [5] -->
• Oﬃces of same level should have similar constitute for equality.

<!-- b000132 | prose | pages [5] -->
• Each executive should be matched with an administrative clerk as his/her secretary.

<!-- b000133 | prose | pages [5] -->
Evaluation of Employee Assignment 3.1.2

<!-- b000134 | prose | pages [5] -->
We ﬁrst quantify these principles as follows:

<!-- b000135 | prose | pages [5] -->
1. Principle of centrality: E1 = P Pi · CCi

<!-- b000136 | prose | pages [5] -->
2. Principle of hierarchy: E2 = P Pi · Li

<!-- b000137 | prose | pages [5] -->
3. Principle of equality: E3 = P Dj

<!-- b000138 | prose | pages [5] -->
4. Principle of uniformity: E4 = P Sj

<!-- b000139 | prose | pages [5] -->
Pi is the annual salary of an employee, which is a representative of his ability. Dj is diﬀerences between oﬃce j and other oﬃces of the same level. Sj is the number of same type of employees in oﬃce j . We hereby give the evaluation function:

<!-- b000140 | prose | pages [5] -->
Eval = α1E1 + α2E2 + α3E3 + α4E4 (1)

<!-- b000141 | prose | pages [5] -->
Because that E3 and E4 are too large, we choose α1 = 0.5, α2 = 0.5, α3 = −0.05, α4 = −0.05 after some experiments with random assignments. We plug these parameters back into Equation 1 to obtain the evaluation function.

<!-- b000142 | heading | pages [5] -->
Optimization Using Genetic Algorithm

<!-- b000143 | prose | pages [5] -->
3.1.3

<!-- b000144 | prose | pages [5] -->
We got an evaluation function in Section 3.1.2. Next we are going to ﬁnd its optimum, which in correspondence is the best assignment solution.

<!-- b000145 | prose | pages [5] -->
It is easy to show that this problem is a Combinatorial Optimization problem, for which search heuristics such as Genetic Algorithm and Tabu Search are proven to be more eﬃcient. We notice that the assignment itself is naturally a representation of the gene code, so we choose Genetic Equation 1). Algorithm to ﬁnd the maximum of the evaluation function (cf.

<!-- b000146 | prose | pages [5] -->
Thus the evolution process such as gene crossover can be easily achieved by swap employees in diﬀerent oﬃces. We implement the algorithm using MATLAB, initialize 500 random solutions and begin iteration. The algorithm produce a satisfactory result (cf. Figure 1).

<!-- b000147 | prose | pages [5] -->
We can see from Figure 1 that the algorithm not only assigned oﬃces according to staﬀhierarchy (i.e. superior oﬃces for staﬀof higher position like senior manager) but also incorporated uniformity and equality.

<!-- b000148 | furniture | pages [6] -->
Team # 33900

<!-- b000149 | furniture | pages [6] -->
Page 4 of 18

<!-- b000150 | prose | pages [6] -->
CEO CEO SM JM AC*2

<!-- b000151 | prose | pages [6] -->
CFO*

<!-- b000152 | prose | pages [6] -->
RESEARCH FACILITIES

<!-- b000153 | prose | pages [6] -->
VP VP

<!-- b000154 | prose | pages [6] -->
HR SALES

<!-- b000155 | prose | pages [6] -->
CIO* SM JM AC*2

<!-- b000156 | prose | pages [6] -->
SM AC EE*5

<!-- b000157 | prose | pages [6] -->
SM AC EE*2 SM AC EE*2

<!-- b000158 | prose | pages [6] -->
SM AC EE*2 SM AC EE*2

<!-- b000159 | prose | pages [6] -->
SM AC EE*5

<!-- b000160 | prose | pages [6] -->
PRODUCT* JM AC ES EE*4

<!-- b000161 | prose | pages [6] -->
DIRECTOR

<!-- b000162 | prose | pages [6] -->
DIRECTOR

<!-- b000163 | prose | pages [6] -->
DIRECTOR

<!-- b000164 | prose | pages [6] -->
IS*3  IE

<!-- b000165 | prose | pages [6] -->
ES IS*2 IE

<!-- b000166 | prose | pages [6] -->
IS*3  IE

<!-- b000167 | prose | pages [6] -->
DIRECTOR

<!-- b000168 | prose | pages [6] -->
DIRECTOR

<!-- b000169 | prose | pages [6] -->
DIRECTOR

<!-- b000170 | prose | pages [6] -->
IS*3  IE

<!-- b000171 | prose | pages [6] -->
IS*3  IE

<!-- b000172 | prose | pages [6] -->
IS*3  IE

<!-- b000173 | prose | pages [6] -->
BRANCH* IS       IE*6

<!-- b000174 | prose | pages [6] -->
Manager Offices* JM  AC  IS  EE*4

<!-- b000175 | prose | pages [6] -->
Branch Offices* ES IE*6

<!-- b000176 | caption | pages [6] -->
Figure 1. Organizational structure of ICM with all the employees assigned. Each block

<!-- b000177 | prose | pages [6] -->
represents an oﬃce (without *) or two divisions (with * and thicker border). Bold text is abbreviation of positions(SM for Senior Manager etc.).

<!-- b000178 | prose | pages [6] -->
Blocks with the same color and style share same constitute. Some blocks (Manager Oﬃces and Branch Oﬃces) are replaced by legend symbols for simpliﬁcation.

<!-- b000179 | prose | pages [6] -->
Building The Human Capital Network 3.2

<!-- b000180 | prose | pages [6] -->
We assigned the staﬀwith proper oﬃces in the above mentioned. Next we are going to build the network using this newly deducted information.

<!-- b000181 | prose | pages [6] -->
Building The Network of Personnel Relationship 3.2.1

<!-- b000182 | prose | pages [6] -->
Now that there are a grant total of N(N ⩽370) employees in ICM, which is corresponding to the N node in graph G, and we use vi(1 ⩽i ⩽N) to denote the ith node in G. In order to simplify the problem,we make a natural assumption that any pair of nodes vi and in G is connected if and only if the three following conditions are satisﬁed:

<!-- b000183 | prose | pages [6] -->
• vi and vj are in the same Branch or division;

<!-- b000184 | prose | pages [6] -->
• vi and vj are in the same level;

<!-- b000185 | prose | pages [6] -->
• vi and vj are respectively leaders of two oﬃce whose superior department are the same.

<!-- b000186 | prose | pages [6] -->
It’s worth noting that the relationship between any two persons in ICM varies, thus G is a weighted graph,the weight of edge eij reveals the level of relationship between node vi and node vj .Let N dimensional matrix A = (wij)N×N be the adjacency matrix of graph G ,we can conclude from previous discussion that:

<!-- b000187 | prose | pages [6] -->
 σ if vi and vj satisfy condition 2

<!-- b000188 | prose | pages [6] -->
wij =

<!-- b000189 | prose | pages [6] -->
if vi and vj satisfy condition 1 or 3 1

<!-- b000190 | prose | pages [6] -->
The graph G is illustrated in Figure 2.

<!-- b000191 | furniture | pages [7] -->
Team # 33900

<!-- b000192 | prose | pages [7] -->
Links within an office/division

<!-- b000193 | prose | pages [7] -->
IE38

<!-- b000194 | prose | pages [7] -->
IE37

<!-- b000195 | prose | pages [7] -->
IE28

<!-- b000196 | prose | pages [7] -->
IE24

<!-- b000197 | prose | pages [7] -->
IE41

<!-- b000198 | prose | pages [7] -->
IE40

<!-- b000199 | prose | pages [7] -->
IE25

<!-- b000200 | prose | pages [7] -->
Links between office heads

<!-- b000201 | prose | pages [7] -->
IE29

<!-- b000202 | prose | pages [7] -->
IE36

<!-- b000203 | prose | pages [7] -->
IE26

<!-- b000204 | prose | pages [7] -->
IE27

<!-- b000205 | prose | pages [7] -->
IE72

<!-- b000206 | prose | pages [7] -->
ES6

<!-- b000207 | prose | pages [7] -->
IE76

<!-- b000208 | prose | pages [7] -->
ES4

<!-- b000209 | prose | pages [7] -->
IE73

<!-- b000210 | prose | pages [7] -->
IE47

<!-- b000211 | prose | pages [7] -->
IE77

<!-- b000212 | prose | pages [7] -->
Inter-hierarchy

<!-- b000213 | prose | pages [7] -->
IE74

<!-- b000214 | prose | pages [7] -->
IE43

<!-- b000215 | prose | pages [7] -->
IE75

<!-- b000216 | prose | pages [7] -->
IE42

<!-- b000217 | prose | pages [7] -->
IE46

<!-- b000218 | prose | pages [7] -->
ES5

<!-- b000219 | prose | pages [7] -->
links

<!-- b000220 | prose | pages [7] -->
IE45

<!-- b000221 | prose | pages [7] -->
ES7

<!-- b000222 | prose | pages [7] -->
IE44

<!-- b000223 | prose | pages [7] -->
IE54

<!-- b000224 | prose | pages [7] -->
IE58

<!-- b000225 | prose | pages [7] -->
IE62

<!-- b000226 | prose | pages [7] -->
IE56

<!-- b000227 | prose | pages [7] -->
IE61

<!-- b000228 | prose | pages [7] -->
IE55

<!-- b000229 | prose | pages [7] -->
IE99

<!-- b000230 | prose | pages [7] -->
ES12

<!-- b000231 | prose | pages [7] -->
IE101

<!-- b000232 | prose | pages [7] -->
IE65

<!-- b000233 | prose | pages [7] -->
IE57

<!-- b000234 | prose | pages [7] -->
IE64

<!-- b000235 | prose | pages [7] -->
IE59

<!-- b000236 | prose | pages [7] -->
IE98

<!-- b000237 | prose | pages [7] -->
IE63

<!-- b000238 | prose | pages [7] -->
IE60

<!-- b000239 | prose | pages [7] -->
IE100

<!-- b000240 | prose | pages [7] -->
IE111

<!-- b000241 | prose | pages [7] -->
ES9

<!-- b000242 | prose | pages [7] -->
IE109

<!-- b000243 | prose | pages [7] -->
ES10

<!-- b000244 | prose | pages [7] -->
ES16

<!-- b000245 | prose | pages [7] -->
IE113 IE112

<!-- b000246 | prose | pages [7] -->
IE108

<!-- b000247 | prose | pages [7] -->
IE68

<!-- b000248 | prose | pages [7] -->
IE104

<!-- b000249 | prose | pages [7] -->
ES18

<!-- b000250 | prose | pages [7] -->
IE103

<!-- b000251 | prose | pages [7] -->
ES11

<!-- b000252 | prose | pages [7] -->
IE110

<!-- b000253 | prose | pages [7] -->
IE67

<!-- b000254 | prose | pages [7] -->
ES17

<!-- b000255 | prose | pages [7] -->
ES8

<!-- b000256 | prose | pages [7] -->
IE71

<!-- b000257 | prose | pages [7] -->
IE51

<!-- b000258 | prose | pages [7] -->
ES13

<!-- b000259 | prose | pages [7] -->
IE66

<!-- b000260 | prose | pages [7] -->
IE102

<!-- b000261 | prose | pages [7] -->
IE81

<!-- b000262 | prose | pages [7] -->
IE105

<!-- b000263 | prose | pages [7] -->
IE48

<!-- b000264 | prose | pages [7] -->
IE83

<!-- b000265 | prose | pages [7] -->
IE106

<!-- b000266 | prose | pages [7] -->
ES19

<!-- b000267 | prose | pages [7] -->
IE49

<!-- b000268 | prose | pages [7] -->
IE13

<!-- b000269 | prose | pages [7] -->
IE70

<!-- b000270 | prose | pages [7] -->
IE53

<!-- b000271 | prose | pages [7] -->
IE114

<!-- b000272 | prose | pages [7] -->
IE14

<!-- b000273 | prose | pages [7] -->
IE69

<!-- b000274 | prose | pages [7] -->
IE78

<!-- b000275 | prose | pages [7] -->
IE118

<!-- b000276 | prose | pages [7] -->
IE115

<!-- b000277 | prose | pages [7] -->
IE82

<!-- b000278 | prose | pages [7] -->
IE17

<!-- b000279 | prose | pages [7] -->
IE117

<!-- b000280 | prose | pages [7] -->
IE10

<!-- b000281 | prose | pages [7] -->
IE12

<!-- b000282 | prose | pages [7] -->
IE52

<!-- b000283 | prose | pages [7] -->
IE119

<!-- b000284 | prose | pages [7] -->
IE50

<!-- b000285 | prose | pages [7] -->
ES2

<!-- b000286 | prose | pages [7] -->
IE16

<!-- b000287 | prose | pages [7] -->
IE79

<!-- b000288 | prose | pages [7] -->
IE11

<!-- b000289 | prose | pages [7] -->
IE80

<!-- b000290 | prose | pages [7] -->
IE15

<!-- b000291 | prose | pages [7] -->
ES1

<!-- b000292 | prose | pages [7] -->
IE19

<!-- b000293 | prose | pages [7] -->
ES3

<!-- b000294 | prose | pages [7] -->
IE22

<!-- b000295 | prose | pages [7] -->
ES0

<!-- b000296 | prose | pages [7] -->
IE18

<!-- b000297 | prose | pages [7] -->
IE4

<!-- b000298 | prose | pages [7] -->
IE23

<!-- b000299 | prose | pages [7] -->
IE5

<!-- b000300 | prose | pages [7] -->
IE21

<!-- b000301 | prose | pages [7] -->
IE0

<!-- b000302 | prose | pages [7] -->
IE139

<!-- b000303 | prose | pages [7] -->
IE141

<!-- b000304 | prose | pages [7] -->
IE126

<!-- b000305 | prose | pages [7] -->
IE20

<!-- b000306 | prose | pages [7] -->
IE3

<!-- b000307 | prose | pages [7] -->
IE128

<!-- b000308 | prose | pages [7] -->
ES23

<!-- b000309 | prose | pages [7] -->
IE143

<!-- b000310 | prose | pages [7] -->
IE1

<!-- b000311 | prose | pages [7] -->
ES21

<!-- b000312 | prose | pages [7] -->
IE142

<!-- b000313 | prose | pages [7] -->
IE2

<!-- b000314 | prose | pages [7] -->
IE131

<!-- b000315 | prose | pages [7] -->
IE130

<!-- b000316 | prose | pages [7] -->
IE138

<!-- b000317 | prose | pages [7] -->
IE140

<!-- b000318 | prose | pages [7] -->
IE127

<!-- b000319 | prose | pages [7] -->
IE129

<!-- b000320 | prose | pages [7] -->
ES15

<!-- b000321 | prose | pages [7] -->
Branch L

<!-- b000322 | prose | pages [7] -->
ES22

<!-- b000323 | prose | pages [7] -->
IE95

<!-- b000324 | prose | pages [7] -->
IE90

<!-- b000325 | prose | pages [7] -->
IE93

<!-- b000326 | prose | pages [7] -->
ES20

<!-- b000327 | prose | pages [7] -->
IE91

<!-- b000328 | prose | pages [7] -->
IE136

<!-- b000329 | prose | pages [7] -->
IE134

<!-- b000330 | prose | pages [7] -->
IE92

<!-- b000331 | prose | pages [7] -->
IE94

<!-- b000332 | prose | pages [7] -->
IE137

<!-- b000333 | prose | pages [7] -->
IE135

<!-- b000334 | prose | pages [7] -->
IE123

<!-- b000335 | prose | pages [7] -->
ES14

<!-- b000336 | prose | pages [7] -->
IE120

<!-- b000337 | prose | pages [7] -->
IE132

<!-- b000338 | prose | pages [7] -->
IE125

<!-- b000339 | prose | pages [7] -->
IE133

<!-- b000340 | prose | pages [7] -->
IE121

<!-- b000341 | prose | pages [7] -->
IE86

<!-- b000342 | prose | pages [7] -->
IE88

<!-- b000343 | prose | pages [7] -->
IE124

<!-- b000344 | prose | pages [7] -->
IE122

<!-- b000345 | prose | pages [7] -->
IE85

<!-- b000346 | prose | pages [7] -->
IE87

<!-- b000347 | prose | pages [7] -->
IE89

<!-- b000348 | prose | pages [7] -->
IE84

<!-- b000349 | furniture | pages [7] -->
Page 5 of 18

<!-- b000350 | prose | pages [7] -->
top-level

<!-- b000351 | prose | pages [7] -->
mid-top

<!-- b000352 | prose | pages [7] -->
IE39 IE39

<!-- b000353 | prose | pages [7] -->
mid-bottom

<!-- b000354 | prose | pages [7] -->
mid-level

<!-- b000355 | prose | pages [7] -->
bottom-level

<!-- b000356 | prose | pages [7] -->
IE32

<!-- b000357 | prose | pages [7] -->
IE31 IE31

<!-- b000358 | prose | pages [7] -->
IE34

<!-- b000359 | prose | pages [7] -->
EE59

<!-- b000360 | prose | pages [7] -->
IE33 IE33

<!-- b000361 | prose | pages [7] -->
EE61

<!-- b000362 | prose | pages [7] -->
EE58

<!-- b000363 | prose | pages [7] -->
IE30

<!-- b000364 | prose | pages [7] -->
IE35 IE35

<!-- b000365 | prose | pages [7] -->
EE60

<!-- b000366 | prose | pages [7] -->
EE62

<!-- b000367 | prose | pages [7] -->
EE71

<!-- b000368 | prose | pages [7] -->
EE64

<!-- b000369 | prose | pages [7] -->
AC12

<!-- b000370 | prose | pages [7] -->
EE63

<!-- b000371 | prose | pages [7] -->
EE70

<!-- b000372 | prose | pages [7] -->
EE72

<!-- b000373 | prose | pages [7] -->
Director 2

<!-- b000374 | prose | pages [7] -->
EE65

<!-- b000375 | prose | pages [7] -->
IS19

<!-- b000376 | prose | pages [7] -->
EE73

<!-- b000377 | prose | pages [7] -->
JM12

<!-- b000378 | prose | pages [7] -->
AC13

<!-- b000379 | prose | pages [7] -->
EE99

<!-- b000380 | prose | pages [7] -->
IS20

<!-- b000381 | prose | pages [7] -->
JM13

<!-- b000382 | prose | pages [7] -->
IS22

<!-- b000383 | prose | pages [7] -->
AC15

<!-- b000384 | prose | pages [7] -->
EE95

<!-- b000385 | prose | pages [7] -->
JM15

<!-- b000386 | prose | pages [7] -->
EE2

<!-- b000387 | prose | pages [7] -->
IE145

<!-- b000388 | prose | pages [7] -->
EE96 EE97

<!-- b000389 | prose | pages [7] -->
IS21

<!-- b000390 | prose | pages [7] -->
JM14

<!-- b000391 | prose | pages [7] -->
SM5

<!-- b000392 | prose | pages [7] -->
IE97 IE97

<!-- b000393 | prose | pages [7] -->
EE89

<!-- b000394 | prose | pages [7] -->
EE67

<!-- b000395 | prose | pages [7] -->
EE69

<!-- b000396 | prose | pages [7] -->
EE81

<!-- b000397 | prose | pages [7] -->
EE98

<!-- b000398 | prose | pages [7] -->
EE3

<!-- b000399 | prose | pages [7] -->
EE79

<!-- b000400 | prose | pages [7] -->
AC27

<!-- b000401 | prose | pages [7] -->
SM7

<!-- b000402 | prose | pages [7] -->
IE96 IE96

<!-- b000403 | prose | pages [7] -->
EE66

<!-- b000404 | prose | pages [7] -->
EE68

<!-- b000405 | prose | pages [7] -->
EE88

<!-- b000406 | prose | pages [7] -->
EE78

<!-- b000407 | prose | pages [7] -->
AC14

<!-- b000408 | prose | pages [7] -->
EE80

<!-- b000409 | prose | pages [7] -->
AC25

<!-- b000410 | prose | pages [7] -->
IS24

<!-- b000411 | prose | pages [7] -->
JM17

<!-- b000412 | prose | pages [7] -->
AC17

<!-- b000413 | prose | pages [7] -->
EE8

<!-- b000414 | prose | pages [7] -->
IS1 IS1

<!-- b000415 | prose | pages [7] -->
EE9

<!-- b000416 | prose | pages [7] -->
EE91

<!-- b000417 | prose | pages [7] -->
IS2 IS2

<!-- b000418 | prose | pages [7] -->
IE148

<!-- b000419 | prose | pages [7] -->
IE107 IE107

<!-- b000420 | prose | pages [7] -->
EE30

<!-- b000421 | prose | pages [7] -->
EE12

<!-- b000422 | prose | pages [7] -->
EE32

<!-- b000423 | prose | pages [7] -->
EE41

<!-- b000424 | prose | pages [7] -->
EE90

<!-- b000425 | prose | pages [7] -->
EE40

<!-- b000426 | prose | pages [7] -->
EE19

<!-- b000427 | prose | pages [7] -->
EE94

<!-- b000428 | prose | pages [7] -->
EE13

<!-- b000429 | prose | pages [7] -->
EE20

<!-- b000430 | prose | pages [7] -->
IS4 IS4

<!-- b000431 | prose | pages [7] -->
IE6 IE6

<!-- b000432 | prose | pages [7] -->
EE39

<!-- b000433 | prose | pages [7] -->
EE10

<!-- b000434 | prose | pages [7] -->
AC26

<!-- b000435 | prose | pages [7] -->
EE33

<!-- b000436 | prose | pages [7] -->
SM6

<!-- b000437 | prose | pages [7] -->
EE5

<!-- b000438 | prose | pages [7] -->
EE21

<!-- b000439 | prose | pages [7] -->
VP

<!-- b000440 | prose | pages [7] -->
EE31

<!-- b000441 | prose | pages [7] -->
AC7

<!-- b000442 | prose | pages [7] -->
EE38

<!-- b000443 | prose | pages [7] -->
EE93

<!-- b000444 | prose | pages [7] -->
IE8 IE8

<!-- b000445 | prose | pages [7] -->
EE92

<!-- b000446 | prose | pages [7] -->
IE116 IE116

<!-- b000447 | prose | pages [7] -->
IE146 IE146

<!-- b000448 | prose | pages [7] -->
AC5

<!-- b000449 | prose | pages [7] -->
AC0

<!-- b000450 | prose | pages [7] -->
EE11

<!-- b000451 | prose | pages [7] -->
AC2

<!-- b000452 | prose | pages [7] -->
IS14

<!-- b000453 | prose | pages [7] -->
IS12

<!-- b000454 | prose | pages [7] -->
JM7

<!-- b000455 | prose | pages [7] -->
JM5

<!-- b000456 | prose | pages [7] -->
EE18

<!-- b000457 | prose | pages [7] -->
EE4

<!-- b000458 | prose | pages [7] -->
IE7 IE7

<!-- b000459 | prose | pages [7] -->
AC20

<!-- b000460 | prose | pages [7] -->
IS6 IS6

<!-- b000461 | prose | pages [7] -->
IS9

<!-- b000462 | prose | pages [7] -->
CEO

<!-- b000463 | prose | pages [7] -->
IS13JM6

<!-- b000464 | prose | pages [7] -->
JM0

<!-- b000465 | prose | pages [7] -->
JM2

<!-- b000466 | prose | pages [7] -->
IS7

<!-- b000467 | prose | pages [7] -->
IE9 IE9

<!-- b000468 | prose | pages [7] -->
JM19 SM1 ES24 ES24

<!-- b000469 | prose | pages [7] -->
IS0

<!-- b000470 | prose | pages [7] -->
IS11 JM4

<!-- b000471 | prose | pages [7] -->
AC18

<!-- b000472 | prose | pages [7] -->
EE35 EE36

<!-- b000473 | prose | pages [7] -->
EE82

<!-- b000474 | prose | pages [7] -->
AC6

<!-- b000475 | prose | pages [7] -->
JM18

<!-- b000476 | prose | pages [7] -->
AC21

<!-- b000477 | prose | pages [7] -->
IE149 IE149

<!-- b000478 | prose | pages [7] -->
SM0

<!-- b000479 | prose | pages [7] -->
IS5 IS5

<!-- b000480 | prose | pages [7] -->
SM2

<!-- b000481 | prose | pages [7] -->
AC19

<!-- b000482 | prose | pages [7] -->
IS8

<!-- b000483 | prose | pages [7] -->
AC22

<!-- b000484 | prose | pages [7] -->
JM1

<!-- b000485 | prose | pages [7] -->
EE26 AC4

<!-- b000486 | prose | pages [7] -->
EE85

<!-- b000487 | prose | pages [7] -->
EE34

<!-- b000488 | prose | pages [7] -->
IS10

<!-- b000489 | prose | pages [7] -->
EE17

<!-- b000490 | prose | pages [7] -->
SM3

<!-- b000491 | prose | pages [7] -->
EE37

<!-- b000492 | prose | pages [7] -->
JM3

<!-- b000493 | prose | pages [7] -->
EE83

<!-- b000494 | prose | pages [7] -->
AC1

<!-- b000495 | prose | pages [7] -->
IS3 IS3

<!-- b000496 | prose | pages [7] -->
EE28 EE29

<!-- b000497 | prose | pages [7] -->
EE84

<!-- b000498 | prose | pages [7] -->
AC23

<!-- b000499 | prose | pages [7] -->
EE1

<!-- b000500 | prose | pages [7] -->
EE15

<!-- b000501 | prose | pages [7] -->
AC3

<!-- b000502 | prose | pages [7] -->
EE23

<!-- b000503 | prose | pages [7] -->
EE16

<!-- b000504 | prose | pages [7] -->
EE27

<!-- b000505 | prose | pages [7] -->
IE144 IE144

<!-- b000506 | prose | pages [7] -->
EE14

<!-- b000507 | prose | pages [7] -->
EE25 EE24

<!-- b000508 | prose | pages [7] -->
EE0

<!-- b000509 | prose | pages [7] -->
EE22

<!-- b000510 | prose | pages [7] -->
IS23

<!-- b000511 | prose | pages [7] -->
JM16 AC16

<!-- b000512 | prose | pages [7] -->
EE105

<!-- b000513 | prose | pages [7] -->
AC29

<!-- b000514 | prose | pages [7] -->
EE7

<!-- b000515 | prose | pages [7] -->
SM9

<!-- b000516 | prose | pages [7] -->
EE107

<!-- b000517 | prose | pages [7] -->
EE77

<!-- b000518 | prose | pages [7] -->
IE147 IE147

<!-- b000519 | prose | pages [7] -->
EE76

<!-- b000520 | prose | pages [7] -->
EE108

<!-- b000521 | prose | pages [7] -->
EE52

<!-- b000522 | prose | pages [7] -->
AC10

<!-- b000523 | prose | pages [7] -->
EE6

<!-- b000524 | prose | pages [7] -->
EE109

<!-- b000525 | prose | pages [7] -->
EE74 EE75

<!-- b000526 | prose | pages [7] -->
AC24

<!-- b000527 | prose | pages [7] -->
EE53

<!-- b000528 | prose | pages [7] -->
EE106

<!-- b000529 | prose | pages [7] -->
EE50

<!-- b000530 | prose | pages [7] -->
EE87

<!-- b000531 | prose | pages [7] -->
Internet

<!-- b000532 | prose | pages [7] -->
EE51

<!-- b000533 | prose | pages [7] -->
IS17 JM10

<!-- b000534 | prose | pages [7] -->
SM4

<!-- b000535 | prose | pages [7] -->
EE86

<!-- b000536 | prose | pages [7] -->
IS15 JM8

<!-- b000537 | prose | pages [7] -->
AC8

<!-- b000538 | prose | pages [7] -->
SM8

<!-- b000539 | prose | pages [7] -->
JM11

<!-- b000540 | prose | pages [7] -->
IS18

<!-- b000541 | prose | pages [7] -->
AC28

<!-- b000542 | prose | pages [7] -->
EE42

<!-- b000543 | prose | pages [7] -->
AC11

<!-- b000544 | prose | pages [7] -->
JM9

<!-- b000545 | prose | pages [7] -->
IS16

<!-- b000546 | prose | pages [7] -->
EE102

<!-- b000547 | prose | pages [7] -->
EE44

<!-- b000548 | prose | pages [7] -->
EE103

<!-- b000549 | prose | pages [7] -->
EE43

<!-- b000550 | prose | pages [7] -->
EE55

<!-- b000551 | prose | pages [7] -->
EE104

<!-- b000552 | prose | pages [7] -->
AC9

<!-- b000553 | prose | pages [7] -->
EE57

<!-- b000554 | prose | pages [7] -->
EE45

<!-- b000555 | prose | pages [7] -->
EE101 EE100

<!-- b000556 | prose | pages [7] -->
EE54

<!-- b000557 | prose | pages [7] -->
EE56

<!-- b000558 | prose | pages [7] -->
EE46

<!-- b000559 | prose | pages [7] -->
EE49

<!-- b000560 | prose | pages [7] -->
EE47

<!-- b000561 | prose | pages [7] -->
EE48

<!-- b000562 | caption | pages [7] -->
Figure 2. Personnel Relationship Network of ICM. The color denotes oﬃce hierarchy.

<!-- b000563 | prose | pages [7] -->
Small clusters of oﬃces and three types of edges are labeled. Some edges are omitted for conciseness.

<!-- b000564 | prose | pages [7] -->
Building the Organizational Network 3.2.2

<!-- b000565 | prose | pages [7] -->
Also we can get the Organizational Network. The procedures of forming g can be imple- mented as follows:

<!-- b000566 | prose | pages [7] -->
1. add all staﬀoﬃces and divisions to g as nodes.

<!-- b000567 | prose | pages [7] -->
2. add hierarchy chains as directed edges, from lower hierarchy to higher.

<!-- b000568 | prose | pages [7] -->
3. for all nodes pairs, if the two nodes have the same hierarchical father, add a bi- directed edge between them.

<!-- b000569 | prose | pages [7] -->
4. add a sink node to graph, then connect all nodes except the sink node to the sink node with a bi-directed edge, which is in convenience for leader rank.

<!-- b000570 | prose | pages [7] -->
Graph g is a directed graph (cf. Figure 3). The calculated LeaderRank Value is illustrated by the node size. Note that LeaderRank Value is not always consistent with hierarchy.

<!-- b000571 | furniture | pages [8] -->
Team # 33900

<!-- b000572 | prose | pages [8] -->
Branch J

<!-- b000573 | furniture | pages [8] -->
Page 6 of 18

<!-- b000574 | prose | pages [8] -->
top-level

<!-- b000575 | prose | pages [8] -->
mid-top

<!-- b000576 | prose | pages [8] -->
Branch B

<!-- b000577 | prose | pages [8] -->
Branch I

<!-- b000578 | prose | pages [8] -->
Branch L

<!-- b000579 | prose | pages [8] -->
Director 5

<!-- b000580 | prose | pages [8] -->
Branch K

<!-- b000581 | prose | pages [8] -->
mid-bottom

<!-- b000582 | prose | pages [8] -->
mid-level

<!-- b000583 | prose | pages [8] -->
Branch A

<!-- b000584 | prose | pages [8] -->
bottom-level

<!-- b000585 | prose | pages [8] -->
Director 1

<!-- b000586 | prose | pages [8] -->
Director 6

<!-- b000587 | prose | pages [8] -->
Branch C

<!-- b000588 | prose | pages [8] -->
CIO

<!-- b000589 | prose | pages [8] -->
Plant Blue

<!-- b000590 | prose | pages [8] -->
CFO

<!-- b000591 | prose | pages [8] -->
Production Manager

<!-- b000592 | prose | pages [8] -->
Director 2

<!-- b000593 | prose | pages [8] -->
Branch D

<!-- b000594 | prose | pages [8] -->
Director 4

<!-- b000595 | prose | pages [8] -->
Director 3

<!-- b000596 | prose | pages [8] -->
Facilities

<!-- b000597 | prose | pages [8] -->
Plant Green

<!-- b000598 | prose | pages [8] -->
CEO

<!-- b000599 | prose | pages [8] -->
VP VP

<!-- b000600 | prose | pages [8] -->
Research

<!-- b000601 | prose | pages [8] -->
Networks

<!-- b000602 | prose | pages [8] -->
HR

<!-- b000603 | prose | pages [8] -->
Information

<!-- b000604 | prose | pages [8] -->
Program Manager

<!-- b000605 | prose | pages [8] -->
Branch G

<!-- b000606 | prose | pages [8] -->
Branch E

<!-- b000607 | prose | pages [8] -->
Branch H

<!-- b000608 | prose | pages [8] -->
Branch F

<!-- b000609 | prose | pages [8] -->
Sales Marketing

<!-- b000610 | prose | pages [8] -->
Regional

<!-- b000611 | prose | pages [8] -->
World Wide

<!-- b000612 | prose | pages [8] -->
Internet

<!-- b000613 | caption | pages [8] -->
Figure 3. Organizational Network of ICM. The color denotes oﬃce level. The size of

<!-- b000614 | prose | pages [8] -->
the node denotes the LeaderRank Value. Note that the LeaderRank Value of Production Manager is higher than that of VP despite of their hierarchical relations.

<!-- b000615 | prose | pages [8] -->
Evaluating Turnover Intention of Employee 3.3

<!-- b000616 | prose | pages [8] -->
Cotton et al. found that factors such as pay and employment perception are the most highly reliable correlates of turnover [6]. The factors can be divided into External Factors and Internal Factors. We adopt his conclusion and further specify them into three basic elements: salary, level of position, promotion prospect. We also introduce the inﬂuence of other people’s turnover behavior, summing up to four elements denoted by C1 , C2 , C3 , C4 for quantiﬁcation.

<!-- b000617 | prose | pages [8] -->
In order to ﬁnd the employee with the highest turnover probability, we use AHP to evaluate the contribution of each factor to turnover intention.

<!-- b000618 | prose | pages [8] -->
3.3.1 Factor of Turnover Contagion

<!-- b000619 | prose | pages [8] -->
Hereinbefore we assumed that if one employee left, other employees close to him are inﬂuenced and are more likely to ‘churn’ (cf. Section 2.1). We quantify the level of inﬂuence by introducing Structural Equivalence [15] as closeness. We assume that the level of inﬂuence of one’s turnover to another’s intention is positively correlated with Structural Equivalence (in other words, similarity).

<!-- b000620 | prose | pages [8] -->
We adopt the RA Index [16] in weighted graph to measure the similarity between nodes. Consider a pair of nodes, x and y which are not directly connected. If node x can send some information to y with their common neighbors playing the role of transmitters, then they would share some similarity. We revise the original RA Index and deﬁne the similarity between x and y as the amount of resource y received from x :

<!-- b000621 | prose | pages [8] -->
X

<!-- b000622 | prose | pages [8] -->
sxy =

<!-- b000623 | prose | pages [8] -->
wxz + wyz

<!-- b000624 | prose | pages [8] -->
k(z)

<!-- b000625 | prose | pages [8] -->
z∈Γ(x)∩Γ(y)

<!-- b000626 | furniture | pages [9] -->
Team # 33900

<!-- b000627 | furniture | pages [9] -->
Page 7 of 18

<!-- b000628 | prose | pages [9] -->
where Γ(i) is the set of neighbors of x and k(i) the degree of x , and we can develop the expression of C1i :

<!-- b000629 | prose | pages [9] -->
X

<!-- b000630 | prose | pages [9] -->
e−β(t−tj)

<!-- b000631 | prose | pages [9] -->
1 + e−β(t−tj) sij

<!-- b000632 | prose | pages [9] -->
C1i =

<!-- b000633 | prose | pages [9] -->
aj∈S

<!-- b000634 | prose | pages [9] -->
where S denotes the set of former employees who have churned at moment ti . We use Logistic Curve to describe former employee’s impact due to the attenuation eﬀect.

<!-- b000635 | prose | pages [9] -->
3.3.2 Factor of Employee Centrality

<!-- b000636 | prose | pages [9] -->
Individuals with greater centrality in a communication network are less likely to turnover due to the information and social support beneﬁts provided by peers in the workplace [15].

<!-- b000637 | prose | pages [9] -->
In our model the overall importance of an employee is determined by his centrality in graph G (cf. Figure 2) and the importance of his department in graph g (cf. Figure 3). Because Closeness Centrality can be regarded as a measure of how long it will take to spread information from certain node to all other nodes and is widely used in Social Network Analysis [17], we choose Closeness Centrality as the measurement.

<!-- b000638 | prose | pages [9] -->
And the importance of his department in graph g is determined by the LeaderRank Value of the oﬃce.

<!-- b000639 | prose | pages [9] -->
For each node in graph G , we calculate its Closeness Centrality as follows: For node i , calculate mean distance between it and every other node as di :

<!-- b000640 | prose | pages [9] -->
di = 1

<!-- b000641 | prose | pages [9] -->
N X

<!-- b000642 | prose | pages [9] -->
dij

<!-- b000643 | prose | pages [9] -->
n n

<!-- b000644 | prose | pages [9] -->
j=1

<!-- b000645 | prose | pages [9] -->
where dij is the topological distance between i and j . The reciprocal of di is deﬁned as Closeness Centrality:

<!-- b000646 | prose | pages [9] -->
CCi = 1

<!-- b000647 | prose | pages [9] -->
di

<!-- b000648 | prose | pages [9] -->
N =

<!-- b000649 | prose | pages [9] -->
NP

<!-- b000650 | prose | pages [9] -->
dij

<!-- b000651 | prose | pages [9] -->
j=1

<!-- b000652 | prose | pages [9] -->
For each oﬃce in directed graph g , we calculate the LeaderRank Value LR as follows:

<!-- b000653 | prose | pages [9] -->
To conclude we give the expression of C2i:

<!-- b000654 | prose | pages [9] -->
C2i = 1 LR × CCi

<!-- b000655 | prose | pages [9] -->
Factors of Salary and Promotion Prospect 3.3.3

<!-- b000656 | prose | pages [9] -->
We assume that the salary is the same among same hierarchy, so we quantify the factor of salary as follows:

<!-- b000657 | prose | pages [9] -->


<!-- b000658 | prose | pages [9] -->
node i belongs to top hierarchy ξ1

<!-- b000659 | prose | pages [9] -->


<!-- b000660 | prose | pages [9] -->
node i belongs to mid hierarchy ξ2

<!-- b000661 | prose | pages [9] -->
C3i =

<!-- b000662 | prose | pages [9] -->
node i belongs to bottom hierarchy ξ3

<!-- b000663 | prose | pages [9] -->


<!-- b000664 | furniture | pages [10] -->
Team # 33900

<!-- b000665 | furniture | pages [10] -->
Page 8 of 18

<!-- b000666 | prose | pages [10] -->
Similarly, assuming that the promotion prospect is the same, we give:

<!-- b000667 | prose | pages [10] -->


<!-- b000668 | prose | pages [10] -->
node i belongs to top hierarchy ψ1

<!-- b000669 | prose | pages [10] -->


<!-- b000670 | prose | pages [10] -->
node i belongs to mid hierarchy ψ2

<!-- b000671 | prose | pages [10] -->
C4i =

<!-- b000672 | prose | pages [10] -->
node i belongs to bottom hierarchy ψ3

<!-- b000673 | prose | pages [10] -->


<!-- b000674 | prose | pages [10] -->
We choose ξ1 = 1 , ξ2 = 0 , ξ3 = 0 on account of the relatively low CEO-to-worker salary ratio. And because that employees in the middle ‘feel stuck in their jobs with little opportunity to advance’ [1], we choose ψ1 = 0 , ψ2 = 1 , ψ3 = 0 .

<!-- b000675 | prose | pages [10] -->
3.3.4 Evaluation using AHP]

<!-- b000676 | prose | pages [10] -->
We gave the quantiﬁcation of factors in the above text. evaluation is illustrated in Figure 4.

<!-- b000677 | prose | pages [10] -->
Our AHP hierarchy for this

<!-- b000678 | prose | pages [10] -->
Turnover Intention (T)

<!-- b000679 | prose | pages [10] -->
Impact from Others (C1) Employee Centrality (C2) Salary (C3) Promotion Prospect (C4)

<!-- b000680 | prose | pages [10] -->
……… Employee3 Employee1 Employee2 ...

<!-- b000681 | caption | pages [10] -->
Figure 4. The AHP hierarchy for determine employee’s turnover intention.

<!-- b000682 | prose | pages [10] -->
Combining those four factors using AHP, we give the following pairwise comparison matrix:

<!-- b000683 | prose | pages [10] -->
C1

<!-- b000684 | prose | pages [10] -->


<!-- b000685 | prose | pages [10] -->
1

<!-- b000686 | prose | pages [10] -->
C1 C2

<!-- b000687 | prose | pages [10] -->
1/3

<!-- b000688 | prose | pages [10] -->
 

<!-- b000689 | prose | pages [10] -->
1/2

<!-- b000690 | prose | pages [10] -->
C3

<!-- b000691 | prose | pages [10] -->


<!-- b000692 | prose | pages [10] -->
3

<!-- b000693 | prose | pages [10] -->
C4 C2 C3 C4

<!-- b000694 | prose | pages [10] -->


<!-- b000695 | prose | pages [10] -->
2 3 1/2 1 1 1/2

<!-- b000696 | prose | pages [10] -->
 

<!-- b000697 | prose | pages [10] -->
1 1 1/3

<!-- b000698 | prose | pages [10] -->


<!-- b000699 | prose | pages [10] -->
2 2 1

<!-- b000700 | prose | pages [10] -->
Thus we have the evaluation function expressed as Equation (4), in which the pa- rameters α1, α2, α3, α4 are to be determined.

<!-- b000701 | prose | pages [10] -->
T = α1C1 + α2C2 + α3C3 + α4C4 (2)

<!-- b000702 | prose | pages [10] -->
We calculate the parameters using MATLAB, and get α1 = 0.3084, α2 = 0.1482, α3 = 0.1445, α4 = 0.3989. We test the consistency of our AHP in the following two aspects:

<!-- b000703 | prose | pages [10] -->
1. The Consistency Index CI = (λmax −n)/(n−1) should be close to zero. With n = 4 we get CI = 0.0045, which is very close to zero.

<!-- b000704 | furniture | pages [11] -->
Team # 33900

<!-- b000705 | furniture | pages [11] -->
Page 9 of 18

<!-- b000706 | prose | pages [11] -->
2. The Consistency Ratio CR = CI/RI should be less than 0.1. With n = 4 we get RI = 0.9 and CR = 0.05 < 0.1.

<!-- b000707 | prose | pages [11] -->
The test result displays perfectly acceptable consistency.

<!-- b000708 | prose | pages [11] -->
Productivity and Costs of HCM 3.4

<!-- b000709 | prose | pages [11] -->
The contribution of employee to the company is intuitively relevant to the following three factors:

<!-- b000710 | prose | pages [11] -->
1. The ability of the employee, represented by his wage.

<!-- b000711 | prose | pages [11] -->
2. The eﬃciency of the employee (denoted by ei). It is trivial to see that eﬃciency is inversely proportional to turnover intention.

<!-- b000712 | prose | pages [11] -->
3. The importance of the oﬃce in which the employee works. This factor is introduced by modifying coeﬃcient λi and is equal to LeaderRank Value of graph g .

<!-- b000713 | prose | pages [11] -->
Thus we have productivity expression as follows:

<!-- b000714 | prose | pages [11] -->
Productivity =

<!-- b000715 | prose | pages [11] -->
X

<!-- b000716 | prose | pages [11] -->
λi × Pi × ei (3)

<!-- b000717 | prose | pages [11] -->
i

<!-- b000718 | prose | pages [11] -->
The overall recruiting costs of ICM is given by the summation of new workers’ median recruit costs:

<!-- b000719 | prose | pages [11] -->
X

<!-- b000720 | prose | pages [11] -->
RCall =

<!-- b000721 | prose | pages [11] -->
j

<!-- b000722 | prose | pages [11] -->
X

<!-- b000723 | prose | pages [11] -->
MRj

<!-- b000724 | prose | pages [11] -->
Nj∈NW

<!-- b000725 | prose | pages [11] -->
where RCall is for overall recruiting costs, Nj represents a node of level j, NW indicates the new worker set, and MRj is the median recruiting costs of level j. The training costs is related to the current number of workers in diﬀerent levels, which are given by:

<!-- b000726 | prose | pages [11] -->
X

<!-- b000727 | prose | pages [11] -->
TCall =

<!-- b000728 | prose | pages [11] -->
j

<!-- b000729 | prose | pages [11] -->
X

<!-- b000730 | prose | pages [11] -->
MTj

<!-- b000731 | prose | pages [11] -->
Nj∈Nodes

<!-- b000732 | prose | pages [11] -->
where TCall is for overall recruiting costs, Nj represents a node of level j, Nodes indicates the set of all nodes, and MTj is the median training costs of level j .

<!-- b000733 | prose | pages [11] -->
Dynamics of Human Capital Network 4

<!-- b000734 | prose | pages [11] -->
We further analyze the dynamic characteristics of HCN. The dynamic process imcludes churns, promotions and recruits. The churn exhibits impacts on linked nodes as parts of the turnover intention. With stochastic process the recruits and promotions can be regarded as random variables following to speciﬁc distributions. Using the model

<!-- b000735 | furniture | pages [12] -->
Team # 33900

<!-- b000736 | prose | pages [12] -->
4.1 Process of Turnover

<!-- b000737 | furniture | pages [12] -->
Page 10 of 18

<!-- b000738 | prose | pages [12] -->
The process of turnover is based on the turnover intention analysis in Section 3. The nodes to churn is chosen randomly with their turnover intention as weight. By approxi- mating the poisson distribution can best describe churns distribution as follows:

<!-- b000739 | prose | pages [12] -->
P(nch = k) = e−λλk

<!-- b000740 | prose | pages [12] -->
(4) k!

<!-- b000741 | prose | pages [12] -->
where represents the number of churns. If the time unit is month, we have Eventually, A churned worker loses his links and is deleted from the G graph.

<!-- b000742 | prose | pages [12] -->
4.2 Process of Promotion

<!-- b000743 | prose | pages [12] -->
We aim to distinguish qualiﬁed workers in the company, hence we choose the service time and the work experience as two diciplines in promoting. The service time of a worker is the duration he stays in this company. The service time requirments with respect to levels of positions are shown as Table 2.

<!-- b000744 | caption | pages [12] -->
Table 2. Service Time Requirements for diﬀerent Level of Positions.

<!-- b000745 | prose | pages [12] -->
Level of Position

<!-- b000746 | prose | pages [12] -->
Service Time Requirements

<!-- b000747 | prose | pages [12] -->
SM JM ES IS EE IE

<!-- b000748 | prose | pages [12] -->
8 5 3 2 1 0

<!-- b000749 | prose | pages [12] -->
Note that the promotion of Administrative Clerk is ignored in the promotion process because of the diﬀerences in jobs especially in a production-oriented company. We assume that worker with service-time beyond comparison in Table 2 be cropped to the maximum requirements initially. Therefore, we choose a truncated gaussian distribution with a mean value of µj and a variance of σj to describe the distribution of service time of workers in level j as the approximation of initial distribution:

<!-- b000750 | prose | pages [12] -->
G(x|µj, σj) =

<!-- b000751 | prose | pages [12] -->
(x−µj)2

<!-- b000752 | prose | pages [12] -->
1

<!-- b000753 | prose | pages [12] -->
−

<!-- b000754 | prose | pages [12] -->
2σj2

<!-- b000755 | prose | pages [12] -->
√ √

<!-- b000756 | prose | pages [12] -->
e 2πσj

<!-- b000757 | prose | pages [12] -->
where G(x|µj, σj) represents the gaussian distribution function, and µj is the minum service time requirement in level j, σj is chosen as twice of the length of intervals. The truncate range is the ranges in Table 2. Because that Senior Manager has no where to promote, we don’t care about his promotion.

<!-- b000758 | prose | pages [12] -->
The work experience can be determined by the similarity of the nodes and the vacancy, where we create a virtual node as well as several virtual edges to connect real nodes. By replacing the vacancy with the virtual node, the similarity between the vacancy and other nodes is calculated. Similarity is a proper indicator of the related work experience for there are strong edges inside the staﬀoﬃce and hierarchy. A worker is promoted to a higher level means he should get used to new circumstances, loses old links and forms new links.

<!-- b000759 | prose | pages [12] -->
4.3 Process of Recruitment

<!-- b000760 | prose | pages [12] -->
Since the median time to recruit(MTj with respect to level j in months) is a constant value, the number of workers ICM recruit during a unit time interval can be formulated

<!-- b000761 | furniture | pages [13] -->
Team # 33900

<!-- b000762 | furniture | pages [13] -->
Page 11 of 18

<!-- b000763 | prose | pages [13] -->
as Poisson Random Distribution. The probability is given by Equation 4. where nj represents the recruit number of level j. When the time unit is month, we have . A new worker forms the links deleted when he is recruited. When the time unit is month, we have:

<!-- b000764 | prose | pages [13] -->
λ = 1 MTj

<!-- b000765 | heading | pages [13] -->
Simulation Results and Analysis

<!-- b000766 | prose | pages [13] -->
5

<!-- b000767 | prose | pages [13] -->
For Task 2(1), our simulation result indicate that a churn in network induces impacts according to the similarity of nodes (cf. Figure 5, 6). Nodes having strong connection with the churn node gain large external factors in their turnover intentions while the others suﬀer less impact, thus those heavily aﬀected nodes are more likely to turnover. As the impact declines with time, the turnover intention of nodes reduce to the unaﬀected level. The impacts spread further when the aﬀected nodes turnover, and stops at a non-churn node.

<!-- b000768 | prose | pages [13] -->
relatively high turnover rate in mid-level positions

<!-- b000769 | prose | pages [13] -->
1.2

<!-- b000770 | prose | pages [13] -->
1.0

<!-- b000771 | prose | pages [13] -->
0.8

<!-- b000772 | prose | pages [13] -->
0.6

<!-- b000773 | prose | pages [13] -->
0.4

<!-- b000774 | prose | pages [13] -->
turnover propagation

<!-- b000775 | prose | pages [13] -->
0.2

<!-- b000776 | prose | pages [13] -->
low high

<!-- b000777 | prose | pages [13] -->
0.0

<!-- b000778 | prose | pages [13] -->
turnover intention

<!-- b000779 | prose | pages [13] -->
−0.2 −0.2 0.0 0.2 0.4 0.6 0.8 1.0

<!-- b000780 | prose | pages [13] -->
month = 6

<!-- b000781 | prose | pages [13] -->
(a)

<!-- b000782 | prose | pages [13] -->
1.2

<!-- b000783 | prose | pages [13] -->
1.0

<!-- b000784 | prose | pages [13] -->
0.8

<!-- b000785 | prose | pages [13] -->
0.6

<!-- b000786 | prose | pages [13] -->
0.4

<!-- b000787 | prose | pages [13] -->
0.2

<!-- b000788 | prose | pages [13] -->
low high

<!-- b000789 | prose | pages [13] -->
0.0

<!-- b000790 | prose | pages [13] -->
turnover intention

<!-- b000791 | prose | pages [13] -->
−0.2

<!-- b000792 | prose | pages [13] -->
1.2 1.2

<!-- b000793 | prose | pages [13] -->
−0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2

<!-- b000794 | prose | pages [13] -->
month = 8

<!-- b000795 | prose | pages [13] -->
(b)

<!-- b000796 | caption | pages [13] -->
Figure 5. Propagation of turnover intention over the Personnel Relationship Network.

<!-- b000797 | prose | pages [13] -->
Observation of Turnover Intention of (a) a certain time and (b) two months later. Turnover propagation is clearly illustrated. It can also be observed that the turnover rate is higher in mid-level positions.

<!-- b000798 | prose | pages [13] -->
For Task 2(2), our simulation shows that churn will both directly and indirectly aﬀect the productivity. As is shown in Equation 4, when an organizational churn takes place, a direct eﬀect is decreases in the number of workers. In the simulation of two years, the number of workers keeps reducing due to the high turn over rate and limited recruiting rate. The average turn over intention of diﬀerent levels of positions are shown in Figure 7, which is a main factor of productivity. The turn over intention of middle managers is relatively higher than the other levels, and the rises shown in these curves represent the continuous impacts of churns. The productivity mainly ﬂuctuate with the number of workers, but with the average productivity shown with the right y-axis, we can see a

<!-- b000799 | furniture | pages [14] -->
Team # 33900

<!-- b000800 | furniture | pages [14] -->
Page 12 of 18

<!-- b000801 | prose | pages [14] -->
reduction of 9.8% at the end of simulation. Churns impacts conducts to linked employee and have a negative eﬀects on their productivity. Considering the declining rate, it is easy to know that the continuous churns will keeps a steady impacts on the productivity, thus causes the decreases in the average productivity comparing to the start point.

<!-- b000802 | prose | pages [14] -->
160

<!-- b000803 | prose | pages [14] -->
140

<!-- b000804 | prose | pages [14] -->
120

<!-- b000805 | prose | pages [14] -->
100

<!-- b000806 | prose | pages [14] -->
Productivity

<!-- b000807 | prose | pages [14] -->
80

<!-- b000808 | prose | pages [14] -->
60

<!-- b000809 | prose | pages [14] -->
40

<!-- b000810 | prose | pages [14] -->
20

<!-- b000811 | prose | pages [14] -->
0

<!-- b000812 | prose | pages [14] -->
Senior Mangers Middle Managers Employees

<!-- b000813 | prose | pages [14] -->
11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6 7 8 9 10 21 22 23 24 Month

<!-- b000814 | caption | pages [14] -->
Figure 6. Task 2.1

<!-- b000815 | prose | pages [14] -->
0.8

<!-- b000816 | prose | pages [14] -->
0.7

<!-- b000817 | prose | pages [14] -->
0.6

<!-- b000818 | prose | pages [14] -->
Turnover Intention

<!-- b000819 | prose | pages [14] -->
0.5

<!-- b000820 | prose | pages [14] -->
0.4

<!-- b000821 | prose | pages [14] -->
0.3

<!-- b000822 | prose | pages [14] -->
0.2

<!-- b000823 | prose | pages [14] -->
0.1

<!-- b000824 | prose | pages [14] -->
0.0

<!-- b000825 | prose | pages [14] -->
5 10 Month

<!-- b000826 | prose | pages [14] -->
0.6

<!-- b000827 | prose | pages [14] -->
Employees Middle Managers

<!-- b000828 | prose | pages [14] -->
0.5

<!-- b000829 | prose | pages [14] -->
Senior Managers Average Productivity

<!-- b000830 | prose | pages [14] -->
Productivity (avg.)

<!-- b000831 | prose | pages [14] -->
0.4

<!-- b000832 | prose | pages [14] -->
0.3

<!-- b000833 | prose | pages [14] -->
0.2

<!-- b000834 | prose | pages [14] -->
0.1

<!-- b000835 | prose | pages [14] -->
0.0

<!-- b000836 | prose | pages [14] -->
15 20

<!-- b000837 | caption | pages [14] -->
Figure 7. Task 2.2

<!-- b000838 | prose | pages [14] -->
For Task 3, Our model yields a budget requirement of 19.14σ for recruiting and 10.87σ for training in the next 2 years, adding up to 30.01σ. The recruiting costs of ICM in terms of σ shown in Figure 8 varies randomly, which is caused by the poisson distribution of recruit numbers. The training costs is a function of the number of workers and their levels resulting in the smooth decrease of the curve.

<!-- b000839 | furniture | pages [15] -->
Team # 33900

<!-- b000840 | prose | pages [15] -->
2.0

<!-- b000841 | furniture | pages [15] -->
Page 13 of 18

<!-- b000842 | prose | pages [15] -->
8

<!-- b000843 | prose | pages [15] -->
Relative Recruiting Cost

<!-- b000844 | prose | pages [15] -->
7

<!-- b000845 | prose | pages [15] -->
Relative Training Cost

<!-- b000846 | prose | pages [15] -->
Relative Recruiting Cost

<!-- b000847 | prose | pages [15] -->
1.5

<!-- b000848 | prose | pages [15] -->
1.0

<!-- b000849 | prose | pages [15] -->
0.5

<!-- b000850 | prose | pages [15] -->
0.0

<!-- b000851 | prose | pages [15] -->
5 10

<!-- b000852 | prose | pages [15] -->
Relative Training Cost

<!-- b000853 | prose | pages [15] -->
6

<!-- b000854 | prose | pages [15] -->
5

<!-- b000855 | prose | pages [15] -->
4

<!-- b000856 | prose | pages [15] -->
3

<!-- b000857 | prose | pages [15] -->
2

<!-- b000858 | prose | pages [15] -->
1

<!-- b000859 | prose | pages [15] -->
0

<!-- b000860 | prose | pages [15] -->
15 20 Month

<!-- b000861 | caption | pages [15] -->
Figure 8. Task 3

<!-- b000862 | prose | pages [15] -->
For Task 4, our result shows that ICM can’t sustain a 80% full status for positions when the annual churn rate is 25% or 35%. In the recruiting model the coming number in an average time distribution is set to follows poisson distribution, thus a higher churn rate makes a faster loss in worker number.

<!-- b000863 | prose | pages [15] -->
As a consequence of high churn rate, the productivity of the company decreases a lot; the workers suﬀer from the impacts of churns and their turn over intentions are higher.

<!-- b000864 | prose | pages [15] -->
The total number of workers are shown in

<!-- b000865 | caption | pages [15] -->
Figure 9 and the numbers at 18% churn rate is also shown for comparison.

<!-- b000866 | prose | pages [15] -->
320

<!-- b000867 | prose | pages [15] -->
300

<!-- b000868 | prose | pages [15] -->
280

<!-- b000869 | prose | pages [15] -->
Number of Workers

<!-- b000870 | prose | pages [15] -->
260

<!-- b000871 | prose | pages [15] -->
240

<!-- b000872 | prose | pages [15] -->
220

<!-- b000873 | prose | pages [15] -->
200

<!-- b000874 | prose | pages [15] -->
180

<!-- b000875 | prose | pages [15] -->
160

<!-- b000876 | prose | pages [15] -->
0 5 10

<!-- b000877 | prose | pages [15] -->
35% Churn Rate 25% Churn Rate 18% Churn Rate

<!-- b000878 | prose | pages [15] -->
15 20 25 Month

<!-- b000879 | caption | pages [15] -->
Figure 9. Task 4

<!-- b000880 | prose | pages [15] -->
For Task 5, our results show that promotion increases the number of high-level em- ployee and improve the quality of staﬀbecause only those qualiﬁed can be promoted. Thus promotion increases the productivity.

<!-- b000881 | prose | pages [15] -->
The promotion is implemented by choosing a qualiﬁed node and replace a vacancy in a higher levels. As an assumption, we spare no eﬀects on promoting qualiﬁed employees, which means that all qualiﬁed nodes will be promoted at once. Figure 10 shows the overall productivity of diﬀerent levels of positions.

<!-- b000882 | prose | pages [15] -->
The promotion method keeps the productivity of higher levels and middle levels while introduces a shortage in low levels employees.

<!-- b000883 | furniture | pages [16] -->
Team # 33900

<!-- b000884 | prose | pages [16] -->
160

<!-- b000885 | prose | pages [16] -->
140

<!-- b000886 | prose | pages [16] -->
120

<!-- b000887 | prose | pages [16] -->
100

<!-- b000888 | prose | pages [16] -->
Productivity

<!-- b000889 | prose | pages [16] -->
80

<!-- b000890 | prose | pages [16] -->
60

<!-- b000891 | prose | pages [16] -->
40

<!-- b000892 | prose | pages [16] -->
20

<!-- b000893 | prose | pages [16] -->
0

<!-- b000894 | prose | pages [16] -->
1 2 3 4 5 6 7 8 9 10 11

<!-- b000895 | furniture | pages [16] -->
Page 14 of 18

<!-- b000896 | prose | pages [16] -->
Senior Mangers Middle Managers Employees

<!-- b000897 | prose | pages [16] -->
12 12 13 14 15 16 17 18 19 20 21 22 23 24 Month

<!-- b000898 | caption | pages [16] -->
Figure 10. Task 5

<!-- b000899 | prose | pages [16] -->
Our further discoveries and results for Task 6 and 7 is in Section 7 and 8.

<!-- b000900 | prose | pages [16] -->
6

<!-- b000901 | heading | pages [16] -->
Sensitivity Analysis

<!-- b000902 | prose | pages [16] -->
The initial distribution of service time is a speciﬁc gaussian distribution with chosen mean value and variation. Since service time is a substantial factor in judging the qualiﬁed work- ers, the distribution can aﬀect the number of qualiﬁed workers. Changing the distribution coeﬃcient the results may change a lot.

<!-- b000903 | prose | pages [16] -->
We choose the σ as the variable to be checked. The σ is originally set to be twice of the length of level interval ( lj with respect to level j ). Thus the new σs are the same as the length of level interval and three times of the length of level interval. We run the simulation in Task 5 and the results are shown as follows:

<!-- b000904 | caption | pages [16] -->
Table 3. Sensitivity Analysis of σ

<!-- b000905 | prose | pages [16] -->
σ 1 2l 3l

<!-- b000906 | prose | pages [16] -->
average promoted number(month) average productivity 2.314 2.083 2.250 0.378 0.353 0.374 average Senior Manager productivity middle manager number 3.378 3.372 3.741 35.16 38.33 37.00

<!-- b000907 | prose | pages [16] -->
These four indicators are related to the high level and the middle level numbers or productivity, which may show same changes. Although we can hardly eliminate the ﬂuc- tuation due to randomness, this indicates that the value of sigma doesn’t cause great changes in our results. Then we choose the mean value µ as the variable to be checked. The µ is originally set as the lower boundary of level interval. Thus the new µ are the median value of level interval and the higher boundary of level interval.

<!-- b000908 | prose | pages [16] -->
We run the simulation in Task 5 and the results are shown as follows:

<!-- b000909 | furniture | pages [17] -->
Team # 33900

<!-- b000910 | furniture | pages [17] -->
Page 15 of 18

<!-- b000911 | caption | pages [17] -->
Table 4. Sensitivity Analysis of µ

<!-- b000912 | prose | pages [17] -->
µ 1 2l 3l

<!-- b000913 | prose | pages [17] -->
average promoted number(month) average productivity 2.314 2.083 2.250 0.378 0.353 0.374 average Senior Manager productivity middle manager number 3.378 3.372 3.741 35.16 38.33 37.00

<!-- b000914 | prose | pages [17] -->
Improvements using Multi-layered Networks 7

<!-- b000915 | prose | pages [17] -->
In this section, we outline the potential use of multi-layered networks.

<!-- b000916 | prose | pages [17] -->
Our model so far has only considered the relationship and links within the ICM. In fact, ICM’s employees in the Human Captial network are connected by a wide range of personal and public relationships. These relational ties are highly diverse in nature and can represent e.g. the inﬂuence or trust a person has for another. Every type of relation spans a social network of its own. The relationship between Human Capital network and other network models of the organization is therefore characterized by the superposition of its networks, all deﬁned on the same set of nodes. This superposition is called multiplex network. We consider Network H and Network C (cf. Figure 11), which respectively represent part of the Human Capital Network and another network linking individuals with the same hometown. Comparing Network C and Network H we can see that both contain information that the other does not contain, e.g. SM1 and EE3 are connected in Network C but not in Network H.

<!-- b000917 | prose | pages [17] -->
EE3

<!-- b000918 | prose | pages [17] -->
EE3

<!-- b000919 | prose | pages [17] -->
JM6

<!-- b000920 | prose | pages [17] -->
SM1

<!-- b000921 | prose | pages [17] -->
SM1

<!-- b000922 | prose | pages [17] -->
EE3

<!-- b000923 | prose | pages [17] -->
JM6

<!-- b000924 | prose | pages [17] -->
SM1

<!-- b000925 | prose | pages [17] -->
Network H ES5

<!-- b000926 | prose | pages [17] -->
ES7

<!-- b000927 | prose | pages [17] -->
IS1 IS1

<!-- b000928 | prose | pages [17] -->
EE34

<!-- b000929 | prose | pages [17] -->
Network C

<!-- b000930 | prose | pages [17] -->
ES5

<!-- b000931 | prose | pages [17] -->
ES7

<!-- b000932 | prose | pages [17] -->
IS1 IS1

<!-- b000933 | prose | pages [17] -->
EE34

<!-- b000934 | caption | pages [17] -->
Figure 11. Task 6

<!-- b000935 | prose | pages [17] -->
We could beneﬁt a lot from the potential use of Multiplex Network [4]. With Multiplex network we could predict and better understand individual’s behavior. In the previous example, It’s consistent with our expectation if both SM1 and EE3 leave ICM for other jobs since thy are adjacent in Network C. Multiplex network can also be used in dynamic analysis at group level. We could measure the similarity based on the Jaccard Coeﬃcient which quantiﬁes the interaction between two networks by measuring the tendency that links simultaneously are present in both networks . Jαβ is a similarity score between two sets of elements and is deﬁned between two sets of elements and is deﬁned as the size ot intersection of the sets divided by the size of their union Jαβ = |α∩β|

<!-- b000936 | prose | pages [17] -->
|α∪β| .

<!-- b000937 | furniture | pages [18] -->
Team # 33900

<!-- b000938 | prose | pages [18] -->
8 Further Discussions on HR

<!-- b000939 | furniture | pages [18] -->
Page 16 of 18

<!-- b000940 | prose | pages [18] -->
We inspect further into this problem on the HR issues pointed out in the problem material.

<!-- b000941 | prose | pages [18] -->
First we incorporate annual evaluation with current HR management. We use a n dimensional vector −→e = (e1, e2, e3, ..., en) to represent the annual evaluation judged by the supervisor , where ei ∈[0, 1] denotes the ith component of evaluation. Assume that there are m optimal positions for the employee and our purpose is to ﬁnd the best position for him/her. The requirement of kth position can be expressed by another similar vector −→ Φ k = (Φk1, Φk2, Φk3, ..., Φkn). Hence we denote the Euclidean distance from the employee to position k by Dk = ||−→ Φ k −−→e || and greater distance indicates lower possibility of position k being suitable for the employee. Therefore the index of the best position for the employee is:

<!-- b000942 | prose | pages [18] -->
k = arg

<!-- b000943 | prose | pages [18] -->
 

<!-- b000944 | prose | pages [18] -->


<!-- b000945 | prose | pages [18] -->
min

<!-- b000946 | prose | pages [18] -->
Dj j

<!-- b000947 | prose | pages [18] -->
Then we analyze the HR elements of ICM by using properties of Human Capital Network. Note that the network average clustering coeﬃcient can be used to analyze the HR functions of the Human Capital network because the coeﬃcient of a single node can indicate the closeness of the cluster centered at this node. Thus the average clustering coeﬃcient represents the unity of ICM by taking all nodes into account.

<!-- b000948 | prose | pages [18] -->
9

<!-- b000949 | heading | pages [18] -->
Strengths and Weaknesses

<!-- b000950 | prose | pages [18] -->
9.1

<!-- b000951 | heading | pages [18] -->
Strengths

<!-- b000952 | prose | pages [18] -->
• Comprehensiveness We take careful consideration of factors related to turn-over intention. Our models are capable of simulating the situation in real life. The results also agree with common sense and life experience. Our model is strongly related to network science whose strength in modeling is in its ability to embrace the complexity of the real world. The diﬀusion process of churn impacts is established and analyzed with dynamic process involved which is a bright spot of our model.

<!-- b000953 | prose | pages [18] -->
• Robustness Our models are fairly robust to the changes in parameters based on sensitivity anal- ysis. It means a slight change in parameters will not cause a signiﬁcant change in the result.

<!-- b000954 | prose | pages [18] -->
• Justiﬁability The result of our model is well consistent with our experience, which proves the rationality and correctness of our model.

<!-- b000955 | prose | pages [18] -->
9.2

<!-- b000956 | heading | pages [18] -->
Weaknesses

<!-- b000957 | prose | pages [18] -->
• We don’t have a full view of the components of the middle managers or the low level employees, we treats them as diﬀerent, but we regard them as a group when analyzing results.

<!-- b000958 | furniture | pages [19] -->
Team # 33900

<!-- b000959 | furniture | pages [19] -->
Page 17 of 18

<!-- b000960 | prose | pages [19] -->
• Some of the parameters are based on common sense because few data are available.

<!-- b000961 | prose | pages [19] -->
However, based on our sensitivity analysis, they will not make a great diﬀerence if slightly changed.

<!-- b000962 | heading | pages [19] -->
References

<!-- b000963 | references | pages [19] -->
[1] COMAP.

<!-- b000964 | references | pages [19] -->
(2015).

<!-- b000965 | references | pages [19] -->
ICM

<!-- b000966 | references | pages [19] -->
Problem

<!-- b000967 | references | pages [19] -->
C.

<!-- b000968 | references | pages [19] -->
http://www.comap.com/undergraduate/

<!-- b000969 | references | pages [19] -->
contests/mcm/contests/2015/problems/2015_ICM_Problem_C.pdf.

<!-- b000970 | references | pages [19] -->
[2] Salas, E., Cooke, N. J., & Rosen, M. A. (2008). On teams, teamwork, and team

<!-- b000971 | references | pages [19] -->
performance: Discoveries and developments. Human Factors: The Journal of the

<!-- b000972 | references | pages [19] -->
Human Factors and Ergonomics Society, 50(3), 540-547.

<!-- b000973 | references | pages [19] -->
[3] Stokols, D., Hall, K. L., Taylor, B. K., & Moser, R. P. (2008). The science of team

<!-- b000974 | references | pages [19] -->
science: overview of the ﬁeld and introduction to the supplement. American journal

<!-- b000975 | references | pages [19] -->
of preventive medicine, 35(2), S77-S89.

<!-- b000976 | references | pages [19] -->
[4] Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A.

<!-- b000977 | references | pages [19] -->
(2014). Multilayer networks. Journal of Complex Networks, 2(3), 203-271.

<!-- b000978 | references | pages [19] -->
[5] Wikipedia(2015).

<!-- b000979 | references | pages [19] -->
Turnover

<!-- b000980 | references | pages [19] -->
(employment).

<!-- b000981 | references | pages [19] -->
http://en.wikipedia.org/wiki/

<!-- b000982 | references | pages [19] -->
Turnover_(employment).

<!-- b000983 | references | pages [19] -->
[6] Cotton, J. L., & Tuttle, J. M. (1986). Employee turnover: A meta-analysis and review

<!-- b000984 | references | pages [19] -->
with implications for research. Academy of management Review, 11(1), 55-70.

<!-- b000985 | references | pages [19] -->
[7] LinkedIn Inc,. (2014). LinkedIn Big Data: The First Report on Promotion to HOD.

<!-- b000986 | references | pages [19] -->
http://www.gs.xinhuanet.com/news/2015-01/30/c_1114195205.htm

<!-- b000987 | references | pages [19] -->
[8] Zhao, X., Liu, L., & Zhang, C. (2003). A Multi-variable Analysis on Factors Inﬂu-

<!-- b000988 | references | pages [19] -->
encing Employee’s Turnover Intention. China Soft Science, (3), 71-74.

<!-- b000989 | references | pages [19] -->
[9] Felps, W., Mitchell, T. R., Hekman, D. R., Lee, T. W., Holtom, B. C., & Harman,

<!-- b000990 | references | pages [19] -->
W. S. (2009). Turnover contagion: How coworkers’ job embeddedness and job search

<!-- b000991 | references | pages [19] -->
behaviors inﬂuence quitting. Academy of Management Journal, 52(3), 545-561.

<!-- b000992 | references | pages [19] -->
[10] Bartunek, J. M., Huang, Z., & Walsh, I. J. (2008). The development of a process

<!-- b000993 | references | pages [19] -->
model of collective turnover. Human Relations, 61(1), 5-38.

<!-- b000994 | references | pages [19] -->
[11] Whitmore, G. A. (1979). An inverse Gaussian model for labour turnover. Journal of

<!-- b000995 | references | pages [19] -->
the Royal Statistical Society. Series A (General), 468-478.

<!-- b000996 | references | pages [19] -->
[12] Jovanovic, B. (1979). Job matching and the theory of turnover. The Journal of Po-

<!-- b000997 | references | pages [19] -->
litical Economy, 972-990.

<!-- b000998 | references | pages [19] -->
[13] Tett, R. P., & Meyer, J. P. (1993). Job satisfaction, organizational commitment,

<!-- b000999 | references | pages [19] -->
turnover intention, and turnover: path analyses based on meta-analytic ﬁndings.

<!-- b001000 | references | pages [19] -->
Personnel Psychology, 46(2), 259-293.

<!-- b001001 | references | pages [19] -->
[14] Mobley, W. H., Griﬀeth, R. W., Hand, H. H., & Meglino, B. M. (1979). Review and

<!-- b001002 | references | pages [19] -->
conceptual analysis of the employee turnover process. Psychological Bulletin, 86(3),

<!-- b001003 | references | pages [19] -->
493.

<!-- b001004 | furniture | pages [20] -->
Team # 33900

<!-- b001005 | furniture | pages [20] -->
Page 18 of 18

<!-- b001006 | references | pages [20] -->
[15] Feeley, T. H., Moon, S. I., Kozey, R. S., & Slowe, A. S. (2010). An erosion model of

<!-- b001007 | references | pages [20] -->
employee turnover based on network centrality. Journal of Applied Communication

<!-- b001008 | references | pages [20] -->
Research, 38(2), 167-188.

<!-- b001009 | references | pages [20] -->
[16] Zhou, T., Lü, L., & Zhang, Y. C. (2009). Predicting missing links via local infor-

<!-- b001010 | references | pages [20] -->
mation. The European Physical Journal B-Condensed Matter and Complex Systems,

<!-- b001011 | references | pages [20] -->
71(4), 623-630.

<!-- b001012 | references | pages [20] -->
[17] Okamoto, K., Chen, W., & Li, X. Y. (2008). Ranking of closeness centrality for large-

<!-- b001013 | references | pages [20] -->
scale social networks. In Frontiers in Algorithmics (pp. 186-195). Springer Berlin

<!-- b001014 | references | pages [20] -->
Heidelberg.
