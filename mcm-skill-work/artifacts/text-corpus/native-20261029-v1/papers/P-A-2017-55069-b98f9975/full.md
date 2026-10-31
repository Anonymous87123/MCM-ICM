# P-A-2017-55069-b98f9975

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | title | pages [1] -->
55069

<!-- b000006 | prose | pages [1] -->
T1 ________________

<!-- b000007 | prose | pages [1] -->
T2 ________________

<!-- b000008 | prose | pages [1] -->
F1 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | title | pages [1] -->
A

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | prose | pages [1] -->
F4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | heading | pages [1] -->
2017 MCM/ICM Summary Sheet

<!-- b000019 | prose | pages [1] -->
The Rehabilitation of the Kariba Dam

<!-- b000020 | prose | pages [1] -->
Recently, the Institute of Risk Management of South Africa has just warned that the Kariba dam is in desperate need of rehabilitation, otherwise the whole dam would collapse, putting 3.5 million people at risk. Aimed to look for the best strategy with the three options listed to maintain the dam, we employ AHP model to filter factors and determine two most influential criteria, including potential costs and benefits. With the weight of each criterion worked out, our model demonstrates that option 3 is the optimal choice.

<!-- b000021 | prose | pages [1] -->
According to our choice, we are required to offer the recommendation as to the number and placement of the new dams. Regarding it as a set covering problem, we develop a multi-objective optimization model to minimize the number of smaller dams while improving the water resources management capacity. Applying TOPSIS evaluation method to get the demand of the electricity and water, we solve this problem with genetic algorithm and get an approximate optimal solution with 12 smaller dams and determine the location of them.

<!-- b000022 | prose | pages [1] -->
Taking the strategy for modulating the water flow into account, we construct a joint operation of dam system to simulate the relationship among the smaller dams with genetic algorithm approach. We define four kinds of year based on the Kariba’s climate data of climate, namely, normal flow year, low flow year, high flow year and differential year. Finally, these statistics could help us simulate the water flow of each month in one year, then we obtain the water resources planning and modulating strategy.

<!-- b000023 | prose | pages [1] -->
The sensitivity analysis of our model has pointed out that small alteration in our constraints (including removing an important city of the countries and changing the measurement of the economic development index etc.) affects the location of some of our dams slightly while the number of dams remains the same. Also we find that the output coefficient is not an important factor for joint operation of the dam system, for the reason that the discharge index and the capacity index would not change a lot with the output coefficient changing.

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [2] -->
Team # 55069                                                            Page 2 of 2

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
1 Overview ................................................................................................................... 1

<!-- b000028 | contents | pages [2] -->
1.1 Background ................................................................................................. 1

<!-- b000029 | contents | pages [2] -->
1.2  Restatement of the Problem ..................................................................... 1

<!-- b000030 | contents | pages [2] -->
1.3  Literature Review ....................................................................................... 2

<!-- b000031 | contents | pages [2] -->
2 Assumptions and Justifications ........................................................................ 2

<!-- b000032 | contents | pages [2] -->
3 Notation .................................................................................................................... 3

<!-- b000033 | contents | pages [2] -->
4 Model Overview ...................................................................................................... 4

<!-- b000034 | contents | pages [2] -->
5 Model Theory........................................................................................................... 5

<!-- b000035 | contents | pages [2] -->
5.1 Determination of the Number and Location of the Dams .................... 5

<!-- b000036 | contents | pages [2] -->
5.2  Joint operation of dam system model ..................................................... 9

<!-- b000037 | contents | pages [2] -->
6 Model Implementation and Results ................................................................ 11

<!-- b000038 | contents | pages [2] -->
6.1 The Number and Location ...................................................................... 11

<!-- b000039 | contents | pages [2] -->
6.2 The Strategy of Modulating Water Flow ............................................... 14

<!-- b000040 | contents | pages [2] -->
7 Sensitivity Analysis ............................................................................................. 15

<!-- b000041 | contents | pages [2] -->
7.1  The Model of Determination of the Number and Location ................. 15

<!-- b000042 | contents | pages [2] -->
7.2  The Model of Modulating Water Flow ................................................... 17

<!-- b000043 | contents | pages [2] -->
8 Further discussion .............................................................................................. 17

<!-- b000044 | contents | pages [2] -->
9 Strengths and Weaknesses .............................................................................. 18

<!-- b000045 | contents | pages [2] -->
9.1  Strengths ................................................................................................... 18

<!-- b000046 | contents | pages [2] -->
9.2  Weaknesses .............................................................................................. 19

<!-- b000047 | contents | pages [2] -->
10 Conclusion .......................................................................................................... 19

<!-- b000048 | contents | pages [2] -->
11 The Evaluation of Three Options ................................................................... 20

<!-- b000049 | contents | pages [2] -->
11.1  Establish a Hierarchical Model ............................................................. 20

<!-- b000050 | contents | pages [2] -->
11.2  Analysis and Results ............................................................................. 21

<!-- b000051 | furniture | pages [2] -->


<!-- b000052 | furniture | pages [3] -->
Team # 55069                                                            Page 1 of 28

<!-- b000053 | contents | pages [3] -->
1

<!-- b000054 | contents | pages [3] -->
Overview

<!-- b000055 | heading | pages [3] -->
1.1  Background

<!-- b000056 | prose | pages [3] -->
A Zambezi River Authority conference was held in March 2014, engineers warned that the foundations of the dam had weakened and there was a possibility of dam failure unless repairs were made.

<!-- b000057 | prose | pages [3] -->
On 3 October 2014 the BBC reported that “The Kariba Dam is in a dangerous state. Opened in 1959, it was built on a seemingly solid bed of basalt. However, in the past 50 years, the torrents from the spillway have eroded that bedrock, carving a vast crater that has undercut the dam’s foundations, engineers are now warning that without urgent repairs, the whole dam will collapse. If that happened, a tsunami-like wall of water would rip through the Zambezi valley, reaching the Mozambique border within eight hours. The torrent would overwhelm Mozambique’s Cahora Bassa Dam and knock out 40% of southern Africa’s hydroelectric capacity. Along with the devastation of wildlife in the valley, the Zambezi River Authority estimates that the live of 3.5 million people are at risk.”

<!-- b000058 | prose | pages [3] -->
On February 2015, Engineers have started on a R3.3bn rescue marathon to prevent the “catastrophic failure” of the Kariba Dam. According to a World Bank special report on the beleaguered structure-one of the biggest man-made dams in the world-a potential wall collapse threatens the lives of about 3-million people living on the Zambezi River floodplain between the hydro scheme on the Zambia-Zimbabwe border and the Mozambique coast. [1]

<!-- b000059 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000060 | prose | pages [3] -->
We are required to provide an overview of potential costs and benefits with the three options already listed. Then we need to establish a model to determine the number and placement of the new dams when removing the Kariba dam along the Zambezi River. The same overall water management capabilities are also needed. In addition, we should consider emergency water flow situations and restrictions regarding the locations and time, so that we could give out the strategy for modulating the water flow through our new multiple dam system.

<!-- b000061 | prose | pages [3] -->
In order to solve those problems, we will proceed as follows:

<!-- b000062 | prose | pages [3] -->
 Build a model to determine the number and location of the multiple dams.

<!-- b000063 | prose | pages [3] -->
 Give the corresponding strategy of modulating water flow in different conditions.

<!-- b000064 | prose | pages [3] -->
In our model, we first establish a multi-objective model and use genetic algorithm determine the number and location of the multiple dams. There are two goals improving the water resources management capacity and reducing the cost. Besides, we add some constraints such as water balance, water level, safety and water protection. We choose twenty suitable dam sites and employ the genetic algorithm to solve the optimal problem to determine the number and the location.

<!-- b000065 | prose | pages [3] -->
After determining the number and location of the dams, we construct our joint operation of dam

<!-- b000066 | furniture | pages [3] -->


<!-- b000067 | furniture | pages [4] -->
Team # 55069                                                            Page 2 of 28

<!-- b000068 | prose | pages [4] -->
system model and employ the genetic algorithm to solve the problem based on the thought of dynamic programming. According to the Kariba’s climate data for about 30 years, we abstract normal flow year, low flow year, high flow year and differential year. We use them to work out the water resources planning and scheduling strategy. The construction of the discharge index and the capacity index benefits an analysis and evaluation for joint operation of the dam system’s performance in different month and year.

<!-- b000069 | heading | pages [4] -->
1.3  Literature Review

<!-- b000070 | prose | pages [4] -->
Dating back to 2004, the United States removed 72 dams in total, which created a historical record. Therefore, it is high time for us to focus on the construction of dams concerning their number and placement. Plenty of researchers have already made a number of notable papers to address these problems

<!-- b000071 | prose | pages [4] -->
Alfer Weber (1909) first proposed a framework for location problem, which is an allocation question with respect to space resource. Among the three classical location model, set covering problem is a significant branch of siting issues. They explored a multi-objective location model to tackle problems with siting optimal points. In their model, maximizing coverage rate in order to satisfy every place’s need is the target function, the concentric point and the capacity restrictions are constraint conditions. Thus, they could convert the optimization problem to the mixed integer linear programming question.

<!-- b000072 | prose | pages [4] -->
After the set covering model was established, we can optimize our choice of siting the dams. Then several scientists were devoted to building an optimal operation model to provide a reasonable balance between safety and balance. They begin to figure out how the multiple dam system would benefit or affect each other within its system. Masse(1940) first illustrated the concept of it; their main computing method was to optimize water modulating strategy during dispatching period.

<!-- b000073 | prose | pages [4] -->
Further studies are carried out about different methods to investigate the optimal operation model, including dynamic programming algorithm and neural network algorithm based on improved computer technique. Also, there is much theoretical analysis about location problem since 1990. John Current and Morton O'Kelly(1992) suggested using a modified version of the set covering location model, which still didn’t take the reality into account.

<!-- b000074 | prose | pages [4] -->
2

<!-- b000075 | heading | pages [4] -->
Assumptions and Justifications

<!-- b000076 | prose | pages [4] -->
To simplify our problems, we make the following basic assumptions, each of which is properly justified.

<!-- b000077 | prose | pages [4] -->
 The dam system is built downstream in the valley of the Kariba Dam. Because it’s more convenient to build and also with less cost, which can be easily implemented.

<!-- b000078 | prose | pages [4] -->
 The cost of the dam is mostly the same. Owing to the fact that the length of the canyon is not large（24km）,geological conditions and climate conditions are mostly the same.

<!-- b000079 | furniture | pages [4] -->


<!-- b000080 | furniture | pages [5] -->
Team # 55069                                                            Page 3 of 28

<!-- b000081 | prose | pages [5] -->
 Each dam’s water supply is mostly the same. Taking into account of safe operation of the entire multi-dam system, we should make the burden of each dam to be the same as much as possible.

<!-- b000082 | prose | pages [5] -->
 The water quality of the dam system is the average of the water quality between the two reservoirs. The river is flowing, so the water quality is mostly similar.

<!-- b000083 | prose | pages [5] -->
 Water of the dams downstream only comes from dams upstream and natural

<!-- b000084 | prose | pages [5] -->
precipitation. According to Google Maps, there are no tributaries near the canyon. Also with the principle of conservation of water, the formula should be maintained.

<!-- b000085 | prose | pages [5] -->
3

<!-- b000086 | heading | pages [5] -->
Notation

<!-- b000087 | prose | pages [5] -->
Abbreviation Description

<!-- b000088 | prose | pages [5] -->
   Y y y , , y The set of cities 1 2 m

<!-- b000089 | prose | pages [5] -->
  X = x x , , x

<!-- b000090 | furniture | pages [5] -->


<!-- b000091 | prose | pages [5] -->
The set of dams 1 2 n

<!-- b000092 | prose | pages [5] -->
thi city to the nearest smaller dam

<!-- b000093 | furniture | pages [5] -->


<!-- b000094 | prose | pages [5] -->
The distance from the d y X ( , ) i n

<!-- b000095 | prose | pages [5] -->
thi city Ele The electricity demand of i

<!-- b000096 | prose | pages [5] -->
thi city Wat The water demand of i

