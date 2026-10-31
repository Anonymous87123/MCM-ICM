For ofﬁce use only For ofﬁce use only

T1 F1 T2 F2 T3 F3 Problem Chosen

T4 F4

MCM/ICM

Summary Sheet

Summary

We construct a Mixed Cooperation model to simulate each section of the trafﬁc network independently based on Cellular Automata. We assume that self-driving vehicles need no safety interval compared with non-self-driving ones because of good synchronization with the former vehicle. And also, we assume that the junctions have little inﬂuence on simulation because the trafﬁc performance is relatively continuous. Our Mixed Cooperation model contains three main part.

First, in our basic model, we presume that trafﬁc counts satisﬁes uniform distribution in a day. We know the trafﬁc count and lanes of each section of the trafﬁc network , so we can get the trafﬁc density of each road section in a period and continue to use different self-driving ratio to simulate the trafﬁc ﬂow.

Next, in our time-based model, we take time model into considera- tion. We presume that trafﬁc density function over time is identical to dual-Gaussian distribution in a day, which means that there are two period of trafﬁc peaks. So we can get the trafﬁc density of each road section in each period of one day and continue to simulate similarly as the basic model.

Further, based on our time-based model, we construct a dedication- model, considering dedicated lanes for self-driving vehicles and con- tinue to simulate similarly as the time-based model.

In conclusion, we use the average velocity of vehicles in each road section in each period to evaluate the performance and capacity. Our models give the result of effect of self-driving on trafﬁc performance under different trafﬁc density. Furthermore, our models point out the condition of needing dedicated lanes for self-driving vehicles.

Governor Jay Inslee

Ofﬁce of the Governor

PO Box 40002

Olympia, WA 98504-0002

Dear Governor Inslee:

I write to you on behalf of the MCM team 55583. We are extremely concerned about the trafﬁc condition in the Great Seattle area. Investigation shows that the trafﬁc ﬂow usually exceeds the trafﬁc capacity in many regions in the Great Seattle, especially during peak hours. We hope to help you improve the trafﬁc conditions.

The current trafﬁc condition could lead to many severe problems. The ﬁrst problem is unacceptable delay during peak hours.During the morning commute and at the end of the day these delays become extreme long. Also it could lead to congested roads, and potentially increase the probability of occurrence of trafﬁc accidents. Congested roads could also cause problems for emergency vehicles, making them unable to respond in an appropriate amount of time.

After an in-depth study of the trafﬁc conditions in the Great Seattle area, we have come up with some ideas that can help address this issue. We propose self- driving, cooperating cars as a solution to increase the trafﬁc capacity without building extra lanes.

Compared to human-drived cars, self-driving cars have many advantages. The biggest advantage is that it take much less time to react in terms of emer- gency. This actually allows self-driving cars to keep a closer distance with the car in front of it, thus it takes up much less trafﬁc resource. In addition to this, self driving cars can tune their acceleration and deceleration proﬁles to consume less fuel.

Those advantages mentioned above make self-driving cars an excellent choice for addressing heavy trafﬁc load. We build a model to simulate the trafﬁc ﬂow of the most busy roads in the Great Seattle area and evaluate the effectiveness of self-driving cars addressing the problem of heavy trafﬁc load. The simula- tion shows promising results. The introduction of self-driving cars makes all cars among all roads in the Great Seattle area go faster, it works especially well among busy roads during trafﬁc peak hours. When no self-driving cars are in- troduced, the trafﬁc goes very slow during peak hours, but after introducing approximately 50% self-driving cars the trafﬁc ﬂow goes 1.5 2 times faster.

In addition to making trafﬁc ﬂow faster, self-driving cars also make trafﬁc ﬂow more stable. From our simulation, we observed that introduction of self- driving cars help to reduce the variance of trafﬁc delay. This is important because it helps to estimate times, and helps to reduce "just in case" time.

