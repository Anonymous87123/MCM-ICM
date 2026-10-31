The overall temperature and uniformity of heat distribution are crucial to the enjoyment of a hot bath. Over time, a bath will lose heat to its surroundings; however, the temperature can be eﬀectively controlled by adding a trickle of hot water. Quantifying the optimal method of restoring heat uniformly will be the subject of this paper.

By making key assumptions, we reduce the problem to one spatial dimension with three-dimensional heat transfer considerations. We develop three independent, generic mathematical models to describe the temperature distribution of the bathtub in space and time:

• Steady State, Uniform, Thermodynamic Model: We characterize the energy and mass interactions between the system and the surroundings, deriving key physical constants used in the subsequent models.

• Analytical Model: Using Fourier analysis we derive an analytical solution to the one-dimensional heat equation with time dependent Neumann boundary conditions and temporally and spatially dependent heat generation/loss.

• Numerical Model: Using a ﬁnite diﬀerence approximation of the one-dimensional convection-diﬀusion equation, we implement an algorithm that estimates the temperature distribution over time based on bulk ﬂuid motion and diﬀusion.

We analyze the results of each of these models, performing sensitivity analyses on the input parameters and demonstrating their ﬂexibility. Ultimately, the numerical model proves the most physically accurate as it models convective ﬂuid motion, which is found to dominate thermal diﬀusion. We then implement closed-loop PID control to regulate the total thermal energy of the system. We also model an intelligent strategy for inlet water distribution in order to achieve temperature uniformity.

Ultimately, our model demonstrates that using well-tuned PID control of input water temperature and evenly distributing this water upstream of the bather quickly achieves a uniform objective temperature while conserving water.

1 Introduction

1.1 Overview

eat transfer and ﬂuid ﬂow are notoriously diﬃcult physical mechanisms to accurately H model. Over the years, much time and energy has been devoted to obtaining general solutions to these types of problems, but this eﬀort has proven largely unsuccessful. In this paper, we will analyze a speciﬁc application of heat transfer and ﬂuid mechanics: modeling the temperature distribution in a bathtub in space and time. The speciﬁc scenario is as follows:

Our friend Joseph Fourier (hereafter Joe) decides to take a warm bath and ﬁlls his bathtub to the desired temperature. After a while, he notices that the water is cooler than it was initially, and he wishes to increase the temperature by adding a trickle of warm water but does not want to disturb the uniformity of the temperature distribution in space. What should he do to most eﬀectively regain the initial temperature while keeping the temperature uniform throughout and not wasting too much water? What if he wished to eliminate the problem altogether by beginning to add water as soon as he got in the bath?

In this paper, we attempt to answer these questions for Joe. We present our mathematical models describing the temperature distribution in a bathtub in space and time. We describe the relevant physical mechanisms, mathematical development, implementation, and results of each model independently. Then, we compare the results of each model in order to evaluate their accuracy and explore the best solution for Joe. Finally, we present the strengths and weaknesses of our models and discuss ideas for future development of an ideal strategy.

1.2 Nomenclature

We begin by deﬁning a list of nomenclature (symbols) used in this report:

Abbreviation Description a Boundary condition at faucet b Boundary condition at overﬂow drain cp Speciﬁc heat Esystem Energy of a system f Controls forcing function g Gravitational acceleration GrL Grashof number h Enthalpy hb Convection heat transfer coeﬃcient through bottom surface hconv Convection heat transfer coeﬃcient ht Convection heat transfer coeﬃcient through top surface hw Convection heat transfer coeﬃcient through the walls H Height of bathtub i Spatial index variable j Temporal index variable Abbreviation Description k Thermal conductivity Kd Derivative gain constant Ki Integral gain constant Kp Proportional gain constant L Length of bathtub Lc Characteristic length m Mass n Summation index variable Nu Nusselt number p Perimeter Pe P´eclet number Pr Prandtl number Q Heat generation ˜Q Shifted heat generation RaL Rayleigh number ReL Reynolds number t Time u Temperature uavg Average temperature uin Inlet water temperature uobj Objective water temperature us Surface temperature u Diﬀerence between average and objective temperature u∞ Air temperature U Shifted temperature distribution v Flow Velocity W Width of bathtub x Length direction y Width direction z Height direction α Thermal diﬀusivity β Volume expansion coeﬃcient ϵ Porosity η Fraction of input heat to be redistributed ν Kinematic viscosity σ Standard deviation from average temperature φ Initial condition ˜φ Shifted initial condition ρ Density

1.3 Simplifying Assumptions

All of our models rely on a set of key assumptions that make the problem solvable in a concise manner. The assumptions that are used in every model are summarized below. The additional assumptions for each individual model will be detailed along with the introduction and description of that model.

• The faucet of the bathtub is placed exactly at one end of the length of the bathtub with the overﬂow drain exactly at the opposite end.

• When Joe is in the bathtub it is full. Any addition of water results immediately in a drainage of the same volume.

• The bathtub is free-standing, i.e. it is surrounded by air on all sides.

• The bathtub itself is in thermal equilibrium with the water at all times. Thus, the interface with the ambient air on all sides can be described without a separate knowl- edge of the temperature distribution within the bathtub material or the heat capacity of the bathtub.

• All radiation eﬀects are ignored. The only mechanism of stationary heat transfer is convection.

• The ambient air temperature is constant in space and time, i.e. the surroundings can be modeled as a thermal reservoir.

• The ambient air can be modeled as a stationary ideal gas at 1 bar ≈1 atm.

• No water loss due to evaporation occurs, i.e. the volume of water in the tub remains constant and the surface of the water interacts directly with dry air.

• The presence of the subject in the bathtub provides only thermal eﬀects. There is no disturbance to the ﬂow caused by the subject.

• The ﬂow is uniform, laminar, incompressible, inviscid, and quasi one-dimensional.

• Water has constant density and constant speciﬁc heat, and remains in liquid form.

• All material properties are assumed to be isotropic.

As was stated previously, additional assumptions will be described throughout the paper.

2 Geometric Considerations

We begin by deﬁning the geometry of the bathtub. The bathtub will be considered as a rectangular prism, with dimensions equal to L, W, and H as shown below in Figure 1.

There are six rectangular faces: ﬁve composed of the bathtub material and one face exposed to ambient air. The x direction is taken to be in the length of the bathtub, and y and z describe width and height directions respectively. The faucet is located at x = 0 and the drain is located at x = L. Any time that we add water to the system through the faucet, an equal volume exits through the overﬂow drain based on the assumption that the bathtub is full. Physically, modeling the temperature throughout the bathtub is a three-dimensional problem, which complicates the analysis greatly. As we consider partial diﬀerential equations (PDEs) with spatial and temporal dependence, simplifying geometric assumptions will be made in order to make the problem more approachable.

The mechanisms of heat transfer and ﬂuid ﬂow within the water will be assumed to be solely in the x direction. The temper- ature within a cross-section parallel to the yz plane will be assumed to be uniform, and can be thought of as an average temperature over that cross-section. This cross section, with volume WH∆x, is shown at right.

These two assumptions allow the three- dimensional problem within the water to be

reduced to one dimension. Heat capacity, ﬂuid ﬂow velocity, heat loss to the surround- ings, and other extensive properties of the system will retain their three dimensional nature, resulting in a ﬁnal geometric model that is fundamentally one-dimensional, but with impor- tant three-dimensional eﬀects preserved. The details of this preservation will be presented along with each individual model development.

3 Thermodynamic Considerations

Next, we examine the key thermodynamic parameters of the problem: the speciﬁc enthalpy, speciﬁc heat, density, and thermal conductivity of water, as well as the convective heat transfer coeﬃcients from the system to the surrounding air.

3.1 Properties of Water

The speciﬁc enthalpy of water is assumed to vary linearly with temperature, with a slope equal to the speciﬁc heat. This as- sumption was validated using property val- ues from the XSteam[1] MATLAB function, shown at right in Figure 3.

