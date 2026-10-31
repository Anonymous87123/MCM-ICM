# P-D-2017-67316-f37f83c8

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only 67316 T1 ________________ F1 ________________ T2 ________________ F2 ________________ Problem Chosen T3 ________________ F3 ________________

<!-- b000003 | front_matter | pages [1] -->
D

<!-- b000004 | front_matter | pages [1] -->
T4 ________________ F4 ________________

<!-- b000005 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Bottlenecks that passengers take time to take care of their carry-on properties before X-ray scanning and that the structure of the checkpoints is not satisfying are spotted, and detailed recommendations for the airport security management to raise throughput of the security checkpoints, to improve the passengers’ satisfaction and to keep the cost relatively low are given with cultural factors quantiﬁed and their impacts on the models discussed.

<!-- b000010 | prose | pages [1] -->
We divided the security check process into two phases and regard the entire as two queueing models in series. By analyzing the given data, the document check is found to be a Poisson queueing (𝑀𝑀/𝑀𝑀/𝑐𝑐) in Kendall notation, and Erlangian process (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐) is concerned in the scan check process. Numeric solution of (𝑴𝑴/𝑬𝑬𝒌𝒌/𝒄𝒄) is introduced using simulation tech- nique.

<!-- b000011 | prose | pages [1] -->
Assumed that arrivals of passengers for a ﬂight obey normal distribution, the varying passenger ﬂow in a period of time can be generated from the real data and used for our sim- ulation. We also believe that the mean 𝜇𝜇 and the variance 𝜎𝜎􏷡􏷡 of the distribution is culture-re- lated. We also ﬁnd that the passenger ﬂow can be changed by recommending the passengers their arrivals, and thus better result of the passengers’ waiting time can be achieved.

<!-- b000012 | prose | pages [1] -->
We also suggested several methods to improve the design of the checkpoint, including shortening the distances between identical checkpoints and more rational human resource allocation.

<!-- b000013 | prose | pages [1] -->
Virtual queueing is recommended as an approach to improve passengers’ experience, and modify the conventional First In First Service queueing discipline to partial priority queueing discipline as well. A partial priority queueing discipline is put forward to reduce the remaining time variance of the passengers and to decrease the number of passengers that missed their ﬂights, thus better passenger satisfaction is reached.

<!-- b000014 | prose | pages [1] -->
We also introduced culture-related factors for passenger arrival recommendation and pri- ority queueing discipline. For the latter, an “acceptability factor” named 𝛼𝛼 is used to denote the acceptability of strict priority discipline. And the examples of diﬀerent cultures are given to illustrate this idea.

<!-- b000015 | prose | pages [1] -->
Validation of each model are made in our essay to make them convincing. We later assess the models and give a complete guide for the security managers to optimize the airport secu- rity check workﬂow. Weaknesses and further work that is not implemented in our essay are also pointed out.

<!-- b000016 | furniture | pages [2] -->
Team #67316

<!-- b000017 | furniture | pages [2] -->
Page 1 of 20

<!-- b000018 | prose | pages [2] -->
Time Counts! Less Waiting & Better Airports

<!-- b000019 | heading | pages [2] -->
Introduction

<!-- b000020 | heading | pages [2] -->
1.1 Background

<!-- b000021 | prose | pages [2] -->
Airport security check has been improved ever since the 911 attack. Although enhanced secu- rity means safer ﬂights, however the complicated procedure may also increase the passengers’ waiting time and add cost to the U.S. Transportation Security Agency (TSA). Under some extreme circumstances, passengers have to wait for hours (and they are often recommended to be earlier for 2–3 hours, which often lead to confusion) (Hetter, 2016). Thus, to shorten the passengers’ waiting and designing a more eﬃcient security check procedure is vitally important.

<!-- b000022 | prose | pages [2] -->
TSA is now in controversy for causing long queues waiting for security check. We, the Internal Control Management (ICM) team, trying to ﬁnd a solution, faces the problems below:

<!-- b000023 | prose | pages [2] -->
1. Identify the bottlenecks of the current security check workﬂow.

<!-- b000024 | prose | pages [2] -->
2. Improve the process with modiﬁcations, and illustrate how the modiﬁcations work.

<!-- b000025 | prose | pages [2] -->
3. Find how to allow the modiﬁed process to be compatible with diﬀerent culture back- grounds and lower the variance of the passengers’ waiting time.

<!-- b000026 | prose | pages [2] -->
4. Make suggestions on the policy for the security manager, with concern of the former requirements and corresponding models.

<!-- b000027 | heading | pages [2] -->
1.2 Analysis and Approach Overview

<!-- b000028 | prose | pages [2] -->
For problem 1, we divide the security check process in two parts: Phase 1, document check; and Phase 2, luggage and body scanning. The former is a Poisson queue, while the latter concerns an Erlangian model. Simulation is practiced as a means of solving multi-server Er- langian model. By testing the total waiting time’s sensitivity to changes on numbers of parallel servers in the two phases respectively, the bottlenecks of the workﬂow can be spotted.

<!-- b000029 | prose | pages [2] -->
To solve problem 2, considering the inﬂuential factors of a queueing process, modiﬁcations will be put forward to optimize and avoid congestions.

<!-- b000030 | prose | pages [2] -->
The current TSA recommended passengers’ arrival time is used to build a model of the passenger arrival behavior at an airport, and we assume the arrivals in time for one certain ﬂight obey normal distribution, and in a small time interval, the arrivals of all passengers for all ﬂights obey an exponential distribution. We will modify the arrival recommendation strat- egy to inﬂuence passengers’ arrival behavior.

<!-- b000031 | prose | pages [2] -->
Another direction to improve the current process is to provide more robust security check service with greater capacity. A few suggestions and their veriﬁcation or explanation will be given.

<!-- b000032 | furniture | pages [3] -->
Team #67316

<!-- b000033 | furniture | pages [3] -->
Page 2 of 20

<!-- b000034 | prose | pages [3] -->
Besides the performance, justiﬁability also counts. Virtual queueing under other disciplines (Zhao, et al., 2016) will be a good practice. Queueing discipline modiﬁcation is culture-sensitive, and thus lead to the discussion of the third problem.

<!-- b000035 | prose | pages [3] -->
The following diagram illustrate the above ideas in a more visual way:

<!-- b000036 | caption | pages [3] -->
Figure 1 Optimizing directions and our modiﬁcations,

<!-- b000037 | prose | pages [3] -->
where “service pattern” concerns the service rate and number of servers.

<!-- b000038 | heading | pages [3] -->
Assumptions

<!-- b000039 | prose | pages [3] -->
1. Individual variability is not considered for the servers, the checkpoint structures, etc.

<!-- b000040 | prose | pages [3] -->
2. Although the number of lanes opened in the scan check process is dynamic, we assume that the service capability is always at its maximum. That is to say, spare lanes will be open, so long as the arrival exceeds the current capability.

<!-- b000041 | prose | pages [3] -->
3. Assume that every passenger will choose to wait in the queue that minimizes their waiting time at every checkpoint.

<!-- b000042 | prose | pages [3] -->
4. Points in time that passengers arrive at the airport for a certain ﬂight obey normal distribution.

<!-- b000043 | prose | pages [3] -->
5. TSA Pre-check won’t contribute much to the congestion compared with the normal one.

<!-- b000044 | prose | pages [3] -->
6. Almost everyone would arrive at the airport for at least half an hour.

<!-- b000045 | prose | pages [3] -->
See 4.1 Security Check Process—Overview, and 4.3 Queueing Model Speciﬁcation for de- tailed interpretation and assumptions of the given datasheet.

<!-- b000046 | heading | pages [3] -->
Symbols and Notations

<!-- b000047 | heading | pages [3] -->
Symbol or Notation

<!-- b000048 | prose | pages [3, 4] -->
Speciﬁcation Kendall notation, where 𝑎𝑎, 𝑏𝑏, 𝑐𝑐, 𝑑𝑑, 𝑒𝑒  and 𝑓𝑓  denote the inter-arrival-time (𝑎𝑎/𝑏𝑏/𝑐𝑐): (𝑑𝑑/𝑒𝑒/𝑓𝑓) distribution, the service time distribution, the number of parallel servers, queueing discipline, restriction on system capacity, and the source of the arrival (usually inﬁnity) respectively. (Taha, 2014) Denote an exponential distribution for inter-arrival time and service time, 𝑀𝑀 i.e. a Poisson distribution for arrival and remove rate.

<!-- b000049 | furniture | pages [4] -->
Team #67316

<!-- b000050 | furniture | pages [4] -->
Page 3 of 20

<!-- b000052 | prose | pages [4] -->
𝐸𝐸𝑘𝑘 Erlang distribution type 𝑘𝑘.

<!-- b000053 | prose | pages [4] -->
𝑥𝑥̂ Estimated value of 𝑥𝑥.

<!-- b000054 | prose | pages [4] -->
𝜆𝜆𝑑𝑑, 𝜇𝜇𝑑𝑑 Arrival and service rates of the document check process.

<!-- b000055 | prose | pages [4] -->
𝜆𝜆𝑠𝑠, 𝜇𝜇𝑠𝑠 Arrival and service rates of the scan check process.

<!-- b000056 | prose | pages [4] -->
∞ Γ(𝛼𝛼) Γ(𝛼𝛼) =  𝑥𝑥𝛼𝛼−1e−𝑥𝑥d𝑥𝑥 0 𝑁𝑁(𝜇𝜇, 𝜎𝜎2) Normal distribution with mean 𝜇𝜇, and variance 𝜎𝜎2.

<!-- b000057 | heading | pages [4] -->
Queueing Model for Security Check Process

<!-- b000058 | prose | pages [4] -->
4.1 Security Check Process------Overview

<!-- b000059 | caption | pages [4] -->
Figure 2 TSA Security checkpoint

<!-- b000060 | prose | pages [4] -->
The detailed security check process of one single checkpoint given in the diagram above. Ac- cording to TSA’s policy, we classify the security processes in two types (pre-check included and no pre-check concerned process), and divide the each process in two queueing phases. In Phase 1, the passengers’ identity documents will be checked, after which they enter Phase 2, where luggage and body screening will be accepted. Two diﬀerent types are in essence the same queueing with diﬀerent parameters (number of servers, service time, etc.). And the entire security check process can be seen as two queueing models in series.

