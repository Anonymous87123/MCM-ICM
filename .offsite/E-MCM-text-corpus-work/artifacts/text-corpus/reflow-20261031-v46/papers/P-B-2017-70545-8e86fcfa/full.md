# P-B-2017-70545-8e86fcfa

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
70545

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | prose | pages [1] -->
T4 F4

<!-- b000007 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
Control Time Model: Wait One Second and Start Your

<!-- b000010 | title | pages [1] -->
Journey

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
People around the world are complaining about the trafﬁc jams every day. Some people may spend more than 3 hours on their way from ofﬁce to home everyday on their cars, which makes them frustrated. And our problem is to investigate the methods to optimize the design of toll plazas on highways, especially the area after merging, which is also a possible location where vehicles can be stuck in.

<!-- b000013 | prose | pages [1] -->
Before establishment of our models, we list some assumptions to make the real life scenario easier to model.

<!-- b000014 | prose | pages [1] -->
And then we start to analyze the existing models, from which we conclude their strengths and weaknesses. By investigating their characteristics, we get the inspiration to form our two new models: Control Time Model (CTM) and Waiting Area Model(WAM). In these two new models, we introduced a way of conducting control of the departure time of the vehicles at the tollbooths. This kind of control is basically preventing the vehi- cles which are merging in the same lane from leaving the booths simultaneously, which may be a hidden danger for trafﬁc accident or leads to a trafﬁc jam. And we?ll continue to calculate the size and shape of the merging area according to our control methods and some assumptions. After that, we introduce a method for ﬁnding the optimal merging pattern based on both mathematical proof and computer simulations.

<!-- b000015 | prose | pages [1] -->
After that, we run some simulations to ﬁnd out the throughput, risk and cost of dif- ferent models, which are based on some statistical laws for real life situations. Then we compare these three models in all factors with the help of statistical hypothesis testing, and conclude that the CTM is the best in general. The next section is about some slight modiﬁcation under different conditions such as including the self-driving car, and the different arrangements in terms of merging patterns when the proportion of different types of tollbooths vary.

<!-- b000016 | prose | pages [1] -->
For the following section, we test our model by investigating the sensitivity of con- struction cost and throughput (per hour) in terms of some variables included in our model, in order to justify the reliability of our model from different perspectives.

<!-- b000017 | prose | pages [1] -->
Finally, we end our report by the conclusion part followed by strengths and weak- nesses analysis.

<!-- b000018 | furniture | pages [2] -->
Team # 70545

<!-- b000019 | furniture | pages [2] -->
Page 1 of 25

<!-- b000020 | prose | pages [2] -->
PO Box 5042, Woodbridge, NJ 07095-5042.

<!-- b000021 | prose | pages [2] -->
Dear New Jersey Turnpike Authority,

<!-- b000022 | prose | pages [2] -->
We are a group of students having conducted a project focusing on solving the problem of merging after tollbooths. And we are sending this letter to let you know the problems that may exist in current toll plaza and suggesting some possible ways to improve it.

<!-- b000023 | prose | pages [2] -->
First of all, by analyzing the design of existing toll plazas on the highways, we ﬁnd out the following weaknesses of them. At most toll plazas, the vehicles go disorderedly after toll for following reasons. For some toll plazas, there are no leading lines after toll, so drivers just go at their own discretion, thus their routes become unpredictable. And even there are some orientation lines, if two vehicles arrive at the merging point at the same time, only one of them can go through at one time and it will also cause some problems. Disorder after toll leads to both harm to the eﬃciency of the highway entrance and more risk for traﬃc accidents.

<!-- b000024 | prose | pages [2] -->
Therefore, to solve the above problem, we introduced a new model called “Control Time Model” (CTM). In our model, the releases of cars are controlled at the booth, ensuring that the time interval from any two releases of cars are more that the “safe time”. Therefore, the merging becomes more orderly and safer.

<!-- b000025 | prose | pages [2] -->
We run some simulations with our models to test and compare the eﬃciency between the CTM and current existing models. The result is that, the eﬃciency of CTM is only slightly smaller than existing model (about 0.6 throughput less per lane per hour), but we haven’t considered the time wasted when accidents happen, which is a lot more likely to take place in existing models theoretically.

<!-- b000026 | prose | pages [2] -->
And also according to the simulation, the risk of car crashes is also limited to a lower level, which is 13.66% less than current existing models.

<!-- b000027 | prose | pages [2] -->
In terms of expenditure of construction and maintenance, as our model is much more orderly, the total length of the merging area can be reduced.

<!-- b000028 | prose | pages [2] -->
Therefore, a decrease in the total expense is expected, let alone the fact that maintenance of plaza could be a lot easier if accident rate decreases distinctively.

<!-- b000029 | prose | pages [2] -->
All in all, our conclusion is that the CTM performs better than existing models in all aspects including but not limited to eﬃciency, risk elimination as well as total cost. Therefore, it is worthwhile to consider the future construction with our model design.

<!-- b000030 | prose | pages [2] -->
Thank you for considering our model and wish you a bright future.

<!-- b000031 | prose | pages [2] -->
Sincerely,

<!-- b000032 | furniture | pages [2] -->
Team#70545

<!-- b000033 | prose | pages [2] -->
MCM2017

<!-- b000034 | furniture | pages [3] -->
Team # 70545

<!-- b000035 | furniture | pages [3] -->
Page 2 of 25

<!-- b000036 | contents | pages [3] -->
Control Time Model: Wait One Second and Start Your

<!-- b000037 | contents | pages [3] -->
Journey

<!-- b000038 | heading | pages [3] -->
Contents

<!-- b000039 | contents | pages [3] -->
1 Introduction

<!-- b000040 | contents | pages [3] -->
3

<!-- b000041 | contents | pages [3] -->
1.1

<!-- b000042 | contents | pages [3] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [3] -->
3

<!-- b000044 | contents | pages [3] -->
1.2

<!-- b000045 | contents | pages [3] -->
Restatement of the problem . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [3] -->
3

<!-- b000047 | contents | pages [3] -->
1.3

<!-- b000048 | contents | pages [3] -->
Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [3] -->
3

<!-- b000050 | contents | pages [3] -->
2 Assumptions

<!-- b000051 | contents | pages [3] -->
3

<!-- b000052 | contents | pages [3] -->
3 Notations

<!-- b000053 | contents | pages [3] -->
4

<!-- b000054 | contents | pages [3] -->
4 Models

<!-- b000055 | contents | pages [3] -->
4

<!-- b000056 | contents | pages [3] -->
4.1

<!-- b000057 | contents | pages [3] -->
Existing Model(EM)

<!-- b000058 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [3] -->
5

<!-- b000060 | contents | pages [3] -->
4.2

<!-- b000061 | contents | pages [3] -->
Control Time Model (CTM) . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [3] -->
5

<!-- b000063 | contents | pages [3] -->
4.3

<!-- b000064 | contents | pages [3] -->
Waiting Area Model(WAM) . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [3] -->
8

<!-- b000066 | contents | pages [3] -->
5 Analysis and Results

<!-- b000067 | contents | pages [3] -->
9

<!-- b000068 | contents | pages [3] -->
5.1

<!-- b000069 | contents | pages [3] -->
Throughput . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [3] -->
9

<!-- b000071 | contents | pages [3] -->
5.1.1

<!-- b000072 | contents | pages [3] -->
Throughput of existing model . . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [3] -->
9

<!-- b000074 | contents | pages [3] -->
5.1.2

