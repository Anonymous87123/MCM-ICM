# P-D-2024-2417004-a737e95b

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型 微信号：MATHmodels 关注数学模型 获取更多资讯 2 MATHmodels

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen 2024 MCM/ICM Summary Sheet Team Control Number

<!-- b000003 | title | pages [1] -->
Regulating the Water of Tomorrow: A Multi-Layer Optimization Model for the Great Lakes

<!-- b000004 | heading | pages [1] -->
Summary

<!-- b000005 | prose | pages [1] -->
The Great Lake in the US and Canada faces water problems. The water level of the Great Lake needs to be regulated to satisfy the interests of stakeholders and balance the ecosystem. It’s challenging to control the flow of water due to its complex dynamics. Several organizations have been working on this problem for decades and released solutions such as Plan 2014. However, stakeholders are not satisfied with the current situation and the ever-changing climate has raised uncertainties.

<!-- b000006 | prose | pages [1] -->
In this project, a network model of the Great Lakes was built to optimize the water level at any time of the year. It employs a multi-layer modeling design, with both a basic network model for describing the major flow processes in the Great Lakes, and an advanced flow model to refine the complex factors affecting the flow. Compared with the previous plans, this scheme allows for increased flexibility in lake water levels, accommodating fluctuations between high and low water levels.

<!-- b000007 | prose | pages [1] -->
The main steps are as follows:

<!-- b000008 | prose | pages [1] -->
First, a basic network model connecting the five lakes was established to analyze the main water processes. Combined with the analysis of the provided data, several equations were formed to describe the flow of water in the network, which is the foundation of the model. With this model and the dataset, the water level and the flow of water can be calculated.

<!-- b000009 | prose | pages [1] -->
Then, an advanced flow model was built based on the basic model to better depict the sophisticated processes affecting the water flow. It is more comprehensive and precise since it analyzes wind, snow, ice jams, and other meteorological factors. This model focuses more on Lake Ontario and the St. Lawrence River to solve the sub-problem. The sensitivity analysis indicated that the model is sensitive to precipitation and less sensitive to the melt of snow.

<!-- b000010 | prose | pages [1] -->
To find a plan that satisfies the stakeholders, multiple benefit and cost functions are first created to form the objective functions, thus creating a multi-objective optimization model. The optimal water level is then solved using the NSGA-II algorithm with operations such as selection, crossover, and mutation.

<!-- b000011 | prose | pages [1] -->
In addition, by utilizing data from 2017, the high stability and accuracy of the model are verified in terms of both water use extrapolation based on the multiple linear regression algorithm and computation of the new optimization algorithm.

<!-- b000012 | prose | pages [1] -->
The study succeeded in effectively simulating and optimizing the water level in the Great Lakes by building network models. It's promising, reliable and it's beneficial for all the stakeholders. More importantly, this new plan is also sustainable and will bring the Great Lakes Region towards a better future.

<!-- b000013 | keywords | pages [1] -->
Keywords: network, flow model, water resource management, water supply, NSGA-II, multiple linear regression

<!-- b000014 | furniture | pages [2] -->
Team # 2417004

<!-- b000015 | furniture | pages [2] -->
Page 2 of 25

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1 Introduction .................................................................................................... 3

<!-- b000018 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000019 | contents | pages [2] -->
1.1 Problem Background ....................................................................................................... 3

<!-- b000020 | contents | pages [2] -->
1.2 Our Work .......................................................................................................................... 3

<!-- b000021 | contents | pages [2] -->
2 Assumptions and Justifications ..................................................................... 4

<!-- b000022 | contents | pages [2] -->
3 Notations .......................................................................................................... 4

<!-- b000023 | contents | pages [2] -->
4 Part I: A Basic Network Model for the Great Lakes ................................... 4

<!-- b000024 | contents | pages [2] -->
4.1 Analysis of the problem ................................................................................................... 4

<!-- b000025 | contents | pages [2] -->
4.2 A basic network model ..................................................................................................... 6

<!-- b000026 | contents | pages [2] -->
4.3 Analyzing the flow of water ............................................................................................. 7

<!-- b000027 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000028 | contents | pages [2] -->
5 Part II: An Advanced Model for Further Analysis ...................................... 9

<!-- b000029 | contents | pages [2] -->
5.1 Background: the need for artificial regulation of dam discharge ..................................... 9

<!-- b000030 | contents | pages [2] -->
5.2 Initial Establishment of Rule Curves ............................................................................. 10

<!-- b000031 | contents | pages [2] -->
5.3 Outflow Limitation Impact Factors ............................................................................... 12

<!-- b000032 | contents | pages [2] -->
5.4 Impact of the Ottawa River on the Flow of St. Lawrence River ................................... 13

<!-- b000033 | contents | pages [2] -->
6 Part III: Modeling to Determine the Optimal Water Levels .................... 14

<!-- b000034 | contents | pages [2] -->
6.1 Analysis .......................................................................................................................... 14

<!-- b000035 | contents | pages [2] -->
6.2 The establishment of the multi-objective optimization model ....................................... 15

<!-- b000036 | contents | pages [2] -->
6.3 Optimal water-level determination model based on NSGA-II algorithm ...................... 17

<!-- b000037 | contents | pages [2] -->
6.4 Tests of the model using 2017 data ................................................................................ 18

<!-- b000038 | contents | pages [2] -->
7 Sensitivity Analysis ....................................................................................... 19

<!-- b000039 | contents | pages [2] -->
7.1 Precipitation ................................................................................................................... 19

<!-- b000040 | contents | pages [2] -->
7.2 Snowmelt ....................................................................................................................... 20

<!-- b000041 | contents | pages [2] -->
8 Model Evaluation .......................................................................................... 21

<!-- b000042 | contents | pages [2] -->
8.1 Strengths ........................................................................................................................ 21

<!-- b000043 | contents | pages [2] -->
8.2 Weaknesses .................................................................................................................... 21

<!-- b000044 | contents | pages [2] -->
8.3 Further discussion .......................................................................................................... 21

<!-- b000045 | contents | pages [2] -->
9 Conclusion ..................................................................................................... 21

<!-- b000046 | contents | pages [2] -->
10 Memo to IJC leadership ............................................................................. 23

<!-- b000047 | contents | pages [2] -->
References ......................................................................................................... 24

<!-- b000048 | contents | pages [2] -->
Appendix .......................................................................................................... 24

<!-- b000049 | contents | pages [2] -->
关注数学模型

<!-- b000050 | furniture | pages [2] -->
2

<!-- b000051 | furniture | pages [2] -->
MATHmodels

<!-- b000052 | furniture | pages [2] -->
获取更多资讯

<!-- b000053 | furniture | pages [3] -->
Team # 2417004

<!-- b000054 | furniture | pages [3] -->
Page 3 of 25

<!-- b000055 | heading | pages [3] -->
1  Introduction

<!-- b000056 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000057 | heading | pages [3] -->
1.1 Problem Background

<!-- b000058 | prose | pages [3] -->
The Great Lake which consists of five lakes and their connecting waterways is an im- portant drainage basin for the United States and Canada. Its water resource is used by various stakeholders for many purposes (including power plants, recreation, fishing and shipping, etc.). Subtle changes in the water level will greatly affect stakeholders’ benefits. Thus, the manage- ment of water is their main concern.

