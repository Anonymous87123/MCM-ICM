2016 MCM/ICM

Summary Sheet

Have a hot bath This paper establishes the heat transfer model and the optimizing model to provide the person in a simple water containment vessel with the best strategy to add water.

Firstly, according to the Fourier's law, we simplify the hot water added in as a point heat source and develop a partial differential equation model of the temperature of the bathtub water in space and time. Applying ANSYS to solve the partial differential equation, we can get the change of the temperature distribution with the water inflow per unit time and the temperature of water added in.

Secondly, making the water inflow per unit time and the temperature of water added in as design variables and setting the temperature even throughout the bathtub and as close as possible to the initial temperature while without wasting too much water as targets to establish a multi-objective optimization model. Then, we transform the multiple target into single target by using the weight methods. Next, we applying the Genetic Algorithm to solve the model, and getting the results that in the case of the certain size of the bathtub and the person. When the bathing time is 30min ,the temperature of the hot water added in is 322.71K , the water   4 3 inflow per unit time is , the variance of the finial temperature of the water is 1.2 10 m  2 0.05513K and the difference between finial temperature and initial temperature is 0.125K , 3 the water wasted is 0.23m .

Thirdly, we study how would our model’s results change with the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub(Table 6,7,8 ,Figure 13,14,16), the motions made by the person(Figure 17,18) and the addition of the bubble additive initially(Table 9 Figure 19). When the shape of the tub change, in30min washing time the temperature of the hot water added in is324.03K , the water inflow per unit time is   4 3 (Table 5 Figure 12).When the volume of the tub is getter larger, the temperature 1.5 10 m of the hot water added increases and the water inflow per unit time is the same trend(Figure 7,8,9,10).

Finally, we provide a one-page non-technical explanation for users of the bathtub to explain the strategy.

optimization model, Genetic Algorithm

1 Introduction

1.1 Background

The bathtub, which is a simple water containment vessel and uses ceramic or other adiabatic material is often used in our daily life. Taking people’s comfort into consideration, the bathtub is designed as a container with a water inlet and water outlet, and when the tub reaches its capacity, excess water escapes through the overflow drain.

Aimed to get relaxed and cleansed, filling the bathtub with hot water before bathing is what we always do. With the time goes by, the temperature of the water will gradually drop. In order to maintain the suitable temperature, adding a constant trickle of hot water from the faucet to reheat the bathing water is necessary.

To have a comfortable hot bath is important for us to relax ourselves. However, there was no research on the model that can predict the temperature change of the water in the bathtub and guide people how to adjust, thus, our task is to build a model to provide a method for people to adjust the temperature of the water.

1.2 Our work

Our work begins with a heat transfer model. In this model, the heat conduction equation which uses the Fourier’s law and the energy conservation law to describe the change of temperature of the water in the bathtub is established. Firstly, we only consider the circumstance that the bathtub whose shape is cuboid is filled with water and without people in it. Besides, we put a person into the model and adds a boundary condition to the heat conduction equation to get the final heat transfer model.

Based on this, we set targets keep the temperature even in the bathtub and as close as possible to the initial temperature while wasting as little as possible of the water when taking a bath to optimize the heat transfer model.

Since our task is to provide people with the strategy to put the water into the bathtub, to test the model applicability in our daily life, we change the characteristic of the bathtub, the characteristic of the person in the bathtub and add the bubble additive to find how would the result change of the multi-objective optimization model.

In this paper, the finite element analysis and ANSYS are applied to solve a four- dimensional differential heat conduction equation to get the temperature distribution of the water in the bathtub.

2 Problem restatement

The problems that we need to solve in this paper are:

 Develop a model of the temperature of the bathtub water in space and time to determine the best strategy the person in the bathtub can adopt to keep the temperature even throughout the bathtub and as close as possible to the initial temperature without wasting too much water.

 Taking the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub, the motions made by the person into consideration, to what extent does your strategy depend on these elements by using your model you build.

 If a bubble additive is used initially, how would this affect the model’s results?

3 Terminology

