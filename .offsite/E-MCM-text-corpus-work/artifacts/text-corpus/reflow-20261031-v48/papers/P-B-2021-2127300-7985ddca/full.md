# P-B-2021-2127300-7985ddca

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | front_matter | pages [1] -->
Team # 2127300

<!-- b000003 | front_matter | pages [1] -->
Problem Chosen

<!-- b000004 | front_matter | pages [1] -->
2021

<!-- b000005 | front_matter | pages [1] -->
Team Control Number

<!-- b000006 | prose | pages [1] -->
MCM/ICM

<!-- b000007 | front_matter | pages [1] -->
B

<!-- b000008 | front_matter | pages [1] -->
2127300

<!-- b000009 | heading | pages [1] -->
Summary Sheet

<!-- b000010 | title | pages [1] -->
Rapid Bushfire Response System

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | heading | pages [1] -->
Abstract

<!-- b000013 | prose | pages [1] -->
To better deal with fires, a new fire response system with drones has been proposed. We use the optimization model to discuss several problems with drones.

<!-- b000014 | prose | pages [1] -->
For problem 1, it is an optimization problem to minimize the equipment cost and maximize the efficiency and safety of fighting fires. First, we choose the fire data of Victoria state on January 4, 2020, when the areas of fires are largest. Then we grid the fire areas and evaluate the fire in each grid by the correlation coefficient of the fire frequency, brightness, and temperature. Next, we analyze the radio wave propagation loss and get the relationship of the communication range of the repeater drones and

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
the terrains. Based on the assumption that SSA drones are equivalent to the forward teams, 3 shifts of SSA drones are needed to cover the forward teams uninterruptedly for each mobile EOC. By genetic algorithm, we get the required numbers of repeater drones is 24 and the number of SSA drones is 30. Therefore, the total budget is $540,000(AUD).

<!-- b000017 | prose | pages [1] -->
For problem 2, we first train the LSTM model to predict the temperature in the next decade. By the regression analysis of the relationship between the number of fire sites and the daily temperature, we predict the fire situation, and the maximum number of fire sites is 2698.14, which 8.84% larger than the number in problem1. Then, according to the fire distribution in the source data, the fire area is diffused by the proportion to get the simulation of extreme fire conditions. Substituting the simulated fire map into the model, new results were obtained: the number of relay stations increased to 27, and the number of SSA increased to 48, with an increase of 30,000 and 18,000, respectively, for a total increase of 210,000(AUD).

<!-- b000018 | prose | pages [1] -->
For problem 3, according to Radio Wave Propagation Loss Model, repeater drones should be located near a high mountain. By limiting the distance between mobile EOC and higher mountains, the search model of a pair of mobile EOC was optimized to find 9 mobile EOC. Then, the range of the repeater drones is limited according to the terrain features, and the communication range is calculated according to the terrain features of its position. We make the optimized genetic model, to finding out that the number of repeater drones is 16, and calculate the corresponding longitude and latitude of the drones as well.

<!-- b000019 | prose | pages [1] -->
To assess the stability of our model, we change the value of drones’flight altitude and discuss its influence. It turns out that the changes have little effect on the final result and the model is relatively stable.

<!-- b000020 | keywords | pages [1] -->
Key words: Genetic Algorithm, LSTM, Multivariate Optimal Programming

<!-- b000021 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000022 | prose | pages [1] -->
关注数学模型

<!-- b000023 | furniture | pages [1] -->
2

<!-- b000024 | furniture | pages [1] -->
MATHmodels

<!-- b000025 | furniture | pages [1] -->
获取更多资讯

<!-- b000026 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000027 | furniture | pages [2] -->
Team # 2127300

<!-- b000028 | heading | pages [2] -->
Contents

<!-- b000029 | contents | pages [2] -->
1. Introduction...................................................................................................................................................1

<!-- b000030 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000031 | contents | pages [2] -->
1.1 Background..............................................................................................................................................1

<!-- b000032 | contents | pages [2] -->
1.2 Problem Restatement..........................................................................................................................1

<!-- b000033 | contents | pages [2] -->
1.3 Our Work..................................................................................................................................................1

<!-- b000034 | contents | pages [2] -->
2. Assumptions and Justification….......................................................................................................2

<!-- b000035 | contents | pages [2] -->
3.Nonations……..................................................................................................................................................2

<!-- b000036 | contents | pages [2] -->
4. Models and Solutions...............................................................................................................................4

<!-- b000037 | contents | pages [2] -->
4.1 Optimal Purchase Plan Model........................................................................................................4

<!-- b000038 | contents | pages [2] -->
4.1.1 Analysis of Problem 1.............................................................................................................4

<!-- b000039 | contents | pages [2] -->
4.1.2 Problem Visualization............................................................................................................5

<!-- b000040 | contents | pages [2] -->
4.1.3 Radio Wave Propagation Loss Model............................................................................6

<!-- b000041 | contents | pages [2] -->
4.1.4 The Relationship between SSA Drones and Front-line Personnel...................7

<!-- b000042 | contents | pages [2] -->
4.1.5 Finding the Locations of EOCs by Genetic Algorithm..........................................8

<!-- b000043 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000044 | contents | pages [2] -->
4.1.6 Finding the locations of Radio-repeater Drones by Genetic Algorithm....11

<!-- b000045 | contents | pages [2] -->
4.1.7 Finding the Number of SSA Drones..............................................................................11

<!-- b000046 | contents | pages [2] -->
4.2 Adaptation of Optimal Purchase Plan Model.......................................................................12

<!-- b000047 | contents | pages [2] -->
4.2.1 Prediction of Extreme Fire Events over the Next Decade.................................12

<!-- b000048 | contents | pages [2] -->
4.2.2 Finding the Number of SSA Drones.............................................................................14

<!-- b000049 | contents | pages [2] -->
4.3 Optimal Location of Radio-repeater Drones Model.........................................................16

<!-- b000050 | contents | pages [2] -->
4.3.1 Analysis of Problem 1......................................................................................................... 16

<!-- b000051 | contents | pages [2] -->
4.3.2 Problem Visualization.........................................................................................................16

<!-- b000052 | contents | pages [2] -->
4.3.3Model Establishment Based on Genetic Algorithm................................................17

<!-- b000053 | contents | pages [2] -->
5.Sensitivity Analysis...................................................................................................................................19

<!-- b000054 | contents | pages [2] -->
5.1 Radio Wave Propagation Loss Model.....................................................................................19

<!-- b000055 | contents | pages [2] -->
6.Strengths and Weakness...................................................................................................................... 20

<!-- b000056 | contents | pages [2] -->
6.1 Strengths.................................................................................................................................................20

<!-- b000057 | contents | pages [2] -->
6.2 Weakness................................................................................................................................................20

<!-- b000058 | contents | pages [2] -->
7.Conclusions.................................................................................................................................................. 20

<!-- b000059 | contents | pages [2] -->
7.1 Conclusions of problem 1............................................................................................................. 20

<!-- b000060 | contents | pages [2] -->
7.2 Conclusions of problem 2.............................................................................................................20

<!-- b000061 | contents | pages [2] -->
7.3 Conclusions of problem 3.............................................................................................................21

<!-- b000062 | contents | pages [2] -->
Budget Request

<!-- b000063 | contents | pages [2] -->
References

<!-- b000064 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000065 | contents | pages [2] -->
关注数学模型

<!-- b000066 | furniture | pages [2] -->
2

<!-- b000067 | furniture | pages [2] -->
MATHmodels

