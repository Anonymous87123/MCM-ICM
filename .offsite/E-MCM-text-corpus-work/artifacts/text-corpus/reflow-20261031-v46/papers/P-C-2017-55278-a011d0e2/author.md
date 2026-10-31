For ofﬁce use only For ofﬁce use only

T1 F1

T2 F2

T3 F3 Problem Chosen

T4 F4

MCM/ICM

Summary Sheet

Summary

We propose an innovative model based on cellar automata to analyze the effects of self-driving cooperating vehicles on highway trafﬁc capacity. We extend the traditional cellar automata used for trafﬁc analysis to increase the ﬂexibility of our model, so that it can deal with complex dynamics of self-driving vehicles.

Based on the extended cellar automata, we ﬁrst model the car generation process using Poisson distributions. This model generates speciﬁed volume of vehicles on a segment of highway. Our car generation model distinguishes the trafﬁc volumes during peak hours and nonpeak hours. Then we model the behaviors of vehicle-following and lane-changing. In this part, we consider the cooperation between self-driving vehicles and interaction between self-driving and human-driven vehicles. Finally, we propose a probability model to analyze the behavior of trafﬁc ﬂow at highway intersections.

We verify the feasibility of our model by running various simulations. Our model is tested with different percentages of self-driving cars, different lane numbers and trafﬁc volumes. We ﬁnd that self-driving cars can stabilize the performance of trafﬁc system when the lane number and trafﬁc volume change.

Then we apply our model to the data of four highways in the Greater Seattle area. Our results show that the trafﬁc capacity increases with rising percentage of self-driving cooperating vehicles. The average velocity of trafﬁc ﬂow doubles when the percentage increasing from 10% to 50%. And in most cases an equilibria exists after 60%. We also test the effects of dedicated lanes for self-driving cars. We suggest using 70% as a dividing point for whether to use dedicated lanes or not. When the percentage of self-driving vehicles is higher than 70% percent, dedicated lanes can be helpful. We also compare the performance during peak hours with average performance during a whole day, and ﬁnd that self-driving cars signiﬁcantly speed up peak-hour trafﬁc ﬂows.

Finally, we analyze the effect of potential error of self-driving system. We ﬁnd that defects of self-driving system can degrade the beneﬁt to trafﬁc capacity. We also do sensitivity analysis of various parameters, including probability of lane-changing and parameters in the vehicle dynamics, to prove the robustness of our model.

5 Sensitivity Analysis

19

Lane-Changing Probability Pc . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 19

Coefﬁcients α, β, and γ in Vehicle Following Model 5.2 . . . . . . . . . . . . . 20

5.3 Error of Self-Driving Systems . . . . . . . . . . . . . . . . . . . . . . . . . . 20

6 Conclusion

22

7 The Letter

24

1 Introduction

Self-driving is a technology with growing importance in these years. 2016 is the tipping point for excitement in self-driving cars. In October Tesla announced that all of its new vehicles now had the hardware to drive fully autonomously. All that’s left is developing the software. Also, as mobile communication becomes ubiquitous, it is easy to build connections among self-driving vehicles to form cooperative driving systems.

Nowadays trafﬁc jam almost disturbs the daily life of every urban citizen. The arising of self-driving cooperating vehicles has long been a hope to increase the trafﬁc capacity without enlarging the roads, since these vehicles have more accurate control, better sense and prediction of the behavior of ambient vehicles than human-driven ones. In this paper, we make a quantitative and qualitative analysis of the impact on trafﬁc capacity of these newly emerging vehicles.

We establish a trafﬁc ﬂow model based on cellar automata to simulate highway trafﬁc ﬂow. We extend the traditional cellar automata to taking into account acceleration values of vehicles. This extension brings much ﬂexibility when modeling the trafﬁc ﬂow, and enable us to test the impact of more detailed control rules for self-driving cooperating cars.

Our model can be divided into four parts. First, we propose a trafﬁc generation model based on Poisson distributions. This model captures variance of trafﬁc counts during peak travel hours and the non-peak hours. Then, we model the behavior of vehicle-following, which deﬁnes how a car acts according the car running before it. Dif- ferent rules are applied to distinguish the cooperation between two self-driving cars, and interactions between self-driving and human-driven cars. Then, we design a lane- changing model for vehicle movement across lanes. Finally, we build an intersection model to describe how vehicles change from one highway to another through inter- changes.

