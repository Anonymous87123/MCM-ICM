# P-D-2019-1902407-b8153b5d

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only 1902407 T1 ________________ F1 ________________

<!-- b000003 | front_matter | pages [1] -->
T2 ________________ F2 ________________

<!-- b000004 | front_matter | pages [1] -->
T3 ________________ Problem Chosen F3 ________________ D T4 ________________ F4 ________________

<!-- b000005 | front_matter | pages [1] -->
2019

<!-- b000006 | prose | pages [1] -->
MCM/ICM Summary Sheet.

<!-- b000007 | prose | pages [1] -->
In case of the terrorist attacks in France, the Louvre needed emergency evacuation plans to avoid danger. This paper first establishes the goal programming model with the minimum total evacuation time to make sure that people in building can be evacuated safely and quickly. The model divides the evacuation time into the moving phase of the room channel, the up and down building phase, the entry and exit phase, and the accident occurrence phase. By optimizing each of these stages, the goal of minimum total time is achieved. In order to achieve optimal path, we improve the Dijkstra algorithm and find the most efficient route from each room to the exit. In addition, we propose a dynamic scheduling algorithm between the same floor and a dynamic scheduling algorithm between different floors to solve the congestion problem according to the goal planning. Furthermore, we have designed targeted response strategies for different characteristics of vulnerable groups to reduce accidents. In our model, we have obtained the optimal evacuate path of the Louvre and the weak bottleneck location. The emergency evacuation completion time of the Louvre is 527s, and the congestion time is 37.5%. Compared with the random method, we reduced the time by 39.3%, reduced the congestion by 24% and reduced the injury of 60.69%. Secondly, this paper incorporates the disaster factors into the model, which further improves the adaptability of the model to different disasters and also considers the arrangement of emergency personnel entering the building. The maximum number of emergency personnel that can be entered at each intersection can be obtained without affecting the maximum evacuation time.

<!-- b000008 | prose | pages [1] -->
Based on the model, we calculated the maximum number of 410 emergency personnel and 370s of the optimal route through the Lions Gate exit, while through the Richelieu is about 229s but the maximum number was 240. In addition, the model proposed in paper also explores other large-scale multi-storey public buildings and gives model improvement plans. Finally, in response to the conclusions of the model, this paper proposes to Louvre managers the plan to speed up evacuation, arrange emergency personnel, increase exits, and target vulnerable groups.

<!-- b000009 | furniture | pages [2] -->
Team # 1902407                                                    Page 2 of 27

<!-- b000010 | heading | pages [2] -->
I. Introduction

<!-- b000011 | heading | pages [2] -->
1.1 Problem Introduction

<!-- b000012 | prose | pages [2] -->
Helped design the evacuation plan for the Louvre in Paris, France, the goal of evacuation is to allow all groups of tourists to leave the building as quickly and safely as possible, while allowing emergency personnel to enter the building as soon as possible. However, the complex structure of venues and complex crowd structure make it more difficult to evacuate in an emergency. For example, different groups of organizations (tour groups, disabled people) evacuation processing. After the model is developed, validate the model and discuss how to implement it. Based on the results of the work, recommendations are made on policies and procedures for the emergency management of the Louvre, how to adjust and implement the model for other large congested structures, and how the model performs under different disasters.

<!-- b000013 | heading | pages [2] -->
1.2 Problem Analysis

<!-- b000014 | prose | pages [2] -->
At evacuation exits, we need to be aware of potential bottlenecks in exit movement. The Louvre museum in Paris, France, has complex building structure and diverse tourists, which should be reflected in the emergency evacuation model. The total number of actual exit points in the Louvre is known only to the staff. Although these additional exits can be used by the public, the safety of these exits cannot be guaranteed. Therefore, the reasonable use of these exits in the model should be considered. This model should be universal in order to facilitate adjustment and implementation for other large crowding structures.

<!-- b000015 | heading | pages [2] -->
1.3 Views of our work

<!-- b000016 | caption | pages [2] -->
Figure 1  summary of our work

<!-- b000017 | furniture | pages [3] -->
Team # 1902407                                                    Page 3 of 27

<!-- b000018 | prose | pages [3] -->
Ⅱ. General Assumption

<!-- b000019 | prose | pages [3] -->
⚫   In the event of a disaster, people in the building can be informed of the dangers in a timely and simultaneous manner and immediately begin evacuation operations.

<!-- b000020 | prose | pages [3] -->
The evacuation emergency personnel can start the evacuation operation in ⚫ time, and can obtain the current evacuation status of the current population through electronic devices.

<!-- b000021 | prose | pages [3] -->
⚫   The evacuated masses listened to the command of evacuation emergency personnel.

<!-- b000022 | prose | pages [3] -->
Ⅲ. Notations Description

<!-- b000023 | heading | pages [3] -->
Notation

<!-- b000024 | prose | pages [3, 4] -->
Description S he node of the path (all exhibition halls, intersections and stairs) D Exit node (all exits) E{𝐞 𝒊𝒋} The set of paths between nodes I and j 𝑪𝒊𝒋 Side 𝑒𝑖𝑗 of the maximum number of people per unit time 𝑪𝒊𝒊 The maximum number of passageways per unit time of node i 𝑵𝒘 The number of people passing the floor w 𝑾 The time of the last person escapes when the 𝑻𝟏𝑲 starting point is on the w floor and taking the k path 𝑾 The time of escaping from the stairs when the 𝑻𝟐𝑲 starting point is on the w floor and taking the k path 𝑾 The time of escaping from the exits when the 𝑻𝟑𝑲 starting point is on the w floor and taking the k path 𝑾 Evacuation delays caused by emergencies and 𝑻𝟒𝑲 special groups (elderly, children, pregnant women and disabled) Ⅵ. Model Design

<!-- b000025 | furniture | pages [4] -->
Team # 1902407                                                    Page 4 of 27

<!-- b000027 | heading | pages [4] -->
4.1 Establish evacuation network

<!-- b000028 | prose | pages [4] -->
Set all exhibition halls, node are 𝑆{𝑆1, 𝑆2, 𝑆3, 𝑆4 … };

<!-- b000029 | prose | pages [4] -->
Intersections, door (narrow channel) and stairs are 𝑅{𝑅1, 𝑅2,𝑅3, 𝑅4 … }.

<!-- b000030 | prose | pages [4] -->
Specifically, when the node 𝑅𝑥 represents a stair node, 𝑅𝑥 𝑤 represents the node of the stair at the w floor.

<!-- b000031 | prose | pages [4] -->
All exits are exit nodes 𝐷{𝐷1, 𝐷2,𝐷3, 𝐷4 … }. The set of paths between node i and j is edge set E{𝑒 𝑖𝑗}, and the nearest node in the building can be reached by path without passing through the connecting edge of other two nodes.

<!-- b000032 | prose | pages [4] -->
Network: G={(S,R,D),E}

<!-- b000033 | caption | pages [4] -->
Figure 2 Example of evacuation network

<!-- b000034 | heading | pages [4] -->
4.2 Optimal Basic Model

<!-- b000035 | prose | pages [4] -->
The goal of emergency evacuation of large multi-story public buildings is to evacuate personnel within the building as quickly as possible. Therefore, the goal of model optimization is to minimize the time that the last evacuated person flees the building.

<!-- b000036 | prose | pages [4] -->
We divide the escape time into the indoor escape phase, the up and down stairs phase, the entry and exit phase, and the escape time delay caused by sudden events such as falls and trampling on the vulnerable groups with a certain probability in the above three stages.

<!-- b000037 | caption | pages [4] -->
Figure 3  Room movement    Figure 4 Staircase movement  Figure 5 Exit movement

