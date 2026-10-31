MCM/ICM

Summary Sheet

Abstract

To better deal with fires, a new fire response system with drones has been proposed. We use the optimization model to discuss several problems with drones.

For problem 1, it is an optimization problem to minimize the equipment cost and maximize the efficiency and safety of fighting fires. First, we choose the fire data of Victoria state on January 4, 2020, when the areas of fires are largest. Then we grid the fire areas and evaluate the fire in each grid by the correlation coefficient of the fire frequency, brightness, and temperature. Next, we analyze the radio wave propagation loss and get the relationship of the communication range of the repeater drones and

the terrains. Based on the assumption that SSA drones are equivalent to the forward teams, 3 shifts of SSA drones are needed to cover the forward teams uninterruptedly for each mobile EOC. By genetic algorithm, we get the required numbers of repeater drones is 24 and the number of SSA drones is 30. Therefore, the total budget is $540,000(AUD).

For problem 2, we first train the LSTM model to predict the temperature in the next decade. By the regression analysis of the relationship between the number of fire sites and the daily temperature, we predict the fire situation, and the maximum number of fire sites is 2698.14, which 8.84% larger than the number in problem1. Then, according to the fire distribution in the source data, the fire area is diffused by the proportion to get the simulation of extreme fire conditions. Substituting the simulated fire map into the model, new results were obtained: the number of relay stations increased to 27, and the number of SSA increased to 48, with an increase of 30,000 and 18,000, respectively, for a total increase of 210,000(AUD).

For problem 3, according to Radio Wave Propagation Loss Model, repeater drones should be located near a high mountain. By limiting the distance between mobile EOC and higher mountains, the search model of a pair of mobile EOC was optimized to find 9 mobile EOC. Then, the range of the repeater drones is limited according to the terrain features, and the communication range is calculated according to the terrain features of its position. We make the optimized genetic model, to finding out that the number of repeater drones is 16, and calculate the corresponding longitude and latitude of the drones as well.

To assess the stability of our model, we change the value of drones’flight altitude and discuss its influence. It turns out that the changes have little effect on the final result and the model is relatively stable.

关注数学模型

1. Introduction

1.1 Background

微信公众号：数学模型 Australia is one of the countries with a high incidence of bushfires. From 2019 to 2020, Australia has been suffering from bushfires for more than four months, which not only led to serious economic losses and casualties but also posed a threat to global ecological security.

微信号：MATHmodels

The development and modification of technologies has greatly expanded the ways of dealing with fire events. For example, drones are widely used in fighting fires nowadays. Compared with the traditional means of disaster relief, the function of monitoring fire and transmitting signals offered by drones can broaden the range of fire detection and played a positive role in ensuring the safety of front-line personnel. In addition, collaboration among drones, front-line personnel and EOCs can help improve the effectiveness of fighting fires.

1.2 Problem Restatement

A bushfire response system composed of drones, front-line personnel and EOCs is proposed to enhance the capability of fighting fires. Considering the restrictions identified with the problem statement, we need to address the following problems:

1. Design a model to determine the optimal purchase plan of SSA drones and radio-repeater drones for a new division of Victoria’s CFA.

2. Adapt the model of problem 1 to the likelihood of extreme fires in the next decade and get the increase in the cost of equipment.

3. Design a model to determine the optimal locations of hovering VHF/UHF radio-repeater drones and take terrains and fire sizes into consideration.

1.3 Our work

Due to the proliferation of wildfires in Australia last year, the fire department's need to deal with fires in a timely manner has increased. At the same time, because of the complex terrain of the mountain, it has become more critical to assist firefighters in handling the fire through drones.

For problem 1, it is required to find the best match between the number of drones equipped with SSA and the number of repeater drones in consideration of safety,

关注数学模型 economy, observation and communication capabilities, terrain, fire size and frequency. ratio. That is, consider how to reasonably arrange the actions of the drones to make it have the highest fire handling capability and minimize the overhead.

For problem 2, we need to predict the fire situation in the next ten years based on 微信公众号：数学模型 past data, and consider the impact on extreme fire conditions on our previous model, that is, optimizing the previous model based on the extreme fire situation, and analyzing the changes in the results.

