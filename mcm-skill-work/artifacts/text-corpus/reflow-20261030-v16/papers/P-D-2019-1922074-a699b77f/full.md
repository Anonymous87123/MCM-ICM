# P-D-2019-1922074-a699b77f

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000003 | front_matter | pages [1] -->
1922074

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 Problem Chosen T3 F3 T4 F4

<!-- b000005 | front_matter | pages [1] -->
D

<!-- b000006 | front_matter | pages [1] -->
2019

<!-- b000007 | heading | pages [1] -->
MCM/ICM Summary Sheet

<!-- b000008 | prose | pages [1] -->
A Model for Determining Evacuation Routes

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In 2018, the number of people in the Louvre was 10.8 million, creating a new high. At the same time, in the event of an emergency, such a large number of tourists will increase the difficulty of evacuation and raise the risk. Therefore, our goal is to design the Louvre's emergency evacuation plan to evacuate visitors from the museum and estimate the evacuation time, while also allowing emergency personnel to enter the building as quickly as possible, as well as considering other factors and potential threats.

<!-- b000011 | prose | pages [1] -->
We make the Visitor Emergency Evacuation(VEE) model to design the evacuation plan. The first model of the emergency evacuation plan is based on an improved ant colony optimization algorithm. The model transforms the entire Louvre into a topological map and influences the selection probability by setting the pheromone concentration threshold to determine the optimal evacuation route for visitors to leave from each region. We also established an evacuation time model and found that the shortest evacuation time for the largest number of visitors in the library was 417.2 s. This result indicates that our evacuation plan is reliable.

<!-- b000012 | prose | pages [1] -->
The third model uses the improved Dijkstra algorithm. The model considers the entire Louvre as a time-varying topology map to determine the route of emergency personnel to the emergency area as quickly as possible. By assuming an emergency in the 101 area of the -1F and adding a new exit near the B3 stairs of the 0F, the optimal path for the emergency personnel to reach the area and the shortest time of 130s are obtained. This result shows that our model is reliable.

<!-- b000013 | prose | pages [1] -->
We also discussed other factors that have an impact on evacuation time, such as whether to open new exports, the impact of tourist diversity, the consequences of potential threats, and so on. And we propose policy and procedural recommendations for emergency management of the Louvre . Additionally, we discuss how we can adapt and implement our models for other large, crowded structures. Then we performed sensitivity analysis on two important parameters: the number of people passing through the stairs and the speed. The results show that the changes of these two parameters will have a huge impact on the shortest evacuation time.

<!-- b000014 | keywords | pages [1] -->
Key Words: Emergency evacuation plan, Ant colony optimization algorithm,

<!-- b000015 | prose | pages [1] -->
Time model, Dijkstra algorithm, Other factors

<!-- b000016 | heading | pages [2] -->
Content

<!-- b000017 | contents | pages [2] -->
1. Introduction.....................................................................................................................................1

<!-- b000018 | contents | pages [2] -->
1.1 Background..............................................................................................................................1

<!-- b000019 | contents | pages [2] -->
1.2 Restatement of Problems...................................................................................................... 1

<!-- b000020 | contents | pages [2] -->
1.3 Our Work.................................................................................................................................2

<!-- b000021 | contents | pages [2] -->
2. Assumptions and Symbol Table.................................................................................................2

<!-- b000022 | contents | pages [2] -->
2.1 Assumptions........................................................................................................................... 2

<!-- b000023 | contents | pages [2] -->
2.2 Symbol Table..........................................................................................................................2

<!-- b000024 | contents | pages [2] -->
3. The Visitor Emergency Evacuation model................................................................................ 3

<!-- b000025 | contents | pages [2] -->
3.1 Distribution of tourists..........................................................................................................3

<!-- b000026 | contents | pages [2] -->
3.2 The evacuation route.............................................................................................................4

<!-- b000027 | contents | pages [2] -->
3.3 The evacuation time.............................................................................................................. 7

<!-- b000028 | contents | pages [2] -->
3.4 Emergency personnel......................................................................................................... 10

<!-- b000029 | contents | pages [2] -->
3.5 Potential factors................................................................................................................... 13

<!-- b000030 | contents | pages [2] -->
4. Policy and procedural recommendations................................................................................ 17

<!-- b000031 | contents | pages [2] -->
5. The VEE model for other large structures............................................................................... 18

<!-- b000032 | contents | pages [2] -->
6. Sensitivity Analysis.....................................................................................................................19

<!-- b000033 | contents | pages [2] -->
7. Strengths and Weaknesses......................................................................................................... 20

<!-- b000034 | contents | pages [2] -->
7.1 Strengths...............................................................................................................................20

<!-- b000035 | contents | pages [2] -->
7.2 Weaknesses..........................................................................................................................20

<!-- b000036 | contents | pages [2] -->
8. Conclusion.....................................................................................................................................20

<!-- b000037 | contents | pages [2] -->
9. References......................................................................................................................................21

<!-- b000038 | contents | pages [2] -->
10. Appendix......................................................................................................................................21

<!-- b000039 | furniture | pages [3] -->
Team # 1922074

<!-- b000040 | furniture | pages [3] -->
Page

<!-- b000041 | furniture | pages [3] -->
of 29

<!-- b000042 | furniture | pages [3] -->
1

<!-- b000043 | heading | pages [3] -->
1. Introduction

<!-- b000044 | heading | pages [3] -->
1.1 Background

<!-- b000045 | prose | pages [3] -->
Nowadays, urban development has entered a period of rapid growth, the city’s scale has expanded rapidly, the number of high-rise buildings and large buildings has increased, and personnel are highly intensive. The dangers and harmfulness of unconventional emergencies, such as overcrowded and trampling in open spaces and buildings, are becoming more and more serious, making the public security of the mainland face severe challenges. Due to the serious casualties caused by emergency emergencies in densely populated places, which is one of the major disasters faced by mankind. Hence, solving the problem of emergency evacuation in densely populated areas has its unprecedented significance in today’s world.

<!-- b000046 | prose | pages [3] -->
The increasing number of terror attacks in France requires a review of the emergency evacuation plans at many popular destinations. In general, the goal of evacuation is to have all occupants leave the building as quickly and safely as possible. Upon notification of a required evacuation, individuals egress to and through an optimal exit in order to empty the building as quickly as possible.

<!-- b000047 | prose | pages [3] -->
The Louvre is one of the world’s largest and most visited art museum, receiving more than 8.1 million visitors in 2017. The number of guests in the museum varies throughout the day and year, which provides challenges in planning for regular movement within the museum. The diversity of visitors -- speaking a variety of languages, groups traveling together, and disabled visitors -- makes evacuation in an emergency even more challenging. As a result, it is necessary for the Louvre to have a complete emergency evacuation plan.

<!-- b000048 | heading | pages [3] -->
1.2 Restatement of Problems

<!-- b000049 | prose | pages [3] -->
To evacuate people safely when an emergency occurs, the reasonable evacuation plans at the Louvre should be developed, while the following tasks are to be accomplished :

<!-- b000050 | prose | pages [3] -->
• The number of guests in the museum varies throughout the day and year and the diversity of visitors such as disabled visitors make evacuation in an emergency challenging. What’s more, the actual exit points that can be used is not only the four exits that the public knows. While public awareness of these exit points could provide additional strength to an evacuation plan, their use would simultaneously cause security concerns due to the lower or limited security postures at these exits compared with level of security at the four main entrances. Thus, when creating the model, we should consider carefully how to evacuate disabled visitors, when and how any additional exits might be utilized.

<!-- b000051 | prose | pages [3] -->
• The model should allow the museum leaders to explore a range of options to evacuate visitors from the museum, while also allowing emergency personnel to enter the building as quickly as possible. It is also important to identify potential bottlenecks that may limit movement towards the exits, address a broad set of considerations and various types of potential threats.

<!-- b000052 | prose | pages [3] -->
• Validate the model and discuss how the Louvre would implement it.

<!-- b000053 | prose | pages [3, 4] -->
1 • Based on the results of the work, propose policy and procedural recommendations for emergency management of the Louvre.

<!-- b000054 | furniture | pages [4] -->
Team # 1922074

<!-- b000055 | furniture | pages [4] -->
Page

<!-- b000056 | furniture | pages [4] -->
of 29

<!-- b000057 | furniture | pages [4] -->
2

<!-- b000059 | heading | pages [4] -->
1.3 Our Work

