# P-B-2021-2102199-f3e89239

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
2021

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
B

<!-- b000007 | title | pages [1] -->
2102199

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
Build an Army of Drones to Fight Wildfires

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | prose | pages [1] -->
Global warming, El Niño... With the emergence of various extreme climates, Australia's wildfires occur more frequently. The greenhouse gases emitted after combustion have exacer- bated global warming, which seems to have entered an endless loop. At the same time, hun- dreds of millions of lives have been killed in the fire, which makes us sad. In order to better control wildfires, we modeled the distribution of drones assisting in the observation to achieve the best balance between economy and efficiency.

<!-- b000012 | prose | pages [1] -->
Several models are established: Model I: Rasterized Multi-Objective Optimization Model; Model II: Model Verification Simulated by Poisson Process; Model III: Hovering Model Based on Tabu Search, etc.

<!-- b000013 | prose | pages [1] -->
Before all the models are established, we rasterize the area to be studied. Through the discrete grid, we can do better analysis. Moreover, we use a variety of visualization methods to make the results more intuitive.

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
For Model I: According to the heat map about distribution of fires in Victoria in recent years, we found that the main fire areas are the plains along the eastern coast. Inspired by weights and Multi-Objective Optimization algorithms, we built a brand-new model to find the best location for EOCs and draw up a suitable hover position and reconnaissance route for the drone. Based on the different positions of the fire site, calculate the maximum number of two types of drones and their ratio. The results are shown in Figure 9.

<!-- b000016 | prose | pages [1] -->
For Model II: This model is actually a supplement to Model I. In the Model I, the fire only appeared in a small area, and there was a possibility of extreme fire events in the study area. Combining the data about nearly half a century and using the Poisson Distribution to obtain the probability and mathematical expectation, it can be concluded that 2.99431 extreme fire events may occur in the next ten years, which is approximately considered to be 3 times. After that, use the mobile EOC to deal with extreme fire events, and utilize the method of Model I to rebuild the drone network to find out what equipment costs need to be increased. Due to the di- versity of the results, it will be shown in section 6.2.

<!-- b000017 | prose | pages [1] -->
For Model III: To tackle the problem of how to optimize the hover position of drones in different terrains, the Tabu Search algorithm (TS) is a good choice. Using the Tabu Search algorithm can make the hover position of the drones achieve the global optimal effect under different terrain conditions. Since drone signals are severely interfered in urban areas, the rea- sonable distribution of EOCs enables it to quickly network to respond to sudden urban fires. The obstruction of mountainous terrain restricts the drone's flying range. Therefore, dividing the area into blocks and managing them separately can effectively improve efficiency.

<!-- b000018 | prose | pages [1] -->
In addition, because rich terrain and emergencies have been discussed in the above three models, our model has strong adaptability. Not only can it be used in the area we are studying, but it can also be used in the rest of Australia.

<!-- b000019 | prose | pages [1] -->
Finally, sensitivity analysis of the mathematical expectation of extreme fire events shows that our model is not sensitive to changes in , that is, it can be applied to areas with different extreme fire invents. Meanwhile, robustness of our model has also been tested. While adding 5% random disturbance to and , the maximum time error is 3.2657%. The model can be considered stable. Afterwards, a Budget Request supported by our stable models has been written for CFA.

<!-- b000020 | keywords | pages [1] -->
Keywords: Fighting Wildfires; Multi-Objective Optimization; Poisson Distribution; Tabu Search

<!-- b000021 | prose | pages [1] -->
Algorithm; Sensitivity Analysis

<!-- b000022 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000023 | prose | pages [1] -->
关注数学模型

<!-- b000024 | furniture | pages [1] -->
2

<!-- b000025 | furniture | pages [1] -->
MATHmodels

<!-- b000026 | furniture | pages [1] -->
获取更多资讯

<!-- b000027 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000028 | furniture | pages [2] -->
Team # 2102199                                                                            Page 2 of 25

<!-- b000029 | heading | pages [2] -->
Contents

<!-- b000030 | contents | pages [2] -->
1 Introduction ...................................................................................................... 3

<!-- b000031 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000032 | contents | pages [2] -->
1.1 Problem Background ....................................................................................................... 3

<!-- b000033 | contents | pages [2] -->
1.2 Restatement of the Problem ............................................................................................. 3

<!-- b000034 | contents | pages [2] -->
1.3 Literature Review ............................................................................................................. 4

<!-- b000035 | contents | pages [2] -->
1.4 Our Work .......................................................................................................................... 5

<!-- b000036 | contents | pages [2] -->
2 Assumptions and Explanations ....................................................................... 5

<!-- b000037 | contents | pages [2] -->
3 Notations ........................................................................................................... 6

<!-- b000038 | contents | pages [2] -->
4 Model Preparation ........................................................................................... 6

<!-- b000039 | contents | pages [2] -->
4.1 Data Overview ................................................................................................................. 6

<!-- b000040 | contents | pages [2] -->
4.2 Conversion from longitude and latitude to distance ........................................................ 7

<!-- b000041 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000042 | contents | pages [2] -->
4.3 Description of the two drones .......................................................................................... 8

<!-- b000043 | contents | pages [2] -->
5 Rasterized Multi-Objective Optimization Model ......................................... 8

<!-- b000044 | contents | pages [2] -->
5.1 Rasterization of Regions .................................................................................................. 8

<!-- b000045 | contents | pages [2] -->
5.2 Wildfire Frequency-Distance Weighted Model ............................................................... 9

<!-- b000046 | contents | pages [2] -->
5.3 Multi-objective Optimization Model ............................................................................. 11

<!-- b000047 | contents | pages [2] -->
5.4 Results and Analysis ...................................................................................................... 12

<!-- b000048 | contents | pages [2] -->
6 Model Verification Simulated by Poisson Process ...................................... 13

<!-- b000049 | contents | pages [2] -->
6.1 Poisson Process of Extreme Fire Events ........................................................................ 13

<!-- b000050 | contents | pages [2] -->
6.2 Model Verification and Analysis .................................................................................... 15

<!-- b000051 | contents | pages [2] -->
7 Hovering Model Based on Tabu Search ....................................................... 17

<!-- b000052 | contents | pages [2] -->
7.1 Model construction of mountains and urban areas ........................................................ 17

<!-- b000053 | contents | pages [2] -->
7.2 Simulation Results ......................................................................................................... 18

<!-- b000054 | contents | pages [2] -->
8 Sensitivity and Robustness Analysis ............................................................. 19

<!-- b000055 | contents | pages [2] -->
8.1 Sensitivity Analysis ........................................................................................................ 19

<!-- b000056 | contents | pages [2] -->
8.2 Sensitivity Analysis ........................................................................................................ 20

<!-- b000057 | contents | pages [2] -->
9 Evaluation of Strengths and Weaknesses .................................................... 21

<!-- b000058 | contents | pages [2] -->
9.1 Strengths ........................................................................................................................ 21

<!-- b000059 | contents | pages [2] -->
9.2 Weaknesses and Further Improvements ......................................................................... 21

<!-- b000060 | contents | pages [2] -->
Budget Request .................................................................................................. 22

<!-- b000061 | contents | pages [2] -->
References .......................................................................................................... 24

<!-- b000062 | contents | pages [2] -->
Appendices ......................................................................................................... 25

<!-- b000063 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000064 | contents | pages [2] -->
关注数学模型

<!-- b000065 | furniture | pages [2] -->
2

<!-- b000066 | furniture | pages [2] -->
MATHmodels

<!-- b000067 | furniture | pages [2] -->
获取更多资讯

<!-- b000068 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000069 | furniture | pages [3] -->
Team # 2102199                                                                            Page 3 of 25

<!-- b000070 | heading | pages [3] -->
1 Introduction

<!-- b000071 | heading | pages [3] -->
1.1 Problem Background

<!-- b000072 | prose | pages [3] -->
微信公众号：数学模型 "Just like you, I was pain and fear when the fire destroyed the land and everything : life, houses, animals and trees. But for us aborigines, what the fire burns down is our memories, our holy land, and all the things that define our identity. " said by an aborigine. In recent years, the scale of fires in Australia has become larger and larger, causing huge economic and cultural losses. With the climate warming, the probability of fire is also greatly increased, so that it cannot be ignored anymore. We can see the fire situation in Australia from the figure below:

<!-- b000073 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000074 | caption | pages [3] -->
Figure 1: Fire Situation in Australia (Feb 2020 - Feb 2021)

<!-- b000075 | prose | pages [3] -->
The data above comes from the website GLOBAL FOREST WHATCH[1], The GFW Fires interactive map includes near real-time fire alerts from NASA and NOAA, real-time wind direction and air quality data, maps of concessions and forest cover, high-resolution satellite images, and geo-tagged social media conversations about where fires occur.

<!-- b000076 | prose | pages [3] -->
As can be seen above: In Australia, the peak fire season typically begins in early Janu- ary and lasts 45 weeks. There were 636,731 VIIRS fire alerts reported between Febru- ary 2020 and February 2021. In response to the situation above, establishing a mathematical model driven by a swarm of drones to quickly deal with forest fires is very necessary and urgent.

<!-- b000077 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000078 | prose | pages [3] -->
Wildfire is a serious natural disaster with many complexities. Through in-depth analysis and research on the background of the problem, combined with the specific constraints given, the restate of the problem can be expressed as follows:

<!-- b000079 | prose | pages [3] -->
 Build a mathematical model to determine the optimal number and combination of SSA drones and Radio Repeater drones. The model should balance several factors.

<!-- b000080 | prose | pages [3] -->
 Based on the model, explain how it adapts to the changing possibilities of extreme fire events in the next ten years.

<!-- b000081 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000082 | prose | pages [3, 4] -->
关注数学模型  Optimize the position of hovering VHF/UHF radio repeater drones based on an im- proved model for fires of different sizes on different terrains.

<!-- b000083 | furniture | pages [3] -->
2

<!-- b000084 | furniture | pages [3] -->
MATHmodels

<!-- b000085 | furniture | pages [3] -->
获取更多资讯

<!-- b000086 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000087 | furniture | pages [4] -->
Team # 2102199                                                                            Page 4 of 25

<!-- b000089 | prose | pages [4] -->
 Considering the results obtained above, prepare one to two pages of annotated budget request and submit to the Victorian Government. 微信公众号：数学模型

<!-- b000090 | heading | pages [4] -->
1.3 Literature Review

<!-- b000091 | prose | pages [4] -->
This question is mainly about mobilizing cluster drones to extinguish wildfires. In recent years, research on optimization algorithms for UAV(drone) cluster path planning is very hot, Generally, it can be divided into two parts, the Swarms of UAVs’ Path Planning Model and the Swarms of UAVs’ Path Planning Optimization Algorithm, this section mainly discusses the models that have been proposed.

<!-- b000092 | prose | pages [4] -->
 First of all, in terms of the dimensionality of the space: In[2] HU et al. sets the planning space to three dimensions. However, in order to simplify the model, more authors tend to 微信号：MATHmodels consider the space as two dimensions[3].

<!-- b000093 | prose | pages [4] -->
 Secondly, in terms of the method of planning space: the commonly used methods include Grid Method[4], Road Sign Method, and Artificial Potential Fields Method.

<!-- b000094 | prose | pages [4] -->
 Finally, the objective function of the UAV Cluster Path Planning Model generally uses flight distance, threat cost, etc. For example, Xu et al. [5] takes the weighted sum of threat cost and time cost as the optimization target. What’s more, Constraints often include self- constraints and environmental constraints, such as flight speed and geographic altitude.

<!-- b000095 | prose | pages [4] -->
 The strengths and weaknesses of the planning space can be visually presented and is shown below:

<!-- b000096 | caption | pages [4] -->
Figure 2: Literature Review Framework

<!-- b000097 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000098 | prose | pages [4] -->
关注数学模型

<!-- b000099 | furniture | pages [4] -->
2

<!-- b000100 | furniture | pages [4] -->
MATHmodels

<!-- b000101 | furniture | pages [4] -->
获取更多资讯

<!-- b000102 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000103 | furniture | pages [5] -->
Team # 2102199                                                                            Page 5 of 25

<!-- b000104 | heading | pages [5] -->
1.4 Our Work

<!-- b000105 | prose | pages [5] -->
The problem requires us to fight fires by optimizing the locations of two type of drones. Our work mainly includes the following:

<!-- b000106 | prose | pages [5] -->
微信公众号：数学模型 1) Based on the data of wildfires, a rasterized Multi-Objective Optimization Model is established;

<!-- b000107 | prose | pages [5] -->
2) The mixture of the two drones is given and the extreme fire events is considered;

<!-- b000108 | prose | pages [5] -->
3) Based on the verification model simulated by Poisson process and the hovering model based on Tabu Search, this article effectively demonstrates the validity and applica- bility.

<!-- b000109 | prose | pages [5] -->
In order to avoid complicated description, intuitively reflect our work process, the flow chart is shown in Figure 3:

<!-- b000110 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000111 | caption | pages [5] -->
Figure 3: Flow Chart of Our Work

<!-- b000112 | heading | pages [5] -->
2 Assumptions and Explanations

<!-- b000113 | prose | pages [5] -->
Considering that practical problems always contain many complex factors, first of all, we need to make reasonable assumptions to simplify the model, and each hypothesis is closely followed by its corresponding explanation:

<!-- b000114 | prose | pages [5] -->
 Assumption 1: Only the influence of terrain on the drone is considered, and other factors such as temperature, humidity, and atmosphere are ignored.

<!-- b000115 | prose | pages [5] -->
Explanation: The UAV's radiation communication range is only affected by terrain fac- tors, and other factors are minimal. In fact, these factors affect each other, but in order to simplify the model ,we ignore the interactions between these factors.  Assumption 2: The location of the EOC can be deployed around the fire due to an emergency.

<!-- b000116 | prose | pages [5] -->
Explanation: The position of the EOC is not clearly given in the question. So, we assume that EOC can be set in a fire-free area around the wildfire site, since the glossary of the problem said that mobile EOC can be deployed near the site of an emergency.

<!-- b000117 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000118 | prose | pages [5, 6] -->
关注数学模型 

<!-- b000119 | furniture | pages [5] -->
2

<!-- b000120 | furniture | pages [5] -->
MATHmodels

<!-- b000121 | furniture | pages [5] -->
获取更多资讯

<!-- b000122 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000123 | furniture | pages [6] -->
Team # 2102199                                                                            Page 6 of 25

<!-- b000125 | heading | pages [6] -->
Assumption 3: The "boots-on-the-ground" forward teams can be approximated as

<!-- b000126 | prose | pages [6] -->
near the fire site.

<!-- b000127 | prose | pages [6] -->
Explanation: The actual movement of the team is very complicated, and it is difficult to accurately calculate its position. Therefore, it is assumed that the squad is near the fire 微信公众号：数学模型 field and the drone arrives at the fire field to establish a connection with the squad.  Assumption 4: The collected data can be considered reliable and can reflect the changing laws of the Victorian wildfire.

<!-- b000128 | prose | pages [6] -->
Explanation: The historical Victorian wildfire data, latitude, longitude and other data come from authoritative websites, such as the official website of FEC in Australia and NASA, with high accuracy.

<!-- b000129 | prose | pages [6] -->
Additional assumptions are made to simplify analysis for individual sections. These as- sumptions will be discussed at the appropriate locations.

<!-- b000130 | heading | pages [6] -->
3 Notations

<!-- b000131 | prose | pages [6] -->
微信号：MATHmodels Some important mathematical notations used in this paper are listed in Table 1.

<!-- b000132 | caption | pages [6] -->
Table 1: Notations used in this paper

<!-- b000133 | heading | pages [6] -->
Symbol

<!-- b000134 | prose | pages [6] -->
Description Longitude within the i-th Wildfire Grid Latitude within the i-th Wildfire Grid The area of the i-th grid the distance between the -th roaming grid and the -th grid

<!-- b000135 | prose | pages [6] -->
Score for evaluating the -th wildfire grid

