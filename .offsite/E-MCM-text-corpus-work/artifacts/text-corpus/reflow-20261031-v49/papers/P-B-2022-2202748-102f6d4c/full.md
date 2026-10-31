# P-B-2022-2202748-102f6d4c

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2022

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
B

<!-- b000005 | title | pages [1] -->
2202748

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Salvation in an Age of Water Scarcity

<!-- b000008 | prose | pages [1] -->
As drought worsens in the western United States, the Colorado River, the lifeline of the Southwest, is in dire straits. In the Colorado River basin, it is important to allocate water wisely. This paper aims at measuring competing interests of different users in different states and making a water and hydroelectric power allocation plan suitable for different environmental conditions.

<!-- b000009 | prose | pages [1] -->
Two models are mainly established: Model I: Water and Electricity Transportation Model； Model II: Coordinated Development of Multi-objective Programming Model.

<!-- b000010 | prose | pages [1] -->
Before all the models are established, we analyze the reservoirs of the Glen Canyon dam and Hoover dam, get the relationship between water height in the reservoir and the volume of water in the reservoirs.

<!-- b000011 | prose | pages [1] -->
For Model I: In order to reasonably allocation water and electricity, we set up a Transportation Model of water and electricity. The objective function is the minimum supply of water from the two dams. The constraint conditions are mainly the constraint of minimum generating water level on supply and the constraint of demand on supply.

<!-- b000012 | prose | pages [1] -->
By analyzing the geographical position and topography of five states, the Glen Canyon dam and Hoover dam, we get the relationship between water flow direction and water resource transfer between the two dams, which reflects the water supply situation. After analyzing the loss of water and electricity during transportation, the final constraint conditions are obtained. Then, we designed the Maintenance Time Calculation Algorithm to solve the longest time to maintain the demand without the addition of additional water. Finally, we assign the initial water level of Lake Powell and Lake Mead to the numerical result Section 5.4.

<!-- b000013 | prose | pages [1] -->
For Model II: This Model is a further extension of Model I, which balances the competing interests of industry, agriculture and residents in five states. The supply of water is reflected in three aspects: Social effect, Economic effect and Environmental effect. The supply of electricity is reflected in Social effect and Economic effect.

<!-- b000014 | prose | pages [1] -->
When the situation of water shortage does not occur, we mainly consider the Economic effect of industrial, agricultural and residential use objects in five states. When water shortage occurs, we combine three effects to carry out multi-objective planning. See Section 6.3 for the results.

<!-- b000015 | prose | pages [1] -->
Additionally, we have taken into account the rights and interests of Mexico and propose an allocation plan for Mexico under the condition of different water resources remaining.

<!-- b000016 | prose | pages [1] -->
Finally, sensitivity analysis includes the influences of the changes over time in the demand for water and electricity of three types of objects (industry, agriculture and residents), the development of renewable energy technology and water and electricity conservation measures.

<!-- b000017 | keywords | pages [1] -->
Keywords: Transportation Model; Multi-objective Programming; Distribution and tradeoff

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
1 Introduction .......................................................................................................................................... 3

<!-- b000020 | contents | pages [2] -->
1.1 Background ................................................................................................................................... 3

<!-- b000021 | contents | pages [2] -->
1.2 Restatement of the Problem .......................................................................................................... 3

<!-- b000022 | contents | pages [2] -->
1.3 Our Work ....................................................................................................................................... 4

<!-- b000023 | contents | pages [2] -->
2 Assumptions and Justifications ........................................................................................................... 5

<!-- b000024 | contents | pages [2] -->
3 Notations ............................................................................................................................................... 5

<!-- b000025 | contents | pages [2] -->
4 Model Preparation ............................................................................................................................... 6

<!-- b000026 | contents | pages [2] -->
4.1 Data Collection ............................................................................................................................. 6

<!-- b000027 | contents | pages [2] -->
4.2 Relationship between Water Level and Storage Volume .............................................................. 6

<!-- b000028 | contents | pages [2] -->
5 Model I: Water and Electricity Transportation Model .................................................................... 8

<!-- b000029 | contents | pages [2] -->
5.1 Basic Ideas .................................................................................................................................... 8

<!-- b000030 | contents | pages [2] -->
5.2 Establishment of Transportation Model ........................................................................................ 9

<!-- b000031 | contents | pages [2] -->
5.3 Maintenance Time Calculation Algorithm .................................................................................. 12

<!-- b000032 | contents | pages [2] -->
5.4 Calculation Results ..................................................................................................................... 13

<!-- b000033 | contents | pages [2] -->
6 Model II: Coordinated Development of Multi-objective Programming Model ........................... 14

<!-- b000034 | contents | pages [2] -->
6.1 The Establishment of Multi-objective Programming Model ...................................................... 14

<!-- b000035 | contents | pages [2] -->
6.2 Parameters to Determine ............................................................................................................. 17

<!-- b000036 | contents | pages [2] -->
6.3 Calculation Results ..................................................................................................................... 20

<!-- b000037 | contents | pages [2] -->
7 Mexican Allocation Model ................................................................................................................. 21

<!-- b000038 | contents | pages [2] -->
7.1 The Establishment of Mexican Allocation Model ...................................................................... 21

<!-- b000039 | contents | pages [2] -->
7.2 Calculation Results ..................................................................................................................... 21

<!-- b000040 | contents | pages [2] -->
8 Sensitivity Analysis ............................................................................................................................. 22

<!-- b000041 | contents | pages [2] -->
8.1 Change in Demand ...................................................................................................................... 22

<!-- b000042 | contents | pages [2] -->
8.2 Renewable Energy Technologies ................................................................................................ 22

<!-- b000043 | contents | pages [2] -->
8.3 Water and Electricity Conservation Measures ............................................................................ 23

<!-- b000044 | contents | pages [2] -->
9 Strengths and Weaknesses ................................................................................................................. 23

<!-- b000045 | contents | pages [2] -->
9.1 Strengths ..................................................................................................................................... 23

<!-- b000046 | contents | pages [2] -->
9.2 Weakness ..................................................................................................................................... 23

<!-- b000047 | contents | pages [2] -->
References .............................................................................................................................................. 24

<!-- b000048 | contents | pages [2] -->
Article for Drought and Thirst magazine ........................................................................................... 25

<!-- b000049 | heading | pages [3] -->
1 Introduction

<!-- b000050 | heading | pages [3] -->
1.1 Background

<!-- b000051 | prose | pages [3] -->
"Please join me and the people of Utah, regardless of religion, in humbly praying for rain for one weekend," Utah Governor Spencer J.Cox said in a video plea on June 4, 2021.[1] "The 'water shortage era' in the Western United States has officially arrived," Xinhua News Agency reported in Los Angeles on August 18.[2] The Colorado River[3] originates in the Rocky Mountains of Colorado in the United States, with a length of more than 2,300 kilometers. Its main stream flows through Utah, Arizona, Nevada, California and Mexico, and finally empties into the Pacific Ocean. The Colorado River forms the largest water system in the Western United States -- known as the "lifeline of the Southwest" because it flows through vast arid and semi-arid areas.

<!-- b000052 | caption | pages [3] -->
Figure 1: U.S. Drought Monitor on February 15, 2022[4]

<!-- b000053 | prose | pages [3] -->
As can be seen from the Figure 1, the drought in the western United States has been severe. Actually, as early as the summer of 2021, it was reported[1] that lake Mead, the Hoover Dam that provides water to 25 million people in western States, was at historically low levels On June 9, the water level dropped to 1,071.57 feet, breaking the previous record low set in 2016. Climate change has reduced the amount of snow flowing into the Colorado River and its tributaries; Warmer temperatures are also making soil thirstier and increasing evaporation as rivers flow through arid areas of the western United States.

<!-- b000054 | prose | pages [3] -->
In the western part of the United States, in the Colorado River basin, two artificial lakes, the Lake Powell and Lake Mead, correspond to two dam (Glen Canyon and Hoover Dam) reservoirs. Water from the two dams is needed to meet the water and electricity demands of five U.S. states, Arizona (AZ), California (CA), Wyoming (WY), New Mexico (NM), and Colorado (CO), with extra water flowing into Mexico from the Colorado River into the Gulf of California.

