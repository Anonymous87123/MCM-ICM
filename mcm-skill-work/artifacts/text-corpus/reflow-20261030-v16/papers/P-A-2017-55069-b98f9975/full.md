# P-A-2017-55069-b98f9975

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000003 | front_matter | pages [1] -->
55069

<!-- b000004 | front_matter | pages [1] -->
T1 ________________ F1 ________________

<!-- b000005 | front_matter | pages [1] -->
T2 ________________ F2 ________________ Problem Chosen T3 ________________ F3 ________________

<!-- b000006 | front_matter | pages [1] -->
A

<!-- b000007 | front_matter | pages [1] -->
T4 ________________ F4 ________________

<!-- b000008 | prose | pages [1] -->
2017 MCM/ICM Summary Sheet

<!-- b000009 | title | pages [1] -->
The Rehabilitation of the Kariba Dam

<!-- b000010 | prose | pages [1] -->
Recently, the Institute of Risk Management of South Africa has just warned that the Kariba dam is in desperate need of rehabilitation, otherwise the whole dam would collapse, putting 3.5 million people at risk. Aimed to look for the best strategy with the three options listed to maintain the dam, we employ AHP model to filter factors and determine two most influential criteria, including potential costs and benefits. With the weight of each criterion worked out, our model demonstrates that option 3 is the optimal choice.

<!-- b000011 | prose | pages [1] -->
According to our choice, we are required to offer the recommendation as to the number and placement of the new dams. Regarding it as a set covering problem, we develop a multi-objective optimization model to minimize the number of smaller dams while improving the water resources management capacity. Applying TOPSIS evaluation method to get the demand of the electricity and water, we solve this problem with genetic algorithm and get an approximate optimal solution with 12 smaller dams and determine the location of them.

<!-- b000012 | prose | pages [1] -->
Taking the strategy for modulating the water flow into account, we construct a joint operation of dam system to simulate the relationship among the smaller dams with genetic algorithm approach. We define four kinds of year based on the Kariba’s climate data of climate, namely, normal flow year, low flow year, high flow year and differential year. Finally, these statistics could help us simulate the water flow of each month in one year, then we obtain the water resources planning and modulating strategy.

<!-- b000013 | prose | pages [1] -->
The sensitivity analysis of our model has pointed out that small alteration in our constraints (including removing an important city of the countries and changing the measurement of the economic development index etc.) affects the location of some of our dams slightly while the number of dams remains the same. Also we find that the output coefficient is not an important factor for joint operation of the dam system, for the reason that the discharge index and the capacity index would not change a lot with the output coefficient changing.

<!-- b000014 | furniture | pages [2] -->
Team # 55069                                                            Page 2 of 2

<!-- b000015 | heading | pages [2] -->
Contents

<!-- b000016 | contents | pages [2] -->
1 Overview ................................................................................................................... 1

<!-- b000017 | contents | pages [2] -->
1.1 Background ................................................................................................. 1

<!-- b000018 | contents | pages [2] -->
1.2  Restatement of the Problem ..................................................................... 1

<!-- b000019 | contents | pages [2] -->
1.3  Literature Review ....................................................................................... 2

<!-- b000020 | contents | pages [2] -->
2 Assumptions and Justifications ........................................................................ 2

<!-- b000021 | contents | pages [2] -->
3 Notation .................................................................................................................... 3

<!-- b000022 | contents | pages [2] -->
4 Model Overview ...................................................................................................... 4

<!-- b000023 | contents | pages [2] -->
5 Model Theory........................................................................................................... 5

<!-- b000024 | contents | pages [2] -->
5.1 Determination of the Number and Location of the Dams .................... 5

<!-- b000025 | contents | pages [2] -->
5.2  Joint operation of dam system model ..................................................... 9

<!-- b000026 | contents | pages [2] -->
6 Model Implementation and Results ................................................................ 11

<!-- b000027 | contents | pages [2] -->
6.1 The Number and Location ...................................................................... 11

<!-- b000028 | contents | pages [2] -->
6.2 The Strategy of Modulating Water Flow ............................................... 14

<!-- b000029 | contents | pages [2] -->
7 Sensitivity Analysis ............................................................................................. 15

<!-- b000030 | contents | pages [2] -->
7.1  The Model of Determination of the Number and Location ................. 15

<!-- b000031 | contents | pages [2] -->
7.2  The Model of Modulating Water Flow ................................................... 17

<!-- b000032 | contents | pages [2] -->
8 Further discussion .............................................................................................. 17

<!-- b000033 | contents | pages [2] -->
9 Strengths and Weaknesses .............................................................................. 18

<!-- b000034 | contents | pages [2] -->
9.1  Strengths ................................................................................................... 18

<!-- b000035 | contents | pages [2] -->
9.2  Weaknesses .............................................................................................. 19

<!-- b000036 | contents | pages [2] -->
10 Conclusion .......................................................................................................... 19

<!-- b000037 | contents | pages [2] -->
11 The Evaluation of Three Options ................................................................... 20

<!-- b000038 | contents | pages [2] -->
11.1  Establish a Hierarchical Model ............................................................. 20

<!-- b000039 | contents | pages [2] -->
11.2  Analysis and Results ............................................................................. 21

<!-- b000040 | furniture | pages [3] -->
Team # 55069                                                            Page 1 of 28

<!-- b000041 | heading | pages [3] -->
1 Overview

<!-- b000042 | heading | pages [3] -->
1.1  Background

<!-- b000043 | prose | pages [3] -->
A Zambezi River Authority conference was held in March 2014, engineers warned that the foundations of the dam had weakened and there was a possibility of dam failure unless repairs were made.

<!-- b000044 | prose | pages [3] -->
On 3 October 2014 the BBC reported that “The Kariba Dam is in a dangerous state. Opened in 1959, it was built on a seemingly solid bed of basalt. However, in the past 50 years, the torrents from the spillway have eroded that bedrock, carving a vast crater that has undercut the dam’s foundations, engineers are now warning that without urgent repairs, the whole dam will collapse. If that happened, a tsunami-like wall of water would rip through the Zambezi valley, reaching the Mozambique border within eight hours. The torrent would overwhelm Mozambique’s Cahora Bassa Dam and knock out 40% of southern Africa’s hydroelectric capacity. Along with the devastation of wildlife in the valley, the Zambezi River Authority estimates that the live of 3.5 million people are at risk.”

<!-- b000045 | prose | pages [3] -->
On February 2015, Engineers have started on a R3.3bn rescue marathon to prevent the “catastrophic failure” of the Kariba Dam. According to a World Bank special report on the beleaguered structure-one of the biggest man-made dams in the world-a potential wall collapse threatens the lives of about 3-million people living on the Zambezi River floodplain between the hydro scheme on the Zambia-Zimbabwe border and the Mozambique coast. [1]

<!-- b000046 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000047 | prose | pages [3] -->
We are required to provide an overview of potential costs and benefits with the three options already listed. Then we need to establish a model to determine the number and placement of the new dams when removing the Kariba dam along the Zambezi River. The same overall water management capabilities are also needed. In addition, we should consider emergency water flow situations and restrictions regarding the locations and time, so that we could give out the strategy for modulating the water flow through our new multiple dam system.

<!-- b000048 | prose | pages [3] -->
In order to solve those problems, we will proceed as follows:

<!-- b000049 | prose | pages [3] -->
 Build a model to determine the number and location of the multiple dams.

<!-- b000050 | prose | pages [3] -->
 Give the corresponding strategy of modulating water flow in different conditions.

<!-- b000051 | prose | pages [3] -->
In our model, we first establish a multi-objective model and use genetic algorithm determine the number and location of the multiple dams. There are two goals improving the water resources management capacity and reducing the cost. Besides, we add some constraints such as water balance, water level, safety and water protection. We choose twenty suitable dam sites and employ the genetic algorithm to solve the optimal problem to determine the number and the location.

