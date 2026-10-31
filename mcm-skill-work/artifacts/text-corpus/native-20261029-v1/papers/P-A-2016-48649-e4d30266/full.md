# P-A-2016-48649-e4d30266

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
48649

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | prose | pages [1] -->
F1 ________________

<!-- b000007 | prose | pages [1] -->
T2 ________________

<!-- b000008 | prose | pages [1] -->
F2 ________________

<!-- b000009 | prose | pages [1] -->
T3 ________________

<!-- b000010 | prose | pages [1] -->
F3 ________________

<!-- b000011 | prose | pages [1] -->
Problem Chosen

<!-- b000012 | prose | pages [1] -->
T4 ________________

<!-- b000013 | prose | pages [1] -->
F4 ________________

<!-- b000014 | prose | pages [1] -->
A

<!-- b000015 | prose | pages [1] -->
2016

<!-- b000016 | prose | pages [1] -->
MCM/ICM

<!-- b000017 | heading | pages [1] -->
Summary Sheet

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | prose | pages [1] -->
Based on the existing Finite Element Method (FEM) technique, we consider two models to analyze the temperature distribution in the bathtub, including without and with a person in it. Then, we build two inflow models, namely, the continuous inflow model and the discontinuous inflow model. At last, we employ Fuzzy Comprehensive Evaluation (FCE) to evaluate these two inflow models in order to find an optimal solution.

<!-- b000020 | prose | pages [1] -->
First, regarding the model without a person in the bathtub, we calculate the heat dissipation in the water-to-air heat convection and build a hot-water tube model for calculating the heat addition. What’s more, to find the temperature distribution in the bathtub, we simulate such

<!-- b000021 | prose | pages [1] -->
model on ANSYS, which is a large-scale common finite element software.

<!-- b000022 | prose | pages [1] -->
Second, we consider the model with a person in the bathtub from two aspects, namely, the person in the still and the moving states. Specific to the moving state of person, we find that there exist two ways of dissipating heat, including the water-to-air heat convection and the water-to-bathtub heat conduction. Furthermore, we exploit MATLAB to find the temperature curve in natural cooling process. .

<!-- b000023 | prose | pages [1] -->
Third, based on the analysis of above two conditions, we propose to simulate on the continuous and discontinuous inflow models of the hot water. Besides, to find an optimal strategy, we evaluate these two models using fuzzy comprehensive evaluation (FCE), where the variables include the amount of needed water, the comfortable degree of user, the operation complexity and the operative difficulty index.

<!-- b000024 | prose | pages [1] -->
Fourth, to analyze the sensitivity of two models with and without person, we extensively change the velocity and the temperature of the hot inflow, the air temperature, the surface area, volume and material of the bathtub, and the volume of the person body.

<!-- b000025 | prose | pages [1] -->
At last, we further study the model for cleansing with a bubble bath additive. In this case, we vary the condition of the bubble to observe this model’s performance.

<!-- b000026 | furniture | pages [2] -->
Team #48649

<!-- b000027 | furniture | pages [2] -->
Page 1 of 44

<!-- b000028 | furniture | pages [2] -->
Team #48649

<!-- b000029 | prose | pages [2] -->
January 28，2014

<!-- b000030 | heading | pages [2] -->
Abstract

<!-- b000031 | prose | pages [2] -->
Naturally a non-spa-style bathtub without a secondary heating system and circulating jet will get noticeably cooler after being filled with hot water. The water lose heat both to the air and to the bathtub. One want to keep warm by adding a constant trickle of hot water from the faucet. To handle fluid’s overflowing, the bathtub is designed in such a way that when the tub reached its capacity, excess water escapes through an overflow drain.

<!-- b000032 | prose | pages [2] -->
We build Bathtub without Person model (BWOP) to simulate the water temperature distribution without people inside, and Bathtub with Person (BWP) model to research the natural cooling process and to propose reasonable strategy for user to maintain the temperature. The simulation of BWOP mainly depends on the finite element method (FEM) using ANSYS, while the simulation of BWP mainly depends on the solving of the thermodynamic equation using MATLAB.

<!-- b000033 | keywords | pages [2] -->
Keywords: Heat Convection, Heat Conduction, Finite Element Method, ANSYS

<!-- b000034 | furniture | pages [3] -->
Team #48649

<!-- b000035 | furniture | pages [3] -->
Page 2 of 44

<!-- b000036 | heading | pages [3] -->
Contents

<!-- b000037 | contents | pages [3] -->
1 Introduction ........................................................................................................................... 4

<!-- b000038 | contents | pages [3] -->
1.1 Restatement of the Problem ........................................................................................................ 4

<!-- b000039 | contents | pages [3] -->
2 Assumptions and Justifications ............................................................................................. 4

<!-- b000040 | contents | pages [3] -->
3 Notations ............................................................................................................................... 5

<!-- b000041 | contents | pages [3] -->
4 Model for bathtub without a person in it (BWOP model) .................................................... 6

<!-- b000042 | contents | pages [3] -->
4.1 The calculation of the heat-transfer coefficient .......................................................................... 8

<!-- b000043 | contents | pages [3] -->
4.1.1 The heat-transfer coefficient between the water surface and the air .................................... 8

<!-- b000044 | contents | pages [3] -->
4.1.2 The heat-transfer coefficient between the water and the water tube .................................... 9

<!-- b000045 | contents | pages [3] -->
4.1.3 The heat-transfer coefficient between the hot water and the cube wall ............................. 10

<!-- b000046 | contents | pages [3] -->
4.2 The heat dissipation between the water surface and the air ...................................................... 11

<!-- b000047 | contents | pages [3] -->
4.3 The heat addition between the water and the hot water tube .................................................... 11

<!-- b000048 | contents | pages [3] -->
4.3.1 The heat exchange between the inside and the outside of the tube .................................... 11

<!-- b000049 | contents | pages [3] -->
4.3.2 The heat exchange between the water and the water tube ................................................. 12

<!-- b000050 | contents | pages [3] -->
4.4 Simulation of BWOP model based on ANSYS ........................................................................ 14

<!-- b000051 | contents | pages [3] -->
5 Model for bathtub with a person in it (BWP model) .......................................................... 17

<!-- b000052 | contents | pages [3] -->
5.1 Simulation of the temperature distribution if the person is still ................................................ 18

<!-- b000053 | contents | pages [3] -->
5.2 Heat dissipation in BWP model ................................................................................................ 19

<!-- b000054 | contents | pages [3] -->
5.2.1 Water-Air heat convection ................................................................................................. 19

<!-- b000055 | contents | pages [3] -->
5.2.2 Water-Bathtub heat conduction ......................................................................................... 20

<!-- b000056 | contents | pages [3] -->
5.2.3 The total heat dissipation in the bathtub ............................................................................ 21

<!-- b000057 | contents | pages [3] -->
5.3 Simulation of BWP model with MATLAB .............................................................................. 21

<!-- b000058 | contents | pages [3] -->
5.4 Heat addition model .................................................................................................................. 23

<!-- b000059 | contents | pages [3] -->
5.4.1 Continuous Inflow model (CI model) ................................................................................ 24

<!-- b000060 | contents | pages [3] -->
5.4.2 Discontinuous Inflow model (DCI model) ........................................................................ 26

<!-- b000061 | contents | pages [3] -->
5.4.3 FCE of the two models ...................................................................................................... 28

<!-- b000062 | contents | pages [3] -->
6 Sensitivity analysis.............................................................................................................. 29

<!-- b000063 | contents | pages [3] -->
6.1 Sensitivity analysis for BWOP ................................................................................................. 29

<!-- b000064 | contents | pages [3] -->
6.1.1 Inflow Velocity .................................................................................................................. 29

<!-- b000065 | contents | pages [3] -->
6.1.2 Inflow Temperature ........................................................................................................... 31

<!-- b000066 | contents | pages [3] -->
6.1.3 Air Temperature ................................................................................................................. 32

<!-- b000067 | furniture | pages [4] -->
Team #48649                                                              Page 3 of 44

<!-- b000068 | contents | pages [4] -->
6.1.4 Conclusion ......................................................................................................................... 34

<!-- b000069 | contents | pages [4] -->
6.2 Sensitivity analysis for BWP .................................................................................................... 34

<!-- b000070 | contents | pages [4] -->
6.2.1 Different surface area of the bathtub ................................................................................. 35

<!-- b000071 | contents | pages [4] -->
6.2.2 Different volume of the bathtub ......................................................................................... 36

<!-- b000072 | contents | pages [4] -->
6.2.3 Different material of the bathtub ........................................................................................ 37

<!-- b000073 | contents | pages [4] -->
6.2.4 Different volume of person in the bathtub ......................................................................... 38

<!-- b000074 | contents | pages [4] -->
6.2.5 Conclusion ......................................................................................................................... 38

<!-- b000075 | contents | pages [4] -->
7 Model for Cleansing with a Bubble Bath Additive (CBBA model) ................................... 39

<!-- b000076 | contents | pages [4] -->
8 Weakness and Strength ....................................................................................................... 40

<!-- b000077 | contents | pages [4] -->
8.1 Strengths ................................................................................................................................... 40

<!-- b000078 | contents | pages [4] -->
8.2 Weaknesses ............................................................................................................................... 41

<!-- b000079 | contents | pages [4] -->
References .............................................................................................................................. 42

<!-- b000080 | contents | pages [4] -->
Appendix ................................................................................................................................ 43

<!-- b000081 | furniture | pages [4] -->


<!-- b000082 | furniture | pages [4] -->


<!-- b000083 | furniture | pages [4] -->


<!-- b000084 | furniture | pages [4] -->


<!-- b000085 | furniture | pages [4] -->


<!-- b000086 | furniture | pages [4] -->


<!-- b000087 | furniture | pages [4] -->


<!-- b000088 | furniture | pages [4] -->


<!-- b000089 | furniture | pages [4] -->


<!-- b000090 | furniture | pages [4] -->


<!-- b000091 | furniture | pages [4] -->


<!-- b000092 | furniture | pages [4] -->


<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | furniture | pages [4] -->


<!-- b000095 | furniture | pages [4] -->


<!-- b000096 | furniture | pages [4] -->


<!-- b000097 | furniture | pages [4] -->


<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | furniture | pages [5] -->
Team #48649                                                              Page 4 of 44

<!-- b000100 | heading | pages [5] -->
1 Introduction

<!-- b000101 | heading | pages [5] -->
1.1 Restatement of the Problem

<!-- b000102 | prose | pages [5] -->
We are required to model the bathtub water’s temperature in space and time, which enables an individual to pick the best strategy in order to keep the temperature almost a constant in the bathtub. Besides, the temperature at any time is required to approach the initial state without wasting too much water.

<!-- b000103 | prose | pages [5] -->
By analysis, we proposed to decompose the problem into two sub-problems:

<!-- b000104 | furniture | pages [5] -->


<!-- b000105 | prose | pages [5] -->
 Build a model that can simulate the temperature of the bathtub in space and time.  Propose an optimal strategy. The strategy should satisfy two conditions: waste the least

<!-- b000106 | prose | pages [5] -->
water and let the user feel comfortable.

<!-- b000107 | furniture | pages [5] -->


<!-- b000108 | prose | pages [5] -->
First, for generality, we set the velocity and temperature of inflow, the size and shape of bathtub variables. Then, we try to model the temperature inside. On one hand, the model needs to show the volume-average temperature. On the other hand, it is required to depict the distribution under the influence of heat loss and addition. Then we can change the inputs to

<!-- b000109 | prose | pages [5] -->
do several simulations. Only using many simulation results can we build a relationship between input and output of the complexed thermodynamical system.

<!-- b000110 | prose | pages [5] -->
Second we seek to use the relationship getting from our simulation to find the best strategy for keeping the temperature. In our model, “best” doesn’t not only means “the least water” but “the most comfortable environment for the people” which put weight on the gradient of temperature and limit on the degree (to avoid scald).

<!-- b000111 | prose | pages [5] -->
At last, we try to adjust our model to different initial state such as the bathtub size and shape, the inflow temperature and the motions made by the people. We also take the bubble bath additive in to consideration.

<!-- b000112 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000113 | heading | pages [5] -->
1) Water is stability, incompressible viscous liquid. The compressibility of the water is

<!-- b000114 | prose | pages [5] -->
small enough to be ignored. The water is steady and viscous in cases that we will discuss later.

<!-- b000115 | heading | pages [5] -->
2) The fluid matches the Boussinesq assumptions[1].

<!-- b000116 | prose | pages [5] -->
 The fluid viscous dissipation can be ignored.  All the physical properties except density are constant  For density, we only consider its change in the body force entries in momentum

<!-- b000117 | prose | pages [5] -->
equation, others can be considered as constant.

<!-- b000118 | furniture | pages [5] -->


<!-- b000119 | furniture | pages [6] -->
Team #48649                                                              Page 5 of 44

<!-- b000120 | heading | pages [6] -->
3) The volume of the air is infinite and the temperature of the air keeps constant.

<!-- b000121 | prose | pages [6] -->
Compared to the volume of the water, the volume of the air is much bigger, thus we can think the air is infinite and even. Then we can ignore the heat transfer in the air and take

<!-- b000122 | prose | pages [6] -->
t as a constant. air

<!-- b000123 | heading | pages [6] -->
4) The temperature can be evenly distributed in bathtub at any time when a person is

<!-- b000124 | prose | pages [6] -->
in it (BWP model). When a person settles in the bathtub to cleanse, if the temperature distribution is uneven, he will feel uncomfortable and then he must agitate the water to make the temperature evenly distribution.

<!-- b000125 | heading | pages [6] -->
5) There doesn’t exist heat convection in the water when a person is in the bathtub

<!-- b000126 | prose | pages [6] -->
(BWP model). From assumption 3 we can see, when the person is in the bathtub, the temperature is even in the water, thus there is no convection[2].

<!-- b000127 | heading | pages [6] -->
6) The temperature of the bathtub is at a steady state at any time (BWP model). Heat

<!-- b000128 | prose | pages [6] -->
dissipation can happen through the wall of the bathtub. When the water temperature and the air temperature remain unchanged, the bathtub temperature gradient will reach a steady state after time T. To simply the model, we take time T close to 0, that is, the

<!-- b000129 | prose | pages [6] -->
temperature of the bathtub is at a steady state at any time.

<!-- b000130 | heading | pages [6] -->
7) The bathtub walls and the bottom are adiabatic in BWOP model. In BWOP model,

<!-- b000131 | prose | pages [6] -->
heat dissipation through the wall of the bathtub is relatively small. Thus to simply the model, we take the bathtub as adiabatic.

<!-- b000132 | heading | pages [6] -->
8) All the model in the paper is at the state that the water filled the bathtub. In normal

<!-- b000133 | prose | pages [6] -->
case, people will cleanse in tub with full water, so we just discuss such case and ignore the situation that the tub is unfilled.

<!-- b000134 | heading | pages [6] -->
3 Notations

<!-- b000135 | caption | pages [6] -->
Table 1: Constants

<!-- b000136 | prose | pages [6] -->
Symbol Definition

<!-- b000137 | furniture | pages [6] -->


<!-- b000138 | furniture | pages [6] -->


<!-- b000139 | prose | pages [6] -->
The temperature of the air t

<!-- b000140 | furniture | pages [6] -->


<!-- b000141 | prose | pages [6] -->
air

<!-- b000142 | prose | pages [6] -->
Stefan-Boltzmann constant 

<!-- b000143 | prose | pages [6] -->
Coefficient of cubical expansion [3]

<!-- b000144 | prose | pages [6] -->
Value Units

<!-- b000145 | furniture | pages [6] -->


<!-- b000146 | furniture | pages [6] -->


<!-- b000147 | prose | pages [6] -->
K 298

<!-- b000148 | prose | pages [6] -->
   8 2 4 .5 67 10 W / m K

<!-- b000149 | furniture | pages [6] -->


<!-- b000150 | prose | pages [6] -->
  t/1

<!-- b000151 | furniture | pages [6] -->


<!-- b000152 | furniture | pages [6] -->


<!-- b000153 | prose | pages [6] -->
Kinematic viscosity of the air （313 K ） 

<!-- b000154 | furniture | pages [6] -->


<!-- b000155 | prose | pages [6] -->
air  6 2 15 . 69 10 m / s

<!-- b000156 | furniture | pages [6] -->


<!-- b000157 | furniture | pages [6] -->


<!-- b000158 | prose | pages [6] -->
Kinematic viscosity of the water（313 K ） 

<!-- b000159 | furniture | pages [6] -->


<!-- b000160 | prose | pages [6] -->
water   4 2 .6 56 10 m / s

