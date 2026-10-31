# P-A-2014-30532-8f80536d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #30532                                                                      Page 1 of 29

<!-- b000002 | front_matter | pages [1] -->
Team Control Number

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000004 | front_matter | pages [1] -->
30532

<!-- b000005 | front_matter | pages [1] -->
T1 ________________ F1 ________________

<!-- b000006 | front_matter | pages [1] -->
T2 ________________ F2 ________________

<!-- b000007 | front_matter | pages [1] -->
T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000008 | front_matter | pages [1] -->
A

<!-- b000009 | front_matter | pages [1] -->
2014 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000010 | prose | pages [1] -->
We build a simulation and statistical model to analyze the performance of Keep-Right-Except-To-Pass rule in light and heavy traffic. We extend the famous Cellular Automaton single-lane Traffic flow simulation model (NaSch model) to multi-lane model using our new lane-changing rules. The factor analyze method is employed by us to study the tradeoffs between traffic flow, safety, max velocity limits and other metrics. Besides the Keep-Right-Except-To-Pass rule mentioned in the problem, we also propose two other rules:     Keep-Right-Or-Left rule and High-Velocity-Left -Low-Velocity-Right-Except-To-Pass rule. A deep compare between the three rules has be done. The result shows that when traffic density, the probability of lane-changing and the velocity limits are low, Keep-Right-Or-Left rule is able to promote traffic flow and safety. In general, Keep-Right-Or-Left rule performs the best, while High-Velocity-Left -Low-Velocity-Right-Except-To-Pass rule performs the worst.

<!-- b000011 | prose | pages [1] -->
In countries where driving automobiles on the left is norm, our Keep-Right-Except-To-Pass model is also suitable with a simple change of orientation. Considering the other two models set no limit on the lane in which vehicles drive, the model can be applied without modification to those countries driving to the left.

<!-- b000012 | prose | pages [1] -->
Last, if the whole traffic is controlled by an intelligent system, we will simulate the random behaviors of the model parameters to optimal parameters under ideal circumstances and also analyze the effects to the three rules. Under the control of an intelligent system, the safety of three rules is almost the same. And the rule of Keep-Right-Except-To-Pass promotes the traffic flow the least while the range of difference is the greatest and the other two rules promote the traffic flow to a similar degree that is greater than that promoted by the Keep-Right-Except-To-Pass rule.

<!-- b000013 | furniture | pages [2] -->
Team #30532                                                                      Page 2 of 29

<!-- b000014 | contents | pages [2] -->
Simulating and Scoring the

<!-- b000015 | contents | pages [2] -->
Performance of Traffic Driving Rules

<!-- b000016 | contents | pages [2] -->
Simulating and Scoring the Performance of Traffic Driving Rules

<!-- b000017 | contents | pages [2] -->
SUMMARY ............................................................................................................................................. 3

<!-- b000018 | contents | pages [2] -->
1 INTRODUCTION & BACKGROUNDS ..................................................................................................... 4

<!-- b000019 | contents | pages [2] -->
2 PROBLEM ANALYSIS ........................................................................................................................... 4

<!-- b000020 | contents | pages [2] -->
2.1 Restatement of the Problem ........................................................................................................ 4

<!-- b000021 | contents | pages [2] -->
2.2 Research Method ........................................................................................................................ 4

<!-- b000022 | contents | pages [2] -->
3 ASSUMPTIONS .................................................................................................................................... 5

<!-- b000023 | contents | pages [2] -->
4 MODEL DEVELOPMENT ...................................................................................................................... 6

<!-- b000024 | contents | pages [2] -->
4.1 Multi-lane Traffic Model for Cellular Automaton ...................................................................... 6

<!-- b000025 | contents | pages [2] -->
4.1.1 Single Lane Model .............................................................................................................................. 6

<!-- b000026 | contents | pages [2] -->
4.1.2 A Generic Multi-Lane Model .............................................................................................................. 6

<!-- b000027 | contents | pages [2] -->
4.2 Rule analysis：Keep-Right-Except-Pass Rule ........................................................................... 7

<!-- b000028 | contents | pages [2] -->
4.2.1 Introduction ......................................................................................................................................... 7

<!-- b000029 | contents | pages [2] -->
4.2.2 Simulation Setup ................................................................................................................................. 8

<!-- b000030 | contents | pages [2] -->
4.2.3 Simulation Results and Discussion ..................................................................................................... 8

<!-- b000031 | contents | pages [2] -->
4.3 Comparison of Different Rules ................................................................................................. 15

<!-- b000032 | contents | pages [2] -->
4.3.1 Introduction of Other Rules ............................................................................................................... 15

<!-- b000033 | contents | pages [2] -->
a. Keep-Left-Or-Right Rule ................................................................................................................... 15

<!-- b000034 | contents | pages [2] -->
b. High-Speed-Right-And-Low-Speed-Left-Except-Pass Rule .............................................................. 16

<!-- b000035 | contents | pages [2] -->
4.3.2 Simulation Results and Discussion ................................................................................................... 16

<!-- b000036 | contents | pages [2] -->
4.3.3 Introduction of factor analysis ........................................................................................................... 19

<!-- b000037 | contents | pages [2] -->
4.3.4 Simulation Results and Discussion ................................................................................................... 19

<!-- b000038 | contents | pages [2] -->
4.4 Results and Discussion under Intelligent System ..................................................................... 25

<!-- b000039 | contents | pages [2] -->
5 CONCLUSION .................................................................................................................................... 28

<!-- b000040 | contents | pages [2] -->
6 STRENGTH AND WEAKNESS .............................................................................................................. 28

<!-- b000041 | contents | pages [2] -->
7 REFERENCE ...................................................................................................................................... 29

<!-- b000042 | furniture | pages [3] -->
Team #30532                                                                      Page 3 of 29

<!-- b000043 | heading | pages [3] -->
Summary

<!-- b000044 | prose | pages [3] -->
We build a simulation and statistical model to analyze the performance of Keep-Right-Or-Left rule in light and heavy traffic. We extend the famous Cellular Automaton single-lane Traffic flow simulation model (NaSch model) to multi-lane model using our new lane changing rules. The factor analyze method is employed by us to study the tradeoffs between traffic flow, safety, max speed limits and other metrics. Besides the Keep-Right-Except-To-Pass rule mentioned in the problem, we also propose two other rules: KROL(Keep-Right-Or-Left) rule and HLLR(High-Velocity-Left -Low-Velocity-Right-Except-To-Pass) rule. A deep compare between the three rules has be done. The result shows that when traffic density, the probability of lane-changing and the speed limit is low, KROL rule is able to promote traffic flow and safety. In general, KROL rule performs the best, while HLLR rule performs the worst.

<!-- b000045 | prose | pages [3] -->
In countries where driving automobiles on the left is norm, our Keep-Right-Except-To-Pass model is also suitable with a simple change of orientation. Considering the other two models set no limit on the lane in which vehicles drive, the model can be applied without modification to those countries driving to the left.

<!-- b000046 | prose | pages [3] -->
Last, if the whole traffic is controlled by an intelligent system, we will simulate the random behaviors of the model parameters to optimal parameters under ideal circumstances and also analyze the effects to the three rules. Under the control of an intelligent system, the safety of three rules is almost the same. And the rule of Keep-Right-Except-To-Pass promotes the traffic flow the least while the range of difference is the greatest and the other two rules promote the traffic flow to a similar degree that is greater than that promoted by the Keep-Right-Except-To-Pass rule.

<!-- b000047 | furniture | pages [4] -->
Team #30532                                                                      Page 4 of 29

<!-- b000048 | heading | pages [4] -->
1 Introduction & Backgrounds

<!-- b000049 | prose | pages [4] -->
Driving rules in the world can be categorized into two factions: driving to the left and driving to the right. Nowadays, most of the countries in the world abide by the Keep-Right-Except-To-Pass rule. On the other hand, driving to the left is prevalent and became a basic traffic rule in countries with UK as the representative and those that have undergone the influence of colonial domination. In the 1920s, traffic accident exponentially increased and studies showed that sitting on the right side of the vehicles and driving to the right often led to the blocking of the drivers’ view when they tried to pass other vehicles on the road. In addition, since most of the population in the world lived in the north hemisphere, driving to the right is safer due to Coriolis force. Consequently, most countries, especially those in Europe and America, unanimously decided to implement the rule of sitting on the right side of vehicles and driving to the right. Today, almost 4 billion people around the world drive on the right side of the road while 2 billion drive on the left.