<!-- b000061 | prose | pages [4] -->
To better clarify the whole process, a procedure sequence diagram is given below:

<!-- b000062 | furniture | pages [5] -->
Team #67316

<!-- b000063 | furniture | pages [5] -->
Page 4 of 20

<!-- b000064 | heading | pages [5] -->
C D

<!-- b000065 | prose | pages [5] -->
A B E

<!-- b000066 | prose | pages [5] -->
F G H

<!-- b000067 | caption | pages [5] -->
Figure 3 Procedure sequence diagram

<!-- b000068 | prose | pages [5] -->
A: time waiting for the document check, B: document checking time C: time waiting for sending luggage for X-ray scanning, D: X-ray scanning time, E: other possible luggage checks F: time waiting for millimeter wave scan, G: body scan time, H: other possible body checks The yellow shaded part is Phase 1 as we introduced in previous paragraphs, and the rest Phase 2.

<!-- b000069 | prose | pages [5] -->
The given Excel datasheet contains time records of the airport checkpoints (whose diﬀer- ences denote the inter-arrival time), time taken of the ID check process of previous checked passenger (i.e. B in the diagram), millimeter wave scan timestamps (diﬀerences of which are the millimeter wave scanning time, shown as G in the diagram), timestamps that luggage getting out of the X-ray scan (diﬀerences denote E), and time to get scanned property (D, E, F, G, H).

<!-- b000070 | prose | pages [5] -->
By analyzing the given datasheet, patterns of the airport security check behaviors, such as the distribution of passengers’ inter-arrival time and service time at each section, can be dis- covered. Therefore a complete queueing model can be speciﬁed.

<!-- b000071 | heading | pages [5] -->
4.2 Significance Test on Two TSA Officers

<!-- b000072 | prose | pages [5] -->
The given datasheet involves timing of two diﬀerent TSA oﬃcers, the signiﬁcance test here is to verify that individual variability does not contribute much to the service time.

<!-- b000073 | prose | pages [5] -->
2 = 𝜎𝜎2 2 = 𝜎𝜎2. Suppose that variances of the service time of the two TSA oﬃcers are equal, 𝜎𝜎1 We make the null hypothesis 𝐻𝐻0 that service time expectations of both oﬃcers are the same, i.e. 𝜇𝜇1 = 𝜇𝜇2.

<!-- b000074 | prose | pages [5] -->
2 = 12.927. The combined sample variance of the two oﬃcers, 𝑠𝑠𝑤𝑤 At 5% level, 𝑠𝑠𝑤𝑤 1/𝑛𝑛1+1/𝑛𝑛2 = 1.375 ≤𝑡𝑡0.025(14) = 2.145, the null hypothesis is not rejected. |𝑥𝑥1 −𝑥𝑥2 |

<!-- b000075 | prose | pages [5] -->
Assume that the document check service time obeys the exponential distribution. The pa- rameter of the distribution, i.e. service rate, is estimated, 𝜇𝜇𝑑𝑑 = 0.09465.

<!-- b000076 | heading | pages [5] -->
4.3 Queueing Model Specification

<!-- b000077 | prose | pages [5] -->
The two phases of the process can be speciﬁed as a series of queues by giving the arrival and service time distribution pattern.

<!-- b000078 | furniture | pages [6] -->
Team #67316

<!-- b000079 | furniture | pages [6] -->
Page 5 of 20

<!-- b000080 | heading | pages [6] -->
4.3.1 Arrival

<!-- b000081 | prose | pages [6] -->
30 20 25 15 20

<!-- b000082 | prose | pages [6] -->
15 10

<!-- b000083 | prose | pages [6] -->
10 5 5

<!-- b000084 | prose | pages [6] -->
0 0 0 10 20 30 40 50 0 20 40 60 80

<!-- b000085 | caption | pages [6] -->
Figure 4 Frequency histogram of non-pre-check arrivals

<!-- b000086 | caption | pages [6] -->
Figure 5 Frequency histogram of pre-check arrivals

<!-- b000087 | prose | pages [6] -->
According to the histograms above, we suppose that the time intervals of both the regular and pre-check arrivals obey exponential distribution 𝑓𝑓(𝑥𝑥) = 𝜆𝜆𝑑𝑑e−𝜆𝜆𝑑𝑑𝑥𝑥.

<!-- b000088 | prose | pages [6] -->
Maximum likelihood estimation of the parameter 𝜆𝜆𝑑𝑑:

<!-- b000089 | prose | pages [6] -->
𝑛𝑛 𝑛𝑛 𝑛𝑛 𝑛𝑛e−𝜆𝜆𝑑𝑑∑ 𝑥𝑥𝑖𝑖 =  𝜆𝜆𝑑𝑑e−𝜆𝜆𝑑𝑑𝑥𝑥𝑖𝑖 𝐿𝐿(𝜆𝜆𝑑𝑑) =  𝑓𝑓(𝑥𝑥𝑖𝑖) = 𝜆𝜆𝑑𝑑 𝑖𝑖=1 𝑖𝑖=1 𝑖𝑖=1 𝑛𝑛 𝑛𝑛 , d ln 𝐿𝐿(𝜆𝜆𝑑𝑑) = 𝑛𝑛 = 0 ln 𝐿𝐿(𝜆𝜆𝑑𝑑) = 𝑛𝑛ln 𝜆𝜆𝑑𝑑−𝜆𝜆𝑑𝑑 𝑥𝑥𝑖𝑖 − 𝑥𝑥𝑖𝑖 d𝜆𝜆𝑑𝑑 𝜆𝜆𝑑𝑑 𝑖𝑖=1 𝑖𝑖=1 Therefore 𝜆𝜆𝑑𝑑 , and the expectation, 𝐸𝐸𝜆𝜆𝑑𝑑 𝐸𝐸(𝑥𝑥) = 𝜆𝜆𝑑𝑑, is an unbi- =  = 𝐸𝐸 1 𝑛𝑛 = 1 1  = 𝑛𝑛 𝑥𝑥𝚤𝚤 𝑥𝑥𝚤𝚤 ∑ 𝑥𝑥𝑖𝑖 𝑖𝑖=1 ased estimation. Thus the arrival rates of the regular and pre-check procedures are estimated to be 𝜆𝜆1 = 0.077244 and 𝜆𝜆2 = 0.10882016, respectively.

<!-- b000090 | prose | pages [6] -->
Here, a goodness of ﬁt test is done, and each of the procedures are classiﬁed into 10 classes. Let’s take the regular (without pre-check) procedure as an example:

<!-- b000091 | prose | pages [6] -->
Class 0-8 8-16 16-24 24-32 32-40 40-48 48-56 56-64 64-72 72-80 True Frequency 21 13 6 3 0 0 1 1 0 1 Predicted Probability 0.461 0.248 0.134  0.072  0.039  0.021  0.011  0.006  0.003  0.002 Predicted Frequency 21.204  11.430  6.161  3.321  1.790  0.965  0.520  0.280  0.151  0.081

<!-- b000092 | caption | pages [6] -->
Table 1 Regular procedure, non-pre-check, true frequencies and predicted frequencies

<!-- b000093 | prose | pages [6] -->
10 𝜒𝜒2 =  (𝑁𝑁𝑖𝑖−𝑛𝑛𝑝𝑝𝑖𝑖) (9) = 16.919 2 = 15.898 < 𝜒𝜒0.05 𝑛𝑛𝑝𝑝𝑖𝑖 𝑖𝑖=1 Thus we consider the above as an exponential distribution.

<!-- b000094 | prose | pages [6] -->
And similarly, ﬁt for the pre-check procedure, 𝜒𝜒2 = 15.599 < 𝜒𝜒0.05 (9) = 16.919. 2 Since the inter-arrival time obeys exponential distribution, the number of passengers’ arri- val in unit time obeys Poisson distribution.

<!-- b000095 | heading | pages [6] -->
4.3.2 Phase 1 Queueing Specification

<!-- b000096 | prose | pages [6] -->
We also consider the service time of Phase 1 obeys exponential distribution, which is a common practice for simple cases in queueing theory, and the service rate is below.

<!-- b000097 | prose | pages [6, 7] -->
𝜇𝜇𝑑𝑑= 0.09465 Based on the above discussion, the Kendall notation of Phase 1 is (𝑀𝑀/𝑀𝑀/𝑐𝑐), where 𝑀𝑀 denotes a Poisson process and 𝑐𝑐 is the number of parallel servers. The arrival rate of this queueing model depend on certain conditions, and 𝑐𝑐 is given by the airport facility background. We assume that the service rate is a constant 𝜇𝜇𝑑𝑑= 0.09465 for each server.

<!-- b000098 | furniture | pages [7] -->
Team #67316

<!-- b000099 | furniture | pages [7] -->
Page 6 of 20

<!-- b000101 | heading | pages [7] -->
4.3.3 Phase 2

<!-- b000102 | prose | pages [7] -->
0.030 Because the two queueing models are in series, we 0.025

<!-- b000103 | prose | pages [7] -->
have 𝜆𝜆𝑠𝑠= 𝜇𝜇𝑑𝑑 . Phase 2 is also a multiple-server 0.020

<!-- b000104 | prose | pages [7] -->
0.015 model, but the serving process is much more com- 0.010 plicated, besides the histogram does not obey ex- 0.005 ponential distribution, apparently. 0.000 An Erlangian model is introduced, Erlang ser- 0 20 40 60 80

<!-- b000105 | caption | pages [7] -->
Figure 6 Histogram of the service time in Phase 2, to-

<!-- b000106 | prose | pages [7] -->
vice is widely used to model combined serving gether with a PDF plot of an Erlang distribution. processes, where consequent queueing models are connected in series. 𝑘𝑘 identical Poisson servers in series generate an Erlang type 𝑘𝑘 service. However, it is often the case that parameter 𝑘𝑘 is not strictly equal to the number of phases in a server. PDF of Erlang type 𝑘𝑘 distribution is given by 1 Γ(𝛼𝛼)𝛽𝛽𝛼𝛼𝑥𝑥𝛼𝛼−1 exp(−𝑥𝑥/𝛽𝛽 ) , (𝛼𝛼, 𝛽𝛽> 0; 0 < 𝑥𝑥< ∞) 𝑓𝑓(𝑥𝑥) =

