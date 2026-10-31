# P-B-2021-2102199-f3e89239

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | prose | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000004 | furniture | pages [1] -->
2021

<!-- b000005 | furniture | pages [1] -->
Team Control Number

<!-- b000006 | prose | pages [1] -->
MCM/ICM

<!-- b000007 | title | pages [1] -->
B

<!-- b000008 | title | pages [1] -->
2102199

<!-- b000009 | heading | pages [1] -->
Summary Sheet

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | prose | pages [1] -->
Build an Army of Drones to Fight Wildfires

<!-- b000012 | title | pages [1] -->
微信公众号：数学模型

<!-- b000013 | prose | pages [1] -->
Global warming, El Niño... With the emergence of various extreme climates, Australia's wildfires occur more frequently. The greenhouse gases emitted after combustion have exacer- bated global warming, which seems to have entered an endless loop. At the same time, hun- dreds of millions of lives have been killed in the fire, which makes us sad. In order to better control wildfires, we modeled the distribution of drones assisting in the observation to achieve the best balance between economy and efficiency.

<!-- b000014 | prose | pages [1] -->
Several models are established: Model I: Rasterized Multi-Objective Optimization Model; Model II: Model Verification Simulated by Poisson Process; Model III: Hovering Model Based on Tabu Search, etc.

<!-- b000015 | prose | pages [1] -->
Before all the models are established, we rasterize the area to be studied. Through the discrete grid, we can do better analysis. Moreover, we use a variety of visualization methods to make the results more intuitive.

<!-- b000016 | title | pages [1] -->
微信号：MATHmodels

<!-- b000017 | prose | pages [1] -->
For Model I: According to the heat map about distribution of fires in Victoria in recent years, we found that the main fire areas are the plains along the eastern coast. Inspired by weights and Multi-Objective Optimization algorithms, we built a brand-new model to find the best location for EOCs and draw up a suitable hover position and reconnaissance route for the drone. Based on the different positions of the fire site, calculate the maximum number of two types of drones and their ratio. The results are shown in Figure 9.

<!-- b000018 | prose | pages [1] -->
For Model II: This model is actually a supplement to Model I. In the Model I, the fire only appeared in a small area, and there was a possibility of extreme fire events in the study area. Combining the data about nearly half a century and using the Poisson Distribution to obtain the probability and mathematical expectation, it can be concluded that 2.99431 extreme fire events may occur in the next ten years, which is approximately considered to be 3 times. After that, use the mobile EOC to deal with extreme fire events, and utilize the method of Model I to rebuild the drone network to find out what equipment costs need to be increased. Due to the di- versity of the results, it will be shown in section 6.2.

<!-- b000019 | prose | pages [1] -->
For Model III: To tackle the problem of how to optimize the hover position of drones in different terrains, the Tabu Search algorithm (TS) is a good choice. Using the Tabu Search algorithm can make the hover position of the drones achieve the global optimal effect under different terrain conditions. Since drone signals are severely interfered in urban areas, the rea- sonable distribution of EOCs enables it to quickly network to respond to sudden urban fires. The obstruction of mountainous terrain restricts the drone's flying range. Therefore, dividing the area into blocks and managing them separately can effectively improve efficiency.

<!-- b000020 | prose | pages [1] -->
In addition, because rich terrain and emergencies have been discussed in the above three models, our model has strong adaptability. Not only can it be used in the area we are studying, but it can also be used in the rest of Australia.

<!-- b000021 | heading | pages [1] -->
Finally, sensitivity analysis of the mathematical expectation of extreme fire events

<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | prose | pages [1] -->
shows that our model is not sensitive to changes in , that is, it can be applied to areas with different extreme fire invents. Meanwhile, robustness of our model has also been tested. While adding 5% random disturbance to and , the maximum time error is 3.2657%. The model can be considered stable. Afterwards, a Budget Request supported by our stable models has been written for CFA.

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | keywords | pages [1] -->
Keywords: Fighting Wildfires; Multi-Objective Optimization; Poisson Distribution; Tabu Search

<!-- b000026 | heading | pages [1] -->
Algorithm; Sensitivity Analysis

<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000029 | prose | pages [1] -->
关注数学模型

<!-- b000030 | furniture | pages [1] -->
2

<!-- b000031 | furniture | pages [1] -->
MATHmodels

<!-- b000032 | furniture | pages [1] -->
获取更多资讯

<!-- b000033 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000034 | furniture | pages [2] -->
Team # 2102199                                                                            Page 2 of 25

<!-- b000035 | heading | pages [2] -->
Contents

<!-- b000036 | contents | pages [2] -->
1 Introduction ...................................................................................................... 3

<!-- b000037 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000038 | contents | pages [2] -->
1.1 Problem Background ....................................................................................................... 3

<!-- b000039 | contents | pages [2] -->
1.2 Restatement of the Problem ............................................................................................. 3

<!-- b000040 | contents | pages [2] -->
1.3 Literature Review ............................................................................................................. 4

<!-- b000041 | contents | pages [2] -->
1.4 Our Work .......................................................................................................................... 5

<!-- b000042 | contents | pages [2] -->
2 Assumptions and Explanations ....................................................................... 5

<!-- b000043 | contents | pages [2] -->
3 Notations ........................................................................................................... 6

<!-- b000044 | contents | pages [2] -->
4 Model Preparation ........................................................................................... 6

<!-- b000045 | contents | pages [2] -->
4.1 Data Overview ................................................................................................................. 6

<!-- b000046 | contents | pages [2] -->
4.2 Conversion from longitude and latitude to distance ........................................................ 7

<!-- b000047 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000048 | contents | pages [2] -->
4.3 Description of the two drones .......................................................................................... 8

<!-- b000049 | contents | pages [2] -->
5 Rasterized Multi-Objective Optimization Model ......................................... 8

<!-- b000050 | contents | pages [2] -->
5.1 Rasterization of Regions .................................................................................................. 8

<!-- b000051 | contents | pages [2] -->
5.2 Wildfire Frequency-Distance Weighted Model ............................................................... 9

<!-- b000052 | contents | pages [2] -->
5.3 Multi-objective Optimization Model ............................................................................. 11

<!-- b000053 | contents | pages [2] -->
5.4 Results and Analysis ...................................................................................................... 12

<!-- b000054 | contents | pages [2] -->
6 Model Verification Simulated by Poisson Process ...................................... 13

<!-- b000055 | contents | pages [2] -->
6.1 Poisson Process of Extreme Fire Events ........................................................................ 13

<!-- b000056 | contents | pages [2] -->
6.2 Model Verification and Analysis .................................................................................... 15

<!-- b000057 | contents | pages [2] -->
7 Hovering Model Based on Tabu Search ....................................................... 17

<!-- b000058 | contents | pages [2] -->
7.1 Model construction of mountains and urban areas ........................................................ 17

<!-- b000059 | contents | pages [2] -->
7.2 Simulation Results ......................................................................................................... 18

<!-- b000060 | contents | pages [2] -->
8 Sensitivity and Robustness Analysis ............................................................. 19

<!-- b000061 | contents | pages [2] -->
8.1 Sensitivity Analysis ........................................................................................................ 19

<!-- b000062 | contents | pages [2] -->
8.2 Sensitivity Analysis ........................................................................................................ 20

<!-- b000063 | contents | pages [2] -->
9 Evaluation of Strengths and Weaknesses .................................................... 21

<!-- b000064 | contents | pages [2] -->
9.1 Strengths ........................................................................................................................ 21

<!-- b000065 | contents | pages [2] -->
9.2 Weaknesses and Further Improvements ......................................................................... 21

<!-- b000066 | contents | pages [2] -->
Budget Request .................................................................................................. 22

<!-- b000067 | contents | pages [2] -->
References .......................................................................................................... 24

<!-- b000068 | contents | pages [2] -->
Appendices ......................................................................................................... 25

<!-- b000069 | furniture | pages [2] -->


<!-- b000070 | furniture | pages [2] -->


<!-- b000071 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000072 | contents | pages [2] -->
关注数学模型

<!-- b000073 | furniture | pages [2] -->
2

<!-- b000074 | furniture | pages [2] -->
MATHmodels

<!-- b000075 | furniture | pages [2] -->
获取更多资讯

<!-- b000076 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000077 | furniture | pages [3] -->
Team # 2102199                                                                            Page 3 of 25

<!-- b000078 | heading | pages [3] -->
1 Introduction

<!-- b000079 | heading | pages [3] -->
1.1 Problem Background

<!-- b000080 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000081 | prose | pages [3] -->
"Just like you, I was pain and fear when the fire destroyed the land and everything : life, houses, animals and trees. But for us aborigines, what the fire burns down is our memories, our holy land, and all the things that define our identity. " said by an aborigine. In recent years, the scale of fires in Australia has become larger and larger, causing huge economic and cultural losses. With the climate warming, the probability of fire is also greatly increased, so that it cannot be ignored anymore. We can see the fire situation in Australia from the figure below:

<!-- b000082 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000083 | furniture | pages [3] -->


<!-- b000084 | caption | pages [3] -->
Figure 1: Fire Situation in Australia (Feb 2020 - Feb 2021)

<!-- b000085 | prose | pages [3] -->
The data above comes from the website GLOBAL FOREST WHATCH[1], The GFW Fires interactive map includes near real-time fire alerts from NASA and NOAA, real-time wind direction and air quality data, maps of concessions and forest cover, high-resolution satellite images, and geo-tagged social media conversations about where fires occur.

<!-- b000086 | prose | pages [3] -->
As can be seen above: In Australia, the peak fire season typically begins in early Janu- ary and lasts 45 weeks. There were 636,731 VIIRS fire alerts reported between Febru- ary 2020 and February 2021. In response to the situation above, establishing a mathematical model driven by a swarm of drones to quickly deal with forest fires is very necessary and urgent.

