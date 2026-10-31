# P-B-2012-15171-ce229936

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
In order to advise the managers of the Big Long River how best to utilize their campsites and maximize the number of boaters they serve in a season, we propose three models, each of which has various strengths and weaknesses and can be applied according to the assumptions the river managers are most inclined to accept. In order to substantiate a number of these assumptions, we use the Colorado River running through Grand Canyon as a real-world analog for the Big Long River. We assume that the demand for boat trips always exceeds supply, which indeed is true regarding rafting permits issued by the National Park Service. We also situate the Big Long River in a geographical location that is similar to that of the Grand Canyon in order to make decisions based on a detailed knowledge of sunrise and sunset times. All three models account for trip durations from 6 to 18 nights, for row boats at 4 miles per hour and motor boats at 8 miles per hour, and for any number of campsites along the river, as long as the spacing of the sites is even. The first model uses an agent-based simulation that assumes each boat acts in its own best interest. This allows boaters to travel without having to follow a predefined itinerary of stops, but opens the possibility that a small fraction (less than 1%) of boaters may have to travel past nightfall to find an open campsite. We find in this model that it is beneficial to require boats to start each day as early as possible and to require the slower row boats to take longer trips (between 12 and 18 nights). The second model produces an itinerary for the river managers at the beginning of the season specifying the required send off dates and stop locations for each boat. Using this approach, it is guaranteed that all boats on the river will be able to find an open campsite in daylight. The algorithm gives precedence to row boats since they have less flexibility in their potential destination sites than motor boats. The itinerary approach allows for seven boats to be launched each day of the season. The third model relies on probability to specify the chance that a given boat will have to travel further than some additional cutoff distance to find an open campsite after they decide they want to stop. Like the first model, this model allows boats to have autonomy regarding where they stop, but there is a smaller than 1% chance that a given boat on the river will have to travel this cutoff distance to find an open campsite. We find in this model that ‘like prefers like;’ that is, row boats generally do better when they only have to compete with other row boats for campsites, and similarly motor boats generally do better when most of their competition comes from other motor boats. Remarkably, despite the different motivations behind our models, all three produce nearly equal values for the maximal seasonal throughput of the river, with between 1150 and 1250 customers served each season when there are 100 campsites along the river. In the best of all situations, the itinerary model can reach up to 1400 customers per season with nearly 100% campsite utilization, though this does introduce a great deal of crowding. Thus, we can confidently say that no matter the approach the river managers choose to take, they can expect a maximum throughput in this range.

<!-- b000002 | furniture | pages [2] -->
Team # 15171

<!-- b000003 | prose | pages [2] -->
To: Managers of Big Long River Adventures, Inc. Date: Monday, February 13, 2012 Subject: Optimization of Seasonal Throughput and Campsite Utilization

<!-- b000004 | prose | pages [2] -->
1. Summary The recent increase in the popularity of the Big Long River as a rafting destination in past years has made clear the need to optimize the utilization of available campsites while capitalizing on the ever-increasing customer base by permitting as many rafts as possible to travel the river each season. Important considerations include boater safety and satisfaction, ease of implementing the scheduling strategy, and conﬁdence in the throughput prediction for the sake of budgeting. To address these considerations, we take into account the times of day during which boats can safely be on the water, the crowding of campsites, a range of potential behaviors for individual boats, and we perform a multiple-model conﬁrmation of the seasonal capacity of the river. Given 100 relatively evenly-spaced campsite along the Big Long River, we can conﬁdently propose a strategy tailored to your needs that will allow between 1150 and 1250 boaters to traverse the river in a season.

<!-- b000005 | prose | pages [2] -->
2. Proposals Itinerary approach: If you can trust your clients to hold to a set itinerary of stops along their journey, we propose using our algorithm to produce an itinerary at the beginning of the season. This itinerary gives which days to send which types of boats, and where these boats should stop. Each customer will be guaranteed to have an open campsite waiting for them that they can reach in a reasonable day’s time. A maximum of about 1400 customers can be sent down the river using this strategy, though this causes a great deal of crowding on the river during the day. Distance-Management approach: If instead you believe that your clients will have variable stops as they travel, the best results can be reached by sending a wave of boats from First Launch each morning and keeping the relative composition of this group with respect to boat type (row or motor) and trip duration as constant as possible from day to day, thus keeping the relative composition of boats on the river nearly constant. You can send between 6 and 7 boats each day using this method and be conﬁdent that under 1% of boats will have to travel an excessive distance to ﬁnd an open campsite at the end of a day.

<!-- b000006 | prose | pages [2] -->
Both of these proposed strategies yield approximately the same throughput, so the choice you make need only depend on the expected behavior of your customers on the river.

<!-- b000007 | prose | pages [2] -->
3. Costs and Benefits There is virtually no economic cost to implementing these strategies, and the beneﬁts are potentially great, depending on your current seasonal capacity. With the second proposal, there is the risk that by chance a larger than expected number of boaters will not be able to ﬁnd an open site within a reasonable distance, potentially leading to unsafe circumstances, though this proposal allows for more individual autonomy than the ﬁrst, enhancing customer satisfaction. The itinerary approach is more dependent than the distance-management approach on keeping all campsites in good working order throughout the season, though if for any reason a campsite must close a new itinerary can be generated, while in the distance-management approach there is enough variability built in that a single closed campsite should not greatly aﬀect satisfaction and throughput.

<!-- b000008 | title | pages [3] -->
OPTIMIZATION OF SEASONAL THROUGHPUT AND

<!-- b000009 | title | pages [3] -->
CAMPSITE UTILIZATION ON THE BIG LONG RIVER

<!-- b000010 | furniture | pages [3] -->
Team # 15171

<!-- b000011 | prose | pages [3] -->
February 12, 2012

<!-- b000012 | heading | pages [3] -->
1 Summary

<!-- b000013 | prose | pages [3] -->
In order to advise the managers of the Big Long River how best to utilize their campsites and maximize the number of boaters they serve in a season, we propose three models, each of which has various strengths and weaknesses and can be applied according to the assumptions the river managers are most inclined to accept. In order to substantiate a number of these assumptions, we use the Colorado River running through Grand Canyon as a real-world analog for the Big Long River. We assume that the demand for boat trips always exceeds supply, which indeed is true regarding rafting permits issued by the National Park Service. We also situate the Big Long River in a geographical location that is similar to that of the Grand Canyon in order to make decisions based on a detailed knowledge of sunrise and sunset times. All three models account for trip durations from 6 to 18 nights, for row boats at 4 miles per hour and motor boats at 8 miles per hour, and for any number of campsites along the river, as long as the spacing of the sites is even.

<!-- b000014 | prose | pages [3] -->
The ﬁrst model uses an agent-based simulation that assumes each boat acts in its own best interest. This allows boaters to travel without having to follow a predeﬁned itinerary of stops, but opens the possibility that a small fraction (less than 1%) of boaters may have to travel past nightfall to ﬁnd an open campsite. We ﬁnd in this model that it is beneﬁcial to require boats to start each day as early as possible and to require the slower row boats to take longer trips (between 12 and 18 nights).

<!-- b000015 | prose | pages [3] -->
The second model produces an itinerary for the river managers at the beginning of the season specifying the required send off dates and stop locations for each boat. Using this approach, it is guaranteed that all boats on the river will be able to ﬁnd an open campsite in daylight. The algorithm gives precedence to row boats since they have less ﬂexibility in their

<!-- b000016 | prose | pages [3] -->
1

<!-- b000017 | furniture | pages [4] -->
Team # 15171

<!-- b000018 | furniture | pages [4] -->
Page 2

<!-- b000019 | prose | pages [4] -->
potential destination sites than motor boats. The itinerary approach allows for seven boats to be launched each day of the season.

<!-- b000020 | prose | pages [4] -->
The third model relies on probability to specify the chance that a given boat will have to travel further than some additional cutoff distance to ﬁnd an open campsite after they decide they want to stop. Like the ﬁrst model, this model allows boats to have autonomy regarding where they stop, but there is a smaller than 1% chance that a given boat on the river will have to travel this cutoff distance to ﬁnd an open campsite. We ﬁnd in this model that ‘like prefers like;’ that is, row boats generally do better when they only have to compete with other row boats for campsites, and similarly motor boats generally do better when most of their competition comes from other motor boats.