For problem 3, the existence of repeater drones makes it easier for frontline personnel to keep in touch with EOC. However, due to the complex terrain of the mountain, it will cause loss of wireless signal propagation, so a suitable position of repeater drones should be found, which can minimize the loss, in turn to make the fire department more capable of handling wildfires.

2. Assumptions and Justification

The maximum flying height of drones is 4000 m. We summarize the 微信号：MATHmodels parameters of common drones in the market.

There are several EOCs that can be sent to the fire scenes. The charging and whole-process control of drones depend on EOC, and the fire scope is generally wide, so EOC should be arranged in different fire areas to ensure timely disaster response.

It is the southeast wind in the fire season. The fire danger period was summer and autumn in Victoria [3], when southeast winds prevail in Victoria.

The temperature of the measuring point can represent the temperature of the whole fire area. The selected Orbost location is close to the fire area.[4] The range where SSA drones can observe is equivalent to the mobile range of front-line personnel. In this way we can see the SSA drones as forward teams, which can simply the problem and ensure the safety of front-line personnel.

3. Notations

Symbols Description ݔ map abscissa ݕ map ordinate the fire evaluation value of the corresponding area ݔݕ the frequency of fires in the corresponding area ݔݕ the temperature of the corresponding area measured by satellite ݐ݁݉ ݔݕ the brightness of the corresponding area measured by satellite 쳌䁐݃ ݐݔݕ

weighting coefficient of temperature ͳ weighting coefficient of brightness ʹ the evaluation value of the whole fire range ݐ݋ݐݐ ܤ the equipment cost (AUD)

关注数学模型 ɉ݂݀ the length of the waves the range of wireless communication frequency dimensionless parameters V 微信公众号：数学模型 ߛͳ the horizontal distance between the radio-repeater drone and the mountain (Figure 5) ߛʹ the horizontal distance between the EOC and the mountain (Figure 5 ) relative altitude (Figure 5) signal loss L ܮ݋ݏ݀쳌݋݋݁ the signal strength of the radio-repeater drones ܣഥ average altitude the distance between a fire site and the EOC D ݐݐ time required for SSA drones to arrive at a specific fire site ܦݐ the distance between the SSA drones and a specific fire site ݐ time required for the radio-repeater drones to arrive at a specific 微信号：MATHmodels fire site ܦ the distance between the radio-repeater drones and a specific fire site ݐݏ the detection time of the drones ݐ the charging time of the drones the number of mobile EOCs N ݋݉݀݉ the number of the radio-repeater drones the distance between the radio-repeater drones and the mobile EOCs the moving range of forward teams 쳌 the rang of a radio-repeater drone 쳌䁐 the range of a handheld radio the projected length of the fire along the 45° counterclockwise line l݈ of the X-axis as the fire action moves northwest the longest projection length within the control range of each ݔݐ mobile EOC ݋ݏݏݐ the number of SSA drones needed to cover the longest projection length within the control range of each mobile EOC 쳌ݏݏݐ the detection range of a single SSA drone ݐ temperature ሺݔ ǡ ݕ ሻ the coordinate of high mountains ሺݔ݁ǡ ݕ݁ሻ the coordinate of a mobile EOC ݉݀ the height of a mountain that can block the path of a repeater drone's wireless signals horizontal distance from the repeater drone to the mountains which can block the path of a repeater drone's wireless signals

关注数学模型

4. Models and Solutions

4.1 Optimal Purchase Plan Model

微信公众号：数学模型

4.1.1 Analysis of Problem 1

The objective of problem 1 is to determine the optimal number and mix of SSA drones and Radio Repeater drones to purchase on the basis of considering relevant factors. We conclude 6 factors from the problem background, including safety, economy, fire size and frequency, observation range, communication ability, and terrain. Therefore, it is essentially an optimization problem.

The relevant factors are described as follows:

Safety: the signal of the front-line personnel can be captured by the SSA drones.

Economy: the cost of the drones should be as low as possible. 微信号：MATHmodels Observation range: the area of fire that can be observed by SSA drones should be as large as possible.