For the above reasons, we propose self-driving cars as a solution to heavy trafﬁc load in the Great Seattle. We appreciate all that you do for this city, and we look forward to seeing positive changes. We hope you can accept out advices.

Sincerely yours

MCM 2017 Team 55583

6 Conclusion

18

Appendices

20

Appendix A Cellular automata program:Moving behavior

20

Appendix B

Cellular automata program:Create new vehicles 23

Appendix C Cellular automata program:Create new vehicles considering

dedicated lanes 23

1 Introduction

1.1 Problem Statement

Trafﬁc capacity is limited in many regions of the United States due to the num- ber of lanes of roads. For example, in the Greater Seattle area drivers experi- ence long delays during peak trafﬁc hours because the volume of trafﬁc exceeds the designed capacity of the road networks. This is particularly pronounced on Interstates 5, 90, and 405, as well as State Route 520, the roads of particular in- terest for this problem. Self-driving, cooperating cars have been proposed as a solution to increase capacity of highways without increasing number of lanes or roads. The behavior of these cars interacting with the existing trafﬁc ﬂow and each other is not well understood at this point. Based on the road listed above in Thurston, Pierce, King, and Snohomish counties, we considered how the ef- fects would change as the percentage of self-driving cars increases from 10% to 50% to 90%, and the equilibria as well as the tipping point where performance changes markedly. Also we simulated that under what conditions, if any, should lanes be dedicated to these cars. Based on our model, we listed several practical suggestions to the local government.

1.2 Related Work

Trafﬁc ﬂow has been researched for a long time by many people.We can get some basic models about relationship among trafﬁc density, speed and through- put[5].When trafﬁc density is medium, there is a linear relationship:

traffic density Speed = Maximum Speed ∗(1 − Maximum density) (1)

When trafﬁc density is nearly full, there is a logarithmic relationship:

Speed = Maximum Speed ∗ln (Maximum density ) (2) traffic density

When trafﬁc density is very low, there is a exponential relationship:

Speed = Maximum Speed ∗(1 −exp (Maximum density )) (3) traffic density

Self-driving has entered our vision and may be popular in the future.The accu- racy and safety have been improved a lot thanks to the development of artiﬁ- cial intelligence.One of the most important point is the sensors on the vehicle[1], which can detect the motion state of the surrounding vehicles, including velocity, distance and acceleration.So, in our models, we assume that self-driving vehicles can keep the same motion state with the former one, without safe interval.

2 Assumptions and Notations

2.1 Assumptions

We make the following basic assumptions in order to simplify the problem. Each of our assumptions is justiﬁed and is consistent with the basic fact.

• Time consumed on the crossroads and toll on the roads is not in consid- eration. We suppose that the cars are in the same speed and ignored the wasted time due to the road conditions.

• The trafﬁc counts on the speciﬁc roads will not change after adjustment.

We presume that at certain day or certain hours the car that need to use certain road will not change because of our adjustment.

• No lane changing situation is considered. This assumption will be ex- plained in 3.1 when we illustrate the self-driving, cooperating car model.

• The capacities and sizes of different kinds of cars will not be differenti- ated. To simplify our model, we assume that all the car in our model share the same regular length 4m and regular width for one car a lane.

2.2 Notations

The notation table contains all the notations we use in this paper.

Symbol Deﬁnition Notes

vins instantaneous speed of a car tresponse equals 1s the response time of a human driver lu equals 4m unit length of a block in Cellular Automaton model nl lane counts of a certain road section d the distance between two adjacent cars LR the whole length of a certain road section Vmax equals7units/s the maximum speed that a car can reach TC TC during a day trafﬁc count during a certain time slot TC24 is a constant v car velocity tavg the average car passing time σ2 car velocity variance during different period in a day t σ2 car velocity variance among different road sections s Pself the possibility of a self-driving car to show up PNself the possibility of a non-self-driving car to show up

3 Model Construction

3.1 The self-driving, cooperating car model