Mathematically, enthalpy (h) can be cal- culated from h = cpu, where cp is the spe- ciﬁc heat and u is the temperature. For the purposes of this paper, we will ignore the small y-intercept value and use a constant speciﬁc heat[2] of 4178 J/(kgK) based on an assumed average temperature of 30◦C.

The density and thermal conductiv- ity of water are taken to be constant at 1000 kg/m3 and 0.615 W/(mK) respectively[2], based on assumed average temperatures of 30◦C.

3.2 Heat Transfer Coeﬃcients

The calculation of convective heat transfer coeﬃcients is involved and will be summarized here. Because the bathtub itself is assumed to be in thermal equilibrium with the water, only convective eﬀects with the surrounding air will be considered. To appropriately estimate the heat transfer coeﬃcient, this convection must be classiﬁed as natural (free), forced, or mixed. In particular, we must check the Grashof number (GrL) and the Reynolds number (ReL). If GrL/Re2 L >> 1, inertial forces prevail and the natural convection dominates, but if GrL/Re2 L << 1, the opposite is true and forced convection dominates. If GrL/Re2 L ≈1, mixed convection must be considered[2].

The formulae for these two dimensionless numbers are shown below, where v is the ﬂow velocity, L is a characteristic length (used in determination of ReL), ν is the kinematic viscosity of the air, g is the local gravitational acceleration, β is the volume expansion coeﬃcient, us and u∞are the temperatures of the surface water and air respectively, and Lc is a characteristic length (used in determination of GrL)[2].

GrL = gβ(us −u∞)L3 ReL = vL c (1) ν2 ν As a ﬁrst order approximation, we take L = 1.5 m as the length of the bathtub in the ﬂow direction, ν = 1.608×10−5 m2/s for air at a ﬁlm temperature of 30◦C (a rough estimate of an expected ﬁlm temperature)[2], us = 40◦C, u∞= 20◦C (rough estimates of the tub and room temperatures respectively), and g = 9.81 m/s2. The ﬂow velocity v is slightly more involved to compute. First, we model the water ﬂowing under the air as air ﬂowing over the water, an equivalent model. Assuming a mass ﬂow rate of 0.06 kg/s (about 1 gallon per minute, a rough estimate of a “trickle”), a bathtub height H = 0.5 m, a bathtub width of W = 1 m, and uniform, laminar ﬂow from the x = 0 face to the x = L face, the ﬂow velocity can be computed as follows:

˙m 0.06 kg/s (1000 kg/m3)(1 m)(0.5 m) = 1.2 × 10−4 m/s ˙m = ρvA ⇒v = ρWH = (2)

For a ﬂat plate of water, Lc = As/p, the ratio of the surface area to the perimeter[2]. In our case, Lc = (1.5 m)(1 m)/(2(1.5 m+1 m)) = 0.3 m. Finally, assuming that air is an ideal gas[2], β = 1/T∞= 1/293.15 K = 0.003411 K−1.

Using these values in the formulae presented in Equation 1, we obtain ReL ≈11.19 and GrL ≈70000000. The ratio of interest GrL/Re2 L ≈558000 >> 1, so natural convection eﬀects signiﬁcantly dominate. Thus, forced convection will be ignored. Even if our rough estimates are slightly incorrect, natural convection should dominate because the ratio is much larger than unity.

Now, we are able to estimate the convective heat transfer coeﬃcients. The determination of these coeﬃcients for a natural convection problem is complicated, but will be summarized brieﬂy here. First, the Rayleigh number must be determined. This number, RaL, is the product of the Grashof and Prandtl numbers and describes the ratio of buoyancy forces to thermal and momentum diﬀusivities. The determination of the Grashof number is shown above, and the Prandtl number, Pr, is a property of the air based on ﬁlm temperature[2].

Once the Rayleigh number is determined, the Nusselt number, Nu, can be found based on the geometry of the natural convection. In our case, there are six surfaces with three independent geometries. Four of the surfaces (the sides) are modeled as vertical plates, one of the surfaces (the top) is modeled as a ﬂat plate with the hotter side facing up, and one of the surfaces (the bottom) is modeled as a ﬂat plate with the hotter side facing down. Due to the complicated physics of natural convection, these three geometries will have separate heat transfer coeﬃcients. Depending on the magnitude of the Rayleigh number and the geometry, the Nusselt number can be determined as follows[2].

