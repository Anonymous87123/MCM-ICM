# P-A-2011-12149-cb2b7105

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Designing a Halfpipe for Advanced Snurfers

<!-- b000002 | title | pages [1] -->
Team Control # 12149

<!-- b000003 | front_matter | pages [1] -->
February 14, 2011

<!-- b000004 | heading | pages [1] -->
Abstract

<!-- b000005 | prose | pages [1] -->
The shape of a snowboarding halfpipe can be designed to maximize the vertical air a professional snowboarder will achieve; however, a practical course will take into account factors such as the number of cycles a snowboarder can make side to side as he descends the mountain, and the shape that yields the best launch for stunts.

<!-- b000006 | prose | pages [1] -->
As a snowboarder descends a halfpipe the forces acting on him are dependent on the shape of the course. We will use Newton’s Second Law of Motion to sum the forces in each direction. Then we used a Runga-Kutta method computer simulation to determine the acceleration of the snowboarder down the course. We tested three diﬀerent functions that describe the shape of the half pipe, with three varying slopes for each. Using a computer simulation and physical testing the velocity of the snowboarder can be analyzed at the edge of the half pipe. The shapes that yield the largest vertical air and the most practical course will then be chosen as the best design.

<!-- b000007 | prose | pages [1] -->
The forces taken into consideration in these models include: gravity, centrifugal, frictional, air resistance, and a constant force applied in the direction of travel that mimics the force from a professional snowboarder pumping his legs. These models do not take into account the force a professional snowboarder’s stylistic force would use to guide his path along the halfpipe.

<!-- b000008 | prose | pages [1] -->
After running our three models we determined that out of the various shapes tested the best vertical height was optimized at a mountain slope of 45 degrees with a half pipe shape of the parabola z(y) = .07y2 −7 The best practical model was found to be the same parabola at a mountain slope of 25 degrees. The Runge Kutta method approximation had an error of 0.1 %. Our best model is the comprehensive three dimensional force because it most realistically describes a snowboarder on a halfpipe.

<!-- b000009 | furniture | pages [2] -->
Team Control Number 12149

<!-- b000010 | furniture | pages [2] -->
Page 1 of 23

<!-- b000011 | heading | pages [2] -->
1 Introduction

<!-- b000012 | prose | pages [2] -->
Developed in the 1970’s, snowboarding has come a long way from the original snurfer (snow-surfer) which was an attempt by Shermann Poppen to bring surﬁng to the Rocky Mountains. Since then snowboarding has taken oﬀwith perfecting ramps and slopes to enable a variety of tricks and stunts. Some of these stunts require a simple slope, others a rail, and for this problem we will look speciﬁcally at the half-pipe in order to optimize vertical air which can be deﬁned as the distance a skilled snowboarder can obtain by being launched oﬀthe edge of the halfpipe.

<!-- b000013 | heading | pages [2] -->
1.1 The Problem

<!-- b000014 | prose | pages [2] -->
A Basic Halfpipe

<!-- b000015 | prose | pages [2] -->
A basic halfpipe consists of two concave ramps separated by a distance which totals to the width of the half pipe(ﬁgure 10). The vertical side of the ramp, or the edge, is called a vertical, the curved part of the vertical is called the transition, and the distance between the two ramps is called the ﬂat.

<!-- b000016 | prose | pages [2] -->
In a basic halfpipe the vertical and transition allow for back and forth motion using the force of gravity to give the snowboarder a velocity. A snowboarder uses the ﬂat to regain balance as well as a time to pump. Pumping adds work to the system and gives the boarder a greater velocity to make it up the opposite vertical and obtain a higher vertical air. Because the ﬂat optimizes the angle that the force exerts on the snowboarder pumping happens primarily on the ﬂat(see equation 6).

<!-- b000017 | prose | pages [2] -->
A Snowboarding Halfpipe

<!-- b000018 | prose | pages [2] -->
A snowboarding halfpipe is a basic halfpipe that is built onto a hill (ﬁgure 9). The slope of the hill gives a new form of energy that can be converted to velocity and used to maximize vertical air. The plane of the transition is oriented downhill at a slight grade to allow riders to use gravity in two directions to create a velocity both back and forth and down the slope to develop the optimal speed for stunts that require vertical air.

<!-- b000019 | prose | pages [2] -->
The character of the half pipe depends mostly on the relationship between the transition angle and the height of each vertical. The higher the vertical the more diﬃcult it is to land while a narrow stretch between the two verticals provides less time to recover as well as less opportunity to pump. So what is the best shape of a half pipe to optimize a skilled snowboarder’s vertical air? And what kind of options does the snowboarder have for a variety of stunts? And what changes could be made to develop a practical course?

<!-- b000020 | prose | pages [2] -->
Our Approach

<!-- b000021 | prose | pages [2, 3] -->
In order to ﬁnd a snowboarder’s optimized vertical air we used both conservation of energy and Newton’s 2nd Law to account for the various forces acting on a snowboarder while traveling down the half-pipe. We constructed models based on the law of conservation of energy and Newton’s Laws. Using a function z(y) for the shape of the halfpipe we were able to set up a model that allows a function to be easily altered and evaluated for any shape.

<!-- b000022 | furniture | pages [3] -->
Team Control Number 12149

