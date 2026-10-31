# P-D-2019-1902407-b8153b5d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
1902407

<!-- b000006 | prose | pages [1] -->
T1 ________________

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
T2 ________________

<!-- b000009 | prose | pages [1] -->
F1 ________________

<!-- b000010 | prose | pages [1] -->
F2 ________________

<!-- b000011 | prose | pages [1] -->
Problem Chosen

<!-- b000012 | prose | pages [1] -->
T3 ________________

<!-- b000013 | prose | pages [1] -->
T4 ________________

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | prose | pages [1] -->
F3 ________________

<!-- b000016 | prose | pages [1] -->
D D

<!-- b000017 | prose | pages [1] -->
F4 ________________

<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
2019

<!-- b000020 | prose | pages [1] -->
MCM/ICM

<!-- b000021 | prose | pages [1] -->
Summary Sheet.

<!-- b000022 | prose | pages [1] -->
In case of the terrorist attacks in France, the Louvre needed emergency evacuation plans to avoid danger. This paper first establishes the goal programming model with the minimum total evacuation time to make sure that people in building can be evacuated safely and quickly. The model divides the evacuation time into the moving phase of the room channel, the up and down building phase, the entry and exit phase, and the accident occurrence phase. By optimizing each of these stages, the goal of minimum total time is achieved. In order to achieve optimal path, we improve the Dijkstra algorithm and find the most efficient route from each room to the exit. In addition, we propose a dynamic scheduling algorithm between the same floor and a dynamic scheduling algorithm between different floors to solve the congestion problem according to the goal planning. Furthermore, we have designed targeted response strategies for different characteristics of vulnerable groups to reduce accidents. In our model, we have obtained the optimal evacuate path of the Louvre and the weak bottleneck location. The emergency evacuation completion time of the Louvre is 527s, and the congestion time is 37.5%. Compared with the random method, we reduced the time by 39.3%, reduced the congestion by 24% and reduced the injury of 60.69%. Secondly, this paper incorporates the disaster factors into the model, which further improves the adaptability of the model to different disasters and also considers the arrangement of emergency personnel entering the building. The maximum number of emergency personnel that can be entered at each intersection can be obtained without affecting the maximum evacuation time.

<!-- b000023 | prose | pages [1] -->
Based on the model, we calculated the maximum number of 410 emergency personnel and 370s of the optimal route through the Lions Gate exit, while through the Richelieu is about 229s but the maximum number was 240. In addition, the model proposed in paper also explores other large-scale multi-storey public buildings and gives model improvement plans. Finally, in response to the conclusions of the model, this paper proposes to Louvre managers the plan to speed up evacuation, arrange emergency personnel, increase exits, and target vulnerable groups.

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [2] -->
Team # 1902407                                                    Page 2 of 27

<!-- b000029 | heading | pages [2] -->
I. Introduction

<!-- b000030 | heading | pages [2] -->
1.1 Problem Introduction

<!-- b000031 | prose | pages [2] -->
Helped design the evacuation plan for the Louvre in Paris, France, the goal of evacuation is to allow all groups of tourists to leave the building as quickly and safely as possible, while allowing emergency personnel to enter the building as soon as possible. However, the complex structure of venues and complex crowd structure make it more difficult to evacuate in an emergency. For example, different groups of organizations (tour groups, disabled people) evacuation processing. After the model is developed, validate the model and discuss how to implement it. Based on the results of the work, recommendations are made on policies and procedures for the emergency management of the Louvre, how to adjust and implement the model for other large congested structures, and how the model performs under different disasters.

<!-- b000032 | heading | pages [2] -->
1.2 Problem Analysis

<!-- b000033 | prose | pages [2] -->
At evacuation exits, we need to be aware of potential bottlenecks in exit movement. The Louvre museum in Paris, France, has complex building structure and diverse tourists, which should be reflected in the emergency evacuation model. The total number of actual exit points in the Louvre is known only to the staff. Although these additional exits can be used by the public, the safety of these exits cannot be guaranteed. Therefore, the reasonable use of these exits in the model should be considered. This model should be universal in order to facilitate adjustment and implementation for other large crowding structures.

<!-- b000034 | heading | pages [2] -->
1.3 Views of our work

<!-- b000035 | furniture | pages [2] -->


<!-- b000036 | caption | pages [2] -->
Figure 1  summary of our work

<!-- b000037 | furniture | pages [2] -->


<!-- b000038 | furniture | pages [2] -->


<!-- b000039 | furniture | pages [3] -->
Team # 1902407                                                    Page 3 of 27

<!-- b000040 | heading | pages [3] -->
Ⅱ. General Assumption

<!-- b000041 | furniture | pages [3] -->


<!-- b000042 | prose | pages [3] -->
⚫   In the event of a disaster, people in the building can be informed of the

<!-- b000043 | prose | pages [3] -->
dangers in a timely and simultaneous manner and immediately begin evacuation operations. The evacuation emergency personnel can start the evacuation operation in ⚫ time, and can obtain the current evacuation status of the current population through electronic devices. ⚫   The evacuated masses listened to the command of evacuation emergency

<!-- b000044 | prose | pages [3] -->
personnel.

<!-- b000045 | furniture | pages [3] -->


<!-- b000046 | furniture | pages [3] -->


<!-- b000047 | furniture | pages [3] -->


<!-- b000048 | furniture | pages [3] -->


<!-- b000049 | heading | pages [3] -->
Ⅲ. Notations Description

<!-- b000050 | furniture | pages [3] -->


<!-- b000051 | heading | pages [3] -->
Notation

<!-- b000052 | prose | pages [3] -->
S

<!-- b000053 | prose | pages [3] -->
D E{𝐞 𝒊𝒋} 𝑪𝒊𝒋

<!-- b000054 | prose | pages [3] -->
𝑪𝒊𝒊

<!-- b000055 | prose | pages [3] -->
𝑵𝒘

<!-- b000056 | prose | pages [3] -->
𝑾

<!-- b000057 | prose | pages [3] -->
𝑻𝟏𝑲

<!-- b000058 | prose | pages [3] -->
𝑾

<!-- b000059 | prose | pages [3] -->
𝑻𝟐𝑲

<!-- b000060 | prose | pages [3] -->
𝑾

<!-- b000061 | prose | pages [3] -->
𝑻𝟑𝑲

<!-- b000062 | prose | pages [3] -->
𝑾

<!-- b000063 | prose | pages [3] -->
𝑻𝟒𝑲

<!-- b000064 | furniture | pages [3] -->


<!-- b000065 | furniture | pages [3] -->


<!-- b000066 | furniture | pages [3] -->


<!-- b000067 | prose | pages [3] -->
Description

<!-- b000068 | prose | pages [3] -->
he node of the path (all exhibition halls,

<!-- b000069 | prose | pages [3] -->
intersections and stairs) Exit node (all exits) The set of paths between nodes I and j Side 𝑒𝑖𝑗 of the maximum number of people

<!-- b000070 | prose | pages [3] -->
per unit time The maximum number of passageways per

<!-- b000071 | prose | pages [3] -->
unit time of node i The number of people passing the floor w

<!-- b000072 | prose | pages [3] -->
The time of the last person escapes when the starting point is on the w floor and taking the

<!-- b000073 | prose | pages [3] -->
k path

<!-- b000074 | prose | pages [3] -->
The time of escaping from the stairs when the

<!-- b000075 | prose | pages [3] -->
starting point is on the w floor and taking the

<!-- b000076 | prose | pages [3] -->
k path

<!-- b000077 | prose | pages [3] -->
The time of escaping from the exits when the starting point is on the w floor and taking the

<!-- b000078 | prose | pages [3] -->
k path

<!-- b000079 | prose | pages [3] -->
Evacuation delays caused by emergencies and

<!-- b000080 | prose | pages [3] -->
special groups (elderly, children, pregnant

<!-- b000081 | prose | pages [3] -->
women and disabled)

<!-- b000082 | furniture | pages [4] -->
Team # 1902407                                                    Page 4 of 27

<!-- b000083 | heading | pages [4] -->
Ⅵ. Model Design

<!-- b000084 | heading | pages [4] -->
4.1 Establish evacuation network

<!-- b000085 | prose | pages [4] -->
Set all exhibition halls, node are 𝑆{𝑆1, 𝑆2, 𝑆3, 𝑆4 … }; Intersections, door (narrow channel) and stairs are 𝑅{𝑅1, 𝑅2,𝑅3, 𝑅4 … }. Specifically, when the node 𝑅𝑥 represents a stair node, 𝑅𝑥

<!-- b000086 | prose | pages [4] -->
the stair at the w floor.

<!-- b000087 | prose | pages [4] -->
𝑤 represents the node of

<!-- b000088 | prose | pages [4] -->
All exits are exit nodes 𝐷{𝐷1, 𝐷2,𝐷3, 𝐷4 … }. The set of paths between node i and j is edge set E{𝑒 𝑖𝑗}, and the nearest node in the building can be reached by path without passing through the connecting edge of other two nodes.

<!-- b000089 | prose | pages [4] -->
Network: G={(S,R,D),E}

<!-- b000090 | furniture | pages [4] -->


<!-- b000091 | caption | pages [4] -->
Figure 2 Example of evacuation network

<!-- b000092 | heading | pages [4] -->
4.2 Optimal Basic Model

<!-- b000093 | prose | pages [4] -->
The goal of emergency evacuation of large multi-story public buildings is to evacuate personnel within the building as quickly as possible. Therefore, the goal of model optimization is to minimize the time that the last evacuated person flees the building.

<!-- b000094 | prose | pages [4] -->
We divide the escape time into the indoor escape phase, the up and down stairs phase, the entry and exit phase, and the escape time delay caused by sudden events such as falls and trampling on the vulnerable groups with a certain probability in the above three stages.

<!-- b000095 | furniture | pages [4] -->


<!-- b000096 | furniture | pages [4] -->


<!-- b000097 | caption | pages [4] -->
Figure 3  Room movement    Figure 4 Staircase movement  Figure 5 Exit movement

<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | prose | pages [4] -->
𝑊+ 𝑇2𝐾

<!-- b000100 | prose | pages [4] -->
minT = 𝑚𝑎𝑥(𝑇1𝐾

<!-- b000101 | prose | pages [4] -->
s.t.

<!-- b000102 | prose | pages [4] -->
𝑊+ 𝑇3𝐾

<!-- b000103 | prose | pages [4] -->
𝑊+ 𝑇4𝐾

<!-- b000104 | prose | pages [4] -->
𝑊) (4 −1)

<!-- b000105 | prose | pages [4] -->
𝑤,𝑘′

<!-- b000106 | prose | pages [4] -->
𝑤,𝑘

<!-- b000107 | prose | pages [4] -->
𝑊= 𝑚𝑎𝑥(𝐿1

<!-- b000108 | prose | pages [4] -->
𝑇1𝐾

<!-- b000109 | prose | pages [4] -->
𝑤,𝑘+ 𝐿1

<!-- b000110 | prose | pages [4] -->
(4 −2) 𝑤,𝑘′)

<!-- b000111 | prose | pages [4] -->
𝑉1 𝑉1

<!-- b000112 | prose | pages [4] -->
𝑉1

<!-- b000113 | prose | pages [4] -->
𝑤,𝑘′

<!-- b000114 | prose | pages [4] -->
𝑤,𝑘

<!-- b000115 | prose | pages [4] -->
𝑊= 𝑚𝑎𝑥(𝐿2

<!-- b000116 | prose | pages [4] -->
𝑇2𝐾

<!-- b000117 | furniture | pages [4] -->


<!-- b000118 | prose | pages [4] -->
𝑤,𝑘+ 𝐿2

<!-- b000119 | prose | pages [4] -->
(4 −3) 𝑤,𝑘′)

<!-- b000120 | prose | pages [4] -->
𝑉2 𝑉2

<!-- b000121 | prose | pages [4] -->
𝑉2

<!-- b000122 | furniture | pages [5] -->
Team # 1902407                                                    Page 5 of 27

<!-- b000123 | prose | pages [5] -->
𝑤,𝑘′

<!-- b000124 | prose | pages [5] -->
𝑤,𝑘

<!-- b000125 | prose | pages [5] -->
𝑊= max (𝐿3

<!-- b000126 | prose | pages [5] -->
𝑇3𝐾

<!-- b000127 | prose | pages [5] -->
𝑊= max ([𝑁𝑘

<!-- b000128 | prose | pages [5] -->
𝑤,𝑘+ 𝐿3

<!-- b000129 | prose | pages [5] -->
(4 −4) 𝑤,𝑘′)

<!-- b000130 | prose | pages [5] -->
𝑉3 𝑉3

<!-- b000131 | prose | pages [5] -->
𝑉3

<!-- b000132 | prose | pages [5] -->
4

<!-- b000133 | prose | pages [5] -->
𝑊+ β𝑇4,2𝐾

<!-- b000134 | prose | pages [5] -->
𝑊+ γ𝑇4,3𝐾

<!-- b000135 | prose | pages [5] -->
𝑊]

<!-- b000136 | prose | pages [5] -->
𝑤𝛿1𝛿2𝑡0] × [α𝑇4,1𝐾

<!-- b000137 | prose | pages [5] -->
𝑤𝛿𝑖𝑡0 + 𝑁𝑘

<!-- b000138 | prose | pages [5] -->
𝑇4𝐾

<!-- b000139 | prose | pages [5] -->
(4 −5) )

