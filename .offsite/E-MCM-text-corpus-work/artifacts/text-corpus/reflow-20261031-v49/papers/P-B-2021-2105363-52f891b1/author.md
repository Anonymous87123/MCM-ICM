MCM/ICM

Summary Sheet

Summary

How to respond and deal with ﬁres in time when they occur is a question worth thinking about. This paper provides a ﬁre response plan for Victoria through the ratio- nal deployment of EOC, drones and forward teams.

In Task 1, the paper establishes the area safety evaluation model with ﬁre frequency, size, and recent ﬁre situation as indicators to classify the danger levels of different areas in Victoria. Then, we conﬁrm that drones should provide different services for high- risk and dangerous areas. In order to increase the service capacity, we optimize both capacity and cost. For capability, we make the average response time of SSA drones to high-risk areas as short as possible, and reserve as many SSA drones to dangerous areas as possible. For cost, we quantify the demand for SSA drones in terms of ﬁre acreage, and take into account the rounds and the attrition rate of drones. We also

consider the mix between SSA drones and radio repeater drones, and calculate the number of repeater drones using a greedy mix-based maximum number solving algo- rithm. The total cost is calculated and ﬁnally the quantity optimization model based on the maximum mix rate and minimum cost is obtained. 200 SSA drones and 32 radio repeater drones are needed, respectively.

In Task 2, we consider countermeasures in terms of both predicting extreme ﬁre events and increasing equipment. We ﬁrst build a ternary commensurable ﬁre predic- tion model to predict the probability and magnitude of extreme ﬁre events. Then, we use the expectation of the number of extreme ﬁres to estimate the amount of equip- ment that should be added to the EOC. Also, based on the size of the ﬁre and the number of ﬁreﬁghters’ equipment, we obtain a probability of success formula for ex- treme ﬁres, and the expected value of the additional equipment, given that the success rate of each extreme ﬁre rescue by the "boots on the ground" team is 80%. The unit cost of the equipment is reﬁned with relevant information to obtain the expected value of the increased equipment cost. So the total cost of additional equipment is A$4,952.25.

In Task 3, we consider signal range loss and drone safety to optimize the distribu- tion range of repeater drones. First, we establish a signal loss model with improved Standard Propagation Model (SPM) model to quantify the signal-to-noise ratio of the repeater drone’s signal around obstacles of different heights, and eliminate the loca- tions where the repeater signal-to-noise ratio is less than 20 dB. Then, we build a dynamics-based ﬁre spread model to calculate the edge length of ﬁre in each direc- tion. The locations where the distance between the repeater drone and the ﬁre edge is less than 50m are excluded. Finally, we simulate three locations at different altitudes, and ﬁnds that the wind direction directly affects the distribution of the optimized repeater drones, which is concentrated at the edge of the ideal range perpendicular to the wind direction.

We verify the robustness of the model by sensitivity analysis with respect to the parameters affecting the safety factors, and ﬁnd that the recent ﬁre conditions have a strong inﬂuence. We analyze the inﬂuence of different ﬁre frequencies and regions on the number of SSA drones, and the results with higher sensitivity are, ﬁre frequency in the [1600,2000] interval and located in the central region of Victoria, respectively. Finally, an annotated Budget Request is provided by collating all the expenses.

关注数学模型

commensurable signal-to-noise ratio

1 Introduction

1.1 Problem Background

微信公众号：数学模型 Australia’s hot and dry climate, with many hills and few mountains, makes it one of the most forest ﬁre-prone places in the world. Since the ﬁrst ﬁre in New South Wales in September 2019, New South Wales and eastern Victoria was severly affected.

Fireﬁghters have used drones for surveillance and situational awareness (SSA) to allow the Emergency Operations Center (EOC) best direct active crews for optimal effect and maximal safety. The main task of drones is to monitor places where ﬁres are violent and where it is easy to grow into active ﬁres.

1.2 Restatement of the Problem

After understanding the relevant background information, the team are supposed 微信号：MATHmodels to do the following:

• Create a model to determine the optimal numbers and mix of SSA drones and Radio Repeater drones.

• Illustrate how your model adapts to the changing likelihood of extreme ﬁre events over the next decade. Project what equipment cost increases will occur assuming the cost of drone systems stays constant.

• Determine a model for optimizing the locations of hovering VHF/UHF radio- repeater drones.

2 Preparation of the Models

2.1 Assumptions and Justiﬁcations

1. The EOC can be deployed and moved to locations as needed for ﬁreﬁghting mis-

sions, with negligible cost of deployment and movement. And it is responsible for ﬁre rescue situations in only one area at a time.

EOC can be moved and deployed according to the ﬁre situation, and its cost is labor cost and equipment cost. The labor cost is more complicated and is a ﬁxed expendi- ture for the ﬁre department, so it is not considered.

2. When calculating the distance we consider that the distance is a straight line dis-

tance in a spatial three-dimensional coordinate system.

There is a big difference between the altitude of the Victorian mountains and the plains, so the distance obtained by considering the altitude is more accurate.

3. The repeaters can receive signals from multiple targets and forward them to mul-

tiple targets.

This is determined by the function of the repeater. A repeater located between the front lines and the EOC can relay radio signals both from the front lines to the EOC

关注数学模型 and from the EOC to the front lines.

4. Drones only serve part of the ﬁre.

Fires in Australia are common, thus it is less likely to attract widespread attention when an average sized ﬁre occurs. And can be quickly extinguished by local ﬁre forces, without dedicated drone deployment. 微信公众号：数学模型

5. The drone needs to adjust its position when working.

To avoid damage to the drone caused by the effects of ﬁre.

2.2 Notations

The primary notations used in this paper are listed in Table 1.

Symbol Deﬁnition 微信号：MATHmodels r drone scanning radius (x, y) a place with longitude x and latitude y f(x, y) ﬁre frequency at (x, y) size(x, y) ﬁre size at (x, y) situation(x, y) recent ﬁre situation at (x, t) S(x, y) safety factor at (x, y) xi the distance between the EOC and the high-risk area Cost(drone) total cost of two types of drones m number of SSA drones n number radio repeater drones L2 signal-to-noise ratio

