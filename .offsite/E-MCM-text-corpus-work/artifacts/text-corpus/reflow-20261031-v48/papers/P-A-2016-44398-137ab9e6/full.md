# P-A-2016-44398-137ab9e6

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000003 | front_matter | pages [1] -->
44398

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 Problem Chosen

<!-- b000005 | front_matter | pages [1] -->
A

<!-- b000006 | prose | pages [1] -->
T3 F3 T4 F4

<!-- b000007 | front_matter | pages [1] -->
2016 Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
A traditional bathtub cannot be reheated by itself, so users have to add hot water from time to time. Our goal is to establish a model of the temperature of bath water in space and time. Then we are expected to propose an optimal strategy for users to keep the temperature even and close to initial temperature and decrease water consumption.

<!-- b000010 | prose | pages [1] -->
To simplify modeling process, we firstly assume there is no person in the bathtub. We regard the whole bathtub as a thermodynamic system and introduce heat transfer formulas.

<!-- b000011 | prose | pages [1] -->
We establish two sub-models: adding water constantly and discontinuously. As for the former sub-model, we define the mean temperature of bath water. Introducing Newton cooling formula, we determine the heat transfer capacity. After deriving the value of parameters, we deduce formulas to derive results and simulate the change of temperature field via CFD. As for the second sub-model, we define an iteration consisting of two process: heating and standby. According to energy conservation law, we obtain the relationship of time and total heat dissipating capacity. Then we determine the mass flow and the time of adding hot water. We also use CFD to simulate the temperature field in second sub-model.

<!-- b000012 | prose | pages [1] -->
In consideration of evaporation, we correct the results of sub-models referring to some scientists’ studies. We define two evaluation criteria and compare the two sub-models. Adding water constantly is found to keep the temperature of bath water even and avoid wasting too much water, so it is recommended by us.

<!-- b000013 | prose | pages [1] -->
Then we determine the influence of some factors: radiation heat transfer, the shape and volume of the tub, the shape/volume/temperature/motions of the person, the bubbles made from bubble bath additives. We focus on the influence of those factors to heat transfer and then conduct sensitivity analysis. The results indicate smaller bathtub with less surface area, lighter personal mass, less motions and more bubbles will decrease heat transfer and save water.

<!-- b000014 | prose | pages [1] -->
Based on our model analysis and conclusions, we propose the optimal strategy for the user in a bathtub and explain the reason of uneven temperature throughout the bathtub. In addition, we make improvement for applying our model in real life.

<!-- b000015 | keywords | pages [1] -->
Key words:  Heat transfer  Thermodynamic system  CFD  Energy conservation

<!-- b000016 | furniture | pages [2] -->
Team #44398                                                    Page 2 of 51

<!-- b000017 | contents | pages [2] -->
Enjoy a Cozy and Green Bath

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
1  Introduction .................................................................................................. 4

<!-- b000020 | contents | pages [2] -->
1.1  Background ......................................................................................... 4

<!-- b000021 | contents | pages [2] -->
1.2 Literature Review ............................................................................... 4

<!-- b000022 | contents | pages [2] -->
1.3 Restatement of the Problem .............................................................. 4

<!-- b000023 | contents | pages [2] -->
2 Assumptions and Justification .................................................................. 6

<!-- b000024 | contents | pages [2] -->
3 Notations........................................................................................................ 7

<!-- b000025 | contents | pages [2] -->
4 Model Overview ........................................................................................... 7

<!-- b000026 | contents | pages [2] -->
5  Sub-model I : Adding Water Continuously ............................................ 8

<!-- b000027 | contents | pages [2] -->
5.1  Model Establishment ......................................................................... 9

<!-- b000028 | contents | pages [2] -->
5.1.1  Control Equations and Boundary Conditions .................... 9

<!-- b000029 | contents | pages [2] -->
5.1.2  Definition of the Mean Temperature .................................. 11

<!-- b000030 | contents | pages [2] -->
5.1.3  Determination of Heat Transfer Capacity ......................... 11

<!-- b000031 | contents | pages [2] -->
5.2  Results ................................................................................................ 13

<!-- b000032 | contents | pages [2] -->
5.2.1  Determination of Parameters .............................................. 13

<!-- b000033 | contents | pages [2] -->
5.2.2  Calculating Results ............................................................... 14

<!-- b000034 | contents | pages [2] -->
5.2.3  Simulating Results ................................................................ 15

<!-- b000035 | contents | pages [2] -->
6  Sub-model II: Adding Water Discontinuously .................................... 18

<!-- b000036 | contents | pages [2] -->
6.1  Heating Model .................................................................................. 18

<!-- b000037 | contents | pages [2] -->
6.1.1  Control Equations and Boundary Conditions .................. 18

<!-- b000038 | contents | pages [2] -->
6.1.2  Determination of Inflow Time and Amount ..................... 19

<!-- b000039 | contents | pages [2] -->
6.2  Standby Model ................................................................................. 20

<!-- b000040 | contents | pages [2] -->
6.2.1  Process Analysis .................................................................... 20

<!-- b000041 | contents | pages [2] -->
6.2.2  Calculation of Parameters .................................................... 20

<!-- b000042 | contents | pages [2] -->
6.3  Results ................................................................................................ 21

<!-- b000043 | contents | pages [2] -->
6.3.1  Determination of Parameters .............................................. 21

<!-- b000044 | contents | pages [2] -->
6.3.2  Calculating Results ............................................................... 23

<!-- b000045 | furniture | pages [3] -->
Team #44398                                                    Page 3 of 51

<!-- b000046 | contents | pages [3] -->
6.3.3  Simulating Results ................................................................ 23

<!-- b000047 | contents | pages [3] -->
6.4  Conclusion ........................................................................................ 27

<!-- b000048 | contents | pages [3] -->
7  Correction and Contrast of Sub-Models ............................................... 27

<!-- b000049 | contents | pages [3] -->
7.1  Correction with Evaporation Heat Transfer ................................ 27

<!-- b000050 | contents | pages [3] -->
7.1.1  Correction Principle .............................................................. 27

<!-- b000051 | contents | pages [3] -->
7.1.2  Correction Results ................................................................. 28

<!-- b000052 | contents | pages [3] -->
7.2  Contrast of Two Sub-Models .......................................................... 30

<!-- b000053 | contents | pages [3] -->
7.2.1  Evaluation Criteria ................................................................ 30

<!-- b000054 | contents | pages [3] -->
7.2.2  Determination of Water Consumption .............................. 30

<!-- b000055 | contents | pages [3] -->
7.2.3  Conclusion ............................................................................. 31

<!-- b000056 | contents | pages [3] -->
8  Model Analysis and Sensitivity Analysis ............................................. 31

<!-- b000057 | contents | pages [3] -->
8.1  The Influence of Different Bathtubs .............................................. 32

<!-- b000058 | contents | pages [3] -->
8.1.1  Different Volumes of Bathtubs ............................................ 32

<!-- b000059 | contents | pages [3] -->
8.1.2  Different Shapes of Bathtubs ............................................... 34

<!-- b000060 | contents | pages [3] -->
8.2  The Influence of Person in Bathtub ............................................... 36

<!-- b000061 | contents | pages [3] -->
8.2.1  When the Person Remains Static in a Bathtub .................. 36

<!-- b000062 | contents | pages [3] -->
8.2.2  When the Person Moves in a Bathtub ................................ 37

<!-- b000063 | contents | pages [3] -->
8.2.3  Results Analysis and Sensitivity Analysis ......................... 38

<!-- b000064 | contents | pages [3] -->
8.3  The Influence of Bubble Bath Additives ....................................... 42

<!-- b000065 | contents | pages [3] -->
8.4  The Influence of Radiation Heat Transfer .................................... 44

<!-- b000066 | contents | pages [3] -->
8.5  Conclusion ........................................................................................ 45

<!-- b000067 | contents | pages [3] -->
9  Further Discussion ..................................................................................... 45

<!-- b000068 | contents | pages [3] -->
9.1  Different Distribution of Inflow Faucets ...................................... 45

<!-- b000069 | contents | pages [3] -->
9.2  Model Application ........................................................................... 46

<!-- b000070 | contents | pages [3] -->
10  Strength and Weakness ........................................................................... 47

<!-- b000071 | contents | pages [3] -->
10.1  Strength ........................................................................................... 47

<!-- b000072 | contents | pages [3] -->
10.2  Weakness ......................................................................................... 47

<!-- b000073 | contents | pages [3] -->
Report ................................................................................................................. 49

<!-- b000074 | contents | pages [3] -->
Reference ........................................................................................................... 50

<!-- b000075 | furniture | pages [4] -->
Team #44398                                                    Page 4 of 51

<!-- b000076 | heading | pages [4] -->
1  Introduction

<!-- b000077 | heading | pages [4] -->
1.1  Background

<!-- b000078 | prose | pages [4] -->
Bathing in a tub is a perfect choice for those who have been worn out after a long day’s working. A traditional bathtub is a simply water containment vessel without a secondary heating system or circulating jets. Thus the temperature of water in bathtub declines noticeably as time goes by, which will influent the experience of bathing. As a result, the bathing person needs to add a constant trickle of hot water from a faucet to reheat the bathing water. This way of bathing will result in waste of water because when the capacity of the bathtub is reached, excess water overflows the tub.

<!-- b000079 | prose | pages [4] -->
An optimal bathing strategy is required for the person in a bathtub to get comfortable bathing experience while reducing the waste of water.

<!-- b000080 | heading | pages [4] -->
1.2 Literature Review

<!-- b000081 | prose | pages [4] -->
Korean physicist Gi-Beum Kim analyzed heat loss through free surface of water contained in bathtub due to conduction and evaporation [1]. He derived a relational equation based on the basic theory of heat transfer to evaluate the performance of bath tubes. The major heat loss was found to be due to evaporation. Moreover, he found out that the speed of heat loss depends more on the humidity of the bathroom than the temperature of water contained in the bathtub. So, it is best to maintain the temperature of bathtub water to be between 41 to 45 ℃ and the humidity of bathroom to be 95%.

<!-- b000082 | prose | pages [4] -->
When it comes to convective heat transfer in bathtub, many studies can be referred to. Newton's law of cooling states that the rate of heat loss of a body is proportional to the difference in temperatures between the body and its surroundings while under the effects of a breeze [2]. Claude-Louis Navier and George Gabriel Stokes described the motion of viscous fluid substances with the Navier–Stokes equations. Those equations may be used to model the weather, ocean currents, water flow in a pipe and air flow around a wing [3].

<!-- b000083 | prose | pages [4] -->
In addition, some numerical simulation software are applied in solving and analyzing problems that involve fluid flows. For example, Computational Fluid Dynamics (CFD) is a common one used to perform the calculations required to simulate the interaction of liquids and gases with surfaces defined by boundary conditions [4].

<!-- b000084 | heading | pages [4] -->
1.3 Restatement of the Problem

<!-- b000085 | prose | pages [4, 5] -->
We are required to establish a model to determine the change of water temperature in space and time. Then we are expected to propose the best strategy for the person in the bathtub to keep the water temperature close to initial temperature and even throughout the tub. Reduction of waste of water is also needed. In addition, we have to consider the impact of different conditions on our model, such as different shapes and volumes of the bathtub, etc.

<!-- b000086 | furniture | pages [5] -->
Team #44398                                                    Page 5 of 51

<!-- b000088 | prose | pages [5] -->
In order to solve those problems, we will proceed as follows:

<!-- b000089 | prose | pages [5] -->
 Stating assumptions. By stating our assumptions, we will narrow the focus of our approach towards the problems and provide some insight into bathtub water temperature issues.

