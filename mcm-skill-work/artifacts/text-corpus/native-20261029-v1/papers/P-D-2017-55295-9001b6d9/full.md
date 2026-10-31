# P-D-2017-55295-9001b6d9

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
55295

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
F1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
Problem Chosen

<!-- b000010 | prose | pages [1] -->
T3

<!-- b000011 | prose | pages [1] -->
F3

<!-- b000012 | title | pages [1] -->
D

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
2017 Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

<!-- b000016 | title | pages [1] -->
Breezing Through Security Checkpoints:

<!-- b000017 | title | pages [1] -->
an Intelligent Airport with Smart Scheduling

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | prose | pages [1] -->
In order to improve the performance of airport security check while preserving the same security standards, we model and reﬁne this process. We run extensive simulations to analyze performance of our model. Speciﬁcally,

<!-- b000020 | prose | pages [1] -->
For task (a), we model the airport security process with a queueing network. We get the parameters of the queueing network model by ﬁtting the data in the provided data sheet to different distributions. We validate our model by simulating it with the real world parameter combination and comparing its output against data collected from airport passengers. We identify three bottlenecks in our model: lack of sufﬁcient ID check points; exclusive assignment of screening check points to passengers; the presence of suspicious passengers.

<!-- b000021 | prose | pages [1] -->
For task (b), we propose three routing algorithms to optimize the throughput and variance of the airport: greedy algorithm, backpressure algorithm, and drift-plus-penalty algorithm. The best one of these algorithms achieves high throughput that is close to optimal and relatively low variance in waiting time. Besides, our proposed routing al- gorithm manages to retain passenger satisfaction while scheduling. We also explore the optimal ratio of different kinds of check points and test the robustness of modiﬁed mod- els.

<!-- b000022 | prose | pages [1] -->
For task (c), we analyze the impact of different cultures and traveler types and run simulation to see the reaction of our model. The cultures we analyze are collectivist cul- tures, individualist cultures. The types of travelers we analyze are family-based travelers and tech-based travelers. We also propose accommodations to these special situations.

<!-- b000023 | prose | pages [1] -->
For task (d), we propose both globally applicable and locally applicable policies to airport security managers. Our policies are based on our analysis of different cultures and types of travelers as well as our analysis of our routing algorithms.

<!-- b000024 | keywords | pages [1] -->
Keywords: Queueing Networks; Routing Algorithms; Lyapunov Optimization

<!-- b000025 | prose | pages [2] -->
Breezing Through Security Checkpoints: an Intelligent Airport with Smart Scheduling

<!-- b000026 | furniture | pages [2] -->
Team # 55295

<!-- b000027 | heading | pages [2] -->
Summary

<!-- b000028 | prose | pages [2] -->
In order to improve the performance of airport security check while preserving the same security standards, we model and reﬁne this process. We run extensive simulations to analyze performance of our model. Speciﬁcally,

<!-- b000029 | prose | pages [2] -->
For task (a), we model the airport security process with a queueing network. We get the parameters of the queueing network model by ﬁtting the data in the provided data sheet to different distributions. We validate our model by simulating it with the real world parameter combination and comparing its output against data collected from airport passengers. We identify three bottlenecks in our model: lack of sufﬁcient ID check points; exclusive assignment of screening check points to passengers; the presence of suspicious passengers.

<!-- b000030 | prose | pages [2] -->
For task (b), we propose three routing algorithms to optimize the throughput and variance of the airport: greedy algorithm, backpressure algorithm, and drift-plus-penalty algorithm. The best one of these algorithms achieves high throughput that is close to optimal and relatively low variance in waiting time. Besides, our proposed routing al- gorithm manages to retain passenger satisfaction while scheduling. We also explore the optimal ratio of different kinds of check points and test the robustness of modiﬁed mod- els.

<!-- b000031 | prose | pages [2] -->
For task (c), we analyze the impact of different cultures and traveler types and run simulation to see the reaction of our model. The cultures we analyze are collectivist cul- tures, individualist cultures. The types of travelers we analyze are family-based travelers and tech-based travelers. We also propose accommodations to these special situations.

<!-- b000032 | prose | pages [2] -->
For task (d), we propose both globally applicable and locally applicable policies to airport security managers. Our policies are based on our analysis of different cultures and types of travelers as well as our analysis of our routing algorithms.

<!-- b000033 | heading | pages [2] -->
Keywords: Queueing Networks; Routing Algorithms; Lyapunov Optimization

<!-- b000034 | furniture | pages [3] -->
Team # 55295

<!-- b000035 | heading | pages [3] -->
Contents

<!-- b000036 | contents | pages [3] -->
1

<!-- b000037 | heading | pages [3] -->
Introduction

<!-- b000038 | prose | pages [3] -->
2 Basic Analysis of the problem

<!-- b000039 | prose | pages [3] -->
1

<!-- b000040 | prose | pages [3] -->
1

<!-- b000041 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 Single Queueing Nodes 1

<!-- b000042 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 Parameter Settings 2

<!-- b000043 | prose | pages [3] -->
Rate Stability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 3

<!-- b000044 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4 Measures of Performance

<!-- b000045 | prose | pages [3] -->
3

<!-- b000046 | heading | pages [3] -->
Models

<!-- b000047 | prose | pages [3] -->
3

<!-- b000048 | prose | pages [3] -->
4

<!-- b000049 | prose | pages [3] -->
Tandem M/G/c Queueing Model . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4

<!-- b000050 | prose | pages [3] -->
Queueing Network Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000051 | prose | pages [3] -->
4 Simulations and Bottleneck Detection

<!-- b000052 | prose | pages [3] -->
5

<!-- b000053 | prose | pages [3] -->
6

<!-- b000054 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Simulation Setup 6

<!-- b000055 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Validating Our Model 6

<!-- b000056 | prose | pages [3] -->
Simulation Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3

<!-- b000057 | prose | pages [3] -->
5 Modiﬁcations to the Process

<!-- b000058 | prose | pages [3] -->
7

<!-- b000059 | prose | pages [3] -->
9

<!-- b000060 | prose | pages [3] -->
Greedy Routing Based on Backlogs . . . . . . . . . . . . . . . . . . . . . . . 5.1 9

<!-- b000061 | prose | pages [3] -->
Lyapunov Drift and Backpressure-Based Routing 5.2 . . . . . . . . . . . . . .

<!-- b000062 | prose | pages [3] -->
10

<!-- b000063 | prose | pages [3] -->
Lyapunov Optimization for Queueing Networks . . . . . . . . . . . 5.2.1 10

<!-- b000064 | prose | pages [3] -->
The Performance of Backpressure Routing 5.2.2 . . . . . . . . . . . . . .

<!-- b000065 | prose | pages [3] -->
11

<!-- b000066 | prose | pages [3] -->
Drift-Plus-Penalty Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 13

<!-- b000067 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.1 Drift-Plus-Penalty 13

<!-- b000068 | prose | pages [3] -->
The Performance of Drift-Plus-Penalty Algorithm . . . . . . . . . . 5.3.2

<!-- b000069 | prose | pages [3] -->
6

<!-- b000070 | heading | pages [3] -->
Sensitivity Analysis

<!-- b000071 | prose | pages [3] -->
14

<!-- b000072 | prose | pages [3] -->
14

<!-- b000073 | prose | pages [3] -->
Modeling Different Situations . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 15

<!-- b000074 | prose | pages [3] -->
Collectivist Cultural Norms . . . . . . . . . . . . . . . . . . . . . . . 6.1.1 15

<!-- b000075 | prose | pages [3] -->
Individualist Cultural Norms . . . . . . . . . . . . . . . . . . . . . . 6.1.2 15

<!-- b000076 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . 6.1.3 Family-based Travelers 16

<!-- b000077 | prose | pages [3] -->
Tech-based Travelers . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.4 16

<!-- b000078 | prose | pages [3] -->
Impact of Various Situations . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 16

<!-- b000079 | furniture | pages [4] -->
Team # 55295

<!-- b000080 | prose | pages [4] -->
Collectivist Cultural Norms . . . . . . . . . . . . . . . . . . . . . . . 6.2.1 16

<!-- b000081 | prose | pages [4] -->
Individualist Cultural Norms . . . . . . . . . . . . . . . . . . . . . . 6.2.2 17

<!-- b000082 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . 6.2.3 Family-based Travelers 17

<!-- b000083 | prose | pages [4] -->
Tech-based Travelers . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.4 18

<!-- b000084 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . 6.3 Accommodation for Situations

<!-- b000085 | prose | pages [4] -->
7

<!-- b000086 | heading | pages [4] -->
Conclusion

<!-- b000087 | prose | pages [4] -->
18

<!-- b000088 | prose | pages [4] -->
19

<!-- b000089 | prose | pages [4] -->
Conclusion of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 19

<!-- b000090 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Policy Proposal 19

<!-- b000091 | prose | pages [4] -->
Strength and Weakness of Our Model 7.3 . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | prose | pages [4] -->
19

<!-- b000093 | prose | pages [4] -->
Future Application of Models . . . . . . . . . . . . . . . . . . . . . . . . . . 7.4 20

<!-- b000094 | furniture | pages [5] -->
Page 1 of 20

<!-- b000095 | furniture | pages [5] -->
Team # 55295

<!-- b000096 | prose | pages [5] -->
1

<!-- b000097 | heading | pages [5] -->
Introduction

<!-- b000098 | prose | pages [5] -->
Security has been of ﬁrst priority in transportation activities that involve people since the beginning of the century. A series of time-consuming security check processes are necessary to ensure the security of all passengers aboard. But passengers are complain- ing about waiting for security check in extremely long queues. It is quite challenging to improve the performance of airport security check systems while preserving the current security standards.

<!-- b000099 | prose | pages [5] -->
In this paper, we try to model this security check process and reﬁne the model. Our main contributions are as follows:

<!-- b000100 | prose | pages [5] -->
1. We model the security check process with a queueing network. We validate our model by simulating it with real-world parameter combinations and comparing its result with real world data. We identify lack of sufﬁcient ID check points, exclusive assignment of screening check points, presence of suspicious passengers as three bottlenecks in the model.

<!-- b000101 | prose | pages [5] -->
2. We propose and implement three routing algorithms to optimize our basic mod- el. We simulate our model with these algorithms and analyze their performance. We ﬁnd that the proposed backpressure algorithm achieves throughput close to optimal and a relatively low variance in waiting time.

<!-- b000102 | prose | pages [5] -->
3. We analyze the sensitivity of our model by considering the impacts of cultural norms and passenger types. We analyze how the output of our model changes with respect to different norms and passengers, and propose accommodations to these situations.

<!-- b000103 | prose | pages [5] -->
2 Basic Analysis of the problem

<!-- b000104 | prose | pages [5] -->
2.1 Single Queueing Nodes

<!-- b000105 | prose | pages [5] -->
M/G/1 Queue: We adopt M/G/1 queue[1](shown in Figure 1(a)) in our model.

