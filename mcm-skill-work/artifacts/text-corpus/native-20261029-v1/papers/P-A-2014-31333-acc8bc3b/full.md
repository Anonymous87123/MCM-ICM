# P-A-2014-31333-acc8bc3b

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Page 1 of 17

<!-- b000002 | furniture | pages [1] -->
Team # 31333

<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | furniture | pages [1] -->


<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | furniture | pages [1] -->


<!-- b000014 | title | pages [1] -->
Rules of the Road

<!-- b000015 | prose | pages [1] -->
Using adaptations of Nagel-Schreckenberg Cellular Automaton Traffic Simulations

<!-- b000016 | prose | pages [1] -->
to Evaluate Passing Rules for Multi-Lane Freeways

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | heading | pages [1] -->
Abstract

<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | prose | pages [1] -->
We present three conventions for regulating the behavior of automobiles on a

<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | prose | pages [1] -->
freeway as potential alternatives to the “keep-right-except-to-pass” rule that is currently established in the United States and in many other nations. These conventions are tested against the established convention within a freeway traffic flow model we have designed based on Nagel-Schreckenberg models of traffic flow. We assume cars remain on the freeway and all drivers attempt to adhere to the rules of the road, but sometimes make mistakes that can lead to accidents. We also assume that an intelligent system controlling the actions of all cars on the roadway would not make those same mistakes.

<!-- b000027 | prose | pages [1] -->
The first of the three alternatives proposed presents drivers with no rules

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | prose | pages [1] -->
governing their lane-to-lane movement, allowing them to move to any lane that will let them go faster, and to stay there for exactly so long as that remains the case. This convention results in the highest flow rate of cars through the system, but also results in a higher accident rate for a typical three-lane freeway than does the “keep-right-except-to- pass” rule. However, when the number of lanes is increased, the accident rate drops significantly.

<!-- b000030 | prose | pages [1] -->
The second of the three alternatives forbids drivers from changing lanes at all, and

<!-- b000031 | furniture | pages [1] -->


<!-- b000032 | prose | pages [1] -->
results in the second highest flow rate seen, between the no rule and “keep-right-except- to-pass” systems, but results in a higher accident rate than either system for typical three- lane highways. The third model, mandating that drivers remain in the center lane of a three-lane of five-lane freeway, exhibited the lowest flow rate and highest accident rate of any of the four conventions studied.

<!-- b000033 | prose | pages [1] -->
Unfortunately, the model used was seen to be very sensitive to the rate governing

<!-- b000034 | furniture | pages [1] -->


<!-- b000035 | prose | pages [1] -->
accident probability and the number of lanes in a simulation. The way accidents were modeled meant that a single accident tended to promote the occurrence of many more. Additionally a software limitation in the function used to generate an initial matrix with unique car locations meant that it was impossible to create true gridlock within the model.

<!-- b000036 | prose | pages [1] -->
Based on the data from all of the models and the uncertainty in the accident data,

<!-- b000037 | furniture | pages [1] -->


<!-- b000038 | prose | pages [1] -->
we conclude that a no rules convention would result in greater flow rate through a typical three-lane freeway, but that no convention is safer than the “keep-right-except-to-pass” rule, supporting its status as the established rule in much of the world.

<!-- b000039 | prose | pages [1] -->
1

<!-- b000040 | furniture | pages [2] -->
Page 2 of 17

<!-- b000041 | furniture | pages [2] -->
Team # 31333

<!-- b000042 | furniture | pages [2] -->


<!-- b000043 | prose | pages [2] -->
1

<!-- b000044 | heading | pages [2] -->
Introduction

<!-- b000045 | furniture | pages [2] -->


<!-- b000046 | prose | pages [2] -->
Due to the high speed at which freeway traffic travels, transport regulatory bodies impose rules on where in a multi-lane freeway drivers should be at any given time, with the purpose of maximizing the safety and efficiency of freeway travel. One such rule, which is commonly used in countries where automobiles drive on the right hand side of roads, requires drivers to stay in the right-most lane of the freeway unless they are attempting to pass another car. Cars that attempt to pass are required to safely move to the left, pass the car or cars they wish to pass, and then return to their original lane. An analogous rule can be used in countries such as the United Kingdom and Australia where automobiles are driven on the left hand side of the road.

<!-- b000047 | prose | pages [2] -->
In this paper we attempt to answer the question of whether or not the “stay right except to pass” rule is a safe and efficient method for controlling freeway traffic, and compare it to three other rules that could be used to regulate traffic. The three alternate rules have been called: “No Rules”, “No Lane Changes”, and “Middle Lane Rule”; and allow for free lane movement, no lane movement and randomized lanes, and free passing with mandatory return to the middle lane, respectively.

<!-- b000048 | prose | pages [2] -->
The three rules were all implemented into the same cellular automaton traffic control model, based on a model outlined by Nagel and Schreckenberg1, under a variety of traffic conditions, with both heavy and light car density, fast and slow speed limits, and three different probabilities governing accident rates. For each rule and traffic condition, data was gathered on accident count and flow rate for 100 cell regions of 2 through 6 lane freeways across 250 time steps. The results of these simulations are presented in Section 4.2, followed by a discussion of the limitations and assumptions of the model in Sections 4.3 and 5.

<!-- b000049 | furniture | pages [2] -->


<!-- b000050 | prose | pages [2] -->
2 Previous Work

<!-- b000051 | furniture | pages [2] -->


<!-- b000052 | heading | pages [2] -->
2.1 Different Approaches to the Problem

<!-- b000053 | furniture | pages [2] -->


<!-- b000054 | prose | pages [2] -->
Modeling of traffic flow is by no means a new problem, and many models have previously been used to describe and model the flow of traffic on various road types, from cities to freeways. The Wikipedia page on “Traffic Flow”2 alone lists a huge number of model types and parameters that have been used in the past to describe traffic flow, with both discrete and continuous methods for approaching the problem. One

<!-- b000055 | heading | pages [2] -->
model by Doboszczak and Forstall3 used partial differential equations to model traffic

<!-- b000056 | furniture | pages [2] -->


