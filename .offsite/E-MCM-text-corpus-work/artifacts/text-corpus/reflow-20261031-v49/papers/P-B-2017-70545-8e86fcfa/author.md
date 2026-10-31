For ofﬁce use only For ofﬁce use only

T1 F1 T2 F2 T3 F3 Problem Chosen

T4 F4

2017 MCM/ICM

Summary Sheet

Summary

People around the world are complaining about the trafﬁc jams every day. Some people may spend more than 3 hours on their way from ofﬁce to home everyday on their cars, which makes them frustrated. And our problem is to investigate the methods to optimize the design of toll plazas on highways, especially the area after merging, which is also a possible location where vehicles can be stuck in.

Before establishment of our models, we list some assumptions to make the real life scenario easier to model.

And then we start to analyze the existing models, from which we conclude their strengths and weaknesses. By investigating their characteristics, we get the inspiration to form our two new models: Control Time Model (CTM) and Waiting Area Model(WAM). In these two new models, we introduced a way of conducting control of the departure time of the vehicles at the tollbooths. This kind of control is basically preventing the vehi- cles which are merging in the same lane from leaving the booths simultaneously, which may be a hidden danger for trafﬁc accident or leads to a trafﬁc jam. And we?ll continue to calculate the size and shape of the merging area according to our control methods and some assumptions. After that, we introduce a method for ﬁnding the optimal merging pattern based on both mathematical proof and computer simulations.

After that, we run some simulations to ﬁnd out the throughput, risk and cost of dif- ferent models, which are based on some statistical laws for real life situations. Then we compare these three models in all factors with the help of statistical hypothesis testing, and conclude that the CTM is the best in general. The next section is about some slight modiﬁcation under different conditions such as including the self-driving car, and the different arrangements in terms of merging patterns when the proportion of different types of tollbooths vary.

For the following section, we test our model by investigating the sensitivity of con- struction cost and throughput (per hour) in terms of some variables included in our model, in order to justify the reliability of our model from different perspectives.

Finally, we end our report by the conclusion part followed by strengths and weak- nesses analysis.

PO Box 5042, Woodbridge, NJ 07095-5042.

Dear New Jersey Turnpike Authority,

We are a group of students having conducted a project focusing on solving the problem of merging after tollbooths. And we are sending this letter to let you know the problems that may exist in current toll plaza and suggesting some possible ways to improve it.

First of all, by analyzing the design of existing toll plazas on the highways, we ﬁnd out the following weaknesses of them. At most toll plazas, the vehicles go disorderedly after toll for following reasons. For some toll plazas, there are no leading lines after toll, so drivers just go at their own discretion, thus their routes become unpredictable. And even there are some orientation lines, if two vehicles arrive at the merging point at the same time, only one of them can go through at one time and it will also cause some problems. Disorder after toll leads to both harm to the eﬃciency of the highway entrance and more risk for traﬃc accidents.

Therefore, to solve the above problem, we introduced a new model called “Control Time Model” (CTM). In our model, the releases of cars are controlled at the booth, ensuring that the time interval from any two releases of cars are more that the “safe time”. Therefore, the merging becomes more orderly and safer.

We run some simulations with our models to test and compare the eﬃciency between the CTM and current existing models. The result is that, the eﬃciency of CTM is only slightly smaller than existing model (about 0.6 throughput less per lane per hour), but we haven’t considered the time wasted when accidents happen, which is a lot more likely to take place in existing models theoretically.

And also according to the simulation, the risk of car crashes is also limited to a lower level, which is 13.66% less than current existing models.

In terms of expenditure of construction and maintenance, as our model is much more orderly, the total length of the merging area can be reduced.

Therefore, a decrease in the total expense is expected, let alone the fact that maintenance of plaza could be a lot easier if accident rate decreases distinctively.

All in all, our conclusion is that the CTM performs better than existing models in all aspects including but not limited to eﬃciency, risk elimination as well as total cost. Therefore, it is worthwhile to consider the future construction with our model design.

Thank you for considering our model and wish you a bright future.

Sincerely,

MCM2017

1 Introduction

1.1 Background

Traveling on highways in recent years are quite convenient ways for people to go to another city. With a compared high speed limit on highway, people are able to travel a lot faster. However, building highways are quite expensive and it also takes a lot for the maintenance. Therefore, building of toll plazas along the highway is a common practice all around the world. Meanwhile, there are many factors to be considered during the design and the construction of the tollbooths. Firstly, the lands and the construction fee for the booths and roads are very expensive, so we need to minimize the area. And as the vehicles on the highway always have a high speed, it is also quite dangerous when they want to merge into a lane. Finally, the design of the booths is also supposed to guarantee the eﬃciency, which is described by the quantity throughout the highway for a certain time interval.

