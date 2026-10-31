# P-B-2017-70545-8e86fcfa

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
70545

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
B

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | title | pages [1] -->
Control Time Model: Wait One Second and Start Your

<!-- b000018 | title | pages [1] -->
Journey

<!-- b000019 | heading | pages [1] -->
Summary

<!-- b000020 | prose | pages [1] -->
People around the world are complaining about the trafﬁc jams every day. Some people may spend more than 3 hours on their way from ofﬁce to home everyday on their cars, which makes them frustrated. And our problem is to investigate the methods to optimize the design of toll plazas on highways, especially the area after merging, which is also a possible location where vehicles can be stuck in.

<!-- b000021 | prose | pages [1] -->
Before establishment of our models, we list some assumptions to make the real life scenario easier to model.

<!-- b000022 | prose | pages [1] -->
And then we start to analyze the existing models, from which we conclude their strengths and weaknesses. By investigating their characteristics, we get the inspiration to form our two new models: Control Time Model (CTM) and Waiting Area Model(WAM). In these two new models, we introduced a way of conducting control of the departure time of the vehicles at the tollbooths. This kind of control is basically preventing the vehi- cles which are merging in the same lane from leaving the booths simultaneously, which may be a hidden danger for trafﬁc accident or leads to a trafﬁc jam. And we?ll continue to calculate the size and shape of the merging area according to our control methods and some assumptions. After that, we introduce a method for ﬁnding the optimal merging pattern based on both mathematical proof and computer simulations.

<!-- b000023 | prose | pages [1] -->
After that, we run some simulations to ﬁnd out the throughput, risk and cost of dif- ferent models, which are based on some statistical laws for real life situations. Then we compare these three models in all factors with the help of statistical hypothesis testing, and conclude that the CTM is the best in general. The next section is about some slight modiﬁcation under different conditions such as including the self-driving car, and the different arrangements in terms of merging patterns when the proportion of different types of tollbooths vary.

<!-- b000024 | prose | pages [1] -->
For the following section, we test our model by investigating the sensitivity of con- struction cost and throughput (per hour) in terms of some variables included in our model, in order to justify the reliability of our model from different perspectives.

<!-- b000025 | prose | pages [1] -->
Finally, we end our report by the conclusion part followed by strengths and weak- nesses analysis.

<!-- b000026 | furniture | pages [2] -->
Team # 70545

<!-- b000027 | furniture | pages [2] -->
Page 1 of 25

<!-- b000028 | prose | pages [2] -->
PO Box 5042, Woodbridge, NJ 07095-5042.

<!-- b000029 | prose | pages [2] -->
Dear New Jersey Turnpike Authority,

<!-- b000030 | prose | pages [2] -->
We are a group of students having conducted a project focusing on solving the problem of merging after tollbooths. And we are sending this letter to let you know the problems that may exist in current toll plaza and suggesting some possible ways to improve it.

<!-- b000031 | prose | pages [2] -->
First of all, by analyzing the design of existing toll plazas on the highways, we ﬁnd out the following weaknesses of them. At most toll plazas, the vehicles go disorderedly after toll for following reasons. For some toll plazas, there are no leading lines after toll, so drivers just go at their own discretion, thus their routes become unpredictable. And even there are some orientation lines, if two vehicles arrive at the merging point at the same time, only one of them can go through at one time and it will also cause some problems. Disorder after toll leads to both harm to the eﬃciency of the highway entrance and more risk for traﬃc accidents.

<!-- b000032 | prose | pages [2] -->
Therefore, to solve the above problem, we introduced a new model called “Control Time Model” (CTM). In our model, the releases of cars are controlled at the booth, ensuring that the time interval from any two releases of cars are more that the “safe time”. Therefore, the merging becomes more orderly and safer.

<!-- b000033 | prose | pages [2] -->
We run some simulations with our models to test and compare the eﬃciency between the CTM and current existing models. The result is that, the eﬃciency of CTM is only slightly smaller than existing model (about 0.6 throughput less per lane per hour), but we haven’t considered the time wasted when accidents happen, which is a lot more likely to take place in existing models theoretically.

<!-- b000034 | prose | pages [2] -->
And also according to the simulation, the risk of car crashes is also limited to a lower level, which is 13.66% less than current existing models.

<!-- b000035 | prose | pages [2] -->
In terms of expenditure of construction and maintenance, as our model is much more orderly, the total length of the merging area can be reduced.

<!-- b000036 | prose | pages [2] -->
Therefore, a decrease in the total expense is expected, let alone the fact that maintenance of plaza could be a lot easier if accident rate decreases distinctively.

<!-- b000037 | prose | pages [2] -->
All in all, our conclusion is that the CTM performs better than existing models in all aspects including but not limited to eﬃciency, risk elimination as well as total cost. Therefore, it is worthwhile to consider the future construction with our model design.

<!-- b000038 | prose | pages [2] -->
Thank you for considering our model and wish you a bright future.

<!-- b000039 | prose | pages [2] -->
Sincerely,

<!-- b000040 | furniture | pages [2] -->
Team#70545

<!-- b000041 | prose | pages [2] -->
MCM2017

<!-- b000042 | furniture | pages [3] -->
Team # 70545

<!-- b000043 | furniture | pages [3] -->
Page 2 of 25

<!-- b000044 | heading | pages [3] -->
Control Time Model: Wait One Second and Start Your

<!-- b000045 | prose | pages [3] -->
Journey

<!-- b000046 | heading | pages [3] -->
Contents

<!-- b000047 | contents | pages [3] -->
1

<!-- b000048 | heading | pages [3] -->
Introduction

<!-- b000049 | prose | pages [3] -->
3 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Restatement of the problem . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Literature review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000050 | prose | pages [3] -->
2

<!-- b000051 | heading | pages [3] -->
Assumptions

<!-- b000052 | prose | pages [3] -->
3

<!-- b000053 | heading | pages [3] -->
Notations

<!-- b000054 | prose | pages [3] -->
4

<!-- b000055 | heading | pages [3] -->
Models

<!-- b000056 | prose | pages [3] -->
3

<!-- b000057 | prose | pages [3] -->
3

<!-- b000058 | prose | pages [3] -->
4

<!-- b000059 | prose | pages [3] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Existing Model(EM) 5 Control Time Model (CTM) . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 5 Waiting Area Model(WAM) . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3

<!-- b000060 | prose | pages [3] -->
5

<!-- b000061 | heading | pages [3] -->
Analysis and Results

<!-- b000062 | prose | pages [3] -->
8

<!-- b000063 | prose | pages [3] -->
9 Throughput . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 9 Throughput of existing model . . . . . . . . . . . . . . . . . . . . . . 5.1.1 9 Throughput of control time model 5.1.2 . . . . . . . . . . . . . . . . . . .

<!-- b000064 | prose | pages [3] -->
10 Throughput of waiting area model 5.1.3 . . . . . . . . . . . . . . . . . . .

<!-- b000065 | prose | pages [3] -->
11 Comparison and hypothesis tests of throughputs . . . . . . . . . . . . 5.1.4 11 Accident prevention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 13 Cost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000066 | prose | pages [3] -->
6 Possible Modiﬁcation

<!-- b000067 | prose | pages [3] -->
14

<!-- b000068 | prose | pages [3] -->
15 Mixture of autonomous vehicles and human-driving vehicles 6.1 . . . . . . . . .

<!-- b000069 | prose | pages [3] -->
15 Change in proportion of di↵erent types of tollbooths 6.2

<!-- b000070 | prose | pages [3] -->
7

<!-- b000071 | heading | pages [3] -->
Sensitivity test

<!-- b000072 | prose | pages [3] -->
. . . . . . . . . . . . .

<!-- b000073 | prose | pages [3] -->
15

<!-- b000074 | prose | pages [3] -->
16 . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 Sensitivity test of throughput 16 . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Sensitivity test of ﬁxed cost

<!-- b000075 | prose | pages [3] -->
8

<!-- b000076 | heading | pages [3] -->
Conclusion

<!-- b000077 | prose | pages [3] -->
9

<!-- b000078 | heading | pages [3] -->
Strengths and Weaknesses

<!-- b000079 | prose | pages [3] -->
17

<!-- b000080 | prose | pages [3] -->
17

<!-- b000081 | prose | pages [3] -->
19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 Strengths 19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2 Weaknesses

<!-- b000082 | heading | pages [3] -->
Appendix

<!-- b000083 | prose | pages [3] -->
19

<!-- b000084 | prose | pages [3] -->
22

<!-- b000085 | furniture | pages [4] -->
Team # 70545

<!-- b000086 | furniture | pages [4] -->
Page 3 of 25