<!-- b000161 | furniture | pages [6] -->


<!-- b000162 | furniture | pages [6] -->


<!-- b000163 | prose | pages [6] -->
The thermal conductivity of the air(313 K )  [4] air 

<!-- b000164 | furniture | pages [6] -->


<!-- b000165 | prose | pages [6] -->
W / m K 0.02624

<!-- b000166 | prose | pages [6] -->
The thermal conductivity of the water（313 K ）  w

<!-- b000167 | prose | pages [6] -->
The specific heat capacity of water c

<!-- b000168 | furniture | pages [6] -->


<!-- b000169 | prose | pages [6] -->


<!-- b000170 | furniture | pages [6] -->


<!-- b000171 | prose | pages [6] -->
W / m K 0.64

<!-- b000172 | prose | pages [6] -->


<!-- b000173 | furniture | pages [6] -->


<!-- b000174 | prose | pages [6] -->
2.4 kJ / kg K

<!-- b000175 | furniture | pages [6] -->


<!-- b000176 | furniture | pages [7] -->
Team #48649                                                              Page 6 of 44

<!-- b000177 | prose | pages [7] -->
 Dynamic viscosity coefficient of the water

<!-- b000178 | prose | pages [7] -->
Pr [5] Prandtl number

<!-- b000179 | prose | pages [7] -->
 Pa s

<!-- b000180 | prose | pages [7] -->
  4

<!-- b000181 | furniture | pages [7] -->


<!-- b000182 | prose | pages [7] -->
.6 56 10

<!-- b000183 | furniture | pages [7] -->


<!-- b000184 | prose | pages [7] -->
0.7~0.8

<!-- b000185 | furniture | pages [7] -->


<!-- b000186 | caption | pages [7] -->
Table 2: Variables

<!-- b000187 | prose | pages [7] -->
Symbol Definition

<!-- b000188 | furniture | pages [7] -->


<!-- b000189 | prose | pages [7] -->
Units

<!-- b000190 | furniture | pages [7] -->


<!-- b000191 | furniture | pages [7] -->


<!-- b000192 | furniture | pages [7] -->


<!-- b000193 | prose | pages [7] -->
The temperature of the water in the bathtub t

<!-- b000194 | furniture | pages [7] -->


<!-- b000195 | prose | pages [7] -->
water K

<!-- b000196 | prose | pages [7] -->
The temperature of the inflow hot water t

<!-- b000197 | furniture | pages [7] -->


<!-- b000198 | prose | pages [7] -->
win K

<!-- b000199 | prose | pages [7] -->
The high threshold of the water temperature in the bathtub

<!-- b000200 | furniture | pages [7] -->


<!-- b000201 | prose | pages [7] -->
ht

<!-- b000202 | prose | pages [7] -->
K

<!-- b000203 | prose | pages [7] -->
The low threshold of the water temperature in the bathtub lt

<!-- b000204 | prose | pages [7] -->
The surface area of the water sA

<!-- b000205 | prose | pages [7] -->
K

<!-- b000206 | prose | pages [7] -->
2 m

<!-- b000207 | prose | pages [7] -->
The contact area of the water and the bathtub

<!-- b000208 | prose | pages [7] -->
bA

<!-- b000209 | prose | pages [7] -->
The sectional area of the faucet

<!-- b000210 | prose | pages [7] -->
A win

<!-- b000211 | prose | pages [7] -->
The thickness of the bathtub

<!-- b000212 | prose | pages [7] -->
d

<!-- b000213 | furniture | pages [7] -->


<!-- b000214 | prose | pages [7] -->
b

<!-- b000215 | prose | pages [7] -->
The volume of the bathtub V

<!-- b000216 | prose | pages [7] -->
2 m

<!-- b000217 | prose | pages [7] -->
2 m

<!-- b000218 | prose | pages [7] -->
m

<!-- b000219 | prose | pages [7] -->
3 m

<!-- b000220 | prose | pages [7] -->
The thermal conductivity of the bathtub

<!-- b000221 | prose | pages [7] -->
b

<!-- b000222 | furniture | pages [7] -->


<!-- b000223 | prose | pages [7] -->
 W / m K

<!-- b000224 | furniture | pages [7] -->


<!-- b000225 | prose | pages [7] -->
The heat transfer coefficient of the air

<!-- b000226 | prose | pages [7] -->
h air

<!-- b000227 | prose | pages [7] -->


<!-- b000228 | prose | pages [7] -->
Time

<!-- b000229 | prose | pages [7] -->
Inflow velocity

<!-- b000230 | prose | pages [7] -->
v in

<!-- b000231 | prose | pages [7] -->
 2 W / m K s

<!-- b000232 | prose | pages [7] -->
m/ s

<!-- b000233 | prose | pages [7] -->
The heat transfer that goes into the water in unit time

<!-- b000234 | prose | pages [7] -->
Q in

<!-- b000235 | prose | pages [7] -->
kJ The heat dissipation of the whole system in unit time

<!-- b000236 | prose | pages [7] -->
Q d

<!-- b000237 | prose | pages [7] -->
kJ

<!-- b000238 | prose | pages [7] -->
Bathtub without a person in it model BWOP

<!-- b000239 | prose | pages [7] -->
Bathtub with a person in it model BWP

<!-- b000240 | prose | pages [7] -->
Continuous Inflow model CI

<!-- b000241 | prose | pages [7] -->
Discontinuous Inflow model DCI

<!-- b000242 | furniture | pages [7] -->


<!-- b000243 | furniture | pages [7] -->


<!-- b000244 | furniture | pages [7] -->


<!-- b000245 | furniture | pages [7] -->


<!-- b000246 | furniture | pages [7] -->


<!-- b000247 | heading | pages [7] -->
4 Model for bathtub without a person in it (BWOP model)

<!-- b000248 | prose | pages [7] -->
First we discuss the model when there is no person in the bathtub (BWOP model). By BWOP model, we can find the natural temperature distribution in the bathtub. Later (in next section) we will discuss the model for bathtub with a person in it (BWP model) based on the analysis of BWOP model.

<!-- b000249 | prose | pages [7] -->
We make the rule that the faucet is at the middle of the base side and the water outlet is

<!-- b000250 | furniture | pages [7] -->


<!-- b000251 | furniture | pages [8] -->
Team #48649                                                              Page 7 of 44

<!-- b000252 | prose | pages [8] -->
located at the middle of the opposite above side.

<!-- b000253 | prose | pages [8] -->
The BWOP model can be decomposed into two parts:

<!-- b000254 | furniture | pages [8] -->


<!-- b000255 | prose | pages [8] -->
1) The heating process 2) The heat dissipation process

<!-- b000256 | furniture | pages [8] -->


<!-- b000257 | prose | pages [8] -->
In the heating process, the water goes into the bathtub from the faucet and overflow from the water outlet.

<!-- b000258 | prose | pages [8] -->
For calculation, as it’s difficult to find the exact mathematical solution for the distribution of the temperature in space and time, we simplify the BWOP model like this:

<!-- b000259 | prose | pages [8] -->
As Graph 1 shows, the addition of the hot water is equivalent to a hot water tube from faucet to the water outlet, which means, there is a water tube heater to reheat the water in the bathtub.

<!-- b000260 | furniture | pages [8] -->


<!-- b000261 | prose | pages [8] -->
Graph 1: The hot water tube model However, later we will simulate the real model by ANSYS. In the heat dissipation process, the heat dissipates in two ways: the heat transfer between the water surface and the air and the heat transfer between the water and the bathtub. Based on the assumption we can see that the bathtub walls and the bottom are adiabatic, so we only consider the heat dissipation between the water surface and the air.

<!-- b000262 | prose | pages [8] -->
The framework of BWOP model is like this:

<!-- b000263 | furniture | pages [8] -->


<!-- b000264 | furniture | pages [9] -->
Team #48649                                                              Page 8 of 44

<!-- b000265 | furniture | pages [9] -->


<!-- b000266 | prose | pages [9] -->
Graph 2: The framework of BWOP model

<!-- b000267 | heading | pages [9] -->
4.1 The calculation of the heat-transfer coefficient

<!-- b000268 | prose | pages [9] -->
There are many factors influence the heat transfer, we can introduce the heat-transfer coefficient to reflect the heat transfer condition between dielectric.

<!-- b000269 | heading | pages [9] -->
4.1.1 The heat-transfer coefficient between the water surface and the air

<!-- b000270 | prose | pages [9] -->
When the system is under a steady condition, the water keeps the same temperature, we

<!-- b000271 | prose | pages [9] -->
t denote it as , the air temperature is water

<!-- b000272 | prose | pages [9] -->
  t ( t t /) 2 , and we can obtain the n water air

<!-- b000273 | prose | pages [9] -->
transfer coefficient between the water surface

<!-- b000274 | prose | pages [9] -->


<!-- b000275 | prose | pages [9] -->
g

<!-- b000276 | prose | pages [9] -->
(

<!-- b000277 | prose | pages [9] -->
t

<!-- b000278 | prose | pages [9] -->


<!-- b000279 | prose | pages [9] -->
water Gr

<!-- b000280 | prose | pages [9] -->


<!-- b000281 | prose | pages [9] -->
Nu  .0 54

<!-- b000282 | prose | pages [9] -->
Ra  Gr

<!-- b000283 | furniture | pages [9] -->


<!-- b000284 | prose | pages [9] -->
t t ,the qualitative temperature of the air is air

<!-- b000285 | prose | pages [9] -->
   , , Pr nt , then we can find the heat- at air air

<!-- b000286 | prose | pages [9] -->
h and the air as follows: air

<!-- b000287 | prose | pages [9] -->
3

<!-- b000288 | prose | pages [9] -->


<!-- b000289 | prose | pages [9] -->
t

<!-- b000290 | prose | pages [9] -->
)

<!-- b000291 | prose | pages [9] -->
l

<!-- b000292 | prose | pages [9] -->
(4.1)

<!-- b000293 | prose | pages [9] -->
air

<!-- b000294 | prose | pages [9] -->
0

<!-- b000295 | prose | pages [9] -->
2 2

<!-- b000296 | prose | pages [9] -->
air air

<!-- b000297 | prose | pages [9] -->
1 (4.2) Ra 4

<!-- b000298 | prose | pages [9] -->
Pr Pr (4.3)

<!-- b000299 | furniture | pages [10] -->
Team #48649                                                              Page 9 of 44

<!-- b000300 | prose | pages [10] -->
 

<!-- b000301 | prose | pages [10] -->
h Nu air

<!-- b000302 | prose | pages [10] -->
2  m / s : Kinematic viscosity of the air,

<!-- b000303 | furniture | pages [10] -->


<!-- b000304 | prose | pages [10] -->
air

<!-- b000305 | prose | pages [10] -->
: Coefficient of cubical expansion and

<!-- b000306 | prose | pages [10] -->
2 m / s

<!-- b000307 | prose | pages [10] -->
g : Gravitational acceleration,

<!-- b000308 | furniture | pages [10] -->


<!-- b000309 | prose | pages [10] -->
0l : The width of the bathtub, m

<!-- b000310 | prose | pages [10] -->
 : The thermal conductivity of the air, air

<!-- b000311 | prose | pages [10] -->
Nu : Nusselt number Ra : Rayleigh number Gr: Grashof number

<!-- b000312 | prose | pages [10] -->
Pr : Prandtl number

<!-- b000313 | prose | pages [10] -->
air air 0l 0l

<!-- b000314 | prose | pages [10] -->
(4.4)

<!-- b000315 | furniture | pages [10] -->


<!-- b000316 | prose | pages [10] -->
  1 nt/

<!-- b000317 | furniture | pages [10] -->


<!-- b000318 | prose | pages [10] -->
 W W / m K

<!-- b000319 | furniture | pages [10] -->


<!-- b000320 | heading | pages [10] -->
4.1.2 The heat-transfer coefficient between the water and the water tube

<!-- b000321 | prose | pages [10] -->
The heat transfer between the water and the water tube mainly contains two parts[6]: Convection heat loss:

<!-- b000322 | prose | pages [10] -->
 Q h A

<!-- b000323 | furniture | pages [10] -->


<!-- b000324 | prose | pages [10] -->
c water os

<!-- b000325 | prose | pages [10] -->
  A 2

<!-- b000326 | furniture | pages [10] -->


<!-- b000327 | prose | pages [10] -->
os

<!-- b000328 | prose | pages [10] -->
Radiation heat loss:

<!-- b000329 | prose | pages [10] -->
 Q A ( t r os

<!-- b000330 | prose | pages [10] -->
 ( ( t t t ) (4.5) out w a t e

<!-- b000331 | prose | pages [10] -->
r r l (4.6) o u t

<!-- b000332 | prose | pages [10] -->
 4 4 4 (4.7) t ) out out water

<!-- b000333 | prose | pages [10] -->
We can see the temperature of the outside of the water tube is low, and it is a process of

<!-- b000334 | prose | pages [10] -->
heat transfer to water, so the radiation heat loss is quite small and we can ignore it. Thus only the convection heat loss should be taken into consideration. According to our assumptions, the system of the water heat transfer is under stability balance, so the heat transfer between the inside and the outside of the tube is equal to the heat transfer between the water and the water tube,

<!-- b000335 | prose | pages [10] -->


<!-- b000336 | prose | pages [10] -->
2

<!-- b000337 | prose | pages [10] -->


<!-- b000338 | furniture | pages [10] -->


<!-- b000339 | prose | pages [10] -->
Q

<!-- b000340 | prose | pages [10] -->
tube io

<!-- b000341 | prose | pages [10] -->
l n (

<!-- b000342 | prose | pages [10] -->
 l l

<!-- b000343 | prose | pages [10] -->
( (

<!-- b000344 | prose | pages [10] -->
t t t

<!-- b000345 | prose | pages [10] -->
)

<!-- b000346 | prose | pages [10] -->
(4.8)

<!-- b000347 | prose | pages [10] -->
in out

<!-- b000348 | prose | pages [10] -->
r r

<!-- b000349 | prose | pages [10] -->
)

<!-- b000350 | prose | pages [10] -->
out

<!-- b000351 | prose | pages [10] -->
r r

<!-- b000352 | prose | pages [10] -->
in

<!-- b000353 | prose | pages [10] -->
h Thus, we can find the heat-transfer coefficient between the water and the water tube

<!-- b000354 | furniture | pages [10] -->


<!-- b000355 | prose | pages [10] -->
: water

<!-- b000356 | furniture | pages [11] -->
Team #48649                                                              Page 10 of 44

<!-- b000357 | prose | pages [11] -->
Q

<!-- b000358 | prose | pages [11] -->


<!-- b000359 | furniture | pages [11] -->


<!-- b000360 | prose | pages [11] -->
h

<!-- b000361 | prose | pages [11] -->
water

<!-- b000362 | prose | pages [11] -->
r Q

<!-- b000363 | prose | pages [11] -->
ln(

<!-- b000364 | prose | pages [11] -->
out

<!-- b000365 | prose | pages [11] -->
r

<!-- b000366 | prose | pages [11] -->
 (

<!-- b000367 | prose | pages [11] -->
t

<!-- b000368 | prose | pages [11] -->
in

<!-- b000369 | prose | pages [11] -->
in

<!-- b000370 | prose | pages [11] -->


<!-- b000371 | prose | pages [11] -->
2

<!-- b000372 | prose | pages [11] -->
tube

<!-- b000373 | furniture | pages [11] -->


<!-- b000374 | prose | pages [11] -->
c c

<!-- b000375 | prose | pages [11] -->
) ) 

<!-- b000376 | prose | pages [11] -->
t

<!-- b000377 | prose | pages [11] -->
)

<!-- b000378 | prose | pages [11] -->
A

<!-- b000379 | prose | pages [11] -->
water os

<!-- b000380 | prose | pages [11] -->
l l

<!-- b000381 | prose | pages [11] -->
(4.9)

<!-- b000382 | prose | pages [11] -->
2 A : The outside surface area of the water tube, os m

<!-- b000383 | prose | pages [11] -->
: The temperature of the outside of the water tube, K t out

<!-- b000384 | prose | pages [11] -->
int : The temperature of the inside of the water tube, K

<!-- b000385 | prose | pages [11] -->
inr : The water tube inside radius, m

<!-- b000386 | prose | pages [11] -->
r : The water tube outside radius, m out

<!-- b000387 | prose | pages [11] -->
 : The thermal conductivity of the tube, tube

<!-- b000388 | prose | pages [11] -->
l : The length of the tube, m

<!-- b000389 | prose | pages [11] -->
: Emissivity (between 0 and 1)

<!-- b000390 | prose | pages [11] -->
  : Stefan-Boltzmann constant .5 67 10

<!-- b000391 | prose | pages [11] -->
 W / m K

<!-- b000392 | furniture | pages [11] -->


<!-- b000393 | prose | pages [11] -->
8 8 2 4

<!-- b000394 | furniture | pages [11] -->


<!-- b000395 | prose | pages [11] -->
W / m · K

<!-- b000396 | heading | pages [11] -->
4.1.3 The heat-transfer coefficient between the hot water and the cube wall

<!-- b000397 | prose | pages [11] -->
  t ( t t /) 2 We can calculate the qualitative temperature of the hot water

<!-- b000398 | prose | pages [11] -->
  

<!-- b000399 | prose | pages [11] -->
and m win wout

<!-- b000400 | prose | pages [11] -->
mt , we can calculate the coefficient as follows: obtain at , , Pr, w water f

<!-- b000401 | prose | pages [11] -->
ud  (4.10) Re 

<!-- b000402 | prose | pages [11] -->
water

<!-- b000403 | prose | pages [11] -->
  f ( .0 79 ln Re .1

<!-- b000404 | prose | pages [11] -->
(

<!-- b000405 | prose | pages [11] -->
f

<!-- b000406 | prose | pages [11] -->
/ )8 Re Pr

<!-- b000407 | prose | pages [11] -->


<!-- b000408 | prose | pages [11] -->
Nu

<!-- b000409 | prose | pages [11] -->
1

<!-- b000410 | prose | pages [11] -->


<!-- b000411 | prose | pages [11] -->
.1 07 12 7. (

<!-- b000412 | prose | pages [11] -->
f

<!-- b000413 | prose | pages [11] -->
/ )8

<!-- b000414 | prose | pages [11] -->
2

<!-- b000415 | prose | pages [11] -->
 

<!-- b000416 | prose | pages [11] -->
h Nu w hwater d

<!-- b000417 | prose | pages [11] -->
 2 64 ) (4.11)

<!-- b000418 | prose | pages [11] -->


<!-- b000419 | prose | pages [11] -->
f

<!-- b000420 | prose | pages [11] -->
( )

<!-- b000421 | prose | pages [11] -->
(4.12)

<!-- b000422 | prose | pages [11] -->


<!-- b000423 | prose | pages [11] -->
2

<!-- b000424 | prose | pages [11] -->


<!-- b000425 | prose | pages [11] -->
w

<!-- b000426 | prose | pages [11] -->
(Pr (Pr )1

<!-- b000427 | prose | pages [11] -->
3

<!-- b000428 | prose | pages [11] -->
(4.13)

<!-- b000429 | prose | pages [11] -->
According to equation (4.10)-(4.13) we can obtain the heat-transfer coefficient between the

<!-- b000430 | prose | pages [11] -->
h hot water and the cube wall . hwater

<!-- b000431 | prose | pages [11] -->
 ：Kinematic viscosity of the water， water 2 m / s

<!-- b000432 | furniture | pages [11] -->


<!-- b000433 | prose | pages [11] -->
f : Friction coefficient of the inside of the cube

<!-- b000434 | furniture | pages [11] -->


<!-- b000435 | furniture | pages [12] -->
Team #48649                                                              Page 11 of 44

<!-- b000436 | prose | pages [12] -->
: Dynamic viscosity at mt ,

<!-- b000437 | furniture | pages [12] -->


<!-- b000438 | prose | pages [12] -->
 Pa s

<!-- b000439 | prose | pages [12] -->
f

<!-- b000440 | prose | pages [12] -->
: Dynamic viscosity at int ,

<!-- b000441 | furniture | pages [12] -->


<!-- b000442 | prose | pages [12] -->
 Pa s

<!-- b000443 | prose | pages [12] -->
w

<!-- b000444 | prose | pages [12] -->
u : The flow velocity of hot water, m/ s

<!-- b000445 | prose | pages [12] -->
d : The inside diameter of the tube, m

<!-- b000446 | heading | pages [12] -->
4.2 The heat dissipation between the water surface and the air

<!-- b000447 | prose | pages [12] -->
At the water surface, there both exists convective heat transfer and radiative heat transfer.

<!-- b000448 | prose | pages [12] -->
We ignore the thermal radiation of air from the heat dissipation, heat absorption and thermal transpiration. Then we can calculate the convective heat transfer and radiative heat transfer at unit time independently as follows:

<!-- b000449 | furniture | pages [12] -->


<!-- b000450 | prose | pages [12] -->
Convection heat loss:

<!-- b000451 | prose | pages [12] -->
 Q h A t ( c air s water

<!-- b000452 | prose | pages [12] -->
Radiation heat loss:

<!-- b000453 | prose | pages [12] -->
  4 Q A t ( r s water

<!-- b000454 | prose | pages [12] -->
 t ) (4.14) air

<!-- b000455 | prose | pages [12] -->
 4 (4.15) t ) air

<!-- b000456 | prose | pages [12] -->
We can see the temperature of the water surface is low, so compared with the convection heat loss, the radiation heat loss is quite small and we can ignore it. Thus only the convection heat loss should be taken into consideration.

<!-- b000457 | prose | pages [12] -->
At the surface of water, consider the third boundary conditions:

<!-- b000458 | prose | pages [12] -->
 t   

<!-- b000459 | furniture | pages [12] -->


<!-- b000460 | prose | pages [12] -->
h  w z h air  z  (4.16) ( ( t t t ) water air

<!-- b000461 | prose | pages [12] -->
Q : The heat loss caused by convective heat transfer, kJ c

<!-- b000462 | prose | pages [12] -->
Q : The heat loss caused by radiative heat transfer, kJ r

<!-- b000463 | prose | pages [12] -->
2 A : The surface area of the water, m S

<!-- b000464 | prose | pages [12] -->
: The thermal conductivity of the water, w

<!-- b000465 | prose | pages [12] -->
h : The depth of the water, m

<!-- b000466 | prose | pages [12] -->
 W / m K

<!-- b000467 | furniture | pages [12] -->


<!-- b000468 | heading | pages [12] -->
4.3 The heat addition between the water and the hot water tube

<!-- b000469 | heading | pages [12] -->
4.3.1 The heat exchange between the inside and the outside of the tube

<!-- b000470 | prose | pages [12] -->
The inflow hot water temperature in the tube is the hot water’s temperature, the outflow hot water temperature in the tube is equivalent to the temperature in the bathtub after mixture.

<!-- b000471 | furniture | pages [12] -->


<!-- b000472 | furniture | pages [13] -->
Team #48649                                                              Page 12 of 44

<!-- b000473 | prose | pages [13] -->
Thus the water qualitative temperature in the process is equivalent to the average of the inflow

<!-- b000474 | prose | pages [13] -->
 t ( t and outflow hot water temperature m win   t /) 2 . wout

<!-- b000475 | prose | pages [13] -->
Since the wall of the tube is thin and the capacity of it is small, the process that hot water passing the tube can be considered as free of inertia and lag. However, the thermal resistance of the tube can’t be ignored. So the temperature of the outside of the tube is not equal to the inside. According to law of the conservation of energy, we can calculate the temperature of

<!-- b000476 | prose | pages [13] -->
t the outside of the tube as follows: out

<!-- b000477 | prose | pages [13] -->
   c Q ( t t ) KA win wout

<!-- b000478 | prose | pages [13] -->


<!-- b000479 | prose | pages [13] -->
1 1

<!-- b000480 | prose | pages [13] -->
 

<!-- b000481 | prose | pages [13] -->
 K h hwater tube

<!-- b000482 | prose | pages [13] -->
 t t    t win wout 2

<!-- b000483 | prose | pages [13] -->
c : The specific heat capacity of hot water,

<!-- b000484 | prose | pages [13] -->
: The density of hot water,

<!-- b000485 | prose | pages [13] -->
3

<!-- b000486 | furniture | pages [13] -->


<!-- b000487 | prose | pages [13] -->
kg m /

<!-- b000488 | prose | pages [13] -->
Q

<!-- b000489 | prose | pages [13] -->
3 : Volume flowrate of the hot water, m /

<!-- b000490 | prose | pages [13] -->
 t (4.17) is

<!-- b000491 | furniture | pages [13] -->


<!-- b000492 | furniture | pages [13] -->


<!-- b000493 | prose | pages [13] -->
,

<!-- b000494 | prose | pages [13] -->
(4.18)

<!-- b000495 | furniture | pages [13] -->


<!-- b000496 | prose | pages [13] -->
t t out (4.19)

<!-- b000497 | prose | pages [13] -->
 kJ / kg K

<!-- b000498 | furniture | pages [13] -->


<!-- b000499 | furniture | pages [13] -->


<!-- b000500 | prose | pages [13] -->
s s

<!-- b000501 | prose | pages [13] -->
A : The area of the inside wall of the cube, is

<!-- b000502 | prose | pages [13] -->
 2 K : Heat transfer coefficient,

<!-- b000503 | furniture | pages [13] -->


<!-- b000504 | prose | pages [13] -->
W / m K

<!-- b000505 | prose | pages [13] -->
: The thickness of the cube, m

<!-- b000506 | prose | pages [13] -->
h

<!-- b000507 | furniture | pages [13] -->


<!-- b000508 | prose | pages [13] -->
2 m

<!-- b000509 | prose | pages [13] -->
 2 W / m K : The heat-transfer coefficient between the hot water and the cube wall, hwater

<!-- b000510 | furniture | pages [13] -->


<!-- b000511 | prose | pages [13] -->
: The temperature of the inflow hot water, K t win

<!-- b000512 | prose | pages [13] -->
: The temperature of the outflow hot water, K t wout

<!-- b000513 | prose | pages [13] -->
 : The thermal conductivity of the tube, tube

<!-- b000514 | furniture | pages [13] -->


<!-- b000515 | prose | pages [13] -->
 W / m K

<!-- b000516 | furniture | pages [13] -->


<!-- b000517 | heading | pages [13] -->
4.3.2 The heat exchange between the water and the water tube

<!-- b000518 | prose | pages [13] -->
The heat transfer between the water and the water tube can be considered as the natural convection. In the process of natural convection, the basic governing equations are equation of continuity, momentum conservation equation, energy conservation equation. This model is a three-dimensional heat-transfer process and there is no inner heat source, so based on the

<!-- b000519 | furniture | pages [13] -->


<!-- b000520 | furniture | pages [14] -->
Team #48649                                                              Page 13 of 44

<!-- b000521 | prose | pages [14] -->
assumption, we can get the governing equations as follows:

<!-- b000522 | prose | pages [14] -->
Equation of continuity:

<!-- b000523 | prose | pages [14] -->
    ( u ) ( v )   w w   x y

<!-- b000524 | prose | pages [14] -->
Momentum conservation equation:

<!-- b000525 | prose | pages [14] -->
    u u u u      ( u v w ) w      x y z

<!-- b000526 | prose | pages [14] -->
    v v v v      ( u v w ) w      x y z

<!-- b000527 | prose | pages [14] -->
    w w w w      ( u v w ) w      x y z

<!-- b000528 | prose | pages [14] -->
Energy conservation equation:

<!-- b000529 | prose | pages [14] -->
    t t t t   

<!-- b000530 | prose | pages [14] -->
water water water water

<!-- b000531 | furniture | pages [14] -->


<!-- b000532 | prose | pages [14] -->
u v w      x y z

<!-- b000533 | prose | pages [14] -->
   ( ( w )  w 0 (4.20)  z

<!-- b000534 | prose | pages [14] -->
    

<!-- b000535 | prose | pages [14] -->
2 2 2

<!-- b000536 | prose | pages [14] -->
P P u u u     ( ) (4.21) w      2 2 2 x x x y z

<!-- b000537 | prose | pages [14] -->
    

<!-- b000538 | prose | pages [14] -->
2 2 2

<!-- b000539 | prose | pages [14] -->
P P v v v     ( ) (4.22) w      2 2 2 y y x y z

<!-- b000540 | prose | pages [14] -->
   

<!-- b000541 | prose | pages [14] -->
2 2 2

<!-- b000542 | prose | pages [14] -->
P w w w       g ( ) (4.23) w w     2 2 2 z x y z

<!-- b000543 | prose | pages [14] -->
   

<!-- b000544 | prose | pages [14] -->
2 2 2

<!-- b000545 | prose | pages [14] -->
t t t   

<!-- b000546 | prose | pages [14] -->
w water water water

<!-- b000547 | prose | pages [14] -->
(4.24)

<!-- b000548 | prose | pages [14] -->
( )

<!-- b000549 | prose | pages [14] -->
   

<!-- b000550 | prose | pages [14] -->
2 2 2

<!-- b000551 | prose | pages [14] -->
c x y z

<!-- b000552 | prose | pages [14] -->
w w

<!-- b000553 | prose | pages [14] -->
Equation (4.19) -（4.23）form the governing equations in the process of the heat transfer between the water and the water tube. Continuous heat transfer process is steady process. In

<!-- b000554 | prose | pages [14] -->
this case, the temperature won’t change with the time, that is:

<!-- b000555 | prose | pages [14] -->


<!-- b000556 | prose | pages [14] -->
t

<!-- b000557 | furniture | pages [14] -->


<!-- b000558 | prose | pages [14] -->
w a t e r

<!-- b000559 | prose | pages [14] -->
    (4.25)

<!-- b000560 | prose | pages [14] -->
0

<!-- b000561 | furniture | pages [14] -->


<!-- b000562 | prose | pages [14] -->
This is the mathematical differential equation of the flow of the fluid, and then we consider the boundary conditions and initial conditions.

<!-- b000563 | prose | pages [14] -->
Boundary conditions: 1) The tube is heat source and is continuous heat transfer process. The temperature of the

<!-- b000564 | prose | pages [14] -->
t outside of the tube’s boundary condition is obtained by calculation out .

<!-- b000565 | prose | pages [14] -->
2) The walls and the bottom of the bathtub can be considered to be adiabatic。

<!-- b000566 | prose | pages [14] -->


<!-- b000567 | prose | pages [14] -->
t

<!-- b000568 | prose | pages [14] -->
 

<!-- b000569 | prose | pages [14] -->
water

<!-- b000570 | prose | pages [14] -->


<!-- b000571 | prose | pages [14] -->
w z

<!-- b000572 | prose | pages [14] -->
 z

<!-- b000573 | furniture | pages [14] -->


<!-- b000574 | prose | pages [14] -->
Initial conditions:

<!-- b000575 | prose | pages [14] -->
t 1) The temperature of the water water

<!-- b000576 | furniture | pages [14] -->


<!-- b000577 | prose | pages [14] -->
2) The gravitational acceleration g.

<!-- b000578 | prose | pages [14] -->
t 3) The air temperature air

<!-- b000579 | furniture | pages [14] -->


<!-- b000580 | prose | pages [14] -->
  (4.26)

<!-- b000581 | prose | pages [14] -->
0 0 0

<!-- b000582 | prose | pages [14] -->
t t 4) The temperature of the inflow and outflow hot water

<!-- b000583 | furniture | pages [14] -->


<!-- b000584 | furniture | pages [14] -->


<!-- b000585 | furniture | pages [14] -->


<!-- b000586 | furniture | pages [14] -->


<!-- b000587 | prose | pages [14] -->
win wout

<!-- b000588 | furniture | pages [15] -->
Team #48649                                                              Page 14 of 44

<!-- b000589 | prose | pages [15] -->
u : The flow velocity of water at X-direction, m/s

<!-- b000590 | prose | pages [15] -->
v : The flow velocity of water at Y-direction, m/s

<!-- b000591 | prose | pages [15] -->
w : The flow velocity of water at Z-direction, m/s

<!-- b000592 | prose | pages [15] -->
: Dynamic viscosity coefficient of the water, Pa s w

<!-- b000593 | heading | pages [15] -->
4.4 Simulation of BWOP model based on ANSYS

<!-- b000594 | prose | pages [15] -->
To simulate the BWOP model, we use finite element method (FEM) by ANSYS. However, when simulating, we don’t adopt the hot water tube model, as this model is only used to

<!-- b000595 | prose | pages [15] -->
simplify the calculating. ANSYS can deal with the real case that the hot water come from the faucet and the excess water escapes through an overflow drain.

<!-- b000596 | prose | pages [15] -->
The finite element method (FEM): FEM is a numerical technique for finding approximate solutions to boundary value problems for partial differential equations. It uses subdivision of a whole problem domain into simpler parts, called finite elements, and variational methods from the calculus of variations to solve the problem by minimizing an associated error function. Analogous to the idea that connecting many tiny straight lines can approximate a larger circle, FEM encompasses methods for connecting many simple element equations over many small subdomains, named finite elements, to approximate a more complex equation over a larger domain[7].

