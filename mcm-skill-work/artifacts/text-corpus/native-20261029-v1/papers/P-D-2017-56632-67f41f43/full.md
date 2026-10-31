# P-D-2017-56632-67f41f43

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
56632

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | prose | pages [1] -->
F1 ________________

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
T2 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | title | pages [1] -->
D

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | furniture | pages [1] -->


<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000020 | heading | pages [1] -->
Summary Sheet

<!-- b000021 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | prose | pages [1] -->
Passengers arrive at TSA security screening at seemingly random times, and the uncertainty in their arrival along with TSA inefficiencies can cause abnormally long and varying wait times. A major problem the agency must confront is the improvement of passenger throughput while maintaining a strict standard of security. Our solution consists of four main parts: a queuing model describing the security screening, a method of simulation for theory verification and experimentation, the application of these results to cost-benefit analysis, and modifications to the model to account for different traveler characteristics.

<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | prose | pages [1] -->
We decided that a reasonable measure for TSA inefficiency was the average time a passenger spent waiting in line. The queuing model was formulated by expressing the relationship between wait times in the queue recursively. We used kernel density estimation and exponential fitting to estimate distributions on the random variables involved in the model. We obtained explicit expressions for passenger wait times, which we used to reason about the system behavior as the number of passengers and arrival rates varied.

<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | prose | pages [1] -->
Using the above framework we developed a method for simulation that used dynamic programming to sample arrival times of passengers within the security system. The simulation numerically verified the results of the theory and allowed for further experimentation with varying parameters. The results of these experiments gave us insights on where the TSA procedure could be optimized and the passenger experience improved.

<!-- b000029 | furniture | pages [1] -->


<!-- b000030 | prose | pages [1] -->
We applied cost-benefit analysis to the efficiency-cost tradeoff that TSA must consider when staffing employees and screening passengers. We found an optimal allocation of resources that maximized profit rate by plotting a profit objective function against the different configurations of TSA employees.

<!-- b000031 | furniture | pages [1] -->


<!-- b000032 | prose | pages [1] -->
Finally, we considered distinctions between travelers and how they might affect the activity in the queuing system and each other’s wait times as a result. We investigated alternative methods to order passengers in queue and found that this approach was not as successful as we expected.

<!-- b000033 | furniture | pages [1] -->


<!-- b000034 | prose | pages [1] -->
Using a diverse array of techniques, we were able to successfully model the flow of passengers through airport security, identify bottlenecks in the screening process, and suggest improvements to the current procedure. As our world becomes more interconnected and airline activity increases, TSA will have to confront the issue of passenger throughput inefficiency. The use of mathematical models will undoubtedly become an invaluable tool in optimizing efficiency while maintaining passenger safety.

<!-- b000035 | prose | pages [2] -->
Reducing Wait Times at Airport Security

<!-- b000036 | prose | pages [2] -->
Team 56632

<!-- b000037 | prose | pages [2] -->
January 24, 2017

<!-- b000038 | heading | pages [2] -->
Abstract

<!-- b000039 | prose | pages [2] -->
In this report, we develop and employ a queuing model for lines and servicing at TSA security in order to identify bottlenecks in the procedure and suggest improvements. We model the inﬂux of passengers as a Poisson process, allowing us to sample from an exponential distribution to simulate inter-arrival times. To ﬁnd probabilistic distributions on the service time spent in security stations, we take a nonparametric approach, using kernel density estimation to obtain probability densities from the given data. Us- ing recurrence concepts from our queuing network, we develop a simulation method via dynamic programming as a means to verify the theoretical results and conduct further experiments. We apply these results to a cost-beneﬁt analysis, which we use to identify the optimal allocation of TSA resources. Additionally, we consider di↵erent cultural norms regarding passenger in- teraction in queues, and add complexity in our model to account for them. These tools allow us to perform experiments, which are realistic within rea- son, and give suggestions for improvement in a manner justiﬁed by both the given and researched data.

<!-- b000040 | prose | pages [2] -->
1

<!-- b000041 | heading | pages [3] -->
Contents

<!-- b000042 | contents | pages [3] -->
1

<!-- b000043 | heading | pages [3] -->
Introduction

<!-- b000044 | prose | pages [3] -->
3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Outline 3 Main Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000045 | prose | pages [3] -->
2

<!-- b000046 | heading | pages [3] -->
A Queuing Model

<!-- b000047 | prose | pages [3] -->
3

<!-- b000048 | prose | pages [3] -->
4 Obtaining Probability Densities . . . . . . . . . . . . . . . . . . . . 2.1 5 . . . . . . . . . . . . . . . . . . . . . . 2.1.1 Exponential Fitting 5 Kernel Density Estimation 2.1.2 . . . . . . . . . . . . . . . . . .

<!-- b000049 | prose | pages [3] -->
6 Writing Down a Recurrence . . . . . . . . . . . . . . . . . . . . . . 2.2 8 Deﬁnitions and Derivations . . . . . . . . . . . . . . . . . . 2.2.1 8 Average Wait Time Values 2.2.2

<!-- b000050 | prose | pages [3] -->
3 The Simulation

<!-- b000051 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . .

<!-- b000052 | prose | pages [3] -->
10

<!-- b000053 | prose | pages [3] -->
11 A Dynamic Programming Method 3.1 . . . . . . . . . . . . . . . . . .

<!-- b000054 | prose | pages [3] -->
11 Pseudo code . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1 12 Comparison to the Model . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000055 | prose | pages [3] -->
4

<!-- b000056 | heading | pages [3] -->
Evaluation/Results

<!-- b000057 | prose | pages [3] -->
12

<!-- b000058 | prose | pages [3] -->
13 Bottlenecks in Passenger Throughput 4.1 . . . . . . . . . . . . . . . .

<!-- b000059 | prose | pages [3] -->
13 ID Check Station . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 13 . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.2 Scan Station 15 Variance in Passenger Wait Time . . . . . . . . . . . . . . . . . . . 4.2 15 . . . . . . . . . . . . . . . . . . . . . . 4.3 Modiﬁcations to the Model 4.3.1 Cost-Beneﬁt Analysis 16 . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | prose | pages [3] -->
16 . . . . . . . . . . . . . . . . . . . . . . 4.3.2 Sensitivity Analysis

<!-- b000061 | prose | pages [3] -->
5

<!-- b000062 | heading | pages [3] -->
Improving the Model

<!-- b000063 | prose | pages [3] -->
18

<!-- b000064 | prose | pages [3] -->
19 . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Traveler Characteristics 19 Di↵erent Queuing Disciplines . . . . . . . . . . . . . . . . . . . . . 5.2 19 Arrival Rate Regulation . . . . . . . . . . . . . . . . . . . . . . . . 5.3 19 Improving Proﬁt Measure . . . . . . . . . . . . . . . . . . . . . . . 5.4

<!-- b000065 | prose | pages [3] -->
6

<!-- b000066 | heading | pages [3] -->
Conclusion

<!-- b000067 | prose | pages [3] -->
7

<!-- b000068 | heading | pages [3] -->
Bibliography

<!-- b000069 | references | pages [3] -->
19

<!-- b000070 | references | pages [3] -->
19

<!-- b000071 | references | pages [3] -->
21

<!-- b000072 | references | pages [3] -->
2

<!-- b000073 | references | pages [3] -->
2

<!-- b000074 | references | pages [4] -->
Team 56632

<!-- b000075 | furniture | pages [4] -->
Page 3 of 21

<!-- b000076 | references | pages [4] -->
1