3.1 Terms

 Heat transfer: the phenomena that energy transfers from a hotter object to the cooler object or heat migrates from the hotter part of the object to the cooler part of the object in the case of no work. It includes three mechanisms, which are thermal conduction, thermal radiation and thermal convection.

 Thermal conduction: the heat transfer phenomena when there is no macroscopic motion within the medium, which can occur in solids, liquids and gases.

3.2 Symbols

Symbols

Descriptions

the temperature of the object in position    x y z and at timet , , T x y z t , , ,

the heat that add to the bathtub per unit time per unit volume of heat   F x y z t , , , source the region surrounded by the closed surface whose boundaries are the  surface of the water and the bathtub

 the region of the heat source 1

V the volume of the water added in per unit time p

cT the temperature of the outlet of the water

rT the temperature of the inlet of the water

the closed surface whose boundaries are the surface of the water and  the bathtub the surface that the water contact with air, the water contact with the     i i 1,2,3 bathtub and the water contact with the person

V the volume of the water in the bathtub

T the initial water temperature that is suitable for people 0

4 General Assumptions

 The initial temperature of the water of each point in the bathtub is the same.

 The room is big enough thus the temperature of the room is constant and don’t change over time and space.

 The wall of the bathtub is insulated, thus the heat transfer between it and water is ignored; because most of the bathtubs’ material is ceramic, therefore, the heat preservation is better.

 Viewing the hot water injection point at the water surface as a heat source, because the water added in is trickle and can’t influence the water in the bathtub.

 Regardless of the heat convection, only considering thermal conduction when hot water is added to the bathtub. Because the water we add in is a trickle, the flow of it can be ignored.

 Regardless of the heat dissipation in the process of the hot water flow into the bathtub, because the time that hot water flow into the bathtub is short.

5 The Heat Transfer Model

In this section, we build a system with bathtub, the outlet of the water, the inlet of the water, the temperature and the velocity of the hot water in it at first. Then we build the basic model which includes heat conduction equation to describe the temperature distribution of the water in the bathtub. At this part, we have two boundaries (the boundary that the surface water contact with air and the boundary that the bottom and side face of the water that contact with bathtub), so we get two boundary conditions. Based on this, we add a person into the system, and when the person is taking the shower, there is heat exchange between them. We can view the person as another medium and add another boundary condition to the heat conduction equation.

To solve the heat conduction equation which is a four-dimensional differential equation, we adopt the finite element analysis and use the ANSYS to find the temperature distribution at the end.

5.1 Local Assumption

 Function T x y z t has the second continuous partial derivatives for all independent   , , , variables (the function T x y z t shows the temperature of object in position x y z and at    , , , , , time t ).

 The water in the bathtub is isotropic and homogeneous; because the water difference has little difference, we can view the density of water is the same in every direction.

 The person added into the bathtub can be viewed as two cuboid spliced together, because in general, the person’s body is homogeneous.

5.2 Basic model

To make the problem simple, we set bathtub of a cuboid shape and only fill the water into the bathtub at first. Besides, there is no people in it to build the basic model.

The bathtub we use in this model is showed in Figure 1:

To make the research of the problem easy, we build a three-dimensional coordinate system whose origin is the hot water injection point at the water surface, x-axis is parallel to the long side of the cuboid, y-axis is parallel to the short side of the cuboid and z-axis forms a right-handed coordinate system with x, y axis.

 The Fourier's law

The Fourier's law describes that the heat flow through an infinitesimal area along the surface normal direction in an infinitesimal period is proportional to the directional derivative of temperature along the surface normal direction:

 (1) T x y z t ( , , , )  dQ dSdt  n

Where:

T x y z t describes the temperature of the object in position  x y z and at timet ;    , , , , ,

is the thermal conductivity ;

dQ is the heat flow through an infinitesimal area along the surface normal direction in an infinitesimal period;

 T is the directional derivative of temperature along the surface normal direction; n

dS is the infinitesimal area and dt is the infinitesimal period.

 The heat conduction equation

For heat transfer in the water with a heat source, the energy Conservation Law with the Fourier’s law (Equation (1)) is as bellow:

                T T T T t           2 c dxdydzdt H 0                  t x x y y z z       t   1    t t         2 2 H F x y z t dxdydzdt , , , F x y z t dxdydzdt , , , (2)  1 2 t t 1 1   1 2