<!-- b000059 | prose | pages [3] -->
The water level is determined by the amount of water that flows in and out of the lake. It’s affected by many physical conditions and their complex interactions, such as precipitation, wind, snow, etc. It’s also influenced by seasons and some unexpected events like extreme weather. 微信号：MATHmodels To control the water levels in the Great Lake system, two main dams were built. They can manipulate the flow of water to some extent to better satisfy the demands of all stakeholders. The International Joint Commission (IJC) has established many plans to control the dams in the past decades to balance water levels. However, it’s hard to satisfy the interests of all stake- holders, especially in the era of climate change where the likelihood of extreme water levels increases.

<!-- b000060 | heading | pages [3] -->
1.2 Our Work

<!-- b000061 | prose | pages [3] -->
In addressing the complex challenges of regulating the water levels in the Great Lakes, our study employed a multi-layer modeling approach, combining a fundamental network model with advanced flow models to enhance precision. The graph below shows the key components of our work.

<!-- b000062 | caption | pages [3] -->
Figure 1: Our framework

<!-- b000063 | prose | pages [3] -->
关注数学模型

<!-- b000064 | furniture | pages [3] -->
2

<!-- b000065 | furniture | pages [3] -->
MATHmodels

<!-- b000066 | furniture | pages [3] -->
获取更多资讯

<!-- b000067 | furniture | pages [4] -->
Team # 2417004

<!-- b000068 | furniture | pages [4] -->
Page 4 of 25

<!-- b000069 | heading | pages [4] -->
2  Assumptions and Justifications

<!-- b000070 | prose | pages [4] -->
Assumption 1: The inflow between each lake is equal to the outflow from the next lake. 微信公众号：数学模型 Assumption 2: The Lake Ontario-St. Lawrence River advanced model is generalizable across the Great Lakes system.

<!-- b000071 | prose | pages [4] -->
Assumption 3: Lake Ontario water levels are approximately the same as those of the St. Lawrence.

<!-- b000072 | heading | pages [4] -->
Assumption 4: The outflow from the Moses-Saunders Dam follows a simple mechani-

<!-- b000073 | prose | pages [4] -->
cal release principle.

<!-- b000074 | prose | pages [4] -->
Assumption 5: Water use is somewhat indicative of the neighborhood's population, eco- nomic conditions, and water levels.

<!-- b000075 | prose | pages [4] -->
Assumption 6: High water levels can lead to increased costs of channel maintenance and potential flood damage. 微信号：MATHmodels

<!-- b000076 | heading | pages [4] -->
3  Notations

<!-- b000077 | prose | pages [4] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000078 | caption | pages [4] -->
Table 1: Notations used in this paper

<!-- b000079 | prose | pages [4] -->
Symbol Description Unit Water level ( ) Water flow ( ) Precipitation ( ) Evapotranspiration ( ) Net basin supply ( ) Net total supply ( ) — The rate of flow adjustment to pre-project flows — The rate of flow adjustment (Each) The number of baffles located above the water surface ( ) Runoff ( ) The amount of outflow added to the dam The total distance traveled of wind (k )

<!-- b000080 | heading | pages [4] -->
4  Part I: A Basic Network Model for the Great Lakes

<!-- b000081 | heading | pages [4] -->
4.1 Analysis of the problem

<!-- b000082 | prose | pages [4] -->
The Great Lakes consists of five connected lakes. Lake Michigan and Lake Huron have approximately the same water level and are often considered integral. Water in this drainage

<!-- b000083 | prose | pages [4, 5] -->
关注数学模型 system starts from Lake Superior, goes through Lake Huron, Lake Erie, Lake Ontario, and ultimately flows into the Atlantic Ocean. (Figure 2)

<!-- b000084 | furniture | pages [4] -->
2

<!-- b000085 | furniture | pages [4] -->
MATHmodels

<!-- b000086 | furniture | pages [4] -->
获取更多资讯

<!-- b000087 | furniture | pages [5] -->
Team # 2417004

<!-- b000088 | furniture | pages [5] -->
Page 5 of 25

<!-- b000090 | prose | pages [5] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000091 | caption | pages [5] -->
Figure 2: A map of the Great Lake Basin

<!-- b000092 | prose | pages [5] -->
Several waterways which have connected these lakes control the inflow and outflow of water. The water flows from one lake to the next lake, which is a one-way flow. It is affected by many natural factors, such as precipitation, wind, ice jams, etc. Since these physical factors change with time, the waterflow has its annual, monthly and daily patterns.

<!-- b000093 | prose | pages [5] -->
The two main control mechanisms of the waterflow is the Soo Locks and the Moses- Saunders Dam. They can be controlled in order to gain better water levels to satisfy the stake- holders in this area.

<!-- b000094 | prose | pages [5] -->
To find a suitable way of adjusting the water levels, it’s important to build a basic network model that describes the waterflow. The changing pattern of water level and water flow in different period of time is the foundation of this model. Based on this network, it’s possible to figure out the relationship between water level and waterflow, which is essential for regulating the water level of the Great Lake.

<!-- b000095 | caption | pages [5] -->
Figure 3: The Great Lake system and the water level of Lake Ontario

<!-- b000096 | prose | pages [5, 6] -->
关注数学模型 The water level and the flow of water have changing patterns under different scales of time. They are affected by factors such as wind, precipitation and snow etc. Take Lake Ontario as an example. The graph above shows that the water level changes annually. (Figure 3) 微信公众号：数学模型

<!-- b000097 | furniture | pages [5] -->
2

<!-- b000098 | furniture | pages [5] -->
MATHmodels

<!-- b000099 | furniture | pages [5] -->
获取更多资讯

<!-- b000100 | furniture | pages [6] -->
Team # 2417004

<!-- b000101 | furniture | pages [6] -->
Page 6 of 25

<!-- b000103 | heading | pages [6] -->
4.2 A basic network model

<!-- b000104 | prose | pages [6] -->
The Great Lake system can be abstracted by a simple network system that connects lakes with rivers. The nodes in the graph below symbolize different lakes, while the edges are the rivers that connect these lakes. All the edges in this graph have only one direction, which is from a relatively high lake to a relatively low lake.

<!-- b000105 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000106 | caption | pages [6] -->
Figure 4: The network model of the Great Lake

<!-- b000107 | prose | pages [6] -->
The directed graph below is the mathematical model of this network. The nodes stands for the lakes or ocean, while the edges stand for rivers.

<!-- b000108 | prose | pages [6] -->
b a d e f

<!-- b000109 | prose | pages [6] -->
c

<!-- b000110 | caption | pages [6] -->
Figure 5: The directed graph of the model

<!-- b000111 | prose | pages [6] -->
The source of this model is node , which represents Lake Superior. The sink of this model is node , which represents the Atlantic Ocean.

<!-- b000112 | prose | pages [6] -->
The amount of water that flows in the edges can be described by the weight of each edge.

<!-- b000113 | prose | pages [6] -->
is the inflow of water from the previous lake and is the outflow of water. Thus, the change between inflow and outflow is

<!-- b000114 | prose | pages [6] -->
The supply of the lake also comes from precipitation, evaporation, and runoff from the basin. These three parts comprise the net basin supply .

<!-- b000115 | prose | pages [6] -->
In the equation above, stands for the amount of water inflow caused by pre- cipitation, and stands for the amount of water outflow caused by evaporation. The runoff of a basin is the portion of precipitation on the land that ultimately reaches streams and lakes.

