summary

Due to the drought of southeast Australia, forest fires burn across the country, impacting New South Wales and eastern Victoria. To help Victoria government response to future wildfire disasters, we established the ‘Rapid Bushfire Response’ system.

For model 1, to address the irregularity of fire regions and SSA drones’ information acquisition areas, we used regional discretization method, turning fire data and multi-drone cooperation in to constraint equations. We then divide the information in discreated area into different layers, the drone layer and information layer indicate an SSA drone’s different search mode and search zone, and the flame layer represents the severity of wildfire, we optimized SSA drone’s search pattern balancing information detection revenue and SSA drone numbers. Finally, we optimized the location of EOC and repeater with the further obtained SSA drone location while considering communication constrains and drones’ traveling distance.

For model 2, we discussed the changes in fire under global warming circumstances. We first formed a two-level function that maps temperature to average fire probability, and average fire probability to burned area size. To obtain the equation, we build cellular automata to simulate fire probability’s effect on burned area and fitted the relation between temperature and fire probability. We then estimated the temperature variance due to climate change from further studies and calculated the estimated average fire probability of this year and the next decade. Finally, we simulated average fire scenes and estimated their fire severity.

For model 3, while referring to the number of SSA drones obtained without terrain conditions, we refined the regional discretization model to bring into the terrain influence. For SSA drones, we considered topographical influence on a drone’s traveling time and discussed path planning considering the varying time cost of different areas. As for repeaters, we evaluated the influence of terrain on communication, and measures a regions’ communication shielding effect with the terrain’s second gradient. We then further considered the reliability of communication and estimated the schedule change in different terrains.

Based on the above three models, we estimated that 10 SSA drones and 2 radio repeater drones is required to build the ‘Rapid Bushfire Response’ system. For next decade, the cost of imaging cameras and telemetry sensors (for SSA drones) will increase. We also suggest that while fire zone area has an influence on drone arrangements, topographical conditions plays a less important role.

1 Introduction

1.1 Problem Background

微信公众号：数学模型 Since September 2019, mountain fires in Australia have been burning for more than 200 days, cover- ing an area of nearly 6 million hectares. The fire in Australia is equivalent to burning half of Jiangsu, three Beijing and two Belgium, which is 7 times of the Amazon rainforest fire that shocked the world (burning 900000 hectares of land), and 60 times of the California fire last year (burning 102000 hec- tares of land).

There were 39 fires in Victoria, the second most serious state, which destroyed 300 houses. The in- surance commission estimated the loss at a $700 million. Victoria is a state located on the southeast coast of Australia, and adjacent to South Australia and New South Wales in the north and west re- spectively. It is the smallest continental state in Australia. The northeast is a mountainous area with towering peaks, mostly between 1000 and 2000 meters above sea level.

Due to the extremely large wildfire and a great number of injured citizens and firefighters, the im- 微信号：MATHmodels portance of drone-detection system is found. It can be widely used in aerial photography, environ- mental detection and other fields, and has a huge industrial prospect [1]. For a sudden wildfire, no matter in the early or middle stage of a fire, we can detect real-time data and communicate with firefighters through UAV system.

1.2 Restatement of the Problem

We need to develop a wildfire disaster relief response system named “Rapid Bushfire Response” and improve its response capabilities based on the situations of Victoria, Australia.

⚫ What we Know:

➢ Distribution of wildfire severity of Australia ➢ Geographic information of Southeast Australia

⚫ What we Have:

➢ 2 kinds of drones. SSA drones are used for video & telemetry and Radio Repeater drones are used to extend the range of low power radios on the front lines.

➢ 1 mobile EOC. central command and control point for emergency related operations and ac- tivities, and for requests for activation and deployment of resources

⚫ What we Should Do:

➢ Determine the type and number of UAV. The UAV fleet should satisfy and balance the need of capability, safety and economics.

