Problem Chosen 2022

MCM/ICM

Summary Sheet

Summary

In this paper, we want to figure out the power curves of different riders and how riders can allocate their power during the course to get better performance in an individual time trial competition.

To begin with, We design the Muscle Fatigue-Recovery Model and the Energy Reserve Model, and combine them to obtain the Rider Power Output Model. Then, we use the data from the "maximum-effort" experiment in [4] [5] to adjust the model parameters. After that, we take both male and female of Time Trial Specialist(TTS) and Sprinter as examples, obtaining their power curves by using our model.

Next, We collect the coordinate information of real-world road points from Google Earth, to build a data structure of roads and define its attribute fields to re-express the road elevation, length, curvature and other attributes in the computer. Thus the bike course can be visualized.

Then, using the bike course information, we model the Newtonian mechanics of the bicycle and established the equations of motion of the rider based on Newton’s second law.

Later, based on these three models, we formally define the power planning optimization problem. The optimal solution of this problem is found by dynamic programming algorithm.

Furthermore, based on this model, we add the environmental factors of wind speed, wind direction, and the ground humidity. Besides, we investigate the effect of the rider on the execution error of the plan.

Finally, we modified the parameters of the previous model to simulate Team Time Trials, in which teams often use the "mountain train" tactic: the team members line up to minimize overall air resistance by finding information and processing data in [13].

Based on the above modeling, we can draw the following conclusions:

1. For a relatively undulating section of road, the optimal power planning plan for the Sprinter is to power up at the beginning and on uphill section, and to ride at a lower power on the relatively gentle sections of road to preserve energy. For the TTS, the opposite is true.

2. Gender makes no significant difference to the above strategy.

3. Higher ground humidity and stronger headwinds will lengthen the time for riders to finish the race, while lower ground humidity and stronger tailwinds will shorten the time.

4. If a riders do not follow a highly detailed plan and miss the power targets, their finishing time will be longer.

5. In Team Time Trials, thanks to the "mountain-train" strategy used in the team competition, the average wind resistance for each rider is reduced, allowing the team to move at a faster pace.

1 Introduction

1.1 Problem Background

Cycling races are very popular worldwide, especially The Individual Time Trials (ITTs) and The Team Time Trials (TTTs), ITTs are also referred to as "the race of truth", as winning depends on each rider’s strength and endurance, and also depend on how well the rider distributes the power according to roads conditions. In order to make the rider get better results, it is very important to analyze how rider with different physical conditions (physical energy reserve, physical recovery ability, explosive ability, etc.) for riding scientifically and rationally in different road conditions by mathematical modeling.

1.2 Restatement of the Problem

1) Firstly we are required to establish a model about the riders according to riders’ physical attributes, and the model can output the power curve of the rider which indicates how long a rider can produce a given amount of power.

2) After modeling the riders themselves, we need to model how should that rider apply power while traversing a given time trial course. To solve this problem, we should consider road conditions, environmental factors, and the rider’s own model.

3) After this we should consider the variation of results obtained when the rider performs deviations from our model.

4) Finally we need to solve the Team Time Trials situation in our model.

In order to solve those problems, we will proceed as follows:

• Design the Rider Power Output Model. We design the Rider Power Output Model and rectify the parameters of the model

• Discrete and Visualize the Roads. We get the data of roads from Google Earth, and then discrete them into segments and visualize them with the help of Python.

• Design the Newtonian Mechanics of Cycling. By analyzing the physical model of the bicycle and combining it with the two-point environmental data of the track, we propose the Newtonian mechanics of cycling.

• Solving problems using dynamic programming. The cycling time trial speeding strat- egy as an optimal control problem and used dynamic programming to solve this optimal control problem.

• Modify Model Parameters to Fit Different Problems. We modify our model parameters to simulate the performance of athletes in different environmental conditions. Similarly, we modify our model parameters to simulate the team performance in a team competition.

1.3 Literature Review

Over the decades, scientists have done a lot of work to understand the physiological concepts behind the athletic performance of riders. Among them, the concepts of critical power (CP) and anaerobic work capacity (AWC) have been frequently discussed in recent articles on the subject, and there are also articles proposing more classical models of muscle fatigue and recovery based on CP and AWC[1]. Not only that, some articles have proposed a muscle fatigue recovery model based on static force derivation[2]. In addition, the power output model based on the physical performance of cyclists also has some validity[3].

