# P-B-2022-2202748-102f6d4c

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2022

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | title | pages [1] -->
2202748

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
Salvation in an Age of Water Scarcity

<!-- b000009 | prose | pages [1] -->
As drought worsens in the western United States, the Colorado River, the lifeline of the Southwest, is in dire straits. In the Colorado River basin, it is important to allocate water wisely. This paper aims at measuring competing interests of different users in different states and making a water and hydroelectric power allocation plan suitable for different environmental conditions.

<!-- b000010 | prose | pages [1] -->
Two models are mainly established: Model I: Water and Electricity Transportation Model； Model II: Coordinated Development of Multi-objective Programming Model.

<!-- b000011 | prose | pages [1] -->
Before all the models are established, we analyze the reservoirs of the Glen Canyon dam and Hoover dam, get the relationship between water height in the reservoir and the volume of water in the reservoirs.

<!-- b000012 | prose | pages [1] -->
For Model I: In order to reasonably allocation water and electricity, we set up a Transportation Model of water and electricity. The objective function is the minimum supply of water from the two dams. The constraint conditions are mainly the constraint of minimum generating water level on supply and the constraint of demand on supply.

<!-- b000013 | prose | pages [1] -->
By analyzing the geographical position and topography of five states, the Glen Canyon dam and Hoover dam, we get the relationship between water flow direction and water resource transfer between the two dams, which reflects the water supply situation. After analyzing the loss of water and electricity during transportation, the final constraint conditions are obtained. Then, we designed the Maintenance Time Calculation Algorithm to solve the longest time to maintain the demand without the addition of additional water. Finally, we assign the initial water level of Lake Powell and Lake Mead to the numerical result Section 5.4.

<!-- b000014 | prose | pages [1] -->
For Model II: This Model is a further extension of Model I, which balances the competing interests of industry, agriculture and residents in five states. The supply of water is reflected in three aspects: Social effect, Economic effect and Environmental effect. The supply of electricity is reflected in Social effect and Economic effect.

<!-- b000015 | prose | pages [1] -->
When the situation of water shortage does not occur, we mainly consider the Economic effect of industrial, agricultural and residential use objects in five states. When water shortage occurs, we combine three effects to carry out multi-objective planning. See Section 6.3 for the results.

<!-- b000016 | prose | pages [1] -->
Additionally, we have taken into account the rights and interests of Mexico and propose an allocation plan for Mexico under the condition of different water resources remaining.

<!-- b000017 | prose | pages [1] -->
Finally, sensitivity analysis includes the influences of the changes over time in the demand for water and electricity of three types of objects (industry, agriculture and residents), the development of renewable energy technology and water and electricity conservation measures.

<!-- b000018 | keywords | pages [1] -->
Keywords: Transportation Model; Multi-objective Programming; Distribution and tradeoff

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1 Introduction .......................................................................................................................................... 3

<!-- b000021 | contents | pages [2] -->
1.1 Background ................................................................................................................................... 3

<!-- b000022 | contents | pages [2] -->
1.2 Restatement of the Problem .......................................................................................................... 3

<!-- b000023 | contents | pages [2] -->
1.3 Our Work ....................................................................................................................................... 4

<!-- b000024 | contents | pages [2] -->
2 Assumptions and Justifications ........................................................................................................... 5

<!-- b000025 | contents | pages [2] -->
3 Notations ............................................................................................................................................... 5

<!-- b000026 | contents | pages [2] -->
4 Model Preparation ............................................................................................................................... 6

<!-- b000027 | contents | pages [2] -->
4.1 Data Collection ............................................................................................................................. 6

<!-- b000028 | contents | pages [2] -->
4.2 Relationship between Water Level and Storage Volume .............................................................. 6

<!-- b000029 | contents | pages [2] -->
5 Model I: Water and Electricity Transportation Model .................................................................... 8

<!-- b000030 | contents | pages [2] -->
5.1 Basic Ideas .................................................................................................................................... 8

<!-- b000031 | contents | pages [2] -->
5.2 Establishment of Transportation Model ........................................................................................ 9

<!-- b000032 | contents | pages [2] -->
5.3 Maintenance Time Calculation Algorithm .................................................................................. 12

<!-- b000033 | contents | pages [2] -->
5.4 Calculation Results ..................................................................................................................... 13

<!-- b000034 | contents | pages [2] -->
6 Model II: Coordinated Development of Multi-objective Programming Model ........................... 14

<!-- b000035 | contents | pages [2] -->
6.1 The Establishment of Multi-objective Programming Model ...................................................... 14

<!-- b000036 | contents | pages [2] -->
6.2 Parameters to Determine ............................................................................................................. 17

<!-- b000037 | contents | pages [2] -->
6.3 Calculation Results ..................................................................................................................... 20

<!-- b000038 | contents | pages [2] -->
7 Mexican Allocation Model ................................................................................................................. 21

<!-- b000039 | contents | pages [2] -->
7.1 The Establishment of Mexican Allocation Model ...................................................................... 21

<!-- b000040 | contents | pages [2] -->
7.2 Calculation Results ..................................................................................................................... 21

<!-- b000041 | contents | pages [2] -->
8 Sensitivity Analysis ............................................................................................................................. 22

<!-- b000042 | contents | pages [2] -->
8.1 Change in Demand ...................................................................................................................... 22

<!-- b000043 | contents | pages [2] -->
8.2 Renewable Energy Technologies ................................................................................................ 22

<!-- b000044 | contents | pages [2] -->
8.3 Water and Electricity Conservation Measures ............................................................................ 23

<!-- b000045 | contents | pages [2] -->
9 Strengths and Weaknesses ................................................................................................................. 23

<!-- b000046 | contents | pages [2] -->
9.1 Strengths ..................................................................................................................................... 23

<!-- b000047 | contents | pages [2] -->
9.2 Weakness ..................................................................................................................................... 23

<!-- b000048 | contents | pages [2] -->
References .............................................................................................................................................. 24

<!-- b000049 | contents | pages [2] -->
Article for Drought and Thirst magazine ........................................................................................... 25

<!-- b000050 | heading | pages [3] -->
1 Introduction

<!-- b000051 | heading | pages [3] -->
1.1 Background

<!-- b000052 | prose | pages [3] -->
"Please join me and the people of Utah, regardless of religion, in humbly praying for rain for one weekend," Utah Governor Spencer J.Cox said in a video plea on June 4, 2021.[1]

<!-- b000053 | prose | pages [3] -->
"The 'water shortage era' in the Western United States has officially arrived," Xinhua News Agency reported in Los Angeles on August 18.[2]

<!-- b000054 | prose | pages [3] -->
The Colorado River[3] originates in the Rocky Mountains of Colorado in the United States, with a length of more than 2,300 kilometers. Its main stream flows through Utah, Arizona, Nevada, California and Mexico, and finally empties into the Pacific Ocean. The Colorado River forms the largest water system in the Western United States -- known as the "lifeline of the Southwest" because it flows through vast arid and semi-arid areas.

<!-- b000055 | caption | pages [3] -->
Figure 1: U.S. Drought Monitor on February 15, 2022[4]

<!-- b000056 | prose | pages [3] -->
As can be seen from the Figure 1, the drought in the western United States has been severe. Actually, as early as the summer of 2021, it was reported[1] that lake Mead, the Hoover Dam that provides water to 25 million people in western States, was at historically low levels On June 9, the water level dropped to 1,071.57 feet, breaking the previous record low set in 2016. Climate change has reduced the amount of snow flowing into the Colorado River and its tributaries; Warmer temperatures are also making soil thirstier and increasing evaporation as rivers flow through arid areas of the western United States.

<!-- b000057 | prose | pages [3] -->
In the western part of the United States, in the Colorado River basin, two artificial lakes, the Lake Powell and Lake Mead, correspond to two dam (Glen Canyon and Hoover Dam) reservoirs. Water from the two dams is needed to meet the water and electricity demands of five U.S. states, Arizona (AZ), California (CA), Wyoming (WY), New Mexico (NM), and Colorado (CO), with extra water flowing into Mexico from the Colorado River into the Gulf of California.

<!-- b000058 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000059 | prose | pages [3] -->
The strained distribution of water affects competing interests in various regions. Through the

<!-- b000060 | prose | pages [4] -->
analysis and investigation of the background and negotiators’ guidance of the problem, the restate of the problem can be expressed as follows:

<!-- b000061 | prose | pages [4] -->
⚫Build a mathematical model to solve the problem of water allocation under the condition of fixed

<!-- b000062 | prose | pages [4] -->
supply and demand conditions.

<!-- b000063 | prose | pages [4] -->
✓Given the initial water level of the two lakes, figure out how much water should be drawn from

<!-- b000064 | prose | pages [4] -->
each lake to meet the water and electricity demands.

<!-- b000065 | prose | pages [4] -->
✓In the absence of additional water supply, and the demands are fixed, solve for the maximum

<!-- b000066 | prose | pages [4] -->
maintenance time that the demands can be met.

<!-- b000067 | prose | pages [4] -->
✓Figure out how much additional water must be supplied overtime to ensure that these fixed

<!-- b000068 | prose | pages [4] -->
demands are met.

<!-- b000069 | prose | pages [4] -->
⚫Establish a model to determine the allocation of water for general (Agricultural, Industrial,

<!-- b000070 | prose | pages [4] -->
Residential) usage and electricity production among five states, and describe the criteria for resolving competing interests.

<!-- b000071 | prose | pages [4] -->
⚫Based on the model, improve the solution in the case of water shortage, so that it can meet all the

<!-- b000072 | prose | pages [4] -->
water and electricity demands.

<!-- b000073 | prose | pages [4] -->
⚫Analyze the changes in model results according to the following situations:

<!-- b000074 | prose | pages [4] -->
✓As the demands for water and electricity change over time, population, agricultural, and

<!-- b000075 | prose | pages [4] -->
industrial change.

<!-- b000076 | prose | pages [4] -->
✓The initial value of renewable energy technologies increases.

<!-- b000077 | prose | pages [4] -->
✓Measures are taken to save water and electricity.

<!-- b000078 | prose | pages [4] -->
⚫Summarize the findings and prepare a one - to two-page article to submit to Drought and Thirst

<!-- b000079 | prose | pages [4] -->
magazine.

<!-- b000080 | heading | pages [4] -->
1.3 Our Work

<!-- b000081 | prose | pages [4] -->
The problem requires us to work out a reasonable allocation plan for water and electricity demands of three categories of objects (industrial, agricultural and residential) in five states, and for different environmental conditions, considering the needs of Mexico. Our main work is as follows:

<!-- b000082 | prose | pages [4] -->
1) In the case of a certain demand, the Water and Electricity Transportation Model is established by analyzing the transportation of water and electricity and the water transferred between two lakes. Figure out the daily supply of water for the two lakes, the maximum maintenance time without additional water, and the additional water needed to meet demands.

<!-- b000083 | prose | pages [4] -->
2) The Coordinated Development of multi-objective Programming Model is established by considering the water and electricity demands of industry, agriculture and residents from three perspectives of society, economy and environment. The distribution of water and electricity when water resource is sufficient and water resource is tight is analyzed respectively.

<!-- b000084 | prose | pages [4] -->
3) Based on the above two models, the Mexican Allocation Model is established to consider the distribution of Mexico's interests.

<!-- b000085 | prose | pages [4] -->
4) The sensitivity of the model was analyzed from the perspectives of demand and renewable Energy Technologies.

<!-- b000086 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000087 | prose | pages [5] -->
In order to build the mathematical model to solve the problems, we make the following supplementary assumptions on the basis of the problem, following a reasonable explanation for each

<!-- b000088 | heading | pages [5] -->
assumption

<!-- b000089 | prose | pages [5] -->
⚫ Lake Powell and Lake Mead are the reservoirs of Glen Canyon dam and Hoover Dam, respectively. These two lakes are artificial lakes and the distance between the reservoir and the dam is very close. Due to the theory of communicating vessels, the lake water height can be considered as the water height of the upstream of the dam, and the error can be ignored.

<!-- b000090 | prose | pages [5] -->
⚫ The dam will not overflow due to conditions such as a breach. The main trend of climate change is the decrease of precipitation and the increase of temperature, and water resources are strained, so the overflow situation is not considered.

<!-- b000091 | prose | pages [5] -->
⚫ The lowest water level for power generation is the lowest water level allowed by the reservoir. After a data search, we set the lowest water level at 3,490 feet for Lake Powell and 950 feet for Lake Mead.

