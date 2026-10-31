# P-B-2014-26333-27e7d8ab

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
26333

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000005 | title | pages [1] -->
A

<!-- b000006 | heading | pages [1] -->
2014 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000007 | front_matter | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000008 | heading | pages [1] -->
Abstract

<!-- b000009 | prose | pages [1] -->
Our goal is a model that can evaluate the performance of the keep-right-except- to-pass rule and other alternatives by simulating the trafﬁc ﬂow on the freeway. We construct models to analyze ﬁve inﬂuencing factors. Then we integrate multi- ple criteria to judge the performance of nine rules using a fuzzy synthetic evalua- tion(FSE).

<!-- b000010 | prose | pages [1] -->
Our basic lane-changing model focuses on the behavior of a speciﬁc vehicle on the freeway. We carefully examine the vehicle ˛a´rs lane-changing behavior, an essential component of overtaking.

<!-- b000011 | prose | pages [1] -->
We extend our model with a cellular-automaton-based approach. We assume that the drivers will change the lane with a probability if the trigger and safety con- ditions are satisﬁed. Using periodic boundary conditions, we seek to simulate a section of a long freeway, which is hardly inﬂuenced by real boundary condition- s. In addition, we can accurately control the occupancy of the freeway. We can simulate the trafﬁc ﬂow under several conditions by varying the number of lanes, maximum speed limit, minimum speed limit and signaling behavior.

<!-- b000012 | prose | pages [1] -->
Four other basic rules such as free-overtaking rule are examined by revising the laws governing the cells in the cellular automaton. Then we design ﬁve improved rules based on the basic rules attempting to obtain an optimal rule.

<!-- b000013 | prose | pages [1] -->
We choose ﬂow rate, average speed as trafﬁc ﬂow criteria, sharp braking fre- quency as a safety criterion and satisfaction and standard deviation of speed as ex- perience criteria. Then we use a fuzzy synthetic evaluation technique to integrate these criteria to determine the performance of each rule. We ﬁnd that in a light trafﬁc case, a partial-assigned-lane-and-keep-right rule performs the best while in a heavy trafﬁc situation, a different-speed-limit-on-each-lane rule is preferred.

<!-- b000014 | prose | pages [1] -->
We change the probability of lane-changing to adjust our model to a country like Great Britain. Moreover, we change that parameter to simulate a freeway fully controlled by an intelligent system and observe small deviations.

<!-- b000015 | prose | pages [1] -->
Additionally, we reﬁne our extended model considering the ramps. We adopt open boundary conditions and assume that the vehicles ﬂowing in are Poisson- distributed. Finally, we change parameters to analyze freeways with ramps under different conditions.

<!-- b000016 | title | pages [2] -->
Keep Right to Keep “Right”

<!-- b000017 | furniture | pages [2] -->
Team #26333

<!-- b000018 | prose | pages [2] -->
February 10, 2014

<!-- b000019 | heading | pages [2] -->
Abstract

<!-- b000020 | prose | pages [2] -->
Our goal is a model that can evaluate the performance of the keep-right- except-to-pass rule and other alternatives by simulating the trafﬁc ﬂow on the freeway. We construct models to analyze ﬁve inﬂuencing factors. Then we integrate multiple criteria to judge the performance of nine rules using a fuzzy synthetic evaluation(FSE).

<!-- b000021 | prose | pages [2] -->
Our basic lane-changing model focuses on the behavior of a speciﬁc ve- hicle on the freeway. We carefully examine the vehicles lane-changing be- havior, an essential component of overtaking.

<!-- b000022 | prose | pages [2] -->
We extend our model with a cellular-automaton-based approach. We assume that the drivers will change the lane with a probability if the trigger and safety conditions are satisﬁed. Using periodic boundary conditions, we seek to simulate a section of a long freeway, which is hardly inﬂuenced by real boundary conditions. In addition, we can accurately control the occu- pancy of the freeway. We can simulate the trafﬁc ﬂow under several con- ditions by varying the number of lanes, maximum speed limit, minimum speed limit and signaling behavior.

<!-- b000023 | prose | pages [2] -->
Four other basic rules such as free-overtaking rule are examined by re- vising the laws governing the cells in the cellular automaton. Then we de- sign ﬁve improved rules based on the basic rules attempting to obtain an optimal rule.

<!-- b000024 | prose | pages [2] -->
We choose ﬂow rate, average speed as trafﬁc ﬂow criteria, sharp brak- ing frequency as a safety criterion and satisfaction and standard deviation of speed as experience criteria. Then we use a fuzzy synthetic evaluation technique to integrate these criteria to determine the performance of each rule. We ﬁnd that in a light trafﬁc case, a partial-assigned-lane-and-keep- right rule performs the best while in a heavy trafﬁc situation, a different- speed-limit-on-each-lane rule is preferred.

<!-- b000025 | prose | pages [2] -->
We change the probability of lane-changing to adjust our model to a country like Great Britain. Moreover, we change that parameter to simu- late a freeway fully controlled by an intelligent system and observe small deviations.

<!-- b000026 | prose | pages [2] -->
Additionally, we reﬁne our extended model considering the ramps. We adopt open boundary conditions and assume that the vehicles ﬂowing in

<!-- b000027 | prose | pages [2, 3] -->
1 are Poisson-distributed. Finally, we change parameters to analyze freeways with ramps under different conditions.

<!-- b000028 | furniture | pages [3] -->
Team # 26333

<!-- b000029 | furniture | pages [3] -->
Page 2 of 53

<!-- b000031 | furniture | pages [4] -->
Team # 26333

<!-- b000032 | furniture | pages [4] -->
Page 3 of 53

<!-- b000033 | heading | pages [4] -->
Contents

<!-- b000034 | contents | pages [4] -->
1

<!-- b000035 | contents | pages [4] -->
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [4] -->
5

<!-- b000037 | contents | pages [4] -->
1.1

<!-- b000038 | contents | pages [4] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [4] -->
5

<!-- b000040 | contents | pages [4] -->
1.2

<!-- b000041 | contents | pages [4] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [4] -->
6

<!-- b000043 | contents | pages [4] -->
2

<!-- b000044 | contents | pages [4] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [4] -->
6

<!-- b000046 | contents | pages [4] -->
3

<!-- b000047 | contents | pages [4] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [4] -->
7

<!-- b000049 | contents | pages [4] -->
4

<!-- b000050 | contents | pages [4] -->
Model Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [4] -->
9

<!-- b000052 | contents | pages [4] -->
5

<!-- b000053 | contents | pages [4] -->
The Keep-Right-Except-To-Pass Model . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [4] -->
9

<!-- b000055 | contents | pages [4] -->
5.1

<!-- b000056 | contents | pages [4] -->
The Basic Lane-changing Model . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [4] -->
9

<!-- b000058 | contents | pages [4] -->
5.2

<!-- b000059 | contents | pages [4] -->
The Extended “Ring Road” Model . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [4] -->
12

<!-- b000061 | contents | pages [4] -->
5.3

<!-- b000062 | contents | pages [4] -->
The Reﬁned Model with Ramps . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [4] -->
19

<!-- b000064 | contents | pages [4] -->
6

<!-- b000065 | contents | pages [4] -->
Results: Inﬂuencing Factors . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [4] -->
21

<!-- b000067 | contents | pages [4] -->
6.1

<!-- b000068 | contents | pages [4] -->
Variables and Criteria . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [4] -->
21

<!-- b000070 | contents | pages [4] -->
6.2

<!-- b000071 | contents | pages [4] -->
Number of Lanes . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [4] -->
23

<!-- b000073 | contents | pages [4] -->
6.3

<!-- b000074 | contents | pages [4] -->
Maximum Speed Limit . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [4] -->
28

<!-- b000076 | contents | pages [4] -->
6.4

<!-- b000077 | contents | pages [4] -->
Minimum speed limit . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [4] -->
31

<!-- b000079 | contents | pages [4] -->
6.5

<!-- b000080 | contents | pages [4] -->
Signal Before Shifting . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [4] -->
33

<!-- b000082 | contents | pages [4] -->
6.6

<!-- b000083 | contents | pages [4] -->
Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [4] -->
34

<!-- b000085 | contents | pages [4] -->
7

<!-- b000086 | contents | pages [4] -->
Results: the Optimal Rule . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [4] -->
35

<!-- b000088 | contents | pages [4] -->
7.1

<!-- b000089 | contents | pages [4] -->
Basic Rules of Overtaking . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [4] -->
35

<!-- b000091 | contents | pages [4] -->
7.2

<!-- b000092 | contents | pages [4] -->
Criteria and Single Criterion Analysis for Basic Rules . . . . . . .

<!-- b000093 | contents | pages [4] -->
35

<!-- b000094 | contents | pages [4] -->
7.3

<!-- b000095 | contents | pages [4] -->
Fuzzy Synthetic Evaluation for Basic Rules . . . . . . . . . . . . .

<!-- b000096 | contents | pages [4] -->
38

<!-- b000097 | contents | pages [4] -->
7.4

<!-- b000098 | contents | pages [4] -->
Improved Rules of Overtaking

<!-- b000099 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [4] -->
41

<!-- b000101 | contents | pages [4] -->
7.5

<!-- b000102 | contents | pages [4] -->
Fuzzy Synthetic Evaluation for All Rules

<!-- b000103 | contents | pages [4] -->
. . . . . . . . . . . . . .

<!-- b000104 | contents | pages [4] -->
41

<!-- b000105 | contents | pages [4] -->
7.6

<!-- b000106 | contents | pages [4] -->
Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [4] -->
41

<!-- b000108 | contents | pages [4] -->
8 Sensitivity Analysis

<!-- b000109 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [4] -->
42

<!-- b000111 | contents | pages [4] -->
8.1

<!-- b000112 | contents | pages [4] -->
Percentages of Vehicles . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [4] -->
42

<!-- b000114 | contents | pages [4] -->
8.2

<!-- b000115 | contents | pages [4] -->
Probability of Randomization . . . . . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [4] -->
43

<!-- b000117 | contents | pages [4] -->
8.3

<!-- b000118 | contents | pages [4] -->
Probability of Willing to Change Lane . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [4] -->
44

<!-- b000120 | contents | pages [4] -->
9 Further Discussions

<!-- b000121 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000122 | contents | pages [4] -->
45

<!-- b000123 | contents | pages [4] -->
9.1

<!-- b000124 | contents | pages [4] -->
Modiﬁcations for Countries Where Driving on the Left Is the Norm 45

<!-- b000125 | contents | pages [4] -->
9.2

<!-- b000126 | contents | pages [4] -->
Modiﬁcations for An Intelligent System . . . . . . . . . . . . . . .

<!-- b000127 | contents | pages [4] -->
46

<!-- b000128 | contents | pages [4] -->
9.3

<!-- b000129 | contents | pages [4] -->
Additional Research on the Reﬁned Model with Ramps . . . . . .

<!-- b000130 | contents | pages [4] -->
49

<!-- b000131 | furniture | pages [5] -->
Team # 26333

<!-- b000132 | furniture | pages [5] -->
Page 4 of 53

<!-- b000133 | heading | pages [5] -->
10 Strengths and Weaknesses

<!-- b000134 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . 52 10.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 10.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

<!-- b000135 | furniture | pages [6] -->
Team # 26333

<!-- b000136 | furniture | pages [6] -->
Page 5 of 53

<!-- b000137 | heading | pages [6] -->
1 Introduction

<!-- b000138 | prose | pages [6] -->
A freeway is a highway designed for high-speed vehicles. It provides an unhin- dered ﬂow of trafﬁc with no trafﬁc lights or intersections.[1] Typically, a freeway has several advantages over common roads, such as the high speed and the high trafﬁc volume. The Keep-Right-Except-To-Pass rule, also known as “Slow- er Trafﬁc Keep Right”, is often employed in right-hand trafﬁc in order to raise the quality of trafﬁc ﬂow, especially the quality of trafﬁc ﬂow on freeways.[2] The effectiveness of the rule will not only increase utilization of freeways but also enhance driver satisfaction. Thus, it will be exhilarating if we can design another rule that can outperform the current rule. In this paper, we simulate different rules of overtaking and compare them so as to decide the optimal rule.