<!-- b000106 | prose | pages [5] -->
• M: the arrival times of the passengers follow a Poisson distribution

<!-- b000107 | prose | pages [5] -->
• G: the service times follow an arbitrary probability distribution

<!-- b000108 | prose | pages [5] -->
• 1: there is only one check point available

<!-- b000109 | prose | pages [5] -->
The arrivals are determined by a Poisson process with rate parameter µ. Job service time has a normal distribution with parameter µ and σ.

<!-- b000110 | prose | pages [5] -->
M/G/c Queue: We also adopt M/G/c queue(shown in Figure 1(b)) in our model, which is a generalization of the M/G/1 queue. c represents the number of check points. The arrival time of passengers follows a Poisson distribution with rate parameter λ. Job service time follows a normal distribution with parameter µ and σ.

<!-- b000111 | prose | pages [5] -->
FIFO: The queue obeys a ﬁrst-come, ﬁrst-served discipline. A single check point serves customers one at a time from the front of the queue. When the service is complete,

<!-- b000112 | furniture | pages [6] -->
Team # 55295

<!-- b000113 | prose | pages [6] -->
λ Poisson

<!-- b000114 | prose | pages [6] -->
μ

<!-- b000115 | prose | pages [6] -->
arrivals

<!-- b000116 | prose | pages [6] -->
Exponentially distributed

<!-- b000117 | prose | pages [6] -->
service time

<!-- b000118 | prose | pages [6] -->
(a) M/G/1

<!-- b000119 | furniture | pages [6] -->
Page 2 of 20

<!-- b000120 | prose | pages [6] -->
1

<!-- b000121 | prose | pages [6] -->
2

<!-- b000122 | prose | pages [6] -->
λ

<!-- b000123 | prose | pages [6] -->
3

<!-- b000124 | prose | pages [6] -->
Poisson arrivals

<!-- b000125 | prose | pages [6] -->
c

<!-- b000126 | prose | pages [6] -->
Exponentially distributed μ

<!-- b000127 | prose | pages [6] -->
service time

<!-- b000128 | prose | pages [6] -->
(b) M/G/c

<!-- b000129 | caption | pages [6] -->
Figure 1: Single Queueing Nodes

<!-- b000130 | prose | pages [6] -->
the customer leaves the queue and the number of customers in the system reduces by one.

<!-- b000131 | prose | pages [6] -->
2.2 Parameter Settings

<!-- b000132 | prose | pages [6] -->
Before the simulation, we set basic parameters of the probability distribution in queue- ing node based on the data in the data sheet. We use the EstimatedDistribution function of Mathematica to determine probability distributions and estimate parame- ters. The average interval for the arrival time of regular and pre-check passengers fol- 1 1 λ1 and λ2 respectively. And the average lows exponential distribution with parameter rate of ID check service in zone A and baggage and body screening follow normal dis- tribution with parameters (µ1, σ1) and (µ2, σ2). Besides, we assume the time for regular passengers to remove shoes, belts, light jackets and computers from their bags follows a normal distribution with the parameters (µ4, σ4). Thus the average rate of baggage and body screening for regular customer follows normal distribution with parameters

<!-- b000133 | prose | pages [6] -->
p

<!-- b000134 | prose | pages [6] -->
σ2

<!-- b000135 | prose | pages [6] -->
(µ3, σ3), where µ3 = µ2 + µ4 and σ3 =

<!-- b000136 | prose | pages [6] -->
2 + σ2 4. The normal distribution (µ3, σ3) and the normal distribution (µ4, σ4) are independent to each other. The speciﬁc numbers are in Table 1.

<!-- b000137 | prose | pages [6] -->
Symbol Deﬁnition λ1 value 4.63476 Rate of regular passenger arrivals λ2 6.52921 Rate of pre-check passenger arrivals (µ1, σ1) (0.186875, 0.0612029) Mean and variance of ID check service time

<!-- b000138 | prose | pages [6] -->
Mean and variance of screening service time (µ2, σ2)

<!-- b000139 | prose | pages [6] -->
(0.507639, 0.158551) for pre-check passengers

<!-- b000140 | prose | pages [6] -->
Mean and variance of screening service time (µ3, σ3)

<!-- b000141 | prose | pages [6] -->
(2.507639, 0.524536) for regular passengers

<!-- b000142 | caption | pages [6] -->
Table 1: The Parameters in the Problems

<!-- b000143 | prose | pages [6] -->
Times

<!-- b000144 | prose | pages [6] -->
Times

<!-- b000145 | prose | pages [6] -->
3.0

<!-- b000146 | prose | pages [6] -->
6

<!-- b000147 | prose | pages [6] -->
2.5

<!-- b000148 | prose | pages [6] -->
5

<!-- b000149 | prose | pages [6] -->
2.0

<!-- b000150 | prose | pages [6] -->
4

<!-- b000151 | prose | pages [6] -->
1.5

<!-- b000152 | prose | pages [6] -->
3

<!-- b000153 | prose | pages [6] -->
1.0

<!-- b000154 | prose | pages [6] -->
2

<!-- b000155 | prose | pages [6] -->
0.5

<!-- b000156 | prose | pages [6] -->
1

<!-- b000157 | prose | pages [6] -->
1.4 Arrving time interval(min)

<!-- b000158 | prose | pages [6] -->
Times

<!-- b000159 | prose | pages [6] -->
Times

<!-- b000160 | prose | pages [6] -->
2.5

<!-- b000161 | prose | pages [6] -->
6

<!-- b000162 | prose | pages [6] -->
2.0

<!-- b000163 | prose | pages [6] -->
5

<!-- b000164 | prose | pages [6] -->
4

<!-- b000165 | prose | pages [6] -->
1.5

<!-- b000166 | prose | pages [6] -->
3

<!-- b000167 | prose | pages [6] -->
1.0

<!-- b000168 | prose | pages [6] -->
2

<!-- b000169 | prose | pages [6] -->
0.5

<!-- b000170 | prose | pages [6] -->
1

<!-- b000171 | prose | pages [6] -->
0.6 Arrving time interval(min)

<!-- b000172 | prose | pages [6] -->
0.0

<!-- b000173 | prose | pages [6] -->
0

<!-- b000174 | prose | pages [6] -->
0.2 0.4 0.6 0.8 1.0 1.2

<!-- b000175 | prose | pages [6] -->
0.1 0.2 0.3 0.4 0.5

<!-- b000176 | prose | pages [6] -->
1.0 Service time(min)

<!-- b000177 | prose | pages [6] -->
0.4 Service time(min)

<!-- b000178 | prose | pages [6] -->
0.0

<!-- b000179 | prose | pages [6] -->
0

<!-- b000180 | prose | pages [6] -->
0.4 0.6 0.8

<!-- b000181 | prose | pages [6] -->
0.1 0.2 0.3

<!-- b000182 | caption | pages [6] -->
Figure 2: The Fitting Results from Mathematica

<!-- b000183 | prose | pages [6] -->
The distribution of service time in different check points s not identical in real life. In

<!-- b000184 | furniture | pages [7] -->
Team # 55295

<!-- b000185 | furniture | pages [7] -->
Page 3 of 20

<!-- b000186 | prose | pages [7] -->
order to simulate the differences among check points, we keep the variance of normal distribution σk unchanged(k = 1, 2, 3), and uniformly generate µki of normal distribu- tion between µk −σk and µk + σk.

<!-- b000187 | prose | pages [7] -->
2.3 Rate Stability

<!-- b000188 | prose | pages [7] -->
Due to the cost of hiring employees and maintaining the machine, it is impossible for airport to set up inﬁnite check points. But the airport makes sure that the number of check points satisﬁes the need of passengers and the number of passengers waiting in queue will not grow larger over time.

<!-- b000189 | prose | pages [7] -->
Let Q (t) represent the contents of a single queueing node deﬁned at time slots t ∈ {0, 1, 2, ...}. Q (t) is a stochastic process according to probability law. A queueing node

<!-- b000190 | prose | pages [7] -->
E{|Q(t)|}

<!-- b000191 | prose | pages [7] -->
= 0. Rate stability ensures the queue will not keep

<!-- b000192 | prose | pages [7] -->
is rate stable[2] if limt→∞

<!-- b000193 | prose | pages [7] -->
t growing over time. a (t) represents the number of new passengers that arrive on slot t and b (t) represents the number of passengers the check point of the queue can serve on slot t . Q (t) is rate stable if

<!-- b000194 | prose | pages [7] -->
t−1

<!-- b000195 | prose | pages [7] -->
1

<!-- b000196 | prose | pages [7] -->
X

<!-- b000197 | prose | pages [7] -->
lim supt→∞

<!-- b000198 | prose | pages [7] -->
t

<!-- b000199 | prose | pages [7] -->
τ=0

<!-- b000200 | prose | pages [7] -->
[a (τ) −b (τ)] ≤0.

<!-- b000201 | prose | pages [7] -->
We stipulate that the number of check points satisﬁes rate stability while the ratio of check points between the regular and pre-check passengers is 3 : 1. Therefore we set the number of check points as shown in Table 2.

<!-- b000202 | prose | pages [7] -->
zone ID check(zone A) Screening(zone B) regular pre-check 3 1 12 4

<!-- b000203 | caption | pages [7] -->
Table 2: The Number of Service Counters

<!-- b000204 | prose | pages [7] -->
2.4 Measures of Performance

<!-- b000205 | prose | pages [7] -->
Throughput and variance of average waiting time are two main measures in the se- curity check system. They are deﬁned as follows.

<!-- b000206 | prose | pages [7] -->
Throughput: The average number of passengers that pass the security check system in per unit time. The per unit time here is set as minute.

<!-- b000207 | prose | pages [7] -->
Variance: Suppose the waiting time for regular passenger is X1 and the waiting time for pre-check passenger is X2. The percentage of regular passengers is p. The variance of system is deﬁned as

<!-- b000208 | prose | pages [7] -->
h

<!-- b000209 | prose | pages [7] -->
(X1 −E (X1))2i

<!-- b000210 | prose | pages [7] -->
h

<!-- b000211 | prose | pages [7] -->
(X2 −E (X2))2i

<!-- b000212 | prose | pages [7] -->
+ (1 −p) E

<!-- b000213 | prose | pages [7] -->
pE

<!-- b000214 | prose | pages [7] -->
Throughput measures the security check system’s capacity on a collective level while variance of waiting time measures the fairness on an individual level.

<!-- b000215 | furniture | pages [8] -->
Page 4 of 20

<!-- b000216 | furniture | pages [8] -->
Team # 55295

<!-- b000217 | prose | pages [8] -->
3

<!-- b000218 | heading | pages [8] -->
Models

<!-- b000219 | prose | pages [8] -->
In this section, we ﬁrst present our models in details. The ﬁrst model is an optimal but unpractical model, which serves as a comparison and aims to provide modiﬁcation insights. The second one models the queueing networks of real security checking system in an airport.