➢ Identify the most-demanded locations for SSA drones. SSA drones has the capability of video & telemetry so that they are the main part of UAV fleet to guarantee the safety of fire- fighters and the data of the most serious fire areas ➢ Identify the best hovering locations for radio-repeater drones. Radio-repeater drones are the core of several SSA drones to transmit information to EOC.

➢ Propose dispatching schedule. Assign flight plan to each type of drones to ensure the Con- tinuous information transmission.

关注数学模型 The simple structure of the “Rapid Bushfire Response” UAV system is shown in figure 1.1.

微信公众号：数学模型

1.3 Model Framework

In this paper, we establish three models to solve the problem. Firstly, because this model is estab- lished to monitor wildfire, and is incapable of monitoring the whole area. We define a variable to determine the observation revenue of UAV in a certain area in a certain period. Secondly, to balance 微信号：MATHmodels the capability, safety and economics, the number of SSA drones and the location of EOC are opti- mized by using the optimization model according to the size of the fire and the frequency of the fire. And we use the number of SSA drones to optimize the number and the location of ratio repeater drones. In the last, we built a model to simulate the size and scale of the possible wildfires in the next decade based on the Cellular Automata model. And then we substituted the predicted data to the model we built to testify whether model adapts to the changing likelihood of extreme fire events over the next decade. The overall algorithm flow chart of the model is shown in the figure 2:

2 Assumptions and Justifications

1. The UAV will not be damaged or malfunction during the mission.

Justification: The probability of UAV's sudden damage due to its own reasons during the mission is ignored.

关注数学模型 2. All drones can only be recharged in the Emergency Operations Center and they are fully charged when leaving the Emergency Operations Center.

Justification: Due to a large forest fire in the mission area, we conclude that the electrical equip- ment in the area is not working properly.

微信公众号：数学模型 3. All drones fly at the maximum speed of 20m/s until they reach the designated location.

Justification: This is because the drones has the limitation of flight time. Flying at the maximum speed can minimize the time consumed on the road to make the mission time as long as possible. 4. The ascending and descending process of UAV is not considered.

Justification: This is because drones have very short ascent and descent times compared to flight times. 5. The terrain and weather do not have influence in the performance of drones.

Justification: Because the drones are hovering well above the ground, the terrain doesn’t affect the speed and battery life of drones. Meanwhile, the influence of weather on the performance of drones is ignore. 6. The atmosphere temperature has no effect on the battery life of drones. 微信号：MATHmodels Justification: Because the drones are hovering well above the ground, the atmosphere temperature doesn’t affect the battery life of drones and battery life. 7. Each UAV is regarded as a particle in the model Justification: The shape, size and mass of UAV have no influence on the performance of drones. 8. The spread of the flame has nothing to do with the terrain.

Justification: For the cellular automata model, the probability of flame propagation from a certain area to all surrounding areas is the same. Therefore, this model ignores the influence of terrain on flame propagation. 9. In the next ten years, the temperature changes with time, and the humidity and wind speed do not change.

Justification: For 3 factors that affect the probability of fire propagation, the humidity and wind speed aren’t influenced by the global warming, which is regarded as constant value. And the tem- perature will increase slowly in the next decade.

3 Notations

3.1 Notations used in this paper

Symbol Description Unit

Maximum speed of drones km/hr

The element division method of the rectangular fire area, M is the num- - ber of elements of one side

S The number of the location of radio repeater -

关注数学模型 The range of low power radios on the front lines km

The range of radio repeater’s signal km

Maximum flight time hr 微信公众号：数学模型 Recharge time for the built-in battery of drones hr

The docking time of the drone in this area hr

km2 Coverage area of the detected area

km2 The area of the largest square that UAV can cover

Detection range of UAV km

The flight range of WileE-15.2X Hybrid Drone km

微信号：MATHmodels The location of Emergency Operations Center -

The location of radio repeater drone -

State variable indicating whether the SSA drone is in this area.

means the drone is in this area; means the drone is not in this - area.

State variable indicating whether the ratio repeater drone is in this area.

means the drone is in this area; means the drone is not - in this area.

The amount of information acquired by UAV in this area -

The severity of the fire in this area. -