<!-- b000052 | prose | pages [3, 4] -->
After determining the number and location of the dams, we construct our joint operation of dam system model and employ the genetic algorithm to solve the problem based on the thought of dynamic programming. According to the Kariba’s climate data for about 30 years, we abstract normal flow year, low flow year, high flow year and differential year. We use them to work out the water resources planning and scheduling strategy. The construction of the discharge index and the capacity index benefits an analysis and evaluation for joint operation of the dam system’s performance in different month and year.

<!-- b000053 | furniture | pages [4] -->
Team # 55069                                                            Page 2 of 28

<!-- b000055 | heading | pages [4] -->
1.3  Literature Review

<!-- b000056 | prose | pages [4] -->
Dating back to 2004, the United States removed 72 dams in total, which created a historical record. Therefore, it is high time for us to focus on the construction of dams concerning their number and placement. Plenty of researchers have already made a number of notable papers to address these problems

<!-- b000057 | prose | pages [4] -->
Alfer Weber (1909) first proposed a framework for location problem, which is an allocation question with respect to space resource. Among the three classical location model, set covering problem is a significant branch of siting issues. They explored a multi-objective location model to tackle problems with siting optimal points. In their model, maximizing coverage rate in order to satisfy every place’s need is the target function, the concentric point and the capacity restrictions are constraint conditions. Thus, they could convert the optimization problem to the mixed integer linear programming question.

<!-- b000058 | prose | pages [4] -->
After the set covering model was established, we can optimize our choice of siting the dams. Then several scientists were devoted to building an optimal operation model to provide a reasonable balance between safety and balance. They begin to figure out how the multiple dam system would benefit or affect each other within its system. Masse(1940) first illustrated the concept of it; their main computing method was to optimize water modulating strategy during dispatching period.

<!-- b000059 | prose | pages [4] -->
Further studies are carried out about different methods to investigate the optimal operation model, including dynamic programming algorithm and neural network algorithm based on improved computer technique. Also, there is much theoretical analysis about location problem since 1990. John Current and Morton O'Kelly(1992) suggested using a modified version of the set covering location model, which still didn’t take the reality into account.

<!-- b000060 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000061 | prose | pages [4] -->
To simplify our problems, we make the following basic assumptions, each of which is properly justified.

<!-- b000062 | prose | pages [4] -->
 The dam system is built downstream in the valley of the Kariba Dam. Because it’s more convenient to build and also with less cost, which can be easily implemented.

<!-- b000063 | prose | pages [4] -->
 The cost of the dam is mostly the same. Owing to the fact that the length of the canyon is not large（24km）,geological conditions and climate conditions are mostly the same.

<!-- b000064 | furniture | pages [5] -->
Team # 55069                                                            Page 3 of 28

<!-- b000065 | prose | pages [5] -->
 Each dam’s water supply is mostly the same. Taking into account of safe operation of the entire multi-dam system, we should make the burden of each dam to be the same as much as possible.

<!-- b000066 | prose | pages [5] -->
 The water quality of the dam system is the average of the water quality between the two reservoirs. The river is flowing, so the water quality is mostly similar.

<!-- b000067 | prose | pages [5] -->
 Water of the dams downstream only comes from dams upstream and natural precipitation. According to Google Maps, there are no tributaries near the canyon. Also with the principle of conservation of water, the formula should be maintained.

<!-- b000068 | heading | pages [5] -->
3 Notation

<!-- b000069 | prose | pages [5] -->
Abbreviation Description

<!-- b000070 | prose | pages [5] -->
   Y y y , , y The set of cities 1 2 m

<!-- b000071 | prose | pages [5] -->
  X = x x , , x The set of dams 1 2 n

<!-- b000072 | prose | pages [5] -->
thi city to the nearest smaller dam The distance from the d y X ( , ) i n

<!-- b000073 | prose | pages [5] -->
thi city Ele The electricity demand of i

<!-- b000074 | prose | pages [5] -->
thi city Wat The water demand of i

<!-- b000075 | prose | pages [5] -->
thi dam at the end of period t, W t i The discharge amount of the ( , )

<!-- b000076 | prose | pages [5] -->
Z t i ( , ) The total amount of water released during period t

<!-- b000077 | prose | pages [5] -->
T t i ( , ) The amount of natural water in period t

<!-- b000078 | prose | pages [5] -->
thj period of the thi dam V The volume in the ij

<!-- b000079 | prose | pages [5, 6] -->
thj period of the thi dam Q The inflow in the ij thj period of the thi dam q The discharge volume in the ij

<!-- b000080 | furniture | pages [6] -->
Team # 55069                                                            Page 4 of 28

<!-- b000082 | prose | pages [6] -->
i  The runoff volume between the thi dam and the( 1)th QJ dam ij

<!-- b000083 | prose | pages [6] -->
thj period The actual water supply thi dam in the S ij

<!-- b000084 | prose | pages [6] -->
thj period thi dam in the D The planned water supply of the ij

<!-- b000085 | prose | pages [6] -->
thj period thi dam in the H The hydraulic head of ij

<!-- b000086 | prose | pages [6] -->
thi dam K The fore-voltage factor of the i

<!-- b000087 | prose | pages [6] -->
t The discharge flow indicators in the tht period

<!-- b000088 | prose | pages [6] -->
t The storage capacity indicators in the tht period

<!-- b000089 | heading | pages [6] -->
4 Model Overview

<!-- b000090 | prose | pages [6] -->
To provide a detailed analysis of the option (3)-removing the Kariba dam and newly building ten to twenty smaller dams. We need to determine the number and location of the multiple dams first. And on that basis we must establish a model to modulate the water flow through the multiple dam system to adapt to different situations. A reasonable balance between safety and cost of our strategy is also needed.

<!-- b000091 | prose | pages [6] -->
Our first model allows us to determine the number and the location of the multiple dams. We regard the optimal problem as a set covering problem and establish a multi-objective model to solve the problem. There are two goals, namely improving water resources management capacity and reducing the cost. And there are also some constraints including water balance, water level, safety, water resources protection and number constraints. On the account that the optimal problem is difficult to solve in polynomial time, so we use genetic algorithm to get the solution.

<!-- b000092 | prose | pages [6, 7] -->
After determining the numbers and the location, we establish a joint operation of dam system model to gain a strategy about modulating water flow in different condition. Though it’s also a multi-objective problem, it is different from the previous model. We use the maximization of economic and social benefits as the objective and set some constraints, such as water balance, reservoir capacity and discharge flow constraints. We use genetic algorithm to get the modulating strategy in different conditions.

<!-- b000093 | furniture | pages [7] -->
Team # 55069                                                            Page 5 of 28

<!-- b000095 | prose | pages [7] -->
In conclusion, we use programming and heuristic algorithm to solve the problem of building dams and the modulating strategy. It’s relatively easy to achieve and it has a significant guidance for the reality.

<!-- b000096 | heading | pages [7] -->
5 Model Theory

<!-- b000097 | heading | pages [7] -->
5.1 Determination of the Number and Location of the Dams

<!-- b000098 | heading | pages [7] -->
5.1.1 Establishment of the model

<!-- b000099 | prose | pages [7] -->
The construction of dams needs to consider many aspects, while at the same time it is subject to economic, social, environmental constraints and other factors. In order to obtain the proper number of dams and their location, we establish a multi-objective model.

<!-- b000100 | prose | pages [7] -->
The Objective

<!-- b000101 | prose | pages [7] -->
 Improve Water Resources Management Capacity

<!-- b000102 | prose | pages [7] -->
The purpose of building smaller dams instead of larger dams is to manage water resources better, mainly to satisfy dweller’s demand for the electricity consumption and water consumption (Including agricultural, industrial and domestic water) of the neighboring cities. Demand may vary between cities, but it is clear that for cities with greater demand, the dam should be built closer to them. so we get that

<!-- b000103 | prose | pages [7] -->
m  min Ele d y X ( , ) i i n i 1

<!-- b000104 | prose | pages [7] -->
m  min Wat d y X ( , ) i i n i 1

