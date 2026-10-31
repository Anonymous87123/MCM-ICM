# P-A-2016-46830-92f43919

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
46830

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T2 ________________

<!-- b000008 | prose | pages [1] -->
F1 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | title | pages [1] -->
A

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | prose | pages [1] -->
F4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | prose | pages [1] -->
2016 MCM/ICM

<!-- b000019 | heading | pages [1] -->
Summary Sheet

<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | title | pages [1] -->
Keep It Warm

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | heading | pages [1] -->
Summary

<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | prose | pages [1] -->
Do you usually get annoyed with the cooling of water during a relaxing bath? In this paper, several models are proposed to solve the problem. Our efforts in building these models followed the path below.

<!-- b000028 | prose | pages [1] -->
Firstly, a universal thermodynamic model(UTM) of bath water is established by constructing two initial sub-equations named the Heat Differential Equation(HDE) and the Temperature Distribution(TD) respectively. Based on Fourier's law, the Stefan-Boltzmann law and the first law of thermodynamics, HDE is established, which also takes heat conduction, heat radiation and evaporation of water into account. Moreover, we get the numerical solution of TD by using the PDE tool of MATLAB, and fit its temperature distribution surface by the plane equation, whose goodness of fit is 0.931. The fitting equation is regarded as the approximate analytical solution.

<!-- b000029 | prose | pages [1] -->
Secondly, taking convection caused by human movement and comfort of water temperature into account, we developed an optimization control model for the bath strategy (OCM) based on UTM, which aims at the smallest water injection, the best temperature stability & the highest comfort level. We use the model(OCM) to optimize the two following

<!-- b000030 | prose | pages [1] -->
strategies：i. Injecting hot water constantly at a certain flow; ii. Injecting hot water when

<!-- b000031 | prose | pages [1] -->
and stopping injecting when temperature increase to temperature declines to T min1 . In T min 2

<!-- b000032 | prose | pages [1] -->
0.007L s strategy I, the optimal conditions are that the flow is and the temperature of  1

<!-- b000033 | prose | pages [1] -->
water injection is 311.1K. The optimization proves efficient after extensive discussion; In strategy II, the upper and lower critical temperature and the temperature of water injection are

<!-- b000034 | prose | pages [1] -->
311.7K，311.7K & 313.1K respectively. It means that the hot water injection is a continuous

<!-- b000035 | prose | pages [1] -->
process.

<!-- b000036 | prose | pages [1] -->
Thirdly, we modify UTM with the actual situation of bubble water to analyze the influence of bubble water towards the optimization, concluding that the heat dissipating power of bubble water is 45.85% of that of normal hot water at 312K. By OCM, we get the 0.004L s and the temperature of water injection is 311.9K , optimal conditions as the flow is  1

<!-- b000037 | prose | pages [1] -->
which shows that the efficiency of bubble water exceed greatly that of normal hot water.

<!-- b000038 | prose | pages [1] -->
Finally, we made error analysis of the factors like external environment etc. and did stability analysis of the geometric parameters of the bathtub & the parameters of human body. The sensitivities of the factors prove the models to be feasible and applicable.

<!-- b000039 | furniture | pages [1] -->


<!-- b000040 | furniture | pages [1] -->


<!-- b000041 | furniture | pages [1] -->


<!-- b000042 | furniture | pages [2] -->
Team #46830

<!-- b000043 | furniture | pages [2] -->


<!-- b000044 | furniture | pages [2] -->


<!-- b000045 | furniture | pages [2] -->
Page 1 of 45

<!-- b000046 | heading | pages [2] -->
Contents

<!-- b000047 | contents | pages [2] -->
1    Introduction .................................................................................................. 1

<!-- b000048 | contents | pages [2] -->
1.1 Restatement of the Problem ..................................................................... 1

<!-- b000049 | contents | pages [2] -->
1.2 Our Approach ........................................................................................... 1

<!-- b000050 | contents | pages [2] -->
2    Assumptions with Justifications .................................................................. 2

<!-- b000051 | contents | pages [2] -->
2.1 About the Bathroom and Water

<!-- b000052 | contents | pages [2] -->
below.

<!-- b000053 | contents | pages [2] -->
Fir

<!-- b000054 | contents | pages [2] -->
-

<!-- b000055 | contents | pages [2] -->
Temperature Distribution(TD) respectively. Based on Fourier's law, the Stefan-

<!-- b000056 | contents | pages [2] -->
re

<!-- b000057 | contents | pages [2] -->
Do you usually get annoyed with the cooling of water during a relaxing bath? In this followed the path

<!-- b000058 | contents | pages [2] -->
stly, a universal thermodynamic model(UTM) of bath water is established by constructing two initial sub

<!-- b000059 | contents | pages [2] -->
Bol

<!-- b000060 | contents | pages [2] -->
tzmann conduction, heat radiation and evaporation of water into account. Moreover, we get the numerical solution of TD by using the PDE tool of MATLAB, and fit its temperatu

<!-- b000061 | contents | pages [2] -->
distribution surface by the plane equation, whose goodness of fit is 0.931. The fitting equation is regarded as the approximate analytical solution .

<!-- b000062 | contents | pages [2] -->
Secondly, taking convection caused by human movement and comfort of water temperature into account, we developed an optimization control model for the bath strategy

<!-- b000063 | contents | pages [2] -->
stability & the highest comfort level. We use the model(OCM) to optimize the two following strategies

<!-- b000064 | contents | pages [2] -->
temperature declines to

<!-- b000065 | contents | pages [2] -->
：i

<!-- b000066 | contents | pages [2] -->
.......................... strategy I, the

<!-- b000067 | contents | pages [2] -->
optimal conditions are that the flow is

<!-- b000068 | furniture | pages [2] -->


<!-- b000069 | contents | pages [2] -->
and the temperature of 311.1K

<!-- b000070 | contents | pages [2] -->
strategy II, the upper and lower critical temperature and the temperature

<!-- b000071 | contents | pages [2] -->
311.7K

<!-- b000072 | contents | pages [2] -->
respectively. It means that the hot water injection is a continuous

<!-- b000073 | contents | pages [2] -->
45.85%

<!-- b000074 | contents | pages [2] -->
311.7K，

<!-- b000075 | contents | pages [2] -->
&

<!-- b000076 | contents | pages [2] -->
313.1K

<!-- b000077 | contents | pages [2] -->
Thirdly, we modify UTM with the actual situation of bubble water to analyze the influence of bubble water towards the optimization, concluding that the heat diss power of bubble water is

<!-- b000078 | contents | pages [2] -->
of that of normal hot water at 312K

<!-- b000079 | contents | pages [2] -->
optimal conditions as the flow is

<!-- b000080 | contents | pages [2] -->
,

<!-- b000081 | furniture | pages [2] -->


<!-- b000082 | contents | pages [2] -->
and the temperature of water injection is

<!-- b000083 | contents | pages [2] -->
which shows that the efficiency of bubble water exceed greatly that of normal hot water .

<!-- b000084 | contents | pages [2] -->
stability analysis of the geometric parameters of the bathtub & the parameters of human body. The sensitivities of the factors pro

<!-- b000085 | contents | pages [2] -->
ve the models to be feasible and applicable. ........................................ 20

<!-- b000086 | contents | pages [2] -->
4.3.2 Solution of human body comfort model ..................................... 21

<!-- b000087 | contents | pages [2] -->
4.4 Optimized control model of bathing strategy ........................................ 22

<!-- b000088 | contents | pages [2] -->
4.4.1 Strategy I ..................................................................................... 23

<!-- b000089 | contents | pages [2] -->
4.4.2 Strategy II.................................................................................... 25

<!-- b000090 | contents | pages [2] -->
4.4.3 Solution of the optimal control models of strategy I & II........... 27

<!-- b000091 | contents | pages [2] -->
4.5 Bubble bath ............................................................................................ 31

<!-- b000092 | contents | pages [2] -->
4.5.1 The effect of bubble water .......................................................... 31

<!-- b000093 | contents | pages [2] -->
4.5.2 Effect of bubble water on optimal control strategy..................... 32

<!-- b000094 | contents | pages [2] -->
5    Testing the Model....................................................................................... 34

<!-- b000095 | contents | pages [2] -->
5.1 Error Analysis ........................................................................................ 34

<!-- b000096 | contents | pages [2] -->
5.1.1 Various factors of external environment ..................................... 34

<!-- b000097 | contents | pages [2] -->
5.1.2 Various factors of water .............................................................. 35

<!-- b000098 | contents | pages [2] -->
5.1.3 Various factors of human ............................................................ 35

<!-- b000099 | contents | pages [2] -->
5.1.4 Error in modeling and solving process ....................................... 35

<!-- b000100 | contents | pages [2] -->
5.2 Sensitivity Analysis................................................................................ 36

<!-- b000101 | contents | pages [2] -->
5.2.1 Sensitivity to the shape and volume of the tub ........................... 37

<!-- b000102 | contents | pages [2] -->
5.2.2 Sensitivity to the human parameters ........................................... 37

<!-- b000103 | contents | pages [2] -->
5.2.3 Sensitivity to the heat transfer rate.............................................. 38

<!-- b000104 | contents | pages [2] -->
6    Conclusions ................................................................................................ 38

<!-- b000105 | contents | pages [2] -->
6.1 Strengths and Weaknesses...................................................................... 38

<!-- b000106 | contents | pages [2] -->
6.1.1 Strengths...................................................................................... 38

<!-- b000107 | contents | pages [2] -->
6.1.2 Weaknesses ................................................................................. 39

<!-- b000108 | contents | pages [2] -->
6.2 Comprehensive Results.......................................................................... 39

<!-- b000109 | furniture | pages [2] -->


<!-- b000110 | furniture | pages [3] -->
Team #46830

<!-- b000111 | furniture | pages [3] -->


<!-- b000112 | furniture | pages [3] -->
Page 2 of 45

<!-- b000113 | furniture | pages [3] -->


<!-- b000114 | contents | pages [3] -->
6.3 Future Work ........................................................................................... 40

<!-- b000115 | contents | pages [3] -->
7    Explanation ................................................................................................ 41

<!-- b000116 | contents | pages [3] -->
References ............................................................................................................ 42

<!-- b000117 | furniture | pages [3] -->


<!-- b000118 | furniture | pages [3] -->


<!-- b000119 | furniture | pages [3] -->


<!-- b000120 | furniture | pages [3] -->


<!-- b000121 | furniture | pages [3] -->


<!-- b000122 | furniture | pages [3] -->


<!-- b000123 | furniture | pages [3] -->


<!-- b000124 | furniture | pages [3] -->


<!-- b000125 | furniture | pages [3] -->


<!-- b000126 | furniture | pages [3] -->


<!-- b000127 | furniture | pages [3] -->


<!-- b000128 | furniture | pages [3] -->


<!-- b000129 | furniture | pages [3] -->


<!-- b000130 | furniture | pages [3] -->


<!-- b000131 | furniture | pages [3] -->


<!-- b000132 | furniture | pages [3] -->


<!-- b000133 | furniture | pages [3] -->


<!-- b000134 | furniture | pages [4] -->
Team #46830

<!-- b000135 | furniture | pages [4] -->


<!-- b000136 | furniture | pages [4] -->
Page 1 of 45

<!-- b000137 | furniture | pages [4] -->


<!-- b000138 | heading | pages [4] -->
1    Introduction

<!-- b000139 | heading | pages [4] -->
1.1 Restatement of the Problem

<!-- b000140 | prose | pages [4] -->
Taking a bath, can remove dirt, eliminate fatigue, promote blood circulation,

<!-- b000141 | prose | pages [4] -->
improve sleep quality, and enhance metabolism. And by soaking in warm water, one

<!-- b000142 | prose | pages [4] -->
can treat certain diseases and combat bacterium in some degrees.

<!-- b000143 | prose | pages [4] -->
The problem needs us to develop a mathematical model to finding out the best

<!-- b000144 | prose | pages [4] -->
bathing strategy depends on the shape/volume of the tub, and the parameters and the

<!-- b000145 | prose | pages [4] -->
motions of the person in the bathtub. This model aims at keeping the temperature even throughout the bathtub and as close as possible to the initial temperature without

<!-- b000146 | prose | pages [4] -->
wasting too much water.

<!-- b000147 | prose | pages [4] -->
We need consider the following: ·Build a thermodynamic model of water in tub to describe the temperature in

<!-- b000148 | prose | pages [4] -->
space and time in the following processes:

<!-- b000149 | prose | pages [4] -->
i. The process of filling the tub with hot water;

<!-- b000150 | prose | pages [4] -->
ii. The natural cooling process of water;

<!-- b000151 | prose | pages [4] -->
iii. The process of adding hot water. ·Consider the influences of the motions of people in tub, and analyze the results

<!-- b000152 | prose | pages [4] -->
of this influences. We need to deal with the obstacle caused by the convection of

<!-- b000153 | prose | pages [4] -->
water and the accompanying heat exchange.

<!-- b000154 | prose | pages [4] -->
·Find out the best control strategy to keep the temperature and save water as

<!-- b000155 | prose | pages [4] -->
possible. The strategy depends on the parameters of tub, the degree of human

<!-- b000156 | prose | pages [4] -->
movement, and the parameters of the human body.

<!-- b000157 | prose | pages [4] -->
·Discuss the difference between water and bubble bath water. We shall clarify

<!-- b000158 | prose | pages [4] -->
how the bubble bath water influences the model and the strategy we have given.

<!-- b000159 | prose | pages [4] -->
·We need to provide a one-page non-technical explanation for users of the bathtub that describes our strategy. It shall explain why it is so difficult to get an

<!-- b000160 | prose | pages [4] -->
evenly maintained temperature throughout the bath water and the advice according to our model.

<!-- b000161 | heading | pages [4] -->
1.2 Our Approach

<!-- b000162 | prose | pages [4] -->
We analyzed the problems above and consulted lots of literature, and then come

<!-- b000163 | prose | pages [4] -->
up with the following approaches:

<!-- b000164 | prose | pages [4] -->
·We analyzed the problems above and consulted lots of literature, and then come

<!-- b000165 | prose | pages [4] -->
up with the following approaches:

<!-- b000166 | furniture | pages [4] -->


<!-- b000167 | furniture | pages [5] -->
Team #46830

<!-- b000168 | furniture | pages [5] -->


<!-- b000169 | furniture | pages [5] -->
Page 2 of 45

<!-- b000170 | furniture | pages [5] -->


<!-- b000171 | prose | pages [5] -->
·We build a general thermodynamic model for water bath. This model is based

<!-- b000172 | prose | pages [5] -->
on the Fourier law, the Newton cooling theorem, Stern-boltzmann's law, the heat conduction formula, and the first law of thermodynamics. And it includes:

<!-- b000173 | prose | pages [5] -->
I.Heat exchange between hot water and bathtub

<!-- b000174 | prose | pages [5] -->
II. Heat exchange between hot water and air, III.Evaporation heat absorption of hot water,

<!-- b000175 | prose | pages [5] -->
IV.Heat absorption and heat release of human body, V.Heat radiation of water, VI. Heat of added hot water and heat carried away by the overflow.

<!-- b000176 | prose | pages [5] -->
·We build a distribution model for water in bathtub. This model is mainly based

<!-- b000177 | prose | pages [5] -->
on the heat conduction equation and the Neumann boundary condition. Unfortunately, the model can only be solved by Matlab, and can't get accurate analytic function

<!-- b000178 | prose | pages [5] -->
expression. So we build an approximate analytical model for water temperature distribution.

<!-- b000179 | prose | pages [5] -->
·We build a forced convection model for the water in the bathtub. The motion of

<!-- b000180 | prose | pages [5] -->
human body in the water will be the force of water. And the convection of water accelerates the heat exchange of water. So we quantify human motion, then build a

<!-- b000181 | prose | pages [5] -->
model for forced convection heat exchanging. This model describes the redistribution

<!-- b000182 | prose | pages [5] -->
of the water temperature under the influence of human motion.

<!-- b000183 | prose | pages [5] -->
·We build an optimal control strategy model based on thermodynamics, water

<!-- b000184 | prose | pages [5] -->
temperature distribution and forced convection. The model is mainly based on

<!-- b000185 | prose | pages [5] -->
nonlinear multivariable optimal control, use it to get the optimal control strategy. We will provide two control strategies based on different aspects under this model.

<!-- b000186 | prose | pages [5] -->
·We obtain the thermodynamic model for bubble bath water by improving general thermodynamic model. Based on this model, we discussed the effects of

<!-- b000187 | prose | pages [5] -->
bubble bath water on the distribution and variation of water temperature, then

<!-- b000188 | prose | pages [5] -->
analyzes the influence of the bubble bath water to the optimal control strategy. At the same time, we analyzed the advantages of bubble bath water.

<!-- b000189 | prose | pages [5] -->
·We use the finite difference method to solve the partial differential equations

<!-- b000190 | prose | pages [5] -->
and the piecewise differential equations.

<!-- b000191 | heading | pages [5] -->
2    Assumptions with Justifications

<!-- b000192 | prose | pages [5] -->
We make the following assumptions about the whole process in this paper to obtain a better model result.

<!-- b000193 | furniture | pages [5] -->


<!-- b000194 | furniture | pages [6] -->
Team #46830

<!-- b000195 | furniture | pages [6] -->


<!-- b000196 | furniture | pages [6] -->
Page 3 of 45

<!-- b000197 | furniture | pages [6] -->


<!-- b000198 | heading | pages [6] -->
2.1 About the Bathroom and Water

<!-- b000199 | prose | pages [6] -->
1. Assume that the air temperature and humidity in the bathroom is constant, not due to the Water vapor from man and bathtub. The temperature and humidity

<!-- b000200 | prose | pages [6] -->
distribution of air is affected by many factors, this problem is very difficult. The other

<!-- b000201 | prose | pages [6] -->
reason is that the discussion of air temperature and humidity not mean much.

<!-- b000202 | prose | pages [6] -->
2. Without taking into account the wave generated by the motion of human and

<!-- b000203 | prose | pages [6] -->
the adding of water, as well as the overflow caused by waves. The reason is that the water wave will be reflected back by the Inner wall of bathtub and leads multiple interference, it is very difficult to study this process. In addition, this mechanical

<!-- b000204 | prose | pages [6] -->
process will not have a significant impact on the thermodynamic process of the bathtub-hot water-human system.

<!-- b000205 | prose | pages [6] -->
3. Regardless of the time between the hot water comes out of the tap and enters

<!-- b000206 | prose | pages [6] -->
the bathtub, which means that ignoring heat dissipation of water in the air. The reason is that the setting position of the tab should be as close as possible to the surface of the

<!-- b000207 | prose | pages [6] -->
full water in the bathtub. That means the time for water to stay in the air is so short

<!-- b000208 | prose | pages [6] -->
that the amount of heat dissipation in the air is negligible.

<!-- b000209 | prose | pages [6] -->
4. Natural convection due to temperature gradient is negligible. Consider only

<!-- b000210 | prose | pages [6] -->
the forced convection caused by the movement of the human. Because the

<!-- b000211 | prose | pages [6] -->
temperature gradient of the bath water is not large enough to consider the natural convection of water caused by it.

<!-- b000212 | prose | pages [6] -->
5. The convection of water inside the bath tub does not affect the current water

<!-- b000213 | prose | pages [6] -->
temperature. The reason is that heat exchange caused by convective occurs only between the parts of the water in the bathtub, this process does not get heat exchange

<!-- b000214 | prose | pages [6] -->
from the outside of the system, in other words, only water temperature distribution changed.

<!-- b000215 | prose | pages [6] -->
6. The physical parameters such as the thermal conductivity, density and the

<!-- b000216 | prose | pages [6] -->
bubble thickness are not changed with the addition of hot water and the loss of overflow water. Although the concentration of bubble water is bound to change with

<!-- b000217 | prose | pages [6] -->
the addition and loss of water, the influence of bubble water concentration on other

<!-- b000218 | prose | pages [6] -->
physical parameters is complicated and not clear, and the change of concentration is quite small for some parameters. Therefore, ignore the bubble water physical

<!-- b000219 | prose | pages [6] -->
properties change over time

<!-- b000220 | heading | pages [6] -->
2.2 About the Human Body

<!-- b000221 | prose | pages [6] -->
7. Heat conductivity of human body is the constant value, it do not change with human posture and body temperature. Because the heat absorption and release of the

<!-- b000222 | furniture | pages [6] -->


<!-- b000223 | furniture | pages [7] -->
Team #46830

<!-- b000224 | furniture | pages [7] -->


<!-- b000225 | furniture | pages [7] -->


<!-- b000226 | furniture | pages [7] -->
Page 4 of 45

<!-- b000227 | prose | pages [7] -->
human body is a complex process of biochemical reaction and physical process. Some

<!-- b000228 | prose | pages [7] -->
factors like the metabolic heat generation, human sweat evaporation and the work done by exercise need to be considered. Since the thermodynamic process in the

<!-- b000229 | prose | pages [7] -->
human body is too complicated and difficult to be analyze, considered the human

<!-- b000230 | prose | pages [7] -->
body as a constant temperature heat source (maybe it’s endothermic), its thermal conductivity is a constant value.

<!-- b000231 | prose | pages [7] -->
8. Each part of the body surface temperature is a constant value. Because the distribution of body temperature is difficult to parameterized, and the body temperature of each part is slightly different(around 0.6℃). Consider that all over the

<!-- b000232 | prose | pages [7] -->
body surface, the temperatures are the same constant.

<!-- b000233 | prose | pages [7] -->
9. Ignore the work of the forced convection generated by human motion. As the fluid, water can only work rely on its viscous force, and the viscous force is too small

<!-- b000234 | prose | pages [7] -->
to be taken into account.

<!-- b000235 | prose | pages [7] -->
10. Considered the human motion as a series of discrete motion with the same

<!-- b000236 | prose | pages [7] -->
amplitude and frequency. Although the motions can have a huge impact on the

<!-- b000237 | prose | pages [7] -->
environment, such as the spatial distribution of water temperature, the movement of people is very irregular. So we use a simple physical quantity to describe the intensity

<!-- b000238 | prose | pages [7] -->
and speed of human motion. For the magnitude of the motions, we will discuss it in

<!-- b000239 | prose | pages [7] -->
detail in the 4.2 chapter.

<!-- b000240 | heading | pages [7] -->
3    Notations

<!-- b000241 | prose | pages [7] -->
All the variables and constants used in this paper are listed in Table1 and Table 2.

<!-- b000242 | furniture | pages [7] -->


<!-- b000243 | caption | pages [7] -->
Table 1 Symbol Table–Constants

<!-- b000244 | prose | pages [7] -->
Symbol Definition

<!-- b000245 | prose | pages [7] -->
Air temperature 0T

<!-- b000246 | prose | pages [7] -->
P

<!-- b000247 | prose | pages [7] -->
Value

<!-- b000248 | prose | pages [7] -->
298K

<!-- b000249 | prose | pages [7] -->
Saturated vapor pressure

<!-- b000250 | prose | pages [7] -->
  3 2.4 10 Pa

<!-- b000251 | furniture | pages [7] -->


<!-- b000252 | prose | pages [7] -->
Density of water

<!-- b000253 | prose | pages [7] -->
  3 3 10 kg m

<!-- b000254 | furniture | pages [7] -->


<!-- b000255 | prose | pages [7] -->
Molar mass of water

<!-- b000256 | prose | pages [7] -->
R

<!-- b000257 | prose | pages [7] -->
    3 1 18 10 kg mol

<!-- b000258 | furniture | pages [7] -->


<!-- b000259 | prose | pages [7] -->
Universal gas constant

<!-- b000260 | prose | pages [7] -->
c     1 1 8.31J mol K

<!-- b000261 | furniture | pages [7] -->


<!-- b000262 | prose | pages [7] -->
Specific heat capacity of water

<!-- b000263 | prose | pages [7] -->
      3 1 1 4.2 10 J kg K

<!-- b000264 | furniture | pages [7] -->


<!-- b000265 | prose | pages [7] -->
0.97 Surface radiation coefficient of water

<!-- b000266 | prose | pages [7] -->
 Stefan-Boltzmann constant

<!-- b000267 | furniture | pages [7] -->


<!-- b000268 | prose | pages [7] -->
      8 2 4 5.67 10 W m K

<!-- b000269 | furniture | pages [7] -->


<!-- b000270 | furniture | pages [8] -->
Team #46830

<!-- b000271 | furniture | pages [8] -->


<!-- b000272 | furniture | pages [8] -->


<!-- b000273 | furniture | pages [8] -->


<!-- b000274 | furniture | pages [8] -->
Page 5 of 45

<!-- b000275 | caption | pages [8] -->
Table 2 Symbol Table–Variables

<!-- b000276 | prose | pages [8] -->
Definition Symbol

<!-- b000277 | prose | pages [8] -->
Q

<!-- b000278 | prose | pages [8] -->
Units

<!-- b000279 | prose | pages [8] -->
J Internal energy of the water in the bathtub

<!-- b000280 | prose | pages [8] -->
K Average temperature of water at time t T t ( )

<!-- b000281 | prose | pages [8] -->
J Heat of heat exchange

<!-- b000282 | furniture | pages [8] -->


<!-- b000283 | prose | pages [8] -->
Q exchange

<!-- b000284 | prose | pages [8] -->
J Heat of water evaporation

<!-- b000285 | furniture | pages [8] -->


<!-- b000286 | prose | pages [8] -->
Q evaporation

<!-- b000287 | prose | pages [8] -->
J Heat absorbed by the body

<!-- b000288 | furniture | pages [8] -->


<!-- b000289 | prose | pages [8] -->
Q body

<!-- b000290 | prose | pages [8] -->
J Heat of radiation Q

<!-- b000291 | furniture | pages [8] -->


<!-- b000292 | prose | pages [8] -->
radiation

<!-- b000293 | prose | pages [8] -->
T x y z t ( , , , ) K Distribution of temperature in time and space

<!-- b000294 | prose | pages [8] -->
u T ( ) Water evaporation rate

<!-- b000295 | prose | pages [8] -->
k m s  1

<!-- b000296 | furniture | pages [8] -->


<!-- b000297 | prose | pages [8] -->
Water flow s  3 1 m

<!-- b000298 | furniture | pages [8] -->


<!-- b000299 | prose | pages [8] -->
K The outlet water temperature 0T 

<!-- b000300 | prose | pages [8] -->
m The movement distance of the k th kS

<!-- b000301 | prose | pages [8] -->
The volume distance of the k th V k F 3 m Source of forced convection 4 m

<!-- b000302 | prose | pages [8] -->
Best water flow bk s  3 1 m

