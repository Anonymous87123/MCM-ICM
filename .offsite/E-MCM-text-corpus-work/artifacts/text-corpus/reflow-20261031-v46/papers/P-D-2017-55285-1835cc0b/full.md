# P-D-2017-55285-1835cc0b

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
55285

<!-- b000004 | prose | pages [1] -->
T1 F1

<!-- b000005 | prose | pages [1] -->
T2 F2

<!-- b000006 | prose | pages [1] -->
T3 F3 Problem Chosen

<!-- b000007 | title | pages [1] -->
D

<!-- b000008 | prose | pages [1] -->
T4 F4

<!-- b000009 | title | pages [1] -->
2017

<!-- b000010 | prose | pages [1] -->
MCM/ICM

<!-- b000011 | heading | pages [1] -->
Summary Sheet

<!-- b000012 | title | pages [1] -->
Analysis and Optimization to the Process of Airport

<!-- b000013 | title | pages [1] -->
Security Check

<!-- b000014 | heading | pages [1] -->
Summary

<!-- b000015 | prose | pages [1] -->
Security check is essential to the safety of airline passengers. However, it is also a time consuming process. Passengers have to wait in lines, get ID check, prepare the belong- ings and get screening inspection and sometimes it even takes hours of time to ﬁnish. Besides, the variance of the waiting time in the checkpoints line is also very high, which is difﬁcult for passengers to decide when to reach the airport. Therefore, we are required to ﬁgure out the potential issues and make some modiﬁcations to the current process that can reduce the average waiting time and its variance.

<!-- b000016 | prose | pages [1] -->
We develop the basic model to simulate the current situation of American airports’ security check and study the properties of Pre-Check policy. Though more ‘Pre-Check’ passengers can help alleviate congestion to some degree, the time in the process of wait for screening is the overwhelming majority of the time spent in security check. It occupy over 98% of total time during rush hours. In addition, we also plot the distribution of different total waiting time, and ﬁnd that it is nearly a uniform distribution over several hours. The variance is hence too high for passengers to predict their total waiting time.

<!-- b000017 | prose | pages [1] -->
Based on this conclusion, we mainly build two efﬁcient modiﬁcation models to opti- mize the current situation. The ﬁrst one is ‘multi-passenger linkage model of belong- ings preparation (MPL)’. It shows that if the airport opens up a small zone for several passengers to prepare for screening at the same time, the average time and variance will obviously decrease. The other one is ‘priority-based queuing model (PBQ)’. It suggests airports to set some appropriate time interval limits to provide passengers who is to take off with great convenience without increasing the average time. Besides, it can encour- age people not to arrive at airports so early that aggravate congestion.

<!-- b000018 | prose | pages [1] -->
We also speculate about the TSA’s latest institution for the elderly and children, but it does not make much contribution. At last, we consider the Chinese cultural norms and apply our model to Chinese airports. We construct the cut-in-line model. The result shows that MPL and PBQ models can still keep their high effectiveness. In other word, our models have high stability, high error-tolerant rate and extensive applicability.

<!-- b000019 | keywords | pages [1] -->
Keywords: Security Check; Poisson Distribution; Gaussian Distribution; Queuing Meth-

<!-- b000020 | prose | pages [1] -->
ods

<!-- b000021 | furniture | pages [2] -->
Team # 55285

<!-- b000022 | furniture | pages [2] -->
Page 1 of 32

<!-- b000023 | contents | pages [2] -->
Analysis and Optimization to the Process of Airport

<!-- b000024 | contents | pages [2] -->
Security Check

<!-- b000025 | contents | pages [2] -->
January 24, 2017

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
1 Restatement of the Problem

<!-- b000028 | contents | pages [2] -->
3

<!-- b000029 | contents | pages [2] -->
1.1

<!-- b000030 | contents | pages [2] -->
Background

<!-- b000031 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
3

<!-- b000033 | contents | pages [2] -->
1.1.1

<!-- b000034 | contents | pages [2] -->
An Overview of the Problem . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
3

<!-- b000036 | contents | pages [2] -->
1.1.2

<!-- b000037 | contents | pages [2] -->
The Process of Security Check . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
3

<!-- b000039 | contents | pages [2] -->
1.2

<!-- b000040 | contents | pages [2] -->
literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
3

<!-- b000042 | contents | pages [2] -->
1.3

<!-- b000043 | contents | pages [2] -->
The Task at Hand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
4

<!-- b000045 | contents | pages [2] -->
2 Model Assumptions and Notations

<!-- b000046 | contents | pages [2] -->
4

<!-- b000047 | contents | pages [2] -->
2.1

<!-- b000048 | contents | pages [2] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
4

<!-- b000050 | contents | pages [2] -->
2.2

<!-- b000051 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
5

<!-- b000053 | contents | pages [2] -->
3 The Basic Model of Security Checkpoints

<!-- b000054 | contents | pages [2] -->
6

<!-- b000055 | contents | pages [2] -->
3.1

<!-- b000056 | contents | pages [2] -->
The Design of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
6

<!-- b000058 | contents | pages [2] -->
3.2

<!-- b000059 | contents | pages [2] -->
Sub Models

<!-- b000060 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
6

<!-- b000062 | contents | pages [2] -->
3.2.1

<!-- b000063 | contents | pages [2] -->
Inﬂow Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
6

<!-- b000065 | contents | pages [2] -->
3.2.2

<!-- b000066 | contents | pages [2] -->
Attributes Generation Model . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
6

<!-- b000068 | contents | pages [2] -->
3.2.3

<!-- b000069 | contents | pages [2] -->
Queuing Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
7

<!-- b000071 | contents | pages [2] -->
3.2.4

<!-- b000072 | contents | pages [2] -->
Screening Model

<!-- b000073 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
7

<!-- b000075 | contents | pages [2] -->
3.3

<!-- b000076 | contents | pages [2] -->
The Result of the Model

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
8

<!-- b000079 | contents | pages [2] -->
The Distribution of the Total Time T . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
3.3.1

<!-- b000081 | contents | pages [2] -->
8

<!-- b000082 | contents | pages [2] -->
3.3.2

<!-- b000083 | contents | pages [2] -->
The proportion of the Time Spent in Different Steps . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
8

<!-- b000085 | contents | pages [2] -->
3.3.3

<!-- b000086 | contents | pages [2] -->
The Inﬂuence of the Ratio of Pre-Check Passengers and Regular

<!-- b000087 | contents | pages [2] -->
Passengers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
8

<!-- b000089 | contents | pages [2] -->
3.3.4

<!-- b000090 | contents | pages [2] -->
The Inﬂuence of the Ratio of Pre-Check Lanes and Regular Lanes .

<!-- b000091 | contents | pages [2] -->
10

<!-- b000092 | contents | pages [2] -->
4 Modiﬁcations to the Current Process

<!-- b000093 | contents | pages [2] -->
10

<!-- b000094 | furniture | pages [3] -->
Team # 55285

<!-- b000095 | furniture | pages [3] -->
Page 2 of 32

<!-- b000096 | contents | pages [3] -->
4.1

<!-- b000097 | contents | pages [3] -->
Multi-passenger Linkage Model of Belongings Preparation . . . . . . . . .

<!-- b000098 | contents | pages [3] -->
11

<!-- b000099 | contents | pages [3] -->
4.1.1

<!-- b000100 | contents | pages [3] -->
The Design of MPL Model . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000101 | contents | pages [3] -->
11

<!-- b000102 | contents | pages [3] -->
4.1.2

<!-- b000103 | contents | pages [3] -->
The Effectiveness of MPL Model . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [3] -->
11

<!-- b000105 | contents | pages [3] -->
4.2

<!-- b000106 | contents | pages [3] -->
Priority-based Queuing Model

<!-- b000107 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [3] -->
12

<!-- b000109 | contents | pages [3] -->
4.2.1

<!-- b000110 | contents | pages [3] -->
The Design of PBQ Model . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000111 | contents | pages [3] -->
12

<!-- b000112 | contents | pages [3] -->
4.2.2

<!-- b000113 | contents | pages [3] -->
The Effectiveness of PBQ Model

<!-- b000114 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000115 | contents | pages [3] -->
13

<!-- b000116 | contents | pages [3] -->
4.3

<!-- b000117 | contents | pages [3] -->
Model of Special Population . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000118 | contents | pages [3] -->
14

<!-- b000119 | contents | pages [3] -->
4.3.1

<!-- b000120 | contents | pages [3] -->
The Design of SP Model . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000121 | contents | pages [3] -->
14

<!-- b000122 | contents | pages [3] -->
4.3.2

<!-- b000123 | contents | pages [3] -->
The Effectiveness of SP Model

<!-- b000124 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [3] -->
15

<!-- b000126 | heading | pages [3] -->
5 Model Evaluation & Sensitivity Analysis

<!-- b000127 | prose | pages [3] -->
15

<!-- b000128 | prose | pages [3] -->
5.1 The Cut-in-line Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

<!-- b000129 | prose | pages [3] -->
5.2 The Sensitivity of MPL Model . . . . . . . . . . . . . . . . . . . . . . . . . . 16

<!-- b000130 | prose | pages [3] -->
5.3 The Sensitivity of PBQ Model . . . . . . . . . . . . . . . . . . . . . . . . . . 17

<!-- b000131 | heading | pages [3] -->
6 Conclusion

<!-- b000132 | prose | pages [3] -->
18

<!-- b000133 | prose | pages [3] -->
6.1 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

<!-- b000134 | prose | pages [3] -->
6.1.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

<!-- b000135 | prose | pages [3] -->
6.1.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

<!-- b000136 | prose | pages [3] -->
6.2 Suggestions to the Security Manager . . . . . . . . . . . . . . . . . . . . . . 18

<!-- b000137 | prose | pages [3] -->
6.3 Future Plans . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

<!-- b000138 | heading | pages [3] -->
Appendices

<!-- b000139 | prose | pages [3] -->
20

<!-- b000140 | heading | pages [3] -->
Appendix A Simulation Code

<!-- b000141 | prose | pages [3] -->
20

<!-- b000142 | heading | pages [3] -->
7 Other ﬁgures

<!-- b000143 | prose | pages [3] -->
30

<!-- b000144 | prose | pages [3] -->
7.1 Figures in ‘Modiﬁcations to the Current Process’ . . . . . . . . . . . . . . . 30

<!-- b000145 | prose | pages [3] -->
7.2 Figures in ‘Model Evaluation & Sensitivity Analysis’ . . . . . . . . . . . . . 30

<!-- b000146 | furniture | pages [4] -->
Team # 55285

<!-- b000147 | furniture | pages [4] -->
Page 3 of 32

<!-- b000148 | heading | pages [4] -->
1 Restatement of the Problem