1.2 Restatement of the problem

As required by the question, we are supposed to determine the shape, size and merging pattern at the toll plaza depended on number of lanes on the highway in one direction (L) and total number of tollbooths in one direction (B). Meanwhile, we will also justify our approach by comparing it with the existing models in terms of risk, cost and eﬃciency. What’s more, the implement of our plan in various situations (e.g. mixture of the self-driving vehicle and di↵erent proportion distribution of types of tollbooths) will also be shown.

1.3 Literature review

The optimal number of tollbooths needed to minimize the average waiting time is well-studied and simulated based on di↵erent real situations (Corwen et al, 2005). Though the deﬁnition of “optimal” varies, similar suggestions have been given. Tollbooths should be implemented conforming to encouraged behaviors, e.g. faster booths should be put on the left (Spann et al, 2005), which is incorporated in our model. Some literature suggested that tollbooths employ no barrier to ensure a relatively smooth ﬂow (Kane, 2005), but we contend that the uplift of barrier takes negligible amount of time, the beneﬁt of which cannot be compared with the chaos and potential risk if some vehicles go through toll plaza directly. Therefore, barriers are included in our model.

2 Assumptions

To simplify the real life situation, we will make the following assumptions as a start of construction of our models.

• Most of the drivers are rational. They will choose the path as suggested by signals at entrance, and act as risk averters. It is reasonable to make this assumption, because without it, it’s meaningless to make any rules as people won’t obey them.

• The arrival time lapse between the ﬁrst vehicle and the second vehicle in the heavy traﬃc follows uniform distribution. By the heavy traﬃc assumption, the second vehicle comes to tollbooth before the ﬁrst vehicle leaves.

• All the paths of the vehicles follow either constant speed motion or constant acceleration motion. As the average speed for the vehicles around the tollbooths are relatively low.

• vehicles are queuing at the entrance of the tollbooth one by one with low speed in the heavy traﬃc situation . And we further assume them to be stationary in our models.

• The service by human-sta↵s at the tollbooth is quite time-consuming, and the approximate mean service time is around 15 seconds, which follows a normal distribution. This assumption is appropriate, because driver need to bring the fee to the sta↵and the sta↵may need to prepare changes for it. And the time varies from people and di↵erent situations.

• The length of vehicles is omitted during the calculation for the size and shape for the merging area. It is valid because the magnitude of the length of toll plaza is a lot larger than the length of vehicles.

3 Notations

Notation

Deﬁnition Unit L Number of outgoing lanes in highway N/A B Number of tollbooths N/A D Distance between the tollbooth and the end of the plaza m dl Width of the lane in highway m db Width of the lane in tollbooth area m r Radius for vehicles’ turning m Th Time of toll service per vehicle human-sta↵ed tollbooths s t0 Time of control (to be deﬁned in Section 4.2) s vm Speed limit in merging area m/s m/s2 as Starting acceleration of vehicles after toll payment m/s2 ab Deceleration of braking vehicles

4 Models

In this section, we ﬁrst introduce and analyze the existing model, and then two new models invented by us. And the focus for the new models will only be the establishment of the ﬁrst new model (control time model) and second new model (waiting area model) only deviates from the ﬁrst one slightly.

4.1 Existing Model(EM)

Under our investigation, the existing solution for the merging after toll can be roughly divided into two types.

The ﬁrst solution is in short called “no solution”, which doesn’t give the drivers any instruction after toll and let them go at their own discretion. Then the second and more commonly used solution is to instruct the vehicles to merge at some pre-determined merging point.

For the ﬁrst solution, the eﬃciency of it is mainly based on the drivers’ own discretions, which can vary a lot among di↵erent people. And in the light traﬃc situations, this solution may be optimal, for the reason that drivers can go whatever path they what, and in other words their own eﬃciency is maximized. Meanwhile, with the light traﬃc assumption, there are little probability to crash. However, it will be fairly chaotic in heavy traﬃc, because it is very likely that driver’s own optimal path can cross each other. And then they will merge at any point so it is also hard to predict what drivers will do. Therefore, in heavy traﬃc, it is neither eﬃcient nor safe.

And the second solution provides a relatively orderly merging pattern. Vehicles merge at some certain merging points and at least the driving direction is predictable as long as the drivers are rational and always follow the instruction. However, some problems also occur at the merging point. As for most time, the number of tollbooths are larger than the number of lanes on the highway, there always exist the situation that vehicles from several di↵erent booths need to merge into one lane. So di↵erent vehicles from di↵erent booths can arrive at the merging point simultaneously, and then only one of them can get through at a time and others have to wait. This situation can be quite dangerous because drivers always want to go ﬁrst, and it also increase the deﬁciency.