<!-- b000075 | contents | pages [3] -->
Throughput of control time model

<!-- b000076 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [3] -->
10

<!-- b000078 | contents | pages [3] -->
5.1.3

<!-- b000079 | contents | pages [3] -->
Throughput of waiting area model

<!-- b000080 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [3] -->
11

<!-- b000082 | contents | pages [3] -->
5.1.4

<!-- b000083 | contents | pages [3] -->
Comparison and hypothesis tests of throughputs . . . . . . . . . . . .

<!-- b000084 | contents | pages [3] -->
11

<!-- b000085 | contents | pages [3] -->
5.2

<!-- b000086 | contents | pages [3] -->
Accident prevention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [3] -->
13

<!-- b000088 | contents | pages [3] -->
5.3

<!-- b000089 | contents | pages [3] -->
Cost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [3] -->
14

<!-- b000091 | contents | pages [3] -->
6 Possible Modiﬁcation

<!-- b000092 | contents | pages [3] -->
15

<!-- b000093 | contents | pages [3] -->
6.1

<!-- b000094 | contents | pages [3] -->
Mixture of autonomous vehicles and human-driving vehicles

<!-- b000095 | contents | pages [3] -->
. . . . . . . . .

<!-- b000096 | contents | pages [3] -->
15

<!-- b000097 | contents | pages [3] -->
6.2

<!-- b000098 | contents | pages [3] -->
Change in proportion of di↵erent types of tollbooths

<!-- b000099 | contents | pages [3] -->
. . . . . . . . . . . . .

<!-- b000100 | contents | pages [3] -->
15

<!-- b000101 | contents | pages [3] -->
7 Sensitivity test

<!-- b000102 | contents | pages [3] -->
16

<!-- b000103 | contents | pages [3] -->
7.1

<!-- b000104 | contents | pages [3] -->
Sensitivity test of throughput

<!-- b000105 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [3] -->
16

<!-- b000107 | contents | pages [3] -->
7.2

<!-- b000108 | contents | pages [3] -->
Sensitivity test of ﬁxed cost

<!-- b000109 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [3] -->
17

<!-- b000111 | contents | pages [3] -->
8 Conclusion

<!-- b000112 | contents | pages [3] -->
17

<!-- b000113 | contents | pages [3] -->
9 Strengths and Weaknesses

<!-- b000114 | contents | pages [3] -->
19

<!-- b000115 | contents | pages [3] -->
9.1

<!-- b000116 | contents | pages [3] -->
Strengths

<!-- b000117 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000118 | contents | pages [3] -->
19

<!-- b000119 | contents | pages [3] -->
9.2

<!-- b000120 | contents | pages [3] -->
Weaknesses

<!-- b000121 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000122 | contents | pages [3] -->
19

<!-- b000123 | contents | pages [3] -->
Appendix

<!-- b000124 | contents | pages [3] -->
22

<!-- b000125 | furniture | pages [4] -->
Team # 70545

<!-- b000126 | furniture | pages [4] -->
Page 3 of 25

<!-- b000127 | heading | pages [4] -->
1 Introduction

<!-- b000128 | heading | pages [4] -->
1.1 Background

<!-- b000129 | prose | pages [4] -->
Traveling on highways in recent years are quite convenient ways for people to go to another city. With a compared high speed limit on highway, people are able to travel a lot faster. However, building highways are quite expensive and it also takes a lot for the maintenance. Therefore, building of toll plazas along the highway is a common practice all around the world. Meanwhile, there are many factors to be considered during the design and the construction of the tollbooths. Firstly, the lands and the construction fee for the booths and roads are very expensive, so we need to minimize the area. And as the vehicles on the highway always have a high speed, it is also quite dangerous when they want to merge into a lane. Finally, the design of the booths is also supposed to guarantee the eﬃciency, which is described by the quantity throughout the highway for a certain time interval.

<!-- b000130 | heading | pages [4] -->
1.2 Restatement of the problem

<!-- b000131 | prose | pages [4] -->
As required by the question, we are supposed to determine the shape, size and merging pattern at the toll plaza depended on number of lanes on the highway in one direction (L) and total number of tollbooths in one direction (B). Meanwhile, we will also justify our approach by comparing it with the existing models in terms of risk, cost and eﬃciency. What’s more, the implement of our plan in various situations (e.g. mixture of the self-driving vehicle and di↵erent proportion distribution of types of tollbooths) will also be shown.

<!-- b000132 | heading | pages [4] -->
1.3 Literature review

<!-- b000133 | prose | pages [4] -->
The optimal number of tollbooths needed to minimize the average waiting time is well-studied and simulated based on di↵erent real situations (Corwen et al, 2005). Though the deﬁnition of “optimal” varies, similar suggestions have been given. Tollbooths should be implemented conforming to encouraged behaviors, e.g. faster booths should be put on the left (Spann et al, 2005), which is incorporated in our model. Some literature suggested that tollbooths employ no barrier to ensure a relatively smooth ﬂow (Kane, 2005), but we contend that the uplift of barrier takes negligible amount of time, the beneﬁt of which cannot be compared with the chaos and potential risk if some vehicles go through toll plaza directly. Therefore, barriers are included in our model.

<!-- b000134 | heading | pages [4] -->
2 Assumptions

<!-- b000135 | prose | pages [4] -->
To simplify the real life situation, we will make the following assumptions as a start of construction of our models.

<!-- b000136 | prose | pages [4] -->
• Most of the drivers are rational. They will choose the path as suggested by signals at entrance, and act as risk averters. It is reasonable to make this assumption, because without it, it’s meaningless to make any rules as people won’t obey them.

<!-- b000137 | furniture | pages [5] -->
Team # 70545

<!-- b000138 | furniture | pages [5] -->
Page 4 of 25

<!-- b000139 | prose | pages [5] -->
• The arrival time lapse between the ﬁrst vehicle and the second vehicle in the heavy traﬃc follows uniform distribution. By the heavy traﬃc assumption, the second vehicle comes to tollbooth before the ﬁrst vehicle leaves.

<!-- b000140 | prose | pages [5] -->
• All the paths of the vehicles follow either constant speed motion or constant acceleration motion. As the average speed for the vehicles around the tollbooths are relatively low.

<!-- b000141 | prose | pages [5] -->
• vehicles are queuing at the entrance of the tollbooth one by one with low speed in the heavy traﬃc situation . And we further assume them to be stationary in our models.

<!-- b000142 | prose | pages [5] -->
• The service by human-sta↵s at the tollbooth is quite time-consuming, and the approximate mean service time is around 15 seconds, which follows a normal distribution. This assumption is appropriate, because driver need to bring the fee to the sta↵and the sta↵may need to prepare changes for it. And the time varies from people and di↵erent situations.

<!-- b000143 | prose | pages [5] -->
• The length of vehicles is omitted during the calculation for the size and shape for the merging area. It is valid because the magnitude of the length of toll plaza is a lot larger than the length of vehicles.

<!-- b000144 | heading | pages [5] -->
3 Notations

<!-- b000145 | heading | pages [5] -->
Notation

<!-- b000146 | prose | pages [5] -->
Deﬁnition Unit L Number of outgoing lanes in highway N/A B Number of tollbooths N/A D Distance between the tollbooth and the end of the plaza m dl Width of the lane in highway m db Width of the lane in tollbooth area m r Radius for vehicles’ turning m Th Time of toll service per vehicle human-sta↵ed tollbooths s t0 Time of control (to be deﬁned in Section 4.2) s vm Speed limit in merging area m/s m/s2 as Starting acceleration of vehicles after toll payment m/s2 ab Deceleration of braking vehicles

