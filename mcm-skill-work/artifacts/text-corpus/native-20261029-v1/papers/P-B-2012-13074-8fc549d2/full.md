# P-B-2012-13074-8fc549d2

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
team13074                                                       page 1of20

<!-- b000002 | prose | pages [1] -->
Best schedule to utilize the Big Long River

<!-- b000003 | heading | pages [1] -->
1 Introduction

<!-- b000004 | prose | pages [1] -->
People enjoy going to the Big Long River for its scenic views and exciting white water rapids, and the only way to achieve this should be to take a river trip that requires several days of camping, since the river is inaccessible to hikers. So far the rise in popularity of river rafting has made it imminent for the park managers to look for a better way to utilize the river in terms of its traveling value. In other words, there is a need for an optimal schedule to use all the campsites on the river. However, this is not an easy question when taking in account of tourists’ requirements for a wilderness experience. Specifically, a basic rule for the arrangement of the river trips should be that no two sets of campers could occupy the same campsite at the same time in order to guarantee tourists minimal contact with other groups of tourists. As given in the problem set, X river trips are currently available each year during a six month period (the rest of the year it is too cold) on the Big Long River. All river trips start at First Launch and exit at Final Exit, 225 miles downstream. There are Y campsites on the river, distributed approximately uniformly throughout the river corridor. The trips differ in mainly two aspects. The first is the ship propulsion, with either oar-powered rubber rafts (average 4 mph) or motorized boats (average 8 mph). The second is the trip duration, ranging from 6 days to 18 days. What we are supposed to accomplish are to develop the best schedule and to determine the carrying capacity of the river. We have examined many policies for different river trips (including Grand Canyon in Arizona, the U.S., Wolf River in Winconsin, the U.S., and Missinaibi river in Canada) and concluded that river agency typically sets the schedule with given trip dates and types for prospect tourists to choose from, while the specific route of a given trip is up to the tourists in order to provide them with flexibility and freedom. (Note that only the campsites where the ship stops matters in the problem, and we will use the word route to denote the campsites throughout the paper.) Also tourists usually take sleep at the campsites and go on along the river in the day, so they only travel in the downstream direction and spend only one night at a certain campsite. We regard the carrying capacity of the river as the maximum total number of trips available each year, hence turning the task of the river managers into looking for the best schedule itself. Given the actual practice mentioned in the previous paragraph, we want to develop mainly three types of schedules, in terms of the flexibility of the trips. In the part 1, we will design a schedule with fixed trip dates and types and also routes. In the part 2, we design a schedule with fixed trip dates and types but unrestrained routes. In the part 3, we design a schedule with fixed trip dates but unrestrained types and routes. As one can imagine, the maximum number of trips should decline in the order of three schedules because of less control on travelers’ trips, and the final choice of the three schedules should be up to the managers, with consideration of commercial and management issues.

<!-- b000005 | heading | pages [1] -->
2 Definitions

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [2] -->
team13074                                                       page 2of20

<!-- b000008 | prose | pages [2] -->
(1) “optimal”: it means to best utilize all the campsites and maximize the total

<!-- b000009 | prose | pages [2] -->
number of trips in a six months period. (2) “route”: it means the campsites at which tourists choose to stop in a given trip. (3) “orbit”: it means a specific campsite set that allows some certain trip types to

<!-- b000010 | prose | pages [2] -->
travel in. (4) For better description we assign a natural number to every campsite in the

<!-- b000011 | prose | pages [2] -->
downstream direction, from 0 to Y+1. (5) For better description we assign a natural number to every trip type, from 1 to 26,

<!-- b000012 | prose | pages [2] -->
as shown in the following chart.

<!-- b000013 | furniture | pages [2] -->


<!-- b000014 | prose | pages [2] -->
6 7 8 9 10 11 12 13 14 15 16 17 18 Oar-powered 1 3 5 7 9 11 13 15 17 19 21 23 25 Motorized 2 4 6 8 10 12 14 16 18 20 22 24 26 Chart1 The numbered list of trip types (6) We use 𝐴𝑖 to denote the average time tourists travel per day for a certain trip

<!-- b000015 | prose | pages [2] -->
type i. (7) We use 𝑛𝑖 to denote the number of campsites in every orbit corresponding to

<!-- b000016 | prose | pages [2] -->
trip type i. (8) We use 𝑚𝑖 to denote the number of trips in a six months period for a certain

<!-- b000017 | prose | pages [2] -->
trip type i.

<!-- b000018 | heading | pages [2] -->
3 Specific formulation of problem

<!-- b000019 | prose | pages [2] -->
We denote the river and the campsites along it using a straight segment with Y uniformly distributed points in it. Time is measured in day units. The total time period is 180 days (six months). Passengers choose to stay at a different point every day downstream the segment. Here our paper will focus on three sub questions. In part 1, passengers have to travel along the rigid route set by river agency, so the problem should be to come up with the schedule to arrange for the maximum number of trips without occurrence of two different trips occupying the same campsite on the same day. In part 2, passengers have the freedom to choose which campsites to stop at, therefore the mathematical description of their actions inevitably involve randomness and probability, and we actually use a probability model. The next campsite passengers choose at a current given campsite is subject to a certain distribution, and we describe events of two trips occupying the same campsite by probability. Note in probability model it is no longer appropriate to say that two trips do not meet at a campsite with certainty; instead, we regard events as impossible if their probabilities are below an adequately small number. Then we try to find the optimal schedule. In part 3, passengers have the freedom to choose both the type and route of the trip; therefore a probability model is also necessary. We continue to adopt the probability description as in part 2 and then try to find the optimal schedule.

<!-- b000020 | heading | pages [2] -->
4 Assumptions

<!-- b000021 | prose | pages [2] -->
We make following assumptions:

<!-- b000022 | furniture | pages [2] -->


<!-- b000023 | furniture | pages [3] -->
team13074                                                       page 3of20

<!-- b000024 | prose | pages [3] -->
①Passengers may not travel back to previous campsite, namely they can only go in downstream direction. ②Passengers can only stay at a certain campsite for one day. ③Time is measured in day units and the time traveling from one campsite to another should always be less than 24 hours (one day) since passengers need to settle at a campsite every night. ④Passengers typically spend half of a day on the river everyday and according to reference we arbitrarily set the time passengers can travel on the river is 8 hours per day. ⑤In part 2 and part 3, we need to assign the route of a given trip with a probability distribution, and we assume it is classical probability, which means all possible routes for a certain trip share the same probability. In fact, this assumption is reasonable not only because the classical probability can be accepted in reality, but also that it is convenient to replace with other given distributions and the model still works in the same way. In terms of simplification, however, we only use the classical probability in part 2 and part 3 to demonstrate our model. ⑥As we need to define the happening of the event of two trips occupying the same campsite in part 2 and part 3, we choose the standard widely used in Probability and Statistics that a small probability event can be considered as not happening in the stochastic sense. Specifically, we choose the small probability to be below 0.05, 0.025. ⑦As Y is given in the problem, our schedule need to be feasible for different values of Y. In terms of simplicity, we let Y=150 when precise calculation is needed to further illustrate the model. (According to the reference, we choose the number of campsites in Grand Canyon in Arizona, namely 150, for the approximate value of Y, since the length of the Grand Canyon River is also 225 miles which is compatible with the Big Long River in the problem.)

<!-- b000025 | heading | pages [3] -->
5 Part 1 Best schedule of trips with fixed dates, types and also routes.

<!-- b000026 | heading | pages [3] -->
5.1 Method

<!-- b000027 | prose | pages [3] -->
5.1.1 Motivation and justification Although most river agencies do not use fixed trip routes to passengers in order to provide with more flexibility, there is still necessity to first discuss the schedule if trip dates, types and routes are all fixed by river agency, since less flexibility for passengers allow more possible space to arrange trips. Therefore we expect this kind of schedule to achieve the highest number of river trips. The special assumptions for this part are rather self-explanatory. Passengers need to obey the trip dates, types and routes prescribed by the river agency. 5.1.2 Key ideas To best utilize the campsites on the river, it is obvious that we should minimize the total number of days of all campsites when no ship occupying them. In other word, we are to use the trips to occupy as many campsites as possible as long as no two

<!-- b000028 | furniture | pages [3] -->


<!-- b000029 | furniture | pages [4] -->
team13074                                                       page 4of20

<!-- b000030 | prose | pages [4] -->
trips occupy the same campsite at the same day. We divide the schedule problem into three subparts. First (see 5.2.1) we assign a specific set of campsites to every type of trips and no two different campsite sets intersect, then we only need to find the best schedule of every type of trip within corresponding campsite set. Second (see 5.2.2) we discuss the situation where Y is relatively small, and we continue the idea by assigning a specific campsite set to every group of trip types. The schedules for the situations where one group contains two and three trip types are given respectively. Third (see 5.2.3) we further develop the idea to only divide into two campsite sets for the case when Y is very small. Finally we finish the discussion of best schedule for different values of Y and come up with an exact schedule when Y=150 in 5.2.2.

<!-- b000031 | furniture | pages [4] -->


<!-- b000032 | prose | pages [4] -->
Chart2 brief description of the model Note for brief description of the model, we will denote every specific campsite set with the word “orbit” throughout the paper.

<!-- b000033 | heading | pages [4] -->
5.2 Development of the model

<!-- b000034 | prose | pages [4] -->
To begin with, we find out the number of trip types available. As for every trip type i, we calculate the average time needed for driving the ship per day and denote it with𝐴𝑖. According to assumption 4.④ (Passengers drive the ship at most 8 hours a day), the trip type is possible iff 𝐴𝑖≤8. Therefore trip type 1 (oar-powered, 6 days) and trip type 3 (oar-powered, 7 days) are crossed out. But here we allow the trip type 3 in the schedule to maximize the total number of trips,

<!-- b000035 | prose | pages [4] -->
225

<!-- b000036 | prose | pages [4] -->
since 𝐴3 =

<!-- b000037 | prose | pages [4] -->
4∗7 = 8.03 is really close to 8.

<!-- b000038 | prose | pages [4] -->
Consequently there are altogether 25 trip types available. 5.2.1 Every campsite set for every single trip type We will discuss the situation where Y is big enough here. (ⅰ)Dividing into separate campsite sets We now have 25 trip types and we assign them with campsite sets using a rather simple way. Put the campsites whose remainders divided by 25 are the same into one campsite set and sequentially assign the 25 campsite sets to 25 trip types.

<!-- b000039 | prose | pages [4] -->
𝑌

