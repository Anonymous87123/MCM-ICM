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

<!-- b000008 | prose | pages [3] -->
OPTIMIZATION OF SEASONAL THROUGHPUT AND

<!-- b000009 | prose | pages [3] -->
CAMPSITE UTILIZATION ON THE BIG LONG RIVER

<!-- b000010 | furniture | pages [3] -->
Team # 15171

<!-- b000011 | prose | pages [3] -->
February 12, 2012

<!-- b000012 | prose | pages [3] -->
1

<!-- b000013 | heading | pages [3] -->
Summary

<!-- b000014 | prose | pages [3] -->
In order to advise the managers of the Big Long River how best to utilize their campsites and

<!-- b000015 | prose | pages [3] -->
maximize the number of boaters they serve in a season, we propose three models, each of which

<!-- b000016 | prose | pages [3] -->
has various strengths and weaknesses and can be applied according to the assumptions the river

<!-- b000017 | prose | pages [3] -->
managers are most inclined to accept. In order to substantiate a number of these assumptions,

<!-- b000018 | prose | pages [3] -->
we use the Colorado River running through Grand Canyon as a real-world analog for the Big

<!-- b000019 | prose | pages [3] -->
Long River. We assume that the demand for boat trips always exceeds supply, which indeed

<!-- b000020 | prose | pages [3] -->
is true regarding rafting permits issued by the National Park Service. We also situate the Big

<!-- b000021 | prose | pages [3] -->
Long River in a geographical location that is similar to that of the Grand Canyon in order to

<!-- b000022 | prose | pages [3] -->
make decisions based on a detailed knowledge of sunrise and sunset times. All three models

<!-- b000023 | prose | pages [3] -->
account for trip durations from 6 to 18 nights, for row boats at 4 miles per hour and motor boats

<!-- b000024 | prose | pages [3] -->
at 8 miles per hour, and for any number of campsites along the river, as long as the spacing of

<!-- b000025 | prose | pages [3] -->
the sites is even.

<!-- b000026 | prose | pages [3] -->
The ﬁrst model uses an agent-based simulation that assumes each boat acts in its own best

<!-- b000027 | prose | pages [3] -->
interest. This allows boaters to travel without having to follow a predeﬁned itinerary of stops,

<!-- b000028 | prose | pages [3] -->
but opens the possibility that a small fraction (less than 1%) of boaters may have to travel past

<!-- b000029 | prose | pages [3] -->
nightfall to ﬁnd an open campsite. We ﬁnd in this model that it is beneﬁcial to require boats

<!-- b000030 | prose | pages [3] -->
to start each day as early as possible and to require the slower row boats to take longer trips

<!-- b000031 | prose | pages [3] -->
(between 12 and 18 nights).

<!-- b000032 | prose | pages [3] -->
The second model produces an itinerary for the river managers at the beginning of the

<!-- b000033 | prose | pages [3] -->
season specifying the required send off dates and stop locations for each boat. Using this

<!-- b000034 | prose | pages [3] -->
approach, it is guaranteed that all boats on the river will be able to ﬁnd an open campsite in

<!-- b000035 | prose | pages [3] -->
daylight. The algorithm gives precedence to row boats since they have less ﬂexibility in their

<!-- b000036 | prose | pages [3] -->
1

<!-- b000037 | furniture | pages [4] -->
Team # 15171

<!-- b000038 | furniture | pages [4] -->
Page 2

<!-- b000039 | prose | pages [4] -->
potential destination sites than motor boats. The itinerary approach allows for seven boats to

<!-- b000040 | prose | pages [4] -->
be launched each day of the season.

<!-- b000041 | prose | pages [4] -->
The third model relies on probability to specify the chance that a given boat will have to

<!-- b000042 | prose | pages [4] -->
travel further than some additional cutoff distance to ﬁnd an open campsite after they decide

<!-- b000043 | prose | pages [4] -->
they want to stop. Like the ﬁrst model, this model allows boats to have autonomy regarding

<!-- b000044 | prose | pages [4] -->
where they stop, but there is a smaller than 1% chance that a given boat on the river will have to

<!-- b000045 | prose | pages [4] -->
travel this cutoff distance to ﬁnd an open campsite. We ﬁnd in this model that ‘like prefers like;’

<!-- b000046 | prose | pages [4] -->
that is, row boats generally do better when they only have to compete with other row boats for

<!-- b000047 | prose | pages [4] -->
campsites, and similarly motor boats generally do better when most of their competition comes

<!-- b000048 | prose | pages [4] -->
from other motor boats.

<!-- b000049 | prose | pages [4] -->
Remarkably, despite the different motivations behind our models, all three produce nearly

<!-- b000050 | prose | pages [4] -->
equal values for the maximal seasonal throughput of the river, with between 1150 and 1250

<!-- b000051 | prose | pages [4] -->
customers served each season when there are 100 campsites along the river. In the best of all

<!-- b000052 | prose | pages [4] -->
situations, the itinerary model can reach up to 1400 customers per season with nearly 100%

<!-- b000053 | prose | pages [4] -->
campsite utilization, though this does introduce a great deal of crowding. Thus, we can con-

<!-- b000054 | prose | pages [4] -->
ﬁdently say that no matter the approach the river managers choose to take, they can expect a

<!-- b000055 | prose | pages [4] -->
maximum throughput in this range.

<!-- b000056 | prose | pages [4] -->
2

<!-- b000057 | heading | pages [4] -->
Introduction

<!-- b000058 | prose | pages [4] -->
The rising popularity of river rafting has lead many park managers to increase the number of

<!-- b000059 | prose | pages [4] -->
allowable trips down these beautiful water ways. The Big Long River is one example where

<!-- b000060 | prose | pages [4] -->
the increased popularity of rafting has lead park managers to consider increasing the number

<!-- b000061 | prose | pages [4] -->
of seasonal visitors. An increase in use provides several challenges for a river. Overuse of a

<!-- b000062 | prose | pages [4] -->
river can overcrowd camps and waterways. This overcrowding diminishes the value to groups

<!-- b000063 | prose | pages [4] -->
traversing the river since only one group should stay at any one of the campsites along the river.

<!-- b000064 | prose | pages [4] -->
Our goal of this paper is to determine the maximum number of groups that can raft down The

<!-- b000065 | prose | pages [4] -->
Big Long River while maintaining the one group per camp site rule. To accomplish this we

<!-- b000066 | prose | pages [4] -->
will be using 3 different models that will be used to determine the carrying capacity of the river

<!-- b000067 | prose | pages [4] -->
for various numbers of camp sties. These models will also provide various optimizations for

<!-- b000068 | prose | pages [4] -->
increasing the carrying capacity of the river.

<!-- b000069 | prose | pages [4] -->
3 Parameters

<!-- b000070 | furniture | pages [5] -->
Team # 15171

<!-- b000071 | furniture | pages [5] -->
Page 3

<!-- b000072 | prose | pages [5] -->
Parameter Deﬁnition

<!-- b000073 | prose | pages [5] -->
Boats per Day ∆X

<!-- b000074 | prose | pages [5] -->
Distance Between Campsites D

<!-- b000075 | prose | pages [5] -->
Start of Day (Sunrise) S

<!-- b000076 | prose | pages [5] -->
End of Day (Sunset) E

<!-- b000077 | prose | pages [5] -->
Boat Speed v

<!-- b000078 | prose | pages [5] -->
# of Campsites Y

<!-- b000079 | prose | pages [5] -->
Utilization µ

<!-- b000080 | prose | pages [5] -->
Failed Boats F

<!-- b000081 | prose | pages [5] -->
Distance Boat Traveled d

<!-- b000082 | prose | pages [5] -->
Daily Goal g

<!-- b000083 | prose | pages [5] -->
# stops a single boat makes n

<!-- b000084 | prose | pages [5] -->
Nights Remaining r

<!-- b000085 | caption | pages [5] -->
Table 1: Parameters

<!-- b000086 | prose | pages [5] -->
4

<!-- b000087 | heading | pages [5] -->
Assumptions

<!-- b000088 | prose | pages [5] -->
4.1

<!-- b000089 | heading | pages [5] -->
Common Assumptions

<!-- b000090 | prose | pages [5] -->
In order to ensure that our models are remain valid given various potential constraints, we

<!-- b000091 | prose | pages [5] -->
make a number of assumptions. Before going into detail about our approach, we list those

<!-- b000092 | prose | pages [5] -->
assumptions here.

<!-- b000093 | prose | pages [5] -->
4.1.1 Rafts can only be on the water during daylight

<!-- b000094 | prose | pages [5] -->
Allowing travel at night increases the carrying capacity of the river, but is impractical because

<!-- b000095 | prose | pages [5] -->
whitewater rafting relies on visibility to remain safe. We have therefore chosen to only allow

<!-- b000096 | prose | pages [5] -->
rafts on the water during daylight hours. For the purpose of this problem, daylight hours are

<!-- b000097 | prose | pages [5] -->
deﬁned as the civil twilight hours and daytime. Therefore the day begins when the center of

<!-- b000098 | prose | pages [5] -->
the sun is 6 ◦below the horizon (the beginning of civil twilight). The day ends when the center

<!-- b000099 | prose | pages [5] -->
of the sun is 6 ◦below the horizon (the end of civil dusk). This is the same deﬁnition that the

<!-- b000100 | prose | pages [5] -->
FAA uses to regulate when aircraft are required to use lights, and provides an upper limit on

<!-- b000101 | prose | pages [5] -->
the travel time of each boat [1]. Rafts that end up on the water after sunset will be monitored

<!-- b000102 | prose | pages [5] -->
and used to show that river is above its carrying capacity.

<!-- b000103 | furniture | pages [6] -->
Team # 15171

<!-- b000104 | furniture | pages [6] -->
Page 4

<!-- b000105 | prose | pages [6] -->
4.1.2 Geographic Location

<!-- b000106 | prose | pages [6] -->
For the purpose of calculating daytime hours as described above, we used the Grand Canyons

<!-- b000107 | prose | pages [6] -->
geographic coordinates of 36 ◦3 18.94 N, 112 ◦7 18.61 W. The Colorado River running through

<!-- b000108 | prose | pages [6] -->
the Grand Canyon is 280 miles in length, which is similar to the 225 mile length of Big River

<!-- b000109 | prose | pages [6] -->
speciﬁed in the problem statement [3]. In addition, several rafting companies offer excursions

<!-- b000110 | prose | pages [6] -->
through the Grand Canyon; for example, Arizona River Runners offers trips that vary in length

<!-- b000111 | prose | pages [6] -->
between 6 and 13 days. The similarities between the Grand Canyon and the hypothetical river

<!-- b000112 | prose | pages [6] -->
described in the problem statement made it a natural choice for our model.

<!-- b000113 | prose | pages [6] -->
4.1.3 May 1st though October 31st

<!-- b000114 | prose | pages [6] -->
We assume that the rafting season will run from May 1st through October 31st. This allows us

<!-- b000115 | prose | pages [6] -->
to estimate the amount of daylight available each day, and so ties into our previous assumption

<!-- b000116 | prose | pages [6] -->
that one can only raft during daylight hours. It also sets the total length of the rafting season at

<!-- b000117 | prose | pages [6] -->
180 days.

<!-- b000118 | prose | pages [6] -->
4.1.4 Length of the river is 225 miles

<!-- b000119 | prose | pages [6] -->
As stated in the problem we will assume that the river in question is 225 miles long. It is worth