<!-- b000057 | prose | pages [2] -->
1 M. Schreckenberg et al., “Discrete Stochastic Models for Traffic Flow,” Physical Review E 51, no. 4 (April 1995): 2939–2949, doi:10.1103/PhysRevE.51.2939. 2 “Traffic Flow,” Wikipedia, the Free Encyclopedia, February 8, 2014, http://en.wikipedia.org/w/index.php?title=Traffic_flow&oldid=579155609. 3 Stefan Doboszczak and Virginia Forstall, “Mathematical Modeling by Differential Equations” (University of Maryland, October 9, 2013), http://www.norbertwiener.umd.edu/Education/m3cdocs/Presentation2.pdf.

<!-- b000058 | prose | pages [2] -->
2

<!-- b000059 | furniture | pages [3] -->
Page 3 of 17

<!-- b000060 | furniture | pages [3] -->
Team # 31333

<!-- b000061 | furniture | pages [3] -->


<!-- b000062 | prose | pages [3] -->
flow for average densities of cars rather than looking at each individual car. These sorts of models use basic equations and assumptions to build up to more complex mathematical statements.  Another model by a group at MIT examined Phantom Traffic Jams4 and watched a group of cars and observed behaviors of traffic flow, then empirically developed algorithms to display the phenomena they observed.

<!-- b000063 | furniture | pages [3] -->


<!-- b000064 | heading | pages [3] -->
2.2 The Nagel-Schreckenberg Model

<!-- b000065 | furniture | pages [3] -->


<!-- b000066 | prose | pages [3] -->
The traffic model used in this paper was derived from the previous work by Kai Nagel and Michael Schreckenberg5, originally published in 1992, in which cars are placed into a one-dimensional array wherein each cell may either be occupied or unoccupied, and the car in each occupied cell will have an associated speed between zero and the assigned maximum speed for the system. Multiple cars may not occupy the same cell, and the model is governed by fours basic operations that are taken to occur simultaneously for each iteration. These four steps are:

<!-- b000067 | prose | pages [3] -->
1.) Acceleration All cars that are not at the maximum velocity, Vmax (speed limit for the road), and that have more than v+1 empty cells in front of them, accelerate by one unit. v  v+1 2.) Slowing Down for Safety If a car has d empty cells ahead of it and its velocity after step one is greater than d, then it reduces it velocity to x. vmin{d,v} 3.) Randomization For cars with a speed greater than 0, the velocity is reduced by one unit with probability p. V v -1 4.) Driving After steps 1- 3 the each car is assigned a new position x based on its current velocity v. x  x+v

<!-- b000068 | furniture | pages [3] -->


<!-- b000069 | prose | pages [3] -->
Each car acts independently in the sense that the driver is concerned with reaching his or her own destination, but any given car’s actions are also based in response to the cars around it. The model assumes that each driver wishes to drive as fast as allowable, but also that drivers wish to avoid accidents. It also introduces an element of imperfect to the control of the drivers by randomly reducing the speed of each car, though it should be noted that as cars slow down in response to the position of the car in front of them, rather than to its speed or expected position, this randomness will never result in the creation of accidents. It is also important to note that the model is designed for a single lane system, and so cannot be used to answer the problem addressed in this paper without modification to account for the probability of lane changes.

<!-- b000070 | furniture | pages [3] -->


<!-- b000071 | furniture | pages [3] -->


<!-- b000072 | prose | pages [3] -->
4 “MIT Mathematics | Traffic Modeling,” accessed February 9, 2014, http://math.mit.edu/projects/traffic/. 5 Schreckenberg et al., “Discrete Stochastic Models for Traffic Flow.”

<!-- b000073 | prose | pages [3] -->
3

<!-- b000074 | furniture | pages [4] -->
Page 4 of 17

<!-- b000075 | furniture | pages [4] -->
Team # 31333

<!-- b000076 | furniture | pages [4] -->


<!-- b000077 | prose | pages [4] -->
3

<!-- b000078 | heading | pages [4] -->
Model

<!-- b000079 | furniture | pages [4] -->


<!-- b000080 | heading | pages [4] -->
3.1 Simplifying Assumptions

<!-- b000081 | prose | pages [4] -->
• A simulation of a small number of cars in a small pre-defined region, can be taken to be representative of an entire freeway. • No cars entered or exited the highway during each simulation, that is, the number of cars remained constant for each simulation, and therefore that the car density on the studied region remained constant for the entire simulation. • All cars were identical, and they were separated by integer multiples of the cell length. • Differing weather conditions can be accounted for by modifying the probability that governed accident rates. • The reaction times of drivers to impending accidents are different for every driver and take random values. • All accidents were taken to occur between two cars, and have the same effect on traffic in their lane. All cars return to the system after their accident is cleared.

<!-- b000082 | furniture | pages [4] -->


<!-- b000083 | prose | pages [4] -->
The first assumption is necessary due to the fact that simulating large numbers of cars over a large distance is computationally expensive, and requires a complex system for measuring traffic flow, which may differ significantly along the length of the region. This assumption is one that has been previously made and discussed in a paper by Courage et.al.6, wherein cars were taken to be members of small platoons that travelled together.

<!-- b000084 | prose | pages [4] -->
The second and third assumptions are inherent in the Nagel-Schreckenberg model on which ours is based, and is also necessary due to limited available computing power. Simulation of variable cell lengths and variable densities and car counts within each simulation would have been extremely resource intensive for the style of model used.

<!-- b000085 | prose | pages [4] -->
The fourth assumption was made due to the fact that the model does not explicitly consider how different weather conditions affect the accident rate on the freeway, despite the fact that weather conditions certainly do change driving conditions in regards to accidents a great deal. If asked to describe how each rule works in heavy rain or snowy conditions, we would address its performance under a condition that simulated high accident rates.

<!-- b000086 | prose | pages [4] -->
The fifth assumption was used to allow drivers in individual cars to prevent an accident from occurring. There was to be a fixed value for reaction time that was required in order to prevent a dangerous speed up, and each driver would randomly be assigned a reaction time to each incident. Benekohal and Treiterer present a justification for the use of random reaction times in their 1988 paper on their model, CARSIM7. While their

<!-- b000087 | furniture | pages [4] -->


<!-- b000088 | prose | pages [4] -->
6 Kenneth G. Courage, Charles E. Wallace, and Rafiq Alqasem, “MODELING THE EFFECT OF TRAFFIC SIGNAL PROGRESSION ON DELAY,” Transportation Research Record no. 1194 (1988), http://trid.trb.org/view.aspx?id=302135. 7 J. Treiterer R F Benekohal, “CARSIM: Car Following Model for Simulation of Traffic in Normal and Stop-and-Go Conditions,” Transportation Research Record (1988): 99–111.

