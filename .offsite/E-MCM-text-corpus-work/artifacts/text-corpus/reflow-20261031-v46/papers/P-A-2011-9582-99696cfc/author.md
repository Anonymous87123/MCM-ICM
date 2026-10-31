Summary

Our basic model can be divided into two parts. The first part is to find a half-pipe shape which can maximize “Vertical Air”; in the second part, we adapt the shape to maximize the possible total angle of rotation. In the extended model, we analyze the snowboarder’s subjective influence on “Vertical Air” and the total degree of rotation. Finally, we discuss the feasibility and the trade-off of building a practical course.

The major assumption is that the resistance includes the friction of snow and air drag. The former is proportional to the normal force and the latter is proportional to the square of velocity. Plus, the snowboarder is perpendicular to the tangential surface of the course at his locus during his movement on the half-pipe. The variables of our model include: coordinate variables x, y, z, normal force N, resistance f, snowboarder’s mass m, mechanical energy lost due to friction of the snow and air drag Elost, vertical air Hf, and the initial angular momentum of the fly L0.

In the first part of our basic model, we obtain a differential equation of Elost based on force analysis and Energy Conservation. Then we derive the representation of Elost by solving the equation, which is a functional. Thus we calculate the representation of “Vertical Air” by analyzing the projectile motion. In the second part of the basic model, we derive the representation of the initial angular momentum before the fly, and discuss the factors influencing it. In our extended model, we calculate the “Vertical Air” when taking the snowboarder’s subjective influence into account.

We use numerical method to solve the model and compare analytical results with reality and validate our method to be correct and robust. We analyzed the effects of factors such as width, height and gradient angle of half-pipe on “vertical Air” by controlling other factors, and found that wider, steeper course with proper depth and the best path chosen by a skilled snowboarder are preferred to obtain locally larger “vertical air”. Using Gene Algorithm, we globally optimized the course shape to provide largest “vertical air” and total degree of rotation. There is a trade-off between maximum “vertical air” and maximum rotation. Implementing a hybrid scoring system as the objective function, we optimize the course shape to a “half-blood” shape that would provide the eclectically best snowboard performance. Furthermore, we take practical problems into consideration and provide answers to more questions such as what roles the flat bottom and “vert” play in reality.

We finely model the entire complicated proceeding and give numerical solution of optimal course, and establish an objective evaluating function to analyze local and global optical course. Diverse subjective influence of snowboarders is also considered. Yet, the model hasn't provided analytic solution of optimal course.

Background

A half-pipe is the venue in which gravity extreme sports such as snowboarding, skateboarding are hold [1]. It usually consists of two concave ramps (including a transition and a vert), topped by copings and decks, facing each other across a transition as shown in Figure 1 [1]. The sport half-pipe snowboarding has been a part of the Winter Olympic competition program since the 2002 Winter Olympic Games held in Nagano, Japan [2]. In the Olympic half-pipe, the riders give two runs, which is a combination of tricks including Straight airs, Grabs, Spins, Flips and Inverted Rotations, etc.

No explicit analysis of the ‘best’ shape of a half-pipe is found. However, it is usually accepted that the half-pipe is 100 to 150 meters long, 17 to 19.5 meters wide and has a height of 5.4 to 6.5 meters (from floor to crown). The slope angle is 16 to 18.5 degrees [3] .In addition, the Federation Internationale de Ski (FIS) recommended that the Width(W), Height(H), Transition(T) and the Bottom Flat(B) could be 15m, 3.5m, 5m, 5m, respectively (as Shown in Figure 2[4]).

Half-pipe snowboarding is currently judged in competition using subjective measures. Still, there is strong community perception that air-time and degree of rotation play a major role in half-pipe competition success [5][6]. Moreover, researches such as Jason William Harding, Colin Gordon Mackintosh, David Thomas Martin1, Allan Geoffrey Hahn5 and Daniel Arthur James [1][7] have attempted to invite objective analysis into the scoring system. According to them, the air time and the total degree of rotation are the two most critical evaluating criterions.

Figure 2 Terminology & Definition

A cycle: the start of “a cycle” is the moment when the snowboarder reaches the edge of the half-pipe after a fly, and the end of “a cycle” is the next start Fly: the part of the movement when the snowboarder is airborne Flying distance (Sf): the displacement along z direction during the fly Flying time (tf): the duration of the fly Cycle distance (Sc): the displacement along z direction during a cycle

Assumptions

a. The cross-section of the half-pipe have to be a curve which is convex to the downwards (U shape), and the curve should be second-order derivable at every point except for the endpoints. b. The snowboarder keeps a crouching position during the whole course of his performance on the half-pipe, and he stands up to gain speed right at the edge of the half-pipe before the fly. c. Neglect the rotational kinetic energy of the snowboarder before considering the twist performance of him. d. The friction of the snow is proportional to the normal force of the snow exerted on the snowboarder while has nothing to do with velocity (that is, the angle between the direction of the snowboard and that of snowboarder’s velocity is constant.), and the coefficient is α. Air drag is proportional to the square of the velocity, and the coefficient is β. e. The snowboarder’s body is perpendicular to the tangential surface of the half-pipe at the locus of the snowboarder during his movement on the half-pipe. f. When considering the half-pipe shape in the model, neglect its mechanical feasibility for the snow and the snowboard. (We will discuss it in the section concerning ‘practical’ course instead) g. The force exerted on board can be considered as acting on the center of the board. h. We neglect the influence of natural factors such as uneven sunshine (which may result from an East or West orientation) , altitude, etc.

Parameters

Parameter Parameter x, y, z Coordinate variables s The length of the path x , y , z The velocities in the direction of E0 The initial mechanical energy at x, y, z respectively the beginning of a cycle y’, y’’ Eleave the kinetic energy right before ∂2y ∂y ∂x , ∂x2 the fly z’ Ereach the kinetic energy at the end of ∂z ∂x the fly N Normal force of the snow exerted on the snowboarder