<!-- b000090 | prose | pages [5] -->
 Making notations. We will give some notations which are important for us to clarify our models.

<!-- b000091 | prose | pages [5] -->
 Presenting our model. In order to investigate the problem deeper, we divide our model into two sub-models. One is a steady convection heat transfer sub-model in which hot water is added constantly. The other one is an unsteady convection heat transfer sub-model where hot water is added discontinuously.

<!-- b000092 | prose | pages [5] -->
 Defining evaluation criteria and comparing sub-models. We define two main criteria to evaluate our model: the mean temperature of bath water and the amount of inflow water.

<!-- b000093 | prose | pages [5] -->
 Analysis of influencing factors. In term of the impact of different factors on our model, we take those into consideration: the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub, the motions made by the person in the bathtub and adding a bubble bath additive initially.

<!-- b000094 | prose | pages [5] -->
 Model testing and sensitivity analysis. With the criteria defined before, we evaluate the reliability of our model and do the sensitivity analysis.

<!-- b000095 | prose | pages [5] -->
 Further discussion. We discuss about different ways to arrange inflow faucets. Then we improve our model to apply them in reality.

<!-- b000096 | prose | pages [5] -->
 Evaluating the model. We discuss about the strengths and weaknesses of our model.

<!-- b000097 | furniture | pages [6] -->
Team #44398                                                    Page 6 of 51

<!-- b000098 | heading | pages [6] -->
2 Assumptions and Justification

<!-- b000099 | prose | pages [6] -->
To simplify the problem and make it convenient for us to simulate real-life conditions, we make the following basic assumptions, each of which is properly justified.

<!-- b000100 | prose | pages [6] -->
 The bath water is incompressible Non-Newtonian fluid. The incompressible Non-Newtonian fluid is the basis of Navier–Stokes equations which are introduced to simulate the flow of bath water.

<!-- b000101 | prose | pages [6] -->
 All the physical properties of bath water, bathtub and air are assumed to be stable. The change of those properties like specific heat, thermal conductivity and density is rather small according to some studies [5]. It is complicated and unnecessary to consider these little change so we ignore them.

<!-- b000102 | prose | pages [6] -->
 There is no internal heat source in the system consisting of bathtub, hot water and air. Before the person lies in the bathtub, no internal heat source exist except the system components. The circumstance where the person is in the bathtub will be investigated in our later discussion.

<!-- b000103 | prose | pages [6] -->
 We ignore radiative thermal exchange. According to Stefan- Boltzmann’s law, the radiative thermal exchange can be ignored when the temperature is low. Refer to industrial standard [6], the temperature in bathroom is lower than 100℃, so it is reasonable for us to make this assumption.

<!-- b000104 | prose | pages [6] -->
 The temperature of the adding hot water from the faucet is stable.

<!-- b000105 | prose | pages [6] -->
This hypothesis can be easily achieved in reality and will simplify our process of solving the problem.

<!-- b000106 | furniture | pages [7] -->
Team #44398                                                    Page 7 of 51

<!-- b000107 | heading | pages [7] -->
3 Notations

<!-- b000108 | caption | pages [7] -->
Table 1  Notations

<!-- b000109 | prose | pages [7] -->
Symbols Definition Unit    2 W / m K h Convection heat transfer coefficient    k W / m K Thermal conductivity    pc J / kg K Specific heat 2  kg / m Density  m Thickness t K ℃、 Temperature  s min h 、 、 Time q kg/s Mass flow m  W Heat transfer power s min h 、 、 T A period of time 3 V m L 、 Volume M m 、 kg Mass 2 m A Area 3 a b c m 、、 The size of a bathtub

<!-- b000110 | prose | pages [7] -->
where we define the main parameters while specific value of those parameters will be

<!-- b000111 | prose | pages [7] -->
given later.

<!-- b000112 | heading | pages [7] -->
4 Model Overview

<!-- b000113 | prose | pages [7] -->
In our basic model, we aim at three goals: keeping the temperature as even as possible, making it close to the initial temperature and decreasing the water consumption.

<!-- b000114 | prose | pages [7] -->
We start with the simple sub-model where hot water is added constantly. At first we introduce convection heat transfer control equations in rectangular coordinate system. Then we define the mean temperature of bath water. Afterwards, we introduce Newton cooling formula to determine heat transfer capacity. After deriving the value of parameters, we get calculating results via formula deduction and simulating results via CFD.

<!-- b000115 | prose | pages [7] -->
Secondly, we present the complicated sub-model in which hot water is added discontinuously. We define an iteration consisting of two process: heating and standby. As for heating process, we derive control equations and boundary conditions. As for standby process, considering energy conservation law, we deduce the relationship of total heat dissipating capacity and time.

<!-- b000116 | furniture | pages [8] -->
Team #44398                                                    Page 8 of 51

<!-- b000117 | prose | pages [8] -->
Then we determine the time and amount of added hot water. After deriving the value of parameters, we get calculating results via formula deduction and simulating results via CFD.

<!-- b000118 | prose | pages [8] -->
At last, we define two criteria to evaluate those two ways of adding hot water. Then we propose optimal strategy for the user in a bathtub.

<!-- b000119 | prose | pages [8] -->
The whole modeling process can be shown as follows.

<!-- b000120 | caption | pages [8] -->
Fig.1  Modeling process

<!-- b000121 | heading | pages [8] -->
5  Sub-model I : Adding Water Continuously

<!-- b000122 | prose | pages [8] -->
We first establish the sub-model based on the condition that a person add water continuously to reheat the bathing water. Then we use Computational Fluid Dynamics (CFD) to simulate the change of water temperature in the bathtub. At last, we evaluate the model with the criteria which have been defined before.

<!-- b000123 | furniture | pages [9] -->
Team #44398                                                    Page 9 of 51

<!-- b000124 | heading | pages [9] -->
5.1  Model Establishment

<!-- b000125 | prose | pages [9] -->
Since we try to keep the temperature of the hot water in bathtub to be even, we have to derive the amount of inflow water and the energy dissipated by the hot water into the air.

<!-- b000126 | prose | pages [9] -->
We derive the basic convection heat transfer control equations based on the former scientists’ achievement. Then, we define the mean temperature of bath water. Afterwards, we determine two types of heat transfer: the boundary heat transfer and the evaporation heat transfer. Combining thermodynamic formulas, we derive calculating results. Via Fluent software, we get simulation results.

<!-- b000127 | heading | pages [9] -->
5.1.1  Control Equations and Boundary Conditions

<!-- b000128 | prose | pages [9] -->
According to thermodynamics knowledge, we recall on basic convection heat transfer control equations in rectangular coordinate system. Those equations show the relationship of the temperature of the bathtub water in space.

<!-- b000129 | prose | pages [9] -->
We assume the hot water in the bathtub as a cube. Then we put it into a rectangular coordinate system. The length, width, and height of it is a , b and c .

<!-- b000130 | caption | pages [9] -->
Fig.2  The water cube in the rectangular coordinate system

<!-- b000131 | prose | pages [9] -->
In the basis of this, we introduce the following equations [5]:

<!-- b000132 | prose | pages [9] -->
 Continuity equation:

<!-- b000133 | prose | pages [9] -->
   u v w   + 0 （1）    x y z

<!-- b000134 | prose | pages [9] -->
where the first component is the change of fluid mass along the X-ray. The second component is the change of fluid mass along the Y-ray. And the third component is the change of fluid mass along the Z-ray. The sum of the change in mass along those three directions is zero.

<!-- b000135 | furniture | pages [10] -->
Team #44398                                                    Page 10 of 51

<!-- b000136 | prose | pages [10] -->
 Moment differential equation (N-S equations):

<!-- b000137 | prose | pages [10] -->
       2 2 2 u u u p u u u         ( u v w ) ( ) （2）        2 2 2 x y z x x y z

<!-- b000138 | prose | pages [10] -->
       2 2 2 v v v p v v v         ( u v w ) ( ) （3）        2 2 2 x y z y x y z

<!-- b000139 | prose | pages [10] -->
       2 2 2 w w w p w w w         ( u v w ) g ( ) （4）        2 2 2 x y z z x y z

<!-- b000140 | prose | pages [10] -->
 Energy differential equation:

<!-- b000141 | prose | pages [10] -->
      2 2 2 t t t t t t       c u ( v + w ) ( ) （5） p       2 2 2 x y z x y z

<!-- b000142 | prose | pages [10] -->
where the left three components are convection terms while the right three components are conduction terms.

<!-- b000143 | prose | pages [10] -->
Having derived those equations, we give the boundary conditions listed as follows:

<!-- b000144 | prose | pages [10] -->
In the inflow water area

<!-- b000145 | prose | pages [10] -->
 t t （6） in

<!-- b000146 | prose | pages [10] -->
On the top surface of bath water, it transfer heat directly into air without heat conduction, so we have  t       h t t （7）  1  z The range of the area suitable for (7) is

<!-- b000147 | prose | pages [10] -->
     0 x b , 0 y a z , c （8） On the front surface in Fig.2, the water transfer heat firstly with bathtub inner surfaces and then the heat comes into air. Hence we have  t      h t t （9） 2 x  x The range of the area suitable for (9) is

<!-- b000148 | prose | pages [10] -->
     0 y a , 0 z c x , b （10）

<!-- b000149 | prose | pages [10, 11] -->
On the right surface in Fig.2, the water also transfers heat firstly with bathtub inner surfaces and then the heat comes into air. The boundary condition here is  t      h t t （11） 3 y  y

<!-- b000150 | furniture | pages [11] -->
Team #44398                                                    Page 11 of 51

<!-- b000152 | prose | pages [11] -->
The range of the area suitable for (11) is

<!-- b000153 | prose | pages [11] -->
     0 x b , 0 z c , y a （12）

<!-- b000154 | heading | pages [11] -->
5.1.2  Definition of the Mean Temperature

<!-- b000155 | prose | pages [11] -->
To simplify the modeling process, we assume the bathtub and hot water in it as a constant temperature system. Thus the heat is equal in value to the enthalpy difference between inflow water and outflow water.

<!-- b000156 | prose | pages [11] -->
We let the total heat dissipation to be Q and the mass flow of inflow q . Recalling on the heat balance equation, we have water to be m  q c t Q （13） m p

<!-- b000157 | prose | pages [11] -->
c is the specific heat of water which is constant according to our where p assumptions.

<!-- b000158 | prose | pages [11] -->
 is t The temperature difference of heat transfer   t t t （14） in out

<!-- b000159 | prose | pages [11] -->
int is the temperature of inflow water and t where is the temperature out of outflow water.

<!-- b000160 | prose | pages [11] -->
Although the temperature is different from area to area, the difference is rather small which has been proved by some scientists [8]. So we substitute the mean temperature in the bathtub with the mean value of the inflow water and outflow water. That is  t t  in out t （15） f 2 ft is the mean temperature in the bathtub. where

<!-- b000161 | heading | pages [11] -->
5.1.3  Determination of Heat Transfer Capacity

<!-- b000162 | prose | pages [11, 12] -->
The real-life heat transfer process is a complicated mixed heat transfer problem which is shown as follows  1

<!-- b000163 | furniture | pages [12] -->
Team #44398                                                    Page 12 of 51

<!-- b000165 | prose | pages [12] -->
  2 2

<!-- b000166 | prose | pages [12] -->
ft ft

<!-- b000167 | prose | pages [12] -->
 2

<!-- b000168 | prose | pages [12] -->
t t