<!-- b000120 | prose | pages [6] -->
noting that all of the following models could be adjusted for a river that of a different length.

<!-- b000121 | prose | pages [6] -->
4.1.5 Campsites are evenly spaced along the river

<!-- b000122 | prose | pages [6] -->
The following models assume that there is a ﬁxed distance between each campsite, and that

<!-- b000123 | prose | pages [6] -->
this separation is known.

<!-- b000124 | prose | pages [6] -->
4.1.6 Only two types of boats are on the river, with average speeds of 4mph and 8mph

<!-- b000125 | prose | pages [6] -->
As stated in the problem, only motorized boats which travel at an average speed of 8 mph and

<!-- b000126 | prose | pages [6] -->
oar-powered boats which travel at an average speed of 4 mph are allowed.

<!-- b000127 | prose | pages [6] -->
4.1.7 Boats can only travel down stream

<!-- b000128 | prose | pages [6] -->
For our models, boats will only be allowed to travel downstream. In reality motor boats could

<!-- b000129 | prose | pages [6] -->
feasibly travel upstream but we have made the assumption passengers will only wish to cover

<!-- b000130 | prose | pages [6] -->
the same stretch of river once.

<!-- b000131 | furniture | pages [7] -->
Team # 15171

<!-- b000132 | furniture | pages [7] -->
Page 5

<!-- b000133 | prose | pages [7] -->
4.1.8 Demand of trips always exceeds supply

<!-- b000134 | prose | pages [7] -->
This is a realistic assumption.

<!-- b000135 | prose | pages [7] -->
Demand for noncommercial rafting permits in The Grand

<!-- b000136 | prose | pages [7] -->
Canyon National Park is so high that The National Park Service has created a weighted lot-

<!-- b000137 | prose | pages [7] -->
tery system for applicants [4].

<!-- b000138 | prose | pages [7] -->
4.2 Base Case

<!-- b000139 | prose | pages [7] -->
4.2.1 Only row boats allowed

<!-- b000140 | prose | pages [7] -->
In order to develop this simplest model we have chosen to only allow the slower of the two

<!-- b000141 | prose | pages [7] -->
types of boats.

<!-- b000142 | prose | pages [7] -->
4.2.2 All trips are 6 days

<!-- b000143 | prose | pages [7] -->
This, along with only allowing row boats, will ensure that all boats travel approximately the

<!-- b000144 | prose | pages [7] -->
same distance at the same speed each day.

<!-- b000145 | prose | pages [7] -->
4.2.3 All boats end their days precisely at sunset

<!-- b000146 | prose | pages [7] -->
This allows us to ensure that some boats do not keep traveling after others have stopped, causing

<!-- b000147 | prose | pages [7] -->
bottlenecks at campsites further downstream.

<!-- b000148 | prose | pages [7] -->
4.3

<!-- b000149 | heading | pages [7] -->
Model 1 (Agent-based model)

<!-- b000150 | prose | pages [7] -->
4.3.1 Boats want to travel approximately the same distance each day

<!-- b000151 | prose | pages [7] -->
If a boat has 100 miles to travel and 10 days to do so, it will try to travel at least 10 miles each

<!-- b000152 | prose | pages [7] -->
day.

<!-- b000153 | prose | pages [7] -->
4.4

<!-- b000154 | heading | pages [7] -->
Model 2 (Itinerary based model)

<!-- b000155 | prose | pages [7] -->
4.4.1 Boats want to travel approximately the same distance each day

<!-- b000156 | prose | pages [7] -->
Same as described in section 4.3.1

<!-- b000157 | prose | pages [7] -->
4.4.2 The demand for boats of various speed and various trip duration is uniform

<!-- b000158 | prose | pages [7] -->
The length of a given boat’s trip is a uniform(6, 18) random variable (where the parameters 6

<!-- b000159 | prose | pages [7] -->
and 18 represent lower and upper bounds for the distribution), and the choice of boat speed is

<!-- b000160 | prose | pages [7] -->
a Bernoulli random variable with p = 0.5.

<!-- b000161 | furniture | pages [8] -->
Team # 15171

<!-- b000162 | furniture | pages [8] -->
Page 6

<!-- b000163 | prose | pages [8] -->
4.5

<!-- b000164 | heading | pages [8] -->
Model 3 (Probabilistic model)

<!-- b000165 | prose | pages [8] -->
4.5.1 The distance a boat travels each day is variable, but the number of stops it makes

<!-- b000166 | prose | pages [8] -->
over the course of its trip is predetermined

<!-- b000167 | prose | pages [8] -->
We make this assumption under the belief that customers will make sure that they spend as

<!-- b000168 | prose | pages [8] -->
many days on the river as they planned to at the start, but that their actual daily travel distance

<!-- b000169 | prose | pages [8] -->
can vary due to various circumstances unrelated to the other boats.

<!-- b000170 | prose | pages [8] -->
4.5.2 The distance a given boat plans to travel in a day can be described by an exponen-

<!-- b000171 | prose | pages [8] -->
tial random variable that is independent of the locations of its previous and future

<!-- b000172 | prose | pages [8] -->
planned stops

<!-- b000173 | prose | pages [8] -->
Exponential random variables are often used to model stopping times and so are well suited

<!-- b000174 | prose | pages [8] -->
for this model. Independence of the outcomes of these variables give us useful mathematical

<!-- b000175 | prose | pages [8] -->
results.

<!-- b000176 | prose | pages [8] -->
4.5.3 The daily send off rate of each different type of boat, taking into account both boat

<!-- b000177 | prose | pages [8] -->
type and trip duration, remains relatively constant throughout the season

<!-- b000178 | prose | pages [8] -->
This assumes that demand from boats of various types remains fairly constant over the course

<!-- b000179 | prose | pages [8] -->
of the season. It provides useful mathematical results.

<!-- b000180 | prose | pages [8] -->
5 Approach

<!-- b000181 | prose | pages [8] -->
In this section we will present our three main model in addition to a simple base case.

<!-- b000182 | prose | pages [8] -->
5.1 Base Case

<!-- b000183 | prose | pages [8] -->
To begin our analysis and optimization of the river rafting problem we need to ﬁrst look at

<!-- b000184 | prose | pages [8] -->
how we can optimize our system for the most basic case. The following list of parameters also

<!-- b000185 | prose | pages [8] -->
includes assumptions made about these parameters:

<!-- b000186 | prose | pages [8] -->
Si = Start time; this is the time of day that boat i leaves from First Launch.

<!-- b000187 | prose | pages [8] -->
E = End time; this is the time of day that all boats will choose to stop rowing.

<!-- b000188 | prose | pages [8] -->
v = Speed of the boats in miles per hour; we assume for now that all boats have the same velocity.

<!-- b000189 | prose | pages [8] -->
D = Distance in miles between campsites.

<!-- b000190 | furniture | pages [9] -->
Team # 15171

<!-- b000191 | furniture | pages [9] -->
Page 7

<!-- b000192 | prose | pages [9] -->
Before developing the model for this section, we rescale these parameters to make them unitless

<!-- b000193 | prose | pages [9] -->
in the following fashion:

<!-- b000194 | prose | pages [9] -->
Express S and E in terms of fractions of a full day; so, the unitless quantities S′ and E′ are

<!-- b000195 | prose | pages [9] -->
calculated by

<!-- b000196 | prose | pages [9] -->
S′ = S/24 and (1)

<!-- b000197 | prose | pages [9] -->
E′ = E/24 (2)

<!-- b000198 | prose | pages [9] -->
where S and E are originally expressed in decimal forms (so the time 4:30pm would be ex-

<!-- b000199 | prose | pages [9] -->
pressed as 16.5).

<!-- b000200 | prose | pages [9] -->
Express v in terms of fraction of the river traveled per day; thus, the rescaled parameter v′

<!-- b000201 | prose | pages [9] -->
is calculated as

<!-- b000202 | prose | pages [9] -->
v′ = v · 24

<!-- b000203 | prose | pages [9] -->
when v is expressed in miles per hour.

<!-- b000204 | prose | pages [9] -->
(3) 225

<!-- b000205 | prose | pages [9] -->
Finally, express D in terms of fractional distance of the river:

<!-- b000206 | prose | pages [9] -->
D′ = D/225 (4)

<!-- b000207 | prose | pages [9] -->
so if the campsites are 5 miles apart, we have D′ = 1/45.

<!-- b000208 | prose | pages [9] -->
Given these parameters, we propose the following equation to give the number of boats that

<!-- b000209 | prose | pages [9] -->
may be sent in a single day:

<!-- b000210 | prose | pages [9] -->
j(E′ −S′)v′

<!-- b000211 | prose | pages [9] -->
∆X =

<!-- b000212 | prose | pages [9] -->
k

<!-- b000213 | prose | pages [9] -->
(5)

<!-- b000214 | prose | pages [9] -->
D′

<!-- b000215 | prose | pages [9] -->
The motivation for this equation is the observation that if all boats are the same speed, we can

<!-- b000216 | prose | pages [9] -->
ﬁll the ﬁrst n campsites on the river, where n is the number of the furthest campsite a boat can

<!-- b000217 | prose | pages [9] -->
reach in a single day. The equation can be understood as

<!-- b000218 | prose | pages [9] -->
n = maximum fraction of the river that a boat can traverse in a single day

<!-- b000219 | prose | pages [9] -->
distance between campsites as a fraction of total river length

<!-- b000220 | prose | pages [9] -->
We ﬁll each campsite from site 1 to site n, and then each day thereafter these boats move

<!-- b000221 | prose | pages [9] -->
as a unit to ﬁll sites n + 1 through 2n, while sites 1 through k are ﬁlled by new boats launched

<!-- b000222 | prose | pages [9] -->
on the second day. In this way, all of the campsites are utilized every evening, and there are no

<!-- b000223 | prose | pages [9] -->
overlaps. This is clearly the optimal way to use campsites, though the assumptions are quite

<!-- b000224 | prose | pages [9] -->
restrictive. Nevertheless, this model will be helpful as a reference point for the following, more

<!-- b000225 | prose | pages [9] -->
complex models.

<!-- b000226 | prose | pages [9] -->
Under the assumption that all boats will stop traveling at precisely the same time of day

<!-- b000227 | prose | pages [9] -->
(E’), the times at which each boat should be sent off each day are calculated by

<!-- b000228 | furniture | pages [10] -->
Team # 15171

<!-- b000229 | prose | pages [10] -->
si = E′ −i · D′

<!-- b000230 | furniture | pages [10] -->
Page 8

<!-- b000231 | prose | pages [10] -->
for i = 1, 2, . . . , ∆X v′

<!-- b000232 | prose | pages [10] -->
where si stands for the send off time for boat i.

<!-- b000233 | prose | pages [10] -->
In our further discussion, it will be helpful to bear in mind this models sensitivities to its

<!-- b000234 | prose | pages [10] -->
parameters. We begin by taking the partial derivatives of n with respect to its parameters (in

<!-- b000235 | prose | pages [10] -->
what follows, the ‘prime’ notation of the scaled parameters will be dropped for simplicity):

<!-- b000236 | prose | pages [10] -->
∂n ∂E = v

<!-- b000237 | prose | pages [10] -->
D

<!-- b000238 | prose | pages [10] -->
∂S = −v ∂n

<!-- b000239 | prose | pages [10] -->
(6)

<!-- b000240 | prose | pages [10] -->
(7) D

<!-- b000241 | prose | pages [10] -->
∂v = E −S ∂n

<!-- b000242 | prose | pages [10] -->
(8) D