<!-- b000087 | prose | pages [4] -->
1

<!-- b000088 | heading | pages [4] -->
Introduction

<!-- b000089 | prose | pages [4] -->
1.1

<!-- b000090 | heading | pages [4] -->
Background

<!-- b000091 | prose | pages [4] -->
Traveling on highways in recent years are quite convenient ways for people to go to another city. With a compared high speed limit on highway, people are able to travel a lot faster. However, building highways are quite expensive and it also takes a lot for the maintenance. Therefore, building of toll plazas along the highway is a common practice all around the world. Meanwhile, there are many factors to be considered during the design and the construction of the tollbooths. Firstly, the lands and the construction fee for the booths and roads are very expensive, so we need to minimize the area. And as the vehicles on the highway always have a high speed, it is also quite dangerous when they want to merge into a lane. Finally, the design of the booths is also supposed to guarantee the eﬃciency, which is described by the quantity throughout the highway for a certain time interval.

<!-- b000092 | prose | pages [4] -->
1.2 Restatement of the problem

<!-- b000093 | prose | pages [4] -->
As required by the question, we are supposed to determine the shape, size and merging pattern at the toll plaza depended on number of lanes on the highway in one direction (L) and total number of tollbooths in one direction (B). Meanwhile, we will also justify our approach by comparing it with the existing models in terms of risk, cost and eﬃciency. What’s more, the implement of our plan in various situations (e.g. mixture of the self-driving vehicle and di↵erent proportion distribution of types of tollbooths) will also be shown.

<!-- b000094 | prose | pages [4] -->
1.3 Literature review

<!-- b000095 | prose | pages [4] -->
The optimal number of tollbooths needed to minimize the average waiting time is well-studied and simulated based on di↵erent real situations (Corwen et al, 2005). Though the deﬁnition of “optimal” varies, similar suggestions have been given. Tollbooths should be implemented conforming to encouraged behaviors, e.g. faster booths should be put on the left (Spann et al, 2005), which is incorporated in our model. Some literature suggested that tollbooths employ no barrier to ensure a relatively smooth ﬂow (Kane, 2005), but we contend that the uplift of barrier takes negligible amount of time, the beneﬁt of which cannot be compared with the chaos and potential risk if some vehicles go through toll plaza directly. Therefore, barriers are included in our model.

<!-- b000096 | prose | pages [4] -->
2

<!-- b000097 | heading | pages [4] -->
Assumptions

<!-- b000098 | prose | pages [4] -->
To simplify the real life situation, we will make the following assumptions as a start of construction of our models.

<!-- b000099 | prose | pages [4] -->
• Most of the drivers are rational. They will choose the path as suggested by signals at entrance, and act as risk averters. It is reasonable to make this assumption, because without it, it’s meaningless to make any rules as people won’t obey them.

<!-- b000100 | furniture | pages [5] -->
Team # 70545

<!-- b000101 | furniture | pages [5] -->
Page 4 of 25

<!-- b000102 | prose | pages [5] -->
• The arrival time lapse between the ﬁrst vehicle and the second vehicle in

<!-- b000103 | heading | pages [5] -->
the heavy traﬃc follows uniform distribution. By the heavy traﬃc assumption,

<!-- b000104 | prose | pages [5] -->
the second vehicle comes to tollbooth before the ﬁrst vehicle leaves.

<!-- b000105 | prose | pages [5] -->
• All the paths of the vehicles follow either constant speed motion or constant acceleration motion. As the average speed for the vehicles around the tollbooths are relatively low.

<!-- b000106 | prose | pages [5] -->
• vehicles are queuing at the entrance of the tollbooth one by one with low speed in the heavy traﬃc situation . And we further assume them to be stationary in our models.

<!-- b000107 | prose | pages [5] -->
• The service by human-sta↵s at the tollbooth is quite time-consuming, and the approximate mean service time is around 15 seconds, which follows a

<!-- b000108 | heading | pages [5] -->
normal distribution. This assumption is appropriate, because driver need to bring

<!-- b000109 | prose | pages [5] -->
the fee to the sta↵and the sta↵may need to prepare changes for it. And the time varies from people and di↵erent situations.

<!-- b000110 | prose | pages [5] -->
• The length of vehicles is omitted during the calculation for the size and shape for the merging area. It is valid because the magnitude of the length of toll plaza is a lot larger than the length of vehicles.

<!-- b000111 | prose | pages [5] -->
3

<!-- b000112 | heading | pages [5] -->
Notations

<!-- b000113 | heading | pages [5] -->
Notation

<!-- b000114 | prose | pages [5] -->
Deﬁnition Unit Number of outgoing lanes in highway L B Number of tollbooths N/A N/A Distance between the tollbooth and the end of the plaza D m Width of the lane in highway dl m Width of the lane in tollbooth area db r Radius for vehicles’ turning m m Time of toll service per vehicle human-sta↵ed tollbooths Th s Time of control (to be deﬁned in Section 4.2) t0 vm Speed limit in merging area s m/s m/s2 Starting acceleration of vehicles after toll payment as

<!-- b000115 | prose | pages [5] -->
m/s2 Deceleration of braking vehicles ab

<!-- b000116 | prose | pages [5] -->
4

<!-- b000117 | heading | pages [5] -->
Models

<!-- b000118 | prose | pages [5] -->
In this section, we ﬁrst introduce and analyze the existing model, and then two new models invented by us. And the focus for the new models will only be the establishment of the ﬁrst new model (control time model) and second new model (waiting area model) only deviates from the ﬁrst one slightly.

<!-- b000119 | furniture | pages [6] -->
Team # 70545

<!-- b000120 | furniture | pages [6] -->
Page 5 of 25

<!-- b000121 | prose | pages [6] -->
4.1

<!-- b000122 | heading | pages [6] -->
Existing Model(EM)

<!-- b000123 | prose | pages [6] -->
Under our investigation, the existing solution for the merging after toll can be roughly divided into two types.

<!-- b000124 | prose | pages [6] -->
The ﬁrst solution is in short called “no solution”, which doesn’t give the drivers any instruction after toll and let them go at their own discretion. Then the second and more commonly used solution is to instruct the vehicles to merge at some pre-determined merging point.

<!-- b000125 | prose | pages [6] -->
For the ﬁrst solution, the eﬃciency of it is mainly based on the drivers’ own discretions, which can vary a lot among di↵erent people. And in the light traﬃc situations, this solution may be optimal, for the reason that drivers can go whatever path they what, and in other words their own eﬃciency is maximized. Meanwhile, with the light traﬃc assumption, there are little probability to crash. However, it will be fairly chaotic in heavy traﬃc, because it is very likely that driver’s own optimal path can cross each other. And then they will merge at any point so it is also hard to predict what drivers will do. Therefore, in heavy traﬃc, it is neither eﬃcient nor safe.

<!-- b000126 | prose | pages [6] -->
And the second solution provides a relatively orderly merging pattern. Vehicles merge at some certain merging points and at least the driving direction is predictable as long as the drivers are rational and always follow the instruction. However, some problems also occur at the merging point. As for most time, the number of tollbooths are larger than the number of lanes on the highway, there always exist the situation that vehicles from several di↵erent booths need to merge into one lane. So di↵erent vehicles from di↵erent booths can arrive at the merging point simultaneously, and then only one of them can get through at a time and others have to wait. This situation can be quite dangerous because drivers always want to go ﬁrst, and it also increase the deﬁciency.

<!-- b000127 | prose | pages [6] -->
4.2

<!-- b000128 | heading | pages [6] -->
Control Time Model (CTM)

<!-- b000129 | prose | pages [6] -->
Given aforementioned deﬁciencies of existing merging pattern, we propose a new model, partially based on the current one. Instead of having all the vehicles moving and merging at their own discretion, control time model will control the departure time of vehicles to ensure a smooth and safe emerging process.

<!-- b000130 | prose | pages [6] -->
Speciﬁcally, for situations where two booths merge into one lane, the second vehicle will only be allowed to proceed t0 seconds after the ﬁrst vehicle moves forward. The time t0 is deﬁned as the control time. Similarly, for situations where three booths merge into one lane, the third vehicle will be allowed to proceed t0 seconds after the second vehicle moves forward, whilst the second vehicle t0 seconds after the ﬁrst vehicle, as shown in Figure 1 and Figure 2.

<!-- b000131 | furniture | pages [7] -->
Team # 70545

<!-- b000132 | caption | pages [7] -->
Figure 1: Either A or B is open

<!-- b000133 | furniture | pages [7] -->
Page 6 of 25