<!-- b000140 | prose | pages [5] -->
𝑊≥𝑁𝑤,𝑘  (𝑖, 𝑗𝜖𝑘)

<!-- b000141 | prose | pages [5] -->
𝐶𝑖𝑗∗𝑇1𝐾

<!-- b000142 | prose | pages [5] -->
(4 −6)

<!-- b000143 | prose | pages [5] -->
𝑊≥𝑁𝑤,𝑘  (𝑖, 𝑗𝜖𝑘)

<!-- b000144 | prose | pages [5] -->
𝐶𝑖𝑗∗𝑇2𝐾

<!-- b000145 | prose | pages [5] -->
(4 −7)

<!-- b000146 | prose | pages [5] -->
𝑤,𝑘+ 𝑁𝑆3

<!-- b000147 | prose | pages [5] -->
𝑤,𝑘+ 𝑁𝑆2

<!-- b000148 | prose | pages [5] -->
𝑁𝑤,𝑘= 𝑁𝑆1

<!-- b000149 | prose | pages [5] -->
𝑤,𝑘+ ⋯  (𝑆1, 𝑆2, 𝑆3𝜖𝑘) (4 −8)

<!-- b000150 | prose | pages [5] -->
𝑤,𝑘. 𝑁𝑆3

<!-- b000151 | prose | pages [5] -->
𝑤,𝑘, 𝑁𝑆2

<!-- b000152 | prose | pages [5] -->
𝑁𝑆1

<!-- b000153 | prose | pages [5] -->
𝑤,𝑘… ≥0 (4 −9)

<!-- b000154 | prose | pages [5] -->
Due to the different scenarios, different groups of people moving speed, we need to separate the indoor escape phase, the upper and lower stairs phases, and the entry and exit phases, respectively, using 𝑉1,𝑠

<!-- b000155 | prose | pages [5] -->
𝑤,𝑘  indicates its normal moving speed,

<!-- b000156 | prose | pages [5] -->
𝑤,𝑘, 𝑉3,𝑖

<!-- b000157 | prose | pages [5] -->
𝑤,𝑘, 𝑉2,𝑠

<!-- b000158 | prose | pages [5] -->
𝑤,𝑘 indicates the moving distance of the three stages at normal moving speed.

<!-- b000159 | prose | pages [5] -->
𝑤,𝑘,𝐿2

<!-- b000160 | prose | pages [5] -->
𝑤,𝑘,𝐿3

<!-- b000161 | prose | pages [5] -->
𝐿1

<!-- b000162 | prose | pages [5] -->
W stands for different floors and k stands for route.

<!-- b000163 | prose | pages [5] -->
In each phase, the speed is divided into normal moving speed and moving speed during congestion due to possible congestion. The congestion rate of the indoor escape phase, the upper and lower stairs phases, and the entry and exit phases is expressed as

<!-- b000164 | prose | pages [5] -->
𝑤,𝑘′, the corresponding total length of congestion is 𝐿1

<!-- b000165 | prose | pages [5] -->
𝑤,𝑘′,𝑉2,𝑠

<!-- b000166 | prose | pages [5] -->
𝑤,𝑘′,𝑉3,𝑖

<!-- b000167 | prose | pages [5] -->
𝑉1,𝑠

<!-- b000168 | prose | pages [5] -->
𝑤,𝑘′,𝐿2

<!-- b000169 | prose | pages [5] -->
𝑤,𝑘′,𝐿3

<!-- b000170 | prose | pages [5] -->
𝑤,𝑘′. Although it is more convenient to replace these two variables with time, since the evacuation model needs to consider different characteristics of the population, such as the old and the weak, and these people have significant differences in the speed of movement, the speed is required. This situation will be discussed in the following.

<!-- b000171 | heading | pages [5] -->
4.3 Optimized for moving and exit

<!-- b000172 | prose | pages [5] -->
The indoor escape phase and the exit phase can be optimized using the same method.

<!-- b000173 | prose | pages [5] -->
𝑤,𝑘′

<!-- b000174 | prose | pages [5] -->
𝑤,𝑘

<!-- b000175 | prose | pages [5] -->
𝑚𝑖𝑛𝑇1 ⟹𝑚𝑎x(𝐿1

<!-- b000176 | prose | pages [5] -->
𝑤,𝑘+ 𝐿1

<!-- b000177 | prose | pages [5] -->
(4 −10) 𝑤,𝑘′)

<!-- b000178 | prose | pages [5] -->
𝑉1

<!-- b000179 | prose | pages [5] -->
𝑉1

<!-- b000180 | prose | pages [5] -->
𝑤,𝑘′

<!-- b000181 | prose | pages [5] -->
𝑤,𝑘

<!-- b000182 | prose | pages [5] -->
𝑚𝑖𝑛𝑇3 ⟹𝑚𝑎𝑥(𝐿3

<!-- b000183 | prose | pages [5] -->
𝑤,𝑘+ 𝐿3

<!-- b000184 | prose | pages [5] -->
(4 −11) 𝑤,𝑘′)

<!-- b000185 | prose | pages [5] -->
𝑉3

<!-- b000186 | prose | pages [5] -->
𝑉3

<!-- b000187 | prose | pages [5] -->
Since the speed of movement of a person can be given,

<!-- b000188 | prose | pages [5] -->
𝑤

<!-- b000189 | prose | pages [5] -->
𝐿𝑡𝑜𝑡𝑎𝑙

<!-- b000190 | prose | pages [5] -->
= ∑(𝐿

<!-- b000191 | prose | pages [5] -->
𝑚𝑖𝑛𝑇  is equivalent to

<!-- b000192 | prose | pages [5] -->
𝑤

<!-- b000193 | prose | pages [5] -->
𝑚𝑖𝑛∑𝐿𝑡𝑜𝑡𝑎𝑙

<!-- b000194 | prose | pages [5] -->
𝑤,𝑘′)                                                  (4 −12)

<!-- b000195 | prose | pages [5] -->
𝑤,𝑘+ 𝐿

<!-- b000196 | prose | pages [5] -->
𝑤,𝑘′)                                     (4 −13)

<!-- b000197 | prose | pages [5] -->
𝑤,𝑘+ 𝐿

<!-- b000198 | prose | pages [5] -->
= min (𝐿

<!-- b000199 | prose | pages [5] -->
According to the principle of proximity, min 𝐿𝑆′

<!-- b000200 | prose | pages [5] -->
𝑤,𝑘represent the smallest queuing

<!-- b000201 | prose | pages [5] -->
𝑤 represents the total visitors flow rate of the node i on the w

<!-- b000202 | prose | pages [5] -->
congestion. Assume 𝑁𝑖𝑗

<!-- b000203 | prose | pages [5] -->
𝑤= 𝑁𝑤,𝑘1 + 𝑁𝑤,𝑘2 + 𝑁𝑤,𝑘3 + ⋯, satisfy 𝑘1 ∩𝑘2 ∩𝑘3 ∩… = 𝑖

<!-- b000204 | prose | pages [5] -->
floor. 𝑁𝑖

<!-- b000205 | prose | pages [5] -->
𝑤

<!-- b000206 | prose | pages [5] -->
(𝑁𝑖

<!-- b000207 | prose | pages [5] -->
−𝐿𝑖

<!-- b000208 | prose | pages [5] -->
𝐶𝑖𝑗

<!-- b000209 | furniture | pages [5] -->


<!-- b000210 | prose | pages [5] -->
𝑤,𝑘

<!-- b000211 | prose | pages [5] -->
) = 𝐿

<!-- b000212 | prose | pages [5] -->
(4 −14)

<!-- b000213 | prose | pages [5] -->
𝑉𝑠 𝑉𝑠

<!-- b000214 | prose | pages [5] -->
𝑉𝑆′

<!-- b000215 | furniture | pages [6] -->
Team # 1902407                                                    Page 6 of 27

<!-- b000216 | prose | pages [6] -->
𝑉𝑠  represents the normal walking speed, 𝑉𝑆′  represents the speed of crowd evacuation. Since the escape speed of the crowd is not uniform, the average speed is adopted here.

<!-- b000217 | prose | pages [6] -->
we can get

<!-- b000218 | prose | pages [6] -->
𝑤

<!-- b000219 | prose | pages [6] -->
𝑉𝑆′ (𝑁𝑖

<!-- b000220 | prose | pages [6] -->
𝐶𝑖𝑗

<!-- b000221 | prose | pages [6] -->
−𝐿𝑖

<!-- b000222 | prose | pages [6] -->
(4 −15) ) = 𝐿𝑆′

<!-- b000223 | prose | pages [6] -->
𝑉𝑠

<!-- b000224 | prose | pages [6] -->
In a known congestion paths,𝑉𝑆′，𝐿𝑖 and 𝑉𝑠 for a fixed amount, therefore we should shorten 𝑁𝑖

<!-- b000225 | prose | pages [6] -->
𝑤

<!-- b000226 | prose | pages [6] -->
𝑤,𝑘′ ⇒𝑚𝑖𝑛 𝑁𝑖

<!-- b000227 | prose | pages [6] -->
𝑚𝑖𝑛 𝐿

<!-- b000228 | prose | pages [6] -->
, , , , , , , , , , , , , , , , s.t.

<!-- b000229 | prose | pages [6] -->
, , , , , 𝑤                                                       (4 −16)

<!-- b000230 | prose | pages [6] -->
∑𝑁𝑤= 𝑁𝑡𝑜𝑡𝑎𝑙

<!-- b000231 | prose | pages [6] -->
𝑤= 𝑁𝑧1

<!-- b000232 | prose | pages [6] -->
(4 −17)

<!-- b000233 | prose | pages [6] -->
𝑤+ 𝑁𝑧2

<!-- b000234 | prose | pages [6] -->
𝑁𝑖

<!-- b000235 | prose | pages [6] -->
𝑤+ 𝑁𝑧3

<!-- b000236 | prose | pages [6] -->
𝑤+ ⋯ (4 −18)

<!-- b000237 | heading | pages [6] -->
4.4 Improved Dijkstra for optimal path

<!-- b000238 | prose | pages [6] -->
Dijkstra is one of the best and universal ways to find the best path, time complexity is O(𝑛2). Dijkstra can improve efficiency for the shortest escape route for large multi- storey buildings.

<!-- b000239 | prose | pages [6] -->
Improved direction: 1 Since multi-storey buildings are evacuated, most of the nodes need to go up and ○ down the stairs through a certain staircase. Therefore, for floors without stairs on this floor, the stairs in the exit direction are the only way. We assume 𝑅∗{ 𝑅1

<!-- b000240 | prose | pages [6] -->
necessary set of stairs.

<!-- b000241 | prose | pages [6] -->
∗……} is a

<!-- b000242 | prose | pages [6] -->
∗，𝑅2

<!-- b000243 | prose | pages [6] -->
2 Due to the flow restriction of the stairway, although some routes are the shortest, ○ they are not optimal due to congestion queues. Therefore, when using Dijkstra to find the shortest path, you should avoid the location that may be congested. Therefore, the necessary set of stairs should be reduced to 𝑅∗′{ 𝑅1

<!-- b000244 | furniture | pages [6] -->


<!-- b000245 | prose | pages [6] -->
∗……}.

<!-- b000246 | prose | pages [6] -->
∗，𝑅2

<!-- b000247 | caption | pages [6] -->
Table 1  Improved Dijkstra algorithm for optimal path

<!-- b000248 | prose | pages [6] -->
Input：Network G，Starting node S，Stairway node 𝐑∗，End point set D，Number of people

<!-- b000249 | prose | pages [6] -->
in the stairway 𝐂𝑹𝒊, Unit Coverage Area y. Output： Optimal route from the starting node S to the destination Initialization：(1)initialize S={s}，V={other nodes}

<!-- b000250 | prose | pages [6] -->
(2) If <U,S> set has edges connected, its weight is assigned, otherwise the value

<!-- b000251 | prose | pages [6] -->
is positive infinity. Process：For 𝐢= 𝟏 to length(𝐑∗)

<!-- b000252 | prose | pages [6] -->
∗∗𝐲

<!-- b000253 | prose | pages [6] -->
𝑨𝒓𝒆𝒂= 𝐂𝑹𝒊

<!-- b000254 | prose | pages [6] -->
If 𝐒∉𝐀𝐫𝐞𝐚

<!-- b000255 | prose | pages [6] -->
𝐑∗′ = 𝐑∗ 𝒓𝒆𝒎𝒐𝒗𝒆 𝐑𝒊 𝑺= 𝑺 𝒓𝒆𝒎𝒐𝒗𝒆 𝐑𝒊 End If End For For w to high(Floor difference between starting point and exit)

<!-- b000256 | prose | pages [6] -->
While 𝐍(𝐰) ≠𝟎(The number of nodes in the w floor is not zero)

<!-- b000257 | prose | pages [6] -->
Find node V closest to S in U

<!-- b000258 | furniture | pages [6] -->


<!-- b000259 | furniture | pages [7] -->
Team # 1902407                                                    Page 7 of 27

<!-- b000260 | prose | pages [7] -->
𝑼= 𝑼 𝒓𝒆𝒎𝒐𝒗𝒆 𝐔 𝑺= 𝑺 𝒓𝒆𝒎𝒐𝒗𝒆 𝑺

<!-- b000261 | prose | pages [7] -->
𝒌 in S and 𝐒∩𝐃= ∅)or(𝐒∩𝐃= ∅)