<!-- b000092 | prose | pages [5] -->
⚫ The supply of electricity in the states is only hydroelectric. In order to simplify the model and reduce the burden of data search, only hydroelectric power is considered.

<!-- b000093 | prose | pages [5] -->
⚫ The water can be reused, and all the water that flows through the dam generates electricity. Based on resource reusability, this assumption is more realistic.

<!-- b000094 | prose | pages [5] -->
⚫ Consider the effects of rainfall, temperature changes, and river evaporation. Climate change has reduced the amount of snow flowing into the Colorado River and its tributaries; Warmer temperatures are also making soil thirstier and increasing evaporation as rivers flow through arid areas of the western United States. The consideration of evaporation is necessary and reasonable.

<!-- b000095 | prose | pages [5] -->
⚫ The water transferred from Lake Powell into Lake Mead and then supplied to users is deemed to belong to Lake Mead.

<!-- b000096 | prose | pages [5] -->
⚫ The supply of water depends on rivers. In practice, each region follows the "proximity principle" for water resources, that is, only the main stream or tributaries flowing through the region can be used for water. Electricity transportation is related to the geography of the five states.

<!-- b000097 | prose | pages [5] -->
⚫ Electrical energy is lost because of the thermal power generated by the resistance of the wire. Transporting electricity from the same dam causes states farther from the dam to generate more power and lose more than states closer to the dam. As the state Wyoming is far from the dam, it is necessary to consider the power loss.

<!-- b000098 | heading | pages [5] -->
3 Notations

<!-- b000099 | prose | pages [5] -->
The important symbols used in this article and their meanings are shown in Table 1. There are some variables that are not listed here and will be discussed in detail in each section.

<!-- b000100 | caption | pages [5] -->
Table 1: Important Symbols and Descriptions

<!-- b000101 | heading | pages [5] -->
Symbol

<!-- b000102 | prose | pages [5] -->
Description

<!-- b000103 | prose | pages [5] -->
l The height of the water level of a reservoir

<!-- b000104 | prose | pages [6] -->
v Volume of water in a reservoir

<!-- b000105 | prose | pages [6] -->
W Total volume of water supply suply

<!-- b000106 | prose | pages [6] -->
Volume of water supplied from Reservoir i to State W

<!-- b000107 | prose | pages [6] -->
j j = ( 1,2, ,5)

<!-- b000108 | prose | pages [6] -->
ij

<!-- b000109 | prose | pages [6] -->
W Volume of water lost through transport loss

<!-- b000110 | prose | pages [6] -->
Electricity demand (transferred to the volume of water) in D j j = w State ( 1,2, j

<!-- b000111 | prose | pages [6] -->
D

<!-- b000112 | prose | pages [6] -->
,5)

<!-- b000113 | furniture | pages [6] -->


<!-- b000114 | prose | pages [6] -->
j j = Water demand in State ( je 1,2, ,5)

<!-- b000115 | prose | pages [6] -->
Supply for m (water or electricity) from source i to k k = ( object

<!-- b000116 | prose | pages [6] -->
km ijx

<!-- b000117 | prose | pages [6] -->
1,2,3) (industrial, agricultural and j j = residential) of State ( 1,2, ,5)

<!-- b000118 | prose | pages [6] -->
Demand for m k k = ( 1,2,3) (water or electricity) of object (industrial, agricultural and residential) in

<!-- b000119 | prose | pages [6] -->
km D j

<!-- b000120 | prose | pages [6] -->
j j = State ( 1,2,

<!-- b000121 | heading | pages [6] -->
4 Model Preparation

<!-- b000122 | heading | pages [6] -->
4.1 Data Collection

<!-- b000123 | prose | pages [6] -->
,5)

<!-- b000124 | furniture | pages [6] -->


<!-- b000125 | prose | pages [6] -->
The problem doesn't give us data, so we need to collect data to build a model. To analyze the problem, we need to collect data on two lakes and dams, as well as the water and electricity demands of agriculture, industry and residential use in five states. After the data is collected, certain processing and analysis are carried out to prepare for the subsequent model establishment.

<!-- b000126 | prose | pages [6] -->
The official websites of the two lakes and dams provide us with a lot of data about the dams. Detailed data sources are shown in the Table 2 below. (Additional data sources are included in the Reference.)

<!-- b000127 | caption | pages [6] -->
Table 2: Partial Data Sources

<!-- b000128 | prose | pages [6] -->
Database Names Database Websites

<!-- b000129 | prose | pages [6] -->
http://lakepowell.water-data.com/ Lake Powell

<!-- b000130 | prose | pages [6] -->
http://lakemead.water-data.com/ Lake Mead

<!-- b000131 | prose | pages [6] -->
https://www.eia.gov/electricity/state/ Electricity Consumption

<!-- b000132 | heading | pages [6] -->
4.2 Relationship between Water Level and Storage Volume

<!-- b000133 | prose | pages [6] -->
Lake Powell and Lake Mead are the reservoirs of Glen Canyon Dam and Hoover Dam respectively. The higher the elevation of the lake, the larger the content of the reservoir. After analyzing and studying the water level of the two lakes in the past 12 months (data sources are shown in the Table 1), we

<!-- b000134 | prose | pages [7] -->
conclude that there is a linear correlation between the elevation and content of the lakes.

<!-- b000135 | prose | pages [7] -->
Therefore, we perform polynomial fitting analysis on elevation and content, and the steps are as follows:

<!-- b000136 | prose | pages [7] -->
Step1: Take a set of data points, including m, as sample points

<!-- b000137 | prose | pages [7] -->
{( , l v )( , l v ) 1 1 2 2

<!-- b000138 | prose | pages [7] -->
= where ( il i 1,2, , m )

<!-- b000139 | prose | pages [7] -->
( , ) l v ( , l v )} (1) i i m m

<!-- b000140 | prose | pages [7] -->
represents the height of the water level of a reservoir corresponding to the sample = point ( i i 1,2, , m ) = iv i ( 1,2, , m ) , namely the elevation of the lake; a reservoir, namely the content of the lake.

<!-- b000141 | prose | pages [7] -->
Step2: Use polynomial for curve fitting

<!-- b000142 | prose | pages [7] -->
−

<!-- b000143 | prose | pages [7] -->
= + +

<!-- b000144 | prose | pages [7] -->
n n 1 ˆ

<!-- b000145 | prose | pages [7] -->
v a l a l

<!-- b000146 | prose | pages [7] -->
0 1

<!-- b000147 | prose | pages [7] -->
represents the volume of water in

<!-- b000148 | prose | pages [7] -->
−

<!-- b000149 | prose | pages [7] -->
+ + +

<!-- b000150 | prose | pages [7] -->
n 2

<!-- b000151 | prose | pages [7] -->
a l a l a l a

<!-- b000152 | prose | pages [7] -->
(2) −

<!-- b000153 | prose | pages [7] -->
2 2

<!-- b000154 | prose | pages [7] -->
n

<!-- b000155 | prose | pages [7] -->
1

<!-- b000156 | prose | pages [7] -->
n

<!-- b000157 | prose | pages [7] -->
th th n degree polynomial; ˆv is the predicted value. na represents fitting coefficient, stands for where

<!-- b000158 | prose | pages [7] -->
Step3: Calculate the sum of squares of residuals

<!-- b000159 | prose | pages [7] -->
m

<!-- b000160 | prose | pages [7] -->


<!-- b000161 | prose | pages [7] -->


<!-- b000162 | prose | pages [7] -->
= =

<!-- b000163 | prose | pages [7] -->
i

<!-- b000164 | prose | pages [7] -->
1

<!-- b000165 | prose | pages [7] -->
−

<!-- b000166 | prose | pages [7] -->
2

<!-- b000167 | prose | pages [7] -->
ˆ( ˆ(

<!-- b000168 | prose | pages [7] -->
v v v

<!-- b000169 | prose | pages [7] -->
)

<!-- b000170 | prose | pages [7] -->
(3)

<!-- b000171 | prose | pages [7] -->
i i i

<!-- b000172 | prose | pages [7] -->
We use MATLAB for polynomial fitting of elevation and content, and the results are as follows

<!-- b000173 | caption | pages [7] -->
Figure 2: The fitting curves of Lake Powell ( Left ) and Lake Mead ( Right )

<!-- b000174 | prose | pages [7] -->
After many times of curve fitting, we find that the fitting effect of quadratic polynomial is more ideal. As can be seen from Figure 2, sample points of Lake Powell and Lake Mead are relatively close to the fitting curve. The relationship between water level and volume of the two reservoirs is as follows

<!-- b000175 | prose | pages [7] -->
= −

<!-- b000176 | prose | pages [7] -->
2

<!-- b000177 | prose | pages [7] -->
+

<!-- b000178 | prose | pages [7] -->
6 9

<!-- b000179 | prose | pages [7] -->
1.5157*10

<!-- b000180 | prose | pages [7] -->
v

<!-- b000181 | prose | pages [7] -->
224.26

<!-- b000182 | prose | pages [7] -->
l

<!-- b000183 | prose | pages [7] -->
powell

<!-- b000184 | prose | pages [7] -->
= −

<!-- b000185 | prose | pages [7] -->
2

<!-- b000186 | prose | pages [7] -->
l

<!-- b000187 | prose | pages [7] -->
2.5622*10

<!-- b000188 | prose | pages [7] -->
(4)

<!-- b000189 | prose | pages [7] -->
+

<!-- b000190 | prose | pages [7] -->
5 8

<!-- b000191 | prose | pages [7] -->
6.719*10

<!-- b000192 | prose | pages [7] -->
v

<!-- b000193 | prose | pages [7] -->
338.64

<!-- b000194 | prose | pages [7] -->
l

<!-- b000195 | prose | pages [7] -->
mead

<!-- b000196 | prose | pages [7] -->
l

<!-- b000197 | prose | pages [7] -->
3.4155*10

<!-- b000198 | prose | pages [7] -->
We verify the function by comparing the predicted value with the actual value. According to Wikipedia, Lake Powell[5] is 3,700 feet above sea level and has an active capacity of 20,876,000 acre-feet with a fitting value of 24,229,400 acre-feet; Lake Mead[6] has an elevation of 1221.4 feet and an effective capacity of 26,120,000 acre-feet with a fitting value of 26,080,000 acre-feet. From the numerical point of view, the fitting effect is ideal.

<!-- b000199 | heading | pages [8] -->
5 Model I: Water and Electricity Transportation Model

<!-- b000200 | heading | pages [8] -->
5.1 Basic Ideas

<!-- b000201 | prose | pages [8] -->
In the basin of the Colorado River, Lake Powell and Lake Mead are two water clusters. The two lakes are at higher elevations and water can flows from them to the surrounding areas. Additionally, Lake Mead has a higher elevation than Lake Powell. So the water flows from the Glen Canyon Dam (Lake Powell) to the Hoover Dam (Lake Mead) and eventually to the Gulf of California.

<!-- b000202 | prose | pages [8] -->
The geographical map is shown in Figure 3.

<!-- b000203 | caption | pages [8] -->
Figure 3: Geographic map[3]

<!-- b000204 | prose | pages [8] -->
Demands includes water demand and electricity demand, which includes agriculture, industry and residents in five states.

<!-- b000205 | prose | pages [8] -->
1. Water supply: It is assumed that each region draws water from the river that flows through it, and this water can be traced back to Lake Powell or Lake Mead. Among them, part of the water of Lake Powell will be supplied to users after flowing into Lake Mead, which is regarded as belonging to Lake Mead. In the process of water transportation, the hydraulic loss caused by evaporation is mainly considered.

<!-- b000206 | prose | pages [8] -->
2. Electricity supply: hydroelectric power is to convert the potential energy of water into mechanical energy and then into electrical energy. Similarly, we can also transform the loss of electric power in the transmission process into the loss of water potential energy, thus producing constraints on reservoir stock.

<!-- b000207 | prose | pages [8] -->
The problem is thus simplified to two lakes distributing water resources to the five continents. The distribution of the three industries (agriculture, industry and resident) will be discussed in detail in the Section 6.

<!-- b000208 | prose | pages [8] -->
In the case of water demand and electricity demand are certain, we can make a reasonable allocation of water resources through Transportation Model.

<!-- b000209 | heading | pages [9] -->
5.2 Establishment of Transportation Model

<!-- b000210 | heading | pages [9] -->
5.2.1 Objective Function

<!-- b000211 | prose | pages [9] -->
In order to make full use of water resources, we hope that the water supply from the two dams will meet the water and electricity demands of each state while providing as little water as possible

<!-- b000212 | prose | pages [9] -->
=

<!-- b000213 | prose | pages [9] -->
min W W suply

<!-- b000214 | prose | pages [9] -->
W

<!-- b000215 | prose | pages [9] -->
2 5

<!-- b000216 | prose | pages [9] -->
= + +

<!-- b000217 | prose | pages [9] -->
W W

<!-- b000218 | prose | pages [9] -->
(5)

<!-- b000219 | prose | pages [9] -->
1 1 2 ij

<!-- b000220 | prose | pages [9] -->
= =

<!-- b000221 | prose | pages [9] -->
i 1 j 1

<!-- b000222 | prose | pages [9] -->
W is the water supply from the Glen Canyon represents the total volume of water supply, where suply 1

<!-- b000223 | prose | pages [9] -->
W is the water supply from the Hoover dam. dam, and 2

<!-- b000224 | prose | pages [9] -->
i i = j j = Reservoir ( to State ( 1,2, 1,2) ,5)

<!-- b000225 | prose | pages [9] -->
W means the volume of water supplied from ij

<!-- b000226 | prose | pages [9] -->
. If there is no corresponding river flowing through, then W = 0 . ij

<!-- b000227 | prose | pages [9] -->
W For a lake, water supply can be divided into two types: water supplied directly without the dam , iup

<!-- b000228 | prose | pages [9] -->
i = represents the Glen Canyon dam, W 1 and water supplied through the dam . ( idown Hoover dam).

<!-- b000229 | prose | pages [9] -->
i = 2 represents the

<!-- b000230 | prose | pages [9] -->
Considering that some water will flow to Lake Mead after Glen Canyon dam, we set the volume of  , where  is a proportional parameter. Additionally, it is W this part of transferred water as 1down

<!-- b000231 | prose | pages [9] -->
W after being transferred. assumed that the transferred water is included in Lake Mead's water supply Thus, the water supply can be expressed as follows

<!-- b000232 | prose | pages [9] -->
= + −

<!-- b000233 | prose | pages [9] -->


<!-- b000234 | prose | pages [9] -->
W W

<!-- b000235 | prose | pages [9] -->
(1

<!-- b000236 | prose | pages [9] -->
suply

<!-- b000237 | prose | pages [9] -->
1

<!-- b000238 | prose | pages [9] -->
up

<!-- b000239 | prose | pages [9] -->
2

<!-- b000240 | prose | pages [9] -->
 = +

<!-- b000241 | prose | pages [9] -->
(

<!-- b000242 | prose | pages [9] -->
W W

<!-- b000243 | prose | pages [9] -->
iup

<!-- b000244 | prose | pages [9] -->
=

<!-- b000245 | prose | pages [9] -->
i

<!-- b000246 | prose | pages [9] -->
1

<!-- b000247 | prose | pages [9] -->
W

<!-- b000248 | prose | pages [9] -->
2

<!-- b000249 | prose | pages [9] -->
+ +

<!-- b000250 | prose | pages [9] -->
) )

<!-- b000251 | prose | pages [9] -->
W W W

<!-- b000252 | prose | pages [9] -->
1

<!-- b000253 | prose | pages [9] -->
down

<!-- b000254 | prose | pages [9] -->
2

<!-- b000255 | prose | pages [9] -->
up

<!-- b000256 | prose | pages [9] -->
2

<!-- b000257 | prose | pages [9] -->
down

<!-- b000258 | prose | pages [9] -->
(6)

<!-- b000259 | prose | pages [9] -->
−

<!-- b000260 | prose | pages [9] -->


<!-- b000261 | prose | pages [9] -->
)

