# P-A-2016-44398-137ab9e6

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | title | pages [1] -->
44398

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
T1

<!-- b000009 | prose | pages [1] -->
F1

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | prose | pages [1] -->
T2

<!-- b000012 | prose | pages [1] -->
F2

<!-- b000013 | prose | pages [1] -->
Problem Chosen

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | title | pages [1] -->
A

<!-- b000016 | prose | pages [1] -->
T3

<!-- b000017 | prose | pages [1] -->
F3

<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
T4

<!-- b000020 | prose | pages [1] -->
F4

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | heading | pages [1] -->
2016 Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

<!-- b000023 | heading | pages [1] -->
Summary

<!-- b000024 | prose | pages [1] -->
A traditional bathtub cannot be reheated by itself, so users have to add hot water from time to time. Our goal is to establish a model of the temperature of bath water in space and time. Then we are expected to propose an optimal strategy for users to keep the temperature even and close to initial temperature and decrease water consumption.

<!-- b000025 | prose | pages [1] -->
To simplify modeling process, we firstly assume there is no person in the bathtub. We regard the whole bathtub as a thermodynamic system and introduce heat transfer formulas.

<!-- b000026 | prose | pages [1] -->
We establish two sub-models: adding water constantly and discontinuously. As for the former sub-model, we define the mean temperature of bath water. Introducing Newton cooling formula, we determine the heat transfer capacity. After deriving the value of parameters, we deduce formulas to derive results and simulate the change of temperature field via CFD. As for the second sub-model, we define an iteration consisting of two process: heating and standby. According to energy conservation law, we obtain the relationship of time and total heat dissipating capacity. Then we determine the mass flow and the time of adding hot water. We also use CFD to simulate the temperature field in second sub-model.

<!-- b000027 | prose | pages [1] -->
In consideration of evaporation, we correct the results of sub-models referring to some scientists’ studies. We define two evaluation criteria and compare the two sub-models. Adding water constantly is found to keep the temperature of bath water even and avoid wasting too much water, so it is recommended by us.

<!-- b000028 | prose | pages [1] -->
Then we determine the influence of some factors: radiation heat transfer, the shape and volume of the tub, the shape/volume/temperature/motions of the person, the bubbles made from bubble bath additives. We focus on the influence of those factors to heat transfer and

<!-- b000029 | heading | pages [1] -->
then conduct sensitivity analysis. The results indicate smaller bathtub with less surface

<!-- b000030 | prose | pages [1] -->
area, lighter personal mass, less motions and more bubbles will decrease heat transfer and save water.

<!-- b000031 | prose | pages [1] -->
Based on our model analysis and conclusions, we propose the optimal strategy for the user in a bathtub and explain the reason of uneven temperature throughout the bathtub. In addition, we make improvement for applying our model in real life.

<!-- b000032 | keywords | pages [1] -->
Key words:  Heat transfer  Thermodynamic system  CFD  Energy conservation

<!-- b000033 | furniture | pages [1] -->


<!-- b000034 | furniture | pages [2] -->
Team #44398                                                    Page 2 of 51

<!-- b000035 | prose | pages [2] -->
Enjoy a Cozy and Green Bath

<!-- b000036 | heading | pages [2] -->
Contents

<!-- b000037 | contents | pages [2] -->
1  Introduction .................................................................................................. 4

<!-- b000038 | contents | pages [2] -->
1.1  Background ......................................................................................... 4

<!-- b000039 | contents | pages [2] -->
1.2 Literature Review ............................................................................... 4

<!-- b000040 | contents | pages [2] -->
1.3 Restatement of the Problem .............................................................. 4

<!-- b000041 | contents | pages [2] -->
2 Assumptions and Justification .................................................................. 6

<!-- b000042 | contents | pages [2] -->
3 Notations........................................................................................................ 7

<!-- b000043 | contents | pages [2] -->
4 Model Overview ........................................................................................... 7

<!-- b000044 | contents | pages [2] -->
5  Sub-model I : Adding Water Continuously ............................................ 8

<!-- b000045 | contents | pages [2] -->
5.1  Model Establishment ......................................................................... 9

<!-- b000046 | contents | pages [2] -->
5.1.1  Control Equations and Boundary Conditions .................... 9

<!-- b000047 | contents | pages [2] -->
5.1.2  Definition of the Mean Temperature .................................. 11

<!-- b000048 | contents | pages [2] -->
5.1.3  Determination of Heat Transfer Capacity ......................... 11

<!-- b000049 | contents | pages [2] -->
5.2  Results ................................................................................................ 13

<!-- b000050 | contents | pages [2] -->
5.2.1  Determination of Parameters .............................................. 13

<!-- b000051 | contents | pages [2] -->
5.2.2  Calculating Results ............................................................... 14

<!-- b000052 | contents | pages [2] -->
5.2.3  Simulating Results ................................................................ 15

<!-- b000053 | contents | pages [2] -->
6  Sub-model II: Adding Water Discontinuously .................................... 18

<!-- b000054 | contents | pages [2] -->
6.1  Heating Model .................................................................................. 18

<!-- b000055 | contents | pages [2] -->
6.1.1  Control Equations and Boundary Conditions .................. 18

<!-- b000056 | contents | pages [2] -->
6.1.2  Determination of Inflow Time and Amount ..................... 19

<!-- b000057 | contents | pages [2] -->
6.2  Standby Model ................................................................................. 20

<!-- b000058 | contents | pages [2] -->
6.2.1  Process Analysis .................................................................... 20

<!-- b000059 | contents | pages [2] -->
6.2.2  Calculation of Parameters .................................................... 20

<!-- b000060 | contents | pages [2] -->
6.3  Results ................................................................................................ 21

<!-- b000061 | contents | pages [2] -->
6.3.1  Determination of Parameters .............................................. 21

<!-- b000062 | contents | pages [2] -->
6.3.2  Calculating Results ............................................................... 23

<!-- b000063 | furniture | pages [2] -->


<!-- b000064 | furniture | pages [3] -->
Team #44398                                                    Page 3 of 51

<!-- b000065 | contents | pages [3] -->
6.3.3  Simulating Results ................................................................ 23

<!-- b000066 | contents | pages [3] -->
6.4  Conclusion ........................................................................................ 27

<!-- b000067 | contents | pages [3] -->
7  Correction and Contrast of Sub-Models ............................................... 27

<!-- b000068 | contents | pages [3] -->
7.1  Correction with Evaporation Heat Transfer ................................ 27

<!-- b000069 | contents | pages [3] -->
7.1.1  Correction Principle .............................................................. 27

<!-- b000070 | contents | pages [3] -->
7.1.2  Correction Results ................................................................. 28

<!-- b000071 | contents | pages [3] -->
7.2  Contrast of Two Sub-Models .......................................................... 30

<!-- b000072 | contents | pages [3] -->
7.2.1  Evaluation Criteria ................................................................ 30

<!-- b000073 | contents | pages [3] -->
7.2.2  Determination of Water Consumption .............................. 30

<!-- b000074 | contents | pages [3] -->
7.2.3  Conclusion ............................................................................. 31

<!-- b000075 | contents | pages [3] -->
8  Model Analysis and Sensitivity Analysis ............................................. 31

<!-- b000076 | contents | pages [3] -->
8.1  The Influence of Different Bathtubs .............................................. 32

<!-- b000077 | contents | pages [3] -->
8.1.1  Different Volumes of Bathtubs ............................................ 32

<!-- b000078 | contents | pages [3] -->
8.1.2  Different Shapes of Bathtubs ............................................... 34

<!-- b000079 | contents | pages [3] -->
8.2  The Influence of Person in Bathtub ............................................... 36

<!-- b000080 | contents | pages [3] -->
8.2.1  When the Person Remains Static in a Bathtub .................. 36

<!-- b000081 | contents | pages [3] -->
8.2.2  When the Person Moves in a Bathtub ................................ 37

<!-- b000082 | contents | pages [3] -->
8.2.3  Results Analysis and Sensitivity Analysis ......................... 38

<!-- b000083 | contents | pages [3] -->
8.3  The Influence of Bubble Bath Additives ....................................... 42

<!-- b000084 | contents | pages [3] -->
8.4  The Influence of Radiation Heat Transfer .................................... 44

<!-- b000085 | contents | pages [3] -->
8.5  Conclusion ........................................................................................ 45

<!-- b000086 | contents | pages [3] -->
9  Further Discussion ..................................................................................... 45

<!-- b000087 | contents | pages [3] -->
9.1  Different Distribution of Inflow Faucets ...................................... 45

<!-- b000088 | contents | pages [3] -->
9.2  Model Application ........................................................................... 46

<!-- b000089 | contents | pages [3] -->
10  Strength and Weakness ........................................................................... 47

<!-- b000090 | contents | pages [3] -->
10.1  Strength ........................................................................................... 47

<!-- b000091 | contents | pages [3] -->
10.2  Weakness ......................................................................................... 47

<!-- b000092 | contents | pages [3] -->
Report ................................................................................................................. 49

<!-- b000093 | contents | pages [3] -->
Reference ........................................................................................................... 50

<!-- b000094 | furniture | pages [3] -->


<!-- b000095 | furniture | pages [3] -->


<!-- b000096 | furniture | pages [3] -->


<!-- b000097 | furniture | pages [4] -->
Team #44398                                                    Page 4 of 51

<!-- b000098 | heading | pages [4] -->
1  Introduction

<!-- b000099 | heading | pages [4] -->
1.1  Background

<!-- b000100 | prose | pages [4] -->
Bathing in a tub is a perfect choice for those who have been worn out after a long day’s working. A traditional bathtub is a simply water containment vessel without a secondary heating system or circulating jets. Thus the temperature of water in bathtub declines noticeably as time goes by, which will influent the experience of bathing. As a result, the bathing person needs to add a constant trickle of hot water from a faucet to reheat the bathing water. This way of bathing will result in waste of water because when the capacity of the bathtub is reached, excess water overflows the tub.

<!-- b000101 | prose | pages [4] -->
An optimal bathing strategy is required for the person in a bathtub to get comfortable bathing experience while reducing the waste of water.

<!-- b000102 | heading | pages [4] -->
1.2 Literature Review

<!-- b000103 | prose | pages [4] -->
Korean physicist Gi-Beum Kim analyzed heat loss through free surface of water contained in bathtub due to conduction and evaporation [1]. He derived a relational equation based on the basic theory of heat transfer to evaluate the

<!-- b000104 | prose | pages [4] -->
performance of bath tubes. The major heat loss was found to be due to evaporation. Moreover, he found out that the speed of heat loss depends more on the humidity of the bathroom than the temperature of water contained in the bathtub. So, it is best to maintain the temperature of bathtub water to be between 41 to 45 ℃ and the humidity of bathroom to be 95%.

<!-- b000105 | prose | pages [4] -->
When it comes to convective heat transfer in bathtub, many studies can be referred to. Newton's law of cooling states that the rate of heat loss of a body is proportional to the difference in temperatures between the body and its surroundings while under the effects of a breeze [2]. Claude-Louis Navier and George Gabriel Stokes described the motion of viscous fluid substances with the Navier–Stokes equations. Those equations may be used to model the weather, ocean currents, water flow in a pipe and air flow around a wing [3].

<!-- b000106 | prose | pages [4] -->
In addition, some numerical simulation software are applied in solving and analyzing problems that involve fluid flows. For example, Computational Fluid Dynamics (CFD) is a common one used to perform the calculations required to simulate the interaction of liquids and gases with surfaces defined

<!-- b000107 | prose | pages [4] -->
by boundary conditions [4].

<!-- b000108 | heading | pages [4] -->
1.3 Restatement of the Problem

<!-- b000109 | prose | pages [4] -->
We are required to establish a model to determine the change of water

<!-- b000110 | furniture | pages [4] -->


<!-- b000111 | furniture | pages [5] -->
Team #44398                                                    Page 5 of 51

<!-- b000112 | prose | pages [5] -->
temperature in space and time. Then we are expected to propose the best strategy for the person in the bathtub to keep the water temperature close to initial temperature and even throughout the tub. Reduction of waste of water

<!-- b000113 | prose | pages [5] -->
is also needed. In addition, we have to consider the impact of different conditions on our model, such as different shapes and volumes of the bathtub, etc.

<!-- b000114 | prose | pages [5] -->
In order to solve those problems, we will proceed as follows:

<!-- b000115 | heading | pages [5] -->
 Stating assumptions. By stating our assumptions, we will narrow

<!-- b000116 | prose | pages [5] -->
the focus of our approach towards the problems and provide some insight into bathtub water temperature issues.

<!-- b000117 | heading | pages [5] -->
 Making notations. We will give some notations which are

<!-- b000118 | prose | pages [5] -->
important for us to clarify our models.

<!-- b000119 | heading | pages [5] -->
 Presenting our model. In order to investigate the problem deeper,

<!-- b000120 | prose | pages [5] -->
we divide our model into two sub-models. One is a steady convection heat transfer sub-model in which hot water is added constantly. The other one is an unsteady convection heat transfer sub-model where hot water is added discontinuously.

<!-- b000121 | heading | pages [5] -->
 Defining evaluation criteria and comparing sub-models. We

<!-- b000122 | prose | pages [5] -->
define two main criteria to evaluate our model: the mean temperature of bath water and the amount of inflow water.

<!-- b000123 | prose | pages [5] -->
 Analysis of influencing factors. In term of the impact of different

<!-- b000124 | prose | pages [5] -->
factors on our model, we take those into consideration: the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub, the motions made by the person in the bathtub and adding a bubble bath additive initially.

<!-- b000125 | heading | pages [5] -->
 Model testing and sensitivity analysis. With the criteria defined

<!-- b000126 | prose | pages [5] -->
before, we evaluate the reliability of our model and do the sensitivity analysis.

<!-- b000127 | heading | pages [5] -->
 Further discussion. We discuss about different ways to arrange

<!-- b000128 | prose | pages [5] -->
inflow faucets. Then we improve our model to apply them in reality.

<!-- b000129 | heading | pages [5] -->
 Evaluating the model. We discuss about the strengths and

<!-- b000130 | prose | pages [5] -->
weaknesses of our model.

<!-- b000131 | furniture | pages [5] -->


<!-- b000132 | furniture | pages [6] -->
Team #44398                                                    Page 6 of 51

<!-- b000133 | heading | pages [6] -->
2 Assumptions and Justification

<!-- b000134 | prose | pages [6] -->
To simplify the problem and make it convenient for us to simulate real-life

<!-- b000135 | prose | pages [6] -->
conditions, we make the following basic assumptions, each of which is properly justified.

<!-- b000136 | prose | pages [6] -->
 The bath water is incompressible Non-Newtonian fluid. The

<!-- b000137 | prose | pages [6] -->
incompressible Non-Newtonian fluid is the basis of Navier–Stokes equations which are introduced to simulate the flow of bath water.

<!-- b000138 | prose | pages [6] -->
 All the physical properties of bath water, bathtub and air are

<!-- b000139 | prose | pages [6] -->
assumed to be stable. The change of those properties like specific heat, thermal conductivity and density is rather small according to some studies [5]. It is complicated and unnecessary to consider these little change so we ignore them.

<!-- b000140 | prose | pages [6] -->
 There is no internal heat source in the system consisting of bathtub,

<!-- b000141 | prose | pages [6] -->
hot water and air. Before the person lies in the bathtub, no internal heat source exist except the system components. The circumstance where the person is in the bathtub will be investigated in our later

<!-- b000142 | prose | pages [6] -->
discussion.

<!-- b000143 | prose | pages [6] -->
 We ignore radiative thermal exchange. According to Stefan-

<!-- b000144 | prose | pages [6] -->
Boltzmann’s law, the radiative thermal exchange can be ignored when the temperature is low. Refer to industrial standard [6], the temperature in bathroom is lower than 100℃, so it is reasonable for us to make this assumption.

<!-- b000145 | prose | pages [6] -->
 The temperature of the adding hot water from the faucet is stable.

<!-- b000146 | prose | pages [6] -->
This hypothesis can be easily achieved in reality and will simplify our process of solving the problem.

<!-- b000147 | furniture | pages [6] -->


<!-- b000148 | furniture | pages [6] -->


<!-- b000149 | furniture | pages [6] -->


<!-- b000150 | furniture | pages [6] -->


<!-- b000151 | furniture | pages [6] -->


<!-- b000152 | furniture | pages [6] -->


<!-- b000153 | furniture | pages [7] -->
Team #44398                                                    Page 7 of 51

<!-- b000154 | heading | pages [7] -->
3 Notations

<!-- b000155 | caption | pages [7] -->
Table 1  Notations

<!-- b000156 | prose | pages [7] -->
Symbols Definition

<!-- b000157 | prose | pages [7] -->
h

<!-- b000158 | prose | pages [7] -->
Unit

<!-- b000159 | prose | pages [7] -->
   2 W / m K Convection heat transfer coefficient

<!-- b000160 | prose | pages [7] -->
k

<!-- b000161 | furniture | pages [7] -->


<!-- b000162 | prose | pages [7] -->
   W / m K Thermal conductivity

<!-- b000163 | prose | pages [7] -->
pc Specific heat

<!-- b000164 | prose | pages [7] -->
 Density  Thickness

<!-- b000165 | prose | pages [7] -->
t Temperature

<!-- b000166 | prose | pages [7] -->
 Time

<!-- b000167 | prose | pages [7] -->
q Mass flow m  Heat transfer power

<!-- b000168 | prose | pages [7] -->
T A period of time V Volume M m 、

<!-- b000169 | furniture | pages [7] -->


<!-- b000170 | prose | pages [7] -->
Mass

<!-- b000171 | prose | pages [7] -->
A Area a b c 、、 The size of a bathtub

<!-- b000172 | furniture | pages [7] -->


<!-- b000173 | prose | pages [7] -->
   J / kg K

<!-- b000174 | furniture | pages [7] -->


<!-- b000175 | prose | pages [7] -->
2 kg / m m

<!-- b000176 | prose | pages [7] -->
K ℃、

<!-- b000177 | furniture | pages [7] -->


<!-- b000178 | prose | pages [7] -->
s min h 、 、

<!-- b000179 | prose | pages [7] -->
kg/s W

<!-- b000180 | prose | pages [7] -->
s min h 、 、 3 m L 、 kg

<!-- b000181 | prose | pages [7] -->
2 m 3 m

<!-- b000182 | prose | pages [7] -->
where we define the main parameters while specific value of those parameters will be

<!-- b000183 | prose | pages [7] -->
given later.

<!-- b000184 | heading | pages [7] -->
4 Model Overview

<!-- b000185 | prose | pages [7] -->
In our basic model, we aim at three goals: keeping the temperature as even as possible, making it close to the initial temperature and decreasing the water consumption.

<!-- b000186 | prose | pages [7] -->
We start with the simple sub-model where hot water is added constantly.

<!-- b000187 | prose | pages [7] -->
At first we introduce convection heat transfer control equations in rectangular coordinate system. Then we define the mean temperature of bath water. Afterwards, we introduce Newton cooling formula to determine heat transfer capacity. After deriving the value of parameters, we get calculating results via formula deduction and simulating results via CFD.

<!-- b000188 | prose | pages [7] -->
Secondly, we present the complicated sub-model in which hot water is

<!-- b000189 | prose | pages [7] -->
added discontinuously. We define an iteration consisting of two process: heating and standby. As for heating process, we derive control equations and boundary conditions. As for standby process, considering energy conservation law, we deduce the relationship of total heat dissipating capacity and time.

<!-- b000190 | furniture | pages [7] -->


<!-- b000191 | furniture | pages [8] -->
Team #44398                                                    Page 8 of 51

<!-- b000192 | prose | pages [8] -->
Then we determine the time and amount of added hot water. After deriving the value of parameters, we get calculating results via formula deduction and simulating results via CFD.

<!-- b000193 | prose | pages [8] -->
At last, we define two criteria to evaluate those two ways of adding hot water. Then we propose optimal strategy for the user in a bathtub.

<!-- b000194 | prose | pages [8] -->
The whole modeling process can be shown as follows.

<!-- b000195 | furniture | pages [8] -->


<!-- b000196 | furniture | pages [8] -->


<!-- b000197 | furniture | pages [8] -->


<!-- b000198 | furniture | pages [8] -->


<!-- b000199 | furniture | pages [8] -->


<!-- b000200 | furniture | pages [8] -->


<!-- b000201 | furniture | pages [8] -->