<!-- b000147 | heading | pages [5] -->
4 Models

<!-- b000148 | prose | pages [5] -->
In this section, we ﬁrst introduce and analyze the existing model, and then two new models invented by us. And the focus for the new models will only be the establishment of the ﬁrst new model (control time model) and second new model (waiting area model) only deviates from the ﬁrst one slightly.

<!-- b000149 | furniture | pages [6] -->
Team # 70545

<!-- b000150 | furniture | pages [6] -->
Page 5 of 25

<!-- b000151 | heading | pages [6] -->
4.1 Existing Model(EM)

<!-- b000152 | prose | pages [6] -->
Under our investigation, the existing solution for the merging after toll can be roughly divided into two types.

<!-- b000153 | prose | pages [6] -->
The ﬁrst solution is in short called “no solution”, which doesn’t give the drivers any instruction after toll and let them go at their own discretion. Then the second and more commonly used solution is to instruct the vehicles to merge at some pre-determined merging point.

<!-- b000154 | prose | pages [6] -->
For the ﬁrst solution, the eﬃciency of it is mainly based on the drivers’ own discretions, which can vary a lot among di↵erent people. And in the light traﬃc situations, this solution may be optimal, for the reason that drivers can go whatever path they what, and in other words their own eﬃciency is maximized. Meanwhile, with the light traﬃc assumption, there are little probability to crash. However, it will be fairly chaotic in heavy traﬃc, because it is very likely that driver’s own optimal path can cross each other. And then they will merge at any point so it is also hard to predict what drivers will do. Therefore, in heavy traﬃc, it is neither eﬃcient nor safe.

<!-- b000155 | prose | pages [6] -->
And the second solution provides a relatively orderly merging pattern. Vehicles merge at some certain merging points and at least the driving direction is predictable as long as the drivers are rational and always follow the instruction. However, some problems also occur at the merging point. As for most time, the number of tollbooths are larger than the number of lanes on the highway, there always exist the situation that vehicles from several di↵erent booths need to merge into one lane. So di↵erent vehicles from di↵erent booths can arrive at the merging point simultaneously, and then only one of them can get through at a time and others have to wait. This situation can be quite dangerous because drivers always want to go ﬁrst, and it also increase the deﬁciency.

<!-- b000156 | heading | pages [6] -->
4.2 Control Time Model (CTM)

<!-- b000157 | prose | pages [6] -->
Given aforementioned deﬁciencies of existing merging pattern, we propose a new model, partially based on the current one. Instead of having all the vehicles moving and merging at their own discretion, control time model will control the departure time of vehicles to ensure a smooth and safe emerging process.

<!-- b000158 | prose | pages [6] -->
Speciﬁcally, for situations where two booths merge into one lane, the second vehicle will only be allowed to proceed t0 seconds after the ﬁrst vehicle moves forward. The time t0 is deﬁned as the control time. Similarly, for situations where three booths merge into one lane, the third vehicle will be allowed to proceed t0 seconds after the second vehicle moves forward, whilst the second vehicle t0 seconds after the ﬁrst vehicle, as shown in Figure 1 and Figure 2.

<!-- b000159 | furniture | pages [7] -->
Team # 70545

<!-- b000160 | furniture | pages [7] -->
Page 6 of 25

<!-- b000161 | caption | pages [7] -->
Figure 1: Either A or B is open

<!-- b000162 | caption | pages [7] -->
Figure 2: Either C, D or E is open

<!-- b000163 | prose | pages [7] -->
In this way, the regulated merging of the vehicles into another lane would be more eﬃcient than the situation where vehicles are proceeding without regulation, for drivers should take time to make decision when multiple booths merge into one lane simultaneously, let alone the risk for doing so.

<!-- b000164 | prose | pages [7] -->
We model that vehicles start with constant acceleration as until reach the maximum speed vm in the straight path. They then immediately starts merging into their prescribed road in two consecutive tangent circle arcs.

<!-- b000165 | caption | pages [7] -->
Figure 3: Two or three tollbooth egress lanes merge into one lane

<!-- b000166 | prose | pages [7] -->
Now we evaluate the “appropriate” control time. When emergency happens, one vehicle take severe brake action with acceleration ab, after response time tres, the posterior vehicle take severe brake action with the same acceleration. Consider the distance of the two vehicles (t = 0 is the time when emergencies happen):

<!-- b000167 | prose | pages [7] -->
Z t Z t vposterior(t)dt − d = vmtres + vprevious(t)dt 0 0 where

<!-- b000168 | prose | pages [7] -->
8 t tres > vm, < tres < t tres + vm vm −ab(t −tres), vprevious = (1) ab > : tres + vm 0, ab < t

<!-- b000169 | prose | pages [7] -->
Solve the equation d ≥0, we get t0 ≥tres. By saying “appropriate” control time, we take t0 = 1s > tres = 0.8s (Lee et al, 2002).

<!-- b000170 | furniture | pages [8] -->
Team # 70545

<!-- b000171 | furniture | pages [8] -->
Page 7 of 25

<!-- b000172 | prose | pages [8] -->
After describing the control time model, we ﬁrst calculate the throughput of the toll plaza.

<!-- b000173 | prose | pages [8] -->
Let ik be the number of booths corresponding with the kth lane. For example, if the ﬁrst three booths merge into the ﬁrst lane, we say i1 = 3.

<!-- b000174 | prose | pages [8] -->
By computer simulation (details are included in Appendix), we have tik close to T ik when T ik << t0 (especially when the variance of service time is small), and tik increases as ik increases, and the increase speed is quite large when ik > T t0. where tik is the averaged time for a car to come into kth lane.

<!-- b000175 | prose | pages [8] -->
Therefore, to maximize the eﬃciency, we’ll keep ik as small as possible, whereas the throughput comes suboptimal if ik > T t0 for some k. The optimal throughput is closed to B T car(s) per second.

<!-- b000176 | prose | pages [8] -->
By substituting B by 8, the expectation of human service time T by 15. According to our optimization method above, when we keep the ik as small as possible, which is in other words, let them distributed evenly(e.g. {2,3,3}). We will get the optimal throughput closed to B T ⇡0.533 car per second. Then we calculate the size of the plaza, by doing so we discuss the value of D.

<!-- b000177 | prose | pages [8] -->
Deﬁne f : {1, 2, . . . , B} ! {1, 2, . . . , L} which is non-decreasing, and f(i) = j if and only if vehicles from ith booth merge into jth lane. It obviously follows that ik = kf −1({k})k. We call the mapping f a “merging pattern”.

<!-- b000178 | prose | pages [8] -->
dB dL Tollbooths

<!-- b000179 | prose | pages [8] -->
Direction of trafﬁc ﬂow

<!-- b000180 | prose | pages [8] -->
D

<!-- b000181 | caption | pages [8] -->
Figure 4: B = 8 tollbooth egress lanes merge into L = 3 lanes

<!-- b000182 | prose | pages [8] -->
By geometric relations, we have !2 ✓ ◆2 D −v2 r −(i −1 2)dB −(j −1 2)dL) m = r2 2a + 2 2

<!-- b000183 | prose | pages [8] -->
Observed from above relation, a certain (i, j) prescribes a lower bound of D, and for a certain merging pattern, the distance between the tollbooth and the end of the plaza that we eventually employ is the greatest lower bound of D. The less the greatest lower bound is, the smaller the size will be, and so will the cost of plaza.

