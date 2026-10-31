Abstract

The shape of a snowboarding halfpipe can be designed to maximize the vertical air a professional snowboarder will achieve; however, a practical course will take into account factors such as the number of cycles a snowboarder can make side to side as he descends the mountain, and the shape that yields the best launch for stunts.

As a snowboarder descends a halfpipe the forces acting on him are dependent on the shape of the course. We will use Newton’s Second Law of Motion to sum the forces in each direction. Then we used a Runga-Kutta method computer simulation to determine the acceleration of the snowboarder down the course. We tested three diﬀerent functions that describe the shape of the half pipe, with three varying slopes for each. Using a computer simulation and physical testing the velocity of the snowboarder can be analyzed at the edge of the half pipe. The shapes that yield the largest vertical air and the most practical course will then be chosen as the best design.

The forces taken into consideration in these models include: gravity, centrifugal, frictional, air resistance, and a constant force applied in the direction of travel that mimics the force from a professional snowboarder pumping his legs. These models do not take into account the force a professional snowboarder’s stylistic force would use to guide his path along the halfpipe.

After running our three models we determined that out of the various shapes tested the best vertical height was optimized at a mountain slope of 45 degrees with a half pipe shape of the parabola z(y) = .07y2 −7 The best practical model was found to be the same parabola at a mountain slope of 25 degrees. The Runge Kutta method approximation had an error of 0.1 %. Our best model is the comprehensive three dimensional force because it most realistically describes a snowboarder on a halfpipe.

1 Introduction

Developed in the 1970’s, snowboarding has come a long way from the original snurfer (snow-surfer) which was an attempt by Shermann Poppen to bring surﬁng to the Rocky Mountains. Since then snowboarding has taken oﬀwith perfecting ramps and slopes to enable a variety of tricks and stunts. Some of these stunts require a simple slope, others a rail, and for this problem we will look speciﬁcally at the half-pipe in order to optimize vertical air which can be deﬁned as the distance a skilled snowboarder can obtain by being launched oﬀthe edge of the halfpipe.

1.1 The Problem

A Basic Halfpipe

A basic halfpipe consists of two concave ramps separated by a distance which totals to the width of the half pipe(ﬁgure 10). The vertical side of the ramp, or the edge, is called a vertical, the curved part of the vertical is called the transition, and the distance between the two ramps is called the ﬂat.

In a basic halfpipe the vertical and transition allow for back and forth motion using the force of gravity to give the snowboarder a velocity. A snowboarder uses the ﬂat to regain balance as well as a time to pump. Pumping adds work to the system and gives the boarder a greater velocity to make it up the opposite vertical and obtain a higher vertical air. Because the ﬂat optimizes the angle that the force exerts on the snowboarder pumping happens primarily on the ﬂat(see equation 6).

A Snowboarding Halfpipe

A snowboarding halfpipe is a basic halfpipe that is built onto a hill (ﬁgure 9). The slope of the hill gives a new form of energy that can be converted to velocity and used to maximize vertical air. The plane of the transition is oriented downhill at a slight grade to allow riders to use gravity in two directions to create a velocity both back and forth and down the slope to develop the optimal speed for stunts that require vertical air.

The character of the half pipe depends mostly on the relationship between the transition angle and the height of each vertical. The higher the vertical the more diﬃcult it is to land while a narrow stretch between the two verticals provides less time to recover as well as less opportunity to pump. So what is the best shape of a half pipe to optimize a skilled snowboarder’s vertical air? And what kind of options does the snowboarder have for a variety of stunts? And what changes could be made to develop a practical course?

Our Approach

In order to ﬁnd a snowboarder’s optimized vertical air we used both conservation of energy and Newton’s 2nd Law to account for the various forces acting on a snowboarder while traveling down the half-pipe. We constructed models based on the law of conservation of energy and Newton’s Laws. Using a function z(y) for the shape of the halfpipe we were able to set up a model that allows a function to be easily altered and evaluated for any shape.

• Conservation of Energy Model: The energy model depends only on the change in height and gravity (ﬁg 1). Work can be added to this model in the form of a snowboarder pumping over the ﬂat. This model gives an idea of how a more complex model might look.

• Two Dimensional Force Model: We used Newton’s 2nd Law in 2D to minimize the energy lost through friction and air resistance by creating a system of ordinary diﬀerential equations that described the forces acting on the snowboarder (ﬁgure 2).