<!-- b000023 | furniture | pages [3] -->
Page 2 of 23

<!-- b000025 | prose | pages [3] -->
• Conservation of Energy Model: The energy model depends only on the change in height and gravity (ﬁg 1). Work can be added to this model in the form of a snowboarder pumping over the ﬂat. This model gives an idea of how a more complex model might look.

<!-- b000026 | prose | pages [3] -->
• Two Dimensional Force Model: We used Newton’s 2nd Law in 2D to minimize the energy lost through friction and air resistance by creating a system of ordinary diﬀerential equations that described the forces acting on the snowboarder (ﬁgure 2).

<!-- b000027 | prose | pages [3] -->
We evaluated a series of equations for the curve of the halfpipe, and evaluated the numerical results to determine which curve gave the best vertical air. This model acts on the assumption that the snowboarder is in a basic halfpipe which does not include the slope of the mountain.

<!-- b000028 | prose | pages [3] -->
• Comprehensive Three Dimensional Force Model: Our ﬁnal and most compre- hensive model takes into account both the potential energy converted from the descent down the slope as well as friction from both air and snow. In order to model the loss in potential energy due to the decreasing height we developed a model that is based on not only the pitch of the two adjacent sides of the half-pipe but also the slope of the hill that the half-pipe is on. We continued using Newton’s 2nd Law of motion as we did for the two dimensional model to determine the maximum height that can be reached by a snowboarder under the inﬂuence of gravity, pumping, air resistance, and the friction between the snow and the board.

<!-- b000029 | heading | pages [3] -->
2 Models

<!-- b000030 | heading | pages [3] -->
2.1 Conservation of Energy

<!-- b000031 | prose | pages [3] -->
How It Works

<!-- b000032 | prose | pages [3] -->
The conservation of energy model is our most intuitive analysis of the snowboarders speed. Looking at the conversion of potential energy to a new potential energy (through a change in height) we can determine analytically the kinetic energy used to launch a snowboarder oﬀ of the verticals and gain as much vertical air as possible (ﬁgure 1).

<!-- b000033 | furniture | pages [4] -->
Team Control Number 12149

<!-- b000034 | furniture | pages [4] -->
Page 3 of 23

<!-- b000035 | caption | pages [4] -->
Figure 1: Energy Model Diagram

<!-- b000036 | prose | pages [4] -->
KEi + PEi = KEf + PEf (1)

<!-- b000037 | prose | pages [4] -->
Under the following conditions:

<!-- b000038 | prose | pages [4] -->
vi = 0 (2)

<!-- b000039 | prose | pages [4] -->
hi > hf (3)

<!-- b000040 | prose | pages [4] -->
The conservation of energy results in the following equation.

<!-- b000041 | prose | pages [4] -->
p (2g(hi −hf)) v = (4)

<!-- b000042 | prose | pages [4] -->
Without adding any work the snowboarder will never go beyond the original height. In order to see the importance of pumping we added work to the system and the equation of velocity is changed by a factor of work (equation 6).

<!-- b000043 | prose | pages [4] -->
W = Fapplied • d = Fappliedd cos σ (5)

<!-- b000044 | prose | pages [4] -->
F(applied) is the force applied by the snowboarder, d is the distance between the two verticals and σ is the angle in which the force is applied.

<!-- b000045 | prose | pages [4] -->
p (2g(hi −hf) + 2W) v = (6)

<!-- b000046 | prose | pages [4, 5] -->
A higher velocity means there is a higher vertical air. However, the angle of take oﬀmust be taken into account as well. Consider θ which is the angle between the horizontal axis and the direction of the velocity of the snowboarder (ﬁgure 1). When θ = π 2 then our velocity is entirely in the z direction and our vertical air is maximized. Conversely we can also see that when θ = 0 our velocity is entirely in the x direction and we have no vertical air.

<!-- b000047 | furniture | pages [5] -->
Team Control Number 12149

<!-- b000048 | furniture | pages [5] -->
Page 4 of 23

<!-- b000050 | prose | pages [5] -->
Consequences

<!-- b000051 | prose | pages [5] -->
The information provided by this analysis gives an intuitive look into what a snow- boarder’s motion would be neglecting all forms of friction in a two dimensional plane, with the option to add work. A closer look at the direction of the resulting velocity shows the importance of the takeoﬀangle. By choosing the angle of take oﬀ(angle between slope and horizon) to be as close as possible to 90 degrees a snowboarder can maximize vertical air.

<!-- b000052 | heading | pages [5] -->
Strengths

<!-- b000053 | prose | pages [5] -->
• This model gives information for the height diﬀerence necessary to give a snowboarder vertical air using only potential energy.

<!-- b000054 | prose | pages [5] -->
• Simulations are quick, and it is easy to alter the height diﬀerence of the halfpipe verticals.

<!-- b000055 | prose | pages [5] -->
• This model allows work to be added to the system.

<!-- b000056 | prose | pages [5] -->
• The model only depends on the original and ﬁnals height which means any path could be taken.

<!-- b000057 | heading | pages [5] -->
Weaknesses

<!-- b000058 | prose | pages [5] -->
• This model does not provide a way to solve for an optimal angle of either the half-pipe or the hill.