<!-- b000262 | prose | pages [9] -->
W

<!-- b000263 | prose | pages [9] -->
idown

<!-- b000264 | prose | pages [9] -->
1

<!-- b000265 | prose | pages [9] -->
down

<!-- b000266 | prose | pages [9] -->
includes the water provided to users by lake i after the dam, which is constrained For dam i , idown D and electricity demand D , namely by users' water demand (transferred to the volume of water)

<!-- b000267 | prose | pages [9] -->


<!-- b000268 | prose | pages [9] -->
e w

<!-- b000269 | prose | pages [9] -->
+ max{ W idown D D } (7) e w

<!-- b000270 | prose | pages [9] -->
The relationship between water and electricity conversion and the loss of water and electricity during transportation will be discussed in detail in Section 5.2.3.

<!-- b000271 | heading | pages [9] -->
5.2.2 Supply constraints

<!-- b000272 | prose | pages [9] -->
The water supply must not exceed the minimum level of the reservoir, otherwise there will be no electricity supply. It is assumed that the lowest water level is the minimum content of reservoir.

<!-- b000273 | prose | pages [9] -->
Therefore, the water supply by Glen Canyon dam

<!-- b000274 | prose | pages [9] -->
W 1   Q (8) G

<!-- b000275 | prose | pages [9] -->
Q represents the reservoir W represents the water supplied by the Glen Canyon dam, and where, 1 content of the Glen Canyon dam.

<!-- b000276 | prose | pages [9] -->
For Hoover Dam, its water supply

<!-- b000277 | prose | pages [9] -->
G

<!-- b000278 | prose | pages [10] -->
 W Q 2 H + +  W (9) 1 down

<!-- b000279 | prose | pages [10] -->
W represents the water supplied by the Hoover Dam, and where, 2  Q represents the reservoir content of G is the water transferred form Glen Canyon dam to Hoover Dam.  is a W the Hoover Dam.

<!-- b000280 | prose | pages [10] -->
1down parameter, which indicating the loss of water during the transportation (the details are discussed Section 5.2.3)

<!-- b000281 | caption | pages [10] -->
Figure 4: Schematic diagram

<!-- b000282 | heading | pages [10] -->
5.2.3 Demand constraints

<!-- b000283 | prose | pages [10] -->
Demands are divided into water demand and electricity demand. Our solution needs to meet both needs on five continents.

<!-- b000284 | prose | pages [10] -->
⚫ Electricity demand

<!-- b000285 | prose | pages [10] -->
When the volume of water in the reservoir is small, the corresponding water flow will decrease. When the water level is low enough, it can even shut down power generation.

<!-- b000286 | prose | pages [10] -->
For hydraulic power generation, the formula[7] of translational power of turbines is as follows

<!-- b000287 | prose | pages [10] -->
= =  E f W ( ) ( + +    )( V g h t ) (10)

<!-- b000288 | prose | pages [10] -->
where E is electric energy and W is the volume of the water, which means the relationship between Potential energy and electric energy of water.  +  is the coefficient of efficiency (a unitless, scalar coefficient, ranging from 0 for completely inefficient to 1 for completely efficient).  represents the function of the renewable energy technologies enhancement.  is the density of water. V is the  is the change in height. t  represents the volumetric flow rate. g is acceleration due to gravity. h working time.

<!-- b000289 | prose | pages [10] -->
The generation height difference is the current water level minus the lowest water level.

<!-- b000290 | prose | pages [10] -->
 =

<!-- b000291 | prose | pages [10] -->
h P

<!-- b000292 | prose | pages [10] -->
1

<!-- b000293 | prose | pages [10] -->
 =

<!-- b000294 | prose | pages [10] -->
h

<!-- b000295 | prose | pages [10] -->
2

<!-- b000296 | prose | pages [10] -->
P where P is water level in Lake Powell,

<!-- b000297 | prose | pages [10] -->
− −

<!-- b000298 | prose | pages [10] -->
P

<!-- b000299 | prose | pages [10] -->
min

<!-- b000300 | prose | pages [10] -->
(11) −

<!-- b000301 | prose | pages [10] -->
M M M

<!-- b000302 | prose | pages [10] -->
min

<!-- b000303 | prose | pages [10] -->
is the lowest generating water level of the Glen Canyon dam, min

<!-- b000304 | prose | pages [11] -->
M M is water level in Lake Mead, and is lowest generating water level of the Hoover dam. min

<!-- b000305 | prose | pages [11] -->
The electrical energy will be lost during transmission due to the resistance of the wire

<!-- b000306 | prose | pages [11] -->
=

<!-- b000307 | prose | pages [11] -->
E

<!-- b000308 | prose | pages [11] -->
loss

<!-- b000309 | prose | pages [11] -->
ij

<!-- b000310 | prose | pages [11] -->
 

<!-- b000311 | prose | pages [11] -->
2 2

<!-- b000312 | prose | pages [11] -->
I I

<!-- b000313 | prose | pages [11] -->
'

<!-- b000314 | prose | pages [11] -->
L t

<!-- b000315 | prose | pages [11] -->
ij i

<!-- b000316 | prose | pages [11] -->
(12)

<!-- b000317 | prose | pages [11] -->
s

<!-- b000318 | prose | pages [11] -->
Thus, additional water supply is available because of the loss of electrical energy, which is denoted W . For electricity, supply needs to meet demand, expressed as follows by eloss

<!-- b000319 | prose | pages [11] -->
2

<!-- b000320 | prose | pages [11] -->
 −

<!-- b000321 | prose | pages [11] -->
W down ij

<!-- b000322 | prose | pages [11] -->
=

<!-- b000323 | prose | pages [11] -->
i 1

<!-- b000324 | prose | pages [11] -->
W

<!-- b000325 | prose | pages [11] -->
2 2

<!-- b000326 | prose | pages [11] -->
  

<!-- b000327 | prose | pages [11] -->
W D

<!-- b000328 | prose | pages [11] -->
(13)

<!-- b000329 | prose | pages [11] -->
eloss e ij j

<!-- b000330 | prose | pages [11] -->
= =

<!-- b000331 | prose | pages [11] -->
i i 1 1

<!-- b000332 | prose | pages [11] -->
can be obtained by combining the Formula (10,12). where eloss

<!-- b000333 | prose | pages [11] -->
⚫ Water demand

<!-- b000334 | prose | pages [11] -->
The transportation of water depends mainly on river systems. Rivers are largely exposed to sunlight and are greatly affected by evaporation. Evaporation is greatly affected by temperature. Therefore, the loss of water during transportation can be expressed as follows

<!-- b000335 | prose | pages [11] -->
W wloss

<!-- b000336 | prose | pages [11] -->
ij

<!-- b000337 | prose | pages [11] -->


<!-- b000338 | prose | pages [11] -->
Td

<!-- b000339 | prose | pages [11] -->
= =  (14)

<!-- b000340 | prose | pages [11] -->
W

<!-- b000341 | prose | pages [11] -->
ij

<!-- b000342 | prose | pages [11] -->
ij

<!-- b000343 | prose | pages [11] -->


<!-- b000344 | prose | pages [11] -->
Td

<!-- b000345 | prose | pages [11] -->
j j =

<!-- b000346 | prose | pages [11] -->


<!-- b000347 | prose | pages [11] -->
W represents the volume of water supplied from Reservoiri to State ( where ij 1,2, ,5) , and

<!-- b000348 | prose | pages [11] -->
is

<!-- b000349 | prose | pages [11] -->
ij

<!-- b000350 | prose | pages [11] -->
the evaporation coefficient affected by temperature.  and  are parameters. T is the temperature.

<!-- b000351 | prose | pages [11] -->
the distance from Reservoiri to State j .

<!-- b000352 | prose | pages [11] -->
d is ij

<!-- b000353 | prose | pages [11] -->
It is assumed that the water will still be available to users after the electricity is generated. Therefore, the transport loss of water and electricity should be considered comprehensively when considering the provision of water

<!-- b000354 | prose | pages [11] -->
= W W loss ij + (15) W wloss eloss ij ij

<!-- b000355 | prose | pages [11] -->
For water, supply needs to meet demand, expressed as follows

<!-- b000356 | prose | pages [11] -->
2

<!-- b000357 | prose | pages [11] -->
 −

<!-- b000358 | prose | pages [11] -->
W down ij

<!-- b000359 | prose | pages [11] -->
=

<!-- b000360 | prose | pages [11] -->
i 1

<!-- b000361 | heading | pages [11] -->
5.2.4 The model summary

<!-- b000362 | prose | pages [11] -->
2 2

<!-- b000363 | prose | pages [11] -->
  

<!-- b000364 | prose | pages [11] -->
W D

