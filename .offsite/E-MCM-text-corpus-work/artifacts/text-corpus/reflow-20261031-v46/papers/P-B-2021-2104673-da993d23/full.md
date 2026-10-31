# P-B-2021-2104673-da993d23

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem chosen 2021 MCM/ICM Summary Sheet Team Control Number B 2104673

<!-- b000002 | title | pages [1] -->
‘Rapid Bushfire Response’ UAV System

<!-- b000003 | heading | pages [1] -->
summary

<!-- b000004 | prose | pages [1] -->
Due to the drought of southeast Australia, forest fires burn across the country, impacting New South Wales and eastern Victoria. To help Victoria government response to future wildfire disasters, we established the ‘Rapid Bushfire Response’ system.

<!-- b000005 | prose | pages [1] -->
For model 1, to address the irregularity of fire regions and SSA drones’ information acquisition areas, we used regional discretization method, turning fire data and multi-drone cooperation in to constraint equations. We then divide the information in discreated area into different layers, the drone layer and information layer indicate an SSA drone’s different search mode and search zone, and the flame layer represents the severity of wildfire, we optimized SSA drone’s search pattern balancing information detection revenue and SSA drone numbers. Finally, we optimized the location of EOC and repeater with the further obtained SSA drone location while considering communication constrains and drones’ traveling distance.

<!-- b000006 | prose | pages [1] -->
For model 2, we discussed the changes in fire under global warming circumstances. We first formed a two-level function that maps temperature to average fire probability, and average fire probability to burned area size. To obtain the equation, we build cellular automata to simulate fire probability’s effect on burned area and fitted the relation between temperature and fire probability. We then estimated the temperature variance due to climate change from further studies and calculated the estimated average fire probability of this year and the next decade. Finally, we simulated average fire scenes and estimated their fire severity.

<!-- b000007 | prose | pages [1] -->
For model 3, while referring to the number of SSA drones obtained without terrain conditions, we refined the regional discretization model to bring into the terrain influence. For SSA drones, we considered topographical influence on a drone’s traveling time and discussed path planning considering the varying time cost of different areas. As for repeaters, we evaluated the influence of terrain on communication, and measures a regions’ communication shielding effect with the terrain’s second gradient. We then further considered the reliability of communication and estimated the schedule change in different terrains.

<!-- b000008 | prose | pages [1] -->
Based on the above three models, we estimated that 10 SSA drones and 2 radio repeater drones is required to build the ‘Rapid Bushfire Response’ system. For next decade, the cost of imaging cameras and telemetry sensors (for SSA drones) will increase. We also suggest that while fire zone area has an influence on drone arrangements, topographical conditions plays a less important role.

<!-- b000009 | keywords | pages [1] -->
Keyword: Drone, Optimization, Regional Discretization, Fire Dynamic Models, Cellular Automata

<!-- b000010 | furniture | pages [1] -->
微信公众号：数学模型 微信号：MATHmodels 微信公众号：数学模型 微信号：MATHmodels 关注数学模型 获取更多资讯 2 MATHmodels

<!-- b000011 | furniture | pages [2] -->
Team #2104673 Page 1 of 25

<!-- b000012 | heading | pages [2] -->
Content

<!-- b000013 | source_object | pages [2] -->
summary .......................................................................................................................................... 1 1 Introduction ........................................................................................................................... 2 1.1 Problem Background ......................................................................................................... 2 1.2 Restatement of the Problem ............................................................................................... 2 1.3 Model Framework ............................................................................................................. 3 2 Assumptions and Justifications ............................................................................................. 3 3 Notations ................................................................................................................................ 4 3.1 Notations used in this paper ............................................................................................... 4 4 Model Derivation ................................................................................................................... 6 4.1 Model Preparation ............................................................................................................. 6 4.2 Model 1: SSA Drones Optimization Model ........................................................................ 7 4.3 Model 2: CA Fire Prediction model ................................................................................... 9 4.4 Model 3: Ratio-Repeater Drones Optimization Model ...................................................... 13 5 Test the Model ...................................................................................................................... 15 5.1 Model 1 Sensitivity Analysis ........................................................................................... 15 5.2 Model 2 Sensitivity Analysis ........................................................................................... 16 6 Conclusion ............................................................................................................................ 17 6.1 Summary of Results......................................................................................................... 17 7 Model Evaluation and Further Discussion.......................................................................... 19 7.1 Strengths ......................................................................................................................... 19 7.2 Possible Improvements .................................................................................................... 19 8 Budget Request .................................................................................................................... 21 References ................................................................................................................................... 19

<!-- b000014 | furniture | pages [2] -->
微信公众号：数学模型 微信号：MATHmodels 微信公众号：数学模型 微信号：MATHmodels 关注数学模型 获取更多资讯 2 MATHmodels

<!-- b000015 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000016 | furniture | pages [3] -->
Team #2104673

<!-- b000017 | furniture | pages [3] -->
Page 2 of 25

<!-- b000018 | heading | pages [3] -->
1 Introduction

<!-- b000019 | heading | pages [3] -->
1.1 Problem Background

<!-- b000020 | prose | pages [3] -->
微信公众号：数学模型 Since September 2019, mountain fires in Australia have been burning for more than 200 days, cover- ing an area of nearly 6 million hectares. The fire in Australia is equivalent to burning half of Jiangsu, three Beijing and two Belgium, which is 7 times of the Amazon rainforest fire that shocked the world (burning 900000 hectares of land), and 60 times of the California fire last year (burning 102000 hec- tares of land).

<!-- b000021 | prose | pages [3] -->
There were 39 fires in Victoria, the second most serious state, which destroyed 300 houses. The in- surance commission estimated the loss at a $700 million. Victoria is a state located on the southeast coast of Australia, and adjacent to South Australia and New South Wales in the north and west re- spectively. It is the smallest continental state in Australia. The northeast is a mountainous area with towering peaks, mostly between 1000 and 2000 meters above sea level.

<!-- b000022 | prose | pages [3] -->
Due to the extremely large wildfire and a great number of injured citizens and firefighters, the im- 微信号：MATHmodels portance of drone-detection system is found. It can be widely used in aerial photography, environ- mental detection and other fields, and has a huge industrial prospect [1]. For a sudden wildfire, no matter in the early or middle stage of a fire, we can detect real-time data and communicate with firefighters through UAV system.

<!-- b000023 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000024 | prose | pages [3] -->
We need to develop a wildfire disaster relief response system named “Rapid Bushfire Response” and improve its response capabilities based on the situations of Victoria, Australia.

<!-- b000025 | prose | pages [3] -->
⚫ What we Know:

<!-- b000026 | prose | pages [3] -->
➢ Distribution of wildfire severity of Australia ➢ Geographic information of Southeast Australia

<!-- b000027 | prose | pages [3] -->
⚫ What we Have:

<!-- b000028 | prose | pages [3] -->
➢ 2 kinds of drones. SSA drones are used for video & telemetry and Radio Repeater drones are used to extend the range of low power radios on the front lines.

<!-- b000029 | prose | pages [3] -->
➢ 1 mobile EOC. central command and control point for emergency related operations and ac- tivities, and for requests for activation and deployment of resources

<!-- b000030 | prose | pages [3] -->
⚫ What we Should Do:

<!-- b000031 | prose | pages [3] -->
➢ Determine the type and number of UAV. The UAV fleet should satisfy and balance the need of capability, safety and economics.

<!-- b000032 | prose | pages [3] -->
➢ Identify the most-demanded locations for SSA drones. SSA drones has the capability of video & telemetry so that they are the main part of UAV fleet to guarantee the safety of fire- fighters and the data of the most serious fire areas ➢ Identify the best hovering locations for radio-repeater drones. Radio-repeater drones are the core of several SSA drones to transmit information to EOC.

<!-- b000033 | prose | pages [3] -->
➢ Propose dispatching schedule. Assign flight plan to each type of drones to ensure the Con- tinuous information transmission.

<!-- b000034 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000035 | prose | pages [3, 4] -->
关注数学模型 The simple structure of the “Rapid Bushfire Response” UAV system is shown in figure 1.1.

<!-- b000036 | furniture | pages [3] -->
2

<!-- b000037 | furniture | pages [3] -->
MATHmodels

<!-- b000038 | furniture | pages [3] -->
获取更多资讯

<!-- b000039 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000040 | furniture | pages [4] -->
Team #2104673