<!-- b000134 | caption | pages [7] -->
Figure 2: Either C, D or E is open

<!-- b000135 | prose | pages [7] -->
In this way, the regulated merging of the vehicles into another lane would be more eﬃcient than the situation where vehicles are proceeding without regulation, for drivers should take time to make decision when multiple booths merge into one lane simultaneously, let alone the risk for doing so.

<!-- b000136 | prose | pages [7] -->
We model that vehicles start with constant acceleration as until reach the maximum speed vm in the straight path. They then immediately starts merging into their prescribed road in two consecutive tangent circle arcs.

<!-- b000137 | caption | pages [7] -->
Figure 3: Two or three tollbooth egress lanes merge into one lane

<!-- b000138 | prose | pages [7] -->
Now we evaluate the “appropriate” control time. When emergency happens, one vehicle take severe brake action with acceleration ab, after response time tres, the posterior vehicle take severe brake action with the same acceleration. Consider the distance of the two vehicles (t = 0 is the time when emergencies happen):

<!-- b000139 | prose | pages [7] -->
Z t

<!-- b000140 | prose | pages [7] -->
Z t

<!-- b000141 | prose | pages [7] -->
vposterior(t)dt −

<!-- b000142 | prose | pages [7] -->
d = vmtres +

<!-- b000143 | prose | pages [7] -->
0

<!-- b000144 | prose | pages [7] -->
where

<!-- b000145 | prose | pages [7] -->
8 >

<!-- b000146 | prose | pages [7] -->
vm,

<!-- b000147 | prose | pages [7] -->
<

<!-- b000148 | prose | pages [7] -->
vprevious(t)dt 0

<!-- b000149 | prose | pages [7] -->
t tres tres < t tres + vm vm −ab(t −tres),

<!-- b000150 | prose | pages [7] -->
vprevious =

<!-- b000151 | prose | pages [7] -->
> :

<!-- b000152 | prose | pages [7] -->
0,

<!-- b000153 | prose | pages [7] -->
(1)

<!-- b000154 | prose | pages [7] -->
ab tres + vm

<!-- b000155 | prose | pages [7] -->
ab < t

<!-- b000156 | prose | pages [7] -->
Solve the equation d ≥0, we get t0 ≥tres. By saying “appropriate” control time, we take t0 = 1s > tres = 0.8s (Lee et al, 2002).

<!-- b000157 | furniture | pages [8] -->
Team # 70545

<!-- b000158 | furniture | pages [8] -->
Page 7 of 25

<!-- b000159 | prose | pages [8] -->
After describing the control time model, we ﬁrst calculate the throughput of the toll plaza. Let ik be the number of booths corresponding with the kth lane. For example, if the ﬁrst three booths merge into the ﬁrst lane, we say i1 = 3.

<!-- b000160 | prose | pages [8] -->
By computer simulation (details are included in Appendix), we have tik close to T

<!-- b000161 | prose | pages [8] -->
T ik when t0 (especially when the variance of service time is small), and tik increases as ik ik << increases, and the increase speed is quite large when ik > T

<!-- b000162 | prose | pages [8] -->
for a car to come into kth lane.

<!-- b000163 | prose | pages [8] -->
t0. where tik is the averaged time

<!-- b000164 | prose | pages [8] -->
Therefore, to maximize the eﬃciency, we’ll keep ik as small as possible, whereas the

<!-- b000165 | prose | pages [8] -->
t0 for some k. The optimal throughput is closed to B

<!-- b000166 | prose | pages [8] -->
throughput comes suboptimal if ik > T

<!-- b000167 | prose | pages [8] -->
car(s) per second.

<!-- b000168 | prose | pages [8] -->
T

<!-- b000169 | prose | pages [8] -->
By substituting B by 8, the expectation of human service time T by 15. According to our optimization method above, when we keep the ik as small as possible, which is in other words, let them distributed evenly(e.g. {2,3,3}). We will get the optimal throughput closed to B

<!-- b000170 | prose | pages [8] -->
T ⇡0.533 car per second.

<!-- b000171 | prose | pages [8] -->
Then we calculate the size of the plaza, by doing so we discuss the value of D. Deﬁne f : {1, 2, . . . , B} ! {1, 2, . . . , L} which is non-decreasing, and f(i) = j if and only if vehicles from ith booth merge into jth lane. It obviously follows that ik = kf −1({k})k. We call the mapping f a “merging pattern”.

<!-- b000172 | prose | pages [8] -->
dB

<!-- b000173 | prose | pages [8] -->
Tollbooths

<!-- b000174 | prose | pages [8] -->
dL

<!-- b000175 | prose | pages [8] -->
Direction of trafﬁc ﬂow

<!-- b000176 | prose | pages [8] -->
D

<!-- b000177 | caption | pages [8] -->
Figure 4: B = 8 tollbooth egress lanes merge into L = 3 lanes

<!-- b000178 | prose | pages [8] -->
By geometric relations, we have

<!-- b000179 | furniture | pages [8] -->


<!-- b000180 | prose | pages [8] -->
!2

<!-- b000181 | prose | pages [8] -->
✓

<!-- b000182 | prose | pages [8] -->
D −v2

<!-- b000183 | prose | pages [8] -->
r −(i −1

<!-- b000184 | prose | pages [8] -->
m 2a

<!-- b000185 | prose | pages [8] -->
+

<!-- b000186 | prose | pages [8] -->
2

<!-- b000187 | prose | pages [8] -->
◆2

<!-- b000188 | prose | pages [8] -->
2)dB −(j −1 2)dL)

<!-- b000189 | prose | pages [8] -->
= r2

<!-- b000190 | prose | pages [8] -->
2

<!-- b000191 | prose | pages [8] -->
Observed from above relation, a certain (i, j) prescribes a lower bound of D, and for a certain merging pattern, the distance between the tollbooth and the end of the plaza that we eventually employ is the greatest lower bound of D. The less the greatest lower bound is, the smaller the size will be, and so will the cost of plaza.

<!-- b000192 | prose | pages [8] -->
By property of quadratic function, for a certain j, the greater i is, the greater D is. We have

<!-- b000193 | furniture | pages [8] -->


<!-- b000194 | prose | pages [8] -->
j

<!-- b000195 | prose | pages [8] -->
j

<!-- b000196 | prose | pages [8] -->
X

<!-- b000197 | prose | pages [8] -->
X

<!-- b000198 | prose | pages [8] -->
ikdB −jdL ≥

<!-- b000199 | prose | pages [8] -->
k=1

<!-- b000200 | prose | pages [8] -->
k=1

<!-- b000201 | prose | pages [8] -->
!

<!-- b000202 | prose | pages [8] -->
dB −(k + 1)dL

<!-- b000203 | prose | pages [8] -->
ik + 1

<!-- b000204 | furniture | pages [9] -->
Team # 70545

<!-- b000205 | furniture | pages [9] -->
Page 8 of 25

<!-- b000206 | prose | pages [9] -->
since dL > dB. That implies if j is changed into j + 1 whilst i is changed into i + 1, D will get smaller. Therefore, the global maximum must be obtained at one of the local maximum points, and then we let x be

<!-- b000207 | prose | pages [9] -->
(

<!-- b000208 | prose | pages [9] -->
(Pj

<!-- b000209 | prose | pages [9] -->
)

<!-- b000210 | prose | pages [9] -->
k=1 ik −1

<!-- b000211 | prose | pages [9] -->
x = max j2{1,2,...,L}

<!-- b000212 | prose | pages [9] -->
2)dB −(j −1 2)dL 2

<!-- b000213 | prose | pages [9] -->
And for given B and L, the optimal choice of merging pattern f would be the case if we can minimize x to be

<!-- b000214 | prose | pages [9] -->
{ik}2{kf−1({k})k:8f} x xmin = min

<!-- b000215 | prose | pages [9] -->
After trying out some pairs of small (B, L), we induce that for any given small number B, L (which can be put in practical use) satisfying B > L, there exists a merging pattern fm such that

<!-- b000216 | prose | pages [9] -->
2)dB −(L −1

<!-- b000217 | prose | pages [9] -->
x = (B −1

<!-- b000218 | prose | pages [9] -->
2)dL) := x0 2 2

<!-- b000219 | prose | pages [9] -->
Since for any ik we have the relation f(B) = L, which implies above expression will appear in every calculation of x for all ik, hence xmin ≥x0, hence the existence of x0 guarantees ”=”, providing us with the optimal merging pattern to minimize D.

<!-- b000220 | prose | pages [9] -->
By substituting B = 8, L = 3, dB = 2.5m, dL = 3.75m, r = 115m, vm = 15m/s, a = 2.78m/s2, the minimum of D is 105.5m, when (i1, i2, i3) 2 {(3, 3, 2), (3, 2, 3), (2, 3, 3)}.

