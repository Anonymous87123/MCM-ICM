# P-D-2017-56632-67f41f43

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000003 | front_matter | pages [1] -->
56632

<!-- b000004 | front_matter | pages [1] -->
T1 ________________ F1 ________________ T2 ________________ F2 ________________ Problem Chosen T3 ________________ F3 ________________

<!-- b000005 | front_matter | pages [1] -->
D

<!-- b000006 | front_matter | pages [1] -->
T4 ________________ F4 ________________

<!-- b000007 | front_matter | pages [1] -->
2017

<!-- b000008 | prose | pages [1] -->
MCM/ICM

<!-- b000009 | heading | pages [1] -->
Summary Sheet

<!-- b000010 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000011 | prose | pages [1] -->
Passengers arrive at TSA security screening at seemingly random times, and the uncertainty in their arrival along with TSA inefficiencies can cause abnormally long and varying wait times. A major problem the agency must confront is the improvement of passenger throughput while maintaining a strict standard of security. Our solution consists of four main parts: a queuing model describing the security screening, a method of simulation for theory verification and experimentation, the application of these results to cost-benefit analysis, and modifications to the model to account for different traveler characteristics.

<!-- b000012 | prose | pages [1] -->
We decided that a reasonable measure for TSA inefficiency was the average time a passenger spent waiting in line. The queuing model was formulated by expressing the relationship between wait times in the queue recursively. We used kernel density estimation and exponential fitting to estimate distributions on the random variables involved in the model. We obtained explicit expressions for passenger wait times, which we used to reason about the system behavior as the number of passengers and arrival rates varied.

<!-- b000013 | prose | pages [1] -->
Using the above framework we developed a method for simulation that used dynamic programming to sample arrival times of passengers within the security system. The simulation numerically verified the results of the theory and allowed for further experimentation with varying parameters. The results of these experiments gave us insights on where the TSA procedure could be optimized and the passenger experience improved.

<!-- b000014 | prose | pages [1] -->
We applied cost-benefit analysis to the efficiency-cost tradeoff that TSA must consider when staffing employees and screening passengers. We found an optimal allocation of resources that maximized profit rate by plotting a profit objective function against the different configurations of TSA employees.

<!-- b000015 | prose | pages [1] -->
Finally, we considered distinctions between travelers and how they might affect the activity in the queuing system and each other’s wait times as a result. We investigated alternative methods to order passengers in queue and found that this approach was not as successful as we expected.

<!-- b000016 | prose | pages [1] -->
Using a diverse array of techniques, we were able to successfully model the flow of passengers through airport security, identify bottlenecks in the screening process, and suggest improvements to the current procedure. As our world becomes more interconnected and airline activity increases, TSA will have to confront the issue of passenger throughput inefficiency. The use of mathematical models will undoubtedly become an invaluable tool in optimizing efficiency while maintaining passenger safety.

<!-- b000017 | title | pages [2] -->
Reducing Wait Times at Airport Security

<!-- b000018 | prose | pages [2] -->
Team 56632

<!-- b000019 | prose | pages [2] -->
January 24, 2017

<!-- b000020 | heading | pages [2] -->
Abstract

<!-- b000021 | prose | pages [2] -->
In this report, we develop and employ a queuing model for lines and servicing at TSA security in order to identify bottlenecks in the procedure and suggest improvements. We model the inﬂux of passengers as a Poisson process, allowing us to sample from an exponential distribution to simulate inter-arrival times. To ﬁnd probabilistic distributions on the service time spent in security stations, we take a nonparametric approach, using kernel density estimation to obtain probability densities from the given data. Us- ing recurrence concepts from our queuing network, we develop a simulation method via dynamic programming as a means to verify the theoretical results and conduct further experiments. We apply these results to a cost-beneﬁt analysis, which we use to identify the optimal allocation of TSA resources. Additionally, we consider di↵erent cultural norms regarding passenger in- teraction in queues, and add complexity in our model to account for them. These tools allow us to perform experiments, which are realistic within rea- son, and give suggestions for improvement in a manner justiﬁed by both the given and researched data.

<!-- b000022 | prose | pages [2] -->
1

<!-- b000023 | heading | pages [3] -->
Contents

<!-- b000024 | contents | pages [3] -->
1 Introduction

<!-- b000025 | contents | pages [3] -->
3

<!-- b000026 | contents | pages [3] -->
1.1

<!-- b000027 | contents | pages [3] -->
Outline

<!-- b000028 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [3] -->
3

<!-- b000030 | contents | pages [3] -->
1.2

<!-- b000031 | contents | pages [3] -->
Main Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [3] -->
3

<!-- b000033 | contents | pages [3] -->
2 A Queuing Model

<!-- b000034 | contents | pages [3] -->
4

<!-- b000035 | contents | pages [3] -->
2.1

<!-- b000036 | contents | pages [3] -->
Obtaining Probability Densities . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [3] -->
5

<!-- b000038 | contents | pages [3] -->
2.1.1

<!-- b000039 | contents | pages [3] -->
Exponential Fitting

<!-- b000040 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [3] -->
5

<!-- b000042 | contents | pages [3] -->
2.1.2

<!-- b000043 | contents | pages [3] -->
Kernel Density Estimation

<!-- b000044 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [3] -->
6

<!-- b000046 | contents | pages [3] -->
2.2

<!-- b000047 | contents | pages [3] -->
Writing Down a Recurrence . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [3] -->
8

<!-- b000049 | contents | pages [3] -->
2.2.1

<!-- b000050 | contents | pages [3] -->
Deﬁnitions and Derivations . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [3] -->
8

<!-- b000052 | contents | pages [3] -->
2.2.2

<!-- b000053 | contents | pages [3] -->
Average Wait Time Values

<!-- b000054 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [3] -->
10

<!-- b000056 | contents | pages [3] -->
3 The Simulation

<!-- b000057 | contents | pages [3] -->
11

<!-- b000058 | contents | pages [3] -->
3.1

<!-- b000059 | contents | pages [3] -->
A Dynamic Programming Method

<!-- b000060 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [3] -->
11