<!-- b000050 | prose | pages [4] -->
This paper intends to develop a mathematical model for the mainstream Keep-Right-Except-To-Pass rule and analysis the changes on traffic flow and safety brought about by various variables. A comparison with other traffic rules will be made to evaluate the strengths and weaknesses of different rules. Furthermore, a quantitative analysis will be carried out on to determine which of these rules outshines the others.

<!-- b000051 | heading | pages [4] -->
2 Problem Analysis

<!-- b000052 | heading | pages [4] -->
2.1 Restatement of the Problem

<!-- b000053 | prose | pages [4] -->
First and foremost, driving automobiles on the right is the rule in most countries unless the drivers need to pass another vehicle, in which case they move one lane to the left, pass, and return to the right-most lane. This paper intends to analyze:

<!-- b000054 | prose | pages [4] -->
1. The rationality of this rule from the perspectives of safety and promotion of traffic flow under the circumstances of different traffic loads or speed limits.

<!-- b000055 | prose | pages [4] -->
2. The effectiveness of this rule in promoting better traffic flow? If its effectiveness is low, suggest alternatives.

<!-- b000056 | prose | pages [4] -->
3. The effect on the solution once the rule is changed to “Keep-Left-Except-To-Pass”.

<!-- b000057 | prose | pages [4] -->
4. The changes need to be made of the earlier analysis if vehicle transportation on the same roadway was fully under the control of an intelligent system.

<!-- b000058 | heading | pages [4] -->
2.2 Research Method

<!-- b000059 | prose | pages [4, 5] -->
First, the performance of this rule is indicated by safety and traffic flow; therefore, it is a must to pin down measurable parametric factors related to tradeoffs between traffic flow and safety as well as the ways in which this rule performs under different load conditions. Load and speed of vehicles will be held as independent variables while the parametric factors will function as dependent variables and the evaluating indicators of the performance of the rule. In addition, a reference model for comparison will be established and used for evaluating the Keep-Right-Except-To-Pass rule.

<!-- b000060 | furniture | pages [5] -->
Team #30532                                                                      Page 5 of 29

<!-- b000062 | prose | pages [5] -->
In case this rule, compared with the reference group, is not capable of promoting traffic flow, a new driving rule will be drafted against the yardstick of previously-stipulated evaluating indicators to ensure a better performance. The analyzing procedure can be illustrated by the flowchart below:

<!-- b000063 | prose | pages [5] -->
The performance of rule

<!-- b000064 | prose | pages [5] -->
Light traffic Heavy

<!-- b000065 | prose | pages [5] -->
Density

<!-- b000066 | prose | pages [5] -->
Number of lanes Max speed limit

<!-- b000067 | prose | pages [5] -->
Vehicle types Random brake probability

<!-- b000068 | prose | pages [5] -->
… Traffic flow Safety

<!-- b000069 | prose | pages [5] -->
… Velocity Lane change

<!-- b000070 | prose | pages [5] -->
The performance of The Keep-Left-Except-To-Pass rule can be compared with that of the Keep-Right-Except-To-Pass rule once the rule is changed in analog simulation and the outputs of the two calculations are obtained.

<!-- b000071 | prose | pages [5] -->
It is a limiting case if vehicle transportation on the same roadway was fully under the control of an intelligent system, which rules out the random cases ; thus the third question can be addressed by following the method in previous questions and compare distinct outputs for difference.

<!-- b000072 | heading | pages [5] -->
3 Assumptions

<!-- b000073 | prose | pages [5, 6] -->
 All vehicles involved are assumed to be to be under ideal condition and the road in the analysis in the analysis is also ideally flat. Besides, all vehicles drive straightly forward all the time with no direction change, rollover or sway.

<!-- b000074 | furniture | pages [6] -->
Team #30532                                                                      Page 6 of 29

<!-- b000076 | prose | pages [6] -->
 When under the circumstances of change lanes, the acceleration and deceleration processes of the vehicles will not be taken into consideration. If the lane-changing conditions are satisfied, the vehicles will directly shift to the adjacent lane.

<!-- b000077 | heading | pages [6] -->
4 Model Development

<!-- b000078 | heading | pages [6] -->
4.1 Multi-lane Traffic Model for Cellular Automaton

<!-- b000079 | heading | pages [6] -->
4.1.1 Single Lane Model

<!-- b000080 | prose | pages [6] -->
We extend the famous Nagel-Schreckenberg(NaSch)[3] single lane model to multi-lane model to simulate the traffic flow by defining our traffic rules.

<!-- b000081 | prose | pages [6] -->
For the convenience of the readers we would like to outline the single lane model. The system consists of a one dimensional grid of L sites with periodic boundary conditions. A site can either be empty, or occupied by a vehicle of velocity zero to vmax. The velocity is equivalent to the number of sites that a vehicle advances in one update ——provided that there are no obstacles ahead. Vehicles move only in one direction. The index i denotes the number of a vehicle, x(i) its position, v(i) its current velocity, vd(i) its maximum speed, pred(i) the number of the preceding vehicle, gap(i) := x(pred(i)) − x(i) − 1 the width of the gap to the predecessor. At the beginning of each step the rules are applied to all vehicles simultaneously (parallel update, in contrast to sequential updates which yield slightly different results). Then the vehicles are advanced according to their new velocities.

<!-- b000082 | prose | pages [6] -->
• IF v(i) !=- vd(i) THEN v(i) := v(i) + 1 (S1)

<!-- b000083 | prose | pages [6] -->
• IF v(i) > gap(i) THEN v(i) := gap(i) (S2)

<!-- b000084 | prose | pages [6] -->
• IF v(i) > 0 AND rand < pd(i) THEN v(i) := v(i) − 1 (S3) S1 represents a linear acceleration until the vehicle has reached its maximum velocity vd. S2 ensures that vehicles having predecessors in their way slow down in order not to run into others. In S3 a random generator is used to decelerate a vehicle with a certain probability of modeling erratic driver behavior.

<!-- b000085 | heading | pages [6] -->
4.1.2 A Generic Multi-Lane Model

<!-- b000086 | prose | pages [6] -->
The single lane model is not capable of modeling realistic traffic situation mainly for one reason: a realistic fleet is usually composed of vehicle types having different desired velocities. Introducing such different vehicle types in the single lane model only results in slow vehicles being followed by faster ones and the average velocity reduced to the free–flow velocity of the slowest vehicle.

<!-- b000087 | prose | pages [6] -->
We extend the NaSch model by using several parallel single lane models with periodic boundary conditions and additional rules defining the exchange of vehicles between the lanes. The update step is split into two sub-steps:

<!-- b000088 | furniture | pages [7] -->
Team #30532                                                                      Page 7 of 29

<!-- b000089 | prose | pages [7] -->
1. Check the exchange of vehicles between the two lanes according to the new rule set. Vehicles are only moved sideways. They do not advance. Note that in reality this sub-step in this regard seems unfeasible since vehicles are usually incapable of pure transversal motion. Only when being together with the second sub-step to do our update rules make sense physically. This first sub-step is implemented as a strict parallel update with each vehicle making its decision based upon the configuration at the beginning of the time step.

<!-- b000090 | prose | pages [7] -->
2. Perform independent single lane updates on both lanes according to the single lane update rules. In this second sub-step the resulting configuration of the first sub-step is used.

<!-- b000091 | prose | pages [7] -->
According to the rule set used to guide the lane change, we can have different Multi-Lane traffic flow model. We have implemented the Keep-Right-Except-Pass rule which is used in most countries. To find out more effective traffic rules, we also implement the KROL rule and the HLLR rule, which we will cover in the next sections in detail.

<!-- b000092 | heading | pages [7] -->
4.2 Rule analysis：Keep-Right-Except-Pass Rule

<!-- b000093 | heading | pages [7] -->
4.2.1 Introduction

<!-- b000094 | prose | pages [7] -->
'L the index of Technically, we use L to represent the index of current lane, and the target lane. Note that the index of lane increases from the right-most lanes to the left-most ones. We keep using gap(i) for the number of empty sites ahead in the same lane, and add the definitions of gap0(i) for the forward gap on the other lane, and gap0,back for the backward gap on the other lane. Note that if there is a vehicle on a neighboring site both return -1.

<!-- b000095 | prose | pages [7] -->
The Keep-Right-Except-Pass rule stipulates that a vehicle i changes to the other lane if all the following incentive, safety and Stochastic conditions are satisfied: Incentive Condition:

<!-- b000096 | prose | pages [7] -->
'L L  (T1) or

<!-- b000097 | prose | pages [7] -->
'L L  and gap ( i )  iv  1 (T2)