<!-- b000087 | furniture | pages [3] -->


<!-- b000088 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000089 | prose | pages [3] -->
Wildfire is a serious natural disaster with many complexities. Through in-depth analysis and research on the background of the problem, combined with the specific constraints given, the restate of the problem can be expressed as follows:

<!-- b000090 | prose | pages [3] -->
 Build a mathematical model to determine the optimal number and combination of

<!-- b000091 | prose | pages [3] -->
SSA drones and Radio Repeater drones. The model should balance several factors.

<!-- b000092 | prose | pages [3] -->
 Based on the model, explain how it adapts to the changing possibilities of extreme

<!-- b000093 | prose | pages [3] -->
fire events in the next ten years.

<!-- b000094 | furniture | pages [3] -->


<!-- b000095 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000096 | prose | pages [3] -->
关注数学模型

<!-- b000097 | furniture | pages [3] -->
2

<!-- b000098 | furniture | pages [3] -->
MATHmodels

<!-- b000099 | furniture | pages [3] -->
获取更多资讯

<!-- b000100 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000101 | furniture | pages [4] -->
Team # 2102199                                                                            Page 4 of 25

<!-- b000102 | prose | pages [4] -->
 Optimize the position of hovering VHF/UHF radio repeater drones based on an im-

<!-- b000103 | prose | pages [4] -->
proved model for fires of different sizes on different terrains.

<!-- b000104 | prose | pages [4] -->
 Considering the results obtained above, prepare one to two pages of annotated budget

<!-- b000105 | prose | pages [4] -->
request and submit to the Victorian Government.

<!-- b000106 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000107 | furniture | pages [4] -->


<!-- b000108 | heading | pages [4] -->
1.3 Literature Review

<!-- b000109 | prose | pages [4] -->
This question is mainly about mobilizing cluster drones to extinguish wildfires. In recent years, research on optimization algorithms for UAV(drone) cluster path planning is very hot, Generally, it can be divided into two parts, the Swarms of UAVs’ Path Planning Model and

<!-- b000110 | heading | pages [4] -->
the Swarms of UAVs’ Path Planning Optimization Algorithm, this section mainly discusses

<!-- b000111 | prose | pages [4] -->
the models that have been proposed.

<!-- b000112 | prose | pages [4] -->
 First of all, in terms of the dimensionality of the space: In[2] HU et al. sets the planning

<!-- b000113 | prose | pages [4] -->
space to three dimensions. However, in order to simplify the model, more authors tend to

<!-- b000114 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000115 | prose | pages [4] -->
consider the space as two dimensions[3].

<!-- b000116 | prose | pages [4] -->
 Secondly, in terms of the method of planning space: the commonly used methods include

<!-- b000117 | prose | pages [4] -->
Grid Method[4], Road Sign Method, and Artificial Potential Fields Method.

<!-- b000118 | prose | pages [4] -->
 Finally, the objective function of the UAV Cluster Path Planning Model generally uses

<!-- b000119 | prose | pages [4] -->
flight distance, threat cost, etc. For example, Xu et al. [5] takes the weighted sum of threat cost and time cost as the optimization target. What’s more, Constraints often include self- constraints and environmental constraints, such as flight speed and geographic altitude.  The strengths and weaknesses of the planning space can be visually presented and is

<!-- b000120 | prose | pages [4] -->
shown below:

<!-- b000121 | furniture | pages [4] -->


<!-- b000122 | caption | pages [4] -->
Figure 2: Literature Review Framework

<!-- b000123 | furniture | pages [4] -->


<!-- b000124 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000125 | prose | pages [4] -->
关注数学模型

<!-- b000126 | furniture | pages [4] -->
2

<!-- b000127 | furniture | pages [4] -->
MATHmodels

<!-- b000128 | furniture | pages [4] -->
获取更多资讯

<!-- b000129 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000130 | furniture | pages [5] -->
Team # 2102199                                                                            Page 5 of 25

<!-- b000131 | heading | pages [5] -->
1.4 Our Work

<!-- b000132 | prose | pages [5] -->
The problem requires us to fight fires by optimizing the locations of two type of drones. Our work mainly includes the following:

<!-- b000133 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000134 | prose | pages [5] -->
1) Based on the data of wildfires, a rasterized Multi-Objective Optimization Model is established; 2) The mixture of the two drones is given and the extreme fire events is considered; 3) Based on the verification model simulated by Poisson process and the hovering model based on Tabu Search, this article effectively demonstrates the validity and applica- bility. In order to avoid complicated description, intuitively reflect our work process, the flow chart is shown in Figure 3:

<!-- b000135 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000136 | caption | pages [5] -->
Figure 3: Flow Chart of Our Work

<!-- b000137 | heading | pages [5] -->
2 Assumptions and Explanations

<!-- b000138 | prose | pages [5] -->
Considering that practical problems always contain many complex factors, first of all, we need to make reasonable assumptions to simplify the model, and each hypothesis is closely followed by its corresponding explanation:

<!-- b000139 | prose | pages [5] -->
 Assumption 1: Only the influence of terrain on the drone is considered, and other factors such as temperature, humidity, and atmosphere are ignored. Explanation: The UAV's radiation communication range is only affected by terrain fac- tors, and other factors are minimal. In fact, these factors affect each other, but in order to simplify the model ,we ignore the interactions between these factors.  Assumption 2: The location of the EOC can be deployed around the fire due to an emergency. Explanation: The position of the EOC is not clearly given in the question. So, we assume that EOC can be set in a fire-free area around the wildfire site, since the glossary of the problem said that mobile EOC can be deployed near the site of an emergency.

<!-- b000140 | furniture | pages [5] -->


<!-- b000141 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000142 | prose | pages [5] -->
关注数学模型

<!-- b000143 | furniture | pages [5] -->
2

<!-- b000144 | furniture | pages [5] -->
MATHmodels

<!-- b000145 | furniture | pages [5] -->
获取更多资讯

<!-- b000146 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000147 | furniture | pages [6] -->
Team # 2102199                                                                            Page 6 of 25

<!-- b000148 | prose | pages [6] -->


<!-- b000149 | heading | pages [6] -->
Assumption 3: The "boots-on-the-ground" forward teams can be approximated as

<!-- b000150 | prose | pages [6] -->
near the fire site. Explanation: The actual movement of the team is very complicated, and it is difficult to accurately calculate its position. Therefore, it is assumed that the squad is near the fire

<!-- b000151 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000152 | prose | pages [6] -->
field and the drone arrives at the fire field to establish a connection with the squad.  Assumption 4: The collected data can be considered reliable and can reflect the changing laws of the Victorian wildfire. Explanation: The historical Victorian wildfire data, latitude, longitude and other data come from authoritative websites, such as the official website of FEC in Australia and NASA, with high accuracy.

<!-- b000153 | prose | pages [6] -->
Additional assumptions are made to simplify analysis for individual sections. These as- sumptions will be discussed at the appropriate locations.

<!-- b000154 | heading | pages [6] -->
3 Notations

<!-- b000155 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000156 | prose | pages [6] -->
Some important mathematical notations used in this paper are listed in Table 1.

<!-- b000157 | caption | pages [6] -->
Table 1: Notations used in this paper

<!-- b000158 | heading | pages [6] -->
Symbol

<!-- b000159 | prose | pages [6] -->
Description

<!-- b000160 | furniture | pages [6] -->


<!-- b000161 | prose | pages [6] -->
Longitude within the i-th Wildfire Grid

<!-- b000162 | furniture | pages [6] -->


<!-- b000163 | prose | pages [6] -->
Latitude within the i-th Wildfire Grid The area of the i-th grid

<!-- b000164 | prose | pages [6] -->
the distance

<!-- b000165 | furniture | pages [6] -->


<!-- b000166 | prose | pages [6] -->
-th grid

<!-- b000167 | furniture | pages [6] -->


<!-- b000168 | prose | pages [6] -->
between the -th roaming grid and the

<!-- b000169 | prose | pages [6] -->
Score for evaluating the -th wildfire grid

<!-- b000170 | prose | pages [6] -->
drone sent by the k-th EOC to the i-th wildfire the

<!-- b000171 | furniture | pages [6] -->


<!-- b000172 | prose | pages [6] -->
grid

<!-- b000173 | prose | pages [6] -->
drone sent by the k-th EOC to the i-th wildfire the

<!-- b000174 | furniture | pages [6] -->


<!-- b000175 | prose | pages [6] -->
grid

<!-- b000176 | furniture | pages [6] -->


<!-- b000177 | prose | pages [6] -->
The flight time of drones

<!-- b000178 | furniture | pages [6] -->


<!-- b000179 | prose | pages [6] -->
Note: There are some variables that are not listed here and will be discussed in detail in each section.

<!-- b000180 | heading | pages [6] -->
4 Model Preparation

<!-- b000181 | heading | pages [6] -->
4.1 Data Overview

<!-- b000182 | prose | pages [6] -->
The question did not provide us with data directly, so we need to consider which data to collect in the model building. Through the analysis of the problem, we need to collect the rel- evant information of Victoria, Australia, such as latitude and longitude, altitude, number of wildfires and so on. Due to the large amount of data, it is not convenient to list them all, so visualizing the data for display is a good method.

<!-- b000183 | furniture | pages [6] -->


<!-- b000184 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000185 | prose | pages [6] -->
关注数学模型

<!-- b000186 | furniture | pages [6] -->
2

<!-- b000187 | furniture | pages [6] -->
MATHmodels

<!-- b000188 | furniture | pages [6] -->
获取更多资讯

<!-- b000189 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000190 | furniture | pages [7] -->
Team # 2102199                                                                            Page 7 of 25