<!-- b000149 | heading | pages [4] -->
1.1 Background

<!-- b000150 | heading | pages [4] -->
1.1.1 An Overview of the Problem

<!-- b000151 | prose | pages [4] -->
In recent years, as the threat of terrorism is upgrading, American society has attached great signiﬁcance to the security of the airport. A key part of the security measures at the airport is security checkpoints, where the passengers and their belongings should be inspected for dangerous objects. However, if the passengers takes a long time to pass the security checkpoints, there will be a negative impact on the customers’ feelings, then the interests of the airlines can be inﬂuenced.

<!-- b000152 | prose | pages [4] -->
There are two major problems in Chicago’s O’Hare international airport and other American airports. First, it is annoying that there are sometimes over-long queues at the airports, but we cannot give an explanation or a prediction. Second, the variance of waiting time is high, that is to say, it is difﬁcult for the travelers to ﬁnd a suitable time to reach the airport without being unnecessarily early or missing the plane. Therefore it makes great sense to solve the congestion problem.

<!-- b000153 | heading | pages [4] -->
1.1.2 The Process of Security Check

<!-- b000154 | prose | pages [4] -->
The process of security check can be decomposed into following processes:

<!-- b000155 | prose | pages [4] -->
• Arriving process: Passengers are assigned at the beginning of our model.

<!-- b000156 | prose | pages [4] -->
• Process of waiting at the checkpoints: Passengers wait at the checkpoints in Zone A and then move to the subsequent queue in Zone B.

<!-- b000157 | prose | pages [4] -->
• ID check process: Passengers get the identiﬁcation check in this process.

<!-- b000158 | prose | pages [4] -->
• Process of waiting for screening: Passengers wait in lanes for screening.

<!-- b000159 | prose | pages [4] -->
• Preparing process: After reaching the front of the line, passengers place their be- longings, including their jackets, liquid containers, computers and so on.

<!-- b000160 | prose | pages [4] -->
• Screening process: Passengers get screened by the millimeter scanner while the goods are scanned by the X-ray, then they retrieve their belongings.

<!-- b000161 | prose | pages [4] -->
• Additional inspection process: If the passengers fail in the screening process, they should get additional inspections in Zone D.

<!-- b000162 | prose | pages [4] -->
1.2 literature review

<!-- b000163 | prose | pages [4, 5] -->
To simplify the problem and facilitate the implementation of computer language, researchers treat time as a discrete variable in the analysis of a single-server queuing system at ﬁrst[1]. After that, some people have applied Queuing Theory to the dynamic allocation of airport security resources, which used pure Markov chain, discontinuous Markov process, Poisson process, statistical properties of transition probability equation and the birth and death process[2] [3]. What’s more, some other people try to achieve a goal of virtual queuing instead of real one in order to get a smoother distribution of ar- riving passengers[4]. We expect to ﬁnd some convenient and intuitive modiﬁcations for the airport security based on the previous wisdom and some necessary math knowledge like Queuing Theory, Probability and Statistics[5].

<!-- b000164 | furniture | pages [5] -->
Team # 55285

<!-- b000165 | furniture | pages [5] -->
Page 4 of 32

<!-- b000167 | heading | pages [5] -->
1.3 The Task at Hand

<!-- b000168 | prose | pages [5] -->
• Construct a mathematical model to simulate the situation of the current security checkpoints and ﬁnd an explanation for the phenomenon of congestion.

<!-- b000169 | prose | pages [5] -->
• Propose some modiﬁcations to improve the current process.

<!-- b000170 | prose | pages [5] -->
• Take the various behaviors of travelers into consideration, then discuss the inﬂu- ence of those factors on the model.

<!-- b000171 | prose | pages [5] -->
• On the basis of the model, give some policy and procedural suggestions to amelio- rate the situation of the security checkpoints.

<!-- b000172 | heading | pages [5] -->
2 Model Assumptions and Notations

<!-- b000173 | heading | pages [5] -->
2.1 Assumptions and Justiﬁcations

<!-- b000174 | prose | pages [5] -->
In order to simplify the course of modeling and draw some reasonable conclusions from our model, we make assumptions as follows:

<!-- b000175 | prose | pages [5] -->
• The excel data can embody the overall level of the airport to some degree. We use the differential method to calculate out the mean value and the standard deviation of the time consumed in different processes.

<!-- b000176 | prose | pages [5] -->
• The intervals of the passengers’ arrivals obey Poisson distribution. Because the time when a passenger arrives is unrelated to that of the last passenger, therefore we assume that the intervals of the passengers’ arrivals obey Poisson distribution.

<!-- b000177 | prose | pages [5] -->
The mean values of the distribution are obtained from the excel data.

<!-- b000178 | prose | pages [5] -->
• The time of ID check and millimeter wave scanning obeys Gaussian distribution.

<!-- b000179 | prose | pages [5] -->
In this two processes, we suppose that the staff of the airport are skillful, that is to say the time cost in these processes ﬂuctuates around a mean value. Thus we assume that they obey Gaussian distribution. The mean values and the standard deviations are also calculated out according to the excel data.

<!-- b000180 | prose | pages [5] -->
• The time interval of two examinations is 11s to pass the X-ray scanning and the time interval between two placements is 2s. According to the excel data, we can see that the interval is sometimes around 2s and sometimes around 11s. We interpret it as: in one time of examination, the inspector inspects several pieces of luggage.

<!-- b000181 | prose | pages [5] -->
There are time intervals between each examinations.

<!-- b000182 | prose | pages [5] -->
• All of the passengers know the rules of the airport. They will go to the back of the shortest queue after arrival.

<!-- b000183 | furniture | pages [6] -->
Team # 55285

<!-- b000184 | furniture | pages [6] -->
Page 5 of 32

<!-- b000185 | prose | pages [6] -->
• There are no emergency incidents happened in the airport. What we discuss is the airport in order and it is clear that any emergency incident can break the order of any airport.

<!-- b000186 | prose | pages [6] -->
• Pre-Check passengers can choose to go through the regular passage of security check when the Pre-Check passage is crowded. As for Pre-Check passengers, it takes them the same time either in Pre-Check passages or in regular passages.

<!-- b000187 | prose | pages [6] -->
• The time of preparing the belongings is 15 ± 5 + 5X s in the Pre-Check passage, while it is 45±10+5X s in the ordinary passage. This is based on our experiments.

<!-- b000188 | prose | pages [6] -->
X is the number of the pieces of luggage.

<!-- b000189 | prose | pages [6] -->
• In our model, there are 4 ID checkpoints in Zone A and 4 checking lanes in Zone B.

<!-- b000190 | prose | pages [6] -->
• We do not take the transiting time between different stations into consideration.

<!-- b000191 | heading | pages [6] -->
2.2 Notations

<!-- b000192 | prose | pages [6] -->
Here we list the symbols and notations used in this paper, as shown in Table 1. Some of them will be deﬁned later in the following sections.

<!-- b000193 | caption | pages [6] -->
Table 1: Notations

<!-- b000194 | prose | pages [6] -->
Symbol Description ta the time interval between two passengers’ arrivals tp the time interval between two Pre-Check passengers’ arrivals tr the time interval between two regular passengers’ arrivals twaitA the time of waiting at Zone A twaitB the time of waiting at Zone B tcheck the time of identiﬁcation check σcheck the standard deviation of tcheck txray the time of X-ray scanning tmilli the time of millimeter wave scanning tpre the time of preparing σpre the standard deviation of tpre tscreening the time of screening T the total time of the security check of a single person Tavg the total time of the security check process of a group of people σT the standard deviation of Tavg Tr the total time consumed by regular passengers Tp the total time consumed by Pre-Check passengers σTr the standard deviation of Tr σTp the standard deviation of Tp Nprepare the number of passengers preparing their belongings Rpassenger the ratio of tp to tr Rlane the ratio of Pre-Check lanes to regular lanes Royp the percentage of people over 70 or under 12 Rcut the percentage of people who cut in line

<!-- b000195 | furniture | pages [7] -->
Team # 55285

<!-- b000196 | furniture | pages [7] -->
Page 6 of 32

<!-- b000197 | heading | pages [7] -->
3 The Basic Model of Security Checkpoints

<!-- b000198 | prose | pages [7] -->
In this section, we develop the basic model to explain the current situation of Amer- ican airports. The basic model simulates the processes mentioned in Section 1.1.2. Then we discover that the process of waiting for screening is the most time consuming. The Pre-Check policy of TSA is effective, but we need to ﬁnd more strategies to solve the problem.

<!-- b000199 | heading | pages [7] -->
3.1 The Design of the Model

<!-- b000200 | prose | pages [7] -->
In order to demonstrate our basic model clearly, we divide it into the four following sub models.

<!-- b000201 | prose | pages [7] -->
• Inﬂow model: This model is designed to simulate the random arrivals of the pas- sengers.

<!-- b000202 | prose | pages [7] -->
• Sub model two: Attributes generating model: In this model, we attribute different properties to the passengers that will inﬂuence the time length of security check.

<!-- b000203 | prose | pages [7] -->
• Queuing model: This model studies the process of waiting in lines.

<!-- b000204 | prose | pages [7] -->
• Screening model: The preparing process and the screening process are discussed in this model.

<!-- b000205 | heading | pages [7] -->
3.2 Sub Models

<!-- b000206 | heading | pages [7] -->
3.2.1 Inﬂow Model

<!-- b000207 | prose | pages [7] -->
The inﬂow model simulates the stochastic arrivals of passengers at the entrance of the airport. According to the excel data, we can obtain that the average time interval of passengers’ arrivals. We can assume that the arrival of each passenger obeys Poisson distribution in Equation (1). λ is the average time interval between the arrivals of two passengers according to the excel data, and N is the number of seconds between the arrivals of two passengers in our stochastic process.

<!-- b000208 | prose | pages [7] -->
P(t = N) = e−λ λN (1) N!

<!-- b000209 | heading | pages [7] -->
3.2.2 Attributes Generation Model

<!-- b000210 | prose | pages [7] -->
After a passenger is assigned in the program, we give some relevant attributes to the passengers, including the time for ID check, the time for millimeter wave scanning, the pieces of luggage they carry, the time for preparing the personal belongings and whether the passenger has enrolled in ‘Pre-Check’. We assume that the ﬁrst two factors obey Gaussian distribution in Equation (2). Then we calculate the mean value and the standard deviation of the ﬁrst three affecting factors. Those of the fourth one are given in the assumptions.

<!-- b000211 | prose | pages [7, 8] -->
−(x−µi)2 1 2σ2 √ ti = 2πe (2) i σi The mean value and the standard are listed in Table 2

<!-- b000212 | furniture | pages [8] -->
Team # 55285

<!-- b000213 | furniture | pages [8] -->
Page 7 of 32

