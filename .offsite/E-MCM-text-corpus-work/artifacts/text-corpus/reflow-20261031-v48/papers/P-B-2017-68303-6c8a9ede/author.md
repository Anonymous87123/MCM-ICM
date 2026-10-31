For ofﬁce use only For ofﬁce use only

T1 F1

T2 F2

T3 F3 Problem Chosen T4 F4

MCM/ICM

Summary Sheet

Summary

With the rapid increment of the trafﬁc ﬂow, the problem of merging after the toll barriers has risen public concern. In our paper, we aim to construct a model to ﬁnd a better design of the area following the toll barrier.

First, we classify the area following the toll barrier which may already be imple- mented into eight kinds according to the different shapes, sizes, and merging patterns of the area based on the toll plazas in reality.

Second, we use VISSIM to do the simulation of the typical eight models of the area following the toll barrier. Through setting the necessary observation points, we obtain the data of throughput, length of queues and the average time of delay we need in the following evaluation model.

Third, we build a comprehensive evaluation model based on PCA to evaluate the eight typical models and the optimum model we build. Considering the selection of the index, we choose the number of merging points to indicate accident prevention of the area, the length of queues, the throughput and the average time of delay to indicate the trafﬁc capacity of the area, and the height of the trapezoid area to indicate the con- struction cost of the area. After data normalization, we get the best model which is in the shape of isosceles trapezoid with stipulated merging pattern and medium size of the area among the eight existing models.

Fourth, in order to obtain a better solution, we build two models to obtain the opti- mum solution. The ﬁrst one is a differential equation model aimed at acquire the opti- mum height of the trapezoid area and the optimum number of tollbooths. The second one is a linear programming model which can calculate the optimum merging pattern while maximizing the throughput of the area.

Last but not least, we analyze the performance of our model under various condi- tions, and modify our model to accommodate to those conditions. Also, we use Lingo to construct sensitivity analysis of the linear programming model.

To sum up, our model is a feasible and reasonable model which can accommodate to various situations.

1 Introduction

1.1 Background

The major problems facing motorists on today’s highways are congestion, accidents, and costs-too many automobiles traveling to the same place at the same time; too many automobiles, trucks, buses, bicycles, and pedestrians attempting to use the same space; too many motorists losing time unnecessarily; too many accidents occurring; and too many decisions being made on highway improvements without adequate analytical tools[1].

As an important part of the highway, the toll plaza is to blame for most of the con- gestions and accidents happen around it. Since there are usually more tollbooths than there are incoming lanes of trafﬁc, vehicles must "fan in" from larger number of tollbooth egress lanes to the smaller number of regular travel lanes. In other words, vehicles need to merge after toll.

Trafﬁc congestion normally happens when merging points are met[2], which may re- sult in long trafﬁc queues on the road. When designing merging area of the toll plaza, shape, size and merging pattern of the area should be taken into consideration. More- over, the design should reduce the risk of accident, the cost of road construction and increase the throughput as much as possible.

1.2 Restatement of the Problem

We are required not only to analyze the performance of the area following the toll bar- rier with different shapes, sizes, and merging patterns that may already be implemented on the aspect of accident prevention, throughput, and cost, but also to determine if there are better solutions than any in common use and evaluate the performance of them un- der different circumstances.

The problem can be analyzed into four parts:

• Analyze the existing design of the area following the toll barrier with different shapes, sizes and merging patterns.

• Build a simulation model to simulate the trafﬁc condition of different designs of the area following the toll barrier.

• Build an evaluation model to rate the performance of different designs of the area following the toll barrier.

• Find a solution which can perform better than any in common use.

1.3 Overview of Our Work

With the increment of trafﬁc ﬂow, the trafﬁc congestion happens more and more fre- quently on the highway, as it gradually becomes the main cause of trafﬁc accidents. The problem of merging after toll has become the common concern of the society.

Firstly, we classify the area following the toll plaza into 8 kinds according to the different shapes, sizes, and merging patterns of the area.

Secondly, we select a series of index to evaluate the existing design of the area fol- lowing the toll plaza. Through the comprehensive evaluation model based on PCA, we evaluate the existing design of the area and our own design.

Thirdly, we build a differential equation model to obtain the optimum number of toll- booths and the height of the trapezoid area and a linear programming model to acquire the optimum merging pattern of the area following the toll barrier.

Finally, we analyze the performance of our model under various conditions and the sensitivity of our model.

1.4 General Assumptions