<!-- b000089 | prose | pages [4] -->
4

<!-- b000090 | furniture | pages [5] -->
Page 5 of 17

<!-- b000091 | furniture | pages [5] -->
Team # 31333

<!-- b000092 | furniture | pages [5] -->


<!-- b000093 | prose | pages [5] -->
model for assigning random reaction times is far more sophisticated and data based than our own, the reasons for using random reaction times remains the same.

<!-- b000094 | prose | pages [5] -->
The sixth and final assumption was another assumption that significantly reduced the amount of time required for each simulation. Though it would be possible for a car to collide with a car that had already collided with another, creating a three-car pileup, cars were assumed to never engage in a simultaneous three-car collision, and cars were assumed not to collide with cars in other lanes. This concept specifically will be discussed in detail when discussing limitations of the model in Section 5.

<!-- b000095 | furniture | pages [5] -->


<!-- b000096 | heading | pages [5] -->
3.2 The Model

<!-- b000097 | prose | pages [5] -->
The model we designed to compare the effectiveness of the different driving conventions used the concept of cells from the Nagel-Schreckenberg model and then added to the model to fit our needs. Our simulation of driving conditions was done by performing various operations on an n by 3 matrix, where n was the number of cars in the simulation. Each row in the matrix represented a car, where the first column’s entry was the cell number of the car’s location, the entry in the second column was the lane that car was located in and the third column’s entry was the current speed of that car.

<!-- b000098 | furniture | pages [5] -->


<!-- b000099 | prose | pages [5] -->
The largest change made from the Nagel-Schreckenberg system was the modeling of multi-lane systems, necessary for the comparison of lane switching strategies. It was made possible for multiple cars to occupy the same cell number, provided they had different lane numbers. The movement of the cars was studied on short, 100 cell regions, with a mechanism implemented to count the number of cars that left the 100 cell region and return them to the region in cell 1. A separate system counted the number of accidents that occurred in the timeframe of a simulation, and to lock down lanes behind accidents, forcing other cars to switch lane or stop and wait for the accident to clear.

<!-- b000100 | furniture | pages [5] -->


<!-- b000101 | prose | pages [5] -->
Accidents themselves occur due to a randomization step that was modified from the Nagel-Schreckenberg randomization step. In the original randomization step every car had fixed probability of randomly slowing down, which, as previously noted, would never cause accidents to be simulated in the system. In our model, the cars have a fixed probability of randomly speeding up, potentially causing them to rear end the car in front of them. Additionally, all the drivers will randomly respond to each potential accident, and will either succeed or fail in preventing the accident from occurring, as discussed in Section 3.1.

<!-- b000102 | furniture | pages [5] -->


<!-- b000103 | prose | pages [5] -->
Though the explicit step sequence differed for each rule within our model, the general sequence of steps in the cellular automaton traffic simulation, each of which modifies the n by 3 matrix discussed above, was as follows:

<!-- b000104 | prose | pages [5] -->
1.) Acceleration All cars that are not at the maximum velocity, Vmax (speed limit for the road), and that have more than v+1 empty cells in front of them, accelerate by one unit. v  v+1 2.) Lane Changing If a car has d empty cells ahead of it and its velocity after step one is greater than d, and there is no adjacent car preventing lane changes as

<!-- b000105 | prose | pages [5] -->
5

<!-- b000106 | furniture | pages [6] -->
Page 6 of 17

<!-- b000107 | furniture | pages [6] -->
Team # 31333

<!-- b000108 | furniture | pages [6] -->


<!-- b000109 | prose | pages [6] -->
allowed by the rule system, the car will move over one lane and then repeat this step until no further productive lane movement is possible. In the Right Hand Rule system, cars can only move left in this step, while in the No Rules, and Middle Lane Rule systems the cars were free to move either left or right. In the No Lane Changes system this step is skipped. Lane  Lane ± 1 3.) Slowing Down for Safety If a car has d empty cells ahead of it and its velocity after step one is greater than d, then it reduces it velocity to x. v  min{d,v} 4.) Randomization For cars with a speed less than Vmax, the velocity is increased by one unit with probability p. vv -1 5.) Driving After steps 1- 4 the each car is assigned a new position x based on its current velocity v. x  x+v 6.) Exit Count and Car Cycling If, after moving, a car is in a cell number above 100, having previously been in a cell number less than or equal to 100, the count of cars that have gone through the system will increase by 1, and if there is an open lane in cell 1 the car will be placed in it. If there is no open lane, the car is recycled at a later time step. Throughput  Throughput +1       Cell  1 7.) Check for and Respond to Accidents If two cars are found to be in the same lane and cell, the count of accidents is increased by one, and their velocities are set to different negative numbers. As all steps other than “Acceleration” ignore cars with a negative value for speed, this will freeze the cars in their accident position for a fixed amount of time, taken to be the amount of time to clear the accident and return the cars to the road. Accidents  Accidents +1 v  -1 or -5. 8.) Return to Designated Start Lane This step is only applied to the Right Hand Rule system and the Middle Lane rule system. For each car the model checks whether or not the car is in its designated start lane, 1 for Right Hand Rule and 2 or 3 for Middle Lane Rule, and if the car is in the wrong lane, and if there is no car adjacent to it in the direction of its start lane, the car will move one step toward its start lane. It will then repeat this step until it is no longer possible for it to move closer to its start lane. LaneLane±1

<!-- b000110 | furniture | pages [6] -->


<!-- b000111 | prose | pages [6] -->
The model was built in MATLAB as a series of scripts to perform the functions described above, with at least one script per step and multiple scripts for steps that varied in different rule systems, that could be inserted into a function in a modular fashion so as to simply create a function capable of running the model several times and averaging data for each of the four rule systems.

<!-- b000112 | prose | pages [6] -->
6

<!-- b000113 | furniture | pages [7] -->
Page 7 of 17

<!-- b000114 | furniture | pages [7] -->
Team # 31333

<!-- b000115 | furniture | pages [7] -->


<!-- b000116 | furniture | pages [7] -->


<!-- b000117 | prose | pages [7] -->
4

<!-- b000118 | heading | pages [7] -->
Results