Scientists have not only worked on human muscle models, but also in the area of human data measurement. Dajo Sanders et al. used data from professional cyclists on a World Cycling Tour team. They used maximal aerobic force, peak sprint force output, and an exponential constant describing the decay of force over time to establish force-duration relationships for each participant [4]. N. J. Rehrer et al. measured EI (energy intake) and EE (energy expenditure) of athletes in a six-day, 10-stage cycling race [3]. Tammie R. Ebert et al. collected power output data from 31 Australian national male road cyclists over 6 years and 207 races and subjected the subjects to a maximum graded exercise test in the laboratory to determine maximum aerobic power output [5].

S. Alireza Fayazi et al. described the cycling time trial speeding strategy as an optimal control problem and used dynamic programming to solve this optimal control problem [2]. Dy- namic programming is both a mathematical optimization method and a computer programming method. The method was developed by Richard Bellman in the 1950s. Dynamic programming refers to simplifying complex problems by decomposing them into simpler subproblems in a recursive manner [6].

2 Assumptions and Justification

In order to simplify the problem and make it convenient for us to simulate the real conditions, we make the following assumptions, and each of them is properly justified.

• All the data we have collected are accurate. The data we collect through various means are measured in different environments, at different times, and on different tracks, and are inevitably interfered with by errors caused by variables that have not been taken into account. Also, the equipment used to measure these data cannot be completely free of measurement errors. So in our model, we assume that all the data we collect are accurate.

• At the beginning of a competition, the athletes always reach their optimal initial physical condition. The initial physical state of a rider at the beginning of a race is not necessarily always the most initial physical state he or she can achieve due to the effects of the rider’s sleep and diet in the days leading up to the race. This uncertainty is troublesome for modeling purposes. In our model, we assume that at the beginning of the race, the athlete always reaches his or her optimal initial body state.

• The athletes always choose the most suitable bike gear for the current road. Choosing larger gears on a flat road is inefficient, and choosing smaller gears on a ramp is time- consuming and laborious. A more reasonable approach is to select smaller gears on a flat road and larger gears on a ramp. In our model, we assume that the rider can always choose the corresponding most available gear on different sections of road.

• No unexpected situations arise during the athletes’ competition. We assume that our simulated athletes are not unwell, fallen or injured during the race. We assume that our athletes finished the race under ideal conditions.

• The environmental parameters are constant over the course of the competition.

Some bike races last for hours or even days, during which the weather and environment may change significantly, such as rain versus sunshine. But we assume in our model that the environmental parameters are constant during the race.

• Male and female riders finish the same number of laps. In order to compare the performance of male and female riders on the same course, we assume that male and female riders finish the same number of laps.

3 Notations

Symbols

Description Unit

Pmax W The maximum power can be released by the muscle at the current state

Pmax0 W The maximum power can be released by the muscle at the initial state

Prider W The output power of the rider at the current time

kf 1 Muscle fatigue coefficient

kr 1 Muscle recovery coefficient

E J body energy reserves at the current time

E0 J Initial body energy reserves

Pin W Energy recovery rate

Pout W Energy output rate

kin 1 Energy recovery coefficient

mb, mr, mt kg Mass of the bicycle, the rider and the total mass of them

kwheel 1 Bicycle power conversion coefficient m2 A Frontal area of the rider

Cd 1 Air drag coefficient

v m/s Velocity of the rider kg/m3 ρ Air density

µ 1 Rolling friction coefficient

θ rad The inclination angle of a road

where we define the main parameters while specific value of those parameters will be given later.

4 Our Model

4.1 Rider Power Output Model

The power output of a cyclist during a race is determined by a variety of factors, such as the athlete’s sleep, diet, mood, muscle state (maximum power output, fatigue resistance, fatigue recovery ability, etc.), fitness state (initial fitness, fitness recovery ability), weather and temperature at the time of the race, etc. Therefore, for such a complex human power output system, we consider it in two combined single models: muscle fatigue-recovery model and human energy reserve model. We rectify the parameters of our model with data from real athletes, and finally obtain the power curves of different athletes. The power curves of athletes obtained from our model overlap well with the power curves of real athletes.

4.1.1 Muscle Fatigue-Recovery Model