<!-- b000040 | prose | pages [4] -->
Therefore every campsite set contains

<!-- b000041 | prose | pages [4] -->
25 campsites.

<!-- b000042 | prose | pages [4] -->
As we can see from the chart below, the distance between two adjacent campsites in

<!-- b000043 | furniture | pages [4] -->


<!-- b000044 | furniture | pages [5] -->
team13074                                                       page 5of20

<!-- b000045 | prose | pages [5] -->
25

<!-- b000046 | prose | pages [5] -->
a specific orbit is less than the length of what we call an interval = (

<!-- b000047 | prose | pages [5] -->
𝑌∗225)miles.

<!-- b000048 | prose | pages [5] -->
(ⅱ)Best schedule for a certain campsite set There are altogether 25 orbits and we are going to demonstrate the schedule of orbit for trip type 3 only, since the schedules of other orbits are rather similar with the entirely identical designing idea. Now that for trip type 3, we first calculate the maximum number of intervals (denoted by Q) that the trip can cover in a day. Passengers can row the boat at most 8 hours per day and trip type 3 travels at the velocity of 4 mph, so trip type 3 travels

<!-- b000049 | prose | pages [5] -->
32∗𝑌

<!-- b000050 | prose | pages [5] -->
25∗225].

<!-- b000051 | prose | pages [5] -->
8 ∗4 = 32miles per day. ThereforeQ = [

<!-- b000052 | prose | pages [5] -->
Now consider the best schedule. To best utilize all campsites means to minimize the number of total days of empty campsites. We call the very first trip that ever comes into the river “leader”, and apparently the campsites are by no means occupied if they cannot be reached by the “leader” traveling in the fastest way possible. We call these campsites “forgone loss” for the time being. Therefore if we come up with a schedule that occupied every campsite every day except these “forgone loss”, then it must be the best schedule. As for minimizing the number of “forgone loss”, the “leader” should travel Q every day from the beginning until it cannot. For every day we let Q trips come into the river to occupy all of the campsites in front of the leader’s campsite and they just copy the leader’s route and get to Final Exit the same day with “leader”. For only several days the arrangement forms a cycle and the schedule just continues to copy the cycle.

<!-- b000053 | prose | pages [5] -->
𝑆𝑡𝑎𝑟𝑡→𝑄→2𝑄→⋯→𝑧𝑄𝑄→𝑧𝑄𝑄+ (𝑄−1) →𝑧𝑄𝑄+ 2(𝑄−1) →⋯

<!-- b000054 | prose | pages [5] -->
𝑄

<!-- b000055 | prose | pages [5] -->
𝑄

<!-- b000056 | prose | pages [5] -->
𝑄

<!-- b000057 | prose | pages [5] -->
→𝑧𝑄𝑄+ 𝑧𝑄−1(𝑄−1) →⋯→∑𝑧𝑖𝑖

<!-- b000058 | prose | pages [5] -->
where

<!-- b000059 | prose | pages [5] -->
𝑄

<!-- b000060 | prose | pages [5] -->
∑𝑧𝑖𝑖

<!-- b000061 | prose | pages [5] -->
𝑖=1

<!-- b000062 | prose | pages [5] -->
𝑄

<!-- b000063 | prose | pages [5] -->
+ 1 →∑𝑧𝑖𝑖

<!-- b000064 | prose | pages [5] -->
+ 2 →⋯→∑𝑧𝑖𝑖

<!-- b000065 | prose | pages [5] -->
→𝑒𝑛𝑑

<!-- b000066 | prose | pages [5] -->
𝑖=2

<!-- b000067 | prose | pages [5] -->
𝑖=2

<!-- b000068 | prose | pages [5] -->
𝑖=1

<!-- b000069 | prose | pages [5] -->
= 𝑛𝑖

<!-- b000070 | prose | pages [5] -->
= 𝑑𝑢𝑟𝑎𝑡𝑖𝑜𝑛−1

<!-- b000071 | prose | pages [5] -->
∑𝑧𝑖

<!-- b000072 | prose | pages [5] -->
𝑖=1

<!-- b000073 | prose | pages [5] -->
𝑄

<!-- b000074 | prose | pages [5] -->
𝑄

<!-- b000075 | prose | pages [5] -->
𝑗−1

<!-- b000076 | prose | pages [5] -->
∑𝑧𝑖𝑖+ 𝑗+ (𝑑𝑢𝑟𝑎𝑡𝑖𝑜𝑛−2 −∑𝑧𝑖

<!-- b000077 | prose | pages [5] -->
𝑖=𝑗

<!-- b000078 | prose | pages [5] -->
𝑖=𝑗

<!-- b000079 | prose | pages [5] -->
)

<!-- b000080 | prose | pages [5] -->
> ∑𝑧𝑖𝑖

<!-- b000081 | prose | pages [5] -->
𝑗= 2,3, ⋯, 𝑄

<!-- b000082 | prose | pages [5] -->
𝑖=1

<!-- b000083 | prose | pages [5] -->
In case of being confused by our awkward description, see the following illustration of the schedule where Y=425 as an example.

<!-- b000084 | furniture | pages [5] -->


<!-- b000085 | furniture | pages [6] -->
team13074                                                       page 6of20

<!-- b000086 | furniture | pages [6] -->


<!-- b000087 | prose | pages [6] -->
Chart3 Schedule where Y=425 (ⅲ)Arrangement of separate campsite sets if the proportions of all trip types are given As shown above in chart3, the number of “forgone loss” can be ignored compared with the total number of days available of all campsites, namely180 ∗Y. In other word, the schedule enables the trips to occupy nearly all campsites for all days in a six months period, and obviously it can be regarded as the best schedule. Furthermore, if we ignore the “forgone loss” and the total number of a specific trip

<!-- b000088 | prose | pages [6] -->
180∗𝑛𝑖

<!-- b000089 | prose | pages [6] -->
type i can be calculated as𝑚𝑖= [

<!-- b000090 | prose | pages [6] -->
𝑑𝑢𝑟𝑎𝑡𝑖𝑜𝑛 𝑜𝑓 𝑡𝑦𝑝𝑒 𝑖]. Therefore 𝑛𝑖can be determined

<!-- b000091 | prose | pages [6] -->
by 𝑚𝑖. We can now design a schedule with given proportions of all trip types. This is because: Given proportions of all trip types→the ratio of the total number of any two trip

<!-- b000092 | prose | pages [6] -->
𝑚𝑖

<!-- b000093 | prose | pages [6] -->
𝑛𝑖

<!-- b000094 | prose | pages [6] -->
𝑚𝑗→the ratio of the campsites

<!-- b000095 | prose | pages [6] -->
types

<!-- b000096 | prose | pages [6] -->
𝑛𝑗

<!-- b000097 | prose | pages [6] -->
→combine with ∑𝑛𝑖 = 𝑌→𝑛𝑖 𝑖 (Note this makes sense because the river agency is supposed to provide with a variety of trip types and the flexibility to control the proportions of all trip types is even more meaningful, since the river agency can refer to historical data and design a schedule with proportions of all trip types compatible with previous demands of tourists.) Therefore we only need to design a schedule to allocate all Y campsites to 𝑛𝑖orbits respectively.

<!-- b000098 | furniture | pages [6] -->


<!-- b000099 | furniture | pages [7] -->
team13074                                                       page 7of20

<!-- b000100 | prose | pages [7] -->
Apparently an orbit in which the trip type can travel between any two adjacent campsites in a day can accommodates with a schedule similar to (ⅱ). Here the “leader” still travels in the fastest way every day and other trips follow the “leader” occupy all campsites in front of the leader’s campsite, and this schedule makes nearly all campsites occupied every day throughout the six months period. Now we only need an allocation satisfying that for every orbit the trip type can travel between any two adjacent campsites in a day. Note for a subset of orbit, if the trip can already travel between any two adjacent campsites in it, then the trip must be able to travel between any two adjacent campsites in the whole orbit. Call this subset a “skeleton orbit” and we only need to find the allocation of skeleton orbits now. Consider the trip types in the order from the maximum 𝐴𝑖to the minimum𝐴𝑖. Asmin𝐴𝑖= 𝐴3, we consider trip type 3 first. Apparently the following six campsites constitute the skeleton orbit of trip type 3, as shown in the chart:

<!-- b000101 | furniture | pages [7] -->


<!-- b000102 | prose | pages [7] -->
Chart4 Skeleton orbit of trip type3 Since𝐴𝑖≥𝐴3, for any trip type i, it can also travel the distance of two adjacent

<!-- b000103 | prose | pages [7] -->
(𝑌+1)

<!-- b000104 | prose | pages [7] -->
campsites in the skeleton orbit of type 3 in a day, so seven campsites (k,

<!-- b000105 | prose | pages [7] -->
+ 7

<!-- b000106 | prose | pages [7] -->
2(𝑌+1)

<!-- b000107 | prose | pages [7] -->
3(𝑌+1)

<!-- b000108 | prose | pages [7] -->
4(𝑌+1)

<!-- b000109 | prose | pages [7] -->
5(𝑌+1)

<!-- b000110 | prose | pages [7] -->
6(𝑌+1)

<!-- b000111 | prose | pages [7] -->
𝑘,

<!-- b000112 | prose | pages [7] -->
+ 𝑘,

<!-- b000113 | prose | pages [7] -->
+ 𝑘,

<!-- b000114 | prose | pages [7] -->
+ 𝑘,

<!-- b000115 | prose | pages [7] -->
+ 𝑘,

<!-- b000116 | prose | pages [7] -->
+ 𝑘, k = 1,2,… 2 ) constitute

<!-- b000117 | prose | pages [7] -->
7

<!-- b000118 | prose | pages [7] -->
7

<!-- b000119 | prose | pages [7] -->
7

<!-- b000120 | prose | pages [7] -->
7

<!-- b000121 | prose | pages [7] -->
7

<!-- b000122 | prose | pages [7] -->
the skeleton orbit of type i, as shown in chart:

<!-- b000123 | furniture | pages [7] -->


<!-- b000124 | prose | pages [7] -->
Chart5 skeleton orbit of typei As long as 𝑛𝑖≥7 holds for all I, other (𝑛𝑖−7)campsites can be chosen casually and finally we have the allocation needed. The schedule here need a basic condition thatY ≥7 + ⋯+ 18 + 6 + 7 + ⋯+ 18 = 306. 5.2.2 Every campsite set for every multiple trip types WhenY < 306, the above schedule becomes invalid. We now consider the allocation where one orbit is for multiple trip types. For simplicity we consider the case where any one orbit contains trip types of the same ship propulsion. For instance, consider the allocation of 13 orbits for 13 groups of trip types as below (the numbers denote the duration of the trip type): Oar-powered ships(7,8),(9,10),(11,12),(13,14),(15,16),(17,18) Motorized ships(6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18) We only demonstrate the schedule for the group (7,8) of oar-powered ships, since the schedule for other groups are similar. The schedule is shown below in the same way as in 5.2.1:

<!-- b000125 | furniture | pages [7] -->


<!-- b000126 | furniture | pages [8] -->
team13074                                                       page 8of20

<!-- b000127 | furniture | pages [8] -->


<!-- b000128 | prose | pages [8] -->
Chart6 schedule when the campsite set is for 2 trip types As one can see, the ratio of the two trip types can also be any number differing from

<!-- b000129 | prose | pages [8] -->
2

<!-- b000130 | prose | pages [8] -->
1 shown in the above example. To achieve this we only need to replace the (7,7,8) in

<!-- b000131 | prose | pages [8] -->
the above schedule with other combination of the two trip types. Therefore similar to 5.2.1, we are able to design the schedule for given proportions of all trip types by designing the schedule for corresponding ratio of every two trip types of the same group. As mentioned in assumption 4⑦, we calculate for the exact schedule when Y=150 in order to illustrate the model. For simplicity we let different trip types distribute uniformly. Similar with 5.2.1, in order to make sure every trip can achieve its duration, we need Y ≥5 + 2(7 + 9 + 11 + 13 + 15 + 17) = 149. As Y=150, a certain trip can cover at most 2 intervals each day, and for most time, a certain trip can only cover 1 interval. Therefore, similar with 5.2.1, we can find out that only 2 days form a cycle. We only present two days’ schedule, and the following days’ schedule can copy the cycle.

<!-- b000132 | furniture | pages [8] -->


<!-- b000133 | furniture | pages [8] -->


<!-- b000134 | furniture | pages [8] -->


<!-- b000135 | furniture | pages [8] -->


<!-- b000136 | furniture | pages [8] -->


<!-- b000137 | furniture | pages [8] -->


<!-- b000138 | furniture | pages [8] -->


<!-- b000139 | furniture | pages [8] -->


<!-- b000140 | furniture | pages [8] -->


<!-- b000141 | furniture | pages [9] -->
team13074                                                       page 9of20

<!-- b000142 | prose | pages [9] -->
date Trip types Trip routes

<!-- b000143 | prose | pages [9] -->
O-7 21, 42, 63, 84, 105, 126

<!-- b000144 | prose | pages [9] -->
O-9 2, 20, 41, 62, 83, 104, 108, 125

<!-- b000145 | prose | pages [9] -->
O-11 6, 19, 28, 40, 61, 66, 82, 103, 112, 124

<!-- b000146 | prose | pages [9] -->
O-13 4, 18, 39, 47, 59, 71, 81, 102, 107, 123, 130, 144

<!-- b000147 | prose | pages [9] -->
O-15 1, 9, 17, 25, 38, 44, 58, 65, 70, 80, 91, 101, 111, 122 O-17 16, 23, 37, 49, 57, 72, 79, 87, 93, 100, 109, 113, 121, 128, 135, 142

<!-- b000148 | prose | pages [9] -->
1

<!-- b000149 | prose | pages [9] -->
M-6 30, 60, 90, 120, 134

<!-- b000150 | prose | pages [9] -->
M-7 15, 36, 56, 78, 99, 119

<!-- b000151 | prose | pages [9] -->
M-9 14, 22, 35, 55, 69, 77, 98, 118

<!-- b000152 | prose | pages [9] -->
M-11 13, 34, 43, 54, 64, 68, 76, 97, 106, 117

<!-- b000153 | prose | pages [9] -->
M-13 7, 12, 33, 45, 53, 67, 75, 96, 110, 116, 129, 133

<!-- b000154 | prose | pages [9] -->
M-15 3, 8, 11, 24, 32, 46, 52, 74, 85, 89, 95, 115, 127, 132

<!-- b000155 | prose | pages [9] -->
M-17 5, 10, 26, 27, 29, 31, 48, 50, 51, 73, 86, 88, 92, 94, 114, 131

<!-- b000156 | prose | pages [9] -->
O-8 21, 42, 63, 84, 105, 126, 147

<!-- b000157 | prose | pages [9] -->
O-10 2, 20, 41, 62, 83, 104, 108, 125, 146 O-12 6, 19, 28, 40, 61, 66, 82, 103, 112, 124, 145

<!-- b000158 | prose | pages [9] -->
O-14 4, 18, 39, 47, 59, 71, 81, 102, 107, 123, 130, 144, 149 O-16 1, 9, 17, 25, 38, 44, 58, 65, 70, 80, 91, 101, 111, 122, 143

<!-- b000159 | prose | pages [9] -->
O-18 16, 23, 37, 49, 57, 72, 79, 87, 93, 100, 109, 113, 121, 128, 135, 142, 148

<!-- b000160 | prose | pages [9] -->
2

<!-- b000161 | prose | pages [9] -->
M-6 30, 60, 90, 120, 134 M-8 15, 36, 56, 78, 99, 119, 141

<!-- b000162 | prose | pages [9] -->
M-10 14, 22, 35, 55, 69, 77, 98, 118, 140 M-12 13, 34, 43, 54, 64, 68, 76, 97, 106, 117, 139

<!-- b000163 | prose | pages [9] -->
M-14 7, 12, 33, 45, 53, 67, 75, 96, 110, 116, 129, 133, 138

<!-- b000164 | prose | pages [9] -->
M-16 3, 8, 11, 24, 32, 46, 52, 74, 85, 89, 95, 115, 127, 132, 137

<!-- b000165 | prose | pages [9] -->
M-18 5, 10, 26, 27, 29, 31, 48, 50, 51, 73, 86, 88, 92, 94, 114, 131, 136 Chart7 The first two days’ schedule In the chart above, in the sign “I j-k”, I stands for the number of the certain trip type, and j stands for the propulsion which O for oar-powered and M for motorized, and k stands for the duration. For example, “3 M-6s” stands for 3 6-night trips of motorized boat.

<!-- b000166 | prose | pages [9] -->
26×180

<!-- b000167 | prose | pages [9] -->
= 2340.

<!-- b000168 | prose | pages [9] -->
The carrying capacity of the river based on the schedule above is

<!-- b000169 | prose | pages [9] -->
2

<!-- b000170 | prose | pages [9] -->
5.2.3 One campsite set for all trip types When Y continues to decline, it is easy to further develop the idea in 5.2.1.and 5.2.2 for new best schedule. Here we only describe the outline. First we design a schedule of orbit containing three trip types. For instance, consider the orbit of the group below: Oar-powered ships: (7,8,9) The corresponding schedule:

<!-- b000171 | furniture | pages [9] -->


<!-- b000172 | furniture | pages [10] -->
team13074                                                       page 10of20

<!-- b000173 | furniture | pages [10] -->


<!-- b000174 | prose | pages [10] -->
Chart8 Schedule for the campsite sets for 3 trip types Then it is similar for schedule of orbit containing m trip types: Oar-powered ships: (n, n+1, n+2, … n+m) Finally it goes to schedule of orbit containing all trip types of the same propulsion. In that case there are only two orbits which contain all trip types of oar-powered and motorized respectively. Note the final schedule can already deal with situation where Y is very small, and we finish the discussion here because we regard situations where Y continues to decrease as of little practical value. (IfY < 18, then passengers of an 18-day trip cannot even spend every day at a different campsite.)

<!-- b000175 | heading | pages [10] -->
6 Part 2 Best schedule of trips with fixed dates and types, but

<!-- b000176 | prose | pages [10] -->
unrestrained routes.

<!-- b000177 | heading | pages [10] -->
6.1 Method

<!-- b000178 | prose | pages [10] -->
6.1.1 Motivation and justification In part 2, we consider trips with fixed dates and types but unrestrained routes to better describe the actual behavior of tourists. In fact, this is the most close-to-reality situation as reference shows that river agency does not fix the route for tourists to provide with more flexibility. So it is natural to come up with a stochastic model. Special assumptions for this part: Here we use classical probability to describe the behavior of tourists’ choice of their own route, which means all possible routes for a given trip type shares the same

<!-- b000179 | furniture | pages [10] -->


<!-- b000180 | furniture | pages [11] -->
team13074                                                       page 11of20

<!-- b000181 | prose | pages [11] -->
probability. Also as mentioned in assumption 4⑥, we regard an event with probability 0.05 as not happening to determine whether two trips occupying the same campsite at the same day. We will use the following symbols and definitions in the description of the model: day is the date of the whole schedule. The original value is 0. f(T,x,t) is the total number of all possible routes from the First Launch to campsite x for trip type T at day t after its launch into the river. p(T,x,t) is the probability of the event that trip type T occupying campsite x at day t after its launch into the river. We will also use the famous Inclusion-exclusion principle in Statistics:

<!-- b000182 | prose | pages [11] -->
n

<!-- b000183 | prose | pages [11] -->
n

<!-- b000184 | prose | pages [11] -->
) = ∑ℙ(Ai)