Minimum transit time of the unit -

Sequence of UAV passing through units -

The state value of each unit area’s fire state in the cellular automata. -

UAV detection performance index -

Monitoring types of SSA drones -

The boundary parameter -

T Ground temperature in fire area (before fire) ℃

The influence factors in the cellular automata model. It will affect the - area and distribution of the fire

关注数学模型

4 Model Derivation

4.1 Model Preparation

微信公众号：数学模型

4.1.1 The Data

1. Data Collection

The data we used mainly include Elevation data of southwest Australia, Australian wildfire data set, Forest fire areas in Australia_ 2019-2020, Global Forest Watch. The data sources are summarized in

Database Names Database Websites Data Type Elevation data of southwest Australia https://topex.ucsd.edu/cgi-bin/get_data.cgi Geography https://www.kesci.com/mw/da- Australian wildfire data set Geography taset/5e21588a2823a10036b575bf 微信号：MATHmodels Forest fire areas in Australia_ 2019- https://www.datafountain.cn/datasets/5395 Geography 2020 Global Forest Watch https://www.globalforestwatch.org/ Geography https://github.com/var- FW_Veg_Rem_Combined unr89/smokey/blob/master/Wild- Climate fire_att_description.txt

2. Data Cleaning

According to the latitude and longitude range and the administrative boundary of Victoria, Australia, we extracted data of terrain and fire details of Victoria from all the data. The fire in Victoria is shown in the figure 3 below.

4.1.2 Geographic Coordinate System

We have collected the geographic coordinates (longitude and latitude) of Victoria. To find the true distance between any two points in the map, we map the spherical coordinate system to the plane rectangular coordinate system. With the latitude and longitude range of the fire area, a rectangular fire field area can be obtained in a rectangular coordinate system. The linear distance between any

关注数学模型 two points in the rectangular coordinate system is the actual distance between the two places.

微信公众号：数学模型

4.2 Model 1: SSA Drones Optimization Model

Due to area detection requirements, UAVs continuously monitor fire regions. However, limited by power and communication, it is impossible to detect all regions of interest continuously. Therefore, 微信号：MATHmodels We optimized the detection time of different regions according to their importance. [2]

4.2.1 Regional Discretization Model

We first discretize the area into a M×N matrix, each unit area is which is the minimum transmit area of 5-watt transmitters. We then divide the matrix in to 4 layers to analyze different information, the time layer (t, a matrix representing the hover time of the unit), the drone layer (x, a 0-1 state variable matrix representing a drone’s hovering zone and t, a matrix storing a drone’s hovering time), the information layer (I, a matrix representing the information SSA drones collected form the unit) and the flame layer (h vector representing the severity of wildfire). We combine these three layers to optimize the number of SSA drones and balance the capability and economics.

Considering a SSA drone’s power limitations, we hypothesize that a drone detects one or two block at once, hence a SSA drones has 5 different detection modes:

关注数学模型 微信公众号：数学模型 As we identify each detection mode with the position of its upper left corner, we could represent a

drones detection behavior by dividing the drone layer into 5 sub-layers, and . For drone

layers we have:

(1)

For the amount of information acquired by UAV in a certain area , we have:

(2) 微信号：MATHmodels For the variables in equation 1,

(3)

In multiple-goods-condition, we consider the drones optimization problem as a Multiple-objective

integer programming problem. Therefore, the objective function of the optimization model is

(4)

where represents the total number of SSA UAVs, Here serves as an threshold, It prevents the

algorithm from adding drones when a new drone’s contribution is smaller than , balancing economic needs and

fire zone detection. represents the detection revenue of SSA drones. is the severity of the

fire area (i,j), As “Boots-on-the-ground” Teams faces more danger in severe areas, The higher the value of , the

more valuable the information of this fire unit is. is calculated with emulations methods and will be further

关注数学模型 discussed in the next section.

4.2.2 EOC Constraint Conditions

微信公众号：数学模型 Apart from constrains with in the regional discretization model, we have