We evaluated a series of equations for the curve of the halfpipe, and evaluated the numerical results to determine which curve gave the best vertical air. This model acts on the assumption that the snowboarder is in a basic halfpipe which does not include the slope of the mountain.

• Comprehensive Three Dimensional Force Model: Our ﬁnal and most compre- hensive model takes into account both the potential energy converted from the descent down the slope as well as friction from both air and snow. In order to model the loss in potential energy due to the decreasing height we developed a model that is based on not only the pitch of the two adjacent sides of the half-pipe but also the slope of the hill that the half-pipe is on. We continued using Newton’s 2nd Law of motion as we did for the two dimensional model to determine the maximum height that can be reached by a snowboarder under the inﬂuence of gravity, pumping, air resistance, and the friction between the snow and the board.

2 Models

2.1 Conservation of Energy

How It Works

The conservation of energy model is our most intuitive analysis of the snowboarders speed. Looking at the conversion of potential energy to a new potential energy (through a change in height) we can determine analytically the kinetic energy used to launch a snowboarder oﬀ of the verticals and gain as much vertical air as possible (ﬁgure 1).

KEi + PEi = KEf + PEf (1)

Under the following conditions:

vi = 0 (2)

hi > hf (3)

The conservation of energy results in the following equation.

p (2g(hi −hf)) v = (4)

Without adding any work the snowboarder will never go beyond the original height. In order to see the importance of pumping we added work to the system and the equation of velocity is changed by a factor of work (equation 6).

W = Fapplied • d = Fappliedd cos σ (5)

F(applied) is the force applied by the snowboarder, d is the distance between the two verticals and σ is the angle in which the force is applied.

p (2g(hi −hf) + 2W) v = (6)

A higher velocity means there is a higher vertical air. However, the angle of take oﬀmust be taken into account as well. Consider θ which is the angle between the horizontal axis and the direction of the velocity of the snowboarder (ﬁgure 1). When θ = π 2 then our velocity is entirely in the z direction and our vertical air is maximized. Conversely we can also see that when θ = 0 our velocity is entirely in the x direction and we have no vertical air.

Consequences

The information provided by this analysis gives an intuitive look into what a snow- boarder’s motion would be neglecting all forms of friction in a two dimensional plane, with the option to add work. A closer look at the direction of the resulting velocity shows the importance of the takeoﬀangle. By choosing the angle of take oﬀ(angle between slope and horizon) to be as close as possible to 90 degrees a snowboarder can maximize vertical air.

Strengths

• This model gives information for the height diﬀerence necessary to give a snowboarder vertical air using only potential energy.

• Simulations are quick, and it is easy to alter the height diﬀerence of the halfpipe verticals.

• This model allows work to be added to the system.

• The model only depends on the original and ﬁnals height which means any path could be taken.

Weaknesses

• This model does not provide a way to solve for an optimal angle of either the half-pipe or the hill.

• This model does not take into account any frictional forces.

2.2 Two Dimensional Force Model

How It Works

In order to model a snowboarder’s path down a two dimensional movement we used a set of linear ordinary diﬀerential equations for the forces acting on the snowboarder in both z and y directions ( down and left to right). The gravitational, frictional and drag forces acting on the snowboarder are summed along the z and y axis (looking in the 3-D z-y plane).

1 2ρairacd(v2 x + v2 y) Fdrag = (7) m

N = g cos(θ) −(v2 y + v2 z) (8) ρ Using Newton’s Second Law of Motion P F = m⃗a we can see that the force acting on the snowboarder in the y-axis is equal to mass times acceleration along the y-axis. Applying this to both the y and z axis yields two second order diﬀerential equations (equations 9 and 10).

dvy dt = N sin θ −µN cos θ −Fdyz cos θ + ρ cos θ (9)

dvz dt = −g + N cos θ −µN sin θ + Fdyz sin θ −ρ sin θ (10)

These two second order diﬀerential equations can be broken down into four ﬁrst order dif- ferential equations. (Further derivation of these equations can be reviewed in the appendix).

Using a computer simulated Runga-Kutta method, the four diﬀerential equations are solved yielding the snowboarder’s path and velocity across the halfpipe. A force was added in the direction of travel that mimics the force of the snowboarder pumping his legs to add speed(equation 5).