<!-- b000116 | prose | pages [6, 7] -->
关注数学模型 Net Basin Supply

<!-- b000117 | furniture | pages [6] -->
2

<!-- b000118 | furniture | pages [6] -->
MATHmodels

<!-- b000119 | furniture | pages [6] -->
获取更多资讯

<!-- b000120 | furniture | pages [7] -->
Team # 2417004

<!-- b000121 | furniture | pages [7] -->
Page 7 of 25

<!-- b000123 | prose | pages [7] -->
Over-lake Evaporation Run-off Precipitation 微信公众号：数学模型 P E R

<!-- b000124 | prose | pages [7] -->
Qin Qout Lake Outflow Inflow

<!-- b000125 | caption | pages [7] -->
Figure 6: A basic model of lake water

<!-- b000126 | prose | pages [7] -->
When the water comes into the water, it leads the water level to rise. The amount of rise is related to the surface area of the lake and the amount of water that goes into the lake. Thus, the rise or fall of the water level caused by any conditions can be calculated.

<!-- b000127 | prose | pages [7] -->
For example, the water rise caused ONLY by runoff is 微信号：MATHmodels where is a specific period of time.

<!-- b000128 | prose | pages [7] -->
Since the monthly precipitation and evaporation are usually recorded in units of meter, the water supply caused by precipitation should be

<!-- b000129 | prose | pages [7] -->
As is mentioned above in Equation[1], net basin supply (NBS) is the net amount of water entering one of the Great Lakes. The net basin supply does not include inflow from another local and runoff from its local basin.

<!-- b000130 | prose | pages [7] -->
The net total supply (NTS) is the net basin supply (NBS) plus the inflow from another lake. That is,

<!-- b000131 | heading | pages [7] -->
4.3 Analyzing the flow of water

<!-- b000132 | prose | pages [7] -->
As the water flows between the lakes, there are two different situations. In the first case, the water flows naturally. And in another case, the water is controlled by dams. Specifically, the water at Soo Locks and Moses-Saunders Dam is controlled manually. And water in other rivers such as St. Clair River flows naturally. Therefore, it’s essential to discuss the difference between the two situations and build up their own model.

<!-- b000133 | prose | pages [7, 8] -->
关注数学模型 Lake A Lake B

<!-- b000134 | furniture | pages [7] -->
2

<!-- b000135 | furniture | pages [7] -->
MATHmodels

<!-- b000136 | furniture | pages [7] -->
获取更多资讯

<!-- b000137 | furniture | pages [8] -->
Team # 2417004

<!-- b000138 | furniture | pages [8] -->
Page 8 of 25

<!-- b000140 | prose | pages [8] -->
River QA_out QB_in 微信公众号：数学模型 (a) Natural flow (b) Controlled by dam

<!-- b000141 | caption | pages [8] -->
Figure 7: Two types of flow in the river

<!-- b000142 | prose | pages [8] -->
When there are not any dams on the river, the water flows naturally from one to another. We assume that the outflow of a lake is equivalent to the inflow of the next lake. That is

<!-- b000143 | prose | pages [8] -->
When there’s a dam on the river, the flow of the lake is affected by both human control and its natural pattern. We still assume that the outflow of a lake is equivalent to the inflow of 微信号：MATHmodels the next lake. However, the amount of water has changed since the control of the dam. It is the previous flow added by the change of flow.

<!-- b000144 | prose | pages [8] -->
could be controlled by many factors since the flow of water is very sensitive to its environment. It can be affected by wind, temperature, policies, etc. The factors will be fur- ther investigated in the next chapter.

<!-- b000145 | prose | pages [8] -->
The water level of the lake is

<!-- b000146 | prose | pages [8] -->
where is the previous height and is the amount of flow that caused the

<!-- b000147 | prose | pages [8] -->
rise of the water level.

<!-- b000148 | caption | pages [8] -->
Figure 8: An example of the water level calculation

<!-- b000149 | prose | pages [8] -->
With the equations above in this chapter, a basic model of the Great Lake is established. This model characterized the flow of water and its effect on water levels. It’s the foundation of further analysis. In the next chapter, some other factors (such as wind, ice, snow, etc.) will be taken into account to further this model.

<!-- b000150 | prose | pages [8] -->
关注数学模型

<!-- b000151 | furniture | pages [8] -->
2

<!-- b000152 | furniture | pages [8] -->
MATHmodels

<!-- b000153 | furniture | pages [8] -->
获取更多资讯

<!-- b000154 | furniture | pages [9] -->
Team # 2417004

<!-- b000155 | furniture | pages [9] -->
Page 9 of 25

<!-- b000156 | heading | pages [9] -->
5  Part II: An Advanced Model for Further Analysis

<!-- b000157 | heading | pages [9] -->
5.1 Background: the need for artificial regulation of dam discharge

<!-- b000158 | prose | pages [9] -->
微信公众号：数学模型 There are two primary control mechanisms within the flow of water in the Great Lakes system - Compensating Works at Sault Ste. and the Moses-Saunders Dam at Cornwall. Among them, the Moses-Saunders Dam manages the outflows from Lake Ontario into the St. Lawrence River. The proper regulation of the dam's discharge has a critical impact on regulating the level of Lake Ontario and the downstream flow and water levels in the St. Lawrence River.

<!-- b000159 | heading | pages [9] -->
5.1.1 Lake Ontario water level control advanced model

<!-- b000160 | prose | pages [9] -->
In the model we designed, natural factors such as ice jams, precipitation, and wind are taken into account, with the expectation that the upstream and downstream water levels will be adjusted to meet the optimal levels for each stakeholder by setting the dam outflow. (The opti- 微信号：MATHmodels mal water level that integrates all stakeholders is described in detail later.)

<!-- b000161 | heading | pages [9] -->
5.1.2 Spotlight on Lake Ontario-St. Lawrence River

<!-- b000162 | prose | pages [9] -->
As there is more recent concern for the management of the water level for the Ontario in recent years. We take Lake Ontario-St. Lawrence River advanced model and analyze it in depth, assuming that the outflow from Lake Ontario approximates the outflow from the Moses-Saun- ders Dam. (Figure 9) As water supplies trend above normal or St. Lawrence River flows de- crease, lake releases are increased. As supplies trend below normal or St. Lawrence River flows increase, lake releases are decreased.

<!-- b000163 | caption | pages [9] -->
Figure 9: The Moses-Saunders Dam sketch[2]

<!-- b000164 | prose | pages [9] -->
关注数学模型

<!-- b000165 | furniture | pages [9] -->
2

<!-- b000166 | furniture | pages [9] -->
MATHmodels

<!-- b000167 | furniture | pages [9] -->
获取更多资讯

<!-- b000168 | furniture | pages [10] -->
Team # 2417004

<!-- b000169 | furniture | pages [10] -->
Page 10 of 25

<!-- b000170 | heading | pages [10] -->
5.2 Initial Establishment of Rule Curves

<!-- b000171 | prose | pages [10] -->
Lake releases are primarily a function of a sliding rule curve based on the pre-project stage-discharge relationship adjusted to recent supply conditions. The flow computed with this 微信公众号：数学模型 equation is then adjusted depending on the recent supply conditions. The newly developed Lake-River model can be applied to other sites in the Great Lakes system except Lake Erie.

<!-- b000172 | prose | pages [10] -->
In the equation above, is the value of the change in outflow, represents the pre-project outflow.