<!-- b000169 | caption | pages [12] -->
Fig.3  The sketch of bathtub heat transfer

<!-- b000170 | prose | pages [12] -->
As we can see in the above figure, the hot water in a bathtub has six radiating surfaces. On top surface transfers heat directly with air. The other surfaces transfer heat firstly with bathtub inner surfaces. Then the heat conducts through the bathtub and be transferred into air.

<!-- b000171 | prose | pages [12] -->
As for the top radiating surface, we derive the amount of radiating heat  with the aid of Newton cooling formula 1     （16） hA t t 1 f

<!-- b000172 | prose | pages [12] -->
In reality, the bathtub manufacturers tend to add some layers of thermal insulation materials to decrease the heat loss. So the boundary of a bathtub is made up by different material layers.

<!-- b000173 | prose | pages [12] -->
t t t w1 w2 w3

<!-- b000174 | prose | pages [12] -->
ft

<!-- b000175 | prose | pages [12] -->
1h

<!-- b000176 | prose | pages [12] -->
2h 1k 2k   t 1 2

<!-- b000177 | prose | pages [12] -->
Layers of thermal Outside the tub Inside the tub insulation materials

<!-- b000178 | caption | pages [12] -->
Fig.4  The sketch of boundary heat transfer

<!-- b000179 | prose | pages [12, 13] -->
1k and k are thermal conductivity of the inner and outer layer In Fig.4, 2  and  are the thickness of the inner and of thermal insulation materials. 1 2 outer layer of thermal insulation materials. The heat transfer coefficient 1h . The heat transfer between the hot water and inner surface of the bathtub is h . t t t coefficient between air and outer surface of the bathtub is , and 2 w1 w2 w3 are the temperatures of three boundaries of the thermal insulation material layers.

<!-- b000180 | furniture | pages [13] -->
Team #44398                                                    Page 13 of 51

<!-- b000182 | prose | pages [13] -->
According to heat conduction formula, we have  t t   = f （17） 2     1 1 1    1 2   A h k k h   1 1 2 2

<!-- b000183 | prose | pages [13] -->
Hence the total heat dissipation capacity is  （18） 1 2

<!-- b000184 | heading | pages [13] -->
5.2  Results

<!-- b000185 | prose | pages [13] -->
We first give the value of parameters based on others’ studies. Then we get the calculation results and simulating results via those data.

<!-- b000186 | heading | pages [13] -->
5.2.1  Determination of Parameters

<!-- b000187 | prose | pages [13] -->
After establishing the model, we have to determine the value of some important parameters.

<!-- b000188 | prose | pages [13] -->
As scholar Beum Kim points out, the optimal temperature for bath is between 41 and 45℃[1]. Meanwhile, according to Shimodozono’s study, 41℃ warm water bath is the perfect choice for individual health [2]. So it is reasonable for us to focus on 41℃~45℃. Because adding hot water continuously is a steady process, so the mean temperature of bath water is supposed to be constant. We value the temperature of inflow and outflow water with the maximum and minimum temperature respectively.

<!-- b000189 | prose | pages [13] -->
The values of all parameters needed are shown as follows:

<!-- b000190 | furniture | pages [14] -->
Team #44398                                                    Page 14 of 51

<!-- b000191 | caption | pages [14] -->
Table 2  The values of parameters

<!-- b000192 | prose | pages [14] -->
Parameters Values Unit int ℃ 45 t ℃ 41 out ft ℃ 43 t ℃ 25 1 mm 0.64  mm 30 2  2 1h W / (m K) 10  2 1h W / (m K) 300  1k W / (m K) 0.19  2k W / (m K) 0.036  c J / (kg K) 4174 p  0.85 None 3  kg / m 992 M kg 320 3 m a b c * * 1.8*0.9*0.64 3 m V 0.32

<!-- b000193 | heading | pages [14] -->
5.2.2  Calculating Results

<!-- b000194 | prose | pages [14] -->
Putting the above value of parameters into the equations we derived before, we can get the some data as follows

<!-- b000195 | caption | pages [14] -->
Table 3  The calculating results

<!-- b000196 | prose | pages [14] -->
Variables Values Unit 2 m 1A 1.05 2 m A 2.24 2  W 189.00 1  W 43.47 2  W 232.47 g/s q 0.014 m

<!-- b000197 | prose | pages [14, 15] -->
In this table, we find the whole amount of radiating heat of the bathtub is 232.47 W. Based on industrial standards, the bathtub we chose has capacity of 320L. The temperature of inflow and outflow water is designed to be 45 and 41℃, the mass flow turns out to be 0.014 g/s (that is 0.84 kg/min ). Only this condition is satisfied can the temperature throughout the bathtub be kept as even as possible.

<!-- b000198 | furniture | pages [15] -->
Team #44398                                                    Page 15 of 51

<!-- b000200 | heading | pages [15] -->
5.2.3  Simulating Results

<!-- b000201 | prose | pages [15] -->
It is quite unrealistic for us to compute the equations (1)-(5) because the N- S equation is coupled to the energy equation. In order to derive the temperature field, the velocity field is needed. Then introduce the boundary conditions, the temperature field is worked out. However, this method is so difficult that The Clay Mathematics Institute of Cambridge, Massachusetts (CMI) even sets prize to inspire people to solve it. So we have to employ Computational Fluid Dynamics (CFD) to simulate the temperature field based on those equations.

<!-- b000202 | prose | pages [15] -->
We will proceed as follows:

<!-- b000203 | heading | pages [15] -->
 Step 1: Via Gambit software, we establish the three-dimensional model and

<!-- b000204 | prose | pages [15] -->
divide meshes. Then we define the boundary type.

<!-- b000205 | prose | pages [15] -->
 Step 2: Using Fluent software to read and examine the meshes.

<!-- b000206 | prose | pages [15] -->
 Step 3: Defining solving model. We introduce Laminar Model to simulate the N-S equation and Energy Model to simulate the energy equation.

<!-- b000207 | prose | pages [15] -->
 Step 4: Defining the materials and correcting the corresponding physical property parameters.

<!-- b000208 | prose | pages [15] -->
 Step 5: Defining the boundary conditions.

<!-- b000209 | prose | pages [15] -->
 Step 6: Solving initialization.

<!-- b000210 | prose | pages [15] -->
 Step 7: Setting number of iterations.

<!-- b000211 | prose | pages [15] -->
 Step 8: The results are derived when the convergence conditions are met.

<!-- b000212 | prose | pages [15] -->
Applying the above steps in our first sub-model, the results turn out to be satisfying.

<!-- b000213 | prose | pages [15] -->
First of all, we divide meshes with the aid of Gambit software, which is shown in the following figure.

<!-- b000214 | furniture | pages [16] -->
Team #44398                                                    Page 16 of 51

<!-- b000215 | caption | pages [16] -->
Fig.5  Divide meshes in Gambit

<!-- b000216 | prose | pages [16] -->
As is shown in Fig.5, we divide the hot water into 129600 meshes. Then we export the Mesh file then import it into Fluent and make corresponding settings. Afterwards, we begin to compute it by iteration. When the iteration is conducted for 379 times, the problem is nearly convergent. The curve of residual is shown in Fig.5.

<!-- b000217 | caption | pages [16] -->
Fig.6  The curve of residual

<!-- b000218 | prose | pages [16] -->
Combining specific boundary conditions, we have the temperature field throughout the bathtub. In reality, there are various ways of water inflow and outflow. We design the water to flow into the bathtub from left side and out of the bathtub from the right side.

<!-- b000219 | prose | pages [16] -->
We take the temperature field of two surfaces as examples.

<!-- b000220 | furniture | pages [17] -->
Team #44398                                                    Page 17 of 51

<!-- b000221 | caption | pages [17] -->
Fig.7 (a)  The temperature field of the bottom surface

<!-- b000222 | caption | pages [17] -->
Fig.7 (b)  The temperature field of the side surface

<!-- b000223 | prose | pages [17] -->
where ‘the bottom surface’ means the x-O-y surface while ‘the side surface’ is the y-O-z

<!-- b000224 | prose | pages [17] -->
surface of the water cube in Fig2. The temperature shown in the legend is presented in

<!-- b000225 | prose | pages [17] -->
Kelvin scale and the data should be expended to 100 times.

<!-- b000226 | prose | pages [17] -->
As we can see in the figures, the temperature in the bathtub is different from area to area, which decreases along the direction of water flow. However, the temperature fluctuates between 43 to 45 ℃(316-318 K). The highest temperature is that of inflow area because the adding water is the hottest. In addition, due to the stability of this model when a person adds hot water continually, the temperature of each area remains stable.

<!-- b000227 | prose | pages [17] -->
In conclusion, the temperature is not strictly even throughout the bathtub. It differs according to boundary conditions. However, the mean temperature of the whole water in the bathtub is stable.

<!-- b000228 | prose | pages [17] -->
By the way, because of the shortage of Fluent software in simulating small water flow, the temperature marked by different colors may differ a little. For example, in the legend, 44℃(317 K) corresponds with colors ranging from blue to orange. Actually, each color represents a different temperature  between 44- 45 ℃(317-318K). The changing tendency of colors strictly represents the changing tendency of the temperature.

<!-- b000229 | furniture | pages [18] -->
Team #44398                                                    Page 18 of 51

<!-- b000230 | heading | pages [18] -->
6  Sub-model II: Adding Water Discontinuously

<!-- b000231 | prose | pages [18] -->
In order to establish the unsteady sub-model, we recall on the working principle of air conditioners. The heating performance of air conditions consist of two processes: heating and standby. After the user set a temperature, the air conditioner will begin to heat until the expected temperature is reached. Then it will go standby. When the temperature get below the expected temperature, the air conditioner begin to work again. As it works in this circle, the temperature remains the expected one.

<!-- b000232 | prose | pages [18] -->
Inspired by this, we divide the bathtub working into two processes: adding hot water until the expected temperature is reached, then keeping this condition for a while unless the temperature is lower than a specific value. Iterating this circle ceaselessly will ensure the temperature kept relatively stable.

<!-- b000233 | heading | pages [18] -->
6.1  Heating Model

<!-- b000234 | heading | pages [18] -->
6.1.1  Control Equations and Boundary Conditions

<!-- b000235 | prose | pages [18] -->
We focus on heating process at first. During this process, the hot water flows throughout the bathtub so we need to use N-S equation. We also have to introduce energy equation considering there is convective heat transfer in the flow.

<!-- b000236 | prose | pages [18] -->
Adding an unsteady term into basic N-S equation [3], we have

<!-- b000237 | prose | pages [18] -->
        2 2 2 u u u u p u u u          ( u v w ) ( ) （19）          2 2 2 x y z x x y z

<!-- b000238 | prose | pages [18] -->
The above equation is established along x-axis. The other two equations along y-axis and z-axis can be easily deduced so we omit them.

<!-- b000239 | prose | pages [18] -->
Similarly, we add unsteady term into energy equation and get

<!-- b000240 | prose | pages [18] -->
       2 2 2 t t t t t t t        c ( u v + w ) ( ) （20） p         2 2 2 x y z x y z

<!-- b000241 | prose | pages [18] -->
As for the boundary conditions, (6)-(12) are also suitable for this model. Except those, there are two other conditions:

<!-- b000242 | prose | pages [18] -->
  （21） when 0 t t ， f

<!-- b000243 | prose | pages [18] -->
    （22） when , t t 0 f min

<!-- b000244 | prose | pages [18] -->
t where is the minimum of mean temperature of bath water. min

<!-- b000245 | furniture | pages [19] -->
Team #44398                                                    Page 19 of 51