4.2 Control Time Model (CTM)

Given aforementioned deﬁciencies of existing merging pattern, we propose a new model, partially based on the current one. Instead of having all the vehicles moving and merging at their own discretion, control time model will control the departure time of vehicles to ensure a smooth and safe emerging process.

Speciﬁcally, for situations where two booths merge into one lane, the second vehicle will only be allowed to proceed t0 seconds after the ﬁrst vehicle moves forward. The time t0 is deﬁned as the control time. Similarly, for situations where three booths merge into one lane, the third vehicle will be allowed to proceed t0 seconds after the second vehicle moves forward, whilst the second vehicle t0 seconds after the ﬁrst vehicle, as shown in Figure 1 and Figure 2.

In this way, the regulated merging of the vehicles into another lane would be more eﬃcient than the situation where vehicles are proceeding without regulation, for drivers should take time to make decision when multiple booths merge into one lane simultaneously, let alone the risk for doing so.

We model that vehicles start with constant acceleration as until reach the maximum speed vm in the straight path. They then immediately starts merging into their prescribed road in two consecutive tangent circle arcs.

Now we evaluate the “appropriate” control time. When emergency happens, one vehicle take severe brake action with acceleration ab, after response time tres, the posterior vehicle take severe brake action with the same acceleration. Consider the distance of the two vehicles (t = 0 is the time when emergencies happen):

Z t Z t vposterior(t)dt − d = vmtres + vprevious(t)dt 0 0 where

8 t tres > vm, < tres < t tres + vm vm −ab(t −tres), vprevious = (1) ab > : tres + vm 0, ab < t

Solve the equation d ≥0, we get t0 ≥tres. By saying “appropriate” control time, we take t0 = 1s > tres = 0.8s (Lee et al, 2002).

After describing the control time model, we ﬁrst calculate the throughput of the toll plaza.

Let ik be the number of booths corresponding with the kth lane. For example, if the ﬁrst three booths merge into the ﬁrst lane, we say i1 = 3.

By computer simulation (details are included in Appendix), we have tik close to T ik when T ik << t0 (especially when the variance of service time is small), and tik increases as ik increases, and the increase speed is quite large when ik > T t0. where tik is the averaged time for a car to come into kth lane.

Therefore, to maximize the eﬃciency, we’ll keep ik as small as possible, whereas the throughput comes suboptimal if ik > T t0 for some k. The optimal throughput is closed to B T car(s) per second.

By substituting B by 8, the expectation of human service time T by 15. According to our optimization method above, when we keep the ik as small as possible, which is in other words, let them distributed evenly(e.g. {2,3,3}). We will get the optimal throughput closed to B T ⇡0.533 car per second. Then we calculate the size of the plaza, by doing so we discuss the value of D.

Deﬁne f : {1, 2, . . . , B} ! {1, 2, . . . , L} which is non-decreasing, and f(i) = j if and only if vehicles from ith booth merge into jth lane. It obviously follows that ik = kf −1({k})k. We call the mapping f a “merging pattern”.

dB dL Tollbooths

Direction of trafﬁc ﬂow

D

By geometric relations, we have !2 ✓ ◆2 D −v2 r −(i −1 2)dB −(j −1 2)dL) m = r2 2a + 2 2

Observed from above relation, a certain (i, j) prescribes a lower bound of D, and for a certain merging pattern, the distance between the tollbooth and the end of the plaza that we eventually employ is the greatest lower bound of D. The less the greatest lower bound is, the smaller the size will be, and so will the cost of plaza.

By property of quadratic function, for a certain j, the greater i is, the greater D is. We have ! j j X X ikdB −jdL ≥ dB −(k + 1)dL ik + 1 k=1 k=1 since dL > dB. That implies if j is changed into j + 1 whilst i is changed into i + 1, D will get smaller. Therefore, the global maximum must be obtained at one of the local maximum points, and then we let x be ( ) k=1 ik −1 2)dB −(j −1 (Pj 2)dL x = max 2 j2{1,2,...,L} And for given B and L, the optimal choice of merging pattern f would be the case if we can minimize x to be xmin = {ik}2{kf−1({k})k:8f} x min

After trying out some pairs of small (B, L), we induce that for any given small number B, L (which can be put in practical use) satisfying B > L, there exists a merging pattern fm such that x = (B −1 2)dB −(L −1 2)dL) := x0 2 Since for any ik we have the relation f(B) = L, which implies above expression will appear in every calculation of x for all ik, hence xmin ≥x0, hence the existence of x0 guarantees ”=”, providing us with the optimal merging pattern to minimize D.