<!-- b000041 | furniture | pages [4] -->
Page 3 of 25

<!-- b000043 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000044 | caption | pages [4] -->
Figure 1 “Rapid Bushfire Response” UAV system

<!-- b000045 | heading | pages [4] -->
1.3 Model Framework

<!-- b000046 | prose | pages [4] -->
In this paper, we establish three models to solve the problem. Firstly, because this model is estab- lished to monitor wildfire, and is incapable of monitoring the whole area. We define a variable to determine the observation revenue of UAV in a certain area in a certain period. Secondly, to balance 微信号：MATHmodels the capability, safety and economics, the number of SSA drones and the location of EOC are opti- mized by using the optimization model according to the size of the fire and the frequency of the fire. And we use the number of SSA drones to optimize the number and the location of ratio repeater drones. In the last, we built a model to simulate the size and scale of the possible wildfires in the next decade based on the Cellular Automata model. And then we substituted the predicted data to the model we built to testify whether model adapts to the changing likelihood of extreme fire events over the next decade. The overall algorithm flow chart of the model is shown in the figure 2:

<!-- b000047 | caption | pages [4] -->
Figure 2 Model Overview

<!-- b000048 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000049 | heading | pages [4] -->
1. The UAV will not be damaged or malfunction during the mission.

<!-- b000050 | prose | pages [4] -->
Justification: The probability of UAV's sudden damage due to its own reasons during the mission is ignored.

<!-- b000051 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000052 | prose | pages [4, 5] -->
关注数学模型 2. All drones can only be recharged in the Emergency Operations Center and they are fully charged when leaving the Emergency Operations Center.

<!-- b000053 | furniture | pages [4] -->
2

<!-- b000054 | furniture | pages [4] -->
MATHmodels

<!-- b000055 | furniture | pages [4] -->
获取更多资讯

<!-- b000056 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000057 | furniture | pages [5] -->
Team #2104673

<!-- b000058 | furniture | pages [5] -->
Page 4 of 25

<!-- b000060 | prose | pages [5] -->
Justification: Due to a large forest fire in the mission area, we conclude that the electrical equip- ment in the area is not working properly.

<!-- b000061 | prose | pages [5] -->
微信公众号：数学模型 3. All drones fly at the maximum speed of 20m/s until they reach the designated location.

<!-- b000062 | prose | pages [5] -->
Justification: This is because the drones has the limitation of flight time. Flying at the maximum speed can minimize the time consumed on the road to make the mission time as long as possible. 4. The ascending and descending process of UAV is not considered.

<!-- b000063 | prose | pages [5] -->
Justification: This is because drones have very short ascent and descent times compared to flight times. 5. The terrain and weather do not have influence in the performance of drones.

<!-- b000064 | prose | pages [5] -->
Justification: Because the drones are hovering well above the ground, the terrain doesn’t affect the speed and battery life of drones. Meanwhile, the influence of weather on the performance of drones is ignore. 6. The atmosphere temperature has no effect on the battery life of drones. 微信号：MATHmodels Justification: Because the drones are hovering well above the ground, the atmosphere temperature doesn’t affect the battery life of drones and battery life. 7. Each UAV is regarded as a particle in the model Justification: The shape, size and mass of UAV have no influence on the performance of drones. 8. The spread of the flame has nothing to do with the terrain.

<!-- b000065 | prose | pages [5] -->
Justification: For the cellular automata model, the probability of flame propagation from a certain area to all surrounding areas is the same. Therefore, this model ignores the influence of terrain on flame propagation. 9. In the next ten years, the temperature changes with time, and the humidity and wind speed do not change.

<!-- b000066 | prose | pages [5] -->
Justification: For 3 factors that affect the probability of fire propagation, the humidity and wind speed aren’t influenced by the global warming, which is regarded as constant value. And the tem- perature will increase slowly in the next decade.

<!-- b000067 | heading | pages [5] -->
3 Notations

<!-- b000068 | heading | pages [5] -->
3.1 Notations used in this paper

<!-- b000069 | caption | pages [5] -->
Table 1 Notations used in this paper

<!-- b000070 | prose | pages [5] -->
Symbol Description Unit

<!-- b000071 | prose | pages [5] -->
Maximum speed of drones km/hr

<!-- b000072 | prose | pages [5] -->
The element division method of the rectangular fire area, M is the num- - ber of elements of one side

<!-- b000073 | prose | pages [5] -->
S The number of the location of radio repeater -

<!-- b000074 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000075 | prose | pages [5, 6] -->
关注数学模型 The range of low power radios on the front lines km

<!-- b000076 | furniture | pages [5] -->
2

<!-- b000077 | furniture | pages [5] -->
MATHmodels

<!-- b000078 | furniture | pages [5] -->
获取更多资讯

<!-- b000079 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000080 | furniture | pages [6] -->
Team #2104673

<!-- b000081 | furniture | pages [6] -->
Page 5 of 25

<!-- b000083 | prose | pages [6] -->
The range of radio repeater’s signal km

<!-- b000084 | prose | pages [6] -->
Maximum flight time hr 微信公众号：数学模型 Recharge time for the built-in battery of drones hr

<!-- b000085 | prose | pages [6] -->
The docking time of the drone in this area hr

<!-- b000086 | prose | pages [6] -->
km2 Coverage area of the detected area

<!-- b000087 | prose | pages [6] -->
km2 The area of the largest square that UAV can cover

<!-- b000088 | prose | pages [6] -->
Detection range of UAV km

<!-- b000089 | prose | pages [6] -->
The flight range of WileE-15.2X Hybrid Drone km

<!-- b000090 | prose | pages [6] -->
微信号：MATHmodels The location of Emergency Operations Center -

<!-- b000091 | prose | pages [6] -->
The location of radio repeater drone -

<!-- b000092 | prose | pages [6] -->
State variable indicating whether the SSA drone is in this area.

<!-- b000093 | prose | pages [6] -->
means the drone is in this area; means the drone is not in this - area.

<!-- b000094 | prose | pages [6] -->
State variable indicating whether the ratio repeater drone is in this area.

<!-- b000095 | prose | pages [6] -->
means the drone is in this area; means the drone is not - in this area.

<!-- b000096 | prose | pages [6] -->
The amount of information acquired by UAV in this area -

<!-- b000097 | prose | pages [6] -->
The severity of the fire in this area. -

<!-- b000098 | prose | pages [6] -->
Minimum transit time of the unit -

<!-- b000099 | prose | pages [6] -->
Sequence of UAV passing through units -

<!-- b000100 | prose | pages [6] -->
The state value of each unit area’s fire state in the cellular automata. -

<!-- b000101 | prose | pages [6] -->
UAV detection performance index -

<!-- b000102 | prose | pages [6] -->
Monitoring types of SSA drones -

<!-- b000103 | prose | pages [6] -->
The boundary parameter -

<!-- b000104 | prose | pages [6] -->
T Ground temperature in fire area (before fire) ℃

<!-- b000105 | prose | pages [6] -->
The influence factors in the cellular automata model. It will affect the - area and distribution of the fire

<!-- b000106 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000107 | prose | pages [6] -->
关注数学模型

<!-- b000108 | furniture | pages [6] -->
2

<!-- b000109 | furniture | pages [6] -->
MATHmodels

<!-- b000110 | furniture | pages [6] -->
获取更多资讯

<!-- b000111 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000112 | furniture | pages [7] -->
Team #2104673

<!-- b000113 | furniture | pages [7] -->
Page 6 of 25

<!-- b000114 | heading | pages [7] -->
4 Model Derivation

<!-- b000115 | heading | pages [7] -->
4.1 Model Preparation

<!-- b000116 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000117 | heading | pages [7] -->
4.1.1 The Data

<!-- b000118 | heading | pages [7] -->
1. Data Collection

<!-- b000119 | prose | pages [7] -->
The data we used mainly include Elevation data of southwest Australia, Australian wildfire data set, Forest fire areas in Australia_ 2019-2020, Global Forest Watch. The data sources are summarized in

<!-- b000120 | caption | pages [7] -->
Table 2.

<!-- b000121 | caption | pages [7] -->
Table 2 Data source collation

