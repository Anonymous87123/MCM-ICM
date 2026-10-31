# P-D-2019-1922074-a699b77f

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | title | pages [1] -->
1922074

<!-- b000005 | prose | pages [1] -->
T1 F1

<!-- b000006 | prose | pages [1] -->
T2 F2 Problem Chosen T3 F3 T4 F4 D

<!-- b000007 | prose | pages [1] -->
2019 MCM/ICM Summary Sheet A Model for Determining Evacuation Routes

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
In 2018, the number of people in the Louvre was 10.8 million, creating a new high. At the same time, in the event of an emergency, such a large number of tourists will increase the difficulty of evacuation and raise the risk. Therefore, our goal is to design the Louvre's emergency evacuation plan to evacuate visitors from the museum and estimate the evacuation time, while also allowing emergency personnel to enter the building as quickly as possible, as well as considering other factors and potential threats.

<!-- b000010 | prose | pages [1] -->
We make the Visitor Emergency Evacuation(VEE) model to design the evacuation plan. The first model of the emergency evacuation plan is based on an improved ant colony optimization algorithm. The model transforms the entire Louvre into a topological map and influences the selection probability by setting the pheromone concentration threshold to determine the optimal evacuation route for visitors to leave from each region. We also established an evacuation time model and found that the shortest evacuation time for the largest number of visitors in the library was 417.2 s. This result indicates that our evacuation plan is reliable.

<!-- b000011 | prose | pages [1] -->
The third model uses the improved Dijkstra algorithm. The model considers the entire Louvre as a time-varying topology map to determine the route of emergency personnel to the emergency area as quickly as possible. By assuming an emergency in the 101 area of the -1F and adding a new exit near the B3 stairs of the 0F, the optimal path for the emergency personnel to reach the area and the shortest time of 130s are obtained. This result shows that our model is reliable.

<!-- b000012 | prose | pages [1] -->
We also discussed other factors that have an impact on evacuation time, such as whether to open new exports, the impact of tourist diversity, the consequences of potential threats, and so on. And we propose policy and procedural recommendations for emergency management of the Louvre . Additionally, we discuss how we can adapt and implement our models for other large, crowded structures. Then we performed sensitivity analysis on two important parameters: the number of people passing through the stairs and the speed. The results show that the changes of these two parameters will have a huge impact on the shortest evacuation time.

<!-- b000013 | keywords | pages [1] -->
Key Words: Emergency evacuation plan, Ant colony optimization algorithm,

<!-- b000014 | prose | pages [1] -->
Time model, Dijkstra algorithm, Other factors

<!-- b000015 | prose | pages [2] -->
Content

<!-- b000016 | prose | pages [2] -->
1. Introduction.....................................................................................................................................1

<!-- b000017 | prose | pages [2] -->
1.1 Background..............................................................................................................................1 1.2 Restatement of Problems...................................................................................................... 1 1.3 Our Work.................................................................................................................................2

<!-- b000018 | prose | pages [2] -->
2. Assumptions and Symbol Table.................................................................................................2

<!-- b000019 | prose | pages [2] -->
2.1 Assumptions........................................................................................................................... 2 2.2 Symbol Table..........................................................................................................................2

<!-- b000020 | prose | pages [2] -->
3. The Visitor Emergency Evacuation model................................................................................ 3

<!-- b000021 | prose | pages [2] -->
3.1 Distribution of tourists..........................................................................................................3 3.2 The evacuation route.............................................................................................................4 3.3 The evacuation time.............................................................................................................. 7 3.4 Emergency personnel......................................................................................................... 10 3.5 Potential factors................................................................................................................... 13

<!-- b000022 | prose | pages [2] -->
4. Policy and procedural recommendations................................................................................ 17

<!-- b000023 | prose | pages [2] -->
5. The VEE model for other large structures............................................................................... 18

<!-- b000024 | prose | pages [2] -->
6. Sensitivity Analysis.....................................................................................................................19

<!-- b000025 | prose | pages [2] -->
7. Strengths and Weaknesses......................................................................................................... 20

<!-- b000026 | prose | pages [2] -->
7.1 Strengths...............................................................................................................................20 7.2 Weaknesses..........................................................................................................................20

<!-- b000027 | prose | pages [2] -->
8. Conclusion.....................................................................................................................................20

<!-- b000028 | prose | pages [2] -->
9. References......................................................................................................................................21

<!-- b000029 | prose | pages [2] -->
10. Appendix......................................................................................................................................21

<!-- b000030 | furniture | pages [3] -->
Team # 1922074

<!-- b000031 | prose | pages [3] -->
1.

<!-- b000032 | heading | pages [3] -->
Introduction

<!-- b000033 | prose | pages [3] -->
1.1

<!-- b000034 | heading | pages [3] -->
Background

<!-- b000035 | furniture | pages [3] -->
Page

<!-- b000036 | furniture | pages [3] -->
of 29

<!-- b000037 | furniture | pages [3] -->
1

<!-- b000038 | prose | pages [3] -->
Nowadays, urban development has entered a period of rapid growth, the city’s scale has expanded rapidly, the number of high-rise buildings and large buildings has increased, and dangers personnel are highly intensive.

<!-- b000039 | prose | pages [3] -->
The and harmfulness of unconventional emergencies, such as overcrowded and trampling in open spaces and buildings, are becoming more and more serious, making the public security of the mainland face severe challenges. Due to the serious casualties caused by emergency emergencies in densely populated places, which is one of the major disasters faced by mankind. Hence, solving the problem of emergency evacuation in densely populated areas has its unprecedented significance in today’s world.

<!-- b000040 | prose | pages [3] -->
The increasing number of terror attacks in France requires a review of the emergency evacuation plans at many popular destinations. In general, the goal of evacuation is to have all occupants leave the building as quickly and safely as possible. Upon notification of a required evacuation, individuals egress to and through an optimal exit in order to empty the building as quickly as possible.

<!-- b000041 | prose | pages [3] -->
The Louvre is one of the world’s largest and most visited art museum, receiving more than 8.1 million visitors in 2017. The number of guests in the museum varies throughout the day and year, which provides challenges in planning for regular movement within the museum. The diversity of visitors -- speaking a variety of languages, groups traveling together, and disabled visitors -- makes evacuation in an emergency even more challenging. As a result, it is necessary for the Louvre to have a complete emergency evacuation plan.

<!-- b000042 | prose | pages [3] -->
1.2 Restatement of Problems

<!-- b000043 | prose | pages [3] -->
To evacuate people safely when an emergency occurs, the reasonable evacuation plans at the Louvre should be developed, while the following tasks are to be accomplished :

<!-- b000044 | prose | pages [3] -->
• The number of guests in the museum varies throughout the day and year and the diversity of visitors such as disabled visitors make evacuation in an emergency challenging. What’s more, the actual exit points that can be used is not only the four exits that the public knows. While public awareness of these exit points could provide additional strength to an evacuation plan, their use would simultaneously cause security concerns due to the lower or limited security postures at these exits compared with level of security at the four main entrances. Thus, when creating the model, we should consider carefully how to evacuate disabled visitors, when and how any additional exits might be utilized.

<!-- b000045 | prose | pages [3] -->
• The model should allow the museum leaders to explore a range of options to evacuate visitors from the museum, while also allowing emergency personnel to enter the building as quickly as possible. It is also important to identify potential bottlenecks that may limit movement towards the exits, address a broad set of considerations and various types of potential threats.

<!-- b000046 | prose | pages [3] -->
• Validate the model and discuss how the Louvre would implement it.

<!-- b000047 | prose | pages [3] -->
1 1

<!-- b000048 | furniture | pages [4] -->
Team # 1922074

<!-- b000049 | furniture | pages [4] -->
Page

<!-- b000050 | furniture | pages [4] -->
of 29

<!-- b000051 | furniture | pages [4] -->
2

<!-- b000052 | prose | pages [4] -->
Based on the results of the work, propose policy and procedural recommendations for • emergency management of the Louvre.

<!-- b000053 | prose | pages [4] -->
1.3 Our Work

<!-- b000054 | prose | pages [4] -->
According to the current queuing time displayed by the APP "Affluences", we get different numbers of people at different times of the day. According to the improved ant colony optimization algorithm, we get the best evacuation route for tourists. Through our time model, we found the shortest time for visitors to evacuate. Based on the improved Dijkstra algorithm, we get the optimal route for emergency personnel to reach the emergency area and calculate the required time. At the same time, other potential factors were considered, such as the diversity of visitors, the opening of other entrances and exits, and uncertain potential threats.

<!-- b000055 | prose | pages [4] -->
Finally, the propose policy and procedural recommendations for emergency management of the Louvre and Additionally, discuss how we can adapt and implement our models for other large, crowded structures.

<!-- b000056 | heading | pages [4] -->
2. Assumptions and Symbol Table

<!-- b000057 | heading | pages [4] -->
2.1 Assumptions

<!-- b000058 | prose | pages [4] -->
We make the following basic assumptions in order to simplify the problem. Each of our assumptions is justified.

<!-- b000059 | prose | pages [4] -->
• Assuming that each visitor runs at the same speed.

<!-- b000060 | prose | pages [4] -->
• Assuming that the distance from chest to back of each visitor is the same. The length of the queue can be calculate directly based on the number of visitors.

<!-- b000061 | prose | pages [4] -->
• Assuming that visitors will escape from the building orderly.

<!-- b000062 | prose | pages [4] -->
• Assuming that when a block happen, tourists with low floors on the stairs are evacuated firstly.

<!-- b000063 | heading | pages [4] -->
2.2 Symbol Table

<!-- b000064 | prose | pages [4] -->
Symbol that we mainly use in the model are shown in the following table :

<!-- b000065 | caption | pages [4] -->
Table 1: Symbol Table

<!-- b000066 | heading | pages [4] -->
Symbol

<!-- b000067 | prose | pages [4] -->
Definition

<!-- b000068 | prose | pages [4] -->
the number of stairs on the 2nd floor I

<!-- b000069 | prose | pages [4] -->
L thi th j the length of the human chain at the ij

<!-- b000070 | prose | pages [4] -->
fL

<!-- b000071 | prose | pages [4] -->
stairs of the floor

<!-- b000072 | prose | pages [4] -->
the length of the stairs

<!-- b000073 | prose | pages [4] -->
it thi the time evacuate from the stairs

<!-- b000074 | prose | pages [4] -->
2 2

<!-- b000075 | furniture | pages [5] -->
Team # 1922074

<!-- b000076 | prose | pages [5] -->
S

<!-- b000077 | furniture | pages [5] -->
Page

<!-- b000078 | furniture | pages [5] -->
of 29

<!-- b000079 | furniture | pages [5] -->
3

<!-- b000080 | prose | pages [5] -->
thi th j the number of visitors at the ij

<!-- b000081 | prose | pages [5] -->
fn

<!-- b000082 | prose | pages [5] -->
stairs entrance of the floor

<!-- b000083 | prose | pages [5] -->
the space between visitors

<!-- b000084 | prose | pages [5] -->
il thi the length required to escape to the

<!-- b000085 | prose | pages [5] -->
T

<!-- b000086 | prose | pages [5] -->
staircase

<!-- b000087 | prose | pages [5] -->
the time for evacuating all visitors min

<!-- b000088 | heading | pages [5] -->
3. The Visitor Emergency Evacuation model