Communication ability: the area of fire that can be covered by the range of radio-repeater drones’ signals should be as large as possible.

Terrain: mountains can influence the coverage area of SSA drones by affecting the radio communication range of the front-line personnel and the radio-repeater drones.

Fire size and frequency: The parameters of the fire area detected by the satellite, such as temperature, brightness, confidence, etc., can be used to evaluate the fire of the corresponding area We gain the data of fire in Australia in 2019-2020. [5] In order to ensure a control ability of wildfires, we select January 4, the day with the largest active fire coverage area from October 2019 to July 2020, as the reference standard. The fire coverage area on that day is shown in the Figure 2.

关注数学模型

4.1.2 Problem Visualization

We gain the state of Victoria's longitude and latitude of the elevation data and take 1 km as the sampling interval. Then we carry out planarization and meshing to 微信公众号：数学模型 construct a specific topographic map.

We choose the eastern part of Victoria to carry on our research. The visualization result of the fire coverage area on January 4 is as Figure 3.

微信号：MATHmodels

The yellow areas in Figure 3 indicate the frequency of fires ݔݕ.

We define ݔݕas the fire evaluation value of the corresponding area, and the

expression is:

ͳ ή ݐ݁݉ ݔݕ൅݇ ʹ ήܾ쳌䁐݃ ݐݔݕ ݔݕൌܲ ݔݕή݇

݀݋ݐ ʹ ൌͳܲ ͳ ൒Ͳ， ʹ ൒Ͳ，݇ͳ ൅݇

ݔݕ——the frequency of fires in the corresponding area

ݐ݁݉ ݔݕ——the temperature of the corresponding area measured by satellite

쳌䁐݃ ݐݔݕ——the brightness of the corresponding area measured by satellite

ͳ——weighting coefficient of temperature ʹ——weighting coefficient of brightness

The higher the brightness is, the greater the value of ݔݕwill be, which means

the fire is more serious.

关注数学模型 Therefore, the problem 1 can be transformed into: determine the optimal number and mix of SSA drones and Radio Repeater drones to maximize the evaluation value of the fire range ݐ݋ݐݐ݈that can be detected and minimize the cost ܤ.

According to the coverage area of the fire on January 4th, the elevation data 微信公众号：数学模型 corresponding to the areas where the fire sites are searched. Fire sites means the squares in fire after we put the map behind grids.

The visualization results are as follows:

微信号：MATHmodels

In Figure 4, the yellow parts represent the areas of higher ground and the blue parts represent areas of lower ground.

It can be seen that the overall altitude of the region is not very high. The highest place is only 2km high, and the flying altitude of the drones can reach 4km. As a result, the drones do not need to go around to avoid mountains.

4.1.3 Radio Wave Propagation Loss Model

However, the complexity of the terrain will affect the communication coverage of the handheld radio of the forward teams and the radio-repeater drones. The influence of the peak landform on the radio waves can be roughly divided into the following two ways:

waves [6] According to the DEM, there are only 1 or 2 peaks per 20km on average within the range of the radio-repeater drones, so only single peak loss needs to be considered.

关注数学模型 The relationship between signal loss and propagation distance is as follows:

32 . 44 20 lg ( ) 20 lg ( ) Los d km f MHz   

Introduce dimensionless parameters V with the expression below: 微信公众号：数学模型 2 1 1 ( ) V h         If h is positive, then the wireless signal propagation path is blocked by the mountain and V is negative.

If h is negative, then the wireless signal propagation path is not blocked by the mountain, and V is positive.

The relationship between signal loss L and V is as follows:

0 , 8.0 dB V    20 lg( 5.0 .0 62 ), 0 8.0 V V      .0 95 V 20 lg( 5.0 ), 1 8.0 e V    L   微信号：MATHmodels 2 20 lg( 4.0 .0 1184 ( 1.0 .0 38 ) ), 4.2 1 V V          .0 225 20 lg( ) 4.2 V     ， V  According to the communication range of the radio-repeater drones, the signal strength can be calculated as ܮ݋ݏ݀쳌݋݋݁ൌ䇅͵Ǥʹ䇅͵⺁݀ܤ.