The main power generating muscles of cyclists are the quadriceps, gluteus maximus and gluteus medius, as shown in the figure. The maximum power that can be exerted by pedaling a bicycle is a decreasing function of the level of muscle fatigue. In this paper, we use a single-state dynamic model to capture changes in the maximum power that can be output by an athlete’s current muscles. The results of [7] justify the integration of the effects of the major physiological factors that contribute to fatigue.

We assume that Pmax is the maximum power that the athlete’s muscles can output in the current state, and its initial value is Pmax0 (i.e., the amount of maximum power that the athlete can output in the best condition of the muscles), and Prider is the current power output of the athlete’s muscles. The larger Prider is, the faster the athlete’s muscles fatigue, and the faster Pmax reduces. The results of several experiments in [8] support the following model:

dPmax(t) = −kf · Pmax(t) · Prider(t) (1) dt Pmax0 fatigue Where kf is the muscle fatigue resistance coefficient, and kf varies for each individual.

Muscle recovery also increases almost exponentially and the muscle recovery process can be represented by the following model [8]:

dPmax(t) = kr · (Pmax0 −Pmax(t)) (2) dt recovery Where kr is the muscle fatigue recovery coefficient, and kr varies for each individual.

However, the fatigue and recovery of an athlete’s muscles are not completely separated in time. Each time a group of muscle fibers is in activation mode, some will fatigue and some will recover[2]. In other words, muscle fatigue and recovery occur simultaneously. To reflect this simultaneous occurrence, we combine equations (1) and (2) to obtain the muscle fatigue-recovery model:

dPmax(t) = −kf · Pmax(t) · Prider(t) + kr · (Pmax0 −Pmax(t)) (3) dt Pmax0

4.1.2 Energy Reserve Model

We know that the body’s blood sugar levels fluctuate within a certain range during human exercise. Blood sugar is the main source of energy for aerobic exercise, such as cycling. As blood sugar is consumed, liver glycogen is broken down into blood sugar to increase blood sugar levels. At the same time, it is common sense that a cycling race will not deplete the athlete’s liver glycogen. Thus, the blood glucose concentration can be stabilized within a certain range during the race. As a result, we designed the following energy reserve model:

Pin(t) = kin · (Pmax0 −Pmax(t)) (4) Pout(t) = Prider(t) + Pother(t) = kout · Prider(t) (5)

Z t Z t Pin(t)dt − E(t) = E0 + Pout(t)dt (6) 0 0 Where E is the total amount of directly usable energy, which can be used to represent blood sugar concentration, and E0 is its initial value, i.e. the total amount of energy directly usable by the athlete after sufficient rest; Pin is the rate of energy replenishment, which can be used to represent the rate of hepatic glycogen breakdown; Pout is the rate of energy output, which can be used to represent the rate of blood sugar consumption; and Pother is the power of energy consumed by the athlete for physiological activities other than mechanical output.

The interpretation of equation (4) is that the rate of energy replenishment is proportional to the degree of muscle fatigue, where kin is the energy replenishment coefficient.

The interpretation of equation (5) is that the energy output rate of the athlete consists of the mechanical output rate of the muscles and the rate of energy consumption by other physiological activities. Pout is approximately proportional to Prider throughout the course of the competition, and kout is this proportional parameter.

The athlete’s output power is determined by both the muscle fatigue-recovery model and the energy reserve model.

(1) When the athlete’s muscles are fatigued and energy reserves are abundant, the maximum output power of the athlete’s muscles is limited by the degree of muscle fatigue.

(2) When the athlete’s muscle energy reserves are depleted and the muscle is not too fatigued, the maximum output power of the athlete’s muscle is limited by the energy reserves.

working together. The blue curve is the power curve of the athlete with more abundant energy reserves, and we can see that the maximum power output of this athlete is limited only by the degree of muscle fatigue (no point where the curve turns); the orange curve is the power curve of the athlete with average energy reserves, and the maximum power output of this athlete is determined by the degree of muscle fatigue at shorter times. The green curve is the power curve of an athlete with low energy reserves, whose muscle output rate is limited by energy reserves for a shorter period of time than the previous athlete (the point at which the curve turns is smaller).

4.1.3 Parameter Rectification

