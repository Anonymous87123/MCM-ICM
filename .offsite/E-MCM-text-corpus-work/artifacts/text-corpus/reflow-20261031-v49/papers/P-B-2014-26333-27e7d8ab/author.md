For ofﬁce use only For ofﬁce use only

T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

2014 Mathematical Contest in Modeling (MCM) Summary Sheet

Abstract

Our goal is a model that can evaluate the performance of the keep-right-except- to-pass rule and other alternatives by simulating the trafﬁc ﬂow on the freeway. We construct models to analyze ﬁve inﬂuencing factors. Then we integrate multi- ple criteria to judge the performance of nine rules using a fuzzy synthetic evalua- tion(FSE).

Our basic lane-changing model focuses on the behavior of a speciﬁc vehicle on the freeway. We carefully examine the vehicle ˛a´rs lane-changing behavior, an essential component of overtaking.

We extend our model with a cellular-automaton-based approach. We assume that the drivers will change the lane with a probability if the trigger and safety con- ditions are satisﬁed. Using periodic boundary conditions, we seek to simulate a section of a long freeway, which is hardly inﬂuenced by real boundary condition- s. In addition, we can accurately control the occupancy of the freeway. We can simulate the trafﬁc ﬂow under several conditions by varying the number of lanes, maximum speed limit, minimum speed limit and signaling behavior.

Four other basic rules such as free-overtaking rule are examined by revising the laws governing the cells in the cellular automaton. Then we design ﬁve improved rules based on the basic rules attempting to obtain an optimal rule.

We choose ﬂow rate, average speed as trafﬁc ﬂow criteria, sharp braking fre- quency as a safety criterion and satisfaction and standard deviation of speed as ex- perience criteria. Then we use a fuzzy synthetic evaluation technique to integrate these criteria to determine the performance of each rule. We ﬁnd that in a light trafﬁc case, a partial-assigned-lane-and-keep-right rule performs the best while in a heavy trafﬁc situation, a different-speed-limit-on-each-lane rule is preferred.

We change the probability of lane-changing to adjust our model to a country like Great Britain. Moreover, we change that parameter to simulate a freeway fully controlled by an intelligent system and observe small deviations.

Additionally, we reﬁne our extended model considering the ramps. We adopt open boundary conditions and assume that the vehicles ﬂowing in are Poisson- distributed. Finally, we change parameters to analyze freeways with ramps under different conditions.

February 10, 2014

Abstract

Our goal is a model that can evaluate the performance of the keep-right- except-to-pass rule and other alternatives by simulating the trafﬁc ﬂow on the freeway. We construct models to analyze ﬁve inﬂuencing factors. Then we integrate multiple criteria to judge the performance of nine rules using a fuzzy synthetic evaluation(FSE).

Our basic lane-changing model focuses on the behavior of a speciﬁc ve- hicle on the freeway. We carefully examine the vehicles lane-changing be- havior, an essential component of overtaking.

We extend our model with a cellular-automaton-based approach. We assume that the drivers will change the lane with a probability if the trigger and safety conditions are satisﬁed. Using periodic boundary conditions, we seek to simulate a section of a long freeway, which is hardly inﬂuenced by real boundary conditions. In addition, we can accurately control the occu- pancy of the freeway. We can simulate the trafﬁc ﬂow under several con- ditions by varying the number of lanes, maximum speed limit, minimum speed limit and signaling behavior.

Four other basic rules such as free-overtaking rule are examined by re- vising the laws governing the cells in the cellular automaton. Then we de- sign ﬁve improved rules based on the basic rules attempting to obtain an optimal rule.

We choose ﬂow rate, average speed as trafﬁc ﬂow criteria, sharp brak- ing frequency as a safety criterion and satisfaction and standard deviation of speed as experience criteria. Then we use a fuzzy synthetic evaluation technique to integrate these criteria to determine the performance of each rule. We ﬁnd that in a light trafﬁc case, a partial-assigned-lane-and-keep- right rule performs the best while in a heavy trafﬁc situation, a different- speed-limit-on-each-lane rule is preferred.

We change the probability of lane-changing to adjust our model to a country like Great Britain. Moreover, we change that parameter to simu- late a freeway fully controlled by an intelligent system and observe small deviations.

Additionally, we reﬁne our extended model considering the ramps. We adopt open boundary conditions and assume that the vehicles ﬂowing in

1 are Poisson-distributed. Finally, we change parameters to analyze freeways with ramps under different conditions.

10 Strengths and Weaknesses

. . . . . . . . . . . . . . . . . . . . . . . . . 52 10.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 10.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

1 Introduction

A freeway is a highway designed for high-speed vehicles. It provides an unhin- dered ﬂow of trafﬁc with no trafﬁc lights or intersections.[1] Typically, a freeway has several advantages over common roads, such as the high speed and the high trafﬁc volume. The Keep-Right-Except-To-Pass rule, also known as “Slow- er Trafﬁc Keep Right”, is often employed in right-hand trafﬁc in order to raise the quality of trafﬁc ﬂow, especially the quality of trafﬁc ﬂow on freeways.[2] The effectiveness of the rule will not only increase utilization of freeways but also enhance driver satisfaction. Thus, it will be exhilarating if we can design another rule that can outperform the current rule. In this paper, we simulate different rules of overtaking and compare them so as to decide the optimal rule.

1.1 Restatement of the Problem

We are required to build a mathematical model to analyze the performance of the keep-right-except-to-pass rule the other alternatives. We decompose the problem into two sub-problems:

• Build a model that can simulate the overtaking process.

• Propose a mathematical criterion to determine the performance of a spe- ciﬁc rule.

In the ﬁrst step, we seek to build a model with the inputs of speed limits and other factors. Most importantly, the model should reﬂect the mechanism of the given rule. Then we can change the inputs to do several simulations. Also, we can change the mechanism to apply alternative rules to our model. Finally, we can obtain the outputs of our model.

In the second step, we seek to use the outputs of our model to propose a math- ematical criterion to evaluate different rules. We will consider the trade-off be- tween trafﬁc ﬂow, safety and other factors. We will design other rules and de- termine which rule is the best.

Then we attempt to adjust our model and apply it to countries like Great Britain. We also consider the inﬂuence of intelligent system.

1.2 Literature Review

A model for the simulation of freeway trafﬁc is inevitable to the study of the performance of the rule. German physicists Nagel and Schreckenberg built a theoretical model for the simulation of freeway trafﬁc, which is a simple cellular automaton model for road trafﬁc ﬂow known as “N-S model”.[3] They deﬁned a one-dimensional lane with two kinds of boundary conditions-open or periodic boundary conditions: In their model, each site may either be occupied by one vehicle or it may be empty. Each vehicle has an integer velocity with values between zero and vmax. During each time step, four sub-steps are performed: acceleration, slowing down, randomization and car motion.

After the single-lane model was established, several scientists were devoted to building a multi-lane model. The main difﬁculty was to set up the rules for shifting to the neighboring lane. Rickert et al. introduced a two-lane model with two parallel lanes in their article.[4] Several conditions have to be fulﬁlled before the vehicle changing to other lanes: (1) another vehicle is in the way (2) other lanes are better and (3) collision will not happen. They also simulated the model using a cellular automaton, and the results were quite reasonable.

As a matter of fact, a multi-lane model does not have to be symmetric. Differ- ence may include different speed limits on each lane, different kinds of cars, etc. In 1997, Chowdhury et al. ﬁrst simulated the model with different kinds of ve- hicles. [5] In their model, different maximum possible speeds are introduced to different kinds of vehicles. The result shows that even if the portion of “slow cars” is relatively low, “fast cars” can only move in a low speed.

