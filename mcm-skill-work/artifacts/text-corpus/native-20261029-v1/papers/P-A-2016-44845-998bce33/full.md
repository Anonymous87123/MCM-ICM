# P-A-2016-44845-998bce33

Status: machine-draft; not source-verified.


<!-- b000001 | heading | pages [1] -->
2016 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000002 | title | pages [1] -->
Beneath the Surface: A Thermal-Fluid

<!-- b000003 | title | pages [1] -->
Analysis of a Hot Bath

<!-- b000004 | prose | pages [1] -->
The overall temperature and uniformity of heat distribution are crucial to the enjoyment of a hot bath. Over time, a bath will lose heat to its surroundings; how- ever, the temperature can be eﬀectively controlled by adding a trickle of hot water. Quantifying the optimal method of restoring heat uniformly will be the subject of this paper.

<!-- b000005 | prose | pages [1] -->
By making key assumptions, we reduce the problem to one spatial dimension with three-dimensional heat transfer considerations. We develop three independent, generic mathematical models to describe the temperature distribution of the bathtub in space and time:

<!-- b000006 | prose | pages [1] -->
• Steady State, Uniform, Thermodynamic Model: We characterize the energy and mass interactions between the system and the surroundings, deriv- ing key physical constants used in the subsequent models.

<!-- b000007 | heading | pages [1] -->
• Analytical Model: Using Fourier analysis we derive an analytical solution

<!-- b000008 | prose | pages [1] -->
to the one-dimensional heat equation with time dependent Neumann boundary conditions and temporally and spatially dependent heat generation/loss.

<!-- b000009 | prose | pages [1] -->
• Numerical Model: Using a ﬁnite diﬀerence approximation of the one-dimensional convection-diﬀusion equation, we implement an algorithm that estimates the temperature distribution over time based on bulk ﬂuid motion and diﬀusion.

<!-- b000010 | prose | pages [1] -->
We analyze the results of each of these models, performing sensitivity analyses on the input parameters and demonstrating their ﬂexibility. Ultimately, the numerical model proves the most physically accurate as it models convective ﬂuid motion, which is found to dominate thermal diﬀusion. We then implement closed-loop PID control to regulate the total thermal energy of the system. We also model an intelligent strategy for inlet water distribution in order to achieve temperature uniformity.

<!-- b000011 | prose | pages [1] -->
Ultimately, our model demonstrates that using well-tuned PID control of input water temperature and evenly distributing this water upstream of the bather quickly achieves a uniform objective temperature while conserving water.

<!-- b000012 | heading | pages [2] -->
Contents

<!-- b000013 | contents | pages [2] -->
1

<!-- b000014 | heading | pages [2] -->
Introduction

<!-- b000015 | prose | pages [2] -->
3 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Nomenclature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Simplifying Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000016 | prose | pages [2] -->
2 Geometric Considerations

<!-- b000017 | prose | pages [2] -->
3 Thermodynamic Considerations

<!-- b000018 | prose | pages [2] -->
5

<!-- b000019 | prose | pages [2] -->
6

<!-- b000020 | prose | pages [2] -->
7 Properties of Water . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 Heat Transfer Coeﬃcients 7

<!-- b000021 | heading | pages [2] -->
Nominal Values Used in Model Simulations

<!-- b000022 | prose | pages [2] -->
4 10

<!-- b000023 | heading | pages [2] -->
A Steady State, Uniform Temperature Model

<!-- b000024 | prose | pages [2] -->
5 11 Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 11 Implementation and Results . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 13

<!-- b000025 | heading | pages [2] -->
An Analytical Model of the Heat Equation

<!-- b000026 | prose | pages [2] -->
6 14 Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 14 Implementing the Analytical Model . . . . . . . . . . . . . . . . . . . . . . . 6.2 18 Basic Results and Veriﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 18

<!-- b000027 | heading | pages [2] -->
A Numerical Model of Convection-Diﬀusion

<!-- b000028 | prose | pages [2] -->
7 22 Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 22 Basic Results and Veriﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 24 Modeling Bather Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3

<!-- b000029 | prose | pages [2] -->
8

<!-- b000030 | heading | pages [2] -->
Model Comparison

<!-- b000031 | prose | pages [2] -->
26

<!-- b000032 | prose | pages [2] -->
27 Solution Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 27 Eﬀect of Bathtub Geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 28 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.3 Eﬀect of Adding Soap 30 Eﬀect of Varied Input Temperature and Flow Rate 8.4 . . . . . . . . . . . . . .

<!-- b000033 | prose | pages [2] -->
31 Eﬀect of Varied Size and Position of Bather 8.5

<!-- b000034 | prose | pages [2] -->
9 Control Theory and Implementation

<!-- b000035 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000036 | prose | pages [2] -->
33

<!-- b000037 | prose | pages [2] -->
34 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 PID Control Theory 34 Implementation of PID Control in Numerical Model . . . . . . . . . . . . . . 9.2 35 Control of Uniformity of Water Temperature Distribution . . . . . . . . . . . 9.3 37 Final PID Control with With Manual Heat Distribution 9.4

<!-- b000038 | heading | pages [2] -->
10 Final Remarks

<!-- b000039 | prose | pages [2] -->
. . . . . . . . . . .

<!-- b000040 | prose | pages [2] -->
39

<!-- b000041 | prose | pages [2] -->
40 10.1 Strengths and Weaknesses of Solution Models . . . . . . . . . . . . . . . . .

<!-- b000042 | prose | pages [2] -->
40 . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.2 Future Model Development 42 10.3 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | prose | pages [2] -->
42

<!-- b000044 | furniture | pages [2] -->
2

<!-- b000045 | furniture | pages [2] -->
2

<!-- b000046 | furniture | pages [3] -->
Team # 44845

<!-- b000047 | furniture | pages [3] -->
Page 3 of 44

<!-- b000048 | prose | pages [3] -->
1

<!-- b000049 | heading | pages [3] -->
Introduction

<!-- b000050 | prose | pages [3] -->
1.1 Overview

<!-- b000051 | prose | pages [3] -->
eat transfer and ﬂuid ﬂow are notoriously diﬃcult physical mechanisms to accurately

<!-- b000052 | prose | pages [3] -->
H

<!-- b000053 | prose | pages [3] -->
model. Over the years, much time and energy has been devoted to obtaining general solutions to these types of problems, but this eﬀort has proven largely unsuccessful. In this paper, we will analyze a speciﬁc application of heat transfer and ﬂuid mechanics: modeling the temperature distribution in a bathtub in space and time. The speciﬁc scenario is as follows:

<!-- b000054 | prose | pages [3] -->
Our friend Joseph Fourier (hereafter Joe) decides to take a warm bath and ﬁlls his bathtub to the desired temperature. After a while, he notices that the water is cooler than it was initially, and he wishes to increase the temperature by adding a trickle of warm water but does not want to disturb the uniformity of the temperature distribution in space. What should he do to most eﬀectively regain the initial temperature while keeping the temperature uniform throughout and not wasting too much water? What if he wished to eliminate the problem altogether by beginning to add water as soon as he got in the bath?

<!-- b000055 | prose | pages [3] -->
In this paper, we attempt to answer these questions for Joe. We present our mathematical models describing the temperature distribution in a bathtub in space and time. We describe the relevant physical mechanisms, mathematical development, implementation, and results of each model independently. Then, we compare the results of each model in order to evaluate their accuracy and explore the best solution for Joe. Finally, we present the strengths and weaknesses of our models and discuss ideas for future development of an ideal strategy.

<!-- b000056 | prose | pages [3] -->
1.2

<!-- b000057 | heading | pages [3] -->
Nomenclature

<!-- b000058 | prose | pages [3] -->
We begin by deﬁning a list of nomenclature (symbols) used in this report:

<!-- b000059 | prose | pages [3] -->
Abbreviation Description a Boundary condition at faucet b Boundary condition at overﬂow drain cp Speciﬁc heat Esystem Energy of a system f Controls forcing function g Gravitational acceleration GrL Grashof number h Enthalpy hb Convection heat transfer coeﬃcient through bottom surface hconv Convection heat transfer coeﬃcient ht Convection heat transfer coeﬃcient through top surface hw Convection heat transfer coeﬃcient through the walls H Height of bathtub i Spatial index variable j Temporal index variable

<!-- b000060 | furniture | pages [3] -->
3

<!-- b000061 | furniture | pages [4] -->
Team # 44845

<!-- b000062 | furniture | pages [4] -->
Page 4 of 44

<!-- b000063 | prose | pages [4] -->
Abbreviation Description k Thermal conductivity Kd Derivative gain constant Ki Integral gain constant Kp Proportional gain constant L Length of bathtub Lc Characteristic length m Mass n Summation index variable Nu Nusselt number p Perimeter Pe P´eclet number Pr Prandtl number Q Heat generation ˜Q Shifted heat generation RaL Rayleigh number ReL Reynolds number t Time u Temperature uavg Average temperature uin Inlet water temperature uobj Objective water temperature us Surface temperature u Diﬀerence between average and objective temperature u∞ Air temperature U Shifted temperature distribution v Flow Velocity W Width of bathtub x Length direction y Width direction z Height direction α Thermal diﬀusivity β Volume expansion coeﬃcient ϵ Porosity η Fraction of input heat to be redistributed ν Kinematic viscosity σ Standard deviation from average temperature φ Initial condition ˜φ Shifted initial condition ρ Density

<!-- b000064 | furniture | pages [4] -->
4

<!-- b000065 | furniture | pages [5] -->
Team # 44845

<!-- b000066 | furniture | pages [5] -->
Page 5 of 44

<!-- b000067 | prose | pages [5] -->
1.3

<!-- b000068 | heading | pages [5] -->
Simplifying Assumptions

<!-- b000069 | prose | pages [5] -->
All of our models rely on a set of key assumptions that make the problem solvable in a concise manner. The assumptions that are used in every model are summarized below. The additional assumptions for each individual model will be detailed along with the introduction and description of that model.

<!-- b000070 | prose | pages [5] -->
• The faucet of the bathtub is placed exactly at one end of the length of the bathtub with the overﬂow drain exactly at the opposite end.

<!-- b000071 | prose | pages [5] -->
• When Joe is in the bathtub it is full. Any addition of water results immediately in a drainage of the same volume.

<!-- b000072 | prose | pages [5] -->
• The bathtub is free-standing, i.e. it is surrounded by air on all sides.

<!-- b000073 | prose | pages [5] -->
• The bathtub itself is in thermal equilibrium with the water at all times. Thus, the interface with the ambient air on all sides can be described without a separate knowl- edge of the temperature distribution within the bathtub material or the heat capacity of the bathtub.

<!-- b000074 | prose | pages [5] -->
• All radiation eﬀects are ignored. The only mechanism of stationary heat transfer is convection.

<!-- b000075 | prose | pages [5] -->
• The ambient air temperature is constant in space and time, i.e. the surroundings can be modeled as a thermal reservoir.

<!-- b000076 | prose | pages [5] -->
• The ambient air can be modeled as a stationary ideal gas at 1 bar ≈1 atm.

<!-- b000077 | prose | pages [5] -->
• No water loss due to evaporation occurs, i.e. the volume of water in the tub remains constant and the surface of the water interacts directly with dry air.

<!-- b000078 | prose | pages [5] -->
• The presence of the subject in the bathtub provides only thermal eﬀects. There is no disturbance to the ﬂow caused by the subject.

<!-- b000079 | prose | pages [5] -->
• The ﬂow is uniform, laminar, incompressible, inviscid, and quasi one-dimensional.

<!-- b000080 | prose | pages [5] -->
• Water has constant density and constant speciﬁc heat, and remains in liquid form.

<!-- b000081 | prose | pages [5] -->
• All material properties are assumed to be isotropic.

<!-- b000082 | prose | pages [5] -->
As was stated previously, additional assumptions will be described throughout the paper.

<!-- b000083 | furniture | pages [5] -->
5

<!-- b000084 | furniture | pages [6] -->
Team # 44845

<!-- b000085 | furniture | pages [6] -->
Page 6 of 44

<!-- b000086 | prose | pages [6] -->
2 Geometric Considerations

<!-- b000087 | prose | pages [6] -->
We begin by deﬁning the geometry of the bathtub. The bathtub will be considered as a rectangular prism, with dimensions equal to L, W, and H as shown below in Figure 1.

<!-- b000088 | caption | pages [6] -->
Figure 1: Bathtub Geometry

<!-- b000089 | prose | pages [6] -->
There are six rectangular faces: ﬁve composed of the bathtub material and one face exposed to ambient air. The x direction is taken to be in the length of the bathtub, and y and z describe width and height directions respectively. The faucet is located at x = 0 and the drain is located at x = L. Any time that we add water to the system through the faucet, an equal volume exits through the overﬂow drain based on the assumption that the bathtub is full. Physically, modeling the temperature throughout the bathtub is a three-dimensional problem, which complicates the analysis greatly. As we consider partial diﬀerential equations (PDEs) with spatial and temporal dependence, simplifying geometric assumptions will be made in order to make the problem more approachable.

<!-- b000090 | prose | pages [6] -->
The mechanisms of heat transfer and ﬂuid ﬂow within the water will be assumed to be solely in the x direction. The temper- ature within a cross-section parallel to the yz plane will be assumed to be uniform, and can be thought of as an average temperature over that cross-section. This cross section, with volume WH∆x, is shown at right.

<!-- b000091 | prose | pages [6] -->
These two assumptions allow the three- dimensional problem within the water to be

<!-- b000092 | caption | pages [6] -->
Figure 2: Cross-sectional Fluid Element

<!-- b000093 | prose | pages [6] -->
reduced to one dimension.

<!-- b000094 | prose | pages [6] -->
Heat capacity, ﬂuid ﬂow velocity, heat loss to the surround- ings, and other extensive properties of the system will retain their three dimensional nature, resulting in a ﬁnal geometric model that is fundamentally one-dimensional, but with impor- tant three-dimensional eﬀects preserved. The details of this preservation will be presented along with each individual model development.

<!-- b000095 | furniture | pages [6] -->
6

<!-- b000096 | furniture | pages [7] -->
Team # 44845

<!-- b000097 | furniture | pages [7] -->
Page 7 of 44

<!-- b000098 | prose | pages [7] -->
Thermodynamic Considerations 3

<!-- b000099 | prose | pages [7] -->
Next, we examine the key thermodynamic parameters of the problem: the speciﬁc enthalpy, speciﬁc heat, density, and thermal conductivity of water, as well as the convective heat transfer coeﬃcients from the system to the surrounding air.

<!-- b000100 | prose | pages [7] -->
3.1 Properties of Water

<!-- b000101 | prose | pages [7] -->
The speciﬁc enthalpy of water is assumed to vary linearly with temperature, with a slope equal to the speciﬁc heat.

<!-- b000102 | prose | pages [7] -->
This as- sumption was validated using property val- ues from the XSteam[1] MATLAB function, shown at right in Figure 3.

<!-- b000103 | prose | pages [7] -->
Mathematically, enthalpy (h) can be cal- culated from h = cpu, where cp is the spe- ciﬁc heat and u is the temperature. For the purposes of this paper, we will ignore the small y-intercept value and use a constant speciﬁc heat[2] of 4178 J/(kgK) based on an assumed average temperature of 30◦C.

<!-- b000104 | prose | pages [7] -->
The density and thermal conductiv- ity of water are taken to be constant at

<!-- b000105 | caption | pages [7] -->
Figure 3: Linear Enthalpy Variation

<!-- b000106 | prose | pages [7] -->
1000 kg/m3 and 0.615 W/(mK) respectively[2], based on assumed average temperatures of 30◦C.

<!-- b000107 | prose | pages [7] -->
3.2 Heat Transfer Coeﬃcients

<!-- b000108 | prose | pages [7] -->
The calculation of convective heat transfer coeﬃcients is involved and will be summarized here. Because the bathtub itself is assumed to be in thermal equilibrium with the water, only convective eﬀects with the surrounding air will be considered. To appropriately estimate the heat transfer coeﬃcient, this convection must be classiﬁed as natural (free), forced, or mixed. In particular, we must check the Grashof number (GrL) and the Reynolds number (ReL). If GrL/Re2