f The friction of the snow + air drag m The mass of the snowboarder

The angle between z axis and θ the horizontal plane ∆h The rise of the mass point of the snowboarder when he stands up from a crouching position. Elost The mechanical energy lost due to friction of the snow and air drag Hf Vertical air

Whuman Work done by the snowboarder at the edge of half-pipe when he stands up WG the decrease of the gravitational potential during the fly The friction coefficient between α the snow and snowboard Drag coefficient of air β

Radius of curvature at a certain ρ point of the cross-section of the half-pipe x, y, z, y’, z’, y , z , y’’ right before xt, yt, zt, yt’, zt’, yt , the fly zt , yt’’

coordinate variables, x is the free variable, while y and z are functions of x depending of the shape of the half-pipe and path of the snowboarder, which can also be represented as y(x) and z(x). The relationship between y and x depends on the shape of the half-pipe, while the relationship between z and x depends on the path chosen by the snowboarder.

Basic Model

Model overview

Figure 4

help give an overview of our model.

air drag, green: with air drag), which is an entire “cycle”.

“A cycle” can be devided into two parts. The first part is the movement on the half-pipe, and the second part is the airbourn performance. In the first part, since our concern is the final velocity, focusing on the convertion and conservation is the most efficient way. Hence the lost of mechanical energy Elost is the key of our study in this part. Due to the fact that Elost is caused by the resistance of snow and air, we can derive an equation about Elost with the help of integration after we derive the representation of resistance f by force analyzing. Then we transform the equation into a differential equation and solve it, which yield the representation of Elost. Since the shape of the half-pipe and the path chosen by the snowboarder need to be determined, the represetation of Elost is a functional. Another thing that cannot be neglected is the contribution of the snowboarder to the increase of mechanical energy at the end of the first part. This part of work is done by streching his body (standing up) and doing work against the pseudo force petrifugal force.

As to the second part, to derive the “vertical air”, the Second Newton Law is applied. If we neglect the air drag during the fly (actually the numerical method in later part of this artical proves that the air drag during the fly is neglegibal), we can calculate “vertical air”, the duration of the fly, flying distance, gravitational potential decrease, etc. Since we don’t know whether air drag is neglegibal before we compare the results of the calculation considering and neglecting the air drag, we also have to make a calculation taking the air drag into account.

Next, the airbourn rotation of the snowboarder is discussed. Since the shape of half-pipe directaly influnces the initial angular momentum of the snowboarder, and the angular momentum is the only thing that cannot be changed during the flight (the snowboarder can do work by changing his posture to increase the mechanical energy), the relationship between the half-pipe shape and the initial angular momentum is the key of our discussion here. After deriving the representation of the initial angular momentum, we can find the optimal shape of the half-pipe.

The Model

A. Vertical air Step 1.  Force analysis (figure 6) There are three kinds of force acted on the snowboarder, which are gravity mg, normal force N and resistance f. Resistance includes air drag and the friction between the snow and snowboard. N balances with the gravity’s and the pseudo force centrifugal force’s projection in the normal direction of the half-pipe surface at this point. And f causes the loss of mechanical energy.

Among the forces, resistance can be represented as: f = αN + β(x 2 + y 2 + z 2) = αN + β(1 + y′2 + z′2)x 2                        (1)

Next consider the expression of normal force. Only the part of centripetal acceleration which parallels the direction of N needs to be considered when we calculate the Normal force. Thus we get the expression eq.2.

3 (1+y′2) 2 ρ = y′′

x 2+y 2 mgcos θ N = m + 1+y′2 ρ

= (y′′x 2 + g cos θ) m 1+y′2                       (2) Path length unit can be represented as:

ds =  1 + y′2 + z′2 dx                          (3)

Step 2.  According to the Energy Conservation Principle, we have equation 4.

2 m 1 + y′2 + z′2 x 2 = E0 −Elost −mg y cos θ −z sin θ          (4) 1

Then we have x 2 = 2 m 1+y′2+z′2  E0 −Elost −mg y cos θ −z sin θ              (5)

Step 3.  Now we can calculate the expression of Elost.

x Elost (x) = f ∙ds −x0

[αN 1 + y′2 + z′2 + β(1 + y′2 + z′2) 3 x 2 ∙τ 2]dτ = −x0

my ′′ x 2 m E0 −Elost τ −mg y cos θ − z sin θ  + = { α + β −x0 1+y′2  1+y′2+z′2

αmgcosθ1+y′2+z′21+y′2}dτ (6)

The expression of Elost in equation 6 is an integral with variable upper limit. And τ, representing the x coordinate, is the integral variable.

Differentiating both sides of equation 6, and solving the out-coming linear ordinary differential equation of the first order, we have x x x a(τ) dτ −a(τ) dτ Elost = e b(ξ) ∙e ∗ dξ               (7) −x0 −x0 −x0 In which

y′′ 2β a(x) = − 2α + m                     (8) 1+y′2  1+y′2+z′2

y′′ 2β m  E0 −mg y cos θ −z sin θ  + b(x) = 2α + 1+y′2  1+y′2+z′2

1+y′2+z′2 αmg cos θ 1+y′2                                      (9)

The smaller Elost, the better. So we need to find the extreme of Elost and its condition. However, since the relationship between y and x as well as that between z and x are unknown and need to be determined, the representation of Elost is a functional. To find the optimal shape of the half-pipe, we need to find the functional extreme, but the calculation is too complicated, so we choose numerical method to solve the problem.

Step 4.  The calculation of Whuman When the snowboarder stands up, he does work overcoming the centrifugal force. At high speed, the centrifugal force is huge, so Whuman is considerable and cannot be neglected. The work done by the snowboarder is yt 2 Whuman = ρ m ∙∆h yt′2yt′′ = m ∙∆h                    (10) 3 (1+yt′2) 2

