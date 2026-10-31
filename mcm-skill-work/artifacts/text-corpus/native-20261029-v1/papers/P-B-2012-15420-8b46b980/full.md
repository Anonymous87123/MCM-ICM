# P-B-2012-15420-8b46b980

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [2] -->
Optimal Scheduling for the Big Long River

<!-- b000002 | furniture | pages [2] -->
Team # 15420

<!-- b000003 | prose | pages [2] -->
February 13, 2012

<!-- b000004 | heading | pages [2] -->
Abstract

<!-- b000005 | prose | pages [2] -->
This paper addresses the problem of scheduling the maximum number of rafting trips along the Big Long River. An optimal schedule for this problem would minimize the number crossovers while maximizing the percentage of campsites used and matching a target distribution of trip lengths.

<!-- b000006 | prose | pages [2] -->
Three main models are proposed for this problem.

<!-- b000007 | prose | pages [2] -->
The Priority Model iteratively generates a schedule by scheduling trip locations daily and allows for crossovers. The Density Perturbation Model places all trips at their optimal campsites and then iteratively perturbs this structure until no trips are in conﬂict. The Bone Growth Model solves for a schedule with no crossovers globally using a heuristic greedy algorithm that builds oﬀan initial input sequence of trips. Because all models attempt to maximize the number of campsites covered, each assume that there is no cost in launching or recieving many trips at once or for boats crossing each other, but this would not be diﬃcult to address with minor improvements. The Priority Model is able to cover 80% of campsites with up to 30 crossovers per trip and the Bone Growth Model covers about 50% with no crossovers. Both models were able to cover more campsites as the number of campsites increased.

<!-- b000008 | prose | pages [2] -->
There is also a tendency of the distribution of trips length to skew towards the shorter length trips. The Bone Model was very robust to changes in the number of campsites and target distributions, but is senstive to intial conditions. The Priority model number of crossovers increases exponentially as the number of campsites gets larger. The Priority model’s schedule is prefered if crossovers are not a problem for a wide river, whereas the Bone Growth Model is preferred for no crossovers. Each model produces a fairly uniform distribution of launch dates for trips of any length and it is possible to mix models over diﬀerent time windows. Given a wide variety of objectives, we believe that one or more of these models can produce an nearly optimal solution.

<!-- b000009 | prose | pages [2] -->
1

<!-- b000010 | furniture | pages [3] -->
Team # 15420

<!-- b000011 | furniture | pages [3] -->
Page 2 of 20

<!-- b000012 | prose | pages [3] -->
1

<!-- b000013 | heading | pages [3] -->
Introduction

<!-- b000014 | prose | pages [3] -->
We address the problem of generating an optimal schedule for rafting trips along the Big Long River during a six month period. All rafting trips start at the beginning of the river, at mile 0, and end at mile 225. The rafting trips are for 7 to 19 days of actual rafting on the river with 6 to 18 stops at campsites during the nights. These campsites are distributed fairly uniformly through- out the river and each campsite cannot hold more than one trip on a night. In addition, trips should not crossover or pass other trips along on the river to help preserve the wildlife experience. Passengers can either take an oar-powered rubber raft, which travels on average 4 miles per hour, or a motorized boat, which travels on average 8 miles per hour. Our goal, given a set number of campsites, is to create a schedule for the managers of the river that maximizes the number and variety of trips, while maintaining an authentic wildlife experience.

<!-- b000015 | prose | pages [3] -->
This problem presents many speciﬁc challenges that make it worthwhile. First, It is extremely diﬃcult to get a variety of trips, have no trips passing each other, and to not have trips crossing each other. Second, most of previous work in scheduling algorithm and queueing theory does not apply to the Big Long River Problem. The majority of these algorithms are designed for scenarios where there are identical parallel machines or a single machine. Finally, it is not easily optimized via integer programming due to the large solution space.

<!-- b000016 | prose | pages [3] -->
Therefore we developed several original algorithms to attempt to try solve this problem. First, we created a na¨ıve algorithm that adds trips to a schedule one at a time. If a new trip can ﬁt, then it is discarded.

<!-- b000017 | prose | pages [3] -->
This was extened to a priority model, which gives priority to the trips that have to go the farthest each day. To implement this, each day was scheduled iteratively, instead of scheduling trips one at a time. If two trips try to stop at the same campsite, then this algorithm arranges them so that they do not cross over and therefore less trips are discarded.

<!-- b000018 | prose | pages [3] -->
The next model that was attempted was a density perturbation algorithm. Similar to the prior- ity model, each day is scheduled iteratively. The diﬀerence between the two models is that the miles traveled by each boat is considered instead of the campsite that each boat stops at. Therefore, the problem is treated in a continous space and then converts back to the discrete space of the ﬁnite number of campsites afterwards. If trips try to move to locations that are too close to each other, then a density vector is created that ﬁnds how close the trips are to each other and moves them apart so that a one-to-one mapping to the campsites can be found.

<!-- b000019 | prose | pages [3] -->
The last model that was created was a bone growth model. This model uses a heuristic algo- rithm to maximize the number of trips while guaranteeing no crossovers. A bone structure sequence of trips is initialized and fattened to saturation by adding additional trips. This model is a greedy deterministic model that is very sensitive to the initial bone structure, but guarentees a local op- timal solution.

<!-- b000020 | prose | pages [3] -->
2 Deﬁnitions and Variables

<!-- b000021 | prose | pages [3] -->
The following deﬁnitions and variables will be used in our discussion of the Big Long River Problem.

<!-- b000022 | prose | pages [3] -->
• A ‘Crossover’ occurs when a trip passes over another trip during the day.

<!-- b000023 | prose | pages [3] -->
• A ‘Trip’ is sequence of pairs of campsites and nights that denote where a group of passengers are expected to be on any given night.

<!-- b000024 | prose | pages [3] -->
• X is the number of trips to be scheduled

<!-- b000025 | furniture | pages [4] -->
Team # 15420

<!-- b000026 | furniture | pages [4] -->
Page 3 of 20

<!-- b000027 | prose | pages [4] -->
• Y is the number of campsites along the Big Long River.

<!-- b000028 | prose | pages [4] -->
• T is the number of nights available for camping in the six month period.