<!-- b000068 | furniture | pages [2] -->
获取更多资讯

<!-- b000069 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000070 | furniture | pages [3] -->
Team # 2127300

<!-- b000071 | furniture | pages [3] -->
Page 1 of 20

<!-- b000072 | heading | pages [3] -->
1. Introduction

<!-- b000073 | heading | pages [3] -->
1.1 Background

<!-- b000074 | prose | pages [3] -->
微信公众号：数学模型 Australia is one of the countries with a high incidence of bushfires. From 2019 to 2020, Australia has been suffering from bushfires for more than four months, which not only led to serious economic losses and casualties but also posed a threat to global ecological security.

<!-- b000075 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000076 | caption | pages [3] -->
Figure 1: A scene of Australia bushfires [1]

<!-- b000077 | prose | pages [3] -->
The development and modification of technologies has greatly expanded the ways of dealing with fire events. For example, drones are widely used in fighting fires nowadays. Compared with the traditional means of disaster relief, the function of monitoring fire and transmitting signals offered by drones can broaden the range of fire detection and played a positive role in ensuring the safety of front-line personnel. In addition, collaboration among drones, front-line personnel and EOCs can help improve the effectiveness of fighting fires.

<!-- b000078 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000079 | prose | pages [3] -->
A bushfire response system composed of drones, front-line personnel and EOCs is proposed to enhance the capability of fighting fires. Considering the restrictions identified with the problem statement, we need to address the following problems:

<!-- b000080 | prose | pages [3] -->
1. Design a model to determine the optimal purchase plan of SSA drones and radio-repeater drones for a new division of Victoria’s CFA.

<!-- b000081 | prose | pages [3] -->
2. Adapt the model of problem 1 to the likelihood of extreme fires in the next decade and get the increase in the cost of equipment.

<!-- b000082 | prose | pages [3] -->
3. Design a model to determine the optimal locations of hovering VHF/UHF radio-repeater drones and take terrains and fire sizes into consideration.

<!-- b000083 | heading | pages [3] -->
1.3 Our work

<!-- b000084 | prose | pages [3] -->
Due to the proliferation of wildfires in Australia last year, the fire department's need to deal with fires in a timely manner has increased. At the same time, because of the complex terrain of the mountain, it has become more critical to assist firefighters in handling the fire through drones.

<!-- b000085 | prose | pages [3] -->
For problem 1, it is required to find the best match between the number of drones equipped with SSA and the number of repeater drones in consideration of safety,

<!-- b000086 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000087 | prose | pages [3, 4] -->
关注数学模型 economy, observation and communication capabilities, terrain, fire size and frequency. ratio. That is, consider how to reasonably arrange the actions of the drones to make it have the highest fire handling capability and minimize the overhead.

<!-- b000088 | furniture | pages [3] -->
2

<!-- b000089 | furniture | pages [3] -->
MATHmodels

<!-- b000090 | furniture | pages [3] -->
获取更多资讯

<!-- b000091 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000092 | furniture | pages [4] -->
Team # 2127300

<!-- b000093 | furniture | pages [4] -->
Page 2 of 20

<!-- b000095 | prose | pages [4] -->
For problem 2, we need to predict the fire situation in the next ten years based on 微信公众号：数学模型 past data, and consider the impact on extreme fire conditions on our previous model, that is, optimizing the previous model based on the extreme fire situation, and analyzing the changes in the results.

<!-- b000096 | prose | pages [4] -->
For problem 3, the existence of repeater drones makes it easier for frontline personnel to keep in touch with EOC. However, due to the complex terrain of the mountain, it will cause loss of wireless signal propagation, so a suitable position of repeater drones should be found, which can minimize the loss, in turn to make the fire department more capable of handling wildfires.

<!-- b000097 | heading | pages [4] -->
2. Assumptions and Justification

<!-- b000098 | prose | pages [4] -->
The maximum flying height of drones is 4000 m. We summarize the 微信号：MATHmodels parameters of common drones in the market.

<!-- b000099 | prose | pages [4] -->
There are several EOCs that can be sent to the fire scenes. The charging and whole-process control of drones depend on EOC, and the fire scope is generally wide, so EOC should be arranged in different fire areas to ensure timely disaster response.

<!-- b000100 | prose | pages [4] -->
It is the southeast wind in the fire season. The fire danger period was summer and autumn in Victoria [3], when southeast winds prevail in Victoria.

<!-- b000101 | prose | pages [4] -->
The temperature of the measuring point can represent the temperature of the whole fire area. The selected Orbost location is close to the fire area.[4] The range where SSA drones can observe is equivalent to the mobile range of front-line personnel. In this way we can see the SSA drones as forward teams, which can simply the problem and ensure the safety of front-line personnel.

<!-- b000102 | heading | pages [4] -->
3. Notations

<!-- b000103 | prose | pages [4] -->
Symbols Description ݔ map abscissa ݕ map ordinate the fire evaluation value of the corresponding area ݔݕ the frequency of fires in the corresponding area ݔݕ the temperature of the corresponding area measured by satellite ݐ݁݉ ݔݕ the brightness of the corresponding area measured by satellite 쳌䁐݃ ݐݔݕ

<!-- b000104 | prose | pages [4] -->
weighting coefficient of temperature ͳ weighting coefficient of brightness ʹ the evaluation value of the whole fire range ݐ݋ݐݐ ܤ the equipment cost (AUD)

<!-- b000105 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000106 | prose | pages [4, 5] -->
关注数学模型 ɉ݂݀ the length of the waves the range of wireless communication frequency dimensionless parameters V 微信公众号：数学模型 ߛͳ the horizontal distance between the radio-repeater drone and the mountain (Figure 5) ߛʹ the horizontal distance between the EOC and the mountain (Figure 5 ) relative altitude (Figure 5) signal loss L ܮ݋ݏ݀쳌݋݋݁ the signal strength of the radio-repeater drones ܣഥ average altitude the distance between a fire site and the EOC D ݐݐ time required for SSA drones to arrive at a specific fire site ܦݐ the distance between the SSA drones and a specific fire site ݐ time required for the radio-repeater drones to arrive at a specific 微信号：MATHmodels fire site ܦ the distance between the radio-repeater drones and a specific fire site ݐݏ the detection time of the drones ݐ the charging time of the drones the number of mobile EOCs N ݋݉݀݉ the number of the radio-repeater drones the distance between the radio-repeater drones and the mobile EOCs the moving range of forward teams 쳌 the rang of a radio-repeater drone 쳌䁐 the range of a handheld radio the projected length of the fire along the 45° counterclockwise line l݈ of the X-axis as the fire action moves northwest the longest projection length within the control range of each ݔݐ mobile EOC ݋ݏݏݐ the number of SSA drones needed to cover the longest projection length within the control range of each mobile EOC 쳌ݏݏݐ the detection range of a single SSA drone ݐ temperature ሺݔ ǡ ݕ ሻ the coordinate of high mountains ሺݔ݁ǡ ݕ݁ሻ the coordinate of a mobile EOC ݉݀ the height of a mountain that can block the path of a repeater drone's wireless signals horizontal distance from the repeater drone to the mountains which can block the path of a repeater drone's wireless signals

<!-- b000107 | furniture | pages [4] -->
2

<!-- b000108 | furniture | pages [4] -->
MATHmodels

<!-- b000109 | furniture | pages [4] -->
获取更多资讯

<!-- b000110 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000111 | furniture | pages [5] -->
Team # 2127300