<!-- b000038 | prose | pages [4] -->
𝑊+ 𝑇2𝐾 𝑊+ 𝑇3𝐾 𝑊+ 𝑇4𝐾 𝑊) (4 −1) minT = 𝑚𝑎𝑥(𝑇1𝐾 s.t.

<!-- b000039 | prose | pages [4] -->
𝑤,𝑘′ 𝑤,𝑘 𝑊= 𝑚𝑎𝑥(𝐿1 𝑤,𝑘+ 𝐿1 (4 −2) 𝑇1𝐾 𝑤,𝑘′) 𝑉1 𝑉1

<!-- b000040 | prose | pages [4, 5] -->
𝑤,𝑘′ 𝑤,𝑘 𝑊= 𝑚𝑎𝑥(𝐿2 𝑤,𝑘+ 𝐿2 (4 −3) 𝑇2𝐾 𝑤,𝑘′) 𝑉2 𝑉2 𝑤,𝑘′ 𝑤,𝑘 𝑊= max (𝐿3 𝑤,𝑘+ 𝐿3 (4 −4) 𝑇3𝐾 𝑤,𝑘′) 𝑉3 𝑉3

<!-- b000041 | furniture | pages [5] -->
Team # 1902407                                                    Page 5 of 27

<!-- b000043 | prose | pages [5] -->
4 𝑊= max ([𝑁𝑘 𝑊+ β𝑇4,2𝐾 𝑊+ γ𝑇4,3𝐾 𝑊] 𝑤𝛿𝑖𝑡0 + 𝑁𝑘 𝑤𝛿1𝛿2𝑡0] × [α𝑇4,1𝐾 (4 −5) 𝑇4𝐾 )

<!-- b000044 | prose | pages [5] -->
𝑊≥𝑁𝑤,𝑘  (𝑖, 𝑗𝜖𝑘) (4 −6) 𝐶𝑖𝑗∗𝑇1𝐾 𝑊≥𝑁𝑤,𝑘  (𝑖, 𝑗𝜖𝑘) (4 −7) 𝐶𝑖𝑗∗𝑇2𝐾

<!-- b000045 | prose | pages [5] -->
𝑤,𝑘+ 𝑁𝑆2 𝑤,𝑘+ 𝑁𝑆3 𝑤,𝑘+ ⋯  (𝑆1, 𝑆2, 𝑆3𝜖𝑘) 𝑁𝑤,𝑘= 𝑁𝑆1 (4 −8)

<!-- b000046 | prose | pages [5] -->
𝑤,𝑘, 𝑁𝑆2 𝑤,𝑘. 𝑁𝑆3 𝑤,𝑘… ≥0 (4 −9) 𝑁𝑆1

<!-- b000047 | prose | pages [5] -->
Due to the different scenarios, different groups of people moving speed, we need to separate the indoor escape phase, the upper and lower stairs phases, and the entry and exit phases, respectively, using 𝑉1,𝑠 𝑤,𝑘  indicates its normal moving speed, 𝑤,𝑘, 𝑉2,𝑠 𝑤,𝑘, 𝑉3,𝑖 𝑤,𝑘 indicates the moving distance of the three stages at normal moving speed. 𝑤,𝑘,𝐿2 𝑤,𝑘,𝐿3 𝐿1 W stands for different floors and k stands for route.

<!-- b000048 | prose | pages [5] -->
In each phase, the speed is divided into normal moving speed and moving speed during congestion due to possible congestion. The congestion rate of the indoor escape phase, the upper and lower stairs phases, and the entry and exit phases is expressed as 𝑤,𝑘′, the corresponding total length of congestion is 𝐿1 𝑤,𝑘′,𝑉2,𝑠 𝑤,𝑘′,𝑉3,𝑖 𝑤,𝑘′,𝐿2 𝑤,𝑘′,𝐿3 𝑤,𝑘′. 𝑉1,𝑠 Although it is more convenient to replace these two variables with time, since the evacuation model needs to consider different characteristics of the population, such as the old and the weak, and these people have significant differences in the speed of movement, the speed is required. This situation will be discussed in the following.

<!-- b000049 | heading | pages [5] -->
4.3 Optimized for moving and exit

<!-- b000050 | prose | pages [5] -->
The indoor escape phase and the exit phase can be optimized using the same method.

<!-- b000051 | prose | pages [5] -->
𝑤,𝑘′ 𝑤,𝑘 𝑚𝑖𝑛𝑇1 ⟹𝑚𝑎x(𝐿1 𝑤,𝑘+ 𝐿1 (4 −10) 𝑤,𝑘′) 𝑉1 𝑉1

<!-- b000052 | prose | pages [5] -->
𝑤,𝑘′ 𝑤,𝑘 𝑚𝑖𝑛𝑇3 ⟹𝑚𝑎𝑥(𝐿3 𝑤,𝑘+ 𝐿3 (4 −11) 𝑤,𝑘′) 𝑉3 𝑉3 Since the speed of movement of a person can be given,

<!-- b000053 | prose | pages [5] -->
𝑤,𝑘′)                                                  (4 −12) 𝑤 𝑤,𝑘+ 𝐿 𝐿𝑡𝑜𝑡𝑎𝑙 = ∑(𝐿

<!-- b000054 | prose | pages [5] -->
𝑚𝑖𝑛𝑇  is equivalent to

<!-- b000055 | prose | pages [5] -->
𝑤,𝑘′)                                     (4 −13) 𝑤 𝑤,𝑘+ 𝐿 𝑚𝑖𝑛∑𝐿𝑡𝑜𝑡𝑎𝑙 = min (𝐿

<!-- b000056 | prose | pages [5, 6] -->
According to the principle of proximity, min 𝐿𝑆′ 𝑤,𝑘represent the smallest queuing congestion. Assume 𝑁𝑖𝑗 𝑤 represents the total visitors flow rate of the node i on the w floor. 𝑁𝑖 𝑤= 𝑁𝑤,𝑘1 + 𝑁𝑤,𝑘2 + 𝑁𝑤,𝑘3 + ⋯, satisfy 𝑘1 ∩𝑘2 ∩𝑘3 ∩… = 𝑖 𝑤 𝑤,𝑘 (𝑁𝑖 −𝐿𝑖 ) = 𝐿 (4 −14) 𝐶𝑖𝑗 𝑉𝑠 𝑉𝑆′ 𝑉𝑠  represents the normal walking speed, 𝑉𝑆′  represents the speed of crowd evacuation. Since the escape speed of the crowd is not uniform, the average speed is adopted here.

<!-- b000057 | furniture | pages [6] -->
Team # 1902407                                                    Page 6 of 27

<!-- b000059 | prose | pages [6] -->
we can get 𝑤 𝑉𝑆′ (𝑁𝑖 −𝐿𝑖 (4 −15) ) = 𝐿𝑆′ 𝐶𝑖𝑗 𝑉𝑠 In a known congestion paths,𝑉𝑆′，𝐿𝑖 and 𝑉𝑠 for a fixed amount, therefore we should shorten 𝑁𝑖 𝑤 𝑤,𝑘′ ⇒𝑚𝑖𝑛 𝑁𝑖 , , , , , 𝑤                                                       (4 −16) 𝑚𝑖𝑛 𝐿 , , , , , , , , , , , , , , , , s.t.

<!-- b000060 | prose | pages [6] -->
∑𝑁𝑤= 𝑁𝑡𝑜𝑡𝑎𝑙 (4 −17)

<!-- b000061 | prose | pages [6] -->
𝑤= 𝑁𝑧1 𝑤+ 𝑁𝑧2 𝑤+ 𝑁𝑧3 𝑤+ ⋯ (4 −18) 𝑁𝑖

<!-- b000062 | heading | pages [6] -->
4.4 Improved Dijkstra for optimal path

<!-- b000063 | prose | pages [6] -->
Dijkstra is one of the best and universal ways to find the best path, time complexity is O(𝑛2). Dijkstra can improve efficiency for the shortest escape route for large multi- storey buildings.

<!-- b000064 | prose | pages [6] -->
Improved direction:

<!-- b000065 | prose | pages [6] -->
1 Since multi-storey buildings are evacuated, most of the nodes need to go up and ○ down the stairs through a certain staircase. Therefore, for floors without stairs on this floor, the stairs in the exit direction are the only way. We assume 𝑅∗{ 𝑅1 ∗……} is a ∗，𝑅2 necessary set of stairs.

<!-- b000066 | prose | pages [6] -->
2 Due to the flow restriction of the stairway, although some routes are the shortest, ○ they are not optimal due to congestion queues. Therefore, when using Dijkstra to find the shortest path, you should avoid the location that may be congested. Therefore, the necessary set of stairs should be reduced to 𝑅∗′{ 𝑅1 ∗……}. ∗，𝑅2

<!-- b000067 | caption | pages [6] -->
Table 1  Improved Dijkstra algorithm for optimal path

<!-- b000068 | prose | pages [6, 7] -->
Input：Network G，Starting node S，Stairway node 𝐑∗，End point set D，Number of people in the stairway 𝐂𝑹𝒊, Unit Coverage Area y. Output： Optimal route from the starting node S to the destination Initialization：(1)initialize S={s}，V={other nodes} (2) If <U,S> set has edges connected, its weight is assigned, otherwise the value is positive infinity. Process：For 𝐢= 𝟏 to length(𝐑∗) ∗∗𝐲 𝑨𝒓𝒆𝒂= 𝐂𝑹𝒊 If 𝐒∉𝐀𝐫𝐞𝐚 𝐑∗′ = 𝐑∗ 𝒓𝒆𝒎𝒐𝒗𝒆 𝐑𝒊 𝑺= 𝑺 𝒓𝒆𝒎𝒐𝒗𝒆 𝐑𝒊 End If End For For w to high(Floor difference between starting point and exit) While 𝐍(𝐰) ≠𝟎(The number of nodes in the w floor is not zero) Find node V closest to S in U 𝑼= 𝑼 𝒓𝒆𝒎𝒐𝒗𝒆 𝐔 𝑺= 𝑺 𝒓𝒆𝒎𝒐𝒗𝒆 𝑺 𝒌 in S and 𝐒∩𝐃= ∅)or(𝐒∩𝐃= ∅) If (all 𝐑𝒘 Break End If End While End For

<!-- b000069 | furniture | pages [7] -->
Team # 1902407                                                    Page 7 of 27

<!-- b000071 | heading | pages [7] -->
4.5 Optimized for the Same floor congestion

<!-- b000072 | prose | pages [7] -->
Although the improved Dijkstra can avoid congestion to some extent and find the optimal path, in the event of a sudden disaster, visitors may still be in a hurry and choose the "shortest" path to escape and cause congestion. At this point, the staff is required to perform dynamic scheduling. The overall purpose of the scheduling strategy is to minimize congestion time (to be faster evacuation). When people on all routes gather at one point, the number of people in the location is

<!-- b000073 | prose | pages [7] -->
𝑤,𝑘 𝑤= ∑𝑁𝑖 (4 −19) 𝑁𝑖

<!-- b000074 | prose | pages [7] -->
The scheduling scheme is specifically to guide a part of the crowd at the congestion location to a relatively smooth place. The specific objective function and the conditions are as follows:

<!-- b000075 | prose | pages [7] -->
𝑤 (𝑁𝑖 −𝐿𝑖 (4 −20) 𝑚𝑖𝑛∑ ) 𝐶𝑖𝑗 𝑉𝑠 𝑖,𝑗 s.t.

<!-- b000076 | prose | pages [7] -->
𝑤= 𝑁𝑧𝑖 𝑤+ 𝑁𝑧2 𝑤+ 𝑁𝑧3 𝑤+ ⋯ (4 −21) 𝑁𝑖 𝑤 + 𝐿𝑖𝑗 𝑁𝑖 > 𝐿𝑖 1, 𝐶𝑖𝑗 𝑉𝑠 𝑉𝑠 (4 −22) M = 𝑤 + 𝐿𝑖𝑗 𝑁𝑖 ≤𝐿𝑖 { 0, 𝐶𝑖𝑗 𝑉𝑠 𝑉𝑠

<!-- b000077 | prose | pages [7] -->
𝑉𝑠+ 𝐿𝑖𝑗 𝑤−(𝐿𝑖 𝑁𝑖 𝑉𝑠)𝐶𝑖𝑗 𝑤−∑𝑁𝑖𝑧 𝑤 𝑤 + 𝐿𝑖𝑗 𝑁𝑖 −𝐿𝑖 ] + 𝑁𝑖𝑧 (4 −23) > max {M [ } 𝐶𝑖𝑗 𝑉𝑠 𝐶𝑖𝑗 𝐶𝑖𝑗 𝑉𝑠

<!-- b000078 | prose | pages [7] -->
After successful scheduling, 𝑁𝑖′𝑤= 𝑁𝑖 𝑤−𝑁𝑖𝑧 𝑤 (4 −24) 𝑁𝑗′𝑤= 𝑁𝑗 𝑤−𝑁𝑗𝑧 𝑤 (4 −25) The algorithm for scheduling strategy in the same floor is shown in the appendix.

<!-- b000079 | caption | pages [7] -->
Figure 6 example of scheduling strategy in the same floor

<!-- b000080 | furniture | pages [8] -->
Team # 1902407                                                    Page 8 of 27

<!-- b000081 | heading | pages [8] -->
4.6 Optimized between floors

<!-- b000082 | prose | pages [8] -->
That is, scheduling optimization of the same w floor can reduce congestion time.

<!-- b000083 | prose | pages [8] -->
Secondly, there is scheduling among different floors, and there is a scramble for stairs among different floors， So we assume the objective function is

<!-- b000084 | prose | pages [8] -->
𝑊 (4 −26) 𝑚𝑖𝑛∑𝑇2𝐾 𝑤

<!-- b000085 | prose | pages [8] -->
𝑊 (4 −27) ∑𝑇2𝐾 = ∑𝑇𝑓2 𝑤 𝐹 s.t.

<!-- b000086 | prose | pages [8] -->
𝑤3 + ⋯ 𝑤1 + 𝑁𝑖 𝑤2 + 𝑁𝑖 𝑇𝐹𝑖2 = 𝑁𝑖 (4 −28) 𝐶𝑖2

<!-- b000087 | prose | pages [8] -->
( 𝑇𝐹𝑖2 −𝑇𝐹𝑖𝑗)𝐶𝑖 ∀  𝑇𝐹𝑖2 −𝑇𝐹𝑖𝑗< 𝐿𝑖𝑗 (4 −29) + 𝑉𝑠 𝐶𝑗

<!-- b000088 | prose | pages [8] -->
𝑇𝑓𝑖≥0 Therefore, the influence on the scheduling between floors is 𝑤(𝑤−1) 𝑚𝑖𝑛∑(𝑁𝑖 −𝐿𝑖 (4 −30) ) 𝐶𝑖 𝑉𝑠 𝑖 s.t.

<!-- b000089 | prose | pages [8] -->
𝑤= 𝑁𝑧1 𝑤+ 𝑁𝑧2 𝑤+ 𝑁𝑧3 𝑤+ ⋯                                         (4 −31) 𝑁𝑖 𝑉𝑠+ 𝐿𝑖𝑗 𝑤(𝑤−1) −(𝐿𝑖 𝑉𝑠) 𝐶𝑗 𝑁𝑗 𝑤−∑𝑁𝑖2 𝑤) 𝑤(𝑤−1) (𝑤−1)(𝑁𝑖 + 𝐿𝑖𝑗 −𝐿𝑖 ] + 𝑁𝑖2 } (4 −32) > 𝑚𝑎𝑥{𝑀[ 𝐶𝑖𝑖 𝑉𝑠 𝐶𝑗 𝐶𝑖𝑗 𝑉𝑠

<!-- b000090 | prose | pages [8] -->
The algorithm for scheduling strategy between different floors is shown in the appendix.

<!-- b000091 | caption | pages [8] -->
Figure 7 Example of scheduling strategy between different floors

<!-- b000092 | heading | pages [8] -->
4.7 Special crowd handling and emergency optimization

<!-- b000093 | prose | pages [8] -->
The objective function is 4 𝑊= [𝑁𝑘 𝑊+ 𝛽𝑇4,2𝐾 𝑊+ 𝛾𝑇4,3𝐾 𝑊] (4 −33) 𝑤𝛿𝑖𝑡0 + 𝑁𝑘 𝑤𝛿1𝛿2𝑡0] × [𝛼𝑇4,1𝐾 𝑚𝑖𝑛𝑇4𝐾 We explain the above function, 𝛿1 represents the probability of falling while fleeing in a particular population; 𝛿2 represents the probability of a stampede after a fall in a particular crowd;

<!-- b000094 | prose | pages [8, 9] -->
𝑾 represents the ratio of the queue time of all people walking and congested to the 𝑻𝟒,𝟏𝑲 total walking time;  𝑻𝟒,𝟐𝑲 𝑾 represents the ratio of the queue time of all the crowds up and down the stairs to the total stairs time;  𝑻𝟒,𝟑𝑲 𝑾 represents the ratio of all people escaping from the export congestion queue time to the total escape time.

<!-- b000095 | furniture | pages [9] -->
Team # 1902407                                                    Page 9 of 27

<!-- b000097 | prose | pages [9] -->
𝑤× 𝜌 (4 −34) 𝛿1 = 𝐷𝑁𝑘 𝑤 represents the number of special people in the k floor using the k path. 𝐷𝑁𝑘

<!-- b000098 | prose | pages [9] -->
𝑤= 𝐷𝑁𝑡𝑜𝑡𝑎𝑙 (4 −35) ∑D𝑁𝑘

<!-- b000099 | prose | pages [9] -->
(4 −36) 𝐷𝑁𝑡𝑜𝑡𝑎𝑙= (ρ1 + ρ2 + ρ3 + ρ4) × 𝑁𝑡𝑜𝑡𝑎𝑙 ρ1, ρ2, ρ3, ρ4 represent the proportion of the elderly, children, pregnant women and the disabled respectively. The main population and feature of 𝑇4

<!-- b000100 | caption | pages [9] -->
Table 2  Group feature analysis

<!-- b000101 | prose | pages [9] -->
group Elderly children Pregnant woman Disabled Speed 0.5v 0.5v 0.2v 0.2v Weight(kg) 50 30 60 55 Force (N) 25 15 21 24 Feature Slower, easy to Faster, easy to Slower, prone to Easy to fall, prone fall fall accidents to accidents

<!-- b000102 | heading | pages [9] -->
4.7.1 Strategy to reduce 𝑻𝟒

<!-- b000103 | prose | pages [9] -->
•Arrange dedicated •When using scheduling passages with special strategies, minimize identification equipment the scheduling of these (hats) for easy people identification.

<!-- b000104 | prose | pages [9] -->
Easy to Slow fall

<!-- b000105 | prose | pages [9] -->
Difficult Language to handle •Set up simple and easy •Make sure that there emergen barrier indicator diagram;Use are passengers who are cies general language evacuated around them, (including body but not let them go to the language);Multiple crowded places.

<!-- b000106 | prose | pages [9] -->
languages are required

<!-- b000107 | prose | pages [9] -->
•。

<!-- b000108 | caption | pages [9] -->
Figure 8 Strategy to reduce 𝑻𝟒

<!-- b000109 | prose | pages [9] -->
Ⅴ. Model application in the Louvre

<!-- b000110 | heading | pages [9] -->
5.1 Data Analysis

<!-- b000111 | prose | pages [9] -->
The Louvre has a total of five floors. The total area of Louvre is about 72735𝑚2. It is divided into two underground floors and three floors above ground. Visitors enter the second floor. Most of the exhibition halls are on the third floor.

<!-- b000112 | furniture | pages [10] -->
Team # 1902407                                                    Page 10 of 27

<!-- b000113 | caption | pages [10] -->
Table 3 Basic data of Louvre

<!-- b000114 | prose | pages [10] -->
The Total room Narrow Narrow Number Stair area area（m2） （m2） number channel channel area of stairs （m2） of rooms number 2nd floor 98 12520.32 27 787.12 10 919.48 1st floor 153 18211.38 55 734.66 16 2226 Ground floor 122 21626.01 67 518.5 18 1870 Lower 27 11382.11 5 620.5 13 872 ground floor Napoleon 1 6260.16 1 2304 3 94.5 Hall (Note: The data sheet is from Google Maps, the guide of the Louvre official website.)

<!-- b000115 | prose | pages [10] -->
It can be learned from the above data that the most dense (the smallest area) and the largest number of room is 1st floor, the average room area is 212 m2/per room, next the ground floor is 309 m2/per room. This shows that the museum’s visitors will gather in the ground floor and the 1st floor. And the average area of the narrow channel of the ground floor is the smallest, being 7.73 m2 / per channel. The narrow channel area of the 1st floor is the second smallest, which is 13.35 m2 / per channel. Therefore, it can be inferred that due to the dense rooms and narrow passages, a large amount of congestion may occur, so the biggest difficulty in evacuation is the evacuation for the ground floor and the 1st floor.

<!-- b000116 | heading | pages [10] -->
5.2 Establish the network node model

<!-- b000117 | caption | pages [10] -->
Figure 9 Louvre evacuation network plan

<!-- b000118 | heading | pages [10] -->
5.3 Model Solution and Result

<!-- b000119 | prose | pages [10] -->
According to the latest statistics, the total number of tourists in the Louvre in 2018 was 10.2 million, an average of 27,945 people per day. Considering the limited capacity of the museum to accommodate tourists, the peak of the museum is one-half of the daily average data, that is, the maximum number of visitors is approximately 13,972 at a certain moment.

<!-- b000120 | heading | pages [10] -->
5.3.1 Longest route and time

<!-- b000121 | furniture | pages [11] -->
Team # 1902407                                                    Page 11 of 27

<!-- b000122 | caption | pages [11] -->
Table 4 Longest route and time

<!-- b000123 | prose | pages [11] -->
Floor Location Evacuation route 2nd floor 924 area The population of the area is evacuated south to the corner of the 931 area and the 924 area and lowered two steps to the 337 area, and then passes through the 338 area, the 339 area, the 345 area, the 347 area, the 408 area, and then descends by stairs to the lower ground floor Zone 170, then descend one step to the Napoleon Hall through the stairs, and finally rise two floors to the exit of the pyramid to escape the exit 1st floor 636 area The population in this area passes through 640 area, 641 area, 645 area, 650 area, 661 area, 703 area, and then descends two steps to the lower ground floor 170 area through the stairs, and then descends to the Napoleon Hall through the stairs, and finally rises two floors to the exit of the pyramid to escape the exit. Ground 323 area The population in this area passes through the 328 area, the 337 area, the floor 338 area, the 339 area, the 345 area, the 347 area, the 408 area, and then descends by a staircase to the lower ground floor 170 area, and then descends one to two floors through the stairs. And finally rise two floors to the exit of the pyramid to escape the exit. Lower 181 area The population in this area first passes through the 183 area, then the ground north walks to the diamond staircase and descends to the Napoleon Hall, floor and finally flees the exit through the Carrousel du Louvre underground corridor. Napoleon Diamond Escape the exit along the Carrousel du Louvre underground corridor Hall Square

<!-- b000124 | caption | pages [11] -->
Table 5  Comparison between model and random

<!-- b000125 | prose | pages [11] -->
2nd floor 1st floor Ground Lower Napoleon Hall floor ground floor

<!-- b000126 | heading | pages [11] -->
Model time

<!-- b000127 | prose | pages [11] -->
527.5s 487s 444.5s 188.5s 58.4s Random time 878s 729s 653s 223s 67.5s

<!-- b000128 | heading | pages [11] -->
Model injuries

<!-- b000129 | prose | pages [11] -->
12 21 30 14 17 Random 25 55 67 35 57 injuries

<!-- b000130 | prose | pages [11] -->
(Note: 𝛿1 =0.08； 𝛿2=0.25；𝛼= 1.2，β = 4.7，γ = 2.4) From the results, the time of the model is reduced by 39.3% compared with the random time, and the model in this paper is effective. The number of injured in this model was reduced from 239 to 94, a decrease of 60.69%.

<!-- b000131 | prose | pages [11] -->
Since the main exit of the Louvre is on the 2nd floor, it takes the longest time to evacuate from the 2nd floor. Although there are entrances and exits on both sides of the Louvre, the exit of the Lions Gate is not connected to other rooms on the ground floor; the exit of Richelieu will give priority to people on the north side. Therefore, if people on the 2nd floor choose to go out, it will cause more big congestion. Therefore the best way to exit the 2nd floor is to return to the main exit of the Napoleon Hall.

<!-- b000132 | furniture | pages [12] -->
Team # 1902407                                                    Page 12 of 27

<!-- b000133 | prose | pages [12] -->
We noticed that the slowest route on all floors was evacuated through the Napoleon Hall, and the extra downstairs did take more time. Therefore, if more exits can be added on the ground floor, the evacuation time will be effectively reduced.

<!-- b000134 | heading | pages [12] -->
5.3.2 Evacuation congestion analysis

<!-- b000135 | caption | pages [12] -->
Figure 10 Total number of evacuations in exits

<!-- b000136 | prose | pages [12] -->
From the chart we can see the exit evacuation: pyramid > Richelieu > Carrousel du Louvre > Lions Gate, the longest time to evacuate : the Carrousel du Louvre > Pyramid > Richelieu > Lions Gate. From the time, we can find the entrance and exit of the ground floor has an obvious effect on the evacuation speed, but from the evacuation number, the Napoleon Hall entrance and exit has an advantage.

<!-- b000137 | caption | pages [12] -->
Table 6 Time analysis of areas

<!-- b000138 | prose | pages [12] -->
Congestion Normal Congestion proportion Room 186.8s 89.2s 16.9% movement Upstairs and 137s 103s 19.5% downstairs Exit 5.5s 6s 1.1% movement 329.3s 198.2s 527.5s

<!-- b000139 | caption | pages [12] -->
Figure 11 Time analysis stereogram

<!-- b000140 | prose | pages [12] -->
In the Louvre evacuation, the slowest route was 52.3% in the room and channel movement; the downstairs time was 45.4% and the exit time was 2.1%.

<!-- b000141 | prose | pages [12, 13] -->
About 49.7% of the time on the slowest route was spent on congestion. Among them, congestion was 2.1% at the entrance and exit, 27.1% at the upper and lower floors, and 20.7% between the room and the channel movement. There are too many corridors from the 2nd floor to the Napoleon Hall, and the distance is long, so it takes more time. However, if evacuated from the ground floor, although the path is shortened, it will collide with the people who are evacuated from the first two floors to the first two layers, resulting in greater congestion and delayed evacuation.

<!-- b000142 | furniture | pages [13] -->
Team # 1902407                                                    Page 13 of 27

<!-- b000144 | heading | pages [13] -->
5.3.3 Potential nodes that limit exits

<!-- b000145 | prose | pages [13] -->
B(Demon on lower ground floor ); D (Lions exit on the ground floor); C(The left vertex at the exit of the diamond); E(Right staircase at the 170 area on the lower ground floor); A(Two exit nodes of the Richelieu)

<!-- b000146 | caption | pages [13] -->
Figure 12 Bottlenect node flow diagram

<!-- b000147 | prose | pages [13] -->
We select five nodes with the highest peak traffic flow at a certain time for analysis. The Louvre's largest peak of human traffic appeared at the lower ground floor of Demon after 245s of evacuation. At this time, the 2nd, 1st , and ground floor people passed through the channel at the same time, and the number of people passing through 30 approaching 700.

<!-- b000148 | prose | pages [13] -->
The second weak link is the left apex of the Diamond exit, the entry point of the Richelieu exit, the stairway of the 170th floor of the lower ground floor, and the entry point of the exit of the ground floor Lions’ Gate.

<!-- b000149 | prose | pages [13] -->
We noticed that two of the weaknesses of the top five restricted exits were at the point of proximity to the entrance and exit. And the two exits are all on the ground floor, which means that the evacuation channel of the ground floor entrance and exit has been fully utilized, our model is accurate, and the museum should pay attention to widening on both sides.

<!-- b000150 | prose | pages [13] -->
Ⅵ. Model Improvement

<!-- b000151 | heading | pages [13] -->
6.1 Model improvements under other disasters

<!-- b000152 | heading | pages [13] -->
6.1.1 Evacuation models for avoiding hazardous areas

<!-- b000153 | prose | pages [13] -->
The previous model is mainly for the general evacuation under ideal conditions, that is, the channel is complete, and there is no obstacle to personnel movement and access. The improvement of the model, that is, the emergency evacuation when the evacuation channel is incomplete and the movement of the person is limited is considered.

<!-- b000154 | prose | pages [13] -->
Emergency evacuation disasters that may be encountered at the Louvre include: fires, earthquakes, violent public attacks, stampede accidents, chemical gas leaks, etc. The methods of these accidents often lead to the unavailability of stairs, passages, and exits.

<!-- b000155 | furniture | pages [14] -->
Team # 1902407                                                    Page 14 of 27

<!-- b000156 | prose | pages [14] -->
At this point, the previous model needs to make three changes:

<!-- b000157 | prose | pages [14] -->
(1) Change the network path.

<!-- b000158 | prose | pages [14] -->
When a fire occurs, or a terrorist bomb attack on a place after use, at the location, personnel should be avoided.

<!-- b000159 | prose | pages [14] -->
(2) Set the recommended route.

<!-- b000160 | prose | pages [14] -->
When the scope of the disaster is large and not clear, in order to avoid casualties, it is often mandatory or recommended to evacuate from certain exits and passages.

<!-- b000161 | prose | pages [14] -->
The algorithm of evacuation models for avoiding hazardous areas is shown in appendix.

<!-- b000162 | prose | pages [14] -->
It can be seen from the algorithm that when an accident occurs in some places, limited the search range of the Dijkstra algorithm can avoid the dangerous area.

<!-- b000163 | prose | pages [14] -->
(3) Consider the impact of different natures of disasters on people's movement speed and mood.

<!-- b000164 | prose | pages [14] -->
When a large fire suddenly spreads and the smoke is large, people's moving speed will be affected and will be reduced. In the event of a sudden incident such as a shooting incident, an explosion, or an earthquake, the speed will increase due to extreme panic, but the accident rate will increase.

<!-- b000165 | prose | pages [14] -->
We assume 𝜑0 be the disaster factor caused by the accident.𝑆𝑐𝑎𝑙𝑒  represents the disaster grade. The disaster factor can be determined by the level of the disaster accident.

<!-- b000166 | prose | pages [14] -->
𝑆𝑐𝑎𝑙𝑒𝑖−𝑆𝑐𝑎𝑙𝑒𝑚𝑖𝑛 (𝑉𝑚𝑎𝑥 (6 −1) 𝜑0 = ) 𝑆𝑐𝑎𝑙𝑒𝑚𝑎𝑥−𝑆𝑐𝑎𝑙𝑒𝑚𝑖𝑛 𝑉

<!-- b000167 | caption | pages [14] -->
Table 7 Calculation of disaster factor

<!-- b000168 | prose | pages [14] -->
M4 M5 M6 M7 Gas leak earthquake earthquake earthquake earthquake Smoke Small fire Medium fire Heavy fire Disaster type alarm Stampede Shooting Explosion event event attack Ⅰ Ⅱ Disaster Grade Ⅲ Ⅳ Ⅴ 𝝋𝟎 0 0.625 1.25 1.875 2.5 Note:𝑉= 2𝑚/𝑠  𝑉𝑚𝑎𝑥= 5𝑚/𝑠

<!-- b000169 | prose | pages [14] -->
𝑤,𝑘′ 𝑤,𝑘 𝑊= 𝑚𝑎𝑥[(𝐿1 𝑤,𝑘+ 𝐿1 1 (6 −2) 𝑇1𝐾 𝑤,𝑘′) (1 + 𝜑0)] 𝑉1 𝑉1

<!-- b000170 | prose | pages [14] -->
𝑤,𝑘′ 𝑤,𝑘 𝑊= 𝑚𝑎𝑥[(𝐿2 𝑤,𝑘+ 𝐿2 1 (6 −3) 𝑇2𝐾 𝑤,𝑘′) (1 + 𝜑0)] 𝑉2 𝑉2

<!-- b000171 | prose | pages [14] -->
𝑤,𝑘′ 𝑤,𝑘 𝑊= 𝑚𝑎𝑥[(𝐿3 𝑤,𝑘+ 𝐿3 1 (6 −4) 𝑇3𝐾 𝑤,𝑘′) (1 + 𝜑0)] 𝑉3 𝑉3

<!-- b000172 | prose | pages [14] -->
4 𝑊= 𝑚𝑎𝑥([𝑁𝑘 𝑊+ β𝑇4,2𝐾 𝑊+ γ𝑇4,3𝐾 𝑊] 𝑤(1 + 𝜑0)𝛿𝑖𝑡0 + 𝑁𝑘 𝑤(1 + 𝜑0)𝛿1𝛿2𝑡0] × [α𝑇4,1𝐾 ) (6 −5) 𝑇4𝐾

<!-- b000173 | heading | pages [14] -->
6.2 Model improvement for emergency personnel entering quickly

<!-- b000174 | furniture | pages [15] -->
Team # 1902407                                                    Page 15 of 27

<!-- b000175 | prose | pages [15] -->
When a disaster occurs, there are tourists in the building who are in urgent need of evacuation and staff who assist in evacuation. But professional emergency personnel need to enter the house from outside the building to handle disaster areas and disaster causes, such as firefighters entering the fire, explosion-proof personnel of terrorist attacks, police, etc.

<!-- b000176 | prose | pages [15] -->
The route of emergency personnel entering the building and going to the accident site changes as the evacuation time changes.

<!-- b000177 | prose | pages [15] -->
After the evacuation is completed, the emergency personnel go to the accident site through the shortest route. With the improved Dijkstra, the shortest route can be found very quickly. However, during the evacuation process, traffic monitoring and prediction of each exit, stairs, and walkways are required to find the shortest route.

<!-- b000178 | prose | pages [15] -->
In the process of evacuation, if emergency personnel enter from the evacuation entrance, the evacuation efficiency will inevitably decrease. Therefore, this is a multi- objective planning problem, which is to ensure that the evacuation time is as short as possible, and that the emergency personnel arrive at the designated place as short as possible.

<!-- b000179 | prose | pages [15] -->
We assume the number of emergency personnel is NX; the designated destination is X. 𝑇1𝑁𝑋 𝑊 represents the time of the emergency personnel in the designated area 𝑊, 𝑇2𝑁𝑋 𝑊, 𝑇3𝑁𝑋 to move, up and down stairs, and entry and exit in the room respectively.

<!-- b000180 | prose | pages [15] -->
The added objective function is:

<!-- b000181 | prose | pages [15] -->
𝑊+ 𝑇2𝑁𝑋 𝑊+ 𝑇3𝑁𝑋 𝑊) 𝑚𝑖𝑛 𝑇𝑁𝑋= max(𝑇1𝑁𝑋 (6 −6) { 𝑊+ 𝑇2𝐾 𝑊+ 𝑇3𝐾 𝑊+ 𝑇4𝐾 𝑊) + 𝑀∗𝐹(𝐺𝑁𝑋)] min  𝑇= max[(𝑇1𝐾

<!-- b000182 | prose | pages [15] -->
𝐺𝑁𝑋  represents the entry route of the emergency personnel. 𝐹(𝐺𝑁𝑋) represents the delay time caused by the current route to evacuation.

<!-- b000183 | heading | pages [15] -->
6.2.1 Strategies to avoid emergency personnel conflict with maximum evacuation

<!-- b000184 | prose | pages [15] -->
time The time for emergency evacuation is determined by the latest evacuated person. If it can be made that the emergency personnel entering the building do not affect the evacuation route of the latest evacuated personnel and the emergency personnel's influence time on the evacuation personnel entering the route is less than the evacuation time of the latest evacuation personnel, the evacuation time will not change. ○ 1 Predict the total number of people per exit based on the route of the improved Dijkstra plan. There are D exits, and the time for predicting D exits is 𝑇𝑑1, 𝑇𝑑2, 𝑇𝑑3 … … ○ . 2 𝑁𝑋≤∑(𝑇𝐷𝑚𝑎𝑥−𝑇𝑑)𝐶𝑑 𝐷 , 𝑁𝑋𝑑= (𝑇𝐷𝑚𝑎𝑥−𝑇𝑑)𝐶𝑑  𝑁𝑋𝑑 represents the number of emergency personnel entering from the d exit. If 𝑁𝑋>∑(𝑇𝐷𝑚𝑎𝑥−𝑇𝑑)𝐶𝑑 , it means that the latest evacuation time will 𝐷 change.

<!-- b000185 | prose | pages [15] -->
3 Determination of the route. ○ With the improved Dijkstra, enter from D-1 entrances to the path of the intended location.

<!-- b000186 | prose | pages [15] -->
After calculating the shortest path, calculate the time of the escape route person on the shortest path, and reduce its speed to 1/2.

<!-- b000187 | furniture | pages [16] -->
Team # 1902407                                                    Page 16 of 27

<!-- b000188 | prose | pages [16] -->
If the evacuated person on the route has time greater than 𝑻𝑫𝒎𝒂𝒙, then the shortest distance in the line is set to infinity (abandon the line), and the second short line is calculated.

<!-- b000189 | heading | pages [16] -->
6.3 Model improvements under inspection in the Louvre

<!-- b000190 | heading | pages [16] -->
6.3.1 Test result

<!-- b000191 | prose | pages [16] -->
When fires happen in the Louvre and all large multi-level buildings, or for some other reasons, some areas cannot be used, the cessation of use in different regions has different effects on evacuation.

<!-- b000192 | caption | pages [16] -->
Table 8 Test result in different areas

<!-- b000193 | prose | pages [16] -->
Most influential area（X Type of regional Congestion time Evacuation time Area） impact ratio A channel 338 area in ground floor 42.5% 632.5s cannot be used A corridor Stairs on the east side of 49.2% 566.0s cannot be used the ground floor 408 area An exit cannot Pyramid exit 52.8% 782.0s be used

<!-- b000194 | caption | pages [16] -->
Figure 13 Evacuation route changes when affected by the disaster channel area

<!-- b000195 | caption | pages [16] -->
Table 9 Optimal route and number of emergency personnel

<!-- b000196 | prose | pages [16] -->
Entry Maximum number Time Route of emergency personnel

<!-- b000197 | prose | pages [16] -->
Enter from the pyramid, from the entrance of the Syrian Pavilion to the lower ground floor, Pyramid 240 229s into the corridor of 132, from the stairs next to 132 to the ground floor, after 348, 345, 339 arrives at 338.

<!-- b000198 | prose | pages [16, 17] -->
Lions Entered by the Lions Gate, the stairs next to 410 370s the door to the 1st floor, from 719, 708, 717, Gate 716, 712, 710, 708, 703, arrived at the stairs measured by 703, down to the ground floor, after 408, 347, 345, 339 ,arrived in the 338 area.

<!-- b000199 | furniture | pages [17] -->
Team # 1902407                                                    Page 17 of 27

<!-- b000201 | prose | pages [17] -->
Since Richelieu entry and Carrousel du Louvre entry influence the longest evacuation route, the number of the emergency personnel is 0.

<!-- b000202 | heading | pages [17] -->
6.3.2 Test conclusion

<!-- b000203 | prose | pages [17] -->
Pyramid exits cannot be used, resulting in a 48.3% delay in evacuation. And the total congestion ratio increased by 22.3%. In all channel areas, the ground floor 338 channel area will maximize the evacuation time delay, delay 20%, and the congestion level increased by 3.1%. The evacuation time delay caused by the stairs on the east side of the ground floor 408 area increased the congestion level by 14.3%.

<!-- b000204 | prose | pages [17] -->
Different areas cannot be used, the most affected by the evacuation time is the exit, next are the key channel, and finally the stairs, but the impact on the degree of congestion is that the influence of the stairs is greater than the key channel. This is due to the circular structure and channel of the Louvre. When one side of the channel is not available, the other side of the channel will take longer to move, but less congestion. The Louvre's stairs have an average of 80 meters, so the corridor cannot be used, the main increase is the congestion time.

<!-- b000205 | prose | pages [17] -->
Among the four main entrances and exits of the Louvre, there are fewer evacuated personnel because the Lions Gate is located on both sides and the same floor is not the same as other rooms. Emergency personnel can be arranged to enter more, but accordingly, emergency personnel need to spend more time on the move because they are not connected to the other room. Entering from the pyramid, the impact on evacuation time is minimal, because there are quite a few stairs to choose from to go to the destination.

<!-- b000206 | heading | pages [17] -->
6.4 Model improvements under other large, crowded structures

<!-- b000207 | prose | pages [17] -->
Intensive public buildings of different large groups, including stadiums, concert halls, subway stations, airplane stations, shopping malls, etc. For these public buildings, feature classification is first performed.

<!-- b000208 | heading | pages [17] -->
6.4.1 Large and medium-sized mall

<!-- b000209 | prose | pages [17] -->
The mall is a gathering place for all kinds of businesses. The staff are mainly cleaners responsible for the cleaning and the security personnel at the door. When the disaster suddenly occurs, there is a lack of sufficient staff to evacuate, often relying on emergency personnel entering from the outside. Lack of on-site evacuation and guidance personnel will make the crowd unable to regulate and dispatch when they are congested. Improvements are:

<!-- b000210 | prose | pages [17] -->
1）Use a system such as broadcasting for grooming and control.

<!-- b000211 | prose | pages [17] -->
2）Use the indicator light that can adjust the direction to change the direction of the indicator light and guide the crowd to avoid the congested area.

<!-- b000212 | heading | pages [17] -->
6.4.2 Stadiums, concert halls, cinemas

<!-- b000213 | prose | pages [17, 18] -->
Usually a large open space, people sit next to each other. When they start to escape, people must stand up and wait in line (congested state) to get out quickly, and the objective function changes to:

<!-- b000214 | furniture | pages [18] -->
Team # 1902407                                                    Page 18 of 27

<!-- b000216 | prose | pages [18] -->
𝑊+ 𝑇2𝐾 𝑊+ 𝑇3𝐾 𝑊+ 𝑇4𝐾 𝑊+ 𝑇5𝐾 𝑊) (6 −7) 𝑚𝑖𝑛 𝑇= 𝑚𝑎𝑥(𝑇1𝐾 𝑊 represents the time to stand up and wait in line to leave the seat,𝑇5𝐾 𝑊= 𝐿𝑆/𝑉𝑆. 𝑇5𝐾 𝐿5 represents the farthest distance from the aisle in the audience seat. 𝑉5 represents the speed of evacuation from the seat.

<!-- b000217 | heading | pages [18] -->
6.4.3 Subway station, railway station, airport

<!-- b000218 | prose | pages [18] -->
These sites are considered to be divided into two areas, on-site and off-site, due to security reasons. That is, free activities such as off-site exits; the main venue is the waiting room. In the case of emergency evacuation, although there are exits (train station) and (airplane) outside the open space, tourists may have a front safety accident at the railway station and the plane. Therefore, when building a network model, the exit cannot select the train station and the aircraft boarding gate. When going from the infield to the outfield, the security checkpoint is a must.

<!-- b000219 | prose | pages [18] -->
For those who evacuate in the field, the network model needs to be improved.

<!-- b000220 | prose | pages [18] -->
When using the improved Dijkstra for calculations

<!-- b000221 | caption | pages [18] -->
Table 10 Key section of improved Dijkstra algorithm for calculation

<!-- b000222 | prose | pages [18] -->
For Infield node, Outfield node While the nodes in the inner field in the collection U are not empty Find U to the nearest node v of S Put v in S, U remove v If S cross J is not empty Break End if End for

<!-- b000223 | prose | pages [18] -->
Ⅶ. Model Summary

<!-- b000224 | heading | pages [18] -->
7.1 Advantage

<!-- b000225 | prose | pages [18] -->
(1) Based on the optimal path and dynamic scheduling model, this paper considers the complex distribution of different nodes, studies the influence of different room nodes and stair nodes, further calculates the proportion of congestion time, and improves the accuracy of the model.

<!-- b000226 | prose | pages [18] -->
(2) At the same time of dynamic scheduling on the same floor, real-time scheduling is also implemented for different floors, thus reducing the time of congestion during evacuation.

<!-- b000227 | prose | pages [18] -->
(3) While considering the evacuation of the Louvre, this paper also extends the model to more complex building structures such as shopping malls and office buildings, making the models and algorithms more universal.

<!-- b000228 | heading | pages [18] -->
7.2 Disadvantage

<!-- b000229 | prose | pages [18] -->
(1) The population distribution is relatively uniform when the model is calculated, but the density of the population in real life is different.

<!-- b000230 | furniture | pages [19] -->
Team # 1902407                                                    Page 19 of 27

<!-- b000231 | prose | pages [19] -->
(2) The model was not taken into account when the different emotions of the crowd were affected by the exit.

<!-- b000232 | prose | pages [19] -->
(3) The structure of the Louvre is intricate and complex, and the number of nodes is huge. Therefore, the calculation of the model is relatively complicated and needs to be improved.

<!-- b000233 | prose | pages [19] -->
Ⅷ. Policy and procedural recommendations for the

<!-- b000234 | prose | pages [19] -->
Louvre emergency management

<!-- b000235 | heading | pages [19] -->
8.1 Model deployment requirements

<!-- b000236 | prose | pages [19] -->
(1) Require the Louvre to have management personnel in the important passages in the museum, and to assist in dynamic scheduling during emergency evacuation.

<!-- b000237 | prose | pages [19] -->
(2) Ask the Louvre to use monitoring equipment in real time to view and calculate the flow of people in each room passage, stairs, entrances and exits.

<!-- b000238 | heading | pages [19] -->
8.2 Suggestions for accelerating emergency evacuation

<!-- b000239 | prose | pages [19] -->
(1) Broaden the channel width of the five bottleneck intersections According to our model calculation results, the bottlenecks that limit evacuation mainly include the channel of the lower ground floor of Demon, the left apex of the diamond exit, the entry node of the Richelieu exit, the stairway of the 170th floor of the lower ground floor, and the entry point of the exit of the lion door of the ground floor.

<!-- b000240 | prose | pages [19] -->
(2) Open the other rooms on the 0th floor to the passage of the Lions Gate

<!-- b000241 | caption | pages [19] -->
Figure 14 Set up the new channel of the Lions Gate

<!-- b000242 | prose | pages [19] -->
After the calculation of our model, the lack of access to the Lions Gate at the ground floor caused the Lions Gate to be fully utilized. When the channel of the blue line in the map is opened, the number of evacuations of the pyramid can be transferred to the Lions Gate at most 1,100 people, thus reducing the congestion of the pyramid by 24% and making full use of the Lions Gate.

<!-- b000243 | prose | pages [19] -->
(3) Give priority to adding intersections at the ground floor Due to the lack of direct exits in the Sully Pavilion, evacuators need to re-enter Richelieu, Denon or the underground pyramid to find the exit. If the exit can be increased in the position of the figure, the evacuation time can be reduced from 527.8s to 440s, which is reduced by 16%. At the same time, it can effectively reduce the congestion of the pyramid and the Carrousel du Louvre exit.

<!-- b000244 | furniture | pages [20] -->
Team # 1902407                                                    Page 20 of 27

<!-- b000245 | caption | pages [20] -->
Figure 15 Set up new doors for Sully exit

<!-- b000246 | heading | pages [20] -->
8.3 Entry of emergency personnel and use of other entrances

<!-- b000247 | prose | pages [20] -->
For the entry of emergency personnel, it is necessary to contact the monitoring in the hall. Through the current route planning for escape and the calculation of traffic monitoring, the longest evacuation route and time in the museum are obtained. Two criteria are adopted: 1. The emergency personnel's route does not conflict with the longest evacuation route; 2. The number of emergency personnel cannot cause the evacuation route delay time on the emergency route to exceed the current longest evacuation route time. To ensure that the evacuation time is the shortest, and emergency personnel can reach the designated location as soon as possible. The relevant algorithm has been given, which calculates the optimal route and calculates the optimal number of emergency personnel. According to the calculations that have been carried out, among the four entrances and exits, the intersection that can arrange the most emergency personnel to enter is the Lions Gate, which can arrange up to 400 people, but it takes the longest travel time. The fastest entry point for emergency personnel arriving at a designated location is the entrance to Richelieu, but a maximum of 200 emergency personnel can be arranged and will greatly increase the congestion level of Richelieu.

<!-- b000248 | heading | pages [20] -->
8.4 Different population structures and characteristics

<!-- b000249 | prose | pages [20] -->
For different population structures and characteristics, different ways to reduce congestion time.

<!-- b000250 | prose | pages [20] -->
Details as follows： (1) For those who are easy to fall, special channels will be arranged, equipped with special identification equipment to facilitate people's identification;

<!-- b000251 | prose | pages [20] -->
(2) For people with slower moving speed, when using the scheduling strategy, minimize the scheduling of these people;

<!-- b000252 | prose | pages [20, 21] -->
(3) For some people who are difficult to deal with emergencies, such as children and the elderly, try to let them have passengers who are evacuated as far as possible, but not let them go to the places where they are congested;

<!-- b000253 | furniture | pages [21] -->
Team # 1902407                                                    Page 21 of 27

<!-- b000255 | prose | pages [21] -->
(4) For some people who have language barrier, set up simple and easy indicator diagram; Use general language (including body language); Multiple languages are required.

<!-- b000256 | prose | pages [21] -->
Ⅸ. References [1] 杨建芳, 高岩, 王宏杰. 多层建筑物应急疏散模型和算法[J]. 系统仿真学报, 2014, 26(2):267-273. [2] Smith M G . State-dependent queueing models in emergency evacuation networks[J].

<!-- b000257 | prose | pages [21] -->
Transportation Research, Part B (Methodological), 1991, 25(6):373-389. [3] Pursals, Salvador Casadesús, Garzón, Federico Garriga. Optimal building evacuation time considering evacuation routes[J]. European Journal of Operational Research, 2009, 192(2):692-699. [4] Manley M ,  Kim Y S . Modeling emergency evacuation of individuals with disabilities (exitus): An agent-based public decision support system[J]. Expert Systems with Applications, 2012, 39(9):8300-8311. [5] Feng F . A fast flow control algorithm for real-time emergency evacuation in large indoor areas[J]. Fire Safety Journal, 2009, 44(5):732-740. [6] Saadatseresht M ,  Mansourian A ,  Taleai M . Evacuation planning using multiobjective evolutionary optimization approach[J]. European Journal of Operational Research, 2009, 198(1):305-314. [7] Hayakawa Y ,  Mori K ,  Ishida Y , et al. Development of emergency rescue evacuation support system in panic-type disasters[C]// Consumer Communications & Networking Conference. IEEE, 2012.

<!-- b000258 | furniture | pages [22] -->
Team # 1902407                                                    Page 22 of 27

<!-- b000259 | prose | pages [22] -->
Ⅹ. Appendix

<!-- b000260 | heading | pages [22] -->
10.1 Algorithm

<!-- b000261 | heading | pages [22] -->
10.1.1 Same floor scheduling algorithms

<!-- b000262 | prose | pages [22] -->
𝑤(𝑡). Input：The total number of people on the w floor in i place: N𝑖 Output：At time t, the number of people evacuated to j at point j 𝑤(𝑡) = 0(i=1,2,3…) Initialization： initialize 𝑁𝑖𝑗 Process：For i = 1 to M (M is the total number of nodes on the w floor) 𝑤(𝑡) N𝑡𝑖= (𝑁𝑖 −𝐿𝑖 ) 𝐶𝑖𝑗 𝑉𝑆 End For For i = 1 to M For j = 1 to M If i ≅j and N𝑡𝑖> N𝑡𝑗 𝑤(𝑡) Calculate 𝑁𝑖𝑗

<!-- b000263 | prose | pages [22] -->
𝐿𝑖𝑗 𝐿𝑖 𝑤(𝑡)−( 𝑤(𝑡)−𝑁𝑖𝑗 𝑤(𝑡) 𝑤(𝑡) 𝑁𝑗 𝑉𝑠+ 𝑉𝑠)𝐶𝑗 𝑁𝑖 𝑁𝑖𝑗 𝐿𝑖𝑗 𝐿𝑖 Which make 𝑉𝑠 − 𝑉𝑠= 𝑀[ ] + + 𝐶𝑖𝑖 𝐶𝑗 𝐶𝑖𝑗

<!-- b000264 | prose | pages [22] -->
𝑤(𝑡) < 0 If 𝑁𝑖𝑗 𝑤(𝑡) = 0 𝑁𝑖𝑗 Else

<!-- b000265 | prose | pages [22] -->
𝐿𝑖𝑗 𝑤(𝑡+ 1) = 𝑁𝑖 𝑤(𝑡) −𝑁𝑖𝑗 𝑤(𝑡) −𝑐𝑖 𝑉𝑠 𝑁𝑖

<!-- b000266 | prose | pages [22] -->
𝑤(𝑡) −𝑐𝑗𝐿𝑖𝑗 𝑤(𝑡+ 1) = 𝑁𝑗 𝑤(𝑡) + 𝑁𝑖𝑗 𝑁𝑗 𝑉𝑠 End If End If End For End For

<!-- b000267 | heading | pages [22] -->
10.1.2 Different floor scheduling algorithms

<!-- b000268 | prose | pages [22] -->
𝑤(𝑡) Input：The number of people waiting for the stairs at the stairway of all floors at t time : ∑N𝑖 𝑤(𝑡) Output：Number of people dispatched to another stairway at a certain stairway at time t : N𝑖𝑗 𝑤(𝑡) = 0(i,j=1,2,3…) Initialization：(1) initialize t=1,N𝑖𝑗 (2) initialize q Process：For i = 1 to M (M is the number of the stairs) 𝑤(𝑡) 𝑇𝑖= ∑𝑁𝑖 𝐶𝑖 End For For i = 1 to M For j = 1 to M

<!-- b000269 | prose | pages [22, 23] -->
𝐿𝑖𝑗 (T𝑖−𝑇𝑗)𝐶𝑖 If i ≅j and T𝑖> 𝑇𝑗 and T𝑖−𝑇𝑗> 𝑉𝑠+ 𝐶𝑗 𝑤(𝑡) = (T𝑖−𝑇𝑗)𝐶𝑖 N𝑖𝑗 𝐶𝑗 𝑐𝑖𝐿𝑖𝑗 N𝑖,𝑤(𝑡+ 1) = N𝑖 𝑤(𝑡) −N𝑖𝑗 𝑤(𝑡) − (𝑤−1)𝑉𝑠 𝑐𝑗𝐿𝑖𝑗 N𝑗;𝑤(𝑡+ 1) = N𝑗 𝑤(𝑡) −N𝑖𝑗 𝑤(𝑡) − (𝑤−1)𝑉𝑠 End If End For End For

<!-- b000270 | furniture | pages [23] -->
Team # 1902407                                                    Page 23 of 27

<!-- b000272 | heading | pages [23] -->
10.1.3 Algorithm of evacuation models for avoiding hazardous areas

<!-- b000273 | prose | pages [23] -->
Input：Disaster occurrence point X，Range of disaster is X area Network G，Starting node S，Stairway node R∗，End point set D，The number of people in the stairway C𝑅𝑖. Output：dist{x} Optimal route from the starting node S to the destination Initialization：(1)initialize S={s}，V={other nodes} (2) if<U,S> set has edges connected, its weight is assigned. Otherwise the assignment is positive infinity Process：For i = 1 to length(R∗) ∗∗y 𝐴𝑟𝑒𝑎= C𝑅𝑖 If S ∉Area R∗′ = R∗ 𝑟𝑒𝑚𝑜𝑣𝑒 R𝑖 𝑆= 𝑆 𝑟𝑒𝑚𝑜𝑣𝑒 R𝑖 End If End For For w to high(Floor difference between starting point and exit) While N(w) ≠0(The number of nodes in the w floor is not zero) Find the node V closest to S in U If  V is not in X area 𝑈= 𝑈 𝑟𝑒𝑚𝑜𝑣𝑒 ; 𝑆= 𝑆 𝑟𝑒𝑚𝑜𝑣𝑒 𝑆 𝑘 in S and S ∩D = ∅)or(S ∩D = ∅) If (all R𝑤 Break End If End While End For

<!-- b000274 | heading | pages [23] -->
10.2 Louvre group statistics

<!-- b000275 | caption | pages [23] -->
Table 1 Proportion of various tourists

<!-- b000276 | prose | pages [23] -->
Elderly Children Disabled Pregnant Language Normal woman barrier Proportion 11% 5% 2.5% 1% 53% 27.5%

<!-- b000277 | caption | pages [23] -->
Table 2 Speed of different areas

<!-- b000278 | prose | pages [23, 24] -->
Upstairs and Room channel moving Entry and exit downstairs speed m/s m/s Normal speed 0.25 2 2 Congestion speed 0.0625 0.5 0.6

<!-- b000279 | furniture | pages [24] -->
Team # 1902407                                                    Page 24 of 27

<!-- b000281 | heading | pages [24] -->
10.3 Detailed Louvre area number

<!-- b000282 | furniture | pages [25] -->
Team # 1902407                                                    Page 25 of 27

<!-- b000283 | heading | pages [25] -->
10.4 Evacuation network diagrams

<!-- b000284 | prose | pages [25, 26] -->
2nd floor 1st floor

<!-- b000285 | furniture | pages [26] -->
Team # 1902407                                                    Page 26 of 27

<!-- b000287 | prose | pages [26] -->
Ground floor

<!-- b000288 | prose | pages [26, 27] -->
Lower ground floor Napoleon Hall

<!-- b000289 | furniture | pages [27] -->
Team # 1902407                                                    Page 27 of 27