( 104 < RaL < 107 0.54Ra1/4 L Top: Nut = 107 < RaL < 1011 0.15Ra1/3 L

105 < RaL < 1011 Nub = 0.27Ra1/4 Bottom: (3) L

2   0.387Ra1/6 L Wall: Nuw = 0.825 + Entire range   1 + (0.492/Pr)9/168/27   At long last, the heat transfer coeﬃcient hconv can be determined from hconv =Nuk/L, where k is the thermal conductivity of the air[2]. In practice, each thermodynamic constant of air is dependent upon the temperature, so there is no explicit solution to these equations. Rather, a system temperature must be guessed and the validity of the guess evaluated. Assuming an air temperature of 20◦C, the variation of ht with water temperature is shown below in Figure 4.

As shown by the above ﬁgure, the heat transfer coeﬃcient does vary with temperature of water, as was expected. For the range of temperatures anticipated in the bath water, how- ever, this variation is relatively small. Similarly, the variation of hb with system temperature is shown below.

As with ht, this coeﬃcient varies only slightly with system temperature within expected bounds. It is interesting to note that the magnitude of the coeﬃcient is lower than for the top surface; this is due to the decreased heat loss through natural convection when the hot bathtub is above the colder air. Finally, the same analysis is shown for hw.

Once again, the coeﬃcient varies only slightly with temperature. The magnitude of the heat transfer coeﬃcient from the walls is between those of the bottom and top surfaces, demonstrating that natural convection is slightly more eﬃcient from vertical walls than from face-down plates, but not as eﬃcient as from face-up plates. In complicated models, it is not realistic to use an iterative numerical method, so the heat transfer coeﬃcients will be taken as their mean value and assumed to not be functions of temperature.

4 Nominal Values Used in Model Simulations

Before describing our ﬁrst model, we must deﬁne the nominal values of each parameter to be used in simulations. In order to conduct reliable analysis of the impact of any one parameter on the solution, we use nominal values of the other parameters. This allows us to examine the eﬀect of a single parameter at a time. The following table contains the model parameters that can be altered as well as their nominal values.

Parameter Description Nominal Value L Bath Length 1.5 m W Bath Width 1 m H Bath Height 0.5 m ˙m Mass Flow Rate 0.05 kg/s 45◦C uin Input Water Temp.

Lbody Body Length 1 m cbody Body Circumference 0.5 m 37◦C ubody Body Temperature Xbody Position of Body Center 0.75 m 43 W/(m2K) [3] hbody Heat Transfer Coeﬀ. of Body 20◦C u∞ Surroundings Temperature 37◦C u0 Initial Water Temperature k Thermal Conductivity 0.615 W/(mK) [2] 1000 kg/m3 [2] ρ Water Density cp Speciﬁc Heat Capacity 4178 J/(kgK) [2] 4.692 W/(m2K) ht Heat Transfer Coeﬀ. of Top 1.934 W/(m2K) hb Heat Transfer Coeﬀ. of Bottom 3.804 W/(m2K) hw Heat Transfer Coeﬀ. of Wall t Time of Bath 1 hr

5 A Steady State, Uniform Temperature Model

5.1 Theory

We now move from deﬁning the geometry and thermodynamic parameters of the prob- lem to developing models for its solution.

As an initial model, the temperature in the bathtub is assumed to be uniform and steady. This allows the analysis to be sim- ply derived from the First Law of Thermo- dynamics. The system will be only the water in the bathtub, and the surroundings will be composed of the inlet, the exit, the bather, and the ambient air. This is shown in Figure 7 at right, where the dotted line represents the control volume (the system).

Assuming steady state, the time deriva-

tives of energy and mass in the system must modynamic System be zero, as no mass or energy can be accu- mulating in the system. This is shown math- ematically below. The energy equation will be the basis for our model and the mass equation will be used for an important simpliﬁcation.

dEsystem dmsystem = 0 ⇒˙Ein = ˙Eout = 0 ⇒˙min = ˙mout (4) dt dt Writing the ﬁrst equation above using the First Law of Thermodynamics, the following expression can be found[2].

h + v2 h + v2     ˙Qin + ˙Win + = ˙Qout + ˙Wout + X X ˙m 2 + gz ˙m 2 + gz (5) exits inlets Physically, Equation 5 is simply an energy balance. Energy transfer by heat, work, and mass are accounted for with enthalpy, kinetic energy, and potential energy making up the mass transfer terms. We assume only one inlet and one exit, which removes the summation from the equation. We also assume no work done on or by the system, no change in potential energy, and no change in kinetic energy. These are valid assumptions, as the inlet (faucet) and exit (overﬂow drain) should both be at the level of the water and the kinetic energy terms will be negligible due to the assumed trickle of water. Furthermore, the mass ﬂow entering and leaving should be the same, assuming ˙min = ˙mout from Equation 4 above. Finally, we can combine ˙Qin and ˙Qout into one term representing the net heat transfer. Using these simpliﬁcations and the relationship h = cpu, the expression is reduced greatly.

˙mcpuin = ˙mcpuout + ˙Qnet,out (6)

Since we assume uniform temperature distribution, the temperature at the exit is equal to the temperature of the system (uout = u). The last piece of this model is to quantify ˙Qnet,out using the heat transfer coeﬃcients discussed in the previous section. We use Newton’s Law of Cooling[2] to ﬁnd an expression for the convective heat transfer.

˙Qconv,out = hconvA(u −u∞). (7)

Associating the appropriate surface areas with each coeﬃcient, the following expression for the total convective heat loss is found.

˙Qconv,out = (u −u∞) ((ht + hb)LW + hw(2HW + 2HL)) . (8)

The presence of Joe in the bathtub provides an additional heat transfer term with its own heat transfer coeﬃcient. We will assume the submerged part of the body is a perfect cylinder without end caps, with a length equal to Lbody, a circumference of cbody, and an external temperature of ubody. The total heat loss from the system now includes a term to account for the body and is shown in Equation 9 below.

˙Qnet,out = (u −u∞) ((ht + hb)LW + hw(2HW + 2HL)) + (u −ubody)hbodyLbodycbody (9)

By substituting Equation 9 into Equation 6 and solving for u, the ﬁnal expression for steady, uniform temperature is found.

u = ˙mcpuin + u∞((ht + hb)LW + hw(2HW + 2HL)) + ubodyhbodyLbodycbody (10) (ht + hb)LW + hw(2HW + 2HL) + hbodyLbodycbody

5.2 Implementation and Results

Equation 10 was implemented using MATLAB. As was discussed previously, the heat transfer coeﬃcients are taken to be averages. Using the nominal parameter values, the steady, uniform temperature as a function of mass ﬂow is shown below in Figure 8.

It is clear from the above ﬁgure that increasing the mass ﬂow results in a ﬁnal temperature that approaches the inlet temperature of 45◦C. A similar plot is shown below to illustrate the dependence on inlet temperature.

When the inlet temperature is close to that of the ambient air (20◦C), the steady temper- ature is higher than that of the inlet, due to the minimal convective heat losses and the eﬀect of the body at 37◦C. However, when the inlet temperature is closer to body temperature, the steady temperature is slightly below the inlet temperature due to the increased convective heat losses. Finally, the sensitivity of the solution to ambient air temperature is presented.

This model is clearly much less sensitive to this parameter, illustrating minimal heat losses to convection due to the relatively low heat transfer coeﬃcients.

In principle, sensitivities for every parameter could be presented. However, to keep this report concise, we will only present these three. Ultimately, this model is too simple to capture the true dynamical nature of the bathtub system. Thus, more accurate models will be described in the following sections, but the qualitative results here serve as a good baseline for comparison with subsequent models.

6 An Analytical Model of the Heat Equation

In this section, we will describe a model based on an analytical solution to the one-dimensional heat equation with time dependent boundary conditions and time and space dependent heat generation/loss.

6.1 Theory

First, we will derive the analytical solution. The multi-dimensional heat equation with a heat generation term Q is shown below in Equation 11.

∂u ∂t = α∇2u + Q(⃗x, t) (11)

Using the geometric considerations detailed earlier in this report, this PDE can be reduced to one spatial dimension, changing the Laplacian operator to a second partial derivative. The resulting one-dimensional heat equation must be accompanied by an initial condition and boundary conditions in order to fully specify a problem. These conditions, along with the heat generation term, allow our model to eﬀectively describe the physical eﬀects inﬂuencing the temperature distribution within the bathtub.

The most appropriate boundary conditions for the bathtub are Neumann conditions which deﬁne a heat ﬂux at the boundaries. The heat ﬂux into the tub on the faucet side is described by the addition of heat to the system, a function of temperature and mass ﬂow of the inlet. The heat ﬂux on the drain side is due to conductive eﬀects through the water at the location of the drain. In order to keep the model generic, these boundary conditions will be allowed to vary with time. The implementation of time dependent boundary conditions allows for greatly increased ﬂexibility and accuracy of the model.

The heat generation term will be extensively used to represent the net eﬀect of both heat loss to the surrounding air and heat generation by Joe himself. As the heat equation admits a heat generation term that is both spatially and temporally dependent, this leads to a highly realistic interpretation of an actual system.

The full presentation of the one dimensional heat equation, with time dependent Neu- mann boundary conditions, customizable heat source, and initial condition φ(x), is shown below in Equation 12. Note that subscript notation will be used to represent partial deriva- tives.

∂t = α∂2u ∂u α ∈R≥0 ∂x2 + Q(x, t) , 0 < x < L , t > 0 , (12)

ux(x = 0, t) = a(t) , t > 0 ux(x = L, t) = b(t) , t > 0 u(x, t = 0) = φ(x) , 0 < x < L

Unlike many standard PDEs, the method of separation of variables will not yield appli- cable solutions, due to the inhomogeneity of the forcing function and the time dependence of the boundary conditions. To solve this problem, the method of shifting the data will be employed to homogenize the boundary conditions. This method, along with many of the other methods in the following solution, is outlined by Grigoryan[4].

First, we will transform the original equation:

x −x2 a(t) + x2   u(x, t) = v(x, t) + U(x, t) where U(x, t) = 2Lb(t). (13) 2L Plugging this transformation back into the original PDE, the following transformed PDE, boundary conditions, and initial conditions can be found.

∂t −α∂2v ∂v ∂x2 = ˜Q(x, t) α ∈R , 0 < x < L , t > 0 , (14)

vx(x = 0, t) = 0 , t > 0 vx(x = L, t) = 0 , t > 0 v(x, t = 0) = ˜φ(x) , 0 < x < L

 d x −x2 dt (a(t)) −x2  dt (b(t)) + α d ˜Q(x, t) = Q(x, t) − L (b(t) −a(t)) (15) 2L 2L

x −x2 a(0) −x2   ˜φ(x) = φ(x) − 2Lb(0) (16) 2L The new variable of interest is v, the transformed heat generation is ˜Q, the transformed initial condition is ˜φ, and the boundary conditions have been homogenized which was the objective of the transformation.

Now, we apply the principles of Fourier analysis to the PDE to ﬁnd a general solution for v(x, t). We deﬁne v(x, t) as a Fourier series in the spatial dimension. By Fourier’s Theorem, this representation is possible for any piecewise smooth v over a ﬁnite interval[5].

To be complete, a full linear combination of sines and cosines would be considered, but the presence of two homogeneous Neumann conditions suggests that just a cosine series is suﬃcient. This cosine series will include a constant term, as Neumann conditions admit a uniform oﬀset. The Fourier series representation of v is shown below in Equation 17, with the Fourier coeﬃcients deﬁned in Equation 18.

∞ nπx  X v(x, t) = vn(t) cos (17) L n=0 Z L Z L vn̸=0(t) = 2 nπx v0(t) = 1  v(x, t) cos dx v(x, t)dx (18) L L L 0 0 Allowing the Fourier coeﬃcients to vary with time is essentially a modiﬁcation of variation of parameters. The same application of Fourier analysis is used on the modiﬁed forcing function, as shown below in Equations 19 and 20.

∞ nπx  ˜Q(x, t) = ˜Qn(t) cos X (19) L n=0 Z L Z L ˜Qn̸=0(t) = 2 nπx ˜Q0(t) = 1  ˜Q(x, t) cos ˜Q(x, t)dx dx (20) L L L 0 0 At this point the solution function and the forcing function have been fully deﬁned in terms of their spatial Fourier cosine series. These two Fourier series representations can be substituted into the PDE in Equation 14. After working through the algebra and moving the derivatives into the sums (assuming that they converge), the PDE is reduced to Equation 21.

∞ ∞ nπ nπx nπx 2 h i   ˜Qn(t) cos X X v′ n(t) + α vn(t) cos = (21) L L L n=0 n=0 By equating Fourier coeﬃcients of the above equation, it can be seen that for every nth term of the series, an ordinary diﬀerential equation (ODE) in time exists relating the coeﬃcients vn(t) and ˜Qn(t). This relationship is shown below in Equation 22.

nπ 2 vn(t) = ˜Qn(t) v′ n(t) + α , n = 0, 1, 2, . . . (22) L This ﬁrst order, non-homogeneous ODE with constant coeﬃcients can be solved using the integrating factor method in which the full ODE is multiplied by a factor that allows the left side terms to be expressed as a perfect derivative of the product of two functions.

This common process will not be demonstrated here, but the solution is shown in Equation 23 below, where s is a dummy variable of integration.

Z t   2t 2s ˜Qn(s)ds vn(t) = e−α( nπ L ) eα( nπ L ) vn(0) + (23) 0 Each of these ODEs is for a speciﬁc nth term of the Fourier series. Therefore, it is necessary to deﬁne the initial condition as a Fourier cosine series, just as was done for the solution variable and the forcing function. The cosine series is shown below in Equation 24, with a note about v(x, 0) that will be used in the next step.

∞ ∞ nπx nπx   ˜φ(x) = ˜φn cos X X Note: v(x, 0) = vn(0) cos (24) L L n=0 n=0 The coeﬃcients are shown in Equation 25.

Z L Z L ˜φn̸=0 = 2 nπx ˜φ0 = 1  ˜φ(x) cos ˜φ(x)dx dx (25) L L L 0 0 By examining the note in Equation 24 and observing that ˜φ(x) ≡v(x, 0), equating the coeﬃcients results in the relationship vn(0) = ˜φn. Thus,

vn̸=0(0) = ˜φn̸=0 v0(0) = ˜φ0, and (26)

which can be directly substituted into Equation 23 where ˜φn̸=0 and ˜φ0 are given by Equation 25.

This completes the solution for vn(t), the Fourier coeﬃcients of the transformed solution. Next, v(t) is represented in terms of these coeﬃcients, where ˜Qn and ˜φn are the Fourier coeﬃcients of the transformed heat generation and initial condition respectively, both known functions.

Z t ∞   nπx 2t + 2(s−t) ˜Qn(s)ds  ˜φne−α( nπ L ) eα( nπ L ) X v(x, t) = cos (27) L 0 n=0 A transformation back from v to u by unshifting the data completes the solution to the original PDE with time dependent Neumann boundary conditions and time and space dependent heat generation.

Z t ∞ x −x2 a(t) + x2     nπx 2t + 2(s−t) ˜Qn(s)ds  ˜φne−α( nπ L ) eα( nπ L ) X u(x, t) = cos + 2Lb(t) L 2L 0 n=0 (28) This solution is a full analytical model of one-dimensional heat diﬀusion within the bath- tub. It accommodates the eﬀects of time dependent heat ﬂux through the faucet and can account for the eﬀects of Joe’s body temperature and convective heat loss to the ambient air, both of which can vary spatially and temporally. The next subsection will detail the implementation of this solution.

6.2 Implementing the Analytical Model

Implementation of the analytical solution is done in MATLAB. Here, we can take full ad- vantage of the underlying vector and matrix structures necessary for these calculations. We deﬁne a grid of (x, t) coordinates with grid sizes ∆x and ∆t.

tj+1 = tj + ∆t xi+1 = xi + ∆x (29)

Using this grid, Equation 28 is ultimately the addition of (x×t) matrices, each a product of an (x × 1) vector and a (1 × t) vector. The following discussion concerns each term of Equation 28 and its implementation in MATLAB.

To ﬁnd the coeﬃcients ˜φn, the integral in Equation 25 is approximated using a Trape- zoidal Rule with a spacing of h and N subdivisions.

Z L N nπx dx ≈h nπxk+1 nπxk  h  i ˜φ(x) cos ˜φ(xk+1) cos + ˜φ(xk) cos X (30) L 2 L L 0 k=1

The same approximation is used to compute ˜Qn.

Z L N nπx dx ≈h nπxk+1 nπxk  h  i ˜Q(x, t) cos ˜Q(xk+1, t) cos + ˜Q(xk, t) cos X (31) L 2 L L 0 k=1

The left-hand side of Equation 31 is a function of t, so the integration on the right-hand side must be performed at every t in the deﬁned grid.

The computation of the time-varying integral in Equation 27 requires more care. A Trapezoidal Rule is still utilized, but the subdivision length becomes a function of time.

Z t N 2(s−t) ˜Qn(s)ds ≈h(t) 2(sk+1−t) ˜Qn(sk+1) + eα( nπ 2(sk−t) ˜Qn(sk) h i eα( nπ L ) eα( nπ L ) L ) X (32) 2 0 k=1

6.3 Basic Results and Veriﬁcation

The ﬁrst scenario to simulate is heat loss over time with insulation on both ends of the bathtub. In this scenario, we expect that the heat loss from the bottom, sides, and top of the bathtub will uniformly decrease the temperature of the water over time. The boundary conditions, initial condition, and internal heat generation are modeled in Equation 33.

ux(x = 0, t) = 0 , t > 0 ux(x = L, t) = 0 , t > 0 (33) u(x, t = 0) = 37 ◦C, 0 < x < L Q(x, t) = ˜h(u∞−u(x, t −∆t)) , 0 < x < L, t > 0 Physically, Q(x, t) describes the combined heat losses from the water to the tub and sur- rounding air. The greater the diﬀerence between the water temperature and the surrounding air temperature, the greater the heat loss. However, the water temperature is sampled from the previous time step; to reﬂect this, t −∆t is used in place of t when computing the water temperature in space. The coeﬃcient ˜h describes the rate of heat loss through the diﬀerent surfaces. We expand ˜h in Equation 34.

2hw  ˜h = 1 W + hb H + ht (34) ρcp H

The subscripts on each h describe the heat transfer coeﬃcients through the wall (hw), bottom (hb), and top (ht). The division of each coeﬃcient by some length indicates the characteristic length relevant to the heat transfer through that surface. In order to have units of ◦C/s, we divide all terms by the product ρcp.

With all the relevant data described, the algorithm necessary to compute u(x, t) is to ﬁrst compute all quantities for t = 0. This way, ˜Q(x, 0) can be initialized in Equation 35.

x −x2 −x2 da(0) db(0) + α  ˜Q(x, 0) = ˜h(u∞−φ(x)) −    b(0) −a(0) (35) 2L dt 2L dt L Now we can iterate over time in a loop. This way, the previous results are used to calculate recursively the heat loss Q(x, y) and then a new u(x, t). Nested in this loop is another loop which iterates over the number of Fourier terms, N. This performs the summation of each Fourier term to yield the ﬁnal solution. For the data used in Equation 33, Figure 11 displays the temperature distribution in x and t.

This result is what we expect: with both ends insulated, the water temperature uniformly decreases over time.

Consider new boundary conditions in Equation 36.

ux(x = 0, t) = ˆh [uin −u(0, t −∆t)] , t > 0 1 ∆x [u(L −∆x, t −∆t) −u(L, t −∆t)] ux(x = L, t) = , t > 0 (36) u(x, t = 0) = 37 ◦C, 0 < x < L Q(x, t) = ˜h[u∞−u(x, t −∆t)] , 0 < x < L, t > 0

The boundary condition at x = 0 represents an inlet heat ﬂux, entering the system with temperature uin. The boundary condition at x = L is a rough approximation of the heat ﬂux from the previous time step. Similar to the internal heat loss, the heat ﬂux decreases as the water temperature at x = 0 approaches uin. The coeﬃcient ˆh ensures that the units agree on both sides of the equation. Physically, ˆh, is proportional to the mass ﬂow rate of water from the inlet. Equation 37 describes this relationship.

˙mcp ˆh = (37) kWH The code structure from the previous set of boundary conditions allows for the recursive calculations to compute each new boundary condition. For uin = 45◦C, the full solution in x and t for the conditions set in Equation 36 are shown in Figure 12.

expected due to the low thermal diﬀusivity of water.

Now we simulate a body moving as a point source through the bath. To do so, we deﬁne F(x, t).

Z x−t+ϵ δ(x −t −400)d(x −t), F(x, t) = f 0 < t < 200 (38) x−t−ϵ Physically, the bather is placed at x = 400 at t = 0; then, whenever x = t + 400, F(x, t) = f. f is simply a constant heat generation term deﬁned by the thermodynamic characteristics of the body placed inside the bath. Including in the heat loss term to the surroundings in Q(x, t), our full problem becomes deﬁned as below.

ux(x = 0, t) = 0 , t > 0 ux(x = L, t) = 0 , t > 0 (39) u(x, t = 0) = 45 ◦C, 0 < x < L Q(x, t) = F(x, t) + ˜h[u∞−u(x, t −∆t)] , 0 < x < L, t > 0

The new solution is displayed below in Figure 13.

in both space and time. Whenever a point source moves to another location, the previous locations remain at the higher temperature because the heat diﬀuses very slowly.

7 A Numerical Model of Convection-Diﬀusion

In this section we will describe our ﬁnal model: a ﬁnite diﬀerence approximation of the convection-diﬀusion equation. We will brieﬂy discuss the theoretical development and im- plementation, and then present initial results.

7.1 Theory

The problem at hand can be even more eﬀectively modeled as a one-dimensional convection- diﬀusion problem. The addition of a convection term allows the actual ﬂow of the water – and not just diﬀusion of heat – to be modeled. It is important to note that convection in this sense means the bulk motion of the water in the tub and not the heat loss to the surroundings. The governing PDE for a convection-diﬀusion problem is shown below, where the only new quantity is ϵ, the porosity.

∂t = α∂2u ∂u ∂x2 −ϵv∂u ∂x + q(x, t) (40) ρcp ∂t represents the transient, α ∂2u In this equation, ∂u ∂x2 represents diﬀusion, ϵv ∂u ∂x represents convection, and the ﬁnal term represents heat generation or loss. Eliminating the convection and generation terms yields the familiar heat equation presented earlier. Due to the diﬃculty in solving this equation analytically, a numerical solution will be implemented using the ﬁnite diﬀerence method, as outlined by Majchrzak and Turcha[6].

The ﬁrst step is to discretize the temporal and spatial variables, as shown below, where j indexes through time, i indexes through space, and ∆t and ∆x are the time step and grid spacing, respectively.

tj+1 = tj + ∆t xi+1 = xi + ∆x (41)

Each derivative can be re-written using a Taylor series in the variable of diﬀerentiation. This is shown below in Equation 42, where the superscript represents time indexed in j and the subscript represents space indexed in i.

−ϵvuj−1 i+1 −uj−1 = αuj i+1 −2uj i + uj i −uj−1 + qj−1 uj i−1 i−1 i i (42) (∆x)2 ∆t ∆x ρcp Solving for the temperature at the time (j) and location (i) of interest yields the following numerical solution to the convection-diﬀusion equation.

 α∆t  α∆t + qj−1     1 −2α∆t (∆x)2 + ϵv∆t (∆x)2 −ϵv∆t uj−1 uj−1 uj i i = + i−1 + cpρ ∆t (43) i (∆x)2 2∆x 2∆x

When selecting step sizes ∆x and ∆t, we must ensure that the stability criteria are met since the forward diﬀerence approximations are conditionally stable. These criteria are described below.

∆t < (∆x)2 ∆x < 2α ϵv , (44) 2α Should these conditions not be met, the error accumulated in each approximation will grow unboundedly[7].

The ﬁnal solution, uj i, describes the propagation of heat through space and time, and can be implemented in MATLAB. The porosity, ϵ, is the ratio of ﬂuid volume to total volume, and since the medium is entirely ﬂuid, it will be taken as unity. To complete this model, we must now quantify q and enforce appropriate boundary conditions.

The fundamental source of heat transfer in this problem is convection from the water surface and from the bathtub surface. In Equation 43 above, q is the heat transfer per unit volume, where the volume in consideration is a slice of the bathtub in the x direction. This slice has volume WH∆x. Thus,

Q q = WH∆x, (45)

where Q is the macroscopic heat loss of the slice. This heat loss is described by the convection terms and the conduction term as follows.

Q = (u −u∞)(htAt + hwAw + hbAb) = (u −u∞)(ht(W∆x) + hs(2H∆x) + hb(W∆x)) (46)

Upon plugging this into Equation 45, we explicitly quantify q due to natural heat transfer eﬀects.

q = (u −u∞) (W(ht + hb) + 2Hhw) (47) WH The same method can be used to model the presence of a person in the bathtub. We estimate that the person will take up a given amount of space in the x direction and have a given circumference cbody, which correlates to the exposed area per unit length of the bathtub. The additional heat generation/loss due to the body can be implemented as follows.

qbody = hbodycbody(u −ubody) (48) WH Together, Equations 47 and 48 make up the heat generation term in the PDE. At a given location i and time step j, we use uj−1 to estimate u in these equations. i Enforcing the boundary conditions requires some creativity. To enforce the boundary condition on the inlet side, we must specify the correct amount of heat ﬂux into the system as a Neumann condition, increasing the energy content of the ﬂuid element at the boundary based on the mass ﬂow and temperature of the inlet.

The energy entering per unit volume, a q term, can be described as

WH∆x = ˙mcp(uin −u) Q q = . (49) WH∆x This can be translated directly into a change in temperature, as in Equation 43 above, by dividing by ρcp, multiplying by the time step ∆t, and approximating u from the previous time step.

i = ˙m(uin −uj−1 ) ∆uj i ∆t (50) ρWH∆x Equation 50 provides a direct method for changing the temperature of the boundary point in order to account for the heat entering the system.

At the other boundary point, we wish for the water to exit the system naturally, which poses a challenge in prescribing a boundary condition. A realistic condition is that the ﬂux out is equal to the ﬂux between the two points adjacent to the boundary. Thus, the temperature at the end can be speciﬁed as follows.

! uj end−1 −uj end−1 + ∂u uj end = uj ∂x∆x = uj ∆x = 2uj end−1 −uj end−2 end−1 + (51) end−2 ∆x

Now, both boundary conditions have been speciﬁed and the ﬁnite diﬀerence method can be implemented in MATLAB. We will not describe the algorithm here, as it follows directly from the derivation above.

7.2 Basic Results and Veriﬁcation

In this subsection, we will present some basic results to demonstrate the functionality of our model. First, the problem was modeled with no heat input (the faucet turned oﬀ). The results from this simulation are shown below in Figure 14.

The temperature in the tub remains uniform and slowly decreases due to heat loss to the surrounding air. Next, the system was modeled with the faucet on, and the results are shown below.

This time, the temperature away from the faucet (near x = L) drops steadily, as before, but the temperature near the faucet increases to the temperature of the incoming water. Through time, this wave of heat convects through the system at a rate determined by the mass ﬂow and the geometry of the tub. Next, the presence of the bather, Joe, was added and the simulation was run.

The deviation of these results from the simulation without the bather is unnoticeable without closely examining the numerical values on a computer. This illustrates that the presence of a bather has little eﬀect on the simulation, an observation that makes physical sense due to the bath temperature and body temperatures being nearly identical.

7.3 Modeling Bather Actions

In this subsection, we will examine the eﬀect of actions of the bather on the solution. As we are assuming no ﬂuid ﬂow other than the bulk, convective motion towards the drain, the bather will have no eﬀect other than to distribute/redistribute heat. Further, we limit ourselves to the case of ﬁxed inlet water temperature and mass ﬂow. This allows the bather to distribute the incoming heat as they wish.

The logic from the boundary condition on the inlet is now extended to the full domain. Given the amount of input energy speciﬁed by Equation 49, this energy can be added to any location or combination of locations in the domain, provided that the total amount of energy added to the system does not change from what would have been originally added at the inlet.

This can be implemented by modifying Equation 50, as shown below, where ηj i (between 0 and 1) is the fraction of available heat prescribed to enter that grid point at that time.

˙m(uin −uj−1 ) ∆uj i = ηj i ∆t (52) i ρWH∆x This temperature change term is in addition to the temperature change already calculated from the discretized derivatives and heat loss to the surroundings. In order to conserve energy, the following equality must be deﬁned for all times.

X ηj i = 1 (53) i

Two interesting applications of bather eﬀects are shown below in Figures 17a and 17b. In the left ﬁgure, 99% of the input water was evenly distributed over the whole domain and the remaining 1% was left to trickle through the x = 0 boundary. In the right ﬁgure, half of the heat was distributed evenly over the region from x = 0.75 to x = 1.5 and the other half trickled through the faucet.

(a) Nearly Uniform Heat Distribution (b) Split Heat Distribution

8 Model Comparison

In this section we present and discuss the major results from both the analytical and nu- merical models, commenting on the eﬀectiveness and validity of each model.

8.1 Solution Metrics

First, we must develop a metric with which to evaluate our solutions. To do this, we return to the original objective: Joe wishes to attain a desired temperature uniformly distributed throughout the bath. The desired temperature constraint and the uniform distribution con- straint will be decoupled and evaluated separately.

The ﬁrst metric evaluates the total heat within the bath, addressing the desired temper- ature constraint. This objective function will be called u, as deﬁned in Equation 54.

u(t) = uavg(t) −uobj (54)

This metric will yield a time-dependent value proportional in magnitude to the diﬀerence between the average and objective, with a sign that denotes whether the bath is below or above the objective temperature. As a standard value, the objective temperature of the water will always be a comfortable 37◦C.

The second metric quantiﬁes the uniformity of the temperature distribution over time. We will deﬁne this metric as σ, the standard deviation of the temperature distribution at a given point in time. The equation for the standard deviation is given below in Equation 55.

v N u t 1 u X (un(t) −uavg)2 σ(t) = (55) N n=1 The evolution of the objective functions (metrics) through time for the numerical model with nominal parameters is shown below, along with the heat map describing the temperature distribution.

(a) Heat Map of Simulation (b) Objective Functions From Simulation

eters By comparing the two plots, the eﬀectiveness of the objective functions is clear; the temperature becomes less uniform as we add too much heat to the system resulting in an increase in the average temperature objective function. In order for Joe to be happy with his bath, our goal is to drive both of these objective functions to zero. As a standard, we will always consider the temperature distribution at the end of a one hour bath. With well deﬁned metrics now in place, simulations can be run to test the impact of each parameter on the solutions from both the analytical and numerical models. The following subsections will each describe the eﬀect of a diﬀerent parameter on the solution metrics.

8.2 Eﬀect of Bathtub Geometry

The ﬁrst parameters under consideration are the physical dimensions of the bathtub. Chang- ing the dimensions of the bath changes the surface areas exposed to the air, the velocity of the water ﬂow, and the extensive properties of the ﬂuid element such as mass and volume. Below, we examine the eﬀect of changing the length of the bathtub while holding all other parameters constant.

(b) Numerical Model

(a) Analytical Model

By increasing the length of the bathtub, the error and standard deviation both increase in magnitude for the analytical solution but both decrease in magnitude for the numerical solution which are notably inconsistent results. The analytical model only takes into account the heat diﬀusion term while the numerical model also accounts for heat convection due to the bulk ﬂow of the water. This fundamental diﬀerence is likely the reason for these inconsistent results.

When considering the more accurate numerical model (convection and diﬀusion) with longer bathtubs, the water is both more uniform and, on average, closer to the objective temperature. As the ﬂow rate is held at its nominal value, a longer bathtub will be less aﬀected by the inﬂux of hot water. The increased error of the analytical model, on the other hand, is due to the low thermal diﬀusivity of water in comparison to the heat loss of the system. Although hot water is being added to the bath, it cools at a faster rate than the heat can diﬀuse through it. Thus, heat builds up at the faucet end of the tub, increasing both error and standard deviation.

A similar study was conducted on the eﬀect of bathtub width, and the results from both models are shown below.

(b) Numerical Model

(a) Analytical Model

In this case, the two models qualitatively agree with one another; the temperature error magnitude and the standard deviation are decreasing as width is increased.This result is consistent with the ﬁndings of the length variation in the numerical model. The eﬀect of increasing the width is to increase the area exposed to air while maintaining the distance in the direction of diﬀusion and bulk ﬂow. This increase results in a more uniform temperature distribution as the heat build-up at the inlet is oﬀset by increased heat loss.

Next, the height dimension was varied and the results from the sensitivity analysis are presented below.

(a) Analytical Model

(b) Numerical Model

This ﬁgure mirrors very closely the result from the width variation, as both the width and height are the two dimensions through which the water is assumed to not ﬂow or diﬀuse heat.

Finally, a simultaneous variation of all three dimensions is implemented. This “volume factor” is the ratio of volume to nominal volume. The results from this analysis are shown in Figure 22 below.

(b) Numerical Model

(a) Analytical Model

These results reﬂect those of the height and width variations, which suggests that height and width are more signiﬁcant parameters in describing the temperature distribution through- out the bathtub, because they correlate strongly with convective heat losses to the air.

The results from this subsection emphasize the strength of the numeric model over the analytical model due to the importance of the bulk motion of the water, which is only accounted for in the numerical model.

8.3 Eﬀect of Adding Soap

If Joe were to use a bubble bath additive or soap, this would change the thermal properties of the water which would ultimately result in a change in thermal diﬀusivity. The primary ingredient of soap is sodium stearate which is also used in bubble bath solutions. The density of sodium stearate is 1020 kg/m3 [8]. This density is nearly identical to that of water and as such should have little to no eﬀect on the density of the water when dissolved especially as the soap to water ratio would be small in a full bath. By adding a solute such as sodium chloride to pure water, the thermal conductivity decreases as solute concentration increases[9]; it is a reasonable assumption that adding sodium stearate results in a similar eﬀect.

Overall, the approximately inconsequential addition of sodium stearate to water in re- alistic concentrations slightly reduces the diﬀusivity of the water. To perform a sensitivity analysis of this parameter, a wide range of diﬀusivities (a full order of magnitude about the standard diﬀusivity of water) was tested. This wide range was used to in order to show a noticeable change in solution behavior. Final temperature distributions after one hour are shown for various values of thermal diﬀusivity below with the ﬁgure at right magnifying the area of interest.

(b) Magniﬁed Variations of Diﬀusivity (a) Varied of Diﬀusivity over Full Length

The thermal diﬀusivity has very little eﬀect on the solution, especially considering the wide range of thermal diﬀusivities tested. This continues to support the hypothesis that the heat transfer is primarily due to bulk ﬂow and not diﬀusion. By examining the P´eclet number (Pe)[10], we can conﬁrm this hypothesis. The Peclet number is the ratio of the convective transport rate to the diﬀusive transport rate, as shown below with our nominal values.

α = (1.2 × 10−4 m/s)(1.5 m) Pe = vL ≈1223 >> 1 (56) 1.472 × 10−7 m2/s This large ratio conﬁrms that diﬀusion eﬀects are negligible in comparison with bulk motion eﬀects, due to the low thermal diﬀusivity of water. From this point onward, only the numerical model will be considered as the analytical model fails to capture the most important mechanism of heat transfer: bulk ﬂuid motion.

8.4 Eﬀect of Varied Input Temperature and Flow Rate

Up to this point, sensitivity analyses have been presented for the physical parameters of the system: the dimensions/shape of the bath and the thermal properties of the water in the bath. The next set of sensitivity analyses will be focused on the parameters that can vary during the course of the bath: the input water stream and the properties of Joe himself. First we analyze the eﬀect of changing the input water temperature and mass ﬂow rate. The results from this analysis are shown below in Figure 24.

(b) Variation of Mass Flow Rate (a) Variation of Input Temperature

Increasing either parameter corresponds to an increase of net energy in the system. An- other important result is that a large ﬂow rate will result in a more uniform distribution when compared with a high temperature inlet. This is because increasing the mass ﬂow rate increases the convective term, which is more eﬃcient than the diﬀusion. The x intercepts of the blue lines on each plot represent important values, namely the input temperature or mass ﬂow required to add the correct amount of heat to the system to maintain the objective temperature.

Heat maps for a low (35◦C) and high (50◦C) inlet temperature are shown below to further validate the model.

(a) Low Input Temperature (b) High Input Temperature

In both cases, the input water convects across the bath, with a slight diﬀusive eﬀect present at the boundary between the input water and the initial water. The rate of bulk ﬂuid motion is clearly visible as the diagonal line of large temperature gradient. Similarly, heat maps for zero mass ﬂow and high mass ﬂow (twice the nominal value) are shown below.

(b) High Mass Flow Rate (a) Zero Mass Flow Rate

In the zero mass ﬂow case, the water temperature is uniform at any given time, but is slowly cooling due to thermal energy loss into the surroundings. In the high mass ﬂow rate case, the increased rate of bulk ﬂuid motion can be seen. After one hour, the high temperature water has moved farther into the bath.

8.5 Eﬀect of Varied Size and Position of Bather

The ﬁnal parameter to be analyzed in the simulation of the bathtub is Joe himself. Any given bather may have diﬀerent properties, such as width, length, temperature, or ability to transfer heat to or from the system.

These possible variations in parameters will be broken into two diﬀerent categories: phys- ical dimensions of the bather and the thermal properties of the bather. Below are the plots of the eﬀects of the geometric parameters on the objective functions.

(b) Eﬀect of Body Surface Area (a) Eﬀect of Body Length Neither Joe’s body length nor his circumference (surface area per unit length) have a signiﬁcant eﬀect on the temperature distribution. It is only for a very long body (near the length of the bath itself) that uniformity and average temperature error are slightly improved. These results suggest that the physical dimensions of the bather have a negligible eﬀect on the objective functions, due to the fact that the body temperature is close to the temperature of the bath.

The eﬀects of the Joe’s thermal parameters are shown below.

(b) Body-Water Heat Transfer Coeﬃcient (a) Eﬀect of Body Temperature

The ﬁrst sub-ﬁgure shows that Joe’s body temperature has a slightly more signiﬁcant impact than the geometry, which makes sense considering the diﬀerence in temperature between Joe and the water. However, it is important to note that this sensitivity is shown over a large range. The heat transfer coeﬃcient has little to no impact, once again due to the small temperature diﬀerence between Joe and the water.

9 Control Theory and Implementation

In this section, we examine the implementation of closed-loop control for the regulation of average temperature and temperature uniformity. Up to this point, we have only considered cases where the initial and objective temperatures are the same. This correlates to Joe being proactive and attempting to mitigate the heat loss before the temperature drops noticeably. Now, we consider the case where the initial temperature is uniform, but noticeably lower than the objective, a potentially more realistic application.

9.1 PID Control Theory

Joe’s ultimate goal is to experience a bath that is both maintained at a desired temperature and uniform in temperature through the water. Up to this point, many of the parameters that inﬂuence the response of the temperature distribution have been analyzed. However, the time dependence of these sensitivities has not been considered. We wish to develop a time dependent strategy for Joe to achieve a uniform bath at the objective temperature using Proportional-Integral-Derivative (PID) control.

The ﬁrst portion of the control system is designed only to achieve and maintain the objective temperature by using the average temperature metric detailed previously. Proper distribution can only take place if the correct amount of energy is already present in the system. As the net amount of heat in the bath is directly controlled by the faucet, this segment of the control system will focus on optimization of the inlet temperature and ﬂow rate of the water from the faucet.

PID control is implemented through the selection of the gains associated with each com- ponent of the control. Below in Equation 57 is the general gain equation of a PID controller as a function of the objective u(t) with variable gains K for each stage, where f(t) represents the calculated forcing (input).

Z t ∂u(t) f(t) = Kpu(t) + Ki u(τ)dτ + Kd (57) ∂t 0 Each of the three components of a PID controller corresponds primarily to a speciﬁc response of the system. The proportional control element is based on the diﬀerence between actual temperature and objective temperature; this control is what physically drives the system to the objective. The inte- gral component deﬁnes the response on ac- cumulated error from the objective instead of current error, decreasing the rise time and removing the steady state error from the sys- tem. The derivative component predicts the response error based on the temporal deriva- tive of the response, damping any oscilla- tions.

Illustration of Properly Tuned At right is an image of the eﬀects of each PID Controller[11] of the three components of a PID controller with properly tuned gains. Properly tuning each gain results in the optimal responses described: a small rise time with minimal oscilla- tion and no steady state error.

9.2 Implementation of PID Control in Numerical Model

PID control was implemented in the numerical model by simply specifying the forcing as a function of u(t), as shown in Equation 57. In particular, we set

f(t) = ˙m(uin −u(x = 0, t)), (58)

a term in the inlet Neumann condition.

In addition, the gain coeﬃcients needed to be determined. These gain coeﬃcients should weight the response with the ultimate goal of achieving a response with minimal rise time, little to no overshoot, and long term stability. These desired responses have strong grounding in the reality of the physical system. The rise time is desired to be short so that Joe does not have to wait long for his bath to reach the objective temperature. Too much overshoot could result in Joe being burned, and is thus not desired. Finally, long term stability reﬂects the maintenance of the desired temperature over the course of the entire bath duration.

There are many methods for determining optimal gains, including PID control software and algorithms such as the Ziegler-Nichols tuning process, but due to the lack of a well deﬁned transfer function in the numerical approach, neither option is applicable and manual tuning is required.

We manually tuned our gains in order to obtain a roughly optimal response. In no way are the following system responses the result of optimal gains; much more tuning would be required for such an optimization. Below, we present the system response using only proportional control, starting at 30◦C and attempting to reach 37◦C.

There are noticeable oscillations in the objective function (the blue line) and there is an overshoot of about 4◦C. Since the forcing is a function of both mass ﬂow and inlet temperature, we ﬁx mass ﬂow and present the result as the required ∆u (the red line). The ∆u peaks at around 20◦C, meaning that the inlet water temperature must be 20◦C hotter than the current water temperature at the inlet.

Using full PID, the results from the same analysis are shown below in Figure 31.

The objective function is driven to nearly zero, as desired. More importantly, the response is achieved with a relatively short rise time, minimal overshoot, and maximal oscillation of less than a degree. The associated forcing function is more reasonable, requiring a maximum ∆u of about 3◦C.

9.3 Control of Uniformity of Water Temperature Distribution

With the average temperature of the water driven to the objective temperature using PID control, the only remaining factor is the uniformity of the temperature distribution. The method of maintaining uniformity is very simple: instead of adding heat from the faucet to the bathtub at x = 0, we evenly distribute the hot water over the whole bath. Physically, this method corresponds to Joe continuously redirecting the water from the faucet, using a cup or another redistribution system.

Logically, it makes sense to evenly distribute the heat throughout the bathtub. Assuming an initial temperature of 37◦C and an objective temperature of 37◦C (which corresponds to Joe being proactive about the heat loss in the bath), this logical argument is easily veriﬁed. In Figure 32 below, we show the objective functions vs. inlet temperature, where the heat is being distributed evenly and the mass ﬂow is ﬁxed. We also show the heat map using the optimized input temperature.

(a) Optimal Input Temperature (b) Heat Map of Optimized Uniformity

The uniformity objective function (the red line) is maintained at zero which conﬁrms the hypothesis that uniform heat distribution is most eﬀective. The heat map demonstrates that using the optimal input temperature for the given mass ﬂow rate results in a perfect bath. The same results are shown in 33 below, this time varying the mass ﬂow with a ﬁxed inlet temperature.

(b) Heat Map of Optimized Uniformity (a) Optimal Mass Flow Rate

Temperature

Just as before, there exists an optimal mass ﬂow, and using this mass ﬂow with uniform distribution, a perfect bath is once again achieved.

9.4 Final PID Control with With Manual Heat Distribution

We close with a simultaneous consideration of average temperature (PID) control and unifor- mity control. Up to this point, we have analyzed these control methods separately and under diﬀerent initial conditions, but to complete our model of the problem it is essential that we implement them simultaneously. The initial condition will be a 30◦C uniform bath, and the objective will be 37◦C, accurately modeling Joe’s realization that his bath has become cold.

The combined model will eﬀectively implement the two control methods by using PID control to determine required temperature of the incident water (given a constant nominal mass ﬂow rate), and using intelligent input water redistribution to maintain uniformity. The intelligent redistribution was determined by tweaking the locations at which the input water is distributed. Ultimately, it was determined that distributing inlet water over the region from x = 0 m (the faucet) to the location that the body starts, x = 0.25 m for the nominal case, is optimal. This allows the body heat to convect downstream and the inlet heat to warm the water upstream of the body.

After manually tuning the gains and implementing full PID in addition to intelligent inlet water distribution, the following results are obtained.

(b) Uniformity over Time (a) PID Control with Manual Heat Distribution

On the left, the average temperature objective function is shown to rise to zero relatively quickly with no overshoot, an optimal result. Additionally, the required ∆u with a nominal ﬂow rate is physically reasonable. On the right, the temperature uniformity is shown to initially increase (due to Joe’s body) but settle to zero as the inlet water distribution begins to have an eﬀect.

The heat map corresponding to this control is shown below in Figure 35.

This result illustrates the optimal strategy that Joe can take to increase his bath tem- perature to his objective while keeping the temperature distribution uniform and only using a nominal trickle of water. He should use PID control to vary the input temperature and si- multaneously use a cup or other redirecting device to continuously distribute the inlet water over the region of the bathtub that is upstream of his body.

10 Final Remarks

We have now completed our mathematical modeling of the bathtub. In this section, we will conclude our paper, commenting on each of our models and presenting ideas for future work.

10.1 Strengths and Weaknesses of Solution Models

Each of our ﬁnal models had very speciﬁc strengths and weaknesses. Below are a list of strengths and weaknesses for the three models developed in this report: the steady state uniform model, the analytical model of heat diﬀusion, and the numerical model of the convection-diﬀusion equation.

Steady State, Uniform Temperature Model

Strengths:

• The implementation is straightforward and the derivation is based solely on thermo- dynamics.

• The results can be used to qualitatively predict the results of more complicated models.

Weaknesses:

• No spatial or temporal dependence is considered.

Analytical Solution Model

Strengths:

• Time dependent boundary conditions and both a spatially and temporally dependent forcing function (heat source) can be eﬀectively modeled.

• The boundary conditions can be customized to reﬂect the physical system.

• The model yields a highly accurate analysis of characteristic transient solutions over one dimensional space due to heat diﬀusion.

Weaknesses:

• Bulk ﬂow of the ﬂuid is not modeled.

• The simulation implementation proved challenging when considering various types of boundaries and sources.

Numerical Convection-Diﬀusion Model

Strengths:

• Solution incorporates eﬀects of both convection and diﬀusion for a realistic ﬂuid ther- modynamic simulation.

• Time dependent boundaries and a spatially and temporally dependent heat source can be customized.

• The straightforward implementation of simulations allows for a variety of tests of pa- rameter sensitivity analyses as well as the implementation of control.

• The numerical approach allows for the possibility of expansion of the simulations into a multidimensional model.

Weaknesses:

• The foundational mathematics of this numerical implementation are highly involved.

The greatest overall strength of all of the models was their generality. This allowed for a wide range of parameter customization, from dimensions of the bath, types of boundaries en- forced on the system, heat transfer coeﬃcients, eﬀects of Joe in the system, and ﬁnal control application. The main weakness of our models is that they only consider one-dimensional heat ﬂow. In reality, the thermal-ﬂuid eﬀects in a bathtub will be largely three-dimensional.

10.2 Future Model Development

As discussed in the weaknesses of the models, many possibilities exist for the development of a more precise model. In the future, a more comprehensive and deﬁnitive model would be developed in the following ways:

• Expand the models to incorporate more detailed information through increasing the dimensionality of each model, more accurately reﬂecting a physical three-dimensional system.

• Conduct experimental trials and extensive research to ensure the accuracy of certain physical parameters, such as transfer coeﬃcients for humans or precise eﬀect of soluble materials on water’s thermal properties.

• Apply geometry and coordinate transformations to explore the eﬀect of various geome- tries on the system, such as cylindrical and trapezoidal geometries.

• Analyze the steady-state distribution of the thermal energy with high accuracy across three dimensions through implementation of Laplace’s Equation, spatially dependent boundary conditions, and realistic heat loss.

10.3 Conclusions

In this paper, we modeled the temperature distribution in a bathtub in space and time in order to determine the most eﬀective method of uniformly increasing the temperature. Three models were developed to describe this temperature distribution: a steady state uniform model, an analytical heat equation model, and a numerical convection-diﬀusion equation model. Ultimately, the numerical model proved most accurate because it alone took into account bulk ﬂuid motion, the dominant heat transfer eﬀect. Using this model and the analytical model, we conducted sensitivity analyses on diﬀerent parameters to explore the eﬀects of diﬀerent bathtub geometries, the addition of soap, and other variations to the problem at hand. We also implemented PID control of the inlet water temperature and intelligent distribution of inlet water. By optimizing this process, we eﬀectively developed a strategy for quickly re-heating the bath while maintaining uniformity. Overall, our model showed that well-tuned PID control combined with distributing the inlet water upstream of the bather proved to be the most eﬀective strategy.
