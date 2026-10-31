# P-A-2016-46830-92f43919

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
For office use only T1 ________________ T2 ________________ T3 ________________ T4 ________________ Team Control Number 46830 Problem Chosen A For office use only F1 ________________ F2 ________________ F3 ________________ F4 ________________ 2016 MCM/ICM Summary Sheet

<!-- b000002 | title | pages [1] -->
Keep It Warm

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
Do you usually get annoyed with the cooling of water during a relaxing bath? In this paper, several models are proposed to solve the problem. Our efforts in building these models followed the path below.

<!-- b000005 | prose | pages [1] -->
Firstly, a universal thermodynamic model(UTM) of bath water is established by constructing two initial sub-equations named the Heat Differential Equation(HDE) and the Temperature Distribution(TD) respectively. Based on Fourier's law, the Stefan-Boltzmann law and the first law of thermodynamics, HDE is established, which also takes heat conduction, heat radiation and evaporation of water into account. Moreover, we get the numerical solution of TD by using the PDE tool of MATLAB, and fit its temperature distribution surface by the plane equation, whose goodness of fit is 0.931. The fitting equation is regarded as the approximate analytical solution.

<!-- b000006 | mixed | pages [1] -->
Secondly, taking convection caused by human movement and comfort of water temperature into account, we developed an optimization control model for the bath strategy (OCM) based on UTM, which aims at the smallest water injection, the best temperature stability & the highest comfort level. We use the model(OCM) to optimize the two following strategies：i. Injecting hot water constantly at a certain flow; ii. Injecting hot water when temperature declines to T min1 and stopping injecting when temperature increase to T min 2 . In strategy I, the optimal conditions are that the flow is 0.007L s  1 and the temperature of water injection is 311.1K. The optimization proves efficient after extensive discussion; In strategy II, the upper and lower critical temperature and the temperature of water injection are 311.7K，311.7K & 313.1K respectively. It means that the hot water injection is a continuous process.

<!-- b000007 | mixed | pages [1] -->
Thirdly, we modify UTM with the actual situation of bubble water to analyze the influence of bubble water towards the optimization, concluding that the heat dissipating power of bubble water is 45.85% of that of normal hot water at 312K. By OCM, we get the optimal conditions as the flow is 0.004L s  1 and the temperature of water injection is 311.9K , which shows that the efficiency of bubble water exceed greatly that of normal hot water.

<!-- b000008 | prose | pages [1] -->
Finally, we made error analysis of the factors like external environment etc. and did stability analysis of the geometric parameters of the bathtub & the parameters of human body. The sensitivities of the factors prove the models to be feasible and applicable.

<!-- b000009 | furniture | pages [2] -->
Team #46830

<!-- b000010 | furniture | pages [2] -->
Page 1 of 45

<!-- b000011 | heading | pages [2] -->
Contents

<!-- b000012 | contents | pages [2] -->
1    Introduction .................................................................................................. 1

<!-- b000013 | contents | pages [2] -->
1.1 Restatement of the Problem ..................................................................... 1

<!-- b000014 | contents | pages [2] -->
1.2 Our Approach ........................................................................................... 1

<!-- b000015 | contents | pages [2] -->
2    Assumptions with Justifications .................................................................. 2

<!-- b000016 | contents | pages [2] -->
2.1 About the Bathroom and Water

<!-- b000017 | contents | pages [2] -->
Do you usually get annoyed with the cooling of water during a relaxing bath? In this followed the path

<!-- b000018 | contents | pages [2] -->
below.

<!-- b000019 | contents | pages [2] -->
Fir

<!-- b000020 | contents | pages [2] -->
stly, a universal thermodynamic model(UTM) of bath water is established by constructing two initial sub

<!-- b000021 | contents | pages [2] -->
-

<!-- b000022 | contents | pages [2] -->
Temperature Distribution(TD) respectively. Based on Fourier's law, the Stefan-

<!-- b000023 | contents | pages [2] -->
Bol

<!-- b000024 | contents | pages [2] -->
tzmann conduction, heat radiation and evaporation of water into account. Moreover, we get the numerical solution of TD by using the PDE tool of MATLAB, and fit its temperatu

<!-- b000025 | contents | pages [2] -->
re

<!-- b000026 | contents | pages [2] -->
distribution surface by the plane equation, whose goodness of fit is 0.931. The fitting equation is regarded as the approximate analytical solution .

<!-- b000027 | contents | pages [2] -->
Secondly, taking convection caused by human movement and comfort of water temperature into account, we developed an optimization control model for the bath strategy

<!-- b000028 | contents | pages [2] -->
stability & the highest comfort level. We use the model(OCM) to optimize the two following strategies

<!-- b000029 | contents | pages [2] -->
：i

<!-- b000030 | contents | pages [2] -->
temperature declines to

<!-- b000031 | contents | pages [2] -->
.......................... strategy I, the

<!-- b000032 | contents | pages [2] -->
optimal conditions are that the flow is

<!-- b000033 | contents | pages [2] -->
and the temperature of 311.1K

<!-- b000034 | contents | pages [2] -->
strategy II, the upper and lower critical temperature and the temperature

<!-- b000035 | contents | pages [2] -->
311.7K，

<!-- b000036 | contents | pages [2] -->
311.7K

<!-- b000037 | contents | pages [2] -->
&

<!-- b000038 | contents | pages [2] -->
313.1K

<!-- b000039 | contents | pages [2] -->
respectively. It means that the hot water injection is a continuous

<!-- b000040 | contents | pages [2] -->
Thirdly, we modify UTM with the actual situation of bubble water to analyze the influence of bubble water towards the optimization, concluding that the heat diss power of bubble water is

<!-- b000041 | contents | pages [2] -->
45.85%

<!-- b000042 | contents | pages [2] -->
of that of normal hot water at 312K

<!-- b000043 | contents | pages [2] -->
optimal conditions as the flow is

<!-- b000044 | contents | pages [2] -->
and the temperature of water injection is

<!-- b000045 | contents | pages [2] -->
,

<!-- b000046 | contents | pages [2] -->
which shows that the efficiency of bubble water exceed greatly that of normal hot water .

<!-- b000047 | contents | pages [2] -->
stability analysis of the geometric parameters of the bathtub & the parameters of human body. The sensitivities of the factors pro

<!-- b000048 | contents | pages [2] -->
ve the models to be feasible and applicable. ........................................ 20

<!-- b000049 | contents | pages [2] -->
4.3.2 Solution of human body comfort model ..................................... 21

<!-- b000050 | contents | pages [2] -->
4.4 Optimized control model of bathing strategy ........................................ 22

<!-- b000051 | contents | pages [2] -->
4.4.1 Strategy I ..................................................................................... 23

<!-- b000052 | contents | pages [2] -->
4.4.2 Strategy II.................................................................................... 25

<!-- b000053 | contents | pages [2] -->
4.4.3 Solution of the optimal control models of strategy I & II........... 27

<!-- b000054 | contents | pages [2] -->
4.5 Bubble bath ............................................................................................ 31

<!-- b000055 | contents | pages [2] -->
4.5.1 The effect of bubble water .......................................................... 31

<!-- b000056 | contents | pages [2] -->
4.5.2 Effect of bubble water on optimal control strategy..................... 32

<!-- b000057 | contents | pages [2] -->
5    Testing the Model....................................................................................... 34

<!-- b000058 | contents | pages [2] -->
5.1 Error Analysis ........................................................................................ 34

<!-- b000059 | contents | pages [2] -->
5.1.1 Various factors of external environment ..................................... 34

<!-- b000060 | contents | pages [2] -->
5.1.2 Various factors of water .............................................................. 35

<!-- b000061 | contents | pages [2] -->
5.1.3 Various factors of human ............................................................ 35

<!-- b000062 | contents | pages [2] -->
5.1.4 Error in modeling and solving process ....................................... 35

<!-- b000063 | contents | pages [2] -->
5.2 Sensitivity Analysis................................................................................ 36

<!-- b000064 | contents | pages [2] -->
5.2.1 Sensitivity to the shape and volume of the tub ........................... 37

<!-- b000065 | contents | pages [2] -->
5.2.2 Sensitivity to the human parameters ........................................... 37

<!-- b000066 | contents | pages [2] -->
5.2.3 Sensitivity to the heat transfer rate.............................................. 38

<!-- b000067 | contents | pages [2] -->
6    Conclusions ................................................................................................ 38

<!-- b000068 | contents | pages [2] -->
6.1 Strengths and Weaknesses...................................................................... 38

<!-- b000069 | contents | pages [2] -->
6.1.1 Strengths...................................................................................... 38

<!-- b000070 | contents | pages [2] -->
6.1.2 Weaknesses ................................................................................. 39

<!-- b000071 | contents | pages [2] -->
6.2 Comprehensive Results.......................................................................... 39

<!-- b000072 | furniture | pages [3] -->
Team #46830

<!-- b000073 | furniture | pages [3] -->
Page 2 of 45

<!-- b000074 | contents | pages [3] -->
6.3 Future Work ........................................................................................... 40

<!-- b000075 | contents | pages [3] -->
7    Explanation ................................................................................................ 41

<!-- b000076 | contents | pages [3] -->
References ............................................................................................................ 42

<!-- b000077 | furniture | pages [4] -->
Team #46830

<!-- b000078 | furniture | pages [4] -->
Page 1 of 45

<!-- b000079 | heading | pages [4] -->
1    Introduction

<!-- b000080 | heading | pages [4] -->
1.1 Restatement of the Problem

<!-- b000081 | prose | pages [4] -->
Taking a bath, can remove dirt, eliminate fatigue, promote blood circulation, improve sleep quality, and enhance metabolism. And by soaking in warm water, one can treat certain diseases and combat bacterium in some degrees.

<!-- b000082 | prose | pages [4] -->
The problem needs us to develop a mathematical model to finding out the best bathing strategy depends on the shape/volume of the tub, and the parameters and the motions of the person in the bathtub. This model aims at keeping the temperature even throughout the bathtub and as close as possible to the initial temperature without wasting too much water.

<!-- b000083 | prose | pages [4] -->
We need consider the following:

<!-- b000084 | prose | pages [4] -->
·Build a thermodynamic model of water in tub to describe the temperature in space and time in the following processes:

<!-- b000085 | prose | pages [4] -->
i. The process of filling the tub with hot water;

<!-- b000086 | prose | pages [4] -->
ii. The natural cooling process of water;

<!-- b000087 | prose | pages [4] -->
iii. The process of adding hot water.

<!-- b000088 | prose | pages [4] -->
·Consider the influences of the motions of people in tub, and analyze the results of this influences. We need to deal with the obstacle caused by the convection of water and the accompanying heat exchange.

<!-- b000089 | prose | pages [4] -->
·Find out the best control strategy to keep the temperature and save water as possible. The strategy depends on the parameters of tub, the degree of human movement, and the parameters of the human body.

<!-- b000090 | prose | pages [4] -->
·Discuss the difference between water and bubble bath water. We shall clarify how the bubble bath water influences the model and the strategy we have given.

<!-- b000091 | prose | pages [4] -->
·We need to provide a one-page non-technical explanation for users of the bathtub that describes our strategy. It shall explain why it is so difficult to get an evenly maintained temperature throughout the bath water and the advice according to our model.

<!-- b000092 | heading | pages [4] -->
1.2 Our Approach

<!-- b000093 | prose | pages [4] -->
We analyzed the problems above and consulted lots of literature, and then come up with the following approaches:

<!-- b000094 | prose | pages [4] -->
·We analyzed the problems above and consulted lots of literature, and then come up with the following approaches:

<!-- b000095 | furniture | pages [5] -->
Team #46830

<!-- b000096 | furniture | pages [5] -->
Page 2 of 45

<!-- b000097 | prose | pages [5] -->
·We build a general thermodynamic model for water bath. This model is based on the Fourier law, the Newton cooling theorem, Stern-boltzmann's law, the heat conduction formula, and the first law of thermodynamics. And it includes:

<!-- b000098 | prose | pages [5] -->
I.Heat exchange between hot water and bathtub II. Heat exchange between hot water and air, III.Evaporation heat absorption of hot water, IV.Heat absorption and heat release of human body, V.Heat radiation of water, VI. Heat of added hot water and heat carried away by the overflow.

<!-- b000099 | prose | pages [5] -->
·We build a distribution model for water in bathtub. This model is mainly based on the heat conduction equation and the Neumann boundary condition. Unfortunately, the model can only be solved by Matlab, and can't get accurate analytic function expression. So we build an approximate analytical model for water temperature distribution.

<!-- b000100 | prose | pages [5] -->
·We build a forced convection model for the water in the bathtub. The motion of human body in the water will be the force of water. And the convection of water accelerates the heat exchange of water. So we quantify human motion, then build a model for forced convection heat exchanging. This model describes the redistribution of the water temperature under the influence of human motion.

<!-- b000101 | prose | pages [5] -->
·We build an optimal control strategy model based on thermodynamics, water temperature distribution and forced convection. The model is mainly based on nonlinear multivariable optimal control, use it to get the optimal control strategy. We will provide two control strategies based on different aspects under this model.

<!-- b000102 | prose | pages [5] -->
·We obtain the thermodynamic model for bubble bath water by improving general thermodynamic model. Based on this model, we discussed the effects of bubble bath water on the distribution and variation of water temperature, then analyzes the influence of the bubble bath water to the optimal control strategy. At the same time, we analyzed the advantages of bubble bath water.

<!-- b000103 | prose | pages [5] -->
·We use the finite difference method to solve the partial differential equations and the piecewise differential equations.

<!-- b000104 | heading | pages [5] -->
2    Assumptions with Justifications

<!-- b000105 | prose | pages [5] -->
We make the following assumptions about the whole process in this paper to obtain a better model result.

<!-- b000106 | furniture | pages [6] -->
Team #46830

<!-- b000107 | furniture | pages [6] -->
Page 3 of 45

<!-- b000108 | heading | pages [6] -->
2.1 About the Bathroom and Water

<!-- b000109 | prose | pages [6] -->
1. Assume that the air temperature and humidity in the bathroom is constant, not due to the Water vapor from man and bathtub. The temperature and humidity distribution of air is affected by many factors, this problem is very difficult. The other reason is that the discussion of air temperature and humidity not mean much.