<!-- b000246 | heading | pages [19] -->
6.1.2  Determination of Inflow Time and Amount

<!-- b000247 | prose | pages [19] -->
The bathtub can be simplified as a water containment vessel, so the amount of inflow and outflow is the equal in value. Hence the mass of the bath water in a bathtub is constant. That is

<!-- b000248 | prose | pages [19] -->
 （23） q q = q m in out

<!-- b000249 | prose | pages [19] -->
t  and the We let initial mean temperature of bath water to be f1 int . Frequently, the mean temperature will temperature of inflow water to be rise as hot water added, which leads the temperature of outflow to rise. We let t the final temperature of outflow to be . out2 t and t Both are functions of time. f1 out2       t f , t g （24） f out

<!-- b000250 | prose | pages [19] -->
We assume the bath water in bathtub as a control volume, so the energy stored in bathtub is the difference between the energy of inflow and outflow. This can be seen in the following figure.

<!-- b000251 | caption | pages [19] -->
Fig.8  The transfer and storage of energy

<!-- b000252 | prose | pages [19] -->
The total heat dissipating capacity turns out to be

<!-- b000253 | prose | pages [19] -->
     Q out = d （25） T 1 We also derive that  t t         （26） t hA t t f  f 1 f     1 1 1    1 2   A h k k h   2 1 1 2 2

<!-- b000254 | prose | pages [19, 20] -->
As the temperature of inflow water is higher than that of bath water in the bathtub, so the inflow will transfer heat into the bath water. The energy that bath water gets is equal in value to the enthalpy difference between inflow and outflow. Hence     mc t t （27） in p f 2 f1 Referring to formula (15), we have

<!-- b000255 | furniture | pages [20] -->
Team #44398                                                    Page 20 of 51

<!-- b000257 | prose | pages [20] -->
 t t in out2 t f 2= （28） 2 The enthalpy difference between inflow and outflow is very the energy added into bath water. That is

<!-- b000258 | prose | pages [20] -->
     d Q q c t t （29） m p in out T 1 According to energy conservation principle, it follows that

<!-- b000259 | prose | pages [20] -->
  Q Q Q （30） in out

<!-- b000260 | prose | pages [20] -->
t , the heating process is When the temperature of bath water reaches f 2 stopped. Based on these above relationships, we derive the time of adding hot 1T and the corresponding amount of inflow q . water m

<!-- b000261 | heading | pages [20] -->
6.2  Standby Model

<!-- b000262 | heading | pages [20] -->
6.2.1  Process Analysis

<!-- b000263 | prose | pages [20] -->
After the heating process is finished, the mean temperature of bath water t . In standby process, it is assumed to be put in a space of which the is f 2 temperature is t and transfer heat into the space. Finally, the temperature f1t and the next iteration begins. During decreases to a specific temperature ft the standby process, the mean temperature of bath water is expressed by which is a function of time.

<!-- b000264 | heading | pages [20] -->
6.2.2  Calculation of Parameters

<!-- b000265 | prose | pages [20] -->
Throughout the whole process of cooling, the bath water transfer heat to the surroundings via convection or other ways. So that its internal energy is reduced as time goes by.

<!-- b000266 | prose | pages [20] -->
We take the whole bath water as a control volume and derive the energy balance equation:

<!-- b000267 | prose | pages [20] -->
dt       c V hA t t （31）  p  d The initial conditions are

<!-- b000268 | prose | pages [20] -->
  when =0 t t （32） ， f2

<!-- b000269 | prose | pages [20] -->
   when t t （33） ， 

<!-- b000270 | prose | pages [20, 21] -->
According to before discussion and based on the surfaces of the control volume, we have

<!-- b000271 | furniture | pages [21] -->
Team #44398                                                    Page 21 of 51

<!-- b000273 | prose | pages [21] -->
1   hA hA （34） 1     1 1 1    1 2   A h k k h   2 1 1 2 2

<!-- b000274 | prose | pages [21] -->
Then we integrating t over  in formula (31) and get   hA       c V    t t t t exp （35）     f 2    p

<!-- b000275 | prose | pages [21] -->
f1t , the time of standby process turns When the temperature decreases to out to be  pc V  t t   T ln f1 （36） 2  hA t t  f 2

<!-- b000276 | prose | pages [21] -->
The whole heat transfer capacity is     hA            Q c V t t 1 exp T （37）      p f 2 2  c V     p

<!-- b000277 | heading | pages [21] -->
6.3  Results

<!-- b000278 | heading | pages [21] -->
6.3.1  Determination of Parameters

<!-- b000279 | prose | pages [21] -->
One of our goals is to keep the temperature even throughout the bathtub. So we firstly have to determine the value of corresponding parameters such as the initial temperature of inflow and outflow.

<!-- b000280 | prose | pages [21] -->
According to the data we use in the first sub-model, the temperature in the bathtub ranges between 41 to 45 ℃. In this sub-model, we still set the int 445 ℃. In order to give the user temperature of inflow water to be comfortable experience, we set the change of the mean temperature less than t f1=42 1℃.thus the lowest mean temperature ℃.While the highest mean t f 2=43 at ℃. The expected mean temperature turns out to be temperature 442.5℃. In that way, the maximum change of the mean temperature is only 0.5℃.

<!-- b000281 | prose | pages [21] -->
The other parameters will change over time. The change value cannot be expressed by specific functions. So we need to analyze them according to our model. We first focus on the different temperatures during the heating process. The temperature of inflow remains stable. The temperature of outflow is stable for a while but begins to rise as hot water added. Meanwhile, the mean temperature also rises when the user adds hot water into the bathtub. The changing trend is shown as follows:

<!-- b000282 | furniture | pages [22] -->
Team #44398                                                    Page 22 of 51

<!-- b000283 | caption | pages [22] -->
Fig.9  The changing trend of different temperature

<!-- b000284 | prose | pages [22] -->
From the above picture, we can see that the mean temperature remains rising. After the added hot water arrives at the outflow side, the temperature of cT to represent the time between outflow begins to be influenced. We let adding hot water and the temperature of outflow beginning to rise. This process can be divided into two parts:

<!-- b000285 | prose | pages [22] -->
 When the time is shorter than cT , the temperature of outflow remains stable.

<!-- b000286 | prose | pages [22] -->
 When the time is longer than cT , the temperature of outflow begins to rise.

<!-- b000287 | prose | pages [22] -->
1T is Then we need to determine whether the time of adding hot water cT . Recalling on the first sub-model, we derive that the longer or shorter than temperature of inflow is 45℃ while the temperature of outflow is 41℃. Under such circumstance, the mean temperature turns out to remain 43℃.

<!-- b000288 | prose | pages [22] -->
We assume the area that added hot water covers is in stable state. If we  T T firstly suppose , the whole hot water is in stable state. This is alike the 1 c first sub-model where the mean temperature is 43℃.However the expected 1T is longer mean temperature is 42.5℃, higher than 43℃. That means before cT , the mean temperature has reached 42.5℃. So it is untrue for us to than   T T T T suppose . That is to say . Based on that, the initial temperature of 1 c 1 c outflow is equal to the value of the lowest mean temperature  t t f1=42 ℃.Still, it is convenient for us to compute. out The value of corresponding parameters is listed in the following table.

<!-- b000289 | furniture | pages [23] -->
Team #44398                                                    Page 23 of 51

<!-- b000290 | caption | pages [23] -->
Table 4  The value of corresponding parameters

<!-- b000291 | prose | pages [23] -->
Parameters Value Unit

<!-- b000292 | prose | pages [23] -->
int ℃ 45 t ℃ 42 f1 t ℃ 43 f 2 at ℃ 42.5 ft ℃ 43 t ℃ 42 out

<!-- b000293 | heading | pages [23] -->
6.3.2  Calculating Results

<!-- b000294 | prose | pages [23] -->
q and the time of adding hot water The relationship between mass flow m 1T is    12522 Tq 232 T 1333008 0 （38） 1 m 1

<!-- b000295 | prose | pages [23] -->
Commonly, it will be better if the time of adding hot water is shorter.

<!-- b000296 | prose | pages [23] -->
T  3min According to some data from the Internet, we make . From formula 1 q 40.61kg/s. Putting these data into formulas (38)，we compute the mass flow m T 45914s (approximately 1.64h). (31)-(36), we find 2

<!-- b000297 | caption | pages [23] -->
Table 5  The calculating results

<!-- b000298 | prose | pages [23] -->
Parameters Value Unit

<!-- b000299 | prose | pages [23] -->
1T 3 min T 1.64 h 2 T 101.4 min q 0.61 kg/s m where T is the total time of an iteration.

<!-- b000300 | heading | pages [23] -->
6.3.3  Simulating Results

<!-- b000301 | prose | pages [23, 24] -->
Because this sub-model is a three-dimensional problem, it is hard for us to simulate it by Fluent. The hot water of constant temperature flows into the bathtub and is mixed with the bath water, causing fluid convection. The temperature field is symmetric so that we can simplify it as a two-dimensional problem. Although there are heat insulating materials around the bathtub, the heat transfer coefficient of forced convection of water is much larger than that of natural convection of air and water. So it is reasonable for us to simplify the problem as a two-dimensional one.

<!-- b000302 | furniture | pages [24] -->
Team #44398                                                    Page 24 of 51

<!-- b000304 | prose | pages [24] -->
Considering the simulating by a computer takes too much time, we set the mass flow of the inflow water to be 0.04m/s. The residual curve of simulation is shown as follows.

<!-- b000305 | caption | pages [24] -->
Fig.10  The residual curve of simulation

<!-- b000306 | prose | pages [24] -->
The change of temperature field is present in the following four pictures.

<!-- b000307 | prose | pages [24] -->
（a）=1s

<!-- b000308 | prose | pages [24, 25] -->
(b) t=2s                     (c) t=10s (d) t=20s                      (e) t=30s

<!-- b000309 | furniture | pages [25] -->
Team #44398                                                    Page 25 of 51

<!-- b000311 | caption | pages [25] -->
Fig.11  The change of temperature field

<!-- b000312 | prose | pages [25] -->
where the picture (a) is the complete representation of the temperature field while

<!-- b000313 | prose | pages [25] -->
pictures (b)-(e) are partial representation of the temperature field. The temperature in the

<!-- b000314 | prose | pages [25] -->
legend is presented in Kelvin scale and the data should be expended to 100 times.

<!-- b000315 | prose | pages [25] -->
From the figure of the residual curve of simulation, we can find that the residual changes periodically and the change is small, which indicates the stability of the simulating results. Limited to time, we simulate situations which only last for 30s.

<!-- b000316 | prose | pages [25] -->
The four pictures in Fig.11 shows the change of temperature field after the hot water is added. Because the water flows in specific velocity, it influences mainly the area in front of it. However, the area beside it is hardly affected and remains the primary temperature. As more hot water is added, the convective surface becomes larger and moves towards the exit. We can also find there is an obvious interface between the added hot water and the initial bath water. That indicates the difference of temperature of added water and bath water is supposed to be small.

<!-- b000317 | prose | pages [25] -->
In the standby process, the bath water is put in a space, cooling freely. Recalling on our calculating results before, it takes about 1.64h for the temperature of the whole bath water to decrease by 1℃. Since it is impossible for out computer to simulate the change over such long time, we shrink the size of bathtub. The boundary conditions remain unchanged. Shrinking the size to 1/100, we get the temperature field as following.

<!-- b000318 | furniture | pages [26] -->
Team #44398                                                    Page 26 of 51

<!-- b000319 | caption | pages [26] -->
Fig.12  The residual curve of simulation