<!-- b000139 | heading | pages [6] -->
1.1 Restatement of the Problem

<!-- b000140 | prose | pages [6] -->
We are required to build a mathematical model to analyze the performance of the keep-right-except-to-pass rule the other alternatives. We decompose the problem into two sub-problems:

<!-- b000141 | prose | pages [6] -->
• Build a model that can simulate the overtaking process.

<!-- b000142 | prose | pages [6] -->
• Propose a mathematical criterion to determine the performance of a spe- ciﬁc rule.

<!-- b000143 | prose | pages [6] -->
In the ﬁrst step, we seek to build a model with the inputs of speed limits and other factors. Most importantly, the model should reﬂect the mechanism of the given rule. Then we can change the inputs to do several simulations. Also, we can change the mechanism to apply alternative rules to our model. Finally, we can obtain the outputs of our model.

<!-- b000144 | prose | pages [6] -->
In the second step, we seek to use the outputs of our model to propose a math- ematical criterion to evaluate different rules. We will consider the trade-off be- tween trafﬁc ﬂow, safety and other factors. We will design other rules and de- termine which rule is the best.

<!-- b000145 | prose | pages [6] -->
Then we attempt to adjust our model and apply it to countries like Great Britain. We also consider the inﬂuence of intelligent system.

<!-- b000146 | furniture | pages [7] -->
Team # 26333

<!-- b000147 | furniture | pages [7] -->
Page 6 of 53

<!-- b000148 | heading | pages [7] -->
1.2 Literature Review

<!-- b000149 | prose | pages [7] -->
A model for the simulation of freeway trafﬁc is inevitable to the study of the performance of the rule. German physicists Nagel and Schreckenberg built a theoretical model for the simulation of freeway trafﬁc, which is a simple cellular automaton model for road trafﬁc ﬂow known as “N-S model”.[3] They deﬁned a one-dimensional lane with two kinds of boundary conditions-open or periodic boundary conditions: In their model, each site may either be occupied by one vehicle or it may be empty. Each vehicle has an integer velocity with values between zero and vmax. During each time step, four sub-steps are performed: acceleration, slowing down, randomization and car motion.

<!-- b000150 | prose | pages [7] -->
After the single-lane model was established, several scientists were devoted to building a multi-lane model. The main difﬁculty was to set up the rules for shifting to the neighboring lane. Rickert et al. introduced a two-lane model with two parallel lanes in their article.[4] Several conditions have to be fulﬁlled before the vehicle changing to other lanes: (1) another vehicle is in the way (2) other lanes are better and (3) collision will not happen. They also simulated the model using a cellular automaton, and the results were quite reasonable.

<!-- b000151 | prose | pages [7] -->
As a matter of fact, a multi-lane model does not have to be symmetric. Differ- ence may include different speed limits on each lane, different kinds of cars, etc. In 1997, Chowdhury et al. ﬁrst simulated the model with different kinds of ve- hicles. [5] In their model, different maximum possible speeds are introduced to different kinds of vehicles. The result shows that even if the portion of “slow cars” is relatively low, “fast cars” can only move in a low speed.

<!-- b000152 | prose | pages [7] -->
Further studies are carried out based on the comparison between model and reality. Knospe, Santen suggested that the inﬂuence of “slow cars” might have been over-estimated.[6] They recommended to consider the impact of expectan- cy in the model.

<!-- b000153 | heading | pages [7] -->
2 Assumptions and Justiﬁcations

<!-- b000154 | prose | pages [7] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justiﬁed.

<!-- b000155 | prose | pages [7] -->
• No pedestrian can affect the vehicles on freeways. Usually, pedestrians have no access to freeways, let alone going across the freeways.

<!-- b000156 | prose | pages [7] -->
• We ignore the force of crosswind to a vehicle when it is changing lanes.This impact is negligible compared with that of the head wind.

<!-- b000157 | furniture | pages [8] -->
Team # 26333

<!-- b000158 | furniture | pages [8] -->
Page 7 of 53

<!-- b000159 | prose | pages [8] -->
• Drivers cannot drive on the emergency lane. Typically, the emergency lane is not for use of ﬂowing trafﬁc. [7]

<!-- b000160 | prose | pages [8] -->
• In our model, we only consider the freeway as completely ﬂat, with no curve or slopes. This assumption greatly simplify our model and allow us to focus on the nature of overtaking.

<!-- b000161 | prose | pages [8] -->
• We assume that all drivers act based on the same set of rules. We clas- sify drivers as aggressive and non-aggressive and both groups follow the relevant rules.

<!-- b000162 | heading | pages [8] -->
3 Notations

<!-- b000163 | prose | pages [8] -->
All the variables and constants used in this paper are listed in Table 1 and Table 2.

<!-- b000164 | prose | pages [8] -->
Table 1 Symbol Table–Constants Symbol Deﬁnition Units

<!-- b000165 | prose | pages [8, 9] -->
Constants λ Expectancy of poisson-distribution unitless pslow Possibility that a vehicle slows down randomly unitless pleft Possibility that a vehicle shift to the left lane when possible unitless pright Possibility that a vehicle shift to the right lane when possible unitless pexit Possibility that a vehicle need to move off through the exit ramp unitless Table 2 Symbol Table–Variables Symbol Deﬁnition Units

<!-- b000166 | furniture | pages [9] -->
Team # 26333

<!-- b000167 | furniture | pages [9] -->
Page 8 of 53

<!-- b000169 | prose | pages [9] -->
Variables vs Speed of vehicles cell/time-step vexpect Expected speed of vehicles cell/time-step vlf Speed of the vehicle on the left lane ahead cell/time-step vlb Speed of the vehicle on the left lane behind cell/time-step vrf Speed of the vehicle on the right lane ahead cell/time-step vrb Speed of the vehicle on the right lane behind cell/time-step t Time time-step

<!-- b000170 | prose | pages [9] -->
Dl,f,gap Left front gap cell Dl,b,gap Left back gap cell Dr,f,gap Right front gap cell Dr,b,gap Right back gap cell vehiclei The jth vehicle on the ith lane unitless j vi Speed of vehiclei j (t) j at tth time-step cell/time-step vi Expcted speed of vehiclei cell/time-step j,expect j gapi Front gap of vehiclei j (t) j at tth time-step cell xi Location of vehiclei j (t) j at tth time-step cell lfgapi Left front gap of vehiclei cell j j lbgapi Left back gap of vehiclei cell j j rfgapi Right front gap of vehiclei cell j j rbgapi Right back gap of vehiclei cell j j lbvi Speed of the vehicle behind vehiclei j on the left lane cell/time-step j rbvi Speed of the vehicle behind vehiclei j on the right lane cell/time-step j

<!-- b000171 | prose | pages [9] -->
v (t) Average speed at tth time-step cell/time-step N The number of vehicles passing a certain point on the highway unitless N (t) The number of vehicles on the highway at tth time-step unitless Nj (t) The number of vehicles on the jth lane at tth time-step unitless Nshift (t) The number of vehicles changing lanes at tth time-step unitless texpect Expected time time-step tactual Actual time time-step

<!-- b000172 | prose | pages [9] -->
aij Value of the jth criterion of the ith rule uncertain u0 Value of the jth criterion of the ideal scheme uncertain j rij Relative deviation of the jth criterion of the ith rule unitless vj coefﬁcient of variation of the jth criterion unitless wj Weight of the jth criterion unitless Fi Relative deviation of the ith rule unitless

<!-- b000173 | furniture | pages [10] -->
Team # 26333

<!-- b000174 | furniture | pages [10] -->
Page 9 of 53

<!-- b000175 | heading | pages [10] -->
4 Model Overview

<!-- b000176 | prose | pages [10] -->
Most research for trafﬁc ﬂow can be classiﬁed as microscopic and macroscopic. As macroscopic methods are difﬁcult to apply to our problem, we approach the problem with microscopic techniques. Our study into the keep-right-except-to- pass rule takes several approaches.

<!-- b000177 | prose | pages [10] -->
Our basic model allows us to have a close look at the lane-changing behavior. We focus on the incentive of changing lane and the conditions for a successful lane changing. We treat the changing-to-the-left-lane behavior and changing-to- the-right-lane behavior differently. This model gives us some intuition about the rule and serves as a stepping stone to our later study.

<!-- b000178 | prose | pages [10] -->
The extended model views the problem from a wider perspective. We consider a section of freeway and divide it into lattices. Then we run a cellular automa- ton to simulate the behavior of vehicles. The essence of the model is the laws governing the cells. We derive the laws according to the analysis of our basic model. Moreover, using periodic boundary conditions, we treat the freeway as a “ring road” so as to accurately control the density. Thus, we call it a “Ring Road” model.

<!-- b000179 | prose | pages [10] -->
Our reﬁned model attempts to tackle a more realistic while more challenging problem. We add an entrance ramp and an exit ramp to our cellular automaton. The laws for the entering and exiting vehicles are also added. We use a Poisson distribution to simulate vehicles moving in from the start point.

<!-- b000180 | prose | pages [10] -->
We use the extended “Ring Road” model as a standard model to analyze the problem and all results have this model at their cores.

<!-- b000181 | heading | pages [10] -->
5 The Keep-Right-Except-To-Pass Model

<!-- b000182 | prose | pages [10] -->
We will start with the idea of the basic model. Then we present the cellular automaton and explain the algorithm. Finally, we introduce our additional work in the reﬁned model.

<!-- b000183 | heading | pages [10] -->
5.1 The Basic Lane-changing Model

<!-- b000184 | prose | pages [10, 11] -->
The basic model is a microscopic approach. A typical overtaking behavior con- sists of ﬁve actions: signal for three seconds, change lane, accelerate, signal back and change back to the former lane. Among these actions, lane-changing is the most crucial part. An analysis of lane-changing behavior might shed light on the nature of the quality of trafﬁc ﬂow.

<!-- b000185 | furniture | pages [11] -->
Team # 26333

<!-- b000186 | furniture | pages [11] -->
Page 10 of 53

<!-- b000188 | heading | pages [11] -->
5.1.1 Changing to the Left Lane

<!-- b000189 | prose | pages [11] -->
When making the decision of whether to overtake, the driver will ﬁrst decide whether to change to the left lane. There are two main considerations [8] :

<!-- b000190 | prose | pages [11] -->
• A reason or a trigger consideration

<!-- b000191 | prose | pages [11] -->
• A safety consideration

<!-- b000192 | prose | pages [11] -->
The former means that the vehicle ahead moves slowly enough, which will trig- ger the driver to overtake it. The latter indicates that he will take safety into account. In other words, if there is a high-speed vehicle driving on the left lane, he will choose to stay on the current lane to avoid collision. Based on these considerations, we can introduce some mathematical intuition into the problem.

<!-- b000193 | caption | pages [11] -->
Figure 1 illustrates the situation that the red car tends to change to the left lane.

<!-- b000194 | prose | pages [11] -->
Figure 1 Change-to-the-left-lane

<!-- b000195 | prose | pages [11] -->
Based on the trigger consideration, the speed of the cars satisﬁes

<!-- b000196 | prose | pages [11] -->
vexpect > vs

<!-- b000197 | prose | pages [11] -->
In terms of safety, the left back gap should satisfy

<!-- b000198 | prose | pages [11, 12] -->
Dl,b,gap > (vlb −vs)t Additionally, the red car attempts to accelerate. It is unreasonable if it changes to the passing lane while slowing down. This happens if there is a vehicle ahead. Therefore, the left front gap should satisfy

<!-- b000199 | furniture | pages [12] -->
Team # 26333

<!-- b000200 | furniture | pages [12] -->
Page 11 of 53

<!-- b000202 | prose | pages [12] -->
Dl,f,gap > (vs −vlf)t

<!-- b000203 | prose | pages [12] -->
The mathematical expressions above give the basic conditions of a change-to- the-left-lane behavior.

<!-- b000204 | heading | pages [12] -->
5.1.2 Changing Back to the Right Lane

<!-- b000205 | prose | pages [12] -->
After accelerating and passing the slow vehicle ahead, the driver tends to change back to the former lane due to the keep-right-except-to-pass rule. However, this lane-changing behavior will be subject to the following constraints:

<!-- b000206 | prose | pages [12] -->
• There is no incentive to pass the car in the current passing lane. If so, and if it is a multi-lane freeway, the driver would prefer to continue to overtake the car ahead and change to the left passing lane rather than change back to the former lane.

<!-- b000207 | prose | pages [12] -->
• It is safe to change back. This condition means that the driver should pass the slow car and ensure that he will not collide with the slow car when changing back.

<!-- b000208 | prose | pages [12] -->
• After changing back to the former lane, the driver can maintain his rela- tively high speed. Otherwise, he will intend to pass more than one car in an overtaking process.

<!-- b000209 | prose | pages [12] -->
The ﬁrst constraint can be treated as the changing-to-the-left-lane situation as mentioned above and the other conditions can be stated as the following math- ematical expressions.

<!-- b000210 | prose | pages [12] -->
Due to the safety consideration, the right back gap should yield

<!-- b000211 | prose | pages [12] -->
Dr,b,gap > (vrb −vs)t

<!-- b000212 | prose | pages [12] -->
Due to the intention to pass more cars, the right front gap should yield

<!-- b000213 | prose | pages [12, 13] -->
Dr,b,gap > (vs −vrf)t Figure 2 Change-back-to-the-right-lane

<!-- b000214 | caption | pages [12] -->
Figure 2 illustrates this change-back-to-the-right-lane situation.

<!-- b000215 | furniture | pages [13] -->
Team # 26333

<!-- b000216 | furniture | pages [13] -->
Page 12 of 53

<!-- b000218 | heading | pages [13] -->
5.2 The Extended “Ring Road” Model

<!-- b000219 | prose | pages [13] -->
In order to understand how the rule works in a trafﬁc ﬂow, we have to ana- lyze the behavior of vehicles in a relatively long way, which will be more like a freeway. One intuition for modeling the problem is to think of it as a stochas- tic process. Therefore, we use a cellular automaton to simulate the behavior of vehicles on a freeway.

<!-- b000220 | prose | pages [13] -->
A cellular automaton is a discrete model that describes the time development of a system. It is referred to as a discrete model because it treats time as a discrete variable. The model requires an initial conﬁguration and a set of ﬁxed laws that determine how the system develops. At every time-step, the cellular automaton will advance incrementally and all the laws will be implemented.

<!-- b000221 | heading | pages [13] -->
5.2.1 Assumptions of the Model

<!-- b000222 | prose | pages [13] -->
The following general assumptions are made based on common sense and we use them throughout our model.

<!-- b000223 | prose | pages [13] -->
• Drivers obey the rules with a probability. It is obvious in real life that a driver might not want to change lane even if all the conditions are satisﬁed.

<!-- b000224 | prose | pages [13] -->
We assume that a driver change to the left lane and the right lane with the probability pleft and pright respectively when possible.

<!-- b000225 | prose | pages [13, 14] -->
• All drivers tend to drive as fast as possible while keeping a safe follow- ing distance. Nearly every driver wants to drive faster on the freeway as long as there is enough time for him to react if the vehicle ahead decel- erates. Also, the maximum speed is limited by the vehicle type and the speed limit of freeway.

<!-- b000226 | furniture | pages [14] -->
Team # 26333

<!-- b000227 | furniture | pages [14] -->
Page 13 of 53

<!-- b000229 | prose | pages [14] -->
• Drivers are “myopic”, which means that they can only see one vehicle in front of him, one vehicle behind him and several vehicles on the neigh- boring lanes. A driver can see the vehicle in front of him by eyes and see the vehicle behind him with the help of rearview mirrors. Moreover, he can turn his head to left and right to see the car on the neighboring lanes. He might see cars, say, on the left lane of the left lane, but he will not take this information into account when deciding whether to change lanes. Thus, we simply suppose that the drivers cannot see these vehicles and other vehicles much further.

<!-- b000230 | prose | pages [14] -->
• Drivers make decisions only according to his own interest. Because driver- s are “myopic”, they cannot know the conditions of the whole freeway.

<!-- b000231 | prose | pages [14] -->
Consequently, they make greedy decisions in order to pass the freeway in a shorter time.

<!-- b000232 | prose | pages [14] -->
Additionally, in order to implement cellular automaton on our problem, we pro- pose the following assumptions:

<!-- b000233 | prose | pages [14] -->
• We assume that lane-changing does not cost additional time. Obviously, vehicles change lanes while moving. Although the travelling distance of lane-changing seems longer compared with just moving in one lane, the drivers tend to accelerate to change lanes. Thus, we simply suppose that the lane-changing costs the same amount of time as moving in one lane.

<!-- b000234 | prose | pages [14] -->
This assumption helps a lot to build a cellular automaton.

<!-- b000235 | prose | pages [14] -->
• Each cell represents a 4m*6m area. The road’s length is 2000 cells. A lane’s width is 1 cell. We divide a multilane freeway into equally parti- tioned lanes. We choose a length of 12km to simulate because of the trade- off between time complexity and the completeness of the model.Also, each array of cells represents a lane.

<!-- b000236 | prose | pages [14] -->
• Every time-step represents 1 second. Such an assumption is made by n- early all cellular automaton techniques.

<!-- b000237 | prose | pages [14] -->
• We run 20000 time-step and analyze the last 1000 steps. This ensures us to obtain steady-state conditions.

<!-- b000238 | prose | pages [14] -->
• While all vehicles have a trend to reach the maximum speed, every sin- gle vehicle randomly slows down with probability p. This randomization is a characteristic of trafﬁc ﬂow.

<!-- b000239 | furniture | pages [15] -->
Team # 26333

<!-- b000240 | furniture | pages [15] -->
Page 14 of 53

<!-- b000241 | prose | pages [15] -->
• Acceleration is done steadily while any kind of deceleration can be done in one time-step. Steady acceleration is an energy-saving behavior and drivers will decelerate to avoid possible collisions.

<!-- b000242 | heading | pages [15] -->
5.2.2 Characteristics of Vehicles

<!-- b000243 | prose | pages [15] -->
We classify the vehicles into three groups:

<!-- b000244 | prose | pages [15] -->
• Cars: Cars are those small vehicles, which usually can have high speeds.

<!-- b000245 | prose | pages [15] -->
• Buses: Buses are large vehicles used for carrying people, and their speeds can be relatively high.

<!-- b000246 | prose | pages [15] -->
• Trucks: Trucks are large vehicles used for moving heavy articles, and they can only have lower speeds.

<!-- b000247 | prose | pages [15] -->
Then we deﬁne the characteristics of the three types of vehicles:

<!-- b000248 | prose | pages [15] -->
• Occupancy: Each car occupies one cell. Since a typical car’s length is 3.6m- 4.6m. The car cannot fully occupy a cell. We place the car in the middle of the cell and treat the space in front of and behind the car as safe distance.

<!-- b000249 | prose | pages [15] -->
Accordingly, each bus and each truck occupies two cells with safe distance preserved.

<!-- b000250 | prose | pages [15] -->
• Maximum speed: At each time-step, cars cannot move more than 6 cells, which means that its maximum speed is 129.6km/h. Similarly, buses can- not move more than 5 cells per time step, since they are large so that they cannot move at a higher speed. Lastly, trucks carry heavy goods so they have the lowest maximum speed. We suppose it is 3 cells per time-step, which equals 64.8km/h. The maximum speed here is based on the vehi- cles themselves. If they exceed the speed limit, vehicles can drive no more than the limit. In China, the maximum speed limit of freeway is 120km/h and the lowest speed limit of that is 60km/h. The role of speed limit is examined by comparing situations under different limits.

<!-- b000251 | prose | pages [15] -->
• Percentage: We assume that cars account for 60% of the trafﬁc ﬂow, buses account for 30% and trucks account for 10%. This assumption are based on the data collected by [9]

<!-- b000252 | prose | pages [15] -->
The characteristics are listed in Table 3.

<!-- b000253 | furniture | pages [16] -->
Team # 26333

<!-- b000254 | furniture | pages [16] -->
Page 15 of 53

<!-- b000255 | prose | pages [16] -->
Table 3 Characteristics of Vehicles Type Occupancy Maximum speed percentage

<!-- b000256 | prose | pages [16] -->
60% Car 1 cell 6 cells/sec 30% Bus 2 cells 5 cells/sec 10% Truck 2 cells 3 cells/sec

<!-- b000257 | heading | pages [16] -->
5.2.3 Laws Governing the Cellular Automaton

<!-- b000258 | prose | pages [16] -->
Our cellular automaton is implemented by an algorithm, the essence of the al- gorithm is the set of laws sequentially implemented in every time-step. In this subsection, we will introduce the laws. These laws are based on the previous analysis and are expressed from a computational perspective.

<!-- b000259 | prose | pages [16] -->
Step 1: moving

<!-- b000260 | prose | pages [16] -->
These laws are set based on the assumptions of the model and the char- acteristics of the vehicles. We denote the jth vehicle on lane i by vehiclei j.

<!-- b000261 | prose | pages [16] -->
(a) Determine the speed Our three laws below was implemented sequentially, so we use (t + 1 3), (t + 2 3) to denote the intermediate state.

<!-- b000262 | prose | pages [16] -->
i. Acceleration

<!-- b000263 | prose | pages [16, 17] -->
Figure 3 Clariﬁcation of some denotes All drivers tend to drive as fast as possible:

<!-- b000264 | furniture | pages [17] -->
Team # 26333

<!-- b000265 | furniture | pages [17] -->
Page 16 of 53

<!-- b000267 | prose | pages [17] -->
j(t + 1 If vi j(t) < vi then vi 3) = vi j,expect, j(t) + 1

<!-- b000268 | prose | pages [17] -->
Where vi j(t) is the speed of vehiclei j at time t, vi j,expect means the expected speed of vehiclei j.

<!-- b000269 | prose | pages [17] -->
ii. Randomization Every vehicle randomly slows down by 1 with probability pslow.

<!-- b000270 | prose | pages [17] -->
Mathematically,

<!-- b000271 | prose | pages [17] -->
j(t + 2 j(t + 1 vi 3) = vi 3) −1

<!-- b000272 | prose | pages [17] -->
iii. Deceleration(because of other vehicles) To maintain a safe following distance and to avoid collision, a cell cannot be occupied by more than one vehicle at the same time-step.

<!-- b000273 | prose | pages [17] -->
j(t + 2 If vi 3) > gapi then vi j(t + 1) = gapi j(t), j(t)

<!-- b000274 | prose | pages [17] -->
Where gapi j(t) is the gap between vehiclei j and the vehicle a- head.

<!-- b000275 | prose | pages [17] -->
(b) Determine the location We derive the locations based on the speeds above:

<!-- b000276 | prose | pages [17] -->
xi j(t + 1) = xi j(t) + vi j(t + 1)

<!-- b000277 | prose | pages [17] -->
gapi j = xi+1 −xi j −1 j Where xi j is the location of vehiclei j.

<!-- b000278 | prose | pages [17] -->
Step 2: lane-changing

<!-- b000279 | prose | pages [17] -->
These rules are set based on

<!-- b000280 | prose | pages [17] -->
(a) Changing to the left lane

<!-- b000281 | prose | pages [17] -->
i. Based on trigger criterion, the driver tends to change to the left if the vehicle ahead moves so slow that he fails to reach his expected speed.

<!-- b000282 | prose | pages [17] -->
gapi j(t) < vi j,expect

<!-- b000283 | prose | pages [17] -->
ii. Then, take acceleration criterion into account, we have

<!-- b000284 | prose | pages [17] -->
gapi j(t) < lfgapi j

<!-- b000285 | prose | pages [17] -->
Where lfgapi j is the left front gap of vehiclei j.

<!-- b000286 | furniture | pages [18] -->
Team # 26333

<!-- b000287 | furniture | pages [18] -->
Page 17 of 53

<!-- b000288 | prose | pages [18, 19] -->
Figure 4 Flow chart of cellular automaton iii. Lastly, consider the factor of safety, we have

<!-- b000289 | furniture | pages [19] -->
Team # 26333

<!-- b000290 | furniture | pages [19] -->
Page 18 of 53

<!-- b000292 | prose | pages [19] -->
lbgapi j > lbvi j Where lbgapi j is the left back gap of vehiclei j, lbvi j is the speed of the vehicle behind on the left lane.

