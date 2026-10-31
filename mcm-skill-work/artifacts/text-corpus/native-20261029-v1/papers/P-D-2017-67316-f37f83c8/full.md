# P-D-2017-67316-f37f83c8

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
67316

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


<!-- b000018 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000019 | heading | pages [1] -->
Summary Sheet

<!-- b000020 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000021 | heading | pages [1] -->
Summary

<!-- b000022 | prose | pages [1] -->
Bottlenecks that passengers take time to take care of their carry-on properties before X-ray scanning and that the structure of the checkpoints is not satisfying are spotted, and detailed recommendations for the airport security management to raise throughput of the security checkpoints, to improve the passengers’ satisfaction and to keep the cost relatively low are given with cultural factors quantiﬁed and their impacts on the models discussed.

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | prose | pages [1] -->
We divided the security check process into two phases and regard the entire as two Poisson queueing (𝑀𝑀/𝑀𝑀/𝑐𝑐) in Kendall notation, and Erlangian process (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐) is concerned queueing models in series. By analyzing the given data, the document check is found to be a in the scan check process. Numeric solution of (𝑴𝑴/𝑬𝑬𝒌𝒌/𝒄𝒄) is introduced using simulation tech- nique.

<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | prose | pages [1] -->
Assumed that arrivals of passengers for a ﬂight obey normal distribution, the varying ulation. We also believe that the mean 𝜇𝜇 and the variance 𝜎𝜎􏷡􏷡 of the distribution is culture-re- passenger ﬂow in a period of time can be generated from the real data and used for our sim-

<!-- b000027 | prose | pages [1] -->
lated. We also ﬁnd that the passenger ﬂow can be changed by recommending the passengers their arrivals, and thus better result of the passengers’ waiting time can be achieved.

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | prose | pages [1] -->
We also suggested several methods to improve the design of the checkpoint, including shortening the distances between identical checkpoints and more rational human resource allocation.

<!-- b000030 | furniture | pages [1] -->


<!-- b000031 | prose | pages [1] -->
Virtual queueing is recommended as an approach to improve passengers’ experience, and modify the conventional First In First Service queueing discipline to partial priority queueing discipline as well. A partial priority queueing discipline is put forward to reduce the remaining time variance of the passengers and to decrease the number of passengers that missed their ﬂights, thus better passenger satisfaction is reached. ority queueing discipline. For the latter, an “acceptability factor” named 𝛼𝛼 is used to denote

<!-- b000032 | furniture | pages [1] -->


<!-- b000033 | prose | pages [1] -->
We also introduced culture-related factors for passenger arrival recommendation and pri-

<!-- b000034 | prose | pages [1] -->
the acceptability of strict priority discipline. And the examples of diﬀerent cultures are given to illustrate this idea.

<!-- b000035 | furniture | pages [1] -->


<!-- b000036 | prose | pages [1] -->
Validation of each model are made in our essay to make them convincing. We later assess the models and give a complete guide for the security managers to optimize the airport secu- rity check workﬂow. Weaknesses and further work that is not implemented in our essay are also pointed out.

<!-- b000037 | furniture | pages [2] -->
Team #67316

<!-- b000038 | furniture | pages [2] -->
Page 1 of 20

<!-- b000039 | prose | pages [2] -->
Time Counts! Less Waiting & Better Airports

<!-- b000040 | heading | pages [2] -->
Introduction

<!-- b000041 | furniture | pages [2] -->


<!-- b000042 | heading | pages [2] -->
1.1 Background

<!-- b000043 | prose | pages [2] -->
Airport security check has been improved ever since the 911 attack. Although enhanced secu- rity means safer ﬂights, however the complicated procedure may also increase the passengers’ waiting time and add cost to the U.S. Transportation Security Agency (TSA). Under some extreme circumstances, passengers have to wait for hours (and they are often recommended to be earlier for 2–3 hours, which often lead to confusion) (Hetter, 2016). Thus, to shorten the passengers’ waiting and designing a more eﬃcient security check procedure is vitally important.

<!-- b000044 | furniture | pages [2] -->


<!-- b000045 | prose | pages [2] -->
TSA is now in controversy for causing long queues waiting for security check. We, the Internal Control Management (ICM) team, trying to ﬁnd a solution, faces the problems below:

<!-- b000046 | prose | pages [2] -->
1. Identify the bottlenecks of the current security check workﬂow. 2. Improve the process with modiﬁcations, and illustrate how the modiﬁcations work. 3. Find how to allow the modiﬁed process to be compatible with diﬀerent culture back- grounds and lower the variance of the passengers’ waiting time. 4. Make suggestions on the policy for the security manager, with concern of the former requirements and corresponding models.

<!-- b000047 | heading | pages [2] -->
1.2 Analysis and Approach Overview

<!-- b000048 | prose | pages [2] -->
For problem 1, we divide the security check process in two parts: Phase 1, document check; and Phase 2, luggage and body scanning. The former is a Poisson queue, while the latter concerns an Erlangian model. Simulation is practiced as a means of solving multi-server Er- langian model. By testing the total waiting time’s sensitivity to changes on numbers of parallel servers in the two phases respectively, the bottlenecks of the workﬂow can be spotted.

<!-- b000049 | furniture | pages [2] -->


<!-- b000050 | prose | pages [2] -->
To solve problem 2, considering the inﬂuential factors of a queueing process, modiﬁcations will be put forward to optimize and avoid congestions.

<!-- b000051 | furniture | pages [2] -->


<!-- b000052 | prose | pages [2] -->
The current TSA recommended passengers’ arrival time is used to build a model of the passenger arrival behavior at an airport, and we assume the arrivals in time for one certain ﬂight obey normal distribution, and in a small time interval, the arrivals of all passengers for all ﬂights obey an exponential distribution. We will modify the arrival recommendation strat- egy to inﬂuence passengers’ arrival behavior.

<!-- b000053 | furniture | pages [2] -->


<!-- b000054 | prose | pages [2] -->
Another direction to improve the current process is to provide more robust security check service with greater capacity. A few suggestions and their veriﬁcation or explanation will be given.

<!-- b000055 | furniture | pages [2] -->


<!-- b000056 | furniture | pages [2] -->


<!-- b000057 | furniture | pages [3] -->
Team #67316

<!-- b000058 | furniture | pages [3] -->
Page 2 of 20

<!-- b000059 | furniture | pages [3] -->


<!-- b000060 | prose | pages [3] -->
Besides the performance, justiﬁability also counts. Virtual queueing under other disciplines (Zhao, et al., 2016) will be a good practice. Queueing discipline modiﬁcation is culture-sensitive, and thus lead to the discussion of the third problem.

<!-- b000061 | furniture | pages [3] -->


<!-- b000062 | prose | pages [3] -->
The following diagram illustrate the above ideas in a more visual way:

<!-- b000063 | furniture | pages [3] -->


<!-- b000064 | caption | pages [3] -->
Figure 1 Optimizing directions and our modiﬁcations,

<!-- b000065 | prose | pages [3] -->
where “service pattern” concerns the service rate and number of servers.

<!-- b000066 | heading | pages [3] -->
Assumptions

<!-- b000067 | furniture | pages [3] -->


<!-- b000068 | prose | pages [3] -->
1. Individual variability is not considered for the servers, the checkpoint structures, etc. 2. Although the number of lanes opened in the scan check process is dynamic, we assume that the service capability is always at its maximum. That is to say, spare lanes will be open, so long as the arrival exceeds the current capability. 3. Assume that every passenger will choose to wait in the queue that minimizes their waiting time at every checkpoint. 4. Points in time that passengers arrive at the airport for a certain ﬂight obey normal distribution. 5. TSA Pre-check won’t contribute much to the congestion compared with the normal one. 6. Almost everyone would arrive at the airport for at least half an hour.

<!-- b000069 | furniture | pages [3] -->


<!-- b000070 | prose | pages [3] -->
See 4.1 Security Check Process—Overview, and 4.3 Queueing Model Speciﬁcation for de- tailed interpretation and assumptions of the given datasheet.

<!-- b000071 | heading | pages [3] -->
Symbols and Notations

<!-- b000072 | furniture | pages [3] -->


<!-- b000073 | heading | pages [3] -->
Symbol or Notation

<!-- b000074 | prose | pages [3] -->
Speciﬁcation

<!-- b000075 | prose | pages [3] -->
Kendall notation, where 𝑎𝑎, 𝑏𝑏, 𝑐𝑐, 𝑑𝑑, 𝑒𝑒  and 𝑓𝑓  denote the inter-arrival-time (𝑎𝑎/𝑏𝑏/𝑐𝑐): (𝑑𝑑/𝑒𝑒/𝑓𝑓) distribution, the service time distribution, the number of parallel servers,

<!-- b000076 | furniture | pages [3] -->


<!-- b000077 | furniture | pages [3] -->


<!-- b000078 | furniture | pages [4] -->
Team #67316

<!-- b000079 | furniture | pages [4] -->
Page 3 of 20

<!-- b000080 | prose | pages [4] -->
queueing discipline, restriction on system capacity, and the source of the arrival (usually inﬁnity) respectively. (Taha, 2014)

<!-- b000081 | prose | pages [4] -->
Denote an exponential distribution for inter-arrival time and service time, 𝑀𝑀 i.e. a Poisson distribution for arrival and remove rate. 𝐸𝐸𝑘𝑘 Erlang distribution type 𝑘𝑘. 𝑥𝑥̂ Estimated value of 𝑥𝑥. 𝜆𝜆𝑑𝑑, 𝜇𝜇𝑑𝑑 Arrival and service rates of the document check process. 𝜆𝜆𝑠𝑠, 𝜇𝜇𝑠𝑠 Arrival and service rates of the scan check process.

<!-- b000082 | prose | pages [4] -->
Γ(𝛼𝛼)

<!-- b000083 | prose | pages [4] -->
𝑁𝑁(𝜇𝜇, 𝜎𝜎2)

<!-- b000084 | prose | pages [4] -->
∞

<!-- b000085 | furniture | pages [4] -->


<!-- b000086 | prose | pages [4] -->
Γ(𝛼𝛼) =  𝑥𝑥𝛼𝛼−1e−𝑥𝑥d𝑥𝑥

<!-- b000087 | prose | pages [4] -->
0

<!-- b000088 | prose | pages [4] -->
Normal distribution with mean 𝜇𝜇, and variance 𝜎𝜎2.

<!-- b000089 | heading | pages [4] -->
Queueing Model for Security Check Process

<!-- b000090 | furniture | pages [4] -->


<!-- b000091 | heading | pages [4] -->
4.1 Security Check Process------Overview

<!-- b000092 | furniture | pages [4] -->


<!-- b000093 | caption | pages [4] -->
Figure 2 TSA Security checkpoint

<!-- b000094 | prose | pages [4] -->
The detailed security check process of one single checkpoint given in the diagram above. Ac- cording to TSA’s policy, we classify the security processes in two types (pre-check included and no pre-check concerned process), and divide the each process in two queueing phases. In Phase 1, the passengers’ identity documents will be checked, after which they enter Phase 2, where luggage and body screening will be accepted. Two diﬀerent types are in essence the same queueing with diﬀerent parameters (number of servers, service time, etc.). And the entire security check process can be seen as two queueing models in series.

<!-- b000095 | prose | pages [4] -->
To better clarify the whole process, a procedure sequence diagram is given below:

<!-- b000096 | furniture | pages [4] -->


<!-- b000097 | furniture | pages [4] -->


<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | furniture | pages [5] -->
Team #67316

<!-- b000100 | prose | pages [5] -->
A B C

<!-- b000101 | furniture | pages [5] -->
Page 4 of 20

<!-- b000102 | prose | pages [5] -->
D E

<!-- b000103 | prose | pages [5] -->
F G H

<!-- b000104 | furniture | pages [5] -->


<!-- b000105 | caption | pages [5] -->
Figure 3 Procedure sequence diagram

<!-- b000106 | prose | pages [5] -->
A: time waiting for the document check, B: document checking time C: time waiting for sending luggage for X-ray scanning, D: X-ray scanning time, E: other possible luggage checks

<!-- b000107 | prose | pages [5] -->
F: time waiting for millimeter wave scan, G: body scan time, H: other possible body checks The yellow shaded part is Phase 1 as we introduced in previous paragraphs, and the rest Phase 2.

<!-- b000108 | prose | pages [5] -->
The given Excel datasheet contains time records of the airport checkpoints (whose diﬀer-

<!-- b000109 | furniture | pages [5] -->


<!-- b000110 | prose | pages [5] -->
ences denote the inter-arrival time), time taken of the ID check process of previous checked passenger (i.e. B in the diagram), millimeter wave scan timestamps (diﬀerences of which are the millimeter wave scanning time, shown as G in the diagram), timestamps that luggage getting out of the X-ray scan (diﬀerences denote E), and time to get scanned property (D, E, F, G, H).

<!-- b000111 | prose | pages [5] -->
By analyzing the given datasheet, patterns of the airport security check behaviors, such as

<!-- b000112 | furniture | pages [5] -->


<!-- b000113 | prose | pages [5] -->
the distribution of passengers’ inter-arrival time and service time at each section, can be dis- covered. Therefore a complete queueing model can be speciﬁed.

<!-- b000114 | heading | pages [5] -->
4.2 Significance Test on Two TSA Officers

<!-- b000115 | prose | pages [5] -->
The given datasheet involves timing of two diﬀerent TSA oﬃcers, the signiﬁcance test here is to verify that individual variability does not contribute much to the service time.

<!-- b000116 | prose | pages [5] -->
2 = 𝜎𝜎2 2 = 𝜎𝜎2.

<!-- b000117 | prose | pages [5] -->
Suppose that variances of the service time of the two TSA oﬃcers are equal, 𝜎𝜎1

<!-- b000118 | furniture | pages [5] -->


<!-- b000119 | prose | pages [5] -->
We make the null hypothesis 𝐻𝐻0 that service time expectations of both oﬃcers are the same,

<!-- b000120 | furniture | pages [5] -->


<!-- b000121 | prose | pages [5] -->
i.e. 𝜇𝜇1 = 𝜇𝜇2.

<!-- b000122 | prose | pages [5] -->
2 = 12.927.

<!-- b000123 | prose | pages [5] -->
The combined sample variance of the two oﬃcers, 𝑠𝑠𝑤𝑤

<!-- b000124 | furniture | pages [5] -->


<!-- b000125 | prose | pages [5] -->
𝑠𝑠𝑤𝑤 1/𝑛𝑛1+1/𝑛𝑛2 = 1.375 ≤𝑡𝑡0.025(14) = 2.145, the null hypothesis is not rejected.