Step 5.  The calculation of “vertical air” At the edge of the half-pipe before the fly, x  is 0. From the Energy Conservation Principle, we have yt′2yt′′ 2 m yt 2 + zt 2 = E0 −Elost xt + mg ∙zt sin θ + 1 m ∙∆h         (11) 3 (1+yt′2) 2

yt yt′ zt′ zt = zt′ ⇒zt = yt′ yt Since

yt′2yt′′ yt 2 = 2 (E0 −Elost xt + mg ∙zt sin θ + m ∙∆h)         (12) 2 3 (1+yt′2) m[1+ zt′ yt′ ] 2

a. If we neglect the air drag during the fly E0−Elost xt +mg ∙zt sin θ+ yt′2yt′′ m∙∆h 3 (1+yt′2) yt 2 1 2 Hf = 2g cos θ = (13) mg ∙cos 2θ[1+(zt′ cos θ yt′)2]

b. If we take the air drag during the fly into account f = β(y 2 + z 2) According to the Second Newton Law:

y g cos θ + β = −g cos θ −β m y 2 + z 2 z m y 2 y = − 2 1 + y z Let y = v. Since dv dt = dv dy ∙dy dt = vdv dy then vdv dy = −g cos θ −β m v2 Separating the variables yields vdv dy = − g cos θ + β m v2 So Hf 0 vdv dy = − g cos θ + β m v2 0 yt

Thus

βyt 2 Hf = m 2β ln⁡(1 + mg cos θ)

Step 6.  Flying distance and energy relationship In order to compare the initial kinetic energy of adjacent two cycles, we have to calculate the decrease of the gravitational potential at the beginning and end of the fly. The duration of the fly can be represented as:

2yt t = g cos θ                           (14) Flying distance is 1 2 g sin θ ∙t2                     (15) Sf = z tt +

The decrease of gravitational potential:

WG = mgSf sin θ                      (16)

Finally, we find it necessary to give an equation to describe the energy conversion and conservation relationship at the beginning and the end of “a cycle”, due to the fact that energy is the key of our analysis. (equation 17) E0 = Elost + mg ∙zt sin θ + WG + Whuman + Ereach        (17)

Hence, from equation 17, we can get the representation of Ereach: Ereach = E0 −Elost − mg ∙zt sin θ −WG −Whuman        (18)

B. Rotation “Vertical air” is not the only judging criteria of a snowboarder’s performance. The total degree of rotation and the level of difficulty are also essential. Hence, it is necessary to discuss the half-pipe shape’s influence on rotation.

Step 1.  Analyzing the Problem As soon as the snowboarder flies into the air, if we neglect the air drag, his angular momentum cannot be changed, so his rotation only depends on the snowboarder himself. By changing his own posture, the snowboarder can do twist, flip or whatever he wants. Thus, since we are discussing the influence of the shape of the half-pipe, we only need to consider the initial angular momentum of the fly. To maximize the twist, we have to maximize the initial angular momentum.

The angular momentum can be disintegrated into three directions----x, y, and z. Let’s represent them with Lx0, Ly0, and Lz0. The shape of the half-pipe can only affect Lz0, while Lx0 and Ly0 are determined by the snowboarder, with the help of the friction of the snow.

Figure 8

(f1 is the friction of the snow and f2 is the air drag)

Therefore, we need to focus on Lz0. The force analysis is in figure 8. Since the angle between N and snowboarder has to be small or the snowboarder will lose balance, the torque of N is comparatively small. So N plays a negligible role in increasing the snowboarder’s Lz0. What’s more, the gravity is exerted on the mass point and the exerting point of f2 can be regarded as near the mass point, so the gravity and f2 are of little help to increase Lz0. Plus, f1 can only make Lz0 smaller. Therefore, Lz0 is the final angular momentum of the snowboarder’s performance on the half-pipe, which has a close relationship with the shape of the half-pipe, to be more specific, the curvature.

From the definition of angular momentum, we have 1 3 𝑙2ω0m                            (19) Lz0 =

(We regard the snowboarder as a stick. ω0 is the angular velocity right before the fly; ρ0 is the radius of curvature of the cross-section of the half-pipe at the edge and the part of the curve that close to the edge; m is the mass of the snowboarder; l is represented in figure 8)

Plus

xt 2+yt 2 ω0 = (20) ρ0

Combining equation 19 and 20 yields

xt 2+yt 2 1 𝑙2m                       (21) Lz0 = 3 ρ0

From equation 21, we can see that the snowboarder should stretch his body as much as possible to increase l (which has nothing to do with the shape of the half-pipe for sure). And to maximize Lz0, ρ0 should be as small as possible and xt 2 + yt 2 should

be as large as possible. Here we still use numerical method to find the optimal half-pipe shape.

Step 2.  Given the initial angular momentum, list and explain some possible tricks (1). Twist of beginners’ level

Figure 9

The angular momentum is along x and y direction. This kind of twist is beginner’s level and doesn’t have much to do with the shape of the half-pipe. Instead, it depends on the snowboarder’s movement right before the fly. So we just skip it here, and discuss it in our extended model.

(2). Flip and double cork

Figure 10

Lz0 alone makes this kind of rotation possible.

(3). Flip->high level twist->flip

Flip 1 Twist

Flip 2

Figure 11

Lx is exerted by the friction of the snow, which depends on the snowboarder’s action right before the fly. In this case we can see that the direction of angular momentum of a twist can also be along z direction.

Numerical Computation

Before numerical computation to obtainElost , the loss of Energy during sliding, and the production of “Vertical Air”, we have to determine the values of some parameters, such as the friction coefficient between the snow and snowboard (α), the drag coefficient of air (β), the mass of the snowboarder (m), and the initial mechanical energy at the beginning of a cycle (E0).