2.3 Drones voyage model

Considering the drone power problem, (km ) Voyage the ﬂight range of the drones are related to the average velocity (only consider single 30 trip), and the relationship between them is parabolic. For practical considerations, we formulate that the average speed of the drone 27.8 cannot exceed 10m/s (i.e., max{v} = 10m/s). When the drone is in the maximum ﬂight At this speed, the drone time (i.e. 2.5 hours), the drone range is max- has the largest range. imum, and the average velocity of the drone is 30km/2.5h ≈3.3m/s. The corresponding 0 3.3 10 ( / ) vavg m s relationship is shown in the ﬁgure below.

age average velocity curve, which is a parabolic. What we obtain is as follows by ﬁtting data. V oyage(v) = −0.2 × v2 + 1.32 × v + 27.8 (km), (1)

where V oyage(v) is the length of vayage when drones travel with the average speed of

关注数学模型 v.

2.4 Data pre-processing

In order to simplify the problem, the range of the repeater signal in the calculation of the ﬁrst question is always 20 km. Handheld two-way radios have a range of 2 km 微信公众号：数学模型 in urban, forest and mountainous areas and 5 km elsewhere. This greatly simpliﬁes the calculation and will be further optimized in the third question.

Fires data processing

Combined with life experience we know that the spread of ﬁre presents a convex polygon, which is approximately estimated as a circle. The circumference of the jth ﬁre with latitude and longitude of (xj, yj) is dj(xj, yj), which yields:

• Radius: rj(xj, yj) = dj(xj,yj) ; 2π

• Area: Scircle,j(xj, yj) = π × r2 j(xj, yj).

We combine ﬁres that occurred on the same day and in close proximity into one ﬁre point.

微信号：MATHmodels

3 Task 1: Optimal Numbers and Mix of Two Types of

Drones

In the model for determining the number and combination of drones, it is necessary to provide an evaluation standard for whether the ﬁre point needs drone rescue to improve rescue efﬁciency. To do this, we ﬁrst classify the ﬁres into different safety levels. On the basis of the known safety level of each area, we optimize the number and combination of drones based on maximum mix rate and minimum cost.

3.1 Area safety evaluation model

In order to assess the safety factor for dif- ferent areas of Victoria, the gridded map is shown in Figure 2. The longitude and lati- tude of each region are denoted by x, y, re- spectively. For different latitude and longi- tude (x, y) regions, we establish three eval- uation indicators: ﬁre frequency f(x, y), re- cent ﬁre situation situation(x, y), andﬁre size size(x,y) , which are used to measure the safety factor S(x, y). The safety coefﬁcients of the grid and the adjacent grid are scored to get the safety levels of the different grids on

the map.

3.1.1 Indicators establishment

(1) Fire frequency f(x, y)

In order to fully understand the ﬁre frequency when ﬁres are most severe in differ-关注数学模型 ent areas, we need the maximum value of the daily ﬁre frequency at that location and explore it on different time scales to estimate that maximum value.

f(x, y) = max{u(ts, i, x, y) 微信公众号：数学模型 }, (2) ts where:

• ts is the time scale in days, ts ∈[1, 365];

• i denotes the number of times, i ∈[1, ⌊365 ts ⌋];

• u(ts, i, x, y) = [number of ﬁres that occurred from day (1+(i−1)×ts) to day (1+ i × ts)]/ts (in place (x,y)), indicating the number of ﬁres that occurred in the ith time scale.

𝑢(𝑡௦, 𝑖) is the number of fires that occurred during this period 微信号：MATHmodels 𝑡௦ 𝑖= 1 𝑖= 2 𝑖 A year (365days) 1 1 + 𝑡௦ 1 + 2𝑡௦ 1 + (𝑖−1)𝑡௦ 1 + 𝑖ȉ 𝑡௦

(2) Recent ﬁre situation situation(x, y)

[2] we know that the "mini-weather zone" formed by smoke and From the website heat absorbing atmospheric moisture can continue to spread the ﬁre through the sparks and form new ignition sites, which is also known as "embers attack". In other words, the area where the ﬁre just broke out is more likely to reignite. during the period t0 (the time period corresponding to Figure 1 in the title, i.e., October 1, 2019 to January 7, 2020). We use t0 as the time criterion for determining the presence of recent ﬁres and the period for updating the safety level, making the following divisions.

Recent ﬁre situation Scores

Burning 3 Happened recently 2 Not happened recently 1

(3) Fire size size(x, y)

[1], we extract the circumference Based on the data obtained from Active Fire Data dj(x, y) for the jth ﬁre in the (x, y) region and obtain annual average size:

365 dj(x, y) X size(x, y) = . (3) 365 j=1

关注数学模型

3.1.2 Safety factors S(x, y) and danger levels

1. Safety factors based on AHP AHP is a systematic and hierarchical multi-objective comprehensive evaluation method. We build the importance matrix of S(x, y): 微信公众号：数学模型   1 2 1/6 2 1 1/5 .  6 5 1

We take the average size of the ﬁre as the most important indicator, and the purpose is to make the area with a high safety factor correspond to a larger average size. The resulting ﬁre is more active or can develop into a more larger size, which is in line with the characteristics of the objects monitored by drones.

The consistency ratio is CR = 0.0739, which is less than 0.1, so the degree of inconsistency of S(x, y) is within the tolerance range. And it passes the consistency test. 微信号：MATHmodels In order to eliminate the differences in the different magnitudes, after normaliza- tion, we get:

S(x, y) = a1 × f(x, y) + a2 × situation(x, y) + a3 × size(x, y). (4)

The result of Formula 4 is a1 = 0.1628, a2 = 0.1088, a3 = 0.7285.

2. Safety Assessment of the area:

When we consider whether a region is safe or not, in addition to the safety fac- tor S(x, y) for that region, for its neighboring regions is also of reference value. We convolve the nine safety factors with a convolution kernel

    S(x −1, y + 1) S(x, y + 1) S(x + 1, y + 1) 0.05 0.05 0.05 S′(x, y) = S(x −1, y) ⊗ S(x, y) S(x + 1, y) 0.05 0.6 0.05 .   S(x −1, y −1) S(x, y −1) S(x + 1, y −1) 0.05 0.05 0.05