<!-- b000221 | prose | pages [9] -->
4.3

<!-- b000222 | heading | pages [9] -->
Waiting Area Model(WAM)

<!-- b000223 | prose | pages [9] -->
After completing the above model, something seems to be deﬁcient also appears in our model. In the control time model, vehicles may need to wait at the booths even after the service ﬁnished, while there are a lot of vehicles queuing after it. So we wonder that whether it is better to build a waiting area at a plaza (as shown in Figure 5), so that the vehicles whose service has ﬁnished can go to the waiting area, then the consecutive vehicle can be serviced. So in this model, the sta↵spending more time serving instead of doing nothing while the vehicles are just waiting at the booths.

<!-- b000224 | prose | pages [9] -->
dB

<!-- b000225 | prose | pages [9] -->
Waiting area

<!-- b000226 | prose | pages [9] -->
Tollbooths

<!-- b000227 | prose | pages [9] -->
dL

<!-- b000228 | prose | pages [9] -->
Direction of trafﬁc ﬂow

<!-- b000229 | prose | pages [9] -->
D

<!-- b000230 | caption | pages [9] -->
Figure 5: B = 8 tollbooth egress lanes merge into L = 3 lanes

<!-- b000231 | prose | pages [9] -->
We will test and compare this model with control time model in the following sections, to see whether it is eﬃcient or not.

<!-- b000232 | furniture | pages [10] -->
Team # 70545

<!-- b000233 | prose | pages [10] -->
5

<!-- b000234 | heading | pages [10] -->
Analysis and Results

<!-- b000235 | furniture | pages [10] -->
Page 9 of 25

<!-- b000236 | prose | pages [10] -->
In this section we will analyze throughput, accident prevention and cost of each models introduced in former section.

<!-- b000237 | prose | pages [10] -->
5.1 Throughput

<!-- b000238 | prose | pages [10] -->
Throughput (✓) here is deﬁned to be the number of vehicles per hour passing the point where the end of the plaza joins one of the the L outgoing traﬃc lanes. Here we discuss only one outgoing lane merged from two lanes in human-sta↵ed tollbooth area in heavy traﬃc where vehicles come continuously during heavy traﬃc so that the cashier work continually, as shown in Figure 6 .

<!-- b000239 | prose | pages [10] -->
Tollbooths

<!-- b000240 | prose | pages [10] -->
dL

<!-- b000241 | prose | pages [10] -->
Direction of traffic flow

<!-- b000242 | prose | pages [10] -->
D

<!-- b000243 | caption | pages [10] -->
Figure 6: B = 8 tollbooth egress lanes merge intoL = 3 lanes in heavy traﬃc

<!-- b000244 | prose | pages [10] -->
5.1.1

<!-- b000245 | heading | pages [10] -->
Throughput of existing model

<!-- b000246 | prose | pages [10] -->
The toll collection service time is a random variable which can be seen as a sum of random variables including time needed by driver to search money or credit vehicled, time needed by cashier to take related record, etc. According to the central limit theorem, we can assume that the service time of ith vehicle (th,i) of the each lane follow normal distribution with µ = 15 and σ2 = 4 independently and identically.

<!-- b000247 | prose | pages [10] -->
Th,i ⇠N(15, 4)

<!-- b000248 | prose | pages [10] -->
Suppose the ﬁrst vehicle coming into the tollbooth area at t = 0, then the time of the nth

<!-- b000249 | prose | pages [10] -->
vehicles coming out from a lane tn should equal to the sum of the service time of itself and former vehicles.

<!-- b000250 | prose | pages [10] -->
tn =

<!-- b000251 | prose | pages [10] -->
n n X

<!-- b000252 | prose | pages [10] -->
Th,i

<!-- b000253 | prose | pages [10] -->
i=1

<!-- b000254 | prose | pages [10] -->
As can be seen that tn is the sum of normally distributed random variables, thus

<!-- b000255 | prose | pages [10] -->
tn ⇠N(15n, 4n)

<!-- b000256 | furniture | pages [11] -->
Team # 70545

<!-- b000257 | furniture | pages [11] -->
Page 10 of 25

<!-- b000258 | prose | pages [11] -->
Besides we introduce a concept Post-Encroachment Time (PET) which is deﬁned to be the time lapse between end of encroachment of turning vehicle and the time that the through vehicle actually arrives at the potential point of collision (Gettman & Head, 2003). When PET is less than reaction time, rational drivers would decelerate in order to maintain a safety distance, corresponding to reaction time tr = 1s, with former vehicle. Consequently, more time is needed to pass the merging area which lower the eﬃciency and throughput. Denote PET of ith vehicle as PETi, then total delayed time Td is

<!-- b000259 | prose | pages [11] -->
X

<!-- b000260 | prose | pages [11] -->
Td =

<!-- b000261 | prose | pages [11] -->
PETi<tr

<!-- b000262 | prose | pages [11] -->
(tr −PETi)

<!-- b000263 | prose | pages [11] -->
Considering the total delayed time Td, the mean time needed of a vehicle coming out from merging area is

<!-- b000264 | prose | pages [11] -->
t = tn + Td

<!-- b000265 | prose | pages [11] -->
2n Since there are two lanes working simultaneously and assume the motion in the merging area of each vehicle is the same, the throughput of the outgoing lane should be

<!-- b000266 | prose | pages [11] -->
✓= 3600

<!-- b000267 | prose | pages [11] -->
t After computer simulation with N = 1000 times, the results are shown in Figure. 7

<!-- b000268 | heading | pages [11] -->
Throughput of control time model

<!-- b000269 | prose | pages [11] -->
5.1.2

<!-- b000270 | prose | pages [11] -->
Now we consider the model with control time (t0). Suppose the nth vehicle coming out from lane a at ta,n with service time Ta,n the mth vehicle coming out from lane b at tb,m with service time Tb,m where

<!-- b000271 | prose | pages [11] -->
Ta,n ⇠N(15, 4) Tb,m ⇠N(15, 4) and

<!-- b000272 | prose | pages [11] -->
Assume the 1st vehicle comes to lane a at t = 0 and after ∆T the 2nd vehicles comes to lane b where ∆T ⇠U(0, 15). If we have

<!-- b000273 | prose | pages [11] -->
ta,n + Ta,n+1 < tb,m + Tb,m+1

<!-- b000274 | prose | pages [11] -->
which means the (n+1)th vehicle in lane a completes toll collection service before the (m+1)th

<!-- b000275 | prose | pages [11] -->
vehicle in lane b, then

<!-- b000276 | prose | pages [11] -->
ta,n+1 = max{ta,n + Ta,n+1, ta,n + t0, tb,m + t0}

<!-- b000277 | prose | pages [11] -->
otherwise

<!-- b000278 | prose | pages [11] -->
tb,m+1 = max{tb,m + Tb,m+1, ta,n + t0, tb,m + t0}

<!-- b000279 | prose | pages [11] -->
Set max{ta,n, tb,m} < 3600 in order to simulate time period of one hour. Once if

<!-- b000280 | prose | pages [11] -->
ta,n⇤> 3600

<!-- b000281 | prose | pages [11] -->
we can obtain the throughput as

<!-- b000282 | prose | pages [11] -->
or or tb,m⇤> 3600

<!-- b000283 | prose | pages [11] -->
✓= n⇤+ m⇤−1

<!-- b000284 | prose | pages [11] -->
After computer simulation with N = 1000 times, the results are shown in Figure. x

<!-- b000285 | furniture | pages [12] -->
Team # 70545

<!-- b000286 | furniture | pages [12] -->
Page 11 of 25

<!-- b000287 | prose | pages [12] -->
5.1.3

<!-- b000288 | heading | pages [12] -->
Throughput of waiting area model

<!-- b000289 | prose | pages [12] -->
Denote tas,n as the time when nth vehicle completes toll collection and starts to wait in lane b, tbs,m as the time when mth vehicle completes toll collection and starts to wait in lane b. The iteration equations in former section can be adapted to the follows. If

<!-- b000290 | prose | pages [12] -->
tas,n + Ta,n+1 < tbs,m + Tb,m+1

<!-- b000291 | prose | pages [12] -->
which means the (n+1)th vehicle in lane a completes toll collection service before the (m+1)th

<!-- b000292 | prose | pages [12] -->
vehicle in lane b, then

<!-- b000293 | prose | pages [12] -->
ta,n+1 = max{tas,n + Ta,n+1, ta,n + t0, tb,m + t0}

