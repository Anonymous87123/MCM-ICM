# P-A-2016-42221-e0b41765

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
42221

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000004 | front_matter | pages [1] -->
A

<!-- b000005 | prose | pages [1] -->
2016 MCM/ICM

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | prose | pages [1] -->
Have a hot bath This paper establishes the heat transfer model and the optimizing model to provide the person in a simple water containment vessel with the best strategy to add water.

<!-- b000008 | prose | pages [1] -->
Firstly, according to the Fourier's law, we simplify the hot water added in as a point heat source and develop a partial differential equation model of the temperature of the bathtub water in space and time. Applying ANSYS to solve the partial differential equation, we can get the change of the temperature distribution with the water inflow per unit time and the temperature of water added in.

<!-- b000009 | prose | pages [1] -->
Secondly, making the water inflow per unit time and the temperature of water added in as design variables and setting the temperature even throughout the bathtub and as close as possible to the initial temperature while without wasting too much water as targets to establish a multi-objective optimization model. Then, we transform the multiple target into single target by using the weight methods. Next, we applying the Genetic Algorithm to solve the model, and getting the results that in the case of the certain size of the bathtub and the person. When the bathing time is 30min ,the temperature of the hot water added in is 322.71K , the water   4 3 inflow per unit time is , the variance of the finial temperature of the water is 1.2 10 m  2 0.05513K and the difference between finial temperature and initial temperature is 0.125K , 3 the water wasted is 0.23m .

<!-- b000010 | prose | pages [1] -->
Thirdly, we study how would our model’s results change with the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub(Table 6,7,8 ,Figure 13,14,16), the motions made by the person(Figure 17,18) and the addition of the bubble additive initially(Table 9 Figure 19). When the shape of the tub change, in30min washing time the temperature of the hot water added in is324.03K , the water inflow per unit time is   4 3 (Table 5 Figure 12).When the volume of the tub is getter larger, the temperature 1.5 10 m of the hot water added increases and the water inflow per unit time is the same trend(Figure 7,8,9,10).

<!-- b000011 | prose | pages [1] -->
Finally, we provide a one-page non-technical explanation for users of the bathtub to explain the strategy.

<!-- b000012 | keywords | pages [1] -->
Key words: heat transfer model, partial differential equation, multi-objective

<!-- b000013 | prose | pages [1] -->
optimization model, Genetic Algorithm

<!-- b000014 | heading | pages [2] -->
Contents

<!-- b000015 | contents | pages [2] -->
1 Introduction ................................................................................................................. 1

<!-- b000016 | contents | pages [2] -->
1.1

<!-- b000017 | contents | pages [2] -->
Background .................................................................................................. 1

<!-- b000018 | contents | pages [2] -->
1.2

<!-- b000019 | contents | pages [2] -->
Our work ....................................................................................................... 1

<!-- b000020 | contents | pages [2] -->
2

<!-- b000021 | contents | pages [2] -->
Problem restatement................................................................................................ 2

<!-- b000022 | contents | pages [2] -->
3

<!-- b000023 | contents | pages [2] -->
Terminology ............................................................................................................ 2

<!-- b000024 | contents | pages [2] -->
3.1

<!-- b000025 | contents | pages [2] -->
Terms ............................................................................................................ 2

<!-- b000026 | contents | pages [2] -->
3.2

<!-- b000027 | contents | pages [2] -->
Symbols ........................................................................................................ 3

<!-- b000028 | contents | pages [2] -->
4

<!-- b000029 | contents | pages [2] -->
General Assumptions .............................................................................................. 3

<!-- b000030 | contents | pages [2] -->
5

<!-- b000031 | contents | pages [2] -->
The Heat Transfer Model ........................................................................................ 4

<!-- b000032 | contents | pages [2] -->
5.1

<!-- b000033 | contents | pages [2] -->
Local Assumption ......................................................................................... 4

<!-- b000034 | contents | pages [2] -->
5.2

<!-- b000035 | contents | pages [2] -->
Basic model .................................................................................................. 4

<!-- b000036 | contents | pages [2] -->
5.3

<!-- b000037 | contents | pages [2] -->
Take people into consideration ..................................................................... 9

<!-- b000038 | contents | pages [2] -->
5.4

<!-- b000039 | contents | pages [2] -->
ANSYS simulation ..................................................................................... 10

<!-- b000040 | contents | pages [2] -->
6 Multi-objective optimization model ......................................................................... 11

<!-- b000041 | contents | pages [2] -->
6.1 The build of the multi-objective optimization model ..................................... 11

<!-- b000042 | contents | pages [2] -->
6.2 The strategy to add water ................................................................................ 13

<!-- b000043 | contents | pages [2] -->
7

<!-- b000044 | contents | pages [2] -->
Sensitivity Analysis ............................................................................................... 14

<!-- b000045 | contents | pages [2] -->
7.1 Change the characteristic of the bathtub ......................................................... 15

<!-- b000046 | contents | pages [2] -->
7.2 Change the characteristic of the person .......................................................... 17

<!-- b000047 | contents | pages [2] -->
7.3 Add the motion of the person in the bathtub ................................................... 19

<!-- b000048 | contents | pages [2] -->
7.4 Add the bubble additive to the bathwater ....................................................... 19

<!-- b000049 | contents | pages [2] -->
8

<!-- b000050 | contents | pages [2] -->
Strengths and Weaknesses .................................................................................... 20

<!-- b000051 | contents | pages [2] -->
8.1 Strengths ......................................................................................................... 20

<!-- b000052 | contents | pages [2] -->
8.2 Weaknesses ..................................................................................................... 20

<!-- b000053 | contents | pages [2] -->
9 Explanation for users ................................................................................................ 21

<!-- b000054 | contents | pages [2] -->
Reference ..................................................................................................................... 21

<!-- b000055 | furniture | pages [3] -->
Team # 42221

<!-- b000056 | furniture | pages [3] -->
Page 1 of

<!-- b000057 | heading | pages [3] -->
1 Introduction

<!-- b000058 | heading | pages [3] -->
1.1 Background

<!-- b000059 | prose | pages [3] -->
The bathtub, which is a simple water containment vessel and uses ceramic or other adiabatic material is often used in our daily life. Taking people’s comfort into consideration, the bathtub is designed as a container with a water inlet and water outlet, and when the tub reaches its capacity, excess water escapes through the overflow drain.