<!-- b000303 | furniture | pages [8] -->


<!-- b000304 | prose | pages [8] -->
K The best outlet water temperature bT 

<!-- b000305 | heading | pages [8] -->
4    The Model

<!-- b000306 | prose | pages [8] -->
We establish an optimal control strategy model based on our normal thermodynamic model, forced convection model of water temperature and body

<!-- b000307 | prose | pages [8] -->
temperature comfort model. Here are the relationship among the three models and

<!-- b000308 | prose | pages [8] -->
equations.

<!-- b000309 | furniture | pages [8] -->


<!-- b000310 | prose | pages [8] -->
Initial Sub equation

<!-- b000311 | prose | pages [8] -->
Heat differential equation Temperature distribution

<!-- b000312 | prose | pages [8] -->
Body temperature

<!-- b000313 | prose | pages [8] -->
Universal thermodynamic model Forced convection

<!-- b000314 | prose | pages [8] -->
Secondary Sub model

<!-- b000315 | prose | pages [8] -->
Final model

<!-- b000316 | furniture | pages [8] -->


<!-- b000317 | prose | pages [8] -->
comfort model

<!-- b000318 | prose | pages [8] -->
model

<!-- b000319 | prose | pages [8] -->
Optimal control model of the bath strategy

<!-- b000320 | furniture | pages [9] -->
Team #46830

<!-- b000321 | furniture | pages [9] -->


<!-- b000322 | furniture | pages [9] -->


<!-- b000323 | furniture | pages [9] -->
Page 6 of 45

<!-- b000324 | caption | pages [9] -->
Figure 1: The relationship among the models and equations

<!-- b000325 | prose | pages [9] -->
According to our model, we propose two kinds of temperature control strategies and analyze their both advantages and shortages. In addition, the shape and volume of

<!-- b000326 | prose | pages [9] -->
the tub, the temperature, flow and convection of tap water, the motions made by the

<!-- b000327 | prose | pages [9] -->
person and some other parameters are extensively discussed in this section. The establishment and solution of our models are as follow.

<!-- b000328 | heading | pages [9] -->
4.1 Normal Thermodynamic Model of Water Temperature

<!-- b000329 | prose | pages [9] -->
In this section, we set up a normal thermodynamic model of water temperature in

<!-- b000330 | prose | pages [9] -->
space and time, which is based on Fourier's law, Newton's law of cooling, the Stefan-Boltzmann law, the heat conduction equation and the first law of

<!-- b000331 | prose | pages [9] -->
thermodynamics.

<!-- b000332 | prose | pages [9] -->
We use Newton's law of cooling, the Stefan-Boltzmann law and the first law of thermodynamics to solve the problem of the distribution of temperature with time.

<!-- b000333 | prose | pages [9] -->
And we use heat conduction equation to solve the problem of the distribution of temperature with space. In our model, the heat transfer and the heat radiation are

<!-- b000334 | prose | pages [9] -->
taken into account while the convection is ignored.

<!-- b000335 | heading | pages [9] -->
4.1.1 The differential equation of water heat in the tub

<!-- b000336 | prose | pages [9] -->
Considering the origin and destination of the infinitesimal of water heat in the tub, we get the differential equation as follows

<!-- b000337 | prose | pages [9] -->
  dQ dQ dQ exchange evaporation      dQ dQ dQ dQ (1)   body radiation water water

<!-- b000338 | prose | pages [9] -->
Here are the derivation and explanation of the equation by analyzing the heat of

<!-- b000339 | prose | pages [9] -->
each part.

<!-- b000340 | prose | pages [9] -->
First of all, assuming the tub as a cube with length a, width b and height H. Then we set a three-dimensional Cartesian coordinate system originated from the bottom center of the tub and paralleled to its height, length and width. As we all know, the drain and overflow valve of the tub are often designed in the midpoint of the two short

<!-- b000341 | prose | pages [9] -->
  a H sides. Thus, the overflow valve is located in

<!-- b000342 | prose | pages [9] -->
  a H

<!-- b000343 | prose | pages [9] -->
.

<!-- b000344 | prose | pages [9] -->
0, ,   2  

<!-- b000345 | furniture | pages [9] -->


<!-- b000346 | prose | pages [9] -->
and the drain is in

<!-- b000347 | prose | pages [9] -->
 0, ,   2  

<!-- b000348 | furniture | pages [10] -->
Team #46830

<!-- b000349 | furniture | pages [10] -->


<!-- b000350 | furniture | pages [10] -->


<!-- b000351 | furniture | pages [10] -->
Page 7 of 45

<!-- b000352 | furniture | pages [10] -->


<!-- b000353 | caption | pages [10] -->
Figure 2: the three-dimensional Cartesian coordinate system of the tub

<!-- b000354 | prose | pages [10] -->
To establish the model of water temperature over time, we firstly consider that the volume of water is changing over time. When the tub isn’t full, the volume of

<!-- b000355 | prose | pages [10] -->
water is proportional to the time growth. Because we usually open the valve to the

<!-- b000356 | prose | pages [10] -->
maximum when we are going to take a shower, the growth rate of the volume of water over time is the biggest flow of the valve. Then, when the volume is proper, people

<!-- b000357 | prose | pages [10] -->
enter the tub and from then on, the volume can be regarded as constant approximately.

<!-- b000358 | prose | pages [10] -->
Here comes the equation.

<!-- b000359 | prose | pages [10] -->


<!-- b000360 | prose | pages [10] -->
k t

<!-- b000361 | prose | pages [10] -->


<!-- b000362 | prose | pages [10] -->
max

<!-- b000363 | prose | pages [10] -->


<!-- b000364 | prose | pages [10] -->
V

<!-- b000365 | prose | pages [10] -->


<!-- b000366 | prose | pages [10] -->
V

<!-- b000367 | prose | pages [10] -->


<!-- b000368 | prose | pages [10] -->
0

<!-- b000369 | prose | pages [10] -->
 

<!-- b000370 | prose | pages [10] -->
V

<!-- b000371 | prose | pages [10] -->


<!-- b000372 | prose | pages [10] -->
0

<!-- b000373 | prose | pages [10] -->
0 t k

<!-- b000374 | prose | pages [10] -->
max

<!-- b000375 | furniture | pages [10] -->


<!-- b000376 | prose | pages [10] -->
V

<!-- b000377 | prose | pages [10] -->


<!-- b000378 | prose | pages [10] -->
0

<!-- b000379 | prose | pages [10] -->
t k

<!-- b000380 | prose | pages [10] -->
max

<!-- b000381 | prose | pages [10] -->
, it means that the largest volume of water when the Where, V abH V 0 body

<!-- b000382 | prose | pages [10] -->
k person is in the tub without overflow.

<!-- b000383 | prose | pages [10] -->
max is the largest flow of the valve.

<!-- b000384 | prose | pages [10] -->
By the definition of internal energy, we get the equation of the energy of water in

<!-- b000385 | prose | pages [10] -->
the tub.

<!-- b000386 | prose | pages [10] -->


<!-- b000387 | prose | pages [10] -->


<!-- b000388 | prose | pages [10] -->


<!-- b000389 | prose | pages [10] -->
c T t Q ( ) dV

<!-- b000390 | prose | pages [10] -->
(2) 

<!-- b000391 | prose | pages [10] -->
T t is the average water temperature on space, which can be defined Where, ( )

<!-- b000392 | prose | pages [10] -->
by

<!-- b000393 | prose | pages [10] -->


<!-- b000394 | prose | pages [10] -->


<!-- b000395 | prose | pages [10] -->
T t

<!-- b000396 | prose | pages [10] -->
( )

<!-- b000397 | prose | pages [10] -->


<!-- b000398 | prose | pages [10] -->
T x y z t

<!-- b000399 | prose | pages [10] -->
( , , , )

<!-- b000400 | prose | pages [10] -->
dV

<!-- b000401 | prose | pages [10] -->
(3)

<!-- b000402 | prose | pages [10] -->


<!-- b000403 | prose | pages [10] -->
dV

<!-- b000404 | prose | pages [10] -->


<!-- b000405 | prose | pages [10] -->
Then, we analyze different part of the heat exchange. The heat exchange is composed of heat transfer, heat radiation, convection, the inflow of hot water and the

<!-- b000406 | prose | pages [10] -->
outflow of cold water. Here we discussed them except convection which is discussed

<!-- b000407 | prose | pages [10] -->
in 4.2.

<!-- b000408 | prose | pages [10] -->
First, we analyze the heat loss due to heat exchange[5]. The loss is caused by the

<!-- b000409 | furniture | pages [10] -->


<!-- b000410 | furniture | pages [11] -->
Team #46830

<!-- b000411 | furniture | pages [11] -->


<!-- b000412 | furniture | pages [11] -->


<!-- b000413 | furniture | pages [11] -->
Page 8 of 45

<!-- b000414 | prose | pages [11] -->
contact of water with the inner wall of the tub and air. According to the Fourier's law,

<!-- b000415 | prose | pages [11] -->
the heat transfer power of per unit area is proportional to the temperature difference and to the thickness of the heat transfer medium. If we suppose that the thickness of

<!-- b000416 | prose | pages [11] -->
the tub wall is constant and its material is homogeneous, the heat transfer power of

<!-- b000417 | prose | pages [11] -->
per unit area is proportional to the temperature difference only. Thus we get the equation of the whole heat emission in unit time.

<!-- b000418 | prose | pages [11] -->
        

<!-- b000419 | prose | pages [11] -->
T dA dQ h T x y z t

<!-- b000420 | prose | pages [11] -->
[ ( , , , )

<!-- b000421 | prose | pages [11] -->


<!-- b000422 | prose | pages [11] -->
exchange

<!-- b000423 | prose | pages [11] -->


<!-- b000424 | prose | pages [11] -->


<!-- b000425 | prose | pages [11] -->
] ]

<!-- b000426 | prose | pages [11] -->
h T x y z t

<!-- b000427 | prose | pages [11] -->
[ ( , , , )

<!-- b000428 | prose | pages [11] -->
T dA dt

<!-- b000429 | prose | pages [11] -->
]

<!-- b000430 | prose | pages [11] -->
(4) 

<!-- b000431 | prose | pages [11] -->
0 0 0

<!-- b000432 | prose | pages [11] -->


<!-- b000433 | prose | pages [11] -->
D

<!-- b000434 | prose | pages [11] -->
Where, h is the heat transfer coefficient of water when the medium is the tub wall. h is the heat transfer coefficient of water to air.

<!-- b000435 | prose | pages [11] -->
Secondly, we analyze the heat loss due to water evaporation. According to the

<!-- b000436 | prose | pages [11] -->
surface molecular evolution rule and Dalton's law of evaporation, the evaporation rate per unit area is related to the liquid temperature, surface wind speed and humidity.

<!-- b000437 | prose | pages [11] -->
Because of assumption 1, humidity is constant and the evaporation rate per unit area is related to the liquid temperature. Here comes the following equation.

<!-- b000438 | prose | pages [11] -->


<!-- b000439 | prose | pages [11] -->
dQ

<!-- b000440 | prose | pages [11] -->


<!-- b000441 | prose | pages [11] -->
evaporation

<!-- b000442 | prose | pages [11] -->
  

<!-- b000443 | prose | pages [11] -->


<!-- b000444 | prose | pages [11] -->


<!-- b000445 | prose | pages [11] -->


<!-- b000446 | prose | pages [11] -->
u T

<!-- b000447 | prose | pages [11] -->


<!-- b000448 | prose | pages [11] -->
P

<!-- b000449 | prose | pages [11] -->


<!-- b000450 | prose | pages [11] -->
0

<!-- b000451 | prose | pages [11] -->


<!-- b000452 | prose | pages [11] -->
 

<!-- b000453 | prose | pages [11] -->


<!-- b000454 | prose | pages [11] -->


<!-- b000455 | prose | pages [11] -->
   

<!-- b000456 | prose | pages [11] -->
u T q dA dt

<!-- b000457 | prose | pages [11] -->
 

<!-- b000458 | prose | pages [11] -->
gas

<!-- b000459 | prose | pages [11] -->
 

<!-- b000460 | prose | pages [11] -->
D

<!-- b000461 | prose | pages [11] -->
(5)

<!-- b000462 | prose | pages [11] -->
1

<!-- b000463 | prose | pages [11] -->


<!-- b000464 | prose | pages [11] -->
  

<!-- b000465 | prose | pages [11] -->
2

<!-- b000466 | prose | pages [11] -->
 

<!-- b000467 | prose | pages [11] -->


<!-- b000468 | prose | pages [11] -->
1

<!-- b000469 | prose | pages [11] -->
w

<!-- b000470 | prose | pages [11] -->
  

<!-- b000471 | prose | pages [11] -->


<!-- b000472 | prose | pages [11] -->
2 2

<!-- b000473 | prose | pages [11] -->
RT

<!-- b000474 | prose | pages [11] -->
  

<!-- b000475 | prose | pages [11] -->
u T is the rate of water evaporation per unit time and area; Where,

<!-- b000476 | prose | pages [11] -->
T is the air temperature of the air to water surface;

<!-- b000477 | prose | pages [11] -->
P is the saturated vapor pressure of water at current temperature;

<!-- b000478 | prose | pages [11] -->
w is the relative humidity of air in the bathroom, which is constant according to

<!-- b000479 | prose | pages [11] -->
assumption 1;

<!-- b000480 | prose | pages [11] -->
    3 3 10 kg m , which is the density of water ;

<!-- b000481 | prose | pages [11] -->
      3 1 18 10 kg mol , which is the mole mass of water;

<!-- b000482 | prose | pages [11] -->
     1 1 R 8.31 J mol k , which is the universal gas constant;

<!-- b000483 | prose | pages [11] -->
Third, we analyze the heat loss due to people’s body [7]. To be specific, it

<!-- b000484 | prose | pages [11] -->
describes the heat exchange of people’s body surface and water. We suppose that the

<!-- b000485 | prose | pages [11] -->
body is fully immersed in water, so the contact area between body and water is the superficial area of the body. Because the heat exchange between the human body and

<!-- b000486 | prose | pages [11] -->
the water is the heat transfer through the water flow, according to Newton cooling

<!-- b000487 | prose | pages [11] -->
theorem, we get the heat infinitesimal equation of body’s absorption.

<!-- b000488 | furniture | pages [11] -->


<!-- b000489 | furniture | pages [12] -->
Team #46830

<!-- b000490 | furniture | pages [12] -->


<!-- b000491 | prose | pages [12] -->


<!-- b000492 | furniture | pages [12] -->


<!-- b000493 | furniture | pages [12] -->
Page 9 of 45

<!-- b000494 | prose | pages [12] -->
   [ ( ) dQ S T t body body T ] h dt (6) body body

<!-- b000495 | prose | pages [12] -->
is the heat transfer rate of human body and water. Because the Where, h body

<!-- b000496 | prose | pages [12] -->
similarity of the macroscopic physical properties between human body and water,

<!-- b000497 | prose | pages [12] -->
can be substituted with heat transfer rate of water and water. h body T t is the ( )

<!-- b000498 | prose | pages [12] -->
average water temperature in the tub. The reason to set this parameter is because the

<!-- b000499 | prose | pages [12] -->
surface of human body is irregular, the temperature distribution between the contact surfaces is harder to formulate. Then we regard the average water temperature in the tub as that of the contact surfaces.

<!-- b000500 | prose | pages [12] -->
Fourth, we analyze the heat loss due to heat radiation [10]. To be specific, it describes that water dissipates heat in the form of electromagnetic radiation to the

<!-- b000501 | prose | pages [12] -->
surrounding and the loss can be calculated by Trevor Boltzmann's law. Unfortunately,

<!-- b000502 | prose | pages [12] -->
the law is set to describe the heat radiation of ideal black-body, while water isn’t totally suit. Thus we modify the law with a rate of heat radiation , and it is recorded

<!-- b000503 | prose | pages [12] -->
 . we get the heat infinitesimal equation of the loss. that the rate of water is 0.97

<!-- b000504 | prose | pages [12] -->
  

<!-- b000505 | prose | pages [12] -->
 dQ radiation

<!-- b000506 | prose | pages [12] -->


<!-- b000507 | prose | pages [12] -->


<!-- b000508 | prose | pages [12] -->


<!-- b000509 | prose | pages [12] -->
  4 T T x y z t dA dt , , ,

<!-- b000510 | prose | pages [12] -->
(7)  

<!-- b000511 | prose | pages [12] -->
Fifth, we analyze the heat increase due to the constant intake of hot water.

<!-- b000512 | prose | pages [12] -->
According to the definition of the internal energy of water, we get the heat infinitesimal equation of the increase.

<!-- b000513 | prose | pages [12] -->
  dQ      c T dV  water c T kdt (8) 0 0 0

<!-- b000514 | prose | pages [12] -->
Sixth, we analyze the heat loss due to the overflow water. We assume the

<!-- b000515 | prose | pages [12] -->
overflow water temperature as the temperature of the water near the outfall and get

<!-- b000516 | prose | pages [12] -->
the heat loss equation.

<!-- b000517 | prose | pages [12] -->
a   dQ a    H t dV c T

<!-- b000518 | prose | pages [12] -->
(0, , , )

<!-- b000519 | prose | pages [12] -->


<!-- b000520 | prose | pages [12] -->
water 2

<!-- b000521 | prose | pages [12] -->
c T

<!-- b000522 | prose | pages [12] -->
(0, ,

<!-- b000523 | prose | pages [12] -->
H t

<!-- b000524 | prose | pages [12] -->
, )

<!-- b000525 | prose | pages [12] -->
kdt (9)

<!-- b000526 | prose | pages [12] -->
2

<!-- b000527 | prose | pages [12] -->
To sum up, the origin and destination of the water heat in the tub are shown

<!-- b000528 | prose | pages [12] -->
below.

<!-- b000529 | furniture | pages [12] -->


<!-- b000530 | furniture | pages [12] -->


<!-- b000531 | furniture | pages [13] -->
Team #46830

<!-- b000532 | furniture | pages [13] -->


<!-- b000533 | furniture | pages [13] -->


<!-- b000534 | furniture | pages [13] -->
Page 10 of 45

<!-- b000535 | caption | pages [13] -->
Figure 3: The origin and destination of heat

<!-- b000536 | prose | pages [13] -->
Combining the six equations of heat exchange [15], we get the universal differential equation of the internal energy of water over temperature in the tub.

<!-- b000537 | prose | pages [13] -->
   dQ dQ dQ exchange evaporation   

<!-- b000538 | furniture | pages [13] -->


<!-- b000539 | prose | pages [13] -->
dQ dQ dQ dQ   body radiation water water

<!-- b000540 | heading | pages [13] -->
4.1.2 Thermodynamic analysis of bath process

<!-- b000541 | prose | pages [13] -->
In this section, according to the periodic change of the volume of water in the tub,

<!-- b000542 | prose | pages [13] -->
we divide the water temperature in the tub over time into three stages:

<!-- b000543 | prose | pages [13] -->
First, the initial filling stage. In this stage, people inject water to the tub when

<!-- b000544 | prose | pages [13] -->
people get into the tub while the water won’t overflow. Then we modify the heat loss

<!-- b000545 | prose | pages [13] -->
dQ in the differential equation of water heat in the tub due to the overflow water water

<!-- b000546 | prose | pages [13] -->
and get the function of the volume of water and the differential equation of the change

<!-- b000547 | prose | pages [13] -->
of water internal energy as follow:

<!-- b000548 | prose | pages [13] -->
   

<!-- b000549 | prose | pages [13] -->
dQ dQ dQ

<!-- b000550 | prose | pages [13] -->


<!-- b000551 | prose | pages [13] -->
exchange

<!-- b000552 | prose | pages [13] -->


<!-- b000553 | prose | pages [13] -->
V V kt

<!-- b000554 | furniture | pages [13] -->


<!-- b000555 | prose | pages [13] -->
 

<!-- b000556 | prose | pages [13] -->
dQ dQ

<!-- b000557 | prose | pages [13] -->
evaporation radiation water

<!-- b000558 | prose | pages [13] -->
Second, the natural cooling stage when the tub is full of water and body. In this

<!-- b000559 | prose | pages [13] -->
V . According to the assumption 2, we modify the heat increase stage, the volume is 0

<!-- b000560 | prose | pages [13] -->
dQ due to the constant intake of hot water

<!-- b000561 | prose | pages [13] -->
dQ

<!-- b000562 | prose | pages [13] -->
and the heat loss due to the overflow water

<!-- b000563 | prose | pages [13] -->
in the differential equation of water heat in the tub and get the water water

<!-- b000564 | prose | pages [13] -->
function of the volume of water and the differential equation of the change of water internal energy as follow:

<!-- b000565 | prose | pages [13] -->
    dQ dQ dQ 

<!-- b000566 | prose | pages [13] -->
exchange

<!-- b000567 | prose | pages [13] -->
 V V V

<!-- b000568 | prose | pages [13] -->
0

<!-- b000569 | furniture | pages [13] -->


<!-- b000570 | prose | pages [13] -->
  dQ dQ

<!-- b000571 | prose | pages [13] -->
evaporation body radiation

<!-- b000572 | prose | pages [13] -->
Third, the reheating after hot water injection stage. In this stage, users are unsatisfactory with the water temperature in the tub and then open the tap again to

<!-- b000573 | prose | pages [13] -->
mix the intake hot water with the previous water in the tub. Owing to the limitation of

<!-- b000574 | prose | pages [13] -->
the volume of the tub, excess water overflows to keep the tub full. We get the function of the volume of water and the differential equation of the change of water internal

<!-- b000575 | prose | pages [13] -->
energy as follow:

<!-- b000576 | prose | pages [13] -->
   

<!-- b000577 | prose | pages [13] -->
dQ dQ dQ dQ

<!-- b000578 | prose | pages [13] -->


<!-- b000579 | prose | pages [13] -->
exchange evaporation body

<!-- b000580 | furniture | pages [13] -->


<!-- b000581 | prose | pages [13] -->


<!-- b000582 | prose | pages [13] -->
V V V

<!-- b000583 | prose | pages [13] -->
0

<!-- b000584 | furniture | pages [13] -->


<!-- b000585 | prose | pages [13] -->
a

<!-- b000586 | prose | pages [13] -->
  

<!-- b000587 | prose | pages [13] -->


<!-- b000588 | prose | pages [13] -->


<!-- b000589 | prose | pages [13] -->


<!-- b000590 | prose | pages [13] -->


<!-- b000591 | prose | pages [13] -->
dQ c kT dt c kT

<!-- b000592 | prose | pages [13] -->
(0, ,

<!-- b000593 | prose | pages [13] -->
H t

<!-- b000594 | prose | pages [13] -->
, )

<!-- b000595 | prose | pages [13] -->
dt

<!-- b000596 | prose | pages [13] -->
radiation 0 2

<!-- b000597 | furniture | pages [14] -->
Team #46830

<!-- b000598 | furniture | pages [14] -->


<!-- b000599 | furniture | pages [14] -->


<!-- b000600 | furniture | pages [14] -->
Page 11 of 45

<!-- b000601 | furniture | pages [14] -->


<!-- b000602 | heading | pages [14] -->
4.1.3 Temperature field distribution of the water in the tub

<!-- b000603 | prose | pages [14] -->
In this section, we establish a model of the distribution of water temperature in the tub when injecting hot water again, and solve the model by the PDE tool of

<!-- b000604 | prose | pages [14] -->
Matlab. However, the solution is difficult to be used in the following models, hence

<!-- b000605 | prose | pages [14] -->
we use plane fitting in the numerical solution and fortunately. Then we find that the fitting degree is pretty high. So we use the fitting plane as approximate analytic

<!-- b000606 | prose | pages [14] -->
solution of temperature field distribution of water. It greatly simplifies the difficulty

<!-- b000607 | prose | pages [14] -->
of solving the model, at the same time, with good accuracy.

<!-- b000608 | prose | pages [14] -->
1. Temperature field distribution based on heat conduction equation

<!-- b000609 | prose | pages [14] -->
 a H t According to assumption 4, water temperature near the tap (0, is , , ) 2

<!-- b000610 | prose | pages [14] -->
 a H t constant when injecting water. That is to say, here (0, is a constant , , ) 2

<!-- b000611 | prose | pages [14] -->
temperature heat source, because whenever the water drop from the tap, the

<!-- b000612 | prose | pages [14] -->
temperature is the same. Therefore, taken heat conduction equation into account, we use the following partial differential equations to describe the temperature field

<!-- b000613 | prose | pages [14] -->
distribution of the water.

<!-- b000614 | prose | pages [14] -->
    T T      c ( ) (     t x x y

<!-- b000615 | prose | pages [14] -->


<!-- b000616 | prose | pages [14] -->
     T T a   

<!-- b000617 | furniture | pages [14] -->


<!-- b000618 | prose | pages [14] -->
) ( ) q (0, , H t , )     y z z 2

<!-- b000619 | prose | pages [14] -->
is thermal diffusion coefficient,  is the thermal   2 Where, ( m s )  c

<!-- b000620 | prose | pages [14] -->
 a  a H t is the equivalent heat source at (0, q (0, , H t , ) conductivity, 2 , , ) . 2

<!-- b000621 | prose | pages [14] -->
The Neumann boundary [8] of the water in the tub can be formulated as:

<!-- b000622 | prose | pages [14] -->
  

<!-- b000623 | prose | pages [14] -->
T b

<!-- b000624 | prose | pages [14] -->


<!-- b000625 | prose | pages [14] -->


<!-- b000626 | prose | pages [14] -->
 

<!-- b000627 | prose | pages [14] -->
h T

<!-- b000628 | prose | pages [14] -->
(

<!-- b000629 | prose | pages [14] -->
   

<!-- b000630 | prose | pages [14] -->
x

<!-- b000631 | prose | pages [14] -->
2

<!-- b000632 | prose | pages [14] -->
   

<!-- b000633 | prose | pages [14] -->
T

<!-- b000634 | prose | pages [14] -->


<!-- b000635 | prose | pages [14] -->


<!-- b000636 | prose | pages [14] -->
 

<!-- b000637 | prose | pages [14] -->
h T x

<!-- b000638 | prose | pages [14] -->
( ,

<!-- b000639 | prose | pages [14] -->
    

<!-- b000640 | prose | pages [14] -->
y

<!-- b000641 | prose | pages [14] -->


<!-- b000642 | prose | pages [14] -->
 

<!-- b000643 | prose | pages [14] -->
T

<!-- b000644 | prose | pages [14] -->


<!-- b000645 | prose | pages [14] -->


<!-- b000646 | prose | pages [14] -->


<!-- b000647 | prose | pages [14] -->
 

<!-- b000648 | prose | pages [14] -->
, , , )

<!-- b000649 | prose | pages [14] -->
y z t T

<!-- b000650 | prose | pages [14] -->


<!-- b000651 | prose | pages [14] -->
0

<!-- b000652 | prose | pages [14] -->
 

<!-- b000653 | prose | pages [14] -->
a a

<!-- b000654 | prose | pages [14] -->


<!-- b000655 | prose | pages [14] -->
, , )