Further studies are carried out based on the comparison between model and reality. Knospe, Santen suggested that the inﬂuence of “slow cars” might have been over-estimated.[6] They recommended to consider the impact of expectan- cy in the model.

2 Assumptions and Justiﬁcations

To simplify the problem, we make the following basic assumptions, each of which is properly justiﬁed.

• No pedestrian can affect the vehicles on freeways. Usually, pedestrians have no access to freeways, let alone going across the freeways.

• We ignore the force of crosswind to a vehicle when it is changing lanes.This impact is negligible compared with that of the head wind.

• Drivers cannot drive on the emergency lane. Typically, the emergency lane is not for use of ﬂowing trafﬁc. [7]

• In our model, we only consider the freeway as completely ﬂat, with no curve or slopes. This assumption greatly simplify our model and allow us to focus on the nature of overtaking.

• We assume that all drivers act based on the same set of rules. We clas- sify drivers as aggressive and non-aggressive and both groups follow the relevant rules.

3 Notations

All the variables and constants used in this paper are listed in Table 1 and Table 2.

Table 1 Symbol Table–Constants Symbol Deﬁnition Units

Constants λ Expectancy of poisson-distribution unitless pslow Possibility that a vehicle slows down randomly unitless pleft Possibility that a vehicle shift to the left lane when possible unitless pright Possibility that a vehicle shift to the right lane when possible unitless pexit Possibility that a vehicle need to move off through the exit ramp unitless Table 2 Symbol Table–Variables Symbol Deﬁnition Units

Variables vs Speed of vehicles cell/time-step vexpect Expected speed of vehicles cell/time-step vlf Speed of the vehicle on the left lane ahead cell/time-step vlb Speed of the vehicle on the left lane behind cell/time-step vrf Speed of the vehicle on the right lane ahead cell/time-step vrb Speed of the vehicle on the right lane behind cell/time-step t Time time-step

Dl,f,gap Left front gap cell Dl,b,gap Left back gap cell Dr,f,gap Right front gap cell Dr,b,gap Right back gap cell vehiclei The jth vehicle on the ith lane unitless j vi Speed of vehiclei j (t) j at tth time-step cell/time-step vi Expcted speed of vehiclei cell/time-step j,expect j gapi Front gap of vehiclei j (t) j at tth time-step cell xi Location of vehiclei j (t) j at tth time-step cell lfgapi Left front gap of vehiclei cell j j lbgapi Left back gap of vehiclei cell j j rfgapi Right front gap of vehiclei cell j j rbgapi Right back gap of vehiclei cell j j lbvi Speed of the vehicle behind vehiclei j on the left lane cell/time-step j rbvi Speed of the vehicle behind vehiclei j on the right lane cell/time-step j

v (t) Average speed at tth time-step cell/time-step N The number of vehicles passing a certain point on the highway unitless N (t) The number of vehicles on the highway at tth time-step unitless Nj (t) The number of vehicles on the jth lane at tth time-step unitless Nshift (t) The number of vehicles changing lanes at tth time-step unitless texpect Expected time time-step tactual Actual time time-step

aij Value of the jth criterion of the ith rule uncertain u0 Value of the jth criterion of the ideal scheme uncertain j rij Relative deviation of the jth criterion of the ith rule unitless vj coefﬁcient of variation of the jth criterion unitless wj Weight of the jth criterion unitless Fi Relative deviation of the ith rule unitless

4 Model Overview

Most research for trafﬁc ﬂow can be classiﬁed as microscopic and macroscopic. As macroscopic methods are difﬁcult to apply to our problem, we approach the problem with microscopic techniques. Our study into the keep-right-except-to- pass rule takes several approaches.

Our basic model allows us to have a close look at the lane-changing behavior. We focus on the incentive of changing lane and the conditions for a successful lane changing. We treat the changing-to-the-left-lane behavior and changing-to- the-right-lane behavior differently. This model gives us some intuition about the rule and serves as a stepping stone to our later study.

The extended model views the problem from a wider perspective. We consider a section of freeway and divide it into lattices. Then we run a cellular automa- ton to simulate the behavior of vehicles. The essence of the model is the laws governing the cells. We derive the laws according to the analysis of our basic model. Moreover, using periodic boundary conditions, we treat the freeway as a “ring road” so as to accurately control the density. Thus, we call it a “Ring Road” model.

Our reﬁned model attempts to tackle a more realistic while more challenging problem. We add an entrance ramp and an exit ramp to our cellular automaton. The laws for the entering and exiting vehicles are also added. We use a Poisson distribution to simulate vehicles moving in from the start point.

We use the extended “Ring Road” model as a standard model to analyze the problem and all results have this model at their cores.

5 The Keep-Right-Except-To-Pass Model

We will start with the idea of the basic model. Then we present the cellular automaton and explain the algorithm. Finally, we introduce our additional work in the reﬁned model.

5.1 The Basic Lane-changing Model

The basic model is a microscopic approach. A typical overtaking behavior con- sists of ﬁve actions: signal for three seconds, change lane, accelerate, signal back and change back to the former lane. Among these actions, lane-changing is the most crucial part. An analysis of lane-changing behavior might shed light on the nature of the quality of trafﬁc ﬂow.

5.1.1 Changing to the Left Lane

When making the decision of whether to overtake, the driver will ﬁrst decide whether to change to the left lane. There are two main considerations [8] :

• A reason or a trigger consideration

• A safety consideration

The former means that the vehicle ahead moves slowly enough, which will trig- ger the driver to overtake it. The latter indicates that he will take safety into account. In other words, if there is a high-speed vehicle driving on the left lane, he will choose to stay on the current lane to avoid collision. Based on these considerations, we can introduce some mathematical intuition into the problem.

Figure 1 Change-to-the-left-lane

Based on the trigger consideration, the speed of the cars satisﬁes

vexpect > vs

In terms of safety, the left back gap should satisfy

Dl,b,gap > (vlb −vs)t Additionally, the red car attempts to accelerate. It is unreasonable if it changes to the passing lane while slowing down. This happens if there is a vehicle ahead. Therefore, the left front gap should satisfy

Dl,f,gap > (vs −vlf)t

The mathematical expressions above give the basic conditions of a change-to- the-left-lane behavior.

5.1.2 Changing Back to the Right Lane

After accelerating and passing the slow vehicle ahead, the driver tends to change back to the former lane due to the keep-right-except-to-pass rule. However, this lane-changing behavior will be subject to the following constraints:

• There is no incentive to pass the car in the current passing lane. If so, and if it is a multi-lane freeway, the driver would prefer to continue to overtake the car ahead and change to the left passing lane rather than change back to the former lane.

• It is safe to change back. This condition means that the driver should pass the slow car and ensure that he will not collide with the slow car when changing back.

• After changing back to the former lane, the driver can maintain his rela- tively high speed. Otherwise, he will intend to pass more than one car in an overtaking process.

The ﬁrst constraint can be treated as the changing-to-the-left-lane situation as mentioned above and the other conditions can be stated as the following math- ematical expressions.

Due to the safety consideration, the right back gap should yield

Dr,b,gap > (vrb −vs)t

Due to the intention to pass more cars, the right front gap should yield

Dr,b,gap > (vs −vrf)t Figure 2 Change-back-to-the-right-lane

5.2 The Extended “Ring Road” Model

In order to understand how the rule works in a trafﬁc ﬂow, we have to ana- lyze the behavior of vehicles in a relatively long way, which will be more like a freeway. One intuition for modeling the problem is to think of it as a stochas- tic process. Therefore, we use a cellular automaton to simulate the behavior of vehicles on a freeway.