<!-- b000021 | prose | pages [4] -->
Remarkably, despite the different motivations behind our models, all three produce nearly equal values for the maximal seasonal throughput of the river, with between 1150 and 1250 customers served each season when there are 100 campsites along the river. In the best of all situations, the itinerary model can reach up to 1400 customers per season with nearly 100% campsite utilization, though this does introduce a great deal of crowding. Thus, we can con- ﬁdently say that no matter the approach the river managers choose to take, they can expect a maximum throughput in this range.

<!-- b000022 | heading | pages [4] -->
2 Introduction

<!-- b000023 | prose | pages [4] -->
The rising popularity of river rafting has lead many park managers to increase the number of allowable trips down these beautiful water ways. The Big Long River is one example where the increased popularity of rafting has lead park managers to consider increasing the number of seasonal visitors. An increase in use provides several challenges for a river. Overuse of a river can overcrowd camps and waterways. This overcrowding diminishes the value to groups traversing the river since only one group should stay at any one of the campsites along the river. Our goal of this paper is to determine the maximum number of groups that can raft down The Big Long River while maintaining the one group per camp site rule. To accomplish this we will be using 3 different models that will be used to determine the carrying capacity of the river for various numbers of camp sties. These models will also provide various optimizations for increasing the carrying capacity of the river.

<!-- b000024 | heading | pages [4] -->
3 Parameters

<!-- b000025 | furniture | pages [5] -->
Team # 15171

<!-- b000026 | furniture | pages [5] -->
Page 3

<!-- b000027 | prose | pages [5] -->
Parameter Deﬁnition Boats per Day ∆X Distance Between Campsites D Start of Day (Sunrise) S End of Day (Sunset) E Boat Speed v # of Campsites Y Utilization µ Failed Boats F Distance Boat Traveled d Daily Goal g # stops a single boat makes n Nights Remaining r

<!-- b000028 | caption | pages [5] -->
Table 1: Parameters

<!-- b000029 | heading | pages [5] -->
4 Assumptions

<!-- b000030 | heading | pages [5] -->
4.1 Common Assumptions

<!-- b000031 | prose | pages [5] -->
In order to ensure that our models are remain valid given various potential constraints, we make a number of assumptions. Before going into detail about our approach, we list those assumptions here.

<!-- b000032 | prose | pages [5] -->
4.1.1 Rafts can only be on the water during daylight

<!-- b000033 | prose | pages [5] -->
Allowing travel at night increases the carrying capacity of the river, but is impractical because whitewater rafting relies on visibility to remain safe. We have therefore chosen to only allow rafts on the water during daylight hours. For the purpose of this problem, daylight hours are deﬁned as the civil twilight hours and daytime. Therefore the day begins when the center of the sun is 6 ◦below the horizon (the beginning of civil twilight). The day ends when the center of the sun is 6 ◦below the horizon (the end of civil dusk). This is the same deﬁnition that the FAA uses to regulate when aircraft are required to use lights, and provides an upper limit on the travel time of each boat [1]. Rafts that end up on the water after sunset will be monitored and used to show that river is above its carrying capacity.

<!-- b000034 | furniture | pages [6] -->
Team # 15171

<!-- b000035 | furniture | pages [6] -->
Page 4

<!-- b000036 | prose | pages [6] -->
4.1.2 Geographic Location

<!-- b000037 | prose | pages [6] -->
For the purpose of calculating daytime hours as described above, we used the Grand Canyons geographic coordinates of 36 ◦3 18.94 N, 112 ◦7 18.61 W. The Colorado River running through the Grand Canyon is 280 miles in length, which is similar to the 225 mile length of Big River speciﬁed in the problem statement [3]. In addition, several rafting companies offer excursions through the Grand Canyon; for example, Arizona River Runners offers trips that vary in length between 6 and 13 days. The similarities between the Grand Canyon and the hypothetical river described in the problem statement made it a natural choice for our model.

<!-- b000038 | prose | pages [6] -->
4.1.3 May 1st though October 31st

<!-- b000039 | prose | pages [6] -->
We assume that the rafting season will run from May 1st through October 31st. This allows us to estimate the amount of daylight available each day, and so ties into our previous assumption that one can only raft during daylight hours. It also sets the total length of the rafting season at 180 days.

<!-- b000040 | prose | pages [6] -->
4.1.4 Length of the river is 225 miles

<!-- b000041 | prose | pages [6] -->
As stated in the problem we will assume that the river in question is 225 miles long. It is worth noting that all of the following models could be adjusted for a river that of a different length.

<!-- b000042 | prose | pages [6] -->
4.1.5 Campsites are evenly spaced along the river

<!-- b000043 | prose | pages [6] -->
The following models assume that there is a ﬁxed distance between each campsite, and that this separation is known.

<!-- b000044 | prose | pages [6] -->
4.1.6 Only two types of boats are on the river, with average speeds of 4mph and 8mph

<!-- b000045 | prose | pages [6] -->
As stated in the problem, only motorized boats which travel at an average speed of 8 mph and oar-powered boats which travel at an average speed of 4 mph are allowed.

<!-- b000046 | prose | pages [6] -->
4.1.7 Boats can only travel down stream

<!-- b000047 | prose | pages [6] -->
For our models, boats will only be allowed to travel downstream. In reality motor boats could feasibly travel upstream but we have made the assumption passengers will only wish to cover the same stretch of river once.

<!-- b000048 | furniture | pages [7] -->
Team # 15171

<!-- b000049 | furniture | pages [7] -->
Page 5

<!-- b000050 | prose | pages [7] -->
4.1.8 Demand of trips always exceeds supply

<!-- b000051 | prose | pages [7] -->
This is a realistic assumption. Demand for noncommercial rafting permits in The Grand Canyon National Park is so high that The National Park Service has created a weighted lot- tery system for applicants [4].

<!-- b000052 | heading | pages [7] -->
4.2 Base Case

<!-- b000053 | prose | pages [7] -->
4.2.1 Only row boats allowed

<!-- b000054 | prose | pages [7] -->
In order to develop this simplest model we have chosen to only allow the slower of the two types of boats.

<!-- b000055 | prose | pages [7] -->
4.2.2 All trips are 6 days

<!-- b000056 | prose | pages [7] -->
This, along with only allowing row boats, will ensure that all boats travel approximately the same distance at the same speed each day.

<!-- b000057 | prose | pages [7] -->
4.2.3 All boats end their days precisely at sunset

<!-- b000058 | prose | pages [7] -->
This allows us to ensure that some boats do not keep traveling after others have stopped, causing bottlenecks at campsites further downstream.

<!-- b000059 | heading | pages [7] -->
4.3 Model 1 (Agent-based model)

<!-- b000060 | prose | pages [7] -->
4.3.1 Boats want to travel approximately the same distance each day

<!-- b000061 | prose | pages [7] -->
If a boat has 100 miles to travel and 10 days to do so, it will try to travel at least 10 miles each day.

<!-- b000062 | heading | pages [7] -->
4.4 Model 2 (Itinerary based model)

<!-- b000063 | prose | pages [7] -->
4.4.1 Boats want to travel approximately the same distance each day

<!-- b000064 | prose | pages [7] -->
Same as described in section 4.3.1

<!-- b000065 | prose | pages [7] -->
4.4.2 The demand for boats of various speed and various trip duration is uniform

<!-- b000066 | prose | pages [7] -->
The length of a given boat’s trip is a uniform(6, 18) random variable (where the parameters 6 and 18 represent lower and upper bounds for the distribution), and the choice of boat speed is a Bernoulli random variable with p = 0.5.

<!-- b000067 | furniture | pages [8] -->
Team # 15171

<!-- b000068 | furniture | pages [8] -->
Page 6

<!-- b000069 | heading | pages [8] -->
4.5 Model 3 (Probabilistic model)

<!-- b000070 | prose | pages [8] -->
4.5.1 The distance a boat travels each day is variable, but the number of stops it makes over the course of its trip is predetermined

<!-- b000071 | prose | pages [8] -->
We make this assumption under the belief that customers will make sure that they spend as many days on the river as they planned to at the start, but that their actual daily travel distance can vary due to various circumstances unrelated to the other boats.

<!-- b000072 | prose | pages [8] -->
4.5.2 The distance a given boat plans to travel in a day can be described by an exponen- tial random variable that is independent of the locations of its previous and future planned stops