<!-- b000107 | prose | pages [7] -->
with the expectation 𝐸𝐸(𝑥𝑥) = 𝛼𝛼𝛼𝛼 and variance 𝑉𝑉𝑉𝑉𝑉𝑉(𝑥𝑥) = 𝛼𝛼𝛽𝛽2 . Parameter 𝛼𝛼 and 𝛽𝛽 is related with 𝑘𝑘 and the service rate 𝜇𝜇 (Gross, et al., 1985):

<!-- b000108 | prose | pages [7] -->
𝛼𝛼= 𝑘𝑘 𝛽𝛽= 1  𝑘𝑘𝑘𝑘 Fit the distribution for the total service time in Phase 2 (time to get scanned property), our results are, 𝑘𝑘= 4, 𝜇𝜇𝑠𝑠= 0.0357.

<!-- b000109 | prose | pages [7] -->
Therefore, the Kendall notation of Phase 2 queueing is (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐), where the input 𝑀𝑀 is identical to the output of Phase 1, 𝐸𝐸𝑘𝑘 is an Erlang type 𝑘𝑘= 4, 𝜇𝜇𝑠𝑠= 0.0357 distribution, and the number of parallel servers (i.e. the number of X-ray scanners and millimeter wave scanners) is depend on speciﬁc airport.

<!-- b000110 | prose | pages [7] -->
(𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐) queueing does not have a good analytical solution; our numerical solution using simulation technique will be introduced later.

<!-- b000111 | heading | pages [7] -->
4.4 Section Summary

<!-- b000112 | prose | pages [7] -->
The airport security check process consists of two phases, ﬁrst of which is an (𝑀𝑀/𝑀𝑀/𝑐𝑐) queue- ing process, and the second is an (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐′) queueing. Arrival rate of the second is the service rate of the ﬁrst. Parameters of the distributions can be estimated using the given data.

<!-- b000113 | furniture | pages [8] -->
Team #67316

<!-- b000114 | furniture | pages [8] -->
Page 7 of 20

<!-- b000115 | prose | pages [8] -->
Queueing Simulation and Bottlenecks Spotting

<!-- b000116 | heading | pages [8] -->
5.1 Estimating Expenses

<!-- b000117 | prose | pages [8] -->
According to (Learn.org; PayScale.com), income of a security oﬃcer is $28,624–$58,987 and of an airline security screener is $23,262–$54,015. That is the human resource expenses of the security check. Costs of security devices are mostly one-oﬀ consumptions. The price of an airport X-ray baggage scanner is at $20,000–50,000 and of a millimeter wave full body scanner is at $100,000 (Alibaba.com). And the maintenance cost is mainly from the electricity. Another fact is that one single lane of the scan check process requires 4 security screeners on average. Therefore, we drew a conclusion that the cost of one lane (server) in Phase 2, is about the cost of 4 desks (servers) at Phase 1.

<!-- b000118 | heading | pages [8] -->
5.2 Basic Ideas

<!-- b000119 | prose | pages [8, 9] -->
A MATLAB program is written to simulate the entire security check process. To build up the numeric solution, Markov chains are used for Erlangian queueing. (Zeng, et al., 2011) Since there is no analytical solution of an (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐) (Phase 2) queueing model, a simulation of the entire security check process is put forward, and both Phase 1 and Phase 2 are concerned in the model in series.

<!-- b000120 | caption | pages [8] -->
Figure 7 MATLAB simulation speciﬁcation

<!-- b000121 | furniture | pages [9] -->
Team #67316

<!-- b000122 | furniture | pages [9] -->
Page 8 of 20

<!-- b000124 | prose | pages [9] -->
Given the parameters of each probability distribution at the two phases, we generate series of random variates to simulate the process. First, random variates obeying exponential distri- bution is generated as people’s inter-arrival time. We then calculate and store the arrival timestamps, service time (generated random variables obeying another exponential distribution) and waiting time (worked out with the previous passenger’s waiting time, service time and the arrival interval) of each passenger in a table. Besides getting results of waiting time spans, the removal rate of Phase 1 is also observed, which is used as the arrival of Phase 2. After working on Phase 1, we do the same on Phase 2, but the new service is Erlangian. Finally, expectations of total waiting time are evaluated.

<!-- b000125 | prose | pages [9] -->
To spot the bottlenecks in the process, we tested the improvements of total waiting time expectations when 4 document check servers are added (row “Document Check Added” in the table below), and 1 scan check server is added (row “Scan Check Added”).

<!-- b000126 | heading | pages [9] -->
5.3 Spot the Bottlenecks!

<!-- b000127 | prose | pages [9] -->
The simulated security process has a changeable arrival rate 𝜆𝜆𝑑𝑑, and both of the initial numbers of the document check servers and of the scan check servers are assigned 5, as is the case in Figure 2, which is a small scale for an airport. The service rate of one document check server is assigned 𝜇𝜇𝑑𝑑= 0.09465, and that of one scan check service is 𝜇𝜇𝑠𝑠= 0.0357. Service of Phase 2 is Erlangian type 𝑘𝑘= 4. These three parameters are the same to what we have mentioned before.

<!-- b000128 | prose | pages [9] -->
Below lists the expectations for total waiting time at diﬀerent arrival rates. Row “Original” is the total waiting time expectation of process consist of (𝑀𝑀/𝑀𝑀/5) and (𝑀𝑀/𝐸𝐸𝑘𝑘/5). Row “Doc- ument Check Added” for the case that 4 document check servers are added, that is (𝑀𝑀/𝑀𝑀/9) for Phase 1 and (𝑀𝑀/𝐸𝐸𝑘𝑘/5) for Phase 2. For row “Scan Check Added”, 1 scan check server is added, that is (𝑀𝑀/𝑀𝑀/5) and (𝑀𝑀/𝐸𝐸𝑘𝑘/6).

<!-- b000129 | prose | pages [9] -->
𝝀𝝀𝒅𝒅 3.247 3.710 4.329 4.478 4.638 4.810 5.194 Original 31349 22632 12781 10807 8988 7391 3668 Document Check Added 31092 21878 11832 10671 8925 7215 3291 Scan Check Added 18258 10643 3045 1680 271 88 24

<!-- b000130 | caption | pages [9] -->
Table 2 Simulation results of the total waiting time (in seconds)

<!-- b000131 | prose | pages [9] -->
We ﬁnd that, the document check process is not the bottleneck of the process, but the scan check. By adding scan check lanes, service capability of the whole system is signiﬁcantly in- creased. We can even observe that some divergent queueing cases converge (e.g. 𝜆𝜆𝑑𝑑= 5.194).

<!-- b000132 | furniture | pages [10] -->
Team #67316

<!-- b000133 | furniture | pages [10] -->
Page 9 of 20

<!-- b000134 | heading | pages [10] -->
5.4 Comments

<!-- b000135 | prose | pages [10] -->
Based on the above analysis, bottlenecks restricting the queueing capacity and eﬃciency comes from the scan process Phase 2. From the given data, we see that the X-ray scan time is usually fast and steady, and is not likely to be the bottleneck. However, time taken for the passenger to take oﬀ clothes and to take care of their carry-on properties contribute much to the next passenger’s waiting (time C in Figure 3), especially when someone is heavy with carry-on properties or not experienced in air travelling.

<!-- b000136 | prose | pages [10] -->
We would recommend the airport to allow the passengers to take a bin for their to-be- scanned properties before queueing, and thus waiting time in Phase 2 will be reduced.

<!-- b000137 | prose | pages [10] -->
Comments on the Safety

<!-- b000138 | prose | pages [10] -->
Firstly, on the stand of the airport, any security accident, including terrorist attacks, hijacking or aircraft destroying, if happens, will cause unbearable blame from the public opinion, which is unacceptable for the airport. Thus it does not sound like a good idea to reduce the links in security check procedure to fasten check-in and to lower the expenses.

<!-- b000139 | prose | pages [10] -->
A fundamental principle of our later discussion is that, no procedure in the security check chain is omitted. Means like optimizing queueing processes, arranging human resources, guid- ing passengers’ arrival can be implemented as ways to improve the passenger experience.

<!-- b000140 | heading | pages [10] -->
Passenger Arrival Behavior Modeling

<!-- b000141 | heading | pages [10] -->
7.1 Passenger Flow Generating

<!-- b000142 | prose | pages [10] -->
Flight records of O’Hare International Airport on Wednesday, Jan. 18, 2017 were found on (Flight Stats), including the departure time and information of the plane models. Most of the airlines are Boeing 737-800 whose capacity is usually 104–189 passengers.

<!-- b000143 | prose | pages [10] -->
To simulate the passenger arrival behavior, i.e. 1000 the varying passenger ﬂow in a time period, we as- 900 sume that the capacity of every ﬂight is about 189, 800 and the points of the passengers’ arrival time obey 700 normal distribution. Since TSA recommends passen- 600 gers to be at the airport 2 hours earlier before the 500 ﬂight for domestic departures, we model the passen- gers’ arrival time for each ﬂight to obey normal dis- 400

<!-- b000144 | prose | pages [10] -->
tribution 𝑁𝑁(𝜇𝜇, 𝜎𝜎2), and let 𝜇𝜇 be 2 hours before the 300 0 100 200 300 400 500 600 700 departure and 𝜇𝜇+ 3𝜎𝜎 be the point in time that there

<!-- b000145 | caption | pages [10] -->
Figure 8 Varying passenger ﬂow in a time period, from

<!-- b000146 | prose | pages [10, 11] -->
is half an hour remained. 6:30 a.m. to 16:40 p.m., O’Hare International Airport, Jan. 18, 2017 We then add these PDFs together and get the dynamic passenger arrival data. The shown plotted graph (Figure 8) is such a practice on timespan between 6:30 a.m. to 16:40 p.m.

<!-- b000147 | furniture | pages [11] -->
Team #67316

<!-- b000148 | furniture | pages [11] -->
Page 10 of 20