By substituting B = 8, L = 3, dB = 2.5m, dL = 3.75m, r = 115m, vm = 15m/s, a = 2.78m/s2, the minimum of D is 105.5m, when (i1, i2, i3) 2 {(3, 3, 2), (3, 2, 3), (2, 3, 3)}.

4.3 Waiting Area Model(WAM)

After completing the above model, something seems to be deﬁcient also appears in our model. In the control time model, vehicles may need to wait at the booths even after the service ﬁnished, while there are a lot of vehicles queuing after it. So we wonder that whether it is better to build a waiting area at a plaza (as shown in Figure 5), so that the vehicles whose service has ﬁnished can go to the waiting area, then the consecutive vehicle can be serviced. So in this model, the sta↵spending more time serving instead of doing nothing while the vehicles are just waiting at the booths.

dB dL Waiting area Tollbooths

Direction of trafﬁc ﬂow

D

We will test and compare this model with control time model in the following sections, to see whether it is eﬃcient or not.

5 Analysis and Results

In this section we will analyze throughput, accident prevention and cost of each models introduced in former section.

5.1 Throughput

Throughput (✓) here is deﬁned to be the number of vehicles per hour passing the point where the end of the plaza joins one of the the L outgoing traﬃc lanes. Here we discuss only one outgoing lane merged from two lanes in human-sta↵ed tollbooth area in heavy traﬃc where vehicles come continuously during heavy traﬃc so that the cashier work continually, as shown in Figure 6 .

dL Tollbooths

Direction of traffic flow

D

5.1.1 Throughput of existing model

The toll collection service time is a random variable which can be seen as a sum of random variables including time needed by driver to search money or credit vehicled, time needed by cashier to take related record, etc. According to the central limit theorem, we can assume that the service time of ith vehicle (th,i) of the each lane follow normal distribution with µ = 15 and σ2 = 4 independently and identically.

Th,i ⇠N(15, 4) Suppose the ﬁrst vehicle coming into the tollbooth area at t = 0, then the time of the nth vehicles coming out from a lane tn should equal to the sum of the service time of itself and former vehicles. n X tn = Th,i i=1 As can be seen that tn is the sum of normally distributed random variables, thus

tn ⇠N(15n, 4n) Besides we introduce a concept Post-Encroachment Time (PET) which is deﬁned to be the time lapse between end of encroachment of turning vehicle and the time that the through vehicle actually arrives at the potential point of collision (Gettman & Head, 2003). When PET is less than reaction time, rational drivers would decelerate in order to maintain a safety distance, corresponding to reaction time tr = 1s, with former vehicle. Consequently, more time is needed to pass the merging area which lower the eﬃciency and throughput. Denote PET of ith vehicle as PETi, then total delayed time Td is X (tr −PETi) Td = PETi<tr

Considering the total delayed time Td, the mean time needed of a vehicle coming out from merging area is t = tn + Td 2n Since there are two lanes working simultaneously and assume the motion in the merging area of each vehicle is the same, the throughput of the outgoing lane should be ✓= 3600 t After computer simulation with N = 1000 times, the results are shown in Figure. 7

5.1.2 Throughput of control time model

Now we consider the model with control time (t0). Suppose the nth vehicle coming out from lane a at ta,n with service time Ta,n the mth vehicle coming out from lane b at tb,m with service time Tb,m where Ta,n ⇠N(15, 4) Tb,m ⇠N(15, 4) and Assume the 1st vehicle comes to lane a at t = 0 and after ∆T the 2nd vehicles comes to lane b where ∆T ⇠U(0, 15). If we have ta,n + Ta,n+1 < tb,m + Tb,m+1 which means the (n+1)th vehicle in lane a completes toll collection service before the (m+1)th vehicle in lane b, then

ta,n+1 = max{ta,n + Ta,n+1, ta,n + t0, tb,m + t0} otherwise tb,m+1 = max{tb,m + Tb,m+1, ta,n + t0, tb,m + t0} Set max{ta,n, tb,m} < 3600 in order to simulate time period of one hour. Once if ta,n⇤> 3600 or tb,m⇤> 3600

we can obtain the throughput as ✓= n⇤+ m⇤−1 After computer simulation with N = 1000 times, the results are shown in Figure. x

5.1.3 Throughput of waiting area model

