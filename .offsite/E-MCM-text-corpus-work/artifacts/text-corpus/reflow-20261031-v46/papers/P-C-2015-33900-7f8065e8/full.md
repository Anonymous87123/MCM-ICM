# P-C-2015-33900-7f8065e8

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
33900

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | heading | pages [1] -->
2015 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000007 | prose | pages [1] -->
Analyzing Employee Turnover Using Dynamic Network

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
In this paper, we build a dynamic network model and perform various simulations to study the behavior of Human Capital Network (HCN) under disturbance such as churns.

<!-- b000010 | prose | pages [1] -->
We detail the structure of HCN factors and continuing eﬀects of turnover and dy- namics of HCN utilizing given information and run simulations to examine the contagion of turnover and analyze the sustainability of HCN. We interpret and present our results along with robustness analysis and strengths and weaknesses of our model.

<!-- b000011 | prose | pages [1] -->
For Task 1, we build two networks (Personnel Relationship Network and Organiza- tional Network), which together form our Human Capital Network. We extract important information from problem material and make assumptions when necessary to deduce the detailed structure and assign employees with the oﬃces. We propose an evaluation function of assignments and use Genetic Algorithm to ﬁnd the optimal assignment. The assign- ment provides us with new information about employee relationship(co-oﬃce relationship etc.), together with the supervisory relationship form the edges in HCN and complete our network building.

<!-- b000012 | prose | pages [1] -->
For Task 2, we ﬁrst detail the turnover in terms of factors and impacts and evaluate the cost and productivity of HCN. We then dig into the dynamics in terms of turnover process, promotion process and recruitment process using probabilistic method and discrete time system simulation. The results show that organizational churn has both direct and indirect eﬀects on the organization’s productivity. The direct eﬀect is because it causes loss of employee and the indirect is because it will make other employee more likely to turnover.

<!-- b000013 | prose | pages [1] -->
For Task 3, we utilize our dynamic network model with our discrete time simulating system to calculate the budget. Our result is a budget requirement of 19.14σ for recruiting and 10.87σ for training in the next 2 years, adding up to 30.01σ.

<!-- b000014 | prose | pages [1] -->
For Task 4, we also run simulations and results show that ICM can’t sustain its 80% full status.

<!-- b000015 | prose | pages [1] -->
For Task 5, our results show that promotion increases the number of high-level em- ployee and improve the quality of staﬀbecause only those qualiﬁed can be promoted. Thus promotion increases the productivity.

<!-- b000016 | prose | pages [1] -->
We also make further discussions on Multi-layer Networks and HR issues which com- plete Task 6, 7 and other requirements that the problem material brought forth.

<!-- b000017 | furniture | pages [2] -->
Team # 33900

<!-- b000018 | contents | pages [2] -->
i

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1 Introduction

<!-- b000021 | contents | pages [2] -->
1

<!-- b000022 | contents | pages [2] -->
1.1

<!-- b000023 | contents | pages [2] -->
Problem Statement

<!-- b000024 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | contents | pages [2] -->
1.2

<!-- b000027 | contents | pages [2] -->
Related Work

<!-- b000028 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [2] -->
1

<!-- b000030 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000031 | contents | pages [2] -->
1

<!-- b000032 | contents | pages [2] -->
2.1

<!-- b000033 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
1

<!-- b000035 | contents | pages [2] -->
2.2

<!-- b000036 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
2

<!-- b000038 | contents | pages [2] -->
3 The Human Capital Network Model

<!-- b000039 | contents | pages [2] -->
2

<!-- b000040 | contents | pages [2] -->
3.1

<!-- b000041 | contents | pages [2] -->
Assigning Employees to Oﬃces . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
2

<!-- b000043 | contents | pages [2] -->
3.1.1

<!-- b000044 | contents | pages [2] -->
Principles of Employee Assignment . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
2

<!-- b000046 | contents | pages [2] -->
3.1.2

<!-- b000047 | contents | pages [2] -->
Evaluation of Employee Assignment

<!-- b000048 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
3

<!-- b000050 | contents | pages [2] -->
3.1.3

<!-- b000051 | contents | pages [2] -->
Optimization Using Genetic Algorithm . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
3

<!-- b000053 | contents | pages [2] -->
3.2

<!-- b000054 | contents | pages [2] -->
Building The Human Capital Network . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
4

<!-- b000056 | contents | pages [2] -->
3.2.1

<!-- b000057 | contents | pages [2] -->
Building The Network of Personnel Relationship

<!-- b000058 | contents | pages [2] -->
. . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
4

<!-- b000060 | contents | pages [2] -->
3.2.2

<!-- b000061 | contents | pages [2] -->
Building the Organizational Network . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
5

<!-- b000063 | contents | pages [2] -->
3.3

<!-- b000064 | contents | pages [2] -->
Evaluating Turnover Intention of Employee . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
6

<!-- b000066 | contents | pages [2] -->
3.3.1

<!-- b000067 | contents | pages [2] -->
Factor of Turnover Contagion . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
6

<!-- b000069 | contents | pages [2] -->
3.3.2

<!-- b000070 | contents | pages [2] -->
Factor of Employee Centrality . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
7

<!-- b000072 | contents | pages [2] -->
3.3.3

<!-- b000073 | contents | pages [2] -->
Factors of Salary and Promotion Prospect . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
7

<!-- b000075 | contents | pages [2] -->
3.3.4

<!-- b000076 | contents | pages [2] -->
Evaluation using AHP] . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
8

<!-- b000078 | contents | pages [2] -->
3.4

<!-- b000079 | contents | pages [2] -->
Productivity and Costs of HCM . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
9

<!-- b000081 | contents | pages [2] -->
4 Dynamics of Human Capital Network

<!-- b000082 | contents | pages [2] -->
9

<!-- b000083 | contents | pages [2] -->
4.1

<!-- b000084 | contents | pages [2] -->
Process of Turnover . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | contents | pages [2] -->
10

<!-- b000086 | contents | pages [2] -->
4.2

<!-- b000087 | contents | pages [2] -->
Process of Promotion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
10

<!-- b000089 | contents | pages [2] -->
4.3

<!-- b000090 | contents | pages [2] -->
Process of Recruitment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
10

<!-- b000092 | contents | pages [2] -->
5 Simulation Results and Analysis

<!-- b000093 | contents | pages [2] -->
11

<!-- b000094 | contents | pages [2] -->
6 Sensitivity Analysis

<!-- b000095 | contents | pages [2] -->
14

<!-- b000096 | contents | pages [2] -->
7 Improvements using Multi-layered Networks

<!-- b000097 | contents | pages [2] -->
15

<!-- b000098 | contents | pages [2] -->
8 Further Discussions on HR

<!-- b000099 | contents | pages [2] -->
16

<!-- b000100 | contents | pages [2] -->
9 Strengths and Weaknesses

<!-- b000101 | contents | pages [2] -->
16

<!-- b000102 | contents | pages [2] -->
9.1

<!-- b000103 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [2] -->
16

<!-- b000105 | contents | pages [2] -->
9.2

<!-- b000106 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [2] -->
16

<!-- b000108 | contents | pages [2] -->
References

<!-- b000109 | contents | pages [2] -->
17

<!-- b000110 | furniture | pages [3] -->
Team # 33900