<!-- b000098 | prose | pages [7] -->
Safety Condition:

<!-- b000099 | prose | pages [7] -->
gap ( i )  iv  1 (T3) 0

<!-- b000100 | prose | pages [7] -->
(T4) gap ( i )  v ,0 back max

<!-- b000101 | prose | pages [7] -->
Stochastic condition

<!-- b000102 | prose | pages [7, 8] -->
rand() < Pchange (T5) Incentive Condition models the desire of a driver to change lane. There are two conditions, either T1 or T2 is met then the incentive condition is found: T1, if the driver is on the left lane, according to the traffic rule, he/she should have the desire to change to right lane; T2, if the driver is on right lane and there is another vehicle ahead, if he/she can get a greater speed when changing lane, then there is an incentive to change lanes. T3 and rule T4 ensure that the lane change is safe and does not ensue a sudden brake from an approaching vehicle.

<!-- b000103 | furniture | pages [8] -->
Team #30532                                                                      Page 8 of 29

<!-- b000105 | prose | pages [8] -->
T5 shows that lane changes are made with probability LCP to simulate the unlikelihood of a driver’s lane-changing move whenever possible.

<!-- b000106 | heading | pages [8] -->
4.2.2 Simulation Setup

<!-- b000107 | prose | pages [8] -->
In our simulation, each time step represents one second. We separate the lane into many road sections(sites), with each road section representing 7.5 meters of a lane and can be occupied by one vehicle at a time or be empty. 7.5 meters is selected since it is the approximate length of one vehicle as well as the distance between two stopped vehicles. Each of our lanes consists of 133 road sections. With 133 sections, each of our lanes is effectively 997.5 meters long. Our lanes are modeled as a closed system, making our road a loop. If a vehicle reaches the end of the road, it will loop back to the start.

<!-- b000108 | prose | pages [8] -->
Before the simulation starts, the simulation road is populated according to the given density, and each vehicle is placed randomly on the road with a random velocity equal to or less than their maximum velocity.

<!-- b000109 | prose | pages [8] -->
In our experiments the RBP (random braking probability) is set to 0.2, with LCP (lane changing probability) to 0.9 and vmax and vthresold to 5 and 4 respectively.

<!-- b000110 | heading | pages [8] -->
4.2.3 Simulation Results and Discussion

<!-- b000111 | prose | pages [8] -->
Through numerical simulation, we can obtain the average density, speed and flow of the traffic. The model under experiment assumes the road to be a loop. The flow rate Q can be calculated if the total number of the laps that all vehicles have run is represented by S, the total simulation time by T and the number of lanes by L.

<!-- b000112 | prose | pages [8] -->
  =  ∗ The density is defined as：  =  2 The average speed is defined as：    1 =  ∗    
,,   

<!-- b000113 | prose | pages [8] -->
In the above formula, V,, represents the speed of vehicle j driving in Lane i at

<!-- b000114 | prose | pages [8] -->
the time of t.

<!-- b000115 | prose | pages [8, 9] -->
The average totality of lane-changing can be defined as：  = 1     c in this formula represents the total number of times lane-changing happens with a range of time t.

<!-- b000116 | furniture | pages [9] -->
Team #30532                                                                      Page 9 of 29

<!-- b000118 | prose | pages [9] -->
The average rate of lane use U is defined as：   = 1   ,  N, represents the number of vehicles on the road at the time of t.

<!-- b000119 | prose | pages [9] -->
We analyzed the effects on the traffic flow, the times of lane-changing and average speed brought about by these six factors: traffic density, number of lanes, maximum speed limit, the proportion of large vehicles, lane-changing probability and the probability of random braking. The simulated results of car track can be described into the following Time-Space chart, and the numbers express the velocity of car.

<!-- b000120 | prose | pages [9] -->
Space