<!-- b000109 | prose | pages [7] -->
L >> 1, inertial forces prevail and the natural convection dominates, but

<!-- b000110 | prose | pages [7] -->
L << 1, the opposite is true and forced convection dominates. If GrL/Re2

<!-- b000111 | prose | pages [7] -->
if GrL/Re2

<!-- b000112 | prose | pages [7] -->
mixed convection must be considered[2].

<!-- b000113 | prose | pages [7] -->
L ≈1,

<!-- b000114 | prose | pages [7] -->
The formulae for these two dimensionless numbers are shown below, where v is the ﬂow velocity, L is a characteristic length (used in determination of ReL), ν is the kinematic viscosity of the air, g is the local gravitational acceleration, β is the volume expansion coeﬃcient, us and u∞are the temperatures of the surface water and air respectively, and Lc is a characteristic length (used in determination of GrL)[2].

<!-- b000115 | prose | pages [7] -->
ReL = vL

<!-- b000116 | prose | pages [7] -->
ν GrL = gβ(us −u∞)L3

<!-- b000117 | prose | pages [7] -->
c (1) ν2

<!-- b000118 | furniture | pages [7] -->
7

<!-- b000119 | furniture | pages [7] -->
7

<!-- b000120 | furniture | pages [8] -->
Team # 44845

<!-- b000121 | furniture | pages [8] -->
Page 8 of 44

<!-- b000122 | prose | pages [8] -->
As a ﬁrst order approximation, we take L = 1.5 m as the length of the bathtub in the ﬂow direction, ν = 1.608×10−5 m2/s for air at a ﬁlm temperature of 30◦C (a rough estimate of an expected ﬁlm temperature)[2], us = 40◦C, u∞= 20◦C (rough estimates of the tub and room temperatures respectively), and g = 9.81 m/s2. The ﬂow velocity v is slightly more involved to compute. First, we model the water ﬂowing under the air as air ﬂowing over the water, an equivalent model. Assuming a mass ﬂow rate of 0.06 kg/s (about 1 gallon per minute, a rough estimate of a “trickle”), a bathtub height H = 0.5 m, a bathtub width of W = 1 m, and uniform, laminar ﬂow from the x = 0 face to the x = L face, the ﬂow velocity can be computed as follows:

<!-- b000123 | prose | pages [8] -->
˙m 0.06 kg/s (1000 kg/m3)(1 m)(0.5 m) = 1.2 × 10−4 m/s ˙m = ρvA ⇒v = ρWH = (2)

<!-- b000124 | prose | pages [8] -->
For a ﬂat plate of water, Lc = As/p, the ratio of the surface area to the perimeter[2]. In our case, Lc = (1.5 m)(1 m)/(2(1.5 m+1 m)) = 0.3 m. Finally, assuming that air is an ideal gas[2], β = 1/T∞= 1/293.15 K = 0.003411 K−1.

<!-- b000125 | prose | pages [8] -->
Using these values in the formulae presented in Equation 1, we obtain ReL ≈11.19 and GrL ≈70000000. The ratio of interest GrL/Re2

<!-- b000126 | prose | pages [8] -->
L ≈558000 >> 1, so natural convection eﬀects signiﬁcantly dominate. Thus, forced convection will be ignored. Even if our rough estimates are slightly incorrect, natural convection should dominate because the ratio is much larger than unity.

<!-- b000127 | prose | pages [8] -->
Now, we are able to estimate the convective heat transfer coeﬃcients. The determination of these coeﬃcients for a natural convection problem is complicated, but will be summarized brieﬂy here. First, the Rayleigh number must be determined. This number, RaL, is the product of the Grashof and Prandtl numbers and describes the ratio of buoyancy forces to thermal and momentum diﬀusivities. The determination of the Grashof number is shown above, and the Prandtl number, Pr, is a property of the air based on ﬁlm temperature[2].

<!-- b000128 | prose | pages [8] -->
Once the Rayleigh number is determined, the Nusselt number, Nu, can be found based on the geometry of the natural convection. In our case, there are six surfaces with three independent geometries. Four of the surfaces (the sides) are modeled as vertical plates, one of the surfaces (the top) is modeled as a ﬂat plate with the hotter side facing up, and one of the surfaces (the bottom) is modeled as a ﬂat plate with the hotter side facing down. Due to the complicated physics of natural convection, these three geometries will have separate heat transfer coeﬃcients. Depending on the magnitude of the Rayleigh number and the geometry, the Nusselt number can be determined as follows[2].