<!-- b000111 | furniture | pages [3] -->
Page 1 of 18

<!-- b000112 | heading | pages [3] -->
1 Introduction

<!-- b000113 | heading | pages [3] -->
1.1 Problem Statement

<!-- b000114 | prose | pages [3] -->
Among various factors that inﬂuence a teamąŕs performance, the members of the team and the chemistry between them, i.e. teamwork, is an important one. The approach to this is to maintain a team of talented and well-trained people and keep them in proper positions. However, in modern companies employee turnover [5] often takes place and disturb the environments. This paper oﬀers a model of employee turnover and its impact based on the Human Capital Network. The HCN is extracted as a hierarchy structure of staﬀoﬃces and divisions as nodes and a list of 370 employees as nodes, then the turnover intention is analyzed by the AHP method, and divided as salary, promotion, importance and impacts from others. The importance of the nodes is given by the closeness centrality and the LeaderRank value of nodesąŕ departments. Salary and promotion are impacts indicators in consideration for diﬀerent levels. The impact is conducted through links and damps as time elapse. The promotion process and recruit process are also predicted by stochastic process methods, which make a part in the total dynamic process.

<!-- b000115 | heading | pages [3] -->
1.2 Related Work

<!-- b000116 | prose | pages [3] -->
In recent years, there has been tremendous interest in studying Team Science and de- veloping appropriate model of team and team performance. Salas et al. reviewed key discoveries and developments in the ﬁeld of team performance over the past 50 years [2]. They concluded that ‘team performance can be modeled’ and which are our motivation to model the productivity.Stokols et al. argued about [3] and Kivelä et al. studied the Multilayer Networks. which are incorporated into our paper for improvement of our model.

<!-- b000117 | prose | pages [3] -->
Many works have inspected the nature of rumor propagation etc. which is similar to[NOT good...] turnover propagation. However, the methods they used are mainly mean-ﬁeld equations for homogeneous networks and ... for heterogenous networks. the underlying mechanism of how network structure inﬂuences the rumor spreading is still an open question.

<!-- b000118 | prose | pages [3] -->
There have been extensive study But limited work has been done in analyzing the turnover process using a mathematical model and quantifying (??) its impact on the overall team performance. We are concerned in this paper with the...

<!-- b000119 | heading | pages [3] -->
2 Assumptions and Notations

<!-- b000120 | heading | pages [3] -->
2.1 Assumptions

<!-- b000121 | prose | pages [3] -->
We make the following basic assumptions in order to simplify the problem. Each of our assumptions is justiﬁed and is consistent with the information given in [1].

<!-- b000122 | prose | pages [3] -->
• Turnover behavior of an employee is contagious. So the worker connected to other employees who have churned is more likely to churn [1].

<!-- b000123 | prose | pages [3, 4] -->
• Similar individuals are more likely to aﬀect each other’s behavior. This is an adopted assumption from previous work of Feeley et al. [15].

<!-- b000124 | furniture | pages [4] -->
Team # 33900

<!-- b000125 | furniture | pages [4] -->
Page 2 of 18

<!-- b000127 | heading | pages [4] -->
2.2 Notations

<!-- b000128 | prose | pages [4] -->
We use a list of symbols (cf. Table 1) for simpliﬁcation of expression.

<!-- b000129 | caption | pages [4] -->
Table 1. Notations (in the order of model)

<!-- b000130 | prose | pages [4] -->
Symbol Deﬁnition Notes

<!-- b000131 | heading | pages [4] -->
Human Capital Network Model

<!-- b000132 | prose | pages [4] -->
G graph of Personnel Relationship Network of ICM cf. Figure 2 g graph of Organizational Network of ICM cf. Figure 3 N number of nodes dij topological distance between node i and j NELDY 1 (NEBY 2+NEEY 3)/2 × 100% [5] Rt employee turnover rate Rt = T turnover intention CCi = 1 N CC Closeness Centrality di = PN j=1 dij Pi average annual salary(payment) of employee i represents employee’s ability Li level of hierarchy of the oﬃce of employee i LCEO = 5 and LBranch = 1

<!-- b000133 | heading | pages [4] -->
The Second Model

<!-- b000134 | prose | pages [4] -->
Emu stuﬀed C frozen

<!-- b000135 | heading | pages [4] -->
3 The Human Capital Network Model

<!-- b000136 | prose | pages [4] -->
In this model, the HCN is extracted as a hierarchy structure of staﬀoﬃces and divisions as nodes and a list of 370 employees as nodes, then the turnover intention is analyzed by the AHP method, and divided as salary, promotion, importance and impacts from others. The importance of the nodes is given by the closeness centrality and the LeaderRank value of nodesąŕ departments.

<!-- b000137 | heading | pages [4] -->
3.1 Assigning Employees to Oﬃces

<!-- b000138 | prose | pages [4] -->
Due to limited given information on the personnel relationship of ICM in detail, we assume some basic rules of allocating oﬃces to complete our model. We apply these rules and form an AHP-based evaluation model, then we use Genetic Algorithm to ﬁnd the solution.

<!-- b000139 | heading | pages [4] -->
3.1.1 Principles of Employee Assignment

<!-- b000140 | prose | pages [4] -->
Our principles for allocating oﬃces is listed as follows:

<!-- b000141 | prose | pages [4] -->
1NELDY:Number of Employees who Left During the Year.

<!-- b000142 | prose | pages [4] -->
2NEBY:Number of Employees at the Beginning of the Year.

<!-- b000143 | prose | pages [4] -->
3NEEY:Number of Employees at the End of the Year.

<!-- b000144 | furniture | pages [5] -->
Team # 33900

<!-- b000145 | furniture | pages [5] -->
Page 3 of 18

<!-- b000146 | prose | pages [5] -->
• Employees with higher level of position should occupy oﬃces of higher centrality and higher hierarchy in the structure diagram given in [1].

<!-- b000147 | prose | pages [5] -->
• Supervisors and executives should distribute as broadly as possible to ensure widespread supervisory and to maximally utilize the manager resource.

<!-- b000148 | prose | pages [5] -->
• Oﬃces of same level should have similar constitute for equality.

<!-- b000149 | prose | pages [5] -->
• Each executive should be matched with an administrative clerk as his/her secretary.

<!-- b000150 | heading | pages [5] -->
3.1.2 Evaluation of Employee Assignment

<!-- b000151 | prose | pages [5] -->
We ﬁrst quantify these principles as follows:

<!-- b000152 | prose | pages [5] -->
1. Principle of centrality: E1 = P Pi · CCi 2. Principle of hierarchy: E2 = P Pi · Li 3. Principle of equality: E3 = P Dj 4. Principle of uniformity: E4 = P Sj

<!-- b000153 | prose | pages [5] -->
Pi is the annual salary of an employee, which is a representative of his ability. Dj is diﬀerences between oﬃce j and other oﬃces of the same level. Sj is the number of same type of employees in oﬃce j . We hereby give the evaluation function:

<!-- b000154 | prose | pages [5] -->
Eval = α1E1 + α2E2 + α3E3 + α4E4 (1)

<!-- b000155 | prose | pages [5] -->
Because that E3 and E4 are too large, we choose α1 = 0.5, α2 = 0.5, α3 = −0.05, α4 = −0.05 after some experiments with random assignments. We plug these parameters back into Equation 1 to obtain the evaluation function.