A cellular automaton is a discrete model that describes the time development of a system. It is referred to as a discrete model because it treats time as a discrete variable. The model requires an initial conﬁguration and a set of ﬁxed laws that determine how the system develops. At every time-step, the cellular automaton will advance incrementally and all the laws will be implemented.

5.2.1 Assumptions of the Model

The following general assumptions are made based on common sense and we use them throughout our model.

• Drivers obey the rules with a probability. It is obvious in real life that a driver might not want to change lane even if all the conditions are satisﬁed.

We assume that a driver change to the left lane and the right lane with the probability pleft and pright respectively when possible.

• All drivers tend to drive as fast as possible while keeping a safe follow- ing distance. Nearly every driver wants to drive faster on the freeway as long as there is enough time for him to react if the vehicle ahead decel- erates. Also, the maximum speed is limited by the vehicle type and the speed limit of freeway.

• Drivers are “myopic”, which means that they can only see one vehicle in front of him, one vehicle behind him and several vehicles on the neigh- boring lanes. A driver can see the vehicle in front of him by eyes and see the vehicle behind him with the help of rearview mirrors. Moreover, he can turn his head to left and right to see the car on the neighboring lanes. He might see cars, say, on the left lane of the left lane, but he will not take this information into account when deciding whether to change lanes. Thus, we simply suppose that the drivers cannot see these vehicles and other vehicles much further.

• Drivers make decisions only according to his own interest. Because driver- s are “myopic”, they cannot know the conditions of the whole freeway.

Consequently, they make greedy decisions in order to pass the freeway in a shorter time.

Additionally, in order to implement cellular automaton on our problem, we pro- pose the following assumptions:

• We assume that lane-changing does not cost additional time. Obviously, vehicles change lanes while moving. Although the travelling distance of lane-changing seems longer compared with just moving in one lane, the drivers tend to accelerate to change lanes. Thus, we simply suppose that the lane-changing costs the same amount of time as moving in one lane.

This assumption helps a lot to build a cellular automaton.

• Each cell represents a 4m*6m area. The road’s length is 2000 cells. A lane’s width is 1 cell. We divide a multilane freeway into equally parti- tioned lanes. We choose a length of 12km to simulate because of the trade- off between time complexity and the completeness of the model.Also, each array of cells represents a lane.

• Every time-step represents 1 second. Such an assumption is made by n- early all cellular automaton techniques.

• We run 20000 time-step and analyze the last 1000 steps. This ensures us to obtain steady-state conditions.

• While all vehicles have a trend to reach the maximum speed, every sin- gle vehicle randomly slows down with probability p. This randomization is a characteristic of trafﬁc ﬂow.

• Acceleration is done steadily while any kind of deceleration can be done in one time-step. Steady acceleration is an energy-saving behavior and drivers will decelerate to avoid possible collisions.

5.2.2 Characteristics of Vehicles

We classify the vehicles into three groups:

• Cars: Cars are those small vehicles, which usually can have high speeds.

• Buses: Buses are large vehicles used for carrying people, and their speeds can be relatively high.

• Trucks: Trucks are large vehicles used for moving heavy articles, and they can only have lower speeds.

Then we deﬁne the characteristics of the three types of vehicles:

• Occupancy: Each car occupies one cell. Since a typical car’s length is 3.6m- 4.6m. The car cannot fully occupy a cell. We place the car in the middle of the cell and treat the space in front of and behind the car as safe distance.

Accordingly, each bus and each truck occupies two cells with safe distance preserved.

• Maximum speed: At each time-step, cars cannot move more than 6 cells, which means that its maximum speed is 129.6km/h. Similarly, buses can- not move more than 5 cells per time step, since they are large so that they cannot move at a higher speed. Lastly, trucks carry heavy goods so they have the lowest maximum speed. We suppose it is 3 cells per time-step, which equals 64.8km/h. The maximum speed here is based on the vehi- cles themselves. If they exceed the speed limit, vehicles can drive no more than the limit. In China, the maximum speed limit of freeway is 120km/h and the lowest speed limit of that is 60km/h. The role of speed limit is examined by comparing situations under different limits.

• Percentage: We assume that cars account for 60% of the trafﬁc ﬂow, buses account for 30% and trucks account for 10%. This assumption are based on the data collected by [9]

The characteristics are listed in Table 3.

Table 3 Characteristics of Vehicles Type Occupancy Maximum speed percentage

60% Car 1 cell 6 cells/sec 30% Bus 2 cells 5 cells/sec 10% Truck 2 cells 3 cells/sec

5.2.3 Laws Governing the Cellular Automaton

Our cellular automaton is implemented by an algorithm, the essence of the al- gorithm is the set of laws sequentially implemented in every time-step. In this subsection, we will introduce the laws. These laws are based on the previous analysis and are expressed from a computational perspective.

Step 1: moving

These laws are set based on the assumptions of the model and the char- acteristics of the vehicles. We denote the jth vehicle on lane i by vehiclei j.

(a) Determine the speed Our three laws below was implemented sequentially, so we use (t + 1 3), (t + 2 3) to denote the intermediate state.

i. Acceleration

Figure 3 Clariﬁcation of some denotes All drivers tend to drive as fast as possible:

j(t + 1 If vi j(t) < vi then vi 3) = vi j,expect, j(t) + 1

Where vi j(t) is the speed of vehiclei j at time t, vi j,expect means the expected speed of vehiclei j.

ii. Randomization Every vehicle randomly slows down by 1 with probability pslow.

Mathematically,

j(t + 2 j(t + 1 vi 3) = vi 3) −1

iii. Deceleration(because of other vehicles) To maintain a safe following distance and to avoid collision, a cell cannot be occupied by more than one vehicle at the same time-step.

j(t + 2 If vi 3) > gapi then vi j(t + 1) = gapi j(t), j(t)

Where gapi j(t) is the gap between vehiclei j and the vehicle a- head.

(b) Determine the location We derive the locations based on the speeds above:

xi j(t + 1) = xi j(t) + vi j(t + 1)

gapi j = xi+1 −xi j −1 j Where xi j is the location of vehiclei j.

Step 2: lane-changing

These rules are set based on

(a) Changing to the left lane

i. Based on trigger criterion, the driver tends to change to the left if the vehicle ahead moves so slow that he fails to reach his expected speed.

gapi j(t) < vi j,expect

ii. Then, take acceleration criterion into account, we have

gapi j(t) < lfgapi j

Where lfgapi j is the left front gap of vehiclei j.

Figure 4 Flow chart of cellular automaton iii. Lastly, consider the factor of safety, we have

lbgapi j > lbvi j Where lbgapi j is the left back gap of vehiclei j, lbvi j is the speed of the vehicle behind on the left lane.

(b) Changing to the right lane i. To check the rules in 2.1 above, if any one of the rules are not satisﬁed, the driver cannot change to the left lane.

ii. To consider safety, we have

rfgapi j > vi j Where rfgapi j is the right front gap of vehiclei j.

iii. To consider another safety criterion, we have

rbgapi j > rbvi j Where rbgapi j is the right back gap of vehiclei j, rbvi j is the speed of the vehicle behind on the right lane.

The algorithm is diagrammed in Figure 4.

5.2.4 Modeling Using Periodic Boundary Conditions

To run a cellular automaton, we need to specify the boundary conditions and the initial condition. Boundary conditions determine the way vehicles move into our system and the way they move out of our system. Likewise, an initial condition determines the distribution of vehicles in our system and the speeds of them.