<!-- b000059 | prose | pages [5] -->
• This model does not take into account any frictional forces.

<!-- b000060 | heading | pages [5] -->
2.2 Two Dimensional Force Model

<!-- b000061 | prose | pages [5] -->
How It Works

<!-- b000062 | prose | pages [5] -->
In order to model a snowboarder’s path down a two dimensional movement we used a set of linear ordinary diﬀerential equations for the forces acting on the snowboarder in both z and y directions ( down and left to right). The gravitational, frictional and drag forces acting on the snowboarder are summed along the z and y axis (looking in the 3-D z-y plane).

<!-- b000063 | prose | pages [5] -->
1 2ρairacd(v2 x + v2 y) Fdrag = (7) m

<!-- b000064 | prose | pages [5, 6] -->
N = g cos(θ) −(v2 y + v2 z) (8) ρ Using Newton’s Second Law of Motion P F = m⃗a we can see that the force acting on the snowboarder in the y-axis is equal to mass times acceleration along the y-axis. Applying this to both the y and z axis yields two second order diﬀerential equations (equations 9 and 10).

<!-- b000065 | furniture | pages [6] -->
Team Control Number 12149

<!-- b000066 | furniture | pages [6] -->
Page 5 of 23

<!-- b000068 | prose | pages [6] -->
dvy dt = N sin θ −µN cos θ −Fdyz cos θ + ρ cos θ (9)

<!-- b000069 | prose | pages [6] -->
dvz dt = −g + N cos θ −µN sin θ + Fdyz sin θ −ρ sin θ (10)

<!-- b000070 | prose | pages [6] -->
These two second order diﬀerential equations can be broken down into four ﬁrst order dif- ferential equations. (Further derivation of these equations can be reviewed in the appendix).

<!-- b000071 | prose | pages [6] -->
Using a computer simulated Runga-Kutta method, the four diﬀerential equations are solved yielding the snowboarder’s path and velocity across the halfpipe. A force was added in the direction of travel that mimics the force of the snowboarder pumping his legs to add speed(equation 5).

<!-- b000072 | prose | pages [6] -->
Consequences

<!-- b000073 | prose | pages [6] -->
This model corrects for the drag force and frictional force acting on the snowboarder. These forces are dependent upon velocity across the halfpipe. This model shows how diﬀerent shapes aﬀect the amount of energy lost due to friction and drag. By adding the force of the snowboarder pumping his legs, the model shows the velocity in the z direction at the point the snowboarder leaves the halfpipe which is proportional to the vertical air the snowboarder achieves. With the added force being constant, and the dimensions similar, each shape can be analyzed side by side to determine the best cross-sectional shape for a halfpipe (ﬁgure 2).

<!-- b000074 | caption | pages [6] -->
Figure 2: Two dimensional Force Model

<!-- b000075 | prose | pages [6, 7] -->
St th • This method takes into account the frictional and drag forces that the ﬁrst model neglected.

<!-- b000076 | furniture | pages [7] -->
Team Control Number 12149

<!-- b000077 | furniture | pages [7] -->
Page 6 of 23

<!-- b000079 | prose | pages [7] -->
• Oﬀers a solution for optimizing the pitch of the halfpipe.

<!-- b000080 | prose | pages [7] -->
• Simulations are quick, and it is easy to alter the height of the verticals or the width of the halfpipe.

<!-- b000081 | prose | pages [7] -->
• The shape of the halfpipe can be changed into any function for z(y).

<!-- b000082 | heading | pages [7] -->
Weaknesses

<!-- b000083 | prose | pages [7] -->
• This model neglects the acceleration added from the halfpipe sloping down a hill.

<!-- b000084 | prose | pages [7] -->
• Only the z-y cross-sectional dimensions are optimized.

<!-- b000085 | heading | pages [7] -->
2.3 Comprehensive Three Dimensional Force Model

<!-- b000086 | prose | pages [7] -->
In order to model this problem in three dimensions we came up with a three dimensional force diagram. In this model we are taking into account the zx plane’s potential energy that is being converted into kinetic energy as the snowboarder descends the hill. For the sake of simplicity we shifted the axis used to deﬁne the zx plane so that the normal force is solely in the z direction (ﬁgure 3).

<!-- b000087 | caption | pages [7] -->
Figure 3: zx plane for 3D Force Model

<!-- b000088 | prose | pages [7, 8] -->
An important observation to take into account for this model is the fact that we redeﬁned the coordinate system; this means that the force of gravity used in the 2D model of the zy plane (ﬁgure 2) is now gravity multiplied by the cos(φ). Where φ is the angle of the halfpipe on the hill.

<!-- b000089 | furniture | pages [8] -->
Team Control Number 12149

<!-- b000090 | furniture | pages [8] -->
Page 7 of 23

<!-- b000092 | prose | pages [8] -->
dvx dt = g sin φma −g cos φµ −Fdx (11)

<!-- b000093 | prose | pages [8] -->
dvy dt = N sin θ −µN cos θ −Fdyz cos θ + ρ cos θ (12)

<!-- b000094 | prose | pages [8] -->
dvz dt = −g cos φ + N cos θ −µN sin θ + Fdyz sin θ −ρ sin θ (13)

<!-- b000095 | prose | pages [8] -->
Consequences