<!-- b000136 | prose | pages [6] -->
the drone sent by the k-th EOC to the i-th wildfire grid the drone sent by the k-th EOC to the i-th wildfire grid The flight time of drones Note: There are some variables that are not listed here and will be discussed in detail in each section.

<!-- b000137 | heading | pages [6] -->
4 Model Preparation

<!-- b000138 | heading | pages [6] -->
4.1 Data Overview

<!-- b000139 | prose | pages [6] -->
The question did not provide us with data directly, so we need to consider which data to collect in the model building. Through the analysis of the problem, we need to collect the rel- evant information of Victoria, Australia, such as latitude and longitude, altitude, number of wildfires and so on. Due to the large amount of data, it is not convenient to list them all, so visualizing the data for display is a good method.

<!-- b000140 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000141 | prose | pages [6] -->
关注数学模型

<!-- b000142 | furniture | pages [6] -->
2

<!-- b000143 | furniture | pages [6] -->
MATHmodels

<!-- b000144 | furniture | pages [6] -->
获取更多资讯

<!-- b000145 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000146 | furniture | pages [7] -->
Team # 2102199                                                                            Page 7 of 25

<!-- b000147 | heading | pages [7] -->
4.1.1 Data Collection

<!-- b000148 | prose | pages [7] -->
The official website of FEC in Victoria, Australia was queried and lots of data about wild- fires were obtained. And other data sources are shown in Table 2.

<!-- b000149 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000150 | caption | pages [7] -->
Table 2: Data and Database Websites

<!-- b000151 | prose | pages [7] -->
Database Names Database Websites

<!-- b000152 | prose | pages [7] -->
Fire Alerts https://www.globalforestwatch.org/map/

<!-- b000153 | prose | pages [7] -->
Altitude https://search.earthdata.nasa.gov/search https://www.kaggle.com/carlosparadis/fires- Latitude and Longitude from-space-australia-and-new-zeland/data Google Scholar https://scholar.google.com/

<!-- b000154 | prose | pages [7] -->
Maps © 2021 Mapbox © OpenStreetMap

<!-- b000155 | heading | pages [7] -->
4.1.2 Data Screening

<!-- b000156 | prose | pages [7] -->
微信号：MATHmodels Judging from the map of Victoria in Figure 4 (right), the eastern region is mainly forest, while the western region is almost no forest. Furthermore, to demonstrate better the situation of wildfires, we plot over a heat map in Figure 4 (left).

<!-- b000157 | prose | pages [7] -->
Considering the heat map we made, it shows the number of wildfires in various states of Victoria from 2012 to 2021, the darker the color, the greater number of fires. Although fires have also occurred in the western region, the number of eastern regions is much higher than that in the western region.

<!-- b000158 | caption | pages [7] -->
Figure 4: Data Screening

<!-- b000159 | prose | pages [7] -->
Through the heat map above, when building the model, a reasonable choice of the size of the area can be made, because the main problem needs to be solved is the emergency treatment of wildfires, so we take the eastern part as the model building area. Bendigo Airport (36.7346S,144.3305E) has been chosen as the boundary of the division, using this longitude as the basis for division, and keep the eastern part, especially taking Southeast Coastal Area into consideration.

<!-- b000160 | heading | pages [7] -->
4.2 Conversion from longitude and latitude to distance

<!-- b000161 | prose | pages [7] -->
Haversine formula can determine the distance between the two places. It can well reflect the influence of the curvature of the earth and is a common way to determine the distance

<!-- b000162 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000163 | prose | pages [7, 8] -->
关注数学模型 between the two places with given latitude and longitude in geography[6], seen in the equa- tion(1):

<!-- b000164 | furniture | pages [7] -->
2

<!-- b000165 | furniture | pages [7] -->
MATHmodels

<!-- b000166 | furniture | pages [7] -->
获取更多资讯

<!-- b000167 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000168 | furniture | pages [8] -->
Team # 2102199                                                                            Page 8 of 25

<!-- b000170 | prose | pages [8] -->
(1) 微信公众号：数学模型 Where R represents the radius of the earth, and indicates the latitude of the two places, and express the longitude of them, d is the distance between the them.

<!-- b000171 | heading | pages [8] -->
4.3 Description of the two drones

<!-- b000172 | prose | pages [8] -->
Although the two types of drones have different names, they all use the same drone, but they have different equipment and functions. The following part refers to Radio Repeater drones as RR drones. A brief schematic diagram is shown in Figure 5:

<!-- b000173 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000174 | caption | pages [8] -->
Figure 5: Two Types of Drones

<!-- b000175 | heading | pages [8] -->
5 Rasterized Multi-Objective Optimization Model

<!-- b000176 | heading | pages [8] -->
5.1 Rasterization of Regions

<!-- b000177 | prose | pages [8] -->
The work of the predecessors has given us some inspiration. For this problem, we should first determine its spatial model[7]. The purpose is to use a mathematical model to express the actual physical environment, which is convenient for computer processing. According to the survey results in the literature review, this article uses grid method to tackle the problem.

<!-- b000178 | prose | pages [8] -->
Therefore, the grid label N of any point can be expressed as:

<!-- b000179 | prose | pages [8] -->
(2)

<!-- b000180 | prose | pages [8] -->
where is the coordinate of a potential place, the abscissa represents the longi-

<!-- b000181 | prose | pages [8] -->
tude and the ordinate represents the latitude, is the grid size, , is the

<!-- b000182 | prose | pages [8] -->
maximum length of the horizontal axis.

<!-- b000183 | prose | pages [8] -->
Further, the coordinates of the grid center position can be obtained:

<!-- b000184 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000185 | prose | pages [8, 9] -->
关注数学模型 (3)

<!-- b000186 | furniture | pages [8] -->
2

<!-- b000187 | furniture | pages [8] -->
MATHmodels

<!-- b000188 | furniture | pages [8] -->
获取更多资讯

<!-- b000189 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000190 | furniture | pages [9] -->
Team # 2102199                                                                            Page 9 of 25

<!-- b000192 | prose | pages [9] -->
微信公众号：数学模型 The grid is divided into three types, Barrier Grid, Roaming Grid and Wildfire Grid, the specific introduction is as follows:

<!-- b000193 | prose | pages [9] -->
 Barrier Grid: The grid of obstacles is used to represent the mountains in the actual map.

<!-- b000194 | prose | pages [9] -->
Because the flying height of drones is limited, it is very difficult to fly over areas with high altitude. Therefore, grids with altitude exceeding a certain limit are transformed into grids of obstacles. This grid cannot be reached by any drones.

<!-- b000195 | prose | pages [9] -->
 Roaming Grid: The roaming grid is a location for emergency mobile EOC settings, that is, in the event of a big fire, the EOC can be set up in the roaming grid.

<!-- b000196 | prose | pages [9] -->
 Wildfire Grid: As the name suggests, the grid where the wildfire occurs is called the wildfire grid, which is the place that the SSA drones will fly to.

<!-- b000197 | prose | pages [9] -->
These Grids can be easily visualized by Figure 6:

<!-- b000198 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000199 | caption | pages [9] -->
Figure 6: Three types of grids

<!-- b000200 | heading | pages [9] -->
5.2 Wildfire Frequency-Distance Weighted Model

<!-- b000201 | prose | pages [9] -->
Firstly, the map of eastern Victoria is rasterized, and the grid size is = 10km. Secondly, the frequency of forest wildfires is the key data for establishing the drone swarm model. Through the Frequency-Distance Weighted Model, we can obtain the EOCs around the wild- fires. Due to the limited pages, the paper presents the southeast area (147.2915~149.1503E, 35.8000 ~ 39.1005S) with the largest number of wildfires.

<!-- b000202 | prose | pages [9] -->
Furthermore, the results of the number of drones in this area will be given in section 5.4. Although the results are given for this area, the model is extensible and can be easily extended to all areas of Victoria. Firstly, the heat map drawn by Python after rasterization is plotted as shown in Figure 7:

<!-- b000203 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000204 | prose | pages [9, 10] -->
关注数学模型 微信公众号：数学模型