From article [1] and [2], we can know that the self-driving, cooperating cars have four potential beneﬁts:

• Fewer accidents. Driverless car can dramatically reduce the accident toll due to drivers’ error.

• More productive commutes. Driverless cars would enable the unproduc- tive hours and minutes to be converted into productive work and/or leisure time. In other word, self-driving car can help reduce the useless waste on time.

• Environmental friendliness. Autonomous cars and trucks can tune their acceleration and deceleration proﬁles to reduce wasted fuel.

• Fewer trafﬁc jams. Driverless cars would be better adapted to higher vol- umes of trafﬁc, as they would be able to travel at higher speeds while keep- ing shorter distances between vehicles.

In our model, we paid special attention to the forth beneﬁt and considered a lot about the self-driving cars’ effects on trafﬁc jams.

A self-driving, cooperating car is guided by internal computers and exter- nal sensors, and it can communicate and exchange datas with other self-driving, cooperating cars as it decides what to do. In our model, we think self-driving, cooperating cars can better deal with emergent situation and almost don’t need the reaction time that human take in face of emergencies.

From article [3] we can see on the one hand, when cars pull over or over- take, they may have trouble recognizing lane markers especially in low light, bad weather, on curves, and at forks and merging lanes. On the other hand, lane change prediction of self-driving cars may not be accurate enough, and the time it will take for a complete turnover of all cars to self-driving cars makes planning for it more than a little premature. So we reasonably assume that in our model, no lane changing situation is considered.

Here is the structural difference between self-driving, cooperating cars and non-self-driving cars.

(a) non-self-driving car (b) self-driving car

emergency situations

Deﬁnition 1. Safe interval is the shortest distance from the former car to guarantee the safety, considering the current speed and response time of a human driver. And we can compute it as follows:

safe interval = vins × tresponse (4)

When two cars’ distance is less than the safe interval, drivers will slow down and keep distance with the former car, which is just as the Figure 1(a) showed above. But for self-driving cooperating cars, they are controlled by artiﬁcial intel- ligence system and they can always react in time when the speed of the former car changes. So these cars donnot need to keep safe interval and they can just follow the former car at best, which is shown in Figure 1(b) above.

3.2 The mixed, dynamic road model

In order to better reproduce the dynamic road trafﬁc ﬂow model, we choose Cellular Automaton to simulate the Real-Time Trafﬁc of every road section. The following Figure2 shows the improved Cellular Automaton model used in our paper.

We update the model data every second. Every line in the CA represents a lane on the road. Every volume block represent a unit length to represent the length of a car and the distance between adjacent cars. As shown in Figure 2, the yellow-colored blocks represents the self-driving cars and the blue-colored blocks represent the non-self-driving cars. The following list contains all the pa- rameters and procedures in our CA based road model.

• Unit length lu: For convenience, the unit length lu = 4m, equals the length of a regular car.

• Lanes count nl: Because the two directions on each road have no distinct difference, and will not disrupt each other as well. So we regard them the same in our model, and the lanes number is the addition of lane counts of these two directions.

nl = nleft + nright (5)

• Adjacent cars distance d: we deﬁne the number of unit length between two cars the distance from the rear end of the ﬁrst car to the head of next car, namely.

d = posformer −poslatter −1 (6)

• Road section length LR: For every section of the road, the length of this section is the number of unit length.

LR = Lreal (7) lu

• Maximum speed Vmax: we deﬁne the speed by how many unit lengths the car has gone per second.Speed limit is 60 mile/h, which is about 27 m/s, namely, 7 unit length per second.Vmax = 7 units/s

• Human response time tresponse: we deﬁne human response time as the time which a person need to start to slow down the car after he or she has found emergency. Commonly, response time is from 0.3 seconds to 1.5 sec- onds.Here we deﬁne tresponse = 1

• Instantaneous velocity of cars vins: The instantaneous speed of this corre- sponding car decides how many blocks the car will move forward at next second. And the unit of vins is blocks per second