<!-- b000055 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000056 | prose | pages [3, 4] -->
The strained distribution of water affects competing interests in various regions. Through the analysis and investigation of the background and negotiators’ guidance of the problem, the restate of the problem can be expressed as follows: ⚫Build a mathematical model to solve the problem of water allocation under the condition of fixed supply and demand conditions.

<!-- b000058 | prose | pages [4] -->
✓Given the initial water level of the two lakes, figure out how much water should be drawn from each lake to meet the water and electricity demands.

<!-- b000059 | prose | pages [4] -->
✓In the absence of additional water supply, and the demands are fixed, solve for the maximum maintenance time that the demands can be met.

<!-- b000060 | prose | pages [4] -->
✓Figure out how much additional water must be supplied overtime to ensure that these fixed demands are met. ⚫Establish a model to determine the allocation of water for general (Agricultural, Industrial, Residential) usage and electricity production among five states, and describe the criteria for resolving competing interests. ⚫Based on the model, improve the solution in the case of water shortage, so that it can meet all the water and electricity demands. ⚫Analyze the changes in model results according to the following situations:

<!-- b000061 | prose | pages [4] -->
✓As the demands for water and electricity change over time, population, agricultural, and industrial change.

<!-- b000062 | prose | pages [4] -->
✓The initial value of renewable energy technologies increases.

<!-- b000063 | prose | pages [4] -->
✓Measures are taken to save water and electricity. ⚫Summarize the findings and prepare a one - to two-page article to submit to Drought and Thirst magazine.

<!-- b000064 | heading | pages [4] -->
1.3 Our Work

<!-- b000065 | prose | pages [4] -->
The problem requires us to work out a reasonable allocation plan for water and electricity demands of three categories of objects (industrial, agricultural and residential) in five states, and for different environmental conditions, considering the needs of Mexico. Our main work is as follows: 1) In the case of a certain demand, the Water and Electricity Transportation Model is established by analyzing the transportation of water and electricity and the water transferred between two lakes.

<!-- b000066 | prose | pages [4] -->
Figure out the daily supply of water for the two lakes, the maximum maintenance time without additional water, and the additional water needed to meet demands. 2) The Coordinated Development of multi-objective Programming Model is established by considering the water and electricity demands of industry, agriculture and residents from three perspectives of society, economy and environment. The distribution of water and electricity when water resource is sufficient and water resource is tight is analyzed respectively. 3) Based on the above two models, the Mexican Allocation Model is established to consider the distribution of Mexico's interests. 4) The sensitivity of the model was analyzed from the perspectives of demand and renewable Energy Technologies.

<!-- b000067 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000068 | prose | pages [5] -->
In order to build the mathematical model to solve the problems, we make the following supplementary assumptions on the basis of the problem, following a reasonable explanation for each

<!-- b000069 | heading | pages [5] -->
assumption

<!-- b000070 | prose | pages [5] -->
⚫ Lake Powell and Lake Mead are the reservoirs of Glen Canyon dam and Hoover Dam, respectively. These two lakes are artificial lakes and the distance between the reservoir and the dam is very close. Due to the theory of communicating vessels, the lake water height can be considered as the water height of the upstream of the dam, and the error can be ignored. ⚫ The dam will not overflow due to conditions such as a breach. The main trend of climate change is the decrease of precipitation and the increase of temperature, and water resources are strained, so the overflow situation is not considered. ⚫ The lowest water level for power generation is the lowest water level allowed by the reservoir.

<!-- b000071 | prose | pages [5] -->
After a data search, we set the lowest water level at 3,490 feet for Lake Powell and 950 feet for Lake Mead.

<!-- b000072 | prose | pages [5] -->
⚫ The supply of electricity in the states is only hydroelectric. In order to simplify the model and reduce the burden of data search, only hydroelectric power is considered. ⚫ The water can be reused, and all the water that flows through the dam generates electricity.

<!-- b000073 | prose | pages [5] -->
Based on resource reusability, this assumption is more realistic. ⚫ Consider the effects of rainfall, temperature changes, and river evaporation. Climate change has reduced the amount of snow flowing into the Colorado River and its tributaries; Warmer temperatures are also making soil thirstier and increasing evaporation as rivers flow through arid areas of the western United States. The consideration of evaporation is necessary and reasonable. ⚫ The water transferred from Lake Powell into Lake Mead and then supplied to users is deemed to belong to Lake Mead. ⚫ The supply of water depends on rivers. In practice, each region follows the "proximity principle" for water resources, that is, only the main stream or tributaries flowing through the region can be used for water. Electricity transportation is related to the geography of the five states. ⚫ Electrical energy is lost because of the thermal power generated by the resistance of the wire.

<!-- b000074 | prose | pages [5] -->
Transporting electricity from the same dam causes states farther from the dam to generate more power and lose more than states closer to the dam. As the state Wyoming is far from the dam, it is necessary to consider the power loss.

<!-- b000075 | heading | pages [5] -->
3 Notations

<!-- b000076 | prose | pages [5] -->
The important symbols used in this article and their meanings are shown in Table 1. There are some variables that are not listed here and will be discussed in detail in each section.

<!-- b000077 | caption | pages [5] -->
Table 1: Important Symbols and Descriptions

<!-- b000078 | heading | pages [5] -->
Symbol

<!-- b000079 | prose | pages [5, 6] -->
Description l The height of the water level of a reservoir v Volume of water in a reservoir

<!-- b000081 | prose | pages [6] -->
W Total volume of water supply suply

<!-- b000082 | prose | pages [6] -->
Volume of water supplied from Reservoir i to State W j j = ( 1,2, ,5) ij

<!-- b000083 | prose | pages [6] -->
W Volume of water lost through transport loss

<!-- b000084 | prose | pages [6] -->
Electricity demand (transferred to the volume of water) in D j j = w State ( 1,2, ,5) j

<!-- b000085 | prose | pages [6] -->
j j = D Water demand in State ( 1,2, ,5) je

<!-- b000086 | prose | pages [6] -->
Supply for m (water or electricity) from source i to k k = ( 1,2,3) object (industrial, agricultural and km ijx j j = residential) of State ( 1,2, ,5)

<!-- b000087 | prose | pages [6] -->
Demand for m (water or electricity) of object k k = ( 1,2,3) (industrial, agricultural and residential) in km D j j j = State ( 1,2, ,5)

<!-- b000088 | heading | pages [6] -->
4 Model Preparation

<!-- b000089 | heading | pages [6] -->
4.1 Data Collection

<!-- b000090 | prose | pages [6] -->
The problem doesn't give us data, so we need to collect data to build a model. To analyze the problem, we need to collect data on two lakes and dams, as well as the water and electricity demands of agriculture, industry and residential use in five states. After the data is collected, certain processing and analysis are carried out to prepare for the subsequent model establishment.

<!-- b000091 | prose | pages [6] -->
The official websites of the two lakes and dams provide us with a lot of data about the dams. Detailed data sources are shown in the Table 2 below. (Additional data sources are included in the Reference.)

<!-- b000092 | caption | pages [6] -->
Table 2: Partial Data Sources

<!-- b000093 | prose | pages [6] -->
Database Names Database Websites

<!-- b000094 | prose | pages [6] -->
Lake Powell http://lakepowell.water-data.com/

<!-- b000095 | prose | pages [6] -->
Lake Mead http://lakemead.water-data.com/

<!-- b000096 | prose | pages [6] -->
Electricity Consumption https://www.eia.gov/electricity/state/

<!-- b000097 | heading | pages [6] -->
4.2 Relationship between Water Level and Storage Volume

<!-- b000098 | prose | pages [6, 7] -->
Lake Powell and Lake Mead are the reservoirs of Glen Canyon Dam and Hoover Dam respectively. The higher the elevation of the lake, the larger the content of the reservoir. After analyzing and studying the water level of the two lakes in the past 12 months (data sources are shown in the Table 1), we conclude that there is a linear correlation between the elevation and content of the lakes.