According to H.Yan, P.Liu, and F.Guo[8], the coefficient of kinetic friction between snow and snowboard is generally about 0.03 to 0.2. In addition, J.Chen, R.Li and Z.Guan [9] discovered the friction coefficient to be 0.0312. Thus, we generally assume α to be 0.03 in our discussion about shape of half-pipe.

As N.Yan stated in reference [10], the air drag coefficient is about 0.15.

Since the mass of Shaun White, one of the most outstanding snowboarders in the world, is 63kg, we assume that the mass of a snowboarder is typically 60kg.

Moreover, according to reference [11], the drop-in ramp height should be at least 5.5m and distance from ramp to pipe should be at least 9m. Since the slope angle is about 18°, the potential energy of gravity is: mg ∙ 5.5 + 9 ∙cos 18° ≈8267 J.

As α may not exceed 0.2 (in which case E0 would be 6613 J), we conservatively assume the initial mechanical energy at the beginning of a cycle (E0) to be 7000 J.

To sum up, we assume that : α ≈0.03, β ≈0.15, m ≈60kg, E0 ≈7000 J.

Besides, we need to define y(x) and z(x), the shape of ramp cross-section and the path snowboard chooses respectively. As we assumed before, y(x) is a convex C2 curve, which is symmetric in reality. There is a horizontal flat line (‘Flat’) connecting two parts of the ramp and each part consists of a smooth transition part and possibly vertical part of (‘Vert’).

Figure 12

The path player choose can be represented by z=z(x). As figure below shows, in a simply condition with constant friction, the energy loss will be minimized if z is proportion to τ x , the length of the projection curvature of the three dimensional

= (𝑥, 𝑦 𝑥 , 𝑧 𝑥 )to X-Y plane. Thus, we define the coordinate along z curve 𝑝(𝑥)

axis as z = z τ x  ≈kτ x . Practically, we control z(x) using the location of the

point right before the fly.

Figure 13 Given certain relationship between y(x) and x and between z(x) and x, we used numerical calculus to solve the differential equation (6):

my ′′ x 2 Elost x = m [E0 −Elost τ −mg y cos θ − { α + β −x0 1+y′2  1+y′2+z′2

zsinθ]+αmgcosθ1+y′2+z′21+y′2}dτ (6)

Then we calculate the resulting “vertical air” use both analytical equations and numerical simulation. We solved the problem of “Projectile” and got analytical results. Since we can obtain “vertical air”, duration of Fly and Flying distance more easily by numerical simulation, we also use numerical simulation for later analysis.

of the snowboarder on the ramp and in the air.

8 6

4 2

0 -2

-4 0 10 -20 5 0 -40 -5 -60 -10

To validate our results, we compared analytical results and numerical results:

We assume: width=15m, flat=5m, depth=3.5m, zt =10m, θ=18°, zt =10m. Transition part is standard elliptic, g=9.8m/s2, m=60kg, β =0.15kg/m, according to reference[4][8][9][10][11].

Condition Method Vy Vertical Air Fly Distance Duration of Fly Without Analytical 11.2316m/s 7.1156m 25.5115 2.4101 friction Numerical 11.2316m/s 7.1216m 25.5121 2.4102 Error Ratio 0% 0.084% 0.002% 0.004% With friction Analytical 11.2316m/s 6.9979m -- -- Numerical 11.2316m/s 7.0037m 24.5173 2.3836 Error Ratio 0% 0.083% -- -- Validity

Using recommended width, height, flat length and gradient angle, with other parameters fitting the reality in Snowboard half-pipe game, the resulting maximum Vertical Air is about 7 meters. This result matches the Shaun White’s best performance of and is consistent with the common “Vertical Air” (12 feet~20 feet for men and 6 feet~15 feet for women) in Snowboard half-pipe games.

Sensitivity

As to the sensitivity, we modified parameters by ±10%, and the result supporting that the numerical simulation is robust.

+10% Vertical Air Change -10% Vertical Air Change Percentage Percentage W(Width)~15m 16.5m 5.53% 13.5m -6.13% H(Depth)~3.5m 3.85m 2.50% 3.15m -2.57% B(Flat)~5m 5.50m 0.86% 4.50m -0.87% Zt(Fly Point)~10m 11m 8.18% 9m -8.08%

Extended Model

In the basic model above, we generally neglect the influence of the snowboarder on the flying path, but rather pay most attention to the objective factors. Nevertheless, snowboarder in itself is the key role in this sport, and their diverse performances owe much to the variations among different snowboarders. In this extended model, we take the impact of the snowboarder into account.

1 The direction of velocity

A snowboarder is different from an rigid body in that he can turn, decelerate etc where a small ball or a stick can’t. The direction of a snowboard could be different from that of the snowboarder’s velocity, although this is often not welcomed, since it would slow down the snowboarder. This means, however, that a skilled snowboarder may move in a direction partly determined by himself. This is why we discussed how to choose the ‘best path’ in a given course.

Especially, consider the point right before a fly. From the discussion above, we learnt that the larger zt is, the longer flying distance is. As a result, the cycle distance would be longer, which ultimately results in fewer cycles. However, since a snowboarder must perform 5 to 8 acrobatic tricks in the Winter Olympic Games, fewer cycles are not allowed. Hence, a snowboarder should avoid flying too far. At the same time, however, a larger zt means greater yt’, which, contrarily, is favorable for a higher ‘vertical air’. In that case, a skilled snowboarder may choose to reduce his zt  right before the fly.

To sum up, a skilled snowboarder would choose a path with reasonable zt and reduce his zt  right before the fly while maintaining his yt  or convert the part of kinetic energy in the velocity along z direction into that in y direction.

Here is a detailed analysis about the fly while taking the snowboarder’s influence on zt  into account.

a. Maintaining 𝐲𝐭 Vertical air maintains the same:

E0−Elost xt +mg ∙zt sin θ+ yt′2yt′′ m∙∆h 3 (1+yt′2) yt 2 1 2 Hf = 2g cos θ = (22) mg ∙cos 2θ[1+(zt′ cos θ yt′)2] Flying distance:

1 2yt g cos θ)2                           (23) Sf = 2 g sin θ ∙(

b. Convert the part of kinetic energy in the velocity along z direction into that in y direction.

yt′2yt′′ yt 2 = 2 m [E0 −Elost xt + mg ∙zt sin θ + m ∙∆h]         (24) 3 (1+yt′2) 2 Vertical air:

E0−Elost xt +mg ∙zt sin θ+ yt′2yt′′ m∙∆h 3 (1+yt′2) yt 2 1 2 Hf = 2g cos θ = (25) mg ∙cos 2θ cos θ Flying distance:

1 2yt g cos θ)2                    (26) Sf = 2 g sin θ ∙(

2 Total degree of rotation 𝚯

The snowboarder’s action has a large influence on the total degree of rotation in two ways. First, before starting a fly with acrobatic trick, the snowboarder can make some preparation for the trick. He can create angular momentum along x and y direction by twisting to the direction that he intends to rotate during the fly and acquiring angular momentum along x and y direction with the help of the friction of the snow. Second, during the fly, despite the fact that the angular of momentum cannot be changed, the snowboarder can change his angular velocity by altering his moment of inertia. For instance, he can hold his arms tight from a stretching posture to increase his angular velocity (because of the decrease of moment of inertia), and in turn increase the total degree of rotation (Figure 15). In this process, the mechanical energy is also increased since the snowboarder has done work against the pseudo force petrifugal force.

Figure 15

3 the landing point

In the basic model, we assumed that a snowboarder enter into the half-pipe right at the coping after a fly. Nevertheless, this is often not the case. Usually, a skilled snowboarder would prefer to land on the transition part rather than land at the coping mainly in the consideration of safety and easiness, flying time, and friction.

Firstly, landing on the transition part is much safer and easier than doing so at coping. The latter requires much more precision in landing, or the snowboarder may land on the deck, which leads to an undesirable crash.

A longer flying time can also resulted from landing on the transition, which is favorable since longer flying time means better trick.

Furthermore, as flying in the air avoid the friction from snow, replacing part of movement on the half-pipe with an airborne one can help lessen the decrease of skiing speed.

In a word, landing on the transition part instead of at coping would sometimes be a more advisable choice for a snowboarder.

To sum up, the schema can be represented as the following ‘map’:

Solutions to the problems

Question1:

Determine the shape of a snowboard course (currently known as a “halfpipe”) to maximize the production of “vertical air” by a skilled snowboarder. “Vertical air” is the maximum vertical distance above the edge of the half-pipe.

Answer 1:

We have used numerical method to test how “Vertical air” is affected by other factors: width of the ramp, the gradient angle of the pipe, the path the snowboarder chooses, etc. Optimizing all factors, we got shape of the cross-section of ramp, which maximize the production of “Vertical Air”.

10

5

0

-5 0 10 -20 5 0 -40 -5 -60 -10

Figure 17

Analysis 1:

The goal of this question is to optimize the shape of the course which provides maximum vertical distance above the edge of the half-pipe during the fly. Mathematically, we define following objective function:

max V𝑒𝑟𝑡𝑖𝑐𝑎𝑙𝐴𝑖𝑟 𝑥, 𝑦 𝑥 , 𝑧 𝑥     𝑠. 𝑡.  𝑦= 𝑦 𝑥 , 𝑧= 𝑧 𝑥

The function is determined by the following parameters: W(width), H(depth), B(length of flat bottom), zt (fly point) and transition shape.

There are several factors affecting the shape of course and path. Among them we firstly consider and optimize following dominant variables.

Variables determine y(x) W: The width of the ramp which is the distance between the edges of two sides.

H: the height/depth of the ramp, the perpendicular distance between coping edge and flat bottom.

B: the length of the flat platform at the middle of the ramp.

Transition Shape: the y-x relationship, indicating the shape of transition part connecting ‘Vert’ and flat bottom.

Variables determine z(x) Zt: z value right before the fly, z coordinate along z-axis, which determine sliding path the snowboarder choose.

Zt will determine the z = z τ x  ~kτ x

We assumed the default value of these variables as the table shows and analyze the effect of each variable respectively while maintaining other variables.

W(width) 15m H(height) 3.5m 𝜃 (gradient angle of the 18° B(length of flat bottom) 5m venue, the angle between z axis and ground) 𝑧𝑡(𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝑜𝑓𝑡𝑎𝑟𝑡 𝑝𝑜𝑖𝑛𝑡 𝑜𝑓 𝐹𝑙𝑦) 10m Transition Shape Standard ellipse

 W(width)

relationship between width & VAf relationship between width & Eleave 8.5 7600

7500 8 7400 7.5 7300 7 7200 Eleave VAf 7100 6.5 7000 6 6900 5.5 6800

5 6700 10 15 20 25 10 15 20 25 width width Figure 18 By simulating with numerical method with W (width of ramp) varying from 10 to 25, we can find the wider the ramp is, the faster the snowboarder can speed up before the fly and, consequently, the larger “Vertical Air” is.

 H(height)

relationship between height & Velocityy relationship between height & VerticalAir 9.5 13.5

9 13 8.5 12.5 8 VerticalAir Velocityy 12 7.5

7 11.5 6.5 11 6

10.5 5.5 2 4 6 8 10 12 14 16 18 20 2 4 6 8 10 12 14 16 18 20 height height

velocity along y axis vs. height(right)

From numerical computation, within about 15 meter (possibly the same value of the width), higher ramp can results in higher velocity and larger “Vertical Air”. But when the ramp is higher than 15 meter, the velocity and the “Vertical Air” will decrease with height. Commonly, the height of ramp is around 3 meter to 6 meter, so we can accept that it is advisable to build a high ramp in this range.

 B(length of flat bottom)

relationship between flat & VAf relationship between flat & Eleave 6.8 7400

6.7 7350 6.6

6.5 7300 Eleave VAf 6.4 7250 6.3

6.2 7200 6.1

6 7150 0 1 2 3 4 5 6 0 1 2 3 4 5 6 flat flat

Figure 20

With other parameters fixed to default values, the effects of flat is complex.

Longer flat provides larger “Vertical Air”. But the decreasing 𝐸𝑙𝑒𝑎𝑣𝑒 value means the potential maximum “Vertical Air” is decreased, the “Vertical Air” is affected by the direction the player flies to.

 𝜃 𝑔𝑟𝑎𝑑𝑖𝑒𝑛𝑡 𝑎𝑛𝑔𝑙𝑒 𝑜𝑓 𝑡𝑕𝑒 𝑣𝑒𝑛𝑢𝑒 It is obvious that the steeper the venue is, the faster players can slide. Thus they will overcome gravity for longer time and “fly” higher.

relationship between theta & VAf relationship between theta & Eleave 12 10000 9500 11 9000 10 8500 9 8000 Eleave VAf 8 7500 7000 7 6500 6 6000 5 5500 4 5000 0 5 10 15 20 25 30 35 40 45 0 5 10 15 20 25 30 35 40 45 theta theta

Figure 21

 𝑧𝑡(𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝑜𝑓𝑡𝑎𝑟𝑡 𝑝𝑜𝑖𝑛𝑡 𝑜𝑓 𝐹𝑙𝑦) What path the snowboarder takes, which is defined by Zt in model, plays significant part for “Vertical Air”. As previous work *14+ suggests, steeper path provides the player higher speed, larger chance to fly farther down the pipe, but fewer tricks in a run. Shallower path means cutting straight across and straight up the wall, but provides less momentum and lower speed.

relationship between zlength & VA relationship between zlength & Eleave 10 8500

9 8000

7500 8

7000 Eleave VA 7 6500 6 6000

5 5500

4 5000 0 5 10 15 0 5 10 15 zlength zlength

between 𝐸𝑙𝑒𝑎𝑣𝑒v.s. Zt (right)

Our simulation coincide with this study and shows players’ skills (choose best path) can help them to optmize “Vertical Air”.

The larger zt is, the steeper the path is and more momentum before the fly. But if the path is too steep (zt>5 meter) the player will fly more down the pipe instead of higher above the pipe. Shallower path (zt is smaller than 5 meter) could provide larger “Vertical Air”.

 Global Optimal We enumerate width from 13m to 18m, height from 2 to 6, flat length from 4 to 6, Zt from 0 to 15 and 𝜃 from 15° to 20°. Use the kinetic energy before the fly (𝐸𝑙𝑒𝑎𝑣𝑒) and “Vertical Air” as criteria:

Best parameters for “Vertical Air” defined in the Basic Model, when the snowboarder does not change his velocity direction right before the fly.

𝑊𝑖𝑑𝑡h = 18𝑚, 𝐻𝑒𝑖𝑔h𝑡= 3𝑚, 𝐹𝑙𝑎𝑡= 4𝑚, 𝑍𝑡= 6𝑚, 𝜃= 20° Also, the optimum shape of the course using Gene Algorithm is:

 Transition Shape Among these factors, the shape of transition plays a significant role since the curve directly determines the energy loss caused by friction along the path. We follow the following procedures, including random Generation of convex curves, controlling Splines (3rd) and Gene Algorithm, to find the optimal transition shape.

Define "Controling Points" of the curves

•satisfying the requests for transition part •connecting coping edge of ramp and flat bottom smoothly

Generate sampling points convex curves •The curve is convex to the downwards and second-order differentiable •Use B-Spline, two-point method and three-point method •Become the 1st generation in Gene Algorithm

Define "Gene" •the position of controling points

Define Fitness-Function •the "Vertical Air"  determined by the shape defined by the controling point and the default parameters

Gene-Algorithm •recursivly process •roulette wheel selection •uniform cross-over •random mutation but maintaining convex •optimize the Fitness of "Gene"

Optimize curve •The optimal curve survives from Gene Algorithm

Here we use a random method to generate convex samplings, which smoothly connect two fixed points (the coping edge and bottom edge). We generate the sample points forming convex curve using following method:

𝒈𝒊𝒗𝒆𝒏: h = 0.01, W = width −flat , H = Height, 2 x n = nh, n = 1 … N, N = W h + 1

𝒈𝒐𝒂𝒍: to generate sampling points of  Convex curve as transition part

y = y x → x n , y n

s. t.  y n > 𝑦 n −1 , y 1 = 0, y N = H

𝑴𝒆𝒕𝒉𝒐𝒅: we define k i = y i + 1 −y i , 1 < 𝑖< 𝑁, 𝑠𝑜 𝑘 i > 𝑘 i −1 > 0 N−1 N−1 = H h = y N = H → k(i) k(i) h i=2 i=2 We generate random numbers and use the summation of previous i numbers as k(i).

H After normalized by h, we can acquire k(i). Finally, the locations of sampling points are determined after all their tangent values have determined, and therefore the sampling points of a random convex curve (x(i),y(i)) is acquired.

The result of Gene Algorithm leads to the best curve, which provide maximum “Vertical Air”

0 0.1 0 0.025 0.09 -0.5 -0.5 0.08 0.02 -1 -1 0.07 0.06 0.015 -1.5 -1.5 0.05 -2 -2 0.04 0.01 0.03 -2.5 -2.5 0.02 0.005 -3 -3 0.01 -3.5 0 -3.5 0 -10 -5 0 5 10 0 50 100 -10 -5 0 5 10 0 50 100

(a) (b)

0

-1

-2

-3

-6 -4 -2 0 2 4 6

(c)                          (d)

(a) initial “generation” of curves(blue) in Gene Algorithm and their fitness values (b) finishing “generation” of curves (blue) and their fitness values (c) the shape of the optimized shape of course (d) fitting the resulting curve with 2nd order curve, which ends up into an ellipse

We fit the optimistic curve as second order differentiable curves and it ends up into an ellipse and adding a ‘Vert’ about half meter long. This result matches the previous work claiming the transition should be an ellipse [4].

 Global Optimum To compute the global optimal shape of course, we just set width, height of the ramp and gradient angle to 15m, 3.5m and 18°respectively (recommended value by FIS) and use Gene Algorithm to optimize the entire curve.

10

5

0

-5 0 10 -20 5 0 -40 -5 -60 -10

(a)

Ellipse Fitting for Optimal Shape of Course 0 2 -0.5 1 -1 0 -1.5 -1 -2 -2 -2.5

-3 -3

-3.5 -4 -8 -6 -4 -2 0 2 4 6 8 -8 -6 -4 -2 0 2 4 6

(b) (c)

(a) Course of half-pipe and path of snowboarder (b) The shape of course cross-section (c) Fitting the optimal curve with an ellipse This optimized shape provides largest “Vertical Air”, and it is also close to an ellipse.

Conclusion 1:

Wider and higher ramp, larger gradient angle, g, chosen by skilled snowboarder all contribute to “Vertical Air”.

While the width and height of the course is fixed, the shape of the course is close to an ellipse.

Sometimes, a short ‘Vert’ and ‘Flat’ is also preferred.

Question2:

Tailor the shape to optimize other possible requirements, such as maximum twist in the air.

Answer2:

We have tailored the shape of the course and optimize degree of rotation which correlates to following requirements respectively.

1) Optimize total duration of fly