<!-- b000060 | prose | pages [3] -->
Aimed to get relaxed and cleansed, filling the bathtub with hot water before bathing is what we always do. With the time goes by, the temperature of the water will gradually drop. In order to maintain the suitable temperature, adding a constant trickle of hot water from the faucet to reheat the bathing water is necessary.

<!-- b000061 | caption | pages [3] -->
Figure 1 The bathtub we use

<!-- b000062 | prose | pages [3] -->
To have a comfortable hot bath is important for us to relax ourselves. However, there was no research on the model that can predict the temperature change of the water in the bathtub and guide people how to adjust, thus, our task is to build a model to provide a method for people to adjust the temperature of the water.

<!-- b000063 | heading | pages [3] -->
1.2 Our work

<!-- b000064 | prose | pages [3, 4] -->
Our work begins with a heat transfer model. In this model, the heat conduction equation which uses the Fourier’s law and the energy conservation law to describe the change of temperature of the water in the bathtub is established. Firstly, we only consider the circumstance that the bathtub whose shape is cuboid is filled with water and without people in it. Besides, we put a person into the model and adds a boundary condition to the heat conduction equation to get the final heat transfer model.

<!-- b000065 | furniture | pages [4] -->
Team # 42221

<!-- b000066 | furniture | pages [4] -->
Page 2 of

<!-- b000068 | prose | pages [4] -->
Based on this, we set targets keep the temperature even in the bathtub and as close as possible to the initial temperature while wasting as little as possible of the water when taking a bath to optimize the heat transfer model.

<!-- b000069 | prose | pages [4] -->
Since our task is to provide people with the strategy to put the water into the bathtub, to test the model applicability in our daily life, we change the characteristic of the bathtub, the characteristic of the person in the bathtub and add the bubble additive to find how would the result change of the multi-objective optimization model.

<!-- b000070 | prose | pages [4] -->
In this paper, the finite element analysis and ANSYS are applied to solve a four- dimensional differential heat conduction equation to get the temperature distribution of the water in the bathtub.

<!-- b000071 | heading | pages [4] -->
2 Problem restatement

<!-- b000072 | prose | pages [4] -->
The problems that we need to solve in this paper are:

<!-- b000073 | prose | pages [4] -->
 Develop a model of the temperature of the bathtub water in space and time to determine the best strategy the person in the bathtub can adopt to keep the temperature even throughout the bathtub and as close as possible to the initial temperature without wasting too much water.

<!-- b000074 | prose | pages [4] -->
 Taking the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub, the motions made by the person into consideration, to what extent does your strategy depend on these elements by using your model you build.

<!-- b000075 | prose | pages [4] -->
 If a bubble additive is used initially, how would this affect the model’s results?

<!-- b000076 | heading | pages [4] -->
3 Terminology

<!-- b000077 | heading | pages [4] -->
3.1 Terms

<!-- b000078 | prose | pages [4] -->
 Heat transfer: the phenomena that energy transfers from a hotter object to the cooler object or heat migrates from the hotter part of the object to the cooler part of the object in the case of no work. It includes three mechanisms, which are thermal conduction, thermal radiation and thermal convection.

<!-- b000079 | prose | pages [4] -->
 Thermal conduction: the heat transfer phenomena when there is no macroscopic motion within the medium, which can occur in solids, liquids and gases.

<!-- b000080 | furniture | pages [5] -->
Team # 42221

<!-- b000081 | furniture | pages [5] -->
Page 3 of

<!-- b000082 | heading | pages [5] -->
3.2 Symbols

<!-- b000083 | heading | pages [5] -->
Symbols

<!-- b000084 | prose | pages [5] -->
Descriptions

<!-- b000085 | prose | pages [5] -->
the temperature of the object in position    x y z and at timet , , T x y z t , , ,

<!-- b000086 | prose | pages [5] -->
the heat that add to the bathtub per unit time per unit volume of heat   F x y z t , , , source the region surrounded by the closed surface whose boundaries are the  surface of the water and the bathtub

<!-- b000087 | prose | pages [5] -->
 the region of the heat source 1

<!-- b000088 | prose | pages [5] -->
V the volume of the water added in per unit time p

<!-- b000089 | prose | pages [5] -->
cT the temperature of the outlet of the water

<!-- b000090 | prose | pages [5] -->
rT the temperature of the inlet of the water

<!-- b000091 | prose | pages [5] -->
the closed surface whose boundaries are the surface of the water and  the bathtub the surface that the water contact with air, the water contact with the     i i 1,2,3 bathtub and the water contact with the person

<!-- b000092 | prose | pages [5] -->
V the volume of the water in the bathtub

<!-- b000093 | prose | pages [5] -->
T the initial water temperature that is suitable for people 0

<!-- b000094 | heading | pages [5] -->
4 General Assumptions

<!-- b000095 | prose | pages [5] -->
 The initial temperature of the water of each point in the bathtub is the same.

<!-- b000096 | prose | pages [5] -->
 The room is big enough thus the temperature of the room is constant and don’t change over time and space.

<!-- b000097 | prose | pages [5] -->
 The wall of the bathtub is insulated, thus the heat transfer between it and water is ignored; because most of the bathtubs’ material is ceramic, therefore, the heat preservation is better.

<!-- b000098 | prose | pages [5] -->
 Viewing the hot water injection point at the water surface as a heat source, because the water added in is trickle and can’t influence the water in the bathtub.

<!-- b000099 | prose | pages [5] -->
 Regardless of the heat convection, only considering thermal conduction when hot water is added to the bathtub. Because the water we add in is a trickle, the flow of it can be ignored.

<!-- b000100 | furniture | pages [6] -->
Team # 42221

<!-- b000101 | furniture | pages [6] -->
Page 4 of

<!-- b000102 | prose | pages [6] -->
 Regardless of the heat dissipation in the process of the hot water flow into the bathtub, because the time that hot water flow into the bathtub is short.

<!-- b000103 | heading | pages [6] -->
5 The Heat Transfer Model