While the safety factor is already a valuable indicator when considering the safety situation, it is clear that we cannot ignore the inﬂuence of topography for the Rapid Bushﬁre Response program. There are signiﬁcant differences in landscape from region to region. Therefore, ﬁres in forested and vegetated hills and mountains (collectively referred to as ﬂammable topography) are more likely to develop over time into ﬁres that are ﬁerce and difﬁcult to extinguish. And urban, desert, plains and other areas (collectively referred to as non-combustible topography) after the ﬁre is difﬁcult to further develop into a larger scale. Do the following division.

Non-flammable topography Flammable topography

Safety factor Danger level Safety factor Danger level 0 0.25 very safe 0 0.25 safe 0.25 0.5 safe 0.25 0.5 general 0.5 0.75 general 0.5 0.75 dangerous

0.75 1 dangerous 0.75 1 high-risk 关注数学模型

3.1.3 Result analyze of heat map

The map of different security levels is shown in Figure 4. The areas in different colors represent areas of different levels. 微信公众号：数学模型 High-risk Dangerous General Safe & very safe

微信号：MATHmodels

As can be seen in Figure 4, central Victoria is safer, probably because it is at a low altitude and is not affected much by climate. There are many high-risk areas in the east, west and south, which is because these areas are very vegetated.

For SSA drones, it should maintain timely response capability to the high-risk area and have certain prevention capability to the dangerous area. Repeater drones, on the other hand, work with SSA drones to maintain communications and surveillance ac- tivities in high-risk areas, while reserving a certain number of radio-repeater drones for dangerous areas to support communications that may be established. In order to ensure the safety of the EOC, set the EOC to move freely in the safe area.

3.2 Optimization of the number and mix of drones

After dividing the gridded map into areas with different security levels, we dis- patch drones to implement emergency response or preventive deployment based on the security level of the ﬁre, demonstrating the advantages and disadvantages of the solution using capability and cost metrics. We evaluate the mix of the two types of drones and optimize the number of drones based on as much capability and as little cost as possible.

3.2.1 Maximum drone capability

The capability of the drone is reﬂected in two aspects: the response time of the high-risk area is as short as possible (response capability) and the response time of the dangerous area is as reasonable as possible (prevention capability). There are M high-risk areas and N precautionary areas in the statistics. These two capabilities are analyzed separately below.

• Response capability

关注数学模型 We consider the ith EOC to be responsible for communication and surveillance. the role of the EOC is to direct the SSA drone to reach the high risk area from a location closer to the ith high risk area in a safer area, such that the average response time tavg is minimized. 微信公众号：数学模型 M ti X tavg = M , i=1 xi ti = . vmax

To ensure that the drone can travel back to,

xi < 0.5 × V oyage(vmax). (5)

xi is the distance between the EOC and the high-risk area, and ti is the time the aircraft ﬂies in the process. In order to maximize the response capability of the drone, tavg should be as small as possible. Therefore, we make the EOC located at the nearest 微信号：MATHmodels point to the ith high-risk area in the safer region.

• Prevention capability

We conﬁgure a certain number of SSA drones in the dangerous area, so that when the EOC is movable, we can ensure that there are SSA drones or EOCs in the dangerous area at regular intervals to check whether there are ﬁres. Prepare a certain number of drones, the more the number, the better the ability to prevent, see Section 3.2.3 for quantiﬁcation.

3.2.2 Minimal drone costs

We calculate the total cost of the two drones and their number separately. Let the number of SSA drones be m and the number of Radio Repeater drones be n. The calculation is as follows.

Cost(drone) = m × Cost(SSA drone) + n × Cost(radio repeater drone), (6)

where Cost(SSA drone) = SSA drones’ HD camera cost+ remote sensing camera cost+ drone cost, Cost(radio repeater drone) = repeater cost+ Radio Repeater drones’ cost. So we want min{Cost(SSA drone).} (7)

3.2.3 Number and mix of drones

The m, n are the number of SSA drones and radio-repeater drones, respectively. We determine the number of SSA drones from the demand of the ﬁre scene and the round system, then determine the number of radio repeater drones by the combination relationship between SSA drones and radio repeater drones, and ﬁnally prepare some drones to prevent dangerous area.

1. Number of SSA drones

For SSA drones, because SSA drones monitor the ﬁre scene directly, the mixed re- lationship with the radio-repeater drones does not change their utilization rate in the关注数学模型 ﬁre now, so it is sufﬁcient to calculate the number of SSA drones directly according to the ﬁre demand.

(1) For high-risk areas 微信公众号：数学模型 Let the longitude and latitude of the jth high-risk area be (x′ j, y′ j), and ﬁnd the num- ber of SSA drones needed to scan the jth high-risk area.

Fires that need to maintain a timely response are very active, large and mostly in terrain that is prone to further expansion.

Side view

Top view

𝑣୫ୟ୶× 𝑡

𝜃= 40° 𝜃 𝑟 𝑟

微信号：MATHmodels 𝑟 𝑟 ℎ= 300𝑚

Scanning acreage 𝑟 𝑟

To ensure ﬁreﬁghting efﬁciency, SSA drones on scene should assure that they can complete scanning surveillance of the entire scene area within half a minute. The scan radius can be obtained from Figure 5.

S′ circle,j m1,j = πr2 + 2r · vmax × 30 seconds. (8)

SSA drones have constant round trips and recharges, and there are handoffs. So the number of SSA required for the jth high-risk area is the product of the number of handoffs and the number of SSA drones required at the same time.

2¯xi v + recharge time m2,j = m1,j · , (9) −xj V oyage(v) v v

where the biggest fractional equation in Formula (9) represents the rounds of the drone, which is obtained by the quotient of the time returning from the disaster area to recharge and arriving at the disaster area again and the time spent in the disaster area.

(2) For dangerous areas For the ith dangerous area, the number of SSA drones should reach a certain thresh- old in order to check for ﬁres in these areas, such that even in the worst case scenario (i.e., when all dangerous areas are on ﬁre), the number of SSA drones in reserve is suf- ﬁcient to dispatch one SSA drone for each hazard area for temporary surveillance and situational awareness. Thus there is a total number of SSAs:

M X m2,j + N × (1 + ϕ), m = (10)

关注数学模型 i=1 where ϕ is loss rate. Considering the attrition of reserve drones, we prepare some additional drones to cope with this attrition. ϕ is the number of extra prepared drones divided by the number of dangerous area drones.

2. Mix of Radio Repeater drones

微信公众号：数学模型 For the radio-repeater drones, consider its combination with the SSA drones, so that each radio-repeater drone can receive as many signals as possible and forward more signals to determine the best number , optimize utilization.

(1) Greedy and multiplexing based solution algorithms

Using a greedy algorithm, the solution that allows each radio repeater drone to reuse the maximum number of SSA drones is planned, and the minimum number of radio repeater drones, n, is output.

The idea of the algorithm is to ﬁnd candidate locations of radio repeater drones that can be multiplexed. Starting from the candidate location with the most multiplex- ing, a radio repeater drone is determined to be placed at that location, while removing the SSA drones in high-risk areas that can use that repeater drone to send and receive 微信号：MATHmodels signals. Then candidate locations with the second highest reuse rate is identiﬁed. Con- tinue this process until all high-risk areas are taken care of by the repeater.

Given the meaning of some symbols:

• n1, n2 are the number of prepared radio-repeater drones and the number of radio- repeater drones responding to the high-risk area, respectively. When calculating n1, the input n is n1, so does n2.

• mi is the number of SSA drones in ith.

• U is the number of corresponding areas when considering high-risk or dangerous areas.

• Rradio = 2km and Rrepeater = 20km are the ranges of the handheld two-way radios and repeaters, respectively.

• SCi is the candidate range of radio repeater drone for the ith high-risk area, SC = {SC1, SC2, · · · , SCM}.

• SRi is the number of radio repeater drones multiplexed corresponding to the ith high-risk area (other high-risk areas use this repeater at the same time), equal to 1 means that this radio repeater drone is only responsible for the signal transceiver in this high-risk area. SR = {SR1, SR2, · · · , SRM}.

• SNj is the reuse number of the radio repeater drones corresponding to the jth high-risk region. If another high-risk area multiplexes this repeater, the serial number of this high-risk area is an element of the set SN. SN = {SN1, SN2, · · · , SNM}

关注数学模型

Algorithm: Radio Repeater drones number solving algorithm

Input: xi, Rradio, Rrepeater, n = 0 Output: n 1 for i = 1; i ⩽U; i + + do 微信公众号：数学模型 if xi > Rradio then 2 take the ith high-risk area as the center and Rradio as the radius to 3 make a circle O1;

take the ith EOC as the center and Rrepeater as the radius to make 4 a circle O2;

SCi = O1 ∩O2; 5 SRi = 1; 6

7 for i = 1; i ⩽U; i + + do for j = 1; j ⩽U; j + + do 8 if SCi ∩SCj̸ = ∅and i̸ = j then 9 SRi = SRi + mj; 10 SCi = SCi ∩SCj; 微信号：MATHmodels 11 SNi = SNi ∪{j}; 12

13 while SR1 + SR2 + · · · + SRU = 0 do SRk = max{SR}, k is the maximum value’s serial number in SR; 14 n = n + 1; 15 for i = 1; i ⩽U; i + + do 16 if k ∈SNi then 17 SNi = ∅; 18 SRi = 0; 19

(2) Maximize the reuse rate m n Using the reuse rate: m n indicates the mix relationship of drone conﬁguration, the larger this indicator is the better the mix relationship of two drones. Then we have: max{m n }. (11)

(3) Continuous supply to high-risk areas

Considering the process of repeater drone round trip and charging, there is hand- offs, so it is necessary to get the number of repeater drones that respond to high risk areas: 2¯xi v + recharge time n′ 1 = n1 × , V oyage(v) −¯xi v v

ditto, 3.3 ⩽v ⩽10,

V oyage(v) > 2 × max(xj).

So the total number of repeater drones:

n = n′ 1 + n2, (12)

where n2 is radio repeater drones that dangerous areas need.

关注数学模型

3.3 Optimization model with maximum mix rate and minimum cost

Combining all the above, λ is introduced to reﬂect the priority of the drone capabil- ity indicators. The larger λ is, the higher the priority of the capability indicators in the 微信公众号：数学模型 drone conﬁguration scheme obtained from the planning. The ﬁnal model is:

min{( n m)λ × Cost(drone)(1−λ)},

n = n′  1 + n2   0 ⩽ϕ ⩽1   s.t. . 0 ⩽λ ⩽13.3 ⩽v ⩽10    V oyage(v) > 2 × max{xj} 

3.3.1 Result Analysis

微信号：MATHmodels The result of the optimization model with maximum drone capability and mini- mum cost are shown in Figure 6.

Pareto front

Choose the relatively optimal solution for the two objective functions in this area.

Cost(drone)

n m

As shown in the Figure 6, the inverse of m n shows an inverse relationship with the cost of the drone, which indicates that our bi-objective optimization is effective. We intercept the middle section of the interval as the solution space, and we can choose a non-inferior solution in the left half of the interval when we prefer the combination rate to be optimal, and in the right half of the interval when we prefer the cost to be minimal.

4 Task 2: Adaptation of Model and Cost Increases for

Equipment

关注数学模型 For simplicity, we make the following two assumptions:

• The topography of Australia will not change dramatically in the next ten years (not considering changes in topography caused by unavoidable factors such as earthquakes).

• The probability of ﬁre occurrence in different hazard areas is independent of each 微信公众号：数学模型 other.

4.1 Ternary commensurable ﬁre prediction model

4.1.1 Model building process

Since the terrain does not change dramatically over the course of a decade, the main task of predicting ﬁre is when extreme ﬁre conditions will occur, what the probability of occurrence is, and what the amount of equipment prepared to respond to ﬁres of different sizes is. We obtained data on extreme ﬁre conditions in Victoria over the last [5], and used this as the few decades by referring to List of major bushﬁres in Australia basis for our predictions. 微信号：MATHmodels The commensurable prediction model is a method of forecasting special events based on special events, and he bases his forecasting on the universal existence of com- mensurability of events, which is a generalized periodicity. Commensurability is a law that is common to all elements of a system and reﬂects the occurrence of special events [6]. (small probability events) in nature