<!-- b000060 | prose | pages [4] -->
According to the current queuing time displayed by the APP "Affluences", we get different numbers of people at different times of the day. According to the improved ant colony optimization algorithm, we get the best evacuation route for tourists. Through our time model, we found the shortest time for visitors to evacuate. Based on the improved Dijkstra algorithm, we get the optimal route for emergency personnel to reach the emergency area and calculate the required time. At the same time, other potential factors were considered, such as the diversity of visitors, the opening of other entrances and exits, and uncertain potential threats.

<!-- b000061 | prose | pages [4] -->
Finally, the propose policy and procedural recommendations for emergency management of the Louvre and Additionally, discuss how we can adapt and implement our models for other large, crowded structures.

<!-- b000062 | heading | pages [4] -->
2. Assumptions and Symbol Table

<!-- b000063 | heading | pages [4] -->
2.1 Assumptions

<!-- b000064 | prose | pages [4] -->
We make the following basic assumptions in order to simplify the problem. Each of our assumptions is justified.

<!-- b000065 | prose | pages [4] -->
• Assuming that each visitor runs at the same speed.

<!-- b000066 | prose | pages [4] -->
• Assuming that the distance from chest to back of each visitor is the same. The length of the queue can be calculate directly based on the number of visitors.

<!-- b000067 | prose | pages [4] -->
• Assuming that visitors will escape from the building orderly.

<!-- b000068 | prose | pages [4] -->
• Assuming that when a block happen, tourists with low floors on the stairs are evacuated firstly.

<!-- b000069 | heading | pages [4] -->
2.2 Symbol Table

<!-- b000070 | prose | pages [4] -->
Symbol that we mainly use in the model are shown in the following table :

<!-- b000071 | caption | pages [4] -->
Table 1: Symbol Table

<!-- b000072 | heading | pages [4] -->
Symbol

<!-- b000073 | prose | pages [4] -->
Definition the number of stairs on the 2nd floor I L thi th j the length of the human chain at the stairs of the floor ij fL the length of the stairs it thi the time evacuate from the stairs

<!-- b000074 | prose | pages [4, 5] -->
2 S thi th j the number of visitors at the stairs entrance of the floor ij

<!-- b000075 | furniture | pages [5] -->
Team # 1922074

<!-- b000076 | furniture | pages [5] -->
Page

<!-- b000077 | furniture | pages [5] -->
of 29

<!-- b000078 | furniture | pages [5] -->
3

<!-- b000080 | prose | pages [5] -->
fn the space between visitors

<!-- b000081 | prose | pages [5] -->
il thi the length required to escape to the staircase T the time for evacuating all visitors min

<!-- b000082 | heading | pages [5] -->
3. The Visitor Emergency Evacuation model

<!-- b000083 | prose | pages [5] -->
In this model, when an emergency occurs, the Visitor Emergency Evacuation(VEE) model uses the improved ant colony optimization algorithm to plan evacuation routes for visitors and calculate the the minimum time for evacuation. It also uses the improved Dijkstra Algorithm to consider how emergency personnel reach the emergency area as quickly as possible and other potential factors such as other entrances that visitors don’t know, diversity of visitors and various types of potential threats.

<!-- b000084 | caption | pages [5] -->
Figure 1. The VEE Model

<!-- b000085 | prose | pages [5] -->
According to the floor plan of the Louvre, we can know that the Louvre has four main entrances, including the pyramid entrance, the Passage Richelieu entrance, the Carrousel du Louvre entrance on the 2nd floor, and the Portes Des Lions entrance on the 0th floor of the building. Due to the different locations of the open exhibition areas on each floor, we divide the Louvre into two catecories: one category has five floors(from -2F to 2F), there are three entrance located on the -2nd basement. The other category has three floors(from 0F to 2F), while the entrance is on the 0th floor. Most visitors in this area will go through the stairs to the entrance, the rest of the visitors can escape directly on the 0th floor.

<!-- b000086 | heading | pages [5] -->
3.1 Distribution of tourists

<!-- b000087 | prose | pages [5] -->
There are many exhibition areas in the Louvre. In order to facilitate the calculation, we first

<!-- b000088 | prose | pages [5, 6] -->
3 assume that the number of people in each exhibition area is equal. According to the information, there are three art treasures in the Louvre, located in 345, 703 and 711. The number of tourists in these three exhibition areas is too many. We assume that the three exhibition areas have three times as much as the number of tourists in the ordinary exhibition area. Then, the number of tourists in each exhibition area is obtained.

<!-- b000089 | furniture | pages [6] -->
Team # 1922074

<!-- b000090 | furniture | pages [6] -->
Page

<!-- b000091 | furniture | pages [6] -->
of 29

<!-- b000092 | furniture | pages [6] -->
4

<!-- b000094 | prose | pages [6] -->
The number of visitors in the Louvre varies throughout the day and year. We reverse the current number of people in the library based on the current queue time by “Affluences” and record it every 15 minutes. Then we can get the diagram between number of visitors and time. As we all know, the Louvre is open every day (except Tuesday) from 9 A.M. to 6 P.M, night opening until 9:45 P.M. on Wednesdays and Fridays. Regardless of the special events, the change of visitors’ number is showed in the Figure 2. 2(B) represents the change on Wednesdays and Fridays, 2(A) represents the change on rest days.

<!-- b000095 | caption | pages [6] -->
Figure 2. The number of visitors

<!-- b000096 | heading | pages [6] -->
3.2 The evacuation route

<!-- b000097 | prose | pages [6] -->
We cite and reference the ant colony optimization algorithm of "Mathematical model of emergency evacuation in densely populated areas and its optimal solution" [5] and improve it, and use the improved ant colony optimization algorithm to select the optimal escape route, and establish the following route model.

<!-- b000098 | heading | pages [6] -->
3.2.1 Traditional ant colony optimization algorithm

<!-- b000099 | prose | pages [6] -->
( . , ) G N R  We convert the Louvre's plan into a topology and build a mesh function , where 0 is the node set. Staircases, each of exhibitions and entrances are nodes. R is route set. N  Stairs, corridors, passages are routes. is an environmental initial pheromone 0 n  ( ) (t ) distribution. m is the total number of ants, m b i t bi  , is the number of ants of the 1 i  thi node at time t .

<!-- b000100 | prose | pages [6, 7] -->
4   ,2,1 , During the iteration of k k  NC k k m  times ( ), the ant  select the probability max according to the pheromone concentration left by the ant colony. The selection probability t thi th pk is the probability that the ant k moves from the node at time t . j node to the ij (t ) indicates the concentration of pheromone between nodes i ,  at time t . j Function ij  is pheromone heuristic factor which indicates how important pheromone is to ant  selection probabilities, is expected heuristic value which indicates how important allowed expectation value is to ant selection probabilities. is a feasible set, indicating the k set of nodes that ant k can choose next.

<!-- b000101 | furniture | pages [7] -->
Team # 1922074

<!-- b000102 | furniture | pages [7] -->
Page

<!-- b000103 | furniture | pages [7] -->
of 29

<!-- b000104 | furniture | pages [7] -->
5

<!-- b000106 | prose | pages [7] -->
      ( ) ( ) t t   ij ij , j allowed        k   ( ) ( ) t t   k p t  (1)  is is ij  s allowed  k ,0 others 

<!-- b000107 | prose | pages [7] -->
The principle of traditional ant colony optimization algorithm is that the principle of the traditional ant colony optimization algorithm is that the ants with shorter routes release more pheromone. As time progresses, the concentration of pheromone accumulated on the shorter route gradually increases, and the number of ants that select the route is also getting more and more. Eventually, ants will focus on the best route under positive feedback. But for the evacuation of people, this situation will happen: when people reach one end of the channel and find that there are many people in the channel, people may choose another channel with fewer people to avoid congestion and collision. When it is found that there are fewer people in the channel, it means that the channel may not be the optimal escape channel, so a channel with more people will be selected. As a result, we need to improve the ant colony optimization algorithm.

<!-- b000108 | heading | pages [7] -->
3.2.2 Improved ant colony optimization algorithm

<!-- b000109 | prose | pages [7] -->
We set a threshold to improve the ant colony optimization algorithm. When the pheromone concentration is lower than the threshold, it means that the number of people in the channel is small. Perhaps this route is not the optimal escape route; when the pheromone concentration is higher than the threshold, it means that the channel is more likely to occur congestion and blocking.

<!-- b000110 | prose | pages [7] -->
For the threshold, when people pass through the channel, they may be crowded inside it without order. However, when passing through the exit of the channel, the maximum number of people allowed to pass at one time is only related to the width of the exit, that is, people are exporting in the form of multiple human chains. The length of the human chain L : is d ( )1 S d S e   L  T T d n (2) d n is the maximum number of people allowed to pass the channel, dl where is the length d is the number of people arriving at the exit of the channel at time T . S 1v of queue, is T m / s the speed when people move. The limit safety speed of people running freely is 1.5