<!-- b000073 | prose | pages [8] -->
Exponential random variables are often used to model stopping times and so are well suited for this model. Independence of the outcomes of these variables give us useful mathematical results.

<!-- b000074 | prose | pages [8] -->
4.5.3 The daily send off rate of each different type of boat, taking into account both boat type and trip duration, remains relatively constant throughout the season

<!-- b000075 | prose | pages [8] -->
This assumes that demand from boats of various types remains fairly constant over the course of the season. It provides useful mathematical results.

<!-- b000076 | heading | pages [8] -->
5 Approach

<!-- b000077 | prose | pages [8] -->
In this section we will present our three main model in addition to a simple base case.

<!-- b000078 | heading | pages [8] -->
5.1 Base Case

<!-- b000079 | prose | pages [8] -->
To begin our analysis and optimization of the river rafting problem we need to ﬁrst look at how we can optimize our system for the most basic case. The following list of parameters also includes assumptions made about these parameters:

<!-- b000080 | prose | pages [8] -->
Si = Start time; this is the time of day that boat i leaves from First Launch.

<!-- b000081 | prose | pages [8] -->
E = End time; this is the time of day that all boats will choose to stop rowing.

<!-- b000082 | prose | pages [8] -->
v = Speed of the boats in miles per hour; we assume for now that all boats have the same velocity.

<!-- b000083 | prose | pages [8] -->
D = Distance in miles between campsites.

<!-- b000084 | furniture | pages [9] -->
Team # 15171

<!-- b000085 | furniture | pages [9] -->
Page 7

<!-- b000086 | prose | pages [9] -->
Before developing the model for this section, we rescale these parameters to make them unitless in the following fashion:

<!-- b000087 | prose | pages [9] -->
Express S and E in terms of fractions of a full day; so, the unitless quantities S′ and E′ are calculated by

<!-- b000088 | prose | pages [9] -->
S′ = S/24 and (1) E′ = E/24 (2)

<!-- b000089 | prose | pages [9] -->
where S and E are originally expressed in decimal forms (so the time 4:30pm would be ex- pressed as 16.5).

<!-- b000090 | prose | pages [9] -->
Express v in terms of fraction of the river traveled per day; thus, the rescaled parameter v′ is calculated as v′ = v · 24 (3) 225 when v is expressed in miles per hour.

<!-- b000091 | prose | pages [9] -->
Finally, express D in terms of fractional distance of the river:

<!-- b000092 | prose | pages [9] -->
D′ = D/225 (4)

<!-- b000093 | prose | pages [9] -->
so if the campsites are 5 miles apart, we have D′ = 1/45.

<!-- b000094 | prose | pages [9] -->
Given these parameters, we propose the following equation to give the number of boats that may be sent in a single day: j(E′ −S′)v′ k (5) ∆X = D′ The motivation for this equation is the observation that if all boats are the same speed, we can ﬁll the ﬁrst n campsites on the river, where n is the number of the furthest campsite a boat can reach in a single day. The equation can be understood as

<!-- b000095 | prose | pages [9] -->
n = maximum fraction of the river that a boat can traverse in a single day distance between campsites as a fraction of total river length We ﬁll each campsite from site 1 to site n, and then each day thereafter these boats move as a unit to ﬁll sites n + 1 through 2n, while sites 1 through k are ﬁlled by new boats launched on the second day. In this way, all of the campsites are utilized every evening, and there are no overlaps. This is clearly the optimal way to use campsites, though the assumptions are quite restrictive. Nevertheless, this model will be helpful as a reference point for the following, more complex models.

<!-- b000096 | prose | pages [9, 10] -->
Under the assumption that all boats will stop traveling at precisely the same time of day (E’), the times at which each boat should be sent off each day are calculated by si = E′ −i · D′ for i = 1, 2, . . . , ∆X v′ where si stands for the send off time for boat i.

<!-- b000097 | furniture | pages [10] -->
Team # 15171

<!-- b000098 | furniture | pages [10] -->
Page 8

<!-- b000100 | prose | pages [10] -->
In our further discussion, it will be helpful to bear in mind this models sensitivities to its parameters. We begin by taking the partial derivatives of n with respect to its parameters (in what follows, the ‘prime’ notation of the scaled parameters will be dropped for simplicity):

<!-- b000101 | prose | pages [10] -->
∂E = v ∂n (6) D ∂S = −v ∂n (7) D ∂v = E −S ∂n (8) D ∂D = −(E −S)v ∂n (9) D2

<!-- b000102 | prose | pages [10] -->
Note that for E, S, and v, the partial derivatives yield constant results with respect to the parameters of differentiation, but in the case of D there is an inverse square relationship with the distance between campsites, which makes this derivative very negative for small positive values of D and increases asymptotically to zero as D becomes large. So, the model is particu- larly sensitive to values of D close to zero. In other words, if the campsites are closely spaced, changes in the other parameters will have a greater effect on the model than if the campsites are spaced further. It will be helpful to take note of this general behavior in developing the subsequent models.

<!-- b000103 | furniture | pages [11] -->
Team # 15171

<!-- b000104 | furniture | pages [11] -->
Page 9

<!-- b000105 | heading | pages [11] -->
5.2 Agent-based model

<!-- b000106 | prose | pages [11] -->
To better understand the complexity of this problem we developed an Agent-based model. For this model we simulate the running of boats along the river over an entire season. This model uses discrete 1 minute time steps to simulate the progression of boats down a river. We assume that each boat is a acting independently in its own best interest and provide rules that each boat must follow. The model operates in a ﬁrst come ﬁrst serve basis where the ﬁrst boat to get to a camp claims it. Therefore, there is no centralized planning of where boats camp each night.

<!-- b000107 | prose | pages [11] -->
For this model we deﬁne two failure criteria that if either are satisﬁed result in the boat being counted as a failure.

<!-- b000108 | prose | pages [11] -->
• The boat must travel after sunset to ﬁnd a campsite

<!-- b000109 | prose | pages [11] -->
• The boat must travel longer than 10 hours in one day to ﬁnd an empty camp site

<!-- b000110 | prose | pages [11] -->
5.2.1 Algorithm

<!-- b000111 | prose | pages [11] -->
To decide the type of boats that should be sent and start times of each boat we created several probability distribution functions. For simplicity we choose to initially set the distribution functions to a random uniform distribution.

<!-- b000112 | prose | pages [11] -->
• Start times of individual boats follow draws from a continuous uniform distribution rang- ing from sunrise to 11am

<!-- b000113 | prose | pages [11] -->
• The speed of a given boat (fast or slow) is determined by a Bernoulli random variable with parameter .5.

<!-- b000114 | prose | pages [11] -->
• Length of trips follow a discrete uniform distribution ranging from 6 to 18 nights.

<!-- b000115 | prose | pages [11] -->
The main algorithm used for this model is described below.

<!-- b000116 | prose | pages [11] -->
1. At the start of each day our model will use a set of probability distribution functions to generate the number, attributes, and launch time of the boats for that day.

<!-- b000117 | prose | pages [11] -->
2. Each boat will then calculate a distance goal for the day.

<!-- b000118 | prose | pages [11] -->
g = (225 −d)/(r + 1)

<!-- b000119 | prose | pages [11] -->
This goal is used to decide how far a boat will travel before making camp.

<!-- b000120 | prose | pages [11] -->
3. Each boat will then begin moving along the river.

<!-- b000121 | prose | pages [11, 12] -->
d = d + v/60 4. Each boat will begin looking for an empty camp site after one of the following conditions have been met

<!-- b000122 | furniture | pages [12] -->
Team # 15171

<!-- b000123 | furniture | pages [12] -->
Page 10

<!-- b000125 | prose | pages [12] -->
• The boat has been on the water for longer than 8 hours

<!-- b000126 | prose | pages [12] -->
• The time of day is 2 hours before sunset

<!-- b000127 | prose | pages [12] -->
• The boat has passed its goal for the day

<!-- b000128 | prose | pages [12] -->
5. After the boat has made camp, several attributes will be adjusted for the next day’s trip.

<!-- b000129 | prose | pages [12] -->
The next day’s start time and goal distance will be recalculated using the same methods as before.

<!-- b000130 | prose | pages [12] -->
5.2.2 Optimizations

<!-- b000131 | prose | pages [12] -->
In order to increase the the throughput of our system we can apply several rules to our model that minimize the number of boats meeting our failure criteria.