<!-- b000365 | prose | pages [11] -->
(16)

<!-- b000366 | prose | pages [11] -->
loss w ij j

<!-- b000367 | prose | pages [11] -->
= =

<!-- b000368 | prose | pages [11] -->
i i 1 1

<!-- b000369 | prose | pages [11] -->
By summarizing the objective function and constraint equation above, we can get the following water and electricity transportation model.

<!-- b000370 | prose | pages [11] -->
2 2 5

<!-- b000371 | prose | pages [11] -->
=

<!-- b000372 | prose | pages [11] -->
W

<!-- b000373 | prose | pages [11] -->
min

<!-- b000374 | prose | pages [11] -->
suply

<!-- b000375 | prose | pages [11] -->
W

<!-- b000376 | prose | pages [11] -->
(17)

<!-- b000377 | prose | pages [11] -->
ij

<!-- b000378 | prose | pages [11] -->
= = =

<!-- b000379 | prose | pages [11] -->
i i 1 j 1

<!-- b000380 | prose | pages [11] -->
st. . st. .

<!-- b000381 | prose | pages [12] -->


<!-- b000382 | prose | pages [12] -->
2

<!-- b000383 | prose | pages [12] -->


<!-- b000384 | prose | pages [12] -->
=

<!-- b000385 | prose | pages [12] -->
W W

<!-- b000386 | prose | pages [12] -->
(

<!-- b000387 | prose | pages [12] -->


<!-- b000388 | prose | pages [12] -->
suply

<!-- b000389 | prose | pages [12] -->


<!-- b000390 | prose | pages [12] -->
=

<!-- b000391 | prose | pages [12] -->
i

<!-- b000392 | prose | pages [12] -->
1

<!-- b000393 | prose | pages [12] -->
 

<!-- b000394 | prose | pages [12] -->
W

<!-- b000395 | prose | pages [12] -->
max{

<!-- b000396 | prose | pages [12] -->
idown

<!-- b000397 | prose | pages [12] -->
 

<!-- b000398 | prose | pages [12] -->
W Q

<!-- b000399 | prose | pages [12] -->


<!-- b000400 | prose | pages [12] -->
1

<!-- b000401 | prose | pages [12] -->
G

<!-- b000402 | prose | pages [12] -->
  +

<!-- b000403 | prose | pages [12] -->


<!-- b000404 | prose | pages [12] -->
W Q W

<!-- b000405 | prose | pages [12] -->


<!-- b000406 | prose | pages [12] -->
2

<!-- b000407 | prose | pages [12] -->
H

<!-- b000408 | prose | pages [12] -->
2 2

<!-- b000409 | prose | pages [12] -->


<!-- b000410 | prose | pages [12] -->
 

<!-- b000411 | prose | pages [12] -->
−

<!-- b000412 | prose | pages [12] -->
W

<!-- b000413 | prose | pages [12] -->


<!-- b000414 | prose | pages [12] -->
down

<!-- b000415 | prose | pages [12] -->
ij

<!-- b000416 | prose | pages [12] -->
= =

<!-- b000417 | prose | pages [12] -->
i

<!-- b000418 | prose | pages [12] -->
1

<!-- b000419 | prose | pages [12] -->
i

<!-- b000420 | prose | pages [12] -->
1

<!-- b000421 | prose | pages [12] -->


<!-- b000422 | prose | pages [12] -->
2 2

<!-- b000423 | prose | pages [12] -->


<!-- b000424 | prose | pages [12] -->
 

<!-- b000425 | prose | pages [12] -->
−

<!-- b000426 | prose | pages [12] -->
W

<!-- b000427 | prose | pages [12] -->


<!-- b000428 | prose | pages [12] -->
down

<!-- b000429 | prose | pages [12] -->
ij

<!-- b000430 | prose | pages [12] -->
= =

<!-- b000431 | prose | pages [12] -->
i

<!-- b000432 | prose | pages [12] -->
1

<!-- b000433 | prose | pages [12] -->
i

<!-- b000434 | prose | pages [12] -->
1

<!-- b000435 | prose | pages [12] -->
 

<!-- b000436 | prose | pages [12] -->
W

<!-- b000437 | prose | pages [12] -->
0

<!-- b000438 | prose | pages [12] -->


<!-- b000439 | prose | pages [12] -->
ij

<!-- b000440 | prose | pages [12] -->
+ −

<!-- b000441 | prose | pages [12] -->


<!-- b000442 | prose | pages [12] -->
W

<!-- b000443 | prose | pages [12] -->
)

<!-- b000444 | prose | pages [12] -->
W

<!-- b000445 | prose | pages [12] -->
iup iup idown

<!-- b000446 | prose | pages [12] -->
1

<!-- b000447 | prose | pages [12] -->
down

<!-- b000448 | prose | pages [12] -->
+

<!-- b000449 | prose | pages [12] -->
D D D

<!-- b000450 | prose | pages [12] -->
}

<!-- b000451 | prose | pages [12] -->
e e w

<!-- b000452 | prose | pages [12] -->
1 1

<!-- b000453 | prose | pages [12] -->
down

<!-- b000454 | prose | pages [12] -->
(18)

<!-- b000455 | prose | pages [12] -->


<!-- b000456 | prose | pages [12] -->
W W D

<!-- b000457 | prose | pages [12] -->
eloss e

<!-- b000458 | prose | pages [12] -->
ij j

<!-- b000459 | prose | pages [12] -->


<!-- b000460 | prose | pages [12] -->
W W D

<!-- b000461 | prose | pages [12] -->
loss w

<!-- b000462 | prose | pages [12] -->
ij j

<!-- b000463 | prose | pages [12] -->
See the Formula (6-16) for a symbolic explanation.

<!-- b000464 | heading | pages [12] -->
5.3 Maintenance Time Calculation Algorithm

<!-- b000465 | prose | pages [12] -->
In order to solve the maximum maintenance time without additional water, we designed an algorithm to calculate the maintenance time.

<!-- b000466 | prose | pages [12] -->
The idea of this algorithm is to repeatedly iterate Model One to solve how long the water in two reservoirs can last without considering the external water supply.

<!-- b000467 | prose | pages [12] -->
The pseudo-code for the algorithm is as follows:

<!-- b000468 | heading | pages [12] -->
Algorithm: Maintenance Time Calculation Algorithm

<!-- b000469 | prose | pages [12] -->
P M j , demand, n←0 W i [ ][ ] Input: P , M , , , min min

<!-- b000470 | prose | pages [12] -->
Output: n

<!-- b000471 | prose | pages [12] -->
1  /*calculate the height and volume of water in the reservoirs base based

<!-- b000472 | prose | pages [12] -->
2  on the fitting function*/

<!-- b000473 | prose | pages [12] -->
P M

<!-- b000474 | heading | pages [12] -->
3  while P ≥

<!-- b000475 | prose | pages [12] -->
or M ≥ do min min

<!-- b000476 | prose | pages [12] -->
4 n ⟵n + 1;

<!-- b000477 | prose | pages [12] -->
5    cost ⟵ 0;

<!-- b000478 | heading | pages [12] -->
6 for i←0 to 1 do

<!-- b000479 | heading | pages [12] -->
7        for j←0 to 4 do

<!-- b000480 | prose | pages [12] -->
if demand> 0 then 8

<!-- b000481 | prose | pages [12] -->
j ∗𝛼 + E[i][j]∗𝛽; W i [ ][ ] cost ← cost + 9

<!-- b000482 | prose | pages [12] -->
j ∗(1 −𝛼) −E[i][j]∗(1 −𝛽); W i [ ][ ] demand ← demand− 10

<!-- b000483 | heading | pages [12] -->
11       end

<!-- b000484 | heading | pages [12] -->
12    end

<!-- b000485 | heading | pages [12] -->
13    if cost = min{cost} then

<!-- b000486 | prose | pages [13] -->
P ←P which is calculated based on the volume 14

<!-- b000487 | prose | pages [13] -->
M M ← which is calculated based on the volume; 15 min

<!-- b000488 | heading | pages [13] -->
16  end

<!-- b000489 | prose | pages [13] -->
The parameters to be input are: the initial water level heights P and M of the two reservoirs, and P M the lowest power level heights and . W is a matrix, and if there is no viable waterway from min min W i [ ][ ] j is initialized to 0. Demand D. The number of days n persisted is reservoir i to state j , then initialized to 0.

<!-- b000490 | prose | pages [13] -->
The parameters in the model are: calculated waterway transport loss α, calculated circuit transmission loss β, W matrix element represents the amount of water transported from reservoir i to state j, similarly, E matrix element codes the amount of electricity generated from reservoir i to state j .

<!-- b000491 | prose | pages [13] -->
Solution and output of the model: According to Model One, the reservoir water consumption required to meet the demand and guarantee the minimum loss can be obtained each time. The corresponding water level of the reservoir is calculated according to the fitting curve. If the water level of both reservoirs is lower than the lowest power generation water level, it indicates that the reservoirs can no longer provide electricity, that is, they can no longer meet the demand. The algorithm exits, and the number of days n is output.

<!-- b000492 | heading | pages [13] -->
5.4 Calculation Results

<!-- b000493 | heading | pages [13] -->
5.4.1 The water drawn from each lake

<!-- b000494 | prose | pages [13] -->
= P 3600 feet We assign values to the initial water levels of Lake Powell and Lake Mead.

<!-- b000495 | prose | pages [13] -->
and = M 1210 feet .Based on past data, we assume that water demand is 43,411 million gallons and electricity demand is 1,073 gigawatt hours.

<!-- b000496 | prose | pages [13] -->
We analyzed the problem on a daily basis. Using the model, we get a total water supply of 59,467 million gallons. The water should be drown from Lake Mead: 41,602 million gallons, The water should be drown from Lake Powell: 17,865 million gallons.

<!-- b000497 | prose | pages [13] -->
After a day of use, the water level of the two lakes changed by 0.45 feet and 1.55feet respectively. The results are reasonable.

<!-- b000498 | heading | pages [13] -->
5.4.2 Maintenance time

<!-- b000499 | prose | pages [13] -->
In the absence of additional water supplies (e.g. rainfall, etc.), water levels will decrease over time. When the water level drops to the lowest generating level, the reservoir can no longer provide electricity, that is, it cannot meet the demand. The maximum maintenance time is from the initial water level to the lowest water level.

<!-- b000500 | prose | pages [13] -->
On the basis of the previous result, combined with Model One and Maintenance time Calculation algorithm, the solution is obtained as 63 days.

<!-- b000501 | heading | pages [13] -->
5.4.3 Additional water

<!-- b000502 | prose | pages [13] -->
Additional water is needed to keep the supply system going when it reaches a critical state where demand cannot be met. At this point, the demand is certain, and the water in the reservoir is a constant value, equivalent to the supply of water is the additional water, so there is little difference in the results. The difference is that the model is based on time lines, and the actual temperature we consider will lead to different evaporation losses, so the actual amount of additional water that needs to be replenished will

<!-- b000503 | prose | pages [14] -->
also be different. The calculation results are shown in the figure below:

<!-- b000504 | caption | pages [14] -->
Figure 5: The result of additional water

<!-- b000505 | prose | pages [14] -->
The amount of water that needs to be replenished is positively correlated with temperature, and the higher the temperature, the higher the loss, and the more additional water needs to be replenished.

<!-- b000506 | heading | pages [14] -->
6 Model II: Coordinated Development of Multi-objective

<!-- b000507 | heading | pages [14] -->
Programming Model

<!-- b000508 | prose | pages [14] -->
Model Two is a further improvement on Model One. In model One, we only distribute the water supply and electricity supply among each state. In Model Two, we take into account the proportion of water consumption by industry, agriculture and residents.

<!-- b000509 | heading | pages [14] -->
6.1 The Establishment of Multi-objective Programming Model

<!-- b000510 | heading | pages [14] -->
6.1.1 Objective function

<!-- b000511 | prose | pages [14] -->
The proportion of water and electricity used by industry, agriculture and residents will ultimately have social, economic and environmental implications.[8]

<!-- b000512 | prose | pages [14] -->
Our goal is to harmonize social, economic and environmental development. The social, economic and environmental conditions correspond to the situation before, during and after the use of water. Electricity before and during use corresponds to this society and economy respectively.

<!-- b000513 | prose | pages [14] -->
➢ Social effect refers to the lack of water (or electricity) when the demand is not met. In other words, the social benefit refers to the negative effect caused by the lack of water (or electricity). When there is no water shortage, social benefits are not considered in the objective function.