<!-- b000173 | heading | pages [10] -->
5.2.1 Model of a dam with baffles

<!-- b000174 | prose | pages [10] -->
This model will demonstrate how the Moses-Saunders Dam is used to help control water 微信号：MATHmodels levels downstream (Figure 10). We assume that it contains 50 gates that can be raised or low- ered to help control water levels downstream. This is accomplished by reducing the number of baffles above the water surface when less outflow is needed.

<!-- b000175 | caption | pages [10] -->
Figure 10: Model of a dam with baffles

<!-- b000176 | prose | pages [10] -->
The variable determine the rate of flow adjustment to pre-project flows and also depend on the long-term trend in supply. The variable  represents the number of baffles located above the water surface, and the constant indicates the amount of outflow added to the dam for each baffle opened.

<!-- b000177 | heading | pages [10] -->
5.2.2 Impact of NTS in Lake Ontario basin on outflow from dams

<!-- b000178 | prose | pages [10] -->
To simplify the model, we assume that the water level of Lake Ontario is the same as that of Lake St. Louis. Dam control outflows are largely determined by total basin supply, and to adapt to long-term climate change, the change in outflows should satisfy the following equation:

<!-- b000179 | prose | pages [10, 11] -->
关注数学模型 A_ NTS A _ NTS A _ NTS Plan Climate avg max min 微信公众号：数学模型 8552 m3/s 5717 m3/s 7011 m3/s Plan2014 Historical (1900-2000)

<!-- b000180 | furniture | pages [10] -->
2

<!-- b000181 | furniture | pages [10] -->
MATHmodels

<!-- b000182 | furniture | pages [10] -->
获取更多资讯

<!-- b000183 | furniture | pages [11] -->
Team # 2417004

<!-- b000184 | furniture | pages [11] -->
Page 11 of 25

<!-- b000185 | caption | pages [11] -->
Table 2: Rule curve parameter values based on historical NTS of Lake Ontario[3]

<!-- b000187 | prose | pages [11] -->
9042 m3/s 5717 m3/s 7067 m3/s Our Plan Historical (1900-2023)

<!-- b000188 | prose | pages [11] -->
For supplies above normal (the index is greater than or equal to 7067 m3/s), the lake re- lease is determined by:

<!-- b000189 | prose | pages [11] -->
M   − 1 W _ NTS A _ NTS now avg ∆ = × Q Z   out 1 − A _ NTS A _ NTS   1   max avg

<!-- b000190 | prose | pages [11] -->
For supplies below normal (the index is less than 7067 m3/s), the lake release is deter- mined by: 微信号：MATHmodels M   − 2 A _ NTS W _ NTS avg now ∆ = − × Q Z   out 2 − A _ NTS W _ NTS   1   avg min

<!-- b000191 | prose | pages [11] -->
In the above equations, W_NTS is a supply index based on net total supply over the past 12 weeks. A_NTS indicates the maximum, minimum, and average statistics of the total annual net supply series. The indices M serve to accelerate or decelerate the rate of flow adjustment.

<!-- b000192 | heading | pages [11] -->
5.2.3 Effect of Lake Ontario water levels on outflows from dams

<!-- b000193 | prose | pages [11] -->
When the water level of Lake Ontario is high, the likelihood of flooding increases, which causes a great deal of disruption to the lives of the people living along the shoreline, so in order to prevent catastrophes from occurring, the factor of the change in the water level of Lake Ontario over time should also be taken into account in the equation for the change in outflow.

<!-- b000194 | caption | pages [11] -->
Table 3: Rule curve parameter values based on historical water levels of Lake Ontario[4]

<!-- b000195 | prose | pages [11] -->
Climate

<!-- b000196 | prose | pages [11] -->
75.37 m 74.00 m 74.77 m Historical (1900-2023)

<!-- b000197 | prose | pages [11] -->
For water levels above normal (the index is greater than or equal to 74.77 m), the lake release is determined by:

<!-- b000198 | prose | pages [11] -->
M   − 3 H H now avg ∆ = × Q Z   out 3 − H H   2   max avg

<!-- b000199 | prose | pages [11] -->
For water levels below normal (the index is lower than 74.77 m), the lake release is deter- mined by:

<!-- b000200 | prose | pages [11, 12] -->
关注数学模型 M   − 4 H H avg now ∆ = − × Q Z   out 4 − H H   2   avg min 微信公众号：数学模型 In the above equations, H indicates the maximum, minimum, and average statistics of the annual of Lake Ontario water levels.

<!-- b000201 | furniture | pages [11] -->
2

<!-- b000202 | furniture | pages [11] -->
MATHmodels

<!-- b000203 | furniture | pages [11] -->
获取更多资讯

<!-- b000204 | furniture | pages [12] -->
Team # 2417004

<!-- b000205 | furniture | pages [12] -->
Page 12 of 25

<!-- b000207 | heading | pages [12] -->
5.3 Outflow Limitation Impact Factors

<!-- b000208 | prose | pages [12] -->
In addition to the effects of total basin supply and water levels, other weather variations and meteorological conditions can limit outflow from dams, with the main considerations in our outflow model being rainfall over the coming period of time, a dramatic increase in the flow of the Ottawa River due to winter snowpack melt in the spring and ice jams on the river in the winter, as well as natural factors such as winds on the lake.

<!-- b000209 | heading | pages [12] -->
5.3.1 Short-term precipitation forecasts

<!-- b000210 | prose | pages [12] -->
微信号：MATHmodels In the previous model we mainly considered the effect of long-term climate change on the outflow from the control dam, however, short-term weather changes such as rainfall cannot be ignored in the complete model, and by predicting future short-term rainfall, we can refine the model more finely to mitigate the effects of sudden storms on water surface heights through the following equation:

<!-- b000211 | prose | pages [12] -->
Variability of releases from one week to the next is smoothed by taking the average of short-term forecasts4 of releases four weeks (or quarter-months) into the future.

<!-- b000212 | heading | pages [12] -->
5.3.2 Modeling of synthetic winds on lakes

<!-- b000213 | prose | pages [12] -->
The wind direction of the prevailing winds on an open lake has an important effect on the distribution of water levels, as shown in the figure 11, where the wind blows water from one shore of the lake surface to the other, resulting in higher water levels on the opposite shore.

<!-- b000214 | caption | pages [12] -->
Figure 11: Simplified Lake Ontario synthetic wind model

<!-- b000215 | prose | pages [12, 13] -->
We consider Lake Ontario as a rectangle, with the lake surface as a rectangle with long 关注数学模型 side L1 (East-West Direction) and short side L2 (North-South Direction). Due to the Narrow Tube Effect, the wind along the lake surface is significantly greater in the east-west direction than in the north-south direction, so a synthetic wind model is used to synthesize the winds 微信公众号：数学模型 from different stations on the lake surface into two directions (E and N), We believe that the amount of water transmitted by the wind factor can be replaced by the wind range, and a greater wind range in the due east or due west direction indicates a higher water level on the eastern shore of the lake, which needs to be regulated by increasing the outflow from the control dam.

<!-- b000216 | furniture | pages [12] -->
2

<!-- b000217 | furniture | pages [12] -->
MATHmodels

<!-- b000218 | furniture | pages [12] -->
获取更多资讯

<!-- b000219 | furniture | pages [13] -->
Team # 2417004

<!-- b000220 | furniture | pages [13] -->
Page 13 of 25