<!-- b000029 | prose | pages [4] -->
• P is a distribution of trip preferences.

<!-- b000030 | prose | pages [4] -->
• S is the Schedule. There are two Scheduling Matrix Formats, S1, S2 that we used. The ﬁrst format is where S1i,j ∈{0, . . . , Y + 1} describes the campsite that trip i makes on night j. Each row represents a passenger trip and each column represents a night. The second format is where S2i,j ∈{0, 1, . . . , X} describes the trip number (0 is none) that campsite i hosts on night j.

<!-- b000031 | prose | pages [4] -->
• The ‘Open Campsite %’ is the fraction of campsites that are unoccupied during the 180 days divided by the total number of campsites. This percentage will never reach 100% since the last campsites on early days and the ﬁrst campsites in the last days can never be used by trips.

<!-- b000032 | prose | pages [4] -->
• Dmax is the maximum guaranteed distance a trip can be expected to travel in a day. In our schedules, no trip is scheduled to travel further than Dmax, but it is assumed that all trips can make Dmax.

<!-- b000033 | prose | pages [4] -->
• The Big Long River Problem is the following. Given some probability distribution of trip preferences P and some spacing of campsites along the river Y our goal is to generate a Schedule S that maximizes the number of trips X and campsites used, minimize the number of crossover, and attempt to match the same distribution of trips.

<!-- b000034 | prose | pages [4] -->
• C(Y ) is the carrying capacity of the river which is deﬁned to be the maximum number of trips in 180 days divided by the total number of campsites in the Big Long River with respect to some trip distribution. C(Y ) = max X(Y )/Y .

<!-- b000035 | prose | pages [4] -->
3

<!-- b000036 | heading | pages [4] -->
Assumptions

<!-- b000037 | prose | pages [4] -->
Distribution of Oar-Powered Rubber Rafts to Motor Boats and Trip Lengths 3.1

<!-- b000038 | prose | pages [4] -->
We assume that we only have to worry about trip length and not vessel type, because of a strong correlation between vessel type and trip length. The following table is the River Trip Statistics for the Colorado River for 2010, 2009, 2008, and 2007 [1].

<!-- b000039 | prose | pages [4] -->
Vessel Type 2010 Motor 415 Non-Motor 183 2009 2008 2007 409 426 425 183 184 181

<!-- b000040 | prose | pages [4] -->
Since the motorized boats can always travel the necessary distance to reach the end in the necessary number of days and the oar-powered rubber rafts can almost always travel the necessary distance to arrive at the end, it is assumed the whole schedule can be made independently of the choice of motorized boat or rubber raft and then afterwards any trips that cannot accomodate a rubber raft will automatically use a motorized boat and the rest of the trips can be chosen as needed.

<!-- b000041 | prose | pages [4] -->
3.2 No Hybrid-Trips

<!-- b000042 | prose | pages [4] -->
We assume that passengers are not allowed to switch which type of boat they are on during their trip.

<!-- b000043 | furniture | pages [5] -->
Team # 15420

<!-- b000044 | furniture | pages [5] -->
Page 4 of 20

<!-- b000045 | prose | pages [5] -->
3.3 ‘Guaranteed’ Distance Traveled

<!-- b000046 | prose | pages [5] -->
the maximum distance a trip is guaranteed to travel is 64 miles in the motorized boats. This is because, we assume motor boats will travel on average of and 8-mph during each day and that each day allows for 8 hours of travel. We assume that the river is not challenging enough to slow the passengers down signiﬁcantly. We noticed that most River Rafting Trips in the Grand Canyon have itineraries of up to 8 hours of rafting with stops for scenic hikes and lunch [2, 3]. We assume that what trips do during the day outside of rafting is neglibile and there is no concern that too many parties stopping at a campsite for lunch or other activities. We will also ignore the eﬀects of weather and river levels in our model that will eﬀect the speed of the rubber rafts and motor boats.

<!-- b000047 | prose | pages [5] -->
3.4 Distribution and Approximate Number of Campsites

<!-- b000048 | prose | pages [5] -->
We assume that the distances of campsites along the Big Long River is similar to the distances of campsites along the Salmon River in Idaho and the Colorado River in the Grand Canyon. According to Whitewater Campsites [8], there are 162 campsites along 250 miles of the Colorado River and 185 campsites along 180.6 miles of the Salmon River. The following histogram shows the distribution of the distances between campsites along the river.

<!-- b000049 | caption | pages [5] -->
Figure 1: Histogram of the distances between campsites

<!-- b000050 | prose | pages [5] -->
The campsite distribution is therefore assumed to be uniform with diﬀerent distances between campsites in diﬀerent trials. The diﬀerent distances between campsites we test include 5, 1.5, and 1 miles/campsite, which means our tests are done for Y = 45, 150, and 225 campsites.

<!-- b000051 | prose | pages [5] -->
3.5 No Equipment and Labor Constraints

<!-- b000052 | prose | pages [5] -->
We assume that there are enough people employed and that the starting location has a large enough dock so that an unlimited number of boats for any length trip may be launched down the river in one day.

<!-- b000053 | prose | pages [5] -->
3.6 Daytime Does Not Matter

<!-- b000054 | prose | pages [5] -->
We assume in our models that time is discrete and only worry about the campsite location of each trip each night. We assume that all the boats and rafts are able to start oﬀearly enough in the day so that they are able to get to the designed campsite by the end of the day. This is equivalent to assuming that the density of boats and rafts at any section of the river has no impact on the

<!-- b000055 | furniture | pages [6] -->
Team # 15420

<!-- b000056 | furniture | pages [6] -->
Page 5 of 20

<!-- b000057 | prose | pages [6] -->
distance the trips are able to go. This assumption is not very realistic, however we can account for this in two ways; we penalize crossovers in our model evaluation and we can decrease the maximum expected distance that trips are allowed to travel.

<!-- b000058 | prose | pages [6] -->
4

<!-- b000059 | heading | pages [6] -->
Models

<!-- b000060 | prose | pages [6] -->
Our models address the Big Long River Problem by attempting to generate the ‘optimal’ schedule. Optimal is deﬁned to be a schedule that satisﬁes the contraint of no two trips staying at the same campsite during the same night.