<!-- b000184 | prose | pages [8, 9] -->
By property of quadratic function, for a certain j, the greater i is, the greater D is. We have ! j j X X ikdB −jdL ≥ dB −(k + 1)dL ik + 1 k=1 k=1 since dL > dB. That implies if j is changed into j + 1 whilst i is changed into i + 1, D will get smaller. Therefore, the global maximum must be obtained at one of the local maximum points, and then we let x be ( ) k=1 ik −1 2)dB −(j −1 (Pj 2)dL x = max 2 j2{1,2,...,L} And for given B and L, the optimal choice of merging pattern f would be the case if we can minimize x to be xmin = {ik}2{kf−1({k})k:8f} x min

<!-- b000185 | furniture | pages [9] -->
Team # 70545

<!-- b000186 | furniture | pages [9] -->
Page 8 of 25

<!-- b000188 | prose | pages [9] -->
After trying out some pairs of small (B, L), we induce that for any given small number B, L (which can be put in practical use) satisfying B > L, there exists a merging pattern fm such that x = (B −1 2)dB −(L −1 2)dL) := x0 2 Since for any ik we have the relation f(B) = L, which implies above expression will appear in every calculation of x for all ik, hence xmin ≥x0, hence the existence of x0 guarantees ”=”, providing us with the optimal merging pattern to minimize D.

<!-- b000189 | prose | pages [9] -->
By substituting B = 8, L = 3, dB = 2.5m, dL = 3.75m, r = 115m, vm = 15m/s, a = 2.78m/s2, the minimum of D is 105.5m, when (i1, i2, i3) 2 {(3, 3, 2), (3, 2, 3), (2, 3, 3)}.

<!-- b000190 | heading | pages [9] -->
4.3 Waiting Area Model(WAM)

<!-- b000191 | prose | pages [9] -->
After completing the above model, something seems to be deﬁcient also appears in our model. In the control time model, vehicles may need to wait at the booths even after the service ﬁnished, while there are a lot of vehicles queuing after it. So we wonder that whether it is better to build a waiting area at a plaza (as shown in Figure 5), so that the vehicles whose service has ﬁnished can go to the waiting area, then the consecutive vehicle can be serviced. So in this model, the sta↵spending more time serving instead of doing nothing while the vehicles are just waiting at the booths.

<!-- b000192 | prose | pages [9] -->
dB dL Waiting area Tollbooths

<!-- b000193 | prose | pages [9] -->
Direction of trafﬁc ﬂow

<!-- b000194 | prose | pages [9] -->
D

<!-- b000195 | caption | pages [9] -->
Figure 5: B = 8 tollbooth egress lanes merge into L = 3 lanes

<!-- b000196 | prose | pages [9] -->
We will test and compare this model with control time model in the following sections, to see whether it is eﬃcient or not.

<!-- b000197 | furniture | pages [10] -->
Team # 70545

<!-- b000198 | furniture | pages [10] -->
Page 9 of 25

<!-- b000199 | heading | pages [10] -->
5 Analysis and Results

<!-- b000200 | prose | pages [10] -->
In this section we will analyze throughput, accident prevention and cost of each models introduced in former section.

<!-- b000201 | heading | pages [10] -->
5.1 Throughput

<!-- b000202 | prose | pages [10] -->
Throughput (✓) here is deﬁned to be the number of vehicles per hour passing the point where the end of the plaza joins one of the the L outgoing traﬃc lanes. Here we discuss only one outgoing lane merged from two lanes in human-sta↵ed tollbooth area in heavy traﬃc where vehicles come continuously during heavy traﬃc so that the cashier work continually, as shown in Figure 6 .

<!-- b000203 | prose | pages [10] -->
dL Tollbooths

<!-- b000204 | prose | pages [10] -->
Direction of traffic flow

<!-- b000205 | prose | pages [10] -->
D

<!-- b000206 | caption | pages [10] -->
Figure 6: B = 8 tollbooth egress lanes merge intoL = 3 lanes in heavy traﬃc

<!-- b000207 | heading | pages [10] -->
5.1.1 Throughput of existing model

<!-- b000208 | prose | pages [10] -->
The toll collection service time is a random variable which can be seen as a sum of random variables including time needed by driver to search money or credit vehicled, time needed by cashier to take related record, etc. According to the central limit theorem, we can assume that the service time of ith vehicle (th,i) of the each lane follow normal distribution with µ = 15 and σ2 = 4 independently and identically.

<!-- b000209 | prose | pages [10] -->
Th,i ⇠N(15, 4) Suppose the ﬁrst vehicle coming into the tollbooth area at t = 0, then the time of the nth vehicles coming out from a lane tn should equal to the sum of the service time of itself and former vehicles. n X tn = Th,i i=1 As can be seen that tn is the sum of normally distributed random variables, thus

<!-- b000210 | prose | pages [10, 11] -->
tn ⇠N(15n, 4n) Besides we introduce a concept Post-Encroachment Time (PET) which is deﬁned to be the time lapse between end of encroachment of turning vehicle and the time that the through vehicle actually arrives at the potential point of collision (Gettman & Head, 2003). When PET is less than reaction time, rational drivers would decelerate in order to maintain a safety distance, corresponding to reaction time tr = 1s, with former vehicle. Consequently, more time is needed to pass the merging area which lower the eﬃciency and throughput. Denote PET of ith vehicle as PETi, then total delayed time Td is X (tr −PETi) Td = PETi<tr

<!-- b000211 | furniture | pages [11] -->
Team # 70545

<!-- b000212 | furniture | pages [11] -->
Page 10 of 25

<!-- b000214 | prose | pages [11] -->
Considering the total delayed time Td, the mean time needed of a vehicle coming out from merging area is t = tn + Td 2n Since there are two lanes working simultaneously and assume the motion in the merging area of each vehicle is the same, the throughput of the outgoing lane should be ✓= 3600 t After computer simulation with N = 1000 times, the results are shown in Figure. 7

<!-- b000215 | heading | pages [11] -->
5.1.2 Throughput of control time model

<!-- b000216 | prose | pages [11] -->
Now we consider the model with control time (t0). Suppose the nth vehicle coming out from lane a at ta,n with service time Ta,n the mth vehicle coming out from lane b at tb,m with service time Tb,m where Ta,n ⇠N(15, 4) Tb,m ⇠N(15, 4) and Assume the 1st vehicle comes to lane a at t = 0 and after ∆T the 2nd vehicles comes to lane b where ∆T ⇠U(0, 15). If we have ta,n + Ta,n+1 < tb,m + Tb,m+1 which means the (n+1)th vehicle in lane a completes toll collection service before the (m+1)th vehicle in lane b, then

<!-- b000217 | prose | pages [11] -->
ta,n+1 = max{ta,n + Ta,n+1, ta,n + t0, tb,m + t0} otherwise tb,m+1 = max{tb,m + Tb,m+1, ta,n + t0, tb,m + t0} Set max{ta,n, tb,m} < 3600 in order to simulate time period of one hour. Once if ta,n⇤> 3600 or tb,m⇤> 3600

<!-- b000218 | prose | pages [11] -->
we can obtain the throughput as ✓= n⇤+ m⇤−1 After computer simulation with N = 1000 times, the results are shown in Figure. x

<!-- b000219 | furniture | pages [12] -->
Team # 70545