<!-- b000243 | prose | pages [10] -->
∂D = −(E −S)v ∂n

<!-- b000244 | prose | pages [10] -->
(9) D2

<!-- b000245 | prose | pages [10] -->
Note that for E, S, and v, the partial derivatives yield constant results with respect to the

<!-- b000246 | prose | pages [10] -->
parameters of differentiation, but in the case of D there is an inverse square relationship with

<!-- b000247 | prose | pages [10] -->
the distance between campsites, which makes this derivative very negative for small positive

<!-- b000248 | prose | pages [10] -->
values of D and increases asymptotically to zero as D becomes large. So, the model is particu-

<!-- b000249 | prose | pages [10] -->
larly sensitive to values of D close to zero. In other words, if the campsites are closely spaced,

<!-- b000250 | prose | pages [10] -->
changes in the other parameters will have a greater effect on the model than if the campsites

<!-- b000251 | prose | pages [10] -->
are spaced further. It will be helpful to take note of this general behavior in developing the

<!-- b000252 | prose | pages [10] -->
subsequent models.

<!-- b000253 | furniture | pages [11] -->
Team # 15171

<!-- b000254 | furniture | pages [11] -->
Page 9

<!-- b000255 | prose | pages [11] -->
5.2

<!-- b000256 | heading | pages [11] -->
Agent-based model

<!-- b000257 | prose | pages [11] -->
To better understand the complexity of this problem we developed an Agent-based model. For

<!-- b000258 | prose | pages [11] -->
this model we simulate the running of boats along the river over an entire season. This model

<!-- b000259 | prose | pages [11] -->
uses discrete 1 minute time steps to simulate the progression of boats down a river. We assume

<!-- b000260 | prose | pages [11] -->
that each boat is a acting independently in its own best interest and provide rules that each boat

<!-- b000261 | prose | pages [11] -->
must follow. The model operates in a ﬁrst come ﬁrst serve basis where the ﬁrst boat to get to a

<!-- b000262 | prose | pages [11] -->
camp claims it. Therefore, there is no centralized planning of where boats camp each night.

<!-- b000263 | prose | pages [11] -->
For this model we deﬁne two failure criteria that if either are satisﬁed result in the boat

<!-- b000264 | prose | pages [11] -->
being counted as a failure.

<!-- b000265 | prose | pages [11] -->
• The boat must travel after sunset to ﬁnd a campsite

<!-- b000266 | prose | pages [11] -->
• The boat must travel longer than 10 hours in one day to ﬁnd an empty camp site

<!-- b000267 | prose | pages [11] -->
5.2.1 Algorithm

<!-- b000268 | prose | pages [11] -->
To decide the type of boats that should be sent and start times of each boat we created several

<!-- b000269 | prose | pages [11] -->
probability distribution functions. For simplicity we choose to initially set the distribution

<!-- b000270 | prose | pages [11] -->
functions to a random uniform distribution.

<!-- b000271 | prose | pages [11] -->
• Start times of individual boats follow draws from a continuous uniform distribution rang-

<!-- b000272 | prose | pages [11] -->
ing from sunrise to 11am

<!-- b000273 | prose | pages [11] -->
• The speed of a given boat (fast or slow) is determined by a Bernoulli random variable

<!-- b000274 | prose | pages [11] -->
with parameter .5.

<!-- b000275 | prose | pages [11] -->
• Length of trips follow a discrete uniform distribution ranging from 6 to 18 nights.

<!-- b000276 | prose | pages [11] -->
The main algorithm used for this model is described below.

<!-- b000277 | prose | pages [11] -->
1. At the start of each day our model will use a set of probability distribution functions to

<!-- b000278 | prose | pages [11] -->
generate the number, attributes, and launch time of the boats for that day.

<!-- b000279 | prose | pages [11] -->
2. Each boat will then calculate a distance goal for the day.

<!-- b000280 | prose | pages [11] -->
g = (225 −d)/(r + 1)

<!-- b000281 | prose | pages [11] -->
This goal is used to decide how far a boat will travel before making camp.

<!-- b000282 | prose | pages [11] -->
3. Each boat will then begin moving along the river.

<!-- b000283 | prose | pages [11] -->
d = d + v/60

<!-- b000284 | furniture | pages [12] -->
Team # 15171

<!-- b000285 | furniture | pages [12] -->
Page 10

<!-- b000286 | prose | pages [12] -->
4. Each boat will begin looking for an empty camp site after one of the following conditions

<!-- b000287 | prose | pages [12] -->
have been met

<!-- b000288 | prose | pages [12] -->
• The boat has been on the water for longer than 8 hours

<!-- b000289 | prose | pages [12] -->
• The time of day is 2 hours before sunset

<!-- b000290 | prose | pages [12] -->
• The boat has passed its goal for the day

<!-- b000291 | prose | pages [12] -->
5. After the boat has made camp, several attributes will be adjusted for the next day’s trip.

<!-- b000292 | prose | pages [12] -->
The next day’s start time and goal distance will be recalculated using the same methods

<!-- b000293 | prose | pages [12] -->
as before.

<!-- b000294 | prose | pages [12] -->
5.2.2 Optimizations

<!-- b000295 | prose | pages [12] -->
In order to increase the the throughput of our system we can apply several rules to our model

<!-- b000296 | prose | pages [12] -->
that minimize the number of boats meeting our failure criteria.

<!-- b000297 | prose | pages [12] -->
One of our deﬁned failure criteria is having a boat out after dark. In order to minimize the

<!-- b000298 | prose | pages [12] -->
chances of this occurring we move the start times of our boats to earlier in the day. Figure 1

<!-- b000299 | prose | pages [12] -->
demonstrates the effect of adjusting the distributing of start times for our boats. As we force

<!-- b000300 | prose | pages [12] -->
boats to leave First Launch and each camp site at earlier times we give the boats a longer

<!-- b000301 | prose | pages [12] -->
amount of time to reach their destination. This reduces the number of boats that fail to ﬁnd a

<!-- b000302 | prose | pages [12] -->
camp site each night. One of the problem of this model is that slow boats must spend on average

<!-- b000303 | prose | pages [12] -->
8hrs a day on the water if they wish to make the trip in 6 nights. This creates a problem where

<!-- b000304 | prose | pages [12] -->
the boats do not have a lot of options in picking a camp before they have satisﬁed our failure

<!-- b000305 | prose | pages [12] -->
conditions. Figure 2 demonstrates this effect over a range of minimum nights for slow boats.

<!-- b000306 | prose | pages [12] -->
By putting less pressure on slow boats to travel long distances each day we reduce the chance

<!-- b000307 | prose | pages [12] -->
of failure. An added beneﬁt of creating longer trips is that camp utilization increases. Figure 3

<!-- b000308 | prose | pages [12] -->
shows the increased camp utilization as we increase the the minimum number of nights allowed

<!-- b000309 | prose | pages [12] -->
for slow boats.

<!-- b000310 | furniture | pages [13] -->
Team # 15171

<!-- b000311 | furniture | pages [13] -->
Page 11

<!-- b000312 | prose | pages [13] -->
Time Optimization (∆X = 6 y = 100)

<!-- b000313 | prose | pages [13] -->
18

<!-- b000314 | prose | pages [13] -->
16

<!-- b000315 | prose | pages [13] -->
14

<!-- b000316 | prose | pages [13] -->
% of boats failing to find camp

<!-- b000317 | prose | pages [13] -->
12

<!-- b000318 | prose | pages [13] -->
10

<!-- b000319 | prose | pages [13] -->
8

<!-- b000320 | prose | pages [13] -->
6

<!-- b000321 | prose | pages [13] -->
4

<!-- b000322 | prose | pages [13] -->
2

<!-- b000323 | prose | pages [13] -->
8 10 14 12 16 Max Start Time (hrs)

<!-- b000324 | caption | pages [13] -->
Figure 1: % of boats failing with start time optimization

<!-- b000325 | prose | pages [13] -->
Minimum Nights for Slow Boat (∆X = 6 y = 100)

<!-- b000326 | prose | pages [13] -->
80

<!-- b000327 | prose | pages [13] -->
78

<!-- b000328 | prose | pages [13] -->
76

<!-- b000329 | prose | pages [13] -->
Utilization of camp sites

<!-- b000330 | prose | pages [13] -->
74

<!-- b000331 | prose | pages [13] -->
72

<!-- b000332 | prose | pages [13] -->
70

<!-- b000333 | prose | pages [13] -->
68

<!-- b000334 | prose | pages [13] -->
66

<!-- b000335 | prose | pages [13] -->
6 8 14 10 12 Minimum Nights Slow Boat

<!-- b000336 | caption | pages [13] -->
Figure 2: % of boats failing with minimum nights for slow boat optimization

<!-- b000337 | prose | pages [13] -->
5.2.3 Results

<!-- b000338 | prose | pages [13] -->
The goal of this model is to provide some insight into how to optimize camp utilization and

<!-- b000339 | prose | pages [13] -->
determine the carrying capacity of the river. The previous section laid out a few key ways

<!-- b000340 | furniture | pages [14] -->
Team # 15171

<!-- b000341 | furniture | pages [14] -->
Page 12

<!-- b000342 | prose | pages [14] -->
Minimum Nights for Slow Boat (∆X = 6 y = 100)

<!-- b000343 | prose | pages [14] -->
80

<!-- b000344 | prose | pages [14] -->
78

<!-- b000345 | prose | pages [14] -->
76

<!-- b000346 | prose | pages [14] -->
utlization of camp sites

<!-- b000347 | prose | pages [14] -->
74

<!-- b000348 | prose | pages [14] -->
72

<!-- b000349 | prose | pages [14] -->
70

<!-- b000350 | prose | pages [14] -->
68

<!-- b000351 | prose | pages [14] -->
66

<!-- b000352 | prose | pages [14] -->
14 6 8 10 12 Minimum Nights Slow Boat

<!-- b000353 | caption | pages [14] -->
Figure 3: µ with minimum nights for slow boat optimization

<!-- b000354 | prose | pages [14] -->
on how to optimize our model with the goal of decreasing the failure rate of boats traveling

<!-- b000355 | prose | pages [14] -->
down the The Big Long River. After applying these optimization we now need to determine

<!-- b000356 | prose | pages [14] -->
the carrying capacity of our river. For this model we will deﬁne the carrying capacity to be the

<!-- b000357 | prose | pages [14] -->
maximum number of boats per day that can be sent down the river without over 1% of boats

<!-- b000358 | prose | pages [14] -->
meeting our failure criteria.

<!-- b000359 | prose | pages [14] -->
To understand the impact that the average number of boats per day has on the failure rate

<!-- b000360 | prose | pages [14] -->
we increased the average number of boats per day from 1 to 11 for 100 camp sites. Figure 4

<!-- b000361 | prose | pages [14] -->
shows our results. From the graph it become clear that as we increase the number of boats per

<!-- b000362 | prose | pages [14] -->
day we remain below 1% failure rate until we approach the carrying capacity of the river. After

<!-- b000363 | prose | pages [14] -->
reaching the carrying capacity of the river the failure rate increases linearly as almost all boats

<!-- b000364 | prose | pages [14] -->
added above the carrying capacity end up failing. In addition to maximizing the number of

<!-- b000365 | prose | pages [14] -->
boats that are permitted to journey down the river we also want to optimize the camp utilization.

<!-- b000366 | caption | pages [14] -->
Figure 5 shows how increasing the number of boats launched each day increases the percent of