<!-- b000126 | furniture | pages [5] -->


<!-- b000127 | prose | pages [5] -->
At 5% level, |𝑥𝑥1 −𝑥𝑥2 |

<!-- b000128 | prose | pages [5] -->
Assume that the document check service time obeys the exponential distribution. The pa-

<!-- b000129 | furniture | pages [5] -->


<!-- b000130 | prose | pages [5] -->
rameter of the distribution, i.e. service rate, is estimated, 𝜇𝜇𝑑𝑑

<!-- b000131 | heading | pages [5] -->
4.3 Queueing Model Specification

<!-- b000132 | prose | pages [5] -->
= 0.09465.

<!-- b000133 | prose | pages [5] -->
The two phases of the process can be speciﬁed as a series of queues by giving the arrival and service time distribution pattern.

<!-- b000134 | furniture | pages [5] -->


<!-- b000135 | furniture | pages [5] -->


<!-- b000136 | furniture | pages [6] -->
Team #67316

<!-- b000137 | prose | pages [6] -->
4.3.1 Arrival

<!-- b000138 | prose | pages [6] -->
20

<!-- b000139 | prose | pages [6] -->
15

<!-- b000140 | prose | pages [6] -->
10

<!-- b000141 | prose | pages [6] -->
5

<!-- b000142 | prose | pages [6] -->
0

<!-- b000143 | furniture | pages [6] -->


<!-- b000144 | prose | pages [6] -->
0 20 40 60 80

<!-- b000145 | caption | pages [6] -->
Figure 4 Frequency histogram of non-pre-check arrivals

<!-- b000146 | furniture | pages [6] -->
Page 5 of 20

<!-- b000147 | prose | pages [6] -->
30

<!-- b000148 | prose | pages [6] -->
25

<!-- b000149 | prose | pages [6] -->
20

<!-- b000150 | prose | pages [6] -->
15

<!-- b000151 | prose | pages [6] -->
10

<!-- b000152 | prose | pages [6] -->
5

<!-- b000153 | prose | pages [6] -->
0

<!-- b000154 | furniture | pages [6] -->


<!-- b000155 | prose | pages [6] -->
0 10 20 30 40 50

<!-- b000156 | caption | pages [6] -->
Figure 5 Frequency histogram of pre-check arrivals

<!-- b000157 | prose | pages [6] -->
According to the histograms above, we suppose that the time intervals of both the regular and pre-check arrivals obey exponential distribution 𝑓𝑓(𝑥𝑥) = 𝜆𝜆𝑑𝑑e−𝜆𝜆𝑑𝑑𝑥𝑥.

<!-- b000158 | prose | pages [6] -->
Maximum likelihood estimation of the parameter 𝜆𝜆𝑑𝑑:

<!-- b000159 | furniture | pages [6] -->


<!-- b000160 | prose | pages [6] -->
𝑛𝑛

<!-- b000161 | prose | pages [6] -->
𝑛𝑛

<!-- b000162 | prose | pages [6] -->
𝑛𝑛

<!-- b000163 | furniture | pages [6] -->


<!-- b000164 | prose | pages [6] -->
𝑛𝑛e−𝜆𝜆𝑑𝑑∑ 𝑥𝑥𝑖𝑖

<!-- b000165 | prose | pages [6] -->
=  𝜆𝜆𝑑𝑑e−𝜆𝜆𝑑𝑑𝑥𝑥𝑖𝑖

<!-- b000166 | prose | pages [6] -->
𝐿𝐿(𝜆𝜆𝑑𝑑) =  𝑓𝑓(𝑥𝑥𝑖𝑖)

<!-- b000167 | prose | pages [6] -->
𝑖𝑖=1

<!-- b000168 | prose | pages [6] -->
𝑖𝑖=1

<!-- b000169 | prose | pages [6] -->
𝑛𝑛

<!-- b000170 | prose | pages [6] -->
ln 𝐿𝐿(𝜆𝜆𝑑𝑑) = 𝑛𝑛ln 𝜆𝜆𝑑𝑑−𝜆𝜆𝑑𝑑 𝑥𝑥𝑖𝑖

<!-- b000171 | prose | pages [6] -->
𝑖𝑖=1

<!-- b000172 | prose | pages [6] -->
= 𝜆𝜆𝑑𝑑

<!-- b000173 | prose | pages [6] -->
𝑖𝑖=1

<!-- b000174 | prose | pages [6] -->
𝑛𝑛

<!-- b000175 | prose | pages [6] -->
, d ln 𝐿𝐿(𝜆𝜆𝑑𝑑)

<!-- b000176 | prose | pages [6] -->
= 𝑛𝑛

<!-- b000177 | prose | pages [6] -->
= 0

<!-- b000178 | prose | pages [6] -->
− 𝑥𝑥𝑖𝑖

<!-- b000179 | prose | pages [6] -->
d𝜆𝜆𝑑𝑑

<!-- b000180 | prose | pages [6] -->
𝜆𝜆𝑑𝑑

<!-- b000181 | prose | pages [6] -->
𝑖𝑖=1

<!-- b000182 | prose | pages [6] -->
, and the expectation, 𝐸𝐸𝜆𝜆𝑑𝑑

<!-- b000183 | furniture | pages [6] -->


<!-- b000184 | prose | pages [6] -->
Therefore 𝜆𝜆𝑑𝑑 = 𝑛𝑛 = 1 𝑛𝑛

<!-- b000185 | prose | pages [6] -->
𝑥𝑥𝚤𝚤

<!-- b000186 | prose | pages [6] -->
∑ 𝑥𝑥𝑖𝑖 𝑖𝑖=1

<!-- b000187 | prose | pages [6] -->
𝐸𝐸(𝑥𝑥) = 𝜆𝜆𝑑𝑑, is an unbi-

<!-- b000188 | prose | pages [6] -->
 = 𝐸𝐸 1

<!-- b000189 | prose | pages [6] -->
1  = 𝑥𝑥𝚤𝚤

<!-- b000190 | prose | pages [6] -->
ased estimation. Thus the arrival rates of the regular and pre-check procedures are estimated = 0.10882016, respectively. to be 𝜆𝜆1 = 0.077244 and 𝜆𝜆2 Here, a goodness of ﬁt test is done, and each of the procedures are classiﬁed into 10 classes.

<!-- b000191 | furniture | pages [6] -->


<!-- b000192 | prose | pages [6] -->
Let’s take the regular (without pre-check) procedure as an example:

<!-- b000193 | prose | pages [6] -->
Class 0-8 8-16 16-24 True Frequency 21 13 6 Predicted Probability 24-32 32-40 40-48 48-56 56-64 64-72 72-80 3 0 0 1 1 0 1 0.134  0.072  0.039  0.021  0.011  0.006  0.003  0.002 0.461 0.248 Predicted Frequency 21.204  11.430  6.161  3.321  1.790  0.965  0.520  0.280  0.151  0.081

<!-- b000194 | caption | pages [6] -->
Table 1 Regular procedure, non-pre-check, true frequencies and predicted frequencies

<!-- b000195 | prose | pages [6] -->
10

<!-- b000196 | prose | pages [6] -->
𝜒𝜒2 =  (𝑁𝑁𝑖𝑖−𝑛𝑛𝑝𝑝𝑖𝑖)

<!-- b000197 | prose | pages [6] -->
(9) = 16.919 2

<!-- b000198 | prose | pages [6] -->
= 15.898 < 𝜒𝜒0.05

<!-- b000199 | prose | pages [6] -->
𝑛𝑛𝑝𝑝𝑖𝑖

<!-- b000200 | prose | pages [6] -->
𝑖𝑖=1

<!-- b000201 | prose | pages [6] -->
Thus we consider the above as an exponential distribution.

<!-- b000202 | furniture | pages [6] -->


<!-- b000203 | prose | pages [6] -->
And similarly, ﬁt for the pre-check procedure, 𝜒𝜒2 = 15.599 < 𝜒𝜒0.05

<!-- b000204 | furniture | pages [6] -->


<!-- b000205 | prose | pages [6] -->
(9) = 16.919. 2 Since the inter-arrival time obeys exponential distribution, the number of passengers’ arri-

<!-- b000206 | furniture | pages [6] -->


<!-- b000207 | prose | pages [6] -->
val in unit time obeys Poisson distribution.

<!-- b000208 | prose | pages [6] -->
4.3.2 Phase 1 Queueing Specification

<!-- b000209 | prose | pages [6] -->
We also consider the service time of Phase 1 obeys exponential distribution, which is a common practice for simple cases in queueing theory, and the service rate is below.

<!-- b000210 | prose | pages [6] -->
𝜇𝜇𝑑𝑑= 0.09465 Based on the above discussion, the Kendall notation of Phase 1 is (𝑀𝑀/𝑀𝑀/𝑐𝑐), where 𝑀𝑀

<!-- b000211 | furniture | pages [6] -->


<!-- b000212 | prose | pages [6] -->
denotes a Poisson process and 𝑐𝑐 is the number of parallel servers. The arrival rate of this

<!-- b000213 | furniture | pages [6] -->


<!-- b000214 | furniture | pages [6] -->


<!-- b000215 | furniture | pages [7] -->
Team #67316

<!-- b000216 | furniture | pages [7] -->
Page 6 of 20

<!-- b000217 | prose | pages [7] -->
queueing model depend on certain conditions, and 𝑐𝑐 is given by the airport facility background. We assume that the service rate is a constant 𝜇𝜇𝑑𝑑= 0.09465 for each server.

<!-- b000218 | prose | pages [7] -->
4.3.3 Phase 2

<!-- b000219 | prose | pages [7] -->
0.030

<!-- b000220 | prose | pages [7] -->
Because the two queueing models are in series, we

<!-- b000221 | prose | pages [7] -->
0.025

<!-- b000222 | prose | pages [7] -->
have 𝜆𝜆𝑠𝑠= 𝜇𝜇𝑑𝑑 . Phase 2 is also a multiple-server

<!-- b000223 | prose | pages [7] -->
0.020

<!-- b000224 | prose | pages [7] -->
0.015

<!-- b000225 | prose | pages [7] -->
model, but the serving process is much more com-

<!-- b000226 | prose | pages [7] -->
0.010

<!-- b000227 | prose | pages [7] -->
plicated, besides the histogram does not obey ex- ponential distribution, apparently.

<!-- b000228 | prose | pages [7] -->
0.005

<!-- b000229 | prose | pages [7] -->
0.000

<!-- b000230 | prose | pages [7] -->
An Erlangian model is introduced, Erlang ser-

<!-- b000231 | furniture | pages [7] -->


<!-- b000232 | prose | pages [7] -->
0 20 40 60 80

<!-- b000233 | caption | pages [7] -->
Figure 6 Histogram of the service time in Phase 2, to-

<!-- b000234 | prose | pages [7] -->
vice is widely used to model combined serving

<!-- b000235 | prose | pages [7] -->
gether with a PDF plot of an Erlang distribution.

<!-- b000236 | prose | pages [7] -->
processes, where consequent queueing models are connected in series. 𝑘𝑘 identical Poisson servers in series generate an Erlang type 𝑘𝑘 service. However, it is often the case that parameter 𝑘𝑘 is not strictly equal to the number of phases in a server. PDF of Erlang type 𝑘𝑘 distribution is given by

<!-- b000237 | prose | pages [7] -->
1 Γ(𝛼𝛼)𝛽𝛽𝛼𝛼𝑥𝑥𝛼𝛼−1 exp(−𝑥𝑥/𝛽𝛽 ) , (𝛼𝛼, 𝛽𝛽> 0; 0 < 𝑥𝑥< ∞) 𝑓𝑓(𝑥𝑥) =

<!-- b000238 | prose | pages [7] -->
with the expectation 𝐸𝐸(𝑥𝑥) = 𝛼𝛼𝛼𝛼 and variance 𝑉𝑉𝑉𝑉𝑉𝑉(𝑥𝑥) = 𝛼𝛼𝛽𝛽2 . Parameter 𝛼𝛼 and 𝛽𝛽 is related with 𝑘𝑘 and the service rate 𝜇𝜇 (Gross, et al., 1985):

<!-- b000239 | prose | pages [7] -->
𝛼𝛼= 𝑘𝑘

<!-- b000240 | furniture | pages [7] -->


<!-- b000241 | prose | pages [7] -->
𝛽𝛽= 1

<!-- b000242 | prose | pages [7] -->


<!-- b000243 | prose | pages [7] -->
𝑘𝑘𝑘𝑘

<!-- b000244 | prose | pages [7] -->
Fit the distribution for the total service time in Phase 2 (time to get scanned property),

<!-- b000245 | furniture | pages [7] -->


<!-- b000246 | prose | pages [7] -->
our results are, 𝑘𝑘= 4, 𝜇𝜇𝑠𝑠= 0.0357.

<!-- b000247 | prose | pages [7] -->
Therefore, the Kendall notation of Phase 2 queueing is (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐), where the input 𝑀𝑀 is

<!-- b000248 | furniture | pages [7] -->


<!-- b000249 | prose | pages [7] -->
identical to the output of Phase 1, 𝐸𝐸𝑘𝑘 is an Erlang type 𝑘𝑘= 4, 𝜇𝜇𝑠𝑠= 0.0357 distribution, and the number of parallel servers (i.e. the number of X-ray scanners and millimeter wave scanners) is depend on speciﬁc airport.

<!-- b000250 | prose | pages [7] -->
(𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐) queueing does not have a good analytical solution; our numerical solution using

<!-- b000251 | furniture | pages [7] -->


<!-- b000252 | prose | pages [7] -->
simulation technique will be introduced later.

<!-- b000253 | heading | pages [7] -->
4.4 Section Summary

<!-- b000254 | prose | pages [7] -->
The airport security check process consists of two phases, ﬁrst of which is an (𝑀𝑀/𝑀𝑀/𝑐𝑐) queue- ing process, and the second is an (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐′) queueing. Arrival rate of the second is the service rate of the ﬁrst. Parameters of the distributions can be estimated using the given data.

<!-- b000255 | furniture | pages [7] -->


<!-- b000256 | furniture | pages [7] -->


<!-- b000257 | furniture | pages [8] -->
Team #67316

<!-- b000258 | furniture | pages [8] -->
Page 7 of 20

<!-- b000259 | prose | pages [8] -->
Queueing Simulation and Bottlenecks Spotting

<!-- b000260 | furniture | pages [8] -->


<!-- b000261 | heading | pages [8] -->
5.1 Estimating Expenses