<!-- b000150 | prose | pages [11] -->
We can see a peak at 9:30 a.m. and at around 11:00, the passenger ﬂow get down to a relatively low level (this is probably because of massive departures).

<!-- b000151 | prose | pages [11] -->
Based on the above passenger ﬂow distribution, we will simulate the security check queue- ing process at a domestic departure checkpoint later.

<!-- b000152 | heading | pages [11] -->
7.2 Arrival Time Recommendation

<!-- b000153 | prose | pages [11] -->
We tend to believe that the passenger arrival behavior can be changed by recommending their arrival time, however this is often much more complex due to airport location or cultural norm of a certain nation.

<!-- b000154 | prose | pages [11] -->
We calculated the mean waiting time of the passengers by simulating using the varying passenger ﬂow introduced in the last subsection, at diﬀerent normal distributions as we men- tioned above. Only one checkpoint is taken into account in the simulation, and the ﬂow is generated with domestic departure ﬂights. When the average arrival of the passengers for a certain ﬂight is 120 minutes earlier, its mean waiting time in the security check process is about 26 minutes as shown in the chart below.

<!-- b000155 | prose | pages [11] -->
Diﬀerence of 𝝁𝝁 and the departure time (min) 90 105 120 150 180 𝝈𝝈 (Ensured that 𝝁𝝁+ 𝟑𝟑𝟑𝟑 is at 30 min earlier the departure) 20 25 30 40 50 Passenger ﬂow per hour 491 498 502 503 498 Mean waiting at Phase 1 (sec) 0.0953 0.0633 0.0781 0.0654 0.0631 Mean waiting at Phase 2 (sec) 82.9986 56.146 26.0189 21.7186 16.9306

<!-- b000156 | caption | pages [11] -->
Table 3 Result for waiting time at diﬀerent recommended time

<!-- b000157 | prose | pages [11] -->
From the chart, we curiously found that the earlier the passengers arrive, the less the mean waiting time will be. This is quite expected, because earlier arrivals and more uniformly dis- tributed arrival intervals can reduce the “strikes” of the passenger ﬂow.

<!-- b000158 | prose | pages [11] -->
Cultural norm impact on the arrival rate distribution (“varying passenger ﬂow”, in other words) will be discussed later. Measures like sending text messages to passengers for recom- mending their arrivals based on real-time data as well as their cultural background will help.

<!-- b000159 | prose | pages [11] -->
Checkpoint Redesign

<!-- b000160 | heading | pages [11] -->
8.1 Concentrating the Checkpoints

<!-- b000161 | heading | pages [11] -->
8.1.1 Basic Ideas

<!-- b000162 | prose | pages [11, 12] -->
In queueing theory, it is found that (𝑀𝑀/𝑀𝑀/𝑐𝑐) queueing has a better performance than 𝑐𝑐 par- allel (𝑀𝑀/𝑀𝑀/1) queueing processes, with shorter mean queue length and better mean waiting time. (See Appendix 13.1 for Proof) Simulation of a more complex system, as in the security check process is made and the results are consistent. According to our assumption, so long as the passengers could see the servers, they will choose to wait in the queue that minimizes their waiting time. Thus making the passengers know the queueing conditions at checkpoints works.

<!-- b000163 | furniture | pages [12] -->
Team #67316

<!-- b000164 | furniture | pages [12] -->
Page 11 of 20

<!-- b000166 | heading | pages [12] -->
8.1.2 Measures to Take

<!-- b000167 | prose | pages [12] -->
Security checkpoints to terminals are shown in the O’Hare terminal map. (Chicago Department of Aviation, 2012). We would recommend the airport to reduce the distances between each checkpoints at Terminal 1 and 3. This will help the passengers to choose a checkpoint minimiz- ing their waiting among the equivalent check- points at each terminal.

<!-- b000168 | prose | pages [12] -->
Another possible solution which is equiva- lent to the former is to monitor the real-time

<!-- b000169 | caption | pages [12] -->
Figure 9 O’Hare Terminal Map, © 2012 Chicago Depart-

<!-- b000170 | prose | pages [12] -->
queue length of each checkpoint at Terminal 1 ment of Aviation, URL: http://www.ﬂychicago.com and 3 and install LED boards to show these in- /OHare/EN/AtAirport/map/default.aspx (Chicago Department of Aviation, 2012) formation. This also helps the passengers to choose a proper checkpoint.

<!-- b000171 | prose | pages [12] -->
The above measures may both avoid some queue’s getting too long and cause a congestion.

<!-- b000172 | heading | pages [12] -->
8.2 Checkpoint Structure

<!-- b000173 | heading | pages [12] -->
8.2.1 Distribution of Human Resource between the 2 Phases

<!-- b000174 | prose | pages [12] -->
This suggestion on checkpoint redesign is a continued section of Section 5.3, Spotting Bottle- necks. We know that the cost of a lane in Phase 2 is 4 times more than that of a desk at Phase 1. Optimizing the checkpoint structure and keep the cost relatively low can balance the service rates of the document check process and the scan check process, as well as saving money.

<!-- b000175 | prose | pages [12] -->
This is a programming problem in operation research. Assume the number of document check servers is 𝑘𝑘1, and that of the scan check is 𝑘𝑘2.

<!-- b000176 | prose | pages [12] -->
𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀 𝑘𝑘1 + 𝑘𝑘2, ⎧0 < 𝑘𝑘1, 𝑘𝑘2 ≤5 ª 𝑘𝑘1𝜇𝜇𝑑𝑑> 𝜆𝜆𝑑𝑑 𝑠𝑠. 𝑡𝑡. ⎨ ª 𝑘𝑘2𝜇𝜇𝑠𝑠> 𝜆𝜆𝑠𝑠 ⎩ We trial the number of servers with our simulation to ﬁnd the appropriate ratio. Our result is, when there are 5 lanes of scan check servers, 3 document check servers are enough for most common cases. Cut on document check service desks won’t cause bottlenecks, and according to our previous study, adding new lanes will greatly improve the security check service.

<!-- b000177 | furniture | pages [13] -->
Team #67316

<!-- b000178 | furniture | pages [13] -->
Page 12 of 20

<!-- b000179 | prose | pages [13] -->
Time since the initial (min)

<!-- b000180 | furniture | pages [13] -->
391-450

<!-- b000181 | furniture | pages [13] -->
451-510

<!-- b000182 | furniture | pages [13] -->
511-570

<!-- b000183 | furniture | pages [13] -->
571-630

<!-- b000184 | furniture | pages [13] -->
631-690

<!-- b000185 | furniture | pages [13] -->
691-750

<!-- b000186 | furniture | pages [13] -->
751-810

<!-- b000187 | furniture | pages [13] -->
811-870

<!-- b000188 | furniture | pages [13] -->
871-930

<!-- b000189 | furniture | pages [13] -->
931-990

<!-- b000190 | prose | pages [13] -->
Passenger ﬂow /h 563 433 277 473 430 484 550 541 662 617 Positions needed for Phase 1 2 2 1 2 2 2 2 2 3 3 Mean waiting time at Phase 1 28.7135 7.6859 103.3296 12.2084 7.2299 11.2017 21.9008 17.9357 4.1698 3.188 Positions needed for Phase 2 5 4 3 5 4 5 5 5 5 5 Mean waiting time at Phase 2 27.3362 31.1131 14.1786 7.986 26.8053 7.2921 19.351 15.4442 6172 96.1114

<!-- b000191 | caption | pages [13] -->
Figure 10 Numbers of positions needed at Phase 1 and Phase 2 to make the queue length converge

<!-- b000192 | heading | pages [13] -->
8.2.2 Dynamic Assignment of Duty in a Time Span

<!-- b000193 | prose | pages [13] -->
Based on our previous work on passenger ﬂow distribution in a period of time and the pro- gramming in the above subsubsection, we evaluate the duty assignment at each checkpoint every hour.

<!-- b000194 | prose | pages [13] -->
7

<!-- b000195 | prose | pages [13] -->
6

<!-- b000196 | prose | pages [13] -->
5

<!-- b000197 | prose | pages [13] -->
4

<!-- b000198 | prose | pages [13] -->
3

<!-- b000199 | prose | pages [13] -->
2

<!-- b000200 | prose | pages [13] -->
1

<!-- b000201 | prose | pages [13] -->
0 6:30 7:30 8:30 9:30 10:30 11:30 12:30 13:30 14:30 15:30

<!-- b000202 | caption | pages [13] -->
Figure 11 Dynamic assignment of duty with Phase 1 in blue and Phase 2 in green

<!-- b000203 | prose | pages [13] -->
Allocating fewer staﬀ at the troughs, and more at the peaks, will help the security check system running properly at relatively low cost.

<!-- b000204 | prose | pages [13] -->
And for the speciﬁc problem we are now considering, we practice this method and plan to allocate the duty like this:

<!-- b000205 | prose | pages [13] -->
– 8:30 a.m. 2 for document check and 4 for scan check 8:30 a.m.  – 13:30 p.m. 2 for document check and 5 for scan check 13:30 p.m.  – 16:30 p.m. 3 for document check and 6 for scan check

<!-- b000206 | caption | pages [13] -->
Table 4 Dynamic duty allocation

<!-- b000207 | heading | pages [13] -->
8.2.3 Sensitivity Test

<!-- b000208 | prose | pages [13] -->
A sensitivity test is made for our model. The test is done via simulation.

<!-- b000209 | prose | pages [13, 14] -->
Original Decreased ﬂow Increased service ability Passenger ﬂow 502 452 502 Serve ability (Phase 2) 0.036 0.036 0.040 Mean waiting time 41.70 12.57 7.834 We ﬁnd that when the passenger ﬂow decreases by 10%, the mean waiting time deceases by 69.9%. When the document check service ability is raised by 10%, the mean waiting time almost remains the same. And if the service ability at Phase 2 is increased by 10%, the mean waiting time drops as much as 81.2%!

<!-- b000210 | caption | pages [13] -->
Table 5 Sensitivity test result, simulations for each case are done for 5 times

<!-- b000211 | furniture | pages [14] -->
Team #67316

<!-- b000212 | furniture | pages [14] -->
Page 13 of 20