<!-- b000220 | furniture | pages [12] -->
Page 11 of 25

<!-- b000221 | heading | pages [12] -->
5.1.3 Throughput of waiting area model

<!-- b000222 | prose | pages [12] -->
Denote tas,n as the time when nth vehicle completes toll collection and starts to wait in lane b, tbs,m as the time when mth vehicle completes toll collection and starts to wait in lane b. The iteration equations in former section can be adapted to the follows. If

<!-- b000223 | prose | pages [12] -->
tas,n + Ta,n+1 < tbs,m + Tb,m+1 which means the (n+1)th vehicle in lane a completes toll collection service before the (m+1)th vehicle in lane b, then

<!-- b000224 | prose | pages [12] -->
ta,n+1 = max{tas,n + Ta,n+1, ta,n + t0, tb,m + t0} otherwise tb,m+1 = max{tbs,m + Tb,m+1, ta,n + t0, tb,m + t0} Set max{ta,n, tb,m} < 3600 in order to simulate time period of one hour. Once if ta,n⇤> 3600 or tb,m⇤> 3600

<!-- b000225 | prose | pages [12] -->
we can obtain the throughput as ✓= n⇤+ m⇤−1 After computer simulation with N = 1000 times, the results are shown in Figure 7

<!-- b000226 | heading | pages [12] -->
5.1.4 Comparison and hypothesis tests of throughputs

<!-- b000227 | prose | pages [12] -->
500

<!-- b000228 | prose | pages [12] -->
490 Throughput veh/(h·lane) 480

<!-- b000229 | prose | pages [12] -->
470

<!-- b000230 | prose | pages [12] -->
460

<!-- b000231 | prose | pages [12] -->
450

<!-- b000232 | prose | pages [12, 13] -->
Existing Model Control Time Model Waiting Area Model It can be seen from Figure 7 that the throughputs di↵er slightly among models. Therefore, we conduct hypothesis test for means at 5% level of signiﬁcance.

<!-- b000233 | caption | pages [12] -->
Figure 7: Comparison of throughput of models

<!-- b000234 | furniture | pages [13] -->
Team # 70545

<!-- b000235 | furniture | pages [13] -->
Page 12 of 25

<!-- b000237 | prose | pages [13] -->
H0 :There is no di↵erence in average throughputs in existing modeland control time model, i.e. µ1 = µ2 H1 :H0 is wrong, i.e.µ1 6= µ2

<!-- b000238 | caption | pages [13] -->
Table 1: Statistics of two models

<!-- b000239 | prose | pages [13] -->
Model Size Mean S.d. SEM Existing Model 1000 477.830 4.054 0.128 Control Time Model 1000 477.422 5.843 0.185 Waiting Area Model 1000 479.081 6.039 0.191

<!-- b000240 | prose | pages [13] -->
di↵erence in means = 477.830 −477.422 = 0.408 p 0.1282 + 0.1852 = 0.225 overall standard error = test statistic = 0.408 0.225 = 1.813 p-value = 0.0348 > 0.025

<!-- b000241 | prose | pages [13] -->
Therefore, H0 is not rejected at 5% level of signiﬁcance. We conclude that there is no signiﬁcant di↵erence of means of throughputs in existing model and control time model.

<!-- b000242 | prose | pages [13] -->
However, by similar method, when we make hypothesis test for means of the later two models, the conclusion is that there is signiﬁcant di↵erence of means of throughputs in existing model and control time model.

<!-- b000243 | prose | pages [13] -->
The analysis of throughputs above lead to the following results:

<!-- b000244 | prose | pages [13] -->
• Control time mechanism would not lower the eﬃciency and throughput. It just transfer delayed time Td in merging area under existing model to control time t0 in tollbooth area under control time model, as shown in

<!-- b000245 | prose | pages [13] -->
• Control time mechanism can improve the orderliness of the pattern of vehicles coming out from tollbooth into merging area which thereby improves the safety level of the merging pattern, to be discussed in section 5.2.

<!-- b000246 | prose | pages [13] -->
• Even though waiting area design could improve throughput, the increment 1.6veh/h is slight compared to the magnitude of throughput. Besides, the cost of land as well as other expense with regard to waiting area can be relatively high. Therefore, the disad- vantageous of waiting area outweigh the beneﬁt it brings so that we should disvehicled this model.

<!-- b000247 | furniture | pages [14] -->
Team # 70545

<!-- b000248 | furniture | pages [14] -->
Page 13 of 25

<!-- b000249 | prose | pages [14] -->
200

<!-- b000250 | prose | pages [14] -->
Model count Control Time Model Existing Model 100

<!-- b000251 | prose | pages [14] -->
0 0 5 10 15 20 25 PET

<!-- b000252 | caption | pages [14] -->
Figure 8: PET of existing model and PET of control time model

<!-- b000253 | heading | pages [14] -->
5.2 Accident prevention

<!-- b000254 | prose | pages [14] -->
This section will analyze accident rate in merging area in terms of PET. When PET is small, it becomes diﬃcult for drivers to make decision promptly to avoid collision, and thus accident is more likely to happen. Therefore, we introduce following function to associate the probability of accident with PET.

<!-- b000255 | prose | pages [14] -->
p = e−PET (2) 100

<!-- b000256 | prose | pages [14] -->
When PET = 0, two vehicles arrive the potential point of collision theoretically while drivers could manage speed along the way in order to avoid collision, and hence the probability of collision under this circumstance can be set 0.01. After computer simulation based on the iteration equations with N = 4000 times, the PET of existing model and PET of control time model are shown in Figure 8.

<!-- b000257 | prose | pages [14] -->
It can be seen that under existing model, a signiﬁcant part of PET lies in the interval [0, 1] where accident is more likely to happen. While under control time model, due to the control mechanism, the minimum PET is control time t0 = 1s which guarantee low accident risk. The expectations of accident rate by simulation on function are shown in Table 2 The control time model can reduce the accident rate by 13.66%. What’s more, the low rate of accident would make vehicles pass merging area without hindrance, which improve eﬃciency and throughput. Therefore, The control time model has better performance in accident prevention than existing model.

<!-- b000258 | furniture | pages [15] -->
Team # 70545

<!-- b000259 | furniture | pages [15] -->
Page 14 of 25

<!-- b000260 | caption | pages [15] -->
Table 2: Accident rate of each model

<!-- b000261 | prose | pages [15] -->
Model Accident per 100,000 vehicles Existing Model 53.024 Control Time Model 61.416

<!-- b000262 | heading | pages [15] -->
5.3 Cost

<!-- b000263 | prose | pages [15] -->
This section analyzes cost of merging area and tollbooth area, including ﬁxed cost and variable cost per year, i.e. annual operation cost. Fixed cost mainly depends on cost of land and tollbooth construction. We can estimate area of land (A) by supposing the marginal curve of the out-most lane is symmetric, as shown in Figure 9

<!-- b000264 | prose | pages [15] -->
dL

<!-- b000265 | prose | pages [15] -->
Tollbooths

<!-- b000266 | prose | pages [15] -->
Direction of trafﬁc ﬂow D

<!-- b000267 | caption | pages [15] -->
Figure 9: Estimation of A by symmetry of shaded area

<!-- b000268 | prose | pages [15] -->
Tollbooth construction cost can be divided to three kinds including human-sta↵ed, elec- tronic and automated tollbooths.