<!-- b000215 | caption | pages [8] -->
Table 2: the Attributes of the Generated Passengers and Their Mean Values and Standard

<!-- b000216 | prose | pages [8] -->
Deviations Attributes(ti) Mean Value(µi/s) Standard Deviation(σi/s) tcheck 11.31 3.70 tmilli 11.64 5.82 tpre_r 45 10 tpre_p 15 5

<!-- b000217 | heading | pages [8] -->
3.2.3 Queuing Model

<!-- b000218 | prose | pages [8] -->
After the arrival of the passengers, they will automatically go to the back of the short- est queue. Then, we use a queuing model to simulate the process that the passengers are waiting in lines. We treat each waiting line of the airport as a queue in our program. The ﬁrst passenger added to the queue will be the ﬁrst to get out as Figure 1 demonstrates.

<!-- b000219 | prose | pages [8] -->
At the front of the queue, the rate of removing each passenger from the queue is determined in the attribute generation model.

<!-- b000220 | prose | pages [8] -->
Regular PreCheck All Step1 Step2 Step3 Step4 Step5 Step6 Step7

<!-- b000221 | prose | pages [8] -->
··· ··· Regular Regular

<!-- b000222 | prose | pages [8] -->
··· ··· ··· ··· Regular

<!-- b000223 | prose | pages [8] -->
Body Scanning ··· ··· Regular Regular ··· Regular Regular Regular Get Baggages Baggage Screen

<!-- b000224 | prose | pages [8] -->
··· ··· PreCheck PreCheck PreCheck PreCheck PreCheck PreCheck

<!-- b000225 | prose | pages [8] -->
Wait For Take Document Prepare For Reach Airpot Wait For Screen Screen Additional Screen Document Check Check Screen

<!-- b000226 | caption | pages [8] -->
Figure 1: The Queuing Model

<!-- b000227 | heading | pages [8] -->
3.2.4 Screening Model

<!-- b000228 | prose | pages [8, 9] -->
When the passengers ﬁnished queuing, they ﬁrst begin to prepare their belongings. Then the passengers and their belongings are scanned respectively. The time cost in this process should be the maximum of the millimeter wave scanning time tmilli and the X-ray scanning time txray.

<!-- b000229 | furniture | pages [9] -->
Team # 55285

<!-- b000230 | furniture | pages [9] -->
Page 8 of 32

<!-- b000232 | prose | pages [9] -->
tscreening = max[tmilli, txray] (3)

<!-- b000233 | heading | pages [9] -->
3.3 The Result of the Model

<!-- b000234 | prose | pages [9] -->
We use c++ to realize the model programmatically and get a set of virtue data, then we process the data to see the cause of congestion.

<!-- b000235 | heading | pages [9] -->
3.3.1 The Distribution of the Total Time T

<!-- b000236 | prose | pages [9] -->
First we want to ﬁgure out how T, the total time consumed in the security check dis- tribute among the travelling populations. We pick out 31678 samples, obtain their total times, and plot Figure 2. According to Figure 2, the total time distribute very uniformly among the populations. That is to say, the probability of the different total time is simi- lar. That explains why it is difﬁcult for passengers to ﬁnd a suitable time to arrive at the airport.

<!-- b000237 | prose | pages [9] -->
Total Time Distribution Total Time Distribution Total Time Distribution 500 Amount Entries Entries 31678 31678 Mean Mean 518.6 518.6 RMS RMS 269.2 269.2 400

<!-- b000238 | prose | pages [9] -->
300

<!-- b000239 | prose | pages [9] -->
200

<!-- b000240 | prose | pages [9] -->
100

<!-- b000241 | prose | pages [9] -->
0 200 400 600 800 1000 1200 Total Time [second]

<!-- b000242 | caption | pages [9] -->
Figure 2: The Distribution of the Total Time

<!-- b000243 | heading | pages [9] -->
3.3.2 The proportion of the Time Spent in Different Steps

<!-- b000244 | prose | pages [9] -->
Then we consider the proportion of the time consumed in different steps, and draw ﬁgure 3. We can see that the time of waiting for screening is very large in proportion to the rest of time. That is the main reason for the congestion of the airport.

<!-- b000245 | heading | pages [9] -->
3.3.3 The Inﬂuence of the Ratio of Pre-Check Passengers and Regular Passengers

<!-- b000246 | prose | pages [9] -->
From Figure 4 and Figure 5 we can view that the curve is in the shape of letter ‘S’. The Tavg converges to a constant as the percentage of Pre-Check passengers grows. This is easy to understand.

<!-- b000247 | furniture | pages [10] -->
Team # 55285

<!-- b000248 | furniture | pages [10] -->
Page 9 of 32

<!-- b000249 | prose | pages [10] -->
Percentage of Time Spent on Each Process

<!-- b000250 | prose | pages [10] -->
Waiting at ID Checkpoints 0.11%

<!-- b000251 | heading | pages [10] -->
ID Check 0.30%

<!-- b000252 | prose | pages [10] -->
Waiting for Screening 98.11% Preparing for Screening 0.66% Screening 0.75% Additional Screening 0.07% Highcharts.com

<!-- b000253 | caption | pages [10] -->
Figure 3: The Percentage of Time in Different Process