In our model, an athlete’s ability can be represented by six parameters in full: kf, Pmax0, kr, E0, kin, kout. In order to obtain different model representations for different athletes, we design different parameters for different athletes. We used data from the "Maximum-Effort" experiment in [4] to design the parameters: the "Maximum-Effort" experiment refers to an athlete sprinting with all his or her strength on a flat section of road after a full rest and recording the athlete’s power output during the process. We found the parameters that best fit the data from the actual athlete’s "Maximal-Effort" experiment and recorded them as follows:

kf kr kin kout Pmax0(J) E0(J) type 106 TTS(male) 0.0416 0.0104 1.11 1.50 1000 8 ×105 TTS(female) 0.018 0.00901 1.18 1.46 900 106 Sprinter(male) 0.057 0.001078 0.50 1.57 1500 8 ×105 Sprinter(female) 0.046 0.0009 0.53 1.52 1300

4.1.4 Power Curve

The power curve represents the maximum power that the rider can maintain for a given length of time. We obtained the power curves for different types of athletes using the following algorithm.

Algorithm idea: constant output power P, find the maximum length of time that the athlete can adhere to this power output.

Algorithm 1 Draw the Power Curve

Input: kf , kr , kin , kout , Pmax0(J) , E0(J): Parameters for the athlete Output: the Power Curve of the athlete 1: tlist=[] 2: Prider_list=[] 3: for Prider = 100; Prider < 1500;Prider + + do E = E0 4:

for i = 1; i < 800; i + + do 5:

update the value of Pmax 6:

update the value of E 7:

if Prider > Pmax or E < 0 then 8:

t = i 9:

break 10:

end if 11:

end for 12:

tlist.append(t) 13:

Prider_list.append(Prider) 14: 15: end for 16: plot(tlist, Prider_list)

4.2 Roads Discretization and Virtualization

For Applying our model to various time trial courses, we built discrete virtual courses using data from two real-world cycling courses in Fig.6, the 2021 Olympic Time Trial course in Tokyo, Japan and the 2021 UCI World Championship time trial course in Flanders, Belgium in Fig.7, and we designed a reasonable cycling course of our own.

4.2.1 Discretization of the Cycling Courses

We calibrated the discrete data points (each point contains its latitude, longitude and altitude information) on the real bike courses on the Google Earth. For the straight roads,the two discrete data points to form them are farther apart, while for the curves, the discrete data points are closer together in order to get better precision.

For a point we got from Google Earth, we define it as a three-dimensional vector ′ = (x ′, y ′, z ′) p

′ is the latitude, y ′ is the longitude, z ′ is the height. Where x

And since the first two dimensions of the information points store latitude and longitude information, we converted them to planar two-dimensional coordinates in meters to achieve higher precision.

So we choose a reference point from the bike course as the origin, and based on the radius of the earth, we can calculate the length of the first two dimensions relative to the origin, so that each of our points becomes p = (x, y, z)

x and y are the coordinates length of the point relative to the origin on its course map, and z stay the same, so we can reconstruct and display the whole map on the axes in the program simulation like Fig.8.

4.2.2 The Data Structure Definition of the Road

After we collected information about the points from the Google Earth, we define the data structure of the road which is basically composed of two points in our model.

