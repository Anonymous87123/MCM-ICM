# P-A-2016-48649-e4d30266

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only 48649 T1 ________________ F1 ________________

<!-- b000003 | front_matter | pages [1] -->
T2 ________________ F2 ________________

<!-- b000004 | front_matter | pages [1] -->
T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________ A

<!-- b000005 | front_matter | pages [1] -->
2016

<!-- b000006 | prose | pages [1] -->
MCM/ICM

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Based on the existing Finite Element Method (FEM) technique, we consider two models to analyze the temperature distribution in the bathtub, including without and with a person in it. Then, we build two inflow models, namely, the continuous inflow model and the discontinuous inflow model. At last, we employ Fuzzy Comprehensive Evaluation (FCE) to evaluate these two inflow models in order to find an optimal solution.

<!-- b000010 | prose | pages [1] -->
First, regarding the model without a person in the bathtub, we calculate the heat dissipation in the water-to-air heat convection and build a hot-water tube model for calculating the heat addition. What’s more, to find the temperature distribution in the bathtub, we simulate such model on ANSYS, which is a large-scale common finite element software.

<!-- b000011 | prose | pages [1] -->
Second, we consider the model with a person in the bathtub from two aspects, namely, the person in the still and the moving states. Specific to the moving state of person, we find that there exist two ways of dissipating heat, including the water-to-air heat convection and the water-to-bathtub heat conduction. Furthermore, we exploit MATLAB to find the temperature curve in natural cooling process. .

<!-- b000012 | prose | pages [1] -->
Third, based on the analysis of above two conditions, we propose to simulate on the continuous and discontinuous inflow models of the hot water. Besides, to find an optimal strategy, we evaluate these two models using fuzzy comprehensive evaluation (FCE), where the variables include the amount of needed water, the comfortable degree of user, the operation complexity and the operative difficulty index.

<!-- b000013 | prose | pages [1] -->
Fourth, to analyze the sensitivity of two models with and without person, we extensively change the velocity and the temperature of the hot inflow, the air temperature, the surface area, volume and material of the bathtub, and the volume of the person body.

<!-- b000014 | prose | pages [1] -->
At last, we further study the model for cleansing with a bubble bath additive. In this case, we vary the condition of the bubble to observe this model’s performance.

<!-- b000015 | furniture | pages [2] -->
Team #48649

<!-- b000016 | furniture | pages [2] -->
Page 1 of 44

<!-- b000017 | furniture | pages [2] -->
Team #48649

<!-- b000018 | prose | pages [2] -->
January 28，2014

<!-- b000019 | heading | pages [2] -->
Abstract

<!-- b000020 | prose | pages [2] -->
Naturally a non-spa-style bathtub without a secondary heating system and circulating jet will get noticeably cooler after being filled with hot water. The water lose heat both to the air and to the bathtub. One want to keep warm by adding a constant trickle of hot water from the faucet. To handle fluid’s overflowing, the bathtub is designed in such a way that when the tub reached its capacity, excess water escapes through an overflow drain.

<!-- b000021 | prose | pages [2] -->
We build Bathtub without Person model (BWOP) to simulate the water temperature distribution without people inside, and Bathtub with Person (BWP) model to research the natural cooling process and to propose reasonable strategy for user to maintain the temperature. The simulation of BWOP mainly depends on the finite element method (FEM) using ANSYS, while the simulation of BWP mainly depends on the solving of the thermodynamic equation using MATLAB.

<!-- b000022 | keywords | pages [2] -->
Keywords: Heat Convection, Heat Conduction, Finite Element Method, ANSYS

<!-- b000023 | furniture | pages [3] -->
Team #48649

<!-- b000024 | furniture | pages [3] -->
Page 2 of 44

<!-- b000025 | heading | pages [3] -->
Contents

<!-- b000026 | contents | pages [3] -->
1 Introduction ........................................................................................................................... 4

<!-- b000027 | contents | pages [3] -->
1.1 Restatement of the Problem ........................................................................................................ 4

<!-- b000028 | contents | pages [3] -->
2 Assumptions and Justifications ............................................................................................. 4

<!-- b000029 | contents | pages [3] -->
3 Notations ............................................................................................................................... 5

<!-- b000030 | contents | pages [3] -->
4 Model for bathtub without a person in it (BWOP model) .................................................... 6

<!-- b000031 | contents | pages [3] -->
4.1 The calculation of the heat-transfer coefficient .......................................................................... 8

<!-- b000032 | contents | pages [3] -->
4.1.1 The heat-transfer coefficient between the water surface and the air .................................... 8

<!-- b000033 | contents | pages [3] -->
4.1.2 The heat-transfer coefficient between the water and the water tube .................................... 9

<!-- b000034 | contents | pages [3] -->
4.1.3 The heat-transfer coefficient between the hot water and the cube wall ............................. 10

<!-- b000035 | contents | pages [3] -->
4.2 The heat dissipation between the water surface and the air ...................................................... 11

<!-- b000036 | contents | pages [3] -->
4.3 The heat addition between the water and the hot water tube .................................................... 11

<!-- b000037 | contents | pages [3] -->
4.3.1 The heat exchange between the inside and the outside of the tube .................................... 11

<!-- b000038 | contents | pages [3] -->
4.3.2 The heat exchange between the water and the water tube ................................................. 12

<!-- b000039 | contents | pages [3] -->
4.4 Simulation of BWOP model based on ANSYS ........................................................................ 14

<!-- b000040 | contents | pages [3] -->
5 Model for bathtub with a person in it (BWP model) .......................................................... 17

<!-- b000041 | contents | pages [3] -->
5.1 Simulation of the temperature distribution if the person is still ................................................ 18

<!-- b000042 | contents | pages [3] -->
5.2 Heat dissipation in BWP model ................................................................................................ 19

<!-- b000043 | contents | pages [3] -->
5.2.1 Water-Air heat convection ................................................................................................. 19

<!-- b000044 | contents | pages [3] -->
5.2.2 Water-Bathtub heat conduction ......................................................................................... 20

<!-- b000045 | contents | pages [3] -->
5.2.3 The total heat dissipation in the bathtub ............................................................................ 21

<!-- b000046 | contents | pages [3] -->
5.3 Simulation of BWP model with MATLAB .............................................................................. 21

<!-- b000047 | contents | pages [3] -->
5.4 Heat addition model .................................................................................................................. 23

<!-- b000048 | contents | pages [3] -->
5.4.1 Continuous Inflow model (CI model) ................................................................................ 24

<!-- b000049 | contents | pages [3] -->
5.4.2 Discontinuous Inflow model (DCI model) ........................................................................ 26

<!-- b000050 | contents | pages [3] -->
5.4.3 FCE of the two models ...................................................................................................... 28

<!-- b000051 | contents | pages [3] -->
6 Sensitivity analysis.............................................................................................................. 29

<!-- b000052 | contents | pages [3] -->
6.1 Sensitivity analysis for BWOP ................................................................................................. 29

<!-- b000053 | contents | pages [3] -->
6.1.1 Inflow Velocity .................................................................................................................. 29

<!-- b000054 | contents | pages [3] -->
6.1.2 Inflow Temperature ........................................................................................................... 31

<!-- b000055 | contents | pages [3] -->
6.1.3 Air Temperature ................................................................................................................. 32

<!-- b000056 | furniture | pages [4] -->
Team #48649                                                              Page 3 of 44

<!-- b000057 | contents | pages [4] -->
6.1.4 Conclusion ......................................................................................................................... 34

<!-- b000058 | contents | pages [4] -->
6.2 Sensitivity analysis for BWP .................................................................................................... 34

<!-- b000059 | contents | pages [4] -->
6.2.1 Different surface area of the bathtub ................................................................................. 35

<!-- b000060 | contents | pages [4] -->
6.2.2 Different volume of the bathtub ......................................................................................... 36

<!-- b000061 | contents | pages [4] -->
6.2.3 Different material of the bathtub ........................................................................................ 37

<!-- b000062 | contents | pages [4] -->
6.2.4 Different volume of person in the bathtub ......................................................................... 38

<!-- b000063 | contents | pages [4] -->
6.2.5 Conclusion ......................................................................................................................... 38

<!-- b000064 | contents | pages [4] -->
7 Model for Cleansing with a Bubble Bath Additive (CBBA model) ................................... 39

<!-- b000065 | contents | pages [4] -->
8 Weakness and Strength ....................................................................................................... 40

<!-- b000066 | contents | pages [4] -->
8.1 Strengths ................................................................................................................................... 40

<!-- b000067 | contents | pages [4] -->
8.2 Weaknesses ............................................................................................................................... 41

<!-- b000068 | contents | pages [4] -->
References .............................................................................................................................. 42

<!-- b000069 | contents | pages [4] -->
Appendix ................................................................................................................................ 43

<!-- b000070 | furniture | pages [5] -->
Team #48649                                                              Page 4 of 44

<!-- b000071 | heading | pages [5] -->
1 Introduction

<!-- b000072 | heading | pages [5] -->
1.1 Restatement of the Problem

<!-- b000073 | prose | pages [5] -->
We are required to model the bathtub water’s temperature in space and time, which enables an individual to pick the best strategy in order to keep the temperature almost a constant in the bathtub. Besides, the temperature at any time is required to approach the initial state without wasting too much water.

<!-- b000074 | prose | pages [5] -->
By analysis, we proposed to decompose the problem into two sub-problems:

<!-- b000075 | prose | pages [5] -->
 Build a model that can simulate the temperature of the bathtub in space and time.  Propose an optimal strategy. The strategy should satisfy two conditions: waste the least water and let the user feel comfortable.

<!-- b000076 | prose | pages [5] -->
First, for generality, we set the velocity and temperature of inflow, the size and shape of bathtub variables. Then, we try to model the temperature inside. On one hand, the model needs to show the volume-average temperature. On the other hand, it is required to depict the distribution under the influence of heat loss and addition. Then we can change the inputs to do several simulations. Only using many simulation results can we build a relationship between input and output of the complexed thermodynamical system.

<!-- b000077 | prose | pages [5] -->
Second we seek to use the relationship getting from our simulation to find the best strategy for keeping the temperature. In our model, “best” doesn’t not only means “the least water” but “the most comfortable environment for the people” which put weight on the gradient of temperature and limit on the degree (to avoid scald).

<!-- b000078 | prose | pages [5] -->
At last, we try to adjust our model to different initial state such as the bathtub size and shape, the inflow temperature and the motions made by the people. We also take the bubble bath additive in to consideration.

<!-- b000079 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000080 | prose | pages [5] -->
1) Water is stability, incompressible viscous liquid. The compressibility of the water is small enough to be ignored. The water is steady and viscous in cases that we will discuss later.