⚫ The EOC locates inside the discrete zone.

(5)

⚫ The EOC locates outside the fire.

(6)

Equation 6 casts no effect when is zero, yet when is not zero which indicates fire, it restrains from being zero, hence EOC will not be optimized in to firezone. 微信号：MATHmodels

4.2.3 Terrain Adapting Regional Discretization Model

To further adapt the integer programming discretization model, we introduced path planning to con- sider the cost of complex terrain. We assume that as SSA drones pass each area unit, it’s time cost varies according to the height change, hence we could brought in terrain information in the form of minimum passing time g. Furthermore to indicate a drone’s flying behavior, we introduced o, is zero when unit area (i,j) is not in the drone’s path, hence we have:

(7)

To ensure all are marked on the path ( is not zero only when is not zero), we have:

(8)

As a drone’s path is continuous, we must constrain the connectivity of matrix o’s non-zero elements. To achieve this, we restrict to be integer and gradually increases as SSA travels unit by unit, while appointing the starting point to be 1, we have:

(9)

While

(10)

The model could be optimized with the same target as the regional discretization model.

4.3 Model 2: CA Fire Prediction model

Considering the lack of spatial distribution data of fire field, we use cellular automata model to sim-

关注数学模型 ulate the fire field distribution in a rectangular area. In the simulation process, there are two parame- ters related to temperature. Considering global warming, these two parameters will change with time, thus affecting the area and distribution of fire field. Therefore, the model can be used to predict the fire distribution in the next ten years and optimize the number and types of SSA drones.

微信公众号：数学模型

4.3.1 Simulation of the Wildfire

1. Simulation Preparation

In order to build cellular automata to simulate the fire severity distribution, it is necessary to determine the state of the unit area. In this paper, we set up three states: after-burning, burning and unburned. And Considering the duration of combustion, this model defines a life for the fire of each point. If firing, the state value of this point decreases by 1 as time increases by 1. Therefore, . represents the unburned state; represents the burn- ing state, whose value represents the residual life of the unit; represents the after-burning state of the unit.

微信号：MATHmodels What’s more, note that the ‘unit area’ of this model is different from the ‘unit area’ in the previous model. The ‘unit area’ in this model is the subset of the ‘unit area’ in the previous model, representing the fire state in this area, thus determining the severity of fire in the larger ‘unit area’.

After determining the unit area state, we build a fire field, which is the same as the fire field in the previous model, but the division of unit area is different. The unit area is much smaller so that high accuracy can be obtained.

Next, considering the probability of unit fire in the fire region, whether a certain point in a fire is on fire at a certain time depends on the distance from the known ignition point. At each time, the ignition probability of each point is obtained by applying the gaussian filter of MATLAB to the whole matrix. When the probability value of the point divided by the critical probability value is large than the random number, then at this moment, the point becomes a new ignition point, that is, be- comes .

2. Simulation Method

The simulation algorithm is as follows: Firstly, the four points in the center of the fire site are set as fire, namely becomes . Secondly, the probability of a new fire point at the next mo- ment is calculated and compared with the critical probability to get the location of the new fire point. Thirdly, the state variable of ignition point, that is, the unit state value , minus one. Fourthly, judge the probability that the fire of all units will be extinguished. If the extinction proba- bility of the unit flame is less than the critical extinction probability, the state variable at this point becomes 0, that is, . Fifthly, update the burning-time matrix for judgment of flame severity. In the last, recalculate the ignition probability of all points. The specific algorithm flow chart is as follows.

关注数学模型 微信公众号：数学模型 微信号：MATHmodels

We can simulate the process of this year's Australian mountain fire through simulation, and the sim- ulation results are as follows

In this model, there exist two parameters, the critical fired probability and critical unfired proba- bility . These two parameters can decide the wildfire distribution. For the critical fired probability, the value of it is determined by the temperature before wildfire happens, which means it has a rela- tionship with the global warming. For the critical unfired probability, it’s the same for the different wildfire events for the decade. But the critical unfired probability will increase as the fire scale in- creases.