<!-- b000214 | prose | pages [14] -->
From the above test, we drew a conclusion that the queueing system is sensitive to the scan check service ability, while a low sensitivity is observed for changes of the document check ability. This again veriﬁes the bottlenecks that we found earlier, and optimization can be given around the found bottlenecks.

<!-- b000215 | prose | pages [14] -->
Virtual Queueing

<!-- b000216 | prose | pages [14] -->
Waiting room can be useful to improve passengers’ experience. What’s even better is that the queueing discipline can be modiﬁed with this method. The conventional physical queue method is a strict FIFS (First In First Served), while virtual queueing can be more ﬂexible. With the popularization of smartphones, new queueing methods that basically share the same process as virtual queueing, such as mobile queueing, but are more convenient and more suﬃcient are introduced, which will also provide us more possibilities to modify the queueing process. (Wikipedia; Zhao, et al., 2016)

<!-- b000217 | heading | pages [14] -->
9.1 Strict Priority Queue

<!-- b000218 | prose | pages [14] -->
Passengers’ satisfaction can be quantiﬁed by the number of passengers that missed their ﬂights, mean remaining time after security check and the variant of the remaining time. Although FIFS sounds like an absolutely equitable practice, it is frustrating under some extreme circum- stances. Imagine an “early bird” comes to the airport 6 hours in advance of his or her departure. If an unfortunate congestion occurs, the early passenger would hold up the passengers behind whose ﬂight might be to take oﬀ. This is not acceptable.

<!-- b000219 | prose | pages [14] -->
Consider a strict priority queue, where the priority is strictly based on the departure time of each passenger. We now prove that this approach achieves better passenger satisfaction with our simulation.

<!-- b000220 | prose | pages [14] -->
Fewer missed flights! Great! Fewer risks!

<!-- b000221 | prose | pages [14] -->
Longer remaining time! Easy boarding.

<!-- b000222 | prose | pages [14] -->
Smaller variance! Sounds fair!

<!-- b000223 | caption | pages [14] -->
Figure 12 Passenger satisfaction

<!-- b000224 | furniture | pages [15] -->
Team #67316

<!-- b000225 | furniture | pages [15] -->
Page 14 of 20

<!-- b000226 | prose | pages [15] -->
Our approach is to change the queueing discipline in the simulation, and we do ﬁnd a strict priority queue performs better in the above aspects. The testing data involves a passenger ﬂow of 723 passengers per hour. Our results are as follows:

<!-- b000227 | prose | pages [15] -->
1 2 3 4 5 6 7 8 9

<!-- b000228 | heading | pages [15] -->
10 Mean

<!-- b000229 | prose | pages [15] -->
FIFS 231 292 233 280 346 298 333 316 209 274 281.2 Priority 19 0 0 35 0 31 0 2 7 0 9.4

<!-- b000230 | caption | pages [15] -->
Figure 13 Numbers of passenger that missed their ﬂights. 10 experiments are done here.

<!-- b000231 | prose | pages [15] -->
And the means and the variances of remaining time:

<!-- b000232 | prose | pages [15] -->
Mean Variance 6.8787 × 106 FIFS 6918 3.9684 × 106 Priority 6864

<!-- b000233 | caption | pages [15] -->
Figure 14 Means and variances of the remaining time

<!-- b000234 | prose | pages [15] -->
Means are almost the same (this is expected, because expectation for the waiting time won’t vary with queueing discipline, which is a theorem in queueing theory. The slight diﬀerence is caused by the generation of random variates) while variance of queueing where priority is considered seems to be better.

<!-- b000235 | heading | pages [15] -->
9.2 Virtual Queueing Concerning Partial Priority Discipline

<!-- b000236 | prose | pages [15] -->
However, a strict priority queue does not sounds rational to a lot of people. (And of course, it is culture dependent.) A better queueing discipline is introduced here to be a fairer and more eﬃcient option, and above all, cultural adaptable.

<!-- b000237 | prose | pages [15] -->
We introduce an “acceptability factor” 𝛼𝛼 (0 ≤𝛼𝛼≤1) denote the acceptance of the strict priority discipline. We then use a partial priority discipline, which is a mixture of strict FIFS and strict priority discipline.

<!-- b000238 | prose | pages [15] -->
Let 𝑡𝑡𝑎𝑎 denote a passenger’s arrival time, and 𝑡𝑡𝑑𝑑 denote his or her departure time. We use 𝑡𝑡𝑝𝑝= 𝛼𝛼𝑡𝑡𝑑𝑑+ (1 −𝛼𝛼)𝑡𝑡𝑎𝑎 as the priority of the passengers, and sort the waiting queue in this discipline.

<!-- b000239 | prose | pages [15] -->
We tested 𝛼𝛼= 0.5 for a passenger ﬂow at 721 passengers/h, which is quite an extreme case for a single checkpoint. Below is our result.

<!-- b000240 | prose | pages [15] -->
Passengers Missed Flight Variance 6.8787 × 106 FIFS 281.2 5.1711 × 106 Partial Priority 71.3 3.9684 × 106 Strict Priority 9.4

<!-- b000241 | caption | pages [15] -->
Table 6 Number of passengers that missed the ﬂight (10 hours) and variance of remaining time, 𝛼𝛼= 0.5

<!-- b000242 | prose | pages [15] -->
We ﬁnd the partial priority discipline is also eﬀective in raising passenger satisfaction.

<!-- b000243 | furniture | pages [16] -->
Team #67316

<!-- b000244 | furniture | pages [16] -->
Page 15 of 20

<!-- b000245 | prose | pages [16] -->
Inter-cultural Applicability

<!-- b000246 | heading | pages [16] -->
10.1 Cultural Impacts on Punctuality

<!-- b000247 | prose | pages [16] -->
Diﬀerent cultural norms have an impact on passengers’ punctuality.

<!-- b000248 | prose | pages [16] -->
People in the United States, Canada and many northern European countries have a linear view of time, and are more likely to be punctual. This is also true to East Asian countries, like China and Japan, where social eﬃciency is seen important. In these countries, people tend to have a keen sense of time, and would usually be early for an event. On the contrast, Spaniards or people from Southern Europe are not so punctual. Passengers from such nations often hurry to board. (Business Insider) Viewing the diﬀerences of varied cultural norms with our passenger arrival behavior model (see Section 7), we can say that the passenger ﬂow in countries where people are more punctual is often more smooth and steady. More mathematically, the mean arrival time 𝜇𝜇 is often far earlier than the passengers’ ﬂight departures, and the variance of their arrival distribution 𝜎𝜎2 is relatively small. Case for countries that are not so punctual is just opposite, as shown in the following plotted graph.

<!-- b000249 | prose | pages [16] -->
1100 1400

<!-- b000250 | prose | pages [16] -->
1000 1200

<!-- b000251 | prose | pages [16] -->
900 1000

<!-- b000252 | prose | pages [16] -->
800 800

<!-- b000253 | prose | pages [16] -->
700 600

<!-- b000254 | prose | pages [16] -->
600 400

<!-- b000255 | prose | pages [16] -->
500 200 0 100 200 300 400 500 600 0 100 200 300 400 500 600

<!-- b000256 | caption | pages [16] -->
Figure 15 Smooth passenger ﬂow, 𝜇𝜇 is 150 minutes earlier

<!-- b000257 | caption | pages [16] -->
Figure 16 Rough passenger ﬂow, where 𝜇𝜇 is 90 minutes

<!-- b000258 | prose | pages [16] -->
the departure, and 𝜎𝜎= 40. earlier, and 𝜎𝜎= 20.

<!-- b000259 | prose | pages [16] -->
Airports with more smooth and steady passenger ﬂow does not requires too much human resource, and its assignment can be more ﬂexible, for passenger ﬂow peaks are seldom observed. Scale eﬀect that adopt (𝑀𝑀/𝑀𝑀/𝑐𝑐) rather than 𝑐𝑐 parallel (𝑀𝑀/𝑀𝑀/1) also tend to work. Instead, it is not this satisfying in a less punctual nation. More peaks will be found, and massive human resource is needed to deal with the sudden congestions.

<!-- b000260 | prose | pages [16] -->
As we have mentioned before, sending text messages in advance to recommend passengers’ check-in time personally based on the current passenger ﬂow at the airport is a very good practice. But when diﬀerent cultural norms are considered, this is not that easy, for people’s punctuality must be taken into account. Since there is no such practice now, we cannot deter- mine the 𝜇𝜇 and 𝜎𝜎2 of people’s arrival behavior in diﬀerent countries, yet we can prove it cer- tainly works.

<!-- b000261 | furniture | pages [17] -->
Team #67316

<!-- b000262 | furniture | pages [17] -->
Page 16 of 20

<!-- b000263 | heading | pages [17] -->
10.2 Cultural Impacts in Queueing Process

<!-- b000264 | prose | pages [17] -->
Another cultural impact on our model is the acceptability of priority queueing in diﬀerent nations. People in the United States respect others’ privacy as well as they hate other people cutting in line. Swiss are punctual and take collective eﬃciency as the most important. While in China, jumping queues is usual because individual eﬃciency is respected, and people tend to forgive such behaviors if the queue jumper has reasonable excuses.

<!-- b000265 | prose | pages [17] -->
The above varied thinking patterns may lead to diﬀerent acceptability in diﬀerent nations. Our acceptability factor 𝛼𝛼 (See 9.2 for deﬁnition), enlighten the culture-related factor in our model.

<!-- b000266 | prose | pages [17] -->
For example, passengers from the United States tend to think the new queueing discipline is not acceptable, because it damages the FIFS principle. However, Swiss might be in favor of our method because it dramatically raises the collective eﬃciency, and thus a greater 𝛼𝛼 could be assigned. Chinese would probably think a neutral 𝛼𝛼 was a good practice.

<!-- b000267 | heading | pages [17] -->
Discussion and Conclusions

<!-- b000268 | heading | pages [17] -->
11.1 Policy Recommendations

<!-- b000269 | prose | pages [17] -->
We here give a complete guide on security check modiﬁcations and policy making for the TSA security manager based on our previous model, as our solution to problem 4.

<!-- b000270 | prose | pages [17] -->
To Security Managers

<!-- b000271 | prose | pages [17] -->
To solve the airport security check congestion, and to optimize the throughput at the airport security checkpoints, we give you the following recommendations on policy making based on our investigation.