<!-- b000262 | prose | pages [8] -->
According to (Learn.org; PayScale.com), income of a security oﬃcer is $28,624–$58,987 and of an airline security screener is $23,262–$54,015. That is the human resource expenses of the security check. Costs of security devices are mostly one-oﬀ consumptions. The price of an airport X-ray baggage scanner is at $20,000–50,000 and of a millimeter wave full body scanner is at $100,000 (Alibaba.com). And the maintenance cost is mainly from the electricity. Another fact is that one single lane of the scan check process requires 4 security screeners on average. Therefore, we drew a conclusion that the cost of one lane (server) in Phase 2, is about the cost of 4 desks (servers) at Phase 1.

<!-- b000263 | heading | pages [8] -->
5.2 Basic Ideas

<!-- b000264 | prose | pages [8] -->
A MATLAB program is written to simulate the entire security check process. To build up the numeric solution, Markov chains are used for Erlangian queueing. (Zeng, et al., 2011)

<!-- b000265 | furniture | pages [8] -->


<!-- b000266 | caption | pages [8] -->
Figure 7 MATLAB simulation speciﬁcation

<!-- b000267 | furniture | pages [8] -->


<!-- b000268 | furniture | pages [8] -->


<!-- b000269 | furniture | pages [9] -->
Team #67316

<!-- b000270 | furniture | pages [9] -->
Page 8 of 20

<!-- b000271 | prose | pages [9] -->
Since there is no analytical solution of an (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐) (Phase 2) queueing model, a simulation

<!-- b000272 | furniture | pages [9] -->


<!-- b000273 | prose | pages [9] -->
of the entire security check process is put forward, and both Phase 1 and Phase 2 are concerned in the model in series.

<!-- b000274 | prose | pages [9] -->
Given the parameters of each probability distribution at the two phases, we generate series

<!-- b000275 | furniture | pages [9] -->


<!-- b000276 | prose | pages [9] -->
of random variates to simulate the process. First, random variates obeying exponential distri- bution is generated as people’s inter-arrival time. We then calculate and store the arrival timestamps, service time (generated random variables obeying another exponential distribution) and waiting time (worked out with the previous passenger’s waiting time, service time and the arrival interval) of each passenger in a table. Besides getting results of waiting time spans, the removal rate of Phase 1 is also observed, which is used as the arrival of Phase 2. After working on Phase 1, we do the same on Phase 2, but the new service is Erlangian. Finally, expectations of total waiting time are evaluated.

<!-- b000277 | prose | pages [9] -->
To spot the bottlenecks in the process, we tested the improvements of total waiting time

<!-- b000278 | furniture | pages [9] -->


<!-- b000279 | prose | pages [9] -->
expectations when 4 document check servers are added (row “Document Check Added” in the table below), and 1 scan check server is added (row “Scan Check Added”).

<!-- b000280 | heading | pages [9] -->
5.3 Spot the Bottlenecks!

<!-- b000281 | prose | pages [9] -->
The simulated security process has a changeable arrival rate 𝜆𝜆𝑑𝑑, and both of the initial numbers of the document check servers and of the scan check servers are assigned 5, as is the case in Figure 2, which is a small scale for an airport. The service rate of one document check server is assigned 𝜇𝜇𝑑𝑑= 0.09465, and that of one scan check service is 𝜇𝜇𝑠𝑠= 0.0357. Service of Phase 2 is Erlangian type 𝑘𝑘= 4. These three parameters are the same to what we have mentioned before.

<!-- b000282 | prose | pages [9] -->
Below lists the expectations for total waiting time at diﬀerent arrival rates. Row “Original”

<!-- b000283 | furniture | pages [9] -->


<!-- b000284 | prose | pages [9] -->
is the total waiting time expectation of process consist of (𝑀𝑀/𝑀𝑀/5) and (𝑀𝑀/𝐸𝐸𝑘𝑘/5). Row “Doc- ument Check Added” for the case that 4 document check servers are added, that is (𝑀𝑀/𝑀𝑀/9) for Phase 1 and (𝑀𝑀/𝐸𝐸𝑘𝑘/5) for Phase 2. For row “Scan Check Added”, 1 scan check server is added, that is (𝑀𝑀/𝑀𝑀/5) and (𝑀𝑀/𝐸𝐸𝑘𝑘/6).

<!-- b000285 | prose | pages [9] -->
𝝀𝝀𝒅𝒅 3.710 3.247 Original 4.329 4.478 4.638 4.810 5.194 22632 31349 Document Check Added 12781 10807 8988 7391 3668 21878 31092 Scan Check Added 11832 10671 8925 7215 3291 10643 18258 3045 1680 271 88 24

<!-- b000286 | caption | pages [9] -->
Table 2 Simulation results of the total waiting time (in seconds)

<!-- b000287 | prose | pages [9] -->
We ﬁnd that, the document check process is not the bottleneck of the process, but the scan

<!-- b000288 | furniture | pages [9] -->


<!-- b000289 | prose | pages [9] -->
check. By adding scan check lanes, service capability of the whole system is signiﬁcantly in- creased. We can even observe that some divergent queueing cases converge (e.g. 𝜆𝜆𝑑𝑑= 5.194).

<!-- b000290 | furniture | pages [9] -->


<!-- b000291 | furniture | pages [9] -->


<!-- b000292 | furniture | pages [10] -->
Team #67316

<!-- b000293 | heading | pages [10] -->
5.4 Comments

<!-- b000294 | furniture | pages [10] -->
Page 9 of 20

<!-- b000295 | prose | pages [10] -->
Based on the above analysis, bottlenecks restricting the queueing capacity and eﬃciency comes from the scan process Phase 2. From the given data, we see that the X-ray scan time is usually fast and steady, and is not likely to be the bottleneck. However, time taken for the passenger to take oﬀ clothes and to take care of their carry-on properties contribute much to the next passenger’s waiting (time C in Figure 3), especially when someone is heavy with carry-on properties or not experienced in air travelling.

<!-- b000296 | prose | pages [10] -->
We would recommend the airport to allow the passengers to take a bin for their to-be-

<!-- b000297 | furniture | pages [10] -->


<!-- b000298 | prose | pages [10] -->
scanned properties before queueing, and thus waiting time in Phase 2 will be reduced.

<!-- b000299 | prose | pages [10] -->
Comments on the Safety

<!-- b000300 | furniture | pages [10] -->


<!-- b000301 | prose | pages [10] -->
Firstly, on the stand of the airport, any security accident, including terrorist attacks, hijacking or aircraft destroying, if happens, will cause unbearable blame from the public opinion, which is unacceptable for the airport. Thus it does not sound like a good idea to reduce the links in security check procedure to fasten check-in and to lower the expenses.

<!-- b000302 | prose | pages [10] -->
A fundamental principle of our later discussion is that, no procedure in the security check

<!-- b000303 | furniture | pages [10] -->


<!-- b000304 | prose | pages [10] -->
chain is omitted. Means like optimizing queueing processes, arranging human resources, guid- ing passengers’ arrival can be implemented as ways to improve the passenger experience.

<!-- b000305 | heading | pages [10] -->
Passenger Arrival Behavior Modeling

<!-- b000306 | furniture | pages [10] -->


<!-- b000307 | heading | pages [10] -->
7.1 Passenger Flow Generating

<!-- b000308 | prose | pages [10] -->
Flight records of O’Hare International Airport on Wednesday, Jan. 18, 2017 were found on (Flight Stats), including the departure time and information of the plane models. Most of the airlines are Boeing 737-800 whose capacity is usually 104–189 passengers.

<!-- b000309 | prose | pages [10] -->
To simulate the passenger arrival behavior, i.e.

<!-- b000310 | furniture | pages [10] -->


<!-- b000311 | prose | pages [10] -->
1000

<!-- b000312 | prose | pages [10] -->
the varying passenger ﬂow in a time period, we as-

<!-- b000313 | prose | pages [10] -->
900

<!-- b000314 | prose | pages [10] -->
sume that the capacity of every ﬂight is about 189,

<!-- b000315 | prose | pages [10] -->
800

<!-- b000316 | prose | pages [10] -->
and the points of the passengers’ arrival time obey

<!-- b000317 | prose | pages [10] -->
700

<!-- b000318 | prose | pages [10] -->
normal distribution. Since TSA recommends passen-

<!-- b000319 | prose | pages [10] -->
600

<!-- b000320 | prose | pages [10] -->
gers to be at the airport 2 hours earlier before the

<!-- b000321 | prose | pages [10] -->
500

<!-- b000322 | prose | pages [10] -->
ﬂight for domestic departures, we model the passen- gers’ arrival time for each ﬂight to obey normal dis-

<!-- b000323 | prose | pages [10] -->
400

<!-- b000324 | prose | pages [10] -->
tribution 𝑁𝑁(𝜇𝜇, 𝜎𝜎2), and let 𝜇𝜇 be 2 hours before the

<!-- b000325 | prose | pages [10] -->
300 200 300 400 500 600 700 0 100

<!-- b000326 | prose | pages [10] -->
departure and 𝜇𝜇+ 3𝜎𝜎 be the point in time that there is half an hour remained.

<!-- b000327 | furniture | pages [10] -->


<!-- b000328 | furniture | pages [10] -->


<!-- b000329 | caption | pages [10] -->
Figure 8 Varying passenger ﬂow in a time period, from

<!-- b000330 | prose | pages [10] -->
6:30 a.m. to 16:40 p.m., O’Hare International Airport, Jan. 18, 2017

<!-- b000331 | furniture | pages [11] -->
Team #67316

<!-- b000332 | furniture | pages [11] -->
Page 10 of 20

<!-- b000333 | prose | pages [11] -->
We then add these PDFs together and get the dynamic passenger arrival data. The shown

<!-- b000334 | furniture | pages [11] -->


<!-- b000335 | prose | pages [11] -->
plotted graph (Figure 8) is such a practice on timespan between 6:30 a.m. to 16:40 p.m.

<!-- b000336 | prose | pages [11] -->
We can see a peak at 9:30 a.m. and at around 11:00, the passenger ﬂow get down to a

<!-- b000337 | furniture | pages [11] -->


<!-- b000338 | prose | pages [11] -->
relatively low level (this is probably because of massive departures).

<!-- b000339 | prose | pages [11] -->
Based on the above passenger ﬂow distribution, we will simulate the security check queue-

<!-- b000340 | furniture | pages [11] -->


<!-- b000341 | prose | pages [11] -->
ing process at a domestic departure checkpoint later.

<!-- b000342 | heading | pages [11] -->
7.2 Arrival Time Recommendation

<!-- b000343 | prose | pages [11] -->
We tend to believe that the passenger arrival behavior can be changed by recommending their arrival time, however this is often much more complex due to airport location or cultural norm of a certain nation.

<!-- b000344 | prose | pages [11] -->
We calculated the mean waiting time of the passengers by simulating using the varying

<!-- b000345 | furniture | pages [11] -->


<!-- b000346 | prose | pages [11] -->
passenger ﬂow introduced in the last subsection, at diﬀerent normal distributions as we men- tioned above. Only one checkpoint is taken into account in the simulation, and the ﬂow is generated with domestic departure ﬂights. When the average arrival of the passengers for a certain ﬂight is 120 minutes earlier, its mean waiting time in the security check process is about 26 minutes as shown in the chart below.

<!-- b000347 | prose | pages [11] -->
Diﬀerence of 𝝁𝝁 and the departure time (min) 90 105 120 150 180 𝝈𝝈 (Ensured that 𝝁𝝁+ 𝟑𝟑𝟑𝟑 is at 30 min earlier the departure) Passenger ﬂow per hour Mean waiting at Phase 1 (sec) Mean waiting at Phase 2 (sec) 20 25 30 40 50 491 498 502 503 498 0.0953 0.0633 0.0781 0.0654 0.0631 82.9986 56.146 26.0189 21.7186 16.9306

<!-- b000348 | caption | pages [11] -->
Table 3 Result for waiting time at diﬀerent recommended time

<!-- b000349 | prose | pages [11] -->
From the chart, we curiously found that the earlier the passengers arrive, the less the mean

<!-- b000350 | furniture | pages [11] -->


<!-- b000351 | prose | pages [11] -->
waiting time will be. This is quite expected, because earlier arrivals and more uniformly dis- tributed arrival intervals can reduce the “strikes” of the passenger ﬂow.

<!-- b000352 | prose | pages [11] -->
Cultural norm impact on the arrival rate distribution (“varying passenger ﬂow”, in other

<!-- b000353 | furniture | pages [11] -->


<!-- b000354 | prose | pages [11] -->
words) will be discussed later. Measures like sending text messages to passengers for recom- mending their arrivals based on real-time data as well as their cultural background will help.

<!-- b000355 | prose | pages [11] -->
Checkpoint Redesign

<!-- b000356 | furniture | pages [11] -->


<!-- b000357 | heading | pages [11] -->
8.1 Concentrating the Checkpoints

<!-- b000358 | prose | pages [11] -->
8.1.1 Basic Ideas

<!-- b000359 | prose | pages [11] -->
In queueing theory, it is found that (𝑀𝑀/𝑀𝑀/𝑐𝑐) queueing has a better performance than 𝑐𝑐 par- allel (𝑀𝑀/𝑀𝑀/1) queueing processes, with shorter mean queue length and better mean waiting time. (See Appendix 13.1 for Proof) Simulation of a more complex system, as in the security check process is made and the results are consistent. According to our assumption, so long as

<!-- b000360 | furniture | pages [11] -->


<!-- b000361 | furniture | pages [11] -->


<!-- b000362 | furniture | pages [12] -->
Team #67316

<!-- b000363 | furniture | pages [12] -->
Page 11 of 20

<!-- b000364 | prose | pages [12] -->
the passengers could see the servers, they will choose to wait in the queue that minimizes their waiting time. Thus making the passengers know the queueing conditions at checkpoints works.

<!-- b000365 | prose | pages [12] -->
8.1.2 Measures to Take

<!-- b000366 | prose | pages [12] -->
Security checkpoints to terminals are shown in the O’Hare terminal map. (Chicago Department of Aviation, 2012). We would recommend the airport to reduce the distances between each checkpoints at Terminal 1 and 3. This will help the passengers to choose a checkpoint minimiz- ing their waiting among the equivalent check- points at each terminal.

<!-- b000367 | furniture | pages [12] -->


<!-- b000368 | prose | pages [12] -->
Another possible solution which is equiva- lent to the former is to monitor the real-time queue length of each checkpoint at Terminal 1 and 3 and install LED boards to show these in- formation. This also helps the passengers to choose a proper checkpoint.

<!-- b000369 | caption | pages [12] -->
Figure 9 O’Hare Terminal Map, © 2012 Chicago Depart-

<!-- b000370 | prose | pages [12] -->
ment of Aviation, URL: http://www.ﬂychicago.com