Inspired by Nagel and Schreckenberg’s work [3], we tackle the problem with periodic boundary conditions. Periodic boundary conditions assume that the vehicles moving out of the freeway will immediately appear at the front of the system, so the total number of vehicles is a constant during the dynamics. Thus, we can accurately deﬁne a constant system density and study the performance of the rule with varying density. Moreover, periodic boundary conditions turn our road into a closed system, so it is similar to the case that all vehicles are moving on a circle. We, in turn, name our extended model as a “Ring Road” model.

Although there is no such short ring road in reality, this model still holds true be- cause we can imagine that a freeway is made up of several equally partitioned sections and the vehicles on all the sections are identical. Obviously, this sit- uation satisﬁes periodic boundary conditions. This is how periodic boundary conditions relate theory with reality.

5.3 The Reﬁned Model with Ramps

Even though the “Ring Road” model is good enough to solve the problem, it fails to consider the effect of ramps. Consequently, we reﬁne our model by adding entrance and exit ramps and applying open boundary conditions.

5.3.1 Adding Entrance and Exit Ramps

Vehicles may also use an entrance ramp to enter the freeway. The entrance ramp- s give them a chance to accelerate to the expected speed. However, most ramps are too short to allow them to speed up to, say, 100km/h. As a result, the vehi- cles on the right-most lane might slow down to yield to the incoming vehicles or incoming vehicles might hard to enter the freeway. Both cases might have dele- terious effects on the quality of trafﬁc ﬂow. Likewise, vehicles have to decelerate in order to enter an exit ramp, and similar problem will occur.

an exit ramp was followed by an entrance ramp. We add the ramps based on this fact.

The laws mentioned in the previous section are still valid, and the only differ- ence is how the incoming vehicles enter the freeway. We add some additional laws to instruct the behavior of incoming vehicles. To introduce the concept of ramps in our cellular automaton, we add the following assumptions.

Figure 5 A real freeway section containing ramps

5.3.2 Additional Assumptions in the Reﬁned Model

• The exit ramp: We assume that the overlap between the freeway and the exit ramp ranges from the 850th cell to the 900th cell, which is 300m.

• The entrance ramp: We assume that the overlap between the freeway and the entrance ramp ranges from the 1100th cell to the 1500th cell, which is 300m.

5.3.3 Additional Laws

• Off-ramp law: If the vehicle wants to go off the free way(how to determine this will be discussed later), it is not allowed to change to left lane after it reaches the 700th cell. At the same time, it will slow down to 3cell/s. If the vehicle is on the right-most lane between the 850th cell and the 900th cell, we assume that it can move into the ramp at the next time step if it wants to. Since in reality exit ramps usually contain two lanes and the ratio of vehicles exit at one ramp is low, this assumption is reasonable. If it misses the exit, it will not be governed by this additional law anymore.

• On-ramp law: For a vehicle on the entrance lamp, if the laws of changing to the left lane are satisﬁed, it can go into the freeway during the next time- step. Otherwise, it will continue to move forward.

5.3.4 Modeling Using Open Boundary Conditions

After we introduce ramps into our model, it is no longer reasonable to consider it as a closed system. Thus, we must use open boundary conditions to determine how the vehicles ﬂow in. Considering that the amount of trafﬁc is stochastic and the input of the system is discrete, a generally used approach is to model the input of vehicles as a Poisson process. Consequently, we assume that the number of vehicles ﬂowing in from the starting point in any interval of length t is Poisson-distributed with mean λt.

While moving into the system, vehicles tend to move off through the exit ramp with a probability pexit. And the vehicles ﬂowing in from the entrance ramp in any interval of length t is 0-1-distributed with mean λt. In other words, we try to let the number of vehicles from the entrance ramp equal the number of vehicles from the exit ramp. However, as discussed above, some vehicles may fail to exit the freeway and some others may fail to enter the freeway. We view both of them as bad characteristics of the trafﬁc ﬂow. We analyze these characteristics and we will discuss them in the next section.

6 Results: Inﬂuencing Factors

In this section, we ﬁrst give a deﬁnition of light and heavy trafﬁc. Then we explicitly deﬁne four factors and change one factor each time in order to ana- lyze how this factor inﬂuence the performance of the Keep-Right-Except-To-Pass Rule.

We run several simulations with cellular automaton and ﬁnd that the trafﬁc ﬂow can be classiﬁed into two groups. The time space diagram (Figure 8) demon- strates these two kinds of trafﬁc ﬂow. The diagram shows the trace of every vehicle in the simulation. A gentle trace indicates a low speed. Conversely, a steep trace indicates a high speed.

(a) Time space diagram(occupancy=0.1) (b) Time space diagram(occupancy=0.4)

Figure 6

• From the left diagram, we can clearly see that the vehicles with a high speed can continue with the high speed which indicates that it is not con- strained by slower vehicles. This is a situation of light trafﬁc.

• From the right diagram, we can see that no vehicle can reach a high speed, which indicates that there is a congestion. This is a situation of heavy trafﬁc.

6.1 Variables and Criteria

We choose number of lanes, the maximum speed limit, the minimum speed limit and signaling behavior as our variables. To judge the effectiveness of the rule, we propose the following criteria:

• Flow rate: ﬂow rate is the number of vehicles passing a point on a highway per unit time.[10] flow rate = N T where N stands for the number of vehicles passing a point on the highway in the time of T.

• Average speed: the average speed of all vehicles passing a point on a high- way or a lane over some speciﬁed time period.

Nj(t) 3 1 X X vi average speed v(t) = j(t) N(t) j=1 i=1

where N(t) stands for the number of vehicles on the freeway, and Nj(t) stands for the number of vehicles on jth lane.

• Lane utilization ratio: lane utilization ratio is deﬁned as the ratio between the number of vehicles on the lane to the total number of vehicle on the freeway.

lane utilization ratioi = Nj(t) N(t)

• Sharp braking frequency: we do not consider the occurrence of accidents in our simulation, since we view accidents as abnormal events and it is difﬁcult to consider abnormal events in microscopic models. Instead, we use sharp braking frequency as an indicator of unsafety. Sharp braking fre- quency occurs when a vehicle’s speed decreases by more than 2 cell/time- step. If this happens in our simulation, we assume that it is more likely to cause an accident in reality.

• Shift ratio: the number of shifts per unit time.

shift ratio = Nshift(t) N(t)

where Nshift(t) stands for the number of vehicles changing lanes at tth time step.

• Satisfaction: if a vehicle fails to reach its maximum speed, the driver’s satisfaction will decrease. We deﬁne the expected time texpect as the time it takes to drive with the maximum speed through a given distance. We deﬁne the actual time tactual as the time it actually takes to drive through the same distance. Then we derive the criteria by dividing expected time by actual time. The value of satisfaction ranges from 0 to 1.

satisfaction = texpect tactual • Standard deviation of speed: people might feel uncomfortable if the ve- hicle continues to accelerate and decelerate. We use standard deviation of speed to measure this kind of discomfort.

v Nj(t) 3 T u 1 u X X X [vi j(t) −v(t)]2 Std. deviation of speed = t N(t) t=1 j=1 i=1

6.2 Number of Lanes

6.2.1 Flow Rate

From the ﬂow rate and occupancy ﬁgure, we can obtain an optimal occupancy. In a low occupancy situation, the number of cars are too low. Although they are more likely to reach their maximum speeds, the road resources are not fully utilized, so the total ﬂow rate is low. In a high occupancy situation, the number of cars are too high, and it might cause a trafﬁc congestion. We expect an optimal occupancy and view it as a watershed of light trafﬁc and heavy trafﬁc.