<!-- b000119 | furniture | pages [7] -->


<!-- b000120 | heading | pages [7] -->
4.1 Description of Parameters and Terminology

<!-- b000121 | prose | pages [7] -->
All of the data presented are the result of averaging the results of ten simulations of the model for each rule system. A single simulation is defined as being 250 time steps of the model evaluated on a 100-cell region. The required reaction time for a driver to prevent an accident was fixed such that any given driver would succeed 30% of the time. All other parameters were considered variable, and tests were performed with every possible combination of conditions.

<!-- b000122 | furniture | pages [7] -->


<!-- b000123 | prose | pages [7] -->
Vmax

<!-- b000124 | prose | pages [7] -->
Fast – For a fast speed limit, Vmax is set equal to 6 cells per time step. Slow – For a slow speed limit, Vmax is set equal to 2 cells per time step. Rate of Random Speed Increase Potentially Resulting in Accidents

<!-- b000125 | prose | pages [7] -->
Computer  – The probability of random speed changes being manually set to zero, which also mean the probability of an accident is zero. Accident Prone – The probability of any given car speeding up in any given time step is 0.3. Normal  – The probability of any given car speeding up in any given time step is 0.01. Traffic Density

<!-- b000126 | prose | pages [7] -->
Heavy  – Large number of cars in the region, which we have defined as 100 cars. Light  –  Small number of cars in the region, which we have defined as 30 cars.

<!-- b000127 | furniture | pages [7] -->


<!-- b000128 | prose | pages [7] -->
For each of the 5 lane numbers in each of the four rule systems, the “Average Flow Rate” is calculated by averaging the total number of cars that leave the region in a simulated time interval, across the ten simulations performed, and then dividing that value by the number of time steps in each simulation, which was fixed at 250. The “Average Accidents” is merely the total number of accidents in each simulation, averaged across the 10 simulations.

<!-- b000129 | furniture | pages [7] -->


<!-- b000130 | heading | pages [7] -->
4.2 Figures

<!-- b000131 | prose | pages [7] -->
The figures presented on the following pages summarize the data that were collected for each of the four conventions across all of the different speed limits, accident rates, traffic densities, and lane numbers used for simulations. They are presented by convention, along with a brief summary of the conditions of the convention.

<!-- b000132 | furniture | pages [7] -->


<!-- b000133 | furniture | pages [7] -->


<!-- b000134 | furniture | pages [7] -->


<!-- b000135 | furniture | pages [7] -->


<!-- b000136 | furniture | pages [7] -->


<!-- b000137 | prose | pages [7] -->
7

<!-- b000138 | furniture | pages [8] -->
Page 8 of 17

<!-- b000139 | furniture | pages [8] -->
Team # 31333

<!-- b000140 | furniture | pages [8] -->


<!-- b000141 | heading | pages [8] -->
4.2.1 Right Hand Rule

<!-- b000142 | furniture | pages [8] -->


<!-- b000143 | prose | pages [8] -->
The Right Hand Rule Algorithms represent the standard convention of driving on the right, and moving left to overtake a car in front. All of the cars start in the right most lane, as if all the cars have all just entered the freeway. The cars then disperse to overtake slower cars but always try to move back into a spot in the right most lane possible.

<!-- b000144 | prose | pages [8] -->
AVERAGE FLOW RATES OF RIGHT HAND RULE

<!-- b000145 | prose | pages [8] -->
3

<!-- b000146 | prose | pages [8] -->
Average Cars/unit of time

<!-- b000147 | prose | pages [8] -->
2.5

<!-- b000148 | prose | pages [8] -->
2

<!-- b000149 | prose | pages [8] -->
1.5

<!-- b000150 | prose | pages [8] -->
1

<!-- b000151 | prose | pages [8] -->
0.5

<!-- b000152 | prose | pages [8] -->
0

<!-- b000153 | prose | pages [8] -->
two lanes

<!-- b000154 | prose | pages [8] -->
three lanes

<!-- b000155 | prose | pages [8] -->
four lanes

<!-- b000156 | prose | pages [8] -->
five lanes

<!-- b000157 | prose | pages [8] -->
six lane

<!-- b000158 | prose | pages [8] -->
Simulation Type

<!-- b000159 | furniture | pages [8] -->


<!-- b000160 | furniture | pages [8] -->


<!-- b000161 | prose | pages [8] -->
RIGHT HAND RULE AVERAGE ACCIDENTS

<!-- b000162 | prose | pages [8] -->
2000

<!-- b000163 | prose | pages [8] -->
Average Number of Accidents

<!-- b000164 | prose | pages [8] -->
1800 1600 1400 1200 1000 800 600 400 200 0

<!-- b000165 | prose | pages [8] -->
two lanes

<!-- b000166 | prose | pages [8] -->
three lanes four lanes five lanes

<!-- b000167 | prose | pages [8] -->
Simulation Type

<!-- b000168 | furniture | pages [8] -->


<!-- b000169 | prose | pages [8] -->
8

<!-- b000170 | furniture | pages [9] -->
Page 9 of 17

<!-- b000171 | furniture | pages [9] -->
Team # 31333

<!-- b000172 | furniture | pages [9] -->


<!-- b000173 | heading | pages [9] -->
4.2.2 No Rules

<!-- b000174 | furniture | pages [9] -->


<!-- b000175 | prose | pages [9] -->
The No Rules method is referring to algorithms that do not prioritize moving to the left lane over moving the right lane. The Cars on the freeway start in random lanes in these simulations, and only move into different lanes if they are trying to overtake a car in front of it.

<!-- b000176 | prose | pages [9] -->
AVERAGE FLOW RATES OF NO RULES

<!-- b000177 | prose | pages [9] -->
4

<!-- b000178 | prose | pages [9] -->
Average Cars/unit of time

<!-- b000179 | prose | pages [9] -->
3.5 3 2.5 2 1.5 1 0.5 0

<!-- b000180 | prose | pages [9] -->
two lanes

<!-- b000181 | prose | pages [9] -->
three lanes

<!-- b000182 | prose | pages [9] -->
four lanes

<!-- b000183 | prose | pages [9] -->
five lanes

<!-- b000184 | prose | pages [9] -->
six lanes

<!-- b000185 | prose | pages [9] -->
Simulation Type

<!-- b000186 | furniture | pages [9] -->


<!-- b000187 | furniture | pages [9] -->