<!-- b000191 | heading | pages [7] -->
4.1.1 Data Collection

<!-- b000192 | prose | pages [7] -->
The official website of FEC in Victoria, Australia was queried and lots of data about wild- fires were obtained. And other data sources are shown in Table 2.

<!-- b000193 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000194 | caption | pages [7] -->
Table 2: Data and Database Websites

<!-- b000195 | prose | pages [7] -->
Database Names Database Websites

<!-- b000196 | prose | pages [7] -->
https://www.globalforestwatch.org/map/ Fire Alerts

<!-- b000197 | prose | pages [7] -->
https://search.earthdata.nasa.gov/search Altitude

<!-- b000198 | prose | pages [7] -->
https://www.kaggle.com/carlosparadis/fires- Latitude and Longitude

<!-- b000199 | prose | pages [7] -->
from-space-australia-and-new-zeland/data

<!-- b000200 | prose | pages [7] -->
Google Scholar https://scholar.google.com/

<!-- b000201 | prose | pages [7] -->
© 2021 Mapbox © OpenStreetMap Maps

<!-- b000202 | furniture | pages [7] -->


<!-- b000203 | heading | pages [7] -->
4.1.2 Data Screening

<!-- b000204 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000205 | prose | pages [7] -->
Judging from the map of Victoria in Figure 4 (right), the eastern region is mainly forest, while the western region is almost no forest. Furthermore, to demonstrate better the situation of wildfires, we plot over a heat map in Figure 4 (left).

<!-- b000206 | prose | pages [7] -->
Considering the heat map we made, it shows the number of wildfires in various states of Victoria from 2012 to 2021, the darker the color, the greater number of fires. Although fires have also occurred in the western region, the number of eastern regions is much higher than that in the western region.

<!-- b000207 | furniture | pages [7] -->


<!-- b000208 | furniture | pages [7] -->


<!-- b000209 | furniture | pages [7] -->


<!-- b000210 | furniture | pages [7] -->


<!-- b000211 | caption | pages [7] -->
Figure 4: Data Screening

<!-- b000212 | prose | pages [7] -->
Through the heat map above, when building the model, a reasonable choice of the size of the area can be made, because the main problem needs to be solved is the emergency treatment of wildfires, so we take the eastern part as the model building area. Bendigo Airport (36.7346S,144.3305E) has been chosen as the boundary of the division, using this longitude as the basis for division, and keep the eastern part, especially taking Southeast Coastal Area into consideration.

<!-- b000213 | furniture | pages [7] -->


<!-- b000214 | heading | pages [7] -->
4.2 Conversion from longitude and latitude to distance

<!-- b000215 | prose | pages [7] -->
Haversine formula can determine the distance between the two places. It can well reflect the influence of the curvature of the earth and is a common way to determine the distance

<!-- b000216 | furniture | pages [7] -->


<!-- b000217 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000218 | prose | pages [7] -->
关注数学模型

<!-- b000219 | furniture | pages [7] -->
2

<!-- b000220 | furniture | pages [7] -->
MATHmodels

<!-- b000221 | furniture | pages [7] -->
获取更多资讯

<!-- b000222 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000223 | furniture | pages [8] -->
Team # 2102199                                                                            Page 8 of 25

<!-- b000224 | prose | pages [8] -->
between the two places with given latitude and longitude in geography[6], seen in the equa- tion(1):

<!-- b000225 | furniture | pages [8] -->


<!-- b000226 | prose | pages [8] -->
(1)

<!-- b000227 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000228 | prose | pages [8] -->
Where R represents the radius of the earth, and indicates the latitude of the two places,

<!-- b000229 | prose | pages [8] -->
express the longitude of them, d is the distance between the them. and

<!-- b000230 | furniture | pages [8] -->


<!-- b000231 | heading | pages [8] -->
4.3 Description of the two drones

<!-- b000232 | prose | pages [8] -->
Although the two types of drones have different names, they all use the same drone, but they have different equipment and functions. The following part refers to Radio Repeater drones as RR drones. A brief schematic diagram is shown in Figure 5:

<!-- b000233 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000234 | furniture | pages [8] -->


<!-- b000235 | caption | pages [8] -->
Figure 5: Two Types of Drones

<!-- b000236 | heading | pages [8] -->
5 Rasterized Multi-Objective Optimization Model

<!-- b000237 | heading | pages [8] -->
5.1 Rasterization of Regions

<!-- b000238 | prose | pages [8] -->
The work of the predecessors has given us some inspiration. For this problem, we should first determine its spatial model[7]. The purpose is to use a mathematical model to express the actual physical environment, which is convenient for computer processing. According to the survey results in the literature review, this article uses grid method to tackle the problem.

<!-- b000239 | prose | pages [8] -->
Therefore, the grid label N of any point can be expressed as:

<!-- b000240 | furniture | pages [8] -->


<!-- b000241 | prose | pages [8] -->
(2)

<!-- b000242 | prose | pages [8] -->
is the coordinate of a potential place, the abscissa where

<!-- b000243 | prose | pages [8] -->
tude and the ordinate represents the latitude,

<!-- b000244 | prose | pages [8] -->
maximum length of the horizontal axis.

<!-- b000245 | prose | pages [8] -->
represents the longi-

<!-- b000246 | prose | pages [8] -->
is the grid size, , is the

<!-- b000247 | prose | pages [8] -->
Further, the coordinates of the grid center position can be obtained:

<!-- b000248 | furniture | pages [8] -->


<!-- b000249 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000250 | prose | pages [8] -->
关注数学模型

<!-- b000251 | furniture | pages [8] -->
2

<!-- b000252 | furniture | pages [8] -->
MATHmodels

<!-- b000253 | furniture | pages [8] -->
获取更多资讯

<!-- b000254 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000255 | furniture | pages [9] -->
Team # 2102199                                                                            Page 9 of 25

<!-- b000256 | furniture | pages [9] -->


<!-- b000257 | prose | pages [9] -->
(3)

<!-- b000258 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000259 | prose | pages [9] -->
The grid is divided into three types, Barrier Grid, Roaming Grid and Wildfire Grid, the specific introduction is as follows:

<!-- b000260 | prose | pages [9] -->
 Barrier Grid: The grid of obstacles is used to represent the mountains in the actual map.

<!-- b000261 | prose | pages [9] -->
Because the flying height of drones is limited, it is very difficult to fly over areas with high altitude. Therefore, grids with altitude exceeding a certain limit are transformed into grids of obstacles. This grid cannot be reached by any drones.

<!-- b000262 | prose | pages [9] -->
 Roaming Grid: The roaming grid is a location for emergency mobile EOC settings, that

<!-- b000263 | prose | pages [9] -->
is, in the event of a big fire, the EOC can be set up in the roaming grid.

<!-- b000264 | prose | pages [9] -->
 Wildfire Grid: As the name suggests, the grid where the wildfire occurs is called the

<!-- b000265 | prose | pages [9] -->
wildfire grid, which is the place that the SSA drones will fly to. These Grids can be easily visualized by Figure 6:

<!-- b000266 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000267 | furniture | pages [9] -->


<!-- b000268 | caption | pages [9] -->
Figure 6: Three types of grids

<!-- b000269 | furniture | pages [9] -->


<!-- b000270 | furniture | pages [9] -->


<!-- b000271 | heading | pages [9] -->
5.2 Wildfire Frequency-Distance Weighted Model

<!-- b000272 | prose | pages [9] -->
Firstly, the map of eastern Victoria is rasterized, and the grid size is = 10km. Secondly, the frequency of forest wildfires is the key data for establishing the drone swarm model. Through the Frequency-Distance Weighted Model, we can obtain the EOCs around the wild- fires. Due to the limited pages, the paper presents the southeast area (147.2915~149.1503E, 35.8000 ~ 39.1005S) with the largest number of wildfires.

<!-- b000273 | prose | pages [9] -->
Furthermore, the results of the number of drones in this area will be given in section 5.4. Although the results are given for this area, the model is extensible and can be easily extended to all areas of Victoria. Firstly, the heat map drawn by Python after rasterization is plotted as shown in Figure 7:

<!-- b000274 | furniture | pages [9] -->


<!-- b000275 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000276 | prose | pages [9] -->
关注数学模型

<!-- b000277 | furniture | pages [9] -->
2

<!-- b000278 | furniture | pages [9] -->
MATHmodels

<!-- b000279 | furniture | pages [9] -->
获取更多资讯

<!-- b000280 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000281 | furniture | pages [10] -->
Team # 2102199                                                                            Page 10 of 25

<!-- b000282 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000283 | furniture | pages [10] -->


<!-- b000284 | caption | pages [10] -->
Figure 7: Heat map after Rasterization

<!-- b000285 | prose | pages [10] -->
The blue grid represents the roaming grid surrounding the yellow wildfire grid. There is

<!-- b000286 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000287 | prose | pages [10] -->
no barrier grid in this terrain, so it will temporarily not be considered here. Altitude is assumed to be the same. In practice, there is a slight difference, but it is understandable to make some simplifications.

<!-- b000288 | prose | pages [10] -->
It can be seen that after rasterization, the discrete model is a bit more convenient to solve. In Table 3, we give some of the data searching from the website:

<!-- b000289 | caption | pages [10] -->
Table 3: Latitude and longitude data of VIIRS

<!-- b000290 | prose | pages [10] -->
latitude longitude bright_ti4

<!-- b000291 | prose | pages [10] -->
-37.5296 143.4565 344.8 -38.0547 143.9076 329.8 -38.0593 143.9081 339.4 -38.0566 143.9038 336.7 -38.0562 143.9098 327.7 … … …

<!-- b000292 | prose | pages [10] -->
scan instrument version daynight