<!-- b000222 | prose | pages [13] -->
The wind range is calculated using the following formula:

<!-- b000223 | prose | pages [13] -->
= ⋅ = ⋅ = ⋅ N V N F , NNE V NNE F , NE V NE F N NNE NE

<!-- b000224 | prose | pages [13] -->
Calculate the synthesized wind direction by breaking down the travel in each direction into travel in the due north and due east directions:

<!-- b000225 | prose | pages [13] -->
( ) = − + + − − ° CN N S NNE NNW SSE SSW cos 22 5. 微信号：MATHmodels ( ) + + − − ° NW NE SW SE cos 45 ( ) + + − − ° ENE WNW ESE WSW cos 67 5.

<!-- b000226 | prose | pages [13] -->
( ) = − + + − − ° CE E W ENE ESE WNW WSW cos 22 5.

<!-- b000227 | prose | pages [13] -->
( ) + + − − ° NE SE NW SW cos 45 ( ) + + − − ° NNE SSW WNW SSW cos 67 5.

<!-- b000228 | prose | pages [13] -->
M   6 L L ∆ = + × 1 2 Q C C Z   out E N 6 + + L L L L 4 1 2 1 2

<!-- b000229 | prose | pages [13] -->
And then calculate synthetic direction and wind speed:

<!-- b000230 | prose | pages [13] -->
C C C 2 2 tan− θ = α = = + v = N N 1 tan , , C C C , N E C C f E E

<!-- b000231 | prose | pages [13] -->
In the above formulas, v is the synthetic wind speed, f is the number of observation , and C is the total distance traveled of wind.

<!-- b000232 | heading | pages [13] -->
5.4 Impact of the Ottawa River on the Flow of St. Lawrence River

<!-- b000233 | prose | pages [13] -->
The flow of the Ottawa River, an important tributary to the St. Lawrence River, has a profound effect on regulating outflow from the control dams (in order to maintain a relatively stable water level in the lower St. Lawrence River), Due to the high latitude of the St. Lawrence River and the long ice age in winter, ice jams result in a decrease in the flow of the St. Lawrence River, and then a dramatic increase in the flow of the St. Lawrence River as a result of ice melt water from the return of warmer temperatures the following spring.

<!-- b000234 | heading | pages [13] -->
5.4.1 Spring flooding from winter snowpack melt

<!-- b000235 | prose | pages [13, 14] -->
Spring ice melt leads to increased flows in the Ottawa River, which feeds into the St. Lawrence River, so controlled dam discharges are needed to balance water levels and flows in 关注数学模型 the lower St. Lawrence River. The change in outflows should satisfy the following equation:

<!-- b000236 | furniture | pages [13] -->
2

<!-- b000237 | furniture | pages [13] -->
MATHmodels

<!-- b000238 | furniture | pages [13] -->
获取更多资讯

<!-- b000239 | furniture | pages [14] -->
Team # 2417004

<!-- b000240 | furniture | pages [14] -->
Page 14 of 25

<!-- b000242 | caption | pages [14] -->
Table 4: Rule curve parameter values based on historical flows of the St. Lawrence River[5]

<!-- b000243 | prose | pages [14] -->
微信公众号：数学模型 A_ Q A _ Q A _ Q Climate avg max min

<!-- b000244 | prose | pages [14] -->
3553 m3/s 2176 m3/s 2968 m3/s Historical (1900-2023)

<!-- b000245 | prose | pages [14] -->
For supplies above normal (the index is greater than or equal to 2968 m3/s), the lake re- lease is determined by:

<!-- b000246 | prose | pages [14] -->
M   − 7 W _ Q A _ Q now avg ∆ = − × Q Z   out 7 − A _ Q A _ Q   5   max avg

<!-- b000247 | prose | pages [14] -->
For water levels below normal (the index is lower than 2968 m3/s), the lake release is 微信号：MATHmodels determined by:

<!-- b000248 | prose | pages [14] -->
M   − 7 A _ Q W _ Q avg now ∆ = × Q Z   out 7 − A _ Q A _ Q   5   avg min

<!-- b000249 | prose | pages [14] -->
In the above equations, is a supply index based on net total supply over the past 12 weeks. A_NTS indicates the maximum, minimum, and average statistics of the total annual net supply series.

<!-- b000250 | heading | pages [14] -->
5.4.2 Impact of ice jams on dam outflows

<!-- b000251 | prose | pages [14] -->
Ice jams result in a reduction in the amount of water in the Ottawa River that feeds into the St. Lawrence River, and it can be assumed that the amount of ice on the river surface can be indirectly expressed as a reduction in the flow of the river, resulting in the need to compen- sate for the reduction in the level of the downstream St. Lawrence River water by increasing discharge from the upstream dams. The calculation formula is similar to the modeling of spring flood flow increases and will not be repeated here due to space limitations.

<!-- b000252 | heading | pages [14] -->
6  Part III: Modeling to Determine the Optimal Water Levels

<!-- b000253 | heading | pages [14] -->
6.1 Analysis

<!-- b000254 | prose | pages [14] -->
Establishing the optimum water level for the Great Lakes at any given time of the year requires consideration of a number of factors. Since there has been more recent interest in the management of Lake Ontario, in this paper we will focus on the desires of the six categories of Lake Ontario stakeholders as a means of obtaining the optimal water level for Lake Ontario. This method will also be used to calculate the optimal water level for the other four lakes in the same way, so as to find the optimal water level for the whole basin.

<!-- b000255 | prose | pages [14] -->
No single critical low or high water level has ‘adverse impacts’ on the system. The level

<!-- b000256 | prose | pages [14, 15] -->
关注数学模型 of harm experienced by a user of the system greatly depends on the location and the usage and sometimes the time of the year, since stormy weather and high winds may cause crashing waves, damaging shorelines at any high water level. 微信公众号：数学模型 In this paper six categories of stakeholders will be considered: shipping companies, people who manage shipping docks or live near the Montreal harbor, environmentalists, property own- ers on the shores of Lake Ontario, recreational boaters and fishing boats on Lake Ontario, and hydro-power generation companies. Their relationship with the water level is shown in the figure.

<!-- b000257 | furniture | pages [14] -->
2

<!-- b000258 | furniture | pages [14] -->
MATHmodels

<!-- b000259 | furniture | pages [14] -->
获取更多资讯

<!-- b000260 | furniture | pages [15] -->
Team # 2417004

<!-- b000261 | furniture | pages [15] -->
Page 15 of 25

<!-- b000263 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000264 | caption | pages [15] -->
Figure 12: (a)Effect of high and low water levels      (b)Effect of water flow stability

<!-- b000265 | prose | pages [15] -->
Their benefit and cost functions are first established to find the corresponding objective functions. Since the multi-objective optimization model is able to consider multiple objectives at the same time, it is more suitable for this question scenario. Genetic algorithms are highly robust and suitable for dealing with complex optimization problems and are able to optimize even when the optimization objectives are unclear or uncertain. Therefore, we establish a multi- objective optimization model and use the genetic algorithm NSGA-II to solve the model.

<!-- b000266 | heading | pages [15] -->
6.2 The establishment of the multi-objective optimization model

<!-- b000267 | prose | pages [15] -->
First, setting the decision variable as follows:

<!-- b000268 | prose | pages [15] -->
H: The current water level Q: The current water flow Then building the objective function, we're here to predict optimal water levels using Lake Ontario's January data:

<!-- b000269 | prose | pages [15] -->
This is the yield function of the shipping companies, which require high and still water in the St. Lawrence River.

<!-- b000270 | prose | pages [15] -->
: Minimum water level required for shipping

<!-- b000271 | prose | pages [15, 16] -->
关注数学模型 : Benefits from rising water levels per unit : Lake Ontario Container Through- put for January [6] : Additional cost increase per unit increase in flow rate 微信公众号：数学模型 This is the cost function of the shipping companies. is the ideal water level for ship- ping, and is the contractor's coefficient resulting from excessive water levels.

<!-- b000272 | furniture | pages [15] -->
2

<!-- b000273 | furniture | pages [15] -->
MATHmodels

<!-- b000274 | furniture | pages [15] -->
获取更多资讯

<!-- b000275 | furniture | pages [16] -->
Team # 2417004

<!-- b000276 | furniture | pages [16] -->
Page 16 of 25

<!-- b000278 | prose | pages [16] -->
From this we can model the satisfaction of this stakeholder:

<!-- b000279 | prose | pages [16] -->
simmilarly, we can model other stakeholders.

<!-- b000280 | prose | pages [16] -->
微信号：MATHmodels This is the yield function of people who manage shipping docks or live near the Montreal harbor. is the steady water level one would expect, is a measure of the sensitivity of the water level to deviation from the steady water level, and is the contribution of the flow rate to the wind speed.

<!-- b000281 | prose | pages [16] -->
This is the yield function of environmentalists. is the average annual water level,

<!-- b000282 | prose | pages [16] -->
is a measure of population size predicted from water use.[7] and

<!-- b000283 | prose | pages [16] -->
This is the yield function of property owners on the shores of Lake Ontario. and are the owner's desired water level and flow rate. and are composite coefficients combining the number of owners with the revenue brought in by the owners, predicting water use.[7]

<!-- b000284 | prose | pages [16] -->
This is the yield function of recreational boaters and fishing boats on Lake Ontario.

<!-- b000285 | prose | pages [16] -->
and are composite coefficients combining the number of them with the revenue brought in by them, predicting water use.[7]

<!-- b000286 | prose | pages [16] -->
This is the yield function of hydro-power generation companies. is a measure of the capacity of the generation system, predicting water use.[7] On this basis, we also need to establish the constraints that the water levels and flow rates we seek will not exceed or fall below the previous year's maximums. From this, we build the multi-objective optimization model:

<!-- b000287 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型

<!-- b000288 | furniture | pages [16] -->
2

<!-- b000289 | furniture | pages [16] -->
MATHmodels

<!-- b000290 | furniture | pages [16] -->
获取更多资讯

<!-- b000291 | furniture | pages [17] -->
Team # 2417004

<!-- b000292 | furniture | pages [17] -->
Page 17 of 25

<!-- b000294 | heading | pages [17] -->
6.3 Optimal water-level determination model based on NSGA-II algorithm

<!-- b000295 | prose | pages [17] -->
NSGA-II (Non-dominated Sorting Genetic Algorithm II) is a genetic algorithm for solving multi-objective optimization problems. It finds the Pareto optimal solution by iterating.

<!-- b000296 | prose | pages [17] -->
1. Coding and initializing populations First, the solution to the problem is encoded by using the binary operation. Each individual in the population represents a set of possible solutions, i.e., a set of values for water level (H) 微信号：MATHmodels and water flow (Q). For each individual, the values of water level (H) and water flow (Q) can be generated randomly within a given constraint. Combined with the complexity of this prob- lem, we chose an initial population size of 100 individuals.

<!-- b000297 | prose | pages [17] -->
2. Calculating Adaptation NSGA-II is a minimization problem solver, so we take the negative of these objective functions as the fitness function.

<!-- b000298 | prose | pages [17] -->
3. Undominated sorting and congestion calculation The NSGA-II algorithm will rank and select individuals in the population based on non- dominated ordering and crowding. Undominated ordering divides the population into multiple ranked frontiers, each containing individuals who are not dominated by each other.

<!-- b000299 | prose | pages [17] -->
The crowding degree comparison is used to differentiate between individuals within the same frontier, giving preference to individuals with lower crowding degrees (i.e., fewer neigh- bors around them) in order to maintain the diversity of the solution.

<!-- b000300 | prose | pages [17] -->
4. Selection, crossover, and mutation The selection operation is based on the tournament selection method, where parent indi- viduals are selected for crossover and mutation to produce a new generation of individuals.

<!-- b000301 | prose | pages [17] -->
5. Generation of new populations Combining parents and offspring, new populations are selected by non-dominated sorting and crowding calculations.

<!-- b000302 | prose | pages [17] -->
6. Iterating until the termination condition is met The above steps are repeated until a predetermined number of iterations is reached or the quality of the solution is no longer significantly improved.

<!-- b000303 | prose | pages [17] -->
Based on the above calculation process, R studio is used to solve equation (34) and used

<!-- b000304 | prose | pages [17, 18] -->
关注数学模型 such an algorithm as well as network flow graphs to solve for the optimal water levels of the Great Lakes from January to December. The results are shown below.

<!-- b000305 | furniture | pages [17] -->
2

<!-- b000306 | furniture | pages [17] -->
MATHmodels

<!-- b000307 | furniture | pages [17] -->
获取更多资讯

<!-- b000308 | furniture | pages [18] -->
Team # 2417004

<!-- b000309 | furniture | pages [18] -->
Page 18 of 25

<!-- b000311 | caption | pages [18] -->
Table 5: Optimal Water Level of the Great Lakes

<!-- b000312 | prose | pages [18] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000313 | caption | pages [18] -->
Figure 13: Comparison of optimum water level and average water level in recent years

<!-- b000314 | heading | pages [18] -->
6.4 Tests of the model using 2017 data

<!-- b000315 | prose | pages [18, 19] -->
In order to give a range of optimal water levels for subsequent testing, we divided the 12 months into seasons (March, April, and May for spring, and so on). The water level is said to 关注数学模型 be optimal if it is within the range of the corresponding quarter.

<!-- b000316 | furniture | pages [18] -->
2

<!-- b000317 | furniture | pages [18] -->
MATHmodels

<!-- b000318 | furniture | pages [18] -->
获取更多资讯

<!-- b000319 | furniture | pages [19] -->
Team # 2417004

<!-- b000320 | furniture | pages [19] -->
Page 19 of 25

<!-- b000322 | prose | pages [19] -->
On one hand, we first substitute 2017 data into the above formula 34, By calculations we find that the actual recorded water levels for the year are satisfactory, and are all within the 微信公众号：数学模型 range of the optimum level we are seeking.

<!-- b000323 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000324 | caption | pages [19] -->
Figure 14: The 2017 data under the new algorithm

<!-- b000325 | prose | pages [19] -->
On the other hand, by using the previous relationship between average annual water levels in the Great Lakes and water use, we can model multiple linear regressions.

<!-- b000326 | prose | pages [19] -->
Y is the amount of water used in the watershed, is the average annual water level in Lake Superior, is the average annual water level in Lake Michigan and Lake Huron, is the average annual water level in Lake Erie, is the average annual water level in Lake On- tario.

<!-- b000327 | prose | pages [19] -->
By substituting the data of 2017, we finally deduced that his water consumption is 130,860 million L, thus we can see that the water level is still within the optimal water level range, so we verified the accuracy of our model from another angle.