<!-- b000121 | prose | pages [9] -->
40.10.1..20.0.0..1..2..2...2..2.....4........5...........5.....5.......4......5........4......3..2.1.1.1.............4....4.....5... ...0..1..2...3....4......4.....5....4....4.......4.....5.......5....4............4........5...0.00.1..2.......4..2..2....2.....4..... 40.10.1..20.1.1.1...2..2...3..2...3.......5.......4............5.....5.......5......5........5...2.1.10...2..............3......5.... ....1..1....3...3......5......5...3.....4.....5.......5.....5......4.....5...........4.......3.100...2..2.......2.1....3....3.......5 0.10.1..20.1.1.1..2...2...3..2...3....4........5.......5............5.....5.......5......5......3.1.10.1....2................4.....3. ...4..2..2.....3....4.......5....3...3......4......5.......5.....5......5....4............5...100.1....2...3....0..1.......4....4.... .10.1..20.10.0...2...3..2...2...3...3......5........5.......5............5.....5.......5......5..10.0.1..2....2...................5.1 5...1...2...3......4.....5......4...3....4.......5.....4........5.....5.....4.....5..........300.1.1......3....4.1...2.........4..... 10.1..20.100..1.....3..2...3...3...3....4.......5........5.......5............5.....5.......5...20.1.1..2..2.....3.................1. ...3.1.....3....4.......5.....5....3....4.....5.......5.....5........5.....5.....5.....5.....00.10...2.......3..1..2....3...........5 0.1.1.0.100.1..1......2...3...3...3....4.....5.......5........5.......5...........4......5.....30.1.1..2..2...3......4..............1 ..3.1..2.......4.....5.......5....4....4.....5.....5.......5.....5........5.....5.....5.....500.0.1.....3.....1...2..2......4........ .1.1.1.1000..1...2.......3..2....3....4.....5.....5.......5........5.......5...........5......50.1.1..2..2..2.....4.......5.........0 ..0...2..2..........5.....5......4...3......5....4......5......4......5........5.....5.....500.1.1.1........4...2...2...3........5... 1.1.1.1000.1...2....3......2...3....3.....4.....4......5......4.........5.......5...........5.0.1.1..2..2.1...2........5.......5..... .5.1....2...3...........4......5....3....4......4.....5......5......5......5........5.....500.1.10...2.........3...3...3....4........ .1.10.000.1..2....3....3......3...3.....4......5.....5......5......5........4........5.......1.10..1..1..1..2....3..........5.......5 .0...2.....3....4............5....3.....4.....5......5.....5.....4.......5......5........500.1.10.1.....3.........3...3....4....4.... 1.10.100.1..2...3....3....3......3....4......5......5.....5......5......5........5........5...10.1..1...2.1....3.....4...........5... 5.1.....3......4....4............4....4......5.....5......5.....5....4........5.....4....000.0.0.1.1........4.......2.....4....4..... .100.00.1..2..2.....4...3....3......3......5......5......5.....5.....4.......5.......4.......30.1..2..2..1..2......4......5.........3 .1..2.......4......4.....5..........3.....4.......5.....5......5....4....4.........5....4000..1.1.1.1............5.....3......4....4. 100.100..1...2...3.....3....4....4......4.......5......5......5.....5.....5.......5.......5..0.1..2..2..2..2............5......5..... 2..2...3.........5.....4......5........3.......5.......5....4.....3....3......5........4000.1..1.1.1..2........3......5....4.....3... 00.100.1..1.....3....4.....4....4.....5......5.......5.....4.......5.....5.....5......4.....2.1..2..2..2..2...3..............5......5 ..2...3....4..........5.....5......5.......4........5......4....4.....4...3........5...0000...20..1.1....3.........4......4.....5..2. 0.100.1..2..2.......4.....5...3.....4......5......5.......5.....5.......5....4......5......5.1..2.1...2..2..2....3................5.0 .3...3....4.....5..........5.....5......5.......5........5.....4....4....3....4.......3000.1..00...1..2......4..........5......5.1... .100.1.1...2..2.........4....3...3......4.......5......5.......5.....5......4.....5......5..1..2.1.1...1...2...3.....4............0.0 ...2.....4.....5.....5..........5....4.......5.......5........5....4....4....4.....5..000.1.1.00.....2...3........5.........4...1..2. 100.10...2...2..2...........4...3....4.......5.......5......5.......5.....5.....4......5...2..2.1.1..2...2....3....4......5........1. .3....3.......5.....5.....5.........4....4........5.......5.......4....4....4.....5..200.1.1.100........3....4.........5.......3..2.. 00.10.1....2...2...3...........3....4.....5.......5.......5......5.......5.....5....4.....3..2.1.1..2...3...3.....4.....5......5....1 3....4....4........5.....5.....5.......3.....4.........5......4.......4....4.....5..200.10..1000............4.....5.........5....2... 0.10.1..2.....3...3....4..........3......5.....5.......5.......5.....4.......4.....4.....5..2.10...2...3...3....4......5.....5.....40 ....4...3......5........5.....5.....5......4......5.........5.....4.......4.....5..200.100..000.1................5....4.........4...3 0.0.1..2...3.....3....4.....5.........4.......5.....5......4........5.....5.......5.....5..20.0.1.....3...3....4.....5......5.....500 ..3....3....4.......5........5.....5....4.......5......5.........5.....5......4..1.00.100.1.00.1..2..................4.....5.......3. .1.1..2..2....3......4.....5....4..........5.......5.....5......5........5.....5.......5..20.10..1........4.........5....4.......5000 .3....4....4....4........5........5....4.....5.......5......5.........5.....5...20.00.00.1.10.1..2...3........4...........5.....5.... 1.1.1..1...2......4.......5....4.....5..........5.......5....4.......5........5.....5....20.10.1...2...........5........4.....5..000. 5...3.....4....4....4........4........4....4......5.......5......5........4....30.10.10.10.0.1..2...3....4.........5...........5..... 0..1..2.1.....3........5......4.....5....4...........5......4.....5.......5........5...3.0.100...2....3.............5........5..2000. ...3....4.....4....4.....5........5.......4.....5......5.......5......5.......400.0.10.10.1.1.1....3....4.....5........4............5 .1...2.1..2.......4........4......4....3......5...........5......5.....5......4.......3.1.1000.....2......4..............5....1.000.1 ..3....4....4....3......5.....5........5......4......5......5......4.......5..00.1.10.100..1.1.1.......4....4......5........5........ 1..2..1.1....3........4.........5.....4....4......4............5.....4......5......5...1.1000.1.......3........5.............4.1000.. ......4....4....4....4......4......5........5......5......5.....4......4.....20.1.10.1000..0..1.1..........4....4.......5........5... ..2..2.1.1.......4.........5.........5....4.....5......5............5....4......4.....3.1000.1.1..........4.........5.........1000.1. .5........4....4....4.....5......5.....4........4.......5......5.....5......500.0.0.1000.1..1..1..2............4.....5.......5....... 2...2.1.1..2..........5.........5........4....4......5......5...........4.....5......5.1000.1.1..2............4.........4.....000.1.. ......5.......4...3.....4......5......5.....5........5......4.......5.....5.000..1.1000.1..2..2..2...3..............5.....5.......5.. ..2..1.1..2...3............5.........5......3......5......5......5...........5....4...10000..1..2...3..............5.........5000...2 ..5.......4......3....4......5......5......5.....5........5......5......4..100.1..1000.1..2..2..2...3....4...............5....4...... .2.1..1..2...3...3..............5.........5.....4.......5......5......5..........4...30000.1...2...3....4...............5....000.1... .......5.......5.....4.....5......5......5......5....4........4.......5...200.1..2000.1.1...2..2...3....4.....5.............3......5. ..1.1...2...3...3....4..............4..........5.....5.......5......5......5........30000.1..2....3....4.....5.............3.00.1..2. ...5.......4........5.....5.....5.....4.......5.....4.....5.......4.....2.000...2000.1.1..2..1....3....4.....5.....5............4.... .3.1..2....3...3....4....4...............5.........4......5.......5......5......5...0000.1.1....3.....4.....5.....5..........20...2.. ........5.......5.......4......5.....5.....5.......5....4.....4........50.00.1..000.1.1..2.1..1......3......5.....5.....5.....1.....4 ..1.1...2.....3....4....4.....5..............4..........5......5.......5......5....3000.10..1.......4......5.....5.....5.....0.1....2 ....5.......4........5.......5......5.....5.....5......4.....5.....5...0.10.1..200.1.1..2.1.1...2........4.......5.....5.....5.1..... .2.1.1.....3......4....4.....5.....5..............5..........5......5.......5....3.000.10.1...2..........5......5....4......5.1..2... .........5.......5........5.......5......5....4.....4.......5....4....3.10.1..200.1.1..2.1.1..2....3..........5.......5.....5.1..2... .0..1..2.......4......4.....5.....5.....5..............5..........5......5......4.100.10.1..2....3............5.....4.....5..1..2...3 ..............5......4.........5.......5.....4.....5.....5......4....40.0.1..200.1.1.1..10...2...3.....4...........5.......50...2..2. 10....2.............5......5.....5....4......5..............5.........4.......5..100.100...2...3.....4.............5.....5..2.1...2.. .3........3........5......5.........5.......5.....5.....5.....5.....40.10...200.1.1.1.1.0.1.....3...3......4............5..00.....2.. Time 0.1......3...............5......5....4....4.......5..............5.........5....200.1000......3....4......5.............5..2.1..2..1. 3...3........3.........4.......5.........5......4......5.....5.....50.10.1..000..1.1.1.1.1.1.......3....4.......5.........20.1....... .1..2........4................5.....4....4.....5.......5..............5........400.10000..........4.....5.....4...........2.1.1...20. ...3...3.........4..........5.......5.........5......5......5.....50.10.1..200.1..1.1.1.1.1..2.........4.....5.......5....0.1..2..... ...2..2...........5................5....4.....5.....5.......5..............5...00.100000...............5.....5.....5.......10..1..0.1 ......3....4..........5..........5.......5.........5......5......50.100...200.1..20..1.1.1..2...3..........4......5......40...2...3.. .2...2...3.............5...............4.....5.....5.....5.......5............300.00000.1..................4......5.....5..0.1...2.1. .4........4.....5..........5..........5.......5.........5......5.0.100.1..00.1.1.0.1..1.1..2..2....3............5......5.0.1.....3... 2...3...3....4..............5...............5....4......5.....5......4.....1..00.100000...2.....................5......5..20...2.0... ......5........5.....5..........5..........5.......5.........5..1.100.1..2..1.1.1.1..2.1.1...2...3.....4.............5..1.1.1.......3 ...3...3...3......5..............5..............4.....5......5.....5.....4...20.100000.1.....3.......................5..1.0.1...1.1.. ...4.......5........5.....5..........5..........5.......5......20.00.1..2..2.1.1.1..20..1..2....3....4......5.........1..1.1..2...... ......3...3....4.......5..............5..............5.....5......5.....5...30.1000000...2.......4.....................2.1.1..2.0...2 ........5.......5........5.....5..........5..........5.......5.0.10.1.1...2.10..1..20.1...2...3.....4.....5......5......2.1..2...3... ..3......3....4.....5......4...............5..............5.....5......5...30.1000000.1.....3.........5.................1.1..2.1.1... 4............5.......5........5.....5.........4...........5...1.100..1..2..10.1...20.1..2...2.....4......5.....5......5.0...2...3.... ......4......4.....5....4.......5...............5..............5....4.....30.1000000.1..2.......4..........5.............1..2.1.1..2. .....5............5.......5.......4......5.........5.........3.100.1...2..20.1..2.0.1..2...3...3.......5.....4......5..1.1.....3....4 .3.........5......5....4.....5.......5...............5.............4.....50.1000000.1.1....3.........5.........4..........1..1.1.1... ...4.....4............4........5.......5......5.........5.....100.1..2..1.0.1..2.10...2...3...3...3........4......5...2.1..2.......4. .....4..........5.....4.....5.....5.......5...............5....1.......4.0.1000000.1.1..2.....3...........5.........5......1..1.1..2. ..4.....5.....5............5........5.......5.....4..........5.0.1..2..2.10...20.00......3..2....3....4........4.....3.1..2...3...... .3........5.........4......5.....5.....5.......5..............4..2.....0.0.000000.1.1..2..2.......4...........4..........5...2.1.1... .......5.....5.....5............5........5.......5....4.......1.1..2..2.10.1..0.10.1......1....3.....4.....5.......4..1..2...3....4.. ....3..........5.........5......5.....5.....5.......5...........2...3...10.00000.1.1..2..2...3.........5...........5.......2..10..1.. ..5.........5.....5....4.............5........5......4.....5...1..2..2.10.1..20.0.1..2......2.....3.......5.....5...1...2...3....4... ........4...........5.........5......5....4.....4........5........2....30.10000.1.1..2.1....3....4..........5..........4....1.0.1..1. .5.....5.........5....4.....5.............5.......4.......5...3.1...2.10.1..200..1..2...3......3......4........5...3..2...2.....4.... 2............5..........4..........5.....4.....5.....5........5......3.0.10000.1.1..2.1..2......4....4...........5.........4.1.1.1... 5.....5.....5........4.....5.....5.............5.......5.....30...2.0.0.1..200.1..1....3...3.......4.......5.....2...2...3...3....... ...3..............5..........5..........5.....5.....5.....5.......4...1.100000..1..2.1..2...3......3......5...........5.....10..1..2. .....5.....5....4.........5....4......5.............5.......50.1...1.10...200.1..2..2....2.....4........5.......5...3..2....3....4... 2......4........5......5..........5.........4......5.....5....4......30.00000.1...2.1..2..2.....4......4.......5...........50.1...2.. .5........5..........5........4.....5......5.............5..0.1..2..10.1..000...2..2...3...2........5.......4......3.1....3.....4.... ...3........5........5......5..........5.........5......5....4.....5.0.10000.1..2..1..2.1...2........5......5......4.......0.1..2..1. 5....4.........5..........5.......4......5......5..........2.1..2..200...200.1....2...3...3..2..........4........5..1..2......4...... 2......4.........5........5......5.........4..........5.....4....4..1.100000...2..2..2.1..2....3..........5......5......5...1..2.1... ...3......5.........5..........5.......5......5......5......1..2..2000...00.1..2.....3..2...2..2.............5....1...2...3........5. ..2........4..........5........5......5.........5..........5....4..20.00000.1...1...2.1.1....3.....4..........4......4.....3.1..1..2. ..4....4.......5.........5..........5.......5......5......5...2..20000...0.1..2...3....2...3..2...3.............3...2....3...3....... 2....3..........5..........5........5......5........4..........4..20.10000.1.1....2..1.1..2......4.....4...........5......5.1..2..2.. ......4....4........5.........5..........5.......5......5...2..1.0000.1...1..2...3....4...3.1....3....4............3...3....3....4... ...3.....4...........5.........4.........5......5........5.......20.10000.1.1..2....20...2...3.......4......5...........5..1.1...2..2 .5........4.....5........5.........5..........5.......5....3..2.1000.1..2...2...3....4...3.1..2......4.....5..........3...3.....4.... ..3....4.....4............5.........5.........5......5........5..0.10000.1.1..2...3.0.1.....3....4.......4.......5........2.1..2...2. 5.....5........5.....5........5........4..........4.......4..2.1000.1..2...3...3....4...3.1..2...3.......4.....4.........3....4...... .3....4.....5.....5............5........4..........5......5....1..10000.10...2..2..1.1..2......3......5.......5......4.....1.1....3.. .....5.....5........5.....5........5........5..........5....2.1000.1..2...3..2.....4...3.1..2...3....4........5.....5........4.....5. 3...3......5.....5.....5............5........5.........4......4..20000.10.1....2..20...2...3......3........5.......5......5.1..2..... ...5......5.....5........5.....5........5........5........3..1000.1..2...3..2...3....2..1..2...3....4.....5........5.....5........5.. ..2.....4.......5.....5.....5...........4........4..........5...20000.10.1..2....20.1.....3....4.....3..........5.......5..1.1....3.. ..5.....5......5.....5.......4......5........5........5....1.000.1..2...3.1...2.....4..2..2..2....3......5.....5........5.....5...... .4...3.......5.......5.....5.....5...........5........5.......2.0000.10.1..2...3.0.1..2.......4....4.....4..........4.....2.1..2..... .......5.....5......5.....5......4.......5........5......3..100.1..2..2..1.1....2.....2..2.1....3.....4......4......5........5.....5. ....3....4........5.......5....4......5...........5........5...1000.10.1..2...3.10...2...3........4.....5.....5.........4..1.1....3.. ...5........5.....5......5.....5.....4.......4.........5..1.000..1...2..2.1..2.....3....2.1..2......4......5......5......5.......4... .4......4.....5........5......4....4......4...........4.......3000.10.1..2...3.10.1.....3....4.........5.....5.....5......2.1..2..... .5......5.......4.....4.......5.....5.....5.......5.....1.0.00.1..1....2.1..2...3......4.1..2...3........5......5......5......5...... ......5......5.....5........5.....4.....5......5...........5..000.10.1..2...3.10.1.1........4.....5.........5.....5.....5..1.1....3.. .....4......4........5.....5.......5.....5.....5.......5.1.10.1..2..2...1..2...3....4..0..1....3....4.........5......5......5.....4.. .4.........5......5.....5........5....4......5.....4.........200.10.1..2...30.0.1.1..2...........5.....5.........5....4...20...2..... ..5.......5......5.......4......5.......5....4......5...1.10.1..2..2...3..2...3....4..2.1...2......4.....5.........5......5......5... .....4..........5......5....4........4.....5......5.....5....00.100...2...30.1.1.1.1....3.............5.....5........4..2.0.1.....3.. .5.....5.......5......5.......5.....4.......4.....5...2..10.1..2..2...3.1....3....4.1..1..2....3.......4......5.........5......5..... .4.......4..........4.....3......5.......4......5......5...3.0.100.1.....30.10..10...2......4..............5.....5.....2.10...2...... ......5.....5.......5......5.......5.....5.......5...3..20.1..2..2..2..1..2......4.1..2..2...3.....4........5......5.........5......5 ......5......4...........5....4.......5.......5......5...2..1.100.1..2...0.100..0.1.....3........5..............5.....5.10.1.....3... ....5......5.....5.......5......5.......5.....5.....3..20.1..2..2..2..2..2...3....1..2.1....3....4......5........5......5.........5.. 4..........5......5.........3.....4........5.......5...2...20.00.1..2..2..100.1..1.1........4.........5..............5.10.1..2....... ..5......5......5....4........5......5.......5.....5..20.1..2..2..2..2..2...3....4..20...2......4.....5......5........5......5....... .....5..........5.....4.........4......5........5....2....30.10.1..2..2..200.1..2.1..2...........5.........5..........10.1..2...3.... .......5......5.....4.....5.......4.......5......4..1.0.1.1...2.1...2..2...3....4..20.1.....3........5.....5......5.......4.......5..