Consequences

This model corrects for the drag force and frictional force acting on the snowboarder. These forces are dependent upon velocity across the halfpipe. This model shows how diﬀerent shapes aﬀect the amount of energy lost due to friction and drag. By adding the force of the snowboarder pumping his legs, the model shows the velocity in the z direction at the point the snowboarder leaves the halfpipe which is proportional to the vertical air the snowboarder achieves. With the added force being constant, and the dimensions similar, each shape can be analyzed side by side to determine the best cross-sectional shape for a halfpipe (ﬁgure 2).

St th • This method takes into account the frictional and drag forces that the ﬁrst model neglected.

• Oﬀers a solution for optimizing the pitch of the halfpipe.

• Simulations are quick, and it is easy to alter the height of the verticals or the width of the halfpipe.

• The shape of the halfpipe can be changed into any function for z(y).

Weaknesses

• This model neglects the acceleration added from the halfpipe sloping down a hill.

• Only the z-y cross-sectional dimensions are optimized.

2.3 Comprehensive Three Dimensional Force Model

In order to model this problem in three dimensions we came up with a three dimensional force diagram. In this model we are taking into account the zx plane’s potential energy that is being converted into kinetic energy as the snowboarder descends the hill. For the sake of simplicity we shifted the axis used to deﬁne the zx plane so that the normal force is solely in the z direction (ﬁgure 3).

An important observation to take into account for this model is the fact that we redeﬁned the coordinate system; this means that the force of gravity used in the 2D model of the zy plane (ﬁgure 2) is now gravity multiplied by the cos(φ). Where φ is the angle of the halfpipe on the hill.

dvx dt = g sin φma −g cos φµ −Fdx (11)

dvy dt = N sin θ −µN cos θ −Fdyz cos θ + ρ cos θ (12)

dvz dt = −g cos φ + N cos θ −µN sin θ + Fdyz sin θ −ρ sin θ (13)

Consequences

With the force caused by the ramp going down a slope added, this model allows the path and the velocity of the snowboarder side to side movement across the halfpipe to be evaluated as well as the velocity down the hill. This lets us see how the slope of the hill eﬀects the vertical distance above the halfepipe the snowboarder is able to achieve.

This model can be used to look at both variables; slope and the function of the cross- section, which allows us to choose the pair that yields the most desirable results.

Strengths

• This model takes into account the forces in all three directions by including the slope of the halfpipe down the hill.

• This model allows diﬀerent combinations of slope and cross-sectionals to be tested together.

• This model oﬀers a way to easily change the parameters of the system in question.

Weaknesses

• This model does not take into account the stylistic ways a snowboarder uses to slow himself down in the x direction.

• This model does not take into account how a professional snowboarder will guide his path down the halfpipe

2.4 Assumptions

• The snowboarder does not add force to the system causing a change in direction.

• The force added in the two-dimensional model to mimic the snowboarder pumping his legs to add speed was added by adding a single constant force in the direction of travel.

• In the three-dimensional model the added force is only taken into consideration in the z-y plane.

• No projectile motion is modeled for after the snowboarder leaves the halfpipe.

3 Results

After evaluating each model we came to the conclusion that the best model is the three dimensional force model. It has the most broad spectra with the ability to easily change the slope of the mountain or the halfpipe verticals and still not lose the information needed to observe the snowboarder’s velocity in all directions. Both the conservation of energy model and the two dimensional force model are necessary for evaluating how the slope changes a snowboarder’s velocity, as well as demonstrating the importance of strategies such as pumping, that add work to the system.

3.1 Conservation of Energy Model Results

This was an analytical model so there is no data to graph. However, a clear understanding of the model gives an intuitive look into why we choose to use second order diﬀerential equations to model the more complex systems. The information taken from this model is that in order to maximize vertical air the take oﬀangle must be as close as possible to 90 degrees. Another less realistic suggestion to maximize velocity in the absence of work is to make one vertical shorter than the other in order to achieve vertical air from the left over converted potential energy (ﬁgure 1).

3.2 Two Dimensional Force Model Results

The two dimensional force model is used to evaluate the ﬁnal velocity of the snowboarder at the peak of the opposite vertical. By breaking the velocity into y and z components we were able to compare the ﬁnal z velocity of three diﬀerent functions.