<!-- b000132 | prose | pages [12] -->
One of our deﬁned failure criteria is having a boat out after dark. In order to minimize the chances of this occurring we move the start times of our boats to earlier in the day. Figure 1 demonstrates the effect of adjusting the distributing of start times for our boats. As we force boats to leave First Launch and each camp site at earlier times we give the boats a longer amount of time to reach their destination. This reduces the number of boats that fail to ﬁnd a camp site each night. One of the problem of this model is that slow boats must spend on average 8hrs a day on the water if they wish to make the trip in 6 nights. This creates a problem where the boats do not have a lot of options in picking a camp before they have satisﬁed our failure conditions. Figure 2 demonstrates this effect over a range of minimum nights for slow boats. By putting less pressure on slow boats to travel long distances each day we reduce the chance of failure. An added beneﬁt of creating longer trips is that camp utilization increases. Figure 3 shows the increased camp utilization as we increase the the minimum number of nights allowed for slow boats.

<!-- b000133 | furniture | pages [13] -->
Team # 15171

<!-- b000134 | furniture | pages [13] -->
Page 11

<!-- b000135 | prose | pages [13] -->
Time Optimization (∆X = 6 y = 100) 18

<!-- b000136 | prose | pages [13] -->
16

<!-- b000137 | prose | pages [13] -->
14 % of boats failing to find camp 12

<!-- b000138 | prose | pages [13] -->
10

<!-- b000139 | prose | pages [13] -->
8

<!-- b000140 | prose | pages [13] -->
6

<!-- b000141 | prose | pages [13] -->
4

<!-- b000142 | prose | pages [13] -->
2 14 8 10 12 16 Max Start Time (hrs)

<!-- b000143 | caption | pages [13] -->
Figure 1: % of boats failing with start time optimization

<!-- b000144 | prose | pages [13] -->
Minimum Nights for Slow Boat (∆X = 6 y = 100) 80

<!-- b000145 | prose | pages [13] -->
78

<!-- b000146 | prose | pages [13] -->
76 Utilization of camp sites 74

<!-- b000147 | prose | pages [13] -->
72

<!-- b000148 | prose | pages [13] -->
70

<!-- b000149 | prose | pages [13] -->
68

<!-- b000150 | prose | pages [13] -->
66 6 8 10 12 14 Minimum Nights Slow Boat

<!-- b000151 | caption | pages [13] -->
Figure 2: % of boats failing with minimum nights for slow boat optimization

<!-- b000152 | prose | pages [13] -->
5.2.3 Results

<!-- b000153 | prose | pages [13, 14] -->
The goal of this model is to provide some insight into how to optimize camp utilization and determine the carrying capacity of the river. The previous section laid out a few key ways Minimum Nights for Slow Boat (∆X = 6 y = 100) 80

<!-- b000154 | furniture | pages [14] -->
Team # 15171

<!-- b000155 | furniture | pages [14] -->
Page 12

<!-- b000157 | prose | pages [14] -->
78

<!-- b000158 | prose | pages [14] -->
76 utlization of camp sites 74

<!-- b000159 | prose | pages [14] -->
72

<!-- b000160 | prose | pages [14] -->
70

<!-- b000161 | prose | pages [14] -->
68

<!-- b000162 | prose | pages [14] -->
66 14 6 8 10 12 Minimum Nights Slow Boat

<!-- b000163 | caption | pages [14] -->
Figure 3: µ with minimum nights for slow boat optimization

<!-- b000164 | prose | pages [14] -->
on how to optimize our model with the goal of decreasing the failure rate of boats traveling down the The Big Long River. After applying these optimization we now need to determine the carrying capacity of our river. For this model we will deﬁne the carrying capacity to be the maximum number of boats per day that can be sent down the river without over 1% of boats meeting our failure criteria.

<!-- b000165 | prose | pages [14] -->
To understand the impact that the average number of boats per day has on the failure rate we increased the average number of boats per day from 1 to 11 for 100 camp sites. Figure 4 shows our results. From the graph it become clear that as we increase the number of boats per day we remain below 1% failure rate until we approach the carrying capacity of the river. After reaching the carrying capacity of the river the failure rate increases linearly as almost all boats added above the carrying capacity end up failing. In addition to maximizing the number of boats that are permitted to journey down the river we also want to optimize the camp utilization.

<!-- b000166 | caption | pages [14] -->
Figure 5 shows how increasing the number of boats launched each day increases the percent of

<!-- b000167 | prose | pages [14] -->
campsites utilized each night for the season.

<!-- b000168 | furniture | pages [15] -->
Team # 15171

<!-- b000169 | furniture | pages [15] -->
Page 13

<!-- b000170 | prose | pages [15] -->
F vs. ∆X (Y = 100) 100

<!-- b000171 | prose | pages [15] -->
80 % of boats failing to find camp 60

<!-- b000172 | prose | pages [15] -->
40

<!-- b000173 | prose | pages [15] -->
20

<!-- b000174 | prose | pages [15] -->
0 4 0 2 6 8 10 ∆X

<!-- b000175 | caption | pages [15] -->
Figure 4: F vs. ∆X (Y=100)

<!-- b000176 | prose | pages [15] -->
µ vs. ∆X (Y = 100) 100

<!-- b000177 | prose | pages [15] -->
80

<!-- b000178 | prose | pages [15] -->
60

<!-- b000179 | prose | pages [15] -->
µ

<!-- b000180 | prose | pages [15] -->
40

<!-- b000181 | prose | pages [15] -->
20

<!-- b000182 | prose | pages [15, 16] -->
0 0 2 4 6 8 10 ∆X F vs. Y (∆X = 7) 10

<!-- b000183 | caption | pages [15] -->
Figure 5: µ vs ∆(Y = 100)

<!-- b000184 | furniture | pages [16] -->
Team # 15171

<!-- b000185 | furniture | pages [16] -->
Page 14

<!-- b000187 | prose | pages [16] -->
8 % of boats failing to find camp 6

<!-- b000188 | prose | pages [16] -->
4

<!-- b000189 | prose | pages [16] -->
2

<!-- b000190 | prose | pages [16] -->
0 50 100 150 200 250 300 350 400 Y

<!-- b000191 | caption | pages [16] -->
Figure 6: F vs. Y (∆= 7)

<!-- b000192 | prose | pages [16] -->
In this model the carrying capacity is directly related to the number of camps available on the river. Figure 7 demonstrates how the carrying capacity of the river increases as the number of camp sites available increases. As we increase the number of camps sites there is a corresponding linear increase in the number of boats that we can push though in a season. If we set the number of campsites to 100 we can push though approximately 1170 boats during a season.

<!-- b000193 | prose | pages [16] -->
In order to verify that we are using our campsites efﬁciently we can look at the utilization of each campsite over 5 simulated seasons. Figure 8 shows the percent utilization of each campsite. From the graph we can see that passengers on The Big Long River avoid campsites near the beginning and end of the river. This produces a low utilization before the 20th mile and after 90th mile. This is a realistic result since most people rafting down The Big Long River would prefer to not have a short ﬁrst or last day. This uneven distribution also has an effect on our calculated utilization of camp sites. Throughout this paper we calculate the utilization using all of the camp sites. However, the low-mile and high-mile campsites are rarely used, causing the utilization of the middle camp sites to be higher than average.

<!-- b000194 | furniture | pages [17] -->
Team # 15171

<!-- b000195 | furniture | pages [17] -->
Page 15

<!-- b000196 | prose | pages [17] -->
Y vs. Total Trips Per Season 2500

<!-- b000197 | prose | pages [17] -->
2000

<!-- b000198 | prose | pages [17] -->
1500

<!-- b000199 | prose | pages [17] -->
X

<!-- b000200 | prose | pages [17] -->
1000

<!-- b000201 | prose | pages [17] -->
500

<!-- b000202 | prose | pages [17] -->
0 0 50 100 150 200 250 Y

<!-- b000203 | caption | pages [17] -->
Figure 7: Max Total Trips Per Season

<!-- b000204 | prose | pages [17] -->
Campsite µ (Y=100, ∆X = 6) 100

<!-- b000205 | prose | pages [17] -->
80

<!-- b000206 | prose | pages [17] -->
60

<!-- b000207 | prose | pages [17] -->
µ