关注数学模型 As for how to determining the severity of the fire, we accumulate the time each point is burned and rescaled to 0-1 as fire are more severe at the starting point. We then transforms it into a M×N dimen- sional matrix to characterize the spatial severity distribution of the fire, which is the value we used for the last model. We can visualize this matrix as follows 微信公众号：数学模型

微信号：MATHmodels The lighter the color in the figure, the lower the flame severity of the unit.

4.3.2 The Influence of Global Warming on Wildfire Simulation

To analyze the impact of global warming on this model, we established the following relationships. Firstly, by traversing the critical fire probability from 0.7 to 0.95, we get the simulation results be- tween the critical fire probability and the fire area size. Then the relationship between the two varia- bles is determined by curve fitting tool of MATLAB, which is shown as below.

(11)

Through the fire data of this year's Australian fire, we can get the relevant data of the fire area and the average temperature of the area before the fire. By using the above formula (1.6), we can trans- form the fire area data into different probability value so that we can get the relationship between the critical fire probability and average temperature of the area.

(12)

Finally, when analyzing the relationship between time and temperature, the temperature we find that the change of temperature includes seasonal periodic change and long-term growth change. For the annual temperature prediction, we can ignore the seasonal periodic change of temperature. Therefore, the temperature in this area increases exponentially with time. Due to an average temperature rise of 1.5 degrees Celsius over the past 50 years, their relationship is as follows

(13)

关注数学模型 微信公众号：数学模型 (a) The relationship between the (b) The relationship between the (c) The relationship between the critical fire probability and the critical average temperature and critical time and the average wildfire area the fire probability temperature (global warming)

With all mentioned above, we can get the critical fire probability of this year and ten years later . Taking them into the simulation model, we can get the difference of fire dis- 微信号：MATHmodels tribution between this year and 10 years later. Finally, the demand change of UAV system can be determined.

4.4 Model 3: Ratio-Repeater Drones Optimization Model

Due to the continuity of communication requirements, the radio repeater UAV needs to hover at a certain position all the time as the intermediate of the signal. According to the location and number of the SSA drones. We can get the location and number of radio repeater drones by optimization model.

4.4.1 Influence of Terrain on Radio Range

Considering the influence of terrain on the drone communication, we extract terrain data from a fire region in Victoria. The matrix is denoted as . Laplace operator is used for the terrain data matrix to obtain the change amplitude of terrain is obtained. Then the rate of change data is converted into the signal transmission range data of the place. The specific transformation methods are as follows.

(14)

is the parameter make sure the range of value is . This matrix represents the signal receiving range of SSA drone at the fire region for each unit.

关注数学模型 微信公众号：数学模型

4.4.2 Radio Repeater Drones Optimization Model

微信号：MATHmodels

1. Optimization objective

The optimization object is sum of distance between ratio repeater and EOC.

(15)

2. Constraint Conditions

⚫ The distance between UAV and EOC is less than the flight distance of UAV.

(16)

⚫ Radio repeater drones can communicate with SSA drones.

(17)

4.4.3 Radio repeater drones scheduling scheme

For radio repeater drones, the reliability of communication needs to be considered, so we need to ensure that there is a ratio repeater drones at the position we get throughout the wildfire course. Therefore, when the drone needs to return for charging, another drone needs to replace it.

For the WileE–15.2X hybrid drone, hovering time and charging time of UAV determine how many UAVs are needed in this position as follow.

(18)

For the formula 13, we know that

关注数学模型 (19)

微信公众号：数学模型 To sum up, we can know the total number of radio repeater drones, namely, .

5 Test the Model

5.1 Model 1 Sensitivity Analysis

1. UAV detection performance index sensitivity analysis

For the model 1, UAV detection performance index depend on the detection range of the UAV. Dif- ferent detectors have different detection capabilities, and we can find out how different detection range will affect the number and distribution of UAVs in this model by solving different parameters 微信号：MATHmodels in its neighborhood range to testify the sensitivity analysis.