<!-- b000062 | contents | pages [3] -->
3.1.1

<!-- b000063 | contents | pages [3] -->
Pseudo code . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [3] -->
12

<!-- b000065 | contents | pages [3] -->
3.2

<!-- b000066 | contents | pages [3] -->
Comparison to the Model . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [3] -->
12

<!-- b000068 | contents | pages [3] -->
4 Evaluation/Results

<!-- b000069 | contents | pages [3] -->
13

<!-- b000070 | contents | pages [3] -->
4.1

<!-- b000071 | contents | pages [3] -->
Bottlenecks in Passenger Throughput

<!-- b000072 | contents | pages [3] -->
. . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [3] -->
13

<!-- b000074 | contents | pages [3] -->
4.1.1

<!-- b000075 | contents | pages [3] -->
ID Check Station . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [3] -->
13

<!-- b000077 | contents | pages [3] -->
4.1.2

<!-- b000078 | contents | pages [3] -->
Scan Station

<!-- b000079 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [3] -->
15

<!-- b000081 | contents | pages [3] -->
4.2

<!-- b000082 | contents | pages [3] -->
Variance in Passenger Wait Time . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [3] -->
15

<!-- b000084 | contents | pages [3] -->
4.3

<!-- b000085 | contents | pages [3] -->
Modiﬁcations to the Model

<!-- b000086 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [3] -->
16

<!-- b000088 | contents | pages [3] -->
4.3.1

<!-- b000089 | contents | pages [3] -->
Cost-Beneﬁt Analysis

<!-- b000090 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [3] -->
16

<!-- b000092 | contents | pages [3] -->
4.3.2

<!-- b000093 | contents | pages [3] -->
Sensitivity Analysis

<!-- b000094 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [3] -->
18

<!-- b000096 | contents | pages [3] -->
5 Improving the Model

<!-- b000097 | contents | pages [3] -->
19

<!-- b000098 | contents | pages [3] -->
5.1

<!-- b000099 | contents | pages [3] -->
Traveler Characteristics

<!-- b000100 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000101 | contents | pages [3] -->
19

<!-- b000102 | contents | pages [3] -->
5.2

<!-- b000103 | contents | pages [3] -->
Di↵erent Queuing Disciplines . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [3] -->
19

<!-- b000105 | contents | pages [3] -->
5.3

<!-- b000106 | contents | pages [3] -->
Arrival Rate Regulation . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [3] -->
19

<!-- b000108 | contents | pages [3] -->
5.4

<!-- b000109 | contents | pages [3] -->
Improving Proﬁt Measure . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [3] -->
19

<!-- b000111 | contents | pages [3] -->
6 Conclusion

<!-- b000112 | contents | pages [3] -->
19

<!-- b000113 | contents | pages [3] -->
7 Bibliography

<!-- b000114 | contents | pages [3] -->
21

<!-- b000115 | contents | pages [3] -->
2

<!-- b000116 | contents | pages [4] -->
Team 56632

<!-- b000117 | furniture | pages [4] -->
Page 3 of 21

<!-- b000118 | heading | pages [4] -->
1 Introduction

<!-- b000119 | prose | pages [4] -->
In this report, we present a model and simulation to optimize TSA security lines with respect to passenger throughput and variance in wait times. Speciﬁcally, we study the relationship between the number of ID check and scan stations and arrival rate to identify bottlenecks in the security process. We also deﬁne a cost measure to determine the optimal number of service stations. Further, we explore the implementation of a “virtual queue” and varying passenger traveling speeds and how they impact these bottlenecks. Our model provides the TSA valuable information for reducing wait time and variance in security lines, while maintaining the same standards of safety and security.

<!-- b000120 | heading | pages [4] -->
1.1 Outline

<!-- b000121 | prose | pages [4] -->
Our objective is to develop and implement a model to explore the ﬂow of pas- sengers through airport security, identify bottlenecks in the current process, and suggest modiﬁcations. To realize this objective we will proceed as follows:

<!-- b000122 | prose | pages [4] -->
• Formulate a queuing model to explore passenger wait times as a measure of ineﬃciency.

<!-- b000123 | prose | pages [4] -->
• Implement a simulation method to verify the theoretical framework and perform experiments to gain further insights.

<!-- b000124 | prose | pages [4] -->
• Analyze simulation results to identify the optimal allocation of resources according to a cost-beneﬁt analysis.

<!-- b000125 | prose | pages [4] -->
• Make modiﬁcations to the model based on cost-beneﬁt analysis and cultural di↵erences. Incorporate more complexity in the model to account for these considerations.

<!-- b000126 | heading | pages [4] -->
1.2 Main Assumptions

<!-- b000127 | prose | pages [4] -->
Queuing systems are probabilistic in nature and as a result are diﬃcult to de- scribe and predict. In order to quantify the uncertainty in waiting times, it is necessary to make some simplifying assumptions. Listed below are several of the main assumptions we make regarding how we view the problem. Throughout the remainder of this paper we introduce additional assumptions as they become relevant.

<!-- b000128 | prose | pages [4] -->
• Transit times between stations and queues are negligible. We as- sume that the time spent moving from a queue to a station or a station to

<!-- b000129 | prose | pages [4, 5] -->
3 Team 56632

<!-- b000131 | furniture | pages [5] -->
Page 4 of 21

<!-- b000132 | prose | pages [5] -->
a queue is negligible. This is a reasonable assumption in that most TSA checkpoints are relatively compact.

<!-- b000133 | prose | pages [5] -->
• Queues operate on the “First In First Out” (FIFO) discipline. This principle states that the ﬁrst person to line up in a queue will be the ﬁrst person to be served.

<!-- b000134 | prose | pages [5] -->
• All employees are identical in terms of competency at their job. We assume that all TSA employees are equally capable. This isn’t entirely realistic because some workers are better at their jobs than others; however, this distinction doesn’t serve to provide any further meaningful insights into the problem.

<!-- b000135 | prose | pages [5] -->
• Passenger wait times are an accurate measure of throughput eﬃ- ciency. Large passenger wait times in queues are the result of ineﬃciencies in the TSA screening process. Passenger throughput (given as passengers per unit time) is inversely proportional to time spent in the system by each passenger. Thus, maximizing passenger throughput is essentially the same as minimizing wait time.