<!-- b000328 | prose | pages [19] -->
In short, from both perspectives, we can argue that for the various stakeholders, my new control method will indeed result in better actual recorded water levels for that year.

<!-- b000329 | heading | pages [19] -->
7  Sensitivity Analysis

<!-- b000330 | heading | pages [19] -->
7.1 Precipitation

<!-- b000331 | prose | pages [19] -->
The optimal water level is used in Lake Ontario in January as an example to verify the accuracy of the model.

<!-- b000332 | prose | pages [19, 20] -->
关注数学模型 微信公众号：数学模型

<!-- b000333 | furniture | pages [19] -->
2

<!-- b000334 | furniture | pages [19] -->
MATHmodels

<!-- b000335 | furniture | pages [19] -->
获取更多资讯

<!-- b000336 | furniture | pages [20] -->
Team # 2417004

<!-- b000337 | furniture | pages [20] -->
Page 20 of 25

<!-- b000339 | caption | pages [20] -->
Figure 15: The relationships between water Level and precipitation

<!-- b000340 | prose | pages [20] -->
As shown in the figure, the satisfaction gradually decreases with the increase of precipi- 微信号：MATHmodels tation and at a faster rate, while the optimal water level keeps fluctuating, indicating that the optimal water level is more sensitive to the precipitation.

<!-- b000341 | heading | pages [20] -->
7.2 Snowmelt

<!-- b000342 | prose | pages [20] -->
As shown in the figure, the satisfaction level gradually decreased with the increase of snowmelt, but the rate of decrease was not fast, and the satisfaction level was always above 0.97. Meanwhile the optimal water level keeps fluctuating. Therefore, it can be considered that the optimal water level is relatively insensitive to snowmelt and has strong robustness.

<!-- b000343 | caption | pages [20] -->
Figure 16: The relationships between water level and snowmelt

<!-- b000344 | prose | pages [20] -->
关注数学模型

<!-- b000345 | furniture | pages [20] -->
2

<!-- b000346 | furniture | pages [20] -->
MATHmodels

<!-- b000347 | furniture | pages [20] -->
获取更多资讯

<!-- b000348 | furniture | pages [21] -->
Team # 2417004

<!-- b000349 | furniture | pages [21] -->
Page 21 of 25

<!-- b000350 | heading | pages [21] -->
8  Model Evaluation

<!-- b000351 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000352 | heading | pages [21] -->
8.1 Strengths

<!-- b000353 | prose | pages [21] -->
1. The effects of water level, precipitation, ice jams, wind, and many other factors are considered in the advanced model.

<!-- b000354 | prose | pages [21] -->
2. Innovatively analyzing a synthetic model of wind on the lake and a baffle model of the dam.

<!-- b000355 | prose | pages [21] -->
3. Using NSGA-II genetic algorithm when solving multi-objective optimization, which combines neural network and symbolic reasoning with good robustness 4. The superiority of the model for solving the optimal water level has been verified in multiple ways, both in terms of water consumption and the new algorithm.

<!-- b000356 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000357 | heading | pages [21] -->
8.2 Weaknesses

<!-- b000358 | prose | pages [21] -->
1. The role of hydroelectric power stations and reservoirs on the Ottawa River in regulat- ing flow and the effect of groundwater level on lake level were not considered.

<!-- b000359 | prose | pages [21] -->
2. The training process of LSTM is relatively slow due to the complex gating mechanism and multiple weighting parameters.

<!-- b000360 | prose | pages [21] -->
3. Inadequate consideration of costs to hydroelectric utilities.

<!-- b000361 | prose | pages [21] -->
4. The algorithm fails to adequately consider whether sensitivity to ice plugs

<!-- b000362 | heading | pages [21] -->
8.3 Further discussion

<!-- b000363 | prose | pages [21] -->
Optimal water levels are in everyone's interest, and it is important to establish and main- tain optimal water levels that are appropriate to the location. The model used in this paper to establish and maintain optimal water levels for the Great Lakes can be generalized, with the appropriate parameter modifications, to a variety of areas other than those mentioned in this paper.

<!-- b000364 | prose | pages [21] -->
For example, it can be used to help planners to better design urban water systems, hydrau- lic facilities and flood control projects to improve the flood resilience and water utilization efficiency of cities. In addition, scientific water level management can protect wetland ecosys- tems, maintain habitats for aquatic plants and animals, and promote biodiversity conservation.

<!-- b000365 | heading | pages [21] -->
9  Conclusion

<!-- b000366 | prose | pages [21] -->
This study aims to address the challenge of control mechanisms for water levels in the Great Lakes region of North America, working to find an optimal solution between meeting stakeholder needs and protecting the ecological balance. By building a multi-layer model de- sign including a base network model and an advanced flow model and its sub-models, this

<!-- b000367 | prose | pages [21, 22] -->
关注数学模型 study successfully simulates and optimizes the water levels of the Great Lakes, and proposes practical management and control strategies, especially for the sub-problems of Lake Ontario and the St. Lawrence River. 微信公众号：数学模型 First, by constructing a base network model connecting the Great Lakes, we analyze the major streamflow processes and develop equations describing the streamflow and water avail- ability in the network with the provided data, which is the basis of the model. Subsequently, based on the base model, we develop a more complex advanced flow model to more accurately depict the complex factors that affect water flow, such as wind, snow, ice jams, and other me- teorological factors. Sensitivity analysis of the advanced model shows that the model was ex- tremely sensitive to rainfall and less sensitive to snowmelt.

<!-- b000368 | furniture | pages [21] -->
2

<!-- b000369 | furniture | pages [21] -->
MATHmodels

<!-- b000370 | furniture | pages [21] -->
获取更多资讯

<!-- b000371 | furniture | pages [22] -->
Team # 2417004

<!-- b000372 | furniture | pages [22] -->
Page 22 of 25

<!-- b000374 | prose | pages [22] -->
In order to identify a solution that would satisfy all stakeholders, we first create multiple benefit and cost functions, form an objective function, and construct a multi-objective optimi- zation model. The model is then solved using the NSGA-II algorithm by initializing the popu- 微信号：MATHmodels lation and operations such as selection, crossover, and mutation. Combined with the previous advanced flow model, the optimal water level is finally determined.

<!-- b000375 | prose | pages [22] -->
In addition, by utilizing 2017 data, this study verifies the high stability and accuracy of the model in terms of water use projection and computation of the new optimization algorithm. This not only reflects the effectiveness of the model in dealing with practical problems but also demonstrates its adaptability to possible future changes.

<!-- b000376 | prose | pages [22] -->
In conclusion, this study effectively simulates and optimizes water levels in the Great Lakes by constructing a complex and detailed model framework. It is our sincere hope that the management and control strategies proposed in this study will be adopted by the International Joint Commission (IJC) for the benefit of a sustainable future for the Great Lakes region. Look- ing forward, we believe that further research should focus on expanding the dataset, improving model accuracy, and enhancing interactions with stakeholders to ensure that our strategies maintain their effectiveness and relevance in a changing environment. In this way, we can not only protect this valuable natural resource, but also ensure that it continues to provide essential ecological, economic, and social benefits to people in the region and beyond.

<!-- b000377 | prose | pages [22] -->
关注数学模型

<!-- b000378 | furniture | pages [22] -->
2

<!-- b000379 | furniture | pages [22] -->
MATHmodels