<!-- b000061 | prose | pages [6] -->
The current algorithms in scheduling theory and queueing theory do not address the Big Long River problem. The Big Long River problem is similar to scheduling n activities (trips), where each activity requires Y+1 jobs (traveling along river sections) with precendence (order matters). Each section of the river can be treated as a machine that does one job. However, the majority of scheduling algorithms today solve scenarios where there are identical parallel machines or a single machine. Our problem requires a sequence of jobs to be complete in order, but among unique machines (diﬀerent river section). Markov processes and queueing theory also do not apply as However, this problem is one where every campsite only has a queue of one person per night and any people beyond that experience balking with probability equal to one.

<!-- b000062 | prose | pages [6] -->
4.1

<!-- b000063 | heading | pages [6] -->
Na¨ıve model

<!-- b000064 | prose | pages [6] -->
Our ﬁrst attempt at an algorithm to solve this problem was to start with an empty schedule and iteratively add trips until no more trips could be added. We did not expect this solution to be optimal, but we belived it would provide a good initial exploration of the problem. The General Idea

<!-- b000065 | prose | pages [6] -->
• A trip to be added can be randomly selected from a distribution of lengths.

<!-- b000066 | prose | pages [6] -->
• If the trip ﬁts anywhere on the schedule, add it at that point.

<!-- b000067 | prose | pages [6] -->
• If no ﬁt is found for the entire 6 months, remove the trip length from the distribution.

<!-- b000068 | heading | pages [6] -->
The Algorithm

<!-- b000069 | prose | pages [6] -->
Input: empty Schedule, trip length distribution Output: populated schedule

<!-- b000070 | prose | pages [6] -->
While distribution̸ = ∅:

<!-- b000071 | prose | pages [6] -->
1. Randomly select one trip length t from the distribution

<!-- b000072 | prose | pages [6] -->
2. For n in [1, T −t]:

<!-- b000073 | prose | pages [6] -->
(a) Attempt to insert the trip into the schedule starting at night n:

<!-- b000074 | prose | pages [6] -->
i. Try to cover an equal portion of the river each day ii. If a desired campsite is taken, move to the closest avialable site, breaking ties ran-

<!-- b000075 | prose | pages [6] -->
domly iii. If no camptites are available within tolerance, then insert failed iv. If a valid campsite is found for every night in [n, n + t], then insert succeded

<!-- b000076 | prose | pages [6] -->
(b) If success then break

<!-- b000077 | furniture | pages [7] -->
Team # 15420

<!-- b000078 | furniture | pages [7] -->
Page 6 of 20

<!-- b000079 | caption | pages [7] -->
Figure 2: Steps for scheduling three trips in the Na¨ıve Model

<!-- b000080 | prose | pages [7] -->
3. If failure for all n then distribution := distrubution \ {t}

<!-- b000081 | prose | pages [7] -->
Problems with this approach

<!-- b000082 | prose | pages [7] -->
• This schedule allocation has no regard for crossovers.

<!-- b000083 | prose | pages [7] -->
• Scheduling long trips all at once may block oﬀshort trips with large distances to cover from using the campsites they need.

<!-- b000084 | prose | pages [7] -->
These problems propmted us to move on to more advanced models, and the na¨ıve model was excluded from formal testing.

<!-- b000085 | prose | pages [7] -->
4.2

<!-- b000086 | heading | pages [7] -->
Priority Model

<!-- b000087 | prose | pages [7] -->
The Priority model builds on the na¨ıve model by ﬁlling the schedule one night at a time instead of one trip at a time, and by giving scheduling priority to trips with a high ratio of distance remaining to days remaining. The General Idea

<!-- b000088 | prose | pages [7] -->
• Trips with higher (distance left) / (days left) ratios can less aﬀord to be pushed back.

<!-- b000089 | prose | pages [7] -->
• Scheduling one night at a time instead of one trip at a time should give a better “cooperation” between trips.

<!-- b000090 | furniture | pages [8] -->
Team # 15420

<!-- b000091 | furniture | pages [8] -->
Page 7 of 20

<!-- b000092 | prose | pages [8] -->
• Crossings can be avoided by examinig other trips in the area when scheduling the next campsite for a trip.

<!-- b000093 | prose | pages [8] -->
• Trips which cannot be scheduled to any campsite get removed.

<!-- b000094 | caption | pages [8] -->
Figure 3: Steps for scheduling three trips in the Priority Model

<!-- b000095 | heading | pages [8] -->
The Algorithm

<!-- b000096 | prose | pages [8] -->
Input: proposed list of departures for every day Output: populated schedule

<!-- b000097 | prose | pages [8] -->
last := ∅ For night in [0, 180]:

<!-- b000098 | prose | pages [8] -->
1. last = last ∪departures[night]

<!-- b000099 | prose | pages [8] -->
2. With probability p, sort last by distance remaining in descending order days remaining else, randomly shuﬄe last

<!-- b000100 | prose | pages [8] -->
3. next := ∅

<!-- b000101 | prose | pages [8] -->
4. For each trip in last:

<!-- b000102 | prose | pages [8] -->
(a) Find best camp as campsite closest to current position + distance remaining

<!-- b000103 | prose | pages [8] -->
days remaining (b) If best camp is already taken by a trip in next then

<!-- b000104 | furniture | pages [9] -->
Team # 15420

<!-- b000105 | furniture | pages [9] -->
Page 8 of 20

<!-- b000106 | prose | pages [9] -->
i. Find campsite range [min camp, max camp] based on minimum and maximum travel

<!-- b000107 | prose | pages [9] -->
distance ii. Remove all campsites that are already taken in next iii. Rank remaining camps primarily by if they incur a crossover and secondarily by

<!-- b000108 | prose | pages [9] -->
proximity to best camp iv. Choose the ﬁrst ranked camp as new camp

<!-- b000109 | prose | pages [9] -->
else use best camp as new camp

<!-- b000110 | prose | pages [9] -->
(c) If trip is ﬁnished, then add to schedule,

<!-- b000111 | prose | pages [9] -->
else, store the pair (new camp, trip) in next

<!-- b000112 | prose | pages [9] -->
5. last := next

<!-- b000113 | prose | pages [9] -->
4.3

<!-- b000114 | heading | pages [9] -->
Density Perturbation Algorithm