Where:

 T is the rate of change of temperature at a point over time; t   T x y z t describes the temperature of the object in position  x y z and at time t ; , , ,  , , is the thermal conductivity;

c is the specific heat capacity of water and is the density of water;

F x y z t is the heat that heat source releases per unit time per unit volume;   , , , 1 x y z t is the heat that water outflow releases per unit time per unit volume;   F , , , 2  is the region of the heat source flowing in per unit time; 1  is the region of the water flowing out the bathtub per unit time; 2  is the region surrounded by the closed surface whose boundaries are the surface of the water and the bathtub.

As the bathtub is full of water initially, the water inflow is equal to the water outflow, we can get:

t t t t         2 2 2 2 FV dt F V dt ( F F V dt ) FV dt 1 p 2 p 1 2 p p (3) t t t t 1 1 1 1

Where:

F x y z t is the heat that add to the bathtub per unit time per unit volume of heat   , , , source.

For the temperature of the hot water added in is constant, thereby the value of the   F x y z t , , , is constant, we can put F x y z t outside of the integral sign. So we get:   , , ,

                 T T T T t           2 c dxdydz FV dt 0           p        t x x y y z z         t     1  (3) Where:

V is the volume of the water added in per unit time. p

For the value of the variables 1t and 2t is arbitrary, and for any time interval, the equation (3) is tenable. Thus, we can get:

               T T T T           c dxdydz FV 0         p        t x  x  y y z  z       (4) Put forward the integral sign:

  FV              T T T T  p          c dxdydz 0                t V x  x  y y z  z        (5)

Where:

Vis the volume of the water in the bathtub.

F is the heat that the heat source releases per unit time per unit volume and can be calculated in the equation shown bellow:

     (6) F c T T r c Where:

T is the temperature of the inlet of water； r T is the temperature of the outlet of the water. c

Eventually, the heat conduction equation we get is；      T T V      2 2 2 T T T T r c p       (7)      2 2 2 t V c x y z   

 Boundary conditions

We divide the closed surface whose boundaries are the surface of the water and the  : bathtub into two part , 1 2  (8) 1 2 Where:

is the surface that the water contact with air; 1 is the surface that the water contact with bathtub. 2 : Then we get the boundary conditions for surface , 1 2  T         T T , x y z , , 1 1 1 1  n 1 (9)  T         T T , x y z , , 2 2 2 2  n 2 (10) Where:

is the thermal conductivity among water;

is the heat transfer coefficient between water and air; 1 is the heat transfer coefficient between water and bathtub; 2 1T is the temperature of the air and 2T is the temperature of the bathtub;

T is the temperature of the surface of the water;

n n are the normal vectors for the upper surface of the water the faces that , 1 2 water contact with bathtub;

 T i    are the directional derivative of temperature along the upper surface 1,2  n i of the water the faces that the water contact with bathtub.

While, as the assumptions we propose above, the wall of the bathtub is insulated, thus the directional derivative of temperature along the normal direction of the wall of bathtub is zero, so the equation (9) can be changed to:

(11)  T     0, x y z , , 2  n 2

 Initial condition

t , the value of 0 Besides, we provide the initial condition that at the initial time temperature in each point of bathtub is the initial temperature of the water T in bathtub 0 which is suitable for people:

(12)    T x y z , , ,0 T 0

Where:

T is the initial water temperature that is suitable for people; 0   is the water temperature in position  x y z at the initial time. T x y z , , ,0 , ,

 The final equations

Adding the initial condition and the boundary condition to the heat conduction equation, we get the heat transfer model eventually. The final equations are shown bellow；

        2 2 2 T T T T        f , x y z , ,         2 2 2 t c x y z        T T V  r c p  f  V s        T x y z , , ,0 T , x y z , ,  0   T          T T , x y z , , （13） 1 1 1 1   n 1  T      0, x y z , ,  2 n  2

Where:

 T is the rate of change of temperature at a point over time; t T x y z t describes the temperature of the object in position  x y z and at time t ;    , , , , , is the thermal conductivity ;