<!-- b000202 | furniture | pages [8] -->


<!-- b000203 | furniture | pages [8] -->


<!-- b000204 | furniture | pages [8] -->


<!-- b000205 | furniture | pages [8] -->


<!-- b000206 | furniture | pages [8] -->


<!-- b000207 | furniture | pages [8] -->


<!-- b000208 | furniture | pages [8] -->


<!-- b000209 | furniture | pages [8] -->


<!-- b000210 | furniture | pages [8] -->


<!-- b000211 | furniture | pages [8] -->


<!-- b000212 | furniture | pages [8] -->


<!-- b000213 | furniture | pages [8] -->


<!-- b000214 | furniture | pages [8] -->


<!-- b000215 | furniture | pages [8] -->


<!-- b000216 | caption | pages [8] -->
Fig.1  Modeling process

<!-- b000217 | heading | pages [8] -->
5  Sub-model I : Adding Water Continuously

<!-- b000218 | prose | pages [8] -->
We first establish the sub-model based on the condition that a person add water continuously to reheat the bathing water. Then we use Computational Fluid Dynamics (CFD) to simulate the change of water temperature in the

<!-- b000219 | prose | pages [8] -->
bathtub. At last, we evaluate the model with the criteria which have been defined before.

<!-- b000220 | furniture | pages [8] -->


<!-- b000221 | furniture | pages [9] -->
Team #44398                                                    Page 9 of 51

<!-- b000222 | heading | pages [9] -->
5.1  Model Establishment

<!-- b000223 | prose | pages [9] -->
Since we try to keep the temperature of the hot water in bathtub to be even,

<!-- b000224 | prose | pages [9] -->
we have to derive the amount of inflow water and the energy dissipated by the hot water into the air.

<!-- b000225 | furniture | pages [9] -->


<!-- b000226 | prose | pages [9] -->
We derive the basic convection heat transfer control equations based on the former scientists’ achievement. Then, we define the mean temperature of bath water. Afterwards, we determine two types of heat transfer: the boundary heat transfer and the evaporation heat transfer. Combining thermodynamic formulas, we derive calculating results. Via Fluent software, we get simulation results.

<!-- b000227 | heading | pages [9] -->
5.1.1  Control Equations and Boundary Conditions

<!-- b000228 | prose | pages [9] -->
According to thermodynamics knowledge, we recall on basic convection heat transfer control equations in rectangular coordinate system. Those

<!-- b000229 | prose | pages [9] -->
equations show the relationship of the temperature of the bathtub water in space.

<!-- b000230 | prose | pages [9] -->
We assume the hot water in the bathtub as a cube. Then we put it into a rectangular coordinate system. The length, width, and height of it is a , b and

<!-- b000231 | prose | pages [9] -->
c .

<!-- b000232 | furniture | pages [9] -->


<!-- b000233 | furniture | pages [9] -->


<!-- b000234 | furniture | pages [9] -->


<!-- b000235 | furniture | pages [9] -->


<!-- b000236 | furniture | pages [9] -->


<!-- b000237 | furniture | pages [9] -->


<!-- b000238 | furniture | pages [9] -->


<!-- b000239 | furniture | pages [9] -->


<!-- b000240 | caption | pages [9] -->
Fig.2  The water cube in the rectangular coordinate system

<!-- b000241 | prose | pages [9] -->
In the basis of this, we introduce the following equations [5]:

<!-- b000242 | prose | pages [9] -->
 Continuity equation:

<!-- b000243 | prose | pages [9] -->
   u v w   + 0 （1）

<!-- b000244 | furniture | pages [9] -->


<!-- b000245 | furniture | pages [9] -->


<!-- b000246 | prose | pages [9] -->
   x y z

<!-- b000247 | prose | pages [9] -->
where the first component is the change of fluid mass along the X-ray. The second component is the change of fluid mass along the Y-ray. And the third component is the change of fluid mass along the Z-ray. The sum of the change in mass along those three directions is zero.

<!-- b000248 | furniture | pages [9] -->


<!-- b000249 | furniture | pages [10] -->
Team #44398                                                    Page 10 of 51

<!-- b000250 | prose | pages [10] -->
 Moment differential equation (N-S equations):

<!-- b000251 | prose | pages [10] -->
   u u u     ( u v w )

<!-- b000252 | furniture | pages [10] -->


<!-- b000253 | prose | pages [10] -->
   x y z

<!-- b000254 | prose | pages [10] -->
   v v v     ( u v w )

<!-- b000255 | furniture | pages [10] -->


<!-- b000256 | prose | pages [10] -->
   x y z

<!-- b000257 | prose | pages [10] -->
   w w w     ( u v w ) g

<!-- b000258 | furniture | pages [10] -->


<!-- b000259 | prose | pages [10] -->
   x y z

<!-- b000260 | prose | pages [10] -->
 Energy differential equation:

<!-- b000261 | prose | pages [10] -->
   t t t   c u

<!-- b000262 | prose | pages [10] -->
(

<!-- b000263 | prose | pages [10] -->
v

<!-- b000264 | prose | pages [10] -->
+

<!-- b000265 | prose | pages [10] -->
w

<!-- b000266 | furniture | pages [10] -->


<!-- b000267 | prose | pages [10] -->
p

<!-- b000268 | prose | pages [10] -->
   x y z

<!-- b000269 | prose | pages [10] -->
    

<!-- b000270 | prose | pages [10] -->
2 2 2

<!-- b000271 | prose | pages [10] -->
p u u u     ( ) （2）

<!-- b000272 | furniture | pages [10] -->


<!-- b000273 | prose | pages [10] -->
     2 2 2 x x y z

<!-- b000274 | prose | pages [10] -->
    

<!-- b000275 | prose | pages [10] -->
2 2 2

<!-- b000276 | prose | pages [10] -->
p v v v     ( ) （3）

<!-- b000277 | furniture | pages [10] -->


<!-- b000278 | prose | pages [10] -->
     2 2 2 y x y z

<!-- b000279 | prose | pages [10] -->
   

<!-- b000280 | prose | pages [10] -->
2 2 2

<!-- b000281 | prose | pages [10] -->
p w w w     ( ) （4）

<!-- b000282 | furniture | pages [10] -->


<!-- b000283 | prose | pages [10] -->
    2 2 2 z x y z

<!-- b000284 | prose | pages [10] -->
  

<!-- b000285 | prose | pages [10] -->
2 2 2

<!-- b000286 | prose | pages [10] -->
t t t    

<!-- b000287 | prose | pages [10] -->
) ) ( )

<!-- b000288 | prose | pages [10] -->
（5）

<!-- b000289 | furniture | pages [10] -->


<!-- b000290 | prose | pages [10] -->
  

<!-- b000291 | prose | pages [10] -->
2 2 2

<!-- b000292 | prose | pages [10] -->
x y z

<!-- b000293 | prose | pages [10] -->
where the left three components are convection terms while the right three components are conduction terms.

<!-- b000294 | prose | pages [10] -->
Having derived those equations, we give the boundary conditions listed as follows:

<!-- b000295 | prose | pages [10] -->
In the inflow water area

<!-- b000296 | prose | pages [10] -->
 t

<!-- b000297 | furniture | pages [10] -->


<!-- b000298 | prose | pages [10] -->
t t （6）

<!-- b000299 | furniture | pages [10] -->


<!-- b000300 | prose | pages [10] -->
in

<!-- b000301 | prose | pages [10] -->
On the top surface of bath water, it transfer heat directly into air without heat conduction, so we have

<!-- b000302 | prose | pages [10] -->
 t   

<!-- b000303 | furniture | pages [10] -->


<!-- b000304 | prose | pages [10] -->
 z    h t t （7）

<!-- b000305 | furniture | pages [10] -->


<!-- b000306 | prose | pages [10] -->
 1 1

<!-- b000307 | prose | pages [10] -->
The range of the area suitable for (7) is

<!-- b000308 | prose | pages [10] -->
  0 x b , 0

<!-- b000309 | furniture | pages [10] -->


<!-- b000310 | prose | pages [10] -->
    y a z , c （8）

<!-- b000311 | prose | pages [10] -->
On the front surface in Fig.2, the water transfer heat firstly with bathtub inner surfaces and then the heat comes into air. Hence we have

<!-- b000312 | prose | pages [10] -->
 t  

<!-- b000313 | furniture | pages [10] -->


<!-- b000314 | prose | pages [10] -->
 x    h h t t （9）

<!-- b000315 | furniture | pages [10] -->


<!-- b000316 | prose | pages [10] -->
2 2 x

<!-- b000317 | prose | pages [10] -->
The range of the area suitable for (9) is

<!-- b000318 | prose | pages [10] -->
  0 y a , 0

<!-- b000319 | furniture | pages [10] -->


<!-- b000320 | prose | pages [10] -->
    z c x , b （10）

<!-- b000321 | furniture | pages [10] -->


<!-- b000322 | prose | pages [10] -->
On the right surface in Fig.2, the water also transfers heat firstly with bathtub inner surfaces and then the heat comes into air. The boundary condition here is

<!-- b000323 | furniture | pages [10] -->


<!-- b000324 | furniture | pages [11] -->
Team #44398                                                    Page 11 of 51

<!-- b000325 | prose | pages [11] -->
 t  

<!-- b000326 | furniture | pages [11] -->


<!-- b000327 | prose | pages [11] -->
 y    h t t （11）

<!-- b000328 | furniture | pages [11] -->


<!-- b000329 | prose | pages [11] -->
3 3 y

<!-- b000330 | prose | pages [11] -->
The range of the area suitable for (11) is

<!-- b000331 | prose | pages [11] -->
  0 x b , 0

<!-- b000332 | furniture | pages [11] -->


<!-- b000333 | prose | pages [11] -->
    z z c , y a （12）

<!-- b000334 | furniture | pages [11] -->


<!-- b000335 | heading | pages [11] -->
5.1.2  Definition of the Mean Temperature

<!-- b000336 | prose | pages [11] -->
To simplify the modeling process, we assume the bathtub and hot water in it as a constant temperature system. Thus the heat is equal in value to the enthalpy difference between inflow water and outflow water.

<!-- b000337 | prose | pages [11] -->
We let the total heat dissipation to be Q and the mass flow of inflow q . Recalling on the heat balance equation, we have water to be m

<!-- b000338 | prose | pages [11] -->
 q c

<!-- b000339 | furniture | pages [11] -->


<!-- b000340 | prose | pages [11] -->
m p t t Q （13）

<!-- b000341 | furniture | pages [11] -->


<!-- b000342 | prose | pages [11] -->
c is the specific heat of water which is constant according to our where p assumptions.

<!-- b000343 | prose | pages [11] -->
 is t The temperature difference of heat transfer

<!-- b000344 | prose | pages [11] -->
 t t

<!-- b000345 | furniture | pages [11] -->


<!-- b000346 | prose | pages [11] -->
 t （14）

<!-- b000347 | furniture | pages [11] -->


<!-- b000348 | prose | pages [11] -->
in in out

<!-- b000349 | prose | pages [11] -->
int is the temperature of inflow water and where of outflow water.

<!-- b000350 | prose | pages [11] -->
t is the temperature out

<!-- b000351 | prose | pages [11] -->
Although the temperature is different from area to area, the difference is rather small which has been proved by some scientists [8]. So we substitute the mean temperature in the bathtub with the mean value of the inflow water and outflow water. That is

<!-- b000352 | prose | pages [11] -->
t  t

<!-- b000353 | furniture | pages [11] -->


<!-- b000354 | prose | pages [11] -->
f  t in in out （15）

<!-- b000355 | furniture | pages [11] -->


<!-- b000356 | prose | pages [11] -->
2

<!-- b000357 | prose | pages [11] -->
ft is the mean temperature in the bathtub. where

<!-- b000358 | heading | pages [11] -->
5.1.3  Determination of Heat Transfer Capacity

<!-- b000359 | prose | pages [11] -->
The real-life heat transfer process is a complicated mixed heat transfer problem which is shown as follows

<!-- b000360 | furniture | pages [11] -->


<!-- b000361 | furniture | pages [11] -->


<!-- b000362 | furniture | pages [11] -->


<!-- b000363 | furniture | pages [11] -->


<!-- b000364 | furniture | pages [11] -->


<!-- b000365 | furniture | pages [11] -->


<!-- b000366 | furniture | pages [11] -->


<!-- b000367 | furniture | pages [11] -->


<!-- b000368 | furniture | pages [12] -->
Team #44398                                                    Page 12 of 51

<!-- b000369 | furniture | pages [12] -->


<!-- b000370 | prose | pages [12] -->
 2

<!-- b000371 | prose | pages [12] -->
ft

<!-- b000372 | prose | pages [12] -->
t

<!-- b000373 | prose | pages [12] -->
 1

<!-- b000374 | furniture | pages [12] -->


<!-- b000375 | furniture | pages [12] -->


<!-- b000376 | furniture | pages [12] -->


<!-- b000377 | furniture | pages [12] -->


<!-- b000378 | prose | pages [12] -->
 2

<!-- b000379 | prose | pages [12] -->
ft

<!-- b000380 | furniture | pages [12] -->


<!-- b000381 | furniture | pages [12] -->


<!-- b000382 | furniture | pages [12] -->


<!-- b000383 | furniture | pages [12] -->


<!-- b000384 | prose | pages [12] -->
 2

<!-- b000385 | furniture | pages [12] -->


<!-- b000386 | furniture | pages [12] -->


<!-- b000387 | prose | pages [12] -->
t

<!-- b000388 | caption | pages [12] -->
Fig.3  The sketch of bathtub heat transfer

<!-- b000389 | prose | pages [12] -->
As we can see in the above figure, the hot water in a bathtub has six radiating surfaces. On top surface transfers heat directly with air. The other surfaces transfer heat firstly with bathtub inner surfaces. Then the heat conducts through the bathtub and be transferred into air.

<!-- b000390 | prose | pages [12] -->
As for the top radiating surface, we derive the amount of radiating heat

<!-- b000391 | prose | pages [12] -->
 with the aid of Newton cooling formula 1

<!-- b000392 | prose | pages [12] -->
 hA t

<!-- b000393 | furniture | pages [12] -->


<!-- b000394 | prose | pages [12] -->
1     （16） t

<!-- b000395 | furniture | pages [12] -->


<!-- b000396 | prose | pages [12] -->
f f

<!-- b000397 | prose | pages [12] -->
In reality, the bathtub manufacturers tend to add some layers of thermal insulation materials to decrease the heat loss. So the boundary of a bathtub is made up by different material layers.

<!-- b000398 | furniture | pages [12] -->


<!-- b000399 | prose | pages [12] -->
t t w1 w2

<!-- b000400 | furniture | pages [12] -->


<!-- b000401 | prose | pages [12] -->
ft

<!-- b000402 | furniture | pages [12] -->


<!-- b000403 | furniture | pages [12] -->


<!-- b000404 | prose | pages [12] -->
1h

<!-- b000405 | furniture | pages [12] -->


<!-- b000406 | furniture | pages [12] -->


<!-- b000407 | prose | pages [12] -->
1k

<!-- b000408 | furniture | pages [12] -->


<!-- b000409 | prose | pages [12] -->


<!-- b000410 | furniture | pages [12] -->


<!-- b000411 | prose | pages [12] -->
 1

<!-- b000412 | furniture | pages [12] -->


<!-- b000413 | furniture | pages [12] -->


<!-- b000414 | furniture | pages [12] -->


<!-- b000415 | prose | pages [12] -->
t w3

<!-- b000416 | prose | pages [12] -->
2h

<!-- b000417 | prose | pages [12] -->
2k 2k

<!-- b000418 | prose | pages [12] -->
t

<!-- b000419 | prose | pages [12] -->
2 2

<!-- b000420 | prose | pages [12] -->
Layers of thermal Inside the tub

<!-- b000421 | furniture | pages [12] -->


<!-- b000422 | prose | pages [12] -->
Outside the tub insulation materials

<!-- b000423 | furniture | pages [12] -->


<!-- b000424 | caption | pages [12] -->
Fig.4  The sketch of boundary heat transfer

<!-- b000425 | prose | pages [12] -->
k are thermal conductivity of the inner and outer layer 1k and In Fig.4, 2

<!-- b000426 | furniture | pages [12] -->


<!-- b000427 | furniture | pages [13] -->
Team #44398                                                    Page 13 of 51

<!-- b000428 | prose | pages [13] -->
 and of thermal insulation materials.

<!-- b000429 | prose | pages [13] -->
1  are the thickness of the inner and 2 outer layer of thermal insulation materials. The heat transfer coefficient 1h . The heat transfer between the hot water and inner surface of the bathtub is

<!-- b000430 | prose | pages [13] -->
t t h .

<!-- b000431 | prose | pages [13] -->
t coefficient between air and outer surface of the bathtub is , and

<!-- b000432 | furniture | pages [13] -->


<!-- b000433 | prose | pages [13] -->
w1 w3 w2 2 are the temperatures of three boundaries of the thermal insulation material layers.

<!-- b000434 | prose | pages [13] -->
According to heat conduction formula, we have

<!-- b000435 | prose | pages [13] -->


<!-- b000436 | prose | pages [13] -->
=

<!-- b000437 | furniture | pages [13] -->


<!-- b000438 | prose | pages [13] -->
2

<!-- b000439 | prose | pages [13] -->


<!-- b000440 | prose | pages [13] -->
1 1

<!-- b000441 | prose | pages [13] -->
 

<!-- b000442 | prose | pages [13] -->
A h

<!-- b000443 | prose | pages [13] -->


<!-- b000444 | prose | pages [13] -->
1

<!-- b000445 | prose | pages [13] -->


<!-- b000446 | prose | pages [13] -->
t t t

<!-- b000447 | prose | pages [13] -->


<!-- b000448 | prose | pages [13] -->
f f

<!-- b000449 | prose | pages [13] -->
（17）

<!-- b000450 | furniture | pages [13] -->


<!-- b000451 | prose | pages [13] -->


<!-- b000452 | prose | pages [13] -->
  

<!-- b000453 | prose | pages [13] -->
1

<!-- b000454 | prose | pages [13] -->
 

<!-- b000455 | prose | pages [13] -->
1 1 2

<!-- b000456 | prose | pages [13] -->


<!-- b000457 | prose | pages [13] -->
k k k h

<!-- b000458 | prose | pages [13] -->


<!-- b000459 | prose | pages [13] -->
1 1 2 2

<!-- b000460 | prose | pages [13] -->
Hence the total heat dissipation capacity is

<!-- b000461 | prose | pages [13] -->


<!-- b000462 | furniture | pages [13] -->


<!-- b000463 | heading | pages [13] -->
5.2  Results

<!-- b000464 | prose | pages [13] -->
（18） 1 1 2

<!-- b000465 | prose | pages [13] -->
We first give the value of parameters based on others’ studies. Then we get the calculation results and simulating results via those data.

<!-- b000466 | heading | pages [13] -->
5.2.1  Determination of Parameters

<!-- b000467 | prose | pages [13] -->
After establishing the model, we have to determine the value of some important parameters.

<!-- b000468 | prose | pages [13] -->
As scholar Beum Kim points out, the optimal temperature for bath is between 41 and 45℃[1]. Meanwhile, according to Shimodozono’s study, 41℃ warm water bath is the perfect choice for individual health [2]. So it is reasonable for us to focus on 41℃~45℃. Because adding hot water continuously is a steady process, so the mean temperature of bath water is supposed to be constant. We value the temperature of inflow and outflow water with the maximum and minimum temperature respectively.

<!-- b000469 | prose | pages [13] -->
The values of all parameters needed are shown as follows:

<!-- b000470 | furniture | pages [13] -->


<!-- b000471 | furniture | pages [13] -->


<!-- b000472 | furniture | pages [13] -->


<!-- b000473 | furniture | pages [13] -->


<!-- b000474 | furniture | pages [13] -->


<!-- b000475 | furniture | pages [13] -->


<!-- b000476 | furniture | pages [13] -->


<!-- b000477 | furniture | pages [13] -->


<!-- b000478 | furniture | pages [13] -->


<!-- b000479 | furniture | pages [13] -->


<!-- b000480 | furniture | pages [14] -->
Team #44398                                                    Page 14 of 51

<!-- b000481 | caption | pages [14] -->
Table 2  The values of parameters

<!-- b000482 | prose | pages [14] -->
Parameters

<!-- b000483 | prose | pages [14] -->
int