<!-- b000111 | prose | pages [7, 8] -->
5 according to the survey data. At this moment, a visitor is at the entrance of the channel. The speed of human chain is v . Obviously, v  v . 1

<!-- b000112 | furniture | pages [8] -->
Team # 1922074

<!-- b000113 | furniture | pages [8] -->
Page

<!-- b000114 | furniture | pages [8] -->
of 29

<!-- b000115 | furniture | pages [8] -->
6

<!-- b000117 | prose | pages [8] -->
1t （the time）, the tourists just When the human chain completely leaves the channel after arrive at the exit of a channel, which means that the length is the most suitable and this L L d  t ST  nvt  d channel is the optimal route. That is, . At this moment, . 1 1 v v 1

<!-- b000118 | prose | pages [8] -->
Let each person carry a pheromone, then the pheromone concentration of the channel is nvt , the threshold is 1t . Finally, the selection probability after improvement is: 1       ( ) ( ) t t   ij ij , , , ( ) j s allowed t nvt         1 k ij   ( ) ( ) t t    is is       ( ) ( ) t t    ij ij k 1 , , , ( ) p t j s allowed t nvt           1 ij k ij   ( ) ( ) t t    is is   ,0 others   (3)

<!-- b000119 | heading | pages [8] -->
3.2.3 The optimal evacuation route

<!-- b000120 | prose | pages [8] -->
We convert the Louvre's floor plan into a topographic map, and the following figure is an example of the 1st and 2nd floor.

<!-- b000121 | caption | pages [8] -->
Figure 3. The topology of the 1st and 2nd floor

<!-- b000122 | prose | pages [8, 9] -->
6 In the topology, circles indicate various areas, and the nodes with symbols refers to the entrances of stairs, and the red line refers to stairs between different floors.

<!-- b000123 | furniture | pages [9] -->
Team # 1922074

<!-- b000124 | furniture | pages [9] -->
Page

<!-- b000125 | furniture | pages [9] -->
of 29

<!-- b000126 | furniture | pages [9] -->
7

<!-- b000128 | prose | pages [9] -->
We choose the appropriate parameters, bring the Louvre plane topology into the algorithm, and finally get the following optimal evacuation routes. In Figure 4, orange arrows indicate evacuated routes.

<!-- b000129 | caption | pages [9] -->
Figure 4. The optimal evacuation route for the Louvre

<!-- b000130 | heading | pages [9] -->
3.3 The evacuation time

<!-- b000131 | prose | pages [9] -->
We figure out that the time required to evacuate all the visitors in the Louvre is the time when last visitor escapes from the Louvre. Moreover, the farthest floor from the 0th floor and the 2nd basement is the 2nd floor. As a result, there must be a stairway that allows visitors from this stairway to evacuate for the longest time. The time required to evacuate all visitors is the longest time for the last visitor to escape the Louvre, and the shortest evacuation time is the minimum of the longest time.

<!-- b000132 | prose | pages [9] -->
Assuming that the number of stairs on the 2nd floor is I , the length of the human chain at thi L , the length of the stairs is fL , the time evacuate from th j the stairs of the floor is ij thi thi S , th j it , the number of visitors at the the stairs is stairs entrance of the floor is ij

<!-- b000133 | prose | pages [9, 10] -->
7 fn is the number of visitors is the thickness of a visitor, e is the space between visitors, d ' jl who can accommodate up to one row at the stairway, v is the speed when people run, il is the length of the exit from the person to the floor with the exit, thi dt is the length required T is the time of blockage in the stairs, to escape to the staircase, evacuating all visitors. is the time for min

<!-- b000134 | furniture | pages [10] -->
Team # 1922074

<!-- b000135 | furniture | pages [10] -->
Page

<!-- b000136 | furniture | pages [10] -->
of 29

<!-- b000137 | furniture | pages [10] -->
8

<!-- b000139 | prose | pages [10] -->
d of each person, the The length of the human chain is determined by the thickness distance e fn . No matter between people and the number of people through the stairs how crowded outside the stairway, when passing through the stairway, the number of fn , so the human chain can be equivalent to the people passing through the stairway is just fn L personal chain, and the new human chain length

<!-- b000140 | prose | pages [10] -->
L ij

<!-- b000141 | prose | pages [10] -->
it is: ij   1 S d S e   ij ij  n (4) f li is composed of the following times: the time The

<!-- b000142 | prose | pages [10] -->
L f from the current area to the v ' l j through the stairs; the time stairway; the time v Lij after reaching the exit floor, the v

<!-- b000143 | prose | pages [10] -->
through the exit; and possibly on the way The congestion time to the exit; the time v dt .So we can get: time caused by the blockage will occur l t  i i v So, The shortest evacuation time is T 

<!-- b000144 | prose | pages [10] -->
dt : For ' L L l f ij j t     d v v v (5)

<!-- b000145 | prose | pages [10] -->
  min max it (6)

<!-- b000146 | prose | pages [10] -->
• Everyone moves at the same speed in the channel, so there is no blockage.

<!-- b000147 | prose | pages [10] -->
• Since the escape route of each layer may pass through the same stairs, the length and width of the stairs are determined. The following situation is easy to occur: visitors on the 2nd floor have reached the 1st floor stairs, and visitors on the 1st floor have not escaped from this stairway, and finally blockage will occur.

<!-- b000148 | prose | pages [10] -->
We assume that when the above situation occurs, there is a priority, that is, the higher floor ' L allows the lower floor visitors to go first. Then we can get the following model where length of the human chain of the   th j 1  is ij thi ' il staircase of the to the stairs.

<!-- b000149 | prose | pages [10] -->
' L  ij  t  d j floor, and is the distance

<!-- b000150 | prose | pages [10] -->
L L     l f ij '   v l    i   i v v v     v (7)

<!-- b000151 | prose | pages [10, 11] -->
8   ' -' L l l L L     ij i i f ij t  d v (8) j 1 0 Set a parameter , when 0   0   dt dt   , ; when , .

<!-- b000152 | furniture | pages [11] -->
Team # 1922074

<!-- b000153 | furniture | pages [11] -->
Page

<!-- b000154 | furniture | pages [11] -->
of 29

<!-- b000155 | furniture | pages [11] -->
9

<!-- b000157 | prose | pages [11] -->
For the three floors model, the number of visitors on the 2nd floor is S , the 1st floor is 2 1 S and the 0th is 0 S .

<!-- b000158 | prose | pages [11] -->
When an emergency occurs, since Arts of Africa, Asia, Oceania and the Americas is not connected to other areas on the 0th floor, only visitors in Arts of Africa, Asia, Oceania and the Americas can escape from the Portes Des Lions entrance. As a result, the evacuation plan of the visitors on the 0th floor can be divided into two situations:

<!-- b000159 | prose | pages [11] -->
0 00 01 S S S   (9)

<!-- b000160 | prose | pages [11] -->
The visitors in Arts of Africa, Asia, Oceania and the Americas can escape directly, the . The rest visitors on the 0th can run from the 0th floor to the 1st floor, then 00 S number is run to the stairs leading to the Arts. Downstairs and escape from the Portes Des Lions 01 S entrance. The number of visitors in this part is . We observe the escape route, and find that the stairs from the 0th floor to the 1st floor is different from the stairs from the 2nd floor to the 1st floor. Therefore, visitors escape from 0F to 1F can be equivalent to visitors escape from the 2nd floor to the 1st floor.

<!-- b000161 | prose | pages [11] -->
2' 01 2 S S S   (10) is the number of visitors on the 2nd floor after the equivalent. 2 ' S Where

<!-- b000162 | prose | pages [11] -->
The 0th floor and the 2nd floor can be equivalent to the same floor, so there are only the situations that 2 floors of visitors going down the stairs on the first floor, and the first floor dt visitors have not been evacuated. The time of congestion is:

<!-- b000163 | prose | pages [11] -->
' ' ( ) L l l L L     1 2 i i i f i t  d v (11)

<!-- b000164 | prose | pages [11] -->
3T The evacuation time of three floors model is:

<!-- b000165 | prose | pages [11] -->
   min max T it 3  (12)

<!-- b000166 | prose | pages [11] -->
' ' ( ) L l l L L      1 2 i i i f i t   d v  ( )1 S d S e    L  2 2 i i 2 i  v  I  2 01  S S S   ij  1 i  ' l L L l     2 i f i j t   i v  (13) For the five floors model, when the visitors on the 2nd floor are evacuating, the visitors on