<!-- b000220 | prose | pages [8] -->
Symbol Deﬁnition λ The rate parameter for the exponential distribution µ The mean value parameter for the normal distribution σ The rate parameter(squared scale) for the normal distribution N The number of check points Q(c)

<!-- b000221 | prose | pages [8] -->
The backlogs at queueing node a for passenger c at time t a (t)

<!-- b000222 | prose | pages [8] -->
The transmitting rate from queueing node a and queueing node b for

<!-- b000223 | prose | pages [8] -->
µ(c)

<!-- b000224 | prose | pages [8] -->
ab (t) passenger c at time t L(t) The Lyanpnov function at time t ∆(t) The Lyanpnov drift at time t V The control parameter in drift-plus-penalty algorithm

<!-- b000225 | caption | pages [8] -->
Table 3: Notations

<!-- b000226 | heading | pages [8] -->
Tandem M/G/c Queueing Model

<!-- b000227 | prose | pages [8] -->
3.1

<!-- b000228 | prose | pages [8] -->
We ﬁrst present an ideal model, the tandem M/G/c model. This model realizes the maximum throughput but is not feasible in the real life. We will later compare the per- formance of this ideal model with that of practical model to evaluate the latter and make modiﬁcation.

<!-- b000229 | prose | pages [8] -->
As Figure 3 demonstrates, two M/G/c queues are in a tandem array. The ﬁrst M/G/c queueing node denotes the queues of ID check(Zone A) and there are NA check points. Similarly, the second M/G/c queue denotes the queues of baggage and body screen- ing(Zone B) and there are NB check points. All check points are accessible to both reg- ular passengers and pre-check passengers and the only difference is that the pre-check passengers are likely to spend less time at Zone B.

<!-- b000230 | prose | pages [8] -->
Screening Check ID Check

<!-- b000231 | prose | pages [8] -->
λ1+λ2

<!-- b000232 | prose | pages [8] -->
Poisson arrivals

<!-- b000233 | prose | pages [8] -->
μ 2，σ 2    Regular Pax μ 1，σ 1 μ 3，σ 3  Pre-check Pax Normal distributed service time

<!-- b000234 | caption | pages [8] -->
Figure 3: Tandem M/G/c Queueing Model

<!-- b000235 | furniture | pages [9] -->
Page 5 of 20

<!-- b000236 | furniture | pages [9] -->
Team # 55295

<!-- b000237 | prose | pages [9] -->
Tandem M/G/c queueing model achieves the optimal performance. All check points in the same zone are busy as long as there are passengers waiting in queue. As for other models, a check point in one queueing node is idle when passengers are waiting before the line in another queueing node when a zone have more than one queueing node. In this way, tandem M/G/c model avoids unnecessary waiting time and attain the maximum throughput.

<!-- b000238 | prose | pages [9] -->
However, tandem M/G/c model is unpractical. For one thing, the single queue at ev- ery zone can be extremely long, which is hard to keep order. For another, access to every check points for both regular passengers and pre-check customers is feasible. Particular- ly, screening check points at zone B have different check process for these two kinds of passengers and it’s impossible to mix two process together.

<!-- b000239 | prose | pages [9] -->
Therefore, tandem M/G/c model has achieved maximum throughput but is unprac- tical in real life. This model is used for comparison with real-life model and provide insights for modiﬁcations later.

<!-- b000240 | prose | pages [9] -->
3.2

<!-- b000241 | heading | pages [9] -->
Queueing Network Model

<!-- b000242 | prose | pages [9] -->
Now we introduce queueing network model which models the security check in real- life airports. Queueing networks are systems in which a number of queues are connected by customer routing. Similar to BCMP networks[3], our queueing network models are open networks with very general service time which follows the normal distribution.

<!-- b000243 | prose | pages [9] -->
The queueing network in real-life airport is illustrated in Figure 4. Every queueing node is an M/G/1 queueing, for there is one queue for every check point. Regular pas- sengers and pre-check passengers are separate from each other in the entire process of security check. Every queueing node at zone A directs to its corresponding queueing nodes at zone B. We use NA1 and NA2 to denotes the number of queueing node in Zone A for regular passengers and pre-check passengers respectively and use NB1 and NB2 to denotes the number of queueing node in Zone B for regular passengers and pre-check passengers respectively.

<!-- b000244 | prose | pages [9] -->
ID Check Screening Check

<!-- b000245 | prose | pages [9] -->
Regular Pax

<!-- b000246 | prose | pages [9] -->
NB1

<!-- b000247 | prose | pages [9] -->
NA1 NA2

<!-- b000248 | prose | pages [9] -->
NB2

<!-- b000249 | prose | pages [9] -->
Pre-check Pax

<!-- b000250 | caption | pages [9] -->
Figure 4: Queueing Network Model

<!-- b000251 | prose | pages [9] -->
We will later modify the topology of queueing networks and apply different routing algorithms in queueing networks to achieve larger throughput and smaller variance in the queueing system.

<!-- b000252 | furniture | pages [10] -->
Page 6 of 20

<!-- b000253 | furniture | pages [10] -->
Team # 55295

<!-- b000254 | prose | pages [10] -->
4 Simulations and Bottleneck Detection

<!-- b000255 | prose | pages [10] -->
4.1 Simulation Setup

<!-- b000256 | prose | pages [10] -->
We run massive simulations on the queueing network model using the data from the real airports to validate the queueing network model.

<!-- b000257 | prose | pages [10] -->
We simulate both the tandem M/G/c network and queueing networks model. The simulation data is generated based on the probability distribution that we obtain from the data sheet. We set 1000 people to pass the system in every simulation and collect statistics of length of the queue, throughput, average, and variance of waiting time.

<!-- b000258 | prose | pages [10] -->
We also consider the presence of suspicious passengers in the security check system 1 in simulation. Every suspicious passenger appears with a probability of 1000 and the queue will be stuck for 10 min. We test the robustness of queueing system by adding the presence of suspicious passengers.

<!-- b000259 | prose | pages [10] -->
4.2

<!-- b000260 | heading | pages [10] -->
Validating Our Model

<!-- b000261 | prose | pages [10] -->
To validate our model, we simulate the model using real-world parameter combina- tions and compare the result with real-world data provided by airport passengers.

<!-- b000262 | prose | pages [10] -->
Speciﬁcally, we get the number of daily passengers of 5 biggest airports in the US from their ofﬁcial website [4][5][6][7][8]. We then assume that the arrival time of pas- sengers follow the Poisson distribution, and therefore we can calculate the mean arrival rate of passengers by dividing the total number of passengers with the time length of a day. Besides, we get the mean waiting time of passengers from [9]. Other parameters are set after the Bangkok International Airport, which is shown in Figure 5. After that, we simulate our model using the corresponding arrival time distribution. The result of our simulation is shown in Table 4.

<!-- b000263 | caption | pages [10] -->
Figure 5: Bangkok International Airport Security Check System

<!-- b000264 | furniture | pages [11] -->
Team # 55295

<!-- b000265 | prose | pages [11] -->
daily

<!-- b000266 | prose | pages [11] -->
Airport

<!-- b000267 | prose | pages [11] -->
arrival passengers

<!-- b000268 | prose | pages [11] -->
Chicago O’Hare 2, 000, 000 International(ORD)

<!-- b000269 | prose | pages [11] -->
Hartsﬁeld-Jackson Atlanta

<!-- b000270 | prose | pages [11] -->
260, 000 International(ATL)

<!-- b000271 | prose | pages [11] -->
Los Angeles 205,000 International(LAX)

<!-- b000272 | prose | pages [11] -->
John F. Kennedy 156, 000 International(JFK)

<!-- b000273 | prose | pages [11] -->
San Francisco 137,000 International(SFO)

<!-- b000274 | furniture | pages [11] -->
Page 7 of 20

<!-- b000275 | prose | pages [11] -->
average waiting

<!-- b000276 | prose | pages [11] -->
average waiting

<!-- b000277 | prose | pages [11] -->
time calculated

<!-- b000278 | prose | pages [11] -->
time from

<!-- b000279 | prose | pages [11] -->
by

<!-- b000280 | prose | pages [11] -->
websites(minute)

<!-- b000281 | prose | pages [11] -->
model(minute)

<!-- b000282 | prose | pages [11] -->
40 −60 79.0155

<!-- b000283 | prose | pages [11] -->
10 −20 42.9196

<!-- b000284 | prose | pages [11] -->
20 −30 32.5824

<!-- b000285 | prose | pages [11] -->
10 −20 16.8958

<!-- b000286 | prose | pages [11] -->
1 −10 9.4987

<!-- b000287 | caption | pages [11] -->
Table 4: Result of Validation Process

<!-- b000288 | prose | pages [11] -->
We can see from Table 4 that the resulting average waiting time of our model is gen- erally close to the real average waiting time and thus our model is valid in real life. The discrepancy between the model output and the ground truth can be explained as fol- lows. The number of check points of our model is far less than that of the real case. Since the real number of check points is unavailable online, so we have to estimate the num- ber from the fact that the waiting queue of clients is at least rate stable(as is discussed in section 2.3). That is, λ ≤c · µ, where λ is the arrival time, µ is the service rate(estimated from Excel data), and c is the number of check points. c obtained in this way is very like- ly to be far smaller than the real number of check points since real airports deploy more check points to deal with large number of passengers. In all, the inaccurate estimation of number of check points contributes to the discrepancy.

<!-- b000289 | prose | pages [11] -->
4.3 Simulation Evaluation

<!-- b000290 | prose | pages [11] -->
We now evaluate the simulation results given the parameters in our problem and analyze the bottleneck in current security check system.

<!-- b000291 | prose | pages [11] -->
The lack of sufﬁcient ID check points for pre-check passengers is a bottleneck in the queueing network model. From section 3.2, we see that the length of ID check queue for pre-check passengers grows quickly. However, the high speed of screening check point for pre-check passengers keeps the average waiting time for pre-check passengers much smaller than that of regular passengers. The imbalanced allocation of resource incurs congestion in the security system for pre-check users. Deploying one more ID check point for pre-check passengers, which is an effective but luxurious solution to the limit of ID check point, may not meet the approval due to the heavy cost.

<!-- b000292 | prose | pages [11] -->
The exclusive assignment of screening check points to some speciﬁc group of pas- sengers is another bottleneck. In this model, every ID check point only connects to 4 screening check points for the convenience of managing passengers and these 4 check points are exclusively used by passengers from the previous ID check point. In section 3.2, 4 screening queues from the same ID check points for regular passengers suffer from long queue while screening queues from other ID check points have much shorter queue.

<!-- b000293 | furniture | pages [12] -->
Team # 55295

<!-- b000294 | furniture | pages [12] -->
Page 8 of 20

<!-- b000295 | prose | pages [12] -->
Since the service time is not identical for every check point, a passenger from fast ID check points is possible to be directed to slow screening check points. In consequence, there might be certain screening check points suffering from long waiting queues and the separation of screening check points for regular customers results in the waste of resource.

<!-- b000296 | prose | pages [12] -->
80

<!-- b000297 | prose | pages [12] -->
Number of PAXin queue