<!-- b000656 | prose | pages [14] -->
z t T

<!-- b000657 | prose | pages [14] -->


<!-- b000658 | prose | pages [14] -->
0

<!-- b000659 | prose | pages [14] -->


<!-- b000660 | prose | pages [14] -->
2 2

<!-- b000661 | furniture | pages [14] -->


<!-- b000662 | prose | pages [14] -->
Boundary

<!-- b000663 | prose | pages [14] -->


<!-- b000664 | prose | pages [14] -->


<!-- b000665 | prose | pages [14] -->
( , ,0, )

<!-- b000666 | prose | pages [14] -->
h T x y

<!-- b000667 | prose | pages [14] -->
 

<!-- b000668 | prose | pages [14] -->
z

<!-- b000669 | prose | pages [14] -->
 

<!-- b000670 | prose | pages [14] -->
T

<!-- b000671 | prose | pages [14] -->


<!-- b000672 | prose | pages [14] -->


<!-- b000673 | prose | pages [14] -->


<!-- b000674 | prose | pages [14] -->


<!-- b000675 | prose | pages [14] -->
1

<!-- b000676 | prose | pages [14] -->
t T

<!-- b000677 | prose | pages [14] -->
0

<!-- b000678 | prose | pages [14] -->


<!-- b000679 | prose | pages [14] -->


<!-- b000680 | prose | pages [14] -->
h T x y H t

<!-- b000681 | prose | pages [14] -->
( , ,

<!-- b000682 | prose | pages [14] -->
  

<!-- b000683 | prose | pages [14] -->
z

<!-- b000684 | prose | pages [14] -->
T x y z ( , , ,0) The starting conditions is

<!-- b000685 | prose | pages [14] -->
, )

<!-- b000686 | prose | pages [14] -->
T

<!-- b000687 | prose | pages [14] -->
0

<!-- b000688 | prose | pages [14] -->
 T x y z ( , , ) . 0

<!-- b000689 | prose | pages [14] -->
T x y z is the distribution of water temperature in the tub before the second 0( , , )

<!-- b000690 | furniture | pages [14] -->


<!-- b000691 | furniture | pages [15] -->
Team #46830

<!-- b000692 | furniture | pages [15] -->


<!-- b000693 | furniture | pages [15] -->
Page 12 of 45

<!-- b000694 | furniture | pages [15] -->


<!-- b000695 | prose | pages [15] -->
of rejecting hot water again.

<!-- b000696 | prose | pages [15] -->
2.The numerical solution of the heat conduction equation [9] We solve the heat conduction model by the PDE tool of Matlab [13][14]. During

<!-- b000697 | prose | pages [15] -->
the process, the starting condition is that the water temperature is 39 centigrade and

<!-- b000698 | prose | pages [15] -->
distributed evenly. The reasons of setting such condition are as follow. First, people’s action will stir the water to a uniform distribution. On the other hand, it’s recorded

<!-- b000699 | prose | pages [15] -->
that 39 centigrade is the most comfortable temperature for bathing. If the water temperature is lower than that, people will inject hot water to heat the water.

<!-- b000700 | prose | pages [15] -->
We set the temperature of the equivalent heat source 45 centigrade to solve the

<!-- b000701 | prose | pages [15] -->
temperature field at 2.5s and 100s, here are the results:

<!-- b000702 | furniture | pages [15] -->


<!-- b000703 | caption | pages [15] -->
Figure 4: Surface temperature field at 2.5s

<!-- b000704 | furniture | pages [15] -->


<!-- b000705 | caption | pages [15] -->
Figure 5: Surface temperature field at 100s

<!-- b000706 | prose | pages [15] -->
The arrow in the figure is the direction of heat transmission. We get the

<!-- b000707 | prose | pages [15] -->
similarities and differences between the temperature distributions of 2.5s and 100s by comparing them.

<!-- b000708 | prose | pages [15] -->
Similarities:

<!-- b000709 | prose | pages [15] -->
i. The heat always spread from the tap, and is gradually dispersed throughout the space. What’s more, temperature distribution is uniform at the end of the outlet. The

<!-- b000710 | furniture | pages [15] -->


<!-- b000711 | furniture | pages [16] -->
Team #46830

<!-- b000712 | furniture | pages [16] -->


<!-- b000713 | furniture | pages [16] -->


<!-- b000714 | furniture | pages [16] -->
Page 13 of 45

<!-- b000715 | prose | pages [16] -->
reason is that the heat is gradually spreading from the inlet to the outlet, during the

<!-- b000716 | prose | pages [16] -->
 process, it disperses evenly in the x o actual situation.

<!-- b000717 | prose | pages [16] -->
  plane, which is in accordance with the z z

<!-- b000718 | prose | pages [16] -->
ii. At the start of injecting hot water, the water temperature near the inlet is

<!-- b000719 | prose | pages [16] -->
keeping at approximately 45 centigrade, while near the out, the temperature is about 40 centigrade. The reason is that water is a poor conductor of heat. 2.5s and 100s are

<!-- b000720 | prose | pages [16] -->
too short to transfer heat evenly. Thus the temperature near outlet doesn’t enhance obviously.

<!-- b000721 | prose | pages [16] -->
Differences:

<!-- b000722 | prose | pages [16] -->
i. The distribution of water temperature at 100s is more even than that at 2.5s.

<!-- b000723 | prose | pages [16] -->
Obviously, the longer time makes the heat transfer more adequate between the intake of water and the previous water in the tub.

<!-- b000724 | prose | pages [16] -->
ii. The total water temperature in the tub is higher at 100s, because the longer time makes bigger amount of hot water injection, enhancing the average water

<!-- b000725 | prose | pages [16] -->
temperature in the tub.

<!-- b000726 | prose | pages [16] -->
iii. The spread of heat in y direction is uniform at 100s, because the whole level of water temperature and the distribution of water temperature gradually becomes

<!-- b000727 | prose | pages [16] -->
  stable over time. Moreover, the distribution of temperature in plane x o z

<!-- b000728 | furniture | pages [16] -->


<!-- b000729 | prose | pages [16] -->
becomes uniform owing to heat transfer. Hence, the spread of heat in y direction is uniform. That means the distribution of the gradient in the Y axis is tend to decrease

<!-- b000730 | prose | pages [16] -->
linearly with the value of y coordinate

<!-- b000731 | prose | pages [16] -->
III. The approximate analytical solution By means of linear fitting, we get the approximate analytic solution of

<!-- b000732 | prose | pages [16] -->
temperature distribution in space. Because in the discussion of the universal thermodynamic model of the water temperature in the previous paper and the optimal

<!-- b000733 | prose | pages [16] -->
bath strategy and bubble bath, we all need the analytical solution of water temperature

<!-- b000734 | prose | pages [16] -->
over time and space to do the further analysis and solution. Nevertheless, it’s more than hard to use the numerical solution of temperature field directly and to optimize

<!-- b000735 | prose | pages [16] -->
the following models. Therefore, we carry out a simple function fitting to the

<!-- b000736 | prose | pages [16] -->
distribution of the water temperature in space.

<!-- b000737 | prose | pages [16] -->
First of all, we observe the distribution surface of temperature in space, which is

<!-- b000738 | prose | pages [16] -->
shown as follows.

<!-- b000739 | furniture | pages [16] -->


<!-- b000740 | furniture | pages [17] -->
Team #46830

<!-- b000741 | furniture | pages [17] -->


<!-- b000742 | furniture | pages [17] -->


<!-- b000743 | furniture | pages [17] -->
Page 14 of 45

<!-- b000744 | furniture | pages [17] -->


<!-- b000745 | caption | pages [17] -->
Figure 6: The distribution surface of temperature in space

<!-- b000746 | prose | pages [17] -->
Combined with the previous analysis, we firstly fit the above surfaces by plane

<!-- b000747 | prose | pages [17] -->
fitting. In our opinion, the linear relationship in the subsequent model will be greatly simplified calculation, and the characteristic of linear, simple and clear has a good approximation to the real situation. Therefore, we select a number of discrete points on the surface of temperature distribution, and try to make the linear fitting to these

<!-- b000748 | prose | pages [17] -->
points. The fitting plane is shown as follows

<!-- b000749 | prose | pages [17] -->
  T x y z ( , , ,2.5 ) s 44.63     0 y 1.3, 0.4 x    4.294 y 0.08328 x

<!-- b000750 | furniture | pages [17] -->


<!-- b000751 | prose | pages [17] -->
    0.4,0 z 0.49

<!-- b000752 | prose | pages [17] -->
R  2 0.931

<!-- b000753 | prose | pages [17] -->
The goodness of fit of this kind of fitting method is

<!-- b000754 | prose | pages [17] -->
, which shows a

<!-- b000755 | prose | pages [17] -->
great fit for this distribution surface. Thus we determine to use the fitting method and the fitting plane is shown in Figure 7.

<!-- b000756 | furniture | pages [17] -->


<!-- b000757 | caption | pages [17] -->
Figure 7: The fitting plane

<!-- b000758 | prose | pages [17] -->
  plane, so is the temperature In addition, the tub is symmetrical at y o z

<!-- b000759 | prose | pages [17] -->
distribution of abstract mathematical model. Moreover, it should be dispersed

<!-- b000760 | prose | pages [17] -->
  plane. However, the temperature function ( , , ,2.5 ) uniformly at x o z T x y z s over

<!-- b000761 | prose | pages [17] -->
x coordinate in the previous fitting plane generates from the error of taking discrete

<!-- b000762 | prose | pages [17] -->
points. Thus the ideal model of the plane should be

<!-- b000763 | furniture | pages [17] -->


<!-- b000764 | furniture | pages [18] -->
Team #46830

<!-- b000765 | furniture | pages [18] -->


<!-- b000766 | prose | pages [18] -->
  T x y z ( , , ,2.5 ) s    0 y 1.3, 0.4 

<!-- b000767 | furniture | pages [18] -->


<!-- b000768 | furniture | pages [18] -->
Page 15 of 45

<!-- b000769 | prose | pages [18] -->
 44.63 4.294 y

<!-- b000770 | furniture | pages [18] -->


<!-- b000771 | prose | pages [18] -->
     x 0.4,0 z 0.49

<!-- b000772 | prose | pages [18] -->
We extend the model to the water temperature distribution at any time, because 2.5s is the very moment when hot water flows into the tub continuously. And at 2.5s,

<!-- b000773 | prose | pages [18] -->
the water temperature gradient is one of the largest, and the distribution is the most

<!-- b000774 | prose | pages [18] -->
uneven. After this moment, the temperature will gradually distribute more evenly and the temperature surface also becomes more close to a plane. Therefore, it’s proper to

<!-- b000775 | prose | pages [18] -->
use the distribution function to describe the water temperature distribution of the other

<!-- b000776 | prose | pages [18] -->
moments after 2.5s. The distribution equation can be universally formulated as

<!-- b000777 | prose | pages [18] -->
T x y z t ( , , , )

<!-- b000778 | prose | pages [18] -->
 

<!-- b000779 | prose | pages [18] -->
    C t K t y (10)

<!-- b000780 | prose | pages [18] -->
K t are the functions on time. C t 、 Where

<!-- b000781 | prose | pages [18] -->
   K t  T x y z t We should notice that

<!-- b000782 | prose | pages [18] -->
temperature distribution function.

<!-- b000783 | prose | pages [18] -->
, , , , which means negative gradient of

<!-- b000784 | prose | pages [18] -->
We set the average water temperature into formula (3) to get the following relationship:

<!-- b000785 | prose | pages [18] -->
 

<!-- b000786 | prose | pages [18] -->
T x y z t

<!-- b000787 | prose | pages [18] -->
( , , , )

<!-- b000788 | prose | pages [18] -->
dV

<!-- b000789 | prose | pages [18] -->
 

<!-- b000790 | prose | pages [18] -->


<!-- b000791 | prose | pages [18] -->
T t

<!-- b000792 | prose | pages [18] -->
( )

<!-- b000793 | prose | pages [18] -->


<!-- b000794 | prose | pages [18] -->
dV

<!-- b000795 | prose | pages [18] -->


<!-- b000796 | prose | pages [18] -->
a a

<!-- b000797 | prose | pages [18] -->
 

<!-- b000798 | prose | pages [18] -->
    

<!-- b000799 | prose | pages [18] -->
bH C t K t y dy

<!-- b000800 | prose | pages [18] -->
2 2

<!-- b000801 | prose | pages [18] -->
 

<!-- b000802 | prose | pages [18] -->
a a

<!-- b000803 | prose | pages [18] -->
 

<!-- b000804 | prose | pages [18] -->


<!-- b000805 | prose | pages [18] -->


<!-- b000806 | furniture | pages [18] -->


<!-- b000807 | prose | pages [18] -->
C t

<!-- b000808 | prose | pages [18] -->
2 2

<!-- b000809 | prose | pages [18] -->
abH

<!-- b000810 | prose | pages [18] -->
Thus the model of the temperature distribution can be transformed in to

<!-- b000811 | prose | pages [18] -->
T x y z t ( , , , )     T t ( ) K t y (11)

<!-- b000812 | prose | pages [18] -->
On the other hand, The variance in the spatial distribution of the water

<!-- b000813 | prose | pages [18] -->
temperature in the tub is

<!-- b000814 | prose | pages [18] -->


<!-- b000815 | prose | pages [18] -->
D T 

<!-- b000816 | prose | pages [18] -->
 2 2

<!-- b000817 | prose | pages [18] -->
a K t

<!-- b000818 | furniture | pages [18] -->


<!-- b000819 | prose | pages [18] -->
12

<!-- b000820 | prose | pages [18] -->
Hence, we get the variance of water temperature at a moment with the realistic

<!-- b000821 | prose | pages [18] -->
data or by programming to get a series of points randomly selected on the surface of the numerical simulation of temperature in 4.1.3.II. Then the temperature gradient

<!-- b000822 | prose | pages [18] -->
equation of the moment is

<!-- b000823 | prose | pages [18] -->
  K t  2 3D T (12) a

<!-- b000824 | prose | pages [18] -->
 K t over time. Unfortunately, with limited time, we don’t fit the function of

<!-- b000825 | furniture | pages [18] -->


<!-- b000826 | furniture | pages [19] -->
Team #46830

<!-- b000827 | furniture | pages [19] -->


<!-- b000828 | prose | pages [19] -->


<!-- b000829 | furniture | pages [19] -->


<!-- b000830 | furniture | pages [19] -->
Page 16 of 45

<!-- b000831 | prose | pages [19] -->
K t is given by an unknown function in the thermodynamic model of water. If So

<!-- b000832 | prose | pages [19] -->
time permits, we will surely fit it into a simple function.

<!-- b000833 | heading | pages [19] -->
4.1.4 The universal thermodynamic model of water

<!-- b000834 | prose | pages [19] -->
In this section, under the condition that water is in the absence of human

<!-- b000835 | prose | pages [19] -->
movement interference, we get the model in time and space.

<!-- b000836 | prose | pages [19] -->
We take formula (11) into formula (4) and formula (9) and get:

<!-- b000837 | prose | pages [19] -->
       dQ h T t ( ) T ab 2   exchange 0

<!-- b000838 | prose | pages [19] -->
 

<!-- b000839 | prose | pages [19] -->
 dQ c T t

<!-- b000840 | prose | pages [19] -->


<!-- b000841 | prose | pages [19] -->


<!-- b000842 | prose | pages [19] -->
water

<!-- b000843 | prose | pages [19] -->


<!-- b000844 | prose | pages [19] -->
        aH 2 bH h T t ( ) T ab dt

<!-- b000845 | furniture | pages [19] -->


<!-- b000846 | prose | pages [19] -->
  0

<!-- b000847 | prose | pages [19] -->


<!-- b000848 | prose | pages [19] -->
a

<!-- b000849 | prose | pages [19] -->


<!-- b000850 | prose | pages [19] -->
 

<!-- b000851 | prose | pages [19] -->
( )

<!-- b000852 | prose | pages [19] -->
K t dV

<!-- b000853 | furniture | pages [19] -->


<!-- b000854 | prose | pages [19] -->


<!-- b000855 | prose | pages [19] -->
2

<!-- b000856 | prose | pages [19] -->


<!-- b000857 | prose | pages [19] -->
In addition, we note that the inner wall of the tub is smooth, and at the beginning of the design of the tub, we propose that coating the metal film on the surface of the

<!-- b000858 | prose | pages [19] -->
tub can effectively reduce the heat radiation power of the water in the tub, just like

<!-- b000859 | prose | pages [19] -->
thermos bottles. Thus we ignore the heat radiation of micro electromagnetic wave through the inner wall of the tub. At the same time, we take formula (11) into formula

<!-- b000860 | prose | pages [19] -->
(7) and get:

<!-- b000861 | prose | pages [19] -->
 

<!-- b000862 | prose | pages [19] -->
a

<!-- b000863 | prose | pages [19] -->
4

<!-- b000864 | prose | pages [19] -->


<!-- b000865 | prose | pages [19] -->
   

<!-- b000866 | prose | pages [19] -->


<!-- b000867 | prose | pages [19] -->


<!-- b000868 | prose | pages [19] -->
dQ b T t

<!-- b000869 | prose | pages [19] -->
( )

<!-- b000870 | prose | pages [19] -->
K t y dy dt

<!-- b000871 | prose | pages [19] -->
 

<!-- b000872 | prose | pages [19] -->
2

<!-- b000873 | prose | pages [19] -->
 

<!-- b000874 | prose | pages [19] -->
a radiation

<!-- b000875 | prose | pages [19] -->


<!-- b000876 | prose | pages [19] -->
 

<!-- b000877 | prose | pages [19] -->
2

<!-- b000878 | prose | pages [19] -->
 

<!-- b000879 | prose | pages [19] -->
5 5

<!-- b000880 | prose | pages [19] -->


<!-- b000881 | prose | pages [19] -->
     

<!-- b000882 | prose | pages [19] -->
b a a

<!-- b000883 | prose | pages [19] -->
 

<!-- b000884 | prose | pages [19] -->
     

<!-- b000885 | prose | pages [19] -->
T t

<!-- b000886 | prose | pages [19] -->
( )

<!-- b000887 | prose | pages [19] -->
K t T t

<!-- b000888 | prose | pages [19] -->
( )

<!-- b000889 | prose | pages [19] -->
K t dt

<!-- b000890 | prose | pages [19] -->
     

<!-- b000891 | prose | pages [19] -->


<!-- b000892 | prose | pages [19] -->
5

<!-- b000893 | prose | pages [19] -->
K t

<!-- b000894 | prose | pages [19] -->
2 2

<!-- b000895 | prose | pages [19] -->
       

<!-- b000896 | prose | pages [19] -->
At this time we simplify our universal thermodynamic model of water in a great

<!-- b000897 | prose | pages [19] -->
degree. The mathematical model is given by the following equations:

<!-- b000898 | prose | pages [19] -->
 

<!-- b000899 | prose | pages [19] -->
  

<!-- b000900 | prose | pages [19] -->
dQ dQ dQ dQ

<!-- b000901 | prose | pages [19] -->
exchange evaporation

<!-- b000902 | prose | pages [19] -->


<!-- b000903 | prose | pages [19] -->
 

<!-- b000904 | prose | pages [19] -->


<!-- b000905 | prose | pages [19] -->
    

<!-- b000906 | prose | pages [19] -->
dQ h T t

<!-- b000907 | prose | pages [19] -->
( )

<!-- b000908 | prose | pages [19] -->
T ab

<!-- b000909 | prose | pages [19] -->
2

<!-- b000910 | prose | pages [19] -->
 

<!-- b000911 | prose | pages [19] -->
exchange

<!-- b000912 | prose | pages [19] -->
0

<!-- b000913 | prose | pages [19] -->
 

<!-- b000914 | prose | pages [19] -->


<!-- b000915 | prose | pages [19] -->
dQ uabq dt

<!-- b000916 | prose | pages [19] -->
evaporation gas

<!-- b000917 | prose | pages [19] -->


<!-- b000918 | prose | pages [19] -->
   

<!-- b000919 | prose | pages [19] -->


<!-- b000920 | prose | pages [19] -->
dQ S

<!-- b000921 | prose | pages [19] -->
[ ( )

<!-- b000922 | prose | pages [19] -->
T t T

<!-- b000923 | prose | pages [19] -->
]

<!-- b000924 | prose | pages [19] -->
h

<!-- b000925 | prose | pages [19] -->
body body body body

<!-- b000926 | prose | pages [19] -->


<!-- b000927 | prose | pages [19] -->
 

<!-- b000928 | prose | pages [19] -->


<!-- b000929 | prose | pages [19] -->
 

<!-- b000930 | prose | pages [19] -->
b

<!-- b000931 | prose | pages [19] -->


<!-- b000932 | prose | pages [19] -->
 

<!-- b000933 | prose | pages [19] -->
dQ T t

<!-- b000934 | prose | pages [19] -->
( )

<!-- b000935 | prose | pages [19] -->
K t

<!-- b000936 | prose | pages [19] -->
  

<!-- b000937 | prose | pages [19] -->


<!-- b000938 | prose | pages [19] -->
radiation

<!-- b000939 | prose | pages [19] -->


<!-- b000940 | prose | pages [19] -->
5

<!-- b000941 | prose | pages [19] -->
K t

<!-- b000942 | prose | pages [19] -->
      

<!-- b000943 | prose | pages [19] -->


<!-- b000944 | prose | pages [19] -->


<!-- b000945 | prose | pages [19] -->


<!-- b000946 | prose | pages [19] -->
dQ c T dV c T kdt

<!-- b000947 | prose | pages [19] -->


<!-- b000948 | prose | pages [19] -->


<!-- b000949 | prose | pages [19] -->
water

<!-- b000950 | prose | pages [19] -->
0 0

<!-- b000951 | prose | pages [19] -->
  

<!-- b000952 | prose | pages [19] -->
a

<!-- b000953 | prose | pages [19] -->


<!-- b000954 | prose | pages [19] -->
 

<!-- b000955 | prose | pages [19] -->


<!-- b000956 | prose | pages [19] -->
 

<!-- b000957 | prose | pages [19] -->
dQ c T t

<!-- b000958 | prose | pages [19] -->
( )

<!-- b000959 | prose | pages [19] -->
K t dV

<!-- b000960 | prose | pages [19] -->
 

<!-- b000961 | prose | pages [19] -->


<!-- b000962 | prose | pages [19] -->
water

<!-- b000963 | prose | pages [19] -->


<!-- b000964 | prose | pages [19] -->
2

<!-- b000965 | prose | pages [19] -->
  

<!-- b000966 | prose | pages [19] -->


<!-- b000967 | prose | pages [19] -->


<!-- b000968 | prose | pages [19] -->


<!-- b000969 | prose | pages [19] -->


<!-- b000970 | prose | pages [19] -->
Q c V t T t

<!-- b000971 | prose | pages [19] -->
( )

<!-- b000972 | prose | pages [19] -->
 

<!-- b000973 | prose | pages [19] -->


<!-- b000974 | prose | pages [19] -->
 

<!-- b000975 | prose | pages [19] -->
T x y z t

<!-- b000976 | prose | pages [19] -->
( , , , )

<!-- b000977 | prose | pages [19] -->
T t

<!-- b000978 | prose | pages [19] -->
( )

<!-- b000979 | prose | pages [19] -->
K t y

<!-- b000980 | prose | pages [19] -->


<!-- b000981 | furniture | pages [19] -->


<!-- b000982 | prose | pages [19] -->
  

<!-- b000983 | prose | pages [19] -->
dQ dQ dQ

<!-- b000984 | prose | pages [19] -->
 

<!-- b000985 | prose | pages [19] -->
body radiation water water

<!-- b000986 | prose | pages [19] -->
 

<!-- b000987 | prose | pages [19] -->
     

<!-- b000988 | prose | pages [19] -->
aH

<!-- b000989 | prose | pages [19] -->
2

<!-- b000990 | prose | pages [19] -->
bH h T t

<!-- b000991 | prose | pages [19] -->
( )

<!-- b000992 | prose | pages [19] -->
T ab dt

<!-- b000993 | prose | pages [19] -->
 

<!-- b000994 | prose | pages [19] -->
0

<!-- b000995 | prose | pages [19] -->
dt dt

<!-- b000996 | prose | pages [19] -->


<!-- b000997 | prose | pages [19] -->
5 5

<!-- b000998 | prose | pages [19] -->
   

<!-- b000999 | prose | pages [19] -->
a a

<!-- b001000 | prose | pages [19] -->
a

<!-- b001001 | prose | pages [19] -->
  

<!-- b001002 | prose | pages [19] -->
  

<!-- b001003 | prose | pages [19] -->
T t

<!-- b001004 | prose | pages [19] -->
( )

<!-- b001005 | prose | pages [19] -->
K t dt

<!-- b001006 | prose | pages [19] -->


<!-- b001007 | prose | pages [19] -->
(13)

<!-- b001008 | prose | pages [19] -->
     

<!-- b001009 | prose | pages [19] -->
2

<!-- b001010 | prose | pages [19] -->
2

<!-- b001011 | prose | pages [19] -->
 

<!-- b001012 | furniture | pages [20] -->
Team #46830

<!-- b001013 | furniture | pages [20] -->


<!-- b001014 | heading | pages [20] -->
4.2 Forced convection model

<!-- b001015 | furniture | pages [20] -->


<!-- b001016 | furniture | pages [20] -->
Page 17 of 45

<!-- b001017 | prose | pages [20] -->
In this section, we set up a model of convection [1][2] heat transfer of water caused by human movement. First we quantify the human movement’s influence on

<!-- b001018 | prose | pages [20] -->
convection, so we define the forced convective cell, use this parameter to describe the

<!-- b001019 | prose | pages [20] -->
human movement’s influence on convection and the temperature distribution. Then we set up a model of the forced convective cell’s influence on the temperature. This

<!-- b001020 | prose | pages [20] -->
model is based on a partial large normal distribution function. Finally, we established a model of the human movement’s influence on the temperature distribution in the bathtub.

<!-- b001021 | heading | pages [20] -->
4.2.1 The introduction of forced convection source