Assuming that the flying altitude of the drones is 4km.

In Figure 6, when the mountain peak is just not occluding the repeater to transmit .0 03 4 8 L dB wireless signals, we can obtain that   and the radio-repeater drones’ communication range is approximately 18.5km. Since the heights of the peak are under 2km, there is no need to consider the influence of communication range when the peak is within the distance of 10km of the radio-repeater drones.

Additionally, the average altitude of this region is ܣഥൌ551.8km, so the loss L can be obtained, L=-16.55dB. Based on the radio wave propagation loss model, when the terrain is relatively complex, the communication range of the radio-repeater drones is approximately 18km.

4.1.4 The Relationship between SSA Drones and Front-line Personnel

The role of the SSA drones is to detect information on the front-line personnel's wearable devices, so we can assume that:

The range where SSA drones can observe is equivalent to the mobile range of front-line personnel.

The observation range of a single SSA drone is equivalent to the radio

关注数学模型 communication range of front-line personnel.

The observation range of SSA drones need to cover the entire front-line personnel.

The maximum flight time of a single SSA drone is 2.5 hours, and it can start 微信公众号：数学模型 again after 1.75 hours of charging time.

The maximum distance between an SSA drone and an EOC is 30km.

Consequently, in the optimization process, we can ignore the marching process of front-line personnel and directly consider how to maximize the coverage of the fire observation area by SSA drones.

For a fire that D km away from the EOC, the time required for SSA drones to arrive at the place is / ( ) t D v hours a  , a and the time for return is / ( ) t D v hours b  . b 微信号：MATHmodels The detection time is ݐݏand the charging time is ݐܿ.

In order to ensure the full coverage of front-line personnel by SSA drones, in the light of the relationship among SSA drones, the full coverage of front-line personnel in any region can be achieved when the number of SSA is 3. The analysis process is shown in the Figure 7.

4.1.5 Finding the Location of EOCs by Genetic Algorithm

To determine the optimal number and mix of SSA drones and Radio Repeater drones, it is necessary to assume the optimal location of mobile EOCs based on fire distribution and the severity of each fire area, the purpose of which is that the evaluation of the fire range that they control can be as high as possible.

The fire distribution diagram is shown in Figure 8.

关注数学模型 微信公众号：数学模型

The number of EOCs to be moved and the corresponding position can be 微信号：MATHmodels calculated using Genetic Algorithm. The algorithm is as follows:

(1) Establish a feasible solution set

We first determine the set of feasible solutions. Each mobile EOC has different positions (x, y), which can be represented by two sets of sequences. We assume that the number of mobile EOCs is n:

[ , ,..., ], [ , ,..., ] x x x y y y 1 2 1 2 n n

(2) Coding For an initial sequence string, the string is treated as a DNA sequence and manipulated genetically. Initialization is done by randomly generating a range of numbers.

(3) Calculate fitness The fitness is the objective function. In this subproblem, the objective function is to maximize the sum of the disaster evaluation value ݔݕcovering the fire area.

The samples with higher fitness are excellent samples, and vice versa.

(4) Select excellent samples as the parent generation Through the way of roulette to realize the choice of the parent generation, the specific steps are as follows:

Step1: sum the fitness of the population.

Step2: calculate the proportion of each sample in the sample sum as the probability, and obtain the cumulative probability in turn.

Step3: Generate a random number between 0 and 1. If the random number falls into the region of accumulative probability, select the sample from the region as the parent generation.

Step4: Run until the number of parent generations meets the conditions.

(5) Cross

关注数学模型 After obtaining the father generation samples, two of the father generation samples are selected to cross each other to produce offspring. Two crossing points are selected for each combination to exchange the DNA between the two crossing points, which is the so-called inheritance. 微信公众号：数学模型 Selecting a good parent for inheritance will also make the offspring have the good genes of the father.

(6) Variation Only crossover operation will make the objective function converge to a local optimal solution. So mutation needs to be set to make the gene mutation of a node in the DNA, which is beneficial to ensure the diversity of the population.

(7) Iteration Repeat the iteration to make the population finally reach the optimal state, the resulting population is the optimal solution.