c is the specific heat capacity of water and is the density of water;

Vis the volume of the water in the bathtub;

V is the volume of the water added in per unit time; p

is the heat transfer coefficient between water and air; 1 T is the initial water temperature that is suitable for people; 0 n n are the normal vectors for the upper surface of the water, the faces that the , 1 2 water contact with bathtub;

1T is the temperature of the air.

5.3 Take people into consideration

Further, we take a person into consideration. The person will have the temperature exchange with the water while having the shower. To research the influence of the person to the temperature distribution of the water in the bathtub, we view the person’s shape as two cuboid spliced together which is shown in Figure 3, the size of the cuboid bellow is   and the size of the cuboid above is 0.5   1.1 m 0.45 m 0.25 m m 0.3 m 0.45 m

The addition of the person add one boundary condition to the heat conduction equation, which is:

 (14) T      T T 3 3 3  n 3 Where:

3T is the temperature of the person;

is the heat transfer coefficient between water and the person; 3 2n is the normal vector of the surface of the person.

Adding the boundary condition to equation (12), we get:

        2 2 2 T T T T        f , x y z , ,         2 2 2 t c x y z        T T V  r c p  f  V         T x y z , , ,0 T , x y z , ,  0  T          T T , x y z , , 1 1 1 1  n  1  T      0, x y z , , 2 n  2  (15)  T          T T , x y z , , 3 3 3 3   n 3 Where:

 T is the rate of change of temperature at a point over time; t T x y z t describes the temperature of the object in position  x y z and at time t ;    , , , , , is the thermal conductivity ;

c is the specific heat capacity of water and is the density of water;

Vis the volume of the water in the bathtub;

  is the heat transfer coefficient between water and air and between   i i 1, 3 water and the person;

T is the initial water temperature that is suitable for people; 0 1n , 2n , 3n are the normal vectors for the upper surface of the water, the faces that the water contact with bathtub and the surface of the person;

  is the temperature of the air and temperature of the person. iT i  1,3

5.4 ANSYS simulation

Given a certain circumstance, in which the bathing time is30min , the size of the bathtub   is 1.5 0.5 0.7 and the values of other variables we set are shown in the Table 1.

1 c f 1T 0T Parameter  15 / ( J Ksm ) 4200 / ( J kg K ) 100J 308K 321K Value    3T Parameter 3 0.64 / ( J Ksm ) 200 / ( J Ksm ) 320K 3 Value kg m 1000 /

we use the heat transfer model and apply ANSYS to simulate the temperature distribution of the water with a person in the bathtub. The process of the temperature distribution for 2-D dimensional is shown in Figure 3(the 2-D dimensional plane we choose in the bathtub is parallel to the horizontal plane) The temperature distribution of the water in the bathtub can be seen in Figure 5:

6 Multi-objective optimization model

In this section, with the targets of wasting as little water as possible, keeping the temperature even and as close as possible to the initial temperature, we apply a multi- objective optimization to the heat transfer model to get the best strategy that can be applied for people in our daily life.

6.1 The build of the multi-objective optimization model

To make the temperature in the bathtub even and as close as possible to the initial temperature, we need to calculate the finial average temperature of the water after taking the shower, which is:

1   T T x y z t dxdydz ( , , , ) z z V (16)  Where:

zt is the time that the person finish the bathing;

zT is the finial average temperature of the water after taking the shower;

To make the temperature as evenly as possible. The first objective function is:

1       2 2 min ( T x y z t , , , T ) dxdydz z z V (17)   Where:

is the variance of the finial temperature of the water. 2

To make the temperature of the water as close as possible to the initial temperature. The second objective function is:

(18)    min T T T z z 0 Where:

is the temperature difference between final average temperature and initial zT temperature of the water in bathtub.

As the bathtub is filled with water at the initial time, the water inflow is equal to the water outflow. We can minimize the water inflow to get the minimum wasting water. The third objective function is:

V min p (19) The range of the temperature we added in is from 317k to 323k, and the range of the volume  of the hot water added in per unit time is from 0 to  , which are the restriction 4 3 2 10 m conditions:

   317 K T 323 K r st . 0    4 3 V 2 10 m  p (20) Eventually, we get the finial multi-objective optimization model, which is:

find T V r p 1       2 2 min ( T x y z t , , , T ) dxdydz z z V      min T T T z z 0 min V p    317 K T 323 K r (21) st . 0    4 3 V 2 10 m  p

Where:

zT is the finial average temperature of the water after taking the shower;

zt is the time that the person finish the bathing;

is the variance of the finial temperature of the water; 2   is the temperature of the water in positon  x y z and at time t ; T x y z t , , , z , , is the temperature difference between final average temperature and initial zT temperature of the water in bathtub;

T is the initial water temperature that is suitable for people; 0 T is the temperature of the inlet of water； r T is the temperature of the outlet of the water; c

V is the volume of the water added in per unit time. p To solve the multi-objective optimization model, we set different weight to the variance of the final temperature and the temperature difference between final average temperature and initial temperature, and change the multi-objective to the single objective optimization model:

find T V r p       2 min T V 1 2 z 3 p    317 K T 323 K r     4 3 0 V 2 10 m  p st .       1  (22) 1 2 3     ( i 1,2,3) 0  i

Where:

V is the volume of the water added in per unit time; p

T is the temperature of the inlet of water； r is the variance of the finial temperature of the water; 2

is the temperature difference between final average temperature and initial zT temperature of the water in bathtub;

is the weight of the the variance of the finial temperature of the water; 1 is the weight of the temperature difference between final average temperature and 2 initial temperature of the water in bathtub;

is the weight of the water wasted per unit time. 3 Using this model, we can calculate the temperature and the velocity of the hot water we need to add in with the certain targets, thereby, a strategy to add water can be provided for people.

6.2 The strategy to add water

To solve the multi-objective optimization model in order to propose the strategy to add water, we use the Genetic Algorithm and address the problem in four steps: (1) At first step, we select countless values from the range of the temperature and the range of the volume of the hot water added in per unit time we set in equation (20) (2) At second step, using the objective function       to filter the 2 min T V 1 2 z 3 p selected values, and then get the values that satisfied the objective function (3) At third step, based on the values we picked out, using the objective function to filter. (4) At fourth step, repeat the third step until find out the best strategy.

We set the values of the parameters in the Genetic Algorithm, which is shown in Table 2:

Evolutionary Crossover Mutation Sample size Parameter times probability probability 8 0.4 0.2 41 Value    Parameter 1 2 3 0.6 0.4 0 Value Using Matlab to programme and call the ANSYS to calculate the best strategy to add water. The values of the variables in the model shown in the Table 3 and the strategy how to add the water is shown in Table 4.

1 c 1T 0T Size of the Parameter bathtub    15 / ( J Ksm ) 4200 / ( J kg K ) 308K 321K 1.5 0.5 0.7 Value    3T Shower time Parameter 3 0.64 / ( J Ksm ) 200 / ( J Ksm ) 320K 3 Value 30min kg m 1000 /

V  rT V zT  Variable 2 p  0.05513 322.71K  0.23m  0.125K Value 3 4 3 1.2 10 m Where:

V is the water we waste.

We get the final temperature distribution after shower of the best strategy in Figure 6.

7 Sensitivity Analysis

To provide people with strategy to add water better. In this part, we find the influence of the shape and volume of the tub, the shape/volume/temperature of the person taking a bathing and the bubble additive to the multi-objective optimization model.

First step, we research the influence of the characteristic of the tub. We change the size of the length, width and height of the tub of a cuboid shape respectively to the multi-objective optimization and we design the shape of the bathtub closer to life to find the better strategy to add water.

Next step, we research the influence of the characteristic of the person. We change the size of the person and the temperature to find the results of the multi-objective optimization model. Besides, we take the motion of the person in the water into consideration. The movement of the person leads to the movement of the water, thus we can think that the forced convection happens to the water which makes the heat transfer coefficient between water and air and between water and the person get changed. At the end, we add the bubble bath 1, to additive initially, which only change the heat transfer coefficient between water and air find how the strategy changes.

Lastly, we research the influence of the addition of the bubble additive which changes the heat transfer coefficient between water and air. Changing the heat transfer coefficient between water and air to get the best strategy to add water