<!-- b000077 | heading | pages [4] -->
Introduction

<!-- b000078 | prose | pages [4] -->
In this report, we present a model and simulation to optimize TSA security lines with respect to passenger throughput and variance in wait times. Speciﬁcally, we study the relationship between the number of ID check and scan stations and arrival rate to identify bottlenecks in the security process. We also deﬁne a cost measure to determine the optimal number of service stations. Further, we explore the implementation of a “virtual queue” and varying passenger traveling speeds and how they impact these bottlenecks.

<!-- b000079 | prose | pages [4] -->
Our model provides the TSA valuable information for reducing wait time and variance in security lines, while maintaining the same standards of safety and security.

<!-- b000080 | prose | pages [4] -->
1.1 Outline

<!-- b000081 | prose | pages [4] -->
Our objective is to develop and implement a model to explore the ﬂow of pas- sengers through airport security, identify bottlenecks in the current process, and suggest modiﬁcations. To realize this objective we will proceed as follows:

<!-- b000082 | prose | pages [4] -->
• Formulate a queuing model to explore passenger wait times as a measure of ineﬃciency.

<!-- b000083 | prose | pages [4] -->
• Implement a simulation method to verify the theoretical framework and perform experiments to gain further insights.

<!-- b000084 | heading | pages [4] -->
• Analyze simulation results to identify the optimal allocation of resources

<!-- b000085 | prose | pages [4] -->
according to a cost-beneﬁt analysis.

<!-- b000086 | heading | pages [4] -->
• Make modiﬁcations to the model based on cost-beneﬁt analysis and

<!-- b000087 | prose | pages [4] -->
cultural di↵erences. Incorporate more complexity in the model to account for these considerations.

<!-- b000088 | prose | pages [4] -->
1.2

<!-- b000089 | heading | pages [4] -->
Main Assumptions

<!-- b000090 | prose | pages [4] -->
Queuing systems are probabilistic in nature and as a result are diﬃcult to de- scribe and predict. In order to quantify the uncertainty in waiting times, it is necessary to make some simplifying assumptions. Listed below are several of the main assumptions we make regarding how we view the problem.

<!-- b000091 | prose | pages [4] -->
Throughout the remainder of this paper we introduce additional assumptions as they become relevant.

<!-- b000092 | prose | pages [4] -->
• Transit times between stations and queues are negligible. We as- sume that the time spent moving from a queue to a station or a station to

<!-- b000093 | prose | pages [4] -->
3

<!-- b000094 | prose | pages [5] -->
Team 56632

<!-- b000095 | furniture | pages [5] -->
Page 4 of 21

<!-- b000096 | prose | pages [5] -->
a queue is negligible. This is a reasonable assumption in that most TSA checkpoints are relatively compact.

<!-- b000097 | prose | pages [5] -->
• Queues operate on the “First In First Out” (FIFO) discipline. This principle states that the ﬁrst person to line up in a queue will be the ﬁrst person to be served.

<!-- b000098 | prose | pages [5] -->
• All employees are identical in terms of competency at their job. We assume that all TSA employees are equally capable. This isn’t entirely realistic because some workers are better at their jobs than others; however, this distinction doesn’t serve to provide any further meaningful insights into the problem.

<!-- b000099 | prose | pages [5] -->
• Passenger wait times are an accurate measure of throughput eﬃ-

<!-- b000100 | heading | pages [5] -->
ciency. Large passenger wait times in queues are the result of ineﬃciencies

<!-- b000101 | prose | pages [5] -->
in the TSA screening process. Passenger throughput (given as passengers per unit time) is inversely proportional to time spent in the system by each passenger. Thus, maximizing passenger throughput is essentially the same as minimizing wait time.

<!-- b000102 | prose | pages [5] -->
2

<!-- b000103 | heading | pages [5] -->
A Queuing Model

<!-- b000104 | prose | pages [5] -->
We model the airport security line as 2 nearly-identical parallel queuing networks with the FIFO discipline depicted below. The network with green entities corre- sponds to the TSA precheck lane and the network with blue entities corresponds to passengers in the regular lane. Both networks are comprised of a queue, Q1, leading to a server S1 (ID check station), leading to another queue Q2, leading to another server S2 (scan station, which includes mm wave scan, carry on screening, and extra screening if necessary). A pre-determined fraction of people will queue in the precheck lane while the rest will queue in the regular lane.

<!-- b000105 | caption | pages [5] -->
Figure 1: A schematic of the queuing model. The superscripts “pre” and “reg”

<!-- b000106 | prose | pages [5] -->
stand for “precheck” and “regular”, respectively.

<!-- b000107 | prose | pages [5] -->
4

<!-- b000108 | prose | pages [6] -->
Team 56632

<!-- b000109 | furniture | pages [6] -->
Page 5 of 21

<!-- b000110 | heading | pages [6] -->
Assumption 1: Time spent in additional screening (Zone D) was included in

<!-- b000111 | prose | pages [6] -->
the “Time to get scanned property” column in the given data ﬁle.

<!-- b000112 | prose | pages [6] -->
Remark.

<!-- b000113 | prose | pages [6] -->
Data was given as total time until picking up scanned property (column H), which would be done after the additional Zone D screening. This implies that column H incorporates any time spent in Zone D.

<!-- b000114 | prose | pages [6] -->
Assumption 2: For the ﬁrst version of our model, we assume that the system includes only the top row in Figure 1, and that there is only one service spot at each of S1 (ID check) and S2 (scan station). Later on we will remove this assumption.

<!-- b000115 | prose | pages [6] -->
Remark.

<!-- b000116 | prose | pages [6] -->
In order to explicitly solve the recurrence relations we develop later on, it suﬃces to assume that service stations S1 and S2 each can only service one entity at a time. When we eventually take a dynamic programming approach, we will vary the number of ID check and scan stations and select a conﬁguration which optimizes the cost-beneﬁt tradeo↵(See “Cost-Beneﬁt Analysis” section).

<!-- b000117 | prose | pages [6] -->
2.1 Obtaining Probability Densities

<!-- b000118 | prose | pages [6] -->
2.1.1 Exponential Fitting

<!-- b000119 | prose | pages [6] -->
Depicted below are histograms of the passenger inter-arrival times extracted from the given data ﬁle. They strongly resemble the shape of an exponential probability density, motivating the next key assumption.

<!-- b000120 | caption | pages [6] -->
Figure 2: The exponential ﬁt (using Matlab’s expfit function) to the inter-

<!-- b000121 | prose | pages [6] -->
arrival times of precheck (left) and regular (right) passengers overlaid onto the corresponding histograms.

<!-- b000122 | prose | pages [6] -->
5

<!-- b000123 | prose | pages [7] -->
Team 56632

<!-- b000124 | furniture | pages [7] -->
Page 6 of 21

<!-- b000125 | heading | pages [7] -->
Assumption 3: The inter-arrival times are distributed i.i.d. exponential with

<!-- b000126 | prose | pages [7] -->
rate λreg = 12.9 and λpre = 9.2 (seconds per passenger).

<!-- b000127 | prose | pages [7] -->
Remark.

<!-- b000128 | prose | pages [7] -->
We chose to model the incoming passengers as a Poisson Pro- cess, since the histogram of the inter-arrival times resembles an exponential distribution, a deﬁning characteristic of the inter-arrival times of a Poisson Process. The estimate for the rate parameter λ we used was the sample mean of the inter-arrival times, as given by maximum likelihood estimation[5].

<!-- b000129 | prose | pages [7] -->
2.1.2 Kernel Density Estimation