<!-- b000129 | prose | pages [8] -->
(

<!-- b000130 | prose | pages [8] -->
104 < RaL < 107 0.54Ra1/4

<!-- b000131 | prose | pages [8] -->
Top:

<!-- b000132 | prose | pages [8] -->
Nut =

<!-- b000133 | prose | pages [8] -->
L L

<!-- b000134 | prose | pages [8] -->
107 < RaL < 1011 0.15Ra1/3 L L

<!-- b000135 | prose | pages [8] -->
105 < RaL < 1011

<!-- b000136 | prose | pages [8] -->
Nub = 0.27Ra1/4 Bottom:

<!-- b000137 | prose | pages [8] -->


<!-- b000138 | prose | pages [8] -->
Wall:

<!-- b000139 | prose | pages [8] -->
Nuw =

<!-- b000140 | prose | pages [8] -->
0.825 + 

<!-- b000141 | prose | pages [8] -->
(3) L

<!-- b000142 | prose | pages [8] -->
2

<!-- b000143 | prose | pages [8] -->


<!-- b000144 | prose | pages [8] -->
0.387Ra1/6 L

<!-- b000145 | prose | pages [8] -->
Entire range

<!-- b000146 | prose | pages [8] -->


<!-- b000147 | prose | pages [8] -->
1 + (0.492/Pr)9/168/27

<!-- b000148 | prose | pages [8] -->


<!-- b000149 | prose | pages [8] -->


<!-- b000150 | furniture | pages [8] -->
8

<!-- b000151 | furniture | pages [8] -->
8

<!-- b000152 | furniture | pages [9] -->
Team # 44845

<!-- b000153 | furniture | pages [9] -->
Page 9 of 44

<!-- b000154 | prose | pages [9] -->
At long last, the heat transfer coeﬃcient hconv can be determined from hconv =Nuk/L, where k is the thermal conductivity of the air[2]. In practice, each thermodynamic constant of air is dependent upon the temperature, so there is no explicit solution to these equations. Rather, a system temperature must be guessed and the validity of the guess evaluated. Assuming an air temperature of 20◦C, the variation of ht with water temperature is shown below in Figure 4.

<!-- b000155 | caption | pages [9] -->
Figure 4: Variation of ht with Water Temperature

<!-- b000156 | prose | pages [9] -->
As shown by the above ﬁgure, the heat transfer coeﬃcient does vary with temperature of water, as was expected. For the range of temperatures anticipated in the bath water, how- ever, this variation is relatively small. Similarly, the variation of hb with system temperature is shown below.

<!-- b000157 | caption | pages [9] -->
Figure 5: Variation of hb with Water Temperature

<!-- b000158 | furniture | pages [9] -->
9

<!-- b000159 | furniture | pages [10] -->
Team # 44845

<!-- b000160 | furniture | pages [10] -->
Page 10 of 44

<!-- b000161 | prose | pages [10] -->
As with ht, this coeﬃcient varies only slightly with system temperature within expected bounds. It is interesting to note that the magnitude of the coeﬃcient is lower than for the top surface; this is due to the decreased heat loss through natural convection when the hot bathtub is above the colder air. Finally, the same analysis is shown for hw.

<!-- b000162 | caption | pages [10] -->
Figure 6: Variation of hw with Water Temperature

<!-- b000163 | prose | pages [10] -->
Once again, the coeﬃcient varies only slightly with temperature.

<!-- b000164 | prose | pages [10] -->
The magnitude of the heat transfer coeﬃcient from the walls is between those of the bottom and top surfaces, demonstrating that natural convection is slightly more eﬃcient from vertical walls than from face-down plates, but not as eﬃcient as from face-up plates. In complicated models, it is not realistic to use an iterative numerical method, so the heat transfer coeﬃcients will be taken as their mean value and assumed to not be functions of temperature.

<!-- b000165 | prose | pages [10] -->
4

<!-- b000166 | heading | pages [10] -->
Nominal Values Used in Model Simulations

<!-- b000167 | prose | pages [10] -->
Before describing our ﬁrst model, we must deﬁne the nominal values of each parameter to be used in simulations. In order to conduct reliable analysis of the impact of any one parameter on the solution, we use nominal values of the other parameters. This allows us to examine the eﬀect of a single parameter at a time. The following table contains the model parameters that can be altered as well as their nominal values.

<!-- b000168 | furniture | pages [10] -->
10

<!-- b000169 | furniture | pages [11] -->
Team # 44845

<!-- b000170 | prose | pages [11] -->
Parameter Description L Bath Length W Bath Width H Bath Height ˙m Mass Flow Rate uin Input Water Temp. Lbody Body Length cbody Body Circumference ubody Body Temperature

<!-- b000171 | furniture | pages [11] -->
Page 11 of 44

<!-- b000172 | prose | pages [11] -->
Nominal Value 1.5 m 1 m 0.5 m 0.05 kg/s 45◦C 1 m 0.5 m 37◦C Position of Body Center Xbody 0.75 m 43 W/(m2K) [3] Heat Transfer Coeﬀ. of Body hbody 20◦C Surroundings Temperature u∞ 37◦C Initial Water Temperature u0 k Thermal Conductivity Water Density ρ 0.615 W/(mK) [2] 1000 kg/m3 [2] Speciﬁc Heat Capacity cp 4178 J/(kgK) [2] 4.692 W/(m2K) Heat Transfer Coeﬀ. of Top ht 1.934 W/(m2K) Heat Transfer Coeﬀ. of Bottom hb 3.804 W/(m2K) Heat Transfer Coeﬀ. of Wall hw Time of Bath t 1 hr

<!-- b000173 | heading | pages [11] -->
A Steady State, Uniform Temperature Model

<!-- b000174 | prose | pages [11] -->
5

<!-- b000175 | prose | pages [11] -->
5.1 Theory

<!-- b000176 | prose | pages [11] -->
We now move from deﬁning the geometry and thermodynamic parameters of the prob- lem to developing models for its solution.

<!-- b000177 | prose | pages [11] -->
As an initial model, the temperature in the bathtub is assumed to be uniform and steady. This allows the analysis to be sim- ply derived from the First Law of Thermo- dynamics. The system will be only the water in the bathtub, and the surroundings will be composed of the inlet, the exit, the bather, and the ambient air. This is shown in Figure 7 at right, where the dotted line represents the control volume (the system).

<!-- b000178 | prose | pages [11] -->
Assuming steady state, the time deriva- tives of energy and mass in the system must be zero, as no mass or energy can be accu- mulating in the system. This is shown math-

<!-- b000179 | caption | pages [11] -->
Figure 7: Graphical Illustration of the Ther-

<!-- b000180 | prose | pages [11] -->
modynamic System

<!-- b000181 | prose | pages [11] -->
ematically below. The energy equation will be the basis for our model and the mass equation will be used for an important simpliﬁcation.

<!-- b000182 | furniture | pages [11] -->
11

<!-- b000183 | furniture | pages [11] -->
11

<!-- b000184 | furniture | pages [12] -->
Team # 44845

<!-- b000185 | prose | pages [12] -->
dEsystem

<!-- b000186 | prose | pages [12] -->
= 0 ⇒˙Ein = ˙Eout dt

<!-- b000187 | furniture | pages [12] -->
Page 12 of 44

<!-- b000188 | prose | pages [12] -->
dmsystem

<!-- b000189 | prose | pages [12] -->
= 0 ⇒˙min = ˙mout (4) dt

<!-- b000190 | prose | pages [12] -->
Writing the ﬁrst equation above using the First Law of Thermodynamics, the following expression can be found[2].

<!-- b000191 | prose | pages [12] -->
h + v2

<!-- b000192 | prose | pages [12] -->


<!-- b000193 | prose | pages [12] -->


<!-- b000194 | prose | pages [12] -->
˙Qin + ˙Win +

<!-- b000195 | prose | pages [12] -->
X

<!-- b000196 | prose | pages [12] -->
˙m

<!-- b000197 | prose | pages [12] -->
2 + gz

<!-- b000198 | prose | pages [12] -->
inlets

<!-- b000199 | prose | pages [12] -->
h + v2

<!-- b000200 | prose | pages [12] -->


<!-- b000201 | prose | pages [12] -->


<!-- b000202 | prose | pages [12] -->
= ˙Qout + ˙Wout +

<!-- b000203 | prose | pages [12] -->
X

<!-- b000204 | prose | pages [12] -->
2 + gz

<!-- b000205 | prose | pages [12] -->
(5)

<!-- b000206 | prose | pages [12] -->
˙m

<!-- b000207 | prose | pages [12] -->
exits

<!-- b000208 | prose | pages [12] -->
Physically, Equation 5 is simply an energy balance. Energy transfer by heat, work, and mass are accounted for with enthalpy, kinetic energy, and potential energy making up the mass transfer terms. We assume only one inlet and one exit, which removes the summation from the equation. We also assume no work done on or by the system, no change in potential energy, and no change in kinetic energy. These are valid assumptions, as the inlet (faucet) and exit (overﬂow drain) should both be at the level of the water and the kinetic energy terms will be negligible due to the assumed trickle of water. Furthermore, the mass ﬂow entering and leaving should be the same, assuming ˙min = ˙mout from Equation 4 above. Finally, we can combine ˙Qin and ˙Qout into one term representing the net heat transfer. Using these simpliﬁcations and the relationship h = cpu, the expression is reduced greatly.

<!-- b000209 | prose | pages [12] -->
˙mcpuin = ˙mcpuout + ˙Qnet,out (6)

<!-- b000210 | prose | pages [12] -->
Since we assume uniform temperature distribution, the temperature at the exit is equal to the temperature of the system (uout = u). The last piece of this model is to quantify ˙Qnet,out using the heat transfer coeﬃcients discussed in the previous section. We use Newton’s Law of Cooling[2] to ﬁnd an expression for the convective heat transfer.

<!-- b000211 | prose | pages [12] -->
˙Qconv,out = hconvA(u −u∞).

<!-- b000212 | prose | pages [12] -->
(7)

<!-- b000213 | prose | pages [12] -->
Associating the appropriate surface areas with each coeﬃcient, the following expression for the total convective heat loss is found.

<!-- b000214 | prose | pages [12] -->
˙Qconv,out = (u −u∞) ((ht + hb)LW + hw(2HW + 2HL)) .

<!-- b000215 | prose | pages [12] -->
(8)

<!-- b000216 | prose | pages [12] -->
The presence of Joe in the bathtub provides an additional heat transfer term with its own heat transfer coeﬃcient. We will assume the submerged part of the body is a perfect cylinder without end caps, with a length equal to Lbody, a circumference of cbody, and an external temperature of ubody. The total heat loss from the system now includes a term to account for the body and is shown in Equation 9 below.

<!-- b000217 | prose | pages [12] -->
˙Qnet,out = (u −u∞) ((ht + hb)LW + hw(2HW + 2HL)) + (u −ubody)hbodyLbodycbody (9)

<!-- b000218 | prose | pages [12] -->
By substituting Equation 9 into Equation 6 and solving for u, the ﬁnal expression for steady, uniform temperature is found.

<!-- b000219 | prose | pages [12] -->
u = ˙mcpuin + u∞((ht + hb)LW + hw(2HW + 2HL)) + ubodyhbodyLbodycbody

<!-- b000220 | prose | pages [12] -->
(10)

<!-- b000221 | prose | pages [12] -->
(ht + hb)LW + hw(2HW + 2HL) + hbodyLbodycbody

<!-- b000222 | furniture | pages [12] -->
12

<!-- b000223 | furniture | pages [12] -->
12

<!-- b000224 | furniture | pages [13] -->
Team # 44845

<!-- b000225 | furniture | pages [13] -->
Page 13 of 44

<!-- b000226 | prose | pages [13] -->
5.2

<!-- b000227 | heading | pages [13] -->
Implementation and Results

<!-- b000228 | prose | pages [13] -->
Equation 10 was implemented using MATLAB. As was discussed previously, the heat transfer coeﬃcients are taken to be averages. Using the nominal parameter values, the steady, uniform temperature as a function of mass ﬂow is shown below in Figure 8.

<!-- b000229 | caption | pages [13] -->
Figure 8: Sensitivity of Final Temperature to Inlet Mass Flow

<!-- b000230 | prose | pages [13] -->
It is clear from the above ﬁgure that increasing the mass ﬂow results in a ﬁnal temperature that approaches the inlet temperature of 45◦C. A similar plot is shown below to illustrate the dependence on inlet temperature.

<!-- b000231 | caption | pages [13] -->
Figure 9: Sensitivity of Final Temperature to Inlet Temperature

<!-- b000232 | prose | pages [13] -->
When the inlet temperature is close to that of the ambient air (20◦C), the steady temper- ature is higher than that of the inlet, due to the minimal convective heat losses and the eﬀect of the body at 37◦C. However, when the inlet temperature is closer to body temperature, the steady temperature is slightly below the inlet temperature due to the increased convective heat losses. Finally, the sensitivity of the solution to ambient air temperature is presented.

<!-- b000233 | furniture | pages [13] -->
13

<!-- b000234 | furniture | pages [14] -->
Team # 44845

<!-- b000235 | furniture | pages [14] -->
Page 14 of 44

<!-- b000236 | caption | pages [14] -->
Figure 10: Sensitivity of Final Temperature to Ambient Air Temperature

<!-- b000237 | prose | pages [14] -->
This model is clearly much less sensitive to this parameter, illustrating minimal heat losses to convection due to the relatively low heat transfer coeﬃcients.

<!-- b000238 | prose | pages [14] -->
In principle, sensitivities for every parameter could be presented. However, to keep this report concise, we will only present these three. Ultimately, this model is too simple to capture the true dynamical nature of the bathtub system. Thus, more accurate models will be described in the following sections, but the qualitative results here serve as a good baseline for comparison with subsequent models.

<!-- b000239 | prose | pages [14] -->
6

<!-- b000240 | heading | pages [14] -->
An Analytical Model of the Heat Equation

<!-- b000241 | prose | pages [14] -->
In this section, we will describe a model based on an analytical solution to the one-dimensional heat equation with time dependent boundary conditions and time and space dependent heat generation/loss.

<!-- b000242 | prose | pages [14] -->
6.1 Theory

<!-- b000243 | prose | pages [14] -->
First, we will derive the analytical solution. The multi-dimensional heat equation with a heat generation term Q is shown below in Equation 11.

<!-- b000244 | prose | pages [14] -->
∂u

<!-- b000245 | prose | pages [14] -->
∂t = α∇2u + Q(⃗x, t) (11)

<!-- b000246 | prose | pages [14] -->
Using the geometric considerations detailed earlier in this report, this PDE can be reduced to one spatial dimension, changing the Laplacian operator to a second partial derivative. The resulting one-dimensional heat equation must be accompanied by an initial condition and boundary conditions in order to fully specify a problem. These conditions, along with the heat generation term, allow our model to eﬀectively describe the physical eﬀects inﬂuencing the temperature distribution within the bathtub.

<!-- b000247 | prose | pages [14] -->
The most appropriate boundary conditions for the bathtub are Neumann conditions which deﬁne a heat ﬂux at the boundaries. The heat ﬂux into the tub on the faucet side is

<!-- b000248 | furniture | pages [14] -->
14

<!-- b000249 | furniture | pages [15] -->
Team # 44845

<!-- b000250 | furniture | pages [15] -->
Page 15 of 44

<!-- b000251 | prose | pages [15] -->
described by the addition of heat to the system, a function of temperature and mass ﬂow of the inlet. The heat ﬂux on the drain side is due to conductive eﬀects through the water at the location of the drain. In order to keep the model generic, these boundary conditions will be allowed to vary with time. The implementation of time dependent boundary conditions allows for greatly increased ﬂexibility and accuracy of the model.

<!-- b000252 | prose | pages [15] -->
The heat generation term will be extensively used to represent the net eﬀect of both heat loss to the surrounding air and heat generation by Joe himself. As the heat equation admits a heat generation term that is both spatially and temporally dependent, this leads to a highly realistic interpretation of an actual system.

<!-- b000253 | prose | pages [15] -->
The full presentation of the one dimensional heat equation, with time dependent Neu- mann boundary conditions, customizable heat source, and initial condition φ(x), is shown below in Equation 12. Note that subscript notation will be used to represent partial deriva- tives.

<!-- b000254 | prose | pages [15] -->
∂t = α∂2u

<!-- b000255 | prose | pages [15] -->
∂u

<!-- b000256 | prose | pages [15] -->
α ∈R≥0 0 < x < L ∂x2 + Q(x, t) , , t > 0 , (12)

<!-- b000257 | prose | pages [15] -->
ux(x = 0, t) = a(t) , t > 0 ux(x = L, t) = b(t) u(x, t = 0) = φ(x) , t > 0 , 0 < x < L

<!-- b000258 | prose | pages [15] -->
Unlike many standard PDEs, the method of separation of variables will not yield appli- cable solutions, due to the inhomogeneity of the forcing function and the time dependence of the boundary conditions. To solve this problem, the method of shifting the data will be employed to homogenize the boundary conditions. This method, along with many of the other methods in the following solution, is outlined by Grigoryan[4].

<!-- b000259 | prose | pages [15] -->
First, we will transform the original equation:

<!-- b000260 | prose | pages [15] -->
u(x, t) = v(x, t) + U(x, t) where

<!-- b000261 | prose | pages [15] -->
a(t) + x2

<!-- b000262 | prose | pages [15] -->
x −x2

<!-- b000263 | prose | pages [15] -->


<!-- b000264 | prose | pages [15] -->


<!-- b000265 | prose | pages [15] -->
2Lb(t).

<!-- b000266 | prose | pages [15] -->
(13)

<!-- b000267 | prose | pages [15] -->
U(x, t) =

<!-- b000268 | prose | pages [15] -->
2L

<!-- b000269 | prose | pages [15] -->
Plugging this transformation back into the original PDE, the following transformed PDE, boundary conditions, and initial conditions can be found.

<!-- b000270 | prose | pages [15] -->
∂t −α∂2v

<!-- b000271 | prose | pages [15] -->
∂v

<!-- b000272 | prose | pages [15] -->
∂x2 = ˜Q(x, t) α ∈R 0 < x < L , , t > 0 , (14)

<!-- b000273 | prose | pages [15] -->
vx(x = 0, t) = 0 , t > 0 vx(x = L, t) = 0

<!-- b000274 | prose | pages [15] -->
v(x, t = 0) = ˜φ(x)

<!-- b000275 | prose | pages [15] -->
 d

<!-- b000276 | prose | pages [15] -->
, t > 0

<!-- b000277 | prose | pages [15] -->
, 0 < x < L

<!-- b000278 | prose | pages [15] -->
dt (a(t)) −x2

<!-- b000279 | prose | pages [15] -->
x −x2

<!-- b000280 | prose | pages [15] -->


<!-- b000281 | prose | pages [15] -->
˜Q(x, t) = Q(x, t) −

<!-- b000282 | prose | pages [15] -->
2L

<!-- b000283 | prose | pages [15] -->
dt (b(t)) + α d

<!-- b000284 | prose | pages [15] -->
L (b(t) −a(t)) (15)

<!-- b000285 | prose | pages [15] -->
2L

<!-- b000286 | prose | pages [15] -->
x −x2

<!-- b000287 | prose | pages [15] -->


<!-- b000288 | prose | pages [15] -->
˜φ(x) = φ(x) −

<!-- b000289 | prose | pages [15] -->
a(0) −x2

<!-- b000290 | prose | pages [15] -->


<!-- b000291 | prose | pages [15] -->
2Lb(0) (16)

<!-- b000292 | prose | pages [15] -->
2L

<!-- b000293 | furniture | pages [15] -->
15

<!-- b000294 | furniture | pages [15] -->
15

<!-- b000295 | furniture | pages [16] -->
Team # 44845

<!-- b000296 | furniture | pages [16] -->
Page 16 of 44

<!-- b000297 | prose | pages [16] -->
The new variable of interest is v, the transformed heat generation is ˜Q, the transformed initial condition is ˜φ, and the boundary conditions have been homogenized which was the objective of the transformation.

<!-- b000298 | prose | pages [16] -->
Now, we apply the principles of Fourier analysis to the PDE to ﬁnd a general solution for v(x, t). We deﬁne v(x, t) as a Fourier series in the spatial dimension. By Fourier’s Theorem, this representation is possible for any piecewise smooth v over a ﬁnite interval[5].

<!-- b000299 | prose | pages [16] -->
To be complete, a full linear combination of sines and cosines would be considered, but the presence of two homogeneous Neumann conditions suggests that just a cosine series is suﬃcient. This cosine series will include a constant term, as Neumann conditions admit a uniform oﬀset. The Fourier series representation of v is shown below in Equation 17, with the Fourier coeﬃcients deﬁned in Equation 18.

<!-- b000300 | prose | pages [16] -->
∞ X

<!-- b000301 | prose | pages [16] -->
v(x, t) =

<!-- b000302 | prose | pages [16] -->
n=0

<!-- b000303 | prose | pages [16] -->
Z L

<!-- b000304 | prose | pages [16] -->
vn̸=0(t) = 2

<!-- b000305 | prose | pages [16] -->
nπx

<!-- b000306 | prose | pages [16] -->
v(x, t) cos

<!-- b000307 | prose | pages [16] -->
L

<!-- b000308 | prose | pages [16] -->
L

<!-- b000309 | prose | pages [16] -->
0

<!-- b000310 | prose | pages [16] -->
nπx

<!-- b000311 | prose | pages [16] -->


<!-- b000312 | prose | pages [16] -->
vn(t) cos

<!-- b000313 | prose | pages [16] -->
(17)

<!-- b000314 | prose | pages [16] -->
L

<!-- b000315 | prose | pages [16] -->
Z L

<!-- b000316 | prose | pages [16] -->
v0(t) = 1

<!-- b000317 | prose | pages [16] -->


<!-- b000318 | prose | pages [16] -->
dx

<!-- b000319 | prose | pages [16] -->
v(x, t)dx (18)

<!-- b000320 | prose | pages [16] -->
L

<!-- b000321 | prose | pages [16] -->
0

<!-- b000322 | prose | pages [16] -->
Allowing the Fourier coeﬃcients to vary with time is essentially a modiﬁcation of variation of parameters. The same application of Fourier analysis is used on the modiﬁed forcing function, as shown below in Equations 19 and 20.

<!-- b000323 | prose | pages [16] -->
∞

<!-- b000324 | prose | pages [16] -->
˜Q(x, t) =

<!-- b000325 | prose | pages [16] -->
X

<!-- b000326 | prose | pages [16] -->
n=0

<!-- b000327 | prose | pages [16] -->
Z L

<!-- b000328 | prose | pages [16] -->
˜Qn̸=0(t) = 2

<!-- b000329 | prose | pages [16] -->
nπx

<!-- b000330 | prose | pages [16] -->
˜Q(x, t) cos

<!-- b000331 | prose | pages [16] -->
L

<!-- b000332 | prose | pages [16] -->
L

<!-- b000333 | prose | pages [16] -->
0

<!-- b000334 | prose | pages [16] -->
nπx

<!-- b000335 | prose | pages [16] -->


<!-- b000336 | prose | pages [16] -->
˜Qn(t) cos

<!-- b000337 | prose | pages [16] -->
(19)

<!-- b000338 | prose | pages [16] -->
L

<!-- b000339 | prose | pages [16] -->
Z L

<!-- b000340 | prose | pages [16] -->
˜Q0(t) = 1

<!-- b000341 | prose | pages [16] -->


<!-- b000342 | prose | pages [16] -->
˜Q(x, t)dx

<!-- b000343 | prose | pages [16] -->
dx

<!-- b000344 | prose | pages [16] -->
(20)

<!-- b000345 | prose | pages [16] -->
L

<!-- b000346 | prose | pages [16] -->
0

<!-- b000347 | prose | pages [16] -->
At this point the solution function and the forcing function have been fully deﬁned in terms of their spatial Fourier cosine series. These two Fourier series representations can be substituted into the PDE in Equation 14. After working through the algebra and moving the derivatives into the sums (assuming that they converge), the PDE is reduced to Equation 21.

<!-- b000348 | prose | pages [16] -->
∞

<!-- b000349 | prose | pages [16] -->
nπ

<!-- b000350 | prose | pages [16] -->
2

<!-- b000351 | prose | pages [16] -->
i

<!-- b000352 | prose | pages [16] -->
h

<!-- b000353 | prose | pages [16] -->
X

<!-- b000354 | prose | pages [16] -->
v′

<!-- b000355 | prose | pages [16] -->
vn(t)

<!-- b000356 | prose | pages [16] -->
cos

<!-- b000357 | prose | pages [16] -->
n(t) + α

<!-- b000358 | prose | pages [16] -->
L

<!-- b000359 | prose | pages [16] -->
n=0

<!-- b000360 | prose | pages [16] -->
∞

<!-- b000361 | prose | pages [16] -->
nπx

<!-- b000362 | prose | pages [16] -->
nπx

<!-- b000363 | prose | pages [16] -->


<!-- b000364 | prose | pages [16] -->


<!-- b000365 | prose | pages [16] -->
˜Qn(t) cos

<!-- b000366 | prose | pages [16] -->
X

<!-- b000367 | prose | pages [16] -->
=

<!-- b000368 | prose | pages [16] -->
(21)

<!-- b000369 | prose | pages [16] -->
L

<!-- b000370 | prose | pages [16] -->
L

<!-- b000371 | prose | pages [16] -->
n=0

<!-- b000372 | prose | pages [16] -->
By equating Fourier coeﬃcients of the above equation, it can be seen that for every nth term of the series, an ordinary diﬀerential equation (ODE) in time exists relating the coeﬃcients vn(t) and ˜Qn(t). This relationship is shown below in Equation 22.

<!-- b000373 | prose | pages [16] -->
nπ

<!-- b000374 | prose | pages [16] -->
2

<!-- b000375 | prose | pages [16] -->
vn(t) = ˜Qn(t)

<!-- b000376 | prose | pages [16] -->
v′

<!-- b000377 | prose | pages [16] -->
n(t) + α

<!-- b000378 | prose | pages [16] -->
L

<!-- b000379 | prose | pages [16] -->
, n = 0, 1, 2, . . .

<!-- b000380 | prose | pages [16] -->
(22)

<!-- b000381 | prose | pages [16] -->
This ﬁrst order, non-homogeneous ODE with constant coeﬃcients can be solved using the integrating factor method in which the full ODE is multiplied by a factor that allows the left side terms to be expressed as a perfect derivative of the product of two functions.

<!-- b000382 | furniture | pages [16] -->
16

<!-- b000383 | furniture | pages [16] -->
16

<!-- b000384 | furniture | pages [17] -->
Team # 44845

<!-- b000385 | furniture | pages [17] -->
Page 17 of 44

<!-- b000386 | prose | pages [17] -->
This common process will not be demonstrated here, but the solution is shown in Equation 23 below, where s is a dummy variable of integration.

<!-- b000387 | prose | pages [17] -->
 2t

<!-- b000388 | prose | pages [17] -->
vn(t) = e−α( nπ

<!-- b000389 | prose | pages [17] -->
L )

<!-- b000390 | prose | pages [17] -->
Z t

<!-- b000391 | prose | pages [17] -->
 2s ˜Qn(s)ds

<!-- b000392 | prose | pages [17] -->
eα( nπ

<!-- b000393 | prose | pages [17] -->
L )

<!-- b000394 | prose | pages [17] -->
vn(0) +

<!-- b000395 | prose | pages [17] -->
(23)

<!-- b000396 | prose | pages [17] -->
0

<!-- b000397 | prose | pages [17] -->
Each of these ODEs is for a speciﬁc nth term of the Fourier series.

<!-- b000398 | prose | pages [17] -->
Therefore, it is necessary to deﬁne the initial condition as a Fourier cosine series, just as was done for the solution variable and the forcing function. The cosine series is shown below in Equation 24, with a note about v(x, 0) that will be used in the next step.

<!-- b000399 | prose | pages [17] -->
∞

<!-- b000400 | prose | pages [17] -->
nπx

<!-- b000401 | prose | pages [17] -->


<!-- b000402 | prose | pages [17] -->
˜φ(x) =

<!-- b000403 | prose | pages [17] -->
˜φn cos

<!-- b000404 | prose | pages [17] -->
X

<!-- b000405 | prose | pages [17] -->
∞

<!-- b000406 | prose | pages [17] -->
nπx

<!-- b000407 | prose | pages [17] -->


<!-- b000408 | prose | pages [17] -->
X

<!-- b000409 | prose | pages [17] -->
vn(0) cos

<!-- b000410 | prose | pages [17] -->
Note: v(x, 0) =

<!-- b000411 | prose | pages [17] -->
L

<!-- b000412 | prose | pages [17] -->
n=0

<!-- b000413 | prose | pages [17] -->
The coeﬃcients are shown in Equation 25.

<!-- b000414 | prose | pages [17] -->
Z L

<!-- b000415 | prose | pages [17] -->
˜φn̸=0 = 2

<!-- b000416 | prose | pages [17] -->
nπx

<!-- b000417 | prose | pages [17] -->


<!-- b000418 | prose | pages [17] -->
˜φ(x) cos

<!-- b000419 | prose | pages [17] -->
L

<!-- b000420 | prose | pages [17] -->
L

<!-- b000421 | prose | pages [17] -->
0

<!-- b000422 | prose | pages [17] -->
(24)

<!-- b000423 | prose | pages [17] -->
L

<!-- b000424 | prose | pages [17] -->
n=0

<!-- b000425 | prose | pages [17] -->
Z L

<!-- b000426 | prose | pages [17] -->
˜φ0 = 1

<!-- b000427 | prose | pages [17] -->
˜φ(x)dx

<!-- b000428 | prose | pages [17] -->
dx

<!-- b000429 | prose | pages [17] -->
(25)

<!-- b000430 | prose | pages [17] -->
L

<!-- b000431 | prose | pages [17] -->
0

<!-- b000432 | prose | pages [17] -->
By examining the note in Equation 24 and observing that ˜φ(x) ≡v(x, 0), equating the coeﬃcients results in the relationship vn(0) = ˜φn. Thus,

<!-- b000433 | prose | pages [17] -->
vn̸=0(0) = ˜φn̸=0 v0(0) = ˜φ0, and (26)

<!-- b000434 | prose | pages [17] -->
which can be directly substituted into Equation 23 where ˜φn̸=0 and ˜φ0 are given by Equation 25.

<!-- b000435 | prose | pages [17] -->
This completes the solution for vn(t), the Fourier coeﬃcients of the transformed solution. Next, v(t) is represented in terms of these coeﬃcients, where ˜Qn and ˜φn are the Fourier coeﬃcients of the transformed heat generation and initial condition respectively, both known functions.

<!-- b000436 | prose | pages [17] -->
Z t

<!-- b000437 | prose | pages [17] -->
∞

<!-- b000438 | prose | pages [17] -->


<!-- b000439 | prose | pages [17] -->
2t +

<!-- b000440 | prose | pages [17] -->
L )