Denote tas,n as the time when nth vehicle completes toll collection and starts to wait in lane b, tbs,m as the time when mth vehicle completes toll collection and starts to wait in lane b. The iteration equations in former section can be adapted to the follows. If

tas,n + Ta,n+1 < tbs,m + Tb,m+1 which means the (n+1)th vehicle in lane a completes toll collection service before the (m+1)th vehicle in lane b, then

ta,n+1 = max{tas,n + Ta,n+1, ta,n + t0, tb,m + t0} otherwise tb,m+1 = max{tbs,m + Tb,m+1, ta,n + t0, tb,m + t0} Set max{ta,n, tb,m} < 3600 in order to simulate time period of one hour. Once if ta,n⇤> 3600 or tb,m⇤> 3600

we can obtain the throughput as ✓= n⇤+ m⇤−1 After computer simulation with N = 1000 times, the results are shown in Figure 7

5.1.4 Comparison and hypothesis tests of throughputs

500

490 Throughput veh/(h·lane) 480

470

460

450

Existing Model Control Time Model Waiting Area Model It can be seen from Figure 7 that the throughputs di↵er slightly among models. Therefore, we conduct hypothesis test for means at 5% level of signiﬁcance.

H0 :There is no di↵erence in average throughputs in existing modeland control time model, i.e. µ1 = µ2 H1 :H0 is wrong, i.e.µ1 6= µ2

Model Size Mean S.d. SEM Existing Model 1000 477.830 4.054 0.128 Control Time Model 1000 477.422 5.843 0.185 Waiting Area Model 1000 479.081 6.039 0.191

di↵erence in means = 477.830 −477.422 = 0.408 p 0.1282 + 0.1852 = 0.225 overall standard error = test statistic = 0.408 0.225 = 1.813 p-value = 0.0348 > 0.025

Therefore, H0 is not rejected at 5% level of signiﬁcance. We conclude that there is no signiﬁcant di↵erence of means of throughputs in existing model and control time model.

However, by similar method, when we make hypothesis test for means of the later two models, the conclusion is that there is signiﬁcant di↵erence of means of throughputs in existing model and control time model.

The analysis of throughputs above lead to the following results:

• Control time mechanism would not lower the eﬃciency and throughput. It just transfer delayed time Td in merging area under existing model to control time t0 in tollbooth area under control time model, as shown in

• Control time mechanism can improve the orderliness of the pattern of vehicles coming out from tollbooth into merging area which thereby improves the safety level of the merging pattern, to be discussed in section 5.2.

• Even though waiting area design could improve throughput, the increment 1.6veh/h is slight compared to the magnitude of throughput. Besides, the cost of land as well as other expense with regard to waiting area can be relatively high. Therefore, the disad- vantageous of waiting area outweigh the beneﬁt it brings so that we should disvehicled this model.

200

Model count Control Time Model Existing Model 100

0 0 5 10 15 20 25 PET

5.2 Accident prevention

This section will analyze accident rate in merging area in terms of PET. When PET is small, it becomes diﬃcult for drivers to make decision promptly to avoid collision, and thus accident is more likely to happen. Therefore, we introduce following function to associate the probability of accident with PET.

p = e−PET (2) 100

When PET = 0, two vehicles arrive the potential point of collision theoretically while drivers could manage speed along the way in order to avoid collision, and hence the probability of collision under this circumstance can be set 0.01. After computer simulation based on the iteration equations with N = 4000 times, the PET of existing model and PET of control time model are shown in Figure 8.

It can be seen that under existing model, a signiﬁcant part of PET lies in the interval [0, 1] where accident is more likely to happen. While under control time model, due to the control mechanism, the minimum PET is control time t0 = 1s which guarantee low accident risk. The expectations of accident rate by simulation on function are shown in Table 2 The control time model can reduce the accident rate by 13.66%. What’s more, the low rate of accident would make vehicles pass merging area without hindrance, which improve eﬃciency and throughput. Therefore, The control time model has better performance in accident prevention than existing model.

Model Accident per 100,000 vehicles Existing Model 53.024 Control Time Model 61.416

5.3 Cost

This section analyzes cost of merging area and tollbooth area, including ﬁxed cost and variable cost per year, i.e. annual operation cost. Fixed cost mainly depends on cost of land and tollbooth construction. We can estimate area of land (A) by supposing the marginal curve of the out-most lane is symmetric, as shown in Figure 9

dL

Tollbooths

Direction of trafﬁc ﬂow D

Tollbooth construction cost can be divided to three kinds including human-sta↵ed, elec- tronic and automated tollbooths.