<!-- b000298 | prose | pages [12] -->
60

<!-- b000299 | prose | pages [12] -->
40

<!-- b000300 | prose | pages [12] -->
20

<!-- b000301 | prose | pages [12] -->
0 0 50 100 150

<!-- b000302 | prose | pages [12] -->
Time/min

<!-- b000303 | prose | pages [12] -->
PreIDQ0

<!-- b000304 | prose | pages [12] -->
RegScreenQ02

<!-- b000305 | prose | pages [12] -->
RegIDQ0

<!-- b000306 | prose | pages [12] -->
RegScreenQ03

<!-- b000307 | prose | pages [12] -->
RegIDQ1

<!-- b000308 | prose | pages [12] -->
RegScreenQ10

<!-- b000309 | prose | pages [12] -->
RegIDQ2

<!-- b000310 | prose | pages [12] -->
RegScreenQ11

<!-- b000311 | prose | pages [12] -->
PreScreenQ00

<!-- b000312 | prose | pages [12] -->
RegScreenQ12

<!-- b000313 | prose | pages [12] -->
PreScreenQ01

<!-- b000314 | prose | pages [12] -->
RegScreenQ13

<!-- b000315 | prose | pages [12] -->
PreScreenQ02

<!-- b000316 | prose | pages [12] -->
RegScreenQ20

<!-- b000317 | prose | pages [12] -->
PreScreenQ03

<!-- b000318 | prose | pages [12] -->
RegScreenQ21

<!-- b000319 | prose | pages [12] -->
RegScreenQ00

<!-- b000320 | prose | pages [12] -->
RegScreenQ22

<!-- b000321 | prose | pages [12] -->
RegScreenQ01

<!-- b000322 | prose | pages [12] -->
RegScreenQ23

<!-- b000323 | caption | pages [12] -->
Figure 6: The Number of PAX in Queue in Queueing Network Model

<!-- b000324 | prose | pages [12] -->
Maxnumber of PAXin a queue

<!-- b000325 | prose | pages [12] -->
80

<!-- b000326 | prose | pages [12] -->
20

<!-- b000327 | prose | pages [12] -->
Number of PAXin queue

<!-- b000328 | prose | pages [12] -->
60

<!-- b000329 | prose | pages [12] -->
15

<!-- b000330 | prose | pages [12] -->
40

<!-- b000331 | prose | pages [12] -->
10

<!-- b000332 | prose | pages [12] -->
20

<!-- b000333 | prose | pages [12] -->
5

<!-- b000334 | prose | pages [12] -->
0

<!-- b000335 | prose | pages [12] -->
0

<!-- b000336 | prose | pages [12] -->
0 50 100 150 200

<!-- b000337 | prose | pages [12] -->
Time/min

<!-- b000338 | prose | pages [12] -->
ID Check Queue

<!-- b000339 | prose | pages [12] -->
Screening Check Queue

<!-- b000340 | prose | pages [12] -->
0 0 20 40 60 80 100 120

<!-- b000341 | prose | pages [12] -->
Time/min

<!-- b000342 | caption | pages [12] -->
Figure 8: The Number of PAX in Queue in Tandem

<!-- b000343 | caption | pages [12] -->
Figure 7: The Longest Queue with

<!-- b000344 | prose | pages [12] -->
M/G/c Queueing Model

<!-- b000345 | prose | pages [12] -->
Suspicious Passenger

<!-- b000346 | prose | pages [12] -->
The presence of suspicious passengers is the third bottleneck of this model. After analyzing Figure 6 and 7, the outline of 6 is the maximum number of passengers in a queue without the presence of suspicious people. Contrasting the Figure 7 with the outline of Figure 6, there is a suspicious passenger showing up at 88 minutes, which results in the rising slope increases for 15 minutes, and the maximum value is larger. At 152 minutes, another suspicious passenger arrives, which results in the maximum number of a queue keeping for 10 minutes instead of decreasing as in Figure 6. By comparing the ﬁgures, we ﬁnd that the presence of suspicious passengers will inﬂuence the stability of the system. In the airport, the suspicious passengers are more likely to be detected when the security check is strict especially in festivals or after certain events. So the inﬂuence of suspicious passengers should be considered as one of the bottlenecks of queueing network model.

<!-- b000347 | prose | pages [12] -->
These bottleneck of queueing networks model all result from the plain structure of security check system and oversimple queueing rules. In Figure 8, passengers wait in front of every queue node during the whole process and thus all the check points are working all the time. The results of tandem M/G/1 network model in Figure 8 show that the balance of all the queueing system enables the system to make full use of resource.

<!-- b000348 | furniture | pages [13] -->
Page 9 of 20

<!-- b000349 | furniture | pages [13] -->
Team # 55295

<!-- b000350 | prose | pages [13] -->
We will modify the security checking system to achieve a more efﬁcient use of resources in the next section.

<!-- b000351 | prose | pages [13] -->
5 Modiﬁcations to the Process

<!-- b000352 | prose | pages [13] -->
In this section we will introduce modiﬁcations for the bottleneck detected in the pre- vious section. We implement different routing algorithms and optimize the ratio of two kinds of passengers in order to achieve larger throughput and smaller variance.

<!-- b000353 | prose | pages [13] -->
5.1 Greedy Routing Based on Backlogs

<!-- b000354 | prose | pages [13] -->
We allow the queueing nodes to direct to more queueing nodes in this section. Pre- vious model have bottleneck where the queueing nodes corresponding to one node are busy and queueing nodes corresponding to another node are idle. Enabling passengers to make choice among more check points will make better use of the resource of check points by avoiding wastes. As Figure 9 demonstrated, both kinds of passengers are still prohibited to enter the check points of each for the privilege of the pre-check passenger- s, but all check points in zone B are accessible to passengers from the check point for passengers of the same kind in zone A.

<!-- b000355 | prose | pages [13] -->
Screening Check ID Check

<!-- b000356 | prose | pages [13] -->
Regular Pax

<!-- b000357 | prose | pages [13] -->
NB1

<!-- b000358 | prose | pages [13] -->
NA1 NA2

<!-- b000359 | prose | pages [13] -->
NB2

<!-- b000360 | prose | pages [13] -->
Pre-check Pax

<!-- b000361 | caption | pages [13] -->
Figure 9: The Queueing Network in Greedy Routing Based on Backlogs

<!-- b000362 | prose | pages [13] -->
We apply greedy routing based on the backlogs of the queueing node. The amount of total passengers waiting in queue nodes n are denoted as the backlog Qn (t). Every passenger makes the locally optimal choice of choosing the queueing node with the least queue backlog.

<!-- b000363 | prose | pages [13] -->
The results are illustrated in the Figure 10. The greedy algorithm achieves a much smaller queue size of less then 16 compared to the original model in section 3.2. Also, the total time required for all passengers to pass the line is much less. The throughput

<!-- b000364 | furniture | pages [14] -->
Team # 55295

<!-- b000365 | prose | pages [14] -->
15

<!-- b000366 | prose | pages [14] -->
Number of PAXin queue

<!-- b000367 | prose | pages [14] -->
10

<!-- b000368 | prose | pages [14] -->
5

<!-- b000369 | prose | pages [14] -->
0 0 20 40 60 80 100

<!-- b000370 | prose | pages [14] -->
Time/min

<!-- b000371 | furniture | pages [14] -->
Page 10 of 20

<!-- b000372 | prose | pages [14] -->
RegScreen7

<!-- b000373 | prose | pages [14] -->
RegID0

<!-- b000374 | prose | pages [14] -->
RegScreen8

<!-- b000375 | prose | pages [14] -->
RegID1

<!-- b000376 | prose | pages [14] -->
RegScreen9

<!-- b000377 | prose | pages [14] -->
RegID2

<!-- b000378 | prose | pages [14] -->
RegScreen10

<!-- b000379 | prose | pages [14] -->
RegScreen0

<!-- b000380 | prose | pages [14] -->
RegScreen11

<!-- b000381 | prose | pages [14] -->
RegScreen1

<!-- b000382 | prose | pages [14] -->
PreID0

<!-- b000383 | prose | pages [14] -->
RegScreen2

<!-- b000384 | prose | pages [14] -->
PreScreen0

<!-- b000385 | prose | pages [14] -->
RegScreen3

<!-- b000386 | prose | pages [14] -->
PreScreen1

<!-- b000387 | prose | pages [14] -->
RegScreen4

<!-- b000388 | prose | pages [14] -->
PreScreen2

<!-- b000389 | prose | pages [14] -->
RegScreen5

<!-- b000390 | prose | pages [14] -->
120

<!-- b000391 | prose | pages [14] -->
PreScreen3

<!-- b000392 | prose | pages [14] -->
RegScreen6

<!-- b000393 | caption | pages [14] -->
Figure 10: The Number of PAX in Queue in Greedy Routing Based on Backlogs

<!-- b000394 | prose | pages [14] -->
is 7.148PAX/min and the variance of waiting time is 103.427min2 The queueing system in greedy algorithm has better performance than the original model.

<!-- b000395 | prose | pages [14] -->
Lyapunov Drift and Backpressure-Based Routing 5.2

<!-- b000396 | prose | pages [14] -->
Lyapunov Optimization for Queueing Networks 5.2.1

<!-- b000397 | prose | pages [14] -->
Consider a queueing network with N queueing nodes in discrete time slots t in {0, 1, 2, ...}. On each slot, routing and transmission scheduling decisions are made in an effort to deliver passenger to destination. Let Q(c)

<!-- b000398 | prose | pages [14] -->
n (t), where c can be both regular and pre-check passengers, be the current amount of passenger in node n, also called the queue backlog. The queue backlogs from one slot to the next satisﬁes the following for all n ∈{1, ..., N}, c ∈{regular, pre −check}:

<!-- b000399 | prose | pages [14] -->
N

<!-- b000400 | prose | pages [14] -->
"

<!-- b000401 | prose | pages [14] -->
X

<!-- b000402 | prose | pages [14] -->
Q(c)

<!-- b000403 | prose | pages [14] -->
Q(c)

<!-- b000404 | prose | pages [14] -->
n (t + 1) ≤max

<!-- b000405 | prose | pages [14] -->
n (t) −

<!-- b000406 | prose | pages [14] -->
b=1

<!-- b000407 | prose | pages [14] -->
where A(c)

<!-- b000408 | prose | pages [14] -->
N

<!-- b000409 | prose | pages [14] -->
#

<!-- b000410 | prose | pages [14] -->
µ(c)

<!-- b000411 | prose | pages [14] -->
X

<!-- b000412 | prose | pages [14] -->
µ(c)

<!-- b000413 | prose | pages [14] -->
an (t) + A(c)

<!-- b000414 | prose | pages [14] -->
nb (t) , 0

<!-- b000415 | prose | pages [14] -->
+

<!-- b000416 | prose | pages [14] -->
n (t)

<!-- b000417 | prose | pages [14] -->
a=1