<!-- b000188 | prose | pages [9] -->
AVERAGE ACCIDENTS OF NO RULES

<!-- b000189 | prose | pages [9] -->
2500

<!-- b000190 | prose | pages [9] -->
Average Number of Accidents

<!-- b000191 | prose | pages [9] -->
2000

<!-- b000192 | prose | pages [9] -->
1500

<!-- b000193 | prose | pages [9] -->
1000

<!-- b000194 | prose | pages [9] -->
500

<!-- b000195 | prose | pages [9] -->
0

<!-- b000196 | prose | pages [9] -->
two lanes

<!-- b000197 | prose | pages [9] -->
three lanes

<!-- b000198 | prose | pages [9] -->
three lanes

<!-- b000199 | prose | pages [9] -->
five lanes

<!-- b000200 | prose | pages [9] -->
six lanes

<!-- b000201 | prose | pages [9] -->
Simulation Type

<!-- b000202 | furniture | pages [9] -->


<!-- b000203 | furniture | pages [9] -->


<!-- b000204 | furniture | pages [9] -->


<!-- b000205 | prose | pages [9] -->
9

<!-- b000206 | furniture | pages [10] -->
Page 10 of 17

<!-- b000207 | furniture | pages [10] -->
Team # 31333

<!-- b000208 | furniture | pages [10] -->


<!-- b000209 | heading | pages [10] -->
4.2.3 No Lane Changes

<!-- b000210 | furniture | pages [10] -->


<!-- b000211 | prose | pages [10] -->
No lane changes refers to algorithms that do not allow cars to change lanes at all. There is no overtaking, all cars in this model have their initial starting lane generated randomly, and it is as if they entered the free-way, moved to a random lane, and stayed there until they would decide to leave the freeway. All lane-changing algorithms were removed.

<!-- b000212 | furniture | pages [10] -->


<!-- b000213 | prose | pages [10] -->
AVERAGE FLOW RATES OF NO CHANGE RULE

<!-- b000214 | prose | pages [10] -->
3.5

<!-- b000215 | prose | pages [10] -->
Average Cars/unit of time

<!-- b000216 | prose | pages [10] -->
3

<!-- b000217 | prose | pages [10] -->
2.5

<!-- b000218 | prose | pages [10] -->
2

<!-- b000219 | prose | pages [10] -->
1.5

<!-- b000220 | prose | pages [10] -->
1

<!-- b000221 | prose | pages [10] -->
0.5

<!-- b000222 | prose | pages [10] -->
0

<!-- b000223 | prose | pages [10] -->
two lanes

<!-- b000224 | prose | pages [10] -->
three lanes

<!-- b000225 | prose | pages [10] -->
four lanes

<!-- b000226 | prose | pages [10] -->
five lanes

<!-- b000227 | prose | pages [10] -->
six lanes

<!-- b000228 | prose | pages [10] -->
Simulation Type

<!-- b000229 | furniture | pages [10] -->


<!-- b000230 | furniture | pages [10] -->


<!-- b000231 | prose | pages [10] -->
AVERAGE ACCIDENTS FOR NO CHANGE RULE

<!-- b000232 | prose | pages [10] -->
2500

<!-- b000233 | prose | pages [10] -->
Average Number of Accidents

<!-- b000234 | prose | pages [10] -->
2000

<!-- b000235 | prose | pages [10] -->
1500

<!-- b000236 | prose | pages [10] -->
1000

<!-- b000237 | prose | pages [10] -->
500

<!-- b000238 | prose | pages [10] -->
0

<!-- b000239 | prose | pages [10] -->
two lanes

<!-- b000240 | prose | pages [10] -->
three lanes

<!-- b000241 | prose | pages [10] -->
four lanes

<!-- b000242 | prose | pages [10] -->
five lanes

<!-- b000243 | prose | pages [10] -->
six lanes

<!-- b000244 | prose | pages [10] -->
Simulation Type

<!-- b000245 | furniture | pages [10] -->


<!-- b000246 | furniture | pages [10] -->


<!-- b000247 | prose | pages [10] -->
10

<!-- b000248 | furniture | pages [11] -->
Page 11 of 17

<!-- b000249 | furniture | pages [11] -->
Team # 31333

<!-- b000250 | furniture | pages [11] -->


<!-- b000251 | furniture | pages [11] -->


<!-- b000252 | heading | pages [11] -->
4.2.4 Middle Lane Rule

<!-- b000253 | furniture | pages [11] -->


<!-- b000254 | prose | pages [11] -->
The Algorithms from Middle Lane Rule start all of the cars in the middle most lane of the freeway, and they disperse out to overtake one another. The overtaking mechanism is similar to “No Rules” in that they can over take on the left or on the right, but the cars always try to find an open spot in the middle lane of the freeway.

<!-- b000255 | furniture | pages [11] -->


<!-- b000256 | prose | pages [11] -->
AVERAGE FLOW RATES OF MIDDLE LANE RULE

<!-- b000257 | prose | pages [11] -->
3

<!-- b000258 | prose | pages [11] -->
Average Cars/unit of time

<!-- b000259 | prose | pages [11] -->
2.5

<!-- b000260 | prose | pages [11] -->
2

<!-- b000261 | prose | pages [11] -->
1.5

<!-- b000262 | prose | pages [11] -->
1

<!-- b000263 | prose | pages [11] -->
0.5

<!-- b000264 | prose | pages [11] -->
0

<!-- b000265 | prose | pages [11] -->
lane three

<!-- b000266 | prose | pages [11] -->
lane five

<!-- b000267 | prose | pages [11] -->
Simulation Type

<!-- b000268 | furniture | pages [11] -->


<!-- b000269 | furniture | pages [11] -->


<!-- b000270 | prose | pages [11] -->
AVERAGE ACCIDENTS FOR MIDDLE LANE RULE

<!-- b000271 | prose | pages [11] -->
3000

<!-- b000272 | prose | pages [11] -->
Average Number of Accidents

<!-- b000273 | prose | pages [11] -->
2500

<!-- b000274 | prose | pages [11] -->
2000

<!-- b000275 | prose | pages [11] -->
1500

<!-- b000276 | prose | pages [11] -->
1000

<!-- b000277 | prose | pages [11] -->
211.3	   98.8

<!-- b000278 | prose | pages [11] -->
500