<!-- b000484 | prose | pages [14] -->
t

<!-- b000485 | furniture | pages [14] -->


<!-- b000486 | prose | pages [14] -->
out

<!-- b000487 | prose | pages [14] -->
ft t

<!-- b000488 | prose | pages [14] -->
1

<!-- b000489 | prose | pages [14] -->
 2

<!-- b000490 | prose | pages [14] -->
1h

<!-- b000491 | prose | pages [14] -->
1h

<!-- b000492 | prose | pages [14] -->
1k

<!-- b000493 | prose | pages [14] -->
2k

<!-- b000494 | prose | pages [14] -->
c p 

<!-- b000495 | prose | pages [14] -->


<!-- b000496 | prose | pages [14] -->
M a b c * *

<!-- b000497 | prose | pages [14] -->
Values Unit

<!-- b000498 | prose | pages [14] -->
℃ 45

<!-- b000499 | prose | pages [14] -->
℃ 41

<!-- b000500 | prose | pages [14] -->
℃ 43 ℃ 25

<!-- b000501 | prose | pages [14] -->
mm 0.64

<!-- b000502 | prose | pages [14] -->
mm 30

<!-- b000503 | prose | pages [14] -->
 2 W / (m K) 10

<!-- b000504 | furniture | pages [14] -->


<!-- b000505 | prose | pages [14] -->
 2 W / (m K) 300

<!-- b000506 | furniture | pages [14] -->


<!-- b000507 | prose | pages [14] -->
 W / (m K) 0.19

<!-- b000508 | furniture | pages [14] -->


<!-- b000509 | prose | pages [14] -->
 W / (m K) 0.036

<!-- b000510 | furniture | pages [14] -->


<!-- b000511 | prose | pages [14] -->
 J / (kg K) 4174

<!-- b000512 | furniture | pages [14] -->


<!-- b000513 | prose | pages [14] -->
0.85 None

<!-- b000514 | prose | pages [14] -->
3 kg / m 992

<!-- b000515 | prose | pages [14] -->
kg 320 3 m 1.8*0.9*0.64 V

<!-- b000516 | heading | pages [14] -->
5.2.2  Calculating Results

<!-- b000517 | prose | pages [14] -->
3 m 0.32

<!-- b000518 | prose | pages [14] -->
Putting the above value of parameters into the equations we derived before, we can get the some data as follows

<!-- b000519 | caption | pages [14] -->
Table 3  The calculating results

<!-- b000520 | prose | pages [14] -->
Variables

<!-- b000521 | prose | pages [14] -->
1A

<!-- b000522 | prose | pages [14] -->
A 2

<!-- b000523 | prose | pages [14] -->
 1

<!-- b000524 | prose | pages [14] -->
 2

<!-- b000525 | prose | pages [14] -->


<!-- b000526 | prose | pages [14] -->
q m

<!-- b000527 | prose | pages [14] -->
Values Unit

<!-- b000528 | prose | pages [14] -->
2 m 1.05

<!-- b000529 | prose | pages [14] -->
2 m 2.24

<!-- b000530 | prose | pages [14] -->
W 189.00

<!-- b000531 | prose | pages [14] -->
W 43.47

<!-- b000532 | prose | pages [14] -->
W 232.47

<!-- b000533 | prose | pages [14] -->
g/s 0.014

<!-- b000534 | prose | pages [14] -->
In this table, we find the whole amount of radiating heat of the bathtub is 232.47 W. Based on industrial standards, the bathtub we chose has capacity of 320L. The temperature of inflow and outflow water is designed to be 45 and 41℃, the mass flow turns out to be 0.014 g/s (that is 0.84 kg/min ). Only this

<!-- b000535 | furniture | pages [14] -->


<!-- b000536 | furniture | pages [15] -->
Team #44398                                                    Page 15 of 51

<!-- b000537 | prose | pages [15] -->
condition is satisfied can the temperature throughout the bathtub be kept as even as possible.

<!-- b000538 | heading | pages [15] -->
5.2.3  Simulating Results

<!-- b000539 | prose | pages [15] -->
It is quite unrealistic for us to compute the equations (1)-(5) because the N- S equation is coupled to the energy equation. In order to derive the temperature field, the velocity field is needed. Then introduce the boundary conditions, the temperature field is worked out. However, this method is so difficult that The Clay Mathematics Institute of Cambridge, Massachusetts (CMI) even sets prize to inspire people to solve it. So we have to employ Computational Fluid Dynamics (CFD) to simulate the temperature field based on those equations.

<!-- b000540 | prose | pages [15] -->
We will proceed as follows:

<!-- b000541 | heading | pages [15] -->
 Step 1: Via Gambit software, we establish the three-dimensional model and

<!-- b000542 | prose | pages [15] -->
divide meshes. Then we define the boundary type.

<!-- b000543 | prose | pages [15] -->
 Step 2: Using Fluent software to read and examine the meshes.

<!-- b000544 | heading | pages [15] -->
 Step 3: Defining solving model. We introduce Laminar Model to simulate

<!-- b000545 | prose | pages [15] -->
the N-S equation and Energy Model to simulate the energy equation.

<!-- b000546 | prose | pages [15] -->
 Step 4: Defining the materials and correcting the corresponding physical

<!-- b000547 | prose | pages [15] -->
property parameters.

<!-- b000548 | prose | pages [15] -->
 Step 5: Defining the boundary conditions.

<!-- b000549 | prose | pages [15] -->
 Step 6: Solving initialization.

<!-- b000550 | prose | pages [15] -->
 Step 7: Setting number of iterations.

<!-- b000551 | prose | pages [15] -->
 Step 8: The results are derived when the convergence conditions are met.

<!-- b000552 | prose | pages [15] -->
Applying the above steps in our first sub-model, the results turn out to be satisfying.

<!-- b000553 | prose | pages [15] -->
First of all, we divide meshes with the aid of Gambit software, which is shown in the following figure.

<!-- b000554 | furniture | pages [15] -->


<!-- b000555 | furniture | pages [15] -->


<!-- b000556 | furniture | pages [15] -->


<!-- b000557 | furniture | pages [15] -->


<!-- b000558 | furniture | pages [15] -->


<!-- b000559 | furniture | pages [15] -->


<!-- b000560 | furniture | pages [15] -->


<!-- b000561 | furniture | pages [16] -->
Team #44398                                                    Page 16 of 51

<!-- b000562 | furniture | pages [16] -->


<!-- b000563 | furniture | pages [16] -->


<!-- b000564 | furniture | pages [16] -->


<!-- b000565 | furniture | pages [16] -->


<!-- b000566 | furniture | pages [16] -->


<!-- b000567 | furniture | pages [16] -->


<!-- b000568 | furniture | pages [16] -->


<!-- b000569 | furniture | pages [16] -->


<!-- b000570 | furniture | pages [16] -->


<!-- b000571 | furniture | pages [16] -->


<!-- b000572 | furniture | pages [16] -->


<!-- b000573 | furniture | pages [16] -->


<!-- b000574 | caption | pages [16] -->
Fig.5  Divide meshes in Gambit

<!-- b000575 | prose | pages [16] -->
As is shown in Fig.5, we divide the hot water into 129600 meshes. Then we export the Mesh file then import it into Fluent and make corresponding settings. Afterwards, we begin to compute it by iteration. When the iteration is conducted for 379 times, the problem is nearly convergent. The curve of residual is shown in Fig.5.

<!-- b000576 | furniture | pages [16] -->


<!-- b000577 | furniture | pages [16] -->


<!-- b000578 | furniture | pages [16] -->


<!-- b000579 | furniture | pages [16] -->


<!-- b000580 | furniture | pages [16] -->


<!-- b000581 | furniture | pages [16] -->


<!-- b000582 | furniture | pages [16] -->


<!-- b000583 | furniture | pages [16] -->


<!-- b000584 | furniture | pages [16] -->


<!-- b000585 | furniture | pages [16] -->


<!-- b000586 | furniture | pages [16] -->


<!-- b000587 | furniture | pages [16] -->


<!-- b000588 | caption | pages [16] -->
Fig.6  The curve of residual

<!-- b000589 | prose | pages [16] -->
Combining specific boundary conditions, we have the temperature field throughout the bathtub. In reality, there are various ways of water inflow and outflow. We design the water to flow into the bathtub from left side and out of

<!-- b000590 | prose | pages [16] -->
the bathtub from the right side.

<!-- b000591 | prose | pages [16] -->
We take the temperature field of two surfaces as examples.

<!-- b000592 | furniture | pages [16] -->


<!-- b000593 | furniture | pages [16] -->


<!-- b000594 | furniture | pages [16] -->


<!-- b000595 | furniture | pages [17] -->
Team #44398                                                    Page 17 of 51

<!-- b000596 | furniture | pages [17] -->


<!-- b000597 | furniture | pages [17] -->


<!-- b000598 | furniture | pages [17] -->


<!-- b000599 | furniture | pages [17] -->


<!-- b000600 | furniture | pages [17] -->


<!-- b000601 | furniture | pages [17] -->


<!-- b000602 | furniture | pages [17] -->


<!-- b000603 | furniture | pages [17] -->


<!-- b000604 | furniture | pages [17] -->


<!-- b000605 | caption | pages [17] -->
Fig.7 (a)  The temperature field of the bottom surface

<!-- b000606 | furniture | pages [17] -->


<!-- b000607 | furniture | pages [17] -->


<!-- b000608 | furniture | pages [17] -->


<!-- b000609 | furniture | pages [17] -->


<!-- b000610 | furniture | pages [17] -->


<!-- b000611 | furniture | pages [17] -->


<!-- b000612 | furniture | pages [17] -->


<!-- b000613 | furniture | pages [17] -->


<!-- b000614 | furniture | pages [17] -->


<!-- b000615 | furniture | pages [17] -->


<!-- b000616 | furniture | pages [17] -->


<!-- b000617 | furniture | pages [17] -->


<!-- b000618 | furniture | pages [17] -->


<!-- b000619 | furniture | pages [17] -->


<!-- b000620 | furniture | pages [17] -->


<!-- b000621 | caption | pages [17] -->
Fig.7 (b)  The temperature field of the side surface

<!-- b000622 | prose | pages [17] -->
where ‘the bottom surface’ means the x-O-y surface while ‘the side surface’ is the y-O-z

<!-- b000623 | prose | pages [17] -->
surface of the water cube in Fig2. The temperature shown in the legend is presented in

<!-- b000624 | prose | pages [17] -->
Kelvin scale and the data should be expended to 100 times.

<!-- b000625 | prose | pages [17] -->
As we can see in the figures, the temperature in the bathtub is different from area to area, which decreases along the direction of water flow. However, the temperature fluctuates between 43 to 45 ℃(316-318 K). The highest temperature is that of inflow area because the adding water is the hottest. In addition, due to the stability of this model when a person adds hot water continually, the temperature of each area remains stable.

<!-- b000626 | prose | pages [17] -->
In conclusion, the temperature is not strictly even throughout the bathtub. It differs according to boundary conditions. However, the mean temperature of the whole water in the bathtub is stable.

<!-- b000627 | prose | pages [17] -->
By the way, because of the shortage of Fluent software in simulating small water flow, the temperature marked by different colors may differ a little. For example, in the legend, 44℃(317 K) corresponds with colors ranging from blue

<!-- b000628 | prose | pages [17] -->
to orange. Actually, each color represents a different temperature  between 44- 45 ℃(317-318K). The changing tendency of colors strictly represents the changing tendency of the temperature.

<!-- b000629 | furniture | pages [17] -->


<!-- b000630 | furniture | pages [18] -->
Team #44398                                                    Page 18 of 51

<!-- b000631 | heading | pages [18] -->
6  Sub-model II: Adding Water Discontinuously

<!-- b000632 | prose | pages [18] -->
In order to establish the unsteady sub-model, we recall on the working

<!-- b000633 | prose | pages [18] -->
principle of air conditioners. The heating performance of air conditions consist of two processes: heating and standby. After the user set a temperature, the air conditioner will begin to heat until the expected temperature is reached. Then it will go standby. When the temperature get below the expected temperature, the air conditioner begin to work again. As it works in this circle, the temperature remains the expected one.

<!-- b000634 | prose | pages [18] -->
Inspired by this, we divide the bathtub working into two processes: adding hot water until the expected temperature is reached, then keeping this condition for a while unless the temperature is lower than a specific value. Iterating this circle ceaselessly will ensure the temperature kept relatively stable.

<!-- b000635 | heading | pages [18] -->
6.1  Heating Model

<!-- b000636 | heading | pages [18] -->
6.1.1  Control Equations and Boundary Conditions

<!-- b000637 | prose | pages [18] -->
We focus on heating process at first. During this process, the hot water

<!-- b000638 | prose | pages [18] -->
flows throughout the bathtub so we need to use N-S equation. We also have to introduce energy equation considering there is convective heat transfer in the flow.

<!-- b000639 | prose | pages [18] -->
Adding an unsteady term into basic N-S equation [3], we have

<!-- b000640 | prose | pages [18] -->
    u u u u     ( u v w )

<!-- b000641 | furniture | pages [18] -->


<!-- b000642 | prose | pages [18] -->
     x y z    

<!-- b000643 | prose | pages [18] -->
2 2 2

<!-- b000644 | prose | pages [18] -->
p u u u      ( ) （19）

<!-- b000645 | furniture | pages [18] -->


<!-- b000646 | prose | pages [18] -->
    2 2 2 x x y z

<!-- b000647 | prose | pages [18] -->
The above equation is established along x-axis. The other two equations along y-axis and z-axis can be easily deduced so we omit them.

<!-- b000648 | prose | pages [18] -->
Similarly, we add unsteady term into energy equation and get

<!-- b000649 | prose | pages [18] -->
   t t t    c

<!-- b000650 | prose | pages [18] -->
(

<!-- b000651 | prose | pages [18] -->
u v

<!-- b000652 | prose | pages [18] -->
+

<!-- b000653 | prose | pages [18] -->
w

<!-- b000654 | furniture | pages [18] -->


<!-- b000655 | prose | pages [18] -->
p

<!-- b000656 | prose | pages [18] -->
    x y     

<!-- b000657 | prose | pages [18] -->
2 2 2

<!-- b000658 | prose | pages [18] -->
t t t t t    

<!-- b000659 | prose | pages [18] -->
) ( )

<!-- b000660 | prose | pages [18] -->
（20）

<!-- b000661 | furniture | pages [18] -->


<!-- b000662 | prose | pages [18] -->
    

<!-- b000663 | prose | pages [18] -->
2 2 2

<!-- b000664 | prose | pages [18] -->
z z x y z

<!-- b000665 | prose | pages [18] -->
As for the boundary conditions, (6)-(12) are also suitable for this model. Except those, there are two other conditions:

<!-- b000666 | prose | pages [18] -->
 when

<!-- b000667 | furniture | pages [18] -->


<!-- b000668 | furniture | pages [18] -->


<!-- b000669 | prose | pages [18] -->
  when

<!-- b000670 | furniture | pages [18] -->


<!-- b000671 | furniture | pages [18] -->


<!-- b000672 | furniture | pages [18] -->


<!-- b000673 | prose | pages [18] -->
t

<!-- b000674 | prose | pages [18] -->
 （21） 0 t t ，

<!-- b000675 | furniture | pages [18] -->


<!-- b000676 | prose | pages [18] -->
f

<!-- b000677 | prose | pages [18] -->
   （22） , t t

<!-- b000678 | furniture | pages [18] -->


<!-- b000679 | prose | pages [18] -->
0 0 f min

<!-- b000680 | prose | pages [18] -->
is the minimum of mean temperature of bath water. where min

<!-- b000681 | furniture | pages [18] -->


<!-- b000682 | furniture | pages [19] -->
Team #44398                                                    Page 19 of 51

<!-- b000683 | heading | pages [19] -->
6.1.2  Determination of Inflow Time and Amount

<!-- b000684 | prose | pages [19] -->
The bathtub can be simplified as a water containment vessel, so the amount

<!-- b000685 | prose | pages [19] -->
of inflow and outflow is the equal in value. Hence the mass of the bath water in a bathtub is constant. That is

<!-- b000686 | prose | pages [19] -->
 q q

<!-- b000687 | furniture | pages [19] -->


<!-- b000688 | prose | pages [19] -->
m （23） = q

<!-- b000689 | furniture | pages [19] -->


<!-- b000690 | prose | pages [19] -->
in in out

<!-- b000691 | prose | pages [19] -->
t  and the We let initial mean temperature of bath water to be f1 int . Frequently, the mean temperature will temperature of inflow water to be rise as hot water added, which leads the temperature of outflow to rise. We let the final temperature of outflow to be t and t t t . out2 are functions of time. Both f1 out2

<!-- b000692 | prose | pages [19] -->
   t f

<!-- b000693 | furniture | pages [19] -->


<!-- b000694 | prose | pages [19] -->
f    , , t t g （24）

<!-- b000695 | furniture | pages [19] -->


<!-- b000696 | prose | pages [19] -->
out

<!-- b000697 | prose | pages [19] -->
We assume the bath water in bathtub as a control volume, so the energy stored in bathtub is the difference between the energy of inflow and outflow. This can be seen in the following figure.

<!-- b000698 | furniture | pages [19] -->


<!-- b000699 | furniture | pages [19] -->


<!-- b000700 | furniture | pages [19] -->


<!-- b000701 | furniture | pages [19] -->


<!-- b000702 | furniture | pages [19] -->


<!-- b000703 | furniture | pages [19] -->


<!-- b000704 | furniture | pages [19] -->


<!-- b000705 | caption | pages [19] -->
Fig.8  The transfer and storage of energy

<!-- b000706 | prose | pages [19] -->
The total heat dissipating capacity turns out to be

<!-- b000707 | prose | pages [19] -->
 Q

<!-- b000708 | prose | pages [19] -->
out =

<!-- b000709 | furniture | pages [19] -->


<!-- b000710 | prose | pages [19] -->
T

<!-- b000711 | prose | pages [19] -->
1

<!-- b000712 | prose | pages [19] -->
We also derive that

<!-- b000713 | prose | pages [19] -->
  

<!-- b000714 | prose | pages [19] -->
   

<!-- b000715 | prose | pages [19] -->
t hA t t

<!-- b000716 | furniture | pages [19] -->


<!-- b000717 | prose | pages [19] -->


<!-- b000718 | prose | pages [19] -->
f 1 f

<!-- b000719 | prose | pages [19] -->


<!-- b000720 | prose | pages [19] -->
    d （25）

<!-- b000721 | furniture | pages [19] -->


<!-- b000722 | prose | pages [19] -->


<!-- b000723 | prose | pages [19] -->
t t

<!-- b000724 | prose | pages [19] -->


<!-- b000725 | prose | pages [19] -->
（26）

<!-- b000726 | prose | pages [19] -->
f

<!-- b000727 | furniture | pages [19] -->


<!-- b000728 | prose | pages [19] -->
 

<!-- b000729 | prose | pages [19] -->
 

<!-- b000730 | prose | pages [19] -->
1 1 1 1

<!-- b000731 | prose | pages [19] -->
  

<!-- b000732 | prose | pages [19] -->
1 2

<!-- b000733 | prose | pages [19] -->
 

<!-- b000734 | prose | pages [19] -->
A A h k k h

<!-- b000735 | prose | pages [19] -->
 

<!-- b000736 | prose | pages [19] -->
2 2 1 1 2 2

<!-- b000737 | prose | pages [19] -->
As the temperature of inflow water is higher than that of bath water in the

<!-- b000738 | prose | pages [19] -->
bathtub, so the inflow will transfer heat into the bath water. The energy that bath water gets is equal in value to the enthalpy difference between inflow and outflow. Hence

<!-- b000739 | prose | pages [19] -->
 mc

<!-- b000740 | furniture | pages [19] -->


<!-- b000741 | prose | pages [19] -->
in

<!-- b000742 | furniture | pages [19] -->


<!-- b000743 | prose | pages [19] -->
    t t （27）

<!-- b000744 | furniture | pages [19] -->


<!-- b000745 | prose | pages [19] -->
p p f 2 f1

<!-- b000746 | furniture | pages [20] -->
Team #44398                                                    Page 20 of 51

<!-- b000747 | prose | pages [20] -->
Referring to formula (15), we have

<!-- b000748 | prose | pages [20] -->
t in t f 2=

<!-- b000749 | furniture | pages [20] -->