<!-- b000367 | prose | pages [14] -->
campsites utilized each night for the season.

<!-- b000368 | furniture | pages [15] -->
Team # 15171

<!-- b000369 | furniture | pages [15] -->
Page 13

<!-- b000370 | prose | pages [15] -->
F vs. ∆X (Y = 100)

<!-- b000371 | prose | pages [15] -->
100

<!-- b000372 | prose | pages [15] -->
80

<!-- b000373 | prose | pages [15] -->
% of boats failing to find camp

<!-- b000374 | prose | pages [15] -->
60

<!-- b000375 | prose | pages [15] -->
40

<!-- b000376 | prose | pages [15] -->
20

<!-- b000377 | prose | pages [15] -->
0

<!-- b000378 | prose | pages [15] -->
4 0 2 6 8 10 ∆X

<!-- b000379 | caption | pages [15] -->
Figure 4: F vs. ∆X (Y=100)

<!-- b000380 | prose | pages [15] -->
µ vs. ∆X (Y = 100)

<!-- b000381 | prose | pages [15] -->
100

<!-- b000382 | prose | pages [15] -->
80

<!-- b000383 | prose | pages [15] -->
60

<!-- b000384 | prose | pages [15] -->
µ

<!-- b000385 | prose | pages [15] -->
40

<!-- b000386 | prose | pages [15] -->
20

<!-- b000387 | prose | pages [15] -->
0

<!-- b000388 | prose | pages [15] -->
4 0 2 6 8 10 ∆X

<!-- b000389 | caption | pages [15] -->
Figure 5: µ vs ∆(Y = 100)

<!-- b000390 | furniture | pages [16] -->
Team # 15171

<!-- b000391 | furniture | pages [16] -->
Page 14

<!-- b000392 | prose | pages [16] -->
F vs. Y (∆X = 7)

<!-- b000393 | prose | pages [16] -->
10

<!-- b000394 | prose | pages [16] -->
8

<!-- b000395 | prose | pages [16] -->
% of boats failing to find camp

<!-- b000396 | prose | pages [16] -->
6

<!-- b000397 | prose | pages [16] -->
4

<!-- b000398 | prose | pages [16] -->
2

<!-- b000399 | prose | pages [16] -->
0

<!-- b000400 | prose | pages [16] -->
50 100 150 200 250 300 350 400 Y Y

<!-- b000401 | caption | pages [16] -->
Figure 6: F vs. Y (∆= 7)

<!-- b000402 | prose | pages [16] -->
In this model the carrying capacity is directly related to the number of camps available

<!-- b000403 | prose | pages [16] -->
on the river. Figure 7 demonstrates how the carrying capacity of the river increases as the

<!-- b000404 | prose | pages [16] -->
number of camp sites available increases. As we increase the number of camps sites there is a

<!-- b000405 | prose | pages [16] -->
corresponding linear increase in the number of boats that we can push though in a season. If

<!-- b000406 | prose | pages [16] -->
we set the number of campsites to 100 we can push though approximately 1170 boats during a

<!-- b000407 | prose | pages [16] -->
season.

<!-- b000408 | prose | pages [16] -->
In order to verify that we are using our campsites efﬁciently we can look at the utilization

<!-- b000409 | prose | pages [16] -->
of each campsite over 5 simulated seasons. Figure 8 shows the percent utilization of each

<!-- b000410 | prose | pages [16] -->
campsite. From the graph we can see that passengers on The Big Long River avoid campsites

<!-- b000411 | prose | pages [16] -->
near the beginning and end of the river. This produces a low utilization before the 20th mile and

<!-- b000412 | prose | pages [16] -->
after 90th mile. This is a realistic result since most people rafting down The Big Long River

<!-- b000413 | prose | pages [16] -->
would prefer to not have a short ﬁrst or last day. This uneven distribution also has an effect

<!-- b000414 | prose | pages [16] -->
on our calculated utilization of camp sites. Throughout this paper we calculate the utilization

<!-- b000415 | prose | pages [16] -->
using all of the camp sites. However, the low-mile and high-mile campsites are rarely used,

<!-- b000416 | prose | pages [16] -->
causing the utilization of the middle camp sites to be higher than average.

<!-- b000417 | furniture | pages [17] -->
Team # 15171

<!-- b000418 | furniture | pages [17] -->
Page 15

<!-- b000419 | prose | pages [17] -->
Y vs. Total Trips Per Season

<!-- b000420 | prose | pages [17] -->
2500

<!-- b000421 | prose | pages [17] -->
2000

<!-- b000422 | prose | pages [17] -->
1500

<!-- b000423 | prose | pages [17] -->
X

<!-- b000424 | prose | pages [17] -->
1000

<!-- b000425 | prose | pages [17] -->
500

<!-- b000426 | prose | pages [17] -->
0

<!-- b000427 | prose | pages [17] -->
0 50 100 150 200 250 Y Y

<!-- b000428 | caption | pages [17] -->
Figure 7: Max Total Trips Per Season

<!-- b000429 | prose | pages [17] -->
Campsite µ (Y=100, ∆X = 6)

<!-- b000430 | prose | pages [17] -->
100

<!-- b000431 | prose | pages [17] -->
80

<!-- b000432 | prose | pages [17] -->
60

<!-- b000433 | prose | pages [17] -->
µ

<!-- b000434 | prose | pages [17] -->
40

<!-- b000435 | prose | pages [17] -->
20

<!-- b000436 | prose | pages [17] -->
0

<!-- b000437 | prose | pages [17] -->
0 20 40 60 80 100 Campsite

<!-- b000438 | caption | pages [17] -->
Figure 8: Campsite µ (∆= 6 Y = 100)

<!-- b000439 | prose | pages [17] -->
5.3

<!-- b000440 | heading | pages [17] -->
Itinerary Model

<!-- b000441 | prose | pages [17] -->
This model uses an itinerary to schedule the camp site each boat uses for the evening. This

<!-- b000442 | prose | pages [17] -->
model has several advantages. It uses a relatively simple greedy heuristic (described below)

<!-- b000443 | furniture | pages [18] -->
Team # 15171

<!-- b000444 | furniture | pages [18] -->
Page 16

<!-- b000445 | prose | pages [18] -->
to determine the location of each boat. Unlike the agent-based model, there are no surprises

<!-- b000446 | prose | pages [18] -->
with scheduling when a boat is on the river. The model can achieve campsite utilization around

<!-- b000447 | prose | pages [18] -->
80%, while failing to place rafts in less than 1% of cases.

<!-- b000448 | prose | pages [18] -->
5.3.1 Algorithm

<!-- b000449 | prose | pages [18] -->
A greedy heuristic was used to schedule the itinerary of each boat on the river.

<!-- b000450 | prose | pages [18] -->
1. Each day a constant number of rafts are added to the river. The duration of the trip is

<!-- b000451 | prose | pages [18] -->
chosen by a uniform (6,18) random variable.

<!-- b000452 | prose | pages [18] -->
2. The target campsites for each new boat are chosen as gi = i ∗L/n where i = 1, 2, ..., 6

<!-- b000453 | prose | pages [18] -->
3. All of the boats on the river are sorted by speed so that the 4 mph boats take precedence

<!-- b000454 | prose | pages [18] -->
in scheduling, since they have the least ﬂexibility.

<!-- b000455 | prose | pages [18] -->
4. For each boat on the river, the algorithm checks all unoccupied campsites within the

<!-- b000456 | prose | pages [18] -->
daily travel range of the boat.

<!-- b000457 | prose | pages [18] -->
5. The boat is placed in the open campsite which is closest to the goal for that day.

<!-- b000458 | prose | pages [18] -->
6. If any boat cannot be placed in a campsite for that day, it is removed from the itinerary

<!-- b000459 | prose | pages [18] -->
entirely.

<!-- b000460 | prose | pages [18] -->
7. If any boat fails to reach the end of the river during its duration, it is removed from the

<!-- b000461 | prose | pages [18] -->
itinerary entirely.

<!-- b000462 | prose | pages [18] -->
8. At the end of the simulation a working itinerary is produced for the rafting company.

<!-- b000463 | prose | pages [18] -->
5.3.2 Results

<!-- b000464 | caption | pages [18] -->
Figure 10 shows the plot of campsite utilization vs. the number of rafts added to the river each

<!-- b000465 | prose | pages [18] -->
day.

<!-- b000466 | caption | pages [18] -->
Figure 11 shows the plot of campsite utilization vs. the number of campsites along the

<!-- b000467 | prose | pages [18] -->
river.

<!-- b000468 | caption | pages [18] -->
Figure 12 shows the plot of campsite utilization vs. the number of campsites along the

<!-- b000469 | prose | pages [18] -->
river for ∆X = 7. In this case, there is clear knee in the utilization curve at approximately 80

<!-- b000470 | prose | pages [18] -->
campsites and the corresponding 90% utilization.

<!-- b000471 | caption | pages [18] -->
Figure 9 shows the plot of unplaceable rafts vs the number of rafts added to the river when

<!-- b000472 | prose | pages [18] -->
Y = 100. After ∆X increases above 7, there is a linear increase in the number of boats that

<!-- b000473 | prose | pages [18] -->
cannot successfully be placed into a campsite over the course of the simulation. However,

<!-- b000474 | furniture | pages [19] -->
Team # 15171

<!-- b000475 | furniture | pages [19] -->
Page 17

<!-- b000476 | prose | pages [19] -->
F vs. ∆X (Y = 100)

<!-- b000477 | prose | pages [19] -->
500

<!-- b000478 | prose | pages [19] -->
400

<!-- b000479 | prose | pages [19] -->
300

<!-- b000480 | prose | pages [19] -->
Failed rafts

<!-- b000481 | prose | pages [19] -->
200

<!-- b000482 | prose | pages [19] -->
100

<!-- b000483 | prose | pages [19] -->
0

<!-- b000484 | prose | pages [19] -->
100

<!-- b000485 | prose | pages [19] -->
4 0 2 6 8 10 12 Rafts added each day

<!-- b000486 | caption | pages [19] -->
Figure 9: Unplaceable Rafts vs. ∆X

<!-- b000487 | prose | pages [19] -->
µ vs. ∆X (Y = 100)

<!-- b000488 | prose | pages [19] -->
100

<!-- b000489 | prose | pages [19] -->
80

<!-- b000490 | prose | pages [19] -->
Campsite Utilization (%)

<!-- b000491 | prose | pages [19] -->
60

<!-- b000492 | prose | pages [19] -->
40

<!-- b000493 | prose | pages [19] -->
20

<!-- b000494 | prose | pages [19] -->
0

<!-- b000495 | prose | pages [19] -->
4 0 2 6 8 10 12 Rafts added each day

<!-- b000496 | caption | pages [19] -->
Figure 10: Utilization vs. ∆X

<!-- b000497 | prose | pages [19] -->
for ∆X ≤6 all of the boats can successfully be placed in campsites over the course of the

<!-- b000498 | prose | pages [19] -->
simulation. At ∆X = 7 there is a small number of boats, less than 1%, that cannot be placed

<!-- b000499 | prose | pages [19] -->
in the simulation. Therefore, the carrying capacity of the river when using the simple greedy

<!-- b000500 | furniture | pages [20] -->
Team # 15171

<!-- b000501 | furniture | pages [20] -->
Page 18

<!-- b000502 | prose | pages [20] -->
F vs. Y (∆X = 7)

<!-- b000503 | prose | pages [20] -->
700

<!-- b000504 | prose | pages [20] -->
600

<!-- b000505 | prose | pages [20] -->
500