<!-- b000167 | prose | pages [11, 12] -->
9 the 1st basement, 0th, and 1st floor may be stuck on the stairs and not evacuated. So, the time dt of congestion is:

<!-- b000168 | furniture | pages [12] -->
Team # 1922074

<!-- b000169 | furniture | pages [12] -->
Page

<!-- b000170 | furniture | pages [12] -->
of 29

<!-- b000171 | furniture | pages [12] -->
10

<!-- b000173 | prose | pages [12] -->
' ' ( 2) L l l L L     1  ij i i f i t  (14) d v 1 j   There are three exits on the 2nd basement, and the Carrousel du Louvre entrance and the Passage Richelieu entrance pass through the same channel, so they can regard as one large exit. The entrance to the pyramid requires a stairway on the 2nd basement, which is the same length as the other two exit channels. As a result, three exits can be equivalent to a 'n new exit. The number of people passing through the new exit is the sum of the three T exits. The evacuation time of five floors model is: 5    min max T it 5  (15) ' ' ( ) L l l L L      1  2 ij i i f i t   d v  1 j   ( )1 S d S e    L  2 2 i i  2 i v  I   2 01 S S S   ij  1 i   ' l L L l    2 i f i j t   i v 

<!-- b000174 | prose | pages [12] -->
10 t s 0  According to the investigation, we can get the reaction time .

<!-- b000175 | prose | pages [12] -->
T Finally, the evacuation time : min

<!-- b000176 | prose | pages [12] -->
max{ , } T T T t   (16) min 3 5 0

<!-- b000177 | prose | pages [12] -->
As we can see from the Figure 2, the number of visitors at 11:30 am on Monday, Thursday, Saturday and Sunday is the highest. It’s about 10,380. We substitute it into the time model 3T T . We use the python language for programming and calculate the value of and 5 calculations (see the appendix for specific code). The result is:

<!-- b000178 | prose | pages [12] -->
417.2 s 281 8. T T 3  5  , s

<!-- b000179 | prose | pages [12] -->
T The shortest evacuation time is 417.2s, about 7 minutes, when the number of visitors min is the largest.

<!-- b000180 | prose | pages [12] -->
According to the information, the best evacuation time for different emergencies is different, but the maximum can not exceed 15 minutes. The shortest evacuation time obtained by the algorithm is realistic and short. Therefore, our model works well.

<!-- b000181 | heading | pages [12] -->
3.4 Emergency personnel

<!-- b000182 | prose | pages [12] -->
When there is an emergency in X area, emergency personnel is required to enter the building as soon as possible, that is, they need to reach the X area through some entrance quickly. The visitors in X area have to escape from there quickly, that is, to reach an exit as soon as possible. However, emergency personnel and visitors are prone to congestion and collisions on stairs and channels. The width of the channel is much larger than the stairs, and the main crowding and collisions will occur at the stairs, where crowding and collisions

<!-- b000183 | prose | pages [12, 13] -->
10 are neglected in the channel. Therefore, the best strategy is that the emergency personnel and visitors do not use the same stairs at the same time, that is, the emergency personnel need to use the stairs without visitors at that moment to avoid congestion. If seal off the original exit and only allow the emergency personnel to enter, it will greatly increase the evacuation time and cause danger. The best way is to open one of other exits for emergency personnel, and visitors still evacuate from the four main entrances.

<!-- b000184 | furniture | pages [13] -->
Team # 1922074

<!-- b000185 | furniture | pages [13] -->
Page

<!-- b000186 | furniture | pages [13] -->
of 29

<!-- b000187 | furniture | pages [13] -->
11

<!-- b000189 | prose | pages [13] -->
( , ( )) G N R t changing over time where N We think of the Louvre as a topology is the node t R set, is the route set that changes over time. The stairway, the various exhibition areas and the entrances are nodes. At the same time, we think of the emergency personnel as a node whose position move with time. Both the stairs and the channels are regarded as routes. The weight of the route is the time required to pass the stairs when the walking 2 / v m s . If there are other visitors on a certain staircase at time t , the weight of  speed is the route is updated to the sum of the time through the stairs and the time for the stairs to be fully unblocked.We get the number of people at different time when the stairs are evacuated by calculations, and then get the time required for the stairs to be completely unblocked at different time. The part of results are show in the following table. The yellow grid means that the stairs are smooth for a while. After the blue finger, the stairs are always clear. The whole result can be seen in the Appendix 1.

<!-- b000190 | caption | pages [13] -->
Table 2. The time when stairs are evacuated completely

<!-- b000191 | prose | pages [13] -->
We use the improved Dijkstra's Algorithm to calculate the optimal route for emergency personnel to the emergency area. The specific process is as follows:

<!-- b000192 | caption | pages [13] -->
Figure 5. The flow chart of optimal route for emergency personnel

<!-- b000193 | prose | pages [13] -->
ijt , iT , and time spent on each aisle of one route is Assuming the time spent on each route is ijt ijt   the time spent on passing staircase is , for a specific route, will be changed because ijt ijt  of the passing of time while will not. consists of two parts, time consumption of going up or down stairs, time consumption of staircase congestion.

<!-- b000194 | prose | pages [13] -->
  T t t   (17) i ij ij j j

<!-- b000195 | prose | pages [13] -->
min( ) min( ) iT , and the route corresponds to iT Then the minimal time cost is is the shortest

<!-- b000196 | prose | pages [13, 14] -->
11 route at this moment. For example, some emergency people now enter by a new entrance (in the southernmost of Sully, close to the staircase B3), and their destination is the room 101 on the -1F. We assume the time from the start of evacuation as T .We set T as 180 and 150, and bring them into our model. The shortest route we get is the same and showed in the following figure:

<!-- b000197 | furniture | pages [14] -->
Team # 1922074

<!-- b000198 | furniture | pages [14] -->
Page

<!-- b000199 | furniture | pages [14] -->
of 29

<!-- b000200 | furniture | pages [14] -->
12

<!-- b000202 | prose | pages [14] -->
180 150 T T  

<!-- b000203 | caption | pages [14] -->
Figure 6. The shortest route A when

<!-- b000204 | prose | pages [14] -->
and

<!-- b000205 | prose | pages [14] -->
We set T as 120 and 90, and bring them into our model. The shortest route we get is the same and showed in the following figure:

<!-- b000206 | prose | pages [14] -->
120 90 T T  

<!-- b000207 | caption | pages [14] -->
Figure 7. The shortest route B when

<!-- b000208 | prose | pages [14] -->
and

<!-- b000209 | prose | pages [14] -->
The route map is showed in the following figure:

<!-- b000210 | caption | pages [14] -->
Figure 8. The route map for route A and B

<!-- b000211 | prose | pages [14] -->
As the moving speed of emergency personnel is estimated to be 2m/s. And they won’t be blocked in staircase because of the small number. While all the staircases are unobstructed, we calculate the time cost of route A and B :

<!-- b000212 | prose | pages [14] -->
130 , 160 T s T s   A B Time for evacuation of each stairs in route A is showed in the Table 3.

<!-- b000213 | caption | pages [14] -->
Table 3. Time for evacuation of each stairs in route A

<!-- b000214 | prose | pages [14] -->
Stairs B3 A3 A1

<!-- b000215 | prose | pages [14, 15] -->
12 Time 110s 46s 172s

<!-- b000216 | furniture | pages [15] -->
Team # 1922074

<!-- b000217 | furniture | pages [15] -->
Page

<!-- b000218 | furniture | pages [15] -->
of 29

<!-- b000219 | furniture | pages [15] -->
13

<!-- b000221 | prose | pages [15] -->
Time for evacuation of each stairs in route B is showed in the Table 4.

<!-- b000222 | caption | pages [15] -->
Table 4. Time for evacuation of each stairs in route B

<!-- b000223 | prose | pages [15] -->
T B Stairs 66s 110s Time

<!-- b000224 | prose | pages [15] -->
So route A can be totally evacuated in 172s, and route B is 110s.

<!-- b000225 | prose | pages [15] -->
, route A and B 90 T  While are both obstructed, and emergency people need to wait until staircases become usable. The time cost of waiting for A is 82s and waiting for B is 20s. The totally time cost on route A is 212s, and on route B is 180s, so route B is shorter.

<!-- b000226 | prose | pages [15] -->
A A 150 T  While , route is still obstructed. The time cost of waiting for is 22s and waiting for B is 0s. The totally time cost on route A is 152s, and on route B is 160s. So route A is shorter.

<!-- b000227 | prose | pages [15] -->
, route A and B are both obstructed. The totally time cost on route A is 180 T  While 130s, and on route B is 160s. So route A is shorter.