<!-- b000110 | prose | pages [6] -->
2. Without taking into account the wave generated by the motion of human and the adding of water, as well as the overflow caused by waves. The reason is that the water wave will be reflected back by the Inner wall of bathtub and leads multiple interference, it is very difficult to study this process. In addition, this mechanical process will not have a significant impact on the thermodynamic process of the bathtub-hot water-human system.

<!-- b000111 | prose | pages [6] -->
3. Regardless of the time between the hot water comes out of the tap and enters the bathtub, which means that ignoring heat dissipation of water in the air. The reason is that the setting position of the tab should be as close as possible to the surface of the full water in the bathtub. That means the time for water to stay in the air is so short that the amount of heat dissipation in the air is negligible.

<!-- b000112 | prose | pages [6] -->
4. Natural convection due to temperature gradient is negligible. Consider only the forced convection caused by the movement of the human. Because the temperature gradient of the bath water is not large enough to consider the natural convection of water caused by it.

<!-- b000113 | prose | pages [6] -->
5. The convection of water inside the bath tub does not affect the current water temperature. The reason is that heat exchange caused by convective occurs only between the parts of the water in the bathtub, this process does not get heat exchange from the outside of the system, in other words, only water temperature distribution changed.

<!-- b000114 | prose | pages [6] -->
6. The physical parameters such as the thermal conductivity, density and the bubble thickness are not changed with the addition of hot water and the loss of overflow water. Although the concentration of bubble water is bound to change with the addition and loss of water, the influence of bubble water concentration on other physical parameters is complicated and not clear, and the change of concentration is quite small for some parameters. Therefore, ignore the bubble water physical properties change over time

<!-- b000115 | heading | pages [6] -->
2.2 About the Human Body

<!-- b000116 | prose | pages [6, 7] -->
7. Heat conductivity of human body is the constant value, it do not change with human posture and body temperature. Because the heat absorption and release of the human body is a complex process of biochemical reaction and physical process. Some factors like the metabolic heat generation, human sweat evaporation and the work done by exercise need to be considered. Since the thermodynamic process in the human body is too complicated and difficult to be analyze, considered the human body as a constant temperature heat source (maybe it’s endothermic), its thermal conductivity is a constant value.

<!-- b000117 | furniture | pages [7] -->
Team #46830

<!-- b000118 | furniture | pages [7] -->
Page 4 of 45

<!-- b000120 | prose | pages [7] -->
8. Each part of the body surface temperature is a constant value. Because the distribution of body temperature is difficult to parameterized, and the body temperature of each part is slightly different(around 0.6℃). Consider that all over the body surface, the temperatures are the same constant.

<!-- b000121 | prose | pages [7] -->
9. Ignore the work of the forced convection generated by human motion. As the fluid, water can only work rely on its viscous force, and the viscous force is too small to be taken into account.

<!-- b000122 | prose | pages [7] -->
10. Considered the human motion as a series of discrete motion with the same amplitude and frequency. Although the motions can have a huge impact on the environment, such as the spatial distribution of water temperature, the movement of people is very irregular. So we use a simple physical quantity to describe the intensity and speed of human motion. For the magnitude of the motions, we will discuss it in detail in the 4.2 chapter.

<!-- b000123 | heading | pages [7] -->
3    Notations

<!-- b000124 | prose | pages [7] -->
All the variables and constants used in this paper are listed in Table1 and Table 2.

<!-- b000125 | caption | pages [7] -->
Table 1 Symbol Table–Constants

<!-- b000126 | prose | pages [7] -->
Symbol Definition Value

<!-- b000127 | prose | pages [7] -->
298K Air temperature 0T P Saturated vapor pressure  3 2.4 10 Pa  Density of water  3 3 10 kg m  Molar mass of water     3 1 18 10 kg mol R Universal gas constant     1 1 8.31J mol K c Specific heat capacity of water      3 1 1 4.2 10 J kg K  0.97 Surface radiation coefficient of water

<!-- b000128 | prose | pages [7, 8] -->
 Stefan-Boltzmann constant       8 2 4 5.67 10 W m K Symbol Definition Units Q J Internal energy of the water in the bathtub

<!-- b000129 | furniture | pages [8] -->
Team #46830

<!-- b000130 | furniture | pages [8] -->
Page 5 of 45

<!-- b000131 | caption | pages [8] -->
Table 2 Symbol Table–Variables

<!-- b000133 | prose | pages [8] -->
Average temperature of water at time t K T t ( ) J Heat of heat exchange Q exchange J Heat of water evaporation Q evaporation J Heat absorbed by the body Q body J Heat of radiation Q radiation T x y z t ( , , , ) K Distribution of temperature in time and space

<!-- b000134 | prose | pages [8] -->
u T ( ) Water evaporation rate m s  1

<!-- b000135 | prose | pages [8] -->
k Water flow s  3 1 m K The outlet water temperature 0T  m The movement distance of the k th kS The volume distance of the k th V 3 m k F Source of forced convection 4 m Best water flow bk s  3 1 m K The best outlet water temperature bT 

<!-- b000136 | heading | pages [8] -->
4    The Model

<!-- b000137 | prose | pages [8] -->
We establish an optimal control strategy model based on our normal thermodynamic model, forced convection model of water temperature and body temperature comfort model. Here are the relationship among the three models and equations.

<!-- b000138 | prose | pages [8] -->
Initial Sub equation Heat differential equation Temperature distribution

<!-- b000139 | prose | pages [8] -->
Body temperature Universal thermodynamic model Forced convection Secondary Sub model comfort model model

<!-- b000140 | prose | pages [8, 9] -->
Final model Optimal control model of the bath strategy According to our model, we propose two kinds of temperature control strategies and analyze their both advantages and shortages. In addition, the shape and volume of the tub, the temperature, flow and convection of tap water, the motions made by the person and some other parameters are extensively discussed in this section. The establishment and solution of our models are as follow.

<!-- b000141 | furniture | pages [9] -->
Team #46830

<!-- b000142 | furniture | pages [9] -->
Page 6 of 45

<!-- b000143 | caption | pages [9] -->
Figure 1: The relationship among the models and equations

<!-- b000145 | heading | pages [9] -->
4.1 Normal Thermodynamic Model of Water Temperature

<!-- b000146 | prose | pages [9] -->
In this section, we set up a normal thermodynamic model of water temperature in space and time, which is based on Fourier's law, Newton's law of cooling, the Stefan-Boltzmann law, the heat conduction equation and the first law of thermodynamics.

<!-- b000147 | prose | pages [9] -->
We use Newton's law of cooling, the Stefan-Boltzmann law and the first law of thermodynamics to solve the problem of the distribution of temperature with time. And we use heat conduction equation to solve the problem of the distribution of temperature with space. In our model, the heat transfer and the heat radiation are taken into account while the convection is ignored.

<!-- b000148 | heading | pages [9] -->
4.1.1 The differential equation of water heat in the tub

<!-- b000149 | prose | pages [9] -->
Considering the origin and destination of the infinitesimal of water heat in the tub, we get the differential equation as follows

<!-- b000150 | prose | pages [9] -->
      dQ dQ dQ dQ dQ dQ dQ (1)   exchange evaporation body radiation water water

<!-- b000151 | prose | pages [9] -->
Here are the derivation and explanation of the equation by analyzing the heat of each part.

<!-- b000152 | prose | pages [9, 10] -->
First of all, assuming the tub as a cube with length a, width b and height H. Then we set a three-dimensional Cartesian coordinate system originated from the bottom center of the tub and paralleled to its height, length and width. As we all know, the drain and overflow valve of the tub are often designed in the midpoint of the two short   a H sides. Thus, the overflow valve is located in and the drain is in  0, ,    2    a H . 0, ,    2  To establish the model of water temperature over time, we firstly consider that the volume of water is changing over time. When the tub isn’t full, the volume of water is proportional to the time growth. Because we usually open the valve to the maximum when we are going to take a shower, the growth rate of the volume of water over time is the biggest flow of the valve. Then, when the volume is proper, people enter the tub and from then on, the volume can be regarded as constant approximately. Here comes the equation.

<!-- b000153 | furniture | pages [10] -->
Team #46830

<!-- b000154 | furniture | pages [10] -->
Page 7 of 45

<!-- b000155 | caption | pages [10] -->
Figure 2: the three-dimensional Cartesian coordinate system of the tub

<!-- b000157 | prose | pages [10] -->
 V  0 k t 0 t  max k max  V V   V t 0  0 k max

<!-- b000158 | prose | pages [10] -->
  Where, , it means that the largest volume of water when the V abH V 0 body

<!-- b000159 | prose | pages [10] -->
k person is in the tub without overflow. is the largest flow of the valve. max

<!-- b000160 | prose | pages [10] -->
By the definition of internal energy, we get the equation of the energy of water in the tub.

<!-- b000161 | prose | pages [10] -->
   Q c T t ( ) dV (2) 

<!-- b000162 | prose | pages [10] -->
Where, T t is the average water temperature on space, which can be defined ( )

<!-- b000163 | prose | pages [10] -->
by   T x y z t ( , , , ) dV  T t ( ) (3)  dV  Then, we analyze different part of the heat exchange. The heat exchange is composed of heat transfer, heat radiation, convection, the inflow of hot water and the outflow of cold water. Here we discussed them except convection which is discussed in 4.2.

<!-- b000164 | prose | pages [10, 11] -->
First, we analyze the heat loss due to heat exchange[5]. The loss is caused by the contact of water with the inner wall of the tub and air. According to the Fourier's law, the heat transfer power of per unit area is proportional to the temperature difference and to the thickness of the heat transfer medium. If we suppose that the thickness of the tub wall is constant and its material is homogeneous, the heat transfer power of per unit area is proportional to the temperature difference only. Thus we get the equation of the whole heat emission in unit time.

<!-- b000165 | furniture | pages [11] -->
Team #46830

<!-- b000166 | furniture | pages [11] -->
Page 8 of 45

<!-- b000168 | prose | pages [11] -->
         dQ h T x y z t [ ( , , , ) T dA ] h T x y z t [ ( , , , ) T dA dt ] (4)   exchange 0 0    D

<!-- b000169 | prose | pages [11] -->
Where, h is the heat transfer coefficient of water when the medium is the tub wall. h is the heat transfer coefficient of water to air.

<!-- b000170 | prose | pages [11] -->
Secondly, we analyze the heat loss due to water evaporation. According to the surface molecular evolution rule and Dalton's law of evaporation, the evaporation rate per unit area is related to the liquid temperature, surface wind speed and humidity. Because of assumption 1, humidity is constant and the evaporation rate per unit area is related to the liquid temperature. Here comes the following equation.

<!-- b000171 | prose | pages [11] -->
        dQ u T q dA dt    evaporation gas    D (5)  1      2      u T 1 w     P  2 RT   0

<!-- b000172 | prose | pages [11] -->
 u T is the rate of water evaporation per unit time and area; Where,

<!-- b000173 | prose | pages [11] -->
T is the air temperature of the air to water surface;

<!-- b000174 | prose | pages [11] -->
P is the saturated vapor pressure of water at current temperature;

<!-- b000175 | prose | pages [11] -->
w is the relative humidity of air in the bathroom, which is constant according to assumption 1;

<!-- b000176 | prose | pages [11] -->
    3 3 10 kg m , which is the density of water ;

<!-- b000177 | prose | pages [11] -->
      3 1 18 10 kg mol , which is the mole mass of water;

<!-- b000178 | prose | pages [11] -->
     1 1 R 8.31 J mol k , which is the universal gas constant;

<!-- b000179 | prose | pages [11] -->
Third, we analyze the heat loss due to people’s body [7]. To be specific, it describes the heat exchange of people’s body surface and water. We suppose that the body is fully immersed in water, so the contact area between body and water is the superficial area of the body. Because the heat exchange between the human body and the water is the heat transfer through the water flow, according to Newton cooling theorem, we get the heat infinitesimal equation of body’s absorption.

<!-- b000180 | furniture | pages [12] -->
Team #46830

<!-- b000181 | furniture | pages [12] -->
Page 9 of 45

<!-- b000182 | prose | pages [12] -->
    dQ S [ ( ) T t T ] h dt (6) body body body body

<!-- b000183 | prose | pages [12] -->
Where, is the heat transfer rate of human body and water. Because the h body

<!-- b000184 | prose | pages [12] -->
similarity of the macroscopic physical properties between human body and water,

<!-- b000185 | prose | pages [12] -->
can be substituted with heat transfer rate of water and water. T t is the ( ) h body

<!-- b000186 | prose | pages [12] -->
average water temperature in the tub. The reason to set this parameter is because the surface of human body is irregular, the temperature distribution between the contact surfaces is harder to formulate. Then we regard the average water temperature in the tub as that of the contact surfaces.

<!-- b000187 | prose | pages [12] -->
Fourth, we analyze the heat loss due to heat radiation [10]. To be specific, it describes that water dissipates heat in the form of electromagnetic radiation to the surrounding and the loss can be calculated by Trevor Boltzmann's law. Unfortunately, the law is set to describe the heat radiation of ideal black-body, while water isn’t totally suit. Thus we modify the law with a rate of heat radiation , and it is recorded  that the rate of water is . we get the heat infinitesimal equation of the loss. 0.97

<!-- b000188 | prose | pages [12] -->
       4 dQ T x y z t dA dt , , , (7)  radiation   

<!-- b000189 | prose | pages [12] -->
Fifth, we analyze the heat increase due to the constant intake of hot water. According to the definition of the internal energy of water, we get the heat infinitesimal equation of the increase.

<!-- b000190 | prose | pages [12] -->
      dQ c T dV c T kdt (8)  water 0 0

<!-- b000191 | prose | pages [12] -->
Sixth, we analyze the heat loss due to the overflow water. We assume the overflow water temperature as the temperature of the water near the outfall and get the heat loss equation.

<!-- b000192 | prose | pages [12] -->
a a      dQ c T (0, , H t dV , ) c T (0, , H t , ) kdt (9)  water 2 2 To sum up, the origin and destination of the water heat in the tub are shown below.

<!-- b000193 | furniture | pages [13] -->
Team #46830

<!-- b000194 | furniture | pages [13] -->
Page 10 of 45

<!-- b000195 | caption | pages [13] -->
Figure 3: The origin and destination of heat