<!-- b000130 | prose | pages [7] -->
We deﬁne the following random variables.

<!-- b000131 | prose | pages [7] -->
.= The total time entity j spends at TSA check in.

<!-- b000132 | prose | pages [7] -->
T (j)

<!-- b000133 | prose | pages [7] -->
total

<!-- b000134 | prose | pages [7] -->
.= The wait time of entity j in queue i.

<!-- b000135 | prose | pages [7] -->
T (j)

<!-- b000136 | prose | pages [7] -->
Qi

<!-- b000137 | prose | pages [7] -->
.= The time spent of entity j in service i.

<!-- b000138 | prose | pages [7] -->
S(j)

<!-- b000139 | prose | pages [7] -->
i

<!-- b000140 | prose | pages [7] -->
Aj .= The arrival time of entity j.

<!-- b000141 | prose | pages [7] -->
Ij .= The inter-arrival time between passenger j −1 and j.

<!-- b000142 | prose | pages [7] -->
The Aj’s can be written as sums of the ﬁrst j inter-arrival times, which we assumed to be distributed i.i.d. exponential. To ﬁnd the distributions on the S(j)

<!-- b000143 | prose | pages [7] -->
i , we perform kernel density estimation on the given data using Matlab’s ksdensity function for estimation of a density over a positive support.

<!-- b000144 | caption | pages [7] -->
Figure 3: The kernel density estimate of both regular and precheck passenger time

<!-- b000145 | prose | pages [7] -->
spent in service station 1 (ID check) overlaid onto the corresponding histogram.

<!-- b000146 | prose | pages [7] -->
6

<!-- b000147 | prose | pages [8] -->
Team 56632

<!-- b000148 | furniture | pages [8] -->
Page 7 of 21

<!-- b000149 | caption | pages [8] -->
Figure 4: The kernel density estimate of precheck (left) vs. regular (right) pas-

<!-- b000150 | prose | pages [8] -->
senger time spent in service station 2 (scanning).

<!-- b000151 | prose | pages [8] -->
Assumption 4: Time spent in the scan station is smaller for precheck passengers since they do not need to remove as many personal items.

<!-- b000152 | prose | pages [8] -->
Remark.

<!-- b000153 | prose | pages [8] -->
This is a reasonable assumption, as precheck passengers pay an extra fee in order to exercise this privilege.

<!-- b000154 | prose | pages [8] -->
To ﬁnd the distribution on the time spent in service station 2 (scanning) for precheck passengers, we noted that since they don’t have to remove personal items, the time they spend in the scanning station, Spre

<!-- b000155 | prose | pages [8] -->
is the maximum of the 2 time spent in the mm wave scan and the time spent on luggage scanning. For instance, if the luggage ﬁnishes scanning ﬁrst, then as soon as the passenger exits the mm wave scan, they can immediately pick up their luggage and go.

<!-- b000156 | prose | pages [8] -->
X .= Time spent in the mm wave scan.

<!-- b000157 | prose | pages [8] -->
W .= Time spent scanning a piece of luggage.

<!-- b000158 | prose | pages [8] -->
Y .= 2.26 · W

<!-- b000159 | prose | pages [8] -->
.= max(X, Y )

<!-- b000160 | prose | pages [8] -->
Spre

<!-- b000161 | prose | pages [8] -->
2

<!-- b000162 | prose | pages [8] -->
Since the provided data ﬁle reports the times that each piece of luggage exits the scan machine, we must multiply the random variable representing this time by the number of bags that the average passenger carries on. According to the TSA, a passenger brings 2.26 bags on average [10].

<!-- b000163 | prose | pages [8] -->
Assumption 5: X and Y are independent.

<!-- b000164 | prose | pages [8] -->
Remark.

<!-- b000165 | prose | pages [8] -->
This is a reasonable assumption, as scan times for luggage ma- chines and mm wave scan machines don’t inﬂuence each other.

<!-- b000166 | prose | pages [8] -->
7

<!-- b000167 | prose | pages [9] -->
Team 56632

<!-- b000168 | furniture | pages [9] -->
Page 8 of 21

<!-- b000169 | prose | pages [9] -->
We estimate the distributions on X and Y using kernel density estimation (de- picted in the left plot of Figure 4 by the dotted densities). To obtain the distri- bution on Spre

<!-- b000170 | prose | pages [9] -->
2 , we write

<!-- b000171 | prose | pages [9] -->
FS(s) .= P(Spre

<!-- b000172 | prose | pages [9] -->
s) 2 2

<!-- b000173 | prose | pages [9] -->
= P(max(X, Y ) s)

<!-- b000174 | prose | pages [9] -->
= P(X s, Y s)

<!-- b000175 | prose | pages [9] -->
= FX(s)FY (s)

<!-- b000176 | prose | pages [9] -->
where the last equality follows from independence. Taking the derivative to obtain the density on Spre

<!-- b000177 | prose | pages [9] -->
2 , we have

<!-- b000178 | prose | pages [9] -->
fS(s) .= d

<!-- b000179 | prose | pages [9] -->
dsFS(s) = fX(s)FY (s) + fY (s)FX(s)

<!-- b000180 | prose | pages [9] -->
This density was computed and plotted as the green curve against the kernel density estimates of fX and fW on the left plot in Figure 4.

<!-- b000181 | prose | pages [9] -->
2.2 Writing Down a Recurrence

<!-- b000182 | prose | pages [9] -->
2.2.1 Deﬁnitions and Derivations

<!-- b000183 | prose | pages [9] -->
We deﬁne the total time spent by passenger n in the system as the sum of time spent in the queues and the service stations.

<!-- b000184 | prose | pages [9] -->
Q1 + T (n)

<!-- b000185 | prose | pages [9] -->
T (n)

<!-- b000186 | prose | pages [9] -->
total = T (n)

<!-- b000187 | prose | pages [9] -->
Q2 + S(n)

<!-- b000188 | prose | pages [9] -->
+ S(n)

<!-- b000189 | prose | pages [9] -->
(1)

<!-- b000190 | prose | pages [9] -->
1

<!-- b000191 | prose | pages [9] -->
2

<!-- b000192 | prose | pages [9] -->
We deﬁne the wait times in the ﬁrst queue {T (i)

<!-- b000193 | prose | pages [9] -->
Q1}i≥1 recursively. The time that passenger i spends in queue 1 is the time at which they arrive subtracted from the time at which passenger i −1 leaves the ﬁrst service station. The latter quantity can be written as the sum of the following quantities of the previous passenger: arrival time, time spent in line, and time spent getting serviced. This recurrence relation is illustrated below.

<!-- b000194 | prose | pages [9] -->
T (1)

<!-- b000195 | prose | pages [9] -->
Q1 = 0

<!-- b000196 | prose | pages [9] -->
Q1 + S(1)

<!-- b000197 | prose | pages [9] -->
T (2)

<!-- b000198 | prose | pages [9] -->
Q1 = A1 + T (1)

<!-- b000199 | prose | pages [9] -->
...

<!-- b000200 | prose | pages [9] -->
−A2 1

<!-- b000201 | prose | pages [9] -->
Q1 = An−1 + T (n−1)

<!-- b000202 | prose | pages [9] -->
T (n)

<!-- b000203 | prose | pages [9] -->
Q1 + S(n−1)

<!-- b000204 | prose | pages [9] -->
−An 1

<!-- b000205 | prose | pages [9] -->
8 8

<!-- b000206 | prose | pages [10] -->
Team 56632

<!-- b000207 | furniture | pages [10] -->
Page 9 of 21