<!-- b000228 | prose | pages [15] -->
141 T  According to the calculations, we choose the value of threshold .

<!-- b000229 | heading | pages [15] -->
3.5 Potential factors

<!-- b000230 | prose | pages [15] -->
There are some potential factors we need to consider: diversity of visitors and other entrances visitors don’t know.

<!-- b000231 | heading | pages [15] -->
3.5.1 Diversity of visitors

<!-- b000232 | prose | pages [15] -->
• Tourist group: whether it is a group or an individual to visit the Louvre, when an emergency occurs, the most important thing to do is to quickly escape breaking up the whole into parts instead waiting for the group to gather and then evacuate which may miss the best escape time.

<!-- b000233 | prose | pages [15] -->
• Languages diversity: the languages diversity often leads some visitors to fail to understand the instructions of emergency broadcasters and evacuation personnel.In our li model, it means that the time to reach the stairway increases. We count the number of v tourists from all over the world in the Louvre in 2018 and get percentages of languages showed in Figure 9.

<!-- b000234 | prose | pages [15, 16] -->
13 Considering that most tourists are from European and American countries, we have established the following measures:

<!-- b000235 | furniture | pages [16] -->
Team # 1922074

<!-- b000236 | furniture | pages [16] -->
Page

<!-- b000237 | furniture | pages [16] -->
of 29

<!-- b000238 | furniture | pages [16] -->
14

<!-- b000239 | caption | pages [16] -->
Figure 9. The nationality distribution of visitors

<!-- b000241 | prose | pages [16] -->
- Use English in emergency broadcasts, then broadcast them in French, Spanish, and Chinese.

<!-- b000242 | prose | pages [16] -->
- The staff mainly use English and French for evacuation guidance.

<!-- b000243 | prose | pages [16] -->
- The safety exit signs in the Louvre are marked in English and French. The legend of the emergency evacuation route map should be in English and French. The route instructions should not use words as much as possible.

<!-- b000244 | prose | pages [16] -->
• The disabled: In the Louvre, the disabled can only use disabled elevators. We still use ( , , ) G N R N  the ant colony optimization algorithm and modify the topology where is 0 R is route set. We changed the stairs in the path set R to the disabled the node set and stairs, and changed the ordinary stairway in the node set N to the disabled stairway. The nodes are dedicated elevators for disabled people. The movement speed of disabled people ' 1 / 'n v m s 1  . The capacity of elevators is 10 people. Eventually, we can draw a route map for the escape of disabled people, and Figure 10 is the escape route map on the 2nd floor.

<!-- b000245 | caption | pages [16] -->
Figure 10. The escape route map for the disabled on the 2nd floor

<!-- b000246 | heading | pages [16] -->
3.5.2 Other entrances

<!-- b000247 | prose | pages [16] -->
• Huge visitors traffic: According to the information, when the Louvre held the Da Vinci exhibition in 2012, the daily visitors amounted to three times as many as the usual. If there

<!-- b000248 | prose | pages [16, 17] -->
14 were any emergency at this time, the evacuation time would increase rapidly when only the original four main entrances open. Based on the Time Model, we study the relationship between the number of visitors and the evacuation time, and represent it by the Figure 11.

<!-- b000249 | furniture | pages [17] -->
Team # 1922074

<!-- b000250 | furniture | pages [17] -->
Page

<!-- b000251 | furniture | pages [17] -->
of 29

<!-- b000252 | furniture | pages [17] -->
15

<!-- b000254 | caption | pages [17] -->
Figure 11. The relationship between number of visitors and evacuation time

<!-- b000255 | prose | pages [17] -->
The prime time for emergency evacuation is 15 minutes when the number of visitors is 28000. Therefore, it’s necessary to consider other exit points when the number of visitors is 28000. The surge in visitors is usually due to some reasons such as free ticket opening, special exhibitions and so on. The Louvre will strengthen security forces to prevent a stampede. Therefore, there is no need to worry about the safety of other exit points. What’s more, a N new route map is obtained by modifying the node set in the ant colony optimization algorithm. We find an entrance in the 338 area of the 0th floor that is closed normally.

<!-- b000256 | caption | pages [17] -->
Figure 12 is the route map of the 0th floor and the 1st floor after opening the entrance.

<!-- b000257 | caption | pages [17] -->
Figure 12. The route map after opening the entrance

<!-- b000258 | prose | pages [17] -->
After the entrance is opened, we obtain the shortest evacuation time when the number of visitors is 10380 and compared it with the original evacuation time. The result is showed in the following table.

<!-- b000259 | prose | pages [17, 18] -->
15 Situation Shortest evacuation time(s) Old 417.2 343.4 New

<!-- b000260 | furniture | pages [18] -->
Team # 1922074

<!-- b000261 | furniture | pages [18] -->
Page

<!-- b000262 | furniture | pages [18] -->
of 29

<!-- b000263 | furniture | pages [18] -->
16

<!-- b000264 | caption | pages [18] -->
Table 5. The comparison of evacuation time

<!-- b000266 | prose | pages [18] -->
• Some entrances cannot be used. When some entrances cannot be used normally due to maintenance, the evacuation time will increase dramatically. Therefore, on the one hand, we need to open other exit points, and on the other hand, we should send security personnel to protect three main entrances and exits as soon as possible. a new route map is obtained N by modifying the node set in the ant colony optimization algorithm. The following figure is the route map of the 0th floor and the 1st floor when the Portes Des Lions entrance is closed and the entrance in 338 is open.

<!-- b000267 | caption | pages [18] -->
Table 6. The comparison of evacuation time

<!-- b000268 | prose | pages [18] -->
Situation Shortest evacuation time(s) Old 417.2 430.1 New The new route map is showed in Figure 13:

<!-- b000269 | caption | pages [18] -->
Figure 13. The new route map

<!-- b000270 | heading | pages [18] -->
3.5.3 Some potential threats

<!-- b000271 | prose | pages [18] -->
There are two consequences of potential threats:

<!-- b000272 | prose | pages [18] -->
• Some channels cannot pass.

<!-- b000273 | prose | pages [18] -->
• Some staircase is not accessible.

<!-- b000274 | prose | pages [18, 19] -->
16 and route set R , then we can get the As a result, we only need to modify the node set N new evacuation map. The time required for the new evacuation can be obtained based on the new evacuation map.

<!-- b000275 | furniture | pages [19] -->
Team # 1922074

<!-- b000276 | furniture | pages [19] -->
Page

<!-- b000277 | furniture | pages [19] -->
of 29

<!-- b000278 | furniture | pages [19] -->
17

<!-- b000280 | prose | pages [19] -->
Assuming that the stairs B on the 2nd floor cannot be used, we use the improved ant colony optimization algorithm to get the new escape route on the 2nd floor which is showed in the Figure 14. The evacuation time is 453.3.

<!-- b000281 | caption | pages [19] -->
Figure 14. The escape route on 2F when B cannot be used

<!-- b000282 | heading | pages [19] -->
4. Policy and procedural recommendations

<!-- b000283 | prose | pages [19] -->
We have developed corresponding policies for the Louvre:

<!-- b000284 | prose | pages [19] -->
• In daily life, the Louvre should conduct emergency drills and training for staff in the museum to improve the staff's ability to handle emergencies. Continuously improve the rules and regulations, and strengthen safety education and training. System implementation is one of the most effective measures to regulate people's safety awareness and safety behavior. They also need regularly conduct safety study meetings to improve the safety awareness of security personnel and strengthen work responsibility.

<!-- b000285 | prose | pages [19] -->
• The Louvre also should make the evacuation route map based on the best evacuation route derived from our model. Evacuate routes are marked at various entrances and exits, and evacuation route maps are added to the Louvre map. It is helpful for tourists to understand the evacuation route in advance, and be able to quickly escape according to the evacuation route in case of emergency.

<!-- b000286 | prose | pages [19] -->
• The Louvre should keep the stairs and channels open during normal time, especially the key stairs and channels. It is good for tourists to escape quickly in the event of an emergency.

<!-- b000287 | prose | pages [19] -->
When an emergency happen, first of all, visitors should be informed through the • radio in time to quickly escape along the evacuation route; at the same time, start the corresponding emergency plan according to the current situation. The staff should correctly guide the tourists to the channels and exits. Considering the language diversity of visitors, the staff at least have to fully grasp the English and French. Besides, they

<!-- b000288 | prose | pages [19, 20] -->
17 also need to keep order to avoid crowding and stamping.

<!-- b000289 | furniture | pages [20] -->
Team # 1922074

<!-- b000290 | furniture | pages [20] -->
Page