<!-- b000506 | prose | pages [20] -->
400

<!-- b000507 | prose | pages [20] -->
Failed Rafts

<!-- b000508 | prose | pages [20] -->
300

<!-- b000509 | prose | pages [20] -->
200

<!-- b000510 | prose | pages [20] -->
100

<!-- b000511 | prose | pages [20] -->
0

<!-- b000512 | prose | pages [20] -->
100

<!-- b000513 | prose | pages [20] -->
0 50 100 150 200 Campsites

<!-- b000514 | caption | pages [20] -->
Figure 11: Failed Boats vs. Y

<!-- b000515 | prose | pages [20] -->
µ vs. Y (∆X = 7)

<!-- b000516 | prose | pages [20] -->
100

<!-- b000517 | prose | pages [20] -->
90

<!-- b000518 | prose | pages [20] -->
80

<!-- b000519 | prose | pages [20] -->
Utilization (%)

<!-- b000520 | prose | pages [20] -->
70

<!-- b000521 | prose | pages [20] -->
60

<!-- b000522 | prose | pages [20] -->
50

<!-- b000523 | prose | pages [20] -->
40

<!-- b000524 | prose | pages [20] -->
30

<!-- b000525 | prose | pages [20] -->
0 50 100 150 200 Campsites

<!-- b000526 | caption | pages [20] -->
Figure 12: Utilization vs. Y

<!-- b000527 | prose | pages [20] -->
heuristic for boat placement is approximately ∆X = 7.

<!-- b000528 | prose | pages [20] -->
As seen in Figure 10, campsite utilization is nearly constant for ∆X ≥9. In addition, camp

<!-- b000529 | prose | pages [20] -->
utilization at the carrying capacity is approximately 80%.

<!-- b000530 | furniture | pages [21] -->
Team # 15171

<!-- b000531 | furniture | pages [21] -->
Page 19

<!-- b000532 | prose | pages [21] -->
n of Failed Boats vs. ∆X (Y = 100)

<!-- b000533 | prose | pages [21] -->
16

<!-- b000534 | prose | pages [21] -->
15

<!-- b000535 | prose | pages [21] -->
14

<!-- b000536 | prose | pages [21] -->
13

<!-- b000537 | prose | pages [21] -->
n of Failed Boats

<!-- b000538 | prose | pages [21] -->
12

<!-- b000539 | prose | pages [21] -->
11

<!-- b000540 | prose | pages [21] -->
10

<!-- b000541 | prose | pages [21] -->
9

<!-- b000542 | prose | pages [21] -->
8

<!-- b000543 | prose | pages [21] -->
7

<!-- b000544 | prose | pages [21] -->
5 0 10 15 20 Rafts Added Each Day

<!-- b000545 | caption | pages [21] -->
Figure 13: Average n for Failed Boats vs. ∆X

<!-- b000546 | prose | pages [21] -->
v of Failed Boats vs. ∆X (Y = 100)

<!-- b000547 | prose | pages [21] -->
9

<!-- b000548 | prose | pages [21] -->
8

<!-- b000549 | prose | pages [21] -->
7

<!-- b000550 | prose | pages [21] -->
v of Failed Boats

<!-- b000551 | prose | pages [21] -->
6

<!-- b000552 | prose | pages [21] -->
5

<!-- b000553 | prose | pages [21] -->
4

<!-- b000554 | prose | pages [21] -->
3

<!-- b000555 | prose | pages [21] -->
5 0 10 15 20 Rafts Added Each Day

<!-- b000556 | caption | pages [21] -->
Figure 14: Average v for Failed Boats vs. ∆X

<!-- b000557 | caption | pages [21] -->
Figure 15 shows the total number of boats that could be successfully placed using the

<!-- b000558 | prose | pages [21] -->
greedy algorithm described in section 5.3.1. At the carrying capacity of the river ∆X = 7, the

<!-- b000559 | prose | pages [21] -->
total number of boats that could be serviced by the river was approximate 1260. This is similar

<!-- b000560 | furniture | pages [22] -->
Team # 15171

<!-- b000561 | furniture | pages [22] -->
Page 20

<!-- b000562 | prose | pages [22] -->
T vs. ∆X (Y = 100)

<!-- b000563 | prose | pages [22] -->
1600

<!-- b000564 | prose | pages [22] -->
1400

<!-- b000565 | prose | pages [22] -->
1200

<!-- b000566 | prose | pages [22] -->
Total rafts accommodated

<!-- b000567 | prose | pages [22] -->
1000

<!-- b000568 | prose | pages [22] -->
800

<!-- b000569 | prose | pages [22] -->
600

<!-- b000570 | prose | pages [22] -->
400

<!-- b000571 | prose | pages [22] -->
200

<!-- b000572 | prose | pages [22] -->
0

<!-- b000573 | prose | pages [22] -->
4 0 2 6 8 10 12 Rafts added each day

<!-- b000574 | caption | pages [22] -->
Figure 15: Total Placed Boats T vs. ∆X

<!-- b000575 | prose | pages [22] -->
to the carrying capacity estimates of the other algorithms. At this carrying capacity, there is a

<!-- b000576 | prose | pages [22] -->
diminished need for scheduling, because only a small number (about 1% of boats) fail to ﬁnd

<!-- b000577 | prose | pages [22] -->
campsites. However, if the algorithm is overdriven by intentionally using ∆X ≥7 the total

<!-- b000578 | prose | pages [22] -->
number of boats serviced can actually be increased. The algorithm then removes any boats that

<!-- b000579 | prose | pages [22] -->
do not ﬁt into the schedule, and between 1360 and 1400 boats can be serviced during a season.

<!-- b000580 | prose | pages [22] -->
This approaches 100% utilization.

<!-- b000581 | prose | pages [22] -->
It is worth noting that placement failure is not strongly correlated with the speed of the boat

<!-- b000582 | prose | pages [22] -->
(v) for ∆X well above the carrying capacity of the river (∆X > 9). The failure rate of the

<!-- b000583 | prose | pages [22] -->
boats is also not correlated with the number of nights that they spend on the river. This can

<!-- b000584 | prose | pages [22] -->
be seen in Figure 13. Therefore, it should be safe to overdrive the algorithm and place more

<!-- b000585 | prose | pages [22] -->
boats on the river, assuming the demand for various boat speeds and trip length is uniform as

<!-- b000586 | prose | pages [22] -->
described in section 4.4.2. However, campsite utilization approaches 100% when ∆X is this

<!-- b000587 | prose | pages [22] -->
large as seen in Figure 10. Therefore, 1400 approaches the absolute upper limit for the carrying

<!-- b000588 | prose | pages [22] -->
capacity of the river. 1260 at ∆X = 7 may be a more comfortable and realistic number.

<!-- b000589 | prose | pages [22] -->
However, as seen in Figure 14, the average speed of failed boats is approximately 7.5 when

<!-- b000590 | prose | pages [22] -->
∆X = 7, right at the carrying capacity. This is not surprising, because the greedy heuristic does

<!-- b000591 | prose | pages [22] -->
give precedence to the slower (4 mph) boats since they have less ﬂexibility with scheduling.

<!-- b000592 | prose | pages [22] -->
Still, the total number of boats which cannot ﬁnd a campsite when ∆X = 7 is relatively small,

<!-- b000593 | prose | pages [22] -->
and the tendency for fast boats to fail should not become an issue.

<!-- b000594 | furniture | pages [23] -->
Team # 15171

<!-- b000595 | furniture | pages [23] -->
Page 21

<!-- b000596 | prose | pages [23] -->
5.4

<!-- b000597 | heading | pages [23] -->
Probability Model

<!-- b000598 | prose | pages [23] -->
The driving question behind this model is: how many boats, of what types, can we send down

<!-- b000599 | prose | pages [23] -->
the Big Long River while keeping the probability that a boat will have to travel more than some

<!-- b000600 | prose | pages [23] -->
cutoff distance to ﬁnd an open campsite within an acceptable range? We make a number of

<!-- b000601 | prose | pages [23] -->
assumptions, many of which are relaxations of the assumptions of previous models:

<!-- b000602 | prose | pages [23] -->
• The actual distance a boat travels each day is variable, but the number of nighttime stops

<!-- b000603 | prose | pages [23] -->
a boat makes is predetermined and non-variable.

<!-- b000604 | prose | pages [23] -->
• The desired daily distance of travel for each boat follows outcomes of an exponential

<!-- b000605 | prose | pages [23] -->
random variable of constant rate, with each outcome independent of all others. Thus,

<!-- b000606 | prose | pages [23] -->
these locations can be modeled as arrivals of a Homogeneous Poisson Process.

<!-- b000607 | prose | pages [23] -->
• The number of boats desiring a certain trip duration sent out each day remains relatively

<!-- b000608 | prose | pages [23] -->
constant; that is, we will not have a single day in which we send only row boats desiring

<!-- b000609 | prose | pages [23] -->
twelve-day trips followed by a single day of sending only motor boats desiring six-day

<!-- b000610 | prose | pages [23] -->
trips. There is very little variation in this respect from one day to the next.

<!-- b000611 | prose | pages [23] -->
• Campsites are placed with equal distance between them.

<!-- b000612 | prose | pages [23] -->
Allowing for variable daily distances is a major strength of this model, since a number of

<!-- b000613 | prose | pages [23] -->
circumstances, from boat problems to medical issues to simple changes of mood, can affect

<!-- b000614 | prose | pages [23] -->
how far an individual boat might travel in a given day. An exponential random variable, and

<!-- b000615 | prose | pages [23] -->
thus a Poisson Process, seems a logical way to model the distance a boat desires to travel each

<!-- b000616 | prose | pages [23] -->
day because each boat will want to average some speciﬁc distance each day (corresponding to

<!-- b000617 | prose | pages [23] -->
the rate of the exponential distribution), but a certain degree of variation can be expected. Note

<!-- b000618 | prose | pages [23] -->
that the location at which a boat desires to stop need not be at a campsite; this maintains the

<!-- b000619 | prose | pages [23] -->
continuous nature of the exponential random variable. It is logical that a group might wish it

<!-- b000620 | prose | pages [23] -->
could stop at a place where there is no campground and yet have to continue until they ﬁnd the

<!-- b000621 | prose | pages [23] -->
ﬁrst open campground.

<!-- b000622 | prose | pages [23] -->
A major mathematical advantage of using a Homogeneous Poisson Process is that if we

<!-- b000623 | prose | pages [23] -->
know the number of arrivals of the process over a given span, the arrivals take the distribution

<!-- b000624 | prose | pages [23] -->
of a uniform random variable[2]. In this model, the number of arrivals for the process is the

<!-- b000625 | prose | pages [23] -->
number of nighttime stops a boat wishes to make, and the given span is the length of the river.

<!-- b000626 | prose | pages [23] -->
Thus, we can model the desired stops of a boat that hopes to spend n nights on the river as n

<!-- b000627 | prose | pages [23] -->
draws from a uniform distribution.

<!-- b000628 | prose | pages [23] -->
We will make two claims to argue that the distribution of desired stop locations for all boats

<!-- b000629 | prose | pages [23] -->
on the river on a single given night also follows N draws from a uniform distribution, where

<!-- b000630 | furniture | pages [24] -->
Team # 15171

<!-- b000631 | furniture | pages [24] -->
Page 22

<!-- b000632 | prose | pages [24] -->
N is the total number of boats on the river. First, we take into account the third assumption