<!-- b000100 | prose | pages [7] -->
Therefore, we perform polynomial fitting analysis on elevation and content, and the steps are as follows:

<!-- b000101 | prose | pages [7] -->
Step1: Take a set of data points, including m, as sample points

<!-- b000102 | prose | pages [7] -->
{( , l v )( , l v ) ( , ) l v ( , l v )} (1) 1 1 2 2 i i m m

<!-- b000103 | prose | pages [7] -->
= where ( il i 1,2, , m ) represents the height of the water level of a reservoir corresponding to the sample = = iv i ( 1,2, , m ) point ( i i 1,2, , m ) , namely the elevation of the lake; represents the volume of water in a reservoir, namely the content of the lake.

<!-- b000104 | prose | pages [7] -->
Step2: Use polynomial for curve fitting − − = + + + + + n n 1 n 2 ˆ v a l a l a l a l a (2) − 0 1 2 n 1 n

<!-- b000105 | prose | pages [7] -->
n degree polynomial; ˆv is the predicted value. th na represents fitting coefficient, stands for where Step3: Calculate the sum of squares of residuals

<!-- b000106 | prose | pages [7] -->
m   = − 2 ˆ( v v ) (3) i i = i 1

<!-- b000107 | prose | pages [7] -->
We use MATLAB for polynomial fitting of elevation and content, and the results are as follows

<!-- b000108 | caption | pages [7] -->
Figure 2: The fitting curves of Lake Powell ( Left ) and Lake Mead ( Right )

<!-- b000109 | prose | pages [7] -->
After many times of curve fitting, we find that the fitting effect of quadratic polynomial is more ideal. As can be seen from Figure 2, sample points of Lake Powell and Lake Mead are relatively close to the fitting curve. The relationship between water level and volume of the two reservoirs is as follows = − + 2 6 9 v 224.26 l 1.5157*10 l 2.5622*10 powell (4) = − + 2 5 8 v 338.64 l 6.719*10 l 3.4155*10 mead

<!-- b000110 | prose | pages [7] -->
We verify the function by comparing the predicted value with the actual value. According to Wikipedia, Lake Powell[5] is 3,700 feet above sea level and has an active capacity of 20,876,000 acre-feet with a fitting value of 24,229,400 acre-feet; Lake Mead[6] has an elevation of 1221.4 feet and an effective capacity of 26,120,000 acre-feet with a fitting value of 26,080,000 acre-feet. From the numerical point of view, the fitting effect is ideal.

<!-- b000111 | heading | pages [8] -->
5 Model I: Water and Electricity Transportation Model

<!-- b000112 | heading | pages [8] -->
5.1 Basic Ideas

<!-- b000113 | prose | pages [8] -->
In the basin of the Colorado River, Lake Powell and Lake Mead are two water clusters. The two lakes are at higher elevations and water can flows from them to the surrounding areas. Additionally, Lake Mead has a higher elevation than Lake Powell. So the water flows from the Glen Canyon Dam (Lake Powell) to the Hoover Dam (Lake Mead) and eventually to the Gulf of California.

<!-- b000114 | prose | pages [8] -->
The geographical map is shown in Figure 3.

<!-- b000115 | caption | pages [8] -->
Figure 3: Geographic map[3]

<!-- b000116 | prose | pages [8] -->
Demands includes water demand and electricity demand, which includes agriculture, industry and residents in five states.

<!-- b000117 | prose | pages [8] -->
1. Water supply: It is assumed that each region draws water from the river that flows through it, and this water can be traced back to Lake Powell or Lake Mead. Among them, part of the water of Lake Powell will be supplied to users after flowing into Lake Mead, which is regarded as belonging to Lake Mead. In the process of water transportation, the hydraulic loss caused by evaporation is mainly considered.

<!-- b000118 | prose | pages [8] -->
2. Electricity supply: hydroelectric power is to convert the potential energy of water into mechanical energy and then into electrical energy. Similarly, we can also transform the loss of electric power in the transmission process into the loss of water potential energy, thus producing constraints on reservoir stock.

<!-- b000119 | prose | pages [8] -->
The problem is thus simplified to two lakes distributing water resources to the five continents. The distribution of the three industries (agriculture, industry and resident) will be discussed in detail in the Section 6.

<!-- b000120 | prose | pages [8] -->
In the case of water demand and electricity demand are certain, we can make a reasonable allocation of water resources through Transportation Model.

<!-- b000121 | heading | pages [9] -->
5.2 Establishment of Transportation Model

<!-- b000122 | heading | pages [9] -->
5.2.1 Objective Function

<!-- b000123 | prose | pages [9] -->
In order to make full use of water resources, we hope that the water supply from the two dams will meet the water and electricity demands of each state while providing as little water as possible

<!-- b000124 | prose | pages [9] -->
2 5 = = + min W W W W (5) suply 1 2 ij = = i 1 j 1

<!-- b000125 | prose | pages [9] -->
W is the water supply from the Glen Canyon W where represents the total volume of water supply, 1 suply W is the water supply from the Hoover dam. W means the volume of water supplied from dam, and 2 ij i i = j j = Reservoir ( 1,2) to State ( 1,2, ,5) . If there is no corresponding river flowing through, then W = 0 . ij

<!-- b000126 | prose | pages [9] -->
W For a lake, water supply can be divided into two types: water supplied directly without the dam , iup i = represents the Glen Canyon dam, i = W 1 2 and water supplied through the dam . ( represents the idown Hoover dam).

<!-- b000127 | prose | pages [9] -->
Considering that some water will flow to Lake Mead after Glen Canyon dam, we set the volume of  , where  is a proportional parameter. Additionally, it is W this part of transferred water as 1down W after being transferred. assumed that the transferred water is included in Lake Mead's water supply 2 Thus, the water supply can be expressed as follows = + −  + + W W (1 ) W W W suply 1 up 1 down 2 up 2 down (6) 2  = + −  ( W W ) W iup idown 1 down = i 1

<!-- b000128 | prose | pages [9] -->
W For dam i , includes the water provided to users by lake i after the dam, which is constrained idown D and electricity demand D , namely by users' water demand (transferred to the volume of water) e w  + W max{ D D } (7) idown e w

<!-- b000129 | prose | pages [9] -->
The relationship between water and electricity conversion and the loss of water and electricity during transportation will be discussed in detail in Section 5.2.3.

<!-- b000130 | heading | pages [9] -->
5.2.2 Supply constraints

<!-- b000131 | prose | pages [9] -->
The water supply must not exceed the minimum level of the reservoir, otherwise there will be no electricity supply. It is assumed that the lowest water level is the minimum content of reservoir.

<!-- b000132 | prose | pages [9] -->
Therefore, the water supply by Glen Canyon dam  W Q (8) 1 G

<!-- b000133 | prose | pages [9] -->
W represents the water supplied by the Glen Canyon dam, and Q represents the reservoir where, 1 G content of the Glen Canyon dam.

<!-- b000134 | prose | pages [9, 10] -->
For Hoover Dam, its water supply  +  W Q W (9) 2 H 1 down

<!-- b000136 | prose | pages [10] -->
W represents the water supplied by the Hoover Dam, and Q represents the reservoir content of where, 2 G  is the water transferred form Glen Canyon dam to Hoover Dam.  is a W the Hoover Dam. 1down parameter, which indicating the loss of water during the transportation (the details are discussed Section 5.2.3)

<!-- b000137 | caption | pages [10] -->
Figure 4: Schematic diagram

<!-- b000138 | heading | pages [10] -->
5.2.3 Demand constraints

<!-- b000139 | prose | pages [10] -->
Demands are divided into water demand and electricity demand. Our solution needs to meet both needs on five continents. ⚫ Electricity demand When the volume of water in the reservoir is small, the corresponding water flow will decrease. When the water level is low enough, it can even shut down power generation.