<!-- b000081 | heading | pages [5] -->
2) The fluid matches the Boussinesq assumptions[1].

<!-- b000082 | prose | pages [5] -->
 The fluid viscous dissipation can be ignored.

<!-- b000083 | prose | pages [5] -->
 All the physical properties except density are constant  For density, we only consider its change in the body force entries in momentum equation, others can be considered as constant.

<!-- b000084 | furniture | pages [6] -->
Team #48649                                                              Page 5 of 44

<!-- b000085 | prose | pages [6] -->
3) The volume of the air is infinite and the temperature of the air keeps constant.

<!-- b000086 | prose | pages [6] -->
Compared to the volume of the water, the volume of the air is much bigger, thus we can think the air is infinite and even. Then we can ignore the heat transfer in the air and take

<!-- b000087 | prose | pages [6] -->
t as a constant. air

<!-- b000088 | prose | pages [6] -->
4) The temperature can be evenly distributed in bathtub at any time when a person is in it (BWP model). When a person settles in the bathtub to cleanse, if the temperature distribution is uneven, he will feel uncomfortable and then he must agitate the water to make the temperature evenly distribution. 5) There doesn’t exist heat convection in the water when a person is in the bathtub (BWP model). From assumption 3 we can see, when the person is in the bathtub, the temperature is even in the water, thus there is no convection[2]. 6) The temperature of the bathtub is at a steady state at any time (BWP model). Heat dissipation can happen through the wall of the bathtub. When the water temperature and the air temperature remain unchanged, the bathtub temperature gradient will reach a steady state after time T. To simply the model, we take time T close to 0, that is, the temperature of the bathtub is at a steady state at any time. 7) The bathtub walls and the bottom are adiabatic in BWOP model. In BWOP model, heat dissipation through the wall of the bathtub is relatively small. Thus to simply the model, we take the bathtub as adiabatic. 8) All the model in the paper is at the state that the water filled the bathtub. In normal case, people will cleanse in tub with full water, so we just discuss such case and ignore the situation that the tub is unfilled.

<!-- b000089 | heading | pages [6] -->
3 Notations

<!-- b000090 | caption | pages [6] -->
Table 1: Constants

<!-- b000091 | prose | pages [6] -->
Symbol Definition Value Units

<!-- b000092 | prose | pages [6, 7] -->
The temperature of the air 298 K t air Stefan-Boltzmann constant     8 2 4 .5 67 10 W / m K Coefficient of cubical expansion   [3] t/1 Kinematic viscosity of the air （313 K ）   6 2 15 . 69 10 m / s air Kinematic viscosity of the water（313 K ）    4 2 .6 56 10 m / s water The thermal conductivity of the air(313 K )   [4] 0.02624 W / m K air The thermal conductivity of the water（313 K ）   0.64 W / m K w The specific heat capacity of water c  2.4 kJ / kg K  Dynamic viscosity coefficient of the water  Pa s   4 .6 56 10 Pr [5] Prandtl number 0.7~0.8

<!-- b000093 | furniture | pages [7] -->
Team #48649                                                              Page 6 of 44

<!-- b000095 | caption | pages [7] -->
Table 2: Variables

<!-- b000096 | prose | pages [7] -->
Symbol Definition Units

<!-- b000097 | prose | pages [7] -->
The temperature of the water in the bathtub K t water The temperature of the inflow hot water K t win The high threshold of the water temperature in the bathtub K ht The low threshold of the water temperature in the bathtub K lt The surface area of the water sA 2 m The contact area of the water and the bathtub bA 2 m The sectional area of the faucet A 2 m win The thickness of the bathtub m d b The volume of the bathtub V 3 m The thermal conductivity of the bathtub b  W / m K The heat transfer coefficient of the air h  2 W / m K air  Time s Inflow velocity m/ s v in The heat transfer that goes into the water in unit time kJ Q in The heat dissipation of the whole system in unit time kJ Q d Bathtub without a person in it model BWOP Bathtub with a person in it model BWP Continuous Inflow model CI Discontinuous Inflow model DCI

<!-- b000098 | heading | pages [7] -->
4 Model for bathtub without a person in it (BWOP model)

<!-- b000099 | prose | pages [7] -->
First we discuss the model when there is no person in the bathtub (BWOP model). By BWOP model, we can find the natural temperature distribution in the bathtub. Later (in next section) we will discuss the model for bathtub with a person in it (BWP model) based on the analysis of BWOP model.

<!-- b000100 | prose | pages [7, 8] -->
We make the rule that the faucet is at the middle of the base side and the water outlet is located at the middle of the opposite above side.

<!-- b000101 | furniture | pages [8] -->
Team #48649                                                              Page 7 of 44

<!-- b000103 | prose | pages [8] -->
The BWOP model can be decomposed into two parts:

<!-- b000104 | prose | pages [8] -->
1) The heating process 2) The heat dissipation process

<!-- b000105 | prose | pages [8] -->
In the heating process, the water goes into the bathtub from the faucet and overflow from the water outlet.

<!-- b000106 | prose | pages [8] -->
For calculation, as it’s difficult to find the exact mathematical solution for the distribution of the temperature in space and time, we simplify the BWOP model like this: As Graph 1 shows, the addition of the hot water is equivalent to a hot water tube from faucet to the water outlet, which means, there is a water tube heater to reheat the water in the bathtub.

<!-- b000107 | prose | pages [8] -->
Graph 1: The hot water tube model However, later we will simulate the real model by ANSYS.

<!-- b000108 | prose | pages [8] -->
In the heat dissipation process, the heat dissipates in two ways: the heat transfer between the water surface and the air and the heat transfer between the water and the bathtub. Based on the assumption we can see that the bathtub walls and the bottom are adiabatic, so we only consider the heat dissipation between the water surface and the air.

<!-- b000109 | prose | pages [8] -->
The framework of BWOP model is like this:

<!-- b000110 | furniture | pages [9] -->
Team #48649                                                              Page 8 of 44

<!-- b000111 | prose | pages [9] -->
Graph 2: The framework of BWOP model

<!-- b000112 | heading | pages [9] -->
4.1 The calculation of the heat-transfer coefficient

<!-- b000113 | prose | pages [9] -->
There are many factors influence the heat transfer, we can introduce the heat-transfer coefficient to reflect the heat transfer condition between dielectric.

<!-- b000114 | heading | pages [9] -->
4.1.1 The heat-transfer coefficient between the water surface and the air

<!-- b000115 | prose | pages [9] -->
When the system is under a steady condition, the water keeps the same temperature, we

<!-- b000116 | prose | pages [9] -->
t t denote it as , the air temperature is ,the qualitative temperature of the air is water air

<!-- b000117 | prose | pages [9] -->
    t ( t t /) 2 , , Pr nt , then we can find the heat- , and we can obtain the at n water air air air

<!-- b000118 | prose | pages [9] -->
h and the air as follows: transfer coefficient between the water surface air

<!-- b000119 | prose | pages [9] -->
3   g ( t t ) l  (4.1) Gr water air 0 2  air

<!-- b000120 | prose | pages [9] -->
1 Nu  (4.2) .0 54 Ra 4

<!-- b000121 | prose | pages [9, 10] -->
Ra  Gr Pr (4.3)   air h Nu air 0l (4.4)

<!-- b000122 | furniture | pages [10] -->
Team #48649                                                              Page 9 of 44

<!-- b000124 | prose | pages [10] -->
2  m / s : Kinematic viscosity of the air, air

<!-- b000125 | prose | pages [10] -->
  1 nt/ : Coefficient of cubical expansion and

<!-- b000126 | prose | pages [10] -->
2 m / s g : Gravitational acceleration,

<!-- b000127 | prose | pages [10] -->
0l : The width of the bathtub, m

<!-- b000128 | prose | pages [10] -->
  W / m K : The thermal conductivity of the air, air

<!-- b000129 | prose | pages [10] -->
Nu : Nusselt number Ra : Rayleigh number Gr: Grashof number Pr : Prandtl number

<!-- b000130 | heading | pages [10] -->
4.1.2 The heat-transfer coefficient between the water and the water tube

<!-- b000131 | prose | pages [10] -->
The heat transfer between the water and the water tube mainly contains two parts[6]: Convection heat loss:

<!-- b000132 | prose | pages [10] -->
  Q h A ( t t ) (4.5) c water os out w a t e

<!-- b000133 | prose | pages [10] -->
  A 2 r l (4.6) os o u t

<!-- b000134 | prose | pages [10] -->
Radiation heat loss:

<!-- b000135 | prose | pages [10] -->
  4 4 (4.7) Q A ( t t ) r os out water

<!-- b000136 | prose | pages [10] -->
We can see the temperature of the outside of the water tube is low, and it is a process of heat transfer to water, so the radiation heat loss is quite small and we can ignore it. Thus only the convection heat loss should be taken into consideration. According to our assumptions, the system of the water heat transfer is under stability balance, so the heat transfer between the inside and the outside of the tube is equal to the heat transfer between the water and the water tube,

<!-- b000137 | prose | pages [10] -->
  2 l ( t t )  (4.8) Q tube in out io r l n ( out ) r in

<!-- b000138 | prose | pages [10, 11] -->
h Thus, we can find the heat-transfer coefficient between the water and the water tube : water Q  h c water r Q ln( out ) r   ( t in t ) A in water os  2 l (4.9) tube

<!-- b000139 | furniture | pages [11] -->
Team #48649                                                              Page 10 of 44

<!-- b000141 | prose | pages [11] -->
2 A : The outside surface area of the water tube, m os

<!-- b000142 | prose | pages [11] -->
: The temperature of the outside of the water tube, K t out

<!-- b000143 | prose | pages [11] -->
int : The temperature of the inside of the water tube, K

<!-- b000144 | prose | pages [11] -->
inr : The water tube inside radius, m

<!-- b000145 | prose | pages [11] -->
r : The water tube outside radius, m out

<!-- b000146 | prose | pages [11] -->
  W / m K : The thermal conductivity of the tube, tube

<!-- b000147 | prose | pages [11] -->
l : The length of the tube, m : Emissivity (between 0 and 1)   8 2 4 : Stefan-Boltzmann constant .5 67 10 W / m · K

<!-- b000148 | heading | pages [11] -->
4.1.3 The heat-transfer coefficient between the hot water and the cube wall

<!-- b000149 | prose | pages [11] -->
  t ( t t /) 2 We can calculate the qualitative temperature of the hot water and m win wout

<!-- b000150 | prose | pages [11] -->
   mt , we can calculate the coefficient as follows: obtain , , Pr, at w water f