<!-- b000633 | prose | pages [24] -->
above, that the daily send off of each trip duration remains relatively constant. Let us consider

<!-- b000634 | prose | pages [24] -->
all boats that wish to have a twelve day trip, and ignore all others. If we send all of these boats

<!-- b000635 | prose | pages [24] -->
out at once, their distribution on a single night will certainly not be uniform; rather, they will

<!-- b000636 | prose | pages [24] -->
follow the distribution of the minimum of a uniform distribution, and so they will all be grouped

<!-- b000637 | prose | pages [24] -->
toward the beginning of the river. If instead we send one out each day, then by the twelfth night

<!-- b000638 | prose | pages [24] -->
their distribution will indeed be uniform. We apply this logic to each subset of boats desiring

<!-- b000639 | prose | pages [24] -->
a trip length of n days, with n ranging from 6 to 18, and note that given the assumption of

<!-- b000640 | prose | pages [24] -->
consistent send offs, the distribution of all of these boats on a single night will be uniform.

<!-- b000641 | prose | pages [24] -->
Superimposing all of these uniform distributions gives another uniform distribution; thus, with

<!-- b000642 | prose | pages [24] -->
this assumption, the distribution of desired stop locations on a given night for all boats follows

<!-- b000643 | prose | pages [24] -->
a uniform distribution.

<!-- b000644 | prose | pages [24] -->
We are now in a position to answer the question posed at the beginning of this section.

<!-- b000645 | prose | pages [24] -->
Consider Figure 16:

<!-- b000646 | caption | pages [24] -->
Figure 16: Schematic Diagram of Boat Placement

<!-- b000647 | prose | pages [24] -->
The ‘x’ on Figure 16 is the spot where the boat in question wishes to stop. w is the distance

<!-- b000648 | prose | pages [24] -->
to the closest campsite, w + D is the distance to the next closest campsite, w + 2D is the

<!-- b000649 | prose | pages [24] -->
distance to the third closest campsite, and so on. Let us for now assume that all boats on the

<!-- b000650 | prose | pages [24] -->
river are row boats; this assumption will be relaxed later. Let us now imagine that the day is

<!-- b000651 | prose | pages [24] -->
closing and boats are all reaching the locations they desired to go, just as our boat has reached

<!-- b000652 | prose | pages [24] -->
its ‘x’ in Figure 16. As the boats jockey for campgrounds, we want to know the probability that

<!-- b000653 | prose | pages [24] -->
our boat will have to travel some distance δ before ﬁnding an open campground. If we assume

<!-- b000654 | prose | pages [24] -->
that any boat that is in front of ours will reach an open campground ﬁrst (valid since, for now,

<!-- b000655 | prose | pages [24] -->
we assume all boats have the same speed), then the probability becomes the chance that there

<!-- b000656 | prose | pages [24] -->
are either two boats in the span w and none in the adjacent span D, or there is one boat in w

<!-- b000657 | prose | pages [24] -->
and another in D (from this probability we can later compute the probability that our boat will

<!-- b000658 | prose | pages [24] -->
have to travel a distance greater than δ to ﬁnd an open campsite). The probabilities of these

<!-- b000659 | prose | pages [24] -->
two events can be computed as binomials:

<!-- b000660 | furniture | pages [25] -->
Team # 15171

<!-- b000661 | furniture | pages [25] -->
Page 23

<!-- b000662 | prose | pages [25] -->
N −1

<!-- b000663 | prose | pages [25] -->


<!-- b000664 | prose | pages [25] -->
(w)2(1 −w)(N−1)−2

<!-- b000665 | prose | pages [25] -->
P(A) =

<!-- b000666 | prose | pages [25] -->
2

<!-- b000667 | prose | pages [25] -->
N −1

<!-- b000668 | prose | pages [25] -->


<!-- b000669 | prose | pages [25] -->
(w + D)2(1 −(w + D))(N−1)−2∗

<!-- b000670 | prose | pages [25] -->
P(B) =

<!-- b000671 | prose | pages [25] -->
2

<!-- b000672 | prose | pages [25] -->
2

<!-- b000673 | prose | pages [25] -->


<!-- b000674 | prose | pages [25] -->
(w)(1 −w)

<!-- b000675 | prose | pages [25] -->
1

<!-- b000676 | prose | pages [25] -->
where N is the number of boats on the river at a given time, A is the event that there are two

<!-- b000677 | prose | pages [25] -->
threatening boats in the span w between the boat and the ﬁrst campsite, and B is the probability

<!-- b000678 | prose | pages [25] -->
that there is one boat in the span w and another in the adjacent span D. These equations again

<!-- b000679 | prose | pages [25] -->
take advantage of the scale of w as a fraction of total river length; this allows an effortless

<!-- b000680 | prose | pages [25] -->
conversion between distance and the probability of landing in a given range. Summing these

<!-- b000681 | prose | pages [25] -->
two probabilities gives the total desired probability, that the boat will have to travel some given

<!-- b000682 | prose | pages [25] -->
distance δ to ﬁnd an open campground. The ﬁrst equation is fairly straightforward; it is just

<!-- b000683 | prose | pages [25] -->
P(K = 2) where K is some random variable and K ∼Binomial(N −1, 2). The second

<!-- b000684 | prose | pages [25] -->
equation is more involved; the ﬁrst term, spanning from the ﬁrst combination to just before

<!-- b000685 | prose | pages [25] -->
the second, gives the probability that there are two boats in the span that includes w and D.

<!-- b000686 | prose | pages [25] -->
The second term, spanning from the second combination to the end of the expression, is the

<!-- b000687 | prose | pages [25] -->
probability that exactly one of these boats lies in w. Given this explanation, it is apparent how

<!-- b000688 | prose | pages [25] -->
one might write a similar expression for when the span between the boat and δ includes three or

<!-- b000689 | prose | pages [25] -->
more campsites. The closed form of the general expression is quite cumbersome as it includes

<!-- b000690 | prose | pages [25] -->
a term for every possible distribution of boats between campsites that could possibly block our

<!-- b000691 | prose | pages [25] -->
boat from reaching an open site in a distance less than δ. However, one can develop the full

<!-- b000692 | prose | pages [25] -->
form for any given probability using the guidelines above.

<!-- b000693 | prose | pages [25] -->
We have now laid enough groundwork to relax one last assumption and allow for both row

<!-- b000694 | prose | pages [25] -->
boats and motor boats. Let us again consider the desired stop locations of all boats on the river

<!-- b000695 | prose | pages [25] -->
on a given night. As noted above, the placement of these stop locations follows a uniform

<!-- b000696 | prose | pages [25] -->
distribution. We again want to calculate the probability that a given boat will have to travel a

<!-- b000697 | prose | pages [25] -->
distance δ to ﬁnd an open campsite. Unlike the previous case, if our boat is a row boat (traveling

<!-- b000698 | prose | pages [25] -->
at approximately 4 miles per hour), then there is the chance that it will be overtaken by a motor

<!-- b000699 | prose | pages [25] -->
boat that is further behind it and thus be cheated out of a campsite. Likewise, if our boat is

<!-- b000700 | prose | pages [25] -->
a motorboat (traveling at approximately 8 miles per hour), it has the chance to overtake row

<!-- b000701 | prose | pages [25] -->
boats to reach an open campsite even though the row boats initially begin their search further

<!-- b000702 | prose | pages [25] -->
downstream. As before, we can express the probability of having to travel a distance δ as the

<!-- b000703 | prose | pages [25] -->
probability that there are other boats positioned in certain conﬁgurations so that they can reach

<!-- b000704 | prose | pages [25] -->
the campsites between our boat and δ distance past our boat before our boat can. To generate

<!-- b000705 | furniture | pages [26] -->
Team # 15171

<!-- b000706 | furniture | pages [26] -->
Page 24

<!-- b000707 | prose | pages [26] -->
this probability, we must take into account both the type of our boat and the probability that

<!-- b000708 | prose | pages [26] -->
another given boat on the river is a motorboat.

<!-- b000709 | prose | pages [26] -->
Let us ﬁrst take the case in which our boat is a row boat. Certainly, any type of boat that is

<!-- b000710 | prose | pages [26] -->
in front of us will be able to reach an open campsite before we can. However, we now have to

<!-- b000711 | prose | pages [26] -->
take into account the additional probability that there is a motor boat sufﬁciently close behind

<!-- b000712 | prose | pages [26] -->
us to overtake us and get to an open site before we can. Consider again the instance in Figure

<!-- b000713 | prose | pages [26] -->
16; the possibility of having motor boats essentially expands the range in which we have to

<!-- b000714 | prose | pages [26] -->
be concerned about other boats to an additional distance ∆behind our boat, where ∆is the

<!-- b000715 | prose | pages [26] -->
distance between our boat and the campsite in question (the motorboats can travel twice as

<!-- b000716 | prose | pages [26] -->
fast as the row boats, so they can cover a distance of 2∆in the time our row boat can travel a

<!-- b000717 | prose | pages [26] -->
distance of ∆). Thus, the probabilities become

<!-- b000718 | prose | pages [26] -->
N −1

<!-- b000719 | prose | pages [26] -->


<!-- b000720 | prose | pages [26] -->
P(A′) =

<!-- b000721 | prose | pages [26] -->
(w + pfw)2(1 −(w + pfw))(N−1)−2

<!-- b000722 | prose | pages [26] -->
2

<!-- b000723 | prose | pages [26] -->
N −1

<!-- b000724 | prose | pages [26] -->


<!-- b000725 | prose | pages [26] -->
P(B′) =

<!-- b000726 | prose | pages [26] -->
(w + D + pfD)2(1 −(w + D + pfD))(N−1)−2∗

<!-- b000727 | prose | pages [26] -->
2

<!-- b000728 | prose | pages [26] -->
2

<!-- b000729 | prose | pages [26] -->


<!-- b000730 | prose | pages [26] -->
(w + pfw)(1 −(w + pfw))

<!-- b000731 | prose | pages [26] -->
1

<!-- b000732 | prose | pages [26] -->
Here, pf is the probability that a boat on the river is a motor boat, and the probabilities in the

<!-- b000733 | prose | pages [26] -->
binomial expressions take into account the chance that there is a motor boat sufﬁciently close

<!-- b000734 | prose | pages [26] -->
behind to overtake our boat. A′ is the event that there are two threatening boats before the ﬁrst

<!-- b000735 | prose | pages [26] -->
campsite and B′ is the event that there is one threatening boat before the ﬁrst campsite and an

<!-- b000736 | prose | pages [26] -->
additional boat between the ﬁrst and second campsites.

<!-- b000737 | prose | pages [26] -->
The case in which our boat is a motor boat is similar. Now, rather than concerning ourselves

<!-- b000738 | prose | pages [26] -->
with boats that are behind us, we want to know if there are any row boats sufﬁciently close in

<!-- b000739 | prose | pages [26] -->
front of us for us to overtake. Noting that we will overtake any row boat that is further than

<!-- b000740 | prose | pages [26] -->
half of our own distance from the site we desire, we construct the following probabilities:

<!-- b000741 | prose | pages [26] -->
N −1

<!-- b000742 | prose | pages [26] -->
w −(1 −pf)w

<!-- b000743 | prose | pages [26] -->


<!-- b000744 | prose | pages [26] -->
P(A′′) =

<!-- b000745 | prose | pages [26] -->
2

<!-- b000746 | prose | pages [26] -->
2

<!-- b000747 | prose | pages [26] -->
N −1

<!-- b000748 | prose | pages [26] -->
(N−1)−2