• Trafﬁc Counts TC: During some time, the amount of the cars reaching the end of road section is the TC of this road section during that long time.

3.3 Performance evaluation criteria

3.3.1 Car Velocity v

From the model above, the instantaneous speed is easily accessible, but the car velocity we use to evaluate the road condition is the average velocity of cars that passed the road during certain time slot. The average car velocity can well reﬂect the road performance under different conditions. The bigger the velocity is, the less crowded the road is and thus the better the road capacity is. From our model, there is a trick to get the average car velocity:

First, we count all the cars every second on the roads and sum them up.

Nsum = Σtn(per second) (8)

Then, the average car passing time is accessible.

tavg = Nsum (9) TC

v = Lreal (10) tavg

1 1

3.3.2 Daily Equilibria

t , σ2 σ2s

We evaluated the trafﬁc network equilibria from both time aspect and space as- pect.

On the one hand, for a certain road section, during a single day, including peak hours and average hours, if the car velocity keeps stable and changes little, the time daily equilibria of the trafﬁc network is obviously better.

Deﬁnition 2. Time daily equilibria.We deﬁne it as 1 ,where σ2 t is the car velocity σ2 t variance during different period in a day for a certain road section.

t = 1 σ2 mΣm(vti −¯v)2 (11)

On the other hand, at speciﬁc time slot, if the car velocities of different road sections do not distinct too much or nearly same, the space daily equilibria of the trafﬁc network is much better. Deﬁnition 3. Space daily equilibria.We deﬁne it as 1 ,where σ2 s as the car velocity σ2 s variance at same time among different road sections. In this problem, the road sections of the particularly concerned four roads is 224.

1 σ2 224Σ(vli −¯v)2 s = (12)

4 Model Extension and Simulation Analysis

We decomposed our simulation into three steps and corresponded them to three problems. First of all, we ignored peak hours in a day and no dedicated lanes. Secondly, we proposed the trafﬁc counts distribution during a day considering the peak hours and average hours, and applied our model into this situation. Lastly, we considered dedicated lanes’ effect and answered the question "Under what condition, if any, should lanes be dedicated to these cars".

4.1 Problem1: The effects of auto-driving cars in trafﬁc network

When peak hours are not taken into consideration, we assume that the cars come randomly at any second during a day with evenly possibilities. So if the propor- tion of the self-driving car is p, the possiblity of a self-driving car come at the start point of a road section on each lanePself is:

Pself = TC24h/24/3600 × p/lanes (13)

and for the non-self-driving car, Pnon−self is:

PNself = TC24h/24/3600 × (1 −p)/lanes (14)

The initial velocity of each car is randomly assigned among 0 to 60 mile/h, that is, the maximum speed of a car is 7units/s. Then we use the procedure showed in Figure 3 to decide how the velocity and position will change in the next second.

First, we check if there is conﬂict between adjacent cars, if there is conﬂict, the drivers or the artiﬁcial intelligence system will brake until the velocity is the same as the car in front, so in this situation, the new velocity is the same as the car in front,and the position will be closely following the former one. Meanwhile, if there is no conﬂict, check if the distance is shorter than safe interval, if not, the car controller will accelerate until the car velocity reached the maximum velocity. If the distance is within the safe interval, for non-self-driving car, the driver will decelerate considering safety, but self-driving car will still accelerating because it has the ability to adjust the speed of itself quickly according to the speed of the former car and need no response time.In other words, self-driving cars can be perfectly synchronized with the former car automatically, and need no safety interval.

Then, we simulated the whole 224 road sections for one hour long time, and repeated every simulation for 100 times to eliminate accidental error.

the car in next second

4.1.1 Car Velocity/Performance v

We simulates the trafﬁc performance when the percentage of self-driving, coop- erating cars change every 5%, and the 10%, 50%, 90% is emphasized in the Figure 4.