Total ﬂow rate under the condition of different occupancies (3 & 4 lanes) Figure 7

From Figure 7, we can see that the optimal occupancy for a 3-lane freeway and a 4-lane freeway is between 0.2 and 0.3. Thus, in our following analysis, we choose an occupancy of 0.1 to represent a light trafﬁc condition and an occu- pancy of 0.4 to represent a heavy trafﬁc condition.

(a) Flow rate of each lane (3 lanes) (b) Flow rate of each lane (4 lanes)

Figure 8

We also calculate the ﬂow rate of each lane and sequence them from left to right. From the ﬁgures, we conclude that the optimal occupancy of rightmost lane is lower than that of leftmost lane. This tendency holds true for both 3-lane and 4-lane freeways. However, it’s not a signiﬁcant difference.

6.2.2 Average Speed

Average speed under the condition of different occupancies (3 & 4 lanes) Figure 9

As occupancy increases, the average speed tends to decrease due to congestion. This common sense can be justiﬁed from the speed-occupancy Figure 9. Sur- prisingly, the curves for 3-lane and 4-lane coincide! This result indicates that different lane numbers may hardly change the performance of the rule under the condition of the same occupancy.

(a) Average speed of each lane (3 lanes) (b) Average speed of each lane (4 lanes)

Figure 10

From the average speed of each lane, we can conclude that the leftmost lane has the highest speed and the rightmost lane has the lowest speed. This is because the rule requires drivers to overtake from the left.

6.2.3 Lane Utilization Ratio

(a) Lane utilization ratio of each lane (3 lanes) (b) Lane utilization ratio of each lane (4 lanes)

Figure 11 From the Figure 11, we can know that the lane utilization ratio of the leftmost lane increases as occupancy increases. It is reasonable because when occupancy increases, more vehicles use the leftmost lane to overtake. In contrast, in the light trafﬁc situation, the lane utilization ratio of the rightmost lane decreases as occupancy increases. It is because more vehicles try to change to the middle lane to move faster. The increase tendency in the heavy trafﬁc condition indicates the difﬁculty of overtaking.

6.2.4 Sharp Braking Frequency

Figure 12 Sharp braking frequency under the condition of different occupancies (3 & 4 lanes)

There also exists a peak value in the sharp braking frequency curve. In the case of light trafﬁc, the average speed is high. Therefore, as occupancy increases, sharp braking situation increases. In the case of heavy trafﬁc, the average speed is low, so the frequency decreases correspondingly.

6.2.5 Shift Ratio

Shift ratio under the condition of different occupancies (3 & 4 lanes) Figure 13

In the low occupancy case, the ratio is high, probably because of the low car number. In the high occupancy case, the ratio approximately keeps unchanged.

6.2.6 Satisfaction

Satisfaction under the condition of different occupancies (3 & 4 lanes) Figure 14

As the occupancy increases, it takes longer for drivers to pass a certain distance, so their satisfaction decreases. Again, the curves coincide, which means there is little difference between 3-lane and 4-lane freeway in terms of satisfaction under the condition of the same occupancy.

6.2.7 Standard Deviation of Speed

Figure 15 Std. deviation of speed.png under the condition of different occupancies (3 & 4 lanes)

The shapes of the curves are similar to the speed curves and they are irrelevant to the lane number.

6.3 Maximum Speed Limit

We study the case in which the maximum speed limit of 4 cell/s (86.4km/h) and 5 cell/s (108km/h) and a case with no maximum speed limit.

6.3.1 Flow Rate and Average Speed

(a) Flow rate in light & heavy trafﬁc (different (b) Average speed in light & heavy trafﬁc (dif- maximum limit) ferent maximum limit)

Figure 16

Vehicles can move in a high speed in a light trafﬁc case, so the maximum speed limit must have a signiﬁcant inﬂuence on the ﬂow rate and speed. In a heavy trafﬁc case, however, vehicles averagely maintain a low speed, and few of them can reach the maximum speed limit, so it can hardly inﬂuence the average speed. However, a maximum speed limit can avoid sharp changes of following dis- tance, which is beneﬁcial to the whole trafﬁc ﬂow. Therefore, a proper speed limit might result in a higher ﬂow rate. We can clearly see that the results meet our expectations from the Figure 16.

6.3.2 Sharp Braking Frequency and Shift Ratio

(a) Sharp braking frequency in light & heavy (b) Shift ratio in light & heavy trafﬁc (different trafﬁc (different maximum limit) maximum limit)

Figure 17

sharp braking frequency and shift ratio in a light trafﬁc case, which is beneﬁcial to safety. Nevertheless, it has little impact in a heavy trafﬁc case.

6.3.3 Lane Utilization Ratio

(a) Lane utilization ratio in light trafﬁc (differ- (b) Lane utilization ratio in heavy trafﬁc (differ- ent maximum limit) ent maximum limit)

Figure 18 From Figure 18, we can conclude that the utilization ratio of the leftmost lane in a light trafﬁc case decreases under a more strict speed limit because the limit reduces driver’s willingness to overtake.

6.4 Minimum speed limit

We study the inﬂuence of minimum speed limit by presenting two cases: a case with a minimum speed limit of 3 cell/s (64.8 km/h). By minimum speed limit we mean that vehicles will not exceed the limit due to randomization. However, they can decelerate due to safety consideration.

6.4.1 Flow Rate and Average Speed

(a) Flow rate in light & heavy trafﬁc (different (b) Average speed in light & heavy trafﬁc (dif- minimum limit) ferent minimum limit)

Figure 19

Opposite from the maximum speed limit case, the minimum speed limit plays an important role in a heavy trafﬁc case and it is of little importance in a light trafﬁc case. We can clearly conclude that from Figure 19

6.4.2 Sharp Braking Frequency and Shift Ratio

(a) Sharp braking frequency in light & heavy (b) Shift ratio in light & heavy trafﬁc (different trafﬁc (different minimum limit) minimum limit)

Figure 20

In the light trafﬁc case, vehicles cannot slow down in advance due to the speed limit, which in turn increase the sharp braking frequency. In the heavy trafﬁc case, the frequency decreases. The reason might lies in the low shift ratio and the ﬂuent trafﬁc ﬂow. The condition for lane changing is difﬁcult to satisfy. Figure 20 illustrates this conclusion.

6.4.3 Lane Utilization Ratio

(a) Lane utilization ratio in light trafﬁc (differ- (b) Lane utilization ratio in heavy trafﬁc (differ- ent minimum limit) ent minimum limit)

Figure 21 In the light trafﬁc case, the ratio is of little inﬂuence. In the heavy trafﬁc case, the ratio tends to evenly distribute between the three lanes due to the difﬁculty to change lane. The results are shown in Figure 21.

6.5 Signal Before Shifting

In real life, it is a rule to signal before changing lane. We try to add this factor into our model. We assume that a driver must signal ﬁrst if the lane-changing conditions are satisﬁed. Then the related vehicle might decelerate to give way to the driver. Then the driver can change the lane in the next time step. We compare the cases with and without this signal mechanism.

6.5.1 Flow Rate and Average Speed

(a) Flow rate in light & heavy trafﬁc (with or (b) Average speed in light & heavy trafﬁc (with without signaling) or without signaling)

Figure 22

When signaling is considered, acceleration will be constrained, which will re- duce the ﬂow rate and the speed of the trafﬁc ﬂow. Figure 22 illustrates this change.

6.5.2 Sharp Braking Frequency and Shift Ratio