<!-- b000112 | furniture | pages [5] -->
Page 3 of 20

<!-- b000114 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000115 | prose | pages [5] -->
关注数学模型

<!-- b000116 | furniture | pages [5] -->
2

<!-- b000117 | furniture | pages [5] -->
MATHmodels

<!-- b000118 | furniture | pages [5] -->
获取更多资讯

<!-- b000119 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000120 | furniture | pages [6] -->
Team # 2127300

<!-- b000121 | furniture | pages [6] -->
Page 4 of 20

<!-- b000122 | heading | pages [6] -->
4. Models and Solutions

<!-- b000123 | heading | pages [6] -->
4.1 Optimal Purchase Plan Model

<!-- b000124 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000125 | heading | pages [6] -->
4.1.1 Analysis of Problem 1

<!-- b000126 | prose | pages [6] -->
The objective of problem 1 is to determine the optimal number and mix of SSA drones and Radio Repeater drones to purchase on the basis of considering relevant factors. We conclude 6 factors from the problem background, including safety, economy, fire size and frequency, observation range, communication ability, and terrain. Therefore, it is essentially an optimization problem.

<!-- b000127 | prose | pages [6] -->
The relevant factors are described as follows:

<!-- b000128 | prose | pages [6] -->
Safety: the signal of the front-line personnel can be captured by the SSA drones.

<!-- b000129 | prose | pages [6] -->
Economy: the cost of the drones should be as low as possible. 微信号：MATHmodels Observation range: the area of fire that can be observed by SSA drones should be as large as possible.

<!-- b000130 | prose | pages [6] -->
Communication ability: the area of fire that can be covered by the range of radio-repeater drones’ signals should be as large as possible.

<!-- b000131 | prose | pages [6] -->
Terrain: mountains can influence the coverage area of SSA drones by affecting the radio communication range of the front-line personnel and the radio-repeater drones.

<!-- b000132 | prose | pages [6] -->
Fire size and frequency: The parameters of the fire area detected by the satellite, such as temperature, brightness, confidence, etc., can be used to evaluate the fire of the corresponding area We gain the data of fire in Australia in 2019-2020. [5] In order to ensure a control ability of wildfires, we select January 4, the day with the largest active fire coverage area from October 2019 to July 2020, as the reference standard. The fire coverage area on that day is shown in the Figure 2.

<!-- b000133 | caption | pages [6] -->
Figure 2: The fire coverage area on January 4, 2020

<!-- b000134 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000135 | prose | pages [6] -->
关注数学模型

<!-- b000136 | furniture | pages [6] -->
2

<!-- b000137 | furniture | pages [6] -->
MATHmodels

<!-- b000138 | furniture | pages [6] -->
获取更多资讯

<!-- b000139 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000140 | furniture | pages [7] -->
Team # 2127300

<!-- b000141 | furniture | pages [7] -->
Page 5 of 20

<!-- b000142 | heading | pages [7] -->
4.1.2 Problem Visualization

<!-- b000143 | prose | pages [7] -->
We gain the state of Victoria's longitude and latitude of the elevation data and take 1 km as the sampling interval. Then we carry out planarization and meshing to 微信公众号：数学模型 construct a specific topographic map.

<!-- b000144 | prose | pages [7] -->
We choose the eastern part of Victoria to carry on our research. The visualization result of the fire coverage area on January 4 is as Figure 3.

<!-- b000145 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000146 | caption | pages [7] -->
Figure 3: The visualization result of the fire coverage area on January 4

<!-- b000147 | prose | pages [7] -->
The yellow areas in Figure 3 indicate the frequency of fires ݔݕ.

<!-- b000148 | prose | pages [7] -->
We define ݔݕas the fire evaluation value of the corresponding area, and the

<!-- b000149 | prose | pages [7] -->
expression is:

<!-- b000150 | prose | pages [7] -->
ͳ ή ݐ݁݉ ݔݕ൅݇ ʹ ήܾ쳌䁐݃ ݐݔݕ ݔݕൌܲ ݔݕή݇

<!-- b000151 | prose | pages [7] -->
݀݋ݐ ʹ ൌͳܲ ͳ ൒Ͳ， ʹ ൒Ͳ，݇ͳ ൅݇

<!-- b000152 | prose | pages [7] -->
ݔݕ——the frequency of fires in the corresponding area

<!-- b000153 | prose | pages [7] -->
ݐ݁݉ ݔݕ——the temperature of the corresponding area measured by satellite

<!-- b000154 | prose | pages [7] -->
쳌䁐݃ ݐݔݕ——the brightness of the corresponding area measured by satellite

<!-- b000155 | prose | pages [7] -->
ͳ——weighting coefficient of temperature ʹ——weighting coefficient of brightness

<!-- b000156 | prose | pages [7] -->
The higher the brightness is, the greater the value of ݔݕwill be, which means

<!-- b000157 | prose | pages [7] -->
the fire is more serious.

<!-- b000158 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000159 | prose | pages [7, 8] -->
关注数学模型 Therefore, the problem 1 can be transformed into: determine the optimal number and mix of SSA drones and Radio Repeater drones to maximize the evaluation value of the fire range ݐ݋ݐݐ݈that can be detected and minimize the cost ܤ.

<!-- b000160 | furniture | pages [7] -->
2

<!-- b000161 | furniture | pages [7] -->
MATHmodels

<!-- b000162 | furniture | pages [7] -->
获取更多资讯

<!-- b000163 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000164 | furniture | pages [8] -->
Team # 2127300

<!-- b000165 | furniture | pages [8] -->
Page 6 of 20

<!-- b000167 | prose | pages [8] -->
According to the coverage area of the fire on January 4th, the elevation data 微信公众号：数学模型 corresponding to the areas where the fire sites are searched. Fire sites means the squares in fire after we put the map behind grids.

<!-- b000168 | prose | pages [8] -->
The visualization results are as follows:

<!-- b000169 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000170 | caption | pages [8] -->
Figure 4: The visualization result of the elevation data

<!-- b000171 | prose | pages [8] -->
In Figure 4, the yellow parts represent the areas of higher ground and the blue parts represent areas of lower ground.

<!-- b000172 | prose | pages [8] -->
It can be seen that the overall altitude of the region is not very high. The highest place is only 2km high, and the flying altitude of the drones can reach 4km. As a result, the drones do not need to go around to avoid mountains.

<!-- b000173 | heading | pages [8] -->
4.1.3 Radio Wave Propagation Loss Model

<!-- b000174 | prose | pages [8] -->
However, the complexity of the terrain will affect the communication coverage of the handheld radio of the forward teams and the radio-repeater drones. The influence of the peak landform on the radio waves can be roughly divided into the following two ways:

<!-- b000175 | caption | pages [8] -->
Figure 5: two situations that the influence of the peak landform on the radio

<!-- b000176 | prose | pages [8] -->
waves [6] According to the DEM, there are only 1 or 2 peaks per 20km on average within the range of the radio-repeater drones, so only single peak loss needs to be considered.

<!-- b000177 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000178 | prose | pages [8, 9] -->
关注数学模型 The relationship between signal loss and propagation distance is as follows:

<!-- b000179 | furniture | pages [8] -->
2

<!-- b000180 | furniture | pages [8] -->
MATHmodels

<!-- b000181 | furniture | pages [8] -->
获取更多资讯

<!-- b000182 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000183 | furniture | pages [9] -->
Team # 2127300

<!-- b000184 | furniture | pages [9] -->
Page 7 of 20