<!-- b000269 | prose | pages [15] -->
Fixed cost = 1 2c1A + (chph + cepe + capa)B where A = v2 a Bdb + (Bdb + Ldl)(D −v2 m m 2a ) cl = construction cost of land per m2 ch = construction cost per automated tollbooth ce = construction cost per electronic tollbooth ca = construction cost per human-sta↵ed tollbooth

<!-- b000270 | prose | pages [15] -->
Substitute B = 8, L = 3, dB = 2.5, dL = 3.75, cl = 172.83, ch = 58500, ce = 15400, ca = 58000 (Pietrzyk,1992), ph = 4/8, pe = 1/8, pa = 3/8 and get ﬁxed cost = $739, 320. Simi- larly, annual operation cost of tollbooth area can be estimated by

<!-- b000271 | prose | pages [15, 16] -->
Annual operation cost = (c0 2 + c0 hph + c0 epe)B c0 a = operation cost of tollbooth construction and operation per year c0 h = operation cost of salary per cashier c0 e = operation cost of each electronic device Substitute c0 h = 141900, c0 e = 4200, c0 a = 43300 (Pietrzyk,1992), ph = 4/8, pe = 1/8, pa = 3/8 and get annual operation cost = $701, 700.

<!-- b000272 | furniture | pages [16] -->
Team # 70545

<!-- b000273 | furniture | pages [16] -->
Page 15 of 25

<!-- b000275 | heading | pages [16] -->
6 Possible Modiﬁcation

<!-- b000276 | prose | pages [16] -->
As required in the problem, our report will then proceed to analyze the inﬂuences of some deviation of the conditions on our model. Some possible modiﬁcations may be made to improve the utility of our model in those situations.

<!-- b000277 | heading | pages [16] -->
6.1 Mixture of autonomous vehicles and human-driving vehicles

<!-- b000278 | prose | pages [16] -->
With the improvements in artiﬁcial intelligence and vehicle industry recent years, autonomous vehicles have become much more reliable and popular. However, some dangerous occasions may occur as the auto-driving system is not completely stable for all time. Therefore, even in some countries people are allowed to take the autonomous vehicle to the street, there are always required to be a driving sitting on the driver’s seat and prepared to take over at any time.

<!-- b000279 | prose | pages [16] -->
If autonomous vehicles are allowed on the street, the situation of merging may become much more complicated. Firstly, sometimes the autonomous vehicles fail to detect the mark- ing on the road and therefore go a wrong lane (Sam, 2016). It will be very dangerous if the autonomous vehicle went wrong when merging. Because there are a lot of complicated lanes at the merging area, and some may even cross each other, which are diﬃcult for an autonomous vehicle to recognize and are hard to determine the turning angle accurately.

<!-- b000280 | prose | pages [16] -->
And one possible solution is to instruct the autonomous vehicles to go to the most left lane. Reason to constraint them to this lane is that the vehicles go through it will just need to go straight till the very end of merging area, which is also the optimal path that the computer will generate even that it fails to detect the signal on the road.

<!-- b000281 | heading | pages [16] -->
6.2 Change in proportion of di↵erent types of tollbooths

<!-- b000282 | prose | pages [16] -->
Nowadays, there are roughly 3 di↵erent types of tollbooths, they are conventional (human- sta↵ed), automated and electronic toll collection booths. The main di↵erence among these three di↵erent types is that they have di↵erent service times. The conventional booths have the longest service time, which is around 15 seconds in our assumption. And the automated ones have the second longest service time, and we assume it to be around 8 seconds. Meanwhile, vehicles equipped with ETC transponder are able to pass the ETC booths even without stop (with a maximal passing speed of 15mph).

<!-- b000283 | prose | pages [16, 17] -->
The model we introduced before works out quite good for both conventional and auto- mated booths as explained before. However, it may not work well with ETC since they don’t need to stop at the booth. First of all, one thing that we would like to classify is that the proportion of ETC booths will be at either a minority or majority position. It is because that the estimated capacity of a single ETC booth is 2000/h, and this number is much larger than the need now considering the proportion of the drivers who possess a ETC transponder. So if the ETC booths are to be included in a toll plaza, we will place it at the most left lane, as we only need one to satisfy all demands for it. And we will arrange the other booths and lanes with the algorithm we introduced before. Of course, if the users of ETC are going to increase signiﬁcantly in the future, the proportion of ETC booths can also be increased. However, one thing to be noticed is that always one booth merges to one lane on highway, provided that the eﬃciency of ETC booths are high and we do not need to increase the number of booths, which will only make it riskier when merging.

<!-- b000284 | furniture | pages [17] -->
Team # 70545

<!-- b000285 | furniture | pages [17] -->
Page 16 of 25

<!-- b000287 | heading | pages [17] -->
7 Sensitivity test

<!-- b000288 | prose | pages [17] -->
This section conducts sensitivity tests of throughput and cost. We deﬁne the sensitivity of dA a function A(X) in terms of X to be X . If A is a discrete function, we change dA into A dX ∆A = A(X + 1) −A(X).

<!-- b000289 | heading | pages [17] -->
7.1 Sensitivity test of throughput

<!-- b000290 | prose | pages [17] -->
-2.0 0.10 Sensitivity of throughput Sensitivity of throughput -1.0 0.00

<!-- b000291 | prose | pages [17] -->
0.0 -0.10 0 1 2 3 4 0 1 2 3 4 Mean of service time Standard deviation of service time

<!-- b000292 | caption | pages [17] -->
Figure 10: Sensitivity of throughput in terms of mean and standard deviation of service time.

<!-- b000293 | prose | pages [17] -->
As shown in 10, the sensitivity of throughput in terms of mean of service time T is a constant −1. Recall that in section 4.2, the optimal throughput is ✓= B T The inverse ratio relationship of ✓and T implies unit constant sensitivity of ✓with respect to T, which is consistent with sensitivity test result. Besides, due to the law of large number, the volatility of service time ﬁnally performs slight e↵ects on throughput and thus the sensitivity is zero.

<!-- b000294 | furniture | pages [18] -->
Team # 70545

<!-- b000295 | furniture | pages [18] -->
Page 17 of 25

<!-- b000296 | heading | pages [18] -->
7.2 Sensitivity test of ﬁxed cost

<!-- b000297 | prose | pages [18] -->
By our assumption stated in Section 4.2 that the greatest lower bound is provided by the most outside lane and booth, combined with the formula to calculate the ﬁxed cost, we get

<!-- b000298 | prose | pages [18] -->
Fixed cost = 1 2c1A + (chph + cepe + capa)B

<!-- b000299 | prose | pages [18] -->
The initial value of

<!-- b000300 | prose | pages [18] -->
(vm, a, B, L, dB, dL, pa, pe, ph, cl, ce, ch, ca) =(15, 2.78, 8, 3, 2.5, 3.75, 3/8, 1/8, 4/8, 172.84, 15400, 58500, 58000)

<!-- b000301 | prose | pages [18] -->
We calculate the sensitivity of the ﬁxed cost with respect to the number of booths B, we get the graph as following And it shows that the the sensitivity of B around 8 is about 1.15 and

<!-- b000302 | prose | pages [18] -->
Sensitivity of Fixed Cost Sensitivity of Fixed Cost Sensitivity of Fixed Cost 0.20 0.7 1.4 0.6 1.3 0.5 0.15 0.4 1.2 0.3 0.10 0.2 1.1 0.1 r v B 100 150 200 250 300 6 8 10 12 14 16 18 20 3 5 6 7 8 9 10