<!-- b000156 | heading | pages [5] -->
3.1.3 Optimization Using Genetic Algorithm

<!-- b000157 | prose | pages [5] -->
We got an evaluation function in Section 3.1.2. Next we are going to ﬁnd its optimum, which in correspondence is the best assignment solution. It is easy to show that this problem is a Combinatorial Optimization problem, for which search heuristics such as Genetic Algorithm and Tabu Search are proven to be more eﬃcient. We notice that the assignment itself is naturally a representation of the gene code, so we choose Genetic Algorithm to ﬁnd the maximum of the evaluation function (cf. Equation 1). Thus the evolution process such as gene crossover can be easily achieved by swap employees in diﬀerent oﬃces. We implement the algorithm using MATLAB, initialize 500 random solutions and begin iteration. The algorithm produce a satisfactory result (cf. Figure 1).

<!-- b000158 | prose | pages [5] -->
We can see from Figure 1 that the algorithm not only assigned oﬃces according to staﬀhierarchy (i.e. superior oﬃces for staﬀof higher position like senior manager) but also incorporated uniformity and equality.

<!-- b000159 | furniture | pages [6] -->
Team # 33900

<!-- b000160 | furniture | pages [6] -->
Page 4 of 18

<!-- b000161 | prose | pages [6] -->
CEO SM JM AC*2

<!-- b000162 | prose | pages [6] -->
CFO* RESEARCH FACILITIES VP HR SALES CIO* SM AC EE*5 SM AC EE*2 SM AC EE*2 SM JM AC*2 SM AC EE*2 SM AC EE*2 SM AC EE*5

<!-- b000163 | prose | pages [6] -->
PRODUCT* JM AC ES EE*4

<!-- b000164 | prose | pages [6] -->
DIRECTOR DIRECTOR DIRECTOR DIRECTOR DIRECTOR DIRECTOR IS*3  IE ES IS*2 IE IS*3  IE IS*3  IE IS*3  IE IS*3  IE

<!-- b000165 | prose | pages [6] -->
BRANCH* IS       IE*6

<!-- b000166 | prose | pages [6] -->
Manager Offices* Branch Offices* JM  AC  IS  EE*4 ES IE*6

<!-- b000167 | caption | pages [6] -->
Figure 1. Organizational structure of ICM with all the employees assigned. Each block

<!-- b000168 | prose | pages [6] -->
represents an oﬃce (without *) or two divisions (with * and thicker border). Bold text is abbreviation of positions(SM for Senior Manager etc.). Blocks with the same color and style share same constitute. Some blocks (Manager Oﬃces and Branch Oﬃces) are replaced by legend symbols for simpliﬁcation.

<!-- b000169 | heading | pages [6] -->
3.2 Building The Human Capital Network

<!-- b000170 | prose | pages [6] -->
We assigned the staﬀwith proper oﬃces in the above mentioned. Next we are going to build the network using this newly deducted information.

<!-- b000171 | heading | pages [6] -->
3.2.1 Building The Network of Personnel Relationship

<!-- b000172 | prose | pages [6] -->
Now that there are a grant total of N(N ⩽370) employees in ICM, which is corresponding to the N node in graph G, and we use vi(1 ⩽i ⩽N) to denote the ith node in G. In order to simplify the problem,we make a natural assumption that any pair of nodes vi and in G is connected if and only if the three following conditions are satisﬁed:

<!-- b000173 | prose | pages [6] -->
• vi and vj are in the same Branch or division;

<!-- b000174 | prose | pages [6] -->
• vi and vj are in the same level;

<!-- b000175 | prose | pages [6] -->
• vi and vj are respectively leaders of two oﬃce whose superior department are the same.

<!-- b000176 | prose | pages [6] -->
It’s worth noting that the relationship between any two persons in ICM varies, thus G is a weighted graph,the weight of edge eij reveals the level of relationship between node vi and node vj .Let N dimensional matrix A = (wij)N×N be the adjacency matrix of graph G ,we can conclude from previous discussion that:

<!-- b000177 | prose | pages [6] -->
 σ if vi and vj satisfy condition 2 wij = 1 if vi and vj satisfy condition 1 or 3

<!-- b000178 | prose | pages [6] -->
The graph G is illustrated in Figure 2.

<!-- b000179 | furniture | pages [7] -->
Team # 33900

<!-- b000180 | furniture | pages [7] -->
Page 5 of 18

<!-- b000181 | prose | pages [7] -->
Links within an office/division top-level mid-top IE38 IE37 IE28 IE24 IE39 IE41 mid-level mid-bottom IE40 IE25 Links between office heads IE29 IE36 IE26 bottom-level IE27 IE32 IE72 IE31 ES6 IE76 ES4 IE73 IE34 EE59 IE33 IE47 IE77 EE61 EE58 Inter-hierarchy IE74 IE43 IE30 IE35 EE60 IE75 EE62 IE42 IE46 ES5 links EE71 EE64 IE45 AC12 EE63 ES7 EE70 EE72 Director 2 IE44 IE54 EE65 IS19 EE73 IE58 JM12 IE62 AC13 EE99 IS20 JM13 IS22 AC15 IE56 EE95 IE61 JM15 IE55 IE99 ES12 IE101 EE2 IE145 IE65 EE96 IE57 EE97 IS21 IE64 JM14 SM5 IE97 IE59 EE89 IE98 EE67 EE69 EE81 EE3 EE98 IE63 EE79 AC27 SM7 IE60 IE100 IE111 ES9 IE109 IE96 EE66 EE68 EE88 EE78 AC14 ES10 EE80 AC25 ES16 IS24 IE113 JM17 AC17 IE112 EE8 IS1 IE108 IE68 EE9 IE104 ES18 IE103 ES11 IE110 IE67 ES17 EE91 ES8 IS2 IE71 IE51 ES13 IE148 IE107 IE66 EE30 IE102 EE12 EE32 EE41 EE90 IE81 EE40 IE105 EE19 EE94 IE48 IE83 EE13 EE20 IS4 IE106 IE6 EE39 ES19 EE10 EE33 AC26 IE49 EE5 SM6 IE13 VP EE21 IE70 AC7 EE31 IE53 IE114 EE38 IE14 EE93 IE8 IE69 EE92 IE78 IE116 IE118 IE146 AC5 AC0 EE11 AC2 IE115 IE82 IS14 IS12 JM7 JM5 EE4 EE18 IE17 IE117 IE10 IE7 IE12 AC20 IS6 IE52 IS9 CEO IE119 IS13JM6 IS7 JM0 JM2 IE50 IE9 JM19 ES2 IE16 SM1 IE79 ES24 IS0 IE11 IE80 IS11 JM4 AC18 IE15 EE35 EE36 EE82 ES1 AC6 JM18 AC21 IE149 SM0 IS5 AC19 SM2 IS8 AC22 JM1 EE26 AC4 EE85 EE34 IE19 ES3 IS10 EE17 EE37 SM3 JM3 EE83 IE22 IS3 AC1 EE28 EE29 EE84 ES0 IE18 AC23 EE1 EE15 IE4 AC3 EE23 EE16 EE27 IE23 IE5 IE144 EE14 IE21 EE25 IE0 EE24 IE139 IE141 EE0 IE126 IE20 IE3 EE22 IE128 ES23 IE143 IE1 IS23 ES21 JM16 AC16 EE105 IE142 AC29 EE7 SM9 IE2 IE131 EE107 EE77 IE147 EE76 IE130 IE138 IE140 IE127 EE108 EE52 AC10 EE6 EE109 EE74 EE75 AC24 EE53 IE129 EE106 ES15 EE50 Branch L EE87 Internet EE51 ES22 IS17 JM10 IE95 IE90 IE93 SM4 ES20 EE86 IS15 JM8 AC8 IE91 JM11 SM8 IS18 AC28 IE136 IE134 EE42 IE94 IE92 AC11 JM9 IS16 EE102 EE44 EE103 EE43 IE137 EE55 EE104 IE135 IE123 ES14 AC9 EE57 EE45 IE120 EE101 IE132 EE100 EE54 IE125 IE133 EE46 EE56 IE121 EE49 IE86 EE47 IE88 IE124 EE48 IE122 IE85 IE87 IE89 IE84