<!-- b000750 | prose | pages [20] -->
  t out2 （28）

<!-- b000751 | furniture | pages [20] -->


<!-- b000752 | prose | pages [20] -->
2

<!-- b000753 | prose | pages [20] -->
The enthalpy difference between inflow and outflow is very the energy added into bath water. That is

<!-- b000754 | prose | pages [20] -->
  Q q c

<!-- b000755 | furniture | pages [20] -->


<!-- b000756 | prose | pages [20] -->
m p T

<!-- b000757 | prose | pages [20] -->
1

<!-- b000758 | prose | pages [20] -->
  

<!-- b000759 | prose | pages [20] -->
 d t t t （29）

<!-- b000760 | furniture | pages [20] -->


<!-- b000761 | prose | pages [20] -->
in in out

<!-- b000762 | prose | pages [20] -->
According to energy conservation principle, it follows that

<!-- b000763 | prose | pages [20] -->
 Q Q

<!-- b000764 | furniture | pages [20] -->


<!-- b000765 | prose | pages [20] -->
 Q （30）

<!-- b000766 | furniture | pages [20] -->


<!-- b000767 | prose | pages [20] -->
in in out

<!-- b000768 | prose | pages [20] -->
t , the heating process is When the temperature of bath water reaches f 2 stopped. Based on these above relationships, we derive the time of adding hot 1T and the corresponding amount of inflow water

<!-- b000769 | heading | pages [20] -->
6.2  Standby Model

<!-- b000770 | heading | pages [20] -->
6.2.1  Process Analysis

<!-- b000771 | prose | pages [20] -->
q . m

<!-- b000772 | prose | pages [20] -->
After the heating process is finished, the mean temperature of bath water

<!-- b000773 | prose | pages [20] -->
t . In standby process, it is assumed to be put in a space of which the is f 2 temperature is t and transfer heat into the space. Finally, the temperature f1t and the next iteration begins. During decreases to a specific temperature ft the standby process, the mean temperature of bath water is expressed by which is a function of time.

<!-- b000774 | heading | pages [20] -->
6.2.2  Calculation of Parameters

<!-- b000775 | prose | pages [20] -->
Throughout the whole process of cooling, the bath water transfer heat to the surroundings via convection or other ways. So that its internal energy is reduced as time goes by.

<!-- b000776 | prose | pages [20] -->
We take the whole bath water as a control volume and derive the energy balance equation:

<!-- b000777 | prose | pages [20] -->
dt

<!-- b000778 | prose | pages [20] -->


<!-- b000779 | prose | pages [20] -->
 c V

<!-- b000780 | furniture | pages [20] -->


<!-- b000781 | prose | pages [20] -->
p

<!-- b000782 | prose | pages [20] -->
 d

<!-- b000783 | prose | pages [20] -->
The initial conditions are

<!-- b000784 | prose | pages [20] -->
 when =0

<!-- b000785 | furniture | pages [20] -->


<!-- b000786 | prose | pages [20] -->
 

<!-- b000787 | prose | pages [20] -->
  

<!-- b000788 | prose | pages [20] -->
hA t t

<!-- b000789 | prose | pages [20] -->
（31）

<!-- b000790 | furniture | pages [20] -->


<!-- b000791 | prose | pages [20] -->


<!-- b000792 | prose | pages [20] -->
 t t （32） ，

<!-- b000793 | furniture | pages [20] -->


<!-- b000794 | prose | pages [20] -->
f2

<!-- b000795 | prose | pages [20] -->
  when

<!-- b000796 | furniture | pages [20] -->


<!-- b000797 | furniture | pages [20] -->


<!-- b000798 | prose | pages [20] -->
 t t （33） ，

<!-- b000799 | furniture | pages [20] -->


<!-- b000800 | prose | pages [20] -->


<!-- b000801 | prose | pages [20] -->
According to before discussion and based on the surfaces of the control

<!-- b000802 | furniture | pages [20] -->


<!-- b000803 | furniture | pages [21] -->
Team #44398                                                    Page 21 of 51

<!-- b000804 | prose | pages [21] -->
volume, we have

<!-- b000805 | prose | pages [21] -->
 

<!-- b000806 | prose | pages [21] -->
hA hA

<!-- b000807 | furniture | pages [21] -->


<!-- b000808 | prose | pages [21] -->
1

<!-- b000809 | prose | pages [21] -->


<!-- b000810 | prose | pages [21] -->
1

<!-- b000811 | prose | pages [21] -->
 A h 

<!-- b000812 | prose | pages [21] -->
2

<!-- b000813 | prose | pages [21] -->
1

<!-- b000814 | prose | pages [21] -->
（34）

<!-- b000815 | furniture | pages [21] -->


<!-- b000816 | prose | pages [21] -->
  

<!-- b000817 | prose | pages [21] -->
1 1 1

<!-- b000818 | prose | pages [21] -->
  

<!-- b000819 | prose | pages [21] -->
1 2

<!-- b000820 | prose | pages [21] -->
 k k h 

<!-- b000821 | prose | pages [21] -->
1 1 1 2 2

<!-- b000822 | prose | pages [21] -->
Then we integrating t over  in formula (31) and get

<!-- b000823 | prose | pages [21] -->


<!-- b000824 | prose | pages [21] -->
  

<!-- b000825 | prose | pages [21] -->
t t t t

<!-- b000826 | furniture | pages [21] -->


<!-- b000827 | prose | pages [21] -->
 

<!-- b000828 | prose | pages [21] -->
f 2

<!-- b000829 | prose | pages [21] -->
 

<!-- b000830 | prose | pages [21] -->
hA

<!-- b000831 | prose | pages [21] -->
 

<!-- b000832 | prose | pages [21] -->


<!-- b000833 | prose | pages [21] -->
c V 

<!-- b000834 | prose | pages [21] -->
 

<!-- b000835 | prose | pages [21] -->
exp

<!-- b000836 | prose | pages [21] -->
（35）

<!-- b000837 | furniture | pages [21] -->


<!-- b000838 | prose | pages [21] -->
 

<!-- b000839 | prose | pages [21] -->


<!-- b000840 | prose | pages [21] -->
 

<!-- b000841 | prose | pages [21] -->
p

<!-- b000842 | prose | pages [21] -->
f1t , the time of standby process turns When the temperature decreases to out to be

<!-- b000843 | prose | pages [21] -->


<!-- b000844 | prose | pages [21] -->
pc V

<!-- b000845 | prose | pages [21] -->


<!-- b000846 | prose | pages [21] -->
T

<!-- b000847 | furniture | pages [21] -->


<!-- b000848 | prose | pages [21] -->
2 hA

<!-- b000849 | prose | pages [21] -->


<!-- b000850 | prose | pages [21] -->
t t

<!-- b000851 | prose | pages [21] -->


<!-- b000852 | prose | pages [21] -->
ln f1

<!-- b000853 | prose | pages [21] -->
（36）

<!-- b000854 | furniture | pages [21] -->


<!-- b000855 | prose | pages [21] -->


<!-- b000856 | prose | pages [21] -->
t t

<!-- b000857 | prose | pages [21] -->


<!-- b000858 | prose | pages [21] -->
f 2

<!-- b000859 | prose | pages [21] -->
The whole heat transfer capacity is

<!-- b000860 | prose | pages [21] -->


<!-- b000861 | prose | pages [21] -->
 

<!-- b000862 | prose | pages [21] -->


<!-- b000863 | prose | pages [21] -->


<!-- b000864 | prose | pages [21] -->
 

<!-- b000865 | prose | pages [21] -->
Q c V t t

<!-- b000866 | furniture | pages [21] -->


<!-- b000867 | prose | pages [21] -->


<!-- b000868 | prose | pages [21] -->


<!-- b000869 | prose | pages [21] -->
p f 2

<!-- b000870 | prose | pages [21] -->


<!-- b000871 | heading | pages [21] -->
6.3  Results

<!-- b000872 | prose | pages [21] -->
  

<!-- b000873 | prose | pages [21] -->
hA

<!-- b000874 | prose | pages [21] -->
     

<!-- b000875 | prose | pages [21] -->
1 exp

<!-- b000876 | prose | pages [21] -->
T

<!-- b000877 | prose | pages [21] -->
（37）

<!-- b000878 | furniture | pages [21] -->


<!-- b000879 | prose | pages [21] -->
  

<!-- b000880 | prose | pages [21] -->
2

<!-- b000881 | prose | pages [21] -->
 c V

<!-- b000882 | prose | pages [21] -->
  

<!-- b000883 | prose | pages [21] -->
p

<!-- b000884 | heading | pages [21] -->
6.3.1  Determination of Parameters

<!-- b000885 | prose | pages [21] -->
One of our goals is to keep the temperature even throughout the bathtub. So we firstly have to determine the value of corresponding parameters such as the initial temperature of inflow and outflow.

<!-- b000886 | prose | pages [21] -->
According to the data we use in the first sub-model, the temperature in the bathtub ranges between 41 to 45 ℃. In this sub-model, we still set the temperature of inflow water to be int 445 ℃. In order to give the user comfortable experience, we set the change of the mean temperature less than t f1=42 1℃.thus the lowest mean temperature t f 2=43 ℃.While the highest mean at ℃. The expected mean temperature turns out to be temperature 442.5℃. In that way, the maximum change of the mean temperature is only 0.5℃.

<!-- b000887 | prose | pages [21] -->
The other parameters will change over time. The change value cannot be expressed by specific functions. So we need to analyze them according to our model. We first focus on the different temperatures during the heating process.

<!-- b000888 | prose | pages [21] -->
The temperature of inflow remains stable. The temperature of outflow is stable for a while but begins to rise as hot water added. Meanwhile, the mean temperature also rises when the user adds hot water into the bathtub. The changing trend is shown as follows:

<!-- b000889 | furniture | pages [21] -->


<!-- b000890 | furniture | pages [22] -->
Team #44398                                                    Page 22 of 51

<!-- b000891 | furniture | pages [22] -->


<!-- b000892 | furniture | pages [22] -->


<!-- b000893 | furniture | pages [22] -->


<!-- b000894 | furniture | pages [22] -->


<!-- b000895 | furniture | pages [22] -->


<!-- b000896 | furniture | pages [22] -->


<!-- b000897 | furniture | pages [22] -->


<!-- b000898 | furniture | pages [22] -->


<!-- b000899 | furniture | pages [22] -->


<!-- b000900 | furniture | pages [22] -->


<!-- b000901 | furniture | pages [22] -->


<!-- b000902 | furniture | pages [22] -->


<!-- b000903 | caption | pages [22] -->
Fig.9  The changing trend of different temperature

<!-- b000904 | prose | pages [22] -->
From the above picture, we can see that the mean temperature remains rising. After the added hot water arrives at the outflow side, the temperature of cT to represent the time between outflow begins to be influenced. We let adding hot water and the temperature of outflow beginning to rise. This process can be divided into two parts:

<!-- b000905 | prose | pages [22] -->
 When the time is shorter than stable.

<!-- b000906 | prose | pages [22] -->
 When the time is longer than rise.

<!-- b000907 | prose | pages [22] -->
cT , the temperature of outflow remains

<!-- b000908 | prose | pages [22] -->
cT , the temperature of outflow begins to

<!-- b000909 | prose | pages [22] -->
1T is Then we need to determine whether the time of adding hot water cT . Recalling on the first sub-model, we derive that the longer or shorter than temperature of inflow is 45℃ while the temperature of outflow is 41℃. Under such circumstance, the mean temperature turns out to remain 43℃.

<!-- b000910 | prose | pages [22] -->
We assume the area that added hot water covers is in stable state. If we  T T , the whole hot water is in stable state. This is alike the firstly suppose 1 c first sub-model where the mean temperature is 43℃.However the expected 1T is longer mean temperature is 42.5℃, higher than 43℃. That means before cT , the mean temperature has reached 42.5℃. So it is untrue for us to than   T T T T . Based on that, the initial temperature of suppose . That is to say 1 c 1 c

<!-- b000911 | prose | pages [22] -->
outflow is equal to the value of the lowest mean temperature

<!-- b000912 | prose | pages [22] -->
 t t f1=42 ℃.Still, it is convenient for us to compute. out The value of corresponding parameters is listed in the following table.

<!-- b000913 | furniture | pages [22] -->


<!-- b000914 | furniture | pages [22] -->


<!-- b000915 | furniture | pages [23] -->
Team #44398                                                    Page 23 of 51

<!-- b000916 | caption | pages [23] -->
Table 4  The value of corresponding parameters

<!-- b000917 | prose | pages [23] -->
Parameters

<!-- b000918 | prose | pages [23] -->
int

<!-- b000919 | prose | pages [23] -->
t f1

<!-- b000920 | prose | pages [23] -->
t f 2

<!-- b000921 | prose | pages [23] -->
at

<!-- b000922 | prose | pages [23] -->
ft

<!-- b000923 | prose | pages [23] -->
t

<!-- b000924 | furniture | pages [23] -->


<!-- b000925 | prose | pages [23] -->
out

<!-- b000926 | heading | pages [23] -->
6.3.2  Calculating Results

<!-- b000927 | prose | pages [23] -->
Value Unit

<!-- b000928 | prose | pages [23] -->
℃ 45

<!-- b000929 | prose | pages [23] -->
℃ 42

<!-- b000930 | prose | pages [23] -->
℃ 43

<!-- b000931 | prose | pages [23] -->
℃ 42.5

<!-- b000932 | prose | pages [23] -->
℃ 43

<!-- b000933 | prose | pages [23] -->
℃ 42

<!-- b000934 | prose | pages [23] -->
q and the time of adding hot water The relationship between mass flow

<!-- b000935 | prose | pages [23] -->
1T is

<!-- b000936 | prose | pages [23] -->
 12522 Tq 232

<!-- b000937 | furniture | pages [23] -->


<!-- b000938 | prose | pages [23] -->
1 m

<!-- b000939 | prose | pages [23] -->
m

<!-- b000940 | prose | pages [23] -->
  T T 1333008 0 （38）

<!-- b000941 | furniture | pages [23] -->


<!-- b000942 | prose | pages [23] -->
1 1

<!-- b000943 | prose | pages [23] -->
Commonly, it will be better if the time of adding hot water is shorter.

<!-- b000944 | prose | pages [23] -->
T  3min According to some data from the Internet, we make . From formula 1

<!-- b000945 | prose | pages [23] -->
q 40.61kg/s. Putting these data into formulas (38)，we compute the mass flow m T 45914s (approximately 1.64h). (31)-(36), we find 2

<!-- b000946 | caption | pages [23] -->
Table 5  The calculating results

<!-- b000947 | prose | pages [23] -->
Parameters

<!-- b000948 | prose | pages [23] -->
1T

<!-- b000949 | prose | pages [23] -->
T 2

<!-- b000950 | prose | pages [23] -->
T

<!-- b000951 | prose | pages [23] -->
q m

<!-- b000952 | prose | pages [23] -->
Value Unit

<!-- b000953 | prose | pages [23] -->
3 min

<!-- b000954 | prose | pages [23] -->
1.64 h

<!-- b000955 | prose | pages [23] -->
101.4 min

<!-- b000956 | prose | pages [23] -->
0.61 kg/s

<!-- b000957 | prose | pages [23] -->
where T is the total time of an iteration.

<!-- b000958 | heading | pages [23] -->
6.3.3  Simulating Results

<!-- b000959 | prose | pages [23] -->
Because this sub-model is a three-dimensional problem, it is hard for us to simulate it by Fluent. The hot water of constant temperature flows into the bathtub and is mixed with the bath water, causing fluid convection. The

<!-- b000960 | prose | pages [23] -->
temperature field is symmetric so that we can simplify it as a two-dimensional problem. Although there are heat insulating materials around the bathtub, the heat transfer coefficient of forced convection of water is much larger than that of natural convection of air and water. So it is reasonable for us to simplify the

<!-- b000961 | furniture | pages [23] -->


<!-- b000962 | furniture | pages [24] -->
Team #44398                                                    Page 24 of 51

<!-- b000963 | prose | pages [24] -->
problem as a two-dimensional one.

<!-- b000964 | prose | pages [24] -->
Considering the simulating by a computer takes too much time, we set the mass flow of the inflow water to be 0.04m/s. The residual curve of simulation

<!-- b000965 | prose | pages [24] -->
is shown as follows.

<!-- b000966 | furniture | pages [24] -->


<!-- b000967 | furniture | pages [24] -->


<!-- b000968 | furniture | pages [24] -->


<!-- b000969 | furniture | pages [24] -->


<!-- b000970 | furniture | pages [24] -->


<!-- b000971 | furniture | pages [24] -->


<!-- b000972 | furniture | pages [24] -->


<!-- b000973 | furniture | pages [24] -->


<!-- b000974 | furniture | pages [24] -->


<!-- b000975 | furniture | pages [24] -->


<!-- b000976 | furniture | pages [24] -->


<!-- b000977 | caption | pages [24] -->
Fig.10  The residual curve of simulation

<!-- b000978 | prose | pages [24] -->
The change of temperature field is present in the following four pictures.

<!-- b000979 | furniture | pages [24] -->


<!-- b000980 | furniture | pages [24] -->


<!-- b000981 | furniture | pages [24] -->


<!-- b000982 | furniture | pages [24] -->


<!-- b000983 | furniture | pages [24] -->


<!-- b000984 | furniture | pages [24] -->


<!-- b000985 | furniture | pages [24] -->


<!-- b000986 | furniture | pages [24] -->


<!-- b000987 | furniture | pages [24] -->


<!-- b000988 | furniture | pages [24] -->


<!-- b000989 | prose | pages [24] -->
（a）=1s

<!-- b000990 | furniture | pages [24] -->


<!-- b000991 | furniture | pages [24] -->


<!-- b000992 | furniture | pages [24] -->


<!-- b000993 | furniture | pages [24] -->


<!-- b000994 | furniture | pages [24] -->


<!-- b000995 | furniture | pages [24] -->


<!-- b000996 | furniture | pages [24] -->


<!-- b000997 | furniture | pages [24] -->


<!-- b000998 | prose | pages [24] -->
(b) t=2s                     (c) t=10s

<!-- b000999 | furniture | pages [24] -->


<!-- b001000 | furniture | pages [25] -->
Team #44398                                                    Page 25 of 51

<!-- b001001 | furniture | pages [25] -->


<!-- b001002 | furniture | pages [25] -->


<!-- b001003 | furniture | pages [25] -->


<!-- b001004 | furniture | pages [25] -->


<!-- b001005 | furniture | pages [25] -->


<!-- b001006 | furniture | pages [25] -->


<!-- b001007 | furniture | pages [25] -->


<!-- b001008 | furniture | pages [25] -->


<!-- b001009 | furniture | pages [25] -->


<!-- b001010 | prose | pages [25] -->
(d) t=20s                      (e) t=30s

<!-- b001011 | caption | pages [25] -->
Fig.11  The change of temperature field

<!-- b001012 | prose | pages [25] -->
where the picture (a) is the complete representation of the temperature field while

<!-- b001013 | prose | pages [25] -->
pictures (b)-(e) are partial representation of the temperature field. The temperature in the

<!-- b001014 | prose | pages [25] -->
legend is presented in Kelvin scale and the data should be expended to 100 times.

<!-- b001015 | prose | pages [25] -->
From the figure of the residual curve of simulation, we can find that the residual changes periodically and the change is small, which indicates the stability of the simulating results. Limited to time, we simulate situations which

<!-- b001016 | prose | pages [25] -->
only last for 30s.

<!-- b001017 | prose | pages [25] -->
The four pictures in Fig.11 shows the change of temperature field after the hot water is added. Because the water flows in specific velocity, it influences mainly the area in front of it. However, the area beside it is hardly affected and remains the primary temperature. As more hot water is added, the convective surface becomes larger and moves towards the exit. We can also find there is

<!-- b001018 | prose | pages [25] -->
an obvious interface between the added hot water and the initial bath water. That indicates the difference of temperature of added water and bath water is supposed to be small.

<!-- b001019 | prose | pages [25] -->
In the standby process, the bath water is put in a space, cooling freely. Recalling on our calculating results before, it takes about 1.64h for the temperature of the whole bath water to decrease by 1℃. Since it is impossible for out computer to simulate the change over such long time, we shrink the size of bathtub. The boundary conditions remain unchanged. Shrinking the size to 1/100, we get the temperature field as following.