<!-- b000186 | prose | pages [9] -->
32 . 44 20 lg ( ) 20 lg ( ) Los d km f MHz   

<!-- b000187 | prose | pages [9] -->
Introduce dimensionless parameters V with the expression below: 微信公众号：数学模型 2 1 1 ( ) V h         If h is positive, then the wireless signal propagation path is blocked by the mountain and V is negative.

<!-- b000188 | prose | pages [9] -->
If h is negative, then the wireless signal propagation path is not blocked by the mountain, and V is positive.

<!-- b000189 | prose | pages [9] -->
The relationship between signal loss L and V is as follows:

<!-- b000190 | prose | pages [9] -->
0 , 8.0 dB V    20 lg( 5.0 .0 62 ), 0 8.0 V V      .0 95 V 20 lg( 5.0 ), 1 8.0 e V    L   微信号：MATHmodels 2 20 lg( 4.0 .0 1184 ( 1.0 .0 38 ) ), 4.2 1 V V          .0 225 20 lg( ) 4.2 V     ， V  According to the communication range of the radio-repeater drones, the signal strength can be calculated as ܮ݋ݏ݀쳌݋݋݁ൌ䇅͵Ǥʹ䇅͵⺁݀ܤ.

<!-- b000191 | prose | pages [9] -->
Assuming that the flying altitude of the drones is 4km.

<!-- b000192 | caption | pages [9] -->
Figure 6: Diagram of the drones’ flight height and mountain height

<!-- b000193 | prose | pages [9] -->
In Figure 6, when the mountain peak is just not occluding the repeater to transmit .0 03 4 8 L dB wireless signals, we can obtain that   and the radio-repeater drones’ communication range is approximately 18.5km. Since the heights of the peak are under 2km, there is no need to consider the influence of communication range when the peak is within the distance of 10km of the radio-repeater drones.

<!-- b000194 | prose | pages [9] -->
Additionally, the average altitude of this region is ܣഥൌ551.8km, so the loss L can be obtained, L=-16.55dB. Based on the radio wave propagation loss model, when the terrain is relatively complex, the communication range of the radio-repeater drones is approximately 18km.

<!-- b000195 | heading | pages [9] -->
4.1.4 The Relationship between SSA Drones and Front-line Personnel

<!-- b000196 | prose | pages [9] -->
The role of the SSA drones is to detect information on the front-line personnel's wearable devices, so we can assume that:

<!-- b000197 | prose | pages [9] -->
The range where SSA drones can observe is equivalent to the mobile range of front-line personnel.

<!-- b000198 | prose | pages [9] -->
The observation range of a single SSA drone is equivalent to the radio

<!-- b000199 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000200 | prose | pages [9, 10] -->
关注数学模型 communication range of front-line personnel.

<!-- b000201 | furniture | pages [9] -->
2

<!-- b000202 | furniture | pages [9] -->
MATHmodels

<!-- b000203 | furniture | pages [9] -->
获取更多资讯

<!-- b000204 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000205 | furniture | pages [10] -->
Team # 2127300

<!-- b000206 | furniture | pages [10] -->
Page 8 of 20

<!-- b000208 | prose | pages [10] -->
The observation range of SSA drones need to cover the entire front-line personnel.

<!-- b000209 | prose | pages [10] -->
The maximum flight time of a single SSA drone is 2.5 hours, and it can start 微信公众号：数学模型 again after 1.75 hours of charging time.

<!-- b000210 | prose | pages [10] -->
The maximum distance between an SSA drone and an EOC is 30km.

<!-- b000211 | prose | pages [10] -->
Consequently, in the optimization process, we can ignore the marching process of front-line personnel and directly consider how to maximize the coverage of the fire observation area by SSA drones.

<!-- b000212 | prose | pages [10] -->
For a fire that D km away from the EOC, the time required for SSA drones to arrive at the place is / ( ) t D v hours a  , a and the time for return is / ( ) t D v hours b  . b 微信号：MATHmodels The detection time is ݐݏand the charging time is ݐܿ.

<!-- b000213 | prose | pages [10] -->
In order to ensure the full coverage of front-line personnel by SSA drones, in the light of the relationship among SSA drones, the full coverage of front-line personnel in any region can be achieved when the number of SSA is 3. The analysis process is shown in the Figure 7.

<!-- b000214 | caption | pages [10] -->
Figure 7: The exchange period of SSA drones

<!-- b000215 | heading | pages [10] -->
4.1.5 Finding the Location of EOCs by Genetic Algorithm

<!-- b000216 | prose | pages [10] -->
To determine the optimal number and mix of SSA drones and Radio Repeater drones, it is necessary to assume the optimal location of mobile EOCs based on fire distribution and the severity of each fire area, the purpose of which is that the evaluation of the fire range that they control can be as high as possible.

<!-- b000217 | prose | pages [10] -->
The fire distribution diagram is shown in Figure 8.

<!-- b000218 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000219 | prose | pages [10, 11] -->
关注数学模型 微信公众号：数学模型

<!-- b000220 | furniture | pages [10] -->
2

<!-- b000221 | furniture | pages [10] -->
MATHmodels

<!-- b000222 | furniture | pages [10] -->
获取更多资讯

<!-- b000223 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000224 | furniture | pages [11] -->
Team # 2127300

<!-- b000225 | furniture | pages [11] -->
Page 9 of 20

<!-- b000227 | caption | pages [11] -->
Figure 8: Fire distribution

<!-- b000228 | prose | pages [11] -->
The number of EOCs to be moved and the corresponding position can be 微信号：MATHmodels calculated using Genetic Algorithm. The algorithm is as follows:

<!-- b000229 | heading | pages [11] -->
(1) Establish a feasible solution set

<!-- b000230 | prose | pages [11] -->
We first determine the set of feasible solutions. Each mobile EOC has different positions (x, y), which can be represented by two sets of sequences. We assume that the number of mobile EOCs is n:

<!-- b000231 | prose | pages [11] -->
[ , ,..., ], [ , ,..., ] x x x y y y 1 2 1 2 n n

<!-- b000232 | prose | pages [11] -->
(2) Coding For an initial sequence string, the string is treated as a DNA sequence and manipulated genetically. Initialization is done by randomly generating a range of numbers.

<!-- b000233 | prose | pages [11] -->
(3) Calculate fitness The fitness is the objective function. In this subproblem, the objective function is to maximize the sum of the disaster evaluation value ݔݕcovering the fire area.

<!-- b000234 | prose | pages [11] -->
The samples with higher fitness are excellent samples, and vice versa.

<!-- b000235 | prose | pages [11] -->
(4) Select excellent samples as the parent generation Through the way of roulette to realize the choice of the parent generation, the specific steps are as follows:

<!-- b000236 | prose | pages [11] -->
Step1: sum the fitness of the population.

<!-- b000237 | prose | pages [11] -->
Step2: calculate the proportion of each sample in the sample sum as the probability, and obtain the cumulative probability in turn.

<!-- b000238 | prose | pages [11] -->
Step3: Generate a random number between 0 and 1. If the random number falls into the region of accumulative probability, select the sample from the region as the parent generation.

<!-- b000239 | prose | pages [11] -->
Step4: Run until the number of parent generations meets the conditions.

<!-- b000240 | prose | pages [11] -->
(5) Cross