From the result, we can safely come to the conclusion that the car velocity steadily increase as the self-driving car percentage raises.

Space Daily Equilibria 1/σ2 4.1.2 s

The trafﬁc counts distribution of time is considered, so σs t is not compared here.

Also, Figure5 shows the car velocity variance decreases steadily, which means the space daily equilibria increase as the self-driving, cooperating cars percent- age raises.

Both this two results can prove that the self-driving, cooperating car can do release the trafﬁc pressure, and help to improve the road capacity.

s versus self-driving ratio

4.1.3 Sensitivity Analysis

• Sensitivity of performance to self-driving ratio.With further observation of Figure 4, we can know that the change of performance is little and the difference between maximum and minimum is about 1 m/s, which is just 4% of the performance.So, performance is not sensitive to the self-driving ratio.

• Sensitivity of variance to self-driving ratio.With further observation of Figure 5, we can get that the change of variance is relatively big and the difference between maximum and minimum is about 4m2/s−2, which is about 66% of the maximum, so the variance is relatively sensitive to the self-driving ratio.

4.2 Problem2: The different effects on peak/average hours

4.2.1 Trafﬁc Density Distribution of Time

Based on the article[4], we re-deﬁned trafﬁc density here to help us ﬁgure out and make the good use of the rules of trafﬁc count distribution of time.

Deﬁnition 4. Trafﬁc Density is the ratio of the number of vehicles arriving per hour to the daily trafﬁc count.

There are two peaks every day, so we choose dual-Gaussian distribution to approximate the trafﬁc density function. Our test and veriﬁcation show that this function can well reﬂect the truly trafﬁc density function versus time.

λ 2π(e−(x−t1)2 + e−(x−t2)2  2σ2 ) √ f(x) = 2σ2   2σ  (15) Z 24  f(x) dx = 1   0

After calculation and comparasion, we got the parameters λ, σ, t1 and t2 in the function, and the function graph is shown in Figure6.

4.2.2 Simulation

Considering peak hours’ heavy trafﬁc loads, we adjust our model’s trafﬁc count parameter according to the density function given above every hour. We simu- lated 24 hours a day for the whole 224 road sections, and repeated for 20 times to eliminate accidental error. Different from the barely three criteria, we adjust our data visualization strategies to stress the changing point.

• The real-time car velocity of 224 road sections at peak time 17:00, during our density model, the heaviest density come at 17:00, so we chose this time point to compare different trafﬁc performance when the self-driving ratio is 0%, 10%, 50% and 90%.

We abstract the four particularly pronounced roads from the map, and cor- responding every road section to a block in the graph. The road direction as well as the road length is adapted based on the fact data on the map.

In Figure 7, we use different colors to reﬂect the real-time car velocity. The lower the car velocity is, the more crowded the road is and the worse the trafﬁc performance is, meanwhile, the color is more close to "red".

As we can see from the graphs in Figure 7, self-driving, cooperating cars can distinctively reduce the trafﬁc pressure at peak hours and get a bet- ter equilibrium of space because the color becomes more uniﬁed.When the percentage of the self-driving cars reaches 50%, the trafﬁc ﬂow can proceed almost without hindrance.

• Tipping Point Observation: In our basic model in Prob.1, the ignorance of peak time will result in the car sparse, so the changing tendency is not so representative. In this part, we compared car velocity in variable density background versus self-driving ratio. Speciﬁcally speaking, we choose the presentative busy hour 17:00, the average of the road conditions during peak hours and daily average car velocity regardless of peak hours, and show its corresponding car velocity changing tendency versus self-driving ratio.

(a) no self-driving car (b) 10% self-driving car

(c) 50% self-driving car (d) 90%self-driving car

face of emergency situations

From Figure 8, especially the curve trends of the two lines of the busy roads, we can see the change is the most obvious when the self-driving car per- centage is around 45%. Therefore, only the tipping point of busy road sec- tions at peak time can be observed, and is about 45%.