<!-- b000122 | prose | pages [7] -->
Database Names Database Websites Data Type Elevation data of southwest Australia https://topex.ucsd.edu/cgi-bin/get_data.cgi Geography https://www.kesci.com/mw/da- Australian wildfire data set Geography taset/5e21588a2823a10036b575bf 微信号：MATHmodels Forest fire areas in Australia_ 2019- https://www.datafountain.cn/datasets/5395 Geography 2020 Global Forest Watch https://www.globalforestwatch.org/ Geography https://github.com/var- FW_Veg_Rem_Combined unr89/smokey/blob/master/Wild- Climate fire_att_description.txt

<!-- b000123 | heading | pages [7] -->
2. Data Cleaning

<!-- b000124 | prose | pages [7] -->
According to the latitude and longitude range and the administrative boundary of Victoria, Australia, we extracted data of terrain and fire details of Victoria from all the data. The fire in Victoria is shown in the figure 3 below.

<!-- b000125 | caption | pages [7] -->
Figure 3 Topographic map and brief contour of Southeast Australia

<!-- b000126 | heading | pages [7] -->
4.1.2 Geographic Coordinate System

<!-- b000127 | prose | pages [7] -->
We have collected the geographic coordinates (longitude and latitude) of Victoria. To find the true distance between any two points in the map, we map the spherical coordinate system to the plane rectangular coordinate system. With the latitude and longitude range of the fire area, a rectangular fire field area can be obtained in a rectangular coordinate system. The linear distance between any

<!-- b000128 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000129 | prose | pages [7, 8] -->
关注数学模型 two points in the rectangular coordinate system is the actual distance between the two places.

<!-- b000130 | furniture | pages [7] -->
2

<!-- b000131 | furniture | pages [7] -->
MATHmodels

<!-- b000132 | furniture | pages [7] -->
获取更多资讯

<!-- b000133 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000134 | furniture | pages [8] -->
Team #2104673

<!-- b000135 | furniture | pages [8] -->
Page 7 of 25

<!-- b000137 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000138 | caption | pages [8] -->
Figure 4 Spherical coordinate transformation

<!-- b000139 | heading | pages [8] -->
4.2 Model 1: SSA Drones Optimization Model

<!-- b000140 | prose | pages [8] -->
Due to area detection requirements, UAVs continuously monitor fire regions. However, limited by power and communication, it is impossible to detect all regions of interest continuously. Therefore, 微信号：MATHmodels We optimized the detection time of different regions according to their importance. [2]

<!-- b000141 | heading | pages [8] -->
4.2.1 Regional Discretization Model

<!-- b000142 | prose | pages [8] -->
We first discretize the area into a M×N matrix, each unit area is which is the minimum transmit area of 5-watt transmitters. We then divide the matrix in to 4 layers to analyze different information, the time layer (t, a matrix representing the hover time of the unit), the drone layer (x, a 0-1 state variable matrix representing a drone’s hovering zone and t, a matrix storing a drone’s hovering time), the information layer (I, a matrix representing the information SSA drones collected form the unit) and the flame layer (h vector representing the severity of wildfire). We combine these three layers to optimize the number of SSA drones and balance the capability and economics.

<!-- b000143 | caption | pages [8] -->
Figure 5 different levels in the optimization model

<!-- b000144 | prose | pages [8] -->
Considering a SSA drone’s power limitations, we hypothesize that a drone detects one or two block at once, hence a SSA drones has 5 different detection modes:

<!-- b000145 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000146 | prose | pages [8, 9] -->
关注数学模型 微信公众号：数学模型 As we identify each detection mode with the position of its upper left corner, we could represent a

<!-- b000147 | furniture | pages [8] -->
2

<!-- b000148 | furniture | pages [8] -->
MATHmodels

<!-- b000149 | furniture | pages [8] -->
获取更多资讯

<!-- b000150 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000151 | furniture | pages [9] -->
Team #2104673

<!-- b000152 | furniture | pages [9] -->
Page 8 of 25

<!-- b000153 | caption | pages [9] -->
Figure 6 detection modes of SSA drones

<!-- b000155 | prose | pages [9] -->
drones detection behavior by dividing the drone layer into 5 sub-layers, and . For drone

<!-- b000156 | prose | pages [9] -->
layers we have:

<!-- b000157 | prose | pages [9] -->
(1)

<!-- b000158 | prose | pages [9] -->
For the amount of information acquired by UAV in a certain area , we have:

<!-- b000159 | prose | pages [9] -->
(2) 微信号：MATHmodels For the variables in equation 1,

<!-- b000160 | prose | pages [9] -->
(3)

<!-- b000161 | prose | pages [9] -->
In multiple-goods-condition, we consider the drones optimization problem as a Multiple-objective

<!-- b000162 | prose | pages [9] -->
integer programming problem. Therefore, the objective function of the optimization model is

<!-- b000163 | prose | pages [9] -->
(4)

<!-- b000164 | prose | pages [9] -->
where represents the total number of SSA UAVs, Here serves as an threshold, It prevents the

<!-- b000165 | prose | pages [9] -->
algorithm from adding drones when a new drone’s contribution is smaller than , balancing economic needs and

<!-- b000166 | prose | pages [9] -->
fire zone detection. represents the detection revenue of SSA drones. is the severity of the

<!-- b000167 | prose | pages [9] -->
fire area (i,j), As “Boots-on-the-ground” Teams faces more danger in severe areas, The higher the value of , the

<!-- b000168 | prose | pages [9] -->
more valuable the information of this fire unit is. is calculated with emulations methods and will be further

<!-- b000169 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000170 | prose | pages [9, 10] -->
关注数学模型 discussed in the next section.

<!-- b000171 | furniture | pages [9] -->
2

<!-- b000172 | furniture | pages [9] -->
MATHmodels

<!-- b000173 | furniture | pages [9] -->
获取更多资讯

<!-- b000174 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000175 | furniture | pages [10] -->
Team #2104673

<!-- b000176 | furniture | pages [10] -->
Page 9 of 25

<!-- b000178 | heading | pages [10] -->
4.2.2 EOC Constraint Conditions

<!-- b000179 | prose | pages [10] -->
微信公众号：数学模型 Apart from constrains with in the regional discretization model, we have

<!-- b000180 | prose | pages [10] -->
⚫ The EOC locates inside the discrete zone.

<!-- b000181 | prose | pages [10] -->
(5)

<!-- b000182 | prose | pages [10] -->
⚫ The EOC locates outside the fire.

<!-- b000183 | prose | pages [10] -->
(6)

<!-- b000184 | prose | pages [10] -->
Equation 6 casts no effect when is zero, yet when is not zero which indicates fire, it restrains from being zero, hence EOC will not be optimized in to firezone. 微信号：MATHmodels

<!-- b000185 | heading | pages [10] -->
4.2.3 Terrain Adapting Regional Discretization Model

<!-- b000186 | prose | pages [10] -->
To further adapt the integer programming discretization model, we introduced path planning to con- sider the cost of complex terrain. We assume that as SSA drones pass each area unit, it’s time cost varies according to the height change, hence we could brought in terrain information in the form of minimum passing time g. Furthermore to indicate a drone’s flying behavior, we introduced o, is zero when unit area (i,j) is not in the drone’s path, hence we have:

<!-- b000187 | prose | pages [10] -->
(7)

<!-- b000188 | prose | pages [10] -->
To ensure all are marked on the path ( is not zero only when is not zero), we have:

<!-- b000189 | prose | pages [10] -->
(8)

<!-- b000190 | prose | pages [10] -->
As a drone’s path is continuous, we must constrain the connectivity of matrix o’s non-zero elements. To achieve this, we restrict to be integer and gradually increases as SSA travels unit by unit, while appointing the starting point to be 1, we have:

<!-- b000191 | prose | pages [10] -->
(9)

<!-- b000192 | prose | pages [10] -->
While

<!-- b000193 | prose | pages [10] -->
(10)

<!-- b000194 | prose | pages [10] -->
The model could be optimized with the same target as the regional discretization model.

<!-- b000195 | heading | pages [10] -->
4.3 Model 2: CA Fire Prediction model

<!-- b000196 | prose | pages [10] -->
Considering the lack of spatial distribution data of fire field, we use cellular automata model to sim-

<!-- b000197 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000198 | prose | pages [10, 11] -->
关注数学模型 ulate the fire field distribution in a rectangular area. In the simulation process, there are two parame- ters related to temperature. Considering global warming, these two parameters will change with time, thus affecting the area and distribution of fire field. Therefore, the model can be used to predict the fire distribution in the next ten years and optimize the number and types of SSA drones.