<!-- b000293 | prose | pages [10] -->
0.54 VIIRS 1.0NRT D 0.51 VIIRS 1.0NRT D 0.51 VIIRS 1.0NRT D 0.52 VIIRS 1.0NRT D 0.52 VIIRS 1.0NRT D … … … … Note: The longitude and latitude will be used in the data, and one occurrence represents a wildfire in the place, total amount of the data is .

<!-- b000294 | prose | pages [10] -->
Through data processing, we can get the relevant statistical data information in this area -th wildfire grid, suppose the frequency of it is for the simulation. For the , when the lon-

<!-- b000295 | prose | pages [10] -->
should be increased by 1, so it can be expressed as fol- gitude and latitude , lowing:

<!-- b000296 | furniture | pages [10] -->


<!-- b000297 | prose | pages [10] -->
(4)

<!-- b000298 | prose | pages [10] -->
-th row of Table 3 for traversing, Where represents the , represents the number of the wildfire grid in Figure 8. Eq. (4) can get the total fire frequencies of each grid. Therefore, combined with the distance between the -th roaming grid and the -th can be modified as: grid, the value of quantitative index

<!-- b000299 | furniture | pages [10] -->


<!-- b000300 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000301 | furniture | pages [10] -->


<!-- b000302 | prose | pages [10] -->
(5)

<!-- b000303 | prose | pages [10] -->
关注数学模型

<!-- b000304 | furniture | pages [10] -->
2

<!-- b000305 | furniture | pages [10] -->
MATHmodels

<!-- b000306 | furniture | pages [10] -->
获取更多资讯

<!-- b000307 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000308 | furniture | pages [11] -->
Team # 2102199                                                                            Page 11 of 25

<!-- b000309 | prose | pages [11] -->
, the EOC should be more likely to set up for the The larger -th roaming area. Through Eq. (5), the descending scores of 33 roaming grids can be obtained. Since the eastern region has a large span, and the question requires rapid forest fire response, 2~3 EOCs are not enough to form a communication network in a short time. Considering the construction

<!-- b000310 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000311 | prose | pages [11] -->
cost of EOC, we select the top 4 EOCs.

<!-- b000312 | prose | pages [11] -->
Furthermore, the EOC distribution obtained by this sorting alone is relatively concentrated, and the balance is not considered, so the following algorithm is used to improve it. This algo- rithm can be viewed in the flowchart in Figure 8:

<!-- b000313 | furniture | pages [11] -->


<!-- b000314 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000315 | furniture | pages [11] -->


<!-- b000316 | caption | pages [11] -->
Figure 8: Algorithm to select EOCs

<!-- b000317 | prose | pages [11] -->
Using this method, the best EOCs can be found more reasonable and accurate, the results would be given in 5.4.

<!-- b000318 | heading | pages [11] -->
5.3 Multi-objective Optimization Model

<!-- b000319 | prose | pages [11] -->
The Multi-objective Optimization Model is an model that uses mathematical program- ming methods to determine the optimal solution. In this question, it is under the established goals (such as minimum cost and shortest distance) and given constraints (such as flight time and radiation range) , determine how to effectively deal with drone’s resources and solve the problem of the best combination of SSA drones and RR drones.

<!-- b000320 | prose | pages [11] -->
 Decision Variable

<!-- b000321 | prose | pages [11] -->
The labels of the SSA drones and RR drones are and , represents the

<!-- b000322 | furniture | pages [11] -->


<!-- b000323 | prose | pages [11] -->
drone sent by the k-th EOC to the i-th wildfire grid. Similarly, represents the that was dispatched by the k-th EOC to the i-th wildfire grid; both of them can only be 0 and 1, which is

<!-- b000324 | prose | pages [11] -->
 Objective Function

<!-- b000325 | prose | pages [11] -->
;

<!-- b000326 | prose | pages [11] -->
The two goals can be attributed to the smallest number of drones and the shortest time.

<!-- b000327 | furniture | pages [11] -->


<!-- b000328 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000329 | prose | pages [11] -->
关注数学模型

<!-- b000330 | furniture | pages [11] -->
2

<!-- b000331 | furniture | pages [11] -->
MATHmodels

<!-- b000332 | furniture | pages [11] -->
获取更多资讯

<!-- b000333 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000334 | furniture | pages [12] -->
Team # 2102199                                                                            Page 12 of 25

<!-- b000335 | prose | pages [12] -->
The mission scenario is to put out a bushfire quickly. Therefore, the requirement of drone exe- cution efficiency is very high, so one optimization goal should be set as the minimum time to complete the Rapid Bushfire Response; and the completion time can be expressed by minimiz- ing the maximum flight distance of each drone, so the first objective function is:

<!-- b000336 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000337 | furniture | pages [12] -->


<!-- b000338 | prose | pages [12] -->
(6)

<!-- b000339 | prose | pages [12] -->
are the roaming grids that selected by simulation. It will be shown in section 5.4. Eq.(6) reflects that the minimization of the maximum firefighting distance of the k-th EOC can be presented by the sum of the two types of drone's dispatch label and its corresponding distance.

<!-- b000340 | prose | pages [12] -->
The other goal is to minimize the number of drones deployed, since and can only be 0 and 1, so the sum of them is the total number of drones:

<!-- b000341 | furniture | pages [12] -->


<!-- b000342 | prose | pages [12] -->
(7)

<!-- b000343 | prose | pages [12] -->
There are two common methods to deal with multi-objective optimization, i.e. staged op- timization and weighted optimization. Considering the time cost, the weighted method has been

<!-- b000344 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000345 | prose | pages [12] -->
chosen to deal with the problem. Therefore, from (6),(7), we have Eq.(8):

<!-- b000346 | furniture | pages [12] -->


<!-- b000347 | prose | pages [12] -->
(8)

<!-- b000348 | prose | pages [12] -->
, the parameter will be optimized by simulation, of course, their order Where of magnitude should have been taken into consideration.

<!-- b000349 | prose | pages [12] -->
reflects the proportion of drones that need to be added when a extreme fire events comes, normally,  Constraints .

<!-- b000350 | prose | pages [12] -->
The time constraint requires that the working time of drones should not exceed its working time after charging once. Subject to the constraint by (9):

<!-- b000351 | furniture | pages [12] -->


<!-- b000352 | prose | pages [12] -->
(9)

<!-- b000353 | prose | pages [12] -->
are flight time and hover time, respectively. refers to the speed Where, and

<!-- b000354 | prose | pages [12] -->
. If the drone is about to run out of power, it needs to be returned to of the drones, the EOC for charging. Assuming that when the drone at a certain location needs to return, there will be a drone from EOC to take over. The distance constraints can be expressed as:

<!-- b000355 | furniture | pages [12] -->


<!-- b000356 | prose | pages [12] -->
(10)

<!-- b000357 | prose | pages [12] -->
There are also other constraints, for example, in view of the terrain, the altitude restriction et al. should be added. However, due to the limited pages, there is no way to give them all in the article; the simulation results will be directly given in the next section.

<!-- b000358 | furniture | pages [12] -->


<!-- b000359 | heading | pages [12] -->
5.4 Results and Analysis

<!-- b000360 | prose | pages [12] -->
We use Python for simulation, the intermediate process is a bit complicated and will not be redundantly given in this part; the results of the region are displayed directly as Figure 9:

<!-- b000361 | furniture | pages [12] -->


<!-- b000362 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000363 | prose | pages [12] -->
关注数学模型

<!-- b000364 | furniture | pages [12] -->
2

<!-- b000365 | furniture | pages [12] -->
MATHmodels

<!-- b000366 | furniture | pages [12] -->
获取更多资讯

<!-- b000367 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000368 | furniture | pages [13] -->
Team # 2102199                                                                            Page 13 of 25

<!-- b000369 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000370 | furniture | pages [13] -->


<!-- b000371 | caption | pages [13] -->
Figure 9:The results of Problem1

<!-- b000372 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000373 | prose | pages [13] -->
The Figure 9 shows the number of EOCs, RR drones and SSA drones under the condition that the farthest distance each EOC could manage, which means that the reflects the maximum number of drones dispatched when rapid response is required in the event of a wildfire in the area. This can be used as the total number of drones in the area.

<!-- b000374 | prose | pages [13] -->
The range in the red circle indicates the area that can be covered by drones. By analyzing the above figure, we can find: Most of the fire area can be effectively covered, and this is the path planning for the worst case of the fire location. When the fire is closer to the EOC, fewer drones can be used to complete the task. A total of 4 SSA drones and 4 RR drones were dis- patched throughout the region. The ratio of the two types of drones is close to 1:1. Consid- ering the time required for charging, a total of 8 SSA drones and 8 repeater drones are re- quired in the area .

<!-- b000375 | furniture | pages [13] -->


<!-- b000376 | heading | pages [13] -->
6 Model Verification Simulated by Poisson Process

<!-- b000377 | heading | pages [13] -->
6.1 Poisson Process of Extreme Fire Events

<!-- b000378 | prose | pages [13] -->
The possibility of extreme fire events in the next decade can be predicted by the occur- rence of such events in the past few decades. Detailed data on extreme fire incidents in Australia in previous years were found on website[8].

<!-- b000379 | prose | pages [13] -->
In [9], the author presents a general statistical methodology for the prediction of forest fires in the context of Poisson models. The article has inspired us for model building.

<!-- b000380 | prose | pages [13] -->
Poisson distribution is a discrete probability distribution commonly seen in statistics and probability. Therefore, we use the Poisson distribution model to predict the number of extreme fire events in the next ten years:

<!-- b000381 | furniture | pages [13] -->


<!-- b000382 | prose | pages [13] -->
(11)