Function Z Velocity (m/s) Y Velocity (m/s) Line Color Initial Position (m) Center Parabola 2 2.71546 1.357389 Green (-10,0) (0,-10) Circle 2.670921 0.139753 Black (-10,0) (0,-10) Parabola 1 3.54291 2.527488 Red (-10,0) (0,-7) Shape Name Formula z(y) = .07y2 −7 Parabola 1 Where the functions used are: z(y) = .1y2 −10 Parabola 2 p 100 −y2 Circle z(y) =

In order to be able to compare these three functions, all the functions should initially start at the same (z,y) and span the same y distance (width of the half pipe). The following graph is showing the motion of a snowboarder in the yz plane with friction and air resistance added.

In order to evaluate the aﬀect of work done by the snowboarder a set value for the force added through work was added to the model. Because the snowboarder cannot reach a height greater than his original height using only potential energy he must use the pumping method to give him a greater velocity.This can be seen in the following graph of the snowboarder’s displacement.

By modeling this further into a projectile motion problem we can verify that the function yielding the greatest velocity in the z direction will give the greatest vertical air. So, by comparing and contrasting the three diﬀerent models we can extrapolate that:

• Parabola 1 is 23 percent better than parabola 2.

• Parabola 2 is 1.6 percent better than the circle.

3.3 Comprehensive Three Dimensional Force Model Results

The comprehensive three dimensional force model allows the displacement in the x, y and the z direction to be graphed in a three dimensional graph (ﬁgure 6).

To evaluate the best halfpipe shape we again looked at the velocities at the top of the vertical point on the halfpipe. Like we did for the two dimensional model we evaluate the velocities this time in both y and z directions. The x velocity is the speed that the snow boarder is traveling down the slope and because the model does not take into account the stylistic ways that snowboarders convert the x velocity we can ignore them for the optimization of vertical air.

φ Shape Y Velocity Z Velocity (degrees) (m/s) (m/s) 45 Parabola 1 2.981 4.232 45 Parabola 2 1.639 3.307 45 Circle 0.129 2.572 By modeling this further into a projectile motion problem we can verify that the function yielding the greatest velocity in the z and y direction will give the greatest vertical air. So, by comparing and contrasting the three diﬀerent models we can extrapolate that:

• Parabola 2 is 44 percent better than parabola 1 for maximizing vertical air.

• Parabola 1 is 62 percent better than the half circle for maximizing vertical air.

3.4 Solutions

Maximized Vertical Air Halfpipe

• In the conservation of energy model we found that vertical air is maximized when σ is closest to 90 degrees.

• In the two dimensional force model the point of interest for velocity is at the top of the vertical where the snowboarder will achieve vertical air granted that enough speed is achieved. By modeling three diﬀerent functions (half pipe slopes), each at three diﬀerent z-slopes (mountain slope) we determined that for optimal vertical air to be reached, a parabola of the form y = .07x2 −7 (14)

gives the greatest vertical air.

• In the comprehensive force model we look at the top of the vertical for the velocities to be evaluated to ﬁnd that the mountain should have a slope of 45 degrees and indeed it is the parabola of the form of equation 14 that yields the greatest vertical air.

Something to think about is that this is what the model tells us is the best shape but what the model does not take into account is that a snowboarder has various techniques to convert velocities in one direction to another such as carving and toe turns. A more shallow slope is needed for a generalized halfpipe.

Best Practical Halfpipe

When applying this model to a more realistic situation where a snowboarder converts most of the x-velocity (downward slope speed) into side to side velocity which can also be used for vertical air we might revaluate this conclusion. Taking into mind the fact that an even distribution of velocities with a max in the z direction is important we can look at the data listed in the appendix and see that it is in fact the same parabola (equation 14) with a diﬀerent mountain’s slope of 25 degrees that gives the best realistic shape for a half pipe that gives the best vertical air.

4 Testing Methods

• Physical testing for the two and three dimensional force models.

• Computer simulation with known values for the two and three dimensional force mod- els.

• Analytical testing for the conservation of energy model.

4.1 Physical Testing

For the three dimensional force model we were able to set up a physical model and send a marble down the halfpipe to verify that our computer simulations were modeling the system correctly(ﬁgure 7). We found that the path the marble followed was almost exactly mirrored the three dimensional graph of the snowboarder’s displacement(ﬁgure 8).