<!-- b000104 | prose | pages [6] -->
In this section, we build a system with bathtub, the outlet of the water, the inlet of the water, the temperature and the velocity of the hot water in it at first. Then we build the basic model which includes heat conduction equation to describe the temperature distribution of the water in the bathtub. At this part, we have two boundaries (the boundary that the surface water contact with air and the boundary that the bottom and side face of the water that contact with bathtub), so we get two boundary conditions. Based on this, we add a person into the system, and when the person is taking the shower, there is heat exchange between them. We can view the person as another medium and add another boundary condition to the heat conduction equation.

<!-- b000105 | prose | pages [6] -->
To solve the heat conduction equation which is a four-dimensional differential equation, we adopt the finite element analysis and use the ANSYS to find the temperature distribution at the end.

<!-- b000106 | heading | pages [6] -->
5.1 Local Assumption

<!-- b000107 | prose | pages [6] -->
 Function T x y z t has the second continuous partial derivatives for all independent   , , , variables (the function T x y z t shows the temperature of object in position x y z and at    , , , , , time t ).

<!-- b000108 | prose | pages [6] -->
 The water in the bathtub is isotropic and homogeneous; because the water difference has little difference, we can view the density of water is the same in every direction.

<!-- b000109 | prose | pages [6] -->
 The person added into the bathtub can be viewed as two cuboid spliced together, because in general, the person’s body is homogeneous.

<!-- b000110 | heading | pages [6] -->
5.2 Basic model

<!-- b000111 | prose | pages [6] -->
To make the problem simple, we set bathtub of a cuboid shape and only fill the water into the bathtub at first. Besides, there is no people in it to build the basic model.

<!-- b000112 | prose | pages [6] -->
The bathtub we use in this model is showed in Figure 1:

<!-- b000113 | furniture | pages [7] -->
Team # 42221

<!-- b000114 | furniture | pages [7] -->
Page 5 of

<!-- b000115 | caption | pages [7] -->
Figure 2 The bathtub we set in this model

<!-- b000116 | prose | pages [7] -->
To make the research of the problem easy, we build a three-dimensional coordinate system whose origin is the hot water injection point at the water surface, x-axis is parallel to the long side of the cuboid, y-axis is parallel to the short side of the cuboid and z-axis forms a right-handed coordinate system with x, y axis.

<!-- b000117 | prose | pages [7] -->
 The Fourier's law

<!-- b000118 | prose | pages [7] -->
The Fourier's law describes that the heat flow through an infinitesimal area along the surface normal direction in an infinitesimal period is proportional to the directional derivative of temperature along the surface normal direction:

<!-- b000119 | prose | pages [7] -->
 (1) T x y z t ( , , , )  dQ dSdt  n

<!-- b000120 | prose | pages [7] -->
Where:

<!-- b000121 | prose | pages [7] -->
T x y z t describes the temperature of the object in position  x y z and at timet ;    , , , , ,

<!-- b000122 | prose | pages [7] -->
is the thermal conductivity ;

<!-- b000123 | prose | pages [7] -->
dQ is the heat flow through an infinitesimal area along the surface normal direction in an infinitesimal period;

<!-- b000124 | prose | pages [7] -->
 T is the directional derivative of temperature along the surface normal direction; n

<!-- b000125 | prose | pages [7] -->
dS is the infinitesimal area and dt is the infinitesimal period.

<!-- b000126 | prose | pages [7] -->
 The heat conduction equation

<!-- b000127 | prose | pages [7] -->
For heat transfer in the water with a heat source, the energy Conservation Law with the Fourier’s law (Equation (1)) is as bellow:

<!-- b000128 | furniture | pages [8] -->
Team # 42221

<!-- b000129 | furniture | pages [8] -->
Page 6 of

<!-- b000130 | prose | pages [8] -->
                T T T T t           2 c dxdydzdt H 0                  t x x y y z z       t   1    t t         2 2 H F x y z t dxdydzdt , , , F x y z t dxdydzdt , , , (2)  1 2 t t 1 1   1 2

<!-- b000131 | prose | pages [8] -->
Where:

<!-- b000132 | prose | pages [8] -->
 T is the rate of change of temperature at a point over time; t   T x y z t describes the temperature of the object in position  x y z and at time t ; , , ,  , , is the thermal conductivity;

<!-- b000133 | prose | pages [8] -->
c is the specific heat capacity of water and is the density of water;

<!-- b000134 | prose | pages [8] -->
F x y z t is the heat that heat source releases per unit time per unit volume;   , , , 1 x y z t is the heat that water outflow releases per unit time per unit volume;   F , , , 2  is the region of the heat source flowing in per unit time; 1  is the region of the water flowing out the bathtub per unit time; 2  is the region surrounded by the closed surface whose boundaries are the surface of the water and the bathtub.

<!-- b000135 | prose | pages [8] -->
As the bathtub is full of water initially, the water inflow is equal to the water outflow, we can get:

<!-- b000136 | prose | pages [8] -->
t t t t         2 2 2 2 FV dt F V dt ( F F V dt ) FV dt 1 p 2 p 1 2 p p (3) t t t t 1 1 1 1

<!-- b000137 | prose | pages [8] -->
Where:

<!-- b000138 | prose | pages [8] -->
F x y z t is the heat that add to the bathtub per unit time per unit volume of heat   , , , source.

<!-- b000139 | prose | pages [8] -->
For the temperature of the hot water added in is constant, thereby the value of the   F x y z t , , , is constant, we can put F x y z t outside of the integral sign. So we get:   , , ,

<!-- b000140 | prose | pages [8] -->
                 T T T T t           2 c dxdydz FV dt 0           p        t x x y y z z         t     1  (3) Where:

<!-- b000141 | prose | pages [8] -->
V is the volume of the water added in per unit time. p

<!-- b000142 | prose | pages [8] -->
For the value of the variables 1t and 2t is arbitrary, and for any time interval, the equation (3) is tenable. Thus, we can get:

<!-- b000143 | prose | pages [8] -->
               T T T T           c dxdydz FV 0         p        t x  x  y y z  z       (4) Put forward the integral sign:

<!-- b000144 | prose | pages [8] -->
  FV              T T T T  p          c dxdydz 0                t V x  x  y y z  z        (5)

<!-- b000145 | prose | pages [8] -->
Where:

<!-- b000146 | furniture | pages [9] -->
Team # 42221

<!-- b000147 | furniture | pages [9] -->
Page 7 of

<!-- b000148 | prose | pages [9] -->
Vis the volume of the water in the bathtub.