<!-- b000293 | prose | pages [19] -->
(b) Changing to the right lane i. To check the rules in 2.1 above, if any one of the rules are not satisﬁed, the driver cannot change to the left lane.

<!-- b000294 | prose | pages [19] -->
ii. To consider safety, we have

<!-- b000295 | prose | pages [19] -->
rfgapi j > vi j Where rfgapi j is the right front gap of vehiclei j.

<!-- b000296 | prose | pages [19] -->
iii. To consider another safety criterion, we have

<!-- b000297 | prose | pages [19] -->
rbgapi j > rbvi j Where rbgapi j is the right back gap of vehiclei j, rbvi j is the speed of the vehicle behind on the right lane.

<!-- b000298 | prose | pages [19] -->
The algorithm is diagrammed in Figure 4.

<!-- b000299 | heading | pages [19] -->
5.2.4 Modeling Using Periodic Boundary Conditions

<!-- b000300 | prose | pages [19] -->
To run a cellular automaton, we need to specify the boundary conditions and the initial condition. Boundary conditions determine the way vehicles move into our system and the way they move out of our system. Likewise, an initial condition determines the distribution of vehicles in our system and the speeds of them.

<!-- b000301 | prose | pages [19] -->
Inspired by Nagel and Schreckenberg’s work [3], we tackle the problem with periodic boundary conditions. Periodic boundary conditions assume that the vehicles moving out of the freeway will immediately appear at the front of the system, so the total number of vehicles is a constant during the dynamics. Thus, we can accurately deﬁne a constant system density and study the performance of the rule with varying density. Moreover, periodic boundary conditions turn our road into a closed system, so it is similar to the case that all vehicles are moving on a circle. We, in turn, name our extended model as a “Ring Road” model.

<!-- b000302 | prose | pages [19] -->
Although there is no such short ring road in reality, this model still holds true be- cause we can imagine that a freeway is made up of several equally partitioned sections and the vehicles on all the sections are identical. Obviously, this sit- uation satisﬁes periodic boundary conditions. This is how periodic boundary conditions relate theory with reality.

<!-- b000303 | furniture | pages [20] -->
Team # 26333

<!-- b000304 | furniture | pages [20] -->
Page 19 of 53

<!-- b000305 | heading | pages [20] -->
5.3 The Reﬁned Model with Ramps

<!-- b000306 | prose | pages [20] -->
Even though the “Ring Road” model is good enough to solve the problem, it fails to consider the effect of ramps. Consequently, we reﬁne our model by adding entrance and exit ramps and applying open boundary conditions.

<!-- b000307 | heading | pages [20] -->
5.3.1 Adding Entrance and Exit Ramps

<!-- b000308 | prose | pages [20] -->
Vehicles may also use an entrance ramp to enter the freeway. The entrance ramp- s give them a chance to accelerate to the expected speed. However, most ramps are too short to allow them to speed up to, say, 100km/h. As a result, the vehi- cles on the right-most lane might slow down to yield to the incoming vehicles or incoming vehicles might hard to enter the freeway. Both cases might have dele- terious effects on the quality of trafﬁc ﬂow. Likewise, vehicles have to decelerate in order to enter an exit ramp, and similar problem will occur.

<!-- b000309 | caption | pages [20] -->
Figure 5 demonstrates a real freeway section containing ramps. We can see that

<!-- b000310 | prose | pages [20] -->
an exit ramp was followed by an entrance ramp. We add the ramps based on this fact.

<!-- b000311 | prose | pages [20] -->
The laws mentioned in the previous section are still valid, and the only differ- ence is how the incoming vehicles enter the freeway. We add some additional laws to instruct the behavior of incoming vehicles. To introduce the concept of ramps in our cellular automaton, we add the following assumptions.

<!-- b000312 | prose | pages [20] -->
Figure 5 A real freeway section containing ramps

<!-- b000313 | furniture | pages [21] -->
Team # 26333

<!-- b000314 | furniture | pages [21] -->
Page 20 of 53

<!-- b000315 | heading | pages [21] -->
5.3.2 Additional Assumptions in the Reﬁned Model

<!-- b000316 | prose | pages [21] -->
• The exit ramp: We assume that the overlap between the freeway and the exit ramp ranges from the 850th cell to the 900th cell, which is 300m.

<!-- b000317 | prose | pages [21] -->
• The entrance ramp: We assume that the overlap between the freeway and the entrance ramp ranges from the 1100th cell to the 1500th cell, which is 300m.

<!-- b000318 | heading | pages [21] -->
5.3.3 Additional Laws

<!-- b000319 | prose | pages [21] -->
• Off-ramp law: If the vehicle wants to go off the free way(how to determine this will be discussed later), it is not allowed to change to left lane after it reaches the 700th cell. At the same time, it will slow down to 3cell/s. If the vehicle is on the right-most lane between the 850th cell and the 900th cell, we assume that it can move into the ramp at the next time step if it wants to. Since in reality exit ramps usually contain two lanes and the ratio of vehicles exit at one ramp is low, this assumption is reasonable. If it misses the exit, it will not be governed by this additional law anymore.

<!-- b000320 | prose | pages [21] -->
• On-ramp law: For a vehicle on the entrance lamp, if the laws of changing to the left lane are satisﬁed, it can go into the freeway during the next time- step. Otherwise, it will continue to move forward.

<!-- b000321 | heading | pages [21] -->
5.3.4 Modeling Using Open Boundary Conditions

<!-- b000322 | prose | pages [21] -->
After we introduce ramps into our model, it is no longer reasonable to consider it as a closed system. Thus, we must use open boundary conditions to determine how the vehicles ﬂow in. Considering that the amount of trafﬁc is stochastic and the input of the system is discrete, a generally used approach is to model the input of vehicles as a Poisson process. Consequently, we assume that the number of vehicles ﬂowing in from the starting point in any interval of length t is Poisson-distributed with mean λt.

<!-- b000323 | prose | pages [21] -->
While moving into the system, vehicles tend to move off through the exit ramp with a probability pexit. And the vehicles ﬂowing in from the entrance ramp in any interval of length t is 0-1-distributed with mean λt. In other words, we try to let the number of vehicles from the entrance ramp equal the number of vehicles from the exit ramp. However, as discussed above, some vehicles may fail to exit the freeway and some others may fail to enter the freeway. We view both of them as bad characteristics of the trafﬁc ﬂow. We analyze these characteristics and we will discuss them in the next section.

<!-- b000324 | furniture | pages [22] -->
Team # 26333

<!-- b000325 | furniture | pages [22] -->
Page 21 of 53

<!-- b000326 | heading | pages [22] -->
6 Results: Inﬂuencing Factors

<!-- b000327 | prose | pages [22] -->
In this section, we ﬁrst give a deﬁnition of light and heavy trafﬁc. Then we explicitly deﬁne four factors and change one factor each time in order to ana- lyze how this factor inﬂuence the performance of the Keep-Right-Except-To-Pass Rule.

<!-- b000328 | prose | pages [22] -->
We run several simulations with cellular automaton and ﬁnd that the trafﬁc ﬂow can be classiﬁed into two groups. The time space diagram (Figure 8) demon- strates these two kinds of trafﬁc ﬂow. The diagram shows the trace of every vehicle in the simulation. A gentle trace indicates a low speed. Conversely, a steep trace indicates a high speed.

<!-- b000329 | prose | pages [22] -->
(a) Time space diagram(occupancy=0.1) (b) Time space diagram(occupancy=0.4)

<!-- b000330 | prose | pages [22] -->
Figure 6

<!-- b000331 | prose | pages [22] -->
• From the left diagram, we can clearly see that the vehicles with a high speed can continue with the high speed which indicates that it is not con- strained by slower vehicles. This is a situation of light trafﬁc.

<!-- b000332 | prose | pages [22] -->
• From the right diagram, we can see that no vehicle can reach a high speed, which indicates that there is a congestion. This is a situation of heavy trafﬁc.

<!-- b000333 | heading | pages [22] -->
6.1 Variables and Criteria

<!-- b000334 | prose | pages [22] -->
We choose number of lanes, the maximum speed limit, the minimum speed limit and signaling behavior as our variables. To judge the effectiveness of the rule, we propose the following criteria:

<!-- b000335 | furniture | pages [23] -->
Team # 26333

<!-- b000336 | furniture | pages [23] -->
Page 22 of 53

<!-- b000337 | prose | pages [23] -->
• Flow rate: ﬂow rate is the number of vehicles passing a point on a highway per unit time.[10] flow rate = N T where N stands for the number of vehicles passing a point on the highway in the time of T.

<!-- b000338 | prose | pages [23] -->
• Average speed: the average speed of all vehicles passing a point on a high- way or a lane over some speciﬁed time period.

<!-- b000339 | prose | pages [23] -->
Nj(t) 3 1 X X vi average speed v(t) = j(t) N(t) j=1 i=1

<!-- b000340 | prose | pages [23] -->
where N(t) stands for the number of vehicles on the freeway, and Nj(t) stands for the number of vehicles on jth lane.

<!-- b000341 | prose | pages [23] -->
• Lane utilization ratio: lane utilization ratio is deﬁned as the ratio between the number of vehicles on the lane to the total number of vehicle on the freeway.

<!-- b000342 | prose | pages [23] -->
lane utilization ratioi = Nj(t) N(t)

<!-- b000343 | prose | pages [23] -->
• Sharp braking frequency: we do not consider the occurrence of accidents in our simulation, since we view accidents as abnormal events and it is difﬁcult to consider abnormal events in microscopic models. Instead, we use sharp braking frequency as an indicator of unsafety. Sharp braking fre- quency occurs when a vehicle’s speed decreases by more than 2 cell/time- step. If this happens in our simulation, we assume that it is more likely to cause an accident in reality.

<!-- b000344 | prose | pages [23] -->
• Shift ratio: the number of shifts per unit time.

<!-- b000345 | prose | pages [23] -->
shift ratio = Nshift(t) N(t)

<!-- b000346 | prose | pages [23] -->
where Nshift(t) stands for the number of vehicles changing lanes at tth time step.

<!-- b000347 | prose | pages [23] -->
• Satisfaction: if a vehicle fails to reach its maximum speed, the driver’s satisfaction will decrease. We deﬁne the expected time texpect as the time it takes to drive with the maximum speed through a given distance. We deﬁne the actual time tactual as the time it actually takes to drive through the same distance. Then we derive the criteria by dividing expected time by actual time. The value of satisfaction ranges from 0 to 1.

<!-- b000348 | prose | pages [23, 24] -->
satisfaction = texpect tactual • Standard deviation of speed: people might feel uncomfortable if the ve- hicle continues to accelerate and decelerate. We use standard deviation of speed to measure this kind of discomfort.

<!-- b000349 | furniture | pages [24] -->
Team # 26333

<!-- b000350 | furniture | pages [24] -->
Page 23 of 53

<!-- b000352 | prose | pages [24] -->
v Nj(t) 3 T u 1 u X X X [vi j(t) −v(t)]2 Std. deviation of speed = t N(t) t=1 j=1 i=1

<!-- b000353 | heading | pages [24] -->
6.2 Number of Lanes

<!-- b000354 | heading | pages [24] -->
6.2.1 Flow Rate

<!-- b000355 | prose | pages [24] -->
From the ﬂow rate and occupancy ﬁgure, we can obtain an optimal occupancy. In a low occupancy situation, the number of cars are too low. Although they are more likely to reach their maximum speeds, the road resources are not fully utilized, so the total ﬂow rate is low. In a high occupancy situation, the number of cars are too high, and it might cause a trafﬁc congestion. We expect an optimal occupancy and view it as a watershed of light trafﬁc and heavy trafﬁc.

<!-- b000356 | prose | pages [24] -->
Total ﬂow rate under the condition of different occupancies (3 & 4 lanes) Figure 7

<!-- b000357 | prose | pages [24] -->
From Figure 7, we can see that the optimal occupancy for a 3-lane freeway and a 4-lane freeway is between 0.2 and 0.3. Thus, in our following analysis, we choose an occupancy of 0.1 to represent a light trafﬁc condition and an occu- pancy of 0.4 to represent a heavy trafﬁc condition.