<!-- b000105 | prose | pages [7] -->
 Reduce the Cost

<!-- b000106 | prose | pages [7] -->
On the basis of ensuring the water supply and power supply, we should minimize the cost of our plan. The whole cost consists of the removal of the Kariba dam and building new smaller dams. Since the cost of removal is fixed, so we only consider the variable cost(building cost), which is only related to the number of dams. So we should minimize the quantity of the smaller dams.

<!-- b000107 | prose | pages [7] -->
min n

<!-- b000108 | prose | pages [7] -->
The Constraints

<!-- b000109 | prose | pages [7] -->
 Water Balance

<!-- b000110 | prose | pages [7, 8] -->
     W t i ( , ) W t ( 1, ) i Z t k ( , ) T t i ( , )   k ( ) i Z t i and T t i represent the discharge amount of the thi dam at the end of period W t i ， ( , ) ( , ) ( , )

<!-- b000111 | furniture | pages [8] -->
Team # 55069                                                            Page 6 of 28

<!-- b000113 | prose | pages [8] -->
t, the total amount of water released during period t and the amount of natural water in period t

<!-- b000114 | prose | pages [8] -->
  thi dam. If respectively. denotes the set of all higher dams of is empty, the ( )i ( )i

<!-- b000115 | prose | pages [8] -->
corresponding summation is zero.[2]

<!-- b000116 | prose | pages [8] -->
 Water Level

<!-- b000117 | prose | pages [8] -->
The water level in the dam area should be kept between the dead water level and the limited water level in the flood season. Dead Water Level, namely the lowest water level that allows a reservoir to fall off under normal operating conditions. Flood limited water level is the requirements of control over flood to limit reservoirs’ water storage.

<!-- b000118 | prose | pages [8] -->
  DWL WL FWL

<!-- b000119 | prose | pages [8] -->
 Safety

<!-- b000120 | prose | pages [8] -->
The construction of multiple smaller dams is at least as safe as the original larger dams. The safety considerations for dam construction mainly include reducing the probability of dam failure, thereby reducing damage to dams downstream and enhancing resistance ability to extreme weather.

<!-- b000121 | prose | pages [8] -->
 Safety Safety sd Bd

<!-- b000122 | prose | pages [8] -->
represents the safety of multiple dams system, while denotes the safety of Safety Safety sd Bd

<!-- b000123 | prose | pages [8] -->
the existing Kariba dam.

<!-- b000124 | prose | pages [8] -->
 Water Resources Protection

<!-- b000125 | prose | pages [8] -->
The construction of smaller dams should require a higher degree of protection for the water resources as the replacement of the existing dam.

<!-- b000126 | prose | pages [8] -->
 WRP WRP sd Bd

<!-- b000127 | prose | pages [8] -->
WRP represents the environment protection of the multiple dams system, while WRP sd Bd

<!-- b000128 | prose | pages [8] -->
denotes the environment protection of the existing Kariba dam.

<!-- b000129 | prose | pages [8] -->
 Number

<!-- b000130 | prose | pages [8] -->
The number of small dams should be greater than ten and less than twenty. Option 3 is replacing the Kariba dam with a series of ten to twenty smaller dams.

<!-- b000131 | prose | pages [8] -->
To ensure the continuity of the model establishment, the parameters of the constraints will be described in the next part. And in the sixth section, we will clarify how to calculate the demand

<!-- b000132 | prose | pages [8, 9] -->
of electricity( Ele ),the demand of the water( Wat ),the safety of different dams and the i i environment protection of different dams.

<!-- b000133 | furniture | pages [9] -->
Team # 55069                                                            Page 7 of 28

<!-- b000135 | prose | pages [9] -->
To sum up, we model the problem about smaller dams’ number and location decision with multi-objective optimization. The formulas of this model is

<!-- b000136 | prose | pages [9] -->
m  min Ele d y X ( , ) i i n i 1 m  min Wat d y X ( , ) i i n i 1 min n

<!-- b000137 | prose | pages [9] -->
 S t     . . W t i ( , ) W t ( 1, ) i Z t k ( , ) T t i ( , )   k ( ) i   DWL WL FWL

<!-- b000138 | prose | pages [9] -->
 Safety Safety sd Bd

<!-- b000139 | prose | pages [9] -->
 WRP WRP sd Bd

<!-- b000140 | prose | pages [9] -->
  (n=10, 11, 12…..20) 10 n 20

<!-- b000141 | heading | pages [9] -->
5.1.2 The Parameter of the Constraints

<!-- b000142 | prose | pages [9] -->
 The Demand of Electricity

<!-- b000143 | prose | pages [9] -->
The power demand of a city is mainly related to its economic and demographic factors. Our paper uses the city's latest available GDP data as the representative of its economic factors, and the total urban population as the representative of its demographic factor.

<!-- b000144 | prose | pages [9] -->
pop . The GDP of the thi city is GDP .The population of the thi city is i i

<!-- b000145 | prose | pages [9] -->
 The Demand of Water

<!-- b000146 | prose | pages [9] -->
The water consumption of residents is mainly affected by residents' income, water price and other factors. Since within a country, the price difference is relatively small, so here we ignore the price difference.. Therefore, the water consumption of urban residents is mainly affected by the income of residents, We use the city's GNI to represent its urban

<!-- b000147 | prose | pages [9] -->
thi city is GNI . residents. The GNI of the i

<!-- b000148 | prose | pages [9] -->
The Safety of Dams and the Kariba Dam[3] 

<!-- b000149 | prose | pages [9] -->
For the safety of dam construction, our paper mainly consider the index of risk loss as the agent of its safety indicators.

<!-- b000150 | prose | pages [9, 10] -->
Bd equals to P multiply N . P is the R For a single Big dam, its Risk Loss Index(RLI) failure probability of the dam beyond the current code standard. For example, the current code specifies that if a dam's seismic safety standard is 50 years beyond 10%, the probability of failure exceeding the current code specification is 0.1 / 50 = 0.002.N is the life loss of dam failure (we can convert economic loss into life loss in a certain percentage). We use the Dekay & McClelland method to calculate the loss. Thus, the RLI of the Kariba dam is

<!-- b000151 | furniture | pages [10] -->
Team # 55069                                                            Page 8 of 28

<!-- b000153 | prose | pages [10] -->
  Bd . R P K ( ) N K ( )

<!-- b000154 | prose | pages [10] -->
For multiple dam system, the RLI of the thj dam is

<!-- b000155 | prose | pages [10] -->
n       R P j ( ) N j ( ) P l j ( | ) P j ( ) N l ( ) j  l j 1

<!-- b000156 | prose | pages [10] -->
and the RLI of the multiple dam system is

<!-- b000157 | prose | pages [10] -->
n  sd sd R R j  j 1

<!-- b000158 | prose | pages [10] -->
The safety of the multiple dam system should be greater than or at least equal to the safety of n   sd Bd   sd R R the existing Kariba dam. So we get that , that is to say .And n R P K ( ) N K ( ) i  i 1 is an integer greater than ten and less than twenty

<!-- b000159 | prose | pages [10] -->
 The water resources protection of dams

<!-- b000160 | prose | pages [10] -->
According to the International Commission On Large Dams(ICOLD), there are three goals of water resources management[4]

<!-- b000161 | prose | pages [10] -->
 Improved management of the water supply

<!-- b000162 | prose | pages [10] -->
 Improved water quality in our rivers

<!-- b000163 | prose | pages [10] -->
 Improved environmental conditions in the watershed

<!-- b000164 | prose | pages [10] -->
Since there are few branches in the Kariba Gorge, we mainly consider the management of the water supply and the water quality.

<!-- b000165 | prose | pages [10] -->
According to the constraints, the water supply of the multiple-dam system should be greater than the big dam. That is to say

<!-- b000166 | prose | pages [10] -->
 WS WS sd Bd

<!-- b000167 | prose | pages [10] -->
WS equals to the number of the smaller dams multiply the water supply of a smaller dam, sd