<!-- b000149 | prose | pages [9] -->
F is the heat that the heat source releases per unit time per unit volume and can be calculated in the equation shown bellow:

<!-- b000150 | prose | pages [9] -->
     (6) F c T T r c Where:

<!-- b000151 | prose | pages [9] -->
T is the temperature of the inlet of water； r T is the temperature of the outlet of the water. c

<!-- b000152 | prose | pages [9] -->
Eventually, the heat conduction equation we get is；      T T V      2 2 2 T T T T r c p       (7)      2 2 2 t V c x y z   

<!-- b000153 | prose | pages [9] -->
 Boundary conditions

<!-- b000154 | prose | pages [9] -->
We divide the closed surface whose boundaries are the surface of the water and the  : bathtub into two part , 1 2  (8) 1 2 Where:

<!-- b000155 | prose | pages [9] -->
is the surface that the water contact with air; 1 is the surface that the water contact with bathtub. 2 : Then we get the boundary conditions for surface , 1 2  T         T T , x y z , , 1 1 1 1  n 1 (9)  T         T T , x y z , , 2 2 2 2  n 2 (10) Where:

<!-- b000156 | prose | pages [9] -->
is the thermal conductivity among water;

<!-- b000157 | prose | pages [9] -->
is the heat transfer coefficient between water and air; 1 is the heat transfer coefficient between water and bathtub; 2 1T is the temperature of the air and 2T is the temperature of the bathtub;

<!-- b000158 | prose | pages [9] -->
T is the temperature of the surface of the water;

<!-- b000159 | prose | pages [9] -->
n n are the normal vectors for the upper surface of the water the faces that , 1 2 water contact with bathtub;

<!-- b000160 | prose | pages [9] -->
 T i    are the directional derivative of temperature along the upper surface 1,2  n i of the water the faces that the water contact with bathtub.

<!-- b000161 | prose | pages [9] -->
While, as the assumptions we propose above, the wall of the bathtub is insulated, thus the directional derivative of temperature along the normal direction of the wall of bathtub is zero, so the equation (9) can be changed to:

<!-- b000162 | furniture | pages [10] -->
Team # 42221

<!-- b000163 | furniture | pages [10] -->
Page 8 of

<!-- b000164 | prose | pages [10] -->
(11)  T     0, x y z , , 2  n 2

<!-- b000165 | prose | pages [10] -->
 Initial condition

<!-- b000166 | prose | pages [10] -->
t , the value of 0 Besides, we provide the initial condition that at the initial time temperature in each point of bathtub is the initial temperature of the water T in bathtub 0 which is suitable for people:

<!-- b000167 | prose | pages [10] -->
(12)    T x y z , , ,0 T 0

<!-- b000168 | prose | pages [10] -->
Where:

<!-- b000169 | prose | pages [10] -->
T is the initial water temperature that is suitable for people; 0   is the water temperature in position  x y z at the initial time. T x y z , , ,0 , ,

<!-- b000170 | prose | pages [10] -->
 The final equations

<!-- b000171 | prose | pages [10] -->
Adding the initial condition and the boundary condition to the heat conduction equation, we get the heat transfer model eventually. The final equations are shown bellow；

<!-- b000172 | prose | pages [10] -->
        2 2 2 T T T T        f , x y z , ,         2 2 2 t c x y z        T T V  r c p  f  V s        T x y z , , ,0 T , x y z , ,  0   T          T T , x y z , , （13） 1 1 1 1   n 1  T      0, x y z , ,  2 n  2

<!-- b000173 | prose | pages [10] -->
Where:

<!-- b000174 | prose | pages [10] -->
 T is the rate of change of temperature at a point over time; t T x y z t describes the temperature of the object in position  x y z and at time t ;    , , , , , is the thermal conductivity ;

<!-- b000175 | prose | pages [10] -->
c is the specific heat capacity of water and is the density of water;

<!-- b000176 | prose | pages [10] -->
Vis the volume of the water in the bathtub;

<!-- b000177 | prose | pages [10] -->
V is the volume of the water added in per unit time; p

<!-- b000178 | prose | pages [10] -->
is the heat transfer coefficient between water and air; 1 T is the initial water temperature that is suitable for people; 0 n n are the normal vectors for the upper surface of the water, the faces that the , 1 2 water contact with bathtub;

<!-- b000179 | prose | pages [10] -->
1T is the temperature of the air.

<!-- b000180 | furniture | pages [11] -->
Team # 42221

<!-- b000181 | furniture | pages [11] -->
Page 9 of

<!-- b000182 | heading | pages [11] -->
5.3 Take people into consideration

<!-- b000183 | prose | pages [11] -->
Further, we take a person into consideration. The person will have the temperature exchange with the water while having the shower. To research the influence of the person to the temperature distribution of the water in the bathtub, we view the person’s shape as two cuboid spliced together which is shown in Figure 3, the size of the cuboid bellow is   and the size of the cuboid above is 0.5   1.1 m 0.45 m 0.25 m m 0.3 m 0.45 m

<!-- b000184 | caption | pages [11] -->
Figure 3 The placement of the person in water

<!-- b000185 | prose | pages [11] -->
The addition of the person add one boundary condition to the heat conduction equation, which is:

<!-- b000186 | prose | pages [11] -->
 (14) T      T T 3 3 3  n 3 Where:

<!-- b000187 | prose | pages [11] -->
3T is the temperature of the person;

<!-- b000188 | prose | pages [11] -->
is the heat transfer coefficient between water and the person; 3 2n is the normal vector of the surface of the person.

<!-- b000189 | prose | pages [11] -->
Adding the boundary condition to equation (12), we get:

<!-- b000190 | prose | pages [11] -->
        2 2 2 T T T T        f , x y z , ,         2 2 2 t c x y z        T T V  r c p  f  V         T x y z , , ,0 T , x y z , ,  0  T          T T , x y z , , 1 1 1 1  n  1  T      0, x y z , , 2 n  2  (15)  T          T T , x y z , , 3 3 3 3   n 3 Where:

<!-- b000191 | prose | pages [11, 12] -->
 T is the rate of change of temperature at a point over time; t T x y z t describes the temperature of the object in position  x y z and at time t ;    , , , , , is the thermal conductivity ;

<!-- b000192 | furniture | pages [12] -->
Team # 42221

<!-- b000193 | furniture | pages [12] -->
Page 10 of