<!-- b000182 | caption | pages [7] -->
Figure 2. Personnel Relationship Network of ICM. The color denotes oﬃce hierarchy.

<!-- b000183 | prose | pages [7] -->
Small clusters of oﬃces and three types of edges are labeled. Some edges are omitted for conciseness.

<!-- b000184 | heading | pages [7] -->
3.2.2 Building the Organizational Network

<!-- b000185 | prose | pages [7] -->
Also we can get the Organizational Network. The procedures of forming g can be imple- mented as follows:

<!-- b000186 | prose | pages [7] -->
1. add all staﬀoﬃces and divisions to g as nodes.

<!-- b000187 | prose | pages [7] -->
2. add hierarchy chains as directed edges, from lower hierarchy to higher.

<!-- b000188 | prose | pages [7] -->
3. for all nodes pairs, if the two nodes have the same hierarchical father, add a bi- directed edge between them.

<!-- b000189 | prose | pages [7] -->
4. add a sink node to graph, then connect all nodes except the sink node to the sink node with a bi-directed edge, which is in convenience for leader rank.

<!-- b000190 | prose | pages [7] -->
Graph g is a directed graph (cf. Figure 3). The calculated LeaderRank Value is illustrated by the node size. Note that LeaderRank Value is not always consistent with hierarchy.

<!-- b000191 | furniture | pages [8] -->
Team # 33900

<!-- b000192 | furniture | pages [8] -->
Page 6 of 18

<!-- b000193 | prose | pages [8] -->
Branch J top-level mid-top Branch B Branch I mid-level mid-bottom Branch L Branch A bottom-level Director 5 Branch K Director 1 Director 6

<!-- b000194 | prose | pages [8] -->
CIO Plant Blue CFO Branch C Production Manager Facilities Director 2 Branch D Plant Green CEO VP Research Networks Director 4 HR Director 3 Information Program Manager Branch G Sales Marketing Branch E Branch H Regional Branch F World Wide Internet

<!-- b000195 | caption | pages [8] -->
Figure 3. Organizational Network of ICM. The color denotes oﬃce level. The size of

<!-- b000196 | prose | pages [8] -->
the node denotes the LeaderRank Value. Note that the LeaderRank Value of Production Manager is higher than that of VP despite of their hierarchical relations.

<!-- b000197 | heading | pages [8] -->
3.3 Evaluating Turnover Intention of Employee

<!-- b000198 | prose | pages [8] -->
Cotton et al. found that factors such as pay and employment perception are the most highly reliable correlates of turnover [6]. The factors can be divided into External Factors and Internal Factors. We adopt his conclusion and further specify them into three basic elements: salary, level of position, promotion prospect. We also introduce the inﬂuence of other people’s turnover behavior, summing up to four elements denoted by C1 , C2 , C3 , C4 for quantiﬁcation.

<!-- b000199 | prose | pages [8] -->
In order to ﬁnd the employee with the highest turnover probability, we use AHP to evaluate the contribution of each factor to turnover intention.

<!-- b000200 | heading | pages [8] -->
3.3.1 Factor of Turnover Contagion

<!-- b000201 | prose | pages [8] -->
Hereinbefore we assumed that if one employee left, other employees close to him are inﬂuenced and are more likely to ‘churn’ (cf. Section 2.1). We quantify the level of inﬂuence by introducing Structural Equivalence [15] as closeness. We assume that the level of inﬂuence of one’s turnover to another’s intention is positively correlated with Structural Equivalence (in other words, similarity).

<!-- b000202 | prose | pages [8] -->
We adopt the RA Index [16] in weighted graph to measure the similarity between nodes. Consider a pair of nodes, x and y which are not directly connected. If node x can send some information to y with their common neighbors playing the role of transmitters, then they would share some similarity. We revise the original RA Index and deﬁne the similarity between x and y as the amount of resource y received from x :

<!-- b000203 | prose | pages [8, 9] -->
wxz + wyz X sxy = k(z) z∈Γ(x)∩Γ(y) where Γ(i) is the set of neighbors of x and k(i) the degree of x , and we can develop the expression of C1i :

<!-- b000204 | furniture | pages [9] -->
Team # 33900

<!-- b000205 | furniture | pages [9] -->
Page 7 of 18

<!-- b000207 | prose | pages [9] -->
e−β(t−tj) X C1i = 1 + e−β(t−tj) sij aj∈S

<!-- b000208 | prose | pages [9] -->
where S denotes the set of former employees who have churned at moment ti . We use Logistic Curve to describe former employee’s impact due to the attenuation eﬀect.

<!-- b000209 | heading | pages [9] -->
3.3.2 Factor of Employee Centrality

<!-- b000210 | prose | pages [9] -->
Individuals with greater centrality in a communication network are less likely to turnover due to the information and social support beneﬁts provided by peers in the workplace [15].

<!-- b000211 | prose | pages [9] -->
In our model the overall importance of an employee is determined by his centrality in graph G (cf. Figure 2) and the importance of his department in graph g (cf. Figure 3). Because Closeness Centrality can be regarded as a measure of how long it will take to spread information from certain node to all other nodes and is widely used in Social Network Analysis [17], we choose Closeness Centrality as the measurement. And the importance of his department in graph g is determined by the LeaderRank Value of the oﬃce.

<!-- b000212 | prose | pages [9] -->
For each node in graph G , we calculate its Closeness Centrality as follows: For node i , calculate mean distance between it and every other node as di :

<!-- b000213 | prose | pages [9] -->
N di = 1 X dij n j=1

<!-- b000214 | prose | pages [9] -->
where dij is the topological distance between i and j . The reciprocal of di is deﬁned as Closeness Centrality:

<!-- b000215 | prose | pages [9] -->
CCi = 1 N = di NP dij j=1

<!-- b000216 | prose | pages [9] -->
For each oﬃce in directed graph g , we calculate the LeaderRank Value LR as follows:

<!-- b000217 | prose | pages [9] -->
To conclude we give the expression of C2i:

<!-- b000218 | prose | pages [9] -->
1 C2i = LR × CCi

<!-- b000219 | heading | pages [9] -->
3.3.3 Factors of Salary and Promotion Prospect

<!-- b000220 | prose | pages [9] -->
We assume that the salary is the same among same hierarchy, so we quantify the factor of salary as follows:

<!-- b000221 | prose | pages [9, 10] -->
 ξ1 node i belongs to top hierarchy  C3i = ξ2 node i belongs to mid hierarchy ξ3 node i belongs to bottom hierarchy  Similarly, assuming that the promotion prospect is the same, we give:

<!-- b000222 | furniture | pages [10] -->
Team # 33900

<!-- b000223 | furniture | pages [10] -->
Page 8 of 18

<!-- b000225 | prose | pages [10] -->
 ψ1 node i belongs to top hierarchy  C4i = ψ2 node i belongs to mid hierarchy ψ3 node i belongs to bottom hierarchy 

<!-- b000226 | prose | pages [10] -->
We choose ξ1 = 1 , ξ2 = 0 , ξ3 = 0 on account of the relatively low CEO-to-worker salary ratio. And because that employees in the middle ‘feel stuck in their jobs with little opportunity to advance’ [1], we choose ψ1 = 0 , ψ2 = 1 , ψ3 = 0 .

<!-- b000227 | heading | pages [10] -->
3.3.4 Evaluation using AHP]

<!-- b000228 | prose | pages [10] -->
We gave the quantiﬁcation of factors in the above text. Our AHP hierarchy for this evaluation is illustrated in Figure 4.

<!-- b000229 | prose | pages [10] -->
Turnover Intention (T)

<!-- b000230 | prose | pages [10] -->
Impact from Others (C1) Employee Centrality (C2) Salary (C3) Promotion Prospect (C4)

<!-- b000231 | prose | pages [10] -->
……… Employee1 Employee2 Employee3 ...

<!-- b000232 | caption | pages [10] -->
Figure 4. The AHP hierarchy for determine employee’s turnover intention.

<!-- b000233 | prose | pages [10] -->
Combining those four factors using AHP, we give the following pairwise comparison matrix:

<!-- b000234 | prose | pages [10] -->
C1 C2 C3 C4   C1 1 2 3 1/2 C2 1/3 1 1 1/2     C3 1/2 1 1 1/3   C4 3 2 2 1

<!-- b000235 | prose | pages [10] -->
Thus we have the evaluation function expressed as Equation (4), in which the pa- rameters α1, α2, α3, α4 are to be determined.

<!-- b000236 | prose | pages [10] -->
T = α1C1 + α2C2 + α3C3 + α4C4 (2)

<!-- b000237 | prose | pages [10] -->
We calculate the parameters using MATLAB, and get α1 = 0.3084, α2 = 0.1482, α3 = 0.1445, α4 = 0.3989. We test the consistency of our AHP in the following two aspects:

<!-- b000238 | prose | pages [10] -->
1. The Consistency Index CI = (λmax −n)/(n−1) should be close to zero. With n = 4 we get CI = 0.0045, which is very close to zero.

<!-- b000239 | furniture | pages [11] -->
Team # 33900

<!-- b000240 | furniture | pages [11] -->
Page 9 of 18

<!-- b000241 | prose | pages [11] -->
2. The Consistency Ratio CR = CI/RI should be less than 0.1. With n = 4 we get RI = 0.9 and CR = 0.05 < 0.1.

<!-- b000242 | prose | pages [11] -->
The test result displays perfectly acceptable consistency.

<!-- b000243 | heading | pages [11] -->
3.4 Productivity and Costs of HCM

<!-- b000244 | prose | pages [11] -->
The contribution of employee to the company is intuitively relevant to the following three factors:

<!-- b000245 | prose | pages [11] -->
1. The ability of the employee, represented by his wage.

<!-- b000246 | prose | pages [11] -->
2. The eﬃciency of the employee (denoted by ei). It is trivial to see that eﬃciency is inversely proportional to turnover intention.

<!-- b000247 | prose | pages [11] -->
3. The importance of the oﬃce in which the employee works. This factor is introduced by modifying coeﬃcient λi and is equal to LeaderRank Value of graph g .

<!-- b000248 | prose | pages [11] -->
Thus we have productivity expression as follows:

<!-- b000249 | prose | pages [11] -->
X λi × Pi × ei Productivity = (3) i

<!-- b000250 | prose | pages [11] -->
The overall recruiting costs of ICM is given by the summation of new workers’ median recruit costs:

<!-- b000251 | prose | pages [11] -->
X X RCall = MRj j Nj∈NW

<!-- b000252 | prose | pages [11] -->
where RCall is for overall recruiting costs, Nj represents a node of level j, NW indicates the new worker set, and MRj is the median recruiting costs of level j. The training costs is related to the current number of workers in diﬀerent levels, which are given by:

<!-- b000253 | prose | pages [11] -->
X X TCall = MTj j Nj∈Nodes

<!-- b000254 | prose | pages [11] -->
where TCall is for overall recruiting costs, Nj represents a node of level j, Nodes indicates the set of all nodes, and MTj is the median training costs of level j .

<!-- b000255 | heading | pages [11] -->
4 Dynamics of Human Capital Network

<!-- b000256 | prose | pages [11] -->
We further analyze the dynamic characteristics of HCN. The dynamic process imcludes churns, promotions and recruits. The churn exhibits impacts on linked nodes as parts of the turnover intention. With stochastic process the recruits and promotions can be regarded as random variables following to speciﬁc distributions. Using the model

<!-- b000257 | furniture | pages [12] -->
Team # 33900

<!-- b000258 | furniture | pages [12] -->
Page 10 of 18

<!-- b000259 | heading | pages [12] -->
4.1 Process of Turnover

<!-- b000260 | prose | pages [12] -->
The process of turnover is based on the turnover intention analysis in Section 3. The nodes to churn is chosen randomly with their turnover intention as weight. By approxi- mating the poisson distribution can best describe churns distribution as follows:

<!-- b000261 | prose | pages [12] -->
P(nch = k) = e−λλk (4) k!

<!-- b000262 | prose | pages [12] -->
where represents the number of churns. If the time unit is month, we have Eventually, A churned worker loses his links and is deleted from the G graph.

<!-- b000263 | heading | pages [12] -->
4.2 Process of Promotion

<!-- b000264 | prose | pages [12] -->
We aim to distinguish qualiﬁed workers in the company, hence we choose the service time and the work experience as two diciplines in promoting. The service time of a worker is the duration he stays in this company. The service time requirments with respect to levels of positions are shown as Table 2.

<!-- b000265 | caption | pages [12] -->
Table 2. Service Time Requirements for diﬀerent Level of Positions.

<!-- b000266 | prose | pages [12] -->
Level of Position SM JM ES IS EE IE

<!-- b000267 | prose | pages [12] -->
Service Time Requirements 8 5 3 2 1 0

<!-- b000268 | prose | pages [12] -->
Note that the promotion of Administrative Clerk is ignored in the promotion process because of the diﬀerences in jobs especially in a production-oriented company. We assume that worker with service-time beyond comparison in Table 2 be cropped to the maximum requirements initially. Therefore, we choose a truncated gaussian distribution with a mean value of µj and a variance of σj to describe the distribution of service time of workers in level j as the approximation of initial distribution:

<!-- b000269 | prose | pages [12] -->
(x−µj)2 1 − 2σj2 √ G(x|µj, σj) = e 2πσj where G(x|µj, σj) represents the gaussian distribution function, and µj is the minum service time requirement in level j, σj is chosen as twice of the length of intervals. The truncate range is the ranges in Table 2. Because that Senior Manager has no where to promote, we don’t care about his promotion.