2) Optimize initial angular momentum along z-direction

3) Optimize total degree of rotation

1) Optimize total duration of fly

Default Values W(width) 15m H(height) 3.5m 𝜃 (gradient angle of the venue, the 18° B(length of flat bottom) 5m angle between z axis and ground) 𝑧𝑡(𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝑜𝑓𝑡𝑎𝑟𝑡 𝑝𝑜𝑖𝑛𝑡 𝑜𝑓 𝐹𝑙𝑦) 10m Transition Shape Standard ellipse

Using the parameters as above table shows, we got following results concerning the factors to duration of fly, which are also known as “air time”.

relationship between width & FlyTime/s relationship between flat & FlyTime/s 3 3 2.95 2.95 2.9 2.9 2.85 2.85 2.8 2.8 FlyTime/s FlyTime/s 2.75 2.75 2.7 2.7 2.65 2.65 2.6 2.6 2.55 2.55 2.5 2.5 12 14 16 18 20 22 24 26 0 1 2 3 4 5 6 width flat

(a)                               (b) relationship between zlength & FlyTime/s relationship between height & FlyTime/s 3 3 2.95 2.95 2.9 2.9 2.85 2.85 2.8 2.8 FlyTime/s FlyTime/s 2.75 2.75 2.7 2.7 2.65 2.65 2.6 2.6 2.55 2.55 2.5 2.5 0 5 10 15 2 2.5 3 3.5 4 4.5 5 5.5 6 zlength height