<!-- b000136 | heading | pages [5] -->
2 A Queuing Model

<!-- b000137 | prose | pages [5] -->
We model the airport security line as 2 nearly-identical parallel queuing networks with the FIFO discipline depicted below. The network with green entities corre- sponds to the TSA precheck lane and the network with blue entities corresponds to passengers in the regular lane. Both networks are comprised of a queue, Q1, leading to a server S1 (ID check station), leading to another queue Q2, leading to another server S2 (scan station, which includes mm wave scan, carry on screening, and extra screening if necessary). A pre-determined fraction of people will queue in the precheck lane while the rest will queue in the regular lane.

<!-- b000138 | caption | pages [5] -->
Figure 1: A schematic of the queuing model. The superscripts “pre” and “reg”

<!-- b000139 | prose | pages [5] -->
stand for “precheck” and “regular”, respectively.

<!-- b000140 | prose | pages [5, 6] -->
4 Team 56632

<!-- b000142 | furniture | pages [6] -->
Page 5 of 21

<!-- b000143 | prose | pages [6] -->
Assumption 1: Time spent in additional screening (Zone D) was included in the “Time to get scanned property” column in the given data ﬁle.

<!-- b000144 | prose | pages [6] -->
Remark. Data was given as total time until picking up scanned property (column H), which would be done after the additional Zone D screening. This implies that column H incorporates any time spent in Zone D.

<!-- b000145 | prose | pages [6] -->
Assumption 2: For the ﬁrst version of our model, we assume that the system includes only the top row in Figure 1, and that there is only one service spot at each of S1 (ID check) and S2 (scan station). Later on we will remove this assumption.

<!-- b000146 | prose | pages [6] -->
Remark. In order to explicitly solve the recurrence relations we develop later on, it suﬃces to assume that service stations S1 and S2 each can only service one entity at a time. When we eventually take a dynamic programming approach, we will vary the number of ID check and scan stations and select a conﬁguration which optimizes the cost-beneﬁt tradeo↵(See “Cost-Beneﬁt Analysis” section).

<!-- b000147 | heading | pages [6] -->
2.1 Obtaining Probability Densities

<!-- b000148 | heading | pages [6] -->
2.1.1 Exponential Fitting

<!-- b000149 | prose | pages [6] -->
Depicted below are histograms of the passenger inter-arrival times extracted from the given data ﬁle. They strongly resemble the shape of an exponential probability density, motivating the next key assumption.

<!-- b000150 | caption | pages [6] -->
Figure 2: The exponential ﬁt (using Matlab’s expfit function) to the inter-

<!-- b000151 | prose | pages [6] -->
arrival times of precheck (left) and regular (right) passengers overlaid onto the corresponding histograms.

<!-- b000152 | prose | pages [6, 7] -->
5 Team 56632

<!-- b000154 | furniture | pages [7] -->
Page 6 of 21

<!-- b000155 | prose | pages [7] -->
Assumption 3: The inter-arrival times are distributed i.i.d. exponential with rate λreg = 12.9 and λpre = 9.2 (seconds per passenger).

<!-- b000156 | prose | pages [7] -->
Remark. We chose to model the incoming passengers as a Poisson Pro- cess, since the histogram of the inter-arrival times resembles an exponential distribution, a deﬁning characteristic of the inter-arrival times of a Poisson Process. The estimate for the rate parameter λ we used was the sample mean of the inter-arrival times, as given by maximum likelihood estimation[5].

<!-- b000157 | heading | pages [7] -->
2.1.2 Kernel Density Estimation

<!-- b000158 | prose | pages [7] -->
We deﬁne the following random variables.

<!-- b000159 | prose | pages [7] -->
.= The total time entity j spends at TSA check in. T (j) total .= The wait time of entity j in queue i. T (j) Qi .= The time spent of entity j in service i. S(j) i Aj .= The arrival time of entity j. Ij .= The inter-arrival time between passenger j −1 and j. The Aj’s can be written as sums of the ﬁrst j inter-arrival times, which we assumed to be distributed i.i.d. exponential. To ﬁnd the distributions on the S(j) i , we perform kernel density estimation on the given data using Matlab’s ksdensity function for estimation of a density over a positive support.

<!-- b000160 | caption | pages [7] -->
Figure 3: The kernel density estimate of both regular and precheck passenger time

<!-- b000161 | prose | pages [7] -->
spent in service station 1 (ID check) overlaid onto the corresponding histogram.

<!-- b000162 | prose | pages [7, 8] -->
6 Team 56632

<!-- b000164 | furniture | pages [8] -->
Page 7 of 21

<!-- b000165 | caption | pages [8] -->
Figure 4: The kernel density estimate of precheck (left) vs. regular (right) pas-

<!-- b000166 | prose | pages [8] -->
senger time spent in service station 2 (scanning).

<!-- b000167 | prose | pages [8] -->
Assumption 4: Time spent in the scan station is smaller for precheck passengers since they do not need to remove as many personal items.

<!-- b000168 | prose | pages [8] -->
Remark. This is a reasonable assumption, as precheck passengers pay an extra fee in order to exercise this privilege.

<!-- b000169 | prose | pages [8] -->
To ﬁnd the distribution on the time spent in service station 2 (scanning) for precheck passengers, we noted that since they don’t have to remove personal items, the time they spend in the scanning station, Spre is the maximum of the 2 time spent in the mm wave scan and the time spent on luggage scanning. For instance, if the luggage ﬁnishes scanning ﬁrst, then as soon as the passenger exits the mm wave scan, they can immediately pick up their luggage and go.

<!-- b000170 | prose | pages [8] -->
X .= Time spent in the mm wave scan.

<!-- b000171 | prose | pages [8] -->
W .= Time spent scanning a piece of luggage.

<!-- b000172 | prose | pages [8] -->
Y .= 2.26 · W .= max(X, Y ) Spre 2