<!-- b000358 | furniture | pages [25] -->
Team # 26333

<!-- b000359 | furniture | pages [25] -->
Page 24 of 53

<!-- b000360 | prose | pages [25] -->
(a) Flow rate of each lane (3 lanes) (b) Flow rate of each lane (4 lanes)

<!-- b000361 | prose | pages [25] -->
Figure 8

<!-- b000362 | prose | pages [25] -->
We also calculate the ﬂow rate of each lane and sequence them from left to right. From the ﬁgures, we conclude that the optimal occupancy of rightmost lane is lower than that of leftmost lane. This tendency holds true for both 3-lane and 4-lane freeways. However, it’s not a signiﬁcant difference.

<!-- b000363 | heading | pages [25] -->
6.2.2 Average Speed

<!-- b000364 | prose | pages [25] -->
Average speed under the condition of different occupancies (3 & 4 lanes) Figure 9

<!-- b000365 | prose | pages [25, 26] -->
As occupancy increases, the average speed tends to decrease due to congestion. This common sense can be justiﬁed from the speed-occupancy Figure 9. Sur- prisingly, the curves for 3-lane and 4-lane coincide! This result indicates that different lane numbers may hardly change the performance of the rule under the condition of the same occupancy.

<!-- b000366 | furniture | pages [26] -->
Team # 26333

<!-- b000367 | furniture | pages [26] -->
Page 25 of 53

<!-- b000369 | prose | pages [26] -->
(a) Average speed of each lane (3 lanes) (b) Average speed of each lane (4 lanes)

<!-- b000370 | prose | pages [26] -->
Figure 10

<!-- b000371 | prose | pages [26] -->
From the average speed of each lane, we can conclude that the leftmost lane has the highest speed and the rightmost lane has the lowest speed. This is because the rule requires drivers to overtake from the left.

<!-- b000372 | heading | pages [26] -->
6.2.3 Lane Utilization Ratio

<!-- b000373 | prose | pages [26] -->
(a) Lane utilization ratio of each lane (3 lanes) (b) Lane utilization ratio of each lane (4 lanes)

<!-- b000374 | prose | pages [26, 27] -->
Figure 11 From the Figure 11, we can know that the lane utilization ratio of the leftmost lane increases as occupancy increases. It is reasonable because when occupancy increases, more vehicles use the leftmost lane to overtake. In contrast, in the light trafﬁc situation, the lane utilization ratio of the rightmost lane decreases as occupancy increases. It is because more vehicles try to change to the middle lane to move faster. The increase tendency in the heavy trafﬁc condition indicates the difﬁculty of overtaking.

<!-- b000375 | furniture | pages [27] -->
Team # 26333

<!-- b000376 | furniture | pages [27] -->
Page 26 of 53

<!-- b000378 | heading | pages [27] -->
6.2.4 Sharp Braking Frequency

<!-- b000379 | prose | pages [27] -->
Figure 12 Sharp braking frequency under the condition of different occupancies (3 & 4 lanes)

<!-- b000380 | prose | pages [27] -->
There also exists a peak value in the sharp braking frequency curve. In the case of light trafﬁc, the average speed is high. Therefore, as occupancy increases, sharp braking situation increases. In the case of heavy trafﬁc, the average speed is low, so the frequency decreases correspondingly.

<!-- b000381 | furniture | pages [28] -->
Team # 26333

<!-- b000382 | furniture | pages [28] -->
Page 27 of 53

<!-- b000383 | heading | pages [28] -->
6.2.5 Shift Ratio

<!-- b000384 | prose | pages [28] -->
Shift ratio under the condition of different occupancies (3 & 4 lanes) Figure 13

<!-- b000385 | prose | pages [28] -->
In the low occupancy case, the ratio is high, probably because of the low car number. In the high occupancy case, the ratio approximately keeps unchanged.

<!-- b000386 | heading | pages [28] -->
6.2.6 Satisfaction

<!-- b000387 | prose | pages [28] -->
Satisfaction under the condition of different occupancies (3 & 4 lanes) Figure 14

<!-- b000388 | prose | pages [28] -->
As the occupancy increases, it takes longer for drivers to pass a certain distance, so their satisfaction decreases. Again, the curves coincide, which means there is little difference between 3-lane and 4-lane freeway in terms of satisfaction under the condition of the same occupancy.

<!-- b000389 | furniture | pages [29] -->
Team # 26333

<!-- b000390 | furniture | pages [29] -->
Page 28 of 53

<!-- b000391 | heading | pages [29] -->
6.2.7 Standard Deviation of Speed

<!-- b000392 | prose | pages [29] -->
Figure 15 Std. deviation of speed.png under the condition of different occupancies (3 & 4 lanes)

<!-- b000393 | prose | pages [29] -->
The shapes of the curves are similar to the speed curves and they are irrelevant to the lane number.

<!-- b000394 | heading | pages [29] -->
6.3 Maximum Speed Limit

<!-- b000395 | prose | pages [29] -->
We study the case in which the maximum speed limit of 4 cell/s (86.4km/h) and 5 cell/s (108km/h) and a case with no maximum speed limit.

<!-- b000396 | furniture | pages [30] -->
Team # 26333

<!-- b000397 | furniture | pages [30] -->
Page 29 of 53

<!-- b000398 | heading | pages [30] -->
6.3.1 Flow Rate and Average Speed

<!-- b000399 | prose | pages [30] -->
(a) Flow rate in light & heavy trafﬁc (different (b) Average speed in light & heavy trafﬁc (dif- maximum limit) ferent maximum limit)

<!-- b000400 | prose | pages [30] -->
Figure 16

<!-- b000401 | prose | pages [30] -->
Vehicles can move in a high speed in a light trafﬁc case, so the maximum speed limit must have a signiﬁcant inﬂuence on the ﬂow rate and speed. In a heavy trafﬁc case, however, vehicles averagely maintain a low speed, and few of them can reach the maximum speed limit, so it can hardly inﬂuence the average speed. However, a maximum speed limit can avoid sharp changes of following dis- tance, which is beneﬁcial to the whole trafﬁc ﬂow. Therefore, a proper speed limit might result in a higher ﬂow rate. We can clearly see that the results meet our expectations from the Figure 16.

<!-- b000402 | furniture | pages [31] -->
Team # 26333

<!-- b000403 | furniture | pages [31] -->
Page 30 of 53

<!-- b000404 | heading | pages [31] -->
6.3.2 Sharp Braking Frequency and Shift Ratio

<!-- b000405 | prose | pages [31] -->
(a) Sharp braking frequency in light & heavy (b) Shift ratio in light & heavy trafﬁc (different trafﬁc (different maximum limit) maximum limit)

<!-- b000406 | prose | pages [31] -->
Figure 17

<!-- b000407 | caption | pages [31] -->
Figure 17 demonstrate that the maximum speed limit can effectively reduce the

<!-- b000408 | prose | pages [31] -->
sharp braking frequency and shift ratio in a light trafﬁc case, which is beneﬁcial to safety. Nevertheless, it has little impact in a heavy trafﬁc case.

<!-- b000409 | heading | pages [31] -->
6.3.3 Lane Utilization Ratio

<!-- b000410 | prose | pages [31] -->
(a) Lane utilization ratio in light trafﬁc (differ- (b) Lane utilization ratio in heavy trafﬁc (differ- ent maximum limit) ent maximum limit)

<!-- b000411 | prose | pages [31, 32] -->
Figure 18 From Figure 18, we can conclude that the utilization ratio of the leftmost lane in a light trafﬁc case decreases under a more strict speed limit because the limit reduces driver’s willingness to overtake.

<!-- b000412 | furniture | pages [32] -->
Team # 26333

<!-- b000413 | furniture | pages [32] -->
Page 31 of 53

<!-- b000415 | heading | pages [32] -->
6.4 Minimum speed limit

<!-- b000416 | prose | pages [32] -->
We study the inﬂuence of minimum speed limit by presenting two cases: a case with a minimum speed limit of 3 cell/s (64.8 km/h). By minimum speed limit we mean that vehicles will not exceed the limit due to randomization. However, they can decelerate due to safety consideration.

<!-- b000417 | heading | pages [32] -->
6.4.1 Flow Rate and Average Speed

<!-- b000418 | prose | pages [32] -->
(a) Flow rate in light & heavy trafﬁc (different (b) Average speed in light & heavy trafﬁc (dif- minimum limit) ferent minimum limit)

<!-- b000419 | prose | pages [32] -->
Figure 19

<!-- b000420 | prose | pages [32] -->
Opposite from the maximum speed limit case, the minimum speed limit plays an important role in a heavy trafﬁc case and it is of little importance in a light trafﬁc case. We can clearly conclude that from Figure 19

<!-- b000421 | furniture | pages [33] -->
Team # 26333

<!-- b000422 | furniture | pages [33] -->
Page 32 of 53

<!-- b000423 | heading | pages [33] -->
6.4.2 Sharp Braking Frequency and Shift Ratio

<!-- b000424 | prose | pages [33] -->
(a) Sharp braking frequency in light & heavy (b) Shift ratio in light & heavy trafﬁc (different trafﬁc (different minimum limit) minimum limit)

<!-- b000425 | prose | pages [33] -->
Figure 20

<!-- b000426 | prose | pages [33] -->
In the light trafﬁc case, vehicles cannot slow down in advance due to the speed limit, which in turn increase the sharp braking frequency. In the heavy trafﬁc case, the frequency decreases. The reason might lies in the low shift ratio and the ﬂuent trafﬁc ﬂow. The condition for lane changing is difﬁcult to satisfy. Figure 20 illustrates this conclusion.

<!-- b000427 | heading | pages [33] -->
6.4.3 Lane Utilization Ratio

<!-- b000428 | prose | pages [33] -->
(a) Lane utilization ratio in light trafﬁc (differ- (b) Lane utilization ratio in heavy trafﬁc (differ- ent minimum limit) ent minimum limit)

<!-- b000429 | prose | pages [33, 34] -->
Figure 21 In the light trafﬁc case, the ratio is of little inﬂuence. In the heavy trafﬁc case, the ratio tends to evenly distribute between the three lanes due to the difﬁculty to change lane. The results are shown in Figure 21.

<!-- b000430 | furniture | pages [34] -->
Team # 26333

<!-- b000431 | furniture | pages [34] -->
Page 33 of 53

<!-- b000433 | heading | pages [34] -->
6.5 Signal Before Shifting

<!-- b000434 | prose | pages [34] -->
In real life, it is a rule to signal before changing lane. We try to add this factor into our model. We assume that a driver must signal ﬁrst if the lane-changing conditions are satisﬁed. Then the related vehicle might decelerate to give way to the driver. Then the driver can change the lane in the next time step. We compare the cases with and without this signal mechanism.

<!-- b000435 | heading | pages [34] -->
6.5.1 Flow Rate and Average Speed

<!-- b000436 | prose | pages [34] -->
(a) Flow rate in light & heavy trafﬁc (with or (b) Average speed in light & heavy trafﬁc (with without signaling) or without signaling)

<!-- b000437 | prose | pages [34] -->
Figure 22

<!-- b000438 | prose | pages [34] -->
When signaling is considered, acceleration will be constrained, which will re- duce the ﬂow rate and the speed of the trafﬁc ﬂow. Figure 22 illustrates this change.

<!-- b000439 | furniture | pages [35] -->
Team # 26333

<!-- b000440 | furniture | pages [35] -->
Page 34 of 53

<!-- b000441 | heading | pages [35] -->
6.5.2 Sharp Braking Frequency and Shift Ratio

<!-- b000442 | prose | pages [35] -->
(a) Sharp braking frequency in light & heavy (b) Shift ratio in light & heavy trafﬁc (with or trafﬁc (with or without signaling) without signaling)

<!-- b000443 | prose | pages [35] -->
Figure 23

<!-- b000444 | prose | pages [35] -->
Because vehicles’ giving-way behavior, the shift ratio increases and vehicles have to respond to the signal behavior, which will increase sharp braking fre- quency and shift ratio. Figure 23 demonstrates this statement.

<!-- b000445 | heading | pages [35] -->
6.6 Conclusions