<!-- b000151 | prose | pages [11] -->
ud  (4.10) Re  water

<!-- b000152 | prose | pages [11] -->
   2 f ( .0 79 ln Re .1 64 ) (4.11)

<!-- b000153 | prose | pages [11] -->
 ( f / )8 Re Pr  f Nu ( ) (4.12)  2 1   w .1 07 12 7. ( f / )8 (Pr )1 3 2

<!-- b000154 | prose | pages [11] -->
  (4.13) h Nu w hwater d According to equation (4.10)-(4.13) we can obtain the heat-transfer coefficient between the

<!-- b000155 | prose | pages [11] -->
h hot water and the cube wall . hwater

<!-- b000156 | prose | pages [11] -->
 2 m / s ：Kinematic viscosity of the water， water

<!-- b000157 | prose | pages [11, 12] -->
f : Friction coefficient of the inside of the cube : Dynamic viscosity at mt ,  Pa s f

<!-- b000158 | furniture | pages [12] -->
Team #48649                                                              Page 11 of 44

<!-- b000160 | prose | pages [12] -->
: Dynamic viscosity at int ,  Pa s w

<!-- b000161 | prose | pages [12] -->
u : The flow velocity of hot water, m/ s d : The inside diameter of the tube, m

<!-- b000162 | heading | pages [12] -->
4.2 The heat dissipation between the water surface and the air

<!-- b000163 | prose | pages [12] -->
At the water surface, there both exists convective heat transfer and radiative heat transfer. We ignore the thermal radiation of air from the heat dissipation, heat absorption and thermal transpiration. Then we can calculate the convective heat transfer and radiative heat transfer at unit time independently as follows:

<!-- b000164 | prose | pages [12] -->
Convection heat loss:

<!-- b000165 | prose | pages [12] -->
  Q h A t ( t ) (4.14) c air s water air

<!-- b000166 | prose | pages [12] -->
Radiation heat loss:

<!-- b000167 | prose | pages [12] -->
   4 4 (4.15) Q A t ( t ) r s water air

<!-- b000168 | prose | pages [12] -->
We can see the temperature of the water surface is low, so compared with the convection heat loss, the radiation heat loss is quite small and we can ignore it. Thus only the convection heat loss should be taken into consideration.

<!-- b000169 | prose | pages [12] -->
At the surface of water, consider the third boundary conditions:

<!-- b000170 | prose | pages [12] -->
 t     (4.16) h ( t t )  w z h air water air  z

<!-- b000171 | prose | pages [12] -->
Q : The heat loss caused by convective heat transfer, kJ c

<!-- b000172 | prose | pages [12] -->
Q : The heat loss caused by radiative heat transfer, kJ r

<!-- b000173 | prose | pages [12] -->
2 A : The surface area of the water, m S

<!-- b000174 | prose | pages [12] -->
: The thermal conductivity of the water,  W / m K w

<!-- b000175 | prose | pages [12] -->
h : The depth of the water, m

<!-- b000176 | heading | pages [12] -->
4.3 The heat addition between the water and the hot water tube

<!-- b000177 | heading | pages [12] -->
4.3.1 The heat exchange between the inside and the outside of the tube

<!-- b000178 | prose | pages [12] -->
The inflow hot water temperature in the tube is the hot water’s temperature, the outflow hot water temperature in the tube is equivalent to the temperature in the bathtub after mixture.

<!-- b000179 | furniture | pages [13] -->
Team #48649                                                              Page 12 of 44

<!-- b000180 | prose | pages [13] -->
Thus the water qualitative temperature in the process is equivalent to the average of the inflow

<!-- b000181 | prose | pages [13] -->
  t ( t t /) 2 and outflow hot water temperature . m win wout

<!-- b000182 | prose | pages [13] -->
Since the wall of the tube is thin and the capacity of it is small, the process that hot water passing the tube can be considered as free of inertia and lag. However, the thermal resistance of the tube can’t be ignored. So the temperature of the outside of the tube is not equal to the inside. According to law of the conservation of energy, we can calculate the temperature of

<!-- b000183 | prose | pages [13] -->
t the outside of the tube as follows: out

<!-- b000184 | prose | pages [13] -->
    c Q ( t t ) KA t (4.17) win wout is

<!-- b000185 | prose | pages [13] -->
 1 1   ,  K h (4.18) hwater tube

<!-- b000186 | prose | pages [13] -->
 t t    t win wout t out 2 (4.19)

<!-- b000187 | prose | pages [13] -->
 kJ / kg K c : The specific heat capacity of hot water,

<!-- b000188 | prose | pages [13] -->
: The density of hot water, 3 kg m /

<!-- b000189 | prose | pages [13] -->
Q 3 : Volume flowrate of the hot water, m / s

<!-- b000190 | prose | pages [13] -->
A : The area of the inside wall of the cube, 2 m is

<!-- b000191 | prose | pages [13] -->
 2 K : Heat transfer coefficient, W / m K

<!-- b000192 | prose | pages [13] -->
: The thickness of the cube, m

<!-- b000193 | prose | pages [13] -->
 2 h W / m K : The heat-transfer coefficient between the hot water and the cube wall, hwater

<!-- b000194 | prose | pages [13] -->
: The temperature of the inflow hot water, K t win

<!-- b000195 | prose | pages [13] -->
: The temperature of the outflow hot water, K t wout

<!-- b000196 | prose | pages [13] -->
  W / m K : The thermal conductivity of the tube, tube

<!-- b000197 | heading | pages [13] -->
4.3.2 The heat exchange between the water and the water tube

<!-- b000198 | prose | pages [13, 14] -->
The heat transfer between the water and the water tube can be considered as the natural convection. In the process of natural convection, the basic governing equations are equation of continuity, momentum conservation equation, energy conservation equation. This model is a three-dimensional heat-transfer process and there is no inner heat source, so based on the assumption, we can get the governing equations as follows:

<!-- b000199 | furniture | pages [14] -->
Team #48649                                                              Page 13 of 44

<!-- b000201 | prose | pages [14] -->
Equation of continuity:

<!-- b000202 | prose | pages [14] -->
      ( u ) ( v ) ( w )    w w w 0 (4.20)    x y z

<!-- b000203 | prose | pages [14] -->
Momentum conservation equation:

<!-- b000204 | prose | pages [14] -->
        2 2 2 u u u u P u u u          ( u v w ) ( ) (4.21) w w          2 2 2 x y z x x y z

<!-- b000205 | prose | pages [14] -->
        2 2 2 v v v v P v v v          ( u v w ) ( ) (4.22) w w          2 2 2 x y z y x y z

<!-- b000206 | prose | pages [14] -->
        2 2 2 w w w w P w w w            ( u v w ) g ( ) (4.23) w w w          2 2 2 x y z z x y z

<!-- b000207 | prose | pages [14] -->
Energy conservation equation:

<!-- b000208 | prose | pages [14] -->
        2 2 2 t t t t t t t       water water water water w water water water u v w ( ) (4.24)          2 2 2 x y z c x y z w w

<!-- b000209 | prose | pages [14] -->
Equation (4.19) -（4.23）form the governing equations in the process of the heat transfer between the water and the water tube. Continuous heat transfer process is steady process. In this case, the temperature won’t change with the time, that is:

<!-- b000210 | prose | pages [14] -->
 t  (4.25) w a t e r 0  

<!-- b000211 | prose | pages [14] -->
This is the mathematical differential equation of the flow of the fluid, and then we consider the boundary conditions and initial conditions.

<!-- b000212 | prose | pages [14] -->
Boundary conditions:

<!-- b000213 | prose | pages [14] -->
1) The tube is heat source and is continuous heat transfer process. The temperature of the

<!-- b000214 | prose | pages [14] -->
t outside of the tube’s boundary condition is obtained by calculation out .

<!-- b000215 | prose | pages [14] -->
2) The walls and the bottom of the bathtub can be considered to be adiabatic。  t    (4.26) water 0  w z 0  z

<!-- b000216 | prose | pages [14] -->
Initial conditions:

<!-- b000217 | prose | pages [14] -->
t 1) The temperature of the water water

<!-- b000218 | prose | pages [14] -->
2) The gravitational acceleration g.

<!-- b000219 | prose | pages [14] -->
t 3) The air temperature air

<!-- b000220 | prose | pages [14, 15] -->
t t 4) The temperature of the inflow and outflow hot water win wout u : The flow velocity of water at X-direction, m/s v : The flow velocity of water at Y-direction, m/s w : The flow velocity of water at Z-direction, m/s

<!-- b000221 | furniture | pages [15] -->
Team #48649                                                              Page 14 of 44

<!-- b000223 | prose | pages [15] -->
: Dynamic viscosity coefficient of the water, Pa s w

<!-- b000224 | heading | pages [15] -->
4.4 Simulation of BWOP model based on ANSYS

<!-- b000225 | prose | pages [15] -->
To simulate the BWOP model, we use finite element method (FEM) by ANSYS. However, when simulating, we don’t adopt the hot water tube model, as this model is only used to simplify the calculating. ANSYS can deal with the real case that the hot water come from the faucet and the excess water escapes through an overflow drain.

<!-- b000226 | prose | pages [15] -->
The finite element method (FEM): FEM is a numerical technique for finding approximate solutions to boundary value problems for partial differential equations. It uses subdivision of a whole problem domain into simpler parts, called finite elements, and variational methods from the calculus of variations to solve the problem by minimizing an associated error function. Analogous to the idea that connecting many tiny straight lines can approximate a larger circle, FEM encompasses methods for connecting many simple element equations over many small subdomains, named finite elements, to approximate a more complex equation over a larger domain[7].

<!-- b000227 | prose | pages [15] -->
ANSYSY: ANSYS is a large-scale common finite element software. It publishes engineering analysis software across a range of disciplines including finite element analysis, structural analysis, computational fluid dynamics, explicit and implicit methods, and heat transfer. In this paper, we use FLUENT function to analyze BWOP model. FLUENT is based on CFD (Computational Fluid Dynamics), which can simulate fluid flows in a virtual environment — for example, the fluid dynamics of ship hulls; gas turbine engines (including the compressors, combustion chamber, turbines and afterburners); aircraft aerodynamics; pumps, fans, HVAC systems, mixing vessels, hydrocyclones, vacuum cleaners, etc[8].

<!-- b000228 | prose | pages [15] -->
If the system reaches steady state, it should meet the conditions:

<!-- b000229 | prose | pages [15] -->
 The bathtub is filled with water.

<!-- b000230 | prose | pages [15] -->
 The distribution of temperature doesn’t change with time When the system reaches steady state, we use ANSYS to simulate the state of the system temperature-space phase graph. In the 3-D model analysis, we use Hex Dominant unit whose shape is like Graph 3. To adjust to the real size in Table 3 of the tub, we define the tub model as Graph 4.