<!-- b000270 | prose | pages [12] -->
The work experience can be determined by the similarity of the nodes and the vacancy, where we create a virtual node as well as several virtual edges to connect real nodes. By replacing the vacancy with the virtual node, the similarity between the vacancy and other nodes is calculated. Similarity is a proper indicator of the related work experience for there are strong edges inside the staﬀoﬃce and hierarchy. A worker is promoted to a higher level means he should get used to new circumstances, loses old links and forms new links.

<!-- b000271 | heading | pages [12] -->
4.3 Process of Recruitment

<!-- b000272 | prose | pages [12, 13] -->
Since the median time to recruit(MTj with respect to level j in months) is a constant value, the number of workers ICM recruit during a unit time interval can be formulated as Poisson Random Distribution. The probability is given by Equation 4. where nj represents the recruit number of level j. When the time unit is month, we have . A new worker forms the links deleted when he is recruited. When the time unit is month, we have: 1 λ = MTj

<!-- b000273 | furniture | pages [13] -->
Team # 33900

<!-- b000274 | furniture | pages [13] -->
Page 11 of 18

<!-- b000276 | heading | pages [13] -->
5 Simulation Results and Analysis

<!-- b000277 | prose | pages [13] -->
For Task 2(1), our simulation result indicate that a churn in network induces impacts according to the similarity of nodes (cf. Figure 5, 6). Nodes having strong connection with the churn node gain large external factors in their turnover intentions while the others suﬀer less impact, thus those heavily aﬀected nodes are more likely to turnover. As the impact declines with time, the turnover intention of nodes reduce to the unaﬀected level. The impacts spread further when the aﬀected nodes turnover, and stops at a non-churn node.

<!-- b000278 | prose | pages [13] -->
relatively high turnover rate in mid-level positions 1.2 1.2

<!-- b000279 | prose | pages [13] -->
1.0 1.0

<!-- b000280 | prose | pages [13] -->
0.8 0.8

<!-- b000281 | prose | pages [13] -->
0.6 0.6

<!-- b000282 | prose | pages [13] -->
0.4 0.4 turnover propagation 0.2 0.2

<!-- b000283 | prose | pages [13] -->
low high low high 0.0 0.0 turnover intention turnover intention −0.2 −0.2 −0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2 −0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2 month = 6 month = 8 (a) (b)

<!-- b000284 | caption | pages [13] -->
Figure 5. Propagation of turnover intention over the Personnel Relationship Network.

<!-- b000285 | prose | pages [13] -->
Observation of Turnover Intention of (a) a certain time and (b) two months later. Turnover propagation is clearly illustrated. It can also be observed that the turnover rate is higher in mid-level positions.

<!-- b000286 | prose | pages [13, 14] -->
For Task 2(2), our simulation shows that churn will both directly and indirectly aﬀect the productivity. As is shown in Equation 4, when an organizational churn takes place, a direct eﬀect is decreases in the number of workers. In the simulation of two years, the number of workers keeps reducing due to the high turn over rate and limited recruiting rate. The average turn over intention of diﬀerent levels of positions are shown in Figure 7, which is a main factor of productivity. The turn over intention of middle managers is relatively higher than the other levels, and the rises shown in these curves represent the continuous impacts of churns. The productivity mainly ﬂuctuate with the number of workers, but with the average productivity shown with the right y-axis, we can see a reduction of 9.8% at the end of simulation. Churns impacts conducts to linked employee and have a negative eﬀects on their productivity. Considering the declining rate, it is easy to know that the continuous churns will keeps a steady impacts on the productivity, thus causes the decreases in the average productivity comparing to the start point.

<!-- b000287 | furniture | pages [14] -->
Team # 33900

<!-- b000288 | furniture | pages [14] -->
Page 12 of 18

<!-- b000290 | prose | pages [14] -->
160 Senior Mangers 140 Middle Managers Employees 120

<!-- b000291 | prose | pages [14] -->
100 Productivity 80

<!-- b000292 | prose | pages [14] -->
60

<!-- b000293 | prose | pages [14] -->
40

<!-- b000294 | prose | pages [14] -->
20

<!-- b000295 | prose | pages [14] -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 Month

<!-- b000296 | caption | pages [14] -->
Figure 6. Task 2.1

<!-- b000297 | prose | pages [14] -->
0.6 0.8 Employees Middle Managers 0.7 0.5 Senior Managers 0.6 Average Productivity Turnover Intention Productivity (avg.) 0.4 0.5

<!-- b000298 | prose | pages [14] -->
0.3 0.4

<!-- b000299 | prose | pages [14] -->
0.3 0.2 0.2 0.1 0.1

<!-- b000300 | prose | pages [14] -->
0.0 0.0 5 10 15 20 Month

<!-- b000301 | caption | pages [14] -->
Figure 7. Task 2.2

<!-- b000302 | prose | pages [14] -->
For Task 3, Our model yields a budget requirement of 19.14σ for recruiting and 10.87σ for training in the next 2 years, adding up to 30.01σ. The recruiting costs of ICM in terms of σ shown in Figure 8 varies randomly, which is caused by the poisson distribution of recruit numbers. The training costs is a function of the number of workers and their levels resulting in the smooth decrease of the curve.

<!-- b000303 | furniture | pages [15] -->
Team # 33900

<!-- b000304 | furniture | pages [15] -->
Page 13 of 18

<!-- b000305 | prose | pages [15] -->
2.0 8 Relative Recruiting Cost 7 Relative Training Cost Relative Recruiting Cost Relative Training Cost 1.5 6

<!-- b000306 | prose | pages [15] -->
5

<!-- b000307 | prose | pages [15] -->
1.0 4

<!-- b000308 | prose | pages [15] -->
3

<!-- b000309 | prose | pages [15] -->
0.5 2

<!-- b000310 | prose | pages [15] -->
1

<!-- b000311 | prose | pages [15] -->
0.0 0 5 10 15 20 Month

<!-- b000312 | caption | pages [15] -->
Figure 8. Task 3

<!-- b000313 | prose | pages [15] -->
For Task 4, our result shows that ICM can’t sustain a 80% full status for positions when the annual churn rate is 25% or 35%. In the recruiting model the coming number in an average time distribution is set to follows poisson distribution, thus a higher churn rate makes a faster loss in worker number. As a consequence of high churn rate, the productivity of the company decreases a lot; the workers suﬀer from the impacts of churns and their turn over intentions are higher. The total number of workers are shown in

<!-- b000314 | caption | pages [15] -->
Figure 9 and the numbers at 18% churn rate is also shown for comparison.

<!-- b000315 | prose | pages [15] -->
320 35% Churn Rate 300 25% Churn Rate 18% Churn Rate 280 Number of Workers 260

<!-- b000316 | prose | pages [15] -->
240

<!-- b000317 | prose | pages [15] -->
220

<!-- b000318 | prose | pages [15] -->
200

<!-- b000319 | prose | pages [15] -->
180

<!-- b000320 | prose | pages [15] -->
160 0 5 10 15 20 25 Month

<!-- b000321 | caption | pages [15] -->
Figure 9. Task 4