<!-- b000096 | prose | pages [8] -->
With the force caused by the ramp going down a slope added, this model allows the path and the velocity of the snowboarder side to side movement across the halfpipe to be evaluated as well as the velocity down the hill. This lets us see how the slope of the hill eﬀects the vertical distance above the halfepipe the snowboarder is able to achieve.

<!-- b000097 | prose | pages [8] -->
This model can be used to look at both variables; slope and the function of the cross- section, which allows us to choose the pair that yields the most desirable results.

<!-- b000098 | heading | pages [8] -->
Strengths

<!-- b000099 | prose | pages [8] -->
• This model takes into account the forces in all three directions by including the slope of the halfpipe down the hill.

<!-- b000100 | prose | pages [8] -->
• This model allows diﬀerent combinations of slope and cross-sectionals to be tested together.

<!-- b000101 | prose | pages [8] -->
• This model oﬀers a way to easily change the parameters of the system in question.

<!-- b000102 | heading | pages [8] -->
Weaknesses

<!-- b000103 | prose | pages [8] -->
• This model does not take into account the stylistic ways a snowboarder uses to slow himself down in the x direction.

<!-- b000104 | prose | pages [8] -->
• This model does not take into account how a professional snowboarder will guide his path down the halfpipe

<!-- b000105 | heading | pages [8] -->
2.4 Assumptions

<!-- b000106 | prose | pages [8] -->
• The snowboarder does not add force to the system causing a change in direction.

<!-- b000107 | prose | pages [8] -->
• The force added in the two-dimensional model to mimic the snowboarder pumping his legs to add speed was added by adding a single constant force in the direction of travel.

<!-- b000108 | prose | pages [8] -->
• In the three-dimensional model the added force is only taken into consideration in the z-y plane.

<!-- b000109 | furniture | pages [9] -->
Team Control Number 12149

<!-- b000110 | furniture | pages [9] -->
Page 8 of 23

<!-- b000111 | prose | pages [9] -->
• No projectile motion is modeled for after the snowboarder leaves the halfpipe.

<!-- b000112 | heading | pages [9] -->
3 Results

<!-- b000113 | prose | pages [9] -->
After evaluating each model we came to the conclusion that the best model is the three dimensional force model. It has the most broad spectra with the ability to easily change the slope of the mountain or the halfpipe verticals and still not lose the information needed to observe the snowboarder’s velocity in all directions. Both the conservation of energy model and the two dimensional force model are necessary for evaluating how the slope changes a snowboarder’s velocity, as well as demonstrating the importance of strategies such as pumping, that add work to the system.

<!-- b000114 | heading | pages [9] -->
3.1 Conservation of Energy Model Results

<!-- b000115 | prose | pages [9] -->
This was an analytical model so there is no data to graph. However, a clear understanding of the model gives an intuitive look into why we choose to use second order diﬀerential equations to model the more complex systems. The information taken from this model is that in order to maximize vertical air the take oﬀangle must be as close as possible to 90 degrees. Another less realistic suggestion to maximize velocity in the absence of work is to make one vertical shorter than the other in order to achieve vertical air from the left over converted potential energy (ﬁgure 1).

<!-- b000116 | heading | pages [9] -->
3.2 Two Dimensional Force Model Results

<!-- b000117 | prose | pages [9] -->
The two dimensional force model is used to evaluate the ﬁnal velocity of the snowboarder at the peak of the opposite vertical. By breaking the velocity into y and z components we were able to compare the ﬁnal z velocity of three diﬀerent functions.

<!-- b000118 | prose | pages [9] -->
Function Z Velocity (m/s) Y Velocity (m/s) Line Color Initial Position (m) Center Parabola 2 2.71546 1.357389 Green (-10,0) (0,-10) Circle 2.670921 0.139753 Black (-10,0) (0,-10) Parabola 1 3.54291 2.527488 Red (-10,0) (0,-7) Shape Name Formula z(y) = .07y2 −7 Parabola 1 Where the functions used are: z(y) = .1y2 −10 Parabola 2 p 100 −y2 Circle z(y) =

<!-- b000119 | prose | pages [9] -->
In order to be able to compare these three functions, all the functions should initially start at the same (z,y) and span the same y distance (width of the half pipe). The following graph is showing the motion of a snowboarder in the yz plane with friction and air resistance added.

<!-- b000120 | furniture | pages [10] -->
Team Control Number 12149

<!-- b000121 | furniture | pages [10] -->
Page 9 of 23

<!-- b000122 | caption | pages [10] -->
Figure 4: Dispacement in the YZ Plane

<!-- b000123 | prose | pages [10] -->
In order to evaluate the aﬀect of work done by the snowboarder a set value for the force added through work was added to the model. Because the snowboarder cannot reach a height greater than his original height using only potential energy he must use the pumping method to give him a greater velocity.This can be seen in the following graph of the snowboarder’s displacement.

<!-- b000124 | furniture | pages [11] -->
Team Control Number 12149

<!-- b000125 | furniture | pages [11] -->
Page 10 of 23

<!-- b000126 | caption | pages [11] -->
Figure 5: Dispacement in the YZ Plane Adding Work