The location of mobile EOCs found by Genetic Algorithm is shown in Figure 9.

微信号：MATHmodels

The red circles represent mobile EOCs. The fitness curve is as follows:

关注数学模型

4.1.6 Finding the Locations of Radio-repeater Drones by Genetic

Algorithm

微信公众号：数学模型 We can use the method in 4.1.5 to formulate the locations and number of the radio-repeater drones, so as to minimize the number of the radio-repeater drones and maximize the evaluation of the fire area covered by its communication range.

Through Genetic Algorithm, the locations and communication range of the Radio-repeater Drones are solved as shown in the Figure 11.

微信号：MATHmodels Figure 11：The locations and communication range of radio-repeater drones The red circle represents the location of the radio-repeater drones, and the white circle represents their communication range.

According to the relationship between the number of the radio-repeater drones (݋݉) and the distance between them and the mobile EOCs (݀ ):

,2 13 5. ( ) d km   m n   m ,3 13 5. ( ) d km   m As a result, the number of the radio-repeater drones is 24.

4.1.7 Finding the Number of SSA Drones

Given the preset location of the radio-repeater drones, it is possible to figure out how far the SSA's drones can detect a fire, which indicates the moving range R of forward teams.

R r r   m i 쳌݉——the range of a radio-repeater drone 쳌䁐——the range of a handheld radio The fire range that the SSA drones can detect is shown in the Figure 12.

关注数学模型 微信公众号：数学模型

微信号：MATHmodels Because wind direction for the southeast wind on January 4, fire action tends to be from southeast to northwest direction. So, calculate the projected length l of the fire along the 45° counterclockwise line of the X-axis as the fire action moves northwest. The longest projection݈݉ݔݐwithin the control range of each mobile EOC corresponds to the maximum number ݋ݏݏݐof SSA drones needed:

3 max / n l r  ssa ssa

쳌ݏݏݐis the detection range of a single SSA drone, and the number of SSA drones required is 30.

The required budget is:

10000 * 540000 B n n    (AUD) （ ） m ssa To sum up, a detailed budget for the expense is attached below:

Types of drones Price Number SSA drones 10,000(AUD) 30 Radio-repeater drones 10,000(AUD) 24 Total expense：540,000

4.2 Adaptation of Optimal Purchase Plan Model

4.2.1 Prediction of Extreme Fire Events over the Next Decade

The occurrence of forest fires is related to many factors, like long-term warming, rainfall deficiency and oceanic circulation anomalies. Among all these factors, temperature has a dominant influence on fire susceptibility for a land area. For example, Australia suffered from severe bushfires in 2019-2020, and at the same time,

关注数学模型 the Australian Bureau of Meteorology has placed 2019 as the hottest year on record so far [7]. So, we make fire predictions based on temperature. 1.Temperature forecast for the next decade According to the areas where the fire occurred, we select the temperature data of 微信公众号：数学模型 the observation point in the eastern part of Victoria State, and it is assumed that the data of the observation point could represent the temperature of the whole fire area. The daily maximum and minimum temperature data from 1938 to 2020 were processed preliminarily. After analyzing the seasonal variation and overall trend of the temperature data, we choose the linear interpolation method to complete the missing data. Due to the long time period to be predicted and the large sample size of original data, we train the LSTM model to predict the temperature in the next decade. The specific training process and prediction results are shown in the Figure 13, 14.

微信号：MATHmodels

关注数学模型

2. Fire events forecast for the next decade

Because the data of the fire sites measured by the MODIS satellite is distributed by date, to align it with the temperature data, we screen out the date of the fire situation, and then count the number of fire sites on that date. After putting these data 微信公众号：数学模型 in chronological order, we find out the temperature data of the corresponding date, and put them into the same table, which makes it easier to analyze the relationship between the temperature and fire sites.

After normalizing the data between August 2019 and January 2020, we compare the number of fires per day with the temperature and show them in the Figure 15.

微信号：MATHmodels