7.1 Change the characteristic of the bathtub

 Change the area of the bathtub’s upper surface We change the area of the bathtub’s upper surface to change the volume of the bathtub, and get the change of optimal temperature of the water added in and the optimal water inflow per unit time with the area, the result is shown on Figure 7,8

per unit time with area of the water added in with the area

Where:

x-axis in Figure 7,8 represents the change of the area;

y-axis in Figure 7 represents the change of the optimal temperature of the water added in;

y-axis in Figure 8 represents the change of the optimal volume of the water inflow per unit time.

The increase of the upper surface’s area causes the increase of the heat exchange ( between water and area), moreover the heat added in increases. We can find both optimal temperature and optimal water inflow per unit time are increasing with the increase of the area.  Change the height of the bathtub We change the height of the bathtub to change the volume of the bathtub, and get the change of optimal temperature of the water added in and the optimal water inflow per unit time with the height, the result is shown on Figure 9,10.

inflow per unit time with the height with the height

Where:

x-axis in Figure 9,10  represents the change of the height;

y-axis in Figure 9 represents the change of the optimal temperature of the water added in;

y-axis in Figure 10 represents the change of the optimal water inflow per unit time.

The increase of the height only causes the increase of the volume of the bathtub, while the area of the water contact with air is not influenced, furthermore, the heat loss isn’t influenced. Thus the curves in the Figure 9,10 are relatively flat.  Change the shape of the bathtub Based on the multi-objective optimization model, and keeping the volume of the bathtub invariant, we design the shape of the bathtub closer to life which is presented in Figure 11 to find the best strategy to add water(Table 5 ) and the final temperature distribution(Figure 12)

V  rT V zT  Variable 2 p  0.0676 324.03K  0.27m  0.1503K Value 3 4 3 1.5 10 m the shape of the bathtub

From the figures above, we can find that the temperature of the hot water added in is higher, and the water inflow per unit time is larger than the bathtub of the cuboid shape. With the same volume the area of the upper surface of the bathtub is bigger and the heat loss increases, thus more heat needs to be added in.

7.2 Change the characteristic of the person

 Change the volume of the person We change the volume of the person which influence the boundary condition of the person and get the change of optimal temperature of the water added in and the optimal water inflow per unit time with the volume of the person, the result is shown on Figure 13,14.

temperature with the volume of the person per unit time with the volume of the person

Where:

x-axis in Figure 13,14 represents the change of the volume of the person;

y-axis in Figure 13 represents the change of the optimal temperature of the water added in;

y-axis in Figure 14 represents the change of the optimal water inflow per unit time.

From the figures, we find that the strategy to add water change a little with the increase of the volume of the person. For the increase of the volume of the person resulting in the surface people contact with water. Furthermore, the heat exchange between people and water get a little increase, so the heat added in has slight increase.  Change the shape of the person Keeping the volume of the person invariant and we change the shape of the person into the two cylinders spliced together, which is shown in Figure 15, to find the best strategy to add water(Table 6) and the final temperature distribution(Figure 16).

V  rT V zT  Variable 2 p 0.0266  323.135K  0.358m  0.158K Value 3 4 3 1.99 10 m

changing the shape of the person From the result, we can find that when the shape of the person is close to reality, the difference between the final temperature and the initial temperature, the wasting water and the water inflow per unit time get some increase. According to the mathematical knowledge, in the same volume, the cylinder’s surface area is bigger than the cuboid’s surface area thus the area the person contact with water increases which leads to more heat exchange. Hence, more heat is needed.

Change the temperature of the person  The range of the temperature change of the person is relatively small, thus we only study the strategy to add water when the temperature are 319.5K and 320.5K which is shown in Table 7,8.

V  rT V zT  Variable 2 p  0.0487 319.5K  0.361m  0.1176K Value 3 4 3 2.01 10 m

V  rT V zT  Variable 2 p  0.0413 320.5K  0.342m  0.1215K Value 3 4 3 1.90 10 m Although the temperature of the surface of the body maybe change for some reasons, for example, getting ill, the range is relatively small. And the temperature of body is close to the temperature of water, so the heat exchange is small. Thus, the change of the temperature of the person has little influence on the strategy to add water.