Then we analyze the feasibility of our model by running simulations with different percentage of self-driving vehicles, different number of lanes and different daily trafﬁc volumes. Under all these simulations our model produces reasonable results, which is consistent with the properties of self-driving vehicles.

After that we apply the provided data. We analyze how the highway capacity changes with the percentage of self-driving cars. Results shows that a equilibria exists at around 50% to 70%. We also study the effect of dedicated lanes for self-driving vehicles, and propose a strategy to allocate such lanes.

Finally, we do sensitive analysis on some parameters in our model. We also consider what if self-driving systems are not perfect. In other words, these autonomous vehicles may not mature enough and new risk can be introduced. We simulate the inaccuracy of a self-driving system by random acceleration and deceleration with a small probability. Results shows that such inaccuracy can degrade the beneﬁt of self-driving vehicles.

1.1 Literature Review

Using cellar automata to analyze trafﬁc ﬂow is widely used by many researchers[1, 2]. This approach has been proved effective to analyze real trafﬁc ﬂow data, and it’s easy to implement. However, none of them consider the scenario with self-driving cars. Their human-driven models lack ﬂexibility to adapt to self-driving vehicles.

On the other hand, studies of self-driving vehicles start up just in recent years. Most of the researches are done by using continuous models with complex simulation soft- wares, and focus on the dynamics of self-driving vehicles and the interactions of several vehicles[3, 4]. But how self-driving technology will inﬂuence an entire highway trafﬁc ﬂow is still not answered.

Some researchers in civil and environmental engineering believe that self-driving technology can increase highway capacity and reduce air pollution[5]. But they didn’t provide quantitative analysis.

In this paper, we propose a brand new cellar automata system which models the impact of self-driving vehicles on highway trafﬁc ﬂow. We extend the traditional trafﬁc ﬂow methods by adding dynamics of self-driving vehicles. We analyze our model with simulations and successfully verify its feasibility. Finally we apply our model to real data and provide constructive advice on trafﬁc management for self-driving cars.

1.2 Assumptions

• Each highway is a straight line without bending.

• Self-driving cars can communicate real time data with each other, including veloc- ity and acceleration.

• Self-driving cars do not need response time to take action as human drivers do.

• Human driven vehicles do not communicate with any other vehicle.

• The width of each lane is only enough for one single vehicle.

• All vehicles are in the same size.

• A car change to another highway through interchanges in intersections, without crossing any trafﬁc ﬂow.

• All human-driven cars are identical and all self-driving cars are identical.

2 The Models

2.1 Basic Settings of Cellar Automata

Cellar Automata has been a widely used model for trafﬁc ﬂow analysis[1]. The road is divided into cells, each cell can have one car or no car on it. A cell also records the current velocity of the car on it, if any. In cellar automata, positions, time, velocity and acceleration are all discrete. The state of a cell is updated according to its current state and current states of its surrounding cells. We apply different updating rules to distin- guish the behaviors of self-driving and human-driven cars in our models.

2.2 Notations

Symbol Meaning s An indicator representing the car type on a cell v Current velocity of a car vnew The newly updated value of v after each iteration a Current acceleration of a car anew The newly updated value of a after each iteration N Daily trafﬁc count of a highway segment n Newly arriving vehicles in a highway segment in one second p Number of peak hours.

q Percentage of self-driving cars G Distance between two cars in the vehicle-following model vp Speed of the preceding vehicle in vehicle-following model ap Acceleration of preceding car in vehicle-following model Tr Response time for a human driver to take action Vmin Minimum velocity allowed on a highway Vmax Maximum velocity allowed on a highway λpeak Rate parameter of Poisson distribution for car generation during peak hours λnon−peak Rate parameter of Poisson distribution for car generation during non-peak hours Trh Response time for a human driver Trs Response time for a self-driving car Tinter Time needed to transfer from one highway to another through an interchange µij Probability of Crossing Interchanges in Intersection Model Pa Acceleration probability when G > GS Pd Deceleration probability when G > GS Pc Probability of lane-changing α, β, γ Coefﬁcients in vehicles following rules (See 2.4.2 and 2.4.3 for details)

2.2.1 Introducing Acceleration into Cellar Automata