<!-- b000208 | heading | pages [10] -->
Assumption 6: When passengers arrive at either queue, there is always someone

<!-- b000209 | prose | pages [10] -->
in line to wait behind (except in the case of the ﬁrst passenger to arrive).

<!-- b000210 | prose | pages [10] -->
In our deﬁnition for the T (i) Remark.

<!-- b000211 | prose | pages [10] -->
Q1’s, we should be taking the max of the expression displayed above and 0, Ai > Ai−1 + T (i−1)

<!-- b000212 | prose | pages [10] -->
+ S(i−1)

<!-- b000213 | prose | pages [10] -->
since we could possibly have

<!-- b000214 | prose | pages [10] -->
passenger i arrives after passenger i −1 , i.e. 1

<!-- b000215 | prose | pages [10] -->
Q1

<!-- b000216 | prose | pages [10] -->
leaves the service station. This would lead to a negative waiting time. However, omitting the max operation allows for an explicit solution to the recurrence T (n)

<!-- b000217 | prose | pages [10] -->
Q1 and simpliﬁes calculations immensely. Later on we will remove this assumption.

<!-- b000218 | prose | pages [10] -->
Solving the recurrence, we obtain an explicit form for the time passenger n waits in queue 1,

<!-- b000219 | prose | pages [10] -->
⇣n−1 X

<!-- b000220 | prose | pages [10] -->
⌘

<!-- b000221 | prose | pages [10] -->
S(i)

<!-- b000222 | prose | pages [10] -->
T (n)

<!-- b000223 | prose | pages [10] -->
Q1 =

<!-- b000224 | prose | pages [10] -->
i=1

<!-- b000225 | prose | pages [10] -->
−An + A1

<!-- b000226 | prose | pages [10] -->
1 1

<!-- b000227 | prose | pages [10] -->
Note that An can be written as a sum of interarrival times {Ij}n

<!-- b000228 | prose | pages [10] -->
j=1 distributed

<!-- b000229 | prose | pages [10] -->
i.i.d. exponential(λ), so that the expectation of T (n)

<!-- b000230 | prose | pages [10] -->
⇣

<!-- b000231 | prose | pages [10] -->
E(T (n)

<!-- b000232 | prose | pages [10] -->
Q1 ) = E

<!-- b000233 | prose | pages [10] -->
Q1 is given by

<!-- b000234 | prose | pages [10] -->
⌘

<!-- b000235 | prose | pages [10] -->
n−1 X

<!-- b000236 | prose | pages [10] -->
S(i)

<!-- b000237 | prose | pages [10] -->
A1 −An +

<!-- b000238 | prose | pages [10] -->
⇣

<!-- b000239 | prose | pages [10] -->
= E

<!-- b000240 | prose | pages [10] -->
A1 −

<!-- b000241 | prose | pages [10] -->
n X

<!-- b000242 | prose | pages [10] -->
= λ −

<!-- b000243 | prose | pages [10] -->
i=1

<!-- b000244 | prose | pages [10] -->
1

<!-- b000245 | prose | pages [10] -->
i=1

<!-- b000246 | prose | pages [10] -->
⌘

<!-- b000247 | prose | pages [10] -->
n−1

<!-- b000248 | prose | pages [10] -->
n X

<!-- b000249 | prose | pages [10] -->
X

<!-- b000250 | prose | pages [10] -->
S(i)

<!-- b000251 | prose | pages [10] -->
Ii +

<!-- b000252 | prose | pages [10] -->
1

<!-- b000253 | prose | pages [10] -->
i=1

<!-- b000254 | prose | pages [10] -->
i=1

<!-- b000255 | prose | pages [10] -->
n−1 X

<!-- b000256 | prose | pages [10] -->
E(S(i)

<!-- b000257 | prose | pages [10] -->
λ +

<!-- b000258 | prose | pages [10] -->
1 )

<!-- b000259 | prose | pages [10] -->
i=1

<!-- b000260 | prose | pages [10] -->
= λ(1 −n) + E(S(1)

<!-- b000261 | prose | pages [10] -->
1 )(n −1)

<!-- b000262 | prose | pages [10] -->
where the third equality follows from linearity of expectations and since A1 and Ii are distributed exp(λ). Simplifying, we have

<!-- b000263 | prose | pages [10] -->
Q1 ) = (n −1)(E(S(1)

<!-- b000264 | prose | pages [10] -->
E(T (n)

<!-- b000265 | prose | pages [10] -->
1 ) −λ) (2)

<!-- b000266 | prose | pages [10] -->
This expression makes sense intuitively since if the expected service Remark. time per customer, E(S(1)

<!-- b000267 | prose | pages [10] -->
1 ), is large relative to time per passenger arrival, λ, then the line will build up, so the expected time spent waiting in the ﬁrst queue grows with n, the number of passengers. We also note an inconsistency in the expression, namely that it can be negative as it is currently written. In reality, time can never be negative. This negativity is a result of Assumption 6, since we don’t take the max of the quantity and 0 in our calculations. This remark is applicable to all boxed equations (5), (6), and (7). Once Assumption 6 is removed in section 3, the times will be strictly non-negative.

<!-- b000268 | prose | pages [10] -->
9 9

<!-- b000269 | prose | pages [11] -->
Team 56632

<!-- b000270 | furniture | pages [11] -->
Page 10 of 21

<!-- b000271 | prose | pages [11] -->
Similarly, we can express the time spent waiting in queue 2 recursively, and solve

<!-- b000272 | prose | pages [11] -->
Q2 . The process is very similar to that of T (n)

<!-- b000273 | prose | pages [11] -->
for T (n)

<!-- b000274 | prose | pages [11] -->
and go straight to the ﬁnal expression.

<!-- b000275 | prose | pages [11] -->
⇣n−1

<!-- b000276 | prose | pages [11] -->
n

<!-- b000277 | prose | pages [11] -->
X

<!-- b000278 | prose | pages [11] -->
X

<!-- b000279 | prose | pages [11] -->
T (n)

<!-- b000280 | prose | pages [11] -->
S(i)

<!-- b000281 | prose | pages [11] -->
T (i)

<!-- b000282 | prose | pages [11] -->
−

<!-- b000283 | prose | pages [11] -->
Q2 =

<!-- b000284 | prose | pages [11] -->
2

<!-- b000285 | prose | pages [11] -->
Q1

<!-- b000286 | prose | pages [11] -->
i=1

<!-- b000287 | prose | pages [11] -->
i=1

<!-- b000288 | prose | pages [11] -->
Q1 , so we omit the calculations

<!-- b000289 | prose | pages [11] -->
⌘ ⌘

<!-- b000290 | prose | pages [11] -->
+ A1 + S(1)

<!-- b000291 | prose | pages [11] -->
−An −S(n) 1

<!-- b000292 | prose | pages [11] -->
1

<!-- b000293 | prose | pages [11] -->
(d)

<!-- b000294 | prose | pages [11] -->
By the linearity of expectations and since S(1)

<!-- b000295 | prose | pages [11] -->
⇣n−1 X

<!-- b000296 | prose | pages [11] -->
E(T (n)

<!-- b000297 | prose | pages [11] -->
E(S(i)

<!-- b000298 | prose | pages [11] -->
2 ) −

<!-- b000299 | prose | pages [11] -->
Q2 ) =

<!-- b000300 | prose | pages [11] -->
i=1

<!-- b000301 | prose | pages [11] -->
Plugging in (2) for E(T (n)

<!-- b000302 | prose | pages [11] -->
= S(n)

<!-- b000303 | prose | pages [11] -->
1 ,

<!-- b000304 | prose | pages [11] -->
1

<!-- b000305 | prose | pages [11] -->
⌘

<!-- b000306 | prose | pages [11] -->
n X

<!-- b000307 | prose | pages [11] -->
E(T (i)

<!-- b000308 | prose | pages [11] -->
+ λ(1 −n)

<!-- b000309 | prose | pages [11] -->
Q1)

<!-- b000310 | prose | pages [11] -->
i=1

<!-- b000311 | prose | pages [11] -->
Q1 ) and simplifying using the i.i.d. assumption of the

<!-- b000312 | prose | pages [11] -->
S(i)

<!-- b000313 | prose | pages [11] -->
(2)’s, we have

<!-- b000314 | prose | pages [11] -->
⇣

<!-- b000315 | prose | pages [11] -->
⌘ 2 ) −1