<!-- b000208 | prose | pages [17] -->
40

<!-- b000209 | prose | pages [17] -->
20

<!-- b000210 | prose | pages [17] -->
0 0 20 40 60 80 100 Campsite

<!-- b000211 | caption | pages [17] -->
Figure 8: Campsite µ (∆= 6 Y = 100)

<!-- b000212 | heading | pages [17] -->
5.3 Itinerary Model

<!-- b000213 | prose | pages [17, 18] -->
This model uses an itinerary to schedule the camp site each boat uses for the evening. This model has several advantages. It uses a relatively simple greedy heuristic (described below) to determine the location of each boat. Unlike the agent-based model, there are no surprises with scheduling when a boat is on the river. The model can achieve campsite utilization around 80%, while failing to place rafts in less than 1% of cases.

<!-- b000214 | furniture | pages [18] -->
Team # 15171

<!-- b000215 | furniture | pages [18] -->
Page 16

<!-- b000217 | prose | pages [18] -->
5.3.1 Algorithm

<!-- b000218 | prose | pages [18] -->
A greedy heuristic was used to schedule the itinerary of each boat on the river.

<!-- b000219 | prose | pages [18] -->
1. Each day a constant number of rafts are added to the river. The duration of the trip is chosen by a uniform (6,18) random variable.

<!-- b000220 | prose | pages [18] -->
2. The target campsites for each new boat are chosen as gi = i ∗L/n where i = 1, 2, ..., 6

<!-- b000221 | prose | pages [18] -->
3. All of the boats on the river are sorted by speed so that the 4 mph boats take precedence in scheduling, since they have the least ﬂexibility.

<!-- b000222 | prose | pages [18] -->
4. For each boat on the river, the algorithm checks all unoccupied campsites within the daily travel range of the boat.

<!-- b000223 | prose | pages [18] -->
5. The boat is placed in the open campsite which is closest to the goal for that day.

<!-- b000224 | prose | pages [18] -->
6. If any boat cannot be placed in a campsite for that day, it is removed from the itinerary entirely.

<!-- b000225 | prose | pages [18] -->
7. If any boat fails to reach the end of the river during its duration, it is removed from the itinerary entirely.

<!-- b000226 | prose | pages [18] -->
8. At the end of the simulation a working itinerary is produced for the rafting company.

<!-- b000227 | prose | pages [18] -->
5.3.2 Results

<!-- b000228 | caption | pages [18] -->
Figure 10 shows the plot of campsite utilization vs. the number of rafts added to the river each

<!-- b000229 | prose | pages [18] -->
day.

<!-- b000230 | caption | pages [18] -->
Figure 11 shows the plot of campsite utilization vs. the number of campsites along the

<!-- b000231 | prose | pages [18] -->
river.

<!-- b000232 | caption | pages [18] -->
Figure 12 shows the plot of campsite utilization vs. the number of campsites along the

<!-- b000233 | prose | pages [18] -->
river for ∆X = 7. In this case, there is clear knee in the utilization curve at approximately 80 campsites and the corresponding 90% utilization.

<!-- b000234 | caption | pages [18] -->
Figure 9 shows the plot of unplaceable rafts vs the number of rafts added to the river when

<!-- b000235 | prose | pages [18, 19] -->
Y = 100. After ∆X increases above 7, there is a linear increase in the number of boats that cannot successfully be placed into a campsite over the course of the simulation. However, F vs. ∆X (Y = 100) 500

<!-- b000236 | furniture | pages [19] -->
Team # 15171

<!-- b000237 | furniture | pages [19] -->
Page 17

<!-- b000239 | prose | pages [19] -->
400

<!-- b000240 | prose | pages [19] -->
300

<!-- b000241 | prose | pages [19] -->
Failed rafts 200

<!-- b000242 | prose | pages [19] -->
100

<!-- b000243 | prose | pages [19] -->
0

<!-- b000244 | prose | pages [19] -->
100 4 0 2 6 8 10 12 Rafts added each day

<!-- b000245 | caption | pages [19] -->
Figure 9: Unplaceable Rafts vs. ∆X

<!-- b000246 | prose | pages [19] -->
µ vs. ∆X (Y = 100) 100

<!-- b000247 | prose | pages [19] -->
80

<!-- b000248 | prose | pages [19] -->
Campsite Utilization (%) 60

<!-- b000249 | prose | pages [19] -->
40

<!-- b000250 | prose | pages [19] -->
20

<!-- b000251 | prose | pages [19] -->
0 4 0 2 6 8 10 12 Rafts added each day

<!-- b000252 | caption | pages [19] -->
Figure 10: Utilization vs. ∆X

<!-- b000253 | prose | pages [19, 20] -->
for ∆X ≤6 all of the boats can successfully be placed in campsites over the course of the simulation. At ∆X = 7 there is a small number of boats, less than 1%, that cannot be placed in the simulation. Therefore, the carrying capacity of the river when using the simple greedy F vs. Y (∆X = 7) 700

<!-- b000254 | furniture | pages [20] -->
Team # 15171

<!-- b000255 | furniture | pages [20] -->
Page 18

<!-- b000257 | prose | pages [20] -->
600

<!-- b000258 | prose | pages [20] -->
500

<!-- b000259 | prose | pages [20] -->
400 Failed Rafts 300

<!-- b000260 | prose | pages [20] -->
200

<!-- b000261 | prose | pages [20] -->
100

<!-- b000262 | prose | pages [20] -->
0

<!-- b000263 | prose | pages [20] -->
100 0 50 100 150 200 Campsites

<!-- b000264 | caption | pages [20] -->
Figure 11: Failed Boats vs. Y

<!-- b000265 | prose | pages [20] -->
µ vs. Y (∆X = 7) 100

<!-- b000266 | prose | pages [20] -->
90

<!-- b000267 | prose | pages [20] -->
80

<!-- b000268 | prose | pages [20] -->
Utilization (%) 70

<!-- b000269 | prose | pages [20] -->
60

<!-- b000270 | prose | pages [20] -->
50

<!-- b000271 | prose | pages [20] -->
40

<!-- b000272 | prose | pages [20] -->
30 0 50 100 150 200 Campsites

<!-- b000273 | caption | pages [20] -->
Figure 12: Utilization vs. Y

<!-- b000274 | prose | pages [20] -->
heuristic for boat placement is approximately ∆X = 7.

<!-- b000275 | prose | pages [20] -->
As seen in Figure 10, campsite utilization is nearly constant for ∆X ≥9. In addition, camp utilization at the carrying capacity is approximately 80%.

<!-- b000276 | furniture | pages [21] -->
Team # 15171

<!-- b000277 | furniture | pages [21] -->
Page 19

<!-- b000278 | prose | pages [21] -->
n of Failed Boats vs. ∆X (Y = 100) 16

<!-- b000279 | prose | pages [21] -->
15

<!-- b000280 | prose | pages [21] -->
14

<!-- b000281 | prose | pages [21] -->
13 n of Failed Boats 12

<!-- b000282 | prose | pages [21] -->
11

<!-- b000283 | prose | pages [21] -->
10

<!-- b000284 | prose | pages [21] -->
9

<!-- b000285 | prose | pages [21] -->
8

<!-- b000286 | prose | pages [21] -->
7 5 15 0 10 20 Rafts Added Each Day

<!-- b000287 | caption | pages [21] -->
Figure 13: Average n for Failed Boats vs. ∆X

<!-- b000288 | prose | pages [21] -->
v of Failed Boats vs. ∆X (Y = 100) 9

<!-- b000289 | prose | pages [21] -->
8

<!-- b000290 | prose | pages [21] -->
7 v of Failed Boats 6

<!-- b000291 | prose | pages [21] -->
5

<!-- b000292 | prose | pages [21] -->
4

<!-- b000293 | prose | pages [21] -->
3 5 15 0 10 20 Rafts Added Each Day

<!-- b000294 | caption | pages [21] -->
Figure 14: Average v for Failed Boats vs. ∆X

<!-- b000295 | caption | pages [21] -->
Figure 15 shows the total number of boats that could be successfully placed using the

<!-- b000296 | prose | pages [21, 22] -->
greedy algorithm described in section 5.3.1. At the carrying capacity of the river ∆X = 7, the total number of boats that could be serviced by the river was approximate 1260. This is similar T vs. ∆X (Y = 100) 1600