<!-- b000749 | prose | pages [26] -->
w −(1 −pf)w

<!-- b000750 | prose | pages [26] -->
2

<!-- b000751 | prose | pages [26] -->
 1 −

<!-- b000752 | prose | pages [26] -->
2

<!-- b000753 | prose | pages [26] -->
w + D −(1 −pf)(w + D)

<!-- b000754 | prose | pages [26] -->


<!-- b000755 | prose | pages [26] -->
P(B′′) =

<!-- b000756 | prose | pages [26] -->
2

<!-- b000757 | prose | pages [26] -->
2

<!-- b000758 | prose | pages [26] -->
∗

<!-- b000759 | prose | pages [26] -->
2

<!-- b000760 | prose | pages [26] -->
(N−1)−2

<!-- b000761 | prose | pages [26] -->
w + D −(1 −pf)(w + D)

<!-- b000762 | prose | pages [26] -->


<!-- b000763 | prose | pages [26] -->
 1 −

<!-- b000764 | prose | pages [26] -->
w −(1 −pf)w

<!-- b000765 | prose | pages [26] -->
2

<!-- b000766 | prose | pages [26] -->


<!-- b000767 | prose | pages [26] -->


<!-- b000768 | prose | pages [26] -->
∗

<!-- b000769 | prose | pages [26] -->
2 2

<!-- b000770 | prose | pages [26] -->
w −(1 −pf)w

<!-- b000771 | prose | pages [26] -->


<!-- b000772 | prose | pages [26] -->


<!-- b000773 | prose | pages [26] -->
1 −

<!-- b000774 | prose | pages [26] -->
1

<!-- b000775 | prose | pages [26] -->
2

<!-- b000776 | prose | pages [26] -->
2

<!-- b000777 | furniture | pages [27] -->
Team # 15171

<!-- b000778 | furniture | pages [27] -->
Page 25

<!-- b000779 | prose | pages [27] -->
Here, A′′ is the event that there are two threatening boats in front of us, such as one motor

<!-- b000780 | prose | pages [27] -->
boat and one row boat that is further than half our distance to the ﬁrst campsite. B′′ is the

<!-- b000781 | prose | pages [27] -->
event that there is one threatening boat between us and the closest campsite and one between

<!-- b000782 | prose | pages [27] -->
the closest and the next closest campsite.

<!-- b000783 | prose | pages [27] -->
Figures 17, 19, and 18 (Appendix) show the dependence of these probabilities on the num-

<!-- b000784 | prose | pages [27] -->
ber of boats on the water; they show the probability that a fast boat will have to travel 14 miles

<!-- b000785 | prose | pages [27] -->
(just under two hours) to ﬁnd an open campsite. Figures 21, 20, and 22 (Appendix) show the

<!-- b000786 | prose | pages [27] -->
corresponding results for a slow boat. Figures 17 and 20 show the results for a river with 29

<!-- b000787 | prose | pages [27] -->
campsites, Figures 18 and 21 show the results for a river with 59 campsites, and Figures 19

<!-- b000788 | prose | pages [27] -->
and 22 show the results for a river with 99 campsites. Note, in agreement with the analysis

<!-- b000789 | prose | pages [27] -->
in the simplest model, there is a great deal of variation in the model results corresponding to

<!-- b000790 | prose | pages [27] -->
campsite placement. In the results for both types of boats, the number of boats that can feasibly

<!-- b000791 | prose | pages [27] -->
be sent down the river greatly increases as the distance between campsites decreases (and thus

<!-- b000792 | prose | pages [27] -->
the total number of campsites increases). In addition, we see that it is more favorable for row

<!-- b000793 | prose | pages [27] -->
boats to have most of their competition for campsites coming from other rowboats, while it is

<!-- b000794 | prose | pages [27] -->
more favorable for motor boats to have most of their competition coming from motor boats.

<!-- b000795 | prose | pages [27] -->
To conclude this section, we will consider what seems to be the most likely case for the

<!-- b000796 | prose | pages [27] -->
Big Long River and make a recommendation for how to best schedule departures from First

<!-- b000797 | prose | pages [27] -->
Launch, assuming that boats will not follow a predetermined itinerary. If the Big Long River

<!-- b000798 | prose | pages [27] -->
indeed has 99 campsites, which seems feasible along its 225 mile length, up to 77 boats can be

<!-- b000799 | prose | pages [27] -->
allowed on the river at a time if there are equal numbers of row boats and motor boats, and this

<!-- b000800 | prose | pages [27] -->
will ensure that an average of only 1% of customers have to travel 14 miles to ﬁnd a campsite.

<!-- b000801 | prose | pages [27] -->
At the beginning of the season, an constant mix of boat types and trip lengths should be sent out

<!-- b000802 | prose | pages [27] -->
each day until the river reaches its capacity of 77 boats. Once it reaches capacity, the boats that

<!-- b000803 | prose | pages [27] -->
ﬁnish should be monitored so that a new boat of similar characteristics can be launched soon

<!-- b000804 | prose | pages [27] -->
thereafter, keeping the relative proportions of the 77 boats as constant as possible. Assuming

<!-- b000805 | prose | pages [27] -->
that the average trip length is twelve days, we can expect to launch an average of 77 boats

<!-- b000806 | prose | pages [27] -->
every twelve days. Over the course of the 180-day season, this gives a 1,155 boat capacity

<!-- b000807 | prose | pages [27] -->
per season for the Big Long River.

<!-- b000808 | prose | pages [27] -->
6

<!-- b000809 | heading | pages [27] -->
Conclusion

<!-- b000810 | prose | pages [27] -->
To conclude, we expand on the joint results of all three models, closely examine their strengths

<!-- b000811 | prose | pages [27] -->
and weaknesses, and propose extensions.

<!-- b000812 | furniture | pages [28] -->
Team # 15171

<!-- b000813 | furniture | pages [28] -->
Page 26

<!-- b000814 | prose | pages [28] -->
6.1

<!-- b000815 | heading | pages [28] -->
Overall Results

<!-- b000816 | prose | pages [28] -->
Perhaps the most striking and valuable result is that all three models propose a maximum

<!-- b000817 | prose | pages [28] -->
seasonal throughput for the Big Long River as some value between 1150 and 1250 boats, with

<!-- b000818 | prose | pages [28] -->
up to 1400 allowed if the itinerary model is used and there is a high tolerance for daytime

<!-- b000819 | prose | pages [28] -->
crowding on the river. Despite this common conclusion, the differing motivations behind the

<!-- b000820 | prose | pages [28] -->
models allow each to provide unique insight into the behavior of boats on the river. The agent-

<!-- b000821 | prose | pages [28] -->
based model shows the importance of starting boats early in the day and restricting the duration

<!-- b000822 | prose | pages [28] -->
of trips by slower boats to twelve or more days. The itinerary-based model suggests that

<!-- b000823 | prose | pages [28] -->
placement preference should go to the slower boats, which are more restricted in their range

<!-- b000824 | prose | pages [28] -->
of potential campsites each night. The probabilistic model advocates for keeping the relative

<!-- b000825 | prose | pages [28] -->
proportions of each type of boat constant over the course of the season and adjusting this

<!-- b000826 | prose | pages [28] -->
proportion depending on whether the rafting management wishes to favor oar or motor boats.

<!-- b000827 | prose | pages [28] -->
Taken together, these results provide a good picture as to how the river should be managed. A

<!-- b000828 | prose | pages [28] -->
manager who is conﬁdent that he or she can trust boats to travel to predetermined campsites

<!-- b000829 | prose | pages [28] -->
and is comfortable with turning down some potential customers should pick the itinerary-based

<!-- b000830 | prose | pages [28] -->
approach, thus preventing any one boat from having to travel in potentially unsafe conditions.

<!-- b000831 | prose | pages [28] -->
A manager who believes that the boaters cannot be trusted to travel to a pre-speciﬁed campsite

<!-- b000832 | prose | pages [28] -->
each evening should rely on the agent-based and probabilistic models, sending out a wave

<!-- b000833 | prose | pages [28] -->
of boats each morning and keeping the relative proportion of each type of boat on the river

<!-- b000834 | prose | pages [28] -->
constant, knowing that each boat runs some small chance of having to travel an exceedingly

<!-- b000835 | prose | pages [28] -->
long distance to ﬁnd an open campsite. Regardless of the approach chosen, the manager can

<!-- b000836 | prose | pages [28] -->
be conﬁdent that their choice will not negatively affect the total number of people they serve in

<!-- b000837 | prose | pages [28] -->
a season.

<!-- b000838 | prose | pages [28] -->
6.2

<!-- b000839 | heading | pages [28] -->
Strengths, Weaknesses, and Extensions

<!-- b000840 | prose | pages [28] -->
As mentioned above, these models taken together have the advantage of catering to a degree

<!-- b000841 | prose | pages [28] -->
of assumptions a river manager is willing to make regarding trustworthiness of the boaters

<!-- b000842 | prose | pages [28] -->
and danger of having a raft spend a long time searching for an open campsite. They also

<!-- b000843 | prose | pages [28] -->
all reach similar results regarding the river’s seasonal capacity, making this ﬁgure particularly

<!-- b000844 | prose | pages [28] -->
trustworthy. However, all three models rely on the perhaps restrictive assumption that the

<!-- b000845 | prose | pages [28] -->
campsites along the river are perfectly evenly spaced. A logical and straightforward extension

<!-- b000846 | prose | pages [28] -->
to this set of models would be to relax this assumption by, in the case of the agent-based and

<!-- b000847 | prose | pages [28] -->
itinerary models, generating the locations of campsites from a continuous uniform distribution,

<!-- b000848 | prose | pages [28] -->
and in the case of the probabilistic model, analyzing the probability of having an excessive

<!-- b000849 | prose | pages [28] -->
number of boats between a randomly placed boat and a randomly placed campsite, rather

<!-- b000850 | furniture | pages [29] -->
Team # 15171

<!-- b000851 | furniture | pages [29] -->
Page 27

<!-- b000852 | prose | pages [29] -->
than a ﬁxed campsite. Another extension could involve adding dependence on weather to the

<!-- b000853 | prose | pages [29] -->
progression of boats down the river. The probabilistic model does not account for this because

<!-- b000854 | prose | pages [29] -->
it assumes that all variations in the boats’ desired stopping locations are due to independent

<!-- b000855 | prose | pages [29] -->
factors, but storms would likely affect all or a signiﬁcant subset of the boats at once. A ﬁnal

<!-- b000856 | prose | pages [29] -->
potential extension not addressed by these models would be to study how the demand from

<!-- b000857 | prose | pages [29] -->
various types of boats and trip lengths changes over the course of a season and then work this