<!-- b000205 | furniture | pages [9] -->
2

<!-- b000206 | furniture | pages [9] -->
MATHmodels

<!-- b000207 | furniture | pages [9] -->
获取更多资讯

<!-- b000208 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000209 | furniture | pages [10] -->
Team # 2102199                                                                            Page 10 of 25

<!-- b000211 | caption | pages [10] -->
Figure 7: Heat map after Rasterization

<!-- b000212 | prose | pages [10] -->
The blue grid represents the roaming grid surrounding the yellow wildfire grid. There is 微信号：MATHmodels no barrier grid in this terrain, so it will temporarily not be considered here. Altitude is assumed to be the same. In practice, there is a slight difference, but it is understandable to make some simplifications.

<!-- b000213 | prose | pages [10] -->
It can be seen that after rasterization, the discrete model is a bit more convenient to solve. In Table 3, we give some of the data searching from the website:

<!-- b000214 | caption | pages [10] -->
Table 3: Latitude and longitude data of VIIRS

<!-- b000215 | prose | pages [10] -->
latitude longitude bright_ti4 scan instrument version daynight -37.5296 143.4565 344.8 0.54 VIIRS 1.0NRT D -38.0547 143.9076 329.8 0.51 VIIRS 1.0NRT D -38.0593 143.9081 339.4 0.51 VIIRS 1.0NRT D -38.0566 143.9038 336.7 0.52 VIIRS 1.0NRT D -38.0562 143.9098 327.7 0.52 VIIRS 1.0NRT D … … … … … … … Note: The longitude and latitude will be used in the data, and one occurrence represents a wildfire in the place, total amount of the data is .

<!-- b000216 | prose | pages [10] -->
Through data processing, we can get the relevant statistical data information in this area for the simulation. For the -th wildfire grid, suppose the frequency of it is , when the lon- gitude and latitude , should be increased by 1, so it can be expressed as fol- lowing:

<!-- b000217 | prose | pages [10] -->
(4) Where represents the -th row of Table 3 for traversing, , represents the number of the wildfire grid in Figure 8. Eq. (4) can get the total fire frequencies of each grid. Therefore, combined with the distance between the -th roaming grid and the -th grid, the value of quantitative index can be modified as:

<!-- b000218 | prose | pages [10] -->
(5)

<!-- b000219 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000220 | prose | pages [10, 11] -->
关注数学模型 The larger , the EOC should be more likely to set up for the -th roaming area.

<!-- b000221 | furniture | pages [10] -->
2

<!-- b000222 | furniture | pages [10] -->
MATHmodels

<!-- b000223 | furniture | pages [10] -->
获取更多资讯

<!-- b000224 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000225 | furniture | pages [11] -->
Team # 2102199                                                                            Page 11 of 25

<!-- b000227 | prose | pages [11] -->
Through Eq. (5), the descending scores of 33 roaming grids can be obtained. Since the eastern region has a large span, and the question requires rapid forest fire response, 2~3 EOCs are not enough to form a communication network in a short time. Considering the construction 微信公众号：数学模型 cost of EOC, we select the top 4 EOCs.

<!-- b000228 | prose | pages [11] -->
Furthermore, the EOC distribution obtained by this sorting alone is relatively concentrated, and the balance is not considered, so the following algorithm is used to improve it. This algo- rithm can be viewed in the flowchart in Figure 8:

<!-- b000229 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000230 | caption | pages [11] -->
Figure 8: Algorithm to select EOCs

<!-- b000231 | prose | pages [11] -->
Using this method, the best EOCs can be found more reasonable and accurate, the results would be given in 5.4.

<!-- b000232 | heading | pages [11] -->
5.3 Multi-objective Optimization Model

<!-- b000233 | prose | pages [11] -->
The Multi-objective Optimization Model is an model that uses mathematical program- ming methods to determine the optimal solution. In this question, it is under the established goals (such as minimum cost and shortest distance) and given constraints (such as flight time and radiation range) , determine how to effectively deal with drone’s resources and solve the problem of the best combination of SSA drones and RR drones.

<!-- b000234 | prose | pages [11] -->
 Decision Variable The labels of the SSA drones and RR drones are and , represents the drone sent by the k-th EOC to the i-th wildfire grid. Similarly, represents the that was dispatched by the k-th EOC to the i-th wildfire grid; both of them can only be 0 and 1, which is ;

<!-- b000235 | prose | pages [11] -->
 Objective Function The two goals can be attributed to the smallest number of drones and the shortest time.

<!-- b000236 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000237 | prose | pages [11, 12] -->
关注数学模型 The mission scenario is to put out a bushfire quickly. Therefore, the requirement of drone exe- cution efficiency is very high, so one optimization goal should be set as the minimum time to complete the Rapid Bushfire Response; and the completion time can be expressed by minimiz- ing the maximum flight distance of each drone, so the first objective function is: 微信公众号：数学模型 (6)

<!-- b000238 | furniture | pages [11] -->
2

<!-- b000239 | furniture | pages [11] -->
MATHmodels

<!-- b000240 | furniture | pages [11] -->
获取更多资讯

<!-- b000241 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000242 | furniture | pages [12] -->
Team # 2102199                                                                            Page 12 of 25

<!-- b000244 | prose | pages [12] -->
are the roaming grids that selected by simulation. It will be shown in section 5.4. Eq.(6) reflects that the minimization of the maximum firefighting distance of the k-th EOC can be presented by the sum of the two types of drone's dispatch label and its corresponding distance.

<!-- b000245 | prose | pages [12] -->
The other goal is to minimize the number of drones deployed, since and can only be 0 and 1, so the sum of them is the total number of drones:

<!-- b000246 | prose | pages [12] -->
(7)

<!-- b000247 | prose | pages [12] -->
There are two common methods to deal with multi-objective optimization, i.e. staged op- timization and weighted optimization. Considering the time cost, the weighted method has been 微信号：MATHmodels chosen to deal with the problem. Therefore, from (6),(7), we have Eq.(8):

<!-- b000248 | prose | pages [12] -->
(8)

<!-- b000249 | prose | pages [12] -->
Where , the parameter will be optimized by simulation, of course, their order of magnitude should have been taken into consideration. reflects the proportion of drones that need to be added when a extreme fire events comes, normally, .

<!-- b000250 | prose | pages [12] -->
 Constraints The time constraint requires that the working time of drones should not exceed its working time after charging once. Subject to the constraint by (9):

<!-- b000251 | prose | pages [12] -->
(9)

<!-- b000252 | prose | pages [12] -->
Where, and are flight time and hover time, respectively. refers to the speed of the drones, . If the drone is about to run out of power, it needs to be returned to the EOC for charging. Assuming that when the drone at a certain location needs to return, there will be a drone from EOC to take over. The distance constraints can be expressed as:

<!-- b000253 | prose | pages [12] -->
(10)

<!-- b000254 | prose | pages [12] -->
There are also other constraints, for example, in view of the terrain, the altitude restriction et al. should be added. However, due to the limited pages, there is no way to give them all in the article; the simulation results will be directly given in the next section.

<!-- b000255 | heading | pages [12] -->
5.4 Results and Analysis

<!-- b000256 | prose | pages [12] -->
We use Python for simulation, the intermediate process is a bit complicated and will not be redundantly given in this part; the results of the region are displayed directly as Figure 9:

<!-- b000257 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000258 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型

<!-- b000259 | furniture | pages [12] -->
2

<!-- b000260 | furniture | pages [12] -->
MATHmodels

<!-- b000261 | furniture | pages [12] -->
获取更多资讯

<!-- b000262 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000263 | furniture | pages [13] -->
Team # 2102199                                                                            Page 13 of 25

<!-- b000265 | caption | pages [13] -->
Figure 9:The results of Problem1

<!-- b000266 | prose | pages [13] -->
微信号：MATHmodels The Figure 9 shows the number of EOCs, RR drones and SSA drones under the condition that the farthest distance each EOC could manage, which means that the reflects the maximum number of drones dispatched when rapid response is required in the event of a wildfire in the area. This can be used as the total number of drones in the area.