<!-- b000122 | caption | pages [9] -->
Figure 1: Track Time vs. Space

<!-- b000123 | prose | pages [9] -->
We can find that traffic jam is generated after a period of time. And the jam in one road can be reduced by another load.

<!-- b000124 | furniture | pages [10] -->
Team #30532                                                                      Page 10 of 29

<!-- b000125 | prose | pages [10] -->
a. Density vs. Flow, Lane Changing Frequency and Average

<!-- b000126 | prose | pages [10] -->
Velocity

<!-- b000127 | prose | pages [10] -->
We vary the vehicle density form 0 to 1, and get the corresponding traffic flow、 lane changing frequency and average velocity.

<!-- b000128 | caption | pages [10] -->
Figure 2.b: Density vs. Lane Changing

<!-- b000129 | caption | pages [10] -->
Figure 2.a: Density vs. Flow

<!-- b000130 | prose | pages [10] -->
Frequency

<!-- b000131 | caption | pages [10] -->
Figure 2.c: Density vs. Velocity

<!-- b000132 | prose | pages [10] -->
The figures show that with the density increasing, flow and lane changing frequency both first increase then decrease, the average velocity has a decrease trend. In fact, when vehicle density increases, the number of vehicle is increase, and car flow is increasing, when flow reach top, increase density will cause the flow decrease because high density cause jam, and the vehicle velocity is decrease.

<!-- b000133 | prose | pages [10, 11] -->
Lanes vs. Flow, Lane Changing b. Number of Frequency and Average Velocity

<!-- b000134 | furniture | pages [11] -->
Team #30532                                                                      Page 11 of 29

<!-- b000136 | prose | pages [11] -->
We vary the lane number from 1 to 8, and get the corresponding traffic flow、lane changing frequency and average velocity.

<!-- b000137 | caption | pages [11] -->
Figure 3.b: Lanes vs. Lane Changing

<!-- b000138 | caption | pages [11] -->
Figure 3.a: Lanes vs. Flow

<!-- b000139 | prose | pages [11] -->
Frequency

<!-- b000140 | caption | pages [11] -->
Figure 3.c: Lanes vs. Velocity

<!-- b000141 | prose | pages [11] -->
Obviously, flow、lane changing frequency and average velocity all increase with the lane number. In reality, most freeways are 4-lane or 6-lane.

<!-- b000142 | prose | pages [11] -->
c. Maximal Velocity Limit vs. Flow, Lane Changing

<!-- b000143 | prose | pages [11] -->
Frequency and Average Velocity

<!-- b000144 | prose | pages [11] -->
We vary maximal velocity limit from 1 to 10, and get the corresponding traffic flow, lane changing frequency and average velocity.