<!-- b000597 | prose | pages [15] -->
ANSYSY: ANSYS is a large-scale common finite element software. It publishes engineering analysis software across a range of disciplines including finite element analysis, structural analysis, computational fluid dynamics, explicit and implicit methods, and heat transfer. In this paper, we use FLUENT function to analyze BWOP model. FLUENT is based on CFD (Computational Fluid Dynamics), which can simulate fluid flows in a virtual environment — for example, the fluid dynamics of ship hulls; gas turbine engines (including the compressors, combustion chamber, turbines and afterburners); aircraft aerodynamics; pumps, fans, HVAC systems, mixing vessels, hydrocyclones, vacuum cleaners, etc[8].

<!-- b000598 | prose | pages [15] -->
If the system reaches steady state, it should meet the conditions:  The bathtub is filled with water.  The distribution of temperature doesn’t change with time When the system reaches steady state, we use ANSYS to simulate the state of the system temperature-space phase graph. In the 3-D model analysis, we use Hex Dominant unit whose shape is like Graph 3. To adjust to the real size in Table 3 of the tub, we define the tub model as Graph 4.

<!-- b000599 | caption | pages [15] -->
Table 3: Size of the tub

<!-- b000600 | prose | pages [15] -->
cubage(m3) height(m) top-surface-size(m,m) bottom-surface-size(m,m)

<!-- b000601 | prose | pages [15] -->
0.3 0.4 1.4(length),0.7(width) 1.0(length),0.5(width)

<!-- b000602 | furniture | pages [15] -->


<!-- b000603 | furniture | pages [15] -->


<!-- b000604 | furniture | pages [15] -->


<!-- b000605 | furniture | pages [16] -->
Team #48649                                                              Page 15 of 44

<!-- b000606 | furniture | pages [16] -->


<!-- b000607 | prose | pages [16] -->
Graph 3: 3-D Hex Dominant model

<!-- b000608 | furniture | pages [16] -->


<!-- b000609 | furniture | pages [16] -->


<!-- b000610 | furniture | pages [16] -->


<!-- b000611 | furniture | pages [16] -->


<!-- b000612 | furniture | pages [16] -->


<!-- b000613 | furniture | pages [16] -->


<!-- b000614 | prose | pages [16] -->
Graph 4: 3-D Bathtub model Using the ANSYS mesh we get the mesh carve up graph for the bathtub as Graph 5.

<!-- b000615 | furniture | pages [16] -->


<!-- b000616 | prose | pages [16] -->
Graph 5: Mesh Carve up

<!-- b000617 | furniture | pages [16] -->


<!-- b000618 | prose | pages [16] -->
Using FEM by ANSYS, we get the isothermal diagram both inside and outside the bathtub as Graph 6 and Graph 7.

<!-- b000619 | furniture | pages [16] -->


<!-- b000620 | prose | pages [16] -->
Graph 6: The isothermal diagram of the intersecting surface

<!-- b000621 | furniture | pages [16] -->


<!-- b000622 | furniture | pages [17] -->
Team #48649                                                              Page 16 of 44

<!-- b000623 | furniture | pages [17] -->


<!-- b000624 | prose | pages [17] -->
Graph 7: The isothermal diagram of the tub body from outside

<!-- b000625 | furniture | pages [17] -->


<!-- b000626 | prose | pages [17] -->
Calculate the result we get statistic in table 4.

<!-- b000627 | furniture | pages [17] -->


<!-- b000628 | caption | pages [17] -->
Table 4: Report on Volume Integral

<!-- b000629 | prose | pages [17] -->
Average tub-

<!-- b000630 | prose | pages [17] -->
Average top

<!-- b000631 | prose | pages [17] -->
Volume-

<!-- b000632 | prose | pages [17] -->
wall heat

<!-- b000633 | prose | pages [17] -->
surface heat

<!-- b000634 | prose | pages [17] -->
average

<!-- b000635 | prose | pages [17] -->
Volume-

<!-- b000636 | prose | pages [17] -->
Volume-

<!-- b000637 | prose | pages [17] -->
Volume-

<!-- b000638 | prose | pages [17] -->
Maximum

<!-- b000639 | prose | pages [17] -->
Minimum

<!-- b000640 | prose | pages [17] -->
average

<!-- b000641 | prose | pages [17] -->
Temp(k)

<!-- b000642 | prose | pages [17] -->
flux(W)

<!-- b000643 | prose | pages [17] -->
flux(W)

<!-- b000644 | prose | pages [17] -->
Temp(K)

<!-- b000645 | prose | pages [17] -->
Temp(K)

<!-- b000646 | prose | pages [17] -->
Temp(ºC)

<!-- b000647 | prose | pages [17] -->
313.1946 -0.06104 -1.3394727

<!-- b000648 | furniture | pages [17] -->


<!-- b000649 | prose | pages [17] -->
318.0238 312.9532 40.4178

<!-- b000650 | prose | pages [17] -->
From Graph 6 and Graph 7 we can obviously find that due to the heat loss to the air, the top surface of the water in bathtub holds lower temperature than other part inside. Also, it is lower than the volume-average temperature. From Graph 6, it is easy to see the temperature distribution across the intersecting surface. The inflow region from the faucet hold the highest degree and the temperature gets down sharply across the line from the faucet to the main body of the water.

<!-- b000651 | prose | pages [17] -->
From the two graphs, we can excitedly find that the main body of the water in bathtub holds stable and comfortable temperature, which will provide people with a great experience. The

<!-- b000652 | prose | pages [17] -->
statistical data of the volume temperature also indicate that the average degree is about 40º-- the most suitable temperature for human beings in winter. Besides, the maximum point with 318º is limited to a small region around the faucet, it is in low possibility to scald people inside. Even if one touch it by accident, 45ºis much lower than adults’ bearing limit 55ºwhich guarantee the safety.

<!-- b000653 | prose | pages [17] -->
At last, from Graph 7 and data in Table 4, it is interesting to find that the heat loss by the tub-wall is much smaller than that by air. It is also realistic according to our reference.

<!-- b000654 | furniture | pages [17] -->


<!-- b000655 | furniture | pages [17] -->


<!-- b000656 | furniture | pages [17] -->


<!-- b000657 | furniture | pages [18] -->
Team #48649                                                              Page 17 of 44

<!-- b000658 | heading | pages [18] -->
5 Model for bathtub with a person in it (BWP model)

<!-- b000659 | prose | pages [18] -->
We have discussed the case of the temperature distribution in a bathtub without a person in it, and now we consider the case where a person is in the bathtub.

<!-- b000660 | prose | pages [18] -->
In BWP model, we first discuss the temperature distribution in the tub if the person is actionless. Based on this, we make the assumption that the temperature is evenly distributed in BWP model.

<!-- b000661 | prose | pages [18] -->
Then we discuss the heat dissipation process based on two sub-models: Water-Air heat convection and Water-Bathtub heat conduction. We simulate the process with MATLAB.

<!-- b000662 | prose | pages [18] -->
Based on the analysis result, we propose two inflow model: Continuous Inflow model and Discontinuous Inflow model. Then we analysis the performance of each model by fuzzy comprehensive evaluation method (FCE) to find a better one.

<!-- b000663 | prose | pages [18] -->
Graph 8 shows the framework of BWP model:

<!-- b000664 | furniture | pages [18] -->


<!-- b000665 | prose | pages [18] -->
Graph 8: The framework of BWP model

<!-- b000666 | furniture | pages [18] -->


<!-- b000667 | furniture | pages [18] -->


<!-- b000668 | furniture | pages [19] -->
Team #48649                                                              Page 18 of 44

<!-- b000669 | heading | pages [19] -->
5.1 Simulation of the temperature distribution if the person is still

<!-- b000670 | prose | pages [19] -->
Graph 9 shows the model of the bathtub when a person is cleaning. There will be some heat transfer between the water and the person, but it’s small enough to be ignored.

<!-- b000671 | furniture | pages [19] -->


<!-- b000672 | prose | pages [19] -->
Graph 9: Bathtub model with person Now we suppose the person keeps still, thus the temperature of water should distributes naturally. Graph 10 show the isothermal in the bathtub and Graph 11 show the temperature distribution on the body surface of the person.

<!-- b000673 | furniture | pages [19] -->


<!-- b000674 | prose | pages [19] -->
Graph 10: The isothermal diagram of the tub body with a person

<!-- b000675 | prose | pages [19] -->
(We don’t show the person in the graph)

<!-- b000676 | furniture | pages [19] -->


<!-- b000677 | furniture | pages [19] -->


<!-- b000678 | furniture | pages [19] -->


<!-- b000679 | furniture | pages [20] -->
Team #48649                                                              Page 19 of 44

<!-- b000680 | furniture | pages [20] -->


<!-- b000681 | prose | pages [20] -->
Graph 11: The isothermal diagram on the body surface of a person From Graph 11 we can see that the temperature distributes unevenly on the body surface of the person if the person just settles down in the bathtub and keeps still. Thus the person will feel uncomfortable as his upper part of the body feel cool and the lower part of the body feels hot. However, in fact, if a person feel uncomfortable, he must agitate the water to make the temperature distributes more evenly. Based on the analysis, when dealing with BWP model, we can make the assumption that the temperature can be evenly distributed in bathtub at any time when a person is in it.

<!-- b000682 | heading | pages [20] -->
5.2 Heat dissipation in BWP model

<!-- b000683 | prose | pages [20] -->
As the temperature can be evenly distributed, we can make the rule：In time T, if some hot water flows into the bathtub, then the temperature distribution will get even immediately.

<!-- b000684 | prose | pages [20] -->
As we ignore the heat transfer between the water and the person, the dissipation of heat can be decomposed into two parts:

<!-- b000685 | prose | pages [20] -->
 The heat exchange between the water surface and the air (Water-Air).  The heat exchange between the water and the wall of the bathtub (Water-Bathtub) Then we can get the total heat dissipation.

<!-- b000686 | heading | pages [20] -->
5.2.1 Water-Air heat convection

<!-- b000687 | prose | pages [20] -->
This process is similar to the case 4.2, the heat transfer in unit time between the water surface and the air in BWOP model. So we directly get the equation: Convection heat loss:

<!-- b000688 | prose | pages [20] -->
 Q h A t c air

<!-- b000689 | prose | pages [20] -->
The third boundary conditions:

<!-- b000690 | prose | pages [20] -->
 t    w z h  z

<!-- b000691 | furniture | pages [20] -->


<!-- b000692 | prose | pages [20] -->
 ( ( t ) (5.1) s s water air

<!-- b000693 | prose | pages [20] -->
   (5.2) h h ( t t ) air water air

<!-- b000694 | furniture | pages [21] -->
Team #48649                                                              Page 20 of 44

<!-- b000695 | prose | pages [21] -->
Suppose in this process, heat dissipation is

<!-- b000696 | heading | pages [21] -->
5.2.2 Water-Bathtub heat conduction

<!-- b000697 | prose | pages [21] -->
 Q Q Q . 1 c

<!-- b000698 | prose | pages [21] -->
Heat dissipation can also happen at the contact surface of the water and the wall of the bathtub. From the assumption we can see, there doesn’t exist convection in the water when the person is in the bathtub and the temperature of the bathtub at the steady state at any time. Thus the heat transfer process between the water and the bathtub should be a steady process.

<!-- b000699 | furniture | pages [21] -->


<!-- b000700 | prose | pages [21] -->
The heat transfer between the water and the bathtub can be decomposed into two parts:  The heat conduction between the water and the wall of the bathtub (Water-Bathtub

<!-- b000701 | prose | pages [21] -->
process)  The heat convection between the outside surface of the bathtub and the air (Bathtub-

<!-- b000702 | prose | pages [21] -->
Air process).

<!-- b000703 | furniture | pages [21] -->


<!-- b000704 | prose | pages [21] -->
Q . Suppose in this process, heat dissipation in unit time is

<!-- b000705 | furniture | pages [21] -->


<!-- b000706 | prose | pages [21] -->
1) Water-Bathtub process

<!-- b000707 | prose | pages [21] -->
2

<!-- b000708 | prose | pages [21] -->
As the water temperature distributes evenly and the bathtub remains steady state, the heat transfer in Water-Bathtub process is a steady heat conduction process.

<!-- b000709 | prose | pages [21] -->
The equation of heat conduction[9]:

<!-- b000710 | prose | pages [21] -->
  Q

<!-- b000711 | prose | pages [21] -->
2

<!-- b000712 | prose | pages [21] -->
 t t

<!-- b000713 | prose | pages [21] -->
water b

<!-- b000714 | prose | pages [21] -->
(5.3) A A

<!-- b000715 | prose | pages [21] -->
b b b

<!-- b000716 | prose | pages [21] -->
d

<!-- b000717 | prose | pages [21] -->
b

<!-- b000718 | prose | pages [21] -->
: The heat conductivity coefficient of the bathtub. In simulating, b b  0.19 W/m K

<!-- b000719 | furniture | pages [21] -->


<!-- b000720 | prose | pages [21] -->
bt : The temperature of the outside of the bathtub.

<!-- b000721 | prose | pages [21] -->
 2 bA : The contact area of the water and the tub. In simulating,

<!-- b000722 | prose | pages [21] -->
 d : The thickness of the bathtub.

<!-- b000723 | prose | pages [21] -->
d 0.04 b b

<!-- b000724 | furniture | pages [21] -->


<!-- b000725 | prose | pages [21] -->
2) Bathtub-Air process

<!-- b000726 | furniture | pages [21] -->


<!-- b000727 | prose | pages [21] -->
bA 1.53 m

<!-- b000728 | prose | pages [21] -->
m

<!-- b000729 | furniture | pages [21] -->


<!-- b000730 | prose | pages [21] -->
The heat transfer between the bathtub and the air is similar to Water-Air case, which can be taken as 2-dimensional heat convection process.

<!-- b000731 | prose | pages [21] -->
Convection heat loss:

<!-- b000732 | prose | pages [21] -->
 Q 2

<!-- b000733 | prose | pages [21] -->
h

<!-- b000734 | prose | pages [21] -->
 h h A t ( t ) (5.4) airb b b air

<!-- b000735 | prose | pages [21] -->
: The convection coefficient of the contact surface between the air and the bathtub. In airb

<!-- b000736 | furniture | pages [21] -->


<!-- b000737 | furniture | pages [22] -->
Team #48649                                                              Page 21 of 44

<!-- b000738 | prose | pages [22] -->
  2 simulating,

<!-- b000739 | furniture | pages [22] -->


<!-- b000740 | prose | pages [22] -->
h 5 W/m K airb

<!-- b000741 | furniture | pages [22] -->


<!-- b000742 | heading | pages [22] -->
5.2.3 The total heat dissipation in the bathtub

<!-- b000743 | prose | pages [22] -->
By the three models above, we can conclude that, when there is a person in the bathtub,

<!-- b000744 | prose | pages [22] -->
  Q Q the heat dissipation in unit time is 2 Q Q

<!-- b000745 | furniture | pages [22] -->


<!-- b000746 | prose | pages [22] -->
1 1

<!-- b000747 | heading | pages [22] -->
5.3 Simulation of BWP model with MATLAB

<!-- b000748 | prose | pages [22] -->
If there is no heating source, we simulate the Temperature-Time graph with MATLAB to find the thermal losses.

<!-- b000749 | prose | pages [22] -->
Graph 12 shows the heat loss caused by the heat convection between the water surface and the air.

<!-- b000750 | prose | pages [22] -->
Temperature curve of Water-Air heat transfer process 318

<!-- b000751 | prose | pages [22] -->
316

<!-- b000752 | prose | pages [22] -->
314

<!-- b000753 | prose | pages [22] -->
312

<!-- b000754 | prose | pages [22] -->
Temperature/K

<!-- b000755 | prose | pages [22] -->
310

<!-- b000756 | prose | pages [22] -->
308

<!-- b000757 | prose | pages [22] -->
306

<!-- b000758 | prose | pages [22] -->
304

<!-- b000759 | prose | pages [22] -->
302

<!-- b000760 | prose | pages [22] -->
300 0 100 200 300 400 500 600 700 800 900 1000

<!-- b000761 | prose | pages [22] -->
Time/min

<!-- b000762 | furniture | pages [22] -->


<!-- b000763 | prose | pages [22] -->
Graph 12: Temperature curve of Water-Air heat transfer process

<!-- b000764 | furniture | pages [22] -->


<!-- b000765 | furniture | pages [22] -->


<!-- b000766 | furniture | pages [22] -->