<!-- b001020 | furniture | pages [25] -->


<!-- b001021 | furniture | pages [25] -->


<!-- b001022 | furniture | pages [25] -->


<!-- b001023 | furniture | pages [25] -->


<!-- b001024 | furniture | pages [25] -->


<!-- b001025 | furniture | pages [25] -->


<!-- b001026 | furniture | pages [26] -->
Team #44398                                                    Page 26 of 51

<!-- b001027 | furniture | pages [26] -->


<!-- b001028 | furniture | pages [26] -->


<!-- b001029 | furniture | pages [26] -->


<!-- b001030 | furniture | pages [26] -->


<!-- b001031 | furniture | pages [26] -->


<!-- b001032 | furniture | pages [26] -->


<!-- b001033 | furniture | pages [26] -->


<!-- b001034 | furniture | pages [26] -->


<!-- b001035 | furniture | pages [26] -->


<!-- b001036 | furniture | pages [26] -->


<!-- b001037 | furniture | pages [26] -->


<!-- b001038 | furniture | pages [26] -->


<!-- b001039 | furniture | pages [26] -->


<!-- b001040 | caption | pages [26] -->
Fig.12  The residual curve of simulation

<!-- b001041 | furniture | pages [26] -->


<!-- b001042 | furniture | pages [26] -->


<!-- b001043 | furniture | pages [26] -->


<!-- b001044 | furniture | pages [26] -->


<!-- b001045 | furniture | pages [26] -->


<!-- b001046 | furniture | pages [26] -->


<!-- b001047 | furniture | pages [26] -->


<!-- b001048 | furniture | pages [26] -->


<!-- b001049 | furniture | pages [26] -->


<!-- b001050 | prose | pages [26] -->
(a) t=3s

<!-- b001051 | furniture | pages [26] -->


<!-- b001052 | furniture | pages [26] -->


<!-- b001053 | furniture | pages [26] -->


<!-- b001054 | furniture | pages [26] -->


<!-- b001055 | furniture | pages [26] -->


<!-- b001056 | furniture | pages [26] -->


<!-- b001057 | furniture | pages [26] -->


<!-- b001058 | furniture | pages [26] -->


<!-- b001059 | furniture | pages [26] -->


<!-- b001060 | prose | pages [26] -->
(b) t=15s

<!-- b001061 | caption | pages [26] -->
Fig.13   The temperature field

<!-- b001062 | prose | pages [26] -->
Compared to initial bathtub, although the size changes, the heat transfer remains the same. As is shown in the picture (a), when the time is short, the change of temperature of middle areas is small. That is because the main

<!-- b001063 | furniture | pages [26] -->


<!-- b001064 | furniture | pages [27] -->
Team #44398                                                    Page 27 of 51

<!-- b001065 | prose | pages [27] -->
convection happens in boundary areas. As time goes by, the cooler areas spread towards the middle area, as is presented in picture (b). So that the temperature of other areas besides the middle begins to change. However, the change is

<!-- b001066 | prose | pages [27] -->
small, most of which is less than 2℃. The lowest temperature occurs in four corners, being 40℃ approximately. After the mean temperature is lower than the expected value, the bathtub user needs to add hot water into the bathtub to reheat the water. This simulating result corresponds to the calculating result we derived before.

<!-- b001067 | heading | pages [27] -->
6.4  Conclusion

<!-- b001068 | prose | pages [27] -->
According to calculation and simulation, we basically determine the time of an iteration. The heating process lasts for 3 min while the mass flow is 0.61kg/s. the standby process lasts for 1.64h while the mean temperature decreases by 1℃. By simulating the two situations, we proof the validity of our model and explain why it is so slow for the temperature of bath water to decrease.

<!-- b001069 | heading | pages [27] -->
7  Correction and Contrast of Sub-Models

<!-- b001070 | prose | pages [27] -->
After establishing two basic sub-models, we have to correct them in consideration of evaporation heat transfer. Then we define two evaluation criteria to compare the two sub-models in order to determine the optimal bath strategy.

<!-- b001071 | heading | pages [27] -->
7.1  Correction with Evaporation Heat Transfer

<!-- b001072 | prose | pages [27] -->
Someone may confuse about the above results: why the mass flow in the first sub-model is so small? Why the standby time is so long? Actually, the above two sub-models are based on ideal conditions without consideration of the change of boundary conditions, the motions made by the person in bathtub and the evaporation of bath water, etc. The influence of personal motions will be discussed later. Here we introducing the evaporation of bath water to correct sub-models.

<!-- b001073 | heading | pages [27] -->
7.1.1  Correction Principle

<!-- b001074 | prose | pages [27] -->
According to Gi-Beum Kim’s studies, the heat transfer capacity is relative not only with boundary mixed heat transfer, but also with evaporation heat transfer. More importantly, the major heat loss is found to be due to evaporation [1]. In order to clarify our correction process more clearly, we briefly introduce his achievement and findings.

<!-- b001075 | furniture | pages [27] -->


<!-- b001076 | furniture | pages [28] -->
Team #44398                                                    Page 28 of 51

<!-- b001077 | prose | pages [28] -->
The evaporation heat transfer is related to the temperature of the bath water, the air humidity of the bathroom, the total thermal resistance, material properties and so on. The relationship is given as follows:

<!-- b001078 | prose | pages [28] -->
t

<!-- b001079 | prose | pages [28] -->
 

<!-- b001080 | prose | pages [28] -->


<!-- b001081 | prose | pages [28] -->
EA L

<!-- b001082 | furniture | pages [28] -->


<!-- b001083 | prose | pages [28] -->
f t

<!-- b001084 | prose | pages [28] -->
0

<!-- b001085 | prose | pages [28] -->


<!-- b001086 | prose | pages [28] -->
Mc

<!-- b001087 | prose | pages [28] -->
p

<!-- b001088 | prose | pages [28] -->
dt

<!-- b001089 | prose | pages [28] -->
（39）

<!-- b001090 | furniture | pages [28] -->


<!-- b001091 | prose | pages [28] -->
  

<!-- b001092 | prose | pages [28] -->


<!-- b001093 | prose | pages [28] -->
t t t kA

<!-- b001094 | prose | pages [28] -->


<!-- b001095 | prose | pages [28] -->
0

<!-- b001096 | prose | pages [28] -->
where k is the thermal resistance. A is the area of heat transfer. L is the latent heat of evaporation.  is the thickness of materials.

<!-- b001097 | prose | pages [28] -->
fA is the area of free surface. E is the evaporation capacity.

<!-- b001098 | prose | pages [28] -->
The experimental formula that Gi-Beum Kim gives is

<!-- b001099 | prose | pages [28] -->
    E 0.37 0.0041 v 0.0041

<!-- b001100 | furniture | pages [28] -->


<!-- b001101 | prose | pages [28] -->
   0.88 0.88    t t /22.009 e e 0.004 1 （40）

<!-- b001102 | furniture | pages [28] -->


<!-- b001103 | prose | pages [28] -->
where v is the mean temperature of air and  is the air humidity. The experimental formula for the latent heat of evaporation L is

<!-- b001104 | prose | pages [28] -->


<!-- b001105 | prose | pages [28] -->
  L t

<!-- b001106 | prose | pages [28] -->


<!-- b001107 | prose | pages [28] -->
t 0.174 273.15 3.484

<!-- b001108 | furniture | pages [28] -->


<!-- b001109 | prose | pages [28] -->
（41）

<!-- b001110 | furniture | pages [28] -->


<!-- b001111 | prose | pages [28] -->
 and the convection We let the evaporation heat transfer capacity to be s . Then the total heat loss is heat transfer capacity to be q

<!-- b001112 | prose | pages [28] -->
  =

<!-- b001113 | furniture | pages [28] -->


<!-- b001114 | prose | pages [28] -->
t （42） s s q

<!-- b001115 | prose | pages [28] -->
Plugging the above formulas into sub-models, we obtain the precise results after being corrected.

<!-- b001116 | heading | pages [28] -->
7.1.2  Correction Results

<!-- b001117 | prose | pages [28] -->
Considering the model established by Gi-Beum Kim is similar with ours,

<!-- b001118 | furniture | pages [28] -->


<!-- b001119 | prose | pages [28] -->
so we can refer to his results to correct our sub-models. In his experiment, the bathtub has a capacity of 250L, which is close to the capacity of our bathtub. When the air humidity remains stable, he finds the change of mean temperature over time as follows [1]:

<!-- b001120 | furniture | pages [28] -->


<!-- b001121 | furniture | pages [28] -->


<!-- b001122 | furniture | pages [28] -->


<!-- b001123 | furniture | pages [28] -->


<!-- b001124 | furniture | pages [28] -->


<!-- b001125 | furniture | pages [28] -->


<!-- b001126 | furniture | pages [28] -->


<!-- b001127 | furniture | pages [28] -->


<!-- b001128 | furniture | pages [28] -->


<!-- b001129 | furniture | pages [28] -->


<!-- b001130 | furniture | pages [28] -->


<!-- b001131 | furniture | pages [28] -->


<!-- b001132 | furniture | pages [29] -->
Team #44398                                                    Page 29 of 51

<!-- b001133 | furniture | pages [29] -->


<!-- b001134 | furniture | pages [29] -->


<!-- b001135 | furniture | pages [29] -->


<!-- b001136 | furniture | pages [29] -->


<!-- b001137 | furniture | pages [29] -->


<!-- b001138 | furniture | pages [29] -->


<!-- b001139 | furniture | pages [29] -->


<!-- b001140 | furniture | pages [29] -->


<!-- b001141 | furniture | pages [29] -->


<!-- b001142 | furniture | pages [29] -->


<!-- b001143 | furniture | pages [29] -->


<!-- b001144 | furniture | pages [29] -->


<!-- b001145 | furniture | pages [29] -->


<!-- b001146 | furniture | pages [29] -->


<!-- b001147 | caption | pages [29] -->
Fig.14  Mean temperature change under different air humidity

<!-- b001148 | furniture | pages [29] -->


<!-- b001149 | prose | pages [29] -->
As is vividly shown in Fig.14, the air humidity affects the mean temperature of bath water heavily. The more air humidity is, the smaller evaporation capacity will be, so that the main heat transfer comes from

<!-- b001150 | prose | pages [29] -->
boundary convection heat transfer.

<!-- b001151 | prose | pages [29] -->
Commonly, the air humidity is high in bathroom but the air temperature is low. According to Fig.14 , we assume it takes 0.75 h (45 min ) for the temperature of bath water to decrease by 1℃.

<!-- b001152 | prose | pages [29] -->
Since we have obtained the convection capacity in before calculation, we can compute the evaporation capacity based on energy conservation. Then the total heat transfer capacity can be derived and the correction is to be conduct. The corrected results in listed in the following table.

<!-- b001153 | caption | pages [29] -->
Table 6  The corrected results

<!-- b001154 | prose | pages [29] -->
Parameters

<!-- b001155 | prose | pages [29] -->
 s

<!-- b001156 | prose | pages [29] -->
 q

<!-- b001157 | prose | pages [29] -->
 t

<!-- b001158 | prose | pages [29] -->
q

<!-- b001159 | furniture | pages [29] -->


<!-- b001160 | prose | pages [29] -->
m 1

<!-- b001161 | prose | pages [29] -->
q

<!-- b001162 | furniture | pages [29] -->


<!-- b001163 | prose | pages [29] -->
m 2

<!-- b001164 | prose | pages [29] -->
1T

<!-- b001165 | prose | pages [29] -->
T 2

<!-- b001166 | prose | pages [29] -->
T

<!-- b001167 | furniture | pages [29] -->


<!-- b001168 | prose | pages [29] -->
Value Unit

<!-- b001169 | prose | pages [29] -->
261.24 W

<!-- b001170 | prose | pages [29] -->
232.47 W

<!-- b001171 | prose | pages [29] -->
522.71 W

<!-- b001172 | prose | pages [29] -->
0.03 kg/s

<!-- b001173 | prose | pages [29] -->
kg/s 0.63

<!-- b001174 | prose | pages [29] -->
3 min

<!-- b001175 | prose | pages [29] -->
45 min

<!-- b001176 | prose | pages [29] -->
48 min

<!-- b001177 | furniture | pages [30] -->
Team #44398                                                    Page 30 of 51

<!-- b001178 | prose | pages [30] -->
Let us analyze the corrected results. The mean temperature in the first sub- model mainly depends on convective heat transfer capacity because it is in steady state. As for the second sub-model, the convection heat transfer hardly

<!-- b001179 | prose | pages [30] -->
affects the heating process because the specific heat is large. The standby process is similar with the first sub-model, so it is affected by evaporation heat transfer.

<!-- b001180 | heading | pages [30] -->
7.2  Contrast of Two Sub-Models

<!-- b001181 | prose | pages [30] -->
Firstly we define two evaluation criteria. Then we contrast the two sub- models via these two criteria. Thus we can derive the best strategy for the person in the bathtub to adopt.

<!-- b001182 | heading | pages [30] -->
7.2.1  Evaluation Criteria

<!-- b001183 | prose | pages [30] -->
We aim at three goals: keeping the temperature as even as possible, making it close to the initial temperature and decreasing the water consumption. Considering that, we define two criteria to evaluate the sub-models:

<!-- b001184 | prose | pages [30] -->
 The average temperature of the water in bathtub. It is difficult to keep

<!-- b001185 | prose | pages [30] -->
the temperature strictly even throughout the bathtub because

<!-- b001186 | prose | pages [30] -->
convective heat transfer is an unsteady process. However, the difference in temperature of diverse area is rather small so we can use the average temperature to substitute the temperature of whole bathtub. With the aid of Gi-Beum Kim’s study, the optimal temperature ranges from 41 to 45℃[1].

<!-- b001187 | prose | pages [30] -->
 Water consumption during a bath. According to data from the

<!-- b001188 | prose | pages [30] -->
internet, the water consumption of bathing in a bathtub is four times as many as bathing with a shower [7]. So it is necessary for the bathtub users to decrease water consumption, not only for lower cost of bath but also for the responsibility to the environment.

<!-- b001189 | heading | pages [30] -->
7.2.2  Determination of Water Consumption

<!-- b001190 | prose | pages [30] -->
In the before discussion, we have derived the mass flow in the two sub- models. Giving the bath time, it is easy to compute the total water consumption. Considering the bathtub is filled with same water capacity, the difference of

<!-- b001191 | prose | pages [30] -->
water consumption is added hot water. So we only have to calculate the amount of added water in order to compare the sub-models.

<!-- b001192 | prose | pages [30] -->
bT . Since the hot water is added consistently, We let the bath time to be the mass flow is a constant over time. So the total amount of added water is

<!-- b001193 | furniture | pages [30] -->


<!-- b001194 | furniture | pages [31] -->
Team #44398                                                    Page 31 of 51

<!-- b001195 | prose | pages [31] -->
 m

<!-- b001196 | furniture | pages [31] -->


<!-- b001197 | prose | pages [31] -->
1 T q （43）

<!-- b001198 | furniture | pages [31] -->


<!-- b001199 | prose | pages [31] -->
b b m 1

<!-- b001200 | prose | pages [31] -->
As for the second sub-model, the hot water is only added during the

<!-- b001201 | prose | pages [31] -->
heating process. So the mass flow in heating process is constant while that in standby process is zero. Then we have the total amount of added water in second sub-model

<!-- b001202 | prose | pages [31] -->
 T 

<!-- b001203 | prose | pages [31] -->
b

<!-- b001204 | prose | pages [31] -->
m

<!-- b001205 | furniture | pages [31] -->


<!-- b001206 | prose | pages [31] -->


<!-- b001207 | prose | pages [31] -->
2

<!-- b001208 | prose | pages [31] -->
T    

<!-- b001209 | prose | pages [31] -->
1

<!-- b001210 | prose | pages [31] -->
T q

<!-- b001211 | prose | pages [31] -->
（44）

<!-- b001212 | furniture | pages [31] -->


<!-- b001213 | prose | pages [31] -->


<!-- b001214 | prose | pages [31] -->
1

<!-- b001215 | prose | pages [31] -->
m

<!-- b001216 | prose | pages [31] -->
2

<!-- b001217 | prose | pages [31] -->


<!-- b001218 | prose | pages [31] -->
bT may not where we use Gauss integral function. Because the bath time be any multiple of the iteration time T , we have to round the figure. No matter what period adding hot water reaches, we assume it as a complete iteration so that the actual iteration times need to be plus one.

<!-- b001219 | prose | pages [31] -->
bT  48min To simplify our calculation, we set the bath time to be , which is very an iteration time. Thus we find the amount of added water consumption

<!-- b001220 | prose | pages [31] -->
m  86.4 kg in the first sub-model to be 1 m  113.4 kg be . 2

<!-- b001221 | heading | pages [31] -->
7.2.3  Conclusion

<!-- b001222 | prose | pages [31] -->
, while that in the second sub-model to

<!-- b001223 | prose | pages [31] -->
In terms of the mean temperature of bath water, the temperature of the first sub-model is 43℃ while that of the second sub-model ranges from 42 to 43℃. According to common sense, a person can hardly feel 1℃change of temperature. So both strategies of adding water are optimal for the person in a bathtub.

<!-- b001224 | prose | pages [31] -->
As the water consumption of the first sub-model is 84.6 kg, while that of the second sub-model is 113.4 kg. Considering our goal to decrease water consumption, it is obviously wise to choose adding hot water continually instead of adding water discontinuously.

<!-- b001225 | prose | pages [31] -->
In conclusion, we recommend the person in the bathtub to add hot water continually with mass flow being 0.03 kg/s. This strategy can not only ensure comfortable bath experience but also avoid wasting too much water.

<!-- b001226 | heading | pages [31] -->
8  Model Analysis and Sensitivity Analysis

<!-- b001227 | prose | pages [31] -->
The results of the model we establish before correspond with literature to

<!-- b001228 | prose | pages [31] -->
huge extent. However, the model is based on an ideal situation that there is no person in bathtub. Still, the bathtub in our model is simplified as a cube.

<!-- b001229 | prose | pages [31] -->
In reality, things are quite different. The bathtub can be designed into various shapes and volumes and there is undoubtedly one person or more in

<!-- b001230 | furniture | pages [31] -->


<!-- b001231 | furniture | pages [32] -->
Team #44398                                                    Page 32 of 51

<!-- b001232 | prose | pages [32] -->
the bathtub. The person in bathtub may have various shapes, volume and temperature. He / She is likely to make mangy motions during bath time. In addition, people tend to use a bubble bath additive while initially filling the

<!-- b001233 | prose | pages [32] -->
bathtub to assist in cleansing, which may affect our model’s results as well.

<!-- b001234 | prose | pages [32] -->
So here we will conduct sensitivity analysis to determine the extent to which our model depends upon those influencing factors

<!-- b001235 | heading | pages [32] -->
8.1  The Influence of Different Bathtubs

<!-- b001236 | prose | pages [32] -->
Definitely, the difference in shape and volume of the tub affects the convection heat transfer. Examining the relationship between them can help people choose optimal bathtubs.

<!-- b001237 | heading | pages [32] -->
8.1.1  Different Volumes of Bathtubs

<!-- b001238 | prose | pages [32] -->
In reality, a cup of water will be cooled down rapidly. However, it takes quite long time for a bucket of water to become cool. That is because their volume is different and the specific heat of water is very large. So that the decrease of temperature is not obvious if the volume of water is huge. That also explains why it takes 45 min for 320 L water to be cooled by 1℃.

<!-- b001239 | prose | pages [32] -->
In order to examine the influence of volume, we analyze our sub-models

<!-- b001240 | prose | pages [32] -->
by conducting sensitivity Analysis to them.

<!-- b001241 | prose | pages [32] -->
  5% 8% We assume the initial volume to be 280 L and change it by   12% 15% , , . With the aid of sub-models we established before, the and variation of some parameters turns out to be as follows

<!-- b001242 | caption | pages [32] -->
Table7  Variation of some parameters

<!-- b001243 | prose | pages [32] -->
2A V 1A  q q T

<!-- b001244 | furniture | pages [32] -->


<!-- b001245 | furniture | pages [32] -->


<!-- b001246 | prose | pages [32] -->
m 1 m 2 2 2 q

<!-- b001247 | prose | pages [32] -->
-12.67% -15.00% -5.06% -9.31% -2.67% -14.14% -5.80%