<!-- b000115 | prose | pages [9] -->
In this section a model is proposed where none of the trips are presumed to be more important than any other trips and crossovers are allowed to happen without bound. Previous models have worked oﬀof the idea that the trips with fewer days have less ﬂexibility and therefore need to be scheduled ﬁrst. The optimal distance to travel in one day for a trip is clearly the total distance left to travel divided by the total number of days left to travel this distance. However, there may be several trips which would end the day at the same campsight if they all traveled their optimal distance. Therefore, some trips will have to be moved to other nearby campsights. Note also that the shortest trips have to travel the farthest distance on average. Since the shortest trips have to travel the farthest every day, if they are pushed very far from their optimal campsight they will either be traveling farther on that day or they will have to travel farther than the average distance they need to travel on each subsequent day. This could be a problem since the oar-powered rafts can only travel an assumed maximum of 32 miles a day and the motorized boats can only travel 64 miles a day. The point in scheduling the shortest trips ﬁrst is to make sure these trips travel as close to the average distance as possible each day so that they don’t have to travel well over their average one day and as a result travel further then the maximum distance for one day. The model in this section contradicts the other model. The idea here is that all trips are important and none is more important than the other. While it is necessary for all boats to travel as close to their average distance every day so they don’t have to travel too far, this is actually a poor way to select the trips for two reasons. First, note that for a six night trip the boats have to travel 32.14 miles per day. Therefore, it is going to be extremely diﬃcult for an oar-powered raft to make this trip anyways since it can only travel a maximum of 32 miles per day. Therefore, most of the shorter trips are going to be with motorized boats anyways, and since these can travel a maximum distance of 64 miles per day, traveling an extra 20 miles in one day, which would be a very extreme case, is not even an issue. Even if the oar-powered boats are used for trips as short as 8 nights they still only need to travel 25 miles per day and can travel a little further every day. The second reason the new model is proposed in this section is that by treating the people with the shortest trips as the most important and not scheduling the people with the longest trips until the end the people with the longest trips become extremely hard to ﬁt into the schedule and are often left out. Since most of the campsights have already been taken by people with shorter trips each night the people with the longer trips have to go a much longer distance then their average on some days and then compensate for this by only moving a few miles on some days. Therefore, the model proposed in this section treats everyone with the same importance. The model in this section works by keeping track of the location that every boat is at in terms

<!-- b000116 | furniture | pages [10] -->
Team # 15420

<!-- b000117 | furniture | pages [10] -->
Page 9 of 20

<!-- b000118 | prose | pages [10] -->
of the mile instead of the campsite so that the data is continuous instead of discrete. The model moves every boat to their optimal location for the next day, where the optimal location is the location the boat would need to move to so that they would be traveling the same distance every single day. As wonderful as this idea is in theory, there will clearly be many boats trying to move to the same campsite. Therefore, a density vector is calculated for each boat. A boat contributes to another trip’s density vector if it is trying to move to a location that is less than the distance between two campsites away from the other boat. If a boat is farther down the river than the other boat, it will contribute positively to the other boats density vector. If a boat is behind another boat, it will contribute negatively to that boat’s density vector. Finally, if two boats are at the same spot, the same magnitude will be contributed to each boat’s density vector, although one will be chosen positive and the other will be chosen negative at random. Therefore, subtracting the density vector from the boat’s current locations will spread them out and keep them from trying to stop at the same campsight. The amount added to the density vectors increases linearly as the boats get closer to each other. The amount contributed by boat i to boat j’s density vector ρij can be seen in Equation (1), where di is the speciﬁc location in miles of boat i, and dcampsite is the distance between campsite. Note that this equation assumes the two boats are within one campsite’s distance of each other. If the two boats are not within a campsite’s distance of each other, the contribution to the density vector is set to zero.

<!-- b000119 | prose | pages [10] -->
 dj −di

<!-- b000120 | prose | pages [10] -->
 dj −di

<!-- b000121 | prose | pages [10] -->


<!-- b000122 | prose | pages [10] -->
−

<!-- b000123 | prose | pages [10] -->
ρi,j = sign

<!-- b000124 | prose | pages [10] -->
dcampsite

<!-- b000125 | prose | pages [10] -->
dcampsite

<!-- b000126 | prose | pages [10] -->


<!-- b000127 | prose | pages [10] -->
|dj −di| if ϵ (0, dcampsite] (1)

<!-- b000128 | prose | pages [10] -->
Note that Equation (1) maps from {[−1, 0)∪(0, 1]} to (−1, 1). If the density between the two boats is zero, the function will map to −1, 1 at random. The total density vector for a boat is the sum of the contributions from other boats. This can be seen in Equation (2), where n is the total number of boats on the river.

<!-- b000129 | prose | pages [10] -->
ρj =

<!-- b000130 | prose | pages [10] -->
n X

<!-- b000131 | prose | pages [10] -->
ρi,j (2)

<!-- b000132 | prose | pages [10] -->
i=1, i̸=j

<!-- b000133 | prose | pages [10] -->
For each day, the total density is calculated and subtracted from the positions until the boats are suﬃciently spread out. Since the boats cannot stop at the same campsite, suﬃciently spread out corresponds to nearly a whole campsite distance away from each other. Note that the boats don’t have to be quite a whole campsite distance away from each other. If one boat is only 99% of a campsite ahead of another one and the next boat is 101% of a campsite away from the boat farther down river, there is still a one-to-one mapping of boats to campsites. In the extremely rare case that two boats try to stop at the same campsite, one boat is discarded. One of the beneﬁts to this model is that it does not rely on any prior information about the distribution of the trips. Therefore, if the rafting company so chooses, it can take orders from customers for rafting trips and use this model to ﬁt them all in instead of having a set rafting schedule from each year and letting people pick from all of the available trips.

<!-- b000134 | prose | pages [10] -->
If the rafting company has a set schedule and it turns out that one year a lot more people want to do 18 day trips and fewer people want to do 6 day trips they could lose a lot of business since they haven’t planned enough trips to accommadate all the people who want to do the 18 day trips. This model tries to ﬁt in everybody’s preferences and not lose any business. Note that one of the disadvantages to this model though is that it does nothing to prevent people from passing each other on the river, and if it schedules a trip in which a party gets passed by other boats frequently it could lessen the authenticity of the wilderness experience.