<!-- b000145 | furniture | pages [12] -->
Team #30532                                                                      Page 12 of 29

<!-- b000146 | caption | pages [12] -->
Figure 4.b: Max Velocity Limit vs. Lane

<!-- b000147 | caption | pages [12] -->
Figure 4.a: Max Velocity Limit vs. Flow

<!-- b000148 | prose | pages [12] -->
Changing Frequency

<!-- b000149 | caption | pages [12] -->
Figure 4.c: Max Velocity Limit vs. Velocity

<!-- b000150 | prose | pages [12] -->
We can find that at first, flow and average velocity both increase with the max velocity, while lane changing frequency decrease with the max velocity. When reach a certern maximal velocity, all the three metrics keep stable.

<!-- b000151 | prose | pages [12] -->
d. Big Car Fraction vs. Flow, Lane Changing Frequency

<!-- b000152 | prose | pages [12] -->
and Average Velocity

<!-- b000153 | prose | pages [12] -->
We vary big car fraction from 0 to 1, and get the corresponding traffic flow、lane changing frequency and average velocity.

<!-- b000154 | furniture | pages [13] -->
Team #30532                                                                      Page 13 of 29

<!-- b000155 | caption | pages [13] -->
Figure 5.b: Big Car Fraction vs. Lane

<!-- b000156 | caption | pages [13] -->
Figure 5.a: Big Car Fraction vs. Flow

<!-- b000157 | prose | pages [13] -->
Changing Frequency

<!-- b000158 | caption | pages [13] -->
Figure 5.c: Big Car Fraction vs. Velocity

<!-- b000159 | prose | pages [13] -->
We find that big car fraction mainly influence the lane changing frequence.

<!-- b000160 | prose | pages [13] -->
When big car fraction is less than 20%, lane changing frequency increases, after that, lane changing frequency decrease.

<!-- b000161 | prose | pages [13] -->
e. Lane Changing Probability vs. Flow, Lane Changing

<!-- b000162 | prose | pages [13] -->
Frequency and Average Velocity)

<!-- b000163 | prose | pages [13] -->
We vary lane changing probability from 0 to 1, and get the corresponding traffic flow、lane changing frequency and average velocity.

<!-- b000164 | furniture | pages [14] -->
Team #30532                                                                      Page 14 of 29

<!-- b000165 | caption | pages [14] -->
Figure 6.b: Lane Change Probability vs. Lane

<!-- b000166 | caption | pages [14] -->
Figure 6.a: Lane Change Probability vs. Flow

<!-- b000167 | prose | pages [14] -->
Changing Frequency

<!-- b000168 | caption | pages [14] -->
Figure 6.c: Lane Change Probability vs.

<!-- b000169 | prose | pages [14] -->
Velocity We find that with the increase of lane changing probability, flow and average velocity keep increase until lane changing probability reach 0.1. While the lane changing keeep increase all the time.

<!-- b000170 | prose | pages [14] -->
f. Random Braking Probability vs. Flow, Lane Changing

<!-- b000171 | prose | pages [14] -->
Frequency and Average Velocity)

<!-- b000172 | prose | pages [14] -->
The influence of random braking probability to flow、lane changing frequency and average velocity.

<!-- b000173 | prose | pages [14] -->
We vary random braking probability from 0 to 1, and get the corresponding traffic flow、lane changing frequency and average velocity.

<!-- b000174 | furniture | pages [15] -->
Team #30532                                                                      Page 15 of 29

<!-- b000175 | caption | pages [15] -->
Figure 7.a: Random Braking Probability vs.

<!-- b000176 | caption | pages [15] -->
Figure 7.b: Random Braking Probability vs.

<!-- b000177 | prose | pages [15] -->
Flow Lane Changing Frequency

<!-- b000178 | caption | pages [15] -->
Figure 7.c: Random Braking Probability vs.

<!-- b000179 | prose | pages [15] -->
Velocity We can see that with the random braking probability increase, flow and average velocity decrease and the lane changing frequency first increase then decrease. In fact, when random braking probability increase, the vehicle will decrease which will cause the flow decrease.

<!-- b000180 | heading | pages [15] -->
4.3 Comparison of Different Rules

<!-- b000181 | heading | pages [15] -->
4.3.1 Introduction of Other Rules

<!-- b000182 | prose | pages [15] -->
a. Keep-Left-Or-Right Rule

<!-- b000183 | prose | pages [15] -->
The Keep-Right-Except-Pass rule is an asymmetry rule because the conditions of changing to the left or the right lane are not the same. To model the symmetry conditions, we define a new rule called Keep-Left-Or-Right rule, in which the driver can pass other vehicles from the left or right lanes and it would not be necessary to keep to the right lane. The following figure illustrates the rules for a vehicle i to change to another lane:

<!-- b000184 | prose | pages [15] -->
Incentive Condition:

<!-- b000185 | prose | pages [15, 16] -->
gap ( i )  iv  1 Safety Condition:

<!-- b000186 | furniture | pages [16] -->
Team #30532                                                                      Page 16 of 29

<!-- b000188 | prose | pages [16] -->
gap ( i )  iv  1 0

<!-- b000189 | prose | pages [16] -->
gap ( i )  v ,0 back max

<!-- b000190 | prose | pages [16] -->
Stochastic condition rand() < Pchange

<!-- b000191 | prose | pages [16] -->
We can find that in this rule, drivers always change lanes with a probability Pchange to get a greater speed under the condition that changing lane is safe.

<!-- b000192 | prose | pages [16] -->
b. High-Speed-Right-And-Low-Speed-Left-Except-Pass Rule

<!-- b000193 | prose | pages [16] -->
We also propose a new rule to classify the vehicles under discussion according to their speed. Under this rule, vehicles with a speed lower than vthreshold should run on the right lane, and vehicles with a speed higher or equal to vthreshold should run on the left lane. If a vehicle intends to pass another vehicle, it can temporally change to another lane. The following illustration demonstrates the rules for a vehicle i to change to another lane: Incentive conditions:

<!-- b000194 | prose | pages [16] -->
'L L  and v  v (T1) i threshold

<!-- b000195 | prose | pages [16] -->
'L L  and v  v (T2) i threshold

<!-- b000196 | prose | pages [16] -->
gap ( i )  iv  1 (T3)

<!-- b000197 | prose | pages [16] -->
Safety conditions:

<!-- b000198 | prose | pages [16] -->
gap ( i )  iv  1 0

<!-- b000199 | prose | pages [16] -->
gap ( i )  v ,0 back max

<!-- b000200 | prose | pages [16] -->
Stochastic condition

<!-- b000201 | prose | pages [16] -->
rand() < Pchange

<!-- b000202 | prose | pages [16] -->
T1 and T2 mean that when a vehicle in the high (low) speed lane has a low (high) speed, it needs to change to the low(high) speed lane; If one of T1, T2 T3 agrees, then there is an incentive to change lanes. The safety condition and Stochastic condition applies the same in terms of the other two rules.

<!-- b000203 | heading | pages [16] -->
4.3.2 Simulation Results and Discussion

<!-- b000204 | furniture | pages [17] -->
Team #30532                                                                      Page 17 of 29

<!-- b000205 | prose | pages [17] -->
a. Flow vs. Density

<!-- b000206 | caption | pages [17] -->
Figure 8: Flow vs. Density

<!-- b000207 | prose | pages [17] -->
This figure shows that, when density is around 0.15, Keep-left-or-right rule has a bigger flow.

<!-- b000208 | prose | pages [17] -->
b. Lane Changing Frequency vs. Density

<!-- b000209 | caption | pages [17] -->
Figure 9: Lane Changing Frequency vs. Density

<!-- b000210 | prose | pages [17] -->
It’s obvious that three rules have a big difference in lane changing frequency. There is more lane changing in Keep-left-or-right rule, because this rule allows turn right or left. However larger lane changing frequency will decrease the safety.

<!-- b000211 | furniture | pages [18] -->
Team #30532                                                                      Page 18 of 29

<!-- b000212 | prose | pages [18] -->
c. Average Velocity vs. Density

<!-- b000213 | caption | pages [18] -->
Figure 10: Average Velocity vs. Density

<!-- b000214 | prose | pages [18] -->
This figure shows that when density is around 0.15, Keep-left-or-right rule has a bigger velocity.

<!-- b000215 | prose | pages [18] -->
d. Lane Usage vs. Density

<!-- b000216 | caption | pages [18] -->
Figure 11: Lane Usage vs. Density