(c)                              (d)

relationship between theta & FlyTime/s 4.5

4

3.5 FlyTime/s 3

2.5

2 0 5 10 15 20 25 30 35 40 45 theta

(e)

height(d) and gradient angle 𝜃 (e)

Simulation results show that the duration of fly (tf) is almost positive linear to ramp width, ramp height and the flat length. Duration of fly reaches locally optimum when zt is around 6 meter, indicating that snowboarders’ choice for path can help them to fly for a longer time. Moreover, the larger the gradient angle 𝜃 is, the longer the fly lasts.

Conclusion for (1):

Here we enumerate width from 13 to 18, height from 2 to 6, flat length from 4 to 6, zt from 0 to 15 and 𝜃 from 15° to 20° to optimize the fly time and obtain the optimal shape of course:

Width = 18m, Height = 5m, Flat = 6m, zt = 4m, 𝜽 = 20° tf = 2.749s

2) Optimize initial angular momentum along z-axis

As we have computed before, xt 2 + yt 2 𝑙2m Lz0 = 3ρ0 Thus, the transition shape is dominant so we use Gene Algorithm to maximize the production of angular momentum:

Conclusion for (2):

We use the parameter recommended by FIS, which also match the optimal parameters from our previous analysis of velocity before fly

W(width) 18m H(height) 3.5m 𝜃 (gradient angle of the 18° B(length of flat bottom) 5m venue, the angle between z axis and ground) 𝑧𝑡(𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝑜𝑓𝑡𝑎𝑟𝑡 𝑝𝑜𝑖𝑛𝑡 𝑜𝑓 𝐹𝑙𝑦) 10m Transition Shape To Be Optimized

Using Gene Algorithm, we obtain the optimal shape as follows:

Ellipse Fitting of Optimal Shape of Course for Angular Momentum 0 3 -0.5 2 -1 1 -1.5 0 -2 -1 -2.5

-2 -3

-3 -3.5

-4 -4 -8 -6 -4 -2 0 2 4 6 8 -8 -6 -4 -2 0 2 4

and fitting the shape with 2nd order curve (right)

After fitting with second order curve, we found it is also closed to ellipse. And this curve is tailored from the other optimal curve for “Vertical Air” in question 1. The “Vert” and “Flat” is much shorter. This result makes sense since “Vert” and a long “Flat” will result in large (actually infinite) radius of curvature.

3) Optimize total degree of rotation

Plus, the total degree of rotation also is affect by duration of fly.

Θ = 𝜔𝑡𝑓 and 𝜔∝𝐿0

So, we use Gene Algorithm to optimize the shape of the course with recommended width (15m) and height (3.5m) of ramp, in order to obtain largest production of initial angular momentum and duration of fly.

Conclusion for 3):

The resulting optimum of Gene Algorithm is shown below.

0

-0.5 10 -1 5 -1.5

0 -2