<!-- b000140 | prose | pages [10] -->
For hydraulic power generation, the formula[7] of translational power of turbines is as follows

<!-- b000141 | prose | pages [10] -->
= =  +    E f W ( ) ( )( V g h t ) (10)

<!-- b000142 | prose | pages [10] -->
where E is electric energy and W is the volume of the water, which means the relationship between Potential energy and electric energy of water.  +  is the coefficient of efficiency (a unitless, scalar coefficient, ranging from 0 for completely inefficient to 1 for completely efficient).  represents the function of the renewable energy technologies enhancement.  is the density of water. V is the  is the change in height. t  represents the volumetric flow rate. g is acceleration due to gravity. h working time.

<!-- b000143 | prose | pages [10] -->
The generation height difference is the current water level minus the lowest water level.

<!-- b000144 | prose | pages [10] -->
 = − h P P 1 min (11)  = − h M M 2 min

<!-- b000145 | prose | pages [10, 11] -->
P where P is water level in Lake Powell, is the lowest generating water level of the Glen Canyon dam, min M M is water level in Lake Mead, and is lowest generating water level of the Hoover dam. min

<!-- b000147 | prose | pages [11] -->
The electrical energy will be lost during transmission due to the resistance of the wire   2 I ' L t ij i = E (12) loss s ij

<!-- b000148 | prose | pages [11] -->
Thus, additional water supply is available because of the loss of electrical energy, which is denoted W by . For electricity, supply needs to meet demand, expressed as follows eloss

<!-- b000149 | prose | pages [11] -->
2 2   −  W W D (13) down eloss e ij ij j = = i 1 i 1

<!-- b000150 | prose | pages [11] -->
W where can be obtained by combining the Formula (10,12). eloss

<!-- b000151 | prose | pages [11] -->
⚫ Water demand The transportation of water depends mainly on river systems. Rivers are largely exposed to sunlight and are greatly affected by evaporation. Evaporation is greatly affected by temperature. Therefore, the loss of water during transportation can be expressed as follows

<!-- b000152 | prose | pages [11] -->
 Td =  (14) W W ij wloss ij ij

<!-- b000153 | prose | pages [11] -->
 Td j j =  W represents the volume of water supplied from Reservoiri to State ( 1,2, ,5) where , and is ij ij the evaporation coefficient affected by temperature.  and  are parameters. T is the temperature. d is ij the distance from Reservoiri to State j .

<!-- b000154 | prose | pages [11] -->
It is assumed that the water will still be available to users after the electricity is generated. Therefore, the transport loss of water and electricity should be considered comprehensively when considering the provision of water = + (15) W W W loss wloss eloss ij ij ij

<!-- b000155 | prose | pages [11] -->
For water, supply needs to meet demand, expressed as follows

<!-- b000156 | prose | pages [11] -->
2 2   −  W W D (16) down loss w ij ij j = = i 1 i 1

<!-- b000157 | heading | pages [11] -->
5.2.4 The model summary

<!-- b000158 | prose | pages [11] -->
By summarizing the objective function and constraint equation above, we can get the following water and electricity transportation model.

<!-- b000159 | prose | pages [11] -->
2 5 = W W min (17) suply ij = = i 1 j 1

<!-- b000160 | prose | pages [11] -->
st. .

<!-- b000161 | prose | pages [12] -->
 2  = + −  W ( W W ) W  suply iup idown 1 down  = i 1  +  W max{ D D } idown e w   W Q  1 G   +  W Q W  2 H 1 down (18) 2 2    −  W W D  down eloss e ij ij j = = i 1 i 1  2 2    −  W W D  down loss w ij ij j = = i 1 i 1   W 0  ij

<!-- b000162 | prose | pages [12] -->
See the Formula (6-16) for a symbolic explanation.

<!-- b000163 | heading | pages [12] -->
5.3 Maintenance Time Calculation Algorithm

<!-- b000164 | prose | pages [12] -->
In order to solve the maximum maintenance time without additional water, we designed an algorithm to calculate the maintenance time.

<!-- b000165 | prose | pages [12] -->
The idea of this algorithm is to repeatedly iterate Model One to solve how long the water in two reservoirs can last without considering the external water supply.

<!-- b000166 | prose | pages [12] -->
The pseudo-code for the algorithm is as follows:

<!-- b000167 | heading | pages [12] -->
Algorithm: Maintenance Time Calculation Algorithm

<!-- b000168 | prose | pages [12] -->
P M W i [ ][ ] j , demand, n←0 Input: P , M , , , min min

<!-- b000169 | prose | pages [12] -->
Output: n 1  /*calculate the height and volume of water in the reservoirs base based 2  on the fitting function*/

<!-- b000170 | prose | pages [12] -->
P M 3  while P ≥ or M ≥ do min min

<!-- b000171 | prose | pages [12] -->
4 n ⟵n + 1;

<!-- b000172 | prose | pages [12] -->
5    cost ⟵ 0;

<!-- b000173 | prose | pages [12] -->
6 for i←0 to 1 do 7        for j←0 to 4 do if demand> 0 then 8 W i [ ][ ] j ∗𝛼 + E[i][j]∗𝛽; cost ← cost + 9

<!-- b000174 | prose | pages [12] -->
W i [ ][ ] j ∗(1 −𝛼) −E[i][j]∗(1 −𝛽); demand ← demand− 10

<!-- b000175 | prose | pages [12, 13] -->
11       end 12    end 13    if cost = min{cost} then P ←P which is calculated based on the volume 14

<!-- b000177 | prose | pages [13] -->
M M ← which is calculated based on the volume; 15 min

<!-- b000178 | prose | pages [13] -->
16  end

<!-- b000179 | prose | pages [13] -->
The parameters to be input are: the initial water level heights P and M of the two reservoirs, and P M the lowest power level heights and . W is a matrix, and if there is no viable waterway from min min W i [ ][ ] j is initialized to 0. Demand D. The number of days n persisted is reservoir i to state j , then initialized to 0.

<!-- b000180 | prose | pages [13] -->
The parameters in the model are: calculated waterway transport loss α, calculated circuit transmission loss β, W matrix element represents the amount of water transported from reservoir i to state j, similarly, E matrix element codes the amount of electricity generated from reservoir i to state j .

<!-- b000181 | prose | pages [13] -->
Solution and output of the model: According to Model One, the reservoir water consumption required to meet the demand and guarantee the minimum loss can be obtained each time. The corresponding water level of the reservoir is calculated according to the fitting curve. If the water level of both reservoirs is lower than the lowest power generation water level, it indicates that the reservoirs can no longer provide electricity, that is, they can no longer meet the demand. The algorithm exits, and the number of days n is output.

<!-- b000182 | heading | pages [13] -->
5.4 Calculation Results

<!-- b000183 | heading | pages [13] -->
5.4.1 The water drawn from each lake

<!-- b000184 | prose | pages [13] -->
= P 3600 feet We assign values to the initial water levels of Lake Powell and Lake Mead. and = M 1210 feet .Based on past data, we assume that water demand is 43,411 million gallons and electricity demand is 1,073 gigawatt hours.

<!-- b000185 | prose | pages [13] -->
We analyzed the problem on a daily basis. Using the model, we get a total water supply of 59,467 million gallons. The water should be drown from Lake Mead: 41,602 million gallons, The water should be drown from Lake Powell: 17,865 million gallons.

<!-- b000186 | prose | pages [13] -->
After a day of use, the water level of the two lakes changed by 0.45 feet and 1.55feet respectively. The results are reasonable.

<!-- b000187 | heading | pages [13] -->
5.4.2 Maintenance time

<!-- b000188 | prose | pages [13] -->
In the absence of additional water supplies (e.g. rainfall, etc.), water levels will decrease over time. When the water level drops to the lowest generating level, the reservoir can no longer provide electricity, that is, it cannot meet the demand. The maximum maintenance time is from the initial water level to the lowest water level.

<!-- b000189 | prose | pages [13] -->
On the basis of the previous result, combined with Model One and Maintenance time Calculation algorithm, the solution is obtained as 63 days.