<!-- b000127 | prose | pages [11] -->
By modeling this further into a projectile motion problem we can verify that the function yielding the greatest velocity in the z direction will give the greatest vertical air. So, by comparing and contrasting the three diﬀerent models we can extrapolate that:

<!-- b000128 | prose | pages [11] -->
• Parabola 1 is 23 percent better than parabola 2.

<!-- b000129 | prose | pages [11] -->
• Parabola 2 is 1.6 percent better than the circle.

<!-- b000130 | heading | pages [11] -->
3.3 Comprehensive Three Dimensional Force Model Results

<!-- b000131 | prose | pages [11] -->
The comprehensive three dimensional force model allows the displacement in the x, y and the z direction to be graphed in a three dimensional graph (ﬁgure 6).

<!-- b000132 | furniture | pages [12] -->
Team Control Number 12149

<!-- b000133 | furniture | pages [12] -->
Page 11 of 23

<!-- b000134 | caption | pages [12] -->
Figure 6: Ariel View of Three Dimensional Displacement

<!-- b000135 | prose | pages [12] -->
To evaluate the best halfpipe shape we again looked at the velocities at the top of the vertical point on the halfpipe. Like we did for the two dimensional model we evaluate the velocities this time in both y and z directions. The x velocity is the speed that the snow boarder is traveling down the slope and because the model does not take into account the stylistic ways that snowboarders convert the x velocity we can ignore them for the optimization of vertical air.

<!-- b000136 | prose | pages [12] -->
φ Shape Y Velocity Z Velocity (degrees) (m/s) (m/s) 45 Parabola 1 2.981 4.232 45 Parabola 2 1.639 3.307 45 Circle 0.129 2.572 By modeling this further into a projectile motion problem we can verify that the function yielding the greatest velocity in the z and y direction will give the greatest vertical air. So, by comparing and contrasting the three diﬀerent models we can extrapolate that:

<!-- b000137 | prose | pages [12] -->
• Parabola 2 is 44 percent better than parabola 1 for maximizing vertical air.

<!-- b000138 | prose | pages [12] -->
• Parabola 1 is 62 percent better than the half circle for maximizing vertical air.

<!-- b000139 | heading | pages [12] -->
3.4 Solutions

<!-- b000140 | prose | pages [12] -->
Maximized Vertical Air Halfpipe

<!-- b000141 | prose | pages [12] -->
• In the conservation of energy model we found that vertical air is maximized when σ is closest to 90 degrees.

<!-- b000142 | furniture | pages [13] -->
Team Control Number 12149

<!-- b000143 | furniture | pages [13] -->
Page 12 of 23

<!-- b000144 | prose | pages [13] -->
• In the two dimensional force model the point of interest for velocity is at the top of the vertical where the snowboarder will achieve vertical air granted that enough speed is achieved. By modeling three diﬀerent functions (half pipe slopes), each at three diﬀerent z-slopes (mountain slope) we determined that for optimal vertical air to be reached, a parabola of the form y = .07x2 −7 (14)

<!-- b000145 | prose | pages [13] -->
gives the greatest vertical air.

<!-- b000146 | prose | pages [13] -->
• In the comprehensive force model we look at the top of the vertical for the velocities to be evaluated to ﬁnd that the mountain should have a slope of 45 degrees and indeed it is the parabola of the form of equation 14 that yields the greatest vertical air.

<!-- b000147 | prose | pages [13] -->
Something to think about is that this is what the model tells us is the best shape but what the model does not take into account is that a snowboarder has various techniques to convert velocities in one direction to another such as carving and toe turns. A more shallow slope is needed for a generalized halfpipe.

<!-- b000148 | prose | pages [13] -->
Best Practical Halfpipe

<!-- b000149 | prose | pages [13] -->
When applying this model to a more realistic situation where a snowboarder converts most of the x-velocity (downward slope speed) into side to side velocity which can also be used for vertical air we might revaluate this conclusion. Taking into mind the fact that an even distribution of velocities with a max in the z direction is important we can look at the data listed in the appendix and see that it is in fact the same parabola (equation 14) with a diﬀerent mountain’s slope of 25 degrees that gives the best realistic shape for a half pipe that gives the best vertical air.

<!-- b000150 | heading | pages [13] -->
4 Testing Methods

<!-- b000151 | prose | pages [13] -->
• Physical testing for the two and three dimensional force models.

<!-- b000152 | prose | pages [13] -->
• Computer simulation with known values for the two and three dimensional force mod- els.

<!-- b000153 | prose | pages [13] -->
• Analytical testing for the conservation of energy model.

<!-- b000154 | heading | pages [13] -->
4.1 Physical Testing

<!-- b000155 | prose | pages [13] -->
For the three dimensional force model we were able to set up a physical model and send a marble down the halfpipe to verify that our computer simulations were modeling the system correctly(ﬁgure 7). We found that the path the marble followed was almost exactly mirrored the three dimensional graph of the snowboarder’s displacement(ﬁgure 8).

<!-- b000156 | furniture | pages [14] -->
Team Control Number 12149

<!-- b000157 | furniture | pages [14] -->
Page 13 of 23

<!-- b000158 | caption | pages [14] -->
Figure 7: Physical Model Testing

<!-- b000159 | caption | pages [14] -->
Figure 8: 3 Dimensional Graph of Snowboarder’s Displacement