<!-- b000322 | prose | pages [15] -->
For Task 5, our results show that promotion increases the number of high-level em- ployee and improve the quality of staﬀbecause only those qualiﬁed can be promoted. Thus promotion increases the productivity.

<!-- b000323 | prose | pages [15] -->
The promotion is implemented by choosing a qualiﬁed node and replace a vacancy in a higher levels. As an assumption, we spare no eﬀects on promoting qualiﬁed employees, which means that all qualiﬁed nodes will be promoted at once. Figure 10 shows the overall productivity of diﬀerent levels of positions. The promotion method keeps the productivity of higher levels and middle levels while introduces a shortage in low levels employees.

<!-- b000324 | furniture | pages [16] -->
Team # 33900

<!-- b000325 | furniture | pages [16] -->
Page 14 of 18

<!-- b000326 | prose | pages [16] -->
160 Senior Mangers Middle Managers 140 Employees 120

<!-- b000327 | prose | pages [16] -->
100 Productivity 80

<!-- b000328 | prose | pages [16] -->
60

<!-- b000329 | prose | pages [16] -->
40

<!-- b000330 | prose | pages [16] -->
20

<!-- b000331 | prose | pages [16] -->
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 Month

<!-- b000332 | caption | pages [16] -->
Figure 10. Task 5

<!-- b000333 | prose | pages [16] -->
Our further discoveries and results for Task 6 and 7 is in Section 7 and 8.

<!-- b000334 | heading | pages [16] -->
6 Sensitivity Analysis

<!-- b000335 | prose | pages [16] -->
The initial distribution of service time is a speciﬁc gaussian distribution with chosen mean value and variation. Since service time is a substantial factor in judging the qualiﬁed work- ers, the distribution can aﬀect the number of qualiﬁed workers. Changing the distribution coeﬃcient the results may change a lot.

<!-- b000336 | prose | pages [16] -->
We choose the σ as the variable to be checked. The σ is originally set to be twice of the length of level interval ( lj with respect to level j ). Thus the new σs are the same as the length of level interval and three times of the length of level interval. We run the simulation in Task 5 and the results are shown as follows:

<!-- b000337 | caption | pages [16] -->
Table 3. Sensitivity Analysis of σ

<!-- b000338 | prose | pages [16] -->
σ 1 2l 3l

<!-- b000339 | prose | pages [16] -->
average promoted number(month) 2.314 2.083 2.250 average productivity 0.378 0.353 0.374 average Senior Manager productivity 3.378 3.372 3.741 middle manager number 35.16 38.33 37.00

<!-- b000340 | prose | pages [16] -->
These four indicators are related to the high level and the middle level numbers or productivity, which may show same changes. Although we can hardly eliminate the ﬂuc- tuation due to randomness, this indicates that the value of sigma doesn’t cause great changes in our results. Then we choose the mean value µ as the variable to be checked. The µ is originally set as the lower boundary of level interval. Thus the new µ are the median value of level interval and the higher boundary of level interval. We run the simulation in Task 5 and the results are shown as follows:

<!-- b000341 | furniture | pages [17] -->
Team # 33900

<!-- b000342 | furniture | pages [17] -->
Page 15 of 18

<!-- b000343 | caption | pages [17] -->
Table 4. Sensitivity Analysis of µ

<!-- b000344 | prose | pages [17] -->
µ 1 2l 3l

<!-- b000345 | prose | pages [17] -->
average promoted number(month) 2.314 2.083 2.250 average productivity 0.378 0.353 0.374 average Senior Manager productivity 3.378 3.372 3.741 middle manager number 35.16 38.33 37.00

<!-- b000346 | heading | pages [17] -->
7 Improvements using Multi-layered Networks

<!-- b000347 | prose | pages [17] -->
In this section, we outline the potential use of multi-layered networks.

<!-- b000348 | prose | pages [17] -->
Our model so far has only considered the relationship and links within the ICM. In fact, ICM’s employees in the Human Captial network are connected by a wide range of personal and public relationships. These relational ties are highly diverse in nature and can represent e.g. the inﬂuence or trust a person has for another. Every type of relation spans a social network of its own. The relationship between Human Capital network and other network models of the organization is therefore characterized by the superposition of its networks, all deﬁned on the same set of nodes. This superposition is called multiplex network. We consider Network H and Network C (cf. Figure 11), which respectively represent part of the Human Capital Network and another network linking individuals with the same hometown. Comparing Network C and Network H we can see that both contain information that the other does not contain, e.g. SM1 and EE3 are connected in Network C but not in Network H.

<!-- b000349 | prose | pages [17] -->
Network H ES5 EE3 EE3 ES7 IS1 JM6 EE34 SM1

<!-- b000350 | prose | pages [17] -->
SM1 Network C ES5 EE3

<!-- b000351 | prose | pages [17] -->
ES7 IS1 JM6 EE34 SM1

<!-- b000352 | caption | pages [17] -->
Figure 11. Task 6

<!-- b000353 | prose | pages [17] -->
We could beneﬁt a lot from the potential use of Multiplex Network [4]. With Multiplex network we could predict and better understand individual’s behavior. In the previous example, It’s consistent with our expectation if both SM1 and EE3 leave ICM for other jobs since thy are adjacent in Network C. Multiplex network can also be used in dynamic analysis at group level. We could measure the similarity based on the Jaccard Coeﬃcient which quantiﬁes the interaction between two networks by measuring the tendency that links simultaneously are present in both networks . Jαβ is a similarity score between two sets of elements and is deﬁned between two sets of elements and is deﬁned as the size ot intersection of the sets divided by the size of their union Jαβ = |α∩β| |α∪β| .

<!-- b000354 | furniture | pages [18] -->
Team # 33900

<!-- b000355 | furniture | pages [18] -->
Page 16 of 18

<!-- b000356 | heading | pages [18] -->
8 Further Discussions on HR

<!-- b000357 | prose | pages [18] -->
We inspect further into this problem on the HR issues pointed out in the problem material.

<!-- b000358 | prose | pages [18] -->
First we incorporate annual evaluation with current HR management. We use a n dimensional vector −→e = (e1, e2, e3, ..., en) to represent the annual evaluation judged by the supervisor , where ei ∈[0, 1] denotes the ith component of evaluation. Assume that there are m optimal positions for the employee and our purpose is to ﬁnd the best position for him/her. The requirement of kth position can be expressed by another similar vector −→ Φ k = (Φk1, Φk2, Φk3, ..., Φkn). Hence we denote the Euclidean distance from the employee to position k by Dk = ||−→ Φ k −−→e || and greater distance indicates lower possibility of position k being suitable for the employee. Therefore the index of the best position for the employee is:

<!-- b000359 | prose | pages [18] -->
  k = arg min Dj j

<!-- b000360 | prose | pages [18] -->
Then we analyze the HR elements of ICM by using properties of Human Capital Network. Note that the network average clustering coeﬃcient can be used to analyze the HR functions of the Human Capital network because the coeﬃcient of a single node can indicate the closeness of the cluster centered at this node. Thus the average clustering coeﬃcient represents the unity of ICM by taking all nodes into account.

<!-- b000361 | heading | pages [18] -->
9 Strengths and Weaknesses

<!-- b000362 | heading | pages [18] -->
9.1 Strengths

<!-- b000363 | prose | pages [18] -->
• Comprehensiveness We take careful consideration of factors related to turn-over intention.