<!-- b000173 | prose | pages [8] -->
Since the provided data ﬁle reports the times that each piece of luggage exits the scan machine, we must multiply the random variable representing this time by the number of bags that the average passenger carries on. According to the TSA, a passenger brings 2.26 bags on average [10].

<!-- b000174 | prose | pages [8] -->
Assumption 5: X and Y are independent.

<!-- b000175 | prose | pages [8] -->
Remark. This is a reasonable assumption, as scan times for luggage ma- chines and mm wave scan machines don’t inﬂuence each other.

<!-- b000176 | prose | pages [8, 9] -->
7 Team 56632

<!-- b000178 | furniture | pages [9] -->
Page 8 of 21

<!-- b000179 | prose | pages [9] -->
We estimate the distributions on X and Y using kernel density estimation (de- picted in the left plot of Figure 4 by the dotted densities). To obtain the distri- bution on Spre 2 , we write FS(s) .= P(Spre s) 2 = P(max(X, Y ) s) = P(X s, Y s) = FX(s)FY (s)

<!-- b000180 | prose | pages [9] -->
where the last equality follows from independence. Taking the derivative to obtain the density on Spre 2 , we have

<!-- b000181 | prose | pages [9] -->
fS(s) .= d dsFS(s) = fX(s)FY (s) + fY (s)FX(s)

<!-- b000182 | prose | pages [9] -->
This density was computed and plotted as the green curve against the kernel density estimates of fX and fW on the left plot in Figure 4.

<!-- b000183 | heading | pages [9] -->
2.2 Writing Down a Recurrence

<!-- b000184 | heading | pages [9] -->
2.2.1 Deﬁnitions and Derivations

<!-- b000185 | prose | pages [9] -->
We deﬁne the total time spent by passenger n in the system as the sum of time spent in the queues and the service stations.

<!-- b000186 | prose | pages [9] -->
T (n) total = T (n) Q1 + T (n) Q2 + S(n) + S(n) (1) 1 2

<!-- b000187 | prose | pages [9] -->
We deﬁne the wait times in the ﬁrst queue {T (i) Q1}i≥1 recursively. The time that passenger i spends in queue 1 is the time at which they arrive subtracted from the time at which passenger i −1 leaves the ﬁrst service station. The latter quantity can be written as the sum of the following quantities of the previous passenger: arrival time, time spent in line, and time spent getting serviced. This recurrence relation is illustrated below.

<!-- b000188 | prose | pages [9] -->
T (1) Q1 = 0 T (2) Q1 = A1 + T (1) Q1 + S(1) −A2 1 ...

<!-- b000189 | prose | pages [9] -->
Q1 = An−1 + T (n−1) + S(n−1) T (n) −An 1 Q1

<!-- b000190 | prose | pages [9, 10] -->
8 Team 56632

<!-- b000192 | furniture | pages [10] -->
Page 9 of 21

<!-- b000193 | prose | pages [10] -->
Assumption 6: When passengers arrive at either queue, there is always someone in line to wait behind (except in the case of the ﬁrst passenger to arrive).

<!-- b000194 | prose | pages [10] -->
In our deﬁnition for the T (i) Remark. Q1’s, we should be taking the max of the expression displayed above and 0, since we could possibly have Ai > Ai−1 + T (i−1) + S(i−1) passenger i arrives after passenger i −1 , i.e. 1 Q1 leaves the service station. This would lead to a negative waiting time. However, omitting the max operation allows for an explicit solution to the recurrence T (n) Q1 and simpliﬁes calculations immensely. Later on we will remove this assumption.

<!-- b000195 | prose | pages [10] -->
Solving the recurrence, we obtain an explicit form for the time passenger n waits in queue 1,

<!-- b000196 | prose | pages [10] -->
⇣n−1 ⌘ X T (n) S(i) −An + A1 Q1 = 1 i=1

<!-- b000197 | prose | pages [10] -->
Note that An can be written as a sum of interarrival times {Ij}n j=1 distributed i.i.d. exponential(λ), so that the expectation of T (n) Q1 is given by

<!-- b000198 | prose | pages [10] -->
⇣ ⌘ n−1 X E(T (n) S(i) Q1 ) = E A1 −An + 1 i=1 ⇣ ⌘ n−1 n X X S(i) = E A1 − Ii + 1 i=1 i=1 n−1 n X X E(S(i) = λ − λ + 1 ) i=1 i=1 = λ(1 −n) + E(S(1) 1 )(n −1) where the third equality follows from linearity of expectations and since A1 and Ii are distributed exp(λ). Simplifying, we have

<!-- b000199 | prose | pages [10] -->
E(T (n) Q1 ) = (n −1)(E(S(1) 1 ) −λ) (2)

<!-- b000200 | prose | pages [10] -->
Remark. This expression makes sense intuitively since if the expected service time per customer, E(S(1) 1 ), is large relative to time per passenger arrival, λ, then the line will build up, so the expected time spent waiting in the ﬁrst queue grows with n, the number of passengers. We also note an inconsistency in the expression, namely that it can be negative as it is currently written. In reality, time can never be negative. This negativity is a result of Assumption 6, since we don’t take the max of the quantity and 0 in our calculations. This remark is applicable to all boxed equations (5), (6), and (7). Once Assumption 6 is removed in section 3, the times will be strictly non-negative.

<!-- b000201 | prose | pages [10, 11] -->
9 Team 56632

<!-- b000203 | furniture | pages [11] -->
Page 10 of 21

<!-- b000204 | prose | pages [11] -->
Similarly, we can express the time spent waiting in queue 2 recursively, and solve for T (n) Q2 . The process is very similar to that of T (n) Q1 , so we omit the calculations and go straight to the ﬁnal expression.

<!-- b000205 | prose | pages [11] -->
⇣n−1 ⌘ n X X T (n) S(i) T (i) + A1 + S(1) −An −S(n) − Q2 = 2 1 1 Q1 i=1 i=1

<!-- b000206 | prose | pages [11] -->
(d) By the linearity of expectations and since S(1) = S(n) 1 , 1 ⇣n−1 ⌘ n X X E(T (n) E(S(i) E(T (i) 2 ) − + λ(1 −n) Q2 ) = Q1) i=1 i=1