<!-- b000241 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000242 | prose | pages [11, 12] -->
关注数学模型 After obtaining the father generation samples, two of the father generation samples are selected to cross each other to produce offspring. Two crossing points are selected for each combination to exchange the DNA between the two crossing points, which is the so-called inheritance. 微信公众号：数学模型 Selecting a good parent for inheritance will also make the offspring have the good genes of the father.

<!-- b000243 | furniture | pages [11] -->
2

<!-- b000244 | furniture | pages [11] -->
MATHmodels

<!-- b000245 | furniture | pages [11] -->
获取更多资讯

<!-- b000246 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000247 | furniture | pages [12] -->
Team # 2127300

<!-- b000248 | furniture | pages [12] -->
Page 10 of 20

<!-- b000250 | prose | pages [12] -->
(6) Variation Only crossover operation will make the objective function converge to a local optimal solution. So mutation needs to be set to make the gene mutation of a node in the DNA, which is beneficial to ensure the diversity of the population.

<!-- b000251 | prose | pages [12] -->
(7) Iteration Repeat the iteration to make the population finally reach the optimal state, the resulting population is the optimal solution.

<!-- b000252 | prose | pages [12] -->
The location of mobile EOCs found by Genetic Algorithm is shown in Figure 9.

<!-- b000253 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000254 | caption | pages [12] -->
Figure 9: The location of mobile EOCs

<!-- b000255 | prose | pages [12] -->
The red circles represent mobile EOCs. The fitness curve is as follows:

<!-- b000256 | caption | pages [12] -->
Figure 10: The fitness curve

<!-- b000257 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000258 | prose | pages [12] -->
关注数学模型

<!-- b000259 | furniture | pages [12] -->
2

<!-- b000260 | furniture | pages [12] -->
MATHmodels

<!-- b000261 | furniture | pages [12] -->
获取更多资讯

<!-- b000262 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000263 | furniture | pages [13] -->
Team # 2127300

<!-- b000264 | furniture | pages [13] -->
Page 11 of 20

<!-- b000265 | heading | pages [13] -->
4.1.6 Finding the Locations of Radio-repeater Drones by Genetic

<!-- b000266 | heading | pages [13] -->
Algorithm

<!-- b000267 | prose | pages [13] -->
微信公众号：数学模型 We can use the method in 4.1.5 to formulate the locations and number of the radio-repeater drones, so as to minimize the number of the radio-repeater drones and maximize the evaluation of the fire area covered by its communication range.

<!-- b000268 | prose | pages [13] -->
Through Genetic Algorithm, the locations and communication range of the Radio-repeater Drones are solved as shown in the Figure 11.

<!-- b000269 | prose | pages [13] -->
微信号：MATHmodels Figure 11：The locations and communication range of radio-repeater drones The red circle represents the location of the radio-repeater drones, and the white circle represents their communication range.

<!-- b000270 | prose | pages [13] -->
According to the relationship between the number of the radio-repeater drones (݋݉) and the distance between them and the mobile EOCs (݀ ):

<!-- b000271 | prose | pages [13] -->
,2 13 5. ( ) d km   m n   m ,3 13 5. ( ) d km   m As a result, the number of the radio-repeater drones is 24.

<!-- b000272 | heading | pages [13] -->
4.1.7 Finding the Number of SSA Drones

<!-- b000273 | prose | pages [13] -->
Given the preset location of the radio-repeater drones, it is possible to figure out how far the SSA's drones can detect a fire, which indicates the moving range R of forward teams.

<!-- b000274 | prose | pages [13] -->
R r r   m i 쳌݉——the range of a radio-repeater drone 쳌䁐——the range of a handheld radio The fire range that the SSA drones can detect is shown in the Figure 12.

<!-- b000275 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000276 | prose | pages [13, 14] -->
关注数学模型 微信公众号：数学模型

<!-- b000277 | furniture | pages [13] -->
2

<!-- b000278 | furniture | pages [13] -->
MATHmodels

<!-- b000279 | furniture | pages [13] -->
获取更多资讯

<!-- b000280 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000281 | furniture | pages [14] -->
Team # 2127300

<!-- b000282 | furniture | pages [14] -->
Page 12 of 20

<!-- b000284 | caption | pages [14] -->
Figure 12: The fire range that the SSA drones can detect

<!-- b000285 | prose | pages [14] -->
微信号：MATHmodels Because wind direction for the southeast wind on January 4, fire action tends to be from southeast to northwest direction. So, calculate the projected length l of the fire along the 45° counterclockwise line of the X-axis as the fire action moves northwest. The longest projection݈݉ݔݐwithin the control range of each mobile EOC corresponds to the maximum number ݋ݏݏݐof SSA drones needed:

<!-- b000286 | prose | pages [14] -->
3 max / n l r  ssa ssa

<!-- b000287 | prose | pages [14] -->
쳌ݏݏݐis the detection range of a single SSA drone, and the number of SSA drones required is 30.

<!-- b000288 | prose | pages [14] -->
The required budget is:

<!-- b000289 | prose | pages [14] -->
10000 * 540000 B n n    (AUD) （ ） m ssa To sum up, a detailed budget for the expense is attached below:

<!-- b000290 | caption | pages [14] -->
Table 1: The results of problem 1

<!-- b000291 | prose | pages [14] -->
Types of drones Price Number SSA drones 10,000(AUD) 30 Radio-repeater drones 10,000(AUD) 24 Total expense：540,000

<!-- b000292 | heading | pages [14] -->
4.2 Adaptation of Optimal Purchase Plan Model

<!-- b000293 | heading | pages [14] -->
4.2.1 Prediction of Extreme Fire Events over the Next Decade

<!-- b000294 | prose | pages [14] -->
The occurrence of forest fires is related to many factors, like long-term warming, rainfall deficiency and oceanic circulation anomalies. Among all these factors, temperature has a dominant influence on fire susceptibility for a land area. For example, Australia suffered from severe bushfires in 2019-2020, and at the same time,

<!-- b000295 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000296 | prose | pages [14, 15] -->
关注数学模型 the Australian Bureau of Meteorology has placed 2019 as the hottest year on record so far [7]. So, we make fire predictions based on temperature. 1.Temperature forecast for the next decade According to the areas where the fire occurred, we select the temperature data of 微信公众号：数学模型 the observation point in the eastern part of Victoria State, and it is assumed that the data of the observation point could represent the temperature of the whole fire area. The daily maximum and minimum temperature data from 1938 to 2020 were processed preliminarily. After analyzing the seasonal variation and overall trend of the temperature data, we choose the linear interpolation method to complete the missing data. Due to the long time period to be predicted and the large sample size of original data, we train the LSTM model to predict the temperature in the next decade. The specific training process and prediction results are shown in the Figure 13, 14.

<!-- b000297 | furniture | pages [14] -->
2

<!-- b000298 | furniture | pages [14] -->
MATHmodels

<!-- b000299 | furniture | pages [14] -->
获取更多资讯

<!-- b000300 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000301 | furniture | pages [15] -->
Team # 2127300

<!-- b000302 | furniture | pages [15] -->
Page 13 of 20

<!-- b000304 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000305 | caption | pages [15] -->
Figure 13: Training process of the model

<!-- b000306 | caption | pages [15] -->
Figure 14: Temperature projections for the next ten years

<!-- b000307 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000308 | prose | pages [15] -->
关注数学模型

<!-- b000309 | furniture | pages [15] -->
2

<!-- b000310 | furniture | pages [15] -->
MATHmodels

<!-- b000311 | furniture | pages [15] -->
获取更多资讯

<!-- b000312 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000313 | furniture | pages [16] -->
Team # 2127300