<!-- b000097 | prose | pages [5] -->
thi dam at the end of period t, W t i The discharge amount of the ( , )

<!-- b000098 | prose | pages [5] -->
Z t i ( , ) The total amount of water released during period t

<!-- b000099 | prose | pages [5] -->
T t i ( , ) The amount of natural water in period t

<!-- b000100 | prose | pages [5] -->
thj period of the thi dam V The volume in the ij

<!-- b000101 | prose | pages [5] -->
thj period of the thi dam Q The inflow in the ij

<!-- b000102 | furniture | pages [5] -->


<!-- b000103 | furniture | pages [6] -->
Team # 55069                                                            Page 4 of 28

<!-- b000104 | prose | pages [6] -->
thj period of the thi dam The discharge volume in the q ij

<!-- b000105 | prose | pages [6] -->
i  The runoff volume between the thi dam and the( QJ ij 1)th dam

<!-- b000106 | prose | pages [6] -->
thj period The actual water supply thi dam in the S ij

<!-- b000107 | prose | pages [6] -->
D thj period thi dam in the The planned water supply of the ij

<!-- b000108 | prose | pages [6] -->
thj period thi dam in the H The hydraulic head of ij

<!-- b000109 | prose | pages [6] -->
K thi dam The fore-voltage factor of the i

<!-- b000110 | prose | pages [6] -->
t The discharge flow indicators in the tht period

<!-- b000111 | prose | pages [6] -->
t The storage capacity indicators in the tht period

<!-- b000112 | prose | pages [6] -->
4

<!-- b000113 | heading | pages [6] -->
Model Overview

<!-- b000114 | prose | pages [6] -->
To provide a detailed analysis of the option (3)-removing the Kariba dam and newly building ten to twenty smaller dams. We need to determine the number and location of the multiple dams first. And on that basis we must establish a model to modulate the water flow through the multiple dam system to adapt to different situations. A reasonable balance between safety and cost of our strategy is also needed.

<!-- b000115 | prose | pages [6] -->
Our first model allows us to determine the number and the location of the multiple dams. We regard the optimal problem as a set covering problem and establish a multi-objective model to solve the problem. There are two goals, namely improving water resources management capacity and reducing the cost. And there are also some constraints including water balance, water level, safety, water resources protection and number constraints. On the account that the optimal problem is difficult to solve in polynomial time, so we use genetic algorithm to get the solution.

<!-- b000116 | prose | pages [6] -->
After determining the numbers and the location, we establish a joint operation of dam system model to gain a strategy about modulating water flow in different condition. Though it’s also a multi-objective problem, it is different from the previous model. We use the maximization of economic and social benefits as the objective and set some constraints, such as water balance, reservoir capacity and discharge flow constraints. We use genetic algorithm to get the

<!-- b000117 | furniture | pages [6] -->


<!-- b000118 | furniture | pages [7] -->
Team # 55069                                                            Page 5 of 28

<!-- b000119 | prose | pages [7] -->
modulating strategy in different conditions.

<!-- b000120 | prose | pages [7] -->
In conclusion, we use programming and heuristic algorithm to solve the problem of building dams and the modulating strategy. It’s relatively easy to achieve and it has a significant guidance for the reality.

<!-- b000121 | prose | pages [7] -->
5

<!-- b000122 | heading | pages [7] -->
Model Theory

<!-- b000123 | heading | pages [7] -->
5.1 Determination of the Number and Location of the Dams

<!-- b000124 | heading | pages [7] -->
5.1.1 Establishment of the model

<!-- b000125 | prose | pages [7] -->
The construction of dams needs to consider many aspects, while at the same time it is subject to economic, social, environmental constraints and other factors. In order to obtain the proper number of dams and their location, we establish a multi-objective model.

<!-- b000126 | prose | pages [7] -->
The Objective

<!-- b000127 | prose | pages [7] -->
 Improve Water Resources Management Capacity

<!-- b000128 | prose | pages [7] -->
The purpose of building smaller dams instead of larger dams is to manage water resources better, mainly to satisfy dweller’s demand for the electricity consumption and water consumption (Including agricultural, industrial and domestic water) of the neighboring cities. Demand may vary between cities, but it is clear that for cities with greater demand, the dam should be built closer to them. so we get that

<!-- b000129 | prose | pages [7] -->
m

<!-- b000130 | prose | pages [7] -->


<!-- b000131 | furniture | pages [7] -->


<!-- b000132 | prose | pages [7] -->
Ele d y X

<!-- b000133 | prose | pages [7] -->
min

<!-- b000134 | prose | pages [7] -->
i

<!-- b000135 | prose | pages [7] -->
1

<!-- b000136 | prose | pages [7] -->
m

<!-- b000137 | prose | pages [7] -->


<!-- b000138 | prose | pages [7] -->
( , )

<!-- b000139 | prose | pages [7] -->
i i i n

<!-- b000140 | furniture | pages [7] -->


<!-- b000141 | prose | pages [7] -->
Wat d y X

<!-- b000142 | prose | pages [7] -->
min

<!-- b000143 | prose | pages [7] -->
i

<!-- b000144 | prose | pages [7] -->
1

<!-- b000145 | prose | pages [7] -->
 Reduce the Cost

<!-- b000146 | prose | pages [7] -->
( , )

<!-- b000147 | prose | pages [7] -->
i i i n

<!-- b000148 | prose | pages [7] -->
On the basis of ensuring the water supply and power supply, we should minimize the cost of our plan. The whole cost consists of the removal of the Kariba dam and building new smaller dams. Since the cost of removal is fixed, so we only consider the variable cost(building cost), which is only related to the number of dams. So we should minimize the quantity of the smaller dams.

<!-- b000149 | prose | pages [7] -->
min n

<!-- b000150 | prose | pages [7] -->
The Constraints

<!-- b000151 | prose | pages [7] -->
 Water Balance

<!-- b000152 | prose | pages [7] -->
 

<!-- b000153 | prose | pages [7] -->
W t i

<!-- b000154 | prose | pages [7] -->
( , )

<!-- b000155 | prose | pages [7] -->
W t

<!-- b000156 | prose | pages [7] -->
( 1, )

<!-- b000157 | prose | pages [7] -->
i

<!-- b000158 | furniture | pages [7] -->


<!-- b000159 | prose | pages [7] -->


<!-- b000160 | furniture | pages [7] -->


<!-- b000161 | prose | pages [7] -->
  

<!-- b000162 | prose | pages [7] -->
Z t k

<!-- b000163 | prose | pages [7] -->
( , )

<!-- b000164 | prose | pages [7] -->
T t i

<!-- b000165 | prose | pages [7] -->
( , )

<!-- b000166 | prose | pages [7] -->
 

<!-- b000167 | prose | pages [7] -->
k k

<!-- b000168 | prose | pages [7] -->
( )

<!-- b000169 | prose | pages [7] -->
i

<!-- b000170 | furniture | pages [8] -->
Team # 55069                                                            Page 6 of 28

<!-- b000171 | prose | pages [8] -->
T t i represent the discharge amount of the Z t i and ( , ) ( , ) W t i ， ( , ) thi dam at the end of period

<!-- b000172 | prose | pages [8] -->
t, the total amount of water released during period t and the amount of natural water in period t

<!-- b000173 | prose | pages [8] -->
  thi dam. If denotes the set of all higher dams of respectively.

<!-- b000174 | prose | pages [8] -->
( )i

<!-- b000175 | prose | pages [8] -->
corresponding summation is zero.[2]

<!-- b000176 | prose | pages [8] -->
 Water Level

<!-- b000177 | prose | pages [8] -->
is empty, the ( )i

<!-- b000178 | prose | pages [8] -->
The water level in the dam area should be kept between the dead water level and the limited water level in the flood season. Dead Water Level, namely the lowest water level that allows a reservoir to fall off under normal operating conditions. Flood limited water level is the requirements of control over flood to limit reservoirs’ water storage.

<!-- b000179 | prose | pages [8] -->
 DWL

<!-- b000180 | prose | pages [8] -->
 Safety

<!-- b000181 | prose | pages [8] -->


<!-- b000182 | furniture | pages [8] -->


<!-- b000183 | prose | pages [8] -->
WL WL FWL

<!-- b000184 | prose | pages [8] -->
The construction of multiple smaller dams is at least as safe as the original larger dams. The safety considerations for dam construction mainly include reducing the probability of dam failure, thereby reducing damage to dams downstream and enhancing resistance ability to extreme weather.

<!-- b000185 | prose | pages [8] -->
Safety sd  

<!-- b000186 | furniture | pages [8] -->


<!-- b000187 | prose | pages [8] -->
Safety Bd

<!-- b000188 | prose | pages [8] -->
represents the safety of multiple dams system, while Safety sd

<!-- b000189 | prose | pages [8] -->
the existing Kariba dam.

<!-- b000190 | prose | pages [8] -->
 Water Resources Protection

<!-- b000191 | prose | pages [8] -->
denotes the safety of Safety Bd

<!-- b000192 | prose | pages [8] -->
The construction of smaller dams should require a higher degree of protection for the water resources as the replacement of the existing dam.

<!-- b000193 | prose | pages [8] -->
WRP sd  

<!-- b000194 | furniture | pages [8] -->


<!-- b000195 | prose | pages [8] -->
WRP Bd

<!-- b000196 | prose | pages [8] -->
WRP represents the environment protection of the multiple dams system, while sd WRP Bd

<!-- b000197 | prose | pages [8] -->
denotes the environment protection of the existing Kariba dam.

<!-- b000198 | prose | pages [8] -->
 Number

<!-- b000199 | prose | pages [8] -->
The number of small dams should be greater than ten and less than twenty. Option 3 is replacing the Kariba dam with a series of ten to twenty smaller dams.

<!-- b000200 | prose | pages [8] -->
To ensure the continuity of the model establishment, the parameters of the constraints will be described in the next part. And in the sixth section, we will clarify how to calculate the demand

<!-- b000201 | prose | pages [8] -->
of electricity( Ele ),the demand of the water( i

<!-- b000202 | furniture | pages [8] -->


<!-- b000203 | prose | pages [8] -->
Wat ),the safety of different dams and the i

<!-- b000204 | furniture | pages [9] -->
Team # 55069                                                            Page 7 of 28

<!-- b000205 | prose | pages [9] -->
environment protection of different dams.

<!-- b000206 | prose | pages [9] -->
To sum up, we model the problem about smaller dams’ number and location decision with multi-objective optimization. The formulas of this model is

<!-- b000207 | prose | pages [9] -->
m

<!-- b000208 | prose | pages [9] -->


<!-- b000209 | prose | pages [9] -->
min

<!-- b000210 | furniture | pages [9] -->


<!-- b000211 | prose | pages [9] -->
Ele d y X

<!-- b000212 | prose | pages [9] -->
i

<!-- b000213 | prose | pages [9] -->
1

<!-- b000214 | prose | pages [9] -->
m

<!-- b000215 | prose | pages [9] -->


<!-- b000216 | prose | pages [9] -->
min

<!-- b000217 | prose | pages [9] -->
( , )

<!-- b000218 | prose | pages [9] -->
i i i n

<!-- b000219 | furniture | pages [9] -->


<!-- b000220 | prose | pages [9] -->
Wat d y X

<!-- b000221 | prose | pages [9] -->
i

<!-- b000222 | prose | pages [9] -->
1

<!-- b000223 | prose | pages [9] -->
min n

<!-- b000224 | furniture | pages [9] -->


<!-- b000225 | prose | pages [9] -->
S t

<!-- b000226 | prose | pages [9] -->


<!-- b000227 | prose | pages [9] -->
. .

<!-- b000228 | prose | pages [9] -->
W t i

<!-- b000229 | prose | pages [9] -->
( , )

<!-- b000230 | prose | pages [9] -->
 DWL WL

<!-- b000231 | prose | pages [9] -->
 Safety sd

<!-- b000232 | prose | pages [9] -->
 WRP

<!-- b000233 | prose | pages [9] -->
( , )

<!-- b000234 | prose | pages [9] -->
i i i n

<!-- b000235 | furniture | pages [9] -->