<!-- b000267 | prose | pages [13] -->
The range in the red circle indicates the area that can be covered by drones. By analyzing the above figure, we can find: Most of the fire area can be effectively covered, and this is the path planning for the worst case of the fire location. When the fire is closer to the EOC, fewer drones can be used to complete the task. A total of 4 SSA drones and 4 RR drones were dis- patched throughout the region. The ratio of the two types of drones is close to 1:1. Consid- ering the time required for charging, a total of 8 SSA drones and 8 repeater drones are re- quired in the area .

<!-- b000268 | heading | pages [13] -->
6 Model Verification Simulated by Poisson Process

<!-- b000269 | heading | pages [13] -->
6.1 Poisson Process of Extreme Fire Events

<!-- b000270 | prose | pages [13] -->
The possibility of extreme fire events in the next decade can be predicted by the occur- rence of such events in the past few decades. Detailed data on extreme fire incidents in Australia in previous years were found on website[8].

<!-- b000271 | prose | pages [13] -->
In [9], the author presents a general statistical methodology for the prediction of forest fires in the context of Poisson models. The article has inspired us for model building.

<!-- b000272 | prose | pages [13] -->
Poisson distribution is a discrete probability distribution commonly seen in statistics and probability. Therefore, we use the Poisson distribution model to predict the number of extreme fire events in the next ten years:

<!-- b000273 | prose | pages [13] -->
(11)

<!-- b000274 | prose | pages [13] -->
represents the average occurrence rate of extreme fire incidents per unit time (here set

<!-- b000275 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000276 | prose | pages [13, 14] -->
关注数学模型 to 10 years), that is, fire incidents frequency; N(t) represents the number of occurrences of the event within t, n and N(t) share the same meaning; e is natural constant.

<!-- b000277 | furniture | pages [13] -->
2

<!-- b000278 | furniture | pages [13] -->
MATHmodels

<!-- b000279 | furniture | pages [13] -->
获取更多资讯

<!-- b000280 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000281 | furniture | pages [14] -->
Team # 2102199                                                                            Page 14 of 25

<!-- b000283 | prose | pages [14] -->
According to the obtained sets of extreme fire incidents data, we can obtain the ex- pression of : 微信公众号：数学模型 (12)

<!-- b000284 | prose | pages [14] -->
Put it into Eq.(11) and use the idea of traversal to find the probability distribution of n from 1 to 10.

<!-- b000285 | prose | pages [14] -->
Because there is no function to directly calculate the Poisson distribution in Python, we design our own algorithm to calculate the probability density distribution. The pseudocode is as follows:

<!-- b000286 | heading | pages [14] -->
Algorithm : Probability distribution of extreme fire events

<!-- b000287 | prose | pages [14] -->
Input:

<!-- b000288 | prose | pages [14] -->
Output: 微信号：MATHmodels for to do According to , the parameter of Poisson distribution can be calculated Randomly select an integer from the aggregate The probability of in the entire dataset can be predicted based on the Poisson distribution Then the probability is recorded as end Draw the probability density distribution of extreme fire events

<!-- b000289 | prose | pages [14] -->
Through simulation, the probability density distribution is shown in Figure 10:

<!-- b000290 | caption | pages [14] -->
Figure 10: The Probability Density Distribution of Extreme Fire Events

<!-- b000291 | prose | pages [14] -->
It can be seen from Figure 10 that the position with the highest probability density is roughly between 2 and 4, and the average number of occurrences can be accurately calculated by the mathematical expectation in the above figure.

<!-- b000292 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000293 | prose | pages [14, 15] -->
关注数学模型 Mathematical expectations, also written as mean, can represent the number of extreme

<!-- b000294 | furniture | pages [14] -->
2

<!-- b000295 | furniture | pages [14] -->
MATHmodels

<!-- b000296 | furniture | pages [14] -->
获取更多资讯

<!-- b000297 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000298 | furniture | pages [15] -->
Team # 2102199                                                                            Page 15 of 25

<!-- b000300 | prose | pages [15] -->
fires that may occur in Victoria in the next 10 years. It is recorded as , and its expression is

<!-- b000301 | prose | pages [15] -->
as follows: 微信公众号：数学模型 (13)

<!-- b000302 | prose | pages [15] -->
Substituting relevant variables into Eq. (13), the result is 2.99431, To simplify the problem, take . reflects the proportion of drones that need to be added when an extreme fire events come in Eq. (8). After substituting the influence factor into the Multi-objective Op- timization Model, via simulation, the result will be shown in section 6.2.

<!-- b000303 | heading | pages [15] -->
6.2 Model Verification and Analysis

<!-- b000304 | prose | pages [15] -->
Substituting the parameters into the model we have established in 5.3, we can simulate the new drone path and the result of the assigned quantity. Considering that the occurrence of 微信号：MATHmodels extreme fires is mainly manifested as an increase in the area of overfire, we will give simulation results under 1 to 10 times size of the unit area (unit area means area in the 5.3 model).

<!-- b000305 | prose | pages [15] -->
Cubic Spline Interpolation can be used to smooth the curve. It is defined as follows:

<!-- b000306 | prose | pages [15] -->
For the interval , , these n+1 nodes and the function values at these points , is the dependent var- iable we need to study. if the function satisfies three conditions, then is the cubic spline interpolation function of with respect to n nodes.

<!-- b000307 | prose | pages [15] -->
The biggest advantage of using it is when the density of interpolation nodes gradually increases, the cubic spline interpolation function converges not only to the function itself and its derivative, but also to the derivative of the function, which is better than polynomial inter- polation.

<!-- b000308 | prose | pages [15] -->
Due to the large number of path diagrams obtained but limited pages, what we need to focus on is how to verify the rationality and analysis of the model; so we directly give the curves with the area of the wildfire as follows:  From the perspective of quantity

<!-- b000309 | prose | pages [15] -->
60

<!-- b000310 | prose | pages [15] -->
50 Number of two drones 40

<!-- b000311 | prose | pages [15] -->
30

<!-- b000312 | prose | pages [15] -->
20

<!-- b000313 | prose | pages [15] -->
10 RR SSA 0 1 2 3 4 5 6 7 8 9 10 S/times of unit area

<!-- b000314 | caption | pages [15] -->
Figure 11 Number of the two drones

<!-- b000315 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000316 | prose | pages [15, 16] -->
关注数学模型 1.In terms of the number of the two kinds of drones, when the fire area begins to increase, the number of RR drones grows faster. Probably because with the expansion of the fire area, more repeaters are needed to communicate to establish the connection between the front team and EOC. 微信公众号：数学模型 2.However, when the fire area exceeds equal to or even greater than 9 times, the number of SSA drones exceeds that of RR drones, and the growth rate is increasing. The number of RR drones is almost unchanged. Through the observation and inference of the path, we guess that it may be because the fire area is too large and more SSAs are required for detailed detection. Since one RR drone can communicate with multiple SSA drones, after the fire area increases to a certain degree, the area has been fully covered by RR drones, so basically only SSA drones continue to grow.

<!-- b000317 | furniture | pages [15] -->
2

<!-- b000318 | furniture | pages [15] -->
MATHmodels

<!-- b000319 | furniture | pages [15] -->
获取更多资讯

<!-- b000320 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000321 | furniture | pages [16] -->
Team # 2102199                                                                            Page 16 of 25

<!-- b000323 | prose | pages [16] -->
 From the perspective of time and ratio

<!-- b000324 | prose | pages [16] -->
微信号：MATHmodels time to cover all area Ratio of RR to SSA

<!-- b000325 | caption | pages [16] -->
Figure 12:Time to Cover and Ratio of RR to SSA

<!-- b000326 | prose | pages [16] -->
From Figure12 (left), it can be seen that:

<!-- b000327 | prose | pages [16] -->
1. At the beginning, the time to cover the fire area rose rapidly, exceeding 1.2 times compared with the original time.

<!-- b000328 | prose | pages [16] -->
2. However, when the burned area is increased from 3 times to 4 times, the time to deploy drones decreases briefly. This may be because the geometric distribution of drones under this area can be optimized for a shorter time.