<!-- b000207 | prose | pages [11] -->
Plugging in (2) for E(T (n) Q1 ) and simplifying using the i.i.d. assumption of the S(i) (2)’s, we have ⇣ ⌘ 2 ) −1 E(T (n) E(S(1) 2 · (E(S(1) Q2 ) = (n −1) 1 ) −λ) −λ (3)

<!-- b000208 | prose | pages [11] -->
Thus, the expected total time that passenger i spends in TSA checking is

<!-- b000209 | prose | pages [11] -->
E(T (n) total) = E(T (n) Q1 ) + E(T (n) Q2 ) + E(S(1) 1 ) + E(S(1) 2 ) (4)

<!-- b000210 | prose | pages [11] -->
where E(T (n) Q1 ) and E(T (n) Q2 ) are given by (2) and (3).

<!-- b000211 | heading | pages [11] -->
2.2.2 Average Wait Time Values

<!-- b000212 | prose | pages [11] -->
To compute the average time that any passenger spends waiting in queue 1, T avg Q1 , we take the average of the waiting times. This will yield an expression in terms of the T (i) Q1’s, which are random variables. We then take the expectation to obtain the average time spent in the queue.

<!-- b000213 | prose | pages [11] -->
⌘ n X ⇣1 .= E T (i) T avg Q1 Q1 n i=1 n X = 1 (i −1)(E(S(1) 1 ) −λ) n i=1

<!-- b000214 | prose | pages [11] -->
where the last equality follows from (2). Simplifying, we have

<!-- b000215 | prose | pages [11] -->
Q1 = n −1 (E(S(1) T avg 1 ) −λ) (5) 2

<!-- b000216 | prose | pages [11] -->
A similar calculation that yielded average wait time for queue 1 will give

<!-- b000217 | prose | pages [11] -->
Q2 = n −1 2 ) −1 1 ) −1 · (E(S(1) 2E(S(1) T avg 2λ) (6) 2

<!-- b000218 | prose | pages [11, 12] -->
10 Team 56632

<!-- b000220 | furniture | pages [12] -->
Page 11 of 21

<!-- b000221 | prose | pages [12] -->
To ﬁnd the average total waiting time, we combine the average waiting times (5) and (6) with expression (1).

<!-- b000222 | prose | pages [12] -->
Q2 + E(S(1) 1 ) + E(S(1) T avg total = T avg Q1 + T avg 2 ) (7)

<!-- b000223 | prose | pages [12] -->
We compute the boxed expressions (5), (6), and (7) to compare with the simula- tion in the following section. This will serve to validate our method of simulation.

<!-- b000224 | heading | pages [12] -->
3 The Simulation

<!-- b000225 | heading | pages [12] -->
3.1 A Dynamic Programming Method

<!-- b000226 | prose | pages [12] -->
In the previous section, assumptions on the number of ID check and scan stations were made in order to simplify calculations. As a result we were able to obtain explicit formulas. In the following section we no longer make this simplifying assumption and instead denote c .= Number of service spots at check stations k .= Number of service spots at scan stations n .= Number of passengers

<!-- b000227 | prose | pages [12] -->
We denote the number of passengers by n even though our model isn’t restricted to any ﬁnite number of passengers. For the sake of the simulation, we sample for n passengers, where n can be made arbitrarily large.

<!-- b000228 | prose | pages [12] -->
Every passenger has an arrival time, a start/end time for the ID checking process, and a start/end time for the scanning process. Since our expression for these times is recursive, we take a dynamic programming approach to ﬁll out a 2-D array, whose rows represent time events and whose columns represent passengers.

<!-- b000229 | prose | pages [12] -->
Since inter-arrival times are distributed i.i.d. exponential(λ), we simulate arrival times by keeping a running sum of i.i.d. exponential random variables. Since there are c spots for ID checking, we inspect the ID check leaving times of the previous c passengers to determine which is most readily available. If the arrival time of the current passenger exceeds this quantity, then the passenger can directly enter one of the ID check spots. Otherwise they must wait until a spot opens up. The start time for the scan process is computed similarly using k, the number of scan stations, in place of c. The end times for both service stations are computed by sampling from the kernel density estimates for the service times and adding these to the start times.

<!-- b000230 | prose | pages [12] -->
To compute the average waiting times, we take the di↵erence between service start times and the times at which passengers start waiting, which is either their

<!-- b000231 | prose | pages [12, 13] -->
11 Team 56632

<!-- b000233 | furniture | pages [13] -->
Page 12 of 21

<!-- b000234 | prose | pages [13] -->
arrival time or their ID check end time depending on the service for which they are in queue. We then take the average over all passengers and return this result. A more concise set of instructions is given below as pseudo code.

<!-- b000235 | heading | pages [13] -->
3.1.1 Pseudo code

<!-- b000236 | heading | pages [13] -->
Algorithm 1 TSA Security Simulation

<!-- b000237 | prose | pages [13] -->
Result: a vector representing the average time spent in queues and the entire system.

<!-- b000238 | prose | pages [13] -->
First, initialize a two dimensional array with 5 rows and max(c, k) + n columns. Each row represents either passenger arrival time, time entering check station, time exiting check station, time entering scan station, or time exiting scan station (ﬁnished).

<!-- b000239 | prose | pages [13] -->
for i 2 {max(c, k), . . . , n} do Arrival(i) = Arrival(i−1) + sampleexp(λ) start = max(Arrival(i), min(Check(i−c) end , . . . , Check(i−1) Check(i) end )) Check(i) end = Check(i) start + sampleid check end, min(Scan(i−k) end , . . . , Scan(i−1) Scan(i) start = max(Check(i) end )) Scan(i) end = Scan(i) start + samplescan end

<!-- b000240 | prose | pages [13] -->
T avg Q1 = 1 n · sum(Checkstart −Arrival) T avg Q2 = 1 n · sum(Scanstart −Checkend) T avg Total = 1 n · sum(Scanend −Arrival) return (T avg Q1 , T avg Q2 , T avg Total)

<!-- b000241 | heading | pages [13] -->
3.2 Comparison to the Model

<!-- b000242 | prose | pages [13] -->
We implemented the simulation described above in Matlab and compared the simulated average waiting times with their explicit formulas which were derived in the previous section, namely, expressions (3), (6), and (7).

<!-- b000243 | prose | pages [13, 14] -->
12 Team 56632

<!-- b000245 | furniture | pages [14] -->
Page 13 of 21

<!-- b000246 | caption | pages [14] -->
Figure 5: Plot of the average time spent in queues 1 (left) and 2 (right). Simulated

<!-- b000247 | prose | pages [14] -->
and theoretical time averages are depicted in blue and orange respectively.

<!-- b000248 | caption | pages [14] -->
Figure 5 shows the calculated results from our model against the simulated results.

<!-- b000249 | prose | pages [14] -->
It appears that they follow the same trend on average as the number of passengers increases from 50 to 4050. As a result, we are more inclined to believe the results obtained from using our simulation in the proceeding experiments. The simulation also seems to vary from the theoretical results more drastically in the waiting time for queue 1. However, looking at the scale on which these waiting times are plotted, we reason that we see this relatively large variance because the waiting times for queue 1 are much smaller in magnitude than those for queue 2. The plot of simulated versus theoretical values for total time spent in the system is omitted since it is essentially the sum of the above two plots and as a result, follows the same trend.

<!-- b000250 | heading | pages [14] -->
4 Evaluation/Results

<!-- b000251 | heading | pages [14] -->
4.1 Bottlenecks in Passenger Throughput

<!-- b000252 | prose | pages [14] -->
From our model we identiﬁed two major bottlenecks in the ﬂow of passengers through airport security: ID check stations and scan stations. Through simulation we investigated how the number of service spots at each station a↵ects the total time a passenger waits.

<!-- b000253 | heading | pages [14] -->
4.1.1 ID Check Station

<!-- b000254 | prose | pages [14] -->
The ﬁrst bottleneck a passenger experiences upon reaching airport security is the ID check station. Both TSA precheck and regular passengers receive service at the same rate from this station and therefore, when investigating this bottleneck we considered only one service distribution. However, TSA precheck and regular

<!-- b000255 | prose | pages [14, 15] -->
13 Team 56632

<!-- b000257 | furniture | pages [15] -->
Page 14 of 21

<!-- b000258 | prose | pages [15] -->
passengers arrive at di↵erent rates to this station, so we investigated how varying arrival rates and the number of check stations would a↵ect the wait time in the checking queue. The results from our simulation can be seen below.

<!-- b000259 | caption | pages [15] -->
Figure 6: Plot of wait time spent in ID check queue for various values of c (left)

<!-- b000260 | prose | pages [15] -->
and k (right).

<!-- b000261 | prose | pages [15] -->
The average wait time of a passenger in the checking queue appears to be inde- pendent of the number of scanning stations, k, an intuitive result. However, there is a clear relationship between the number of open spots at the ID check station, c, and the average wait time of a passenger in the ID check queue. The wait time undergoes a signiﬁcant transition, decreasing drastically, as the arrival rate of passengers slows (λ increases). Using the queuing model described previously, the λ value at which this transition takes place can be estimated by the following relation.

<!-- b000262 | prose | pages [15] -->
λ = E(S(i) 1 ) (8) c

<!-- b000263 | prose | pages [15] -->
Remark. This relation can be understood as the condition for when the average arrival rate (λ) is equal to the average service rate (E(S(i) 1 )/c). When passengers arrive faster than they are being serviced at the ID check stations, a queue forms, causing a bottle neck on passenger throughput. Conversely, when passengers are serviced more quickly than they arrive, a queue becomes less likely to form. In the case of c = 1, this is equivalent to setting the expected waiting time in Q1 given by (2) equal to 0.

<!-- b000264 | prose | pages [15] -->
The estimated λ transition values given by (8) are plotted as vertical lines on the same plot in Figure 6. One can see that these points correspond very closely to the observed transitions from our simulation.

<!-- b000265 | prose | pages [15, 16] -->
14 Team 56632

<!-- b000267 | furniture | pages [16] -->
Page 15 of 21

<!-- b000268 | heading | pages [16] -->
4.1.2 Scan Station

<!-- b000269 | prose | pages [16] -->
The second bottleneck a passenger will experience in airport security is the scan station. We conducted an analysis similar to the one we performed on the ﬁrst bottleneck. Unlike the ID check station, TSA precheck and regular passengers experience di↵erent service rates at this station; however, the general trend re- mains the same. The results from our simulation of regular passengers can be seen below.

<!-- b000270 | caption | pages [16] -->
Figure 7: Plot of average time spent in the regular scan queue with varying arrival

<!-- b000271 | prose | pages [16] -->
rates for various values of c (left) and k (right).

<!-- b000272 | prose | pages [16] -->
The average wait time of a passenger in the scanning station is dependent on both c and k. We observe that the concept of λ transition values, discussed above in the ﬁrst bottleneck, are important as they mark signiﬁcant transitions in T (n) Q2 , where the analogous values are given by

<!-- b000273 | prose | pages [16] -->
λ = E(S(i) 2 ) (9) c

<!-- b000274 | heading | pages [16] -->
4.2 Variance in Passenger Wait Time

<!-- b000275 | prose | pages [16] -->
Increasing passenger throughput and decreasing wait times is only part of the story when it comes to improving airport security. Equally important is reducing the variance in passenger wait times to ensure that passengers know generally how long security lines will be. Using our simulation, we investigated how the number of check stations (c) and scan stations (k) a↵ected the variance of passenger wait times in queues. We found that the number of check stations had a larger a↵ect on the variance of wait times in both queues than the number of scan stations.

<!-- b000276 | prose | pages [16, 17] -->
15 Team 56632

<!-- b000278 | furniture | pages [17] -->
Page 16 of 21

<!-- b000279 | caption | pages [17] -->
Figure 8: Plot of variance of passenger wait times spent in check station queue

<!-- b000280 | prose | pages [17] -->
(left) and scan station queue (right) for various values of c and constant k = 1.

<!-- b000281 | prose | pages [17] -->
As seen in the plots above, the variance in passenger wait times spent in either queue decreases as arrival rate increases. Major transitions occur at the same λ transition values given by (8).

<!-- b000282 | heading | pages [17] -->
4.3 Modiﬁcations to the Model

<!-- b000283 | heading | pages [17] -->
4.3.1 Cost-Beneﬁt Analysis

<!-- b000284 | prose | pages [17] -->
In this section we confront the optimization problem of balancing the cost of employing TSA workers with the beneﬁt of increasing passenger ﬂow. Following the events of September 11, TSA began to include a $6.60 security fee per one- way-trip in the year 2017 [3]. The fee goes to funding the TSA’s airport security measures. In other words, increasing passenger throughput while limiting secu- rity costs can be proﬁtable for TSA. In order to investigate this relationship, we describe an objective function for TSA proﬁt using the following variables.

<!-- b000285 | prose | pages [17] -->
Cp .= September 11 fee per one-way-trip Ct .= The cost of a Transportation Security Oﬃcer (TSO). Ttotal .= Average time spent from entering to leaving the system.

<!-- b000286 | prose | pages [17] -->
Remark. In the ATL Hartsﬁeld-Jackson airport, a TSO makes on average 18.5 dollars an hour. Converting this salary into units relevant to our calculations, the average TSO makes 0.0005139 dollars per second [9]. In addition, we assume that 1 TSO is required to operate an ID check station, and that 3 TSOs are required to operate a scan station: one for the mm wave scan, one for the X-Ray, and one for auxiliary help.

<!-- b000287 | prose | pages [17, 18] -->
16 Team 56632

<!-- b000289 | furniture | pages [18] -->
Page 17 of 21

<!-- b000290 | prose | pages [18] -->
Assumption 7: The only cost for running a TSA security check point is to employ TSA workers.

<!-- b000291 | prose | pages [18] -->
Remark. There are other costs including management, machine mainte- nance, and training of TSOs, but these costs per employee are marginal compared to employee salary.

<!-- b000292 | prose | pages [18] -->
Finally, we deﬁne TSA proﬁt rate, P, as the di↵erence in the rate at which TSA gains money through the September 11 fee and the rate at which TSA loses money by staﬃng employees. Combining the terms deﬁned above in this way yields a measure of proﬁt, P, whose units are dollars per second.

<!-- b000293 | prose | pages [18] -->
Cp −(c + 3k) · Ct P = Ttotal

<!-- b000294 | prose | pages [18] -->
As in section 3, c and k refer to the number of spots at ID check stations and scan stations, respectively. We wish to ﬁnd the parameters c and k which maximize this objective function. Using the dynamic programming approach described in section 3, we sample values for Ttotal, compute P for di↵erent values of c and k, and plot the resulting heat maps below.

<!-- b000295 | caption | pages [18] -->
Figure 9: Proﬁt as a function of the number of ID check and scan stations for

<!-- b000296 | prose | pages [18] -->
TSA precheck (left) and Regular passengers (right).

<!-- b000297 | prose | pages [18] -->
For the TSA precheck line, the most cost-eﬃcient layout is to have 3 checking stations and 3 scanning stations to achieve a rate of P = 0.140 dollars per second. For the regular security line, the most cost-eﬃcient layout is to have 2 checking stations and 3 scanning stations, yielding a proﬁt rate of P = 0.083 dollars per second. TSA precheck gives the TSA a 68.6% gain in revenue per passenger compared to regular screening.

<!-- b000298 | prose | pages [18, 19] -->
17 Team 56632

<!-- b000300 | furniture | pages [19] -->
Page 18 of 21

<!-- b000301 | heading | pages [19] -->
4.3.2 Sensitivity Analysis

<!-- b000302 | prose | pages [19] -->
Our other modiﬁcation is the introduction of virtual queuing, a method ﬁrst implemented in call centers for minimizing perceived wait times [7]. After a passenger checks in for their ﬂight, the airline assigns them an arrival time and a window around this time to enter the security process. The assigned boarding time instructs the passenger when to arrive at the ﬁrst queue. The passenger now has more free time to shop at airport businesses instead of physically waiting in line. Virtual queuing not only allows for the reduction in perceived wait time but also for the implementation of non-FIFO disciplines.

<!-- b000303 | prose | pages [19] -->
We distinguish between two types of travelers: slow and fast (inexperienced and experienced), whose service times are multiplied by a predetermined factor. We deﬁne a new discipline, Priority, to describe the use of the virtual queue to group passengers of similar experience levels together, so that all slow passengers go ﬁrst, followed by the quick passengers. This is done in contrast to the previous discipline, in which passengers of varying speeds arrive randomly.

<!-- b000304 | caption | pages [19] -->
Figure 10: Plots of time (left) and variance (right) versus the fraction of fast

<!-- b000305 | prose | pages [19] -->
passengers for the Priority (orange) and FIFO disciplines (blue).

<!-- b000306 | prose | pages [19] -->
In Figure 10, we plot wait time vs. the fraction of slow passengers. Contrary to our initial hypotheses, the Priority discipline generally led to both longer average total wait time and higher variance. A possible explanation is that if slow people go ﬁrst, they cause fast passengers to wait longer in line, increasing the average overall time waiting.

<!-- b000307 | prose | pages [19] -->
In reality, inexperienced travelers (slow) are more likely to come early as they are new to the security process while experienced travelers (fast) are likely to come late. Thus, they will naturally group up into something similar to the conditions of our Priority discipline simulation. Because our simulations suggest that this decreases passenger throughput, airports can use virtual queuing and new disci- plines to ensure a more uniform distribution of passengers to avoid bottlenecks.

<!-- b000308 | prose | pages [19, 20] -->
18 Team 56632

<!-- b000310 | furniture | pages [20] -->
Page 19 of 21

<!-- b000311 | heading | pages [20] -->
5 Improving the Model

<!-- b000312 | heading | pages [20] -->
5.1 Traveler Characteristics

<!-- b000313 | prose | pages [20] -->
In our model and modiﬁcations, we only account for travelers we deem slow and fast based on traveling experience. However, we can get more nuanced results by creating a system to proﬁle people based on a variety of features like age, walking speed, families, etc. Perhaps there would be an optimal solution in creating di↵erent lanes designed for di↵erent types of travelers.

<!-- b000314 | heading | pages [20] -->
5.2 Di↵erent Queuing Disciplines

<!-- b000315 | prose | pages [20] -->
We only considered the FIFO and Priority disciplines for our simulation. We can further explore new disciplines and ways of organizing passenger populations. These disciplines could possibly lead to more e↵ective virtual queuing.

<!-- b000316 | heading | pages [20] -->
5.3 Arrival Rate Regulation

<!-- b000317 | prose | pages [20] -->
Due to the nature of airport scheduling, it is unlikely that arrival rates follow a consistent Poisson distribution throughout the course of a day [2]. Virtual queuing gives us greater control over the arrival rate (λ) variation, because we set the passenger arrival times. In our simulations we show that total wait time and its variance is largely characterized by the ﬂuctuation in λ. Therefore, we can explore methods to regulate the arrival rate while ensuring all passengers make their ﬂight.

<!-- b000318 | heading | pages [20] -->
5.4 Improving Proﬁt Measure

<!-- b000319 | prose | pages [20] -->
There were many sources of cost and revenue which were not included in the construction of our proﬁt measure. Some examples are machine maintenance, employee management, and variance in passenger wait times.

<!-- b000320 | heading | pages [20] -->
6 Conclusion

<!-- b000321 | prose | pages [20] -->
Our solution to the problem of excessive waiting times in airport security re- quired the use of a diverse collection of techniques from the ﬁelds of statistics and computer science. The uncertainty in the dynamics of the TSA security check were described by a queuing network and simulated with the use of dy- namic programming. The results of our simulations helped to indicate an optimal

<!-- b000322 | prose | pages [20, 21] -->
19 Team 56632

<!-- b000324 | furniture | pages [21] -->
Page 20 of 21

<!-- b000325 | prose | pages [21] -->
number of security oﬃcers to employ in order to maximize proﬁt rate, while the sensitivity analysis hinted that our initial intuitions about line ordering based on passenger experience were ﬂawed. We further identiﬁed where we could make our model more powerful by considering things such as traveler characteristics, cre- ative queuing disciplines, and arrival time regulation. The real world continues to present all sorts of interesting problems for mankind to think about and develop mathematical tools to solve. Our attempt to gain insight into this problem closely follows this narrative, illustrating and verifying the importance of bringing theory to application and curiosity to exploration.

<!-- b000326 | prose | pages [21, 22] -->
20 Team 56632

<!-- b000328 | furniture | pages [22] -->
Page 21 of 21

<!-- b000329 | heading | pages [22] -->
References

<!-- b000330 | references | pages [22] -->
[1] Chen, Hong, David D. Yao. “Fundamentals of Queuing Networks: Perfor-

<!-- b000331 | references | pages [22] -->
mance, Asymptotics, and Optimization.” New York: Springer, 2001. Print.

<!-- b000332 | references | pages [22] -->
[2] Dorton, Stephen L. ”Analysis of Airport Security Screening Checkpoints using

<!-- b000333 | references | pages [22] -->
Queuing Networks and Discrete Event Simulation: A Theoretical and Empir-

<!-- b000334 | references | pages [22] -->
ical Approach.” Embry-Riddle Scholarly Commons (2011): n. pag. Embry-

<!-- b000335 | references | pages [22] -->
Riddle Aeronautical Unviersity, 2011. Web.

<!-- b000336 | references | pages [22] -->
[3] Gillen, David, William G. Morrison. “Aviation security: Costing, pricing,

<!-- b000337 | references | pages [22] -->
ﬁnance and performance.” Journal of Air Transport Management 48 (2015):

<!-- b000338 | references | pages [22] -->
1-12. Web. 21 Jan. 2017.

<!-- b000339 | references | pages [22] -->
[4] Bowman, A. W., Adelchi Azzalini. “Applied smoothing techniques for data

<!-- b000340 | references | pages [22] -->
analysis: the kernel approach with S-Plus illustrations.” Oxford: Clarendon

<!-- b000341 | references | pages [22] -->
Press, 1997. Print.

<!-- b000342 | references | pages [22] -->
[5] Casella, George, and Roger L. Berger. “Statistical inference.” Australia:

<!-- b000343 | references | pages [22] -->
Thomson Learning, 2002. Print.

<!-- b000344 | references | pages [22] -->
[6] Jacobson, Sheldon H., Arash Khatibi, Ge Yu. “When should TSA PreCheck

<!-- b000345 | references | pages [22] -->
be o↵ered at no cost to travelers?” Journal of Transportation Security (2016):

<!-- b000346 | references | pages [22] -->
1-7. Web. 21 Jan. 2017.

<!-- b000347 | references | pages [22] -->
[7] Lange, Robert De, Ilya Samoilovich, Bo Van Der Rhee. “Virtual queuing at air-

<!-- b000348 | references | pages [22] -->
port security lanes.” European Journal of Operational Research 225.1 (2013):

<!-- b000349 | references | pages [22] -->
153-65. Web. 21 Jan. 2017.

<!-- b000350 | references | pages [22] -->
[8] TranSafety. “Study Compares Older and Younger Pedestrian Walking

<!-- b000351 | references | pages [22] -->
Speeds.” USRoads. N.p., n.d. Web. 22 Jan. 2017.

<!-- b000352 | references | pages [22] -->
[9] “Transportation Security Oﬃcer (TSO) Job O↵ering.” USAJOBS. Trans-

<!-- b000353 | references | pages [22] -->
portation Security Administration, n.d. Web. 21 Jan. 2017.

<!-- b000354 | references | pages [22] -->
[10] “TSA releases 2015 statistics.” Transportation Security Administration. De-

<!-- b000355 | references | pages [22] -->
partment of Homeland Security, 21 Jan. 2016. Web. 21 Jan. 2017.

<!-- b000356 | references | pages [22] -->
21