<!-- b000418 | prose | pages [14] -->
n (t) is the random amount of passengers that exogenously arrives to node n on slot t, and µ(c)

<!-- b000419 | prose | pages [14] -->
ab (t) is the transmission rate allocated to passenger c on link (a, b) on slot t. Note that µ(c)

<!-- b000420 | prose | pages [14] -->
ab (t) may be more than the amount of passengers c that is actually transmitted on link (a, b) on slot t. This is because there may not be enough backlog in node a.

<!-- b000421 | prose | pages [14] -->
The backpressure algorithm[10] is designed by choosing transmission and routing variables to greedily minimize a bound on the drift of a Lyapunov function. Speciﬁcally, deﬁne Q (t) = Q(c)

<!-- b000422 | prose | pages [14] -->
n (t) as the matrix of current queue backlogs. Deﬁne the Lyapunov function

<!-- b000423 | prose | pages [14] -->
N

<!-- b000424 | prose | pages [14] -->
L (t) = 1

<!-- b000425 | prose | pages [14] -->
X

<!-- b000426 | prose | pages [14] -->
2

<!-- b000427 | prose | pages [14] -->
i=1

<!-- b000428 | prose | pages [14] -->
(t)2 .

<!-- b000429 | prose | pages [14] -->
Q(c)

<!-- b000430 | prose | pages [14] -->
X

<!-- b000431 | prose | pages [14] -->
i

<!-- b000432 | prose | pages [14] -->
c

<!-- b000433 | prose | pages [14] -->
This fuction is a scalar measure of the total queue backlog in the network. Note that this is a sum of the squares of queue backlogs. Thus the backlogs in every Queues are small if the Lyanpnov function is small. Then the Lyapunov drift is deﬁned as the change in

<!-- b000434 | furniture | pages [15] -->
Team # 55295

<!-- b000435 | prose | pages [15] -->
this function from one slot to the next:

<!-- b000436 | furniture | pages [15] -->
Page 11 of 20

<!-- b000437 | prose | pages [15] -->
∆(t) = E {L (t + 1) −L (t) |Q (t)} .

<!-- b000438 | prose | pages [15] -->
We intend to minimize the Lyapunov drift so as to minimize the total queue backlog in the network as time goes by.

<!-- b000439 | prose | pages [15] -->
We transform the equation using the inequality of backlog from one slot to another slot

<!-- b000440 | prose | pages [15] -->
N

<!-- b000441 | prose | pages [15] -->
(

<!-- b000442 | prose | pages [15] -->
Q(c)

<!-- b000443 | prose | pages [15] -->
X

<!-- b000444 | prose | pages [15] -->
X

<!-- b000445 | prose | pages [15] -->
(t) E

<!-- b000446 | prose | pages [15] -->
λ(c)

<!-- b000447 | prose | pages [15] -->
∆(t) ≤B +

<!-- b000448 | prose | pages [15] -->
N

<!-- b000449 | prose | pages [15] -->
N

<!-- b000450 | prose | pages [15] -->
)

<!-- b000451 | prose | pages [15] -->
µ(c)

<!-- b000452 | prose | pages [15] -->
X

<!-- b000453 | prose | pages [15] -->
X

<!-- b000454 | prose | pages [15] -->
µ(c)

<!-- b000455 | prose | pages [15] -->
an (t) −

<!-- b000456 | prose | pages [15] -->
nb (t) |Q (t)

<!-- b000457 | prose | pages [15] -->
,

<!-- b000458 | prose | pages [15] -->
n (t) +

<!-- b000459 | prose | pages [15] -->
i

<!-- b000460 | prose | pages [15] -->
c

<!-- b000461 | prose | pages [15] -->
n=1

<!-- b000462 | prose | pages [15] -->


<!-- b000463 | prose | pages [15] -->


<!-- b000464 | prose | pages [15] -->
λ(c)

<!-- b000465 | prose | pages [15] -->
where B is a ﬁnite constant and

<!-- b000466 | prose | pages [15] -->
n (t)

<!-- b000467 | prose | pages [15] -->


<!-- b000468 | prose | pages [15] -->


<!-- b000469 | prose | pages [15] -->
λ(c)

<!-- b000470 | prose | pages [15] -->
n (t)

<!-- b000471 | prose | pages [15] -->
a=1

<!-- b000472 | prose | pages [15] -->
b=1

<!-- b000473 | prose | pages [15] -->
is passenger arrival rate matrix. Since B and

<!-- b000474 | prose | pages [15] -->
is constant, we maximize the following terms to minimizing the Lyanpnov drift

<!-- b000475 | prose | pages [15] -->
N

<!-- b000476 | prose | pages [15] -->
N

<!-- b000477 | prose | pages [15] -->
µ(c)

<!-- b000478 | prose | pages [15] -->
X

<!-- b000479 | prose | pages [15] -->
X

<!-- b000480 | prose | pages [15] -->
X

<!-- b000481 | prose | pages [15] -->
ab (t)

<!-- b000482 | prose | pages [15] -->
c

<!-- b000483 | prose | pages [15] -->
a=1

<!-- b000484 | prose | pages [15] -->
b=1

<!-- b000485 | prose | pages [15] -->
The weight Q(c)

<!-- b000486 | prose | pages [15] -->
a (t) −Q(c)

<!-- b000487 | prose | pages [15] -->
i

<!-- b000488 | prose | pages [15] -->
h h

<!-- b000489 | prose | pages [15] -->
a (t) −Q(c)

<!-- b000490 | prose | pages [15] -->
Q(c)

<!-- b000491 | prose | pages [15] -->
(t)

<!-- b000492 | prose | pages [15] -->
.

<!-- b000493 | prose | pages [15] -->
b

<!-- b000494 | prose | pages [15] -->
(t) is called the current differential backlog of c between nodes b

<!-- b000495 | prose | pages [15] -->


<!-- b000496 | prose | pages [15] -->


<!-- b000497 | prose | pages [15] -->
µ(c)

<!-- b000498 | prose | pages [15] -->
a and b. Thus, we want to choose decision variables

<!-- b000499 | prose | pages [15] -->
ab (t)

<!-- b000500 | prose | pages [15] -->
so as to maximize the above weighted sum, where weights are differential backlogs.

<!-- b000501 | prose | pages [15] -->
Clearly we should not send data in a direction of negative differential backlog, and so we should choose µ(c)

<!-- b000502 | prose | pages [15] -->
ab (t) = 0 whenever the differential backlog is negative. Further, giv-

<!-- b000503 | prose | pages [15] -->
ab (t) for a particular link (a, b), the optimal µ(c)

<!-- b000504 | prose | pages [15] -->
en µ(c)

<!-- b000505 | prose | pages [15] -->
copt ab (t) are chosen as follows: ﬁrst ﬁnd

<!-- b000506 | prose | pages [15] -->
ab (t) that maximize the differential backlog for link (a, b). If this maximizing differen- tial backlog is negative, assign µ(c)

<!-- b000507 | prose | pages [15] -->
ab (t) = 0 for both kinds of passengers. Else, allocate the full link rate µab (t) to the passengers copt

<!-- b000508 | prose | pages [15] -->
ab (t), and zero rate to the other passengers on this link. With this choice, our aim is to maximize

<!-- b000509 | prose | pages [15] -->
N

<!-- b000510 | prose | pages [15] -->
N

<!-- b000511 | prose | pages [15] -->
X

<!-- b000512 | prose | pages [15] -->
X

<!-- b000513 | prose | pages [15] -->


<!-- b000514 | prose | pages [15] -->


<!-- b000515 | prose | pages [15] -->
copt(t)

<!-- b000516 | prose | pages [15] -->
copt(t)

<!-- b000517 | prose | pages [15] -->
(t) −Q

<!-- b000518 | prose | pages [15] -->
(t)

<!-- b000519 | prose | pages [15] -->
Wab (t) = max µabWab (t) (t) , where

<!-- b000520 | prose | pages [15] -->
a=1

<!-- b000521 | prose | pages [15] -->
b=1

<!-- b000522 | prose | pages [15] -->
Q

<!-- b000523 | prose | pages [15] -->
ab

<!-- b000524 | prose | pages [15] -->
ab

<!-- b000525 | prose | pages [15] -->
a

<!-- b000526 | prose | pages [15] -->
b

<!-- b000527 | prose | pages [15] -->
choosing µ (ab) is called the max-weight algorithm. It maximizes a linear sum of trans- mission rates, where the weights Wab (t) correspond to differential backlogs. The back- pressure algorithm uses the max-weight decisions for µab (t), and then chooses routing

<!-- b000528 | prose | pages [15] -->


<!-- b000529 | prose | pages [15] -->


<!-- b000530 | prose | pages [15] -->
µ(c)

<!-- b000531 | prose | pages [15] -->
ab (t)

<!-- b000532 | prose | pages [15] -->
via the maximum differential backlog as described above.

<!-- b000533 | prose | pages [15] -->
variables

<!-- b000534 | prose | pages [15] -->
The Performance of Backpressure Routing 5.2.2

<!-- b000535 | prose | pages [15] -->
Now we apply the backpressure routing to the queueing network model. The trans- mitting rate µ(c)

<!-- b000536 | prose | pages [15] -->
ab (t) has an inverse relationship with the current serving time of queueing node a. Except the rules in 5.2.1, pre-check passengers are able to queue before the check points for regular passengers. However, they receive the same check process and spend the same time as the regular passengers. This assumption is reasonable, for pre-check passengers have rights to go to regular check points when their own check points are too busy. The diagram of the queueing network is illustrated in Figure 11.

<!-- b000537 | furniture | pages [16] -->
Team # 55295

<!-- b000538 | prose | pages [16] -->
ID Check

<!-- b000539 | furniture | pages [16] -->
Page 12 of 20

<!-- b000540 | prose | pages [16] -->
Screening Check

<!-- b000541 | prose | pages [16] -->
Regular Pax

<!-- b000542 | prose | pages [16] -->
Pre-check Pax

<!-- b000543 | caption | pages [16] -->
Figure 11: The Queueing Network in Backpressure Routing

<!-- b000544 | caption | pages [16] -->
Figure 12 demonstrates the results of the backpressure routing. Compared to Figure

<!-- b000545 | prose | pages [16] -->
10 in greedy routing, the longest queue is the same. Although more queues are likely to have the long queues, this result from shorter service time of these check point. The graph also shows that it takes less time for all passengers to pass the security check The throughput is 7.328PAX/min, which is closer to systems than greedy routing. 7.673PAX/min of the optimal models than greedy routing. The variance of waiting time is 84.971min2, smaller than that of greedy routing.

<!-- b000546 | prose | pages [16] -->
14

<!-- b000547 | prose | pages [16] -->
12

<!-- b000548 | prose | pages [16] -->
Number of PAXin queue

<!-- b000549 | prose | pages [16] -->
10

<!-- b000550 | prose | pages [16] -->
8

<!-- b000551 | prose | pages [16] -->
6

<!-- b000552 | prose | pages [16] -->
4