<!-- b000320 | prose | pages [26] -->
(a) t=3s

<!-- b000321 | prose | pages [26] -->
(b) t=15s

<!-- b000322 | caption | pages [26] -->
Fig.13   The temperature field

<!-- b000323 | prose | pages [26, 27] -->
Compared to initial bathtub, although the size changes, the heat transfer remains the same. As is shown in the picture (a), when the time is short, the change of temperature of middle areas is small. That is because the main convection happens in boundary areas. As time goes by, the cooler areas spread towards the middle area, as is presented in picture (b). So that the temperature of other areas besides the middle begins to change. However, the change is small, most of which is less than 2℃. The lowest temperature occurs in four corners, being 40℃ approximately. After the mean temperature is lower than the expected value, the bathtub user needs to add hot water into the bathtub to reheat the water. This simulating result corresponds to the calculating result we derived before.

<!-- b000324 | furniture | pages [27] -->
Team #44398                                                    Page 27 of 51

<!-- b000326 | heading | pages [27] -->
6.4  Conclusion

<!-- b000327 | prose | pages [27] -->
According to calculation and simulation, we basically determine the time of an iteration. The heating process lasts for 3 min while the mass flow is 0.61kg/s. the standby process lasts for 1.64h while the mean temperature decreases by 1℃. By simulating the two situations, we proof the validity of our model and explain why it is so slow for the temperature of bath water to decrease.

<!-- b000328 | heading | pages [27] -->
7  Correction and Contrast of Sub-Models

<!-- b000329 | prose | pages [27] -->
After establishing two basic sub-models, we have to correct them in consideration of evaporation heat transfer. Then we define two evaluation criteria to compare the two sub-models in order to determine the optimal bath strategy.

<!-- b000330 | heading | pages [27] -->
7.1  Correction with Evaporation Heat Transfer

<!-- b000331 | prose | pages [27] -->
Someone may confuse about the above results: why the mass flow in the first sub-model is so small? Why the standby time is so long? Actually, the above two sub-models are based on ideal conditions without consideration of the change of boundary conditions, the motions made by the person in bathtub and the evaporation of bath water, etc. The influence of personal motions will be discussed later. Here we introducing the evaporation of bath water to correct sub-models.

<!-- b000332 | heading | pages [27] -->
7.1.1  Correction Principle

<!-- b000333 | prose | pages [27] -->
According to Gi-Beum Kim’s studies, the heat transfer capacity is relative not only with boundary mixed heat transfer, but also with evaporation heat transfer. More importantly, the major heat loss is found to be due to evaporation [1]. In order to clarify our correction process more clearly, we briefly introduce his achievement and findings.

<!-- b000334 | furniture | pages [28] -->
Team #44398                                                    Page 28 of 51

<!-- b000335 | prose | pages [28] -->
The evaporation heat transfer is related to the temperature of the bath water, the air humidity of the bathroom, the total thermal resistance, material properties and so on. The relationship is given as follows:

<!-- b000336 | prose | pages [28] -->
 Mc t  p   EA L dt （39）   f  t t kA t 0  0

<!-- b000337 | prose | pages [28] -->
where k is the thermal resistance. A is the area of heat transfer. L is the latent heat of evaporation.  is the thickness of materials. fA is the area of free surface. E is the evaporation capacity.

<!-- b000338 | prose | pages [28] -->
The experimental formula that Gi-Beum Kim gives is    0.88   0.88      t /22.009 E 0.37 0.0041 v 0.0041 e 0.004 1 （40）

<!-- b000339 | prose | pages [28] -->
where v is the mean temperature of air and  is the air humidity.

<!-- b000340 | prose | pages [28] -->
The experimental formula for the latent heat of evaporation L is   t   0.174 L t 273.15 3.484 （41）

<!-- b000341 | prose | pages [28] -->
 and the convection We let the evaporation heat transfer capacity to be s . Then the total heat loss is heat transfer capacity to be q   = （42） t s q

<!-- b000342 | prose | pages [28] -->
Plugging the above formulas into sub-models, we obtain the precise results after being corrected.

<!-- b000343 | heading | pages [28] -->
7.1.2  Correction Results

<!-- b000344 | prose | pages [28] -->
Considering the model established by Gi-Beum Kim is similar with ours, so we can refer to his results to correct our sub-models. In his experiment, the bathtub has a capacity of 250L, which is close to the capacity of our bathtub. When the air humidity remains stable, he finds the change of mean temperature over time as follows [1]:

<!-- b000345 | furniture | pages [29] -->
Team #44398                                                    Page 29 of 51

<!-- b000346 | caption | pages [29] -->
Fig.14  Mean temperature change under different air humidity

<!-- b000347 | prose | pages [29] -->
As is vividly shown in Fig.14, the air humidity affects the mean temperature of bath water heavily. The more air humidity is, the smaller evaporation capacity will be, so that the main heat transfer comes from boundary convection heat transfer.

<!-- b000348 | prose | pages [29] -->
Commonly, the air humidity is high in bathroom but the air temperature is low. According to Fig.14 , we assume it takes 0.75 h (45 min ) for the temperature of bath water to decrease by 1℃.

<!-- b000349 | prose | pages [29] -->
Since we have obtained the convection capacity in before calculation, we can compute the evaporation capacity based on energy conservation. Then the total heat transfer capacity can be derived and the correction is to be conduct. The corrected results in listed in the following table.

<!-- b000350 | caption | pages [29] -->
Table 6  The corrected results

<!-- b000351 | prose | pages [29, 30] -->
Parameters Value Unit  261.24 W s  232.47 W q  522.71 W t q 0.03 kg/s m 1 q kg/s 0.63 m 2 1T 3 min T 45 min 2 T 48 min Let us analyze the corrected results. The mean temperature in the first sub- model mainly depends on convective heat transfer capacity because it is in steady state. As for the second sub-model, the convection heat transfer hardly affects the heating process because the specific heat is large. The standby process is similar with the first sub-model, so it is affected by evaporation heat transfer.

<!-- b000352 | furniture | pages [30] -->
Team #44398                                                    Page 30 of 51

<!-- b000354 | heading | pages [30] -->
7.2  Contrast of Two Sub-Models

<!-- b000355 | prose | pages [30] -->
Firstly we define two evaluation criteria. Then we contrast the two sub- models via these two criteria. Thus we can derive the best strategy for the person in the bathtub to adopt.

<!-- b000356 | heading | pages [30] -->
7.2.1  Evaluation Criteria

<!-- b000357 | prose | pages [30] -->
We aim at three goals: keeping the temperature as even as possible, making it close to the initial temperature and decreasing the water consumption. Considering that, we define two criteria to evaluate the sub-models:

<!-- b000358 | prose | pages [30] -->
 The average temperature of the water in bathtub. It is difficult to keep the temperature strictly even throughout the bathtub because convective heat transfer is an unsteady process. However, the difference in temperature of diverse area is rather small so we can use the average temperature to substitute the temperature of whole bathtub. With the aid of Gi-Beum Kim’s study, the optimal temperature ranges from 41 to 45℃[1].

<!-- b000359 | prose | pages [30] -->
 Water consumption during a bath. According to data from the internet, the water consumption of bathing in a bathtub is four times as many as bathing with a shower [7]. So it is necessary for the bathtub users to decrease water consumption, not only for lower cost of bath but also for the responsibility to the environment.

<!-- b000360 | heading | pages [30] -->
7.2.2  Determination of Water Consumption

<!-- b000361 | prose | pages [30] -->
In the before discussion, we have derived the mass flow in the two sub- models. Giving the bath time, it is easy to compute the total water consumption. Considering the bathtub is filled with same water capacity, the difference of water consumption is added hot water. So we only have to calculate the amount of added water in order to compare the sub-models.

<!-- b000362 | prose | pages [30, 31] -->
bT . Since the hot water is added consistently, We let the bath time to be the mass flow is a constant over time. So the total amount of added water is  m T q （43） 1 b m 1

<!-- b000363 | furniture | pages [31] -->
Team #44398                                                    Page 31 of 51

<!-- b000365 | prose | pages [31] -->
As for the second sub-model, the hot water is only added during the heating process. So the mass flow in heating process is constant while that in standby process is zero. Then we have the total amount of added water in second sub-model

<!-- b000366 | prose | pages [31] -->
  T   b m 1 T q （44）   2 1 m 2 T  

<!-- b000367 | prose | pages [31] -->
bT may not where we use Gauss integral function. Because the bath time be any multiple of the iteration time T , we have to round the figure. No matter what period adding hot water reaches, we assume it as a complete iteration so that the actual iteration times need to be plus one.

<!-- b000368 | prose | pages [31] -->
bT  48min To simplify our calculation, we set the bath time to be , which is very an iteration time. Thus we find the amount of added water consumption m  86.4 kg in the first sub-model to be , while that in the second sub-model to 1 m  113.4 kg be . 2

<!-- b000369 | heading | pages [31] -->
7.2.3  Conclusion

<!-- b000370 | prose | pages [31] -->
In terms of the mean temperature of bath water, the temperature of the first sub-model is 43℃ while that of the second sub-model ranges from 42 to 43℃. According to common sense, a person can hardly feel 1℃change of temperature. So both strategies of adding water are optimal for the person in a bathtub.

<!-- b000371 | prose | pages [31] -->
As the water consumption of the first sub-model is 84.6 kg, while that of the second sub-model is 113.4 kg. Considering our goal to decrease water consumption, it is obviously wise to choose adding hot water continually instead of adding water discontinuously.

<!-- b000372 | prose | pages [31] -->
In conclusion, we recommend the person in the bathtub to add hot water continually with mass flow being 0.03 kg/s. This strategy can not only ensure comfortable bath experience but also avoid wasting too much water.

<!-- b000373 | heading | pages [31] -->
8  Model Analysis and Sensitivity Analysis

<!-- b000374 | prose | pages [31] -->
The results of the model we establish before correspond with literature to huge extent. However, the model is based on an ideal situation that there is no person in bathtub. Still, the bathtub in our model is simplified as a cube.

<!-- b000375 | prose | pages [31, 32] -->
In reality, things are quite different. The bathtub can be designed into various shapes and volumes and there is undoubtedly one person or more in the bathtub. The person in bathtub may have various shapes, volume and temperature. He / She is likely to make mangy motions during bath time. In addition, people tend to use a bubble bath additive while initially filling the bathtub to assist in cleansing, which may affect our model’s results as well.

<!-- b000376 | furniture | pages [32] -->
Team #44398                                                    Page 32 of 51

<!-- b000378 | prose | pages [32] -->
So here we will conduct sensitivity analysis to determine the extent to which our model depends upon those influencing factors

<!-- b000379 | heading | pages [32] -->
8.1  The Influence of Different Bathtubs

<!-- b000380 | prose | pages [32] -->
Definitely, the difference in shape and volume of the tub affects the convection heat transfer. Examining the relationship between them can help people choose optimal bathtubs.

<!-- b000381 | heading | pages [32] -->
8.1.1  Different Volumes of Bathtubs

<!-- b000382 | prose | pages [32] -->
In reality, a cup of water will be cooled down rapidly. However, it takes quite long time for a bucket of water to become cool. That is because their volume is different and the specific heat of water is very large. So that the decrease of temperature is not obvious if the volume of water is huge. That also explains why it takes 45 min for 320 L water to be cooled by 1℃.

<!-- b000383 | prose | pages [32] -->
In order to examine the influence of volume, we analyze our sub-models by conducting sensitivity Analysis to them.