<!-- b000272 | prose | pages [17] -->
On human resource distribution, we would recommend fewer document check servers, while more for scan check. Bottlenecks of the security check workﬂow are at the scan check phase, and we have proved that 2 or 3 desks for document check is enough for a 5-lane scan check area. Dynamic allocation of document check servers and lanes opened should be reserved as a way to reduce unnecessary cost, besides, our approach to solve this has been put forward in our paper.

<!-- b000273 | prose | pages [17] -->
On facilities, waiting rooms should be built for virtual queueing. If possible, adding lanes for scan check at each checkpoint will dramatically increase the pas- senger throughput. Shorten the distances between identical checkpoints in the ter- minal will help passengers to choose one that minimizes their waiting. LED boards providing information of queue lengths at each checkpoint works in the same way.

<!-- b000274 | prose | pages [17, 18] -->
If possible, we also recommend a mobile queue system to be built, together with a queue management system, these facilities, thanks to the new information technol- ogy, will enhance the eﬃciency encouragingly. Providing passengers with bins for their to-be-scanned properties in advance will also shorten their waiting during the scan check process and avoid bottlenecks.

<!-- b000275 | furniture | pages [18] -->
Team #67316

<!-- b000276 | furniture | pages [18] -->
Page 17 of 20

<!-- b000278 | prose | pages [18] -->
On safety and the cost, no reduction of links on the current security check procedure is recommended, since the risks cannot be assessed in value. Dynamic assignment of the duties is a possible solution as we have just mentioned above.

<!-- b000279 | prose | pages [18] -->
Opening new lanes for checkpoints will also cost money, but money saved by good human resource allocation can be used for throughput enhancement.

<!-- b000280 | prose | pages [18] -->
We would like to highlight our approach to inﬂuence the passengers’ arri- val. TSA has already made recommendations of time-in-advance for the passengers to avoid missing ﬂights. Through our assumptions and modeling, we are curious to ﬁnd that it is possible to aﬀect the passenger ﬂow by informing passengers of the arrival time ahead of their departure personally and dynamically based on the real- time statistics of the passenger ﬂow at the airport. And the inﬂuenced passenger ﬂow may reduce the occurrence of congestions at security checkpoints.

<!-- b000281 | prose | pages [18] -->
Passengers’ satisfaction is considered and quantiﬁed. With the help of vir- tual queueing mechanism, the departure priority queueing discipline can be prac- ticed, which will reduce the variant of the passengers’ remaining time (thus raises the fairness) and more importantly, reduce the missed ﬂights of the passengers.

<!-- b000282 | prose | pages [18] -->
Cultural norm impact on our model is also taken into consideration. Passen- gers’ cultural background may inﬂuence their punctuality of arrival and acceptabil- ity of our partial priority queueing discipline. Punctuality of a nation has an impact on the passenger ﬂow at an airport, and acceptability of priority queueing should also be taken into account to avoid cultural taboos. This requires adaptation of our models in diﬀerent countries. Changing the assumed normal distribution for passen- ger arrival and the acceptability factor 𝛼𝛼 (See 9.2 for deﬁnition) will help. For ex- ample, for countries where people are not punctual, we can recommend them to be earlier for the ﬂights. Another example is to illustrate the acceptability of our partial priority queueing discipline. In countries where jumping queue is extremely disa- greeable, we can set the queueing to be more FIFS. On contrary, in countries where collective eﬃciency is emphasized, we adjust our factor 𝛼𝛼 to add the priority com- ponents in the queueing process.

<!-- b000283 | prose | pages [18] -->
We hereby sincerely hope the above recommendations will work.

<!-- b000284 | prose | pages [18] -->
Internal Control Management (ICM) team

<!-- b000285 | heading | pages [18] -->
11.2 Model Assessment

<!-- b000286 | prose | pages [18] -->
Model validation has been implemented in each section of the above modeling. Here, we assess the strengths, weaknesses and possible future work in the section.

<!-- b000287 | furniture | pages [19] -->
Team #67316

<!-- b000288 | furniture | pages [19] -->
Page 18 of 20

<!-- b000289 | heading | pages [19] -->
11.2.1 Strengths

<!-- b000290 | prose | pages [19] -->
• Full assumptions and validations are made for passengers’ arrival distribution and se- curity check service time models. Bottlenecks are spotted and thorough analysis is made.

<!-- b000291 | prose | pages [19] -->
• Our simulation of one day’s passenger ﬂow is based on the real data of O’Hare Interna- tional Airport, which is convincing.

<!-- b000292 | prose | pages [19] -->
• Safety is taken as a fundamental principle. All optimization is done based on the prin- ciple.

<!-- b000293 | prose | pages [19] -->
• Recommendations on passenger arrival guidance, checkpoint redesign, change of the queueing discipline, allocation of human resources, virtual queueing are given. Passen- gers’ satisfactory are considered, and the passenger’s ﬂight experience will be improved.

<!-- b000294 | prose | pages [19] -->
• Cultural diﬀerences are quantiﬁed and fully assessed. Sensitivity to these cultural factors of the passenger ﬂow and acceptability to our priority queueing discipline.

<!-- b000295 | heading | pages [19] -->
11.2.2 Weaknesses

<!-- b000296 | prose | pages [19] -->
• TSA Pre-check is not investigated thoroughly.

<!-- b000297 | prose | pages [19] -->
• Lack of further consideration on safety.

<!-- b000298 | heading | pages [19] -->
11.3 Conclusions

<!-- b000299 | prose | pages [19] -->
For problem 1, we use the given data and ﬁnd the distribution pattern of passenger ﬂow and service time, then queueing models are built for the security check process at each checkpoint. We see the security check process as a (𝑀𝑀/𝑀𝑀/𝑐𝑐) queueing and a (𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐) process in series. Evaluation of passenger ﬂow behavior in a period of time is made. We use normal distribution to simulate the varying passenger ﬂow.

<!-- b000300 | prose | pages [19] -->
For problem 2, we put forward several possible approaches to improve passenger through- put and raise the passengers’ satisfaction, including checkpoint redesign and virtual queueing where a partial priority queueing discipline is introduced.

<!-- b000301 | prose | pages [19] -->
Cultural norm impacts are also taken into account. For problem 3, we discussed the cultural impact on passenger ﬂow and acceptability of the priority discipline, and recommendations are given to adapt our model to diﬀerent cultures.

<!-- b000302 | prose | pages [19] -->
A detailed guide for policy making is made as our solution of problem 4, again, cultural factors are considered and recommendations concerning cultural diﬀerence are made. The rec- ommendations we gave are all proved to be valid in previous discussions.

<!-- b000303 | heading | pages [19] -->
11.4 Further Work

<!-- b000304 | prose | pages [19] -->
• Discuss the Pre-check modiﬁcation. Levels of security check based on the passengers’ credit rating, or more detailed background check can be implemented.

<!-- b000305 | furniture | pages [20] -->
Team #67316

<!-- b000306 | furniture | pages [20] -->
Page 19 of 20

<!-- b000307 | prose | pages [20] -->
• Investigation on how cultural norm diﬀerences impact the punctuality and attitude towards the priority queueing need to be done. The correlations between the mathe- matical parameters and factors in reality should be revealed.

<!-- b000308 | prose | pages [20] -->
• Detailed research on raising the check-in experience of the disabled and the senior should be made.

<!-- b000309 | prose | pages [20] -->
• Eﬀect caused by waiting based on Lorenz curve.

<!-- b000310 | furniture | pages [21] -->
Team #67316

<!-- b000311 | furniture | pages [21] -->
Page 20 of 20

<!-- b000312 | heading | pages [21] -->
References

<!-- b000313 | references | pages [21] -->
Alibaba.com. Airport security device x-ray baggage scanner. Alibaba. [Online] [Cited: 1

<!-- b000314 | references | pages [21] -->
[1]

<!-- b000315 | references | pages [21] -->
22, 2017.]

<!-- b000316 | references | pages [21] -->
https://www.alibaba.com/product-detail/Airport-security-device-x-ray-

<!-- b000317 | references | pages [21] -->
baggage_60381309000.html.

<!-- b000318 | references | pages [21] -->
—. High Quality Product Millimeter Wave Full Body Scanner Price. Alibaba. [Online]

<!-- b000319 | references | pages [21] -->
[2]

<!-- b000320 | references | pages [21] -->
[Cited: 1 22, 2017.]

<!-- b000321 | references | pages [21] -->
https://www.alibaba.com/product-detail/High-Quality-Product-Millimeter-Wave-

<!-- b000322 | references | pages [21] -->
Full_60569216900.html?spm=a2700.7724838.0.0.uHVhJp.

<!-- b000323 | references | pages [21] -->
Business Insider. How Diﬀerent Cultures Understand Time. Business Insider. [Online]

<!-- b000324 | references | pages [21] -->
[3]

<!-- b000325 | references | pages [21] -->
[Cited: 1 24, 2017.]

<!-- b000326 | references | pages [21] -->
http://www.businessinsider.com/how-different-cultures-understand-time-2014-

<!-- b000327 | references | pages [21] -->
5?IR=T.

<!-- b000328 | references | pages [21] -->
Chicago Department of Aviation. 2012. O'Hare Map. FlyChicago. [Online] Chicago

<!-- b000329 | references | pages [21] -->
[4]

<!-- b000330 | references | pages [21] -->
Department of Aviation, 2012. [Cited: 1 23, 2017.]

<!-- b000331 | references | pages [21] -->
http://www.flychicago.com/pages/landingpage.aspx.

<!-- b000332 | references | pages [21] -->
Flight Stats. Flight Stats Information. Flight Stats. [Online] Flight Stats. [Cited: 1 23,

<!-- b000333 | references | pages [21] -->
[5]

<!-- b000334 | references | pages [21] -->
2017.] http://www.flightstats.com/go/FlightStatus/flightStatusByFlight.do.

<!-- b000335 | references | pages [21] -->
[6]

<!-- b000336 | references | pages [21] -->
Gross, Donald and Harris, Carl M. 1985. Fundamentals of Queueing Theory. s.l. :