-2.5 -5 0 10 -3 -20 5 0 -40 -5 -3.5 -60 -8 -6 -4 -2 0 2 4 6 8 -10

and the course of optimal pipe and the path of snowboarder (right)

This curve can also be fitted with second order curve, which is an ellipse as well.

Ellipse Fitting of Optimal Shape of Course for Total Degree of Rotation 3

2

1

0

-1

-2

-3

-4 -8 -6 -4 -2 0 2 4

Tailor the course

We have also modified the objective function and implemented Gene Algorithm for the tradeoff between “Vertical Air” and Total Degree of Rotation. As the perception model[9] and automated scoring system[10], developed by Harding JW, etc, has shown, the overall performance of half-pipe snowboard can be treated as a complex combination of “Vertical Air”, Average Air Time(AAT) and Average Degree of Rotation (ADR). They also put forward an equation to predict score of snowboarder automatically.

Predicted Score = 11.424AAT + 0.013ADR −2.223

This function is justified empirically and also makes good sense. (As we have derived before, air time (flying time) is almost proportion to the square root of “Vertical Air” in the motion of Projectile, so they can be regarded as a single criterion) We set objective function in Gene Algorithm to become the “Predicted Score”. In this way, we are able to find the optimal shape of course, as shown below. It enjoys the characteristics of previous optimized shapes based on different objective functions, which may provide the eclectically best snowboard performance to certain extent.

Fitting with 2nd order curves, we found this curve is perfectly fitting by two ellipse which fit optimal curves for “vertical air” and total degree of rotation respectively. Judging by the formula of predicted score, this course could get more than 46, supporting the validity of this combined criterion.

0 8 6 -0.5 4 -1 2 0 -1.5 -2

0 -2 -10 -2.5 -20 -3 -30 -40 -3.5 5 -8 -6 -4 -2 0 2 4 6 8 0 -50 -5

(a)                             (b)

3 Vertical Air Optimal Shape for Scoring System Total Degree Hybrid Scoring 2 Fit 1 Fit 2 1

0

-1

-2

-3

-4 -8 -6 -4 -2 0 2 4 6 (c)

(a) Course and path (b) the optimal shape of the course, judging by eclectic scoring (c) Fitting the resulting optimum with 2nd order curves.

Question3:

What tradeoffs may be required to develop a “practical” course?

Answer 3:

a. Radius of Curvature The radius of curvature of the half-pipe cross-section cannot be too small, or the snow may fall off[12]. And due to the fact that the snowboard is more than one meter long, it is obvious that a too small radius of curvature is dangerous and infeasible.

b. Flat bottom Since the 1980s, half-pipes have had extended flat ground (the flat bottom) added between the quarter-pipes; the original-style half-pipes have become deprecated. The flat ground gives the athlete time to regain balance after landing and more time to prepare for the next trick.[1]

Moreover, according to our numerical computation, when a half-pipe has wider flat bottom, Ereach and Eleave decreases, whereas the duration of fly, yt  and vertical air increases. The change in number of cycles is negligible.

c. Ereach Ereach represents the final kinetic energy of a cycle, as well as the E0 of the next cycle. Considering that the snowboarder experiences more than one cycle, it is not wise to chase a higher jump at the cost of less Ereach .

According to our numerical computation, the wider the course is, the larger the vertical air is. However, wider course leads to lower final kinetic energy (Ereach), which is unwelcomed. It is similar with the height of the half-pipe: as long as height is less than width, higher course results in larger vertical air while less Ereach. And flat is also has the same effect here (as shown in Figure 30).

Therefore, the half-pipe should not be too wide, too high or too flat.

width Vs VerticalAir width Vs Ereach 4 1.39 x 10 9.9

9.8 1.38 9.7 1.37 9.6 VerticalAir 1.36 Ereach 9.5

9.4 1.35 9.3 1.34 9.2 1.33 9.1

9 1.32 13 14 15 16 17 18 13 14 15 16 17 18 width width height Vs Ereach height Vs VerticalAir 4 1.44 x 10 10.2 10 1.42 9.8 1.4 9.6 VerticalAir 9.4 1.38 Ereach 9.2 1.36 9

8.8 1.34 8.6 1.32 8.4

1.3 8.2 1 2 3 4 5 6 1 2 3 4 5 6 height height

flat Vs Ereach flat Vs VerticalAir 4 1.405 x 10 9.45

1.4 9.4 1.395 9.35 1.39 9.3 VerticalAir 1.385 Ereach 9.25 1.38 9.2 1.375 9.15 1.37 9.1 1.365 9.05 1.36

1.355 9 0 1 2 3 4 5 6 0 1 2 3 4 5 6 flat flat Figure 30

d. number of cycles In the Winter Olympic Games, a snowboarder must perform 5 to 8 acrobatic tricks in a run. Thus, a snowboarder should complete 5 to 8 cycles in the half-pipe’s 110m extent.

From the numerical computation above, it can be learnt that both vertical air and Ereach would become larger if 𝜃 (the angle between z axis and the horizontal plane) increases. Nonetheless, since Sf (the displacement along z direction during the fly) increases as 𝜃 increases, a snowboarder would find it difficult to perform enough acrobatic tricks on a very steep half-pipe.

Hence, 𝜃 should not be too large.

Strength and Weakness

 The model describes the entire proceeding of movement in a detailed manner, which pertains to intricate correlation between many physical quantities and is well-organized.

 Precise numerical computation.  The results generated by numerical computation and the empirical data are in agreement, lending support to the model and the corresponding computer codes.  The model takes the subjective influence of snowboarders into account and notes the difference among them.  We established an objective evaluating function to compare different shapes of courses.  We analyzed local optimal course (in order to learn the individual impact of the parameters) as well as global optimal course (so as to shed light on the design of a half-pipe), and obtained numerical solution of them.

 The model does not provide analytic solution of optimal course.  The model does not take the detailed mechanical characteristics and the on-snow performance of snowboards into account.