<!-- b000199 | furniture | pages [10] -->
2

<!-- b000200 | furniture | pages [10] -->
MATHmodels

<!-- b000201 | furniture | pages [10] -->
获取更多资讯

<!-- b000202 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000203 | furniture | pages [11] -->
Team #2104673

<!-- b000204 | furniture | pages [11] -->
Page 10 of 25

<!-- b000206 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000207 | heading | pages [11] -->
4.3.1 Simulation of the Wildfire

<!-- b000208 | heading | pages [11] -->
1. Simulation Preparation

<!-- b000209 | prose | pages [11] -->
In order to build cellular automata to simulate the fire severity distribution, it is necessary to determine the state of the unit area. In this paper, we set up three states: after-burning, burning and unburned. And Considering the duration of combustion, this model defines a life for the fire of each point. If firing, the state value of this point decreases by 1 as time increases by 1. Therefore, . represents the unburned state; represents the burn- ing state, whose value represents the residual life of the unit; represents the after-burning state of the unit.

<!-- b000210 | prose | pages [11] -->
微信号：MATHmodels What’s more, note that the ‘unit area’ of this model is different from the ‘unit area’ in the previous model. The ‘unit area’ in this model is the subset of the ‘unit area’ in the previous model, representing the fire state in this area, thus determining the severity of fire in the larger ‘unit area’.

<!-- b000211 | prose | pages [11] -->
After determining the unit area state, we build a fire field, which is the same as the fire field in the previous model, but the division of unit area is different. The unit area is much smaller so that high accuracy can be obtained.

<!-- b000212 | prose | pages [11] -->
Next, considering the probability of unit fire in the fire region, whether a certain point in a fire is on fire at a certain time depends on the distance from the known ignition point. At each time, the ignition probability of each point is obtained by applying the gaussian filter of MATLAB to the whole matrix. When the probability value of the point divided by the critical probability value is large than the random number, then at this moment, the point becomes a new ignition point, that is, be- comes .

<!-- b000213 | heading | pages [11] -->
2. Simulation Method

<!-- b000214 | prose | pages [11] -->
The simulation algorithm is as follows: Firstly, the four points in the center of the fire site are set as fire, namely becomes . Secondly, the probability of a new fire point at the next mo- ment is calculated and compared with the critical probability to get the location of the new fire point. Thirdly, the state variable of ignition point, that is, the unit state value , minus one. Fourthly, judge the probability that the fire of all units will be extinguished. If the extinction proba- bility of the unit flame is less than the critical extinction probability, the state variable at this point becomes 0, that is, . Fifthly, update the burning-time matrix for judgment of flame severity. In the last, recalculate the ignition probability of all points. The specific algorithm flow chart is as follows.

<!-- b000215 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000216 | prose | pages [11, 12] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000217 | furniture | pages [11] -->
2

<!-- b000218 | furniture | pages [11] -->
MATHmodels

<!-- b000219 | furniture | pages [11] -->
获取更多资讯

<!-- b000220 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000221 | furniture | pages [12] -->
Team #2104673

<!-- b000222 | furniture | pages [12] -->
Page 11 of 25

<!-- b000224 | caption | pages [12] -->
Figure 7 Algorithm of fire simulation model based on Cellular Automata

<!-- b000225 | prose | pages [12] -->
We can simulate the process of this year's Australian mountain fire through simulation, and the sim- ulation results are as follows

<!-- b000226 | caption | pages [12] -->
Figure 8 Simulation result of wildfire course based on the cellular automata

<!-- b000227 | prose | pages [12] -->
In this model, there exist two parameters, the critical fired probability and critical unfired proba- bility . These two parameters can decide the wildfire distribution. For the critical fired probability, the value of it is determined by the temperature before wildfire happens, which means it has a rela- tionship with the global warming. For the critical unfired probability, it’s the same for the different wildfire events for the decade. But the critical unfired probability will increase as the fire scale in- creases.

<!-- b000228 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000229 | prose | pages [12, 13] -->
关注数学模型 As for how to determining the severity of the fire, we accumulate the time each point is burned and rescaled to 0-1 as fire are more severe at the starting point. We then transforms it into a M×N dimen- sional matrix to characterize the spatial severity distribution of the fire, which is the value we used for the last model. We can visualize this matrix as follows 微信公众号：数学模型

<!-- b000230 | furniture | pages [12] -->
2

<!-- b000231 | furniture | pages [12] -->
MATHmodels

<!-- b000232 | furniture | pages [12] -->
获取更多资讯

<!-- b000233 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000234 | furniture | pages [13] -->
Team #2104673

<!-- b000235 | furniture | pages [13] -->
Page 12 of 25

<!-- b000237 | caption | pages [13] -->
Figure 9 Fire severity matrix (5 times simulations)

<!-- b000238 | prose | pages [13] -->
微信号：MATHmodels The lighter the color in the figure, the lower the flame severity of the unit.

<!-- b000239 | heading | pages [13] -->
4.3.2 The Influence of Global Warming on Wildfire Simulation

<!-- b000240 | prose | pages [13] -->
To analyze the impact of global warming on this model, we established the following relationships. Firstly, by traversing the critical fire probability from 0.7 to 0.95, we get the simulation results be- tween the critical fire probability and the fire area size. Then the relationship between the two varia- bles is determined by curve fitting tool of MATLAB, which is shown as below.

<!-- b000241 | prose | pages [13] -->
(11)

<!-- b000242 | prose | pages [13] -->
Through the fire data of this year's Australian fire, we can get the relevant data of the fire area and the average temperature of the area before the fire. By using the above formula (1.6), we can trans- form the fire area data into different probability value so that we can get the relationship between the critical fire probability and average temperature of the area.

<!-- b000243 | prose | pages [13] -->
(12)

<!-- b000244 | prose | pages [13] -->
Finally, when analyzing the relationship between time and temperature, the temperature we find that the change of temperature includes seasonal periodic change and long-term growth change. For the annual temperature prediction, we can ignore the seasonal periodic change of temperature. Therefore, the temperature in this area increases exponentially with time. Due to an average temperature rise of 1.5 degrees Celsius over the past 50 years, their relationship is as follows

<!-- b000245 | prose | pages [13] -->
(13)

<!-- b000246 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000247 | prose | pages [13, 14] -->
关注数学模型 微信公众号：数学模型 (a) The relationship between the (b) The relationship between the (c) The relationship between the critical fire probability and the critical average temperature and critical time and the average wildfire area the fire probability temperature (global warming)

<!-- b000248 | furniture | pages [13] -->
2

<!-- b000249 | furniture | pages [13] -->
MATHmodels

<!-- b000250 | furniture | pages [13] -->
获取更多资讯

<!-- b000251 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000252 | furniture | pages [14] -->
Team #2104673

<!-- b000253 | furniture | pages [14] -->
Page 13 of 25

<!-- b000255 | caption | pages [14] -->
Figure 10 Relationship between fire area and critical ignition point probability

<!-- b000256 | prose | pages [14] -->
With all mentioned above, we can get the critical fire probability of this year and ten years later . Taking them into the simulation model, we can get the difference of fire dis- 微信号：MATHmodels tribution between this year and 10 years later. Finally, the demand change of UAV system can be determined.

<!-- b000257 | heading | pages [14] -->
4.4 Model 3: Ratio-Repeater Drones Optimization Model

<!-- b000258 | prose | pages [14] -->
Due to the continuity of communication requirements, the radio repeater UAV needs to hover at a certain position all the time as the intermediate of the signal. According to the location and number of the SSA drones. We can get the location and number of radio repeater drones by optimization model.

<!-- b000259 | heading | pages [14] -->
4.4.1 Influence of Terrain on Radio Range

<!-- b000260 | prose | pages [14] -->
Considering the influence of terrain on the drone communication, we extract terrain data from a fire region in Victoria. The matrix is denoted as . Laplace operator is used for the terrain data matrix to obtain the change amplitude of terrain is obtained. Then the rate of change data is converted into the signal transmission range data of the place. The specific transformation methods are as follows.

<!-- b000261 | prose | pages [14] -->
(14)

<!-- b000262 | prose | pages [14] -->
is the parameter make sure the range of value is . This matrix represents the signal receiving range of SSA drone at the fire region for each unit.