<!-- b000314 | furniture | pages [16] -->
Page 14 of 20

<!-- b000315 | heading | pages [16] -->
2. Fire events forecast for the next decade

<!-- b000316 | prose | pages [16] -->
Because the data of the fire sites measured by the MODIS satellite is distributed by date, to align it with the temperature data, we screen out the date of the fire situation, and then count the number of fire sites on that date. After putting these data 微信公众号：数学模型 in chronological order, we find out the temperature data of the corresponding date, and put them into the same table, which makes it easier to analyze the relationship between the temperature and fire sites.

<!-- b000317 | prose | pages [16] -->
After normalizing the data between August 2019 and January 2020, we compare the number of fires per day with the temperature and show them in the Figure 15.

<!-- b000318 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000319 | caption | pages [16] -->
Figure 15: The trend of fire sites number and the temperature

<!-- b000320 | prose | pages [16] -->
It can be found that the occurrence of large area fires is often related to the occurrence of extreme high temperature weather. Consequently, the higher the temperature is, the more likely fires are to occur, and the increase rate of the number of fires is faster. In this case, we use cftool in Matlab for regression analysis, and choose exponential curve as the fitting method for the relationship between fire and temperature. After calculating the coefficient in the case of minimum error sum of squares, we substitute the inverse normalization to obtain the following relationship.

<!-- b000321 | prose | pages [16] -->
ͳ͵Ǥ䇅㐲 ݐ ݐൌͳǤͲʹͶ ൈ ൈʹͶ͹㐲݂ Ͷ͵Ǥͳ ݐ represents the number of fire sites in Victoria at temperature ݐ.

<!-- b000322 | prose | pages [16] -->
According to the above expression and temperature data of the next decade, we can estimate the corresponding number of fire sites. Due to the need to consider the cost increase in extreme phenomena, we choose the maximum number of possible fire sites for the study. The number of fire sites is 2698.14 in the maximum case, which is about 8.84% more than the maximum in the source data. (Source data refers to fire data of Victoria state in 2019-2020.)

<!-- b000323 | heading | pages [16] -->
4.2.2 Finding the Number of SSA Drones

<!-- b000324 | prose | pages [16] -->
We only get the total number of fire sites through prediction, which is not enough for us to determine the locations of the drones. So, we use the largest range of fire site conditions in 19-20 years to simulate the possibility of a large fire in eastern

<!-- b000325 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000326 | prose | pages [16, 17] -->
关注数学模型 Victoria under future extreme conditions. In the case that the expansion ratio of the fire area relative to the source data has been worked out, we take the fire map of January 4, 2020 as the sample, and expand the fire area to 1.0884 times of the original on this basis. 微信公众号：数学模型 In order to realize the simulation of fire spread, we first draw the boundary range of the fire map on January 4, 2020 as a reference, as shown in the following Figure 16.

<!-- b000327 | furniture | pages [16] -->
2

<!-- b000328 | furniture | pages [16] -->
MATHmodels

<!-- b000329 | furniture | pages [16] -->
获取更多资讯

<!-- b000330 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000331 | furniture | pages [17] -->
Team # 2127300

<!-- b000332 | furniture | pages [17] -->
Page 15 of 20

<!-- b000334 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000335 | caption | pages [17] -->
Figure 16: the boundary range of the fire map on January 4, 2020

<!-- b000336 | prose | pages [17] -->
After the calculation of the fire area in the source data, we calculate the spread the fire area according to the proportion. On the basis of the Figure 15, we expand the area of fire, to simulate extreme fire situation may arise in the next decade. In accordance with the same probability to the spread of fire to fill in the form of grid fire beyond boundaries, we finally form a new fire situation map in Figure 17.

<!-- b000337 | caption | pages [17] -->
Figure 17: the boundary range of the extreme fire in the next decade

<!-- b000338 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000339 | prose | pages [17, 18] -->
关注数学模型 According to the fire situation data after expansion, the Optimal Purchase Plan Model is modified to solve the problem. It is found that the EOCs’ locations remain unchanged, while the number of radio-repeater drones and SSA drones changes as follows: 微信公众号：数学模型 The number of radio-repeater drones increases from 24 to 27, and the number of SSA drones increases from 30 to 48. In this case, the equipment cost increases by 30,000 and 18,000 respectively, with a total increase of 210,000(AUD).

<!-- b000340 | furniture | pages [17] -->
2

<!-- b000341 | furniture | pages [17] -->
MATHmodels

<!-- b000342 | furniture | pages [17] -->
获取更多资讯

<!-- b000343 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000344 | furniture | pages [18] -->
Team # 2127300

<!-- b000345 | furniture | pages [18] -->
Page 16 of 20

<!-- b000347 | caption | pages [18] -->
Table 2: The results of problem 2

<!-- b000348 | prose | pages [18] -->
Types of drones Price Number SSA drones 10,000(AUD) 48 Radio-repeater drones 10,000(AUD) 27 Total expense：750,000 The increase of equipment cost: 210,000

<!-- b000349 | heading | pages [18] -->
4.3 Optimal Location of Radio-repeater Drones Model

<!-- b000350 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000351 | heading | pages [18] -->
4.3.1 Analysis of Problem 3

<!-- b000352 | prose | pages [18] -->
Problem 3 is essentially the optimization of the location finding process of the radio-repeater drones in the modeling process of Problem 1. To specify, the model has to be modified to adapt to fires of different size on different terrains.

<!-- b000353 | prose | pages [18] -->
According to 4.2.1, when the wireless signal of the radio-repeater drones is just not blocked by the mountain, the communication range is about 18.5km. When there is diffraction during the transmission of the signal, it can be known by calculation that the diffracted signal can propagate far less than 1km. Therefore, diffraction happens, the communication range can be regarded as the horizontal distance between the radio-repeater drones and mountains.

<!-- b000354 | prose | pages [18] -->
To make the communication range of the radio-repeater drones as large as possible, high mountains should be in the circle of the 10km radius of the radio-repeater drones. At the same time, high mountain should not appear within the range of 10-20km of the radio-repeater drones. In this way, mountains have no effect on the communication range of the drones.

<!-- b000355 | prose | pages [18] -->
This constraint condition is added into the Optimal Purchase Plan Model. We take the fire occurred from October 1, 2019 to January 7, 2020 as the fire range for solving, aiming at simulating the optimal locations of radio-repeater drones for fires of different sizes on different terrains.

<!-- b000356 | heading | pages [18] -->
4.3.2 Problem Visualization

<!-- b000357 | prose | pages [18] -->
The areas covered by the wildfire between October 1, 2019, and January 7, 2020 is shown in Figure 18.

<!-- b000358 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000359 | prose | pages [18, 19] -->
关注数学模型 微信公众号：数学模型

<!-- b000360 | furniture | pages [18] -->
2

<!-- b000361 | furniture | pages [18] -->
MATHmodels

<!-- b000362 | furniture | pages [18] -->
获取更多资讯

<!-- b000363 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000364 | furniture | pages [19] -->
Team # 2127300

<!-- b000365 | furniture | pages [19] -->
Page 17 of 20

<!-- b000367 | caption | pages [19] -->
Figure 18: The areas covered by the wildfire between October 1, 2019, and

<!-- b000368 | prose | pages [19] -->
微信号：MATHmodels January 7, 2020 The corresponding DEM is shown in Figure19:

<!-- b000369 | caption | pages [19] -->
Figure 19: The terrains of areas covered by the wildfire between October 1,