(a) Sharp braking frequency in light & heavy (b) Shift ratio in light & heavy trafﬁc (with or trafﬁc (with or without signaling) without signaling)

Figure 23

Because vehicles’ giving-way behavior, the shift ratio increases and vehicles have to respond to the signal behavior, which will increase sharp braking fre- quency and shift ratio. Figure 23 demonstrates this statement.

6.6 Conclusions

Based on the results, we can conclude that:

• The number of lanes is not an inﬂuential factor under any circumstances.

• The maximum speed limit plays a signiﬁcant role in light trafﬁc while it is of no importance in heavy trafﬁc.

• The minimum speed limit plays a signiﬁcant role in heavy trafﬁc while it is of no importance in light trafﬁc.

• Signaling behavior reduce ﬂow rate and average while enhancing safety.

7 Results: the Optimal Rule

We examine ﬁve basic rules and design four improved rules. In order to deter- mine the performance of the rules, we implement a fuzzy synthetic evaluation to consider all the criteria.

7.1 Basic Rules of Overtaking

We take a three-lane freeway as an example to state the rules, similar rules for other kind of freeway can be easily derived from these rules. Apart from the keep-right-except-to-pass rule, another four basic rules are presented as follows:

• The free-overtaking rule: Drivers can overtake or change lane as they wish. In other words, there is no rule for overtaking.

• The no-overtaking rule: It restricts the vehicles in their own lane. The ve- hicles randomly move into the freeway and once they are moving on the freeway, they must stick to their current lane. This rule can be implement- ed by replacing the dashed lines separating lanes with full lines. This lane marking bans drivers from changing lanes.

• The different-speed-limit-on-each-lane rule:the maximum speed limit on the rightmost lane is the lowest. The maximum speed limit on the leftmost lane is the highest. The maximum speed limit on the middle lane is in the middle. This rule can be implemented by hanging corresponding speed limit sign over each lane, which will indicate the drivers to control their speeds.

• The complete-assigned-lane rule: Cars are assigned to the leftmost lane.

Buses are assigned to the middle lane. Trucks are assigned to the rightmost lane. No vehicles can change lanes after it moves into the freeway. This rule can be implemented by hanging the corresponding guide sign over each lane.

7.2 Criteria and Single Criterion Analysis for Basic Rules

We adopt ﬂow rate and average speed as criteria for the quality of trafﬁc ﬂow and we use sharp braking frequency as a criterion for safety. Moreover, we use satisfaction and standard deviation of speed as criteria for people’s experience of the trip. We analyze the ﬁve basic rules with every single criterion to see their performance in both light and heavy trafﬁc.

7.2.1 Trafﬁc Flow Criteria: Flow Rate and Speed

(a) Flow rate in light & heavy trafﬁc (different (b) Average speed in light & heavy trafﬁc (dif- rules) ferent rules)

Figure 24

We can see that the speed is coherent with the ﬂow rate. In the light trafﬁc case, the no-overtaking rule performs the worst because the road resources cannot be fully used. There is no signiﬁcant difference between other rules.

In the heavy trafﬁc case, the complete-assigned-lane rule behaves the worst. In the simulation, the leftmost lane, which is assigned to cars, suffers bad conges- tion while the other two lanes are relatively available. The different-speed-limit- on-each-lane rule performs the best. The rule bans large vehicles from entering the passing lanes as well as prevents a large number of cars from entering the rightmost lane.

7.2.2 Safety Criterion: Sharp Braking Frequency

Sharp braking frequency in light & heavy trafﬁc (different rules) Figure 25

Higher sharp braking frequency indicates a higher risk of accidents in reality. The results are presented in Figure 25.

In the light trafﬁc case, the no-overtaking rule performs the worst because ve- hicles of high speeds can only press the brake instead of changing lane if they encounters slow vehicles ahead. The well-performed rules are the keep-right- except-to-pass rule and the complete-assigned-lane rule. The latter bans over- taking too, but the speed is relatively even, so the sharp braking situation seldom occurs.

In the heavy trafﬁc case, the free-overtaking rule performs the worst. The different- speed-limit-on-each-lane rule performs the best because the rule can reasonably allocate the vehicles to three lanes by speed. Thus, the trafﬁc can ﬂow ﬂuently.

7.2.3 Experience Criterion: Satisfaction and Standard Deviation of Speed

(a) Satisfaction & heavy trafﬁc (different rules) (b) Std. deviation of speed in light & heavy traf- ﬁc (different rules)

Figure 26

Figure 26(a) describes satisfaction and it is coherent with the speed Figure 24(a). This coherence indicates that people feel more satisﬁed with higher speed.

Figure 26(b) compares the standard deviation of different rules. In the light trafﬁc, different-speed-limit-on-each-lane performs the best. Other rules’ per- formance are almost the same. In the heavy trafﬁc, the complete-assigned-lane rule obtains the minimum value, but this is because of low speed. In this case, the criterion cannot accurately indicate people’s experience.

7.3 Fuzzy Synthetic Evaluation for Basic Rules

The main challenge of the judging process is that we can obtain different results using different criteria. If we want to obtain a unique answer, we have to com- bine criteria to get a new, unique criterion. The relative importance of the crite- ria is hard to determine. Since we have no other information, we implement a fuzzy synthetic evaluation (FSE).[11] FSE is a multiple-criteria-decision-making method. It can determine the weights of each criterion based on the data only. One way to determine the weights is the coefﬁcient of variation method. If crite- rion can differentiate the rules evaluated, the method will assign a large weight to the criterion. We use this technique to analyze the performance of each rule.

In the following subsections, we use the light trafﬁc as a case to introduce the process of FSE. The case of heavy trafﬁc can be processed in a similar way.

7.3.1 Identify Alternatives and Attributes

In our problem, the alternatives are the ﬁve basic rules and the attributes are the ﬁve criteria. The values of each attributes of each alternative are listed as follows:

Table 4 Criteria of Basic Rules in Light Trafﬁc sharp breaking std. deviation ﬂow rate average speed satisfaction frequency of speed

keep-right-except- 0.964 4.552 0.041 0.841 1.152 to-pass free-overtaking 0.077 1.357 0.928 4.201 0.785 no-overtaking 0.631 2.800 0.091 0.531 1.415 different-speed- 0.063 0.813 0.845 4.129 0.777 limit-on-each-lane complete-assigned- 0.033 1.481 0.932 4.256 0.808 lane

Then we derive the ideal alternative from Table ??.

u = (u0 1, u0 2, u0 3, u0 4, u0 5) = (0.964, 4.552, 0.033, 0.841, 0.813)

7.3.2 Determine Fuzzy Evaluation Matrix

The membership function is deﬁned as

|aij −u0 i | rij = max{aij} −min{aij}

Then we have the fuzzy evaluation matrix

  0.000 0.000 0.127 0.000 0.508 0.108 0.201 0.750 0.180 0.814   1.000 1.000 1.000 1.000 0.901 R = 0.357 0.242 0.504 0.205 0.000 0.096 0.169 0.000 0.104 1.000 Using coefﬁcient of variation method, we deﬁne vj and wj as:

vj = sj vj , wj = P5 xj i=j vj

Then we calculate the weighted vector

w = (0.243, 0.226, 0.164, 0.251, 0.117)

7.3.3 Aggregate using a fuzzy operator

Then we use a fuzzy operator to aggregate and obtain the relative deviation.

5 X Fi = wjrij j=1

The relative deviation measures the distance between a speciﬁc alternative to the ideal alternative. The lower the value is, the better the alternative is.

7.3.4 The Results

The relative deviation in both cases are listed below