<!-- b000291 | furniture | pages [20] -->
of 29

<!-- b000292 | furniture | pages [20] -->
18

<!-- b000294 | prose | pages [20] -->
• In the optimal evacuation route got by our model, some stairs are closed, some stairs are only allowed up or down. Therefore, when an emergency happens, the staff is required to place a direction sign next to the corresponding stairs and promptly guide the visitors who are on the wrong stairs to the correct stairs.

<!-- b000295 | prose | pages [20] -->
• For other factors, such as the diversity of visitors, potential threats, whether other entrances are used and so on. The Louvre needs to modify the topology in the ant colony optimization algorithm based on our model, and use the ant colony optimization algorithm to find the optimal evacuation route based on it. The Louvre also needs to develop relevant contingency plans for these factors so that they can respond as quickly as possible.

<!-- b000296 | prose | pages [20] -->
The optimal route for emergency personnel to reach the emergency area can be • calculated according to our model. The Louvre needs to set the time for the emergency personnel to arrive at the Louvre, the location of the emergency area, and the entry of emergency personnel into the Louvre. Different routes make it easy for emergency personnel to reach the area where an emergency occurs.

<!-- b000297 | heading | pages [20] -->
5. The VEE model for other large structures

<!-- b000298 | prose | pages [20] -->
For other large, crowded structures, we still can use the improved ant colony optimization algorithm to get the optimal evacuation route. First, it is necessary to calculate basic data such as the number, length, and width of stairways, passages, and areas of each floor in the structure. It is also necessary to count the specific number of people in each area of each floor at different time so that the optimal evacuation route can be obtained according to the improved ant colony optimization algorithm.

<!-- b000299 | prose | pages [20] -->
At the same time, other factors still need to be considered. For example, the diversity of people in the building, various potential threats (such as some stairs can not be used in an emergency). For these factors, the topology should be modified and updated. After that, we can use ant colony optimization algorithm to find the optimal evacuation route.

<!-- b000300 | prose | pages [20] -->
It is also necessary to consider how the emergency personnel enter the structure. The entry of emergency personnel is different from the evacuation of people inside the structure. On the one hand, the number of emergency personnel is usually not particularly large, and it is usually not necessary to consider whether or not they will be congested. On the other hand, emergency personnel usually need to reach the high floors from the lower floors, avoiding collisions and crowding with people evacuating from the high floors to the lower floors. Therefore, we can use the Dijkstra algorithm where the weight of the route will be change over time. The change value is the time at which the stairs need to be completely unblocked at the current time. Then, we can calculate the optimal evacuation route. In addition, in response to these factors, it is necessary to prepare sufficient emergency plans in advance so that they can respond promptly when corresponding situations occur.

<!-- b000301 | prose | pages [20] -->
18

<!-- b000302 | furniture | pages [21] -->
Team # 1922074

<!-- b000303 | furniture | pages [21] -->
Page

<!-- b000304 | furniture | pages [21] -->
of 29

<!-- b000305 | furniture | pages [21] -->
19

<!-- b000306 | heading | pages [21] -->
6. Sensitivity Analysis

<!-- b000307 | prose | pages [21] -->
There must be a lot of “What if” scenarios happen when the When performing evacuation plans. “What if” scenarios can be reflected in the fluctuation of important parameter of our model.Therefore, we will list two important “What if” scenarios and do sensitive analysis at the same time.

<!-- b000308 | prose | pages [21] -->
• The fluctuation of the speed of tourists. In the actual evacuation, the speed of the tourists will not be exactly 1m/s, and will fluctuate up and down on the basis of 1m/s. We 2.0 adjust the visitor speed v to v  , and the results are shown in the Figure 15.

<!-- b000309 | caption | pages [21] -->
Figure 15. Change the value of speed

<!-- b000310 | prose | pages [21] -->
It can be seen that the effect of speed on evacuation time is very large. Therefore, in the actual evacuation process, the staff should guide the tourists to run as fast as possible while paying attention to safety.

<!-- b000311 | prose | pages [21] -->
• The reduction of the number of people passing through the stairs. In the actual evacuation, the number of people who can pass the stairs at one time is not necessarily the largest, and may be reduced because the stairway is too crowded and the tourists do not 4 3 2 fn fn fn    obey the order. We can adjust the number of stairs by and and , and the result is as shown in the Figure 16.

<!-- b000312 | caption | pages [21] -->
Figure 16. Change the value of the number of people

<!-- b000313 | prose | pages [21] -->
It can be seen that the reduction in the number of people passing through the stairs has a great influence on the evacuation time. Therefore, in the actual evacuation process, it is necessary to ensure the orderly passage of the stairway, and maximize the number of people who can pass the stairs.

<!-- b000314 | prose | pages [21] -->
19

<!-- b000315 | furniture | pages [22] -->
Team # 1922074

<!-- b000316 | furniture | pages [22] -->
Page

<!-- b000317 | furniture | pages [22] -->
of 29

<!-- b000318 | furniture | pages [22] -->
20

<!-- b000319 | heading | pages [22] -->
7. Strengths and Weaknesses

<!-- b000320 | heading | pages [22] -->
7.1 Strengths

<!-- b000321 | prose | pages [22] -->
Our model is an adaptive model, that can be designed to address a broad set of • considerations and various types of potential threats.

<!-- b000322 | prose | pages [22] -->
We improved the ant colony optimization algorithm so that it can be used for the • evacuation planning of large-scale crowded structures.

<!-- b000323 | prose | pages [22] -->
• We have improved the Dijkstra algorithm so that the route of emergency personnel to the emergency area is immediacy.

<!-- b000324 | heading | pages [22] -->
7.2 Weaknesses

<!-- b000325 | prose | pages [22] -->
• For our model, to simplify the calculation, we simply assume the thickness and width of each visitor and the running speed. In fact, we found through information that in 2018, about 10% of tourists are children, and 13% of tourists are elderly people, accounting for about a quarter of the total, and the number is still relatively large.

<!-- b000326 | prose | pages [22] -->
• We simply think that the number of visitors is evenly distributed, except for the area of the treasures of the three major town halls. In fact, the number of visitors in different exhibition areas is inevitably different, and will vary with the size of the exhibition area, the popularity of the exhibition area, and the time.

<!-- b000327 | prose | pages [22] -->
For some stairs, we are unable to obtain the corresponding data. This may affect the • actual evacuation time.

<!-- b000328 | heading | pages [22] -->
8. Conclusion

<!-- b000329 | prose | pages [22] -->
In our work, we make the VEE model to design the evacuation plan. At first, we get different numbers of people at different times of the day according to the current queuing time displayed by the APP "Affluences". Then, we use the improved ant colony optimization algorithm to get the optimal evacuation route, and establish the Time Model to get the shortest evacuation time when the number of people is the largest. Meanwhile, we use the improved Dijkstra algorithm to for emergency personnel to reach the emergency area. We also consider other potential factors. In addition, we propose policy and procedural recommendations for emergency management of the Louvre, and discuss how our model could adapt and implement our models for other large, crowded structures. Finally, we performed sensitivity analysis on two important parameters: the number of people passing through the stairs and the speed.

<!-- b000330 | heading | pages [22] -->
9. References

<!-- b000331 | references | pages [22] -->
[1] Reporters, Telegraph. “Terror Attacks in France: From Toulouse to the Louvre.” The

<!-- b000332 | references | pages [22] -->
Telegraph, Telegraph Media Group, 24 June 2018, www.telegraph.co.uk/news/0/terror-

<!-- b000333 | references | pages [22] -->
attacks-france-toulouse-louvre/.

<!-- b000334 | references | pages [22] -->
20

<!-- b000335 | furniture | pages [23] -->
Team # 1922074

<!-- b000336 | furniture | pages [23] -->
Page

<!-- b000337 | furniture | pages [23] -->
of 29

<!-- b000338 | furniture | pages [23] -->
21

<!-- b000339 | references | pages [23] -->
[2] "8.1 Million Visitors to the Louvre in 2017." Louvre Press Release, 25 Jan. 2018,

<!-- b000340 | references | pages [23] -->
presse.louvre.fr/8-1-million-visitors-to-the-louvre-in-2017/.

<!-- b000341 | references | pages [23] -->
[3] “Interactive Floor Plans.” Louvre - Interactive Floor Plans | Louvre Museum | Paris, 30

<!-- b000342 | references | pages [23] -->
June 2016, ww.louvre.fr/en/plan.

<!-- b000343 | references | pages [23] -->
[4] "Pyramid" Project Launch –

<!-- b000344 | references | pages [23] -->
The Musée du Louvre is improving visitor reception