<!-- b000446 | prose | pages [35] -->
Based on the results, we can conclude that:

<!-- b000447 | prose | pages [35] -->
• The number of lanes is not an inﬂuential factor under any circumstances.

<!-- b000448 | prose | pages [35] -->
• The maximum speed limit plays a signiﬁcant role in light trafﬁc while it is of no importance in heavy trafﬁc.

<!-- b000449 | prose | pages [35] -->
• The minimum speed limit plays a signiﬁcant role in heavy trafﬁc while it is of no importance in light trafﬁc.

<!-- b000450 | prose | pages [35] -->
• Signaling behavior reduce ﬂow rate and average while enhancing safety.

<!-- b000451 | furniture | pages [36] -->
Team # 26333

<!-- b000452 | furniture | pages [36] -->
Page 35 of 53

<!-- b000453 | heading | pages [36] -->
7 Results: the Optimal Rule

<!-- b000454 | prose | pages [36] -->
We examine ﬁve basic rules and design four improved rules. In order to deter- mine the performance of the rules, we implement a fuzzy synthetic evaluation to consider all the criteria.

<!-- b000455 | heading | pages [36] -->
7.1 Basic Rules of Overtaking

<!-- b000456 | prose | pages [36] -->
We take a three-lane freeway as an example to state the rules, similar rules for other kind of freeway can be easily derived from these rules. Apart from the keep-right-except-to-pass rule, another four basic rules are presented as follows:

<!-- b000457 | prose | pages [36] -->
• The free-overtaking rule: Drivers can overtake or change lane as they wish. In other words, there is no rule for overtaking.

<!-- b000458 | prose | pages [36] -->
• The no-overtaking rule: It restricts the vehicles in their own lane. The ve- hicles randomly move into the freeway and once they are moving on the freeway, they must stick to their current lane. This rule can be implement- ed by replacing the dashed lines separating lanes with full lines. This lane marking bans drivers from changing lanes.

<!-- b000459 | prose | pages [36] -->
• The different-speed-limit-on-each-lane rule:the maximum speed limit on the rightmost lane is the lowest. The maximum speed limit on the leftmost lane is the highest. The maximum speed limit on the middle lane is in the middle. This rule can be implemented by hanging corresponding speed limit sign over each lane, which will indicate the drivers to control their speeds.

<!-- b000460 | prose | pages [36] -->
• The complete-assigned-lane rule: Cars are assigned to the leftmost lane.

<!-- b000461 | prose | pages [36] -->
Buses are assigned to the middle lane. Trucks are assigned to the rightmost lane. No vehicles can change lanes after it moves into the freeway. This rule can be implemented by hanging the corresponding guide sign over each lane.

<!-- b000462 | heading | pages [36] -->
7.2 Criteria and Single Criterion Analysis for Basic Rules

<!-- b000463 | prose | pages [36] -->
We adopt ﬂow rate and average speed as criteria for the quality of trafﬁc ﬂow and we use sharp braking frequency as a criterion for safety. Moreover, we use satisfaction and standard deviation of speed as criteria for people’s experience of the trip. We analyze the ﬁve basic rules with every single criterion to see their performance in both light and heavy trafﬁc.

<!-- b000464 | furniture | pages [37] -->
Team # 26333

<!-- b000465 | furniture | pages [37] -->
Page 36 of 53

<!-- b000466 | heading | pages [37] -->
7.2.1 Trafﬁc Flow Criteria: Flow Rate and Speed

<!-- b000467 | prose | pages [37] -->
(a) Flow rate in light & heavy trafﬁc (different (b) Average speed in light & heavy trafﬁc (dif- rules) ferent rules)

<!-- b000468 | prose | pages [37] -->
Figure 24

<!-- b000469 | prose | pages [37] -->
We can see that the speed is coherent with the ﬂow rate. In the light trafﬁc case, the no-overtaking rule performs the worst because the road resources cannot be fully used. There is no signiﬁcant difference between other rules.

<!-- b000470 | prose | pages [37] -->
In the heavy trafﬁc case, the complete-assigned-lane rule behaves the worst. In the simulation, the leftmost lane, which is assigned to cars, suffers bad conges- tion while the other two lanes are relatively available. The different-speed-limit- on-each-lane rule performs the best. The rule bans large vehicles from entering the passing lanes as well as prevents a large number of cars from entering the rightmost lane.

<!-- b000471 | furniture | pages [38] -->
Team # 26333

<!-- b000472 | furniture | pages [38] -->
Page 37 of 53

<!-- b000473 | heading | pages [38] -->
7.2.2 Safety Criterion: Sharp Braking Frequency

<!-- b000474 | prose | pages [38] -->
Sharp braking frequency in light & heavy trafﬁc (different rules) Figure 25

<!-- b000475 | prose | pages [38] -->
Higher sharp braking frequency indicates a higher risk of accidents in reality. The results are presented in Figure 25.

<!-- b000476 | prose | pages [38] -->
In the light trafﬁc case, the no-overtaking rule performs the worst because ve- hicles of high speeds can only press the brake instead of changing lane if they encounters slow vehicles ahead. The well-performed rules are the keep-right- except-to-pass rule and the complete-assigned-lane rule. The latter bans over- taking too, but the speed is relatively even, so the sharp braking situation seldom occurs.

<!-- b000477 | prose | pages [38] -->
In the heavy trafﬁc case, the free-overtaking rule performs the worst. The different- speed-limit-on-each-lane rule performs the best because the rule can reasonably allocate the vehicles to three lanes by speed. Thus, the trafﬁc can ﬂow ﬂuently.

<!-- b000478 | furniture | pages [39] -->
Team # 26333

<!-- b000479 | furniture | pages [39] -->
Page 38 of 53

<!-- b000480 | heading | pages [39] -->
7.2.3 Experience Criterion: Satisfaction and Standard Deviation of Speed

<!-- b000481 | prose | pages [39] -->
(a) Satisfaction & heavy trafﬁc (different rules) (b) Std. deviation of speed in light & heavy traf- ﬁc (different rules)

<!-- b000482 | prose | pages [39] -->
Figure 26

<!-- b000483 | prose | pages [39] -->
Figure 26(a) describes satisfaction and it is coherent with the speed Figure 24(a). This coherence indicates that people feel more satisﬁed with higher speed.

<!-- b000484 | prose | pages [39] -->
Figure 26(b) compares the standard deviation of different rules. In the light trafﬁc, different-speed-limit-on-each-lane performs the best. Other rules’ per- formance are almost the same. In the heavy trafﬁc, the complete-assigned-lane rule obtains the minimum value, but this is because of low speed. In this case, the criterion cannot accurately indicate people’s experience.

<!-- b000485 | heading | pages [39] -->
7.3 Fuzzy Synthetic Evaluation for Basic Rules

<!-- b000486 | prose | pages [39] -->
The main challenge of the judging process is that we can obtain different results using different criteria. If we want to obtain a unique answer, we have to com- bine criteria to get a new, unique criterion. The relative importance of the crite- ria is hard to determine. Since we have no other information, we implement a fuzzy synthetic evaluation (FSE).[11] FSE is a multiple-criteria-decision-making method. It can determine the weights of each criterion based on the data only. One way to determine the weights is the coefﬁcient of variation method. If crite- rion can differentiate the rules evaluated, the method will assign a large weight to the criterion. We use this technique to analyze the performance of each rule.

<!-- b000487 | prose | pages [39, 40] -->
In the following subsections, we use the light trafﬁc as a case to introduce the process of FSE. The case of heavy trafﬁc can be processed in a similar way.

<!-- b000488 | furniture | pages [40] -->
Team # 26333

<!-- b000489 | furniture | pages [40] -->
Page 39 of 53

<!-- b000491 | heading | pages [40] -->
7.3.1 Identify Alternatives and Attributes

<!-- b000492 | prose | pages [40] -->
In our problem, the alternatives are the ﬁve basic rules and the attributes are the ﬁve criteria. The values of each attributes of each alternative are listed as follows:

<!-- b000493 | prose | pages [40] -->
Table 4 Criteria of Basic Rules in Light Trafﬁc sharp breaking std. deviation ﬂow rate average speed satisfaction frequency of speed

<!-- b000494 | prose | pages [40] -->
keep-right-except- 0.964 4.552 0.041 0.841 1.152 to-pass free-overtaking 0.077 1.357 0.928 4.201 0.785 no-overtaking 0.631 2.800 0.091 0.531 1.415 different-speed- 0.063 0.813 0.845 4.129 0.777 limit-on-each-lane complete-assigned- 0.033 1.481 0.932 4.256 0.808 lane

<!-- b000495 | prose | pages [40] -->
Then we derive the ideal alternative from Table ??.

<!-- b000496 | prose | pages [40] -->
u = (u0 1, u0 2, u0 3, u0 4, u0 5) = (0.964, 4.552, 0.033, 0.841, 0.813)

<!-- b000497 | heading | pages [40] -->
7.3.2 Determine Fuzzy Evaluation Matrix

<!-- b000498 | prose | pages [40] -->
The membership function is deﬁned as

<!-- b000499 | prose | pages [40] -->
|aij −u0 i | rij = max{aij} −min{aij}

<!-- b000500 | prose | pages [40] -->
Then we have the fuzzy evaluation matrix

<!-- b000501 | prose | pages [40, 41] -->
  0.000 0.000 0.127 0.000 0.508 0.108 0.201 0.750 0.180 0.814   1.000 1.000 1.000 1.000 0.901 R = 0.357 0.242 0.504 0.205 0.000 0.096 0.169 0.000 0.104 1.000 Using coefﬁcient of variation method, we deﬁne vj and wj as:

<!-- b000502 | furniture | pages [41] -->
Team # 26333

<!-- b000503 | furniture | pages [41] -->
Page 40 of 53

<!-- b000505 | prose | pages [41] -->
vj = sj vj , wj = P5 xj i=j vj

<!-- b000506 | prose | pages [41] -->
Then we calculate the weighted vector

<!-- b000507 | prose | pages [41] -->
w = (0.243, 0.226, 0.164, 0.251, 0.117)

<!-- b000508 | heading | pages [41] -->
7.3.3 Aggregate using a fuzzy operator

<!-- b000509 | prose | pages [41] -->
Then we use a fuzzy operator to aggregate and obtain the relative deviation.

<!-- b000510 | prose | pages [41] -->
5 X Fi = wjrij j=1

<!-- b000511 | prose | pages [41] -->
The relative deviation measures the distance between a speciﬁc alternative to the ideal alternative. The lower the value is, the better the alternative is.

<!-- b000512 | heading | pages [41] -->
7.3.4 The Results

<!-- b000513 | prose | pages [41] -->
The relative deviation in both cases are listed below

<!-- b000514 | prose | pages [41] -->
Table 5 Relative deviations of different rules in light trafﬁc keep-right- different-speed- complete- free-overtaking no-overtaking except-to-pass limit-on-each-lane assigned-lane

<!-- b000515 | prose | pages [41] -->
Fi 0.080 0.335 0.998 0.275 0.205

<!-- b000516 | prose | pages [41] -->
Table 6 Relative deviations of different rules in heavy trafﬁc keep-right- different-speed- complete- free-overtaking no-overtaking except-to-pass limit-on-each-lane assigned-lane

<!-- b000517 | prose | pages [41] -->
Fi 0.564 0.156 0.669 0.570 0.627

<!-- b000518 | prose | pages [41] -->
In the light trafﬁc case, the keep-right-except-to-pass rule has an absolute advan- tage over other rules while in the heavy trafﬁc case, the different-speed-limit-on- each-lane rule is the best.

<!-- b000519 | furniture | pages [42] -->
Team # 26333

<!-- b000520 | furniture | pages [42] -->
Page 41 of 53

<!-- b000521 | heading | pages [42] -->
7.4 Improved Rules of Overtaking

<!-- b000522 | prose | pages [42] -->
Based on the basic rules, we propose four improved rules by modifying or com- bining the ﬁve basic rules. When creating the rules, we consider not only the implementation of the rules but the overall quality of trafﬁc ﬂow, safety and experience as well.

<!-- b000523 | prose | pages [42] -->
• The partial-assigned-lane rule: cars are assigned to the middle lane and the leftmost lane with the permission to change between these two lanes.