Most cellar automata used for trafﬁc analysis, however, only consider the velocity of vehicles[1, 2, 6], without considering accelerations. Whenever the velocity changes, it can only increase or decrease by a ﬁxed value. This is nature for human-driven cars, since human drivers have no accurate data about the behavior of ambient vehicles, they tend to be careful. Also, a human driver has no accurate perception of acceleration, so a cellar automata considering only velocity of cars is enough.

However, researchers of self-driving use acceleration as an important variable in their analysis[3, 7, 8]. In the case of self-driving cooperating vehicles, a ﬁxed acceleration can be a limitation due to their self-driving and cooperating properties.

• Self-Driving Autonomous vehicles are often equipped with accurate sensors[9], complex control system and even artiﬁcial intelligence technology. They can con- trol acceleration accurately. Thus they can steer more ﬂexibly and fearlessly than human-driven ones.

• Cooperating These vehicles can share data including their current acceleration[4], and with these data, they can take more accurate actions to avoid collision as well as make full use of the space of highway. Considering acceleration in our model make more complex cooperating rules possible.

Thus, we extend the traditional cellar automata trafﬁc ﬂow model by adding acceler- ation as an attribute of a cell.

2.2.2 Attributes of a Cell

In our model, a cell represent a 4 meter long space on a single lane, and each cell can only contain one car at a time. A cell has three attributes,

1. An integer s ranging from 0 to 2 (inclusive) to represent the car type. 0 for no car, 1 for human-driven, and 2 for self-driving.

2. Current velocity v a car.

3. Current acceleration a of a car.

Only when s is non-zero does the other two attributes make sense.

In each step of the simulation, a car moves forward by v cells, and v is updated by adding a and bounded by Vmin and Vmax, the speed limitations of highway. Rules are applied to update a according to the states of surrounding cells. For human-driven and self-driving vehicles we have different rules. Speciﬁc updating rules are introduced in following sections.

2.3 Generation Model

We need a model to generate cars for each highway segment. Poisson distribution is appropriate for this task[10]. It expresses the possibility of number of events occurring in a ﬁxed interval of time. Instead of using one Poisson distribution for all time during the day, we use two for peak hours and non-peak hours respectively. Our generation model also controls the percentage of self-driving cars on the way.

Assuming that there are p peak hours in a day and 8% of the daily trafﬁc volume occurs during peak travel hours. With the data of daily vehicle counts, we can calculate the average number of newly arriving cars in one second in each highway segment.

λpeak = 0.08N 0.92N 3600p , λnon−peak = 3600(24 −p)

Suppose the arrival of vehicles follows Poisson distribution, then λpeak and λnon−peak are unbiased estimation for the rate parameters. Thus each second we can sample from the Poisson distributions λn λn non−peak peak n! e−λpeak, e−λnon−peak Ppeak(n) = Pnon−peak(n) = n!

as the number of newly entered vehicles into a highway segment in our simulation, during peak hours and non-peak hours respectively.

By adjusting p, we can control the average frequency of vehicles arriving at peak hours, i.e. λpeak. Since the proportion of peak hour trafﬁc count is ﬁxed at 8%, when p is bigger, these 8% vehicles can arrive at a relatively low frequency. We will simulate with different values of p to test the inﬂuence of peak and average trafﬁc volume on our model. The following ﬁgure shows how λpeak and λnon−peak vary with respect to p, when the daily trafﬁc count is 200, 000.

Car Arriving Frequency

5

Number of arriving cars per second 4

3

2

1

0 1 2 3 4 5 6 7 8 9 Peak Hours

peak non-peak

From Figure 1, when p = 1, we have about 2 newly arriving cars each second on average during peak hours, and about 1 during non-peak hours. As the number of peak hours increase, the trafﬁc density during peak hours decreases and that during non-peak hours increases.

For each car generated from the Poisson distributions, it will be a self-driving car with a probability of q, and a human-driven one with a probability of 1−q. As we adjust q, different percentage of self-driving cars will be on the way.

We set the initial velocity v of a newly arriving vehicle as 20m/s, which is a rela- tively low value. Setting the initial speed slow does not hurt the following simulation, because if the trafﬁc density is low, a higher velocity is allowed, and the vehicle will speed up soon according to our following model. The initial value of acceleration a is calculated according to state of ambient vehicles, using the rules introduced in the vehicle-following model.

2.4 Vehicle-Following Model