<!-- b000135 | caption | pages [10] -->
Figure 4 shows one result from this algorithm. The algorithm ﬁt 1978 trips into the 180 day time

<!-- b000136 | furniture | pages [11] -->
Team # 15420

<!-- b000137 | furniture | pages [11] -->
Page 10 of 20

<!-- b000138 | caption | pages [11] -->
Figure 4: One result from the density perturbation algorithm. Results in 1978 trips in 180 days

<!-- b000139 | prose | pages [11] -->
with 200 campsites and no trips stopping at the same campsite. Each thread represents a diﬀerent trip. The campsite number at an integral number of days gives the campsite that the trip stops at on that day.

<!-- b000140 | prose | pages [11] -->
period with 200 campsites along the river. The campsites start at mile 10 and are distributed uniformly up through mile 215.

<!-- b000141 | prose | pages [11] -->
4.4

<!-- b000142 | heading | pages [11] -->
Bone Growth Model

<!-- b000143 | prose | pages [11] -->
The Bone Growth Model attempts to maximize the number of trips while matching a given distri- bution of trip preferences. The main selling point of this model is that it uses a heuristic algorithm to maximize the number of trips while guaranteeing no crossovers. The motivation behind this model is to exploit symmetry and to have a deterministic alogrithm that can improve upon pre- vious optimal guesses. We initially start with a “Bone” structure of sequences and fatten it to saturation by adding additional trips. This Algorithm is able to ﬁll approximately 50 % of the campsites with an average carrying capacity of 7.5 trips per campsite over 180 days with respect to a slightly skewed uniform distribution of trips. This Algorithm generates very uniform spread of launch times of trips of all lengths.

<!-- b000144 | prose | pages [11] -->
The main idea of the model is based on the following two Heuristics.

<!-- b000145 | prose | pages [11] -->
Heuristic 1: Long Trips are the Rate Determining Trips.

<!-- b000146 | prose | pages [11] -->
The order of launches by trip type on a single day begins with the shortest length trips and increases to the the longest length trips. In addition, the shortest length trip we launch must be

<!-- b000147 | furniture | pages [12] -->
Team # 15420

<!-- b000148 | furniture | pages [12] -->
Page 11 of 20

<!-- b000149 | prose | pages [12] -->
greater or equal in length to the remaining days of the longest trip on the river. If this is not satisﬁed then we will have sent a short trip that will ﬁnish before a long trip and will have to crossover the long trip.

<!-- b000150 | prose | pages [12] -->
Therefore the optimal sequence alternates between a monotonically increasing sequence from 6 to 18 days and a monotone decreasing sequence from 18 to 6 days (e.g. {6, 7, 8, .., 17, 18, 18, 17, ..., 8, 6}). The sequence also ﬁxes the launch and ﬁnish dates of the trip.

<!-- b000151 | prose | pages [12] -->
Heuristic 2: Packing towards Center Maximizes Number of Trips.

<!-- b000152 | prose | pages [12] -->
At maximum saturation, another trip of any length cannot be added without crossing another. To determine if a sequence of trips is possible it is necessary that all trips could be ‘squeezed’ into the center. Since the launch and ﬁnish dates of a trip are determined, ‘squeezing’ is pulling the trajectory of the trip to be as close to the trip closest to the center. This is a necessary condition once the launch and ﬁnish dates of a sequence are determined, since all other schedules involve ‘peeling’ or spreading the trips from the clumped up pattern. (See the lower two graphs in Figure 5). The outline of the Bone Growth algorithm is below.

<!-- b000153 | caption | pages [12] -->
Figure 5: An Example of the Bone Growth Algorithm

<!-- b000154 | prose | pages [12] -->
1. Start with an intial “Bone” Sequence and a target Distribution of Trips

<!-- b000155 | prose | pages [12] -->
2. Try adding another trip to the current sequence to closer match the target distribution.

<!-- b000156 | prose | pages [12] -->
(a) Find Possible insertion points from Heuristic 1

<!-- b000157 | prose | pages [12] -->
(b) Build the Schedule from this sequence by Starting with the center and adding additional

<!-- b000158 | prose | pages [12] -->
trips following Heuristic 2.

<!-- b000159 | prose | pages [12] -->
(c) If the new sequence is possible to schedule with no crossovers, spread the trips out in

<!-- b000160 | prose | pages [12] -->
time to make it more uniform

<!-- b000161 | prose | pages [12] -->
(d) If the new sequence is not possible to schedule, attempt to add the next ‘best’ trip to

<!-- b000162 | prose | pages [12] -->
the current schedule.

<!-- b000163 | furniture | pages [13] -->
Team # 15420

<!-- b000164 | furniture | pages [13] -->
Page 12 of 20

<!-- b000165 | prose | pages [13] -->
3. Repeat Process with diﬀerent starting “Bone” Sequence.

<!-- b000166 | prose | pages [13] -->
The method of determining the ‘best’ trip to add to the current schedule can be based on various criteria. We decided on a greed algorithm that adds the trip that maximizes the sequence’s score relative to all others.

<!-- b000167 | caption | pages [13] -->
Figure 5 is an example of the algorithm working over 43 days. The initial Bone Structure is

<!-- b000168 | prose | pages [13] -->
shown in the Upper Left. After 40 new trips have been added we obtain the result in the Upper Right. The Lower Left is the result when the Bone Structure has been saturated and no further trips of any size can be added. Finally, the trips are spread more evenly to obtain the result in the Lower Right.

<!-- b000169 | caption | pages [13] -->
Figure 6: An Example of the Bone Growth with Diﬀerent Trip Types. Blue are Motor Boats.

<!-- b000170 | prose | pages [13] -->
Purple are Oar Powered Rubber Rafts

<!-- b000171 | prose | pages [13] -->
This model can be extended to allow for diﬀerentiation between motor boats and oar-powered rubber rafts. The setup is exactly the same, the only diﬀerence is in that oar-powered rubber rafts are less ﬂexible than motor boats. An example of this modiﬁcation is shown in Figure 6. Due to time constraints we were not able to adjust our spreading algorithm appropriately to account for the less-ﬂexibility of the oar-powered rubber rafts.