<!-- b000384 | prose | pages [32] -->
  5% 8% We assume the initial volume to be 280 L and change it by , ,   12% 15% and . With the aid of sub-models we established before, the variation of some parameters turns out to be as follows

<!-- b000385 | caption | pages [32] -->
Table7  Variation of some parameters

<!-- b000386 | prose | pages [32] -->
 2A T q q V 1A 2 m 1 m 2 q

<!-- b000387 | prose | pages [32] -->
-15.00% -5.06% -9.31% -12.67% -2.67% -14.14% -5.80%

<!-- b000388 | prose | pages [32] -->
-12.00% -4.04% -7.43% -10.09% -2.13% -11.31% -4.63%

<!-- b000389 | prose | pages [32] -->
-8.00% -2.68% -4.94% -6.68% -1.41% -7.54% -3.07%

<!-- b000390 | prose | pages [32] -->
-5.00% -1.67% -3.08% -4.16% -0.88% -4.71% -1.92%

<!-- b000391 | prose | pages [32] -->
-2.00% -0.67% -1.23% -1.65% -0.35% -1.89% -0.76%

<!-- b000392 | prose | pages [32] -->
0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00%

<!-- b000393 | prose | pages [32] -->
2.00% 0.67% 1.22% 1.64% 0.35% 1.89% 0.76%

<!-- b000394 | prose | pages [32] -->
5.00% 1.66% 3.05% 4.09% 0.87% 4.71% 1.90%

<!-- b000395 | prose | pages [32] -->
8.00% 2.65% 4.87% 6.51% 1.40% 7.54% 3.03%

<!-- b000396 | prose | pages [32] -->
12.00% 3.96% 7.28% 9.71% 2.09% 11.31% 4.54%

<!-- b000397 | prose | pages [32, 33] -->
15.00% 4.94% 9.08% 12.08% 2.60% 14.14% 5.66% To show the relationship of different parameters and volume, we put the data in the following pictures.

<!-- b000398 | furniture | pages [33] -->
Team #44398                                                    Page 33 of 51

<!-- b000400 | prose | pages [33] -->
 over volume T and

<!-- b000401 | caption | pages [33] -->
Fig.15  The change of

<!-- b000402 | prose | pages [33] -->
2 q

<!-- b000403 | prose | pages [33] -->
q q

<!-- b000404 | caption | pages [33] -->
Fig.16  The change of

<!-- b000405 | prose | pages [33] -->
and over volume m 1 m 2

<!-- b000406 | prose | pages [33] -->
From the above figures, we can find when the bathtub volume is small, the volume of other parameters is small too. For example, as the volume decreases, the heat loss becomes less so that the mass flow of added water decreases correspondingly in the two sub-models.

<!-- b000407 | prose | pages [33, 34] -->
In conclusion, smaller bathtub is a better choice for people in terms of saving more water resource. This can not only decrease the initial water consumption to fill the bathtub but also avoid adding too much hot water afterwards. Of course, it is unwise for taller or fatter people to choose a small bathtub.

<!-- b000408 | furniture | pages [34] -->
Team #44398                                                    Page 34 of 51

<!-- b000410 | heading | pages [34] -->
8.1.2  Different Shapes of Bathtubs

<!-- b000411 | prose | pages [34] -->
When the volume is constant, different shapes of bathtub mainly affect surface area of bath water, influencing heat transfer consequently. So we convert the change of shapes into that of surface area.

<!-- b000412 | prose | pages [34] -->
Usually, there are bathtubs in shapes of round, ellipse, rectangular, heart- shaped, rounded rectangle and so on [18]. We let the perimeter of the section of the bathtub to be C . The area of top surface and other surfaces is 1A and A . 2 The parameters of different shapes of bathtubs are listed as follows.

<!-- b000413 | caption | pages [34] -->
Table 8  The parameters of different shapes

<!-- b000414 | prose | pages [34] -->
1A A Shapes Sketches 2

<!-- b000415 | prose | pages [34] -->
  2 V A  2r Round 1 A 1

<!-- b000416 | prose | pages [34] -->
2V a     b A ab Rectangle 1 A 1

<!-- b000417 | prose | pages [34] -->
4V  A 2 a Square 1 A 1

<!-- b000418 | prose | pages [34] -->
V C Rounded  A   2r ab 1 A rectangle 1

<!-- b000419 | prose | pages [34] -->
Recalling on the average inequality, we have

<!-- b000420 | prose | pages [34, 35] -->
  2 A     2 A 4 A 2 a 1 （45）   1 1  a  So the perimeter of rectangle is the largest while that of square being smaller and that of circle being the smallest. We assume the volume to be 280L A  2 1.05m and the area of the top surface . The value of other parameters are 1 shown in the following table.

<!-- b000421 | furniture | pages [35] -->
Team #44398                                                    Page 35 of 51

<!-- b000423 | caption | pages [35] -->
Table 9  The value of other parameters

<!-- b000424 | prose | pages [35] -->
 A q q 2T Shapes Size/m 2 m1 m2 q r  0.578 Round 2.02 0.0293 0.5565 227.7 39.76   a 1.5, b 0.7 Rectangle I 2.22 0.0295 0.5568 231.5 39.45 1 1   a 1.7, b 0.62 Rectangle II 2.29 0.0296 0.5569 232.8 39.34 2 2 a  1.025 Square 2.14 0.0294 0.5567 230.0 39.57    a 1.2, b 0.7, r 0.05 Rounded rectangle 2.15 0.0294 0.5567 230.2 39.56

<!-- b000425 | prose | pages [35] -->
As the rounded rectangle is the most commonly shape of bathtubs, we choose it as the basic bathtub. Comparing it with other shapes, we derive the variation as follows.

<!-- b000426 | caption | pages [35] -->
Table 10  The variation compared to other shapes

<!-- b000427 | prose | pages [35] -->
Rounded rectangle Shapes Rectangle I Rectangle II Square Round

<!-- b000428 | prose | pages [35] -->
A 0.00% 3.26% 6.39% -0.47% -6.05% 2  0.00% 0.58% 1.14% -0.08% -1.08% q q 0.00% 0.34% 0.68% 0.00% -0.34% m1 q 0.00% 0.02% 0.04% 0.00% -0.04% m2 2T 0.00% -0.27% -0.53% 0.04% 0.51%

<!-- b000429 | prose | pages [35] -->
and 2T of tubs in different shapes

<!-- b000430 | caption | pages [35] -->
Fig.17  The value of

<!-- b000431 | prose | pages [35, 36] -->
q 1A and From the above data, we conclude when the area of top surface volume V are given, the area of side surface A in round bathtub is the smallest 2 among different shapes. So the heat loss of bathtubs in round shape is the smallest. On the contrary, the area of side surface and heat loss of rectangle bathtubs are a b / the largest. As for rectangle bathtubs, if the ratio of length to width becomes lager, the area of side surface will consequently increase, leading to the rise of heat loss. So that square bathtub is better than rectangle one in consideration of heat loss.

<!-- b000432 | furniture | pages [36] -->
Team #44398                                                    Page 36 of 51

<!-- b000434 | prose | pages [36] -->
In conclusion, with regard to heat transfer, the round bathtub is best to choose while the square and rounded rectangle bathtub is less recommended. The rectangle bathtub is the least to choose.

<!-- b000435 | prose | pages [36] -->
In reality, however, the rounded rectangle bathtubs are more common instead of round bathtubs. That is because of the shape of human body and space of the bathroom. A round bathtub will cover more area in a bathroom.

<!-- b000436 | heading | pages [36] -->
8.2  The Influence of Person in Bathtub

<!-- b000437 | prose | pages [36] -->
To some extent, our model may be affected by the difference of people in a bathtub and motions they make. So it is necessary for us to investigate their influence further.

<!-- b000438 | prose | pages [36] -->
In consideration of our goal to avoid wasting too much water, we assume the bathtub is not completely filled with hot water before the person comes into it.

<!-- b000439 | heading | pages [36] -->
8.2.1  When the Person Remains Static in a Bathtub

<!-- b000440 | prose | pages [36] -->
Recalling on our biologic knowledge, human beings are warm-blooded animals whose average temperature remains around 37℃. The change of 1℃ of average temperature means lot to a person. For example, when the temperature rises to 38℃, the person is diagnosed to have a fever. As for skin of human beings, it is made up of three layers: epidermal, dermis and hypodermis. The epidermal layer contacts directly to surroundings, so its temperature is close to the temperature of the surroundings. However, the temperature inside skins commonly remain around 37℃.

<!-- b000441 | prose | pages [36, 37] -->
To simplify the problem, we firstly assume the person in the bathtub remains stable without any motions. Under this circumstance, the skin transfer heat with bath water. According to convection heat transfer formula, we have  t t f p  = （46） p    1 1  3   A k h   3 3 3  is the heat transfer capacity and A is the average area of where p 3  is the thickness of skin. 3h is the convection heat transfer human skin. 3 pt is the average 3k  is the thermal conductivity of skin. coefficient. temperature of human beings, which is commonly 37℃.

<!-- b000442 | furniture | pages [37] -->
Team #44398                                                    Page 37 of 51

<!-- b000444 | prose | pages [37] -->
pt

<!-- b000445 | prose | pages [37] -->
ft

<!-- b000446 | caption | pages [37] -->
Fig.18  Heat transfer through skin

<!-- b000447 | prose | pages [37] -->
where the orange curve represents the temperature trend.

<!-- b000448 | prose | pages [37] -->
The total heat transfer capacity is   = （47） t s q p

<!-- b000449 | prose | pages [37] -->
Because the person remains static, so the value of is unchanged. As the bathtub is not completely full of hot water, the surface area of bath water will be creased after the person comes into the tub. We let the mass of the person to  and the volume to be m , the density of the person to be V . It is easy be 3 3 3 . V after knowing m and to calculate 3 3 3 With the aid of formulas we get on the above, we can assume the volume to change and then correct it with surface area. Through this we can get the corrected results.

<!-- b000450 | heading | pages [37] -->
8.2.2  When the Person Moves in a Bathtub

<!-- b000451 | prose | pages [37, 38] -->
Theoretically, the motions made by the person obviously affect heat transfer. When the person moves, the hot water will be stirred. So that the natural convection transfers into forced convection where the convection heat transfer coefficient will rise a lot. Meanwhile, the motion of bath water will increase the surface area of convection, leading to more heat loss. According to heat transfer theory, the influence of motion caused by the person can be determined.

<!-- b000452 | furniture | pages [38] -->
Team #44398                                                    Page 38 of 51

<!-- b000454 | heading | pages [38] -->
8.2.3  Results Analysis and Sensitivity Analysis

<!-- b000455 | prose | pages [38] -->
Professor Anand Mani sums up other scientists’ research outcome in his essay [10]. We choose some values from the data in his essay which are listed as follows.

<!-- b000456 | caption | pages [38] -->
Table 11  The value of some parameters

<!-- b000457 | prose | pages [38] -->
Parameters Range Value Unit 2 A m 1.5~2 [11] 1.8 3  mm 2~3 [12] 2.5 3    pc J/ kg K 3300,3800,4200,3300 [13-16] 3800 3    W/ m K 3k 0.3,0.21,0.5*,0.543 [17] 0.3  3 kg / m 1040,1050,1000,1100 1050 3

<!-- b000458 | prose | pages [38] -->
* Combined Conductivity for dermal and epidermal layers.

<!-- b000459 | prose | pages [38] -->
The heat transfer coefficient differs a lot in natural convection and forced convection. We list those coefficients as follows.

<!-- b000460 | caption | pages [38] -->
Table 12  The heat transfer coefficients