1. The general commensurable prediction model is:

l X Xi+1 = IjXj, j=1

where X is entered in chronological order for the past years in which extreme ﬁre events occurred to obtain X = {X1, X2, ..., X17} in the sequence.. {j} ∈{i}, that is, j is an element of the set i. Ij is an integer.

2. In order to get the optimal results, the ternary commensurable prediction model

[7]. And the formula is: with the best results in general is selected

Xa + Xb −Xc = Xu(a,b,c),

where a, b, c, d, e, f, g = 1, 2, · · · , n, u, v, w = 1, 2, · · · , m.

3. Enumerate the equations that match the above relationship by enumeration, and

process the sequence numbers to obtain a vector

V = (b −a, c −b, u −c,′ +′,′ −′),

which means the difference between the serial numbers of the ﬁrst two years, the differ- ence between the serial numbers of the second and third years, the difference between the serial numbers of the third and fourth years, the sign before the second year, and the sign before the third year.

Find among all vectors the vectors that exist identical to itself and obtain the multi- set ternary commensurable forecast formula:

关注数学模型 i = 1, 2, · · · , XiV4Xi+V 1V5Xi+V1+V2 = Xi+V1+V2+V3 let the term with the largest ordinal number in the forecast equation be X18, and the forecast value for multiple years corresponding to X18 can be calculated.

4. We sort the past year series and the forecasted year series from left to right by serial number, enumerate four years from all of them, ﬁnd the ternary commensurable 微信公众号：数学模型 forecast formula they match, and connect them two by two with their differences to get the butterﬂy diagram.

Δ = 17 Δ = 17(18) Δ = 17 Δ = 17 Δ = 17 Δ = 17(18) Δ =17(18)

1851 1898 1926 1939 1944 1951 1965 1977 1983 1985 1997 2003 2006 2007 2009 2014 2020 2023

𝚫= 9(8) 𝚫= 9 𝚫= 9 𝚫= 9(8) Years not used in the forecast 微信号：MATHmodels Δ = 3 Δ = 3(4) Δ = 3 Δ = 3(2) Δ = 3 Two Years with difference of 17 Two Years with difference of 9 Two Years with difference of 3

According to the K. Pearson-Fisher theorem, Figure 7 satisﬁes the butterﬂy struc- ture probability reference criterion. It reﬂects the most important quasi-cycles since 1851 as 3, 9, 17a, with 17a being the most typical, occurring seven times.

5. Count statistically the total number of extreme ﬁres used to predict the ith extreme

ﬁre situation as ni, and the number of extreme ﬁres participating in the prediction of the ith extreme ﬁre case is mi, then the probability of the ith extreme ﬁre event is

P(ith extreme ﬁre occur) = mi , ni

and mi can be seen by butterﬂy structure diagram clearly.

For example, our predicted year for the next extreme ﬁre is 2023, which is involved in all three cycles, and the number of years involved in the prediction is 16. The prob- ability of the event prediction is P = m/n = 16/17 = 94.12%, which is the probability of an extreme severe ﬁre in 2023.

6. We use the ﬁre acreage in the data to indicate the severity of extreme ﬁre condi- tions Sdanger, and similarly the ﬁre scale can be predicted by the ternary commensurable prediction model.

7. Test the predicted values and calculate the relative residuals:

ε(k) = x(0)(k) −ˆx(0)(k) , k = 1, 2, . . . , n. x(0)(k)

If for all ε|(k)| < 0.1, the higher requirement is considered to be reached; otherwise, if for all |ε(k)| < 0.2, the general requirement is considered to be reached.

关注数学模型

4.1.2 Result of ternary commensurable ﬁre prediction model

1. Table of predicted years and residual test

微信公众号：数学模型

Years Probability Residual Residual change

2022 64.71% 53 2.62% 2023 94.12% 54 2.67% 2024 52.94% 55 2.72% 2027 41.18% 58 2.86%

and the corresponding probabilities of it. The fourth column shows that the residual change in the occurrence of extreme ﬁres for all four years is around 2%, which is less 微信号：MATHmodels than 5%. This indicates that our predictions have a strong accuracy.

2. Pie map of predicted relative index

Based on the commensurable model, we predict the relative index of severity that would result from the next extreme severity ﬁre when it occurred. As shown in Figure 8, the next extreme severity ﬁre is most likely to produce a ﬁre with a severity index of 0-50. Also, ﬁres with larger severity indices have a high likelihood, accounting for more than half of the likelihood. Therefore, in order to meet future emergency response needs for large ﬁres, we may need to increase the number of drones or "Boots-on-the- ground" Forward Teams.

4.2 Increased Equipment Costs

After predicting the ﬁre, to accommodate changes in the likelihood of extreme ﬁre events over the next decade, we increase the equipment conﬁguration of the EOC and "boots-on-the-ground" ﬁreﬁghters for extreme ﬁre events only, getting the increased equipment costs.

Equipment includes handheld radios for the "boots-on-the-ground" teams, wear-

able devices, and two-way radios for the EOC. From a safety perspective, we assume关注数学模型 that each "boots on the ground" squad ﬁreﬁghter has one handheld radio and one set of wearables, and that each EOC has one two-way radio for surveillance and commu- nications and one two-way radio for backup.

微信公众号：数学模型

4.2.1 Additional equipment costs for EOCs Cost(EOC)

When extreme ﬁres occur, the drone needs the appropriate EOC to support commu- nication and surveillance. Find the expected value E(number, extreme) of the number of extreme ﬁres that have a probability of occurring in the next ten years, which is equal to the sum of the probabilities of occurrence in the ﬁre prediction model.

N X P(ﬁres in i areas) · P(no ﬁres in N −i areas) · i, E(number, extreme) = i=1

where P denotes the probability.

微信号：MATHmodels From Task 1, we know that the number of EOCs responsible for extreme ﬁres is equal to the number of extreme ﬁres. So the cost of the additional equipment for the EOC is calculated as