<!-- b000195 | prose | pages [12] -->
c is the specific heat capacity of water and is the density of water;

<!-- b000196 | prose | pages [12] -->
Vis the volume of the water in the bathtub;

<!-- b000197 | prose | pages [12] -->
  is the heat transfer coefficient between water and air and between   i i 1, 3 water and the person;

<!-- b000198 | prose | pages [12] -->
T is the initial water temperature that is suitable for people; 0 1n , 2n , 3n are the normal vectors for the upper surface of the water, the faces that the water contact with bathtub and the surface of the person;

<!-- b000199 | prose | pages [12] -->
  is the temperature of the air and temperature of the person. iT i  1,3

<!-- b000200 | heading | pages [12] -->
5.4 ANSYS simulation

<!-- b000201 | prose | pages [12] -->
Given a certain circumstance, in which the bathing time is30min , the size of the bathtub   is 1.5 0.5 0.7 and the values of other variables we set are shown in the Table 1.

<!-- b000202 | caption | pages [12] -->
Table 1 The values of the parameters

<!-- b000203 | prose | pages [12] -->
1 c f 1T 0T Parameter  15 / ( J Ksm ) 4200 / ( J kg K ) 100J 308K 321K Value    3T Parameter 3 0.64 / ( J Ksm ) 200 / ( J Ksm ) 320K 3 Value kg m 1000 /

<!-- b000204 | prose | pages [12, 13] -->
we use the heat transfer model and apply ANSYS to simulate the temperature distribution of the water with a person in the bathtub. The process of the temperature distribution for 2-D dimensional is shown in Figure 3(the 2-D dimensional plane we choose in the bathtub is parallel to the horizontal plane) The temperature distribution of the water in the bathtub can be seen in Figure 5:

<!-- b000205 | furniture | pages [13] -->
Team # 42221

<!-- b000206 | furniture | pages [13] -->
Page 11 of

<!-- b000207 | caption | pages [13] -->
Figure 4 The process of the temperature distribution for 2-D dimensional

<!-- b000209 | caption | pages [13] -->
Figure 5 The temperature distribution in certain circumstance

<!-- b000210 | heading | pages [13] -->
6 Multi-objective optimization model

<!-- b000211 | prose | pages [13] -->
In this section, with the targets of wasting as little water as possible, keeping the temperature even and as close as possible to the initial temperature, we apply a multi- objective optimization to the heat transfer model to get the best strategy that can be applied for people in our daily life.

<!-- b000212 | heading | pages [13] -->
6.1 The build of the multi-objective optimization model

<!-- b000213 | prose | pages [13] -->
To make the temperature in the bathtub even and as close as possible to the initial temperature, we need to calculate the finial average temperature of the water after taking the shower, which is:

<!-- b000214 | furniture | pages [14] -->
Team # 42221

<!-- b000215 | furniture | pages [14] -->
Page 12 of

<!-- b000216 | prose | pages [14] -->
1   T T x y z t dxdydz ( , , , ) z z V (16)  Where:

<!-- b000217 | prose | pages [14] -->
zt is the time that the person finish the bathing;

<!-- b000218 | prose | pages [14] -->
zT is the finial average temperature of the water after taking the shower;

<!-- b000219 | prose | pages [14] -->
To make the temperature as evenly as possible. The first objective function is:

<!-- b000220 | prose | pages [14] -->
1       2 2 min ( T x y z t , , , T ) dxdydz z z V (17)   Where:

<!-- b000221 | prose | pages [14] -->
is the variance of the finial temperature of the water. 2

<!-- b000222 | prose | pages [14] -->
To make the temperature of the water as close as possible to the initial temperature. The second objective function is:

<!-- b000223 | prose | pages [14] -->
(18)    min T T T z z 0 Where:

<!-- b000224 | prose | pages [14] -->
is the temperature difference between final average temperature and initial zT temperature of the water in bathtub.

<!-- b000225 | prose | pages [14] -->
As the bathtub is filled with water at the initial time, the water inflow is equal to the water outflow. We can minimize the water inflow to get the minimum wasting water. The third objective function is:

<!-- b000226 | prose | pages [14] -->
V min p (19) The range of the temperature we added in is from 317k to 323k, and the range of the volume  of the hot water added in per unit time is from 0 to  , which are the restriction 4 3 2 10 m conditions:

<!-- b000227 | prose | pages [14] -->
   317 K T 323 K r st . 0    4 3 V 2 10 m  p (20) Eventually, we get the finial multi-objective optimization model, which is:

<!-- b000228 | prose | pages [14] -->
find T V r p 1       2 2 min ( T x y z t , , , T ) dxdydz z z V      min T T T z z 0 min V p    317 K T 323 K r (21) st . 0    4 3 V 2 10 m  p

<!-- b000229 | prose | pages [14] -->
Where:

<!-- b000230 | prose | pages [14] -->
zT is the finial average temperature of the water after taking the shower;

<!-- b000231 | prose | pages [14] -->
zt is the time that the person finish the bathing;

<!-- b000232 | prose | pages [14, 15] -->
is the variance of the finial temperature of the water; 2   is the temperature of the water in positon  x y z and at time t ; T x y z t , , , z , , is the temperature difference between final average temperature and initial zT temperature of the water in bathtub;

<!-- b000233 | furniture | pages [15] -->
Team # 42221

<!-- b000234 | furniture | pages [15] -->
Page 13 of

<!-- b000236 | prose | pages [15] -->
T is the initial water temperature that is suitable for people; 0 T is the temperature of the inlet of water； r T is the temperature of the outlet of the water; c

<!-- b000237 | prose | pages [15] -->
V is the volume of the water added in per unit time. p To solve the multi-objective optimization model, we set different weight to the variance of the final temperature and the temperature difference between final average temperature and initial temperature, and change the multi-objective to the single objective optimization model:

<!-- b000238 | prose | pages [15] -->
find T V r p       2 min T V 1 2 z 3 p    317 K T 323 K r     4 3 0 V 2 10 m  p st .       1  (22) 1 2 3     ( i 1,2,3) 0  i

<!-- b000239 | prose | pages [15] -->
Where:

<!-- b000240 | prose | pages [15] -->
V is the volume of the water added in per unit time; p

<!-- b000241 | prose | pages [15] -->
T is the temperature of the inlet of water； r is the variance of the finial temperature of the water; 2