<!-- b000297 | furniture | pages [22] -->
Team # 15171

<!-- b000298 | furniture | pages [22] -->
Page 20

<!-- b000300 | prose | pages [22] -->
1400

<!-- b000301 | prose | pages [22] -->
1200 Total rafts accommodated 1000

<!-- b000302 | prose | pages [22] -->
800

<!-- b000303 | prose | pages [22] -->
600

<!-- b000304 | prose | pages [22] -->
400

<!-- b000305 | prose | pages [22] -->
200

<!-- b000306 | prose | pages [22] -->
0 4 0 2 6 8 10 12 Rafts added each day

<!-- b000307 | caption | pages [22] -->
Figure 15: Total Placed Boats T vs. ∆X

<!-- b000308 | prose | pages [22] -->
to the carrying capacity estimates of the other algorithms. At this carrying capacity, there is a diminished need for scheduling, because only a small number (about 1% of boats) fail to ﬁnd campsites. However, if the algorithm is overdriven by intentionally using ∆X ≥7 the total number of boats serviced can actually be increased. The algorithm then removes any boats that do not ﬁt into the schedule, and between 1360 and 1400 boats can be serviced during a season. This approaches 100% utilization.

<!-- b000309 | prose | pages [22] -->
It is worth noting that placement failure is not strongly correlated with the speed of the boat (v) for ∆X well above the carrying capacity of the river (∆X > 9). The failure rate of the boats is also not correlated with the number of nights that they spend on the river. This can be seen in Figure 13. Therefore, it should be safe to overdrive the algorithm and place more boats on the river, assuming the demand for various boat speeds and trip length is uniform as described in section 4.4.2. However, campsite utilization approaches 100% when ∆X is this large as seen in Figure 10. Therefore, 1400 approaches the absolute upper limit for the carrying capacity of the river. 1260 at ∆X = 7 may be a more comfortable and realistic number.

<!-- b000310 | prose | pages [22] -->
However, as seen in Figure 14, the average speed of failed boats is approximately 7.5 when ∆X = 7, right at the carrying capacity. This is not surprising, because the greedy heuristic does give precedence to the slower (4 mph) boats since they have less ﬂexibility with scheduling. Still, the total number of boats which cannot ﬁnd a campsite when ∆X = 7 is relatively small, and the tendency for fast boats to fail should not become an issue.

<!-- b000311 | furniture | pages [23] -->
Team # 15171

<!-- b000312 | furniture | pages [23] -->
Page 21

<!-- b000313 | heading | pages [23] -->
5.4 Probability Model

<!-- b000314 | prose | pages [23] -->
The driving question behind this model is: how many boats, of what types, can we send down the Big Long River while keeping the probability that a boat will have to travel more than some cutoff distance to ﬁnd an open campsite within an acceptable range? We make a number of assumptions, many of which are relaxations of the assumptions of previous models:

<!-- b000315 | prose | pages [23] -->
• The actual distance a boat travels each day is variable, but the number of nighttime stops a boat makes is predetermined and non-variable.

<!-- b000316 | prose | pages [23] -->
• The desired daily distance of travel for each boat follows outcomes of an exponential random variable of constant rate, with each outcome independent of all others. Thus, these locations can be modeled as arrivals of a Homogeneous Poisson Process.

<!-- b000317 | prose | pages [23] -->
• The number of boats desiring a certain trip duration sent out each day remains relatively constant; that is, we will not have a single day in which we send only row boats desiring twelve-day trips followed by a single day of sending only motor boats desiring six-day trips. There is very little variation in this respect from one day to the next.

<!-- b000318 | prose | pages [23] -->
• Campsites are placed with equal distance between them.

<!-- b000319 | prose | pages [23] -->
Allowing for variable daily distances is a major strength of this model, since a number of circumstances, from boat problems to medical issues to simple changes of mood, can affect how far an individual boat might travel in a given day. An exponential random variable, and thus a Poisson Process, seems a logical way to model the distance a boat desires to travel each day because each boat will want to average some speciﬁc distance each day (corresponding to the rate of the exponential distribution), but a certain degree of variation can be expected. Note that the location at which a boat desires to stop need not be at a campsite; this maintains the continuous nature of the exponential random variable. It is logical that a group might wish it could stop at a place where there is no campground and yet have to continue until they ﬁnd the ﬁrst open campground.

<!-- b000320 | prose | pages [23] -->
A major mathematical advantage of using a Homogeneous Poisson Process is that if we know the number of arrivals of the process over a given span, the arrivals take the distribution of a uniform random variable[2]. In this model, the number of arrivals for the process is the number of nighttime stops a boat wishes to make, and the given span is the length of the river. Thus, we can model the desired stops of a boat that hopes to spend n nights on the river as n draws from a uniform distribution.

<!-- b000321 | prose | pages [23, 24] -->
We will make two claims to argue that the distribution of desired stop locations for all boats on the river on a single given night also follows N draws from a uniform distribution, where N is the total number of boats on the river. First, we take into account the third assumption above, that the daily send off of each trip duration remains relatively constant. Let us consider all boats that wish to have a twelve day trip, and ignore all others. If we send all of these boats out at once, their distribution on a single night will certainly not be uniform; rather, they will follow the distribution of the minimum of a uniform distribution, and so they will all be grouped toward the beginning of the river. If instead we send one out each day, then by the twelfth night their distribution will indeed be uniform. We apply this logic to each subset of boats desiring a trip length of n days, with n ranging from 6 to 18, and note that given the assumption of consistent send offs, the distribution of all of these boats on a single night will be uniform. Superimposing all of these uniform distributions gives another uniform distribution; thus, with this assumption, the distribution of desired stop locations on a given night for all boats follows a uniform distribution.

<!-- b000322 | furniture | pages [24] -->
Team # 15171

<!-- b000323 | furniture | pages [24] -->
Page 22

<!-- b000325 | prose | pages [24] -->
We are now in a position to answer the question posed at the beginning of this section. Consider Figure 16:

<!-- b000326 | caption | pages [24] -->
Figure 16: Schematic Diagram of Boat Placement

<!-- b000327 | prose | pages [24] -->
The ‘x’ on Figure 16 is the spot where the boat in question wishes to stop. w is the distance to the closest campsite, w + D is the distance to the next closest campsite, w + 2D is the distance to the third closest campsite, and so on. Let us for now assume that all boats on the river are row boats; this assumption will be relaxed later. Let us now imagine that the day is closing and boats are all reaching the locations they desired to go, just as our boat has reached its ‘x’ in Figure 16. As the boats jockey for campgrounds, we want to know the probability that our boat will have to travel some distance δ before ﬁnding an open campground. If we assume that any boat that is in front of ours will reach an open campground ﬁrst (valid since, for now, we assume all boats have the same speed), then the probability becomes the chance that there are either two boats in the span w and none in the adjacent span D, or there is one boat in w and another in D (from this probability we can later compute the probability that our boat will have to travel a distance greater than δ to ﬁnd an open campsite). The probabilities of these two events can be computed as binomials:

<!-- b000328 | furniture | pages [25] -->
Team # 15171

<!-- b000329 | furniture | pages [25] -->
Page 23

<!-- b000330 | prose | pages [25] -->
N −1  (w)2(1 −w)(N−1)−2 P(A) = 2 N −1  (w + D)2(1 −(w + D))(N−1)−2∗ P(B) = 2 2  (w)(1 −w) 1

<!-- b000331 | prose | pages [25] -->
where N is the number of boats on the river at a given time, A is the event that there are two threatening boats in the span w between the boat and the ﬁrst campsite, and B is the probability that there is one boat in the span w and another in the adjacent span D. These equations again take advantage of the scale of w as a fraction of total river length; this allows an effortless conversion between distance and the probability of landing in a given range. Summing these two probabilities gives the total desired probability, that the boat will have to travel some given distance δ to ﬁnd an open campground. The ﬁrst equation is fairly straightforward; it is just P(K = 2) where K is some random variable and K ∼Binomial(N −1, 2). The second equation is more involved; the ﬁrst term, spanning from the ﬁrst combination to just before the second, gives the probability that there are two boats in the span that includes w and D. The second term, spanning from the second combination to the end of the expression, is the probability that exactly one of these boats lies in w. Given this explanation, it is apparent how one might write a similar expression for when the span between the boat and δ includes three or more campsites. The closed form of the general expression is quite cumbersome as it includes a term for every possible distribution of boats between campsites that could possibly block our boat from reaching an open site in a distance less than δ. However, one can develop the full form for any given probability using the guidelines above.