<!-- b000371 | prose | pages [12] -->
/OHare/EN/AtAirport/map/default.aspx (Chicago

<!-- b000372 | prose | pages [12] -->
Department of Aviation, 2012)

<!-- b000373 | prose | pages [12] -->
The above measures may both avoid some queue’s getting too long and cause a congestion.

<!-- b000374 | furniture | pages [12] -->


<!-- b000375 | heading | pages [12] -->
8.2 Checkpoint Structure

<!-- b000376 | prose | pages [12] -->
Distribution of Human Resource between the 2 Phases 8.2.1

<!-- b000377 | prose | pages [12] -->
This suggestion on checkpoint redesign is a continued section of Section 5.3, Spotting Bottle- necks. We know that the cost of a lane in Phase 2 is 4 times more than that of a desk at Phase 1. Optimizing the checkpoint structure and keep the cost relatively low can balance the service rates of the document check process and the scan check process, as well as saving money.

<!-- b000378 | prose | pages [12] -->
This is a programming problem in operation research. Assume the number of document

<!-- b000379 | furniture | pages [12] -->


<!-- b000380 | prose | pages [12] -->
check servers is 𝑘𝑘1, and that of the scan check is 𝑘𝑘2.

<!-- b000381 | prose | pages [12] -->
𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀 𝑘𝑘1 + 𝑘𝑘2,

<!-- b000382 | prose | pages [12] -->
⎧0 < 𝑘𝑘1, 𝑘𝑘2 ≤5 ª

<!-- b000383 | furniture | pages [12] -->


<!-- b000384 | prose | pages [12] -->
𝑘𝑘1𝜇𝜇𝑑𝑑> 𝜆𝜆𝑑𝑑

<!-- b000385 | prose | pages [12] -->
𝑠𝑠. 𝑡𝑡.

<!-- b000386 | prose | pages [12] -->
⎨ ª

<!-- b000387 | prose | pages [12] -->
𝑘𝑘2𝜇𝜇𝑠𝑠> 𝜆𝜆𝑠𝑠

<!-- b000388 | prose | pages [12] -->
⎩

<!-- b000389 | prose | pages [12] -->
We trial the number of servers with our simulation to ﬁnd the appropriate ratio. Our result

<!-- b000390 | furniture | pages [12] -->


<!-- b000391 | prose | pages [12] -->
is, when there are 5 lanes of scan check servers, 3 document check servers are enough for most common cases. Cut on document check service desks won’t cause bottlenecks, and according to our previous study, adding new lanes will greatly improve the security check service.

<!-- b000392 | furniture | pages [12] -->


<!-- b000393 | furniture | pages [12] -->


<!-- b000394 | furniture | pages [13] -->
Team #67316

<!-- b000395 | furniture | pages [13] -->
Page 12 of 20

<!-- b000396 | furniture | pages [13] -->
571-630

<!-- b000397 | prose | pages [13] -->
Time since the initial (min)

<!-- b000398 | furniture | pages [13] -->
391-450

<!-- b000399 | furniture | pages [13] -->
451-510

<!-- b000400 | furniture | pages [13] -->
511-570

<!-- b000401 | prose | pages [13] -->
Passenger ﬂow /h 563 433 277 Positions needed for Phase 1 2 2 1 Mean waiting time at Phase 1

<!-- b000402 | furniture | pages [13] -->
631-690

<!-- b000403 | furniture | pages [13] -->
691-750

<!-- b000404 | furniture | pages [13] -->
751-810

<!-- b000405 | furniture | pages [13] -->
811-870

<!-- b000406 | furniture | pages [13] -->
871-930

<!-- b000407 | furniture | pages [13] -->
931-990

<!-- b000408 | prose | pages [13] -->
473 430 484 550 541 662 617 2 2 2 2 2 2 3 3 12.2084 28.7135 7.6859 103.3296 Positions needed for Phase 2 5 4 3 Mean waiting time at Phase 2 27.3362 31.1131 14.1786 7.2299 11.2017 21.9008 17.9357 4.1698 3.188 5 5 4 5 5 5 5 5 7.986 26.8053 7.2921 19.351 15.4442 6172 96.1114

<!-- b000409 | caption | pages [13] -->
Figure 10 Numbers of positions needed at Phase 1 and Phase 2 to make the queue length converge

<!-- b000410 | prose | pages [13] -->
Dynamic Assignment of Duty in a Time Span 8.2.2

<!-- b000411 | prose | pages [13] -->
Based on our previous work on passenger ﬂow distribution in a period of time and the pro- gramming in the above subsubsection, we evaluate the duty assignment at each checkpoint every hour.

<!-- b000412 | prose | pages [13] -->
7

<!-- b000413 | prose | pages [13] -->
6

<!-- b000414 | prose | pages [13] -->
5

<!-- b000415 | prose | pages [13] -->
4

<!-- b000416 | prose | pages [13] -->
3

<!-- b000417 | prose | pages [13] -->
2

<!-- b000418 | prose | pages [13] -->
1

<!-- b000419 | prose | pages [13] -->
0

<!-- b000420 | prose | pages [13] -->
6:30 7:30 8:30 9:30 10:30 11:30 12:30 13:30 14:30 15:30

<!-- b000421 | furniture | pages [13] -->


<!-- b000422 | caption | pages [13] -->
Figure 11 Dynamic assignment of duty with Phase 1 in blue and Phase 2 in green

<!-- b000423 | prose | pages [13] -->
Allocating fewer staﬀ at the troughs, and more at the peaks, will help the security check

<!-- b000424 | furniture | pages [13] -->


<!-- b000425 | prose | pages [13] -->
system running properly at relatively low cost.

<!-- b000426 | prose | pages [13] -->
And for the speciﬁc problem we are now considering, we practice this method and plan to

<!-- b000427 | furniture | pages [13] -->


<!-- b000428 | prose | pages [13] -->
allocate the duty like this:

<!-- b000429 | furniture | pages [13] -->


<!-- b000430 | furniture | pages [13] -->


<!-- b000431 | prose | pages [13] -->
– 8:30 a.m.

<!-- b000432 | prose | pages [13] -->
2 for document check and 4 for scan check 8:30 a.m.  – 13:30 p.m.

<!-- b000433 | prose | pages [13] -->
2 for document check and 5 for scan check 13:30 p.m.  – 16:30 p.m.

<!-- b000434 | prose | pages [13] -->
3 for document check and 6 for scan check

<!-- b000435 | caption | pages [13] -->
Table 4 Dynamic duty allocation

<!-- b000436 | prose | pages [13] -->
8.2.3

<!-- b000437 | heading | pages [13] -->
Sensitivity Test

<!-- b000438 | prose | pages [13] -->
A sensitivity test is made for our model. The test is done via simulation.

<!-- b000439 | furniture | pages [13] -->


<!-- b000440 | prose | pages [13] -->
Original Passenger ﬂow 502 Serve ability (Phase 2) 0.036 Mean waiting time 41.70 Decreased ﬂow Increased service ability 452 502 0.036 0.040 12.57 7.834

<!-- b000441 | caption | pages [13] -->
Table 5 Sensitivity test result, simulations for each case are done for 5 times

<!-- b000442 | furniture | pages [13] -->


<!-- b000443 | furniture | pages [13] -->


<!-- b000444 | furniture | pages [14] -->
Team #67316

<!-- b000445 | furniture | pages [14] -->
Page 13 of 20

<!-- b000446 | prose | pages [14] -->
We ﬁnd that when the passenger ﬂow decreases by 10%, the mean waiting time deceases

<!-- b000447 | furniture | pages [14] -->


<!-- b000448 | prose | pages [14] -->
by 69.9%. When the document check service ability is raised by 10%, the mean waiting time almost remains the same. And if the service ability at Phase 2 is increased by 10%, the mean waiting time drops as much as 81.2%!

<!-- b000449 | prose | pages [14] -->
From the above test, we drew a conclusion that the queueing system is sensitive to the scan

<!-- b000450 | furniture | pages [14] -->


<!-- b000451 | prose | pages [14] -->
check service ability, while a low sensitivity is observed for changes of the document check ability. This again veriﬁes the bottlenecks that we found earlier, and optimization can be given around the found bottlenecks.

<!-- b000452 | prose | pages [14] -->
Virtual Queueing

<!-- b000453 | furniture | pages [14] -->


<!-- b000454 | prose | pages [14] -->
Waiting room can be useful to improve passengers’ experience. What’s even better is that the queueing discipline can be modiﬁed with this method. The conventional physical queue method is a strict FIFS (First In First Served), while virtual queueing can be more ﬂexible. With the popularization of smartphones, new queueing methods that basically share the same process as virtual queueing, such as mobile queueing, but are more convenient and more suﬃcient are introduced, which will also provide us more possibilities to modify the queueing process. (Wikipedia; Zhao, et al., 2016)

<!-- b000455 | heading | pages [14] -->
9.1 Strict Priority Queue

<!-- b000456 | prose | pages [14] -->
Passengers’ satisfaction can be quantiﬁed by the number of passengers that missed their ﬂights, mean remaining time after security check and the variant of the remaining time. Although FIFS sounds like an absolutely equitable practice, it is frustrating under some extreme circum- stances. Imagine an “early bird” comes to the airport 6 hours in advance of his or her departure. If an unfortunate congestion occurs, the early passenger would hold up the passengers behind whose ﬂight might be to take oﬀ. This is not acceptable.

<!-- b000457 | prose | pages [14] -->
Consider a strict priority queue, where the priority is strictly based on the departure time

<!-- b000458 | furniture | pages [14] -->


<!-- b000459 | prose | pages [14] -->
of each passenger. We now prove that this approach achieves better passenger satisfaction with our simulation.

<!-- b000460 | prose | pages [14] -->
Fewer missed flights!

<!-- b000461 | prose | pages [14] -->
Longer remaining time!

<!-- b000462 | prose | pages [14] -->
Smaller variance!

<!-- b000463 | prose | pages [14] -->
Great! Fewer risks!

<!-- b000464 | prose | pages [14] -->
Easy boarding.

<!-- b000465 | prose | pages [14] -->
Sounds fair!

<!-- b000466 | furniture | pages [14] -->


<!-- b000467 | caption | pages [14] -->
Figure 12 Passenger satisfaction

<!-- b000468 | furniture | pages [14] -->


<!-- b000469 | furniture | pages [14] -->


<!-- b000470 | furniture | pages [15] -->
Team #67316

<!-- b000471 | furniture | pages [15] -->
Page 14 of 20

<!-- b000472 | prose | pages [15] -->
Our approach is to change the queueing discipline in the simulation, and we do ﬁnd a strict

<!-- b000473 | furniture | pages [15] -->


<!-- b000474 | prose | pages [15] -->
priority queue performs better in the above aspects. The testing data involves a passenger ﬂow of 723 passengers per hour. Our results are as follows:

<!-- b000475 | furniture | pages [15] -->


<!-- b000476 | prose | pages [15] -->
1 2 3 4 5 FIFS 231 292 233 280 346 Priority 19 0 0 35 0 6 7 8 9 10 Mean 298 333 316 209 274 281.2 31 0 2 7 0 9.4

<!-- b000477 | caption | pages [15] -->
Figure 13 Numbers of passenger that missed their ﬂights. 10 experiments are done here.

<!-- b000478 | prose | pages [15] -->
And the means and the variances of remaining time:

<!-- b000479 | furniture | pages [15] -->


<!-- b000480 | furniture | pages [15] -->


<!-- b000481 | prose | pages [15] -->
Mean FIFS Variance 6.8787 × 106 6918

<!-- b000482 | prose | pages [15] -->
Priority 3.9684 × 106 6864

<!-- b000483 | caption | pages [15] -->
Figure 14 Means and variances of the remaining time

<!-- b000484 | prose | pages [15] -->
Means are almost the same (this is expected, because expectation for the waiting time won’t

<!-- b000485 | furniture | pages [15] -->


<!-- b000486 | prose | pages [15] -->
vary with queueing discipline, which is a theorem in queueing theory. The slight diﬀerence is caused by the generation of random variates) while variance of queueing where priority is considered seems to be better.

<!-- b000487 | heading | pages [15] -->
9.2 Virtual Queueing Concerning Partial Priority Discipline

<!-- b000488 | prose | pages [15] -->
However, a strict priority queue does not sounds rational to a lot of people. (And of course, it is culture dependent.) A better queueing discipline is introduced here to be a fairer and more eﬃcient option, and above all, cultural adaptable.

<!-- b000489 | prose | pages [15] -->
We introduce an “acceptability factor” 𝛼𝛼 (0 ≤𝛼𝛼≤1) denote the acceptance of the strict

<!-- b000490 | furniture | pages [15] -->


<!-- b000491 | prose | pages [15] -->
priority discipline. We then use a partial priority discipline, which is a mixture of strict FIFS and strict priority discipline.

<!-- b000492 | prose | pages [15] -->
Let 𝑡𝑡𝑎𝑎 denote a passenger’s arrival time, and 𝑡𝑡𝑑𝑑 denote his or her departure time. We use

<!-- b000493 | furniture | pages [15] -->


<!-- b000494 | prose | pages [15] -->
𝑡𝑡𝑝𝑝= 𝛼𝛼𝑡𝑡𝑑𝑑+ (1 −𝛼𝛼)𝑡𝑡𝑎𝑎

<!-- b000495 | prose | pages [15] -->
as the priority of the passengers, and sort the waiting queue in this discipline.

<!-- b000496 | prose | pages [15] -->
We tested 𝛼𝛼= 0.5 for a passenger ﬂow at 721 passengers/h, which is quite an extreme case

<!-- b000497 | furniture | pages [15] -->


<!-- b000498 | prose | pages [15] -->
for a single checkpoint. Below is our result.

<!-- b000499 | furniture | pages [15] -->


<!-- b000500 | prose | pages [15] -->
Passengers Missed Flight FIFS Variance 6.8787 × 106 281.2

<!-- b000501 | prose | pages [15] -->
Partial Priority 5.1711 × 106 71.3

<!-- b000502 | prose | pages [15] -->
Strict Priority 3.9684 × 106 9.4

<!-- b000503 | caption | pages [15] -->
Table 6 Number of passengers that missed the ﬂight (10 hours) and variance of remaining time, 𝛼𝛼= 0.5

<!-- b000504 | prose | pages [15] -->
We ﬁnd the partial priority discipline is also eﬀective in raising passenger satisfaction.

<!-- b000505 | furniture | pages [15] -->


<!-- b000506 | furniture | pages [15] -->


<!-- b000507 | furniture | pages [15] -->


<!-- b000508 | furniture | pages [16] -->
Team #67316