sity conditions.

• In this part, we also compare Time daily equilibria and Space daily equilib- ria to illustrate what effect the self-driving, cooperating car will take to the road equilibria.

For time daily equilibria, we displayed its changing tendency with the in- crease of the self-driving car percentage. The corresponding curve is shown in Figure 9.

For space daily equilibria, we displayed its changing tendency versus time during a day when the self-driving car percentage is 10%, 50% and 90%.

The 0% line works as a reference here. The corresponding curve is shown in Figure10.

From Figure9, we can clearly observe that the σ2 t decreases as the percent- age increases, especially when the trafﬁc density is heavy, that is, espe- cially in peak hours. Also, the biggest drop come up around the tipping point 45%. From Figure10, the σ2 s decreases as the percentage increases too.

When the percentage of self-driving cars reaches 50%, the peak hours effect become less signiﬁcant.

4.2.3 Sensitivity Analysis

From the results of this part, the self-driving car applied can dramatically improve the trafﬁc capacity and performance during peak hours, and for the busy roads, the tipping point come up around 45%, the percentage of the self-driving cooperating cars.Spatially, road performance is more sen- sitive to self-driving ratio during peak hours.Chronologically, road perfor- driving ratios.

mance is more sensitive to self-driving ratio at busy road sections, like In- terstate 5,milepost 163.36.

4.3 Problem3: Dedicated lane assessment

To assess the performance of dedicated lane, we added a dedicated lane to both directions of each road section. In our model, if there is a dedicated lane for self-driving, cooperating cars, these cars cannot drive on other lanes and the dedicated lane is not open for non-self-driving cars.

We simulate the performance of the road sections when two lanes are ded- icated to self-driving cars, and compare it with the performance without dedi- cated lanes.

The average car velocity performance is shown in Figure 11.

cated to self-driving cars.

Also, the space daily equilibria performance is shown in Figure 12. To bet- ter represent the effects of self-driving cars, we chose the busy road to simulate instead of average road condition.

From the two ﬁgures, we can see, when the self-driving cooperating cars per- centage is less than 68%, the roads without dedicated lines have relatively bet- ter capacity and performance. However, when the percentage reaches 68%, the roads with two dedicated liens have relatively better capacity and performance.

Also, we can ﬁnd that when the percentage reaches 95% or more, the perfor- lanes dedicated to self-driving cars.

mance of roads with dedicated lanes declined at the same time. We think, it is because we limited the self-driving car on the dedicated lanes, and it may re- sult in the over-crowded dedicated lanes for self-driving cars. In this situation, add more lanes dedicated to self-driving, cooperating cars may get performance improve. But we did not simulate it, because of the simulation time cost.

4.3.1 Sensitivity analysis

For dedicated lanes,here we only allocate one on each road section in each direc- tion. But we ﬁnd something within our expectation.The performance is sensitive to dedicated lane number when self-driving ratio is lower than 68% because, the dedicated lanes have robbed the capacity of other lanes to serve self-driving cars, so the common lanes become more busy.Although the performance is improved by allocating a dedicated lane to each road section in each direction when self- driving ratio is higher than 68%, the performance changes little.The reason is that we only allocate one dedicated lane for self-driving vehicles and the dedicated lane becomes busy when self-driving ratio is high.

5 Strengths and Weaknesses

5.1 Strengths

Our model take time, space, self-driving ratio, trafﬁc density and dedicated lanes into consideration. Based on the analysis above, we list strengths of our model as follows:

• Extensibility. Our models deal with each road section independently, so we can extend them easily. For instance, given the trafﬁc density function of time over the whole year, we can get the effect of self-driving-ratio on the trafﬁc during a whole year. Furthermore, we can modify the moving behavior in 4.1 to construct a more complicated but more practical model.

Such as adding lane changing situation into consideration as the technol- ogy improved.