For the UAV detection performance index, we take 0.005 as the step size within the range of [0.01,0.03], and observe the effect of the change of the value on the model solution result. The results are shown in the following table:

Drone number

0.010 3

0.015 5

0.020 6

0.025 5

0.030 5

It can be seen from the results that when the value of λ is greater than a certain threshold, the number of UAVs solved by the model stabilizes at 5. It can be seen that the stability of the parameter is robust.

2 The boundary parameter sensitivity analysis

The boundary parameter measures the increase of costs by adding SSA drone. When the detection revenue is greater than the increased cost, continue to increase SSA drones; when the detection reve- nue is less than the increased cost, stop increasing SSA drones.

For the boundary parameter 𝛼, we use 0.1 as the step size in the range of [0.3, 0.7] to observe the influence of the change of its value on the model solution result. The results are shown in the table 4 below

关注数学模型 α Drone number

0.3 7 微信公众号：数学模型 0.4 6

0.5 6

0.6 4

0.7 3

It can be seen from the table that this parameter has a great influence on the result of UAV. It is known that this parameter has high sensitivity and poor stability. Based on the physical meaning of this pa- rameter, this is understandable. 微信号：MATHmodels

5.2 Model 2 Sensitivity Analysis

For cellular automata, due to the random simulation process involved in the model, any parameter value change may result in different fire field distributions, and multiple solution results of the same parameter value may also obtain different fire field distributions. Therefore, we can change the value of a certain parameter and solve the model twice for each value to verify the sensitivity of the model.

For the critical fire probability pf, we use 0.03 as the step size in the range of [0.74, 0.83] to observe the influence of the change of its value on the model solution result. The results are shown in the table 5 below:

Drone number Drone number pf (1st time result) (2nd time result) 0.74 10 10 0.77 6 6 0.80 6 5 0.83 4 4

It can be seen from the solution result that the change of the value of k has a greater influence on the

关注数学模型 solution result of the model, indicating that the sensitivity of parameter pf is high. Therefore, it is necessary to accurately simulate the value of k in the process of model building, otherwise the solution result will produce errors.

6 Conclusion

微信公众号：数学模型

6.1 Summary of Results

6.1.1 Result of Problem 1

Through cellular automata, according to the fire data of the Australian fire, we can get the distribution of one of the fires as follows, where the critical fire probability is . We ran five simula- tions. Then we got the flame severity distribution matrix. We visualize it as shown in the figure 10.

微信号：MATHmodels

The optimization objectives and constraints of SSA drones are as follows. Bring the fire severity data in the figure 11 into the planning model in the figure below.

(20)

Through lingo, the matrix for 5 kinds of SSA drones monitoring mode and the location of EOC is

obtained. Meanwhile, the total number of SSA UAVs is known as . The location

of EOC is (1,6).

The optimization objectives and constraints of radio repeater drones are as follows.

(21)

关注数学模型 Through lingo, the matrix for the location of radio repeater drones is obtained. Meanwhile, the total

number of radio repeater drones is known as . Ultimately, the total number of 2 kinds of

drones is 10. 微信公众号：数学模型

6.1.2 Result of Problem 2

Due to global warming, the surface temperature of Victoria will increase, which will affect the fire

probability of the region. The critical fire probability after ten years is . Through cellular

automata, we can get the distribution of one of the fires as follows.

The optimization objectives and constraints of SSA drones and the optimization objectives and con-

微信号：MATHmodels straints of radio repeater drones for the ten years later are the same as what the paper showed in model

1&3. Therefore, we can get the UAV configuration for the ‘Rapid Bushfire Response’ system.

The number of SSA drones is known as . The number of radio repeater drones

is known as .

Therefore, for the next decade, due to global warming, the cost of thermal imaging cameras and te-

lemetry sensors increases.

6.1.3 Result of Problem 3

We can get the different area data of fire region by changing the critical fire probability so that the location of radio repeater drones is available. By changing the critical fire probability pf from 0.74 to 0.83 by the step of 0.03, areas of wildfire region and the locations of radio repeater drones are shown in the Table 6.