<!-- b000190 | heading | pages [13] -->
5.4.3 Additional water

<!-- b000191 | prose | pages [13, 14] -->
Additional water is needed to keep the supply system going when it reaches a critical state where demand cannot be met. At this point, the demand is certain, and the water in the reservoir is a constant value, equivalent to the supply of water is the additional water, so there is little difference in the results. The difference is that the model is based on time lines, and the actual temperature we consider will lead to different evaporation losses, so the actual amount of additional water that needs to be replenished will also be different. The calculation results are shown in the figure below:

<!-- b000193 | caption | pages [14] -->
Figure 5: The result of additional water

<!-- b000194 | prose | pages [14] -->
The amount of water that needs to be replenished is positively correlated with temperature, and the higher the temperature, the higher the loss, and the more additional water needs to be replenished.

<!-- b000195 | heading | pages [14] -->
6 Model II: Coordinated Development of Multi-objective

<!-- b000196 | heading | pages [14] -->
Programming Model

<!-- b000197 | prose | pages [14] -->
Model Two is a further improvement on Model One. In model One, we only distribute the water supply and electricity supply among each state. In Model Two, we take into account the proportion of water consumption by industry, agriculture and residents.

<!-- b000198 | heading | pages [14] -->
6.1 The Establishment of Multi-objective Programming Model

<!-- b000199 | heading | pages [14] -->
6.1.1 Objective function

<!-- b000200 | prose | pages [14] -->
The proportion of water and electricity used by industry, agriculture and residents will ultimately have social, economic and environmental implications.[8] Our goal is to harmonize social, economic and environmental development. The social, economic and environmental conditions correspond to the situation before, during and after the use of water. Electricity before and during use corresponds to this society and economy respectively. ➢ Social effect refers to the lack of water (or electricity) when the demand is not met. In other words, the social benefit refers to the negative effect caused by the lack of water (or electricity). When there is no water shortage, social benefits are not considered in the objective function. ➢ Economic effect refers to the industrial output from water (or electricity). The supply for industry, agriculture and residents in an area affects the economic situation of the area to varying degrees. ➢ Environmental effect refers to the amount of pollutants that water brings with it after use. From the perspective of environmental sustainability, we want the total amount of pollutants to be as small as possible.

<!-- b000201 | prose | pages [15] -->
= F opt f x [ ( ), f ( ), x f x ( )] (19) 1 2 3

<!-- b000202 | prose | pages [15] -->
x k = kf ( )( 1,2,3) where, correspond to social, economic and environmental implications respectively.

<!-- b000203 | prose | pages [15] -->
Water supply and demand affect all three effects simultaneously, whereas electricity supply and demand affect only the social effect and economic effect.

<!-- b000204 | prose | pages [15] -->
f x 1( ) ⚫ Social effect

<!-- b000205 | prose | pages [15] -->
i = i = There are three main sources of water supply: Glen Canyon dam ( 1) , Hoover Dam ( 2) and i = i = rainfall ( 3) . There are two sources of electricity supply: Glen Canyon dam ( 1) and Hoover Dam i = ( 2) .

<!-- b000206 | prose | pages [15] -->
When the supply cannot meet the demand, the water (or electricity) shortage is the quantity demanded minus the supply. We want the social effect to be as small as possible.

<!-- b000207 | prose | pages [15] -->
I m ( ) 2 3 5   = − − km km max f x ( ) min [ D x ] (20) 1 j ij = = = = m 1 k 1 j 1 i 1