It can be found that the occurrence of large area fires is often related to the occurrence of extreme high temperature weather. Consequently, the higher the temperature is, the more likely fires are to occur, and the increase rate of the number of fires is faster. In this case, we use cftool in Matlab for regression analysis, and choose exponential curve as the fitting method for the relationship between fire and temperature. After calculating the coefficient in the case of minimum error sum of squares, we substitute the inverse normalization to obtain the following relationship.

ͳ͵Ǥ䇅㐲 ݐ ݐൌͳǤͲʹͶ ൈ ൈʹͶ͹㐲݂ Ͷ͵Ǥͳ ݐ represents the number of fire sites in Victoria at temperature ݐ.

According to the above expression and temperature data of the next decade, we can estimate the corresponding number of fire sites. Due to the need to consider the cost increase in extreme phenomena, we choose the maximum number of possible fire sites for the study. The number of fire sites is 2698.14 in the maximum case, which is about 8.84% more than the maximum in the source data. (Source data refers to fire data of Victoria state in 2019-2020.)

4.2.2 Finding the Number of SSA Drones

We only get the total number of fire sites through prediction, which is not enough for us to determine the locations of the drones. So, we use the largest range of fire site conditions in 19-20 years to simulate the possibility of a large fire in eastern

关注数学模型 Victoria under future extreme conditions. In the case that the expansion ratio of the fire area relative to the source data has been worked out, we take the fire map of January 4, 2020 as the sample, and expand the fire area to 1.0884 times of the original on this basis. 微信公众号：数学模型 In order to realize the simulation of fire spread, we first draw the boundary range of the fire map on January 4, 2020 as a reference, as shown in the following Figure 16.

微信号：MATHmodels

After the calculation of the fire area in the source data, we calculate the spread the fire area according to the proportion. On the basis of the Figure 15, we expand the area of fire, to simulate extreme fire situation may arise in the next decade. In accordance with the same probability to the spread of fire to fill in the form of grid fire beyond boundaries, we finally form a new fire situation map in Figure 17.

关注数学模型 According to the fire situation data after expansion, the Optimal Purchase Plan Model is modified to solve the problem. It is found that the EOCs’ locations remain unchanged, while the number of radio-repeater drones and SSA drones changes as follows: 微信公众号：数学模型 The number of radio-repeater drones increases from 24 to 27, and the number of SSA drones increases from 30 to 48. In this case, the equipment cost increases by 30,000 and 18,000 respectively, with a total increase of 210,000(AUD).

Types of drones Price Number SSA drones 10,000(AUD) 48 Radio-repeater drones 10,000(AUD) 27 Total expense：750,000 The increase of equipment cost: 210,000

4.3 Optimal Location of Radio-repeater Drones Model

微信号：MATHmodels

4.3.1 Analysis of Problem 3

Problem 3 is essentially the optimization of the location finding process of the radio-repeater drones in the modeling process of Problem 1. To specify, the model has to be modified to adapt to fires of different size on different terrains.

According to 4.2.1, when the wireless signal of the radio-repeater drones is just not blocked by the mountain, the communication range is about 18.5km. When there is diffraction during the transmission of the signal, it can be known by calculation that the diffracted signal can propagate far less than 1km. Therefore, diffraction happens, the communication range can be regarded as the horizontal distance between the radio-repeater drones and mountains.

To make the communication range of the radio-repeater drones as large as possible, high mountains should be in the circle of the 10km radius of the radio-repeater drones. At the same time, high mountain should not appear within the range of 10-20km of the radio-repeater drones. In this way, mountains have no effect on the communication range of the drones.

This constraint condition is added into the Optimal Purchase Plan Model. We take the fire occurred from October 1, 2019 to January 7, 2020 as the fire range for solving, aiming at simulating the optimal locations of radio-repeater drones for fires of different sizes on different terrains.

4.3.2 Problem Visualization

The areas covered by the wildfire between October 1, 2019, and January 7, 2020 is shown in Figure 18.

关注数学模型 微信公众号：数学模型

微信号：MATHmodels January 7, 2020 The corresponding DEM is shown in Figure19:

2019, and January 7, 2020

4.3.3 Model Establishment Based on Genetic Algorithm

First of all, in order to prevent the radio-repeater drones from higher mountains, the mobile EOC should be near high mountains instead. Thus, the following constraints are added to the search model of the mobile EOCs:

2 2 2 ( ) ( ) 20 x x y y     h e h e

x , x , h y e y ( ) is the coordinate of a high mountain, and ( ) is the coordinate of mobile h e

EOCs.

关注数学模型 Based on the Optimal Purchase Plan Model, the assumed locations of mobile EOCs are solved by Genetic Algorithm, which are shown in Figure 20.

微信公众号：数学模型 微信号：MATHmodels

For the communication range of the radio-repeater drones, the following constraints are added:

ʹͲǡ݀ ൑ͳͲ ͳ䇅Ǥ⺁ǡ 쳌 ൌ Ͷ ൌʹͲ െ݀ ʹͲ 쳌ͳǡͳͲ ൑݀ ൑ʹͲ ݉——the height of a mountain that can block the path of a repeater drone's wireless signals݀ ——horizontal distance from the repeater drone to the mountains which can block the path of a repeater drone's wireless signals The optimized Genetic Algorithm is used to solve the locations of the radio-repeater drones, and the obtained locations are shown in Figure 21.

关注数学模型 The corresponding longitude and latitude are shown in Table 3.

Num. Lat Lon Num Lat Lon 1 9 -38.00177382 146.3194898 -37.92946048 146.4085731 微信公众号：数学模型 2 10 -37.99273465 146.3306252 -37.92042131 146.4197085 3 11 -37.98369548 146.3417606 -37.91138215 146.430844 4 12 -37.97465632 146.352896 -37.90234298 146.4419794 5 13 -37.96561715 146.3640314 -37.89330381 146.4531148 6 14 -37.95657798 146.3751669 -37.88426465 146.4642502 7 15 -37.94753882 146.3863023 -37.87522548 146.4753856 8 16 -37.93849965 146.3974377 -37.86618631 146.486521

5. Sensitivity Analysis

微信号：MATHmodels

5.1 Radio Wave Propagation Loss Model

Since the topic do not give the flying altitude of the drones, after consulting relevant data of drones’ performance and radio signal transmission, as well as the terrain analysis of Victoria, we assume that the flying altitude of the UAV in the model was constant at 4km. At this point, in the case of single peak loss, the signal range of the repeater will decrease from 20km to 18km when the terrain is relatively complex, according to the relevant calculation.

In order to analyze the stability of the model under this hypothetical condition, we consider modifying the flying altitude of the drones. Taking 0.2 as the change value, we take 3.6km,3.8km,4.2km and 4.4km as the new conditions to calculate the signal range of the radio-repeater drones. The results are shown in the Table 5

Flight Altitude ͵Ǥh ͵Ǥ䇅 ͶǤͲ ͶǤʹ ͶǤͶ ( ) Signal Range ͳ͹Ǥʹ 17.5 ͳ䇅ǤͲ ͳ䇅Ǥ͵ ͳ䇅Ǥ͹ ( ʹ) When the drones’ flight height is increased by 5%, the signal range will be increased by 1.67%. At the same time, when flying height is decreased by 5%, the signal range will be decreased by 2.78%. So the scope of the change is not big.

Consequently, the flight height has little effect on the monitoring scope of the radio-repeater drones. The number of the drones mainly depends on the size and frequency of fires, and terrains.

The influence of flight altitude on the results is within the acceptable range, and the model created above is relatively stable on the whole based on the current hypothesis.

关注数学模型

6. Strengths and Weaknesses

6.1 Strengths

微信公众号：数学模型 The comprehensive evaluation of the fire is completed with the parameters of  frequency, temperature and brightness, which makes the calculated coverage range of the drones more accurate and in line with the actual situation. Considering the overall value of fire evaluation and on the premise of ensuring  effectiveness, the scheme with the lowest cost can be solved by Genetic Algorithm. Moreover, the adaptability curve reaches the optimum under multiple iterations, indicating that the solution effect is good. In order to predict the future 10 years’ temperature, we chose LSTM model,  making both short-term and long-term memory network. The model is mainly to solve the gradient vanishing and gradient explosion problems in the training process of long sequence. Compared with ordinary RNN, LSTM has better performance in long sequence and more accurate prediction results. 微信号：MATHmodels