<!-- b000089 | prose | pages [5] -->
In this model, when an emergency occurs, the Visitor Emergency Evacuation(VEE) model uses the improved ant colony optimization algorithm to plan evacuation routes for visitors and calculate the the minimum time for evacuation. It also uses the improved Dijkstra Algorithm to consider how emergency personnel reach the emergency area as quickly as possible and other potential factors such as other entrances that visitors don’t know, diversity of visitors and various types of potential threats.

<!-- b000090 | caption | pages [5] -->
Figure 1. The VEE Model

<!-- b000091 | prose | pages [5] -->
According to the floor plan of the Louvre, we can know that the Louvre has four main entrances, including the pyramid entrance, the Passage Richelieu entrance, the Carrousel du Louvre entrance on the 2nd floor, and the Portes Des Lions entrance on the 0th floor of the building. Due to the different locations of the open exhibition areas on each floor, we divide the Louvre into two catecories: one category has five floors(from -2F to 2F), there are three entrance located on the -2nd basement. The other category has three floors(from 0F to 2F), while the entrance is on the 0th floor. Most visitors in this area will go through the stairs to the entrance, the rest of the visitors can escape directly on the 0th floor.

<!-- b000092 | heading | pages [5] -->
3.1 Distribution of tourists

<!-- b000093 | prose | pages [5] -->
There are many exhibition areas in the Louvre. In order to facilitate the calculation, we first

<!-- b000094 | prose | pages [5] -->
3 3

<!-- b000095 | furniture | pages [6] -->
Team # 1922074

<!-- b000096 | furniture | pages [6] -->
Page

<!-- b000097 | furniture | pages [6] -->
of 29

<!-- b000098 | furniture | pages [6] -->
4

<!-- b000099 | prose | pages [6] -->
assume that the number of people in each exhibition area is equal. According to the information, there are three art treasures in the Louvre, located in 345, 703 and 711. The number of tourists in these three exhibition areas is too many. We assume that the three exhibition areas have three times as much as the number of tourists in the ordinary exhibition area. Then, the number of tourists in each exhibition area is obtained.

<!-- b000100 | prose | pages [6] -->
The number of visitors in the Louvre varies throughout the day and year. We reverse the current number of people in the library based on the current queue time by “Affluences” and record it every 15 minutes. Then we can get the diagram between number of visitors and time. As we all know, the Louvre is open every day (except Tuesday) from 9 A.M. to 6 P.M, night opening until 9:45 P.M. on Wednesdays and Fridays. Regardless of the special events, the change of visitors’ number is showed in the Figure 2. 2(B) represents the change on Wednesdays and Fridays, 2(A) represents the change on rest days.

<!-- b000101 | caption | pages [6] -->
Figure 2. The number of visitors

<!-- b000102 | heading | pages [6] -->
3.2 The evacuation route

<!-- b000103 | prose | pages [6] -->
We cite and reference the ant colony optimization algorithm of "Mathematical model of emergency evacuation in densely populated areas and its optimal solution" [5] and improve it, and use the improved ant colony optimization algorithm to select the optimal escape route, and establish the following route model.

<!-- b000104 | heading | pages [6] -->
3.2.1 Traditional ant colony optimization algorithm

<!-- b000105 | prose | pages [6] -->
( . , ) G N R  We convert the Louvre's plan into a topology and build a mesh function , where 0 is the node set. Staircases, each of exhibitions and entrances are nodes. R is route set. N  Stairs, corridors, passages are routes.

<!-- b000106 | prose | pages [6] -->
distribution. m is the total number of ants,

<!-- b000107 | prose | pages [6] -->
thi node at time t .

<!-- b000108 | prose | pages [6] -->
is an environmental initial pheromone 0 0

<!-- b000109 | prose | pages [6] -->
n

<!-- b000110 | prose | pages [6] -->


<!-- b000111 | prose | pages [6] -->
( ) (t )

<!-- b000112 | prose | pages [6] -->
m b i t

<!-- b000113 | prose | pages [6] -->
bi

<!-- b000114 | prose | pages [6] -->


<!-- b000115 | prose | pages [6] -->
, is the number of ants of the 1

<!-- b000116 | prose | pages [6] -->
i

<!-- b000117 | prose | pages [6] -->


<!-- b000118 | prose | pages [6] -->
4 4

<!-- b000119 | furniture | pages [7] -->
Team # 1922074

<!-- b000120 | prose | pages [7] -->
k  NC During the iteration of k times ( max

<!-- b000121 | furniture | pages [7] -->
Page

<!-- b000122 | furniture | pages [7] -->
of 29

<!-- b000123 | furniture | pages [7] -->
5

<!-- b000124 | prose | pages [7] -->
  ,2,1 , k k m  ), the ant select the probability  according to the pheromone concentration left by the ant colony. The selection probability

<!-- b000125 | prose | pages [7] -->
t pk

<!-- b000126 | prose | pages [7] -->
thi th node at time t . is the probability that the ant k moves from the ij (t ) j node to the indicates the concentration of pheromone between nodes i ,  Function ij

<!-- b000127 | prose | pages [7] -->


<!-- b000128 | prose | pages [7] -->
at time t . j

<!-- b000129 | prose | pages [7] -->
is pheromone heuristic factor which indicates how important pheromone is to ant  is expected heuristic value which indicates how important selection probabilities, allowed expectation value is to ant selection probabilities. set of nodes that ant k can choose next.

<!-- b000130 | prose | pages [7] -->


<!-- b000131 | prose | pages [7] -->


<!-- b000132 | prose | pages [7] -->
(

<!-- b000133 | prose | pages [7] -->
t

<!-- b000134 | prose | pages [7] -->


<!-- b000135 | prose | pages [7] -->
ij

<!-- b000136 | prose | pages [7] -->


<!-- b000137 | prose | pages [7] -->


<!-- b000138 | prose | pages [7] -->


<!-- b000139 | prose | pages [7] -->


<!-- b000140 | prose | pages [7] -->


<!-- b000141 | prose | pages [7] -->
k

<!-- b000142 | prose | pages [7] -->
p t

<!-- b000143 | prose | pages [7] -->


<!-- b000144 | prose | pages [7] -->


<!-- b000145 | prose | pages [7] -->
ij

<!-- b000146 | prose | pages [7] -->


<!-- b000147 | prose | pages [7] -->
s allowed

<!-- b000148 | prose | pages [7] -->


<!-- b000149 | prose | pages [7] -->
k

<!-- b000150 | prose | pages [7] -->


<!-- b000151 | prose | pages [7] -->
is a feasible set, indicating the k

<!-- b000152 | prose | pages [7] -->
 

<!-- b000153 | prose | pages [7] -->
  

<!-- b000154 | prose | pages [7] -->
) ) ( )

<!-- b000155 | prose | pages [7] -->
t

<!-- b000156 | prose | pages [7] -->


<!-- b000157 | prose | pages [7] -->
ij

<!-- b000158 | prose | pages [7] -->
,

<!-- b000159 | prose | pages [7] -->
j allowed

<!-- b000160 | prose | pages [7] -->


<!-- b000161 | prose | pages [7] -->
 

<!-- b000162 | prose | pages [7] -->
k

<!-- b000163 | prose | pages [7] -->
 