<!-- b000553 | prose | pages [16] -->
2

<!-- b000554 | prose | pages [16] -->
0 0 20 40 60 80 100 120

<!-- b000555 | prose | pages [16] -->
Time/min

<!-- b000556 | prose | pages [16] -->
IDCheck0

<!-- b000557 | prose | pages [16] -->
ScreenCheck6

<!-- b000558 | prose | pages [16] -->
IDCheck1

<!-- b000559 | prose | pages [16] -->
ScreenCheck7

<!-- b000560 | prose | pages [16] -->
IDCheck2

<!-- b000561 | prose | pages [16] -->
ScreenCheck8

<!-- b000562 | prose | pages [16] -->
IDCheck3

<!-- b000563 | prose | pages [16] -->
ScreenCheck9

<!-- b000564 | prose | pages [16] -->
ScreenCheck0

<!-- b000565 | prose | pages [16] -->
ScreenCheck10

<!-- b000566 | prose | pages [16] -->
ScreenCheck1

<!-- b000567 | prose | pages [16] -->
ScreenCheck11

<!-- b000568 | prose | pages [16] -->
ScreenCheck2

<!-- b000569 | prose | pages [16] -->
ScreenCheck12

<!-- b000570 | prose | pages [16] -->
ScreenCheck3

<!-- b000571 | prose | pages [16] -->
ScreenCheck13

<!-- b000572 | prose | pages [16] -->
ScreenCheck4

<!-- b000573 | prose | pages [16] -->
ScreenCheck14

<!-- b000574 | prose | pages [16] -->
ScreenCheck5

<!-- b000575 | prose | pages [16] -->
ScreenCheck15

<!-- b000576 | caption | pages [16] -->
Figure 12: The Number of PAX in Queue in Backpressure Routing

<!-- b000577 | prose | pages [16] -->
The robustness of the queueing networks improves when suspicious passengers pass the system. As illustrated in Figure 13a, where the dash line denotes the arrival of the suspicious passengers, the longest line is almost the same as the outline of Figure 12 and the queueing networks are rather stable. The queueing network is almost immune to the suspicious passengers.

<!-- b000578 | prose | pages [16] -->
We also explore the optimal ratio between regular and pre-check passengers(Figure 14). We adjust the ratio of check points in zone B, where exists most of the long queues and we have 16 check points in the zone B. The throughput increases sharply at ﬁrst and then ﬂuctuates around 7.3 while the variance of average waiting time goes directly down with the increase of check points for regular passengers. 13 check points for regular passengers is a proper choice for the queueing system in backpressure algorithm, for it maintains a relatively small variance as well as the largest throughput.

<!-- b000579 | furniture | pages [17] -->
Team # 55295

<!-- b000580 | prose | pages [17] -->
20

<!-- b000581 | prose | pages [17] -->
Maxnumber of PAXin a queue

<!-- b000582 | prose | pages [17] -->
15

<!-- b000583 | prose | pages [17] -->
10

<!-- b000584 | prose | pages [17] -->
5

<!-- b000585 | prose | pages [17] -->
0 0 20 40 60 80 100 120 140

<!-- b000586 | prose | pages [17] -->
Time/min

<!-- b000587 | prose | pages [17] -->
(a) Backpressure Routing

<!-- b000588 | furniture | pages [17] -->
Page 13 of 20

<!-- b000589 | prose | pages [17] -->
20

<!-- b000590 | prose | pages [17] -->
Maxnumber of PAXin a queue

<!-- b000591 | prose | pages [17] -->
15

<!-- b000592 | prose | pages [17] -->
10

<!-- b000593 | prose | pages [17] -->
5

<!-- b000594 | prose | pages [17] -->
0 0 50 100 150

<!-- b000595 | prose | pages [17] -->
Time/min

<!-- b000596 | prose | pages [17] -->
(b) Drift-Plus-Penalty Algorithm

<!-- b000597 | caption | pages [17] -->
Figure 13: The Longest Queue in the Network(The Dash Line Denotes the Arrival of

<!-- b000598 | prose | pages [17] -->
Suspicious Passengers)

<!-- b000599 | prose | pages [17] -->
7.6

<!-- b000600 | prose | pages [17] -->
7.4

<!-- b000601 | prose | pages [17] -->
Throughput PAX/min

<!-- b000602 | prose | pages [17] -->
7.2

<!-- b000603 | prose | pages [17] -->
7.0

<!-- b000604 | prose | pages [17] -->
6.8

<!-- b000605 | prose | pages [17] -->
6.6

<!-- b000606 | prose | pages [17] -->
6.4

<!-- b000607 | prose | pages [17] -->
6.2 0 2 4 6 8 10 12 14

<!-- b000608 | prose | pages [17] -->
Number of TSA regular check points

<!-- b000609 | prose | pages [17] -->
250

<!-- b000610 | prose | pages [17] -->
200

<!-- b000611 | prose | pages [17] -->
Variance/min 2

<!-- b000612 | prose | pages [17] -->
150

<!-- b000613 | prose | pages [17] -->
100

<!-- b000614 | prose | pages [17] -->
50

<!-- b000615 | prose | pages [17] -->
0 0 2 4 6 8 10 12 14

<!-- b000616 | prose | pages [17] -->
Number of TSA regular check points

<!-- b000617 | caption | pages [17] -->
Figure 14: Throughput and Variance of Different Ratio Between Regular and Pre-check

<!-- b000618 | prose | pages [17] -->
Check Points(16 Check Points in total)

<!-- b000619 | prose | pages [17] -->
5.3

<!-- b000620 | heading | pages [17] -->
Drift-Plus-Penalty Algorithm

<!-- b000621 | prose | pages [17] -->
5.3.1 Drift-Plus-Penalty

<!-- b000622 | prose | pages [17] -->
We intend to reduce the number of pre-check passengers to enter the check points compared to the previous routing algorithm under the same rule. Previous routing algo- rithm requires the pre-check passengers to enter the check points for regular customers to achieve larger throughput and smaller variance. Since the pre-check passengers pay extra money for better-service, they may be reluctant to receive the security check like the regular customers. Therefore, we improve the previous routing algorithm.

<!-- b000623 | prose | pages [17] -->
V penalty (t) term is introduced to the Lyapunov drift in the previous backpressure routing. Instead of taking a control action to minimize a bound on ∆(t), we minimize a bound the following drift-plus-penalty expression:

<!-- b000624 | prose | pages [17] -->
∆(t) + V E {penalty (t)}

<!-- b000625 | prose | pages [17] -->
where V ≥0 is a parameter that represents an “importance weight” on how much we emphasize to reduce the number of the pre-check passengers to enter the check point for regular passengers.

<!-- b000626 | prose | pages [17] -->
In the same way that minimizing a bound on ∆(t) leads to an expression ∆(t) ≤B, minimizing a bound on the drift-plus-penalty leads to an expression of the form:

<!-- b000627 | prose | pages [17] -->
∆(t) + V E {penalty (t)} ≤B + V p∗,

<!-- b000628 | prose | pages [17] -->
where p∗is the optimal time average penalty.

<!-- b000629 | furniture | pages [18] -->
Team # 55295

<!-- b000630 | furniture | pages [18] -->
Page 14 of 20

<!-- b000631 | heading | pages [18] -->
The Performance of Drift-Plus-Penalty Algorithm

<!-- b000632 | prose | pages [18] -->
5.3.2

<!-- b000633 | prose | pages [18] -->
We apply the drift-plus-penalty algorithm in the problem. Let V = 0.5 and penalty (t) =

<!-- b000634 | prose | pages [18] -->


<!-- b000635 | prose | pages [18] -->


<!-- b000636 | prose | pages [18] -->
−Q(c)

<!-- b000637 | prose | pages [18] -->
1

<!-- b000638 | prose | pages [18] -->
t(c)

<!-- b000639 | prose | pages [18] -->
 

<!-- b000640 | prose | pages [18] -->
when we transmit pre-check passengers from queueing node a to

<!-- b000641 | prose | pages [18] -->
Qa

<!-- b000642 | prose | pages [18] -->
(t) b

<!-- b000643 | prose | pages [18] -->
2

<!-- b000644 | prose | pages [18] -->
queueing node b.

<!-- b000645 | prose | pages [18] -->
The results of drift-plus-penalty algorithm are demonstrate in Figure 15. The back- logs are larger than the backpressure routing as some queue reach over 14 and the largest backlog attain 20. Also, it takes more time for all passengers to pass the security check. The throughput of the system is 7.224PAX/min and the variance of waiting time is 149.880min2, both of the result are worse off compared to the backpressure routing. This algorithm sacriﬁce the throughput and variance of waiting time to maintain the right of pre-check users.

<!-- b000646 | prose | pages [18] -->
20

<!-- b000647 | prose | pages [18] -->
Number of PAXin queue

<!-- b000648 | prose | pages [18] -->
15

<!-- b000649 | prose | pages [18] -->
10

<!-- b000650 | prose | pages [18] -->
5

<!-- b000651 | prose | pages [18] -->
0 0 20 40 60 80 100 120

<!-- b000652 | prose | pages [18] -->
Time/min

<!-- b000653 | prose | pages [18] -->
IDCheck0

<!-- b000654 | prose | pages [18] -->
ScreenCheck6

<!-- b000655 | prose | pages [18] -->
IDCheck1

<!-- b000656 | prose | pages [18] -->
ScreenCheck7

<!-- b000657 | prose | pages [18] -->
IDCheck2

<!-- b000658 | prose | pages [18] -->
ScreenCheck8

<!-- b000659 | prose | pages [18] -->
IDCheck3

<!-- b000660 | prose | pages [18] -->
ScreenCheck9

<!-- b000661 | prose | pages [18] -->
ScreenCheck0

<!-- b000662 | prose | pages [18] -->
ScreenCheck10

<!-- b000663 | prose | pages [18] -->
ScreenCheck1

<!-- b000664 | prose | pages [18] -->
ScreenCheck11

<!-- b000665 | prose | pages [18] -->
ScreenCheck2

<!-- b000666 | prose | pages [18] -->
ScreenCheck12

<!-- b000667 | prose | pages [18] -->
ScreenCheck3

<!-- b000668 | prose | pages [18] -->
ScreenCheck13

<!-- b000669 | prose | pages [18] -->
ScreenCheck4

<!-- b000670 | prose | pages [18] -->
ScreenCheck14

<!-- b000671 | prose | pages [18] -->
140

<!-- b000672 | prose | pages [18] -->
ScreenCheck5

<!-- b000673 | prose | pages [18] -->
ScreenCheck15

<!-- b000674 | caption | pages [18] -->
Figure 15: The Number of PAX in Queue in Drift-Plus-Penalty Algorithm

<!-- b000675 | prose | pages [18] -->
We also look into the robustness of the queueing networks when suspicious passen- gers enter security check system. Figure 13b illustrates the longest queue in the security check system and the dash line means the time when the suspicious passengers pass. Only a small increase in slope shows up in Figure 13b compared to the outline of Figure 15 and the increase diminishes quickly in less than 5 minutes. This means the queue length of are less susceptible to this kind of emergency case.