Fixed cost = 1 2c1A + (chph + cepe + capa)B where A = v2 a Bdb + (Bdb + Ldl)(D −v2 m m 2a ) cl = construction cost of land per m2 ch = construction cost per automated tollbooth ce = construction cost per electronic tollbooth ca = construction cost per human-sta↵ed tollbooth

Substitute B = 8, L = 3, dB = 2.5, dL = 3.75, cl = 172.83, ch = 58500, ce = 15400, ca = 58000 (Pietrzyk,1992), ph = 4/8, pe = 1/8, pa = 3/8 and get ﬁxed cost = $739, 320. Simi- larly, annual operation cost of tollbooth area can be estimated by

Annual operation cost = (c0 2 + c0 hph + c0 epe)B c0 a = operation cost of tollbooth construction and operation per year c0 h = operation cost of salary per cashier c0 e = operation cost of each electronic device Substitute c0 h = 141900, c0 e = 4200, c0 a = 43300 (Pietrzyk,1992), ph = 4/8, pe = 1/8, pa = 3/8 and get annual operation cost = $701, 700.

6 Possible Modiﬁcation

As required in the problem, our report will then proceed to analyze the inﬂuences of some deviation of the conditions on our model. Some possible modiﬁcations may be made to improve the utility of our model in those situations.

6.1 Mixture of autonomous vehicles and human-driving vehicles

With the improvements in artiﬁcial intelligence and vehicle industry recent years, autonomous vehicles have become much more reliable and popular. However, some dangerous occasions may occur as the auto-driving system is not completely stable for all time. Therefore, even in some countries people are allowed to take the autonomous vehicle to the street, there are always required to be a driving sitting on the driver’s seat and prepared to take over at any time.

If autonomous vehicles are allowed on the street, the situation of merging may become much more complicated. Firstly, sometimes the autonomous vehicles fail to detect the mark- ing on the road and therefore go a wrong lane (Sam, 2016). It will be very dangerous if the autonomous vehicle went wrong when merging. Because there are a lot of complicated lanes at the merging area, and some may even cross each other, which are diﬃcult for an autonomous vehicle to recognize and are hard to determine the turning angle accurately.

And one possible solution is to instruct the autonomous vehicles to go to the most left lane. Reason to constraint them to this lane is that the vehicles go through it will just need to go straight till the very end of merging area, which is also the optimal path that the computer will generate even that it fails to detect the signal on the road.

6.2 Change in proportion of di↵erent types of tollbooths

Nowadays, there are roughly 3 di↵erent types of tollbooths, they are conventional (human- sta↵ed), automated and electronic toll collection booths. The main di↵erence among these three di↵erent types is that they have di↵erent service times. The conventional booths have the longest service time, which is around 15 seconds in our assumption. And the automated ones have the second longest service time, and we assume it to be around 8 seconds. Meanwhile, vehicles equipped with ETC transponder are able to pass the ETC booths even without stop (with a maximal passing speed of 15mph).

The model we introduced before works out quite good for both conventional and auto- mated booths as explained before. However, it may not work well with ETC since they don’t need to stop at the booth. First of all, one thing that we would like to classify is that the proportion of ETC booths will be at either a minority or majority position. It is because that the estimated capacity of a single ETC booth is 2000/h, and this number is much larger than the need now considering the proportion of the drivers who possess a ETC transponder. So if the ETC booths are to be included in a toll plaza, we will place it at the most left lane, as we only need one to satisfy all demands for it. And we will arrange the other booths and lanes with the algorithm we introduced before. Of course, if the users of ETC are going to increase signiﬁcantly in the future, the proportion of ETC booths can also be increased. However, one thing to be noticed is that always one booth merges to one lane on highway, provided that the eﬃciency of ETC booths are high and we do not need to increase the number of booths, which will only make it riskier when merging.

7 Sensitivity test

This section conducts sensitivity tests of throughput and cost. We deﬁne the sensitivity of dA a function A(X) in terms of X to be X . If A is a discrete function, we change dA into A dX ∆A = A(X + 1) −A(X).

7.1 Sensitivity test of throughput

-2.0 0.10 Sensitivity of throughput Sensitivity of throughput -1.0 0.00

0.0 -0.10 0 1 2 3 4 0 1 2 3 4 Mean of service time Standard deviation of service time

As shown in 10, the sensitivity of throughput in terms of mean of service time T is a constant −1. Recall that in section 4.2, the optimal throughput is ✓= B T The inverse ratio relationship of ✓and T implies unit constant sensitivity of ✓with respect to T, which is consistent with sensitivity test result. Besides, due to the law of large number, the volatility of service time ﬁnally performs slight e↵ects on throughput and thus the sensitivity is zero.