<!-- b000509 | prose | pages [16] -->
Inter-cultural Applicability

<!-- b000510 | heading | pages [16] -->
10.1 Cultural Impacts on Punctuality

<!-- b000511 | furniture | pages [16] -->
Page 15 of 20

<!-- b000512 | prose | pages [16] -->
Diﬀerent cultural norms have an impact on passengers’ punctuality.

<!-- b000513 | prose | pages [16] -->
People in the United States, Canada and many northern European countries have a linear

<!-- b000514 | furniture | pages [16] -->


<!-- b000515 | prose | pages [16] -->
view of time, and are more likely to be punctual. This is also true to East Asian countries, like China and Japan, where social eﬃciency is seen important. In these countries, people tend to have a keen sense of time, and would usually be early for an event. On the contrast, Spaniards or people from Southern Europe are not so punctual. Passengers from such nations often hurry to board. (Business Insider) Viewing the diﬀerences of varied cultural norms with our passenger arrival behavior model

<!-- b000516 | furniture | pages [16] -->


<!-- b000517 | prose | pages [16] -->
(see Section 7), we can say that the passenger ﬂow in countries where people are more punctual is often more smooth and steady. More mathematically, the mean arrival time 𝜇𝜇 is often far earlier than the passengers’ ﬂight departures, and the variance of their arrival distribution 𝜎𝜎2 is relatively small. Case for countries that are not so punctual is just opposite, as shown in the following plotted graph.

<!-- b000518 | prose | pages [16] -->
1100

<!-- b000519 | prose | pages [16] -->
1000

<!-- b000520 | prose | pages [16] -->
900

<!-- b000521 | prose | pages [16] -->
800

<!-- b000522 | prose | pages [16] -->
700

<!-- b000523 | prose | pages [16] -->
600

<!-- b000524 | prose | pages [16] -->
500 0 100 200 300 400 500 600

<!-- b000525 | furniture | pages [16] -->


<!-- b000526 | caption | pages [16] -->
Figure 15 Smooth passenger ﬂow, 𝜇𝜇 is 150 minutes earlier

<!-- b000527 | prose | pages [16] -->
the departure, and 𝜎𝜎= 40.

<!-- b000528 | furniture | pages [16] -->


<!-- b000529 | prose | pages [16] -->
1400

<!-- b000530 | prose | pages [16] -->
1200

<!-- b000531 | prose | pages [16] -->
1000

<!-- b000532 | prose | pages [16] -->
800

<!-- b000533 | prose | pages [16] -->
600

<!-- b000534 | prose | pages [16] -->
400

<!-- b000535 | prose | pages [16] -->
200 0 100 200 300 400 500 600

<!-- b000536 | furniture | pages [16] -->


<!-- b000537 | caption | pages [16] -->
Figure 16 Rough passenger ﬂow, where 𝜇𝜇 is 90 minutes

<!-- b000538 | prose | pages [16] -->
earlier, and 𝜎𝜎= 20.

<!-- b000539 | prose | pages [16] -->
Airports with more smooth and steady passenger ﬂow does not requires too much human

<!-- b000540 | furniture | pages [16] -->


<!-- b000541 | prose | pages [16] -->
resource, and its assignment can be more ﬂexible, for passenger ﬂow peaks are seldom observed. Scale eﬀect that adopt (𝑀𝑀/𝑀𝑀/𝑐𝑐) rather than 𝑐𝑐 parallel (𝑀𝑀/𝑀𝑀/1) also tend to work. Instead, it is not this satisfying in a less punctual nation. More peaks will be found, and massive human resource is needed to deal with the sudden congestions.

<!-- b000542 | prose | pages [16] -->
As we have mentioned before, sending text messages in advance to recommend passengers’

<!-- b000543 | furniture | pages [16] -->


<!-- b000544 | prose | pages [16] -->
check-in time personally based on the current passenger ﬂow at the airport is a very good practice. But when diﬀerent cultural norms are considered, this is not that easy, for people’s punctuality must be taken into account. Since there is no such practice now, we cannot deter- mine the 𝜇𝜇 and 𝜎𝜎2 of people’s arrival behavior in diﬀerent countries, yet we can prove it cer- tainly works.

<!-- b000545 | furniture | pages [16] -->


<!-- b000546 | furniture | pages [16] -->


<!-- b000547 | furniture | pages [17] -->
Team #67316

<!-- b000548 | furniture | pages [17] -->
Page 16 of 20

<!-- b000549 | heading | pages [17] -->
10.2 Cultural Impacts in Queueing Process

<!-- b000550 | prose | pages [17] -->
Another cultural impact on our model is the acceptability of priority queueing in diﬀerent nations. People in the United States respect others’ privacy as well as they hate other people cutting in line. Swiss are punctual and take collective eﬃciency as the most important. While in China, jumping queues is usual because individual eﬃciency is respected, and people tend to forgive such behaviors if the queue jumper has reasonable excuses.

<!-- b000551 | furniture | pages [17] -->


<!-- b000552 | prose | pages [17] -->
The above varied thinking patterns may lead to diﬀerent acceptability in diﬀerent nations. Our acceptability factor 𝛼𝛼 (See 9.2 for deﬁnition), enlighten the culture-related factor in our model.

<!-- b000553 | furniture | pages [17] -->


<!-- b000554 | prose | pages [17] -->
For example, passengers from the United States tend to think the new queueing discipline is not acceptable, because it damages the FIFS principle. However, Swiss might be in favor of our method because it dramatically raises the collective eﬃciency, and thus a greater 𝛼𝛼 could be assigned. Chinese would probably think a neutral 𝛼𝛼 was a good practice.

<!-- b000555 | heading | pages [17] -->
Discussion and Conclusions

<!-- b000556 | heading | pages [17] -->
11.1 Policy Recommendations

<!-- b000557 | prose | pages [17] -->
We here give a complete guide on security check modiﬁcations and policy making for the TSA security manager based on our previous model, as our solution to problem 4.

<!-- b000558 | furniture | pages [17] -->


<!-- b000559 | prose | pages [17] -->
To Security Managers

<!-- b000560 | prose | pages [17] -->
To solve the airport security check congestion, and to optimize the throughput at the airport security checkpoints, we give you the following recommendations on policy making based on our investigation.

<!-- b000561 | prose | pages [17] -->
On human resource distribution, we would recommend fewer document

<!-- b000562 | furniture | pages [17] -->


<!-- b000563 | prose | pages [17] -->
check servers, while more for scan check. Bottlenecks of the security check workﬂow are at the scan check phase, and we have proved that 2 or 3 desks for document check is enough for a 5-lane scan check area. Dynamic allocation of document check servers and lanes opened should be reserved as a way to reduce unnecessary cost, besides, our approach to solve this has been put forward in our paper.

<!-- b000564 | prose | pages [17] -->
On facilities, waiting rooms should be built for virtual queueing. If possible,

<!-- b000565 | furniture | pages [17] -->


<!-- b000566 | prose | pages [17] -->
adding lanes for scan check at each checkpoint will dramatically increase the pas- senger throughput. Shorten the distances between identical checkpoints in the ter- minal will help passengers to choose one that minimizes their waiting. LED boards providing information of queue lengths at each checkpoint works in the same way. If possible, we also recommend a mobile queue system to be built, together with a queue management system, these facilities, thanks to the new information technol- ogy, will enhance the eﬃciency encouragingly. Providing passengers with bins for

<!-- b000567 | furniture | pages [17] -->


<!-- b000568 | furniture | pages [17] -->


<!-- b000569 | furniture | pages [18] -->
Team #67316

<!-- b000570 | furniture | pages [18] -->
Page 17 of 20

<!-- b000571 | prose | pages [18] -->
their to-be-scanned properties in advance will also shorten their waiting during the scan check process and avoid bottlenecks.

<!-- b000572 | prose | pages [18] -->
On safety and the cost, no reduction of links on the current security check

<!-- b000573 | furniture | pages [18] -->


<!-- b000574 | prose | pages [18] -->
procedure is recommended, since the risks cannot be assessed in value. Dynamic assignment of the duties is a possible solution as we have just mentioned above. Opening new lanes for checkpoints will also cost money, but money saved by good human resource allocation can be used for throughput enhancement.

<!-- b000575 | prose | pages [18] -->
We would like to highlight our approach to inﬂuence the passengers’ arri-

<!-- b000576 | furniture | pages [18] -->


<!-- b000577 | heading | pages [18] -->
val. TSA has already made recommendations of time-in-advance for the passengers

<!-- b000578 | prose | pages [18] -->
to avoid missing ﬂights. Through our assumptions and modeling, we are curious to ﬁnd that it is possible to aﬀect the passenger ﬂow by informing passengers of the arrival time ahead of their departure personally and dynamically based on the real- time statistics of the passenger ﬂow at the airport. And the inﬂuenced passenger ﬂow may reduce the occurrence of congestions at security checkpoints.

<!-- b000579 | prose | pages [18] -->
Passengers’ satisfaction is considered and quantiﬁed. With the help of vir-

<!-- b000580 | furniture | pages [18] -->


<!-- b000581 | prose | pages [18] -->
tual queueing mechanism, the departure priority queueing discipline can be prac- ticed, which will reduce the variant of the passengers’ remaining time (thus raises the fairness) and more importantly, reduce the missed ﬂights of the passengers.

<!-- b000582 | heading | pages [18] -->
Cultural norm impact on our model is also taken into consideration. Passen-

<!-- b000583 | furniture | pages [18] -->


<!-- b000584 | prose | pages [18] -->
gers’ cultural background may inﬂuence their punctuality of arrival and acceptabil- ity of our partial priority queueing discipline. Punctuality of a nation has an impact on the passenger ﬂow at an airport, and acceptability of priority queueing should also be taken into account to avoid cultural taboos. This requires adaptation of our models in diﬀerent countries. Changing the assumed normal distribution for passen- ger arrival and the acceptability factor 𝛼𝛼 (See 9.2 for deﬁnition) will help. For ex- ample, for countries where people are not punctual, we can recommend them to be earlier for the ﬂights. Another example is to illustrate the acceptability of our partial priority queueing discipline. In countries where jumping queue is extremely disa- greeable, we can set the queueing to be more FIFS. On contrary, in countries where collective eﬃciency is emphasized, we adjust our factor 𝛼𝛼 to add the priority com- ponents in the queueing process.

<!-- b000585 | furniture | pages [18] -->


<!-- b000586 | prose | pages [18] -->
We hereby sincerely hope the above recommendations will work.

<!-- b000587 | furniture | pages [18] -->


<!-- b000588 | prose | pages [18] -->
Internal Control Management (ICM) team

<!-- b000589 | furniture | pages [18] -->


<!-- b000590 | heading | pages [18] -->
11.2 Model Assessment

<!-- b000591 | prose | pages [18] -->
Model validation has been implemented in each section of the above modeling. Here, we assess the strengths, weaknesses and possible future work in the section.

<!-- b000592 | furniture | pages [18] -->


<!-- b000593 | furniture | pages [18] -->


<!-- b000594 | furniture | pages [19] -->
Team #67316

<!-- b000595 | furniture | pages [19] -->
Page 18 of 20

<!-- b000596 | heading | pages [19] -->
11.2.1 Strengths

<!-- b000597 | prose | pages [19] -->
• Full assumptions and validations are made for passengers’ arrival distribution and se- curity check service time models. Bottlenecks are spotted and thorough analysis is made. • Our simulation of one day’s passenger ﬂow is based on the real data of O’Hare Interna- tional Airport, which is convincing. • Safety is taken as a fundamental principle. All optimization is done based on the prin- ciple. • Recommendations on passenger arrival guidance, checkpoint redesign, change of the queueing discipline, allocation of human resources, virtual queueing are given. Passen- gers’ satisfactory are considered, and the passenger’s ﬂight experience will be improved. • Cultural diﬀerences are quantiﬁed and fully assessed. Sensitivity to these cultural factors of the passenger ﬂow and acceptability to our priority queueing discipline.

<!-- b000598 | heading | pages [19] -->
11.2.2 Weaknesses

<!-- b000599 | prose | pages [19] -->
• TSA Pre-check is not investigated thoroughly. • Lack of further consideration on safety.

<!-- b000600 | heading | pages [19] -->
11.3 Conclusions

<!-- b000601 | prose | pages [19] -->
For problem 1, we use the given data and ﬁnd the distribution pattern of passenger ﬂow and service time, then queueing models are built for the security check process at each checkpoint. We see the security check process as a (𝑀𝑀/𝑀𝑀/𝑐𝑐) queueing and a (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐) process in series. Evaluation of passenger ﬂow behavior in a period of time is made. We use normal distribution to simulate the varying passenger ﬂow.

<!-- b000602 | furniture | pages [19] -->


<!-- b000603 | prose | pages [19] -->
For problem 2, we put forward several possible approaches to improve passenger through- put and raise the passengers’ satisfaction, including checkpoint redesign and virtual queueing where a partial priority queueing discipline is introduced.

<!-- b000604 | furniture | pages [19] -->


<!-- b000605 | prose | pages [19] -->
Cultural norm impacts are also taken into account. For problem 3, we discussed the cultural impact on passenger ﬂow and acceptability of the priority discipline, and recommendations are given to adapt our model to diﬀerent cultures.

<!-- b000606 | furniture | pages [19] -->


<!-- b000607 | prose | pages [19] -->
A detailed guide for policy making is made as our solution of problem 4, again, cultural factors are considered and recommendations concerning cultural diﬀerence are made. The rec- ommendations we gave are all proved to be valid in previous discussions.

<!-- b000608 | heading | pages [19] -->
11.4 Further Work

<!-- b000609 | prose | pages [19] -->
• Discuss the Pre-check modiﬁcation. Levels of security check based on the passengers’ credit rating, or more detailed background check can be implemented.

<!-- b000610 | furniture | pages [19] -->


<!-- b000611 | furniture | pages [19] -->


<!-- b000612 | furniture | pages [20] -->
Team #67316

<!-- b000613 | furniture | pages [20] -->
Page 19 of 20

<!-- b000614 | prose | pages [20] -->
• Investigation on how cultural norm diﬀerences impact the punctuality and attitude towards the priority queueing need to be done. The correlations between the mathe- matical parameters and factors in reality should be revealed. • Detailed research on raising the check-in experience of the disabled and the senior should be made. • Eﬀect caused by waiting based on Lorenz curve.

<!-- b000615 | furniture | pages [20] -->


<!-- b000616 | furniture | pages [20] -->


<!-- b000617 | furniture | pages [20] -->


<!-- b000618 | furniture | pages [20] -->


<!-- b000619 | furniture | pages [20] -->