<!-- b000316 | prose | pages [11] -->
E(T (n)

<!-- b000317 | prose | pages [11] -->
E(S(1)

<!-- b000318 | prose | pages [11] -->
Q2 ) = (n −1)

<!-- b000319 | prose | pages [11] -->
2 · (E(S(1) 1 ) −λ) −λ

<!-- b000320 | prose | pages [11] -->
(3)

<!-- b000321 | prose | pages [11] -->
Thus, the expected total time that passenger i spends in TSA checking is

<!-- b000322 | prose | pages [11] -->
Q1 ) + E(T (n)

<!-- b000323 | prose | pages [11] -->
E(T (n)

<!-- b000324 | prose | pages [11] -->
total) = E(T (n)

<!-- b000325 | prose | pages [11] -->
where E(T (n)

<!-- b000326 | prose | pages [11] -->
Q1 ) and E(T (n)

<!-- b000327 | prose | pages [11] -->
Q2 ) + E(S(1)

<!-- b000328 | prose | pages [11] -->
1 ) + E(S(1) 2 ) (4)

<!-- b000329 | prose | pages [11] -->
Q2 ) are given by (2) and (3).

<!-- b000330 | prose | pages [11] -->
2.2.2 Average Wait Time Values

<!-- b000331 | prose | pages [11] -->
To compute the average time that any passenger spends waiting in queue 1, T avg

<!-- b000332 | prose | pages [11] -->
Q1 , we take the average of the waiting times. This will yield an expression in terms of the T (i)

<!-- b000333 | prose | pages [11] -->
Q1’s, which are random variables. We then take the expectation to obtain the average time spent in the queue.

<!-- b000334 | prose | pages [11] -->
⇣1

<!-- b000335 | prose | pages [11] -->
n X

<!-- b000336 | prose | pages [11] -->
.= E

<!-- b000337 | prose | pages [11] -->
T avg

<!-- b000338 | prose | pages [11] -->
Q1

<!-- b000339 | prose | pages [11] -->
n

<!-- b000340 | prose | pages [11] -->
i=1

<!-- b000341 | prose | pages [11] -->
n X

<!-- b000342 | prose | pages [11] -->
= 1

<!-- b000343 | prose | pages [11] -->
⌘

<!-- b000344 | prose | pages [11] -->
T (i)

<!-- b000345 | prose | pages [11] -->
Q1

<!-- b000346 | prose | pages [11] -->
(i −1)(E(S(1)

<!-- b000347 | prose | pages [11] -->
n

<!-- b000348 | prose | pages [11] -->
i=1

<!-- b000349 | prose | pages [11] -->
1 ) −λ)

<!-- b000350 | prose | pages [11] -->
where the last equality follows from (2). Simplifying, we have

<!-- b000351 | prose | pages [11] -->
Q1 = n −1

<!-- b000352 | prose | pages [11] -->
T avg

<!-- b000353 | prose | pages [11] -->
2 (E(S(1)

<!-- b000354 | prose | pages [11] -->
1 ) −λ) (5)

<!-- b000355 | prose | pages [11] -->
A similar calculation that yielded average wait time for queue 1 will give

<!-- b000356 | prose | pages [11] -->
Q2 = n −1

<!-- b000357 | prose | pages [11] -->
· (E(S(1)

<!-- b000358 | prose | pages [11] -->
T avg

<!-- b000359 | prose | pages [11] -->
2 2 ) −1 1 ) −1 2E(S(1) 2λ) (6)

<!-- b000360 | prose | pages [11] -->
10 10

<!-- b000361 | prose | pages [12] -->
Team 56632

<!-- b000362 | furniture | pages [12] -->
Page 11 of 21

<!-- b000363 | prose | pages [12] -->
To ﬁnd the average total waiting time, we combine the average waiting times (5) and (6) with expression (1).

<!-- b000364 | prose | pages [12] -->
Q2 + E(S(1)

<!-- b000365 | prose | pages [12] -->
T avg

<!-- b000366 | prose | pages [12] -->
total = T avg

<!-- b000367 | prose | pages [12] -->
Q1 + T avg

<!-- b000368 | prose | pages [12] -->
1 ) + E(S(1) 2 ) (7)

<!-- b000369 | prose | pages [12] -->
We compute the boxed expressions (5), (6), and (7) to compare with the simula- tion in the following section. This will serve to validate our method of simulation.

<!-- b000370 | prose | pages [12] -->
3 The Simulation

<!-- b000371 | prose | pages [12] -->
A Dynamic Programming Method 3.1

<!-- b000372 | prose | pages [12] -->
In the previous section, assumptions on the number of ID check and scan stations were made in order to simplify calculations. As a result we were able to obtain In the following section we no longer make this simplifying explicit formulas. assumption and instead denote

<!-- b000373 | prose | pages [12] -->
c .= Number of service spots at check stations

<!-- b000374 | prose | pages [12] -->
k .= Number of service spots at scan stations

<!-- b000375 | prose | pages [12] -->
n .= Number of passengers

<!-- b000376 | prose | pages [12] -->
We denote the number of passengers by n even though our model isn’t restricted to any ﬁnite number of passengers. For the sake of the simulation, we sample for n passengers, where n can be made arbitrarily large.

<!-- b000377 | prose | pages [12] -->
Every passenger has an arrival time, a start/end time for the ID checking process, and a start/end time for the scanning process. Since our expression for these times is recursive, we take a dynamic programming approach to ﬁll out a 2-D array, whose rows represent time events and whose columns represent passengers.

<!-- b000378 | prose | pages [12] -->
Since inter-arrival times are distributed i.i.d. exponential(λ), we simulate arrival times by keeping a running sum of i.i.d. exponential random variables. Since there are c spots for ID checking, we inspect the ID check leaving times of the previous c passengers to determine which is most readily available. If the arrival time of the current passenger exceeds this quantity, then the passenger can directly enter one of the ID check spots. Otherwise they must wait until a spot opens up. The start time for the scan process is computed similarly using k, the number of scan stations, in place of c. The end times for both service stations are computed by sampling from the kernel density estimates for the service times and adding these to the start times.

<!-- b000379 | prose | pages [12] -->
To compute the average waiting times, we take the di↵erence between service start times and the times at which passengers start waiting, which is either their

<!-- b000380 | prose | pages [12] -->
11 11

<!-- b000381 | prose | pages [13] -->
Team 56632

<!-- b000382 | furniture | pages [13] -->
Page 12 of 21

<!-- b000383 | prose | pages [13] -->
arrival time or their ID check end time depending on the service for which they are in queue. We then take the average over all passengers and return this result. A more concise set of instructions is given below as pseudo code.

<!-- b000384 | prose | pages [13] -->
3.1.1 Pseudo code

<!-- b000385 | heading | pages [13] -->
Algorithm 1 TSA Security Simulation

<!-- b000386 | prose | pages [13] -->
Result: a vector representing the average time spent in queues and the entire

<!-- b000387 | prose | pages [13] -->
system.

<!-- b000388 | prose | pages [13] -->
First, initialize a two dimensional array with 5 rows and max(c, k) + n columns.

<!-- b000389 | prose | pages [13] -->
Each row represents either passenger arrival time, time entering check station, time exiting check station, time entering scan station, or time exiting scan station (ﬁnished).

<!-- b000390 | prose | pages [13] -->
for i 2 {max(c, k), . . . , n} do

<!-- b000391 | prose | pages [13] -->
Arrival(i) = Arrival(i−1) + sampleexp(λ)

<!-- b000392 | prose | pages [13] -->
start = max(Arrival(i), min(Check(i−c)

<!-- b000393 | prose | pages [13] -->
Check(i)

<!-- b000394 | prose | pages [13] -->
Check(i)

<!-- b000395 | prose | pages [13] -->
end = Check(i)

<!-- b000396 | prose | pages [13] -->
end , . . . , Check(i−1)

<!-- b000397 | prose | pages [13] -->
end ))

<!-- b000398 | prose | pages [13] -->
start + sampleid check

<!-- b000399 | prose | pages [13] -->
end, min(Scan(i−k)

<!-- b000400 | prose | pages [13] -->
Scan(i)

<!-- b000401 | prose | pages [13] -->
start = max(Check(i)

<!-- b000402 | prose | pages [13] -->
Scan(i)

<!-- b000403 | prose | pages [13] -->
end = Scan(i)

<!-- b000404 | prose | pages [13] -->
start + samplescan end

<!-- b000405 | prose | pages [13] -->
T avg

<!-- b000406 | prose | pages [13] -->
Q1 = 1

<!-- b000407 | prose | pages [13] -->
n · sum(Checkstart −Arrival)

<!-- b000408 | prose | pages [13] -->
T avg

<!-- b000409 | prose | pages [13] -->
Q2 = 1

<!-- b000410 | prose | pages [13] -->
n · sum(Scanstart −Checkend)

<!-- b000411 | prose | pages [13] -->
T avg

<!-- b000412 | prose | pages [13] -->
Total = 1

<!-- b000413 | prose | pages [13] -->
n · sum(Scanend −Arrival)

<!-- b000414 | prose | pages [13] -->
return (T avg

<!-- b000415 | prose | pages [13] -->
Q1 , T avg

<!-- b000416 | prose | pages [13] -->
Q2 , T avg

<!-- b000417 | prose | pages [13] -->
Total)

<!-- b000418 | prose | pages [13] -->
3.2

<!-- b000419 | heading | pages [13] -->
Comparison to the Model

<!-- b000420 | prose | pages [13] -->
end , . . . , Scan(i−1)

<!-- b000421 | prose | pages [13] -->
end ))

<!-- b000422 | prose | pages [13] -->
We implemented the simulation described above in Matlab and compared the simulated average waiting times with their explicit formulas which were derived in the previous section, namely, expressions (3), (6), and (7).

<!-- b000423 | prose | pages [13] -->
12 12

<!-- b000424 | prose | pages [14] -->
Team 56632

<!-- b000425 | furniture | pages [14] -->
Page 13 of 21

<!-- b000426 | caption | pages [14] -->
Figure 5: Plot of the average time spent in queues 1 (left) and 2 (right). Simulated

<!-- b000427 | prose | pages [14] -->
and theoretical time averages are depicted in blue and orange respectively.

<!-- b000428 | caption | pages [14] -->
Figure 5 shows the calculated results from our model against the simulated results.

<!-- b000429 | prose | pages [14] -->
It appears that they follow the same trend on average as the number of passengers increases from 50 to 4050. As a result, we are more inclined to believe the results obtained from using our simulation in the proceeding experiments. The simulation also seems to vary from the theoretical results more drastically in the waiting time for queue 1. However, looking at the scale on which these waiting times are plotted, we reason that we see this relatively large variance because the waiting times for queue 1 are much smaller in magnitude than those for queue 2. The plot of simulated versus theoretical values for total time spent in the system is omitted since it is essentially the sum of the above two plots and as a result, follows the same trend.

<!-- b000430 | prose | pages [14] -->
4

<!-- b000431 | heading | pages [14] -->
Evaluation/Results

<!-- b000432 | prose | pages [14] -->
4.1 Bottlenecks in Passenger Throughput

<!-- b000433 | prose | pages [14] -->
From our model we identiﬁed two major bottlenecks in the ﬂow of passengers through airport security: ID check stations and scan stations. Through simulation we investigated how the number of service spots at each station a↵ects the total time a passenger waits.

<!-- b000434 | prose | pages [14] -->
4.1.1 ID Check Station

<!-- b000435 | prose | pages [14] -->
The ﬁrst bottleneck a passenger experiences upon reaching airport security is the ID check station. Both TSA precheck and regular passengers receive service at the same rate from this station and therefore, when investigating this bottleneck we considered only one service distribution. However, TSA precheck and regular

<!-- b000436 | prose | pages [14] -->
13

<!-- b000437 | prose | pages [15] -->
Team 56632

<!-- b000438 | furniture | pages [15] -->
Page 14 of 21

<!-- b000439 | prose | pages [15] -->
passengers arrive at di↵erent rates to this station, so we investigated how varying arrival rates and the number of check stations would a↵ect the wait time in the checking queue. The results from our simulation can be seen below.

<!-- b000440 | caption | pages [15] -->
Figure 6: Plot of wait time spent in ID check queue for various values of c (left)

<!-- b000441 | prose | pages [15] -->
and k (right).

<!-- b000442 | prose | pages [15] -->
The average wait time of a passenger in the checking queue appears to be inde- pendent of the number of scanning stations, k, an intuitive result. However, there is a clear relationship between the number of open spots at the ID check station, c, and the average wait time of a passenger in the ID check queue. The wait time undergoes a signiﬁcant transition, decreasing drastically, as the arrival rate of passengers slows (λ increases). Using the queuing model described previously, the λ value at which this transition takes place can be estimated by the following relation.

<!-- b000443 | prose | pages [15] -->
λ = E(S(i)

<!-- b000444 | prose | pages [15] -->
1 ) (8) c

<!-- b000445 | prose | pages [15] -->
Remark. This relation can be understood as the condition for when the average arrival rate (λ) is equal to the average service rate (E(S(i)

<!-- b000446 | prose | pages [15] -->
1 )/c). When passengers arrive faster than they are being serviced at the ID check stations, a queue forms, causing a bottle neck on passenger throughput. Conversely, when passengers are serviced more quickly than they arrive, a queue becomes less likely to form. In the case of c = 1, this is equivalent to setting the expected waiting time in Q1 given by (2) equal to 0.

<!-- b000447 | prose | pages [15] -->
The estimated λ transition values given by (8) are plotted as vertical lines on the same plot in Figure 6. One can see that these points correspond very closely to the observed transitions from our simulation.

<!-- b000448 | prose | pages [15] -->
14 14

<!-- b000449 | prose | pages [16] -->
Team 56632

<!-- b000450 | prose | pages [16] -->
4.1.2 Scan Station

<!-- b000451 | furniture | pages [16] -->
Page 15 of 21

<!-- b000452 | prose | pages [16] -->
The second bottleneck a passenger will experience in airport security is the scan station. We conducted an analysis similar to the one we performed on the ﬁrst bottleneck. Unlike the ID check station, TSA precheck and regular passengers experience di↵erent service rates at this station; however, the general trend re- mains the same. The results from our simulation of regular passengers can be seen below.

<!-- b000453 | caption | pages [16] -->
Figure 7: Plot of average time spent in the regular scan queue with varying arrival

<!-- b000454 | prose | pages [16] -->
rates for various values of c (left) and k (right).

<!-- b000455 | prose | pages [16] -->
The average wait time of a passenger in the scanning station is dependent on both c and k. We observe that the concept of λ transition values, discussed above in the ﬁrst bottleneck, are important as they mark signiﬁcant transitions in T (n)

<!-- b000456 | prose | pages [16] -->
where the analogous values are given by Q2 ,

<!-- b000457 | prose | pages [16] -->
λ = E(S(i)

<!-- b000458 | prose | pages [16] -->
2 ) (9) c

<!-- b000459 | prose | pages [16] -->
Variance in Passenger Wait Time 4.2

<!-- b000460 | prose | pages [16] -->
Increasing passenger throughput and decreasing wait times is only part of the story when it comes to improving airport security. Equally important is reducing the variance in passenger wait times to ensure that passengers know generally how long security lines will be. Using our simulation, we investigated how the number of check stations (c) and scan stations (k) a↵ected the variance of passenger wait times in queues. We found that the number of check stations had a larger a↵ect on the variance of wait times in both queues than the number of scan stations.

<!-- b000461 | prose | pages [16] -->
15 15

<!-- b000462 | prose | pages [17] -->
Team 56632

<!-- b000463 | furniture | pages [17] -->
Page 16 of 21

<!-- b000464 | caption | pages [17] -->
Figure 8: Plot of variance of passenger wait times spent in check station queue

<!-- b000465 | prose | pages [17] -->
(left) and scan station queue (right) for various values of c and constant k = 1.

<!-- b000466 | prose | pages [17] -->
As seen in the plots above, the variance in passenger wait times spent in either queue decreases as arrival rate increases. Major transitions occur at the same λ transition values given by (8).

<!-- b000467 | prose | pages [17] -->
4.3

<!-- b000468 | heading | pages [17] -->
Modiﬁcations to the Model

<!-- b000469 | prose | pages [17] -->
4.3.1 Cost-Beneﬁt Analysis

<!-- b000470 | prose | pages [17] -->
In this section we confront the optimization problem of balancing the cost of employing TSA workers with the beneﬁt of increasing passenger ﬂow. Following the events of September 11, TSA began to include a $6.60 security fee per one- way-trip in the year 2017 [3]. The fee goes to funding the TSA’s airport security measures. In other words, increasing passenger throughput while limiting secu- rity costs can be proﬁtable for TSA. In order to investigate this relationship, we describe an objective function for TSA proﬁt using the following variables.

<!-- b000471 | prose | pages [17] -->
Cp .= September 11 fee per one-way-trip

<!-- b000472 | prose | pages [17] -->
Ct .= The cost of a Transportation Security Oﬃcer (TSO).

<!-- b000473 | prose | pages [17] -->
Ttotal .= Average time spent from entering to leaving the system.

<!-- b000474 | prose | pages [17] -->
Remark. In the ATL Hartsﬁeld-Jackson airport, a TSO makes on average 18.5 dollars an hour. Converting this salary into units relevant to our calculations, the average TSO makes 0.0005139 dollars per second [9]. In addition, we assume that 1 TSO is required to operate an ID check station, and that 3 TSOs are required to operate a scan station: one for the mm wave scan, one for the X-Ray, and one for auxiliary help.

<!-- b000475 | prose | pages [17] -->
16

<!-- b000476 | prose | pages [18] -->
Team 56632

<!-- b000477 | furniture | pages [18] -->
Page 17 of 21

<!-- b000478 | prose | pages [18] -->
Assumption 7: The only cost for running a TSA security check point is to employ TSA workers.

<!-- b000479 | prose | pages [18] -->
Remark.

<!-- b000480 | prose | pages [18] -->
There are other costs including management, machine mainte- nance, and training of TSOs, but these costs per employee are marginal compared to employee salary.

<!-- b000481 | prose | pages [18] -->
Finally, we deﬁne TSA proﬁt rate, P, as the di↵erence in the rate at which TSA gains money through the September 11 fee and the rate at which TSA loses money by staﬃng employees. Combining the terms deﬁned above in this way yields a measure of proﬁt, P, whose units are dollars per second.

<!-- b000482 | prose | pages [18] -->
Cp

<!-- b000483 | prose | pages [18] -->
−(c + 3k) · Ct

<!-- b000484 | prose | pages [18] -->
P = Ttotal

<!-- b000485 | prose | pages [18] -->
As in section 3, c and k refer to the number of spots at ID check stations and scan stations, respectively. We wish to ﬁnd the parameters c and k which maximize this objective function. Using the dynamic programming approach described in section 3, we sample values for Ttotal, compute P for di↵erent values of c and k, and plot the resulting heat maps below.

<!-- b000486 | caption | pages [18] -->
Figure 9: Proﬁt as a function of the number of ID check and scan stations for

<!-- b000487 | prose | pages [18] -->
TSA precheck (left) and Regular passengers (right).

<!-- b000488 | prose | pages [18] -->
For the TSA precheck line, the most cost-eﬃcient layout is to have 3 checking stations and 3 scanning stations to achieve a rate of P = 0.140 dollars per second. For the regular security line, the most cost-eﬃcient layout is to have 2 checking stations and 3 scanning stations, yielding a proﬁt rate of P = 0.083 dollars per second.

<!-- b000489 | prose | pages [18] -->
TSA precheck gives the TSA a 68.6% gain in revenue per passenger compared to regular screening.

<!-- b000490 | prose | pages [18] -->
17

<!-- b000491 | prose | pages [19] -->
Team 56632

<!-- b000492 | furniture | pages [19] -->
Page 18 of 21

<!-- b000493 | prose | pages [19] -->
4.3.2

<!-- b000494 | heading | pages [19] -->
Sensitivity Analysis

<!-- b000495 | prose | pages [19] -->
Our other modiﬁcation is the introduction of virtual queuing, a method ﬁrst implemented in call centers for minimizing perceived wait times [7].

<!-- b000496 | prose | pages [19] -->
After a passenger checks in for their ﬂight, the airline assigns them an arrival time and a window around this time to enter the security process. The assigned boarding time instructs the passenger when to arrive at the ﬁrst queue. The passenger now has more free time to shop at airport businesses instead of physically waiting in line. Virtual queuing not only allows for the reduction in perceived wait time but also for the implementation of non-FIFO disciplines.

<!-- b000497 | prose | pages [19] -->
We distinguish between two types of travelers: slow and fast (inexperienced and experienced), whose service times are multiplied by a predetermined factor. We deﬁne a new discipline, Priority, to describe the use of the virtual queue to group passengers of similar experience levels together, so that all slow passengers go ﬁrst, followed by the quick passengers. This is done in contrast to the previous discipline, in which passengers of varying speeds arrive randomly.

<!-- b000498 | caption | pages [19] -->
Figure 10: Plots of time (left) and variance (right) versus the fraction of fast

<!-- b000499 | prose | pages [19] -->
passengers for the Priority (orange) and FIFO disciplines (blue).

<!-- b000500 | prose | pages [19] -->
In Figure 10, we plot wait time vs. the fraction of slow passengers. Contrary to our initial hypotheses, the Priority discipline generally led to both longer average total wait time and higher variance. A possible explanation is that if slow people go ﬁrst, they cause fast passengers to wait longer in line, increasing the average overall time waiting.

<!-- b000501 | prose | pages [19] -->
In reality, inexperienced travelers (slow) are more likely to come early as they are new to the security process while experienced travelers (fast) are likely to come late. Thus, they will naturally group up into something similar to the conditions of our Priority discipline simulation. Because our simulations suggest that this decreases passenger throughput, airports can use virtual queuing and new disci- plines to ensure a more uniform distribution of passengers to avoid bottlenecks.

<!-- b000502 | prose | pages [19] -->
18

<!-- b000503 | prose | pages [20] -->
Team 56632

<!-- b000504 | furniture | pages [20] -->
Page 19 of 21

<!-- b000505 | prose | pages [20] -->
5

<!-- b000506 | heading | pages [20] -->
Improving the Model

<!-- b000507 | prose | pages [20] -->
5.1 Traveler Characteristics

<!-- b000508 | prose | pages [20] -->
In our model and modiﬁcations, we only account for travelers we deem slow and fast based on traveling experience. However, we can get more nuanced results by creating a system to proﬁle people based on a variety of features like age, walking speed, families, etc.

<!-- b000509 | prose | pages [20] -->
Perhaps there would be an optimal solution in creating di↵erent lanes designed for di↵erent types of travelers.

<!-- b000510 | prose | pages [20] -->
5.2 Di↵erent Queuing Disciplines

<!-- b000511 | prose | pages [20] -->
We only considered the FIFO and Priority disciplines for our simulation.

<!-- b000512 | prose | pages [20] -->
We can further explore new disciplines and ways of organizing passenger populations. These disciplines could possibly lead to more e↵ective virtual queuing.

<!-- b000513 | prose | pages [20] -->
5.3 Arrival Rate Regulation

<!-- b000514 | prose | pages [20] -->
Due to the nature of airport scheduling, it is unlikely that arrival rates follow a consistent Poisson distribution throughout the course of a day [2].

<!-- b000515 | prose | pages [20] -->
Virtual queuing gives us greater control over the arrival rate (λ) variation, because we set the passenger arrival times. In our simulations we show that total wait time and its variance is largely characterized by the ﬂuctuation in λ. Therefore, we can explore methods to regulate the arrival rate while ensuring all passengers make their ﬂight.

<!-- b000516 | prose | pages [20] -->
5.4 Improving Proﬁt Measure

<!-- b000517 | prose | pages [20] -->
There were many sources of cost and revenue which were not included in the construction of our proﬁt measure.

<!-- b000518 | prose | pages [20] -->
Some examples are machine maintenance, employee management, and variance in passenger wait times.

<!-- b000519 | prose | pages [20] -->
6

<!-- b000520 | heading | pages [20] -->
Conclusion

<!-- b000521 | prose | pages [20] -->
Our solution to the problem of excessive waiting times in airport security re- quired the use of a diverse collection of techniques from the ﬁelds of statistics and computer science.

<!-- b000522 | prose | pages [20] -->
The uncertainty in the dynamics of the TSA security check were described by a queuing network and simulated with the use of dy- namic programming. The results of our simulations helped to indicate an optimal

<!-- b000523 | prose | pages [20] -->
19

<!-- b000524 | prose | pages [21] -->
Team 56632

<!-- b000525 | furniture | pages [21] -->
Page 20 of 21

<!-- b000526 | prose | pages [21] -->
number of security oﬃcers to employ in order to maximize proﬁt rate, while the sensitivity analysis hinted that our initial intuitions about line ordering based on passenger experience were ﬂawed. We further identiﬁed where we could make our model more powerful by considering things such as traveler characteristics, cre- ative queuing disciplines, and arrival time regulation. The real world continues to present all sorts of interesting problems for mankind to think about and develop mathematical tools to solve. Our attempt to gain insight into this problem closely follows this narrative, illustrating and verifying the importance of bringing theory to application and curiosity to exploration.

<!-- b000527 | prose | pages [21] -->
20

<!-- b000528 | prose | pages [22] -->
Team 56632

<!-- b000529 | furniture | pages [22] -->
Page 21 of 21

<!-- b000530 | heading | pages [22] -->
References

<!-- b000531 | references | pages [22] -->
[1] Chen, Hong, David D. Yao. “Fundamentals of Queuing Networks: Perfor-

<!-- b000532 | references | pages [22] -->
mance, Asymptotics, and Optimization.” New York: Springer, 2001. Print.

<!-- b000533 | references | pages [22] -->
[2] Dorton, Stephen L. ”Analysis of Airport Security Screening Checkpoints using

<!-- b000534 | references | pages [22] -->
Queuing Networks and Discrete Event Simulation: A Theoretical and Empir-

<!-- b000535 | references | pages [22] -->
ical Approach.” Embry-Riddle Scholarly Commons (2011): n. pag. Embry-

<!-- b000536 | references | pages [22] -->
Riddle Aeronautical Unviersity, 2011. Web.

<!-- b000537 | references | pages [22] -->
[3] Gillen, David, William G. Morrison. “Aviation security: Costing, pricing,

<!-- b000538 | references | pages [22] -->
ﬁnance and performance.” Journal of Air Transport Management 48 (2015):

<!-- b000539 | references | pages [22] -->
1-12. Web. 21 Jan. 2017.

<!-- b000540 | references | pages [22] -->
[4] Bowman, A. W., Adelchi Azzalini. “Applied smoothing techniques for data

<!-- b000541 | references | pages [22] -->
analysis: the kernel approach with S-Plus illustrations.” Oxford: Clarendon

<!-- b000542 | references | pages [22] -->
Press, 1997. Print.

<!-- b000543 | references | pages [22] -->
[5] Casella, George, and Roger L. Berger. “Statistical inference.” Australia:

<!-- b000544 | references | pages [22] -->
Thomson Learning, 2002. Print.

<!-- b000545 | references | pages [22] -->
[6] Jacobson, Sheldon H., Arash Khatibi, Ge Yu. “When should TSA PreCheck

<!-- b000546 | references | pages [22] -->
be o↵ered at no cost to travelers?” Journal of Transportation Security (2016):

<!-- b000547 | references | pages [22] -->
1-7. Web. 21 Jan. 2017.

<!-- b000548 | references | pages [22] -->
[7] Lange, Robert De, Ilya Samoilovich, Bo Van Der Rhee. “Virtual queuing at air-

<!-- b000549 | references | pages [22] -->
port security lanes.” European Journal of Operational Research 225.1 (2013):

<!-- b000550 | references | pages [22] -->
153-65. Web. 21 Jan. 2017.

<!-- b000551 | references | pages [22] -->
[8] TranSafety. “Study Compares Older and Younger Pedestrian Walking

<!-- b000552 | references | pages [22] -->
Speeds.” USRoads. N.p., n.d. Web. 22 Jan. 2017.

<!-- b000553 | references | pages [22] -->
[9] “Transportation Security Oﬃcer (TSO) Job O↵ering.” USAJOBS. Trans-

<!-- b000554 | references | pages [22] -->
portation Security Administration, n.d. Web. 21 Jan. 2017.

<!-- b000555 | references | pages [22] -->
[10] “TSA releases 2015 statistics.” Transportation Security Administration. De-

<!-- b000556 | references | pages [22] -->
partment of Homeland Security, 21 Jan. 2016. Web. 21 Jan. 2017.

<!-- b000557 | references | pages [22] -->
21