<!-- b000524 | prose | pages [42] -->
Buses and trucks are assigned to the rightmost lane and they are banned from changing lanes. This rule can be implemented by hanging the cor- responding guide sign over each lane. We present this rule because cars account for 60% of the total vehicles and they have relatively high speed.

<!-- b000525 | prose | pages [42] -->
• The truck-on-rightmost-lane-only rule: It requires trucks to stick to the rightmost lane while cars and buses can change between the three lanes.

<!-- b000526 | prose | pages [42] -->
This rule can be implemented by hanging the corresponding guide sign over each lane. We present this rule because trucks have the lowest speed and they may constrain the speed of others if they appear on the passing lane.

<!-- b000527 | prose | pages [42] -->
• The minimum-speed-on-leftmost-lane rule: It sets a special minimum speed for the leftmost lane. This rule can be implemented by hanging the special speed limit sign over each lane. We hope it will help increase the efﬁciency of the leftmost passing lane.

<!-- b000528 | prose | pages [42] -->
• The partial-assigned-lane-and-keep-right rule: We combine the partial- assigned-lane rule and the keep-right-except-to-pass rule to make this rule.

<!-- b000529 | prose | pages [42] -->
In other words, vehicles are assigned by the partial-assigned-lane rule and cars overtakes by the keep-right-except-to-pass rule. We hope this rule can have the merits of previous two rules.

<!-- b000530 | heading | pages [42] -->
7.5 Fuzzy Synthetic Evaluation for All Rules

<!-- b000531 | prose | pages [42] -->
To test the performance of the improved rules, we apply a fuzzy synthetic eval- uation to all rules.

<!-- b000532 | heading | pages [42] -->
7.6 Conclusions

<!-- b000533 | prose | pages [42] -->
We can make two conclusions from the results:

<!-- b000534 | furniture | pages [43] -->
Team # 26333

<!-- b000535 | furniture | pages [43] -->
Page 42 of 53

<!-- b000536 | prose | pages [43] -->
Relative deviations of different rules in light & heavy trafﬁc Table 7 light trafﬁc heavy trafﬁc overall

<!-- b000537 | prose | pages [43] -->
keep-right-except-to-pass 0.141 0.519 0.269 free-overtaking 0.367 0.518 0.418 no-overtaking 0.991 0.576 0.851 different-speed-limit-on-each-lane 0.326 0.116 0.255 complete-assigned-lane 0.255 0.708 0.408 partial-assigned-lane 0.055 0.563 0.227 trucks-on-rightmost-lane-only 0.170 0.527 0.291 minimum-speed-on-leftmost-lane 0.233 0.320 0.262 partial-assigned-lane-and-keep-right 0.000 0.562 0.190

<!-- b000538 | prose | pages [43] -->
• The partial-assigned-lane-and-keep-right rule is the best in a light trafﬁc situation.

<!-- b000539 | prose | pages [43] -->
• The different-speed-limit-on-each-lane rule is the best in a heavy trafﬁc situation.

<!-- b000540 | prose | pages [43] -->
Based on the conclusions, we suggest that the different-speed-limit-on-each-lane rule should be used during the rush hour while the partial-assigned-lane-and- keep-right rule should be used at other times.

<!-- b000541 | heading | pages [43] -->
8 Sensitivity Analysis

<!-- b000542 | prose | pages [43] -->
Some inputs of our model may be hard to obtain or there might be some un- certainty in our inputs. Both these kinds of deviation might inﬂuence the result of our model. To test the robustness of our model, we implement a sensitivity analysis. We test our model in both light trafﬁc and heavy trafﬁc case. The anal- ysis proves that our model does not demonstrate a chaotic behavior, showing a good sensitivity.

<!-- b000543 | heading | pages [43] -->
8.1 Percentages of Vehicles

<!-- b000544 | prose | pages [43] -->
We obtain this data from a freeway company.[9] Although the data are accurate- ly collected, the percentages of vehicles may vary on different freeways. There- fore, we change the percentage of large vehicles(40%) by up to 15% to obtain the changes in our criteria.(Table 8 and Table 9) We observe a 16.61% increase in sharp braking frequency in the light trafﬁc case. The other criteria changes little.

<!-- b000545 | furniture | pages [44] -->
Team # 26333

<!-- b000546 | furniture | pages [44] -->
Page 43 of 53

<!-- b000547 | prose | pages [44] -->
In the heavy trafﬁc case, all criteria changes little. This indicates that our model can be used on freeways with varying percentages of vehicles.