<!-- b000294 | prose | pages [12] -->
otherwise

<!-- b000295 | prose | pages [12] -->
tb,m+1 = max{tbs,m + Tb,m+1, ta,n + t0, tb,m + t0}

<!-- b000296 | prose | pages [12] -->
Set max{ta,n, tb,m} < 3600 in order to simulate time period of one hour. Once if

<!-- b000297 | prose | pages [12] -->
ta,n⇤> 3600 or tb,m⇤> 3600

<!-- b000298 | prose | pages [12] -->
we can obtain the throughput as

<!-- b000299 | prose | pages [12] -->
✓= n⇤+ m⇤−1

<!-- b000300 | prose | pages [12] -->
After computer simulation with N = 1000 times, the results are shown in Figure 7

<!-- b000301 | prose | pages [12] -->
5.1.4 Comparison and hypothesis tests of throughputs

<!-- b000302 | prose | pages [12] -->
500

<!-- b000303 | prose | pages [12] -->
490

<!-- b000304 | prose | pages [12] -->
Throughput veh/(h·lane)

<!-- b000305 | prose | pages [12] -->
480

<!-- b000306 | prose | pages [12] -->
470

<!-- b000307 | prose | pages [12] -->
460

<!-- b000308 | prose | pages [12] -->
450

<!-- b000309 | prose | pages [12] -->
Existing Model Control Time Model Waiting Area Model

<!-- b000310 | caption | pages [12] -->
Figure 7: Comparison of throughput of models

<!-- b000311 | furniture | pages [13] -->
Team # 70545

<!-- b000312 | furniture | pages [13] -->
Page 12 of 25

<!-- b000313 | prose | pages [13] -->
It can be seen from Figure 7 that the throughputs di↵er slightly among models. Therefore, we conduct hypothesis test for means at 5% level of signiﬁcance.

<!-- b000314 | prose | pages [13] -->
H0 :There is no di↵erence in average throughputs

<!-- b000315 | prose | pages [13] -->
in existing modeland control time model, i.e. µ1 = µ2 H1 :H0 is wrong, i.e.µ1 6= µ2

<!-- b000316 | caption | pages [13] -->
Table 1: Statistics of two models

<!-- b000317 | prose | pages [13] -->
Model Size Existing Model 1000 Control Time Model 1000 Waiting Area Model 1000 Mean S.d.

<!-- b000318 | prose | pages [13] -->
SEM 477.830 4.054 0.128 477.422 5.843 0.185 479.081 6.039 0.191

<!-- b000319 | prose | pages [13] -->
di↵erence in means = 477.830 −477.422 = 0.408

<!-- b000320 | prose | pages [13] -->
overall standard error =

<!-- b000321 | prose | pages [13] -->
p p

<!-- b000322 | prose | pages [13] -->
0.1282 + 0.1852 = 0.225

<!-- b000323 | prose | pages [13] -->
test statistic = 0.408

<!-- b000324 | prose | pages [13] -->
0.225 = 1.813

<!-- b000325 | prose | pages [13] -->
p-value = 0.0348 > 0.025

<!-- b000326 | prose | pages [13] -->
Therefore, H0 is not rejected at 5% level of signiﬁcance.

<!-- b000327 | prose | pages [13] -->
We conclude that there is no signiﬁcant di↵erence of means of throughputs in existing model and control time model.

<!-- b000328 | prose | pages [13] -->
However, by similar method, when we make hypothesis test for means of the later two models, the conclusion is that there is signiﬁcant di↵erence of means of throughputs in existing model and control time model.

<!-- b000329 | prose | pages [13] -->
The analysis of throughputs above lead to the following results:

<!-- b000330 | prose | pages [13] -->
• Control time mechanism would not lower the eﬃciency and throughput. It just transfer delayed time Td in merging area under existing model to control time t0 in tollbooth area under control time model, as shown in

<!-- b000331 | prose | pages [13] -->
• Control time mechanism can improve the orderliness of the pattern of vehicles coming out from tollbooth into merging area which thereby improves the safety level of the merging pattern, to be discussed in section 5.2.

<!-- b000332 | prose | pages [13] -->
• Even though waiting area design could improve throughput, the increment 1.6veh/h is slight compared to the magnitude of throughput. Besides, the cost of land as well as other expense with regard to waiting area can be relatively high. Therefore, the disad- vantageous of waiting area outweigh the beneﬁt it brings so that we should disvehicled this model.

<!-- b000333 | furniture | pages [14] -->
Team # 70545

<!-- b000334 | prose | pages [14] -->
200

<!-- b000335 | prose | pages [14] -->
count

<!-- b000336 | prose | pages [14] -->
100

<!-- b000337 | prose | pages [14] -->
0

<!-- b000338 | prose | pages [14] -->
0 5 10 PET

<!-- b000339 | furniture | pages [14] -->
Page 13 of 25

<!-- b000340 | prose | pages [14] -->
Model

<!-- b000341 | prose | pages [14] -->
Control Time Model

<!-- b000342 | prose | pages [14] -->
Existing Model

<!-- b000343 | prose | pages [14] -->
15 15 20 25

<!-- b000344 | caption | pages [14] -->
Figure 8: PET of existing model and PET of control time model

<!-- b000345 | prose | pages [14] -->
5.2 Accident prevention

<!-- b000346 | prose | pages [14] -->
This section will analyze accident rate in merging area in terms of PET. When PET is small, it becomes diﬃcult for drivers to make decision promptly to avoid collision, and thus accident is more likely to happen. Therefore, we introduce following function to associate the probability of accident with PET.

<!-- b000347 | prose | pages [14] -->
p = e−PET

<!-- b000348 | prose | pages [14] -->
(2) 100

<!-- b000349 | prose | pages [14] -->
When PET = 0, two vehicles arrive the potential point of collision theoretically while drivers could manage speed along the way in order to avoid collision, and hence the probability of collision under this circumstance can be set 0.01. After computer simulation based on the iteration equations with N = 4000 times, the PET of existing model and PET of control time model are shown in Figure 8.

<!-- b000350 | prose | pages [14] -->
It can be seen that under existing model, a signiﬁcant part of PET lies in the interval [0, 1] where accident is more likely to happen. While under control time model, due to the control mechanism, the minimum PET is control time t0 = 1s which guarantee low accident risk. The expectations of accident rate by simulation on function are shown in Table 2 The control time model can reduce the accident rate by 13.66%. What’s more, the low rate of accident would make vehicles pass merging area without hindrance, which improve eﬃciency Therefore, The control time model has better performance in accident and throughput. prevention than existing model.

<!-- b000351 | furniture | pages [15] -->
Team # 70545

<!-- b000352 | furniture | pages [15] -->
Page 14 of 25

<!-- b000353 | caption | pages [15] -->
Table 2: Accident rate of each model

<!-- b000354 | prose | pages [15] -->
Accident per 100,000 vehicles Model Existing Model Control Time Model

<!-- b000355 | prose | pages [15] -->
5.3 Cost

<!-- b000356 | prose | pages [15] -->
53.024 61.416

<!-- b000357 | prose | pages [15] -->
This section analyzes cost of merging area and tollbooth area, including ﬁxed cost and variable cost per year, i.e. annual operation cost. Fixed cost mainly depends on cost of land and tollbooth construction. We can estimate area of land (A) by supposing the marginal curve of the out-most lane is symmetric, as shown in Figure 9

<!-- b000358 | prose | pages [15] -->
Tollbooths

<!-- b000359 | prose | pages [15] -->
dL

<!-- b000360 | prose | pages [15] -->
Direction of trafﬁc ﬂow

<!-- b000361 | prose | pages [15] -->
D

<!-- b000362 | caption | pages [15] -->
Figure 9: Estimation of A by symmetry of shaded area

<!-- b000363 | prose | pages [15] -->
Tollbooth construction cost can be divided to three kinds including human-sta↵ed, elec- tronic and automated tollbooths.

<!-- b000364 | prose | pages [15] -->
Fixed cost = 1

<!-- b000365 | prose | pages [15] -->
2c1A + (chph + cepe + capa)B

<!-- b000366 | prose | pages [15] -->
where

<!-- b000367 | prose | pages [15] -->
A = v2

<!-- b000368 | prose | pages [15] -->
a Bdb + (Bdb + Ldl)(D −v2 m

<!-- b000369 | prose | pages [15] -->
m 2a )

<!-- b000370 | prose | pages [15] -->
cl = construction cost of land per m2

<!-- b000371 | prose | pages [15] -->
ch = construction cost per automated tollbooth