<!-- b000217 | prose | pages [18] -->
Compare this two figures, because our lane is a loop which means the total lane usage is not changed, one lane usage high will cause another lane usage low. These figures show that Keep-Right-Except-Pass rule has a high usage in left lane and High-in-left-Low-in-Right rule has a high usage in right lane, and Keep-Left-or-Right is in between.

<!-- b000218 | furniture | pages [19] -->
Team #30532                                                                      Page 19 of 29

<!-- b000219 | heading | pages [19] -->
4.3.3 Introduction of factor analysis

<!-- b000220 | prose | pages [19] -->
We need to evaluate the performance of different rules, so we have to define some metrics. In the previous section, we define several metrics (i.e. traffic flow, average velocity, lane change frequency) . In this section, in order to get a general metrics, we apply the factor analysis method to the output data of our simulation model.

<!-- b000221 | prose | pages [19] -->
Factor analysis method is a kind of quantitative analysis method that finds a few random variables being able to represent all variables through analyzing internal dependency relationship of covariance matrix (or correlation coefficient matrix) among many variables. Among it, several random variables found are immeasurable, which are called common factors. It is irrelevant between each common factor and common factor, and all the variables can be expressed by these several common factors. Factor analysis analyzes the whole economic issues through reducing the number of the variables and replacing all the variables with several factors, which greatly simplifies the realistic analysis process. Assume that there are N samples and P indexes, x=(x1,x2,…,xr)T is random variable, the common factor needing to be found is F=(F1,F2,…,Fm)T. Assume the impact of  common factors is linear, the indexes can be decomposed into the following form. We call this model

<!-- b000222 | prose | pages [19] -->
 X a a a  F         1 11 12 1 q 1 1          X a a a  F         2 21 22 2 q 2 2  + +                         X a a a  F         p p 1 p 2 pq p m

<!-- b000223 | prose | pages [19] -->
as factor models. We call matrix A=(aij) factor loading (Loading), call aij factor and the essence of loading is the related coefficient of common factor Fi and variable Xj. Among it, ε is special factor, which represents the influencing factor except common factor, when actually analyzing generally it can be ignored. For the common factor needing to solve out, the actual meaning is depended on that on which variables the common factor has greater loading. But under the general condition, the factor loading matrix of initial factor model is complicated, which is not good for the explanation of factor. Therefore, the more reasonable and obvious explanation for each common factor can be given further through factor rotation, so that Loading can be closer to ±1,0 as possible, thereby simplifying the complication of factor.

<!-- b000224 | prose | pages [19] -->
After the common factor is solved, regression estimate etc. methods can further used to solve the mathematical model of each common factor scoring, and express them to the linear form of the variable, thus calculating the score. The model is as following:

<!-- b000225 | prose | pages [19] -->
Fi=ai1X1+ai2X2+…+ainXn  (i=1,2,…,m)

<!-- b000226 | heading | pages [19] -->
4.3.4 Simulation Results and Discussion

<!-- b000227 | prose | pages [19, 20] -->
We apply factor analyze to the output data of our simulation model. In our analyze, the X1-X8 represents density, flow, velocity, lane changing frequency, maximal velocity, fraction of big car, lane changing probability and random braking probability respectively. We use principal component method to estimate the factor loading matrix, and get the eigenvalues of the correlation matrix, the difference of neighbor eigenvalues, the proportion and cumulative proportion (see below form):

<!-- b000228 | furniture | pages [20] -->
Team #30532                                                                      Page 20 of 29

<!-- b000230 | prose | pages [20] -->
Eigenvalues of the Correlation Matrix: Total = 8 Average = 1

<!-- b000231 | prose | pages [20] -->
Eigenvalue Difference Proportion Cumulative

<!-- b000232 | prose | pages [20] -->
2.89645713 1.31353361 0.3621 0.3621 1

<!-- b000233 | prose | pages [20] -->
1.58292351 0.37816016 0.1979 0.5599 2

<!-- b000234 | prose | pages [20] -->
1.20476335 0.20044055 0.1506 0.7105 3

<!-- b000235 | prose | pages [20] -->
1.00432280 0.37373366 0.1255 0.8361 4

<!-- b000236 | prose | pages [20] -->
0.63058914 0.12739757 0.0788 0.9149 5

<!-- b000237 | prose | pages [20] -->
0.50319158 0.34892813 0.0629 0.9778 6

<!-- b000238 | prose | pages [20] -->
0.15426345 0.13077440 0.0193 0.9971 7

<!-- b000239 | prose | pages [20] -->
0.02348904 0.0029 1.0000 8

<!-- b000240 | prose | pages [20] -->
Table 1 We find that the first four common factors have a cumulative proportion of more than 80%, which shows that the first four common factors represents more than 80% data of  the original data’s information.

<!-- b000241 | prose | pages [20] -->
Then we apply the orthogonal rotation that has the biggest variance to the factor loading matrix, and get the rotated factor pattern:

<!-- b000242 | prose | pages [20] -->
Rotated Factor Pattern

<!-- b000243 | prose | pages [20] -->
Factor1 Factor2 Factor3 Factor4

<!-- b000244 | prose | pages [20] -->
-0.88732 -0.38185 0.02988 0.03612 x1

<!-- b000245 | prose | pages [20] -->
0.83844 -0.40101 0.04766 0.07084 x2

<!-- b000246 | prose | pages [20] -->
0.89907 -0.26680 0.01582 0.04136 x3

<!-- b000247 | prose | pages [20] -->
0.04415 0.82960 0.10929 0.03195 x4

<!-- b000248 | prose | pages [20, 21] -->
0.04149 0.00296 -0.00558 0.99387 x5 Rotated Factor Pattern

<!-- b000249 | furniture | pages [21] -->
Team #30532                                                                      Page 21 of 29

<!-- b000251 | prose | pages [21] -->
Factor1 Factor2 Factor3 Factor4

<!-- b000252 | prose | pages [21] -->
0.30426 -0.16390 0.77151 -0.07155 x6

<!-- b000253 | prose | pages [21] -->
-0.29847 0.23335 0.77425 0.06986 x7

<!-- b000254 | prose | pages [21] -->
-0.28825 0.86579 -0.08082 -0.03168 x8

<!-- b000255 | prose | pages [21] -->
Table 2 We find that among all the factors of F1, positive factors are mainly X3(velocity), X2(flow), negative factors are mainly X1(density), so we think that F1 represents the ability of promoting traffic flow; among all the factors of F2, positive factors are mainly X4(lane changing frequency) and X8(random braking probability), negative factors are mainly X1(density), X2(flow), so we think that F2 represents the safety; The positive factors of F3 are mainly X6(fraction of big car) and X7(lane changing probability), so we think F3 represents the usage of the road. The position factor of F4 is X5(maximal velocity limits), so we think F4 represents the maximal velocity limits.

<!-- b000256 | prose | pages [21] -->
After that, we use Thompson factor to calculate the scores of F1, F2, F3 and F4, and get the following form of standardized scoring coefficients:

<!-- b000257 | prose | pages [21] -->
Standardized Scoring Coefficients

<!-- b000258 | prose | pages [21] -->
Factor1 Factor2 Factor3 Factor4

<!-- b000259 | prose | pages [21] -->
-0.42148 -0.32831 0.05569 0.05885 x1

<!-- b000260 | prose | pages [21] -->
0.29755 -0.12210 0.02855 0.04560 x2

<!-- b000261 | prose | pages [21] -->
0.34145 -0.03788 -0.00242 0.01521 x3

<!-- b000262 | prose | pages [21] -->
0.11943 0.47215 0.06831 0.03353 x4

<!-- b000263 | prose | pages [21] -->
-0.00956 0.01093 -0.00814 0.98713 x5

<!-- b000264 | prose | pages [21] -->
0.08992 -0.07379 0.63251 -0.08209 x6

<!-- b000265 | prose | pages [21] -->
-0.11648 0.07545 0.63929 0.07671 x7

<!-- b000266 | prose | pages [21] -->
-0.00884 0.45523 -0.08095 -0.01995 x8

<!-- b000267 | prose | pages [21] -->
Table 3 Base on this form, we get the factor scoring function for the four factors.

<!-- b000268 | prose | pages [21, 22] -->
F = −0.42148X + 0.29755X. + 0.34145X0 + 0.11943X1 −0.00956X3 + 0.08992X4 −0.11648X5 −0.00884X6 F. = −0.32831X −0.1221X. −0.03788X0 + 0.47215X1 + 0.01093X3 −0.07379X4 + 0.07545X5 + 0.45523X6 F0 = 0.05569X + 0.02855X. −0.00242X0 + 0.06831X1 −0.00814X3 + 0.63251X4 + 0.63929X5 −0.08095X6 F1 = 0.05885X + 0.0456X. + 0.01521X0 + 0.03353X1 + 0.98713X3 −0.08209X4 + 0.07671X5 −0.01995X6