<!-- b000263 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000264 | prose | pages [14, 15] -->
关注数学模型 微信公众号：数学模型

<!-- b000265 | furniture | pages [14] -->
2

<!-- b000266 | furniture | pages [14] -->
MATHmodels

<!-- b000267 | furniture | pages [14] -->
获取更多资讯

<!-- b000268 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000269 | furniture | pages [15] -->
Team #2104673

<!-- b000270 | furniture | pages [15] -->
Page 14 of 25

<!-- b000272 | caption | pages [15] -->
Figure 11 the signal receiving range of SSA drone at the fire region for each unit

<!-- b000273 | heading | pages [15] -->
4.4.2 Radio Repeater Drones Optimization Model

<!-- b000274 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000275 | heading | pages [15] -->
1. Optimization objective

<!-- b000276 | prose | pages [15] -->
The optimization object is sum of distance between ratio repeater and EOC.

<!-- b000277 | prose | pages [15] -->
(15)

<!-- b000278 | heading | pages [15] -->
2. Constraint Conditions

<!-- b000279 | prose | pages [15] -->
⚫ The distance between UAV and EOC is less than the flight distance of UAV.

<!-- b000280 | prose | pages [15] -->
(16)

<!-- b000281 | prose | pages [15] -->
⚫ Radio repeater drones can communicate with SSA drones.

<!-- b000282 | prose | pages [15] -->
(17)

<!-- b000283 | heading | pages [15] -->
4.4.3 Radio repeater drones scheduling scheme

<!-- b000284 | prose | pages [15] -->
For radio repeater drones, the reliability of communication needs to be considered, so we need to ensure that there is a ratio repeater drones at the position we get throughout the wildfire course. Therefore, when the drone needs to return for charging, another drone needs to replace it.

<!-- b000285 | prose | pages [15] -->
For the WileE–15.2X hybrid drone, hovering time and charging time of UAV determine how many UAVs are needed in this position as follow.

<!-- b000286 | prose | pages [15] -->
(18)

<!-- b000287 | prose | pages [15] -->
For the formula 13, we know that

<!-- b000288 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000289 | prose | pages [15, 16] -->
关注数学模型 (19)

<!-- b000290 | furniture | pages [15] -->
2

<!-- b000291 | furniture | pages [15] -->
MATHmodels

<!-- b000292 | furniture | pages [15] -->
获取更多资讯

<!-- b000293 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000294 | furniture | pages [16] -->
Team #2104673

<!-- b000295 | furniture | pages [16] -->
Page 15 of 25

<!-- b000297 | prose | pages [16] -->
微信公众号：数学模型 To sum up, we can know the total number of radio repeater drones, namely, .

<!-- b000298 | heading | pages [16] -->
5 Test the Model

<!-- b000299 | heading | pages [16] -->
5.1 Model 1 Sensitivity Analysis

<!-- b000300 | heading | pages [16] -->
1. UAV detection performance index sensitivity analysis

<!-- b000301 | prose | pages [16] -->
For the model 1, UAV detection performance index depend on the detection range of the UAV. Dif- ferent detectors have different detection capabilities, and we can find out how different detection range will affect the number and distribution of UAVs in this model by solving different parameters 微信号：MATHmodels in its neighborhood range to testify the sensitivity analysis.

<!-- b000302 | prose | pages [16] -->
For the UAV detection performance index, we take 0.005 as the step size within the range of [0.01,0.03], and observe the effect of the change of the value on the model solution result. The results are shown in the following table:

<!-- b000303 | caption | pages [16] -->
Table 3 The relationship between UAV detection performance index and drone number

<!-- b000304 | prose | pages [16] -->
Drone number

<!-- b000305 | prose | pages [16] -->
0.010 3

<!-- b000306 | prose | pages [16] -->
0.015 5

<!-- b000307 | prose | pages [16] -->
0.020 6

<!-- b000308 | prose | pages [16] -->
0.025 5

<!-- b000309 | prose | pages [16] -->
0.030 5

<!-- b000310 | prose | pages [16] -->
It can be seen from the results that when the value of λ is greater than a certain threshold, the number of UAVs solved by the model stabilizes at 5. It can be seen that the stability of the parameter is robust.

<!-- b000311 | heading | pages [16] -->
2 The boundary parameter sensitivity analysis

<!-- b000312 | prose | pages [16] -->
The boundary parameter measures the increase of costs by adding SSA drone. When the detection revenue is greater than the increased cost, continue to increase SSA drones; when the detection reve- nue is less than the increased cost, stop increasing SSA drones.

<!-- b000313 | prose | pages [16] -->
For the boundary parameter 𝛼, we use 0.1 as the step size in the range of [0.3, 0.7] to observe the influence of the change of its value on the model solution result. The results are shown in the table 4 below

<!-- b000314 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000315 | prose | pages [16, 17] -->
关注数学模型 α Drone number

<!-- b000316 | furniture | pages [16] -->
2

<!-- b000317 | furniture | pages [16] -->
MATHmodels

<!-- b000318 | furniture | pages [16] -->
获取更多资讯

<!-- b000319 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000320 | furniture | pages [17] -->
Team #2104673

<!-- b000321 | furniture | pages [17] -->
Page 16 of 25

<!-- b000322 | caption | pages [17] -->
Table 4 The relationship between the boundary parameter and drone number

<!-- b000324 | prose | pages [17] -->
0.3 7 微信公众号：数学模型 0.4 6

<!-- b000325 | prose | pages [17] -->
0.5 6

<!-- b000326 | prose | pages [17] -->
0.6 4

<!-- b000327 | prose | pages [17] -->
0.7 3

<!-- b000328 | prose | pages [17] -->
It can be seen from the table that this parameter has a great influence on the result of UAV. It is known that this parameter has high sensitivity and poor stability. Based on the physical meaning of this pa- rameter, this is understandable. 微信号：MATHmodels

<!-- b000329 | heading | pages [17] -->
5.2 Model 2 Sensitivity Analysis

<!-- b000330 | prose | pages [17] -->
For cellular automata, due to the random simulation process involved in the model, any parameter value change may result in different fire field distributions, and multiple solution results of the same parameter value may also obtain different fire field distributions. Therefore, we can change the value of a certain parameter and solve the model twice for each value to verify the sensitivity of the model.

<!-- b000331 | prose | pages [17] -->
For the critical fire probability pf, we use 0.03 as the step size in the range of [0.74, 0.83] to observe the influence of the change of its value on the model solution result. The results are shown in the table 5 below:

<!-- b000332 | caption | pages [17] -->
Table 5 The relationship between the critical fire probability pf and drone number

<!-- b000333 | prose | pages [17] -->
Drone number Drone number pf (1st time result) (2nd time result) 0.74 10 10 0.77 6 6 0.80 6 5 0.83 4 4

<!-- b000334 | caption | pages [17] -->
Figure 2 Sensitivity Analysis for the critical fire probability

<!-- b000335 | prose | pages [17] -->
It can be seen from the solution result that the change of the value of k has a greater influence on the

<!-- b000336 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000337 | prose | pages [17, 18] -->
关注数学模型 solution result of the model, indicating that the sensitivity of parameter pf is high. Therefore, it is necessary to accurately simulate the value of k in the process of model building, otherwise the solution result will produce errors.

<!-- b000338 | furniture | pages [17] -->
2

<!-- b000339 | furniture | pages [17] -->
MATHmodels

<!-- b000340 | furniture | pages [17] -->
获取更多资讯

<!-- b000341 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000342 | furniture | pages [18] -->
Team #2104673

<!-- b000343 | furniture | pages [18] -->
Page 17 of 25

<!-- b000345 | heading | pages [18] -->
6 Conclusion

<!-- b000346 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000347 | heading | pages [18] -->
6.1 Summary of Results

<!-- b000348 | heading | pages [18] -->
6.1.1 Result of Problem 1

<!-- b000349 | prose | pages [18] -->
Through cellular automata, according to the fire data of the Australian fire, we can get the distribution of one of the fires as follows, where the critical fire probability is . We ran five simula- tions. Then we got the flame severity distribution matrix. We visualize it as shown in the figure 10.

<!-- b000350 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000351 | caption | pages [18] -->
Figure 3 flame severity distribution matrix

<!-- b000352 | prose | pages [18] -->
The optimization objectives and constraints of SSA drones are as follows. Bring the fire severity data in the figure 11 into the planning model in the figure below.