4.2 Computer Program Stability

• In our two dimensional model, we were able to test its stability by changing the pa- rameters controlling it in order to obtain results we knew we should get given the conditions previously set. In our two dimensional model we tested it by:

1. Taking away the frictional force and drag force applied to the snowboard and snowboarder and checking to make sure that snowboarder continues perpetually in a pendulum like motion.

2. By not adding work and checking that the snowboarder will continue with a damped motion, until ﬁnally coming to rest.

By checking these two conditions, we were able to ensure that our two dimensional model successfully simulated a snowboarder limited to movement in 2 dimensions.

• In our three dimensional model, we were able to test the stability in a similar way as was done for the two dimensional model. The stability tests that were run on the three dimension model were:

1. Taking away the frictional force and drag force applied to the snowboard and snowboarder, as well as setting φ equal to 0, and checking to make sure that our three dimensional model gave the same results as did our two dimensional model under the same conditions.

2. By Setting φ equal to 0 and making sure that our model gives the gives the same results as our two dimensional model.

3. By not adding work and checking that the snowboarder will continue with a damped motion, until ﬁnally coming to rest.

4. By running our full three dimensional model, and comparing it to the two di- mensional model using the same half-pipe shape, and checking that our three dimensional model gave a higher y velocity as greater Vertical Air, due to added force in the y and z directions due to the added x velocity.

With this these methods for checking the stability of our three dimensional model, we were able to make sure that our transition from two dimensions to three, was consistent with the physics behind our model.

Analytical Testing

The method for testing the conservation of energy model was an intuitive approach to the laws of conservation. Taking into mind the fact that the snowboarder only has as much energy as he starts with when no work is added we could see he would only be able to reach his original height. When adding in work we could verify that the only way that a snowboarder could reach any vertical height above the edge of the halfpipe would be if the snowboarder used pumping to give an additional force to the system.

4.3 Error Analysis

For our two dimensional model, we computed the error in position due to the Runge Kutta approximation of our ODEs to be 0.1% with a delta t of 0.00001 iterated for 30 seconds.

For our three dimensional model, we computed our error in the x, y, z direction to be 0.1% error due to the factors mentioned above. We found that with the Runge Kutta approximation program we ran our simulations on, it is possible to achieve less than 0.1% error by reducing our delta t; however for the given project 0.1% error is a very acceptable percentage.

5 Future Work

A possible future model could be a half-pipe down the slope given by the equation of a cycloid. A cycloid is what Bernoulli found to be as the line of fastest line of descent. So, if the average velocity is maximized in the zx direction while holding basic half pipe function constant could potentially increase kinetic energy and maximize vertical air. Realistically this would not necessarily be the best model as the slope of a mountain is rarely in the cycloid equation form.

Further consideration with respect to our model would be further testing with piecewise function as well as adding diﬀerent types of work. Our model allowed work to be added in one direction. Also, ﬁnding some way to take into account the stylistic choices of a skilled snowboarder would be another factor we might add in.

6 Appendix

/***************************************************************/ /* Runge Kutta for a set of first order differential equations */ /***************************************************************/

#include <stdio.h> #include <math.h> #include <iostream> using namespace std;

/*************************************/ /* Parameters you may want to change */ /*************************************/ #define N 6 /*number of first order equations */ #define DELTA_T 0.00001 /*stepsize in t */ #define T_MAX 30.0 /*max for t */ #define INITIAL_Y0 0.0 /*y */ #define INITIAL_Y2 0.0 /*velocity y */ #define INITIAL_Y3 0.0 /*velocity in z */ #define INITIAL_Y4 0.0 /*possition in x */ #define INITIAL_Y5 0.0 /*velocity in x */ #define m 75.0 #define g 9.80665 #define mu 0.04 #define w 6000.0 #define hi 3000.0 #define rho_air 1.225 #define area 0.87 #define c_d 0.7 #define PI 3.1415926 #define phi 15*PI/180