• Exactness. Our models deal with time using second as a unit, so, in fact, we monitor how vehicles move in a second, which improves the accuracy a lot. In addition, in our time-based model, thetrafﬁc density function of time during a day has a second-level accuracy better than minute-level or hour-level.

• Stability. Our models have some undetermined factors, like the initial speed of a vehicle. But we have veriﬁed that the results of many tests under the same conditions have little ﬂuctuation, which means a great stability.

5.2 Weaknesses

• Junctions are ignored. Actually, what happens in the junction between two road sections is very complex. We have observed that the two adjacent road sections have different trafﬁc counts, which means loss or gain of trafﬁc counts. If we could consider the initial condition and ﬁnal condition based on the junction parts, we are likely to get a more accurate model of the whole trafﬁc network.

• Switching lanes is ignored. Actually, for non-self-driving vehicles, switch- ing lanes is possible. If we try considering switching lanes, we also need to distinguish the left lanes and right lanes and vehicles can not cross the line between this two kinds of lanes.

5.3 Future work

First, take junctions into consideration for higher exactness of the whole trafﬁc network. In our model, we can extend it by recording the ﬁnal condition of current road section and using it as the initial condition of the adjacent road section.

Second, take switching lanes into consideration. In our model, we can mod- ify the moving behavior of non-self-driving and self-driving vehicles, and add switching behavior into it.

Finally, in fact, how to determine a path over the whole road network is also different for non-self-driving and self-driving. Self-driving vehicles probably know the performance of each road section, and could select a path which costs least, while non-self-driving vehicles probably choose a path which is shortest physically but may cost more. If we add the way of searching a path into our models, they could be more practical and strong.

Since the time is limited, we are sorry that we implement little of the future work. But the future work is really worth considering. We suppose that the model can become more practical after the future work has been done.

6 Conclusion

From the simulation analysis of the model we proposed, self-driving, cooper- ating cars can do be regarded as a solution to increase capacity of highways without increasing number of lanes or roads. In particular, when the percentage of self-driving cars increases, the performance of the road capacity and perfor- mance increase as well. Especially for peak hours and busy road sections. From our simulation, we ﬁnd, for busy road or on peak hours, the capacity of the roads improve dramatically when the percentage of the self-driving, cooperating car is around 45%. And, we ﬁnd, when the self-driving-car ratio reached 68% or more, dedicating two lanes to self-driving cars can help to further improve the road capacity. But when the ratio reaches 95% or more, two dedicated lanes is not enough, the crowded car on the dedicated lanes will lower the performance.

Appendices

Appendix A

Cellular automata program:Moving be- havior

Here is part of MATLAB simulation programs we used in our model.

Moving behavior

function [plaza,v,vmax,traffic_count]=move_forward(plaza,v,vmax,plazalength,cc);

[L,W]=size(plaza);% length and lane numbers gap=zeros(L,W);

count=cc;

t_response=1;%response time 1s v_pre=0;

for lanes=2:W-1;

temp=find(plaza(1:L,lanes)>=1);

nn=length(temp);% The number of the cars in the lane for k=1:nn;

i=temp(k);

if(k==nn) gap(i,lanes)=999;

continue;

end gap(i,lanes)=temp(k+1)-temp(k)-1;

end end

for lanes=2:W-1;

temp=find(plaza(1:L,lanes)>0);

nn=length(temp);

temp=flipud(temp);%from end if(nn>0) i=temp(1);

pos=i+v(i,lanes);

temp(1)=pos;

v_pre=v(i,lanes);

if(plaza(i,lanes)==1)%common car need to consider safety if(pos>plazalength) count=count+1;

plaza(i,lanes)=0;

v(i,lanes)=0;

vmax(i,lanes)=0;

else plaza(pos,lanes)=plaza(i,lanes);

v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes));

vmax(pos,lanes)=vmax(i,lanes);

plaza(i,lanes)=0;

v(i,lanes)=0;

vmax(i,lanes);