<!-- b000231 | caption | pages [15] -->
Table 3: Size of the tub

<!-- b000232 | prose | pages [15, 16] -->
cubage(m3) height(m) top-surface-size(m,m) bottom-surface-size(m,m) 0.3 0.4 1.4(length),0.7(width) 1.0(length),0.5(width) Graph 3: 3-D Hex Dominant model Graph 4: 3-D Bathtub model Using the ANSYS mesh we get the mesh carve up graph for the bathtub as Graph 5.

<!-- b000233 | furniture | pages [16] -->
Team #48649                                                              Page 15 of 44

<!-- b000235 | prose | pages [16] -->
Graph 5: Mesh Carve up

<!-- b000236 | prose | pages [16] -->
Using FEM by ANSYS, we get the isothermal diagram both inside and outside the bathtub as Graph 6 and Graph 7.

<!-- b000237 | prose | pages [16, 17] -->
Graph 6: The isothermal diagram of the intersecting surface Graph 7: The isothermal diagram of the tub body from outside

<!-- b000238 | furniture | pages [17] -->
Team #48649                                                              Page 16 of 44

<!-- b000240 | prose | pages [17] -->
Calculate the result we get statistic in table 4.

<!-- b000241 | caption | pages [17] -->
Table 4: Report on Volume Integral

<!-- b000242 | prose | pages [17] -->
Average tub- Average top Volume- Volume- Volume- Volume- wall heat surface heat average Maximum Minimum average flux(W) flux(W) Temp(k) Temp(K) Temp(K) Temp(ºC) -0.06104 -1.3394727 313.1946 318.0238 312.9532 40.4178

<!-- b000243 | prose | pages [17] -->
From Graph 6 and Graph 7 we can obviously find that due to the heat loss to the air, the top surface of the water in bathtub holds lower temperature than other part inside. Also, it is lower than the volume-average temperature. From Graph 6, it is easy to see the temperature distribution across the intersecting surface. The inflow region from the faucet hold the highest degree and the temperature gets down sharply across the line from the faucet to the main body of the water.

<!-- b000244 | prose | pages [17] -->
From the two graphs, we can excitedly find that the main body of the water in bathtub holds stable and comfortable temperature, which will provide people with a great experience. The statistical data of the volume temperature also indicate that the average degree is about 40º-- the most suitable temperature for human beings in winter. Besides, the maximum point with 318º is limited to a small region around the faucet, it is in low possibility to scald people inside. Even if one touch it by accident, 45ºis much lower than adults’ bearing limit 55ºwhich guarantee the safety.

<!-- b000245 | prose | pages [17] -->
At last, from Graph 7 and data in Table 4, it is interesting to find that the heat loss by the tub-wall is much smaller than that by air. It is also realistic according to our reference.

<!-- b000246 | furniture | pages [18] -->
Team #48649                                                              Page 17 of 44

<!-- b000247 | heading | pages [18] -->
5 Model for bathtub with a person in it (BWP model)

<!-- b000248 | prose | pages [18] -->
We have discussed the case of the temperature distribution in a bathtub without a person in it, and now we consider the case where a person is in the bathtub.

<!-- b000249 | prose | pages [18] -->
In BWP model, we first discuss the temperature distribution in the tub if the person is actionless. Based on this, we make the assumption that the temperature is evenly distributed in BWP model.

<!-- b000250 | prose | pages [18] -->
Then we discuss the heat dissipation process based on two sub-models: Water-Air heat convection and Water-Bathtub heat conduction. We simulate the process with MATLAB. Based on the analysis result, we propose two inflow model: Continuous Inflow model and Discontinuous Inflow model. Then we analysis the performance of each model by fuzzy comprehensive evaluation method (FCE) to find a better one.

<!-- b000251 | prose | pages [18] -->
Graph 8 shows the framework of BWP model:

<!-- b000252 | prose | pages [18, 19] -->
Graph 8: The framework of BWP model 5.1 Simulation of the temperature distribution if the person is still

<!-- b000253 | furniture | pages [19] -->
Team #48649                                                              Page 18 of 44

<!-- b000255 | prose | pages [19] -->
Graph 9 shows the model of the bathtub when a person is cleaning. There will be some heat transfer between the water and the person, but it’s small enough to be ignored.

<!-- b000256 | prose | pages [19] -->
Graph 9: Bathtub model with person Now we suppose the person keeps still, thus the temperature of water should distributes naturally. Graph 10 show the isothermal in the bathtub and Graph 11 show the temperature distribution on the body surface of the person.

<!-- b000257 | prose | pages [19, 20] -->
Graph 10: The isothermal diagram of the tub body with a person (We don’t show the person in the graph) Graph 11: The isothermal diagram on the body surface of a person From Graph 11 we can see that the temperature distributes unevenly on the body surface of the person if the person just settles down in the bathtub and keeps still. Thus the person will feel uncomfortable as his upper part of the body feel cool and the lower part of the body feels hot. However, in fact, if a person feel uncomfortable, he must agitate the water to make the temperature distributes more evenly. Based on the analysis, when dealing with BWP model, we can make the assumption that the temperature can be evenly distributed in bathtub at any time when a person is in it.

<!-- b000258 | furniture | pages [20] -->
Team #48649                                                              Page 19 of 44

<!-- b000260 | heading | pages [20] -->
5.2 Heat dissipation in BWP model

<!-- b000261 | prose | pages [20] -->
As the temperature can be evenly distributed, we can make the rule：In time T, if some hot water flows into the bathtub, then the temperature distribution will get even immediately.

<!-- b000262 | prose | pages [20] -->
As we ignore the heat transfer between the water and the person, the dissipation of heat can be decomposed into two parts:

<!-- b000263 | prose | pages [20] -->
 The heat exchange between the water surface and the air (Water-Air).

<!-- b000264 | prose | pages [20] -->
 The heat exchange between the water and the wall of the bathtub (Water-Bathtub) Then we can get the total heat dissipation.

<!-- b000265 | heading | pages [20] -->
5.2.1 Water-Air heat convection

<!-- b000266 | prose | pages [20] -->
This process is similar to the case 4.2, the heat transfer in unit time between the water surface and the air in BWOP model. So we directly get the equation: Convection heat loss:

<!-- b000267 | prose | pages [20] -->
  Q h A t ( t ) (5.1) c air s water air

<!-- b000268 | prose | pages [20] -->
The third boundary conditions:

<!-- b000269 | prose | pages [20, 21] -->
 t     (5.2) h ( t t )  w z h air water air  z  Q Q Suppose in this process, heat dissipation is . 1 c

<!-- b000270 | furniture | pages [21] -->
Team #48649                                                              Page 20 of 44

<!-- b000272 | heading | pages [21] -->
5.2.2 Water-Bathtub heat conduction

<!-- b000273 | prose | pages [21] -->
Heat dissipation can also happen at the contact surface of the water and the wall of the bathtub. From the assumption we can see, there doesn’t exist convection in the water when the person is in the bathtub and the temperature of the bathtub at the steady state at any time. Thus the heat transfer process between the water and the bathtub should be a steady process.

<!-- b000274 | prose | pages [21] -->
The heat transfer between the water and the bathtub can be decomposed into two parts:

<!-- b000275 | prose | pages [21] -->
 The heat conduction between the water and the wall of the bathtub (Water-Bathtub process)  The heat convection between the outside surface of the bathtub and the air (Bathtub- Air process).

<!-- b000276 | prose | pages [21] -->
Q . Suppose in this process, heat dissipation in unit time is 2

<!-- b000277 | prose | pages [21] -->
1) Water-Bathtub process As the water temperature distributes evenly and the bathtub remains steady state, the heat transfer in Water-Bathtub process is a steady heat conduction process.

<!-- b000278 | prose | pages [21] -->
The equation of heat conduction[9]:

<!-- b000279 | prose | pages [21] -->
 t t   water b Q A (5.3) 2 b b d b

<!-- b000280 | prose | pages [21] -->
: The heat conductivity coefficient of the bathtub. In simulating, b  0.19 W/m K b

<!-- b000281 | prose | pages [21] -->
bt : The temperature of the outside of the bathtub.

<!-- b000282 | prose | pages [21] -->
 2 bA : The contact area of the water and the tub. In simulating, bA 1.53 m

<!-- b000283 | prose | pages [21] -->
 d : The thickness of the bathtub. d 0.04 m b b

<!-- b000284 | prose | pages [21] -->
2) Bathtub-Air process The heat transfer between the bathtub and the air is similar to Water-Air case, which can be taken as 2-dimensional heat convection process.

<!-- b000285 | prose | pages [21] -->
Convection heat loss:

<!-- b000286 | prose | pages [21] -->
  Q h A t ( t ) (5.4) 2 airb b b air

<!-- b000287 | prose | pages [21, 22] -->
h : The convection coefficient of the contact surface between the air and the bathtub. In airb   2 simulating, h 5 W/m K airb

<!-- b000288 | furniture | pages [22] -->
Team #48649                                                              Page 21 of 44

<!-- b000290 | heading | pages [22] -->
5.2.3 The total heat dissipation in the bathtub

<!-- b000291 | prose | pages [22] -->
By the three models above, we can conclude that, when there is a person in the bathtub,

<!-- b000292 | prose | pages [22] -->
  Q Q Q the heat dissipation in unit time is 2 1

<!-- b000293 | heading | pages [22] -->
5.3 Simulation of BWP model with MATLAB

<!-- b000294 | prose | pages [22] -->
If there is no heating source, we simulate the Temperature-Time graph with MATLAB to find the thermal losses.

<!-- b000295 | prose | pages [22] -->
Graph 12 shows the heat loss caused by the heat convection between the water surface and the air.

<!-- b000296 | prose | pages [22] -->
Temperature curve of Water-Air heat transfer process 318

<!-- b000297 | prose | pages [22] -->
316

<!-- b000298 | prose | pages [22] -->
314

<!-- b000299 | prose | pages [22] -->
312 Temperature/K 310

<!-- b000300 | prose | pages [22] -->
308

<!-- b000301 | prose | pages [22] -->
306

<!-- b000302 | prose | pages [22] -->
304

<!-- b000303 | prose | pages [22] -->
302

<!-- b000304 | prose | pages [22] -->
300 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000305 | prose | pages [22, 23] -->
Graph 12: Temperature curve of Water-Air heat transfer process Temperature curve of Water-Buthtub heat transfer process 318

<!-- b000306 | furniture | pages [23] -->
Team #48649                                                              Page 22 of 44