<!-- b000620 | furniture | pages [21] -->
Team #67316

<!-- b000621 | furniture | pages [21] -->
Page 20 of 20

<!-- b000622 | heading | pages [21] -->
References

<!-- b000623 | references | pages [21] -->
Alibaba.com. Airport security device x-ray baggage scanner. Alibaba. [Online] [Cited: 1

<!-- b000624 | references | pages [21] -->
[1]

<!-- b000625 | references | pages [21] -->
22, 2017.]

<!-- b000626 | references | pages [21] -->
https://www.alibaba.com/product-detail/Airport-security-device-x-ray-

<!-- b000627 | references | pages [21] -->
baggage_60381309000.html.

<!-- b000628 | references | pages [21] -->
—. High Quality Product Millimeter Wave Full Body Scanner Price. Alibaba. [Online]

<!-- b000629 | references | pages [21] -->
[2]

<!-- b000630 | references | pages [21] -->
[Cited: 1 22, 2017.]

<!-- b000631 | references | pages [21] -->
https://www.alibaba.com/product-detail/High-Quality-Product-Millimeter-Wave-

<!-- b000632 | references | pages [21] -->
Full_60569216900.html?spm=a2700.7724838.0.0.uHVhJp.

<!-- b000633 | references | pages [21] -->
Business Insider. How Diﬀerent Cultures Understand Time. Business Insider. [Online]

<!-- b000634 | references | pages [21] -->
[3]

<!-- b000635 | references | pages [21] -->
[Cited: 1 24, 2017.]

<!-- b000636 | references | pages [21] -->
http://www.businessinsider.com/how-different-cultures-understand-time-2014-

<!-- b000637 | references | pages [21] -->
5?IR=T.

<!-- b000638 | references | pages [21] -->
Chicago Department of Aviation. 2012. O'Hare Map. FlyChicago. [Online] Chicago

<!-- b000639 | references | pages [21] -->
[4]

<!-- b000640 | references | pages [21] -->
Department of Aviation, 2012. [Cited: 1 23, 2017.]

<!-- b000641 | references | pages [21] -->
http://www.flychicago.com/pages/landingpage.aspx.

<!-- b000642 | references | pages [21] -->
Flight Stats. Flight Stats Information. Flight Stats. [Online] Flight Stats. [Cited: 1 23,

<!-- b000643 | references | pages [21] -->
[5]

<!-- b000644 | references | pages [21] -->
2017.] http://www.flightstats.com/go/FlightStatus/flightStatusByFlight.do.

<!-- b000645 | references | pages [21] -->
[6]

<!-- b000646 | references | pages [21] -->
Gross, Donald and Harris, Carl M. 1985. Fundamentals of Queueing Theory. s.l. :

<!-- b000647 | references | pages [21] -->
Wiley, 1985. pp. 170-175. ISBN 0-471-89067-7.

<!-- b000648 | references | pages [21] -->
[7]

<!-- b000649 | references | pages [21] -->
Hetter, Katia. 2016. How long will you wait in the TSA security line? CNN. [Online] 6

<!-- b000650 | references | pages [21] -->
9, 2016. [Cited: 1 20, 2017.] http://edition.cnn.com/2016/06/09/travel/tsa-security-

<!-- b000651 | references | pages [21] -->
line-wait-times-how-long/.

<!-- b000652 | references | pages [21] -->
[8]

<!-- b000653 | references | pages [21] -->
Learn.org. How Much Do Airport Security Jobs Pay? Learn.org. [Online] [Cited: 1 22,

<!-- b000654 | references | pages [21] -->
2017.] http://learn.org/articles/How_Much_Do_Airport_Security_Jobs_Pay.html.

<!-- b000655 | references | pages [21] -->
[9]

<!-- b000656 | references | pages [21] -->
PayScale.com. Security Guard Salary (United States). PayScale. [Online] [Cited: 1 22,

<!-- b000657 | references | pages [21] -->
2017.] http://www.payscale.com/research/US/Job=Security_Guard/Hourly_Rate.

<!-- b000658 | references | pages [21] -->
[10]  Taha, Hamdy A. 2014. Operations Research: Pearson New International Edition: An

<!-- b000659 | references | pages [21] -->
Introduction, 9/E. s.l. : Pearson, 2014. ISBN-10: 129202433X.

<!-- b000660 | references | pages [21] -->
[11]  Wikipedia. Queue area. Wikipedia. [Online] [Cited: 1 23, 2017.]

<!-- b000661 | references | pages [21] -->
https://en.wikipedia.org/wiki/Queue_area.

<!-- b000662 | heading | pages [21] -->
[12]  Zeng, Yong, Dong, Lihua and Ma, Jianfeng. 2011. Modeling, Analysis and

<!-- b000663 | prose | pages [21] -->
Simulation in Queueing Phenomena. Xi'an : Xidian Univerisity Press, 2011. pp. 92-96.

<!-- b000664 | prose | pages [21] -->
ISBN 978-7-5606-2672-7.

<!-- b000665 | prose | pages [21] -->
[13]  Zhao, Zhenwu and Ma, Jianjun. 2016. Tendency and Research on the Queue System

<!-- b000666 | prose | pages [21] -->
of Airport Security Check. China Transportation Review. 10 2016, Vol. 38, 10, pp. 64-69.

<!-- b000667 | furniture | pages [21] -->


<!-- b000668 | furniture | pages [21] -->


<!-- b000669 | furniture | pages [22] -->
Team #67316

<!-- b000670 | heading | pages [22] -->
Appendix

<!-- b000671 | heading | pages [22] -->
13.1 Proof

<!-- b000672 | furniture | pages [22] -->
Page 21 of 20

<!-- b000673 | prose | pages [22] -->
Theorem: Mean waiting time of a (𝑀𝑀/𝑀𝑀/𝑘𝑘)  queueing is shorter than that of 𝑘𝑘  parallel

<!-- b000674 | prose | pages [22] -->
(𝑀𝑀/𝑀𝑀/1) queueing processes (Zeng, et al., 2011; Taha, 2014). Proof: Consider 𝑘𝑘 parallel (𝑀𝑀/𝑀𝑀/1) processes, input of each server is Poisson 𝜆𝜆/𝑘𝑘. The mean

<!-- b000675 | prose | pages [22] -->
queue length,

<!-- b000676 | prose | pages [22] -->
(1 −𝜌𝜌1)2 ⋅𝑃𝑃0,1, where 𝜌𝜌1 = 𝜆𝜆 𝜌𝜌1 𝐿𝐿𝑞𝑞,1 =

<!-- b000677 | furniture | pages [22] -->


<!-- b000678 | prose | pages [22] -->
𝑃𝑃0,1 = ¶1 +

<!-- b000679 | prose | pages [22] -->
𝑘𝑘𝑘𝑘

<!-- b000680 | prose | pages [22] -->
−1

<!-- b000681 | prose | pages [22] -->
𝜌𝜌1 𝜌𝜌1

<!-- b000682 | prose | pages [22] -->
= 1 −𝜌𝜌1

<!-- b000683 | prose | pages [22] -->
· 1 −𝜌𝜌1

<!-- b000684 | prose | pages [22] -->
Thus,

<!-- b000685 | prose | pages [22] -->
𝐿𝐿𝑞𝑞,1 =

<!-- b000686 | prose | pages [22] -->
And the mean waiting time (Little’s formula),

<!-- b000687 | prose | pages [22] -->
𝑊𝑊𝑞𝑞,1 = 𝐿𝐿𝑞𝑞,1

<!-- b000688 | prose | pages [22] -->
2

<!-- b000689 | prose | pages [22] -->
𝜌𝜌1

<!-- b000690 | furniture | pages [22] -->


<!-- b000691 | prose | pages [22] -->
1 −𝜌𝜌1

<!-- b000692 | prose | pages [22] -->
𝜌𝜌2 𝜌𝜌2

<!-- b000693 | prose | pages [22] -->
𝑘𝑘𝑘𝑘(1 −𝜌𝜌/𝑘𝑘) , where 𝜌𝜌= 𝜆𝜆

<!-- b000694 | prose | pages [22] -->
𝜆𝜆/𝑘𝑘=

<!-- b000695 | prose | pages [22] -->
𝜇𝜇

<!-- b000696 | prose | pages [22] -->
As for the (𝑀𝑀/𝑀𝑀/𝑘𝑘) process, the input is Poisson 𝜆𝜆.

<!-- b000697 | prose | pages [22] -->
𝜌𝜌𝑘𝑘+1

<!-- b000698 | prose | pages [22] -->
(𝑘𝑘−1)! (𝑘𝑘−𝜌𝜌)2 ⋅𝑃𝑃0,2

<!-- b000699 | prose | pages [22] -->
𝐿𝐿𝑞𝑞,2 =

<!-- b000700 | prose | pages [22] -->
𝑘𝑘−1

<!-- b000701 | prose | pages [22] -->
𝑃𝑃0,2 = ¹ 𝜌𝜌𝑛𝑛

<!-- b000702 | prose | pages [22] -->
𝑛𝑛!

<!-- b000703 | prose | pages [22] -->
𝑛𝑛=0

<!-- b000704 | prose | pages [22] -->
And thus,

<!-- b000705 | prose | pages [22] -->
𝜌𝜌𝑘𝑘+1 𝐿𝐿𝑞𝑞,2 =

<!-- b000706 | prose | pages [22] -->
(𝑘𝑘−1)! (𝑘𝑘−𝜌𝜌)2 ⋅

<!-- b000707 | prose | pages [22] -->
The mean waiting time is given by

<!-- b000708 | prose | pages [22] -->
𝜌𝜌𝑘𝑘+1

<!-- b000709 | prose | pages [22] -->
𝑊𝑊𝑞𝑞,2 = 𝐿𝐿𝑞𝑞,2

<!-- b000710 | prose | pages [22] -->
= 1

<!-- b000711 | prose | pages [22] -->
−1

<!-- b000712 | prose | pages [22] -->
+ 𝜌𝜌𝑘𝑘

<!-- b000713 | prose | pages [22] -->
1

<!-- b000714 | furniture | pages [22] -->


<!-- b000715 | prose | pages [22] -->
𝑘𝑘! ⋅ 1 −𝜌𝜌/𝑘𝑘º

<!-- b000716 | prose | pages [22] -->
1

<!-- b000717 | furniture | pages [22] -->


<!-- b000718 | prose | pages [22] -->
𝜌𝜌𝑛𝑛

<!-- b000719 | prose | pages [22] -->
+ 𝜌𝜌𝑘𝑘

<!-- b000720 | prose | pages [22] -->
1

<!-- b000721 | prose | pages [22] -->
𝑘𝑘−1

<!-- b000722 | prose | pages [22] -->
∑

<!-- b000723 | prose | pages [22] -->
𝑘𝑘! ⋅

<!-- b000724 | prose | pages [22] -->
𝑛𝑛!

<!-- b000725 | prose | pages [22] -->
1 −𝜌𝜌/𝑘𝑘

<!-- b000726 | prose | pages [22] -->
𝑛𝑛=0

<!-- b000727 | prose | pages [22] -->
1

<!-- b000728 | furniture | pages [22] -->


<!-- b000729 | prose | pages [22] -->
𝑘𝑘2(𝑘𝑘−1)! (1 −𝜌𝜌/𝑘𝑘)2 ⋅

<!-- b000730 | prose | pages [22] -->
𝜆𝜆⋅

<!-- b000731 | prose | pages [22] -->
𝜆𝜆

<!-- b000732 | prose | pages [22] -->
To prove that 𝑊𝑊𝑞𝑞,2 < 𝑊𝑊𝑞𝑞,1,

<!-- b000733 | prose | pages [22] -->
𝜌𝜌𝑘𝑘+1

<!-- b000734 | prose | pages [22] -->
⇔1

<!-- b000735 | prose | pages [22] -->
𝜆𝜆⋅

<!-- b000736 | prose | pages [22] -->
𝑘𝑘2(𝑘𝑘−1)! (1 −𝜌𝜌/𝑘𝑘)2 ⋅

<!-- b000737 | prose | pages [22] -->
𝑘𝑘−1

<!-- b000738 | prose | pages [22] -->
∑

<!-- b000739 | prose | pages [22] -->
𝑛𝑛=0

<!-- b000740 | prose | pages [22] -->
𝜌𝜌𝑘𝑘−1 ⇐

<!-- b000741 | prose | pages [22] -->
𝜌𝜌𝑛𝑛

<!-- b000742 | prose | pages [22] -->
𝑘𝑘−1

<!-- b000743 | prose | pages [22] -->
𝑘𝑘! ½∑

<!-- b000744 | prose | pages [22] -->
𝑛𝑛!

<!-- b000745 | prose | pages [22] -->
𝑛𝑛=0

<!-- b000746 | furniture | pages [22] -->


<!-- b000747 | furniture | pages [22] -->


<!-- b000748 | prose | pages [22] -->
𝜌𝜌𝑛𝑛

<!-- b000749 | prose | pages [22] -->
+ 𝜌𝜌𝑘𝑘

<!-- b000750 | prose | pages [22] -->
1

<!-- b000751 | prose | pages [22] -->
𝑘𝑘−1

<!-- b000752 | prose | pages [22] -->
∑

<!-- b000753 | prose | pages [22] -->
𝑘𝑘! ⋅

<!-- b000754 | prose | pages [22] -->
𝑛𝑛!

<!-- b000755 | prose | pages [22] -->
1 −𝜌𝜌/𝑘𝑘

<!-- b000756 | prose | pages [22] -->
𝑛𝑛=0

<!-- b000757 | prose | pages [22] -->
𝜌𝜌2

<!-- b000758 | prose | pages [22] -->
1

<!-- b000759 | prose | pages [22] -->
𝑘𝑘𝑘𝑘(1 −𝜌𝜌/𝑘𝑘)

<!-- b000760 | prose | pages [22] -->
<

<!-- b000761 | prose | pages [22] -->
𝜌𝜌𝑛𝑛

<!-- b000762 | prose | pages [22] -->
+ 𝜌𝜌𝑘𝑘

<!-- b000763 | prose | pages [22] -->
1 𝑘𝑘! ⋅

<!-- b000764 | prose | pages [22] -->
𝑛𝑛!

<!-- b000765 | prose | pages [22] -->
1 −𝜌𝜌/𝑘𝑘

<!-- b000766 | prose | pages [22] -->
< 1

<!-- b000767 | prose | pages [22] -->
𝑘𝑘 + 𝜌𝜌𝑘𝑘

<!-- b000768 | prose | pages [22] -->
1 −𝜌𝜌

<!-- b000769 | prose | pages [22] -->
𝑘𝑘!¾