<!-- b000172 | furniture | pages [14] -->
Team # 15420

<!-- b000173 | prose | pages [14] -->
5

<!-- b000174 | heading | pages [14] -->
Testing and Results

<!-- b000175 | furniture | pages [14] -->
Page 13 of 20

<!-- b000176 | prose | pages [14] -->
We tested our model based on the following criterion, which they prioritize in this order: Maximize the number of trips and campsites occupied, Minimizes the number of crossovers, and Match a target Distribution of Trips. We also checked that no two trips occupy the same campsite at the end of the night, and all of our schedules satisfy this necessary condition.

<!-- b000177 | prose | pages [14] -->
5.1

<!-- b000178 | heading | pages [14] -->
Model Comparison

<!-- b000179 | prose | pages [14] -->
We tested the Bone Growth Model and Priority Model using 3 diﬀerent campsite values 45, 150, 225 and 2 diﬀerent target distributions, Uniform and Triangle. The uniform distribution would target having a uniform number of trip lengths. The Triangle distribution assigned a weight of 40 −l to each trip where l is the trip length. To measure how good of a schedule each produced, we looked at the percentage of open campsites, the average number of crossovers per trip, and the Variance between the Simulated Distribution and the Target Distribution. We obtained the following results in the tables below:

<!-- b000180 | prose | pages [14] -->
Var from Distr −104 % Open Model Y Distr # of Trips Avg # Crossovers

<!-- b000181 | prose | pages [14] -->
52.32 Bones1 45 Uniform 337 0.00 1.83 48.02 Bones2 45 Uniform 409 0.00 14.15 23.80 Priority 45 Uniform 546 4.37 6.19 53.60 Bones1 45 Triangle 337 0.00 3.73 48.96 Bones2 45 Triangle 405 0.00 15.24 24.59 Priority 45 Triangle 555 4.37 6.27 52.14 Bones1 150 Uniform 1129 0.00 1.96 47.24 Bones2 150 Uniform 1391 0.00 14.78 17.17 Priority 150 Uniform 1900 18.56 1.88 53.59 Bones1 150 Triangle 1129 0.00 4.27 48.26 Bones2 150 Triangle 1387 0.00 17.51 17.39 Priority 150 Triangle 2019 18.96 5.54 41.07 D.Pertb.

<!-- b000182 | prose | pages [14] -->
200 Uniform 1811 19.07 5.85 51.82 Bones1 225 Uniform 1707 0.00 2.09 46.80 Bones2 225 Uniform 2107 0.00 15.04 16.55 Priority 225 Uniform 2911 28.93 1.30 53.20 Bones1 225 Triangle 1709 0.00 4.41 47.74 Bones2 225 Triangle 2107 0.00 18.02 17.28 Priority 225 Triangle 2937 29.06 1.99 Testing Results

<!-- b000183 | prose | pages [14] -->
5.2

<!-- b000184 | heading | pages [14] -->
Priority Model Results

<!-- b000185 | prose | pages [14] -->
There are two trends with the priority model. The ﬁrst is that as the number of campsites increase, we are able to schedule more trips of diﬀerent varieties. In addition, the carrying capacity this algorithm produces is 12.13, 12.66, 12.94 trips/campsite over 180 days for the uniform distribution and 12.33, 13.45, 13.05 trips/campsite over 180 days for the triangle distributions. The second is that with more trips, the number of crossovers grow exponentially. This is a result of there being

<!-- b000186 | furniture | pages [15] -->
Team # 15420

<!-- b000187 | furniture | pages [15] -->
Page 14 of 20

<!-- b000188 | prose | pages [15] -->
more trips to required to crossover when there are more trips. An example of one of the result is shown in Figure 7.

<!-- b000189 | caption | pages [15] -->
Figure 7: Picture of Y = 225 Target: Uniform. Each line represents a trip. The mix of colors

<!-- b000190 | prose | pages [15] -->
shows the overlap between the trips.

<!-- b000191 | prose | pages [15] -->
5.3

<!-- b000192 | heading | pages [15] -->
Bone Growth Model Results

<!-- b000193 | prose | pages [15] -->
For the Bone Growth Model we used two initial starting Bone Structures:

<!-- b000194 | prose | pages [15] -->
Bones1 =[6, 18, 6, 18, 6, 18, 6, 18, 6, 18, 6, 18, 6, 18, 6, 9, 6]

<!-- b000195 | prose | pages [15] -->
Bones2 =[6, 18, 6, 18, 6, 17, 6, 17, 6, 16, 6, 15, 6, 13, 6, 12, 6, 11, 6, 10, 6]

<!-- b000196 | prose | pages [15] -->
The ﬁrst is fairly uniform in 18’s and 6’s and the second decreases the number of large trips. The ideas was that the ﬁrst bone structure would better match the uniform distribution and the second bone structure would match the triangle distribution better. What we observed is that the bone structures would saturate out all large trip numbers and eventually only have room for shorter trips, leading the skew distributions you see in Figure 8. Although Bones2 did not match our target distributions, it does match qualitatively what we wanted, a triangle distribution as seen in the Lower Left of Figure 8. Bones2 also consistently out performed Bones1 in the number of trips, but this is because Bones2 consisted mainly of shorter trips. This model also produces very symmetrical results as the algorithm it uses mirrors the left and right about the trip in the center. The carrying capacity this algorithm produces is approximately 7.5 trips/campsite over 180 days for both distributions under Bones1 and 9 trips/campsite over 180 days for both distributions under Bones2 (but does not closely match the distributions in Bones2).

<!-- b000197 | furniture | pages [16] -->
Team # 15420

<!-- b000198 | furniture | pages [16] -->
Page 15 of 20

<!-- b000199 | caption | pages [16] -->
Figure 8: Picture of Y = 225 Target: Uniform. Blue is using Bones1. Red is using Bones2.

<!-- b000200 | prose | pages [16] -->
6

<!-- b000201 | heading | pages [16] -->
Analysis of Results

<!-- b000202 | prose | pages [16] -->
In analyzing our models, we considered

<!-- b000203 | prose | pages [16] -->
1. Number of trips in a 6 month period

<!-- b000204 | prose | pages [16] -->
2. Distribution of trip lengths