<!-- b001248 | prose | pages [32] -->
-10.09% -12.00% -4.04% -7.43% -2.13% -11.31% -4.63%

<!-- b001249 | prose | pages [32] -->
-6.68% -8.00% -2.68% -4.94% -1.41% -7.54% -3.07%

<!-- b001250 | prose | pages [32] -->
-4.16% -5.00% -1.67% -3.08% -0.88% -4.71% -1.92%

<!-- b001251 | prose | pages [32] -->
-1.65% -2.00% -0.67% -1.23% -0.35% -1.89% -0.76%

<!-- b001252 | prose | pages [32] -->
0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00%

<!-- b001253 | prose | pages [32] -->
1.64% 2.00% 0.67% 1.22% 0.35% 1.89% 0.76%

<!-- b001254 | prose | pages [32] -->
4.09% 5.00% 1.66% 3.05% 0.87% 4.71% 1.90%

<!-- b001255 | prose | pages [32] -->
6.51% 8.00% 2.65% 4.87% 1.40% 7.54% 3.03%

<!-- b001256 | prose | pages [32] -->
9.71% 12.00% 3.96% 7.28% 2.09% 11.31% 4.54%

<!-- b001257 | prose | pages [32] -->
12.08% 15.00% 4.94% 9.08%

<!-- b001258 | furniture | pages [32] -->


<!-- b001259 | prose | pages [32] -->
2.60% 14.14% 5.66%

<!-- b001260 | furniture | pages [33] -->
Team #44398                                                    Page 33 of 51

<!-- b001261 | prose | pages [33] -->
To show the relationship of different parameters and volume, we put the data in the following pictures.

<!-- b001262 | furniture | pages [33] -->


<!-- b001263 | furniture | pages [33] -->


<!-- b001264 | furniture | pages [33] -->


<!-- b001265 | furniture | pages [33] -->


<!-- b001266 | furniture | pages [33] -->


<!-- b001267 | furniture | pages [33] -->


<!-- b001268 | furniture | pages [33] -->


<!-- b001269 | furniture | pages [33] -->


<!-- b001270 | furniture | pages [33] -->


<!-- b001271 | caption | pages [33] -->
Fig.15  The change of

<!-- b001272 | caption | pages [33] -->
Fig.16  The change of

<!-- b001273 | furniture | pages [33] -->


<!-- b001274 | furniture | pages [33] -->


<!-- b001275 | furniture | pages [33] -->


<!-- b001276 | furniture | pages [33] -->


<!-- b001277 | furniture | pages [33] -->


<!-- b001278 | furniture | pages [33] -->


<!-- b001279 | prose | pages [33] -->
 over volume T and 2 q

<!-- b001280 | furniture | pages [33] -->


<!-- b001281 | furniture | pages [33] -->


<!-- b001282 | furniture | pages [33] -->


<!-- b001283 | furniture | pages [33] -->


<!-- b001284 | furniture | pages [33] -->


<!-- b001285 | furniture | pages [33] -->


<!-- b001286 | furniture | pages [33] -->


<!-- b001287 | furniture | pages [33] -->


<!-- b001288 | furniture | pages [33] -->


<!-- b001289 | furniture | pages [33] -->


<!-- b001290 | furniture | pages [33] -->


<!-- b001291 | furniture | pages [33] -->


<!-- b001292 | furniture | pages [33] -->


<!-- b001293 | furniture | pages [33] -->


<!-- b001294 | furniture | pages [33] -->


<!-- b001295 | furniture | pages [33] -->


<!-- b001296 | furniture | pages [33] -->


<!-- b001297 | furniture | pages [33] -->


<!-- b001298 | furniture | pages [33] -->


<!-- b001299 | furniture | pages [33] -->


<!-- b001300 | prose | pages [33] -->
q q q and over volume m m 1 1 m 2

<!-- b001301 | prose | pages [33] -->
From the above figures, we can find when the bathtub volume is small, the volume of other parameters is small too. For example, as the volume decreases,

<!-- b001302 | prose | pages [33] -->
the heat loss becomes less so that the mass flow of added water decreases correspondingly in the two sub-models.

<!-- b001303 | prose | pages [33] -->
In conclusion, smaller bathtub is a better choice for people in terms of saving more water resource. This can not only decrease the initial water

<!-- b001304 | furniture | pages [33] -->


<!-- b001305 | furniture | pages [34] -->
Team #44398                                                    Page 34 of 51

<!-- b001306 | prose | pages [34] -->
consumption to fill the bathtub but also avoid adding too much hot water afterwards. Of course, it is unwise for taller or fatter people to choose a small bathtub.

<!-- b001307 | heading | pages [34] -->
8.1.2  Different Shapes of Bathtubs

<!-- b001308 | prose | pages [34] -->
When the volume is constant, different shapes of bathtub mainly affect surface area of bath water, influencing heat transfer consequently. So we convert the change of shapes into that of surface area.

<!-- b001309 | prose | pages [34] -->
Usually, there are bathtubs in shapes of round, ellipse, rectangular, heart- shaped, rounded rectangle and so on [18]. We let the perimeter of the section of the bathtub to be C . The area of top surface and other surfaces is A . 1A and 2 The parameters of different shapes of bathtubs are listed as follows.

<!-- b001310 | caption | pages [34] -->
Table 8  The parameters of different shapes

<!-- b001311 | prose | pages [34] -->
Shapes Sketches

<!-- b001312 | furniture | pages [34] -->


<!-- b001313 | prose | pages [34] -->
Round

<!-- b001314 | furniture | pages [34] -->


<!-- b001315 | prose | pages [34] -->
Rectangle

<!-- b001316 | furniture | pages [34] -->


<!-- b001317 | prose | pages [34] -->
Square

<!-- b001318 | furniture | pages [34] -->


<!-- b001319 | prose | pages [34] -->
Rounded

<!-- b001320 | prose | pages [34] -->
rectangle

<!-- b001321 | prose | pages [34] -->
A 1A 2

<!-- b001322 | prose | pages [34] -->
  2 V A 

<!-- b001323 | furniture | pages [34] -->


<!-- b001324 | prose | pages [34] -->
2r

<!-- b001325 | furniture | pages [34] -->


<!-- b001326 | prose | pages [34] -->
1 A 1

<!-- b001327 | prose | pages [34] -->
2V a

<!-- b001328 | prose | pages [34] -->
 

<!-- b001329 | prose | pages [34] -->
  b A

<!-- b001330 | furniture | pages [34] -->


<!-- b001331 | prose | pages [34] -->
ab 1

<!-- b001332 | prose | pages [34] -->
A

<!-- b001333 | prose | pages [34] -->
1

<!-- b001334 | prose | pages [34] -->
4V

<!-- b001335 | prose | pages [34] -->


<!-- b001336 | prose | pages [34] -->
A

<!-- b001337 | furniture | pages [34] -->


<!-- b001338 | prose | pages [34] -->
2 a 1

<!-- b001339 | prose | pages [34] -->
A

<!-- b001340 | prose | pages [34] -->
1

<!-- b001341 | prose | pages [34] -->
V C  A

<!-- b001342 | furniture | pages [34] -->


<!-- b001343 | prose | pages [34] -->
  2r ab

<!-- b001344 | furniture | pages [34] -->


<!-- b001345 | prose | pages [34] -->
1

<!-- b001346 | prose | pages [34] -->
A

<!-- b001347 | prose | pages [34] -->
1

<!-- b001348 | prose | pages [34] -->
Recalling on the average inequality, we have

<!-- b001349 | prose | pages [34] -->
  2 A 4 A

<!-- b001350 | furniture | pages [34] -->


<!-- b001351 | prose | pages [34] -->
1

<!-- b001352 | furniture | pages [34] -->


<!-- b001353 | prose | pages [34] -->
  2 A    2 a 1

<!-- b001354 | prose | pages [34] -->
（45）

<!-- b001355 | furniture | pages [34] -->


<!-- b001356 | prose | pages [34] -->
  1 1 a  

<!-- b001357 | furniture | pages [35] -->
Team #44398                                                    Page 35 of 51

<!-- b001358 | prose | pages [35] -->
So the perimeter of rectangle is the largest while that of square being smaller and that of circle being the smallest. We assume the volume to be 280L A  2 1.05m and the area of the top surface 1

<!-- b001359 | prose | pages [35] -->
shown in the following table.

<!-- b001360 | prose | pages [35] -->
. The value of other parameters are

<!-- b001361 | caption | pages [35] -->
Table 9  The value of other parameters

<!-- b001362 | prose | pages [35] -->
Shapes Size/m

<!-- b001363 | prose | pages [35] -->
r  0.578 Round

<!-- b001364 | furniture | pages [35] -->


<!-- b001365 | prose | pages [35] -->
  a 1.5, b 0.7 Rectangle I

<!-- b001366 | furniture | pages [35] -->


<!-- b001367 | prose | pages [35] -->
1 1

<!-- b001368 | prose | pages [35] -->
  a 1.7, b 0.62 Rectangle II

<!-- b001369 | furniture | pages [35] -->


<!-- b001370 | prose | pages [35] -->
2 2

<!-- b001371 | prose | pages [35] -->
a  1.025 Square

<!-- b001372 | furniture | pages [35] -->


<!-- b001373 | prose | pages [35] -->
   a 1.2, b 0.7, r 0.05 Rounded rectangle

<!-- b001374 | prose | pages [35] -->
 A q q 2T

<!-- b001375 | furniture | pages [35] -->


<!-- b001376 | furniture | pages [35] -->


<!-- b001377 | prose | pages [35] -->
m1 m2 2 q

<!-- b001378 | prose | pages [35] -->
2.02 0.0293 0.5565 227.7 39.76

<!-- b001379 | prose | pages [35] -->
2.22 0.0295 0.5568 231.5 39.45

<!-- b001380 | prose | pages [35] -->
2.29 0.0296 0.5569 232.8 39.34

<!-- b001381 | prose | pages [35] -->
2.14 0.0294 0.5567 230.0 39.57

<!-- b001382 | furniture | pages [35] -->


<!-- b001383 | furniture | pages [35] -->


<!-- b001384 | prose | pages [35] -->
2.15 0.0294 0.5567 230.2 39.56

<!-- b001385 | prose | pages [35] -->
As the rounded rectangle is the most commonly shape of bathtubs, we choose it as the basic bathtub. Comparing it with other shapes, we derive the variation as follows.

<!-- b001386 | caption | pages [35] -->
Table 10  The variation compared to other shapes

<!-- b001387 | prose | pages [35] -->
Rounded rectangle Shapes Rectangle I

<!-- b001388 | prose | pages [35] -->
A 0.00% 3.26% 2

<!-- b001389 | prose | pages [35] -->
 0.00% 0.58% q

<!-- b001390 | prose | pages [35] -->
q

<!-- b001391 | furniture | pages [35] -->


<!-- b001392 | prose | pages [35] -->
0.00% 0.34% m1

<!-- b001393 | prose | pages [35] -->
q

<!-- b001394 | furniture | pages [35] -->


<!-- b001395 | prose | pages [35] -->
0.00% 0.02% m2

<!-- b001396 | prose | pages [35] -->
2T 0.00% -0.27%

<!-- b001397 | furniture | pages [35] -->


<!-- b001398 | furniture | pages [35] -->


<!-- b001399 | furniture | pages [35] -->


<!-- b001400 | furniture | pages [35] -->


<!-- b001401 | furniture | pages [35] -->


<!-- b001402 | furniture | pages [35] -->


<!-- b001403 | furniture | pages [35] -->


<!-- b001404 | prose | pages [35] -->
and

<!-- b001405 | caption | pages [35] -->
Fig.17  The value of

<!-- b001406 | prose | pages [35] -->
q

<!-- b001407 | furniture | pages [35] -->


<!-- b001408 | prose | pages [35] -->
Rectangle II Square Round

<!-- b001409 | prose | pages [35] -->
6.39% -0.47% -6.05%

<!-- b001410 | prose | pages [35] -->
1.14% -0.08% -1.08%

<!-- b001411 | prose | pages [35] -->
0.68% 0.00% -0.34%

<!-- b001412 | prose | pages [35] -->
0.04% 0.00% -0.04%

<!-- b001413 | prose | pages [35] -->
-0.53% 0.04% 0.51%

<!-- b001414 | furniture | pages [35] -->


<!-- b001415 | furniture | pages [35] -->


<!-- b001416 | prose | pages [35] -->
2T of tubs in different shapes

<!-- b001417 | furniture | pages [36] -->
Team #44398                                                    Page 36 of 51

<!-- b001418 | prose | pages [36] -->
1A and From the above data, we conclude when the area of top surface

<!-- b001419 | furniture | pages [36] -->


<!-- b001420 | prose | pages [36] -->
volume V are given, the area of side surface A in round bathtub is the smallest 2

<!-- b001421 | prose | pages [36] -->
among different shapes. So the heat loss of bathtubs in round shape is the smallest.

<!-- b001422 | prose | pages [36] -->
On the contrary, the area of side surface and heat loss of rectangle bathtubs are a b / the largest. As for rectangle bathtubs, if the ratio of length to width becomes lager, the area of side surface will consequently increase, leading to the rise of heat loss. So that square bathtub is better than rectangle one in consideration of heat loss.

<!-- b001423 | prose | pages [36] -->
In conclusion, with regard to heat transfer, the round bathtub is best to

<!-- b001424 | furniture | pages [36] -->


<!-- b001425 | prose | pages [36] -->
choose while the square and rounded rectangle bathtub is less recommended. The rectangle bathtub is the least to choose.

<!-- b001426 | prose | pages [36] -->
In reality, however, the rounded rectangle bathtubs are more common

<!-- b001427 | furniture | pages [36] -->


<!-- b001428 | prose | pages [36] -->
instead of round bathtubs. That is because of the shape of human body and space of the bathroom. A round bathtub will cover more area in a bathroom.

<!-- b001429 | heading | pages [36] -->
8.2  The Influence of Person in Bathtub

<!-- b001430 | prose | pages [36] -->
To some extent, our model may be affected by the difference of people in a bathtub and motions they make. So it is necessary for us to investigate their influence further.

<!-- b001431 | prose | pages [36] -->
In consideration of our goal to avoid wasting too much water, we assume the bathtub is not completely filled with hot water before the person comes into it.

<!-- b001432 | heading | pages [36] -->
8.2.1  When the Person Remains Static in a Bathtub

<!-- b001433 | prose | pages [36] -->
Recalling on our biologic knowledge, human beings are warm-blooded animals whose average temperature remains around 37℃. The change of 1℃ of average temperature means lot to a person. For example, when the temperature rises to 38℃, the person is diagnosed to have a fever. As for skin of human beings, it is made up of three layers: epidermal, dermis and hypodermis. The epidermal layer contacts directly to surroundings, so its temperature is close to the temperature of the surroundings. However, the temperature inside skins commonly remain around 37℃.

<!-- b001434 | prose | pages [36] -->
To simplify the problem, we firstly assume the person in the bathtub remains stable without any motions. Under this circumstance, the skin transfer

<!-- b001435 | prose | pages [36] -->
heat with bath water. According to convection heat transfer formula, we have

<!-- b001436 | prose | pages [36] -->


<!-- b001437 | prose | pages [36] -->
=

<!-- b001438 | furniture | pages [36] -->


<!-- b001439 | prose | pages [36] -->
p

<!-- b001440 | prose | pages [36] -->
1

<!-- b001441 | prose | pages [36] -->
A

<!-- b001442 | prose | pages [36] -->
3

<!-- b001443 | furniture | pages [36] -->


<!-- b001444 | prose | pages [36] -->


<!-- b001445 | prose | pages [36] -->
t t t

<!-- b001446 | prose | pages [36] -->
f f p

<!-- b001447 | prose | pages [36] -->
（46）

<!-- b001448 | furniture | pages [36] -->


<!-- b001449 | prose | pages [36] -->
  

<!-- b001450 | prose | pages [36] -->


<!-- b001451 | prose | pages [36] -->
1

<!-- b001452 | prose | pages [36] -->


<!-- b001453 | prose | pages [36] -->
3

<!-- b001454 | prose | pages [36] -->
  

<!-- b001455 | prose | pages [36] -->
k k h

<!-- b001456 | prose | pages [36] -->
  

<!-- b001457 | prose | pages [36] -->
3 3

<!-- b001458 | furniture | pages [37] -->
Team #44398                                                    Page 37 of 51

<!-- b001459 | prose | pages [37] -->
 is the heat transfer capacity and where p A is the average area of 3  is the thickness of skin. human skin.

<!-- b001460 | prose | pages [37] -->
3 3h is the convection heat transfer pt is the average 3k  is the thermal conductivity of skin. coefficient.

<!-- b001461 | prose | pages [37] -->
temperature of human beings, which is commonly 37℃.

<!-- b001462 | furniture | pages [37] -->


<!-- b001463 | furniture | pages [37] -->


<!-- b001464 | furniture | pages [37] -->


<!-- b001465 | furniture | pages [37] -->


<!-- b001466 | furniture | pages [37] -->


<!-- b001467 | prose | pages [37] -->
pt

<!-- b001468 | furniture | pages [37] -->


<!-- b001469 | furniture | pages [37] -->


<!-- b001470 | furniture | pages [37] -->


<!-- b001471 | furniture | pages [37] -->


<!-- b001472 | furniture | pages [37] -->


<!-- b001473 | furniture | pages [37] -->


<!-- b001474 | furniture | pages [37] -->


<!-- b001475 | furniture | pages [37] -->


<!-- b001476 | furniture | pages [37] -->


<!-- b001477 | prose | pages [37] -->
ft

<!-- b001478 | caption | pages [37] -->
Fig.18  Heat transfer through skin

<!-- b001479 | prose | pages [37] -->
where the orange curve represents the temperature trend.

<!-- b001480 | furniture | pages [37] -->


<!-- b001481 | prose | pages [37] -->
The total heat transfer capacity is

<!-- b001482 | prose | pages [37] -->
  =

<!-- b001483 | furniture | pages [37] -->


<!-- b001484 | prose | pages [37] -->
t s （47） q p

<!-- b001485 | prose | pages [37] -->
Because the person remains static, so the value of is unchanged. As the bathtub is not completely full of hot water, the surface area of bath water will be creased after the person comes into the tub. We let the mass of the person to m , the density of the person to be be 3 m and V after knowing to calculate 3 3  and the volume to be V . It is easy 3 3 . 3 With the aid of formulas we get on the above, we can assume the volume to change and then correct it with surface area. Through this we can get the corrected results.

<!-- b001486 | heading | pages [37] -->
8.2.2  When the Person Moves in a Bathtub

<!-- b001487 | prose | pages [37] -->
Theoretically, the motions made by the person obviously affect heat

<!-- b001488 | prose | pages [37] -->
transfer. When the person moves, the hot water will be stirred. So that the natural convection transfers into forced convection where the convection heat transfer coefficient will rise a lot. Meanwhile, the motion of bath water will increase the surface area of convection, leading to more heat loss. According to

<!-- b001489 | furniture | pages [37] -->


<!-- b001490 | furniture | pages [38] -->
Team #44398                                                    Page 38 of 51

<!-- b001491 | prose | pages [38] -->
heat transfer theory, the influence of motion caused by the person can be determined.

<!-- b001492 | heading | pages [38] -->
8.2.3  Results Analysis and Sensitivity Analysis

<!-- b001493 | prose | pages [38] -->
Professor Anand Mani sums up other scientists’ research outcome in his essay [10]. We choose some values from the data in his essay which are listed as follows.

<!-- b001494 | caption | pages [38] -->
Table 11  The value of some parameters

<!-- b001495 | prose | pages [38] -->
Parameters Range

<!-- b001496 | prose | pages [38] -->
A 1.5~2 [11] 3

<!-- b001497 | prose | pages [38] -->
 2~3 [12] 3

<!-- b001498 | prose | pages [38] -->
pc

<!-- b001499 | prose | pages [38] -->
Value Unit

<!-- b001500 | prose | pages [38] -->
2 m 1.8

<!-- b001501 | prose | pages [38] -->
mm 2.5

<!-- b001502 | prose | pages [38] -->
   J/ kg K 3300,3800,4200,3300 [13-16]

<!-- b001503 | furniture | pages [38] -->


<!-- b001504 | prose | pages [38] -->
3

<!-- b001505 | prose | pages [38] -->
3k

<!-- b001506 | prose | pages [38] -->
3800

<!-- b001507 | furniture | pages [38] -->