<!-- b000236 | furniture | pages [9] -->


<!-- b000237 | prose | pages [9] -->


<!-- b000238 | furniture | pages [9] -->


<!-- b000239 | prose | pages [9] -->
  

<!-- b000240 | prose | pages [9] -->
W t

<!-- b000241 | prose | pages [9] -->
( ( 1, )

<!-- b000242 | prose | pages [9] -->
i Z t k

<!-- b000243 | prose | pages [9] -->
( , )

<!-- b000244 | prose | pages [9] -->
T t i

<!-- b000245 | prose | pages [9] -->
( , )

<!-- b000246 | prose | pages [9] -->
 

<!-- b000247 | prose | pages [9] -->
k

<!-- b000248 | prose | pages [9] -->
( )

<!-- b000249 | prose | pages [9] -->
i

<!-- b000250 | prose | pages [9] -->
 

<!-- b000251 | furniture | pages [9] -->


<!-- b000252 | prose | pages [9] -->
FWL

<!-- b000253 | furniture | pages [9] -->


<!-- b000254 | prose | pages [9] -->
Safety Bd

<!-- b000255 | furniture | pages [9] -->


<!-- b000256 | prose | pages [9] -->
WRP sd

<!-- b000257 | prose | pages [9] -->
  10 n 20

<!-- b000258 | prose | pages [9] -->
Bd

<!-- b000259 | prose | pages [9] -->
(n=10, 11, 12…..20)

<!-- b000260 | heading | pages [9] -->
5.1.2 The Parameter of the Constraints

<!-- b000261 | prose | pages [9] -->
 The Demand of Electricity

<!-- b000262 | prose | pages [9] -->
The power demand of a city is mainly related to its economic and demographic factors. Our paper uses the city's latest available GDP data as the representative of its economic factors, and the total urban population as the representative of its demographic factor.

<!-- b000263 | prose | pages [9] -->
pop . GDP .The population of the The GDP of the thi city is i

<!-- b000264 | prose | pages [9] -->
 The Demand of Water

<!-- b000265 | prose | pages [9] -->
thi city is i

<!-- b000266 | prose | pages [9] -->
The water consumption of residents is mainly affected by residents' income, water price and other factors. Since within a country, the price difference is relatively small, so here we ignore the price difference.. Therefore, the water consumption of urban residents is mainly affected by the income of residents, We use the city's GNI to represent its urban

<!-- b000267 | prose | pages [9] -->
GNI . thi city is residents. The GNI of the i

<!-- b000268 | prose | pages [9] -->
The Safety of Dams and the Kariba Dam[3] 

<!-- b000269 | prose | pages [9] -->
For the safety of dam construction, our paper mainly consider the index of risk loss as the agent of its safety indicators.

<!-- b000270 | prose | pages [9] -->
Bd equals to P multiply N . P is the R For a single Big dam, its Risk Loss Index(RLI) failure probability of the dam beyond the current code standard. For example, the current code specifies that if a dam's seismic safety standard is 50 years beyond 10%, the probability of

<!-- b000271 | furniture | pages [9] -->


<!-- b000272 | furniture | pages [10] -->
Team # 55069                                                            Page 8 of 28

<!-- b000273 | prose | pages [10] -->
failure exceeding the current code specification is 0.1 / 50 = 0.002.N is the life loss of dam failure (we can convert economic loss into life loss in a certain percentage). We use the Dekay & McClelland method to calculate the loss. Thus, the RLI of the Kariba dam is

<!-- b000274 | prose | pages [10] -->
 Bd R P K  . ( ) N K ( )

<!-- b000275 | prose | pages [10] -->
thj dam is For multiple dam system, the RLI of the

<!-- b000276 | prose | pages [10] -->
  

<!-- b000277 | prose | pages [10] -->
R P j

<!-- b000278 | prose | pages [10] -->
( )

<!-- b000279 | prose | pages [10] -->
N j

<!-- b000280 | prose | pages [10] -->
( )

<!-- b000281 | prose | pages [10] -->
j

<!-- b000282 | prose | pages [10] -->
l

<!-- b000283 | prose | pages [10] -->
and the RLI of the multiple dam system is

<!-- b000284 | prose | pages [10] -->
n n

<!-- b000285 | prose | pages [10] -->
   

<!-- b000286 | prose | pages [10] -->
P l j

<!-- b000287 | prose | pages [10] -->
( | )

<!-- b000288 | prose | pages [10] -->
P j

<!-- b000289 | prose | pages [10] -->
( )

<!-- b000290 | prose | pages [10] -->
N l

<!-- b000291 | prose | pages [10] -->
( )

<!-- b000292 | furniture | pages [10] -->


<!-- b000293 | prose | pages [10] -->
 

<!-- b000294 | prose | pages [10] -->
j j

<!-- b000295 | prose | pages [10] -->
1 1

<!-- b000296 | prose | pages [10] -->
n n

<!-- b000297 | prose | pages [10] -->


<!-- b000298 | prose | pages [10] -->
sd R sd

<!-- b000299 | furniture | pages [10] -->


<!-- b000300 | prose | pages [10] -->
R j

<!-- b000301 | prose | pages [10] -->
 

<!-- b000302 | prose | pages [10] -->
j j

<!-- b000303 | prose | pages [10] -->
1

<!-- b000304 | prose | pages [10] -->
The safety of the multiple dam system should be greater than or at least equal to the safety of

<!-- b000305 | prose | pages [10] -->
 sd R the existing Kariba dam. So we get that

<!-- b000306 | prose | pages [10] -->
n

<!-- b000307 | prose | pages [10] -->


<!-- b000308 | prose | pages [10] -->
Bd

<!-- b000309 | prose | pages [10] -->
 

<!-- b000310 | prose | pages [10] -->
sd

<!-- b000311 | prose | pages [10] -->
R R , that is to say

<!-- b000312 | prose | pages [10] -->
.And n

<!-- b000313 | prose | pages [10] -->
R P K

<!-- b000314 | prose | pages [10] -->
( )

<!-- b000315 | prose | pages [10] -->
N K

<!-- b000316 | prose | pages [10] -->
( )

<!-- b000317 | prose | pages [10] -->
i

<!-- b000318 | prose | pages [10] -->


<!-- b000319 | prose | pages [10] -->
i

<!-- b000320 | prose | pages [10] -->
1

<!-- b000321 | prose | pages [10] -->
is an integer greater than ten and less than twenty

<!-- b000322 | prose | pages [10] -->
 The water resources protection of dams

<!-- b000323 | prose | pages [10] -->
According to the International Commission On Large Dams(ICOLD), there are three goals of water resources management[4]

<!-- b000324 | prose | pages [10] -->
 Improved management of the water supply

<!-- b000325 | prose | pages [10] -->
 Improved water quality in our rivers

<!-- b000326 | prose | pages [10] -->
 Improved environmental conditions in the watershed

<!-- b000327 | prose | pages [10] -->
Since there are few branches in the Kariba Gorge, we mainly consider the management of the water supply and the water quality.

<!-- b000328 | prose | pages [10] -->
According to the constraints, the water supply of the multiple-dam system should be greater than the big dam. That is to say

<!-- b000329 | prose | pages [10] -->
WS sd  

<!-- b000330 | furniture | pages [10] -->


<!-- b000331 | prose | pages [10] -->
WS Bd

<!-- b000332 | prose | pages [10] -->
WS equals to the number of the smaller dams multiply the water supply of a smaller dam, sd

<!-- b000333 | prose | pages [10] -->
represents the water supply of the Kariba Dam. while WS Bd

<!-- b000334 | furniture | pages [10] -->


<!-- b000335 | furniture | pages [11] -->
Team # 55069                                                            Page 9 of 28

<!-- b000336 | prose | pages [11] -->
Besides, the water quality of the multiple-dam system should be greater than the Kariba dam.

<!-- b000337 | prose | pages [11] -->
WQ sd   , WQ Bd

<!-- b000338 | prose | pages [11] -->
WQ represents the expected average water quality of the Lake Kariba if the authority adopt sd

<!-- b000339 | prose | pages [11] -->
represents the present water quality of the Lake Kariba. the option three, while WQ Bd

<!-- b000340 | heading | pages [11] -->
5.2 Joint Operation of Dam System Model

<!-- b000341 | prose | pages [11] -->
Joint operation of dam system can utilize the differences between dam capacity and hydrologic condition, so that we develop a joint compensation effect for the dam group and make full use of water resources. Compared with the traditional single large dam, the dam group establish on the basis of multi –dam system, which could help us take advantage of water resources for our social benefits, including economic and social benefits. Therefore, it is necessary to establish an effective water resources dispatching scheme.

<!-- b000342 | prose | pages [11] -->
In order to better express our model，we let    j 1...

<!-- b000343 | prose | pages [11] -->
T i i 1...

<!-- b000344 | prose | pages [11] -->
n indicates the number of dams，

<!-- b000345 | prose | pages [11] -->
V illustrates the thi dam’s water storage during the denotes the cycle of water dispatching， ij

<!-- b000346 | prose | pages [11] -->
thj period.[5]

<!-- b000347 | prose | pages [11] -->
The Objective

<!-- b000348 | prose | pages [11] -->
The hydropower station mainly bring about economic and social benefits. But obviously, hydropower station can bring magnificent economic benefits. Among them, the most direct indication is the dam power generation. Therefore, taking the reservoir power generation as the revelation of economic benefit.

<!-- b000349 | prose | pages [11] -->
n T

<!-- b000350 | prose | pages [11] -->


<!-- b000351 | prose | pages [11] -->
I K 

<!-- b000352 | prose | pages [11] -->
e

<!-- b000353 | prose | pages [11] -->
 

<!-- b000354 | prose | pages [11] -->
i

<!-- b000355 | prose | pages [11] -->
1

<!-- b000356 | prose | pages [11] -->
j

<!-- b000357 | prose | pages [11] -->
1

<!-- b000358 | prose | pages [11] -->
q is the discharge flow of the thi dam in the ij

<!-- b000359 | prose | pages [11] -->


<!-- b000360 | furniture | pages [11] -->


<!-- b000361 | prose | pages [11] -->
* *

<!-- b000362 | prose | pages [11] -->
q

<!-- b000363 | prose | pages [11] -->
*

<!-- b000364 | prose | pages [11] -->
H

<!-- b000365 | prose | pages [11] -->
*

<!-- b000366 | prose | pages [11] -->
t

<!-- b000367 | prose | pages [11] -->
i i ij ij

<!-- b000368 | prose | pages [11] -->
H is the hydraulic head of thj period， thi dam ij

<!-- b000369 | prose | pages [11] -->
is the time period. K is the force-voltage factor of the thj period， in the i thi dam，t

<!-- b000370 | prose | pages [11] -->
In addition to creating enormous economic benefits, a large dam can also bring huge social benefits. Through the construction of dams, it can meet the need of a large number of industrial and agricultural water, also the domestic water.

<!-- b000371 | furniture | pages [11] -->


<!-- b000372 | furniture | pages [12] -->
Team # 55069                                                            Page 10 of 28

<!-- b000373 | prose | pages [12] -->
n T

<!-- b000374 | prose | pages [12] -->


<!-- b000375 | prose | pages [12] -->
I 

<!-- b000376 | prose | pages [12] -->
s

<!-- b000377 | prose | pages [12] -->
 

<!-- b000378 | prose | pages [12] -->
i

<!-- b000379 | prose | pages [12] -->
1

<!-- b000380 | prose | pages [12] -->
i

<!-- b000381 | prose | pages [12] -->
S is the actual water supply thi dam in the ij

<!-- b000382 | prose | pages [12] -->
thi dam in the tht stage. supply of the

<!-- b000383 | prose | pages [12] -->


<!-- b000384 | furniture | pages [12] -->


<!-- b000385 | prose | pages [12] -->
( (

<!-- b000386 | prose | pages [12] -->
S D

<!-- b000387 | prose | pages [12] -->
)

<!-- b000388 | prose | pages [12] -->
ij ij

<!-- b000389 | prose | pages [12] -->
1 1

<!-- b000390 | prose | pages [12] -->
tht stage， D is water demand or planned water ij

<!-- b000391 | prose | pages [12] -->
Therefore, we should make full use of water resources so as to make the economic and social benefits as large as possible.[6]

<!-- b000392 | prose | pages [12] -->
 I max(

<!-- b000393 | prose | pages [12] -->
The Constraints

<!-- b000394 | prose | pages [12] -->
 Water Balance

<!-- b000395 | prose | pages [12] -->
  V V ( Q i t ,( 1) it

<!-- b000396 | prose | pages [12] -->
 Q  i t ,( 1)

<!-- b000397 | prose | pages [12] -->


<!-- b000398 | furniture | pages [12] -->


<!-- b000399 | prose | pages [12] -->
I I ) e s

<!-- b000400 | prose | pages [12] -->
 

<!-- b000401 | furniture | pages [12] -->


<!-- b000402 | prose | pages [12] -->
q ) t L it it it it

<!-- b000403 | prose | pages [12] -->


<!-- b000404 | furniture | pages [12] -->


<!-- b000405 | prose | pages [12] -->
q q QJ   ( ( i i 1), t it

<!-- b000406 | prose | pages [12] -->
tht period of the thi ijq are the average inflow into the dam and discharge volume in the Q 、 it

<!-- b000407 | prose | pages [12] -->
itL is the evaporation and leakage loss. dam,

<!-- b000408 | prose | pages [12] -->
thj dam. and the

<!-- b000409 | prose | pages [12] -->
 Capacity of the Dam

<!-- b000410 | prose | pages [12] -->
thi dam QJ is the runoff volume between the it

<!-- b000411 | prose | pages [12] -->
To prevent floods and droughts，The capacity of each dam must be limited.

<!-- b000412 | prose | pages [12] -->
 V min i 

<!-- b000413 | furniture | pages [12] -->


<!-- b000414 | prose | pages [12] -->
V V V max it it i

<!-- b000415 | prose | pages [12] -->
are the upper and lower limit of the thi dam’s water storage，namely the V min i V max i 、

<!-- b000416 | prose | pages [12] -->
dead capacity and the flood control capacity.

<!-- b000417 | prose | pages [12] -->
 Discharge Flow Constraint

<!-- b000418 | prose | pages [12] -->
In order to keep the normal life standard and to maintain the downstream ecological water use,

<!-- b000419 | prose | pages [12] -->
q min i we must ensure the certain discharge of water, we employ to indicate the minimal

<!-- b000420 | prose | pages [12] -->
discharge of water. Because of the limitation of the dam itself and the purpose of flood control, q max i there need to be a maximal discharge capacity constraint

<!-- b000421 | prose | pages [12] -->
 q m in i

<!-- b000422 | furniture | pages [12] -->


<!-- b000423 | furniture | pages [12] -->


<!-- b000424 | prose | pages [12] -->
 q q q max

<!-- b000425 | furniture | pages [12] -->


<!-- b000426 | prose | pages [12] -->
it it i

<!-- b000427 | furniture | pages [13] -->
Team # 55069                                                            Page 11 of 28

<!-- b000428 | prose | pages [13] -->
In conclusion, in order to make economic benefit and social benefit as large as possible while satisfying the constraint conditions, we need to develop water resources optimized dispatching scheme.

<!-- b000429 | prose | pages [13] -->
n T

<!-- b000430 | prose | pages [13] -->
 

<!-- b000431 | prose | pages [13] -->
max

<!-- b000432 | prose | pages [13] -->
I K

<!-- b000433 | prose | pages [13] -->
*

<!-- b000434 | prose | pages [13] -->
q

<!-- b000435 | prose | pages [13] -->
*

<!-- b000436 | prose | pages [13] -->
i ij

<!-- b000437 | prose | pages [13] -->
 

<!-- b000438 | prose | pages [13] -->
i

<!-- b000439 | prose | pages [13] -->
1

<!-- b000440 | prose | pages [13] -->
j

<!-- b000441 | prose | pages [13] -->
1

<!-- b000442 | prose | pages [13] -->
  

<!-- b000443 | prose | pages [13] -->
V V

<!-- b000444 | prose | pages [13] -->


<!-- b000445 | prose | pages [13] -->
i

<!-- b000446 | prose | pages [13] -->
, (

<!-- b000447 | prose | pages [13] -->
t

<!-- b000448 | prose | pages [13] -->
1)

<!-- b000449 | prose | pages [13] -->
it

<!-- b000450 | prose | pages [13] -->


<!-- b000451 | prose | pages [13] -->
Q

<!-- b000452 | prose | pages [13] -->
 

<!-- b000453 | prose | pages [13] -->
i

<!-- b000454 | prose | pages [13] -->
, (

<!-- b000455 | prose | pages [13] -->
t

<!-- b000456 | prose | pages [13] -->
1)

<!-- b000457 | prose | pages [13] -->
s t

<!-- b000458 | prose | pages [13] -->
. .

<!-- b000459 | prose | pages [13] -->
V

<!-- b000460 | prose | pages [13] -->
min

<!-- b000461 | prose | pages [13] -->


<!-- b000462 | prose | pages [13] -->
i

<!-- b000463 | prose | pages [13] -->


<!-- b000464 | prose | pages [13] -->
q

<!-- b000465 | prose | pages [13] -->
m

<!-- b000466 | prose | pages [13] -->
in

<!-- b000467 | prose | pages [13] -->


<!-- b000468 | prose | pages [13] -->
i

<!-- b000469 | prose | pages [13] -->
V 、itq are the interval-type variable，min i V it

<!-- b000470 | prose | pages [13] -->
n T

<!-- b000471 | prose | pages [13] -->
  

<!-- b000472 | furniture | pages [13] -->


<!-- b000473 | prose | pages [13] -->
H H

<!-- b000474 | prose | pages [13] -->
*

<!-- b000475 | prose | pages [13] -->
t

<!-- b000476 | prose | pages [13] -->
(

<!-- b000477 | prose | pages [13] -->
S D

<!-- b000478 | prose | pages [13] -->
)

<!-- b000479 | prose | pages [13] -->
ij ij ij ij

<!-- b000480 | prose | pages [13] -->
 

<!-- b000481 | prose | pages [13] -->
i

<!-- b000482 | prose | pages [13] -->
1

<!-- b000483 | prose | pages [13] -->
i

<!-- b000484 | prose | pages [13] -->
1

<!-- b000485 | prose | pages [13] -->
 

<!-- b000486 | prose | pages [13] -->
( (

<!-- b000487 | prose | pages [13] -->
Q q

<!-- b000488 | prose | pages [13] -->
)*

<!-- b000489 | prose | pages [13] -->
t L

<!-- b000490 | prose | pages [13] -->
it it it

<!-- b000491 | prose | pages [13] -->
  

<!-- b000492 | prose | pages [13] -->
q q QJ

<!-- b000493 | prose | pages [13] -->


<!-- b000494 | prose | pages [13] -->
(

<!-- b000495 | prose | pages [13] -->
i

<!-- b000496 | prose | pages [13] -->
1),

<!-- b000497 | prose | pages [13] -->
t it

<!-- b000498 | furniture | pages [13] -->


<!-- b000499 | prose | pages [13] -->
  

<!-- b000500 | prose | pages [13] -->
V V

<!-- b000501 | prose | pages [13] -->
max

<!-- b000502 | prose | pages [13] -->
it i

<!-- b000503 | prose | pages [13] -->
  

<!-- b000504 | prose | pages [13] -->
q q

<!-- b000505 | prose | pages [13] -->
max

<!-- b000506 | prose | pages [13] -->
it i

<!-- b000507 | prose | pages [13] -->
、min i q correspond to meet the basic industrial

<!-- b000508 | prose | pages [13] -->
and agricultural water、domestic water and ecological water，they are the dead water level.

<!-- b000509 | prose | pages [13] -->
For safety considerations such as flood control，max i V 、max i q are the maximal water level.

<!-- b000510 | prose | pages [13] -->
itq .[7] qf qF is the optimum interval of We let [ Vf VF to be the of V ,[ , , ] ] i i i i it

<!-- b000511 | prose | pages [13] -->
  

<!-- b000512 | prose | pages [13] -->
1 (

<!-- b000513 | prose | pages [13] -->
Vf V

<!-- b000514 | prose | pages [13] -->
) / (

<!-- b000515 | prose | pages [13] -->
Vf

<!-- b000516 | prose | pages [13] -->
i it i

<!-- b000517 | prose | pages [13] -->


<!-- b000518 | prose | pages [13] -->
1,

<!-- b000519 | prose | pages [13] -->
Vf

<!-- b000520 | prose | pages [13] -->


<!-- b000521 | prose | pages [13] -->


<!-- b000522 | prose | pages [13] -->


<!-- b000523 | prose | pages [13] -->
it

<!-- b000524 | prose | pages [13] -->


<!-- b000525 | prose | pages [13] -->
1 (

<!-- b000526 | prose | pages [13] -->
V VF

<!-- b000527 | prose | pages [13] -->
) / ( max

<!-- b000528 | prose | pages [13] -->
V

<!-- b000529 | prose | pages [13] -->


<!-- b000530 | prose | pages [13] -->
it i

<!-- b000531 | prose | pages [13] -->


<!-- b000532 | prose | pages [13] -->


<!-- b000533 | prose | pages [13] -->


<!-- b000534 | prose | pages [13] -->
t

<!-- b000535 | prose | pages [13] -->
  

<!-- b000536 | prose | pages [13] -->
1 (

<!-- b000537 | prose | pages [13] -->
qf q

<!-- b000538 | prose | pages [13] -->
) / (

<!-- b000539 | prose | pages [13] -->
qf

<!-- b000540 | prose | pages [13] -->
i it i

<!-- b000541 | prose | pages [13] -->


<!-- b000542 | prose | pages [13] -->
1,

<!-- b000543 | prose | pages [13] -->
qf

<!-- b000544 | prose | pages [13] -->


<!-- b000545 | prose | pages [13] -->


<!-- b000546 | prose | pages [13] -->


<!-- b000547 | prose | pages [13] -->
it

<!-- b000548 | prose | pages [13] -->


<!-- b000549 | prose | pages [13] -->
1 (

<!-- b000550 | prose | pages [13] -->
q qF

<!-- b000551 | prose | pages [13] -->
) / ( max

<!-- b000552 | prose | pages [13] -->
q

<!-- b000553 | prose | pages [13] -->


<!-- b000554 | prose | pages [13] -->
it i

<!-- b000555 | prose | pages [13] -->


<!-- b000556 | prose | pages [13] -->


<!-- b000557 | prose | pages [13] -->


<!-- b000558 | prose | pages [13] -->
t

<!-- b000559 | prose | pages [13] -->
   

<!-- b000560 | prose | pages [13] -->
V V

<!-- b000561 | prose | pages [13] -->
min ),

<!-- b000562 | prose | pages [13] -->
V

<!-- b000563 | prose | pages [13] -->
min

<!-- b000564 | prose | pages [13] -->
V Vf

<!-- b000565 | prose | pages [13] -->
i i it i

<!-- b000566 | prose | pages [13] -->
 

<!-- b000567 | prose | pages [13] -->
V VF

<!-- b000568 | prose | pages [13] -->
i i it i

<!-- b000569 | furniture | pages [13] -->


<!-- b000570 | prose | pages [13] -->
  

<!-- b000571 | prose | pages [13] -->
VF VF

<!-- b000572 | prose | pages [13] -->
),

<!-- b000573 | prose | pages [13] -->
V V

<!-- b000574 | prose | pages [13] -->
max

<!-- b000575 | prose | pages [13] -->
i i i i it i

<!-- b000576 | prose | pages [13] -->
0,

<!-- b000577 | prose | pages [13] -->
else

<!-- b000578 | prose | pages [13] -->
N 1 1

<!-- b000579 | prose | pages [13] -->


<!-- b000580 | prose | pages [13] -->


<!-- b000581 | furniture | pages [13] -->


<!-- b000582 | prose | pages [13] -->
it

<!-- b000583 | prose | pages [13] -->
N N

<!-- b000584 | prose | pages [13] -->


<!-- b000585 | prose | pages [13] -->
i i

<!-- b000586 | prose | pages [13] -->
1

<!-- b000587 | prose | pages [13] -->
   

<!-- b000588 | prose | pages [13] -->
q

<!-- b000589 | prose | pages [13] -->
min ), min

<!-- b000590 | prose | pages [13] -->
q q qf

<!-- b000591 | prose | pages [13] -->
i i it i

<!-- b000592 | prose | pages [13] -->
 

<!-- b000593 | prose | pages [13] -->
q qF

<!-- b000594 | prose | pages [13] -->
i i it i

<!-- b000595 | furniture | pages [13] -->


<!-- b000596 | prose | pages [13] -->
  

<!-- b000597 | prose | pages [13] -->
qF

<!-- b000598 | prose | pages [13] -->
),

<!-- b000599 | prose | pages [13] -->
qF q q

<!-- b000600 | prose | pages [13] -->
max

<!-- b000601 | prose | pages [13] -->
i i i i it i

<!-- b000602 | prose | pages [13] -->
0,

<!-- b000603 | prose | pages [13] -->
else

<!-- b000604 | prose | pages [13] -->
N 1 1

<!-- b000605 | prose | pages [13] -->


<!-- b000606 | prose | pages [13] -->


<!-- b000607 | furniture | pages [13] -->


<!-- b000608 | prose | pages [13] -->
it

<!-- b000609 | prose | pages [13] -->
N N

<!-- b000610 | prose | pages [13] -->


<!-- b000611 | prose | pages [13] -->
i i

<!-- b000612 | prose | pages [13] -->
1

<!-- b000613 | heading | pages [13] -->
Model Implementation and Results

<!-- b000614 | prose | pages [13] -->
6

<!-- b000615 | heading | pages [13] -->
6.1 The Number and Location

<!-- b000616 | prose | pages [13] -->
 Measuring the demand of the nearby city

<!-- b000617 | furniture | pages [13] -->


<!-- b000618 | furniture | pages [14] -->
Team # 55069                                                            Page 12 of 28

<!-- b000619 | prose | pages [14] -->
TOPSIS (Technique for Order Preference by Similarity to an Ideal Solution) is a commonly used and effective method in multi-objective decision analysis. Hence ,we employ this model and then investigate extended TOPSIS to evaluate the demand of  electricity and water of each city.

<!-- b000620 | prose | pages [14] -->
Then we use the data to calculate the demand of the electricity and water with TOPSIS, and part of the results is shown in Table 1.

<!-- b000621 | caption | pages [14] -->
Table 1 The Demand of Electricity and Water

<!-- b000622 | furniture | pages [14] -->


<!-- b000623 | prose | pages [14] -->
 Calculate the shortest distance from each dam to each city

<!-- b000624 | prose | pages [14] -->
The dam should be built in the valley of the river fully, because the project is small with low cost. Moreover, the construction of small dams is mainly to replace the larger dam, so the small dam should be constructed mainly in the downstream of the Kariba dam in the canyon. Figure 1 is the suitable site for building dams.

<!-- b000625 | furniture | pages [14] -->


<!-- b000626 | caption | pages [14] -->
Figure 1 The Suitable Gorge for Building Dams

<!-- b000627 | prose | pages [14] -->
With respect to the option 3 that we need to construct 10 to 20 small dams, considering the geological factors around the dam, we first select the suitable location of the 20 dams.

<!-- b000628 | furniture | pages [14] -->


<!-- b000629 | furniture | pages [15] -->
Team # 55069                                                            Page 13 of 28

<!-- b000630 | prose | pages [15] -->
According to our model, we use the distance from the dam to the center of the city as a representative of the distance to the city. A total of 25 cities are selected close to the Kariba gorge, including 15 cities in Zambia, 10 cities in Zimbabwe. We search and calculate the shortest distance and path of each dam to the city through Google maps, and the results of some small dams to the cities are shown in Table 2.

<!-- b000631 | caption | pages [15] -->
Table 2 The Distance Between the Dams and the City(Part)

<!-- b000632 | prose | pages [15] -->
 The Data of Other Factors

<!-- b000633 | furniture | pages [15] -->


<!-- b000634 | prose | pages [15] -->
At the same time, we collect the data of other related factors through the Zambia National Bureau of Statistics, the World Bank, the World Commission on Dams and other institutions to gain the relevant statistics.

<!-- b000635 | caption | pages [15] -->
Table 3 The Data of Other Factors

<!-- b000636 | furniture | pages [15] -->


<!-- b000637 | prose | pages [15] -->
DWL NWL FWL

<!-- b000638 | prose | pages [15] -->
Kariba 475.5 484.6 490

<!-- b000639 | prose | pages [15] -->
Multiple 382 408 412

<!-- b000640 | prose | pages [15] -->
BFWL RLI WS WQ

<!-- b000641 | prose | pages [15] -->
476.7 9000 608.5 19

<!-- b000642 | prose | pages [15] -->


<!-- b000643 | prose | pages [15] -->
385

<!-- b000644 | prose | pages [15] -->
e

<!-- b000645 | prose | pages [15] -->
n

<!-- b000646 | prose | pages [15] -->
WS n

<!-- b000647 | prose | pages [15] -->


<!-- b000648 | prose | pages [15] -->
sd

<!-- b000649 | furniture | pages [15] -->


<!-- b000650 | prose | pages [15] -->
WQ e

<!-- b000651 | prose | pages [15] -->
R

<!-- b000652 | prose | pages [15] -->
i i

<!-- b000653 | prose | pages [15] -->
1

<!-- b000654 | prose | pages [15] -->
Under normal circumstances the water level should be higher than the dead water level, and lower than the normal position. But before the flood season, the water level is lower than the limit of water level.

<!-- b000655 | prose | pages [15] -->
 The numbers and the location

<!-- b000656 | prose | pages [15] -->
This optimal problem belongs to the NP-hard problem. We can’t solve it in polynomial time. So we can only use heuristic algorithms such as artificial neural networks, genetic algorithm, simulated annealing to obtain the approximate solution. In this paper, we select the genetic algorithm to solve the problem.

<!-- b000657 | prose | pages [15] -->
We run the program repeatedly, and finally get a relatively good result and determine our number and location of the dams. There should be 12 smaller dams in the Kariba Gorge. Besides, we select the optimal 12 dam location to maximize our objective function from 20 appropriate

<!-- b000658 | furniture | pages [15] -->


<!-- b000659 | furniture | pages [16] -->
Team # 55069                                                            Page 14 of 28

<!-- b000660 | prose | pages [16] -->
dam sites. The sixth and twelfth site locations are listed in the Table 4

<!-- b000661 | caption | pages [16] -->
Table 4 The Location of the Dam

<!-- b000662 | prose | pages [16] -->
At the same time, we will also mark the location of the small dam on the map, we put the location of the sixth and twelfth dam on the map. We can see it on the Figure 2 and Figure 3

<!-- b000663 | furniture | pages [16] -->


<!-- b000664 | furniture | pages [16] -->


<!-- b000665 | caption | pages [16] -->
Figure 2 The Location of the 6th Dam           Figure 3 The Location of the 12th Dam

<!-- b000666 | heading | pages [16] -->
6.2 The Strategy of Modulating Water Flow

<!-- b000667 | prose | pages [16] -->
Traditional optimization algorithm mostly belongs to the convex optimization category. It demands a unique global optimal solution, which is often used in practical applications. A number of heuristic intelligent algorithm, for example genetic algorithm etc.These methods show that the algorithm can work out satisfactory results for solving the optimization problem. Employing joint operation of dam system model, we use genetic algorithm and Matlab2014 for the solution.[8]

<!-- b000668 | prose | pages [16] -->
By running the genetic algorithm and adjusting the parameters, we obtain a relatively satisfactory result, and then develop a joint operation of dam system model.(The picture of the results is shown in the appendix part four.)

<!-- b000669 | prose | pages [16] -->
 Normal Flow Year：Take the climate and hydrological conditions of the average of nearly 5 years to simulate normal climatic conditions.

<!-- b000670 | prose | pages [16] -->
In normal years, the water resources dispatching of the dam system shows obvious seasonal difference. In the dry season from June to September, the discharge of each reservoir reaches the bottom line. Compared with the middle and lower reaches of the river, upper and middle

<!-- b000671 | furniture | pages [16] -->


<!-- b000672 | furniture | pages [17] -->
Team # 55069                                                            Page 15 of 28

<!-- b000673 | prose | pages [17] -->
reaches of water resources and reserves are relatively abundant, therefore, still a lot of water could be scheduled downstream. But until the rainy season from November to March, the precipitation intensity and the discharge of each dam are very large. The results show that the discharge index and storage capacity index perform better in May and October, which are in the optimum range, while the other month are all above 0.7, this is a satisfactory result.

<!-- b000674 | prose | pages [17] -->
 Low Flow Year: The monthly precipitation is taken as the highest value in the past 30 years, simulating the more serious flood threat..

<!-- b000675 | prose | pages [17] -->
When the annual precipitation decreases, each dam discharge is significantly lower, but the discharge index and the capacity index is still above 0.7, which reflects the joint operation of dam system still has obvious effect to resist abnormal weather like the drought condition.

<!-- b000676 | prose | pages [17] -->
 High Flow Year：The monthly precipitation is taken as the highest value inthe past 30 years, simulating the more serious flood threat.

<!-- b000677 | prose | pages [17] -->
When the annual precipitation has increased significantly, then the reservoir’s discharge would increase.  While the discharge of the rainy season increases a lot, but in dry season the increase range is smaller, which makes the discharge capacity index and volume index increase significantly from May to September. Although the index decreases significantly in November and February the figure are more than 0.7, is still relatively satisfactory.

<!-- b000678 | prose | pages [17] -->
 Differentiation Year：The precipitation from May to September is taken as the lowest value in the past 30 years, the precipitation from October to April was taken as the highest value in the past 30 years. So that we could simulate drought, flood significantly differentiated condition..

<!-- b000679 | prose | pages [17] -->
When confronted with the differentiation year where there comes rainy season when the precipitation increases and the dry season when the precipitation decreases all come about in one year. The discharge flow of each reservoir expands seasonally, which makes the discharge index and storage capacity index of each month decrease, and it is more obvious in the rainy season. Which can not be ignored is that the discharge flow indicators and storage capacity indicators remained at 0.7 or more.[9]

<!-- b000680 | heading | pages [17] -->
7. Sensitivity Analysis

<!-- b000681 | heading | pages [17] -->
7.1 The Model of Determination of the Number and Location

<!-- b000682 | prose | pages [17] -->
 Remove an important city of both countries

<!-- b000683 | prose | pages [17] -->
In the questions we discussed above，we have selected 15 cities in Zambia，10 cities in Zimbabwe to specify the number and placement of the newly built smaller dams. Among the sensitivity analysis, we remove important cities of the two countries, thus, we could see whether this movement would influence the number and placement of constructing dams.

<!-- b000684 | prose | pages [17] -->
In our analysis, we leave out Lusaka (The capital city of Zambia) and Harare(The capital city of Zimbabwe) from our original cities, yet, we still use the multi objective optimization model and genetic algorithm we already established to calculate the number and placement of smaller dams. We discover that the optimal number of constructing dams is also 12, but the location of each dam is slightly changed. Just the fourth and the eleventh dam’s place changes a lot, while other dam’s place just changes a little. Therefore, we list the location of the fourth and the eleventh dam’s site in Table 5.

<!-- b000685 | furniture | pages [17] -->


<!-- b000686 | furniture | pages [18] -->
Team # 55069                                                            Page 16 of 28

<!-- b000687 | prose | pages [18] -->
To sum up, the influence of removing bigger cities is not that much. Still in accordance with our former model, we could also draw the conclusion that large cities exert magnificent impact on the selection of the dam’s location. Hence, putting larger cities into our model while constructing dams is an appropriate choice.

<!-- b000688 | caption | pages [18] -->
Table 5 The Location of 4th Dam and 11th Dam

<!-- b000689 | prose | pages [18] -->
 Change the measurement of the economic development index

<!-- b000690 | prose | pages [18] -->
In the model we have discussed before, we mainly employ the current GDP of each city as a measure of the economic development, which is also used as one of the indicators to measure the water and electricity demand. Here, we will use its GDP growth rate as an agent indicator for the city's economic development, and change its GDP growth rate to observe whether it has the impact on the number and location of the construction of dams.

<!-- b000691 | prose | pages [18] -->
Our paper first use economic growth data of the city to measure its water and electricity demand, and then float up and down of the basis, the maximum change is up to 8%. The impact of economic growth on the number of dams is shown in Table 6.

<!-- b000692 | caption | pages [18] -->
Table 6 The Sensitivity of the GDP growth rate

<!-- b000693 | furniture | pages [18] -->


<!-- b000694 | prose | pages [18] -->
From the table above we can see that the changing of the economic growth rate for the number of the building small dam is relatively small. Even reaching to 8% changes, building two more small dams from the original can meet the demand of electricity and water. While Zambia and Zimbabwe are African countries, so that they are in a relatively poor condition. Due to the lack of economic development momentum, the change in its economic growth in the future is relatively small. Therefore, it is a reasonable choice of constructing 12 dams.

<!-- b000695 | furniture | pages [18] -->


<!-- b000696 | furniture | pages [19] -->
Team # 55069                                                            Page 17 of 28

<!-- b000697 | prose | pages [19] -->
Alteration in the economic growth rate has little impact on the position of dams. Basing on the fact that Kariba gorge is about 34.9 kilometers, and we only need to build 10 to 20 small dam in the canyon, also small dams need to maintain a certain distance, so that the small dam’s location is relatively stable and the change is not great.

<!-- b000698 | prose | pages [19] -->
In conclusion, we can see that the representative index of its economic development is reasonable. Despite the fact that the figure floats up and down, its influence on the number and location of small dams is relatively small. It also shows that the model we established in the previous paper about the location and quantity of small dams is robust and has good adaptability to the reality.

<!-- b000699 | heading | pages [19] -->
7.2  The Model of Modulating Water Flow

<!-- b000700 | prose | pages [19] -->
Output coefficient is a comprehensive benefit coefficient which reflects water-turbine generator set’s overall efficiency. It equals to turbine efficiency, generator efficiency, transfer efficiency multiply invariant constant 9.81. Its value is up to the scale of Hydropower Station Dam. For Large hydropower station the value is about 8.5.For media hydropower station the value is about 8-8.5. While for small hydropower station the value is about 6.0-8.0. Multiply the coefficient, water-head and water-flow and the answer will be the unit’s output.

<!-- b000701 | prose | pages [19] -->
We analyze the change of output coefficient’s influence on the joint operation of dam system in the Table 7.

<!-- b000702 | caption | pages [19] -->
Table 7 The Sensitivity of the Output Coefficient

<!-- b000703 | furniture | pages [19] -->


<!-- b000704 | prose | pages [19] -->
 15% We could see from the Table 7 that,output coefficient K change about would bring about  and  change for about only  5% . This indicates that output coefficient K is not

<!-- b000705 | prose | pages [19] -->
an important factor for joint operation of the dam system.

<!-- b000706 | heading | pages [19] -->
8. Further Discussion

<!-- b000707 | prose | pages [19] -->
 Take the future benefits into account. Reservoir operation not only has the current economic and social benefits, but also has the economic and social benefits in the future The future economic benefits can be expressed by the total energy storage at the end of the

<!-- b000708 | furniture | pages [19] -->


<!-- b000709 | furniture | pages [20] -->
Team # 55069                                                            Page 18 of 28

<!-- b000710 | prose | pages [20] -->
dispatching cycle, the greater the total energy storage, the more the potential for future development. The social benefits in the future can be illustrated as the total capacity in the last scheduling period. Generally speaking, the more water storage in the reservoir, the more able to meet the needs of future generations.

<!-- b000711 | prose | pages [20] -->
n T

<!-- b000712 | prose | pages [20] -->
 

<!-- b000713 | prose | pages [20] -->
I

<!-- b000714 | prose | pages [20] -->
[

<!-- b000715 | prose | pages [20] -->
K

<!-- b000716 | prose | pages [20] -->
*

<!-- b000717 | prose | pages [20] -->
q

<!-- b000718 | prose | pages [20] -->
*

<!-- b000719 | prose | pages [20] -->
H

<!-- b000720 | prose | pages [20] -->
*

<!-- b000721 | prose | pages [20] -->


<!-- b000722 | prose | pages [20] -->
e i ij ij

<!-- b000723 | prose | pages [20] -->
 

<!-- b000724 | prose | pages [20] -->
i

<!-- b000725 | prose | pages [20] -->
1

<!-- b000726 | prose | pages [20] -->
j

<!-- b000727 | prose | pages [20] -->
1

<!-- b000728 | prose | pages [20] -->
n

<!-- b000729 | prose | pages [20] -->
 

<!-- b000730 | prose | pages [20] -->
t t

<!-- b000731 | prose | pages [20] -->
(

<!-- b000732 | prose | pages [20] -->
h h

<!-- b000733 | prose | pages [20] -->
)(

<!-- b000734 | prose | pages [20] -->
Q q

<!-- b000735 | prose | pages [20] -->
)]

<!-- b000736 | furniture | pages [20] -->


<!-- b000737 | prose | pages [20] -->


<!-- b000738 | prose | pages [20] -->
(

<!-- b000739 | prose | pages [20] -->
i

<!-- b000740 | prose | pages [20] -->
1),

<!-- b000741 | prose | pages [20] -->
j i j

<!-- b000742 | prose | pages [20] -->
,

<!-- b000743 | prose | pages [20] -->
ij ij

<!-- b000744 | prose | pages [20] -->
T T

<!-- b000745 | prose | pages [20] -->
  

<!-- b000746 | prose | pages [20] -->
I V

<!-- b000747 | prose | pages [20] -->
s T

<!-- b000748 | prose | pages [20] -->


<!-- b000749 | prose | pages [20] -->
i

<!-- b000750 | prose | pages [20] -->
h illustrates the water level of thi dam in the ij

<!-- b000751 | prose | pages [20] -->
in the end of the dispatching period.

<!-- b000752 | prose | pages [20] -->


<!-- b000753 | prose | pages [20] -->


<!-- b000754 | furniture | pages [20] -->


<!-- b000755 | prose | pages [20] -->
(

<!-- b000756 | prose | pages [20] -->
S D

<!-- b000757 | prose | pages [20] -->
)

<!-- b000758 | prose | pages [20] -->
ij ij

<!-- b000759 | prose | pages [20] -->
 

<!-- b000760 | prose | pages [20] -->
1 1

<!-- b000761 | prose | pages [20] -->
i i

<!-- b000762 | prose | pages [20] -->
1

<!-- b000763 | prose | pages [20] -->
V indicates the dam’s water storage thj period, T

<!-- b000764 | prose | pages [20] -->
Increase ecological benefits：Most people pay more attention to the traditional functions of power generation, flood control, water supply and so on. We will further consider the ecological benefits of the reservoir. We do not take the ecological flow as a constraint, but consider it as one of the scheduling objectives, but there are many difficulties.

<!-- b000765 | prose | pages [20] -->
n T

<!-- b000766 | prose | pages [20] -->


<!-- b000767 | prose | pages [20] -->
f V Q q de I

<!-- b000768 | prose | pages [20] -->
en

<!-- b000769 | prose | pages [20] -->
 

<!-- b000770 | prose | pages [20] -->
i

<!-- b000771 | prose | pages [20] -->
1

<!-- b000772 | prose | pages [20] -->
j

<!-- b000773 | prose | pages [20] -->
1 ( ( , , , )

<!-- b000774 | furniture | pages [20] -->


<!-- b000775 | prose | pages [20] -->
ij ij ij ij

<!-- b000776 | prose | pages [20] -->
de is the ecological water requirement of the thi dam in the ij

<!-- b000777 | prose | pages [20] -->


<!-- b000778 | prose | pages [20] -->
thj period.

<!-- b000779 | prose | pages [20] -->
In order to avoid the large change of the reservoir water level, which could lead to the change of the geological condition, and even cause the reservoir earthquake. So we will

<!-- b000780 | prose | pages [20] -->
 increase the constraint condition.

<!-- b000781 | prose | pages [20] -->
h h it i , (

<!-- b000782 | prose | pages [20] -->
of reservoir water level.

<!-- b000783 | heading | pages [20] -->
9 Strengths and Weaknesses

<!-- b000784 | heading | pages [20] -->
9.1 Strengths

<!-- b000785 | prose | pages [20] -->


<!-- b000786 | prose | pages [20] -->
 is the allowable variation   ,in which i   t t 1) i

<!-- b000787 | prose | pages [20] -->
Our models are robust while the parameters changes. That is to say, a slight change of parameter will not cause a significant change of the results.

<!-- b000788 | prose | pages [20] -->
 Our models can be well applied in other places and we just need to change a little the specific conditions.

<!-- b000789 | prose | pages [20] -->
 Based on different situation, we develop the corresponding modulating strategy and make

<!-- b000790 | furniture | pages [20] -->


<!-- b000791 | furniture | pages [21] -->
Team # 55069                                                            Page 19 of 28

<!-- b000792 | prose | pages [21] -->
a relative comprehensive plan. This can provide a specific guidance for the ZRA.

<!-- b000793 | prose | pages [21] -->
 Our data comes from the official website such as Central Statistical Office, Zambia, which is believable.

<!-- b000794 | heading | pages [21] -->
9.2 Weaknesses

<!-- b000795 | prose | pages [21] -->
 Our model didn’t consider the economic, social and environment benefits in the future. We mainly focus on the current benefits. But in fact, future prospects is important for sustainable development. So we add it to the further discussion and hope we can solve it in the future.

<!-- b000796 | prose | pages [21] -->
 There are not much data regarding the demand of the electricity and water. So the analysis of the demand may be not exhaustive and it may have some deviations. But it didn’t affect the results significantly.

<!-- b000797 | prose | pages [21] -->
 The data of some parameters is forecast data because we don’t build the dams. However, based on the sensitivity analysis, they will not make a great difference if parameters are slightly changed.

<!-- b000798 | heading | pages [21] -->
10 Conclusion

<!-- b000799 | prose | pages [21] -->
Through the establishment of three models, we evaluate the three plans respectively. First,we select the number and location of the dam, then plan the joint operation of the dam system. We consider the comprehensive evaluation of three options from five aspects: direct cost, potential cost, economic benefits, environmental benefits and social benefits. Through the AHP analysis, we draw the conclusion that option three is a relatively good solution.

<!-- b000800 | prose | pages [21] -->
Then, we establish a multi-objective optimization model to determine the number and location of the dams. We let the water resources management capacity and cost to be the objective function, and let the water balance function, water level limit, the protection of water resources and the number to be the constraints. We also use genetic algorithm to solve the problem and find that the 12 dam is a relatively satisfactory results, and determine their geographic location.

<!-- b000801 | prose | pages [21] -->
After determining the number and location of the dam, we established a joint operation model of dam system. We let the economic and social benefits as the goal, water balance function and flow limitation to be the constraints. Considering four different year type, we use genetic algorithm to solve and determine the corresponding scheduling scheme, Also,the sensitivity results show that the joint operation of dams can be well adapted to different climatic conditions.

<!-- b000802 | prose | pages [21] -->
Finally, we make an objective analysis of the advantages and disadvantages of the model and make an attempt to further expand the model in order to make our model and method more successful.

<!-- b000803 | furniture | pages [21] -->


<!-- b000804 | furniture | pages [21] -->


<!-- b000805 | furniture | pages [21] -->


<!-- b000806 | furniture | pages [22] -->
Team # 55069                                                            Page 20 of 28

<!-- b000807 | heading | pages [22] -->
11 The Evaluation of Three Options

<!-- b000808 | prose | pages [22] -->
South Africa had just warned that the dam was in desperate need of rehabilitation. The reasons may as follows :

<!-- b000809 | prose | pages [22] -->
 Forcing people who dwell downstream to evacuate since the heavy rain might lead to a release of water from the dam.

<!-- b000810 | prose | pages [22] -->
 Basing on a seemingly solid bed of basalt，the Kariba Dam has been eroded by the torrents from the spillway, which could give rise to severe collapse without urgent repairs.

<!-- b000811 | prose | pages [22] -->
With the three options already given, we adopt AHP model using two most influential criterion to provide a brief overview of potential costs and benefits.

<!-- b000812 | prose | pages [22] -->
Jery Stedinger and Pete Loucks（February 1982）[10]thought that evaluation criterion of dam should include reliability ,resiliency, and vulnerability criteria; Mohamed Rami Mahmoud and Luis A. Garcia (July 2000) [11] propose different multicriteria evaluation methods for the Red Bluff diversion dam. With the help of the current literatures, we develop AHP model considering these main factors.

<!-- b000813 | heading | pages [22] -->
11.1  Establish a Hierarchical Model

<!-- b000814 | prose | pages [22] -->
Cost Index

<!-- b000815 | prose | pages [22] -->
Chengxinwen (2008) [12] proposed the components of the cost while constructing operating or repairing. In addition, the expense of rebuilding the Kariba Dam is significantly greater than just repairing the existing one. The factors below are of great importance.

<!-- b000816 | prose | pages [22] -->
 Direct cost(Demolition[A1] 、Construction[A2] 、Operation[A3] 、Maintenance and management expense[A4])

<!-- b000817 | prose | pages [22] -->
 Potential cost(Dam failure loss[B1]、Flowage damage[B2])

<!-- b000818 | prose | pages [22] -->
Benefit Index

<!-- b000819 | prose | pages [22] -->
Replacing the bigger dams with ten to twenty smaller dams could bring about advantages and disadvantages. Our goal is to seek out whether it is beneficial or not to removing the Kariba dam. We divide the benefit index into three main categories below:[ 13]

<!-- b000820 | prose | pages [22] -->
 Economic effect (Irrigation[C1]、Water-supply[C2]、Power generation[C3]、Navigation benefits[C4])

<!-- b000821 | prose | pages [22] -->
 Environmental effect (Climate change[D1]；Alteration in river ecosystem[D2])

<!-- b000822 | prose | pages [22] -->
 Social effect (Flood control benefit[E1]；Drought resistance benefit[E2])

<!-- b000823 | prose | pages [22] -->
Through above analysis of the three main criterion, which affect evaluation significantly, hierarchy figure is shown in

<!-- b000824 | furniture | pages [22] -->


<!-- b000825 | furniture | pages [23] -->
Team # 55069                                                            Page 21 of 28

<!-- b000826 | furniture | pages [23] -->


<!-- b000827 | caption | pages [23] -->
Figure 4  Hierarchy figure

<!-- b000828 | prose | pages [23] -->
In Figure 4 we let the Direct cost to be Index A;Potential cost to be Index B;Economic effect to be Index C;Environmental effect to be Index D;Social effect to be index E;We divide these index into more specific index(namely A1 A2 A3 etc.) and we show that above.

<!-- b000829 | heading | pages [23] -->
11.2  Analysis and Results

<!-- b000830 | prose | pages [23] -->
We construct comparison matrix by comparison method of 1-7，then we get the weights of each index.(Complete matrix of project hierarchy can be seen in the appendix.)[14]

<!-- b000831 | caption | pages [23] -->
Table 8 Pairwise Comparison Matrix of Hierarchy II-III

<!-- b000832 | prose | pages [23] -->
Comprehensive

<!-- b000833 | prose | pages [23] -->
Direct cost

<!-- b000834 | prose | pages [23] -->
impact

<!-- b000835 | prose | pages [23] -->
Direct cost 1 Potential cost 1/4

<!-- b000836 | prose | pages [23] -->
Potential cost Weight

<!-- b000837 | prose | pages [23] -->
4 0.8 1 0.2

<!-- b000838 | caption | pages [23] -->
Table 9 Pairwise Comparison Matrix of Hierarchy II-III

<!-- b000839 | prose | pages [23] -->
Environmental

<!-- b000840 | prose | pages [23] -->
Comprehensive

<!-- b000841 | prose | pages [23] -->
Economic

<!-- b000842 | prose | pages [23] -->
impact

<!-- b000843 | prose | pages [23] -->
effect

<!-- b000844 | prose | pages [23] -->
Economic effect 1 Environmental

<!-- b000845 | prose | pages [23] -->
1/2

<!-- b000846 | prose | pages [23] -->
effect

<!-- b000847 | prose | pages [23] -->
Social effect 1/5 Consistency ratio：0.0961

<!-- b000848 | prose | pages [23] -->
Social

<!-- b000849 | prose | pages [23] -->
Weight

<!-- b000850 | prose | pages [23] -->
effect

<!-- b000851 | prose | pages [23] -->
effect

<!-- b000852 | prose | pages [23] -->
2 5 0.2908

<!-- b000853 | prose | pages [23] -->
1 3 0.1545

<!-- b000854 | prose | pages [23] -->
1/3 1 0.0547

<!-- b000855 | prose | pages [23] -->
With the five index. only the Economic and Environment effect are positive. Moreover, from above tables, we know that all Consistency Test is right.

<!-- b000856 | prose | pages [23] -->
We could draw conclusions from the weight that the direct cost is of great importance to constructing a dam, potential cost has close relationship to repairing a dam; Also, we could gain better economic and navigation effect when we choose option 3.[15]

<!-- b000857 | prose | pages [23] -->
Due to the index and results above, we arrive at a conclusion that option 3 is our best choice to concerning the potential cost and benefit.

<!-- b000858 | furniture | pages [23] -->


<!-- b000859 | furniture | pages [23] -->


<!-- b000860 | furniture | pages [24] -->
Team # 55069                                                            Page 22 of 28

<!-- b000861 | prose | pages [24] -->
Reference

<!-- b000862 | prose | pages [24] -->
[1] http://www.zaraho.org.zm/hydrology/lake-levels

<!-- b000863 | prose | pages [24] -->
[2]Grigier J C and Stedinger J R. Algorithms for network programming. Wiley-interscience publication, 1980

<!-- b000864 | prose | pages [24] -->
[3] Dekay M L， Mcclelland G H. Predicting loss of life in cases of dam failure and flash flood[J]. Risk analysis， 1993， 13(2):193-205

<!-- b000865 | prose | pages [24] -->
[4] http://www.icold-cigb.org/GB/dams/dams_and_environment.asp

<!-- b000866 | prose | pages [24] -->
[5]Ayvaz MT (2009a) Application of Harmony Search algorithm to the solution of groundwater management models. Adv Water Resour 32:916–924

<!-- b000867 | prose | pages [24] -->
[6]Chang L C， Chang F J． Multi-objective evolutionary algorithm for operating parallel reservoir system [J]． Journal of Hydrology，2009，377：12-20．

<!-- b000868 | prose | pages [24] -->
[7]Approved consolidated baseline and monitoring methodology ACM0002

<!-- b000869 | prose | pages [24] -->
[8] http://www.zaraho.org.zm/

<!-- b000870 | prose | pages [24] -->
[9] http://worldweather.wmo.int/en/city.html?cityId=966

<!-- b000871 | prose | pages [24] -->
[10] Larkin, P. A.,  Maybe you can't get there from hcre:  Hi\tory  of research  in  relation to management of kicific Salmon. J. Fish. Res. Board Can.. 36(1). 98-106,1979.

<!-- b000872 | prose | pages [24] -->
[11] Tecle, A., 1992. Selecting a multicriterion decision making techniquefor watershed resources management. Water Resources Bulletin 28(1), 129–140.

<!-- b000873 | prose | pages [24] -->
[12] Larkin,  P. A.,  Maybe  you  can't  get  there  from  hcre:  Hi\tory  of research in  relation  to management  of  kicific  Salmon.  J. Fish. Res. Board Can.. 36(1). 98- 106,  1979.

<!-- b000874 | prose | pages [24] -->
[13] Loucks, D.  P., J. R.Stedinger. and D.  A. Hiuth.  \\.crfer Hr.courre Systems Planning and Analysis, Rent~cc-Hall.  Engleu-ood Cliffs. New Jersev.  1981.

<!-- b000875 | prose | pages [24] -->
[14] Mark, R. K.,  and  D.  E.  Stuart-Alexander. D~sa*tcr  as a ncccssclry part of benefit-cost analyses. Sclrnrr. 197,  I  ItrO.  1977.

<!-- b000876 | prose | pages [24] -->
[15] Velikanov,  A.  K.,  The  aspects  of  lonp-tcnr, water  re- sources planning  as applied  to  the  integr~ted  regional  development  problem,  Collahor.  Pap.  CP- 37-l.  11-11,  In>[.  for  Appl. Systems Anal.,  Laxenburg, Austria. Mnv  1979.

<!-- b000877 | furniture | pages [24] -->


<!-- b000878 | furniture | pages [24] -->


<!-- b000879 | furniture | pages [24] -->


<!-- b000880 | furniture | pages [24] -->


<!-- b000881 | furniture | pages [25] -->
Team # 55069                                                            Page 23 of 28

<!-- b000882 | heading | pages [25] -->
Appendix

<!-- b000883 | prose | pages [25] -->
Part1: Comparison matrix of criterion hierarchy

<!-- b000884 | caption | pages [25] -->
Table 10 Pairwise comparison matrix of hierarchy II-III

<!-- b000885 | prose | pages [25] -->
Comprehensive

<!-- b000886 | prose | pages [25] -->
Direct cost

<!-- b000887 | prose | pages [25] -->
impact

<!-- b000888 | prose | pages [25] -->
Direct cost 1 Potential cost 1/4

<!-- b000889 | prose | pages [25] -->
Potential cost Weight

<!-- b000890 | prose | pages [25] -->
4 0.8 1 0.2

<!-- b000891 | caption | pages [25] -->
Table 11 Pairwise comparison matrix of hierarchy II-III

<!-- b000892 | prose | pages [25] -->
Environmental

<!-- b000893 | prose | pages [25] -->
Comprehensive

<!-- b000894 | prose | pages [25] -->
Economic

<!-- b000895 | prose | pages [25] -->
Social

<!-- b000896 | prose | pages [25] -->
Weight

<!-- b000897 | prose | pages [25] -->
effect

<!-- b000898 | prose | pages [25] -->
impact

<!-- b000899 | prose | pages [25] -->
effect

<!-- b000900 | prose | pages [25] -->
Economic

<!-- b000901 | prose | pages [25] -->
1

<!-- b000902 | prose | pages [25] -->
effect

<!-- b000903 | prose | pages [25] -->
Environmental

<!-- b000904 | prose | pages [25] -->
1/2

<!-- b000905 | prose | pages [25] -->
effect

<!-- b000906 | prose | pages [25] -->
Social

<!-- b000907 | prose | pages [25] -->
1/5

<!-- b000908 | prose | pages [25] -->
effect

<!-- b000909 | prose | pages [25] -->
Consistency ratio：0.0961

<!-- b000910 | prose | pages [25] -->
effect

<!-- b000911 | prose | pages [25] -->
2 2 5 0.2908

<!-- b000912 | prose | pages [25] -->
1 1 3 0.1545

<!-- b000913 | prose | pages [25] -->
1/3 1 0.0547

<!-- b000914 | caption | pages [25] -->
Table 12 Pairwise comparison matrix of hierarchyIII-IV

<!-- b000915 | prose | pages [25] -->
Construction

<!-- b000916 | prose | pages [25] -->
Comprehensive

<!-- b000917 | prose | pages [25] -->
Demolition

<!-- b000918 | prose | pages [25] -->
impact

<!-- b000919 | prose | pages [25] -->
expense

<!-- b000920 | prose | pages [25] -->
expense

<!-- b000921 | prose | pages [25] -->
Demolition 1 1/9 Construction 9 1 Operation 2 1/4 Maintenance

<!-- b000922 | prose | pages [25] -->
1/3 1/9

<!-- b000923 | prose | pages [25] -->
management

<!-- b000924 | prose | pages [25] -->
Consistency ratio: 0.0405

<!-- b000925 | prose | pages [25] -->
Operation

<!-- b000926 | prose | pages [25] -->
Maintenance

<!-- b000927 | prose | pages [25] -->
Weight

<!-- b000928 | prose | pages [25] -->
expense

<!-- b000929 | prose | pages [25] -->
Management

<!-- b000930 | prose | pages [25] -->
expense

<!-- b000931 | prose | pages [25] -->
1/2 3 0.0403 4 9 0.2672 1 4 0.0728

<!-- b000932 | prose | pages [25] -->
1/4 1 0.0197

<!-- b000933 | caption | pages [25] -->
Table 13 Pairwise comparison matrix of hierarchy III-IV

<!-- b000934 | prose | pages [25] -->
Comprehensive

<!-- b000935 | prose | pages [25] -->
Dam failure loss

<!-- b000936 | prose | pages [25] -->
impact

<!-- b000937 | prose | pages [25] -->
Dam failure loss 1 Flowage damage 5

<!-- b000938 | prose | pages [25] -->
Consistency ratio：0.0122

<!-- b000939 | furniture | pages [25] -->


<!-- b000940 | prose | pages [25] -->
Flowage damage Weight

<!-- b000941 | prose | pages [25] -->
1/5 0.0167 1 0.0833

<!-- b000942 | furniture | pages [26] -->
Team # 55069                                                            Page 24 of 28

<!-- b000943 | caption | pages [26] -->
Table 14 Pairwise comparison matrix of hierarchy III-IV

<!-- b000944 | prose | pages [26] -->
Comprehensive

<!-- b000945 | prose | pages [26] -->
Irrigation Water-

<!-- b000946 | prose | pages [26] -->
impact

<!-- b000947 | prose | pages [26] -->
supply

<!-- b000948 | prose | pages [26] -->
Irrigation 1 3 Water-supply 1/3 1 Power 5 9 Navigation 1/2 4

<!-- b000949 | prose | pages [26] -->
Consistency ratio：0.0684

<!-- b000950 | prose | pages [26] -->
Power

<!-- b000951 | prose | pages [26] -->
Navigation

<!-- b000952 | prose | pages [26] -->
Weight

<!-- b000953 | prose | pages [26] -->
generation

<!-- b000954 | prose | pages [26] -->
benefits

<!-- b000955 | prose | pages [26] -->
1/5 2 0.0466 1/9 1/4 0.0143 1 8 0.1968 1/8 1 0.0331

<!-- b000956 | caption | pages [26] -->
Table 15. Pairwise comparison matrix of hierarchy III-IV

<!-- b000957 | prose | pages [26] -->
Comprehensive

<!-- b000958 | prose | pages [26] -->
Climate change

<!-- b000959 | prose | pages [26] -->
impact

<!-- b000960 | prose | pages [26] -->
Climate change 1 Alteration 1/2

<!-- b000961 | prose | pages [26] -->
Consistency ratio：0.0674

<!-- b000962 | prose | pages [26] -->
Alteration in river

<!-- b000963 | prose | pages [26] -->
Weight

<!-- b000964 | prose | pages [26] -->
ecosystem

<!-- b000965 | prose | pages [26] -->
2 0.1030 1 0.0513

<!-- b000966 | caption | pages [26] -->
Table 16. Pairwise comparison matrix of hierarchy III-IV

<!-- b000967 | prose | pages [26] -->
Comprehensive

<!-- b000968 | prose | pages [26] -->
Flood control

<!-- b000969 | prose | pages [26] -->
impact

<!-- b000970 | prose | pages [26] -->
benefit

<!-- b000971 | prose | pages [26] -->
Flood control

<!-- b000972 | prose | pages [26] -->
1

<!-- b000973 | prose | pages [26] -->
benefit

<!-- b000974 | prose | pages [26] -->
Drought resistance

<!-- b000975 | prose | pages [26] -->
1/3

<!-- b000976 | prose | pages [26] -->
benefit

<!-- b000977 | prose | pages [26] -->
Consistency ratio：0.021

<!-- b000978 | prose | pages [26] -->
Drought resistance

<!-- b000979 | prose | pages [26] -->
Weight

<!-- b000980 | prose | pages [26] -->
benefit

<!-- b000981 | prose | pages [26] -->
3 0.0410

<!-- b000982 | prose | pages [26] -->
1 0.0137

<!-- b000983 | prose | pages [26] -->
Part2: Comparison matrix of project hierarchy

<!-- b000984 | prose | pages [26] -->
A1 Op1 Op2 Op3 A2 Op1

<!-- b000985 | prose | pages [26] -->
Op1 1 1/6 2 Op1 1

<!-- b000986 | prose | pages [26] -->
Op2 6 1 8 Op2 10

<!-- b000987 | prose | pages [26] -->
Op3 1/2 1/8 1 Op3 1/2

<!-- b000988 | prose | pages [26] -->
A4 Op1 Op2 Op3 B1 Op1

<!-- b000989 | prose | pages [26] -->
Op1 1 2 3 Op1 1

<!-- b000990 | prose | pages [26] -->
Op2 1/2 1 2 Op2 1/2

<!-- b000991 | prose | pages [26] -->
Op3 1/3 1/2 1 Op3 1/4

<!-- b000992 | prose | pages [26] -->
C1 Op1 Op2 Op3 C2 Op1

<!-- b000993 | prose | pages [26] -->
Op1 1 1/2 1/3 Op1 1

<!-- b000994 | prose | pages [26] -->
Op2 2 1 1/2 Op2 3

<!-- b000995 | prose | pages [26] -->
Op3 3 2 1 Op3 4

<!-- b000996 | prose | pages [26] -->
C4 Op1 Op2 Op3 D1 Op1

<!-- b000997 | furniture | pages [26] -->


<!-- b000998 | prose | pages [26] -->
Op2 Op3 A3 Op1 Op2 Op3

<!-- b000999 | prose | pages [26] -->
1/10 2 Op1 1 1/3 2

<!-- b001000 | prose | pages [26] -->
1 11 Op2 3 1 2

<!-- b001001 | prose | pages [26] -->
1/11 1 Op3 1/2 1/2 1

<!-- b001002 | prose | pages [26] -->
Op2 Op3 B2 Op1 Op2 Op3

<!-- b001003 | prose | pages [26] -->
2 4 Op1 1 4 6

<!-- b001004 | prose | pages [26] -->
1 2 Op2 1/4 1 3

<!-- b001005 | prose | pages [26] -->
1/2 1 Op3 1/6 1/3 1

<!-- b001006 | prose | pages [26] -->
Op2 Op3 C3 Op1 Op2 Op3

<!-- b001007 | prose | pages [26] -->
1/3 1/4 Op1 1 1/2 3

<!-- b001008 | prose | pages [26] -->
1 1/2 Op2 2 1 4

<!-- b001009 | prose | pages [26] -->
2 1 Op3 1/3 1/4 1

<!-- b001010 | prose | pages [26] -->
Op2 Op3 D2 Op1 Op2 Op3

<!-- b001011 | furniture | pages [27] -->
Team # 55069                                                            Page 25 of 28

<!-- b001012 | prose | pages [27] -->
Op1 1 1/2 2 Op1 1

<!-- b001013 | prose | pages [27] -->
Op2 2 1 3 Op2 1/4

<!-- b001014 | prose | pages [27] -->
Op3 1/2 1/3 1 Op3 2

<!-- b001015 | prose | pages [27] -->
E1 Op1 Op2 Op3 E2 Op1

<!-- b001016 | prose | pages [27] -->
Op1 1 1/2 1/6 Op1 1

<!-- b001017 | prose | pages [27] -->
Op2 2 1 1/8 Op2 2

<!-- b001018 | prose | pages [27] -->
Op3 6 8 1 Op3 4

<!-- b001019 | prose | pages [27] -->
4 1/2 Op1 1 4 1/2

<!-- b001020 | prose | pages [27] -->
1 1/7 Op2 1/4 1 1/8

<!-- b001021 | prose | pages [27] -->
7 1 Op3 2 8 1

<!-- b001022 | prose | pages [27] -->
Op2 Op3

<!-- b001023 | furniture | pages [27] -->


<!-- b001024 | furniture | pages [27] -->


<!-- b001025 | furniture | pages [27] -->


<!-- b001026 | furniture | pages [27] -->


<!-- b001027 | prose | pages [27] -->
1/2 1/4

<!-- b001028 | furniture | pages [27] -->


<!-- b001029 | furniture | pages [27] -->


<!-- b001030 | furniture | pages [27] -->


<!-- b001031 | furniture | pages [27] -->


<!-- b001032 | prose | pages [27] -->
1 1/3

<!-- b001033 | furniture | pages [27] -->


<!-- b001034 | furniture | pages [27] -->


<!-- b001035 | furniture | pages [27] -->


<!-- b001036 | furniture | pages [27] -->


<!-- b001037 | prose | pages [27] -->
3 1

<!-- b001038 | furniture | pages [27] -->


<!-- b001039 | furniture | pages [27] -->


<!-- b001040 | furniture | pages [27] -->


<!-- b001041 | furniture | pages [27] -->


<!-- b001042 | heading | pages [27] -->
Part three :the data of model of determination of number and location

<!-- b001043 | furniture | pages [27] -->


<!-- b001044 | furniture | pages [27] -->


<!-- b001045 | heading | pages [27] -->
Part four: the model of modulating of water flow

<!-- b001046 | prose | pages [27] -->
 The climate and hydrology of Kariba area

<!-- b001047 | furniture | pages [27] -->


<!-- b001048 | furniture | pages [28] -->
Team # 55069                                                            Page 26 of 28

<!-- b001049 | furniture | pages [28] -->


<!-- b001050 | prose | pages [28] -->
Mean Daily

<!-- b001051 | prose | pages [28] -->
Mean Daily

<!-- b001052 | prose | pages [28] -->
Maximum

<!-- b001053 | prose | pages [28] -->
Minimum

<!-- b001054 | prose | pages [28] -->
Mean Total

<!-- b001055 | prose | pages [28] -->
Mean Number

<!-- b001056 | prose | pages [28] -->
Temperature

<!-- b001057 | prose | pages [28] -->
Month

<!-- b001058 | prose | pages [28] -->
Temperature

<!-- b001059 | prose | pages [28] -->
Jan 21.8

<!-- b001060 | prose | pages [28] -->
Rainfall

<!-- b001061 | prose | pages [28] -->
of Rain Days 31 191.6 16 30.8 Feb 21.4 157.7 13 31.2 Mar 20.7 112.5 10 30.5 Apr 18.5 30 3 28.5 May 14.3 4.2 1 26.3 Jun 11.2 1 0 26.3 Jul 11.1 0.6 0 28.9 Aug 13.9 0.1 0 32.9 Sep 19.1 0.6 0 35.1 Oct 23.2 17.8 2 33.9 Nov 23.4 74.4 7 31.3 Dec 22.1

<!-- b001062 | prose | pages [28] -->
 The reservoir levels

<!-- b001063 | furniture | pages [28] -->


<!-- b001064 | prose | pages [28] -->
175 14

<!-- b001065 | furniture | pages [29] -->
Team # 55069                                                            Page 27 of 28

<!-- b001066 | furniture | pages [29] -->


<!-- b001067 | prose | pages [29] -->
 The strategy

<!-- b001068 | prose | pages [29] -->
 Normal flow year

<!-- b001069 | furniture | pages [29] -->


<!-- b001070 | prose | pages [29] -->
 Low flow year

<!-- b001071 | furniture | pages [29] -->


<!-- b001072 | furniture | pages [30] -->
Team # 55069                                                            Page 28 of 28

<!-- b001073 | furniture | pages [30] -->


<!-- b001074 | prose | pages [30] -->
 High flow year

<!-- b001075 | furniture | pages [30] -->


<!-- b001076 | prose | pages [30] -->
 Differentiation year

<!-- b001077 | furniture | pages [30] -->


<!-- b001078 | furniture | pages [30] -->


<!-- b001079 | furniture | pages [30] -->


<!-- b001080 | furniture | pages [30] -->