<!-- b001022 | prose | pages [20] -->
kV ) moving (distance= kS ) in a Consider the case of an object (volume=

<!-- b001023 | prose | pages [20] -->
bathtub. In essence, the principle of the movement of the object in water can cause the

<!-- b001024 | prose | pages [20] -->
forced convection of water is: In the process of moving the object pushed a part of the water, while the other water filled to its original position, this process has caused the

<!-- b001025 | prose | pages [20] -->
movement of water and water, to complete this action in the form of flow (Fig 8). As a

<!-- b001026 | prose | pages [20] -->
result, the movement of the object causes the water to flow, while the convection of the water has a corresponding heat exchange.

<!-- b001027 | prose | pages [20] -->
Vk

<!-- b001028 | prose | pages [20] -->
Sk

<!-- b001029 | furniture | pages [20] -->


<!-- b001030 | caption | pages [20] -->
Figure 8: Forced convection cause by body

<!-- b001031 | prose | pages [20] -->
We abstract every movement of a person as an object in the water [6]. Because

<!-- b001032 | prose | pages [20] -->
the movement of a person's bath is a process of moving one part of the body from one

<!-- b001033 | prose | pages [20] -->
position to the other. This process will be pushed the moving path of the water, while the other water filled to its original position, resulting in convection. So we define human motion intensity as the forced convection cell. According to the assumption 11,

<!-- b001034 | prose | pages [20] -->
we use k to mark the number of forced convection, its definition is as follows:

<!-- b001035 | prose | pages [20] -->
F

<!-- b001036 | furniture | pages [20] -->


<!-- b001037 | prose | pages [20] -->
   S V

<!-- b001038 | furniture | pages [20] -->


<!-- b001039 | prose | pages [20] -->
k k k k

<!-- b001040 | furniture | pages [21] -->
Team #46830

<!-- b001041 | furniture | pages [21] -->


<!-- b001042 | furniture | pages [21] -->


<!-- b001043 | furniture | pages [21] -->
Page 18 of 45

<!-- b001044 | prose | pages [21] -->
kV is the volume of the moving part of the body during the k th Where,

<!-- b001045 | prose | pages [21] -->
kS is the distance of the moving part of the body during the k th movement,

<!-- b001046 | prose | pages [21] -->
movement

<!-- b001047 | heading | pages [21] -->
4.2.2 Effect of forced convection on the temperature

<!-- b001048 | prose | pages [21] -->
The movement of people to produce convection, the result of convection is to

<!-- b001049 | prose | pages [21] -->
make the distribution of temperature in the water more balanced. Further considered,

<!-- b001050 | prose | pages [21] -->
F through a non-negative function the forced convection source k f F ( ) so that the k

<!-- b001051 | prose | pages [21] -->
temperature of each point in the water is closer to the average temperature, so we got

<!-- b001052 | prose | pages [21] -->
the formula:

<!-- b001053 | prose | pages [21] -->
 T 1( , , , ) x y z t           (14) ( , , , ) T x y z t  k k f F ( ) T x y z t ( , , , ) T t ( )  k

<!-- b001054 | prose | pages [21] -->
F , the distribution function After the effect of the k th forced convection source

<!-- b001055 | prose | pages [21] -->
kT of water temperature in space became 

<!-- b001056 | prose | pages [21] -->
k

<!-- b001057 | prose | pages [21] -->
1( , , , ) x y z t kT x y z t . ( , , , ) from

<!-- b001058 | prose | pages [21] -->
According to the formula (14), we obtain after a forced convection source affects,

<!-- b001059 | prose | pages [21] -->
the resulting convection only changes the temperature distribution, and doesn’t cause a mutation of the water’s average temperature. This phenomenon is consistent with

<!-- b001060 | prose | pages [21] -->
the hypothesis 6, which shows that the model is self-consistent and reasonable.

<!-- b001061 | prose | pages [21] -->
In addition, we put the water temperature as a function of space and time formula (11) into formula (14), temperature gradient satisfy the following relationship. This

<!-- b001062 | prose | pages [21] -->
formula shows that the distribution of the temperature field is essentially the effect of

<!-- b001063 | prose | pages [21] -->
human motion on the temperature gradient:

<!-- b001064 | prose | pages [21] -->
  K 1( ) t 1  k

<!-- b001065 | prose | pages [21] -->
Then, consider the form of function

<!-- b001066 | prose | pages [21] -->
    f F ( ) K t (15) k k

<!-- b001067 | prose | pages [21] -->
f F ( ( ) . The result of the action of the human k

<!-- b001068 | prose | pages [21] -->
in the bathtub is to promote the mixing of cold water and hot water. Analysis shows

<!-- b001069 | prose | pages [21] -->
that the action is more big, bigger source of forced convection, the influence of water

<!-- b001070 | prose | pages [21] -->
temperature distribution is bigger, but the influence of temperature on forced convection source rate is not increased with the increase of uniform motion.

<!-- b001071 | prose | pages [21] -->
f F ( ) F slow growth, first increases with the growth of The influence rate k k

<!-- b001072 | prose | pages [21] -->
F for the overall flow of water distribution is almost no impact, because too small k

<!-- b001073 | furniture | pages [21] -->


<!-- b001074 | furniture | pages [22] -->
Team #46830

<!-- b001075 | furniture | pages [22] -->


<!-- b001076 | prose | pages [22] -->
F is in this range, the rate of f F ( When k

<!-- b001077 | prose | pages [22] -->
f F Subsequently, the impact rate of

<!-- b001078 | furniture | pages [22] -->


<!-- b001079 | furniture | pages [22] -->
Page 19 of 45

<!-- b001080 | prose | pages [22] -->
) F . is not sensitive to the value of k k k

<!-- b001081 | prose | pages [22] -->
( ( ) F growth, with the rapid growth of k k

<!-- b001082 | prose | pages [22] -->
F and the total amount of water can be compared to the that is, when the value of k

<!-- b001083 | prose | pages [22] -->
F will be sensitive to the value of macro size, the size of k

<!-- b001084 | prose | pages [22] -->
f F ( Finally, the rate of impact of k

<!-- b001085 | prose | pages [22] -->
f F ( ) . k

<!-- b001086 | prose | pages [22] -->
F slow growth, and ) ) with the growth of k

<!-- b001087 | prose | pages [22] -->
F is large enough, the water can be fully mixed, the closer to 1. Because when the k

<!-- b001088 | prose | pages [22] -->
f F ( ) F continues to increase, the will be very close to 1, but when the value of k k

<!-- b001089 | prose | pages [22] -->
forced convection of the source of the water has been able to fully mixed the role has

<!-- b001090 | prose | pages [22] -->
been very small.

<!-- b001091 | prose | pages [22] -->
f F ( ) F should be shown in the with the change of The influence rate of k

<!-- b001092 | prose | pages [22] -->
following figure:

<!-- b001093 | prose | pages [22] -->
k

<!-- b001094 | furniture | pages [22] -->


<!-- b001095 | caption | pages [22] -->
Figure 9: The variation of convective mixing rate over the forced convection

<!-- b001096 | prose | pages [22] -->
Based on the above analysis, we select the partial large state distribution function

<!-- b001097 | prose | pages [22] -->
f F ( as the approximate analytic formula of

<!-- b001098 | prose | pages [22] -->


<!-- b001099 | prose | pages [22] -->
f F

<!-- b001100 | prose | pages [22] -->
( ) 1

<!-- b001101 | prose | pages [22] -->
) : k k

<!-- b001102 | prose | pages [22] -->
2

<!-- b001103 | prose | pages [22] -->
  

<!-- b001104 | prose | pages [22] -->
F F

<!-- b001105 | prose | pages [22] -->
a

<!-- b001106 | prose | pages [22] -->
 

<!-- b001107 | prose | pages [22] -->
F

<!-- b001108 | furniture | pages [22] -->


<!-- b001109 | prose | pages [22] -->
 

<!-- b001110 | prose | pages [22] -->
e

<!-- b001111 | prose | pages [22] -->
b

<!-- b001112 | prose | pages [22] -->
F are all the constants to be determined, the units are F and Where, a b 4 m . We

<!-- b001113 | prose | pages [22] -->
will give the decisive factor of the constant through the following analysis.

<!-- b001114 | prose | pages [22] -->
kF  0 F takes the special value, when Consider the case that the special , that k k

<!-- b001115 | prose | pages [22] -->
person did not make any action, it is obvious that the water temperature distribution of

<!-- b001116 | prose | pages [22] -->
 f (0) 0 kF , the F  0 , can be solved the impact rate of 0, that is,

<!-- b001117 | furniture | pages [22] -->


<!-- b001118 | prose | pages [22] -->
. When a

<!-- b001119 | furniture | pages [23] -->
Team #46830

<!-- b001120 | furniture | pages [23] -->


<!-- b001121 | furniture | pages [23] -->


<!-- b001122 | furniture | pages [23] -->
Page 20 of 45

<!-- b001123 | prose | pages [23] -->
action is very large or even infinite, the water in the bathtub is fully mixed, the

<!-- b001124 | prose | pages [23] -->
temperature distribution becomes very uniform, the mixing rate is infinitely close to 1,

<!-- b001125 | prose | pages [23] -->
. Note that the equation is established, and the results of the

<!-- b001126 | prose | pages [23] -->
that is lim

<!-- b001127 | prose | pages [23] -->
f F

<!-- b001128 | prose | pages [23] -->
( ) 1

<!-- b001129 | prose | pages [23] -->
k  F

<!-- b001130 | prose | pages [23] -->
k

<!-- b001131 | prose | pages [23] -->
model are consistent with the analysis.

<!-- b001132 | prose | pages [23] -->
In particular, when considering the forced convection source value is equal to the

<!-- b001133 | prose | pages [23] -->
half volume of water in the bathtub multiplied by the value of the long side of the

<!-- b001134 | prose | pages [23] -->
1  . This formula says bath half water movement from the left half bathtub kF V a 0 2

<!-- b001135 | prose | pages [23] -->
side of the movement to the right side, back into the left half side, the moving distance

<!-- b001136 | prose | pages [23] -->
is 1 1   . This process will make the water in the bathtub more fully mixed, a a a 2 2

<!-- b001137 | prose | pages [23] -->
because of the forced convection the distribution of temperature becomes more

<!-- b001138 | prose | pages [23] -->
average. In fact, we can determine the influence rate by the test of the variance of the

<!-- b001139 | prose | pages [23] -->
temperature before and after the experiment according to 4.1.3-3 and 4.2.2-2. In this, in order to facilitate the calculation of the subsequent model, we may wish to set

<!-- b001140 | prose | pages [23] -->
1 V a  f ( ) 95% , which can be obtained F 0 a 2   . 4 0.191378 m

<!-- b001141 | prose | pages [23] -->
Here, we have established a concise and practical mathematical model for the effect of forced convection on human motion:

<!-- b001142 | prose | pages [23] -->
 

<!-- b001143 | prose | pages [23] -->
F S V

<!-- b001144 | prose | pages [23] -->
k k

<!-- b001145 | prose | pages [23] -->


<!-- b001146 | prose | pages [23] -->
2

<!-- b001147 | prose | pages [23] -->
 

<!-- b001148 | prose | pages [23] -->
F

<!-- b001149 | prose | pages [23] -->


<!-- b001150 | prose | pages [23] -->
 

<!-- b001151 | prose | pages [23] -->
F

<!-- b001152 | prose | pages [23] -->


<!-- b001153 | prose | pages [23] -->
 

<!-- b001154 | prose | pages [23] -->
f F

<!-- b001155 | prose | pages [23] -->
( ) 1

<!-- b001156 | prose | pages [23] -->
e

<!-- b001157 | prose | pages [23] -->


<!-- b001158 | prose | pages [23] -->
b

<!-- b001159 | prose | pages [23] -->
 

<!-- b001160 | prose | pages [23] -->
T

<!-- b001161 | prose | pages [23] -->
( , , , )

<!-- b001162 | prose | pages [23] -->
x y z t T x y z t

<!-- b001163 | prose | pages [23] -->
( , , , )

<!-- b001164 | prose | pages [23] -->


<!-- b001165 | prose | pages [23] -->


<!-- b001166 | prose | pages [23] -->
k

<!-- b001167 | prose | pages [23] -->
1

<!-- b001168 | prose | pages [23] -->
k

<!-- b001169 | prose | pages [23] -->


<!-- b001170 | furniture | pages [23] -->


<!-- b001171 | prose | pages [23] -->
     

<!-- b001172 | prose | pages [23] -->
f F

<!-- b001173 | prose | pages [23] -->
( )

<!-- b001174 | prose | pages [23] -->
T x y z t

<!-- b001175 | prose | pages [23] -->
( , , , )

<!-- b001176 | prose | pages [23] -->
T t

<!-- b001177 | prose | pages [23] -->
( )

<!-- b001178 | prose | pages [23] -->
 

<!-- b001179 | prose | pages [23] -->
k

<!-- b001180 | heading | pages [23] -->
4.3 The human body comfort model

<!-- b001181 | prose | pages [23] -->
In this part, we establish and solve the model of human body's comfortable

<!-- b001182 | prose | pages [23] -->
degree of thermal sensation. This model describes the human body's temperature perception of comfort, the comfort of this gives a quantitative results. In subsequent

<!-- b001183 | prose | pages [23] -->
discussions, the body's temperature perception of comfort will also be used as a part

<!-- b001184 | prose | pages [23] -->
of the bath strategy needs to be taken into account.

<!-- b001185 | heading | pages [23] -->
4.3.1 Establish human body comfort model

<!-- b001186 | prose | pages [23] -->
We have established the human comfort model by using the normal distribution.

<!-- b001187 | prose | pages [23] -->
We consider the human body has a specific optimum bath temperature, when the

<!-- b001188 | furniture | pages [23] -->


<!-- b001189 | furniture | pages [24] -->
Team #46830

<!-- b001190 | furniture | pages [24] -->


<!-- b001191 | furniture | pages [24] -->


<!-- b001192 | furniture | pages [24] -->
Page 21 of 45

<!-- b001193 | prose | pages [24] -->
water temperature is higher than the temperature comfortable degree decline, and

<!-- b001194 | prose | pages [24] -->
gradually feel the heat, even burn; when the water temperature is lower than the temperature of comfort will also decline, people will gradually feel the cold, even

<!-- b001195 | prose | pages [24] -->
suffer from cold.

<!-- b001196 | prose | pages [24] -->
Because the normal distribution is widespread in nature, the unimodal normal distribution are consistent with the perception of comfort temperature In addition,

<!-- b001197 | prose | pages [24] -->
when the temperature exceeds a certain value people will be burned, or temperature below a certain value people will get cold. At this time, the feelings of the people are not comfortable, so comfort should close to zero, the characteristic with normal

<!-- b001198 | prose | pages [24] -->
distribution are in good agreement.

<!-- b001199 | prose | pages [24] -->
Therefore, we choose the normal distribution function to describe the distribution of the body's comfort with temperature, that is, the following expressions:

<!-- b001200 | prose | pages [24] -->
1

<!-- b001201 | prose | pages [24] -->


<!-- b001202 | prose | pages [24] -->


<!-- b001203 | prose | pages [24] -->
2

<!-- b001204 | prose | pages [24] -->


<!-- b001205 | prose | pages [24] -->


<!-- b001206 | prose | pages [24] -->
 

<!-- b001207 | prose | pages [24] -->
T B

<!-- b001208 | prose | pages [24] -->
  

<!-- b001209 | prose | pages [24] -->


<!-- b001210 | furniture | pages [24] -->


<!-- b001211 | prose | pages [24] -->
 

<!-- b001212 | prose | pages [24] -->
e

<!-- b001213 | prose | pages [24] -->


<!-- b001214 | prose | pages [24] -->
2

<!-- b001215 | prose | pages [24] -->
 

<!-- b001216 | prose | pages [24] -->
Where, represents the most comfortable temperature of human body feeling,

<!-- b001217 | prose | pages [24] -->
represents the standard deviation of the comfortable feeling degree of human body to the temperature.

<!-- b001218 | heading | pages [24] -->
4.3.2 Solution of human body comfort model

<!-- b001219 | prose | pages [24] -->
Taking into account the temperature of the most comfortable temperature in the

<!-- b001220 | prose | pages [24] -->
vicinity of 2 times the standard deviation of the sum of the 95.45%, that is, when the temperature is not within this range, the cumulative amount of satisfaction of the

<!-- b001221 | prose | pages [24] -->
cumulative amount of less than 4.55% of the total amount of comfort.

<!-- b001222 | prose | pages [24] -->
On the other hand, the data show that the human feelings to nociceptive

<!-- b001223 | prose | pages [24] -->
temperature is 306K, human feel hot temperature is 318k, so the temperature outside

<!-- b001224 | prose | pages [24] -->
the scope of this comfort will be very low, outside the scope of the comfortable cumulative value is at a rather low level.

<!-- b001225 | prose | pages [24] -->
May in this range of comfort for the cumulative value of the sum of 95.45%.

<!-- b001226 | prose | pages [24] -->
Doing so for a reason: in statistics normal distribution of twice the standard deviation is often used as to judge whether an event is a small probability event, and in this

<!-- b001227 | prose | pages [24] -->
article, in this article, it is considered that the water temperature above 318K or below

<!-- b001228 | prose | pages [24] -->
306K is unacceptable therefore can be equated to the small probability events in statistics. So it is reasonable to do so.

<!-- b001229 | prose | pages [24] -->
By the above analysis, we can get the following equations

<!-- b001230 | furniture | pages [24] -->


<!-- b001231 | furniture | pages [25] -->
Team #46830

<!-- b001232 | furniture | pages [25] -->


<!-- b001233 | prose | pages [25] -->


<!-- b001234 | prose | pages [25] -->


<!-- b001235 | prose | pages [25] -->


<!-- b001236 | prose | pages [25] -->
306

<!-- b001237 | prose | pages [25] -->
 

<!-- b001238 | prose | pages [25] -->
318

<!-- b001239 | prose | pages [25] -->


<!-- b001240 | prose | pages [25] -->
318

<!-- b001241 | prose | pages [25] -->


<!-- b001242 | prose | pages [25] -->


<!-- b001243 | prose | pages [25] -->


<!-- b001244 | prose | pages [25] -->
306

<!-- b001245 | furniture | pages [25] -->


<!-- b001246 | furniture | pages [25] -->
Page 22 of 45

<!-- b001247 | prose | pages [25] -->
318 318

<!-- b001248 | prose | pages [25] -->


<!-- b001249 | prose | pages [25] -->
dT

<!-- b001250 | prose | pages [25] -->
B

<!-- b001251 | prose | pages [25] -->


<!-- b001252 | prose | pages [25] -->


<!-- b001253 | prose | pages [25] -->


<!-- b001254 | furniture | pages [25] -->


<!-- b001255 | prose | pages [25] -->
306

<!-- b001256 | prose | pages [25] -->


<!-- b001257 | prose | pages [25] -->
dT dT

<!-- b001258 | prose | pages [25] -->
95.45%

<!-- b001259 | prose | pages [25] -->
B

<!-- b001260 | prose | pages [25] -->
So we get the solution of the model of human body comfort:

<!-- b001261 | prose | pages [25] -->
1

<!-- b001262 | prose | pages [25] -->


<!-- b001263 | prose | pages [25] -->


<!-- b001264 | prose | pages [25] -->


<!-- b001265 | prose | pages [25] -->
3 2

<!-- b001266 | prose | pages [25] -->
 

<!-- b001267 | prose | pages [25] -->
2

<!-- b001268 | prose | pages [25] -->


<!-- b001269 | prose | pages [25] -->
T

<!-- b001270 | prose | pages [25] -->
312

<!-- b001271 | prose | pages [25] -->
B

<!-- b001272 | prose | pages [25] -->
  

<!-- b001273 | furniture | pages [25] -->


<!-- b001274 | prose | pages [25] -->
e

<!-- b001275 | prose | pages [25] -->
9

<!-- b001276 | prose | pages [25] -->
The above formula shows that the human body to feel the most comfortable

<!-- b001277 | prose | pages [25] -->
temperature is 312K, and by the state distribution characteristics we can know,

<!-- b001278 | prose | pages [25] -->
temperature range in   K the cumulative comfort of total sum of 68.26%, 309 K ,315

<!-- b001279 | prose | pages [25] -->
temperature range in   K total comfort reached 99.7% of the total. So we 303 ,321 K

<!-- b001280 | prose | pages [25] -->
think that when the temperature is above 321K or below 303K is completely unacceptable, people will be burned or cold due to these temperatures.

<!-- b001281 | prose | pages [25] -->
In comparison with literature data, we found that the burn the body temperature

<!-- b001282 | prose | pages [25] -->
of 47 degrees Celsius (320K) ,the relative error of the scald temperature predicted by the human body comfort model

<!-- b001283 | prose | pages [25] -->
 320 K 321 K   100% 0.3125%

<!-- b001284 | prose | pages [25] -->
we have established is only

<!-- b001285 | prose | pages [25] -->
, indicating that the model coincide with the actual 320 K

<!-- b001286 | prose | pages [25] -->
situation very well.

<!-- b001287 | heading | pages [25] -->
4.4 Optimized control model of bathing strategy

<!-- b001288 | prose | pages [25] -->
In this section, based on the models we established previously, we get the optimized control model of bathing strategy.

<!-- b001289 | prose | pages [25] -->
We note that the water temperature is reduced when users are in the bath, then they open the hot water faucet to heat the water. We need to develop a water injection

<!-- b001290 | prose | pages [25] -->
scheme, to make the temperature of the water temperature maintained at a level which is close to the initial water temperature and won't get water temperature too high to

<!-- b001291 | prose | pages [25] -->
decline the comfort of users or even hurt. Thus, we propose two kinds of injection

<!-- b001292 | prose | pages [25] -->
scheme towards two different controlling ways:

<!-- b001293 | prose | pages [25] -->
1. Control artificially to make the water in the bathtub maintain a long-term

<!-- b001294 | prose | pages [25] -->
comfortable temperature and hope that the operation is simple, so keep the tap a

<!-- b001295 | prose | pages [25] -->
trickle.

<!-- b001296 | prose | pages [25] -->
2. Control automatically. When the sensor accept the signal that the water

<!-- b001297 | prose | pages [25] -->
temperature is reduced to a certain critical temperature, the tap is automatically

<!-- b001298 | furniture | pages [25] -->


<!-- b001299 | furniture | pages [26] -->
Team #46830

<!-- b001300 | furniture | pages [26] -->


<!-- b001301 | furniture | pages [26] -->


<!-- b001302 | furniture | pages [26] -->
Page 23 of 45

<!-- b001303 | prose | pages [26] -->
controlled to the maximum. When water temperature is picked up to a certain value,

<!-- b001304 | prose | pages [26] -->
the faucet is turned off. The tap repeated this cycle before the end.

<!-- b001305 | heading | pages [26] -->
4.4.1 Strategy I

<!-- b001306 | prose | pages [26] -->
Constant flooding strategy: After users have entered the tub bath, the flow rate

<!-- b001307 | prose | pages [26] -->
bT  to maintain the bk which has a certain temperature of always keep constant in

<!-- b001308 | prose | pages [26] -->
bath tub water temperature. This strategy makes it easy to operate, suitable for

<!-- b001309 | prose | pages [26] -->
ordinary hot water supply system which needs manual operation, and the parameters

<!-- b001310 | prose | pages [26] -->
bT . So this plan has considerable practical reference bk and to be optimized only be

<!-- b001311 | prose | pages [26] -->
value for manual operation.

<!-- b001312 | prose | pages [26] -->
Now we need to optimize the strategy’s variable, to find the optimal water flow

<!-- b001313 | prose | pages [26] -->
bk and temperature of hot water injection bT .

<!-- b001314 | prose | pages [26] -->
First, we show the optimization objective function. In view of the user who wishes to make water temperature when he get into the bath as close to the l temperature of he has taking the shower, which can be abstracted to a mathematical

<!-- b001315 | prose | pages [26] -->
expression, make the average difference of initial temperature and the average

<!-- b001316 | prose | pages [26] -->
temperature in period of time to be least, which can b show in the following expression.

<!-- b001317 | prose | pages [26] -->


<!-- b001318 | prose | pages [26] -->
min

<!-- b001319 | prose | pages [26] -->
  

<!-- b001320 | prose | pages [26] -->
t t

<!-- b001321 | prose | pages [26] -->


<!-- b001322 | prose | pages [26] -->
m m

<!-- b001323 | prose | pages [26] -->
T T t dt

<!-- b001324 | prose | pages [26] -->
( )

<!-- b001325 | prose | pages [26] -->
  

<!-- b001326 | prose | pages [26] -->
0 0 0

<!-- b001327 | furniture | pages [26] -->


<!-- b001328 | prose | pages [26] -->
t

<!-- b001329 | prose | pages [26] -->
m

<!-- b001330 | prose | pages [26] -->
In addition, users do not want to waste too much water just for maintaining the

<!-- b001331 | prose | pages [26] -->
water temperature, so the user will control the flow of water injection so that the

<!-- b001332 | prose | pages [26] -->
waste water will be controlled, which can be abstracted in mathematical expression of the minimum of flow rate, the expression is as follows:

<!-- b001333 | prose | pages [26] -->
min bk

<!-- b001334 | prose | pages [26] -->
In view of the added hot water temperature cannot be too high. As the high

<!-- b001335 | prose | pages [26] -->
temperature is likely to affect user’s comfort, even scald users, so it’s necessary to consider the impact of hot water to the user's comfort. Clearly, in our optimization strategy, it should be ensure the comfort get a maximum under certain conditions, the

<!-- b001336 | prose | pages [26] -->
expression is as follows:

<!-- b001337 | prose | pages [26] -->


<!-- b001338 | prose | pages [26] -->


<!-- b001339 | prose | pages [26] -->
max

<!-- b001340 | prose | pages [26] -->
3 2

<!-- b001341 | prose | pages [26] -->
 

<!-- b001342 | prose | pages [26] -->
2

<!-- b001343 | prose | pages [26] -->


<!-- b001344 | prose | pages [26] -->
T

<!-- b001345 | prose | pages [26] -->
312 1 1

<!-- b001346 | prose | pages [26] -->
B

<!-- b001347 | prose | pages [26] -->
 

<!-- b001348 | prose | pages [26] -->
e

<!-- b001349 | furniture | pages [26] -->


<!-- b001350 | prose | pages [26] -->
9

<!-- b001351 | prose | pages [26] -->


<!-- b001352 | prose | pages [26] -->
Considering the above three factors, we get the final optimization objective

<!-- b001353 | furniture | pages [26] -->


<!-- b001354 | furniture | pages [27] -->
Team #46830

<!-- b001355 | furniture | pages [27] -->


<!-- b001356 | prose | pages [27] -->
function:

<!-- b001357 | prose | pages [27] -->
 

<!-- b001358 | prose | pages [27] -->
t

<!-- b001359 | prose | pages [27] -->
 

<!-- b001360 | prose | pages [27] -->
m

<!-- b001361 | prose | pages [27] -->
T T t dt

<!-- b001362 | prose | pages [27] -->
( )

<!-- b001363 | prose | pages [27] -->
 

<!-- b001364 | prose | pages [27] -->
0 0

<!-- b001365 | prose | pages [27] -->


<!-- b001366 | prose | pages [27] -->


<!-- b001367 | prose | pages [27] -->
min 1

<!-- b001368 | prose | pages [27] -->
t

<!-- b001369 | prose | pages [27] -->
m

<!-- b001370 | furniture | pages [27] -->


<!-- b001371 | furniture | pages [27] -->
Page 24 of 45

<!-- b001372 | prose | pages [27] -->
 

<!-- b001373 | prose | pages [27] -->
2

<!-- b001374 | prose | pages [27] -->


<!-- b001375 | prose | pages [27] -->
T

<!-- b001376 | prose | pages [27] -->
312 1

<!-- b001377 | prose | pages [27] -->
B

<!-- b001378 | prose | pages [27] -->
  

<!-- b001379 | prose | pages [27] -->


<!-- b001380 | prose | pages [27] -->
 

<!-- b001381 | prose | pages [27] -->


<!-- b001382 | prose | pages [27] -->
 

<!-- b001383 | prose | pages [27] -->
k t e

<!-- b001384 | furniture | pages [27] -->


<!-- b001385 | prose | pages [27] -->
9 2

<!-- b001386 | prose | pages [27] -->
b m

<!-- b001387 | prose | pages [27] -->
3

<!-- b001388 | prose | pages [27] -->


<!-- b001389 | prose | pages [27] -->
3 2

<!-- b001390 | prose | pages [27] -->
3 is the weight of temperature factor, water factor and comfort , 1, Where 2

<!-- b001391 | prose | pages [27] -->
factor respectively, whose value can be determined by the user's preferences. Symbol on the third function is negative because we have done a minimization process in

<!-- b001392 | prose | pages [27] -->
three factors, which means the smaller value the more excellent program.

<!-- b001393 | prose | pages [27] -->
Second, we give the optimization constraints. Considering the hot water faucet

<!-- b001394 | prose | pages [27] -->
has a maximum of flow rate, we get the first constraint:

<!-- b001395 | prose | pages [27] -->
 0 bk 

<!-- b001396 | furniture | pages [27] -->


<!-- b001397 | prose | pages [27] -->
k max

<!-- b001398 | prose | pages [27] -->
The temperature of injection water should be higher than the user's body temperature clearly. Otherwise users will dissipate heat in the water and feel cold. In

<!-- b001399 | prose | pages [27] -->
addition, the temperature of boiling water which poured to should not make the user

<!-- b001400 | prose | pages [27] -->
burn. As the second constraint:

<!-- b001401 | prose | pages [27] -->
T body     T T

<!-- b001402 | furniture | pages [27] -->


<!-- b001403 | prose | pages [27] -->
b highest

<!-- b001404 | prose | pages [27] -->
Next we consider the constraints associated with the temperature, make the relationship between the average temperature and internal energy to be a third

<!-- b001405 | prose | pages [27] -->
constraint:

<!-- b001406 | prose | pages [27] -->
T t ( ) Q  

<!-- b001407 | furniture | pages [27] -->


<!-- b001408 | prose | pages [27] -->
 c V 0

<!-- b001409 | prose | pages [27] -->
The changes of the water temperature and the distribution of water is controlled by the universal thermodynamic model formula (13). Because of space limitations we just give the water heat differential equation here:

<!-- b001410 | prose | pages [27] -->
   dQ dQ dQ exchange evaporation    dQ dQ dQ dQ

<!-- b001411 | furniture | pages [27] -->


<!-- b001412 | prose | pages [27] -->
  body radiation water water

<!-- b001413 | prose | pages [27] -->
Moreover, it should also consider the user’s normal bathing time, based on the

<!-- b001414 | prose | pages [27] -->
life knowledge we take the longest bath time for 30 minutes, so we obtain a fifth constraint:

<!-- b001415 | prose | pages [27] -->
 mt 1800 s

<!-- b001416 | furniture | pages [27] -->


<!-- b001417 | prose | pages [27] -->
To sum up, we have established the optimal control model of a strategy 1 :

<!-- b001418 | furniture | pages [27] -->


<!-- b001419 | furniture | pages [28] -->
Team #46830

<!-- b001420 | furniture | pages [28] -->


<!-- b001421 | prose | pages [28] -->
 

<!-- b001422 | prose | pages [28] -->
t

<!-- b001423 | prose | pages [28] -->


<!-- b001424 | prose | pages [28] -->


<!-- b001425 | prose | pages [28] -->
m

<!-- b001426 | prose | pages [28] -->
T T t dt

<!-- b001427 | prose | pages [28] -->
( )

<!-- b001428 | prose | pages [28] -->
 

<!-- b001429 | prose | pages [28] -->
0 0

<!-- b001430 | prose | pages [28] -->


<!-- b001431 | prose | pages [28] -->
 

<!-- b001432 | prose | pages [28] -->


<!-- b001433 | prose | pages [28] -->


<!-- b001434 | prose | pages [28] -->
min

<!-- b001435 | prose | pages [28] -->
k t

<!-- b001436 | prose | pages [28] -->
1 2

<!-- b001437 | prose | pages [28] -->
b m

<!-- b001438 | prose | pages [28] -->
t

<!-- b001439 | prose | pages [28] -->
m

<!-- b001440 | prose | pages [28] -->
 

<!-- b001441 | prose | pages [28] -->
0

<!-- b001442 | prose | pages [28] -->
k k

<!-- b001443 | prose | pages [28] -->
b

<!-- b001444 | prose | pages [28] -->
max

<!-- b001445 | prose | pages [28] -->
   

<!-- b001446 | prose | pages [28] -->
T T T

<!-- b001447 | prose | pages [28] -->


<!-- b001448 | prose | pages [28] -->
body b highest

<!-- b001449 | prose | pages [28] -->


<!-- b001450 | prose | pages [28] -->
Q

<!-- b001451 | prose | pages [28] -->


<!-- b001452 | prose | pages [28] -->
s t T t

<!-- b001453 | prose | pages [28] -->
. .

<!-- b001454 | prose | pages [28] -->
( )

<!-- b001455 | prose | pages [28] -->


<!-- b001456 | prose | pages [28] -->


<!-- b001457 | prose | pages [28] -->
c V

<!-- b001458 | prose | pages [28] -->


<!-- b001459 | prose | pages [28] -->
0

<!-- b001460 | prose | pages [28] -->
   

<!-- b001461 | prose | pages [28] -->
dQ dQ dQ

<!-- b001462 | prose | pages [28] -->


<!-- b001463 | prose | pages [28] -->
exchange evaporation

<!-- b001464 | prose | pages [28] -->
 

<!-- b001465 | prose | pages [28] -->
t

<!-- b001466 | prose | pages [28] -->
1800

<!-- b001467 | prose | pages [28] -->
s

<!-- b001468 | prose | pages [28] -->
m

<!-- b001469 | heading | pages [28] -->
4.4.2 Strategy II

<!-- b001470 | furniture | pages [28] -->


<!-- b001471 | furniture | pages [28] -->
Page 25 of 45

<!-- b001472 | prose | pages [28] -->
 

<!-- b001473 | prose | pages [28] -->
2

<!-- b001474 | prose | pages [28] -->


<!-- b001475 | prose | pages [28] -->
T

<!-- b001476 | prose | pages [28] -->
312

<!-- b001477 | prose | pages [28] -->
1

<!-- b001478 | prose | pages [28] -->
B

<!-- b001479 | prose | pages [28] -->


<!-- b001480 | prose | pages [28] -->


<!-- b001481 | prose | pages [28] -->


<!-- b001482 | prose | pages [28] -->
 

<!-- b001483 | prose | pages [28] -->
e

<!-- b001484 | prose | pages [28] -->
9 3

<!-- b001485 | prose | pages [28] -->


<!-- b001486 | prose | pages [28] -->
3 2

<!-- b001487 | furniture | pages [28] -->


<!-- b001488 | prose | pages [28] -->
  

<!-- b001489 | prose | pages [28] -->
dQ dQ dQ dQ

<!-- b001490 | prose | pages [28] -->
 

<!-- b001491 | prose | pages [28] -->
body radiation water water

<!-- b001492 | prose | pages [28] -->
Temperature switch strategy: When the minimum temperature in the bath is

<!-- b001493 | prose | pages [28] -->
T bT  is injected into , the hot water with the temperature reduced to a critical value min1

<!-- b001494 | prose | pages [28] -->
T the tub. When the minimum temperature in tub inclines to a certain value of , min 2

<!-- b001495 | prose | pages [28] -->
the water injection stops. The tap switch repeated this cycle before the end. This

<!-- b001496 | prose | pages [28] -->
strategy is based on the consideration of automation control, and the strategy essentially is a self-regulation of the hot water supply system towards the change of

<!-- b001497 | prose | pages [28] -->
temperature in. The system can rely on the temperature sensor to accurately identify

<!-- b001498 | prose | pages [28] -->
the current water temperature, and control the tap frequently to switch, so as to control the water temperature carefully. Thus the scheme is practical and meaningful.

<!-- b001499 | prose | pages [28] -->
Then we need to optimize the variate of the strategy and search the critical value

<!-- b001500 | prose | pages [28] -->
T T bT . and the temperature of the injection water of the temperature switch 、min 2 min1

<!-- b001501 | prose | pages [28] -->
First, we propose the optimized objective function. Because the process is piecewise continuous, the temperature changes according to 2 different functions after

<!-- b001502 | prose | pages [28] -->
opening and closing the switch. Then, the optimized objective function should also be

<!-- b001503 | prose | pages [28] -->
piecewise continuous. Moreover, we note that users hope water temperature as close as possible to the initial temperature, then abstract the equation so as to render the

<!-- b001504 | prose | pages [28] -->
mean value of the difference between the initial water temperature and the average

<!-- b001505 | prose | pages [28] -->
water temperature at a certain time is minimum. The expression is as follows:

<!-- b001506 | prose | pages [28] -->
n

<!-- b001507 | prose | pages [28] -->


<!-- b001508 | prose | pages [28] -->


<!-- b001509 | prose | pages [28] -->
i

<!-- b001510 | prose | pages [28] -->
1

<!-- b001511 | prose | pages [28] -->
min

<!-- b001512 | prose | pages [28] -->
 

<!-- b001513 | prose | pages [28] -->
t t

<!-- b001514 | prose | pages [28] -->


<!-- b001515 | prose | pages [28] -->
 

<!-- b001516 | prose | pages [28] -->
i i

<!-- b001517 | prose | pages [28] -->
1

<!-- b001518 | prose | pages [28] -->
T T t dt

<!-- b001519 | prose | pages [28] -->
( )

<!-- b001520 | prose | pages [28] -->
 

<!-- b001521 | prose | pages [28] -->
0

<!-- b001522 | prose | pages [28] -->
t t

<!-- b001523 | prose | pages [28] -->
i i

<!-- b001524 | furniture | pages [28] -->


<!-- b001525 | prose | pages [28] -->
n

<!-- b001526 | prose | pages [28] -->


<!-- b001527 | prose | pages [28] -->
t

<!-- b001528 | prose | pages [28] -->
i

<!-- b001529 | prose | pages [28] -->


<!-- b001530 | prose | pages [28] -->
i

<!-- b001531 | prose | pages [28] -->
1

<!-- b001532 | prose | pages [28] -->
Here, is for the 2 different equations at the situation after the opening and

<!-- b001533 | furniture | pages [28] -->


<!-- b001534 | furniture | pages [29] -->
Team #46830

<!-- b001535 | furniture | pages [29] -->


<!-- b001536 | prose | pages [29] -->
closing of the switch.

<!-- b001537 | furniture | pages [29] -->


<!-- b001538 | furniture | pages [29] -->
Page 26 of 45

<!-- b001539 | prose | pages [29] -->
To save water as much as possible, while the flow is a constant and the water consumption is in direct proportion to the time of the tap opening. If the first time to

<!-- b001540 | prose | pages [29] -->
 t t 1t , then every interval of injection is open the tap is

<!-- b001541 | prose | pages [29] -->
following objective functions:

<!-- b001542 | prose | pages [29] -->


<!-- b001543 | prose | pages [29] -->
n

<!-- b001544 | prose | pages [29] -->
 

<!-- b001545 | prose | pages [29] -->
2

<!-- b001546 | prose | pages [29] -->


<!-- b001547 | prose | pages [29] -->
min

<!-- b001548 | prose | pages [29] -->


<!-- b001549 | prose | pages [29] -->
k

<!-- b001550 | prose | pages [29] -->
1

<!-- b001551 | prose | pages [29] -->
 n

<!-- b001552 | prose | pages [29] -->
. Here comes our  2 k 2 k 1

<!-- b001553 | prose | pages [29] -->
1 1

<!-- b001554 | prose | pages [29] -->
  

<!-- b001555 | prose | pages [29] -->


<!-- b001556 | prose | pages [29] -->
t t t

<!-- b001557 | furniture | pages [29] -->


<!-- b001558 | prose | pages [29] -->


<!-- b001559 | prose | pages [29] -->
2

<!-- b001560 | prose | pages [29] -->
k

<!-- b001561 | prose | pages [29] -->
2

<!-- b001562 | prose | pages [29] -->
k

<!-- b001563 | prose | pages [29] -->
1

<!-- b001564 | prose | pages [29] -->
n , n means the number of the tap

<!-- b001565 | prose | pages [29] -->
means the integral part of

<!-- b001566 | prose | pages [29] -->
Where,

<!-- b001567 | prose | pages [29] -->
 2 

<!-- b001568 | prose | pages [29] -->
operations.

<!-- b001569 | prose | pages [29] -->
2

<!-- b001570 | prose | pages [29] -->
In addition, we consider that the comfort level should be maximum under certain conditions. Here comes the following expression:

<!-- b001571 | prose | pages [29] -->
Considering three factors above comprehensively, we get the optimization

<!-- b001572 | prose | pages [29] -->
objective function similar to strategy two:

<!-- b001573 | prose | pages [29] -->
n

<!-- b001574 | prose | pages [29] -->
  

<!-- b001575 | prose | pages [29] -->
t

<!-- b001576 | prose | pages [29] -->


<!-- b001577 | prose | pages [29] -->


<!-- b001578 | prose | pages [29] -->
i

<!-- b001579 | prose | pages [29] -->
1

<!-- b001580 | prose | pages [29] -->
T T t dt

<!-- b001581 | prose | pages [29] -->
( )

<!-- b001582 | prose | pages [29] -->
 

<!-- b001583 | prose | pages [29] -->
0

<!-- b001584 | prose | pages [29] -->
t

<!-- b001585 | prose | pages [29] -->
 

<!-- b001586 | prose | pages [29] -->
i

<!-- b001587 | prose | pages [29] -->


<!-- b001588 | prose | pages [29] -->


<!-- b001589 | prose | pages [29] -->


<!-- b001590 | prose | pages [29] -->


<!-- b001591 | prose | pages [29] -->


<!-- b001592 | prose | pages [29] -->
i

<!-- b001593 | prose | pages [29] -->
1

<!-- b001594 | prose | pages [29] -->
min

<!-- b001595 | prose | pages [29] -->
2 2

<!-- b001596 | prose | pages [29] -->
n

<!-- b001597 | prose | pages [29] -->


<!-- b001598 | prose | pages [29] -->
t

<!-- b001599 | prose | pages [29] -->
i

<!-- b001600 | prose | pages [29] -->


<!-- b001601 | prose | pages [29] -->
i

<!-- b001602 | prose | pages [29] -->
1

<!-- b001603 | prose | pages [29] -->


<!-- b001604 | prose | pages [29] -->
n n

<!-- b001605 | prose | pages [29] -->
1

<!-- b001606 | prose | pages [29] -->
 

<!-- b001607 | prose | pages [29] -->
2

<!-- b001608 | prose | pages [29] -->
  

<!-- b001609 | prose | pages [29] -->
T

<!-- b001610 | prose | pages [29] -->
312

<!-- b001611 | prose | pages [29] -->
 

<!-- b001612 | prose | pages [29] -->
2 2

<!-- b001613 | prose | pages [29] -->
1

<!-- b001614 | prose | pages [29] -->
B

<!-- b001615 | prose | pages [29] -->


<!-- b001616 | prose | pages [29] -->


<!-- b001617 | prose | pages [29] -->
 

<!-- b001618 | prose | pages [29] -->
  

<!-- b001619 | prose | pages [29] -->


<!-- b001620 | prose | pages [29] -->
 

<!-- b001621 | prose | pages [29] -->
t t e

<!-- b001622 | prose | pages [29] -->
9

<!-- b001623 | furniture | pages [29] -->


<!-- b001624 | prose | pages [29] -->


<!-- b001625 | prose | pages [29] -->
2

<!-- b001626 | prose | pages [29] -->
k

<!-- b001627 | prose | pages [29] -->
2

<!-- b001628 | prose | pages [29] -->
k

<!-- b001629 | prose | pages [29] -->
1 3

<!-- b001630 | prose | pages [29] -->


<!-- b001631 | prose | pages [29] -->
3 2

<!-- b001632 | prose | pages [29] -->
 

<!-- b001633 | prose | pages [29] -->
k k

<!-- b001634 | prose | pages [29] -->
1

<!-- b001635 | prose | pages [29] -->
Second, we propose the constraint conditions of optimization. Obviously, the

<!-- b001636 | prose | pages [29] -->
temperature of the injection water should be higher than the user’s temperature. In addition, the injection water can’t scald the user. Moreover, the lower critical value

<!-- b001637 | prose | pages [29] -->
T T aren’t supposed to exceed the higher one min1 which should be lower than min 2

<!-- b001638 | prose | pages [29] -->
bT . Or the higher critical value is impossible to the temperature of the injection water

<!-- b001639 | prose | pages [29] -->
reach. Here comes the first constraint condition:

<!-- b001640 | prose | pages [29] -->
  T T T body min1   T T

<!-- b001641 | furniture | pages [29] -->


<!-- b001642 | prose | pages [29] -->
min2 b highest

<!-- b001643 | prose | pages [29] -->
The second constraint condition is the relationship between the average

<!-- b001644 | prose | pages [29] -->
temperature and the internal energy:

<!-- b001645 | prose | pages [29] -->
T t ( ) Q  

<!-- b001646 | furniture | pages [29] -->


<!-- b001647 | prose | pages [29] -->
 c V 0

<!-- b001648 | prose | pages [29] -->
Finally, the water temperature change and distribution are controlled by the

<!-- b001649 | prose | pages [29] -->
universal thermodynamic model of water (Eq. 4.1.4-1). However, the differential equation after the opening and closing of the switch is quite different. To unify the

<!-- b001650 | prose | pages [29] -->
expression of these two processes, we set a 0-1 variable .

<!-- b001651 | furniture | pages [29] -->


<!-- b001652 | furniture | pages [30] -->
Team #46830

<!-- b001653 | furniture | pages [30] -->


<!-- b001654 | prose | pages [30] -->


<!-- b001655 | prose | pages [30] -->
 

<!-- b001656 | prose | pages [30] -->
1

<!-- b001657 | prose | pages [30] -->


<!-- b001658 | prose | pages [30] -->
 0

<!-- b001659 | prose | pages [30] -->


<!-- b001660 | prose | pages [30] -->
 n   q 1,2,3, , 1

<!-- b001661 | furniture | pages [30] -->


<!-- b001662 | furniture | pages [30] -->
Page 27 of 45

<!-- b001663 | prose | pages [30] -->
 

<!-- b001664 | prose | pages [30] -->
k 2 q 1

<!-- b001665 | furniture | pages [30] -->


<!-- b001666 | prose | pages [30] -->


<!-- b001667 | prose | pages [30] -->
k 2 q

<!-- b001668 | prose | pages [30] -->
, it means that when the number of operation is odd,

<!-- b001669 | prose | pages [30] -->
Where,  2 

<!-- b001670 | prose | pages [30] -->
, or conversely, 1 the tap is open and  0 . So we can unify the temperature of

<!-- b001671 | prose | pages [30] -->
the hot water injection and natural cooling process in the following form:

<!-- b001672 | prose | pages [30] -->
   dQ dQ dQ dQ exchange evaporation       dQ dQ dQ

<!-- b001673 | furniture | pages [30] -->


<!-- b001674 | prose | pages [30] -->
  body radiation water water

<!-- b001675 | prose | pages [30] -->
To sum up, the optimal control model of strategy II is as follows:

<!-- b001676 | prose | pages [30] -->
n

<!-- b001677 | prose | pages [30] -->
 

<!-- b001678 | prose | pages [30] -->


<!-- b001679 | prose | pages [30] -->
t

<!-- b001680 | prose | pages [30] -->


<!-- b001681 | prose | pages [30] -->


<!-- b001682 | prose | pages [30] -->
n

<!-- b001683 | prose | pages [30] -->


<!-- b001684 | prose | pages [30] -->
i

<!-- b001685 | prose | pages [30] -->
1

<!-- b001686 | prose | pages [30] -->
T T t dt

<!-- b001687 | prose | pages [30] -->
( )

<!-- b001688 | prose | pages [30] -->


<!-- b001689 | prose | pages [30] -->
 

<!-- b001690 | prose | pages [30] -->
0

<!-- b001691 | prose | pages [30] -->


<!-- b001692 | prose | pages [30] -->
2

<!-- b001693 | prose | pages [30] -->
t

<!-- b001694 | prose | pages [30] -->


<!-- b001695 | prose | pages [30] -->
 

<!-- b001696 | prose | pages [30] -->
i

<!-- b001697 | prose | pages [30] -->


<!-- b001698 | prose | pages [30] -->


<!-- b001699 | prose | pages [30] -->


<!-- b001700 | prose | pages [30] -->


<!-- b001701 | prose | pages [30] -->


<!-- b001702 | prose | pages [30] -->
i

<!-- b001703 | prose | pages [30] -->
1

<!-- b001704 | prose | pages [30] -->
min

<!-- b001705 | prose | pages [30] -->
2 2

<!-- b001706 | prose | pages [30] -->
n

<!-- b001707 | prose | pages [30] -->


<!-- b001708 | prose | pages [30] -->
k

<!-- b001709 | prose | pages [30] -->
t

<!-- b001710 | prose | pages [30] -->
i

<!-- b001711 | prose | pages [30] -->


<!-- b001712 | prose | pages [30] -->
i

<!-- b001713 | prose | pages [30] -->
1

<!-- b001714 | prose | pages [30] -->
   

<!-- b001715 | prose | pages [30] -->


<!-- b001716 | prose | pages [30] -->
T T T T T

<!-- b001717 | prose | pages [30] -->
body

<!-- b001718 | prose | pages [30] -->
min1 min2

<!-- b001719 | prose | pages [30] -->
b highest

<!-- b001720 | prose | pages [30] -->


<!-- b001721 | prose | pages [30] -->
Q

<!-- b001722 | prose | pages [30] -->


<!-- b001723 | prose | pages [30] -->


<!-- b001724 | prose | pages [30] -->
T t

<!-- b001725 | prose | pages [30] -->
( )

<!-- b001726 | prose | pages [30] -->


<!-- b001727 | prose | pages [30] -->


<!-- b001728 | prose | pages [30] -->
c V

<!-- b001729 | prose | pages [30] -->
0

<!-- b001730 | prose | pages [30] -->
s t

<!-- b001731 | prose | pages [30] -->
. .

<!-- b001732 | prose | pages [30] -->


<!-- b001733 | prose | pages [30] -->
   

<!-- b001734 | prose | pages [30] -->
1

<!-- b001735 | prose | pages [30] -->
k

<!-- b001736 | prose | pages [30] -->
2

<!-- b001737 | prose | pages [30] -->
q

<!-- b001738 | prose | pages [30] -->
1

<!-- b001739 | prose | pages [30] -->


<!-- b001740 | prose | pages [30] -->


<!-- b001741 | prose | pages [30] -->


<!-- b001742 | prose | pages [30] -->


<!-- b001743 | prose | pages [30] -->


<!-- b001744 | prose | pages [30] -->
0

<!-- b001745 | prose | pages [30] -->
k

<!-- b001746 | prose | pages [30] -->
2

<!-- b001747 | prose | pages [30] -->
q

<!-- b001748 | prose | pages [30] -->


<!-- b001749 | prose | pages [30] -->


<!-- b001750 | prose | pages [30] -->
  

<!-- b001751 | prose | pages [30] -->
dQ dQ dQ dQ

<!-- b001752 | prose | pages [30] -->


<!-- b001753 | prose | pages [30] -->
exchange evaporation

<!-- b001754 | prose | pages [30] -->
1 1

<!-- b001755 | prose | pages [30] -->
 

<!-- b001756 | prose | pages [30] -->
2

<!-- b001757 | prose | pages [30] -->


<!-- b001758 | prose | pages [30] -->
T

<!-- b001759 | prose | pages [30] -->
312

<!-- b001760 | prose | pages [30] -->
1

<!-- b001761 | prose | pages [30] -->
B

<!-- b001762 | prose | pages [30] -->


<!-- b001763 | prose | pages [30] -->
 

<!-- b001764 | prose | pages [30] -->
  

<!-- b001765 | prose | pages [30] -->


<!-- b001766 | prose | pages [30] -->
 

<!-- b001767 | prose | pages [30] -->
t t e

<!-- b001768 | prose | pages [30] -->
9

<!-- b001769 | prose | pages [30] -->


<!-- b001770 | prose | pages [30] -->
2

<!-- b001771 | prose | pages [30] -->
k

<!-- b001772 | prose | pages [30] -->
2

<!-- b001773 | prose | pages [30] -->
k

<!-- b001774 | prose | pages [30] -->
1 3

<!-- b001775 | prose | pages [30] -->


<!-- b001776 | prose | pages [30] -->
3 2

<!-- b001777 | prose | pages [30] -->
 

<!-- b001778 | prose | pages [30] -->
1 1

<!-- b001779 | furniture | pages [30] -->


<!-- b001780 | prose | pages [30] -->
 

<!-- b001781 | prose | pages [30] -->
 

<!-- b001782 | prose | pages [30] -->


<!-- b001783 | prose | pages [30] -->


<!-- b001784 | prose | pages [30] -->
dQ d

<!-- b001785 | prose | pages [30] -->
Q dQ  

<!-- b001786 | prose | pages [30] -->
body radiation

<!-- b001787 | prose | pages [30] -->
water water

<!-- b001788 | heading | pages [30] -->
4.4.3 Solution of the optimal control models of strategy I & II

<!-- b001789 | prose | pages [30] -->
In this section, we solve the optimal control models of strategy I & II by Matlab. I. Algorithm flow

<!-- b001790 | prose | pages [30] -->
For optimal control model, we adopt enumeration method to solve its optimal solution, and transform all partial differential equations and differential equations [3]which are nested inside model to difference equations and solve them.

<!-- b001791 | prose | pages [30] -->
Algorithm flow charts of strategy 1 and strategy 2 are as follow:

<!-- b001792 | furniture | pages [30] -->


<!-- b001793 | furniture | pages [31] -->
Team #46830

<!-- b001794 | furniture | pages [31] -->


<!-- b001795 | prose | pages [31] -->
Strategy1

<!-- b001796 | prose | pages [31] -->
Initialize variables

<!-- b001797 | prose | pages [31] -->
N

<!-- b001798 | prose | pages [31] -->
While sum<1800

<!-- b001799 | prose | pages [31] -->
(30 minutes)

<!-- b001800 | prose | pages [31] -->
Y

<!-- b001801 | prose | pages [31] -->
Dispersed the

<!-- b001802 | prose | pages [31] -->
Output the average

<!-- b001803 | prose | pages [31] -->
interval within the

<!-- b001804 | prose | pages [31] -->
temperature(the water in

<!-- b001805 | prose | pages [31] -->
range of 0 to 1800

<!-- b001806 | prose | pages [31] -->
the bathtub)-time relationship curve

<!-- b001807 | prose | pages [31] -->
Solve temperature increment

<!-- b001808 | prose | pages [31] -->
(negative)beta_k

<!-- b001809 | prose | pages [31] -->
Tnext=Tk+beta_k

<!-- b001810 | prose | pages [31] -->
sum=sum+beta_t

<!-- b001811 | furniture | pages [31] -->


<!-- b001812 | furniture | pages [31] -->
Page 28 of 45

<!-- b001813 | prose | pages [31] -->
Strategy2

<!-- b001814 | prose | pages [31] -->
Initialize variables

<!-- b001815 | prose | pages [31] -->
N

<!-- b001816 | prose | pages [31] -->
While Tb<the highest

<!-- b001817 | prose | pages [31] -->
water temperature

<!-- b001818 | prose | pages [31] -->
Y Output The

<!-- b001819 | prose | pages [31] -->
Tb+beta_k

<!-- b001820 | prose | pages [31] -->
optimal result

<!-- b001821 | prose | pages [31] -->
Solve Ts; Tmin1,Tmin2

<!-- b001822 | prose | pages [31] -->
initialization

<!-- b001823 | prose | pages [31] -->
N

<!-- b001824 | prose | pages [31] -->
While Tmin1<Ts

<!-- b001825 | prose | pages [31] -->
Y

<!-- b001826 | prose | pages [31] -->
Tmin1+beta_k

<!-- b001827 | prose | pages [31] -->
N

<!-- b001828 | prose | pages [31] -->
While Tmin2<Ts

<!-- b001829 | prose | pages [31] -->
Y

<!-- b001830 | prose | pages [31] -->
Tmin2+beta_k

<!-- b001831 | prose | pages [31] -->
Finding the optimal temperature of adding

<!-- b001832 | prose | pages [31] -->
water/draining

<!-- b001833 | furniture | pages [31] -->


<!-- b001834 | caption | pages [31] -->
Figure 10: Algorithm flow charts

<!-- b001835 | prose | pages [31] -->
II. Result of optimal control model of strategy 1 We get optimal parameter under the strategy 1 through programming the above

<!-- b001836 | prose | pages [31] -->
program in MATLAB software:

<!-- b001837 | prose | pages [31] -->
   

<!-- b001838 | prose | pages [31] -->
1 0.007

<!-- b001839 | prose | pages [31] -->
k

<!-- b001840 | prose | pages [31] -->


<!-- b001841 | prose | pages [31] -->
b

<!-- b001842 | prose | pages [31] -->


<!-- b001843 | prose | pages [31] -->
L s

<!-- b001844 | furniture | pages [31] -->


<!-- b001845 | prose | pages [31] -->
311.1

<!-- b001846 | prose | pages [31] -->
T

<!-- b001847 | prose | pages [31] -->


<!-- b001848 | prose | pages [31] -->
b

<!-- b001849 | prose | pages [31] -->
K

<!-- b001850 | prose | pages [31] -->
We also get the change curve of water average temperature T t during user bathing ( )

<!-- b001851 | prose | pages [31] -->
when in optimal parameter, as shown in the graph.

<!-- b001852 | furniture | pages [31] -->


<!-- b001853 | furniture | pages [32] -->
Team #46830

<!-- b001854 | furniture | pages [32] -->


<!-- b001855 | furniture | pages [32] -->


<!-- b001856 | furniture | pages [32] -->
Page 29 of 45

<!-- b001857 | furniture | pages [32] -->


<!-- b001858 | caption | pages [32] -->
Figure 11: The change curve of water average temperature

<!-- b001859 | prose | pages [32] -->
In the graph, the red curve is the temperature curve of normal hot water under

<!-- b001860 | prose | pages [32] -->
condition of optimal strategy, the blue curve is the natural cooling curve of normal water. We can find directly the cooling speed under optimal parameter is lower than

<!-- b001861 | prose | pages [32] -->
natural cooling curve. Then we explain quantitatively the validity of our model

<!-- b001862 | prose | pages [32] -->
through several data.

<!-- b001863 | caption | pages [32] -->
Table 3: Average temperature data

<!-- b001864 | prose | pages [32] -->
T       t 300 600 900 1200 1500 1800

<!-- b001865 | prose | pages [32] -->
3143814 316.0650 315.1926 T optimize( ) t 313.6271 312.9256 312.2413

<!-- b001866 | prose | pages [32] -->
313.9801 315.9266 314.9203 t T ( ) nature 313.1016 312.2809 311.5501

<!-- b001867 | prose | pages [32] -->
Through the calculation we can get extra water requirement in strategy is

<!-- b001868 | prose | pages [32] -->
    1 0.007 L s 1800 s 12.6 L , the ratio between extra water requirement and bathing

<!-- b001869 | prose | pages [32] -->
water requirement is:

<!-- b001870 | prose | pages [32] -->
12.6 12.6 L   100%  

<!-- b001871 | furniture | pages [32] -->


<!-- b001872 | prose | pages [32] -->
100% 2.84% 443.4 V

<!-- b001873 | prose | pages [32] -->
0

<!-- b001874 | prose | pages [32] -->
After applying optimal strategy I, the temperature decrease to 4.76℃from5.45℃,

<!-- b001875 | prose | pages [32] -->


<!-- b001876 | prose | pages [32] -->
5.45 4.76

<!-- b001877 | prose | pages [32] -->


<!-- b001878 | prose | pages [32] -->
5.45

<!-- b001879 | prose | pages [32] -->


<!-- b001880 | prose | pages [32] -->
100% 12.66%

<!-- b001881 | furniture | pages [32] -->


<!-- b001882 | prose | pages [32] -->
As for comfort level aspect, the most comfortable water temperature satisfaction

<!-- b001883 | prose | pages [32] -->
rate is

<!-- b001884 | prose | pages [32] -->
：

<!-- b001885 | prose | pages [32] -->
 

<!-- b001886 | prose | pages [32] -->


<!-- b001887 | prose | pages [32] -->


<!-- b001888 | prose | pages [32] -->
 311.1 312 311.1

<!-- b001889 | prose | pages [32] -->
  

<!-- b001890 | prose | pages [32] -->
100% e 9

<!-- b001891 | prose | pages [32] -->
 

<!-- b001892 | prose | pages [32] -->


<!-- b001893 | prose | pages [32] -->
312

<!-- b001894 | furniture | pages [32] -->


<!-- b001895 | prose | pages [32] -->
    2 2

<!-- b001896 | prose | pages [32] -->


<!-- b001897 | prose | pages [32] -->
312 312

<!-- b001898 | prose | pages [32] -->
  

<!-- b001899 | prose | pages [32] -->
100% 91.39% 9

<!-- b001900 | furniture | pages [32] -->


<!-- b001901 | furniture | pages [33] -->
Team #46830

<!-- b001902 | furniture | pages [33] -->


<!-- b001903 | furniture | pages [33] -->


<!-- b001904 | furniture | pages [33] -->
Page 30 of 45

<!-- b001905 | prose | pages [33] -->
To sum up, based on our optimal control model for water injection, we merely

<!-- b001906 | prose | pages [33] -->
need 2.84% extra hot water to get a 12.66% optimization effect in temperature variation and 91.39% of the most comfortable water temperature satisfaction rate.

<!-- b001907 | prose | pages [33] -->
These results shows that our model and strategy are of great effectiveness and

<!-- b001908 | prose | pages [33] -->
practical reference value.

<!-- b001909 | prose | pages [33] -->
In addition, according to the forced convection model and the distribution model

<!-- b001910 | prose | pages [33] -->
of temperature in space, we can get the data of the water temperature in time and space at any moment when bathing. According to assumption 12 combined with

<!-- b001911 | prose | pages [33] -->
Eq.4.1.3-2 &4.2.2-2 and the definition of f F ,we get the distribution of water ( )

<!-- b001912 | prose | pages [33] -->
temperature in the tub at any moment when bathing:

<!-- b001913 | prose | pages [33] -->


<!-- b001914 | prose | pages [33] -->
T x y z t

<!-- b001915 | prose | pages [33] -->
( , , , )

<!-- b001916 | prose | pages [33] -->
T t

<!-- b001917 | prose | pages [33] -->
2

<!-- b001918 | prose | pages [33] -->
 

<!-- b001919 | prose | pages [33] -->
F

<!-- b001920 | prose | pages [33] -->
 

<!-- b001921 | prose | pages [33] -->
 

<!-- b001922 | prose | pages [33] -->
f t

<!-- b001923 | prose | pages [33] -->
1

<!-- b001924 | prose | pages [33] -->
 

<!-- b001925 | prose | pages [33] -->


<!-- b001926 | prose | pages [33] -->
0

<!-- b001927 | prose | pages [33] -->
F

<!-- b001928 | prose | pages [33] -->
   (15)

<!-- b001929 | prose | pages [33] -->
( )

<!-- b001930 | prose | pages [33] -->
e K

<!-- b001931 | prose | pages [33] -->
0

<!-- b001932 | prose | pages [33] -->
y

<!-- b001933 | prose | pages [33] -->
b

<!-- b001934 | prose | pages [33] -->
 Here, we assume human action frequency

<!-- b001935 | furniture | pages [33] -->


<!-- b001936 | prose | pages [33] -->
f 1 Hz 0

<!-- b001937 | prose | pages [33] -->
Human motion range is 0.5m,the volume of the moving parts is 1/10 of the volume of the body, which is 6L. Thus we get the forced convection of human motion

<!-- b001938 | prose | pages [33] -->
  F 0.5 m 6 10

<!-- b001939 | prose | pages [33] -->
 4

<!-- b001940 | prose | pages [33] -->
    3 3 3 3 4

<!-- b001941 | furniture | pages [33] -->


<!-- b001942 | prose | pages [33] -->
m 3 10 m

<!-- b001943 | prose | pages [33] -->
, which is mentioned at the end of 4.2.2 bF 0.191378 m

<!-- b001944 | prose | pages [33] -->
 is the temperature gradient at the beginning of the hot water injection. We K 0

<!-- b001945 | prose | pages [33] -->
might as well set it the value of 2.5s, then  

<!-- b001946 | furniture | pages [33] -->


<!-- b001947 | prose | pages [33] -->
K 0 4.294

<!-- b001948 | prose | pages [33] -->
Take these data into formula (15) , we have:

<!-- b001949 | prose | pages [33] -->
 

<!-- b001950 | prose | pages [33] -->
T x y z t ( , , , ) T t ( )

<!-- b001951 | prose | pages [33] -->
Where, T t is determined Fig11. ( )

<!-- b001952 | prose | pages [33] -->
 

<!-- b001953 | prose | pages [33] -->


<!-- b001954 | prose | pages [33] -->
4

<!-- b001955 | prose | pages [33] -->
  

<!-- b001956 | prose | pages [33] -->
2.45731 10 t 1 4.294 e y

<!-- b001957 | furniture | pages [33] -->


<!-- b001958 | prose | pages [33] -->
III. Result of optimal control model of strategy II

<!-- b001959 | prose | pages [33] -->
We get optimal parameter under the strategy II through programming the above program in MATLAB software:

<!-- b001960 | prose | pages [33] -->
 

<!-- b001961 | prose | pages [33] -->
T

<!-- b001962 | prose | pages [33] -->
min1

<!-- b001963 | prose | pages [33] -->
 

<!-- b001964 | prose | pages [33] -->
T

<!-- b001965 | prose | pages [33] -->


<!-- b001966 | prose | pages [33] -->
min2

<!-- b001967 | prose | pages [33] -->
 

<!-- b001968 | prose | pages [33] -->
311.7

<!-- b001969 | prose | pages [33] -->
K

<!-- b001970 | prose | pages [33] -->
311.7

<!-- b001971 | prose | pages [33] -->
K

<!-- b001972 | furniture | pages [33] -->


<!-- b001973 | prose | pages [33] -->
313.1

<!-- b001974 | prose | pages [33] -->
T

<!-- b001975 | prose | pages [33] -->


<!-- b001976 | prose | pages [33] -->
b

<!-- b001977 | prose | pages [33] -->
T Amazingly, we get the result min1

<!-- b001978 | prose | pages [33] -->
following aspects:

<!-- b001979 | prose | pages [33] -->
K

<!-- b001980 | prose | pages [33] -->
 T . Then we discuss deeply in the min2

<!-- b001981 | prose | pages [33] -->
1. In this strategy, the upper and lower two critical temperatures are equal. In strategy 2, the best solution is that the time of turning the tap on and off is infinitely

<!-- b001982 | furniture | pages [33] -->


<!-- b001983 | furniture | pages [34] -->
Team #46830

<!-- b001984 | furniture | pages [34] -->


<!-- b001985 | furniture | pages [34] -->
Page 31 of 45

<!-- b001986 | furniture | pages [34] -->


<!-- b001987 | prose | pages [34] -->
small. Thus degenerate to a continuous process in macroscopic.

<!-- b001988 | prose | pages [34] -->
 T T 1. In this strategy, means that every discrete process is infinitely min1 min2

<!-- b001989 | prose | pages [34] -->
small, every interval between the tap opening and closing is infinitely small, so it degenerates to a continuous process.

<!-- b001990 | prose | pages [34] -->
2. Because we use the difference equation to replace the differential equation, the

<!-- b001991 | prose | pages [34] -->
accuracy of the differential equation is not enough, otherwise we can solve this approximation in the continuous process of opening and closing the tap of the time

<!-- b001992 | prose | pages [34] -->
ratio for further, and calculate the flow rate of the continuous addition of water.

<!-- b001993 | prose | pages [34] -->
Because the model is a three-dimensional optimization with huge calculation. If Cyclic step is shorter in the difference equation, the calculation will increase in

<!-- b001994 | prose | pages [34] -->
geometric progression. With the limitation of our computers, we can’t analyze more

<!-- b001995 | prose | pages [34] -->
deeply.

<!-- b001996 | prose | pages [34] -->
3. The optimal solution of strategy II is a continuous process of injection,

<!-- b001997 | prose | pages [34] -->
however, the results are totally different with those of strategy I. Here is our guess:

<!-- b001998 | prose | pages [34] -->
Although we set additional water consumption, temperature deviation, and comfort for the two strategies for the same weight, with different standardized ways of each

<!-- b001999 | prose | pages [34] -->
factor, the results vary a lot.

<!-- b002000 | heading | pages [34] -->
4.5 Bubble bath

<!-- b002001 | prose | pages [34] -->
In this section, we get the universal thermodynamic model of bubble [4] water by

<!-- b002002 | prose | pages [34] -->
modifying that of normal hot water , and get the effect of bubble water on optimal control strategy through the previous optimal control strategy.

<!-- b002003 | heading | pages [34] -->
4.5.1 The effect of bubble water

<!-- b002004 | prose | pages [34] -->
Bubble water has an impact on the thermodynamic process of the bathtub

<!-- b002005 | prose | pages [34] -->
system, mainly because the bubble water has some different physical parameters and it brings a layer of air bubbles on the surface of the water. This bubble will

<!-- b002006 | prose | pages [34] -->
reduce the evaporation rate of water and will reduce the heat exchange power of

<!-- b002007 | prose | pages [34] -->
water surface and air [11[]12].

<!-- b002008 | prose | pages [34] -->
As for the similarities and differences between bubble water and normal water i. Their density and specific heat capacity are slightly different. However the concentration of bubble water is low, so we can ignore this difference.

<!-- b002009 | prose | pages [34] -->
ii. The surface tension of bubble water can be 1.3-2.2 times of the tension of

<!-- b002010 | prose | pages [34] -->
distilled water due to its different concentration. As we all know, the large surface tension reduces the escape rate of the molecules on the surface.

<!-- b002011 | prose | pages [34] -->
iii. bubble water brings a layer of air bubbles on the surface of the water, which

<!-- b002012 | furniture | pages [34] -->


<!-- b002013 | furniture | pages [35] -->
Team #46830

<!-- b002014 | furniture | pages [35] -->


<!-- b002015 | furniture | pages [35] -->


<!-- b002016 | furniture | pages [35] -->
Page 32 of 45

<!-- b002017 | prose | pages [35] -->
is equivalent to add a thick layer of air insulation to the water in the bath and

<!-- b002018 | prose | pages [35] -->
effectively prevent the evaporation of water at the same time.

<!-- b002019 | prose | pages [35] -->
dQ should be deleted from the heat differential equation of In a word, evaporation

<!-- b002020 | prose | pages [35] -->
bubble water, because the bubble layer and its large surface tension coefficient can

<!-- b002021 | prose | pages [35] -->
dQ reduce the evaporation capacity in the tub greatly,

<!-- b002022 | prose | pages [35] -->
dQ

<!-- b002023 | prose | pages [35] -->
is inevitable to decline. evaporation

<!-- b002024 | prose | pages [35] -->
part of the heat conduction with the air will also be Additionally, in the exchange

<!-- b002025 | prose | pages [35] -->
modified. Because the water doesn’t contact with air directly. Instead, the heat exchanges with the outside air through the bubble layer.

<!-- b002026 | prose | pages [35] -->
Considering these factors and formula (4) and formula (13), the expression after modifying the heat transfer between water and air is as follows:

<!-- b002027 | prose | pages [35] -->


<!-- b002028 | prose | pages [35] -->


<!-- b002029 | prose | pages [35] -->
     

<!-- b002030 | prose | pages [35] -->
dQ h T t

<!-- b002031 | prose | pages [35] -->
( )

<!-- b002032 | prose | pages [35] -->
T ab

<!-- b002033 | prose | pages [35] -->
2

<!-- b002034 | prose | pages [35] -->
  

<!-- b002035 | prose | pages [35] -->
exchange 0

<!-- b002036 | prose | pages [35] -->
  

<!-- b002037 | prose | pages [35] -->


<!-- b002038 | prose | pages [35] -->
    

<!-- b002039 | prose | pages [35] -->
aH

<!-- b002040 | prose | pages [35] -->
2

<!-- b002041 | prose | pages [35] -->
bH T t

<!-- b002042 | prose | pages [35] -->
( )

<!-- b002043 | prose | pages [35] -->
T ab dt

<!-- b002044 | furniture | pages [35] -->


<!-- b002045 | prose | pages [35] -->
  

<!-- b002046 | prose | pages [35] -->
0

<!-- b002047 | prose | pages [35] -->
d

<!-- b002048 | prose | pages [35] -->


<!-- b002049 | prose | pages [35] -->
air

<!-- b002050 | prose | pages [35] -->
Add the two amendments to the differential equation of heat. We have:

<!-- b002051 | prose | pages [35] -->
    dQ dQ dQ exchange body  

<!-- b002052 | furniture | pages [35] -->


<!-- b002053 | prose | pages [35] -->
dQ dQ dQ   radiation water water

<!-- b002054 | prose | pages [35] -->
After taking the expression above into formula (13), we get the universal

<!-- b002055 | prose | pages [35] -->
thermodynamic model of bubble water.

<!-- b002056 | prose | pages [35] -->
Here we don’t solve the model. Instead, we contrast the natural heat dissipation power of the bubble water in the body's most comfortable temperature with the

<!-- b002057 | prose | pages [35] -->
natural heat dissipation power of the normal hot water in this case, assuming the

<!-- b002058 | prose | pages [35] -->
thickness of the bubble layer as 3cm.

<!-- b002059 | prose | pages [35] -->
  

<!-- b002060 | prose | pages [35] -->
dQ dQ dQ

<!-- b002061 | prose | pages [35] -->
exchange body

<!-- b002062 | prose | pages [35] -->
 

<!-- b002063 | prose | pages [35] -->
W

<!-- b002064 | prose | pages [35] -->
water

<!-- b002065 | prose | pages [35] -->
dt

<!-- b002066 | prose | pages [35] -->
  

<!-- b002067 | prose | pages [35] -->
dQ dQ dQ

<!-- b002068 | prose | pages [35] -->
exchange

<!-- b002069 | prose | pages [35] -->
 

<!-- b002070 | prose | pages [35] -->
W

<!-- b002071 | prose | pages [35] -->
bubble

<!-- b002072 | prose | pages [35] -->
dt

<!-- b002073 | prose | pages [35] -->
  

<!-- b002074 | prose | pages [35] -->
dQ dQ

<!-- b002075 | prose | pages [35] -->
radiation evaporation

<!-- b002076 | prose | pages [35] -->


<!-- b002077 | prose | pages [35] -->
6710.88

<!-- b002078 | prose | pages [35] -->
W

<!-- b002079 | furniture | pages [35] -->


<!-- b002080 | prose | pages [35] -->
dt

<!-- b002081 | prose | pages [35] -->


<!-- b002082 | prose | pages [35] -->
dQ

<!-- b002083 | prose | pages [35] -->
body radiation

<!-- b002084 | prose | pages [35] -->


<!-- b002085 | prose | pages [35] -->
3076.92

<!-- b002086 | prose | pages [35] -->
W

<!-- b002087 | furniture | pages [35] -->


<!-- b002088 | prose | pages [35] -->
dt dt

<!-- b002089 | prose | pages [35] -->
Then we draw the conclusion that the heat dissipating power of bubble water in the tub is 45.85% of the original power, which shows that bubble water has good

<!-- b002090 | prose | pages [35] -->
thermal insulation property. The improvement is because the air bubble layer separates the direct convective heat exchange between the air and the water surface.

<!-- b002091 | prose | pages [35] -->
Heat transfer becomes based on Fourier’s law only.

<!-- b002092 | heading | pages [35] -->
4.5.2 Effect of bubble water on optimal control strategy

<!-- b002093 | prose | pages [35] -->
We take the universal thermodynamic model into optimal control strategy and solve it by Matlab:

<!-- b002094 | furniture | pages [35] -->


<!-- b002095 | furniture | pages [36] -->
Team #46830

<!-- b002096 | furniture | pages [36] -->


<!-- b002097 | prose | pages [36] -->
 

<!-- b002098 | furniture | pages [36] -->


<!-- b002099 | furniture | pages [36] -->
Page 33 of 45

<!-- b002100 | prose | pages [36] -->
 

<!-- b002101 | prose | pages [36] -->
1 0.004

<!-- b002102 | prose | pages [36] -->
k

<!-- b002103 | prose | pages [36] -->


<!-- b002104 | prose | pages [36] -->
b

<!-- b002105 | prose | pages [36] -->


<!-- b002106 | prose | pages [36] -->
L s

<!-- b002107 | furniture | pages [36] -->


<!-- b002108 | prose | pages [36] -->
311.9

<!-- b002109 | prose | pages [36] -->
T

<!-- b002110 | prose | pages [36] -->


<!-- b002111 | prose | pages [36] -->
b

<!-- b002112 | prose | pages [36] -->
K

<!-- b002113 | prose | pages [36] -->
As is shown in Figure 12, the green curve is the curve of the temperature change over time under the conditions of the optimal strategy I, the red curve is the

<!-- b002114 | prose | pages [36] -->
temperature curve of normal hot water under the condition of the optimal strategy I,

<!-- b002115 | prose | pages [36] -->
the blue curve is the natural heat dissipating curve of normal water. The figure tells us that bubble water has the excellent performance in thermal insulation, if combined

<!-- b002116 | prose | pages [36] -->
with the optimal control strategy, it can effectively keep the water warm in the

<!-- b002117 | prose | pages [36] -->
bathtub.

<!-- b002118 | furniture | pages [36] -->


<!-- b002119 | caption | pages [36] -->
Figure 12: Curves of temperature

<!-- b002120 | prose | pages [36] -->
If we replace normal water with bubble water in the tub, the optimal solution of

<!-- b002121 | prose | pages [36] -->
    1 0.004 L s 1800 s 7.2 L which is 57.14% of the normal water.

<!-- b002122 | prose | pages [36] -->
our model is

<!-- b002123 | prose | pages [36] -->
In addition, 311.9K brings users a higher comfort level. Temperature change in bath

<!-- b002124 | prose | pages [36] -->
tub declines from approximately 5.54℃ to no more than 2.91℃, the optimization rate

<!-- b002125 | prose | pages [36] -->
reaches 47.47%.

<!-- b002126 | prose | pages [36] -->
To sum up, water bubble bath combined with a scientific way of injection can

<!-- b002127 | prose | pages [36] -->
very effectively keep the water warm. The result is of practical reference value and

<!-- b002128 | prose | pages [36] -->
provide a good theoretical model for the industry of hot spring, indoor swimming pool and so on.

<!-- b002129 | furniture | pages [36] -->


<!-- b002130 | furniture | pages [37] -->
Team #46830

<!-- b002131 | furniture | pages [37] -->


<!-- b002132 | furniture | pages [37] -->
Page 34 of 45

<!-- b002133 | furniture | pages [37] -->


<!-- b002134 | heading | pages [37] -->
5    Testing the Model

<!-- b002135 | heading | pages [37] -->
5.1 Error Analysis

<!-- b002136 | prose | pages [37] -->
In this part, we will analyze the factors that may cause the error of the solution. Many factors will influence the bath water temperature, including the outside

<!-- b002137 | prose | pages [37] -->
environment factors(such as air temperature and humidity, air flow rate), the water itself (such as waves, drop, natural heat convection), human (do work, metabolic heat

<!-- b002138 | prose | pages [37] -->
production). In addition to the influencing factors, the approximation and fitting used

<!-- b002139 | prose | pages [37] -->
in the model building process, as well as the algorithm in the solving process. It will also bring errors.

<!-- b002140 | heading | pages [37] -->
5.1.1 Various factors of external environment

<!-- b002141 | prose | pages [37] -->
I. Air temperature and humidity

<!-- b002142 | prose | pages [37] -->
In fact, in such a relatively closed bathroom, air humidity will rise with the evaporation of the water in the bathtub. The heat caused by the evaporation of water

<!-- b002143 | prose | pages [37] -->
vapor increases the temperature of the air. But the temperature and humidity of the air in the bathroom is not uniform, and the influence of water on the air is difficult to be

<!-- b002144 | prose | pages [37] -->
given by simple ordinary differential equations, which makes the error difficult to get

<!-- b002145 | prose | pages [37] -->
the numerical value.

<!-- b002146 | prose | pages [37] -->
But after analysis, we know that the rise of air humidity inhibits the evaporation

<!-- b002147 | prose | pages [37] -->
rate of water vapor, at the same time, the air temperature rise will reduce the

<!-- b002148 | prose | pages [37] -->
difference in temperature between air and water, and then inhibits water heat exchange of air. In assumption 1 we ignore the change of air temperature and

<!-- b002149 | prose | pages [37] -->
humidity. So without considering other cases, according to the results of the model,

<!-- b002150 | prose | pages [37] -->
water cooling slightly faster than the actual, it means that the error of a value is above zero.

<!-- b002151 | prose | pages [37] -->
II. Air flow

<!-- b002152 | prose | pages [37] -->
Compared with the change of air temperature and humidity, air flow's influence on the water temperature should be much smaller. Because the bathroom is relatively

<!-- b002153 | prose | pages [37] -->
closed, in addition to the exhaust fan, there are no air source and sink. Since there is no air source and sink, the air flow in the bathroom is very small.

<!-- b002154 | prose | pages [37] -->
But as a part of the error, we need to analyze the air flow. Refer to the above

<!-- b002155 | prose | pages [37] -->
discussion of the temperature and humidity, we know that the air flow inhibits water cooling. So without considering other cases, according to the results of the model, water

<!-- b002156 | prose | pages [37] -->
cooling slightly faster than the actual, it means that the error of a value is above zero.

<!-- b002157 | furniture | pages [37] -->


<!-- b002158 | furniture | pages [38] -->
Team #46830

<!-- b002159 | furniture | pages [38] -->


<!-- b002160 | furniture | pages [38] -->
Page 35 of 45

<!-- b002161 | furniture | pages [38] -->


<!-- b002162 | heading | pages [38] -->
5.1.2 Various factors of water

<!-- b002163 | prose | pages [38] -->
I. Waves

<!-- b002164 | prose | pages [38] -->
As a result of the movement of water injection or motions of human, the water must

<!-- b002165 | prose | pages [38] -->
generate waves. Waves will increase the surface contact area of water and air, thus cooling

<!-- b002166 | prose | pages [38] -->
speed up. On the other hand, waves will lead to the overflow under full water condition, and

<!-- b002167 | prose | pages [38] -->
take away the heat. In fact the overflow is a very considerable value, it take away heat is

<!-- b002168 | prose | pages [38] -->
relatively large, and the heat it takes away is also quite large. But according to assumption 2, we

<!-- b002169 | prose | pages [38] -->
ignore the impact. So without considering other cases, according to the results of the model,

<!-- b002170 | prose | pages [38] -->
water cooling slightly slower than the actual, it means that the error of a value is less than zero.

<!-- b002171 | prose | pages [38] -->
II. Water drop process

<!-- b002172 | prose | pages [38] -->
Loss of heat will occurred in the dropping process of water. When it reaches the surface of

<!-- b002173 | prose | pages [38] -->
the water, the temperature will be slightly lower than the outlet water temperature. That means

<!-- b002174 | prose | pages [38] -->
0T  is slightly larger than the actual value, the error of a value is above zero. the value of

<!-- b002175 | prose | pages [38] -->
III. Natural heat convection

<!-- b002176 | prose | pages [38] -->
Natural heat convection is generated by the temperature gradient, and the result is necessarily reduce the absolute value of the temperature gradient. That means the

<!-- b002177 | prose | pages [38] -->
 K t is slightly larger than the actual value, the error of a value is above value of

<!-- b002178 | prose | pages [38] -->
zero.

<!-- b002179 | heading | pages [38] -->
5.1.3 Various factors of human

<!-- b002180 | prose | pages [38] -->
I. Human work to water

<!-- b002181 | prose | pages [38] -->
Human work to water, part of this energy change into the kinetic energy of the water flow,

<!-- b002182 | prose | pages [38] -->
another part change into heat in the form of viscous resistance. This factor is actually a small

<!-- b002183 | prose | pages [38] -->
heat source. That means the heat dissipation of water is slightly slower than the actual value,

<!-- b002184 | prose | pages [38] -->
the error of a value is less than zero.

<!-- b002185 | prose | pages [38] -->
II. Metabolic heat production

<!-- b002186 | prose | pages [38] -->
When the water temperature is lower than the body temperature, the body can be regarded

<!-- b002187 | prose | pages [38] -->
as an independent heat source. So according to the results of the model, water cooling slightly

<!-- b002188 | prose | pages [38] -->
slower than the actual, it means that the error of a value is less than zero.

<!-- b002189 | heading | pages [38] -->
5.1.4 Error in modeling and solving process

<!-- b002190 | prose | pages [38] -->
I. Error of plane fitting to temperature distribution surface

<!-- b002191 | prose | pages [38] -->
Because the analytic form of the curved surface is unknown, we can’t evaluate the error

<!-- b002192 | furniture | pages [38] -->


<!-- b002193 | furniture | pages [39] -->
Team #46830

<!-- b002194 | furniture | pages [39] -->


<!-- b002195 | prose | pages [39] -->


<!-- b002196 | furniture | pages [39] -->


<!-- b002197 | furniture | pages [39] -->
Page 36 of 45

<!-- b002198 | prose | pages [39] -->
T t . But we can get the average value of some points on the surface, caused by this fitting to

<!-- b002199 | prose | pages [39] -->
then get the error by compared the average value with 

<!-- b002200 | furniture | pages [39] -->


<!-- b002201 | prose | pages [39] -->
II. Error of the step size of the algorithm

<!-- b002202 | prose | pages [39] -->
T t .

<!-- b002203 | prose | pages [39] -->
We use enumeration method to solve the optimization model. In strategy one, the step size

<!-- b002204 | prose | pages [39] -->
bT  is 0.1. In the optimal strategy we get, the error of bk is 0.001, the step size of of bk

<!-- b002205 | prose | pages [39] -->
bT should be half of the step size, as shown in the following formula and

<!-- b002206 | prose | pages [39] -->


<!-- b002207 | prose | pages [39] -->
 

<!-- b002208 | prose | pages [39] -->
k

<!-- b002209 | prose | pages [39] -->
0.0070

<!-- b002210 | prose | pages [39] -->


<!-- b002211 | prose | pages [39] -->
b

<!-- b002212 | prose | pages [39] -->


<!-- b002213 | prose | pages [39] -->
T

<!-- b002214 | prose | pages [39] -->
311.10

<!-- b002215 | prose | pages [39] -->


<!-- b002216 | prose | pages [39] -->
b

<!-- b002217 | heading | pages [39] -->
5.2 Sensitivity Analysis

<!-- b002218 | prose | pages [39] -->


<!-- b002219 | prose | pages [39] -->
   

<!-- b002220 | prose | pages [39] -->
1 0.0005

<!-- b002221 | prose | pages [39] -->
L s

<!-- b002222 | furniture | pages [39] -->


<!-- b002223 | prose | pages [39] -->


<!-- b002224 | prose | pages [39] -->
 

<!-- b002225 | prose | pages [39] -->
0.05

<!-- b002226 | prose | pages [39] -->
K

<!-- b002227 | prose | pages [39] -->
Some inputs of our model may be hard to obtain or there may be some deviation in our

<!-- b002228 | prose | pages [39] -->
inputs. So it's possible that these kinds of situation will influence the solution of our model. To

<!-- b002229 | prose | pages [39] -->
understand the situations above, we implement a sensitivity analysis to test the robustness of

<!-- b002230 | prose | pages [39] -->
our model. The analysis results show that our model does not exhibit a chaotic behavior and

<!-- b002231 | prose | pages [39] -->
show good sensitivity.

<!-- b002232 | prose | pages [39] -->
Our sensitivity analysis will be based on factor variation method, in order to see how the

<!-- b002233 | prose | pages [39] -->
result of the model changes when the input parameters change. We will analyze the following

<!-- b002234 | prose | pages [39] -->
parameters:

<!-- b002235 | prose | pages [39] -->
1. The shape and volume of the tub

<!-- b002236 | prose | pages [39] -->
2. Human's volume, surface area, comfortable temperature and the motion in the tub, etc.

<!-- b002237 | prose | pages [39] -->
3. Heat transfer rate

<!-- b002238 | prose | pages [39] -->
We have obtained the optimal solution of the model. We will use this as a contrast to do

<!-- b002239 | prose | pages [39] -->
sensitivity analysis. The parameters of the optimal solution are set as follows:

<!-- b002240 | prose | pages [39] -->
 H 0.49 m 1. The height of the tub , length

<!-- b002241 | prose | pages [39] -->


<!-- b002242 | prose | pages [39] -->
  a b 1.3 m 0.8 m , width

<!-- b002243 | furniture | pages [39] -->


<!-- b002244 | prose | pages [39] -->
 2 W m h 42.8 2. The heat transfer rate of tub

<!-- b002245 | prose | pages [39] -->
2 S =1.9 m 3. Body surface area

<!-- b002246 | prose | pages [39] -->
 h 166 4. The heat transfer rate of water water

<!-- b002247 | prose | pages [39] -->
k

<!-- b002248 | furniture | pages [39] -->


<!-- b002249 | prose | pages [39] -->
 2 W m k

<!-- b002250 | furniture | pages [39] -->


<!-- b002251 | prose | pages [39] -->
 k 0.007 L s By these parameters, the solution is that，the rate of flow

<!-- b002252 | prose | pages [39] -->
 T 311.1 k

<!-- b002253 | prose | pages [39] -->
，the outlet water

<!-- b002254 | prose | pages [39] -->
,water consumption is 12.6 Liters(Assume that bath time is 30 temperature 0

<!-- b002255 | furniture | pages [39] -->


<!-- b002256 | furniture | pages [40] -->
Team #46830

<!-- b002257 | furniture | pages [40] -->


<!-- b002258 | furniture | pages [40] -->


<!-- b002259 | furniture | pages [40] -->
Page 37 of 45

<!-- b002260 | prose | pages [40] -->
minutes).It is the optimal bathing strategy with the least amount of water.

<!-- b002261 | heading | pages [40] -->
5.2.1 Sensitivity to the shape and volume of the tub

<!-- b002262 | prose | pages [40] -->
Change the shape and volume of the tub, observe the influence of the changes of each

<!-- b002263 | prose | pages [40] -->
factor on the optimal bathing strategy. The sensitivity of the shape and volume of the tub by

<!-- b002264 | prose | pages [40] -->
calculation is obtained, as shown in the following tables.

<!-- b002265 | furniture | pages [40] -->


<!-- b002266 | caption | pages [40] -->
Table 4: Sensitivity of the shape and volume of the tub (for water consumption)

<!-- b002267 | furniture | pages [40] -->


<!-- b002268 | prose | pages [40] -->
-5% -3% -1% a -85.71% -57.14% -42.86% b -57.14% -57.14% -42.86%

<!-- b002269 | prose | pages [40] -->
H -42.86% -28.57% -28.57% h -42.86% -42.86% -28.57%

<!-- b002270 | prose | pages [40] -->
0 1% 3% 5% 0% 0% 28.57% 57.14% 0% 0% 14.29% 28.57%

<!-- b002271 | prose | pages [40] -->
0% -14.29% 0% 0% 0% -14.29% 0% 0%

<!-- b002272 | furniture | pages [40] -->


<!-- b002273 | caption | pages [40] -->
Table 5: Sensitivity of the shape and volume of the tub (for water temperature)

<!-- b002274 | furniture | pages [40] -->


<!-- b002275 | prose | pages [40] -->
-5% -3% -1% a -0.03% -0.03% -0.03% b -0.03% -0.03% -0.03%

<!-- b002276 | prose | pages [40] -->
H -0.03% -0.03% -0.03% h -0.03% -0.03% -0.03%

<!-- b002277 | prose | pages [40] -->
0 1% 3% 5% 0% 0% 0% 0% 0% 0% 0% 0%

<!-- b002278 | prose | pages [40] -->
0% 0% 0% 0% 0% 0% 0% 0%

<!-- b002279 | prose | pages [40] -->
We can see that the water consumption is very sensitive to the parameters of the shape

<!-- b002280 | prose | pages [40] -->
 . It proves that the model we established is suitable and volume of the tub in the context of 5%

<!-- b002281 | prose | pages [40] -->
for various shapes and volumes of the tub.

<!-- b002282 | prose | pages [40] -->
On the other hand, the water temperature is not very sensitive to the parameters of the

<!-- b002283 | prose | pages [40] -->
shape and volume of the tub. But we can understand that the outlet temperature had great

<!-- b002284 | prose | pages [40] -->
 by analysis the data. That is to say, the temperature can not changes in the context of 1%

<!-- b002285 | prose | pages [40] -->
change too much，this shows that our model takes the person's comfort level into account, the

<!-- b002286 | prose | pages [40] -->
model can produce good results.

<!-- b002287 | heading | pages [40] -->
5.2.2 Sensitivity to the human parameters

<!-- b002288 | prose | pages [40] -->
In the process of building model, some influencing factors of the optimal solution like

<!-- b002289 | prose | pages [40] -->
body surface area varies from person to person. That cause changes in the optimal strategy.

<!-- b002290 | prose | pages [40] -->
Take human body surface area as an example, and observe the effect on optimal bathing

<!-- b002291 | prose | pages [40] -->
strategy. Sensitivity of the human parameters was obtained by calculating, as shown in the

<!-- b002292 | prose | pages [40] -->
following two tables.

<!-- b002293 | furniture | pages [40] -->


<!-- b002294 | furniture | pages [40] -->


<!-- b002295 | furniture | pages [41] -->
Team #46830

<!-- b002296 | furniture | pages [41] -->


<!-- b002297 | furniture | pages [41] -->


<!-- b002298 | furniture | pages [41] -->
Page 38 of 45

<!-- b002299 | caption | pages [41] -->
Table 6: Sensitivity of the human parameters (for water consumption)

<!-- b002300 | furniture | pages [41] -->


<!-- b002301 | prose | pages [41] -->
-5% -3% -1%

<!-- b002302 | prose | pages [41] -->
S 28.57% 14.29% 0%

<!-- b002303 | prose | pages [41] -->
0 1% 3% 5%

<!-- b002304 | prose | pages [41] -->
0% -42.86% -57.14% -71.43%

<!-- b002305 | furniture | pages [41] -->


<!-- b002306 | caption | pages [41] -->
Table 7: Sensitivity of the human parameters (for water temperature)

<!-- b002307 | furniture | pages [41] -->


<!-- b002308 | prose | pages [41] -->
-5% -3% -1%

<!-- b002309 | prose | pages [41] -->
S 0% 0% 0%

<!-- b002310 | prose | pages [41] -->
0 1% 3% 5%

<!-- b002311 | prose | pages [41] -->
0% -0.03% -0.03% -0.03%

<!-- b002312 | prose | pages [41] -->
We can see that the water consumption is very sensitive to the human parameters in the

<!-- b002313 | prose | pages [41] -->
 . It proves that the model we established is suitable for people of various sizes. context of 5%

<!-- b002314 | heading | pages [41] -->
5.2.3 Sensitivity to the heat transfer rate

<!-- b002315 | prose | pages [41] -->
Observation the influence of heat transfer rate on the optimal bathing strategy. Change the

<!-- b002316 | prose | pages [41] -->
heat transfer rate, then taps out the sensitivity of the heat transfer rate, as shown in the following

<!-- b002317 | prose | pages [41] -->
two tables.

<!-- b002318 | furniture | pages [41] -->


<!-- b002319 | caption | pages [41] -->
Table 8: Sensitivity of the heat transfer rate (for water consumption)

<!-- b002320 | furniture | pages [41] -->


<!-- b002321 | prose | pages [41] -->
-5% -3% -1%

<!-- b002322 | prose | pages [41] -->
28.57% 14.29% 14.29% h

<!-- b002323 | furniture | pages [41] -->


<!-- b002324 | prose | pages [41] -->
water

<!-- b002325 | prose | pages [41] -->
0 1% 3% 5%

<!-- b002326 | prose | pages [41] -->
0% -42.86% -57.14% -71.43%

<!-- b002327 | furniture | pages [41] -->


<!-- b002328 | caption | pages [41] -->
Table 9: Sensitivity of the heat transfer rate (for water temperature)

<!-- b002329 | furniture | pages [41] -->


<!-- b002330 | prose | pages [41] -->
-5% -3% -1%

<!-- b002331 | prose | pages [41] -->
-0.03% -0.03% 0.03% h

<!-- b002332 | furniture | pages [41] -->


<!-- b002333 | prose | pages [41] -->
water

<!-- b002334 | prose | pages [41] -->
0 1% 3% 5%

<!-- b002335 | prose | pages [41] -->
0% 0% 0% 0%

<!-- b002336 | prose | pages [41] -->
We can see that the water consumption is very sensitive to the heat transfer rate

<!-- b002337 | prose | pages [41] -->
 . It proves that no matter how much the effect of thermal in the context of 5%

<!-- b002338 | prose | pages [41] -->
conductivity made by bubble bath, the model we established is suitable.

<!-- b002339 | heading | pages [41] -->
6    Conclusions

<!-- b002340 | heading | pages [41] -->
6.1 Strengths and Weaknesses

<!-- b002341 | heading | pages [41] -->
6.1.1 Strengths

<!-- b002342 | prose | pages [41] -->
I. This model considers all the ways of heat flow, that is, heat conduction, convection and heat radiation, and the mathematical physics of the model is

<!-- b002343 | furniture | pages [41] -->


<!-- b002344 | furniture | pages [42] -->
Team #46830

<!-- b002345 | furniture | pages [42] -->


<!-- b002346 | prose | pages [42] -->
improved.

<!-- b002347 | furniture | pages [42] -->


<!-- b002348 | furniture | pages [42] -->
Page 39 of 45

<!-- b002349 | prose | pages [42] -->
II. This model includes a large number of parameters. These parameters include the shape and volume of the tub, the shape/volume/temperature of the person in the

<!-- b002350 | prose | pages [42] -->
bathtub, and the motions made by the person in the bathtub, they have great practical

<!-- b002351 | prose | pages [42] -->
value and a wide range of application

<!-- b002352 | prose | pages [42] -->
III. The model is fit for the complex problem of the space distribution of

<!-- b002353 | prose | pages [42] -->
temperature and convection. These fitting and approximation greatly reduce the difficulty of solving the model, and can get the results agree well with the real situation

<!-- b002354 | prose | pages [42] -->
IV. This model also takes into account the user's bath feeling, and further

<!-- b002355 | prose | pages [42] -->
improve the guiding significance of the model in the reality. In addition, according to this model, the effect of the optimal strategy has been obtained is obvious.

<!-- b002356 | prose | pages [42] -->
V. For the error analysis and sensitivity of the model, we discuss each parameter. Sensitivity analysis results show that our model parameters have a wide range of

<!-- b002357 | prose | pages [42] -->
application.

<!-- b002358 | prose | pages [42] -->
 F S V VI. The forced convection is introduced into the model（ ）to describe k k

<!-- b002359 | prose | pages [42] -->
the strength of human motions, and a complete explanation on the principle and influence are given. It is highly innovative.

<!-- b002360 | heading | pages [42] -->
6.1.2 Weaknesses

<!-- b002361 | prose | pages [42] -->
I. This model takes into account too much factors, causing the solving process is

<!-- b002362 | prose | pages [42] -->
tedious and the way to solve is difficult.

<!-- b002363 | prose | pages [42] -->
F in forced convection model）still II. One of the model parameters（Variable b

<!-- b002364 | prose | pages [42] -->
needs to be determined by experiment, and it cannot be deduced from the existing physical constants.

<!-- b002365 | prose | pages [42] -->
III. In this paper, the solution of the model is limited to the capacity of the

<!-- b002366 | prose | pages [42] -->
computer, and it can't achieve higher accuracy。

<!-- b002367 | heading | pages [42] -->
6.2 Comprehensive Results

<!-- b002368 | prose | pages [42] -->
I. Results of optimal control strategy

<!-- b002369 | prose | pages [42] -->
The result derived by solving an optimal solution is: when the flow of continuous

<!-- b002370 | prose | pages [42] -->
L s   1 bk 0.007  bT 311.1 K , and the water temperature is injection of hot water is ,

<!-- b002371 | prose | pages [42] -->
This strategy can achieve the goal of keeping the temperature even throughout the bathtub and as close as possible to the initial temperature without wasting too much

<!-- b002372 | furniture | pages [42] -->


<!-- b002373 | furniture | pages [43] -->
Team #46830

<!-- b002374 | furniture | pages [43] -->


<!-- b002375 | furniture | pages [43] -->


<!-- b002376 | furniture | pages [43] -->
Page 40 of 45

<!-- b002377 | prose | pages [43] -->
water, and the injected hot water temperature is kept in a very comfortable range. At

<!-- b002378 | prose | pages [43] -->
this point, additional water requirement is 12.6L . The ratio of the additional water requirement and the water demand of the bath is 2.84%, the optimal rate for this

<!-- b002379 | prose | pages [43] -->
strategy is 12.66%. After adding hot water, the most comfortable water temperature

<!-- b002380 | prose | pages [43] -->
satisfactory rate is 91.39%.The function of water temperature over time and space in the whole bath process is as follows:

<!-- b002381 | prose | pages [43] -->
 

<!-- b002382 | prose | pages [43] -->
T x y z t ( , , , ) T t ( )

<!-- b002383 | prose | pages [43] -->
Where the relation curve of variance

<!-- b002384 | prose | pages [43] -->
and scattered points.

<!-- b002385 | prose | pages [43] -->
 

<!-- b002386 | prose | pages [43] -->


<!-- b002387 | prose | pages [43] -->
4

<!-- b002388 | prose | pages [43] -->
  

<!-- b002389 | prose | pages [43] -->
2.45731 10 t 1

<!-- b002390 | furniture | pages [43] -->


<!-- b002391 | prose | pages [43] -->
4.294 e y

<!-- b002392 | prose | pages [43] -->
T t has been given in the form of images ( )

<!-- b002393 | prose | pages [43] -->
This series of results shows the effectiveness and the practical reference value of the optimal control model and optimization strategy. II. The situation of using the bubble water

<!-- b002394 | prose | pages [43] -->
Based on the thermodynamic model modified by bubble water, we obtain the overall heat dissipated at 312K degrees power after using the bubble is 3076.92W ,

<!-- b002395 | prose | pages [43] -->
This value is 45.85%times larger than the original. In addition, under the coordination of

<!-- b002396 | prose | pages [43] -->
the optimal policy, adding additional 12.6L hot water of 311.1K can make the

<!-- b002397 | prose | pages [43] -->
temperature difference reach 46.79%, It shows that the bubble bath and the way of adding can be very effective to keep the water temperature

<!-- b002398 | heading | pages [43] -->
6.3 Future Work

<!-- b002399 | prose | pages [43] -->
I. The variance of the water in the bathtub is measured by the actual situation or

<!-- b002400 | prose | pages [43] -->
A series of points were randomly selected on the 4.1.3.II temperature surface by

<!-- b002401 | prose | pages [43] -->
 K t in the simple function fitting programming for calculating or using the function

<!-- b002402 | prose | pages [43] -->
 T x y z t ( , , , ) T t expressions formula (11)   ( ) K t y , and then we can get more

<!-- b002403 | prose | pages [43] -->
accurate temperature distribution function in time and space.

<!-- b002404 | prose | pages [43] -->
II. By improving the algorithm and the use of more computing power compute to

<!-- b002405 | prose | pages [43] -->
calculate the accurate optimized results. Especially for the calculation of strategy 2, it

<!-- b002406 | prose | pages [43] -->
needs a powerful computer to make a further analysis, for example, solving the equivalent injection quantity of water injection in subsection by the strategy, etc.

<!-- b002407 | prose | pages [43] -->
III. We can also use this model to calculate the other bathtub, for instance the top view of the bathtub is sector, half elliptical sphere, etc.

<!-- b002408 | furniture | pages [43] -->


<!-- b002409 | furniture | pages [44] -->
Team #46830

<!-- b002410 | furniture | pages [44] -->


<!-- b002411 | furniture | pages [44] -->
Page 41 of 45

<!-- b002412 | furniture | pages [44] -->


<!-- b002413 | heading | pages [44] -->
7    Explanation

<!-- b002414 | prose | pages [44] -->
Why it's so hard to enjoy a hot bath

<!-- b002415 | prose | pages [44] -->
Is your bathtub a spa-style tub with a secondary heating system and circulating

<!-- b002416 | prose | pages [44] -->
jets? If not, then you will feel the water will gradually cool when you are taking a bath. That's right, it is extremely hard for the simple bathtub to keep constant temperature.

<!-- b002417 | prose | pages [44] -->
As we all know, if we want to keep the bath water temperature maintain a certain temperature, the only way is the injection of water. But in order to save water, we

<!-- b002418 | prose | pages [44] -->
need to take a certain strategy. Some people will do that, inject water when you feel

<!-- b002419 | prose | pages [44] -->
cold, stop adding hot water when you feel hot. But it seems a little hard to do that. We obtain the switching time, water temperature of the best strategy by the computer.

<!-- b002420 | prose | pages [44] -->
Finally, it was found that time interval between water injection and off water is zero. Is means that this method is not as good as most people think about? Maybe it’s a good idea to try another method.

<!-- b002421 | prose | pages [44] -->
Some people will leave the tap running out of hot water, and then take a

<!-- b002422 | prose | pages [44] -->
comfortable bath. In fact, this is the best way. So the problem comes, how fast to keep the hot water running, how high the temperature of hot water can keep the

<!-- b002423 | prose | pages [44] -->
temperature of bathwater constant? Generally speaking, we need to consider the heat

<!-- b002424 | prose | pages [44] -->
exchange between hot water and bath, heat exchange between hot water and air, evaporation heat absorption of hot water, heat absorption and heat release of human

<!-- b002425 | prose | pages [44] -->
body and heat radiation of water. We also need to take the heat of adding hot water and the energy taken away by overflow into account. Let alone to consider these

<!-- b002426 | prose | pages [44] -->
factors of the movement of people or bubble bath.

<!-- b002427 | furniture | pages [44] -->


<!-- b002428 | prose | pages [44] -->
In addition, personal preferences of hot water temperature settings are not

<!-- b002429 | prose | pages [44] -->
necessarily the same. To give further consideration to the human body size, the

<!-- b002430 | prose | pages [44] -->
volume and body surface area are different, the size, shape and material of each bathtub are different. Each of the above factors will affect the optimal bath strategy.

<!-- b002431 | prose | pages [44] -->
More importantly, because the heat transfer process is continuous, so it makes the calculation complexity, and we also need to consider the data acquisition and the error

<!-- b002432 | prose | pages [44] -->
of calculation. In a word, it's not easy to enjoy a hot bath.

<!-- b002433 | furniture | pages [44] -->


<!-- b002434 | furniture | pages [45] -->
Team #46830

<!-- b002435 | furniture | pages [45] -->


<!-- b002436 | heading | pages [45] -->
References

<!-- b002437 | furniture | pages [45] -->


<!-- b002438 | furniture | pages [45] -->
Page 42 of 45

<!-- b002439 | references | pages [45] -->
[1] Oronzio Manca,Sergio Nardini,Daniele icci. Numerical Analysis of Water Forced

<!-- b002440 | references | pages [45] -->
Convection in Channels with Differently Shaped Transverse Ribs. Journal of Applied

<!-- b002441 | references | pages [45] -->
Mathematics, 2011, Vol.2011, pp.1-25

<!-- b002442 | references | pages [45] -->
[2] Gheorghe Juncu. Unsteady conjugate forced convection heat/mass transfer in

<!-- b002443 | references | pages [45] -->
ensembles of Newtonian fluid spheres. International Journal of Heat and Mass

<!-- b002444 | references | pages [45] -->
Transfer, 2010, Vol.53 (13), pp.2780-2789

<!-- b002445 | references | pages [45] -->
[3] Li Liu,Xiaodong Li, Fang Q. Hu.Nonuniform-time-step explicit Runge–Kutta

<!-- b002446 | references | pages [45] -->
scheme for high-order finite difference method. Computers and Fluids,2014,Vol.105

<!-- b002447 | references | pages [45] -->
[4] Fang, Shah. The Effect of Surfactant Monolayers on the Heat Transfer Through

<!-- b002448 | references | pages [45] -->
Air/Water and Oil/Water Interfaces Using IR Imaging Technique. Journal of colloid

<!-- b002449 | references | pages [45] -->
and interface science, 1998, Vol.205 (2), pp.531-534

<!-- b002450 | references | pages [45] -->
[5] Xue-jun Zhang,Ke-qing Zheng,Ling-shi Wang,Wei Wang,Min Jiang,Sheng-ying

<!-- b002451 | references | pages [45] -->
Zhao. Analysis of ice slurry production by direct contact heat transfer of air and water

<!-- b002452 | references | pages [45] -->
solution. Journal of Zhejiang University SCIENCE A, 2013, Vol.14 (8), pp.583-588

<!-- b002453 | references | pages [45] -->
[6] Yoshihito Kurazumi,Tadahiro Tsuchikawa, Naoki Matsubara,Tetsumi Horikoshi.

<!-- b002454 | references | pages [45] -->
Effect of posture on the heat transfer areas of the human body. Building and

<!-- b002455 | references | pages [45] -->
Environment, 2007, Vol.43 (10), pp.1555-1565

<!-- b002456 | references | pages [45] -->
[7] Yoshihito Kurazumi,Tadahiro Tsuchikawa, Naoki Matsubara,Tetsumi Horikoshi.

<!-- b002457 | references | pages [45] -->
Convective heat transfer area of the human body. European Journal of Applied

<!-- b002458 | references | pages [45] -->
Physiology, 2004, Vol.93 (3), pp.273-285

<!-- b002459 | references | pages [45] -->
[8] Fajie Wang,Wen Chen,Yan Gu.Boundary element analysis of inverse heat

<!-- b002460 | references | pages [45] -->
conduction problems in 2D thin-walled structures. International Journal of Heat and

<!-- b002461 | references | pages [45] -->
Mass Transfer, 2015, Vol.91

<!-- b002462 | references | pages [45] -->
J.-L.Battaglia,O.Cois,L.Puigsegur,A.Oustaloup.Solving

<!-- b002463 | references | pages [45] -->
[9]

<!-- b002464 | references | pages [45] -->
an

<!-- b002465 | references | pages [45] -->
inverse

<!-- b002466 | references | pages [45] -->
heat

<!-- b002467 | references | pages [45] -->
conduction problem using a non-integer identified model. International Journal of

<!-- b002468 | references | pages [45] -->
Heat and Mass Transfer, 2001, Vol.44 (14), pp.2671-2680

<!-- b002469 | references | pages [45] -->
[10] Yasser Mahmoudi.Effect of thermal radiation on temperature differential in a

<!-- b002470 | references | pages [45] -->
porous medium under local thermal non-equilibrium condition .International Journal

<!-- b002471 | references | pages [45] -->
of Heat and Mass Transfer, 2014, Vol.76

<!-- b002472 | references | pages [45] -->
[11] J.R.Saylor,G.B.Smith,K.A.Flack.The effect of a surfactant monolayer on the

<!-- b002473 | references | pages [45] -->
temperature field of a water surface undergoing evaporation. International Journal of

<!-- b002474 | references | pages [45] -->
Heat and Mass Transfer, 2000, Vol.43 (17), pp.3073-3086

<!-- b002475 | references | pages [45] -->
[12] Rosario De Lisi,Stefania Milioto,Nicola Muratore. Thermodynamics of

<!-- b002476 | references | pages [45] -->
Surfactants, Block Copolymers and Their Mixtures in Water: The Role of the

<!-- b002477 | references | pages [45] -->
Isothermal Calorimetry. International Journal of Molecular Sciences, 2009, Vol.10 (7),

<!-- b002478 | references | pages [45] -->
pp.2873

<!-- b002479 | furniture | pages [45] -->


<!-- b002480 | furniture | pages [46] -->
Team #46830

<!-- b002481 | furniture | pages [46] -->


<!-- b002482 | furniture | pages [46] -->
Page 43 of 45

<!-- b002483 | furniture | pages [46] -->


<!-- b002484 | references | pages [46] -->
[13] YUAN Yirang .Finite difference method and analysis for three-dimensional

<!-- b002485 | references | pages [46] -->
semiconductor device of heat conduction. Institute of Mathematics, Science in

<!-- b002486 | references | pages [46] -->
China .Ser.A, 1996

<!-- b002487 | references | pages [46] -->
[14] Cheng Rong-Jun. Meshless analysis of three-dimensional steady-state heat

<!-- b002488 | references | pages [46] -->
Conduction problems. Ningbo Institute of Technology, 2005

<!-- b002489 | references | pages [46] -->
[15] SUN Shufen, YAN Jinfeng, XIA Nan, SUN Changhai .Development of a Model

<!-- b002490 | references | pages [46] -->
for Water and Heat Exchange Between the Atmosphere and a Water Body.

<!-- b002491 | references | pages [46] -->
Geophysical Fluid Dynamics (LASG) Institute of Atmospheric Physics Chinese

<!-- b002492 | references | pages [46] -->
Academy of Sciences, 2007

<!-- b002493 | furniture | pages [46] -->


<!-- b002494 | furniture | pages [46] -->


<!-- b002495 | furniture | pages [46] -->


<!-- b002496 | furniture | pages [46] -->


<!-- b002497 | furniture | pages [46] -->


<!-- b002498 | furniture | pages [46] -->


<!-- b002499 | furniture | pages [46] -->


<!-- b002500 | furniture | pages [46] -->


<!-- b002501 | furniture | pages [46] -->


<!-- b002502 | furniture | pages [46] -->


<!-- b002503 | furniture | pages [46] -->


<!-- b002504 | furniture | pages [46] -->


<!-- b002505 | furniture | pages [46] -->


<!-- b002506 | furniture | pages [46] -->


<!-- b002507 | furniture | pages [46] -->


<!-- b002508 | furniture | pages [46] -->


<!-- b002509 | furniture | pages [46] -->


<!-- b002510 | furniture | pages [46] -->


<!-- b002511 | furniture | pages [46] -->


<!-- b002512 | furniture | pages [46] -->


<!-- b002513 | furniture | pages [46] -->


<!-- b002514 | furniture | pages [46] -->


<!-- b002515 | furniture | pages [46] -->


<!-- b002516 | furniture | pages [46] -->


<!-- b002517 | furniture | pages [46] -->


<!-- b002518 | furniture | pages [46] -->


<!-- b002519 | furniture | pages [46] -->


<!-- b002520 | furniture | pages [46] -->


<!-- b002521 | furniture | pages [46] -->


<!-- b002522 | furniture | pages [46] -->


<!-- b002523 | furniture | pages [46] -->


<!-- b002524 | heading | pages [47] -->
Appendix

<!-- b002525 | furniture | pages [47] -->


<!-- b002526 | prose | pages [47] -->
First: program list

<!-- b002527 | prose | pages [47] -->
1.Spherical propagation of heat source

<!-- b002528 | prose | pages [47] -->
x=-2:.1:2;y=x;  %x=-1.4:0.1:2

<!-- b002529 | prose | pages [47] -->
[x,y]=meshgrid(x,y);

<!-- b002530 | prose | pages [47] -->
z=sqrt(16-x.^2-y.^2);

<!-- b002531 | prose | pages [47] -->
mesh(x,y,z)

<!-- b002532 | prose | pages [47] -->
hold on

<!-- b002533 | prose | pages [47] -->
z=z+2;

<!-- b002534 | prose | pages [47] -->
%mesh(x,y,z)

<!-- b002535 | prose | pages [47] -->
plot3(x,y,z,'r')

<!-- b002536 | prose | pages [47] -->
hold on

<!-- b002537 | prose | pages [47] -->
z=z+2;

<!-- b002538 | prose | pages [47] -->
mesh(x,y,z)

<!-- b002539 | prose | pages [47] -->
xlabel('x')

<!-- b002540 | prose | pages [47] -->
ylabel('y')

<!-- b002541 | prose | pages [47] -->
zlabel('z')

<!-- b002542 | prose | pages [47] -->
2.partial large-normal distribution

<!-- b002543 | prose | pages [47] -->
clear

<!-- b002544 | prose | pages [47] -->
clc

<!-- b002545 | prose | pages [47] -->
x=0:0.01:1;aj=0;qj=0.21829;

<!-- b002546 | prose | pages [47] -->
w=1-exp(-((x-aj)/qj).^2);

<!-- b002547 | prose | pages [47] -->
plot(x,w)

<!-- b002548 | prose | pages [47] -->
xlabel('Forced convection')

<!-- b002549 | prose | pages [47] -->
ylabel('Convective mixing ratio')

<!-- b002550 | prose | pages [47] -->
3. Solve the optimal water flow rate and optimal water temperature

<!-- b002551 | prose | pages [47] -->
function [y,Tr,Te]=algorithm2()

<!-- b002552 | prose | pages [47] -->
clear

<!-- b002553 | prose | pages [47] -->
clc

<!-- b002554 | prose | pages [47] -->
t=0.5;y=1000;

<!-- b002555 | prose | pages [47] -->
dT=0.1;total=0;

<!-- b002556 | prose | pages [47] -->
sum=0;S=0;

<!-- b002557 | prose | pages [47] -->
a=1.3;b=0.8;H=0.49;     %size of bathtub

<!-- b002558 | prose | pages [47] -->
c=4200;p=1000;         %water-specific heat capacity,

<!-- b002559 | prose | pages [47] -->
D o you usually get annoyed with the cooling of water during a relaxing bath? In this

<!-- b002560 | prose | pages [47] -->
p aper, several models are proposed to solve the problem. Our efforts in building these models

<!-- b002561 | furniture | pages [47] -->


<!-- b002562 | prose | pages [48] -->
Tb=306;h1=166;

<!-- b002563 | prose | pages [48] -->
q=2.4062*10^6;u=0.9824*10^(-3)/2;

<!-- b002564 | prose | pages [48] -->
m=5.67*10^(-8);k=0.15*10^(-3)*0.5/0.15;

<!-- b002565 | prose | pages [48] -->
k1=2.7;C0=0.4434*c*p;

<!-- b002566 | prose | pages [48] -->
C1=-a*h*(2*H+b);C2=-q*a*b*u;

<!-- b002567 | prose | pages [48] -->
C3=-h1*S1;C4=-a*b*m;

<!-- b002568 | prose | pages [48] -->
C5=c*p*k*Tb;C6=c*p*k;

<!-- b002569 | prose | pages [48] -->
x=[];

<!-- b002570 | prose | pages [48] -->
syms T;

<!-- b002571 | prose | pages [48] -->
while(Tb<318)

<!-- b002572 | prose | pages [48] -->
C5=c*p*k*Tb;

<!-- b002573 | prose | pages [48] -->
syms T Tc;

<!-- b002574 | prose | pages [48] -->
Tm=solve('-T*2.5157*10^3+2100*Tc+5.8969*10^(-8)*T^4+1.2885*10^5=0',T)

<!-- b002575 | prose | pages [48] -->
Tsk=vpa(subs(Tm,Tc,Tb));

<!-- b002576 | prose | pages [48] -->
Tsk=double(Tsk);

<!-- b002577 | prose | pages [48] -->
xe=find(Tsk>250&Tsk<320);

<!-- b002578 | prose | pages [48] -->
Ts=Tsk(xe);

<!-- b002579 | prose | pages [48] -->
Tmin1=306;

<!-- b002580 | prose | pages [48] -->
while(Tmin1<=Ts-1.1)

<!-- b002581 | prose | pages [48] -->
Tmin2=306+dT;

<!-- b002582 | prose | pages [48] -->
while(Tmin2<=Ts-1)

<!-- b002583 | prose | pages [48] -->
Tk=Tmin1;

<!-- b002584 | prose | pages [48] -->
T2=Tmin2;

<!-- b002585 | prose | pages [48] -->
total=0;S=0;sum=0;

<!-- b002586 | prose | pages [48] -->
while(Tk<=Tmin2)

<!-- b002587 | prose | pages [48] -->
betak=(C1*(Tk-T0)+C2+C3*(Tk-T1)+C4*Tk^4+C5-C6*(Tk-0.5*a*k1))/C0;

<!-- b002588 | prose | pages [48] -->
Tk1=Tk+betak;

<!-- b002589 | prose | pages [48] -->
total=total+t;

<!-- b002590 | prose | pages [48] -->
sum=sum+t;

<!-- b002591 | prose | pages [48] -->
S=(317-Tk1)*t+S;

<!-- b002592 | prose | pages [48] -->
if(betak<10^(-8))

<!-- b002593 | prose | pages [48] -->
break;

<!-- b002594 | prose | pages [48] -->
end

<!-- b002595 | prose | pages [48] -->
Tk=Tk1;

<!-- b002596 | prose | pages [48] -->
end

<!-- b002597 | prose | pages [48] -->
Tk=T2;

<!-- b002598 | prose | pages [48] -->
while(Tk>=Tmin1)

<!-- b002599 | prose | pages [48] -->
betak=(C1*(Tk-T0)+C2+C3*(Tk-T1)+C4*Tk^4)/C0;

<!-- b002600 | prose | pages [48] -->
Tk1=Tk+betak;

<!-- b002601 | furniture | pages [48] -->


<!-- b002602 | prose | pages [49] -->
sum=sum+t;

<!-- b002603 | prose | pages [49] -->
S=(317-Tk1)*t+S;

<!-- b002604 | prose | pages [49] -->
Tk=Tk1;

<!-- b002605 | prose | pages [49] -->
end

<!-- b002606 | prose | pages [49] -->
res=total/50+2*S/sum-100/(3*sqrt(2)*pi)*exp(-(Tb-312)^2/9);

<!-- b002607 | prose | pages [49] -->
if(y>res)

<!-- b002608 | prose | pages [49] -->
y=res;

<!-- b002609 | prose | pages [49] -->
Tr=Tmin1;

<!-- b002610 | prose | pages [49] -->
Te=Tmin2;

<!-- b002611 | prose | pages [49] -->
qw=[y Tr Te Ts Tb]

<!-- b002612 | prose | pages [49] -->
end

<!-- b002613 | prose | pages [49] -->
Tmin2=Tmin2+dT;

<!-- b002614 | prose | pages [49] -->
end

<!-- b002615 | prose | pages [49] -->
Tmin1=Tmin1+dT;

<!-- b002616 | prose | pages [49] -->
end

<!-- b002617 | prose | pages [49] -->
Tb=Tb+dT;

<!-- b002618 | prose | pages [49] -->
end

<!-- b002619 | prose | pages [49] -->
end

<!-- b002620 | heading | pages [49] -->
4. Solve the relationship curve between the temperature of water bathtub and time

<!-- b002621 | prose | pages [49] -->
function []=algorithm3()

<!-- b002622 | prose | pages [49] -->
clear

<!-- b002623 | prose | pages [49] -->
clc

<!-- b002624 | prose | pages [49] -->
a=1.3;b=0.8;H=0.49;

<!-- b002625 | prose | pages [49] -->
c=4200;p=1000;

<!-- b002626 | prose | pages [49] -->
h=42.8;T0=298;

<!-- b002627 | prose | pages [49] -->
S1=1.9;T1=310;

<!-- b002628 | prose | pages [49] -->
h1=166;q=2.4062*10^6;

<!-- b002629 | prose | pages [49] -->
u=0.9824*10^(-3)/2;m=5.67*10^(-8);

<!-- b002630 | prose | pages [49] -->
k1=2.7;C0=0.4434*c*p;

<!-- b002631 | prose | pages [49] -->
C1=-a*h*(2*H+b);C2=-q*a*b*u;

<!-- b002632 | prose | pages [49] -->
C3=-h1*S1;C4=-a*b*m;

<!-- b002633 | prose | pages [49] -->
beta_t=1;x=[];y=[];

<!-- b002634 | prose | pages [49] -->
Tb=311.1;kb=0.007;

<!-- b002635 | prose | pages [49] -->
k=kb*10^(-3);sum=0;Tk=317;C5=c*p*k*Tb;C6=c*p*k;C7=k1*h1*2.23;

<!-- b002636 | prose | pages [49] -->
while(sum<1800)

<!-- b002637 | prose | pages [49] -->
beta_k=(C1*(Tk-T0)+C2+C3*(Tk-T1)+C4*Tk^4+C5-C6*(Tk-0.5*a*k1))/C0;

<!-- b002638 | prose | pages [49] -->
Tnext=Tk+beta_k;

<!-- b002639 | prose | pages [49] -->
sum=sum+beta_t;

<!-- b002640 | prose | pages [49] -->
x=[x,sum];

<!-- b002641 | furniture | pages [49] -->


<!-- b002642 | prose | pages [50] -->
y=[y,Tk];

<!-- b002643 | prose | pages [50] -->
Tk=Tnext;

<!-- b002644 | prose | pages [50] -->
end

<!-- b002645 | prose | pages [50] -->
plot(x,y,'r')

<!-- b002646 | prose | pages [50] -->
hold on

<!-- b002647 | prose | pages [50] -->
sum=0;beta_t=1;x=[];y=[];Tk=317;

<!-- b002648 | prose | pages [50] -->
while(sum<1800)

<!-- b002649 | prose | pages [50] -->
beta_k=(C1*(Tk-T0)+C2+C3*(Tk-T1)+C4*Tk^4-C7)/C0;

<!-- b002650 | prose | pages [50] -->
Tnext=Tk+beta_k;

<!-- b002651 | prose | pages [50] -->
sum=sum+beta_t;

<!-- b002652 | prose | pages [50] -->
x=[x,sum];

<!-- b002653 | prose | pages [50] -->
y=[y,Tk];

<!-- b002654 | prose | pages [50] -->
Tk=Tnext;

<!-- b002655 | prose | pages [50] -->
end

<!-- b002656 | prose | pages [50] -->
plot(x,y)

<!-- b002657 | prose | pages [50] -->
%axis([0 1800 306 318])

<!-- b002658 | prose | pages [50] -->
legend('improved','normal')

<!-- b002659 | prose | pages [50] -->
xlabel('t/bath-time(s)')

<!-- b002660 | prose | pages [50] -->
ylabel('T/average temperature of water(K)')

<!-- b002661 | prose | pages [50] -->
end

<!-- b002662 | prose | pages [50] -->
6. t=pi/2:pi/20:pi;

<!-- b002663 | prose | pages [50] -->
x=sin(t)*5;

<!-- b002664 | prose | pages [50] -->
y=cos(t)*5;

<!-- b002665 | prose | pages [50] -->
z=linspace(0,5,length(t));

<!-- b002666 | prose | pages [50] -->
X=meshgrid(x);

<!-- b002667 | prose | pages [50] -->
Y=meshgrid(y);

<!-- b002668 | prose | pages [50] -->
Z=[meshgrid(z)]';

<!-- b002669 | prose | pages [50] -->
surf(X,Y,Z)

<!-- b002670 | prose | pages [50] -->
xlabel('x'),ylabel('y'),zlabel('z')

<!-- b002671 | prose | pages [50] -->
axis equal

<!-- b002672 | prose | pages [50] -->
axis([0 6 -5 0 0 5])

<!-- b002673 | prose | pages [50] -->
for k=1:4

<!-- b002674 | prose | pages [50] -->
view(-37.5,10*k)

<!-- b002675 | prose | pages [50] -->
end

<!-- b002676 | prose | pages [50] -->
hold on

<!-- b002677 | prose | pages [50] -->
[y,z]=meshgrid(-5:0,0:5);  % ---x=0

<!-- b002678 | prose | pages [50] -->
x=zeros(length(y),length(y));

<!-- b002679 | prose | pages [50] -->
%mesh(x,y,z)

<!-- b002680 | prose | pages [50] -->
surf(x,y,z)

<!-- b002681 | furniture | pages [50] -->


<!-- b002682 | prose | pages [51] -->
hold on

<!-- b002683 | prose | pages [51] -->
[x,z]=meshgrid(0:5,0:5); %  ---y=0

<!-- b002684 | prose | pages [51] -->
y=zeros(length(z),length(z));

<!-- b002685 | prose | pages [51] -->
%mesh(x,y,z)

<!-- b002686 | prose | pages [51] -->
surf(x,y,z)

<!-- b002687 | prose | pages [51] -->
hold on

<!-- b002688 | prose | pages [51] -->
alpha=-pi/2:pi/20:0;    %  --z=0

<!-- b002689 | prose | pages [51] -->
R=5;

<!-- b002690 | prose | pages [51] -->
x=R*cos(alpha);

<!-- b002691 | prose | pages [51] -->
y=R*sin(alpha);

<!-- b002692 | prose | pages [51] -->
plot(x,y,'-')

<!-- b002693 | prose | pages [51] -->
axis equal

<!-- b002694 | prose | pages [51] -->
fill([0,x],[0,y],'r');

<!-- b002695 | prose | pages [51] -->
Second:  data list

<!-- b002696 | prose | pages [51] -->
1. The data of temperature curve for fitting

<!-- b002697 | prose | pages [51] -->
x1=[0 0.1238 0.2476 0.3714 0.4952 0.619 0.7129 0.8667 1.052 1.176 1.3];

<!-- b002698 | prose | pages [51] -->
y1=[0.8  0.8  0.8   0.8   0.8    0.8   0.8   0.8   0.8   0.8   0.8];

<!-- b002699 | prose | pages [51] -->
z1=[44.3 44.17 43.73 43.08 42.34 41.68 41.09 40.58 40.02 39.79 39.67];

<!-- b002700 | prose | pages [51] -->
x2=[0 0.1857 0.3095 0.4333 0.5571 0.681 0.8048 0.9286 1.114 1.3];

<!-- b002701 | prose | pages [51] -->
y2=[0.318 0.381 0.381 0.381 0.381 0.381 0.381 0.381 0.381 0.381];

<!-- b002702 | prose | pages [51] -->
z2=[45.05 44.59 43.83 43 42.2 41.49 40.94 40.49 40.01 39.79];

<!-- b002703 | prose | pages [51] -->
x3=[0 0.1857 0.3714 0.4952 0.619 0.7429 0.8667 1.052 1.176];

<!-- b002704 | prose | pages [51] -->
y3=[0  0   0   0   0   0   0   0   0];

<!-- b002705 | prose | pages [51] -->
z3=[44.31 43.98 43.05 42.33 41.66 41.08 40.59 40.03 39.79];

<!-- b002706 | prose | pages [51] -->
x4=[0.0619 0.2476 0.3714 0.4952 0.619 0.7429 0.9286 1.114 1.3];

<!-- b002707 | prose | pages [51] -->
y4=[0.6095 0.6095 0.6095 0.6095 0.6095 0.6095 0.6095 0.6095 0.6095];

<!-- b002708 | prose | pages [51] -->
z4=[44.64 44 43.27 42.49 41.77 41.16 40.45 39.97 39.75];

<!-- b002709 | prose | pages [51] -->
x5=[0 0.1857 0.3714 0.4952 0.619 0.7429 0.9286 1.114];

<!-- b002710 | prose | pages [51] -->
y5=[0.1905 0.1905 0.1905 0.1905 0.1905 0.1905 0.1905 0.1905];

<!-- b002711 | prose | pages [51] -->
z5=[44.7 44.31 43.25 42.5  41.8  41.16  40.45 39.97];

<!-- b002712 | prose | pages [51] -->
x=[x1,x2,x3,x4,x5];

<!-- b002713 | prose | pages [51] -->
y=[y1,y2,y3,y4,y5];

<!-- b002714 | prose | pages [51] -->
z=[z1,z2,z3,z4,z5];

<!-- b002715 | furniture | pages [51] -->