<!-- b000383 | prose | pages [13] -->
represents the average occurrence rate of extreme fire incidents per unit time (here set

<!-- b000384 | furniture | pages [13] -->


<!-- b000385 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000386 | prose | pages [13] -->
关注数学模型

<!-- b000387 | furniture | pages [13] -->
2

<!-- b000388 | furniture | pages [13] -->
MATHmodels

<!-- b000389 | furniture | pages [13] -->
获取更多资讯

<!-- b000390 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000391 | furniture | pages [14] -->
Team # 2102199                                                                            Page 14 of 25

<!-- b000392 | prose | pages [14] -->
to 10 years), that is, fire incidents frequency; N(t) represents the number of occurrences of the event within t, n and N(t) share the same meaning; e is natural constant.

<!-- b000393 | prose | pages [14] -->
sets of extreme fire incidents data, we can obtain the ex- According to the obtained pression of :

<!-- b000394 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000395 | furniture | pages [14] -->


<!-- b000396 | prose | pages [14] -->
(12)

<!-- b000397 | prose | pages [14] -->
Put it into Eq.(11) and use the idea of traversal to find the probability distribution of n from 1 to 10.

<!-- b000398 | prose | pages [14] -->
Because there is no function to directly calculate the Poisson distribution in Python, we design our own algorithm to calculate the probability density distribution. The pseudocode is as follows:

<!-- b000399 | heading | pages [14] -->
Algorithm : Probability distribution of extreme fire events

<!-- b000400 | prose | pages [14] -->
Input:

<!-- b000401 | furniture | pages [14] -->


<!-- b000402 | prose | pages [14] -->
Output:

<!-- b000403 | furniture | pages [14] -->


<!-- b000404 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000405 | prose | pages [14] -->
for to do

<!-- b000406 | furniture | pages [14] -->


<!-- b000407 | prose | pages [14] -->
According to , the parameter of Poisson distribution can be calculated

<!-- b000408 | prose | pages [14] -->
from the aggregate Randomly select an integer

<!-- b000409 | furniture | pages [14] -->


<!-- b000410 | prose | pages [14] -->
in the entire dataset can be predicted based on the Poisson The probability of distribution Then the probability is recorded as

<!-- b000411 | prose | pages [14] -->
end

<!-- b000412 | furniture | pages [14] -->


<!-- b000413 | prose | pages [14] -->
Draw the probability density distribution of extreme fire events

<!-- b000414 | furniture | pages [14] -->


<!-- b000415 | prose | pages [14] -->
Through simulation, the probability density distribution is shown in Figure 10:

<!-- b000416 | furniture | pages [14] -->


<!-- b000417 | caption | pages [14] -->
Figure 10: The Probability Density Distribution of Extreme Fire Events

<!-- b000418 | prose | pages [14] -->
It can be seen from Figure 10 that the position with the highest probability density is roughly between 2 and 4, and the average number of occurrences can be accurately calculated by the mathematical expectation in the above figure.

<!-- b000419 | furniture | pages [14] -->


<!-- b000420 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000421 | prose | pages [14] -->
关注数学模型

<!-- b000422 | furniture | pages [14] -->
2

<!-- b000423 | furniture | pages [14] -->
MATHmodels

<!-- b000424 | furniture | pages [14] -->
获取更多资讯

<!-- b000425 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000426 | furniture | pages [15] -->
Team # 2102199                                                                            Page 15 of 25

<!-- b000427 | prose | pages [15] -->
Mathematical expectations, also written as mean, can represent the number of extreme

<!-- b000428 | prose | pages [15] -->
fires that may occur in Victoria in the next 10 years. It is recorded as

<!-- b000429 | prose | pages [15] -->
as follows:

<!-- b000430 | prose | pages [15] -->
, and its expression is

<!-- b000431 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000432 | furniture | pages [15] -->


<!-- b000433 | prose | pages [15] -->
(13)

<!-- b000434 | prose | pages [15] -->
Substituting relevant variables into Eq. (13), the result is 2.99431, To simplify the problem, . reflects the proportion of drones that need to be added when an extreme fire take events come in Eq. (8). After substituting the influence factor into the Multi-objective Op- timization Model, via simulation, the result will be shown in section 6.2.

<!-- b000435 | furniture | pages [15] -->


<!-- b000436 | heading | pages [15] -->
6.2 Model Verification and Analysis

<!-- b000437 | prose | pages [15] -->
Substituting the parameters into the model we have established in 5.3, we can simulate the new drone path and the result of the assigned quantity. Considering that the occurrence of

<!-- b000438 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000439 | prose | pages [15] -->
extreme fires is mainly manifested as an increase in the area of overfire, we will give simulation results under 1 to 10 times size of the unit area (unit area means area in the 5.3 model).

<!-- b000440 | prose | pages [15] -->
Cubic Spline Interpolation can be used to smooth the curve. It is defined as follows: For the interval

<!-- b000441 | prose | pages [15] -->
and the function values at these points

<!-- b000442 | prose | pages [15] -->
, , , these n+1 nodes

<!-- b000443 | prose | pages [15] -->
, is the dependent var-

<!-- b000444 | prose | pages [15] -->
satisfies three conditions, then iable we need to study. if the function is the cubic

<!-- b000445 | prose | pages [15] -->
with respect to n nodes. spline interpolation function of

<!-- b000446 | prose | pages [15] -->
The biggest advantage of using it is when the density of interpolation nodes gradually increases, the cubic spline interpolation function converges not only to the function itself and its derivative, but also to the derivative of the function, which is better than polynomial inter- polation.

<!-- b000447 | prose | pages [15] -->
Due to the large number of path diagrams obtained but limited pages, what we need to focus on is how to verify the rationality and analysis of the model; so we directly give the curves with the area of the wildfire as follows:

<!-- b000448 | prose | pages [15] -->
 From the perspective of quantity

<!-- b000449 | prose | pages [15] -->
60

<!-- b000450 | prose | pages [15] -->
50

<!-- b000451 | prose | pages [15] -->
Number of two drones

<!-- b000452 | prose | pages [15] -->
40

<!-- b000453 | prose | pages [15] -->
30

<!-- b000454 | prose | pages [15] -->
20

<!-- b000455 | prose | pages [15] -->
10

<!-- b000456 | prose | pages [15] -->
0

<!-- b000457 | prose | pages [15] -->
1 2 3 4

<!-- b000458 | prose | pages [15] -->
RR SSA

<!-- b000459 | prose | pages [15] -->
5 5 6 7 8 9 10

<!-- b000460 | furniture | pages [15] -->


<!-- b000461 | prose | pages [15] -->
S/times of unit area

<!-- b000462 | caption | pages [15] -->
Figure 11 Number of the two drones

<!-- b000463 | furniture | pages [15] -->


<!-- b000464 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000465 | prose | pages [15] -->
关注数学模型

<!-- b000466 | furniture | pages [15] -->
2

<!-- b000467 | furniture | pages [15] -->
MATHmodels

<!-- b000468 | furniture | pages [15] -->
获取更多资讯

<!-- b000469 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000470 | furniture | pages [16] -->
Team # 2102199                                                                            Page 16 of 25

<!-- b000471 | prose | pages [16] -->
1.In terms of the number of the two kinds of drones, when the fire area begins to increase, the number of RR drones grows faster. Probably because with the expansion of the fire area, more repeaters are needed to communicate to establish the connection between the front team and EOC.

<!-- b000472 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000473 | prose | pages [16] -->
2.However, when the fire area exceeds equal to or even greater than 9 times, the number of SSA drones exceeds that of RR drones, and the growth rate is increasing. The number of RR drones is almost unchanged. Through the observation and inference of the path, we guess that it may be because the fire area is too large and more SSAs are required for detailed detection. Since one RR drone can communicate with multiple SSA drones, after the fire area increases to a certain degree, the area has been fully covered by RR drones, so basically only SSA drones continue to grow.

<!-- b000474 | furniture | pages [16] -->


<!-- b000475 | prose | pages [16] -->
 From the perspective of time and ratio

<!-- b000476 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000477 | prose | pages [16] -->
time to cover all area

<!-- b000478 | prose | pages [16] -->
Ratio of RR to SSA

<!-- b000479 | furniture | pages [16] -->


<!-- b000480 | caption | pages [16] -->
Figure 12:Time to Cover and Ratio of RR to SSA

<!-- b000481 | prose | pages [16] -->
From Figure12 (left), it can be seen that: 1. At the beginning, the time to cover the fire area rose rapidly, exceeding 1.2 times compared with the original time. 2. However, when the burned area is increased from 3 times to 4 times, the time to deploy drones decreases briefly. This may be because the geometric distribution of drones under this area can be optimized for a shorter time. 3. When increasing from 4 times to 8 times, the coverage time of drones only slowly increases, reaching a state of equilibrium with the overfire area. 4. Continue to increase the burned area, the coverage time is growing rapidly. We suspect that the out of control has led to an increase in the number of SSA drones and a longer deployment time. From Figure12 (right), it can be seen that: The ratio of the two drones changes with the burned area. The ratio curve first rises and then falls. This provides a good basis for CFA to provide the ratio of two kinds of drones. After judging the fire area observed by satellite, when the number of two kinds of drones is equipped, the optimal effect can be obtained by following the ratio.

<!-- b000482 | prose | pages [16] -->
Of course, our model is not perfect, and more factors can be considered to make the anal- ysis more accurate. However, within the allowable range of error, we can draw the conclusion

<!-- b000483 | furniture | pages [16] -->


<!-- b000484 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000485 | prose | pages [16] -->
关注数学模型

<!-- b000486 | furniture | pages [16] -->
2

<!-- b000487 | furniture | pages [16] -->
MATHmodels

<!-- b000488 | furniture | pages [16] -->
获取更多资讯

<!-- b000489 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000490 | furniture | pages [17] -->
Team # 2102199                                                                            Page 17 of 25

<!-- b000491 | prose | pages [17] -->
that:

<!-- b000492 | heading | pages [17] -->
1. The cost of RR drones will increase compared to SSA drones under the premise when

<!-- b000493 | prose | pages [17] -->
the burned area does not increase much;

<!-- b000494 | heading | pages [17] -->
2. When the burned area exceeds a certain limit, SSA drones’ costs will highly increase.

<!-- b000495 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000496 | heading | pages [17] -->
7 Hovering Model Based on Tabu Search

<!-- b000497 | prose | pages [17] -->
Since the first question has already discussed the hovering situation and distribution of drones in plain areas, the plain terrain of eastern Victoria will not be discussed in this model. We will focus on mountain areas and urban areas.

<!-- b000498 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000499 | furniture | pages [17] -->


<!-- b000500 | caption | pages [17] -->
Figure 13:Altitudinal Map of Victoria[10]

<!-- b000501 | prose | pages [17] -->
There are some additional assumptions to simplify analysis for the question.  Hypothesis 1: Since the signal attenuation rate of the radio in the city is 50%, we also

<!-- b000502 | prose | pages [17] -->
consider the signal attenuation rate of the repeater to be 50%.  Hypothesis 2: In mountainous terrain, due to the complex terrain, the signal of the

<!-- b000503 | prose | pages [17] -->
repeater will drop as the flying height of the drone rises. We assume that it is a linear relationship.  Hypothesis 3: According to the information obtained on the Internet[11], the maxi-

<!-- b000504 | prose | pages [17] -->
mum flight altitude of the drone does not have the ability to directly cross mountain peaks. We assume that its maximum flight altitude threshold is 800m. Considering the page constraint, the article can not discuss all the cities and mountains in eastern Victoria. We focus on selecting the mountains and the famous city Melbourne in the diagram given by the problem to construct and optimize the model. Due to the altitude limita- tion of drones, we will deploy EOCs on the north and south sides of the mountains, and their drones will not bypass the mountains for relay and detection missions.

<!-- b000505 | heading | pages [17] -->
7.1 Model construction of mountains and urban areas

<!-- b000506 | prose | pages [17] -->
For the optimization of the hovering position of RR drones, Tabu Search(TS) is undoubt- edly a suitable algorithm. We still follow the grid method in question 1, set the grids with boundary intersection lines as mutual neighborhoods, that is, for any grid , the neighborhood grid can be understood as the neighborhood mapping on .Determine the four neighborhoods

<!-- b000507 | furniture | pages [17] -->


<!-- b000508 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000509 | prose | pages [17] -->
关注数学模型

<!-- b000510 | furniture | pages [17] -->
2

<!-- b000511 | furniture | pages [17] -->
MATHmodels

<!-- b000512 | furniture | pages [17] -->
获取更多资讯

<!-- b000513 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000514 | furniture | pages [18] -->
Team # 2102199                                                                            Page 18 of 25

<!-- b000515 | prose | pages [18] -->
as . the expression is:

<!-- b000516 | furniture | pages [18] -->


<!-- b000517 | prose | pages [18] -->
(14)

<!-- b000518 | prose | pages [18] -->
For the optimal hovering position of the repeater drone, considering economic factors and

<!-- b000519 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000520 | prose | pages [18] -->
efficiency, the grid that is closest to the line between the grid where is located and the grid which the fire source is located in can be considered to have the highest temporary evaluation value. Put it into the candidate set. By analogy, we can integrate a temporarily considered op- timal path, and calculate the cost of . Since this process completely follows the principle of local optimality, over-fitting may , and at the same time list occur. We go back to the root node that has just been selected as a taboo object, and put it in the taboo table and have a discussion. Select an element in the remaining neighborhood to enter the candidate set, repeat the above algorithm again, and cal- culate the cost .

<!-- b000521 | prose | pages [18] -->
grid is needed to walk from We define that to a certain grid, and set it as the -th . When the first level of neighborhood mapping is completely trav- neighborhood map on

<!-- b000522 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000523 | prose | pages [18] -->
ersed, we find that over-fitting will also occur from the second level of mapping.

<!-- b000524 | prose | pages [18] -->
At this time, we will amnesty all the elements in the taboo table and use the same method to treat the next few levels of neighbors. The domain is traversed layer by layer, and under different paths is calculated separately and put into the taboo table. Finally, through the com- value is determined. parison, the path with the smallest After that, let us consider the attenuation of repeater and radio signals as the altitude in- creases, which conforms to the following expression:

<!-- b000525 | furniture | pages [18] -->


<!-- b000526 | prose | pages [18] -->
(15)

<!-- b000527 | prose | pages [18] -->
is the distance that the radio can emit after attenuation, Where refers to the distance represents the attenuation coefficient, and that the radio can emit before attenuation, the altitude.

<!-- b000528 | prose | pages [18] -->
is

<!-- b000529 | prose | pages [18] -->
Compared with cities, there is no interference from other electromagnetic waves in the mountains, so its attenuation coefficient is smaller than that in cities. After consulting the data, we have calculated that it is between 0.4 and 0.45. We set it to 0.4 for easy calculation.

<!-- b000530 | furniture | pages [18] -->


<!-- b000531 | heading | pages [18] -->
7.2 Simulation Results

<!-- b000532 | prose | pages [18] -->
Based on the above, the distribution position of the RR drones can be basically determined. Affected by space, all calculation results will not be released here, the optimal results will be displayed through the following visual drawing:

<!-- b000533 | furniture | pages [18] -->


<!-- b000534 | furniture | pages [18] -->


<!-- b000535 | caption | pages [18] -->
Figure 14: Mountain Areas

<!-- b000536 | furniture | pages [18] -->


<!-- b000537 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000538 | prose | pages [18] -->
关注数学模型

<!-- b000539 | furniture | pages [18] -->
2

<!-- b000540 | furniture | pages [18] -->
MATHmodels

<!-- b000541 | furniture | pages [18] -->
获取更多资讯

<!-- b000542 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000543 | furniture | pages [19] -->
Team # 2102199                                                                            Page 19 of 25

<!-- b000544 | prose | pages [19] -->
 The yellow area in the left picture shows the coverage of the RR drones, it shows that the

<!-- b000545 | prose | pages [19] -->
results obtained by using TS algorithm can well cover the mountainous area.

<!-- b000546 | prose | pages [19] -->
 The figure on the right shows the movement path of the RR drones. It can be seen from

<!-- b000547 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000548 | prose | pages [19] -->
the figure that such a planning scheme can use fewer repeater drones to achieve full cov- erage of the mountains. From the side, the method we use is fast and effective.

<!-- b000549 | prose | pages [19] -->
 The network also takes into account the time cost. Therefore, when constructing the net-

<!-- b000550 | prose | pages [19] -->
work, the maximum number of layers is 3. If setting fewer EOCs, the number of layers of the network will be too many, and the time to deploy drones will increase significantly. We are supposed to meet the requirements for rapid emergency response.

<!-- b000551 | furniture | pages [19] -->


<!-- b000552 | prose | pages [19] -->
Similarly, the construction of the urban area model uses the same tabu search algorithm as the mountain model to find the most economical path. Only for the smaller cities around Melbourne, we also need to take into account the situation that they face sudden fires, so we set up EOCs on the surrounding of Melbourne in case of the sudden fires in Geelong and Cran- bourne. Since the title clearly states that the radio will attenuate to 2 kilometers in the city, no

<!-- b000553 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000554 | prose | pages [19] -->
more expressions are added here. The finally calculated hovering position of the RR drones is shown in the figure below:

<!-- b000555 | furniture | pages [19] -->


<!-- b000556 | furniture | pages [19] -->


<!-- b000557 | furniture | pages [19] -->


<!-- b000558 | caption | pages [19] -->
Figure 15: Urban Areas

<!-- b000559 | prose | pages [19] -->
So far, our model has been established, perfected and verified. It can be seen that the optimized model can be applied to different terrains, and it takes into account economic and time costs. It is a highly usable model result.

<!-- b000560 | furniture | pages [19] -->


<!-- b000561 | heading | pages [19] -->
8 Sensitivity and Robustness Analysis

<!-- b000562 | heading | pages [19] -->
8.1 Sensitivity Analysis

<!-- b000563 | prose | pages [19] -->
is introduced to estimate the parameters of the extreme fire events. In section 5.3, factor Therefore, change the size of this parameter, that is, the average number of extreme fires per decade has changed. We want to analyze the sensitivity of this parameter.

<!-- b000564 | furniture | pages [19] -->


<!-- b000565 | prose | pages [19] -->
(16) The reason for the only consider increase rather than decrease of is to reflect the worst case, that is, the average number of fires per decade is more, and observe whether our model is sensitive to this parameter.

<!-- b000566 | furniture | pages [19] -->


<!-- b000567 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000568 | prose | pages [19] -->
关注数学模型

<!-- b000569 | furniture | pages [19] -->
2

<!-- b000570 | furniture | pages [19] -->
MATHmodels

<!-- b000571 | furniture | pages [19] -->
获取更多资讯

<!-- b000572 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000573 | furniture | pages [20] -->
Team # 2102199                                                                            Page 20 of 25

<!-- b000574 | prose | pages [20] -->
Therefore, Re-simulate the calculation results and obtain 4 sets of curves as shown in

<!-- b000575 | caption | pages [20] -->
Figure 16:

<!-- b000576 | prose | pages [20] -->
3.5

<!-- b000577 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000578 | prose | pages [20] -->
3

<!-- b000579 | prose | pages [20] -->
Ratio of RR to SSA

<!-- b000580 | prose | pages [20] -->
2.5

<!-- b000581 | prose | pages [20] -->
2

<!-- b000582 | prose | pages [20] -->
1.5

<!-- b000583 | prose | pages [20] -->
1

<!-- b000584 | prose | pages [20] -->
Ratio