<!-- b000548 | prose | pages [44] -->
Table 8 Sensitivity analysis—percentages of vehicles(light trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

<!-- b000549 | prose | pages [44] -->
16.6% 6.4% -15% 0.0% -5.9% -3.5% -10% 0.8% -0.4% 6.3% -0.6% 1.0% -5% -2.6% -2.8% 13.8% -2.5% 6.6% 0.0% 0.0% 0% 0.0% 0.0% 0.0% 5% -1.2% 0.6% 0.6% -0.1% 1.0% 10% -3.8% -2.3% 0.2% -0.1% -1.7% -5.5% -3.4% 15% -3.7% 0.3% 0.9%

<!-- b000550 | prose | pages [44] -->
Table 9 Sensitivity analysis—percentages of vehicles(heavy trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

<!-- b000551 | prose | pages [44] -->
-15% 0.1% -6.2% -2.5% -6.3% -3.4% -10% -1.3% -4.4% -3.2% -5.0% -0.8% -1.3% 0.4% -5% 4.8% -0.8% -1.5% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% 7.0% 2.6% -0.4% 2.0% 2.1% 0.1% 1.4% 10% 6.1% 3.6% 4.6% 15% 6.9% 4.4% 0.3% 5.8% 2.5%

<!-- b000552 | heading | pages [44] -->
8.2 Probability of Randomization

<!-- b000553 | prose | pages [44, 45] -->
The probability of randomization pslow describes the random deceleration be- havior of drivers. Obviously, this parameter is difﬁcult to obtain and it may change severely under different circumstances. In our approach, we assume it to be 0.2 since very few data on this matter are available. We change it by up to 15% and the sharp braking frequency shows a 15.75% deviation, which is ac- ceptable.(Table 10 and Table 11) Table 10 Sensitivity analysis—probability of randomization(light trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

<!-- b000554 | furniture | pages [45] -->
Team # 26333

<!-- b000555 | furniture | pages [45] -->
Page 44 of 53

<!-- b000557 | prose | pages [45] -->
-15% 3.4% 0.2% -1.4% 0.4% 0.3% -10% 0.3% 0.6% 0.4% 0.0% 1.4% -5% 1.6% -1.8% 2.9% -0.7% 1.8% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% 4.7% 2.3% -4.7% 0.9% -1.4% 10% 0.8% -2.0% 3.2% -0.8% 0.0% 15% -4.6% -4.9% 15.7% -3.3% 6.5%

<!-- b000558 | prose | pages [45] -->
Table 11 Sensitivity analysis—probability of randomization(heavy trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

<!-- b000559 | prose | pages [45] -->
-15% 7.3% 6.0% 3.6% 5.4% 0.4% -10% 4.7% 3.1% 0.9% 3.0% 2.8% -5% 3.6% 1.0% -0.4% 1.2% 0.7% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% -4.4% -1.1% -3.4% -2.1% 2.4% 10% -3.0% -2.8% -3.1% -3.6% 0.9% 15% -1.6% -4.1% -4.7% -4.4% 0.8%

<!-- b000560 | heading | pages [45] -->
8.3 Probability of Willing to Change Lane

<!-- b000561 | prose | pages [45] -->
We consider the case that a driver might choose not to change lane even if all the other conditions are satisﬁed. Obviously, the data are hard to get and it may suf- fer from a severe change during a short period of time. We assume probability of willing to change to the left lane and right lane are 0.5 and 0.7 respectively in our model. Therefore, we change the probabilities by up to 15% proportionally. The maximum deviation is 7.05%, which indicates a good robustness.

<!-- b000562 | furniture | pages [46] -->
Team # 26333

<!-- b000563 | furniture | pages [46] -->
Page 45 of 53

<!-- b000564 | prose | pages [46] -->
Table 12 Sensitivity analysis—probability of willing to change lane(light trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

<!-- b000565 | prose | pages [46] -->
-15% 1.9% -0.4% 4.5% -0.8% 2.4% -10% -3.9% -1.5% 6.7% -1.5% 4.5% -5% 0.4% -1.6% 4.1% -0.7% 1.1% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% 1.9% 0.5% 0.0% 0.1% 0.0% 10% -7.1% -4.7% 6.6% -3.2% 5.5% 15% -2.7% -2.4% 4.2% -1.1% 1.7%

<!-- b000566 | prose | pages [46] -->
Table 13 Sensitivity analysis—probability of willing to change lane(heavy trafﬁc) sharp breaking std. deviation of ﬂow rate average speed satisfaction frequency speed

<!-- b000567 | prose | pages [46] -->
-15% 1.8% 0.7% 0.0% -0.4% 1.4% -10% 3.5% 0.5% -0.9% 0.1% 1.1% -5% 2.6% -0.2% -1.4% -1.1% 1.9% 0% 0.0% 0.0% 0.0% 0.0% 0.0% 5% 3.8% 0.8% -1.6% -0.1% 2.2% 10% 3.9% 0.6% -1.0% -0.5% 1.8% 15% -2.2% -0.5% -2.2% -0.3% 1.1%

<!-- b000568 | heading | pages [46] -->
9 Further Discussions

<!-- b000569 | prose | pages [46] -->
9.1 Modiﬁcations for Countries Where Driving on the Left Is the Norm

<!-- b000570 | prose | pages [46] -->
Imagine there is a mirror standing in the middle of a two-way freeway in a country where driving on the right is the norm. What’s happening in the mirror is similar to a freeway in a country where driving on the left is the norm. The “passing lane” is on the right. The drivers are sitting in the right side of their cars. The cars obeys the keep-left-except-to-pass rule. All the roads, vehicles and rules look like that in a country where driving on the left is the rule.

<!-- b000571 | prose | pages [46, 47] -->
However, there is one difference which is human beings. A left-handed person is always a left handed person, but in the “mirror world”, he becomes a right- handed person and vice versa. This thought inspires us that we can modify our model to reﬂect this difference instead of simply changing the orientation. We assume in our model that the probability of willing to change to the left lane and right lane are 0.5 and 0.7 and this tendency do not change under any circumstances. Therefore, in a country like Great Britain, drivers still maintain this tendency, which means drivers have a higher tendency to move to the right lane – the passing lane. This is exactly the same as the case that we swap the two probabilities in our original model.

<!-- b000572 | furniture | pages [47] -->
Team # 26333

<!-- b000573 | furniture | pages [47] -->
Page 46 of 53

<!-- b000575 | prose | pages [47] -->
Based on the discussions above, we modify our model and run a simulation.(tableand table. ) We observe a maximum change of 4.6% in our criteria. From this analy- sis, we can safely conclude that

<!-- b000576 | prose | pages [47] -->
• Simply changing the orientation is reasonable if the willingness of chang- ing to the left lane equals the willingness of changing to the right lane.

<!-- b000577 | prose | pages [47] -->
• Even if the two values are different, the deviations are small enough to ignore.

<!-- b000578 | heading | pages [47] -->
9.2 Modiﬁcations for An Intelligent System

<!-- b000579 | prose | pages [47] -->
An intelligent system can fully control all the vehicles and let them strictly obey the rule, The keep-right-except-to-pass rule states that the vehicles must drive in the rightmost lane unless they are passing another vehicle, which means the vehicles MUST change to the right lane if the conditions are satisﬁed. In other words, the probability of willing to change to the right lane equals to 1. Based on this characteristic, we propose two intelligent systems:

<!-- b000580 | prose | pages [47] -->
• The semi-intelligent system: this system forces vehicles to change to the right lane if the conditions are satisﬁed, while whether to change to the left lane relies upon human judgment.

<!-- b000581 | prose | pages [47] -->
• The complete intelligent system: this system not only forces vehicles to change to the right lane if the conditions are satisﬁed, but also forces vehi- cles to change to the left lane if the corresponding conditions are satisﬁed.

<!-- b000582 | prose | pages [47] -->
We run the simulation to examine the performance of the intelligent systems.

<!-- b000583 | furniture | pages [48] -->
Team # 26333

<!-- b000584 | furniture | pages [48] -->
Page 47 of 53

<!-- b000585 | heading | pages [48] -->
9.2.1 Flow Rate and Average Speed

<!-- b000586 | prose | pages [48] -->
(a) Flow rate in light & heavy trafﬁc (with or (b) Average speed in light & heavy trafﬁc (with without intelligent system) or without intelligent system)

<!-- b000587 | prose | pages [48] -->
Figure 27

<!-- b000588 | prose | pages [48] -->
In the light trafﬁc case, the ﬂow rate of complete intelligent system increases s- lightly, while that of semi-intelligent system decreases slightly compared with the situation without intelligent system. The little impact is due to rich pass- ing lane resources. In the heavy trafﬁc case, the ﬂow rates of intelligent sys- tems increase. This is because forcing vehicles to move back to the rightmost lane release more passing lane resources. This is consistent with the speed ﬁg- ure.(Figure 27)

<!-- b000589 | heading | pages [48] -->
9.2.2 Sharp Braking Frequency and Shift Ratio

<!-- b000590 | prose | pages [48, 49] -->
In the light trafﬁc case, the shift ratio and sharp braking frequency change slight- ly. In the heavy trafﬁc case, the shift ratio increases signiﬁcantly as expected. The intelligent system will certainly increase shift ratio. (Figure 28) (a) Sharp braking frequency in light & heavy (b) Shift ratio in light & heavy trafﬁc (with or trafﬁc (with or without intelligent system) without intelligent system)

<!-- b000591 | furniture | pages [49] -->
Team # 26333

<!-- b000592 | furniture | pages [49] -->
Page 48 of 53

<!-- b000594 | prose | pages [49] -->
Figure 28

<!-- b000595 | prose | pages [49] -->
In the light trafﬁc case, the sharp braking frequency decreases greatly if a com- plete intelligent system is implemented. It is because if a driver is about to be constrained by the vehicle ahead, he can change to the left lane in time to avoid a sharp braking.

<!-- b000596 | heading | pages [49] -->
9.2.3 Lane Utilization Ratio

<!-- b000597 | prose | pages [49] -->
(a) Lane utilization ratio of each lane in light (b) Lane utilization ratio of each lane in heavy trafﬁc (with or without intelligent system) trafﬁc (with or without intelligent system)

<!-- b000598 | prose | pages [49, 50] -->
Figure 29 For a semi-intelligent system, the vehicles tend to move to the left lane. For a complete intelligent system, the vehicles tend to move to the right lane. Both the light trafﬁc case and the heavy trafﬁc case have this tendency. The overall changes are relatively small.

<!-- b000599 | furniture | pages [50] -->
Team # 26333

<!-- b000600 | furniture | pages [50] -->
Page 49 of 53

<!-- b000602 | heading | pages [50] -->
9.3 Additional Research on the Reﬁned Model with Ramps

<!-- b000603 | prose | pages [50] -->
In section 5.3, we present a reﬁned model taking ramps into account. Due to open boundary conditions, we use λ to control the occupancy, which determines whether the trafﬁc is heavy or light. Then we vary the value of pexit to study the model. In the simulation, we have some interesting ﬁndings.

<!-- b000604 | heading | pages [50] -->
9.3.1 Flow Rate

<!-- b000605 | prose | pages [50] -->
Flow rate in light & heavy trafﬁc (different pexit) Figure 30

<!-- b000606 | prose | pages [50] -->
The probability to exit from ramp pexit has little, if any, impact on ﬂow rate, partly because we equate the numbers of vehicles entering from the on-ramp with the numbers of vehicles exiting through the off-ramp.

<!-- b000607 | furniture | pages [51] -->
Team # 26333

<!-- b000608 | furniture | pages [51] -->
Page 50 of 53

<!-- b000609 | heading | pages [51] -->
9.3.2 Average Speed

<!-- b000610 | prose | pages [51] -->
Average speed in light & heavy trafﬁc (different pexit) Figure 31

<!-- b000611 | prose | pages [51] -->
In the previous analysis, the average speed is always consistent with ﬂow rate. Adding ramps, however, breaks this consistency, especially in the heavy trafﬁc case. As pexit increases, a large number of vehicles need to exit through the off- ramp. They will decelerate in advance, which causes low average speed.

<!-- b000612 | heading | pages [51] -->
9.3.3 Lane Utilization Ratio

<!-- b000613 | prose | pages [51] -->
(a) Lane utilization ratio of each lane in light (b) Lane utilization ratio of each lane in heavy trafﬁc (different pexit) trafﬁc (different pexit)

<!-- b000614 | prose | pages [51, 52] -->
Figure 32 In the heavy trafﬁc case, pexit will increase the utilization ratio of the rightmost lane. This reasonable because a large number of vehicles tend to use the right- most lane to move into the off-ramp.

<!-- b000615 | furniture | pages [52] -->
Team # 26333

<!-- b000616 | furniture | pages [52] -->
Page 51 of 53

<!-- b000618 | heading | pages [52] -->
9.3.4 Failure Ratio

<!-- b000619 | prose | pages [52] -->
A signiﬁcant difference in our reﬁned model is that some vehicles might fail to move to the exit of the freeway, a common situation in the real world. The failure ratio is deﬁned as the ratio of the number of the vehicles failing to exit to the total number of vehicles. We seek to investigate how failure rate changes with varying pexit.

<!-- b000620 | prose | pages [52] -->
Failure ratio in light & heavy trafﬁc (different pexit) Figure 33

<!-- b000621 | caption | pages [52] -->
Figure 33 demonstrate that in the case of light trafﬁc, pexit is an irrelevant factor.

<!-- b000622 | prose | pages [52] -->
The vehicles can move to the rightmost lane with ease. pexit plays an impor- tant role in the heavy trafﬁc case. When pexit remains low, the average speed is relatively high, which makes moving to the rightmost lane extremely difﬁcult. When pexit becomes high, the average speed slows down. Vehicles have more time to move to the rightmost lane, which in turn reduces the failure ratio.

<!-- b000623 | furniture | pages [53] -->
Team # 26333

<!-- b000624 | furniture | pages [53] -->
Page 52 of 53

<!-- b000625 | heading | pages [53] -->
10 Strengths and Weaknesses

<!-- b000626 | heading | pages [53] -->
10.1 Strengths

<!-- b000627 | prose | pages [53] -->
• Our models are fairly robust to the changes in parameters based on sen- sitivity analysis. It means a slight change in parameters will not cause a signiﬁcant change in the result.

<!-- b000628 | prose | pages [53] -->
• Different types of vehicles are taken into consideration, and the mixing ra- tio is based on actual data. We consider the length of vehicles and different maximum speeds which makes the model closer to reality.

<!-- b000629 | prose | pages [53] -->
• We come up with various criteria to compare different situations. Hence an overall comparison can be made based on these criteria.

<!-- b000630 | prose | pages [53] -->
• Our models are capable of simulating the situation in real life. The results also agree with common sense and life experience.

<!-- b000631 | prose | pages [53] -->
• A reﬁned model is established to consider the role of ramps, which is a bright spot of our model.

<!-- b000632 | heading | pages [53] -->
10.2 Weaknesses

<!-- b000633 | prose | pages [53] -->
• Factors of human judgments may be over-simpliﬁed. In order to consider that a driver may randomly decelerate and not choose to overtake when possible, we simply deﬁned a possibility respectively. Actual situation may be more complicated.

<!-- b000634 | prose | pages [53] -->
• Some of the parameters are based on semi-educated guess because few data are available. However, based on our sensitivity analysis, they will not make a great difference if slightly changed.

<!-- b000635 | prose | pages [53] -->
• We did not consider the prediction of each driver. In our model, drivers change their speed only based on the information of the previous time step. But in fact, they can make a prediction and choose their speed in a more complicated way.

<!-- b000636 | heading | pages [53] -->
References

<!-- b000637 | references | pages [53] -->
[1] Wikipedia. Controlled-access highway. https://en.wikipedia.org/

<!-- b000638 | references | pages [53] -->
wiki/Controlled_access_highway

<!-- b000639 | furniture | pages [54] -->
Team # 26333

<!-- b000640 | furniture | pages [54] -->
Page 53 of 53

<!-- b000641 | references | pages [54] -->
https://en.wikipedia.org/wiki/

<!-- b000642 | references | pages [54] -->
[2] Wikipedia.

<!-- b000643 | references | pages [54] -->
Passing lane.

<!-- b000644 | references | pages [54] -->
Passing_lane

<!-- b000645 | references | pages [54] -->
[3] Nagel, K., & Schreckenberg, M. (1992). A cellular automaton model for

<!-- b000646 | references | pages [54] -->
freeway trafﬁc. Journal de Physique I, 2(12), 2221-2229.

<!-- b000647 | references | pages [54] -->
[4] Rickert, M., Nagel, K., Schreckenberg, M., & Latour, A. (1996). Two lane

<!-- b000648 | references | pages [54] -->
trafﬁc simulations using cellular automata. Physica A: Statistical Mechanics

<!-- b000649 | references | pages [54] -->
and its Applications, 231(4), 534-550.

<!-- b000650 | references | pages [54] -->
[5] Chowdhury, D., Wolf, D. E., & Schreckenberg, M. (1997). Particle hop-

<!-- b000651 | references | pages [54] -->
ping models for two-lane trafﬁc with two kinds of vehicles: Effects of lane-

<!-- b000652 | references | pages [54] -->
changing rules. Physica A: Statistical Mechanics and its Applications, 235(3),

<!-- b000653 | references | pages [54] -->
417-439.

<!-- b000654 | references | pages [54] -->
[6] Knospe, W., Santen, L., Schadschneider, A., & Schreckenberg, M. (1999).

<!-- b000655 | references | pages [54] -->
Disorder effects in cellular automata for two-lane trafﬁc. Physica A: Statisti-

<!-- b000656 | references | pages [54] -->
cal Mechanics and its Applications, 265(3), 614-633.

<!-- b000657 | references | pages [54] -->
http://en.wikipedia.org/wiki/

<!-- b000658 | references | pages [54] -->
[7] Wikipedia.

<!-- b000659 | references | pages [54] -->
Shoulder (road).

<!-- b000660 | references | pages [54] -->
Shoulder_%28road%29

<!-- b000661 | references | pages [54] -->
[8] Chowdhury, D., Wolf, D. E., & Schreckenberg, M. (1997). Particle hop-

<!-- b000662 | references | pages [54] -->
ping models for two-lane trafﬁc with two kinds of vehicles: Effects of lane-

<!-- b000663 | references | pages [54] -->
changing rules. Physica A: Statistical Mechanics and its Applications, 235 417-

<!-- b000664 | references | pages [54] -->
439.

<!-- b000665 | references | pages [54] -->
[9] Anhui Expressway Company Limited Network.

<!-- b000666 | references | pages [54] -->
(2013).

<!-- b000667 | references | pages [54] -->
Trafﬁc

<!-- b000668 | references | pages [54] -->
http://www.

<!-- b000669 | references | pages [54] -->
ﬂow on Tianchang section of the national road 205.

<!-- b000670 | references | pages [54] -->
anhui-expressway.net/enterprise/quarterselect1.aspx?

<!-- b000671 | references | pages [54] -->
Year=2013&RoadID=205%u56fd%u9053%u5929%u957f%u6bb5

<!-- b000672 | references | pages [54] -->
[10] Roess, R. P., Prassas, E. S, & Mcshane, W. R. (2004). Trafﬁc Engineering Third

<!-- b000673 | references | pages [54] -->
Edition. New Jersey: Pearson Education, Inc.

<!-- b000674 | references | pages [54] -->
[11] Sadiq, R., Husain, T., Veitch, B., & Bose, N. (2004). Risk-based decision–

<!-- b000675 | references | pages [54] -->
making for drilling waste discharges using a fuzzy synthetic evaluation

<!-- b000676 | references | pages [54] -->
technique. Ocean Engineering, 31 31(16), 1929-1953.