<!-- b000676 | prose | pages [18] -->
We explore the optimal ratio between regular and pre-check passengers(Figure 16). As most long queues exist in zone B, we intend to adjust the ratio of check points in zone B. Suppose we have 16 check points in the zone B. The throughput increases sharply at ﬁrst and then ﬂuctuates around 7.2 while the variance of average waiting time goes directly down with the increase of check points for regular passengers. We choose 11 check points for regular passengers, which lead to a relatively small variance as well as a large throughput.

<!-- b000677 | prose | pages [18] -->
6

<!-- b000678 | heading | pages [18] -->
Sensitivity Analysis

<!-- b000679 | prose | pages [18] -->
We perform sensitivity analysis on our model by considering the cultural impacts on the parameters. More speciﬁcally, we examine several different cultural norms and model them as changes to input parameters of our model. Then we are able to tell the exact impacts of different cultural norms by comparing the performance metrics of our

<!-- b000680 | furniture | pages [19] -->
Team # 55295

<!-- b000681 | prose | pages [19] -->
7.5

<!-- b000682 | prose | pages [19] -->
Throughput (PAX/min)

<!-- b000683 | prose | pages [19] -->
7.0

<!-- b000684 | prose | pages [19] -->
6.5

<!-- b000685 | prose | pages [19] -->
6.0

<!-- b000686 | prose | pages [19] -->
0 2 4 6 8 10 12 14

<!-- b000687 | prose | pages [19] -->
Number of TSA regular check points

<!-- b000688 | furniture | pages [19] -->
Page 15 of 20

<!-- b000689 | prose | pages [19] -->
300

<!-- b000690 | prose | pages [19] -->
250

<!-- b000691 | prose | pages [19] -->
Variance/min 2

<!-- b000692 | prose | pages [19] -->
200

<!-- b000693 | prose | pages [19] -->
150

<!-- b000694 | prose | pages [19] -->
100

<!-- b000695 | prose | pages [19] -->
50

<!-- b000696 | prose | pages [19] -->
0 0 2 4 6 8 10 12 14

<!-- b000697 | prose | pages [19] -->
Number of TSA regular check points

<!-- b000698 | caption | pages [19] -->
Figure 16: Throughput and Variance of Different Ratio Between Regular and Pre-check

<!-- b000699 | prose | pages [19] -->
Check Points(16 Check Points in total)

<!-- b000700 | prose | pages [19] -->
model under different parameter combinations.

<!-- b000701 | prose | pages [19] -->
6.1

<!-- b000702 | heading | pages [19] -->
Modeling Different Situations

<!-- b000703 | prose | pages [19] -->
We will present the modeling of four different situations(including those in different cultural norms and different types of traveler) in this section. The evaluation of the impacts of these situations will be provided in section 6.2. The accommodation to these situations will be provided in section 6.3.

<!-- b000704 | prose | pages [19] -->
6.1.1 Collectivist Cultural Norms

<!-- b000705 | prose | pages [19] -->
Switzerland is a country whose Power Distance Index(PDI), an indicator that ex- presses the public’s general acceptance towards inequalities, is lower than that of most countries [11]. Believing that inequalities among people should be minimized, Swiss people tend to prioritize collective efﬁciency, which motivates us to model their willing- ness to sacriﬁce personal gains for the good of the public.

<!-- b000706 | prose | pages [19] -->
We change the control parameter V of the drift-plus-penalty model to describe such willingness. As is discussed in section 5.3.1, V stands for the penalty of scheduling a pre-check passenger to regular check points, a decision that will improve the global throughput and variance but cost the pre-check passenger more time. A passenger from collectivist cultures(as those in Switzerland) may readily follow the schedule and thus has a small control parameter.

<!-- b000707 | prose | pages [19] -->
6.1.2 Individualist Cultural Norms

<!-- b000708 | prose | pages [19] -->
In contrast to what was believed by Chinese a thousand years ago, individual efﬁ- ciency is the dominating factor in the code of conduct of Chinese today. The act of cutting in line, carried out by those who desperately seek individual efﬁciency, can be observed in some airports in China. This leads us to model the act of skipping by adding new queueing rules to our model.

<!-- b000709 | prose | pages [19] -->
As is shown in section 2.1 ,our model naturally supports the ﬁrst-in-ﬁrst-out queue- ing rule. To model the skipping acts, a new passenger can now go to the head of the queue. The probability of a passenger going to the head of a queue is 30%, a value estimated from daily life experience.

<!-- b000710 | furniture | pages [20] -->
Team # 55295

<!-- b000711 | prose | pages [20] -->
6.1.3 Family-based Travelers

<!-- b000712 | furniture | pages [20] -->
Page 16 of 20

<!-- b000713 | prose | pages [20] -->
Familial relationships are cherished in almost all cultures. Flying with family mem- bers to some fascinating destinations is a good choice of spending vacations as well as enhancing family ties. This traveling situation motivates us to model the family-based travelers with different passenger arrival distribution.

<!-- b000714 | prose | pages [20] -->
In the previous discussion, we have mentioned that our model assumes the arriving passengers are a Poisson ﬂow(section 2.1). The family-based travelers do not follow the Poisson distribution since they arrive at the same time, which is a safe assumption. Also, we assume that family-based travelers from the same family will process through the same check point and that they are always consecutive in a queue.

<!-- b000715 | prose | pages [20] -->
6.1.4 Tech-based Travelers

<!-- b000716 | prose | pages [20] -->
Our last proposed situation consists of travelers who turn to modern communication technology for an accurate estimation of waiting time. A growing number of airports collect the queueing information in the airport and push estimated waiting time to pas- sengers through mobile apps. In this way, the passengers are aware of the queueing situations and are able to better arrange their trips to the airport. We model this type of travelers using different arrival distribution.

<!-- b000717 | prose | pages [20] -->
Similar to the situation in section 6.1.3, with a-prior knowledge, the arriving passen- gers do not follow poisson distribution. We therefore model the arrival time of these travelers as a random variable following a normal distribution whose parameters are estimated through life experiences: the mean value of this distribution is 30 minutes be- fore the departure time, and the variance depends on the accuracy of the information provided by the airport.

<!-- b000718 | prose | pages [20] -->
6.2 Impact of Various Situations

<!-- b000719 | prose | pages [20] -->
6.2.1 Collectivist Cultural Norms

<!-- b000720 | prose | pages [20] -->
We change the control parameter from 0.1 to 1.0 and measure the performance met- rics of our model. The result of this experiment is shown in Figure 17.

<!-- b000721 | prose | pages [20] -->
1200

<!-- b000722 | prose | pages [20] -->
1000

<!-- b000723 | prose | pages [20] -->
Variance(min 2)

<!-- b000724 | prose | pages [20] -->
800

<!-- b000725 | prose | pages [20] -->
600

<!-- b000726 | prose | pages [20] -->
400

<!-- b000727 | prose | pages [20] -->
200

<!-- b000728 | prose | pages [20] -->
0 0.0 0.2 0.4 0.6

<!-- b000729 | prose | pages [20] -->
Penalty factor

<!-- b000730 | prose | pages [20] -->
7.50

<!-- b000731 | prose | pages [20] -->
Throughput (PAX/min)

<!-- b000732 | prose | pages [20] -->
7.00

<!-- b000733 | prose | pages [20] -->
6.50

<!-- b000734 | prose | pages [20] -->
6.00

<!-- b000735 | prose | pages [20] -->
Variance

<!-- b000736 | prose | pages [20] -->
Throughput

<!-- b000737 | prose | pages [20] -->
5.50

<!-- b000738 | prose | pages [20] -->
5.00

<!-- b000739 | prose | pages [20] -->
4.50

<!-- b000740 | prose | pages [20] -->
0.8 1.0

<!-- b000741 | caption | pages [20] -->
Figure 17: System variance and throughput with respect to control parameter V

<!-- b000742 | prose | pages [20] -->
We can see that the throughput of the system shrinks and that the variance increases

<!-- b000743 | furniture | pages [21] -->
Team # 55295

<!-- b000744 | furniture | pages [21] -->
Page 17 of 20

<!-- b000745 | prose | pages [21] -->
as the control parameter grows, which means both the performance and the stability of the system deteriorates if passengers favor individual efﬁciency too much.

<!-- b000746 | prose | pages [21] -->
6.2.2 Individualist Cultural Norms

<!-- b000747 | prose | pages [21] -->
We run our model with skipping queueing rule for 10 times and calculate the aver- aged performance metrics. Table 5 shows the variance and the throughput of the cutting- in-line system and the normal system.

<!-- b000748 | prose | pages [21] -->
Variance(min2) Non-cutting 96.024 Cutting 43.622 Throughput(PAX/min) 7.575 7.690

<!-- b000749 | caption | pages [21] -->
Table 5: Averaged variance and throughput of systems

<!-- b000750 | prose | pages [21] -->
We can see that the system which allows cutting in line has better variance and s- lightly better throughput than the system that does not. This is because cutting in line increases the waiting time of passengers after the person who skips, but does not nec- essarily increase the waiting time of the person who leaves last, and therefore does not necessarily deteriorate throughput.

<!-- b000751 | prose | pages [21] -->
6.2.3 Family-based Travelers

<!-- b000752 | prose | pages [21] -->
We add family-based travelers to our model and simulate the model for different percentages of family-based travelers in all passengers. Figure 18 shows the variance and throughput of the system with respect to different ratios.

<!-- b000753 | prose | pages [21] -->
1200

<!-- b000754 | prose | pages [21] -->
1000

<!-- b000755 | prose | pages [21] -->
Variance(min 2)

<!-- b000756 | prose | pages [21] -->
800

<!-- b000757 | prose | pages [21] -->
600

<!-- b000758 | prose | pages [21] -->
400

<!-- b000759 | prose | pages [21] -->
200

<!-- b000760 | prose | pages [21] -->
0 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7

<!-- b000761 | prose | pages [21] -->
Percentage of family PAX

<!-- b000762 | prose | pages [21] -->
5

<!-- b000763 | prose | pages [21] -->
Throughput (PAX/min)

<!-- b000764 | prose | pages [21] -->
4

<!-- b000765 | prose | pages [21] -->
3

<!-- b000766 | prose | pages [21] -->
Control group

<!-- b000767 | prose | pages [21] -->
2

<!-- b000768 | prose | pages [21] -->
With family checkpoint

<!-- b000769 | prose | pages [21] -->
1

<!-- b000770 | prose | pages [21] -->
W/o family checkpoint

<!-- b000771 | prose | pages [21] -->
0 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7

<!-- b000772 | prose | pages [21] -->
Percentage of family PAX

<!-- b000773 | caption | pages [21] -->
Figure 18: System variance and throughput with respect to family-based travelers’ ratio