<!-- b000767 | furniture | pages [22] -->


<!-- b000768 | furniture | pages [22] -->


<!-- b000769 | furniture | pages [23] -->
Team #48649                                                              Page 22 of 44

<!-- b000770 | prose | pages [23] -->
Temperature curve of Water-Buthtub heat transfer process 318

<!-- b000771 | prose | pages [23] -->
317

<!-- b000772 | prose | pages [23] -->
316

<!-- b000773 | prose | pages [23] -->
315

<!-- b000774 | prose | pages [23] -->
Temperature/K

<!-- b000775 | prose | pages [23] -->
314

<!-- b000776 | prose | pages [23] -->
313

<!-- b000777 | prose | pages [23] -->
312

<!-- b000778 | prose | pages [23] -->
311

<!-- b000779 | prose | pages [23] -->
310

<!-- b000780 | prose | pages [23] -->
309

<!-- b000781 | prose | pages [23] -->
308 0 500 1000 1500 2000 2500 3000

<!-- b000782 | prose | pages [23] -->
Time/min

<!-- b000783 | furniture | pages [23] -->


<!-- b000784 | prose | pages [23] -->
Graph 13: Temperature curve of Water-Bathtub heat transfer process

<!-- b000785 | furniture | pages [23] -->


<!-- b000786 | prose | pages [23] -->
Graph 13 shows the heat loss only caused by the heat conduction between the water and the bathtub. We can find that the heat loss through the bathtub is much slower than the heat

<!-- b000787 | prose | pages [23] -->
loss through the Water-Air surface, which is truthfulness as the thermal conductivity of the bathtub is much smaller than the convection coefficient of the surface between the water and the air.

<!-- b000788 | prose | pages [23] -->
Temperature curve of the total heat transfer process 318

<!-- b000789 | prose | pages [23] -->
316

<!-- b000790 | prose | pages [23] -->
314

<!-- b000791 | prose | pages [23] -->
312

<!-- b000792 | prose | pages [23] -->
Temperature/K

<!-- b000793 | prose | pages [23] -->
310

<!-- b000794 | prose | pages [23] -->
308

<!-- b000795 | prose | pages [23] -->
306

<!-- b000796 | prose | pages [23] -->
304

<!-- b000797 | prose | pages [23] -->
302

<!-- b000798 | prose | pages [23] -->
300 0 100 200 300 400 500 600 700 800 900 1000

<!-- b000799 | prose | pages [23] -->
Time/min

<!-- b000800 | furniture | pages [23] -->


<!-- b000801 | prose | pages [23] -->
Graph 14: Temperature curve of total heat transfer process

<!-- b000802 | prose | pages [23] -->
Graph 14 shows the total heat dissipation in BWP model which contains the Water-Air transfer and the Water-Bathtub transfer. We can see the curve is similar to the curve of the

<!-- b000803 | furniture | pages [23] -->


<!-- b000804 | furniture | pages [24] -->
Team #48649                                                              Page 23 of 44

<!-- b000805 | prose | pages [24] -->
Water-Air case, as most of the heat loss is dissipated through the water surface.

<!-- b000806 | heading | pages [24] -->
5.4 Heat addition model

<!-- b000807 | prose | pages [24] -->
Based on the former analysis of BWP model, we can find the heat dissipation Q in unit time. Our goal is to find an optimal strategy, so now we use two inflow model to simulate the inflow of water:

<!-- b000808 | prose | pages [24] -->
 Continuous Inflow model (CI model)  Discontinuous Inflow model (DCI model). In CI model, the water flow into the bathtub with a constant trickle.

<!-- b000809 | prose | pages [24] -->
In DCI model, the water flow into the bathtub only when the temperature comes below a low threshold value and it will stop watering when the temperature reaches a high threshold value.

<!-- b000810 | prose | pages [24] -->
After discuss the two model, we use the fuzzy comprehensive evaluation to find a better strategy.

<!-- b000811 | prose | pages [24] -->
For normal case, we set the proper cleansing temperature as 313 K, the inflow water temperature as 318 K and the cleansing time as 40 min.

<!-- b000812 | furniture | pages [24] -->


<!-- b000813 | prose | pages [24] -->
The evaluation criteria are:

<!-- b000814 | heading | pages [24] -->
1) The amount of water needed, Wn . We will calculate Wn of each model later.

<!-- b000815 | heading | pages [24] -->
2) The comfortable degree of the user, Cd

<!-- b000816 | prose | pages [24] -->
We can see that people will feel comfortable when the water temperature keeps constant, if the temperature of the water changes frequently, people can feel uncomfortable. Thus we define the comfortable degree as the reciprocal of the  standard deviation of the temperature.

<!-- b000817 | prose | pages [24] -->
1

<!-- b000818 | prose | pages [24] -->


<!-- b000819 | prose | pages [24] -->
Cd

<!-- b000820 | prose | pages [24] -->
n

<!-- b000821 | prose | pages [24] -->


<!-- b000822 | prose | pages [24] -->
(

<!-- b000823 | prose | pages [24] -->
t

<!-- b000824 | prose | pages [24] -->


<!-- b000825 | prose | pages [24] -->
i

<!-- b000826 | prose | pages [24] -->
1

<!-- b000827 | prose | pages [24] -->
t is the average temperature.

<!-- b000828 | heading | pages [24] -->
3) The operation complexity, Oc

<!-- b000829 | prose | pages [24] -->
(5.5)

<!-- b000830 | furniture | pages [24] -->


<!-- b000831 | prose | pages [24] -->
 

<!-- b000832 | prose | pages [24] -->
2

<!-- b000833 | prose | pages [24] -->
t

<!-- b000834 | prose | pages [24] -->
)

<!-- b000835 | prose | pages [24] -->
i i

<!-- b000836 | prose | pages [24] -->
n n

<!-- b000837 | prose | pages [24] -->
If the person always need to open or close the faucet, it will improve the operation complexity. Thus we define the operation complexity as the reciprocal of the operation

<!-- b000838 | prose | pages [24] -->
oT : period

<!-- b000839 | prose | pages [24] -->
1   (0

<!-- b000840 | prose | pages [24] -->
  

<!-- b000841 | furniture | pages [24] -->


<!-- b000842 | prose | pages [24] -->
Oc

<!-- b000843 | prose | pages [24] -->
Oc

<!-- b000844 | prose | pages [24] -->
T o

<!-- b000845 | heading | pages [24] -->
4) The operative difficulty index 

<!-- b000846 | furniture | pages [24] -->


<!-- b000847 | prose | pages [24] -->
(5.6)

<!-- b000848 | prose | pages [24] -->
1)

<!-- b000849 | furniture | pages [25] -->
Team #48649                                                              Page 24 of 44

<!-- b000850 | heading | pages [25] -->
5.4.1 Continuous Inflow model (CI model)

<!-- b000851 | prose | pages [25] -->
In continuous influent model, we let the hot water go into the bathtub with a constant inflow

<!-- b000852 | prose | pages [25] -->
v . When the bathtub is filled with water, excess water will escape through the velocity in

<!-- b000853 | prose | pages [25] -->
v overflow drain with an overflow velocity out . Now we make the rules:

<!-- b000854 | prose | pages [25] -->
 As the maximum of the volume of the bathtub is a constant, we can get that the

<!-- b000855 | prose | pages [25] -->
overflow velocity is a constant and it’s equal to the inflow velocity. That is:

<!-- b000856 | prose | pages [25] -->
 v v

<!-- b000857 | prose | pages [25] -->
 When time  goes from

<!-- b000858 | prose | pages [25] -->
 v (5.7) in in out

<!-- b000859 | prose | pages [25] -->
i, we think the hot water has been mixed evenly i to 1

<!-- b000860 | prose | pages [25] -->
t with the original water, so the temperature of the overflow water

<!-- b000861 | prose | pages [25] -->
i. That is: temperature of the water at 1

<!-- b000862 | prose | pages [25] -->
t wout

<!-- b000863 | prose | pages [25] -->
Now we deeply discuss the CI model.

<!-- b000864 | prose | pages [25] -->
is equal to the wout

<!-- b000865 | prose | pages [25] -->
 (5.8) t  w i ( 1)

<!-- b000866 | prose | pages [25] -->
v keeps constant, which also In the process of the continuous inflow of hot water, in

<!-- b000867 | prose | pages [25] -->
Q is a constant. The heating capacity can be equal to the means, the heating capacity in

<!-- b000868 | prose | pages [25] -->
decrement of the thermal of the inflow hot water and the overflow water. That is[10]:

<!-- b000869 | prose | pages [25] -->
  Q c in w w in

<!-- b000870 | furniture | pages [25] -->


<!-- b000871 | prose | pages [25] -->
 v A ( t t ) (5.9) win win wout

<!-- b000872 | prose | pages [25] -->
The heating process is a steady heat transfer process and the heat go into the bathtub is absorbed by the water entirely. The heat absorbed is consumed in two ways:

<!-- b000873 | prose | pages [25] -->
Q Q is absorbed by the water to raise its temperature, represented by  Part of in wt

<!-- b000874 | prose | pages [25] -->
Q is transferred to the air and the bathtub, which is equal toQ .  Another part of in

<!-- b000875 | prose | pages [25] -->
When time  goes from i, by energy conservation equation: i to 1

<!-- b000876 | prose | pages [25] -->
    Q Q in d

<!-- b000877 | prose | pages [25] -->
t

<!-- b000878 | prose | pages [25] -->
  c V t ( t ) (5.10)  w w w i ( 1) w i ( )

<!-- b000879 | prose | pages [25] -->
 : The temperature of the inflow hot water, C win

<!-- b000880 | prose | pages [25] -->
t

<!-- b000881 | furniture | pages [25] -->


<!-- b000882 | prose | pages [25] -->
i, C  : The temperature of the water in the bathtub at time w i ( )

<!-- b000883 | prose | pages [25] -->
3 V: The volume of the bathtub, m

<!-- b000884 | furniture | pages [25] -->


<!-- b000885 | furniture | pages [25] -->


<!-- b000886 | furniture | pages [26] -->
Team #48649                                                              Page 25 of 44

<!-- b000887 | prose | pages [26] -->
2 A : The sectional area of the faucet, m win

<!-- b000888 | heading | pages [26] -->
1) Find the amount of needed water

<!-- b000889 | furniture | pages [26] -->


<!-- b000890 | prose | pages [26] -->
ct time and we can get the amount of the water needed Suppose the person cleanses for

<!-- b000891 | prose | pages [26] -->
(measured in volume) is:

<!-- b000892 | prose | pages [26] -->
Wn  v A t (5.11) in win c

<!-- b000893 | prose | pages [26] -->
We set the proper water temperature that the people will feel comfortable as 313K. When the water temperature is at 313K, we control the inflow heat the same as the heat dissipation, thus the temperature can stay at the proper temperature.

<!-- b000894 | prose | pages [26] -->
From the graph 14 and calculation we can get:

<!-- b000895 | caption | pages [26] -->
Table 5: Water needed of CI model

<!-- b000896 | prose | pages [26] -->
Inflow velocity

<!-- b000897 | prose | pages [26] -->
(m/min)

<!-- b000898 | prose | pages [26] -->
16.2426

<!-- b000899 | furniture | pages [26] -->


<!-- b000900 | prose | pages [26] -->
3 Water need ( m )

<!-- b000901 | prose | pages [26] -->
0.0735

<!-- b000902 | prose | pages [26] -->
We simulate the Continuous Inflow model with MATLAB and we get the temperature curve as Graph 15 shows.

<!-- b000903 | furniture | pages [26] -->


<!-- b000904 | prose | pages [26] -->
Temperature curve of the continuous inflow process 319

<!-- b000905 | prose | pages [26] -->
318

<!-- b000906 | prose | pages [26] -->
317

<!-- b000907 | prose | pages [26] -->
316

<!-- b000908 | prose | pages [26] -->
Temperature/K

<!-- b000909 | prose | pages [26] -->
315

<!-- b000910 | prose | pages [26] -->
314

<!-- b000911 | prose | pages [26] -->
313

<!-- b000912 | prose | pages [26] -->
312

<!-- b000913 | prose | pages [26] -->
311

<!-- b000914 | prose | pages [26] -->
310 0 100 200 300 400 500 600 700 800 900 1000

<!-- b000915 | prose | pages [26] -->
Time/min

<!-- b000916 | furniture | pages [26] -->


<!-- b000917 | prose | pages [26] -->
Graph 15: Temperature curve of the continuous inflow process

<!-- b000918 | heading | pages [26] -->
2) The comfortable degree of user

<!-- b000919 | furniture | pages [26] -->


<!-- b000920 | prose | pages [26] -->
By MATLAB, the standard deviation of the temperature is 0.09432.

<!-- b000921 | furniture | pages [26] -->


<!-- b000922 | furniture | pages [27] -->
Team #48649                                                              Page 26 of 44

<!-- b000923 | prose | pages [27] -->
Thus we can getCd =10.6021 . CI

<!-- b000924 | heading | pages [27] -->
3) The operation complexity

<!-- b000925 | prose | pages [27] -->
Similarly, the person don’t need operate and the operation period is infinite.

<!-- b000926 | prose | pages [27] -->
SoOc =1

<!-- b000927 | furniture | pages [27] -->


<!-- b000928 | prose | pages [27] -->
CI

<!-- b000929 | heading | pages [27] -->
4) The operative difficulty index

<!-- b000930 | prose | pages [27] -->
In order to keep the temperature unchanged, the operative difficulty index  is high. We

<!-- b000931 | prose | pages [27] -->
 =10 let

<!-- b000932 | furniture | pages [27] -->


<!-- b000933 | furniture | pages [27] -->


<!-- b000934 | heading | pages [27] -->
5.4.2 Discontinuous Inflow model (DCI model)

<!-- b000935 | prose | pages [27] -->
In DCI model, the hot water only inflow when the temperature comes below a low threshold

<!-- b000936 | prose | pages [27] -->
lt and it will stop inflow when the temperature of the water comes above a high value

<!-- b000937 | prose | pages [27] -->
, there are two stages: heating stage and cooling stage. threshold value ht . In a time period p

<!-- b000938 | prose | pages [27] -->
 Heating stage

<!-- b000939 | prose | pages [27] -->
 t t , the faucet is opened and the hot water inflow with a constant velocity When water l

<!-- b000940 | prose | pages [27] -->
  v , the temperature of the water reaches the high for time . After time p 1 p 1 in

<!-- b000941 | prose | pages [27] -->
threshold value ht , thus the hot water stop inflowing.

<!-- b000942 | prose | pages [27] -->
This process is similar to the CI model, so we can get the equation directly:

<!-- b000943 | prose | pages [27] -->
    Q Q c in p 1 d p 1

<!-- b000944 | prose | pages [27] -->
 t t   w ( ) p 1

<!-- b000945 | prose | pages [27] -->
 t w ( )

<!-- b000946 | prose | pages [27] -->
is reference time.

<!-- b000947 | prose | pages [27] -->
wt

<!-- b000948 | prose | pages [27] -->
  V t ( t ) (5.9)    w w w w ( ) w ( ) p 1

<!-- b000949 | prose | pages [27] -->
(5.10) h h

<!-- b000950 | prose | pages [27] -->
(5.11) t t l l

<!-- b000951 | prose | pages [27] -->
 is the temperature of the water after time   ( ) p 1

<!-- b000952 | prose | pages [27] -->
 Cooling stage

<!-- b000953 | prose | pages [27] -->
. p 1

<!-- b000954 | prose | pages [27] -->
 The water will cool down from high temperature ht to lower one lt for time . This p 1

<!-- b000955 | prose | pages [27] -->
process is a natural cooling process. Without internal heat source, the thermal equation becomes:

<!-- b000956 | prose | pages [27] -->
    0 Q c V t ( d p 2 w w w

<!-- b000957 | furniture | pages [27] -->


<!-- b000958 | prose | pages [27] -->
 t ) (5.12)        ( ( ) w ( ) p 1 p 2 p 1

<!-- b000959 | furniture | pages [28] -->
Team #48649                                                              Page 27 of 44

<!-- b000960 | prose | pages [28] -->
 t t     w ( ) p 1 p 2

<!-- b000961 | heading | pages [28] -->
1) Find the amount of needed water

<!-- b000962 | prose | pages [28] -->
 lt 312 K We set the low threshold value