<!-- b000168 | prose | pages [10, 11] -->
while represents the water supply of the Kariba Dam. WS Bd Besides, the water quality of the multiple-dam system should be greater than the Kariba dam.

<!-- b000169 | furniture | pages [11] -->
Team # 55069                                                            Page 9 of 28

<!-- b000171 | prose | pages [11] -->
 , WQ WQ sd Bd

<!-- b000172 | prose | pages [11] -->
WQ represents the expected average water quality of the Lake Kariba if the authority adopt sd

<!-- b000173 | prose | pages [11] -->
the option three, while represents the present water quality of the Lake Kariba. WQ Bd

<!-- b000174 | heading | pages [11] -->
5.2 Joint Operation of Dam System Model

<!-- b000175 | prose | pages [11] -->
Joint operation of dam system can utilize the differences between dam capacity and hydrologic condition, so that we develop a joint compensation effect for the dam group and make full use of water resources. Compared with the traditional single large dam, the dam group establish on the basis of multi –dam system, which could help us take advantage of water resources for our social benefits, including economic and social benefits. Therefore, it is necessary to establish an effective water resources dispatching scheme.

<!-- b000176 | prose | pages [11] -->
  j 1... T i 1... n In order to better express our model，we let indicates the number of dams，

<!-- b000177 | prose | pages [11] -->
V illustrates the thi dam’s water storage during the denotes the cycle of water dispatching， ij

<!-- b000178 | prose | pages [11] -->
thj period.[5]

<!-- b000179 | prose | pages [11] -->
The Objective

<!-- b000180 | prose | pages [11] -->
The hydropower station mainly bring about economic and social benefits. But obviously, hydropower station can bring magnificent economic benefits. Among them, the most direct indication is the dam power generation. Therefore, taking the reservoir power generation as the revelation of economic benefit.

<!-- b000181 | prose | pages [11] -->
n T   I K * q * H * t  e i ij ij   i 1 j 1

<!-- b000182 | prose | pages [11] -->
q is the discharge flow of the H is the hydraulic head of thi dam in the thj period， thi dam ij ij

<!-- b000183 | prose | pages [11] -->
is the time period. K is the force-voltage factor of the thi dam，t thj period， in the i

<!-- b000184 | prose | pages [11] -->
In addition to creating enormous economic benefits, a large dam can also bring huge social benefits. Through the construction of dams, it can meet the need of a large number of industrial and agricultural water, also the domestic water.

<!-- b000185 | furniture | pages [12] -->
Team # 55069                                                            Page 10 of 28

<!-- b000186 | prose | pages [12] -->
n T   I ( S D )  s ij ij   i 1 i 1

<!-- b000187 | prose | pages [12] -->
S is the actual water supply thi dam in the tht stage， D is water demand or planned water ij ij

<!-- b000188 | prose | pages [12] -->
thi dam in the tht stage. supply of the

<!-- b000189 | prose | pages [12] -->
Therefore, we should make full use of water resources so as to make the economic and social benefits as large as possible.[6]

<!-- b000190 | prose | pages [12] -->
  I max( I I ) e s

<!-- b000191 | prose | pages [12] -->
The Constraints

<!-- b000192 | prose | pages [12] -->
 Water Balance

<!-- b000193 | prose | pages [12] -->
   

<!-- b000194 | heading | pages [12] -->
V V

<!-- b000195 | prose | pages [12] -->
( Q q ) t L i t ,( 1) it it it it

<!-- b000196 | prose | pages [12] -->
  Q q QJ   i t ,( 1) ( i 1), t it

<!-- b000197 | prose | pages [12] -->
tht period of the thi ijq are the average inflow into the dam and discharge volume in the Q 、 it

<!-- b000198 | prose | pages [12] -->
itL is the evaporation and leakage loss. thi dam QJ is the runoff volume between the dam, it

<!-- b000199 | prose | pages [12] -->
thj dam. and the

<!-- b000200 | prose | pages [12] -->
 Capacity of the Dam

<!-- b000201 | prose | pages [12] -->
To prevent floods and droughts，The capacity of each dam must be limited.

<!-- b000202 | prose | pages [12] -->
  V min V V max i it i

<!-- b000203 | prose | pages [12] -->
are the upper and lower limit of the thi dam’s water storage，namely the V min i V max i 、

<!-- b000204 | prose | pages [12] -->
dead capacity and the flood control capacity.

<!-- b000205 | prose | pages [12] -->
 Discharge Flow Constraint

<!-- b000206 | prose | pages [12] -->
In order to keep the normal life standard and to maintain the downstream ecological water use,

<!-- b000207 | prose | pages [12] -->
q min i we must ensure the certain discharge of water, we employ to indicate the minimal

<!-- b000208 | prose | pages [12] -->
discharge of water. Because of the limitation of the dam itself and the purpose of flood control, q max i there need to be a maximal discharge capacity constraint

<!-- b000209 | prose | pages [12, 13] -->
  q m in q q max i it i In conclusion, in order to make economic benefit and social benefit as large as possible while satisfying the constraint conditions, we need to develop water resources optimized dispatching scheme.

<!-- b000210 | furniture | pages [13] -->
Team # 55069                                                            Page 11 of 28

<!-- b000212 | prose | pages [13] -->
n T n T      max I K * q * H * t ( S D ) i ij ij ij ij     i 1 j 1 i 1 i 1

<!-- b000213 | prose | pages [13] -->
     V V ( Q q )* t L  i , ( t 1) it it it it    Q q QJ    i , ( t 1) ( i 1), t it s t . .   V min V V max  i it i    q m in q q max  i it i

<!-- b000214 | prose | pages [13] -->
V 、itq are the interval-type variable，min i 、min i q V correspond to meet the basic industrial it

<!-- b000215 | prose | pages [13] -->
and agricultural water、domestic water and ecological water，they are the dead water level.

<!-- b000216 | prose | pages [13] -->
For safety considerations such as flood control，max i V 、max i q are the maximal water level.

<!-- b000217 | prose | pages [13] -->
itq .[7] We let [ Vf VF to be the of , ] V ,[ qf qF is the optimum interval of , ] i i i i it

<!-- b000218 | prose | pages [13] -->
      1 ( Vf V ) / ( Vf V min ), V min V Vf i it i i i it i    1, Vf V VF  i it i   it     1 ( V VF ) / ( max V VF VF ), V V max  it i i i i it i  0, else

<!-- b000219 | prose | pages [13] -->
1 N     t it N  i 1

<!-- b000220 | prose | pages [13] -->
      1 ( qf q ) / ( qf q min ), min q q qf i it i i i it i    1, qf q qF  i it i   it     1 ( q qF ) / ( max q qF ), qF q q max  it i i i i it i  0, else

<!-- b000221 | prose | pages [13] -->
1 N     t it N  i 1

<!-- b000222 | heading | pages [13] -->
6 Model Implementation and Results

<!-- b000223 | heading | pages [13] -->
6.1 The Number and Location

<!-- b000224 | prose | pages [13, 14] -->
 Measuring the demand of the nearby city TOPSIS (Technique for Order Preference by Similarity to an Ideal Solution) is a commonly used and effective method in multi-objective decision analysis. Hence ,we employ this model and then investigate extended TOPSIS to evaluate the demand of  electricity and water of each city.

<!-- b000225 | furniture | pages [14] -->
Team # 55069                                                            Page 12 of 28

<!-- b000227 | prose | pages [14] -->
Then we use the data to calculate the demand of the electricity and water with TOPSIS, and part of the results is shown in Table 1.

<!-- b000228 | caption | pages [14] -->
Table 1 The Demand of Electricity and Water

<!-- b000229 | prose | pages [14] -->
 Calculate the shortest distance from each dam to each city

<!-- b000230 | prose | pages [14] -->
The dam should be built in the valley of the river fully, because the project is small with low cost. Moreover, the construction of small dams is mainly to replace the larger dam, so the small dam should be constructed mainly in the downstream of the Kariba dam in the canyon. Figure 1 is the suitable site for building dams.

