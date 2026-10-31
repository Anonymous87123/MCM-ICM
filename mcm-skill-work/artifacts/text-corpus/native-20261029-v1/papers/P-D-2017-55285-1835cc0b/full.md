# P-D-2017-55285-1835cc0b

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
55285

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

<!-- b000012 | title | pages [1] -->
D

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | title | pages [1] -->
Analysis and Optimization to the Process of Airport

<!-- b000018 | title | pages [1] -->
Security Check

<!-- b000019 | heading | pages [1] -->
Summary

<!-- b000020 | prose | pages [1] -->
Security check is essential to the safety of airline passengers. However, it is also a time consuming process. Passengers have to wait in lines, get ID check, prepare the belong- ings and get screening inspection and sometimes it even takes hours of time to ﬁnish. Besides, the variance of the waiting time in the checkpoints line is also very high, which is difﬁcult for passengers to decide when to reach the airport. Therefore, we are required to ﬁgure out the potential issues and make some modiﬁcations to the current process that can reduce the average waiting time and its variance.

<!-- b000021 | prose | pages [1] -->
We develop the basic model to simulate the current situation of American airports’ security check and study the properties of Pre-Check policy. Though more ‘Pre-Check’ passengers can help alleviate congestion to some degree, the time in the process of wait for screening is the overwhelming majority of the time spent in security check. It occupy over 98% of total time during rush hours. In addition, we also plot the distribution of different total waiting time, and ﬁnd that it is nearly a uniform distribution over several hours. The variance is hence too high for passengers to predict their total waiting time.

<!-- b000022 | prose | pages [1] -->
Based on this conclusion, we mainly build two efﬁcient modiﬁcation models to opti- mize the current situation. The ﬁrst one is ‘multi-passenger linkage model of belong- ings preparation (MPL)’. It shows that if the airport opens up a small zone for several passengers to prepare for screening at the same time, the average time and variance will obviously decrease. The other one is ‘priority-based queuing model (PBQ)’. It suggests airports to set some appropriate time interval limits to provide passengers who is to take off with great convenience without increasing the average time. Besides, it can encour- age people not to arrive at airports so early that aggravate congestion.

<!-- b000023 | prose | pages [1] -->
We also speculate about the TSA’s latest institution for the elderly and children, but it does not make much contribution. At last, we consider the Chinese cultural norms and apply our model to Chinese airports. We construct the cut-in-line model. The result shows that MPL and PBQ models can still keep their high effectiveness. In other word, our models have high stability, high error-tolerant rate and extensive applicability.

<!-- b000024 | keywords | pages [1] -->
Keywords: Security Check; Poisson Distribution; Gaussian Distribution; Queuing Meth-

<!-- b000025 | prose | pages [1] -->
ods

<!-- b000026 | furniture | pages [2] -->
Team # 55285

<!-- b000027 | furniture | pages [2] -->
Page 1 of 32

<!-- b000028 | prose | pages [2] -->
Analysis and Optimization to the Process of Airport

<!-- b000029 | prose | pages [2] -->
Security Check

<!-- b000030 | prose | pages [2] -->
January 24, 2017

<!-- b000031 | heading | pages [2] -->
Contents

<!-- b000032 | contents | pages [2] -->
1

<!-- b000033 | contents | pages [2] -->
Restatement of the Problem

<!-- b000034 | contents | pages [2] -->
3

<!-- b000035 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
1.1

<!-- b000037 | contents | pages [2] -->
Background

<!-- b000038 | contents | pages [2] -->
3

<!-- b000039 | contents | pages [2] -->
An Overview of the Problem . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
1.1.1

<!-- b000041 | contents | pages [2] -->
3

<!-- b000042 | contents | pages [2] -->
The Process of Security Check . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
1.1.2

<!-- b000044 | contents | pages [2] -->
3

<!-- b000045 | contents | pages [2] -->
literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
1.2

<!-- b000047 | contents | pages [2] -->
3

<!-- b000048 | contents | pages [2] -->
The Task at Hand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
1.3

<!-- b000050 | contents | pages [2] -->
2

<!-- b000051 | heading | pages [2] -->
Model Assumptions and Notations

<!-- b000052 | prose | pages [2] -->
4

<!-- b000053 | prose | pages [2] -->
4

<!-- b000054 | prose | pages [2] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4

<!-- b000055 | prose | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 5

<!-- b000056 | heading | pages [2] -->
The Basic Model of Security Checkpoints

<!-- b000057 | prose | pages [2] -->
3 6

<!-- b000058 | prose | pages [2] -->
The Design of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 6

<!-- b000059 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 Sub Models 6

<!-- b000060 | prose | pages [2] -->
Inﬂow Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1 6

<!-- b000061 | prose | pages [2] -->
Attributes Generation Model . . . . . . . . . . . . . . . . . . . . . . 3.2.2 6

<!-- b000062 | prose | pages [2] -->
Queuing Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.3 7

<!-- b000063 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.4 Screening Model 7

<!-- b000064 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 The Result of the Model 8

<!-- b000065 | prose | pages [2] -->
The Distribution of the Total Time T . . . . . . . . . . . . . . . . . . 3.3.1 8

<!-- b000066 | prose | pages [2] -->
The proportion of the Time Spent in Different Steps . . . . . . . . . 3.3.2 8

<!-- b000067 | prose | pages [2] -->
The Inﬂuence of the Ratio of Pre-Check Passengers and Regular 3.3.3 Passengers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | prose | pages [2] -->
8

<!-- b000069 | prose | pages [2] -->
The Inﬂuence of the Ratio of Pre-Check Lanes and Regular Lanes . 3.3.4

<!-- b000070 | prose | pages [2] -->
4 Modiﬁcations to the Current Process

<!-- b000071 | prose | pages [2] -->
10

<!-- b000072 | prose | pages [2] -->
10

<!-- b000073 | furniture | pages [3] -->
Team # 55285

<!-- b000074 | furniture | pages [3] -->
Page 2 of 32

<!-- b000075 | prose | pages [3] -->
Multi-passenger Linkage Model of Belongings Preparation . . . . . . . . . 4.1 11

<!-- b000076 | prose | pages [3] -->
The Design of MPL Model . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 11

<!-- b000077 | prose | pages [3] -->
The Effectiveness of MPL Model . . . . . . . . . . . . . . . . . . . . 4.1.2 11

<!-- b000078 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Priority-based Queuing Model 12

<!-- b000079 | prose | pages [3] -->
The Design of PBQ Model . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 12

<!-- b000080 | prose | pages [3] -->
The Effectiveness of PBQ Model 4.2.2 . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | prose | pages [3] -->
13

<!-- b000082 | prose | pages [3] -->
Model of Special Population . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 14

<!-- b000083 | prose | pages [3] -->
The Design of SP Model . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.1 14

<!-- b000084 | prose | pages [3] -->
The Effectiveness of SP Model 4.3.2 . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | prose | pages [3] -->
15

<!-- b000086 | heading | pages [3] -->
Model Evaluation & Sensitivity Analysis

<!-- b000087 | prose | pages [3] -->
5 15

<!-- b000088 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 The Cut-in-line Model 15

<!-- b000089 | prose | pages [3] -->
The Sensitivity of MPL Model . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 16

<!-- b000090 | prose | pages [3] -->
The Sensitivity of PBQ Model . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000091 | prose | pages [3] -->
6

<!-- b000092 | heading | pages [3] -->
Conclusion

<!-- b000093 | prose | pages [3] -->
17

<!-- b000094 | prose | pages [3] -->
18

<!-- b000095 | prose | pages [3] -->
Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 18

<!-- b000096 | prose | pages [3] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.1 18

<!-- b000097 | prose | pages [3] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.2 18

<!-- b000098 | prose | pages [3] -->
Suggestions to the Security Manager . . . . . . . . . . . . . . . . . . . . . . 6.2 18

<!-- b000099 | prose | pages [3] -->
Future Plans . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3

<!-- b000100 | heading | pages [3] -->
Appendices

<!-- b000101 | heading | pages [3] -->
Appendix A Simulation Code

<!-- b000102 | prose | pages [3] -->
7 Other ﬁgures

<!-- b000103 | prose | pages [3] -->
19

<!-- b000104 | prose | pages [3] -->
20

<!-- b000105 | prose | pages [3] -->
20

<!-- b000106 | prose | pages [3] -->
30

<!-- b000107 | prose | pages [3] -->
Figures in ‘Modiﬁcations to the Current Process’ . . . . . . . . . . . . . . . 7.1 30

<!-- b000108 | prose | pages [3] -->
Figures in ‘Model Evaluation & Sensitivity Analysis’ . . . . . . . . . . . . . 7.2 30

<!-- b000109 | furniture | pages [4] -->
Team # 55285

<!-- b000110 | furniture | pages [4] -->
Page 3 of 32

<!-- b000111 | prose | pages [4] -->
1 Restatement of the Problem

<!-- b000112 | prose | pages [4] -->
1.1

<!-- b000113 | heading | pages [4] -->
Background

<!-- b000114 | prose | pages [4] -->
1.1.1 An Overview of the Problem

<!-- b000115 | prose | pages [4] -->
In recent years, as the threat of terrorism is upgrading, American society has attached great signiﬁcance to the security of the airport. A key part of the security measures at the airport is security checkpoints, where the passengers and their belongings should be inspected for dangerous objects. However, if the passengers takes a long time to pass the security checkpoints, there will be a negative impact on the customers’ feelings, then the interests of the airlines can be inﬂuenced.

<!-- b000116 | prose | pages [4] -->
There are two major problems in Chicago’s O’Hare international airport and other American airports. First, it is annoying that there are sometimes over-long queues at the airports, but we cannot give an explanation or a prediction. Second, the variance of waiting time is high, that is to say, it is difﬁcult for the travelers to ﬁnd a suitable time to reach the airport without being unnecessarily early or missing the plane. Therefore it makes great sense to solve the congestion problem.

<!-- b000117 | prose | pages [4] -->
1.1.2 The Process of Security Check

<!-- b000118 | prose | pages [4] -->
The process of security check can be decomposed into following processes:

<!-- b000119 | prose | pages [4] -->
• Arriving process: Passengers are assigned at the beginning of our model.

<!-- b000120 | prose | pages [4] -->
• Process of waiting at the checkpoints: Passengers wait at the checkpoints in Zone A and then move to the subsequent queue in Zone B.

<!-- b000121 | prose | pages [4] -->
• ID check process: Passengers get the identiﬁcation check in this process.

<!-- b000122 | prose | pages [4] -->
• Process of waiting for screening: Passengers wait in lanes for screening.

<!-- b000123 | prose | pages [4] -->
• Preparing process: After reaching the front of the line, passengers place their be- longings, including their jackets, liquid containers, computers and so on.

<!-- b000124 | prose | pages [4] -->
• Screening process: Passengers get screened by the millimeter scanner while the goods are scanned by the X-ray, then they retrieve their belongings.

<!-- b000125 | prose | pages [4] -->
• Additional inspection process: If the passengers fail in the screening process, they should get additional inspections in Zone D.

<!-- b000126 | prose | pages [4] -->
1.2 literature review

<!-- b000127 | prose | pages [4] -->
To simplify the problem and facilitate the implementation of computer language, researchers treat time as a discrete variable in the analysis of a single-server queuing system at ﬁrst[1]. After that, some people have applied Queuing Theory to the dynamic allocation of airport security resources, which used pure Markov chain, discontinuous Markov process, Poisson process, statistical properties of transition probability equation and the birth and death process[2] [3]. What’s more, some other people try to achieve a

<!-- b000128 | furniture | pages [5] -->
Team # 55285

<!-- b000129 | furniture | pages [5] -->
Page 4 of 32

<!-- b000130 | prose | pages [5] -->
goal of virtual queuing instead of real one in order to get a smoother distribution of ar- riving passengers[4]. We expect to ﬁnd some convenient and intuitive modiﬁcations for the airport security based on the previous wisdom and some necessary math knowledge like Queuing Theory, Probability and Statistics[5].

<!-- b000131 | prose | pages [5] -->
1.3 The Task at Hand

<!-- b000132 | prose | pages [5] -->
• Construct a mathematical model to simulate the situation of the current security checkpoints and ﬁnd an explanation for the phenomenon of congestion.

<!-- b000133 | prose | pages [5] -->
• Propose some modiﬁcations to improve the current process.

<!-- b000134 | prose | pages [5] -->
• Take the various behaviors of travelers into consideration, then discuss the inﬂu- ence of those factors on the model.

<!-- b000135 | prose | pages [5] -->
• On the basis of the model, give some policy and procedural suggestions to amelio- rate the situation of the security checkpoints.

<!-- b000136 | prose | pages [5] -->
2

<!-- b000137 | heading | pages [5] -->
Model Assumptions and Notations

<!-- b000138 | prose | pages [5] -->
2.1

<!-- b000139 | heading | pages [5] -->
Assumptions and Justiﬁcations

<!-- b000140 | prose | pages [5] -->
In order to simplify the course of modeling and draw some reasonable conclusions from our model, we make assumptions as follows:

<!-- b000141 | prose | pages [5] -->
• The excel data can embody the overall level of the airport to some degree. We use the differential method to calculate out the mean value and the standard deviation of the time consumed in different processes.

<!-- b000142 | prose | pages [5] -->
• The intervals of the passengers’ arrivals obey Poisson distribution. Because the time when a passenger arrives is unrelated to that of the last passenger, therefore we assume that the intervals of the passengers’ arrivals obey Poisson distribution. The mean values of the distribution are obtained from the excel data.

<!-- b000143 | prose | pages [5] -->
• The time of ID check and millimeter wave scanning obeys Gaussian distribution.

<!-- b000144 | prose | pages [5] -->
In this two processes, we suppose that the staff of the airport are skillful, that is to say the time cost in these processes ﬂuctuates around a mean value. Thus we assume that they obey Gaussian distribution. The mean values and the standard deviations are also calculated out according to the excel data.

<!-- b000145 | prose | pages [5] -->
• The time interval of two examinations is 11s to pass the X-ray scanning and the time interval between two placements is 2s. According to the excel data, we can see that the interval is sometimes around 2s and sometimes around 11s. We interpret it as: in one time of examination, the inspector inspects several pieces of luggage. There are time intervals between each examinations.