<!-- b000303 | caption | pages [18] -->
Figure 11: Sensitivity of ﬁxed cost in terms of vm, r and B

<!-- b000304 | prose | pages [18] -->
always above 1, and the decreasing speed is very low, which means that D is always sensitive in terms of B. So increasing B can have signiﬁcant inﬂuence on D, and we may need to evaluate more whether to build more booths considering the balance of cost and eﬃciency.

<!-- b000305 | prose | pages [18] -->
Similarly, we can calculate the sensitivity of ﬁxed cost with respect to vm and r(as shown in the Figure 11).

<!-- b000306 | prose | pages [18] -->
The sensitivity of vm around 0.38, and it remains below 1 as it vary from 10m/s to 20m/s, which shows that the cost is not sensitive to the speed limit. So our cost estimation should be roughly correct with slight deviation with vm. Finally, with similar analysis, sensitivity in terms of r is always around 0.1 and 0.2 from 50m to 200m. So the radius only have little inﬂuence on our ﬁnal result.

<!-- b000307 | heading | pages [18] -->
8 Conclusion

<!-- b000308 | prose | pages [18] -->
In Section 4 we describe three models, namely existing models, CTM, WAM. By simulation in Section 5, we discard WAM and point out the deﬁciencies of EM model and employ CTM. Therefore, the following conclusion is based on CTM.

<!-- b000309 | prose | pages [18, 19] -->
The shape of the plaza should enable cars from every booth to merge into its prescribed lane with two consecutive arcs. By the assumption stated in Section 4.2, the shape of the plaza is determined by the most outside booth merging into the most outside lane. The boundary should make sure that the most outside vehicles have suﬃcient space on its right side. Take the example of B = 8, L = 3, the shape and merging pattern are as follows.

<!-- b000310 | furniture | pages [19] -->
Team # 70545

<!-- b000311 | furniture | pages [19] -->
Page 18 of 25

<!-- b000313 | prose | pages [19] -->
dB dL Tollbooths

<!-- b000314 | prose | pages [19] -->
Direction of trafﬁc ﬂow

<!-- b000315 | prose | pages [19] -->
D

<!-- b000316 | caption | pages [19] -->
Figure 12: Shape and merging pattern of merging area

<!-- b000317 | prose | pages [19] -->
Note that in no case will cars from di↵erent booths merge into one lane simultaneously as is stated in our control time model, so it does not matter whether the distance between two adjacent trajectories merging into one lane becomes smaller or not. Additionally, leading lines should be drawn on the ground to ensure that vehicles take intended paths.

<!-- b000318 | prose | pages [19] -->
The size of merging area is given by formula A = v2 a Bdb + (Bdb + Ldl)(D −v2 m m 2a ) for one direction. This includes the acceleration paths (the left term) and merging (turning) paths (the right term). Multiply it by a factor 2 if we are to calculate for two directions. For the above example B = 8, L = 3, the area for one direction is 1824.93m2 In heavy traﬃc (deﬁned as the situation where there is at least one car at every service booths), the throughput of plaza is approximately 3600B/T vehicles per hour (if all the toll- booths are human-sta↵ed) , computed by induction of computer simulation. By substituting B = 8, Th = 15, we get 1920 vehicles per hour from human-sta↵ed lanes. In light traﬃc, the throughput is less than 3600B/T. Overall, there is no statistical signiﬁcant of di↵erence between throughput of CTM and existing model. This comparison does not include the con- sideration of accident. If we take into account the fact that CTM reduces the accident rate by 13.66% and that accident is likely to cause traﬃc jam and reduce toll plaza’s throughput, the superiority of CTM would be more distinct. The cost of construction (ﬁxed cost) and operation (variable cost) of the merging area and tollbooth area are calculated respectively. The ﬁxed cost is given by the formula Fixed cost = 1 2c1A + (chph + cepe + capa)B the denotation is given in Section 5.3. In the B=8, L=3 example, the ﬁxed cost is $739320. The annual cost is given by similar formula Annual operation cost = (c0 2 + c0 hph + c0 epe)B

<!-- b000319 | prose | pages [19] -->
which, in our example, turns to be $701, 700 per year.

<!-- b000320 | furniture | pages [20] -->
Team # 70545

<!-- b000321 | furniture | pages [20] -->
Page 19 of 25

<!-- b000322 | heading | pages [20] -->
9 Strengths and Weaknesses

<!-- b000323 | heading | pages [20] -->
9.1 Strengths

<!-- b000324 | prose | pages [20] -->
By computer simulation, as the expression of throughput ✓only contains the number of booths B and service time T, the employment of regulation in control time model does not reduce the throughput of the plaza (control time t0 is not in the expression). However, the risk of accident decreases to a great extent, which ensures a safe and smooth ﬂow of vehicles.

<!-- b000325 | prose | pages [20] -->
Moreover, we consider service time T following normal distribution instead of assuming a constant, which can better approximate real situation. Additionally, the control time mech- anism could decrease the size of merging area compared with existing model where vehicles merge at their discretion. Last but not least, we use multiple programming platforms to run computer simulations (Mathematica, MATLAB and R), which provides us with accurate and convincing data to support our models.

<!-- b000326 | heading | pages [20] -->
9.2 Weaknesses

<!-- b000327 | prose | pages [20] -->
We assume the vehicles adopt two tangent uniform circular motion to merge into its pre- scribed lane, which may not be the real trajectory of vehicles. However, we can draw some leading lines on the ground to guide vehicles. Additionally, we do not consider the situation where vehicles break down and block certain booths and/or lanes.

<!-- b000328 | prose | pages [20] -->
The arrival of vehicles should follow Poisson distribution, but as we did not have the real- world data to estimate λ, we instead assume that the di↵erence of two consecutive vehicles’ arrival follows a uniform distribution, which may lead to some inaccuracies. This problem, together with the diﬃculties to determine the expectation and variance of service time T, could be addressed if data collected in real-world situation could be provided.

<!-- b000329 | heading | pages [21] -->
References

<!-- b000330 | references | pages [21] -->
[1] Abdel-Aty, M. A., & Radwan, A. E. (2000). Modeling traﬃc accident occurrence and

<!-- b000331 | references | pages [21] -->
involvement. Accident Analysis & Prevention, 32(5), 633-642.

<!-- b000332 | references | pages [21] -->
[2] Corwin, I., Ganatra, S., & Rozenblyum, N. (2005). A Single-vehicle Interaction Model

<!-- b000333 | references | pages [21] -->
of Traﬃc for a Highway Toll Plaza. The UMAP Journal, 26(223), 299-315.

<!-- b000334 | references | pages [21] -->
[3] Friedman, D. A., & Waldfogel, J. (1995). The administrative and compliance cost of

<!-- b000335 | references | pages [21] -->
manual highway toll collection: evidence from Massachusetts and New Jersey. National

<!-- b000336 | references | pages [21] -->
Tax Journal, 217-228.

<!-- b000337 | references | pages [21] -->
[4] Gettman, D., & Head, L. (2003). Surrogate safety measures from traﬃc simulation mod-

<!-- b000338 | references | pages [21] -->
els. Transportation Research Record: Journal of the Transportation Research Board,

<!-- b000339 | references | pages [21] -->
(1840), 104-115.)

<!-- b000340 | references | pages [21] -->
[5] Gurney, J. K. (2013). Sue my vehicle not me: Products liability and accidents involving

<!-- b000341 | references | pages [21] -->
autonomous vehicles.