<!-- b000279 | prose | pages [11] -->
66.2 97.3

<!-- b000280 | prose | pages [11] -->
0

<!-- b000281 | prose | pages [11] -->
lane three

<!-- b000282 | prose | pages [11] -->
30.6	   102

<!-- b000283 | prose | pages [11] -->
86.1

<!-- b000284 | prose | pages [11] -->
lane five

<!-- b000285 | prose | pages [11] -->
Simulation Type

<!-- b000286 | furniture | pages [11] -->


<!-- b000287 | prose | pages [11] -->
11

<!-- b000288 | furniture | pages [12] -->
Page 12 of 17

<!-- b000289 | furniture | pages [12] -->
Team # 31333

<!-- b000290 | furniture | pages [12] -->


<!-- b000291 | furniture | pages [12] -->


<!-- b000292 | furniture | pages [12] -->


<!-- b000293 | heading | pages [12] -->
4.3 Comparison of Rule Systems

<!-- b000294 | prose | pages [12] -->
There were three different rule conventions that were used to compare against the right hand rule convention, which is the standard convention in America.

<!-- b000295 | furniture | pages [12] -->


<!-- b000296 | prose | pages [12] -->
No Rules Convention

<!-- b000297 | furniture | pages [12] -->


<!-- b000298 | prose | pages [12] -->
The No Rules Convention was a simulation that allowed for drivers to overtake on either side of the road, and to stay in whatever lane they find themselves. This model provided the fastest flow rate out of any of the models but was slightly less safe for low lane numbers than the RHR. The No Rules Convention having the fastest flow rate was not entirely surprising, because the cars are all permitted to do anything they can to increase their speeds, and are able, unlike in the No Lane Changes convention, to switch lanes to move quickly past an accident. The Cars in the No Rules Model did not try to reposition themselves at the end of each iteration, which allowed them to spread themselves across all available lanes, causing particularly high flow rates for simulations with high lane counts. This convention led to slightly more accidents compared to the RHM when lanes were low, likely due to cars frequently moving in and out of lanes directly in front of each other. However, when lane counts were high, the No Rules convention exhibit much better safety than the RHR convention, with the cars in the RHR convention confining themselves to be as far to the right as possible, thereby increasing the likelihood that accidents can occur. No Change Convention

<!-- b000299 | prose | pages [12] -->
The simplest of all the derivatives is the No Change Convention, which generated a fixed number of cars into random lanes where the cars would remain throughout the entire simulation. This is essentially the 1-dimensional Nagel-Schreckenberg model running in multiple lanes at the same time. This model provided the second fastest results, but also was the most dangerous.

<!-- b000300 | prose | pages [12] -->
The simulation moves in discrete steps, one of them being the random speed up routine. When an accident occurred in the No Change Model, the cars behind the accident were unable to change lanes to move around the accident, as they could in all other models. The result of this fact is that when the probability of random speed ups and the car density were both high, a single accident resulted in many cars becoming stuck at zero velocity behind it for five time steps. Due to the high accident probability, one of these cars eventually experiences a random speed up, at which time it plows into the car in front of it, causing an accident, resulting in accident chain reactions. This can be seen in the second figure of Section 4.2.4, where the “Accident-Prone Heavy Traffic” simulations show extremely high number of accidents. In the same figure, the simulations that had a 0 or 0.01 probability of a speed up showed little or no accidents.

<!-- b000301 | prose | pages [12] -->
12

<!-- b000302 | furniture | pages [13] -->
Page 13 of 17

<!-- b000303 | furniture | pages [13] -->
Team # 31333

<!-- b000304 | furniture | pages [13] -->


<!-- b000305 | prose | pages [13] -->
Interestingly, simulations run by Alexander Lobkovsky Meitiv of the National Center for Biotechnology Information for his personal blog8 using his own adaptation of the Nagel- Schreckenberg model, indicated that a “stay in lane” rule system yields higher average car velocities than if cars switch into faster moving lanes. Those are the only two rule sets he discusses, the “switch into faster lanes” rule system is not directly analogous to our “No Rules” system, his model operates on a truly circular track, and he does not attempt to account for accident rates. Nonetheless, his conclusions provide an interesting second look at the performance “No Lane Changes” rule system against fast switching rule systems in preserving a consistent high rate of traffic flow for the car system as a whole. Despite its many differences from our model, his model lends support to the conclusion suggested by our own data, that a system of never changing lanes leads to fast movement of all cars relative to certain other lane changing systems.

<!-- b000306 | prose | pages [13] -->
The No Change Convention was the most unrealistic out of all provided because it didn’t allow drivers to change lanes at all, even in case of accidents, but was still useful as a way to measure the effectiveness of models, and estimate the general effect of many cars changing lanes on the traffic flow of the system as a whole. Middle Lane Convention

<!-- b000307 | prose | pages [13] -->
The Middle Lane convention showed the lowest flow rate of all models, as well as showing the highest accident rate of all the models. While data for this rule was only collected for a three-lane and a five-lane freeway, owing to the fact that even-laned freeways do not have a single middle lane, the data collected give strong evidence that the model leads to high accident rates and low numbers of cars flowing through the region than any other rule convention studied. Much like the RHR convention, the increase from three lanes to five lanes did not result in a decrease in accident rates on the scale of that seen for the No Rules and No Lane Changes conventions. Of the four conventions studied, this one is considered to be by far the worst.

<!-- b000308 | furniture | pages [13] -->


<!-- b000309 | furniture | pages [13] -->


<!-- b000310 | prose | pages [13] -->
5

<!-- b000311 | heading | pages [13] -->
Discussion

<!-- b000312 | furniture | pages [13] -->


<!-- b000313 | heading | pages [13] -->
5.1 Limitations of the model

<!-- b000314 | prose | pages [13] -->
In our model there are factors that were not properly taken into account due to our assumptions and the way that the algorithms were developed. The model works in steps, which means that every car in the simulation is looked at individually, and cars don’t move simultaneously. The model presented is all built off of the Negal-Schreckenburg model which used uniform undefined time steps, and this is carried over into our model’s designs. One flaw of the model is that each of the steps of the algorithms are carried out individually (cars will one by one move left, then one by one do safety checks etc.) the only time that accidents occur is in the speed up phase, which would cause all accidents to be rear-end accident, where one car hits the car directly in front of it, and no accidents