Cost(EOC) = 2 × E(number, extreme) · Cost(radio). (13)

4.2.2 Additional equipment costs for ﬁreﬁghters Cost(ﬁreﬁghter)

The number of "boots on the ground" teams on each attendance is determined by the EOC after considering the severity of the ﬁre. The probability model for the ﬁre department to handle an extreme ﬁre event is established, and the probability of suc- cessful response to the ﬁre is estimated based on the number of team members Numi and the severity Sdanger,i in ith extreme ﬁre event.

Combined with the actual situation, the more serious the ﬁre, the smaller the pos- sibility of "boots-on-the-ground" squad to put out the ﬁre, while the more the number of squad, the greater the ability to deal with the ﬁre. This change in the relationship should be the ﬁrst slow then fast and ﬁnally slow trend, so the sigmoid function is selected to ﬁt. 1 P(success, i) = Sdanger,i + C), (14) Numi 1 + exp(−

where i ∈[1, E(number, extreme)] and C is a constant, from the article Brief introduction [3], it is known that the average number of Polish ﬁre de- of Polish volunteer ﬁre brigade partment is 24, we can use Fnumber,i = 24, Sdanger,i = average of Sdanger when the success rate is 0.8 to estimate C.

The EOC should ensure that the success rate of each team’s rescue is above 80% when making decisions. Substitute Sdanger,i, calculate the number of team members Pnumber,i for the ith extreme ﬁre with a success rate of exactly 0.8. And utilize the expected value of the increase in the number of "boots-on-the-ground" ﬁreﬁghters to estimate the number of increases needed.

M P(Numi) · P(ith extreme ﬁre occur). X E(Numi) =

关注数学模型 i=1 The cost of additional equipment for ﬁreﬁghters of "boots on the ground" is:

Cost(ﬁreﬁghter) = E(Numi) · (Cost(radio) + Cost(wearable device)). (15) 微信公众号：数学模型

4.2.3 Results of additional equipment

Equipment Number Single price Total price EOC radios 5 92.725 463.625 1,800 “Boots-on-the-ground” handheld radios 19 94.741 “Boots-on-the-ground” team wearable 2,688.625 19 141.507 equipment

微信号：MATHmodels

5 Task 3: Location Optimization

In the greedy and multiplexing based solution algorithms of Task 1, we have ob- tained the ideal distribution range of each repeater drone. Based on this, we consider the signal loss and safety of the repeater drone to optimize its optimal position in the ideal distribution range.

5.1 Signal loss model

SPM model is suitable for propagation loss prediction for distances from 1 to 20 km and frequencies from 150 to 3500 MHz, running GSM and other communication systems. This model takes the feature classiﬁcation map and effective antenna height [4]. into account to calculate the path loss. Its basic equation is shown in Formula 16

L1 = K1 + K2 lg d + K3 lg HTxeff + K4Diff_loss (16) + K5 lg HTxeff lg d + K6HRxeff + Kchitterf(clutter),

where K4 is the multiplicative factor of the bypassing amount; Diff_loss(unit: dB) is the loss caused by bypassing the obstacle; K6 is the multiplicative factor of HRxeff, Rxeff is the mobile station receiving antenna height. K1, K2 and other variables are related to the height and distance of the signal base station as well as environment of drones.

For the repeater drone, when the siting is varied within the ideal distribution, K1, K2, K3, HTxeff, K4, K5, K6, and Kchitter are unchanged, and the small change of d is negligible, only HRxeff and Diff_loss will change. Therefore, the signal loss model of the repeater drone is established as follows.

L2 = K4 · Diff_loss + K6 · HRxeff + L0, (17)

[8] K4 = 44.9 −6.55 log HRxeff, [8] K6 = 1.1 log frepeater −0.7, 4π

[8] 关注数学模型 L0 = 20 log10( ),

λtransmitted wave where fradio is frequency of repeater. λtransmitted wave is wavelength of transmitted wave in meters.

For Rxeff, drone altitude = altitude of location + height above ground.

微信公众号：数学模型 For Diff_loss, we assume that the height of the obstacle is linearly related to the loss of the repeater range, with the most severe loss for obstacle heights greater than 1.5·Rxeff and considered almost no loss effect for obstacle heights less than 0.5·Rxeff. In the ideal case the loss ratio δ is 1.0, the worst case is 0.8. The loss ratio of the ith obstacle :

δi = (Hi/Rxeff) · (1 −0.7)/(1.5 −0.5) + 0.7. where Hi is the height of the ith obstacle Counting K obstacles on the linear path be- tween the repeater drone and the ﬁre area in 1000m. Calculate Diff_loss:

Y Diff_loss = δi. (18) i=1,2,...,K

[9] we can see that we should ensure that the signal-to-noise ratio 微信号：MATHmodels From the website is not less than 20dB, that is, L2 ⩾20dB. (19)

We use this formula to ﬁlter out the areas that do not meet the requirements.

5.2 Drone safety

Depending on the scale of the ﬁre, repeater drones need to avoid nearby ﬁres to ensure safe operations. Because of the limited signal range of handheld radio, repeater drones are often located 2 to 5 km from the center of the ﬁre, and when the ﬁre is large and the terrain is ﬂammable, it is easy to spread to the repeater drone is located, causing damage to the drone in serious cases. We perform a quantitative analysis of safety based on information related to ﬁres.

Kinetics-based ﬁre spread model:

𝑣_𝑤𝑖𝑛𝑑

As shown in the Figure 10, the ﬁre spread into eight directions, of which the direc- tion of the angle with the wind speed less than 45 degrees will spread outside (such as the direction of the yellow arrow), the other directions remain unchanged (such as the

关注数学模型 direction of the blue arrow).

Vspread =⃗Vwind × exp((D + topography scoring) · ﬁre size + E),

where⃗Sr denotes the rate of spread in the vector direction, and D and E both denote 微信公众号：数学模型 constants.

In the ﬁre spread range, the amount of change in the length of the ﬁre⃗k direction is

( Vspread ×⃗k × unit time, Vspread ×⃗k > 0 ∆⃗Lk = , 0, others

and length of ﬁre⃗k direction is

Lk =⃗Lk(last time) + ∆⃗Lk.

Wind speeds were obtained from SSA drones collecting data from “boots-on-the- ground” teams, and terrain was scored to create a scoring table as follows. 微信号：MATHmodels

Terrains Scores

Forests, grassy hills, grasslands 3 Plains, other terrain 2 Not happened recently 1

To ensure safety, the distance between the ith repeater drone position (xdrone,i, ydrone,i), which is in a certain direction of the ﬁre, and the edge of the ﬁre should be made no less than the safety threshold, which is set here to 50 m. Therefore,

|(xdrone,i, ydrone,i) −(x, y) of center| ⩾50 + the range length of the ﬁre. (20)

where "(x, y) of the center" denotes the latitude and longitude of the ﬁre center. "The range length of the ﬁre" means the range length in a certain direction of the ﬁre at a certain moment.

Location optimization:

The signal-to-noise ratio and distance from the edge of the ﬁre are calculated for each location in the ideal distribution range, and reasonable locations are selected:

[9] L2 ⩾20dB.

We use this constraint to optimize to get the drone range from the point of view of preventing ﬁre spread hazards by drones.

关注数学模型

5.3 Result analysis

𝐿𝑎𝑡𝑖𝑡𝑢𝑑𝑒 𝑎𝑛𝑑 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑𝑒: −37.4935, 147.3724 𝐿𝑎𝑡𝑖𝑡𝑢𝑑𝑒 𝑎𝑛𝑑 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑𝑒: −36.7322, 147.3058 𝐻𝑒𝑖𝑔ℎ𝑡: 14m 𝐹𝑖𝑟𝑒 𝑑𝑖𝑟𝑒𝑐𝑡𝑖𝑜𝑛 𝐻𝑒𝑖𝑔ℎ𝑡: 1986m 𝐹𝑖𝑟𝑒 𝑑𝑖𝑟𝑒𝑐𝑡𝑖𝑜𝑛 微信公众号：数学模型 𝐼𝑑𝑒𝑎𝑙 𝑐𝑎𝑛𝑑𝑖𝑑𝑎𝑡𝑒 𝑟𝑎𝑛𝑔𝑒

𝑂𝑝𝑡𝑖𝑚𝑖𝑧𝑒𝑑 𝑜𝑝𝑡𝑖𝑜𝑛𝑎𝑙 𝑟𝑎𝑛𝑔𝑒

𝑁𝑜𝑛 𝑠𝑎𝑓𝑒𝑟 𝑎𝑟𝑒𝑎𝑠 (b) The lowest altitude (a) The highest altitude

Obviously, the wind direction directly affects the distribution of the optimized re- 微信号：MATHmodels peater drones, which is concentrated at the edge of the ideal range perpendicular to the wind direction. High altitude areas are more likely to be affected by the altitude of dif- ferent locations, which manifests itself in the form of a discontinuous and interrupted range of the optimized distribution.

6 Sensitivity analysis

6.1 Sensitivity Analysis of safety factor S(x, y)

In Task 1, we classify the areas of Victoria as different danger levels by calculating the safety factor. Therefore, the safety factor S(x, y) is a crucial parameter, which is cal- culated by ﬁre frequency f(x, y), ﬁze size size(x, y), recent ﬁre situation situation(x, y) (see Formula 4). As a result, we do sensitivity analysis on the coefﬁcients a1, a2 and a3 of these three parameters and the results are shown in Figure 12.

1 Comprehensive safety factor S(x,y) 0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0 -10% -10% -5% -5% 0 0 5% 5% 10% 10% -10% -10% -5% -5% 0 0 5% 5% 10% 10% -10% -10% -5% -5% 0 0 5% 5% 10% 10% 1a a 3a 2 The weight change of parameter a

关注数学模型 In Figure 12, we select a high-risk area as a place to test sensitivity, and the coordi- nate is (x, y) = (−36.0634, 148.2911)

From the ﬁgure we can conclude that When the variation of a1, a2 and a3 change from -10% to 10%, the changes in the values of S(x, y) corresponding to a1 and a3 are 微信公众号：数学模型 small and the overall trend is ﬂat. Therefore, we believe that the frequency and size of ﬁres are more robust and do not affect S too much. Meanwhile, a2 corresponds to a relatively large amount of change in S(x, y), so we think the sensitivity of the recent ﬁre situation to be strong. This result veriﬁes the reasonableness of our consideration of situation(x, y) in Section 3.1.1.

6.2 Sensitivity analysis of ﬁre frequency in different regions per year

The annual frequency of ﬁres in different regions has a signiﬁcant impact on the number of SSA drones. Therefore, we divid Victoria into central, eastern, western, and southern regions, and do sensitivity analysis on the ﬁre frequency in each of these four 微信号：MATHmodels geographic regions.

400

Number of SSA drones 320

240

180

Central region Eastern region 120 Western region Southern region

60

0 400 800 1200 1600 2000 2400 2800 3200 3600 Frequency of fire(times/year)

We can analyze Figure 13 in two ways. For ﬁre frequency, the number of SSA drones vary the most when the number of ﬁres in Victoria is in the range of 1600∼2000 per year. That is, the ﬁre frequency is sensitive in the interval [1600,2000]. Therefore, when CFA uses our model, if the measured number of ﬁres in the year is within this interval, they should calculate the number of SSA drones very carefully.

For different regions, the number of SSA drones in the four regions change sig- niﬁcantly when the ﬁre frequency is greater than 1600. The central region of Victoria has the highest number, while the southern region has the lowest. Therefore, regions are also sensitive to the number of SSA drones, and CFA’s drone dispatch should be different in different regions.

关注数学模型

7 Strengths and Weaknesses

7.1 Strengths

微信公众号：数学模型

• We innovatively use safety factors to classify classes for areas with different ﬁre conditions, which improves the efﬁciency of drone response for emergency situ- ations and provides a clear idea for drone dispatching and distribution.

• The combination and reuse relationship between drones is used to optimize the utilization rate of repeater drones, which both ﬁts the actual situation and has a universal solution to other conﬁguration problems.

• The ternary commensurable prediction model is a model that predicts the prob- ability of future special situations for data of special situations, and the commen- surabiliby it considers is very accurate in the face of special situations with the superiority that other forecasting models do not have.

• We have reviewed a large amount of literature, not only with sufﬁcient data, but also with estimation and calculation methods for the parameters of each model 微信号：MATHmodels from specialized literature, and the results are scientiﬁc and rigorous.

7.2 Weaknesses

• In the problem of optimizing the position of the repeater drone, we are limited by the data for the simulation solution, and the results may be somewhat different from the real situation.

• The index estimated by using AHP model has some subjective inﬂuence, and sensitivity analysis is needed to calculate the reliability of the model.

8 Annotated Budget Request

Budget Justiﬁcation for Cost Proposal (Unit: A$)

We are a numerical modeling competition team from MCM and will be responsi- ble for the overall management and direction of the Victorian National Fire Service’s drone acquisition program for the Rapid Bushﬁre Response Division and equipment acquisition program for extreme ﬁres over the next decade, based on the soundness of our models through testing and analysis of results.

1. "Rapid Jungle Response" Project

Direct costs: 2,401,030

Drones Number Single price Total price SSA drones 200 10,390 2,077,200 Radio repeater drones 32 10,094.741 323,030

The number of SSA drones procured to respond to emergency ﬁre situations in Vic- toria includes 134 shift SSA drones for emergency response to high-risk areas, 62 SSA drones for ﬁre preparedness in prepared areas, and 4 standby drones for considera-

tion of wear and tear. The cost of each SSA drone includes the cost of a bare drone at关注数学模型 A$10,000, an HD camera at A$47.370, and a thermal imaging camera at A$338.648; the repeater drones include 21 repeater drones in combination with SSA drones in high- risk areas and 21 repeater drones in combination with SSA drones in preparedness areas 11, the cost of each repeater drone includes a bare drone of A$10,000, the cost of 微信公众号：数学模型 a repeater of A$94.741.

With this drone conﬁguration, the drones can detect all 373 locations (including 154 high-risk areas and 219 precautionary areas) throughout the state with high frequency and large ﬁre sizes, and have an average response time to emergency ﬁres of only 5 minutes and 17 seconds. In addition, each repeater drone achieved a combined rate of 6.25 with SSA drones. the overall system had excellent responsiveness and excellent combined relationships.

Other costs: None.

Electricity cost for drone charging: A$0.

Our analysis of the infrastructure within the Victorian State Fire Service concluded that the infrastructure within the Fire Service can accommodate the normal conduct of 微信号：MATHmodels activities for other costs and therefore the cost is 0.

2. Equipment procurement items to respond to extreme ﬁres over the next ten

years

Direct Costs: 148,950

Additional equipment (abbreviated): $A 4952.25

Equipment Number Single price Total price EOC radios 5 92.725 463.625 1,800 “Boots-on-the-ground” handheld radios 19 94.741 “Boots-on-the-ground” team wearable 2,688.625 19 141.507 equipment

From a safety perspective, we consider a one-to-one EOC for extreme ﬁres and adjust the number of ﬁreﬁghters in the Ground Boots team based on the predicted size of the extreme ﬁre. We provide a handheld radio and a set of wearables for each ﬁreﬁghter in the "boots on the ground" team, with one two-way radio and a backup two-way radio per EOC. The unit cost of the wearables included a ﬁre axe for $11.288, a heat suit for $120.442, and a ﬁre extinguisher for $9.877. According to our modeling, this scenario has a success rate of more than 80% for "boots on the ground" teams for extreme ﬁres.

Staff cost: 144,000

Staff Number Single price Total price Command staff within EOC 5 6,000 30,000 Firefighters in “Boots-on-the-ground” 19 6,000 114,000

We consider subsidizing a bonus for ﬁreﬁghters to encourage their performance in ﬁre rescue, and similarly, for each EOC, the hard work of the command staff is worth a bonus. We refer to the federal government’s subsidy for volunteer ﬁreﬁghters in New

关注数学模型 South Wales for the bonus assessment.

Other costs: None

Cost of apparatus consumption: None

Wear and tear of ﬁreﬁghting equipment: A$0 Loss of drones: $0 微信公众号：数学模型 The primary job of the "boots on the ground" team is to detect ﬁrst-hand informa- tion about the ﬁre, make judgments about the rapidly changing situation, and pass additional information to the EOC. Therefore, ﬁre ﬁghting is not their main job, the consumption of ﬁreﬁghting equipment is negligible. The wear and tear of drones is already considered in the cost of drones.

introduction

of Polish volunteer ﬁre brigade[J].Fire technology and product information,2014,(6):116,47. DOI:10.3969/j.issn.1002- 784X.2014.06.044.

[4] Chu Peisi. Research and system measurement of wireless signal propagation loss prediction algorithm in mobile communication system[D]. Sichuan:University of Electronic Science and Technology, 2013. DOI:10.7666/d.D762613.

https://en.wikip [5] List of major bushﬁres in Australia. [online] Available at:

edia.org/wiki/List_of_major_bushfires_in_Australia [Accessed 8 Feb. 2021]

[6] Huang Jinfeng, Xia Jun, Du Hong, et al. Medium- and long-term ﬂood fore- casting at Lutaizi and Bengbu stations based on metrizability and gray corre- lation pattern recognition method[J]. Journal of Wuhan University (Engineering Edition),2015,48(5):622-626. DOI:10.14188/j.1671-8844.2015-05-005.

[7] Yellow River Survey, Planning and Design Co. Feasibility study report of the downstream Yellow River ﬂood control project [R]. Zhengzhou: Yellow River Sur- vey, Planning and Design Co., Ltd, 2015: 4-192.

[8] B. Sridhar and M. Z. Ali Khan, "RMSE comparison of path loss models for UH- F/VHF bands in India," 2014 IEEE REGION 10 SYMPOSIUM, Kuala Lumpur, 2014, pp. 330-335, doi: 10.1109/TENCONSpring.2014.6863052.

[9] What is the general signal-to-noise ratio, the useful signal will not be drowned. [online] zhidao.baidu.com/question/624747251070347044.ht Available at:

ml [Accessed 8 Feb. 2021]

关注数学模型