<!-- b000372 | prose | pages [15] -->
ce = construction cost per electronic tollbooth ca = construction cost per human-sta↵ed tollbooth

<!-- b000373 | prose | pages [15] -->
Substitute B = 8, L = 3, dB = 2.5, dL = 3.75, cl = 172.83, ch = 58500, ce = 15400, ca = 58000 (Pietrzyk,1992), ph = 4/8, pe = 1/8, pa = 3/8 and get ﬁxed cost = $739, 320. Simi- larly, annual operation cost of tollbooth area can be estimated by

<!-- b000374 | prose | pages [15] -->
Annual operation cost = (c0

<!-- b000375 | prose | pages [15] -->
2 + c0 hph + c0

<!-- b000376 | prose | pages [15] -->
epe)B

<!-- b000377 | furniture | pages [16] -->
Team # 70545

<!-- b000378 | furniture | pages [16] -->
Page 15 of 25

<!-- b000379 | prose | pages [16] -->
c0

<!-- b000380 | prose | pages [16] -->
a = operation cost of tollbooth construction and operation per year c0

<!-- b000381 | prose | pages [16] -->
h = operation cost of salary per cashier c0

<!-- b000382 | prose | pages [16] -->
e = operation cost of each electronic device

<!-- b000383 | prose | pages [16] -->
Substitute c0

<!-- b000384 | prose | pages [16] -->
h = 141900, c0

<!-- b000385 | prose | pages [16] -->
e = 4200, c0

<!-- b000386 | prose | pages [16] -->
a = 43300 (Pietrzyk,1992), ph = 4/8, pe = 1/8, pa = 3/8 and get annual operation cost = $701, 700.

<!-- b000387 | prose | pages [16] -->
6 Possible Modiﬁcation

<!-- b000388 | prose | pages [16] -->
As required in the problem, our report will then proceed to analyze the inﬂuences of some deviation of the conditions on our model.

<!-- b000389 | prose | pages [16] -->
Some possible modiﬁcations may be made to improve the utility of our model in those situations.

<!-- b000390 | prose | pages [16] -->
6.1 Mixture of autonomous vehicles and human-driving vehicles

<!-- b000391 | prose | pages [16] -->
With the improvements in artiﬁcial intelligence and vehicle industry recent years, autonomous vehicles have become much more reliable and popular. However, some dangerous occasions may occur as the auto-driving system is not completely stable for all time. Therefore, even in some countries people are allowed to take the autonomous vehicle to the street, there are always required to be a driving sitting on the driver’s seat and prepared to take over at any time.

<!-- b000392 | prose | pages [16] -->
If autonomous vehicles are allowed on the street, the situation of merging may become much more complicated. Firstly, sometimes the autonomous vehicles fail to detect the mark- ing on the road and therefore go a wrong lane (Sam, 2016). It will be very dangerous if the autonomous vehicle went wrong when merging. Because there are a lot of complicated lanes at the merging area, and some may even cross each other, which are diﬃcult for an autonomous vehicle to recognize and are hard to determine the turning angle accurately.

<!-- b000393 | prose | pages [16] -->
And one possible solution is to instruct the autonomous vehicles to go to the most left lane. Reason to constraint them to this lane is that the vehicles go through it will just need to go straight till the very end of merging area, which is also the optimal path that the computer will generate even that it fails to detect the signal on the road.

<!-- b000394 | prose | pages [16] -->
6.2 Change in proportion of di↵erent types of tollbooths

<!-- b000395 | prose | pages [16] -->
Nowadays, there are roughly 3 di↵erent types of tollbooths, they are conventional (human- sta↵ed), automated and electronic toll collection booths. The main di↵erence among these three di↵erent types is that they have di↵erent service times.

<!-- b000396 | prose | pages [16] -->
The conventional booths have the longest service time, which is around 15 seconds in our assumption.

<!-- b000397 | prose | pages [16] -->
And the automated ones have the second longest service time, and we assume it to be around 8 seconds. Meanwhile, vehicles equipped with ETC transponder are able to pass the ETC booths even without stop (with a maximal passing speed of 15mph).

<!-- b000398 | prose | pages [16] -->
The model we introduced before works out quite good for both conventional and auto- mated booths as explained before. However, it may not work well with ETC since they don’t

<!-- b000399 | furniture | pages [17] -->
Team # 70545

<!-- b000400 | furniture | pages [17] -->
Page 16 of 25

<!-- b000401 | prose | pages [17] -->
need to stop at the booth. First of all, one thing that we would like to classify is that the proportion of ETC booths will be at either a minority or majority position. It is because that the estimated capacity of a single ETC booth is 2000/h, and this number is much larger than the need now considering the proportion of the drivers who possess a ETC transponder. So if the ETC booths are to be included in a toll plaza, we will place it at the most left lane, as we only need one to satisfy all demands for it. And we will arrange the other booths and lanes with the algorithm we introduced before. Of course, if the users of ETC are going to increase signiﬁcantly in the future, the proportion of ETC booths can also be increased. However, one thing to be noticed is that always one booth merges to one lane on highway, provided that the eﬃciency of ETC booths are high and we do not need to increase the number of booths, which will only make it riskier when merging.

<!-- b000402 | prose | pages [17] -->
7

<!-- b000403 | heading | pages [17] -->
Sensitivity test

<!-- b000404 | prose | pages [17] -->
This section conducts sensitivity tests of throughput and cost. We deﬁne the sensitivity of

<!-- b000405 | prose | pages [17] -->
dA

<!-- b000406 | prose | pages [17] -->
X . If A is a discrete function, we change dA into

<!-- b000407 | prose | pages [17] -->
a function A(X) in terms of X to be

<!-- b000408 | prose | pages [17] -->
A dX

<!-- b000409 | prose | pages [17] -->
∆A = A(X + 1) −A(X).

<!-- b000410 | heading | pages [17] -->
Sensitivity test of throughput

<!-- b000411 | prose | pages [17] -->
7.1

<!-- b000412 | prose | pages [17] -->
-2.0

<!-- b000413 | prose | pages [17] -->
Sensitivity of throughput

<!-- b000414 | prose | pages [17] -->
-1.0

<!-- b000415 | prose | pages [17] -->
0.0

<!-- b000416 | prose | pages [17] -->
0 1 2 3 4

<!-- b000417 | prose | pages [17] -->
Mean of service time

<!-- b000418 | prose | pages [17] -->
0.10

<!-- b000419 | prose | pages [17] -->
Sensitivity of throughput

<!-- b000420 | prose | pages [17] -->
0.00

<!-- b000421 | prose | pages [17] -->
-0.10

<!-- b000422 | prose | pages [17] -->
0 1 2 3 4

<!-- b000423 | prose | pages [17] -->
Standard deviation of service time

<!-- b000424 | caption | pages [17] -->
Figure 10: Sensitivity of throughput in terms of mean and standard deviation of service time.

<!-- b000425 | prose | pages [17] -->
As shown in 10, the sensitivity of throughput in terms of mean of service time T is a constant −1. Recall that in section 4.2, the optimal throughput is

<!-- b000426 | prose | pages [17] -->
✓= B

<!-- b000427 | prose | pages [17] -->
T The inverse ratio relationship of ✓and T implies unit constant sensitivity of ✓with respect to T, which is consistent with sensitivity test result. Besides, due to the law of large number, the volatility of service time ﬁnally performs slight e↵ects on throughput and thus the sensitivity is zero.

<!-- b000428 | furniture | pages [18] -->
Team # 70545

<!-- b000429 | prose | pages [18] -->
7.2

<!-- b000430 | heading | pages [18] -->
Sensitivity test of ﬁxed cost

<!-- b000431 | furniture | pages [18] -->
Page 17 of 25

<!-- b000432 | prose | pages [18] -->
By our assumption stated in Section 4.2 that the greatest lower bound is provided by the most outside lane and booth, combined with the formula to calculate the ﬁxed cost, we get

<!-- b000433 | prose | pages [18] -->
Fixed cost = 1

<!-- b000434 | prose | pages [18] -->
2c1A + (chph + cepe + capa)B

<!-- b000435 | prose | pages [18] -->
The initial value of

<!-- b000436 | prose | pages [18] -->
(vm, a, B, L, dB, dL, pa, pe, ph, cl, ce, ch, ca) =(15, 2.78, 8, 3, 2.5, 3.75, 3/8, 1/8, 4/8, 172.84, 15400, 58500, 58000)

<!-- b000437 | prose | pages [18] -->
We calculate the sensitivity of the ﬁxed cost with respect to the number of booths B, we get the graph as following And it shows that the the sensitivity of B around 8 is about 1.15 and