<!-- b000770 | furniture | pages [23] -->
Team #67316

<!-- b000771 | prose | pages [23] -->
𝜌𝜌𝑘𝑘−1 ⇐

<!-- b000772 | prose | pages [23] -->
𝑘𝑘! ½0 + 𝜌𝜌𝑘𝑘

<!-- b000773 | furniture | pages [23] -->
Page 22 of 20

<!-- b000774 | prose | pages [23] -->
= 1

<!-- b000775 | prose | pages [23] -->
𝜌𝜌< 1

<!-- b000776 | prose | pages [23] -->
𝑘𝑘!¾

<!-- b000777 | prose | pages [23] -->
Since 𝜌𝜌= 𝜆𝜆/𝜇𝜇, generally we have 1 < 𝜌𝜌< 𝑘𝑘. It is true that 𝑊𝑊𝑞𝑞,2 < 𝑊𝑊𝑞𝑞,1 ∎

<!-- b000778 | heading | pages [23] -->
13.2 MATLAB Source Code for Simulation

<!-- b000779 | heading | pages [23] -->
13.2.1 simulation_simple.m

<!-- b000780 | prose | pages [23] -->
1 clc;

<!-- b000781 | prose | pages [23] -->
2 clear all;

<!-- b000782 | prose | pages [23] -->
3 load leave_time_ID;

<!-- b000783 | prose | pages [23] -->
4 load peo_num_ID

<!-- b000784 | prose | pages [23] -->
5 % load peo_num;%change comments

<!-- b000785 | prose | pages [23] -->
6 i=1;

<!-- b000786 | prose | pages [23] -->
7 x_k = 4;

<!-- b000787 | prose | pages [23] -->
8 x_mu = 1/28;

<!-- b000788 | prose | pages [23] -->
9 machine_number = 5;

<!-- b000789 | prose | pages [23] -->
10 % mean_arr = 12.9870/2.7;%0.077/10 %just influence the people number

<!-- b000790 | prose | pages [23] -->
11 % final_span = 3600*10;

<!-- b000791 | prose | pages [23] -->
12

<!-- b000792 | furniture | pages [23] -->


<!-- b000793 | prose | pages [23] -->
13 % peo_num = floor(span/mean_arr);%change comments

<!-- b000794 | prose | pages [23] -->
14 peo_num = peo_num_ID;

<!-- b000795 | prose | pages [23] -->
15

<!-- b000796 | furniture | pages [23] -->


<!-- b000797 | prose | pages [23] -->
16 % % generate the arrival intervals of people at airport randomly

<!-- b000798 | prose | pages [23] -->
17 % peo_in = exprnd(mean_arr,1,peo_num);

<!-- b000799 | prose | pages [23] -->
18 % actual_span = sum(peo_in);

<!-- b000800 | prose | pages [23] -->
19 % peo_in = peo_in.*(span/actual_span);

<!-- b000801 | prose | pages [23] -->
20 % peo_arr = cumsum(peo_in);

<!-- b000802 | prose | pages [23] -->
21

<!-- b000803 | furniture | pages [23] -->


<!-- b000804 | prose | pages [23] -->
22 % record_arr =

<!-- b000805 | prose | pages [23] -->
23 [leave_time_ID(1,:),leave_time_ID(2,:),leave_time_ID(3,:),leave_time_ID(4,:),leave_time_ID(5,:)];

<!-- b000806 | prose | pages [23] -->
24 record_arr = (leave_time_ID(:))';

<!-- b000807 | prose | pages [23] -->
25 record_arr(find(record_arr == 0)) = [];

<!-- b000808 | prose | pages [23] -->
26 record_arr = sort(record_arr);

<!-- b000809 | prose | pages [23] -->
27 peo_arr = record_arr;

<!-- b000810 | prose | pages [23] -->
28

<!-- b000811 | furniture | pages [23] -->


<!-- b000812 | prose | pages [23] -->
29 % %generate the service time of people at airport

<!-- b000813 | prose | pages [23] -->
30 % peo_serv = gamrnd(x_k,1/(x_k*x_mu),1,peo_num);

<!-- b000814 | prose | pages [23] -->
31

<!-- b000815 | furniture | pages [23] -->


<!-- b000816 | prose | pages [23] -->
32 %record the state of each security check point

<!-- b000817 | furniture | pages [23] -->


<!-- b000818 | furniture | pages [23] -->


<!-- b000819 | furniture | pages [24] -->
Team #67316

<!-- b000820 | furniture | pages [24] -->
Page 23 of 20

<!-- b000821 | prose | pages [24] -->
33 state = zeros(3*machine_number,peo_num);

<!-- b000822 | prose | pages [24] -->
34

<!-- b000823 | furniture | pages [24] -->


<!-- b000824 | prose | pages [24] -->
35 %initialize the time and intervals to leave in each array

<!-- b000825 | prose | pages [24] -->
36 leave_time = zeros(machine_number,peo_num);

<!-- b000826 | prose | pages [24] -->
37 leave_interval = zeros(machine_number,peo_num);%the time each person in arrays

<!-- b000827 | prose | pages [24] -->
38

<!-- b000828 | furniture | pages [24] -->


<!-- b000829 | prose | pages [24] -->
39 %initialize the number of people waited in each array

<!-- b000830 | prose | pages [24] -->
40 count = ones(1,machine_number);

<!-- b000831 | prose | pages [24] -->
41

<!-- b000832 | furniture | pages [24] -->


<!-- b000833 | prose | pages [24] -->
42 %initialize the person's data

<!-- b000834 | prose | pages [24] -->
43 for i = 1:machine_number

<!-- b000835 | prose | pages [24] -->
44 state(3*(i-1)+1,1) = peo_arr(i);

<!-- b000836 | prose | pages [24] -->
45 state(3*(i-1)+2,:) = gamrnd(x_k,1/(x_k*x_mu),1,peo_num);

<!-- b000837 | prose | pages [24] -->
46 state(3*i,1) = 0;

<!-- b000838 | prose | pages [24] -->
47

<!-- b000839 | furniture | pages [24] -->


<!-- b000840 | prose | pages [24] -->
48 leave_time(i,1) = sum(state(3*(i-1)+1 : 3*i , 1));%generate the leaving time of the first

<!-- b000841 | prose | pages [24] -->
49 person in each array

<!-- b000842 | prose | pages [24] -->
50 leave_interval(i,1) = sum(state(3*(i-1)+3:3*i,1));%generate the leaving intervals of the first

<!-- b000843 | prose | pages [24] -->
51 person in each array

<!-- b000844 | prose | pages [24] -->
52 end

<!-- b000845 | prose | pages [24] -->
53

<!-- b000846 | furniture | pages [24] -->


<!-- b000847 | prose | pages [24] -->
54 record_min = zeros(1,machine_number);

<!-- b000848 | prose | pages [24] -->
55 for i = machine_number+1 : peo_num

<!-- b000849 | prose | pages [24] -->
56

<!-- b000850 | furniture | pages [24] -->


<!-- b000851 | prose | pages [24] -->
57 for j = 1:machine_number

<!-- b000852 | prose | pages [24] -->
58 record_min(j) = leave_time(j,count(j));

<!-- b000853 | prose | pages [24] -->
59 end

<!-- b000854 | prose | pages [24] -->
60 [temp,min_array] = min(record_min);

<!-- b000855 | prose | pages [24] -->
61

<!-- b000856 | furniture | pages [24] -->


<!-- b000857 | prose | pages [24] -->
62 count(min_array) = count(min_array) + 1;

<!-- b000858 | prose | pages [24] -->
63 state(3*(min_array-1)+1 , count(min_array) ) = peo_arr(i);%let the people in the min_ array

<!-- b000859 | prose | pages [24] -->
64

<!-- b000860 | furniture | pages [24] -->


<!-- b000861 | prose | pages [24] -->
65 if state(3*(min_array-1)+1 , count(min_array) ) < state(3*(min_array-1)+2 , count(min_array)-

<!-- b000862 | prose | pages [24] -->
66 1 )...

<!-- b000863 | prose | pages [24] -->
67 +state(3*(min_array-1)+1 ,

<!-- b000864 | prose | pages [24] -->
68 count(min_array)-1 )...

<!-- b000865 | prose | pages [24] -->
69 +state(3*(min_array-1)+3 ,

<!-- b000866 | prose | pages [24] -->
70 count(min_array)-1 )

<!-- b000867 | prose | pages [24] -->
71

<!-- b000868 | furniture | pages [24] -->


<!-- b000869 | prose | pages [24] -->
72 state(3*(min_array) , count(min_array) ) = state(3*(min_array-1)+2 , count(min_array)-

<!-- b000870 | prose | pages [24] -->
73 1 )...

<!-- b000871 | furniture | pages [24] -->


<!-- b000872 | furniture | pages [24] -->


<!-- b000873 | furniture | pages [25] -->
Team #67316

<!-- b000874 | furniture | pages [25] -->
Page 24 of 20

<!-- b000875 | prose | pages [25] -->
74 +state(3*(min_array-1)+1 ,

<!-- b000876 | prose | pages [25] -->
75 count(min_array)-1 )...

<!-- b000877 | prose | pages [25] -->
76 +state(3*(min_array-1)+3 ,

<!-- b000878 | prose | pages [25] -->
77 count(min_array)-1 )...

<!-- b000879 | prose | pages [25] -->
78 -state(3*(min_array-1)+1 ,

<!-- b000880 | prose | pages [25] -->
79 count(min_array) );

<!-- b000881 | prose | pages [25] -->
80 else

<!-- b000882 | prose | pages [25] -->
81 state(3*(min_array) , count(min_array) ) = 0;

<!-- b000883 | prose | pages [25] -->
82 end

<!-- b000884 | prose | pages [25] -->
83

<!-- b000885 | furniture | pages [25] -->


<!-- b000886 | prose | pages [25] -->
84 leave_time(min_array,count(min_array)) = sum(state(3*(min_array-1)+1:3*min_array ,

<!-- b000887 | prose | pages [25] -->
85 count(min_array) ) );

<!-- b000888 | prose | pages [25] -->
86 leave_interval(min_array,count(min_array)) = sum(state(3*(min_array-1)+3:3*min_array ,

<!-- b000889 | prose | pages [25] -->
87 count(min_array) ) );

<!-- b000890 | prose | pages [25] -->
88 end

<!-- b000891 | prose | pages [25] -->
89

<!-- b000892 | furniture | pages [25] -->


<!-- b000893 | prose | pages [25] -->
90 total = 0;

<!-- b000894 | prose | pages [25] -->
91 for i = 1:size(leave_interval,1)

<!-- b000895 | prose | pages [25] -->
92 for j = 1:size(leave_interval,2)

<!-- b000896 | prose | pages [25] -->
93 if leave_interval(i,j) ~= 0

<!-- b000897 | prose | pages [25] -->
94 total = total + leave_interval(i,j);

<!-- b000898 | prose | pages [25] -->
95 end

<!-- b000899 | prose | pages [25] -->
96 end

<!-- b000900 | prose | pages [25] -->
97 end

<!-- b000901 | prose | pages [25] -->
98 means = total/peo_num;

<!-- b000902 | heading | pages [25] -->
13.2.2 simulation_tick.m

<!-- b000903 | prose | pages [25] -->
1 clc;

<!-- b000904 | prose | pages [25] -->
2 clear all;

<!-- b000905 | prose | pages [25] -->
3 load change2;

<!-- b000906 | prose | pages [25] -->
4

<!-- b000907 | furniture | pages [25] -->


<!-- b000908 | prose | pages [25] -->
5 x_k = 4;

<!-- b000909 | prose | pages [25] -->
6 x_mu = 1/28;

<!-- b000910 | prose | pages [25] -->
7

<!-- b000911 | furniture | pages [25] -->


<!-- b000912 | prose | pages [25] -->
8 mean_serv = 10.5652;

<!-- b000913 | prose | pages [25] -->
9 machine_number = 5;

<!-- b000914 | prose | pages [25] -->
10

<!-- b000915 | furniture | pages [25] -->


<!-- b000916 | prose | pages [25] -->
11 peo_arr = change2(2,:).*60;

<!-- b000917 | prose | pages [25] -->
12 peo_fli = change2(1,:).*60;

<!-- b000918 | prose | pages [25] -->
13 peo_num = size(change2,2);

<!-- b000919 | furniture | pages [25] -->


<!-- b000920 | furniture | pages [25] -->


<!-- b000921 | furniture | pages [26] -->
Team #67316

<!-- b000922 | furniture | pages [26] -->
Page 25 of 20

<!-- b000923 | prose | pages [26] -->
14

<!-- b000924 | furniture | pages [26] -->


<!-- b000925 | prose | pages [26] -->
15 state = zeros(4*machine_number,peo_num);

<!-- b000926 | prose | pages [26] -->
16 %the first row is the flight time of each passenger

<!-- b000927 | prose | pages [26] -->
17 %the second row is the arrival time of each passenger

<!-- b000928 | prose | pages [26] -->
18 %the third row is the service time of each passenger

<!-- b000929 | prose | pages [26] -->
19 %the fourth row is the waiting time of each passenger

<!-- b000930 | prose | pages [26] -->
20

<!-- b000931 | furniture | pages [26] -->


<!-- b000932 | prose | pages [26] -->
21 leave_time = zeros(machine_number,peo_num);

<!-- b000933 | prose | pages [26] -->
22 wait_time = zeros(machine_number,peo_num);

<!-- b000934 | prose | pages [26] -->
23

<!-- b000935 | furniture | pages [26] -->


<!-- b000936 | prose | pages [26] -->
24 %initialize the state matrix

<!-- b000937 | prose | pages [26] -->
25 for i = 1:machine_number

<!-- b000938 | prose | pages [26] -->
26 state(4*(i-1)+1,1) = peo_fli(i);

<!-- b000939 | prose | pages [26] -->
27 state(4*(i-1)+2,1) = peo_arr(i);

<!-- b000940 | prose | pages [26] -->
28 %     state(4*(i-1)+3,:) = exprnd(mean_serv,1,peo_num);%service times of each machine in

<!-- b000941 | prose | pages [26] -->
29 expoential distribution

<!-- b000942 | prose | pages [26] -->
30 state(4*(i-1)+3,:) = gamrnd(x_k,1/(x_k*x_mu),1,peo_num);

<!-- b000943 | prose | pages [26] -->
31 state(4*(i-1)+4,1) = 0;

<!-- b000944 | prose | pages [26] -->
32

<!-- b000945 | furniture | pages [26] -->


<!-- b000946 | prose | pages [26] -->
33 leave_time(i,1) = sum(state(4*(i-1)+2 : 4*i ,1));