<!-- b000231 | caption | pages [14] -->
Figure 1 The Suitable Gorge for Building Dams

<!-- b000232 | prose | pages [14] -->
With respect to the option 3 that we need to construct 10 to 20 small dams, considering the geological factors around the dam, we first select the suitable location of the 20 dams.

<!-- b000233 | furniture | pages [15] -->
Team # 55069                                                            Page 13 of 28

<!-- b000234 | prose | pages [15] -->
According to our model, we use the distance from the dam to the center of the city as a representative of the distance to the city. A total of 25 cities are selected close to the Kariba gorge, including 15 cities in Zambia, 10 cities in Zimbabwe. We search and calculate the shortest distance and path of each dam to the city through Google maps, and the results of some small dams to the cities are shown in Table 2.

<!-- b000235 | caption | pages [15] -->
Table 2 The Distance Between the Dams and the City(Part)

<!-- b000236 | prose | pages [15] -->
 The Data of Other Factors

<!-- b000237 | prose | pages [15] -->
At the same time, we collect the data of other related factors through the Zambia National Bureau of Statistics, the World Bank, the World Commission on Dams and other institutions to gain the relevant statistics.

<!-- b000238 | caption | pages [15] -->
Table 3 The Data of Other Factors

<!-- b000239 | prose | pages [15] -->
DWL NWL FWL BFWL RLI WS WQ

<!-- b000240 | prose | pages [15] -->
Kariba 475.5 484.6 490 476.7 9000 608.5 19

<!-- b000241 | prose | pages [15] -->
 Multiple 382 408 412 385 e n WS n  sd WQ R e i i 1

<!-- b000242 | prose | pages [15] -->
Under normal circumstances the water level should be higher than the dead water level, and lower than the normal position. But before the flood season, the water level is lower than the limit of water level.

<!-- b000243 | prose | pages [15] -->
 The numbers and the location

<!-- b000244 | prose | pages [15] -->
This optimal problem belongs to the NP-hard problem. We can’t solve it in polynomial time. So we can only use heuristic algorithms such as artificial neural networks, genetic algorithm, simulated annealing to obtain the approximate solution. In this paper, we select the genetic algorithm to solve the problem.

<!-- b000245 | prose | pages [15, 16] -->
We run the program repeatedly, and finally get a relatively good result and determine our number and location of the dams. There should be 12 smaller dams in the Kariba Gorge. Besides, we select the optimal 12 dam location to maximize our objective function from 20 appropriate dam sites. The sixth and twelfth site locations are listed in the Table 4

<!-- b000246 | furniture | pages [16] -->
Team # 55069                                                            Page 14 of 28

<!-- b000248 | caption | pages [16] -->
Table 4 The Location of the Dam

<!-- b000249 | prose | pages [16] -->
At the same time, we will also mark the location of the small dam on the map, we put the location of the sixth and twelfth dam on the map. We can see it on the Figure 2 and Figure 3

<!-- b000250 | caption | pages [16] -->
Figure 2 The Location of the 6th Dam           Figure 3 The Location of the 12th Dam

<!-- b000251 | heading | pages [16] -->
6.2 The Strategy of Modulating Water Flow

<!-- b000252 | prose | pages [16] -->
Traditional optimization algorithm mostly belongs to the convex optimization category. It demands a unique global optimal solution, which is often used in practical applications. A number of heuristic intelligent algorithm, for example genetic algorithm etc.These methods show that the algorithm can work out satisfactory results for solving the optimization problem. Employing joint operation of dam system model, we use genetic algorithm and Matlab2014 for the solution.[8]

<!-- b000253 | prose | pages [16] -->
By running the genetic algorithm and adjusting the parameters, we obtain a relatively satisfactory result, and then develop a joint operation of dam system model.(The picture of the results is shown in the appendix part four.)

<!-- b000254 | prose | pages [16] -->
 Normal Flow Year：Take the climate and hydrological conditions of the average of nearly 5 years to simulate normal climatic conditions.

<!-- b000255 | prose | pages [16, 17] -->
In normal years, the water resources dispatching of the dam system shows obvious seasonal difference. In the dry season from June to September, the discharge of each reservoir reaches the bottom line. Compared with the middle and lower reaches of the river, upper and middle reaches of water resources and reserves are relatively abundant, therefore, still a lot of water could be scheduled downstream. But until the rainy season from November to March, the precipitation intensity and the discharge of each dam are very large. The results show that the discharge index and storage capacity index perform better in May and October, which are in the optimum range, while the other month are all above 0.7, this is a satisfactory result.

<!-- b000256 | furniture | pages [17] -->
Team # 55069                                                            Page 15 of 28

<!-- b000258 | prose | pages [17] -->
 Low Flow Year: The monthly precipitation is taken as the highest value in the past 30 years, simulating the more serious flood threat..

<!-- b000259 | prose | pages [17] -->
When the annual precipitation decreases, each dam discharge is significantly lower, but the discharge index and the capacity index is still above 0.7, which reflects the joint operation of dam system still has obvious effect to resist abnormal weather like the drought condition.

<!-- b000260 | prose | pages [17] -->
 High Flow Year：The monthly precipitation is taken as the highest value inthe past 30 years, simulating the more serious flood threat.

<!-- b000261 | prose | pages [17] -->
When the annual precipitation has increased significantly, then the reservoir’s discharge would increase.  While the discharge of the rainy season increases a lot, but in dry season the increase range is smaller, which makes the discharge capacity index and volume index increase significantly from May to September. Although the index decreases significantly in November and February the figure are more than 0.7, is still relatively satisfactory.

<!-- b000262 | prose | pages [17] -->
 Differentiation Year：The precipitation from May to September is taken as the lowest value in the past 30 years, the precipitation from October to April was taken as the highest value in the past 30 years. So that we could simulate drought, flood significantly differentiated condition..

<!-- b000263 | prose | pages [17] -->
When confronted with the differentiation year where there comes rainy season when the precipitation increases and the dry season when the precipitation decreases all come about in one year. The discharge flow of each reservoir expands seasonally, which makes the discharge index and storage capacity index of each month decrease, and it is more obvious in the rainy season. Which can not be ignored is that the discharge flow indicators and storage capacity indicators remained at 0.7 or more.[9]

<!-- b000264 | heading | pages [17] -->
7. Sensitivity Analysis

<!-- b000265 | heading | pages [17] -->
7.1 The Model of Determination of the Number and Location

<!-- b000266 | prose | pages [17] -->
 Remove an important city of both countries

<!-- b000267 | prose | pages [17] -->
In the questions we discussed above，we have selected 15 cities in Zambia，10 cities in Zimbabwe to specify the number and placement of the newly built smaller dams. Among the sensitivity analysis, we remove important cities of the two countries, thus, we could see whether this movement would influence the number and placement of constructing dams.

<!-- b000268 | prose | pages [17] -->
In our analysis, we leave out Lusaka (The capital city of Zambia) and Harare(The capital city of Zimbabwe) from our original cities, yet, we still use the multi objective optimization model and genetic algorithm we already established to calculate the number and placement of smaller dams. We discover that the optimal number of constructing dams is also 12, but the location of each dam is slightly changed. Just the fourth and the eleventh dam’s place changes a lot, while other dam’s place just changes a little. Therefore, we list the location of the fourth and the eleventh dam’s site in Table 5.

<!-- b000269 | furniture | pages [18] -->
Team # 55069                                                            Page 16 of 28

<!-- b000270 | prose | pages [18] -->
To sum up, the influence of removing bigger cities is not that much. Still in accordance with our former model, we could also draw the conclusion that large cities exert magnificent impact on the selection of the dam’s location. Hence, putting larger cities into our model while constructing dams is an appropriate choice.

<!-- b000271 | caption | pages [18] -->
Table 5 The Location of 4th Dam and 11th Dam

<!-- b000272 | prose | pages [18] -->
 Change the measurement of the economic development index