7.3 Add the motion of the person in the bathtub

Considering the actual situation, we add the motion of the person in the bathtub to obtain the strategy to add water. The motion of the person only change the heat transfer coefficient 1 and the heat transfer coefficient between water and the person and between water and air 3 other variables are the same as the values of the variables we choose in Table 3.

We use percentage to measure the intensity of the motion, and obtain the change of the optimal temperature of the water added in and the optimal water inflow per unit time with the percentage, the result is shown on Figure 17,18.

with the percentage inflow per unit time with the percentage

Where:

x-axis in Figure 17,18 represents the change of the percentage which measures the intensity of the motion;

y-axis in Figure 17 represents the change of the optimal temperature of the water added in;

y-axis in Figure 18 represents the change of the optimal water inflow per unit time.

We can find that the optimal temperature of the water added in and the optimal water inflow per unit time are get larger with the increase of the intensity of the motion. Because the intenser the movement is, the more heat dissipates. If we want to keep the temperature even and as close as possible to the initial temperature, more heat will be added in the bathtub.

7.4 Add the bubble additive to the bathwater

The addition of the bubble additive only change the heat transfer coefficient between 1, the values of the other variables in the multi-objective optimization we water and air 1as 11 / ( choose are the same as what we choose in Table 3. We set the value of Ksm ,and J ) obtain the strategy to add water (Table 9). At the same time, the final temperature distribution is presented in Figure 19.

V  rT V zT  Variable 2 p  0.0189 321.02K  0.286m  0.1144K Value 3 4 3 1.59 10 m We come to the conclusion that compared with the circumstance without the bubble additive in the water, the variance of the finial temperature of the water and the water inflow per unit time increase, while the temperature of the inlet of water and the temperature difference between final average temperature and initial temperature of the water in bathtub decrease.

8 Strengths and Weaknesses

8.1 Strengths

(1) The main strength of our model is close to the reality. The heat exchange between people and water and between water and air is considered when research the temperature distribution in the bathtub. (2) To test the application of the model in our daily life, we take the characteristic of the person and the motions of the person into discussion. (3) Besides, considering the comfort of the person, we also change the cross section of the bathtub to isosceles trapezoid and change the sloped angle of the trapezoid to discuss the temperature distribution.

8.2 Weaknesses

(1) The calculation of our model is complex, we need to solve a four-dimensional differential equation. (2) The bathroom of small size whose room temperature is changed is not taken into consideration.

(3) When we change the shape of the person in the bathtub in the sensitivity analysis of our model, we only consider the change based on the shape of a cuboid. But other changes such as cylinder is not taken into consideration.

9 Explanation for users

The bathtub we use in our daily life is a simple water containment vessel, in order to take a shower comfortably, the person needs to add a constant trickle of the hot water from the faucet. Here, we give the explanation of the strategy to add water researched in this paper.

If the bathtub you use is a little larger than the normal size, you should increase the temperature of the hot water added in by14.28K per unit cubic meter. You’d batter to use the bathtub whose upper surface is not very big. Besides, if you are fat, maybe you should increase the temperature of the hot water a little (about 0.5K ). If the temperature of your body surface is a little higher, to decrease the temperature of the hot water. Some children like playing while taking the shower, you need to increase the temperature of the water according to the intensity of his movement; if he is crazy, you need to increase the temperature by 2K . Bubble additive is our preference; don’t forget to decrease the temperature if you want to have a comfortable washing.

While, getting an evenly maintained temperature throughout the bath water is difficult. We have the reasons as follow: (1) Without hot water added in, the surface of the water contact with air will have the heat loss making the temperature of the upper layer and lower layer different. Besides, the motion of the person is complex, which leads to the complexity of the heat loss (2) With hot water added in, the temperature of the inlet is different with the temperature of the outlet. When the volume of the bathtub gets bigger, with the restriction of the water inflow(the maximum flow of the faucet is definite), the heat that the water in the outlet absorbs is litter which makes the temperature gradient from inlet to the outlet becomes large