<!-- b000160 | heading | pages [14] -->
4.2 Computer Program Stability

<!-- b000161 | prose | pages [14] -->
• In our two dimensional model, we were able to test its stability by changing the pa- rameters controlling it in order to obtain results we knew we should get given the conditions previously set. In our two dimensional model we tested it by:

<!-- b000162 | prose | pages [14] -->
1. Taking away the frictional force and drag force applied to the snowboard and snowboarder and checking to make sure that snowboarder continues perpetually in a pendulum like motion.

<!-- b000163 | furniture | pages [15] -->
Team Control Number 12149

<!-- b000164 | furniture | pages [15] -->
Page 14 of 23

<!-- b000165 | prose | pages [15] -->
2. By not adding work and checking that the snowboarder will continue with a damped motion, until ﬁnally coming to rest.

<!-- b000166 | prose | pages [15] -->
By checking these two conditions, we were able to ensure that our two dimensional model successfully simulated a snowboarder limited to movement in 2 dimensions.

<!-- b000167 | prose | pages [15] -->
• In our three dimensional model, we were able to test the stability in a similar way as was done for the two dimensional model. The stability tests that were run on the three dimension model were:

<!-- b000168 | prose | pages [15] -->
1. Taking away the frictional force and drag force applied to the snowboard and snowboarder, as well as setting φ equal to 0, and checking to make sure that our three dimensional model gave the same results as did our two dimensional model under the same conditions.

<!-- b000169 | prose | pages [15] -->
2. By Setting φ equal to 0 and making sure that our model gives the gives the same results as our two dimensional model.

<!-- b000170 | prose | pages [15] -->
3. By not adding work and checking that the snowboarder will continue with a damped motion, until ﬁnally coming to rest.

<!-- b000171 | prose | pages [15] -->
4. By running our full three dimensional model, and comparing it to the two di- mensional model using the same half-pipe shape, and checking that our three dimensional model gave a higher y velocity as greater Vertical Air, due to added force in the y and z directions due to the added x velocity.

<!-- b000172 | prose | pages [15] -->
With this these methods for checking the stability of our three dimensional model, we were able to make sure that our transition from two dimensions to three, was consistent with the physics behind our model.

<!-- b000173 | prose | pages [15] -->
Analytical Testing

<!-- b000174 | prose | pages [15] -->
The method for testing the conservation of energy model was an intuitive approach to the laws of conservation. Taking into mind the fact that the snowboarder only has as much energy as he starts with when no work is added we could see he would only be able to reach his original height. When adding in work we could verify that the only way that a snowboarder could reach any vertical height above the edge of the halfpipe would be if the snowboarder used pumping to give an additional force to the system.

<!-- b000175 | heading | pages [15] -->
4.3 Error Analysis

<!-- b000176 | prose | pages [15] -->
For our two dimensional model, we computed the error in position due to the Runge Kutta approximation of our ODEs to be 0.1% with a delta t of 0.00001 iterated for 30 seconds.

<!-- b000177 | prose | pages [15, 16] -->
For our three dimensional model, we computed our error in the x, y, z direction to be 0.1% error due to the factors mentioned above. We found that with the Runge Kutta approximation program we ran our simulations on, it is possible to achieve less than 0.1% error by reducing our delta t; however for the given project 0.1% error is a very acceptable percentage.

<!-- b000178 | furniture | pages [16] -->
Team Control Number 12149

<!-- b000179 | furniture | pages [16] -->
Page 15 of 23

<!-- b000181 | heading | pages [16] -->
5 Future Work

<!-- b000182 | prose | pages [16] -->
A possible future model could be a half-pipe down the slope given by the equation of a cycloid. A cycloid is what Bernoulli found to be as the line of fastest line of descent. So, if the average velocity is maximized in the zx direction while holding basic half pipe function constant could potentially increase kinetic energy and maximize vertical air. Realistically this would not necessarily be the best model as the slope of a mountain is rarely in the cycloid equation form.

<!-- b000183 | prose | pages [16] -->
Further consideration with respect to our model would be further testing with piecewise function as well as adding diﬀerent types of work. Our model allowed work to be added in one direction. Also, ﬁnding some way to take into account the stylistic choices of a skilled snowboarder would be another factor we might add in.

<!-- b000184 | furniture | pages [17] -->
Team Control Number 12149

<!-- b000185 | furniture | pages [17] -->
Page 16 of 23

<!-- b000186 | heading | pages [17] -->
6 Appendix

<!-- b000187 | prose | pages [17] -->
/***************************************************************/ /* Runge Kutta for a set of first order differential equations */ /***************************************************************/

<!-- b000188 | prose | pages [17] -->
#include <stdio.h> #include <math.h> #include <iostream> using namespace std;

<!-- b000189 | prose | pages [17] -->
/*************************************/ /* Parameters you may want to change */ /*************************************/ #define N 6 /*number of first order equations */ #define DELTA_T 0.00001 /*stepsize in t */ #define T_MAX 30.0 /*max for t */ #define INITIAL_Y0 0.0 /*y */ #define INITIAL_Y2 0.0 /*velocity y */ #define INITIAL_Y3 0.0 /*velocity in z */ #define INITIAL_Y4 0.0 /*possition in x */ #define INITIAL_Y5 0.0 /*velocity in x */ #define m 75.0 #define g 9.80665 #define mu 0.04 #define w 6000.0 #define hi 3000.0 #define rho_air 1.225 #define area 0.87 #define c_d 0.7 #define PI 3.1415926 #define phi 15*PI/180