<!-- b000332 | prose | pages [25, 26] -->
We have now laid enough groundwork to relax one last assumption and allow for both row boats and motor boats. Let us again consider the desired stop locations of all boats on the river on a given night. As noted above, the placement of these stop locations follows a uniform distribution. We again want to calculate the probability that a given boat will have to travel a distance δ to ﬁnd an open campsite. Unlike the previous case, if our boat is a row boat (traveling at approximately 4 miles per hour), then there is the chance that it will be overtaken by a motor boat that is further behind it and thus be cheated out of a campsite. Likewise, if our boat is a motorboat (traveling at approximately 8 miles per hour), it has the chance to overtake row boats to reach an open campsite even though the row boats initially begin their search further downstream. As before, we can express the probability of having to travel a distance δ as the probability that there are other boats positioned in certain conﬁgurations so that they can reach the campsites between our boat and δ distance past our boat before our boat can. To generate this probability, we must take into account both the type of our boat and the probability that another given boat on the river is a motorboat.

<!-- b000333 | furniture | pages [26] -->
Team # 15171

<!-- b000334 | furniture | pages [26] -->
Page 24

<!-- b000336 | prose | pages [26] -->
Let us ﬁrst take the case in which our boat is a row boat. Certainly, any type of boat that is in front of us will be able to reach an open campsite before we can. However, we now have to take into account the additional probability that there is a motor boat sufﬁciently close behind us to overtake us and get to an open site before we can. Consider again the instance in Figure 16; the possibility of having motor boats essentially expands the range in which we have to be concerned about other boats to an additional distance ∆behind our boat, where ∆is the distance between our boat and the campsite in question (the motorboats can travel twice as fast as the row boats, so they can cover a distance of 2∆in the time our row boat can travel a distance of ∆). Thus, the probabilities become

<!-- b000337 | prose | pages [26] -->
N −1  P(A′) = (w + pfw)2(1 −(w + pfw))(N−1)−2 2 N −1  P(B′) = (w + D + pfD)2(1 −(w + D + pfD))(N−1)−2∗ 2 2  (w + pfw)(1 −(w + pfw)) 1

<!-- b000338 | prose | pages [26] -->
Here, pf is the probability that a boat on the river is a motor boat, and the probabilities in the binomial expressions take into account the chance that there is a motor boat sufﬁciently close behind to overtake our boat. A′ is the event that there are two threatening boats before the ﬁrst campsite and B′ is the event that there is one threatening boat before the ﬁrst campsite and an additional boat between the ﬁrst and second campsites.

<!-- b000339 | prose | pages [26] -->
The case in which our boat is a motor boat is similar. Now, rather than concerning ourselves with boats that are behind us, we want to know if there are any row boats sufﬁciently close in front of us for us to overtake. Noting that we will overtake any row boat that is further than half of our own distance from the site we desire, we construct the following probabilities:

<!-- b000340 | prose | pages [26, 27] -->
(N−1)−2 N −1 w −(1 −pf)w w −(1 −pf)w  2  P(A′′) = 1 − 2 2 2 N −1 w + D −(1 −pf)(w + D)  2 P(B′′) = ∗ 2 2 (N−1)−2 w + D −(1 −pf)(w + D)   1 − ∗ 2 w −(1 −pf)w w −(1 −pf)w 2     1 − 1 2 2 Here, A′′ is the event that there are two threatening boats in front of us, such as one motor boat and one row boat that is further than half our distance to the ﬁrst campsite. B′′ is the event that there is one threatening boat between us and the closest campsite and one between the closest and the next closest campsite.

<!-- b000341 | furniture | pages [27] -->
Team # 15171

<!-- b000342 | furniture | pages [27] -->
Page 25

<!-- b000344 | prose | pages [27] -->
Figures 17, 19, and 18 (Appendix) show the dependence of these probabilities on the num- ber of boats on the water; they show the probability that a fast boat will have to travel 14 miles (just under two hours) to ﬁnd an open campsite. Figures 21, 20, and 22 (Appendix) show the corresponding results for a slow boat. Figures 17 and 20 show the results for a river with 29 campsites, Figures 18 and 21 show the results for a river with 59 campsites, and Figures 19 and 22 show the results for a river with 99 campsites. Note, in agreement with the analysis in the simplest model, there is a great deal of variation in the model results corresponding to campsite placement. In the results for both types of boats, the number of boats that can feasibly be sent down the river greatly increases as the distance between campsites decreases (and thus the total number of campsites increases). In addition, we see that it is more favorable for row boats to have most of their competition for campsites coming from other rowboats, while it is more favorable for motor boats to have most of their competition coming from motor boats.

<!-- b000345 | prose | pages [27] -->
To conclude this section, we will consider what seems to be the most likely case for the Big Long River and make a recommendation for how to best schedule departures from First Launch, assuming that boats will not follow a predetermined itinerary. If the Big Long River indeed has 99 campsites, which seems feasible along its 225 mile length, up to 77 boats can be allowed on the river at a time if there are equal numbers of row boats and motor boats, and this will ensure that an average of only 1% of customers have to travel 14 miles to ﬁnd a campsite. At the beginning of the season, an constant mix of boat types and trip lengths should be sent out each day until the river reaches its capacity of 77 boats. Once it reaches capacity, the boats that ﬁnish should be monitored so that a new boat of similar characteristics can be launched soon thereafter, keeping the relative proportions of the 77 boats as constant as possible. Assuming that the average trip length is twelve days, we can expect to launch an average of 77 boats every twelve days. Over the course of the 180-day season, this gives a 1,155 boat capacity per season for the Big Long River.

<!-- b000346 | heading | pages [27] -->
6 Conclusion

<!-- b000347 | prose | pages [27] -->
To conclude, we expand on the joint results of all three models, closely examine their strengths and weaknesses, and propose extensions.

<!-- b000348 | furniture | pages [28] -->
Team # 15171

<!-- b000349 | furniture | pages [28] -->
Page 26

<!-- b000350 | heading | pages [28] -->
6.1 Overall Results

<!-- b000351 | prose | pages [28] -->
Perhaps the most striking and valuable result is that all three models propose a maximum seasonal throughput for the Big Long River as some value between 1150 and 1250 boats, with up to 1400 allowed if the itinerary model is used and there is a high tolerance for daytime crowding on the river. Despite this common conclusion, the differing motivations behind the models allow each to provide unique insight into the behavior of boats on the river. The agent- based model shows the importance of starting boats early in the day and restricting the duration of trips by slower boats to twelve or more days. The itinerary-based model suggests that placement preference should go to the slower boats, which are more restricted in their range of potential campsites each night. The probabilistic model advocates for keeping the relative proportions of each type of boat constant over the course of the season and adjusting this proportion depending on whether the rafting management wishes to favor oar or motor boats. Taken together, these results provide a good picture as to how the river should be managed. A manager who is conﬁdent that he or she can trust boats to travel to predetermined campsites and is comfortable with turning down some potential customers should pick the itinerary-based approach, thus preventing any one boat from having to travel in potentially unsafe conditions. A manager who believes that the boaters cannot be trusted to travel to a pre-speciﬁed campsite each evening should rely on the agent-based and probabilistic models, sending out a wave of boats each morning and keeping the relative proportion of each type of boat on the river constant, knowing that each boat runs some small chance of having to travel an exceedingly long distance to ﬁnd an open campsite. Regardless of the approach chosen, the manager can be conﬁdent that their choice will not negatively affect the total number of people they serve in a season.

<!-- b000352 | heading | pages [28] -->
6.2 Strengths, Weaknesses, and Extensions