Critical fire prob- Area of fire region Location of radio repeater (km2) ability drone 79.2342 (3,4) 0.74 81.3212 (2,5) 80.8094 (0,3) 0.77 81.0506 (0,3) 77.7141 (0,3) 0.80 76.3213 (2,5) 72.7502 (2,4) 0.83 74.0506 (2,4)

关注数学模型 As for the location of different terrains, because the terrain characteristic is considered into the model 3, we choose 3 different area to simulate the results. The locations of radio repeater are all the same because the terrain has a much less infect on the location of radio repeater drones. The reason that the effect is small is the effect of terrain on the radio range is not large enough to counteracting SSA drones impact on the location of radio repeater drones. What’s more, it turns out that ratio repeater 微信公众号：数学模型 will get close to the area where the altitude changes rapidly.

7 Model Evaluation and Further Discussion

7.1 Strengths

⚫ The model has wide applicability. Knowing the fire situation, the deployment position of EOC and UAV can be quickly solved, which can improve the efficiency of fire rescue.

⚫ The model can predict the future fire situation according to the weather conditions, so that EOC and drones can be deployed in advance to improve fire rescue efficiency and reduce losses.

微信号：MATHmodels

7.2 Possible Improvements

⚫ The impact of weather and other factors on the flight of the UAV is not considered, which leads to a certain error between the model prediction results and reality. As the planning model is rel- atively large, in order to simplify the model, we have to give up thinking about factors such as weather.

⚫ Due to the lack of detailed fire and climate data in Victoria, the prediction of fire sites in the next ten years lacks accuracy.

⚫ The fire field prediction model assumes that fires are likely to occur in every area. In fact, fires are likely to occur only in places covered by vegetation, which is inconsistent with reality.

Appendices

Appendix 1 —— Tools and software

微信公众号：数学模型 Lingo & Matlab

Appendix 2 —— Code