<!-- b000308 | prose | pages [23] -->
317

<!-- b000309 | prose | pages [23] -->
316

<!-- b000310 | prose | pages [23] -->
315 Temperature/K 314

<!-- b000311 | prose | pages [23] -->
313

<!-- b000312 | prose | pages [23] -->
312

<!-- b000313 | prose | pages [23] -->
311

<!-- b000314 | prose | pages [23] -->
310

<!-- b000315 | prose | pages [23] -->
309

<!-- b000316 | prose | pages [23] -->
308 0 500 1000 1500 2000 2500 3000 Time/min

<!-- b000317 | prose | pages [23] -->
Graph 13: Temperature curve of Water-Bathtub heat transfer process

<!-- b000318 | prose | pages [23] -->
Graph 13 shows the heat loss only caused by the heat conduction between the water and the bathtub. We can find that the heat loss through the bathtub is much slower than the heat loss through the Water-Air surface, which is truthfulness as the thermal conductivity of the bathtub is much smaller than the convection coefficient of the surface between the water and the air.

<!-- b000319 | prose | pages [23] -->
Temperature curve of the total heat transfer process 318

<!-- b000320 | prose | pages [23] -->
316

<!-- b000321 | prose | pages [23] -->
314

<!-- b000322 | prose | pages [23] -->
312 Temperature/K 310

<!-- b000323 | prose | pages [23] -->
308

<!-- b000324 | prose | pages [23] -->
306

<!-- b000325 | prose | pages [23] -->
304

<!-- b000326 | prose | pages [23] -->
302

<!-- b000327 | prose | pages [23] -->
300 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000328 | prose | pages [23, 24] -->
Graph 14: Temperature curve of total heat transfer process Graph 14 shows the total heat dissipation in BWP model which contains the Water-Air transfer and the Water-Bathtub transfer. We can see the curve is similar to the curve of the Water-Air case, as most of the heat loss is dissipated through the water surface.

<!-- b000329 | furniture | pages [24] -->
Team #48649                                                              Page 23 of 44

<!-- b000331 | heading | pages [24] -->
5.4 Heat addition model

<!-- b000332 | prose | pages [24] -->
Based on the former analysis of BWP model, we can find the heat dissipation Q in unit time. Our goal is to find an optimal strategy, so now we use two inflow model to simulate the inflow of water:

<!-- b000333 | prose | pages [24] -->
 Continuous Inflow model (CI model)  Discontinuous Inflow model (DCI model).

<!-- b000334 | prose | pages [24] -->
In CI model, the water flow into the bathtub with a constant trickle.

<!-- b000335 | prose | pages [24] -->
In DCI model, the water flow into the bathtub only when the temperature comes below a low threshold value and it will stop watering when the temperature reaches a high threshold value.

<!-- b000336 | prose | pages [24] -->
After discuss the two model, we use the fuzzy comprehensive evaluation to find a better strategy.

<!-- b000337 | prose | pages [24] -->
For normal case, we set the proper cleansing temperature as 313 K, the inflow water temperature as 318 K and the cleansing time as 40 min.

<!-- b000338 | prose | pages [24] -->
The evaluation criteria are:

<!-- b000339 | prose | pages [24] -->
1) The amount of water needed, Wn . We will calculate Wn of each model later.

<!-- b000340 | heading | pages [24] -->
2) The comfortable degree of the user, Cd

<!-- b000341 | prose | pages [24] -->
We can see that people will feel comfortable when the water temperature keeps constant, if the temperature of the water changes frequently, people can feel uncomfortable. Thus we define the comfortable degree as the reciprocal of the  standard deviation of the temperature.

<!-- b000342 | prose | pages [24] -->
1  (5.5) Cd n   2 ( t t ) i  i 1 n

<!-- b000343 | prose | pages [24] -->
t is the average temperature.

<!-- b000344 | heading | pages [24] -->
3) The operation complexity, Oc

<!-- b000345 | prose | pages [24] -->
If the person always need to open or close the faucet, it will improve the operation complexity. Thus we define the operation complexity as the reciprocal of the operation

<!-- b000346 | prose | pages [24] -->
oT : period

<!-- b000347 | prose | pages [24] -->
1   (0    Oc Oc 1) (5.6) T o

<!-- b000348 | heading | pages [24] -->
4) The operative difficulty index 

<!-- b000349 | furniture | pages [25] -->
Team #48649                                                              Page 24 of 44

<!-- b000350 | heading | pages [25] -->
5.4.1 Continuous Inflow model (CI model)

<!-- b000351 | prose | pages [25] -->
In continuous influent model, we let the hot water go into the bathtub with a constant inflow

<!-- b000352 | prose | pages [25] -->
v . When the bathtub is filled with water, excess water will escape through the velocity in

<!-- b000353 | prose | pages [25] -->
v overflow drain with an overflow velocity . Now we make the rules: out

<!-- b000354 | prose | pages [25] -->
 As the maximum of the volume of the bathtub is a constant, we can get that the overflow velocity is a constant and it’s equal to the inflow velocity. That is:

<!-- b000355 | prose | pages [25] -->
  v v v (5.7) in out

<!-- b000356 | prose | pages [25] -->
 When time  goes from i to i, we think the hot water has been mixed evenly 1

<!-- b000357 | prose | pages [25] -->
t with the original water, so the temperature of the overflow water is equal to the wout

<!-- b000358 | prose | pages [25] -->
i. That is: temperature of the water at 1

<!-- b000359 | prose | pages [25] -->
 (5.8) t t  wout w i ( 1)

<!-- b000360 | prose | pages [25] -->
Now we deeply discuss the CI model.

<!-- b000361 | prose | pages [25] -->
v keeps constant, which also In the process of the continuous inflow of hot water, in

<!-- b000362 | prose | pages [25] -->
Q is a constant. The heating capacity can be equal to the means, the heating capacity in

<!-- b000363 | prose | pages [25] -->
decrement of the thermal of the inflow hot water and the overflow water. That is[10]:

<!-- b000364 | prose | pages [25] -->
   Q c v A ( t t ) (5.9) in w w in win win wout

<!-- b000365 | prose | pages [25] -->
The heating process is a steady heat transfer process and the heat go into the bathtub is absorbed by the water entirely. The heat absorbed is consumed in two ways:

<!-- b000366 | prose | pages [25] -->
Q is absorbed by the water to raise its temperature, represented by Q  Part of in wt

<!-- b000367 | prose | pages [25] -->
Q is transferred to the air and the bathtub, which is equal toQ .  Another part of in

<!-- b000368 | prose | pages [25] -->
When time  goes from i to i, by energy conservation equation: 1

<!-- b000369 | prose | pages [25] -->
      Q Q c V t ( t ) (5.10)  in d w w w i ( 1) w i ( )

<!-- b000370 | prose | pages [25] -->
 t : The temperature of the inflow hot water, C win

<!-- b000371 | prose | pages [25] -->
i, C  t : The temperature of the water in the bathtub at time w i ( )

<!-- b000372 | prose | pages [25, 26] -->
3 V: The volume of the bathtub, m 2 A : The sectional area of the faucet, m win

<!-- b000373 | furniture | pages [26] -->
Team #48649                                                              Page 25 of 44

<!-- b000375 | heading | pages [26] -->
1) Find the amount of needed water

<!-- b000376 | prose | pages [26] -->
ct time and we can get the amount of the water needed Suppose the person cleanses for

<!-- b000377 | prose | pages [26] -->
(measured in volume) is:

<!-- b000378 | prose | pages [26] -->
 Wn v A t (5.11) in win c

<!-- b000379 | prose | pages [26] -->
We set the proper water temperature that the people will feel comfortable as 313K. When the water temperature is at 313K, we control the inflow heat the same as the heat dissipation, thus the temperature can stay at the proper temperature.

<!-- b000380 | prose | pages [26] -->
From the graph 14 and calculation we can get:

<!-- b000381 | caption | pages [26] -->
Table 5: Water needed of CI model

<!-- b000382 | prose | pages [26] -->
Inflow velocity 3 Water need ( m ) (m/min) 16.2426 0.0735

<!-- b000383 | prose | pages [26] -->
We simulate the Continuous Inflow model with MATLAB and we get the temperature curve as Graph 15 shows.

<!-- b000384 | prose | pages [26] -->
Temperature curve of the continuous inflow process 319

<!-- b000385 | prose | pages [26] -->
318

<!-- b000386 | prose | pages [26] -->
317

<!-- b000387 | prose | pages [26] -->
316 Temperature/K 315

<!-- b000388 | prose | pages [26] -->
314

<!-- b000389 | prose | pages [26] -->
313

<!-- b000390 | prose | pages [26] -->
312

<!-- b000391 | prose | pages [26] -->
311

<!-- b000392 | prose | pages [26] -->
310 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000393 | prose | pages [26] -->
Graph 15: Temperature curve of the continuous inflow process

<!-- b000394 | heading | pages [26] -->
2) The comfortable degree of user

<!-- b000395 | prose | pages [26] -->
By MATLAB, the standard deviation of the temperature is 0.09432.

<!-- b000396 | furniture | pages [27] -->
Team #48649                                                              Page 26 of 44

<!-- b000397 | prose | pages [27] -->
Thus we can getCd =10.6021 . CI

<!-- b000398 | heading | pages [27] -->
3) The operation complexity

<!-- b000399 | prose | pages [27] -->
Similarly, the person don’t need operate and the operation period is infinite.

<!-- b000400 | prose | pages [27] -->
SoOc =1 CI

<!-- b000401 | heading | pages [27] -->
4) The operative difficulty index

<!-- b000402 | prose | pages [27] -->
In order to keep the temperature unchanged, the operative difficulty index  is high. We

<!-- b000403 | prose | pages [27] -->
 =10 let

<!-- b000404 | heading | pages [27] -->
5.4.2 Discontinuous Inflow model (DCI model)

<!-- b000405 | prose | pages [27] -->
In DCI model, the hot water only inflow when the temperature comes below a low threshold

<!-- b000406 | prose | pages [27] -->
lt and it will stop inflow when the temperature of the water comes above a high value

<!-- b000407 | prose | pages [27] -->
, there are two stages: heating stage and cooling stage. threshold value ht . In a time period p

<!-- b000408 | prose | pages [27] -->
 Heating stage  t t When water , the faucet is opened and the hot water inflow with a constant velocity l

<!-- b000409 | prose | pages [27] -->
  v for time . After time , the temperature of the water reaches the high p 1 p 1 in

<!-- b000410 | prose | pages [27] -->
threshold value ht , thus the hot water stop inflowing.

<!-- b000411 | prose | pages [27] -->
This process is similar to the CI model, so we can get the equation directly:

<!-- b000412 | prose | pages [27] -->
      Q Q c V t ( t ) (5.9)    in p 1 d p 1 w w w ( ) w ( ) p 1

<!-- b000413 | prose | pages [27] -->
 t t (5.10)   w ( ) h p 1

<!-- b000414 | prose | pages [27] -->
 t t (5.11) w ( ) l

<!-- b000415 | prose | pages [27] -->
is reference time.  wt is the temperature of the water after time .   ( ) p 1 p 1

<!-- b000416 | prose | pages [27] -->
 Cooling stage  The water will cool down from high temperature ht to lower one lt for time . This p 1

<!-- b000417 | prose | pages [27] -->
process is a natural cooling process. Without internal heat source, the thermal equation becomes:

<!-- b000418 | prose | pages [27, 28] -->
     0 Q c V t ( t ) (5.12)       d p 2 w w w ( ) w ( ) p 1 p 2 p 1   t t t (5.13)       w ( ) w ( ) l p 1 p 2 p

<!-- b000419 | furniture | pages [28] -->
Team #48649                                                              Page 27 of 44

<!-- b000421 | heading | pages [28] -->
1) Find the amount of needed water

<!-- b000422 | prose | pages [28] -->
  lt 312 K ht 314 K We set the low threshold value , the high threshold value .

<!-- b000423 | prose | pages [28] -->
Temperature curve of the discontinuous inflow process 319

<!-- b000424 | prose | pages [28] -->
318

<!-- b000425 | prose | pages [28] -->
317

<!-- b000426 | prose | pages [28] -->
316 Temperature/K 315

<!-- b000427 | prose | pages [28] -->
314

<!-- b000428 | prose | pages [28] -->
313

<!-- b000429 | prose | pages [28] -->
312

<!-- b000430 | prose | pages [28] -->
311

<!-- b000431 | prose | pages [28] -->
310 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000432 | prose | pages [28] -->
Graph 16: Temperature curve of the discontinuous inflow process By this graph we can get the amount of the water needed:

<!-- b000433 | caption | pages [28] -->
Table 6: Water needed of DCI model

<!-- b000434 | prose | pages [28] -->
Inflow velocity 3 Water need ( m ) (m/min) 25.67 0.0524

<!-- b000435 | heading | pages [28] -->
2) The comfortable degree of user

<!-- b000436 | prose | pages [28] -->
By MATLAB, the standard deviation of the temperature is 0.5961.

<!-- b000437 | prose | pages [28] -->
Thus we can getCd =1.67757 . DCI

<!-- b000438 | heading | pages [28] -->
3) The operation complexity

<!-- b000439 | prose | pages [28] -->
By MATLAB, the operation period is 94min.

<!-- b000440 | prose | pages [28] -->
Thus we can get Oc =0.01064 DCI

<!-- b000441 | heading | pages [28] -->
4) The operative difficulty index

<!-- b000442 | prose | pages [28] -->
It’s easy if the person just open the faucet with a relatively high water velocity, thus we

<!-- b000443 | prose | pages [28] -->
; 1 set

<!-- b000444 | furniture | pages [29] -->
Team #48649                                                              Page 28 of 44

<!-- b000445 | heading | pages [29] -->
5.4.3 FCE of the two models

<!-- b000446 | prose | pages [29] -->
FCE is a useful method for multiple criteria decision process. It determines the weights of each criterion based on the data only. Based on the actual statistics of the 2 strategies, we get the values of each factor from section 5.4 and show them in Table 7.

<!-- b000447 | caption | pages [29] -->
Table 7: values of factors and allocations

<!-- b000448 | prose | pages [29] -->
The comfortable operation operative Model 3 Water need ( m ) degree complexity difficulty index CI 0.0735 10.0621 1 10 DCI 0.0524 1.67757 0.01064 1

<!-- b000449 | prose | pages [29] -->
From Table 7, we derive the ideal allocation as follows,  (0.0524, 10.6021, 1, 1)                   (5.14) u

<!-- b000450 | prose | pages [29] -->
 The Fuzzy Evaluation Matrix (FEM) We define

<!-- b000451 | prose | pages [29] -->
 a u i , j j  (5.15) r i , j  max{ a } min{ a } i , j i , j

<!-- b000452 | prose | pages [29] -->
We obtain the FEM

<!-- b000453 | prose | pages [29] -->
  0 . 0021 0 0 0 . 9045  (5.16) R    0 0 . 8364 0 . 0994 0 

<!-- b000454 | prose | pages [29] -->
Also we define

<!-- b000455 | prose | pages [29] -->
s v   j j (5.17) v , w j j 4 X  v j j  i j

<!-- b000456 | prose | pages [29] -->
Then we get   (0.3, 0.15, 0.15, 0.4)                    (5.18)

<!-- b000457 | prose | pages [29] -->
 Result of the FCE Define the relative deviation as

<!-- b000458 | prose | pages [29] -->
   T (5.19) F R

<!-- b000459 | prose | pages [29] -->
F measures the distance from a specific factor group to the ideal one, so the smaller F is, the better the strategy is. Then we get the final result shown in Table 8.

<!-- b000460 | caption | pages [29] -->
Table 8: FCE result for two strategies

<!-- b000461 | furniture | pages [30] -->
Team #48649                                                              Page 29 of 44

<!-- b000462 | prose | pages [30] -->
F CI 0.3624 DCI 0.1404

<!-- b000463 | prose | pages [30] -->
The result tells us that: the DCI model is better when we take all the factor into consideration. DCI model is economic and operable, which is very important for our users.

<!-- b000464 | heading | pages [30] -->
6 Sensitivity analysis

<!-- b000465 | heading | pages [30] -->
6.1 Sensitivity analysis for BWOP

<!-- b000466 | prose | pages [30] -->
Considering our simulation results on BWOP model, the heat loss by the bathtub-wall is less than 10 percent of that by water-air convection. In our further discussion on the model, we ignore this aspect and pay our attention to other parameters such as the air temperature, the inflow temperature and the inflow velocity. We choose four main criteria to evaluate the model: the average top surface heat flux, volume-average temperature, Volume-maximum temperature and volume-minimum temperature. By using control variate method, we change the parameters from the best condition to see their effect on the four criteria. By doing simulation we get the result shown in Table 9, Table 10 and Table 11.

<!-- b000467 | heading | pages [30] -->
6.1.1 Inflow Velocity

<!-- b000468 | caption | pages [30] -->
Table 9: Results by Changing Inflow Velocity

<!-- b000469 | prose | pages [30, 31] -->
Inflow Average top Volume- Volume- Volume- Velocity Inflow Air surface heat average maximum minimum (m/s) Temp(K) Temp(K) flux(W) Temp(K) Temp(K) Temp(K) 0.01 318 298 1.1590 310.3719 318.101 309.9957 0.02 318 298 1.4406 313.4178 318.024 312.9532 0.03 318 298 1.5651 314.7500 318.007 314.2474 0.04 318 298 1.6329 315.4771 318.003 314.9534 0.05 318 298 1.6765 315.9474 318.003 315.4104 Temperature-Inflow Velocity graph 319

<!-- b000470 | furniture | pages [31] -->
Team #48649                                                              Page 30 of 44

<!-- b000472 | prose | pages [31] -->
318

<!-- b000473 | prose | pages [31] -->
317

<!-- b000474 | prose | pages [31] -->
316 Temperature/K 315

<!-- b000475 | prose | pages [31] -->
314

<!-- b000476 | prose | pages [31] -->
313

<!-- b000477 | prose | pages [31] -->
312 Volume-average Temp Volume-maximum Temp 311 Volume-minimum Temp 310

<!-- b000478 | prose | pages [31] -->
309 0.01 0.015 0.02 0.025 0.03 0.035 0.04 0.045 0.05 Inflow Velocity/(m/s)

<!-- b000479 | prose | pages [31] -->
Graph 17: Temperature-Inflow Velocity graph

<!-- b000480 | prose | pages [31] -->
Average top surface heat flux-Inflow Velocity graph 1.8

<!-- b000481 | prose | pages [31] -->
1.7

<!-- b000482 | prose | pages [31] -->
1.6

<!-- b000483 | prose | pages [31] -->
heat flux/W 1.5

<!-- b000484 | prose | pages [31] -->
1.4

<!-- b000485 | prose | pages [31] -->
1.3

<!-- b000486 | prose | pages [31] -->
1.2

<!-- b000487 | prose | pages [31] -->
1.1 0.01 0.015 0.02 0.025 0.03 0.035 0.04 0.045 0.05 Inflow Velocity/(m/s)

<!-- b000488 | prose | pages [31] -->
Graph 18: Average top surface heat-Inflow Velocity graph From Table 9 and the corresponding graph we can notice that: the average top surface heat flux, the volume-average temperature and volume-minimum temperature have positive correlation with inflow velocity, and the raising rate goes down as the inflow velocity goes up for the maximum temperature is bounded. It is corresponding to our common sense that more hot water per second leads to a higher temperature. The heat flux of the top surface is also determined by the volume average temperature with air temperature fixed.

<!-- b000489 | furniture | pages [32] -->
Team #48649                                                              Page 31 of 44

<!-- b000490 | heading | pages [32] -->
6.1.2 Inflow Temperature

<!-- b000491 | caption | pages [32] -->
Table 10: Results by Changing Inflow Temperature

<!-- b000492 | prose | pages [32] -->
Inflow Average top Volume- Volume- Volume- Velocity Inflow Air surface heat average maximum minimum (m/s) Temp(K) Temp(K) flux(W) Temp(K) Temp(K) Temp(K) 0.02 314 298 1.1525 310.3342 314.019 309.9626 0.02 316 298 1.2966 311.8761 316.025 311.4579 0.02 318 298 1.5652 313.4178 318.024 312.9532 0.02 320 298 1.5871 314.9596 320.026 314.4485 0.02 322 298 1.7287 316.5013 322.029 315.9438

<!-- b000493 | prose | pages [32] -->
Volume Temperature-Inflow Temperature graph 324

<!-- b000494 | prose | pages [32] -->
322

<!-- b000495 | prose | pages [32] -->
320 Volume Temperature/K 318

<!-- b000496 | prose | pages [32] -->
316

<!-- b000497 | prose | pages [32] -->
314

<!-- b000498 | prose | pages [32] -->
312 Volume-average Temp Volume-maximum Temp 310 Volume-minimum Temp

<!-- b000499 | prose | pages [32] -->
308 314 315 316 317 318 319 320 321 322 Inflow Temperature/K

<!-- b000500 | prose | pages [32, 33] -->
Graph 19: Volume Temperature- Inflow Temperature graph Average top surface heat flux-Inflow Temperature graph 1.9