<!-- b001508 | prose | pages [38] -->
   W/ m K 0.3,0.21,0.5*,0.543 [17]

<!-- b001509 | prose | pages [38] -->


<!-- b001510 | prose | pages [38] -->
0.3

<!-- b001511 | furniture | pages [38] -->


<!-- b001512 | prose | pages [38] -->
3 kg / m 1040,1050,1000,1100 3 1050

<!-- b001513 | prose | pages [38] -->
* Combined Conductivity for dermal and epidermal layers.

<!-- b001514 | prose | pages [38] -->
The heat transfer coefficient differs a lot in natural convection and forced

<!-- b001515 | prose | pages [38] -->
convection. We list those coefficients as follows.

<!-- b001516 | caption | pages [38] -->
Table 12  The heat transfer coefficients

<!-- b001517 | prose | pages [38] -->
Types Coefficients

<!-- b001518 | prose | pages [38] -->
Coefficient of air

<!-- b001519 | prose | pages [38] -->
Coefficient of water

<!-- b001520 | prose | pages [38] -->
Natural

<!-- b001521 | prose | pages [38] -->
1h

<!-- b001522 | prose | pages [38] -->
convection

<!-- b001523 | prose | pages [38] -->
2h

<!-- b001524 | prose | pages [38] -->
3h

<!-- b001525 | prose | pages [38] -->
Coefficient of air

<!-- b001526 | prose | pages [38] -->
Coefficient of water

<!-- b001527 | prose | pages [38] -->
Forced

<!-- b001528 | prose | pages [38] -->
1h

<!-- b001529 | prose | pages [38] -->
convection

<!-- b001530 | prose | pages [38] -->
2h

<!-- b001531 | prose | pages [38] -->
3h

<!-- b001532 | prose | pages [38] -->
Ranges /Values Unit

<!-- b001533 | prose | pages [38] -->
1~10

<!-- b001534 | prose | pages [38] -->
200~1000

<!-- b001535 | prose | pages [38] -->
   2 W/ m K

<!-- b001536 | prose | pages [38] -->
10

<!-- b001537 | furniture | pages [38] -->


<!-- b001538 | prose | pages [38] -->
300

<!-- b001539 | prose | pages [38] -->
300

<!-- b001540 | prose | pages [38] -->
20~100

<!-- b001541 | furniture | pages [38] -->


<!-- b001542 | furniture | pages [38] -->


<!-- b001543 | prose | pages [38] -->
1000~1500

<!-- b001544 | prose | pages [38] -->
   2 W/ m K

<!-- b001545 | furniture | pages [38] -->


<!-- b001546 | prose | pages [38] -->
60

<!-- b001547 | prose | pages [38] -->
1100

<!-- b001548 | prose | pages [38] -->
1100

<!-- b001549 | prose | pages [38] -->
Putting those data into the sub-models, we derive the following results.

<!-- b001550 | furniture | pages [38] -->


<!-- b001551 | furniture | pages [38] -->


<!-- b001552 | furniture | pages [38] -->


<!-- b001553 | furniture | pages [38] -->


<!-- b001554 | furniture | pages [39] -->
Team #44398                                                    Page 39 of 51

<!-- b001555 | caption | pages [39] -->
Table 13  Results of two sub-models

<!-- b001556 | prose | pages [39] -->
Parameters Static

<!-- b001557 | prose | pages [39] -->
 261.24 s

<!-- b001558 | prose | pages [39] -->
 238.95 q

<!-- b001559 | prose | pages [39] -->
 925.71 p

<!-- b001560 | prose | pages [39] -->
 1425.9 t

<!-- b001561 | prose | pages [39] -->
q

<!-- b001562 | furniture | pages [39] -->


<!-- b001563 | prose | pages [39] -->
0.0854 m 1

<!-- b001564 | prose | pages [39] -->
q

<!-- b001565 | furniture | pages [39] -->


<!-- b001566 | prose | pages [39] -->
0.6314 m 2

<!-- b001567 | prose | pages [39] -->
1T 3

<!-- b001568 | prose | pages [39] -->
T 13.63 2 T 16.63

<!-- b001569 | prose | pages [39] -->
Moving Unit

<!-- b001570 | prose | pages [39] -->
261.24 W

<!-- b001571 | prose | pages [39] -->
1222.4 W

<!-- b001572 | prose | pages [39] -->
1168.5 W

<!-- b001573 | prose | pages [39] -->
2652.1 W

<!-- b001574 | prose | pages [39] -->
0.1588 kg/s

<!-- b001575 | prose | pages [39] -->
kg/s 0.7293

<!-- b001576 | prose | pages [39] -->
3 min

<!-- b001577 | prose | pages [39] -->
7.33 min 10.33 min

<!-- b001578 | prose | pages [39] -->
The sub-models are heavily affected in consideration of person. The mass flow rises because more hot water is needed. The time of iteration becomes shorter, wasting more water resource. When the person moves in the bathtub, his /her motions will lead to forced convection. This will decrease the thermal resistance so that more heat will be lost. In conclusion, the more frequent and fiercer the motions are, the more hot water will be wasted.

<!-- b001579 | prose | pages [39] -->
Then we conduct sensitivity analysis to determine the relationship between the convection heat transfer coefficient and individual motions. Still, the relationship of volume of the person and the convection heat transfer area.

<!-- b001580 | prose | pages [39] -->
At first, we assume the personal mass to be 60 kg and the volume of the     12% 2% 5% 8% bathtub to be 320 L. Changing the mass by  15% , , , and , we can get the variation as follows.

<!-- b001581 | caption | pages [39] -->
Table 14  The variation of parameters over mass

<!-- b001582 | prose | pages [39] -->
 m 3 q

<!-- b001583 | prose | pages [39] -->
-15.00% -0.22% -12.00% -0.17% -8.00% -0.12% -5.00% -0.07% -2.00% -0.03% 0.00% 0.00% 2.00% 0.03% 5.00% 0.07% 8.00% 0.12% 12.00% 0.17% 15.00% 0.22%

<!-- b001584 | furniture | pages [39] -->


<!-- b001585 | prose | pages [39] -->
q q 2T

<!-- b001586 | furniture | pages [39] -->


<!-- b001587 | furniture | pages [39] -->


<!-- b001588 | prose | pages [39] -->
m 1 m 2

<!-- b001589 | prose | pages [39] -->
0.18% -0.18% -0.03% 0.14% -0.14% -0.03% 0.09% -0.09% -0.02% 0.06% -0.06% -0.01% 0.02% -0.02% 0.00% 0.00% 0.00% 0.00% -0.02% 0.02% 0.00% -0.06% 0.06% 0.01% -0.09% 0.09% 0.02% -0.14% 0.14% 0.03% -0.18% 0.18% 0.03%

<!-- b001590 | furniture | pages [40] -->
Team #44398                                                    Page 40 of 51

<!-- b001591 | prose | pages [40] -->
From the above figure, we find the heat transfer capacity and mass flow of added water are both in proportion to the personal mass. That is to say, those two parameters are positively correlated to personal volume while the volume

<!-- b001592 | prose | pages [40] -->
of added water is negatively correlated to personal volume.

<!-- b001593 | prose | pages [40] -->
To show the relationship more vividly, we draw the variations in the following figure.

<!-- b001594 | furniture | pages [40] -->


<!-- b001595 | furniture | pages [40] -->


<!-- b001596 | furniture | pages [40] -->


<!-- b001597 | furniture | pages [40] -->


<!-- b001598 | furniture | pages [40] -->


<!-- b001599 | furniture | pages [40] -->


<!-- b001600 | furniture | pages [40] -->


<!-- b001601 | furniture | pages [40] -->


<!-- b001602 | furniture | pages [40] -->


<!-- b001603 | furniture | pages [40] -->


<!-- b001604 | furniture | pages [40] -->


<!-- b001605 | furniture | pages [40] -->


<!-- b001606 | furniture | pages [40] -->


<!-- b001607 | prose | pages [40] -->
and 2T

<!-- b001608 | caption | pages [40] -->
Fig.19  The variation of

<!-- b001609 | furniture | pages [40] -->


<!-- b001610 | furniture | pages [40] -->


<!-- b001611 | furniture | pages [40] -->


<!-- b001612 | furniture | pages [40] -->


<!-- b001613 | furniture | pages [40] -->


<!-- b001614 | furniture | pages [40] -->


<!-- b001615 | furniture | pages [40] -->


<!-- b001616 | furniture | pages [40] -->


<!-- b001617 | furniture | pages [40] -->


<!-- b001618 | furniture | pages [40] -->


<!-- b001619 | furniture | pages [40] -->


<!-- b001620 | prose | pages [40] -->
q

<!-- b001621 | prose | pages [40] -->
q q

<!-- b001622 | caption | pages [40] -->
Fig.20  The variation of

<!-- b001623 | prose | pages [40] -->
and

<!-- b001624 | furniture | pages [40] -->


<!-- b001625 | prose | pages [40] -->
m 1 m 2

<!-- b001626 | prose | pages [40] -->
We can find the change of those parameters to be relatively small, which indicates the personal volume affects minutely to the model. However, we ignore one factor: the contact area of the person and bath water. In order to conduct sensitivity analyze, we assume the contact area as a constant. Due to

<!-- b001627 | furniture | pages [40] -->


<!-- b001628 | furniture | pages [41] -->
Team #44398                                                    Page 41 of 51

<!-- b001629 | prose | pages [41] -->
the limit of time, we do not investigate its influence further. But we deduce the area is positively correlated to personal volume.

<!-- b001630 | prose | pages [41] -->
In conclusion, if the personal mas and volume are small, the water

<!-- b001631 | prose | pages [41] -->
consumption is small.

<!-- b001632 | prose | pages [41] -->
At last, we analyze the influence of personal motions. Because the motions   2% 5% mainly affect convection heat transfer coefficient, we change it by    8% 12% 15% , , . The results is listed as follows. , and

<!-- b001633 | caption | pages [41] -->
Table 15  The variation of parameters

<!-- b001634 | prose | pages [41] -->
 3h q

<!-- b001635 | prose | pages [41] -->
-15.00% -8.21%

<!-- b001636 | prose | pages [41] -->
-12.00% -6.55%

<!-- b001637 | prose | pages [41] -->
-8.00% -4.35%

<!-- b001638 | prose | pages [41] -->
-5.00% -2.71%

<!-- b001639 | prose | pages [41] -->
-2.00% -1.08%

<!-- b001640 | prose | pages [41] -->
0.00% 0.00%

<!-- b001641 | prose | pages [41] -->
2.00% 1.08%

<!-- b001642 | prose | pages [41] -->
5.00% 2.69%

<!-- b001643 | prose | pages [41] -->
8.00% 4.29%

<!-- b001644 | prose | pages [41] -->
12.00% 6.42%

<!-- b001645 | prose | pages [41] -->
15.00% 8.01%

<!-- b001646 | prose | pages [41] -->
q q 2T

<!-- b001647 | furniture | pages [41] -->


<!-- b001648 | furniture | pages [41] -->


<!-- b001649 | prose | pages [41] -->
m 1 m 2

<!-- b001650 | prose | pages [41] -->
8.00% -7.40% -2.15%

<!-- b001651 | prose | pages [41] -->
6.27% -5.90% -1.71%

<!-- b001652 | prose | pages [41] -->
4.08% -3.92% -1.14%

<!-- b001653 | prose | pages [41] -->
2.51% -2.44% -0.71%

<!-- b001654 | prose | pages [41] -->
0.98% -0.98% -0.28%

<!-- b001655 | prose | pages [41] -->
0.00% 0.00% 0.00%

<!-- b001656 | prose | pages [41] -->
-0.96% 0.97% 0.28%

<!-- b001657 | prose | pages [41] -->
-2.37% 2.42% 0.70%

<!-- b001658 | prose | pages [41] -->
-3.73% 3.87% 1.12%

<!-- b001659 | prose | pages [41] -->
-5.47% 5.79% 1.68%

<!-- b001660 | prose | pages [41] -->
-6.74% 7.22% 2.10%

<!-- b001661 | prose | pages [41] -->
From the above data, we conclude the convection heat transfer coefficient

<!-- b001662 | prose | pages [41] -->
affects the model heavily, especially for the first sub-model. This indicates the stability of the second sub-model is better with less change based on the surroundings. Like before, we list the variation of parameters as follows.

<!-- b001663 | furniture | pages [41] -->


<!-- b001664 | furniture | pages [41] -->


<!-- b001665 | furniture | pages [41] -->


<!-- b001666 | furniture | pages [41] -->


<!-- b001667 | furniture | pages [41] -->


<!-- b001668 | furniture | pages [41] -->


<!-- b001669 | furniture | pages [41] -->


<!-- b001670 | furniture | pages [41] -->


<!-- b001671 | furniture | pages [42] -->
Team #44398                                                    Page 42 of 51

<!-- b001672 | furniture | pages [42] -->


<!-- b001673 | furniture | pages [42] -->


<!-- b001674 | furniture | pages [42] -->


<!-- b001675 | furniture | pages [42] -->


<!-- b001676 | furniture | pages [42] -->


<!-- b001677 | furniture | pages [42] -->


<!-- b001678 | furniture | pages [42] -->


<!-- b001679 | furniture | pages [42] -->


<!-- b001680 | furniture | pages [42] -->


<!-- b001681 | prose | pages [42] -->
and 2T

<!-- b001682 | caption | pages [42] -->
Fig. 21  The variation of

<!-- b001683 | furniture | pages [42] -->


<!-- b001684 | furniture | pages [42] -->


<!-- b001685 | furniture | pages [42] -->


<!-- b001686 | furniture | pages [42] -->


<!-- b001687 | furniture | pages [42] -->


<!-- b001688 | furniture | pages [42] -->


<!-- b001689 | furniture | pages [42] -->


<!-- b001690 | furniture | pages [42] -->


<!-- b001691 | furniture | pages [42] -->


<!-- b001692 | prose | pages [42] -->
q

<!-- b001693 | furniture | pages [42] -->


<!-- b001694 | furniture | pages [42] -->


<!-- b001695 | furniture | pages [42] -->


<!-- b001696 | furniture | pages [42] -->


<!-- b001697 | furniture | pages [42] -->


<!-- b001698 | furniture | pages [42] -->


<!-- b001699 | prose | pages [42] -->
q q

<!-- b001700 | caption | pages [42] -->
Fig.22  The variation of

<!-- b001701 | prose | pages [42] -->
and

<!-- b001702 | furniture | pages [42] -->


<!-- b001703 | prose | pages [42] -->
m 1 m 2

<!-- b001704 | prose | pages [42] -->
We find the mass flow in two sub-models is positively correlated to heat transfer coefficient. The mass flow of added water in the first sub-model is affected minutely by the change of heat transfer coefficient. However, the mass flow in the second sub-model is affected heavily by the change. So we deduce if the person in a bathtub moves more fiercely, he/she will have to add more hot water to reheat the bath water.

<!-- b001705 | heading | pages [42] -->
8.3  The Influence of Bubble Bath Additives

<!-- b001706 | prose | pages [42] -->
According to thermodynamics knowledge, a factor can influence heat transfer in two opposite ways: adding heat transfer or decreasing heat transfer. The bubbles made by a bubble bath additive often float on the bath water.

<!-- b001707 | furniture | pages [42] -->


<!-- b001708 | furniture | pages [43] -->
Team #44398                                                    Page 43 of 51

<!-- b001709 | prose | pages [43] -->
Because the thermal conductivity of bubbles is little, those bubbles can be seen as a thermal insulation layer added between bath water and air. This layer restricts the direct convection of air and bath water so it brings about heat

<!-- b001710 | prose | pages [43] -->
preservation. That indicates we can add bubble bath additives to decrease the amount of added hot water.

<!-- b001711 | prose | pages [43] -->
, the thermal conductivity We let the thickness of layer of bubbles to be 4 4k , the convection heat transfer coefficient of the top surface of bubbles to be h and that of the bottom of bubbles and bath water of bubbles and air to be 4L h . This analysis can be better understood by the following figure. to be 4H

<!-- b001712 | furniture | pages [43] -->


<!-- b001713 | furniture | pages [43] -->


<!-- b001714 | furniture | pages [43] -->


<!-- b001715 | furniture | pages [43] -->


<!-- b001716 | furniture | pages [43] -->


<!-- b001717 | furniture | pages [43] -->


<!-- b001718 | furniture | pages [43] -->


<!-- b001719 | furniture | pages [43] -->


<!-- b001720 | furniture | pages [43] -->


<!-- b001721 | furniture | pages [43] -->


<!-- b001722 | caption | pages [43] -->
Fig.23  The sketch of bubbles affecting heat transfer

<!-- b001723 | prose | pages [43] -->
Here we analyze from two points: on one hand, the bubbles restrict the evaporation heat transfer. We assume the evaporation heat transfer decrease to 10%. On the other hand, adding bubbles adds a heat transfer process between the air and hot water. Recalling on our before analysis, the top surface is the

<!-- b001724 | prose | pages [43] -->
main surface to lose heat. So covering bubbles on the top surface will decrease the heat loss heavily.

<!-- b001725 | prose | pages [43] -->
Based on thermodynamic knowledge, the convection heat transfer capacity is

<!-- b001726 | prose | pages [43] -->


<!-- b001727 | prose | pages [43] -->
=

<!-- b001728 | furniture | pages [43] -->


<!-- b001729 | prose | pages [43] -->
4

<!-- b001730 | prose | pages [43] -->


<!-- b001731 | prose | pages [43] -->
1 1

<!-- b001732 | prose | pages [43] -->


<!-- b001733 | prose | pages [43] -->
A h

<!-- b001734 | prose | pages [43] -->


<!-- b001735 | prose | pages [43] -->
4 4

<!-- b001736 | prose | pages [43] -->
L

<!-- b001737 | prose | pages [43] -->


<!-- b001738 | prose | pages [43] -->
t t t

<!-- b001739 | prose | pages [43] -->


<!-- b001740 | prose | pages [43] -->
f f

<!-- b001741 | prose | pages [43] -->
（48）

<!-- b001742 | furniture | pages [43] -->


<!-- b001743 | prose | pages [43] -->


<!-- b001744 | prose | pages [43] -->


<!-- b001745 | prose | pages [43] -->
1

<!-- b001746 | prose | pages [43] -->
  

<!-- b001747 | prose | pages [43] -->
4

<!-- b001748 | prose | pages [43] -->


<!-- b001749 | prose | pages [43] -->
k h

<!-- b001750 | prose | pages [43] -->


<!-- b001751 | prose | pages [43] -->
4 4

<!-- b001752 | prose | pages [43] -->
H

<!-- b001753 | prose | pages [43] -->
Then we correct the heat transfer capacity and then put corrected results into sub-models. We derive the value of parameters listed in the following table.

<!-- b001754 | furniture | pages [43] -->


<!-- b001755 | furniture | pages [43] -->


<!-- b001756 | furniture | pages [43] -->


<!-- b001757 | furniture | pages [43] -->


<!-- b001758 | furniture | pages [43] -->


<!-- b001759 | furniture | pages [44] -->
Team #44398                                                    Page 44 of 51

<!-- b001760 | caption | pages [44] -->
Table 16  The value of parameters

<!-- b001761 | prose | pages [44] -->
Parameters

<!-- b001762 | prose | pages [44] -->
ft

<!-- b001763 | prose | pages [44] -->
t

<!-- b001764 | prose | pages [44] -->
s 

<!-- b001765 | prose | pages [44] -->
4A

<!-- b001766 | prose | pages [44] -->
 2

<!-- b001767 | prose | pages [44] -->
h

<!-- b001768 | furniture | pages [44] -->


<!-- b001769 | prose | pages [44] -->
4L

<!-- b001770 | prose | pages [44] -->
h

<!-- b001771 | furniture | pages [44] -->


<!-- b001772 | prose | pages [44] -->
4H

<!-- b001773 | prose | pages [44] -->
4k

<!-- b001774 | prose | pages [44] -->
Value Unit

<!-- b001775 | prose | pages [44] -->
℃ 43

<!-- b001776 | prose | pages [44] -->
℃ 25

<!-- b001777 | prose | pages [44] -->
23.2 W

<!-- b001778 | prose | pages [44] -->
2 m 1.05

<!-- b001779 | prose | pages [44] -->
0.03 m

<!-- b001780 | prose | pages [44] -->
   2 W/ m K