<!-- b000345 | references | pages [23] -->
(2014-2016)."Louvre Press Kit, 18 Sept. 2014,

<!-- b000346 | references | pages [23] -->
www.louvre.fr/sites/default/files/dp_pyramide%2028102014_en.pdf.

<!-- b000347 | references | pages [23] -->
[5] “ The ‘ Pyramid ’

<!-- b000348 | references | pages [23] -->
Project - Improving Visitor Reception (2014-2016). ”

<!-- b000349 | references | pages [23] -->
Louvre Press

<!-- b000350 | references | pages [23] -->
Release, 6 July 2016, presse.louvre.fr/the-pyramid-project/.

<!-- b000351 | references | pages [23] -->
[6] QIdong Du,Rouxiang Chen,Aijun Xu.Optimization of Evacuation Route Selection in

<!-- b000352 | references | pages [23] -->
Flue Gas Based on ant colony optimization algorithms[J].Computer Era,2018,No. 2:18-21

<!-- b000353 | references | pages [23] -->
[7] Yanfang Zhang,Jing Yuan,Fuchang Wang,Yibin Zhao,Yong ’ an Zhao.Mathematical

<!-- b000354 | references | pages [23] -->
model

<!-- b000355 | references | pages [23] -->
of

<!-- b000356 | references | pages [23] -->
emergency

<!-- b000357 | references | pages [23] -->
evacuation

<!-- b000358 | references | pages [23] -->
in

<!-- b000359 | references | pages [23] -->
densely

<!-- b000360 | references | pages [23] -->
populated

<!-- b000361 | references | pages [23] -->
areas

<!-- b000362 | references | pages [23] -->
and

<!-- b000363 | references | pages [23] -->
its

<!-- b000364 | references | pages [23] -->
optimal

<!-- b000365 | references | pages [23] -->
solution[J].MATHEMATICS IN PRACTICE AND THEORY,2009,No.39(24):48-52

<!-- b000366 | heading | pages [23] -->
10. Appendix

<!-- b000367 | prose | pages [23] -->
1. Table: the time when stairs are evacuated completely

<!-- b000368 | prose | pages [23, 24] -->
21 2. ETxls_time1.py import math import xlwt

<!-- b000369 | furniture | pages [24] -->
Team # 1922074

<!-- b000370 | furniture | pages [24] -->
Page

<!-- b000371 | furniture | pages [24] -->
of 29

<!-- b000372 | furniture | pages [24] -->
22

<!-- b000374 | prose | pages [24] -->
total = 8000 floorweight = [1, 3, 8, 12, 6] floors = [] sum = 0 d = 0.5 e = 0.1 nf = 4 v = 1 aimstairs = [] aimadd = []

<!-- b000375 | prose | pages [24] -->
for f in floorweight:

<!-- b000376 | prose | pages [24] -->
sum += f

<!-- b000377 | prose | pages [24] -->
scost = 10/v print(scost)

<!-- b000378 | prose | pages [24] -->
book = xlwt.Workbook() sheet = book.add_sheet('Result')

<!-- b000379 | prose | pages [24] -->
class stair:

<!-- b000380 | prose | pages [24] -->
def __init__(self, name, fl, aim, aimfloor, num):

<!-- b000381 | prose | pages [24] -->
self.name = name self.fl = fl self.aim = aim self.aimfloor = aimfloor self.num = math.floor(num)

<!-- b000382 | prose | pages [24, 25] -->
22 def run(self, time):

<!-- b000383 | furniture | pages [25] -->
Team # 1922074

<!-- b000384 | furniture | pages [25] -->
Page

<!-- b000385 | furniture | pages [25] -->
of 29

<!-- b000386 | furniture | pages [25] -->
23

<!-- b000388 | prose | pages [25] -->
if time == self.cleartime() and self.aimfloor != -1:

<!-- b000389 | prose | pages [25] -->
ss = floors[s.aimfloor].findstair(s.aim) aimstairs.append(ss) aimadd.append(s.num) self.num = math.floor(self.num - (time*nf*v)/(d+e)) if self.num < 0:

<!-- b000390 | prose | pages [25] -->
self.num = 0

<!-- b000391 | prose | pages [25] -->
def cleartime(self):

<!-- b000392 | prose | pages [25] -->
if (self.num*d + self.num*e)/nf >= 0:

<!-- b000393 | prose | pages [25] -->
return (self.num*d + self.num*e)/(nf*v) else:

<!-- b000394 | prose | pages [25] -->
return 0

<!-- b000395 | prose | pages [25] -->
class floor:

<!-- b000396 | prose | pages [25] -->
def __init__(self, fl, sname, saim, saimfloor, sweight):

<!-- b000397 | prose | pages [25] -->
self.name = fl self.num = total/sum*floorweight[fl] self.stairs = [] n = 0 for t in sweight:

<!-- b000398 | prose | pages [25] -->
n = n + t for i in range(sname.__len__()):

<!-- b000399 | prose | pages [25] -->
self.stairs.append(stair(sname[i], fl, saim[i], saimfloor[i], self.num*sweight[i]/n))

<!-- b000400 | prose | pages [25] -->
def findstair(self, name):

<!-- b000401 | prose | pages [25] -->
for s in self.stairs:

<!-- b000402 | prose | pages [25] -->
if s.name == name:

<!-- b000403 | prose | pages [25] -->
return s return None

<!-- b000404 | prose | pages [25] -->
def min(self):

<!-- b000405 | prose | pages [25] -->
result = None time = 1000000

<!-- b000406 | prose | pages [25] -->
for s in self.stairs:

<!-- b000407 | prose | pages [25] -->
if s.cleartime()>0 and s.cleartime()<time:

<!-- b000408 | prose | pages [25] -->
result = s time = s.cleartime() return result

<!-- b000409 | prose | pages [25, 26] -->
23 def run(self, time):

<!-- b000410 | furniture | pages [26] -->
Team # 1922074

<!-- b000411 | furniture | pages [26] -->
Page

<!-- b000412 | furniture | pages [26] -->
of 29

<!-- b000413 | furniture | pages [26] -->
24

<!-- b000415 | prose | pages [26] -->
for s in self.stairs:

<!-- b000416 | prose | pages [26] -->
s.run(time)

<!-- b000417 | prose | pages [26] -->
if __name__ == '__main__':

<!-- b000418 | prose | pages [26] -->
sn0 = ['E'] sw0 = [1] sa0 = ['esc'] saf0 = [-1]

<!-- b000419 | prose | pages [26] -->
f = floor(0, sn0, sa0, saf0, sw0) floors.append(f)

<!-- b000420 | prose | pages [26] -->
sn1 = ['A1', 'A2', 'A3'] sw1 = [3, 4, 3] sa1 = ['E', 'E', 'E'] saf1 = [0, 0, 0] f = floor(1, sn1, sa1, saf1, sw1) floors.append(f)

<!-- b000421 | prose | pages [26] -->
sn2 = ['B1', 'B2', 'B', 'B3'] sw2 = [2,2,2,2] sa2 = ['A1','A1','A1','A3'] saf2 = [1,1,1,1] f = floor(2, sn2, sa2, saf2, sw2) floors.append(f)

<!-- b000422 | prose | pages [26] -->
sn3 = ['E1','E2','E3','B'] sw3 = [3,1,3,3] sa3 = ['B1','B','B2','B'] saf3 = [2,2,2,2] f = floor(3, sn3, sa3, saf3, sw3) floors.append(f)

<!-- b000423 | prose | pages [26] -->
sn4 = ['E1','B','B4'] sw4 = [4,4,2] sa4 = ['E1','B','F'] saf4 = [3,3,3] f = floor(4, sn4, sa4, saf4, sw4) floors.append(f) totaltime = 0

<!-- b000424 | prose | pages [26, 27] -->
24 col = 0 while True:

<!-- b000425 | furniture | pages [27] -->
Team # 1922074

<!-- b000426 | furniture | pages [27] -->
Page

<!-- b000427 | furniture | pages [27] -->
of 29

<!-- b000428 | furniture | pages [27] -->
25

<!-- b000430 | prose | pages [27] -->
aimstairs.clear() aimadd.clear() time = 1000000 s = None row = 0

<!-- b000431 | prose | pages [27] -->
sheet.write(col, row, 'total') sheet.write(col+1, row, totaltime)

<!-- b000432 | prose | pages [27] -->
for i in range(5):

<!-- b000433 | prose | pages [27] -->
stas = floors[i].stairs for sta in stas:

<!-- b000434 | prose | pages [27] -->
row += 1 str = sta.name + ' ' + sta.fl.__str__() num = sta.cleartime() if num <0:

<!-- b000435 | prose | pages [27] -->
num = 0 sheet.write(col, row, str) sheet.write(col+1, row, num)

<!-- b000436 | prose | pages [27] -->
for i in range(5):

<!-- b000437 | prose | pages [27] -->
ss = floors[i].min() if ss is not None and 0 < ss.cleartime() < time:

<!-- b000438 | prose | pages [27] -->
time = ss.cleartime() s = ss

<!-- b000439 | prose | pages [27] -->
if s is None:

<!-- b000440 | prose | pages [27] -->
break

<!-- b000441 | prose | pages [27] -->
totaltime = totaltime + time + scost for i in range(5):

<!-- b000442 | prose | pages [27] -->
floors[i].run(time)

<!-- b000443 | prose | pages [27] -->
for i in range(aimstairs.__len__()):

<!-- b000444 | prose | pages [27] -->
aimstairs[i].num = aimstairs[i].num + aimadd[i] print(aimstairs[i].name)

<!-- b000445 | prose | pages [27] -->
col += 2

<!-- b000446 | prose | pages [27] -->
print(totaltime)

<!-- b000447 | prose | pages [27] -->
book.save('G:/MathModeling/result_Five.xls')

<!-- b000448 | prose | pages [27, 28] -->
25 3. ETxls_time2.py

<!-- b000449 | furniture | pages [28] -->
Team # 1922074

<!-- b000450 | furniture | pages [28] -->
Page

<!-- b000451 | furniture | pages [28] -->
of 29

<!-- b000452 | furniture | pages [28] -->
26

<!-- b000454 | prose | pages [28] -->
import math import xlwt

<!-- b000455 | prose | pages [28] -->
total = 4000 floorweight = [8, 12, 6] floors = [] sum = 0 d = 0.5 e = 0.1 nf = 6 v = 1

<!-- b000456 | prose | pages [28] -->
aimstairs = [] aimadd = []

<!-- b000457 | prose | pages [28] -->
for f in floorweight:

<!-- b000458 | prose | pages [28] -->
sum += f

<!-- b000459 | prose | pages [28] -->
scost = 10/v

<!-- b000460 | prose | pages [28] -->
book = xlwt.Workbook() sheet = book.add_sheet('Result')

<!-- b000461 | prose | pages [28] -->
class stair:

<!-- b000462 | prose | pages [28] -->
def __init__(self, name, fl, aim, aimfloor, num):

<!-- b000463 | prose | pages [28] -->
self.name = name self.fl = fl self.aim = aim self.aimfloor = aimfloor self.num = math.floor(num)

<!-- b000464 | prose | pages [28] -->
def run(self, time):

<!-- b000465 | prose | pages [28] -->
if time == self.cleartime() and self.aimfloor != -1:

<!-- b000466 | prose | pages [28] -->
ss = floors[s.aimfloor].findstair(s.aim) aimstairs.append(ss) aimadd.append(s.num) self.num = math.floor(self.num - (time*nf*v)/(d+e)) if self.num < 0:

<!-- b000467 | prose | pages [28] -->
self.num = 0

<!-- b000468 | prose | pages [28] -->
def cleartime(self):

<!-- b000469 | prose | pages [28] -->
if (self.num*d + self.num*e)/nf >= 0:

<!-- b000470 | prose | pages [28] -->
return (self.num*d + self.num*e)/(nf*v);

<!-- b000471 | prose | pages [28, 29] -->
26 else:

<!-- b000472 | furniture | pages [29] -->
Team # 1922074

<!-- b000473 | furniture | pages [29] -->
Page

<!-- b000474 | furniture | pages [29] -->
of 29

<!-- b000475 | furniture | pages [29] -->
27

<!-- b000477 | prose | pages [29] -->
return 0

<!-- b000478 | prose | pages [29] -->
class floor:

<!-- b000479 | prose | pages [29] -->
def __init__(self, fl, sname, saim, saimfloor, sweight):

<!-- b000480 | prose | pages [29] -->
self.name = fl self.num = total/sum*floorweight[fl] self.stairs = [] n = 0 for t in sweight:

<!-- b000481 | prose | pages [29] -->
n = n + t for i in range(sname.__len__()):

<!-- b000482 | prose | pages [29] -->
self.stairs.append(stair(sname[i], fl, saim[i], saimfloor[i], self.num*sweight[i]/n))

<!-- b000483 | prose | pages [29] -->
def findstair(self, name):

<!-- b000484 | prose | pages [29] -->
for s in self.stairs:

<!-- b000485 | prose | pages [29] -->
if s.name == name:

<!-- b000486 | prose | pages [29] -->
return s return None

<!-- b000487 | prose | pages [29] -->
def min(self):

<!-- b000488 | prose | pages [29] -->
result = None time = 1000000

<!-- b000489 | prose | pages [29] -->
for s in self.stairs:

<!-- b000490 | prose | pages [29] -->
if s.cleartime()>0 and s.cleartime()<time:

<!-- b000491 | prose | pages [29] -->
result = s time = s.cleartime() return result

<!-- b000492 | prose | pages [29] -->
def run(self, time):

<!-- b000493 | prose | pages [29] -->
for s in self.stairs:

<!-- b000494 | prose | pages [29] -->
s.run(time)

<!-- b000495 | prose | pages [29] -->
if __name__ == '__main__':

<!-- b000496 | prose | pages [29] -->
sn0 = ['B4', 'E', 'T1', 'T2', 'T3', 'T4'] sw0 = [1,4,6,1,1,1] sa0 = ['F','esc','F','F','F','F'] saf0 = [1,-1,1,1,1,1] f = floor(0, sn0, sa0, saf0, sw0)

<!-- b000497 | prose | pages [29, 30] -->
27 floors.append(f)

<!-- b000498 | furniture | pages [30] -->
Team # 1922074

<!-- b000499 | furniture | pages [30] -->
Page

<!-- b000500 | furniture | pages [30] -->
of 29

<!-- b000501 | furniture | pages [30] -->
28

<!-- b000503 | prose | pages [30] -->
sn1 = ['F'] sw1 = [20] sa1 = ['E'] saf1 = [0] f = floor(1, sn1, sa1, saf1, sw1) floors.append(f)

<!-- b000504 | prose | pages [30] -->
sn2 = ['T3','T','T4'] sw2 = [1,1,1] sa2 = ['F','F','F'] saf2 = [1,1,1] f = floor(2, sn2, sa2, saf2, sw2) floors.append(f) totaltime = 0

<!-- b000505 | prose | pages [30] -->
col = 0 while True:

<!-- b000506 | prose | pages [30] -->
aimstairs.clear() aimadd.clear() time = 1000000 s = None row = 0

<!-- b000507 | prose | pages [30] -->
sheet.write(col, row, 'total') sheet.write(col+1, row, totaltime)

<!-- b000508 | prose | pages [30] -->
for i in range(3):

<!-- b000509 | prose | pages [30] -->
stas = floors[i].stairs for sta in stas:

<!-- b000510 | prose | pages [30] -->
row += 1 str = sta.name + ' ' + sta.fl.__str__() num = sta.cleartime() if num <0:

<!-- b000511 | prose | pages [30] -->
num = 0 sheet.write(col, row, str) sheet.write(col+1, row, num)

<!-- b000512 | prose | pages [30] -->
for i in range(3):

<!-- b000513 | prose | pages [30] -->
ss = floors[i].min() if ss is not None and 0 < ss.cleartime() < time:

<!-- b000514 | prose | pages [30] -->
time = ss.cleartime() s = ss

<!-- b000515 | prose | pages [30, 31] -->
28 if s is None:

<!-- b000516 | furniture | pages [31] -->
Team # 1922074

<!-- b000517 | furniture | pages [31] -->
Page

<!-- b000518 | furniture | pages [31] -->
of 29

<!-- b000519 | furniture | pages [31] -->
29

<!-- b000521 | prose | pages [31] -->
break

<!-- b000522 | prose | pages [31] -->
totaltime = totaltime + time + scost for i in range(3):

<!-- b000523 | prose | pages [31] -->
floors[i].run(time)

<!-- b000524 | prose | pages [31] -->
for i in range(aimstairs.__len__()):

<!-- b000525 | prose | pages [31] -->
aimstairs[i].num = aimstairs[i].num + aimadd[i] print(aimstairs[i].name)

<!-- b000526 | prose | pages [31] -->
col += 2

<!-- b000527 | prose | pages [31] -->
print(totaltime)

<!-- b000528 | prose | pages [31] -->
book.save('G:/MathModeling/result_Three.xls')

<!-- b000529 | prose | pages [31] -->
29