Table 5 Relative deviations of different rules in light trafﬁc keep-right- different-speed- complete- free-overtaking no-overtaking except-to-pass limit-on-each-lane assigned-lane

Fi 0.080 0.335 0.998 0.275 0.205

Table 6 Relative deviations of different rules in heavy trafﬁc keep-right- different-speed- complete- free-overtaking no-overtaking except-to-pass limit-on-each-lane assigned-lane

Fi 0.564 0.156 0.669 0.570 0.627

In the light trafﬁc case, the keep-right-except-to-pass rule has an absolute advan- tage over other rules while in the heavy trafﬁc case, the different-speed-limit-on- each-lane rule is the best.

7.4 Improved Rules of Overtaking

Based on the basic rules, we propose four improved rules by modifying or com- bining the ﬁve basic rules. When creating the rules, we consider not only the implementation of the rules but the overall quality of trafﬁc ﬂow, safety and experience as well.

• The partial-assigned-lane rule: cars are assigned to the middle lane and the leftmost lane with the permission to change between these two lanes.

Buses and trucks are assigned to the rightmost lane and they are banned from changing lanes. This rule can be implemented by hanging the cor- responding guide sign over each lane. We present this rule because cars account for 60% of the total vehicles and they have relatively high speed.

• The truck-on-rightmost-lane-only rule: It requires trucks to stick to the rightmost lane while cars and buses can change between the three lanes.

This rule can be implemented by hanging the corresponding guide sign over each lane. We present this rule because trucks have the lowest speed and they may constrain the speed of others if they appear on the passing lane.

• The minimum-speed-on-leftmost-lane rule: It sets a special minimum speed for the leftmost lane. This rule can be implemented by hanging the special speed limit sign over each lane. We hope it will help increase the efﬁciency of the leftmost passing lane.

• The partial-assigned-lane-and-keep-right rule: We combine the partial- assigned-lane rule and the keep-right-except-to-pass rule to make this rule.

In other words, vehicles are assigned by the partial-assigned-lane rule and cars overtakes by the keep-right-except-to-pass rule. We hope this rule can have the merits of previous two rules.

7.5 Fuzzy Synthetic Evaluation for All Rules

To test the performance of the improved rules, we apply a fuzzy synthetic eval- uation to all rules.

7.6 Conclusions

We can make two conclusions from the results:

Relative deviations of different rules in light & heavy trafﬁc Table 7 light trafﬁc heavy trafﬁc overall

keep-right-except-to-pass 0.141 0.519 0.269 free-overtaking 0.367 0.518 0.418 no-overtaking 0.991 0.576 0.851 different-speed-limit-on-each-lane 0.326 0.116 0.255 complete-assigned-lane 0.255 0.708 0.408 partial-assigned-lane 0.055 0.563 0.227 trucks-on-rightmost-lane-only 0.170 0.527 0.291 minimum-speed-on-leftmost-lane 0.233 0.320 0.262 partial-assigned-lane-and-keep-right 0.000 0.562 0.190

• The partial-assigned-lane-and-keep-right rule is the best in a light trafﬁc situation.

• The different-speed-limit-on-each-lane rule is the best in a heavy trafﬁc situation.

Based on the conclusions, we suggest that the different-speed-limit-on-each-lane rule should be used during the rush hour while the partial-assigned-lane-and- keep-right rule should be used at other times.

8 Sensitivity Analysis

Some inputs of our model may be hard to obtain or there might be some un- certainty in our inputs. Both these kinds of deviation might inﬂuence the result of our model. To test the robustness of our model, we implement a sensitivity analysis. We test our model in both light trafﬁc and heavy trafﬁc case. The anal- ysis proves that our model does not demonstrate a chaotic behavior, showing a good sensitivity.

8.1 Percentages of Vehicles

We obtain this data from a freeway company.[9] Although the data are accurate- ly collected, the percentages of vehicles may vary on different freeways. There- fore, we change the percentage of large vehicles(40%) by up to 15% to obtain the changes in our criteria.(Table 8 and Table 9) We observe a 16.61% increase in sharp braking frequency in the light trafﬁc case. The other criteria changes little.

In the heavy trafﬁc case, all criteria changes little. This indicates that our model can be used on freeways with varying percentages of vehicles.