<!-- b001781 | furniture | pages [44] -->


<!-- b001782 | prose | pages [44] -->
300,1100

<!-- b001783 | prose | pages [44] -->
   2 W/ m K 10,60

<!-- b001784 | furniture | pages [44] -->


<!-- b001785 | prose | pages [44] -->
   W/ m K 0.3

<!-- b001786 | furniture | pages [44] -->


<!-- b001787 | prose | pages [44] -->
In consideration of the person in bathtub, we correct the above data. To show the influence of bubbles vividly, we compare the results with and without adding bubbles.

<!-- b001788 | caption | pages [44] -->
Table 17  Comparison of adding bubbles and no bubbles

<!-- b001789 | prose | pages [44] -->
Natural convection

<!-- b001790 | prose | pages [44] -->
Forced convection

<!-- b001791 | prose | pages [44] -->
Change

<!-- b001792 | prose | pages [44] -->
Parameters

<!-- b001793 | prose | pages [44] -->
Adding

<!-- b001794 | prose | pages [44] -->
No

<!-- b001795 | prose | pages [44] -->
bubbles

<!-- b001796 | prose | pages [44] -->
bubbles

<!-- b001797 | prose | pages [44] -->


<!-- b001798 | prose | pages [44] -->
Change

<!-- b001799 | prose | pages [44] -->
Adding

<!-- b001800 | prose | pages [44] -->
No

<!-- b001801 | prose | pages [44] -->
bubbles

<!-- b001802 | prose | pages [44] -->
bubbles

<!-- b001803 | prose | pages [44] -->
8.83% 1061.8 1164.7 q

<!-- b001804 | prose | pages [44] -->
2T

<!-- b001805 | prose | pages [44] -->
1376.7 2390.9 42.42%

<!-- b001806 | prose | pages [44] -->
-31.11% 17.87 13.63

<!-- b001807 | prose | pages [44] -->
q

<!-- b001808 | prose | pages [44] -->
13.86 7.33 -89.09%

<!-- b001809 | prose | pages [44] -->
23.53%

<!-- b001810 | furniture | pages [44] -->


<!-- b001811 | prose | pages [44] -->
0.065 0.085 m 1

<!-- b001812 | prose | pages [44] -->
q

<!-- b001813 | prose | pages [44] -->
0.084 0.159 47.17%

<!-- b001814 | prose | pages [44] -->
4.28%

<!-- b001815 | furniture | pages [44] -->


<!-- b001816 | prose | pages [44] -->
0.604 0.631 m 2 0.630 0.729 13.58%

<!-- b001817 | prose | pages [44] -->
From the above table, we find bubbles affect heat transfer heavily. They can not only decrease the heat transfer capacity, but also save hot water. Comparing the two sub-models, the change of parameters in the second sub- model is larger. That indicates the second sub-model is more sensitive to bubbles.

<!-- b001818 | prose | pages [44] -->
In conclusion, adding bubble bath additives can slow down the process of bath water becoming cooler and avoid wasting too much water.

<!-- b001819 | heading | pages [44] -->
8.4  The Influence of Radiation Heat Transfer

<!-- b001820 | prose | pages [44] -->
In our before discussion, we ignore the influence of radiation heat transfer because we assume it to be very small to simplify our model. Now it is time for us to investigate the validity of this assumption.

<!-- b001821 | prose | pages [44] -->
According to Stefan-Boltzmann law, we have

<!-- b001822 | furniture | pages [44] -->


<!-- b001823 | furniture | pages [45] -->
Team #44398                                                    Page 45 of 51

<!-- b001824 | prose | pages [45] -->
   t 273.15   AC f  

<!-- b001825 | furniture | pages [45] -->


<!-- b001826 | prose | pages [45] -->
0 1 0 100     4 4     t 273.15   

<!-- b001827 | prose | pages [45] -->
（49）

<!-- b001828 | prose | pages [45] -->
  

<!-- b001829 | furniture | pages [45] -->


<!-- b001830 | prose | pages [45] -->
100     

<!-- b001831 | prose | pages [45] -->
Because only the top surface of bath water contacts directly with air, so we just take the top surface into consideration. Putting the parameters into formula (49), we derive the approximate value  70W . In reality, when a person takes bath in a bathtub, the total heat transfer capacity is 2652W. the variation of radiation heat transfer is merely 2.64% so that it can be ignored. That indicates the rationality of our assumption.

<!-- b001832 | heading | pages [45] -->
8.5  Conclusion

<!-- b001833 | prose | pages [45] -->
After having corrected our model and determined the influence of possible influencing factors, we finally propose our strategy for the user of bathtub to adopt. From point of

<!-- b001834 | caption | pages [45] -->
Table 18   Results under different situations

<!-- b001835 | prose | pages [45] -->
q Situation Sub-model m

<!-- b001836 | prose | pages [45] -->
I 0.014 Ideal

<!-- b001837 | prose | pages [45] -->
II 0.61

<!-- b001838 | prose | pages [45] -->
I 0.03 Evaporation

<!-- b001839 | prose | pages [45] -->
II 0.63

<!-- b001840 | prose | pages [45] -->
I 0.029 Shape

<!-- b001841 | prose | pages [45] -->
II 0.557

<!-- b001842 | prose | pages [45] -->
I 0.0854 Static

<!-- b001843 | prose | pages [45] -->
II 0.6314

<!-- b001844 | prose | pages [45] -->
I 0.1588 Moving

<!-- b001845 | prose | pages [45] -->
II 0.7293

<!-- b001846 | prose | pages [45] -->
I 0.084 Bubbles

<!-- b001847 | prose | pages [45] -->
II 0.630

<!-- b001848 | prose | pages [45] -->
T Water consumption* 2

<!-- b001849 | prose | pages [45] -->
85.18 1.64h

<!-- b001850 | prose | pages [45] -->
109.8

<!-- b001851 | prose | pages [45] -->
86.40 45min

<!-- b001852 | prose | pages [45] -->
113.4

<!-- b001853 | prose | pages [45] -->
74.40 39.76min

<!-- b001854 | prose | pages [45] -->
100.3

<!-- b001855 | prose | pages [45] -->
85.21 13.63min

<!-- b001856 | prose | pages [45] -->
113.6

<!-- b001857 | prose | pages [45] -->
98.42 7.33min

<!-- b001858 | prose | pages [45] -->
131.3

<!-- b001859 | prose | pages [45] -->
84.97 13.86min

<!-- b001860 | prose | pages [45] -->
113.4

<!-- b001861 | prose | pages [45] -->
* water consumption is the amount of water during an iteration.

<!-- b001862 | heading | pages [45] -->
9  Further Discussion

<!-- b001863 | prose | pages [45] -->
In this part, we will focus on different distribution of inflow faucets. Then we discuss about the real-life application of our model.

<!-- b001864 | heading | pages [45] -->
9.1  Different Distribution of Inflow Faucets

<!-- b001865 | prose | pages [45] -->
In our before discussion, we assume there being just one entrance of inflow.

<!-- b001866 | furniture | pages [45] -->


<!-- b001867 | furniture | pages [46] -->
Team #44398                                                    Page 46 of 51

<!-- b001868 | prose | pages [46] -->
From the simulating outcome, we find the temperature of bath water is hardly even. So we come up with the idea of adding more entrances.

<!-- b001869 | prose | pages [46] -->
The simulation turns out to be as follows

<!-- b001870 | furniture | pages [46] -->


<!-- b001871 | furniture | pages [46] -->


<!-- b001872 | furniture | pages [46] -->


<!-- b001873 | furniture | pages [46] -->


<!-- b001874 | furniture | pages [46] -->


<!-- b001875 | furniture | pages [46] -->


<!-- b001876 | furniture | pages [46] -->


<!-- b001877 | furniture | pages [46] -->


<!-- b001878 | furniture | pages [46] -->


<!-- b001879 | furniture | pages [46] -->


<!-- b001880 | prose | pages [46] -->
(a) One entrance                (b) Two entrance

<!-- b001881 | furniture | pages [46] -->


<!-- b001882 | furniture | pages [46] -->


<!-- b001883 | furniture | pages [46] -->


<!-- b001884 | furniture | pages [46] -->


<!-- b001885 | furniture | pages [46] -->


<!-- b001886 | furniture | pages [46] -->


<!-- b001887 | furniture | pages [46] -->


<!-- b001888 | furniture | pages [46] -->


<!-- b001889 | furniture | pages [46] -->


<!-- b001890 | furniture | pages [46] -->


<!-- b001891 | prose | pages [46] -->
(c) Five entrance        (d) The whole side as entrance

<!-- b001892 | caption | pages [46] -->
Fig.24  The simulation results of different ways of arranging entrances

<!-- b001893 | prose | pages [46] -->
From the above figure, the more the entrances are, the evener the temperature will be. Recalling on the before simulation outcome, when there is only one entrance for inflow, the temperature of corners is quietly lower than the middle area.

<!-- b001894 | prose | pages [46] -->
In conclusion, if we design more entrances, it will be easier to realize the goal to keep temperature even throughout the bathtub.

<!-- b001895 | heading | pages [46] -->
9.2  Model Application

<!-- b001896 | prose | pages [46] -->
Our before discussion is based on ideal assumptions. In reality, we have to make some corrections and improvement.

<!-- b001897 | prose | pages [46] -->
 Adding hot water continually with the mass flow of 0.16 kg/s. This way

<!-- b001898 | furniture | pages [46] -->


<!-- b001899 | furniture | pages [47] -->
Team #44398                                                    Page 47 of 51

<!-- b001900 | prose | pages [47] -->
can ensure even mean temperature throughout the bathtub and waste less water.

<!-- b001901 | prose | pages [47] -->
 The manufacturers can design an intelligent control system to monitor

<!-- b001902 | prose | pages [47] -->
the temperature so that users can get more enjoyable bath experience.

<!-- b001903 | prose | pages [47] -->
 We recommend users to add bubble additives to slow down the water

<!-- b001904 | prose | pages [47] -->
being cooler and help cleanse. The additives with lower thermal conductivity are optimal.

<!-- b001905 | prose | pages [47] -->
 The study method of our establishing model can be applied in other

<!-- b001906 | prose | pages [47] -->
area relative to convection heat transfer, such as air conditioners.

<!-- b001907 | heading | pages [47] -->
10  Strength and Weakness

<!-- b001908 | heading | pages [47] -->
10.1  Strength

<!-- b001909 | prose | pages [47] -->
 We analyze the problem based on thermodynamic formulas and laws,

<!-- b001910 | prose | pages [47] -->
so that the model we established is of great validity.

<!-- b001911 | prose | pages [47] -->
 Our model is fairly robust due to our careful corrections in

<!-- b001912 | prose | pages [47] -->
consideration of real-life situations and detailed sensitivity analysis.

<!-- b001913 | prose | pages [47] -->
 Via Fluent software, we simulate the time field of different areas

<!-- b001914 | prose | pages [47] -->
throughout the bathtub. The outcome is vivid for us to understand the changing process.

<!-- b001915 | prose | pages [47] -->
 We come up with various criteria to compare different situations, like

<!-- b001916 | prose | pages [47] -->
water consumption and the time of adding hot water. Hence an overall comparison can be made according to these criteria.

<!-- b001917 | prose | pages [47] -->
 Besides common factors, we still consider other factors, such as

<!-- b001918 | prose | pages [47] -->
evaporation and radiation heat transfer. The evaporation turns out to be the main reason of heat loss, which corresponds with other scientist’s experimental outcome.

<!-- b001919 | heading | pages [47] -->
10.2  Weakness

<!-- b001920 | prose | pages [47] -->
 Having knowing the range of some parameters from others’ essays, we

<!-- b001921 | prose | pages [47] -->
choose a value from them to apply in our model. Those values may not be reasonable in reality.

<!-- b001922 | furniture | pages [47] -->


<!-- b001923 | furniture | pages [48] -->
Team #44398                                                    Page 48 of 51

<!-- b001924 | prose | pages [48] -->
 Although we investigate a lot in the influence of personal motions,

<!-- b001925 | prose | pages [48] -->
they are so complicated that need to be studied further.

<!-- b001926 | prose | pages [48] -->
 Limited to time, we do not conduct sensitivity analysis for the

<!-- b001927 | prose | pages [48] -->
influence of personal surface area.

<!-- b001928 | furniture | pages [48] -->


<!-- b001929 | furniture | pages [48] -->


<!-- b001930 | furniture | pages [48] -->


<!-- b001931 | prose | pages [49] -->
Report

<!-- b001932 | furniture | pages [49] -->
Team #44398                                                    Page 49 of 51

<!-- b001933 | furniture | pages [49] -->


<!-- b001934 | furniture | pages [49] -->


<!-- b001935 | furniture | pages [49] -->


<!-- b001936 | furniture | pages [49] -->


<!-- b001937 | furniture | pages [49] -->


<!-- b001938 | furniture | pages [49] -->


<!-- b001939 | furniture | pages [49] -->


<!-- b001940 | furniture | pages [49] -->


<!-- b001941 | furniture | pages [49] -->


<!-- b001942 | furniture | pages [49] -->


<!-- b001943 | furniture | pages [49] -->


<!-- b001944 | furniture | pages [49] -->


<!-- b001945 | furniture | pages [49] -->


<!-- b001946 | prose | pages [49] -->
Suggestions

<!-- b001947 | furniture | pages [49] -->


<!-- b001948 | furniture | pages [49] -->


<!-- b001949 | prose | pages [49] -->
In order to enjoy a comfortable bath

<!-- b001950 | furniture | pages [49] -->


<!-- b001951 | prose | pages [49] -->
with even temperature of bath water and without wasting too much water, we

<!-- b001952 | furniture | pages [49] -->


<!-- b001953 | prose | pages [49] -->
propose the following suggestions.

<!-- b001954 | furniture | pages [49] -->


<!-- b001955 | furniture | pages [49] -->


<!-- b001956 | prose | pages [49] -->
Adding hot water consistently

<!-- b001957 | furniture | pages [49] -->


<!-- b001958 | prose | pages [49] -->
Using smaller bathtub if possible

<!-- b001959 | furniture | pages [49] -->


<!-- b001960 | prose | pages [49] -->
Decreasing motions during bath

<!-- b001961 | furniture | pages [49] -->


<!-- b001962 | prose | pages [49] -->
Using bubble bath additives

<!-- b001963 | prose | pages [49] -->
Decreasing motions during bath

<!-- b001964 | prose | pages [49] -->
Arranging more faucets of inflow

<!-- b001965 | furniture | pages [49] -->


<!-- b001966 | heading | pages [49] -->
From simulation results of

<!-- b001967 | prose | pages [49] -->
real-life situations, we find it takes

<!-- b001968 | prose | pages [49] -->
a period of time for the inflow hot

<!-- b001969 | prose | pages [49] -->
water to spread throughout the

<!-- b001970 | prose | pages [49] -->
bathtub. During this process, the

<!-- b001971 | prose | pages [49] -->
bath water continues transferring

<!-- b001972 | prose | pages [49] -->
heat into air, bathtub and the

<!-- b001973 | prose | pages [49] -->
person in bathtub. The difference

<!-- b001974 | prose | pages [49] -->
between heat transfer capacity

<!-- b001975 | prose | pages [49] -->
makes the temperature of various

<!-- b001976 | prose | pages [49] -->
areas to be different. So that it is

<!-- b001977 | prose | pages [49] -->
difficult to get an evenly main-

<!-- b001978 | prose | pages [49] -->
tained temperature throughout the

<!-- b001979 | prose | pages [49] -->
bath water.

<!-- b001980 | furniture | pages [50] -->
Team #44398                                                    Page 50 of 51

<!-- b001981 | prose | pages [50] -->
Reference

<!-- b001982 | prose | pages [50] -->
[1] Gi-Beum Kim. Change of the Warm Water Temperature for the

<!-- b001983 | prose | pages [50] -->
Development of Smart Healthecare Bathing System. Hwahak konghak. 2006,

<!-- b001984 | prose | pages [50] -->
44(3): 270-276.

<!-- b001985 | prose | pages [50] -->
[2] https://en.wikipedia.org/wiki/Convective_heat_transfer#Newton.27s_law

<!-- b001986 | prose | pages [50] -->
_of_cooling

<!-- b001987 | prose | pages [50] -->
[3] https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations

<!-- b001988 | prose | pages [50] -->
[4] https://en.wikipedia.org/wiki/Computational_fluid_dynamics

<!-- b001989 | prose | pages [50] -->
[5] Holman J P. 2002. Heat Transfer (9th ed.) New York: McGraw-Hill.

<!-- b001990 | prose | pages [50] -->
[6] http://www.czs.gov.cn/html/zwgk/ztbd/ggfw/10265/10552/10565/10595/co

<!-- b001991 | prose | pages [50] -->
ntent_393852.html

<!-- b001992 | prose | pages [50] -->
[7] http://www.kankanews.com/IClux/1353641549/2014-01-08/3645040.shtml

<!-- b001993 | prose | pages [50] -->
[8] W. M. Kays, M. E. Crawford, B. Weigand. Convective Heat and Mass

<!-- b001994 | prose | pages [50] -->
Fransfer

<!-- b001995 | prose | pages [50] -->
[9] Shimodozono, Megumi；Matsumoto, Shuji；Ninomiya, Koji；Miyata, Ryuji；

<!-- b001996 | prose | pages [50] -->
Ogata, Atsuko；Etoh, Seiji；Watanabe, Satoshi；Kawahira, Kazumi. Acute

<!-- b001997 | prose | pages [50] -->
effects of a single warm-water bath on serum adiponectin and leptin levels

<!-- b001998 | prose | pages [50] -->
in healthy men: A pilot study. International Journal of Biometeorology. 2012,

<!-- b001999 | prose | pages [50] -->
56(5): 933-939.

<!-- b002000 | prose | pages [50] -->
[10] Anand Mani. Critical Evaluation of Current Skin Thermal Property

<!-- b002001 | prose | pages [50] -->
Measurements.

<!-- b002002 | prose | pages [50] -->
[11] Bennett, Howard (2014-05-25). "Ever wondered about your skin?". The

<!-- b002003 | prose | pages [50] -->
Washington Post. Retrieved 2014-10-27.

<!-- b002004 | prose | pages [50] -->
[12] https://en.wikipedia.org/wiki/Human_skin#cite_note-Bennett-8

<!-- b002005 | prose | pages [50] -->
[13] Wang, Yunjian, Zhu Liang, Rosengart, Axel J. Targeted brain hypothermia

<!-- b002006 | prose | pages [50] -->
induced by an interstitial cooling device in the rat neck: Experimental study

<!-- b002007 | prose | pages [50] -->
and model validation. International Journal of Heat and Mass Transfer.

<!-- b002008 | prose | pages [50] -->
2008(51): 5662-5670.

<!-- b002009 | prose | pages [50] -->
[14] Yang, Yang. Liu, Jing.Detection of Athersclerosis Through Mapping Skin

<!-- b002010 | prose | pages [50] -->
Temperature Variation Caused by Carotid Atherosclerosis Plaques. Journal

<!-- b002011 | prose | pages [50] -->
of Thermal Science and Engineering Applications. 2011(3).

<!-- b002012 | prose | pages [50] -->
[15] Diller, K.R. and Hayes, J.L. A Finite Element Model of burn injury in blood

<!-- b002013 | prose | pages [50] -->
perfused skin. Journal of Biomechanical Engineering. 1983(105): 300-307.

<!-- b002014 | prose | pages [50] -->
[16] Mattix, Steven. Using skin heat transfer anisotropy as a diagnostic tool:

<!-- b002015 | furniture | pages [50] -->


<!-- b002016 | furniture | pages [51] -->
Team #44398                                                    Page 51 of 51

<!-- b002017 | prose | pages [51] -->
Measurement of Skin Thermal Properties. 2010.

<!-- b002018 | prose | pages [51] -->
[17] Kenneth R. Holmes. Thermal Conductivity Data for Specific Tissues and

<!-- b002019 | prose | pages [51] -->
Organs for Humans and other Mammalian Species.

<!-- b002020 | prose | pages [51] -->
[18] http://www.oppein.cn/news/3430

<!-- b002021 | prose | pages [51] -->
[19] Cohen Myron, L. Measurement of the thermal properties of human skin. A

<!-- b002022 | prose | pages [51] -->
Review. Journal of Investigative Dermatology, 69, 333-338.

<!-- b002023 | furniture | pages [51] -->