<!-- b000196 | prose | pages [13] -->
Combining the six equations of heat exchange [15], we get the universal differential equation of the internal energy of water over temperature in the tub.

<!-- b000197 | prose | pages [13] -->
      dQ dQ dQ dQ dQ dQ dQ   exchange evaporation body radiation water water

<!-- b000198 | heading | pages [13] -->
4.1.2 Thermodynamic analysis of bath process

<!-- b000199 | prose | pages [13] -->
In this section, according to the periodic change of the volume of water in the tub, we divide the water temperature in the tub over time into three stages:

<!-- b000200 | prose | pages [13] -->
First, the initial filling stage. In this stage, people inject water to the tub when people get into the tub while the water won’t overflow. Then we modify the heat loss

<!-- b000201 | prose | pages [13] -->
dQ due to the overflow water in the differential equation of water heat in the tub water

<!-- b000202 | prose | pages [13] -->
and get the function of the volume of water and the differential equation of the change of water internal energy as follow:

<!-- b000203 | prose | pages [13] -->
  V kt      dQ dQ dQ dQ dQ  exchange evaporation radiation water

<!-- b000204 | prose | pages [13] -->
Second, the natural cooling stage when the tub is full of water and body. In this

<!-- b000205 | prose | pages [13] -->
V . According to the assumption 2, we modify the heat increase stage, the volume is 0

<!-- b000206 | prose | pages [13] -->
dQ due to the constant intake of hot water and the heat loss due to the overflow water

<!-- b000207 | prose | pages [13] -->
dQ water in the differential equation of water heat in the tub and get the water

<!-- b000208 | prose | pages [13] -->
function of the volume of water and the differential equation of the change of water internal energy as follow:

<!-- b000209 | prose | pages [13] -->
  V V 0      dQ dQ dQ dQ dQ  exchange evaporation body radiation

<!-- b000210 | prose | pages [13] -->
Third, the reheating after hot water injection stage. In this stage, users are unsatisfactory with the water temperature in the tub and then open the tap again to mix the intake hot water with the previous water in the tub. Owing to the limitation of the volume of the tub, excess water overflows to keep the tub full. We get the function of the volume of water and the differential equation of the change of water internal energy as follow:

<!-- b000211 | prose | pages [13] -->
  V V 0 a           dQ dQ dQ dQ dQ c kT dt c kT (0, , H t , ) dt  exchange evaporation body radiation 0 2

<!-- b000212 | furniture | pages [14] -->
Team #46830

<!-- b000213 | furniture | pages [14] -->
Page 11 of 45

<!-- b000214 | heading | pages [14] -->
4.1.3 Temperature field distribution of the water in the tub

<!-- b000215 | prose | pages [14] -->
In this section, we establish a model of the distribution of water temperature in the tub when injecting hot water again, and solve the model by the PDE tool of Matlab. However, the solution is difficult to be used in the following models, hence we use plane fitting in the numerical solution and fortunately. Then we find that the fitting degree is pretty high. So we use the fitting plane as approximate analytic solution of temperature field distribution of water. It greatly simplifies the difficulty of solving the model, at the same time, with good accuracy.

<!-- b000216 | prose | pages [14] -->
1. Temperature field distribution based on heat conduction equation  a H t According to assumption 4, water temperature near the tap (0, is , , ) 2  a H t constant when injecting water. That is to say, here (0, is a constant , , ) 2 temperature heat source, because whenever the water drop from the tap, the temperature is the same. Therefore, taken heat conduction equation into account, we use the following partial differential equations to describe the temperature field distribution of the water.

<!-- b000217 | prose | pages [14] -->
        T T T T a         c ( ) ( ) ( ) q (0, , H t , )        t x x y y z z 2

<!-- b000218 | prose | pages [14] -->
 is thermal diffusion coefficient,  is the thermal   2 Where, ( m s )  c

<!-- b000219 | prose | pages [14] -->
  a a H t q (0, , H t , ) is the equivalent heat source at (0, , , ) conductivity, . 2 2 The Neumann boundary [8] of the water in the tub can be formulated as:

<!-- b000220 | prose | pages [14] -->
    T b      h T ( , , , ) y z t T    0  x  2       T a      h T x ( , , , ) z t T     0  y  2  Boundary    T      h T x y ( , ,0, ) t T  0  z   T       1 h T x y H t ( , , , ) T  0   z

<!-- b000221 | prose | pages [14] -->
 T x y z ( , , ,0) T x y z ( , , ) The starting conditions is . 0

<!-- b000222 | prose | pages [14, 15] -->
T x y z is the distribution of water temperature in the tub before the second 0( , , ) of rejecting hot water again.

<!-- b000223 | furniture | pages [15] -->
Team #46830

<!-- b000224 | furniture | pages [15] -->
Page 12 of 45

<!-- b000226 | prose | pages [15] -->
2.The numerical solution of the heat conduction equation [9] We solve the heat conduction model by the PDE tool of Matlab [13][14]. During the process, the starting condition is that the water temperature is 39 centigrade and distributed evenly. The reasons of setting such condition are as follow. First, people’s action will stir the water to a uniform distribution. On the other hand, it’s recorded that 39 centigrade is the most comfortable temperature for bathing. If the water temperature is lower than that, people will inject hot water to heat the water.

<!-- b000227 | prose | pages [15] -->
We set the temperature of the equivalent heat source 45 centigrade to solve the temperature field at 2.5s and 100s, here are the results:

<!-- b000228 | caption | pages [15] -->
Figure 4: Surface temperature field at 2.5s

<!-- b000229 | caption | pages [15] -->
Figure 5: Surface temperature field at 100s

<!-- b000230 | prose | pages [15] -->
The arrow in the figure is the direction of heat transmission. We get the similarities and differences between the temperature distributions of 2.5s and 100s by comparing them.

<!-- b000231 | prose | pages [15] -->
Similarities:

<!-- b000232 | prose | pages [15, 16] -->
i. The heat always spread from the tap, and is gradually dispersed throughout the space. What’s more, temperature distribution is uniform at the end of the outlet. The reason is that the heat is gradually spreading from the inlet to the outlet, during the   process, it disperses evenly in the x o z plane, which is in accordance with the actual situation.

<!-- b000233 | furniture | pages [16] -->
Team #46830

<!-- b000234 | furniture | pages [16] -->
Page 13 of 45

<!-- b000236 | prose | pages [16] -->
ii. At the start of injecting hot water, the water temperature near the inlet is keeping at approximately 45 centigrade, while near the out, the temperature is about 40 centigrade. The reason is that water is a poor conductor of heat. 2.5s and 100s are too short to transfer heat evenly. Thus the temperature near outlet doesn’t enhance obviously.

<!-- b000237 | prose | pages [16] -->
Differences:

<!-- b000238 | prose | pages [16] -->
i. The distribution of water temperature at 100s is more even than that at 2.5s. Obviously, the longer time makes the heat transfer more adequate between the intake of water and the previous water in the tub.

<!-- b000239 | prose | pages [16] -->
ii. The total water temperature in the tub is higher at 100s, because the longer time makes bigger amount of hot water injection, enhancing the average water temperature in the tub.

<!-- b000240 | prose | pages [16] -->
iii. The spread of heat in y direction is uniform at 100s, because the whole level of water temperature and the distribution of water temperature gradually becomes   stable over time. Moreover, the distribution of temperature in plane x o z becomes uniform owing to heat transfer. Hence, the spread of heat in y direction is uniform. That means the distribution of the gradient in the Y axis is tend to decrease linearly with the value of y coordinate III. The approximate analytical solution By means of linear fitting, we get the approximate analytic solution of temperature distribution in space. Because in the discussion of the universal thermodynamic model of the water temperature in the previous paper and the optimal bath strategy and bubble bath, we all need the analytical solution of water temperature over time and space to do the further analysis and solution. Nevertheless, it’s more than hard to use the numerical solution of temperature field directly and to optimize the following models. Therefore, we carry out a simple function fitting to the distribution of the water temperature in space.

<!-- b000241 | prose | pages [16] -->
First of all, we observe the distribution surface of temperature in space, which is shown as follows.

<!-- b000242 | furniture | pages [17] -->
Team #46830

<!-- b000243 | furniture | pages [17] -->
Page 14 of 45

<!-- b000244 | caption | pages [17] -->
Figure 6: The distribution surface of temperature in space

<!-- b000245 | prose | pages [17] -->
Combined with the previous analysis, we firstly fit the above surfaces by plane fitting. In our opinion, the linear relationship in the subsequent model will be greatly simplified calculation, and the characteristic of linear, simple and clear has a good approximation to the real situation. Therefore, we select a number of discrete points on the surface of temperature distribution, and try to make the linear fitting to these points. The fitting plane is shown as follows

<!-- b000246 | prose | pages [17] -->
    T x y z ( , , ,2.5 ) s 44.63 4.294 y 0.08328 x        0 y 1.3, 0.4 x 0.4,0 z 0.49 

<!-- b000247 | prose | pages [17] -->
R  2 0.931 The goodness of fit of this kind of fitting method is , which shows a

<!-- b000248 | prose | pages [17] -->
great fit for this distribution surface. Thus we determine to use the fitting method and the fitting plane is shown in Figure 7.

<!-- b000249 | caption | pages [17] -->
Figure 7: The fitting plane

<!-- b000250 | prose | pages [17] -->
  plane, so is the temperature In addition, the tub is symmetrical at y o z

<!-- b000251 | prose | pages [17] -->
distribution of abstract mathematical model. Moreover, it should be dispersed

<!-- b000252 | prose | pages [17] -->
  plane. However, the temperature function ( , , ,2.5 ) T x y z s over uniformly at x o z

<!-- b000253 | prose | pages [17, 18] -->
x coordinate in the previous fitting plane generates from the error of taking discrete points. Thus the ideal model of the plane should be    T x y z ( , , ,2.5 ) s 44.63 4.294 y        0 y 1.3, 0.4 x 0.4,0 z 0.49  We extend the model to the water temperature distribution at any time, because 2.5s is the very moment when hot water flows into the tub continuously. And at 2.5s, the water temperature gradient is one of the largest, and the distribution is the most uneven. After this moment, the temperature will gradually distribute more evenly and the temperature surface also becomes more close to a plane. Therefore, it’s proper to use the distribution function to describe the water temperature distribution of the other moments after 2.5s. The distribution equation can be universally formulated as     T x y z t ( , , , ) C t K t y (10)

<!-- b000254 | furniture | pages [18] -->
Team #46830

<!-- b000255 | furniture | pages [18] -->
Page 15 of 45

<!-- b000257 | prose | pages [18] -->
  C t 、 K t are the functions on time. Where

<!-- b000258 | prose | pages [18] -->
    K t T x y z t , , , We should notice that , which means negative gradient of

<!-- b000259 | prose | pages [18] -->
temperature distribution function.

<!-- b000260 | prose | pages [18] -->
We set the average water temperature into formula (3) to get the following relationship:

<!-- b000261 | prose | pages [18] -->
a         T x y z t ( , , , ) dV bH C t K t y dy 2   a       T t ( ) C t 2  abH dV 

<!-- b000262 | prose | pages [18] -->
Thus the model of the temperature distribution can be transformed in to    T x y z t ( , , , ) T t ( ) K t y (11)

<!-- b000263 | prose | pages [18] -->
On the other hand, The variance in the spatial distribution of the water temperature in the tub is  2 2 a K t  D T  12

<!-- b000264 | prose | pages [18] -->
Hence, we get the variance of water temperature at a moment with the realistic data or by programming to get a series of points randomly selected on the surface of the numerical simulation of temperature in 4.1.3.II. Then the temperature gradient equation of the moment is  2 3D T   K t (12) a

<!-- b000265 | prose | pages [18, 19] -->
 K t over time. Unfortunately, with limited time, we don’t fit the function of  K t is given by an unknown function in the thermodynamic model of water. If So

<!-- b000266 | furniture | pages [19] -->
Team #46830

<!-- b000267 | furniture | pages [19] -->
Page 16 of 45

<!-- b000269 | prose | pages [19] -->
time permits, we will surely fit it into a simple function.

<!-- b000270 | heading | pages [19] -->
4.1.4 The universal thermodynamic model of water

<!-- b000271 | prose | pages [19] -->
In this section, under the condition that water is in the absence of human movement interference, we get the model in time and space.

<!-- b000272 | prose | pages [19] -->
We take formula (11) into formula (4) and formula (9) and get:

<!-- b000273 | prose | pages [19] -->
               dQ h T t ( ) T ab 2 aH 2 bH h T t ( ) T ab dt     exchange 0 0

<!-- b000274 | prose | pages [19] -->
  a      dQ c T t ( ) K t dV    water  2 

<!-- b000275 | prose | pages [19] -->
In addition, we note that the inner wall of the tub is smooth, and at the beginning of the design of the tub, we propose that coating the metal film on the surface of the tub can effectively reduce the heat radiation power of the water in the tub, just like thermos bottles. Thus we ignore the heat radiation of micro electromagnetic wave through the inner wall of the tub. At the same time, we take formula (11) into formula (7) and get:

<!-- b000276 | prose | pages [19] -->
  5 5   a        b a a 4                dQ b T t ( ) K t y dy dt T t ( ) K t T t ( ) K t dt     2        a radiation 5 K t  2   2         2

<!-- b000277 | prose | pages [19] -->
At this time we simplify our universal thermodynamic model of water in a great degree. The mathematical model is given by the following equations:

<!-- b000278 | prose | pages [19] -->
        dQ dQ dQ dQ dQ dQ dQ   exchange evaporation body radiation water water                  dQ h T t ( ) T ab 2 aH 2 bH h T t ( ) T ab dt     exchange 0 0    dQ uabq dt evaporation gas       dQ S [ ( ) T t T ] h dt body body body body    5 5         b a a         dQ T t ( ) K t T t ( ) K t dt    (13)      radiation 5 K t  2   2              dQ c T dV c T kdt   water 0 0    a       dQ c T t ( ) K t dV    water   2       Q c V t T t ( )      T x y z t ( , , , ) T t ( ) K t y 

<!-- b000279 | furniture | pages [20] -->
Team #46830

<!-- b000280 | furniture | pages [20] -->
Page 17 of 45

<!-- b000281 | heading | pages [20] -->
4.2 Forced convection model