<!-- b000205 | prose | pages [16] -->
3. Percentage of campsites left open

<!-- b000206 | prose | pages [16] -->
4. Number of crossovers per trip

<!-- b000207 | prose | pages [16] -->
5. Carrying capacity using a given model

<!-- b000208 | prose | pages [16] -->
We evaluated carrying capacity as the ratio of number of trips in a six month period to number of campsites on the river. The carrying capacity could also be evauated using the percentage of campsites ﬁlled.

<!-- b000209 | prose | pages [16] -->
In all our models, there was a tendency of skewing the distribution of trips towards shorter when maximizing campsites used.

<!-- b000210 | prose | pages [16] -->
This is to be expected as it is easier to ﬁt in shorter trips. However it was interesting to note that the Priority Model did better at matching the distribution as the number of campsites increased, while the Bones Growth model started to skew away from the distribution. The Priority Model became increasingly worse with the number of crossovers, increasing to around 29 per trip. However, the average number of crossovers is lower in shorter

<!-- b000211 | furniture | pages [17] -->
Team # 15420

<!-- b000212 | furniture | pages [17] -->
Page 16 of 20

<!-- b000213 | prose | pages [17] -->
trips and the majority of crossovers are from longer trips. We attempted to decrease the number of crossovers, by removing the trips with the highest number of crossovers, but this resulted in removing most long trips and reduced our coverage of campsites by 10-15%. The Bone Growth model was very consistent in its distribution of trips in time and its ability to utilize approximately half of the campsites.

<!-- b000214 | prose | pages [17] -->
6.1

<!-- b000215 | heading | pages [17] -->
Strengths and Weaknesses

<!-- b000216 | heading | pages [17] -->
Priority Model - Strengths

<!-- b000217 | prose | pages [17] -->
• High river carrying capacity

<!-- b000218 | prose | pages [17] -->
– High percentage of campsites ﬁlled

<!-- b000219 | prose | pages [17] -->
– High number of trips in 6 months

<!-- b000220 | prose | pages [17] -->
• Low variance in distance traveled per day

<!-- b000221 | heading | pages [17] -->
Priority Model - Weaknesses

<!-- b000222 | prose | pages [17] -->
• The model makes no attempt to resolve crossovers

<!-- b000223 | prose | pages [17] -->
– Some crossovers cannot be avoided, but a second pass on the output scedule may be

<!-- b000224 | prose | pages [17] -->
able to remove some unnecesary crossovers

<!-- b000225 | prose | pages [17] -->
• The model makes no attempt to reuse space freed in previously scheduled days when trips are removed

<!-- b000226 | prose | pages [17] -->
– Bactracking after removing a trip and re-planning nearby trip may reduce crossovers

<!-- b000227 | prose | pages [17] -->
and travel distance variance

<!-- b000228 | prose | pages [17] -->
• The mechanics of the model distort the input distribution

<!-- b000229 | prose | pages [17] -->
– Long trips constantly have lower distance left

<!-- b000230 | prose | pages [17] -->
ratios and are therefore less likely to get days left preferred campsites

<!-- b000231 | prose | pages [17] -->
– Long trips also have more days that need to be scheduled, and so more chances to be

<!-- b000232 | prose | pages [17] -->
removed

<!-- b000233 | prose | pages [17] -->
• Sensitive to number of trips per day in departures input

<!-- b000234 | prose | pages [17] -->
– If the number of trips is too high, the output distribution skews toward shorter trips.

<!-- b000235 | prose | pages [17] -->
– If number of trips is too low, the campsite utilization and acrrying capacity start to drop

<!-- b000236 | prose | pages [17] -->
signiﬁcantly.

<!-- b000237 | prose | pages [17] -->
– In our experiments, the right number of trips per day was about 12-20.

<!-- b000238 | prose | pages [17] -->
• Sensitive to distribution of trips in departures input

<!-- b000239 | prose | pages [17] -->
– The output distribution skews toward shorter trips, but in a nonlinear fashion.

<!-- b000240 | prose | pages [17] -->
– An input distribution skewed toward longer trips was used obtain an output distribution

<!-- b000241 | prose | pages [17] -->
that was approximateley uniform.

<!-- b000242 | furniture | pages [18] -->
Team # 15420

<!-- b000243 | furniture | pages [18] -->
Page 17 of 20

<!-- b000244 | prose | pages [18] -->
• Sensitive to probability of sort/shuﬄe

<!-- b000245 | prose | pages [18] -->
– Increasing the probability of sorting also skews the output distribution more toward

<!-- b000246 | prose | pages [18] -->
shorter trips.

<!-- b000247 | prose | pages [18] -->
– We found that p ∈[0.3, 0.6] was useful four our tests.

<!-- b000248 | heading | pages [18] -->
Bone Growth Model - Strengths

<!-- b000249 | prose | pages [18] -->
• There are no crossover between any two trips

<!-- b000250 | prose | pages [18] -->
• Trips are be evenly spread out along the whole river

<!-- b000251 | prose | pages [18] -->
• The launch dates of trips are spread out among the 180 days

<!-- b000252 | prose | pages [18] -->
• The model scales well and can be expanded to include oar-powered rubber rafts

<!-- b000253 | heading | pages [18] -->
Bone Growth Model - Weaknesses

<!-- b000254 | prose | pages [18] -->
• Crossovers are not allowed, reducing the total number of trips and campsite coverage

<!-- b000255 | prose | pages [18] -->
• The model is very sensitive to the initial bone structure and the greed algorithm used

<!-- b000256 | prose | pages [18] -->
– After testing the model with two bone structures, our team developed some addional

<!-- b000257 | prose | pages [18] -->
bone structures that could drastically increase campsite usage by sacriﬁcing some other properties. For example, scheduling all the six night trips, followed by all the seven day trips, etc.

<!-- b000258 | prose | pages [18] -->
• Some trips may be pushed to their speed limits or asked to stay at near same campsite to make room for other trips

<!-- b000259 | prose | pages [18] -->
• There are days with high number of launches or high number of arrivals in between days with low activity

<!-- b000260 | prose | pages [18] -->
7

<!-- b000261 | heading | pages [18] -->
Conclusion