• All the motorists would obey the trafﬁc rules. We don’t take accidents resulted from drink-driving or speeding into consideration.

• We set the average speed of the vehicles under normal circumstances. Ignore the impact of weather conditions.

• We assume the vehicles on the highway are all cars, for other kinds of vehicles accounts for a relatively small proportion.

• The queue at the merging point would not affect the service of the tollbooths.

• All the tollbooths on the toll plaza operate all day.

2 Classify the Design

Before constructing the simulation model, we need to classify the design of the area following the toll barrier according to the shape, the size, as well as the merging pattern.

According to the satellite map, we ﬁnd that most of the area following the toll bar- rier can be abstracted into two shapes which are right-angled trapezoid and isosceles trapezoid. { right-angled trapezoid, Sp1 shape isosceles trapezoid, Sp2

Then we ﬁnd that the height of the trapezoid determines the size of the area following the toll barrier when the number and width of the tollbooths and travel lanes are deﬁned. According to Japan highway design essentials[3], we choose S/H to indicate the size of the area. To simplify our model, we only take small size S/H = 1/3 and large size S/H = 1/6 into simulation.  H = 1 S   3, Sz1 size H = 1 S   6, Sz2 According to our observation, vehicles can change into any lane when getting out of the toll barrier. On the basis of this observation, we assume that there may be a merging pattern which stipulates the vehicles on the left side can only drive down to the left lanes and the vehicles on the right can only drive down to the right lanes. The stipulation may reduce the risk of collision. { normal merging pattern, Mp1 merging pattern stipulated merging pattern, Mp2

3 Simulation Model

For the lack of data, we choose frequently used software VISSIM to simulate the trafﬁc condition following the toll barrier.

Before the simulation, we need to set a series of parameters. According to the exam- ple mentioned in the problem that the toll highway has L lanes of travel in each direction and a barrier toll contains B tollbooths in each direction, we set the number of lanes and tollbooths L = 3, B = 8 the same as the example.

After consulting Highway Capacity Manual 2000 [4], we set the width of each lane d = 3.5m, the combined width of tollbooth and lane D = 5.5m, and the average speed of vehicles on the highway v = 120km/h. For S = (D ∗B −d ∗L) ∗0.5, S = 16.75. When it comes to a small-sized area S/H = 1/3, H = 50.25. Similarly, when it comes to a large-sized area S/H = 1/6, H = 50.25.

Since we only have to determine the area following the toll barrier, we just need to set the number of vehicles leaving the toll barrier per hour instead of considering the number of vehicles on the travel lanes entering the barrier toll. Through information research[5], we ﬁnd that the temporary retention time at the toll booth is 12 seconds. We want to stimulate the process for 3600 seconds, so the number of vehicles leaving the toll barrier is approximately 3600/12 = 300 vehicles per hour per lane.

To simplify our model, we set the vehicle composition as 100% cars. Considering that there will be many merging points in the area following the barrier toll, we set con- ﬂict areas between each pair of possible crossed paths to simulate the process of vehicle collision avoidance.

Parameter Symbol Value

T simulation time 3600s

L number of travel lanes 3

B number of toll booths 8

d width of travel lanes 3.5m

D combined width of tollbooth and lane 5.5m

In ingress trafﬁc ﬂow of the area 2400 vehicles/h

V average speed of vehicles on the highway 120km/h

Afterwards, we set travel time sections, data collection point, and queue counters of the area to monitor the values of delay, number of passing vehicles and queue length.

Then, we simulate eight kinds of area following the toll barrier according to our above classiﬁcation, to obtain the data we need in the evaluation model.

After simulation, we collect data from the program of the eight models.

height of throughput average length number of kind delay(s) trapezoid (m) (veh/h) of queue(m) merging points

1 50.5 2149 13.8 21.38 24

2 105 2193 20.5 25.49 24

3 50.5 2271 8.2 10.02 7

4 105 2191 14.1 17.65 7

5 50.5 2178 10.4 18.77 24

6 105 2168 17.3 20.04 24

7 50.5 2301 5.8 8.13 7

8 105 2228 11.92 13.26 7

4 Evaluation Model

To illustrate the independence, and the relationship between different variables, we use Principal Component Analysis (PCA)[6]. When some of the variables can explain a great percentage of the results, we can say these variables are strongly correlated and we can use the great one to represent others. After that, we can build a comprehensive evaluation model which based on PCA to evaluate our area models.

4.1 Index variables

We are required to consider the accident prevention, throughput and cost of our mod- els. Since some of the aspects cannot be valued directly, we have to ﬁnd some other parameters to indicate them.

Firstly, as most of the trafﬁc accidents happen at the merging point of lanes, we set the number of merging point of the area as the index to indicate accident prevention level.

Secondly, the cost of land and road construction is proportional to the area size. Since the sum of the bottoms of the trapezoid area are the same, we use the height of the trapezoid area to indicate the construction cost.

Thirdly, there are several indicators of the trafﬁc performance in the area following the toll barrier. We choose the average delay time, the length of queue at merging points and the throughput (number of vehicles per hour passing the point where the end of the plaza joins the eight outgoing trafﬁc lanes) to indicate[7].

4.2 PCA Model

The model is better, if the values of delay time, the length of queue at merging points and the number of merging points are smaller. Since PCA determines the ranking of the models based on the comprehensive score, we take the reciprocal of these values.

In order to facilitate the further analysis, we do the data normalization. Map the index variable data setx = x1, x2, . . . , x5. Set aij as the value of index variable j of model i. ˜aij = aij −µj , i = 1, . . . , 8, j = 1, . . . , 5 (1) sj ˜xj = xj −µj , j = 1, . . . , 5 (2) sj √ ∑n ∑n Where: µj = 1 1 i=1(aij −µi)2. i=1 aij, sj = n−1 n

Then we calculate the correlation coefﬁcient matrix R = (rij)5∗5:

∑n k=1 ˜aki ∗˜akj rij = , i, j = 1, . . . , 5 (3) n −1

Afterwards, we calculate the eigenvalues λj and the corresponding eigenvectors of R, to form the ﬁve new index variables. On the basis of the eigenvalues, we can get the contribution rate b and the accumulative contributions rate α of the parameters.

λj ∑m bj = , j = 1, . . . , 5 (4) k=1 λk ∑p k=1 λk αp = ∑5 (5) k=1 λk

Since b=[72.8902,21.8503,3.8901,1.0350,0.3341] and α=[72.8902,94.7408,98.6309,99.6659,100], we select the ﬁrst three components as the three principle components y1, y2, y3 to replace the used ﬁve index variables.

According to the principle components, the ﬁrst component contributes most to the throughput, the second component contributes most to the cost, and the third compo- nent contributes most to the accidents prevention.

4.3 Analysis and Result

Multiplying the contribution rate with the value of corresponding principle compo- nents, we can obtain the comprehensive scores of our eight models.

p ∑ Z = bjyj (6) j=1

The ﬁnal score of the eight models are shown in Table 3.

From the result above, we ﬁnd that right-angled trapezoid is better than isosceles trapezoid and the stipulated merging pattern is better than normal merging pattern.

Rank Model Score Rank Model Score

1 7 2.5822 5 4 -0.6187

2 3 1.6134 6 1 -0.6190

3 8 -0.0457 7 6 -1.3492

4 5 -0.1332 8 2 -1.4298

When it comes to the size of the area, we assume that the longer the height of the trapezoid area is, the larger the size of the area is which may increase the throughput of the area. According to the scores listed above, the result is contrary to our assump- tion. Then we simulate a new circumstance whose height is half of the 5th kind of model and evaluate it through the method above. The evaluation score of this model is -0.6726, while the evaluation score of the 5th kind of model is -0.1332. Thus, we can come to a conclusion that it may exist an optimum height of the trapezoid area to make the throughput of the area come to its maximum. Meanwhile, we also should take the increment of the cost resulted from the increment of the height of the trapezoid area into consideration.

5 Find the Optimum Solution

5.1 Overview

From our evaluation model, we can see that the height of the trapezoid area and the merging pattern have a great impact on the throughput of the area following the toll bar- rier. When determining if there exists a better solution, we should include quantitative or qualitative estimates of these two parameters. Also, the number of tollbooths may inﬂuence the number of the vehicles passing through the toll barrier, while this outﬂow of the toll barrier may affect the trafﬁc pressure of the area following the toll barrier. So we should also take the number of tollbooths into consideration.

When it comes to the cost of the area which is determined by the size of the area, there are two parameters to indicate: the height of the trapezoid area and the number of toll booths which determine the length of one bottom of the trapezoid area and may add to the operating cost of the toll plaza.

Then we can build two models to ﬁnd the optimum solution. The ﬁrst one is a dif- ferential equation model aimed at minimizing the cost of the road construction and the operating cost of toll booths. The second one is a linear programming model calculating the optimum strategy of merging pattern.

5.2 Differential Equation Model

(1) Terms and Deﬁnitions Symbol Meaning

C total cost

W average waiting time per vehicle in the toll plaza

W1 time spent in lines

W2 service time

W3 time spent passing through the area following the toll barrier

v average time value of a person in one vehicle

µ average number of person in one vehicle

n the number of vehicles passing through the toll plaza

C1 the operation cost of a tollbooth per day

C2 the construction cost of unit area

F(t) value of inﬂux at t minute

O(t, B) value of outﬂux at t minute with B tollbooths

s the average number of vehicles which one tollbooth can serve per minute

k outﬂux barrier

• Inﬂux is the number of vehicles entering the toll plaza per minute.(veh/min)

• Outﬂux is the number of vehicles existing the toll plaza per minute.(veh/min)

• Total cost is the sum of the value of time wasted in the toll plaza, the operating cost of toll booths and the construction cost of the area.

(2) Data processing

From a previous research paper’s trafﬁc ﬂow data, we ﬁnd the value of inﬂux for a toll plaza on a given typical day. Since we need an inﬂux rate at every minute of the day, instead of just once an hour, we select a Fourier Series approximation with 8 terms to ﬁnd a close ﬁt[8]. The ﬁtting function of the inﬂux at t minute is described below where 24 = 0.2513. The approximation ﬁts the data point with an R2 value of 0.9997 which ω = 2π is close to 1. It represents the result is in good agreement with the research data.

F(t) = 41.68 −16.38 cos(tω) −18.59 cos(2tω) + 3.572 cos(3tω) + 7.876 cos(4tω) . . .

−0.5048 cos(tω) −2.970 cos(6tω) + 0.2518 cos(7tω) + 0.5785 cos(8tω) . . .

+ 12.53 sin(tω) + 0.6370 sin(2tω) −13.67 sin(3tω) + 0.4378 sin(4tω) . . .

+ 6.930 sin(5tω) + 0.4869 sin(6tω) −1.554 sin(7tω) −0.5871 sin(8tω) (7)

(3) Establishment We formulate a function C(B, H) to ﬁnd the number of tollbooths B and the height of the trapezoid area H that minimize the total cost C.

C(B, H) = (W1 + W2 + W3)vµn + C1B + C2H(BD −Ld) (8) 2

Firstly, we need to calculate the un-known parameters in the function.

• F(t) is calculated from the above data processing.

• For the randomness of O(t, B), we use the average value of outﬂux per minute in simulation as O(t, B).

• k(veh/min) is relevant to L and H, while irrelevant to B. If the value of outﬂux exceeds k, trafﬁc congestion may happen.

∫24

• We can integrate F(t) over time to calculate n = 0 3600F(t) dt.

• For W1 represents the average amount of time each time spent waiting in lines before reaching the tollbooth, we need to integrate over time to calculate how many cars were forced to wait in line. So, the value of W1(t) can be depicted as:

{∫24 ∫t 0 3600(F(τ)−Bs) dt dτ , F(τ) > Bs 0 n W1 = (9) F(τ) ≤Bs 0,

• The way to calculate W3 is similar to the way we used to ﬁnd W1.

{∫24 ∫t 0 3600(O(τ,B)−k) dt dτ , O(τ, B) > k 0 n W3 = (10) O(τ, B) ≤k 0,

• Apparently, W2 is the reciprocal of s. So, W2 = 1 s.

(4) Calculation

When solving the integral equation above, we set a variance range for B and calculate the corresponding W1 and W3 for each B respectively. A Mathematica quartic polynom- inal ﬁt is then done on the resulting points. Through this ﬁtting procedure, we can get the function W1(B) and W3(B).

To minimize the value of C(B, H), we take the partial derivative of C(B, H).

∂C(B, H) = vµn(∂W1(B) + ∂W3(B, H) ) + C1 + C2HD (11) ∂B ∂B ∂B 2

+ C2(BD −Ld) ∂C(B, H) = vµn∂W3(B, H) (12) ∂H ∂H 2

Set these two formulas equal to 0. Then, we can compute the stationary points and the Hessian matrix. If the matrix is a positive deﬁnite matrix, the stationary point is the optimum B and H. When it comes to the example the title cite in which the number of travel lanes L = 3, the optimum number of toll booths B = 6, and the optimum height of the trapezoid area H = 35.6472m.

5.3 Linear Programming Model

We develop a vehicle transition matrix TB∗L in which tij represents the probability of vehicles which exit from tollbooth i drive down to lane j. We can abstract a merging pattern from matrix T by selecting the largest element i of column j in the matrix which means vehicles exiting from tollbooth i will merge into travel lane j.

Since we assume that the service ability of each toll booth is the same, we set the out- ﬂux probability vector of the toll barrier as P = [ 1 B, 1 B, . . . , 1 B]B. To increase the through- put of the area following the toll barrier, we assume the number of fan in to each of the travel lane is allocated averagely. Then, we set the inﬂux probability of the travel lane following the toll barrier as Q = [ 1 L, L L, . . . , 1 L]L.

In order to allocate the vehicles to each travel lane following the toll barrier averagely, we get:

P ∗T = Q (13)

The total probability for vehicles driving down to each of the travel lane is 1.

L ∑ Tij = 1 (14) j=1

The objective is to maximize the throughput with the speciﬁed value of L, B, H. In other words, we need to minimize the desired length of the vehicles travel path between the toll barrier and the travel lane.

We build a simple model shown as ﬁgure 11 to calculate the length z of every travel path. √ H2 + [(j −1)d + (i −1)SD]2 z = (15) Then, we can get the objective function as following:

B L ∑ ∑ Tij ∗z min g = (16) i=1 j=1

From the conditions and object functions listed above, we have constructed a linear programming model.

B L ∑ ∑ √ H2 + [(j −1)d + (i −1)SD]2 Tij ∗ min g = object function:

i=1 j=1

 P ∗T = Q    L ∑ s.t.  Tij = 1   j=1

For example, when we set B = 6, L = 3, the optimum vehicle transition matrix T is as following.   1 0 0   1 0 0

0 1 0 T = 0 1 0

0 0 1

0 0 1

From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 and 2 should merge into lane 1. Vehicles leaving from tollbooth 3 and 4 should merge into lane 2. Vehicles leaving from tollbooth 5 and 6 should merge into lane 3.

5.4 Result and Model Testing

From the result above, we ﬁnd the optimum solution of three lanes is in the shape of isosceles trapezoid with six tollbooths and stipulated merging pattern and the height of the area following the toll barrier is 35.6472m .

In order to test if the solution is better than the above eight existing models, we put the corresponding data into our simulation model and evaluation model.

The ﬁnal score of our model is 4.3026 which is higher than the existing eight models we discussed above.

6 Effects and Adjustment

6.1 Light and Heavy Trafﬁc

Under the condition of light trafﬁc, the inﬂux and outﬂux value of the tollbooths will decline. For the drop of the number of vehicles, the possibility of trafﬁc congestion will decrease. Thus when it comes to light trafﬁc, the throughput of the area will not show up while the principle problem is that the number of toll booths may exceed the demand which may waste the operation cost of the area. We can calculate the optimum number of tollbooths by modifying the inﬂux parameter of our differential equation model. Then some of the redundant tollbooths can be shut down appropriately to ensure that we can reduce the operation cost to the greatest extend without reducing the throughput of the area.

When it comes to heavy trafﬁc, the possibility of trafﬁc congestion will increase for the rise of inﬂux value of the tollbooths. Our model which adopts an optimum merging strategy, number of tollbooths and the size of the area following the toll barriers can work well under the pressure of heavy trafﬁc. However, when the number of vehicles reach a certain level, we can adjust the merging strategy to promote the capacity of the area following the toll barrier. For example, if we ﬁnd the nearest lane a of the toll barrier i, then we can set a proper number of b based on the reality and value of L to make tij = 0, j /∈[a −b, a + b].

On the one hand, the adjustment can reduce the delay time of vehicles passing through the area following the toll barrier. On the other hand, it can reduce the possibility of accident which caused from heavy trafﬁc while it may increase the length of queue at merging points which should be studied by our further research.

6.2 Add Autonomous Vehicles

After our research, we ﬁnd that the autonomous vehicles have the following advantages[9]:

• Safety: The vehicle is controlled by computer. So it can adjust its driving route on time and choose the safer path when entering the area following the toll barrier. As a result, self-driving can reduce the risk of trafﬁc accidents caused by limitations of human beings.

• Efﬁciency: Compared to normal vehicles, autonomous vehicles can adjust the gap between vehicles and the speed of vehicles intelligently which can lead to lower possibility of trafﬁc congestion.

Due to the safety and the efﬁciency of autonomous vehicles, we do not have to stip- ulate the merge pattern of the area following the toll barrier which can bring the advan- tages of autonomous vehicles to the full play.

6.3 Compositions of Tollbooths

Different compositions of tollbooths may affect the outﬂux value of the toll barrier, which is represented by outﬂux probability vector of the toll barrier P in the linear pro- gramming model.

There are three kinds of tollbooths listed in the problem. We set the average service rate of tollbooths i in type k as rik in which type 1 is conventional tollbooth, type 2 is exact-change tollbooth, and type 3 is electronic toll collection booth. From our research[9], ri1 = 5, ri2 = 7, and ri3 = 20 .The total service rate is r = ∑B i=1 rik, k = 1, 2, 3. The outﬂux probability vector of the toll barrier P should be modiﬁed as P ′ = n r [rik, . . . , rBk], k = 1, 2, 3.

Under the optimum condition we calculated in the previous models in which L = 3, B = 6, H = 35.6472, D = 5.5, d = 3.5, we assume one kind of proportion of tollbooths in which NO.1 and NO.2 tollbooths are electronic toll collection booths, No.3 and No.4 tollbooths are conventional toll booths, and No.5 and No.6 tollbooths are exact-change tollbooths. Then we input the data into our linear programming model. The optimum result vehicle transition matrix T1 is as following:

  1 0 0   0 0.8833 0.1167

0.2667 0.7333 0 T1 = 0 0 1

0 0 1

0 0 1

From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 enter into lane 1. Vehicles leaving from tollbooth 2 and 3 should merge into lane 2. Vehicles leaving from tollbooth 4, 5 and 6 should merge into lane 3.

Then, we assume another one kind of proportion of tollbooths in which NO.1, NO.2, NO.3 tollbooths are electronic toll collection booths, No.4 tollbooth is conventional toll booths, and No.5 and No.6 tollbooths are exact-change tollbooths. Then we input the data into our linear programming model. The optimum result vehicle transition matrix T2 is as following:   1 0 0   0.3167 0.6833 0

0 0.6363 0.3667 T2 = 0 0 1

0 0 1

0 0 1

From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 enter into lane 1. Vehicles leaving from tollbooth 2 and 3 should merge into lane 2. Vehicles leaving from tollbooth 4, 5 and 6 should merge into lane 3.

In the way we illustrated in two examples above, Our model can adjust to different proportions of the three common kinds of tollbooths.

Then, we take extreme cases into consideration. If the proportion of electronic toll collection booths is too high, the number of vehicles exiting the toll barrier will increase signiﬁcantly. It is similar to the condition of heavy trafﬁc, we can solve it in the same way as the heavy trafﬁc condition.

7 Sensitivity Analysis

We do two kinds of sensitivity analysis on our linear programming model.

7.1 Reduced Cost

Reduced cost is the increment of objective function, when one of the variables increased by one unit. We use LINGO to calculate the reduced cost of every variables. The result is shown in ﬁgure 13.

The result indicates that when variable t13 and t61 increase by one unit, it will produce a larger deviation on the objective function. In other words, the desired number of the vehicles selecting the longest path to get into the travel lane increases signiﬁcantly, while the throughput of the area will decline at the same time. These kinds of selection may lead to the increment of merging points which is bad for accident prevention. Therefore, we should avoid this kind of situation.

7.2 Change Range of Variables

We use LINGO to calculate the change range of variables with the same optimum solution. The result is shown in ﬁgure 14.

The result indicates the reasonable error range of the construction in reality.

8 Conclusion

8.1 Strengths

• Applies widely The differential equation model and the linear programming model can be easily modiﬁed to accommodate to various situation.

• The result is a global optimum solution Our differential equation model consider the time value of the delayed passengers and the construction cost of the area at the same time which can result in a global optimum solution.

• Good ﬂexibility According to our analysis, our model can always ﬁnd the optimum solution under various kinds of conditions.

• Technical supporting We use many theory and methods to support our work. And each one of them is used reasonably and properly.

8.2 Weakness

• Inaccuracy When considering the value of parameters, we obtain them through a lot of differ- ent research papers which may inﬂuence the result of our model.

• Simplifying assumptions To simplify the model, we make a few assumptions which may affect the result of our model.

• Lack of data For the lack of data, we have to simulate the models abstracted from the reality to obtain the data we need which may be different from the real data.