<!-- b000380 | furniture | pages [22] -->
获取更多资讯

<!-- b000381 | furniture | pages [23] -->
Team # 2417004

<!-- b000382 | furniture | pages [23] -->
Page 23 of 25

<!-- b000383 | heading | pages [23] -->
10  Memo to IJC leadership

<!-- b000384 | prose | pages [23] -->
Date: February 6, 2024 微信公众号：数学模型 To: Leadership, IJC From: ICM Team #2417004

<!-- b000385 | heading | pages [23] -->
Subject: A Multi-Layer Optimization Model for the Great Lakes

<!-- b000386 | prose | pages [23] -->
Dear IJC leadership:

<!-- b000387 | prose | pages [23] -->
In response to your inquiry regarding the historical data utilized in our model and consid- ering the key features of Plan 2014, I would like to highlight the incorporation of the strengths of Plan 2014 into our proposal, along with targeted enhancements to address its identified shortcomings.

<!-- b000388 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000389 | heading | pages [23] -->
·Inheritance of Plan 2014's Strengths:

<!-- b000390 | heading | pages [23] -->
1  Ecological and Environmental Focus: Our model maintains a strong emphasis on

<!-- b000391 | prose | pages [23] -->
restoring lake and coastal ecosystems, contributing to overall ecological balance.

<!-- b000392 | heading | pages [23] -->
2  Optimized Water Level Management: Our model allows for increased flexibility in

<!-- b000393 | prose | pages [23] -->
lake water levels, accommodating fluctuations between high and low water levels.

<!-- b000394 | heading | pages [23] -->
·Addressing Plan 2014's Shortcomings:

<!-- b000395 | heading | pages [23] -->
1  Controversy and Dissatisfaction: Some stakeholders expressed reservations about

<!-- b000396 | prose | pages [23] -->
the new water level ranges and ecological goals.

<!-- b000397 | prose | pages [23] -->
2  High Water Events: Concerns were raised regarding potential impacts on shoreline properties and infrastructure during periods of high water levels.

<!-- b000398 | heading | pages [23] -->
3  Complexity due to Multiple Variables: The intricate interplay of meteorological,

<!-- b000399 | prose | pages [23] -->
hydrological, and ecological factors complicated predictions and management strategies.

<!-- b000400 | heading | pages [23] -->
·Our Solutions and Advantages:

<!-- b000401 | heading | pages [23] -->
1  Multi-Objective Optimization Model: We advocate for the implementation of a

<!-- b000402 | prose | pages [23] -->
multi-objective optimization model utilizing genetic algorithms. This model aims to determine water levels, achieving Pareto solutions that maximize the interests of various stakeholders.

<!-- b000403 | heading | pages [23] -->
2  Control Algorithm-based Flood Mitigation: Employing a sophisticated control al-

<!-- b000404 | prose | pages [23] -->
gorithm within a dynamic flow model, we intend to minimize the occurrence of high water events by regulating dam discharges effectively.

<!-- b000405 | heading | pages [23] -->
3  Comprehensive Impact Consideration: Our model takes into account the influence

<!-- b000406 | prose | pages [23] -->
of multiple factors, including precipitation, water levels, net total supply, wind, ice jams, snow accumulation, and more, addressing the complexity associated with Plan 2014.

<!-- b000407 | prose | pages [23] -->
Sincerely,

<!-- b000408 | furniture | pages [23] -->
Team #2417004

<!-- b000409 | prose | pages [23] -->
关注数学模型

<!-- b000410 | furniture | pages [23] -->
2

<!-- b000411 | furniture | pages [23] -->
MATHmodels

<!-- b000412 | furniture | pages [23] -->
获取更多资讯

<!-- b000413 | furniture | pages [24] -->
Team # 2417004

<!-- b000414 | furniture | pages [24] -->
Page 24 of 25

<!-- b000415 | heading | pages [24] -->
References

<!-- b000416 | references | pages [24] -->
[1] GLAM Committee, Great Lakes – St. Lawrence River Adaptive Management (GLAM) Committee

<!-- b000417 | references | pages [24] -->
微信公众号：数学模型

<!-- b000418 | references | pages [24] -->
Report for 2017, 2018

<!-- b000419 | references | pages [24] -->
[2] Current Perspectives on Lake Ontario-St. Lawrence River: Water Levels. (2023). Retrieved from In-

<!-- b000420 | references | pages [24] -->
ternational Lake Ontario - St. Lawrence River Board, https://ijc.org/en/loslrb/library/modules, Febru-

<!-- b000421 | references | pages [24] -->
ary 3, 2024

<!-- b000422 | references | pages [24] -->
[3] Historic Water Levels and Hydrologic Data such as flows, forecasts, wind, ice, and temperatures:

<!-- b000423 | references | pages [24] -->
Great Lakes Water Data and Related Information. (2023). Retrieved from Environment and Climate

<!-- b000424 | references | pages [24] -->
Change Canada, https://www.canada.ca/en/environment-climate-change/services/water over-

<!-- b000425 | references | pages [24] -->
view/quantity/great-lakes-levels-related-data.html, February 4, 2024

<!-- b000426 | references | pages [24] -->
[4] Reports on Great Lakes including water levels, forecasts, basin conditions and outflows: Great

<!-- b000427 | references | pages [24] -->
Lakes Information. (2023). Retrieved from US Corps of Engineers Detroit District,

<!-- b000428 | references | pages [24] -->
微信号：MATHmodels

<!-- b000429 | references | pages [24] -->
https://www.lre.usace.army.mil/Missions/Great-Lakes-Information/, February 3, 2024

<!-- b000430 | references | pages [24] -->
[5] Historic Perspectives specific to Ottawa River: Ottawa River at Carillon Station. (2023). Re-

<!-- b000431 | references | pages [24] -->
trieved from Ottawa River Regulational Planning Board, https://ottawariver.ca/information/his-

<!-- b000432 | references | pages [24] -->
torical-waterlevel-streamflow-summary/ottawa-river-at-carillon/, February 6, 2024

<!-- b000433 | references | pages [24] -->
[6] China Science Communication Science Encyclopedia, minimum navigable stage of channel, 2015

<!-- b000434 | references | pages [24] -->
[7] Historic Water Use Data such as withdrawals, diversions and consumption: Great Lakes Re-

<!-- b000435 | references | pages [24] -->
gional Water Use Database. (2023). Retrieved from Great Lakes Commission,

<!-- b000436 | references | pages [24] -->
https://www.gic.org-Water Use Sector Definitions, February 5, 2024

<!-- b000437 | heading | pages [24] -->
Appendix

<!-- b000438 | prose | pages [24] -->
Note: To avoid copyright infringement, all the contents in the essay are written on our own.

<!-- b000439 | prose | pages [24, 25] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000440 | furniture | pages [24] -->
2

<!-- b000441 | furniture | pages [24] -->
MATHmodels

<!-- b000442 | furniture | pages [24] -->
获取更多资讯

<!-- b000443 | furniture | pages [25] -->
Team # 2417004

<!-- b000444 | furniture | pages [25] -->
Page 25 of 25

<!-- b000446 | prose | pages [25] -->
关注数学模型

<!-- b000447 | furniture | pages [25] -->
2

<!-- b000448 | furniture | pages [25] -->
MATHmodels

<!-- b000449 | furniture | pages [25] -->
获取更多资讯