7.2 Sensitivity test of ﬁxed cost

By our assumption stated in Section 4.2 that the greatest lower bound is provided by the most outside lane and booth, combined with the formula to calculate the ﬁxed cost, we get

Fixed cost = 1 2c1A + (chph + cepe + capa)B

The initial value of

(vm, a, B, L, dB, dL, pa, pe, ph, cl, ce, ch, ca) =(15, 2.78, 8, 3, 2.5, 3.75, 3/8, 1/8, 4/8, 172.84, 15400, 58500, 58000)

We calculate the sensitivity of the ﬁxed cost with respect to the number of booths B, we get the graph as following And it shows that the the sensitivity of B around 8 is about 1.15 and

Sensitivity of Fixed Cost Sensitivity of Fixed Cost Sensitivity of Fixed Cost 0.20 0.7 1.4 0.6 1.3 0.5 0.15 0.4 1.2 0.3 0.10 0.2 1.1 0.1 r v B 100 150 200 250 300 6 8 10 12 14 16 18 20 3 5 6 7 8 9 10

always above 1, and the decreasing speed is very low, which means that D is always sensitive in terms of B. So increasing B can have signiﬁcant inﬂuence on D, and we may need to evaluate more whether to build more booths considering the balance of cost and eﬃciency.

Similarly, we can calculate the sensitivity of ﬁxed cost with respect to vm and r(as shown in the Figure 11).

The sensitivity of vm around 0.38, and it remains below 1 as it vary from 10m/s to 20m/s, which shows that the cost is not sensitive to the speed limit. So our cost estimation should be roughly correct with slight deviation with vm. Finally, with similar analysis, sensitivity in terms of r is always around 0.1 and 0.2 from 50m to 200m. So the radius only have little inﬂuence on our ﬁnal result.

8 Conclusion

In Section 4 we describe three models, namely existing models, CTM, WAM. By simulation in Section 5, we discard WAM and point out the deﬁciencies of EM model and employ CTM. Therefore, the following conclusion is based on CTM.

The shape of the plaza should enable cars from every booth to merge into its prescribed lane with two consecutive arcs. By the assumption stated in Section 4.2, the shape of the plaza is determined by the most outside booth merging into the most outside lane. The boundary should make sure that the most outside vehicles have suﬃcient space on its right side. Take the example of B = 8, L = 3, the shape and merging pattern are as follows.

dB dL Tollbooths

Direction of trafﬁc ﬂow

D

Note that in no case will cars from di↵erent booths merge into one lane simultaneously as is stated in our control time model, so it does not matter whether the distance between two adjacent trajectories merging into one lane becomes smaller or not. Additionally, leading lines should be drawn on the ground to ensure that vehicles take intended paths.

The size of merging area is given by formula A = v2 a Bdb + (Bdb + Ldl)(D −v2 m m 2a ) for one direction. This includes the acceleration paths (the left term) and merging (turning) paths (the right term). Multiply it by a factor 2 if we are to calculate for two directions. For the above example B = 8, L = 3, the area for one direction is 1824.93m2 In heavy traﬃc (deﬁned as the situation where there is at least one car at every service booths), the throughput of plaza is approximately 3600B/T vehicles per hour (if all the toll- booths are human-sta↵ed) , computed by induction of computer simulation. By substituting B = 8, Th = 15, we get 1920 vehicles per hour from human-sta↵ed lanes. In light traﬃc, the throughput is less than 3600B/T. Overall, there is no statistical signiﬁcant of di↵erence between throughput of CTM and existing model. This comparison does not include the con- sideration of accident. If we take into account the fact that CTM reduces the accident rate by 13.66% and that accident is likely to cause traﬃc jam and reduce toll plaza’s throughput, the superiority of CTM would be more distinct. The cost of construction (ﬁxed cost) and operation (variable cost) of the merging area and tollbooth area are calculated respectively. The ﬁxed cost is given by the formula Fixed cost = 1 2c1A + (chph + cepe + capa)B the denotation is given in Section 5.3. In the B=8, L=3 example, the ﬁxed cost is $739320. The annual cost is given by similar formula Annual operation cost = (c0 2 + c0 hph + c0 epe)B

which, in our example, turns to be $701, 700 per year.

9 Strengths and Weaknesses

9.1 Strengths

By computer simulation, as the expression of throughput ✓only contains the number of booths B and service time T, the employment of regulation in control time model does not reduce the throughput of the plaza (control time t0 is not in the expression). However, the risk of accident decreases to a great extent, which ensures a safe and smooth ﬂow of vehicles.