<!-- b000370 | prose | pages [19] -->
2019, and January 7, 2020

<!-- b000371 | heading | pages [19] -->
4.3.3 Model Establishment Based on Genetic Algorithm

<!-- b000372 | prose | pages [19] -->
First of all, in order to prevent the radio-repeater drones from higher mountains, the mobile EOC should be near high mountains instead. Thus, the following constraints are added to the search model of the mobile EOCs:

<!-- b000373 | prose | pages [19] -->
2 2 2 ( ) ( ) 20 x x y y     h e h e

<!-- b000374 | prose | pages [19] -->
x , x , h y e y ( ) is the coordinate of a high mountain, and ( ) is the coordinate of mobile h e

<!-- b000375 | prose | pages [19] -->
EOCs.

<!-- b000376 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000377 | prose | pages [19, 20] -->
关注数学模型 Based on the Optimal Purchase Plan Model, the assumed locations of mobile EOCs are solved by Genetic Algorithm, which are shown in Figure 20.

<!-- b000378 | furniture | pages [19] -->
2

<!-- b000379 | furniture | pages [19] -->
MATHmodels

<!-- b000380 | furniture | pages [19] -->
获取更多资讯

<!-- b000381 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000382 | furniture | pages [20] -->
Team # 2127300

<!-- b000383 | furniture | pages [20] -->
Page 18 of 20

<!-- b000385 | prose | pages [20] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000386 | caption | pages [20] -->
Figure 20: The assumed locations of mobile EOCs

<!-- b000387 | prose | pages [20] -->
For the communication range of the radio-repeater drones, the following constraints are added:

<!-- b000388 | prose | pages [20] -->
ʹͲǡ݀ ൑ͳͲ ͳ䇅Ǥ⺁ǡ 쳌 ൌ Ͷ ൌʹͲ െ݀ ʹͲ 쳌ͳǡͳͲ ൑݀ ൑ʹͲ ݉——the height of a mountain that can block the path of a repeater drone's wireless signals݀ ——horizontal distance from the repeater drone to the mountains which can block the path of a repeater drone's wireless signals The optimized Genetic Algorithm is used to solve the locations of the radio-repeater drones, and the obtained locations are shown in Figure 21.

<!-- b000389 | caption | pages [20] -->
Figure 21: the locations of the radio-repeater drones

<!-- b000390 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000391 | prose | pages [20, 21] -->
关注数学模型 The corresponding longitude and latitude are shown in Table 3.

<!-- b000392 | furniture | pages [20] -->
2

<!-- b000393 | furniture | pages [20] -->
MATHmodels

<!-- b000394 | furniture | pages [20] -->
获取更多资讯

<!-- b000395 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000396 | furniture | pages [21] -->
Team # 2127300

<!-- b000397 | furniture | pages [21] -->
Page 19 of 20

<!-- b000399 | caption | pages [21] -->
Table 3: The longitude and latitude of each locations of the radio-repeater drones

<!-- b000400 | prose | pages [21] -->
Num. Lat Lon Num Lat Lon 1 9 -38.00177382 146.3194898 -37.92946048 146.4085731 微信公众号：数学模型 2 10 -37.99273465 146.3306252 -37.92042131 146.4197085 3 11 -37.98369548 146.3417606 -37.91138215 146.430844 4 12 -37.97465632 146.352896 -37.90234298 146.4419794 5 13 -37.96561715 146.3640314 -37.89330381 146.4531148 6 14 -37.95657798 146.3751669 -37.88426465 146.4642502 7 15 -37.94753882 146.3863023 -37.87522548 146.4753856 8 16 -37.93849965 146.3974377 -37.86618631 146.486521

<!-- b000401 | heading | pages [21] -->
5. Sensitivity Analysis

<!-- b000402 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000403 | heading | pages [21] -->
5.1 Radio Wave Propagation Loss Model

<!-- b000404 | prose | pages [21] -->
Since the topic do not give the flying altitude of the drones, after consulting relevant data of drones’ performance and radio signal transmission, as well as the terrain analysis of Victoria, we assume that the flying altitude of the UAV in the model was constant at 4km. At this point, in the case of single peak loss, the signal range of the repeater will decrease from 20km to 18km when the terrain is relatively complex, according to the relevant calculation.

<!-- b000405 | prose | pages [21] -->
In order to analyze the stability of the model under this hypothetical condition, we consider modifying the flying altitude of the drones. Taking 0.2 as the change value, we take 3.6km,3.8km,4.2km and 4.4km as the new conditions to calculate the signal range of the radio-repeater drones. The results are shown in the Table 5

<!-- b000406 | caption | pages [21] -->
Table 4: comparison of changes in flight altitude and signal range

<!-- b000407 | prose | pages [21] -->
Flight Altitude ͵Ǥh ͵Ǥ䇅 ͶǤͲ ͶǤʹ ͶǤͶ ( ) Signal Range ͳ͹Ǥʹ 17.5 ͳ䇅ǤͲ ͳ䇅Ǥ͵ ͳ䇅Ǥ͹ ( ʹ) When the drones’ flight height is increased by 5%, the signal range will be increased by 1.67%. At the same time, when flying height is decreased by 5%, the signal range will be decreased by 2.78%. So the scope of the change is not big.

<!-- b000408 | prose | pages [21] -->
Consequently, the flight height has little effect on the monitoring scope of the radio-repeater drones. The number of the drones mainly depends on the size and frequency of fires, and terrains.

<!-- b000409 | prose | pages [21] -->
The influence of flight altitude on the results is within the acceptable range, and the model created above is relatively stable on the whole based on the current hypothesis.

<!-- b000410 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000411 | prose | pages [21] -->
关注数学模型

<!-- b000412 | furniture | pages [21] -->
2

<!-- b000413 | furniture | pages [21] -->
MATHmodels

<!-- b000414 | furniture | pages [21] -->
获取更多资讯

<!-- b000415 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000416 | furniture | pages [22] -->
Team # 2127300

<!-- b000417 | furniture | pages [22] -->
Page 20 of 20

<!-- b000418 | heading | pages [22] -->
6. Strengths and Weaknesses

<!-- b000419 | heading | pages [22] -->
6.1 Strengths

<!-- b000420 | prose | pages [22] -->
微信公众号：数学模型 The comprehensive evaluation of the fire is completed with the parameters of  frequency, temperature and brightness, which makes the calculated coverage range of the drones more accurate and in line with the actual situation. Considering the overall value of fire evaluation and on the premise of ensuring  effectiveness, the scheme with the lowest cost can be solved by Genetic Algorithm. Moreover, the adaptability curve reaches the optimum under multiple iterations, indicating that the solution effect is good. In order to predict the future 10 years’ temperature, we chose LSTM model,  making both short-term and long-term memory network. The model is mainly to solve the gradient vanishing and gradient explosion problems in the training process of long sequence. Compared with ordinary RNN, LSTM has better performance in long sequence and more accurate prediction results. 微信号：MATHmodels

<!-- b000421 | heading | pages [22] -->
7.2 Weakness

<!-- b000422 | prose | pages [22] -->
 In problem 2, we ignored the change of the fire between areas and expand by proportion regarlessly. Thus the model is still an approximate on a large scale. This has doomed to limit the applications of it.  In the prediction the future fire event, we only used fire data in 2019-2020 for regression prediction, so data quantity is too little. Besides, There are many factors affecting fire, such as artificial fire fighting measures, etc., which reduce the accuracy of fire prediction. 7.Conclusions