/******************/ /* Define the ODE */ /******************/ double f(double x, double y[], int i) { double theta, fdrag, n, rho, dzdy, dz2dy,fdragx,fy,fx,vx,vy,z; if(y[0] <= (20/3)) { dzdy=0.5*y[0]-(10/3); dz2dy=0.5; } if(y[0] <= (40/3)) { dzdy=0;

dz2dy=0; } else { dzdy=0.5*y[0]-(20/3); dzdy=0.5; } theta=-atan(dzdy); fdrag=.5*rho_air*area*c_d*(y[2]*y[2]+y[3]*y[3])/m; fdragx=.5*rho_air*area*c_d*(y[5]*y[5])/m; rho=-sqrt((1+dzdy*dzdy)*(1+dzdy*dzdy)*(1+dzdy*dzdy))/dz2dy; n=g*cos(phi)*cos(theta)-(y[2]*y[2]+y[3]*y[3])/rho;

if(y[0]==0) { fx=(n*sin(theta))-(mu*n*cos(theta))-(fdrag*cos(theta));

fy=-g*cos(phi)+(n*cos(theta))+(mu*n*sin(theta))+(fdrag*sin(theta)); } else if((y[2]<0)) { fy=-g*cos(phi)+(n*cos(theta))-(mu*n*sin(theta))-(fdrag*sin(theta));

fx=(n*sin(theta))+(mu*n*cos(theta))+(fdrag*cos(theta)); } //else if((y[2]<0) & (y[3]>0) & (0<=theta) & (theta<= PI/2)) //{ // fy=-g*cos(phi)+(n*cos(theta))+(mu*n*sin(theta))+(fdrag*sin(theta));

// fx=(n*sin(theta))-(mu*n*cos(theta))-(fdrag*cos(theta)); //} else { fx=(n*sin(theta))-(mu*n*cos(theta))-(fdrag*cos(theta));

fy=-g*cos(phi)+(n*cos(theta))+(mu*n*sin(theta))+(fdrag*sin(theta)); }

if (i==0) return(y[2]);

if (i==1) return(y[3]); if (i==2) return(fx); if (i==3) return(fy); if (i==4) return(y[5]); if (i==5) return(g*sin(phi)-g*cos(phi)*mu-fdragx); cout << fx;

f }

int main(void) {

double t, y[N], bob, count;

int j,k;

void runge4(double x, double y[], double step); /* Runge-Kutta function */

y[0]=INITIAL_Y0; /* initial Y[0] */ if(y[0] <= (20/3)) { y[1]=(1/4)*((y[0]-(20/3))*(y[0]-(20/3))); } else if(y[0] <= (40/3)) { y[1]=0; } else { y[1]=(1/4)*((y[0]-(40/3))*(y[0]-(40/3))); } y[2]=INITIAL_Y2; y[3]=0; /* initial Y[1] */

count=-1;

printf("%lf\t%lf\t%lf\n", INITIAL_Y0,y[1],y[5]);

/*************/ /* Time Loop */ /*************/ for (t=0; y[4]<= 175; t+=DELTA_T) {

runge4(t, y, DELTA_T);

count++;

if(y[0] <= (20/3)) { b b (1/4) (( [0] (20/3)) ( [0] (20/3))) } else if(y[0] <= (40/3)) { bob=0; } else { bob=(1/4)*((y[0]-(40/3))*(y[0]-(40/3))); } if (count==6000) { printf("%lf\t%lf\t%lf\n", y[0],y[1],y[5]); count=0;

}

}

return 0; }

/***************************/ /* RK4 Loop, Do Not Change */ /***************************/ void runge4(double x, double y[], double step) { double h=step/2.0; /* the midpoint */ double t1[N], t2[N], t3[N]; /* temporary storage arrays */ double k1[N], k2[N], k3[N],k4[N]; /* for Runge-Kutta */ int i;

for (i=0;i<N;i++) t1[i]=y[i]+0.5*(k1[i]=step*f(x, y, i));

for (i=0;i<N;i++) t2[i]=y[i]+0.5*(k2[i]=step*f(x+h, t1, i));

for (i=0;i<N;i++) t3[i]=y[i]+ (k3[i]=step*f(x+h, t2, i));

for (i=0;i<N;i++) k4[i]= step*f(x+step, t3, i);

for (i=0;i<N;i++) y[i]+=(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6.0; return; }

6.1 Figures

6.2 Figures

6.3 Equations for the Comprehensive Force Model

X F = m⃗a (15)

vy = dy (16) dt vz = dz (17) dt

N = mg cos φ cos θ −mv2 (18) ρ Fk = µN (19) Fd = 1 2ρacdv2 (20)

θ = arctan dz (21) dy