end end if(plaza(i,lanes)==2)%Self-driving car speed up if(pos>plazalength) count=count+1; plaza(i,lanes)=0; v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes)); vmax(pos,lanes)=vmax(i,lanes); plaza(i,lanes)=0; v(i,lanes)=0; vmax(i,lanes)=0; end end end

for k=2:nn;%from end i=temp(k); j=temp(k-1); if(v(i,lanes)<=j-i-1)%no conflict pos=i+v(i,lanes); temp(k)=pos; safety_dis=v(i,lanes)*t_response; if(plaza(i,lanes)==1)%common car need to consider safety if(safety_dis>gap(i,lanes))%not safe %disp(’not safe’); if(pos>plazalength) count=count+1; plaza(i,lanes)=0; v_pre=max(v(i,lanes)-1,1); v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); v(pos,lanes)=max(v(i,lanes)-1,1); vmax(pos,lanes)=vmax(i,lanes); plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; end else%if safe, accelerate %disp(’safe’); if(pos>plazalength) count=count+1; plaza(i,lanes)=0; v_pre=v(i,lanes);%record the v before moving v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes)); vmax(pos,lanes)=vmax(i,lanes);

plaza(i,lanes)=0; v_pre=v(i,lanes);%record the v before moving v(i,lanes)=0; vmax(i,lanes)=0; end

end end if(plaza(i,lanes)==2)%self-driving car accelerate if(pos>plazalength) %plaza(pos,lanes)=plaza(i,lanes); %v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes)); %vmax(pos,lanes)=vmax(i,lanes) count=count+1; plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes)); vmax(pos,lanes)=vmax(i,lanes); plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; end end else% conflict pos=j-1;%move next to the former car temp(k)=pos; if(pos>plazalength) count=count+1; plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); if(j<=plazalength) v(pos,lanes)=v(j,lanes); else v(pos,lanes)=v(i,lanes); end %v(pos,lanes)=v(i,lanes); vmax(pos,lanes)=vmax(i,lanes); plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; end end end end traffic_count=count;

end

Appendix B

Cellular automata program:Create new vehicles

Here is part of our simulation programs we used in our model.

Generate new vehicles

function [plaza,v,vmax]=new_cars(plaza_1,v_1,vmax_1,probc,probv,max_speed);

[L,W]=size(plaza_1);

plaza=plaza_1;

v=v_1;

vmax=vmax_1;

for lanes=2:W-1;

if(rand<=probc) %generate a car for a lane according to time distribution %disp(rand);

if(rand<probv(1)) %generate a self-driving vehicle in possibility p plaza(1,lanes)=2;

vmax(1,lanes)=max_speed;

v(1,lanes)=round(rand*7)+1;%random initial speed else %generate a non-self-driving vehicle in possibility 1-p plaza(1,lanes)=1;

vmax(1,lanes)=max_speed;

v(1,lanes)=round(rand*7)+1;%random initial speed end end end end

Appendix C

Cellular automata program:Create new vehicles considering dedicated lanes

Here is part of our simulation programs we used in our model.

Generate new vehicles

function [plaza,v,vmax]=new_cars(plaza_1,v_1,vmax_1,probc,probv,max_speed,dedicated_nu [L,W]=size(plaza_1);

plaza=plaza_1;

v=v_1;

vmax=vmax_1;

for lanes=2:W-1;

if(lanes<2+dedicated_num)%dedicated lanes for self-driving if(rand<(probc*(W-2)/dedicated_num*probv(1))) plaza(1,lanes)=2; vmax(1,lanes)=max_speed; v(1,lanes)=round(rand*7)+1; end else %common lanes for non-self-driving vehicles if(rand<(probc*(W-2)/(W-2-dedicated_num)*(1-probv(1)))) plaza(1,lanes)=1; vmax(1,lanes)=max_speed; v(1,lanes)=round(rand*7)+1; end end end end