<!-- b000441 | prose | pages [17] -->
˜φne−α( nπ

<!-- b000442 | prose | pages [17] -->
X

<!-- b000443 | prose | pages [17] -->
v(x, t) =

<!-- b000444 | prose | pages [17] -->
0

<!-- b000445 | prose | pages [17] -->
n=0

<!-- b000446 | prose | pages [17] -->


<!-- b000447 | prose | pages [17] -->
nπx

<!-- b000448 | prose | pages [17] -->
2(s−t) ˜Qn(s)ds

<!-- b000449 | prose | pages [17] -->


<!-- b000450 | prose | pages [17] -->
eα( nπ

<!-- b000451 | prose | pages [17] -->
L )

<!-- b000452 | prose | pages [17] -->
(27)

<!-- b000453 | prose | pages [17] -->
cos

<!-- b000454 | prose | pages [17] -->
L

<!-- b000455 | prose | pages [17] -->
A transformation back from v to u by unshifting the data completes the solution to the original PDE with time dependent Neumann boundary conditions and time and space dependent heat generation.

<!-- b000456 | prose | pages [17] -->
Z t

<!-- b000457 | prose | pages [17] -->
∞

<!-- b000458 | prose | pages [17] -->


<!-- b000459 | prose | pages [17] -->
x −x2

<!-- b000460 | prose | pages [17] -->
a(t) + x2

<!-- b000461 | prose | pages [17] -->


<!-- b000462 | prose | pages [17] -->


<!-- b000463 | prose | pages [17] -->


<!-- b000464 | prose | pages [17] -->
nπx

<!-- b000465 | prose | pages [17] -->
2(s−t) ˜Qn(s)ds

<!-- b000466 | prose | pages [17] -->
2t +

<!-- b000467 | prose | pages [17] -->
˜φne−α( nπ

<!-- b000468 | prose | pages [17] -->
L )

<!-- b000469 | prose | pages [17] -->
eα( nπ

<!-- b000470 | prose | pages [17] -->
L )

<!-- b000471 | prose | pages [17] -->
X

<!-- b000472 | prose | pages [17] -->
u(x, t) =

<!-- b000473 | prose | pages [17] -->
0

<!-- b000474 | prose | pages [17] -->
n=0

<!-- b000475 | prose | pages [17] -->


<!-- b000476 | prose | pages [17] -->
cos

<!-- b000477 | prose | pages [17] -->
+

<!-- b000478 | prose | pages [17] -->
2Lb(t)

<!-- b000479 | prose | pages [17] -->
L

<!-- b000480 | prose | pages [17] -->
2L

<!-- b000481 | prose | pages [17] -->
(28) This solution is a full analytical model of one-dimensional heat diﬀusion within the bath- tub. It accommodates the eﬀects of time dependent heat ﬂux through the faucet and can account for the eﬀects of Joe’s body temperature and convective heat loss to the ambient air, both of which can vary spatially and temporally. The next subsection will detail the implementation of this solution.

<!-- b000482 | furniture | pages [17] -->
17

<!-- b000483 | furniture | pages [17] -->
17

<!-- b000484 | furniture | pages [18] -->
Team # 44845

<!-- b000485 | furniture | pages [18] -->
Page 18 of 44

<!-- b000486 | heading | pages [18] -->
Implementing the Analytical Model

<!-- b000487 | prose | pages [18] -->
6.2

<!-- b000488 | prose | pages [18] -->
Implementation of the analytical solution is done in MATLAB. Here, we can take full ad- vantage of the underlying vector and matrix structures necessary for these calculations. We deﬁne a grid of (x, t) coordinates with grid sizes ∆x and ∆t.

<!-- b000489 | prose | pages [18] -->
tj+1 = tj + ∆t xi+1 = xi + ∆x (29)

<!-- b000490 | prose | pages [18] -->
Using this grid, Equation 28 is ultimately the addition of (x×t) matrices, each a product of an (x × 1) vector and a (1 × t) vector. The following discussion concerns each term of Equation 28 and its implementation in MATLAB.

<!-- b000491 | prose | pages [18] -->
To ﬁnd the coeﬃcients ˜φn, the integral in Equation 25 is approximated using a Trape- zoidal Rule with a spacing of h and N subdivisions.

<!-- b000492 | prose | pages [18] -->
Z L

<!-- b000493 | prose | pages [18] -->
N

<!-- b000494 | prose | pages [18] -->
nπx

<!-- b000495 | prose | pages [18] -->
dx ≈h

<!-- b000496 | prose | pages [18] -->


<!-- b000497 | prose | pages [18] -->
h

<!-- b000498 | prose | pages [18] -->
˜φ(x) cos

<!-- b000499 | prose | pages [18] -->
nπxk+1

<!-- b000500 | prose | pages [18] -->
nπxk

<!-- b000501 | prose | pages [18] -->


<!-- b000502 | prose | pages [18] -->
i

<!-- b000503 | prose | pages [18] -->
˜φ(xk+1) cos

<!-- b000504 | prose | pages [18] -->
X

<!-- b000505 | prose | pages [18] -->
L

<!-- b000506 | prose | pages [18] -->
2

<!-- b000507 | prose | pages [18] -->
0

<!-- b000508 | prose | pages [18] -->
k=1

<!-- b000509 | prose | pages [18] -->
+ ˜φ(xk) cos

<!-- b000510 | prose | pages [18] -->
(30)

<!-- b000511 | prose | pages [18] -->
L

<!-- b000512 | prose | pages [18] -->
L

<!-- b000513 | prose | pages [18] -->
The same approximation is used to compute ˜Qn.

<!-- b000514 | prose | pages [18] -->
Z L

<!-- b000515 | prose | pages [18] -->
N

<!-- b000516 | prose | pages [18] -->
dx ≈h

<!-- b000517 | prose | pages [18] -->
nπx

<!-- b000518 | prose | pages [18] -->


<!-- b000519 | prose | pages [18] -->
h

<!-- b000520 | prose | pages [18] -->
nπxk

<!-- b000521 | prose | pages [18] -->
nπxk+1

<!-- b000522 | prose | pages [18] -->


<!-- b000523 | prose | pages [18] -->
i

<!-- b000524 | prose | pages [18] -->
˜Q(xk+1, t) cos

<!-- b000525 | prose | pages [18] -->
˜Q(x, t) cos

<!-- b000526 | prose | pages [18] -->
X

<!-- b000527 | prose | pages [18] -->
L

<!-- b000528 | prose | pages [18] -->
2

<!-- b000529 | prose | pages [18] -->
0

<!-- b000530 | prose | pages [18] -->
k=1

<!-- b000531 | prose | pages [18] -->
+ ˜Q(xk, t) cos

<!-- b000532 | prose | pages [18] -->
(31)

<!-- b000533 | prose | pages [18] -->
L

<!-- b000534 | prose | pages [18] -->
L

<!-- b000535 | prose | pages [18] -->
The left-hand side of Equation 31 is a function of t, so the integration on the right-hand side must be performed at every t in the deﬁned grid.

<!-- b000536 | prose | pages [18] -->
The computation of the time-varying integral in Equation 27 requires more care.

<!-- b000537 | prose | pages [18] -->
A Trapezoidal Rule is still utilized, but the subdivision length becomes a function of time.

<!-- b000538 | prose | pages [18] -->
Z t

<!-- b000539 | prose | pages [18] -->
N

<!-- b000540 | prose | pages [18] -->
2(s−t) ˜Qn(s)ds ≈h(t)

<!-- b000541 | prose | pages [18] -->
h

<!-- b000542 | prose | pages [18] -->
L )

<!-- b000543 | prose | pages [18] -->
eα( nπ

<!-- b000544 | prose | pages [18] -->
L )