<!-- b000438 | prose | pages [18] -->
Sensitivity of Fixed Cost

<!-- b000439 | prose | pages [18] -->
Sensitivity of Fixed Cost

<!-- b000440 | prose | pages [18] -->
0.20

<!-- b000441 | prose | pages [18] -->
0.7 0.6 0.5

<!-- b000442 | prose | pages [18] -->
0.15

<!-- b000443 | prose | pages [18] -->
0.4 0.3

<!-- b000444 | prose | pages [18] -->
0.10

<!-- b000445 | prose | pages [18] -->
0.2 0.1 v

<!-- b000446 | prose | pages [18] -->
100

<!-- b000447 | prose | pages [18] -->
6 8 10 12 14 16 18 20

<!-- b000448 | prose | pages [18] -->
Sensitivity of Fixed Cost

<!-- b000449 | prose | pages [18] -->
1.4

<!-- b000450 | prose | pages [18] -->
1.3

<!-- b000451 | prose | pages [18] -->
1.2

<!-- b000452 | prose | pages [18] -->
1.1

<!-- b000453 | prose | pages [18] -->
r

<!-- b000454 | prose | pages [18] -->
B

<!-- b000455 | prose | pages [18] -->
150 200 250 300

<!-- b000456 | prose | pages [18] -->
3 5 6 7 8 9 10

<!-- b000457 | caption | pages [18] -->
Figure 11: Sensitivity of ﬁxed cost in terms of vm, r and B

<!-- b000458 | prose | pages [18] -->
always above 1, and the decreasing speed is very low, which means that D is always sensitive in terms of B. So increasing B can have signiﬁcant inﬂuence on D, and we may need to evaluate more whether to build more booths considering the balance of cost and eﬃciency.

<!-- b000459 | prose | pages [18] -->
Similarly, we can calculate the sensitivity of ﬁxed cost with respect to vm and r(as shown in the Figure 11).

<!-- b000460 | prose | pages [18] -->
The sensitivity of vm around 0.38, and it remains below 1 as it vary from 10m/s to 20m/s, which shows that the cost is not sensitive to the speed limit. So our cost estimation should be roughly correct with slight deviation with vm. Finally, with similar analysis, sensitivity in terms of r is always around 0.1 and 0.2 from 50m to 200m. So the radius only have little inﬂuence on our ﬁnal result.

<!-- b000461 | prose | pages [18] -->
8

<!-- b000462 | heading | pages [18] -->
Conclusion

<!-- b000463 | prose | pages [18] -->
In Section 4 we describe three models, namely existing models, CTM, WAM. By simulation in Section 5, we discard WAM and point out the deﬁciencies of EM model and employ CTM. Therefore, the following conclusion is based on CTM.

<!-- b000464 | prose | pages [18] -->
The shape of the plaza should enable cars from every booth to merge into its prescribed lane with two consecutive arcs. By the assumption stated in Section 4.2, the shape of the plaza is determined by the most outside booth merging into the most outside lane. The

<!-- b000465 | furniture | pages [19] -->
Team # 70545

<!-- b000466 | furniture | pages [19] -->
Page 18 of 25

<!-- b000467 | prose | pages [19] -->
boundary should make sure that the most outside vehicles have suﬃcient space on its right side. Take the example of B = 8, L = 3, the shape and merging pattern are as follows.

<!-- b000468 | prose | pages [19] -->
dB

<!-- b000469 | prose | pages [19] -->
Tollbooths

<!-- b000470 | prose | pages [19] -->
dL

<!-- b000471 | prose | pages [19] -->
Direction of trafﬁc ﬂow

<!-- b000472 | prose | pages [19] -->
D

<!-- b000473 | caption | pages [19] -->
Figure 12: Shape and merging pattern of merging area

<!-- b000474 | prose | pages [19] -->
Note that in no case will cars from di↵erent booths merge into one lane simultaneously as is stated in our control time model, so it does not matter whether the distance between two adjacent trajectories merging into one lane becomes smaller or not. Additionally, leading lines should be drawn on the ground to ensure that vehicles take intended paths.

<!-- b000475 | prose | pages [19] -->
The size of merging area is given by formula

<!-- b000476 | prose | pages [19] -->
a Bdb + (Bdb + Ldl)(D −v2

<!-- b000477 | prose | pages [19] -->
A = v2

<!-- b000478 | prose | pages [19] -->
m

<!-- b000479 | prose | pages [19] -->
m 2a )

<!-- b000480 | prose | pages [19] -->
for one direction. This includes the acceleration paths (the left term) and merging (turning) paths (the right term). Multiply it by a factor 2 if we are to calculate for two directions. For the above example B = 8, L = 3, the area for one direction is 1824.93m2

<!-- b000481 | prose | pages [19] -->
In heavy traﬃc (deﬁned as the situation where there is at least one car at every service booths), the throughput of plaza is approximately 3600B/T vehicles per hour (if all the toll- booths are human-sta↵ed) , computed by induction of computer simulation. By substituting B = 8, Th = 15, we get 1920 vehicles per hour from human-sta↵ed lanes. In light traﬃc, the throughput is less than 3600B/T. Overall, there is no statistical signiﬁcant of di↵erence between throughput of CTM and existing model. This comparison does not include the con- sideration of accident. If we take into account the fact that CTM reduces the accident rate by 13.66% and that accident is likely to cause traﬃc jam and reduce toll plaza’s throughput, the superiority of CTM would be more distinct. The cost of construction (ﬁxed cost) and operation (variable cost) of the merging area and tollbooth area are calculated respectively. The ﬁxed cost is given by the formula

<!-- b000482 | prose | pages [19] -->
Fixed cost = 1

<!-- b000483 | prose | pages [19] -->
2c1A + (chph + cepe + capa)B

<!-- b000484 | prose | pages [19] -->
the denotation is given in Section 5.3. In the B=8, L=3 example, the ﬁxed cost is $739320. The annual cost is given by similar formula

<!-- b000485 | prose | pages [19] -->
Annual operation cost = (c0

<!-- b000486 | prose | pages [19] -->
2 + c0 hph + c0

<!-- b000487 | prose | pages [19] -->
epe)B

<!-- b000488 | prose | pages [19] -->
which, in our example, turns to be $701, 700 per year.

<!-- b000489 | furniture | pages [20] -->
Team # 70545

<!-- b000490 | furniture | pages [20] -->
Page 19 of 25

<!-- b000491 | prose | pages [20] -->
9

<!-- b000492 | heading | pages [20] -->
Strengths and Weaknesses

<!-- b000493 | prose | pages [20] -->
9.1

<!-- b000494 | heading | pages [20] -->
Strengths

<!-- b000495 | prose | pages [20] -->
By computer simulation, as the expression of throughput ✓only contains the number of booths B and service time T, the employment of regulation in control time model does not reduce the throughput of the plaza (control time t0 is not in the expression). However, the risk of accident decreases to a great extent, which ensures a safe and smooth ﬂow of vehicles.

<!-- b000496 | prose | pages [20] -->
Moreover, we consider service time T following normal distribution instead of assuming a constant, which can better approximate real situation. Additionally, the control time mech- anism could decrease the size of merging area compared with existing model where vehicles merge at their discretion. Last but not least, we use multiple programming platforms to run computer simulations (Mathematica, MATLAB and R), which provides us with accurate and convincing data to support our models.

<!-- b000497 | prose | pages [20] -->
9.2

<!-- b000498 | heading | pages [20] -->
Weaknesses

<!-- b000499 | prose | pages [20] -->
We assume the vehicles adopt two tangent uniform circular motion to merge into its pre- scribed lane, which may not be the real trajectory of vehicles. However, we can draw some leading lines on the ground to guide vehicles. Additionally, we do not consider the situation where vehicles break down and block certain booths and/or lanes.

<!-- b000500 | prose | pages [20] -->
The arrival of vehicles should follow Poisson distribution, but as we did not have the real- world data to estimate λ, we instead assume that the di↵erence of two consecutive vehicles’ arrival follows a uniform distribution, which may lead to some inaccuracies. This problem, together with the diﬃculties to determine the expectation and variance of service time T, could be addressed if data collected in real-world situation could be provided.

<!-- b000501 | heading | pages [21] -->
References

<!-- b000502 | references | pages [21] -->
[1] Abdel-Aty, M. A., & Radwan, A. E. (2000). Modeling traﬃc accident occurrence and

<!-- b000503 | references | pages [21] -->
involvement. Accident Analysis & Prevention, 32(5), 633-642.

<!-- b000504 | references | pages [21] -->
[2] Corwin, I., Ganatra, S., & Rozenblyum, N. (2005). A Single-vehicle Interaction Model