<!-- b000329 | prose | pages [16] -->
3. When increasing from 4 times to 8 times, the coverage time of drones only slowly increases, reaching a state of equilibrium with the overfire area.

<!-- b000330 | prose | pages [16] -->
4. Continue to increase the burned area, the coverage time is growing rapidly. We suspect that the out of control has led to an increase in the number of SSA drones and a longer deployment time.

<!-- b000331 | prose | pages [16] -->
From Figure12 (right), it can be seen that:

<!-- b000332 | prose | pages [16] -->
The ratio of the two drones changes with the burned area. The ratio curve first rises and then falls. This provides a good basis for CFA to provide the ratio of two kinds of drones. After judging the fire area observed by satellite, when the number of two kinds of drones is equipped, the optimal effect can be obtained by following the ratio.

<!-- b000333 | prose | pages [16] -->
Of course, our model is not perfect, and more factors can be considered to make the anal- ysis more accurate. However, within the allowable range of error, we can draw the conclusion

<!-- b000334 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000335 | prose | pages [16, 17] -->
关注数学模型 that:

<!-- b000336 | furniture | pages [16] -->
2

<!-- b000337 | furniture | pages [16] -->
MATHmodels

<!-- b000338 | furniture | pages [16] -->
获取更多资讯

<!-- b000339 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000340 | furniture | pages [17] -->
Team # 2102199                                                                            Page 17 of 25

<!-- b000342 | prose | pages [17] -->
1. The cost of RR drones will increase compared to SSA drones under the premise when the burned area does not increase much;

<!-- b000343 | heading | pages [17] -->
2. When the burned area exceeds a certain limit, SSA drones’ costs will highly increase.

<!-- b000344 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000345 | heading | pages [17] -->
7 Hovering Model Based on Tabu Search

<!-- b000346 | prose | pages [17] -->
Since the first question has already discussed the hovering situation and distribution of drones in plain areas, the plain terrain of eastern Victoria will not be discussed in this model. We will focus on mountain areas and urban areas.

<!-- b000347 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000348 | caption | pages [17] -->
Figure 13:Altitudinal Map of Victoria[10]

<!-- b000349 | prose | pages [17] -->
There are some additional assumptions to simplify analysis for the question.

<!-- b000350 | prose | pages [17] -->
 Hypothesis 1: Since the signal attenuation rate of the radio in the city is 50%, we also consider the signal attenuation rate of the repeater to be 50%.

<!-- b000351 | prose | pages [17] -->
 Hypothesis 2: In mountainous terrain, due to the complex terrain, the signal of the repeater will drop as the flying height of the drone rises. We assume that it is a linear relationship.

<!-- b000352 | prose | pages [17] -->
 Hypothesis 3: According to the information obtained on the Internet[11], the maxi- mum flight altitude of the drone does not have the ability to directly cross mountain peaks. We assume that its maximum flight altitude threshold is 800m.

<!-- b000353 | prose | pages [17] -->
Considering the page constraint, the article can not discuss all the cities and mountains in eastern Victoria. We focus on selecting the mountains and the famous city Melbourne in the diagram given by the problem to construct and optimize the model. Due to the altitude limita- tion of drones, we will deploy EOCs on the north and south sides of the mountains, and their drones will not bypass the mountains for relay and detection missions.

<!-- b000354 | heading | pages [17] -->
7.1 Model construction of mountains and urban areas

<!-- b000355 | prose | pages [17] -->
For the optimization of the hovering position of RR drones, Tabu Search(TS) is undoubt- edly a suitable algorithm. We still follow the grid method in question 1, set the grids with boundary intersection lines as mutual neighborhoods, that is, for any grid , the neighborhood grid can be understood as the neighborhood mapping on .Determine the four neighborhoods

<!-- b000356 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000357 | prose | pages [17, 18] -->
关注数学模型 as . the expression is:

<!-- b000358 | furniture | pages [17] -->
2

<!-- b000359 | furniture | pages [17] -->
MATHmodels

<!-- b000360 | furniture | pages [17] -->
获取更多资讯

<!-- b000361 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000362 | furniture | pages [18] -->
Team # 2102199                                                                            Page 18 of 25

<!-- b000364 | prose | pages [18] -->
(14)

<!-- b000365 | prose | pages [18] -->
For the optimal hovering position of the repeater drone, considering economic factors and 微信公众号：数学模型 efficiency, the grid that is closest to the line between the grid where is located and the grid which the fire source is located in can be considered to have the highest temporary evaluation value. Put it into the candidate set. By analogy, we can integrate a temporarily considered op- timal path, and calculate the cost of .

<!-- b000366 | prose | pages [18] -->
Since this process completely follows the principle of local optimality, over-fitting may occur. We go back to the root node , and at the same time list that has just been selected as a taboo object, and put it in the taboo table and have a discussion. Select an element in the remaining neighborhood to enter the candidate set, repeat the above algorithm again, and cal- culate the cost .

<!-- b000367 | prose | pages [18] -->
We define that grid is needed to walk from to a certain grid, and set it as the -th neighborhood map on . When the first level of neighborhood mapping is completely trav- 微信号：MATHmodels ersed, we find that over-fitting will also occur from the second level of mapping.

<!-- b000368 | prose | pages [18] -->
At this time, we will amnesty all the elements in the taboo table and use the same method to treat the next few levels of neighbors. The domain is traversed layer by layer, and under different paths is calculated separately and put into the taboo table. Finally, through the com- parison, the path with the smallest value is determined.

<!-- b000369 | prose | pages [18] -->
After that, let us consider the attenuation of repeater and radio signals as the altitude in- creases, which conforms to the following expression:

<!-- b000370 | prose | pages [18] -->
(15)

<!-- b000371 | prose | pages [18] -->
Where is the distance that the radio can emit after attenuation, refers to the distance that the radio can emit before attenuation, represents the attenuation coefficient, and is the altitude.

<!-- b000372 | prose | pages [18] -->
Compared with cities, there is no interference from other electromagnetic waves in the mountains, so its attenuation coefficient is smaller than that in cities. After consulting the data, we have calculated that it is between 0.4 and 0.45. We set it to 0.4 for easy calculation.

<!-- b000373 | heading | pages [18] -->
7.2 Simulation Results

<!-- b000374 | prose | pages [18] -->
Based on the above, the distribution position of the RR drones can be basically determined. Affected by space, all calculation results will not be released here, the optimal results will be displayed through the following visual drawing:

<!-- b000375 | caption | pages [18] -->
Figure 14: Mountain Areas

<!-- b000376 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000377 | prose | pages [18, 19] -->
关注数学模型  The yellow area in the left picture shows the coverage of the RR drones, it shows that the results obtained by using TS algorithm can well cover the mountainous area.

<!-- b000378 | furniture | pages [18] -->
2

<!-- b000379 | furniture | pages [18] -->
MATHmodels

<!-- b000380 | furniture | pages [18] -->
获取更多资讯

<!-- b000381 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000382 | furniture | pages [19] -->
Team # 2102199                                                                            Page 19 of 25

<!-- b000384 | prose | pages [19] -->
 The figure on the right shows the movement path of the RR drones. It can be seen from 微信公众号：数学模型 the figure that such a planning scheme can use fewer repeater drones to achieve full cov- erage of the mountains. From the side, the method we use is fast and effective.

<!-- b000385 | prose | pages [19] -->
 The network also takes into account the time cost. Therefore, when constructing the net- work, the maximum number of layers is 3. If setting fewer EOCs, the number of layers of the network will be too many, and the time to deploy drones will increase significantly.

<!-- b000386 | prose | pages [19] -->
We are supposed to meet the requirements for rapid emergency response.

<!-- b000387 | prose | pages [19] -->
Similarly, the construction of the urban area model uses the same tabu search algorithm as the mountain model to find the most economical path. Only for the smaller cities around Melbourne, we also need to take into account the situation that they face sudden fires, so we set up EOCs on the surrounding of Melbourne in case of the sudden fires in Geelong and Cran- bourne. Since the title clearly states that the radio will attenuate to 2 kilometers in the city, no 微信号：MATHmodels more expressions are added here. The finally calculated hovering position of the RR drones is shown in the figure below:

<!-- b000388 | caption | pages [19] -->
Figure 15: Urban Areas

<!-- b000389 | prose | pages [19] -->
So far, our model has been established, perfected and verified. It can be seen that the optimized model can be applied to different terrains, and it takes into account economic and time costs. It is a highly usable model result.

<!-- b000390 | heading | pages [19] -->
8 Sensitivity and Robustness Analysis

<!-- b000391 | heading | pages [19] -->
8.1 Sensitivity Analysis

<!-- b000392 | prose | pages [19] -->
In section 5.3, factor is introduced to estimate the parameters of the extreme fire events. Therefore, change the size of this parameter, that is, the average number of extreme fires per decade has changed. We want to analyze the sensitivity of this parameter.

<!-- b000393 | prose | pages [19] -->
(16) The reason for the only consider increase rather than decrease of is to reflect the worst case, that is, the average number of fires per decade is more, and observe whether our model is sensitive to this parameter.

<!-- b000394 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000395 | prose | pages [19, 20] -->
关注数学模型 Therefore, Re-simulate the calculation results and obtain 4 sets of curves as shown in

<!-- b000396 | furniture | pages [19] -->
2

<!-- b000397 | furniture | pages [19] -->
MATHmodels

<!-- b000398 | furniture | pages [19] -->
获取更多资讯

<!-- b000399 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000400 | furniture | pages [20] -->
Team # 2102199                                                                            Page 20 of 25

<!-- b000402 | caption | pages [20] -->
Figure 16:

<!-- b000403 | prose | pages [20] -->
3.5 微信公众号：数学模型 3

<!-- b000404 | prose | pages [20] -->
Ratio of RR to SSA 2.5

<!-- b000405 | prose | pages [20] -->
2

<!-- b000406 | prose | pages [20] -->
1.5

<!-- b000407 | prose | pages [20] -->
1

<!-- b000408 | prose | pages [20] -->
Ratio 0.5 1 2 3 4 5 6 7 8 9 10 S/times of unit area

<!-- b000409 | caption | pages [20] -->
Figure 16: Sensitivity analysis of

<!-- b000410 | prose | pages [20] -->
It is indicated that with the increase of 5% of each step length, the number of both types of drones is on the rise. However, the growth of both did not change in the form of a curve.

<!-- b000411 | prose | pages [20] -->
Correspondingly, the ratio of the two drones that CFA needs to be equipped has also in- 微信号：MATHmodels creased, which is reasonable and can be explained. The trend of the curve obtained by sensi- tivity test is consistent with the actual situation.

<!-- b000412 | heading | pages [20] -->
8.2 Sensitivity Analysis

<!-- b000413 | prose | pages [20] -->
Furthermore, we also verified the robustness of our model. While we add 5% random disturbance to and , Its practical significance is: We hope to study whether the drones can accurately reach the destination when there is a certain deviation in the data be- tween the two places and calculate how much the required time is disturbed:

<!-- b000414 | prose | pages [20] -->
(17)

<!-- b000415 | prose | pages [20] -->
(18) We did 1000 simulations. The calculation found that 95.7% of UAVs can reach the des- tination correctly, and the degree of deviation from the original time is shown in the table:

<!-- b000416 | caption | pages [20] -->
Table 4: Degree of Deviation from The Original Time

<!-- b000417 | prose | pages [20] -->
Number Time Error Number Time Error 1 -0.9654% 6 0.2689% 2 1.5987% 7 -3.2657% 3 2.1391% 8 2.1894% 4 -1.9439% 9 UNFOUND 5 0.3823% 10 -1.2243% … … … …

<!-- b000418 | prose | pages [20] -->
We can find that the disturbance of has a certain influence on the result, but it is within an acceptable range. Therefore, when the CFA handles a fire, even if there is a slight error in the distance calculation, the task can be completed to a large extent, and the time er- ror does not exceed 5%.

<!-- b000419 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000420 | prose | pages [20] -->
关注数学模型

<!-- b000421 | furniture | pages [20] -->
2

<!-- b000422 | furniture | pages [20] -->
MATHmodels

<!-- b000423 | furniture | pages [20] -->
获取更多资讯

<!-- b000424 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000425 | furniture | pages [21] -->
Team # 2102199                                                                            Page 21 of 25

<!-- b000426 | heading | pages [21] -->
9 Evaluation of Strengths and Weaknesses

<!-- b000427 | heading | pages [21] -->
9.1 Strengths

<!-- b000428 | prose | pages [21] -->
微信公众号：数学模型 Our model offers the following strengths:

<!-- b000429 | prose | pages [21] -->
 The main strength is its enormous extensible and including all factors into a single, robust framework. For instance, the rapid deployment plan of locations of hovering VHF/UHF radio-repeater drones for fires can be applied not only to Victoria, Australia, but also to New South Wales and others by Calculating and use the algorithm presented by Figure 9;

<!-- b000430 | prose | pages [21] -->
 The Rasterized Multi-Objective Optimization Model is scientific and reasonable. More- over, the idea of rasterization is used creatively by us, and can be suitable for different practical situations. Results of extreme fire events prediction based on Poisson distribu- tion have a reliable statistical description;

<!-- b000431 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000432 | prose | pages [21] -->
 The visualization work is done very well by us, such as the framework of the research method in the literature review, the schematic diagram of the two drones in the introduc- tion, the heat map made in the fire research, and the curve of the Poisson distribution etc.

<!-- b000433 | prose | pages [21] -->
Boring data may be able to reflect the law, but not as intuitive as so many images;

<!-- b000434 | prose | pages [21] -->
 Our model effectively achieved all of the goals. It was not only fast and could handle large quantities of data, but also had the flexibility we desired. For example, compared to the basic model, the occurrence of extreme fire invents is also taken into account and have a good result;

<!-- b000435 | prose | pages [21] -->
 Effectiveness of the model can be demonstrated under different parameter of the model by sensitivity analysis. So the model can be applied to much more wildfire events.

<!-- b000436 | heading | pages [21] -->
9.2 Weaknesses and Further Improvements

<!-- b000437 | prose | pages [21] -->
Our model has the following limitations and related improvements:

<!-- b000438 | prose | pages [21] -->
 The analysis of locations of hovering VHF/UHF radio-repeater drones for fires can be more accurate if we have more complete data;

<!-- b000439 | prose | pages [21] -->
 The assumption that the "boots-on-the-ground" forward teams can be approximated as near the fire site is a bit idealized. If the trajectory of the team is taken into account, a more practical model and results can be obtained.

<!-- b000440 | prose | pages [21] -->
 Some approximate analysis methods are applied to model other places, which may lead to the situation that not to be the most optimal.

<!-- b000441 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000442 | prose | pages [21, 22] -->
关注数学模型 Budget Request

<!-- b000443 | furniture | pages [21] -->
2

<!-- b000444 | furniture | pages [21] -->
MATHmodels

<!-- b000445 | furniture | pages [21] -->
获取更多资讯

<!-- b000446 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000447 | furniture | pages [22] -->
Team # 2102199                                                                            Page 22 of 25

<!-- b000449 | prose | pages [22] -->
Dear Victoria State Government:

<!-- b000450 | prose | pages [22] -->
微信公众号：数学模型 Forest fires have always been the greatest threat to Australia. Tens of thousands of lives are lost every year in these fires. We are very worried about this situa- tion. After our investigation, we found that the eastern coastal plain of Victoria is the most frequent place for fires, which can be clearly shown from the figure on the right.

<!-- b000451 | prose | pages [22] -->
It is too dangerous for people to enter the fire scene directly. Therefore, we believe that drones should be used to detect the fire scene and ensure 微信号：MATHmodels safety before allowing people to en- (The red dots indicate the fire scene) ter. Meanwhile, we also know that drones are very expensive, so we optimize the model as much as possible to re- duce the budget. But some necessary expenses are still inevitable:

<!-- b000452 | prose | pages [22] -->
For eastern coastal plain areas, since it is the most frequent for fires, we have deployed more drones to ensure the safety. We have arranged a total of sixteen drones to face various emergencies happened in this area, which may cost around 160,000 dollars. Based on the data from the past half century, we found that there is a possibility of extreme fire events in this area. Because of this, we predicted the number of extreme fire events in the next ten years and planned corresponding countermeasures. Conservatively estimated, it may take about 970,000 dollars to deal with extreme fire events in the next ten years.

<!-- b000453 | prose | pages [22] -->
For mountain areas, due to the obstruction of terrain, drones cannot cross the mountains, so we deployed the EOCs in the north and south of the mountains to improve the efficiency of firefighting. Thus, we need much more drones to over- come various obstacles from signal and terrain. According to the calculation re- sults, about 830,000 dollars are needed to meet the above demand.

<!-- b000454 | prose | pages [22] -->
For metropolitan areas, because of the blocking of buildings and the interfer- ence of electromagnetic waves, the effect of radio signals in the city is poor. Con- sidering these, the layout of drones is more difficult. It’s more complex. After many optimizations, we finally found a better method, but it still needs 570,000 dollars as the equipment cost.

<!-- b000455 | prose | pages [22] -->
At the end, to facilitate your better reading, we show all the funds needed in the

<!-- b000456 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000457 | prose | pages [22, 23] -->
关注数学模型 following table:

<!-- b000458 | furniture | pages [22] -->
2

<!-- b000459 | furniture | pages [22] -->
MATHmodels

<!-- b000460 | furniture | pages [22] -->
获取更多资讯

<!-- b000461 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000462 | furniture | pages [23] -->
Team # 2102199                                                                            Page 23 of 25

<!-- b000464 | prose | pages [23] -->
Normal Extreme Total($) Cost Condition 微信公众号：数学模型 events($) events($)

<!-- b000465 | prose | pages [23] -->
160,000 970,000 1,130,000 Eastern coast plain

<!-- b000466 | prose | pages [23] -->
10,000 830,000 Mountains

<!-- b000467 | prose | pages [23] -->
10,000 570,000 Metropolis

<!-- b000468 | prose | pages [23] -->
From CFA in Victoria February 8, 2021 微信号：MATHmodels

<!-- b000469 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000470 | prose | pages [23] -->
关注数学模型

<!-- b000471 | furniture | pages [23] -->
2

<!-- b000472 | furniture | pages [23] -->
MATHmodels

<!-- b000473 | furniture | pages [23] -->
获取更多资讯

<!-- b000474 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000475 | furniture | pages [24] -->
Team # 2102199                                                                            Page 24 of 25

<!-- b000476 | heading | pages [24] -->
References

<!-- b000477 | references | pages [24] -->
[1]  GLOBAL FOREST WHATCH OF AUSTRALIA https://www.globalforestwatch.org/top-

<!-- b000478 | references | pages [24] -->
微信公众号：数学模型

<!-- b000479 | references | pages [24] -->
ics/fires/?topic=fires#footer

<!-- b000480 | references | pages [24] -->
[2]  HU Teng, LIU Zhanjun, LIU Yang, et al. 3D reconnaissance path planning of multiple

<!-- b000481 | references | pages [24] -->
UAVs. Journal of Systems Engineering and Electronics, 2019, 41(7): 1551 – 1559.

<!-- b000482 | references | pages [24] -->
[3]  BASBOUS B. 2D UAV path planning with radar threatening areas using simulated anneal-

<!-- b000483 | references | pages [24] -->
ing algorithm for event detection. The 2018 International Conference on Artificial Intelli-

<!-- b000484 | references | pages [24] -->
gence and Data Processing. Malatya, Turkey: IEEE, 2018: 1 – 7.

<!-- b000485 | references | pages [24] -->
[4]  WANG W F, WU Y C, ZHANG X. Research of the unit decomposing traversal method

<!-- b000486 | references | pages [24] -->
based on grid method of the mobile robot. Techniques of Automation and Applications,

<!-- b000487 | references | pages [24] -->
2013, 32(11): 34 – 38.

<!-- b000488 | references | pages [24] -->
[5]  XU Jian, ZHOU Deyun, HUANG He. Multi UAV path planning based on improved ge-

<!-- b000489 | references | pages [24] -->
netic algorithm. Aeronautical Computing Technique, 2009, 39(4): 43 – 46.

<!-- b000490 | references | pages [24] -->
微信号：MATHmodels

<!-- b000491 | references | pages [24] -->
[6]  G T S Lee, Lee G T S, Arisandi D, et al. Travel App - showing nearest tourism site using

<!-- b000492 | references | pages [24] -->
Haversine formula and directions with Google Maps. 2020, 852(1):012161-.

<!-- b000493 | references | pages [24] -->
[7]  Chen Kun. Research and Verification of Multi-UAV Cooperative Control Technology in

<!-- b000494 | references | pages [24] -->
Dynamic Environment. 2019

<!-- b000495 | references | pages [24] -->
[8]  List of major bushfires in Australia From Wikipedia, the free encyclopedia https://en.wik-

<!-- b000496 | references | pages [24] -->
ipedia.org/wiki/List_of_major_bushfires_in_Australia

<!-- b000497 | references | pages [24] -->
[9]  Mandallaz, D,R Ye. Prediction of forest fires with Poisson models. Journal of Forest Re-

<!-- b000498 | references | pages [24] -->
search . 1997

<!-- b000499 | references | pages [24] -->
[10]  ALTITUDINAL MAP OF VICTORIA http://romseyaustralia.com/rombook1map1.html

<!-- b000500 | references | pages [24] -->
[11]  Drone Laws in Australia

<!-- b000501 | references | pages [24] -->
https://web.archive.org/web/20170515150737/http://uavcoach.com/drone-laws-in-aus-

<!-- b000502 | references | pages [24] -->
tralia/

<!-- b000503 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000504 | references | pages [24] -->
关注数学模型

<!-- b000505 | furniture | pages [24] -->
2

<!-- b000506 | furniture | pages [24] -->
MATHmodels

<!-- b000507 | furniture | pages [24] -->
获取更多资讯

<!-- b000508 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000509 | furniture | pages [25] -->
Team # 2102199                                                                            Page 25 of 25

<!-- b000510 | heading | pages [25] -->
Appendices

<!-- b000511 | prose | pages [25] -->
Python code 微信公众号：数学模型 1. from haversine import haversine, Unit 2. import folium 3. import pandas as pd 4. from folium.plugins import HeatMap 5. import numpy as np 6.

<!-- b000512 | prose | pages [25] -->
7. def mark_Repeater(location: tuple, longth,color = 'red'):

<!-- b000513 | prose | pages [25] -->
8.     folium.Circle( 9.         radius=longth, 10.         location=location, 11.         color='orange', 微信号：MATHmodels 12.         fill=True, 13.     ).add_to(m) 14.     folium.Marker(location, icon=folium.Icon(color=color, pre- fix='fa', icon='tree')).add_to(m) 15.

<!-- b000514 | prose | pages [25] -->
16.

<!-- b000515 | prose | pages [25] -->
17. def fill_grid(m, boundary, color):

<!-- b000516 | prose | pages [25] -->
18.     for (a, b) in boundary:

<!-- b000517 | prose | pages [25] -->
19.         a = a-1 20.         b = b-1 21.         folium.Polygon([ 22.             [-35.8 - (b - 1) * 0.09, 144.4 + (a - 1) * 0.1158849], 23.             [-35.8 - (b - 1) * 0.09, 144.4 + a * 0.1158849], 24.             [-35.8 - b * 0.09, 144.4 + a * 0.1158849], 25.             [-35.8 - b * 0.09, 144.4 + (a - 1) * 0.1158849], 26.         ], color=color, weight=2, fill=True, fill_color=color, fill_opac ity=0.3).add_to(m)

<!-- b000518 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000519 | prose | pages [25] -->
关注数学模型

<!-- b000520 | furniture | pages [25] -->
2

<!-- b000521 | furniture | pages [25] -->
MATHmodels

<!-- b000522 | furniture | pages [25] -->
获取更多资讯