<!-- b000963 | prose | pages [28] -->
 t (5.13)   w w ( ( ) l p

<!-- b000964 | furniture | pages [28] -->


<!-- b000965 | prose | pages [28] -->
 ht 314 K , the high threshold value .

<!-- b000966 | prose | pages [28] -->
Temperature curve of the discontinuous inflow process 319

<!-- b000967 | prose | pages [28] -->
318

<!-- b000968 | prose | pages [28] -->
317

<!-- b000969 | prose | pages [28] -->
316

<!-- b000970 | prose | pages [28] -->
Temperature/K

<!-- b000971 | prose | pages [28] -->
315

<!-- b000972 | prose | pages [28] -->
314

<!-- b000973 | prose | pages [28] -->
313

<!-- b000974 | prose | pages [28] -->
312

<!-- b000975 | prose | pages [28] -->
311

<!-- b000976 | prose | pages [28] -->
310 0 100 200 300 400 500 600 700 800 900 1000

<!-- b000977 | prose | pages [28] -->
Time/min

<!-- b000978 | furniture | pages [28] -->


<!-- b000979 | prose | pages [28] -->
Graph 16: Temperature curve of the discontinuous inflow process By this graph we can get the amount of the water needed:

<!-- b000980 | caption | pages [28] -->
Table 6: Water needed of DCI model

<!-- b000981 | prose | pages [28] -->
Inflow velocity

<!-- b000982 | prose | pages [28] -->
(m/min)

<!-- b000983 | prose | pages [28] -->
25.67

<!-- b000984 | heading | pages [28] -->
2) The comfortable degree of user

<!-- b000985 | prose | pages [28] -->
3 Water need ( m )

<!-- b000986 | prose | pages [28] -->
0.0524

<!-- b000987 | prose | pages [28] -->
By MATLAB, the standard deviation of the temperature is 0.5961.

<!-- b000988 | prose | pages [28] -->
Thus we can getCd =1.67757 . DCI

<!-- b000989 | heading | pages [28] -->
3) The operation complexity

<!-- b000990 | prose | pages [28] -->
By MATLAB, the operation period is 94min.

<!-- b000991 | prose | pages [28] -->
Thus we can get Oc =0.01064

<!-- b000992 | furniture | pages [28] -->


<!-- b000993 | prose | pages [28] -->
DCI

<!-- b000994 | heading | pages [28] -->
4) The operative difficulty index

<!-- b000995 | prose | pages [28] -->
It’s easy if the person just open the faucet with a relatively high water velocity, thus we

<!-- b000996 | prose | pages [28] -->
;

<!-- b000997 | prose | pages [28] -->
1 set

<!-- b000998 | furniture | pages [28] -->


<!-- b000999 | furniture | pages [28] -->


<!-- b001000 | furniture | pages [29] -->
Team #48649                                                              Page 28 of 44

<!-- b001001 | heading | pages [29] -->
5.4.3 FCE of the two models

<!-- b001002 | prose | pages [29] -->
FCE is a useful method for multiple criteria decision process. It determines the weights of each criterion based on the data only. Based on the actual statistics of the 2 strategies, we get the values of each factor from section 5.4 and show them in Table 7.

<!-- b001003 | caption | pages [29] -->
Table 7: values of factors and allocations

<!-- b001004 | prose | pages [29] -->
The comfortable Model 3 Water need ( m )

<!-- b001005 | prose | pages [29] -->
operation

<!-- b001006 | prose | pages [29] -->
operative

<!-- b001007 | prose | pages [29] -->
degree

<!-- b001008 | prose | pages [29] -->
complexity

<!-- b001009 | prose | pages [29] -->
difficulty index

<!-- b001010 | prose | pages [29] -->
10.0621 CI 0.0735 1 10 1.67757 DCI 0.0524

<!-- b001011 | furniture | pages [29] -->


<!-- b001012 | prose | pages [29] -->
0.01064 1

<!-- b001013 | prose | pages [29] -->
From Table 7, we derive the ideal allocation as follows,

<!-- b001014 | prose | pages [29] -->
 (0.0524, 10.6021, 1, 1)                   (5.14) u

<!-- b001015 | furniture | pages [29] -->


<!-- b001016 | prose | pages [29] -->
 The Fuzzy Evaluation Matrix (FEM)

<!-- b001017 | prose | pages [29] -->
We define

<!-- b001018 | prose | pages [29] -->


<!-- b001019 | prose | pages [29] -->
r

<!-- b001020 | prose | pages [29] -->
i

<!-- b001021 | prose | pages [29] -->
,

<!-- b001022 | prose | pages [29] -->
j

<!-- b001023 | prose | pages [29] -->
max{

<!-- b001024 | prose | pages [29] -->
We obtain the FEM

<!-- b001025 | prose | pages [29] -->


<!-- b001026 | prose | pages [29] -->
0 . 0021

<!-- b001027 | prose | pages [29] -->


<!-- b001028 | furniture | pages [29] -->


<!-- b001029 | furniture | pages [29] -->


<!-- b001030 | furniture | pages [29] -->


<!-- b001031 | furniture | pages [29] -->


<!-- b001032 | furniture | pages [29] -->


<!-- b001033 | prose | pages [29] -->
R

<!-- b001034 | prose | pages [29] -->
 

<!-- b001035 | prose | pages [29] -->
0 0

<!-- b001036 | prose | pages [29] -->
Also we define

<!-- b001037 | prose | pages [29] -->
s

<!-- b001038 | prose | pages [29] -->


<!-- b001039 | prose | pages [29] -->
j

<!-- b001040 | furniture | pages [29] -->


<!-- b001041 | furniture | pages [29] -->


<!-- b001042 | furniture | pages [29] -->


<!-- b001043 | furniture | pages [29] -->


<!-- b001044 | prose | pages [29] -->
v

<!-- b001045 | prose | pages [29] -->
j

<!-- b001046 | prose | pages [29] -->
X

<!-- b001047 | prose | pages [29] -->
j

<!-- b001048 | prose | pages [29] -->
Then we get

<!-- b001049 | prose | pages [29] -->
 

<!-- b001050 | prose | pages [29] -->


<!-- b001051 | prose | pages [29] -->
a u

<!-- b001052 | prose | pages [29] -->
i

<!-- b001053 | prose | pages [29] -->
,

<!-- b001054 | prose | pages [29] -->
j j

<!-- b001055 | prose | pages [29] -->
(5.15)

<!-- b001056 | prose | pages [29] -->


<!-- b001057 | prose | pages [29] -->
a a

<!-- b001058 | prose | pages [29] -->
} min{

<!-- b001059 | prose | pages [29] -->
a

<!-- b001060 | prose | pages [29] -->
}

<!-- b001061 | prose | pages [29] -->
i

<!-- b001062 | prose | pages [29] -->
,

<!-- b001063 | prose | pages [29] -->
j i

<!-- b001064 | prose | pages [29] -->
,

<!-- b001065 | prose | pages [29] -->
j

<!-- b001066 | prose | pages [29] -->


<!-- b001067 | prose | pages [29] -->
0 0 0 . 9045 (5.16)

<!-- b001068 | prose | pages [29] -->
 

<!-- b001069 | prose | pages [29] -->
. . 8364 0 . 0994 0

<!-- b001070 | furniture | pages [29] -->


<!-- b001071 | prose | pages [29] -->
v

<!-- b001072 | prose | pages [29] -->


<!-- b001073 | prose | pages [29] -->
j

<!-- b001074 | prose | pages [29] -->
(5.17)

<!-- b001075 | prose | pages [29] -->
, ,

<!-- b001076 | prose | pages [29] -->
w

<!-- b001077 | prose | pages [29] -->
j

<!-- b001078 | prose | pages [29] -->
4

<!-- b001079 | prose | pages [29] -->


<!-- b001080 | prose | pages [29] -->
v

<!-- b001081 | prose | pages [29] -->
j

<!-- b001082 | prose | pages [29] -->


<!-- b001083 | prose | pages [29] -->
i j

<!-- b001084 | prose | pages [29] -->
(0.3, 0.15, 0.15, 0.4)                    (5.18)

<!-- b001085 | furniture | pages [29] -->


<!-- b001086 | furniture | pages [29] -->


<!-- b001087 | furniture | pages [29] -->


<!-- b001088 | furniture | pages [29] -->


<!-- b001089 | furniture | pages [29] -->


<!-- b001090 | furniture | pages [29] -->


<!-- b001091 | prose | pages [29] -->
 Result of the FCE

<!-- b001092 | prose | pages [29] -->
Define the relative deviation as

<!-- b001093 | prose | pages [29] -->
 F   T (5.19) R

<!-- b001094 | prose | pages [29] -->
F measures the distance from a specific factor group to the ideal one, so the smaller

<!-- b001095 | prose | pages [29] -->
F is, the better the strategy is. Then we get the final result shown in Table 8.

<!-- b001096 | furniture | pages [29] -->


<!-- b001097 | caption | pages [29] -->
Table 8: FCE result for two strategies

<!-- b001098 | furniture | pages [29] -->


<!-- b001099 | furniture | pages [30] -->
Team #48649                                                              Page 29 of 44

<!-- b001100 | furniture | pages [30] -->


<!-- b001101 | prose | pages [30] -->
CI DCI

<!-- b001102 | furniture | pages [30] -->


<!-- b001103 | prose | pages [30] -->
F

<!-- b001104 | prose | pages [30] -->
0.3624 0.1404

<!-- b001105 | prose | pages [30] -->
The result tells us that: the DCI model is better when we take all the factor into consideration. DCI model is economic and operable, which is very important for our users.

<!-- b001106 | heading | pages [30] -->
6 Sensitivity analysis

<!-- b001107 | heading | pages [30] -->
6.1 Sensitivity analysis for BWOP

<!-- b001108 | prose | pages [30] -->
Considering our simulation results on BWOP model, the heat loss by the bathtub-wall is less than 10 percent of that by water-air convection. In our further discussion on the model, we ignore this aspect and pay our attention to other parameters such as the air temperature, the inflow temperature and the inflow velocity. We choose four main criteria to evaluate the model: the average top surface heat flux, volume-average temperature, Volume-maximum temperature and volume-minimum temperature.

<!-- b001109 | prose | pages [30] -->
By using control variate method, we change the parameters from the best condition to see their effect on the four criteria. By doing simulation we get the result shown in Table 9, Table 10 and Table 11.

<!-- b001110 | heading | pages [30] -->
6.1.1 Inflow Velocity

<!-- b001111 | caption | pages [30] -->
Table 9: Results by Changing Inflow Velocity

<!-- b001112 | prose | pages [30] -->
Average top

<!-- b001113 | prose | pages [30] -->
Inflow

<!-- b001114 | prose | pages [30] -->
Volume-

<!-- b001115 | prose | pages [30] -->
Volume-

<!-- b001116 | prose | pages [30] -->
Volume-

<!-- b001117 | prose | pages [30] -->
surface heat

<!-- b001118 | prose | pages [30] -->
Velocity

<!-- b001119 | prose | pages [30] -->
Inflow

<!-- b001120 | prose | pages [30] -->
Air

<!-- b001121 | prose | pages [30] -->
average

<!-- b001122 | prose | pages [30] -->
maximum

<!-- b001123 | prose | pages [30] -->
minimum

<!-- b001124 | prose | pages [30] -->
flux(W)

<!-- b001125 | prose | pages [30] -->
(m/s)

<!-- b001126 | prose | pages [30] -->
Temp(K)

<!-- b001127 | prose | pages [30] -->
Temp(K)

<!-- b001128 | prose | pages [30] -->
Temp(K)

<!-- b001129 | prose | pages [30] -->
Temp(K)

<!-- b001130 | prose | pages [30] -->
Temp(K)

<!-- b001131 | prose | pages [30] -->
1.1590 0.01 318 298 310.3719 318.101 309.9957 1.4406 0.02 318 298 313.4178 318.024 312.9532 1.5651 0.03 318 298 314.7500 318.007 314.2474 1.6329 0.04 318 298 315.4771 318.003 314.9534 1.6765 0.05 318 298

<!-- b001132 | furniture | pages [30] -->


<!-- b001133 | prose | pages [30] -->
315.9474 318.003 315.4104

<!-- b001134 | furniture | pages [31] -->
Team #48649                                                              Page 30 of 44

<!-- b001135 | prose | pages [31] -->
Temperature-Inflow Velocity graph 319

<!-- b001136 | prose | pages [31] -->
318

<!-- b001137 | prose | pages [31] -->
317

<!-- b001138 | prose | pages [31] -->
316

<!-- b001139 | prose | pages [31] -->
Temperature/K

<!-- b001140 | prose | pages [31] -->
315

<!-- b001141 | prose | pages [31] -->
314

<!-- b001142 | prose | pages [31] -->
313

<!-- b001143 | prose | pages [31] -->
312

<!-- b001144 | prose | pages [31] -->
311

<!-- b001145 | prose | pages [31] -->
310

<!-- b001146 | prose | pages [31] -->
309

<!-- b001147 | furniture | pages [31] -->


<!-- b001148 | prose | pages [31] -->
0.01 0.015 0.02 0.025

<!-- b001149 | furniture | pages [31] -->


<!-- b001150 | prose | pages [31] -->
Volume-average Temp Volume-maximum Temp Volume-minimum Temp

<!-- b001151 | prose | pages [31] -->
0.03 0.035 0.04 0.045 0.05

<!-- b001152 | prose | pages [31] -->
Inflow Velocity/(m/s)

<!-- b001153 | furniture | pages [31] -->


<!-- b001154 | prose | pages [31] -->
Graph 17: Temperature-Inflow Velocity graph

<!-- b001155 | furniture | pages [31] -->


<!-- b001156 | furniture | pages [31] -->


<!-- b001157 | prose | pages [31] -->
Average top surface heat flux-Inflow Velocity graph 1.8

<!-- b001158 | prose | pages [31] -->
1.7

<!-- b001159 | prose | pages [31] -->
1.6

<!-- b001160 | prose | pages [31] -->
heat flux/W

<!-- b001161 | prose | pages [31] -->
1.5

<!-- b001162 | prose | pages [31] -->
1.4

<!-- b001163 | prose | pages [31] -->
1.3

<!-- b001164 | prose | pages [31] -->
1.2

<!-- b001165 | prose | pages [31] -->
1.1 0.01 0.015 0.02 0.025 0.03 0.035 0.04 0.045 0.05

<!-- b001166 | prose | pages [31] -->
Inflow Velocity/(m/s)

<!-- b001167 | furniture | pages [31] -->


<!-- b001168 | prose | pages [31] -->
Graph 18: Average top surface heat-Inflow Velocity graph From Table 9 and the corresponding graph we can notice that: the average top surface heat flux, the volume-average temperature and volume-minimum temperature have positive correlation with inflow velocity, and the raising rate goes down as the inflow velocity goes up for the maximum temperature is bounded. It is corresponding to our common sense that more hot water per second leads to a higher temperature. The heat flux of the top surface is also

<!-- b001169 | prose | pages [31] -->
determined by the volume average temperature with air temperature fixed.

<!-- b001170 | furniture | pages [31] -->


<!-- b001171 | furniture | pages [31] -->


<!-- b001172 | furniture | pages [32] -->
Team #48649                                                              Page 31 of 44

<!-- b001173 | heading | pages [32] -->
6.1.2 Inflow Temperature

<!-- b001174 | caption | pages [32] -->
Table 10: Results by Changing Inflow Temperature

<!-- b001175 | prose | pages [32] -->
Average top

<!-- b001176 | prose | pages [32] -->
Inflow

<!-- b001177 | prose | pages [32] -->
Volume-

<!-- b001178 | prose | pages [32] -->
Volume-

<!-- b001179 | prose | pages [32] -->
Volume-

<!-- b001180 | prose | pages [32] -->
surface heat

<!-- b001181 | prose | pages [32] -->
Velocity

<!-- b001182 | prose | pages [32] -->
Inflow

<!-- b001183 | prose | pages [32] -->
Air

<!-- b001184 | prose | pages [32] -->
average

<!-- b001185 | prose | pages [32] -->
maximum

<!-- b001186 | prose | pages [32] -->
minimum

<!-- b001187 | prose | pages [32] -->
flux(W)

<!-- b001188 | prose | pages [32] -->
(m/s)

<!-- b001189 | prose | pages [32] -->
Temp(K)

<!-- b001190 | prose | pages [32] -->
Temp(K)

<!-- b001191 | prose | pages [32] -->
Temp(K)

<!-- b001192 | prose | pages [32] -->
Temp(K)

<!-- b001193 | prose | pages [32] -->
Temp(K)

<!-- b001194 | prose | pages [32] -->
1.1525 0.02 314 298 310.3342 314.019 309.9626 1.2966 0.02 316 298 311.8761 316.025 311.4579 1.5652 0.02 318 298 313.4178 318.024 312.9532 1.5871 0.02 320 298 314.9596 320.026 314.4485 1.7287 0.02 322 298