<!-- b000514 | prose | pages [14] -->
➢ Economic effect refers to the industrial output from water (or electricity). The supply for industry, agriculture and residents in an area affects the economic situation of the area to varying degrees.

<!-- b000515 | prose | pages [14] -->
➢ Environmental effect refers to the amount of pollutants that water brings with it after use. From the perspective of environmental sustainability, we want the total amount of pollutants to be as small as possible.

<!-- b000516 | prose | pages [15] -->
= F opt f x [ ( ), 1

<!-- b000517 | prose | pages [15] -->
x k = kf ( )( 1,2,3)

<!-- b000518 | prose | pages [15] -->
f ( ), x f x ( )] (19) 2 3

<!-- b000519 | prose | pages [15] -->
correspond to social, economic and environmental implications respectively. where,

<!-- b000520 | prose | pages [15] -->
Water supply and demand affect all three effects simultaneously, whereas electricity supply and demand affect only the social effect and economic effect.

<!-- b000521 | prose | pages [15] -->
f x 1( ) ⚫ Social effect

<!-- b000522 | prose | pages [15] -->
i = i = There are three main sources of water supply: Glen Canyon dam ( i = , Hoover Dam ( 1) 2) and i = . There are two sources of electricity supply: Glen Canyon dam ( rainfall ( 3) i = ( 2) .

<!-- b000523 | prose | pages [15] -->
1) and Hoover Dam

<!-- b000524 | prose | pages [15] -->
When the supply cannot meet the demand, the water (or electricity) shortage is the quantity demanded minus the supply. We want the social effect to be as small as possible.

<!-- b000525 | prose | pages [15] -->
I m

<!-- b000526 | prose | pages [15] -->
( ) 2 2 3 5

<!-- b000527 | prose | pages [15] -->
 = −

<!-- b000528 | prose | pages [15] -->
max

<!-- b000529 | prose | pages [15] -->
f x

<!-- b000530 | prose | pages [15] -->
( ) min 1

<!-- b000531 | prose | pages [15] -->
m

<!-- b000532 | prose | pages [15] -->
m = 1 km

<!-- b000533 | prose | pages [15] -->
 −

<!-- b000534 | prose | pages [15] -->
km km

<!-- b000535 | prose | pages [15] -->
[

<!-- b000536 | prose | pages [15] -->
D x

<!-- b000537 | prose | pages [15] -->
]

<!-- b000538 | prose | pages [15] -->
(20)

<!-- b000539 | prose | pages [15] -->
j ij

<!-- b000540 | prose | pages [15] -->
= = = = =

<!-- b000541 | prose | pages [15] -->
1 1

<!-- b000542 | prose | pages [15] -->
k k

<!-- b000543 | prose | pages [15] -->
1

<!-- b000544 | prose | pages [15] -->
j

<!-- b000545 | prose | pages [15] -->
1

<!-- b000546 | prose | pages [15] -->
i

<!-- b000547 | prose | pages [15] -->
1