<!-- b000461 | prose | pages [38] -->
Types Coefficients Ranges /Values Unit

<!-- b000462 | prose | pages [38] -->
Coefficient of air 1~10

<!-- b000463 | prose | pages [38] -->
Coefficient of water 200~1000 Natural    2 1h W/ m K 10 convection 2h 300 3h 300

<!-- b000464 | prose | pages [38] -->
Coefficient of air 20~100

<!-- b000465 | prose | pages [38] -->
Coefficient of water 1000~1500 Forced    2 W/ m K 1h 60 convection 2h 1100 3h 1100

<!-- b000466 | prose | pages [38] -->
Putting those data into the sub-models, we derive the following results.

<!-- b000467 | furniture | pages [39] -->
Team #44398                                                    Page 39 of 51

<!-- b000468 | caption | pages [39] -->
Table 13  Results of two sub-models

<!-- b000469 | prose | pages [39] -->
Parameters Static Moving Unit  261.24 261.24 W s  238.95 1222.4 W q  925.71 1168.5 W p  1425.9 2652.1 W t q 0.0854 0.1588 kg/s m 1 q kg/s 0.6314 0.7293 m 2 1T 3 3 min T 13.63 7.33 min 2 T 16.63 10.33 min

<!-- b000470 | prose | pages [39] -->
The sub-models are heavily affected in consideration of person. The mass flow rises because more hot water is needed. The time of iteration becomes shorter, wasting more water resource. When the person moves in the bathtub, his /her motions will lead to forced convection. This will decrease the thermal resistance so that more heat will be lost. In conclusion, the more frequent and fiercer the motions are, the more hot water will be wasted.

<!-- b000471 | prose | pages [39] -->
Then we conduct sensitivity analysis to determine the relationship between the convection heat transfer coefficient and individual motions. Still, the relationship of volume of the person and the convection heat transfer area.

<!-- b000472 | prose | pages [39] -->
At first, we assume the personal mass to be 60 kg and the volume of the     2% 5% 8% 12% bathtub to be 320 L. Changing the mass by , , , and  15% , we can get the variation as follows.

<!-- b000473 | caption | pages [39] -->
Table 14  The variation of parameters over mass

<!-- b000474 | prose | pages [39, 40] -->
 m 2T q q 3 q m 1 m 2 -15.00% -0.22% 0.18% -0.18% -0.03% -12.00% -0.17% 0.14% -0.14% -0.03% -8.00% -0.12% 0.09% -0.09% -0.02% -5.00% -0.07% 0.06% -0.06% -0.01% -2.00% -0.03% 0.02% -0.02% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2.00% 0.03% -0.02% 0.02% 0.00% 5.00% 0.07% -0.06% 0.06% 0.01% 8.00% 0.12% -0.09% 0.09% 0.02% 12.00% 0.17% -0.14% 0.14% 0.03% 15.00% 0.22% -0.18% 0.18% 0.03% From the above figure, we find the heat transfer capacity and mass flow of added water are both in proportion to the personal mass. That is to say, those two parameters are positively correlated to personal volume while the volume of added water is negatively correlated to personal volume.

<!-- b000475 | furniture | pages [40] -->
Team #44398                                                    Page 40 of 51

<!-- b000477 | prose | pages [40] -->
To show the relationship more vividly, we draw the variations in the following figure.

<!-- b000478 | prose | pages [40] -->
and 2T

<!-- b000479 | caption | pages [40] -->
Fig.19  The variation of

<!-- b000480 | prose | pages [40] -->
q

<!-- b000481 | prose | pages [40] -->
q q

<!-- b000482 | caption | pages [40] -->
Fig.20  The variation of

<!-- b000483 | prose | pages [40] -->
and m 1 m 2

<!-- b000484 | prose | pages [40, 41] -->
We can find the change of those parameters to be relatively small, which indicates the personal volume affects minutely to the model. However, we ignore one factor: the contact area of the person and bath water. In order to conduct sensitivity analyze, we assume the contact area as a constant. Due to the limit of time, we do not investigate its influence further. But we deduce the area is positively correlated to personal volume.

<!-- b000485 | furniture | pages [41] -->
Team #44398                                                    Page 41 of 51

<!-- b000487 | prose | pages [41] -->
In conclusion, if the personal mas and volume are small, the water consumption is small.

<!-- b000488 | prose | pages [41] -->
At last, we analyze the influence of personal motions. Because the motions   2% 5% mainly affect convection heat transfer coefficient, we change it by , ,    8% 12% 15% , and . The results is listed as follows.

<!-- b000489 | caption | pages [41] -->
Table 15  The variation of parameters

<!-- b000490 | prose | pages [41] -->
 3h 2T q q m 1 m 2 q

<!-- b000491 | prose | pages [41] -->
-15.00% -8.21% 8.00% -7.40% -2.15%

<!-- b000492 | prose | pages [41] -->
-12.00% -6.55% 6.27% -5.90% -1.71%

<!-- b000493 | prose | pages [41] -->
-8.00% -4.35% 4.08% -3.92% -1.14%

<!-- b000494 | prose | pages [41] -->
-5.00% -2.71% 2.51% -2.44% -0.71%

<!-- b000495 | prose | pages [41] -->
-2.00% -1.08% 0.98% -0.98% -0.28%

<!-- b000496 | prose | pages [41] -->
0.00% 0.00% 0.00% 0.00% 0.00%

<!-- b000497 | prose | pages [41] -->
2.00% 1.08% -0.96% 0.97% 0.28%

<!-- b000498 | prose | pages [41] -->
5.00% 2.69% -2.37% 2.42% 0.70%

<!-- b000499 | prose | pages [41] -->
8.00% 4.29% -3.73% 3.87% 1.12%

<!-- b000500 | prose | pages [41] -->
12.00% 6.42% -5.47% 5.79% 1.68%

<!-- b000501 | prose | pages [41] -->
15.00% 8.01% -6.74% 7.22% 2.10%

<!-- b000502 | prose | pages [41] -->
From the above data, we conclude the convection heat transfer coefficient affects the model heavily, especially for the first sub-model. This indicates the stability of the second sub-model is better with less change based on the surroundings. Like before, we list the variation of parameters as follows.

<!-- b000503 | furniture | pages [42] -->
Team #44398                                                    Page 42 of 51

<!-- b000504 | prose | pages [42] -->
and 2T

<!-- b000505 | caption | pages [42] -->
Fig. 21  The variation of

<!-- b000506 | prose | pages [42] -->
q

<!-- b000507 | prose | pages [42] -->
q q

<!-- b000508 | caption | pages [42] -->
Fig.22  The variation of

<!-- b000509 | prose | pages [42] -->
and m 1 m 2

<!-- b000510 | prose | pages [42] -->
We find the mass flow in two sub-models is positively correlated to heat transfer coefficient. The mass flow of added water in the first sub-model is affected minutely by the change of heat transfer coefficient. However, the mass flow in the second sub-model is affected heavily by the change. So we deduce if the person in a bathtub moves more fiercely, he/she will have to add more hot water to reheat the bath water.

<!-- b000511 | heading | pages [42] -->
8.3  The Influence of Bubble Bath Additives

<!-- b000512 | prose | pages [42] -->
According to thermodynamics knowledge, a factor can influence heat transfer in two opposite ways: adding heat transfer or decreasing heat transfer. The bubbles made by a bubble bath additive often float on the bath water.

<!-- b000513 | furniture | pages [43] -->
Team #44398                                                    Page 43 of 51

<!-- b000514 | prose | pages [43] -->
Because the thermal conductivity of bubbles is little, those bubbles can be seen as a thermal insulation layer added between bath water and air. This layer restricts the direct convection of air and bath water so it brings about heat preservation. That indicates we can add bubble bath additives to decrease the amount of added hot water.

<!-- b000515 | prose | pages [43] -->
, the thermal conductivity We let the thickness of layer of bubbles to be 4 4k , the convection heat transfer coefficient of the top surface of bubbles to be h of bubbles and air to be and that of the bottom of bubbles and bath water 4L h to be . This analysis can be better understood by the following figure. 4H

<!-- b000516 | caption | pages [43] -->
Fig.23  The sketch of bubbles affecting heat transfer

<!-- b000517 | prose | pages [43] -->
Here we analyze from two points: on one hand, the bubbles restrict the evaporation heat transfer. We assume the evaporation heat transfer decrease to 10%. On the other hand, adding bubbles adds a heat transfer process between the air and hot water. Recalling on our before analysis, the top surface is the main surface to lose heat. So covering bubbles on the top surface will decrease the heat loss heavily.

<!-- b000518 | prose | pages [43] -->
Based on thermodynamic knowledge, the convection heat transfer capacity is  t t   = f （48） 4    1 1 1   4   A h k h   4 4 L 4 4 H

<!-- b000519 | prose | pages [43] -->
Then we correct the heat transfer capacity and then put corrected results into sub-models. We derive the value of parameters listed in the following table.

<!-- b000520 | furniture | pages [44] -->
Team #44398                                                    Page 44 of 51

<!-- b000521 | caption | pages [44] -->
Table 16  The value of parameters

<!-- b000522 | prose | pages [44] -->
Parameters Value Unit ft ℃ 43 t ℃ 25 s  23.2 W 2 4A m 1.05  0.03 m 2    2 h W/ m K 300,1100 4L    2 h W/ m K 10,60 4H    4k W/ m K 0.3

<!-- b000523 | prose | pages [44] -->
In consideration of the person in bathtub, we correct the above data. To show the influence of bubbles vividly, we compare the results with and without adding bubbles.

<!-- b000524 | caption | pages [44] -->
Table 17  Comparison of adding bubbles and no bubbles

<!-- b000525 | prose | pages [44] -->
Natural convection Forced convection Parameters Change Change Adding No Adding No bubbles bubbles bubbles bubbles  1061.8 1164.7 8.83% 1376.7 2390.9 42.42% q 2T 17.87 13.63 -31.11% 13.86 7.33 -89.09% q 0.065 0.085 23.53% 0.084 0.159 47.17% m 1 q 0.604 0.631 4.28% 0.630 0.729 13.58% m 2

<!-- b000526 | prose | pages [44] -->
From the above table, we find bubbles affect heat transfer heavily. They can not only decrease the heat transfer capacity, but also save hot water. Comparing the two sub-models, the change of parameters in the second sub- model is larger. That indicates the second sub-model is more sensitive to bubbles.

<!-- b000527 | prose | pages [44] -->
In conclusion, adding bubble bath additives can slow down the process of bath water becoming cooler and avoid wasting too much water.

<!-- b000528 | heading | pages [44] -->
8.4  The Influence of Radiation Heat Transfer

<!-- b000529 | prose | pages [44] -->
In our before discussion, we ignore the influence of radiation heat transfer because we assume it to be very small to simplify our model. Now it is time for us to investigate the validity of this assumption.

<!-- b000530 | prose | pages [44, 45] -->
According to Stefan-Boltzmann law, we have   4 4       t 273.15 t 273.15     AC f   （49）     0 1 0  100   100     

<!-- b000531 | furniture | pages [45] -->
Team #44398                                                    Page 45 of 51

<!-- b000533 | prose | pages [45] -->
Because only the top surface of bath water contacts directly with air, so we just take the top surface into consideration. Putting the parameters into formula  70W (49), we derive the approximate value . In reality, when a person takes bath in a bathtub, the total heat transfer capacity is 2652W. the variation of radiation heat transfer is merely 2.64% so that it can be ignored. That indicates the rationality of our assumption.