<!-- b000505 | references | pages [21] -->
of Traﬃc for a Highway Toll Plaza. The UMAP Journal, 26(223), 299-315.

<!-- b000506 | references | pages [21] -->
[3] Friedman, D. A., & Waldfogel, J. (1995). The administrative and compliance cost of

<!-- b000507 | references | pages [21] -->
manual highway toll collection: evidence from Massachusetts and New Jersey. National

<!-- b000508 | references | pages [21] -->
Tax Journal, 217-228.

<!-- b000509 | references | pages [21] -->
[4] Gettman, D., & Head, L. (2003). Surrogate safety measures from traﬃc simulation mod-

<!-- b000510 | references | pages [21] -->
els. Transportation Research Record: Journal of the Transportation Research Board,

<!-- b000511 | references | pages [21] -->
(1840), 104-115.)

<!-- b000512 | references | pages [21] -->
[5] Gurney, J. K. (2013). Sue my vehicle not me: Products liability and accidents involving

<!-- b000513 | references | pages [21] -->
autonomous vehicles.

<!-- b000514 | references | pages [21] -->
[6] Harchol-Balter, M., Osogami, T., Scheller-Wolf, A., & Wierman, A. (2005). Multi-server

<!-- b000515 | references | pages [21] -->
queueing systems with multiple priority classes. Queueing Systems, 51(3-4), 331-360.

<!-- b000516 | references | pages [21] -->
[7] Lai, S. F. (2011). The Accident Risk Measuring Model for Urban Arterials. In 3rd

<!-- b000517 | references | pages [21] -->
International Conference on Road Safety and Simulation, Indianapolis, USA, September

<!-- b000518 | references | pages [21] -->
(pp. 14-16).

<!-- b000519 | references | pages [21] -->
[8] Lee, J. D., McGehee, D. V., Brown, T. L., & Reyes, M. L. (2002). Collision warning

<!-- b000520 | references | pages [21] -->
timing, driver distraction, and driver response to imminent rear-end collisions in a high-

<!-- b000521 | references | pages [21] -->
ﬁdelity driving simulator. Human Factors, 44(2), 314.

<!-- b000522 | references | pages [21] -->
[9] Oliver, N., & Pentland, A. P. (2000). Graphical models for driver behavior recognition

<!-- b000523 | references | pages [21] -->
in a smartvehicle. In Intelligent Vehicles Symposium, 2000. IV 2000. Proceedings of the

<!-- b000524 | references | pages [21] -->
IEEE (pp. 7-12). IEEE.

<!-- b000525 | references | pages [21] -->
[10] Pietrzyk, M. C. (1992). COST-EFFECTIVENESS ANALYSIS OF AVI/ETTM FOR

<!-- b000526 | references | pages [21] -->
FLORIDA’S TURNPIKE SYSTEM (No. WPI 0510406,).

<!-- b000527 | references | pages [21] -->
[11] Song, L. X. (2008). Application and mathematic model of queueing theory in freeway

<!-- b000528 | references | pages [21] -->
toll system. Science &Technology Information, 29, 391.

<!-- b000529 | references | pages [21] -->
[12] Spann, A., Kane, D., & Gulotta, D. (2005). Lane Changes and Close Following: Trou-

<!-- b000530 | references | pages [21] -->
blesome Tollbooth Traﬃc. UMAPJournal, 317.

<!-- b000531 | references | pages [21] -->
[13] Spiliopoulou, A. D., Papamichail, I., & Papageorgiou, M. (2009). Toll plaza merging traf-

<!-- b000532 | references | pages [21] -->
ﬁc control for throughput maximization. Journal of Transportation Engineering, 136(1),

<!-- b000533 | references | pages [21] -->
67-76.

<!-- b000534 | references | pages [22] -->
[14] Zhang, Z. (2014). Research on traﬃc conﬂict of freeway diverging and merging sections

<!-- b000535 | references | pages [22] -->
and toll booth.

<!-- b000536 | references | pages [22] -->
[15] ZHENG, Y. L., ZHAI, R. P., & MA, S. Q. (2006). Survey of Cellular Automata Model

<!-- b000537 | references | pages [22] -->
of Traﬃc Flow. Journal of Highway and Transportation Research and Development, 1,

<!-- b000538 | references | pages [22] -->
027.

<!-- b000539 | heading | pages [23] -->
Appendix

<!-- b000540 | prose | pages [23] -->
Some useful codes in R

<!-- b000541 | heading | pages [23] -->
1. Eﬃciency simulations

<!-- b000542 | heading | pages [23] -->
1.1 Eﬃciency simulation of existing model

<!-- b000543 | prose | pages [23] -->
x=numeric(1000) y=numeric(1000) mean.ex=numeric(1000) PET.ex=numeric(1999) for (j in 1:1000) { t1=rnorm(1000,15,4) t2=rnorm(1000,15,4) for (i in 1:1000) { x[i]=sum(t1[1:i]) y[i]=sum(t2[1:i]) time.x.y=sort(c(x,y)) } k=1:1999 PET.ex[k]=time.x.y[k+1]-time.x.y[k] T.dl=sum(1-PET.ex[PET.ex¡1]) T.dl mean.ex[j]=(x[1000]+T.dl)/2000 } Th.ex=3600/mean.ex Th.ex mean(Th.ex)

<!-- b000544 | heading | pages [23] -->
1.2 Eﬃciency simulation of CTM

<!-- b000545 | prose | pages [23] -->
k=1 stat.2=matrix(0,2,1000) m=1:1000 for (m in 1:1000) { i=0 j=0 x=0 y=runif(1,0,15) T1=rnorm(1000,15,2) T2=rnorm(1000,15,2)

<!-- b000546 | prose | pages [24] -->
while (max(x,y)¡=3600) { if (x+T1[i+1]¡y+T2[j+1]) { x=max(x+T1[i+1],x+k,y+k) i=i+1 } else { y=max(y+T2[j+1],x+k,y+k) j=j+1 } } stat.2[1,m]=i stat.2[2,m]=j } stat.2 Th.ct=stat.2[1,]+stat.2[2,]-1 Th.ct mean(Th.ct)

<!-- b000547 | heading | pages [24] -->
1.3 Eﬃciency simulation of WAM

<!-- b000548 | prose | pages [24] -->
k=1 stat.3=matrix(0,2,1000) m=1:1000 for (m in 1:1000) { i=0 j=0 x=0 y=runif(1,0,) X=0 Y=0 T1=rnorm(1000,15,2) T2=rnorm(1000,15,2) while (max(X,Y)¡=3600) { if (x+T1[i+1]¡y+T2[j+1]) { X=max(x+T1[i+1],X+k,Y+k) x=x+T1[i+1] i=i+1 }

<!-- b000549 | prose | pages [25] -->
else { Y=max(y+T2[j+1],X+k,Y+k) y=y+T2[j+1] j=j+1 } } stat.3[1,m]=i stat.3[2,m]=j } stat.3 Th.wa=stat.3[1,]+stat.3[2,]-1 Th.wa mean(Th.wa)

<!-- b000550 | heading | pages [25] -->
2 Risk evaluation by simulations

<!-- b000551 | heading | pages [25] -->
2.1 Simulation of existing model

<!-- b000552 | prose | pages [25] -->
x=numeric(1000) y=numeric(1000) mean.ex=numeric(1000) PET.ex=numeric(1999) t1=rnorm(1000,15,2) t2=rnorm(1000,15,2) for (i in 1:1000) { x[i]=sum(t1[1:i]) y[i]=sum(t2[1:i]) time.x.y=sort(c(x,y)) } k=1:1999 PET.ex[k]=time.x.y[k+1]-time.x.y[k] PET.ex

<!-- b000553 | heading | pages [25] -->
2.2 Simulation of CTM

<!-- b000554 | prose | pages [25] -->
k=1 i=0 j=0 x=0 y=runif(1,0,15) T1=rnorm(1100,15,2) T2=rnorm(1100,15,2) X=numeric(1100)

<!-- b000555 | prose | pages [26] -->
Y=numeric(1100) while (i+j¡2000) { if (x+T1[i+1]¡y+T2[j+1]) { x=max(x+T1[i+1],x+k,y+k) i=i+1 } else { y=max(y+T2[j+1],x+k,y+k) j=j+1 } X[i]=x Y[j]=y } i j X=X[which(X¿0)] Y=Y[which(Y¿0)] time.x.y=sort(c(X,Y)) PET.ct=numeric(i+j-1) n=1:(i+j-1) PET.ct[n]=time.x.y[n+1]-time.x.y[n] PET.ct