<!-- b000315 | furniture | pages [13] -->


<!-- b000316 | prose | pages [13] -->
8	  “What	  Can	  Scientific	  Models	  Tell	  Us	  about	  the	  World?,”	  accessed	  February	  10,	  2014, http://playingwithmodels.wordpress.com/2010/06/24/should-­‐you-­‐switch-­‐lanes-­‐in-­‐traffic/),.

<!-- b000317 | prose | pages [13] -->
13

<!-- b000318 | furniture | pages [14] -->
Page 14 of 17

<!-- b000319 | furniture | pages [14] -->
Team # 31333

<!-- b000320 | furniture | pages [14] -->


<!-- b000321 | prose | pages [14] -->
are caused as cars move into other lanes. In reality this doesn’t happen, accidents can come from any direction, but this all comes from the assumption that all accidents occur randomly.

<!-- b000322 | prose | pages [14] -->
In our model the way that we accounted for accidents was through random number generation. Cars would speed up or slow down depending on whether a number was less than a value that is specified in the parameters of the model, and an accident would occur if the driver’s randomly generated response time value was not low enough. We created simulations were a perfect drivers (i.e. computer driven vehicles) were used and thus we assumed that they would have a perfect knowledge of the surrounding system, and thus their probability of speeding up would be 0. For “normal” simulations we put the probability of an accident occurring at less than .01. This assumes that drivers would have control of their vehicles and would slam on the breaks less, and or not be distracted while driving. In our simulations of accident prone drivers, the probability of a speeding up is set to .3, this was to cover all situations where drivers had significantly less control over their vehicles. We did not however alter the response time needed to avoid an accident in any of these situations. Different weather conditions would call for different response times, and different chances of speeding ups. Ice on the roads would be more serious than higher wind speeds. Instead accident prone simulations were run to cover any of those situations instead of looking into the matter with more detail.

<!-- b000323 | furniture | pages [14] -->


<!-- b000324 | prose | pages [14] -->
Throughout our model, an accident was caused when two cars in the same lane had the same position value in Car_Matrix. This would cause cars in the same lane that were behind the accident to lag and help simulate slowed down traffic. However, in some of the simulations certain accidents could lead to more accidents, in a domino effect. This was caused by the random speed ups that we put in, when cars were lined up in consecutive cells in their respective lanes, if there were multiple cars behind each other waiting for an accident to clear, and a speed up occurred (which could be quite high in accident prone simulations), then another accident would continue to block that lane. This posed as quite a problem in the No Change simulation as cars could not leave their lanes when an accident occurred, and thus there were more accidents in the No Change simulations.

<!-- b000325 | prose | pages [14] -->
Cars and their actions were simulated by the matrix Car_Matrix, and one major limitation of the matrix, by virtue of our programming in MATLAB, was that the number of cars in the matrix could not exceed the number of rows of cells being used to represent the lanes of the highway. Thus, we couldn’t simulate proper grid lock, or true high density traffic patterns. This becomes increasingly clear as we look at the data for highways with more lanes. Since the number of cars was held constant for the number of lanes being used in the simulation, the car density of the grid drops as we add more lanes, this means that traffic gets lighter and lighter even though the simulation are technically being looked at as “heavy traffic” and accidents drop and the flow rate increases because cars have less and less interactions with one another and therefore cars can move with less obstruction. The model can still be used because as the iterations increase, the cars will move closer and closer together since they all want to move forward, and thus at the top of the grid of cells the cars will bunch together which creates a form of pseudo-grid

<!-- b000326 | prose | pages [14] -->
14

<!-- b000327 | furniture | pages [15] -->
Page 15 of 17

<!-- b000328 | furniture | pages [15] -->
Team # 31333

<!-- b000329 | furniture | pages [15] -->


<!-- b000330 | prose | pages [15] -->
lock. Also, since the rate of change of the density decreases at the same rate in all of the models, all of the data experiences the same shift throughout all the simulations.

<!-- b000331 | prose | pages [15] -->
Finally, cars also do not enter or leave the freeway. In addition,  cars also either come onto the freeway all in the same lane, or randomly depending on which simulation was used. Then the cars all stay on the freeway and only move forward. In reality cars enter and exit all the time, and this means that cars would have reasons to cross over lanes other than in compulsion to the regulations of the road. If cars would have crossed over to exit then there would be more chances for accidents to occur, and cars would disperse over the grid of cells a lot more than they did in any of our simulations.

<!-- b000332 | furniture | pages [15] -->


<!-- b000333 | heading | pages [15] -->
5.2 Symmetry of model

<!-- b000334 | prose | pages [15] -->
All of the algorithms of our model would easily transition over to any driving systems that implemented left hand side driving. In countries where the left side of the road is the norm, cars place the driver on the other side, thus the visibility for each driver is the same and our algorithms would still hold because they all use integers to describe the different lanes, positions and, velocities, in essence our algorithms are all symmetric. So we could model cars that drove on the left by renumbering the lanes of Car_Matrix backwards, n:1 lanes instead of 1: n, and the model’s algorithms would still hold true.

<!-- b000335 | furniture | pages [15] -->


<!-- b000336 | heading | pages [15] -->
5.3 Sensitivity

<!-- b000337 | prose | pages [15] -->
The model appears to be very sensitive to the number of lanes in any given simulation, due to the fact that the function that propagates the freeway region with automobiles cannot add more vehicles than cells, regardless of the number of lanes in the simulation. This limitation was built into MATLAB’s randperm function, and could not be circumvented in the scope of the project. The result of this fact was that for high lane numbers, the two conventions that had no defined start lane appeared to be very safe, despite appearing less safe for low lane numbers. This is a result of the fact that for a six lane highway a car was only expected to appear every 6 cells, so for conventions that were able to spread to all lanes, the car density became extremely low, while remaining relatively high in systems that forced cars to return toward some specific lane.

<!-- b000338 | furniture | pages [15] -->


<!-- b000339 | prose | pages [15] -->
Another factor toward which the model appeared to be particularly sensitive was the probability governing the rate of accidents in a simulation. Though only three values for this parameter were tested, a non-linear relationship was observed between the number of accidents and the probability governing accident rate. It appeared that once a few accidents occurred in a simulation, they tended to result in many more accidents occurring as well. This presented itself as extremely high accident rates for all simulations of dense traffic with high speed limits and a high probability, far above what would be expected based on the values for other conditions. This might have been partially due to what the extremely high value we set for the probability of random speed ups in these simulations, which was intended to simulate a worst case scenario in terms of driving conditions, but that alone cannot account for the data seen, which must have been partially caused by accident chain reactions.