<!-- b000273 | prose | pages [18] -->
In the model we have discussed before, we mainly employ the current GDP of each city as a measure of the economic development, which is also used as one of the indicators to measure the water and electricity demand. Here, we will use its GDP growth rate as an agent indicator for the city's economic development, and change its GDP growth rate to observe whether it has the impact on the number and location of the construction of dams.

<!-- b000274 | prose | pages [18] -->
Our paper first use economic growth data of the city to measure its water and electricity demand, and then float up and down of the basis, the maximum change is up to 8%. The impact of economic growth on the number of dams is shown in Table 6.

<!-- b000275 | caption | pages [18] -->
Table 6 The Sensitivity of the GDP growth rate

<!-- b000276 | prose | pages [18] -->
From the table above we can see that the changing of the economic growth rate for the number of the building small dam is relatively small. Even reaching to 8% changes, building two more small dams from the original can meet the demand of electricity and water. While Zambia and Zimbabwe are African countries, so that they are in a relatively poor condition. Due to the lack of economic development momentum, the change in its economic growth in the future is relatively small. Therefore, it is a reasonable choice of constructing 12 dams.

<!-- b000277 | furniture | pages [19] -->
Team # 55069                                                            Page 17 of 28

<!-- b000278 | prose | pages [19] -->
Alteration in the economic growth rate has little impact on the position of dams. Basing on the fact that Kariba gorge is about 34.9 kilometers, and we only need to build 10 to 20 small dam in the canyon, also small dams need to maintain a certain distance, so that the small dam’s location is relatively stable and the change is not great.

<!-- b000279 | prose | pages [19] -->
In conclusion, we can see that the representative index of its economic development is reasonable. Despite the fact that the figure floats up and down, its influence on the number and location of small dams is relatively small. It also shows that the model we established in the previous paper about the location and quantity of small dams is robust and has good adaptability to the reality.

<!-- b000280 | heading | pages [19] -->
7.2  The Model of Modulating Water Flow

<!-- b000281 | prose | pages [19] -->
Output coefficient is a comprehensive benefit coefficient which reflects water-turbine generator set’s overall efficiency. It equals to turbine efficiency, generator efficiency, transfer efficiency multiply invariant constant 9.81. Its value is up to the scale of Hydropower Station Dam. For Large hydropower station the value is about 8.5.For media hydropower station the value is about 8-8.5. While for small hydropower station the value is about 6.0-8.0. Multiply the coefficient, water-head and water-flow and the answer will be the unit’s output.

<!-- b000282 | prose | pages [19] -->
We analyze the change of output coefficient’s influence on the joint operation of dam system in the Table 7.

<!-- b000283 | caption | pages [19] -->
Table 7 The Sensitivity of the Output Coefficient

<!-- b000284 | prose | pages [19] -->
 15% We could see from the Table 7 that,output coefficient K change about would bring about  and  change for about only  5% . This indicates that output coefficient K is not an important factor for joint operation of the dam system.

<!-- b000285 | heading | pages [19] -->
8. Further Discussion

<!-- b000286 | prose | pages [19, 20] -->
 Take the future benefits into account. Reservoir operation not only has the current economic and social benefits, but also has the economic and social benefits in the future The future economic benefits can be expressed by the total energy storage at the end of the dispatching cycle, the greater the total energy storage, the more the potential for future development. The social benefits in the future can be illustrated as the total capacity in the last scheduling period. Generally speaking, the more water storage in the reservoir, the more able to meet the needs of future generations.

<!-- b000287 | furniture | pages [20] -->
Team # 55069                                                            Page 18 of 28

<!-- b000289 | prose | pages [20] -->
n T     I [ K * q * H * t ( h h )( Q q )]   e i ij ij ( i 1), j i j , ij ij   i 1 j 1

<!-- b000290 | prose | pages [20] -->
n T     I V ( S D ) s T ij ij   i 1 i 1

<!-- b000291 | prose | pages [20] -->
h illustrates the water level of V indicates the dam’s water storage thi dam in the thj period, ij T

<!-- b000292 | prose | pages [20] -->
in the end of the dispatching period.

<!-- b000293 | prose | pages [20] -->
 Increase ecological benefits：Most people pay more attention to the traditional functions of power generation, flood control, water supply and so on. We will further consider the ecological benefits of the reservoir. We do not take the ecological flow as a constraint, but consider it as one of the scheduling objectives, but there are many difficulties.

<!-- b000294 | prose | pages [20] -->
n T  I f V Q q de ( , , , ) en ij ij ij ij   i 1 j 1

<!-- b000295 | prose | pages [20] -->
de is the ecological water requirement of the thi dam in the thj period. ij

<!-- b000296 | prose | pages [20] -->
 In order to avoid the large change of the reservoir water level, which could lead to the change of the geological condition, and even cause the reservoir earthquake. So we will

<!-- b000297 | prose | pages [20] -->
 is the allowable variation    increase the constraint condition. ,in which h h i  it i , ( t 1) i

<!-- b000298 | prose | pages [20] -->
of reservoir water level.

<!-- b000299 | heading | pages [20] -->
9 Strengths and Weaknesses

<!-- b000300 | heading | pages [20] -->
9.1 Strengths

<!-- b000301 | prose | pages [20] -->
 Our models are robust while the parameters changes. That is to say, a slight change of parameter will not cause a significant change of the results.

<!-- b000302 | prose | pages [20] -->
 Our models can be well applied in other places and we just need to change a little the specific conditions.

<!-- b000303 | prose | pages [20, 21] -->
 Based on different situation, we develop the corresponding modulating strategy and make a relative comprehensive plan. This can provide a specific guidance for the ZRA.

<!-- b000304 | furniture | pages [21] -->
Team # 55069                                                            Page 19 of 28

<!-- b000306 | prose | pages [21] -->
 Our data comes from the official website such as Central Statistical Office, Zambia, which is believable.

<!-- b000307 | heading | pages [21] -->
9.2 Weaknesses

<!-- b000308 | prose | pages [21] -->
 Our model didn’t consider the economic, social and environment benefits in the future. We mainly focus on the current benefits. But in fact, future prospects is important for sustainable development. So we add it to the further discussion and hope we can solve it in the future.

<!-- b000309 | prose | pages [21] -->
 There are not much data regarding the demand of the electricity and water. So the analysis of the demand may be not exhaustive and it may have some deviations. But it didn’t affect the results significantly.

<!-- b000310 | prose | pages [21] -->
 The data of some parameters is forecast data because we don’t build the dams. However, based on the sensitivity analysis, they will not make a great difference if parameters are slightly changed.

<!-- b000311 | heading | pages [21] -->
10 Conclusion

<!-- b000312 | prose | pages [21] -->
Through the establishment of three models, we evaluate the three plans respectively. First,we select the number and location of the dam, then plan the joint operation of the dam system. We consider the comprehensive evaluation of three options from five aspects: direct cost, potential cost, economic benefits, environmental benefits and social benefits. Through the AHP analysis, we draw the conclusion that option three is a relatively good solution.

<!-- b000313 | prose | pages [21] -->
Then, we establish a multi-objective optimization model to determine the number and location of the dams. We let the water resources management capacity and cost to be the objective function, and let the water balance function, water level limit, the protection of water resources and the number to be the constraints. We also use genetic algorithm to solve the problem and find that the 12 dam is a relatively satisfactory results, and determine their geographic location.

<!-- b000314 | prose | pages [21] -->
After determining the number and location of the dam, we established a joint operation model of dam system. We let the economic and social benefits as the goal, water balance function and flow limitation to be the constraints. Considering four different year type, we use genetic algorithm to solve and determine the corresponding scheduling scheme, Also,the sensitivity results show that the joint operation of dams can be well adapted to different climatic conditions.

<!-- b000315 | prose | pages [21] -->
Finally, we make an objective analysis of the advantages and disadvantages of the model and make an attempt to further expand the model in order to make our model and method more successful.