<!-- b000262 | prose | pages [7] -->
If (all 𝐑𝒘

<!-- b000263 | prose | pages [7] -->
Break End If End While End For

<!-- b000264 | heading | pages [7] -->
4.5 Optimized for the Same floor congestion

<!-- b000265 | prose | pages [7] -->
Although the improved Dijkstra can avoid congestion to some extent and find the optimal path, in the event of a sudden disaster, visitors may still be in a hurry and choose the "shortest" path to escape and cause congestion. At this point, the staff is required to perform dynamic scheduling. The overall purpose of the scheduling strategy is to minimize congestion time (to be faster evacuation). When people on all routes gather at one point, the number of people in the location is

<!-- b000266 | prose | pages [7] -->
𝑤,𝑘

<!-- b000267 | prose | pages [7] -->
𝑤= ∑𝑁𝑖

<!-- b000268 | prose | pages [7] -->
𝑁𝑖

<!-- b000269 | prose | pages [7] -->
(4 −19)

<!-- b000270 | prose | pages [7] -->
The scheduling scheme is specifically to guide a part of the crowd at the congestion location to a relatively smooth place. The specific objective function and the conditions are as follows:

<!-- b000271 | prose | pages [7] -->
𝑚𝑖𝑛∑

<!-- b000272 | prose | pages [7] -->
𝑖,𝑗

<!-- b000273 | furniture | pages [7] -->


<!-- b000274 | prose | pages [7] -->
s.t.

<!-- b000275 | prose | pages [7] -->
𝑤= 𝑁𝑧𝑖

<!-- b000276 | prose | pages [7] -->
𝑤

<!-- b000277 | prose | pages [7] -->
(𝑁𝑖

<!-- b000278 | prose | pages [7] -->
−𝐿𝑖

<!-- b000279 | prose | pages [7] -->
(4 −20)

<!-- b000280 | prose | pages [7] -->
)

<!-- b000281 | prose | pages [7] -->
𝐶𝑖𝑗

<!-- b000282 | prose | pages [7] -->
𝑉𝑠

<!-- b000283 | prose | pages [7] -->
𝑤+ 𝑁𝑧2

<!-- b000284 | prose | pages [7] -->
𝑁𝑖

<!-- b000285 | prose | pages [7] -->
1,

<!-- b000286 | prose | pages [7] -->
M =

<!-- b000287 | prose | pages [7] -->
{

<!-- b000288 | prose | pages [7] -->
0,

<!-- b000289 | prose | pages [7] -->
𝑤+ 𝑁𝑧3

<!-- b000290 | prose | pages [7] -->
𝑤+ ⋯ (4 −21)

<!-- b000291 | prose | pages [7] -->
𝑤

<!-- b000292 | prose | pages [7] -->
+ 𝐿𝑖𝑗

<!-- b000293 | prose | pages [7] -->
𝑁𝑖 𝑁𝑖

<!-- b000294 | prose | pages [7] -->
> 𝐿𝑖

<!-- b000295 | prose | pages [7] -->
𝐶𝑖𝑗

<!-- b000296 | prose | pages [7] -->
𝑉𝑠

<!-- b000297 | prose | pages [7] -->
𝑉𝑠

<!-- b000298 | prose | pages [7] -->
(4 −22)

<!-- b000299 | prose | pages [7] -->
𝑤

<!-- b000300 | prose | pages [7] -->
+ 𝐿𝑖𝑗

<!-- b000301 | prose | pages [7] -->
𝑁𝑖 𝑁𝑖

<!-- b000302 | prose | pages [7] -->
≤𝐿𝑖

<!-- b000303 | prose | pages [7] -->
𝐶𝑖𝑗

<!-- b000304 | prose | pages [7] -->
𝑉𝑠

<!-- b000305 | prose | pages [7] -->
𝑉𝑠

<!-- b000306 | prose | pages [7] -->
𝑉𝑠+ 𝐿𝑖𝑗

<!-- b000307 | prose | pages [7] -->
𝑤−(𝐿𝑖

<!-- b000308 | prose | pages [7] -->
𝑁𝑖

<!-- b000309 | prose | pages [7] -->
𝑤−∑𝑁𝑖𝑧

<!-- b000310 | prose | pages [7] -->
𝑤

<!-- b000311 | prose | pages [7] -->
𝑁𝑖

<!-- b000312 | prose | pages [7] -->
−𝐿𝑖

<!-- b000313 | prose | pages [7] -->
> max {M [

<!-- b000314 | prose | pages [7] -->
𝐶𝑖𝑗

<!-- b000315 | prose | pages [7] -->
𝑉𝑠

<!-- b000316 | prose | pages [7] -->
After successful scheduling,

<!-- b000317 | prose | pages [7] -->
𝑁𝑖′𝑤= 𝑁𝑖

<!-- b000318 | prose | pages [7] -->
𝑁𝑗′𝑤= 𝑁𝑗

<!-- b000319 | prose | pages [7] -->
𝑉𝑠)𝐶𝑖𝑗

<!-- b000320 | prose | pages [7] -->
𝑤

<!-- b000321 | prose | pages [7] -->
+ 𝐿𝑖𝑗

<!-- b000322 | prose | pages [7] -->
] + 𝑁𝑖𝑧

<!-- b000323 | prose | pages [7] -->
(4 −23) }

<!-- b000324 | prose | pages [7] -->
𝐶𝑖𝑗

<!-- b000325 | prose | pages [7] -->
𝐶𝑖𝑗

<!-- b000326 | prose | pages [7] -->
𝑉𝑠

<!-- b000327 | prose | pages [7] -->
𝑤−𝑁𝑖𝑧

<!-- b000328 | prose | pages [7] -->
𝑤 (4 −24)

<!-- b000329 | prose | pages [7] -->
𝑤−𝑁𝑗𝑧

<!-- b000330 | prose | pages [7] -->
𝑤 (4 −25) The algorithm for scheduling strategy in the same floor is shown in the appendix.

<!-- b000331 | furniture | pages [7] -->


<!-- b000332 | caption | pages [7] -->
Figure 6 example of scheduling strategy in the same floor

<!-- b000333 | furniture | pages [7] -->


<!-- b000334 | furniture | pages [8] -->
Team # 1902407                                                    Page 8 of 27

<!-- b000335 | heading | pages [8] -->
4.6 Optimized between floors

<!-- b000336 | prose | pages [8] -->
That is, scheduling optimization of the same w floor can reduce congestion time. Secondly, there is scheduling among different floors, and there is a scramble for stairs among different floors，

<!-- b000337 | prose | pages [8] -->
So we assume the objective function is

<!-- b000338 | prose | pages [8] -->
𝑊

<!-- b000339 | prose | pages [8] -->
(4 −26)

<!-- b000340 | prose | pages [8] -->
𝑚𝑖𝑛∑𝑇2𝐾

<!-- b000341 | prose | pages [8] -->
𝑊

<!-- b000342 | prose | pages [8] -->
∑𝑇2𝐾

<!-- b000343 | prose | pages [8] -->
𝑤

<!-- b000344 | prose | pages [8] -->
s.t.

<!-- b000345 | prose | pages [8] -->
𝑤1 + 𝑁𝑖

<!-- b000346 | prose | pages [8] -->
𝑇𝐹𝑖2 = 𝑁𝑖

<!-- b000347 | prose | pages [8] -->
∀  𝑇𝐹𝑖2 −𝑇𝐹𝑖𝑗< 𝐿𝑖𝑗

<!-- b000348 | prose | pages [8] -->
𝑉𝑠

<!-- b000349 | prose | pages [8] -->
𝑤

<!-- b000350 | prose | pages [8] -->
(4 −27)

<!-- b000351 | prose | pages [8] -->
= ∑𝑇𝑓2 𝐹

<!-- b000352 | prose | pages [8] -->
𝑤3 + ⋯

<!-- b000353 | prose | pages [8] -->
𝑤2 + 𝑁𝑖

<!-- b000354 | prose | pages [8] -->
(4 −28)

<!-- b000355 | prose | pages [8] -->
𝐶𝑖2

<!-- b000356 | prose | pages [8] -->
( 𝑇𝐹𝑖2 −𝑇𝐹𝑖𝑗)𝐶𝑖

<!-- b000357 | prose | pages [8] -->
(4 −29)

<!-- b000358 | prose | pages [8] -->
+

<!-- b000359 | prose | pages [8] -->
𝐶𝑗

<!-- b000360 | prose | pages [8] -->
𝑇𝑓𝑖≥0 Therefore, the influence on the scheduling between floors is

<!-- b000361 | prose | pages [8] -->
𝑚𝑖𝑛∑(𝑁𝑖

<!-- b000362 | prose | pages [8] -->
𝑖

<!-- b000363 | prose | pages [8] -->
s.t.

<!-- b000364 | prose | pages [8] -->
𝑤= 𝑁𝑧1

<!-- b000365 | prose | pages [8] -->
𝑤(𝑤−1)

<!-- b000366 | prose | pages [8] -->
−𝐿𝑖

<!-- b000367 | prose | pages [8] -->
(4 −30)

<!-- b000368 | prose | pages [8] -->
)

<!-- b000369 | prose | pages [8] -->
𝐶𝑖

<!-- b000370 | prose | pages [8] -->
𝑉𝑠

<!-- b000371 | prose | pages [8] -->
𝑤+ 𝑁𝑧2

<!-- b000372 | prose | pages [8] -->
𝑁𝑖

<!-- b000373 | prose | pages [8] -->
𝑤+ 𝑁𝑧3

<!-- b000374 | prose | pages [8] -->
𝑤+ ⋯                                         (4 −31)

<!-- b000375 | prose | pages [8] -->
𝑉𝑠+ 𝐿𝑖𝑗

<!-- b000376 | prose | pages [8] -->
𝑤(𝑤−1) −(𝐿𝑖

<!-- b000377 | prose | pages [8] -->
𝑁𝑗

<!-- b000378 | prose | pages [8] -->
𝑤−∑𝑁𝑖2

<!-- b000379 | prose | pages [8] -->
𝑤)

<!-- b000380 | prose | pages [8] -->
(𝑤−1)(𝑁𝑖

<!-- b000381 | prose | pages [8] -->
−𝐿𝑖

<!-- b000382 | prose | pages [8] -->
> 𝑚𝑎𝑥{𝑀[

<!-- b000383 | prose | pages [8] -->
𝐶𝑖𝑖

<!-- b000384 | prose | pages [8] -->
𝑉𝑠

<!-- b000385 | prose | pages [8] -->
𝑉𝑠) 𝐶𝑗

<!-- b000386 | prose | pages [8] -->
𝑤(𝑤−1)

<!-- b000387 | prose | pages [8] -->
+ 𝐿𝑖𝑗

<!-- b000388 | prose | pages [8] -->
] + 𝑁𝑖2

<!-- b000389 | prose | pages [8] -->
} (4 −32)

<!-- b000390 | prose | pages [8] -->
𝐶𝑗

<!-- b000391 | prose | pages [8] -->
𝐶𝑖𝑗

<!-- b000392 | prose | pages [8] -->
𝑉𝑠

<!-- b000393 | prose | pages [8] -->
The algorithm for scheduling strategy between different floors is shown in the appendix.

<!-- b000394 | furniture | pages [8] -->


<!-- b000395 | furniture | pages [8] -->


<!-- b000396 | caption | pages [8] -->
Figure 7 Example of scheduling strategy between different floors

<!-- b000397 | heading | pages [8] -->
4.7 Special crowd handling and emergency optimization

<!-- b000398 | prose | pages [8] -->
The objective function is

<!-- b000399 | prose | pages [8] -->
𝑊= [𝑁𝑘

<!-- b000400 | prose | pages [8] -->
4 (4 −33)

<!-- b000401 | prose | pages [8] -->
𝑊+ 𝛽𝑇4,2𝐾

<!-- b000402 | prose | pages [8] -->
𝑊+ 𝛾𝑇4,3𝐾

<!-- b000403 | prose | pages [8] -->
𝑊]

<!-- b000404 | prose | pages [8] -->
𝑤𝛿1𝛿2𝑡0] × [𝛼𝑇4,1𝐾

<!-- b000405 | prose | pages [8] -->
𝑤𝛿𝑖𝑡0 + 𝑁𝑘

<!-- b000406 | prose | pages [8] -->
𝑚𝑖𝑛𝑇4𝐾

<!-- b000407 | prose | pages [8] -->
We explain the above function,

<!-- b000408 | prose | pages [8] -->
𝛿1 represents the probability of falling while fleeing in a particular population;

<!-- b000409 | prose | pages [8] -->
𝛿2 represents the probability of a stampede after a fall in a particular crowd;

<!-- b000410 | prose | pages [8] -->
𝑾 represents the ratio of the queue time of all people walking and congested to the

<!-- b000411 | prose | pages [8] -->
𝑻𝟒,𝟏𝑲

<!-- b000412 | prose | pages [8] -->
𝑾 represents the ratio of the queue time of all the crowds up and

<!-- b000413 | prose | pages [8] -->
total walking time;  𝑻𝟒,𝟐𝑲

<!-- b000414 | prose | pages [8] -->
down the stairs to the total stairs time;  𝑻𝟒,𝟑𝑲

<!-- b000415 | furniture | pages [8] -->


<!-- b000416 | prose | pages [8] -->
𝑾 represents the ratio of all people escaping

<!-- b000417 | furniture | pages [9] -->
Team # 1902407                                                    Page 9 of 27

<!-- b000418 | prose | pages [9] -->
from the export congestion queue time to the total escape time.

<!-- b000419 | prose | pages [9] -->
𝑤× 𝜌 (4 −34)

<!-- b000420 | prose | pages [9] -->
𝛿1 = 𝐷𝑁𝑘

<!-- b000421 | prose | pages [9] -->
𝑤 represents the number of special people in the k floor using the k path.

<!-- b000422 | prose | pages [9] -->
𝐷𝑁𝑘

<!-- b000423 | prose | pages [9] -->
𝑤= 𝐷𝑁𝑡𝑜𝑡𝑎𝑙

<!-- b000424 | prose | pages [9] -->
∑D𝑁𝑘

<!-- b000425 | prose | pages [9] -->
(4 −35)

<!-- b000426 | prose | pages [9] -->
(4 −36) 𝐷𝑁𝑡𝑜𝑡𝑎𝑙= (ρ1 + ρ2 + ρ3 + ρ4) × 𝑁𝑡𝑜𝑡𝑎𝑙

<!-- b000427 | prose | pages [9] -->
ρ1, ρ2, ρ3, ρ4 represent the proportion of the elderly, children, pregnant women and the disabled respectively. The main population and feature of 𝑇4

<!-- b000428 | caption | pages [9] -->
Table 2  Group feature analysis

<!-- b000429 | prose | pages [9] -->
group Elderly children

<!-- b000430 | prose | pages [9] -->
Speed 0.5v 0.5v

<!-- b000431 | prose | pages [9] -->
Weight(kg) 50 30

<!-- b000432 | prose | pages [9] -->
Force (N) 25 15

<!-- b000433 | prose | pages [9] -->
Pregnant woman Disabled

<!-- b000434 | prose | pages [9] -->
0.2v 0.2v

<!-- b000435 | prose | pages [9] -->
60 55

<!-- b000436 | prose | pages [9] -->
21 24

<!-- b000437 | prose | pages [9] -->
Faster, easy to

<!-- b000438 | prose | pages [9] -->
Feature Slower, easy to

<!-- b000439 | prose | pages [9] -->
fall

<!-- b000440 | prose | pages [9] -->
fall

<!-- b000441 | furniture | pages [9] -->


<!-- b000442 | heading | pages [9] -->
4.7.1 Strategy to reduce 𝑻𝟒

<!-- b000443 | prose | pages [9] -->
•Arrange dedicated passages with special identification equipment (hats) for easy identification.

<!-- b000444 | prose | pages [9] -->
Easy to

<!-- b000445 | prose | pages [9] -->
fall

<!-- b000446 | prose | pages [9] -->
Difficult to handle

<!-- b000447 | prose | pages [9] -->
•Make sure that there

<!-- b000448 | prose | pages [9] -->
emergen

<!-- b000449 | prose | pages [9] -->
are passengers who are

<!-- b000450 | prose | pages [9] -->
cies

<!-- b000451 | prose | pages [9] -->
evacuated around them, but not let them go to the crowded places.

<!-- b000452 | prose | pages [9] -->
Slower, prone to

<!-- b000453 | prose | pages [9] -->
Easy to fall, prone

<!-- b000454 | prose | pages [9] -->
accidents

<!-- b000455 | prose | pages [9] -->
to accidents

<!-- b000456 | furniture | pages [9] -->


<!-- b000457 | furniture | pages [9] -->


<!-- b000458 | prose | pages [9] -->
•When using scheduling strategies, minimize the scheduling of these people

<!-- b000459 | prose | pages [9] -->
Slow

<!-- b000460 | prose | pages [9] -->
Language

<!-- b000461 | prose | pages [9] -->
•Set up simple and easy

<!-- b000462 | prose | pages [9] -->
barrier

<!-- b000463 | prose | pages [9] -->
indicator diagram;Use

<!-- b000464 | prose | pages [9] -->
general language

<!-- b000465 | prose | pages [9] -->
(including body language);Multiple languages are required

<!-- b000466 | prose | pages [9] -->
•。

<!-- b000467 | furniture | pages [9] -->


<!-- b000468 | caption | pages [9] -->
Figure 8 Strategy to reduce 𝑻𝟒

<!-- b000469 | furniture | pages [9] -->


<!-- b000470 | furniture | pages [9] -->


<!-- b000471 | heading | pages [9] -->
Ⅴ. Model application in the Louvre

<!-- b000472 | heading | pages [9] -->
5.1 Data Analysis

<!-- b000473 | prose | pages [9] -->
The Louvre has a total of five floors. The total area of Louvre is about 72735𝑚2. It is divided into two underground floors and three floors above ground. Visitors enter the second floor. Most of the exhibition halls are on the third floor.

<!-- b000474 | furniture | pages [9] -->


<!-- b000475 | furniture | pages [10] -->
Team # 1902407                                                    Page 10 of 27

<!-- b000476 | caption | pages [10] -->
Table 3 Basic data of Louvre

<!-- b000477 | prose | pages [10] -->
Narrow

<!-- b000478 | prose | pages [10] -->
The

<!-- b000479 | prose | pages [10] -->
Total room

<!-- b000480 | furniture | pages [10] -->


<!-- b000481 | prose | pages [10] -->
area（m2）

<!-- b000482 | prose | pages [10] -->
Narrow

<!-- b000483 | prose | pages [10] -->
Number

<!-- b000484 | prose | pages [10] -->
Stair area

<!-- b000485 | prose | pages [10] -->
（m2）

<!-- b000486 | prose | pages [10] -->
channel

<!-- b000487 | prose | pages [10] -->
number

<!-- b000488 | prose | pages [10] -->
channel area

<!-- b000489 | prose | pages [10] -->
of stairs

<!-- b000490 | prose | pages [10] -->
（m2）

<!-- b000491 | prose | pages [10] -->
number

<!-- b000492 | prose | pages [10] -->
of rooms

<!-- b000493 | prose | pages [10] -->
2nd floor 98 12520.32 1st floor 153 18211.38 Ground floor 122 21626.01 Lower

<!-- b000494 | prose | pages [10] -->
27 11382.11

<!-- b000495 | prose | pages [10] -->
ground floor

<!-- b000496 | prose | pages [10] -->
Napoleon

<!-- b000497 | prose | pages [10] -->
1 6260.16

<!-- b000498 | prose | pages [10] -->
Hall

<!-- b000499 | prose | pages [10] -->
27 787.12 10 919.48 55 734.66 16 2226 67 518.5 18 1870

<!-- b000500 | prose | pages [10] -->
5 5 620.5 13 872

<!-- b000501 | prose | pages [10] -->
1 1 2304 3 94.5

<!-- b000502 | prose | pages [10] -->
(Note: The data sheet is from Google Maps, the guide of the Louvre official website.)

<!-- b000503 | prose | pages [10] -->
It can be learned from the above data that the most dense (the smallest area) and the largest number of room is 1st floor, the average room area is 212 m2/per room, next the ground floor is 309 m2/per room. This shows that the museum’s visitors will gather in the ground floor and the 1st floor. And the average area of the narrow channel of the ground floor is the smallest, being 7.73 m2 / per channel. The narrow channel area of the 1st floor is the second smallest, which is 13.35 m2 / per channel. Therefore, it can be inferred that due to the dense rooms and narrow passages, a large amount of congestion may occur, so the biggest difficulty in evacuation is the evacuation for the ground floor and the 1st floor.

<!-- b000504 | heading | pages [10] -->
5.2 Establish the network node model

<!-- b000505 | furniture | pages [10] -->


<!-- b000506 | caption | pages [10] -->
Figure 9 Louvre evacuation network plan

<!-- b000507 | heading | pages [10] -->
5.3 Model Solution and Result

<!-- b000508 | prose | pages [10] -->
According to the latest statistics, the total number of tourists in the Louvre in 2018 was 10.2 million, an average of 27,945 people per day. Considering the limited capacity of the museum to accommodate tourists, the peak of the museum is one-half of the daily average data, that is, the maximum number of visitors is approximately 13,972 at a certain moment.

<!-- b000509 | heading | pages [10] -->
5.3.1 Longest route and time

<!-- b000510 | furniture | pages [10] -->


<!-- b000511 | furniture | pages [11] -->
Team # 1902407                                                    Page 11 of 27

<!-- b000512 | caption | pages [11] -->
Table 4 Longest route and time

<!-- b000513 | prose | pages [11] -->
Floor Location

<!-- b000514 | prose | pages [11] -->
2nd floor

<!-- b000515 | prose | pages [11] -->
Evacuation route

<!-- b000516 | prose | pages [11] -->
The population of the area is evacuated south to the corner of the 931 area 924 area

<!-- b000517 | prose | pages [11] -->
and the 924 area and lowered two steps to the 337 area, and then passes

<!-- b000518 | prose | pages [11] -->
through the 338 area, the 339 area, the 345 area, the 347 area, the 408 area, and then descends by stairs to the lower ground floor Zone 170, then

<!-- b000519 | prose | pages [11] -->
descend one step to the Napoleon Hall through the stairs, and finally rise

<!-- b000520 | prose | pages [11] -->
two floors to the exit of the pyramid to escape the exit

<!-- b000521 | prose | pages [11] -->
1st floor The population in this area passes through 640 area, 641 area, 645 area, 636 area

<!-- b000522 | prose | pages [11] -->
650 area, 661 area, 703 area, and then descends two steps to the lower ground floor 170 area through the stairs, and then descends to the Napoleon Hall through the stairs, and finally rises two floors to the exit of

<!-- b000523 | prose | pages [11] -->
the pyramid to escape the exit.

<!-- b000524 | prose | pages [11] -->
The population in this area passes through the 328 area, the 337 area, the

<!-- b000525 | prose | pages [11] -->
Ground

<!-- b000526 | prose | pages [11] -->
323 area

<!-- b000527 | prose | pages [11] -->
338 area, the 339 area, the 345 area, the 347 area, the 408 area, and then

<!-- b000528 | prose | pages [11] -->
floor

<!-- b000529 | prose | pages [11] -->
descends by a staircase to the lower ground floor 170 area, and then descends one to two floors through the stairs. And finally rise two floors

<!-- b000530 | prose | pages [11] -->
to the exit of the pyramid to escape the exit.

<!-- b000531 | prose | pages [11] -->
The population in this area first passes through the 183 area, then the

<!-- b000532 | prose | pages [11] -->
Lower

<!-- b000533 | prose | pages [11] -->
181 area north walks to the diamond staircase and descends to the Napoleon Hall,

<!-- b000534 | prose | pages [11] -->
ground

<!-- b000535 | prose | pages [11] -->
and finally flees the exit through the Carrousel du Louvre underground

<!-- b000536 | prose | pages [11] -->
floor

<!-- b000537 | prose | pages [11] -->
corridor.

<!-- b000538 | prose | pages [11] -->
Escape the exit along the Carrousel du Louvre underground corridor

<!-- b000539 | prose | pages [11] -->
Napoleon

<!-- b000540 | prose | pages [11] -->
Diamond

<!-- b000541 | prose | pages [11] -->
Hall

<!-- b000542 | prose | pages [11] -->
Square

<!-- b000543 | furniture | pages [11] -->


<!-- b000544 | furniture | pages [11] -->


<!-- b000545 | caption | pages [11] -->
Table 5  Comparison between model and random

<!-- b000546 | prose | pages [11] -->
2nd floor 1st floor

<!-- b000547 | furniture | pages [11] -->


<!-- b000548 | heading | pages [11] -->
Model time

<!-- b000549 | prose | pages [11] -->
527.5s 487s

<!-- b000550 | prose | pages [11] -->
Random time 878s 729s

<!-- b000551 | heading | pages [11] -->
Model injuries

<!-- b000552 | prose | pages [11] -->
12 21

<!-- b000553 | prose | pages [11] -->
Random

<!-- b000554 | prose | pages [11] -->
25 55

<!-- b000555 | prose | pages [11] -->
injuries

<!-- b000556 | prose | pages [11] -->
Ground

<!-- b000557 | prose | pages [11] -->
Lower

<!-- b000558 | prose | pages [11] -->
Napoleon Hall

<!-- b000559 | prose | pages [11] -->
floor

<!-- b000560 | prose | pages [11] -->
ground floor

<!-- b000561 | prose | pages [11] -->
444.5s 188.5s 58.4s

<!-- b000562 | prose | pages [11] -->
653s 223s 67.5s

<!-- b000563 | prose | pages [11] -->
30 14 17

<!-- b000564 | prose | pages [11] -->
67 35 57

<!-- b000565 | prose | pages [11] -->
(Note: 𝛿1 =0.08； 𝛿2=0.25；𝛼= 1.2，β = 4.7，γ = 2.4)

<!-- b000566 | furniture | pages [11] -->


<!-- b000567 | prose | pages [11] -->
From the results, the time of the model is reduced by 39.3% compared with the random time, and the model in this paper is effective. The number of injured in this model was reduced from 239 to 94, a decrease of 60.69%.

<!-- b000568 | prose | pages [11] -->
Since the main exit of the Louvre is on the 2nd floor, it takes the longest time to evacuate from the 2nd floor. Although there are entrances and exits on both sides of the Louvre, the exit of the Lions Gate is not connected to other rooms on the ground floor; the exit of Richelieu will give priority to people on the north side. Therefore, if people on the 2nd floor choose to go out, it will cause more big congestion. Therefore the best way to exit the 2nd floor is to return to the main exit of the Napoleon Hall.

<!-- b000569 | furniture | pages [11] -->


<!-- b000570 | furniture | pages [12] -->
Team # 1902407                                                    Page 12 of 27

<!-- b000571 | prose | pages [12] -->
We noticed that the slowest route on all floors was evacuated through the Napoleon Hall, and the extra downstairs did take more time. Therefore, if more exits can be added on the ground floor, the evacuation time will be effectively reduced.

<!-- b000572 | heading | pages [12] -->
5.3.2 Evacuation congestion analysis

<!-- b000573 | furniture | pages [12] -->


<!-- b000574 | caption | pages [12] -->
Figure 10 Total number of evacuations in exits

<!-- b000575 | prose | pages [12] -->
From the chart we can see the exit evacuation: pyramid > Richelieu > Carrousel du Louvre > Lions Gate, the longest time to evacuate : the Carrousel du Louvre > Pyramid > Richelieu > Lions Gate. From the time, we can find the entrance and exit of the ground floor has an obvious effect on the evacuation speed, but from the evacuation number, the Napoleon Hall entrance and exit has an advantage.

<!-- b000576 | caption | pages [12] -->
Table 6 Time analysis of areas

<!-- b000577 | prose | pages [12] -->
Congestion

<!-- b000578 | furniture | pages [12] -->


<!-- b000579 | prose | pages [12] -->
Normal Congestion

<!-- b000580 | prose | pages [12] -->
proportion

<!-- b000581 | prose | pages [12] -->
Room 186.8s 89.2s 16.9% movement

<!-- b000582 | prose | pages [12] -->
Upstairs

<!-- b000583 | prose | pages [12] -->
and

<!-- b000584 | prose | pages [12] -->
137s 103s 19.5%

<!-- b000585 | prose | pages [12] -->
downstairs

<!-- b000586 | prose | pages [12] -->
Exit 5.5s 6s 1.1% movement

<!-- b000587 | furniture | pages [12] -->


<!-- b000588 | prose | pages [12] -->
329.3s 198.2s 527.5s

<!-- b000589 | caption | pages [12] -->
Figure 11 Time analysis stereogram

<!-- b000590 | prose | pages [12] -->
In the Louvre evacuation, the slowest route was 52.3% in the room and channel movement; the downstairs time was 45.4% and the exit time was 2.1%.

<!-- b000591 | prose | pages [12] -->
About 49.7% of the time on the slowest route was spent on congestion. Among them, congestion was 2.1% at the entrance and exit, 27.1% at the upper and lower floors, and 20.7% between the room and the channel movement. There are too many corridors from the 2nd floor to the Napoleon Hall, and the distance is long, so it takes more time. However, if evacuated from the ground floor, although the path is shortened, it will collide with the people who are evacuated from the first two floors to the first two layers,

<!-- b000592 | furniture | pages [12] -->


<!-- b000593 | furniture | pages [13] -->
Team # 1902407                                                    Page 13 of 27

<!-- b000594 | prose | pages [13] -->
resulting in greater congestion and delayed evacuation.

<!-- b000595 | heading | pages [13] -->
5.3.3 Potential nodes that limit exits

<!-- b000596 | furniture | pages [13] -->


<!-- b000597 | prose | pages [13] -->
B(Demon on lower ground floor ); D (Lions exit on the ground floor); C(The left vertex at the exit of the diamond); E(Right

<!-- b000598 | prose | pages [13] -->
staircase at the 170 area on the lower ground floor); A(Two exit nodes of the Richelieu)

<!-- b000599 | caption | pages [13] -->
Figure 12 Bottlenect node flow diagram

<!-- b000600 | prose | pages [13] -->
We select five nodes with the highest peak traffic flow at a certain time for analysis. The Louvre's largest peak of human traffic appeared at the lower ground floor of Demon after 245s of evacuation. At this time, the 2nd, 1st , and ground floor people passed through the channel at the same time, and the number of people passing through 30 approaching 700.

<!-- b000601 | prose | pages [13] -->
The second weak link is the left apex of the Diamond exit, the entry point of the Richelieu exit, the stairway of the 170th floor of the lower ground floor, and the entry point of the exit of the ground floor Lions’ Gate.

<!-- b000602 | prose | pages [13] -->
We noticed that two of the weaknesses of the top five restricted exits were at the point of proximity to the entrance and exit. And the two exits are all on the ground floor, which means that the evacuation channel of the ground floor entrance and exit has been fully utilized, our model is accurate, and the museum should pay attention to widening on both sides.

<!-- b000603 | furniture | pages [13] -->


<!-- b000604 | furniture | pages [13] -->


<!-- b000605 | furniture | pages [13] -->


<!-- b000606 | heading | pages [13] -->
Ⅵ. Model Improvement

<!-- b000607 | heading | pages [13] -->
6.1 Model improvements under other disasters

<!-- b000608 | heading | pages [13] -->
6.1.1 Evacuation models for avoiding hazardous areas

<!-- b000609 | prose | pages [13] -->
The previous model is mainly for the general evacuation under ideal conditions, that is, the channel is complete, and there is no obstacle to personnel movement and access. The improvement of the model, that is, the emergency evacuation when the evacuation channel is incomplete and the movement of the person is limited is considered.

<!-- b000610 | prose | pages [13] -->
Emergency evacuation disasters that may be encountered at the Louvre include: fires, earthquakes, violent public attacks, stampede accidents, chemical gas leaks, etc. The methods of these accidents often lead to the unavailability of stairs, passages, and exits.

<!-- b000611 | furniture | pages [13] -->


<!-- b000612 | furniture | pages [14] -->
Team # 1902407                                                    Page 14 of 27

<!-- b000613 | prose | pages [14] -->
At this point, the previous model needs to make three changes:

<!-- b000614 | prose | pages [14] -->
(1) Change the network path.

<!-- b000615 | prose | pages [14] -->
When a fire occurs, or a terrorist bomb attack on a place after use, at the location, personnel should be avoided. (2) Set the recommended route.

<!-- b000616 | prose | pages [14] -->
When the scope of the disaster is large and not clear, in order to avoid casualties, it is often mandatory or recommended to evacuate from certain exits and passages.

<!-- b000617 | heading | pages [14] -->
The algorithm of evacuation models for avoiding hazardous areas is shown in

<!-- b000618 | prose | pages [14] -->
appendix.

<!-- b000619 | prose | pages [14] -->
It can be seen from the algorithm that when an accident occurs in some places, limited the search range of the Dijkstra algorithm can avoid the dangerous area.

<!-- b000620 | prose | pages [14] -->
(3) Consider the impact of different natures of disasters on people's movement speed and mood.

<!-- b000621 | prose | pages [14] -->
When a large fire suddenly spreads and the smoke is large, people's moving speed will be affected and will be reduced. In the event of a sudden incident such as a shooting incident, an explosion, or an earthquake, the speed will increase due to extreme panic, but the accident rate will increase.

<!-- b000622 | prose | pages [14] -->
We assume 𝜑0 be the disaster factor caused by the accident.𝑆𝑐𝑎𝑙𝑒  represents the disaster grade. The disaster factor can be determined by the level of the disaster accident.

<!-- b000623 | prose | pages [14] -->
𝑆𝑐𝑎𝑙𝑒𝑖−𝑆𝑐𝑎𝑙𝑒𝑚𝑖𝑛 𝜑0 =

<!-- b000624 | prose | pages [14] -->
(𝑉𝑚𝑎𝑥

<!-- b000625 | prose | pages [14] -->
(6 −1) )

<!-- b000626 | prose | pages [14] -->
𝑆𝑐𝑎𝑙𝑒𝑚𝑎𝑥−𝑆𝑐𝑎𝑙𝑒𝑚𝑖𝑛

<!-- b000627 | prose | pages [14] -->
𝑉

<!-- b000628 | caption | pages [14] -->
Table 7 Calculation of disaster factor

<!-- b000629 | prose | pages [14] -->
M4

<!-- b000630 | prose | pages [14] -->
M5

<!-- b000631 | prose | pages [14] -->
earthquake

<!-- b000632 | prose | pages [14] -->
earthquake

<!-- b000633 | prose | pages [14] -->
Smoke

<!-- b000634 | prose | pages [14] -->
Small fire

<!-- b000635 | prose | pages [14] -->
Disaster type

<!-- b000636 | prose | pages [14] -->
alarm

<!-- b000637 | furniture | pages [14] -->


<!-- b000638 | furniture | pages [14] -->


<!-- b000639 | prose | pages [14] -->
Ⅰ Ⅱ Disaster Grade

<!-- b000640 | prose | pages [14] -->
𝝋𝟎 0 0.625

<!-- b000641 | prose | pages [14] -->
Note:𝑉= 2𝑚/𝑠  𝑉𝑚𝑎𝑥= 5𝑚/𝑠

<!-- b000642 | prose | pages [14] -->
𝑤,𝑘

<!-- b000643 | prose | pages [14] -->
M6

<!-- b000644 | prose | pages [14] -->
M7

<!-- b000645 | prose | pages [14] -->
Gas leak

<!-- b000646 | prose | pages [14] -->
earthquake

<!-- b000647 | prose | pages [14] -->
earthquake

<!-- b000648 | furniture | pages [14] -->


<!-- b000649 | prose | pages [14] -->
Medium fire Heavy fire

<!-- b000650 | prose | pages [14] -->
Stampede

<!-- b000651 | prose | pages [14] -->
Shooting

<!-- b000652 | prose | pages [14] -->
Explosion

<!-- b000653 | prose | pages [14] -->
event

<!-- b000654 | prose | pages [14] -->
event

<!-- b000655 | prose | pages [14] -->
attack Ⅲ Ⅳ Ⅴ

<!-- b000656 | prose | pages [14] -->
1.25 1.875 2.5

<!-- b000657 | prose | pages [14] -->
𝑤,𝑘′

<!-- b000658 | prose | pages [14] -->
𝑤,𝑘+ 𝐿1

<!-- b000659 | prose | pages [14] -->
𝑊= 𝑚𝑎𝑥[(𝐿1

<!-- b000660 | prose | pages [14] -->
𝑇1𝐾

<!-- b000661 | prose | pages [14] -->
𝑉1

<!-- b000662 | prose | pages [14] -->
𝑤,𝑘

<!-- b000663 | prose | pages [14] -->
1 (6 −2) 𝑤,𝑘′) (1 + 𝜑0)]

<!-- b000664 | prose | pages [14] -->
𝑉1

<!-- b000665 | prose | pages [14] -->
𝑤,𝑘′

<!-- b000666 | prose | pages [14] -->
𝑤,𝑘+ 𝐿2

<!-- b000667 | prose | pages [14] -->
𝑊= 𝑚𝑎𝑥[(𝐿2

<!-- b000668 | prose | pages [14] -->
𝑇2𝐾

<!-- b000669 | prose | pages [14] -->
𝑉2

<!-- b000670 | prose | pages [14] -->
𝑤,𝑘

<!-- b000671 | prose | pages [14] -->
1 (6 −3) 𝑤,𝑘′) (1 + 𝜑0)]

<!-- b000672 | prose | pages [14] -->
𝑉2

<!-- b000673 | prose | pages [14] -->
𝑤,𝑘′

<!-- b000674 | prose | pages [14] -->
𝑤,𝑘+ 𝐿3

<!-- b000675 | prose | pages [14] -->
𝑊= 𝑚𝑎𝑥[(𝐿3

<!-- b000676 | prose | pages [14] -->
𝑇3𝐾

<!-- b000677 | prose | pages [14] -->
𝑉3

<!-- b000678 | prose | pages [14] -->
𝑊= 𝑚𝑎𝑥([𝑁𝑘

<!-- b000679 | prose | pages [14] -->
1 (6 −4) 𝑤,𝑘′) (1 + 𝜑0)]

<!-- b000680 | prose | pages [14] -->
𝑉3

<!-- b000681 | prose | pages [14] -->
4

<!-- b000682 | prose | pages [14] -->
𝑊+ β𝑇4,2𝐾

<!-- b000683 | prose | pages [14] -->
𝑊+ γ𝑇4,3𝐾

<!-- b000684 | prose | pages [14] -->
𝑊]

<!-- b000685 | prose | pages [14] -->
𝑤(1 + 𝜑0)𝛿1𝛿2𝑡0] × [α𝑇4,1𝐾

<!-- b000686 | prose | pages [14] -->
𝑤(1 + 𝜑0)𝛿𝑖𝑡0 + 𝑁𝑘

<!-- b000687 | prose | pages [14] -->
𝑇4𝐾

<!-- b000688 | furniture | pages [14] -->


<!-- b000689 | prose | pages [14] -->
) (6 −5)

<!-- b000690 | heading | pages [14] -->
6.2 Model improvement for emergency personnel entering quickly

<!-- b000691 | furniture | pages [14] -->


<!-- b000692 | furniture | pages [15] -->
Team # 1902407                                                    Page 15 of 27

<!-- b000693 | prose | pages [15] -->
When a disaster occurs, there are tourists in the building who are in urgent need of evacuation and staff who assist in evacuation. But professional emergency personnel need to enter the house from outside the building to handle disaster areas and disaster causes, such as firefighters entering the fire, explosion-proof personnel of terrorist attacks, police, etc.

<!-- b000694 | prose | pages [15] -->
The route of emergency personnel entering the building and going to the accident site changes as the evacuation time changes.

<!-- b000695 | prose | pages [15] -->
After the evacuation is completed, the emergency personnel go to the accident site through the shortest route. With the improved Dijkstra, the shortest route can be found very quickly. However, during the evacuation process, traffic monitoring and prediction of each exit, stairs, and walkways are required to find the shortest route.

<!-- b000696 | prose | pages [15] -->
In the process of evacuation, if emergency personnel enter from the evacuation entrance, the evacuation efficiency will inevitably decrease. Therefore, this is a multi- objective planning problem, which is to ensure that the evacuation time is as short as possible, and that the emergency personnel arrive at the designated place as short as possible.

<!-- b000697 | prose | pages [15] -->
We assume the number of emergency personnel is NX; the designated destination is X. 𝑇1𝑁𝑋

<!-- b000698 | prose | pages [15] -->
𝑊 represents the time of the emergency personnel in the designated area

<!-- b000699 | prose | pages [15] -->
𝑊, 𝑇2𝑁𝑋

<!-- b000700 | prose | pages [15] -->
𝑊, 𝑇3𝑁𝑋

<!-- b000701 | prose | pages [15] -->
to move, up and down stairs, and entry and exit in the room respectively.

<!-- b000702 | prose | pages [15] -->
The added objective function is:

<!-- b000703 | prose | pages [15] -->
𝑊+ 𝑇2𝑁𝑋

<!-- b000704 | prose | pages [15] -->
𝑊+ 𝑇3𝑁𝑋

<!-- b000705 | prose | pages [15] -->
𝑊)

<!-- b000706 | prose | pages [15] -->
𝑚𝑖𝑛 𝑇𝑁𝑋= max(𝑇1𝑁𝑋

<!-- b000707 | prose | pages [15] -->
(6 −6)

<!-- b000708 | prose | pages [15] -->
{

<!-- b000709 | prose | pages [15] -->
𝑊+ 𝑇2𝐾

<!-- b000710 | prose | pages [15] -->
𝑊+ 𝑇3𝐾

<!-- b000711 | prose | pages [15] -->
𝑊+ 𝑇4𝐾

<!-- b000712 | prose | pages [15] -->
𝑊) + 𝑀∗𝐹(𝐺𝑁𝑋)]

<!-- b000713 | prose | pages [15] -->
min  𝑇= max[(𝑇1𝐾

<!-- b000714 | prose | pages [15] -->
𝐺𝑁𝑋  represents the entry route of the emergency personnel. 𝐹(𝐺𝑁𝑋) represents the delay time caused by the current route to evacuation.

<!-- b000715 | heading | pages [15] -->
6.2.1 Strategies to avoid emergency personnel conflict with maximum evacuation

<!-- b000716 | prose | pages [15] -->
time

<!-- b000717 | prose | pages [15] -->
The time for emergency evacuation is determined by the latest evacuated person. If it can be made that the emergency personnel entering the building do not affect the evacuation route of the latest evacuated personnel and the emergency personnel's influence time on the evacuation personnel entering the route is less than the evacuation time of the latest evacuation personnel, the evacuation time will not change. ○ 1 Predict the total number of people per exit based on the route of the improved Dijkstra plan. There are D exits, and the time for predicting D exits is 𝑇𝑑1, 𝑇𝑑2, 𝑇𝑑3 … …

<!-- b000718 | prose | pages [15] -->
○ . 2 𝑁𝑋≤∑(𝑇𝐷𝑚𝑎𝑥−𝑇𝑑)𝐶𝑑 𝐷 , 𝑁𝑋𝑑= (𝑇𝐷𝑚𝑎𝑥−𝑇𝑑)𝐶𝑑  𝑁𝑋𝑑 represents the number of emergency personnel entering from the d exit. If 𝑁𝑋>∑(𝑇𝐷𝑚𝑎𝑥−𝑇𝑑)𝐶𝑑 , it means that the latest evacuation time will 𝐷 change.

<!-- b000719 | prose | pages [15] -->
3 Determination of the route. ○ With the improved Dijkstra, enter from D-1 entrances to the path of the intended location.

<!-- b000720 | prose | pages [15] -->
After calculating the shortest path, calculate the time of the escape route person on the shortest path, and reduce its speed to 1/2.

<!-- b000721 | furniture | pages [15] -->


<!-- b000722 | furniture | pages [16] -->
Team # 1902407                                                    Page 16 of 27

<!-- b000723 | prose | pages [16] -->
If the evacuated person on the route has time greater than 𝑻𝑫𝒎𝒂𝒙, then the shortest distance in the line is set to infinity (abandon the line), and the second short line is calculated.

<!-- b000724 | heading | pages [16] -->
6.3 Model improvements under inspection in the Louvre

<!-- b000725 | heading | pages [16] -->
6.3.1 Test result

<!-- b000726 | prose | pages [16] -->
When fires happen in the Louvre and all large multi-level buildings, or for some other reasons, some areas cannot be used, the cessation of use in different regions has different effects on evacuation.

<!-- b000727 | furniture | pages [16] -->


<!-- b000728 | caption | pages [16] -->
Table 8 Test result in different areas

<!-- b000729 | prose | pages [16] -->
Most influential area（X

<!-- b000730 | prose | pages [16] -->
Type of regional

<!-- b000731 | prose | pages [16] -->
Area）

<!-- b000732 | prose | pages [16] -->
impact

<!-- b000733 | prose | pages [16] -->
A channel

<!-- b000734 | prose | pages [16] -->
338 area in ground floor

<!-- b000735 | prose | pages [16] -->
cannot be used

<!-- b000736 | prose | pages [16] -->
A corridor

<!-- b000737 | prose | pages [16] -->
Stairs on the east side of

<!-- b000738 | prose | pages [16] -->
cannot be used

<!-- b000739 | prose | pages [16] -->
the ground floor 408 area

<!-- b000740 | prose | pages [16] -->
An exit cannot

<!-- b000741 | prose | pages [16] -->
Pyramid exit

<!-- b000742 | prose | pages [16] -->
be used

<!-- b000743 | prose | pages [16] -->
Congestion time

<!-- b000744 | prose | pages [16] -->
Evacuation time

<!-- b000745 | prose | pages [16] -->
ratio

<!-- b000746 | prose | pages [16] -->
42.5% 632.5s

<!-- b000747 | prose | pages [16] -->
49.2% 566.0s

<!-- b000748 | prose | pages [16] -->
52.8% 782.0s

<!-- b000749 | furniture | pages [16] -->


<!-- b000750 | caption | pages [16] -->
Figure 13 Evacuation route changes when affected by the disaster channel area

<!-- b000751 | caption | pages [16] -->
Table 9 Optimal route and number of emergency personnel

<!-- b000752 | prose | pages [16] -->
Entry Maximum number

<!-- b000753 | prose | pages [16] -->
Time

<!-- b000754 | prose | pages [16] -->
of emergency

<!-- b000755 | prose | pages [16] -->
personnel

<!-- b000756 | prose | pages [16] -->
Pyramid 240 229s

<!-- b000757 | prose | pages [16] -->
Lions

<!-- b000758 | prose | pages [16] -->
410 370s Gate

<!-- b000759 | furniture | pages [16] -->


<!-- b000760 | prose | pages [16] -->
Route

<!-- b000761 | furniture | pages [16] -->


<!-- b000762 | prose | pages [16] -->
Enter from the pyramid, from the entrance of the Syrian Pavilion to the lower ground floor,

<!-- b000763 | prose | pages [16] -->
into the corridor of 132, from the stairs next to 132 to the ground floor, after 348, 345, 339

<!-- b000764 | prose | pages [16] -->
arrives at 338.

<!-- b000765 | prose | pages [16] -->
Entered by the Lions Gate, the stairs next to the door to the 1st floor, from 719, 708, 717,

<!-- b000766 | furniture | pages [17] -->
Team # 1902407                                                    Page 17 of 27

<!-- b000767 | prose | pages [17] -->
716, 712, 710, 708, 703, arrived at the stairs measured by 703, down to the ground floor,

<!-- b000768 | prose | pages [17] -->
after 408, 347, 345, 339 ,arrived in the 338

<!-- b000769 | prose | pages [17] -->
area.

<!-- b000770 | prose | pages [17] -->
Since Richelieu entry and Carrousel du Louvre entry influence the longest evacuation route, the number of the emergency personnel is 0.

<!-- b000771 | heading | pages [17] -->
6.3.2 Test conclusion

<!-- b000772 | prose | pages [17] -->
Pyramid exits cannot be used, resulting in a 48.3% delay in evacuation. And the total congestion ratio increased by 22.3%. In all channel areas, the ground floor 338 channel area will maximize the evacuation time delay, delay 20%, and the congestion level increased by 3.1%. The evacuation time delay caused by the stairs on the east side of the ground floor 408 area increased the congestion level by 14.3%.

<!-- b000773 | prose | pages [17] -->
Different areas cannot be used, the most affected by the evacuation time is the exit, next are the key channel, and finally the stairs, but the impact on the degree of congestion is that the influence of the stairs is greater than the key channel. This is due to the circular structure and channel of the Louvre. When one side of the channel is not available, the other side of the channel will take longer to move, but less congestion. The Louvre's stairs have an average of 80 meters, so the corridor cannot be used, the main increase is the congestion time.

<!-- b000774 | prose | pages [17] -->
Among the four main entrances and exits of the Louvre, there are fewer evacuated personnel because the Lions Gate is located on both sides and the same floor is not the same as other rooms. Emergency personnel can be arranged to enter more, but accordingly, emergency personnel need to spend more time on the move because they are not connected to the other room. Entering from the pyramid, the impact on evacuation time is minimal, because there are quite a few stairs to choose from to go to the destination.

<!-- b000775 | heading | pages [17] -->
6.4 Model improvements under other large, crowded structures

<!-- b000776 | prose | pages [17] -->
Intensive public buildings of different large groups, including stadiums, concert halls, subway stations, airplane stations, shopping malls, etc. For these public buildings, feature classification is first performed.

<!-- b000777 | heading | pages [17] -->
6.4.1 Large and medium-sized mall

<!-- b000778 | prose | pages [17] -->
The mall is a gathering place for all kinds of businesses. The staff are mainly cleaners responsible for the cleaning and the security personnel at the door. When the disaster suddenly occurs, there is a lack of sufficient staff to evacuate, often relying on emergency personnel entering from the outside. Lack of on-site evacuation and guidance personnel will make the crowd unable to regulate and dispatch when they are congested. Improvements are:

<!-- b000779 | prose | pages [17] -->
1）Use a system such as broadcasting for grooming and control.

<!-- b000780 | furniture | pages [17] -->


<!-- b000781 | prose | pages [17] -->
2）Use the indicator light that can adjust the direction to change the direction of

<!-- b000782 | furniture | pages [17] -->


<!-- b000783 | prose | pages [17] -->
the indicator light and guide the crowd to avoid the congested area.

<!-- b000784 | heading | pages [17] -->
6.4.2 Stadiums, concert halls, cinemas

<!-- b000785 | prose | pages [17] -->
Usually a large open space, people sit next to each other. When they start to escape, people must stand up and wait in line (congested state) to get out quickly, and the

<!-- b000786 | furniture | pages [17] -->


<!-- b000787 | furniture | pages [18] -->
Team # 1902407                                                    Page 18 of 27

<!-- b000788 | prose | pages [18] -->
objective function changes to:

<!-- b000789 | prose | pages [18] -->
𝑊+ 𝑇2𝐾

<!-- b000790 | prose | pages [18] -->
𝑚𝑖𝑛 𝑇= 𝑚𝑎𝑥(𝑇1𝐾

<!-- b000791 | prose | pages [18] -->
𝑊+ 𝑇3𝐾

<!-- b000792 | prose | pages [18] -->
𝑊+ 𝑇4𝐾

<!-- b000793 | prose | pages [18] -->
𝑊+ 𝑇5𝐾

<!-- b000794 | prose | pages [18] -->
𝑊) (6 −7)

<!-- b000795 | prose | pages [18] -->
𝑊 represents the time to stand up and wait in line to leave the seat,𝑇5𝐾

<!-- b000796 | furniture | pages [18] -->


<!-- b000797 | prose | pages [18] -->
𝑇5𝐾

<!-- b000798 | prose | pages [18] -->
𝑊= 𝐿𝑆/𝑉𝑆.

<!-- b000799 | prose | pages [18] -->
𝐿5 represents the farthest distance from the aisle in the audience seat. 𝑉5 represents the speed of evacuation from the seat.

<!-- b000800 | heading | pages [18] -->
6.4.3 Subway station, railway station, airport

<!-- b000801 | prose | pages [18] -->
These sites are considered to be divided into two areas, on-site and off-site, due to security reasons. That is, free activities such as off-site exits; the main venue is the waiting room. In the case of emergency evacuation, although there are exits (train station) and (airplane) outside the open space, tourists may have a front safety accident at the railway station and the plane. Therefore, when building a network model, the exit cannot select the train station and the aircraft boarding gate. When going from the infield to the outfield, the security checkpoint is a must.

<!-- b000802 | prose | pages [18] -->
For those who evacuate in the field, the network model needs to be improved. When using the improved Dijkstra for calculations

<!-- b000803 | furniture | pages [18] -->


<!-- b000804 | caption | pages [18] -->
Table 10 Key section of improved Dijkstra algorithm for calculation

<!-- b000805 | prose | pages [18] -->
For Infield node, Outfield node While the nodes in the inner field in the collection U are not empty

<!-- b000806 | furniture | pages [18] -->


<!-- b000807 | prose | pages [18] -->
Find U to the nearest node v of S

<!-- b000808 | furniture | pages [18] -->


<!-- b000809 | furniture | pages [18] -->


<!-- b000810 | prose | pages [18] -->
Put v in S, U remove v

<!-- b000811 | furniture | pages [18] -->


<!-- b000812 | furniture | pages [18] -->


<!-- b000813 | furniture | pages [18] -->


<!-- b000814 | furniture | pages [18] -->


<!-- b000815 | furniture | pages [18] -->


<!-- b000816 | prose | pages [18] -->
If S cross J is not empty

<!-- b000817 | furniture | pages [18] -->


<!-- b000818 | furniture | pages [18] -->


<!-- b000819 | furniture | pages [18] -->


<!-- b000820 | prose | pages [18] -->
Break

<!-- b000821 | furniture | pages [18] -->


<!-- b000822 | furniture | pages [18] -->


<!-- b000823 | prose | pages [18] -->
End if End for

<!-- b000824 | furniture | pages [18] -->


<!-- b000825 | furniture | pages [18] -->


<!-- b000826 | heading | pages [18] -->
Ⅶ. Model Summary

<!-- b000827 | heading | pages [18] -->
7.1 Advantage

<!-- b000828 | prose | pages [18] -->
(1) Based on the optimal path and dynamic scheduling model, this paper considers the complex distribution of different nodes, studies the influence of different room nodes and stair nodes, further calculates the proportion of congestion time, and improves the accuracy of the model.

<!-- b000829 | prose | pages [18] -->
(2) At the same time of dynamic scheduling on the same floor, real-time scheduling is also implemented for different floors, thus reducing the time of congestion during evacuation.

<!-- b000830 | prose | pages [18] -->
(3) While considering the evacuation of the Louvre, this paper also extends the model to more complex building structures such as shopping malls and office buildings, making the models and algorithms more universal.

<!-- b000831 | heading | pages [18] -->
7.2 Disadvantage

<!-- b000832 | prose | pages [18] -->
(1) The population distribution is relatively uniform when the model is calculated, but the density of the population in real life is different.

<!-- b000833 | furniture | pages [18] -->


<!-- b000834 | furniture | pages [19] -->
Team # 1902407                                                    Page 19 of 27

<!-- b000835 | prose | pages [19] -->
(2) The model was not taken into account when the different emotions of the crowd were affected by the exit.

<!-- b000836 | prose | pages [19] -->
(3) The structure of the Louvre is intricate and complex, and the number of nodes is huge. Therefore, the calculation of the model is relatively complicated and needs to be improved.

<!-- b000837 | furniture | pages [19] -->


<!-- b000838 | heading | pages [19] -->
Ⅷ. Policy and procedural recommendations for the

<!-- b000839 | prose | pages [19] -->
Louvre emergency management

<!-- b000840 | heading | pages [19] -->
8.1 Model deployment requirements

<!-- b000841 | prose | pages [19] -->
(1) Require the Louvre to have management personnel in the important passages in the museum, and to assist in dynamic scheduling during emergency evacuation.

<!-- b000842 | prose | pages [19] -->
(2) Ask the Louvre to use monitoring equipment in real time to view and calculate the flow of people in each room passage, stairs, entrances and exits.

<!-- b000843 | heading | pages [19] -->
8.2 Suggestions for accelerating emergency evacuation

<!-- b000844 | prose | pages [19] -->
(1) Broaden the channel width of the five bottleneck intersections According to our model calculation results, the bottlenecks that limit evacuation mainly include the channel of the lower ground floor of Demon, the left apex of the diamond exit, the entry node of the Richelieu exit, the stairway of the 170th floor of the lower ground floor, and the entry point of the exit of the lion door of the ground floor.

<!-- b000845 | prose | pages [19] -->
(2) Open the other rooms on the 0th floor to the passage of the Lions Gate

<!-- b000846 | furniture | pages [19] -->


<!-- b000847 | caption | pages [19] -->
Figure 14 Set up the new channel of the Lions Gate

<!-- b000848 | prose | pages [19] -->
After the calculation of our model, the lack of access to the Lions Gate at the ground floor caused the Lions Gate to be fully utilized. When the channel of the blue line in the map is opened, the number of evacuations of the pyramid can be transferred to the Lions Gate at most 1,100 people, thus reducing the congestion of the pyramid by 24% and making full use of the Lions Gate.

<!-- b000849 | prose | pages [19] -->
(3) Give priority to adding intersections at the ground floor Due to the lack of direct exits in the Sully Pavilion, evacuators need to re-enter Richelieu, Denon or the underground pyramid to find the exit. If the exit can be increased in the position of the figure, the evacuation time can be reduced from 527.8s to 440s, which is reduced by 16%. At the same time, it can effectively reduce the congestion of the pyramid and the Carrousel du Louvre exit.

<!-- b000850 | furniture | pages [19] -->


<!-- b000851 | furniture | pages [20] -->
Team # 1902407                                                    Page 20 of 27

<!-- b000852 | furniture | pages [20] -->


<!-- b000853 | caption | pages [20] -->
Figure 15 Set up new doors for Sully exit

<!-- b000854 | furniture | pages [20] -->


<!-- b000855 | furniture | pages [20] -->


<!-- b000856 | heading | pages [20] -->
8.3 Entry of emergency personnel and use of other entrances

<!-- b000857 | prose | pages [20] -->
For the entry of emergency personnel, it is necessary to contact the monitoring in the hall. Through the current route planning for escape and the calculation of traffic monitoring, the longest evacuation route and time in the museum are obtained. Two criteria are adopted: 1. The emergency personnel's route does not conflict with the longest evacuation route; 2. The number of emergency personnel cannot cause the evacuation route delay time on the emergency route to exceed the current longest evacuation route time. To ensure that the evacuation time is the shortest, and emergency personnel can reach the designated location as soon as possible. The relevant algorithm has been given, which calculates the optimal route and calculates the optimal number of emergency personnel. According to the calculations that have been carried out, among the four entrances and exits, the intersection that can arrange the most emergency personnel to enter is the Lions Gate, which can arrange up to 400 people, but it takes the longest travel time. The fastest entry point for emergency personnel arriving at a designated location is the entrance to Richelieu, but a maximum of 200 emergency personnel can be arranged and will greatly increase the congestion level of Richelieu.

<!-- b000858 | heading | pages [20] -->
8.4 Different population structures and characteristics

<!-- b000859 | prose | pages [20] -->
For different population structures and characteristics, different ways to reduce congestion time.

<!-- b000860 | prose | pages [20] -->
Details as follows： (1) For those who are easy to fall, special channels will be arranged, equipped with special identification equipment to facilitate people's identification;

<!-- b000861 | prose | pages [20] -->
(2) For people with slower moving speed, when using the scheduling strategy, minimize the scheduling of these people;

<!-- b000862 | prose | pages [20] -->
(3) For some people who are difficult to deal with emergencies, such as children and the elderly, try to let them have passengers who are evacuated as far as possible, but not

<!-- b000863 | furniture | pages [20] -->


<!-- b000864 | furniture | pages [21] -->
Team # 1902407                                                    Page 21 of 27

<!-- b000865 | prose | pages [21] -->
let them go to the places where they are congested;

<!-- b000866 | prose | pages [21] -->
(4) For some people who have language barrier, set up simple and easy indicator diagram; Use general language (including body language); Multiple languages are required.

<!-- b000867 | furniture | pages [21] -->


<!-- b000868 | furniture | pages [21] -->


<!-- b000869 | furniture | pages [21] -->


<!-- b000870 | furniture | pages [21] -->


<!-- b000871 | furniture | pages [21] -->


<!-- b000872 | furniture | pages [21] -->


<!-- b000873 | furniture | pages [21] -->


<!-- b000874 | furniture | pages [21] -->


<!-- b000875 | furniture | pages [21] -->


<!-- b000876 | furniture | pages [21] -->


<!-- b000877 | furniture | pages [21] -->


<!-- b000878 | furniture | pages [21] -->


<!-- b000879 | furniture | pages [21] -->


<!-- b000880 | furniture | pages [21] -->


<!-- b000881 | furniture | pages [21] -->


<!-- b000882 | furniture | pages [21] -->


<!-- b000883 | prose | pages [21] -->
Ⅸ. References

<!-- b000884 | prose | pages [21] -->
[1] 杨建芳, 高岩, 王宏杰. 多层建筑物应急疏散模型和算法[J]. 系统仿真学报, 2014,

<!-- b000885 | prose | pages [21] -->
26(2):267-273. [2] Smith M G . State-dependent queueing models in emergency evacuation networks[J].

<!-- b000886 | prose | pages [21] -->
Transportation Research, Part B (Methodological), 1991, 25(6):373-389. [3] Pursals, Salvador Casadesús, Garzón, Federico Garriga. Optimal building evacuation time

<!-- b000887 | prose | pages [21] -->
considering evacuation routes[J]. European Journal of Operational Research, 2009, 192(2):692-699. [4] Manley M ,  Kim Y S . Modeling emergency evacuation of individuals with disabilities

<!-- b000888 | prose | pages [21] -->
(exitus): An agent-based public decision support system[J]. Expert Systems with Applications, 2012, 39(9):8300-8311. [5] Feng F . A fast flow control algorithm for real-time emergency evacuation in large indoor

<!-- b000889 | prose | pages [21] -->
areas[J]. Fire Safety Journal, 2009, 44(5):732-740. [6] Saadatseresht M ,  Mansourian A ,  Taleai M . Evacuation planning using multiobjective

<!-- b000890 | prose | pages [21] -->
evolutionary optimization approach[J]. European Journal of Operational Research, 2009, 198(1):305-314. [7] Hayakawa Y ,  Mori K ,  Ishida Y , et al. Development of emergency rescue evacuation

<!-- b000891 | prose | pages [21] -->
support system in panic-type disasters[C]// Consumer Communications & Networking Conference. IEEE, 2012.

<!-- b000892 | furniture | pages [21] -->


<!-- b000893 | furniture | pages [21] -->


<!-- b000894 | furniture | pages [21] -->


<!-- b000895 | furniture | pages [21] -->


<!-- b000896 | furniture | pages [21] -->


<!-- b000897 | furniture | pages [21] -->


<!-- b000898 | furniture | pages [22] -->
Team # 1902407                                                    Page 22 of 27

<!-- b000899 | prose | pages [22] -->
Ⅹ. Appendix

<!-- b000900 | heading | pages [22] -->
10.1 Algorithm

<!-- b000901 | heading | pages [22] -->
10.1.1 Same floor scheduling algorithms

<!-- b000902 | prose | pages [22] -->
𝑤(𝑡).

<!-- b000903 | prose | pages [22] -->
Input：The total number of people on the w floor in i place: N𝑖

<!-- b000904 | prose | pages [22] -->
Output：At time t, the number of people evacuated to j at point j

<!-- b000905 | prose | pages [22] -->
𝑤(𝑡) = 0(i=1,2,3…)

<!-- b000906 | prose | pages [22] -->
Initialization： initialize 𝑁𝑖𝑗

<!-- b000907 | prose | pages [22] -->
Process：For i = 1 to M (M is the total number of nodes on the w floor)

<!-- b000908 | prose | pages [22] -->
𝑤(𝑡)

<!-- b000909 | prose | pages [22] -->
N𝑡𝑖= (𝑁𝑖

<!-- b000910 | prose | pages [22] -->
−𝐿𝑖

<!-- b000911 | prose | pages [22] -->
)

<!-- b000912 | prose | pages [22] -->
𝐶𝑖𝑗

<!-- b000913 | prose | pages [22] -->
𝑉𝑆

<!-- b000914 | prose | pages [22] -->
End For For i = 1 to M

<!-- b000915 | prose | pages [22] -->
For j = 1 to M

<!-- b000916 | prose | pages [22] -->
If i ≅j and N𝑡𝑖> N𝑡𝑗

<!-- b000917 | prose | pages [22] -->
𝑤(𝑡)

<!-- b000918 | prose | pages [22] -->
Calculate 𝑁𝑖𝑗

<!-- b000919 | prose | pages [22] -->
𝑤(𝑡)−𝑁𝑖𝑗

<!-- b000920 | prose | pages [22] -->
𝑤(𝑡)

<!-- b000921 | prose | pages [22] -->
𝑁𝑖

<!-- b000922 | prose | pages [22] -->
Which make

<!-- b000923 | prose | pages [22] -->
𝐶𝑖𝑖

<!-- b000924 | prose | pages [22] -->
𝑤(𝑡) < 0

<!-- b000925 | prose | pages [22] -->
If 𝑁𝑖𝑗

<!-- b000926 | prose | pages [22] -->
𝑤(𝑡) = 0

<!-- b000927 | prose | pages [22] -->
𝑁𝑖𝑗

<!-- b000928 | prose | pages [22] -->
Else

<!-- b000929 | prose | pages [22] -->
𝐿𝑖𝑗

<!-- b000930 | prose | pages [22] -->
𝐿𝑖

<!-- b000931 | prose | pages [22] -->
𝑤(𝑡)−(

<!-- b000932 | prose | pages [22] -->
𝑤(𝑡)

<!-- b000933 | prose | pages [22] -->
𝑁𝑗

<!-- b000934 | prose | pages [22] -->
𝑉𝑠+

<!-- b000935 | prose | pages [22] -->
𝑉𝑠)𝐶𝑗

<!-- b000936 | prose | pages [22] -->
𝑁𝑖𝑗

<!-- b000937 | prose | pages [22] -->
𝐿𝑖𝑗

<!-- b000938 | prose | pages [22] -->
𝐿𝑖

<!-- b000939 | prose | pages [22] -->
𝑉𝑠

<!-- b000940 | prose | pages [22] -->
−

<!-- b000941 | prose | pages [22] -->
𝑉𝑠= 𝑀[

<!-- b000942 | prose | pages [22] -->
] +

<!-- b000943 | prose | pages [22] -->
+

<!-- b000944 | prose | pages [22] -->
𝐶𝑗

<!-- b000945 | prose | pages [22] -->
𝐶𝑖𝑗

<!-- b000946 | prose | pages [22] -->
𝐿𝑖𝑗

<!-- b000947 | prose | pages [22] -->
𝑤(𝑡) −𝑁𝑖𝑗

<!-- b000948 | prose | pages [22] -->
𝑤(𝑡+ 1) = 𝑁𝑖

<!-- b000949 | furniture | pages [22] -->


<!-- b000950 | prose | pages [22] -->
𝑁𝑖

<!-- b000951 | prose | pages [22] -->
𝑤(𝑡) −𝑐𝑖

<!-- b000952 | prose | pages [22] -->
𝑉𝑠

<!-- b000953 | prose | pages [22] -->
𝑤(𝑡) −𝑐𝑗𝐿𝑖𝑗

<!-- b000954 | prose | pages [22] -->
𝑤(𝑡+ 1) = 𝑁𝑗

<!-- b000955 | prose | pages [22] -->
𝑁𝑗

<!-- b000956 | prose | pages [22] -->
End If End If End For End For

<!-- b000957 | prose | pages [22] -->
𝑤(𝑡) + 𝑁𝑖𝑗

<!-- b000958 | furniture | pages [22] -->


<!-- b000959 | prose | pages [22] -->
𝑉𝑠

<!-- b000960 | heading | pages [22] -->
10.1.2 Different floor scheduling algorithms

<!-- b000961 | prose | pages [22] -->
𝑤(𝑡)

<!-- b000962 | prose | pages [22] -->
Input：The number of people waiting for the stairs at the stairway of all floors at t time : ∑N𝑖

<!-- b000963 | prose | pages [22] -->
𝑤(𝑡)

<!-- b000964 | prose | pages [22] -->
Output：Number of people dispatched to another stairway at a certain stairway at time t : N𝑖𝑗

<!-- b000965 | prose | pages [22] -->
𝑤(𝑡) = 0(i,j=1,2,3…)

<!-- b000966 | prose | pages [22] -->
Initialization：(1) initialize t=1,N𝑖𝑗

<!-- b000967 | prose | pages [22] -->
(2) initialize q Process：For i = 1 to M (M is the number of the stairs)

<!-- b000968 | prose | pages [22] -->
𝑤(𝑡)

<!-- b000969 | prose | pages [22] -->
𝑇𝑖= ∑𝑁𝑖

<!-- b000970 | furniture | pages [22] -->


<!-- b000971 | prose | pages [22] -->
𝐶𝑖

<!-- b000972 | prose | pages [22] -->
End For For i = 1 to M

<!-- b000973 | prose | pages [22] -->
For j = 1 to M

<!-- b000974 | prose | pages [22] -->
𝐿𝑖𝑗

<!-- b000975 | prose | pages [22] -->
(T𝑖−𝑇𝑗)𝐶𝑖

<!-- b000976 | prose | pages [22] -->
If i ≅j and T𝑖> 𝑇𝑗 and T𝑖−𝑇𝑗>

<!-- b000977 | furniture | pages [22] -->


<!-- b000978 | furniture | pages [22] -->


<!-- b000979 | prose | pages [22] -->
𝑉𝑠+

<!-- b000980 | prose | pages [22] -->
𝐶𝑗

<!-- b000981 | furniture | pages [23] -->
Team # 1902407                                                    Page 23 of 27

<!-- b000982 | prose | pages [23] -->
𝑤(𝑡) = (T𝑖−𝑇𝑗)𝐶𝑖

<!-- b000983 | furniture | pages [23] -->


<!-- b000984 | prose | pages [23] -->
N𝑖𝑗

<!-- b000985 | prose | pages [23] -->
𝐶𝑗

<!-- b000986 | prose | pages [23] -->
𝑐𝑖𝐿𝑖𝑗

<!-- b000987 | prose | pages [23] -->
𝑤(𝑡) −N𝑖𝑗

<!-- b000988 | prose | pages [23] -->
N𝑖,𝑤(𝑡+ 1) = N𝑖

<!-- b000989 | prose | pages [23] -->
𝑤(𝑡) −

<!-- b000990 | furniture | pages [23] -->


<!-- b000991 | prose | pages [23] -->
(𝑤−1)𝑉𝑠

<!-- b000992 | prose | pages [23] -->
𝑐𝑗𝐿𝑖𝑗

<!-- b000993 | prose | pages [23] -->
𝑤(𝑡) −N𝑖𝑗

<!-- b000994 | prose | pages [23] -->
N𝑗;𝑤(𝑡+ 1) = N𝑗

<!-- b000995 | prose | pages [23] -->
End If End For End For

<!-- b000996 | prose | pages [23] -->
𝑤(𝑡) −

<!-- b000997 | furniture | pages [23] -->


<!-- b000998 | prose | pages [23] -->
(𝑤−1)𝑉𝑠

<!-- b000999 | heading | pages [23] -->
10.1.3 Algorithm of evacuation models for avoiding hazardous areas

<!-- b001000 | prose | pages [23] -->
Input：Disaster occurrence point X，Range of disaster is X area Network G，Starting node S，Stairway node R∗，End point set D，The number of people

<!-- b001001 | furniture | pages [23] -->


<!-- b001002 | furniture | pages [23] -->


<!-- b001003 | prose | pages [23] -->
in the stairway C𝑅𝑖. Output：dist{x} Optimal route from the starting node S to the destination Initialization：(1)initialize S={s}，V={other nodes}

<!-- b001004 | prose | pages [23] -->
(2) if<U,S> set has edges connected, its weight is assigned. Otherwise the assignment is positive infinity Process：For i = 1 to length(R∗)

<!-- b001005 | prose | pages [23] -->
∗∗y

<!-- b001006 | prose | pages [23] -->
𝐴𝑟𝑒𝑎= C𝑅𝑖

<!-- b001007 | prose | pages [23] -->
If S ∉Area

<!-- b001008 | prose | pages [23] -->
R∗′ = R∗ 𝑟𝑒𝑚𝑜𝑣𝑒 R𝑖 𝑆= 𝑆 𝑟𝑒𝑚𝑜𝑣𝑒 R𝑖 End If End For For w to high(Floor difference between starting point and exit)

<!-- b001009 | prose | pages [23] -->
While N(w) ≠0(The number of nodes in the w floor is not zero)

<!-- b001010 | prose | pages [23] -->
Find the node V closest to S in U If  V is not in X area

<!-- b001011 | prose | pages [23] -->
𝑈= 𝑈 𝑟𝑒𝑚𝑜𝑣𝑒 ; 𝑆= 𝑆 𝑟𝑒𝑚𝑜𝑣𝑒 𝑆

<!-- b001012 | prose | pages [23] -->
𝑘 in S and S ∩D = ∅)or(S ∩D = ∅)

<!-- b001013 | prose | pages [23] -->
If (all R𝑤

<!-- b001014 | prose | pages [23] -->
Break End If End While End For

<!-- b001015 | heading | pages [23] -->
10.2 Louvre group statistics

<!-- b001016 | caption | pages [23] -->
Table 1 Proportion of various tourists

<!-- b001017 | prose | pages [23] -->
Disabled

<!-- b001018 | furniture | pages [23] -->


<!-- b001019 | prose | pages [23] -->
Elderly Children

<!-- b001020 | prose | pages [23] -->
Proportion 11% 5%

<!-- b001021 | furniture | pages [23] -->


<!-- b001022 | prose | pages [23] -->
Pregnant

<!-- b001023 | prose | pages [23] -->
Language

<!-- b001024 | prose | pages [23] -->
Normal

<!-- b001025 | prose | pages [23] -->
woman

<!-- b001026 | prose | pages [23] -->
barrier

<!-- b001027 | furniture | pages [23] -->


<!-- b001028 | prose | pages [23] -->
2.5% 1% 53% 27.5%

<!-- b001029 | caption | pages [23] -->
Table 2 Speed of different areas

<!-- b001030 | prose | pages [23] -->
Room channel moving

<!-- b001031 | furniture | pages [23] -->


<!-- b001032 | prose | pages [23] -->
Upstairs and

<!-- b001033 | prose | pages [23] -->
downstairs

<!-- b001034 | furniture | pages [23] -->


<!-- b001035 | prose | pages [23] -->
Entry and exit

<!-- b001036 | prose | pages [23] -->
speed

<!-- b001037 | furniture | pages [24] -->
Team # 1902407                                                    Page 24 of 27

<!-- b001038 | prose | pages [24] -->
m/s

<!-- b001039 | prose | pages [24] -->
Normal speed 0.25

<!-- b001040 | prose | pages [24] -->
Congestion speed 0.0625

<!-- b001041 | heading | pages [24] -->
10.3 Detailed Louvre area number

<!-- b001042 | furniture | pages [24] -->


<!-- b001043 | prose | pages [24] -->
m/s

<!-- b001044 | prose | pages [24] -->
2 2

<!-- b001045 | prose | pages [24] -->
0.5 0.6

<!-- b001046 | furniture | pages [24] -->


<!-- b001047 | furniture | pages [24] -->


<!-- b001048 | furniture | pages [24] -->


<!-- b001049 | furniture | pages [25] -->
Team # 1902407                                                    Page 25 of 27

<!-- b001050 | furniture | pages [25] -->


<!-- b001051 | furniture | pages [25] -->


<!-- b001052 | heading | pages [25] -->
10.4 Evacuation network diagrams

<!-- b001053 | prose | pages [25] -->
2nd floor

<!-- b001054 | furniture | pages [25] -->


<!-- b001055 | furniture | pages [25] -->


<!-- b001056 | furniture | pages [25] -->


<!-- b001057 | furniture | pages [26] -->
Team # 1902407                                                    Page 26 of 27

<!-- b001058 | furniture | pages [26] -->


<!-- b001059 | prose | pages [26] -->
1st floor

<!-- b001060 | furniture | pages [26] -->


<!-- b001061 | prose | pages [26] -->
Ground floor

<!-- b001062 | furniture | pages [26] -->


<!-- b001063 | prose | pages [26] -->
Lower ground floor

<!-- b001064 | furniture | pages [26] -->


<!-- b001065 | furniture | pages [27] -->
Team # 1902407                                                    Page 27 of 27

<!-- b001066 | prose | pages [27] -->
Napoleon Hall

<!-- b001067 | furniture | pages [27] -->


<!-- b001068 | furniture | pages [27] -->