<!-- b000501 | furniture | pages [33] -->
Team #48649                                                              Page 32 of 44

<!-- b000503 | prose | pages [33] -->
1.8

<!-- b000504 | prose | pages [33] -->
1.7

<!-- b000505 | prose | pages [33] -->
1.6 heat flux/W 1.5

<!-- b000506 | prose | pages [33] -->
1.4

<!-- b000507 | prose | pages [33] -->
1.3

<!-- b000508 | prose | pages [33] -->
1.2

<!-- b000509 | prose | pages [33] -->
1.1 314 315 316 317 318 319 320 321 322 Inflow Temperature/K

<!-- b000510 | prose | pages [33] -->
Graph 20: Average top surface heat - Inflow Temperature graph From Table 10 and the corresponding graph we can notice that: the average top surface heat flux, the volume-average temperature, the volume-maximum temperature and volume- minimum temperature have positive correlation with inflow temperature, and the raising rate keeps still as the inflow velocity goes up. It is corresponding to our common sense that the hotter the inflow, the warmer the bathtub water. And different from the inflow velocity, all the criteria changes at almost direct proportion. That indicates adding hotter inflow is the most effective way to keep the bathtub warm. However, considering about people’s bearing capacity on water temperature and comfortability, the inflow temperature have to be bounded under 323K to avoid scald.

<!-- b000511 | heading | pages [33] -->
6.1.3 Air Temperature

<!-- b000512 | caption | pages [33] -->
Table 11: Results by Changing Air Temperature

<!-- b000513 | prose | pages [33, 34] -->
Inflow Average top Volume- Volume- Volume- Velocity Inflow Air surface heat average maximum minimum (m/s) Temp(K) Temp(K) flux(W) Temp(K) Temp(K) Temp(K) 0.02 318 294 1.7287 312.5041 318.029 311.9438 0.02 318 296 1.5847 312.9596 318.026 312.4485 0.02 318 298 1.5652 313.4178 318.024 312.9532 0.02 318 300 1.2966 313.8762 318.022 313.4579 0.02 318 302 1.1525 314.3342 318.091 313.9625 Table Volume Temperature-Air Temperature graph 319

<!-- b000514 | furniture | pages [34] -->
Team #48649                                                              Page 33 of 44

<!-- b000516 | prose | pages [34] -->
318

<!-- b000517 | prose | pages [34] -->
317 Volume Temperature/K 316 Volume-average Temp Volume-maximum Temp Volume-minimum Temp 315

<!-- b000518 | prose | pages [34] -->
314

<!-- b000519 | prose | pages [34] -->
313

<!-- b000520 | prose | pages [34] -->
312

<!-- b000521 | prose | pages [34] -->
311 294 295 296 297 298 299 300 301 302 Air Temperature/K

<!-- b000522 | prose | pages [34] -->
Graph 21: Volume Temperature - Air Temperature graph

<!-- b000523 | prose | pages [34] -->
Average top surface heat flux-Air Temperature graph 1.9

<!-- b000524 | prose | pages [34] -->
1.8

<!-- b000525 | prose | pages [34] -->
1.7

<!-- b000526 | prose | pages [34] -->
1.6 heat flux/W 1.5

<!-- b000527 | prose | pages [34] -->
1.4

<!-- b000528 | prose | pages [34] -->
1.3

<!-- b000529 | prose | pages [34] -->
1.2

<!-- b000530 | prose | pages [34] -->
1.1 294 295 296 297 298 299 300 301 302 Air Temperature/K

<!-- b000531 | prose | pages [34] -->
Graph 22: Average top surface heat - Air Temperature graph

<!-- b000532 | prose | pages [34, 35] -->
From Table 11 and the corresponding graph we can notice that: the average top surface heat flux has negative correlation with air temperature. When the air gets warmer, the heat lass becomes small is realistic and that just indicates why we need bath heater in our bathroom to avoid us from getting cold. The volume-average temperature and volume-minimum temperature have positive correlation with air temperature, and the raising rate goes down as the inflow velocity goes up. It is corresponding to our common sense that once the heat loss gets smaller, the remaining water gets warmer which follows energy conservation law.

<!-- b000533 | furniture | pages [35] -->
Team #48649                                                              Page 34 of 44

<!-- b000535 | heading | pages [35] -->
6.1.4 Conclusion

<!-- b000536 | prose | pages [35] -->
From all above we also notice that, all the parameters that have noticeable effect on the bathtub water temperature lead us to a better strategy. Combination of all the parameter will give us a great environment for bath. Also, it is happy to find that changing the parameter in a reasonable range will not do great harm to the final result, and the heating system is stable under most circumstances.

<!-- b000537 | heading | pages [35] -->
6.2 Sensitivity analysis for BWP

<!-- b000538 | prose | pages [35] -->
In the BWP model, the required hot flow is right corresponding to the total heat loss. As a result, we can research this criteria by observing the temperature-variation curve of the bathtub water. After finishing building the model with some fixed parameters, we look back to consider some more condition: different surface area of the bathtub, different volume of the bathtub, different material of the bathtub and different volume of person in the bathtub. Then we analyze the result below.

<!-- b000539 | furniture | pages [36] -->
Team #48649                                                              Page 35 of 44

<!-- b000540 | heading | pages [36] -->
6.2.1 Different surface area of the bathtub

<!-- b000541 | prose | pages [36] -->
Temperature curve with different surface area of the bathtub 318 s=1.4m2 316 s=1.5m2 s=1.53m2 314 s=1.6m2 s=1.7m2 312 Temperature/K 310

<!-- b000542 | prose | pages [36] -->
308

<!-- b000543 | prose | pages [36] -->
306

<!-- b000544 | prose | pages [36] -->
304

<!-- b000545 | prose | pages [36] -->
302

<!-- b000546 | prose | pages [36] -->
300 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000547 | prose | pages [36] -->
Graph 23: Temperature curve with different surface area of the bathtub We try 5 different surface areas of the bathtub, and change the corresponding volume. Then we get the temperature-variation curve by simulating them all. From Graph 23 we can easily find that: the surface area of the bathtub have very small effect on the total heat loss. The model is stable with the surface area of the bathtub.

<!-- b000548 | prose | pages [36] -->
It is reasonable to get this result because both in our model and in the real world, heat loss by the bathtub is much smaller than that by air-water convention.

<!-- b000549 | furniture | pages [37] -->
Team #48649                                                              Page 36 of 44

<!-- b000550 | heading | pages [37] -->
6.2.2 Different volume of the bathtub

<!-- b000551 | prose | pages [37] -->
Temperature curve with different volume of the bathtub 318 V=230L 316 V=270L V=300L 314 V=320L V=350L 312 Temperature/K 310

<!-- b000552 | prose | pages [37] -->
308

<!-- b000553 | prose | pages [37] -->
306

<!-- b000554 | prose | pages [37] -->
304

<!-- b000555 | prose | pages [37] -->
302

<!-- b000556 | prose | pages [37] -->
300

<!-- b000557 | prose | pages [37] -->
298 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000558 | prose | pages [37] -->
Graph 24: Temperature curve with different volume area of the bathtub

<!-- b000559 | prose | pages [37] -->
We try 5 different volume of the bathtub, and change the corresponding surface areas. Then we get the temperature-variation curve by simulating them all. From Graph 24 we can easily find that: compared with the surface area of the bathtub, the velocity have larger effect on the total heat loss. But after 10 hours the largest variation can just around 4K. The larger the volume, the slower the heat loss.

<!-- b000560 | prose | pages [37] -->
This result can be easily understood that: the volume of the bathtub (in this paper, the volume can also be regarded as the cubage) represents the volume of water. It is a common sense that a large amount of water refrigerate slow, and here it is also the case.

<!-- b000561 | furniture | pages [38] -->
Team #48649                                                              Page 37 of 44

<!-- b000562 | heading | pages [38] -->
6.2.3 Different material of the bathtub

<!-- b000563 | prose | pages [38] -->
Temperature curve with different material of the bathtub 318 cast iron λ=42 316 acrylic λ=1.4 steel λ=36 porcelain λ=0.87 314 wood λ=0.38 312 Temperature/K 310

<!-- b000564 | prose | pages [38] -->
308

<!-- b000565 | prose | pages [38] -->
306

<!-- b000566 | prose | pages [38] -->
304

<!-- b000567 | prose | pages [38] -->
302

<!-- b000568 | prose | pages [38] -->
300 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000569 | prose | pages [38] -->
Graph 25: Temperature curve with different material of the bathtub

<!-- b000570 | prose | pages [38] -->
We try 5 different material of the bathtub. Then we get the temperature-variation curve by simulating them all. From Graph 25 we can easily find that: the material of the bathtub have very small effect on the total heat loss. The model is stable with the material of the bathtub.

<!-- b000571 | prose | pages [38] -->
It is because of the same reason as the surface area of the bathtub that heat loss by the bathtub is much smaller than that by air-water convention.

<!-- b000572 | furniture | pages [39] -->
Team #48649                                                              Page 38 of 44

<!-- b000573 | heading | pages [39] -->
6.2.4 Different volume of person in the bathtub

<!-- b000574 | prose | pages [39] -->
Temperature curve with different volume of person 318 V=30L 316 V=40L V=50L V=60L 314 V=75L 312 Temperature/K 310

<!-- b000575 | prose | pages [39] -->
308

<!-- b000576 | prose | pages [39] -->
306

<!-- b000577 | prose | pages [39] -->
304

<!-- b000578 | prose | pages [39] -->
302

<!-- b000579 | prose | pages [39] -->
300 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000580 | prose | pages [39] -->
Graph 26: Temperature curve with different volume of person

<!-- b000581 | prose | pages [39] -->
We try 5 different volume of the people in the bathtub. Then we get the temperature- variation curve by simulating them all. From Graph 26 we can easily find that: the material of the bathtub have larger effect on the total heat loss than the surface or the material of the bathtub. But is holds smaller effect than that of the volume of the bathtub. The larger the volume, the faster the heat loss is.

<!-- b000582 | prose | pages [39] -->
It is because of the same reason as the volume of the bathtub that a large amount of water refrigerate slow, and here the difference between volume of bathtub and that of people is just the volume of water.

<!-- b000583 | heading | pages [39] -->
6.2.5 Conclusion

<!-- b000584 | prose | pages [39] -->
As we consider various different conditions and analyze the result we can conclude that:

<!-- b000585 | prose | pages [39] -->
 The system under this model is fairly stable with different variables.

<!-- b000586 | prose | pages [39] -->
 The volume of water is particularly an important influential factor on the heat loss.