<!-- b001195 | furniture | pages [32] -->


<!-- b001196 | prose | pages [32] -->
316.5013 322.029 315.9438

<!-- b001197 | prose | pages [32] -->
Volume Temperature-Inflow Temperature graph 324

<!-- b001198 | prose | pages [32] -->
322

<!-- b001199 | prose | pages [32] -->
320

<!-- b001200 | prose | pages [32] -->
Volume Temperature/K

<!-- b001201 | prose | pages [32] -->
318

<!-- b001202 | prose | pages [32] -->
316

<!-- b001203 | prose | pages [32] -->
314

<!-- b001204 | prose | pages [32] -->
312

<!-- b001205 | prose | pages [32] -->
310

<!-- b001206 | prose | pages [32] -->
308

<!-- b001207 | furniture | pages [32] -->


<!-- b001208 | prose | pages [32] -->
314 315 316 317

<!-- b001209 | furniture | pages [32] -->


<!-- b001210 | prose | pages [32] -->
Volume-average Temp Volume-maximum Temp Volume-minimum Temp

<!-- b001211 | prose | pages [32] -->
318 319 320 321 322

<!-- b001212 | prose | pages [32] -->
Inflow Temperature/K

<!-- b001213 | furniture | pages [32] -->


<!-- b001214 | prose | pages [32] -->
Graph 19: Volume Temperature- Inflow Temperature graph

<!-- b001215 | furniture | pages [32] -->


<!-- b001216 | furniture | pages [33] -->
Team #48649                                                              Page 32 of 44

<!-- b001217 | prose | pages [33] -->
Average top surface heat flux-Inflow Temperature graph 1.9

<!-- b001218 | prose | pages [33] -->
1.8

<!-- b001219 | prose | pages [33] -->
1.7

<!-- b001220 | prose | pages [33] -->
1.6

<!-- b001221 | prose | pages [33] -->
heat flux/W

<!-- b001222 | prose | pages [33] -->
1.5

<!-- b001223 | prose | pages [33] -->
1.4

<!-- b001224 | prose | pages [33] -->
1.3

<!-- b001225 | prose | pages [33] -->
1.2

<!-- b001226 | prose | pages [33] -->
1.1 314 315 316 317 318 319 320 321 322

<!-- b001227 | prose | pages [33] -->
Inflow Temperature/K

<!-- b001228 | furniture | pages [33] -->


<!-- b001229 | prose | pages [33] -->
Graph 20: Average top surface heat - Inflow Temperature graph From Table 10 and the corresponding graph we can notice that: the average top surface heat flux, the volume-average temperature, the volume-maximum temperature and volume- minimum temperature have positive correlation with inflow temperature, and the raising rate

<!-- b001230 | prose | pages [33] -->
keeps still as the inflow velocity goes up. It is corresponding to our common sense that the hotter the inflow, the warmer the bathtub water. And different from the inflow velocity, all the criteria changes at almost direct proportion. That indicates adding hotter inflow is the most effective way to keep the bathtub warm. However, considering about people’s bearing capacity on water temperature and comfortability, the inflow temperature have to be bounded under 323K to avoid scald.

<!-- b001231 | furniture | pages [33] -->


<!-- b001232 | heading | pages [33] -->
6.1.3 Air Temperature

<!-- b001233 | caption | pages [33] -->
Table 11: Results by Changing Air Temperature

<!-- b001234 | prose | pages [33] -->
Average top

<!-- b001235 | prose | pages [33] -->
Inflow

<!-- b001236 | prose | pages [33] -->
Volume-

<!-- b001237 | prose | pages [33] -->
Volume-

<!-- b001238 | prose | pages [33] -->
Volume-

<!-- b001239 | prose | pages [33] -->
surface heat

<!-- b001240 | prose | pages [33] -->
Velocity

<!-- b001241 | prose | pages [33] -->
Inflow

<!-- b001242 | prose | pages [33] -->
Air

<!-- b001243 | prose | pages [33] -->
average

<!-- b001244 | prose | pages [33] -->
maximum

<!-- b001245 | prose | pages [33] -->
minimum

<!-- b001246 | prose | pages [33] -->
flux(W)

<!-- b001247 | prose | pages [33] -->
(m/s)

<!-- b001248 | prose | pages [33] -->
Temp(K)

<!-- b001249 | prose | pages [33] -->
Temp(K)

<!-- b001250 | prose | pages [33] -->
Temp(K)

<!-- b001251 | prose | pages [33] -->
Temp(K)

<!-- b001252 | prose | pages [33] -->
Temp(K)

<!-- b001253 | prose | pages [33] -->
1.7287 0.02 318 294 312.5041 318.029 311.9438 1.5847 0.02 318 296 312.9596 318.026 312.4485 1.5652 0.02 318 298 313.4178 318.024 312.9532 1.2966 0.02 318 300 313.8762 318.022 313.4579 1.1525 0.02 318 302

<!-- b001254 | prose | pages [33] -->
Table

<!-- b001255 | furniture | pages [33] -->


<!-- b001256 | prose | pages [33] -->
314.3342 318.091 313.9625

<!-- b001257 | furniture | pages [34] -->
Team #48649                                                              Page 33 of 44

<!-- b001258 | prose | pages [34] -->
Volume Temperature-Air Temperature graph 319

<!-- b001259 | prose | pages [34] -->
318

<!-- b001260 | prose | pages [34] -->
317

<!-- b001261 | prose | pages [34] -->
Volume Temperature/K

<!-- b001262 | prose | pages [34] -->
316

<!-- b001263 | prose | pages [34] -->
315

<!-- b001264 | prose | pages [34] -->
314

<!-- b001265 | prose | pages [34] -->
313

<!-- b001266 | prose | pages [34] -->
312

<!-- b001267 | prose | pages [34] -->
311

<!-- b001268 | furniture | pages [34] -->


<!-- b001269 | prose | pages [34] -->
294 295 296 297

<!-- b001270 | furniture | pages [34] -->


<!-- b001271 | prose | pages [34] -->
Volume-average Temp Volume-maximum Temp Volume-minimum Temp

<!-- b001272 | prose | pages [34] -->
298 299 300 301 302

<!-- b001273 | prose | pages [34] -->
Air Temperature/K

<!-- b001274 | furniture | pages [34] -->


<!-- b001275 | prose | pages [34] -->
Graph 21: Volume Temperature - Air Temperature graph

<!-- b001276 | furniture | pages [34] -->


<!-- b001277 | furniture | pages [34] -->


<!-- b001278 | furniture | pages [34] -->


<!-- b001279 | furniture | pages [34] -->


<!-- b001280 | furniture | pages [34] -->


<!-- b001281 | furniture | pages [34] -->


<!-- b001282 | furniture | pages [34] -->


<!-- b001283 | furniture | pages [34] -->


<!-- b001284 | prose | pages [34] -->
Average top surface heat flux-Air Temperature graph 1.9

<!-- b001285 | prose | pages [34] -->
1.8

<!-- b001286 | prose | pages [34] -->
1.7

<!-- b001287 | prose | pages [34] -->
1.6

<!-- b001288 | prose | pages [34] -->
heat flux/W

<!-- b001289 | prose | pages [34] -->
1.5

<!-- b001290 | prose | pages [34] -->
1.4

<!-- b001291 | prose | pages [34] -->
1.3

<!-- b001292 | prose | pages [34] -->
1.2

<!-- b001293 | prose | pages [34] -->
1.1 294 295 296 297 298 299 300 301 302

<!-- b001294 | prose | pages [34] -->
Air Temperature/K

<!-- b001295 | furniture | pages [34] -->


<!-- b001296 | prose | pages [34] -->
Graph 22: Average top surface heat - Air Temperature graph

<!-- b001297 | furniture | pages [34] -->


<!-- b001298 | prose | pages [34] -->
From Table 11 and the corresponding graph we can notice that: the average top surface heat

<!-- b001299 | prose | pages [34] -->
flux has negative correlation with air temperature. When the air gets warmer, the heat lass becomes small is realistic and that just indicates why we need bath heater in our bathroom to

<!-- b001300 | furniture | pages [34] -->


<!-- b001301 | furniture | pages [35] -->
Team #48649                                                              Page 34 of 44

<!-- b001302 | prose | pages [35] -->
avoid us from getting cold. The volume-average temperature and volume-minimum temperature have positive correlation with air temperature, and the raising rate goes down as the inflow velocity goes up. It is corresponding to our common sense that once the heat loss gets smaller, the remaining water gets warmer which follows energy conservation law.

<!-- b001303 | heading | pages [35] -->
6.1.4 Conclusion

<!-- b001304 | prose | pages [35] -->
From all above we also notice that, all the parameters that have noticeable effect on the bathtub water temperature lead us to a better strategy. Combination of all the parameter will give us a great environment for bath. Also, it is happy to find that changing the parameter in

<!-- b001305 | prose | pages [35] -->
a reasonable range will not do great harm to the final result, and the heating system is stable under most circumstances.

<!-- b001306 | furniture | pages [35] -->


<!-- b001307 | furniture | pages [35] -->


<!-- b001308 | heading | pages [35] -->
6.2 Sensitivity analysis for BWP

<!-- b001309 | prose | pages [35] -->
In the BWP model, the required hot flow is right corresponding to the total heat loss. As a result, we can research this criteria by observing the temperature-variation curve of the bathtub

<!-- b001310 | prose | pages [35] -->
water. After finishing building the model with some fixed parameters, we look back to consider some more condition: different surface area of the bathtub, different volume of the bathtub, different material of the bathtub and different volume of person in the bathtub. Then we analyze the result below.

<!-- b001311 | furniture | pages [35] -->


<!-- b001312 | furniture | pages [36] -->
Team #48649                                                              Page 35 of 44

<!-- b001313 | heading | pages [36] -->
6.2.1 Different surface area of the bathtub

<!-- b001314 | prose | pages [36] -->
Temperature curve with different surface area of the bathtub 318

<!-- b001315 | prose | pages [36] -->
316

<!-- b001316 | prose | pages [36] -->
314

<!-- b001317 | prose | pages [36] -->
312

<!-- b001318 | prose | pages [36] -->
Temperature/K

<!-- b001319 | prose | pages [36] -->
310

<!-- b001320 | prose | pages [36] -->
308

<!-- b001321 | prose | pages [36] -->
306

<!-- b001322 | prose | pages [36] -->
304

<!-- b001323 | prose | pages [36] -->
302

<!-- b001324 | prose | pages [36] -->
300

<!-- b001325 | furniture | pages [36] -->


<!-- b001326 | prose | pages [36] -->
0 100 200 300 400

<!-- b001327 | furniture | pages [36] -->


<!-- b001328 | prose | pages [36] -->
s=1.4m2

<!-- b001329 | prose | pages [36] -->
s=1.5m2

<!-- b001330 | prose | pages [36] -->
s=1.53m2

<!-- b001331 | prose | pages [36] -->
s=1.6m2

<!-- b001332 | prose | pages [36] -->
s=1.7m2

<!-- b001333 | prose | pages [36] -->
500 600 700 800 900 1000

<!-- b001334 | prose | pages [36] -->
Time/min

<!-- b001335 | furniture | pages [36] -->


<!-- b001336 | prose | pages [36] -->
Graph 23: Temperature curve with different surface area of the bathtub We try 5 different surface areas of the bathtub, and change the corresponding volume. Then we get the temperature-variation curve by simulating them all. From Graph 23 we can easily find that: the surface area of the bathtub have very small effect on the total heat loss. The model is stable with the surface area of the bathtub.

<!-- b001337 | prose | pages [36] -->
It is reasonable to get this result because both in our model and in the real world, heat loss by the bathtub is much smaller than that by air-water convention.

<!-- b001338 | furniture | pages [36] -->


<!-- b001339 | furniture | pages [36] -->


<!-- b001340 | furniture | pages [37] -->
Team #48649                                                              Page 36 of 44

<!-- b001341 | heading | pages [37] -->
6.2.2 Different volume of the bathtub

<!-- b001342 | prose | pages [37] -->
Temperature curve with different volume of the bathtub 318

<!-- b001343 | prose | pages [37] -->
316

<!-- b001344 | prose | pages [37] -->
314

<!-- b001345 | prose | pages [37] -->
312

<!-- b001346 | prose | pages [37] -->
Temperature/K

<!-- b001347 | prose | pages [37] -->
310

<!-- b001348 | prose | pages [37] -->
308

<!-- b001349 | prose | pages [37] -->
306

<!-- b001350 | prose | pages [37] -->
304

<!-- b001351 | prose | pages [37] -->
302

<!-- b001352 | prose | pages [37] -->
300

<!-- b001353 | prose | pages [37] -->
298

<!-- b001354 | furniture | pages [37] -->


<!-- b001355 | prose | pages [37] -->
0 100 200 300 400

<!-- b001356 | furniture | pages [37] -->


<!-- b001357 | prose | pages [37] -->
V=230L V=270L V=300L V=320L V=350L

<!-- b001358 | prose | pages [37] -->
500 600 700 800 900 1000

<!-- b001359 | prose | pages [37] -->
Time/min

<!-- b001360 | furniture | pages [37] -->


<!-- b001361 | prose | pages [37] -->
Graph 24: Temperature curve with different volume area of the bathtub

<!-- b001362 | furniture | pages [37] -->


<!-- b001363 | furniture | pages [37] -->


<!-- b001364 | prose | pages [37] -->
We try 5 different volume of the bathtub, and change the corresponding surface areas. Then we get the temperature-variation curve by simulating them all. From Graph 24 we can easily find that: compared with the surface area of the bathtub, the velocity have larger effect on the total heat loss. But after 10 hours the largest variation can just around 4K. The larger the volume, the slower the heat loss.

<!-- b001365 | prose | pages [37] -->
This result can be easily understood that: the volume of the bathtub (in this paper, the volume can also be regarded as the cubage) represents the volume of water. It is a common sense that a large amount of water refrigerate slow, and here it is also the case.

<!-- b001366 | furniture | pages [37] -->


<!-- b001367 | furniture | pages [37] -->


<!-- b001368 | furniture | pages [38] -->
Team #48649                                                              Page 37 of 44

<!-- b001369 | heading | pages [38] -->
6.2.3 Different material of the bathtub

<!-- b001370 | prose | pages [38] -->
Temperature curve with different material of the bathtub 318

<!-- b001371 | prose | pages [38] -->
316

<!-- b001372 | prose | pages [38] -->
314

<!-- b001373 | prose | pages [38] -->
312

<!-- b001374 | prose | pages [38] -->
Temperature/K

<!-- b001375 | prose | pages [38] -->
310

<!-- b001376 | prose | pages [38] -->
308

<!-- b001377 | prose | pages [38] -->
306

<!-- b001378 | prose | pages [38] -->
304

<!-- b001379 | prose | pages [38] -->
302

<!-- b001380 | prose | pages [38] -->
300

<!-- b001381 | furniture | pages [38] -->


<!-- b001382 | prose | pages [38] -->
0 100 200 300 400

<!-- b001383 | furniture | pages [38] -->


<!-- b001384 | prose | pages [38] -->
cast iron λ=42 acrylic λ=1.4 steel λ=36 porcelain λ=0.87 wood λ=0.38

<!-- b001385 | prose | pages [38] -->
500 600 700 800 900 1000

<!-- b001386 | prose | pages [38] -->
Time/min

<!-- b001387 | furniture | pages [38] -->


<!-- b001388 | prose | pages [38] -->
Graph 25: Temperature curve with different material of the bathtub

<!-- b001389 | furniture | pages [38] -->


<!-- b001390 | furniture | pages [38] -->


<!-- b001391 | prose | pages [38] -->
We try 5 different material of the bathtub. Then we get the temperature-variation curve by simulating them all. From Graph 25 we can easily find that: the material of the bathtub have very small effect on the total heat loss. The model is stable with the material of the bathtub.

<!-- b001392 | prose | pages [38] -->
It is because of the same reason as the surface area of the bathtub that heat loss by the bathtub is much smaller than that by air-water convention.

<!-- b001393 | furniture | pages [38] -->


<!-- b001394 | furniture | pages [38] -->


<!-- b001395 | furniture | pages [39] -->
Team #48649                                                              Page 38 of 44

<!-- b001396 | heading | pages [39] -->
6.2.4 Different volume of person in the bathtub

<!-- b001397 | prose | pages [39] -->
Temperature curve with different volume of person 318

<!-- b001398 | prose | pages [39] -->
316

<!-- b001399 | prose | pages [39] -->
314