<!-- b000146 | prose | pages [5] -->
• All of the passengers know the rules of the airport. They will go to the back of the shortest queue after arrival.

<!-- b000147 | furniture | pages [6] -->
Team # 55285

<!-- b000148 | furniture | pages [6] -->
Page 5 of 32

<!-- b000149 | prose | pages [6] -->
• There are no emergency incidents happened in the airport. What we discuss is the airport in order and it is clear that any emergency incident can break the order of any airport.

<!-- b000150 | prose | pages [6] -->
• Pre-Check passengers can choose to go through the regular passage of security check when the Pre-Check passage is crowded. As for Pre-Check passengers, it takes them the same time either in Pre-Check passages or in regular passages.

<!-- b000151 | prose | pages [6] -->
• The time of preparing the belongings is 15 ± 5 + 5X s in the Pre-Check passage, while it is 45±10+5X s in the ordinary passage. This is based on our experiments. X is the number of the pieces of luggage.

<!-- b000152 | prose | pages [6] -->
• In our model, there are 4 ID checkpoints in Zone A and 4 checking lanes in Zone B.

<!-- b000153 | prose | pages [6] -->
• We do not take the transiting time between different stations into consideration.

<!-- b000154 | prose | pages [6] -->
2.2

<!-- b000155 | heading | pages [6] -->
Notations

<!-- b000156 | prose | pages [6] -->
Here we list the symbols and notations used in this paper, as shown in Table 1. Some of them will be deﬁned later in the following sections.

<!-- b000157 | caption | pages [6] -->
Table 1: Notations

<!-- b000158 | prose | pages [6] -->
Symbol Description ta the time interval between two passengers’ arrivals tp the time interval between two Pre-Check passengers’ arrivals tr the time interval between two regular passengers’ arrivals twaitA the time of waiting at Zone A twaitB the time of waiting at Zone B tcheck the time of identiﬁcation check σcheck the standard deviation of tcheck txray the time of X-ray scanning tmilli the time of millimeter wave scanning tpre the time of preparing σpre the standard deviation of tpre tscreening the time of screening T the total time of the security check of a single person Tavg the total time of the security check process of a group of people σT the standard deviation of Tavg Tr the total time consumed by regular passengers Tp the total time consumed by Pre-Check passengers σTr the standard deviation of Tr σTp the standard deviation of Tp Nprepare the number of passengers preparing their belongings Rpassenger the ratio of tp to tr Rlane the ratio of Pre-Check lanes to regular lanes Royp the percentage of people over 70 or under 12 Rcut the percentage of people who cut in line

<!-- b000159 | furniture | pages [7] -->
Team # 55285

<!-- b000160 | furniture | pages [7] -->
Page 6 of 32

<!-- b000161 | heading | pages [7] -->
The Basic Model of Security Checkpoints

<!-- b000162 | prose | pages [7] -->
3

<!-- b000163 | prose | pages [7] -->
In this section, we develop the basic model to explain the current situation of Amer- ican airports. The basic model simulates the processes mentioned in Section 1.1.2. Then we discover that the process of waiting for screening is the most time consuming. The Pre-Check policy of TSA is effective, but we need to ﬁnd more strategies to solve the problem.

<!-- b000164 | prose | pages [7] -->
3.1

<!-- b000165 | heading | pages [7] -->
The Design of the Model

<!-- b000166 | prose | pages [7] -->
In order to demonstrate our basic model clearly, we divide it into the four following sub models.

<!-- b000167 | prose | pages [7] -->
• Inﬂow model: This model is designed to simulate the random arrivals of the pas- sengers.

<!-- b000168 | prose | pages [7] -->
• Sub model two: Attributes generating model: In this model, we attribute different properties to the passengers that will inﬂuence the time length of security check.

<!-- b000169 | prose | pages [7] -->
• Queuing model: This model studies the process of waiting in lines.

<!-- b000170 | prose | pages [7] -->
• Screening model: The preparing process and the screening process are discussed in this model.

<!-- b000171 | prose | pages [7] -->
3.2

<!-- b000172 | heading | pages [7] -->
Sub Models

<!-- b000173 | prose | pages [7] -->
3.2.1

<!-- b000174 | heading | pages [7] -->
Inﬂow Model

<!-- b000175 | prose | pages [7] -->
The inﬂow model simulates the stochastic arrivals of passengers at the entrance of the airport. According to the excel data, we can obtain that the average time interval of passengers’ arrivals. We can assume that the arrival of each passenger obeys Poisson distribution in Equation (1). λ is the average time interval between the arrivals of two passengers according to the excel data, and N is the number of seconds between the arrivals of two passengers in our stochastic process.

<!-- b000176 | prose | pages [7] -->
P(t = N) = e−λ λN

<!-- b000177 | prose | pages [7] -->
3.2.2

<!-- b000178 | heading | pages [7] -->
Attributes Generation Model

<!-- b000179 | prose | pages [7] -->
(1) N!

<!-- b000180 | prose | pages [7] -->
After a passenger is assigned in the program, we give some relevant attributes to the passengers, including the time for ID check, the time for millimeter wave scanning, the pieces of luggage they carry, the time for preparing the personal belongings and whether the passenger has enrolled in ‘Pre-Check’. We assume that the ﬁrst two factors obey Gaussian distribution in Equation (2). Then we calculate the mean value and the standard deviation of the ﬁrst three affecting factors. Those of the fourth one are given in the assumptions.

<!-- b000181 | prose | pages [7] -->
1

<!-- b000182 | prose | pages [7] -->
√

<!-- b000183 | prose | pages [7] -->
ti = σi

<!-- b000184 | prose | pages [7] -->
−(x−µi)2

<!-- b000185 | prose | pages [7] -->
2σ2

<!-- b000186 | prose | pages [7] -->
2πe

<!-- b000187 | prose | pages [7] -->
(2) i

<!-- b000188 | furniture | pages [8] -->
Team # 55285

<!-- b000189 | furniture | pages [8] -->
Page 7 of 32

<!-- b000190 | prose | pages [8] -->
The mean value and the standard are listed in Table 2

<!-- b000191 | caption | pages [8] -->
Table 2: the Attributes of the Generated Passengers and Their Mean Values and Standard

<!-- b000192 | prose | pages [8] -->
Deviations

<!-- b000193 | prose | pages [8] -->
Mean Value(µi/s) Attributes(ti) tcheck 11.31 tmilli 11.64 tpre_r 45 tpre_p 15

<!-- b000194 | prose | pages [8] -->
3.2.3

<!-- b000195 | heading | pages [8] -->
Queuing Model

<!-- b000196 | prose | pages [8] -->
Standard Deviation(σi/s) 3.70 5.82 10 5

<!-- b000197 | prose | pages [8] -->
After the arrival of the passengers, they will automatically go to the back of the short- est queue. Then, we use a queuing model to simulate the process that the passengers are waiting in lines. We treat each waiting line of the airport as a queue in our program. The ﬁrst passenger added to the queue will be the ﬁrst to get out as Figure 1 demonstrates.

<!-- b000198 | prose | pages [8] -->
At the front of the queue, the rate of removing each passenger from the queue is determined in the attribute generation model.

<!-- b000199 | prose | pages [8] -->
Step1 Step2 Step3 Step4

<!-- b000200 | prose | pages [8] -->
···

<!-- b000201 | prose | pages [8] -->
···

<!-- b000202 | prose | pages [8] -->
Regular Regular

<!-- b000203 | prose | pages [8] -->
···

<!-- b000204 | prose | pages [8] -->
···

<!-- b000205 | prose | pages [8] -->
···

<!-- b000206 | prose | pages [8] -->
Regular

<!-- b000207 | prose | pages [8] -->
···

<!-- b000208 | prose | pages [8] -->
···

<!-- b000209 | prose | pages [8] -->
Regular Regular

<!-- b000210 | prose | pages [8] -->
Regular

<!-- b000211 | prose | pages [8] -->
Regular

<!-- b000212 | prose | pages [8] -->
···

<!-- b000213 | prose | pages [8] -->
···

<!-- b000214 | prose | pages [8] -->
PreCheck PreCheck

<!-- b000215 | prose | pages [8] -->
PreCheck PreCheck PreCheck

<!-- b000216 | prose | pages [8] -->
Wait For

<!-- b000217 | prose | pages [8] -->
Take Document

<!-- b000218 | prose | pages [8] -->
Reach Airpot

<!-- b000219 | prose | pages [8] -->
Wait For Screen

<!-- b000220 | prose | pages [8] -->
Document Check

<!-- b000221 | prose | pages [8] -->
Check

<!-- b000222 | prose | pages [8] -->
Regular PreCheck All

<!-- b000223 | prose | pages [8] -->
Step5 Step6 Step7

<!-- b000224 | prose | pages [8] -->
···

<!-- b000225 | prose | pages [8] -->
Body Scanning

<!-- b000226 | prose | pages [8] -->
···

<!-- b000227 | prose | pages [8] -->
Regular

<!-- b000228 | prose | pages [8] -->
Get Baggages

<!-- b000229 | prose | pages [8] -->
Baggage Screen

<!-- b000230 | prose | pages [8] -->
PreCheck

<!-- b000231 | prose | pages [8] -->
Prepare For

<!-- b000232 | prose | pages [8] -->
Screen Additional Screen Screen

<!-- b000233 | caption | pages [8] -->
Figure 1: The Queuing Model

<!-- b000234 | prose | pages [8] -->
3.2.4

<!-- b000235 | heading | pages [8] -->
Screening Model

<!-- b000236 | prose | pages [8] -->
When the passengers ﬁnished queuing, they ﬁrst begin to prepare their belongings. Then the passengers and their belongings are scanned respectively. The time cost in this process should be the maximum of the millimeter wave scanning time tmilli and the

<!-- b000237 | furniture | pages [9] -->
Team # 55285

<!-- b000238 | prose | pages [9] -->
X-ray scanning time txray.

<!-- b000239 | furniture | pages [9] -->
Page 8 of 32

<!-- b000240 | prose | pages [9] -->
tscreening = max[tmilli, txray]

<!-- b000241 | prose | pages [9] -->
3.3

<!-- b000242 | heading | pages [9] -->
The Result of the Model

<!-- b000243 | prose | pages [9] -->
(3)

<!-- b000244 | prose | pages [9] -->
We use c++ to realize the model programmatically and get a set of virtue data, then we process the data to see the cause of congestion.

<!-- b000245 | prose | pages [9] -->
The Distribution of the Total Time T 3.3.1

<!-- b000246 | prose | pages [9] -->
First we want to ﬁgure out how T, the total time consumed in the security check dis- tribute among the travelling populations. We pick out 31678 samples, obtain their total times, and plot Figure 2. According to Figure 2, the total time distribute very uniformly among the populations. That is to say, the probability of the different total time is simi- lar. That explains why it is difﬁcult for passengers to ﬁnd a suitable time to arrive at the airport.

<!-- b000247 | prose | pages [9] -->
Total Time Distribution

<!-- b000248 | prose | pages [9] -->
500

<!-- b000249 | prose | pages [9] -->
Amount

<!-- b000250 | prose | pages [9] -->
400

<!-- b000251 | prose | pages [9] -->
300

<!-- b000252 | prose | pages [9] -->
200

<!-- b000253 | prose | pages [9] -->
100

<!-- b000254 | prose | pages [9] -->
0

<!-- b000255 | prose | pages [9] -->
200 400 600

<!-- b000256 | prose | pages [9] -->
Total Time Distribution

<!-- b000257 | prose | pages [9] -->
Total Time Distribution

<!-- b000258 | prose | pages [9] -->
Entries

<!-- b000259 | prose | pages [9] -->
Entries

<!-- b000260 | prose | pages [9] -->
31678

<!-- b000261 | prose | pages [9] -->
31678

<!-- b000262 | prose | pages [9] -->
Mean

<!-- b000263 | prose | pages [9] -->
Mean

<!-- b000264 | prose | pages [9] -->
518.6

<!-- b000265 | prose | pages [9] -->
518.6

<!-- b000266 | prose | pages [9] -->
RMS

<!-- b000267 | prose | pages [9] -->
RMS

<!-- b000268 | prose | pages [9] -->
269.2

<!-- b000269 | prose | pages [9] -->
269.2

<!-- b000270 | prose | pages [9] -->
800 1000 1200 Total Time [second]

<!-- b000271 | caption | pages [9] -->
Figure 2: The Distribution of the Total Time

<!-- b000272 | prose | pages [9] -->
The proportion of the Time Spent in Different Steps 3.3.2

<!-- b000273 | prose | pages [9] -->
Then we consider the proportion of the time consumed in different steps, and draw ﬁgure 3. We can see that the time of waiting for screening is very large in proportion to the rest of time. That is the main reason for the congestion of the airport.

<!-- b000274 | prose | pages [9] -->
The Inﬂuence of the Ratio of Pre-Check Passengers and Regular Passengers 3.3.3

<!-- b000275 | prose | pages [9] -->
From Figure 4 and Figure 5 we can view that the curve is in the shape of letter ‘S’. The Tavg converges to a constant as the percentage of Pre-Check passengers grows. This is easy to understand.

<!-- b000276 | furniture | pages [10] -->
Team # 55285

<!-- b000277 | furniture | pages [10] -->
Page 9 of 32

<!-- b000278 | prose | pages [10] -->
Percentage of Time Spent on Each Process

<!-- b000279 | prose | pages [10] -->
Waiting at ID Checkpoints 0.11%

<!-- b000280 | prose | pages [10] -->
Waiting for Screening 98.11%

<!-- b000281 | prose | pages [10] -->
ID Check 0.30%

<!-- b000282 | prose | pages [10] -->
Preparing for Screening 0.66% Additional Screening 0.07% Screening 0.75%

<!-- b000283 | prose | pages [10] -->
Highcharts.com

<!-- b000284 | caption | pages [10] -->
Figure 3: The Percentage of Time in Different Process

<!-- b000285 | prose | pages [10] -->
8 5