<!-- b000242 | prose | pages [15] -->
is the temperature difference between final average temperature and initial zT temperature of the water in bathtub;

<!-- b000243 | prose | pages [15] -->
is the weight of the the variance of the finial temperature of the water; 1 is the weight of the temperature difference between final average temperature and 2 initial temperature of the water in bathtub;

<!-- b000244 | prose | pages [15] -->
is the weight of the water wasted per unit time. 3 Using this model, we can calculate the temperature and the velocity of the hot water we need to add in with the certain targets, thereby, a strategy to add water can be provided for people.

<!-- b000245 | heading | pages [15] -->
6.2 The strategy to add water

<!-- b000246 | prose | pages [15] -->
To solve the multi-objective optimization model in order to propose the strategy to add water, we use the Genetic Algorithm and address the problem in four steps: (1) At first step, we select countless values from the range of the temperature and the range of the volume of the hot water added in per unit time we set in equation (20) (2) At second step, using the objective function       to filter the 2 min T V 1 2 z 3 p selected values, and then get the values that satisfied the objective function (3) At third step, based on the values we picked out, using the objective function to filter. (4) At fourth step, repeat the third step until find out the best strategy.

<!-- b000247 | prose | pages [15] -->
We set the values of the parameters in the Genetic Algorithm, which is shown in Table 2:

<!-- b000248 | furniture | pages [16] -->
Team # 42221

<!-- b000249 | furniture | pages [16] -->
Page 14 of

<!-- b000250 | caption | pages [16] -->
Table 2 The values of the parameters in Genetic Algorithm

<!-- b000251 | prose | pages [16] -->
Evolutionary Crossover Mutation Sample size Parameter times probability probability 8 0.4 0.2 41 Value    Parameter 1 2 3 0.6 0.4 0 Value Using Matlab to programme and call the ANSYS to calculate the best strategy to add water. The values of the variables in the model shown in the Table 3 and the strategy how to add the water is shown in Table 4.

<!-- b000252 | caption | pages [16] -->
Table 3 The values of the variables in the model

<!-- b000253 | prose | pages [16] -->
1 c 1T 0T Size of the Parameter bathtub    15 / ( J Ksm ) 4200 / ( J kg K ) 308K 321K 1.5 0.5 0.7 Value    3T Shower time Parameter 3 0.64 / ( J Ksm ) 200 / ( J Ksm ) 320K 3 Value 30min kg m 1000 /

<!-- b000254 | caption | pages [16] -->
Table 4 The best strategy to add water

<!-- b000255 | prose | pages [16] -->
V  rT V zT  Variable 2 p  0.05513 322.71K  0.23m  0.125K Value 3 4 3 1.2 10 m Where:

<!-- b000256 | prose | pages [16] -->
V is the water we waste.

<!-- b000257 | prose | pages [16] -->
We get the final temperature distribution after shower of the best strategy in Figure 6.

<!-- b000258 | caption | pages [16] -->
Figure 6 The temperature distribution of the best strategy

<!-- b000259 | heading | pages [16] -->
7 Sensitivity Analysis

<!-- b000260 | prose | pages [16] -->
To provide people with strategy to add water better. In this part, we find the influence of the shape and volume of the tub, the shape/volume/temperature of the person taking a bathing and the bubble additive to the multi-objective optimization model.

<!-- b000261 | furniture | pages [17] -->
Team # 42221

<!-- b000262 | furniture | pages [17] -->
Page 15 of

<!-- b000263 | prose | pages [17] -->
First step, we research the influence of the characteristic of the tub. We change the size of the length, width and height of the tub of a cuboid shape respectively to the multi-objective optimization and we design the shape of the bathtub closer to life to find the better strategy to add water.

<!-- b000264 | prose | pages [17] -->
Next step, we research the influence of the characteristic of the person. We change the size of the person and the temperature to find the results of the multi-objective optimization model. Besides, we take the motion of the person in the water into consideration. The movement of the person leads to the movement of the water, thus we can think that the forced convection happens to the water which makes the heat transfer coefficient between water and air and between water and the person get changed. At the end, we add the bubble bath 1, to additive initially, which only change the heat transfer coefficient between water and air find how the strategy changes.

<!-- b000265 | prose | pages [17] -->
Lastly, we research the influence of the addition of the bubble additive which changes the heat transfer coefficient between water and air. Changing the heat transfer coefficient between water and air to get the best strategy to add water

<!-- b000266 | heading | pages [17] -->
7.1 Change the characteristic of the bathtub

<!-- b000267 | prose | pages [17] -->
 Change the area of the bathtub’s upper surface We change the area of the bathtub’s upper surface to change the volume of the bathtub, and get the change of optimal temperature of the water added in and the optimal water inflow per unit time with the area, the result is shown on Figure 7,8

<!-- b000268 | caption | pages [17] -->
Figure 7 The change of the optimal temperature

<!-- b000269 | caption | pages [17] -->
Figure 8 The change of the optimal water inflow

<!-- b000270 | prose | pages [17] -->
per unit time with area of the water added in with the area

<!-- b000271 | prose | pages [17] -->
Where:

<!-- b000272 | prose | pages [17] -->
x-axis in Figure 7,8 represents the change of the area;

<!-- b000273 | prose | pages [17] -->
y-axis in Figure 7 represents the change of the optimal temperature of the water added in;

<!-- b000274 | prose | pages [17] -->
y-axis in Figure 8 represents the change of the optimal volume of the water inflow per unit time.

<!-- b000275 | prose | pages [17, 18] -->
The increase of the upper surface’s area causes the increase of the heat exchange ( between water and area), moreover the heat added in increases. We can find both optimal temperature and optimal water inflow per unit time are increasing with the increase of the area.  Change the height of the bathtub We change the height of the bathtub to change the volume of the bathtub, and get the change of optimal temperature of the water added in and the optimal water inflow per unit time with the height, the result is shown on Figure 9,10.

<!-- b000276 | furniture | pages [18] -->
Team # 42221

<!-- b000277 | furniture | pages [18] -->
Page 16 of

<!-- b000279 | caption | pages [18] -->
Figure 9 The change of the optimal temperature

<!-- b000280 | caption | pages [18] -->
Figure 10 The change of the optimal water