<!-- b000353 | prose | pages [18] -->
(20)

<!-- b000354 | prose | pages [18] -->
Through lingo, the matrix for 5 kinds of SSA drones monitoring mode and the location of EOC is

<!-- b000355 | prose | pages [18] -->
obtained. Meanwhile, the total number of SSA UAVs is known as . The location

<!-- b000356 | prose | pages [18] -->
of EOC is (1,6).

<!-- b000357 | prose | pages [18] -->
The optimization objectives and constraints of radio repeater drones are as follows.

<!-- b000358 | prose | pages [18] -->
(21)

<!-- b000359 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000360 | prose | pages [18, 19] -->
关注数学模型 Through lingo, the matrix for the location of radio repeater drones is obtained. Meanwhile, the total

<!-- b000361 | furniture | pages [18] -->
2

<!-- b000362 | furniture | pages [18] -->
MATHmodels

<!-- b000363 | furniture | pages [18] -->
获取更多资讯

<!-- b000364 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000365 | furniture | pages [19] -->
Team #2104673

<!-- b000366 | furniture | pages [19] -->
Page 18 of 25

<!-- b000368 | prose | pages [19] -->
number of radio repeater drones is known as . Ultimately, the total number of 2 kinds of

<!-- b000369 | prose | pages [19] -->
drones is 10. 微信公众号：数学模型

<!-- b000370 | heading | pages [19] -->
6.1.2 Result of Problem 2

<!-- b000371 | prose | pages [19] -->
Due to global warming, the surface temperature of Victoria will increase, which will affect the fire

<!-- b000372 | prose | pages [19] -->
probability of the region. The critical fire probability after ten years is . Through cellular

<!-- b000373 | prose | pages [19] -->
automata, we can get the distribution of one of the fires as follows.

<!-- b000374 | prose | pages [19] -->
The optimization objectives and constraints of SSA drones and the optimization objectives and con-

<!-- b000375 | prose | pages [19] -->
微信号：MATHmodels straints of radio repeater drones for the ten years later are the same as what the paper showed in model

<!-- b000376 | prose | pages [19] -->
1&3. Therefore, we can get the UAV configuration for the ‘Rapid Bushfire Response’ system.

<!-- b000377 | prose | pages [19] -->
The number of SSA drones is known as . The number of radio repeater drones

<!-- b000378 | prose | pages [19] -->
is known as .

<!-- b000379 | prose | pages [19] -->
Therefore, for the next decade, due to global warming, the cost of thermal imaging cameras and te-

<!-- b000380 | prose | pages [19] -->
lemetry sensors increases.

<!-- b000381 | heading | pages [19] -->
6.1.3 Result of Problem 3

<!-- b000382 | prose | pages [19] -->
We can get the different area data of fire region by changing the critical fire probability so that the location of radio repeater drones is available. By changing the critical fire probability pf from 0.74 to 0.83 by the step of 0.03, areas of wildfire region and the locations of radio repeater drones are shown in the Table 6.

<!-- b000383 | caption | pages [19] -->
Table 6 The location of radio repeater for different fire area

<!-- b000384 | prose | pages [19] -->
Critical fire prob- Area of fire region Location of radio repeater (km2) ability drone 79.2342 (3,4) 0.74 81.3212 (2,5) 80.8094 (0,3) 0.77 81.0506 (0,3) 77.7141 (0,3) 0.80 76.3213 (2,5) 72.7502 (2,4) 0.83 74.0506 (2,4)

<!-- b000385 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000386 | prose | pages [19, 20] -->
关注数学模型 As for the location of different terrains, because the terrain characteristic is considered into the model 3, we choose 3 different area to simulate the results. The locations of radio repeater are all the same because the terrain has a much less infect on the location of radio repeater drones. The reason that the effect is small is the effect of terrain on the radio range is not large enough to counteracting SSA drones impact on the location of radio repeater drones. What’s more, it turns out that ratio repeater 微信公众号：数学模型 will get close to the area where the altitude changes rapidly.

<!-- b000387 | furniture | pages [19] -->
2

<!-- b000388 | furniture | pages [19] -->
MATHmodels

<!-- b000389 | furniture | pages [19] -->
获取更多资讯

<!-- b000390 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000391 | furniture | pages [20] -->
Team #2104673

<!-- b000392 | furniture | pages [20] -->
Page 19 of 25

<!-- b000394 | heading | pages [20] -->
7 Model Evaluation and Further Discussion

<!-- b000395 | heading | pages [20] -->
7.1 Strengths

<!-- b000396 | prose | pages [20] -->
⚫ The model has wide applicability. Knowing the fire situation, the deployment position of EOC and UAV can be quickly solved, which can improve the efficiency of fire rescue.

<!-- b000397 | prose | pages [20] -->
⚫ The model can predict the future fire situation according to the weather conditions, so that EOC and drones can be deployed in advance to improve fire rescue efficiency and reduce losses.

<!-- b000398 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000399 | heading | pages [20] -->
7.2 Possible Improvements

<!-- b000400 | prose | pages [20] -->
⚫ The impact of weather and other factors on the flight of the UAV is not considered, which leads to a certain error between the model prediction results and reality. As the planning model is rel- atively large, in order to simplify the model, we have to give up thinking about factors such as weather.

<!-- b000401 | prose | pages [20] -->
⚫ Due to the lack of detailed fire and climate data in Victoria, the prediction of fire sites in the next ten years lacks accuracy.

<!-- b000402 | prose | pages [20] -->
⚫ The fire field prediction model assumes that fires are likely to occur in every area. In fact, fires are likely to occur only in places covered by vegetation, which is inconsistent with reality.

<!-- b000403 | heading | pages [20] -->
8 References

<!-- b000404 | references | pages [20] -->
[1] W. Wei, M. Hao, X. Jin-qi, and S. Chang-yin, “Research on standardized design method of air-

<!-- b000405 | references | pages [20] -->
frame for multi-rotor uav,” no. 5, pp. 147150, 2014.

<!-- b000406 | references | pages [20] -->
[2]Xiang Tingli, Wang Hongjun, Shi Yingchun. Multi-aircraft cooperative detection task allocation

<!-- b000407 | references | pages [20] -->
strategy for area coverage[J]. Journal of Air Force Engineering University (Natural Science Edi-

<!-- b000408 | references | pages [20] -->
tion), 2019, 20(06): 33-38+71.

<!-- b000409 | references | pages [20] -->
[3] Niu Ruoyun, Zhai Panmao, Sun Minghua. Review of Forest Fire Risk Meteorological Index and

<!-- b000410 | references | pages [20] -->
Its Construction Method[J]. Meteorology, 2006(12): 3-9.

<!-- b000411 | references | pages [20] -->
[4] Zhang Wenwen, Wang Qiuhua, Wang Ruichen, Long Tengteng, Wei Jianheng, Gao Zhongliang.

<!-- b000412 | references | pages [20] -->
Research progress on Australian eucalyptus forest fires[J/OL]. World Forestry Re-search:1-

<!-- b000413 | references | pages [20] -->
10[2021-02-07].https://doi.org/10.13348/j.cnki.sjlyyj.2021.0004.y.

<!-- b000414 | references | pages [20] -->
[5] Li Chengxin, Zhao Liangchen, Li Dongyun, Ma Jiahui. Australian forest fire spread prediction

<!-- b000415 | references | pages [20] -->
model based on CA system and application of emergency supplies dispatching [J]. Forestry In-

<!-- b000416 | references | pages [20] -->
vestigation and Planning, 2020, 45(05): 62-69+89.

<!-- b000417 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000418 | references | pages [20] -->
关注数学模型

<!-- b000419 | furniture | pages [20] -->
2

<!-- b000420 | furniture | pages [20] -->
MATHmodels

<!-- b000421 | furniture | pages [20] -->
获取更多资讯

<!-- b000422 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000423 | furniture | pages [21] -->
Team #2104673

<!-- b000424 | furniture | pages [21] -->
Page 20 of 25

<!-- b000425 | references | pages [21] -->
[6] Liu Jiachang, Tang Bin, Zou Yuan. Using GIS to analyze the factors affecting the occurrence of

<!-- b000426 | references | pages [21] -->
forest fires and their temporal and spatial distribution characteristics: Taking California as an ex-