<!-- b000364 | prose | pages [18] -->
Our models are capable of simulating the situation in real life. The results also agree with common sense and life experience.

<!-- b000365 | prose | pages [18] -->
Our model is strongly related to network science whose strength in modeling is in its ability to embrace the complexity of the real world.

<!-- b000366 | prose | pages [18] -->
The diﬀusion process of churn impacts is established and analyzed with dynamic process involved which is a bright spot of our model.

<!-- b000367 | prose | pages [18] -->
• Robustness Our models are fairly robust to the changes in parameters based on sensitivity anal- ysis. It means a slight change in parameters will not cause a signiﬁcant change in the result.

<!-- b000368 | prose | pages [18] -->
• Justiﬁability The result of our model is well consistent with our experience, which proves the rationality and correctness of our model.

<!-- b000369 | heading | pages [18] -->
9.2 Weaknesses

<!-- b000370 | prose | pages [18] -->
• We don’t have a full view of the components of the middle managers or the low level employees, we treats them as diﬀerent, but we regard them as a group when analyzing results.

<!-- b000371 | furniture | pages [19] -->
Team # 33900

<!-- b000372 | furniture | pages [19] -->
Page 17 of 18

<!-- b000373 | prose | pages [19] -->
• Some of the parameters are based on common sense because few data are available.

<!-- b000374 | prose | pages [19] -->
However, based on our sensitivity analysis, they will not make a great diﬀerence if slightly changed.

<!-- b000375 | heading | pages [19] -->
References

<!-- b000376 | references | pages [19] -->
[1] COMAP.

<!-- b000377 | references | pages [19] -->
(2015).

<!-- b000378 | references | pages [19] -->
ICM

<!-- b000379 | references | pages [19] -->
Problem

<!-- b000380 | references | pages [19] -->
C.

<!-- b000381 | references | pages [19] -->
http://www.comap.com/undergraduate/

<!-- b000382 | references | pages [19] -->
contests/mcm/contests/2015/problems/2015_ICM_Problem_C.pdf.

<!-- b000383 | references | pages [19] -->
[2] Salas, E., Cooke, N. J., & Rosen, M. A. (2008). On teams, teamwork, and team

<!-- b000384 | references | pages [19] -->
performance: Discoveries and developments. Human Factors: The Journal of the

<!-- b000385 | references | pages [19] -->
Human Factors and Ergonomics Society, 50(3), 540-547.

<!-- b000386 | references | pages [19] -->
[3] Stokols, D., Hall, K. L., Taylor, B. K., & Moser, R. P. (2008). The science of team

<!-- b000387 | references | pages [19] -->
science: overview of the ﬁeld and introduction to the supplement. American journal

<!-- b000388 | references | pages [19] -->
of preventive medicine, 35(2), S77-S89.

<!-- b000389 | references | pages [19] -->
[4] Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A.

<!-- b000390 | references | pages [19] -->
(2014). Multilayer networks. Journal of Complex Networks, 2(3), 203-271.

<!-- b000391 | references | pages [19] -->
[5] Wikipedia(2015).

<!-- b000392 | references | pages [19] -->
Turnover

<!-- b000393 | references | pages [19] -->
(employment).

<!-- b000394 | references | pages [19] -->
http://en.wikipedia.org/wiki/

<!-- b000395 | references | pages [19] -->
Turnover_(employment).

<!-- b000396 | references | pages [19] -->
[6] Cotton, J. L., & Tuttle, J. M. (1986). Employee turnover: A meta-analysis and review

<!-- b000397 | references | pages [19] -->
with implications for research. Academy of management Review, 11(1), 55-70.

<!-- b000398 | references | pages [19] -->
[7] LinkedIn Inc,. (2014). LinkedIn Big Data: The First Report on Promotion to HOD.

<!-- b000399 | references | pages [19] -->
http://www.gs.xinhuanet.com/news/2015-01/30/c_1114195205.htm

<!-- b000400 | references | pages [19] -->
[8] Zhao, X., Liu, L., & Zhang, C. (2003). A Multi-variable Analysis on Factors Inﬂu-

<!-- b000401 | references | pages [19] -->
encing Employee’s Turnover Intention. China Soft Science, (3), 71-74.

<!-- b000402 | references | pages [19] -->
[9] Felps, W., Mitchell, T. R., Hekman, D. R., Lee, T. W., Holtom, B. C., & Harman,

<!-- b000403 | references | pages [19] -->
W. S. (2009). Turnover contagion: How coworkers’ job embeddedness and job search

<!-- b000404 | references | pages [19] -->
behaviors inﬂuence quitting. Academy of Management Journal, 52(3), 545-561.

<!-- b000405 | references | pages [19] -->
[10] Bartunek, J. M., Huang, Z., & Walsh, I. J. (2008). The development of a process

<!-- b000406 | references | pages [19] -->
model of collective turnover. Human Relations, 61(1), 5-38.

<!-- b000407 | references | pages [19] -->
[11] Whitmore, G. A. (1979). An inverse Gaussian model for labour turnover. Journal of

<!-- b000408 | references | pages [19] -->
the Royal Statistical Society. Series A (General), 468-478.

<!-- b000409 | references | pages [19] -->
[12] Jovanovic, B. (1979). Job matching and the theory of turnover. The Journal of Po-

<!-- b000410 | references | pages [19] -->
litical Economy, 972-990.

<!-- b000411 | references | pages [19] -->
[13] Tett, R. P., & Meyer, J. P. (1993). Job satisfaction, organizational commitment,

<!-- b000412 | references | pages [19] -->
turnover intention, and turnover: path analyses based on meta-analytic ﬁndings.

<!-- b000413 | references | pages [19] -->
Personnel Psychology, 46(2), 259-293.

<!-- b000414 | references | pages [19] -->
[14] Mobley, W. H., Griﬀeth, R. W., Hand, H. H., & Meglino, B. M. (1979). Review and

<!-- b000415 | references | pages [19] -->
conceptual analysis of the employee turnover process. Psychological Bulletin, 86(3),

<!-- b000416 | references | pages [19] -->
493.

<!-- b000417 | furniture | pages [20] -->
Team # 33900

<!-- b000418 | furniture | pages [20] -->
Page 18 of 18

<!-- b000419 | references | pages [20] -->
[15] Feeley, T. H., Moon, S. I., Kozey, R. S., & Slowe, A. S. (2010). An erosion model of

<!-- b000420 | references | pages [20] -->
employee turnover based on network centrality. Journal of Applied Communication

<!-- b000421 | references | pages [20] -->
Research, 38(2), 167-188.

<!-- b000422 | references | pages [20] -->
[16] Zhou, T., Lü, L., & Zhang, Y. C. (2009). Predicting missing links via local infor-

<!-- b000423 | references | pages [20] -->
mation. The European Physical Journal B-Condensed Matter and Complex Systems,

<!-- b000424 | references | pages [20] -->
71(4), 623-630.

<!-- b000425 | references | pages [20] -->
[17] Okamoto, K., Chen, W., & Li, X. Y. (2008). Ranking of closeness centrality for large-

<!-- b000426 | references | pages [20] -->
scale social networks. In Frontiers in Algorithmics (pp. 186-195). Springer Berlin

<!-- b000427 | references | pages [20] -->
Heidelberg.