<!-- b000281 | prose | pages [18] -->
inflow per unit time with the height with the height

<!-- b000282 | prose | pages [18] -->
Where:

<!-- b000283 | prose | pages [18] -->
x-axis in Figure 9,10  represents the change of the height;

<!-- b000284 | prose | pages [18] -->
y-axis in Figure 9 represents the change of the optimal temperature of the water added in;

<!-- b000285 | prose | pages [18] -->
y-axis in Figure 10 represents the change of the optimal water inflow per unit time.

<!-- b000286 | prose | pages [18] -->
The increase of the height only causes the increase of the volume of the bathtub, while the area of the water contact with air is not influenced, furthermore, the heat loss isn’t influenced. Thus the curves in the Figure 9,10 are relatively flat.  Change the shape of the bathtub Based on the multi-objective optimization model, and keeping the volume of the bathtub invariant, we design the shape of the bathtub closer to life which is presented in Figure 11 to find the best strategy to add water(Table 5 ) and the final temperature distribution(Figure 12)

<!-- b000287 | caption | pages [18] -->
Table 5 The best strategy to add water after changing the shape of the bathtub

<!-- b000288 | prose | pages [18, 19] -->
V  rT V zT  Variable 2 p  0.0676 324.03K  0.27m  0.1503K Value 3 4 3 1.5 10 m the shape of the bathtub

<!-- b000289 | furniture | pages [19] -->
Team # 42221

<!-- b000290 | furniture | pages [19] -->
Page 17 of

<!-- b000291 | caption | pages [19] -->
Figure 11 The shape of the bathtub after changing

<!-- b000292 | caption | pages [19] -->
Figure 12 The temperature distribution after changing

<!-- b000294 | prose | pages [19] -->
From the figures above, we can find that the temperature of the hot water added in is higher, and the water inflow per unit time is larger than the bathtub of the cuboid shape. With the same volume the area of the upper surface of the bathtub is bigger and the heat loss increases, thus more heat needs to be added in.

<!-- b000295 | heading | pages [19] -->
7.2 Change the characteristic of the person

<!-- b000296 | prose | pages [19] -->
 Change the volume of the person We change the volume of the person which influence the boundary condition of the person and get the change of optimal temperature of the water added in and the optimal water inflow per unit time with the volume of the person, the result is shown on Figure 13,14.

<!-- b000297 | caption | pages [19] -->
Figure 13 The change of the optimal

<!-- b000298 | caption | pages [19] -->
Figure 14 The change of the optimal water inflow

<!-- b000299 | prose | pages [19] -->
temperature with the volume of the person per unit time with the volume of the person

<!-- b000300 | prose | pages [19] -->
Where:

<!-- b000301 | prose | pages [19] -->
x-axis in Figure 13,14 represents the change of the volume of the person;

<!-- b000302 | prose | pages [19] -->
y-axis in Figure 13 represents the change of the optimal temperature of the water added in;

<!-- b000303 | prose | pages [19] -->
y-axis in Figure 14 represents the change of the optimal water inflow per unit time.

<!-- b000304 | prose | pages [19, 20] -->
From the figures, we find that the strategy to add water change a little with the increase of the volume of the person. For the increase of the volume of the person resulting in the surface people contact with water. Furthermore, the heat exchange between people and water get a little increase, so the heat added in has slight increase.  Change the shape of the person Keeping the volume of the person invariant and we change the shape of the person into the two cylinders spliced together, which is shown in Figure 15, to find the best strategy to add water(Table 6) and the final temperature distribution(Figure 16).

<!-- b000305 | furniture | pages [20] -->
Team # 42221

<!-- b000306 | furniture | pages [20] -->
Page 18 of

<!-- b000308 | caption | pages [20] -->
Table 6 The best strategy to add water when change the shape of the person

<!-- b000309 | prose | pages [20] -->
V  rT V zT  Variable 2 p 0.0266  323.135K  0.358m  0.158K Value 3 4 3 1.99 10 m

<!-- b000310 | caption | pages [20] -->
Figure 15 the shape of the person after change

<!-- b000311 | caption | pages [20] -->
Figure 16 the temperature distribution after

<!-- b000312 | prose | pages [20] -->
changing the shape of the person From the result, we can find that when the shape of the person is close to reality, the difference between the final temperature and the initial temperature, the wasting water and the water inflow per unit time get some increase. According to the mathematical knowledge, in the same volume, the cylinder’s surface area is bigger than the cuboid’s surface area thus the area the person contact with water increases which leads to more heat exchange. Hence, more heat is needed.

<!-- b000313 | prose | pages [20] -->
Change the temperature of the person  The range of the temperature change of the person is relatively small, thus we only study the strategy to add water when the temperature are 319.5K and 320.5K which is shown in Table 7,8.

<!-- b000314 | caption | pages [20] -->
Table 7 The best strategy to add water when the temperature of the person is 319.5K

<!-- b000315 | prose | pages [20] -->
V  rT V zT  Variable 2 p  0.0487 319.5K  0.361m  0.1176K Value 3 4 3 2.01 10 m

<!-- b000316 | caption | pages [20] -->
Table 8 The best strategy to add water when the temperature of the person is 320.5K

<!-- b000317 | prose | pages [20] -->
V  rT V zT  Variable 2 p  0.0413 320.5K  0.342m  0.1215K Value 3 4 3 1.90 10 m Although the temperature of the surface of the body maybe change for some reasons, for example, getting ill, the range is relatively small. And the temperature of body is close to the temperature of water, so the heat exchange is small. Thus, the change of the temperature of the person has little influence on the strategy to add water.

<!-- b000318 | furniture | pages [21] -->
Team # 42221

<!-- b000319 | furniture | pages [21] -->
Page 19 of

<!-- b000320 | heading | pages [21] -->
7.3 Add the motion of the person in the bathtub

<!-- b000321 | prose | pages [21] -->
Considering the actual situation, we add the motion of the person in the bathtub to obtain the strategy to add water. The motion of the person only change the heat transfer coefficient 1 and the heat transfer coefficient between water and the person and between water and air 3 other variables are the same as the values of the variables we choose in Table 3.

<!-- b000322 | prose | pages [21] -->
We use percentage to measure the intensity of the motion, and obtain the change of the optimal temperature of the water added in and the optimal water inflow per unit time with the percentage, the result is shown on Figure 17,18.