<!-- b000427 | references | pages [21] -->
ample [J]. Journal of Northeast Forestry University, 2020, 48(07): 70-74.

<!-- b000428 | references | pages [21] -->
[7] Li Binghua, Zhu Jiping, Xiaodezhi, Peng Chen. A method for estimating the frequency of major

<!-- b000429 | references | pages [21] -->
微信公众号：数学模型

<!-- b000430 | references | pages [21] -->
fires based on the information diffusion of small sample data[J]. Fire Science, 2010, 19(02): 82-

<!-- b000431 | references | pages [21] -->
88.

<!-- b000432 | references | pages [21] -->
[8] Liu Chang. Research and simulation of forest fire spread model based on cellular automata[D].

<!-- b000433 | references | pages [21] -->
Dalian University of Technology, 2012.

<!-- b000434 | references | pages [21] -->
[9] Yang Fulong. Three-dimensional simulation of forest fire spread based on cellular automata[D].

<!-- b000435 | references | pages [21] -->
Beijing Forestry University, 2016.

<!-- b000436 | references | pages [21] -->
[10] Zhou Peiheng. Research on the evolution model of regional disaster consequences based on

<!-- b000437 | references | pages [21] -->
cellular automata [D]. Dalian University of Technology, 2015.

<!-- b000438 | references | pages [21] -->
微信号：MATHmodels

<!-- b000439 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000440 | references | pages [21] -->
关注数学模型

<!-- b000441 | furniture | pages [21] -->
2

<!-- b000442 | furniture | pages [21] -->
MATHmodels

<!-- b000443 | furniture | pages [21] -->
获取更多资讯

<!-- b000444 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000445 | furniture | pages [22] -->
Team #2104673

<!-- b000446 | furniture | pages [22] -->
Page 21 of 25

<!-- b000447 | references | pages [22] -->
Budget Request

<!-- b000448 | references | pages [22] -->
To: CFA

<!-- b000449 | references | pages [22] -->
From: MCM/ICM Team #2104673

<!-- b000450 | references | pages [22] -->
微信公众号：数学模型

<!-- b000451 | references | pages [22] -->
Date: Friday, February 5, 2021

<!-- b000452 | references | pages [22] -->
Subject: Budget request for establishing ‘Rapid Bushfire Response’ UAV system for Victoria state

<!-- b000453 | references | pages [22] -->
government

<!-- b000454 | references | pages [22] -->
Dear Sir or Madam:

<!-- b000455 | references | pages [22] -->
Hearing that CFA is preparing to set up a new department called “Rapid Bushfire Response” and

<!-- b000456 | references | pages [22] -->
recently developing a drone system to deal with forest fires. We are more than glad to share our

<!-- b000457 | references | pages [22] -->
mathematical model to give some recommendations.

<!-- b000458 | references | pages [22] -->
From 2019 to 2020, Australia has launched devastating forest fires, causing serious damage to the

<!-- b000459 | references | pages [22] -->
environment in every state and seriously affecting people's normal lives. In order to curb the spread

<!-- b000460 | references | pages [22] -->
微信号：MATHmodels

<!-- b000461 | references | pages [22] -->
of fire and reduce property losses, emergency systems must be designed to better help the Victorian

<!-- b000462 | references | pages [22] -->
government to rescue fires.

<!-- b000463 | references | pages [22] -->
Since the drones are not restricted by road conditions, they can observe the situation in the disaster

<!-- b000464 | references | pages [22] -->
area, transport relief supplies, and provide communication services to support post-disaster rescue.

<!-- b000465 | references | pages [22] -->
Therefore, it is widely used in the rescue of natural disasters such as fires, earthquakes and hurri-

<!-- b000466 | references | pages [22] -->
canes. Our team has developed an drone system for fire detection and information transmission. The

<!-- b000467 | references | pages [22] -->
system can be used to observe forest fires and provide communication services between firefighters

<!-- b000468 | references | pages [22] -->
and the command center.

<!-- b000469 | references | pages [22] -->
First, we built a fire prediction model based on climate data. By collecting climate data from Victoria

<!-- b000470 | references | pages [22] -->
and combining with future climate change trends, we can predict the probability and magnitude of

<!-- b000471 | references | pages [22] -->
fires in this area in the next ten years. Then by discretizing the fire area, comprehensively considering

<!-- b000472 | references | pages [22] -->
the impact of Victoria's terrain on the signal transmission of drones and the performance indicators

<!-- b000473 | references | pages [22] -->
of drones to construct a planning model. Solve the model to get the number and location of SSA

<!-- b000474 | references | pages [22] -->
drones. Through the number and location of SSA drones, combined with the performance indicators

<!-- b000475 | references | pages [22] -->
of dornes, we can obtain the number and location of Radio Repeater drones, thereby obtaining the

<!-- b000476 | references | pages [22] -->
position of the EOC.

<!-- b000477 | references | pages [22] -->
In order to reduce the government's financial burden, we propose to purchase rechargeable drones

<!-- b000478 | references | pages [22] -->
and find the minimum number of drones that can meet the rescue requirements. We recommend that

<!-- b000479 | references | pages [22] -->
you purchase 10 SSA drones and 2 radio repeater drones to deal with forest fires in Victoria in the

<!-- b000480 | references | pages [22] -->
next ten years, otherwise it may not be able to cover the entire fire scene and ensure the communica-

<!-- b000481 | references | pages [22] -->
tion safety of all firefighters.

<!-- b000482 | references | pages [22] -->
We hope that our model can help CFA improve the efficiency of fire rescue, ensure the safety of

<!-- b000483 | references | pages [22] -->
firefighters, and reduce the loss caused by fire.

<!-- b000484 | references | pages [22] -->
Yours Sincerely,

<!-- b000485 | furniture | pages [22] -->
Team # 2104673

<!-- b000486 | references | pages [22] -->
P.S. The attached table for the budget request is on the next page.

<!-- b000487 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000488 | references | pages [22] -->
关注数学模型

<!-- b000489 | furniture | pages [22] -->
2

<!-- b000490 | furniture | pages [22] -->
MATHmodels

<!-- b000491 | furniture | pages [22] -->
获取更多资讯

<!-- b000492 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000493 | furniture | pages [23] -->
Team #2104673

<!-- b000494 | furniture | pages [23] -->
Page 22 of 25

<!-- b000495 | references | pages [23] -->
Budget Request

<!-- b000496 | references | pages [23] -->
Project for Requesting Department

<!-- b000497 | references | pages [23] -->
Effective Date

<!-- b000498 | references | pages [23] -->
微信公众号：数学模型

<!-- b000499 | references | pages [23] -->
‘Rapid Bushfire Response’ UAV system

<!-- b000500 | references | pages [23] -->
Friday, February 5, 2021

<!-- b000501 | references | pages [23] -->
Title: UAV system for fire detection and information transmission

<!-- b000502 | references | pages [23] -->
Purpose:

<!-- b000503 | references | pages [23] -->
Detect fire conditions to improve fire rescue efficiency and reduce losses caused by fire. Provide

<!-- b000504 | references | pages [23] -->
communication services between firefighters and rescue centers to ensure the safety of firefighters.

<!-- b000505 | references | pages [23] -->
How are funds used：

<!-- b000506 | references | pages [23] -->
The money is mainly used to purchase WileE–15.2X Hybrid Drones, handheld two-way radios,

<!-- b000507 | references | pages [23] -->
thermal imaging cameras and telemetry sensors and repeaters.

<!-- b000508 | references | pages [23] -->
Num-

<!-- b000509 | references | pages [23] -->
微信号：MATHmodels

<!-- b000510 | references | pages [23] -->
Estimated Expenditures

<!-- b000511 | references | pages [23] -->
Price

<!-- b000512 | references | pages [23] -->
Comments

<!-- b000513 | references | pages [23] -->
ber

<!-- b000514 | references | pages [23] -->
An UVA equipped with radio repeaters or

<!-- b000515 | references | pages [23] -->
WileE–15.2X Hybrid Drone

<!-- b000516 | references | pages [23] -->
$12000

<!-- b000517 | references | pages [23] -->
12

<!-- b000518 | references | pages [23] -->
video and telemetry functions.

<!-- b000519 | references | pages [23] -->
thermal imaging cameras and

<!-- b000520 | references | pages [23] -->
Portable communication equipment between

<!-- b000521 | references | pages [23] -->
$1000