<!-- b000858 | prose | pages [29] -->
variation into the models to better reﬂect the true client`ele of the Big Long River.

<!-- b000859 | furniture | pages [30] -->
Team # 15171

<!-- b000860 | prose | pages [30] -->
7

<!-- b000861 | heading | pages [30] -->
Appendix

<!-- b000862 | prose | pages [30] -->
7.1

<!-- b000863 | heading | pages [30] -->
Probabilistic Model

<!-- b000864 | furniture | pages [30] -->
Page 28

<!-- b000865 | prose | pages [30] -->
The following ﬁgures are visualizations of results from the probabilistic model:

<!-- b000866 | prose | pages [30] -->
Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.25

<!-- b000867 | prose | pages [30] -->
P(fast) = .1 P(fast) = .25 P(fast) = .5 P(fast) = .75 P(fast) = .9

<!-- b000868 | prose | pages [30] -->
0.2

<!-- b000869 | prose | pages [30] -->
1% cutoff

<!-- b000870 | prose | pages [30] -->
Probability of having to travel an additional 14 miles

<!-- b000871 | prose | pages [30] -->
Other Parameters:

<!-- b000872 | prose | pages [30] -->
Location on river = 28.125 miles (1/8 of river length)

<!-- b000873 | prose | pages [30] -->
0.15

<!-- b000874 | prose | pages [30] -->
Distance between sites = 7.5 miles (1/30 of river length)

<!-- b000875 | prose | pages [30] -->
Total # of Campsites = 29

<!-- b000876 | prose | pages [30] -->
0.1

<!-- b000877 | prose | pages [30] -->
0.05

<!-- b000878 | prose | pages [30] -->
0

<!-- b000879 | furniture | pages [30] -->


<!-- b000880 | prose | pages [30] -->
0 10 20 30 40

<!-- b000881 | furniture | pages [30] -->


<!-- b000882 | prose | pages [30] -->
50 60 70 80 90 100

<!-- b000883 | prose | pages [30] -->
Number of Boats

<!-- b000884 | caption | pages [30] -->
Figure 17: Probability a Fast Boat must travel 14 miles - Far Campsites

<!-- b000885 | furniture | pages [31] -->
Team # 15171

<!-- b000886 | furniture | pages [31] -->
Page 29

<!-- b000887 | prose | pages [31] -->
Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.2

<!-- b000888 | prose | pages [31] -->
P(fast) = .1 P(fast) = .25

<!-- b000889 | prose | pages [31] -->
0.18

<!-- b000890 | prose | pages [31] -->
P(fast) = .5 P(fast) = .75 P(fast) = .9

<!-- b000891 | prose | pages [31] -->
0.16

<!-- b000892 | prose | pages [31] -->
1% cutoff

<!-- b000893 | prose | pages [31] -->
Probability of having to travel an additional 14 miles

<!-- b000894 | prose | pages [31] -->
Other Parameters:

<!-- b000895 | prose | pages [31] -->
0.14

<!-- b000896 | prose | pages [31] -->
Location on river = 28.125 miles (1/8 of river length)

<!-- b000897 | prose | pages [31] -->
Distance between sites = 3.75

<!-- b000898 | prose | pages [31] -->
0.12

<!-- b000899 | prose | pages [31] -->
miles (1/60 of river length)

<!-- b000900 | prose | pages [31] -->
Total # of Campsites = 59

<!-- b000901 | prose | pages [31] -->
0.1

<!-- b000902 | prose | pages [31] -->
0.08

<!-- b000903 | prose | pages [31] -->
0.06

<!-- b000904 | prose | pages [31] -->
0.04

<!-- b000905 | prose | pages [31] -->
0.02

<!-- b000906 | prose | pages [31] -->
0

<!-- b000907 | furniture | pages [31] -->


<!-- b000908 | prose | pages [31] -->
0 10 20 30 40

<!-- b000909 | furniture | pages [31] -->


<!-- b000910 | prose | pages [31] -->
50 60 70 80 90 100

<!-- b000911 | prose | pages [31] -->
Number of Boats

<!-- b000912 | caption | pages [31] -->
Figure 18: Probability a Fast Boat must travel 14 miles - Medium-Distance Campsites

<!-- b000913 | furniture | pages [32] -->
Team # 15171

<!-- b000914 | furniture | pages [32] -->
Page 30

<!-- b000915 | prose | pages [32] -->
Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.06

<!-- b000916 | prose | pages [32] -->
P(fast) = .1 P(fast) = .25 P(fast) = .5 P(fast) = .75

<!-- b000917 | prose | pages [32] -->
0.05

<!-- b000918 | prose | pages [32] -->
P(fast) = .9 1% cutoff

<!-- b000919 | prose | pages [32] -->
Probability of having to travel an additional 14 miles

<!-- b000920 | prose | pages [32] -->
Other Parameters:

<!-- b000921 | prose | pages [32] -->
Location on river = 28.125

<!-- b000922 | prose | pages [32] -->
0.04

<!-- b000923 | prose | pages [32] -->
miles (1/8 of river length)

<!-- b000924 | prose | pages [32] -->
Distance between sites = 1.25 miles (1/100 of river length)

<!-- b000925 | prose | pages [32] -->
Total # of Campsites = 99

<!-- b000926 | prose | pages [32] -->
0.03

<!-- b000927 | prose | pages [32] -->
0.02

<!-- b000928 | prose | pages [32] -->
0.01

<!-- b000929 | prose | pages [32] -->
0

<!-- b000930 | furniture | pages [32] -->


<!-- b000931 | prose | pages [32] -->
0 10 20 30 40

<!-- b000932 | furniture | pages [32] -->


<!-- b000933 | prose | pages [32] -->
50 60 70 80 90 100

<!-- b000934 | prose | pages [32] -->
Number of Boats

<!-- b000935 | caption | pages [32] -->
Figure 19: Probability a Fast Boat must travel 14 miles - Close Campsites

<!-- b000936 | furniture | pages [33] -->
Team # 15171

<!-- b000937 | furniture | pages [33] -->
Page 31

<!-- b000938 | prose | pages [33] -->
Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.25

<!-- b000939 | prose | pages [33] -->
P(fast) = .1 P(fast) = .25 P(fast) = .5 P(fast) = .75 P(fast) = .9

<!-- b000940 | prose | pages [33] -->
0.2

<!-- b000941 | prose | pages [33] -->
1% cutoff

<!-- b000942 | prose | pages [33] -->
Other Parameters:

<!-- b000943 | prose | pages [33] -->
Probability of having to travel an additional 14 miles

<!-- b000944 | prose | pages [33] -->
Location on river = 28.125 miles (1/8 of river length)

<!-- b000945 | prose | pages [33] -->
Distance between sites = 7.5

<!-- b000946 | prose | pages [33] -->
0.15

<!-- b000947 | prose | pages [33] -->
miles (1/30 of river length)

<!-- b000948 | prose | pages [33] -->
Total # of Campsites = 29

<!-- b000949 | prose | pages [33] -->
0.1

<!-- b000950 | prose | pages [33] -->
0.05

<!-- b000951 | prose | pages [33] -->
0

<!-- b000952 | furniture | pages [33] -->


<!-- b000953 | prose | pages [33] -->
0 10 20 30 40

<!-- b000954 | furniture | pages [33] -->


<!-- b000955 | prose | pages [33] -->
50 60 70 80 90 100

<!-- b000956 | prose | pages [33] -->
Number of Boats

<!-- b000957 | caption | pages [33] -->
Figure 20: Probability a Slow Boat must travel 14 miles - Far Campsites

<!-- b000958 | furniture | pages [34] -->
Team # 15171

<!-- b000959 | furniture | pages [34] -->
Page 32

<!-- b000960 | prose | pages [34] -->
Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.25

<!-- b000961 | prose | pages [34] -->
P(fast) = .1 P(fast) = .25 P(fast) = .5 P(fast) = .75 P(fast) = .9

<!-- b000962 | prose | pages [34] -->
0.2

<!-- b000963 | prose | pages [34] -->
1% cutoff

<!-- b000964 | prose | pages [34] -->
Probability of having to travel an additional 14 miles

<!-- b000965 | prose | pages [34] -->
Other Parameters:

<!-- b000966 | prose | pages [34] -->
Location on river = 28.125 miles (1/8 of riverlength)

<!-- b000967 | prose | pages [34] -->
0.15

<!-- b000968 | prose | pages [34] -->
Distance between sites = 3.75 miles (1/60 of river length)

<!-- b000969 | prose | pages [34] -->
Total # of Campsites = 59

<!-- b000970 | prose | pages [34] -->
0.1

<!-- b000971 | prose | pages [34] -->
0.05

<!-- b000972 | prose | pages [34] -->
0

<!-- b000973 | furniture | pages [34] -->


<!-- b000974 | prose | pages [34] -->
0 10 20 30 40

<!-- b000975 | furniture | pages [34] -->


<!-- b000976 | prose | pages [34] -->
50 60 70 80 90 100

<!-- b000977 | prose | pages [34] -->
Number of Boats

<!-- b000978 | caption | pages [34] -->
Figure 21: Probability a Slow Boat must travel 14 miles - Medium-Distance Campsites

<!-- b000979 | furniture | pages [35] -->
Team # 15171

<!-- b000980 | furniture | pages [35] -->
Page 33

<!-- b000981 | prose | pages [35] -->
Probability of having to travel an additional distance of 14 miles for varying numbers of boats on the water 0.07

<!-- b000982 | prose | pages [35] -->
P(fast) = .1 P(fast) = .25

<!-- b000983 | prose | pages [35] -->
0.06

<!-- b000984 | prose | pages [35] -->
P(fast) = .5 P(fast) = .75 P(fast) = .9

<!-- b000985 | prose | pages [35] -->
Probability of having to travel an additional 14 miles

<!-- b000986 | prose | pages [35] -->
1% cutoff

<!-- b000987 | prose | pages [35] -->
0.05

<!-- b000988 | prose | pages [35] -->
Other Parameters:

<!-- b000989 | prose | pages [35] -->
Location on river = 28.125 miles (1/8 of river length)

<!-- b000990 | prose | pages [35] -->
0.04

<!-- b000991 | prose | pages [35] -->
Distance between sites = 1.25 miles (1/100 of river length)

<!-- b000992 | prose | pages [35] -->
Total # of Campsites = 99

<!-- b000993 | prose | pages [35] -->
0.03

<!-- b000994 | prose | pages [35] -->
0.02

<!-- b000995 | prose | pages [35] -->
0.01

<!-- b000996 | prose | pages [35] -->
0

<!-- b000997 | furniture | pages [35] -->


<!-- b000998 | prose | pages [35] -->
0 10 20 30 40

<!-- b000999 | furniture | pages [35] -->


<!-- b001000 | prose | pages [35] -->
50 60 70 80 90 100

<!-- b001001 | prose | pages [35] -->
Number of Boats

<!-- b001002 | caption | pages [35] -->
Figure 22: Probability a Slow Boat must travel 14 miles - Close Campsites

<!-- b001003 | furniture | pages [36] -->
Team # 15171

<!-- b001004 | furniture | pages [36] -->
Page 34

<!-- b001005 | heading | pages [36] -->
References

<!-- b001006 | references | pages [36] -->
[1] Federal Aviation Administration. Code of federal regulations sec 91.205. http://www.

<!-- b001007 | references | pages [36] -->
airweb.faa.gov/Regulatory_and_Guidance_Library/rgFAR.nsf/,

<!-- b001008 | references | pages [36] -->
2007.

<!-- b001009 | references | pages [36] -->
[2] Rick Durrett. Essentials of Stochastic Processes. Springer, Ithica, NY, 1999.

<!-- b001010 | references | pages [36] -->
http://www.

<!-- b001011 | references | pages [36] -->
[3] Arizona River Runners.

<!-- b001012 | references | pages [36] -->
Colorado river rafting in arizona.

<!-- b001013 | references | pages [36] -->
raftarizona.com/, 2011.

<!-- b001014 | references | pages [36] -->
http://www.nps.gov/grca/planyourvisit/

<!-- b001015 | references | pages [36] -->
[4] National

<!-- b001016 | references | pages [36] -->
Park

<!-- b001017 | references | pages [36] -->
Service.

<!-- b001018 | references | pages [36] -->
weightedlottery.htm, 2012.