<!-- b000316 | furniture | pages [22] -->
Team # 55069                                                            Page 20 of 28

<!-- b000317 | heading | pages [22] -->
11 The Evaluation of Three Options

<!-- b000318 | prose | pages [22] -->
South Africa had just warned that the dam was in desperate need of rehabilitation. The reasons may as follows :

<!-- b000319 | prose | pages [22] -->
 Forcing people who dwell downstream to evacuate since the heavy rain might lead to a release of water from the dam.

<!-- b000320 | prose | pages [22] -->
 Basing on a seemingly solid bed of basalt，the Kariba Dam has been eroded by the torrents from the spillway, which could give rise to severe collapse without urgent repairs.

<!-- b000321 | prose | pages [22] -->
With the three options already given, we adopt AHP model using two most influential criterion to provide a brief overview of potential costs and benefits.

<!-- b000322 | prose | pages [22] -->
Jery Stedinger and Pete Loucks（February 1982）[10]thought that evaluation criterion of dam should include reliability ,resiliency, and vulnerability criteria; Mohamed Rami Mahmoud and Luis A. Garcia (July 2000) [11] propose different multicriteria evaluation methods for the Red Bluff diversion dam. With the help of the current literatures, we develop AHP model considering these main factors.

<!-- b000323 | heading | pages [22] -->
11.1  Establish a Hierarchical Model

<!-- b000324 | prose | pages [22] -->
Cost Index

<!-- b000325 | prose | pages [22] -->
Chengxinwen (2008) [12] proposed the components of the cost while constructing operating or repairing. In addition, the expense of rebuilding the Kariba Dam is significantly greater than just repairing the existing one. The factors below are of great importance.

<!-- b000326 | prose | pages [22] -->
 Direct cost(Demolition[A1] 、Construction[A2] 、Operation[A3] 、Maintenance and management expense[A4])

<!-- b000327 | prose | pages [22] -->
 Potential cost(Dam failure loss[B1]、Flowage damage[B2])

<!-- b000328 | prose | pages [22] -->
Benefit Index

<!-- b000329 | prose | pages [22] -->
Replacing the bigger dams with ten to twenty smaller dams could bring about advantages and disadvantages. Our goal is to seek out whether it is beneficial or not to removing the Kariba dam. We divide the benefit index into three main categories below:[ 13]

<!-- b000330 | prose | pages [22] -->
 Economic effect (Irrigation[C1]、Water-supply[C2]、Power generation[C3]、Navigation benefits[C4])

<!-- b000331 | prose | pages [22] -->
 Environmental effect (Climate change[D1]；Alteration in river ecosystem[D2])

<!-- b000332 | prose | pages [22] -->
 Social effect (Flood control benefit[E1]；Drought resistance benefit[E2])

<!-- b000333 | prose | pages [22, 23] -->
Through above analysis of the three main criterion, which affect evaluation significantly, hierarchy figure is shown in In Figure 4 we let the Direct cost to be Index A;Potential cost to be Index B;Economic effect to be Index C;Environmental effect to be Index D;Social effect to be index E;We divide these index into more specific index(namely A1 A2 A3 etc.) and we show that above.

<!-- b000334 | furniture | pages [23] -->
Team # 55069                                                            Page 21 of 28

<!-- b000335 | caption | pages [23] -->
Figure 4  Hierarchy figure

<!-- b000337 | heading | pages [23] -->
11.2  Analysis and Results

<!-- b000338 | prose | pages [23] -->
We construct comparison matrix by comparison method of 1-7，then we get the weights of each index.(Complete matrix of project hierarchy can be seen in the appendix.)[14]

<!-- b000339 | caption | pages [23] -->
Table 8 Pairwise Comparison Matrix of Hierarchy II-III

<!-- b000340 | prose | pages [23] -->
Comprehensive Direct cost Potential cost Weight impact Direct cost 1 4 0.8 Potential cost 1/4 1 0.2

<!-- b000341 | caption | pages [23] -->
Table 9 Pairwise Comparison Matrix of Hierarchy II-III

<!-- b000342 | prose | pages [23] -->
Comprehensive Economic Environmental Social Weight impact effect effect effect Economic effect 1 2 5 0.2908 Environmental 1/2 1 3 0.1545 effect Social effect 1/5 1/3 1 0.0547 Consistency ratio：0.0961

<!-- b000343 | prose | pages [23] -->
With the five index. only the Economic and Environment effect are positive. Moreover, from above tables, we know that all Consistency Test is right.

<!-- b000344 | prose | pages [23] -->
We could draw conclusions from the weight that the direct cost is of great importance to constructing a dam, potential cost has close relationship to repairing a dam; Also, we could gain better economic and navigation effect when we choose option 3.[15]

<!-- b000345 | prose | pages [23] -->
Due to the index and results above, we arrive at a conclusion that option 3 is our best choice to concerning the potential cost and benefit.

<!-- b000346 | furniture | pages [24] -->
Team # 55069                                                            Page 22 of 28

<!-- b000347 | heading | pages [24] -->
Reference

<!-- b000348 | references | pages [24] -->
[1] http://www.zaraho.org.zm/hydrology/lake-levels

<!-- b000349 | references | pages [24] -->
[2]Grigier J C and Stedinger J R. Algorithms for network programming. Wiley-interscience

<!-- b000350 | references | pages [24] -->
publication, 1980

<!-- b000351 | references | pages [24] -->
[3] Dekay M L， Mcclelland G H. Predicting loss of life in cases of dam failure and flash

<!-- b000352 | references | pages [24] -->
flood[J]. Risk analysis， 1993， 13(2):193-205

<!-- b000353 | references | pages [24] -->
[4] http://www.icold-cigb.org/GB/dams/dams_and_environment.asp

<!-- b000354 | references | pages [24] -->
[5]Ayvaz MT (2009a) Application of Harmony Search algorithm to the solution of groundwater

<!-- b000355 | references | pages [24] -->
management models. Adv Water Resour 32:916–924

<!-- b000356 | references | pages [24] -->
[6]Chang L C， Chang F J． Multi-objective evolutionary algorithm for operating parallel

<!-- b000357 | references | pages [24] -->
reservoir system [J]． Journal of Hydrology，2009，377：12-20．

<!-- b000358 | references | pages [24] -->
[7]Approved consolidated baseline and monitoring methodology ACM0002

<!-- b000359 | references | pages [24] -->
[8] http://www.zaraho.org.zm/

<!-- b000360 | references | pages [24] -->
[9] http://worldweather.wmo.int/en/city.html?cityId=966

<!-- b000361 | references | pages [24] -->
[10] Larkin, P. A.,  Maybe you can't get there from hcre:  Hi\tory  of research  in  relation

<!-- b000362 | references | pages [24] -->
to management of kicific Salmon. J. Fish. Res. Board Can.. 36(1). 98-106,1979.

<!-- b000363 | references | pages [24] -->
[11] Tecle, A., 1992. Selecting a multicriterion decision making techniquefor watershed

<!-- b000364 | references | pages [24] -->
resources management. Water Resources Bulletin 28(1), 129–140.

<!-- b000365 | references | pages [24] -->
[12] Larkin,  P. A.,  Maybe  you  can't  get  there  from  hcre:  Hi\tory  of research

<!-- b000366 | references | pages [24] -->
in  relation  to management  of  kicific  Salmon.  J. Fish. Res. Board Can.. 36(1). 98-

<!-- b000367 | references | pages [24] -->
106,  1979.

<!-- b000368 | references | pages [24] -->
[13] Loucks, D.  P., J. R.Stedinger. and D.  A. Hiuth.  \\.crfer Hr.courre Systems Planning

<!-- b000369 | references | pages [24] -->
and Analysis, Rent~cc-Hall.  Engleu-ood Cliffs. New Jersev.  1981.

<!-- b000370 | references | pages [24] -->
[14] Mark, R. K.,  and  D.  E.  Stuart-Alexander. D~sa*tcr  as a ncccssclry part of