<!-- b000774 | prose | pages [21] -->
We see from Figure 18 that the family-based travelers hurt the performance metrics of the airport. The more family-based travelers, the more the metrics will deteriorate. To accommodate large number of family-based travelers, a check point that specially designed for them can be deployed. This kind of check points can help improve vari- ance and throughput when the number of family-based travelers is large. We will give detailed explanation for this kind of special check points at section 6.3.

<!-- b000775 | furniture | pages [22] -->
Team # 55295

<!-- b000776 | prose | pages [22] -->
6.2.4 Tech-based Travelers

<!-- b000777 | furniture | pages [22] -->
Page 18 of 20

<!-- b000778 | prose | pages [22] -->
We simulate our model on different arrival distributions described earlier in sec- tion 6.1.4. Figure 19 illustrates how variance and throughput of our model change with respect to the standard variance of the arrival distribution.

<!-- b000779 | prose | pages [22] -->
550

<!-- b000780 | prose | pages [22] -->
500

<!-- b000781 | prose | pages [22] -->
Variance(min 2)

<!-- b000782 | prose | pages [22] -->
450

<!-- b000783 | prose | pages [22] -->
400

<!-- b000784 | prose | pages [22] -->
350

<!-- b000785 | prose | pages [22] -->
10 12 14

<!-- b000786 | prose | pages [22] -->
6.40

<!-- b000787 | prose | pages [22] -->
6.20

<!-- b000788 | prose | pages [22] -->
Throughput (PAX/min)

<!-- b000789 | prose | pages [22] -->
6.00

<!-- b000790 | prose | pages [22] -->
5.80

<!-- b000791 | prose | pages [22] -->
Variance

<!-- b000792 | prose | pages [22] -->
5.60

<!-- b000793 | prose | pages [22] -->
Throughput

<!-- b000794 | prose | pages [22] -->
5.40

<!-- b000795 | prose | pages [22] -->
5.20

<!-- b000796 | prose | pages [22] -->
5.00

<!-- b000797 | prose | pages [22] -->
16 16 18

<!-- b000798 | prose | pages [22] -->
σ of arrival normal distribution

<!-- b000799 | caption | pages [22] -->
Figure 19: System variance and throughput with respect to the variance of arrival distri-

<!-- b000800 | prose | pages [22] -->
bution

<!-- b000801 | prose | pages [22] -->
Basically, Figure 19 tells us that if passengers arrive more intensely in a given time period, then the security check process will have better performance. So if the airport provides more accurate information such that the passengers can correctly estimate their arriving time, the airport will have better throughput and lower variance.

<!-- b000802 | prose | pages [22] -->
6.3 Accommodation for Situations

<!-- b000803 | prose | pages [22] -->
In this section, we will provide some accommodations that correspond to the previ- ous situations we have discussed.

<!-- b000804 | prose | pages [22] -->
1. Collectivist cultural norms: people from collectivist cultures favor collective ef- ﬁciency more. The airport can deploy a scheduling algorithm like that in sec- tion 5.3.1 to optimize global throughput and variance.

<!-- b000805 | prose | pages [22] -->
2. Individualist cultural norms: for the sake of passenger’s satisfaction, the airport should strictly forbid cutting in line despite its potential help in lower the variance of waiting time.

<!-- b000806 | prose | pages [22] -->
3. Family-based travelers: deploying a special check point for family members can help. The special check point only serves family-based travelers and mainly focus on the parents when doing identiﬁcation check, which implies shorter service time for the whole family. Figure 18 shows that this special check point helps improve throughput and variance.

<!-- b000807 | prose | pages [22] -->
4. Tech-based travelers: the airport should encourage the passengers to use the mo- bile app that provides information about queueing in the airport.

<!-- b000808 | prose | pages [22] -->
The airport should also try to collect as accurate data as possible to help passengers better estimate their arriving time.

<!-- b000809 | furniture | pages [23] -->
Page 19 of 20

<!-- b000810 | furniture | pages [23] -->
Team # 55295

<!-- b000811 | prose | pages [23] -->
7

<!-- b000812 | heading | pages [23] -->
Conclusion

<!-- b000813 | prose | pages [23] -->
7.1

<!-- b000814 | heading | pages [23] -->
Conclusion of the Problem

<!-- b000815 | prose | pages [23] -->
We model the problem as a queueing network and identify lack of sufﬁcient ID check points, exclusive assignment of screening check points, presence of suspicious passen- gers as three bottlenecks of the system. We reﬁne the model by applying greedy routing algorithm, backpressure algorithm, drift-plus-penalty algorithm to optimize passenger scheduling process. We implement and simulate our model and ﬁnd that the backpres- sure algorithm is close to optimal scheduling and is practical in real airports. We also explore the optimal ratio of different kinds of check points and test the robustness of modiﬁed models. We perform sensitivity analysis of our model by considering the im- pacts of different cultural norms and different types of travelers. We also propose several policies that may help airports deal with the inﬂow of passengers in various situations.

<!-- b000816 | prose | pages [23] -->
7.2 Policy Proposal

<!-- b000817 | prose | pages [23] -->
We propose the following policies:

<!-- b000818 | prose | pages [23] -->
1. Globally applicable:

<!-- b000819 | prose | pages [23] -->
(a) Deploy backpressure algorithm discussed in section 5.3.1 to optimize passen-

<!-- b000820 | prose | pages [23] -->
ger scheduling.

<!-- b000821 | prose | pages [23] -->
(b) Push accurate airport queueing information to passengers through mobile

<!-- b000822 | prose | pages [23] -->
apps.

<!-- b000823 | prose | pages [23] -->
(c) Strictly forbid cutting in line for the sake of passengers’ satisfaction.

<!-- b000824 | prose | pages [23] -->
(d) The ratio of pre-check check points and regular check points should be care-

<!-- b000825 | prose | pages [23] -->
fully chosen(based on arriving rate of passengers, the percentage of pre-check passengers, etc).

<!-- b000826 | prose | pages [23] -->
2. Locally applicable:

<!-- b000827 | prose | pages [23] -->
(a) Airports in countries inﬂuenced by collectivist cultures can deploy drift-plus-

<!-- b000828 | prose | pages [23] -->
penalty algorithm with small control factor to improve throughput and vari- ance of passengers.

<!-- b000829 | prose | pages [23] -->
(b) When operate in traveling season, airports can deploy a temporary check

<!-- b000830 | prose | pages [23] -->
point for family-based travelers to enhance throughput and decrease vari- ance.

<!-- b000831 | prose | pages [23] -->
7.3

<!-- b000832 | heading | pages [23] -->
Strength and Weakness of Our Model

<!-- b000833 | prose | pages [23] -->
Strength:

<!-- b000834 | prose | pages [23] -->
1. Requiring little change to current security check process

<!-- b000835 | prose | pages [23] -->
2. Achieving throughput of passengers close to optimal

<!-- b000836 | prose | pages [23] -->
3. Retaining passenger satisfaction while scheduling passengers

<!-- b000837 | furniture | pages [24] -->
Page 20 of 20

<!-- b000838 | furniture | pages [24] -->
Team # 55295

<!-- b000839 | prose | pages [24] -->
4. Consistent good performance regardless of the distribution of arriving times

<!-- b000840 | prose | pages [24] -->
Weakness:

<!-- b000841 | prose | pages [24] -->
1. Requiring external intervention to achieve good performance

<!-- b000842 | prose | pages [24] -->
2. Not taking the distances among check points into consideration

<!-- b000843 | prose | pages [24] -->
3. Limited performance metrics

<!-- b000844 | prose | pages [24] -->
4. Using imprecise estimated parameter from a small data set

<!-- b000845 | prose | pages [24] -->
7.4

<!-- b000846 | heading | pages [24] -->
Future Application of Models

<!-- b000847 | prose | pages [24] -->
Our proposed model can also be generalized into ﬁelds like:

<!-- b000848 | prose | pages [24] -->
1. communication systems: our scheduling algorithm can be used to schedule the transportation of data packets in order to improve throughput and reduce vari- ance.

<!-- b000849 | prose | pages [24] -->
2. logistics networks: our models correctly reﬂect the queueing process and trans- portation process of logistics networks. The optimization approaches mentioned in our model can also be applied in this ﬁeld.

<!-- b000850 | prose | pages [24] -->
3. queueing hardware: in hardware systems, several queueing devices may need to compete to use the bus to send their data to destinations. The scheduling algorithm in our model can be used to optimize the throughput and variance of such systems.

<!-- b000851 | heading | pages [25] -->
References

<!-- b000852 | references | pages [25] -->
[1] J. P. C. Kleijnen, S. M. Sanchez, T. W. Lucas, and T. M. Cioppa, “State-of-the-art re-

<!-- b000853 | references | pages [25] -->
view: A user’s guide to the brave new world of designing simulation experiments,”

<!-- b000854 | references | pages [25] -->
Informs Journal on Computing, vol. 17, no. 3, pp. 263–289, 2005.

<!-- b000855 | references | pages [25] -->
[2] M. J. Neely, “Stochastic network optimization with application to communication

<!-- b000856 | references | pages [25] -->
and queueing systems,” Synthesis Lectures on Communication Networks, vol. 3, no. 1,

<!-- b000857 | references | pages [25] -->
p. 211, 2010.

<!-- b000858 | references | pages [25] -->
[3] F. Baskett, K. M. Chandy, R. R. Muntz, and F. G. Palacios, “Open, closed, and mixed

<!-- b000859 | references | pages [25] -->
networks of queues with different classes of customers,” Journal of the ACM, vol. 22,

<!-- b000860 | references | pages [25] -->
no. 2, pp. 248–260, 1975.

<!-- b000861 | references | pages [25] -->
[4] “Chicago o ˛a´rhare international(ord).” http://www.airport-ohare.com/.

<!-- b000862 | references | pages [25] -->
[5] “Hartsﬁeld-jackson atlanta international(atl).” http://www.atl.com/.

<!-- b000863 | references | pages [25] -->
[6] “Los angeles international(lax).” http://www.lawa.org/welcomeLAX.aspx.

<!-- b000864 | references | pages [25] -->
[7] “John f. kennedy international(jfk).” http://www.airport-jfk.com/.

<!-- b000865 | references | pages [25] -->
[8] “San francisco international(sfo).” https://www.flysfo.com/.

<!-- b000866 | references | pages [25] -->
https://apps.tsa.dhs.gov/mytsa/wait_times_detail.

<!-- b000867 | references | pages [25] -->
[9] “My

<!-- b000868 | references | pages [25] -->
TSA.”

<!-- b000869 | references | pages [25] -->
aspx.

<!-- b000870 | references | pages [25] -->
[10] L. Tassiulas and A. Ephremides, “Stability properties of constrained queueing sys-

<!-- b000871 | references | pages [25] -->
tems and scheduling policies for maximum throughput in multihop radio network-

<!-- b000872 | references | pages [25] -->
s,” conference on decision and control, vol. 37, no. 12, pp. 1936–1948, 1992.

<!-- b000873 | references | pages [25] -->
[11] “Country comparison.” https://geert-hofstede.com/countries.html.