<!-- b000286 | prose | pages [10] -->
Equation y = A/(1+exp(-B*(x-C)^D))+E Adj. R-Squ 0.99315

<!-- b000287 | prose | pages [10] -->
8 0

<!-- b000288 | prose | pages [10] -->
Value Standard E Averge Wa A 617.58024 9.25894 Averge Wa B 0.005 9.55053E-

<!-- b000289 | prose | pages [10] -->
7 5

<!-- b000290 | prose | pages [10] -->
Averge Wa C 0.09962 9.6187E-6 Averge Wa D 3.0284 0.10629

<!-- b000291 | prose | pages [10] -->
7 0

<!-- b000292 | prose | pages [10] -->
Averge Wa E 196.41502 6.11854

<!-- b000293 | prose | pages [10] -->
6 5

<!-- b000294 | prose | pages [10] -->
a v g ( s

<!-- b000295 | prose | pages [10] -->
6 0

<!-- b000296 | prose | pages [10] -->
5 5

<!-- b000297 | prose | pages [10] -->
5 0

<!-- b000298 | prose | pages [10] -->
4 5

<!-- b000299 | prose | pages [10] -->
R l a n e = 1 : 3

<!-- b000300 | prose | pages [10] -->
F i t o f R l a n e = 1 : 3

<!-- b000301 | prose | pages [10] -->
1

<!-- b000302 | prose | pages [10] -->
p a s s e n g e

<!-- b000303 | caption | pages [10] -->
Figure 4: The Total Time Curves of Different Rpassengers

<!-- b000304 | prose | pages [10] -->
Equation y = A/(1+exp(-B*(x-C)^D))+E

<!-- b000305 | prose | pages [10] -->
5 5

<!-- b000306 | prose | pages [10] -->
Adj. R-Square 0.98763

<!-- b000307 | prose | pages [10] -->
Value Standard Error

<!-- b000308 | prose | pages [10] -->
5 0

<!-- b000309 | prose | pages [10] -->
Stanard Error A 545.84726 8.45339

<!-- b000310 | prose | pages [10] -->
Stanard Error B 0.01102 0.00263

<!-- b000311 | prose | pages [10] -->
Stanard Error C 0.09955 2.52643E-5

<!-- b000312 | prose | pages [10] -->
4 5

<!-- b000313 | prose | pages [10] -->
Stanard Error D 2.94864 0.14403

<!-- b000314 | prose | pages [10] -->
Stanard Error E -22.46356 6.76615

<!-- b000315 | prose | pages [10] -->
4 0

<!-- b000316 | prose | pages [10] -->
σΤ ( s

<!-- b000317 | prose | pages [10] -->
3 5

<!-- b000318 | prose | pages [10] -->
3 0

<!-- b000319 | prose | pages [10] -->
2 5

<!-- b000320 | prose | pages [10] -->
R l a n e = 1 : 3

<!-- b000321 | prose | pages [10] -->
F i t o f R l a n e = 1 : 3

<!-- b000322 | prose | pages [10] -->
1

<!-- b000323 | prose | pages [10] -->
p a s s e n g e

<!-- b000324 | caption | pages [10] -->
Figure 5: The Standard Deviation Curves of Different Rpassengers

<!-- b000325 | furniture | pages [11] -->
Team # 55285

<!-- b000326 | furniture | pages [11] -->
Page 10 of 32

<!-- b000327 | prose | pages [11] -->
We know that the more Pre-Check passengers, the smaller average time. Therefore, Tavg will ﬁnally converge to the value when everyone can use Pre-Check lane and spend less time, just like the ‘S’ curve of the Natural Growth Model (NGM) in biolagy. We try to use one function of the NGM, Equation (4), to ﬁt the data. The correlation coefﬁcient of the ﬁtting is 0.99, which conﬁrms our thoughts.

<!-- b000328 | prose | pages [11] -->
y = A/(1 + exp(−B(x −C)D)) + E (4)

<!-- b000329 | prose | pages [11] -->
The Inﬂuence of the Ratio of Pre-Check Lanes and Regular Lanes 3.3.4

<!-- b000330 | prose | pages [11] -->
First, we study the inﬂuence of the Rlane, the ratio of Pre-Check lanes and Regular lanes. We consider the three different conditions, when the Rlane is 1:3, 2:2 and 3:1. Our purpose is to ﬁnd an optimal ratio to satisfy the following two requirements:

<!-- b000331 | prose | pages [11] -->
1. Minimize the waiting time.

<!-- b000332 | prose | pages [11] -->
2. When the ratio of the Pre-Check and Regular passengers varies, the variance can be controlled in a small range.

<!-- b000333 | prose | pages [11] -->
For every condition, we change Rpassenger and test the average waiting time. Then we plot the ﬁgure and set Rpassenger as x-axis and the average waiting time t as y-axis to see the tendency in different conditions.

<!-- b000334 | prose | pages [11] -->
As is shown in Figure 6 and Figure 7 , when Rlane is 1:3, the average waiting time and its variance is rather small and stable when we change a series of different Rpassenger. That is to say, the ratio set by the airport is reasonable.

<!-- b000335 | prose | pages [11] -->
a v g ( s

<!-- b000336 | prose | pages [11] -->
1 0 0

<!-- b000337 | prose | pages [11] -->
p a s s e n g e

<!-- b000338 | prose | pages [11] -->
R l a n e = 1 : 3

<!-- b000339 | prose | pages [11] -->
R l a n e = 2 : 2

<!-- b000340 | prose | pages [11] -->
R l a n e = 3 : 1

<!-- b000341 | prose | pages [11] -->
F i t o f R l a n e = 1 : 3

<!-- b000342 | prose | pages [11] -->
F i t o f R l a n e = 2 : 2

<!-- b000343 | prose | pages [11] -->
F i t o f R l a n e = 3 : 1

<!-- b000344 | prose | pages [11] -->
1

<!-- b000345 | caption | pages [11] -->
Figure 6: The Total Time Curves of Different Rlane

<!-- b000346 | prose | pages [11] -->
Modiﬁcations to the Current Process 4

<!-- b000347 | prose | pages [11] -->
According to the ﬁrst model, the allocation of the four lanes and the percentage of Pre-Check passengers are both optimal, however, congestion still happens at the airport. Thus, we need to ﬁnd more strategies to improve the institution of security check. In this section, we build three extra models to modify the current process, which are:

<!-- b000348 | furniture | pages [12] -->
Team # 55285

<!-- b000349 | prose | pages [12] -->
4 0 0

<!-- b000350 | prose | pages [12] -->
3 5 0

<!-- b000351 | prose | pages [12] -->
3 0 0

<!-- b000352 | prose | pages [12] -->
2 5 0

<!-- b000353 | prose | pages [12] -->
2 0 0

<!-- b000354 | prose | pages [12] -->
σΤ ( s

<!-- b000355 | prose | pages [12] -->
1 5 0

<!-- b000356 | prose | pages [12] -->
1 0 0

<!-- b000357 | prose | pages [12] -->
5 0

<!-- b000358 | furniture | pages [12] -->
Page 11 of 32

<!-- b000359 | prose | pages [12] -->
R l a n e = 1 : 3

<!-- b000360 | prose | pages [12] -->
R l a n e = 2 : 2

<!-- b000361 | prose | pages [12] -->
R l a n e = 3 : 1

<!-- b000362 | prose | pages [12] -->
F i t o f R l a n e = 1 : 3

<!-- b000363 | prose | pages [12] -->
F i t o f R l a n e = 2 : 2

<!-- b000364 | prose | pages [12] -->
F i t o f R l a n e = 3 : 1

<!-- b000365 | prose | pages [12] -->
1

<!-- b000366 | prose | pages [12] -->
p a s s e n g e

<!-- b000367 | caption | pages [12] -->
Figure 7: The Standard Deviation Curves of Different Rlane

<!-- b000368 | prose | pages [12] -->
• Multi-passenger linkage model of belongings preparation (MPL model)

<!-- b000369 | prose | pages [12] -->
• Priority-based queuing model(PBQ model)

<!-- b000370 | prose | pages [12] -->
• Model of special population (SP model)

<!-- b000371 | heading | pages [12] -->
Multi-passenger Linkage Model of Belongings Preparation

<!-- b000372 | prose | pages [12] -->
4.1

<!-- b000373 | prose | pages [12] -->
4.1.1

<!-- b000374 | heading | pages [12] -->
The Design of MPL Model

<!-- b000375 | prose | pages [12] -->
As is mentioned in Section 3, congestion mostly happens in the process of waiting for screening. In the previous model, a passenger cannot begin preparing his or her belongings until the last passenger ﬁnishes preparing. It is obvious that we can save more time in this process. Therefore, we make the following improvements.

<!-- b000376 | prose | pages [12] -->
Suppose every checkpoint can allow Nprepare passengers to prepare their belongings at the same time. Once a passenger ﬁnished preparing and started the screening process, another passenger at the front of the waiting line can join the preparing process. In this linkage process, we can guarantee that there are always several passengers preparing their belongings together. Though the preparing time of a certain passenger does not decline, the waiting time of other passengers is lessened.

<!-- b000377 | prose | pages [12] -->
4.1.2

<!-- b000378 | heading | pages [12] -->
The Effectiveness of MPL Model

<!-- b000379 | prose | pages [12] -->
Then we are to ﬁnd the optimal Nprepare that can reduce the waiting time while the preparing area is not very crowded. As is shown in Figure 8 and Figure 9, we can see that when Nprepare = 3, the total time Tavg is signiﬁcantly reduced. When the Nprepare reaches 4 and 5, the change is not obvious but the area is more crowded. Therefore, we can conclude that three-passenger linkage model is the best strategy. After the MPL modiﬁcation, we draw the proportion of the time in different processes again. As is shown in Figure 11, the time consumed in the process of waiting for screening is reduced from 98.11% to 57.21%.

<!-- b000380 | furniture | pages [13] -->
Team # 55285

<!-- b000381 | prose | pages [13] -->
N p r e p a r e =

<!-- b000382 | prose | pages [13] -->
6 0 0

<!-- b000383 | prose | pages [13] -->
N p r e p a r e = N p r e p a r e =

<!-- b000384 | prose | pages [13] -->
5 0 0

<!-- b000385 | prose | pages [13] -->
N p r e p a r e = N p r e p a r e =

<!-- b000386 | prose | pages [13] -->
4 0 0

<!-- b000387 | prose | pages [13] -->
N o P r e p a r

<!-- b000388 | prose | pages [13] -->
3 0 0

<!-- b000389 | prose | pages [13] -->
a v g ( s

<!-- b000390 | prose | pages [13] -->
2 0 0

<!-- b000391 | prose | pages [13] -->
1 0 0

<!-- b000392 | prose | pages [13] -->
t a ( s

<!-- b000393 | caption | pages [13] -->
Figure 8: The Total Time Curves of Different

<!-- b000394 | prose | pages [13] -->
Nprepare

<!-- b000395 | prose | pages [13] -->
Percentage of Time Spent on Each Process

<!-- b000396 | prose | pages [13] -->
Waiting at ID Checkpoints 0.11% ID Check 0.30% Waiting for Screening 98.11% Preparing for Screening 0.66%

<!-- b000397 | prose | pages [13] -->
Screening 0.75% Additional Screening 0.07%

<!-- b000398 | prose | pages [13] -->
Highcharts.com

<!-- b000399 | caption | pages [13] -->
Figure 10: The Percentage of Time in Differ-

<!-- b000400 | prose | pages [13] -->
ent Process before MPL modiﬁcation

<!-- b000401 | prose | pages [13] -->
4.2

<!-- b000402 | heading | pages [13] -->
Priority-based Queuing Model

<!-- b000403 | prose | pages [13] -->
4.2.1

<!-- b000404 | heading | pages [13] -->
The Design of PBQ Model

<!-- b000405 | furniture | pages [13] -->
Page 12 of 32

<!-- b000406 | prose | pages [13] -->
4 0 0

<!-- b000407 | prose | pages [13] -->
N p r e p a r e = N p r e p a r e =

<!-- b000408 | prose | pages [13] -->
3 5 0

<!-- b000409 | prose | pages [13] -->
N p r e p a r e =

<!-- b000410 | prose | pages [13] -->
3 0 0

<!-- b000411 | prose | pages [13] -->
N p r e p a r e = N p r e p a r e =

<!-- b000412 | prose | pages [13] -->
2 5 0

<!-- b000413 | prose | pages [13] -->
N o P r e p a r

<!-- b000414 | prose | pages [13] -->
2 0 0

<!-- b000415 | prose | pages [13] -->
σΤ ( s

<!-- b000416 | prose | pages [13] -->
1 5 0

<!-- b000417 | prose | pages [13] -->
1 0 0

<!-- b000418 | prose | pages [13] -->
5 0

<!-- b000419 | prose | pages [13] -->
t a ( s

<!-- b000420 | caption | pages [13] -->
Figure 9: The Standard Deviation Curve of

<!-- b000421 | prose | pages [13] -->
Different Nprepare

<!-- b000422 | prose | pages [13] -->
Percentage of Time Spent on Each Process

<!-- b000423 | prose | pages [13] -->
Waiting at ID Checkpoints 3.00% ID Check 6.31% Waiting for Screening 57.21% Preparing For Screening 18.05%

<!-- b000424 | prose | pages [13] -->
Screening 13.47% Additional Screening 1.96%

<!-- b000425 | prose | pages [13] -->
Highcharts.com

<!-- b000426 | caption | pages [13] -->
Figure 11: The Percentage of Time in Differ-

<!-- b000427 | prose | pages [13] -->
ent Process after MPL modiﬁcation

<!-- b000428 | prose | pages [13] -->
In this model, we divide the four lanes of security check into the following kinds: one Pre-Check lane, two regular lanes and one emergency lane. In the attributes generation process, we add a new property into the attributes, tad, the time between the arrivals of the passengers to the departure of the airplane. Based on this attribute, we divide the passengers into three priorities. We set two time intevals tad1 and tad2. Passengers whose tad is under tad1 are of the ﬁrst priority, whose one is between [tad1, tad1 + tad2] are of the second priority and the rest are of the third priority. The relevant groups of people are called the priority group, the regular group and the over-punctual group.

<!-- b000429 | prose | pages [13] -->
For different priorities, passengers enjoy different policies. For the priority group, passengers can use the emergency lane immediately. For the regular group, passengers cannot go pass the emergency lane until they have been waiting at the airport for a period of tad1. When a period of tad2 has passed, the passengers of the over-punctual group can make use of the emergency lane. This policy can not only guarantee that the one in an urgent can get aboard in the ﬁrst time, but also warn people not to arrive unnecessarily early. Figure 12 discribes this new modiﬁcation.

<!-- b000430 | furniture | pages [14] -->
Team # 55285

<!-- b000431 | furniture | pages [14] -->
Page 13 of 32

<!-- b000432 | prose | pages [14] -->
Emergency

<!-- b000433 | prose | pages [14] -->
At the time nodes, some of regular and pre-check people will

<!-- b000434 | prose | pages [14] -->
have priority attributes and can pass ID check through the

<!-- b000435 | prose | pages [14] -->
Regular

<!-- b000436 | prose | pages [14] -->
emergency lane.

<!-- b000437 | prose | pages [14] -->
Redistribute

<!-- b000438 | prose | pages [14] -->
Emergency

<!-- b000439 | prose | pages [14] -->
Emergency

<!-- b000440 | prose | pages [14] -->
Regular

<!-- b000441 | prose | pages [14] -->
Regular

<!-- b000442 | prose | pages [14] -->
Regular

<!-- b000443 | prose | pages [14] -->
Regular

<!-- b000444 | prose | pages [14] -->
Pre-check

<!-- b000445 | prose | pages [14] -->
Pre-check

<!-- b000446 | prose | pages [14] -->
The First Time Node

<!-- b000447 | prose | pages [14] -->
Pre-check

<!-- b000448 | prose | pages [14] -->
Redistribute

<!-- b000449 | prose | pages [14] -->
Emergency

<!-- b000450 | prose | pages [14] -->
Emergency

<!-- b000451 | prose | pages [14] -->
Emergency

<!-- b000452 | prose | pages [14] -->
Regular

<!-- b000453 | prose | pages [14] -->
Regular

<!-- b000454 | prose | pages [14] -->
Regular

<!-- b000455 | prose | pages [14] -->
Reg ular

<!-- b000456 | prose | pages [14] -->
Regular

<!-- b000457 | prose | pages [14] -->
Regular

<!-- b000458 | prose | pages [14] -->
Regular

<!-- b000459 | prose | pages [14] -->
Pre-check

<!-- b000460 | prose | pages [14] -->
Pre-check

<!-- b000461 | prose | pages [14] -->
Pre-check

<!-- b000462 | prose | pages [14] -->
The Second Time Node Time Process

<!-- b000463 | caption | pages [14] -->
Figure 12: The PBQ Model

<!-- b000464 | prose | pages [14] -->
4.2.2

<!-- b000465 | heading | pages [14] -->
The Effectiveness of PBQ Model

<!-- b000466 | prose | pages [14] -->
We investigate the average time consumed in the whole process of different groups under PBQ modiﬁcation. We change ta, the arrival time interval between two passengers and observe the trend of the curves. Then we compare it with that without PBQ modi- ﬁcation. According to Figure 13 and Figure 23, at the peak ﬂow of passengers (ta < 1s), Tavg and its standard deviation of the ﬁrst group are signiﬁcantly

<!-- b000467 | prose | pages [14] -->
1 4

<!-- b000468 | prose | pages [14] -->
B e f o r e P B Q M o d i f i c a t i o A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s

<!-- b000469 | prose | pages [14] -->
1 2

<!-- b000470 | prose | pages [14] -->
A f t e r P B Q M o d i f i c a t i o n ( B o t h P r i o r a n d R e g u l a r P a s s e n g e r s A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s

<!-- b000471 | prose | pages [14] -->
1 0

<!-- b000472 | prose | pages [14] -->
A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r

<!-- b000473 | prose | pages [14] -->
8

<!-- b000474 | prose | pages [14] -->
i n

<!-- b000475 | prose | pages [14] -->
6

<!-- b000476 | prose | pages [14] -->
a v g (

<!-- b000477 | prose | pages [14] -->
4

<!-- b000478 | prose | pages [14] -->
2

<!-- b000479 | prose | pages [14] -->
t a ( s

<!-- b000480 | caption | pages [14] -->
Figure 13: The Total Time curves under PBQ

<!-- b000481 | prose | pages [14] -->
Model of Different Groups

<!-- b000482 | prose | pages [14] -->
9

<!-- b000483 | prose | pages [14] -->
B e f o r e P B Q M o d i f i c a t i o

<!-- b000484 | prose | pages [14] -->
8

<!-- b000485 | prose | pages [14] -->
A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s A f t e r P B Q M o d i f i c a t i o n ( B o t h P r i o r a n d R e g u l a r P a s s e n g e r s

<!-- b000486 | prose | pages [14] -->
7

<!-- b000487 | prose | pages [14] -->
A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r

<!-- b000488 | prose | pages [14] -->
6

<!-- b000489 | prose | pages [14] -->
5

<!-- b000490 | prose | pages [14] -->
4

<!-- b000491 | prose | pages [14] -->
i n

<!-- b000492 | prose | pages [14] -->
3

<!-- b000493 | prose | pages [14] -->
σΤ (

<!-- b000494 | prose | pages [14] -->
2

<!-- b000495 | prose | pages [14] -->
1

<!-- b000496 | prose | pages [14] -->
- 1

<!-- b000497 | prose | pages [14] -->
t a ( s

<!-- b000498 | caption | pages [14] -->
Figure 14: The Total Time curves under PBQ

<!-- b000499 | prose | pages [14] -->
Model of Different Groups

<!-- b000500 | prose | pages [14] -->
We programme to implement this modiﬁcation and draw the ﬁgure of Tavg as a func- tion of tad1 and tad2 to ﬁnd out the optimal parameters tad1 and tad2.

<!-- b000501 | prose | pages [14] -->
According to Figure 15 and Figure 16, we can conclude that PBQ model has the fol- lowing properties.

<!-- b000502 | prose | pages [14] -->
As is shown in Figure 15, the average time of the three groups does not change much as the parameters change. That is to say, when tad1 and tad2 are set unsuitably, which

<!-- b000503 | furniture | pages [15] -->
Team # 55285

<!-- b000504 | furniture | pages [15] -->
Page 14 of 32

<!-- b000505 | prose | pages [15] -->
Average Waiting Time of Different Advance Time

<!-- b000506 | prose | pages [15] -->
[min] ad2

<!-- b000507 | prose | pages [15] -->
70

<!-- b000508 | prose | pages [15] -->
t

<!-- b000509 | prose | pages [15] -->
60

<!-- b000510 | prose | pages [15] -->
50

<!-- b000511 | prose | pages [15] -->
40

<!-- b000512 | prose | pages [15] -->
30

<!-- b000513 | prose | pages [15] -->
20

<!-- b000514 | prose | pages [15] -->
35 40 45

<!-- b000515 | prose | pages [15] -->
[min]

<!-- b000516 | prose | pages [15] -->
27

<!-- b000517 | prose | pages [15] -->
avg T

<!-- b000518 | prose | pages [15] -->
26

<!-- b000519 | prose | pages [15] -->
25

<!-- b000520 | prose | pages [15] -->
24

<!-- b000521 | prose | pages [15] -->
23

<!-- b000522 | prose | pages [15] -->
22

<!-- b000523 | prose | pages [15] -->
21

<!-- b000524 | prose | pages [15] -->
20

<!-- b000525 | prose | pages [15] -->
19

<!-- b000526 | prose | pages [15] -->
18

<!-- b000527 | prose | pages [15] -->
50 55 60 t [min] ad1

<!-- b000528 | caption | pages [15] -->
Figure 15: The ﬁgure of Tavg of the ﬁrst two groups

<!-- b000529 | prose | pages [15] -->
Average Waiting Time of Different Advance Time

<!-- b000530 | prose | pages [15] -->
[min]

<!-- b000531 | prose | pages [15] -->
37.2 37

<!-- b000532 | prose | pages [15] -->
avg

<!-- b000533 | prose | pages [15] -->
36.8

<!-- b000534 | prose | pages [15] -->
T

<!-- b000535 | prose | pages [15] -->
36.6 36.4 36.2 36 35.8 35.6 35.4 35.2 35

<!-- b000536 | prose | pages [15] -->
70

<!-- b000537 | prose | pages [15] -->
t [min] ad2

<!-- b000538 | prose | pages [15] -->
60 50 40 30 20

<!-- b000539 | prose | pages [15] -->
35 60 55

<!-- b000540 | prose | pages [15] -->
[min]

<!-- b000541 | prose | pages [15] -->
50

<!-- b000542 | prose | pages [15] -->
t

<!-- b000543 | prose | pages [15] -->
45

<!-- b000544 | prose | pages [15] -->
ad1

<!-- b000545 | prose | pages [15] -->
40

<!-- b000546 | caption | pages [15] -->
Figure 16: The ﬁgure of Tavg of the three groups

<!-- b000547 | prose | pages [15] -->
do not match the relevant ﬂow volumn of passengers, it does not have negative effects. But, if we set suitable parameters, the screening speed of the ﬁrst two groups can be accelerated. In other words, the rate of fault tolerance is strong.

<!-- b000548 | prose | pages [15] -->
It is obvious that in Figure 16, if the sum of tad1 and tad2 is a constant, the average time of the ﬁrst two groups, the priority group and the regular group do not change much. When the sum gets smaller, the average time gets smaller as well. This is because with the decrease of the tad1 and tad2, the number of passengers decreases as well, which means the number of passengers who can make use of the emergency lane is reduced.

<!-- b000549 | prose | pages [15] -->
Therefore, we can set the ratio of tad1 and tad2 according to the ratio of the passengers numbers of the two groups. This means that we can improve the utilization rate of the current resources. Besides, this phenomenon also shows that the model accords to the reality.

<!-- b000550 | prose | pages [15] -->
4.3

<!-- b000551 | heading | pages [15] -->
Model of Special Population

<!-- b000552 | prose | pages [15] -->
4.3.1

<!-- b000553 | heading | pages [15] -->
The Design of SP Model

<!-- b000554 | prose | pages [15] -->
In actual situation, the elderly and children are less likely to bring dangerous objects, and they usually do not bring luggage with them as well. According to the website of TSA[6], they have implemented a policy to reduce the time of security inspection of the

<!-- b000555 | furniture | pages [16] -->
Team # 55285

<!-- b000556 | furniture | pages [16] -->
Page 15 of 32

<!-- b000557 | prose | pages [16] -->
elderly over 75 and the children under 12. They claim that those people will no longer removing shoes and light outerwear.

<!-- b000558 | prose | pages [16] -->
We build the model of special population to simulate this situation. We assume that neither the elderly nor the children will bring luggage with them. In this situation, ac- cording to Equation (3), the time of screening equals to the time of body scanning.

<!-- b000559 | prose | pages [16] -->
We set the percentage as 0, 10%, 20%, 30%, respectively. In each condition, we study how Tavg , the average total time changes as a function of ta, the time interval between two passengers’ arrivals.

<!-- b000560 | prose | pages [16] -->
4.3.2

<!-- b000561 | heading | pages [16] -->
The Effectiveness of SP Model

<!-- b000562 | prose | pages [16] -->
As is shown in Figure 17 and Figure 18, the four curves of 0, 10%, 20%, 30% are similar. The change in Tavg brought by this institution is subtle. That is to say, TSA’s new policy on the ofﬁcial website is not as effective.

<!-- b000563 | prose | pages [16] -->
5 0 0

<!-- b000564 | prose | pages [16] -->
R o y p = 0 R o y p = 1 0

<!-- b000565 | prose | pages [16] -->
4 0 0

<!-- b000566 | prose | pages [16] -->
R o y p = 2 0 R o y p = 3 0

<!-- b000567 | prose | pages [16] -->
3 0 0

<!-- b000568 | prose | pages [16] -->
a v g ( s

<!-- b000569 | prose | pages [16] -->
2 0 0

<!-- b000570 | prose | pages [16] -->
1 0 0

<!-- b000571 | prose | pages [16] -->
t a ( s

<!-- b000572 | caption | pages [16] -->
Figure 17: The Total Time Curves of Differ-

<!-- b000573 | prose | pages [16] -->
ent Royp

<!-- b000574 | prose | pages [16] -->
3 0 0

<!-- b000575 | prose | pages [16] -->
R o y p = 0 R o y p = 1 0

<!-- b000576 | prose | pages [16] -->
2 5 0

<!-- b000577 | prose | pages [16] -->
R o y p = 2 0 R o y p = 3 0

<!-- b000578 | prose | pages [16] -->
2 0 0

<!-- b000579 | prose | pages [16] -->
1 5 0

<!-- b000580 | prose | pages [16] -->
σΤ ( s

<!-- b000581 | prose | pages [16] -->
1 0 0

<!-- b000582 | prose | pages [16] -->
5 0

<!-- b000583 | prose | pages [16] -->
t a ( s

<!-- b000584 | caption | pages [16] -->
Figure 18: The Standard Deviation Curve of

<!-- b000585 | prose | pages [16] -->
Different Royp

<!-- b000586 | heading | pages [16] -->
Model Evaluation & Sensitivity Analysis

<!-- b000587 | prose | pages [16] -->
5

<!-- b000588 | prose | pages [16] -->
We operate the model in the condition of Chinese airport to test its sensitivity. We build a cut-in-line model to describe the situation of China. Then we test the sensitivity of modiﬁcation models in Chinese airports.

<!-- b000589 | prose | pages [16] -->
5.1

<!-- b000590 | heading | pages [16] -->
The Cut-in-line Model

<!-- b000591 | prose | pages [16] -->
In this model, we consider some special factors under China’s reality, including:

<!-- b000592 | prose | pages [16] -->
• In China, the threat of terrorism is not as severe, hence the rules in Chinese airports are not strict as those in America. The passengers do not need to take off their clothes and shoes.

<!-- b000593 | prose | pages [16] -->
• The passengers will attach much importance to personal efﬁciency and there exists the phenomenon of cutting in lines.

<!-- b000594 | furniture | pages [17] -->
Team # 55285

<!-- b000595 | furniture | pages [17] -->
Page 16 of 32

<!-- b000596 | prose | pages [17] -->
Therefore, we make the relevant alternations to our model:

<!-- b000597 | prose | pages [17] -->
• The preparing time of all Chinese people is the same as Pre-Check passengers in the American model.

<!-- b000598 | prose | pages [17] -->
• When a passenger is generated, we give two additional attributes to him or her.

<!-- b000599 | prose | pages [17] -->
One is whether the passenger will cut in lines or not. The other is the position the passenger cut in. We assume that the probability of jumping into each position in front of the passenger is the same. This process is shown in Figure 19.

<!-- b000600 | prose | pages [17] -->
Regular

<!-- b000601 | prose | pages [17] -->
Regular

<!-- b000602 | prose | pages [17] -->
Regular

<!-- b000603 | prose | pages [17] -->
Regular

<!-- b000604 | caption | pages [17] -->
Figure 19: The Process of Cutting Lines

<!-- b000605 | prose | pages [17] -->
5.2

<!-- b000606 | heading | pages [17] -->
The Sensitivity of MPL Model

<!-- b000607 | prose | pages [17] -->
We investigate the sensitivity of MPL Model in Chinese situation. Under the different rate of cutting in lines, we observe the difference brought by the model. According to

<!-- b000608 | caption | pages [17] -->
Figure 20 and Figure 21, the total time and its variance can still be signiﬁcantly reduced.

<!-- b000609 | prose | pages [17] -->
5 A v e r a g e T i m e w i t h o u t M P L M o d e

<!-- b000610 | prose | pages [17] -->
2 0

<!-- b000611 | prose | pages [17] -->
1 0 A v e r a g e T i m e w i t h o u t M P L M o d e 1 5 A v e r a g e T i m e w i t h o u t M P L M o d e 5 A v e r a g e T i m e w i t h M P L M o d e

<!-- b000612 | prose | pages [17] -->
1 5

<!-- b000613 | prose | pages [17] -->
1 0 A v e r a g e T i m e w i t h M P L M o d e 1 5 A v e r a g e T i m e w i t h M P L M o d e

<!-- b000614 | prose | pages [17] -->
i n

<!-- b000615 | prose | pages [17] -->
1 0

<!-- b000616 | prose | pages [17] -->
a v g (

<!-- b000617 | prose | pages [17] -->
5

<!-- b000618 | prose | pages [17] -->
t a ( s

<!-- b000619 | caption | pages [17] -->
Figure 20: The Total Time Curves under M-

<!-- b000620 | prose | pages [17] -->
PL Model in Chinese Situation

<!-- b000621 | prose | pages [17] -->
5 V a r i a n c e w i t h o u t M P L M o d e

<!-- b000622 | prose | pages [17] -->
1 2

<!-- b000623 | prose | pages [17] -->
1 0 V a r i a n c e w i t h o u t M P L M o d e 1 5 V a r i a n c e w i t h o u t M P L M o d e

<!-- b000624 | prose | pages [17] -->
1 0

<!-- b000625 | prose | pages [17] -->
5 V a r i a n c e w i t h M P L M o d e 1 0 V a r i a n c e w i t h M P L M o d e

<!-- b000626 | prose | pages [17] -->
8

<!-- b000627 | prose | pages [17] -->
1 5 V a r i a n c e w i t h M P L M o d e

<!-- b000628 | prose | pages [17] -->
6

<!-- b000629 | prose | pages [17] -->
i n σT (

<!-- b000630 | prose | pages [17] -->
4

<!-- b000631 | prose | pages [17] -->
2

<!-- b000632 | prose | pages [17] -->
t a ( s

<!-- b000633 | caption | pages [17] -->
Figure 21: The Standard Deviation Curves

<!-- b000634 | prose | pages [17] -->
under MPL Model in Chinese Situation

<!-- b000635 | furniture | pages [18] -->
Team # 55285

<!-- b000636 | prose | pages [18] -->
5.3

<!-- b000637 | heading | pages [18] -->
The Sensitivity of PBQ Model

<!-- b000638 | furniture | pages [18] -->
Page 17 of 32

<!-- b000639 | prose | pages [18] -->
We test the sensitivity of PBQ Model in Chinese situation. Under the different rate of cutting in lines, we observe the difference brought by the model. According to Figure 22 and Figure 23, the average time of the priority group and its variance can be signiﬁcantly reduced, while the average time of all the passengers keeps the same as that without the model. This is the same as that in America. From Figure 24, we can view that after the modiﬁcation of PBQ model, the rate of cutting in lines does not make sense to the average consumed time.

<!-- b000640 | prose | pages [18] -->
1 4

<!-- b000641 | prose | pages [18] -->
5 A v e r a g e T i m e B e f o r e P B Q M o d i f i c a t i o 1 5 A v e r a g e T i m e B e f o r e P B Q M o d i f i c a t i o

<!-- b000642 | prose | pages [18] -->
1 2

<!-- b000643 | prose | pages [18] -->
5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s 1 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s

<!-- b000644 | prose | pages [18] -->
1 0

<!-- b000645 | prose | pages [18] -->
1 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r s 1 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r s

<!-- b000646 | prose | pages [18] -->
8

<!-- b000647 | prose | pages [18] -->
5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( P r o i r a n d R e g u l a r P a s s e n g e r s 1 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( P r o i r a n d R e g u l a r P a s s e n g e r s

<!-- b000648 | prose | pages [18] -->
i n

<!-- b000649 | prose | pages [18] -->
6

<!-- b000650 | prose | pages [18] -->
a v g (

<!-- b000651 | prose | pages [18] -->
4

<!-- b000652 | prose | pages [18] -->
2

<!-- b000653 | prose | pages [18] -->
t a ( s

<!-- b000654 | caption | pages [18] -->
Figure 22: The Total Time Curves under P-

<!-- b000655 | prose | pages [18] -->
BQ Model in Chinese Situation

<!-- b000656 | prose | pages [18] -->
9

<!-- b000657 | prose | pages [18] -->
5 V a r i a n c e B e f o r e P B Q M o d i f i c a t i o 1 5 V a r i a n c e B e f o r e P B Q M o d i f i c a t i o

<!-- b000658 | prose | pages [18] -->
8

<!-- b000659 | prose | pages [18] -->
5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s 1 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s

<!-- b000660 | prose | pages [18] -->
7

<!-- b000661 | prose | pages [18] -->
5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s 1 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s

<!-- b000662 | prose | pages [18] -->
6

<!-- b000663 | prose | pages [18] -->
5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r s 1 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r s

<!-- b000664 | prose | pages [18] -->
5

<!-- b000665 | prose | pages [18] -->
5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( P r o i r a n d R e g u l a r P a s s e n g e r s 1 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( P r o i r a n d R e g u l a r P a s s e n g e r s

<!-- b000666 | prose | pages [18] -->
4

<!-- b000667 | prose | pages [18] -->
i n

<!-- b000668 | prose | pages [18] -->
3

<!-- b000669 | prose | pages [18] -->
σT (

<!-- b000670 | prose | pages [18] -->
2

<!-- b000671 | prose | pages [18] -->
1

<!-- b000672 | prose | pages [18] -->
- 1

<!-- b000673 | prose | pages [18] -->
a ( s

<!-- b000674 | caption | pages [18] -->
Figure 23: The Standard Deviation Curves

<!-- b000675 | prose | pages [18] -->
under PBQ Model in Chinese Situation

<!-- b000676 | prose | pages [18] -->
Prior and Regular Passengers' Average Waiting Time of Different R

<!-- b000677 | prose | pages [18] -->
1.4

<!-- b000678 | prose | pages [18] -->
[second]

<!-- b000679 | prose | pages [18] -->
1.3

<!-- b000680 | prose | pages [18] -->
at

<!-- b000681 | prose | pages [18] -->
1.2

<!-- b000682 | prose | pages [18] -->
1.1

<!-- b000683 | prose | pages [18] -->
1

<!-- b000684 | prose | pages [18] -->
0.9

<!-- b000685 | prose | pages [18] -->
0.8

<!-- b000686 | prose | pages [18] -->
0.7

<!-- b000687 | prose | pages [18] -->
0.6

<!-- b000688 | prose | pages [18] -->
0.5

<!-- b000689 | prose | pages [18] -->
0 0.05 0.1

<!-- b000690 | prose | pages [18] -->
After PBQ Modification cut

<!-- b000691 | prose | pages [18] -->
[min]

<!-- b000692 | prose | pages [18] -->
80

<!-- b000693 | prose | pages [18] -->
avg12

<!-- b000694 | prose | pages [18] -->
70

<!-- b000695 | prose | pages [18] -->
T

<!-- b000696 | prose | pages [18] -->
60

<!-- b000697 | prose | pages [18] -->
50

<!-- b000698 | prose | pages [18] -->
40

<!-- b000699 | prose | pages [18] -->
30

<!-- b000700 | prose | pages [18] -->
20

<!-- b000701 | prose | pages [18] -->
10

<!-- b000702 | prose | pages [18] -->
0

<!-- b000703 | prose | pages [18] -->
0.15 0.2 0.25 R cut

<!-- b000704 | caption | pages [18] -->
Figure 24: Prior and Regular Passengers’ Average Waiting Time of Different Rcut After

<!-- b000705 | prose | pages [18] -->
PBQ Modiﬁcation

<!-- b000706 | prose | pages [18] -->
To conclude, both MPL model and PBQ are as effective in China as that in America. That is to say, our model can also be applied to Chinese airports with a few modiﬁcations.

<!-- b000707 | furniture | pages [19] -->
Team # 55285

<!-- b000708 | furniture | pages [19] -->
Page 18 of 32

<!-- b000709 | prose | pages [19] -->
6

<!-- b000710 | heading | pages [19] -->
Conclusion

<!-- b000711 | prose | pages [19] -->
6.1

<!-- b000712 | heading | pages [19] -->
Strengths and Weaknesses

<!-- b000713 | prose | pages [19] -->
6.1.1

<!-- b000714 | heading | pages [19] -->
Strengths

<!-- b000715 | prose | pages [19] -->
Our models are adaptable to different conditions. Both MPL and PBQ models can still provide stable efﬁciency improvement though there may be some impacts.

<!-- b000716 | prose | pages [19] -->
PBQ model has strong fault tolerance. Though we may not get the exact optimal time interval tad1 and tad2, the modiﬁcation is still able to reduce a lot of time, especially when we meet the extreme peak ﬂow.

<!-- b000717 | prose | pages [19] -->
Our models have broad application prospect. PBQ model can not only reduce the urgent people’s waiting time, but also encourages people not to arrive at airport too early. This can decline the pressure during peak ﬂow.

<!-- b000718 | prose | pages [19] -->
6.1.2

<!-- b000719 | heading | pages [19] -->
Weaknesses

<!-- b000720 | prose | pages [19] -->
Our models ignore the probability of emergent incident, thus our models only work in a peaceful environment.

<!-- b000721 | prose | pages [19] -->
In the SP model, we just consider the old and the young as another ‘PreCheck’ pas- senger, this may be improper.

<!-- b000722 | prose | pages [19] -->
In the Cut-in-line model, we assume that the occurrence probability of the cutting in line is constant, this may be a little different from reality.

<!-- b000723 | prose | pages [19] -->
6.2 Suggestions to the Security Manager

<!-- b000724 | prose | pages [19] -->
According to our simulation result, we have the following recommendations for the security managers.

<!-- b000725 | prose | pages [19] -->
• Pre-Check policy is indeed effective in accelerating the process, and the ratio of Pre- Check lanes and regular lanes is optimal. Therefore we should keep the suitable ratio and advertise the advantages of Pre-Check policy.

<!-- b000726 | prose | pages [19] -->
• The airports can add a small zone between the screening machine and the waiting lanes, which can allow 3 passengers to prepare for screening in advance at the same time.

<!-- b000727 | prose | pages [19] -->
• The airports can set up some time limit intervals for security check as PBQ model, to reduce the waiting time of the passengers who is going to takeoff. This policy can also encourage passengers not to arrive too early, so that congestion during fastigia can be alleviated. What’s more, the length of the time intervals tad1 and tad2 and the number of passengers in the priority group ﬂow are directly related.

<!-- b000728 | prose | pages [19] -->
• It is not necessary for TSA to consider adjusting policy to the old and the young too much, because this modiﬁcation will not provide passengers with much help.

<!-- b000729 | furniture | pages [20] -->
Team # 55285

<!-- b000730 | furniture | pages [20] -->
Page 19 of 32

<!-- b000731 | prose | pages [20] -->
• For Chinese airports, cutting in lines will not inﬂuence the effectiveness of the two models, therefore we can also apply these two models to Chinese airports.

<!-- b000732 | prose | pages [20] -->
6.3 Future Plans

<!-- b000733 | prose | pages [20] -->
Our present PBQ model has ﬁxed total peak passenger ﬂow, in the future, we try to use the passenger generating time to decide the duration of peak period, MPL can study the linkage condition and time node at a ﬁxed peak time, make more objective evaluations on its performance.

<!-- b000734 | prose | pages [20] -->
Make the occurrence probability of the cutting in line be related to the congestion level, in the real condition, more crowded the airport is, more cut-in-line phenomenon will take place.

<!-- b000735 | heading | pages [20] -->
References

<!-- b000736 | references | pages [20] -->
[1] T. Meisling, “Discrete-time queuing theory,” Operations Research, vol. 6, no. 1, pp.

<!-- b000737 | references | pages [20] -->
96–105, 1958.

<!-- b000738 | references | pages [20] -->
[2] G. Yang, Z. Min, Z. Hang, and L. Yue, “Research on dynamic allocations of airport

<!-- b000739 | references | pages [20] -->
security check resources,” Aeronautical Computing Technology, vol. 46, no. 5, 2016.

<!-- b000740 | references | pages [20] -->
[3] R. de Lange, I. Samoilovich, and B. van der Rhee, “Virtual queuing at airport security

<!-- b000741 | references | pages [20] -->
lanes,” European Journal of Operational Research, vol. 225, no. 1, pp. 153 – 165, 2013.

<!-- b000742 | references | pages [20] -->
[4] M. Bevilacqua and F. E. Ciarapica, “Analysis of check-in procedure using simula-

<!-- b000743 | references | pages [20] -->
tion: A case study,” in 2010 IEEE International Conference on Industrial Engineering and

<!-- b000744 | references | pages [20] -->
Engineering Management, Dec 2010, pp. 1621–1625.

<!-- b000745 | references | pages [20] -->
[5] X. He, Stochastic process and queuing theory.

<!-- b000746 | references | pages [20] -->
Hunan University Press, 2010.

<!-- b000747 | references | pages [20] -->
[6] http://www.portofportland.com/Notices/PDX_TSA_75over_Scrng_01_BLT.htm.

<!-- b000748 | furniture | pages [21] -->
Team # 55285

<!-- b000749 | furniture | pages [21] -->
Page 20 of 32

<!-- b000750 | heading | pages [21] -->
Appendices

<!-- b000751 | heading | pages [21] -->
Appendix A

<!-- b000752 | prose | pages [21] -->
Simulation Code

<!-- b000753 | prose | pages [21] -->
Our simulation codes written in C++:

<!-- b000754 | prose | pages [21] -->
#include<cstdio> #include<cmath> #include<iostream> #include<fstream>

<!-- b000755 | prose | pages [21] -->
using namespace std;

<!-- b000756 | prose | pages [21] -->
const int Files = 4;

<!-- b000757 | prose | pages [21] -->
string filename[Files] = {"A", "B", "E", "F"};

<!-- b000758 | prose | pages [21] -->
double stringToSecond(string &str) {

<!-- b000759 | prose | pages [21] -->
int now = 0; double min = 0, sec = 0; while (str[now] != ’:’) {

<!-- b000760 | prose | pages [21] -->
min = min * 10 + str[now++] - 48; } now++; while (str[now] != ’.’) {

<!-- b000761 | prose | pages [21] -->
sec = sec * 10 + str[now++] - 48; } return min * 60 + sec; }

<!-- b000762 | prose | pages [21] -->
void work(ifstream &inFile, ofstream &outFile) {

<!-- b000763 | prose | pages [21] -->
double second[100], difference[100]; int n = 0; string str; while (inFile >> str) {

<!-- b000764 | prose | pages [21] -->
second[n++] = stringToSecond(str); outFile << second[n - 1] << endl; } double sum = 0; for (int i = 1; i < n; ++i) {

<!-- b000765 | prose | pages [21] -->
difference[i] = second[i] - second[i - 1]; sum += difference[i]; } double ave = sum / (n - 1); sum = 0; for (int i = 1; i < n; ++i) {

<!-- b000766 | prose | pages [21] -->
sum += (difference[i] - ave) * (difference[i] - ave); } double vari = sum / (n - 2); outFile << "average: " << ave << endl; outFile << "variance: " << vari << endl; outFile << "standard deviation: " << sqrt(vari) << endl; }

<!-- b000767 | prose | pages [21] -->
int main() {

<!-- b000768 | prose | pages [21] -->
ifstream inFile; ofstream outFile; for (int i = 0; i < Files; ++i) {

<!-- b000769 | furniture | pages [22] -->
Team # 55285

<!-- b000770 | furniture | pages [22] -->
Page 21 of 32

<!-- b000771 | prose | pages [22] -->
inFile.open(filename[i] + ".txt"); outFile.open(filename[i] + "_out.txt"); work(inFile, outFile); inFile.close(); outFile.close(); } return 0; }

<!-- b000772 | prose | pages [22] -->
#include<cstdio> #include<cmath> #include<ctime> #include<cstdlib> #include<iostream> #include<queue> #include<fstream>

<!-- b000773 | heading | pages [22] -->
#include<algorithm>

<!-- b000774 | prose | pages [22] -->
using namespace std;

<!-- b000775 | prose | pages [22] -->
double gaussrand(double E, double V) {

<!-- b000776 | prose | pages [22] -->
static double V1, V2, S; static int phase = 0; double X; if (phase == 0) {

<!-- b000777 | prose | pages [22] -->
do {

<!-- b000778 | prose | pages [22] -->
double U1 = (double)rand() / RAND_MAX; double U2 = (double)rand() / RAND_MAX; V1 = 2 * U1 - 1; V2 = 2 * U2 - 1; S = V1 * V1 + V2 * V2; } while (S >= 1 || S == 0); X = V1 * sqrt(-2 * log(S) / S); } else X = V2 * sqrt(-2 * log(S) / S); phase = 1 - phase; return X * V + E; }

<!-- b000779 | prose | pages [22] -->
double U_Random() {

<!-- b000780 | prose | pages [22] -->
double f; f = (float)(rand() % 100); return f/100; }

<!-- b000781 | prose | pages [22] -->
double possion(double Lambda) {

<!-- b000782 | prose | pages [22] -->
double k = 0; long double p = 1.0; long double l = exp(-Lambda); while (p >= l) {

<!-- b000783 | prose | pages [22] -->
double u = U_Random(); p *= u; k += 1; } return k-1; }

<!-- b000784 | prose | pages [22] -->
const double AgeSeed = 0.0; const double VIPErrorRatio = 0.01; const double PaxErrorRatio = 0.03;

<!-- b000785 | furniture | pages [23] -->
Team # 55285

<!-- b000786 | furniture | pages [23] -->
Page 22 of 32

<!-- b000787 | prose | pages [23] -->
const double VIPArrivalSeed = 4; const double PaxArrivalSeed = 6; const int VIPIDCheck = 1; const int PaxIDCheck = 3; const double IDCheckSeed_E = 11.3125; const double IDCheckSeed_S = 3.70079; const double VIPRemoveThingsSeed_E = 15.0; const double VIPRemoveThingsSeed_S = 5.0; const double PaxRemoveThingsSeed_E = 40.0; const double PaxRemoveThingsSeed_S = 10.0; const int VIPLanes = 1; const int PaxLanes = 3; const double BaggagePrepareSeed = 5.0; const double BaggageCheckSeed_1 = 11.0; const double BaggageCheckSeed_2 = 2.0; const double BodyCheckSeed_E = 11.6; const double BodyCheckSeed_S = 5.8; const double ZoneDTime_E = 120.0; const double ZoneDTime_S = 20.0; const double RatioBinOne = 0.2; const double RatioCinOne = 0.1; const double RatioCinTwo = 0.2;

<!-- b000788 | prose | pages [23] -->
double FastigiumTime = VIPArrivalSeed * 2160; double FirstPoint, SecondPoint; int ContainMost = 3; const int Times = 5; const int AllNumber = 10000; int Number = 0, VIPNumber = 0, PaxNumber = 0; int NumberKind_1 = 0, NumberKind_2 = 0;

<!-- b000789 | prose | pages [23] -->
bool isSrand = false;

<!-- b000790 | prose | pages [23] -->
int baggageRand() {

<!-- b000791 | prose | pages [23] -->
return rand() % 4; }

<!-- b000792 | prose | pages [23] -->
struct HumanBeings {

<!-- b000793 | prose | pages [23] -->
int waitKind; bool isVIP; bool isError; double zoneDTime; double arrivalTime; double IDCheckTime; double removeThingsTime; double baggageCheckTime; double bodyCheckTime; double departTime; int baggageNumber; HumanBeings() {

<!-- b000794 | prose | pages [23] -->
if (!isSrand) {

<!-- b000795 | prose | pages [23] -->
srand((unsigned)time(NULL)); isSrand = true; } IDCheckTime = gaussrand(IDCheckSeed_E, IDCheckSeed_S); baggageNumber = baggageRand(); baggageCheckTime = BaggageCheckSeed_1 + BaggageCheckSeed_2 * baggageNumber; bodyCheckTime = gaussrand(BodyCheckSeed_E, BodyCheckSeed_S); departTime = 0; isError = false; if (IDCheckTime < 0) IDCheckTime = 0; if (baggageCheckTime < 0) baggageCheckTime = 0;

<!-- b000796 | furniture | pages [24] -->
Team # 55285

<!-- b000797 | furniture | pages [24] -->
Page 23 of 32

<!-- b000798 | prose | pages [24] -->
if (bodyCheckTime < 0) bodyCheckTime = 0; } HumanBeings(const HumanBeings &other) {

<!-- b000799 | prose | pages [24] -->
waitKind = other.waitKind; isVIP = other.isVIP; isError = other.isError; zoneDTime = other.zoneDTime; arrivalTime = other.arrivalTime; IDCheckTime = other.IDCheckTime; removeThingsTime = other.removeThingsTime; baggageCheckTime = other.baggageCheckTime; bodyCheckTime = other.bodyCheckTime; departTime = other.departTime; baggageNumber = other.baggageNumber; } void produce(bool VIPCheck, double &lastTime) {

<!-- b000800 | prose | pages [24] -->
isVIP = VIPCheck; if (isVIP) {

<!-- b000801 | prose | pages [24] -->
if ((double)rand() / RAND_MAX < VIPErrorRatio) {

<!-- b000802 | prose | pages [24] -->
isError = true; zoneDTime = gaussrand(ZoneDTime_E, ZoneDTime_S); } else isError = false; arrivalTime = possion(VIPArrivalSeed) + lastTime; removeThingsTime = gaussrand(VIPRemoveThingsSeed_E, VIPRemoveThingsSeed_S) + (doubl } else {

<!-- b000803 | prose | pages [24] -->
if ((double)rand() / RAND_MAX < PaxErrorRatio) {

<!-- b000804 | prose | pages [24] -->
isError = true; zoneDTime = gaussrand(ZoneDTime_E, ZoneDTime_S); } else isError = false; arrivalTime = possion(PaxArrivalSeed) + lastTime; removeThingsTime = gaussrand(PaxRemoveThingsSeed_E, PaxRemoveThingsSeed_S) + (doubl } if ((double)rand() / RAND_MAX < AgeSeed) {

<!-- b000805 | prose | pages [24] -->
baggageNumber = 0; removeThingsTime = gaussrand(VIPRemoveThingsSeed_E, VIPRemoveThingsSeed_S); baggageCheckTime = BaggageCheckSeed_1; } if (arrivalTime < FirstPoint) {

<!-- b000806 | prose | pages [24] -->
double r = (double)rand() / RAND_MAX; if (r < RatioCinOne) waitKind = 3; else if (r < RatioCinOne + RatioBinOne) waitKind = 2; else waitKind = 1; } else if (arrivalTime < SecondPoint) {

<!-- b000807 | prose | pages [24] -->
double r = (double)rand() / RAND_MAX; if (r < RatioCinTwo) waitKind = 3; else waitKind = 2; } else waitKind = 3; if (waitKind == 1) NumberKind_1++; if (waitKind == 2) NumberKind_2++; if (zoneDTime < 0) zoneDTime = 0; if (removeThingsTime < 0) removeThingsTime = 0; lastTime = arrivalTime; } }*human;

<!-- b000808 | prose | pages [24] -->
void produceHuman() {

<!-- b000809 | furniture | pages [25] -->
Team # 55285

<!-- b000810 | furniture | pages [25] -->
Page 24 of 32

<!-- b000811 | prose | pages [25] -->
double lastTime = 0; while (lastTime < FastigiumTime) {

<!-- b000812 | prose | pages [25] -->
human[Number++].produce(true, lastTime); VIPNumber++; } Number--; lastTime = 0; while (lastTime < FastigiumTime) {

<!-- b000813 | prose | pages [25] -->
human[Number++].produce(false, lastTime); PaxNumber++; } }

<!-- b000814 | prose | pages [25] -->
double max(double &a, double &b) {

<!-- b000815 | prose | pages [25] -->
if (a > b) return a; return b; }

<!-- b000816 | prose | pages [25] -->
double swap(HumanBeings &a, HumanBeings &b) {

<!-- b000817 | prose | pages [25] -->
HumanBeings c = a; a = b; b = c; }

<!-- b000818 | prose | pages [25] -->
ofstream output("test.txt");

<!-- b000819 | prose | pages [25] -->
void adjustQueue(queue<int> &a, queue<int> &b, int sign) {

<!-- b000820 | prose | pages [25] -->
if (a.size() <= b.size()) return; int qa[a.size()], qb[a.size()], qd[a.size()]; int suma = 0, sumb = 0, sumd = 0; while (!a.empty()) {

<!-- b000821 | prose | pages [25] -->
qa[suma++] = a.front(); a.pop(); } while (!b.empty()) {

<!-- b000822 | prose | pages [25] -->
qb[sumb++] = b.front(); b.pop(); } for (int i = sumb + 2; i < suma; ++i) {

<!-- b000823 | prose | pages [25] -->
int loc = qa[i]; if (i - sumd > sumb + 1 && (sign == 0 || human[loc].waitKind == sign)) {

<!-- b000824 | prose | pages [25] -->
qb[sumb++] = loc; qd[sumd++] = i; } } int nowd = 0; for (int i = 0; i < suma; ++i) {

<!-- b000825 | prose | pages [25] -->
if (i != qd[nowd] || nowd == sumd) a.push(qa[i]); else nowd++; } for (int i = 0; i < sumb; ++i) b.push(qb[i]); }

<!-- b000826 | prose | pages [25] -->
void simulation(int vipIDCheck, int vipLanes, int paxIDCheck, int paxLanes) {

<!-- b000827 | prose | pages [25] -->
int sumIDCheck = vipIDCheck + paxIDCheck; int sumLanes = vipLanes + paxLanes; int nowPoint = 1; double nowTime = 0; queue<int> IDCheckQueue[sumIDCheck]; double IDCheckLastDepartTime[sumIDCheck] = {0}; queue<int> LanesQueue[sumLanes];

<!-- b000828 | furniture | pages [26] -->
Team # 55285

<!-- b000829 | furniture | pages [26] -->
Page 25 of 32

<!-- b000830 | prose | pages [26] -->
double LanesLastDepartTime[sumLanes] = {0}; int lastQueue[sumLanes][ContainMost]; int sumLastQueue[sumLanes] = {0}; double lastDepartTime[sumLanes] = {0}; double lastEnterTime[sumLanes] = {0}; queue<int> zoneDQueue; double zoneDDepartTime = 0;

<!-- b000831 | prose | pages [26] -->
for (int loc = 0; loc < Number; ++loc) {

<!-- b000832 | prose | pages [26] -->
output << loc << ": " << endl; output << ’\t’ << "IDCheckQueue: "; for (int i = 0; i < sumIDCheck; ++i) output << IDCh output << ’\t’ << "LanesQueue: "; for (int i = 0; i < sumLanes; ++i) output << LanesQue output << ’\t’ << "lastQueue: "; for (int i = 0; i < sumLanes; ++i) output << sumLastQu nowTime = human[loc].arrivalTime; human[loc].departTime = nowTime; for (int i = 0; i < sumIDCheck; ++i) {

<!-- b000833 | prose | pages [26] -->
while (!IDCheckQueue[i].empty()) {

<!-- b000834 | prose | pages [26] -->
int loc = IDCheckQueue[i].front(); double dt = max(IDCheckLastDepartTime[i], human[loc].departTime) + human[loc].I if (dt <= nowTime) {

<!-- b000835 | prose | pages [26] -->
IDCheckQueue[i].pop(); IDCheckLastDepartTime[i] = dt; human[loc].departTime = dt;

<!-- b000836 | prose | pages [26] -->
int x = Number, y = 0; if (human[loc].isVIP) {

<!-- b000837 | prose | pages [26] -->
for (int j = 0; j < sumLanes; ++j) {

<!-- b000838 | prose | pages [26] -->
if (LanesQueue[j].size() < x) {

<!-- b000839 | prose | pages [26] -->
x = LanesQueue[j].size(); y = j; } } } else {

<!-- b000840 | prose | pages [26] -->
for (int j = vipLanes; j < sumLanes; ++j) {

<!-- b000841 | prose | pages [26] -->
if (LanesQueue[j].size() < x) {

<!-- b000842 | prose | pages [26] -->
x = LanesQueue[j].size(); y = j; } } } LanesQueue[y].push(loc); } else break; } if (IDCheckQueue[i].empty()) IDCheckLastDepartTime[i] = nowTime; }

<!-- b000843 | prose | pages [26] -->
if (nowTime > SecondPoint && nowPoint == 2) {

<!-- b000844 | prose | pages [26] -->
nowPoint = 3; for (int i = sumIDCheck - 2; i >= 0; --i)

<!-- b000845 | prose | pages [26] -->
adjustQueue(IDCheckQueue[i], IDCheckQueue[sumIDCheck - 1], nowPoint); adjustQueue(IDCheckQueue[2], IDCheckQueue[1], 0); adjustQueue(IDCheckQueue[1], IDCheckQueue[2], 0); adjustQueue(IDCheckQueue[0], IDCheckQueue[1], 0); adjustQueue(IDCheckQueue[0], IDCheckQueue[2], 0); } else if (nowTime > FirstPoint && nowPoint == 1) {

<!-- b000846 | prose | pages [26] -->
nowPoint = 2; for (int i = sumIDCheck - 2; i >= 0; --i)

<!-- b000847 | prose | pages [26] -->
adjustQueue(IDCheckQueue[i], IDCheckQueue[sumIDCheck - 1], nowPoint);

<!-- b000848 | furniture | pages [27] -->
Team # 55285

<!-- b000849 | furniture | pages [27] -->
Page 26 of 32

<!-- b000850 | prose | pages [27] -->
adjustQueue(IDCheckQueue[2], IDCheckQueue[1], 0); adjustQueue(IDCheckQueue[1], IDCheckQueue[2], 0); adjustQueue(IDCheckQueue[0], IDCheckQueue[1], 0); adjustQueue(IDCheckQueue[0], IDCheckQueue[2], 0); }

<!-- b000851 | prose | pages [27] -->
int x = Number, y = 0, temp = 1; if (human[loc].waitKind == nowPoint) temp = 0; if (human[loc].isVIP) {

<!-- b000852 | prose | pages [27] -->
for (int i = 0; i < sumIDCheck - temp; ++i) {

<!-- b000853 | prose | pages [27] -->
if (IDCheckQueue[i].size() < x) {

<!-- b000854 | prose | pages [27] -->
x = IDCheckQueue[i].size(); y = i; } } } else {

<!-- b000855 | prose | pages [27] -->
for (int i = vipIDCheck; i < sumIDCheck - temp; ++i) {

<!-- b000856 | prose | pages [27] -->
if (IDCheckQueue[i].size() < x) {

<!-- b000857 | prose | pages [27] -->
x = IDCheckQueue[i].size(); y = i; } } } IDCheckQueue[y].push(loc);

<!-- b000858 | prose | pages [27] -->
for (int i = 0; i < sumLanes; ++i) {

<!-- b000859 | prose | pages [27] -->
bool flag1 = true; bool flag2 = true; while (flag1 || flag2) {

<!-- b000860 | prose | pages [27] -->
flag1 = flag2 = false; while (!LanesQueue[i].empty()) {

<!-- b000861 | prose | pages [27] -->
int loc = LanesQueue[i].front(); double dt = max(LanesLastDepartTime[i], human[loc].departTime); if (sumLastQueue[i] < ContainMost && dt <= nowTime) {

<!-- b000862 | prose | pages [27] -->
flag2 = true; dt = max(dt, lastEnterTime[i]); LanesLastDepartTime[i] = dt; human[loc].departTime = dt + human[loc].removeThingsTime;

<!-- b000863 | prose | pages [27] -->
LanesQueue[i].pop(); int j = sumLastQueue[i] - 1; for (; j >= 0; --j) {

<!-- b000864 | prose | pages [27] -->
if (j == -1) break; if (human[lastQueue[i][j]].departTime > human[loc].departTime) last else break; } sumLastQueue[i]++; lastQueue[i][j + 1] = loc; } else break; } while (sumLastQueue[i]) {

<!-- b000865 | prose | pages [27] -->
int loc = lastQueue[i][0]; double dt = max(human[loc].departTime, lastDepartTime[i]); if (dt <= nowTime) {

<!-- b000866 | prose | pages [27] -->
flag1 = true; human[loc].departTime = dt + max(human[loc].baggageCheckTime, human[loc lastEnterTime[i] = dt; lastDepartTime[i] = dt + human[loc].bodyCheckTime; if (human[loc].isError) zoneDQueue.push(loc);

<!-- b000867 | furniture | pages [28] -->
Team # 55285

<!-- b000868 | furniture | pages [28] -->
Page 27 of 32

<!-- b000869 | prose | pages [28] -->
sumLastQueue[i]--; for (int k = 0; k < sumLastQueue[i]; ++k) lastQueue[i][k] = lastQueue[i } else break; } } } }

<!-- b000870 | prose | pages [28] -->
// Deal with the tail. for (int i = 0; i < sumIDCheck; ++i) {

<!-- b000871 | prose | pages [28] -->
while (!IDCheckQueue[i].empty()) {

<!-- b000872 | prose | pages [28] -->
int loc = IDCheckQueue[i].front(); double dt = max(IDCheckLastDepartTime[i], human[loc].departTime) + human[loc].IDChe

<!-- b000873 | prose | pages [28] -->
IDCheckQueue[i].pop(); IDCheckLastDepartTime[i] = dt; human[loc].departTime = dt;

<!-- b000874 | prose | pages [28] -->
int x = Number, y = 0; if (human[loc].isVIP) {

<!-- b000875 | prose | pages [28] -->
for (int j = 0; j < sumLanes; ++j) {

<!-- b000876 | prose | pages [28] -->
if (LanesQueue[j].size() < x) {

<!-- b000877 | prose | pages [28] -->
x = LanesQueue[j].size(); y = j; } } } else {

<!-- b000878 | prose | pages [28] -->
for (int j = vipLanes; j < sumLanes; ++j) {

<!-- b000879 | prose | pages [28] -->
if (LanesQueue[j].size() < x) {

<!-- b000880 | prose | pages [28] -->
x = LanesQueue[j].size(); y = j; } } } LanesQueue[y].push(loc); } }

<!-- b000881 | prose | pages [28] -->
for (int i = 0; i < sumLanes; ++i) {

<!-- b000882 | prose | pages [28] -->
if (!sumLastQueue[i] || LanesQueue[i].empty()) continue; do {

<!-- b000883 | prose | pages [28] -->
while (sumLastQueue[i] < ContainMost) {

<!-- b000884 | prose | pages [28] -->
if (!LanesQueue[i].empty()) {

<!-- b000885 | prose | pages [28] -->
int loc = LanesQueue[i].front(); double dt = max(LanesLastDepartTime[i], human[loc].departTime); dt = max(lastEnterTime[i], dt); LanesLastDepartTime[i] = dt; human[loc].departTime = dt + human[loc].removeThingsTime;

<!-- b000886 | prose | pages [28] -->
LanesQueue[i].pop(); int j = sumLastQueue[i] - 1; for (; j >= 0; --j) {

<!-- b000887 | prose | pages [28] -->
if (j == -1) break; if (human[lastQueue[i][j]].departTime > human[loc].departTime) lastQueu else break; } lastQueue[i][j + 1] = loc; sumLastQueue[i]++; }

<!-- b000888 | furniture | pages [29] -->
Team # 55285

<!-- b000889 | furniture | pages [29] -->
Page 28 of 32

<!-- b000890 | prose | pages [29] -->
else break; } int loc = lastQueue[i][0]; double dt = max(human[loc].departTime, lastDepartTime[i]);

<!-- b000891 | prose | pages [29] -->
human[loc].departTime = dt + max(human[loc].baggageCheckTime, human[loc].bodyCheckT lastEnterTime[i] = dt; lastDepartTime[i] = dt + human[loc].bodyCheckTime; if (human[loc].isError) zoneDQueue.push(loc); sumLastQueue[i]--; for (int k = 0; k < sumLastQueue[i]; ++k) lastQueue[i][k] = lastQueue[i][k + 1]; } while (sumLastQueue[i]); }

<!-- b000892 | prose | pages [29] -->
//Zone D while (!zoneDQueue.empty()) {

<!-- b000893 | prose | pages [29] -->
int loc = zoneDQueue.front(); double dt = max(human[loc].departTime, zoneDDepartTime) + human[loc].zoneDTime; human[loc].departTime = dt; zoneDDepartTime = dt; zoneDQueue.pop(); } }

<!-- b000894 | prose | pages [29] -->
ofstream outFileAve[3]; ofstream outFileStd[3];

<!-- b000895 | prose | pages [29] -->
void assessment(double sumAve[][2], double sumVar[][2]) {

<!-- b000896 | prose | pages [29] -->
double sumVIP[2] = {0}, sumPax[2] = {0}, sumAll[2] = {0}; int humanVIP[2] = {0}, humanPax[2] = {0}; for (int i = 0; i < Number; ++i) {

<!-- b000897 | prose | pages [29] -->
double a = human[i].arrivalTime; double d = human[i].departTime; int k = human[i].waitKind; if (k != 3) {

<!-- b000898 | prose | pages [29] -->
if (human[i].isVIP) sumVIP[k - 1] += d - a; if (!human[i].isVIP) sumPax[k - 1] += d - a; if (human[i].isVIP) humanVIP[k - 1]++; if (!human[i].isVIP) humanPax[k - 1]++; sumAll[k - 1] += d - a; } } double aveVIP[2]; double avePax[2]; double aveAll[2]; for (int i = 0; i < 2; ++i) {

<!-- b000899 | prose | pages [29] -->
aveVIP[i] = sumVIP[i] / humanVIP[i]; avePax[i] = sumPax[i] / humanPax[i]; aveAll[i] = sumAll[i] / (humanVIP[i] + humanPax[i]); sumVIP[i] = sumPax[i] = sumAll[i] = 0; } for (int i = 0; i < Number; ++i) {

<!-- b000900 | prose | pages [29] -->
double a = human[i].arrivalTime; double d = human[i].departTime; int k = human[i].waitKind; if (k != 3) {

<!-- b000901 | prose | pages [29] -->
if (human[i].isVIP) sumVIP[k - 1] += (d - a - aveVIP[k - 1]) * (d - a - aveVIP[k - if (!human[i].isVIP) sumPax[k - 1] += (d - a - avePax[k - 1]) * (d - a - avePax[k - sumAll[k - 1] += (d - a - aveAll[k - 1]) * (d - a - aveAll[k - 1]); } }

<!-- b000902 | furniture | pages [30] -->
Team # 55285

<!-- b000903 | furniture | pages [30] -->
Page 29 of 32

<!-- b000904 | prose | pages [30] -->
double varVIP[2]; double varPax[2]; double varAll[2]; for (int i = 0; i < 2; ++i) {

<!-- b000905 | prose | pages [30] -->
varVIP[i] = sumVIP[i] / (humanVIP[i] - 1); varPax[i] = sumPax[i] / (humanPax[i] - 1); varAll[i] = sumAll[i] / (humanVIP[i] + humanPax[i] - 1); sumAve[0][i] += aveVIP[i]; sumAve[1][i] += avePax[i]; sumAve[2][i] += aveAll[i]; sumVar[0][i] += varVIP[i]; sumVar[1][i] += varPax[i]; sumVar[2][i] += varAll[i]; } // output << aveVIP << endl; }

<!-- b000906 | prose | pages [30] -->
bool cmp(const HumanBeings &a, const HumanBeings &b) {

<!-- b000907 | prose | pages [30] -->
return a.arrivalTime < b.arrivalTime; }

<!-- b000908 | prose | pages [30] -->
int main() {

<!-- b000909 | prose | pages [30] -->
outFileAve[0].open("statisticsV2/VIP_Ave.txt"); outFileAve[1].open("statisticsV2/Pax_Ave.txt"); outFileAve[2].open("statisticsV2/All_Ave.txt"); outFileStd[0].open("statisticsV2/VIP_Std.txt"); outFileStd[1].open("statisticsV2/Pax_Std.txt"); outFileStd[2].open("statisticsV2/All_Std.txt"); for (int i = 0; i < 3; ++i) {

<!-- b000910 | prose | pages [30] -->
for (SecondPoint = FastigiumTime / 9 * 5; SecondPoint < FastigiumTime / 9 * 7; SecondPo

<!-- b000911 | prose | pages [30] -->
outFileAve[i] << ’\t’ << SecondPoint; outFileStd[i] << ’\t’ << SecondPoint; } outFileAve[i] << endl; outFileStd[i] << endl; } for (FirstPoint = FastigiumTime / 9 * 2; FirstPoint < FastigiumTime / 9 * 4; FirstPoint +=

<!-- b000912 | prose | pages [30] -->
for (int i = 0; i < 3; ++i) {

<!-- b000913 | prose | pages [30] -->
outFileAve[i] << FirstPoint; outFileStd[i] << FirstPoint; } for (SecondPoint = FastigiumTime / 9 * 5; SecondPoint < FastigiumTime / 9 * 7; SecondPo

<!-- b000914 | prose | pages [30] -->
cout << SecondPoint << endl; double sumAve[3][2] = {0}; double sumVar[3][2] = {0}; for (int i = 0; i < Times; ++i) {

<!-- b000915 | prose | pages [30] -->
human = new HumanBeings[AllNumber]; Number = VIPNumber = PaxNumber = 0; NumberKind_1 = NumberKind_2 = 0; produceHuman(); sort(human, human + Number, cmp);

<!-- b000916 | prose | pages [30] -->
simulation(VIPIDCheck, VIPLanes, PaxIDCheck, PaxLanes); assessment(sumAve, sumVar); delete [] human; } for (int i = 0; i < 3; ++i) {

<!-- b000917 | prose | pages [30] -->
outFileAve[i] << ’\t’ << (sumAve[i][0] * NumberKind_1 + sumAve[i][1] * NumberKi outFileStd[i] << ’\t’ << sqrt((sumVar[i][0] * NumberKind_1 + sumVar[i][1] * Num } } for (int i = 0; i < 3; ++i) {

<!-- b000918 | prose | pages [30] -->
outFileAve[i] << endl; outFileStd[i] << endl; }

<!-- b000919 | furniture | pages [31] -->
Team # 55285

<!-- b000920 | prose | pages [31] -->
} for (int i = 0; i < 3; ++i) {

<!-- b000921 | prose | pages [31] -->
outFileAve[i].close(); outFileStd[i].close(); } return 0; }

<!-- b000922 | prose | pages [31] -->
7 Other ﬁgures

<!-- b000923 | furniture | pages [31] -->
Page 30 of 32

<!-- b000924 | prose | pages [31] -->
Figures in ‘Modiﬁcations to the Current Process’ 7.1

<!-- b000925 | prose | pages [31] -->
Standard Deviations of Different Advance Time

<!-- b000926 | prose | pages [31] -->
12.5

<!-- b000927 | prose | pages [31] -->
[min]

<!-- b000928 | prose | pages [31] -->
12

<!-- b000929 | prose | pages [31] -->
T

<!-- b000930 | prose | pages [31] -->
11.5

<!-- b000931 | prose | pages [31] -->
σ

<!-- b000932 | prose | pages [31] -->
11

<!-- b000933 | prose | pages [31] -->
10.5

<!-- b000934 | prose | pages [31] -->
10

<!-- b000935 | prose | pages [31] -->
9.5

<!-- b000936 | prose | pages [31] -->
9

<!-- b000937 | prose | pages [31] -->
8.5

<!-- b000938 | prose | pages [31] -->
8

<!-- b000939 | prose | pages [31] -->
70

<!-- b000940 | prose | pages [31] -->
t [min] ad2

<!-- b000941 | prose | pages [31] -->
60 50 40 30 20

<!-- b000942 | prose | pages [31] -->
35 60 55

<!-- b000943 | prose | pages [31] -->
[min]

<!-- b000944 | prose | pages [31] -->
50

<!-- b000945 | prose | pages [31] -->
t

<!-- b000946 | prose | pages [31] -->
45

<!-- b000947 | prose | pages [31] -->
ad1

<!-- b000948 | prose | pages [31] -->
40

<!-- b000949 | caption | pages [31] -->
Figure 25: Standard Deviations of Different Advance Time of the First Two Groups

<!-- b000950 | prose | pages [31] -->
Standard Deviations of Different Advance Time

<!-- b000951 | prose | pages [31] -->
[min]

<!-- b000952 | prose | pages [31] -->
21.8 21.6

<!-- b000953 | prose | pages [31] -->
T σ

<!-- b000954 | prose | pages [31] -->
21.4 21.2 21 20.8 20.6 20.4 20.2 20

<!-- b000955 | prose | pages [31] -->
35

<!-- b000956 | prose | pages [31] -->
40

<!-- b000957 | prose | pages [31] -->
45

<!-- b000958 | prose | pages [31] -->
50

<!-- b000959 | prose | pages [31] -->
t

<!-- b000960 | prose | pages [31] -->
55

<!-- b000961 | prose | pages [31] -->
ad1 [min]

<!-- b000962 | prose | pages [31] -->
60

<!-- b000963 | prose | pages [31] -->
40 30 20 70 60 50 [min] t ad2

<!-- b000964 | caption | pages [31] -->
Figure 26: Standard Deviations of Different Advance Time of All the Groups

<!-- b000965 | heading | pages [31] -->
Figures in ‘Model Evaluation & Sensitivity Analysis’

<!-- b000966 | prose | pages [31] -->
7.2

<!-- b000967 | furniture | pages [32] -->
Team # 55285

<!-- b000968 | furniture | pages [32] -->
Page 31 of 32

<!-- b000969 | prose | pages [32] -->
Prior and Regular Passengers' Standard Deviations of Different Advance Time After PBQ Modification

<!-- b000970 | prose | pages [32] -->
1.4

<!-- b000971 | prose | pages [32] -->
[second]

<!-- b000972 | prose | pages [32] -->
1.3

<!-- b000973 | prose | pages [32] -->
at

<!-- b000974 | prose | pages [32] -->
1.2

<!-- b000975 | prose | pages [32] -->
1.1

<!-- b000976 | prose | pages [32] -->
1

<!-- b000977 | prose | pages [32] -->
0.9

<!-- b000978 | prose | pages [32] -->
0.8

<!-- b000979 | prose | pages [32] -->
0.7

<!-- b000980 | prose | pages [32] -->
0.6

<!-- b000981 | prose | pages [32] -->
0.5

<!-- b000982 | prose | pages [32] -->
0 0.05 0.1

<!-- b000983 | prose | pages [32] -->
[min] T12

<!-- b000984 | prose | pages [32] -->
70

<!-- b000985 | prose | pages [32] -->
σ

<!-- b000986 | prose | pages [32] -->
60

<!-- b000987 | prose | pages [32] -->
50

<!-- b000988 | prose | pages [32] -->
40

<!-- b000989 | prose | pages [32] -->
30

<!-- b000990 | prose | pages [32] -->
20

<!-- b000991 | prose | pages [32] -->
10

<!-- b000992 | prose | pages [32] -->
0

<!-- b000993 | prose | pages [32] -->
0.15 0.2 0.25 R cut

<!-- b000994 | caption | pages [32] -->
Figure 27: Prior and Regular Passengers’ Standard Deviations of Different Advance Time

<!-- b000995 | prose | pages [32] -->
After PBQ Modiﬁcation

<!-- b000996 | prose | pages [32] -->
Average Waiting Time of Different R

<!-- b000997 | prose | pages [32] -->
1.4

<!-- b000998 | prose | pages [32] -->
[second]

<!-- b000999 | prose | pages [32] -->
1.3

<!-- b001000 | prose | pages [32] -->
at

<!-- b001001 | prose | pages [32] -->
1.2

<!-- b001002 | prose | pages [32] -->
1.1

<!-- b001003 | prose | pages [32] -->
1

<!-- b001004 | prose | pages [32] -->
0.9

<!-- b001005 | prose | pages [32] -->
0.8

<!-- b001006 | prose | pages [32] -->
0.7

<!-- b001007 | prose | pages [32] -->
0.6

<!-- b001008 | prose | pages [32] -->
0.5

<!-- b001009 | prose | pages [32] -->
0 0.05 0.1

<!-- b001010 | prose | pages [32] -->
After PBQ Modification cut

<!-- b001011 | prose | pages [32] -->
[min]

<!-- b001012 | prose | pages [32] -->
100

<!-- b001013 | prose | pages [32] -->
avg T

<!-- b001014 | prose | pages [32] -->
80

<!-- b001015 | prose | pages [32] -->
60

<!-- b001016 | prose | pages [32] -->
40

<!-- b001017 | prose | pages [32] -->
20

<!-- b001018 | prose | pages [32] -->
0

<!-- b001019 | prose | pages [32] -->
0.15 0.2 0.25 R cut

<!-- b001020 | caption | pages [32] -->
Figure 28: Average Waiting Time of Different Rcut after PBQ Modiﬁcation

<!-- b001021 | prose | pages [32] -->
Average Waiting Time of Different R

<!-- b001022 | prose | pages [32] -->
1.4

<!-- b001023 | prose | pages [32] -->
[second]

<!-- b001024 | prose | pages [32] -->
1.3

<!-- b001025 | prose | pages [32] -->
at

<!-- b001026 | prose | pages [32] -->
1.2

<!-- b001027 | prose | pages [32] -->
1.1

<!-- b001028 | prose | pages [32] -->
1

<!-- b001029 | prose | pages [32] -->
0.9

<!-- b001030 | prose | pages [32] -->
0.8

<!-- b001031 | prose | pages [32] -->
0.7

<!-- b001032 | prose | pages [32] -->
0.6

<!-- b001033 | prose | pages [32] -->
0.5

<!-- b001034 | prose | pages [32] -->
0 0.05 0.1

<!-- b001035 | prose | pages [32] -->
Before PBQ Modification cut

<!-- b001036 | prose | pages [32] -->
[min]

<!-- b001037 | prose | pages [32] -->
100

<!-- b001038 | prose | pages [32] -->
avg T

<!-- b001039 | prose | pages [32] -->
80

<!-- b001040 | prose | pages [32] -->
60

<!-- b001041 | prose | pages [32] -->
40

<!-- b001042 | prose | pages [32] -->
20

<!-- b001043 | prose | pages [32] -->
0

<!-- b001044 | prose | pages [32] -->
0.15 0.2 0.25 R cut

<!-- b001045 | caption | pages [32] -->
Figure 29: Average Waiting Time of Different Rcut before PBQ Modiﬁcation

<!-- b001046 | furniture | pages [33] -->
Team # 55285

<!-- b001047 | furniture | pages [33] -->
Page 32 of 32

<!-- b001048 | prose | pages [33] -->
Standard Deviations of Different Advance Time After PBQ Modification

<!-- b001049 | prose | pages [33] -->
1.4

<!-- b001050 | prose | pages [33] -->
[second]

<!-- b001051 | prose | pages [33] -->
1.3

<!-- b001052 | prose | pages [33] -->
at

<!-- b001053 | prose | pages [33] -->
1.2

<!-- b001054 | prose | pages [33] -->
1.1

<!-- b001055 | prose | pages [33] -->
1

<!-- b001056 | prose | pages [33] -->
0.9

<!-- b001057 | prose | pages [33] -->
0.8

<!-- b001058 | prose | pages [33] -->
0.7

<!-- b001059 | prose | pages [33] -->
0.6

<!-- b001060 | prose | pages [33] -->
0.5

<!-- b001061 | prose | pages [33] -->
0 0.05 0.1

<!-- b001062 | prose | pages [33] -->
[min]

<!-- b001063 | prose | pages [33] -->
70

<!-- b001064 | prose | pages [33] -->
T σ

<!-- b001065 | prose | pages [33] -->
60

<!-- b001066 | prose | pages [33] -->
50

<!-- b001067 | prose | pages [33] -->
40

<!-- b001068 | prose | pages [33] -->
30

<!-- b001069 | prose | pages [33] -->
20

<!-- b001070 | prose | pages [33] -->
10

<!-- b001071 | prose | pages [33] -->
0

<!-- b001072 | prose | pages [33] -->
0.15 0.2 0.25 R cut

<!-- b001073 | caption | pages [33] -->
Figure 30: The Standard Deviations of Different Rcut after PBQ Modiﬁcation

<!-- b001074 | prose | pages [33] -->
Standard Deviations of Different Advance Time Before PBQ Modification

<!-- b001075 | prose | pages [33] -->
1.4

<!-- b001076 | prose | pages [33] -->
[second]

<!-- b001077 | prose | pages [33] -->
1.3

<!-- b001078 | prose | pages [33] -->
at

<!-- b001079 | prose | pages [33] -->
1.2

<!-- b001080 | prose | pages [33] -->
1.1

<!-- b001081 | prose | pages [33] -->
1

<!-- b001082 | prose | pages [33] -->
0.9

<!-- b001083 | prose | pages [33] -->
0.8

<!-- b001084 | prose | pages [33] -->
0.7

<!-- b001085 | prose | pages [33] -->
0.6

<!-- b001086 | prose | pages [33] -->
0.5

<!-- b001087 | prose | pages [33] -->
0 0.05 0.1

<!-- b001088 | prose | pages [33] -->
[min]

<!-- b001089 | prose | pages [33] -->
70

<!-- b001090 | prose | pages [33] -->
T σ

<!-- b001091 | prose | pages [33] -->
60

<!-- b001092 | prose | pages [33] -->
50

<!-- b001093 | prose | pages [33] -->
40

<!-- b001094 | prose | pages [33] -->
30

<!-- b001095 | prose | pages [33] -->
20

<!-- b001096 | prose | pages [33] -->
10

<!-- b001097 | prose | pages [33] -->
0

<!-- b001098 | prose | pages [33] -->
0.15 0.2 0.25 R cut

<!-- b001099 | caption | pages [33] -->
Figure 31: The Standard Deviations of Different Rcut before PBQ Modiﬁcation