7.2 Weakness

 In problem 2, we ignored the change of the fire between areas and expand by proportion regarlessly. Thus the model is still an approximate on a large scale. This has doomed to limit the applications of it.  In the prediction the future fire event, we only used fire data in 2019-2020 for regression prediction, so data quantity is too little. Besides, There are many factors affecting fire, such as artificial fire fighting measures, etc., which reduce the accuracy of fire prediction. 7.Conclusions

7.1 Conclusions of Problem 1

Based on the Radio Wave Propagation Loss Model, when the terrain is complex,  the communication range of the radio-repeater drones is approximately 18km. In order to ensure the full coverage of front-line personnel by SSA drones, in the  light of the relationship among SSA drones, the full coverage of front-line personnel in any region can be achieved when the number of SSA is 3.

Types of drones Price Number SSA drones 10,000(AUD) 30 Radio-repeater drones 10,000(AUD) 24 Total expense：540,000

7.2 Conclusions of Problem 2

The occurrence of large area fires is closely related to the occurrence of extreme  high temperature weather. Consequently, the higher the temperature is, the more

关注数学模型 likely fires are to occur, and the increase rate of the number of fires is faster.

After forecasting the number of fire sites in the next decade, the maximum is  2698.14 in the maximum case, which is about 8.84% more than the maximum in the data of 2019-2020. 微信公众号：数学模型

Types of drones Price Number SSA drones 10,000(AUD) 48 Radio-repeater drones 10,000(AUD) 27 Total expense：750,000 The increase of equipment cost: 210,000

7.3 Conclusions of Problem 3

Num. Lat Lon Num Lat Lon 微信号：MATHmodels 1 9 -38.00177382 146.3194898 -37.92946048 146.4085731 2 10 -37.99273465 146.3306252 -37.92042131 146.4197085 3 11 -37.98369548 146.3417606 -37.91138215 146.430844 4 12 -37.97465632 146.352896 -37.90234298 146.4419794 5 13 -37.96561715 146.3640314 -37.89330381 146.4531148 6 14 -37.95657798 146.3751669 -37.88426465 146.4642502 7 15 -37.94753882 146.3863023 -37.87522548 146.4753856 8 16 -37.93849965 146.3974377 -37.86618631 146.486521

关注数学模型 Budget Request

Dear official: 微信公众号：数学模型 In 19-20 Australia bushfire season, intense fire events occurred in many parts of the country, which resulted in economic losses and human casualties, even some firefighters and volunteers left us. Besides, the continuous fire caused immeasurable damage to the ecological environment. Victoria is one of the states suffering from the fire event significantly.

CFA is an organization, which offers volunteer fire service to the state Victoria. After this fire, in order to ensure the safety of firefighters and enhance the capability of fighting fire, CFA intends to improve bushfire response system. Through analysis, a strategy about the collaboration of forward teams, drones and EOCs has been proposed. To specify, two kinds of drones are included in the system, SSA drones and radio-repeater drones. 微信号：MATHmodels SSA drones are equipped with high definition & thermal imaging cameras and telemetry sensors, so they are capable of sending image data to wearable devices on front-line personnel. In this way, the forward teams are more aware of the fire situations nearby，which can not only speed up the process of fighting fire but also allow forward teams to respond to potentially dangerous situations in a timely manner.

Radio-repeater drones are able to sense radio signals and extend their range. By locating them properly, EOC and forward teams can communicate over long distances. Hence, the command scope of EOCs can be broadened CFA plans to set up a new division, "Rapid Bushfire Response", the purpose of which is to respond to and take action in the event of a fire quickly by implement of the system. Therefore, we need to purchase the drones in advance.

We have established the Optimal Purchase Plan Model to determine the numbers and mix of SSA drones and Radio Repeater drones.

A detailed budget for the expense is attached below: Types of drones Price Number SSA drones 10,000(AUD) 30 Radio-repeater drones 10,000(AUD) 24 Total expense：540,000 (AUD) We hope that the funds will be released before the next fire season. Please let me know if you need further information.

Yours Sincerely

关注数学模型