<!-- b000545 | prose | pages [18] -->
eα( nπ

<!-- b000546 | prose | pages [18] -->
X

<!-- b000547 | prose | pages [18] -->
2

<!-- b000548 | prose | pages [18] -->
0

<!-- b000549 | prose | pages [18] -->
k=1

<!-- b000550 | prose | pages [18] -->
2(sk+1−t) ˜Qn(sk+1) + eα( nπ

<!-- b000551 | prose | pages [18] -->
2(sk−t) ˜Qn(sk) i

<!-- b000552 | prose | pages [18] -->
L )

<!-- b000553 | prose | pages [18] -->
(32)

<!-- b000554 | heading | pages [18] -->
Basic Results and Veriﬁcation

<!-- b000555 | prose | pages [18] -->
6.3

<!-- b000556 | prose | pages [18] -->
The ﬁrst scenario to simulate is heat loss over time with insulation on both ends of the bathtub. In this scenario, we expect that the heat loss from the bottom, sides, and top of the bathtub will uniformly decrease the temperature of the water over time. The boundary conditions, initial condition, and internal heat generation are modeled in Equation 33.

<!-- b000557 | prose | pages [18] -->
ux(x = 0, t) = 0 , t > 0 ux(x = L, t) = 0 , t > 0

<!-- b000558 | prose | pages [18] -->
(33)

<!-- b000559 | prose | pages [18] -->
u(x, t = 0) = 37 ◦C, 0 < x < L

<!-- b000560 | prose | pages [18] -->
Q(x, t) = ˜h(u∞−u(x, t −∆t)) , 0 < x < L, t > 0

<!-- b000561 | furniture | pages [18] -->
18

<!-- b000562 | furniture | pages [18] -->
18

<!-- b000563 | furniture | pages [19] -->
Team # 44845

<!-- b000564 | furniture | pages [19] -->
Page 19 of 44

<!-- b000565 | prose | pages [19] -->
Physically, Q(x, t) describes the combined heat losses from the water to the tub and sur- rounding air. The greater the diﬀerence between the water temperature and the surrounding air temperature, the greater the heat loss. However, the water temperature is sampled from the previous time step; to reﬂect this, t −∆t is used in place of t when computing the water temperature in space. The coeﬃcient ˜h describes the rate of heat loss through the diﬀerent surfaces. We expand ˜h in Equation 34.

<!-- b000566 | prose | pages [19] -->
2hw

<!-- b000567 | prose | pages [19] -->


<!-- b000568 | prose | pages [19] -->
W + hb

<!-- b000569 | prose | pages [19] -->
˜h = 1

<!-- b000570 | prose | pages [19] -->
ρcp

<!-- b000571 | prose | pages [19] -->
H + ht

<!-- b000572 | prose | pages [19] -->
(34)

<!-- b000573 | prose | pages [19] -->
H

<!-- b000574 | prose | pages [19] -->
The subscripts on each h describe the heat transfer coeﬃcients through the wall (hw), bottom (hb), and top (ht). The division of each coeﬃcient by some length indicates the characteristic length relevant to the heat transfer through that surface. In order to have units of ◦C/s, we divide all terms by the product ρcp.

<!-- b000575 | prose | pages [19] -->
With all the relevant data described, the algorithm necessary to compute u(x, t) is to ﬁrst compute all quantities for t = 0. This way, ˜Q(x, 0) can be initialized in Equation 35.

<!-- b000576 | prose | pages [19] -->
x −x2

<!-- b000577 | prose | pages [19] -->


<!-- b000578 | prose | pages [19] -->
˜Q(x, 0) = ˜h(u∞−φ(x)) −

<!-- b000579 | prose | pages [19] -->
2L

<!-- b000580 | prose | pages [19] -->
−x2

<!-- b000581 | prose | pages [19] -->
da(0)

<!-- b000582 | prose | pages [19] -->
db(0)

<!-- b000583 | prose | pages [19] -->
+ α

<!-- b000584 | prose | pages [19] -->
 

<!-- b000585 | prose | pages [19] -->


<!-- b000586 | prose | pages [19] -->
b(0) −a(0)

<!-- b000587 | prose | pages [19] -->
(35)

<!-- b000588 | prose | pages [19] -->
dt

<!-- b000589 | prose | pages [19] -->
2L

<!-- b000590 | prose | pages [19] -->
dt

<!-- b000591 | prose | pages [19] -->
L

<!-- b000592 | prose | pages [19] -->
Now we can iterate over time in a loop. This way, the previous results are used to calculate recursively the heat loss Q(x, y) and then a new u(x, t). Nested in this loop is another loop which iterates over the number of Fourier terms, N. This performs the summation of each Fourier term to yield the ﬁnal solution. For the data used in Equation 33, Figure 11 displays the temperature distribution in x and t.

<!-- b000593 | caption | pages [19] -->
Figure 11: Heat Map of Heat Loss over Time

<!-- b000594 | prose | pages [19] -->
This result is what we expect: with both ends insulated, the water temperature uniformly decreases over time.

<!-- b000595 | prose | pages [19] -->
Consider new boundary conditions in Equation 36.

<!-- b000596 | furniture | pages [19] -->
19

<!-- b000597 | furniture | pages [19] -->
19

<!-- b000598 | furniture | pages [20] -->
Team # 44845

<!-- b000599 | furniture | pages [20] -->
Page 20 of 44

<!-- b000600 | prose | pages [20] -->
ux(x = 0, t) = ˆh [uin −u(0, t −∆t)]

<!-- b000601 | prose | pages [20] -->
1

<!-- b000602 | prose | pages [20] -->
, t > 0

<!-- b000603 | prose | pages [20] -->
∆x [u(L −∆x, t −∆t) −u(L, t −∆t)] ux(x = L, t) = , t > 0

<!-- b000604 | prose | pages [20] -->
(36)

<!-- b000605 | prose | pages [20] -->
u(x, t = 0) = 37 ◦C, 0 < x < L

<!-- b000606 | prose | pages [20] -->
Q(x, t) = ˜h[u∞−u(x, t −∆t)] , 0 < x < L, t > 0

<!-- b000607 | prose | pages [20] -->
The boundary condition at x = 0 represents an inlet heat ﬂux, entering the system with temperature uin. The boundary condition at x = L is a rough approximation of the heat ﬂux from the previous time step. Similar to the internal heat loss, the heat ﬂux decreases as the water temperature at x = 0 approaches uin. The coeﬃcient ˆh ensures that the units agree on both sides of the equation. Physically, ˆh, is proportional to the mass ﬂow rate of water from the inlet. Equation 37 describes this relationship.

<!-- b000608 | prose | pages [20] -->
ˆh = ˙mcp (37) kWH

<!-- b000609 | prose | pages [20] -->
The code structure from the previous set of boundary conditions allows for the recursive calculations to compute each new boundary condition. For uin = 45◦C, the full solution in x and t for the conditions set in Equation 36 are shown in Figure 12.

<!-- b000610 | caption | pages [20] -->
Figure 12: Demonstration of Heat Distribution and Heat Loss With Input Water

<!-- b000611 | caption | pages [20] -->
Figure 12 demonstrates that the heat propagates through the water. This behavior is

<!-- b000612 | prose | pages [20] -->
expected due to the low thermal diﬀusivity of water.

<!-- b000613 | prose | pages [20] -->
Now we simulate a body moving as a point source through the bath. To do so, we deﬁne F(x, t).

<!-- b000614 | furniture | pages [20] -->
20

<!-- b000615 | furniture | pages [20] -->
20

<!-- b000616 | furniture | pages [21] -->
Team # 44845

<!-- b000617 | prose | pages [21] -->
Z x−t+ϵ

<!-- b000618 | furniture | pages [21] -->
Page 21 of 44

<!-- b000619 | prose | pages [21] -->
δ(x −t −400)d(x −t),

<!-- b000620 | prose | pages [21] -->
F(x, t) = f

<!-- b000621 | prose | pages [21] -->
x−t−ϵ

<!-- b000622 | prose | pages [21] -->
0 < t < 200 (38)

<!-- b000623 | prose | pages [21] -->
Physically, the bather is placed at x = 400 at t = 0; then, whenever x = t + 400, F(x, t) = f. f is simply a constant heat generation term deﬁned by the thermodynamic characteristics of the body placed inside the bath. Including in the heat loss term to the surroundings in Q(x, t), our full problem becomes deﬁned as below.

<!-- b000624 | prose | pages [21] -->
ux(x = 0, t) = 0 , t > 0 ux(x = L, t) = 0 , t > 0

<!-- b000625 | prose | pages [21] -->
(39)

<!-- b000626 | prose | pages [21] -->
u(x, t = 0) = 45 ◦C, 0 < x < L

<!-- b000627 | prose | pages [21] -->
Q(x, t) = F(x, t) + ˜h[u∞−u(x, t −∆t)] , 0 < x < L, t > 0

<!-- b000628 | prose | pages [21] -->
The new solution is displayed below in Figure 13.

<!-- b000629 | caption | pages [21] -->
Figure 13: Demonstration of a Moving Heat Source in the Bath

<!-- b000630 | caption | pages [21] -->
Figure 13 shows that the analytical model is capable of capturing a moving heat source

<!-- b000631 | prose | pages [21] -->
in both space and time. Whenever a point source moves to another location, the previous locations remain at the higher temperature because the heat diﬀuses very slowly.

<!-- b000632 | furniture | pages [21] -->
21

<!-- b000633 | furniture | pages [21] -->
21

<!-- b000634 | furniture | pages [22] -->
Team # 44845

<!-- b000635 | furniture | pages [22] -->
Page 22 of 44

<!-- b000636 | heading | pages [22] -->
A Numerical Model of Convection-Diﬀusion

<!-- b000637 | prose | pages [22] -->
7

<!-- b000638 | prose | pages [22] -->
In this section we will describe our ﬁnal model: a ﬁnite diﬀerence approximation of the convection-diﬀusion equation. We will brieﬂy discuss the theoretical development and im- plementation, and then present initial results.

<!-- b000639 | prose | pages [22] -->
7.1 Theory

<!-- b000640 | prose | pages [22] -->
The problem at hand can be even more eﬀectively modeled as a one-dimensional convection- diﬀusion problem. The addition of a convection term allows the actual ﬂow of the water – and not just diﬀusion of heat – to be modeled. It is important to note that convection in this sense means the bulk motion of the water in the tub and not the heat loss to the surroundings. The governing PDE for a convection-diﬀusion problem is shown below, where the only new quantity is ϵ, the porosity.

<!-- b000641 | prose | pages [22] -->
∂t = α∂2u

<!-- b000642 | prose | pages [22] -->
∂u

<!-- b000643 | prose | pages [22] -->
∂x2 −ϵv∂u

<!-- b000644 | prose | pages [22] -->
∂x + q(x, t)

<!-- b000645 | prose | pages [22] -->
(40)

<!-- b000646 | prose | pages [22] -->
ρcp

<!-- b000647 | prose | pages [22] -->
∂t represents the transient, α ∂2u

<!-- b000648 | prose | pages [22] -->
In this equation, ∂u

<!-- b000649 | prose | pages [22] -->
∂x2 represents diﬀusion, ϵv ∂u

<!-- b000650 | prose | pages [22] -->
∂x represents convection, and the ﬁnal term represents heat generation or loss. Eliminating the convection and generation terms yields the familiar heat equation presented earlier. Due to the diﬃculty in solving this equation analytically, a numerical solution will be implemented using the ﬁnite diﬀerence method, as outlined by Majchrzak and Turcha[6].

<!-- b000651 | prose | pages [22] -->
The ﬁrst step is to discretize the temporal and spatial variables, as shown below, where j indexes through time, i indexes through space, and ∆t and ∆x are the time step and grid spacing, respectively.

<!-- b000652 | prose | pages [22] -->
tj+1 = tj + ∆t xi+1 = xi + ∆x (41)

<!-- b000653 | prose | pages [22] -->
Each derivative can be re-written using a Taylor series in the variable of diﬀerentiation. This is shown below in Equation 42, where the superscript represents time indexed in j and the subscript represents space indexed in i.

<!-- b000654 | prose | pages [22] -->
= αuj

<!-- b000655 | prose | pages [22] -->
i+1 −2uj

<!-- b000656 | prose | pages [22] -->
i + uj

<!-- b000657 | prose | pages [22] -->
i −uj−1

<!-- b000658 | prose | pages [22] -->
uj

<!-- b000659 | prose | pages [22] -->
i

<!-- b000660 | prose | pages [22] -->
(∆x)2

<!-- b000661 | prose | pages [22] -->
∆t

<!-- b000662 | prose | pages [22] -->
−ϵvuj−1

<!-- b000663 | prose | pages [22] -->
i+1 −uj−1

<!-- b000664 | prose | pages [22] -->
+ qj−1

<!-- b000665 | prose | pages [22] -->
i−1

<!-- b000666 | prose | pages [22] -->
i−1

<!-- b000667 | prose | pages [22] -->
i

<!-- b000668 | prose | pages [22] -->
(42)

<!-- b000669 | prose | pages [22] -->
∆x

<!-- b000670 | prose | pages [22] -->
ρcp

<!-- b000671 | prose | pages [22] -->
Solving for the temperature at the time (j) and location (i) of interest yields the following numerical solution to the convection-diﬀusion equation.

<!-- b000672 | prose | pages [22] -->
 α∆t

<!-- b000673 | prose | pages [22] -->


<!-- b000674 | prose | pages [22] -->


<!-- b000675 | prose | pages [22] -->
1 −2α∆t

<!-- b000676 | prose | pages [22] -->
(∆x)2 + ϵv∆t

<!-- b000677 | prose | pages [22] -->
uj−1

<!-- b000678 | prose | pages [22] -->
uj

<!-- b000679 | prose | pages [22] -->
i =

<!-- b000680 | prose | pages [22] -->
+ i

<!-- b000681 | prose | pages [22] -->
(∆x)2

<!-- b000682 | prose | pages [22] -->
2∆x

<!-- b000683 | prose | pages [22] -->
 α∆t

<!-- b000684 | prose | pages [22] -->
+ qj−1

<!-- b000685 | prose | pages [22] -->


<!-- b000686 | prose | pages [22] -->


<!-- b000687 | prose | pages [22] -->
(∆x)2 −ϵv∆t

<!-- b000688 | prose | pages [22] -->
uj−1

<!-- b000689 | prose | pages [22] -->
i

<!-- b000690 | prose | pages [22] -->
i−1 +

<!-- b000691 | prose | pages [22] -->
cpρ ∆t (43)

<!-- b000692 | prose | pages [22] -->
2∆x

<!-- b000693 | prose | pages [22] -->
When selecting step sizes ∆x and ∆t, we must ensure that the stability criteria are met since the forward diﬀerence approximations are conditionally stable. These criteria are described below.

<!-- b000694 | prose | pages [22] -->
∆x < 2α

<!-- b000695 | prose | pages [22] -->
ϵv , ∆t < (∆x)2

<!-- b000696 | prose | pages [22] -->
(44) 2α

<!-- b000697 | furniture | pages [22] -->
22

<!-- b000698 | furniture | pages [22] -->
22

<!-- b000699 | furniture | pages [23] -->
Team # 44845

<!-- b000700 | furniture | pages [23] -->
Page 23 of 44

<!-- b000701 | prose | pages [23] -->
Should these conditions not be met, the error accumulated in each approximation will grow unboundedly[7].

<!-- b000702 | prose | pages [23] -->
The ﬁnal solution, uj

<!-- b000703 | prose | pages [23] -->
i, describes the propagation of heat through space and time, and can be implemented in MATLAB. The porosity, ϵ, is the ratio of ﬂuid volume to total volume, and since the medium is entirely ﬂuid, it will be taken as unity. To complete this model, we must now quantify q and enforce appropriate boundary conditions.

<!-- b000704 | prose | pages [23] -->
The fundamental source of heat transfer in this problem is convection from the water surface and from the bathtub surface. In Equation 43 above, q is the heat transfer per unit volume, where the volume in consideration is a slice of the bathtub in the x direction. This slice has volume WH∆x. Thus,

<!-- b000705 | prose | pages [23] -->
q = Q WH∆x, (45)

<!-- b000706 | prose | pages [23] -->
where Q is the macroscopic heat loss of the slice. This heat loss is described by the convection terms and the conduction term as follows.

<!-- b000707 | prose | pages [23] -->
Q = (u −u∞)(htAt + hwAw + hbAb) = (u −u∞)(ht(W∆x) + hs(2H∆x) + hb(W∆x)) (46)

<!-- b000708 | prose | pages [23] -->
Upon plugging this into Equation 45, we explicitly quantify q due to natural heat transfer eﬀects.

<!-- b000709 | prose | pages [23] -->
q = (u −u∞)

<!-- b000710 | prose | pages [23] -->
(W(ht + hb) + 2Hhw) WH (47)

<!-- b000711 | prose | pages [23] -->
The same method can be used to model the presence of a person in the bathtub. We estimate that the person will take up a given amount of space in the x direction and have a given circumference cbody, which correlates to the exposed area per unit length of the bathtub. The additional heat generation/loss due to the body can be implemented as follows.

<!-- b000712 | prose | pages [23] -->
qbody = hbodycbody(u −ubody)

<!-- b000713 | prose | pages [23] -->
(48) WH

<!-- b000714 | prose | pages [23] -->
Together, Equations 47 and 48 make up the heat generation term in the PDE. At a given location i and time step j, we use uj−1

<!-- b000715 | prose | pages [23] -->
to estimate u in these equations. i Enforcing the boundary conditions requires some creativity. To enforce the boundary condition on the inlet side, we must specify the correct amount of heat ﬂux into the system as a Neumann condition, increasing the energy content of the ﬂuid element at the boundary based on the mass ﬂow and temperature of the inlet.

<!-- b000716 | prose | pages [23] -->
The energy entering per unit volume, a q term, can be described as

<!-- b000717 | prose | pages [23] -->
WH∆x = ˙mcp(uin −u) Q q =

<!-- b000718 | prose | pages [23] -->
.

<!-- b000719 | prose | pages [23] -->
(49) WH∆x

<!-- b000720 | prose | pages [23] -->
This can be translated directly into a change in temperature, as in Equation 43 above, by dividing by ρcp, multiplying by the time step ∆t, and approximating u from the previous time step.

<!-- b000721 | prose | pages [23] -->
i = ˙m(uin −uj−1

<!-- b000722 | prose | pages [23] -->
∆uj

<!-- b000723 | prose | pages [23] -->
) i ∆t (50) ρWH∆x

<!-- b000724 | furniture | pages [23] -->
23

<!-- b000725 | furniture | pages [23] -->
23

<!-- b000726 | furniture | pages [24] -->
Team # 44845

<!-- b000727 | furniture | pages [24] -->
Page 24 of 44

<!-- b000728 | prose | pages [24] -->
Equation 50 provides a direct method for changing the temperature of the boundary point in order to account for the heat entering the system.

<!-- b000729 | prose | pages [24] -->
At the other boundary point, we wish for the water to exit the system naturally, which poses a challenge in prescribing a boundary condition.

<!-- b000730 | prose | pages [24] -->
A realistic condition is that the ﬂux out is equal to the ﬂux between the two points adjacent to the boundary. Thus, the temperature at the end can be speciﬁed as follows.

<!-- b000731 | furniture | pages [24] -->


<!-- b000732 | prose | pages [24] -->
!

<!-- b000733 | prose | pages [24] -->
end−1 −uj

<!-- b000734 | prose | pages [24] -->
uj

<!-- b000735 | prose | pages [24] -->
end−1 + ∂u

<!-- b000736 | prose | pages [24] -->
uj

<!-- b000737 | prose | pages [24] -->
end = uj

<!-- b000738 | prose | pages [24] -->
∂x∆x = uj

<!-- b000739 | prose | pages [24] -->
end−1 +

<!-- b000740 | prose | pages [24] -->
∆x = 2uj

<!-- b000741 | prose | pages [24] -->
end−1 −uj

<!-- b000742 | prose | pages [24] -->
end−2

<!-- b000743 | prose | pages [24] -->
(51) end−2

<!-- b000744 | prose | pages [24] -->
∆x

<!-- b000745 | prose | pages [24] -->
Now, both boundary conditions have been speciﬁed and the ﬁnite diﬀerence method can be implemented in MATLAB. We will not describe the algorithm here, as it follows directly from the derivation above.

<!-- b000746 | heading | pages [24] -->
Basic Results and Veriﬁcation

<!-- b000747 | prose | pages [24] -->
7.2

<!-- b000748 | prose | pages [24] -->
In this subsection, we will present some basic results to demonstrate the functionality of our model. First, the problem was modeled with no heat input (the faucet turned oﬀ). The results from this simulation are shown below in Figure 14.

<!-- b000749 | caption | pages [24] -->
Figure 14: Demonstration of Heat Loss over Time in Numerical Model

<!-- b000750 | prose | pages [24] -->
The temperature in the tub remains uniform and slowly decreases due to heat loss to the surrounding air. Next, the system was modeled with the faucet on, and the results are shown below.

<!-- b000751 | furniture | pages [24] -->
24

<!-- b000752 | furniture | pages [24] -->
24

<!-- b000753 | furniture | pages [25] -->
Team # 44845

<!-- b000754 | furniture | pages [25] -->
Page 25 of 44

<!-- b000755 | caption | pages [25] -->
Figure 15: Heat Map of Uniform Mass Flow from Faucet with Heat Loss

<!-- b000756 | prose | pages [25] -->
This time, the temperature away from the faucet (near x = L) drops steadily, as before, but the temperature near the faucet increases to the temperature of the incoming water. Through time, this wave of heat convects through the system at a rate determined by the mass ﬂow and the geometry of the tub. Next, the presence of the bather, Joe, was added and the simulation was run.

<!-- b000757 | caption | pages [25] -->
Figure 16: Heat Map of Numerical Model with Bather Present

<!-- b000758 | prose | pages [25] -->
The deviation of these results from the simulation without the bather is unnoticeable without closely examining the numerical values on a computer. This illustrates that the presence of a bather has little eﬀect on the simulation, an observation that makes physical sense due to the bath temperature and body temperatures being nearly identical.

<!-- b000759 | furniture | pages [25] -->
25

<!-- b000760 | furniture | pages [26] -->
Team # 44845

<!-- b000761 | prose | pages [26] -->
7.3

<!-- b000762 | heading | pages [26] -->
Modeling Bather Actions

<!-- b000763 | furniture | pages [26] -->
Page 26 of 44

<!-- b000764 | prose | pages [26] -->
In this subsection, we will examine the eﬀect of actions of the bather on the solution. As we are assuming no ﬂuid ﬂow other than the bulk, convective motion towards the drain, the bather will have no eﬀect other than to distribute/redistribute heat. Further, we limit ourselves to the case of ﬁxed inlet water temperature and mass ﬂow. This allows the bather to distribute the incoming heat as they wish.

<!-- b000765 | prose | pages [26] -->
The logic from the boundary condition on the inlet is now extended to the full domain. Given the amount of input energy speciﬁed by Equation 49, this energy can be added to any location or combination of locations in the domain, provided that the total amount of energy added to the system does not change from what would have been originally added at the inlet.

<!-- b000766 | prose | pages [26] -->
This can be implemented by modifying Equation 50, as shown below, where ηj

<!-- b000767 | prose | pages [26] -->
i (between 0 and 1) is the fraction of available heat prescribed to enter that grid point at that time.

<!-- b000768 | prose | pages [26] -->
˙m(uin −uj−1

<!-- b000769 | prose | pages [26] -->
∆uj

<!-- b000770 | prose | pages [26] -->
i = ηj

<!-- b000771 | prose | pages [26] -->
i

<!-- b000772 | prose | pages [26] -->
) i ∆t (52) ρWH∆x

<!-- b000773 | prose | pages [26] -->
This temperature change term is in addition to the temperature change already calculated from the discretized derivatives and heat loss to the surroundings. In order to conserve energy, the following equality must be deﬁned for all times.

<!-- b000774 | prose | pages [26] -->
X

<!-- b000775 | prose | pages [26] -->
i

<!-- b000776 | prose | pages [26] -->
ηj ηj

<!-- b000777 | prose | pages [26] -->
i = 1 (53)

<!-- b000778 | prose | pages [26] -->
Two interesting applications of bather eﬀects are shown below in Figures 17a and 17b. In the left ﬁgure, 99% of the input water was evenly distributed over the whole domain and the remaining 1% was left to trickle through the x = 0 boundary. In the right ﬁgure, half of the heat was distributed evenly over the region from x = 0.75 to x = 1.5 and the other half trickled through the faucet.

<!-- b000779 | prose | pages [26] -->
(a) Nearly Uniform Heat Distribution (b) Split Heat Distribution

<!-- b000780 | caption | pages [26] -->
Figure 17: Eﬀects of Redistribution of Water

<!-- b000781 | furniture | pages [26] -->
26

<!-- b000782 | furniture | pages [26] -->
26

<!-- b000783 | furniture | pages [27] -->
Team # 44845

<!-- b000784 | prose | pages [27] -->
8

<!-- b000785 | heading | pages [27] -->
Model Comparison

<!-- b000786 | furniture | pages [27] -->
Page 27 of 44

<!-- b000787 | prose | pages [27] -->
In this section we present and discuss the major results from both the analytical and nu- merical models, commenting on the eﬀectiveness and validity of each model.

<!-- b000788 | prose | pages [27] -->
8.1

<!-- b000789 | heading | pages [27] -->
Solution Metrics

<!-- b000790 | prose | pages [27] -->
First, we must develop a metric with which to evaluate our solutions. To do this, we return to the original objective: Joe wishes to attain a desired temperature uniformly distributed throughout the bath. The desired temperature constraint and the uniform distribution con- straint will be decoupled and evaluated separately.

<!-- b000791 | prose | pages [27] -->
The ﬁrst metric evaluates the total heat within the bath, addressing the desired temper- ature constraint. This objective function will be called u, as deﬁned in Equation 54.

<!-- b000792 | prose | pages [27] -->
u(t) = uavg(t) −uobj (54)

<!-- b000793 | prose | pages [27] -->
This metric will yield a time-dependent value proportional in magnitude to the diﬀerence between the average and objective, with a sign that denotes whether the bath is below or above the objective temperature. As a standard value, the objective temperature of the water will always be a comfortable 37◦C.

<!-- b000794 | prose | pages [27] -->
The second metric quantiﬁes the uniformity of the temperature distribution over time. We will deﬁne this metric as σ, the standard deviation of the temperature distribution at a given point in time. The equation for the standard deviation is given below in Equation 55.

<!-- b000795 | prose | pages [27] -->
v

<!-- b000796 | prose | pages [27] -->
N

<!-- b000797 | prose | pages [27] -->
u t 1 u

<!-- b000798 | prose | pages [27] -->
X

<!-- b000799 | prose | pages [27] -->
σ(t) =

<!-- b000800 | prose | pages [27] -->
N

<!-- b000801 | prose | pages [27] -->
n=1

<!-- b000802 | prose | pages [27] -->
(un(t) −uavg)2 (55)

<!-- b000803 | prose | pages [27] -->
The evolution of the objective functions (metrics) through time for the numerical model with nominal parameters is shown below, along with the heat map describing the temperature distribution.

<!-- b000804 | prose | pages [27] -->
(a) Heat Map of Simulation (b) Objective Functions From Simulation

<!-- b000805 | caption | pages [27] -->
Figure 18: Demonstration of the Objective Functions, u(t) and σ(t) With Nominal Param-

<!-- b000806 | prose | pages [27] -->
eters

<!-- b000807 | furniture | pages [27] -->
27

<!-- b000808 | furniture | pages [27] -->
27

<!-- b000809 | furniture | pages [28] -->
Team # 44845

<!-- b000810 | furniture | pages [28] -->
Page 28 of 44

<!-- b000811 | prose | pages [28] -->
By comparing the two plots, the eﬀectiveness of the objective functions is clear; the temperature becomes less uniform as we add too much heat to the system resulting in an increase in the average temperature objective function. In order for Joe to be happy with his bath, our goal is to drive both of these objective functions to zero. As a standard, we will always consider the temperature distribution at the end of a one hour bath. With well deﬁned metrics now in place, simulations can be run to test the impact of each parameter on the solutions from both the analytical and numerical models. The following subsections will each describe the eﬀect of a diﬀerent parameter on the solution metrics.

<!-- b000812 | prose | pages [28] -->
8.2 Eﬀect of Bathtub Geometry

<!-- b000813 | prose | pages [28] -->
The ﬁrst parameters under consideration are the physical dimensions of the bathtub. Chang- ing the dimensions of the bath changes the surface areas exposed to the air, the velocity of the water ﬂow, and the extensive properties of the ﬂuid element such as mass and volume. Below, we examine the eﬀect of changing the length of the bathtub while holding all other parameters constant.

<!-- b000814 | heading | pages [28] -->
(b) Numerical Model

<!-- b000815 | heading | pages [28] -->
(a) Analytical Model

<!-- b000816 | caption | pages [28] -->
Figure 19: Eﬀects of Variation of Length in Both Models

<!-- b000817 | prose | pages [28] -->
By increasing the length of the bathtub, the error and standard deviation both increase in magnitude for the analytical solution but both decrease in magnitude for the numerical solution which are notably inconsistent results. The analytical model only takes into account the heat diﬀusion term while the numerical model also accounts for heat convection due to the bulk ﬂow of the water. This fundamental diﬀerence is likely the reason for these inconsistent results.

<!-- b000818 | prose | pages [28] -->
When considering the more accurate numerical model (convection and diﬀusion) with longer bathtubs, the water is both more uniform and, on average, closer to the objective temperature. As the ﬂow rate is held at its nominal value, a longer bathtub will be less aﬀected by the inﬂux of hot water. The increased error of the analytical model, on the other hand, is due to the low thermal diﬀusivity of water in comparison to the heat loss of the system. Although hot water is being added to the bath, it cools at a faster rate than the

<!-- b000819 | furniture | pages [28] -->
28

<!-- b000820 | furniture | pages [29] -->
Team # 44845

<!-- b000821 | furniture | pages [29] -->
Page 29 of 44

<!-- b000822 | prose | pages [29] -->
heat can diﬀuse through it. Thus, heat builds up at the faucet end of the tub, increasing both error and standard deviation.

<!-- b000823 | prose | pages [29] -->
A similar study was conducted on the eﬀect of bathtub width, and the results from both models are shown below.

<!-- b000824 | heading | pages [29] -->
(b) Numerical Model

<!-- b000825 | heading | pages [29] -->
(a) Analytical Model

<!-- b000826 | caption | pages [29] -->
Figure 20: Eﬀects of Variation of Width in Both Models

<!-- b000827 | prose | pages [29] -->
In this case, the two models qualitatively agree with one another; the temperature error magnitude and the standard deviation are decreasing as width is increased.This result is consistent with the ﬁndings of the length variation in the numerical model. The eﬀect of increasing the width is to increase the area exposed to air while maintaining the distance in the direction of diﬀusion and bulk ﬂow. This increase results in a more uniform temperature distribution as the heat build-up at the inlet is oﬀset by increased heat loss.

<!-- b000828 | prose | pages [29] -->
Next, the height dimension was varied and the results from the sensitivity analysis are presented below.

<!-- b000829 | heading | pages [29] -->
(a) Analytical Model

<!-- b000830 | heading | pages [29] -->
(b) Numerical Model

<!-- b000831 | caption | pages [29] -->
Figure 21: Eﬀects of Variation of Height in Both Models

<!-- b000832 | furniture | pages [29] -->
29

<!-- b000833 | furniture | pages [30] -->
Team # 44845

<!-- b000834 | furniture | pages [30] -->
Page 30 of 44

<!-- b000835 | prose | pages [30] -->
This ﬁgure mirrors very closely the result from the width variation, as both the width and height are the two dimensions through which the water is assumed to not ﬂow or diﬀuse heat.

<!-- b000836 | prose | pages [30] -->
Finally, a simultaneous variation of all three dimensions is implemented. This “volume factor” is the ratio of volume to nominal volume. The results from this analysis are shown in Figure 22 below.

<!-- b000837 | heading | pages [30] -->
(b) Numerical Model

<!-- b000838 | heading | pages [30] -->
(a) Analytical Model

<!-- b000839 | caption | pages [30] -->
Figure 22: Eﬀects of Variation of Volume in Both Models

<!-- b000840 | prose | pages [30] -->
These results reﬂect those of the height and width variations, which suggests that height and width are more signiﬁcant parameters in describing the temperature distribution through- out the bathtub, because they correlate strongly with convective heat losses to the air.

<!-- b000841 | prose | pages [30] -->
The results from this subsection emphasize the strength of the numeric model over the analytical model due to the importance of the bulk motion of the water, which is only accounted for in the numerical model.

<!-- b000842 | prose | pages [30] -->
8.3 Eﬀect of Adding Soap

<!-- b000843 | prose | pages [30] -->
If Joe were to use a bubble bath additive or soap, this would change the thermal properties of the water which would ultimately result in a change in thermal diﬀusivity. The primary ingredient of soap is sodium stearate which is also used in bubble bath solutions. The density of sodium stearate is 1020 kg/m3 [8]. This density is nearly identical to that of water and as such should have little to no eﬀect on the density of the water when dissolved especially as the soap to water ratio would be small in a full bath. By adding a solute such as sodium chloride to pure water, the thermal conductivity decreases as solute concentration increases[9]; it is a reasonable assumption that adding sodium stearate results in a similar eﬀect.

<!-- b000844 | prose | pages [30] -->
Overall, the approximately inconsequential addition of sodium stearate to water in re- alistic concentrations slightly reduces the diﬀusivity of the water. To perform a sensitivity analysis of this parameter, a wide range of diﬀusivities (a full order of magnitude about the standard diﬀusivity of water) was tested. This wide range was used to in order to show a noticeable change in solution behavior. Final temperature distributions after one hour are

<!-- b000845 | furniture | pages [30] -->
30

<!-- b000846 | furniture | pages [31] -->
Team # 44845

<!-- b000847 | furniture | pages [31] -->
Page 31 of 44

<!-- b000848 | prose | pages [31] -->
shown for various values of thermal diﬀusivity below with the ﬁgure at right magnifying the area of interest.

<!-- b000849 | prose | pages [31] -->
(a) Varied of Diﬀusivity over Full Length (b) Magniﬁed Variations of Diﬀusivity

<!-- b000850 | caption | pages [31] -->
Figure 23: Eﬀects of Variation of Thermal Diﬀusivity in Numerical Model

<!-- b000851 | prose | pages [31] -->
The thermal diﬀusivity has very little eﬀect on the solution, especially considering the wide range of thermal diﬀusivities tested. This continues to support the hypothesis that the heat transfer is primarily due to bulk ﬂow and not diﬀusion. By examining the P´eclet number (Pe)[10], we can conﬁrm this hypothesis. The Peclet number is the ratio of the convective transport rate to the diﬀusive transport rate, as shown below with our nominal values.

<!-- b000852 | prose | pages [31] -->
α = (1.2 × 10−4 m/s)(1.5 m)

<!-- b000853 | prose | pages [31] -->
Pe = vL

<!-- b000854 | prose | pages [31] -->
≈1223 >> 1 (56) 1.472 × 10−7 m2/s

<!-- b000855 | prose | pages [31] -->
This large ratio conﬁrms that diﬀusion eﬀects are negligible in comparison with bulk motion eﬀects, due to the low thermal diﬀusivity of water. From this point onward, only the numerical model will be considered as the analytical model fails to capture the most important mechanism of heat transfer: bulk ﬂuid motion.

<!-- b000856 | prose | pages [31] -->
Eﬀect of Varied Input Temperature and Flow Rate 8.4

<!-- b000857 | prose | pages [31] -->
Up to this point, sensitivity analyses have been presented for the physical parameters of the system: the dimensions/shape of the bath and the thermal properties of the water in the bath. The next set of sensitivity analyses will be focused on the parameters that can vary during the course of the bath: the input water stream and the properties of Joe himself. First we analyze the eﬀect of changing the input water temperature and mass ﬂow rate. The results from this analysis are shown below in Figure 24.

<!-- b000858 | furniture | pages [31] -->
31

<!-- b000859 | furniture | pages [31] -->
31

<!-- b000860 | furniture | pages [32] -->
Team # 44845

<!-- b000861 | furniture | pages [32] -->
Page 32 of 44

<!-- b000862 | prose | pages [32] -->
(b) Variation of Mass Flow Rate (a) Variation of Input Temperature

<!-- b000863 | caption | pages [32] -->
Figure 24: Eﬀects of Varied Input Temperature and Mass Flow at Input

<!-- b000864 | prose | pages [32] -->
Increasing either parameter corresponds to an increase of net energy in the system. An- other important result is that a large ﬂow rate will result in a more uniform distribution when compared with a high temperature inlet. This is because increasing the mass ﬂow rate increases the convective term, which is more eﬃcient than the diﬀusion. The x intercepts of the blue lines on each plot represent important values, namely the input temperature or mass ﬂow required to add the correct amount of heat to the system to maintain the objective temperature.

<!-- b000865 | prose | pages [32] -->
Heat maps for a low (35◦C) and high (50◦C) inlet temperature are shown below to further validate the model.

<!-- b000866 | prose | pages [32] -->
(a) Low Input Temperature (b) High Input Temperature

<!-- b000867 | caption | pages [32] -->
Figure 25: Heat Map Comparison of Input Temperature Eﬀect in Numerical Model

<!-- b000868 | prose | pages [32] -->
In both cases, the input water convects across the bath, with a slight diﬀusive eﬀect present at the boundary between the input water and the initial water. The rate of bulk ﬂuid motion is clearly visible as the diagonal line of large temperature gradient. Similarly, heat maps for zero mass ﬂow and high mass ﬂow (twice the nominal value) are shown below.

<!-- b000869 | furniture | pages [32] -->
32

<!-- b000870 | furniture | pages [33] -->
Team # 44845

<!-- b000871 | furniture | pages [33] -->
Page 33 of 44

<!-- b000872 | prose | pages [33] -->
(b) High Mass Flow Rate (a) Zero Mass Flow Rate

<!-- b000873 | caption | pages [33] -->
Figure 26: Heat Map Comparison of Mass Flow Rates in Numerical Model

<!-- b000874 | prose | pages [33] -->
In the zero mass ﬂow case, the water temperature is uniform at any given time, but is slowly cooling due to thermal energy loss into the surroundings. In the high mass ﬂow rate case, the increased rate of bulk ﬂuid motion can be seen. After one hour, the high temperature water has moved farther into the bath.

<!-- b000875 | prose | pages [33] -->
8.5 Eﬀect of Varied Size and Position of Bather

<!-- b000876 | prose | pages [33] -->
The ﬁnal parameter to be analyzed in the simulation of the bathtub is Joe himself. Any given bather may have diﬀerent properties, such as width, length, temperature, or ability to transfer heat to or from the system.

<!-- b000877 | prose | pages [33] -->
These possible variations in parameters will be broken into two diﬀerent categories: phys- ical dimensions of the bather and the thermal properties of the bather. Below are the plots of the eﬀects of the geometric parameters on the objective functions.

<!-- b000878 | prose | pages [33] -->
(b) Eﬀect of Body Surface Area (a) Eﬀect of Body Length

<!-- b000879 | caption | pages [33] -->
Figure 27: Impact of Body Shape and Size on Objective Functions

<!-- b000880 | furniture | pages [33] -->
33

<!-- b000881 | furniture | pages [34] -->
Team # 44845

<!-- b000882 | furniture | pages [34] -->
Page 34 of 44

<!-- b000883 | prose | pages [34] -->
Neither Joe’s body length nor his circumference (surface area per unit length) have a signiﬁcant eﬀect on the temperature distribution.

<!-- b000884 | prose | pages [34] -->
It is only for a very long body (near the length of the bath itself) that uniformity and average temperature error are slightly improved. These results suggest that the physical dimensions of the bather have a negligible eﬀect on the objective functions, due to the fact that the body temperature is close to the temperature of the bath.

<!-- b000885 | prose | pages [34] -->
The eﬀects of the Joe’s thermal parameters are shown below.

<!-- b000886 | prose | pages [34] -->
(b) Body-Water Heat Transfer Coeﬃcient (a) Eﬀect of Body Temperature

<!-- b000887 | caption | pages [34] -->
Figure 28: Impact of Thermal Properties of Body on Objective Functions

<!-- b000888 | prose | pages [34] -->
The ﬁrst sub-ﬁgure shows that Joe’s body temperature has a slightly more signiﬁcant impact than the geometry, which makes sense considering the diﬀerence in temperature between Joe and the water. However, it is important to note that this sensitivity is shown over a large range. The heat transfer coeﬃcient has little to no impact, once again due to the small temperature diﬀerence between Joe and the water.

<!-- b000889 | prose | pages [34] -->
9 Control Theory and Implementation

<!-- b000890 | prose | pages [34] -->
In this section, we examine the implementation of closed-loop control for the regulation of average temperature and temperature uniformity. Up to this point, we have only considered cases where the initial and objective temperatures are the same. This correlates to Joe being proactive and attempting to mitigate the heat loss before the temperature drops noticeably. Now, we consider the case where the initial temperature is uniform, but noticeably lower than the objective, a potentially more realistic application.

<!-- b000891 | prose | pages [34] -->
9.1 PID Control Theory

<!-- b000892 | prose | pages [34] -->
Joe’s ultimate goal is to experience a bath that is both maintained at a desired temperature and uniform in temperature through the water. Up to this point, many of the parameters that inﬂuence the response of the temperature distribution have been analyzed. However, the time dependence of these sensitivities has not been considered. We wish to develop a

<!-- b000893 | furniture | pages [34] -->
34

<!-- b000894 | furniture | pages [35] -->
Team # 44845

<!-- b000895 | furniture | pages [35] -->
Page 35 of 44

<!-- b000896 | prose | pages [35] -->
time dependent strategy for Joe to achieve a uniform bath at the objective temperature using Proportional-Integral-Derivative (PID) control.

<!-- b000897 | prose | pages [35] -->
The ﬁrst portion of the control system is designed only to achieve and maintain the objective temperature by using the average temperature metric detailed previously. Proper distribution can only take place if the correct amount of energy is already present in the system. As the net amount of heat in the bath is directly controlled by the faucet, this segment of the control system will focus on optimization of the inlet temperature and ﬂow rate of the water from the faucet.

<!-- b000898 | prose | pages [35] -->
PID control is implemented through the selection of the gains associated with each com- ponent of the control. Below in Equation 57 is the general gain equation of a PID controller as a function of the objective u(t) with variable gains K for each stage, where f(t) represents the calculated forcing (input).

<!-- b000899 | prose | pages [35] -->
f(t) = Kpu(t) + Ki

<!-- b000900 | prose | pages [35] -->
Each of the three components of a PID controller corresponds primarily to a speciﬁc response of the system.

<!-- b000901 | prose | pages [35] -->
The proportional control element is based on the diﬀerence between actual temperature and objective temperature; this control is what physically drives the system to the objective. The inte- gral component deﬁnes the response on ac- cumulated error from the objective instead of current error, decreasing the rise time and removing the steady state error from the sys- tem. The derivative component predicts the response error based on the temporal deriva- tive of the response, damping any oscilla- tions.

<!-- b000902 | prose | pages [35] -->
At right is an image of the eﬀects of each of the three components of a PID controller with properly tuned gains. Properly tuning

<!-- b000903 | prose | pages [35] -->
Z t

<!-- b000904 | prose | pages [35] -->
∂u(t)

<!-- b000905 | prose | pages [35] -->
u(τ)dτ + Kd

<!-- b000906 | prose | pages [35] -->
(57) ∂t

<!-- b000907 | prose | pages [35] -->
0 0

<!-- b000908 | caption | pages [35] -->
Figure 29:

<!-- b000909 | prose | pages [35] -->
Illustration of Properly Tuned PID Controller[11]

<!-- b000910 | prose | pages [35] -->
each gain results in the optimal responses described: a small rise time with minimal oscilla- tion and no steady state error.

<!-- b000911 | heading | pages [35] -->
Implementation of PID Control in Numerical Model

<!-- b000912 | prose | pages [35] -->
9.2

<!-- b000913 | prose | pages [35] -->
PID control was implemented in the numerical model by simply specifying the forcing as a function of u(t), as shown in Equation 57. In particular, we set

<!-- b000914 | prose | pages [35] -->
f(t) = ˙m(uin −u(x = 0, t)),

<!-- b000915 | prose | pages [35] -->
a term in the inlet Neumann condition.

<!-- b000916 | prose | pages [35] -->
(58)

<!-- b000917 | prose | pages [35] -->
In addition, the gain coeﬃcients needed to be determined. These gain coeﬃcients should weight the response with the ultimate goal of achieving a response with minimal rise time,

<!-- b000918 | furniture | pages [35] -->
35

<!-- b000919 | furniture | pages [35] -->
35

<!-- b000920 | furniture | pages [36] -->
Team # 44845

<!-- b000921 | furniture | pages [36] -->
Page 36 of 44

<!-- b000922 | prose | pages [36] -->
little to no overshoot, and long term stability. These desired responses have strong grounding in the reality of the physical system. The rise time is desired to be short so that Joe does not have to wait long for his bath to reach the objective temperature. Too much overshoot could result in Joe being burned, and is thus not desired. Finally, long term stability reﬂects the maintenance of the desired temperature over the course of the entire bath duration.

<!-- b000923 | prose | pages [36] -->
There are many methods for determining optimal gains, including PID control software and algorithms such as the Ziegler-Nichols tuning process, but due to the lack of a well deﬁned transfer function in the numerical approach, neither option is applicable and manual tuning is required.

<!-- b000924 | prose | pages [36] -->
We manually tuned our gains in order to obtain a roughly optimal response. In no way are the following system responses the result of optimal gains; much more tuning would be required for such an optimization. Below, we present the system response using only proportional control, starting at 30◦C and attempting to reach 37◦C.

<!-- b000925 | caption | pages [36] -->
Figure 30: Eﬀect of Proportional Control

<!-- b000926 | prose | pages [36] -->
There are noticeable oscillations in the objective function (the blue line) and there is an overshoot of about 4◦C. Since the forcing is a function of both mass ﬂow and inlet temperature, we ﬁx mass ﬂow and present the result as the required ∆u (the red line). The ∆u peaks at around 20◦C, meaning that the inlet water temperature must be 20◦C hotter than the current water temperature at the inlet.

<!-- b000927 | prose | pages [36] -->
Using full PID, the results from the same analysis are shown below in Figure 31.

<!-- b000928 | furniture | pages [36] -->
36

<!-- b000929 | furniture | pages [37] -->
Team # 44845

<!-- b000930 | furniture | pages [37] -->
Page 37 of 44

<!-- b000931 | caption | pages [37] -->
Figure 31: Optimal Control of Average Bath Temperature

<!-- b000932 | prose | pages [37] -->
The objective function is driven to nearly zero, as desired. More importantly, the response is achieved with a relatively short rise time, minimal overshoot, and maximal oscillation of less than a degree. The associated forcing function is more reasonable, requiring a maximum ∆u of about 3◦C.

<!-- b000933 | prose | pages [37] -->
9.3 Control of Uniformity of Water Temperature Distribution

<!-- b000934 | prose | pages [37] -->
With the average temperature of the water driven to the objective temperature using PID control, the only remaining factor is the uniformity of the temperature distribution. The method of maintaining uniformity is very simple: instead of adding heat from the faucet to the bathtub at x = 0, we evenly distribute the hot water over the whole bath. Physically, this method corresponds to Joe continuously redirecting the water from the faucet, using a cup or another redistribution system.

<!-- b000935 | prose | pages [37] -->
Logically, it makes sense to evenly distribute the heat throughout the bathtub. Assuming an initial temperature of 37◦C and an objective temperature of 37◦C (which corresponds to Joe being proactive about the heat loss in the bath), this logical argument is easily veriﬁed. In Figure 32 below, we show the objective functions vs. inlet temperature, where the heat is being distributed evenly and the mass ﬂow is ﬁxed. We also show the heat map using the optimized input temperature.

<!-- b000936 | furniture | pages [37] -->
37

<!-- b000937 | furniture | pages [38] -->
Team # 44845

<!-- b000938 | furniture | pages [38] -->
Page 38 of 44

<!-- b000939 | prose | pages [38] -->
(a) Optimal Input Temperature (b) Heat Map of Optimized Uniformity

<!-- b000940 | caption | pages [38] -->
Figure 32: Determination of Optimal Input Temperature with Prescribed Flow Rate

<!-- b000941 | prose | pages [38] -->
The uniformity objective function (the red line) is maintained at zero which conﬁrms the hypothesis that uniform heat distribution is most eﬀective. The heat map demonstrates that using the optimal input temperature for the given mass ﬂow rate results in a perfect bath. The same results are shown in 33 below, this time varying the mass ﬂow with a ﬁxed inlet temperature.

<!-- b000942 | prose | pages [38] -->
(b) Heat Map of Optimized Uniformity (a) Optimal Mass Flow Rate

<!-- b000943 | caption | pages [38] -->
Figure 33: Determination of Optimal Mass Flow Rate with Prescribed Nominal Input

<!-- b000944 | prose | pages [38] -->
Temperature

<!-- b000945 | prose | pages [38] -->
Just as before, there exists an optimal mass ﬂow, and using this mass ﬂow with uniform distribution, a perfect bath is once again achieved.

<!-- b000946 | furniture | pages [38] -->
38

<!-- b000947 | furniture | pages [39] -->
Team # 44845

<!-- b000948 | furniture | pages [39] -->
Page 39 of 44

<!-- b000949 | prose | pages [39] -->
9.4 Final PID Control with With Manual Heat Distribution

<!-- b000950 | prose | pages [39] -->
We close with a simultaneous consideration of average temperature (PID) control and unifor- mity control. Up to this point, we have analyzed these control methods separately and under diﬀerent initial conditions, but to complete our model of the problem it is essential that we implement them simultaneously. The initial condition will be a 30◦C uniform bath, and the objective will be 37◦C, accurately modeling Joe’s realization that his bath has become cold.

<!-- b000951 | prose | pages [39] -->
The combined model will eﬀectively implement the two control methods by using PID control to determine required temperature of the incident water (given a constant nominal mass ﬂow rate), and using intelligent input water redistribution to maintain uniformity. The intelligent redistribution was determined by tweaking the locations at which the input water is distributed. Ultimately, it was determined that distributing inlet water over the region from x = 0 m (the faucet) to the location that the body starts, x = 0.25 m for the nominal case, is optimal. This allows the body heat to convect downstream and the inlet heat to warm the water upstream of the body.

<!-- b000952 | prose | pages [39] -->
After manually tuning the gains and implementing full PID in addition to intelligent inlet water distribution, the following results are obtained.

<!-- b000953 | prose | pages [39] -->
(b) Uniformity over Time (a) PID Control with Manual Heat Distribution

<!-- b000954 | caption | pages [39] -->
Figure 34: PID System Response Using Intelligent Heat Distribution

<!-- b000955 | prose | pages [39] -->
On the left, the average temperature objective function is shown to rise to zero relatively quickly with no overshoot, an optimal result. Additionally, the required ∆u with a nominal ﬂow rate is physically reasonable. On the right, the temperature uniformity is shown to initially increase (due to Joe’s body) but settle to zero as the inlet water distribution begins to have an eﬀect.

<!-- b000956 | prose | pages [39] -->
The heat map corresponding to this control is shown below in Figure 35.

<!-- b000957 | furniture | pages [39] -->
39

<!-- b000958 | furniture | pages [40] -->
Team # 44845

<!-- b000959 | furniture | pages [40] -->
Page 40 of 44

<!-- b000960 | caption | pages [40] -->
Figure 35: Heat Map of PID System Response Using Intelligent Heat Distribution

<!-- b000961 | prose | pages [40] -->
This result illustrates the optimal strategy that Joe can take to increase his bath tem- perature to his objective while keeping the temperature distribution uniform and only using a nominal trickle of water. He should use PID control to vary the input temperature and si- multaneously use a cup or other redirecting device to continuously distribute the inlet water over the region of the bathtub that is upstream of his body.

<!-- b000962 | prose | pages [40] -->
10 Final Remarks

<!-- b000963 | prose | pages [40] -->
We have now completed our mathematical modeling of the bathtub. In this section, we will conclude our paper, commenting on each of our models and presenting ideas for future work.

<!-- b000964 | prose | pages [40] -->
10.1

<!-- b000965 | heading | pages [40] -->
Strengths and Weaknesses of Solution Models

<!-- b000966 | prose | pages [40] -->
Each of our ﬁnal models had very speciﬁc strengths and weaknesses. Below are a list of strengths and weaknesses for the three models developed in this report: the steady state uniform model, the analytical model of heat diﬀusion, and the numerical model of the convection-diﬀusion equation.

<!-- b000967 | heading | pages [40] -->
Steady State, Uniform Temperature Model

<!-- b000968 | prose | pages [40] -->
Strengths:

<!-- b000969 | prose | pages [40] -->
• The implementation is straightforward and the derivation is based solely on thermo- dynamics.

<!-- b000970 | prose | pages [40] -->
• The results can be used to qualitatively predict the results of more complicated models.

<!-- b000971 | prose | pages [40] -->
Weaknesses:

<!-- b000972 | prose | pages [40] -->
• No spatial or temporal dependence is considered.

<!-- b000973 | furniture | pages [40] -->
40

<!-- b000974 | furniture | pages [41] -->
Team # 44845

<!-- b000975 | furniture | pages [41] -->
Page 41 of 44

<!-- b000976 | heading | pages [41] -->
Analytical Solution Model

<!-- b000977 | prose | pages [41] -->
Strengths:

<!-- b000978 | prose | pages [41] -->
• Time dependent boundary conditions and both a spatially and temporally dependent forcing function (heat source) can be eﬀectively modeled.

<!-- b000979 | prose | pages [41] -->
• The boundary conditions can be customized to reﬂect the physical system.

<!-- b000980 | prose | pages [41] -->
• The model yields a highly accurate analysis of characteristic transient solutions over one dimensional space due to heat diﬀusion.

<!-- b000981 | prose | pages [41] -->
Weaknesses:

<!-- b000982 | prose | pages [41] -->
• Bulk ﬂow of the ﬂuid is not modeled.

<!-- b000983 | prose | pages [41] -->
• The simulation implementation proved challenging when considering various types of boundaries and sources.

<!-- b000984 | heading | pages [41] -->
Numerical Convection-Diﬀusion Model

<!-- b000985 | prose | pages [41] -->
Strengths:

<!-- b000986 | prose | pages [41] -->
• Solution incorporates eﬀects of both convection and diﬀusion for a realistic ﬂuid ther- modynamic simulation.

<!-- b000987 | prose | pages [41] -->
• Time dependent boundaries and a spatially and temporally dependent heat source can be customized.

<!-- b000988 | prose | pages [41] -->
• The straightforward implementation of simulations allows for a variety of tests of pa- rameter sensitivity analyses as well as the implementation of control.

<!-- b000989 | prose | pages [41] -->
• The numerical approach allows for the possibility of expansion of the simulations into a multidimensional model.

<!-- b000990 | prose | pages [41] -->
Weaknesses:

<!-- b000991 | prose | pages [41] -->
• The foundational mathematics of this numerical implementation are highly involved.

<!-- b000992 | prose | pages [41] -->
The greatest overall strength of all of the models was their generality. This allowed for a wide range of parameter customization, from dimensions of the bath, types of boundaries en- forced on the system, heat transfer coeﬃcients, eﬀects of Joe in the system, and ﬁnal control application. The main weakness of our models is that they only consider one-dimensional heat ﬂow. In reality, the thermal-ﬂuid eﬀects in a bathtub will be largely three-dimensional.

<!-- b000993 | furniture | pages [41] -->
41

<!-- b000994 | furniture | pages [42] -->
Team # 44845

<!-- b000995 | furniture | pages [42] -->
Page 42 of 44

<!-- b000996 | prose | pages [42] -->
10.2

<!-- b000997 | heading | pages [42] -->
Future Model Development

<!-- b000998 | prose | pages [42] -->
As discussed in the weaknesses of the models, many possibilities exist for the development of a more precise model. In the future, a more comprehensive and deﬁnitive model would be developed in the following ways:

<!-- b000999 | prose | pages [42] -->
• Expand the models to incorporate more detailed information through increasing the dimensionality of each model, more accurately reﬂecting a physical three-dimensional system.

<!-- b001000 | prose | pages [42] -->
• Conduct experimental trials and extensive research to ensure the accuracy of certain physical parameters, such as transfer coeﬃcients for humans or precise eﬀect of soluble materials on water’s thermal properties.

<!-- b001001 | prose | pages [42] -->
• Apply geometry and coordinate transformations to explore the eﬀect of various geome- tries on the system, such as cylindrical and trapezoidal geometries.

<!-- b001002 | prose | pages [42] -->
• Analyze the steady-state distribution of the thermal energy with high accuracy across three dimensions through implementation of Laplace’s Equation, spatially dependent boundary conditions, and realistic heat loss.

<!-- b001003 | prose | pages [42] -->
10.3

<!-- b001004 | heading | pages [42] -->
Conclusions

<!-- b001005 | prose | pages [42] -->
In this paper, we modeled the temperature distribution in a bathtub in space and time in order to determine the most eﬀective method of uniformly increasing the temperature. Three models were developed to describe this temperature distribution: a steady state uniform model, an analytical heat equation model, and a numerical convection-diﬀusion equation model. Ultimately, the numerical model proved most accurate because it alone took into account bulk ﬂuid motion, the dominant heat transfer eﬀect. Using this model and the analytical model, we conducted sensitivity analyses on diﬀerent parameters to explore the eﬀects of diﬀerent bathtub geometries, the addition of soap, and other variations to the problem at hand. We also implemented PID control of the inlet water temperature and intelligent distribution of inlet water. By optimizing this process, we eﬀectively developed a strategy for quickly re-heating the bath while maintaining uniformity. Overall, our model showed that well-tuned PID control combined with distributing the inlet water upstream of the bather proved to be the most eﬀective strategy.

<!-- b001006 | furniture | pages [42] -->
42

<!-- b001007 | furniture | pages [43] -->
Team # 44845

<!-- b001008 | furniture | pages [43] -->
Page 43 of 44

<!-- b001009 | heading | pages [43] -->
References

<!-- b001010 | references | pages [43] -->
[1] ”IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and

<!-- b001011 | references | pages [43] -->
Steam.” International Steam Tables (2008): 7-150. Web.

<!-- b001012 | references | pages [43] -->
[2] Cengel, Yunus A, and Robert H. Turner. Fundamentals of Thermal-Fluid Sciences.

<!-- b001013 | references | pages [43] -->
Boston: McGraw-Hill, 2001. Print.

<!-- b001014 | references | pages [43] -->
[3] Boutelier, C., L. Bougues, and J. Timbal. “Experimental Study of Convective Heat

<!-- b001015 | references | pages [43] -->
Transfer Coeﬃcient for the Human Body in Water.” US National Library of Medicine

<!-- b001016 | references | pages [43] -->
(1977). PubMed.gov. Web. 31 Jan. 2016.

<!-- b001017 | references | pages [43] -->
[4] Grigoryan, Viktor. “Inhomogeneous Boundary Value Problems.” Math 12B, Fourier Se-

<!-- b001018 | references | pages [43] -->
ries and Numerical Methods. University of California, Santa Barbara, 31 Jan. 2012. Web.

<!-- b001019 | references | pages [43] -->
30 Jan. 2016.

<!-- b001020 | references | pages [43] -->
[5] Haberman, Richard. Applied Partial Diﬀerential Equations: With Fourier Series and

<!-- b001021 | references | pages [43] -->
Boundary Value Problems. 5th ed. Upper Saddle River, NJ: Pearson Prentice Hall, 2013.

<!-- b001022 | references | pages [43] -->
Print.

<!-- b001023 | references | pages [43] -->
[6] Ewa Majchrzak, ukasz Turchan, The Finite Diﬀerence Method for transient convection-

<!-- b001024 | references | pages [43] -->
diﬀusion problems, Scientiﬁc Research of the Institute of Mathematics and Computer

<!-- b001025 | references | pages [43] -->
Science, 2012, Volume 11, Issue 1, pages 63-72.

<!-- b001026 | references | pages [43] -->
[7] Burden, Richard L, and J D. Faires. Numerical Analysis. Belmont, CA: Thomson

<!-- b001027 | references | pages [43] -->
Brooks/Cole, 2005. Print.

<!-- b001028 | references | pages [43] -->
[8] “Sodium Stearate (CAS 822-16-2).” Sodium Stearate. Santa Cruz Biotechnology, 2007.

<!-- b001029 | references | pages [43] -->
Web. 31 Jan. 2016.

<!-- b001030 | references | pages [43] -->
[9] Martinez, Isidoro. ”Properties of Particular Solutions.” UPM, Jan. 1995. Web. 1 Feb.

<!-- b001031 | references | pages [43] -->
2016.

<!-- b001032 | references | pages [43] -->
[10] ”5. Advection and Diﬀusion of an Instantaneous Release.” MIT.edu. Massachusetts

<!-- b001033 | references | pages [43] -->
Institute of Technology. Web. 1 Feb. 2016.

<!-- b001034 | references | pages [43] -->
[11] PID Compensation. Digital image. PID Controller. Wikipedia, 28 May 2015. Web. 30

<!-- b001035 | references | pages [43] -->
Jan. 2016.

<!-- b001036 | furniture | pages [43] -->
43

<!-- b001037 | references | pages [44] -->
Superior Products, L.L.C.*

<!-- b001038 | references | pages [44] -->
Letter to International Society for the

<!-- b001039 | references | pages [44] -->
Promotion of Comfort and Cleanliness

<!-- b001040 | references | pages [44] -->
2/1/16

<!-- b001041 | references | pages [44] -->
As many of you are likely aware, there

<!-- b001042 | references | pages [44] -->
has been a singular problem facing avid bath

<!-- b001043 | references | pages [44] -->
users for many generations. Though we have

<!-- b001044 | references | pages [44] -->
come quite far as a society with the invention

<!-- b001045 | references | pages [44] -->
of running water, synthetic bathtub materi-

<!-- b001046 | references | pages [44] -->
als, and even advances in soap and shampoo

<!-- b001047 | references | pages [44] -->
solutions, the issue of keeping your bath at a

<!-- b001048 | references | pages [44] -->
comfortable temperature without pockets of

<!-- b001049 | references | pages [44] -->
cold or hot water has not been improved upon

<!-- b001050 | references | pages [44] -->
for generations.

<!-- b001051 | references | pages [44] -->
Solutions

<!-- b001052 | references | pages [44] -->
range

<!-- b001053 | references | pages [44] -->
from

<!-- b001054 | references | pages [44] -->
self-circulating

<!-- b001055 | references | pages [44] -->
baths, expensive water jets, or even the de-

<!-- b001056 | references | pages [44] -->
ferring of a magniﬁcent bath to a common

<!-- b001057 | references | pages [44] -->
shower, but an explanation has slowly pre-

<!-- b001058 | references | pages [44] -->
sented itself to the diﬃculty shrouding this

<!-- b001059 | references | pages [44] -->
dilemma. The underlying factor of the cool-

<!-- b001060 | references | pages [44] -->
ing bath problem is a combination of being

<!-- b001061 | references | pages [44] -->
able to maintain heat within the bath over the

<!-- b001062 | references | pages [44] -->
course of your soak and also to distribute any

<!-- b001063 | references | pages [44] -->
hot water you introduce to the system. This

<!-- b001064 | references | pages [44] -->
is diﬃcult due to the fact that water diﬀuses

<!-- b001065 | references | pages [44] -->
heat very poorly.

<!-- b001066 | references | pages [44] -->
Your relaxing afternoon

<!-- b001067 | references | pages [44] -->
bath is in reality a complex dynamical sys-

<!-- b001068 | references | pages [44] -->
tem, controlled by the physical phenomena

<!-- b001069 | references | pages [44] -->
of thermodynamics, heat transfer, and ﬂuid

<!-- b001070 | references | pages [44] -->
mechanics.

<!-- b001071 | references | pages [44] -->
Fortunately for the bathing community,

<!-- b001072 | references | pages [44] -->
a small percentage of our fellow bathers are

<!-- b001073 | references | pages [44] -->
not only aspiring to the ideals of cleanliness,

<!-- b001074 | references | pages [44] -->
but also ardently pursuing an understanding

<!-- b001075 | references | pages [44] -->
*This company is purely a work of ﬁction.

<!-- b001076 | references | pages [44] -->
of applied mathematics. This question of the

<!-- b001077 | references | pages [44] -->
ﬂuid dynamics of the bath tub has intrigued

<!-- b001078 | references | pages [44] -->
your friends here at Superior Products, and

<!-- b001079 | references | pages [44] -->
we have attempted to ﬁnd a solution to the

<!-- b001080 | references | pages [44] -->
age old question of how to achieve the perfect

<!-- b001081 | references | pages [44] -->
bath.

<!-- b001082 | references | pages [44] -->
Despite the daunting complexities of the

<!-- b001083 | references | pages [44] -->
common bathtub, the advent of modern com-

<!-- b001084 | references | pages [44] -->
putational methods and simulation tools has

<!-- b001085 | references | pages [44] -->
allowed for an extensive understanding of

<!-- b001086 | references | pages [44] -->
heat ﬂow within the bath. Through careful

<!-- b001087 | references | pages [44] -->
studying of the heat loss from the bath, diﬀu-

<!-- b001088 | references | pages [44] -->
sion of energy from warm to cold regions, and

<!-- b001089 | references | pages [44] -->
the bulk ﬂow of water from faucet to drain, a

<!-- b001090 | references | pages [44] -->
ﬁnal solution to your issues has been found.

<!-- b001091 | references | pages [44] -->
Ultimately, the solution involves precision

<!-- b001092 | references | pages [44] -->
control theory to deﬁne the optimal temper-

<!-- b001093 | references | pages [44] -->
ature of the incoming water at every given

<!-- b001094 | references | pages [44] -->
time of your bath. This temperature is cho-

<!-- b001095 | references | pages [44] -->
sen to achieve your ideal temperature quickly,

<!-- b001096 | references | pages [44] -->
without the risk of burning yourself. The sec-

<!-- b001097 | references | pages [44] -->
ond fundamental portion of the strategy is to

<!-- b001098 | references | pages [44] -->
spread the incoming water continuously over

<!-- b001099 | references | pages [44] -->
the surface of your bath as it enters through

<!-- b001100 | references | pages [44] -->
the faucet, possibly through the use of a cup

<!-- b001101 | references | pages [44] -->
or customized bathwater distribution device.

<!-- b001102 | references | pages [44] -->
Our generic solution can take into account

<!-- b001103 | references | pages [44] -->
any uniqueness in your speciﬁc bath, such

<!-- b001104 | references | pages [44] -->
as your desired bath temperature and your

<!-- b001105 | references | pages [44] -->
bathtub shape and size.

<!-- b001106 | references | pages [44] -->
This simple yet reﬁned strategy will en-

<!-- b001107 | references | pages [44] -->
sure that your bath is always at the perfect,

<!-- b001108 | references | pages [44] -->
uniform temperature. Feel free to use what-

<!-- b001109 | references | pages [44] -->
ever soaps, shampoos, or even enhanced bub-

<!-- b001110 | references | pages [44] -->
ble solutions to improve your bathing experi-

<!-- b001111 | references | pages [44] -->
ence.