<!-- b000190 | prose | pages [17] -->
/******************/ /* Define the ODE */ /******************/ double f(double x, double y[], int i) { double theta, fdrag, n, rho, dzdy, dz2dy,fdragx,fy,fx,vx,vy,z; if(y[0] <= (20/3)) { dzdy=0.5*y[0]-(10/3); dz2dy=0.5; } if(y[0] <= (40/3)) { dzdy=0;

<!-- b000191 | furniture | pages [18] -->
Team Control Number 12149

<!-- b000192 | furniture | pages [18] -->
Page 17 of 23

<!-- b000193 | prose | pages [18] -->
dz2dy=0; } else { dzdy=0.5*y[0]-(20/3); dzdy=0.5; } theta=-atan(dzdy); fdrag=.5*rho_air*area*c_d*(y[2]*y[2]+y[3]*y[3])/m; fdragx=.5*rho_air*area*c_d*(y[5]*y[5])/m; rho=-sqrt((1+dzdy*dzdy)*(1+dzdy*dzdy)*(1+dzdy*dzdy))/dz2dy; n=g*cos(phi)*cos(theta)-(y[2]*y[2]+y[3]*y[3])/rho;

<!-- b000194 | prose | pages [18] -->
if(y[0]==0) { fx=(n*sin(theta))-(mu*n*cos(theta))-(fdrag*cos(theta));

<!-- b000195 | prose | pages [18] -->
fy=-g*cos(phi)+(n*cos(theta))+(mu*n*sin(theta))+(fdrag*sin(theta)); } else if((y[2]<0)) { fy=-g*cos(phi)+(n*cos(theta))-(mu*n*sin(theta))-(fdrag*sin(theta));

<!-- b000196 | prose | pages [18] -->
fx=(n*sin(theta))+(mu*n*cos(theta))+(fdrag*cos(theta)); } //else if((y[2]<0) & (y[3]>0) & (0<=theta) & (theta<= PI/2)) //{ // fy=-g*cos(phi)+(n*cos(theta))+(mu*n*sin(theta))+(fdrag*sin(theta));

<!-- b000197 | prose | pages [18] -->
// fx=(n*sin(theta))-(mu*n*cos(theta))-(fdrag*cos(theta)); //} else { fx=(n*sin(theta))-(mu*n*cos(theta))-(fdrag*cos(theta));

<!-- b000198 | prose | pages [18] -->
fy=-g*cos(phi)+(n*cos(theta))+(mu*n*sin(theta))+(fdrag*sin(theta)); }

<!-- b000199 | prose | pages [18] -->
if (i==0) return(y[2]);

<!-- b000200 | prose | pages [18] -->
if (i==1) return(y[3]); if (i==2) return(fx); if (i==3) return(fy); if (i==4) return(y[5]); if (i==5) return(g*sin(phi)-g*cos(phi)*mu-fdragx); cout << fx;

<!-- b000201 | prose | pages [18, 19] -->
f }

<!-- b000202 | furniture | pages [19] -->
Team Control Number 12149

<!-- b000203 | furniture | pages [19] -->
Page 18 of 23

<!-- b000205 | prose | pages [19] -->
int main(void) {

<!-- b000206 | prose | pages [19] -->
double t, y[N], bob, count;

<!-- b000207 | prose | pages [19] -->
int j,k;

<!-- b000208 | prose | pages [19] -->
void runge4(double x, double y[], double step); /* Runge-Kutta function */

<!-- b000209 | prose | pages [19] -->
y[0]=INITIAL_Y0; /* initial Y[0] */ if(y[0] <= (20/3)) { y[1]=(1/4)*((y[0]-(20/3))*(y[0]-(20/3))); } else if(y[0] <= (40/3)) { y[1]=0; } else { y[1]=(1/4)*((y[0]-(40/3))*(y[0]-(40/3))); } y[2]=INITIAL_Y2; y[3]=0; /* initial Y[1] */

<!-- b000210 | prose | pages [19] -->
count=-1;

<!-- b000211 | prose | pages [19] -->
printf("%lf\t%lf\t%lf\n", INITIAL_Y0,y[1],y[5]);

<!-- b000212 | prose | pages [19] -->
/*************/ /* Time Loop */ /*************/ for (t=0; y[4]<= 175; t+=DELTA_T) {

<!-- b000213 | prose | pages [19] -->
runge4(t, y, DELTA_T);

<!-- b000214 | prose | pages [19] -->
count++;

<!-- b000215 | prose | pages [19, 20] -->
if(y[0] <= (20/3)) { b b (1/4) (( [0] (20/3)) ( [0] (20/3))) } else if(y[0] <= (40/3)) { bob=0; } else { bob=(1/4)*((y[0]-(40/3))*(y[0]-(40/3))); } if (count==6000) { printf("%lf\t%lf\t%lf\n", y[0],y[1],y[5]); count=0;

<!-- b000216 | furniture | pages [20] -->
Team Control Number 12149

<!-- b000217 | furniture | pages [20] -->
Page 19 of 23

<!-- b000219 | prose | pages [20] -->
}

<!-- b000220 | prose | pages [20] -->
}

<!-- b000221 | prose | pages [20] -->
return 0; }