<!-- b000587 | prose | pages [39] -->
This tells us that, with the bathtub volume fixed, we can give fairly stable evaluation on the system and also the best strategy for the user to enjoy their bath experience.

<!-- b000588 | furniture | pages [40] -->
Team #48649                                                              Page 39 of 44

<!-- b000589 | heading | pages [40] -->
7 Model for Cleansing with a Bubble Bath Additive (CBBA model)

<!-- b000590 | prose | pages [40] -->
If the person used a bubble bath additive while initially filling the bathtub to assist in cleansing, then the heat dissipation through the water and the air will be influenced by the bubble layer. Thus we expand the CBBA model based on BWP model. As Graph 27 shows, we modeled the bubble layer as a kind of porous medium that locates between the water surface and the air.

<!-- b000591 | prose | pages [40] -->
Graph 27: The diagram of the bubble layer

<!-- b000592 | prose | pages [40] -->
 The medium has a different heat transfer coefficient . The heat transfer process between bub

<!-- b000593 | prose | pages [40] -->
the water and the air through the air can be modeled as a heat conduction process. The heat conduction:

<!-- b000594 | prose | pages [40] -->
 t t   water bub Q A (7.1) bub bub bub d bub

<!-- b000595 | prose | pages [40] -->
Q : Heat loss through the water surface by the bubble layer in unit time bub

<!-- b000596 | prose | pages [40] -->
A sA . : The surface area of the bubble layer, which should be equal to the water surface bub

<!-- b000597 | prose | pages [40] -->
t t : The upper surface temperature of the bubble layer, which can be equal to air . bub

<!-- b000598 | prose | pages [40] -->
d : The thickness of the bubble layer. bub

<!-- b000599 | prose | pages [40] -->
 We change the heat transfer coefficient and get the total heat dissipation in natural bub

<!-- b000600 | prose | pages [40] -->
cooling process as Graph 28 shows:

<!-- b000601 | furniture | pages [41] -->
Team #48649                                                              Page 40 of 44

<!-- b000602 | prose | pages [41] -->
Temperature curve of bubble model 318 λ=0.5 316 λ=0.7 λ=1 314

<!-- b000603 | prose | pages [41] -->
312 Temperature/K 310

<!-- b000604 | prose | pages [41] -->
308

<!-- b000605 | prose | pages [41] -->
306

<!-- b000606 | prose | pages [41] -->
304

<!-- b000607 | prose | pages [41] -->
302

<!-- b000608 | prose | pages [41] -->
300 0 100 200 300 400 500 600 700 800 900 1000 Time/min

<!-- b000609 | prose | pages [41] -->
 Graph 28: Temperature curve of bubble model with different heat transfer coefficient bub

<!-- b000610 | prose | pages [41] -->
From the graph we can see the heat dissipation becomes slower with the bubble layer on

<!-- b000611 | prose | pages [41] -->
 the surface of the water. It is also clear that the dissipation rate becomes high as goes bub

<!-- b000612 | prose | pages [41] -->
up. In other words, the bubble layer can be regarded as a thermal insulation layer.

<!-- b000613 | heading | pages [41] -->
8 Weakness and Strength

<!-- b000614 | prose | pages [41] -->
Like any model, our model has its own strengths and weaknesses. Some of major points are presented below.

<!-- b000615 | heading | pages [41] -->
8.1 Strengths

<!-- b000616 | prose | pages [41] -->
 BWOP simulation using FEM by ANSYS returns very specific temperature distribution.

<!-- b000617 | prose | pages [41] -->
Our BWOP model use FEM by ANSYS to simulate the 3-D flow field heat convection.

<!-- b000618 | prose | pages [41] -->
Instead just working out some boundary formulas to get a theoretical result, ANSYS provides strong function to simulate the heat conduction between many finite elements.

<!-- b000619 | prose | pages [41] -->
The result presents a clear temperature distribution with isothermal diagram and the statistical data. It can not only show us the temporary temperature of the water but to show the gradient visually. Even in BWP model, we use this method to simulate the temperature distribution across people’s body surface.

<!-- b000620 | prose | pages [41] -->
 Simplification of complexed thermal system by BWP model.

<!-- b000621 | prose | pages [41, 42] -->
The temperature of the water in bathtub can be simulated statically, however, if someone is in the bathtub, then the system becomes abstrusely complexed to solve. Considering people’s motility, which is both a bad and a great condition, we can simplify the water model to a homogeneous body where temperature is the same everywhere. Using this simplification we can do many simulation and calculations. Due to people’s motility, this assumption is reasonable.  Offering discrete inflow model to reach a more realistic and operable result.

<!-- b000622 | furniture | pages [42] -->
Team #48649                                                              Page 41 of 44

<!-- b000624 | prose | pages [42] -->
Apart adding from a constant trickle of hot water, we propose anther discrete strategy to adjust the temperature. As is always the case, people can’t control the inflow velocity precisely. Then the discrete approach offers users with a lazy and operable strategy.

<!-- b000625 | prose | pages [42] -->
According to our experiment, the discrete approach can also make the water waste less.

<!-- b000626 | heading | pages [42] -->
8.2 Weaknesses

<!-- b000627 | prose | pages [42] -->
 Some assumptions are not accurate enough.

<!-- b000628 | prose | pages [42] -->
 The 3th assumption tells that the volume of the air is infinite and the temperature of the air keeps constant. But in a bathroom in real world, air close to the surface of hot water must have higher temperature, and that difference have an influence on the heat convection between water and air.

<!-- b000629 | prose | pages [42] -->
 The 4th assumption tells that the temperature can be evenly distributed in bathtub at any time when a person is in it. It is a great way to take this condition as an assumption to simplify the model. But is inevitably decrease the precision of the model. Different temperature attributions leads to different heat convections and also different final result.

<!-- b000630 | prose | pages [42] -->
 The 5th assumption tells that there doesn’t exist heat convection in the water when a person is in the bathtub (BWP model). It is also a great way to take this condition as an assumption to simplify the model. But this assumption changes the heat convection to heat conduction. Some deviation must appear in this process.

<!-- b000631 | furniture | pages [43] -->
Team #48649                                                              Page 42 of 44

<!-- b000632 | heading | pages [43] -->
References

<!-- b000633 | references | pages [43] -->
[1]Gray, D.D., and Giorgin, A., The Validity of the Boussinesqe Approximation for Liquids and Gases

<!-- b000634 | references | pages [43] -->
[M], Int.J.Heat Mass Transfer, 1976, 19: 545-551

<!-- b000635 | references | pages [43] -->
[2]http://www.biocab.org/Heat_Transfer.html

<!-- b000636 | references | pages [43] -->
[3]https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_constant

<!-- b000637 | references | pages [43] -->
[4]http://a.hiphotos.baidu.com/zhidao/pic/item/8ad4b31c8701a18b5f381c2c9f2f07082938fe86.jpg?q

<!-- b000638 | references | pages [43] -->
q-pf-to=pcqq.c2c

<!-- b000639 | references | pages [43] -->
[5]https://en.wikipedia.org/wiki/Prandtl_number

<!-- b000640 | references | pages [43] -->
[6]https://en.wikipedia.org/wiki/Heat_transfer#cite_note-15

<!-- b000641 | references | pages [43] -->
[7]https://en.wikipedia.org/wiki/Finite_element_method

<!-- b000642 | references | pages [43] -->
[8]https://en.wikipedia.org/wiki/Ansys#ANSYS_CFD.2C_CFX

<!-- b000643 | references | pages [43] -->
[9]Abbott, J.M. Smith, H.C. Van Ness, M.M. (2005). Introduction to chemical engineering

<!-- b000644 | references | pages [43] -->
thermodynamics (7th ed.). Boston ; Montreal: McGraw-Hill. ISBN 0-07-310445-0

<!-- b000645 | references | pages [43] -->
[10]J.P.Holman，Heat Transfer 1990 ISBN-13: 978-0079093882

<!-- b000646 | furniture | pages [44] -->
Team #48649                                                              Page 43 of 44

<!-- b000647 | heading | pages [44] -->
Appendix

<!-- b000648 | prose | pages [44] -->
Enjoying Making Your Own Spa-type Bathtub

<!-- b000649 | prose | pages [44] -->
To all interested users

<!-- b000650 | prose | pages [44] -->
Have you ever suffered from the cooling water as you are enjoying the bath?

<!-- b000651 | prose | pages [44] -->
Have you ever dreamed about owning you own spa-type bathtub?

<!-- b000652 | prose | pages [44] -->
That is not a dream now! Taking several simple steps to make you own it now!

<!-- b000653 | prose | pages [44] -->
At first, find a pipe to draw hot water from faucet to the bottom of the bathtub which is opposite to the overflow drain. It is well recommended to be the bottom to maximize the utilization of your hot water (that is the best way to reduce the heat loss). During your enjoyment, you’ve get two different way to get your suitable temperature.

<!-- b000654 | prose | pages [44] -->
Strategy 1: If you want to have a sound sleep while enjoying your bath, then you’d better choose this strategy. Take a relatively long time to adapt your bathtub to our model, then you will get exact inflow per second for a given temperature (don’t worry about the complexity, you will just need to do this for ONE time). Set your faucet to get the given flow velocity (this step may be a little bit hard), then you may enjoy your sound sleep in warm water.

<!-- b000655 | prose | pages [44] -->
Strategy 2: If you feel troublesome to adapt to the model or you just don’t want to set the faucet precisely every time, it is OK for strategy 2. In this way, you don’t even need to know any parameter about your own bathtub and your faucet. Adjusting the faucet to guarantee the water from which will not be too hot to bear. Then maximize the flow until the bathtub get a little bit hot. Stop the faucet and enjoy your bath for a period of time until you feel a little bit cold. Repeat the operations and you can easily enjoy your bathing time.

<!-- b000656 | prose | pages [44] -->
Note 1: You may have to serious on the temperature of water from the faucet just to avoid scald. For Strategy 1, you’d better choose a temperature that you won’t feel very hot to keep your bathtub warm, or you may suffer from the hottest region during your sleep. For Strategy 2, it is OK to choose a higher temperature in order to reheat your bathtub fast, but you have to agitate the water rapidly to make the temperature distribute evenly.

<!-- b000657 | prose | pages [44] -->
Note 2: Pay attention to the temperature distribution if you want to stay still to recover from fatigue. The water somewhere mat not be warm as you think such that the hottest region must be around the pipe and the top surface of the water is commonly relatively cold. It takes time for heat to transfer from hot water to cold water, and during this period of time, the air cools the top surface. So it is really hard for our strategy to keep an evenly maintained temperature. You may just twist for a while to get them mixed to solve the problem. Be sure to remember this.