<!-- b000353 | prose | pages [28, 29] -->
As mentioned above, these models taken together have the advantage of catering to a degree of assumptions a river manager is willing to make regarding trustworthiness of the boaters and danger of having a raft spend a long time searching for an open campsite. They also all reach similar results regarding the river’s seasonal capacity, making this ﬁgure particularly trustworthy. However, all three models rely on the perhaps restrictive assumption that the campsites along the river are perfectly evenly spaced. A logical and straightforward extension to this set of models would be to relax this assumption by, in the case of the agent-based and itinerary models, generating the locations of campsites from a continuous uniform distribution, and in the case of the probabilistic model, analyzing the probability of having an excessive number of boats between a randomly placed boat and a randomly placed campsite, rather than a ﬁxed campsite. Another extension could involve adding dependence on weather to the progression of boats down the river. The probabilistic model does not account for this because it assumes that all variations in the boats’ desired stopping locations are due to independent factors, but storms would likely affect all or a signiﬁcant subset of the boats at once. A ﬁnal potential extension not addressed by these models would be to study how the demand from various types of boats and trip lengths changes over the course of a season and then work this variation into the models to better reﬂect the true client`ele of the Big Long River.

<!-- b000354 | furniture | pages [29] -->
Team # 15171

<!-- b000355 | furniture | pages [29] -->
Page 27

<!-- b000357 | furniture | pages [30] -->
Team # 15171

<!-- b000358 | furniture | pages [30] -->
Page 28

<!-- b000359 | heading | pages [30] -->
7 Appendix

<!-- b000360 | heading | pages [30] -->
7.1 Probabilistic Model

<!-- b000361 | prose | pages [30] -->
The following ﬁgures are visualizations of results from the probabilistic model:

<!-- b000362 | prose | pages [30] -->
Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.25

<!-- b000363 | prose | pages [30] -->
P(fast) = .1 P(fast) = .25 P(fast) = .5 P(fast) = .75 P(fast) = .9 0.2 1% cutoff Probability of having to travel an additional 14 miles Other Parameters:

<!-- b000364 | prose | pages [30] -->
Location on river = 28.125 miles (1/8 of river length) 0.15 Distance between sites = 7.5 miles (1/30 of river length) Total # of Campsites = 29

<!-- b000365 | prose | pages [30] -->
0.1

<!-- b000366 | prose | pages [30] -->
0.05

<!-- b000367 | prose | pages [30, 31] -->
0 0 10 20 30 40 50 60 70 80 90 100 Number of Boats Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.2 P(fast) = .1 P(fast) = .25 0.18 P(fast) = .5 P(fast) = .75 P(fast) = .9 0.16 1% cutoff

<!-- b000368 | caption | pages [30] -->
Figure 17: Probability a Fast Boat must travel 14 miles - Far Campsites

<!-- b000369 | furniture | pages [31] -->
Team # 15171

<!-- b000370 | furniture | pages [31] -->
Page 29

<!-- b000372 | prose | pages [31] -->
Probability of having to travel an additional 14 miles Other Parameters: 0.14 Location on river = 28.125 miles (1/8 of river length) Distance between sites = 3.75 0.12 miles (1/60 of river length) Total # of Campsites = 59 0.1

<!-- b000373 | prose | pages [31] -->
0.08

<!-- b000374 | prose | pages [31] -->
0.06

<!-- b000375 | prose | pages [31] -->
0.04

<!-- b000376 | prose | pages [31] -->
0.02

<!-- b000377 | prose | pages [31, 32] -->
0 0 10 20 30 40 50 60 70 80 90 100 Number of Boats Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.06

<!-- b000378 | caption | pages [31] -->
Figure 18: Probability a Fast Boat must travel 14 miles - Medium-Distance Campsites

<!-- b000379 | furniture | pages [32] -->
Team # 15171

<!-- b000380 | furniture | pages [32] -->
Page 30

<!-- b000382 | prose | pages [32] -->
P(fast) = .1 P(fast) = .25 P(fast) = .5 P(fast) = .75 0.05 P(fast) = .9 1% cutoff

<!-- b000383 | prose | pages [32] -->
Probability of having to travel an additional 14 miles Other Parameters: Location on river = 28.125 0.04 miles (1/8 of river length) Distance between sites = 1.25 miles (1/100 of river length) Total # of Campsites = 99 0.03

<!-- b000384 | prose | pages [32] -->
0.02

<!-- b000385 | prose | pages [32] -->
0.01

<!-- b000386 | prose | pages [32, 33] -->
0 0 10 20 30 40 50 60 70 80 90 100 Number of Boats Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.25

<!-- b000387 | caption | pages [32] -->
Figure 19: Probability a Fast Boat must travel 14 miles - Close Campsites

<!-- b000388 | furniture | pages [33] -->
Team # 15171

<!-- b000389 | furniture | pages [33] -->
Page 31

<!-- b000391 | prose | pages [33] -->
P(fast) = .1 P(fast) = .25 P(fast) = .5 P(fast) = .75 P(fast) = .9 0.2 1% cutoff

<!-- b000392 | prose | pages [33] -->
Other Parameters: Probability of having to travel an additional 14 miles Location on river = 28.125 miles (1/8 of river length) Distance between sites = 7.5 0.15 miles (1/30 of river length) Total # of Campsites = 29

<!-- b000393 | prose | pages [33] -->
0.1

<!-- b000394 | prose | pages [33] -->
0.05

<!-- b000395 | prose | pages [33, 34] -->
0 0 10 20 30 40 50 60 70 80 90 100 Number of Boats Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.25

<!-- b000396 | caption | pages [33] -->
Figure 20: Probability a Slow Boat must travel 14 miles - Far Campsites

<!-- b000397 | furniture | pages [34] -->
Team # 15171

<!-- b000398 | furniture | pages [34] -->
Page 32

<!-- b000400 | prose | pages [34] -->
P(fast) = .1 P(fast) = .25 P(fast) = .5 P(fast) = .75 P(fast) = .9 0.2 1% cutoff Probability of having to travel an additional 14 miles Other Parameters:

<!-- b000401 | prose | pages [34] -->
Location on river = 28.125 miles (1/8 of riverlength) 0.15 Distance between sites = 3.75 miles (1/60 of river length) Total # of Campsites = 59

<!-- b000402 | prose | pages [34] -->
0.1

<!-- b000403 | prose | pages [34] -->
0.05

<!-- b000404 | prose | pages [34, 35] -->
0 0 10 20 30 40 50 60 70 80 90 100 Number of Boats Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.07

<!-- b000405 | caption | pages [34] -->
Figure 21: Probability a Slow Boat must travel 14 miles - Medium-Distance Campsites

<!-- b000406 | furniture | pages [35] -->
Team # 15171

<!-- b000407 | furniture | pages [35] -->
Page 33

<!-- b000409 | prose | pages [35] -->
P(fast) = .1 P(fast) = .25 0.06 P(fast) = .5 P(fast) = .75 P(fast) = .9 Probability of having to travel an additional 14 miles 1% cutoff 0.05 Other Parameters: Location on river = 28.125 miles (1/8 of river length) 0.04 Distance between sites = 1.25 miles (1/100 of river length) Total # of Campsites = 99 0.03

<!-- b000410 | prose | pages [35] -->
0.02

<!-- b000411 | prose | pages [35] -->
0.01

<!-- b000412 | prose | pages [35] -->
0 0 10 20 30 40 50 60 70 80 90 100 Number of Boats

<!-- b000413 | caption | pages [35] -->
Figure 22: Probability a Slow Boat must travel 14 miles - Close Campsites

<!-- b000414 | furniture | pages [36] -->
Team # 15171

<!-- b000415 | furniture | pages [36] -->
Page 34

<!-- b000416 | heading | pages [36] -->
References

<!-- b000417 | references | pages [36] -->
[1] Federal Aviation Administration. Code of federal regulations sec 91.205. http://www.

<!-- b000418 | references | pages [36] -->
airweb.faa.gov/Regulatory_and_Guidance_Library/rgFAR.nsf/,

<!-- b000419 | references | pages [36] -->
2007.

<!-- b000420 | references | pages [36] -->
[2] Rick Durrett. Essentials of Stochastic Processes. Springer, Ithica, NY, 1999.

<!-- b000421 | references | pages [36] -->
http://www.

<!-- b000422 | references | pages [36] -->
[3] Arizona River Runners.

<!-- b000423 | references | pages [36] -->
Colorado river rafting in arizona.

<!-- b000424 | references | pages [36] -->
raftarizona.com/, 2011.

<!-- b000425 | references | pages [36] -->
http://www.nps.gov/grca/planyourvisit/

<!-- b000426 | references | pages [36] -->
[4] National

<!-- b000427 | references | pages [36] -->
Park

<!-- b000428 | references | pages [36] -->
Service.

<!-- b000429 | references | pages [36] -->
weightedlottery.htm, 2012.