Vehicle-Following model deﬁnes the behavior of two cars on the same lane, one run- ning after another. We call the car running in the front preceding car, and the other car follower car.

The vehicle-following model deﬁnes how the follower car changes its velocity and acceleration according to the status of the preceding car. We consider three different cases:

1. The follower car is human driven.

2. The follower car is self-driving and preceding car is human driven.

3. Both cars are self-driving.

In each case, we deﬁne a rule to update the velocity and acceleration of the follower car.

2.4.1 The follower car is Human Driven

When the follower car is human driven, the driver can only try to keep a safe dis- tance with the preceding car, since a human driver needs longer response time than self-driving cars to react when the preceding car decelerates suddenly. Here’s the safe distance of a human driven follower car

GS = Trhv where Trh stands for response time of a human driver. According to the Two Second Rule[11], Trh = 2s is an appropriate setting, which will be used in our simulation.

Human drivers tend to be careful due to potential human error when changing speed. Thus their acceleration is a ﬁxed value. In every second, they can either increase or decrease the velocity by one unit, which is also a convention taken by previous cellar automata based trafﬁc ﬂow analysis.

Thus the behavior of a human-driven cars can be divided into two cases:

• When the current distance G ≤GS, the driver decelerates.

• When G > GS, the driver can accelerate with a probability Pa and decelerate with a probability Pd, and keep the velocity unchanged otherwise. Here Pa + Pd ≤1.

The values of Pa and Pd will be specify later.

When decelerating, the velocity decreases by 1, i.e. vnew = max(Vmin, v −1). When accelerating, the velocity increases by 1 and bounded by the maximum velocity of high- way, i.e. vnew = min(v + 1, Vmax).

Finally let’s specify values of Pa and Pd. When a car runs fast, the human driver tends to slow down. Thus as current velocity v increases, Pa decreases and Pd increases. Each cell is 4 meters long, the maximum speed allowed is 60 miles, which is about 7 cells per second. The following table shows values of Pa and Pd for different v’s.

v 1 2 3 4 5 6 7 Pa 1 0.9 0.8 0.7 0.5 0.2 0 Pd 0 0.1 0.2 0.2 0.3 0.4 0.6

2.4.2 Self-Driving Vehicle Follows a Human Driven Vehicle

Even if self-driving vehicle cannot communicate with the preceding human driver, their sensors can still detect the real time velocity of human-driven car and make a reac- tion immediately. Thus the response time is much shorter than a human driver. The safe distance in this case is still measured by GS = Trsv, but here Trs can take a smaller value than the human response time Trh. We’ll use Trs = 1s in our simulation.

Unlike human drivers, self-driving cars equipped with accurate controller have large ﬂexibility in the control of acceleration, they can adjust their acceleration value con- stantly. In every second, we have the updating rules for its velocity and acceleration