<!-- b000323 | caption | pages [21] -->
Figure 17 The change of optimal temperature

<!-- b000324 | caption | pages [21] -->
Figure 18 The change of the optimal water

<!-- b000325 | prose | pages [21] -->
with the percentage inflow per unit time with the percentage

<!-- b000326 | prose | pages [21] -->
Where:

<!-- b000327 | prose | pages [21] -->
x-axis in Figure 17,18 represents the change of the percentage which measures the intensity of the motion;

<!-- b000328 | prose | pages [21] -->
y-axis in Figure 17 represents the change of the optimal temperature of the water added in;

<!-- b000329 | prose | pages [21] -->
y-axis in Figure 18 represents the change of the optimal water inflow per unit time.

<!-- b000330 | prose | pages [21] -->
We can find that the optimal temperature of the water added in and the optimal water inflow per unit time are get larger with the increase of the intensity of the motion. Because the intenser the movement is, the more heat dissipates. If we want to keep the temperature even and as close as possible to the initial temperature, more heat will be added in the bathtub.

<!-- b000331 | heading | pages [21] -->
7.4 Add the bubble additive to the bathwater

<!-- b000332 | prose | pages [21] -->
The addition of the bubble additive only change the heat transfer coefficient between 1, the values of the other variables in the multi-objective optimization we water and air 1as 11 / ( choose are the same as what we choose in Table 3. We set the value of Ksm ,and J ) obtain the strategy to add water (Table 9). At the same time, the final temperature distribution is presented in Figure 19.

<!-- b000333 | caption | pages [21] -->
Table 9 The best strategy to add water when the bubble additive is added initially

<!-- b000334 | prose | pages [21, 22] -->
V  rT V zT  Variable 2 p  0.0189 321.02K  0.286m  0.1144K Value 3 4 3 1.59 10 m We come to the conclusion that compared with the circumstance without the bubble additive in the water, the variance of the finial temperature of the water and the water inflow per unit time increase, while the temperature of the inlet of water and the temperature difference between final average temperature and initial temperature of the water in bathtub decrease.

<!-- b000335 | furniture | pages [22] -->
Team # 42221

<!-- b000336 | furniture | pages [22] -->
Page 20 of

<!-- b000337 | caption | pages [22] -->
Figure 19 The final temperature distribution when the bubble additive is added initially

<!-- b000339 | heading | pages [22] -->
8 Strengths and Weaknesses

<!-- b000340 | heading | pages [22] -->
8.1 Strengths

<!-- b000341 | prose | pages [22] -->
(1) The main strength of our model is close to the reality. The heat exchange between people and water and between water and air is considered when research the temperature distribution in the bathtub. (2) To test the application of the model in our daily life, we take the characteristic of the person and the motions of the person into discussion. (3) Besides, considering the comfort of the person, we also change the cross section of the bathtub to isosceles trapezoid and change the sloped angle of the trapezoid to discuss the temperature distribution.

<!-- b000342 | heading | pages [22] -->
8.2 Weaknesses

<!-- b000343 | prose | pages [22] -->
(1) The calculation of our model is complex, we need to solve a four-dimensional differential equation. (2) The bathroom of small size whose room temperature is changed is not taken into consideration.

<!-- b000344 | furniture | pages [23] -->
Team # 42221

<!-- b000345 | furniture | pages [23] -->
Page 21 of

<!-- b000346 | prose | pages [23] -->
(3) When we change the shape of the person in the bathtub in the sensitivity analysis of our model, we only consider the change based on the shape of a cuboid. But other changes such as cylinder is not taken into consideration.

<!-- b000347 | heading | pages [23] -->
9 Explanation for users

<!-- b000348 | prose | pages [23] -->
The bathtub we use in our daily life is a simple water containment vessel, in order to take a shower comfortably, the person needs to add a constant trickle of the hot water from the faucet. Here, we give the explanation of the strategy to add water researched in this paper.

<!-- b000349 | prose | pages [23] -->
If the bathtub you use is a little larger than the normal size, you should increase the temperature of the hot water added in by14.28K per unit cubic meter. You’d batter to use the bathtub whose upper surface is not very big. Besides, if you are fat, maybe you should increase the temperature of the hot water a little (about 0.5K ). If the temperature of your body surface is a little higher, to decrease the temperature of the hot water. Some children like playing while taking the shower, you need to increase the temperature of the water according to the intensity of his movement; if he is crazy, you need to increase the temperature by 2K . Bubble additive is our preference; don’t forget to decrease the temperature if you want to have a comfortable washing.

<!-- b000350 | prose | pages [23] -->
While, getting an evenly maintained temperature throughout the bath water is difficult. We have the reasons as follow: (1) Without hot water added in, the surface of the water contact with air will have the heat loss making the temperature of the upper layer and lower layer different. Besides, the motion of the person is complex, which leads to the complexity of the heat loss (2) With hot water added in, the temperature of the inlet is different with the temperature of the outlet. When the volume of the bathtub gets bigger, with the restriction of the water inflow(the maximum flow of the faucet is definite), the heat that the water in the outlet absorbs is litter which makes the temperature gradient from inlet to the outlet becomes large

<!-- b000351 | heading | pages [23] -->
Reference

<!-- b000352 | references | pages [23] -->
[1]  GU CHaohao&LI Daqian & CHEN SHuxing & ZHEN Songmu & TAN Yongji.

<!-- b000353 | references | pages [23] -->
Equations of Mathematical Physics[M].Beijing: Higher Education Press,2012.7

<!-- b000354 | references | pages [23] -->
[2]  K.Deb.Multi-objective Genetic Algorithms: Problem Difficulties and Construction of

<!-- b000355 | references | pages [23] -->
Test Problems. Evolutionary Computation .(1999)

<!-- b000356 | references | pages [23] -->
[3]  XU Lei. Multi-objective optimization problem based on genetic algorithm research

<!-- b000357 | references | pages [23] -->
and application[D]. Central South University,(2007).

<!-- b000358 | references | pages [23] -->
[4]  Finite Element Analysis and Optimal Design Based on ANSYS in a XH2408 Gantry

<!-- b000359 | references | pages [23] -->
Style NC Machining Center[J]. International Journal of Plant Engineering and

<!-- b000360 | references | pages [23] -->
Management,2010,03:188-192.