Table 8 Sensitivity analysis—percentages of vehicles(light trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

16.6% 6.4% -15% 0.0% -5.9% -3.5% -10% 0.8% -0.4% 6.3% -0.6% 1.0% -5% -2.6% -2.8% 13.8% -2.5% 6.6% 0.0% 0.0% 0% 0.0% 0.0% 0.0% 5% -1.2% 0.6% 0.6% -0.1% 1.0% 10% -3.8% -2.3% 0.2% -0.1% -1.7% -5.5% -3.4% 15% -3.7% 0.3% 0.9%

Table 9 Sensitivity analysis—percentages of vehicles(heavy trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

-15% 0.1% -6.2% -2.5% -6.3% -3.4% -10% -1.3% -4.4% -3.2% -5.0% -0.8% -1.3% 0.4% -5% 4.8% -0.8% -1.5% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% 7.0% 2.6% -0.4% 2.0% 2.1% 0.1% 1.4% 10% 6.1% 3.6% 4.6% 15% 6.9% 4.4% 0.3% 5.8% 2.5%

8.2 Probability of Randomization

The probability of randomization pslow describes the random deceleration be- havior of drivers. Obviously, this parameter is difﬁcult to obtain and it may change severely under different circumstances. In our approach, we assume it to be 0.2 since very few data on this matter are available. We change it by up to 15% and the sharp braking frequency shows a 15.75% deviation, which is ac- ceptable.(Table 10 and Table 11) Table 10 Sensitivity analysis—probability of randomization(light trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

-15% 3.4% 0.2% -1.4% 0.4% 0.3% -10% 0.3% 0.6% 0.4% 0.0% 1.4% -5% 1.6% -1.8% 2.9% -0.7% 1.8% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% 4.7% 2.3% -4.7% 0.9% -1.4% 10% 0.8% -2.0% 3.2% -0.8% 0.0% 15% -4.6% -4.9% 15.7% -3.3% 6.5%

Table 11 Sensitivity analysis—probability of randomization(heavy trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

-15% 7.3% 6.0% 3.6% 5.4% 0.4% -10% 4.7% 3.1% 0.9% 3.0% 2.8% -5% 3.6% 1.0% -0.4% 1.2% 0.7% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% -4.4% -1.1% -3.4% -2.1% 2.4% 10% -3.0% -2.8% -3.1% -3.6% 0.9% 15% -1.6% -4.1% -4.7% -4.4% 0.8%

8.3 Probability of Willing to Change Lane

We consider the case that a driver might choose not to change lane even if all the other conditions are satisﬁed. Obviously, the data are hard to get and it may suf- fer from a severe change during a short period of time. We assume probability of willing to change to the left lane and right lane are 0.5 and 0.7 respectively in our model. Therefore, we change the probabilities by up to 15% proportionally. The maximum deviation is 7.05%, which indicates a good robustness.

Table 12 Sensitivity analysis—probability of willing to change lane(light trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

-15% 1.9% -0.4% 4.5% -0.8% 2.4% -10% -3.9% -1.5% 6.7% -1.5% 4.5% -5% 0.4% -1.6% 4.1% -0.7% 1.1% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% 1.9% 0.5% 0.0% 0.1% 0.0% 10% -7.1% -4.7% 6.6% -3.2% 5.5% 15% -2.7% -2.4% 4.2% -1.1% 1.7%

Table 13 Sensitivity analysis—probability of willing to change lane(heavy trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

-15% 1.8% 0.7% 0.0% -0.4% 1.4% -10% 3.5% 0.5% -0.9% 0.1% 1.1% -5% 2.6% -0.2% -1.4% -1.1% 1.9% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% 3.8% 0.8% -1.6% -0.1% 2.2% 10% 3.9% 0.6% -1.0% -0.5% 1.8% 15% -2.2% -0.5% -2.2% -0.3% 1.1%

9 Further Discussions

9.1 Modiﬁcations for Countries Where Driving on the Left Is the Norm

Imagine there is a mirror standing in the middle of a two-way freeway in a country where driving on the right is the norm. What’s happening in the mirror is similar to a freeway in a country where driving on the left is the norm. The “passing lane” is on the right. The drivers are sitting in the right side of their cars. The cars obeys the keep-left-except-to-pass rule. All the roads, vehicles and rules look like that in a country where driving on the left is the rule.

However, there is one difference which is human beings. A left-handed person is always a left handed person, but in the “mirror world”, he becomes a right- handed person and vice versa. This thought inspires us that we can modify our model to reﬂect this difference instead of simply changing the orientation. We assume in our model that the probability of willing to change to the left lane and right lane are 0.5 and 0.7 and this tendency do not change under any circumstances. Therefore, in a country like Great Britain, drivers still maintain this tendency, which means drivers have a higher tendency to move to the right lane – the passing lane. This is exactly the same as the case that we swap the two probabilities in our original model.

Based on the discussions above, we modify our model and run a simulation.(tableand table. ) We observe a maximum change of 4.6% in our criteria. From this analy- sis, we can safely conclude that

• Simply changing the orientation is reasonable if the willingness of chang- ing to the left lane equals the willingness of changing to the right lane.

• Even if the two values are different, the deviations are small enough to ignore.

9.2 Modiﬁcations for An Intelligent System

An intelligent system can fully control all the vehicles and let them strictly obey the rule, The keep-right-except-to-pass rule states that the vehicles must drive in the rightmost lane unless they are passing another vehicle, which means the vehicles MUST change to the right lane if the conditions are satisﬁed. In other words, the probability of willing to change to the right lane equals to 1. Based on this characteristic, we propose two intelligent systems:

• The semi-intelligent system: this system forces vehicles to change to the right lane if the conditions are satisﬁed, while whether to change to the left lane relies upon human judgment.

• The complete intelligent system: this system not only forces vehicles to change to the right lane if the conditions are satisﬁed, but also forces vehi- cles to change to the left lane if the corresponding conditions are satisﬁed.

We run the simulation to examine the performance of the intelligent systems.

9.2.1 Flow Rate and Average Speed

(a) Flow rate in light & heavy trafﬁc (with or (b) Average speed in light & heavy trafﬁc (with without intelligent system) or without intelligent system)

Figure 27

In the light trafﬁc case, the ﬂow rate of complete intelligent system increases s- lightly, while that of semi-intelligent system decreases slightly compared with the situation without intelligent system. The little impact is due to rich pass- ing lane resources. In the heavy trafﬁc case, the ﬂow rates of intelligent sys- tems increase. This is because forcing vehicles to move back to the rightmost lane release more passing lane resources. This is consistent with the speed ﬁg- ure.(Figure 27)

9.2.2 Sharp Braking Frequency and Shift Ratio

In the light trafﬁc case, the shift ratio and sharp braking frequency change slight- ly. In the heavy trafﬁc case, the shift ratio increases signiﬁcantly as expected. The intelligent system will certainly increase shift ratio. (Figure 28) (a) Sharp braking frequency in light & heavy (b) Shift ratio in light & heavy trafﬁc (with or trafﬁc (with or without intelligent system) without intelligent system)

Figure 28

In the light trafﬁc case, the sharp braking frequency decreases greatly if a com- plete intelligent system is implemented. It is because if a driver is about to be constrained by the vehicle ahead, he can change to the left lane in time to avoid a sharp braking.

9.2.3 Lane Utilization Ratio

(a) Lane utilization ratio of each lane in light (b) Lane utilization ratio of each lane in heavy trafﬁc (with or without intelligent system) trafﬁc (with or without intelligent system)

Figure 29 For a semi-intelligent system, the vehicles tend to move to the left lane. For a complete intelligent system, the vehicles tend to move to the right lane. Both the light trafﬁc case and the heavy trafﬁc case have this tendency. The overall changes are relatively small.

9.3 Additional Research on the Reﬁned Model with Ramps

In section 5.3, we present a reﬁned model taking ramps into account. Due to open boundary conditions, we use λ to control the occupancy, which determines whether the trafﬁc is heavy or light. Then we vary the value of pexit to study the model. In the simulation, we have some interesting ﬁndings.

9.3.1 Flow Rate

Flow rate in light & heavy trafﬁc (different pexit) Figure 30

The probability to exit from ramp pexit has little, if any, impact on ﬂow rate, partly because we equate the numbers of vehicles entering from the on-ramp with the numbers of vehicles exiting through the off-ramp.

9.3.2 Average Speed

Average speed in light & heavy trafﬁc (different pexit) Figure 31

In the previous analysis, the average speed is always consistent with ﬂow rate. Adding ramps, however, breaks this consistency, especially in the heavy trafﬁc case. As pexit increases, a large number of vehicles need to exit through the off- ramp. They will decelerate in advance, which causes low average speed.

9.3.3 Lane Utilization Ratio

(a) Lane utilization ratio of each lane in light (b) Lane utilization ratio of each lane in heavy trafﬁc (different pexit) trafﬁc (different pexit)

Figure 32 In the heavy trafﬁc case, pexit will increase the utilization ratio of the rightmost lane. This reasonable because a large number of vehicles tend to use the right- most lane to move into the off-ramp.

9.3.4 Failure Ratio

A signiﬁcant difference in our reﬁned model is that some vehicles might fail to move to the exit of the freeway, a common situation in the real world. The failure ratio is deﬁned as the ratio of the number of the vehicles failing to exit to the total number of vehicles. We seek to investigate how failure rate changes with varying pexit.

Failure ratio in light & heavy trafﬁc (different pexit) Figure 33

The vehicles can move to the rightmost lane with ease. pexit plays an impor- tant role in the heavy trafﬁc case. When pexit remains low, the average speed is relatively high, which makes moving to the rightmost lane extremely difﬁcult. When pexit becomes high, the average speed slows down. Vehicles have more time to move to the rightmost lane, which in turn reduces the failure ratio.

10 Strengths and Weaknesses

10.1 Strengths

• Our models are fairly robust to the changes in parameters based on sen- sitivity analysis. It means a slight change in parameters will not cause a signiﬁcant change in the result.

• Different types of vehicles are taken into consideration, and the mixing ra- tio is based on actual data. We consider the length of vehicles and different maximum speeds which makes the model closer to reality.

• We come up with various criteria to compare different situations. Hence an overall comparison can be made based on these criteria.

• Our models are capable of simulating the situation in real life. The results also agree with common sense and life experience.

• A reﬁned model is established to consider the role of ramps, which is a bright spot of our model.

10.2 Weaknesses

• Factors of human judgments may be over-simpliﬁed. In order to consider that a driver may randomly decelerate and not choose to overtake when possible, we simply deﬁned a possibility respectively. Actual situation may be more complicated.

• Some of the parameters are based on semi-educated guess because few data are available. However, based on our sensitivity analysis, they will not make a great difference if slightly changed.

• We did not consider the prediction of each driver. In our model, drivers change their speed only based on the information of the previous time step. But in fact, they can make a prediction and choose their speed in a more complicated way.