( a ≥0 min(Vmax, v + a), vnew = max(Vmin, v + a), a < 0

anew = α(G −GS) + β(vp −v)

The acceleration of a self-driving car depends on the current distance G, safe distance GS, current velocity v and velocity of the preceding vehicle vp. α and β are positive coefﬁ- cients depicting how much the acceleration depends on (G−GS) and velocity difference (v −vp). When G is greater than GS, the distance is too large thus an acceleration is fa- vorable. Conversely when G < GS the car should slow down. The second term β(vp −v) favors acceleration when the self-driving car is slower than preceding human-driven car, and deceleration when it is faster.

2.4.3 Following Model For Two Self-Driving Vehicles

When both vehicles are self-driving, they can communicate velocity and acceleration constantly. They still need a safe distance GS = Trsv. Since two cooperating cars can communicate, the follower car can get the accurate real time acceleration of preceding car ap. Taking ap into account when updating the acceleration provides further ﬂexibility for a self-driving car.

The updating rules[3] for the follower car are

( min(Vmax, v + a), a ≥0 vnew = max(Vmin, v + a), a < 0

anew = α(G −GS) + β(vp −v) + γap

Adding the term γap, when the preceding car wants to accelerate (ap > 0) or decelerate (ap < 0), the follower car will immediately take corresponding action. Thus this rule makes use of the communication between two self-driving cooperating cars.

2.5 Lane-Changing Model

Besides adjusting its speed and acceleration, each car has a chance to move to the neighboring lane. A lane-changing can happen only when

• Current distance with the preceding car is less than the safe distance.

• The cell on the neighboring lane is empty and distances with preceding and fol- lower cars in the neighboring lane are safe.

Formally, in the case of Figure 2, if GAB ≤GSAB, then car A can change to lane 1 when GAC > GSAC and GAD > GSAD. Here GAC is the distance between car A and C, and GAB is the distance between car A and B. GSAB, GSAC and GSAD are safe distances between A and B, A and C, and A and D respectively. They are deﬁned in the same way as vehicle-following model, according to the categories of the cars.

When only one neighboring lane satisﬁes the condition, the car changes to that lane with a probability Pc. When both left and right lanes satisﬁes the condition, the car changes to either lane with a probability Pc/2.

Lane-changing happens before the velocity and acceleration update in the vehicle- following model. After lane-changing, the velocity and acceleration of a vehicle are up- dated according to the rules in the vehicle-following model.

2.6 Intersection Model

Most high way intersections are based on interchanges, a structure that allows high- way to pass through the junction without directly crossing any trafﬁc stream. Thus in an intersection, a car in one highway can move to another highway without waiting for a trafﬁc light. We will use cloverleaf interchange in our model, since it is the most widely used one. Figure 3 shows the trafﬁc ﬂow on a cloverleaf interchange. A car in Position A on Lane 2 can move to Position B on Lane 3 or Position C on Lane 4. Similarly, a car can enter Lane 2 from Position D on Lane 3 and Position E on Lane 4. The trafﬁc ﬂow on Lane 1 has a similar interaction with trafﬁc ﬂow on Lane 3 and Lane 4.

Because there’s no crossing through the trafﬁc stream, we can assume the car disap- pears from one highway and appears on another one after a period of time.

With this assumption, we introduce 8 parameter µij and µji, for all i ∈{1, 2}, j ∈ {3, 4}, to represent the probability of cars moving from Lane i to Lane j, and from Lane j to Lane i respectively. Assuming all these movements across the interchange takes time Tinter. We summarize the rules for intersection crossing as follows

• When a car arrives at the intersection, with probability µij, its movement from Lane i to Lane j starts.

• If the movement starts and Tinter seconds pass after that, check if the destination position on Lane j is empty. If so, put the car on that position with its old velocity and update its acceleration with the rules in the vehicle-following model. Other- wise, the car has to wait until the position becomes empty.

The intersection model is simulated by running four cellar automata using vehicle- following rules and lane-changing rules, and the intersection rules deﬁned above. De- tails are deferred to the simulation part.

3 Analyzing the Model by Simulation

We analyze how the highway capacity varies in our model when the percentage of self-driving vehicles, number of lanes and trafﬁc volume change. We run the simulation on a highway segment of 250 cells long, which is 1000 meters. Each simulation runs for a trafﬁc ﬂow of 24 hours, using the generation model to generate vehicles.

The simulation results shows that self-driving vehicles increases the highway capac- ity. We also compare the effects of self-driving vehicles with other factors.

3.1 Criteria

To evaluate the trafﬁc capacity, we need some criteria. In our simulations, we mainly use average passing time and trafﬁc density.

• Whole-Day Average Passing Time The average time for a vehicle to pass the 250- cell long highway segment.

• Peak-Hour Average Passing Time The average time for a vehicle to pass the 250- cell long highway segment during peak hours.

• Trafﬁc Density Number of vehicles on the 250-cell long highway segment. This value will change with time as the cars run in and out the highway. So for each combination of model parameters, we can obtain a curve of trafﬁc density varying with time. Since the trafﬁc load is a time dependent value, we can further use it to analyze the stability of a trafﬁc ﬂow.

3.2 Effects of Percentage of Self-Driving Vehicles

We run the cellar automata on a highway segment, varying the percentage of self- driving vehicles to observe the change of highway capacity. The highway segment has 3 lanes on both directions. We ﬁxed the daily trafﬁc volume at 100, 000, with 50, 000 on each direction. The lane-changing probability Pc = 0.5. Number of peak hours in the generation model is p = 1. We calculate the average time to pass through the highway segment and trafﬁc load. Figure 4 and Figure 5 show the results.

We have following observations when the self-driving percentage increases.

• Average passing time reduces: As the percentage of self-driving vehicles increases, the average passing time during peak hours decreases sharply at ﬁrst, and reach a equilibria at around 70%. Self-driving vehicles can increase the trafﬁc capacity by more accurate control and cooperating. The beneﬁt is tiny when the percentage of self-driving car is low. Because cooperation is difﬁcult with few self-driving cars on the road.

• Peak-hour pressure is alleviated Self-driving cars reduce the difference between peak-hour passing time and whole-day passing time. In Figure 4, as the percentage of driving cars increases, the blue curve and black curve get closer. This reveal an important advantage of self-driving cars, that they are ﬂexible enough to deal with peak hours.

• The space capacity of highway increases: In Figure 5, as the percentage of self- driving cars increases, average number of vehicles on the 250-cell highway seg- ment reduces. When self-driving percentage is low, cars on the road moves slowly, as indicated in Figure 4. Thus, trafﬁc jam is easy to arise, which result in many cars being stuck on the road. With more self-driving cars, trafﬁc jam can be relief.

Again, the impact of self-driving car is more obvious during peak hours.

3.3 Effects of Lane Number

We run simulations with 3, 4 and 5 lanes on both directions respectively. The daily trafﬁc volume is 100, 000, with 50, 000 on each direction and number of peak hours p = 1. The lane-changing probability Pc = 0.5. And the self-driving percentage is 50%.

We also test the effects of lane number with different self-driving percentage. We simulate lane numbers 3, 4 and 5 with self-driving percentage 30% and 70%.

We have two important observations based on Figure 6 and Figure 7.

• More lanes can speed up trafﬁc ﬂow: Both during the whole day and peak hours, adding lanes to the highway shorten the average passing time. This is consistent with our intuition. Because with more lanes on the highway, cars have more free- dom to change lane when the current lane is too crowded.

• Self-driving reduces the impact of lane number: Both in Figure 6 and Figure 7, as self-driving percentage increases, the three curves get closer to each other. When most of the cars are self-driving, adding more lanes to the highway make small difference.

(Whole Day) (Peak Hours)

3.4 Effects of Dedicated Lanes for Self-Driving Cars

This section we discuss how our model reacts to dedicated lanes for self-driving cars. To test the effects of dedicated lanes, we modify the generation model and lane-changing model.

• Generation Model When a self-driving car is generated, we put it to one of the dedicated lanes.

• Lane-Changing Model A self-driving car cannot change to a non-dedicated lane.

Impact of Dedicated

Impact of Dedicated Lanes (Whole Day) Lanes (Peak Hours) With these modiﬁcations, run the simulation with 5 lanes on both directions. The daily trafﬁc volume is 100, 000, with 50, 000 on each direction. The number of peak hours p = 1. The lane-changing probability Pc = 0.5. We increase the dedicated lanes from 1 to 3 and calculate the average passing time, when self-driving percentage is 30%, 50% and 70% respectively.

From Figure 8 and Figure 9, when the percentage of self-driving vehicles are small, dedicated lanes may hurt the trafﬁc capacity, especially during the peak hours. For ex- ample, in Figure 9, when there are only 30% of self-driving cars, 3 dedicated lines results in an average passing time of 80s, which is much slower than other cases.

However, as the percentage of self-driving cars arises, dedicated lane can improve the performance by a little. For example, in Figure 9, when 70% are self-driving, any number of dedicated lanes outperforms no dedicated lane strategy.

3.5 Effects of Trafﬁc Volume

Different daily trafﬁc volume from 100, 000 to 500, 000 are tested. The trafﬁc volume are distributed to both directions equally. Each direction has 5 lanes. The lane-changing probability Pc = 0.5. Fix the number of peak hours p = 1. Simulations are done for 30%, 50% and 70% of self-driving cars.

(Whole Day) (Peak Hours)

The impact of trafﬁc volume reduces as percentage of self-driving cars increases. Thus self-driving cars can maintain the highway capacity well even when the trafﬁc is quite heavy.

4 Apply to the Real Data

We apply our model to the provided data of Interstates 5, 90, and 405, as well as State Route 520. We test how trafﬁc capacity of these roads changes with the percentage of self-driving cars. We also analyze the feasibility of dedicated lanes, and give suggestions based on our analysis.

4.1 Percentage of Self-Driving Vehicles

We run simulation for each segment on the data sheet, study the impact of self- driving vehicles on highway capacity during the whole day and during peak hours. Though self-driving vehicles do not increase the highway capacity a lot on average dur- ing the day, but they have a signiﬁcant impact during the peak hours.

4.1.1 Average Velocity During a Whole Day

In the data sheet, 224 highway segments are listed. These segments belong to four roads, Interstates 5, 90, and 405 and State Route 520. For each segment and its corre- sponding daily trafﬁc count, we test the average velocity vi, i = 1, 2, ..., 224 of cars pass- ing through the segment during a day. Then we calculate the average velocity for each road, by averaging vi’s of the segments belonging to the road.

On each road, the average velocity increases with percentage of self-driving vehicles. As the percentage of self-driving cars increases from 10% to 50%, the average velocity increases rapidly. However, when the percentage changing from 50% to 90%, the average velocity only increases by a little. An equilibria is reached at around 80%.

The average velocity increases most markedly when percentage of self-driving vehi- cles changes from 0% to 10%, and from 10% to 20%.

4.1.2 Average Velocity During Peak Hours

Average velocities of each road during peak hours are calculated in the same way as 4.1.1.

Compared with Figure 12, we found self-driving has a more signiﬁcant impact for peak hour trafﬁc ﬂow. The average velocities on all four roads experience a huge increase as self-driving percentage increases. For example, when the percentage increases from 10% to 50%, average velocity on Route 5 increases by about 10m/s, and by about 5m/s when the percentage increases from 50% to 90%. An equilibria is reached at around 70%.

4.1.3 Trafﬁc Density

We calculated the average trafﬁc density of the four highways. We record how many trafﬁc are there on each road per second when doing the simulation in 4.1.1 and 4.1.2. Then we calculate the average number of cars per second per kilometer.

From Figure 14 and Figure 15 self-driving cars help reduce the trafﬁc density of each road. Again, the impact is more signiﬁcant during the peak hours. In Figure 15, the trafﬁc density decreases rapidly when the percentage of self-driving is low. From 10% to 50%, the trafﬁc density reduces by half. While from 50% to 90%, there’s no signiﬁcant change. An equilibria is reached at around 50%.

Cars on Trafﬁc Density (Whole Cars on Trafﬁc Density (Peak Day) Hours)

4.1.4 Average Velocity at Intersections

We apply the intersection model to simulate the trafﬁc ﬂow at the mile post 152.72 to 155.18 of Interstate 5 highway, where it intersects with Interstate 405 (mile post 0 to 0.09). We calculate the average velocity of vehicles during the whole day. Each vehicle running through mile post 152.72 to 155.18 on Interstate 5, or on mile post 0 to 0.09 on Interstate 405 may cross the interchange or not, with all the probabilities in the intersection model being 50%. We set Tinter, the time to cross interchange, as 10s. We get similar result as in straight results.

4.2 Dedicated Lanes

Impact of Dedicated

Impact of Dedicated Lanes (Whole Day) Lanes (Peak Hours)

We pick the data of Interstate 5 to analyze effects of dedicated lanes. Figure 17 and

lanes for self-driving cars.

When self-driving cars take a small proportion, dedicated lanes do not help to in- crease the average velocity a lot. However, when most vehicles are self-driving, for example 70%, dedicated lanes become necessary.

5 Sensitivity Analysis

We analyze the sensitivity of some parameters in our model. We run simulations on a 250-cell long high way segment with 5 lanes, and no dedicated lane. The daily trafﬁc count is 100, 000. With this setting, we analyze how the parameters in our model inﬂuences our conclusion. The results show that our model is quite robust.

5.1 Lane-Changing Probability Pc

In our previous experiments, the default value of Pc is 0.5. So when the distance G be- tween two cars is less than safe distance GS, the follower car will change to another lane with probability 50%. Here we test the impact of self-driving cars on highway capacity with different Pc’s.

When Pc = 0.2, the cars tend to stay on the same lane even if it is crowded. Thus the average passing time for a car is longer. While Pc = 0.8, the cars change lanes frequently to make use of spare spaces, so the average passing time is shorter. However, the differences with Pc = 0.5 are small.

5.2 Coefﬁcients α, β, and γ in Vehicle Following Model

Recall that α, β and γ are coefﬁcients used in the update of the acceleration of self- driving vehicles in Section 2.4.2 and 2.4.3. Our default setting is α = β = γ = 1. Recall the updating rule anew = α(G −GS) + β(vp −v) + γαp

Thus α control how much the acceleration depends on distance. β controls the impact of relative speed. And γ controls the impact of acceleration of the preceding car. When α is bigger, the follower car tends to keep a safe distance. When β is bigger, the follower car tries to catch up the speed of the preceding car. And when γ is big, the follower car will accelerate synchronously with the preceding car.

We test different combinations of α, β and γ. The results are shown in Figure 20. We see a tiny speed up of trafﬁc ﬂow when they are larger.

5.3 Error of Self-Driving Systems

In our model, we assume self-driving cars are perfect. They don’t introduce any new risk. However, as a newly emerging technology, self-driving today is not mature enough. On June 30, 2016, a fatal crash of self-driving Tesla was reported. The driver was killed. Thus, it is necessary to test how system error will affect the performance of self-driving cars.

We introduce self-driving system error by making self-driving cars accelerate or de- celerate by 1 unit both with a probability of 10%. The result is shown in Figure 21. As we can see, such inaccurate acceleration and deceleration will degrade the performance, resulting longer passing time compared with perfect self-driving systems.

6 Conclusion

In this paper, we build a model to analyze the impact of self-driving cars on highway capacity. We analyze our models with many simulations. And ﬁnally we apply our model to the data of four real highway. Here we conclude our interesting ﬁndings.

• Self-driving vehicles can increase highway capacity. As the percentage of self- driving cars increases, the trafﬁc ﬂow proceeds with higher velocity, and lower space density.

• Dedicated lanes for self-driving cars are not necessary when the percentage of self- driving cars is low, while dedicated lanes can increase the capacity by a little when the percentage is higher than 70%.

• Self-driving vehicles can reduce the impact of lane number and trafﬁc volume.

When most of the cars are self-driving, the velocity of a trafﬁc ﬂow do not change a lot with these factors.

7 The Letter

Dear Ofﬁcials,

It’s our honor to help you with analyzing the effects of allowing self-driving, coop- erating vehicles on capacity of highways in the Greater Seattle area. We are writing this letter to report our latest ﬁndings.

We have built a novel Cellar Automata Model to analyze the effects of allowing self- driving, cooperating cars on Interstates 5, 90, and 405, as well as State Route 520 in Thurston, Pierce, King and Snohomish counties. By running simulations with different percentage of self-driving vehicles, different number of lanes and different daily trafﬁc volumes, we analyze the feasibility of our model and then apply it to the real data. The results show that self-driving and cooperating cars can increase highway capacity. In other words, they can relieve the stress of trafﬁc jams.

The capacity of highway increases markedly when there are 10% self-driving vehi- cles, and reach an equilibria at around 70%. Speciﬁcally, the average velocity of trafﬁc ﬂow increases with the arising percentage of self-driving vehicles. Also, the trafﬁc den- sity on the road decreases with more self-driving vehicles.

These vehicles are equipped with accurate sensors and intelligent control systems. So they require shorter safe distance with other vehicles and have higher ﬂexibility of acceleration and deceleration. These properties enable them to make full use of the space on highways and accelerate the overall trafﬁc ﬂow.

What’s more, these vehicles can communicate with each other and share data in- cluding velocity and acceleration. Such communication makes the synchronous actions between two vehicles possible and eliminate potential collisions even when two cars are very close to each other. They can also test the real time velocity of ambient vehicles, and adjust their own speed accordingly.

Based on our analysis, we provide some suggestions to better manage and exploit self-driving vehicles:

1. Popularize self-driving vehicles, even only a little bit. Our analysis shows most

beneﬁt to trafﬁc capacity happens when the percentage of self-driving increases from 0% to 50%. Since self-driving vehicles are not very popular now, huge im- provement can be achieved even increase the number of these vehicles by a little.

2. Do not hurry to build dedicated lanes for self-driving cars. Our simulations sug-

gest that dedicated lanes can only be helpful when the percentage of self-driving cars is high enough, for example 70%. Allocating dedicated lanes can increase the overhead and can be expensive. Since few self-driving vehicles are on the road to- day, such dedicated lanes may even hurt the trafﬁc system by making other lanes for human-driven cars too crowded.

We believe our model is useful for management of self-driving cars in the future. You’re welcome to contact us at any time for further cooperation.

Yours Sincerely,