Moreover, we consider service time T following normal distribution instead of assuming a constant, which can better approximate real situation. Additionally, the control time mech- anism could decrease the size of merging area compared with existing model where vehicles merge at their discretion. Last but not least, we use multiple programming platforms to run computer simulations (Mathematica, MATLAB and R), which provides us with accurate and convincing data to support our models.

9.2 Weaknesses

We assume the vehicles adopt two tangent uniform circular motion to merge into its pre- scribed lane, which may not be the real trajectory of vehicles. However, we can draw some leading lines on the ground to guide vehicles. Additionally, we do not consider the situation where vehicles break down and block certain booths and/or lanes.

The arrival of vehicles should follow Poisson distribution, but as we did not have the real- world data to estimate λ, we instead assume that the di↵erence of two consecutive vehicles’ arrival follows a uniform distribution, which may lead to some inaccuracies. This problem, together with the diﬃculties to determine the expectation and variance of service time T, could be addressed if data collected in real-world situation could be provided.

Appendix

Some useful codes in R

1. Eﬃciency simulations

1.1 Eﬃciency simulation of existing model

x=numeric(1000) y=numeric(1000) mean.ex=numeric(1000) PET.ex=numeric(1999) for (j in 1:1000) { t1=rnorm(1000,15,4) t2=rnorm(1000,15,4) for (i in 1:1000) { x[i]=sum(t1[1:i]) y[i]=sum(t2[1:i]) time.x.y=sort(c(x,y)) } k=1:1999 PET.ex[k]=time.x.y[k+1]-time.x.y[k] T.dl=sum(1-PET.ex[PET.ex¡1]) T.dl mean.ex[j]=(x[1000]+T.dl)/2000 } Th.ex=3600/mean.ex Th.ex mean(Th.ex)

1.2 Eﬃciency simulation of CTM

k=1 stat.2=matrix(0,2,1000) m=1:1000 for (m in 1:1000) { i=0 j=0 x=0 y=runif(1,0,15) T1=rnorm(1000,15,2) T2=rnorm(1000,15,2) while (max(x,y)¡=3600) { if (x+T1[i+1]¡y+T2[j+1]) { x=max(x+T1[i+1],x+k,y+k) i=i+1 } else { y=max(y+T2[j+1],x+k,y+k) j=j+1 } } stat.2[1,m]=i stat.2[2,m]=j } stat.2 Th.ct=stat.2[1,]+stat.2[2,]-1 Th.ct mean(Th.ct)

1.3 Eﬃciency simulation of WAM

k=1 stat.3=matrix(0,2,1000) m=1:1000 for (m in 1:1000) { i=0 j=0 x=0 y=runif(1,0,) X=0 Y=0 T1=rnorm(1000,15,2) T2=rnorm(1000,15,2) while (max(X,Y)¡=3600) { if (x+T1[i+1]¡y+T2[j+1]) { X=max(x+T1[i+1],X+k,Y+k) x=x+T1[i+1] i=i+1 } else { Y=max(y+T2[j+1],X+k,Y+k) y=y+T2[j+1] j=j+1 } } stat.3[1,m]=i stat.3[2,m]=j } stat.3 Th.wa=stat.3[1,]+stat.3[2,]-1 Th.wa mean(Th.wa)

2 Risk evaluation by simulations

2.1 Simulation of existing model

x=numeric(1000) y=numeric(1000) mean.ex=numeric(1000) PET.ex=numeric(1999) t1=rnorm(1000,15,2) t2=rnorm(1000,15,2) for (i in 1:1000) { x[i]=sum(t1[1:i]) y[i]=sum(t2[1:i]) time.x.y=sort(c(x,y)) } k=1:1999 PET.ex[k]=time.x.y[k+1]-time.x.y[k] PET.ex

2.2 Simulation of CTM

k=1 i=0 j=0 x=0 y=runif(1,0,15) T1=rnorm(1100,15,2) T2=rnorm(1100,15,2) X=numeric(1100) Y=numeric(1100) while (i+j¡2000) { if (x+T1[i+1]¡y+T2[j+1]) { x=max(x+T1[i+1],x+k,y+k) i=i+1 } else { y=max(y+T2[j+1],x+k,y+k) j=j+1 } X[i]=x Y[j]=y } i j X=X[which(X¿0)] Y=Y[which(Y¿0)] time.x.y=sort(c(X,Y)) PET.ct=numeric(i+j-1) n=1:(i+j-1) PET.ct[n]=time.x.y[n+1]-time.x.y[n] PET.ct