<!-- b000534 | heading | pages [45] -->
8.5  Conclusion

<!-- b000535 | prose | pages [45] -->
After having corrected our model and determined the influence of possible influencing factors, we finally propose our strategy for the user of bathtub to adopt. From point of

<!-- b000536 | caption | pages [45] -->
Table 18   Results under different situations

<!-- b000537 | prose | pages [45] -->
q T Situation Sub-model Water consumption* m 2

<!-- b000538 | prose | pages [45] -->
I 0.014 85.18 Ideal 1.64h II 0.61 109.8 I 0.03 86.40 Evaporation 45min II 0.63 113.4 I 0.029 74.40 Shape 39.76min II 0.557 100.3 I 0.0854 85.21 Static 13.63min II 0.6314 113.6 I 0.1588 98.42 Moving 7.33min II 0.7293 131.3 I 0.084 84.97 Bubbles 13.86min II 0.630 113.4

<!-- b000539 | prose | pages [45] -->
* water consumption is the amount of water during an iteration.

<!-- b000540 | heading | pages [45] -->
9  Further Discussion

<!-- b000541 | prose | pages [45] -->
In this part, we will focus on different distribution of inflow faucets. Then we discuss about the real-life application of our model.

<!-- b000542 | heading | pages [45] -->
9.1  Different Distribution of Inflow Faucets

<!-- b000543 | prose | pages [45] -->
In our before discussion, we assume there being just one entrance of inflow.

<!-- b000544 | furniture | pages [46] -->
Team #44398                                                    Page 46 of 51

<!-- b000545 | prose | pages [46] -->
From the simulating outcome, we find the temperature of bath water is hardly even. So we come up with the idea of adding more entrances.

<!-- b000546 | prose | pages [46] -->
The simulation turns out to be as follows

<!-- b000547 | prose | pages [46] -->
(a) One entrance                (b) Two entrance

<!-- b000548 | prose | pages [46] -->
(c) Five entrance        (d) The whole side as entrance

<!-- b000549 | caption | pages [46] -->
Fig.24  The simulation results of different ways of arranging entrances

<!-- b000550 | prose | pages [46] -->
From the above figure, the more the entrances are, the evener the temperature will be. Recalling on the before simulation outcome, when there is only one entrance for inflow, the temperature of corners is quietly lower than the middle area.

<!-- b000551 | prose | pages [46] -->
In conclusion, if we design more entrances, it will be easier to realize the goal to keep temperature even throughout the bathtub.

<!-- b000552 | heading | pages [46] -->
9.2  Model Application

<!-- b000553 | prose | pages [46] -->
Our before discussion is based on ideal assumptions. In reality, we have to make some corrections and improvement.

<!-- b000554 | prose | pages [46, 47] -->
 Adding hot water continually with the mass flow of 0.16 kg/s. This way can ensure even mean temperature throughout the bathtub and waste less water.

<!-- b000555 | furniture | pages [47] -->
Team #44398                                                    Page 47 of 51

<!-- b000557 | prose | pages [47] -->
 The manufacturers can design an intelligent control system to monitor the temperature so that users can get more enjoyable bath experience.

<!-- b000558 | prose | pages [47] -->
 We recommend users to add bubble additives to slow down the water being cooler and help cleanse. The additives with lower thermal conductivity are optimal.

<!-- b000559 | prose | pages [47] -->
 The study method of our establishing model can be applied in other area relative to convection heat transfer, such as air conditioners.

<!-- b000560 | heading | pages [47] -->
10  Strength and Weakness

<!-- b000561 | heading | pages [47] -->
10.1  Strength

<!-- b000562 | prose | pages [47] -->
 We analyze the problem based on thermodynamic formulas and laws, so that the model we established is of great validity.

<!-- b000563 | prose | pages [47] -->
 Our model is fairly robust due to our careful corrections in consideration of real-life situations and detailed sensitivity analysis.

<!-- b000564 | prose | pages [47] -->
 Via Fluent software, we simulate the time field of different areas throughout the bathtub. The outcome is vivid for us to understand the changing process.

<!-- b000565 | prose | pages [47] -->
 We come up with various criteria to compare different situations, like water consumption and the time of adding hot water. Hence an overall comparison can be made according to these criteria.

<!-- b000566 | prose | pages [47] -->
 Besides common factors, we still consider other factors, such as evaporation and radiation heat transfer. The evaporation turns out to be the main reason of heat loss, which corresponds with other scientist’s experimental outcome.

<!-- b000567 | heading | pages [47] -->
10.2  Weakness

<!-- b000568 | prose | pages [47] -->
 Having knowing the range of some parameters from others’ essays, we choose a value from them to apply in our model. Those values may not be reasonable in reality.

<!-- b000569 | furniture | pages [48] -->
Team #44398                                                    Page 48 of 51

<!-- b000570 | prose | pages [48] -->
 Although we investigate a lot in the influence of personal motions, they are so complicated that need to be studied further.

<!-- b000571 | prose | pages [48] -->
 Limited to time, we do not conduct sensitivity analysis for the influence of personal surface area.

<!-- b000572 | prose | pages [49] -->
Report

<!-- b000573 | furniture | pages [49] -->
Team #44398                                                    Page 49 of 51

<!-- b000574 | prose | pages [49] -->
Suggestions

<!-- b000575 | prose | pages [49] -->
In order to enjoy a comfortable bath with even temperature of bath water and without wasting too much water, we propose the following suggestions.

<!-- b000576 | prose | pages [49] -->
Adding hot water consistently

<!-- b000577 | prose | pages [49] -->
Using smaller bathtub if possible

<!-- b000578 | prose | pages [49] -->
Decreasing motions during bath

<!-- b000579 | prose | pages [49] -->
Using bubble bath additives

<!-- b000580 | prose | pages [49] -->
Decreasing motions during bath Arranging more faucets of inflow

<!-- b000581 | heading | pages [49] -->
From simulation results of

<!-- b000582 | prose | pages [49] -->
real-life situations, we find it takes

<!-- b000583 | prose | pages [49] -->
a period of time for the inflow hot

<!-- b000584 | prose | pages [49] -->
water to spread throughout the

<!-- b000585 | prose | pages [49] -->
bathtub. During this process, the

<!-- b000586 | prose | pages [49] -->
bath water continues transferring

<!-- b000587 | prose | pages [49] -->
heat into air, bathtub and the

<!-- b000588 | prose | pages [49] -->
person in bathtub. The difference

<!-- b000589 | prose | pages [49] -->
between heat transfer capacity

<!-- b000590 | prose | pages [49] -->
makes the temperature of various

<!-- b000591 | prose | pages [49] -->
areas to be different. So that it is

<!-- b000592 | prose | pages [49] -->
difficult to get an evenly main-

<!-- b000593 | prose | pages [49] -->
tained temperature throughout the

<!-- b000594 | prose | pages [49] -->
bath water.

<!-- b000595 | furniture | pages [50] -->
Team #44398                                                    Page 50 of 51

<!-- b000596 | heading | pages [50] -->
Reference

<!-- b000597 | references | pages [50] -->
[1] Gi-Beum Kim. Change of the Warm Water Temperature for the

<!-- b000598 | references | pages [50] -->
Development of Smart Healthecare Bathing System. Hwahak konghak. 2006,

<!-- b000599 | references | pages [50] -->
44(3): 270-276.

<!-- b000600 | references | pages [50] -->
[2] https://en.wikipedia.org/wiki/Convective_heat_transfer#Newton.27s_law

<!-- b000601 | references | pages [50] -->
_of_cooling

<!-- b000602 | references | pages [50] -->
[3] https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations

<!-- b000603 | references | pages [50] -->
[4] https://en.wikipedia.org/wiki/Computational_fluid_dynamics

<!-- b000604 | references | pages [50] -->
[5] Holman J P. 2002. Heat Transfer (9th ed.) New York: McGraw-Hill.

<!-- b000605 | references | pages [50] -->
[6] http://www.czs.gov.cn/html/zwgk/ztbd/ggfw/10265/10552/10565/10595/co

<!-- b000606 | references | pages [50] -->
ntent_393852.html

<!-- b000607 | references | pages [50] -->
[7] http://www.kankanews.com/IClux/1353641549/2014-01-08/3645040.shtml

<!-- b000608 | references | pages [50] -->
[8] W. M. Kays, M. E. Crawford, B. Weigand. Convective Heat and Mass

<!-- b000609 | references | pages [50] -->
Fransfer

<!-- b000610 | references | pages [50] -->
[9] Shimodozono, Megumi；Matsumoto, Shuji；Ninomiya, Koji；Miyata, Ryuji；

<!-- b000611 | references | pages [50] -->
Ogata, Atsuko；Etoh, Seiji；Watanabe, Satoshi；Kawahira, Kazumi. Acute

<!-- b000612 | references | pages [50] -->
effects of a single warm-water bath on serum adiponectin and leptin levels

<!-- b000613 | references | pages [50] -->
in healthy men: A pilot study. International Journal of Biometeorology. 2012,

<!-- b000614 | references | pages [50] -->
56(5): 933-939.

<!-- b000615 | references | pages [50] -->
[10] Anand Mani. Critical Evaluation of Current Skin Thermal Property

<!-- b000616 | references | pages [50] -->
Measurements.

<!-- b000617 | references | pages [50] -->
[11] Bennett, Howard (2014-05-25). "Ever wondered about your skin?". The

<!-- b000618 | references | pages [50] -->
Washington Post. Retrieved 2014-10-27.

<!-- b000619 | references | pages [50] -->
[12] https://en.wikipedia.org/wiki/Human_skin#cite_note-Bennett-8

<!-- b000620 | references | pages [50] -->
[13] Wang, Yunjian, Zhu Liang, Rosengart, Axel J. Targeted brain hypothermia

<!-- b000621 | references | pages [50] -->
induced by an interstitial cooling device in the rat neck: Experimental study

<!-- b000622 | references | pages [50] -->
and model validation. International Journal of Heat and Mass Transfer.

<!-- b000623 | references | pages [50] -->
2008(51): 5662-5670.

<!-- b000624 | references | pages [50] -->
[14] Yang, Yang. Liu, Jing.Detection of Athersclerosis Through Mapping Skin

<!-- b000625 | references | pages [50] -->
Temperature Variation Caused by Carotid Atherosclerosis Plaques. Journal

<!-- b000626 | references | pages [50] -->
of Thermal Science and Engineering Applications. 2011(3).

<!-- b000627 | references | pages [50] -->
[15] Diller, K.R. and Hayes, J.L. A Finite Element Model of burn injury in blood

<!-- b000628 | references | pages [50] -->
perfused skin. Journal of Biomechanical Engineering. 1983(105): 300-307.

<!-- b000629 | references | pages [50] -->
[16] Mattix, Steven. Using skin heat transfer anisotropy as a diagnostic tool:

<!-- b000630 | furniture | pages [51] -->
Team #44398                                                    Page 51 of 51

<!-- b000631 | references | pages [51] -->
Measurement of Skin Thermal Properties. 2010.

<!-- b000632 | references | pages [51] -->
[17] Kenneth R. Holmes. Thermal Conductivity Data for Specific Tissues and

<!-- b000633 | references | pages [51] -->
Organs for Humans and other Mammalian Species.

<!-- b000634 | references | pages [51] -->
[18] http://www.oppein.cn/news/3430

<!-- b000635 | references | pages [51] -->
[19] Cohen Myron, L. Measurement of the thermal properties of human skin. A

<!-- b000636 | references | pages [51] -->
Review. Journal of Investigative Dermatology, 69, 333-338.