<!-- b001400 | prose | pages [39] -->
312

<!-- b001401 | prose | pages [39] -->
Temperature/K

<!-- b001402 | prose | pages [39] -->
310

<!-- b001403 | prose | pages [39] -->
308

<!-- b001404 | prose | pages [39] -->
306

<!-- b001405 | prose | pages [39] -->
304

<!-- b001406 | prose | pages [39] -->
302

<!-- b001407 | prose | pages [39] -->
300

<!-- b001408 | furniture | pages [39] -->


<!-- b001409 | prose | pages [39] -->
0 100 200 300 400

<!-- b001410 | furniture | pages [39] -->


<!-- b001411 | prose | pages [39] -->
V=30L V=40L V=50L V=60L V=75L

<!-- b001412 | prose | pages [39] -->
500 600 700 800 900 1000

<!-- b001413 | prose | pages [39] -->
Time/min

<!-- b001414 | furniture | pages [39] -->


<!-- b001415 | prose | pages [39] -->
Graph 26: Temperature curve with different volume of person

<!-- b001416 | furniture | pages [39] -->


<!-- b001417 | furniture | pages [39] -->


<!-- b001418 | prose | pages [39] -->
We try 5 different volume of the people in the bathtub. Then we get the temperature- variation curve by simulating them all. From Graph 26 we can easily find that: the material of the bathtub have larger effect on the total heat loss than the surface or the material of the bathtub. But is holds smaller effect than that of the volume of the bathtub. The larger the volume, the faster the heat loss is.

<!-- b001419 | prose | pages [39] -->
It is because of the same reason as the volume of the bathtub that a large amount of water refrigerate slow, and here the difference between volume of bathtub and that of people is just the volume of water.

<!-- b001420 | furniture | pages [39] -->


<!-- b001421 | heading | pages [39] -->
6.2.5 Conclusion

<!-- b001422 | prose | pages [39] -->
As we consider various different conditions and analyze the result we can conclude that:

<!-- b001423 | furniture | pages [39] -->


<!-- b001424 | prose | pages [39] -->
 The system under this model is fairly stable with different variables.  The volume of water is particularly an important influential factor on the heat loss.

<!-- b001425 | furniture | pages [39] -->


<!-- b001426 | prose | pages [39] -->
This tells us that, with the bathtub volume fixed, we can give fairly stable evaluation on the system and also the best strategy for the user to enjoy their bath experience.

<!-- b001427 | furniture | pages [39] -->


<!-- b001428 | furniture | pages [40] -->
Team #48649                                                              Page 39 of 44

<!-- b001429 | heading | pages [40] -->
7 Model for Cleansing with a Bubble Bath Additive (CBBA model)

<!-- b001430 | prose | pages [40] -->
If the person used a bubble bath additive while initially filling the bathtub to assist in cleansing, then the heat dissipation through the water and the air will be influenced by the bubble layer. Thus we expand the CBBA model based on BWP model. As Graph 27 shows, we modeled the bubble layer as a kind of porous medium that locates between the water surface and the air.

<!-- b001431 | furniture | pages [40] -->


<!-- b001432 | prose | pages [40] -->
Graph 27: The diagram of the bubble layer

<!-- b001433 | prose | pages [40] -->
 The medium has a different heat transfer coefficient . The heat transfer process between bub

<!-- b001434 | prose | pages [40] -->
the water and the air through the air can be modeled as a heat conduction process. The heat conduction:

<!-- b001435 | prose | pages [40] -->
  Q A

<!-- b001436 | prose | pages [40] -->
bub bub bub

<!-- b001437 | prose | pages [40] -->
Q

<!-- b001438 | prose | pages [40] -->
 t t t

<!-- b001439 | prose | pages [40] -->
water bub

<!-- b001440 | prose | pages [40] -->
(7.1) d

<!-- b001441 | prose | pages [40] -->
bub

<!-- b001442 | prose | pages [40] -->
: Heat loss through the water surface by the bubble layer in unit time bub

<!-- b001443 | prose | pages [40] -->
A sA . : The surface area of the bubble layer, which should be equal to the water surface bub

<!-- b001444 | prose | pages [40] -->
t t : The upper surface temperature of the bubble layer, which can be equal to air bub

<!-- b001445 | prose | pages [40] -->
d : The thickness of the bubble layer. bub

<!-- b001446 | prose | pages [40] -->
 We change the heat transfer coefficient

<!-- b001447 | prose | pages [40] -->
cooling process as Graph 28 shows:

<!-- b001448 | furniture | pages [40] -->


<!-- b001449 | prose | pages [40] -->
.

<!-- b001450 | prose | pages [40] -->
and get the total heat dissipation in natural bub bub

<!-- b001451 | furniture | pages [41] -->
Team #48649                                                              Page 40 of 44

<!-- b001452 | prose | pages [41] -->
Temperature curve of bubble model 318

<!-- b001453 | prose | pages [41] -->
316

<!-- b001454 | prose | pages [41] -->
314

<!-- b001455 | prose | pages [41] -->
312

<!-- b001456 | prose | pages [41] -->
Temperature/K

<!-- b001457 | prose | pages [41] -->
310

<!-- b001458 | prose | pages [41] -->
308

<!-- b001459 | prose | pages [41] -->
306

<!-- b001460 | prose | pages [41] -->
304

<!-- b001461 | prose | pages [41] -->
302

<!-- b001462 | prose | pages [41] -->
300

<!-- b001463 | furniture | pages [41] -->


<!-- b001464 | prose | pages [41] -->
0 100 200 300 400

<!-- b001465 | furniture | pages [41] -->


<!-- b001466 | prose | pages [41] -->
λ=0.5 λ=0.7 λ=1

<!-- b001467 | prose | pages [41] -->
500 600 700 800 900 1000

<!-- b001468 | prose | pages [41] -->
Time/min

<!-- b001469 | furniture | pages [41] -->


<!-- b001470 | prose | pages [41] -->
 Graph 28: Temperature curve of bubble model with different heat transfer coefficient

<!-- b001471 | furniture | pages [41] -->


<!-- b001472 | prose | pages [41] -->
bub

<!-- b001473 | prose | pages [41] -->
From the graph we can see the heat dissipation becomes slower with the bubble layer on

<!-- b001474 | prose | pages [41] -->
 the surface of the water. It is also clear that the dissipation rate becomes high as goes bub

<!-- b001475 | prose | pages [41] -->
up. In other words, the bubble layer can be regarded as a thermal insulation layer.

<!-- b001476 | heading | pages [41] -->
8 Weakness and Strength

<!-- b001477 | prose | pages [41] -->
Like any model, our model has its own strengths and weaknesses. Some of major points are presented below.

<!-- b001478 | heading | pages [41] -->
8.1 Strengths

<!-- b001479 | prose | pages [41] -->
 BWOP simulation using FEM by ANSYS returns very specific temperature distribution.

<!-- b001480 | prose | pages [41] -->
Our BWOP model use FEM by ANSYS to simulate the 3-D flow field heat convection. Instead just working out some boundary formulas to get a theoretical result, ANSYS provides strong function to simulate the heat conduction between many finite elements. The result presents a clear temperature distribution with isothermal diagram and the statistical data. It can not only show us the temporary temperature of the water but to show the gradient visually. Even in BWP model, we use this method to simulate the temperature distribution across people’s body surface.

<!-- b001481 | furniture | pages [41] -->


<!-- b001482 | furniture | pages [41] -->


<!-- b001483 | prose | pages [41] -->
 Simplification of complexed thermal system by BWP model.

<!-- b001484 | prose | pages [41] -->
The temperature of the water in bathtub can be simulated statically, however, if someone

<!-- b001485 | furniture | pages [41] -->


<!-- b001486 | furniture | pages [42] -->
Team #48649                                                              Page 41 of 44

<!-- b001487 | prose | pages [42] -->
is in the bathtub, then the system becomes abstrusely complexed to solve. Considering people’s motility, which is both a bad and a great condition, we can simplify the water model to a homogeneous body where temperature is the same everywhere. Using this simplification we can do many simulation and calculations. Due to people’s motility, this assumption is reasonable.  Offering discrete inflow model to reach a more realistic and operable result.

<!-- b001488 | prose | pages [42] -->
Apart adding from a constant trickle of hot water, we propose anther discrete strategy to adjust the temperature. As is always the case, people can’t control the inflow velocity precisely. Then the discrete approach offers users with a lazy and operable strategy. According to our experiment, the discrete approach can also make the water waste less.

<!-- b001489 | heading | pages [42] -->
8.2 Weaknesses

<!-- b001490 | prose | pages [42] -->
 Some assumptions are not accurate enough.

<!-- b001491 | prose | pages [42] -->
 The 3th assumption tells that the volume of the air is infinite and the temperature of

<!-- b001492 | prose | pages [42] -->
the air keeps constant. But in a bathroom in real world, air close to the surface of hot water must have higher temperature, and that difference have an influence on the heat convection between water and air.  The 4th assumption tells that the temperature can be evenly distributed in bathtub at

<!-- b001493 | prose | pages [42] -->
any time when a person is in it. It is a great way to take this condition as an assumption to simplify the model. But is inevitably decrease the precision of the model. Different temperature attributions leads to different heat convections and also different final result.  The 5th assumption tells that there doesn’t exist heat convection in the water when a

<!-- b001494 | prose | pages [42] -->
person is in the bathtub (BWP model). It is also a great way to take this condition as an assumption to simplify the model. But this assumption changes the heat convection to heat conduction. Some deviation must appear in this process.

<!-- b001495 | furniture | pages [42] -->


<!-- b001496 | furniture | pages [42] -->


<!-- b001497 | furniture | pages [42] -->


<!-- b001498 | furniture | pages [42] -->


<!-- b001499 | furniture | pages [42] -->


<!-- b001500 | furniture | pages [42] -->


<!-- b001501 | furniture | pages [42] -->


<!-- b001502 | furniture | pages [42] -->


<!-- b001503 | furniture | pages [42] -->


<!-- b001504 | furniture | pages [42] -->


<!-- b001505 | furniture | pages [42] -->


<!-- b001506 | furniture | pages [43] -->
Team #48649                                                              Page 42 of 44

<!-- b001507 | heading | pages [43] -->
References

<!-- b001508 | references | pages [43] -->
[1]Gray, D.D., and Giorgin, A., The Validity of the Boussinesqe Approximation for Liquids and Gases

<!-- b001509 | references | pages [43] -->
[M], Int.J.Heat Mass Transfer, 1976, 19: 545-551

<!-- b001510 | references | pages [43] -->
[2]http://www.biocab.org/Heat_Transfer.html

<!-- b001511 | references | pages [43] -->
[3]https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_constant

<!-- b001512 | references | pages [43] -->
[4]http://a.hiphotos.baidu.com/zhidao/pic/item/8ad4b31c8701a18b5f381c2c9f2f07082938fe86.jpg?q

<!-- b001513 | references | pages [43] -->
q-pf-to=pcqq.c2c

<!-- b001514 | references | pages [43] -->
[5]https://en.wikipedia.org/wiki/Prandtl_number

<!-- b001515 | references | pages [43] -->
[6]https://en.wikipedia.org/wiki/Heat_transfer#cite_note-15

<!-- b001516 | references | pages [43] -->
[7]https://en.wikipedia.org/wiki/Finite_element_method

<!-- b001517 | references | pages [43] -->
[8]https://en.wikipedia.org/wiki/Ansys#ANSYS_CFD.2C_CFX

<!-- b001518 | heading | pages [43] -->
[9]Abbott, J.M. Smith, H.C. Van Ness, M.M. (2005). Introduction to chemical engineering

<!-- b001519 | prose | pages [43] -->
thermodynamics (7th ed.). Boston ; Montreal: McGraw-Hill. ISBN 0-07-310445-0 [10]J.P.Holman，Heat Transfer 1990 ISBN-13: 978-0079093882

<!-- b001520 | furniture | pages [43] -->


<!-- b001521 | furniture | pages [43] -->


<!-- b001522 | furniture | pages [43] -->


<!-- b001523 | furniture | pages [43] -->


<!-- b001524 | furniture | pages [43] -->


<!-- b001525 | furniture | pages [43] -->


<!-- b001526 | furniture | pages [43] -->


<!-- b001527 | furniture | pages [43] -->


<!-- b001528 | furniture | pages [43] -->


<!-- b001529 | furniture | pages [43] -->


<!-- b001530 | furniture | pages [43] -->


<!-- b001531 | furniture | pages [43] -->


<!-- b001532 | furniture | pages [43] -->


<!-- b001533 | furniture | pages [43] -->


<!-- b001534 | furniture | pages [43] -->


<!-- b001535 | furniture | pages [43] -->


<!-- b001536 | furniture | pages [43] -->


<!-- b001537 | furniture | pages [43] -->


<!-- b001538 | furniture | pages [43] -->


<!-- b001539 | furniture | pages [43] -->


<!-- b001540 | furniture | pages [43] -->


<!-- b001541 | furniture | pages [43] -->


<!-- b001542 | furniture | pages [43] -->


<!-- b001543 | furniture | pages [43] -->


<!-- b001544 | furniture | pages [43] -->


<!-- b001545 | furniture | pages [43] -->


<!-- b001546 | furniture | pages [43] -->


<!-- b001547 | furniture | pages [44] -->
Team #48649                                                              Page 43 of 44

<!-- b001548 | heading | pages [44] -->
Appendix

<!-- b001549 | prose | pages [44] -->
Enjoying Making Your Own Spa-type Bathtub

<!-- b001550 | prose | pages [44] -->
To all interested users

<!-- b001551 | furniture | pages [44] -->


<!-- b001552 | furniture | pages [44] -->


<!-- b001553 | furniture | pages [44] -->


<!-- b001554 | prose | pages [44] -->
Have you ever suffered from the cooling water as you are enjoying the bath?

<!-- b001555 | furniture | pages [44] -->


<!-- b001556 | furniture | pages [44] -->


<!-- b001557 | furniture | pages [44] -->


<!-- b001558 | prose | pages [44] -->
Have you ever dreamed about owning you own spa-type bathtub?

<!-- b001559 | furniture | pages [44] -->


<!-- b001560 | furniture | pages [44] -->


<!-- b001561 | prose | pages [44] -->
That is not a dream now! Taking several simple steps to make you own it now! At first, find a pipe to draw hot water from faucet to the bottom of the bathtub which is opposite to the overflow drain. It is well recommended to be the bottom to maximize the utilization of your hot water (that is the best way to reduce the heat loss). During your enjoyment, you’ve get two different way to get your suitable temperature.

<!-- b001562 | furniture | pages [44] -->


<!-- b001563 | prose | pages [44] -->
Strategy 1: If you want to have a sound sleep while enjoying your bath, then you’d better choose this strategy. Take a relatively long time to adapt your bathtub to our model, then you will get exact inflow per second for a given temperature (don’t worry about the complexity,

<!-- b001564 | prose | pages [44] -->
you will just need to do this for ONE time). Set your faucet to get the given flow velocity (this step may be a little bit hard), then you may enjoy your sound sleep in warm water.

<!-- b001565 | prose | pages [44] -->
Strategy 2: If you feel troublesome to adapt to the model or you just don’t want to set the faucet precisely every time, it is OK for strategy 2. In this way, you don’t even need to know any parameter about your own bathtub and your faucet. Adjusting the faucet to guarantee the water from which will not be too hot to bear. Then maximize the flow until the bathtub get a little bit hot. Stop the faucet and enjoy your bath for a period of time until you feel a little bit cold. Repeat the operations and you can easily enjoy your bathing time.

<!-- b001566 | furniture | pages [44] -->


<!-- b001567 | prose | pages [44] -->
Note 1: You may have to serious on the temperature of water from the faucet just to avoid scald. For Strategy 1, you’d better choose a temperature that you won’t feel very hot to keep your bathtub warm, or you may suffer from the hottest region during your sleep. For Strategy 2, it is OK to choose a higher temperature in order to reheat your bathtub fast, but you have to agitate the water rapidly to make the temperature distribute evenly.

<!-- b001568 | prose | pages [44] -->
Note 2: Pay attention to the temperature distribution if you want to stay still to recover from fatigue. The water somewhere mat not be warm as you think such that the hottest region must be around the pipe and the top surface of the water is commonly relatively cold. It takes time for heat to transfer from hot water to cold water, and during this period of time, the air

<!-- b001569 | prose | pages [44] -->
cools the top surface. So it is really hard for our strategy to keep an evenly maintained temperature. You may just twist for a while to get them mixed to solve the problem. Be sure to remember this.

<!-- b001570 | furniture | pages [44] -->