<!-- b000185 | prose | pages [11] -->
−∑ℙ(Ai ∩Aj)

<!-- b000186 | prose | pages [11] -->
ℙ(⋃Ai

<!-- b000187 | prose | pages [11] -->
i=1

<!-- b000188 | prose | pages [11] -->
i=1

<!-- b000189 | prose | pages [11] -->
i,j: i<j

<!-- b000190 | prose | pages [11] -->
n

<!-- b000191 | prose | pages [11] -->
+ (−1)n−1ℙ(⋃Ai

<!-- b000192 | prose | pages [11] -->
)

<!-- b000193 | prose | pages [11] -->
i=1

<!-- b000194 | prose | pages [11] -->
+ ∑ ℙ(Ai ∩Aj ∩Ak) − ⋯

<!-- b000195 | prose | pages [11] -->
i,j,k: i<j<k

<!-- b000196 | prose | pages [11] -->
Trip(n) is an auxiliary function, where n is the number of the trip added into the schedule, T is the type of the current trip, Day is the date when the trip first launches into the river. q(x,day) is the probability of the event that there exist at least two trips occupying campsite x at the date day. 6.1.2 Key ideas The central idea of this model is the Greedy Algorithm. We add the trips one by one and every trip added is the best choice considering the current circumstances. Specifically the construction of the model can be developed into three subparts. First, we calculate the probability of a given trip occupying a given campsite at a given day after its launch into the river, using the recursive algorithm. Second, we use the Jordan Formula to calculate the probability of two given trips occupying a given campsite at a given day, and then use the minimax principle as the stopping rule for the Greedy algorithm to find the optimal schedule. Third, we consider the optimal schedule for the situation where there are already X trips set in the schedule.

<!-- b000197 | furniture | pages [11] -->


<!-- b000198 | prose | pages [11] -->
Chart9 Brief description of the model

<!-- b000199 | furniture | pages [11] -->


<!-- b000200 | furniture | pages [12] -->
team13074                                                       page 12of20

<!-- b000201 | heading | pages [12] -->
6.2 Development of the model

<!-- b000202 | prose | pages [12] -->
To start with, we find out the number of trip types available. Similar to the calculation in 5.2, but here we consider that the time passengers can travel every day must be rigorously less than 8 hours, therefore trip type 1 (oar-powered, 6 days) and trip type 3 (oar-powered, 7 days) are crossed out. Consequently there are altogether 24 trip types available. When we speak of 26 types below, just think two of them are not exist. 6.2.1 Calculation of p(T,x,t) First we calculate f(T,x,t) for all values of T, x, t. This is easily done with computer using the following recursive formula:

<!-- b000203 | prose | pages [12] -->
f (T,x, 1) = 1        1 ≤T ≤26, 1 ≤x ≤N

<!-- b000204 | prose | pages [12] -->
f (T, y, t −1)       1 ≤T ≤26, 1 ≤x ≤Y, f (T,x, t) = ∑

<!-- b000205 | prose | pages [12] -->
All available y

<!-- b000206 | prose | pages [12] -->
1 < t ≤duration

<!-- b000207 | prose | pages [12] -->
where N is the largest number of campsite sets that the trip T could pass through in one day, and available y means the campsite set, before x, from which the trip T could reach x in one day. Then we have the following probability formula to calculate p(T,x,t) for all values of T, x, t:

<!-- b000208 | prose | pages [12] -->
P(T, x,t) = f (T, x,t) × f (T, Y + 1 −x,duration)

<!-- b000209 | furniture | pages [12] -->


<!-- b000210 | prose | pages [12] -->
f (T, Y + 1, duration)

<!-- b000211 | prose | pages [12] -->
6.2.2 Best schedule using Greedy algorithm When day=1, choose any one trip type as the first trip comes into the river. With the aid of function Trip(n) and Jordan Formula, we can easily calculate q(x,day), where the campsite x ranges from 1 to Y, and the date day ranges from 1 to 18, with all trips already launched into the river are given. Note a trip can last for at most 18 days, so it only exerts an influence on the probabilities in these 18 consecutive days, namely the 18*Y values of all q(x,day). Then according to the minimax principle, we find the minimum value among 26 trip types if added of their maximum of q(x,day) among 18*Y values. According to Greedy algorithm, put the trip type that reaches this minimax value as the trip added. The stopping rule of this process is when the minimax value is larger than 0.05, which means that the event of two trips occupying the same campsite can no longer be seen as small probability event. Then let day=2 and replicate the above process. Until finally day=180 and we get the whole schedule. As mentioned in assumption 4⑦, we calculate for the exact schedule when Y=150 in order to illustrate the model. The whole schedule is shown as the following chart: Sun.

<!-- b000212 | prose | pages [12] -->
Mon.

<!-- b000213 | prose | pages [12] -->
Tues.

<!-- b000214 | prose | pages [12] -->
Wed.

<!-- b000215 | furniture | pages [12] -->


<!-- b000216 | furniture | pages [12] -->


<!-- b000217 | furniture | pages [12] -->


<!-- b000218 | furniture | pages [12] -->


<!-- b000219 | furniture | pages [12] -->


<!-- b000220 | prose | pages [12] -->
Thur.

<!-- b000221 | prose | pages [12] -->
Fri.

<!-- b000222 | prose | pages [12] -->
Sat.

<!-- b000223 | prose | pages [12] -->
Mar.    1

<!-- b000224 | prose | pages [12] -->
2

<!-- b000225 | prose | pages [12] -->
3

<!-- b000226 | prose | pages [12] -->
3 M-6s

<!-- b000227 | prose | pages [12] -->
1 O-8

<!-- b000228 | prose | pages [12] -->
1 O-8

<!-- b000229 | prose | pages [12] -->
8 M-7s

<!-- b000230 | prose | pages [12] -->
1 M-18

<!-- b000231 | prose | pages [12] -->
1 O-12

<!-- b000232 | prose | pages [12] -->
1 M-8

<!-- b000233 | prose | pages [12] -->
1 M-18

<!-- b000234 | prose | pages [12] -->
1 M-16

<!-- b000235 | furniture | pages [13] -->
team13074                                                       page 13of20

<!-- b000236 | prose | pages [13] -->
4

<!-- b000237 | prose | pages [13] -->
5

<!-- b000238 | prose | pages [13] -->
6

<!-- b000239 | prose | pages [13] -->
1 O-11

<!-- b000240 | prose | pages [13] -->
1 O-11

<!-- b000241 | prose | pages [13] -->
1 O-10

<!-- b000242 | prose | pages [13] -->
2 M-6s

<!-- b000243 | prose | pages [13] -->
4 M-6s

<!-- b000244 | prose | pages [13] -->
2 M-6s

<!-- b000245 | prose | pages [13] -->
1 O-15

<!-- b000246 | prose | pages [13] -->
1 M-9

<!-- b000247 | prose | pages [13] -->
1 M-7

<!-- b000248 | prose | pages [13] -->
1 M-7

<!-- b000249 | prose | pages [13] -->
2 M-18s

<!-- b000250 | prose | pages [13] -->
1 M-16

<!-- b000251 | prose | pages [13] -->
1 M-18

<!-- b000252 | prose | pages [13] -->
1 M-14

<!-- b000253 | prose | pages [13] -->
1 M-18

<!-- b000254 | prose | pages [13] -->
1 M-18

<!-- b000255 | prose | pages [13] -->
7

<!-- b000256 | prose | pages [13] -->
8

<!-- b000257 | prose | pages [13] -->
9

<!-- b000258 | prose | pages [13] -->
10

<!-- b000259 | prose | pages [13] -->
1 O-15

<!-- b000260 | prose | pages [13] -->
1 O-16

<!-- b000261 | prose | pages [13] -->
1 O-16

<!-- b000262 | prose | pages [13] -->
1 M-7

<!-- b000263 | prose | pages [13] -->
1 M-9

<!-- b000264 | prose | pages [13] -->
1 M-9

<!-- b000265 | prose | pages [13] -->
2 M-18s

<!-- b000266 | prose | pages [13] -->
2 M-18s

<!-- b000267 | prose | pages [13] -->
2 M-18s

<!-- b000268 | prose | pages [13] -->
14

<!-- b000269 | prose | pages [13] -->
11

<!-- b000270 | prose | pages [13] -->
12

<!-- b000271 | prose | pages [13] -->
13

<!-- b000272 | prose | pages [13] -->
15

<!-- b000273 | prose | pages [13] -->
16

<!-- b000274 | prose | pages [13] -->
17

<!-- b000275 | prose | pages [13] -->
2 O-17s

<!-- b000276 | prose | pages [13] -->
3 M-18s

<!-- b000277 | prose | pages [13] -->
1 O-18

<!-- b000278 | prose | pages [13] -->
1 M-14

<!-- b000279 | prose | pages [13] -->
1 M-10

<!-- b000280 | prose | pages [13] -->
1 M-17

<!-- b000281 | prose | pages [13] -->
1 M-18

<!-- b000282 | prose | pages [13] -->
1 M-18

<!-- b000283 | prose | pages [13] -->
1 M-18

<!-- b000284 | prose | pages [13] -->
1 M-9

<!-- b000285 | prose | pages [13] -->
1 O-15

<!-- b000286 | prose | pages [13] -->
2 O-18s

<!-- b000287 | prose | pages [13] -->
2 M-18s

<!-- b000288 | prose | pages [13] -->
1 O-16

<!-- b000289 | prose | pages [13] -->
1 M-18

<!-- b000290 | prose | pages [13] -->
1 M-18

<!-- b000291 | prose | pages [13] -->
21

<!-- b000292 | prose | pages [13] -->
18

<!-- b000293 | prose | pages [13] -->
19

<!-- b000294 | prose | pages [13] -->
20

<!-- b000295 | prose | pages [13] -->
2 O-18s

<!-- b000296 | prose | pages [13] -->
1 M-7

<!-- b000297 | prose | pages [13] -->
3 O-18s

<!-- b000298 | prose | pages [13] -->
1 O-18

<!-- b000299 | prose | pages [13] -->
1 M-18

<!-- b000300 | prose | pages [13] -->
2 M-18s

<!-- b000301 | prose | pages [13] -->
1 M-14

<!-- b000302 | prose | pages [13] -->
1 M-18

<!-- b000303 | furniture | pages [13] -->


<!-- b000304 | prose | pages [13] -->
22

<!-- b000305 | prose | pages [13] -->
23

<!-- b000306 | prose | pages [13] -->
24

<!-- b000307 | prose | pages [13] -->
2 O-18s

<!-- b000308 | prose | pages [13] -->
1 O-14

<!-- b000309 | prose | pages [13] -->
1 O-18

<!-- b000310 | prose | pages [13] -->
1 M-18

<!-- b000311 | prose | pages [13] -->
2 M-18s

<!-- b000312 | prose | pages [13] -->
28

<!-- b000313 | prose | pages [13] -->
25

<!-- b000314 | prose | pages [13] -->
26

<!-- b000315 | prose | pages [13] -->
27

<!-- b000316 | prose | pages [13] -->
29

<!-- b000317 | prose | pages [13] -->
30

<!-- b000318 | prose | pages [13] -->
31

<!-- b000319 | prose | pages [13] -->
2 O-18s

<!-- b000320 | furniture | pages [13] -->


<!-- b000321 | prose | pages [13] -->
4 O-18s

<!-- b000322 | prose | pages [13] -->
3 O-18s

<!-- b000323 | prose | pages [13] -->
2 O-18s

<!-- b000324 | prose | pages [13] -->
1 O-11

<!-- b000325 | prose | pages [13] -->
1 O-16

<!-- b000326 | prose | pages [13] -->
1 O-18

<!-- b000327 | prose | pages [13] -->
2 O-17s

<!-- b000328 | prose | pages [13] -->
1 O-18

<!-- b000329 | prose | pages [13] -->
4

<!-- b000330 | prose | pages [13] -->
Apr.     1

<!-- b000331 | prose | pages [13] -->
2

<!-- b000332 | prose | pages [13] -->
3

<!-- b000333 | prose | pages [13] -->
2 O-17s

<!-- b000334 | prose | pages [13] -->
1 M-7

<!-- b000335 | prose | pages [13] -->
1 O-16

<!-- b000336 | prose | pages [13] -->
1 O-17

<!-- b000337 | prose | pages [13] -->
1 O-18

<!-- b000338 | prose | pages [13] -->
2 O-17s

<!-- b000339 | prose | pages [13] -->
1 O-18

<!-- b000340 | prose | pages [13] -->
1 O-18 1 M-8

<!-- b000341 | prose | pages [13] -->
5

<!-- b000342 | prose | pages [13] -->
6

<!-- b000343 | prose | pages [13] -->
7

<!-- b000344 | prose | pages [13] -->
4 O-18s

<!-- b000345 | prose | pages [13] -->
2 O-18s

<!-- b000346 | prose | pages [13] -->
2 O-17s 1 O-18

<!-- b000347 | prose | pages [13] -->
11

<!-- b000348 | prose | pages [13] -->
8

<!-- b000349 | prose | pages [13] -->
9

<!-- b000350 | prose | pages [13] -->
10

<!-- b000351 | prose | pages [13] -->
3 O-18s

<!-- b000352 | prose | pages [13] -->
1 O-18

<!-- b000353 | prose | pages [13] -->
3 O-18s

<!-- b000354 | prose | pages [13] -->
1 O-17

<!-- b000355 | prose | pages [13] -->
12

<!-- b000356 | prose | pages [13] -->
13

<!-- b000357 | prose | pages [13] -->
14

<!-- b000358 | prose | pages [13] -->
1 M-18

<!-- b000359 | prose | pages [13] -->
1 O-17

<!-- b000360 | prose | pages [13] -->
3 O-18s

<!-- b000361 | prose | pages [13] -->
3 O-18s

<!-- b000362 | furniture | pages [13] -->


<!-- b000363 | prose | pages [13] -->
1 M-7

<!-- b000364 | prose | pages [13] -->
18

<!-- b000365 | prose | pages [13] -->
15 16

<!-- b000366 | prose | pages [13] -->
17

<!-- b000367 | prose | pages [13] -->
1 O-18 1 O-17

<!-- b000368 | prose | pages [13] -->
1 O-16

<!-- b000369 | furniture | pages [13] -->


<!-- b000370 | prose | pages [13] -->
3 O-18s

<!-- b000371 | prose | pages [13] -->
2 O-18s

<!-- b000372 | furniture | pages [13] -->


<!-- b000373 | prose | pages [13] -->
19

<!-- b000374 | prose | pages [13] -->
20

<!-- b000375 | prose | pages [13] -->
21

<!-- b000376 | prose | pages [13] -->
1 O-18

<!-- b000377 | prose | pages [13] -->
1 O-9

<!-- b000378 | prose | pages [13] -->
4 O-18s

<!-- b000379 | prose | pages [13] -->
1 M-6

<!-- b000380 | prose | pages [13] -->
1 O-17 1 O-18

<!-- b000381 | prose | pages [13] -->
25

<!-- b000382 | prose | pages [13] -->
22 23 24 3 O-18s 1 O-18 3 O-18s

<!-- b000383 | prose | pages [13] -->
1 O-11

<!-- b000384 | prose | pages [13] -->
1 M-7

<!-- b000385 | prose | pages [13] -->
26

<!-- b000386 | prose | pages [13] -->
27

<!-- b000387 | prose | pages [13] -->
28

<!-- b000388 | prose | pages [13] -->
1 O-16

<!-- b000389 | prose | pages [13] -->
1 O-16

<!-- b000390 | prose | pages [13] -->
2 O-18s

<!-- b000391 | prose | pages [13] -->
3 O-17s

<!-- b000392 | prose | pages [13] -->
1 O-17 1 M-10

<!-- b000393 | prose | pages [13] -->
2

<!-- b000394 | prose | pages [13] -->
29

<!-- b000395 | prose | pages [13] -->
30

<!-- b000396 | prose | pages [13] -->
May.    1

<!-- b000397 | prose | pages [13] -->
2 O-18s

<!-- b000398 | prose | pages [13] -->
2 O-17s

<!-- b000399 | prose | pages [13] -->
4 O-18s

<!-- b000400 | prose | pages [13] -->
1 M-18

<!-- b000401 | prose | pages [13] -->
1 O-18

<!-- b000402 | furniture | pages [13] -->


<!-- b000403 | prose | pages [13] -->
3

<!-- b000404 | prose | pages [13] -->
4

<!-- b000405 | prose | pages [13] -->
5

<!-- b000406 | prose | pages [13] -->
3 O-18s

<!-- b000407 | prose | pages [13] -->
1 O-16

<!-- b000408 | prose | pages [13] -->
1 M-7s

<!-- b000409 | prose | pages [13] -->
1 O-17 1 O-18

<!-- b000410 | prose | pages [13] -->
1 M-18

<!-- b000411 | furniture | pages [14] -->
team13074                                                       page 14of20

<!-- b000412 | prose | pages [14] -->
9

<!-- b000413 | prose | pages [14] -->
6 7

<!-- b000414 | prose | pages [14] -->
8

<!-- b000415 | prose | pages [14] -->
1 O-18

<!-- b000416 | prose | pages [14] -->
1 O-17

<!-- b000417 | prose | pages [14] -->
1 O-16

<!-- b000418 | prose | pages [14] -->
10

<!-- b000419 | prose | pages [14] -->
11 12

<!-- b000420 | prose | pages [14] -->
1 O-18

<!-- b000421 | prose | pages [14] -->
3 O-18s 1 O-17

<!-- b000422 | prose | pages [14] -->
2 O-17s

<!-- b000423 | prose | pages [14] -->
1 M-6

<!-- b000424 | prose | pages [14] -->
2 O-18s

<!-- b000425 | prose | pages [14] -->
1 M-7

<!-- b000426 | prose | pages [14] -->
1 O-18

<!-- b000427 | prose | pages [14] -->
1 M-18

<!-- b000428 | prose | pages [14] -->
16

<!-- b000429 | prose | pages [14] -->
13 14

<!-- b000430 | prose | pages [14] -->
15

<!-- b000431 | prose | pages [14] -->
1 O-10 2 O-16s

<!-- b000432 | prose | pages [14] -->
1 O-15

<!-- b000433 | prose | pages [14] -->
1 O-18

<!-- b000434 | prose | pages [14] -->
2 O-17s

<!-- b000435 | prose | pages [14] -->
1 O-16

<!-- b000436 | prose | pages [14] -->
1 O-17

<!-- b000437 | prose | pages [14] -->
1 O-18

<!-- b000438 | prose | pages [14] -->
17

<!-- b000439 | prose | pages [14] -->
18

<!-- b000440 | prose | pages [14] -->
19

<!-- b000441 | prose | pages [14] -->
2 O-18s

<!-- b000442 | prose | pages [14] -->
1 O-17

<!-- b000443 | prose | pages [14] -->
3 O-18s

<!-- b000444 | prose | pages [14] -->
1 M-6

<!-- b000445 | prose | pages [14] -->
3 O-18s

<!-- b000446 | prose | pages [14] -->
23

<!-- b000447 | prose | pages [14] -->
20

<!-- b000448 | prose | pages [14] -->
21

<!-- b000449 | prose | pages [14] -->
22

<!-- b000450 | prose | pages [14] -->
1 O-18

<!-- b000451 | prose | pages [14] -->
3 O-18s

<!-- b000452 | prose | pages [14] -->
1 O-11

<!-- b000453 | prose | pages [14] -->
1 O-16

<!-- b000454 | prose | pages [14] -->
1 M-6

<!-- b000455 | prose | pages [14] -->
1 M-18

<!-- b000456 | prose | pages [14] -->
1 O-17

<!-- b000457 | prose | pages [14] -->
24

<!-- b000458 | prose | pages [14] -->
25

<!-- b000459 | prose | pages [14] -->
26

<!-- b000460 | prose | pages [14] -->
3 O-18s

<!-- b000461 | prose | pages [14] -->
1 O-18

<!-- b000462 | prose | pages [14] -->
4 O-18s

<!-- b000463 | prose | pages [14] -->
1 M-18

<!-- b000464 | prose | pages [14] -->
2 O-18s

<!-- b000465 | prose | pages [14] -->
30

<!-- b000466 | prose | pages [14] -->
27

<!-- b000467 | prose | pages [14] -->
28

<!-- b000468 | prose | pages [14] -->
29

<!-- b000469 | prose | pages [14] -->
1 O-18

<!-- b000470 | prose | pages [14] -->
2 O-17s

<!-- b000471 | prose | pages [14] -->
1 O-17

<!-- b000472 | prose | pages [14] -->
1 O-17

<!-- b000473 | prose | pages [14] -->
1 O-18

<!-- b000474 | prose | pages [14] -->
1 O-18 1 M-10

<!-- b000475 | prose | pages [14] -->
31

<!-- b000476 | prose | pages [14] -->
June.    1

<!-- b000477 | prose | pages [14] -->
2

<!-- b000478 | prose | pages [14] -->
1 O-17

<!-- b000479 | prose | pages [14] -->
2 O-17s

<!-- b000480 | prose | pages [14] -->
1 O-16

<!-- b000481 | prose | pages [14] -->
1 O-18

<!-- b000482 | prose | pages [14] -->
2 O-18s

<!-- b000483 | prose | pages [14] -->
1 O-18

<!-- b000484 | prose | pages [14] -->
6

<!-- b000485 | prose | pages [14] -->
3 4 5 3 O-18s 3 O-18s 1 O-15

<!-- b000486 | prose | pages [14] -->
1 O-17

<!-- b000487 | prose | pages [14] -->
7 8

<!-- b000488 | prose | pages [14] -->
9

<!-- b000489 | prose | pages [14] -->
1 O-18 1 O-18

<!-- b000490 | prose | pages [14] -->
2 O-17s

<!-- b000491 | prose | pages [14] -->
2 O-18s

<!-- b000492 | prose | pages [14] -->
1 M-18

<!-- b000493 | prose | pages [14] -->
1 M-6

<!-- b000494 | prose | pages [14] -->
1 O-18 1 M-7

<!-- b000495 | prose | pages [14] -->
13

<!-- b000496 | prose | pages [14] -->
10

<!-- b000497 | prose | pages [14] -->
11

<!-- b000498 | prose | pages [14] -->
12

<!-- b000499 | prose | pages [14] -->
2 O-17s

<!-- b000500 | prose | pages [14] -->
1 O-18

<!-- b000501 | prose | pages [14] -->
3 O-18s 1 O-16

<!-- b000502 | prose | pages [14] -->
2 O-18s

<!-- b000503 | prose | pages [14] -->
1 M-18

<!-- b000504 | prose | pages [14] -->
1 M-6

<!-- b000505 | prose | pages [14] -->
14 15

<!-- b000506 | prose | pages [14] -->
16

<!-- b000507 | prose | pages [14] -->
1 O-17 1 O-17

<!-- b000508 | prose | pages [14] -->
1 O-18

<!-- b000509 | prose | pages [14] -->
2 O-18s

<!-- b000510 | prose | pages [14] -->
1 M-6

<!-- b000511 | prose | pages [14] -->
1 M-7

<!-- b000512 | prose | pages [14] -->
20

<!-- b000513 | prose | pages [14] -->
17 18

<!-- b000514 | prose | pages [14] -->
19

<!-- b000515 | prose | pages [14] -->
4 O-18s 2 O-18s

<!-- b000516 | prose | pages [14] -->
1 O-15 1 O-11

<!-- b000517 | prose | pages [14] -->
1 M-6

<!-- b000518 | prose | pages [14] -->
1 M-18

<!-- b000519 | prose | pages [14] -->
21 22

<!-- b000520 | prose | pages [14] -->
23

<!-- b000521 | prose | pages [14] -->
4 O-18s 3 O-18s

<!-- b000522 | prose | pages [14] -->
2 O-18s

<!-- b000523 | prose | pages [14] -->
1 M-9

<!-- b000524 | prose | pages [14] -->
27

<!-- b000525 | prose | pages [14] -->
24

<!-- b000526 | prose | pages [14] -->
25 26

<!-- b000527 | prose | pages [14] -->
1 O-17

<!-- b000528 | prose | pages [14] -->
2 O-18s 1 O-10

<!-- b000529 | prose | pages [14] -->
1 M-8

<!-- b000530 | prose | pages [14] -->
3 O-18s

<!-- b000531 | prose | pages [14] -->
28

<!-- b000532 | prose | pages [14] -->
29

<!-- b000533 | prose | pages [14] -->
30

<!-- b000534 | prose | pages [14] -->
1 O-17

<!-- b000535 | prose | pages [14] -->
2 O-18s

<!-- b000536 | prose | pages [14] -->
1 O-18

<!-- b000537 | prose | pages [14] -->
3 O-18s

<!-- b000538 | prose | pages [14] -->
1 M-7

<!-- b000539 | prose | pages [14] -->
1 M-18

<!-- b000540 | prose | pages [14] -->
1 M-8

<!-- b000541 | prose | pages [14] -->
1 M-18

<!-- b000542 | prose | pages [14] -->
4

<!-- b000543 | prose | pages [14] -->
July.     1

<!-- b000544 | prose | pages [14] -->
2

<!-- b000545 | prose | pages [14] -->
3

<!-- b000546 | prose | pages [14] -->
1 O-11

<!-- b000547 | prose | pages [14] -->
1 O-15

<!-- b000548 | prose | pages [14] -->
3 O-18s

<!-- b000549 | prose | pages [14] -->
1 M-6

<!-- b000550 | prose | pages [14] -->
1 O-16

<!-- b000551 | prose | pages [14] -->
1 M-11

<!-- b000552 | prose | pages [14] -->
1 O-17 1 O-18

<!-- b000553 | prose | pages [14] -->
5

<!-- b000554 | prose | pages [14] -->
6

<!-- b000555 | prose | pages [14] -->
7

<!-- b000556 | prose | pages [14] -->
1 O-16

<!-- b000557 | prose | pages [14] -->
1 O-16

<!-- b000558 | prose | pages [14] -->
2 O-18s

<!-- b000559 | prose | pages [14] -->
3 O-17s

<!-- b000560 | prose | pages [14] -->
1 O-17

<!-- b000561 | prose | pages [14] -->
1 M-7

<!-- b000562 | prose | pages [14] -->
11

<!-- b000563 | prose | pages [14] -->
8

<!-- b000564 | prose | pages [14] -->
9

<!-- b000565 | prose | pages [14] -->
10

<!-- b000566 | prose | pages [14] -->
2 O-18s

<!-- b000567 | prose | pages [14] -->
2 O-17s

<!-- b000568 | prose | pages [14] -->
4 O-18s

<!-- b000569 | prose | pages [14] -->
1 M-18

<!-- b000570 | prose | pages [14] -->
1 O-18

<!-- b000571 | furniture | pages [14] -->


<!-- b000572 | prose | pages [14] -->
12

<!-- b000573 | prose | pages [14] -->
13

<!-- b000574 | prose | pages [14] -->
14

<!-- b000575 | prose | pages [14] -->
3 O-18s

<!-- b000576 | prose | pages [14] -->
1 O-16

<!-- b000577 | furniture | pages [14] -->


<!-- b000578 | prose | pages [14] -->
1 M-6

<!-- b000579 | prose | pages [14] -->
1 O-17

<!-- b000580 | prose | pages [14] -->
1 O-18

<!-- b000581 | prose | pages [14] -->
1 M-18

<!-- b000582 | furniture | pages [15] -->
team13074                                                       page 15of20

<!-- b000583 | prose | pages [15] -->
18

<!-- b000584 | prose | pages [15] -->
15

<!-- b000585 | prose | pages [15] -->
16

<!-- b000586 | prose | pages [15] -->
17

<!-- b000587 | furniture | pages [15] -->


<!-- b000588 | prose | pages [15] -->
1 O-18

<!-- b000589 | prose | pages [15] -->
1 O-17

<!-- b000590 | prose | pages [15] -->
1 O-16

<!-- b000591 | prose | pages [15] -->
19

<!-- b000592 | prose | pages [15] -->
20 21

<!-- b000593 | prose | pages [15] -->
1 O-18

<!-- b000594 | prose | pages [15] -->
3 O-18s 1 O-17

<!-- b000595 | prose | pages [15] -->
2 O-17s

<!-- b000596 | prose | pages [15] -->
1 M-6

<!-- b000597 | prose | pages [15] -->
2 O-18s

<!-- b000598 | prose | pages [15] -->
1 M-7

<!-- b000599 | prose | pages [15] -->
1 O-18

<!-- b000600 | prose | pages [15] -->
1 M-18

<!-- b000601 | prose | pages [15] -->
25

<!-- b000602 | prose | pages [15] -->
22 23

<!-- b000603 | prose | pages [15] -->
24

<!-- b000604 | prose | pages [15] -->
1 O-10 2 O-16s

<!-- b000605 | prose | pages [15] -->
1 O-15

<!-- b000606 | prose | pages [15] -->
1 O-18

<!-- b000607 | prose | pages [15] -->
2 O-17s

<!-- b000608 | prose | pages [15] -->
1 O-16

<!-- b000609 | prose | pages [15] -->
1 O-17

<!-- b000610 | prose | pages [15] -->
1 O-18

<!-- b000611 | prose | pages [15] -->
26

<!-- b000612 | prose | pages [15] -->
27

<!-- b000613 | prose | pages [15] -->
28

<!-- b000614 | prose | pages [15] -->
2 O-18s

<!-- b000615 | prose | pages [15] -->
1 O-17

<!-- b000616 | prose | pages [15] -->
3 O-18s

<!-- b000617 | prose | pages [15] -->
1 M-6

<!-- b000618 | prose | pages [15] -->
3 O-18s

<!-- b000619 | prose | pages [15] -->
Aug.    1

<!-- b000620 | prose | pages [15] -->
29

<!-- b000621 | prose | pages [15] -->
30

<!-- b000622 | prose | pages [15] -->
31

<!-- b000623 | prose | pages [15] -->
1 O-18

<!-- b000624 | prose | pages [15] -->
3 O-18s

<!-- b000625 | prose | pages [15] -->
1 O-11

<!-- b000626 | prose | pages [15] -->
1 O-16

<!-- b000627 | prose | pages [15] -->
1 M-6

<!-- b000628 | prose | pages [15] -->
1 M-18

<!-- b000629 | prose | pages [15] -->
1 O-17

<!-- b000630 | prose | pages [15] -->
2

<!-- b000631 | prose | pages [15] -->
3

<!-- b000632 | prose | pages [15] -->
4

<!-- b000633 | prose | pages [15] -->
3 O-18s

<!-- b000634 | prose | pages [15] -->
1 O-18

<!-- b000635 | prose | pages [15] -->
4 O-18s

<!-- b000636 | prose | pages [15] -->
1 M-18

<!-- b000637 | prose | pages [15] -->
2 O-18s

<!-- b000638 | prose | pages [15] -->
8

<!-- b000639 | prose | pages [15] -->
5

<!-- b000640 | prose | pages [15] -->
6

<!-- b000641 | prose | pages [15] -->
7

<!-- b000642 | prose | pages [15] -->
1 O-18

<!-- b000643 | prose | pages [15] -->
2 O-17s

<!-- b000644 | prose | pages [15] -->
1 O-17

<!-- b000645 | prose | pages [15] -->
1 O-17

<!-- b000646 | prose | pages [15] -->
1 O-18

<!-- b000647 | prose | pages [15] -->
1 O-18 1 M-10

<!-- b000648 | prose | pages [15] -->
9

<!-- b000649 | prose | pages [15] -->
10

<!-- b000650 | prose | pages [15] -->
11

<!-- b000651 | prose | pages [15] -->
1 O-17

<!-- b000652 | prose | pages [15] -->
2 O-17s

<!-- b000653 | prose | pages [15] -->
1 O-16

<!-- b000654 | prose | pages [15] -->
1 O-18

<!-- b000655 | prose | pages [15] -->
2 O-18s

<!-- b000656 | prose | pages [15] -->
1 O-18

<!-- b000657 | prose | pages [15] -->
15

<!-- b000658 | prose | pages [15] -->
12 13 14 3 O-18s 3 O-18s 1 O-15

<!-- b000659 | prose | pages [15] -->
1 O-17

<!-- b000660 | prose | pages [15] -->
16 17

<!-- b000661 | prose | pages [15] -->
18

<!-- b000662 | prose | pages [15] -->
1 O-18 1 O-18

<!-- b000663 | prose | pages [15] -->
2 O-17s

<!-- b000664 | prose | pages [15] -->
2 O-18s

<!-- b000665 | prose | pages [15] -->
1 M-18

<!-- b000666 | prose | pages [15] -->
1 M-6

<!-- b000667 | prose | pages [15] -->
1 O-18 1 M-7

<!-- b000668 | prose | pages [15] -->
22

<!-- b000669 | prose | pages [15] -->
19

<!-- b000670 | prose | pages [15] -->
20

<!-- b000671 | prose | pages [15] -->
21

<!-- b000672 | prose | pages [15] -->
2 O-17s

<!-- b000673 | prose | pages [15] -->
1 O-18

<!-- b000674 | prose | pages [15] -->
3 O-18s 1 O-16

<!-- b000675 | prose | pages [15] -->
2 O-18s

<!-- b000676 | prose | pages [15] -->
1 M-18

<!-- b000677 | prose | pages [15] -->
1 M-6

<!-- b000678 | prose | pages [15] -->
23 24

<!-- b000679 | prose | pages [15] -->
25

<!-- b000680 | prose | pages [15] -->
1 O-17 1 O-17

<!-- b000681 | prose | pages [15] -->
1 O-18

<!-- b000682 | prose | pages [15] -->
2 O-18s

<!-- b000683 | prose | pages [15] -->
1 M-6

<!-- b000684 | prose | pages [15] -->
1 M-7

<!-- b000685 | prose | pages [15] -->
29

<!-- b000686 | prose | pages [15] -->
26 27

<!-- b000687 | prose | pages [15] -->
28

<!-- b000688 | prose | pages [15] -->
4 O-18s 2 O-18s

<!-- b000689 | furniture | pages [15] -->


<!-- b000690 | furniture | pages [15] -->


<!-- b000691 | prose | pages [15] -->
1 M-6

<!-- b000692 | prose | pages [15] -->
2 M-18s

<!-- b000693 | prose | pages [15] -->
30

<!-- b000694 | prose | pages [15] -->
31

<!-- b000695 | furniture | pages [15] -->


<!-- b000696 | furniture | pages [15] -->


<!-- b000697 | furniture | pages [15] -->


<!-- b000698 | prose | pages [15] -->
Chart10 whole schedule for part2 with Y=150 6.2.3 Application to situation where X trips are given (ⅰ) X trips are given with fixed dates, types and unrestrained routes This is equivalent to a situation where the first X trips are already chosen in the process described in 6.2.2, so we only need to continue the Greedy algorithm to form a final schedule on the basis of these X given trips. (ⅱ) X trips are given with fixed dates, types and routes This is similar to (ⅰ) except for one thing. The probability of the event that there exist two trips occupying the same campsite at the same day equals the probability of the event that there exist one trip occupying this campsite at this day, if the other trip is within those X trips and the campsite as well as the date are within its route. This value is still obtained using Jordan Formula. The rest of the process is identical to (ⅱ).

<!-- b000699 | heading | pages [15] -->
7 Part 3 Best schedule of trips with fixed dates, but unrestrained types

<!-- b000700 | furniture | pages [15] -->


<!-- b000701 | furniture | pages [16] -->
team13074                                                       page 16of20

<!-- b000702 | prose | pages [16] -->
and routes.

<!-- b000703 | heading | pages [16] -->
7.1 Method

<!-- b000704 | prose | pages [16] -->
7.1.1 Motivation and justification In part 3, our solution gives tourists the freedom to choose trip types, and we still consider that the routes of trips are unrestrained. This solution simulates the actual situations that the river agency provides several available trips and the tourists could choose one of them, and also, like in Part 2, the river agency does not fix the route for tourists. Special assumptions for this part: Just as the assumptions in Part 2, we use classical probability to describe the behavior of tourists’ choice of their route, all possible routes sharing the same probability. And as assumption 4⑥, we consider an event with probability 0.05 as not happening. In addition, in this part, we also assume that all available trips provided to tourists share the same probability, which means that in our solution tourist will choose one of the available trips randomly. 7.1.2 Key ideas In this solution, we add trips one by one and the trip added is randomly selected from all possible trips for the current condition. The only difference between the solution in this part and in Part 2 is that we randomly choose a trip to add it into the schedule instead of the trip which could optimize the schedule.

<!-- b000705 | heading | pages [16] -->
7.2 Development of the model

<!-- b000706 | prose | pages [16] -->
To start with, we find out the number of trip types available. Similar to the calculation in 5.2, but here we consider that the time passengers can travel every day must be rigorously less than 8 hours, therefore trip type 1 (oar-powered, 6 days) and trip type 3 (oar-powered, 7 days) are crossed out. Consequently there are altogether 24 trip types available. When we speak of 26 types below, just think two of them are not exist. The program flow of this solution is stated below: STEP 1: Day=1, and Day records the day in which the next trip will be added. STEP 2: Find out all the available trips for the current situation. And the method to determine whether a trip could be added is mentioned in Part 2, which means that a trip could be added if and only if the probability, after the trip is added, of two trips occupying a certain campsite in a certain day is less than 0.05. STEP 3: Randomly select one trip from all the available trips and add it into the schedule. STEP 4: Repeat STEP 2 and 3 until no trips could be added. And then Day=Day+1. STEP 5: Repeat STEP 4 until Day>180. The following is the data of 8 schedules we get using this program.

<!-- b000707 | furniture | pages [16] -->


<!-- b000708 | furniture | pages [16] -->


<!-- b000709 | furniture | pages [16] -->


<!-- b000710 | furniture | pages [17] -->
team13074                                                       page 17of20

<!-- b000711 | prose | pages [17] -->
Run times 1 2 3

<!-- b000712 | prose | pages [17] -->
Carrying capacity 482 486 493

<!-- b000713 | prose | pages [17] -->
4 5 6 7 8

<!-- b000714 | prose | pages [17] -->
493 476 474 485 475 Chart11 carrying capacity of the river The number of trip type i The percentage of trip type i Trip type i

<!-- b000715 | prose | pages [17] -->
5 3 7 8 9 36 11 40 13 34 15 23

<!-- b000716 | prose | pages [17] -->
Oar-powered

<!-- b000717 | prose | pages [17] -->
17 38 19 83 21 221 23 553 25 1577 Total 2616

<!-- b000718 | prose | pages [17] -->
2 56 4 62 6 56 8 42 10 28 12 17 14 21

<!-- b000719 | prose | pages [17] -->
Motorized

<!-- b000720 | prose | pages [17] -->
16 18 18 19 20 25 22 74 24 207 26 623 Total 1248 Total 3864

<!-- b000721 | prose | pages [17] -->
0.08% 0.21% 0.93% 1.04% 0.88% 0.60% 0.98% 2.15% 5.72% 14.31% 40.81% 67.7%

<!-- b000722 | prose | pages [17] -->
1.45% 1.60% 1.45% 1.09% 0.72% 0.44% 0.54% 0.47% 0.49% 0.65% 1.92% 5.36% 16.12% 32.3%

<!-- b000723 | furniture | pages [17] -->


<!-- b000724 | prose | pages [17] -->
Chart12 number of varying trip types Comparing with the results of Part 2, the total numbers of trips in each schedule are almost the same. This is because the differences caused by adding different trips are very small. Moreover, this solution could also apply to the situation where X trips are given and the method is nearly the same with which we discuss in 6.2.3.

<!-- b000725 | heading | pages [17] -->
8 Testing of the model----Sensitivity analysis

<!-- b000726 | prose | pages [17] -->
We use the sensitivity analysis to defend our model. The sensitivity of a model is a measure of how sensitive the result changes at small changes of parameters. A good model is corresponding to low sensitiveness. Considering the parameters used in our solutions, here we provide following

<!-- b000727 | furniture | pages [17] -->


<!-- b000728 | furniture | pages [18] -->
team13074                                                       page 18of20

<!-- b000729 | prose | pages [18] -->
discussion.

<!-- b000730 | heading | pages [18] -->
8.1 Stability with varying trip types chosen in 6

<!-- b000731 | prose | pages [18] -->
In 6.2.2, we consider that choosing any one trip type as the first trip coming into the river will not significantly change the result. Here we will give the sensitivity analysis to defend this consideration. We set all the 24 trip types respectively as the first trip and obtain the numbers of trips in each schedule, as is shown in the chart.

<!-- b000732 | prose | pages [18] -->
The first trip

<!-- b000733 | prose | pages [18] -->
Carrying

<!-- b000734 | prose | pages [18] -->
The first trip

<!-- b000735 | prose | pages [18] -->
type

<!-- b000736 | prose | pages [18] -->
capacity

<!-- b000737 | prose | pages [18] -->
type

<!-- b000738 | prose | pages [18] -->
2 490 11

<!-- b000739 | prose | pages [18] -->
4 479 12 5 486 13

<!-- b000740 | prose | pages [18] -->
6 486 14 7 486 15

<!-- b000741 | prose | pages [18] -->
8 490 16

<!-- b000742 | prose | pages [18] -->
9 490 17 10 486 18

<!-- b000743 | prose | pages [18] -->
Carrying

<!-- b000744 | prose | pages [18] -->
The first trip

<!-- b000745 | prose | pages [18] -->
Carrying

<!-- b000746 | prose | pages [18] -->
capacity

<!-- b000747 | prose | pages [18] -->
type

<!-- b000748 | prose | pages [18] -->
capacity

<!-- b000749 | prose | pages [18] -->
473 19 481

<!-- b000750 | prose | pages [18] -->
483 20 487 496 21 488

<!-- b000751 | prose | pages [18] -->
493 22 500 476 23 486

<!-- b000752 | prose | pages [18] -->
478 24 482

<!-- b000753 | prose | pages [18] -->
489 25 479 485 26 488

<!-- b000754 | prose | pages [18] -->
Chart13 carrying capacities due to varying first trip type From the data, we could conclude that different first trips could only cause slight differences in the results. So we could randomly select the first trip to get the schedule.

<!-- b000755 | heading | pages [18] -->
8.2 The sensitivity analysis of the assumption 4④

<!-- b000756 | prose | pages [18] -->
In assumption 4④, we assume that passengers could spend no more than 8 hours per day on the river. However, different durations per day could change the results of our solutions. The following is the results of Part 2, setting type 22 trip as the first trip and using 7, 7.5, 8, 8.5, 9 hours as the largest time spent on the river every day. And it can be seen from the data that the results only change slightly, which could be served to low sensitiveness.

<!-- b000757 | prose | pages [18] -->
Trip hour per day 7

<!-- b000758 | prose | pages [18] -->
Carrying capacity 454

<!-- b000759 | prose | pages [18] -->
7.5 8 8.5 9

<!-- b000760 | prose | pages [18] -->
484 560 483 488 Chart14 carrying capacities of varying trip hour per day

<!-- b000761 | heading | pages [18] -->
8.3 The sensitivity analysis of the assumption 4⑥

<!-- b000762 | prose | pages [18] -->
In Part 2 and 3 we set 0.05 as the small probability of events that can be considered as not happening. And the following table includes the results setting type 22 trip as the first trip and using 0.01, 0.025, 0.05 as this small probability. And we could conclude that, the different setting of this parameter could cause the differences that should not be ignored.

<!-- b000763 | prose | pages [18] -->
Small probability 0.01

<!-- b000764 | prose | pages [18] -->
Carrying capacity 215

<!-- b000765 | prose | pages [18] -->
0.025 0.05

<!-- b000766 | prose | pages [18] -->
376 500 Chart15 carrying capacities of varying small probability

<!-- b000767 | heading | pages [18] -->
9 Evaluation of the model

<!-- b000768 | furniture | pages [18] -->


<!-- b000769 | furniture | pages [19] -->
team13074                                                       page 19of20

<!-- b000770 | heading | pages [19] -->
9.1 Strengths and weaknesses

<!-- b000771 | prose | pages [19] -->
9.1.1 Strengths Our models have following advantages: In Part 1: ①We could utilize the campsite sets to a great extent, because all the campsite sets are used almost in every day in the 6 months. ②The method limiting the orbits and distributing the campsite sets for each type of trip could reduce the problem’s complexity effectively. ③The model could provide solutions for different value of Y. ④The model allows different rate distribution among all kinds of trip types, which is more close to reality. In Part 2: ①Using classical probability, to describe the behavior of tourists’ choice of their own route, could accurately compute the probability that trips occupy the same campsite at the same day. ②As mentioned in 6.2.3, the model could apply to the situations where X trips are given, with fixed routes or not. ③The model allows the tourists to choose the campsite sets where they prefer to stay, which is more close to the fact. In Part 3: ①In this solution, tourists could select the trip type from several available type the river agency provides, which makes this solution more realistic than Part 1 and 2. 9.1.2 Weakness Our models have following disadvantages: ①In Part 1, the model is not realistic, because it fails to provide different types of trips and alternative routes to be chosen by tourists. ②In Part 2, the classical probability may be not enough accurate to describe the behavior of tourists’ choice of their own route, which could cause the errors in the results. ③In Part 3, all available trips provided to tourists may not share the same probability, which could also results in the unreality. ④In the results of Part 2 and 3, the differences among the trip numbers of different types are significant, which is not close to the reality.

<!-- b000772 | heading | pages [19] -->
9.2 Further discussion

<!-- b000773 | prose | pages [19] -->
①Although the solutions in Part 1, to some extent, are not realistic, the method limiting the orbits and distributing the campsite sets for each type of trip is valuable and could be adjusted to be used in practical applications. ②Using the model in Part 2, the government could do some practical research and questionnaire surveys in order to find the more accurate probability, describing the behavior of tourists’ choice of their own route, than the classical probability. ③In Part 3, we assume that all available trips provided to tourists share the same probability, which may be not realistic. However, the government and the river

<!-- b000774 | furniture | pages [19] -->


<!-- b000775 | furniture | pages [20] -->
team13074                                                       page 20of20

<!-- b000776 | prose | pages [20] -->
agency could also do some relevant research to find out which types of trips the tourists more likely to prefer, and use the results in the model in Part 3.

<!-- b000777 | heading | pages [20] -->
10 Conclusions

<!-- b000778 | prose | pages [20] -->
We mainly divide the problem into three parts and come up with three different schedules in terms of the flexibility of the trips, and it is up to managers to choose from them for further considerations such as commercial and management issues. In part 1, we find the schedule of trips with fixed dates, types (propulsion and duration) and routes (which campsites the trip stops at), and to achieve this we use a rather novel method. The key idea is to divide campsites into different “orbits” that only allows some certain trip types to travel in, therefore the problem turns into several separate small problem to allocate fewer trip types, and the discussion of orbits allowing one, two, three trip types lead to general result which can deal with any value of Y. Particularly, we let Y=150, a rather realistic number of campsites, to demonstrate a concrete schedule and the carrying capacity of the river is 2340 trips. In part 2, we find the schedule of trips with fixed dates, types but unrestrained routes. To better describe the behavior of tourists, we need to use a stochastic model. We assume a classical probability model and also use the upper limit value of small probability to define an event as not happening. Then we use Greedy algorithm to choose the trips added and recursive algorithm together with Jordan Formula to calculate the probability of two trips simultaneously occupying the same campsites. The carrying capacity of the river by this method is 500 trips. This method can easily find the optimal schedule with X given trips, no matter these X trips are with fixed routes or not. In part 3, we find the optimal schedule of trips with fixed dates and unrestrained types and routes. This is based on the probability model developed in part 2 and we assign the choice of trip types of the tourists with a uniform distribution to describe their freedom to choose and obtain the results similar to part 2. The carrying capacity of the river by this method is 493 trips. Also this method can easily find the optimal schedule with X given trips, no matter these X trips are with fixed routes or not.

<!-- b000779 | heading | pages [20] -->
11 References

<!-- b000780 | references | pages [20] -->
【1】http://zhidao.baidu.com/question/213576448.html

<!-- b000781 | references | pages [20] -->
【2】http://www.missinaibi.com/upper_missinaibi_river.html

<!-- b000782 | references | pages [20] -->
【3】http://www.missinaibi.com/upper_missinaibi_river.html

<!-- b000783 | references | pages [20] -->
【4】http://canyonx.com/day_on_the_river.php

<!-- b000784 | furniture | pages [20] -->


<!-- b000785 | furniture | pages [20] -->


<!-- b000786 | furniture | pages [20] -->


<!-- b000787 | furniture | pages [20] -->


<!-- b000788 | furniture | pages [20] -->


<!-- b000789 | furniture | pages [20] -->


<!-- b000790 | furniture | pages [20] -->


<!-- b000791 | furniture | pages [20] -->


<!-- b000792 | furniture | pages [21] -->
team13074                                                       page 21of20

<!-- b000793 | heading | pages [21] -->
12 Letter to the river managers

<!-- b000794 | prose | pages [21] -->
To managers of the Big Long River, Given the rise in popularity of river trips on the Big Long River, there is an urge to come up with a schedule to best utilize the campsites on the river. However, there is also a requirement to

<!-- b000795 | prose | pages [21] -->
provide the tourists with wilderness experiences and therefore no two trips can occupy the same campsite at the same time. Given the above considerations, we want to find the optimal

<!-- b000796 | prose | pages [21] -->
schedule of trips of varying duration and propulsion to use the campsites as many as possible and hence finding the carrying capacity of the river, which means the maximum number of trips in a

<!-- b000797 | prose | pages [21] -->
six months period and is therefore equal to the number of trips in the optimal schedule. Also we

<!-- b000798 | prose | pages [21] -->
need to find the maximum number of trips added with X given trips, and equivalently the optimal schedule with X given trips. We have undertaken an extensive examination of the problem and

<!-- b000799 | prose | pages [21] -->
here are our key findings, hope they are beneficial to your management of the river. We mainly design three schedules for three different situations in terms of the flexibility of the

<!-- b000800 | prose | pages [21] -->
trip. The first schedule is of trips with fixed dates, types (propulsion and duration), and routes (which

<!-- b000801 | prose | pages [21] -->
campsites the tourists choose to stop at), and we develop a rather novel method here. The key

<!-- b000802 | prose | pages [21] -->
idea is to divide the campsites into separate “which” are for some certain trip types to travel in, and we only need to find the optimal schedule for every orbit with fewer trip types. This reduces

<!-- b000803 | prose | pages [21] -->
the problem to be simple and solvable. To better demonstrate our model, we let Y=150 (which is an appropriate number for Big Long River based on reference) and obtain an exact schedule and

<!-- b000804 | prose | pages [21] -->
the carrying capacity of the river in this method is 2340 trips. Note this provides with a rather large number of total trips but it provides with little flexibility to tourists. The advantages of this model are that it provides with a simple but almost optimal schedule and that it is able to control the proportions of the number of all trip types, which makes sense to you for easier management

<!-- b000805 | prose | pages [21] -->
of the river trips.

<!-- b000806 | prose | pages [21] -->
The second schedule is of trips with fixed dates, types but unrestrained routes. To better describe the behavior of tourists, we choose to use a stochastic model. We assume a classical probability model and also use the upper limit value of small probability to define an event as not happening. Then we use Greedy algorithm to choose the trips added and recursive algorithm together with

<!-- b000807 | prose | pages [21] -->
Jordan Formula to calculate the probability of two trips simultaneously occupying the same campsites. The carrying capacity of the river by this method is 500 trips. The advantages of this

<!-- b000808 | prose | pages [21] -->
model are that it best describes the actual behaviors of tourists in terms of trip flexibility and that the classical probability assumption can be easily replaced with other given distributions that better describe the tourists’ behaviors, also it can easily find the optimal schedule with X given

<!-- b000809 | prose | pages [21] -->
trips, no matter these X trips are with fixed routes or not. The third schedule is of trips with fixed dates and unrestrained types and routes. This is based on

<!-- b000810 | prose | pages [21] -->
the probability model developed in the second schedule and we assign the choice of trip types of the tourists with a uniform distribution to describe their freedom to choose and obtain the

<!-- b000811 | prose | pages [21] -->
results similar to the process in the second schedule. The carrying capacity of the river by this

<!-- b000812 | prose | pages [21] -->
method is 493 trips. The advantages of this model are that it well describes the actual behavior of tourists in terms of the trip flexibility and that it can easily find the optimal schedule with X given

<!-- b000813 | prose | pages [21] -->
trips and also the stability of it proves rewarding through our test of sensibility. Above are the descriptions of our three kinds of schedules. The important characteristics of them

<!-- b000814 | furniture | pages [21] -->


<!-- b000815 | furniture | pages [22] -->
team13074                                                       page 22of20

<!-- b000816 | prose | pages [22] -->
are explained and we think it can be up to you to decide which schedule to choose in

<!-- b000817 | prose | pages [22] -->
considerations of commercial and management issues. Hope our solutions can reach your expectations.

<!-- b000818 | furniture | pages [22] -->


<!-- b000819 | furniture | pages [22] -->


<!-- b000820 | furniture | pages [22] -->