<!-- b000548 | prose | pages [15] -->
k = m = 2 1 ) of object k (industrial or electricity where is the demand for m (water D j

<!-- b000549 | prose | pages [15] -->
k = k = ) in State (

<!-- b000550 | prose | pages [15] -->
,

<!-- b000551 | prose | pages [15] -->
m = or j j = 2 3 agricultural and residential

<!-- b000552 | prose | pages [15] -->
m = k = 2 1 ) to object k (industrial

<!-- b000553 | prose | pages [15] -->
1 km 1,2, ,5) , is the supply for m (water ijx

<!-- b000554 | prose | pages [15] -->
k = k = 2 3 , agricultural electricity j j = ( 1,2, ,5) .

<!-- b000555 | prose | pages [15] -->
f 2( ) x ⚫ Economic effect

<!-- b000556 | prose | pages [15] -->
and residential ) of State

<!-- b000557 | prose | pages [15] -->
The economy mainly includes the value of water (or electricity) brought by water resources, and the benefits brought by the utilization of water (or electricity).

<!-- b000558 | prose | pages [15] -->
The value of water (or electricity) brought by water resources is directly reflected in the charging system of hydropower, which is expressed by the charging coefficient c . The benefits brought by the utilization of hydropower are expressed by the benefit coefficient b . For example, for a factory, its utilities can be reflected in the charging coefficient, its profit can be reflected in the benefit coefficient.

<!-- b000559 | prose | pages [15] -->
2 3 5

<!-- b000560 | prose | pages [15] -->
I m

<!-- b000561 | prose | pages [15] -->
( ( )

<!-- b000562 | prose | pages [15] -->
 =

<!-- b000563 | prose | pages [15] -->
max

<!-- b000564 | prose | pages [15] -->
f

<!-- b000565 | prose | pages [15] -->
( )

<!-- b000566 | prose | pages [15] -->
x

<!-- b000567 | prose | pages [15] -->
max 2

<!-- b000568 | prose | pages [15] -->
= = =

<!-- b000569 | prose | pages [15] -->
m

<!-- b000570 | prose | pages [15] -->
1

<!-- b000571 | prose | pages [15] -->
k

<!-- b000572 | prose | pages [15] -->
1

<!-- b000573 | prose | pages [15] -->
j

<!-- b000574 | prose | pages [15] -->
km km

<!-- b000575 | prose | pages [15] -->


<!-- b000576 | prose | pages [15] -->
−

<!-- b000577 | prose | pages [15] -->
km km km m km m

<!-- b000578 | prose | pages [15] -->
(

<!-- b000579 | prose | pages [15] -->
b c

<!-- b000580 | prose | pages [15] -->
)

<!-- b000581 | prose | pages [15] -->
x w

<!-- b000582 | prose | pages [15] -->
(21)

<!-- b000583 | prose | pages [15] -->
ij ij ij ij j j

<!-- b000584 | prose | pages [15] -->
=

<!-- b000585 | prose | pages [15] -->
1 1

<!-- b000586 | prose | pages [15] -->
i i

<!-- b000587 | prose | pages [15] -->
1

<!-- b000588 | prose | pages [15] -->
 km m is the charging coefficient, where, is the benefit coefficient, ijb ijc

<!-- b000589 | prose | pages [15] -->
 km m

<!-- b000590 | prose | pages [15] -->
is the supply, is the order ijx ij

<!-- b000591 | prose | pages [15] -->
is the regional tradeoff coefficient.

<!-- b000592 | prose | pages [15] -->
coefficient, is the fairness coefficient and

<!-- b000593 | prose | pages [15] -->
w

<!-- b000594 | prose | pages [15] -->
j

<!-- b000595 | prose | pages [15] -->
j

<!-- b000596 | prose | pages [15] -->
The influence of three economic factors: the supply difference in different regions, the demand difference in different regions, and the demand difference in different industries in the same region.

<!-- b000597 | prose | pages [15] -->
The influence of water evaporation and power loss in the process of electric transportation are both constrained by distance. Each state is located at a different distance from the two dams, which determines the different priority of the two dams’ supply to the five states, expressed by order coefficient . The three types of objects (industry, agriculture and residents) are the three types of fixed demand groups of hydropower resources. Their demands are different, and the difference of their demand proportion is

<!-- b000598 | prose | pages [16] -->
represented by fairness coefficient . The distribution of resources among the five states is expressed as regional tradeoff coefficient w.

<!-- b000599 | prose | pages [16] -->
The specific acquisition and method of the three coefficients will be introduced in detail in Section

<!-- b000600 | heading | pages [16] -->
6.2 combined with examples.

<!-- b000601 | prose | pages [16] -->
f 3( ) x ⚫ Environmental effect

<!-- b000602 | prose | pages [16] -->
After the use of water, there will be a large number of sewage discharge containing important pollutants (such as COD, BOD)[9], which will have a negative impact on the environment, such as the destruction of the ecosystem. The smaller the environmental effect, the better.

<!-- b000603 | prose | pages [16] -->
= −

<!-- b000604 | prose | pages [16] -->
max f x ( ) min

<!-- b000605 | furniture | pages [16] -->


<!-- b000606 | prose | pages [16] -->
3

<!-- b000607 | prose | pages [16] -->
k

<!-- b000608 | prose | pages [16] -->
3 5 3

<!-- b000609 | prose | pages [16] -->
 

<!-- b000610 | prose | pages [16] -->
k k k d p x

<!-- b000611 | furniture | pages [16] -->


<!-- b000612 | prose | pages [16] -->
(22)

<!-- b000613 | prose | pages [16] -->
j j ij

<!-- b000614 | prose | pages [16] -->
= = =

<!-- b000615 | prose | pages [16] -->
k 1 j 1 i 1

<!-- b000616 | prose | pages [16] -->
k k = ( 1,2,3) jp is the pollutant emission coefficient of object

<!-- b000617 | prose | pages [16] -->
where

<!-- b000618 | prose | pages [16] -->
j j = k residential) in State ( 1,2, ,5)

<!-- b000619 | prose | pages [16] -->
(industrial, agricultural and

<!-- b000620 | prose | pages [16] -->
d is the content of important pollutants (mg/L) in the amount , and j

<!-- b000621 | prose | pages [16] -->
k k = ( 1,2,3) (industrial, agricultural and residential) in State of water discharged by object j j = ( 1,2, ,5) .

<!-- b000622 | heading | pages [16] -->
6.1.2 Constraints

<!-- b000623 | prose | pages [16] -->
The constraints of supply and demand can be followed by Model One, with some additional constraints due to the inclusion of social, economic and environmental factors in Model Two.

<!-- b000624 | prose | pages [16] -->
⚫ Demand constraint

<!-- b000625 | prose | pages [16] -->
Users will have maximum and minimum demand for water. Maximum demand refers to the maximum output of production capacity, that is, to achieve the maximum satisfaction of users. Minimum demand is what the user needs to maintain basic operations.

<!-- b000626 | prose | pages [16] -->
When the supply is greater than the maximum demand, it will cause the waste of resources. When the supply is less than the minimum demand, demand is not guaranteed. So, the supply and demand constraints are as follows

<!-- b000627 | prose | pages [16] -->
 

<!-- b000628 | prose | pages [16] -->
k D

<!-- b000629 | furniture | pages [16] -->


<!-- b000630 | prose | pages [16] -->
j

<!-- b000631 | prose | pages [16] -->
min

<!-- b000632 | prose | pages [16] -->
i

<!-- b000633 | prose | pages [16] -->
⚫ Pollutant constraint

<!-- b000634 | prose | pages [16] -->
3 3

<!-- b000635 | prose | pages [16] -->


<!-- b000636 | prose | pages [16] -->
k k x D

<!-- b000637 | furniture | pages [16] -->


<!-- b000638 | prose | pages [16] -->
(23)

<!-- b000639 | prose | pages [16] -->
ij j

<!-- b000640 | prose | pages [16] -->
max

<!-- b000641 | prose | pages [16] -->
= =

<!-- b000642 | prose | pages [16] -->
1 1

<!-- b000643 | prose | pages [16] -->
The discharge of pollutants cannot exceed the maximum allowable total amount of pollutants

<!-- b000644 | prose | pages [16] -->
3 5

<!-- b000645 | prose | pages [16] -->


<!-- b000646 | prose | pages [16] -->
k k d p

<!-- b000647 | furniture | pages [16] -->


<!-- b000648 | prose | pages [16] -->
j

<!-- b000649 | prose | pages [16] -->
= =

<!-- b000650 | prose | pages [16] -->
k

<!-- b000651 | prose | pages [16] -->
1

<!-- b000652 | prose | pages [16] -->
j

<!-- b000653 | prose | pages [16] -->
1

<!-- b000654 | prose | pages [16] -->
k

<!-- b000655 | prose | pages [16] -->
3 3

<!-- b000656 | prose | pages [16] -->
 

<!-- b000657 | prose | pages [16] -->
k k x M

<!-- b000658 | furniture | pages [16] -->


<!-- b000659 | prose | pages [16] -->
(24)

<!-- b000660 | prose | pages [16] -->
j j ij

<!-- b000661 | prose | pages [16] -->
max

<!-- b000662 | prose | pages [16] -->
= =

<!-- b000663 | prose | pages [16] -->
i i

<!-- b000664 | prose | pages [16] -->
1

<!-- b000665 | prose | pages [16] -->
k k = ( 1,2,3) jp is the pollutant emission coefficient of object

<!-- b000666 | prose | pages [16] -->
where

<!-- b000667 | prose | pages [16] -->
j j = k residential) in State ( 1,2, ,5)

<!-- b000668 | prose | pages [16] -->
(industrial, agricultural and

<!-- b000669 | prose | pages [16] -->
d is the content of important pollutants (mg/L) in the amount , and j

<!-- b000670 | prose | pages [16] -->
k k = ( 1,2,3) (industrial, agricultural and residential) in State of water discharged by object

<!-- b000671 | prose | pages [17] -->
j j =

<!-- b000672 | prose | pages [17] -->
k

<!-- b000673 | prose | pages [17] -->
( 1,2, ,5)

<!-- b000674 | prose | pages [17] -->
M is the maximum allowable total amount of contaminants, and the value is 5989kg

<!-- b000675 | prose | pages [17] -->
.

<!-- b000676 | prose | pages [17] -->
max

<!-- b000677 | prose | pages [17] -->
(total COG/day)[9].

<!-- b000678 | heading | pages [17] -->
6.1.3 The model summary

<!-- b000679 | prose | pages [17] -->
By summarizing the objective function and constraint equation above, we can get the following coordinated development multi-objective programming model.

<!-- b000680 | prose | pages [17] -->
=

<!-- b000681 | prose | pages [17] -->
. (

<!-- b000682 | prose | pages [17] -->
obj F X

<!-- b000683 | prose | pages [17] -->
)

<!-- b000684 | prose | pages [17] -->
opt f x

<!-- b000685 | prose | pages [17] -->
[ ( ), ( ),

<!-- b000686 | prose | pages [17] -->
f

<!-- b000687 | prose | pages [17] -->
( )]

<!-- b000688 | prose | pages [17] -->
x f x

<!-- b000689 | prose | pages [17] -->
1 2 3

<!-- b000690 | prose | pages [17] -->
 

<!-- b000691 | prose | pages [17] -->
( )

<!-- b000692 | prose | pages [17] -->
I m

<!-- b000693 | prose | pages [17] -->
2 2 3 5

<!-- b000694 | prose | pages [17] -->


<!-- b000695 | prose | pages [17] -->
= −

<!-- b000696 | prose | pages [17] -->
max ( ) min

<!-- b000697 | prose | pages [17] -->
f x

<!-- b000698 | prose | pages [17] -->


<!-- b000699 | prose | pages [17] -->
1

<!-- b000700 | prose | pages [17] -->
 

<!-- b000701 | prose | pages [17] -->
2

<!-- b000702 | prose | pages [17] -->


<!-- b000703 | prose | pages [17] -->
−

<!-- b000704 | prose | pages [17] -->
km km

<!-- b000705 | prose | pages [17] -->
[

<!-- b000706 | prose | pages [17] -->
D

<!-- b000707 | prose | pages [17] -->
]

<!-- b000708 | prose | pages [17] -->
x

<!-- b000709 | prose | pages [17] -->


<!-- b000710 | prose | pages [17] -->
j ij

<!-- b000711 | prose | pages [17] -->


<!-- b000712 | prose | pages [17] -->
= = = = =

<!-- b000713 | prose | pages [17] -->
m m

<!-- b000714 | prose | pages [17] -->
1 1

<!-- b000715 | prose | pages [17] -->
k

<!-- b000716 | prose | pages [17] -->
1

<!-- b000717 | prose | pages [17] -->
j

<!-- b000718 | prose | pages [17] -->
1 1

<!-- b000719 | prose | pages [17] -->
i

<!-- b000720 | prose | pages [17] -->


<!-- b000721 | prose | pages [17] -->
(25)

<!-- b000722 | prose | pages [17] -->
( )

<!-- b000723 | prose | pages [17] -->
I m

<!-- b000724 | prose | pages [17] -->
3 5

<!-- b000725 | prose | pages [17] -->


<!-- b000726 | prose | pages [17] -->
= =

<!-- b000727 | prose | pages [17] -->
max ( ) max

<!-- b000728 | prose | pages [17] -->
f x

<!-- b000729 | prose | pages [17] -->


<!-- b000730 | prose | pages [17] -->
2

<!-- b000731 | prose | pages [17] -->


<!-- b000732 | prose | pages [17] -->
m

<!-- b000733 | prose | pages [17] -->
  = −

<!-- b000734 | prose | pages [17] -->
max

<!-- b000735 | prose | pages [17] -->
f

<!-- b000736 | prose | pages [17] -->
( )

<!-- b000737 | prose | pages [17] -->
x

<!-- b000738 | prose | pages [17] -->
min

<!-- b000739 | prose | pages [17] -->
3

<!-- b000740 | prose | pages [17] -->


<!-- b000741 | prose | pages [17] -->
st. .

<!-- b000742 | prose | pages [17] -->
 

<!-- b000743 | prose | pages [17] -->
W Q

<!-- b000744 | prose | pages [17] -->
1

<!-- b000745 | prose | pages [17] -->
G

<!-- b000746 | prose | pages [17] -->
  +

<!-- b000747 | prose | pages [17] -->


<!-- b000748 | prose | pages [17] -->
W Q W

<!-- b000749 | prose | pages [17] -->


<!-- b000750 | prose | pages [17] -->
2

<!-- b000751 | prose | pages [17] -->
H

<!-- b000752 | prose | pages [17] -->
1

<!-- b000753 | prose | pages [17] -->
down

<!-- b000754 | prose | pages [17] -->


<!-- b000755 | prose | pages [17] -->
3

<!-- b000756 | prose | pages [17] -->


<!-- b000757 | prose | pages [17] -->
 

<!-- b000758 | prose | pages [17] -->
k k k

<!-- b000759 | prose | pages [17] -->
D x D

<!-- b000760 | prose | pages [17] -->


<!-- b000761 | prose | pages [17] -->
j

<!-- b000762 | prose | pages [17] -->
min

<!-- b000763 | prose | pages [17] -->
ij j

<!-- b000764 | prose | pages [17] -->
=

<!-- b000765 | prose | pages [17] -->
i

<!-- b000766 | prose | pages [17] -->
1

<!-- b000767 | prose | pages [17] -->


<!-- b000768 | prose | pages [17] -->
3 5 3

<!-- b000769 | prose | pages [17] -->
 

<!-- b000770 | prose | pages [17] -->
 

<!-- b000771 | prose | pages [17] -->
k k k

<!-- b000772 | prose | pages [17] -->
d p x

<!-- b000773 | prose | pages [17] -->
j j ij

<!-- b000774 | prose | pages [17] -->


<!-- b000775 | prose | pages [17] -->
= = =

<!-- b000776 | prose | pages [17] -->
1 1 1

<!-- b000777 | prose | pages [17] -->
k j i

<!-- b000778 | prose | pages [17] -->
 

<!-- b000779 | prose | pages [17] -->
k

<!-- b000780 | prose | pages [17] -->
0

<!-- b000781 | prose | pages [17] -->
x

<!-- b000782 | prose | pages [17] -->


<!-- b000783 | prose | pages [17] -->
ij

<!-- b000784 | prose | pages [17] -->
−

<!-- b000785 | prose | pages [17] -->


<!-- b000786 | prose | pages [17] -->
km km km m km m

<!-- b000787 | prose | pages [17] -->
( )

<!-- b000788 | prose | pages [17] -->
b c x w

<!-- b000789 | prose | pages [17] -->


<!-- b000790 | prose | pages [17] -->
ij ij ij ij j j

<!-- b000791 | prose | pages [17] -->


<!-- b000792 | prose | pages [17] -->
= = = = =

<!-- b000793 | prose | pages [17] -->
1 1

<!-- b000794 | prose | pages [17] -->
k k

<!-- b000795 | prose | pages [17] -->
1

<!-- b000796 | prose | pages [17] -->
j

<!-- b000797 | prose | pages [17] -->
1 1

<!-- b000798 | prose | pages [17] -->
i

<!-- b000799 | prose | pages [17] -->


<!-- b000800 | prose | pages [17] -->
I m

<!-- b000801 | prose | pages [17] -->
( ) 3 3 5

<!-- b000802 | prose | pages [17] -->
 

<!-- b000803 | prose | pages [17] -->


<!-- b000804 | prose | pages [17] -->
k k k

<!-- b000805 | prose | pages [17] -->
d p x

<!-- b000806 | prose | pages [17] -->
j j ij

<!-- b000807 | prose | pages [17] -->


<!-- b000808 | prose | pages [17] -->
= = = =

<!-- b000809 | prose | pages [17] -->
k k

<!-- b000810 | prose | pages [17] -->
1 1

<!-- b000811 | prose | pages [17] -->
j

<!-- b000812 | prose | pages [17] -->
1 1

<!-- b000813 | prose | pages [17] -->
i

<!-- b000814 | prose | pages [17] -->
max max

<!-- b000815 | prose | pages [17] -->
(26)

<!-- b000816 | prose | pages [17] -->
k

<!-- b000817 | prose | pages [17] -->
M

<!-- b000818 | prose | pages [17] -->
max

<!-- b000819 | prose | pages [17] -->
See the Formula (8-24) for a symbolic explanation. More parameters are determined in the Section 6.2.

<!-- b000820 | heading | pages [17] -->
6.2 Parameters to Determine

<!-- b000821 | prose | pages [17] -->
Due to the limitation of paper space, it is impossible to list every case. Therefore, we take California as an example to explain the determination of each parameter in the model.

<!-- b000822 | prose | pages [17] -->
f 2( ) x

<!-- b000823 | heading | pages [17] -->
6.2.1 Parameters in economic effect

<!-- b000824 | prose | pages [17] -->
There are five parameters in economic effect

<!-- b000825 | prose | pages [17] -->
  km m km , Order coefficient , Fairness coefficient ijc ij j

<!-- b000826 | prose | pages [17] -->
km ⚫ Benefit coefficient ijb

<!-- b000827 | prose | pages [17] -->
f f 2( ) x : Benefit coefficient km , Charging coefficient ijb

<!-- b000828 | prose | pages [17] -->
m , and Regional tradeoff coefficient

<!-- b000829 | prose | pages [17] -->
w . j

<!-- b000830 | prose | pages [17] -->
The benefits brought by the utilization of hydropower are expressed by the benefit coefficient.

<!-- b000831 | prose | pages [17] -->
The benefit coefficient of industrial and agricultural water (or electricity) can be determined by the reciprocal of the water (or electricity) demand of output value. According to the data we checked[11,12], we can get:

<!-- b000832 | caption | pages [18] -->
Table 3: Benefit coefficient of industry and agriculture

<!-- b000833 | prose | pages [18] -->
Total output value

<!-- b000834 | prose | pages [18] -->
Total water volume

<!-- b000835 | prose | pages [18] -->
Object

<!-- b000836 | prose | pages [18] -->
Benefit

<!-- b000837 | prose | pages [18] -->
Benefit

<!-- b000838 | prose | pages [18] -->
Total

<!-- b000839 | prose | pages [18] -->
coefficient(water)

<!-- b000840 | prose | pages [18] -->
coefficient(electricity)

<!-- b000841 | prose | pages [18] -->
electricity/KMWh

<!-- b000842 | prose | pages [18] -->
/million dollars

<!-- b000843 | prose | pages [18] -->
/million gallons

<!-- b000844 | prose | pages [18] -->
Industry 9,025,218 19183

<!-- b000845 | prose | pages [18] -->
Agriculture 196037.6 399

<!-- b000846 | prose | pages [18] -->
dollars/gallons

<!-- b000847 | prose | pages [18] -->
dollars/KWh

<!-- b000848 | prose | pages [18] -->
47631.5 470.48 189.48

<!-- b000849 | prose | pages [18] -->
6804.5 491.3223 28.80999

<!-- b000850 | prose | pages [18] -->
Domestic water (electricity) coefficient is generally difficult to have a clear value[8], in order to ensure the supply, we give a large value according to the Table 3. The benefit coefficient of water is 550 dollars/gallons, and the benefit coefficient of electricity is 200 dollars/kwh.

<!-- b000851 | prose | pages [18] -->
km ⚫ Charging coefficient

<!-- b000852 | furniture | pages [18] -->


<!-- b000853 | prose | pages [18] -->
ijc

<!-- b000854 | prose | pages [18] -->
The value of water and electricity brought by water resources is directly reflected in the charging system of hydropower, which is expressed by the charging coefficient.

<!-- b000855 | prose | pages [18] -->
The charging coefficient can be determined by the California unit price of water and electricity[13,14,15].

<!-- b000856 | caption | pages [18] -->
Table 4: Charging coefficient of three objects

<!-- b000857 | prose | pages [18] -->
Industry Object Water price 3.77 (dollars/gallons）

<!-- b000858 | prose | pages [18] -->
Electricity price

<!-- b000859 | prose | pages [18] -->
8.16 (cents/KWh）

<!-- b000860 | prose | pages [18] -->
 m ⚫ Order coefficient

<!-- b000861 | furniture | pages [18] -->


<!-- b000862 | prose | pages [18] -->
ij

<!-- b000863 | prose | pages [18] -->
Agriculture Residents

<!-- b000864 | prose | pages [18] -->
2.12 5.85

<!-- b000865 | prose | pages [18] -->
17.5 15.98

<!-- b000866 | prose | pages [18] -->
The different priority of the three water sources’ supply to the five states, expressed by order coefficient.

<!-- b000867 | prose | pages [18] -->
The conversion of water (or electricity) use priority to order coefficient can be obtained from the following transformation relationship[8]:

<!-- b000868 | prose | pages [18] -->
+

<!-- b000869 | prose | pages [18] -->
1

<!-- b000870 | prose | pages [18] -->


<!-- b000871 | prose | pages [18] -->
=

<!-- b000872 | prose | pages [18] -->
m

<!-- b000873 | furniture | pages [18] -->


<!-- b000874 | prose | pages [18] -->
ij I m

<!-- b000875 | prose | pages [18] -->
( )

<!-- b000876 | prose | pages [18] -->


<!-- b000877 | prose | pages [18] -->
(1

<!-- b000878 | prose | pages [18] -->
=

<!-- b000879 | prose | pages [18] -->
i

<!-- b000880 | prose | pages [18] -->
1

<!-- b000881 | prose | pages [18] -->
−

<!-- b000882 | prose | pages [18] -->
m m

<!-- b000883 | prose | pages [18] -->
n n n

<!-- b000884 | prose | pages [18] -->
max

<!-- b000885 | prose | pages [18] -->
j ij

<!-- b000886 | furniture | pages [18] -->


<!-- b000887 | prose | pages [18] -->
(27)

<!-- b000888 | prose | pages [18] -->
+ + −

<!-- b000889 | prose | pages [18] -->
m m

<!-- b000890 | prose | pages [18] -->
n n

<!-- b000891 | prose | pages [18] -->
)

<!-- b000892 | prose | pages [18] -->
max

<!-- b000893 | prose | pages [18] -->
j ij

<!-- b000894 | prose | pages [18] -->
m = (or electricity 1 m where, n represents the conversion of water ij m = 2 ) use priority.

<!-- b000895 | prose | pages [18] -->
i = 1 For a given state, water is provided from three sources: Glen Canyon dam i = i = 2 3 ）, Hoover Dam （ ）. As the increase of transport distance will cause the loss of water due to ）, and rainfall （ （ evaporation, the priority is determined by distance. For California, rainfall is available in a very short period of time, and its distance to Hoover Dam is less than Glen Canyon dam. Therefore, the priority  = = = respectively. 1 1 1 1 degree is rainfall first, Hoover second, and Glenn last, denoted by

<!-- b000896 | prose | pages [18] -->
(water) are 1/3, 1/2, 1/6 respectively.

<!-- b000897 | prose | pages [18] -->
n 3, n 2, n 1 1 j 2 j 3 j ij

<!-- b000898 | prose | pages [18] -->
i = i = 1 2 Electricity comes from two sources: Glen Canyon dam ） and Hoover Dam ）. As the （ （ increase of transportation distance will cause loss due to power loss, its priority is also determined by the

<!-- b000899 | prose | pages [19] -->
distance. The degree of priority is: Hoover is the first, Glenn is the second, respectively expressed by

<!-- b000900 | prose | pages [19] -->
 (electricity) are 1/3, 2/3 respectively. = = , it is obtained that 2 2 1 n 2, n 1 1 j 2 j ij

<!-- b000901 | prose | pages [19] -->
 km ⚫ Fairness coefficient

<!-- b000902 | furniture | pages [19] -->


<!-- b000903 | prose | pages [19] -->
j

<!-- b000904 | prose | pages [19] -->
Their demands are different, and the difference of their demand proportion is represented by fairness coefficient.

<!-- b000905 | prose | pages [19] -->
+

<!-- b000906 | prose | pages [19] -->
1

<!-- b000907 | prose | pages [19] -->


<!-- b000908 | prose | pages [19] -->
=

<!-- b000909 | prose | pages [19] -->
km

<!-- b000910 | furniture | pages [19] -->


<!-- b000911 | prose | pages [19] -->
j

<!-- b000912 | prose | pages [19] -->
3

<!-- b000913 | prose | pages [19] -->


<!-- b000914 | prose | pages [19] -->
(1

<!-- b000915 | prose | pages [19] -->
=

<!-- b000916 | prose | pages [19] -->
k

<!-- b000917 | prose | pages [19] -->
1

<!-- b000918 | prose | pages [19] -->
−

<!-- b000919 | prose | pages [19] -->
km km

<!-- b000920 | prose | pages [19] -->
n n n

<!-- b000921 | prose | pages [19] -->
max

<!-- b000922 | prose | pages [19] -->
j

<!-- b000923 | furniture | pages [19] -->


<!-- b000924 | prose | pages [19] -->
(28)

<!-- b000925 | prose | pages [19] -->
+ + −

<!-- b000926 | prose | pages [19] -->
km km

<!-- b000927 | prose | pages [19] -->
n n

<!-- b000928 | prose | pages [19] -->
)

<!-- b000929 | prose | pages [19] -->
max

<!-- b000930 | prose | pages [19] -->
j

<!-- b000931 | prose | pages [19] -->
Water demand priority[16]: residential water first, agricultural water second, industrial water last, = = = . Substitute into the formula, and the water use fairness 11 21 31 corresponding to the order:

<!-- b000932 | prose | pages [19] -->
n 3, n 2, n 1 j j j

<!-- b000933 | prose | pages [19] -->
coefficients are 1/3, 1/2, 1/6 respectively.

<!-- b000934 | prose | pages [19] -->
Priority of electricity demand[17]: agricultural electricity consumption occupies a small part of electricity consumption, so we give priority to domestic electricity consumption, followed by industrial electricity consumption, and agricultural electricity consumption last.

<!-- b000935 | prose | pages [19] -->
Corresponding: = , plug into the formula, and the electricity fairness coefficient is 1/3, 1/6, 1/2, = = 11 21 31 n 2, n 3, n 1 j j j

<!-- b000936 | prose | pages [19] -->
respectively.

<!-- b000937 | prose | pages [19] -->
m ⚫ Regional tradeoff coefficient

<!-- b000938 | prose | pages [19] -->
w j

<!-- b000939 | prose | pages [19] -->
The distribution of resources among the five states is expressed as regional tradeoff coefficient.

<!-- b000940 | prose | pages [19] -->
Taking water as an example, we have data[10] on water use in five states. According to the data, the weight of the five states is shown in the following Figure 5.

<!-- b000941 | furniture | pages [19] -->


<!-- b000942 | caption | pages [19] -->
Figure 6: The regional tradeoff coefficient of five states

<!-- b000943 | prose | pages [19] -->
f 3( ) x

<!-- b000944 | heading | pages [19] -->
6.2.2 Parameters in environmental effect

<!-- b000945 | prose | pages [19] -->
f 3( ) x : pollutant emission coefficient k There are two parameters in environmental effect

<!-- b000946 | prose | pages [19] -->
k content of important pollutants d . j

<!-- b000947 | prose | pages [19] -->
jp ,and the

<!-- b000948 | prose | pages [19] -->
Through data search[19], California's COD (or other pollutants) emissions k d 190mg/L, emission j

<!-- b000949 | prose | pages [20] -->
k coefficient

<!-- b000950 | prose | pages [20] -->
is 0.20. jp

<!-- b000951 | heading | pages [20] -->
6.3 Calculation Results

<!-- b000952 | heading | pages [20] -->
6.3.1 The answer to question two

<!-- b000953 | prose | pages [20] -->
In order to better represent the relationship between agricultural, industrial, residential water use and power generation, we assume that each state has sufficient water supply and rainfall of 1000 million gallons, calculate the optimal economic benefit, and obtain the distribution of hydropower resources in each state as shown in the table  below.

<!-- b000954 | prose | pages [20] -->
As can be seen from the table :(1) in most areas, agricultural and residential water use is relatively high. This is because (1) each state has a relatively large area of farmland and a high demand for irrigation water. (2) The priority of residential water is high. We give priority to residential water in the redistribution of water resources, so the proportion of residential water is relatively high.

<!-- b000955 | prose | pages [20] -->
As can be seen from the table, the proportion of industrial and residential electricity consumption is relatively high, while that of agriculture is relatively low. This is because (1) industrial output has a high demand for electricity, (2) residents are given priority to power consumption to ensure their living needs, and (3) the main demand of agriculture is water, which has a low demand for electricity.

<!-- b000956 | heading | pages [20] -->
6.3.2 The answer to question three

<!-- b000957 | prose | pages [20] -->
Question two considers resource allocation in the absence of water shortage. At this point, Economic effect is mainly used for consideration. The third problem is the consideration of water shortage, so the multi-objective planning with Social effect, Economic effect and Environmental effect is used. The guarantee rate is listed in the following table

<!-- b000958 | caption | pages [20] -->
Table 5: Guarantee rate

<!-- b000959 | prose | pages [20] -->
f x 1( )

<!-- b000960 | prose | pages [20] -->
f 2( ) x

<!-- b000961 | prose | pages [20] -->
f 3( ) x

<!-- b000962 | prose | pages [20] -->
Guarantee rate /million gallons

<!-- b000963 | prose | pages [20] -->
/million dollars

<!-- b000964 | prose | pages [20] -->
/kg 50% 2071.65 37965.48 1235.68 75% 2748.52 34545.59 1396.32 95% 3107.47 28675.33 1731.43

<!-- b000965 | prose | pages [20] -->
In the process of the guarantee rate changing from 50% to 95%, the total water shortage increases, and the discharge of important pollutants in the state also increases, but the benefit value generated in the state decreases, that is, the improvement of regional economic effect is at the cost of the reduction of social effect and environmental effect. It shows that the three objectives are interacting and competing

<!-- b000966 | prose | pages [21] -->
with each other in the established coordinated multi-objective programming model.

<!-- b000967 | heading | pages [21] -->
6.3.3 The re-run of the model

<!-- b000968 | prose | pages [21] -->
Considering the work of reservoir operation and dispatching in real life and the need to make corresponding adjustments after a certain period of time in the model, we run the model at an interval of one month. Each time you run the model, you get a month of scheduling data. In case of surplus and shortage, corresponding adjustment can be made next month.

<!-- b000969 | heading | pages [21] -->
7 Mexican Allocation Model

<!-- b000970 | heading | pages [21] -->
7.1 The Establishment of Mexican Allocation Model

<!-- b000971 | prose | pages [21] -->
The model is based on the allocation plan for Mexico after the reservoir allocation.

<!-- b000972 | prose | pages [21] -->
In either Model One or Model Two, after allocating resources to each state, if there are no resources =  remainRem . (Rem 0 0 means insufficient resources, Rem=0 means just used up), then the model is not applicable. No allocation of resources to Mexico.

<!-- b000973 | prose | pages [21] -->
If there is surplus after allocating resources: consider allocating resources to Mexico. We take every month as the operation cycle of the model, run the model according to the data, and obtain the water consumption Req required by the United States in a month. Taking the estimated total amount of water minus the estimated monthly water consumption Req, we get Rem. This is where the model applies. The amount allocated to Mexico is μ*Req(calculated as a scaling factor multiplied by a month's demand from the United States).

<!-- b000974 | prose | pages [21] -->
We refer to the Logistic curve and set parameters to make it conform to our model:

<!-- b000975 | prose | pages [21] -->
1

<!-- b000976 | prose | pages [21] -->


<!-- b000977 | prose | pages [21] -->
=

<!-- b000978 | prose | pages [21] -->
( )

<!-- b000979 | prose | pages [21] -->
t

<!-- b000980 | prose | pages [21] -->
(29)

<!-- b000981 | prose | pages [21] -->


<!-- b000982 | prose | pages [21] -->
−

<!-- b000983 | prose | pages [21] -->
+ −

<!-- b000984 | prose | pages [21] -->
rt 1 ( 1)

<!-- b000985 | prose | pages [21] -->
e

<!-- b000986 | prose | pages [21] -->
m

<!-- b000987 | prose | pages [21] -->


<!-- b000988 | prose | pages [21] -->
0

<!-- b000989 | heading | pages [21] -->
7.2 Calculation Results

<!-- b000990 | prose | pages [21] -->
We use MATLAB to set the parameters to conform to our model and get the final parameter value

<!-- b000991 | prose | pages [21] -->
= = =1, r = 0.0001 1 9.2 , . m 0

<!-- b000992 | caption | pages [21] -->
Figure 7: Relation graph

<!-- b000993 | prose | pages [22] -->
When the remaining Rem is very small and μ is close to 0, the resources allocated to Mexico are also close to 0. When Rem is greater than or equal to twice America's monthly demand Req, μ is almost 1, giving Mexico the amount of the United States in a month, i.e., giving Mexico the amount of the United States in a month at most. (The calculation period is one month). When Rem is exactly equal to Req, μ=0.5, giving the United States half of what it needs in a month.

<!-- b000994 | heading | pages [22] -->
8 Sensitivity Analysis

<!-- b000995 | heading | pages [22] -->
8.1 Change in Demand

<!-- b000996 | prose | pages [22] -->
Over time, demand for hydropower may rise or fall in various industries. At this point, we select industrial, agricultural and residential water consumption demand to increase by 5% on the basis of the original demand, industrial, agricultural and residential electricity consumption demand to decrease by 5% on the basis of the original demand, so as to explore the impact on the final result of our model solution.

<!-- b000997 | caption | pages [22] -->
Figure 8: Change in demand

<!-- b000998 | prose | pages [22] -->
It can be seen that the original proportion of residential water consumption is relatively large, and the water resource base used is relatively large. Therefore, when the industrial, agricultural and residential water demand increases by 5% respectively, the overall proportion changes greatly, and the residential proportion increases more. However, the original industrial proportion is relatively small. After the 5% increase in demand, it has little influence on the overall proportion, and the industrial proportion is also less adjusted. For electricity consumption, it can also be seen that the industry with a large original share will cause a large change in the overall share.

<!-- b000999 | heading | pages [22] -->
8.2 Renewable Energy Technologies

<!-- b001000 | prose | pages [22] -->
In our model, only the technological upgrading of hydropower generation in renewable energy technologies is considered for the time being. If considering wind power, solar power and other renewable energy technologies, you just add the power supply. In the first model, it is mentioned that the utilization efficiency of water energy conversion into electric energy is η+β, where η is the basic utilization efficiency, which is 80%.  represents the function of the renewable energy technologies enhancement., and the added value is assumed to be 5%, 10% and 15% respectively. The calculated water supply decreases with the increase of utilization efficiency. This is quite understandable because there is less extra energy lost, so there is less water to provide.

<!-- b001001 | caption | pages [23] -->
Table 6: Change of renewable energy technologies

<!-- b001002 | prose | pages [23] -->
β 5%

<!-- b001003 | prose | pages [23] -->
Supply 55567

<!-- b001004 | prose | pages [23] -->
10% 15%

<!-- b001005 | prose | pages [23] -->
53722 52642

<!-- b001006 | prose | pages [23] -->
It can be seen from the data that after the increase of β in our model, the water supply decreased, but not significantly, indicating that the water use efficiency η+β has little influence on our model, which may be because the loss caused by evaporation is greater than that of water use efficiency.

<!-- b001007 | heading | pages [23] -->
8.3 Water and Electricity Conservation Measures

<!-- b001008 | prose | pages [23] -->
We believe that additional water and electricity conservation measures will lead to a reduction in residential demand for water and electricity. The need for less resources will keep the dam at a higher  is high), so the more demand water level, which will keep generating capacity at a higher level ( h decreases, the more water the reservoir provides. However, when the demand is reduced to a certain extent, the water level of the reservoir is high enough and there is little change, and the power generation capacity is basically stable. With the decrease of the demand, the reduced water provided by the dam also tends to be positively correlated.

<!-- b001009 | caption | pages [23] -->
Figure 9: Change of conservation measures

<!-- b001010 | heading | pages [23] -->
9 Strengths and Weaknesses

<!-- b001011 | heading | pages [23] -->
9.1 Strengths

<!-- b001012 | prose | pages [23] -->
(1) The two main models used in this paper are universal and can deal with different supply and demand conditions and get better distribution schemes.

<!-- b001013 | prose | pages [23] -->
(2) Model Two comprehensively considers social effect, economic effect and environmental effect, which interact and compete with each other to improve the rationality of the results

<!-- b001014 | prose | pages [23] -->
(3) In terms of water and electricity conversion and power loss, a large number of literatures are referred to ensure the rigor of the model.

<!-- b001015 | heading | pages [23] -->
9.2 Weakness

<!-- b001016 | prose | pages [24] -->
(1) In the model calculation, specific values of some parameters are not found, which may have certain influence on the results.

<!-- b001017 | prose | pages [24] -->
(2) Only hydroelectric power generation is considered in the model. If other power generation methods such as wind power generation are considered, the results will be more realistic.

<!-- b001018 | heading | pages [24] -->
References

<!-- b001019 | references | pages [24] -->
[1] https://finance.sina.com.cn/tech/2021-06-11/doc-ikqcfnca0393441.shtml

<!-- b001020 | references | pages [24] -->
[2] News of water shortages in the Western United States https://finance.sina.com.cn/tech/2021-08-

<!-- b001021 | references | pages [24] -->
19/doc-ikqciyzm2363948.shtml

<!-- b001022 | references | pages [24] -->
[3] The river basin of Colorado River from Wikipedia https://en.wikipedia.org/wiki/Colorado_River

<!-- b001023 | references | pages [24] -->
[4] https://droughtmonitor.unl.edu/

<!-- b001024 | references | pages [24] -->
[5] Lake Powell https://en.wikipedia.org/wiki/Lake_Powell

<!-- b001025 | references | pages [24] -->
[6] Lake Mead https://en.wikipedia.org/wiki/Lake_Mead

<!-- b001026 | references | pages [24] -->
[7] Hydroelectricity https://en.wikipedia.org/wiki/Hydroelectricity

<!-- b001027 | references | pages [24] -->
[8] Chang Yi. Research and application of optimal allocation of regional water resources based on genetic

<!-- b001028 | references | pages [24] -->
algorithm [D] Huazhong University of science and technology, 2011.

<!-- b001029 | references | pages [24] -->
[9] Du Bolin. Research on optimal allocation of water resources in Dali County Based on simulated

<!-- b001030 | references | pages [24] -->
annealing particle swarm optimization [D] Xi'an University of technology, 2021 DOI:10.27398/d.cnki.

<!-- b001031 | references | pages [24] -->
gxalu. 2021.000819.

<!-- b001032 | references | pages [24] -->
[10] Dieter C A. Water availability and use science program: Estimated use of water in the United States

<!-- b001033 | references | pages [24] -->
in 2015[M]. Geological Survey, 2018.

<!-- b001034 | references | pages [24] -->
[11] https://www.eia.gov/electricity/sales_revenue_price/pdf/table5_c.pdf

<!-- b001035 | references | pages [24] -->
[12] https://apps.bea.gov/regional/downloadzip.cfm

<!-- b001036 | references | pages [24] -->
[13] https://www.boardofwatersupply.com/customer-service/water-rates-and-charges/water-rate-

<!-- b001037 | references | pages [24] -->
schedule-july-1-2019-june-30-2023

<!-- b001038 | references | pages [24] -->
[14] https://www.electricitylocal.com/states/california/industry/

<!-- b001039 | references | pages [24] -->
[15] https://www.cfbf.com/wp-content/uploads/2019/06/ElectricityRates.pdf

<!-- b001040 | references | pages [24] -->
[16] https://www.suiniann.com/book/895/25709.html

<!-- b001041 | references | pages [24] -->
[17] https://www.eia.gov/electricity/state/

<!-- b001042 | references | pages [24] -->
[18] https://www.waterboards.ca.gov/resources/data_databases/wq_status_report.html

<!-- b001043 | references | pages [25] -->
Article for Drought and Thirst magazine

<!-- b001044 | references | pages [25] -->
Salvation in an age of water scarcity

<!-- b001045 | references | pages [25] -->
The Colorado River forms the largest water

<!-- b001046 | references | pages [25] -->
system in the Western United States -- known as

<!-- b001047 | references | pages [25] -->
the "lifeline of the Southwest" because it flows

<!-- b001048 | references | pages [25] -->
through vast arid and semi-arid areas. However,

<!-- b001049 | references | pages [25] -->
due to severe drought and irrational use of water

<!-- b001050 | references | pages [25] -->
resources, the volume of water from sources

<!-- b001051 | references | pages [25] -->
feeding dams and reservoirs is decreasing in

<!-- b001052 | references | pages [25] -->
many areas. Consequently, a rational, defensible

<!-- b001053 | references | pages [25] -->
water allocation plan for current and future water

<!-- b001054 | references | pages [25] -->
supply conditions is critically important.

<!-- b001055 | references | pages [25] -->
In order to solve the reservoir water

<!-- b001056 | references | pages [25] -->
resources allocation problem, we put forward two

<!-- b001057 | references | pages [25] -->
models: Model I is Water and Electricity

<!-- b001058 | references | pages [25] -->
Transportation Model and Model II is Coordinated Development of Multi-objective Programming Model.

<!-- b001059 | references | pages [25] -->
For the convenience of solving our model, we first solved the problem of the relationship between

<!-- b001060 | references | pages [25] -->
water height in the reservoirs and the volume of water in the reservoirs. On this basis, we further consider

<!-- b001061 | references | pages [25] -->
the objective function and constraint relations of the model. We try to find a distribution method that

<!-- b001062 | references | pages [25] -->
would allow the dam to supply the least amount of water, which can alleviate the water shortage situation.

<!-- b001063 | references | pages [25] -->
With regard to the constraints of the model, we think about the constraints on quantity demanded, the

<!-- b001064 | references | pages [25] -->
constraints on loss, and the constraints on inventory capacity. Based on the relationship between the Glen

<!-- b001065 | references | pages [25] -->
Canyon and Hoover dams and given parameters, the model can be used to calculate the amount of water

<!-- b001066 | references | pages [25] -->
and electricity supplied by the two dams to the five states, namely Arizona, California, Wyoming, New

<!-- b001067 | references | pages [25] -->
Mexico, and Colorado.

<!-- b001068 | references | pages [25] -->
It is equally difficult to resolve the competing interests of water availability for general usage and

<!-- b001069 | references | pages [25] -->
electricity production. To this end, we propose Model II, which can better determine a suitable allocation

<!-- b001070 | references | pages [25] -->
of water and electricity to agriculture, industry, and residences in the five states. The idea of our second

<!-- b001071 | references | pages [25] -->
model is to combine social and economic benefits and put forward a multi-objective programming model.

<!-- b001072 | references | pages [25] -->
Through this model, we can meet the basic needs of water and power supply while taking other aspects

<!-- b001073 | references | pages [25] -->
into account. Finally, we can get the trade-offs for each industry.

<!-- b001074 | references | pages [25] -->
After getting enough data, our model works well. For example, we might need temperature data,

<!-- b001075 | references | pages [25] -->
rainfall data, and so on. We recommend running our model every other month to better manage water

<!-- b001076 | references | pages [25] -->
resources so that the optimal strategy can be adjusted in time.

<!-- b001077 | references | pages [25] -->
When it comes to Mexico’s rights, we have a tiered distribution system, which can allocate the

<!-- b001078 | references | pages [25] -->
remaining water resources well. Because of the water shortage, we are not considering the diversion of

<!-- b001079 | references | pages [25] -->
the Colorado River into the Gulf of California.

<!-- b001080 | references | pages [25] -->
Although our method can solve the problem of reservoir water allocation more, we still need to

<!-- b001081 | references | pages [25] -->
cherish water resources. We encourage people to save water, and encourage relevant sectors to increase

<!-- b001082 | references | pages [25] -->
the proportion of renewable energy technologies. Only by working together can we solve the problem of

<!-- b001083 | references | pages [25] -->
water shortage.