<!-- b000585 | prose | pages [20] -->
0.5

<!-- b000586 | prose | pages [20] -->
1 2 3 4 5 6 7 8 9 10

<!-- b000587 | furniture | pages [20] -->


<!-- b000588 | prose | pages [20] -->
S/times of unit area

<!-- b000589 | caption | pages [20] -->
Figure 16: Sensitivity analysis of

<!-- b000590 | prose | pages [20] -->
It is indicated that with the increase of 5% of each step length, the number of both types of drones is on the rise. However, the growth of both did not change in the form of a curve.

<!-- b000591 | prose | pages [20] -->
Correspondingly, the ratio of the two drones that CFA needs to be equipped has also in-

<!-- b000592 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000593 | prose | pages [20] -->
creased, which is reasonable and can be explained. The trend of the curve obtained by sensi- tivity test is consistent with the actual situation.

<!-- b000594 | furniture | pages [20] -->


<!-- b000595 | heading | pages [20] -->
8.2 Sensitivity Analysis

<!-- b000596 | prose | pages [20] -->
Furthermore, we also verified the robustness of our model. While we add 5% random , Its practical significance is: We hope to study whether the disturbance to and drones can accurately reach the destination when there is a certain deviation in the data be- tween the two places and calculate how much the required time is disturbed:

<!-- b000597 | furniture | pages [20] -->


<!-- b000598 | prose | pages [20] -->
(17)

<!-- b000599 | furniture | pages [20] -->


<!-- b000600 | prose | pages [20] -->
(18) We did 1000 simulations. The calculation found that 95.7% of UAVs can reach the des- tination correctly, and the degree of deviation from the original time is shown in the table:

<!-- b000601 | caption | pages [20] -->
Table 4: Degree of Deviation from The Original Time

<!-- b000602 | prose | pages [20] -->
Number Time Error

<!-- b000603 | prose | pages [20] -->
1 -0.9654% 2 1.5987% 3 2.1391% 4 -1.9439% 5 0.3823% … …

<!-- b000604 | prose | pages [20] -->
We can find that the disturbance of

<!-- b000605 | prose | pages [20] -->
Number Time Error

<!-- b000606 | prose | pages [20] -->
6 0.2689% 7 -3.2657% 8 2.1894% 9 UNFOUND 10 -1.2243% … …

<!-- b000607 | prose | pages [20] -->
has a certain influence on the result, but it is within an acceptable range. Therefore, when the CFA handles a fire, even if there is a slight error in the distance calculation, the task can be completed to a large extent, and the time er- ror does not exceed 5%.

<!-- b000608 | furniture | pages [20] -->


<!-- b000609 | furniture | pages [20] -->


<!-- b000610 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000611 | prose | pages [20] -->
关注数学模型

<!-- b000612 | furniture | pages [20] -->
2

<!-- b000613 | furniture | pages [20] -->
MATHmodels

<!-- b000614 | furniture | pages [20] -->
获取更多资讯

<!-- b000615 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000616 | furniture | pages [21] -->
Team # 2102199                                                                            Page 21 of 25

<!-- b000617 | heading | pages [21] -->
9 Evaluation of Strengths and Weaknesses

<!-- b000618 | heading | pages [21] -->
9.1 Strengths

<!-- b000619 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000620 | prose | pages [21] -->
Our model offers the following strengths:  The main strength is its enormous extensible and including all factors into a single, robust

<!-- b000621 | prose | pages [21] -->
framework. For instance, the rapid deployment plan of locations of hovering VHF/UHF radio-repeater drones for fires can be applied not only to Victoria, Australia, but also to New South Wales and others by Calculating Figure 9;

<!-- b000622 | prose | pages [21] -->
and use the algorithm presented by

<!-- b000623 | heading | pages [21] -->
 The Rasterized Multi-Objective Optimization Model is scientific and reasonable. More-

<!-- b000624 | prose | pages [21] -->
over, the idea of rasterization is used creatively by us, and can be suitable for different

<!-- b000625 | heading | pages [21] -->
practical situations. Results of extreme fire events prediction based on Poisson distribu-

<!-- b000626 | prose | pages [21] -->
tion have a reliable statistical description;

<!-- b000627 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000628 | prose | pages [21] -->
 The visualization work is done very well by us, such as the framework of the research

<!-- b000629 | prose | pages [21] -->
method in the literature review, the schematic diagram of the two drones in the introduc- tion, the heat map made in the fire research, and the curve of the Poisson distribution etc. Boring data may be able to reflect the law, but not as intuitive as so many images;

<!-- b000630 | prose | pages [21] -->
 Our model effectively achieved all of the goals. It was not only fast and could handle

<!-- b000631 | prose | pages [21] -->
large quantities of data, but also had the flexibility we desired. For example, compared to the basic model, the occurrence of extreme fire invents is also taken into account and have a good result;

<!-- b000632 | prose | pages [21] -->
 Effectiveness of the model can be demonstrated under different parameter of the model

<!-- b000633 | prose | pages [21] -->
by sensitivity analysis. So the model can be applied to much more wildfire events.

<!-- b000634 | furniture | pages [21] -->


<!-- b000635 | heading | pages [21] -->
9.2 Weaknesses and Further Improvements

<!-- b000636 | prose | pages [21] -->
Our model has the following limitations and related improvements:  The analysis of locations of hovering VHF/UHF radio-repeater drones for fires can be

<!-- b000637 | prose | pages [21] -->
more accurate if we have more complete data;

<!-- b000638 | prose | pages [21] -->
 The assumption that the "boots-on-the-ground" forward teams can be approximated as

<!-- b000639 | prose | pages [21] -->
near the fire site is a bit idealized. If the trajectory of the team is taken into account, a more practical model and results can be obtained.

<!-- b000640 | prose | pages [21] -->
 Some approximate analysis methods are applied to model other places, which may lead

<!-- b000641 | prose | pages [21] -->
to the situation that not to be the most optimal.

<!-- b000642 | furniture | pages [21] -->


<!-- b000643 | furniture | pages [21] -->


<!-- b000644 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000645 | prose | pages [21] -->
关注数学模型

<!-- b000646 | furniture | pages [21] -->
2

<!-- b000647 | furniture | pages [21] -->
MATHmodels

<!-- b000648 | furniture | pages [21] -->
获取更多资讯

<!-- b000649 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000650 | furniture | pages [22] -->
Team # 2102199                                                                            Page 22 of 25

<!-- b000651 | prose | pages [22] -->
Budget Request

<!-- b000652 | prose | pages [22] -->
Dear Victoria State Government:

<!-- b000653 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000654 | furniture | pages [22] -->


<!-- b000655 | prose | pages [22] -->
Forest fires have always been the greatest threat to Australia. Tens of thousands of lives are lost every year in these fires. We are very worried about this situa- tion. After our investigation, we found that the eastern coastal plain of Victoria is the most frequent place for fires, which can be clearly shown from the figure on the right.

<!-- b000656 | furniture | pages [22] -->


<!-- b000657 | prose | pages [22] -->
It is too dangerous for people to enter the fire scene directly. Therefore, we believe that drones should be used to detect the fire scene and ensure

<!-- b000658 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000659 | prose | pages [22] -->
safety before allowing people to en- ter. Meanwhile, we also know that

<!-- b000660 | prose | pages [22] -->
(The red dots indicate the fire scene)

<!-- b000661 | prose | pages [22] -->
drones are very expensive, so we optimize the model as much as possible to re- duce the budget. But some necessary expenses are still inevitable:

<!-- b000662 | furniture | pages [22] -->


<!-- b000663 | prose | pages [22] -->
For eastern coastal plain areas, since it is the most frequent for fires, we have deployed more drones to ensure the safety. We have arranged a total of sixteen drones to face various emergencies happened in this area, which may cost around 160,000 dollars. Based on the data from the past half century, we found that there is a possibility of extreme fire events in this area. Because of this, we predicted the number of extreme fire events in the next ten years and planned corresponding countermeasures. Conservatively estimated, it may take about 970,000 dollars to deal with extreme fire events in the next ten years.

<!-- b000664 | furniture | pages [22] -->


<!-- b000665 | prose | pages [22] -->
For mountain areas, due to the obstruction of terrain, drones cannot cross the mountains, so we deployed the EOCs in the north and south of the mountains to improve the efficiency of firefighting. Thus, we need much more drones to over- come various obstacles from signal and terrain. According to the calculation re- sults, about 830,000 dollars are needed to meet the above demand.

<!-- b000666 | furniture | pages [22] -->


<!-- b000667 | prose | pages [22] -->
For metropolitan areas, because of the blocking of buildings and the interfer- ence of electromagnetic waves, the effect of radio signals in the city is poor. Con- sidering these, the layout of drones is more difficult. It’s more complex. After many optimizations, we finally found a better method, but it still needs 570,000 dollars as the equipment cost.

<!-- b000668 | furniture | pages [22] -->


<!-- b000669 | prose | pages [22] -->
At the end, to facilitate your better reading, we show all the funds needed in the

<!-- b000670 | furniture | pages [22] -->


<!-- b000671 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000672 | prose | pages [22] -->
关注数学模型

<!-- b000673 | furniture | pages [22] -->
2

<!-- b000674 | furniture | pages [22] -->
MATHmodels

<!-- b000675 | furniture | pages [22] -->
获取更多资讯

<!-- b000676 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000677 | furniture | pages [23] -->
Team # 2102199                                                                            Page 23 of 25

<!-- b000678 | prose | pages [23] -->
following table:

<!-- b000679 | furniture | pages [23] -->


<!-- b000680 | prose | pages [23] -->
Normal

<!-- b000681 | prose | pages [23] -->
Cost Condition

<!-- b000682 | furniture | pages [23] -->