Appendix 2.1 Introduce: Regional Discretization Model sets: x/1..COLS/; y/1..ROWS/; actions/1..5/; link(x,y):H,totaltime; link3(x,y,actions):t,delta; endsets dronenum = @sum(link3(i,j,k):delta(i,j,k)); 微信号：MATHmodels value = @sum(x(i):@sum(y(j):(1-@exp(lambda*@sum(ac- tions(k):t(i,j,k))))*H(i,j))) - boundary * dronenum; @gin(eocx); @gin(eocy); eocx<=COLS; eocy<=ROWS; @for(link3(i,j,k):@bin(delta(i,j,k))); @for(link(i,j):t(i,j,1)=delta(i,j,1)*(Gmax-@sqrt((eocx-i)^2+(eocy- j)^2)*dtime)); @for(link(i,j)|i#gt#1:t(i,j,2)=(delta(i,j,2)*(Gmax-@sqrt((eocx-i-0.5)^2+(eocy- j)^2)*dtime) + delta(i-1,j,2)*(Gmax-@sqrt((eocx-i+0.5)^2+(eocy- j)^2)*dtime))/2); @for(link(i,j)|j#gt#1:t(i,j,3)=(delta(i,j,3)*(Gmax-@sqrt((eocx-i)^2+(eocy-j- 0.5)^2)*dtime) + delta(i,j-1,3)*(Gmax-@sqrt((eocx-i)^2+(eocy- j+0.5)^2)*dtime))/2); @for(link(i,j)|i#gt#1 #and# j#gt#1:t(i,j,4)=(delta(i-1,j,4)*(Gmax-@sqrt((eocx- i+0.5)^2+(eocy-j-0.5)^2)*dtime) +delta(i,j-1,4)*(Gmax-@sqrt((eocx-i- 0.5)^2+(eocy-j+0.5)^2)*dtime))/2); @for(link(i,j)|i#gt#1 #and# j#gt#1:t(i,j,5)=(delta(i,j,5)*(Gmax-@sqrt((eocx-i- 0.5)^2+(eocy-j-0.5)^2)*dtime) +delta(i-1,j-1,5)*(Gmax-@sqrt((eocx- i+0.5)^2+(eocy-j+0.5)^2)*dtime))/2); @for(link(i,j):H(i,j)<=H(i,j)*((eocx-i)*(COLS+1)-(eocy-j))^2); @for(link(i,j):totaltime(i,j)=@sum(link3(i,j,k):t(i,j,k))); value = @sum(x(i):@sum(y(j):(1-@exp(lambda*@sum(ac- tions(k):t(i,j,k))))*H(i,j))) - boundary * dronenum; max =value; Appendix 2.2 Introduce: Cellular automata simulation a = 500; b = 400; k = 0.005; veg = 5*ones(a,b); imh = image(cat(3,veg,veg,veg)); W = fspecial('gaussian',[51,51],0.9); vegpast = zeros(a,b); resultmat = zeros(5,25); for burn = 0.6:0.02:1 for turn = 1:5

关注数学模型 veg=5*ones(a,b); veg(a/2:a/2+1,b/2:b/2+1)=[4 4;4 4]; for i=1:1000 vegpast = veg; vegavg = imfilter(double(veg<5&veg>1), W, 'replicate'); veg = veg - 1 + (veg==5) + (veg==0) + (veg<0) ...

微信公众号：数学模型 - (veg==5).*(vegavg >= burn * rand(a,b)) ... - 5*((1<veg&veg<5).*rand(a,b) > exp(-k*i)); set(imh, 'cdata', cat(3,(1<veg&veg<5),(veg==5),zeros(a,b))); drawnow if sum(sum((vegpast==5) == (veg==5))) == a * b break; end end resultmat(turn,int16(50*burn-29)) = a*b-sum(sum((veg==5))); end end Appendix 2.3 Introduce: Terrain Adapting Regional Discretization Model sets: x/1..COLS/; 微信号：MATHmodels y/1..ROWS/; z/1..DRONES/:totalpoint; link(x,y):G,H,oinit1,oinit2,oinit3,tinit1,tinit2,tinit3; link3(x,y,z):t,o,delta; endsets @for(z(k):@sum(link(i,j):t(i,j,k))<=Gmax); @for(link3(i,j,k):o(i,j,k)*t(i,j,k)>=o(i,j,k)*G(i,j)); @for(link3(i,j,k):t(i,j,k)<o(i,j,k)*Gmax); @for(z(k):totalpoint(k)*(totalpoint(k)-1) = @sum(x(i):@sum(y(j):o(i,j,k)))); @for(z(k):@for(x(i):@for(y(j):o(i,j,k) <= totalpoint(k)))); @for(z(k):@for(x(i)|i#gt#1 #and# i#lt#COLS:@for(y(j)|j#gt#1 #and# j#lt#ROWS: delta(i,j,k) * (totalpoint(k) - o(i,j,k))* (o(i-1,j-1,k)-o(i,j,k)-1) *(o(i,j-1,k)-o(i,j,k)-1) *(o(i+1,j-1,k)-o(i,j,k)-1)* (o(i-1,j,k)-o(i,j,k)-1) *(o(i+1,j,k)-o(i,j,k)-1) * (o(i-1,j+1,k)-o(i,j,k)-1)* (o(i,j+1,k)-o(i,j,k)-1) *(o(i+1,j+1,k)-o(i,j,k)-1) = 0))); @for(z(k):@for(link(i,j):delta(i,j,k)=@smin(o(i,j,k),1))); @for(z(k):o(startx, starty, k) = 1); @for(z(k):@for(x(i):o(i,1,k)=0)); @for(z(k):@for(x(i):o(i,ROWS,k)=0)); @for(z(k):@for(y(j):o(1,j,k)=0)); @for(z(k):@for(y(j):o(COLS,j,k)=0)); max = @sum(link3(i,j,k):t(i,j,k)*H(i,j));

 In order to meet the page number requirements of the paper, only the most important part of the most important code solution is included in the attachment

关注数学模型