<!-- b000222 | prose | pages [20] -->
/***************************/ /* RK4 Loop, Do Not Change */ /***************************/ void runge4(double x, double y[], double step) { double h=step/2.0; /* the midpoint */ double t1[N], t2[N], t3[N]; /* temporary storage arrays */ double k1[N], k2[N], k3[N],k4[N]; /* for Runge-Kutta */ int i;

<!-- b000223 | prose | pages [20] -->
for (i=0;i<N;i++) t1[i]=y[i]+0.5*(k1[i]=step*f(x, y, i));

<!-- b000224 | prose | pages [20] -->
for (i=0;i<N;i++) t2[i]=y[i]+0.5*(k2[i]=step*f(x+h, t1, i));

<!-- b000225 | prose | pages [20] -->
for (i=0;i<N;i++) t3[i]=y[i]+ (k3[i]=step*f(x+h, t2, i));

<!-- b000226 | prose | pages [20] -->
for (i=0;i<N;i++) k4[i]= step*f(x+step, t3, i);

<!-- b000227 | prose | pages [20] -->
for (i=0;i<N;i++) y[i]+=(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6.0; return; }

<!-- b000228 | furniture | pages [21] -->
Team Control Number 12149

<!-- b000229 | furniture | pages [21] -->
Page 20 of 23

<!-- b000230 | heading | pages [21] -->
6.1 Figures

<!-- b000231 | caption | pages [21] -->
Figure 9: Snowboard halfpipe

<!-- b000232 | caption | pages [21] -->
Figure 10: Basic (no slope in XZ plane) halfpipe

<!-- b000233 | furniture | pages [22] -->
Team Control Number 12149

<!-- b000234 | furniture | pages [22] -->
Page 21 of 23

<!-- b000235 | caption | pages [22] -->
Figure 11: Basic (Velocity Data for the Comprehensive Three Dimensional Force Model

<!-- b000236 | furniture | pages [23] -->
Team Control Number 12149

<!-- b000237 | furniture | pages [23] -->
Page 22 of 23

<!-- b000238 | heading | pages [23] -->
6.2 Figures

<!-- b000239 | caption | pages [23] -->
Figure 12: y and z velocities

<!-- b000240 | heading | pages [23] -->
6.3 Equations for the Comprehensive Force Model

<!-- b000241 | prose | pages [23] -->
X F = m⃗a (15)

<!-- b000242 | prose | pages [23] -->
vy = dy (16) dt vz = dz (17) dt

<!-- b000243 | prose | pages [23] -->
N = mg cos φ cos θ −mv2 (18) ρ Fk = µN (19) Fd = 1 2ρacdv2 (20)

<!-- b000244 | prose | pages [23] -->
θ = arctan dz (21) dy

<!-- b000245 | furniture | pages [24] -->
Team Control Number 12149

<!-- b000246 | furniture | pages [24] -->
Page 23 of 23

<!-- b000247 | heading | pages [24] -->
References

<!-- b000248 | references | pages [24] -->
[1] halfpipe, http : //www.bulgariaski.com/snowboarding.shtml, accessed Febru-

<!-- b000249 | references | pages [24] -->
ary 12, 2011.

<!-- b000250 | references | pages [24] -->
[2] halfpipe, pagesofmind.com, accessed February 12, 2011.

<!-- b000251 | references | pages [24] -->
[3] www.fis −ski.com, accessed February 12, 2011.

<!-- b000252 | references | pages [24] -->
[4] Brisson, Pierre, and Margaret Estivalet. The Engineering of Sport 7. Paris:

<!-- b000253 | references | pages [24] -->
Springer, 2009. Print.

<!-- b000254 | references | pages [24] -->
[5] Fischer-Cripps, Anthony C. The Physics Companion. Bristol:

<!-- b000255 | references | pages [24] -->
Institute of

<!-- b000256 | references | pages [24] -->
Physics Pub., 2003. Print.

<!-- b000257 | references | pages [24] -->
[6] Harding, W, J., Mackintosh, G, C,. Hahn, G, A,. and James, A, D,. Classiﬁca-

<!-- b000258 | references | pages [24] -->
tion of Aerial Acrobatics in Elite Half-Pipe Snowboarding Using Body Mounted

<!-- b000259 | references | pages [24] -->
Inertial Sensors. Biarrits: Proceedings of 7th ISEA Conference., 2008.

<!-- b000260 | references | pages [24] -->
[7] Hibbeler, R. C., and Peter Schiavone. Engineering Mechanics: Dynamics. Upper

<!-- b000261 | references | pages [24] -->
Saddle River, NJ: Pearson/Prentice Hall, 2007. Print.

<!-- b000262 | references | pages [24] -->
[8] Van, Brunt B. The Calculus of Variations. New York: Springer, 2004. Print.

<!-- b000263 | references | pages [24] -->
[9] Walker, James S. Physics. Upper Saddle River, NJ: Prentice Hall, 2002. Print.