<!-- b000522 | references | pages [23] -->
10

<!-- b000523 | references | pages [23] -->
telemetry sensors

<!-- b000524 | references | pages [23] -->
firefighters and EOC.

<!-- b000525 | references | pages [23] -->
Transceivers that automatically rebroadcast

<!-- b000526 | references | pages [23] -->
Repeater

<!-- b000527 | references | pages [23] -->
$1000

<!-- b000528 | references | pages [23] -->
2

<!-- b000529 | references | pages [23] -->
signals at higher powers.

<!-- b000530 | references | pages [23] -->
Reporting Department: Team #2104673 MCM/ICM

<!-- b000531 | references | pages [23] -->
Requested by: CFA

<!-- b000532 | references | pages [23] -->
Date: Friday, February 5, 2021

<!-- b000533 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000534 | references | pages [23] -->
关注数学模型

<!-- b000535 | furniture | pages [23] -->
2

<!-- b000536 | furniture | pages [23] -->
MATHmodels

<!-- b000537 | furniture | pages [23] -->
获取更多资讯

<!-- b000538 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000539 | furniture | pages [24] -->
Team #2104673

<!-- b000540 | furniture | pages [24] -->
Page 23 of 25

<!-- b000541 | heading | pages [24] -->
Appendices

<!-- b000542 | heading | pages [24] -->
Appendix 1 —— Tools and software

<!-- b000543 | prose | pages [24] -->
微信公众号：数学模型 Lingo & Matlab

<!-- b000544 | heading | pages [24] -->
Appendix 2 —— Code

<!-- b000545 | prose | pages [24] -->
Appendix 2.1 Introduce: Regional Discretization Model sets: x/1..COLS/; y/1..ROWS/; actions/1..5/; link(x,y):H,totaltime; link3(x,y,actions):t,delta; endsets dronenum = @sum(link3(i,j,k):delta(i,j,k)); 微信号：MATHmodels value = @sum(x(i):@sum(y(j):(1-@exp(lambda*@sum(ac- tions(k):t(i,j,k))))*H(i,j))) - boundary * dronenum; @gin(eocx); @gin(eocy); eocx<=COLS; eocy<=ROWS; @for(link3(i,j,k):@bin(delta(i,j,k))); @for(link(i,j):t(i,j,1)=delta(i,j,1)*(Gmax-@sqrt((eocx-i)^2+(eocy- j)^2)*dtime)); @for(link(i,j)|i#gt#1:t(i,j,2)=(delta(i,j,2)*(Gmax-@sqrt((eocx-i-0.5)^2+(eocy- j)^2)*dtime) + delta(i-1,j,2)*(Gmax-@sqrt((eocx-i+0.5)^2+(eocy- j)^2)*dtime))/2); @for(link(i,j)|j#gt#1:t(i,j,3)=(delta(i,j,3)*(Gmax-@sqrt((eocx-i)^2+(eocy-j- 0.5)^2)*dtime) + delta(i,j-1,3)*(Gmax-@sqrt((eocx-i)^2+(eocy- j+0.5)^2)*dtime))/2); @for(link(i,j)|i#gt#1 #and# j#gt#1:t(i,j,4)=(delta(i-1,j,4)*(Gmax-@sqrt((eocx- i+0.5)^2+(eocy-j-0.5)^2)*dtime) +delta(i,j-1,4)*(Gmax-@sqrt((eocx-i- 0.5)^2+(eocy-j+0.5)^2)*dtime))/2); @for(link(i,j)|i#gt#1 #and# j#gt#1:t(i,j,5)=(delta(i,j,5)*(Gmax-@sqrt((eocx-i- 0.5)^2+(eocy-j-0.5)^2)*dtime) +delta(i-1,j-1,5)*(Gmax-@sqrt((eocx- i+0.5)^2+(eocy-j+0.5)^2)*dtime))/2); @for(link(i,j):H(i,j)<=H(i,j)*((eocx-i)*(COLS+1)-(eocy-j))^2); @for(link(i,j):totaltime(i,j)=@sum(link3(i,j,k):t(i,j,k))); value = @sum(x(i):@sum(y(j):(1-@exp(lambda*@sum(ac- tions(k):t(i,j,k))))*H(i,j))) - boundary * dronenum; max =value; Appendix 2.2 Introduce: Cellular automata simulation a = 500; b = 400; k = 0.005; veg = 5*ones(a,b); imh = image(cat(3,veg,veg,veg)); W = fspecial('gaussian',[51,51],0.9); vegpast = zeros(a,b); resultmat = zeros(5,25); for burn = 0.6:0.02:1 for turn = 1:5

<!-- b000546 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000547 | prose | pages [24, 25] -->
关注数学模型 veg=5*ones(a,b); veg(a/2:a/2+1,b/2:b/2+1)=[4 4;4 4]; for i=1:1000 vegpast = veg; vegavg = imfilter(double(veg<5&veg>1), W, 'replicate'); veg = veg - 1 + (veg==5) + (veg==0) + (veg<0) ...

<!-- b000548 | furniture | pages [24] -->
2

<!-- b000549 | furniture | pages [24] -->
MATHmodels

<!-- b000550 | furniture | pages [24] -->
获取更多资讯

<!-- b000551 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000552 | furniture | pages [25] -->
Team #2104673

<!-- b000553 | furniture | pages [25] -->
Page 24 of 25

<!-- b000555 | prose | pages [25] -->
微信公众号：数学模型 - (veg==5).*(vegavg >= burn * rand(a,b)) ... - 5*((1<veg&veg<5).*rand(a,b) > exp(-k*i)); set(imh, 'cdata', cat(3,(1<veg&veg<5),(veg==5),zeros(a,b))); drawnow if sum(sum((vegpast==5) == (veg==5))) == a * b break; end end resultmat(turn,int16(50*burn-29)) = a*b-sum(sum((veg==5))); end end Appendix 2.3 Introduce: Terrain Adapting Regional Discretization Model sets: x/1..COLS/; 微信号：MATHmodels y/1..ROWS/; z/1..DRONES/:totalpoint; link(x,y):G,H,oinit1,oinit2,oinit3,tinit1,tinit2,tinit3; link3(x,y,z):t,o,delta; endsets @for(z(k):@sum(link(i,j):t(i,j,k))<=Gmax); @for(link3(i,j,k):o(i,j,k)*t(i,j,k)>=o(i,j,k)*G(i,j)); @for(link3(i,j,k):t(i,j,k)<o(i,j,k)*Gmax); @for(z(k):totalpoint(k)*(totalpoint(k)-1) = @sum(x(i):@sum(y(j):o(i,j,k)))); @for(z(k):@for(x(i):@for(y(j):o(i,j,k) <= totalpoint(k)))); @for(z(k):@for(x(i)|i#gt#1 #and# i#lt#COLS:@for(y(j)|j#gt#1 #and# j#lt#ROWS: delta(i,j,k) * (totalpoint(k) - o(i,j,k))* (o(i-1,j-1,k)-o(i,j,k)-1) *(o(i,j-1,k)-o(i,j,k)-1) *(o(i+1,j-1,k)-o(i,j,k)-1)* (o(i-1,j,k)-o(i,j,k)-1) *(o(i+1,j,k)-o(i,j,k)-1) * (o(i-1,j+1,k)-o(i,j,k)-1)* (o(i,j+1,k)-o(i,j,k)-1) *(o(i+1,j+1,k)-o(i,j,k)-1) = 0))); @for(z(k):@for(link(i,j):delta(i,j,k)=@smin(o(i,j,k),1))); @for(z(k):o(startx, starty, k) = 1); @for(z(k):@for(x(i):o(i,1,k)=0)); @for(z(k):@for(x(i):o(i,ROWS,k)=0)); @for(z(k):@for(y(j):o(1,j,k)=0)); @for(z(k):@for(y(j):o(COLS,j,k)=0)); max = @sum(link3(i,j,k):t(i,j,k)*H(i,j));

<!-- b000556 | prose | pages [25] -->
 In order to meet the page number requirements of the paper, only the most important part of the most important code solution is included in the attachment

<!-- b000557 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000558 | prose | pages [25] -->
关注数学模型

<!-- b000559 | furniture | pages [25] -->
2

<!-- b000560 | furniture | pages [25] -->
MATHmodels

<!-- b000561 | furniture | pages [25] -->
获取更多资讯