<!-- b000947 | prose | pages [26] -->
34 wait_time(i,1) = state(4*i,1);

<!-- b000948 | prose | pages [26] -->
35 end

<!-- b000949 | prose | pages [26] -->
36

<!-- b000950 | furniture | pages [26] -->


<!-- b000951 | prose | pages [26] -->
37 count = ones(1,machine_number);%record the array length of each machine

<!-- b000952 | prose | pages [26] -->
38

<!-- b000953 | furniture | pages [26] -->


<!-- b000954 | prose | pages [26] -->
39 queue = zeros(1,peo_num);

<!-- b000955 | prose | pages [26] -->
40 front = 1;

<!-- b000956 | prose | pages [26] -->
41 rear = 1;

<!-- b000957 | prose | pages [26] -->
42

<!-- b000958 | furniture | pages [26] -->


<!-- b000959 | prose | pages [26] -->
43 scanning = machine_number+1;

<!-- b000960 | prose | pages [26] -->
44

<!-- b000961 | furniture | pages [26] -->


<!-- b000962 | prose | pages [26] -->
45 record_min = zeros(1,machine_number);

<!-- b000963 | prose | pages [26] -->
46 for j = 1:machine_number

<!-- b000964 | prose | pages [26] -->
47 record_min(j) = leave_time(j,count(j));

<!-- b000965 | prose | pages [26] -->
48 end

<!-- b000966 | prose | pages [26] -->
49 [min_time,min_array] = min(record_min);

<!-- b000967 | prose | pages [26] -->
50

<!-- b000968 | furniture | pages [26] -->


<!-- b000969 | prose | pages [26] -->
51 % %push the next person into queue

<!-- b000970 | prose | pages [26] -->
52 % queue(rear) = scanning;

<!-- b000971 | prose | pages [26] -->
53 % rear = rear + 1;

<!-- b000972 | prose | pages [26] -->
54 % scanning = scanning+1;

<!-- b000973 | furniture | pages [26] -->


<!-- b000974 | furniture | pages [26] -->


<!-- b000975 | furniture | pages [27] -->
Team #67316

<!-- b000976 | furniture | pages [27] -->
Page 26 of 20

<!-- b000977 | prose | pages [27] -->
55

<!-- b000978 | furniture | pages [27] -->


<!-- b000979 | prose | pages [27] -->
56 for tick = floor(peo_arr(1)):floor(peo_fli(length(peo_fli)))

<!-- b000980 | prose | pages [27] -->
57 if tick > peo_arr(scanning) && scanning < peo_num%push the latest person into queue

<!-- b000981 | prose | pages [27] -->
58 queue(rear) = scanning;

<!-- b000982 | prose | pages [27] -->
59 rear = rear + 1;

<!-- b000983 | prose | pages [27] -->
60 %         if rear > front

<!-- b000984 | prose | pages [27] -->
61 %             temp_queue = queue(front:rear - 1);

<!-- b000985 | prose | pages [27] -->
62 %             [temp_record,temp_order] = sort(peo_fli(temp_queue));

<!-- b000986 | prose | pages [27] -->
63 %             queue(front:rear-1) = temp_queue(temp_order);

<!-- b000987 | prose | pages [27] -->
64 %         end

<!-- b000988 | prose | pages [27] -->
65

<!-- b000989 | furniture | pages [27] -->


<!-- b000990 | prose | pages [27] -->
66 scanning = scanning + 1;

<!-- b000991 | prose | pages [27] -->
67 end

<!-- b000992 | prose | pages [27] -->
68

<!-- b000993 | furniture | pages [27] -->


<!-- b000994 | prose | pages [27] -->
69 %     if peo_arr(queue(front)) < min_time

<!-- b000995 | prose | pages [27] -->
70 if tick > min_time

<!-- b000996 | prose | pages [27] -->
71 if rear > front % the queue is not empty

<!-- b000997 | prose | pages [27] -->
72 count(min_array) = count(min_array) + 1;

<!-- b000998 | prose | pages [27] -->
73 state(4*(min_array-1)+1 , count(min_array) ) = peo_fli(queue(front));

<!-- b000999 | prose | pages [27] -->
74 state(4*(min_array-1)+2 , count(min_array) ) = peo_arr(queue(front));

<!-- b001000 | prose | pages [27] -->
75 state(4*(min_array-1)+4 , count(min_array) ) = max( min_time - peo_arr(queue(front)) ,

<!-- b001001 | prose | pages [27] -->
76 0);

<!-- b001002 | prose | pages [27] -->
77

<!-- b001003 | furniture | pages [27] -->


<!-- b001004 | prose | pages [27] -->
78 leave_time( min_array,count(min_array) ) = sum(state(4*(min_array-1)+2 :

<!-- b001005 | prose | pages [27] -->
79 4*(min_array) ,count(min_array)));

<!-- b001006 | prose | pages [27] -->
80 wait_time( min_array,count(min_array) ) =

<!-- b001007 | prose | pages [27] -->
81 state(4*(min_array),count(min_array));%update the leave time

<!-- b001008 | prose | pages [27] -->
82

<!-- b001009 | furniture | pages [27] -->


<!-- b001010 | prose | pages [27] -->
83 front = front + 1;%pop the prior person to serve

<!-- b001011 | prose | pages [27] -->
84

<!-- b001012 | furniture | pages [27] -->


<!-- b001013 | prose | pages [27] -->
85 for j = 1:machine_number

<!-- b001014 | prose | pages [27] -->
86 record_min(j) = leave_time(j,count(j));

<!-- b001015 | prose | pages [27] -->
87 end

<!-- b001016 | prose | pages [27] -->
88 [min_time,min_array] = min(record_min);%update the min_time and the min_array

<!-- b001017 | prose | pages [27] -->
89

<!-- b001018 | furniture | pages [27] -->


<!-- b001019 | prose | pages [27] -->
90 end

<!-- b001020 | prose | pages [27] -->
91

<!-- b001021 | furniture | pages [27] -->


<!-- b001022 | prose | pages [27] -->
92 end

<!-- b001023 | prose | pages [27] -->
93

<!-- b001024 | furniture | pages [27] -->


<!-- b001025 | prose | pages [27] -->
94 end

<!-- b001026 | prose | pages [27] -->
95

<!-- b001027 | furniture | pages [27] -->


<!-- b001028 | furniture | pages [27] -->


<!-- b001029 | furniture | pages [27] -->


<!-- b001030 | furniture | pages [28] -->
Team #67316

<!-- b001031 | furniture | pages [28] -->
Page 27 of 20

<!-- b001032 | prose | pages [28] -->
96 total = 0;

<!-- b001033 | prose | pages [28] -->
97 flag = 0;

<!-- b001034 | prose | pages [28] -->
98 for i = 1:machine_number

<!-- b001035 | prose | pages [28] -->
99 for j = 1:count(i)

<!-- b001036 | prose | pages [28] -->
100 total = total + state(4*(i-1)+1,j)-state(4*(i-1)+2,j)-state(4*(i-1)+3,j)-state(4*i,j);

<!-- b001037 | prose | pages [28] -->
101 if state(4*(i-1)+1,j)-state(4*(i-1)+2,j)-state(4*(i-1)+3,j)-state(4*i,j) < 0

<!-- b001038 | prose | pages [28] -->
102 flag = flag + 1;

<!-- b001039 | prose | pages [28] -->
103 end

<!-- b001040 | prose | pages [28] -->
104 end

<!-- b001041 | prose | pages [28] -->
105 end

<!-- b001042 | prose | pages [28] -->
106 means = total / peo_num;

<!-- b001043 | prose | pages [28] -->
107

<!-- b001044 | furniture | pages [28] -->


<!-- b001045 | prose | pages [28] -->
108 summation = 0;

<!-- b001046 | prose | pages [28] -->
109 for i = 1:machine_number

<!-- b001047 | prose | pages [28] -->
110 for j = 1:count(i)

<!-- b001048 | prose | pages [28] -->
111 summation = summation + (state(4*(i-1)+1,j)-state(4*(i-1)+2,j)-state(4*(i-1)+3,j)-

<!-- b001049 | prose | pages [28] -->
112 state(4*i,j)-means)^2;

<!-- b001050 | prose | pages [28] -->
113 end

<!-- b001051 | prose | pages [28] -->
114 end

<!-- b001052 | prose | pages [28] -->
115 variance = summation / peo_num;

<!-- b001053 | heading | pages [28] -->
13.2.3 stream.m

<!-- b001054 | prose | pages [28] -->
1 function [ total ] = stream( pretime, variance,people)

<!-- b001055 | prose | pages [28] -->
2 %UNTITLED

<!-- b001056 | prose | pages [28] -->
3 % original:pretime=120,variance=30,people=189

<!-- b001057 | prose | pages [28] -->
4 a=[-3*variance:1:3*variance];

<!-- b001058 | prose | pages [28] -->
5 a=[a;a];

<!-- b001059 | prose | pages [28] -->
6 a(2,1)=normcdf(a(1,1),0,variance)*people;

<!-- b001060 | prose | pages [28] -->
7 for i=2:6*variance+1

<!-- b001061 | prose | pages [28] -->
8 a(2,i)=normcdf(a(1,i),0,variance)-normcdf(a(1,i-1),0,variance);

<!-- b001062 | prose | pages [28] -->
9 a(2,i)=a(2,i)*people;

<!-- b001063 | prose | pages [28] -->
10 end

<!-- b001064 | prose | pages [28] -->
11 data=xlsread('data',2);

<!-- b001065 | prose | pages [28] -->
12 siz=size(data);

<!-- b001066 | prose | pages [28] -->
13 dataset=[];

<!-- b001067 | prose | pages [28] -->
14 data=data*24*60;

<!-- b001068 | prose | pages [28] -->
15 for i=1:siz(1,1)

<!-- b001069 | prose | pages [28] -->
16 for j=1:siz(1,2)

<!-- b001070 | prose | pages [28] -->
17 if data(i,j)>0

<!-- b001071 | prose | pages [28] -->
18 dataset=[dataset,data(i,j)];

<!-- b001072 | furniture | pages [28] -->


<!-- b001073 | furniture | pages [28] -->


<!-- b001074 | furniture | pages [29] -->
Team #67316

<!-- b001075 | furniture | pages [29] -->
Page 28 of 20

<!-- b001076 | prose | pages [29] -->
19 end

<!-- b001077 | prose | pages [29] -->
20 end

<!-- b001078 | prose | pages [29] -->
21 end

<!-- b001079 | prose | pages [29] -->
22 siz=size(dataset);

<!-- b001080 | prose | pages [29] -->
23 total=zeros(1,1440);

<!-- b001081 | prose | pages [29] -->
24 for i=1:siz(1,2)

<!-- b001082 | prose | pages [29] -->
25 for j=1:variance*6+1

<!-- b001083 | prose | pages [29] -->
26 if dataset(1,i)-pretime+a(1,j)>=1

<!-- b001084 | prose | pages [29] -->
27 total(1,round(dataset(1,i)-pretime+a(1,j)))=total(1,round(dataset(1,i)-

<!-- b001085 | prose | pages [29] -->
28 pretime+a(1,j)))+a(2,j);

<!-- b001086 | prose | pages [29] -->
29 end

<!-- b001087 | prose | pages [29] -->
30 end

<!-- b001088 | prose | pages [29] -->
31 end

<!-- b001089 | prose | pages [29] -->
32 end

<!-- b001090 | heading | pages [29] -->
13.2.4 stream2.m

<!-- b001091 | prose | pages [29] -->
1 function [ total ] = stream( pretime, variance,people)

<!-- b001092 | prose | pages [29] -->
2 %UNTITLED

<!-- b001093 | prose | pages [29] -->
3 % original:pretime=120,variance=30,people=189

<!-- b001094 | prose | pages [29] -->
4 a=[-3*variance:1:3*variance];

<!-- b001095 | prose | pages [29] -->
5 a=[a;a];

<!-- b001096 | prose | pages [29] -->
6 a(2,1)=normcdf(a(1,1),0,variance)*people;

<!-- b001097 | prose | pages [29] -->
7 for i=2:6*variance+1

<!-- b001098 | prose | pages [29] -->
8 a(2,i)=normcdf(a(1,i),0,variance)-normcdf(a(1,i-1),0,variance);

<!-- b001099 | prose | pages [29] -->
9 a(2,i)=a(2,i)*people;

<!-- b001100 | prose | pages [29] -->
10 end

<!-- b001101 | prose | pages [29] -->
11 data=xlsread('data',2);

<!-- b001102 | prose | pages [29] -->
12 siz=size(data);

<!-- b001103 | prose | pages [29] -->
13 dataset=[];

<!-- b001104 | prose | pages [29] -->
14 data=data*24*60;

<!-- b001105 | prose | pages [29] -->
15 for i=1:siz(1,1)

<!-- b001106 | prose | pages [29] -->
16 for j=1:siz(1,2)

<!-- b001107 | prose | pages [29] -->
17 if data(i,j)>0

<!-- b001108 | prose | pages [29] -->
18 dataset=[dataset,data(i,j)];

<!-- b001109 | prose | pages [29] -->
19 end

<!-- b001110 | prose | pages [29] -->
20 end

<!-- b001111 | prose | pages [29] -->
21 end

<!-- b001112 | prose | pages [29] -->
22 siz=size(dataset);

<!-- b001113 | prose | pages [29] -->
23 total=zeros(1,1440);

<!-- b001114 | prose | pages [29] -->
24 for i=1:siz(1,2)

<!-- b001115 | furniture | pages [29] -->


<!-- b001116 | furniture | pages [29] -->


<!-- b001117 | furniture | pages [30] -->
Team #67316

<!-- b001118 | furniture | pages [30] -->
Page 29 of 20

<!-- b001119 | prose | pages [30] -->
25 for j=1:variance*6+1

<!-- b001120 | prose | pages [30] -->
26 if dataset(1,i)-pretime+a(1,j)>=1

<!-- b001121 | prose | pages [30] -->
27 total(1,round(dataset(1,i)-pretime+a(1,j)))=total(1,round(dataset(1,i)-

<!-- b001122 | prose | pages [30] -->
28 pretime+a(1,j)))+a(2,j);

<!-- b001123 | prose | pages [30] -->
29 end

<!-- b001124 | prose | pages [30] -->
30 end

<!-- b001125 | prose | pages [30] -->
31 end

<!-- b001126 | prose | pages [30] -->
32 end

<!-- b001127 | furniture | pages [30] -->


<!-- b001128 | furniture | pages [30] -->


<!-- b001129 | furniture | pages [30] -->


<!-- b001130 | furniture | pages [30] -->