<!-- b000683 | prose | pages [23] -->
Extreme

<!-- b000684 | prose | pages [23] -->
Total($)

<!-- b000685 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000686 | prose | pages [23] -->
events($)

<!-- b000687 | prose | pages [23] -->
160,000 Eastern coast plain

<!-- b000688 | prose | pages [23] -->
10,000 Mountains

<!-- b000689 | prose | pages [23] -->
10,000 Metropolis

<!-- b000690 | furniture | pages [23] -->


<!-- b000691 | prose | pages [23] -->
events($)

<!-- b000692 | prose | pages [23] -->
970,000 1,130,000

<!-- b000693 | furniture | pages [23] -->


<!-- b000694 | prose | pages [23] -->
830,000

<!-- b000695 | furniture | pages [23] -->


<!-- b000696 | prose | pages [23] -->
570,000

<!-- b000697 | furniture | pages [23] -->


<!-- b000698 | prose | pages [23] -->
From CFA in Victoria

<!-- b000699 | prose | pages [23] -->
February 8, 2021

<!-- b000700 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000701 | furniture | pages [23] -->


<!-- b000702 | furniture | pages [23] -->


<!-- b000703 | furniture | pages [23] -->


<!-- b000704 | furniture | pages [23] -->


<!-- b000705 | furniture | pages [23] -->


<!-- b000706 | furniture | pages [23] -->


<!-- b000707 | furniture | pages [23] -->


<!-- b000708 | furniture | pages [23] -->


<!-- b000709 | furniture | pages [23] -->


<!-- b000710 | furniture | pages [23] -->


<!-- b000711 | furniture | pages [23] -->


<!-- b000712 | furniture | pages [23] -->


<!-- b000713 | furniture | pages [23] -->


<!-- b000714 | furniture | pages [23] -->


<!-- b000715 | furniture | pages [23] -->


<!-- b000716 | furniture | pages [23] -->


<!-- b000717 | furniture | pages [23] -->


<!-- b000718 | furniture | pages [23] -->


<!-- b000719 | furniture | pages [23] -->


<!-- b000720 | furniture | pages [23] -->


<!-- b000721 | furniture | pages [23] -->


<!-- b000722 | furniture | pages [23] -->


<!-- b000723 | furniture | pages [23] -->


<!-- b000724 | furniture | pages [23] -->


<!-- b000725 | furniture | pages [23] -->


<!-- b000726 | furniture | pages [23] -->


<!-- b000727 | furniture | pages [23] -->


<!-- b000728 | furniture | pages [23] -->


<!-- b000729 | furniture | pages [23] -->


<!-- b000730 | furniture | pages [23] -->


<!-- b000731 | furniture | pages [23] -->


<!-- b000732 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000733 | prose | pages [23] -->
关注数学模型

<!-- b000734 | furniture | pages [23] -->
2

<!-- b000735 | furniture | pages [23] -->
MATHmodels

<!-- b000736 | furniture | pages [23] -->
获取更多资讯

<!-- b000737 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000738 | furniture | pages [24] -->
Team # 2102199                                                                            Page 24 of 25

<!-- b000739 | heading | pages [24] -->
References

<!-- b000740 | references | pages [24] -->
[1]  GLOBAL FOREST WHATCH OF AUSTRALIA https://www.globalforestwatch.org/top-

<!-- b000741 | references | pages [24] -->
微信公众号：数学模型

<!-- b000742 | references | pages [24] -->
ics/fires/?topic=fires#footer

<!-- b000743 | references | pages [24] -->
[2]  HU Teng, LIU Zhanjun, LIU Yang, et al. 3D reconnaissance path planning of multiple

<!-- b000744 | references | pages [24] -->
UAVs. Journal of Systems Engineering and Electronics, 2019, 41(7): 1551 – 1559.

<!-- b000745 | references | pages [24] -->
[3]  BASBOUS B. 2D UAV path planning with radar threatening areas using simulated anneal-

<!-- b000746 | references | pages [24] -->
ing algorithm for event detection. The 2018 International Conference on Artificial Intelli-

<!-- b000747 | references | pages [24] -->
gence and Data Processing. Malatya, Turkey: IEEE, 2018: 1 – 7.

<!-- b000748 | references | pages [24] -->
[4]  WANG W F, WU Y C, ZHANG X. Research of the unit decomposing traversal method

<!-- b000749 | references | pages [24] -->
based on grid method of the mobile robot. Techniques of Automation and Applications,

<!-- b000750 | references | pages [24] -->
2013, 32(11): 34 – 38.

<!-- b000751 | references | pages [24] -->
[5]  XU Jian, ZHOU Deyun, HUANG He. Multi UAV path planning based on improved ge-

<!-- b000752 | references | pages [24] -->
netic algorithm. Aeronautical Computing Technique, 2009, 39(4): 43 – 46.

<!-- b000753 | references | pages [24] -->
微信号：MATHmodels

<!-- b000754 | references | pages [24] -->
[6]  G T S Lee, Lee G T S, Arisandi D, et al. Travel App - showing nearest tourism site using

<!-- b000755 | references | pages [24] -->
Haversine formula and directions with Google Maps. 2020, 852(1):012161-.

<!-- b000756 | references | pages [24] -->
[7]  Chen Kun. Research and Verification of Multi-UAV Cooperative Control Technology in

<!-- b000757 | references | pages [24] -->
Dynamic Environment. 2019

<!-- b000758 | references | pages [24] -->
[8]  List of major bushfires in Australia From Wikipedia, the free encyclopedia https://en.wik-

<!-- b000759 | references | pages [24] -->
ipedia.org/wiki/List_of_major_bushfires_in_Australia

<!-- b000760 | references | pages [24] -->
[9]  Mandallaz, D,R Ye. Prediction of forest fires with Poisson models. Journal of Forest Re-

<!-- b000761 | references | pages [24] -->
search . 1997

<!-- b000762 | references | pages [24] -->
[10]  ALTITUDINAL MAP OF VICTORIA http://romseyaustralia.com/rombook1map1.html

<!-- b000763 | references | pages [24] -->
[11]  Drone Laws in Australia

<!-- b000764 | references | pages [24] -->
https://web.archive.org/web/20170515150737/http://uavcoach.com/drone-laws-in-aus-

<!-- b000765 | references | pages [24] -->
tralia/

<!-- b000766 | furniture | pages [24] -->


<!-- b000767 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000768 | references | pages [24] -->
关注数学模型

<!-- b000769 | furniture | pages [24] -->
2

<!-- b000770 | furniture | pages [24] -->
MATHmodels

<!-- b000771 | furniture | pages [24] -->
获取更多资讯

<!-- b000772 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000773 | furniture | pages [25] -->
Team # 2102199                                                                            Page 25 of 25

<!-- b000774 | heading | pages [25] -->
Appendices

<!-- b000775 | prose | pages [25] -->
Python code

<!-- b000776 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000777 | heading | pages [25] -->
1. from haversine import haversine, Unit

<!-- b000778 | heading | pages [25] -->
2. import folium

<!-- b000779 | heading | pages [25] -->
3. import pandas as pd

<!-- b000780 | heading | pages [25] -->
4. from folium.plugins import HeatMap

<!-- b000781 | heading | pages [25] -->
5. import numpy as np

<!-- b000782 | prose | pages [25] -->
6.

<!-- b000783 | heading | pages [25] -->
7. def mark_Repeater(location: tuple, longth,color = 'red'):

<!-- b000784 | prose | pages [25] -->
8.     folium.Circle(

<!-- b000785 | prose | pages [25] -->
9.         radius=longth,

<!-- b000786 | prose | pages [25] -->
10.         location=location,

<!-- b000787 | prose | pages [25] -->
11.         color='orange',

<!-- b000788 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000789 | prose | pages [25] -->
12.         fill=True,

<!-- b000790 | prose | pages [25] -->
13.     ).add_to(m)

<!-- b000791 | prose | pages [25] -->
14.     folium.Marker(location, icon=folium.Icon(color=color, pre-

<!-- b000792 | prose | pages [25] -->
fix='fa', icon='tree')).add_to(m)

<!-- b000793 | prose | pages [25] -->
15.

<!-- b000794 | prose | pages [25] -->
16.

<!-- b000795 | heading | pages [25] -->
17. def fill_grid(m, boundary, color):

<!-- b000796 | heading | pages [25] -->
18.     for (a, b) in boundary:

<!-- b000797 | prose | pages [25] -->
19.         a = a-1

<!-- b000798 | prose | pages [25] -->
20.         b = b-1

<!-- b000799 | prose | pages [25] -->
21.         folium.Polygon([

<!-- b000800 | prose | pages [25] -->
22.             [-35.8 - (b - 1) * 0.09, 144.4 + (a - 1) * 0.1158849],

<!-- b000801 | prose | pages [25] -->
23.             [-35.8 - (b - 1) * 0.09, 144.4 + a * 0.1158849],

<!-- b000802 | prose | pages [25] -->
24.             [-35.8 - b * 0.09, 144.4 + a * 0.1158849],

<!-- b000803 | prose | pages [25] -->
25.             [-35.8 - b * 0.09, 144.4 + (a - 1) * 0.1158849],

<!-- b000804 | prose | pages [25] -->
26.         ], color=color, weight=2, fill=True, fill_color=color, fill_opac

<!-- b000805 | prose | pages [25] -->
ity=0.3).add_to(m)

<!-- b000806 | furniture | pages [25] -->


<!-- b000807 | furniture | pages [25] -->


<!-- b000808 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000809 | prose | pages [25] -->
关注数学模型

<!-- b000810 | furniture | pages [25] -->
2

<!-- b000811 | furniture | pages [25] -->
MATHmodels

<!-- b000812 | furniture | pages [25] -->
获取更多资讯