<!-- b000208 | prose | pages [15] -->
m = m = k = km 1 2 ) of object k (industrial 1 where is the demand for m (water or electricity , D j k = k = ) in State ( m = or j j = 2 3 km 1 1,2, ,5) agricultural and residential , is the supply for m (water ijx m = k = k = k = 2 ) to object k (industrial 1 2 3 electricity , agricultural and residential ) of State j j = ( 1,2, ,5) .

<!-- b000209 | prose | pages [15] -->
f 2( ) x ⚫ Economic effect

<!-- b000210 | prose | pages [15] -->
The economy mainly includes the value of water (or electricity) brought by water resources, and the benefits brought by the utilization of water (or electricity).

<!-- b000211 | prose | pages [15] -->
The value of water (or electricity) brought by water resources is directly reflected in the charging system of hydropower, which is expressed by the charging coefficient c . The benefits brought by the utilization of hydropower are expressed by the benefit coefficient b . For example, for a factory, its utilities can be reflected in the charging coefficient, its profit can be reflected in the benefit coefficient.

<!-- b000212 | prose | pages [15] -->
I m ( ) 2 3 5  = −  km km km m km m max f ( ) x max ( b c ) x w (21) 2 ij ij ij ij j j = = = = m 1 k 1 j 1 i 1

<!-- b000213 | prose | pages [15] -->
 km km km m where, is the benefit coefficient, is the charging coefficient, is the supply, is the order ijb ijc ijx ij  km m coefficient, is the fairness coefficient and is the regional tradeoff coefficient. w j j

<!-- b000214 | prose | pages [15] -->
The influence of three economic factors: the supply difference in different regions, the demand difference in different regions, and the demand difference in different industries in the same region.

<!-- b000215 | prose | pages [15, 16] -->
The influence of water evaporation and power loss in the process of electric transportation are both constrained by distance. Each state is located at a different distance from the two dams, which determines the different priority of the two dams’ supply to the five states, expressed by order coefficient . The three types of objects (industry, agriculture and residents) are the three types of fixed demand groups of hydropower resources. Their demands are different, and the difference of their demand proportion is represented by fairness coefficient . The distribution of resources among the five states is expressed as regional tradeoff coefficient w.

<!-- b000217 | prose | pages [16] -->
The specific acquisition and method of the three coefficients will be introduced in detail in Section 6.2 combined with examples.

<!-- b000218 | prose | pages [16] -->
f 3( ) x ⚫ Environmental effect

<!-- b000219 | prose | pages [16] -->
After the use of water, there will be a large number of sewage discharge containing important pollutants (such as COD, BOD)[9], which will have a negative impact on the environment, such as the destruction of the ecosystem. The smaller the environmental effect, the better.

<!-- b000220 | prose | pages [16] -->
3 5 3   = − k k k max f x ( ) min d p x (22) 3 j j ij = = = k 1 j 1 i 1

<!-- b000221 | prose | pages [16] -->
k k = k ( 1,2,3) where jp is the pollutant emission coefficient of object (industrial, agricultural and j j = k residential) in State ( 1,2, ,5) , and d is the content of important pollutants (mg/L) in the amount j k k = ( 1,2,3) of water discharged by object (industrial, agricultural and residential) in State j j = ( 1,2, ,5) .

<!-- b000222 | heading | pages [16] -->
6.1.2 Constraints

<!-- b000223 | prose | pages [16] -->
The constraints of supply and demand can be followed by Model One, with some additional constraints due to the inclusion of social, economic and environmental factors in Model Two. ⚫ Demand constraint

<!-- b000224 | prose | pages [16] -->
Users will have maximum and minimum demand for water. Maximum demand refers to the maximum output of production capacity, that is, to achieve the maximum satisfaction of users. Minimum demand is what the user needs to maintain basic operations.

<!-- b000225 | prose | pages [16] -->
When the supply is greater than the maximum demand, it will cause the waste of resources. When the supply is less than the minimum demand, demand is not guaranteed. So, the supply and demand constraints are as follows

<!-- b000226 | prose | pages [16] -->
3    k k k D x D (23) j min ij j max = i 1

<!-- b000227 | prose | pages [16] -->
⚫ Pollutant constraint

<!-- b000228 | prose | pages [16] -->
The discharge of pollutants cannot exceed the maximum allowable total amount of pollutants

<!-- b000229 | prose | pages [16] -->
3 5 3    k k k k d p x M (24) j j ij max = = = k 1 j 1 i 1

<!-- b000230 | prose | pages [16, 17] -->
k k = k ( 1,2,3) where jp is the pollutant emission coefficient of object (industrial, agricultural and j j = k residential) in State ( 1,2, ,5) , and d is the content of important pollutants (mg/L) in the amount j k k = ( 1,2,3) of water discharged by object (industrial, agricultural and residential) in State j j = k ( 1,2, ,5) M . is the maximum allowable total amount of contaminants, and the value is 5989kg max (total COG/day)[9].

<!-- b000232 | heading | pages [17] -->
6.1.3 The model summary

<!-- b000233 | prose | pages [17] -->
By summarizing the objective function and constraint equation above, we can get the following coordinated development multi-objective programming model.

<!-- b000234 | prose | pages [17] -->
= obj F X . ( ) opt f x [ ( ), f ( ), x f ( )] x 1 2 3   I m ( ) 2 3 5   = − − km km max f x ( ) min [ D x ]   1 j ij   = = = = m 1 k 1 j 1 i 1   (25) I m ( ) 2 3 5  = = −  km km km m km m max f ( ) x max ( b c ) x w   2 ij ij ij ij j j   = = = = m 1 k 1 j 1 i 1   I m ( ) 3 5     = − k k k max f ( ) x min d p x 3 j j ij   = = = k 1 j 1 i 1

<!-- b000235 | prose | pages [17] -->
st. .

<!-- b000236 | prose | pages [17] -->
  W Q 1 G   +  W Q W  2 H 1 down  3    k k k D x D  j min ij j max (26) = i 1  3 5 3     k k k k d p x M j j ij max  = = = k 1 j 1 i 1   k x 0  ij

<!-- b000237 | prose | pages [17] -->
See the Formula (8-24) for a symbolic explanation. More parameters are determined in the Section 6.2.

<!-- b000238 | heading | pages [17] -->
6.2 Parameters to Determine

<!-- b000239 | prose | pages [17] -->
Due to the limitation of paper space, it is impossible to list every case. Therefore, we take California as an example to explain the determination of each parameter in the model.

<!-- b000240 | prose | pages [17] -->
f 2( ) x

<!-- b000241 | heading | pages [17] -->
6.2.1 Parameters in economic effect

<!-- b000242 | prose | pages [17] -->
f 2( ) x : Benefit coefficient km There are five parameters in economic effect , Charging coefficient ijb   km m km m , Order coefficient , Fairness coefficient , and Regional tradeoff coefficient w . ijc ij j j

<!-- b000243 | prose | pages [17] -->
km ⚫ Benefit coefficient ijb

<!-- b000244 | prose | pages [17] -->
The benefits brought by the utilization of hydropower are expressed by the benefit coefficient.

<!-- b000245 | prose | pages [17] -->
The benefit coefficient of industrial and agricultural water (or electricity) can be determined by the reciprocal of the water (or electricity) demand of output value. According to the data we checked[11,12], we can get:

<!-- b000246 | caption | pages [18] -->
Table 3: Benefit coefficient of industry and agriculture

<!-- b000247 | prose | pages [18] -->
Benefit Benefit Total output value Total water volume Total Object coefficient(water) coefficient(electricity) /million dollars /million gallons electricity/KMWh dollars/gallons dollars/KWh

<!-- b000248 | prose | pages [18] -->
Industry 9,025,218 19183 47631.5 470.48 189.48

<!-- b000249 | prose | pages [18] -->
Agriculture 196037.6 399 6804.5 491.3223 28.80999

<!-- b000250 | prose | pages [18] -->
Domestic water (electricity) coefficient is generally difficult to have a clear value[8], in order to ensure the supply, we give a large value according to the Table 3. The benefit coefficient of water is 550 dollars/gallons, and the benefit coefficient of electricity is 200 dollars/kwh.

<!-- b000251 | prose | pages [18] -->
km ⚫ Charging coefficient ijc

<!-- b000252 | prose | pages [18] -->
The value of water and electricity brought by water resources is directly reflected in the charging system of hydropower, which is expressed by the charging coefficient.

<!-- b000253 | prose | pages [18] -->
The charging coefficient can be determined by the California unit price of water and electricity[13,14,15].

<!-- b000254 | caption | pages [18] -->
Table 4: Charging coefficient of three objects

<!-- b000255 | prose | pages [18] -->
Industry Object Agriculture Residents Water price 3.77 2.12 5.85 (dollars/gallons） Electricity price 8.16 17.5 15.98 (cents/KWh）

<!-- b000256 | prose | pages [18] -->
 m ⚫ Order coefficient ij

<!-- b000257 | prose | pages [18] -->
The different priority of the three water sources’ supply to the five states, expressed by order coefficient.

<!-- b000258 | prose | pages [18] -->
The conversion of water (or electricity) use priority to order coefficient can be obtained from the following transformation relationship[8]:

<!-- b000259 | prose | pages [18] -->
+ − m m 1 n n max j ij  = m (27) ij I m ( )  + − m m (1 n n ) max j ij = i 1

<!-- b000260 | prose | pages [18] -->
m = (or electricity m = 1 2 m where, n represents the conversion of water ) use priority. ij

<!-- b000261 | prose | pages [18] -->
i = 1 For a given state, water is provided from three sources: Glen Canyon dam ）, Hoover Dam （ i = i = 2 3 ）, and rainfall ）. As the increase of transport distance will cause the loss of water due to （ （ evaporation, the priority is determined by distance. For California, rainfall is available in a very short period of time, and its distance to Hoover Dam is less than Glen Canyon dam. Therefore, the priority = = = respectively.  1 1 1 1 degree is rainfall first, Hoover second, and Glenn last, denoted by n 3, n 2, n 1 1 j 2 j 3 j ij (water) are 1/3, 1/2, 1/6 respectively.

<!-- b000262 | prose | pages [18, 19] -->
i = i = 1 2 Electricity comes from two sources: Glen Canyon dam ） and Hoover Dam ）. As the （ （ increase of transportation distance will cause loss due to power loss, its priority is also determined by the distance. The degree of priority is: Hoover is the first, Glenn is the second, respectively expressed by = = , it is obtained that  (electricity) are 1/3, 2/3 respectively. 2 2 1 n 2, n 1 1 j 2 j ij

<!-- b000264 | prose | pages [19] -->
 km ⚫ Fairness coefficient j

<!-- b000265 | prose | pages [19] -->
Their demands are different, and the difference of their demand proportion is represented by fairness coefficient.

<!-- b000266 | prose | pages [19] -->
+ − km km 1 n n max j  = km (28) j 3  + − km km (1 n n ) max j = k 1

<!-- b000267 | prose | pages [19] -->
Water demand priority[16]: residential water first, agricultural water second, industrial water last, = = = . Substitute into the formula, and the water use fairness 11 21 31 corresponding to the order: n 3, n 2, n 1 j j j coefficients are 1/3, 1/2, 1/6 respectively.

<!-- b000268 | prose | pages [19] -->
Priority of electricity demand[17]: agricultural electricity consumption occupies a small part of electricity consumption, so we give priority to domestic electricity consumption, followed by industrial electricity consumption, and agricultural electricity consumption last. Corresponding:

<!-- b000269 | prose | pages [19] -->
= = = , plug into the formula, and the electricity fairness coefficient is 1/3, 1/6, 1/2, 11 21 31 n 2, n 3, n 1 j j j respectively.

<!-- b000270 | prose | pages [19] -->
m ⚫ Regional tradeoff coefficient w j

<!-- b000271 | prose | pages [19] -->
The distribution of resources among the five states is expressed as regional tradeoff coefficient.

<!-- b000272 | prose | pages [19] -->
Taking water as an example, we have data[10] on water use in five states. According to the data, the weight of the five states is shown in the following Figure 5.

<!-- b000273 | caption | pages [19] -->
Figure 6: The regional tradeoff coefficient of five states

<!-- b000274 | prose | pages [19] -->
f 3( ) x

<!-- b000275 | heading | pages [19] -->
6.2.2 Parameters in environmental effect

<!-- b000276 | prose | pages [19] -->
f 3( ) x : pollutant emission coefficient k There are two parameters in environmental effect jp ,and the k content of important pollutants d . j

<!-- b000277 | prose | pages [19, 20] -->
Through data search[19], California's COD (or other pollutants) emissions k d 190mg/L, emission j k coefficient is 0.20. jp

<!-- b000279 | heading | pages [20] -->
6.3 Calculation Results

<!-- b000280 | heading | pages [20] -->
6.3.1 The answer to question two

<!-- b000281 | prose | pages [20] -->
In order to better represent the relationship between agricultural, industrial, residential water use and power generation, we assume that each state has sufficient water supply and rainfall of 1000 million gallons, calculate the optimal economic benefit, and obtain the distribution of hydropower resources in each state as shown in the table  below.

<!-- b000282 | prose | pages [20] -->
As can be seen from the table :(1) in most areas, agricultural and residential water use is relatively high. This is because (1) each state has a relatively large area of farmland and a high demand for irrigation water. (2) The priority of residential water is high. We give priority to residential water in the redistribution of water resources, so the proportion of residential water is relatively high.

<!-- b000283 | prose | pages [20] -->
As can be seen from the table, the proportion of industrial and residential electricity consumption is relatively high, while that of agriculture is relatively low. This is because (1) industrial output has a high demand for electricity, (2) residents are given priority to power consumption to ensure their living needs, and (3) the main demand of agriculture is water, which has a low demand for electricity.

<!-- b000284 | heading | pages [20] -->
6.3.2 The answer to question three

<!-- b000285 | prose | pages [20] -->
Question two considers resource allocation in the absence of water shortage. At this point, Economic effect is mainly used for consideration. The third problem is the consideration of water shortage, so the multi-objective planning with Social effect, Economic effect and Environmental effect is used. The guarantee rate is listed in the following table

<!-- b000286 | caption | pages [20] -->
Table 5: Guarantee rate

<!-- b000287 | prose | pages [20] -->
f x 1( ) f 2( ) x f 3( ) x Guarantee rate /million gallons /million dollars /kg 50% 2071.65 37965.48 1235.68 75% 2748.52 34545.59 1396.32 95% 3107.47 28675.33 1731.43

<!-- b000288 | prose | pages [20, 21] -->
In the process of the guarantee rate changing from 50% to 95%, the total water shortage increases, and the discharge of important pollutants in the state also increases, but the benefit value generated in the state decreases, that is, the improvement of regional economic effect is at the cost of the reduction of social effect and environmental effect. It shows that the three objectives are interacting and competing with each other in the established coordinated multi-objective programming model.

<!-- b000290 | heading | pages [21] -->
6.3.3 The re-run of the model

<!-- b000291 | prose | pages [21] -->
Considering the work of reservoir operation and dispatching in real life and the need to make corresponding adjustments after a certain period of time in the model, we run the model at an interval of one month. Each time you run the model, you get a month of scheduling data. In case of surplus and shortage, corresponding adjustment can be made next month.

<!-- b000292 | heading | pages [21] -->
7 Mexican Allocation Model

<!-- b000293 | heading | pages [21] -->
7.1 The Establishment of Mexican Allocation Model

<!-- b000294 | prose | pages [21] -->
The model is based on the allocation plan for Mexico after the reservoir allocation.

<!-- b000295 | prose | pages [21] -->
In either Model One or Model Two, after allocating resources to each state, if there are no resources =  remainRem 0 . (Rem 0 means insufficient resources, Rem=0 means just used up), then the model is not applicable. No allocation of resources to Mexico.

<!-- b000296 | prose | pages [21] -->
If there is surplus after allocating resources: consider allocating resources to Mexico. We take every month as the operation cycle of the model, run the model according to the data, and obtain the water consumption Req required by the United States in a month. Taking the estimated total amount of water minus the estimated monthly water consumption Req, we get Rem. This is where the model applies. The amount allocated to Mexico is μ*Req(calculated as a scaling factor multiplied by a month's demand from the United States).

<!-- b000297 | prose | pages [21] -->
We refer to the Logistic curve and set parameters to make it conform to our model:

<!-- b000298 | prose | pages [21] -->
1  = ( ) t (29)  − + − rt 1 ( 1) e m  0

<!-- b000299 | heading | pages [21] -->
7.2 Calculation Results

<!-- b000300 | prose | pages [21, 22] -->
We use MATLAB to set the parameters to conform to our model and get the final parameter value = =1, = r = 1 0.0001 9.2 , . m 0 When the remaining Rem is very small and μ is close to 0, the resources allocated to Mexico are also close to 0. When Rem is greater than or equal to twice America's monthly demand Req, μ is almost 1, giving Mexico the amount of the United States in a month, i.e., giving Mexico the amount of the United States in a month at most. (The calculation period is one month). When Rem is exactly equal to Req, μ=0.5, giving the United States half of what it needs in a month.

<!-- b000301 | caption | pages [21] -->
Figure 7: Relation graph

<!-- b000303 | heading | pages [22] -->
8 Sensitivity Analysis

<!-- b000304 | heading | pages [22] -->
8.1 Change in Demand

<!-- b000305 | prose | pages [22] -->
Over time, demand for hydropower may rise or fall in various industries. At this point, we select industrial, agricultural and residential water consumption demand to increase by 5% on the basis of the original demand, industrial, agricultural and residential electricity consumption demand to decrease by 5% on the basis of the original demand, so as to explore the impact on the final result of our model solution.

<!-- b000306 | caption | pages [22] -->
Figure 8: Change in demand

<!-- b000307 | prose | pages [22] -->
It can be seen that the original proportion of residential water consumption is relatively large, and the water resource base used is relatively large. Therefore, when the industrial, agricultural and residential water demand increases by 5% respectively, the overall proportion changes greatly, and the residential proportion increases more. However, the original industrial proportion is relatively small. After the 5% increase in demand, it has little influence on the overall proportion, and the industrial proportion is also less adjusted. For electricity consumption, it can also be seen that the industry with a large original share will cause a large change in the overall share.

<!-- b000308 | heading | pages [22] -->
8.2 Renewable Energy Technologies

<!-- b000309 | prose | pages [22] -->
In our model, only the technological upgrading of hydropower generation in renewable energy technologies is considered for the time being. If considering wind power, solar power and other renewable energy technologies, you just add the power supply. In the first model, it is mentioned that the utilization efficiency of water energy conversion into electric energy is η+β, where η is the basic utilization efficiency, which is 80%.  represents the function of the renewable energy technologies enhancement., and the added value is assumed to be 5%, 10% and 15% respectively. The calculated water supply decreases with the increase of utilization efficiency. This is quite understandable because there is less extra energy lost, so there is less water to provide.

<!-- b000310 | caption | pages [23] -->
Table 6: Change of renewable energy technologies

<!-- b000311 | prose | pages [23] -->
β 5% 10% 15%

<!-- b000312 | prose | pages [23] -->
Supply 55567 53722 52642

<!-- b000313 | prose | pages [23] -->
It can be seen from the data that after the increase of β in our model, the water supply decreased, but not significantly, indicating that the water use efficiency η+β has little influence on our model, which may be because the loss caused by evaporation is greater than that of water use efficiency.

<!-- b000314 | heading | pages [23] -->
8.3 Water and Electricity Conservation Measures

<!-- b000315 | prose | pages [23] -->
We believe that additional water and electricity conservation measures will lead to a reduction in residential demand for water and electricity. The need for less resources will keep the dam at a higher  is high), so the more demand water level, which will keep generating capacity at a higher level ( h decreases, the more water the reservoir provides. However, when the demand is reduced to a certain extent, the water level of the reservoir is high enough and there is little change, and the power generation capacity is basically stable. With the decrease of the demand, the reduced water provided by the dam also tends to be positively correlated.

<!-- b000316 | caption | pages [23] -->
Figure 9: Change of conservation measures

<!-- b000317 | heading | pages [23] -->
9 Strengths and Weaknesses

<!-- b000318 | heading | pages [23] -->
9.1 Strengths

<!-- b000319 | prose | pages [23] -->
(1) The two main models used in this paper are universal and can deal with different supply and demand conditions and get better distribution schemes.

<!-- b000320 | prose | pages [23] -->
(2) Model Two comprehensively considers social effect, economic effect and environmental effect, which interact and compete with each other to improve the rationality of the results (3) In terms of water and electricity conversion and power loss, a large number of literatures are referred to ensure the rigor of the model.

<!-- b000321 | heading | pages [23] -->
9.2 Weakness

<!-- b000322 | prose | pages [24] -->
(1) In the model calculation, specific values of some parameters are not found, which may have certain influence on the results.

<!-- b000323 | prose | pages [24] -->
(2) Only hydroelectric power generation is considered in the model. If other power generation methods such as wind power generation are considered, the results will be more realistic.

<!-- b000324 | heading | pages [24] -->
References

<!-- b000325 | references | pages [24] -->
[1] https://finance.sina.com.cn/tech/2021-06-11/doc-ikqcfnca0393441.shtml

<!-- b000326 | references | pages [24] -->
[2] News of water shortages in the Western United States https://finance.sina.com.cn/tech/2021-08-

<!-- b000327 | references | pages [24] -->
19/doc-ikqciyzm2363948.shtml

<!-- b000328 | references | pages [24] -->
[3] The river basin of Colorado River from Wikipedia https://en.wikipedia.org/wiki/Colorado_River

<!-- b000329 | references | pages [24] -->
[4] https://droughtmonitor.unl.edu/

<!-- b000330 | references | pages [24] -->
[5] Lake Powell https://en.wikipedia.org/wiki/Lake_Powell

<!-- b000331 | references | pages [24] -->
[6] Lake Mead https://en.wikipedia.org/wiki/Lake_Mead

<!-- b000332 | references | pages [24] -->
[7] Hydroelectricity https://en.wikipedia.org/wiki/Hydroelectricity

<!-- b000333 | references | pages [24] -->
[8] Chang Yi. Research and application of optimal allocation of regional water resources based on genetic

<!-- b000334 | references | pages [24] -->
algorithm [D] Huazhong University of science and technology, 2011.

<!-- b000335 | references | pages [24] -->
[9] Du Bolin. Research on optimal allocation of water resources in Dali County Based on simulated

<!-- b000336 | references | pages [24] -->
annealing particle swarm optimization [D] Xi'an University of technology, 2021 DOI:10.27398/d.cnki.

<!-- b000337 | references | pages [24] -->
gxalu. 2021.000819.

<!-- b000338 | references | pages [24] -->
[10] Dieter C A. Water availability and use science program: Estimated use of water in the United States

<!-- b000339 | references | pages [24] -->
in 2015[M]. Geological Survey, 2018.

<!-- b000340 | references | pages [24] -->
[11] https://www.eia.gov/electricity/sales_revenue_price/pdf/table5_c.pdf

<!-- b000341 | references | pages [24] -->
[12] https://apps.bea.gov/regional/downloadzip.cfm

<!-- b000342 | references | pages [24] -->
[13] https://www.boardofwatersupply.com/customer-service/water-rates-and-charges/water-rate-

<!-- b000343 | references | pages [24] -->
schedule-july-1-2019-june-30-2023

<!-- b000344 | references | pages [24] -->
[14] https://www.electricitylocal.com/states/california/industry/

<!-- b000345 | references | pages [24] -->
[15] https://www.cfbf.com/wp-content/uploads/2019/06/ElectricityRates.pdf

<!-- b000346 | references | pages [24] -->
[16] https://www.suiniann.com/book/895/25709.html

<!-- b000347 | references | pages [24] -->
[17] https://www.eia.gov/electricity/state/

<!-- b000348 | references | pages [24] -->
[18] https://www.waterboards.ca.gov/resources/data_databases/wq_status_report.html

<!-- b000349 | references | pages [25] -->
Article for Drought and Thirst magazine

<!-- b000350 | references | pages [25] -->
Salvation in an age of water scarcity

<!-- b000351 | references | pages [25] -->
The Colorado River forms the largest water

<!-- b000352 | references | pages [25] -->
system in the Western United States -- known as

<!-- b000353 | references | pages [25] -->
the "lifeline of the Southwest" because it flows

<!-- b000354 | references | pages [25] -->
through vast arid and semi-arid areas. However,

<!-- b000355 | references | pages [25] -->
due to severe drought and irrational use of water

<!-- b000356 | references | pages [25] -->
resources, the volume of water from sources

<!-- b000357 | references | pages [25] -->
feeding dams and reservoirs is decreasing in

<!-- b000358 | references | pages [25] -->
many areas. Consequently, a rational, defensible

<!-- b000359 | references | pages [25] -->
water allocation plan for current and future water

<!-- b000360 | references | pages [25] -->
supply conditions is critically important.

<!-- b000361 | references | pages [25] -->
In order to solve the reservoir water

<!-- b000362 | references | pages [25] -->
resources allocation problem, we put forward two

<!-- b000363 | references | pages [25] -->
models: Model I is Water and Electricity

<!-- b000364 | references | pages [25] -->
Transportation Model and Model II is Coordinated Development of Multi-objective Programming Model.

<!-- b000365 | references | pages [25] -->
For the convenience of solving our model, we first solved the problem of the relationship between

<!-- b000366 | references | pages [25] -->
water height in the reservoirs and the volume of water in the reservoirs. On this basis, we further consider

<!-- b000367 | references | pages [25] -->
the objective function and constraint relations of the model. We try to find a distribution method that

<!-- b000368 | references | pages [25] -->
would allow the dam to supply the least amount of water, which can alleviate the water shortage situation.

<!-- b000369 | references | pages [25] -->
With regard to the constraints of the model, we think about the constraints on quantity demanded, the

<!-- b000370 | references | pages [25] -->
constraints on loss, and the constraints on inventory capacity. Based on the relationship between the Glen

<!-- b000371 | references | pages [25] -->
Canyon and Hoover dams and given parameters, the model can be used to calculate the amount of water

<!-- b000372 | references | pages [25] -->
and electricity supplied by the two dams to the five states, namely Arizona, California, Wyoming, New

<!-- b000373 | references | pages [25] -->
Mexico, and Colorado.

<!-- b000374 | references | pages [25] -->
It is equally difficult to resolve the competing interests of water availability for general usage and

<!-- b000375 | references | pages [25] -->
electricity production. To this end, we propose Model II, which can better determine a suitable allocation

<!-- b000376 | references | pages [25] -->
of water and electricity to agriculture, industry, and residences in the five states. The idea of our second

<!-- b000377 | references | pages [25] -->
model is to combine social and economic benefits and put forward a multi-objective programming model.

<!-- b000378 | references | pages [25] -->
Through this model, we can meet the basic needs of water and power supply while taking other aspects

<!-- b000379 | references | pages [25] -->
into account. Finally, we can get the trade-offs for each industry.

<!-- b000380 | references | pages [25] -->
After getting enough data, our model works well. For example, we might need temperature data,

<!-- b000381 | references | pages [25] -->
rainfall data, and so on. We recommend running our model every other month to better manage water

<!-- b000382 | references | pages [25] -->
resources so that the optimal strategy can be adjusted in time.

<!-- b000383 | references | pages [25] -->
When it comes to Mexico’s rights, we have a tiered distribution system, which can allocate the

<!-- b000384 | references | pages [25] -->
remaining water resources well. Because of the water shortage, we are not considering the diversion of

<!-- b000385 | references | pages [25] -->
the Colorado River into the Gulf of California.

<!-- b000386 | references | pages [25] -->
Although our method can solve the problem of reservoir water allocation more, we still need to

<!-- b000387 | references | pages [25] -->
cherish water resources. We encourage people to save water, and encourage relevant sectors to increase

<!-- b000388 | references | pages [25] -->
the proportion of renewable energy technologies. Only by working together can we solve the problem of

<!-- b000389 | references | pages [25] -->
water shortage.