<!-- b000282 | prose | pages [20] -->
In this section, we set up a model of convection [1][2] heat transfer of water caused by human movement. First we quantify the human movement’s influence on convection, so we define the forced convective cell, use this parameter to describe the human movement’s influence on convection and the temperature distribution. Then we set up a model of the forced convective cell’s influence on the temperature. This model is based on a partial large normal distribution function. Finally, we established a model of the human movement’s influence on the temperature distribution in the bathtub.

<!-- b000283 | heading | pages [20] -->
4.2.1 The introduction of forced convection source

<!-- b000284 | prose | pages [20] -->
kV ) moving (distance= kS ) in a Consider the case of an object (volume=

<!-- b000285 | prose | pages [20] -->
bathtub. In essence, the principle of the movement of the object in water can cause the forced convection of water is: In the process of moving the object pushed a part of the water, while the other water filled to its original position, this process has caused the movement of water and water, to complete this action in the form of flow (Fig 8). As a result, the movement of the object causes the water to flow, while the convection of the water has a corresponding heat exchange.

<!-- b000286 | prose | pages [20] -->
Sk

<!-- b000287 | prose | pages [20] -->
Vk

<!-- b000288 | caption | pages [20] -->
Figure 8: Forced convection cause by body

<!-- b000289 | prose | pages [20] -->
We abstract every movement of a person as an object in the water [6]. Because the movement of a person's bath is a process of moving one part of the body from one position to the other. This process will be pushed the moving path of the water, while the other water filled to its original position, resulting in convection. So we define human motion intensity as the forced convection cell. According to the assumption 11, we use k to mark the number of forced convection, its definition is as follows:

<!-- b000290 | prose | pages [20, 21] -->
  F S V k k k kV is the volume of the moving part of the body during the k th Where,

<!-- b000291 | furniture | pages [21] -->
Team #46830

<!-- b000292 | furniture | pages [21] -->
Page 18 of 45

<!-- b000294 | prose | pages [21] -->
kS is the distance of the moving part of the body during the k th movement,

<!-- b000295 | prose | pages [21] -->
movement

<!-- b000296 | heading | pages [21] -->
4.2.2 Effect of forced convection on the temperature

<!-- b000297 | prose | pages [21] -->
The movement of people to produce convection, the result of convection is to make the distribution of temperature in the water more balanced. Further considered,

<!-- b000298 | prose | pages [21] -->
F through a non-negative function f F ( ) the forced convection source so that the k k

<!-- b000299 | prose | pages [21] -->
temperature of each point in the water is closer to the average temperature, so we got the formula:

<!-- b000300 | prose | pages [21] -->
           (14) T 1( , , , ) x y z t T x y z t ( , , , ) f F ( ) T x y z t ( , , , ) T t ( )   k k k

<!-- b000301 | prose | pages [21] -->
F , the distribution function After the effect of the k th forced convection source k

<!-- b000302 | prose | pages [21] -->
kT 1( , , , ) x y z t kT x y z t . ( , , , ) of water temperature in space became from 

<!-- b000303 | prose | pages [21] -->
According to the formula (14), we obtain after a forced convection source affects, the resulting convection only changes the temperature distribution, and doesn’t cause a mutation of the water’s average temperature. This phenomenon is consistent with the hypothesis 6, which shows that the model is self-consistent and reasonable.

<!-- b000304 | prose | pages [21] -->
In addition, we put the water temperature as a function of space and time formula (11) into formula (14), temperature gradient satisfy the following relationship. This formula shows that the distribution of the temperature field is essentially the effect of human motion on the temperature gradient:

<!-- b000305 | prose | pages [21] -->
     K 1( ) t 1 f F ( ) K t (15)  k k k

<!-- b000306 | prose | pages [21] -->
f F ( ) Then, consider the form of function . The result of the action of the human k

<!-- b000307 | prose | pages [21] -->
in the bathtub is to promote the mixing of cold water and hot water. Analysis shows that the action is more big, bigger source of forced convection, the influence of water temperature distribution is bigger, but the influence of temperature on forced convection source rate is not increased with the increase of uniform motion.

<!-- b000308 | prose | pages [21] -->
f F ( ) F slow growth, The influence rate first increases with the growth of k k

<!-- b000309 | prose | pages [21, 22] -->
F for the overall flow of water distribution is almost no impact, because too small k F is in this range, the rate of f F ( When k

<!-- b000310 | furniture | pages [22] -->
Team #46830

<!-- b000312 | prose | pages [22] -->
f F Subsequently, the impact rate of

<!-- b000313 | furniture | pages [22] -->
Page 19 of 45

<!-- b000314 | prose | pages [22] -->
) F . is not sensitive to the value of k k

<!-- b000315 | prose | pages [22] -->
( ) F growth, with the rapid growth of k k

<!-- b000316 | prose | pages [22] -->
F and the total amount of water can be compared to the that is, when the value of k

<!-- b000317 | prose | pages [22] -->
F will be sensitive to the value of macro size, the size of k

<!-- b000318 | prose | pages [22] -->
f F ( Finally, the rate of impact of k f F ( ) . k

<!-- b000319 | prose | pages [22] -->
F slow growth, and ) with the growth of k

<!-- b000320 | prose | pages [22] -->
F is large enough, the water can be fully mixed, the closer to 1. Because when the k

<!-- b000321 | prose | pages [22] -->
f F ( ) F continues to increase, the will be very close to 1, but when the value of k k

<!-- b000322 | prose | pages [22] -->
forced convection of the source of the water has been able to fully mixed the role has been very small.

<!-- b000323 | prose | pages [22] -->
f F ( ) F should be shown in the with the change of The influence rate of k

<!-- b000324 | prose | pages [22] -->
following figure: k

<!-- b000325 | caption | pages [22] -->
Figure 9: The variation of convective mixing rate over the forced convection

<!-- b000326 | prose | pages [22] -->
Based on the above analysis, we select the partial large state distribution function

<!-- b000327 | prose | pages [22] -->
f F ( as the approximate analytic formula of

<!-- b000328 | prose | pages [22] -->
 f F ( ) 1 ) : k

<!-- b000329 | prose | pages [22] -->
2    F F a   F   e b

<!-- b000330 | prose | pages [22] -->
F are all the constants to be determined, the units are F and Where, a b 4 m . We

<!-- b000331 | prose | pages [22] -->
will give the decisive factor of the constant through the following analysis.

<!-- b000332 | prose | pages [22] -->
kF  0 F takes the special value, when Consider the case that the special , that k

<!-- b000333 | prose | pages [22, 23] -->
person did not make any action, it is obvious that the water temperature distribution of  f (0) 0 kF , the F  0 , can be solved the impact rate of 0, that is, . When a action is very large or even infinite, the water in the bathtub is fully mixed, the temperature distribution becomes very uniform, the mixing rate is infinitely close to 1, . Note that the equation is established, and the results of the that is lim f F ( ) 1 k  F k model are consistent with the analysis.

<!-- b000334 | furniture | pages [23] -->
Team #46830

<!-- b000335 | furniture | pages [23] -->
Page 20 of 45

<!-- b000337 | prose | pages [23] -->
In particular, when considering the forced convection source value is equal to the half volume of water in the bathtub multiplied by the value of the long side of the 1  bathtub . This formula says bath half water movement from the left half kF V a 0 2 side of the movement to the right side, back into the left half side, the moving distance is 1 1   . This process will make the water in the bathtub more fully mixed, a a a 2 2 because of the forced convection the distribution of temperature becomes more average. In fact, we can determine the influence rate by the test of the variance of the temperature before and after the experiment according to 4.1.3-3 and 4.2.2-2. In this, in order to facilitate the calculation of the subsequent model, we may wish to set

<!-- b000338 | prose | pages [23] -->
1 V a  f ( ) 95%  , which can be obtained . 4 F 0.191378 m 0 a 2

<!-- b000339 | prose | pages [23] -->
Here, we have established a concise and practical mathematical model for the effect of forced convection on human motion:

<!-- b000340 | prose | pages [23] -->
  F S V k k  2    F   F    f F ( ) 1 e  b        T ( , , , ) x y z t T x y z t ( , , , ) f F ( ) T x y z t ( , , , ) T t ( )     k 1 k k 

<!-- b000341 | heading | pages [23] -->
4.3 The human body comfort model

<!-- b000342 | prose | pages [23] -->
In this part, we establish and solve the model of human body's comfortable degree of thermal sensation. This model describes the human body's temperature perception of comfort, the comfort of this gives a quantitative results. In subsequent discussions, the body's temperature perception of comfort will also be used as a part of the bath strategy needs to be taken into account.

<!-- b000343 | heading | pages [23] -->
4.3.1 Establish human body comfort model

<!-- b000344 | prose | pages [23] -->
We have established the human comfort model by using the normal distribution.

<!-- b000345 | prose | pages [23, 24] -->
We consider the human body has a specific optimum bath temperature, when the water temperature is higher than the temperature comfortable degree decline, and gradually feel the heat, even burn; when the water temperature is lower than the temperature of comfort will also decline, people will gradually feel the cold, even suffer from cold.

<!-- b000346 | furniture | pages [24] -->
Team #46830

<!-- b000347 | furniture | pages [24] -->
Page 21 of 45

<!-- b000349 | prose | pages [24] -->
Because the normal distribution is widespread in nature, the unimodal normal distribution are consistent with the perception of comfort temperature In addition, when the temperature exceeds a certain value people will be burned, or temperature below a certain value people will get cold. At this time, the feelings of the people are not comfortable, so comfort should close to zero, the characteristic with normal distribution are in good agreement.

<!-- b000350 | prose | pages [24] -->
Therefore, we choose the normal distribution function to describe the distribution of the body's comfort with temperature, that is, the following expressions:

<!-- b000351 | prose | pages [24] -->
2     T 1 B         e   2

<!-- b000352 | prose | pages [24] -->
Where, represents the most comfortable temperature of human body feeling,

<!-- b000353 | prose | pages [24] -->
represents the standard deviation of the comfortable feeling degree of human body to the temperature.

<!-- b000354 | heading | pages [24] -->
4.3.2 Solution of human body comfort model

<!-- b000355 | prose | pages [24] -->
Taking into account the temperature of the most comfortable temperature in the vicinity of 2 times the standard deviation of the sum of the 95.45%, that is, when the temperature is not within this range, the cumulative amount of satisfaction of the cumulative amount of less than 4.55% of the total amount of comfort.

<!-- b000356 | prose | pages [24] -->
On the other hand, the data show that the human feelings to nociceptive temperature is 306K, human feel hot temperature is 318k, so the temperature outside the scope of this comfort will be very low, outside the scope of the comfortable cumulative value is at a rather low level.

<!-- b000357 | prose | pages [24] -->
May in this range of comfort for the cumulative value of the sum of 95.45%. Doing so for a reason: in statistics normal distribution of twice the standard deviation is often used as to judge whether an event is a small probability event, and in this article, in this article, it is considered that the water temperature above 318K or below 306K is unacceptable therefore can be equated to the small probability events in statistics. So it is reasonable to do so.

<!-- b000358 | prose | pages [24, 25] -->
By the above analysis, we can get the following equations  318   dT  B   306    318 306  318    dT 95.45%  B 306

<!-- b000359 | furniture | pages [25] -->
Team #46830

<!-- b000360 | furniture | pages [25] -->
Page 22 of 45

<!-- b000362 | prose | pages [25] -->
So we get the solution of the model of human body comfort:

<!-- b000363 | prose | pages [25] -->
  2  T 312 1 B     e 9  3 2

<!-- b000364 | prose | pages [25] -->
The above formula shows that the human body to feel the most comfortable temperature is 312K, and by the state distribution characteristics we can know, temperature range in   K the cumulative comfort of total sum of 68.26%, 309 K ,315

<!-- b000365 | prose | pages [25] -->
temperature range in   K total comfort reached 99.7% of the total. So we 303 ,321 K

<!-- b000366 | prose | pages [25] -->
think that when the temperature is above 321K or below 303K is completely unacceptable, people will be burned or cold due to these temperatures.

<!-- b000367 | prose | pages [25] -->
In comparison with literature data, we found that the burn the body temperature of 47 degrees Celsius (320K) ,the relative error of the scald temperature predicted by the human body comfort model we have established is only

<!-- b000368 | prose | pages [25] -->
 320 K 321 K   100% 0.3125% , indicating that the model coincide with the actual 320 K

<!-- b000369 | prose | pages [25] -->
situation very well.

<!-- b000370 | heading | pages [25] -->
4.4 Optimized control model of bathing strategy

<!-- b000371 | prose | pages [25] -->
In this section, based on the models we established previously, we get the optimized control model of bathing strategy.

<!-- b000372 | prose | pages [25] -->
We note that the water temperature is reduced when users are in the bath, then they open the hot water faucet to heat the water. We need to develop a water injection scheme, to make the temperature of the water temperature maintained at a level which is close to the initial water temperature and won't get water temperature too high to decline the comfort of users or even hurt. Thus, we propose two kinds of injection scheme towards two different controlling ways:

<!-- b000373 | prose | pages [25] -->
1. Control artificially to make the water in the bathtub maintain a long-term comfortable temperature and hope that the operation is simple, so keep the tap a trickle.

<!-- b000374 | prose | pages [25, 26] -->
2. Control automatically. When the sensor accept the signal that the water temperature is reduced to a certain critical temperature, the tap is automatically controlled to the maximum. When water temperature is picked up to a certain value, the faucet is turned off. The tap repeated this cycle before the end.

<!-- b000375 | furniture | pages [26] -->
Team #46830

<!-- b000376 | furniture | pages [26] -->
Page 23 of 45

<!-- b000378 | heading | pages [26] -->
4.4.1 Strategy I

<!-- b000379 | prose | pages [26] -->
Constant flooding strategy: After users have entered the tub bath, the flow rate

<!-- b000380 | prose | pages [26] -->
bT  to maintain the bk which has a certain temperature of always keep constant in

<!-- b000381 | prose | pages [26] -->
bath tub water temperature. This strategy makes it easy to operate, suitable for ordinary hot water supply system which needs manual operation, and the parameters bT . So this plan has considerable practical reference bk and to be optimized only be

<!-- b000382 | prose | pages [26] -->
value for manual operation.

<!-- b000383 | prose | pages [26] -->
Now we need to optimize the strategy’s variable, to find the optimal water flow

<!-- b000384 | prose | pages [26] -->
bT . bk and temperature of hot water injection

<!-- b000385 | prose | pages [26] -->
First, we show the optimization objective function. In view of the user who wishes to make water temperature when he get into the bath as close to the l temperature of he has taking the shower, which can be abstracted to a mathematical expression, make the average difference of initial temperature and the average temperature in period of time to be least, which can b show in the following expression.

<!-- b000386 | prose | pages [26] -->
  t   m T T t dt ( )   0 0 min t m In addition, users do not want to waste too much water just for maintaining the water temperature, so the user will control the flow of water injection so that the waste water will be controlled, which can be abstracted in mathematical expression of the minimum of flow rate, the expression is as follows:

<!-- b000387 | prose | pages [26] -->
min bk

<!-- b000388 | prose | pages [26] -->
In view of the added hot water temperature cannot be too high. As the high temperature is likely to affect user’s comfort, even scald users, so it’s necessary to consider the impact of hot water to the user's comfort. Clearly, in our optimization strategy, it should be ensure the comfort get a maximum under certain conditions, the expression is as follows:

<!-- b000389 | prose | pages [26] -->
  2  T 312 1 B     max e 9  3 2

<!-- b000390 | prose | pages [26, 27] -->
Considering the above three factors, we get the final optimization objective function:

<!-- b000391 | furniture | pages [27] -->
Team #46830

<!-- b000392 | furniture | pages [27] -->
Page 24 of 45

<!-- b000394 | prose | pages [27] -->
  t   m T T t dt ( )   2  T 312 1   B  0 0          min k t e 9 1 2 b m 3  t 3 2 m 1, , 3 is the weight of temperature factor, water factor and comfort Where 2

<!-- b000395 | prose | pages [27] -->
factor respectively, whose value can be determined by the user's preferences. Symbol on the third function is negative because we have done a minimization process in three factors, which means the smaller value the more excellent program.

<!-- b000396 | prose | pages [27] -->
Second, we give the optimization constraints. Considering the hot water faucet has a maximum of flow rate, we get the first constraint:

<!-- b000397 | prose | pages [27] -->
  0 bk k max

<!-- b000398 | prose | pages [27] -->
The temperature of injection water should be higher than the user's body temperature clearly. Otherwise users will dissipate heat in the water and feel cold. In addition, the temperature of boiling water which poured to should not make the user burn. As the second constraint:

<!-- b000399 | prose | pages [27] -->
   T T T body b highest

<!-- b000400 | prose | pages [27] -->
Next we consider the constraints associated with the temperature, make the relationship between the average temperature and internal energy to be a third constraint:

<!-- b000401 | prose | pages [27] -->
Q  T t ( )  c V 0

<!-- b000402 | prose | pages [27] -->
The changes of the water temperature and the distribution of water is controlled by the universal thermodynamic model formula (13). Because of space limitations we just give the water heat differential equation here:

<!-- b000403 | prose | pages [27] -->
      dQ dQ dQ dQ dQ dQ dQ   exchange evaporation body radiation water water

<!-- b000404 | prose | pages [27] -->
Moreover, it should also consider the user’s normal bathing time, based on the life knowledge we take the longest bath time for 30 minutes, so we obtain a fifth constraint:

<!-- b000405 | prose | pages [27] -->
 mt 1800 s

<!-- b000406 | prose | pages [27] -->
To sum up, we have established the optimal control model of a strategy 1 :

<!-- b000407 | furniture | pages [28] -->
Team #46830

<!-- b000408 | furniture | pages [28] -->
Page 25 of 45

<!-- b000409 | prose | pages [28] -->
  t   m T T t dt ( )   2  T 312 1   B  0 0          min k t e 9 1 2 b m 3  t 3 2 m   0 k k b max     T T T  body b highest  Q  s t T t . . ( )   c V  0        dQ dQ dQ dQ dQ dQ dQ    exchange evaporation body radiation water water   t 1800 s m

<!-- b000410 | heading | pages [28] -->
4.4.2 Strategy II

<!-- b000411 | prose | pages [28] -->
Temperature switch strategy: When the minimum temperature in the bath is

<!-- b000412 | prose | pages [28] -->
bT  is injected into T reduced to a critical value , the hot water with the temperature min1

<!-- b000413 | prose | pages [28] -->
T the tub. When the minimum temperature in tub inclines to a certain value of , min 2

<!-- b000414 | prose | pages [28] -->
the water injection stops. The tap switch repeated this cycle before the end. This strategy is based on the consideration of automation control, and the strategy essentially is a self-regulation of the hot water supply system towards the change of temperature in. The system can rely on the temperature sensor to accurately identify the current water temperature, and control the tap frequently to switch, so as to control the water temperature carefully. Thus the scheme is practical and meaningful.

<!-- b000415 | prose | pages [28] -->
Then we need to optimize the variate of the strategy and search the critical value bT . T T of the temperature switch and the temperature of the injection water 、min 2 min1

<!-- b000416 | prose | pages [28] -->
First, we propose the optimized objective function. Because the process is piecewise continuous, the temperature changes according to 2 different functions after opening and closing the switch. Then, the optimized objective function should also be piecewise continuous. Moreover, we note that users hope water temperature as close as possible to the initial temperature, then abstract the equation so as to render the mean value of the difference between the initial water temperature and the average water temperature at a certain time is minimum. The expression is as follows:

<!-- b000417 | prose | pages [28] -->
n    t   i 1 T T t dt ( )   0 t i  i 1 min n  t i  i 1

<!-- b000418 | prose | pages [28, 29] -->
Here, is for the 2 different equations at the situation after the opening and closing of the switch.

<!-- b000419 | furniture | pages [29] -->
Team #46830

<!-- b000420 | furniture | pages [29] -->
Page 26 of 45

<!-- b000422 | prose | pages [29] -->
To save water as much as possible, while the flow is a constant and the water consumption is in direct proportion to the time of the tap opening. If the first time to

<!-- b000423 | prose | pages [29] -->
 1t , then every interval of injection is t t open the tap is . Here comes our  2 k 2 k 1

<!-- b000424 | prose | pages [29] -->
following objective functions:

<!-- b000425 | prose | pages [29] -->
 n 1   2     min t t  2 k 2 k 1  k 1

<!-- b000426 | prose | pages [29] -->
 n , n means the number of the tap n Where, means the integral part of  2  2

<!-- b000427 | prose | pages [29] -->
operations.

<!-- b000428 | prose | pages [29] -->
In addition, we consider that the comfort level should be maximum under certain conditions. Here comes the following expression:

<!-- b000429 | prose | pages [29] -->
Considering three factors above comprehensively, we get the optimization objective function similar to strategy two:

<!-- b000430 | prose | pages [29] -->
n    t   n  i 1 T T t dt ( ) 1   2     T 312 0  2 1 B  t       i           i 1 min t t e 9  2 2 2 k 2 k 1 3 n  3 2   k 1 t i  i 1

<!-- b000431 | prose | pages [29] -->
Second, we propose the constraint conditions of optimization. Obviously, the temperature of the injection water should be higher than the user’s temperature. In addition, the injection water can’t scald the user. Moreover, the lower critical value

<!-- b000432 | prose | pages [29] -->
T T aren’t supposed to exceed the higher one which should be lower than min1 min 2

<!-- b000433 | prose | pages [29] -->
bT . Or the higher critical value is impossible to the temperature of the injection water

<!-- b000434 | prose | pages [29] -->
reach. Here comes the first constraint condition:

<!-- b000435 | prose | pages [29] -->
    T T T T T body min1 min2 b highest

<!-- b000436 | prose | pages [29] -->
The second constraint condition is the relationship between the average temperature and the internal energy:

<!-- b000437 | prose | pages [29] -->
Q  T t ( )  c V 0

<!-- b000438 | prose | pages [29] -->
Finally, the water temperature change and distribution are controlled by the universal thermodynamic model of water (Eq. 4.1.4-1). However, the differential equation after the opening and closing of the switch is quite different. To unify the

<!-- b000439 | prose | pages [29] -->
expression of these two processes, we set a 0-1 variable .

<!-- b000440 | furniture | pages [30] -->
Team #46830

<!-- b000441 | furniture | pages [30] -->
Page 27 of 45

<!-- b000442 | prose | pages [30] -->
     1 k 2 q 1    0 k 2 q 

<!-- b000443 | prose | pages [30] -->
 n   q 1,2,3, , 1 Where, , it means that when the number of operation is odd,   2

<!-- b000444 | prose | pages [30] -->
, or conversely,  0 1 the tap is open and . So we can unify the temperature of

<!-- b000445 | prose | pages [30] -->
the hot water injection and natural cooling process in the following form:

<!-- b000446 | prose | pages [30] -->
         dQ dQ dQ dQ dQ dQ dQ   exchange evaporation body radiation water water

<!-- b000447 | prose | pages [30] -->
To sum up, the optimal control model of strategy II is as follows:

<!-- b000448 | prose | pages [30] -->
n    t   n  i 1 T T t dt ( ) 1   2     T 312 0  2 1 B  t       i           i 1 min t t e 9  2 2 2 k 2 k 1 3 n  3 2   t k 1 i  i 1      T T T T T body min1 min2 b highest  Q   T t ( )   c V 0 s t . .      1 k 2 q 1      0 k 2 q            dQ dQ dQ dQ dQ d Q dQ    exchange evaporation body radiation water water

<!-- b000449 | heading | pages [30] -->
4.4.3 Solution of the optimal control models of strategy I & II

<!-- b000450 | prose | pages [30] -->
In this section, we solve the optimal control models of strategy I & II by Matlab.

<!-- b000451 | prose | pages [30] -->
I. Algorithm flow For optimal control model, we adopt enumeration method to solve its optimal solution, and transform all partial differential equations and differential equations [3]which are nested inside model to difference equations and solve them. Algorithm flow charts of strategy 1 and strategy 2 are as follow:

<!-- b000452 | furniture | pages [31] -->
Team #46830

<!-- b000453 | furniture | pages [31] -->
Page 28 of 45

<!-- b000454 | prose | pages [31] -->
Strategy2 Strategy1

<!-- b000455 | prose | pages [31] -->
Initialize variables Initialize variables

<!-- b000456 | prose | pages [31] -->
N While Tb<the highest N While sum<1800 water temperature (30 minutes) Y Y Output The Tb+beta_k optimal result Dispersed the Output the average interval within the temperature(the water in range of 0 to 1800 the bathtub)-time Solve Ts;

<!-- b000457 | prose | pages [31] -->
relationship curve Tmin1,Tmin2 initialization Solve temperature increment N (negative)beta_k While Tmin1<Ts

<!-- b000458 | prose | pages [31] -->
Y Tnext=Tk+beta_k Tmin1+beta_k

<!-- b000459 | prose | pages [31] -->
N While Tmin2<Ts sum=sum+beta_t Y Tmin2+beta_k

<!-- b000460 | prose | pages [31] -->
Finding the optimal temperature of adding water/draining

<!-- b000461 | caption | pages [31] -->
Figure 10: Algorithm flow charts

<!-- b000462 | prose | pages [31] -->
II. Result of optimal control model of strategy 1 We get optimal parameter under the strategy 1 through programming the above program in MATLAB software:

<!-- b000463 | prose | pages [31] -->
    1 k 0.007 L s  b  T 311.1 K  b

<!-- b000464 | prose | pages [31] -->
We also get the change curve of water average temperature T t during user bathing ( )

<!-- b000465 | prose | pages [31] -->
when in optimal parameter, as shown in the graph.

<!-- b000466 | furniture | pages [32] -->
Team #46830

<!-- b000467 | furniture | pages [32] -->
Page 29 of 45

<!-- b000468 | caption | pages [32] -->
Figure 11: The change curve of water average temperature

<!-- b000469 | prose | pages [32] -->
In the graph, the red curve is the temperature curve of normal hot water under condition of optimal strategy, the blue curve is the natural cooling curve of normal water. We can find directly the cooling speed under optimal parameter is lower than natural cooling curve. Then we explain quantitatively the validity of our model through several data.

<!-- b000470 | caption | pages [32] -->
Table 3: Average temperature data

<!-- b000471 | prose | pages [32] -->
T       t 300 600 900 1200 1500 1800

<!-- b000472 | prose | pages [32] -->
316.0650 315.1926 3143814 313.6271 312.9256 312.2413 T optimize( ) t 315.9266 314.9203 313.9801 313.1016 312.2809 311.5501 t T ( ) nature Through the calculation we can get extra water requirement in strategy is

<!-- b000473 | prose | pages [32] -->
    1 0.007 L s 1800 s 12.6 L , the ratio between extra water requirement and bathing

<!-- b000474 | prose | pages [32] -->
water requirement is:

<!-- b000475 | prose | pages [32] -->
12.6 L 12.6     100% 100% 2.84% V 443.4 0

<!-- b000476 | prose | pages [32] -->
After applying optimal strategy I, the temperature decrease to 4.76℃from5.45℃,

<!-- b000477 | prose | pages [32] -->
 5.45 4.76   100% 12.66% 5.45

<!-- b000478 | prose | pages [32, 33] -->
As for comfort level aspect, the most comfortable water temperature satisfaction rate is ：       2 2    311.1 312 312 312 311.1       100% e 100% 91.39% 9 9    312 To sum up, based on our optimal control model for water injection, we merely need 2.84% extra hot water to get a 12.66% optimization effect in temperature variation and 91.39% of the most comfortable water temperature satisfaction rate. These results shows that our model and strategy are of great effectiveness and practical reference value.

<!-- b000479 | furniture | pages [33] -->
Team #46830

<!-- b000480 | furniture | pages [33] -->
Page 30 of 45

<!-- b000482 | prose | pages [33] -->
In addition, according to the forced convection model and the distribution model of temperature in space, we can get the data of the water temperature in time and space at any moment when bathing. According to assumption 12 combined with

<!-- b000483 | prose | pages [33] -->
f F ,we get the distribution of water ( ) Eq.4.1.3-2 &4.2.2-2 and the definition of

<!-- b000484 | prose | pages [33] -->
temperature in the tub at any moment when bathing:

<!-- b000485 | prose | pages [33] -->
2   F     f t 1    0 F     T x y z t ( , , , ) T t ( ) e K 0 y (15) b

<!-- b000486 | prose | pages [33] -->
 Here, we assume human action frequency f 1 Hz 0

<!-- b000487 | prose | pages [33] -->
Human motion range is 0.5m,the volume of the moving parts is 1/10 of the volume of the body, which is 6L. Thus we get the forced convection of human motion      3 3 3 4 F 0.5 m 6 10 m 3 10 m

<!-- b000488 | prose | pages [33] -->
 4 , which is mentioned at the end of 4.2.2 bF 0.191378 m

<!-- b000489 | prose | pages [33] -->
 is the temperature gradient at the beginning of the hot water injection. We K 0

<!-- b000490 | prose | pages [33] -->
  might as well set it the value of 2.5s, then K 0 4.294

<!-- b000491 | prose | pages [33] -->
Take these data into formula (15) , we have:

<!-- b000492 | prose | pages [33] -->
   4    2.45731 10 t 1   T x y z t ( , , , ) T t ( ) 4.294 e y

<!-- b000493 | prose | pages [33] -->
Where, T t is determined Fig11. ( )

<!-- b000494 | prose | pages [33] -->
III. Result of optimal control model of strategy II We get optimal parameter under the strategy II through programming the above program in MATLAB software:

<!-- b000495 | prose | pages [33] -->
  T 311.7 K min1   T 311.7 K  min2   T 313.1 K  b

<!-- b000496 | prose | pages [33] -->
 T T Amazingly, we get the result . Then we discuss deeply in the min1 min2

<!-- b000497 | prose | pages [33] -->
following aspects:

<!-- b000498 | prose | pages [33, 34] -->
1. In this strategy, the upper and lower two critical temperatures are equal. In strategy 2, the best solution is that the time of turning the tap on and off is infinitely small. Thus degenerate to a continuous process in macroscopic.

<!-- b000499 | furniture | pages [34] -->
Team #46830

<!-- b000500 | furniture | pages [34] -->
Page 31 of 45

<!-- b000502 | prose | pages [34] -->
 T T 1. In this strategy, means that every discrete process is infinitely min1 min2

<!-- b000503 | prose | pages [34] -->
small, every interval between the tap opening and closing is infinitely small, so it degenerates to a continuous process.

<!-- b000504 | prose | pages [34] -->
2. Because we use the difference equation to replace the differential equation, the accuracy of the differential equation is not enough, otherwise we can solve this approximation in the continuous process of opening and closing the tap of the time ratio for further, and calculate the flow rate of the continuous addition of water. Because the model is a three-dimensional optimization with huge calculation. If Cyclic step is shorter in the difference equation, the calculation will increase in geometric progression. With the limitation of our computers, we can’t analyze more deeply.

<!-- b000505 | prose | pages [34] -->
3. The optimal solution of strategy II is a continuous process of injection, however, the results are totally different with those of strategy I. Here is our guess: Although we set additional water consumption, temperature deviation, and comfort for the two strategies for the same weight, with different standardized ways of each factor, the results vary a lot.

<!-- b000506 | heading | pages [34] -->
4.5 Bubble bath

<!-- b000507 | prose | pages [34] -->
In this section, we get the universal thermodynamic model of bubble [4] water by modifying that of normal hot water , and get the effect of bubble water on optimal control strategy through the previous optimal control strategy.

<!-- b000508 | heading | pages [34] -->
4.5.1 The effect of bubble water

<!-- b000509 | prose | pages [34] -->
Bubble water has an impact on the thermodynamic process of the bathtub system, mainly because the bubble water has some different physical parameters and it brings a layer of air bubbles on the surface of the water. This bubble will reduce the evaporation rate of water and will reduce the heat exchange power of water surface and air [11[]12].

<!-- b000510 | prose | pages [34] -->
As for the similarities and differences between bubble water and normal water i. Their density and specific heat capacity are slightly different. However the concentration of bubble water is low, so we can ignore this difference.

<!-- b000511 | prose | pages [34] -->
ii. The surface tension of bubble water can be 1.3-2.2 times of the tension of distilled water due to its different concentration. As we all know, the large surface tension reduces the escape rate of the molecules on the surface.

<!-- b000512 | prose | pages [34, 35] -->
iii. bubble water brings a layer of air bubbles on the surface of the water, which is equivalent to add a thick layer of air insulation to the water in the bath and effectively prevent the evaporation of water at the same time.

<!-- b000513 | furniture | pages [35] -->
Team #46830

<!-- b000514 | furniture | pages [35] -->
Page 32 of 45

<!-- b000516 | prose | pages [35] -->
dQ In a word, should be deleted from the heat differential equation of evaporation

<!-- b000517 | prose | pages [35] -->
bubble water, because the bubble layer and its large surface tension coefficient can

<!-- b000518 | prose | pages [35] -->
dQ reduce the evaporation capacity in the tub greatly, is inevitable to decline. evaporation

<!-- b000519 | prose | pages [35] -->
dQ Additionally, in the part of the heat conduction with the air will also be exchange

<!-- b000520 | prose | pages [35] -->
modified. Because the water doesn’t contact with air directly. Instead, the heat exchanges with the outside air through the bubble layer.

<!-- b000521 | prose | pages [35] -->
Considering these factors and formula (4) and formula (13), the expression after modifying the heat transfer between water and air is as follows:

<!-- b000522 | prose | pages [35] -->
                dQ h T t ( ) T ab 2 aH 2 bH T t ( ) T ab dt       exchange 0 0 d   air

<!-- b000523 | prose | pages [35] -->
Add the two amendments to the differential equation of heat. We have:

<!-- b000524 | prose | pages [35] -->
      dQ dQ dQ dQ dQ dQ   exchange body radiation water water

<!-- b000525 | prose | pages [35] -->
After taking the expression above into formula (13), we get the universal thermodynamic model of bubble water.

<!-- b000526 | prose | pages [35] -->
Here we don’t solve the model. Instead, we contrast the natural heat dissipation power of the bubble water in the body's most comfortable temperature with the natural heat dissipation power of the normal hot water in this case, assuming the thickness of the bubble layer as 3cm.

<!-- b000527 | prose | pages [35] -->
     dQ dQ dQ dQ dQ exchange body radiation evaporation    W 6710.88 W water dt dt

<!-- b000528 | prose | pages [35] -->
    dQ dQ dQ dQ exchange body radiation    W 3076.92 W bubble dt dt

<!-- b000529 | prose | pages [35] -->
Then we draw the conclusion that the heat dissipating power of bubble water in the tub is 45.85% of the original power, which shows that bubble water has good thermal insulation property. The improvement is because the air bubble layer separates the direct convective heat exchange between the air and the water surface. Heat transfer becomes based on Fourier’s law only.

<!-- b000530 | heading | pages [35] -->
4.5.2 Effect of bubble water on optimal control strategy

<!-- b000531 | prose | pages [35] -->
We take the universal thermodynamic model into optimal control strategy and solve it by Matlab:

<!-- b000532 | furniture | pages [36] -->
Team #46830

<!-- b000533 | furniture | pages [36] -->
Page 33 of 45

<!-- b000534 | prose | pages [36] -->
    1 k 0.004 L s  b  T 311.9 K  b

<!-- b000535 | prose | pages [36] -->
As is shown in Figure 12, the green curve is the curve of the temperature change over time under the conditions of the optimal strategy I, the red curve is the temperature curve of normal hot water under the condition of the optimal strategy I, the blue curve is the natural heat dissipating curve of normal water. The figure tells us that bubble water has the excellent performance in thermal insulation, if combined with the optimal control strategy, it can effectively keep the water warm in the bathtub.

<!-- b000536 | caption | pages [36] -->
Figure 12: Curves of temperature

<!-- b000537 | prose | pages [36] -->
If we replace normal water with bubble water in the tub, the optimal solution of

<!-- b000538 | prose | pages [36] -->
    1 0.004 L s 1800 s 7.2 L our model is which is 57.14% of the normal water.

<!-- b000539 | prose | pages [36] -->
In addition, 311.9K brings users a higher comfort level. Temperature change in bath

<!-- b000540 | prose | pages [36] -->
tub declines from approximately 5.54℃ to no more than 2.91℃, the optimization rate reaches 47.47%.

<!-- b000541 | prose | pages [36] -->
To sum up, water bubble bath combined with a scientific way of injection can very effectively keep the water warm. The result is of practical reference value and provide a good theoretical model for the industry of hot spring, indoor swimming pool and so on.

<!-- b000542 | furniture | pages [37] -->
Team #46830

<!-- b000543 | furniture | pages [37] -->
Page 34 of 45

<!-- b000544 | heading | pages [37] -->
5    Testing the Model

<!-- b000545 | heading | pages [37] -->
5.1 Error Analysis

<!-- b000546 | prose | pages [37] -->
In this part, we will analyze the factors that may cause the error of the solution. Many factors will influence the bath water temperature, including the outside environment factors(such as air temperature and humidity, air flow rate), the water itself (such as waves, drop, natural heat convection), human (do work, metabolic heat production). In addition to the influencing factors, the approximation and fitting used in the model building process, as well as the algorithm in the solving process. It will also bring errors.

<!-- b000547 | heading | pages [37] -->
5.1.1 Various factors of external environment

<!-- b000548 | prose | pages [37] -->
I. Air temperature and humidity In fact, in such a relatively closed bathroom, air humidity will rise with the evaporation of the water in the bathtub. The heat caused by the evaporation of water vapor increases the temperature of the air. But the temperature and humidity of the air in the bathroom is not uniform, and the influence of water on the air is difficult to be given by simple ordinary differential equations, which makes the error difficult to get the numerical value.

<!-- b000549 | prose | pages [37] -->
But after analysis, we know that the rise of air humidity inhibits the evaporation rate of water vapor, at the same time, the air temperature rise will reduce the difference in temperature between air and water, and then inhibits water heat exchange of air. In assumption 1 we ignore the change of air temperature and humidity. So without considering other cases, according to the results of the model, water cooling slightly faster than the actual, it means that the error of a value is above zero.

<!-- b000550 | prose | pages [37] -->
II. Air flow Compared with the change of air temperature and humidity, air flow's influence on the water temperature should be much smaller. Because the bathroom is relatively closed, in addition to the exhaust fan, there are no air source and sink. Since there is no air source and sink, the air flow in the bathroom is very small.

<!-- b000551 | prose | pages [37] -->
But as a part of the error, we need to analyze the air flow. Refer to the above discussion of the temperature and humidity, we know that the air flow inhibits water cooling. So without considering other cases, according to the results of the model, water cooling slightly faster than the actual, it means that the error of a value is above zero.

<!-- b000552 | furniture | pages [38] -->
Team #46830

<!-- b000553 | furniture | pages [38] -->
Page 35 of 45

<!-- b000554 | heading | pages [38] -->
5.1.2 Various factors of water

<!-- b000555 | prose | pages [38] -->
I. Waves As a result of the movement of water injection or motions of human, the water must generate waves. Waves will increase the surface contact area of water and air, thus cooling speed up. On the other hand, waves will lead to the overflow under full water condition, and take away the heat. In fact the overflow is a very considerable value, it take away heat is relatively large, and the heat it takes away is also quite large. But according to assumption 2, we ignore the impact. So without considering other cases, according to the results of the model, water cooling slightly slower than the actual, it means that the error of a value is less than zero.

<!-- b000556 | prose | pages [38] -->
II. Water drop process Loss of heat will occurred in the dropping process of water. When it reaches the surface of the water, the temperature will be slightly lower than the outlet water temperature. That means

<!-- b000557 | prose | pages [38] -->
0T  is slightly larger than the actual value, the error of a value is above zero. the value of

<!-- b000558 | prose | pages [38] -->
III. Natural heat convection Natural heat convection is generated by the temperature gradient, and the result is necessarily reduce the absolute value of the temperature gradient. That means the  K t is slightly larger than the actual value, the error of a value is above value of

<!-- b000559 | prose | pages [38] -->
zero.

<!-- b000560 | heading | pages [38] -->
5.1.3 Various factors of human

<!-- b000561 | prose | pages [38] -->
I. Human work to water Human work to water, part of this energy change into the kinetic energy of the water flow, another part change into heat in the form of viscous resistance. This factor is actually a small heat source. That means the heat dissipation of water is slightly slower than the actual value, the error of a value is less than zero.

<!-- b000562 | prose | pages [38] -->
II. Metabolic heat production When the water temperature is lower than the body temperature, the body can be regarded as an independent heat source. So according to the results of the model, water cooling slightly slower than the actual, it means that the error of a value is less than zero.

<!-- b000563 | heading | pages [38] -->
5.1.4 Error in modeling and solving process

<!-- b000564 | prose | pages [38, 39] -->
I. Error of plane fitting to temperature distribution surface Because the analytic form of the curved surface is unknown, we can’t evaluate the error  T t . But we can get the average value of some points on the surface, caused by this fitting to

<!-- b000565 | furniture | pages [39] -->
Team #46830

<!-- b000566 | furniture | pages [39] -->
Page 36 of 45

<!-- b000568 | prose | pages [39] -->
then get the error by compared the average value with  T t .

<!-- b000569 | prose | pages [39] -->
II. Error of the step size of the algorithm We use enumeration method to solve the optimization model. In strategy one, the step size

<!-- b000570 | prose | pages [39] -->
bT  is 0.1. In the optimal strategy we get, the error of bk is 0.001, the step size of bk of

<!-- b000571 | prose | pages [39] -->
bT should be half of the step size, as shown in the following formula and

<!-- b000572 | prose | pages [39] -->
       1 k 0.0070 0.0005 L s  b    T 311.10 0.05 K  b

<!-- b000573 | heading | pages [39] -->
5.2 Sensitivity Analysis

<!-- b000574 | prose | pages [39] -->
Some inputs of our model may be hard to obtain or there may be some deviation in our inputs. So it's possible that these kinds of situation will influence the solution of our model. To understand the situations above, we implement a sensitivity analysis to test the robustness of our model. The analysis results show that our model does not exhibit a chaotic behavior and show good sensitivity.

<!-- b000575 | prose | pages [39] -->
Our sensitivity analysis will be based on factor variation method, in order to see how the result of the model changes when the input parameters change. We will analyze the following parameters:

<!-- b000576 | prose | pages [39] -->
1. The shape and volume of the tub 2. Human's volume, surface area, comfortable temperature and the motion in the tub, etc.

<!-- b000577 | prose | pages [39] -->
3. Heat transfer rate We have obtained the optimal solution of the model. We will use this as a contrast to do sensitivity analysis. The parameters of the optimal solution are set as follows:

<!-- b000578 | prose | pages [39] -->
   H 0.49 m a 1.3 m b 0.8 m 1. The height of the tub , length , width

<!-- b000579 | prose | pages [39] -->
  2 h 42.8 W m k 2. The heat transfer rate of tub

<!-- b000580 | prose | pages [39] -->
2 S =1.9 m 3. Body surface area

<!-- b000581 | prose | pages [39] -->
  2 4. The heat transfer rate of water h 166 W m k water

<!-- b000582 | prose | pages [39] -->
 k 0.007 L s By these parameters, the solution is that，the rate of flow ，the outlet water

<!-- b000583 | prose | pages [39, 40] -->
 T 311.1 k temperature ,water consumption is 12.6 Liters(Assume that bath time is 30 0 minutes).It is the optimal bathing strategy with the least amount of water.

<!-- b000584 | furniture | pages [40] -->
Team #46830

<!-- b000585 | furniture | pages [40] -->
Page 37 of 45

<!-- b000587 | heading | pages [40] -->
5.2.1 Sensitivity to the shape and volume of the tub

<!-- b000588 | prose | pages [40] -->
Change the shape and volume of the tub, observe the influence of the changes of each factor on the optimal bathing strategy. The sensitivity of the shape and volume of the tub by calculation is obtained, as shown in the following tables.

<!-- b000589 | caption | pages [40] -->
Table 4: Sensitivity of the shape and volume of the tub (for water consumption)

<!-- b000590 | prose | pages [40] -->
-5% -3% -1% 0 1% 3% 5% a -85.71% -57.14% -42.86% 0% 0% 28.57% 57.14% b -57.14% -57.14% -42.86% 0% 0% 14.29% 28.57% H -42.86% -28.57% -28.57% 0% -14.29% 0% 0% h -42.86% -42.86% -28.57% 0% -14.29% 0% 0%

<!-- b000591 | caption | pages [40] -->
Table 5: Sensitivity of the shape and volume of the tub (for water temperature)

<!-- b000592 | prose | pages [40] -->
-5% -3% -1% 0 1% 3% 5% a -0.03% -0.03% -0.03% 0% 0% 0% 0% b -0.03% -0.03% -0.03% 0% 0% 0% 0% H -0.03% -0.03% -0.03% 0% 0% 0% 0% h -0.03% -0.03% -0.03% 0% 0% 0% 0% We can see that the water consumption is very sensitive to the parameters of the shape  and volume of the tub in the context of 5% . It proves that the model we established is suitable for various shapes and volumes of the tub.

<!-- b000593 | prose | pages [40] -->
On the other hand, the water temperature is not very sensitive to the parameters of the shape and volume of the tub. But we can understand that the outlet temperature had great  changes in the context of 1% by analysis the data. That is to say, the temperature can not change too much，this shows that our model takes the person's comfort level into account, the model can produce good results.

<!-- b000594 | heading | pages [40] -->
5.2.2 Sensitivity to the human parameters

<!-- b000595 | prose | pages [40] -->
In the process of building model, some influencing factors of the optimal solution like body surface area varies from person to person. That cause changes in the optimal strategy. Take human body surface area as an example, and observe the effect on optimal bathing strategy. Sensitivity of the human parameters was obtained by calculating, as shown in the following two tables.

<!-- b000596 | furniture | pages [41] -->
Team #46830

<!-- b000597 | furniture | pages [41] -->
Page 38 of 45

<!-- b000598 | caption | pages [41] -->
Table 6: Sensitivity of the human parameters (for water consumption)

<!-- b000599 | prose | pages [41] -->
-5% -3% -1% 0 1% 3% 5% S 28.57% 14.29% 0% 0% -42.86% -57.14% -71.43%

<!-- b000600 | caption | pages [41] -->
Table 7: Sensitivity of the human parameters (for water temperature)

<!-- b000601 | prose | pages [41] -->
-5% -3% -1% 0 1% 3% 5% S 0% 0% 0% 0% -0.03% -0.03% -0.03% We can see that the water consumption is very sensitive to the human parameters in the  context of 5% . It proves that the model we established is suitable for people of various sizes.

<!-- b000602 | heading | pages [41] -->
5.2.3 Sensitivity to the heat transfer rate

<!-- b000603 | prose | pages [41] -->
Observation the influence of heat transfer rate on the optimal bathing strategy. Change the heat transfer rate, then taps out the sensitivity of the heat transfer rate, as shown in the following two tables.

<!-- b000604 | caption | pages [41] -->
Table 8: Sensitivity of the heat transfer rate (for water consumption)

<!-- b000605 | prose | pages [41] -->
-5% -3% -1% 0 1% 3% 5% 28.57% 14.29% 14.29% 0% -42.86% -57.14% -71.43% h water

<!-- b000606 | caption | pages [41] -->
Table 9: Sensitivity of the heat transfer rate (for water temperature)

<!-- b000607 | prose | pages [41] -->
-5% -3% -1% 0 1% 3% 5% -0.03% -0.03% 0.03% 0% 0% 0% 0% h water

<!-- b000608 | prose | pages [41] -->
We can see that the water consumption is very sensitive to the heat transfer rate  in the context of 5% . It proves that no matter how much the effect of thermal conductivity made by bubble bath, the model we established is suitable.

<!-- b000609 | heading | pages [41] -->
6    Conclusions

<!-- b000610 | heading | pages [41] -->
6.1 Strengths and Weaknesses

<!-- b000611 | heading | pages [41] -->
6.1.1 Strengths

<!-- b000612 | prose | pages [41, 42] -->
I. This model considers all the ways of heat flow, that is, heat conduction, convection and heat radiation, and the mathematical physics of the model is improved.

<!-- b000613 | furniture | pages [42] -->
Team #46830

<!-- b000614 | furniture | pages [42] -->
Page 39 of 45

<!-- b000616 | prose | pages [42] -->
II. This model includes a large number of parameters. These parameters include the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub, and the motions made by the person in the bathtub, they have great practical value and a wide range of application III. The model is fit for the complex problem of the space distribution of temperature and convection. These fitting and approximation greatly reduce the difficulty of solving the model, and can get the results agree well with the real situation IV. This model also takes into account the user's bath feeling, and further improve the guiding significance of the model in the reality. In addition, according to this model, the effect of the optimal strategy has been obtained is obvious.

<!-- b000617 | prose | pages [42] -->
V. For the error analysis and sensitivity of the model, we discuss each parameter. Sensitivity analysis results show that our model parameters have a wide range of application.

<!-- b000618 | prose | pages [42] -->
 F S V VI. The forced convection is introduced into the model（ ）to describe k k

<!-- b000619 | prose | pages [42] -->
the strength of human motions, and a complete explanation on the principle and influence are given. It is highly innovative.

<!-- b000620 | heading | pages [42] -->
6.1.2 Weaknesses

<!-- b000621 | prose | pages [42] -->
I. This model takes into account too much factors, causing the solving process is tedious and the way to solve is difficult.

<!-- b000622 | prose | pages [42] -->
F in forced convection model）still II. One of the model parameters（Variable b

<!-- b000623 | prose | pages [42] -->
needs to be determined by experiment, and it cannot be deduced from the existing physical constants.

<!-- b000624 | prose | pages [42] -->
III. In this paper, the solution of the model is limited to the capacity of the computer, and it can't achieve higher accuracy。

<!-- b000625 | heading | pages [42] -->
6.2 Comprehensive Results

<!-- b000626 | prose | pages [42] -->
I. Results of optimal control strategy The result derived by solving an optimal solution is: when the flow of continuous

<!-- b000627 | prose | pages [42] -->
 L s   bT 311.1 K 1 injection of hot water is bk 0.007 , and the water temperature is ,

<!-- b000628 | prose | pages [42, 43] -->
This strategy can achieve the goal of keeping the temperature even throughout the bathtub and as close as possible to the initial temperature without wasting too much water, and the injected hot water temperature is kept in a very comfortable range. At this point, additional water requirement is 12.6L . The ratio of the additional water requirement and the water demand of the bath is 2.84%, the optimal rate for this strategy is 12.66%. After adding hot water, the most comfortable water temperature satisfactory rate is 91.39%.The function of water temperature over time and space in the whole bath process is as follows:

<!-- b000629 | furniture | pages [43] -->
Team #46830

<!-- b000630 | furniture | pages [43] -->
Page 40 of 45

<!-- b000632 | prose | pages [43] -->
   4    2.45731 10 t 1   T x y z t ( , , , ) T t ( ) 4.294 e y

<!-- b000633 | prose | pages [43] -->
Where the relation curve of variance T t has been given in the form of images ( )

<!-- b000634 | prose | pages [43] -->
and scattered points.

<!-- b000635 | prose | pages [43] -->
This series of results shows the effectiveness and the practical reference value of the optimal control model and optimization strategy. II. The situation of using the bubble water Based on the thermodynamic model modified by bubble water, we obtain the overall heat dissipated at 312K degrees power after using the bubble is 3076.92W , This value is 45.85%times larger than the original. In addition, under the coordination of

<!-- b000636 | prose | pages [43] -->
the optimal policy, adding additional 12.6L hot water of 311.1K can make the

<!-- b000637 | prose | pages [43] -->
temperature difference reach 46.79%, It shows that the bubble bath and the way of adding can be very effective to keep the water temperature

<!-- b000638 | heading | pages [43] -->
6.3 Future Work

<!-- b000639 | prose | pages [43] -->
I. The variance of the water in the bathtub is measured by the actual situation or A series of points were randomly selected on the 4.1.3.II temperature surface by  K t in the simple function fitting programming for calculating or using the function

<!-- b000640 | prose | pages [43] -->
   T x y z t ( , , , ) T t ( ) K t y expressions formula (11) , and then we can get more

<!-- b000641 | prose | pages [43] -->
accurate temperature distribution function in time and space.

<!-- b000642 | prose | pages [43] -->
II. By improving the algorithm and the use of more computing power compute to calculate the accurate optimized results. Especially for the calculation of strategy 2, it needs a powerful computer to make a further analysis, for example, solving the equivalent injection quantity of water injection in subsection by the strategy, etc.

<!-- b000643 | prose | pages [43] -->
III. We can also use this model to calculate the other bathtub, for instance the top view of the bathtub is sector, half elliptical sphere, etc.

<!-- b000644 | furniture | pages [44] -->
Team #46830

<!-- b000645 | furniture | pages [44] -->
Page 41 of 45

<!-- b000646 | heading | pages [44] -->
7    Explanation

<!-- b000647 | prose | pages [44] -->
Why it's so hard to enjoy a hot bath

<!-- b000648 | prose | pages [44] -->
Is your bathtub a spa-style tub with a secondary heating system and circulating jets? If not, then you will feel the water will gradually cool when you are taking a bath. That's right, it is extremely hard for the simple bathtub to keep constant temperature.

<!-- b000649 | prose | pages [44] -->
As we all know, if we want to keep the bath water temperature maintain a certain temperature, the only way is the injection of water. But in order to save water, we need to take a certain strategy. Some people will do that, inject water when you feel cold, stop adding hot water when you feel hot. But it seems a little hard to do that. We obtain the switching time, water temperature of the best strategy by the computer. Finally, it was found that time interval between water injection and off water is zero. Is means that this method is not as good as most people think about? Maybe it’s a good idea to try another method.

<!-- b000650 | prose | pages [44] -->
Some people will leave the tap running out of hot water, and then take a comfortable bath. In fact, this is the best way. So the problem comes, how fast to keep the hot water running, how high the temperature of hot water can keep the temperature of bathwater constant? Generally speaking, we need to consider the heat exchange between hot water and bath, heat exchange between hot water and air, evaporation heat absorption of hot water, heat absorption and heat release of human body and heat radiation of water. We also need to take the heat of adding hot water and the energy taken away by overflow into account. Let alone to consider these factors of the movement of people or bubble bath.

<!-- b000651 | prose | pages [44] -->
In addition, personal preferences of hot water temperature settings are not necessarily the same. To give further consideration to the human body size, the volume and body surface area are different, the size, shape and material of each bathtub are different. Each of the above factors will affect the optimal bath strategy. More importantly, because the heat transfer process is continuous, so it makes the calculation complexity, and we also need to consider the data acquisition and the error of calculation. In a word, it's not easy to enjoy a hot bath.

<!-- b000652 | furniture | pages [45] -->
Team #46830

<!-- b000653 | furniture | pages [45] -->
Page 42 of 45

<!-- b000654 | heading | pages [45] -->
References

<!-- b000655 | references | pages [45] -->
[1] Oronzio Manca,Sergio Nardini,Daniele icci. Numerical Analysis of Water Forced

<!-- b000656 | references | pages [45] -->
Convection in Channels with Differently Shaped Transverse Ribs. Journal of Applied

<!-- b000657 | references | pages [45] -->
Mathematics, 2011, Vol.2011, pp.1-25

<!-- b000658 | references | pages [45] -->
[2] Gheorghe Juncu. Unsteady conjugate forced convection heat/mass transfer in

<!-- b000659 | references | pages [45] -->
ensembles of Newtonian fluid spheres. International Journal of Heat and Mass

<!-- b000660 | references | pages [45] -->
Transfer, 2010, Vol.53 (13), pp.2780-2789

<!-- b000661 | references | pages [45] -->
[3] Li Liu,Xiaodong Li, Fang Q. Hu.Nonuniform-time-step explicit Runge–Kutta

<!-- b000662 | references | pages [45] -->
scheme for high-order finite difference method. Computers and Fluids,2014,Vol.105

<!-- b000663 | references | pages [45] -->
[4] Fang, Shah. The Effect of Surfactant Monolayers on the Heat Transfer Through

<!-- b000664 | references | pages [45] -->
Air/Water and Oil/Water Interfaces Using IR Imaging Technique. Journal of colloid

<!-- b000665 | references | pages [45] -->
and interface science, 1998, Vol.205 (2), pp.531-534

<!-- b000666 | references | pages [45] -->
[5] Xue-jun Zhang,Ke-qing Zheng,Ling-shi Wang,Wei Wang,Min Jiang,Sheng-ying

<!-- b000667 | references | pages [45] -->
Zhao. Analysis of ice slurry production by direct contact heat transfer of air and water

<!-- b000668 | references | pages [45] -->
solution. Journal of Zhejiang University SCIENCE A, 2013, Vol.14 (8), pp.583-588

<!-- b000669 | references | pages [45] -->
[6] Yoshihito Kurazumi,Tadahiro Tsuchikawa, Naoki Matsubara,Tetsumi Horikoshi.

<!-- b000670 | references | pages [45] -->
Effect of posture on the heat transfer areas of the human body. Building and

<!-- b000671 | references | pages [45] -->
Environment, 2007, Vol.43 (10), pp.1555-1565

<!-- b000672 | references | pages [45] -->
[7] Yoshihito Kurazumi,Tadahiro Tsuchikawa, Naoki Matsubara,Tetsumi Horikoshi.

<!-- b000673 | references | pages [45] -->
Convective heat transfer area of the human body. European Journal of Applied

<!-- b000674 | references | pages [45] -->
Physiology, 2004, Vol.93 (3), pp.273-285

<!-- b000675 | references | pages [45] -->
[8] Fajie Wang,Wen Chen,Yan Gu.Boundary element analysis of inverse heat

<!-- b000676 | references | pages [45] -->
conduction problems in 2D thin-walled structures. International Journal of Heat and

<!-- b000677 | references | pages [45] -->
Mass Transfer, 2015, Vol.91

<!-- b000678 | references | pages [45] -->
[9]

<!-- b000679 | references | pages [45] -->
J.-L.Battaglia,O.Cois,L.Puigsegur,A.Oustaloup.Solving

<!-- b000680 | references | pages [45] -->
an

<!-- b000681 | references | pages [45] -->
inverse

<!-- b000682 | references | pages [45] -->
heat

<!-- b000683 | references | pages [45] -->
conduction problem using a non-integer identified model. International Journal of

<!-- b000684 | references | pages [45] -->
Heat and Mass Transfer, 2001, Vol.44 (14), pp.2671-2680

<!-- b000685 | references | pages [45] -->
[10] Yasser Mahmoudi.Effect of thermal radiation on temperature differential in a

<!-- b000686 | references | pages [45] -->
porous medium under local thermal non-equilibrium condition .International Journal

<!-- b000687 | references | pages [45] -->
of Heat and Mass Transfer, 2014, Vol.76

<!-- b000688 | references | pages [45] -->
[11] J.R.Saylor,G.B.Smith,K.A.Flack.The effect of a surfactant monolayer on the

<!-- b000689 | references | pages [45] -->
temperature field of a water surface undergoing evaporation. International Journal of

<!-- b000690 | references | pages [45] -->
Heat and Mass Transfer, 2000, Vol.43 (17), pp.3073-3086

<!-- b000691 | references | pages [45] -->
[12] Rosario De Lisi,Stefania Milioto,Nicola Muratore. Thermodynamics of

<!-- b000692 | references | pages [45] -->
Surfactants, Block Copolymers and Their Mixtures in Water: The Role of the

<!-- b000693 | references | pages [45] -->
Isothermal Calorimetry. International Journal of Molecular Sciences, 2009, Vol.10 (7),

<!-- b000694 | references | pages [45] -->
pp.2873

<!-- b000695 | furniture | pages [46] -->
Team #46830

<!-- b000696 | furniture | pages [46] -->
Page 43 of 45

<!-- b000697 | references | pages [46] -->
[13] YUAN Yirang .Finite difference method and analysis for three-dimensional

<!-- b000698 | references | pages [46] -->
semiconductor device of heat conduction. Institute of Mathematics, Science in

<!-- b000699 | references | pages [46] -->
China .Ser.A, 1996

<!-- b000700 | references | pages [46] -->
[14] Cheng Rong-Jun. Meshless analysis of three-dimensional steady-state heat

<!-- b000701 | references | pages [46] -->
Conduction problems. Ningbo Institute of Technology, 2005

<!-- b000702 | references | pages [46] -->
[15] SUN Shufen, YAN Jinfeng, XIA Nan, SUN Changhai .Development of a Model

<!-- b000703 | references | pages [46] -->
for Water and Heat Exchange Between the Atmosphere and a Water Body.

<!-- b000704 | references | pages [46] -->
Geophysical Fluid Dynamics (LASG) Institute of Atmospheric Physics Chinese

<!-- b000705 | references | pages [46] -->
Academy of Sciences, 2007

<!-- b000706 | heading | pages [47] -->
Appendix

<!-- b000707 | prose | pages [47] -->
First: program list

<!-- b000708 | prose | pages [47] -->
1.Spherical propagation of heat source x=-2:.1:2;y=x;  %x=-1.4:0.1:2 [x,y]=meshgrid(x,y); z=sqrt(16-x.^2-y.^2); mesh(x,y,z) hold on z=z+2; %mesh(x,y,z) plot3(x,y,z,'r') hold on z=z+2; mesh(x,y,z) xlabel('x') ylabel('y') zlabel('z')

<!-- b000709 | prose | pages [47] -->
2.partial large-normal distribution

<!-- b000710 | prose | pages [47] -->
clear

<!-- b000711 | prose | pages [47] -->
clc

<!-- b000712 | prose | pages [47] -->
x=0:0.01:1;aj=0;qj=0.21829;

<!-- b000713 | prose | pages [47] -->
w=1-exp(-((x-aj)/qj).^2);

<!-- b000714 | prose | pages [47] -->
plot(x,w) xlabel('Forced convection') ylabel('Convective mixing ratio') 3. Solve the optimal water flow rate and optimal water temperature

<!-- b000715 | prose | pages [47, 48] -->
function [y,Tr,Te]=algorithm2() clear clc t=0.5;y=1000; dT=0.1;total=0; sum=0;S=0; a=1.3;b=0.8;H=0.49;     %size of bathtub c=4200;p=1000;         %water-specific heat capacity, D o you usually get annoyed with the cooling of water during a relaxing bath? In this p aper, several models are proposed to solve the problem. Our efforts in building these models Tb=306;h1=166; q=2.4062*10^6;u=0.9824*10^(-3)/2; m=5.67*10^(-8);k=0.15*10^(-3)*0.5/0.15; k1=2.7;C0=0.4434*c*p; C1=-a*h*(2*H+b);C2=-q*a*b*u; C3=-h1*S1;C4=-a*b*m; C5=c*p*k*Tb;C6=c*p*k; x=[]; syms T; while(Tb<318) C5=c*p*k*Tb; syms T Tc; Tm=solve('-T*2.5157*10^3+2100*Tc+5.8969*10^(-8)*T^4+1.2885*10^5=0',T) Tsk=vpa(subs(Tm,Tc,Tb)); Tsk=double(Tsk); xe=find(Tsk>250&Tsk<320); Ts=Tsk(xe); Tmin1=306; while(Tmin1<=Ts-1.1) Tmin2=306+dT; while(Tmin2<=Ts-1) Tk=Tmin1; T2=Tmin2; total=0;S=0;sum=0; while(Tk<=Tmin2) betak=(C1*(Tk-T0)+C2+C3*(Tk-T1)+C4*Tk^4+C5-C6*(Tk-0.5*a*k1))/C0; Tk1=Tk+betak; total=total+t; sum=sum+t; S=(317-Tk1)*t+S; if(betak<10^(-8)) break; end Tk=Tk1; end Tk=T2; while(Tk>=Tmin1) betak=(C1*(Tk-T0)+C2+C3*(Tk-T1)+C4*Tk^4)/C0; Tk1=Tk+betak;

<!-- b000717 | prose | pages [49] -->
sum=sum+t; S=(317-Tk1)*t+S; Tk=Tk1; end res=total/50+2*S/sum-100/(3*sqrt(2)*pi)*exp(-(Tb-312)^2/9);

<!-- b000718 | prose | pages [49] -->
if(y>res) y=res; Tr=Tmin1; Te=Tmin2; qw=[y Tr Te Ts Tb] end Tmin2=Tmin2+dT; end Tmin1=Tmin1+dT; end Tb=Tb+dT; end end

<!-- b000719 | heading | pages [49] -->
4. Solve the relationship curve between the temperature of water bathtub and time

<!-- b000720 | prose | pages [49] -->
function []=algorithm3() clear clc a=1.3;b=0.8;H=0.49; c=4200;p=1000; h=42.8;T0=298; S1=1.9;T1=310; h1=166;q=2.4062*10^6; u=0.9824*10^(-3)/2;m=5.67*10^(-8); k1=2.7;C0=0.4434*c*p; C1=-a*h*(2*H+b);C2=-q*a*b*u; C3=-h1*S1;C4=-a*b*m; beta_t=1;x=[];y=[]; Tb=311.1;kb=0.007; k=kb*10^(-3);sum=0;Tk=317;C5=c*p*k*Tb;C6=c*p*k;C7=k1*h1*2.23; while(sum<1800) beta_k=(C1*(Tk-T0)+C2+C3*(Tk-T1)+C4*Tk^4+C5-C6*(Tk-0.5*a*k1))/C0; Tnext=Tk+beta_k; sum=sum+beta_t; x=[x,sum];

<!-- b000721 | prose | pages [50] -->
y=[y,Tk];

<!-- b000722 | prose | pages [50] -->
Tk=Tnext;

<!-- b000723 | prose | pages [50] -->
end plot(x,y,'r') hold on sum=0;beta_t=1;x=[];y=[];Tk=317;

<!-- b000724 | prose | pages [50] -->
while(sum<1800) beta_k=(C1*(Tk-T0)+C2+C3*(Tk-T1)+C4*Tk^4-C7)/C0;

<!-- b000725 | prose | pages [50] -->
Tnext=Tk+beta_k;

<!-- b000726 | prose | pages [50] -->
sum=sum+beta_t;

<!-- b000727 | prose | pages [50] -->
x=[x,sum];

<!-- b000728 | prose | pages [50] -->
y=[y,Tk];

<!-- b000729 | prose | pages [50] -->
Tk=Tnext;

<!-- b000730 | prose | pages [50] -->
end plot(x,y) %axis([0 1800 306 318]) legend('improved','normal') xlabel('t/bath-time(s)') ylabel('T/average temperature of water(K)') end

<!-- b000731 | prose | pages [50] -->
6. t=pi/2:pi/20:pi;

<!-- b000732 | prose | pages [50, 51] -->
x=sin(t)*5; y=cos(t)*5; z=linspace(0,5,length(t)); X=meshgrid(x); Y=meshgrid(y); Z=[meshgrid(z)]'; surf(X,Y,Z) xlabel('x'),ylabel('y'),zlabel('z') axis equal axis([0 6 -5 0 0 5]) for k=1:4 view(-37.5,10*k) end hold on [y,z]=meshgrid(-5:0,0:5);  % ---x=0 x=zeros(length(y),length(y)); %mesh(x,y,z) surf(x,y,z) hold on [x,z]=meshgrid(0:5,0:5); %  ---y=0 y=zeros(length(z),length(z));

<!-- b000734 | prose | pages [51] -->
%mesh(x,y,z) surf(x,y,z) hold on alpha=-pi/2:pi/20:0;    %  --z=0 R=5;

<!-- b000735 | prose | pages [51] -->
x=R*cos(alpha);

<!-- b000736 | prose | pages [51] -->
y=R*sin(alpha);

<!-- b000737 | prose | pages [51] -->
plot(x,y,'-') axis equal fill([0,x],[0,y],'r');

<!-- b000738 | prose | pages [51] -->
Second:  data list 1. The data of temperature curve for fitting x1=[0 0.1238 0.2476 0.3714 0.4952 0.619 0.7129 0.8667 1.052 1.176 1.3];

<!-- b000739 | prose | pages [51] -->
y1=[0.8  0.8  0.8   0.8   0.8    0.8   0.8   0.8   0.8   0.8   0.8];

<!-- b000740 | prose | pages [51] -->
z1=[44.3 44.17 43.73 43.08 42.34 41.68 41.09 40.58 40.02 39.79 39.67];

<!-- b000741 | prose | pages [51] -->
x2=[0 0.1857 0.3095 0.4333 0.5571 0.681 0.8048 0.9286 1.114 1.3];

<!-- b000742 | prose | pages [51] -->
y2=[0.318 0.381 0.381 0.381 0.381 0.381 0.381 0.381 0.381 0.381];

<!-- b000743 | prose | pages [51] -->
z2=[45.05 44.59 43.83 43 42.2 41.49 40.94 40.49 40.01 39.79];

<!-- b000744 | prose | pages [51] -->
x3=[0 0.1857 0.3714 0.4952 0.619 0.7429 0.8667 1.052 1.176];

<!-- b000745 | prose | pages [51] -->
y3=[0  0   0   0   0   0   0   0   0];

<!-- b000746 | prose | pages [51] -->
z3=[44.31 43.98 43.05 42.33 41.66 41.08 40.59 40.03 39.79];

<!-- b000747 | prose | pages [51] -->
x4=[0.0619 0.2476 0.3714 0.4952 0.619 0.7429 0.9286 1.114 1.3];

<!-- b000748 | prose | pages [51] -->
y4=[0.6095 0.6095 0.6095 0.6095 0.6095 0.6095 0.6095 0.6095 0.6095];

<!-- b000749 | prose | pages [51] -->
z4=[44.64 44 43.27 42.49 41.77 41.16 40.45 39.97 39.75];

<!-- b000750 | prose | pages [51] -->
x5=[0 0.1857 0.3714 0.4952 0.619 0.7429 0.9286 1.114];

<!-- b000751 | prose | pages [51] -->
y5=[0.1905 0.1905 0.1905 0.1905 0.1905 0.1905 0.1905 0.1905];

<!-- b000752 | prose | pages [51] -->
z5=[44.7 44.31 43.25 42.5  41.8  41.16  40.45 39.97];

<!-- b000753 | prose | pages [51] -->
x=[x1,x2,x3,x4,x5];

<!-- b000754 | prose | pages [51] -->
y=[y1,y2,y3,y4,y5];

<!-- b000755 | prose | pages [51] -->
z=[z1,z2,z3,z4,z5];