<!-- b000423 | heading | pages [22] -->
7.1 Conclusions of Problem 1

<!-- b000424 | prose | pages [22] -->
Based on the Radio Wave Propagation Loss Model, when the terrain is complex,  the communication range of the radio-repeater drones is approximately 18km. In order to ensure the full coverage of front-line personnel by SSA drones, in the  light of the relationship among SSA drones, the full coverage of front-line personnel in any region can be achieved when the number of SSA is 3.

<!-- b000425 | caption | pages [22] -->
Table 5: The results of problem 1

<!-- b000426 | prose | pages [22] -->
Types of drones Price Number SSA drones 10,000(AUD) 30 Radio-repeater drones 10,000(AUD) 24 Total expense：540,000

<!-- b000427 | heading | pages [22] -->
7.2 Conclusions of Problem 2

<!-- b000428 | prose | pages [22] -->
The occurrence of large area fires is closely related to the occurrence of extreme  high temperature weather. Consequently, the higher the temperature is, the more

<!-- b000429 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000430 | prose | pages [22, 23] -->
关注数学模型 likely fires are to occur, and the increase rate of the number of fires is faster.

<!-- b000431 | furniture | pages [22] -->
2

<!-- b000432 | furniture | pages [22] -->
MATHmodels

<!-- b000433 | furniture | pages [22] -->
获取更多资讯

<!-- b000434 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000435 | furniture | pages [23] -->
Team # 2127300

<!-- b000436 | furniture | pages [23] -->
Page 21 of 20

<!-- b000438 | prose | pages [23] -->
After forecasting the number of fire sites in the next decade, the maximum is  2698.14 in the maximum case, which is about 8.84% more than the maximum in the data of 2019-2020. 微信公众号：数学模型

<!-- b000439 | caption | pages [23] -->
Table 6: The results of problem 2

<!-- b000440 | prose | pages [23] -->
Types of drones Price Number SSA drones 10,000(AUD) 48 Radio-repeater drones 10,000(AUD) 27 Total expense：750,000 The increase of equipment cost: 210,000

<!-- b000441 | heading | pages [23] -->
7.3 Conclusions of Problem 3

<!-- b000442 | caption | pages [23] -->
Table 3: The longitude and latitude of each locations of the radio-repeater drones

<!-- b000443 | prose | pages [23] -->
Num. Lat Lon Num Lat Lon 微信号：MATHmodels 1 9 -38.00177382 146.3194898 -37.92946048 146.4085731 2 10 -37.99273465 146.3306252 -37.92042131 146.4197085 3 11 -37.98369548 146.3417606 -37.91138215 146.430844 4 12 -37.97465632 146.352896 -37.90234298 146.4419794 5 13 -37.96561715 146.3640314 -37.89330381 146.4531148 6 14 -37.95657798 146.3751669 -37.88426465 146.4642502 7 15 -37.94753882 146.3863023 -37.87522548 146.4753856 8 16 -37.93849965 146.3974377 -37.86618631 146.486521

<!-- b000444 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000445 | prose | pages [23, 24] -->
关注数学模型 Budget Request

<!-- b000446 | furniture | pages [23] -->
2

<!-- b000447 | furniture | pages [23] -->
MATHmodels

<!-- b000448 | furniture | pages [23] -->
获取更多资讯

<!-- b000449 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000450 | furniture | pages [24] -->
Team # 2120188

<!-- b000452 | prose | pages [24] -->
Dear official: 微信公众号：数学模型 In 19-20 Australia bushfire season, intense fire events occurred in many parts of the country, which resulted in economic losses and human casualties, even some firefighters and volunteers left us. Besides, the continuous fire caused immeasurable damage to the ecological environment. Victoria is one of the states suffering from the fire event significantly.

<!-- b000453 | prose | pages [24] -->
CFA is an organization, which offers volunteer fire service to the state Victoria. After this fire, in order to ensure the safety of firefighters and enhance the capability of fighting fire, CFA intends to improve bushfire response system. Through analysis, a strategy about the collaboration of forward teams, drones and EOCs has been proposed. To specify, two kinds of drones are included in the system, SSA drones and radio-repeater drones. 微信号：MATHmodels SSA drones are equipped with high definition & thermal imaging cameras and telemetry sensors, so they are capable of sending image data to wearable devices on front-line personnel. In this way, the forward teams are more aware of the fire situations nearby，which can not only speed up the process of fighting fire but also allow forward teams to respond to potentially dangerous situations in a timely manner.

<!-- b000454 | prose | pages [24] -->
Radio-repeater drones are able to sense radio signals and extend their range. By locating them properly, EOC and forward teams can communicate over long distances. Hence, the command scope of EOCs can be broadened CFA plans to set up a new division, "Rapid Bushfire Response", the purpose of which is to respond to and take action in the event of a fire quickly by implement of the system. Therefore, we need to purchase the drones in advance.

<!-- b000455 | prose | pages [24] -->
We have established the Optimal Purchase Plan Model to determine the numbers and mix of SSA drones and Radio Repeater drones.

<!-- b000456 | prose | pages [24] -->
A detailed budget for the expense is attached below: Types of drones Price Number SSA drones 10,000(AUD) 30 Radio-repeater drones 10,000(AUD) 24 Total expense：540,000 (AUD) We hope that the funds will be released before the next fire season. Please let me know if you need further information.

<!-- b000457 | prose | pages [24] -->
Yours Sincerely

<!-- b000458 | furniture | pages [24] -->
Team #2127300

<!-- b000459 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000460 | prose | pages [24] -->
关注数学模型

<!-- b000461 | furniture | pages [24] -->
2

<!-- b000462 | furniture | pages [24] -->
MATHmodels

<!-- b000463 | furniture | pages [24] -->
获取更多资讯

<!-- b000464 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000465 | furniture | pages [25] -->
Team # 2120188

<!-- b000466 | heading | pages [25] -->
7. References

<!-- b000467 | references | pages [25] -->
[1] https://www.weforum.org/agenda/2020/01/australia-bushfires-size-impact-wildlife-emissions/

<!-- b000468 | references | pages [25] -->
[2] https://www.parrot.com/en/drones/anafi-thermal

<!-- b000469 | references | pages [25] -->
微信公众号：数学模型

<!-- b000470 | references | pages [25] -->
[3] Department of Agriculture and Water Resources. Australia’s State of the Forests Report

<!-- b000471 | references | pages [25] -->
[4] http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=136&p_display_type=d

<!-- b000472 | references | pages [25] -->
ailyDataFile&p_startYear=2002&p_c=-1416074956&p_stn_num=84145

<!-- b000473 | references | pages [25] -->
[5] https://www.kaggle.com/carlosparadis/fires-from-space-australia-and-new-zeland

<!-- b000474 | references | pages [25] -->
[6] En Mu. The Effect of Hilly Terrain on Radio Communication. Mobile Communication. 1996

<!-- b000475 | references | pages [25] -->
(4): 35-36.

<!-- b000476 | references | pages [25] -->
[7] https://storymaps.arcgis.com/stories/9ebbe1b54dc847f2a7dd01917c9f3071

<!-- b000477 | references | pages [25] -->
微信号：MATHmodels

<!-- b000478 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000479 | references | pages [25] -->
关注数学模型

<!-- b000480 | furniture | pages [25] -->
2

<!-- b000481 | furniture | pages [25] -->
MATHmodels

<!-- b000482 | furniture | pages [25] -->
获取更多资讯