<!-- b000254 | prose | pages [10] -->
8 5 Equation y = A/(1+exp(-B*(x-C)^D))+E Adj. R-Squ 0.99315 8 0 Value Standard E Averge Wa A 617.58024 9.25894 Averge Wa B 0.005 9.55053E- 7 5 Averge Wa C 0.09962 9.6187E-6 Averge Wa D 3.0284 0.10629 7 0 Averge Wa E 196.41502 6.11854 6 5 a v g ( s 6 0 R l a n e = 1 : 3 F i t o f R l a n e = 1 : 3 5 5 5 0 4 5 1 p a s s e n g e

<!-- b000255 | caption | pages [10] -->
Figure 4: The Total Time Curves of Different Rpassengers

<!-- b000256 | prose | pages [10, 11] -->
Equation y = A/(1+exp(-B*(x-C)^D))+E 5 5 Adj. R-Square 0.98763 Value Standard Error 5 0 Stanard Error A 545.84726 8.45339 Stanard Error B 0.01102 0.00263 Stanard Error C 0.09955 2.52643E-5 4 5 Stanard Error D 2.94864 0.14403 Stanard Error E -22.46356 6.76615 4 0 σΤ ( s 3 5 R l a n e = 1 : 3 F i t o f R l a n e = 1 : 3 3 0 2 5 1 p a s s e n g e We know that the more Pre-Check passengers, the smaller average time. Therefore, Tavg will ﬁnally converge to the value when everyone can use Pre-Check lane and spend less time, just like the ‘S’ curve of the Natural Growth Model (NGM) in biolagy. We try to use one function of the NGM, Equation (4), to ﬁt the data. The correlation coefﬁcient of the ﬁtting is 0.99, which conﬁrms our thoughts.

<!-- b000257 | caption | pages [10] -->
Figure 5: The Standard Deviation Curves of Different Rpassengers

<!-- b000258 | furniture | pages [11] -->
Team # 55285

<!-- b000259 | furniture | pages [11] -->
Page 10 of 32

<!-- b000261 | prose | pages [11] -->
y = A/(1 + exp(−B(x −C)D)) + E (4)

<!-- b000262 | heading | pages [11] -->
3.3.4 The Inﬂuence of the Ratio of Pre-Check Lanes and Regular Lanes

<!-- b000263 | prose | pages [11] -->
First, we study the inﬂuence of the Rlane, the ratio of Pre-Check lanes and Regular lanes. We consider the three different conditions, when the Rlane is 1:3, 2:2 and 3:1. Our purpose is to ﬁnd an optimal ratio to satisfy the following two requirements:

<!-- b000264 | prose | pages [11] -->
1. Minimize the waiting time.

<!-- b000265 | prose | pages [11] -->
2. When the ratio of the Pre-Check and Regular passengers varies, the variance can be controlled in a small range.

<!-- b000266 | prose | pages [11] -->
For every condition, we change Rpassenger and test the average waiting time. Then we plot the ﬁgure and set Rpassenger as x-axis and the average waiting time t as y-axis to see the tendency in different conditions.

<!-- b000267 | prose | pages [11] -->
As is shown in Figure 6 and Figure 7 , when Rlane is 1:3, the average waiting time and its variance is rather small and stable when we change a series of different Rpassenger. That is to say, the ratio set by the airport is reasonable.

<!-- b000268 | prose | pages [11] -->
R l a n e = 1 : 3 R l a n e = 2 : 2 a v g ( s R l a n e = 3 : 1 F i t o f R l a n e = 1 : 3 1 0 0 F i t o f R l a n e = 2 : 2 F i t o f R l a n e = 3 : 1

<!-- b000269 | prose | pages [11] -->
1 p a s s e n g e

<!-- b000270 | caption | pages [11] -->
Figure 6: The Total Time Curves of Different Rlane

<!-- b000271 | heading | pages [11] -->
4 Modiﬁcations to the Current Process

<!-- b000272 | prose | pages [11] -->
According to the ﬁrst model, the allocation of the four lanes and the percentage of Pre-Check passengers are both optimal, however, congestion still happens at the airport. Thus, we need to ﬁnd more strategies to improve the institution of security check. In this section, we build three extra models to modify the current process, which are:

<!-- b000273 | furniture | pages [12] -->
Team # 55285

<!-- b000274 | furniture | pages [12] -->
Page 11 of 32

<!-- b000275 | prose | pages [12] -->
4 0 0 3 5 0 R l a n e = 1 : 3 R l a n e = 2 : 2 3 0 0 R l a n e = 3 : 1 2 5 0 F i t o f R l a n e = 1 : 3 F i t o f R l a n e = 2 : 2 2 0 0 F i t o f R l a n e = 3 : 1 σΤ ( s 1 5 0 1 0 0 5 0

<!-- b000276 | prose | pages [12] -->
1 p a s s e n g e

<!-- b000277 | caption | pages [12] -->
Figure 7: The Standard Deviation Curves of Different Rlane

<!-- b000278 | prose | pages [12] -->
• Multi-passenger linkage model of belongings preparation (MPL model)

<!-- b000279 | prose | pages [12] -->
• Priority-based queuing model(PBQ model)

<!-- b000280 | prose | pages [12] -->
• Model of special population (SP model)

<!-- b000281 | heading | pages [12] -->
4.1 Multi-passenger Linkage Model of Belongings Preparation

<!-- b000282 | heading | pages [12] -->
4.1.1 The Design of MPL Model

<!-- b000283 | prose | pages [12] -->
As is mentioned in Section 3, congestion mostly happens in the process of waiting for screening. In the previous model, a passenger cannot begin preparing his or her belongings until the last passenger ﬁnishes preparing. It is obvious that we can save more time in this process. Therefore, we make the following improvements.

<!-- b000284 | prose | pages [12] -->
Suppose every checkpoint can allow Nprepare passengers to prepare their belongings at the same time. Once a passenger ﬁnished preparing and started the screening process, another passenger at the front of the waiting line can join the preparing process. In this linkage process, we can guarantee that there are always several passengers preparing their belongings together. Though the preparing time of a certain passenger does not decline, the waiting time of other passengers is lessened.

<!-- b000285 | heading | pages [12] -->
4.1.2 The Effectiveness of MPL Model

<!-- b000286 | prose | pages [12] -->
Then we are to ﬁnd the optimal Nprepare that can reduce the waiting time while the preparing area is not very crowded. As is shown in Figure 8 and Figure 9, we can see that when Nprepare = 3, the total time Tavg is signiﬁcantly reduced. When the Nprepare reaches 4 and 5, the change is not obvious but the area is more crowded. Therefore, we can conclude that three-passenger linkage model is the best strategy. After the MPL modiﬁcation, we draw the proportion of the time in different processes again. As is shown in Figure 11, the time consumed in the process of waiting for screening is reduced from 98.11% to 57.21%.

<!-- b000287 | furniture | pages [13] -->
Team # 55285

<!-- b000288 | furniture | pages [13] -->
Page 12 of 32

<!-- b000289 | prose | pages [13] -->
4 0 0 N p r e p a r e = N p r e p a r e = 6 0 0 N p r e p a r e = 3 5 0 N p r e p a r e = N p r e p a r e = N p r e p a r e = 5 0 0 3 0 0 N p r e p a r e = N p r e p a r e = N p r e p a r e = 2 5 0 N p r e p a r e = 4 0 0 N o P r e p a r N o P r e p a r 2 0 0 3 0 0 a v g ( s σΤ ( s 1 5 0 2 0 0 1 0 0 5 0 1 0 0

<!-- b000290 | prose | pages [13] -->
t a ( s t a ( s

<!-- b000291 | caption | pages [13] -->
Figure 8: The Total Time Curves of Different

<!-- b000292 | caption | pages [13] -->
Figure 9: The Standard Deviation Curve of

<!-- b000293 | prose | pages [13] -->
Nprepare Different Nprepare

<!-- b000294 | prose | pages [13] -->
Percentage of Time Spent on Each Process Percentage of Time Spent on Each Process

<!-- b000295 | prose | pages [13] -->
Waiting at ID Checkpoints 0.11%

<!-- b000296 | heading | pages [13] -->
ID Check 0.30%

<!-- b000297 | prose | pages [13] -->
Waiting at ID Checkpoints 3.00%

<!-- b000298 | heading | pages [13] -->
ID Check 6.31%

<!-- b000299 | prose | pages [13] -->
Waiting for Screening 98.11% Preparing for Screening 0.66% Waiting for Screening 57.21% Preparing For Screening 18.05% Screening 0.75% Additional Screening 0.07% Screening 13.47% Additional Screening 1.96% Highcharts.com Highcharts.com

<!-- b000300 | caption | pages [13] -->
Figure 10: The Percentage of Time in Differ-

<!-- b000301 | caption | pages [13] -->
Figure 11: The Percentage of Time in Differ-

<!-- b000302 | prose | pages [13] -->
ent Process before MPL modiﬁcation ent Process after MPL modiﬁcation

<!-- b000303 | heading | pages [13] -->
4.2 Priority-based Queuing Model

<!-- b000304 | heading | pages [13] -->
4.2.1 The Design of PBQ Model

<!-- b000305 | prose | pages [13] -->
In this model, we divide the four lanes of security check into the following kinds: one Pre-Check lane, two regular lanes and one emergency lane. In the attributes generation process, we add a new property into the attributes, tad, the time between the arrivals of the passengers to the departure of the airplane. Based on this attribute, we divide the passengers into three priorities. We set two time intevals tad1 and tad2. Passengers whose tad is under tad1 are of the ﬁrst priority, whose one is between [tad1, tad1 + tad2] are of the second priority and the rest are of the third priority. The relevant groups of people are called the priority group, the regular group and the over-punctual group.

<!-- b000306 | prose | pages [13] -->
For different priorities, passengers enjoy different policies. For the priority group, passengers can use the emergency lane immediately. For the regular group, passengers cannot go pass the emergency lane until they have been waiting at the airport for a period of tad1. When a period of tad2 has passed, the passengers of the over-punctual group can make use of the emergency lane. This policy can not only guarantee that the one in an urgent can get aboard in the ﬁrst time, but also warn people not to arrive unnecessarily early. Figure 12 discribes this new modiﬁcation.

<!-- b000307 | furniture | pages [14] -->
Team # 55285

<!-- b000308 | furniture | pages [14] -->
Page 13 of 32

<!-- b000309 | prose | pages [14] -->
Emergency At the time nodes, some of regular and pre-check people will have priority attributes and can pass ID check through the Regular emergency lane. Pre-check Redistribute Redistribute

<!-- b000310 | prose | pages [14] -->
Emergency Emergency Emergency Emergency Emergency

<!-- b000311 | prose | pages [14] -->
Regular Regular Regular Regular Regular

<!-- b000312 | prose | pages [14] -->
Reg ular Regular Regular Regular Regular Regular

<!-- b000313 | prose | pages [14] -->
Pre-check Pre-check Pre-check Pre-check Pre-check

<!-- b000314 | prose | pages [14] -->
The First Time Node The Second Time Node Time Process

<!-- b000315 | caption | pages [14] -->
Figure 12: The PBQ Model

<!-- b000316 | heading | pages [14] -->
4.2.2 The Effectiveness of PBQ Model

<!-- b000317 | prose | pages [14] -->
We investigate the average time consumed in the whole process of different groups under PBQ modiﬁcation. We change ta, the arrival time interval between two passengers and observe the trend of the curves. Then we compare it with that without PBQ modi- ﬁcation. According to Figure 13 and Figure 23, at the peak ﬂow of passengers (ta < 1s), Tavg and its standard deviation of the ﬁrst group are signiﬁcantly 9 1 4 B e f o r e P B Q M o d i f i c a t i o B e f o r e P B Q M o d i f i c a t i o 8 A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s 1 2 A f t e r P B Q M o d i f i c a t i o n ( B o t h P r i o r a n d R e g u l a r P a s s e n g e r s A f t e r P B Q M o d i f i c a t i o n ( B o t h P r i o r a n d R e g u l a r P a s s e n g e r s 7 A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r 1 0 6 A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r 5 8 4 i n i n 6 3 a v g ( σΤ ( 4 2 1 2

<!-- b000318 | prose | pages [14] -->
- 1 t a ( s t a ( s

<!-- b000319 | caption | pages [14] -->
Figure 13: The Total Time curves under PBQ

<!-- b000320 | caption | pages [14] -->
Figure 14: The Total Time curves under PBQ

<!-- b000321 | prose | pages [14] -->
Model of Different Groups Model of Different Groups

<!-- b000322 | prose | pages [14] -->
We programme to implement this modiﬁcation and draw the ﬁgure of Tavg as a func- tion of tad1 and tad2 to ﬁnd out the optimal parameters tad1 and tad2.

<!-- b000323 | prose | pages [14] -->
According to Figure 15 and Figure 16, we can conclude that PBQ model has the fol- lowing properties.

<!-- b000324 | prose | pages [14, 15] -->
As is shown in Figure 15, the average time of the three groups does not change much as the parameters change. That is to say, when tad1 and tad2 are set unsuitably, which Average Waiting Time of Different Advance Time [min] [min] 27 avg ad2 70 t T 26

<!-- b000325 | furniture | pages [15] -->
Team # 55285

<!-- b000326 | furniture | pages [15] -->
Page 14 of 32

<!-- b000328 | prose | pages [15] -->
25 60 24 50 23

<!-- b000329 | prose | pages [15] -->
22 40 21

<!-- b000330 | prose | pages [15] -->
30 20

<!-- b000331 | prose | pages [15] -->
19 20 18 35 40 45 50 55 60 t [min] ad1

<!-- b000332 | caption | pages [15] -->
Figure 15: The ﬁgure of Tavg of the ﬁrst two groups

<!-- b000333 | prose | pages [15] -->
Average Waiting Time of Different Advance Time

<!-- b000334 | prose | pages [15] -->
[min] 37.2 37 avg 36.8 T 36.6 36.4 36.2 36 35.8 35.6 35.4 35.2 35 70 t [min] ad2 60 50 60 55 40 [min] 50 t 45 30 ad1 40 20 35

<!-- b000335 | caption | pages [15] -->
Figure 16: The ﬁgure of Tavg of the three groups

<!-- b000336 | prose | pages [15] -->
do not match the relevant ﬂow volumn of passengers, it does not have negative effects. But, if we set suitable parameters, the screening speed of the ﬁrst two groups can be accelerated. In other words, the rate of fault tolerance is strong.

<!-- b000337 | prose | pages [15] -->
It is obvious that in Figure 16, if the sum of tad1 and tad2 is a constant, the average time of the ﬁrst two groups, the priority group and the regular group do not change much. When the sum gets smaller, the average time gets smaller as well. This is because with the decrease of the tad1 and tad2, the number of passengers decreases as well, which means the number of passengers who can make use of the emergency lane is reduced.

<!-- b000338 | prose | pages [15] -->
Therefore, we can set the ratio of tad1 and tad2 according to the ratio of the passengers numbers of the two groups. This means that we can improve the utilization rate of the current resources. Besides, this phenomenon also shows that the model accords to the reality.

<!-- b000339 | heading | pages [15] -->
4.3 Model of Special Population

<!-- b000340 | heading | pages [15] -->
4.3.1 The Design of SP Model

<!-- b000341 | prose | pages [15, 16] -->
In actual situation, the elderly and children are less likely to bring dangerous objects, and they usually do not bring luggage with them as well. According to the website of TSA[6], they have implemented a policy to reduce the time of security inspection of the elderly over 75 and the children under 12. They claim that those people will no longer removing shoes and light outerwear.

<!-- b000342 | furniture | pages [16] -->
Team # 55285

<!-- b000343 | furniture | pages [16] -->
Page 15 of 32

<!-- b000345 | prose | pages [16] -->
We build the model of special population to simulate this situation. We assume that neither the elderly nor the children will bring luggage with them. In this situation, ac- cording to Equation (3), the time of screening equals to the time of body scanning.

<!-- b000346 | prose | pages [16] -->
We set the percentage as 0, 10%, 20%, 30%, respectively. In each condition, we study how Tavg , the average total time changes as a function of ta, the time interval between two passengers’ arrivals.

<!-- b000347 | heading | pages [16] -->
4.3.2 The Effectiveness of SP Model

<!-- b000348 | prose | pages [16] -->
As is shown in Figure 17 and Figure 18, the four curves of 0, 10%, 20%, 30% are similar. The change in Tavg brought by this institution is subtle. That is to say, TSA’s new policy on the ofﬁcial website is not as effective.

<!-- b000349 | prose | pages [16] -->
5 0 0 3 0 0 R o y p = 0 R o y p = 0 R o y p = 1 0 R o y p = 1 0 2 5 0 4 0 0 R o y p = 2 0 R o y p = 2 0 R o y p = 3 0 2 0 0 R o y p = 3 0 3 0 0 1 5 0 a v g ( s 2 0 0 σΤ ( s 1 0 0 1 0 0 5 0

<!-- b000350 | prose | pages [16] -->
t a ( s t a ( s

<!-- b000351 | caption | pages [16] -->
Figure 17: The Total Time Curves of Differ-

<!-- b000352 | caption | pages [16] -->
Figure 18: The Standard Deviation Curve of

<!-- b000353 | prose | pages [16] -->
ent Royp Different Royp

<!-- b000354 | heading | pages [16] -->
5 Model Evaluation & Sensitivity Analysis

<!-- b000355 | prose | pages [16] -->
We operate the model in the condition of Chinese airport to test its sensitivity. We build a cut-in-line model to describe the situation of China. Then we test the sensitivity of modiﬁcation models in Chinese airports.

<!-- b000356 | heading | pages [16] -->
5.1 The Cut-in-line Model

<!-- b000357 | prose | pages [16] -->
In this model, we consider some special factors under China’s reality, including:

<!-- b000358 | prose | pages [16] -->
• In China, the threat of terrorism is not as severe, hence the rules in Chinese airports are not strict as those in America. The passengers do not need to take off their clothes and shoes.

<!-- b000359 | prose | pages [16] -->
• The passengers will attach much importance to personal efﬁciency and there exists the phenomenon of cutting in lines.

<!-- b000360 | furniture | pages [17] -->
Team # 55285

<!-- b000361 | furniture | pages [17] -->
Page 16 of 32

<!-- b000362 | prose | pages [17] -->
Therefore, we make the relevant alternations to our model:

<!-- b000363 | prose | pages [17] -->
• The preparing time of all Chinese people is the same as Pre-Check passengers in the American model.

<!-- b000364 | prose | pages [17] -->
• When a passenger is generated, we give two additional attributes to him or her.

<!-- b000365 | prose | pages [17] -->
One is whether the passenger will cut in lines or not. The other is the position the passenger cut in. We assume that the probability of jumping into each position in front of the passenger is the same. This process is shown in Figure 19.

<!-- b000366 | prose | pages [17] -->
Regular

<!-- b000367 | prose | pages [17] -->
Regular

<!-- b000368 | prose | pages [17] -->
Regular

<!-- b000369 | prose | pages [17] -->
Regular

<!-- b000370 | caption | pages [17] -->
Figure 19: The Process of Cutting Lines

<!-- b000371 | heading | pages [17] -->
5.2 The Sensitivity of MPL Model

<!-- b000372 | prose | pages [17] -->
We investigate the sensitivity of MPL Model in Chinese situation. Under the different rate of cutting in lines, we observe the difference brought by the model. According to

<!-- b000373 | caption | pages [17] -->
Figure 20 and Figure 21, the total time and its variance can still be signiﬁcantly reduced.

<!-- b000374 | prose | pages [17] -->
5 A v e r a g e T i m e w i t h o u t M P L M o d e 5 V a r i a n c e w i t h o u t M P L M o d e 2 0 1 2 1 0 A v e r a g e T i m e w i t h o u t M P L M o d e 1 0 V a r i a n c e w i t h o u t M P L M o d e 1 5 A v e r a g e T i m e w i t h o u t M P L M o d e 1 5 V a r i a n c e w i t h o u t M P L M o d e 5 A v e r a g e T i m e w i t h M P L M o d e 1 0 5 V a r i a n c e w i t h M P L M o d e 1 5 1 0 A v e r a g e T i m e w i t h M P L M o d e 1 0 V a r i a n c e w i t h M P L M o d e 1 5 A v e r a g e T i m e w i t h M P L M o d e 8 1 5 V a r i a n c e w i t h M P L M o d e i n 1 0 6 i n a v g ( σT ( 4 5 2

<!-- b000375 | prose | pages [17] -->
t a ( s t a ( s

<!-- b000376 | caption | pages [17] -->
Figure 20: The Total Time Curves under M-

<!-- b000377 | caption | pages [17] -->
Figure 21: The Standard Deviation Curves

<!-- b000378 | prose | pages [17] -->
PL Model in Chinese Situation under MPL Model in Chinese Situation

<!-- b000379 | furniture | pages [18] -->
Team # 55285

<!-- b000380 | furniture | pages [18] -->
Page 17 of 32

<!-- b000381 | heading | pages [18] -->
5.3 The Sensitivity of PBQ Model

<!-- b000382 | prose | pages [18] -->
We test the sensitivity of PBQ Model in Chinese situation. Under the different rate of cutting in lines, we observe the difference brought by the model. According to Figure 22 and Figure 23, the average time of the priority group and its variance can be signiﬁcantly reduced, while the average time of all the passengers keeps the same as that without the model. This is the same as that in America. From Figure 24, we can view that after the modiﬁcation of PBQ model, the rate of cutting in lines does not make sense to the average consumed time.

<!-- b000383 | prose | pages [18] -->
1 4 9 5 A v e r a g e T i m e B e f o r e P B Q M o d i f i c a t i o 5 V a r i a n c e B e f o r e P B Q M o d i f i c a t i o 1 5 A v e r a g e T i m e B e f o r e P B Q M o d i f i c a t i o 1 5 V a r i a n c e B e f o r e P B Q M o d i f i c a t i o 8 1 2 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s 1 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s 1 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( A l l P a s s e n g e r s 7 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s 1 0 1 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s 1 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( P r i o r P a s s e n g e r s 6 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r s 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r s 1 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r s 1 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( R e g u l a r P a s s e n g e r s 8 5 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( P r o i r a n d R e g u l a r P a s s e n g e r s 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( P r o i r a n d R e g u l a r P a s s e n g e r s 1 5 V a r i a n c e A f t e r P B Q M o d i f i c a t i o n ( P r o i r a n d R e g u l a r P a s s e n g e r s 1 5 A v e r a g e T i m e A f t e r P B Q M o d i f i c a t i o n ( P r o i r a n d R e g u l a r P a s s e n g e r s i n 4 6 i n a v g ( 3 σT ( 4 2 2 1

<!-- b000384 | prose | pages [18] -->
- 1 a ( s t a ( s

<!-- b000385 | caption | pages [18] -->
Figure 22: The Total Time Curves under P-

<!-- b000386 | caption | pages [18] -->
Figure 23: The Standard Deviation Curves

<!-- b000387 | prose | pages [18] -->
BQ Model in Chinese Situation under PBQ Model in Chinese Situation

<!-- b000388 | prose | pages [18] -->
Prior and Regular Passengers' Average Waiting Time of Different R After PBQ Modification cut 1.4 [second] [min] 80 1.3 avg12 at 70 T 1.2 60 1.1 50 1 40 0.9 30 0.8

<!-- b000389 | prose | pages [18] -->
20 0.7

<!-- b000390 | prose | pages [18] -->
0.6 10

<!-- b000391 | prose | pages [18] -->
0.5 0 0 0.05 0.1 0.15 0.2 0.25 R cut

<!-- b000392 | caption | pages [18] -->
Figure 24: Prior and Regular Passengers’ Average Waiting Time of Different Rcut After

<!-- b000393 | prose | pages [18] -->
PBQ Modiﬁcation

<!-- b000394 | prose | pages [18] -->
To conclude, both MPL model and PBQ are as effective in China as that in America. That is to say, our model can also be applied to Chinese airports with a few modiﬁcations.

<!-- b000395 | furniture | pages [19] -->
Team # 55285

<!-- b000396 | furniture | pages [19] -->
Page 18 of 32

<!-- b000397 | heading | pages [19] -->
6 Conclusion

<!-- b000398 | heading | pages [19] -->
6.1 Strengths and Weaknesses

<!-- b000399 | heading | pages [19] -->
6.1.1 Strengths

<!-- b000400 | prose | pages [19] -->
Our models are adaptable to different conditions. Both MPL and PBQ models can still provide stable efﬁciency improvement though there may be some impacts.

<!-- b000401 | prose | pages [19] -->
PBQ model has strong fault tolerance. Though we may not get the exact optimal time interval tad1 and tad2, the modiﬁcation is still able to reduce a lot of time, especially when we meet the extreme peak ﬂow.

<!-- b000402 | prose | pages [19] -->
Our models have broad application prospect. PBQ model can not only reduce the urgent people’s waiting time, but also encourages people not to arrive at airport too early. This can decline the pressure during peak ﬂow.

<!-- b000403 | heading | pages [19] -->
6.1.2 Weaknesses

<!-- b000404 | prose | pages [19] -->
Our models ignore the probability of emergent incident, thus our models only work in a peaceful environment.

<!-- b000405 | prose | pages [19] -->
In the SP model, we just consider the old and the young as another ‘PreCheck’ pas- senger, this may be improper.

<!-- b000406 | prose | pages [19] -->
In the Cut-in-line model, we assume that the occurrence probability of the cutting in line is constant, this may be a little different from reality.

<!-- b000407 | heading | pages [19] -->
6.2 Suggestions to the Security Manager

<!-- b000408 | prose | pages [19] -->
According to our simulation result, we have the following recommendations for the security managers.

<!-- b000409 | prose | pages [19] -->
• Pre-Check policy is indeed effective in accelerating the process, and the ratio of Pre- Check lanes and regular lanes is optimal. Therefore we should keep the suitable ratio and advertise the advantages of Pre-Check policy.

<!-- b000410 | prose | pages [19] -->
• The airports can add a small zone between the screening machine and the waiting lanes, which can allow 3 passengers to prepare for screening in advance at the same time.

<!-- b000411 | prose | pages [19] -->
• The airports can set up some time limit intervals for security check as PBQ model, to reduce the waiting time of the passengers who is going to takeoff. This policy can also encourage passengers not to arrive too early, so that congestion during fastigia can be alleviated. What’s more, the length of the time intervals tad1 and tad2 and the number of passengers in the priority group ﬂow are directly related.

<!-- b000412 | prose | pages [19] -->
• It is not necessary for TSA to consider adjusting policy to the old and the young too much, because this modiﬁcation will not provide passengers with much help.

<!-- b000413 | furniture | pages [20] -->
Team # 55285

<!-- b000414 | furniture | pages [20] -->
Page 19 of 32

<!-- b000415 | prose | pages [20] -->
• For Chinese airports, cutting in lines will not inﬂuence the effectiveness of the two models, therefore we can also apply these two models to Chinese airports.

<!-- b000416 | heading | pages [20] -->
6.3 Future Plans

<!-- b000417 | prose | pages [20] -->
Our present PBQ model has ﬁxed total peak passenger ﬂow, in the future, we try to use the passenger generating time to decide the duration of peak period, MPL can study the linkage condition and time node at a ﬁxed peak time, make more objective evaluations on its performance.

<!-- b000418 | prose | pages [20] -->
Make the occurrence probability of the cutting in line be related to the congestion level, in the real condition, more crowded the airport is, more cut-in-line phenomenon will take place.

<!-- b000419 | heading | pages [20] -->
References

<!-- b000420 | references | pages [20] -->
[1] T. Meisling, “Discrete-time queuing theory,” Operations Research, vol. 6, no. 1, pp.

<!-- b000421 | references | pages [20] -->
96–105, 1958.

<!-- b000422 | references | pages [20] -->
[2] G. Yang, Z. Min, Z. Hang, and L. Yue, “Research on dynamic allocations of airport

<!-- b000423 | references | pages [20] -->
security check resources,” Aeronautical Computing Technology, vol. 46, no. 5, 2016.

<!-- b000424 | references | pages [20] -->
[3] R. de Lange, I. Samoilovich, and B. van der Rhee, “Virtual queuing at airport security

<!-- b000425 | references | pages [20] -->
lanes,” European Journal of Operational Research, vol. 225, no. 1, pp. 153 – 165, 2013.

<!-- b000426 | references | pages [20] -->
[4] M. Bevilacqua and F. E. Ciarapica, “Analysis of check-in procedure using simula-

<!-- b000427 | references | pages [20] -->
tion: A case study,” in 2010 IEEE International Conference on Industrial Engineering and

<!-- b000428 | references | pages [20] -->
Engineering Management, Dec 2010, pp. 1621–1625.

<!-- b000429 | references | pages [20] -->
[5] X. He, Stochastic process and queuing theory.

<!-- b000430 | references | pages [20] -->
Hunan University Press, 2010.

<!-- b000431 | references | pages [20] -->
[6] http://www.portofportland.com/Notices/PDX_TSA_75over_Scrng_01_BLT.htm.

<!-- b000432 | furniture | pages [21] -->
Team # 55285

<!-- b000433 | furniture | pages [21] -->
Page 20 of 32

<!-- b000434 | heading | pages [21] -->
Appendices

<!-- b000435 | heading | pages [21] -->
Appendix A

<!-- b000436 | prose | pages [21] -->
Simulation Code

<!-- b000437 | prose | pages [21] -->
Our simulation codes written in C++:

<!-- b000438 | prose | pages [21] -->
#include<cstdio> #include<cmath> #include<iostream> #include<fstream>

<!-- b000439 | prose | pages [21] -->
using namespace std;

<!-- b000440 | prose | pages [21] -->
const int Files = 4;

<!-- b000441 | prose | pages [21] -->
string filename[Files] = {"A", "B", "E", "F"};

<!-- b000442 | prose | pages [21] -->
double stringToSecond(string &str) { int now = 0; double min = 0, sec = 0; while (str[now] != ’:’) { min = min * 10 + str[now++] - 48; } now++; while (str[now] != ’.’) { sec = sec * 10 + str[now++] - 48; } return min * 60 + sec; }

<!-- b000443 | prose | pages [21] -->
void work(ifstream &inFile, ofstream &outFile) { double second[100], difference[100]; int n = 0; string str; while (inFile >> str) { second[n++] = stringToSecond(str);

<!-- b000444 | prose | pages [21] -->
outFile << second[n - 1] << endl; } double sum = 0; for (int i = 1; i < n; ++i) { difference[i] = second[i] - second[i - 1];

<!-- b000445 | prose | pages [21] -->
sum += difference[i]; } double ave = sum / (n - 1); sum = 0; for (int i = 1; i < n; ++i) { sum += (difference[i] - ave) * (difference[i] - ave); } double vari = sum / (n - 2); outFile << "average: " << ave << endl; outFile << "variance: " << vari << endl; outFile << "standard deviation: " << sqrt(vari) << endl; }

<!-- b000446 | prose | pages [21, 22] -->
int main() { ifstream inFile; ofstream outFile; for (int i = 0; i < Files; ++i) { inFile.open(filename[i] + ".txt"); outFile.open(filename[i] + "_out.txt"); work(inFile, outFile); inFile.close(); outFile.close(); } return 0; }

<!-- b000447 | furniture | pages [22] -->
Team # 55285

<!-- b000448 | furniture | pages [22] -->
Page 21 of 32

<!-- b000450 | prose | pages [22] -->
#include<cstdio> #include<cmath> #include<ctime> #include<cstdlib> #include<iostream> #include<queue> #include<fstream>

<!-- b000451 | heading | pages [22] -->
#include<algorithm>

<!-- b000452 | prose | pages [22] -->
using namespace std;

<!-- b000453 | prose | pages [22] -->
double gaussrand(double E, double V) { static double V1, V2, S; static int phase = 0; double X; if (phase == 0) { do { double U1 = (double)rand() / RAND_MAX; double U2 = (double)rand() / RAND_MAX; V1 = 2 * U1 - 1; V2 = 2 * U2 - 1; S = V1 * V1 + V2 * V2; } while (S >= 1 || S == 0); X = V1 * sqrt(-2 * log(S) / S); } else X = V2 * sqrt(-2 * log(S) / S); phase = 1 - phase; return X * V + E; }

<!-- b000454 | prose | pages [22] -->
double U_Random() { double f; f = (float)(rand() % 100); return f/100; }

<!-- b000455 | prose | pages [22] -->
double possion(double Lambda) { double k = 0; long double p = 1.0; long double l = exp(-Lambda); while (p >= l) { double u = U_Random(); p *= u; k += 1; } return k-1; }

<!-- b000456 | prose | pages [22] -->
const double AgeSeed = 0.0; const double VIPErrorRatio = 0.01; const double PaxErrorRatio = 0.03;

<!-- b000457 | furniture | pages [23] -->
Team # 55285

<!-- b000458 | furniture | pages [23] -->
Page 22 of 32

<!-- b000459 | prose | pages [23] -->
const double VIPArrivalSeed = 4; const double PaxArrivalSeed = 6; const int VIPIDCheck = 1; const int PaxIDCheck = 3; const double IDCheckSeed_E = 11.3125; const double IDCheckSeed_S = 3.70079; const double VIPRemoveThingsSeed_E = 15.0; const double VIPRemoveThingsSeed_S = 5.0; const double PaxRemoveThingsSeed_E = 40.0; const double PaxRemoveThingsSeed_S = 10.0; const int VIPLanes = 1; const int PaxLanes = 3; const double BaggagePrepareSeed = 5.0; const double BaggageCheckSeed_1 = 11.0; const double BaggageCheckSeed_2 = 2.0; const double BodyCheckSeed_E = 11.6; const double BodyCheckSeed_S = 5.8; const double ZoneDTime_E = 120.0; const double ZoneDTime_S = 20.0; const double RatioBinOne = 0.2; const double RatioCinOne = 0.1; const double RatioCinTwo = 0.2;

<!-- b000460 | prose | pages [23] -->
double FastigiumTime = VIPArrivalSeed * 2160; double FirstPoint, SecondPoint; int ContainMost = 3; const int Times = 5; const int AllNumber = 10000; int Number = 0, VIPNumber = 0, PaxNumber = 0; int NumberKind_1 = 0, NumberKind_2 = 0;

<!-- b000461 | prose | pages [23] -->
bool isSrand = false;

<!-- b000462 | prose | pages [23] -->
int baggageRand() { return rand() % 4; }

<!-- b000463 | prose | pages [23] -->
struct HumanBeings { int waitKind; bool isVIP; bool isError; double zoneDTime; double arrivalTime; double IDCheckTime; double removeThingsTime; double baggageCheckTime; double bodyCheckTime; double departTime; int baggageNumber; HumanBeings() { if (!isSrand) { srand((unsigned)time(NULL)); isSrand = true; } IDCheckTime = gaussrand(IDCheckSeed_E, IDCheckSeed_S); baggageNumber = baggageRand(); baggageCheckTime = BaggageCheckSeed_1 + BaggageCheckSeed_2 * baggageNumber; bodyCheckTime = gaussrand(BodyCheckSeed_E, BodyCheckSeed_S); departTime = 0; isError = false; if (IDCheckTime < 0) IDCheckTime = 0; if (baggageCheckTime < 0) baggageCheckTime = 0;

<!-- b000464 | furniture | pages [24] -->
Team # 55285

<!-- b000465 | furniture | pages [24] -->
Page 23 of 32

<!-- b000466 | prose | pages [24] -->
if (bodyCheckTime < 0) bodyCheckTime = 0; } HumanBeings(const HumanBeings &other) { waitKind = other.waitKind; isVIP = other.isVIP; isError = other.isError; zoneDTime = other.zoneDTime; arrivalTime = other.arrivalTime; IDCheckTime = other.IDCheckTime; removeThingsTime = other.removeThingsTime; baggageCheckTime = other.baggageCheckTime; bodyCheckTime = other.bodyCheckTime; departTime = other.departTime; baggageNumber = other.baggageNumber; } void produce(bool VIPCheck, double &lastTime) { isVIP = VIPCheck; if (isVIP) { if ((double)rand() / RAND_MAX < VIPErrorRatio) { isError = true; zoneDTime = gaussrand(ZoneDTime_E, ZoneDTime_S); } else isError = false; arrivalTime = possion(VIPArrivalSeed) + lastTime; removeThingsTime = gaussrand(VIPRemoveThingsSeed_E, VIPRemoveThingsSeed_S) + (doubl } else { if ((double)rand() / RAND_MAX < PaxErrorRatio) { isError = true; zoneDTime = gaussrand(ZoneDTime_E, ZoneDTime_S); } else isError = false; arrivalTime = possion(PaxArrivalSeed) + lastTime; removeThingsTime = gaussrand(PaxRemoveThingsSeed_E, PaxRemoveThingsSeed_S) + (doubl } if ((double)rand() / RAND_MAX < AgeSeed) { baggageNumber = 0; removeThingsTime = gaussrand(VIPRemoveThingsSeed_E, VIPRemoveThingsSeed_S); baggageCheckTime = BaggageCheckSeed_1; } if (arrivalTime < FirstPoint) { double r = (double)rand() / RAND_MAX; if (r < RatioCinOne) waitKind = 3; else if (r < RatioCinOne + RatioBinOne) waitKind = 2; else waitKind = 1; } else if (arrivalTime < SecondPoint) { double r = (double)rand() / RAND_MAX; if (r < RatioCinTwo) waitKind = 3; else waitKind = 2; } else waitKind = 3; if (waitKind == 1) NumberKind_1++; if (waitKind == 2) NumberKind_2++; if (zoneDTime < 0) zoneDTime = 0; if (removeThingsTime < 0) removeThingsTime = 0; lastTime = arrivalTime; } }*human;

<!-- b000467 | prose | pages [24, 25] -->
void produceHuman() { double lastTime = 0; while (lastTime < FastigiumTime) { human[Number++].produce(true, lastTime); VIPNumber++; } Number--; lastTime = 0; while (lastTime < FastigiumTime) { human[Number++].produce(false, lastTime); PaxNumber++; } }

<!-- b000468 | furniture | pages [25] -->
Team # 55285

<!-- b000469 | furniture | pages [25] -->
Page 24 of 32

<!-- b000471 | prose | pages [25] -->
double max(double &a, double &b) { if (a > b) return a; return b; }

<!-- b000472 | prose | pages [25] -->
double swap(HumanBeings &a, HumanBeings &b) { HumanBeings c = a; a = b; b = c; }

<!-- b000473 | prose | pages [25] -->
ofstream output("test.txt");

<!-- b000474 | prose | pages [25] -->
void adjustQueue(queue<int> &a, queue<int> &b, int sign) { if (a.size() <= b.size()) return; int qa[a.size()], qb[a.size()], qd[a.size()]; int suma = 0, sumb = 0, sumd = 0; while (!a.empty()) { qa[suma++] = a.front(); a.pop(); } while (!b.empty()) { qb[sumb++] = b.front(); b.pop(); } for (int i = sumb + 2; i < suma; ++i) { int loc = qa[i]; if (i - sumd > sumb + 1 && (sign == 0 || human[loc].waitKind == sign)) { qb[sumb++] = loc; qd[sumd++] = i; } } int nowd = 0; for (int i = 0; i < suma; ++i) { if (i != qd[nowd] || nowd == sumd) a.push(qa[i]); else nowd++; } for (int i = 0; i < sumb; ++i) b.push(qb[i]); }

<!-- b000475 | prose | pages [25] -->
void simulation(int vipIDCheck, int vipLanes, int paxIDCheck, int paxLanes) { int sumIDCheck = vipIDCheck + paxIDCheck; int sumLanes = vipLanes + paxLanes; int nowPoint = 1; double nowTime = 0; queue<int> IDCheckQueue[sumIDCheck]; double IDCheckLastDepartTime[sumIDCheck] = {0}; queue<int> LanesQueue[sumLanes];

<!-- b000476 | furniture | pages [26] -->
Team # 55285

<!-- b000477 | furniture | pages [26] -->
Page 25 of 32

<!-- b000478 | prose | pages [26] -->
double LanesLastDepartTime[sumLanes] = {0}; int lastQueue[sumLanes][ContainMost]; int sumLastQueue[sumLanes] = {0}; double lastDepartTime[sumLanes] = {0}; double lastEnterTime[sumLanes] = {0}; queue<int> zoneDQueue; double zoneDDepartTime = 0;

<!-- b000479 | prose | pages [26] -->
for (int loc = 0; loc < Number; ++loc) { output << loc << ": " << endl; output << ’\t’ << "IDCheckQueue: "; for (int i = 0; i < sumIDCheck; ++i) output << IDCh output << ’\t’ << "LanesQueue: "; for (int i = 0; i < sumLanes; ++i) output << LanesQue output << ’\t’ << "lastQueue: "; for (int i = 0; i < sumLanes; ++i) output << sumLastQu nowTime = human[loc].arrivalTime; human[loc].departTime = nowTime; for (int i = 0; i < sumIDCheck; ++i) { while (!IDCheckQueue[i].empty()) { int loc = IDCheckQueue[i].front(); double dt = max(IDCheckLastDepartTime[i], human[loc].departTime) + human[loc].I if (dt <= nowTime) { IDCheckQueue[i].pop(); IDCheckLastDepartTime[i] = dt; human[loc].departTime = dt;

<!-- b000480 | prose | pages [26] -->
int x = Number, y = 0; if (human[loc].isVIP) { for (int j = 0; j < sumLanes; ++j) { if (LanesQueue[j].size() < x) { x = LanesQueue[j].size(); y = j; } } } else { for (int j = vipLanes; j < sumLanes; ++j) { if (LanesQueue[j].size() < x) { x = LanesQueue[j].size(); y = j; } } } LanesQueue[y].push(loc); } else break; } if (IDCheckQueue[i].empty()) IDCheckLastDepartTime[i] = nowTime; }

<!-- b000481 | prose | pages [26] -->
if (nowTime > SecondPoint && nowPoint == 2) { nowPoint = 3; for (int i = sumIDCheck - 2; i >= 0; --i) adjustQueue(IDCheckQueue[i], IDCheckQueue[sumIDCheck - 1], nowPoint); adjustQueue(IDCheckQueue[2], IDCheckQueue[1], 0); adjustQueue(IDCheckQueue[1], IDCheckQueue[2], 0); adjustQueue(IDCheckQueue[0], IDCheckQueue[1], 0); adjustQueue(IDCheckQueue[0], IDCheckQueue[2], 0); } else if (nowTime > FirstPoint && nowPoint == 1) { nowPoint = 2; for (int i = sumIDCheck - 2; i >= 0; --i) adjustQueue(IDCheckQueue[i], IDCheckQueue[sumIDCheck - 1], nowPoint);

<!-- b000482 | furniture | pages [27] -->
Team # 55285

<!-- b000483 | furniture | pages [27] -->
Page 26 of 32

<!-- b000484 | prose | pages [27] -->
adjustQueue(IDCheckQueue[2], IDCheckQueue[1], 0); adjustQueue(IDCheckQueue[1], IDCheckQueue[2], 0); adjustQueue(IDCheckQueue[0], IDCheckQueue[1], 0); adjustQueue(IDCheckQueue[0], IDCheckQueue[2], 0); }

<!-- b000485 | prose | pages [27] -->
int x = Number, y = 0, temp = 1; if (human[loc].waitKind == nowPoint) temp = 0; if (human[loc].isVIP) { for (int i = 0; i < sumIDCheck - temp; ++i) { if (IDCheckQueue[i].size() < x) { x = IDCheckQueue[i].size(); y = i; } } } else { for (int i = vipIDCheck; i < sumIDCheck - temp; ++i) { if (IDCheckQueue[i].size() < x) { x = IDCheckQueue[i].size(); y = i; } } } IDCheckQueue[y].push(loc);

<!-- b000486 | prose | pages [27] -->
for (int i = 0; i < sumLanes; ++i) { bool flag1 = true; bool flag2 = true; while (flag1 || flag2) { flag1 = flag2 = false; while (!LanesQueue[i].empty()) { int loc = LanesQueue[i].front(); double dt = max(LanesLastDepartTime[i], human[loc].departTime); if (sumLastQueue[i] < ContainMost && dt <= nowTime) { flag2 = true; dt = max(dt, lastEnterTime[i]); LanesLastDepartTime[i] = dt; human[loc].departTime = dt + human[loc].removeThingsTime;

<!-- b000487 | prose | pages [27] -->
LanesQueue[i].pop(); int j = sumLastQueue[i] - 1; for (; j >= 0; --j) { if (j == -1) break; if (human[lastQueue[i][j]].departTime > human[loc].departTime) last else break; } sumLastQueue[i]++; lastQueue[i][j + 1] = loc; } else break; } while (sumLastQueue[i]) { int loc = lastQueue[i][0]; double dt = max(human[loc].departTime, lastDepartTime[i]); if (dt <= nowTime) { flag1 = true; human[loc].departTime = dt + max(human[loc].baggageCheckTime, human[loc lastEnterTime[i] = dt; lastDepartTime[i] = dt + human[loc].bodyCheckTime; if (human[loc].isError) zoneDQueue.push(loc);

<!-- b000488 | furniture | pages [28] -->
Team # 55285

<!-- b000489 | furniture | pages [28] -->
Page 27 of 32

<!-- b000490 | prose | pages [28] -->
sumLastQueue[i]--; for (int k = 0; k < sumLastQueue[i]; ++k) lastQueue[i][k] = lastQueue[i } else break; } } } }

<!-- b000491 | prose | pages [28] -->
// Deal with the tail. for (int i = 0; i < sumIDCheck; ++i) { while (!IDCheckQueue[i].empty()) { int loc = IDCheckQueue[i].front(); double dt = max(IDCheckLastDepartTime[i], human[loc].departTime) + human[loc].IDChe

<!-- b000492 | prose | pages [28] -->
IDCheckQueue[i].pop(); IDCheckLastDepartTime[i] = dt; human[loc].departTime = dt;

<!-- b000493 | prose | pages [28] -->
int x = Number, y = 0; if (human[loc].isVIP) { for (int j = 0; j < sumLanes; ++j) { if (LanesQueue[j].size() < x) { x = LanesQueue[j].size(); y = j; } } } else { for (int j = vipLanes; j < sumLanes; ++j) { if (LanesQueue[j].size() < x) { x = LanesQueue[j].size(); y = j; } } } LanesQueue[y].push(loc); } }

<!-- b000494 | prose | pages [28] -->
for (int i = 0; i < sumLanes; ++i) { if (!sumLastQueue[i] || LanesQueue[i].empty()) continue; do { while (sumLastQueue[i] < ContainMost) { if (!LanesQueue[i].empty()) { int loc = LanesQueue[i].front(); double dt = max(LanesLastDepartTime[i], human[loc].departTime); dt = max(lastEnterTime[i], dt); LanesLastDepartTime[i] = dt; human[loc].departTime = dt + human[loc].removeThingsTime;

<!-- b000495 | prose | pages [28, 29] -->
LanesQueue[i].pop(); int j = sumLastQueue[i] - 1; for (; j >= 0; --j) { if (j == -1) break; if (human[lastQueue[i][j]].departTime > human[loc].departTime) lastQueu else break; } lastQueue[i][j + 1] = loc; sumLastQueue[i]++; } else break; } int loc = lastQueue[i][0]; double dt = max(human[loc].departTime, lastDepartTime[i]);

<!-- b000496 | furniture | pages [29] -->
Team # 55285

<!-- b000497 | furniture | pages [29] -->
Page 28 of 32

<!-- b000499 | prose | pages [29] -->
human[loc].departTime = dt + max(human[loc].baggageCheckTime, human[loc].bodyCheckT lastEnterTime[i] = dt; lastDepartTime[i] = dt + human[loc].bodyCheckTime; if (human[loc].isError) zoneDQueue.push(loc); sumLastQueue[i]--; for (int k = 0; k < sumLastQueue[i]; ++k) lastQueue[i][k] = lastQueue[i][k + 1]; } while (sumLastQueue[i]); }

<!-- b000500 | prose | pages [29] -->
//Zone D while (!zoneDQueue.empty()) { int loc = zoneDQueue.front(); double dt = max(human[loc].departTime, zoneDDepartTime) + human[loc].zoneDTime; human[loc].departTime = dt; zoneDDepartTime = dt; zoneDQueue.pop(); } }

<!-- b000501 | prose | pages [29] -->
ofstream outFileAve[3]; ofstream outFileStd[3];

<!-- b000502 | prose | pages [29, 30] -->
void assessment(double sumAve[][2], double sumVar[][2]) { double sumVIP[2] = {0}, sumPax[2] = {0}, sumAll[2] = {0}; int humanVIP[2] = {0}, humanPax[2] = {0}; for (int i = 0; i < Number; ++i) { double a = human[i].arrivalTime; double d = human[i].departTime; int k = human[i].waitKind; if (k != 3) { if (human[i].isVIP) sumVIP[k - 1] += d - a; if (!human[i].isVIP) sumPax[k - 1] += d - a; if (human[i].isVIP) humanVIP[k - 1]++; if (!human[i].isVIP) humanPax[k - 1]++; sumAll[k - 1] += d - a; } } double aveVIP[2]; double avePax[2]; double aveAll[2]; for (int i = 0; i < 2; ++i) { aveVIP[i] = sumVIP[i] / humanVIP[i]; avePax[i] = sumPax[i] / humanPax[i]; aveAll[i] = sumAll[i] / (humanVIP[i] + humanPax[i]); sumVIP[i] = sumPax[i] = sumAll[i] = 0; } for (int i = 0; i < Number; ++i) { double a = human[i].arrivalTime; double d = human[i].departTime; int k = human[i].waitKind; if (k != 3) { if (human[i].isVIP) sumVIP[k - 1] += (d - a - aveVIP[k - 1]) * (d - a - aveVIP[k - if (!human[i].isVIP) sumPax[k - 1] += (d - a - avePax[k - 1]) * (d - a - avePax[k - sumAll[k - 1] += (d - a - aveAll[k - 1]) * (d - a - aveAll[k - 1]); } } double varVIP[2]; double varPax[2]; double varAll[2]; for (int i = 0; i < 2; ++i) { varVIP[i] = sumVIP[i] / (humanVIP[i] - 1); varPax[i] = sumPax[i] / (humanPax[i] - 1); varAll[i] = sumAll[i] / (humanVIP[i] + humanPax[i] - 1); sumAve[0][i] += aveVIP[i]; sumAve[1][i] += avePax[i]; sumAve[2][i] += aveAll[i]; sumVar[0][i] += varVIP[i]; sumVar[1][i] += varPax[i]; sumVar[2][i] += varAll[i]; } // output << aveVIP << endl; }

<!-- b000503 | furniture | pages [30] -->
Team # 55285

<!-- b000504 | furniture | pages [30] -->
Page 29 of 32

<!-- b000506 | prose | pages [30] -->
bool cmp(const HumanBeings &a, const HumanBeings &b) { return a.arrivalTime < b.arrivalTime; }

<!-- b000507 | prose | pages [30] -->
int main() { outFileAve[0].open("statisticsV2/VIP_Ave.txt"); outFileAve[1].open("statisticsV2/Pax_Ave.txt"); outFileAve[2].open("statisticsV2/All_Ave.txt"); outFileStd[0].open("statisticsV2/VIP_Std.txt"); outFileStd[1].open("statisticsV2/Pax_Std.txt"); outFileStd[2].open("statisticsV2/All_Std.txt"); for (int i = 0; i < 3; ++i) { for (SecondPoint = FastigiumTime / 9 * 5; SecondPoint < FastigiumTime / 9 * 7; SecondPo outFileAve[i] << ’\t’ << SecondPoint; outFileStd[i] << ’\t’ << SecondPoint; } outFileAve[i] << endl; outFileStd[i] << endl; } for (FirstPoint = FastigiumTime / 9 * 2; FirstPoint < FastigiumTime / 9 * 4; FirstPoint += for (int i = 0; i < 3; ++i) { outFileAve[i] << FirstPoint; outFileStd[i] << FirstPoint; } for (SecondPoint = FastigiumTime / 9 * 5; SecondPoint < FastigiumTime / 9 * 7; SecondPo cout << SecondPoint << endl; double sumAve[3][2] = {0}; double sumVar[3][2] = {0}; for (int i = 0; i < Times; ++i) { human = new HumanBeings[AllNumber]; Number = VIPNumber = PaxNumber = 0; NumberKind_1 = NumberKind_2 = 0; produceHuman(); sort(human, human + Number, cmp);

<!-- b000508 | prose | pages [30, 31] -->
simulation(VIPIDCheck, VIPLanes, PaxIDCheck, PaxLanes); assessment(sumAve, sumVar); delete [] human; } for (int i = 0; i < 3; ++i) { outFileAve[i] << ’\t’ << (sumAve[i][0] * NumberKind_1 + sumAve[i][1] * NumberKi outFileStd[i] << ’\t’ << sqrt((sumVar[i][0] * NumberKind_1 + sumVar[i][1] * Num } } for (int i = 0; i < 3; ++i) { outFileAve[i] << endl; outFileStd[i] << endl; } } for (int i = 0; i < 3; ++i) { outFileAve[i].close();

<!-- b000509 | furniture | pages [31] -->
Team # 55285

<!-- b000510 | furniture | pages [31] -->
Page 30 of 32

<!-- b000512 | prose | pages [31] -->
outFileStd[i].close();

<!-- b000513 | prose | pages [31] -->
} return 0; }

<!-- b000514 | heading | pages [31] -->
7 Other ﬁgures

<!-- b000515 | heading | pages [31] -->
7.1 Figures in ‘Modiﬁcations to the Current Process’

<!-- b000516 | prose | pages [31] -->
Standard Deviations of Different Advance Time

<!-- b000517 | prose | pages [31] -->
12.5 [min] 12 T 11.5 σ 11 10.5 10 9.5 9 8.5 8 70 t [min] ad2 60 50 60 55 40 [min] 50 t 45 30 ad1 40 20 35

<!-- b000518 | caption | pages [31] -->
Figure 25: Standard Deviations of Different Advance Time of the First Two Groups

<!-- b000519 | prose | pages [31] -->
Standard Deviations of Different Advance Time

<!-- b000520 | prose | pages [31] -->
[min] 21.8 21.6 T σ 21.4 21.2 21 20.8 20.6 20.4 20.2 20 35 40 45 50 t 55 ad1 [min] 60 70 60 50 40 30 20 [min] t ad2

<!-- b000521 | caption | pages [31] -->
Figure 26: Standard Deviations of Different Advance Time of All the Groups

<!-- b000522 | heading | pages [31] -->
7.2 Figures in ‘Model Evaluation & Sensitivity Analysis’

<!-- b000523 | furniture | pages [32] -->
Team # 55285

<!-- b000524 | furniture | pages [32] -->
Page 31 of 32

<!-- b000525 | prose | pages [32] -->
Prior and Regular Passengers' Standard Deviations of Different Advance Time After PBQ Modification 1.4 [second] [min] 1.3 T12 70 σ at 1.2 60

<!-- b000526 | prose | pages [32] -->
1.1 50 1 40 0.9 30 0.8 20 0.7

<!-- b000527 | prose | pages [32] -->
10 0.6

<!-- b000528 | prose | pages [32] -->
0.5 0 0 0.05 0.1 0.15 0.2 0.25 R cut

<!-- b000529 | caption | pages [32] -->
Figure 27: Prior and Regular Passengers’ Standard Deviations of Different Advance Time

<!-- b000530 | prose | pages [32] -->
After PBQ Modiﬁcation

<!-- b000531 | prose | pages [32] -->
Average Waiting Time of Different R After PBQ Modification cut 1.4 [second] [min] 100 1.3 avg T at 1.2 80 1.1

<!-- b000532 | prose | pages [32] -->
1 60

<!-- b000533 | prose | pages [32] -->
0.9 40 0.8

<!-- b000534 | prose | pages [32] -->
0.7 20 0.6

<!-- b000535 | prose | pages [32] -->
0.5 0 0 0.05 0.1 0.15 0.2 0.25 R cut

<!-- b000536 | caption | pages [32] -->
Figure 28: Average Waiting Time of Different Rcut after PBQ Modiﬁcation

<!-- b000537 | prose | pages [32] -->
Average Waiting Time of Different R Before PBQ Modification cut 1.4 [second] [min] 100 1.3 avg T at 1.2 80 1.1

<!-- b000538 | prose | pages [32] -->
1 60

<!-- b000539 | prose | pages [32] -->
0.9 40 0.8

<!-- b000540 | prose | pages [32] -->
0.7 20 0.6

<!-- b000541 | prose | pages [32, 33] -->
0.5 0 0 0.05 0.1 0.15 0.2 0.25 R cut Standard Deviations of Different Advance Time After PBQ Modification 1.4 [second] [min] 70 1.3 T σ at 60 1.2

<!-- b000542 | caption | pages [32] -->
Figure 29: Average Waiting Time of Different Rcut before PBQ Modiﬁcation

<!-- b000543 | furniture | pages [33] -->
Team # 55285

<!-- b000544 | furniture | pages [33] -->
Page 32 of 32

<!-- b000546 | prose | pages [33] -->
1.1 50

<!-- b000547 | prose | pages [33] -->
1 40 0.9 30 0.8 20 0.7 10 0.6

<!-- b000548 | prose | pages [33] -->
0.5 0 0 0.05 0.1 0.15 0.2 0.25 R cut

<!-- b000549 | caption | pages [33] -->
Figure 30: The Standard Deviations of Different Rcut after PBQ Modiﬁcation

<!-- b000550 | prose | pages [33] -->
Standard Deviations of Different Advance Time Before PBQ Modification 1.4 [second] [min] 70 1.3 T σ at 60 1.2

<!-- b000551 | prose | pages [33] -->
1.1 50

<!-- b000552 | prose | pages [33] -->
1 40 0.9 30 0.8 20 0.7 10 0.6

<!-- b000553 | prose | pages [33] -->
0.5 0 0 0.05 0.1 0.15 0.2 0.25 R cut

<!-- b000554 | caption | pages [33] -->
Figure 31: The Standard Deviations of Different Rcut before PBQ Modiﬁcation