<!-- b000269 | furniture | pages [22] -->
Team #30532                                                                      Page 22 of 29

<!-- b000271 | prose | pages [22] -->
We apply theses scoring functions to our simulation data, and get following curves. In these figures, KROL=Keep-Right-Or-Left，KREP=Keep-Right-Except-Pass， HLLR=High speed-Right-Low speed-Left。

<!-- b000272 | caption | pages [22] -->
Figure 12: Density vs. Factor Score

<!-- b000273 | prose | pages [22] -->
From this figure we can get that the flow of three rules first increase then decrease when the density is increasing. And the safety has the trend of first decreasing then increasing and finally decreasing slowly. Before the density reach 0.1, three rules performs equal, when density is over 0.1, the flow and safety of KROL rule are better than other two rules. KREP rule is the second, which is slightly better than HLLR rule.

<!-- b000274 | furniture | pages [23] -->
Team #30532                                                                      Page 23 of 29

<!-- b000275 | caption | pages [23] -->
Figure 13: Max speed limits vs. Factor sore

<!-- b000276 | prose | pages [23] -->
From the above figure we find that with the increasing of maximal velocity limit, the flow of three rules keep increasing, but the increasing speed is slow; the safety is first decrease then increase slowly.

<!-- b000277 | caption | pages [23] -->
Figure 14: The proportion of big car vs. Factor Score

<!-- b000278 | furniture | pages [24] -->
Team #30532                                                                      Page 24 of 29

<!-- b000279 | prose | pages [24] -->
Above figure shows that with the increasing of the big car fraction, the flow of three rules all continue increase, but the safety is decrease. In this experiment, the KROL rule performs best, the second is KREP rule and the last is HLLR rule.

<!-- b000280 | caption | pages [24] -->
Figure 15: Probability of changing lanes vs. Factor score

<!-- b000281 | prose | pages [24] -->
Above figure shows that, with the increase of lane changing probability, the flow of three rules is sable with no big change, and the safety is continue increasing. In this experiment, KROL continue performs best, the KREP rule is the second and the worst is HLLR rule.

<!-- b000282 | furniture | pages [25] -->
Team #30532                                                                      Page 25 of 29

<!-- b000283 | caption | pages [25] -->
Figure 16: Probability of random brake vs. Factor score

<!-- b000284 | prose | pages [25] -->
From above figure we can find that with the increase of random braking probability, the flow decrease but the safety increase. In this situation, the KROL rule performs best, the KREP rule is the second and HLLR rule is the worst.

<!-- b000285 | prose | pages [25] -->
To conclude, the KROL rule performs best, KREP is the second and HLLR rule is the last.

<!-- b000286 | prose | pages [25] -->
On the other hand, if we need to scoring traffic driving rules, collect the actual data and get data into factor scoring function, comparing the score, it is easy to judge the performance of rule.

<!-- b000287 | heading | pages [25] -->
4.4 Results and Discussion under Intelligent System

<!-- b000288 | prose | pages [25] -->
As we know, under the intelligent system, drivers know road condition ahead in advance, so we can choose the shortest and fastest way to drive on. Owing to ITS is embedded in road network and vehicles, it can be interpreted that we do not need a human operator, car’s behavior is fully under ITS control. However, due to the owners liking, speed will be various.

<!-- b000289 | prose | pages [25] -->
In that case, we let randomly brake probability drops to 0, the probability of changing lanes will be promoted to 1, the traffic situation is artificially enhanced to the ideal situation through intelligent control. The following are figures of flow, lane change frequency and average speed.

<!-- b000290 | furniture | pages [26] -->
Team #30532                                                                      Page 26 of 29

<!-- b000291 | prose | pages [26] -->
a. Density vs. Traffic Flow

<!-- b000292 | caption | pages [26] -->
Figure 17: Density vs. Traffic Flow

<!-- b000293 | prose | pages [26] -->
When 0.15<density<0.23, the traffic flow under KLOR rule and HLLR rule is almost the same, and KREP is the lowest.

<!-- b000294 | prose | pages [26] -->
b. Density vs. Lane Change Frequency

<!-- b000295 | caption | pages [26] -->
Figure 18: Density vs. Lane Change Frequency

<!-- b000296 | prose | pages [26] -->
Under the three kinds of rules, Lane change behavior exists only occur in their specific density range. This is consistent with the facts. The average number of lane change frequency under KREP rule is minimal.

<!-- b000297 | furniture | pages [27] -->
Team #30532                                                                      Page 27 of 29

<!-- b000298 | prose | pages [27] -->
c. Density vs. Average Velocity

<!-- b000299 | caption | pages [27] -->
Figure 19: Density vs. Average Velocity

<!-- b000300 | prose | pages [27] -->
When 0.15<density<0.2, the average velocity under KLOR rule and HLLR rule is almost the same, but KREP rule is the lowest.

<!-- b000301 | prose | pages [27] -->
We get the data into the formula of factor score, get the following figure:

<!-- b000302 | caption | pages [27] -->
Figure 12: Density vs. Factor Score

<!-- b000303 | furniture | pages [28] -->
Team #30532                                                                      Page 28 of 29

<!-- b000304 | prose | pages [28] -->
When 0.15<density<0.23, the traffic flow under KROL rule is maximal, the next is HLLR rule and the last one is KREP rule. However, the safety under the three rules is almost unanimous.

<!-- b000305 | heading | pages [28] -->
5 Conclusion

<!-- b000306 | prose | pages [28] -->
Finishing the work above, we conclude that, when traffic density, the probability of lane-changing and the speed limit is low, KROL rule is able to promote traffic flow and safety. In general, KROL rule performs the best, while HLLR rule performs the worst.

<!-- b000307 | prose | pages [28] -->
In countries where driving automobiles on the left is norm, our KREP model is also suitable with a simple change of orientation. Considering the other two models set no limit on the lane in which vehicles drive, the model can be applied without modification to those countries driving to the left.

<!-- b000308 | prose | pages [28] -->
Under the control of an intelligent system, the rule of KREP rule promotes the traffic flow the least while the range of difference is the greatest and the other two rules promote the traffic flow to a similar degree that is greater than that promoted by the KREP rule.

<!-- b000309 | heading | pages [28] -->
6 Strength and Weakness

<!-- b000310 | heading | pages [28] -->
 Strengths

<!-- b000311 | prose | pages [28] -->
1. The application of cell automation model has advantages in large traffic network simulation in that this model entails discrete result from the perspectives of time, space and state.

<!-- b000312 | prose | pages [28] -->
2. This model succeeded in improving the CA model and managed a two-lane simulation, which is persuasive in that it is more in line with the actual situation.

<!-- b000313 | prose | pages [28] -->
3. Factor analysis has been applied to the evaluation of dispersing capability and safety, which makes more sharp comparison among various evaluations with regard to traffic rules.

<!-- b000314 | heading | pages [28] -->
 Weaknesses

<!-- b000315 | prose | pages [28] -->
1. It is a pity that we have not found adequate data for empirical date evaluation on the basis of the proposed model.

<!-- b000316 | prose | pages [28] -->
2. In reality, there is higher probability that drivers randomly brake and pass other cars during driving. Thus we only made a rough estimation due to lack of accurate statistics from the actual life.

<!-- b000317 | furniture | pages [29] -->
Team #30532                                                                      Page 29 of 29

<!-- b000318 | heading | pages [29] -->
7 Reference

<!-- b000319 | references | pages [29] -->
[1] Nagel K, Schreckenberg M. A cellular automaton model for freeway traffic.

<!-- b000320 | references | pages [29] -->
Journal de Physique I, 1992, 2(12): 2221-2229.

<!-- b000321 | references | pages [29] -->
[2] Carlos F. Daganzo. A continuum theory of traffic dynamics for freeways with

<!-- b000322 | references | pages [29] -->
special lanes, Transportation Research Part B. 1997, 31 (2):83-102.

<!-- b000323 | references | pages [29] -->
[3] Peter Hidas. Modeling lane changing and merging in microscopic traffic

<!-- b000324 | references | pages [29] -->
simulation, Transportation Research Part C. 2002,10: 351-371.

<!-- b000325 | references | pages [29] -->
[4] H. W. Zhang. Anisotropic property revisited-does it hold in multi-lane traffic.

<!-- b000326 | references | pages [29] -->
Transportation Research Part B. 2003,37: 561-577.