<!-- b000337 | references | pages [21] -->
Wiley, 1985. pp. 170-175. ISBN 0-471-89067-7.

<!-- b000338 | references | pages [21] -->
[7]

<!-- b000339 | references | pages [21] -->
Hetter, Katia. 2016. How long will you wait in the TSA security line? CNN. [Online] 6

<!-- b000340 | references | pages [21] -->
9, 2016. [Cited: 1 20, 2017.] http://edition.cnn.com/2016/06/09/travel/tsa-security-

<!-- b000341 | references | pages [21] -->
line-wait-times-how-long/.

<!-- b000342 | references | pages [21] -->
[8]

<!-- b000343 | references | pages [21] -->
Learn.org. How Much Do Airport Security Jobs Pay? Learn.org. [Online] [Cited: 1 22,

<!-- b000344 | references | pages [21] -->
2017.] http://learn.org/articles/How_Much_Do_Airport_Security_Jobs_Pay.html.

<!-- b000345 | references | pages [21] -->
[9]

<!-- b000346 | references | pages [21] -->
PayScale.com. Security Guard Salary (United States). PayScale. [Online] [Cited: 1 22,

<!-- b000347 | references | pages [21] -->
2017.] http://www.payscale.com/research/US/Job=Security_Guard/Hourly_Rate.

<!-- b000348 | references | pages [21] -->
[10]  Taha, Hamdy A. 2014. Operations Research: Pearson New International Edition: An

<!-- b000349 | references | pages [21] -->
Introduction, 9/E. s.l. : Pearson, 2014. ISBN-10: 129202433X.

<!-- b000350 | references | pages [21] -->
[11]  Wikipedia. Queue area. Wikipedia. [Online] [Cited: 1 23, 2017.]

<!-- b000351 | references | pages [21] -->
https://en.wikipedia.org/wiki/Queue_area.

<!-- b000352 | references | pages [21] -->
[12]  Zeng, Yong, Dong, Lihua and Ma, Jianfeng. 2011. Modeling, Analysis and

<!-- b000353 | references | pages [21] -->
Simulation in Queueing Phenomena. Xi'an : Xidian Univerisity Press, 2011. pp. 92-96.

<!-- b000354 | references | pages [21] -->
ISBN 978-7-5606-2672-7.

<!-- b000355 | references | pages [21] -->
[13]  Zhao, Zhenwu and Ma, Jianjun. 2016. Tendency and Research on the Queue System

<!-- b000356 | references | pages [21] -->
of Airport Security Check. China Transportation Review. 10 2016, Vol. 38, 10, pp. 64-69.

<!-- b000357 | furniture | pages [22] -->
Team #67316

<!-- b000358 | furniture | pages [22] -->
Page 21 of 20

<!-- b000359 | heading | pages [22] -->
Appendix

<!-- b000360 | heading | pages [22] -->
13.1 Proof

<!-- b000361 | prose | pages [22] -->
Theorem: Mean waiting time of a (𝑀𝑀/𝑀𝑀/𝑘𝑘)  queueing is shorter than that of 𝑘𝑘  parallel (𝑀𝑀/𝑀𝑀/1) queueing processes (Zeng, et al., 2011; Taha, 2014). Proof: Consider 𝑘𝑘 parallel (𝑀𝑀/𝑀𝑀/1) processes, input of each server is Poisson 𝜆𝜆/𝑘𝑘. The mean queue length, (1 −𝜌𝜌1)2 ⋅𝑃𝑃0,1, where 𝜌𝜌1 = 𝜆𝜆 𝜌𝜌1 𝑘𝑘𝑘𝑘 𝐿𝐿𝑞𝑞,1 =

<!-- b000362 | prose | pages [22] -->
−1 𝜌𝜌1 = 1 −𝜌𝜌1 𝑃𝑃0,1 = ¶1 + · 1 −𝜌𝜌1 Thus, 2 𝜌𝜌1 𝐿𝐿𝑞𝑞,1 = 1 −𝜌𝜌1 And the mean waiting time (Little’s formula), 𝑊𝑊𝑞𝑞,1 = 𝐿𝐿𝑞𝑞,1 𝜌𝜌2 𝑘𝑘𝑘𝑘(1 −𝜌𝜌/𝑘𝑘) , where 𝜌𝜌= 𝜆𝜆 𝜇𝜇 𝜆𝜆/𝑘𝑘= As for the (𝑀𝑀/𝑀𝑀/𝑘𝑘) process, the input is Poisson 𝜆𝜆.

<!-- b000363 | prose | pages [22] -->
𝜌𝜌𝑘𝑘+1 (𝑘𝑘−1)! (𝑘𝑘−𝜌𝜌)2 ⋅𝑃𝑃0,2 𝐿𝐿𝑞𝑞,2 =

<!-- b000364 | prose | pages [22] -->
−1 𝑘𝑘−1 𝑃𝑃0,2 = ¹ 𝜌𝜌𝑛𝑛 + 𝜌𝜌𝑘𝑘 1 𝑘𝑘! ⋅ 1 −𝜌𝜌/𝑘𝑘º 𝑛𝑛! 𝑛𝑛=0 And thus, 𝜌𝜌𝑘𝑘+1 1 𝐿𝐿𝑞𝑞,2 = (𝑘𝑘−1)! (𝑘𝑘−𝜌𝜌)2 ⋅ 𝜌𝜌𝑛𝑛 + 𝜌𝜌𝑘𝑘 1 𝑘𝑘−1 ∑ 𝑘𝑘! ⋅ 𝑛𝑛! 1 −𝜌𝜌/𝑘𝑘 𝑛𝑛=0 The mean waiting time is given by 𝜌𝜌𝑘𝑘+1 𝑊𝑊𝑞𝑞,2 = 𝐿𝐿𝑞𝑞,2 = 1 1 𝜆𝜆⋅ 𝑘𝑘2(𝑘𝑘−1)! (1 −𝜌𝜌/𝑘𝑘)2 ⋅ 𝜌𝜌𝑛𝑛 + 𝜌𝜌𝑘𝑘 𝜆𝜆 1 𝑘𝑘−1 ∑ 𝑘𝑘! ⋅ 𝑛𝑛! 1 −𝜌𝜌/𝑘𝑘 𝑛𝑛=0

<!-- b000365 | prose | pages [22] -->
To prove that 𝑊𝑊𝑞𝑞,2 < 𝑊𝑊𝑞𝑞,1,

<!-- b000366 | prose | pages [22] -->
𝜌𝜌𝑘𝑘+1 𝜌𝜌2 ⇔1 1 𝑘𝑘𝑘𝑘(1 −𝜌𝜌/𝑘𝑘) 𝜆𝜆⋅ 𝑘𝑘2(𝑘𝑘−1)! (1 −𝜌𝜌/𝑘𝑘)2 ⋅ < 𝜌𝜌𝑛𝑛 + 𝜌𝜌𝑘𝑘 1 𝑘𝑘−1 ∑ 𝑘𝑘! ⋅ 𝑛𝑛! 1 −𝜌𝜌/𝑘𝑘 𝑛𝑛=0

<!-- b000367 | prose | pages [22, 23] -->
𝜌𝜌𝑘𝑘−1 < 1 ⇐ 𝜌𝜌𝑛𝑛 𝑘𝑘 + 𝜌𝜌𝑘𝑘 1 −𝜌𝜌 𝑘𝑘−1 𝑘𝑘! ½∑ 𝑘𝑘!¾ 𝑛𝑛! 𝑛𝑛=0 𝜌𝜌𝑘𝑘−1 = 1 𝜌𝜌< 1 ⇐ 𝑘𝑘! ½0 + 𝜌𝜌𝑘𝑘 𝑘𝑘!¾

<!-- b000368 | furniture | pages [23] -->
Team #67316

<!-- b000369 | furniture | pages [23] -->
Page 22 of 20

<!-- b000371 | prose | pages [23] -->
Since 𝜌𝜌= 𝜆𝜆/𝜇𝜇, generally we have 1 < 𝜌𝜌< 𝑘𝑘. It is true that 𝑊𝑊𝑞𝑞,2 < 𝑊𝑊𝑞𝑞,1 ∎

<!-- b000372 | heading | pages [23] -->
13.2 MATLAB Source Code for Simulation

<!-- b000373 | prose | pages [23] -->
13.2.1 simulation_simple.m

<!-- b000374 | prose | pages [23, 24] -->
1 clc; 2 clear all; 3 load leave_time_ID; 4 load peo_num_ID 5 % load peo_num;%change comments 6 i=1; 7 x_k = 4; 8 x_mu = 1/28; 9 machine_number = 5; 10 % mean_arr = 12.9870/2.7;%0.077/10 %just influence the people number 11 % final_span = 3600*10; 12 13 % peo_num = floor(span/mean_arr);%change comments 14 peo_num = peo_num_ID; 15 16 % % generate the arrival intervals of people at airport randomly 17 % peo_in = exprnd(mean_arr,1,peo_num); 18 % actual_span = sum(peo_in); 19 % peo_in = peo_in.*(span/actual_span); 20 % peo_arr = cumsum(peo_in); 21 22 % record_arr = 23 [leave_time_ID(1,:),leave_time_ID(2,:),leave_time_ID(3,:),leave_time_ID(4,:),leave_time_ID(5,:)]; 24 record_arr = (leave_time_ID(:))'; 25 record_arr(find(record_arr == 0)) = []; 26 record_arr = sort(record_arr); 27 peo_arr = record_arr; 28 29 % %generate the service time of people at airport 30 % peo_serv = gamrnd(x_k,1/(x_k*x_mu),1,peo_num); 31 32 %record the state of each security check point 33 state = zeros(3*machine_number,peo_num); 34 35 %initialize the time and intervals to leave in each array 36 leave_time = zeros(machine_number,peo_num); 37 leave_interval = zeros(machine_number,peo_num);%the time each person in arrays 38 39 %initialize the number of people waited in each array 40 count = ones(1,machine_number); 41 42 %initialize the person's data 43 for i = 1:machine_number 44 state(3*(i-1)+1,1) = peo_arr(i); 45 state(3*(i-1)+2,:) = gamrnd(x_k,1/(x_k*x_mu),1,peo_num); 46 state(3*i,1) = 0; 47 48 leave_time(i,1) = sum(state(3*(i-1)+1 : 3*i , 1));%generate the leaving time of the first 49 person in each array 50 leave_interval(i,1) = sum(state(3*(i-1)+3:3*i,1));%generate the leaving intervals of the first 51 person in each array 52 end 53 54 record_min = zeros(1,machine_number); 55 for i = machine_number+1 : peo_num 56 57 for j = 1:machine_number 58 record_min(j) = leave_time(j,count(j)); 59 end 60 [temp,min_array] = min(record_min); 61 62 count(min_array) = count(min_array) + 1; 63 state(3*(min_array-1)+1 , count(min_array) ) = peo_arr(i);%let the people in the min_ array 64 65 if state(3*(min_array-1)+1 , count(min_array) ) < state(3*(min_array-1)+2 , count(min_array)- 66 1 )... 67 +state(3*(min_array-1)+1 , 68 count(min_array)-1 )... 69 +state(3*(min_array-1)+3 , 70 count(min_array)-1 ) 71 72 state(3*(min_array) , count(min_array) ) = state(3*(min_array-1)+2 , count(min_array)- 73 1 )...