<!-- b000262 | prose | pages [18] -->
Overall, there are several diﬀerent ways to address the problem of scheduling rafting trips on the Big Long River. While the na¨ıve algorithm and the density perturbation algorithm did not work very well, the priority model and bone growth model produced the best results covering 80% and 50% of campsites respectively. If the managers of the rafting company decide that it is okay for trips to occassionally pass each other, then the priority model is best since this model uses the highest percentage of the campsites. If the priority algorithm is used, each boat comes into contact with another party less than once ever hour. So while this number is not very large, it still provides some contact with other people during the trip and it is up to the managers of the rafting company to decide whether or not they want to use this model. If the managers of the rafting company want to give the most authentic wildlife experience and not allow trips to ever pass each other, then the bone growth model produces the best results. We can mix the two models over diﬀerent time periods if desired. These models could be extended in many ways. The diﬀerences between scheduling oar-powered rubber rafts and motorized boats, uneven distribution of campsites, and varying spped on diﬀerent

<!-- b000263 | furniture | pages [19] -->
Team # 15420

<!-- b000264 | furniture | pages [19] -->
Page 18 of 20

<!-- b000265 | prose | pages [19] -->
parts of the river are all areas that could be addressed more strongly. Each of these models also has room for individual improvement. We Hypothesize that with more work, either the Bone Growth Model or the Density Perturbation model could be made to produce a globally optimal solution. For the former, we beleive that a carefully constructed starting sequence may be able to yield a schedule with no crossovers and nearly 100% campsite usage. For the latter, we beleive that an application of optimization techniques such as simulated annealing may be able to ﬁnd a globally optimal solution for our loss function. The modeling dommain presented by this problem is vast, and there is a large amount of room for improvement, but we believe that the work we have presented here is a signiﬁcant and succesful attempt at solving this problem.

<!-- b000266 | furniture | pages [20] -->
Team # 15420

<!-- b000267 | furniture | pages [20] -->
Page 19 of 20

<!-- b000268 | heading | pages [20] -->
Memo

<!-- b000269 | prose | pages [20] -->
To: Managers of the Big Long River From: Team # 15420 Date: February 13, 2012 Subject: Rafting Trip Scheduling

<!-- b000270 | prose | pages [20] -->
To generate the best schedule for trips and to determine the carrying capacity of the Big Long River, we have developed two working algorithms. The goal of both algorithms is to maximize the number of trips and campsite usuage, while preventing two trips camping in the same location. We were able to cover 70 % to 50 % of campsites depending on preferences of trip distributions and crossover minization, leading to carrying capacity of approximately 12.5 to 7.5 trips per campsite over 180 days.

<!-- b000271 | prose | pages [20] -->
Both algorithms will generate a schedule of campsite locations for each night for the river guides and a master list trips locations along the river. Both algorithms are able to generate any ratio of trips desired, with launch times fairly uniformly among the six month season.

<!-- b000272 | prose | pages [20] -->
The drawbacks of the models are that we assume that First Launch and Final Exit are able to accomadate as many trips as possible and that the traveling speed along the river is roughly uniform. Of course given more information and time we can adjust these models to account for realistic conditions at First Launch and Final Exit, and along the length of the river.

<!-- b000273 | prose | pages [20] -->
The ﬁrst algorithm (Priority Model) will generate a schedule that better maximizes the number of campsites being used, but will also schedule crossovers. The second algorithm (Bone Growth Model) will generate a schedule that prevents crossovers, but only gets two-thirds as good coverage of campsites as the ﬁrst algorithm. If a middle ground is desired, then you can mix the models over the six month period to allow for diﬀerent pricing options.

<!-- b000274 | prose | pages [20] -->
Sincerely,

<!-- b000275 | furniture | pages [20] -->
Team # 15420

<!-- b000276 | furniture | pages [21] -->
Team # 15420

<!-- b000277 | heading | pages [21] -->
References

<!-- b000278 | furniture | pages [21] -->
Page 20 of 20

<!-- b000279 | references | pages [21] -->
[1] ”River Trips”. Grand Canyon National Park. July 25,

<!-- b000280 | references | pages [21] -->
2011. National Park Service.

<!-- b000281 | references | pages [21] -->
www.nps.gov/grca/planyourvisit/whitewater-rafting.htm

<!-- b000282 | references | pages [21] -->
Hatch

<!-- b000283 | references | pages [21] -->
[2] ”Whitewater

<!-- b000284 | references | pages [21] -->
Resources”.

<!-- b000285 | references | pages [21] -->
www.hatchriverexpeditions.com/faqs.html

<!-- b000286 | references | pages [21] -->
River

<!-- b000287 | references | pages [21] -->
Expeditions.

<!-- b000288 | references | pages [21] -->
2010.

<!-- b000289 | references | pages [21] -->
[3] ”Grand Canyon Trips”. Arizona Raft Adventures. www.azraft.com/

<!-- b000290 | references | pages [21] -->
[4] Robert, Yves and Frederic Vivien. Introduction to Scheduling. FL: Taylor and Francis

<!-- b000291 | references | pages [21] -->
Group, LLC, 2010.

<!-- b000292 | references | pages [21] -->
[5] Rao, Singiresu. Engineering Optimization. 3rd Edition. IN: John Wiley & Sons, 1996.

<!-- b000293 | references | pages [21] -->
[6] Pham, D.T. and D. Karaboga. Intelligent Optimisation Techniques. New York: Springer-

<!-- b000294 | references | pages [21] -->
Verlag, 2000.

<!-- b000295 | references | pages [21] -->
[7] Brucker, Peter. Scheduling Algorithm. 5th Edtion. New York: Springer-Verlag, 2007.

<!-- b000296 | references | pages [21] -->
[8] ”Resources

<!-- b000297 | references | pages [21] -->
for

<!-- b000298 | references | pages [21] -->
Rafting

<!-- b000299 | references | pages [21] -->
Trips”.

<!-- b000300 | references | pages [21] -->
www.whitewatercampsites.com/

<!-- b000301 | references | pages [21] -->
Whitewater

<!-- b000302 | references | pages [21] -->
Campsites.

<!-- b000303 | references | pages [21] -->
2009

<!-- b000304 | references | pages [21] -->
Will

<!-- b000305 | references | pages [21] -->
Hansen.