For the roadi where the i is the index the road in the roads list, and we assume that the points p(1) and p(2) are the start point and the end point of the roadi, we can obtain these properties i i below q  i .x)2 + (p(1) i .y)2 + (p(1) (p(1) i .x −p(2) i .y −p(2) i .z −p(2) i .z)2 Li =    ∆hi = p(1) i .z −p(2) (7) i .z ∆hi θi = arctan   q  (p(1) .x−p(2) .x)2+(p(1) .y−p(2) .y)2 i i i i where Li is the length, ∆hi is the height difference and θi is the inclination angle of the roadi

4.2.3 Radius of Curvature Definitions of Points and Roads

In order for our model to incorporate the effect of curves, we introduce the concept of radius of curvature of points and roads.

For a given data point pi on the cycling course,the radius of curvature of it, donated as R(pi), is the radius of the excircle of the triangle formed by pi−1, pi and pi+1. If pi+1 or pi−1 do not exist, which means that pi is one of the end points of the whole course, the radius of curvature of pi is not defined.

For a given road whose end points are pi and pi+1, if radius of curvature of both points exist, the radius of curvature of it is R(pi)+R(pi+1) . Otherwise, the road is the beginning or ending road 2 of the course, and the radius of curvature of it is pi+1 for beginning, pi for ending.

As shown in Fig.9, the larger the radius of curvature, the closer the section of road is to a straight line.

4.3 Newtonian mechanics analysis of cycling

4.3.1 Cycling on a straight course

According to Newton’s second law and neglecting the inertial effect of wheel rotation, the longitudinal model of the bicycle is assumed as follows

Prider −1 2CdρAv2 −mtg(µ cos θ + sin θ) −Fb mta = krider (8) v

where mt is the total mass of the cyclist and the bike, a donates the acceleration of the cyclist. Thus mta, according to Newton’s second law, equal to the net force apply to the system.

In general, cyclists have two degrees of freedom in managing their own road planning: the freedom to plan their own output power, and the freedom to plan their own gear set selection, based on road information. We assume that the cyclists are fully trained players who can optimally select gear sets based on their experience. krider indicates the conversion efficiency of the player’s output power to the bike under the gear set chosen by the player.

Prider Therefore,krider donates the output force from the cyclist to the bike. v 2CdρAv2 represents the amount of air resistance to the cyclist, where Cd is the air drag 1

coefficient, ρ is the air density at the race course, which decreases with increasing altitude, A and v are the frontal area and velocity of the rider,respectively.

The mtg(µ cos θ + sin θ) term is the combined force of the frictional resistance µmtg cos θ and the sliding force mtg sin θ on the cyclist’s system. µ is the rolling friction coefficient between the bicycle tires and the road. θ is the inclination angle of a given road.

Fb donates the resistance of the brake pads to the tires when the player decides to brake.

Typical values of the above variables are shown in the following table.

Symbols

Description Value

mt 60kg Total mass of bicycle and cyclist

kwheel 0.99 Bicycle power conversion coefficient 0.35m2 A Frontal area of the rider

Cd 0.05 Air drag coefficient 1.1kg/m3 ρ Air density

µ 0.003 Rolling friction coefficient

4.3.2 Cycling on a curved course

When a cyclist rides on a curve, a component of static friction is needed to provide the centripetal force required for his turn.

For a section of road with radius of curvature R, when the cyclist’s speed is v, mass is mt, the required centripetal force is mtv2 R . Therefore, if the maximum static friction force is µ0mtg cos θ, the velocity of the cyclist can not exceed √µ0g cos θR.

4.4 Formalization and Numerical Solution of the Optimizing Problem

In the above section, we systematically established a mathematical model of the cyclist’s body muscles, the physical properties of the bike, and the physical properties of the cycling courses.

In this section, we try to formally define the optimization problem of minimum time in an Individual Time Trail race and solve the problem using dynamic programming (DP).

4.4.1 Formalization of the Problem

In an Individual Time Trail race, the goal is to reach the finish line in as short a time as possible. Therefore, we formally define our optimization problem as follows.

Z tf Z xf   dx Prider(t) T = min min dt = min (9) v(t) Prider(t) Prider(t) t0 x0 subject to, 0 ⩽v(t) ⩽min{vmax, √µg cos θR} velocity limits:

0 ⩽E(t) ⩽E0 remaining energy limits:

0 ⩽Prider(t) ⩽Pmax(t) rider’s power limit:

where the decision variable Prider(t) denotes the output power of the rider’s decision at time t, and t0, tf denote the moments at the beginning and end of the track, respectively. x0, xf denote the positions at the beginning and end of the track, respectively.

4.4.2 Numerically Solving the Optimizing Problem Using Dynamic Programming

Dynamic programming is both a mathematical optimization method and a computer pro- gramming method. The main concept of dynamic programming is straight-forward. We divide a problem into smaller nested sub-problems, and then combine the solutions to reach an overall solution. This concept is known as the principle of optimality, and a more formal exposition is provided in this section. The term “dynamic programming” was first used in the 1940’s by Richard Bellman to describe problems where one needs to find the best decisions one after another. In the 1950’s, he refined it to describe nesting small decision problems into larger ones. The mathematical statement of principle of optimality is remembered in his name as the Bellman Equation.[6]

To facilitate the discussion, we define some notations as follows:

We call quadruple si = (xi, vi, Pmax,i, Ei) a state. let the four state variables xi,vi,Pmax,i,Ei, respectively, indicate the distance of the current position from the starting point, the speed of the current state, the maximum output power of the current state, and the remaining energy of the current state.

Wedefine that statesj = (xj, vj, Pmax,j, Ej)can betransferred tostatesi = (xi, vi, Pmax,i, Ei) (xj ≤xi) at cost ∆t if and only if there exist Prider,0 ≤Prider ≤Pmax,j,that satisfies

∆t = xi−xj  vj   vi = vj + a∆t  (10) Prider Pmax,i = −kfPmax,j Pmax0∆t + kr(Pmax0 −Pmax,j)∆t    Ei = Ej + ki(Pmax0 −Pmax,j)∆t −Prider∆t We call Prider the decision from sj to si.

The cost of multiple transfers is the sum of the cost of each transfer. let T(xi, vi, Pmax,i, Ei) denotes the minimum cost used to optimally transfer from the starting state (0, 0, Pmax0, E0) to the current state (xi, vi, Pmax,i, Ei).

According to the Bellman’s principle of optimality, i.e. an optimal policy (set of decisions) has the property that whatever the initial state and decisions are, the remaining decisions must constitute and optimal policy with regard to the state resulting from the first decision.

Bellman’s principle of optimality holds for our optimizing problem.Therefore,we have Prider{T(xj, vj, Pmax,j, Ej) + ∆t} T(xi, vi, Pmax,i, Ei) = max (11)

where Prider, ∆t are the decision and cost of transfer from state (xj, vj, Pmax,j, Ej) to (xi, vi, Pmax,i, Ei) respectively.

4.4.3 Complexity Analysis of Dynamic Programming Solution

Since modern electronic computers are very limited in their ability to process continuous data directly, so we quantify our continuous data into discrete levels.

let nx, nv, np, ne, nr donate the quantification levels (number of distinct discrete levels) of x, v, Pmax, E, Prider,respectively.

Therefore, the total number of states is as nxnvnpne , and for each state, the number of computations required can be expressed as O(nr). Thus, the time complexity of our dynamic programming algorithm is O(nxnvnpnenr), the space complexity is O(nxnvnpne).

When nx = 400, nv = 30, np = 10, ne = 10, nr = 450,the calculation takes about 10 minutes on a MacBook Pro(2020,Apple M1).

5 Results

5.1 The Power Profiles of Time Trail Specialist and Sprinter of Different

Genders

The power profiles are shown in Fig.5.

5.2 Power Distribution for Various Courses

5.2.1 2021 Olympic Time Trial course in Tokyo, Japan

for different kinds of cyclists with different stages of the track.

From the graph, we can see that Sprinter cyclists are suitable to increase their power output at the beginning of the race and in the uphill phase to get a lead in the progress. However, compared to Time Trail Specialists, Sprinters are usually not good at long distance riding, so they usually lag behind Time Trail Specialists on long flat sections.

Therefore, we came up with the following planning strategy: for a relatively undulating section of road, the optimal power planning plan for the Sprinter is roughly to power up at the beginning and on the large uphill section, and to ride at a lower power on the large, relatively gentle section of road to preserve energy. For the TTS, the opposite is true: don’t accelerate at full power at the beginning of the race, and the same for the uphill, but allocate more power on the large gentle sections. Gender makes no significant difference to this strategy.

5.2.2 2021 UCI World Championship Time Trial Course and The Course We Designed

Course The Optimal Power Distribution of 2021 UCI World Championship Time Trial Course and the Course We Designed are shown in Fig.13 and Fig.14, respectively.

The data from these two courses also supports our view on Time Trail Specialists and Sprinter.

5.3 Result Analysis

Trail

Specialist (male) on the 2021 Olympic Time Trail. We can see that the runner has more power and less speed when the course is uphill, and the opposite is true for the downhill. This further confirms the validity of our model.

5.4 Potential Impact of Weather Conditions

Even on the same track, different weather conditions can cause different race results. In our model, we mainly consider the effect of wind and ground humidity on the courses.

5.4.1 Wind

The factors affecting wind on cycling races can be divided into wind direction and wind force. In the case of larger tailwind, athletes need to resist less wind resistance, and in the case of larger headwind, athletes need to resist more wind resistance. For different winds, we make different modifications to the model as follows:

v = |vrider ± vwind| · cosθ (12) Where vrider is the cyclist’s rate, vwind is the wind speed, and θ is the angle between the rider’s riding direction and the wind direction.

5.4.2 Ground Humidity

If the ground humidity is high, the cyclist will reduce his speed to prevent slipping or falling; while if the ground is dry, the cyclist can release his speed as much as he wants.In our model: µ is smaller when the ground humidity is higher, and µ is larger when the ground humidity is lower.

The influence of environmental factors on rider performance can be seen as follows:

In Figure 16, The green line shows the "distance-power" curve of a TTS(male) under ideal conditions(Time:24’25"); The blue line shows the "distance-power" curve of the same TTS(male) in a rainy day(Time:30’10"); The yellow line shows the "distance-power" curve of the same TTS(male) during the race in upwind conditions(Time:25’11"). We can see from the simulation results that higher ground humidity and stronger headwinds will lengthen the time for riders to finish the race.

5.5 Sensitivity of the Results to Rider Deviations from the Target Power

Distribution

Due to the uncontrollability of environmental factors, riders’ own physical conditions and different views and divisions of the track between riders and coaches, riders will not strictly follow the planned optimal plan to race, we regard the actual power output of riders as the sum of the planned optimal power output plan and a random error obeying normal distribution.

Prider(t) = Prider_real(t) = Prider_plan(t) + ε(t) (13) where ε(t) is a random error that follows a normal distribution

The improved model was brought into simulation and the following results were obtained:

The Optimal time result is 24’25", the after disturbance is 26’44".

5.6 Result of Team Time Trial

We know that cyclists need to resist air resistance during high speed. The faster the speed, the greater the air resistance is. In team cycling, teams often use the "mountain train" tactic:

the team members line up to minimize overall air resistance. The rider at the front of the line needs the most wind resistance, while the rider further back in the line needs to resist less wind resistance. By finding information and data processing [13], we got the information of wind resistance of each rider in the 6-member team, which is listed as follows:(the percentage indicates the percentage of wind resistance each rider needs to resist compared with the rider at the front of the queue)

The dynamic strategy used by the team in the "Mountain Train" tactic is that each time the rider at the front of the queue helps the team to resist the maximum wind resistance for a period of time, then switches to the last position in the queue to enjoy the least wind resistance. The rest of the riders will move forward to replace one another in turn. And so on and so forth. The average power output of each driver in the team will be different (i.e., the average speed of the team will be different) for different lengths of replacement intervals (the time a driver is at the front of the queue in each position sequence cycle). After several simulations, we found the replacement interval time that makes the average power output maximum (shortest finish time), and the simulation results are as follows:

InFigure 19, The red line shows the "distance-power" curve of a Team Time Trial(Time:22’36"); The green line shows the "distance-power" curve of an Individual Time Trial(Time:24’25"). We can see from the simulation results that thanks to the "mountain-train" strategy used in the team competition, the average wind resistance for each rider is reduced, allowing the team to move at a faster pace.

6 Strength and Weakness

6.1 Strength

• We establish the power output model of the rider according to the human muscle physiol- ogy and human energy model, and by considering the different input parameters of riders, we can output power profiles with their own attribute fields.

• We model the bike course with real data and reasonable design, and set data structure included height difference, radius of curvature, etc. and some global environmental variables such as ground friction coefficient, wind resistance coefficient, etc., which well rebuild the real bike courses and exhibits some important features such as road curves and wind or weather conditions, etc.

• We use the well-known Newtonian mechanics model in our model analysis of bicycle and road riding, which is simple and produces scientifically reliable mechanical analysis.

• After rigorously defining the optimization problem formally, we use a dynamic program- ming algorithm to solve the optimization problem. Under our model definition, dynamic programming is able to guarantee that the optimal solution can be solved in a relatively modest amount of time.

6.2 Weakness

• Real-life data is continuous, but computer simulations are difficult to handle continuous data, so we disaggregate the data, which makes continuous data lose some information.

• There are more factors affecting the rider such as the rider’s mental state, etc, but in mathematical modeling we can only consider a limited number of major factors to model which may also lose some details of the impact

• In the team time trials competition, we simplify the multiplayer team into prime points, and also risk missing some actions within the team that can optimize the performance.