<!-- b000375 | furniture | pages [24] -->
Team #67316

<!-- b000376 | furniture | pages [24] -->
Page 23 of 20

<!-- b000378 | furniture | pages [25] -->
Team #67316

<!-- b000379 | furniture | pages [25] -->
Page 24 of 20

<!-- b000380 | prose | pages [25] -->
74 +state(3*(min_array-1)+1 , 75 count(min_array)-1 )... 76 +state(3*(min_array-1)+3 , 77 count(min_array)-1 )... 78 -state(3*(min_array-1)+1 , 79 count(min_array) ); 80 else 81 state(3*(min_array) , count(min_array) ) = 0; 82 end 83 84 leave_time(min_array,count(min_array)) = sum(state(3*(min_array-1)+1:3*min_array , 85 count(min_array) ) ); 86 leave_interval(min_array,count(min_array)) = sum(state(3*(min_array-1)+3:3*min_array , 87 count(min_array) ) ); 88 end 89 90 total = 0; 91 for i = 1:size(leave_interval,1) 92 for j = 1:size(leave_interval,2) 93 if leave_interval(i,j) ~= 0 94 total = total + leave_interval(i,j); 95 end 96 end 97 end 98 means = total/peo_num;

<!-- b000381 | prose | pages [25] -->
13.2.2 simulation_tick.m

<!-- b000382 | prose | pages [25] -->
1 clc; 2 clear all; 3 load change2; 4 5 x_k = 4; 6 x_mu = 1/28; 7 8 mean_serv = 10.5652; 9 machine_number = 5; 10 11 peo_arr = change2(2,:).*60; 12 peo_fli = change2(1,:).*60; 13 peo_num = size(change2,2);

<!-- b000383 | furniture | pages [26] -->
Team #67316

<!-- b000384 | furniture | pages [26] -->
Page 25 of 20

<!-- b000385 | prose | pages [26] -->
14 15 state = zeros(4*machine_number,peo_num); 16 %the first row is the flight time of each passenger 17 %the second row is the arrival time of each passenger 18 %the third row is the service time of each passenger 19 %the fourth row is the waiting time of each passenger 20 21 leave_time = zeros(machine_number,peo_num); 22 wait_time = zeros(machine_number,peo_num); 23 24 %initialize the state matrix 25 for i = 1:machine_number 26 state(4*(i-1)+1,1) = peo_fli(i); 27 state(4*(i-1)+2,1) = peo_arr(i); 28 %     state(4*(i-1)+3,:) = exprnd(mean_serv,1,peo_num);%service times of each machine in 29 expoential distribution 30 state(4*(i-1)+3,:) = gamrnd(x_k,1/(x_k*x_mu),1,peo_num); 31 state(4*(i-1)+4,1) = 0; 32 33 leave_time(i,1) = sum(state(4*(i-1)+2 : 4*i ,1)); 34 wait_time(i,1) = state(4*i,1); 35 end 36 37 count = ones(1,machine_number);%record the array length of each machine 38 39 queue = zeros(1,peo_num); 40 front = 1; 41 rear = 1; 42 43 scanning = machine_number+1; 44 45 record_min = zeros(1,machine_number); 46 for j = 1:machine_number 47 record_min(j) = leave_time(j,count(j)); 48 end 49 [min_time,min_array] = min(record_min); 50 51 % %push the next person into queue 52 % queue(rear) = scanning; 53 % rear = rear + 1; 54 % scanning = scanning+1;

<!-- b000386 | furniture | pages [27] -->
Team #67316

<!-- b000387 | furniture | pages [27] -->
Page 26 of 20

<!-- b000388 | prose | pages [27, 28] -->
55 56 for tick = floor(peo_arr(1)):floor(peo_fli(length(peo_fli))) 57 if tick > peo_arr(scanning) && scanning < peo_num%push the latest person into queue 58 queue(rear) = scanning; 59 rear = rear + 1; 60 %         if rear > front 61 %             temp_queue = queue(front:rear - 1); 62 %             [temp_record,temp_order] = sort(peo_fli(temp_queue)); 63 %             queue(front:rear-1) = temp_queue(temp_order); 64 %         end 65 66 scanning = scanning + 1; 67 end 68 69 %     if peo_arr(queue(front)) < min_time 70 if tick > min_time 71 if rear > front % the queue is not empty 72 count(min_array) = count(min_array) + 1; 73 state(4*(min_array-1)+1 , count(min_array) ) = peo_fli(queue(front)); 74 state(4*(min_array-1)+2 , count(min_array) ) = peo_arr(queue(front)); 75 state(4*(min_array-1)+4 , count(min_array) ) = max( min_time - peo_arr(queue(front)) , 76 0); 77 78 leave_time( min_array,count(min_array) ) = sum(state(4*(min_array-1)+2 : 79 4*(min_array) ,count(min_array))); 80 wait_time( min_array,count(min_array) ) = 81 state(4*(min_array),count(min_array));%update the leave time 82 83 front = front + 1;%pop the prior person to serve 84 85 for j = 1:machine_number 86 record_min(j) = leave_time(j,count(j)); 87 end 88 [min_time,min_array] = min(record_min);%update the min_time and the min_array 89 90 end 91 92 end 93 94 end 95 96 total = 0; 97 flag = 0; 98 for i = 1:machine_number 99 for j = 1:count(i) 100 total = total + state(4*(i-1)+1,j)-state(4*(i-1)+2,j)-state(4*(i-1)+3,j)-state(4*i,j); 101 if state(4*(i-1)+1,j)-state(4*(i-1)+2,j)-state(4*(i-1)+3,j)-state(4*i,j) < 0 102 flag = flag + 1; 103 end 104 end 105 end 106 means = total / peo_num; 107 108 summation = 0; 109 for i = 1:machine_number 110 for j = 1:count(i) 111 summation = summation + (state(4*(i-1)+1,j)-state(4*(i-1)+2,j)-state(4*(i-1)+3,j)- 112 state(4*i,j)-means)^2; 113 end 114 end 115 variance = summation / peo_num;

<!-- b000389 | furniture | pages [28] -->
Team #67316

<!-- b000390 | furniture | pages [28] -->
Page 27 of 20

<!-- b000392 | prose | pages [28] -->
13.2.3 stream.m

<!-- b000393 | prose | pages [28] -->
1 function [ total ] = stream( pretime, variance,people) 2 %UNTITLED 3 % original:pretime=120,variance=30,people=189 4 a=[-3*variance:1:3*variance]; 5 a=[a;a]; 6 a(2,1)=normcdf(a(1,1),0,variance)*people; 7 for i=2:6*variance+1 8 a(2,i)=normcdf(a(1,i),0,variance)-normcdf(a(1,i-1),0,variance); 9 a(2,i)=a(2,i)*people; 10 end 11 data=xlsread('data',2); 12 siz=size(data); 13 dataset=[]; 14 data=data*24*60; 15 for i=1:siz(1,1) 16 for j=1:siz(1,2) 17 if data(i,j)>0 18 dataset=[dataset,data(i,j)];

<!-- b000394 | furniture | pages [29] -->
Team #67316

<!-- b000395 | furniture | pages [29] -->
Page 28 of 20

<!-- b000396 | prose | pages [29] -->
19 end 20 end 21 end 22 siz=size(dataset); 23 total=zeros(1,1440); 24 for i=1:siz(1,2) 25 for j=1:variance*6+1 26 if dataset(1,i)-pretime+a(1,j)>=1 27 total(1,round(dataset(1,i)-pretime+a(1,j)))=total(1,round(dataset(1,i)- 28 pretime+a(1,j)))+a(2,j); 29 end 30 end 31 end 32 end

<!-- b000397 | prose | pages [29] -->
13.2.4 stream2.m

<!-- b000398 | prose | pages [29, 30] -->
1 function [ total ] = stream( pretime, variance,people) 2 %UNTITLED 3 % original:pretime=120,variance=30,people=189 4 a=[-3*variance:1:3*variance]; 5 a=[a;a]; 6 a(2,1)=normcdf(a(1,1),0,variance)*people; 7 for i=2:6*variance+1 8 a(2,i)=normcdf(a(1,i),0,variance)-normcdf(a(1,i-1),0,variance); 9 a(2,i)=a(2,i)*people; 10 end 11 data=xlsread('data',2); 12 siz=size(data); 13 dataset=[]; 14 data=data*24*60; 15 for i=1:siz(1,1) 16 for j=1:siz(1,2) 17 if data(i,j)>0 18 dataset=[dataset,data(i,j)]; 19 end 20 end 21 end 22 siz=size(dataset); 23 total=zeros(1,1440); 24 for i=1:siz(1,2) 25 for j=1:variance*6+1 26 if dataset(1,i)-pretime+a(1,j)>=1 27 total(1,round(dataset(1,i)-pretime+a(1,j)))=total(1,round(dataset(1,i)- 28 pretime+a(1,j)))+a(2,j); 29 end 30 end 31 end 32 end

<!-- b000399 | furniture | pages [30] -->
Team #67316

<!-- b000400 | furniture | pages [30] -->
Page 29 of 20