<!-- b000342 | references | pages [21] -->
[6] Harchol-Balter, M., Osogami, T., Scheller-Wolf, A., & Wierman, A. (2005). Multi-server

<!-- b000343 | references | pages [21] -->
queueing systems with multiple priority classes. Queueing Systems, 51(3-4), 331-360.

<!-- b000344 | references | pages [21] -->
[7] Lai, S. F. (2011). The Accident Risk Measuring Model for Urban Arterials. In 3rd

<!-- b000345 | references | pages [21] -->
International Conference on Road Safety and Simulation, Indianapolis, USA, September

<!-- b000346 | references | pages [21] -->
(pp. 14-16).

<!-- b000347 | references | pages [21] -->
[8] Lee, J. D., McGehee, D. V., Brown, T. L., & Reyes, M. L. (2002). Collision warning

<!-- b000348 | references | pages [21] -->
timing, driver distraction, and driver response to imminent rear-end collisions in a high-

<!-- b000349 | references | pages [21] -->
ﬁdelity driving simulator. Human Factors, 44(2), 314.

<!-- b000350 | references | pages [21] -->
[9] Oliver, N., & Pentland, A. P. (2000). Graphical models for driver behavior recognition

<!-- b000351 | references | pages [21] -->
in a smartvehicle. In Intelligent Vehicles Symposium, 2000. IV 2000. Proceedings of the

<!-- b000352 | references | pages [21] -->
IEEE (pp. 7-12). IEEE.

<!-- b000353 | references | pages [21] -->
[10] Pietrzyk, M. C. (1992). COST-EFFECTIVENESS ANALYSIS OF AVI/ETTM FOR

<!-- b000354 | references | pages [21] -->
FLORIDA’S TURNPIKE SYSTEM (No. WPI 0510406,).

<!-- b000355 | references | pages [21] -->
[11] Song, L. X. (2008). Application and mathematic model of queueing theory in freeway

<!-- b000356 | references | pages [21] -->
toll system. Science &Technology Information, 29, 391.

<!-- b000357 | references | pages [21] -->
[12] Spann, A., Kane, D., & Gulotta, D. (2005). Lane Changes and Close Following: Trou-

<!-- b000358 | references | pages [21] -->
blesome Tollbooth Traﬃc. UMAPJournal, 317.

<!-- b000359 | references | pages [21] -->
[13] Spiliopoulou, A. D., Papamichail, I., & Papageorgiou, M. (2009). Toll plaza merging traf-

<!-- b000360 | references | pages [21] -->
ﬁc control for throughput maximization. Journal of Transportation Engineering, 136(1),

<!-- b000361 | references | pages [21] -->
67-76.

<!-- b000362 | references | pages [22] -->
[14] Zhang, Z. (2014). Research on traﬃc conﬂict of freeway diverging and merging sections

<!-- b000363 | references | pages [22] -->
and toll booth.

<!-- b000364 | references | pages [22] -->
[15] ZHENG, Y. L., ZHAI, R. P., & MA, S. Q. (2006). Survey of Cellular Automata Model

<!-- b000365 | references | pages [22] -->
of Traﬃc Flow. Journal of Highway and Transportation Research and Development, 1,

<!-- b000366 | references | pages [22] -->
027.

<!-- b000367 | heading | pages [23] -->
Appendix

<!-- b000368 | prose | pages [23] -->
Some useful codes in R

<!-- b000369 | heading | pages [23] -->
1. Eﬃciency simulations

<!-- b000370 | heading | pages [23] -->
1.1 Eﬃciency simulation of existing model

<!-- b000371 | prose | pages [23] -->
x=numeric(1000) y=numeric(1000) mean.ex=numeric(1000) PET.ex=numeric(1999) for (j in 1:1000) { t1=rnorm(1000,15,4) t2=rnorm(1000,15,4) for (i in 1:1000) { x[i]=sum(t1[1:i]) y[i]=sum(t2[1:i]) time.x.y=sort(c(x,y)) } k=1:1999 PET.ex[k]=time.x.y[k+1]-time.x.y[k] T.dl=sum(1-PET.ex[PET.ex¡1]) T.dl mean.ex[j]=(x[1000]+T.dl)/2000 } Th.ex=3600/mean.ex Th.ex mean(Th.ex)

<!-- b000372 | heading | pages [23] -->
1.2 Eﬃciency simulation of CTM

<!-- b000373 | prose | pages [23, 24] -->
k=1 stat.2=matrix(0,2,1000) m=1:1000 for (m in 1:1000) { i=0 j=0 x=0 y=runif(1,0,15) T1=rnorm(1000,15,2) T2=rnorm(1000,15,2) while (max(x,y)¡=3600) { if (x+T1[i+1]¡y+T2[j+1]) { x=max(x+T1[i+1],x+k,y+k) i=i+1 } else { y=max(y+T2[j+1],x+k,y+k) j=j+1 } } stat.2[1,m]=i stat.2[2,m]=j } stat.2 Th.ct=stat.2[1,]+stat.2[2,]-1 Th.ct mean(Th.ct)

<!-- b000375 | heading | pages [24] -->
1.3 Eﬃciency simulation of WAM

<!-- b000376 | prose | pages [24, 25] -->
k=1 stat.3=matrix(0,2,1000) m=1:1000 for (m in 1:1000) { i=0 j=0 x=0 y=runif(1,0,) X=0 Y=0 T1=rnorm(1000,15,2) T2=rnorm(1000,15,2) while (max(X,Y)¡=3600) { if (x+T1[i+1]¡y+T2[j+1]) { X=max(x+T1[i+1],X+k,Y+k) x=x+T1[i+1] i=i+1 } else { Y=max(y+T2[j+1],X+k,Y+k) y=y+T2[j+1] j=j+1 } } stat.3[1,m]=i stat.3[2,m]=j } stat.3 Th.wa=stat.3[1,]+stat.3[2,]-1 Th.wa mean(Th.wa)

<!-- b000378 | heading | pages [25] -->
2 Risk evaluation by simulations

<!-- b000379 | heading | pages [25] -->
2.1 Simulation of existing model

<!-- b000380 | prose | pages [25] -->
x=numeric(1000) y=numeric(1000) mean.ex=numeric(1000) PET.ex=numeric(1999) t1=rnorm(1000,15,2) t2=rnorm(1000,15,2) for (i in 1:1000) { x[i]=sum(t1[1:i]) y[i]=sum(t2[1:i]) time.x.y=sort(c(x,y)) } k=1:1999 PET.ex[k]=time.x.y[k+1]-time.x.y[k] PET.ex

<!-- b000381 | heading | pages [25] -->
2.2 Simulation of CTM

<!-- b000382 | prose | pages [25, 26] -->
k=1 i=0 j=0 x=0 y=runif(1,0,15) T1=rnorm(1100,15,2) T2=rnorm(1100,15,2) X=numeric(1100) Y=numeric(1100) while (i+j¡2000) { if (x+T1[i+1]¡y+T2[j+1]) { x=max(x+T1[i+1],x+k,y+k) i=i+1 } else { y=max(y+T2[j+1],x+k,y+k) j=j+1 } X[i]=x Y[j]=y } i j X=X[which(X¿0)] Y=Y[which(Y¿0)] time.x.y=sort(c(X,Y)) PET.ct=numeric(i+j-1) n=1:(i+j-1) PET.ct[n]=time.x.y[n+1]-time.x.y[n] PET.ct