<!-- b000164 | prose | pages [7] -->
( ( ) ( )

<!-- b000165 | prose | pages [7] -->
t t t

<!-- b000166 | prose | pages [7] -->


<!-- b000167 | prose | pages [7] -->
(1)

<!-- b000168 | prose | pages [7] -->
is is is

<!-- b000169 | prose | pages [7] -->
,0

<!-- b000170 | prose | pages [7] -->
others

<!-- b000171 | prose | pages [7] -->
The principle of traditional ant colony optimization algorithm is that the principle of the traditional ant colony optimization algorithm is that the ants with shorter routes release more pheromone. As time progresses, the concentration of pheromone accumulated on the shorter route gradually increases, and the number of ants that select the route is also getting more and more. Eventually, ants will focus on the best route under positive feedback. But for the evacuation of people, this situation will happen: when people reach one end of the channel and find that there are many people in the channel, people may choose another channel with fewer people to avoid congestion and collision. When it is found that there are fewer people in the channel, it means that the channel may not be the optimal escape channel, so a channel with more people will be selected. As a result, we need to improve the ant colony optimization algorithm.

<!-- b000172 | heading | pages [7] -->
3.2.2 Improved ant colony optimization algorithm

<!-- b000173 | prose | pages [7] -->
We set a threshold to improve the ant colony optimization algorithm. When the pheromone concentration is lower than the threshold, it means that the number of people in the channel is small. Perhaps this route is not the optimal escape route; when the pheromone concentration is higher than the threshold, it means that the channel is more likely to occur congestion and blocking.

<!-- b000174 | prose | pages [7] -->
For the threshold, when people pass through the channel, they may be crowded inside it without order. However, when passing through the exit of the channel, the maximum number of people allowed to pass at one time is only related to the width of the exit, that is, people are exporting in the form of multiple human chains. The length of the human chain L : is d

<!-- b000175 | prose | pages [7] -->
S L 

<!-- b000176 | prose | pages [7] -->
T d

<!-- b000177 | prose | pages [7] -->
( )1 d d S e  

<!-- b000178 | prose | pages [7] -->
T n

<!-- b000179 | prose | pages [7] -->
(2)

<!-- b000180 | prose | pages [7] -->
d

<!-- b000181 | prose | pages [7] -->
n is the maximum number of people allowed to pass the channel, where d dl is the length

<!-- b000182 | prose | pages [7] -->
is the number of people arriving at the exit of the channel at time T . S of queue, T 1v is m / s the speed when people move. The limit safety speed of people running freely is 1.5

<!-- b000183 | prose | pages [7] -->
5 5

<!-- b000184 | furniture | pages [8] -->
Team # 1922074

<!-- b000185 | furniture | pages [8] -->
Page

<!-- b000186 | furniture | pages [8] -->
of 29

<!-- b000187 | furniture | pages [8] -->
6

<!-- b000188 | prose | pages [8] -->
according to the survey data. At this moment, a visitor is at the entrance of the channel. The speed of human chain is v . Obviously, v  v 1 . .

<!-- b000189 | prose | pages [8] -->
1t （the time）, the tourists just When the human chain completely leaves the channel after arrive at the exit of a channel, which means that the length is the most suitable and this

<!-- b000190 | prose | pages [8] -->
L d  t 

<!-- b000191 | prose | pages [8] -->
channel is the optimal route. That is,

<!-- b000192 | prose | pages [8] -->
1 v L ST  nvt d . At this moment, . 1 v 1

<!-- b000193 | prose | pages [8] -->
Let each person carry a pheromone, then the pheromone concentration of the channel is

<!-- b000194 | prose | pages [8] -->
1t . Finally, the selection probability after improvement is: nvt , the threshold is 1

<!-- b000195 | prose | pages [8] -->
 

<!-- b000196 | prose | pages [8] -->


<!-- b000197 | prose | pages [8] -->


<!-- b000198 | prose | pages [8] -->
( )

<!-- b000199 | prose | pages [8] -->
t

<!-- b000200 | prose | pages [8] -->
 

<!-- b000201 | prose | pages [8] -->
ij

<!-- b000202 | prose | pages [8] -->


<!-- b000203 | prose | pages [8] -->
 

<!-- b000204 | prose | pages [8] -->


<!-- b000205 | prose | pages [8] -->


<!-- b000206 | prose | pages [8] -->
( )

<!-- b000207 | prose | pages [8] -->
t

<!-- b000208 | prose | pages [8] -->
 

<!-- b000209 | prose | pages [8] -->


<!-- b000210 | prose | pages [8] -->
is

<!-- b000211 | prose | pages [8] -->
 

<!-- b000212 | prose | pages [8] -->


<!-- b000213 | prose | pages [8] -->


<!-- b000214 | prose | pages [8] -->
( )

<!-- b000215 | prose | pages [8] -->
t

<!-- b000216 | prose | pages [8] -->


<!-- b000217 | prose | pages [8] -->


<!-- b000218 | prose | pages [8] -->
ij

<!-- b000219 | prose | pages [8] -->
k

<!-- b000220 | prose | pages [8] -->
1

<!-- b000221 | prose | pages [8] -->
p t

<!-- b000222 | prose | pages [8] -->


<!-- b000223 | prose | pages [8] -->


<!-- b000224 | prose | pages [8] -->


<!-- b000225 | prose | pages [8] -->


<!-- b000226 | prose | pages [8] -->


<!-- b000227 | prose | pages [8] -->
ij

<!-- b000228 | prose | pages [8] -->
( )

<!-- b000229 | prose | pages [8] -->
t

<!-- b000230 | prose | pages [8] -->


<!-- b000231 | prose | pages [8] -->


<!-- b000232 | prose | pages [8] -->
is

<!-- b000233 | prose | pages [8] -->
 

<!-- b000234 | prose | pages [8] -->
,0

<!-- b000235 | prose | pages [8] -->
others

<!-- b000236 | prose | pages [8] -->


<!-- b000237 | prose | pages [8] -->


<!-- b000238 | heading | pages [8] -->
3.2.3 The optimal evacuation route

<!-- b000239 | prose | pages [8] -->


<!-- b000240 | prose | pages [8] -->


<!-- b000241 | prose | pages [8] -->
( ( )

<!-- b000242 | prose | pages [8] -->
t t

<!-- b000243 | prose | pages [8] -->
ij ij

<!-- b000244 | prose | pages [8] -->
, , , ( )

<!-- b000245 | prose | pages [8] -->
j s allowed t nvt

<!-- b000246 | prose | pages [8] -->


<!-- b000247 | prose | pages [8] -->


<!-- b000248 | prose | pages [8] -->


<!-- b000249 | prose | pages [8] -->


<!-- b000250 | prose | pages [8] -->
1

<!-- b000251 | prose | pages [8] -->
k ij

<!-- b000252 | prose | pages [8] -->


<!-- b000253 | prose | pages [8] -->
( )

<!-- b000254 | prose | pages [8] -->
t

<!-- b000255 | prose | pages [8] -->
is is

<!-- b000256 | prose | pages [8] -->


<!-- b000257 | prose | pages [8] -->


<!-- b000258 | prose | pages [8] -->
( )

<!-- b000259 | prose | pages [8] -->
t

<!-- b000260 | prose | pages [8] -->


<!-- b000261 | prose | pages [8] -->
ij

<!-- b000262 | prose | pages [8] -->
, , , ( )

<!-- b000263 | prose | pages [8] -->
j s allowed t nvt

<!-- b000264 | prose | pages [8] -->


<!-- b000265 | prose | pages [8] -->


<!-- b000266 | prose | pages [8] -->


<!-- b000267 | prose | pages [8] -->
 

<!-- b000268 | prose | pages [8] -->
1

<!-- b000269 | prose | pages [8] -->
k ij

<!-- b000270 | prose | pages [8] -->
  

<!-- b000271 | prose | pages [8] -->
( )

<!-- b000272 | prose | pages [8] -->
t

<!-- b000273 | prose | pages [8] -->


<!-- b000274 | prose | pages [8] -->
is

<!-- b000275 | prose | pages [8] -->
(3)

<!-- b000276 | prose | pages [8] -->
We convert the Louvre's floor plan into a topographic map, and the following figure is an example of the 1st and 2nd floor.

<!-- b000277 | caption | pages [8] -->
Figure 3. The topology of the 1st and 2nd floor

<!-- b000278 | prose | pages [8] -->
6 6

<!-- b000279 | furniture | pages [9] -->
Team # 1922074

<!-- b000280 | furniture | pages [9] -->
Page

<!-- b000281 | furniture | pages [9] -->
of 29

<!-- b000282 | furniture | pages [9] -->
7

<!-- b000283 | prose | pages [9] -->
In the topology, circles indicate various areas, and the nodes with symbols refers to the entrances of stairs, and the red line refers to stairs between different floors.

<!-- b000284 | prose | pages [9] -->
We choose the appropriate parameters, bring the Louvre plane topology into the algorithm, and finally get the following optimal evacuation routes. In Figure 4, orange arrows indicate evacuated routes.

<!-- b000285 | caption | pages [9] -->
Figure 4. The optimal evacuation route for the Louvre

<!-- b000286 | heading | pages [9] -->
3.3 The evacuation time

<!-- b000287 | prose | pages [9] -->
We figure out that the time required to evacuate all the visitors in the Louvre is the time when last visitor escapes from the Louvre. Moreover, the farthest floor from the 0th floor and the 2nd basement is the 2nd floor. As a result, there must be a stairway that allows visitors from this stairway to evacuate for the longest time. The time required to evacuate all visitors is the longest time for the last visitor to escape the Louvre, and the shortest evacuation time is the minimum of the longest time.

<!-- b000288 | prose | pages [9] -->
Assuming that the number of stairs on the 2nd floor is I , the length of the human chain at thi L , the length of the stairs is th j the stairs of the floor is ij

<!-- b000289 | prose | pages [9] -->
thi

<!-- b000290 | prose | pages [9] -->
fL , the time evacuate from

<!-- b000291 | prose | pages [9] -->
thi S , th j it , the number of visitors at the the stairs is stairs entrance of the floor is ij

<!-- b000292 | prose | pages [9] -->
7 7

<!-- b000293 | furniture | pages [10] -->
Team # 1922074

<!-- b000294 | furniture | pages [10] -->
Page

<!-- b000295 | furniture | pages [10] -->
of 29

<!-- b000296 | furniture | pages [10] -->
8

<!-- b000297 | prose | pages [10] -->
fn is the number of visitors is the thickness of a visitor, e is the space between visitors, d

<!-- b000298 | prose | pages [10] -->
' jl who can accommodate up to one row at the stairway, v is the speed when people run,

<!-- b000299 | prose | pages [10] -->
il is the length of the exit from the person to the floor with the exit,

<!-- b000300 | prose | pages [10] -->
thi dt

<!-- b000301 | prose | pages [10] -->
is the length required

<!-- b000302 | prose | pages [10] -->
T is the time of blockage in the stairs, to escape to the staircase,

<!-- b000303 | prose | pages [10] -->
evacuating all visitors.

<!-- b000304 | prose | pages [10] -->
is the time for min

<!-- b000305 | prose | pages [10] -->
d of each person, the The length of the human chain is determined by the thickness distance e fn . No matter between people and the number of people through the stairs

<!-- b000306 | prose | pages [10] -->
how crowded outside the stairway, when passing through the stairway, the number of fn , so the human chain can be equivalent to the people passing through the stairway is just

<!-- b000307 | prose | pages [10] -->
fn L personal chain, and the new human chain length

<!-- b000308 | prose | pages [10] -->
L

<!-- b000309 | prose | pages [10] -->
ij

<!-- b000310 | prose | pages [10] -->
it

<!-- b000311 | prose | pages [10] -->
is: ij  

<!-- b000312 | prose | pages [10] -->
1 S d S e  

<!-- b000313 | prose | pages [10] -->
ij ij

<!-- b000314 | prose | pages [10] -->
 

<!-- b000315 | prose | pages [10] -->
n

<!-- b000316 | prose | pages [10] -->
(4)

<!-- b000317 | prose | pages [10] -->
f

<!-- b000318 | prose | pages [10] -->
li is composed of the following times: the time The

<!-- b000319 | prose | pages [10] -->
L f

<!-- b000320 | prose | pages [10] -->
from the current area to the v

<!-- b000321 | prose | pages [10] -->
'

<!-- b000322 | prose | pages [10] -->
l j

<!-- b000323 | prose | pages [10] -->
through the stairs; the time

<!-- b000324 | prose | pages [10] -->
stairway; the time v

<!-- b000325 | prose | pages [10] -->
Lij

<!-- b000326 | prose | pages [10] -->
after reaching the exit floor, the

<!-- b000327 | prose | pages [10] -->
v

<!-- b000328 | prose | pages [10] -->
through the exit; and possibly on the way The congestion

<!-- b000329 | prose | pages [10] -->
time to the exit; the time v

<!-- b000330 | prose | pages [10] -->
dt .So we can get: time caused by the blockage will occur

<!-- b000331 | prose | pages [10] -->
l t 

<!-- b000332 | prose | pages [10] -->
i i

<!-- b000333 | prose | pages [10] -->
v

<!-- b000334 | prose | pages [10] -->
So, The shortest evacuation time is

<!-- b000335 | prose | pages [10] -->
T 

<!-- b000336 | prose | pages [10] -->
dt : For

<!-- b000337 | prose | pages [10] -->
'

<!-- b000338 | prose | pages [10] -->
L

<!-- b000339 | prose | pages [10] -->
L

<!-- b000340 | prose | pages [10] -->
l

<!-- b000341 | prose | pages [10] -->
f ij j t

<!-- b000342 | prose | pages [10] -->
    

<!-- b000343 | prose | pages [10] -->
d

<!-- b000344 | prose | pages [10] -->
v

<!-- b000345 | prose | pages [10] -->
v

<!-- b000346 | prose | pages [10] -->
v

<!-- b000347 | prose | pages [10] -->
(5)

<!-- b000348 | prose | pages [10] -->
  min max it

<!-- b000349 | prose | pages [10] -->
(6)

<!-- b000350 | prose | pages [10] -->
• Everyone moves at the same speed in the channel, so there is no blockage.

<!-- b000351 | prose | pages [10] -->
• Since the escape route of each layer may pass through the same stairs, the length and width of the stairs are determined. The following situation is easy to occur: visitors on the 2nd floor have reached the 1st floor stairs, and visitors on the 1st floor have not escaped from this stairway, and finally blockage will occur.

<!-- b000352 | prose | pages [10] -->
We assume that when the above situation occurs, there is a priority, that is, the higher floor ' L allows the lower floor visitors to go first. Then we can get the following model where

<!-- b000353 | prose | pages [10] -->
length of the human chain of the  

<!-- b000354 | prose | pages [10] -->
th j 1 

<!-- b000355 | prose | pages [10] -->
is ij

<!-- b000356 | prose | pages [10] -->
thi ' il staircase of the

<!-- b000357 | prose | pages [10] -->
to the stairs.

<!-- b000358 | prose | pages [10] -->
'

<!-- b000359 | prose | pages [10] -->
L

<!-- b000360 | prose | pages [10] -->


<!-- b000361 | prose | pages [10] -->
ij

<!-- b000362 | prose | pages [10] -->


<!-- b000363 | prose | pages [10] -->
t

<!-- b000364 | prose | pages [10] -->


<!-- b000365 | prose | pages [10] -->
d

<!-- b000366 | prose | pages [10] -->
j

<!-- b000367 | prose | pages [10] -->
floor, and is the distance

<!-- b000368 | prose | pages [10] -->
L

<!-- b000369 | prose | pages [10] -->
L

<!-- b000370 | prose | pages [10] -->
 

<!-- b000371 | prose | pages [10] -->


<!-- b000372 | prose | pages [10] -->
 

<!-- b000373 | prose | pages [10] -->


<!-- b000374 | prose | pages [10] -->
l

<!-- b000375 | prose | pages [10] -->
f ij

<!-- b000376 | prose | pages [10] -->
'

<!-- b000377 | prose | pages [10] -->
 

<!-- b000378 | prose | pages [10] -->


<!-- b000379 | prose | pages [10] -->
v l

<!-- b000380 | prose | pages [10] -->
 

<!-- b000381 | prose | pages [10] -->


<!-- b000382 | prose | pages [10] -->
i

<!-- b000383 | prose | pages [10] -->
 

<!-- b000384 | prose | pages [10] -->


<!-- b000385 | prose | pages [10] -->
i

<!-- b000386 | prose | pages [10] -->
v

<!-- b000387 | prose | pages [10] -->
v

<!-- b000388 | prose | pages [10] -->
v

<!-- b000389 | prose | pages [10] -->
 

<!-- b000390 | prose | pages [10] -->


<!-- b000391 | prose | pages [10] -->
 

<!-- b000392 | prose | pages [10] -->


<!-- b000393 | prose | pages [10] -->
v

<!-- b000394 | prose | pages [10] -->
(7)

<!-- b000395 | prose | pages [10] -->
8 8

<!-- b000396 | furniture | pages [11] -->
Team # 1922074

<!-- b000397 | prose | pages [11] -->


<!-- b000398 | prose | pages [11] -->
t

<!-- b000399 | prose | pages [11] -->


<!-- b000400 | prose | pages [11] -->
d

<!-- b000401 | prose | pages [11] -->
j

<!-- b000402 | prose | pages [11] -->
1 0 Set a parameter , when   dt  , ; when

<!-- b000403 | furniture | pages [11] -->
Page

<!-- b000404 | furniture | pages [11] -->
of 29

<!-- b000405 | furniture | pages [11] -->
9

<!-- b000406 | prose | pages [11] -->
 

<!-- b000407 | prose | pages [11] -->
' ' -' L L l l L L

<!-- b000408 | prose | pages [11] -->
  

<!-- b000409 | prose | pages [11] -->
ij ij i i f ij v

<!-- b000410 | prose | pages [11] -->
(8) 0 0   dt  , .

<!-- b000411 | prose | pages [11] -->
For the three floors model, the number of visitors on the 2nd floor is and the 0th is 0 S .

<!-- b000412 | prose | pages [11] -->
S , the 1st floor is 2 1 S

<!-- b000413 | prose | pages [11] -->
When an emergency occurs, since Arts of Africa, Asia, Oceania and the Americas is not connected to other areas on the 0th floor, only visitors in Arts of Africa, Asia, Oceania and the Americas can escape from the Portes Des Lions entrance. As a result, the evacuation plan of the visitors on the 0th floor can be divided into two situations:

<!-- b000414 | prose | pages [11] -->
0 S 00 01 S S    (9)

<!-- b000415 | prose | pages [11] -->
The visitors in Arts of Africa, Asia, Oceania and the Americas can escape directly, the . The rest visitors on the 0th can run from the 0th floor to the 1st floor, then 00 S number is run to the stairs leading to the Arts. Downstairs and escape from the Portes Des Lions 01 S entrance. The number of visitors in this part is . We observe the escape route, and find that the stairs from the 0th floor to the 1st floor is different from the stairs from the 2nd floor to the 1st floor. Therefore, visitors escape from 0F to 1F can be equivalent to visitors escape from the 2nd floor to the 1st floor.

<!-- b000416 | prose | pages [11] -->
2' S  01 2 S S S  (10)

<!-- b000417 | prose | pages [11] -->
is the number of visitors on the 2nd floor after the equivalent. 2 ' S Where

<!-- b000418 | prose | pages [11] -->
The 0th floor and the 2nd floor can be equivalent to the same floor, so there are only the situations that 2 floors of visitors going down the stairs on the first floor, and the first floor dt visitors have not been evacuated. The time of congestion

<!-- b000419 | prose | pages [11] -->
L

<!-- b000420 | prose | pages [11] -->
i

<!-- b000421 | prose | pages [11] -->
t

<!-- b000422 | prose | pages [11] -->


<!-- b000423 | prose | pages [11] -->
d

<!-- b000424 | prose | pages [11] -->
3T The evacuation time of three floors model

<!-- b000425 | prose | pages [11] -->
min T 3 

<!-- b000426 | prose | pages [11] -->
'

<!-- b000427 | prose | pages [11] -->
L l

<!-- b000428 | prose | pages [11] -->


<!-- b000429 | prose | pages [11] -->


<!-- b000430 | prose | pages [11] -->
1

<!-- b000431 | prose | pages [11] -->
i

<!-- b000432 | prose | pages [11] -->
t

<!-- b000433 | prose | pages [11] -->


<!-- b000434 | prose | pages [11] -->


<!-- b000435 | prose | pages [11] -->
d

<!-- b000436 | prose | pages [11] -->


<!-- b000437 | prose | pages [11] -->
S

<!-- b000438 | prose | pages [11] -->


<!-- b000439 | prose | pages [11] -->
L

<!-- b000440 | prose | pages [11] -->


<!-- b000441 | prose | pages [11] -->
i

<!-- b000442 | prose | pages [11] -->
2

<!-- b000443 | prose | pages [11] -->
i

<!-- b000444 | prose | pages [11] -->


<!-- b000445 | prose | pages [11] -->


<!-- b000446 | prose | pages [11] -->
I

<!-- b000447 | prose | pages [11] -->


<!-- b000448 | prose | pages [11] -->


<!-- b000449 | prose | pages [11] -->
S

<!-- b000450 | prose | pages [11] -->
ij

<!-- b000451 | prose | pages [11] -->


<!-- b000452 | prose | pages [11] -->
1

<!-- b000453 | prose | pages [11] -->
i

<!-- b000454 | prose | pages [11] -->


<!-- b000455 | prose | pages [11] -->
l

<!-- b000456 | prose | pages [11] -->


<!-- b000457 | prose | pages [11] -->


<!-- b000458 | prose | pages [11] -->
i

<!-- b000459 | prose | pages [11] -->
t

<!-- b000460 | prose | pages [11] -->


<!-- b000461 | prose | pages [11] -->


<!-- b000462 | prose | pages [11] -->
i

<!-- b000463 | prose | pages [11] -->


<!-- b000464 | prose | pages [11] -->
is:

<!-- b000465 | prose | pages [11] -->
' ' ' ( )

<!-- b000466 | prose | pages [11] -->
l l L L

<!-- b000467 | prose | pages [11] -->
     1 1 2

<!-- b000468 | prose | pages [11] -->
i i f i

<!-- b000469 | prose | pages [11] -->
v

<!-- b000470 | prose | pages [11] -->
(11)

<!-- b000471 | prose | pages [11] -->
is:

<!-- b000472 | prose | pages [11] -->
   max it (12)

<!-- b000473 | prose | pages [11] -->
' ' ( )

<!-- b000474 | prose | pages [11] -->
l L L

<!-- b000475 | prose | pages [11] -->
   

<!-- b000476 | prose | pages [11] -->
2

<!-- b000477 | prose | pages [11] -->
i i i f i

<!-- b000478 | prose | pages [11] -->
v

<!-- b000479 | prose | pages [11] -->
( )1

<!-- b000480 | prose | pages [11] -->
d d S e

<!-- b000481 | prose | pages [11] -->
 

<!-- b000482 | prose | pages [11] -->
2 2 2

<!-- b000483 | prose | pages [11] -->
i

<!-- b000484 | prose | pages [11] -->
v

<!-- b000485 | prose | pages [11] -->
2 01

<!-- b000486 | prose | pages [11] -->
S S

<!-- b000487 | prose | pages [11] -->
  

<!-- b000488 | prose | pages [11] -->
'

<!-- b000489 | prose | pages [11] -->
L L L l

<!-- b000490 | prose | pages [11] -->
 

<!-- b000491 | prose | pages [11] -->
2

<!-- b000492 | prose | pages [11] -->
f f i j

<!-- b000493 | prose | pages [11] -->
v

<!-- b000494 | prose | pages [11] -->
(13) For the five floors model, when the visitors on the 2nd floor are evacuating, the visitors on

<!-- b000495 | prose | pages [11] -->
9 9

<!-- b000496 | furniture | pages [12] -->
Team # 1922074

<!-- b000497 | furniture | pages [12] -->
Page

<!-- b000498 | furniture | pages [12] -->
of 29

<!-- b000499 | furniture | pages [12] -->
10

<!-- b000500 | prose | pages [12] -->
the 1st basement, 0th, and 1st floor may be stuck on the stairs and not evacuated. So, the time dt of congestion is:

<!-- b000501 | prose | pages [12] -->
L

<!-- b000502 | prose | pages [12] -->
1

<!-- b000503 | prose | pages [12] -->


<!-- b000504 | prose | pages [12] -->
t

<!-- b000505 | prose | pages [12] -->


<!-- b000506 | prose | pages [12] -->
d

<!-- b000507 | prose | pages [12] -->
1

<!-- b000508 | prose | pages [12] -->
j

<!-- b000509 | prose | pages [12] -->
 

<!-- b000510 | prose | pages [12] -->
' ' ' ( 2)

<!-- b000511 | prose | pages [12] -->
l l L L

<!-- b000512 | prose | pages [12] -->
   

<!-- b000513 | prose | pages [12] -->
ij ij i i f i

<!-- b000514 | prose | pages [12] -->
(14)

<!-- b000515 | prose | pages [12] -->
v

<!-- b000516 | prose | pages [12] -->
There are three exits on the 2nd basement, and the Carrousel du Louvre entrance and the Passage Richelieu entrance pass through the same channel, so they can regard as one large exit. The entrance to the pyramid requires a stairway on the 2nd basement, which is the same length as the other two exit channels. As a result, three exits can be equivalent to a 'n of people passing through the new exit is the sum of the three new exit. The number exits. The evacuation time of five floors model

<!-- b000517 | prose | pages [12] -->
min T 5 

<!-- b000518 | prose | pages [12] -->
'

<!-- b000519 | prose | pages [12] -->
L

<!-- b000520 | prose | pages [12] -->


<!-- b000521 | prose | pages [12] -->


<!-- b000522 | prose | pages [12] -->
1

<!-- b000523 | prose | pages [12] -->


<!-- b000524 | prose | pages [12] -->
ij

<!-- b000525 | prose | pages [12] -->
t

<!-- b000526 | prose | pages [12] -->


<!-- b000527 | prose | pages [12] -->


<!-- b000528 | prose | pages [12] -->
d

<!-- b000529 | prose | pages [12] -->


<!-- b000530 | prose | pages [12] -->
1

<!-- b000531 | prose | pages [12] -->
j

<!-- b000532 | prose | pages [12] -->
 

<!-- b000533 | prose | pages [12] -->
S

<!-- b000534 | prose | pages [12] -->


<!-- b000535 | prose | pages [12] -->
L

<!-- b000536 | prose | pages [12] -->


<!-- b000537 | prose | pages [12] -->
2

<!-- b000538 | prose | pages [12] -->
i

<!-- b000539 | prose | pages [12] -->


<!-- b000540 | prose | pages [12] -->
2

<!-- b000541 | prose | pages [12] -->
i

<!-- b000542 | prose | pages [12] -->


<!-- b000543 | prose | pages [12] -->
I

<!-- b000544 | prose | pages [12] -->


<!-- b000545 | prose | pages [12] -->


<!-- b000546 | prose | pages [12] -->
S

<!-- b000547 | prose | pages [12] -->
ij

<!-- b000548 | prose | pages [12] -->


<!-- b000549 | prose | pages [12] -->
1

<!-- b000550 | prose | pages [12] -->
i

<!-- b000551 | prose | pages [12] -->


<!-- b000552 | prose | pages [12] -->


<!-- b000553 | prose | pages [12] -->
l

<!-- b000554 | prose | pages [12] -->


<!-- b000555 | prose | pages [12] -->
i

<!-- b000556 | prose | pages [12] -->
t

<!-- b000557 | prose | pages [12] -->


<!-- b000558 | prose | pages [12] -->


<!-- b000559 | prose | pages [12] -->
i

<!-- b000560 | prose | pages [12] -->


<!-- b000561 | prose | pages [12] -->
T is: 5

<!-- b000562 | prose | pages [12] -->
   max it (15)

<!-- b000563 | prose | pages [12] -->
' ' ( )

<!-- b000564 | prose | pages [12] -->
l l l L L

<!-- b000565 | prose | pages [12] -->
   

<!-- b000566 | prose | pages [12] -->
2

<!-- b000567 | prose | pages [12] -->
i i i f i

<!-- b000568 | prose | pages [12] -->
v

<!-- b000569 | prose | pages [12] -->
( )1

<!-- b000570 | prose | pages [12] -->
d d S e

<!-- b000571 | prose | pages [12] -->
 

<!-- b000572 | prose | pages [12] -->
2

<!-- b000573 | prose | pages [12] -->
i

<!-- b000574 | prose | pages [12] -->
v

<!-- b000575 | prose | pages [12] -->
2 01

<!-- b000576 | prose | pages [12] -->
S S

<!-- b000577 | prose | pages [12] -->
  

<!-- b000578 | prose | pages [12] -->
'

<!-- b000579 | prose | pages [12] -->
L L L l

<!-- b000580 | prose | pages [12] -->
 

<!-- b000581 | prose | pages [12] -->
2

<!-- b000582 | prose | pages [12] -->
f f i j

<!-- b000583 | prose | pages [12] -->
v

<!-- b000584 | prose | pages [12] -->
10 t s 0  According to the investigation, we can get the reaction time

<!-- b000585 | prose | pages [12] -->
T Finally, the evacuation time : min

<!-- b000586 | prose | pages [12] -->
.

<!-- b000587 | prose | pages [12] -->
max{ T  min , } T T t  (16) 3 5 0

<!-- b000588 | prose | pages [12] -->
As we can see from the Figure 2, the number of visitors at 11:30 am on Monday, Thursday, Saturday and Sunday is the highest. It’s about 10,380. We substitute it into the time model T . We use the python language for programming 3T and calculate the value of and 5

<!-- b000589 | prose | pages [12] -->
calculations (see the appendix for specific code). The result is:

<!-- b000590 | prose | pages [12] -->
417.2 s T 3 

<!-- b000591 | prose | pages [12] -->
T

<!-- b000592 | prose | pages [12] -->
281 8. T 5  , , s

<!-- b000593 | prose | pages [12] -->
is 417.2s, about 7 minutes, when the number of visitors The shortest evacuation time min is the largest.

<!-- b000594 | prose | pages [12] -->
According to the information, the best evacuation time for different emergencies is different, but the maximum can not exceed 15 minutes. The shortest evacuation time obtained by the algorithm is realistic and short. Therefore, our model works well.

<!-- b000595 | heading | pages [12] -->
3.4 Emergency personnel

<!-- b000596 | prose | pages [12] -->
When there is an emergency in X area, emergency personnel is required to enter the building as soon as possible, that is, they need to reach the X area through some entrance quickly. The visitors in X area have to escape from there quickly, that is, to reach an exit as soon as possible. However, emergency personnel and visitors are prone to congestion and collisions on stairs and channels. The width of the channel is much larger than the stairs, and the main crowding and collisions will occur at the stairs, where crowding and collisions

<!-- b000597 | prose | pages [12] -->
10 10

<!-- b000598 | furniture | pages [13] -->
Team # 1922074

<!-- b000599 | furniture | pages [13] -->
Page

<!-- b000600 | furniture | pages [13] -->
of 29

<!-- b000601 | furniture | pages [13] -->
11

<!-- b000602 | prose | pages [13] -->
are neglected in the channel. Therefore, the best strategy is that the emergency personnel and visitors do not use the same stairs at the same time, that is, the emergency personnel need to use the stairs without visitors at that moment to avoid congestion. If seal off the original exit and only allow the emergency personnel to enter, it will greatly increase the evacuation time and cause danger. The best way is to open one of other exits for emergency personnel, and visitors still evacuate from the four main entrances.

<!-- b000603 | prose | pages [13] -->
( , G N R We think of the Louvre as a topology t R ( ( )) t t changing over time where N is the node is the route set that changes over time. The stairway, the various exhibition areas set, and the entrances are nodes. At the same time, we think of the emergency personnel as a node whose position move with time. Both the stairs and the channels are regarded as routes. The weight of the route is the time required to pass the stairs when the walking 2 / . If there are other visitors on a certain staircase at time t , the weight of v m s  speed is the route is updated to the sum of the time through the stairs and the time for the stairs to be fully unblocked.We get the number of people at different time when the stairs are evacuated by calculations, and then get the time required for the stairs to be completely unblocked at different time. The part of results are show in the following table. The yellow grid means that the stairs are smooth for a while. After the blue finger, the stairs are always clear. The whole result can be seen in the Appendix 1.

<!-- b000604 | caption | pages [13] -->
Table 2. The time when stairs are evacuated completely

<!-- b000605 | prose | pages [13] -->
We use the improved Dijkstra's Algorithm to calculate the optimal route for emergency personnel to the emergency area. The specific process is as follows:

<!-- b000606 | caption | pages [13] -->
Figure 5. The flow chart of optimal route for emergency personnel

<!-- b000607 | prose | pages [13] -->
ijt , iT , and time spent on each aisle of one route is Assuming the time spent on each route is

<!-- b000608 | prose | pages [13] -->
ijt  ijt  , for a specific route, the time spent on passing staircase is

<!-- b000609 | prose | pages [13] -->
ijt  of the passing of time while will not.

<!-- b000610 | prose | pages [13] -->
will be changed because

<!-- b000611 | prose | pages [13] -->
ijt ijt consists of two parts, time consumption of going up or down stairs, time consumption of staircase congestion.

<!-- b000612 | prose | pages [13] -->


<!-- b000613 | prose | pages [13] -->
T

<!-- b000614 | prose | pages [13] -->


<!-- b000615 | prose | pages [13] -->
i

<!-- b000616 | prose | pages [13] -->
j

<!-- b000617 | prose | pages [13] -->
min( )

<!-- b000618 | prose | pages [13] -->


<!-- b000619 | prose | pages [13] -->
t t t

<!-- b000620 | prose | pages [13] -->


<!-- b000621 | prose | pages [13] -->
(17) ij ij ij

<!-- b000622 | prose | pages [13] -->
j

<!-- b000623 | prose | pages [13] -->
min( ) iT , and the route corresponds to Then the minimal time cost is iT is the shortest

<!-- b000624 | prose | pages [13] -->
11 11

<!-- b000625 | furniture | pages [14] -->
Team # 1922074

<!-- b000626 | prose | pages [14] -->
route at this moment.

<!-- b000627 | furniture | pages [14] -->
Page

<!-- b000628 | furniture | pages [14] -->
of 29

<!-- b000629 | furniture | pages [14] -->
12

<!-- b000630 | prose | pages [14] -->
For example, some emergency people now enter by a new entrance (in the southernmost of Sully, close to the staircase B3), and their destination is the room 101 on the -1F. We assume the time from the start of evacuation as T .We set T as 180 and 150, and bring them into our model. The shortest route we get is the same and showed in the following figure:

<!-- b000631 | prose | pages [14] -->
180 150 T T  

<!-- b000632 | caption | pages [14] -->
Figure 6. The shortest route A when

<!-- b000633 | prose | pages [14] -->
We set T

<!-- b000634 | prose | pages [14] -->
and

<!-- b000635 | prose | pages [14] -->
as 120 and 90, and bring them into our model. The shortest route we get is the same and showed in the following figure:

<!-- b000636 | prose | pages [14] -->
120 90 T T  

<!-- b000637 | caption | pages [14] -->
Figure 7. The shortest route B when

<!-- b000638 | prose | pages [14] -->
and

<!-- b000639 | prose | pages [14] -->
The route map is showed in the following figure:

<!-- b000640 | caption | pages [14] -->
Figure 8. The route map for route A and B

<!-- b000641 | prose | pages [14] -->
As the moving speed of emergency personnel is estimated to be 2m/s. And they won’t be blocked in staircase because of the small number. While all the staircases are unobstructed, we calculate the time cost of route A and B :

<!-- b000642 | prose | pages [14] -->
130 T  A , , 160 s s T s  B

<!-- b000643 | prose | pages [14] -->
Time for evacuation of each stairs in route A is showed in the Table 3.

<!-- b000644 | caption | pages [14] -->
Table 3. Time for evacuation of each stairs in route A

<!-- b000645 | prose | pages [14] -->
Stairs B3 A3 A1

<!-- b000646 | prose | pages [14] -->
12 12

<!-- b000647 | furniture | pages [15] -->
Team # 1922074

<!-- b000648 | prose | pages [15] -->
Time 110s

<!-- b000649 | furniture | pages [15] -->
Page

<!-- b000650 | furniture | pages [15] -->
of 29

<!-- b000651 | furniture | pages [15] -->
13

<!-- b000652 | prose | pages [15] -->
46s 172s

<!-- b000653 | prose | pages [15] -->
Time for evacuation of each stairs in route B is showed in the Table 4.

<!-- b000654 | caption | pages [15] -->
Table 4. Time for evacuation of each stairs in route B

<!-- b000655 | prose | pages [15] -->
Stairs T T B

<!-- b000656 | prose | pages [15] -->
66s Time 110s

<!-- b000657 | prose | pages [15] -->
So route A can be totally evacuated in 172s, and route B is 110s.

<!-- b000658 | prose | pages [15] -->
, route A and B 90 T  are both obstructed, and emergency people need to wait While until staircases become usable. The time cost of waiting for A is 82s and waiting for B is 20s. The totally time cost on route A is 212s, and on route B is 180s, so route B is shorter.

<!-- b000659 | prose | pages [15] -->
A 150 T  A is still obstructed. The time cost of waiting for While , route is 22s and waiting for B is 0s. The totally time cost on route A is 152s, and on route B is 160s. So route A is shorter.

<!-- b000660 | prose | pages [15] -->
, route A and B are both obstructed. The totally time cost on route A is 180 T  While 130s, and on route B is 160s. So route A is shorter.

<!-- b000661 | prose | pages [15] -->
141 T  According to the calculations, we choose the value of threshold

<!-- b000662 | heading | pages [15] -->
3.5 Potential factors

<!-- b000663 | prose | pages [15] -->
.

<!-- b000664 | prose | pages [15] -->
There are some potential factors we need to consider: diversity of visitors and other entrances visitors don’t know.

<!-- b000665 | heading | pages [15] -->
3.5.1 Diversity of visitors

<!-- b000666 | prose | pages [15] -->
• Tourist group: whether it is a group or an individual to visit the Louvre, when an emergency occurs, the most important thing to do is to quickly escape breaking up the whole into parts instead waiting for the group to gather and then evacuate which may miss the best escape time.

<!-- b000667 | prose | pages [15] -->
• Languages diversity: the languages diversity often leads some visitors to fail to understand the instructions of emergency broadcasters and evacuation personnel.In our

<!-- b000668 | prose | pages [15] -->
li to reach the stairway increases. We count the number of model, it means that the time v

<!-- b000669 | prose | pages [15] -->
tourists from all over the world in the Louvre in 2018 and get percentages of languages showed in Figure 9.

<!-- b000670 | prose | pages [15] -->
13 13

<!-- b000671 | furniture | pages [16] -->
Team # 1922074

<!-- b000672 | furniture | pages [16] -->
Page

<!-- b000673 | furniture | pages [16] -->
of 29

<!-- b000674 | furniture | pages [16] -->
14

<!-- b000675 | caption | pages [16] -->
Figure 9. The nationality distribution of visitors

<!-- b000676 | prose | pages [16] -->
Considering that most tourists are from European and American countries, we have established the following measures:

<!-- b000677 | prose | pages [16] -->
- Use English in emergency broadcasts, then broadcast them in French, Spanish, and Chinese.

<!-- b000678 | prose | pages [16] -->
- The staff mainly use English and French for evacuation guidance.

<!-- b000679 | prose | pages [16] -->
- The safety exit signs in the Louvre are marked in English and French. The legend of the emergency evacuation route map should be in English and French. The route instructions should not use words as much as possible.

<!-- b000680 | prose | pages [16] -->
• The disabled: In the Louvre, the disabled can only use disabled elevators. We still use ( , , ) G N R N  the ant colony optimization algorithm and modify the topology where is 0

<!-- b000681 | prose | pages [16] -->
R is route set. We changed the stairs in the path set R to the disabled the node set and stairs, and changed the ordinary stairway in the node set N to the disabled stairway. The nodes are dedicated elevators for disabled people. The movement speed of disabled people

<!-- b000682 | prose | pages [16] -->
'n ' 1 / v m s 1  is 10 people. Eventually, we can draw a route map . The capacity of elevators for the escape of disabled people, and Figure 10 is the escape route map on the 2nd floor.

<!-- b000683 | caption | pages [16] -->
Figure 10. The escape route map for the disabled on the 2nd floor

<!-- b000684 | heading | pages [16] -->
3.5.2 Other entrances

<!-- b000685 | prose | pages [16] -->
• Huge visitors traffic: According to the information, when the Louvre held the Da Vinci exhibition in 2012, the daily visitors amounted to three times as many as the usual. If there

<!-- b000686 | prose | pages [16] -->
14 14

<!-- b000687 | furniture | pages [17] -->
Team # 1922074

<!-- b000688 | furniture | pages [17] -->
Page

<!-- b000689 | furniture | pages [17] -->
of 29

<!-- b000690 | furniture | pages [17] -->
15

<!-- b000691 | prose | pages [17] -->
were any emergency at this time, the evacuation time would increase rapidly when only the original four main entrances open. Based on the Time Model, we study the relationship between the number of visitors and the evacuation time, and represent it by the Figure 11.

<!-- b000692 | caption | pages [17] -->
Figure 11. The relationship between number of visitors and evacuation time

<!-- b000693 | prose | pages [17] -->
The prime time for emergency evacuation is 15 minutes when the number of visitors is 28000. Therefore, it’s necessary to consider other exit points when the number of visitors is 28000. The surge in visitors is usually due to some reasons such as free ticket opening, special exhibitions and so on. The Louvre will strengthen security forces to prevent a stampede. Therefore, there is no need to worry about the safety of other exit points. What’s more, a N new route map is obtained by modifying the node set in the ant colony optimization algorithm. We find an entrance in the 338 area of the 0th floor that is closed normally.

<!-- b000694 | caption | pages [17] -->
Figure 12 is the route map of the 0th floor and the 1st floor after opening the entrance.

<!-- b000695 | caption | pages [17] -->
Figure 12. The route map after opening the entrance

<!-- b000696 | prose | pages [17] -->
After the entrance is opened, we obtain the shortest evacuation time when the number of visitors is 10380 and compared it with the original evacuation time. The result is showed in the following table.

<!-- b000697 | prose | pages [17] -->
15

<!-- b000698 | furniture | pages [18] -->
Team # 1922074

<!-- b000699 | furniture | pages [18] -->
Page

<!-- b000700 | furniture | pages [18] -->
of 29

<!-- b000701 | furniture | pages [18] -->
16

<!-- b000702 | caption | pages [18] -->
Table 5. The comparison of evacuation time

<!-- b000703 | prose | pages [18] -->
Shortest evacuation time(s) Situation

<!-- b000704 | prose | pages [18] -->
Old New 417.2 343.4

<!-- b000705 | prose | pages [18] -->
• Some entrances cannot be used. When some entrances cannot be used normally due to maintenance, the evacuation time will increase dramatically. Therefore, on the one hand, we need to open other exit points, and on the other hand, we should send security personnel to protect three main entrances and exits as soon as possible. a new route map is obtained N in the ant colony optimization algorithm. The following by modifying the node set figure is the route map of the 0th floor and the 1st floor when the Portes Des Lions entrance is closed and the entrance in 338 is open.

<!-- b000706 | caption | pages [18] -->
Table 6. The comparison of evacuation time

<!-- b000707 | prose | pages [18] -->
Shortest evacuation time(s) Situation

<!-- b000708 | prose | pages [18] -->
Old New The new route map is showed in Figure 13:

<!-- b000709 | prose | pages [18] -->
417.2 430.1

<!-- b000710 | caption | pages [18] -->
Figure 13. The new route map

<!-- b000711 | heading | pages [18] -->
3.5.3 Some potential threats

<!-- b000712 | prose | pages [18] -->
There are two consequences of potential threats:

<!-- b000713 | prose | pages [18] -->
• Some channels cannot pass. • Some staircase is not accessible.

<!-- b000714 | prose | pages [18] -->
16 16

<!-- b000715 | furniture | pages [19] -->
Team # 1922074

<!-- b000716 | furniture | pages [19] -->
Page

<!-- b000717 | furniture | pages [19] -->
of 29

<!-- b000718 | furniture | pages [19] -->
17

<!-- b000719 | prose | pages [19] -->
and route set R , then we can get the As a result, we only need to modify the node set N new evacuation map. The time required for the new evacuation can be obtained based on the new evacuation map.

<!-- b000720 | prose | pages [19] -->
Assuming that the stairs B on the 2nd floor cannot be used, we use the improved ant colony optimization algorithm to get the new escape route on the 2nd floor which is showed in the Figure 14. The evacuation time is 453.3.

<!-- b000721 | caption | pages [19] -->
Figure 14. The escape route on 2F when B cannot be used

<!-- b000722 | heading | pages [19] -->
4. Policy and procedural recommendations

<!-- b000723 | prose | pages [19] -->
We have developed corresponding policies for the Louvre:

<!-- b000724 | prose | pages [19] -->
• In daily life, the Louvre should conduct emergency drills and training for staff in the museum to improve the staff's ability to handle emergencies. Continuously improve the rules and regulations, and strengthen safety education and training.

<!-- b000725 | prose | pages [19] -->
System implementation is one of the most effective measures to regulate people's safety awareness and safety behavior. They also need regularly conduct safety study meetings to improve the safety awareness of responsibility.

<!-- b000726 | prose | pages [19] -->
security personnel and strengthen work

<!-- b000727 | prose | pages [19] -->
• The Louvre also should make the evacuation route map based on the best evacuation route derived from our model. Evacuate routes are marked at various entrances and exits, and evacuation route maps are added to the Louvre map. It is helpful for tourists to understand the evacuation route in advance, and be able to quickly escape according to the evacuation route in case of emergency.

<!-- b000728 | prose | pages [19] -->
• The Louvre should keep the stairs and channels open during normal time, especially the key stairs and channels. It is good for tourists to escape quickly in the event of an emergency.

<!-- b000729 | prose | pages [19] -->
When an emergency happen, first of all, visitors should be informed through the • radio in time to quickly escape along the evacuation route; at the same time, start the corresponding emergency plan according to the current situation. The staff should correctly guide the tourists to the channels and exits. Considering the language diversity of visitors, the staff at least have to fully grasp the English and French. Besides, they

<!-- b000730 | prose | pages [19] -->
17 17

<!-- b000731 | furniture | pages [20] -->
Team # 1922074

<!-- b000732 | furniture | pages [20] -->
Page

<!-- b000733 | furniture | pages [20] -->
of 29

<!-- b000734 | furniture | pages [20] -->
18

<!-- b000735 | prose | pages [20] -->
also need to keep order to avoid crowding and stamping.

<!-- b000736 | prose | pages [20] -->
• In the optimal evacuation route got by our model, some stairs are closed, some stairs are only allowed up or down. Therefore, when an emergency happens, the staff is required to place a direction sign next to the corresponding stairs and promptly guide the visitors who are on the wrong stairs to the correct stairs.

<!-- b000737 | prose | pages [20] -->
• For other factors, such as the diversity of visitors, potential threats, whether other entrances are used and so on. The Louvre needs to modify the topology in the ant colony optimization algorithm based on our model, and use the ant colony optimization algorithm to find the optimal evacuation route based on it. The Louvre also needs to develop relevant contingency plans for these factors so that they can respond as quickly as possible.

<!-- b000738 | prose | pages [20] -->
The optimal route for emergency personnel to reach the emergency area can be • calculated according to our model. The Louvre needs to set the time for the emergency personnel to arrive at the Louvre, the location of the emergency area, and the entry of emergency personnel into the Louvre. Different routes make it easy for emergency personnel to reach the area where an emergency occurs.

<!-- b000739 | heading | pages [20] -->
5. The VEE model for other large structures

<!-- b000740 | prose | pages [20] -->
For other large, crowded structures, we still can use the improved ant colony optimization algorithm to get the optimal evacuation route. First, it is necessary to calculate basic data such as the number, length, and width of stairways, passages, and areas of each floor in the structure. It is also necessary to count the specific number of people in each area of each floor at different time so that the optimal evacuation route can be obtained according to the improved ant colony optimization algorithm.

<!-- b000741 | prose | pages [20] -->
At the same time, other factors still need to be considered. For example, the diversity of people in the building, various potential threats (such as some stairs can not be used in an emergency). For these factors, the topology should be modified and updated. After that, we can use ant colony optimization algorithm to find the optimal evacuation route.

<!-- b000742 | prose | pages [20] -->
It is also necessary to consider how the emergency personnel enter the structure. The entry of emergency personnel is different from the evacuation of people inside the structure. On the one hand, the number of emergency personnel is usually not particularly large, and it is usually not necessary to consider whether or not they will be congested. On the other hand, emergency personnel usually need to reach the high floors from the lower floors, avoiding collisions and crowding with people evacuating from the high floors to the lower floors. Therefore, we can use the Dijkstra algorithm where the weight of the route will be change over time. The change value is the time at which the stairs need to be completely unblocked at the current time. Then, we can calculate the optimal evacuation route. In addition, in response to these factors, it is necessary to prepare sufficient emergency plans in advance so that they can respond promptly when corresponding situations occur.

<!-- b000743 | prose | pages [20] -->
18

<!-- b000744 | furniture | pages [21] -->
Team # 1922074

<!-- b000745 | heading | pages [21] -->
6. Sensitivity Analysis

<!-- b000746 | furniture | pages [21] -->
Page

<!-- b000747 | furniture | pages [21] -->
of 29

<!-- b000748 | furniture | pages [21] -->
19

<!-- b000749 | prose | pages [21] -->
There must be a lot of “What if” scenarios happen when the When performing evacuation plans. “What if” scenarios can be reflected in the fluctuation of important parameter of our model.Therefore, we will list two important “What if” scenarios and do sensitive analysis at the same time.

<!-- b000750 | prose | pages [21] -->
• The fluctuation of the speed of tourists. In the actual evacuation, the speed of the tourists will not be exactly 1m/s, and will fluctuate up and down on the basis of 1m/s. We 2.0 adjust the visitor speed v to v  , and the results are shown in the Figure 15.

<!-- b000751 | caption | pages [21] -->
Figure 15. Change the value of speed

<!-- b000752 | prose | pages [21] -->
It can be seen that the effect of speed on evacuation time is very large. Therefore, in the actual evacuation process, the staff should guide the tourists to run as fast as possible while paying attention to safety.

<!-- b000753 | prose | pages [21] -->
• The reduction of the number of people passing through the stairs. In the actual evacuation, the number of people who can pass the stairs at one time is not necessarily the largest, and may be reduced because the stairway is too crowded and the tourists do not 4 3 2 fn fn fn    obey the order. We can adjust the number of stairs by the result is as shown in the Figure 16.

<!-- b000754 | prose | pages [21] -->
and and , and

<!-- b000755 | caption | pages [21] -->
Figure 16. Change the value of the number of people

<!-- b000756 | prose | pages [21] -->
It can be seen that the reduction in the number of people passing through the stairs has a great influence on the evacuation time. Therefore, in the actual evacuation process, it is necessary to ensure the orderly passage of the stairway, and maximize the number of people who can pass the stairs.

<!-- b000757 | prose | pages [21] -->
19 19

<!-- b000758 | furniture | pages [22] -->
Team # 1922074

<!-- b000759 | furniture | pages [22] -->
Page

<!-- b000760 | furniture | pages [22] -->
of 29

<!-- b000761 | furniture | pages [22] -->
20

<!-- b000762 | heading | pages [22] -->
7. Strengths and Weaknesses

<!-- b000763 | heading | pages [22] -->
7.1 Strengths

<!-- b000764 | prose | pages [22] -->
Our model is an adaptive model, that can be designed to address a broad set of • considerations and various types of potential threats.

<!-- b000765 | prose | pages [22] -->
We improved the ant colony optimization algorithm so that it can be used for the • evacuation planning of large-scale crowded structures.

<!-- b000766 | prose | pages [22] -->
• We have improved the Dijkstra algorithm so that the route of emergency personnel to the emergency area is immediacy.

<!-- b000767 | heading | pages [22] -->
7.2 Weaknesses

<!-- b000768 | prose | pages [22] -->
• For our model, to simplify the calculation, we simply assume the thickness and width of each visitor and the running speed. In fact, we found through information that in 2018, about 10% of tourists are children, and 13% of tourists are elderly people, accounting for about a quarter of the total, and the number is still relatively large.

<!-- b000769 | prose | pages [22] -->
• We simply think that the number of visitors is evenly distributed, except for the area of the treasures of the three major town halls. In fact, the number of visitors in different exhibition areas is inevitably different, and will vary with the size of the exhibition area, the popularity of the exhibition area, and the time.

<!-- b000770 | prose | pages [22] -->
For some stairs, we are unable to obtain the corresponding data. This may affect the • actual evacuation time.

<!-- b000771 | heading | pages [22] -->
8. Conclusion

<!-- b000772 | prose | pages [22] -->
In our work, we make the VEE model to design the evacuation plan. At first, we get different numbers of people at different times of the day according to the current queuing time displayed by the APP "Affluences". Then, we use the improved ant colony optimization algorithm to get the optimal evacuation route, and establish the Time Model to get the shortest evacuation time when the number of people is the largest. Meanwhile, we use the improved Dijkstra algorithm to for emergency personnel to reach the emergency area. We also consider other potential factors. In addition, we propose policy and procedural recommendations for emergency management of the Louvre, and discuss how our model could adapt and implement our models for other large, crowded structures. Finally, we performed sensitivity analysis on two important parameters: the number of people passing through the stairs and the speed.

<!-- b000773 | heading | pages [22] -->
9. References

<!-- b000774 | references | pages [22] -->
[1] Reporters, Telegraph. “Terror Attacks in France: From Toulouse to the Louvre.” The

<!-- b000775 | references | pages [22] -->
Telegraph, Telegraph Media Group, 24 June 2018, www.telegraph.co.uk/news/0/terror-

<!-- b000776 | references | pages [22] -->
attacks-france-toulouse-louvre/.

<!-- b000777 | references | pages [22] -->
20

<!-- b000778 | furniture | pages [23] -->
Team # 1922074

<!-- b000779 | furniture | pages [23] -->
Page

<!-- b000780 | furniture | pages [23] -->
of 29

<!-- b000781 | furniture | pages [23] -->
21

<!-- b000782 | references | pages [23] -->
[2] "8.1 Million Visitors to the Louvre in 2017." Louvre Press Release, 25 Jan. 2018,

<!-- b000783 | references | pages [23] -->
presse.louvre.fr/8-1-million-visitors-to-the-louvre-in-2017/.

<!-- b000784 | references | pages [23] -->
[3] “Interactive Floor Plans.” Louvre - Interactive Floor Plans | Louvre Museum | Paris, 30

<!-- b000785 | references | pages [23] -->
June 2016, ww.louvre.fr/en/plan.

<!-- b000786 | references | pages [23] -->
[4] "Pyramid" Project Launch –

<!-- b000787 | references | pages [23] -->
The Musée du Louvre is improving visitor reception

<!-- b000788 | references | pages [23] -->
(2014-2016)."Louvre Press Kit, 18 Sept. 2014,

<!-- b000789 | references | pages [23] -->
www.louvre.fr/sites/default/files/dp_pyramide%2028102014_en.pdf.

<!-- b000790 | references | pages [23] -->
Project - Improving Visitor Reception (2014-2016). ”

<!-- b000791 | references | pages [23] -->
[5] “ The ‘ Pyramid ’

<!-- b000792 | references | pages [23] -->
Louvre Press

<!-- b000793 | references | pages [23] -->
Release, 6 July 2016, presse.louvre.fr/the-pyramid-project/.

<!-- b000794 | references | pages [23] -->
[6] QIdong Du,Rouxiang Chen,Aijun Xu.Optimization of Evacuation Route Selection in

<!-- b000795 | references | pages [23] -->
Flue Gas Based on ant colony optimization algorithms[J].Computer Era,2018,No. 2:18-21

<!-- b000796 | references | pages [23] -->
[7] Yanfang Zhang,Jing Yuan,Fuchang Wang,Yibin Zhao,Yong ’ an Zhao.Mathematical

<!-- b000797 | references | pages [23] -->
densely

<!-- b000798 | references | pages [23] -->
model

<!-- b000799 | references | pages [23] -->
of

<!-- b000800 | references | pages [23] -->
emergency

<!-- b000801 | references | pages [23] -->
evacuation

<!-- b000802 | references | pages [23] -->
in

<!-- b000803 | references | pages [23] -->
populated

<!-- b000804 | references | pages [23] -->
areas

<!-- b000805 | references | pages [23] -->
and

<!-- b000806 | references | pages [23] -->
its

<!-- b000807 | references | pages [23] -->
optimal

<!-- b000808 | references | pages [23] -->
solution[J].MATHEMATICS IN PRACTICE AND THEORY,2009,No.39(24):48-52

<!-- b000809 | references | pages [23] -->
10.

<!-- b000810 | heading | pages [23] -->
Appendix

<!-- b000811 | prose | pages [23] -->
1. Table: the time when stairs are evacuated completely

<!-- b000812 | prose | pages [23] -->
21 21

<!-- b000813 | furniture | pages [24] -->
Team # 1922074

<!-- b000814 | furniture | pages [24] -->
Page

<!-- b000815 | furniture | pages [24] -->
of 29

<!-- b000816 | furniture | pages [24] -->
22

<!-- b000817 | prose | pages [24] -->
2. ETxls_time1.py import math import xlwt

<!-- b000818 | prose | pages [24] -->
total = 8000 floorweight = [1, 3, 8, 12, 6] floors = [] sum = 0 d = 0.5 e = 0.1 nf = 4 v = 1 aimstairs = [] aimadd = []

<!-- b000819 | prose | pages [24] -->
for f in floorweight:

<!-- b000820 | prose | pages [24] -->
sum += f

<!-- b000821 | prose | pages [24] -->
scost = 10/v print(scost)

<!-- b000822 | prose | pages [24] -->
book = xlwt.Workbook() sheet = book.add_sheet('Result')

<!-- b000823 | prose | pages [24] -->
class stair:

<!-- b000824 | prose | pages [24] -->
def __init__(self, name, fl, aim, aimfloor, num):

<!-- b000825 | prose | pages [24] -->
self.name = name self.fl = fl self.aim = aim self.aimfloor = aimfloor self.num = math.floor(num)

<!-- b000826 | prose | pages [24] -->
22

<!-- b000827 | furniture | pages [25] -->
Team # 1922074

<!-- b000828 | prose | pages [25] -->
def run(self, time):

<!-- b000829 | furniture | pages [25] -->
Page

<!-- b000830 | furniture | pages [25] -->
of 29

<!-- b000831 | furniture | pages [25] -->
23

<!-- b000832 | prose | pages [25] -->
if time == self.cleartime() and self.aimfloor != -1:

<!-- b000833 | prose | pages [25] -->
ss = floors[s.aimfloor].findstair(s.aim) aimstairs.append(ss) aimadd.append(s.num) self.num = math.floor(self.num - (time*nf*v)/(d+e)) if self.num < 0:

<!-- b000834 | prose | pages [25] -->
self.num = 0

<!-- b000835 | prose | pages [25] -->
def cleartime(self):

<!-- b000836 | prose | pages [25] -->
if (self.num*d + self.num*e)/nf >= 0:

<!-- b000837 | prose | pages [25] -->
return (self.num*d + self.num*e)/(nf*v) else:

<!-- b000838 | prose | pages [25] -->
return 0

<!-- b000839 | prose | pages [25] -->
class floor:

<!-- b000840 | prose | pages [25] -->
def __init__(self, fl, sname, saim, saimfloor, sweight):

<!-- b000841 | prose | pages [25] -->
self.name = fl self.num = total/sum*floorweight[fl] self.stairs = [] n = 0 for t in sweight:

<!-- b000842 | prose | pages [25] -->
n = n + t for i in range(sname.__len__()):

<!-- b000843 | prose | pages [25] -->
self.stairs.append(stair(sname[i], self.num*sweight[i]/n))

<!-- b000844 | prose | pages [25] -->
def findstair(self, name):

<!-- b000845 | prose | pages [25] -->
for s in self.stairs:

<!-- b000846 | prose | pages [25] -->
if s.name == name:

<!-- b000847 | prose | pages [25] -->
return s return None

<!-- b000848 | prose | pages [25] -->
def min(self):

<!-- b000849 | prose | pages [25] -->
result = None time = 1000000

<!-- b000850 | prose | pages [25] -->
for s in self.stairs:

<!-- b000851 | prose | pages [25] -->
fl, saim[i], saimfloor[i],

<!-- b000852 | prose | pages [25] -->
if s.cleartime()>0 and s.cleartime()<time:

<!-- b000853 | prose | pages [25] -->
result = s time = s.cleartime() return result

<!-- b000854 | prose | pages [25] -->
23 23

<!-- b000855 | furniture | pages [26] -->
Team # 1922074

<!-- b000856 | furniture | pages [26] -->
Page

<!-- b000857 | furniture | pages [26] -->
of 29

<!-- b000858 | furniture | pages [26] -->
24

<!-- b000859 | prose | pages [26] -->
def run(self, time):

<!-- b000860 | prose | pages [26] -->
for s in self.stairs:

<!-- b000861 | prose | pages [26] -->
s.run(time)

<!-- b000862 | prose | pages [26] -->
if __name__ == '__main__':

<!-- b000863 | prose | pages [26] -->
sn0 = ['E'] sw0 = [1] sa0 = ['esc'] saf0 = [-1]

<!-- b000864 | prose | pages [26] -->
f = floor(0, sn0, sa0, saf0, sw0) floors.append(f)

<!-- b000865 | prose | pages [26] -->
sn1 = ['A1', 'A2', 'A3'] sw1 = [3, 4, 3] sa1 = ['E', 'E', 'E'] saf1 = [0, 0, 0] f = floor(1, sn1, sa1, saf1, sw1) floors.append(f)

<!-- b000866 | prose | pages [26] -->
sn2 = ['B1', 'B2', 'B', 'B3'] sw2 = [2,2,2,2] sa2 = ['A1','A1','A1','A3'] saf2 = [1,1,1,1] f = floor(2, sn2, sa2, saf2, sw2) floors.append(f)

<!-- b000867 | prose | pages [26] -->
sn3 = ['E1','E2','E3','B'] sw3 = [3,1,3,3] sa3 = ['B1','B','B2','B'] saf3 = [2,2,2,2] f = floor(3, sn3, sa3, saf3, sw3) floors.append(f)

<!-- b000868 | prose | pages [26] -->
sn4 = ['E1','B','B4'] sw4 = [4,4,2] sa4 = ['E1','B','F'] saf4 = [3,3,3] f = floor(4, sn4, sa4, saf4, sw4) floors.append(f) totaltime = 0

<!-- b000869 | prose | pages [26] -->
24

<!-- b000870 | furniture | pages [27] -->
Team # 1922074

<!-- b000871 | furniture | pages [27] -->
Page

<!-- b000872 | furniture | pages [27] -->
of 29

<!-- b000873 | furniture | pages [27] -->
25

<!-- b000874 | prose | pages [27] -->
col = 0 while True:

<!-- b000875 | prose | pages [27] -->
aimstairs.clear() aimadd.clear() time = 1000000 s = None row = 0

<!-- b000876 | prose | pages [27] -->
sheet.write(col, row, 'total') sheet.write(col+1, row, totaltime)

<!-- b000877 | prose | pages [27] -->
for i in range(5):

<!-- b000878 | prose | pages [27] -->
stas = floors[i].stairs for sta in stas:

<!-- b000879 | prose | pages [27] -->
row += 1 str = sta.name + ' ' + sta.fl.__str__() num = sta.cleartime() if num <0:

<!-- b000880 | prose | pages [27] -->
num = 0 sheet.write(col, row, str) sheet.write(col+1, row, num)

<!-- b000881 | prose | pages [27] -->
for i in range(5):

<!-- b000882 | prose | pages [27] -->
ss = floors[i].min() if ss is not None and 0 < ss.cleartime() < time:

<!-- b000883 | prose | pages [27] -->
time = ss.cleartime() s = ss

<!-- b000884 | prose | pages [27] -->
if s is None:

<!-- b000885 | prose | pages [27] -->
break

<!-- b000886 | prose | pages [27] -->
totaltime = totaltime + time + scost for i in range(5):

<!-- b000887 | prose | pages [27] -->
floors[i].run(time)

<!-- b000888 | prose | pages [27] -->
for i in range(aimstairs.__len__()):

<!-- b000889 | prose | pages [27] -->
aimstairs[i].num = aimstairs[i].num + aimadd[i] print(aimstairs[i].name)

<!-- b000890 | prose | pages [27] -->
col += 2

<!-- b000891 | prose | pages [27] -->
print(totaltime)

<!-- b000892 | prose | pages [27] -->
book.save('G:/MathModeling/result_Five.xls')

<!-- b000893 | prose | pages [27] -->
25

<!-- b000894 | furniture | pages [28] -->
Team # 1922074

<!-- b000895 | furniture | pages [28] -->
Page

<!-- b000896 | furniture | pages [28] -->
of 29

<!-- b000897 | furniture | pages [28] -->
26

<!-- b000898 | prose | pages [28] -->
3. ETxls_time2.py

<!-- b000899 | prose | pages [28] -->
import math import xlwt

<!-- b000900 | prose | pages [28] -->
total = 4000 floorweight = [8, 12, 6] floors = [] sum = 0 d = 0.5 e = 0.1 nf = 6 v = 1

<!-- b000901 | prose | pages [28] -->
aimstairs = [] aimadd = []

<!-- b000902 | prose | pages [28] -->
for f in floorweight:

<!-- b000903 | prose | pages [28] -->
sum += f

<!-- b000904 | prose | pages [28] -->
scost = 10/v

<!-- b000905 | prose | pages [28] -->
book = xlwt.Workbook() sheet = book.add_sheet('Result')

<!-- b000906 | prose | pages [28] -->
class stair:

<!-- b000907 | prose | pages [28] -->
def __init__(self, name, fl, aim, aimfloor, num):

<!-- b000908 | prose | pages [28] -->
self.name = name self.fl = fl self.aim = aim self.aimfloor = aimfloor self.num = math.floor(num)

<!-- b000909 | prose | pages [28] -->
def run(self, time):

<!-- b000910 | prose | pages [28] -->
if time == self.cleartime() and self.aimfloor != -1:

<!-- b000911 | prose | pages [28] -->
ss = floors[s.aimfloor].findstair(s.aim) aimstairs.append(ss) aimadd.append(s.num) self.num = math.floor(self.num - (time*nf*v)/(d+e)) if self.num < 0:

<!-- b000912 | prose | pages [28] -->
self.num = 0

<!-- b000913 | prose | pages [28] -->
def cleartime(self):

<!-- b000914 | prose | pages [28] -->
if (self.num*d + self.num*e)/nf >= 0:

<!-- b000915 | prose | pages [28] -->
return (self.num*d + self.num*e)/(nf*v);

<!-- b000916 | prose | pages [28] -->
26

<!-- b000917 | furniture | pages [29] -->
Team # 1922074

<!-- b000918 | prose | pages [29] -->
else:

<!-- b000919 | prose | pages [29] -->
return 0

<!-- b000920 | prose | pages [29] -->
class floor:

<!-- b000921 | furniture | pages [29] -->
Page

<!-- b000922 | furniture | pages [29] -->
of 29

<!-- b000923 | furniture | pages [29] -->
27

<!-- b000924 | prose | pages [29] -->
def __init__(self, fl, sname, saim, saimfloor, sweight):

<!-- b000925 | prose | pages [29] -->
self.name = fl self.num = total/sum*floorweight[fl] self.stairs = [] n = 0 for t in sweight:

<!-- b000926 | prose | pages [29] -->
n = n + t for i in range(sname.__len__()):

<!-- b000927 | prose | pages [29] -->
self.stairs.append(stair(sname[i], self.num*sweight[i]/n))

<!-- b000928 | prose | pages [29] -->
def findstair(self, name):

<!-- b000929 | prose | pages [29] -->
for s in self.stairs:

<!-- b000930 | prose | pages [29] -->
if s.name == name:

<!-- b000931 | prose | pages [29] -->
return s return None

<!-- b000932 | prose | pages [29] -->
def min(self):

<!-- b000933 | prose | pages [29] -->
result = None time = 1000000

<!-- b000934 | prose | pages [29] -->
for s in self.stairs:

<!-- b000935 | prose | pages [29] -->
fl, saim[i], saimfloor[i],

<!-- b000936 | prose | pages [29] -->
if s.cleartime()>0 and s.cleartime()<time:

<!-- b000937 | prose | pages [29] -->
result = s time = s.cleartime() return result

<!-- b000938 | prose | pages [29] -->
def run(self, time):

<!-- b000939 | prose | pages [29] -->
for s in self.stairs:

<!-- b000940 | prose | pages [29] -->
s.run(time)

<!-- b000941 | prose | pages [29] -->
if __name__ == '__main__':

<!-- b000942 | prose | pages [29] -->
sn0 = ['B4', 'E', 'T1', 'T2', 'T3', 'T4'] sw0 = [1,4,6,1,1,1] sa0 = ['F','esc','F','F','F','F'] saf0 = [1,-1,1,1,1,1] f = floor(0, sn0, sa0, saf0, sw0)

<!-- b000943 | prose | pages [29] -->
27 27

<!-- b000944 | furniture | pages [30] -->
Team # 1922074

<!-- b000945 | furniture | pages [30] -->
Page

<!-- b000946 | furniture | pages [30] -->
of 29

<!-- b000947 | furniture | pages [30] -->
28

<!-- b000948 | prose | pages [30] -->
floors.append(f)

<!-- b000949 | prose | pages [30] -->
sn1 = ['F'] sw1 = [20] sa1 = ['E'] saf1 = [0] f = floor(1, sn1, sa1, saf1, sw1) floors.append(f)

<!-- b000950 | prose | pages [30] -->
sn2 = ['T3','T','T4'] sw2 = [1,1,1] sa2 = ['F','F','F'] saf2 = [1,1,1] f = floor(2, sn2, sa2, saf2, sw2) floors.append(f) totaltime = 0

<!-- b000951 | prose | pages [30] -->
col = 0 while True:

<!-- b000952 | prose | pages [30] -->
aimstairs.clear() aimadd.clear() time = 1000000 s = None row = 0

<!-- b000953 | prose | pages [30] -->
sheet.write(col, row, 'total') sheet.write(col+1, row, totaltime)

<!-- b000954 | prose | pages [30] -->
for i in range(3):

<!-- b000955 | prose | pages [30] -->
stas = floors[i].stairs for sta in stas:

<!-- b000956 | prose | pages [30] -->
row += 1 str = sta.name + ' ' + sta.fl.__str__() num = sta.cleartime() if num <0:

<!-- b000957 | prose | pages [30] -->
num = 0 sheet.write(col, row, str) sheet.write(col+1, row, num)

<!-- b000958 | prose | pages [30] -->
for i in range(3):

<!-- b000959 | prose | pages [30] -->
ss = floors[i].min() if ss is not None and 0 < ss.cleartime() < time:

<!-- b000960 | prose | pages [30] -->
time = ss.cleartime() s = ss

<!-- b000961 | prose | pages [30] -->
28

<!-- b000962 | furniture | pages [31] -->
Team # 1922074

<!-- b000963 | furniture | pages [31] -->
Page

<!-- b000964 | furniture | pages [31] -->
of 29

<!-- b000965 | furniture | pages [31] -->
29

<!-- b000966 | prose | pages [31] -->
if s is None:

<!-- b000967 | prose | pages [31] -->
break

<!-- b000968 | prose | pages [31] -->
totaltime = totaltime + time + scost for i in range(3):

<!-- b000969 | prose | pages [31] -->
floors[i].run(time)

<!-- b000970 | prose | pages [31] -->
for i in range(aimstairs.__len__()):

<!-- b000971 | prose | pages [31] -->
aimstairs[i].num = aimstairs[i].num + aimadd[i] print(aimstairs[i].name)

<!-- b000972 | prose | pages [31] -->
col += 2

<!-- b000973 | prose | pages [31] -->
print(totaltime)

<!-- b000974 | prose | pages [31] -->
book.save('G:/MathModeling/result_Three.xls')

<!-- b000975 | prose | pages [31] -->
29