<!-- b000371 | references | pages [24] -->
benefit-cost analyses. Sclrnrr. 197,  I  ItrO.  1977.

<!-- b000372 | references | pages [24] -->
[15] Velikanov,  A.  K.,  The  aspects  of  lonp-tcnr, water  re- sources planning  as

<!-- b000373 | references | pages [24] -->
applied  to  the  integr~ted  regional  development  problem,  Collahor.  Pap.  CP-

<!-- b000374 | references | pages [24] -->
37-l.  11-11,  In>[.  for  Appl. Systems Anal.,  Laxenburg, Austria. Mnv  1979.

<!-- b000375 | furniture | pages [25] -->
Team # 55069                                                            Page 23 of 28

<!-- b000376 | heading | pages [25] -->
Appendix

<!-- b000377 | prose | pages [25] -->
Part1: Comparison matrix of criterion hierarchy

<!-- b000378 | caption | pages [25] -->
Table 10 Pairwise comparison matrix of hierarchy II-III

<!-- b000379 | prose | pages [25] -->
Comprehensive Direct cost Potential cost Weight impact Direct cost 1 4 0.8 Potential cost 1/4 1 0.2

<!-- b000380 | caption | pages [25] -->
Table 11 Pairwise comparison matrix of hierarchy II-III

<!-- b000381 | prose | pages [25] -->
Comprehensive Economic Environmental Social Weight impact effect effect effect Economic 1 2 5 0.2908 effect Environmental 1/2 1 3 0.1545 effect Social 1/5 1/3 1 0.0547 effect Consistency ratio：0.0961

<!-- b000382 | caption | pages [25] -->
Table 12 Pairwise comparison matrix of hierarchyIII-IV

<!-- b000383 | prose | pages [25] -->
Comprehensive Demolition Construction Operation Maintenance Weight impact expense expense expense Management expense Demolition 1 1/9 1/2 3 0.0403 Construction 9 1 4 9 0.2672 Operation 2 1/4 1 4 0.0728 Maintenance 1/3 1/9 1/4 1 0.0197 management Consistency ratio: 0.0405

<!-- b000384 | caption | pages [25] -->
Table 13 Pairwise comparison matrix of hierarchy III-IV

<!-- b000385 | prose | pages [25, 26] -->
Comprehensive Dam failure loss Flowage damage Weight impact Dam failure loss 1 1/5 0.0167 Flowage damage 5 1 0.0833 Consistency ratio：0.0122 Comprehensive Irrigation Water- Power Navigation Weight impact supply generation benefits Irrigation 1 3 1/5 2 0.0466 Water-supply 1/3 1 1/9 1/4 0.0143 Power 5 9 1 8 0.1968 Navigation 1/2 4 1/8 1 0.0331 Consistency ratio：0.0684

<!-- b000386 | furniture | pages [26] -->
Team # 55069                                                            Page 24 of 28

<!-- b000387 | caption | pages [26] -->
Table 14 Pairwise comparison matrix of hierarchy III-IV

<!-- b000389 | caption | pages [26] -->
Table 15. Pairwise comparison matrix of hierarchy III-IV

<!-- b000390 | prose | pages [26] -->
Comprehensive Climate change Alteration in river Weight impact ecosystem Climate change 1 2 0.1030 Alteration 1/2 1 0.0513 Consistency ratio：0.0674

<!-- b000391 | caption | pages [26] -->
Table 16. Pairwise comparison matrix of hierarchy III-IV

<!-- b000392 | prose | pages [26] -->
Comprehensive Flood control Drought resistance Weight impact benefit benefit Flood control 1 3 0.0410 benefit Drought resistance 1/3 1 0.0137 benefit Consistency ratio：0.021 Part2: Comparison matrix of project hierarchy A1 Op1 Op2 Op3 A2 Op1 Op2 Op3 A3 Op1 Op2 Op3

<!-- b000393 | prose | pages [26] -->
Op1 1 1/6 2 Op1 1 1/10 2 Op1 1 1/3 2

<!-- b000394 | prose | pages [26] -->
Op2 6 1 8 Op2 10 1 11 Op2 3 1 2

<!-- b000395 | prose | pages [26] -->
Op3 1/2 1/8 1 Op3 1/2 1/11 1 Op3 1/2 1/2 1

<!-- b000396 | prose | pages [26] -->
A4 Op1 Op2 Op3 B1 Op1 Op2 Op3 B2 Op1 Op2 Op3

<!-- b000397 | prose | pages [26] -->
Op1 1 2 3 Op1 1 2 4 Op1 1 4 6

<!-- b000398 | prose | pages [26] -->
Op2 1/2 1 2 Op2 1/2 1 2 Op2 1/4 1 3

<!-- b000399 | prose | pages [26] -->
Op3 1/3 1/2 1 Op3 1/4 1/2 1 Op3 1/6 1/3 1

<!-- b000400 | prose | pages [26] -->
C1 Op1 Op2 Op3 C2 Op1 Op2 Op3 C3 Op1 Op2 Op3

<!-- b000401 | prose | pages [26] -->
Op1 1 1/2 1/3 Op1 1 1/3 1/4 Op1 1 1/2 3

<!-- b000402 | prose | pages [26] -->
Op2 2 1 1/2 Op2 3 1 1/2 Op2 2 1 4

<!-- b000403 | prose | pages [26] -->
Op3 3 2 1 Op3 4 2 1 Op3 1/3 1/4 1

<!-- b000404 | prose | pages [26, 27] -->
C4 Op1 Op2 Op3 D1 Op1 Op2 Op3 D2 Op1 Op2 Op3 Op1 1 1/2 2 Op1 1 4 1/2 Op1 1 4 1/2

<!-- b000405 | furniture | pages [27] -->
Team # 55069                                                            Page 25 of 28

<!-- b000407 | prose | pages [27] -->
Op2 2 1 3 Op2 1/4 1 1/7 Op2 1/4 1 1/8

<!-- b000408 | prose | pages [27] -->
Op3 1/2 1/3 1 Op3 2 7 1 Op3 2 8 1

<!-- b000409 | prose | pages [27] -->
E1 Op1 Op2 Op3 E2 Op1 Op2 Op3

<!-- b000410 | prose | pages [27] -->
Op1 1 1/2 1/6 Op1 1 1/2 1/4

<!-- b000411 | prose | pages [27] -->
Op2 2 1 1/8 Op2 2 1 1/3

<!-- b000412 | prose | pages [27] -->
Op3 6 8 1 Op3 4 3 1

<!-- b000413 | heading | pages [27] -->
Part three :the data of model of determination of number and location

<!-- b000414 | heading | pages [27] -->
Part four: the model of modulating of water flow

<!-- b000415 | prose | pages [27, 28] -->
 The climate and hydrology of Kariba area Mean Daily Mean Daily Minimum Maximum Mean Total Mean Number Month Temperature Temperature Rainfall of Rain Days Jan 21.8 31 191.6 16 Feb 21.4 30.8 157.7 13 Mar 20.7 31.2 112.5 10 Apr 18.5 30.5 30 3 May 14.3 28.5 4.2 1 Jun 11.2 26.3 1 0 Jul 11.1 26.3 0.6 0 Aug 13.9 28.9 0.1 0 Sep 19.1 32.9 0.6 0 Oct 23.2 35.1 17.8 2 Nov 23.4 33.9 74.4 7 Dec 22.1 31.3 175 14

<!-- b000416 | furniture | pages [28] -->
Team # 55069                                                            Page 26 of 28

<!-- b000418 | prose | pages [28, 29] -->
 The reservoir levels  The strategy

<!-- b000419 | furniture | pages [29] -->
Team # 55069                                                            Page 27 of 28

<!-- b000421 | prose | pages [29] -->
 Normal flow year

<!-- b000422 | prose | pages [29, 30] -->
 Low flow year  High flow year

<!-- b000423 | furniture | pages [30] -->
Team # 55069                                                            Page 28 of 28

<!-- b000425 | prose | pages [30] -->
 Differentiation year