<!-- b000340 | furniture | pages [15] -->


<!-- b000341 | prose | pages [15] -->
15

<!-- b000342 | furniture | pages [16] -->
Page 16 of 17

<!-- b000343 | furniture | pages [16] -->
Team # 31333

<!-- b000344 | furniture | pages [16] -->


<!-- b000345 | furniture | pages [16] -->


<!-- b000346 | heading | pages [16] -->
5.4 Conclusion

<!-- b000347 | prose | pages [16] -->
With all the data presented to us, we have concluded that the current convention of driving on the right is the safest method of driving. Our data showed us driving with the ability to perform lane changes in either direction, or not being able to change lanes at all would give us faster car flow, but was less safe than the right hand rule. As we are prioritizing driving safely and getting the driver to their destination, we decided that the increased flow rate of the No Rules Method, and the No Change Method was not worth the subsequent increase in accidents in each method.

<!-- b000348 | furniture | pages [16] -->


<!-- b000349 | furniture | pages [16] -->


<!-- b000350 | prose | pages [16] -->
16

<!-- b000351 | furniture | pages [17] -->
Page 17 of 17

<!-- b000352 | furniture | pages [17] -->
Team # 31333

<!-- b000353 | furniture | pages [17] -->


<!-- b000354 | furniture | pages [17] -->


<!-- b000355 | prose | pages [17] -->
6

<!-- b000356 | heading | pages [17] -->
References

<!-- b000357 | references | pages [17] -->
[1.] Courage, Kenneth G., Charles E. Wallace, and Rafiq Alqasem. “MODELING THE

<!-- b000358 | references | pages [17] -->
EFFECT OF TRAFFIC SIGNAL PROGRESSION ON DELAY.” Transportation

<!-- b000359 | references | pages [17] -->
Research Record no. 1194 (1988). http://trid.trb.org/view.aspx?id=302135.

<!-- b000360 | furniture | pages [17] -->


<!-- b000361 | references | pages [17] -->
[2.] Doboszczak, Stefan, and Virginia Forstall. “Mathematical Modeling by Differential

<!-- b000362 | references | pages [17] -->
Equations.” University of Maryland, October 9, 2013.

<!-- b000363 | references | pages [17] -->
http://www.norbertwiener.umd.edu/Education/m3cdocs/Presentation2.pdf.

<!-- b000364 | furniture | pages [17] -->


<!-- b000365 | references | pages [17] -->
[3.] “MIT Mathematics | Traffic Modeling.” Accessed February 9, 2014.

<!-- b000366 | references | pages [17] -->
http://math.mit.edu/projects/traffic/.

<!-- b000367 | references | pages [17] -->
“Nagel–Schreckenberg Model.” Wikipedia, the Free Encyclopedia, February 7, 2014.

<!-- b000368 | references | pages [17] -->
http://en.wikipedia.org/w/index.php?title=Nagel%E2%80%93Schreckenberg_model&old

<!-- b000369 | references | pages [17] -->
id=594319709.

<!-- b000370 | furniture | pages [17] -->


<!-- b000371 | references | pages [17] -->
[4.] National Research Council (U.S.). Traffic Flow Theory, Characteristics, and Highway

<!-- b000372 | references | pages [17] -->
Capacity. Transportation Research Record 1091. Washington, D.C: Transportation

<!-- b000373 | references | pages [17] -->
Research Board, National Research Council, 1986.

<!-- b000374 | furniture | pages [17] -->


<!-- b000375 | references | pages [17] -->
[5.] “What Can Scientific Models Tell Us about the World?” Accessed February 10, 2014.

<!-- b000376 | references | pages [17] -->
http://playingwithmodels.wordpress.com/2010/06/24/should-you-switch-lanes-in-traffic/).

<!-- b000377 | furniture | pages [17] -->


<!-- b000378 | references | pages [17] -->
[6.] R F Benekohal, J. Treiterer. “CARSIM: Car Following Model for Simulation of Traffic in

<!-- b000379 | references | pages [17] -->
Normal and Stop-and-Go Conditions.” Transportation Research Record (1988): 99–111.

<!-- b000380 | furniture | pages [17] -->


<!-- b000381 | references | pages [17] -->
[7.] Schadschneider, Andreas. “Modelling of Traffic Flow.” Accessed February 9, 2014.

<!-- b000382 | references | pages [17] -->
http://www.thp.uni-koeln.de/~as/Mypage/traffic.html.

<!-- b000383 | furniture | pages [17] -->


<!-- b000384 | references | pages [17] -->
[8.] Schreckenberg, Michael, Andreas Schadschneider, Kai Nagel, and Nobuyasu Ito.

<!-- b000385 | references | pages [17] -->
“Discrete Stochastic Models for Traffic Flow.” Physical Review E 51, no. 4 (1995): 2939.

<!-- b000386 | furniture | pages [17] -->


<!-- b000387 | references | pages [17] -->
[9.] “Traffic Flow.” Wikipedia, the Free Encyclopedia, February 8, 2014.

<!-- b000388 | references | pages [17] -->
http://en.wikipedia.org/w/index.php?title=Traffic_flow&oldid=579155609.

<!-- b000389 | furniture | pages [17] -->


<!-- b000390 | references | pages [17] -->
[10.] Werbach, Adam. “The American Commuter Spends 38 Hours a Year Stuck in Traffic.”

<!-- b000391 | references | pages [17] -->
The Atlantic, February 6, 2013. http://www.theatlantic.com/business/archive/2013/02/the-

<!-- b000392 | references | pages [17] -->
american-commuter-spends-38-hours-a-year-stuck-in-traffic/272905/.

<!-- b000393 | furniture | pages [17] -->


<!-- b000394 | references | pages [17] -->
[11.] “What Are Traffic Waves and Why Do They Happen So Much?” The Lowdown.

<!-- b000395 | references | pages [17] -->
Accessed February 9, 2014. http://blogs.kqed.org/lowdown/2013/11/12/traffic-waves.

<!-- b000396 | furniture | pages [17] -->


<!-- b000397 | references | pages [17] -->
17
