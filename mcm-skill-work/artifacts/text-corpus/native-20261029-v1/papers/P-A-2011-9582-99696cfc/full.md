# P-A-2011-9582-99696cfc

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team # 9582

<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
Page 1 of 34

<!-- b000004 | title | pages [1] -->
A half-blood half-pipe, a perfect performance

<!-- b000005 | heading | pages [1] -->
Summary

<!-- b000006 | prose | pages [1] -->
Our basic model can be divided into two parts. The first part is to find a half-pipe shape which can maximize “Vertical Air”; in the second part, we adapt the shape to maximize the possible total angle of rotation. In the extended model, we analyze the snowboarder’s subjective influence on “Vertical Air” and the total degree of rotation. Finally, we discuss the feasibility and the trade-off of building a practical course.

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
The major assumption is that the resistance includes the friction of snow and air drag. The former is proportional to the normal force and the latter is proportional to the square of velocity. Plus, the snowboarder is perpendicular to the tangential surface of the course at his locus during his movement on the half-pipe. The variables of our model include: coordinate variables x, y, z, normal force N, resistance f, snowboarder’s mass m, mechanical energy lost due to friction of the snow and air drag Elost, vertical air Hf, and the initial angular momentum of the fly L0.

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | prose | pages [1] -->
In the first part of our basic model, we obtain a differential equation of Elost based on force analysis and Energy Conservation. Then we derive the representation of Elost by solving the equation, which is a functional. Thus we calculate the representation of “Vertical Air” by analyzing the projectile motion. In the second part of the basic model, we derive the representation of the initial angular momentum before the fly, and discuss the factors influencing it. In our extended model, we calculate the “Vertical Air” when taking the snowboarder’s subjective influence into account.

<!-- b000011 | furniture | pages [1] -->


<!-- b000012 | prose | pages [1] -->
We use numerical method to solve the model and compare analytical results with reality and validate our method to be correct and robust. We analyzed the effects of factors such as width, height and gradient angle of half-pipe on “vertical Air” by controlling other factors, and found that wider, steeper course with proper depth and the best path chosen by a skilled snowboarder are preferred to obtain locally larger “vertical air”. Using Gene Algorithm, we globally optimized the course shape to provide largest “vertical air” and total degree of rotation. There is a trade-off between maximum “vertical air” and maximum rotation. Implementing a hybrid scoring system as the objective function, we optimize the course shape to a “half-blood” shape that would provide the eclectically best snowboard performance. Furthermore, we take practical problems into consideration and provide answers to more questions such as what roles the flat bottom and “vert” play in reality.

<!-- b000013 | furniture | pages [1] -->


<!-- b000014 | prose | pages [1] -->
We finely model the entire complicated proceeding and give numerical solution of optimal course, and establish an objective evaluating function to analyze local and global optical course. Diverse subjective influence of snowboarders is also considered. Yet, the model hasn't provided analytic solution of optimal course.

<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | furniture | pages [2] -->
Team # 9582

<!-- b000017 | furniture | pages [2] -->


<!-- b000018 | furniture | pages [2] -->
Page 2 of 34

<!-- b000019 | heading | pages [2] -->
Background

<!-- b000020 | prose | pages [2] -->
A half-pipe is the venue in which gravity extreme sports such as snowboarding, skateboarding are hold [1]. It usually consists of two concave ramps (including a transition and a vert), topped by copings and decks, facing each other across a transition as shown in Figure 1 [1]. The sport half-pipe snowboarding has been a part of the Winter Olympic competition program since the 2002 Winter Olympic Games held in Nagano, Japan [2]. In the Olympic half-pipe, the riders give two runs, which is a combination of tricks including Straight airs, Grabs, Spins, Flips and Inverted Rotations, etc.

<!-- b000021 | furniture | pages [2] -->


<!-- b000022 | prose | pages [2] -->
No explicit analysis of the ‘best’ shape of a half-pipe is found. However, it is usually accepted that the half-pipe is 100 to 150 meters long, 17 to 19.5 meters wide and has a height of 5.4 to 6.5 meters (from floor to crown). The slope angle is 16 to 18.5 degrees [3] .In addition, the Federation Internationale de Ski (FIS) recommended that the Width(W), Height(H), Transition(T) and the Bottom Flat(B) could be 15m, 3.5m, 5m, 5m, respectively (as Shown in Figure 2[4]).

<!-- b000023 | furniture | pages [2] -->


<!-- b000024 | prose | pages [2] -->
Half-pipe snowboarding is currently judged in competition using subjective measures. Still, there is strong community perception that air-time and degree of rotation play a major role in half-pipe competition success [5][6]. Moreover, researches such as Jason William Harding, Colin Gordon Mackintosh, David Thomas Martin1, Allan Geoffrey Hahn5 and Daniel Arthur James [1][7] have attempted to invite objective analysis into the scoring system. According to them, the air time and the total degree of rotation are the two most critical evaluating criterions.

<!-- b000025 | furniture | pages [2] -->


<!-- b000026 | caption | pages [2] -->
Figure 1 half-pipe

<!-- b000027 | furniture | pages [2] -->


<!-- b000028 | prose | pages [2] -->
Figure 2

<!-- b000029 | furniture | pages [2] -->


<!-- b000030 | furniture | pages [3] -->
Team # 9582

<!-- b000031 | prose | pages [3] -->
Terminology & Definition

<!-- b000032 | furniture | pages [3] -->


<!-- b000033 | furniture | pages [3] -->


<!-- b000034 | furniture | pages [3] -->
Page 3 of 34

<!-- b000035 | prose | pages [3] -->
A cycle: the start of “a cycle” is the moment when the snowboarder reaches the edge of the half-pipe after a fly, and the end of “a cycle” is the next start Fly: the part of the movement when the snowboarder is airborne Flying distance (Sf): the displacement along z direction during the fly Flying time (tf): the duration of the fly Cycle distance (Sc): the displacement along z direction during a cycle

<!-- b000036 | furniture | pages [3] -->


<!-- b000037 | heading | pages [3] -->
Assumptions

<!-- b000038 | prose | pages [3] -->
a. The cross-section of the half-pipe have to be a curve which is convex to the

<!-- b000039 | prose | pages [3] -->
downwards (U shape), and the curve should be second-order derivable at every point except for the endpoints. b. The snowboarder keeps a crouching position during the whole course of his

<!-- b000040 | prose | pages [3] -->
performance on the half-pipe, and he stands up to gain speed right at the edge of the half-pipe before the fly. c. Neglect the rotational kinetic energy of the snowboarder before considering the

<!-- b000041 | prose | pages [3] -->
twist performance of him. d. The friction of the snow is proportional to the normal force of the snow exerted

<!-- b000042 | prose | pages [3] -->
on the snowboarder while has nothing to do with velocity (that is, the angle between the direction of the snowboard and that of snowboarder’s velocity is constant.), and the coefficient is α. Air drag is proportional to the square of the velocity, and the coefficient is β. e. The snowboarder’s body is perpendicular to the tangential surface of the

<!-- b000043 | prose | pages [3] -->
half-pipe at the locus of the snowboarder during his movement on the half-pipe. f. When considering the half-pipe shape in the model, neglect its mechanical

<!-- b000044 | prose | pages [3] -->
feasibility for the snow and the snowboard. (We will discuss it in the section concerning ‘practical’ course instead) g. The force exerted on board can be considered as acting on the center of the

<!-- b000045 | prose | pages [3] -->
board. h. We neglect the influence of natural factors such as uneven sunshine (which may

<!-- b000046 | prose | pages [3] -->
result from an East or West orientation) , altitude, etc.

<!-- b000047 | furniture | pages [3] -->


<!-- b000048 | prose | pages [3] -->
Parameters

<!-- b000049 | prose | pages [3] -->
Parameter

<!-- b000050 | furniture | pages [3] -->


<!-- b000051 | prose | pages [3] -->
x, y, z Coordinate variables x , y , z The velocities in the direction of x, y, z respectively

<!-- b000052 | prose | pages [3] -->
y’, y’’

<!-- b000053 | prose | pages [3] -->
∂2y

<!-- b000054 | prose | pages [3] -->
∂y

<!-- b000055 | prose | pages [3] -->
∂x ,

<!-- b000056 | prose | pages [3] -->
∂x2 z’ ∂z

<!-- b000057 | prose | pages [3] -->
∂x

<!-- b000058 | prose | pages [3] -->
Parameter

<!-- b000059 | furniture | pages [3] -->


<!-- b000060 | prose | pages [3] -->
s The length of the path

<!-- b000061 | prose | pages [3] -->
E0 The initial mechanical energy at the beginning of a cycle

<!-- b000062 | prose | pages [3] -->
Eleave the kinetic energy right before the fly

<!-- b000063 | prose | pages [3] -->
Ereach the kinetic energy at the end of the fly

<!-- b000064 | furniture | pages [4] -->
Team # 9582

<!-- b000065 | prose | pages [4] -->
N Normal force of the snow exerted on the snowboarder

<!-- b000066 | prose | pages [4] -->
f The friction of the snow + air drag

<!-- b000067 | prose | pages [4] -->
m The mass of the snowboarder

<!-- b000068 | prose | pages [4] -->
The angle between z axis and θ the horizontal plane

<!-- b000069 | prose | pages [4] -->
∆h The rise of the mass point of the snowboarder when he stands up from a crouching position.

<!-- b000070 | prose | pages [4] -->
Elost The mechanical energy lost due to friction of the snow and air drag

<!-- b000071 | prose | pages [4] -->
Hf Vertical air

<!-- b000072 | furniture | pages [4] -->


<!-- b000073 | furniture | pages [4] -->


<!-- b000074 | furniture | pages [4] -->


<!-- b000075 | furniture | pages [4] -->
Page 4 of 34

<!-- b000076 | prose | pages [4] -->
Whuman Work done by the snowboarder at the edge of half-pipe when he stands up

<!-- b000077 | prose | pages [4] -->
WG the decrease of the gravitational potential during the fly The friction coefficient between α the snow and snowboard

<!-- b000078 | prose | pages [4] -->
Drag coefficient of air β

<!-- b000079 | prose | pages [4] -->
Radius of curvature at a certain ρ point of the cross-section of the half-pipe

<!-- b000080 | prose | pages [4] -->
x, y, z, y’, z’, y , z , y’’ right before

<!-- b000081 | prose | pages [4] -->
xt, yt, zt, yt’, zt’, yt ,

<!-- b000082 | prose | pages [4] -->
the fly

<!-- b000083 | prose | pages [4] -->
zt , yt’’

<!-- b000084 | furniture | pages [4] -->


<!-- b000085 | furniture | pages [4] -->


<!-- b000086 | furniture | pages [4] -->


<!-- b000087 | furniture | pages [4] -->


<!-- b000088 | furniture | pages [4] -->


<!-- b000089 | furniture | pages [4] -->


<!-- b000090 | furniture | pages [4] -->


<!-- b000091 | caption | pages [4] -->
Figure 3 the build of Cartesian coordinate

<!-- b000092 | furniture | pages [4] -->


<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | caption | pages [4] -->
Figure 3 shows the definition of the coordinate variables x, y, z. Among the

<!-- b000095 | prose | pages [4] -->
coordinate variables, x is the free variable, while y and z are functions of x depending of the shape of the half-pipe and path of the snowboarder, which can also be represented as y(x) and z(x). The relationship between y and x depends on the shape of the half-pipe, while the relationship between z and x depends on the path chosen by the snowboarder.

<!-- b000096 | furniture | pages [4] -->


<!-- b000097 | heading | pages [4] -->
Basic Model

<!-- b000098 | heading | pages [4] -->
Model overview

<!-- b000099 | furniture | pages [5] -->
Team # 9582

<!-- b000100 | furniture | pages [5] -->


<!-- b000101 | furniture | pages [5] -->
Page 5 of 34

<!-- b000102 | caption | pages [5] -->
Figure 4 shows a simplified outline of our basic model

<!-- b000103 | furniture | pages [5] -->


<!-- b000104 | prose | pages [5] -->
Figure 4

<!-- b000105 | furniture | pages [5] -->


<!-- b000106 | caption | pages [5] -->
Figure 5 is the yield of our study in the following part of this artical. Here, we use it to

<!-- b000107 | prose | pages [5] -->
help give an overview of our model.

<!-- b000108 | furniture | pages [5] -->


<!-- b000109 | furniture | pages [5] -->


<!-- b000110 | caption | pages [5] -->
Figure 5. the path of snowboarder on the course (red) and in the air (blue: without

<!-- b000111 | prose | pages [5] -->
air drag, green: with air drag), which is an entire “cycle”.

<!-- b000112 | furniture | pages [5] -->


<!-- b000113 | prose | pages [5] -->
“A cycle” can be devided into two parts. The first part is the movement on the half-pipe, and the second part is the airbourn performance. In the first part, since our concern is the final velocity, focusing on the convertion and conservation is the most efficient way. Hence the lost of mechanical energy Elost is the key of our study in this part. Due to the fact that Elost is caused by the resistance of snow and air, we can derive an equation about Elost with the help of integration after we derive the representation of resistance f by force analyzing. Then we transform the equation into a differential equation and solve it, which yield the representation of Elost. Since the shape of the half-pipe and the path chosen by the snowboarder need to be determined, the represetation of Elost is a functional. Another thing that cannot be neglected is the contribution of the snowboarder to the increase of mechanical energy at the end of the first part. This part of work is done by streching his body (standing up) and doing work against the pseudo force petrifugal force.

<!-- b000114 | furniture | pages [5] -->


<!-- b000115 | prose | pages [5] -->
As to the second part, to derive the “vertical air”, the Second Newton Law is applied. If we neglect the air drag during the fly (actually the numerical method in later part

<!-- b000116 | furniture | pages [6] -->
Team # 9582

<!-- b000117 | furniture | pages [6] -->


<!-- b000118 | furniture | pages [6] -->


<!-- b000119 | furniture | pages [6] -->
Page 6 of 34

<!-- b000120 | prose | pages [6] -->
of this artical proves that the air drag during the fly is neglegibal), we can calculate “vertical air”, the duration of the fly, flying distance, gravitational potential decrease, etc. Since we don’t know whether air drag is neglegibal before we compare the results of the calculation considering and neglecting the air drag, we also have to make a calculation taking the air drag into account.

<!-- b000121 | furniture | pages [6] -->


<!-- b000122 | prose | pages [6] -->
Next, the airbourn rotation of the snowboarder is discussed. Since the shape of half-pipe directaly influnces the initial angular momentum of the snowboarder, and the angular momentum is the only thing that cannot be changed during the flight (the snowboarder can do work by changing his posture to increase the mechanical energy), the relationship between the half-pipe shape and the initial angular momentum is the key of our discussion here. After deriving the representation of the initial angular momentum, we can find the optimal shape of the half-pipe.

<!-- b000123 | furniture | pages [6] -->


<!-- b000124 | heading | pages [6] -->
The Model

<!-- b000125 | prose | pages [6] -->
A. Vertical air Step 1.  Force analysis (figure 6)

<!-- b000126 | furniture | pages [6] -->


<!-- b000127 | furniture | pages [6] -->


<!-- b000128 | furniture | pages [6] -->


<!-- b000129 | furniture | pages [6] -->


<!-- b000130 | furniture | pages [6] -->


<!-- b000131 | caption | pages [6] -->
Figure 6  Force Analysis

<!-- b000132 | furniture | pages [6] -->


<!-- b000133 | furniture | pages [7] -->
Team # 9582

<!-- b000134 | furniture | pages [7] -->


<!-- b000135 | furniture | pages [7] -->


<!-- b000136 | furniture | pages [7] -->
Page 7 of 34

<!-- b000137 | prose | pages [7] -->
There are three kinds of force acted on the snowboarder, which are gravity mg, normal force N and resistance f. Resistance includes air drag and the friction between the snow and snowboard. N balances with the gravity’s and the pseudo force centrifugal force’s projection in the normal direction of the half-pipe surface at this point. And f causes the loss of mechanical energy.

<!-- b000138 | furniture | pages [7] -->


<!-- b000139 | prose | pages [7] -->
Among the forces, resistance can be represented as: f = αN + β(x 2 + y 2 + z 2)

<!-- b000140 | prose | pages [7] -->
= αN + β(1 + y′2 + z′2)x 2                        (1)

<!-- b000141 | prose | pages [7] -->
Next consider the expression of normal force. Only the part of centripetal acceleration which parallels the direction of N needs to be considered when we calculate the Normal force. Thus we get the expression eq.2.

<!-- b000142 | prose | pages [7] -->
3

<!-- b000143 | prose | pages [7] -->
(1+y′2)

<!-- b000144 | prose | pages [7] -->
2

<!-- b000145 | prose | pages [7] -->
ρ =

<!-- b000146 | furniture | pages [7] -->


<!-- b000147 | prose | pages [7] -->
y′′

<!-- b000148 | prose | pages [7] -->
x 2+y 2

<!-- b000149 | prose | pages [7] -->
N =

<!-- b000150 | prose | pages [7] -->
m + ρ

<!-- b000151 | furniture | pages [7] -->


<!-- b000152 | prose | pages [7] -->
mgcos θ

<!-- b000153 | prose | pages [7] -->
1+y′2

<!-- b000154 | prose | pages [7] -->
= (y′′x 2 + g cos θ)

<!-- b000155 | prose | pages [7] -->
Path length unit can be represented as:

<!-- b000156 | prose | pages [7] -->
m

<!-- b000157 | prose | pages [7] -->
1+y′2                       (2)

<!-- b000158 | prose | pages [7] -->
ds =  1 + y′2 + z′2 dx                          (3)

<!-- b000159 | furniture | pages [7] -->


<!-- b000160 | prose | pages [7] -->
Step 2.  According to the Energy Conservation Principle, we have equation 4.

<!-- b000161 | prose | pages [7] -->
2 m 1 + y′2 + z′2 x 2 = E0 −Elost −mg y cos θ −z sin θ          (4)

<!-- b000162 | prose | pages [7] -->
1

<!-- b000163 | furniture | pages [7] -->


<!-- b000164 | prose | pages [7] -->
Then we have

<!-- b000165 | prose | pages [7] -->
x 2 =

<!-- b000166 | prose | pages [7] -->
2

<!-- b000167 | prose | pages [7] -->
m 1+y′2+z′2  E0 −Elost −mg y cos θ −z sin θ              (5)

<!-- b000168 | furniture | pages [7] -->


<!-- b000169 | prose | pages [7] -->
Step 3.  Now we can calculate the expression of Elost.

<!-- b000170 | prose | pages [7] -->
x Elost (x) = f ∙ds

<!-- b000171 | furniture | pages [7] -->


<!-- b000172 | prose | pages [7] -->
−x0

<!-- b000173 | prose | pages [7] -->
[αN 1 + y′2 + z′2 + β(1 + y′2 + z′2)

<!-- b000174 | prose | pages [7] -->
x

<!-- b000175 | prose | pages [7] -->
=

<!-- b000176 | prose | pages [7] -->
−x0

<!-- b000177 | prose | pages [7] -->
my ′′

<!-- b000178 | prose | pages [7] -->
x

<!-- b000179 | prose | pages [7] -->
2

<!-- b000180 | prose | pages [7] -->
3 2 ∙τ 2]dτ

<!-- b000181 | furniture | pages [7] -->


<!-- b000182 | prose | pages [7] -->
m E0 −Elost τ −mg y cos θ − z sin θ  +

<!-- b000183 | prose | pages [7] -->
= { α

<!-- b000184 | prose | pages [7] -->
+ β

<!-- b000185 | prose | pages [7] -->
−x0

<!-- b000186 | prose | pages [7] -->
1+y′2  1+y′2+z′2

<!-- b000187 | prose | pages [7] -->
αmgcosθ1+y′2+z′21+y′2}dτ (6)

<!-- b000188 | prose | pages [7] -->
The expression of Elost in equation 6 is an integral with variable upper limit. And τ, representing the x coordinate, is the integral variable.

<!-- b000189 | furniture | pages [8] -->
Team # 9582

<!-- b000190 | furniture | pages [8] -->


<!-- b000191 | furniture | pages [8] -->


<!-- b000192 | furniture | pages [8] -->


<!-- b000193 | furniture | pages [8] -->
Page 8 of 34

<!-- b000194 | prose | pages [8] -->
Differentiating both sides of equation 6, and solving the out-coming linear ordinary differential equation of the first order, we have

<!-- b000195 | prose | pages [8] -->
x a(τ) dτ Elost = e ∗ −x0

<!-- b000196 | prose | pages [8] -->
In which

<!-- b000197 | prose | pages [8] -->
a(x) = − 2α

<!-- b000198 | prose | pages [8] -->
x x x −a(τ) dτ b(ξ) ∙e dξ               (7) −x0 −x0 −x0

<!-- b000199 | prose | pages [8] -->
y′′ y′′

<!-- b000200 | prose | pages [8] -->
2β

<!-- b000201 | prose | pages [8] -->
+

<!-- b000202 | prose | pages [8] -->
m                     (8)

<!-- b000203 | prose | pages [8] -->
1+y′2  1+y′2+z′2

<!-- b000204 | prose | pages [8] -->
y′′

<!-- b000205 | prose | pages [8] -->
2β

<!-- b000206 | prose | pages [8] -->
m  E0 −mg y cos θ −z sin θ  +

<!-- b000207 | prose | pages [8] -->
b(x) = 2α

<!-- b000208 | prose | pages [8] -->
+

<!-- b000209 | prose | pages [8] -->
1+y′2  1+y′2+z′2

<!-- b000210 | prose | pages [8] -->
1+y′2+z′2

<!-- b000211 | prose | pages [8] -->
αmg cos θ

<!-- b000212 | prose | pages [8] -->
1+y′2                                      (9)

<!-- b000213 | prose | pages [8] -->
The smaller Elost, the better. So we need to find the extreme of Elost and its condition. However, since the relationship between y and x as well as that between z and x are unknown and need to be determined, the representation of Elost is a functional. To find the optimal shape of the half-pipe, we need to find the functional extreme, but the calculation is too complicated, so we choose numerical method to solve the problem.

<!-- b000214 | furniture | pages [8] -->


<!-- b000215 | prose | pages [8] -->
Step 4.  The calculation of Whuman When the snowboarder stands up, he does work overcoming the centrifugal force. At high speed, the centrifugal force is huge, so Whuman is considerable and cannot be neglected. The work done by the snowboarder is

<!-- b000216 | prose | pages [8] -->
yt 2

<!-- b000217 | prose | pages [8] -->
Whuman =

<!-- b000218 | prose | pages [8] -->
=

<!-- b000219 | furniture | pages [8] -->


<!-- b000220 | prose | pages [8] -->
Step 5.  The calculation of “vertical air”

<!-- b000221 | prose | pages [8] -->
ρ m ∙∆h

<!-- b000222 | prose | pages [8] -->
yt′2yt′′

<!-- b000223 | prose | pages [8] -->
m ∙∆h                    (10) 3

<!-- b000224 | prose | pages [8] -->
(1+yt′2)

<!-- b000225 | prose | pages [8] -->
2

<!-- b000226 | prose | pages [8] -->
At the edge of the half-pipe before the fly, x  is 0. From the Energy Conservation Principle, we have

<!-- b000227 | prose | pages [8] -->
yt′2yt′′ 2 m yt 2 + zt 2 = E0 −Elost xt + mg ∙zt sin θ +

<!-- b000228 | prose | pages [8] -->
1

<!-- b000229 | furniture | pages [8] -->


<!-- b000230 | prose | pages [8] -->
yt

<!-- b000231 | prose | pages [8] -->
yt′

<!-- b000232 | prose | pages [8] -->
m ∙∆h         (11) 3

<!-- b000233 | prose | pages [8] -->
(1+yt′2)

<!-- b000234 | prose | pages [8] -->
2

<!-- b000235 | prose | pages [8] -->
zt′

<!-- b000236 | prose | pages [8] -->
zt′ ⇒zt =

<!-- b000237 | prose | pages [8] -->
zt =

<!-- b000238 | prose | pages [8] -->
Since

<!-- b000239 | prose | pages [8] -->
yt 2 =

<!-- b000240 | prose | pages [8] -->
2

<!-- b000241 | prose | pages [8] -->
yt′ yt

<!-- b000242 | prose | pages [8] -->
yt′2yt′′

<!-- b000243 | prose | pages [8] -->
(E0 −Elost xt + mg ∙zt sin θ +

<!-- b000244 | prose | pages [8] -->
2

<!-- b000245 | prose | pages [8] -->
m[1+ zt′

<!-- b000246 | prose | pages [8] -->
yt′

<!-- b000247 | prose | pages [8] -->
]

<!-- b000248 | prose | pages [8] -->
a. If we neglect the air drag during the fly

<!-- b000249 | prose | pages [8] -->
m ∙∆h)         (12) 3

<!-- b000250 | prose | pages [8] -->
(1+yt′2)

<!-- b000251 | prose | pages [8] -->
2

<!-- b000252 | caption | pages [8] -->
Figure 7 clearly shows that the "vertical air" can be represented as:

<!-- b000253 | furniture | pages [9] -->
Team # 9582

<!-- b000254 | furniture | pages [9] -->


<!-- b000255 | furniture | pages [9] -->


<!-- b000256 | furniture | pages [9] -->
Page 9 of 34

<!-- b000257 | prose | pages [9] -->
E0−Elost xt +mg ∙zt sin θ+ yt′2yt′′

<!-- b000258 | prose | pages [9] -->
yt 2

<!-- b000259 | prose | pages [9] -->
1

<!-- b000260 | prose | pages [9] -->
Hf =

<!-- b000261 | prose | pages [9] -->
2g cos θ =

<!-- b000262 | prose | pages [9] -->
cos θ

<!-- b000263 | prose | pages [9] -->
m∙∆h 3

<!-- b000264 | prose | pages [9] -->
(1+yt′2)

<!-- b000265 | prose | pages [9] -->
2

<!-- b000266 | prose | pages [9] -->
(13)

<!-- b000267 | prose | pages [9] -->
mg ∙cos 2θ[1+(zt′

<!-- b000268 | prose | pages [9] -->
yt′)2]

<!-- b000269 | furniture | pages [9] -->


<!-- b000270 | caption | pages [9] -->
Figure 7  the path and force analysis of the fly

<!-- b000271 | furniture | pages [9] -->


<!-- b000272 | prose | pages [9] -->
b. If we take the air drag during the fly into account

<!-- b000273 | prose | pages [9] -->
f = β(y 2 + z 2) According to the Second Newton Law:

<!-- b000274 | furniture | pages [9] -->


<!-- b000275 | prose | pages [9] -->
g cos θ + β

<!-- b000276 | prose | pages [9] -->
m y 2 + z 2

<!-- b000277 | furniture | pages [9] -->


<!-- b000278 | prose | pages [9] -->
y = −

<!-- b000279 | furniture | pages [9] -->


<!-- b000280 | furniture | pages [9] -->


<!-- b000281 | prose | pages [9] -->
Let y = v. Since

<!-- b000282 | prose | pages [9] -->
y

<!-- b000283 | furniture | pages [9] -->


<!-- b000284 | prose | pages [9] -->
= −g cos θ −β

<!-- b000285 | prose | pages [9] -->
z

<!-- b000286 | furniture | pages [9] -->


<!-- b000287 | prose | pages [9] -->
m y 2

<!-- b000288 | prose | pages [9] -->
2

<!-- b000289 | furniture | pages [9] -->


<!-- b000290 | prose | pages [9] -->
1 + y

<!-- b000291 | prose | pages [9] -->
z

<!-- b000292 | furniture | pages [9] -->


<!-- b000293 | prose | pages [9] -->
dy ∙dy

<!-- b000294 | prose | pages [9] -->
dv

<!-- b000295 | prose | pages [9] -->
dt = dv

<!-- b000296 | prose | pages [9] -->
then

<!-- b000297 | prose | pages [9] -->
vdv

<!-- b000298 | prose | pages [9] -->
dt = vdv

<!-- b000299 | prose | pages [9] -->
dy

<!-- b000300 | prose | pages [9] -->
dy = −g cos θ −β

<!-- b000301 | prose | pages [9] -->
Separating the variables yields

<!-- b000302 | prose | pages [9] -->
dy = −

<!-- b000303 | prose | pages [9] -->
m v2

<!-- b000304 | prose | pages [9] -->
vdv

<!-- b000305 | furniture | pages [9] -->


<!-- b000306 | prose | pages [9] -->
g cos θ + β

<!-- b000307 | prose | pages [9] -->
So

<!-- b000308 | prose | pages [9] -->
Hf

<!-- b000309 | prose | pages [9] -->
dy

<!-- b000310 | prose | pages [9] -->
= − 0

<!-- b000311 | prose | pages [9] -->
yt

<!-- b000312 | prose | pages [9] -->
Thus

<!-- b000313 | prose | pages [9] -->
Hf = m

<!-- b000314 | prose | pages [9] -->
m v2

<!-- b000315 | prose | pages [9] -->
0 0

<!-- b000316 | prose | pages [9] -->
vdv

<!-- b000317 | furniture | pages [9] -->


<!-- b000318 | prose | pages [9] -->
g cos θ + β

<!-- b000319 | prose | pages [9] -->
m v2

<!-- b000320 | prose | pages [9] -->
βyt 2 2β ln⁡(1 +

<!-- b000321 | furniture | pages [9] -->


<!-- b000322 | prose | pages [9] -->
mg cos θ)

<!-- b000323 | prose | pages [9] -->
Step 6.  Flying distance and energy relationship

<!-- b000324 | furniture | pages [10] -->
Team # 9582

<!-- b000325 | furniture | pages [10] -->


<!-- b000326 | furniture | pages [10] -->


<!-- b000327 | furniture | pages [10] -->
Page 10 of 34

<!-- b000328 | prose | pages [10] -->
In order to compare the initial kinetic energy of adjacent two cycles, we have to calculate the decrease of the gravitational potential at the beginning and end of the fly. The duration of the fly can be represented as:

<!-- b000329 | prose | pages [10] -->
t =

<!-- b000330 | prose | pages [10] -->
Flying distance is

<!-- b000331 | prose | pages [10] -->
Sf = z tt +

<!-- b000332 | prose | pages [10] -->
The decrease of gravitational potential:

<!-- b000333 | prose | pages [10] -->
2yt

<!-- b000334 | prose | pages [10] -->
g cos θ                           (14)

<!-- b000335 | prose | pages [10] -->
1

<!-- b000336 | prose | pages [10] -->
2 g sin θ ∙t2                     (15)

<!-- b000337 | prose | pages [10] -->
WG = mgSf sin θ                      (16)

<!-- b000338 | furniture | pages [10] -->


<!-- b000339 | prose | pages [10] -->
Finally, we find it necessary to give an equation to describe the energy conversion and conservation relationship at the beginning and the end of “a cycle”, due to the fact that energy is the key of our analysis. (equation 17)

<!-- b000340 | prose | pages [10] -->
E0 = Elost + mg ∙zt sin θ + WG + Whuman + Ereach        (17)

<!-- b000341 | furniture | pages [10] -->


<!-- b000342 | prose | pages [10] -->
Hence, from equation 17, we can get the representation of Ereach:

<!-- b000343 | prose | pages [10] -->
Ereach = E0 −Elost − mg ∙zt sin θ −WG −Whuman        (18)

<!-- b000344 | furniture | pages [10] -->


<!-- b000345 | prose | pages [10] -->
B. Rotation “Vertical air” is not the only judging criteria of a snowboarder’s performance. The total degree of rotation and the level of difficulty are also essential. Hence, it is necessary to discuss the half-pipe shape’s influence on rotation.

<!-- b000346 | furniture | pages [10] -->


<!-- b000347 | prose | pages [10] -->
Step 1.  Analyzing the Problem As soon as the snowboarder flies into the air, if we neglect the air drag, his angular momentum cannot be changed, so his rotation only depends on the snowboarder himself. By changing his own posture, the snowboarder can do twist, flip or whatever he wants. Thus, since we are discussing the influence of the shape of the half-pipe, we only need to consider the initial angular momentum of the fly. To maximize the twist, we have to maximize the initial angular momentum.

<!-- b000348 | furniture | pages [10] -->


<!-- b000349 | prose | pages [10] -->
The angular momentum can be disintegrated into three directions----x, y, and z. Let’s represent them with Lx0, Ly0, and Lz0. The shape of the half-pipe can only affect Lz0, while Lx0 and Ly0 are determined by the snowboarder, with the help of the friction of the snow.

<!-- b000350 | furniture | pages [11] -->
Team # 9582

<!-- b000351 | furniture | pages [11] -->


<!-- b000352 | furniture | pages [11] -->


<!-- b000353 | furniture | pages [11] -->
Page 11 of 34

<!-- b000354 | furniture | pages [11] -->


<!-- b000355 | prose | pages [11] -->
Figure 8

<!-- b000356 | furniture | pages [11] -->


<!-- b000357 | furniture | pages [11] -->


<!-- b000358 | prose | pages [11] -->
(f1 is the friction of the snow and f2 is the air drag)

<!-- b000359 | furniture | pages [11] -->


<!-- b000360 | prose | pages [11] -->
Therefore, we need to focus on Lz0. The force analysis is in figure 8. Since the angle between N and snowboarder has to be small or the snowboarder will lose balance, the torque of N is comparatively small. So N plays a negligible role in increasing the snowboarder’s Lz0. What’s more, the gravity is exerted on the mass point and the exerting point of f2 can be regarded as near the mass point, so the gravity and f2 are of little help to increase Lz0. Plus, f1 can only make Lz0 smaller. Therefore, Lz0 is the final angular momentum of the snowboarder’s performance on the half-pipe, which has a close relationship with the shape of the half-pipe, to be more specific, the curvature.

<!-- b000361 | furniture | pages [11] -->


<!-- b000362 | prose | pages [11] -->
From the definition of angular momentum, we have

<!-- b000363 | prose | pages [11] -->
1

<!-- b000364 | prose | pages [11] -->
3 𝑙2ω0m                            (19)

<!-- b000365 | prose | pages [11] -->
Lz0 =

<!-- b000366 | prose | pages [11] -->
(We regard the snowboarder as a stick. ω0 is the angular velocity right before the fly; ρ0 is the radius of curvature of the cross-section of the half-pipe at the edge and the part of the curve that close to the edge; m is the mass of the snowboarder; l is represented in figure 8)

<!-- b000367 | furniture | pages [11] -->


<!-- b000368 | prose | pages [11] -->
Plus

<!-- b000369 | prose | pages [11] -->
xt 2+yt 2

<!-- b000370 | prose | pages [11] -->
ω0 =

<!-- b000371 | prose | pages [11] -->
ρ0

<!-- b000372 | prose | pages [11] -->
Combining equation 19 and 20 yields

<!-- b000373 | prose | pages [11] -->
(20)

<!-- b000374 | prose | pages [11] -->
xt 2+yt 2

<!-- b000375 | prose | pages [11] -->
1

<!-- b000376 | prose | pages [11] -->
Lz0 =

<!-- b000377 | prose | pages [11] -->
3

<!-- b000378 | prose | pages [11] -->
𝑙2m                       (21) ρ0

<!-- b000379 | prose | pages [11] -->
From equation 21, we can see that the snowboarder should stretch his body as much as possible to increase l (which has nothing to do with the shape of the half-pipe for

<!-- b000380 | prose | pages [11] -->
sure). And to maximize Lz0, ρ0 should be as small as possible and xt 2 + yt 2 should

<!-- b000381 | prose | pages [11] -->
be as large as possible. Here we still use numerical method to find the optimal

<!-- b000382 | furniture | pages [12] -->
Team # 9582

<!-- b000383 | prose | pages [12] -->
half-pipe shape.

<!-- b000384 | furniture | pages [12] -->


<!-- b000385 | furniture | pages [12] -->


<!-- b000386 | furniture | pages [12] -->


<!-- b000387 | furniture | pages [12] -->
Page 12 of 34

<!-- b000388 | prose | pages [12] -->
Step 2.  Given the initial angular momentum, list and explain some possible tricks (1). Twist of beginners’ level

<!-- b000389 | furniture | pages [12] -->


<!-- b000390 | prose | pages [12] -->
Figure 9

<!-- b000391 | furniture | pages [12] -->


<!-- b000392 | furniture | pages [12] -->


<!-- b000393 | prose | pages [12] -->
The angular momentum is along x and y direction. This kind of twist is beginner’s level and doesn’t have much to do with the shape of the half-pipe. Instead, it depends on the snowboarder’s movement right before the fly. So we just skip it here, and discuss it in our extended model.

<!-- b000394 | furniture | pages [12] -->


<!-- b000395 | prose | pages [12] -->
(2). Flip and double cork

<!-- b000396 | furniture | pages [12] -->


<!-- b000397 | prose | pages [12] -->
Figure 10

<!-- b000398 | furniture | pages [12] -->


<!-- b000399 | furniture | pages [12] -->


<!-- b000400 | prose | pages [12] -->
Lz0 alone makes this kind of rotation possible.

<!-- b000401 | furniture | pages [12] -->


<!-- b000402 | prose | pages [12] -->
(3). Flip->high level twist->flip

<!-- b000403 | prose | pages [12] -->
Flip 1

<!-- b000404 | furniture | pages [12] -->


<!-- b000405 | furniture | pages [13] -->
Team # 9582

<!-- b000406 | furniture | pages [13] -->


<!-- b000407 | furniture | pages [13] -->


<!-- b000408 | furniture | pages [13] -->


<!-- b000409 | furniture | pages [13] -->
Page 13 of 34

<!-- b000410 | furniture | pages [13] -->


<!-- b000411 | furniture | pages [13] -->


<!-- b000412 | prose | pages [13] -->
Twist

<!-- b000413 | furniture | pages [13] -->


<!-- b000414 | furniture | pages [13] -->


<!-- b000415 | furniture | pages [13] -->


<!-- b000416 | furniture | pages [13] -->


<!-- b000417 | furniture | pages [13] -->


<!-- b000418 | prose | pages [13] -->
Flip 2

<!-- b000419 | furniture | pages [13] -->


<!-- b000420 | prose | pages [13] -->
Figure 11

<!-- b000421 | furniture | pages [13] -->


<!-- b000422 | furniture | pages [13] -->


<!-- b000423 | prose | pages [13] -->
Lx is exerted by the friction of the snow, which depends on the snowboarder’s action right before the fly. In this case we can see that the direction of angular momentum of a twist can also be along z direction.

<!-- b000424 | furniture | pages [13] -->


<!-- b000425 | prose | pages [13] -->
Numerical Computation

<!-- b000426 | prose | pages [13] -->
Before numerical computation to obtainElost , the loss of Energy during sliding, and the production of “Vertical Air”, we have to determine the values of some parameters, such as the friction coefficient between the snow and snowboard (α), the drag coefficient of air (β), the mass of the snowboarder (m), and the initial mechanical energy at the beginning of a cycle (E0).

<!-- b000427 | furniture | pages [13] -->


<!-- b000428 | prose | pages [13] -->
According to H.Yan, P.Liu, and F.Guo[8], the coefficient of kinetic friction between snow and snowboard is generally about 0.03 to 0.2. In addition, J.Chen, R.Li and Z.Guan [9] discovered the friction coefficient to be 0.0312. Thus, we generally assume α to be 0.03 in our discussion about shape of half-pipe.

<!-- b000429 | furniture | pages [13] -->


<!-- b000430 | prose | pages [13] -->
As N.Yan stated in reference [10], the air drag coefficient is about 0.15.

<!-- b000431 | furniture | pages [13] -->


<!-- b000432 | prose | pages [13] -->
Since the mass of Shaun White, one of the most outstanding snowboarders in the world, is 63kg, we assume that the mass of a snowboarder is typically 60kg.

<!-- b000433 | furniture | pages [14] -->
Team # 9582

<!-- b000434 | furniture | pages [14] -->


<!-- b000435 | furniture | pages [14] -->


<!-- b000436 | furniture | pages [14] -->
Page 14 of 34

<!-- b000437 | prose | pages [14] -->
Moreover, according to reference [11], the drop-in ramp height should be at least 5.5m and distance from ramp to pipe should be at least 9m. Since the slope angle is about 18°, the potential energy of gravity is: mg ∙ 5.5 + 9 ∙cos 18° ≈8267 J.

<!-- b000438 | furniture | pages [14] -->


<!-- b000439 | prose | pages [14] -->
As α may not exceed 0.2 (in which case E0 would be 6613 J), we conservatively assume the initial mechanical energy at the beginning of a cycle (E0) to be 7000 J.

<!-- b000440 | furniture | pages [14] -->


<!-- b000441 | prose | pages [14] -->
To sum up, we assume that : α ≈0.03, β ≈0.15, m ≈60kg, E0 ≈7000 J.

<!-- b000442 | furniture | pages [14] -->


<!-- b000443 | prose | pages [14] -->
Besides, we need to define y(x) and z(x), the shape of ramp cross-section and the path snowboard chooses respectively. As we assumed before, y(x) is a convex C2 curve, which is symmetric in reality. There is a horizontal flat line (‘Flat’) connecting two parts of the ramp and each part consists of a smooth transition part and possibly vertical part of (‘Vert’).

<!-- b000444 | furniture | pages [14] -->


<!-- b000445 | prose | pages [14] -->
Figure 12

<!-- b000446 | furniture | pages [14] -->


<!-- b000447 | furniture | pages [14] -->


<!-- b000448 | prose | pages [14] -->
The path player choose can be represented by z=z(x). As figure below shows, in a simply condition with constant friction, the energy loss will be minimized if z is proportion to τ x , the length of the projection curvature of the three dimensional

<!-- b000449 | prose | pages [14] -->
= (𝑥, 𝑦 𝑥 , 𝑧 𝑥 )to X-Y plane. Thus, we define the coordinate along z curve 𝑝(𝑥)

<!-- b000450 | prose | pages [14] -->
axis as z = z τ x  ≈kτ x . Practically, we control z(x) using the location of the

<!-- b000451 | prose | pages [14] -->
point right before the fly.

<!-- b000452 | furniture | pages [14] -->


<!-- b000453 | prose | pages [14] -->
Figure 13

<!-- b000454 | furniture | pages [14] -->


<!-- b000455 | furniture | pages [14] -->


<!-- b000456 | furniture | pages [15] -->
Team # 9582

<!-- b000457 | furniture | pages [15] -->


<!-- b000458 | furniture | pages [15] -->


<!-- b000459 | furniture | pages [15] -->
Page 15 of 34

<!-- b000460 | prose | pages [15] -->
Given certain relationship between y(x) and x and between z(x) and x, we used numerical calculus to solve the differential equation (6):

<!-- b000461 | prose | pages [15] -->
my ′′

<!-- b000462 | prose | pages [15] -->
x

<!-- b000463 | prose | pages [15] -->
Elost x = { α

<!-- b000464 | prose | pages [15] -->
+ β

<!-- b000465 | prose | pages [15] -->
−x0

<!-- b000466 | prose | pages [15] -->
1+y′2  1+y′2+z′2

<!-- b000467 | prose | pages [15] -->
2

<!-- b000468 | prose | pages [15] -->
m [E0 −Elost τ −mg y cos θ −

<!-- b000469 | prose | pages [15] -->
zsinθ]+αmgcosθ1+y′2+z′21+y′2}dτ (6)

<!-- b000470 | furniture | pages [15] -->


<!-- b000471 | prose | pages [15] -->
Then we calculate the resulting “vertical air” use both analytical equations and numerical simulation. We solved the problem of “Projectile” and got analytical results. Since we can obtain “vertical air”, duration of Fly and Flying distance more easily by numerical simulation, we also use numerical simulation for later analysis.

<!-- b000472 | caption | pages [15] -->
Figure 14 shows the output figure of numerical simulation which represents the path

<!-- b000473 | prose | pages [15] -->
of the snowboarder on the ramp and in the air.

<!-- b000474 | furniture | pages [15] -->


<!-- b000475 | prose | pages [15] -->
8

<!-- b000476 | prose | pages [15] -->
6

<!-- b000477 | prose | pages [15] -->
4

<!-- b000478 | prose | pages [15] -->
2

<!-- b000479 | prose | pages [15] -->
0

<!-- b000480 | prose | pages [15] -->
-2

<!-- b000481 | prose | pages [15] -->
-4 0

<!-- b000482 | prose | pages [15] -->
-20

<!-- b000483 | prose | pages [15] -->
-40

<!-- b000484 | prose | pages [15] -->
-60

<!-- b000485 | prose | pages [15] -->
10 5 0

<!-- b000486 | prose | pages [15] -->
-5

<!-- b000487 | prose | pages [15] -->
-10 -10

<!-- b000488 | caption | pages [15] -->
Figure 14 output figure of numerical simulation of entire “cycle” in snowboarding

<!-- b000489 | furniture | pages [15] -->


<!-- b000490 | prose | pages [15] -->
To validate our results, we compared analytical results and numerical results:

<!-- b000491 | furniture | pages [15] -->


<!-- b000492 | prose | pages [15] -->
We assume: width=15m, flat=5m, depth=3.5m, zt =10m, θ=18°, zt =10m. Transition part is standard elliptic, g=9.8m/s2, m=60kg, β =0.15kg/m, according to reference[4][8][9][10][11].

<!-- b000493 | furniture | pages [15] -->


<!-- b000494 | prose | pages [15] -->
Condition Method Vy

<!-- b000495 | prose | pages [15] -->
Without

<!-- b000496 | prose | pages [15] -->
Analytical 11.2316m/s

<!-- b000497 | prose | pages [15] -->
friction

<!-- b000498 | prose | pages [15] -->
Numerical 11.2316m/s Error Ratio 0%

<!-- b000499 | prose | pages [15] -->
With friction Analytical 11.2316m/s Numerical 11.2316m/s Error Ratio 0%

<!-- b000500 | furniture | pages [15] -->


<!-- b000501 | prose | pages [15] -->
Vertical Air Fly Distance Duration of Fly

<!-- b000502 | prose | pages [15] -->
7.1156m 25.5115 2.4101 7.1216m 25.5121 2.4102 0.084% 0.002% 0.004%

<!-- b000503 | prose | pages [15] -->
6.9979m -- -- 7.0037m 24.5173 2.3836 0.083% -- --

<!-- b000504 | furniture | pages [16] -->
Team # 9582

<!-- b000505 | prose | pages [16] -->
Validity

<!-- b000506 | furniture | pages [16] -->


<!-- b000507 | furniture | pages [16] -->


<!-- b000508 | furniture | pages [16] -->
Page 16 of 34

<!-- b000509 | prose | pages [16] -->
Using recommended width, height, flat length and gradient angle, with other parameters fitting the reality in Snowboard half-pipe game, the resulting maximum Vertical Air is about 7 meters. This result matches the Shaun White’s best performance of and is consistent with the common “Vertical Air” (12 feet~20 feet for men and 6 feet~15 feet for women) in Snowboard half-pipe games.

<!-- b000510 | furniture | pages [16] -->


<!-- b000511 | heading | pages [16] -->
Sensitivity

<!-- b000512 | prose | pages [16] -->
As to the sensitivity, we modified parameters by ±10%, and the result supporting that the numerical simulation is robust.

<!-- b000513 | furniture | pages [16] -->


<!-- b000514 | prose | pages [16] -->
Vertical Air Change

<!-- b000515 | furniture | pages [16] -->


<!-- b000516 | prose | pages [16] -->
+10% Percentage

<!-- b000517 | prose | pages [16] -->
W(Width)~15m 16.5m 5.53% H(Depth)~3.5m 3.85m 2.50% B(Flat)~5m 5.50m 0.86% Zt(Fly Point)~10m 11m 8.18%

<!-- b000518 | furniture | pages [16] -->


<!-- b000519 | heading | pages [16] -->
Extended Model

<!-- b000520 | prose | pages [16] -->
-10% Vertical Air Change Percentage 13.5m -6.13% 3.15m -2.57% 4.50m -0.87% 9m -8.08%

<!-- b000521 | prose | pages [16] -->
In the basic model above, we generally neglect the influence of the snowboarder on the flying path, but rather pay most attention to the objective factors. Nevertheless, snowboarder in itself is the key role in this sport, and their diverse performances owe much to the variations among different snowboarders. In this extended model, we take the impact of the snowboarder into account.

<!-- b000522 | furniture | pages [16] -->


<!-- b000523 | heading | pages [16] -->
1 The direction of velocity

<!-- b000524 | prose | pages [16] -->
A snowboarder is different from an rigid body in that he can turn, decelerate etc where a small ball or a stick can’t. The direction of a snowboard could be different from that of the snowboarder’s velocity, although this is often not welcomed, since it would slow down the snowboarder. This means, however, that a skilled snowboarder may move in a direction partly determined by himself. This is why we discussed how to choose the ‘best path’ in a given course.

<!-- b000525 | furniture | pages [16] -->


<!-- b000526 | prose | pages [16] -->
Especially, consider the point right before a fly. From the discussion above, we learnt that the larger zt is, the longer flying distance is. As a result, the cycle distance would be longer, which ultimately results in fewer cycles. However, since a snowboarder must perform 5 to 8 acrobatic tricks in the Winter Olympic Games, fewer cycles are not allowed. Hence, a snowboarder should avoid flying too far. At the same time, however, a larger zt means greater yt’, which, contrarily, is favorable for a higher

<!-- b000527 | furniture | pages [17] -->
Team # 9582

<!-- b000528 | furniture | pages [17] -->


<!-- b000529 | furniture | pages [17] -->


<!-- b000530 | furniture | pages [17] -->
Page 17 of 34

<!-- b000531 | prose | pages [17] -->
‘vertical air’. In that case, a skilled snowboarder may choose to reduce his zt  right before the fly.

<!-- b000532 | furniture | pages [17] -->


<!-- b000533 | prose | pages [17] -->
To sum up, a skilled snowboarder would choose a path with reasonable zt and reduce his zt  right before the fly while maintaining his yt  or convert the part of kinetic energy in the velocity along z direction into that in y direction.

<!-- b000534 | furniture | pages [17] -->


<!-- b000535 | prose | pages [17] -->
Here is a detailed analysis about the fly while taking the snowboarder’s influence on

<!-- b000536 | prose | pages [17] -->
zt  into account.

<!-- b000537 | furniture | pages [17] -->


<!-- b000538 | prose | pages [17] -->
a. Maintaining 𝐲𝐭 Vertical air maintains the same:

<!-- b000539 | prose | pages [17] -->
E0−Elost xt +mg ∙zt sin θ+ yt′2yt′′

<!-- b000540 | prose | pages [17] -->
yt 2

<!-- b000541 | prose | pages [17] -->
1

<!-- b000542 | prose | pages [17] -->
Hf =

<!-- b000543 | prose | pages [17] -->
2g cos θ =

<!-- b000544 | prose | pages [17] -->
cos θ

<!-- b000545 | prose | pages [17] -->
Flying distance:

<!-- b000546 | prose | pages [17] -->
1

<!-- b000547 | prose | pages [17] -->
m∙∆h 3

<!-- b000548 | prose | pages [17] -->
(1+yt′2)

<!-- b000549 | prose | pages [17] -->
2

<!-- b000550 | prose | pages [17] -->
(22)

<!-- b000551 | prose | pages [17] -->
mg ∙cos 2θ[1+(zt′

<!-- b000552 | prose | pages [17] -->
yt′)2]

<!-- b000553 | prose | pages [17] -->
2yt

<!-- b000554 | prose | pages [17] -->
g cos θ)2                           (23)

<!-- b000555 | prose | pages [17] -->
Sf =

<!-- b000556 | prose | pages [17] -->
2 g sin θ ∙(

<!-- b000557 | furniture | pages [17] -->


<!-- b000558 | prose | pages [17] -->
b. Convert the part of kinetic energy in the velocity along z direction into that in y

<!-- b000559 | prose | pages [17] -->
direction.

<!-- b000560 | prose | pages [17] -->
yt 2 =

<!-- b000561 | prose | pages [17] -->
2

<!-- b000562 | prose | pages [17] -->
yt′2yt′′

<!-- b000563 | prose | pages [17] -->
m [E0 −Elost xt + mg ∙zt sin θ +

<!-- b000564 | prose | pages [17] -->
Vertical air:

<!-- b000565 | prose | pages [17] -->
m ∙∆h]         (24) 3

<!-- b000566 | prose | pages [17] -->
(1+yt′2)

<!-- b000567 | prose | pages [17] -->
2

<!-- b000568 | prose | pages [17] -->
E0−Elost xt +mg ∙zt sin θ+ yt′2yt′′

<!-- b000569 | prose | pages [17] -->
yt 2

<!-- b000570 | prose | pages [17] -->
1

<!-- b000571 | prose | pages [17] -->
Hf =

<!-- b000572 | prose | pages [17] -->
2g cos θ =

<!-- b000573 | prose | pages [17] -->
cos θ

<!-- b000574 | prose | pages [17] -->
Flying distance:

<!-- b000575 | prose | pages [17] -->
1

<!-- b000576 | prose | pages [17] -->
m∙∆h 3

<!-- b000577 | prose | pages [17] -->
(1+yt′2)

<!-- b000578 | prose | pages [17] -->
2

<!-- b000579 | prose | pages [17] -->
(25) mg ∙cos 2θ

<!-- b000580 | prose | pages [17] -->
2yt

<!-- b000581 | prose | pages [17] -->
g cos θ)2                    (26)

<!-- b000582 | prose | pages [17] -->
2 g sin θ ∙(

<!-- b000583 | prose | pages [17] -->
Sf =

<!-- b000584 | furniture | pages [17] -->


<!-- b000585 | heading | pages [17] -->
2 Total degree of rotation 𝚯

<!-- b000586 | prose | pages [17] -->
The snowboarder’s action has a large influence on the total degree of rotation in two ways. First, before starting a fly with acrobatic trick, the snowboarder can make some preparation for the trick. He can create angular momentum along x and y direction by twisting to the direction that he intends to rotate during the fly and acquiring angular momentum along x and y direction with the help of the friction of the snow. Second, during the fly, despite the fact that the angular of momentum cannot be changed, the snowboarder can change his angular velocity by altering his moment of inertia. For instance, he can hold his arms tight from a stretching posture to increase his angular velocity (because of the decrease of moment of inertia), and in turn increase the total degree of rotation (Figure 15). In this process, the mechanical energy is also increased since the snowboarder has done work against the pseudo

<!-- b000587 | furniture | pages [18] -->
Team # 9582

<!-- b000588 | furniture | pages [18] -->


<!-- b000589 | furniture | pages [18] -->
Page 18 of 34

<!-- b000590 | prose | pages [18] -->
force petrifugal force.

<!-- b000591 | furniture | pages [18] -->


<!-- b000592 | prose | pages [18] -->
Figure 15

<!-- b000593 | furniture | pages [18] -->


<!-- b000594 | heading | pages [18] -->
3 the landing point

<!-- b000595 | prose | pages [18] -->
In the basic model, we assumed that a snowboarder enter into the half-pipe right at the coping after a fly. Nevertheless, this is often not the case. Usually, a skilled snowboarder would prefer to land on the transition part rather than land at the coping mainly in the consideration of safety and easiness, flying time, and friction.

<!-- b000596 | furniture | pages [18] -->


<!-- b000597 | prose | pages [18] -->
Firstly, landing on the transition part is much safer and easier than doing so at coping. The latter requires much more precision in landing, or the snowboarder may land on the deck, which leads to an undesirable crash.

<!-- b000598 | furniture | pages [18] -->


<!-- b000599 | prose | pages [18] -->
A longer flying time can also resulted from landing on the transition, which is favorable since longer flying time means better trick.

<!-- b000600 | furniture | pages [18] -->


<!-- b000601 | prose | pages [18] -->
Furthermore, as flying in the air avoid the friction from snow, replacing part of movement on the half-pipe with an airborne one can help lessen the decrease of skiing speed.

<!-- b000602 | furniture | pages [18] -->


<!-- b000603 | prose | pages [18] -->
In a word, landing on the transition part instead of at coping would sometimes be a more advisable choice for a snowboarder.

<!-- b000604 | furniture | pages [18] -->


<!-- b000605 | prose | pages [18] -->
To sum up, the schema can be represented as the following ‘map’:

<!-- b000606 | furniture | pages [19] -->
Team # 9582

<!-- b000607 | furniture | pages [19] -->


<!-- b000608 | furniture | pages [19] -->
Page 19 of 34

<!-- b000609 | caption | pages [19] -->
Figure 16 complete schema of model

<!-- b000610 | furniture | pages [19] -->


<!-- b000611 | furniture | pages [19] -->


<!-- b000612 | heading | pages [19] -->
Solutions to the problems

<!-- b000613 | prose | pages [19] -->
Question1:

<!-- b000614 | prose | pages [19] -->
Determine the shape of a snowboard course (currently known as a “halfpipe”) to maximize the production of “vertical air” by a skilled snowboarder. “Vertical air” is the maximum vertical distance above the edge of the half-pipe.

<!-- b000615 | furniture | pages [19] -->


<!-- b000616 | prose | pages [19] -->
Answer 1:

<!-- b000617 | prose | pages [19] -->
We have used numerical method to test how “Vertical air” is affected by other factors: width of the ramp, the gradient angle of the pipe, the path the snowboarder chooses, etc. Optimizing all factors, we got shape of the cross-section of ramp, which maximize the production of “Vertical Air”.

<!-- b000618 | furniture | pages [20] -->
Team # 9582

<!-- b000619 | prose | pages [20] -->
10

<!-- b000620 | prose | pages [20] -->
5

<!-- b000621 | prose | pages [20] -->
0

<!-- b000622 | prose | pages [20] -->
-5 0

<!-- b000623 | prose | pages [20] -->
-20

<!-- b000624 | prose | pages [20] -->
-40

<!-- b000625 | furniture | pages [20] -->


<!-- b000626 | furniture | pages [20] -->


<!-- b000627 | furniture | pages [20] -->
Page 20 of 34

<!-- b000628 | prose | pages [20] -->
10 5 0

<!-- b000629 | prose | pages [20] -->
-5

<!-- b000630 | prose | pages [20] -->
-60

<!-- b000631 | prose | pages [20] -->
-10

<!-- b000632 | prose | pages [20] -->
Figure 17

<!-- b000633 | furniture | pages [20] -->


<!-- b000634 | prose | pages [20] -->
Analysis 1:

<!-- b000635 | prose | pages [20] -->
The goal of this question is to optimize the shape of the course which provides maximum vertical distance above the edge of the half-pipe during the fly. Mathematically, we define following objective function:

<!-- b000636 | prose | pages [20] -->
max V𝑒𝑟𝑡𝑖𝑐𝑎𝑙𝐴𝑖𝑟 𝑥, 𝑦 𝑥 , 𝑧 𝑥     𝑠. 𝑡.  𝑦= 𝑦 𝑥 , 𝑧= 𝑧 𝑥

<!-- b000637 | furniture | pages [20] -->


<!-- b000638 | prose | pages [20] -->
The function is determined by the following parameters: W(width), H(depth), B(length of flat bottom), zt (fly point) and transition shape.

<!-- b000639 | furniture | pages [20] -->


<!-- b000640 | prose | pages [20] -->
There are several factors affecting the shape of course and path. Among them we firstly consider and optimize following dominant variables.

<!-- b000641 | furniture | pages [20] -->


<!-- b000642 | prose | pages [20] -->
Variables determine y(x)

<!-- b000643 | prose | pages [20] -->
W: The width of the ramp which is the distance between the edges of two sides. H: the height/depth of the ramp, the perpendicular distance between coping edge and flat bottom. B: the length of the flat platform at the middle of the ramp. Transition Shape: the y-x relationship, indicating the shape of transition part connecting ‘Vert’ and flat bottom.

<!-- b000644 | furniture | pages [20] -->


<!-- b000645 | prose | pages [20] -->
Variables determine z(x)

<!-- b000646 | prose | pages [20] -->
Zt: z value right before the fly, z coordinate along z-axis, which determine sliding path the snowboarder choose.

<!-- b000647 | prose | pages [20] -->
Zt will determine the z = z τ x  ~kτ x

<!-- b000648 | furniture | pages [20] -->


<!-- b000649 | prose | pages [20] -->
We assumed the default value of these variables as the table shows and analyze the

<!-- b000650 | furniture | pages [21] -->
Team # 9582

<!-- b000651 | furniture | pages [21] -->


<!-- b000652 | furniture | pages [21] -->


<!-- b000653 | furniture | pages [21] -->
Page 21 of 34

<!-- b000654 | prose | pages [21] -->
effect of each variable respectively while maintaining other variables.

<!-- b000655 | furniture | pages [21] -->


<!-- b000656 | prose | pages [21] -->
W(width) 15m B(length of flat bottom) 5m

<!-- b000657 | prose | pages [21] -->
𝑧𝑡(𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝑜𝑓𝑡𝑎𝑟𝑡 𝑝𝑜𝑖𝑛𝑡 𝑜𝑓 𝐹𝑙𝑦) 10m

<!-- b000658 | furniture | pages [21] -->


<!-- b000659 | prose | pages [21] -->
 W(width)

<!-- b000660 | furniture | pages [21] -->


<!-- b000661 | prose | pages [21] -->
relationship between width & VAf

<!-- b000662 | prose | pages [21] -->
8.5

<!-- b000663 | prose | pages [21] -->
8

<!-- b000664 | prose | pages [21] -->
7.5

<!-- b000665 | prose | pages [21] -->
7

<!-- b000666 | prose | pages [21] -->
VAf

<!-- b000667 | prose | pages [21] -->
6.5

<!-- b000668 | prose | pages [21] -->
6

<!-- b000669 | prose | pages [21] -->
5.5

<!-- b000670 | prose | pages [21] -->
5 10 15 20 25

<!-- b000671 | prose | pages [21] -->
width

<!-- b000672 | prose | pages [21] -->
H(height) 3.5m 𝜃 (gradient angle of the

<!-- b000673 | prose | pages [21] -->
18°

<!-- b000674 | prose | pages [21] -->
venue, the angle between z

<!-- b000675 | prose | pages [21] -->
axis and ground)

<!-- b000676 | prose | pages [21] -->
Transition Shape Standard

<!-- b000677 | prose | pages [21] -->
ellipse

<!-- b000678 | prose | pages [21] -->
relationship between width & Eleave

<!-- b000679 | prose | pages [21] -->
7600

<!-- b000680 | prose | pages [21] -->
7500

<!-- b000681 | prose | pages [21] -->
7400

<!-- b000682 | prose | pages [21] -->
7300

<!-- b000683 | prose | pages [21] -->
7200

<!-- b000684 | prose | pages [21] -->
Eleave

<!-- b000685 | prose | pages [21] -->
7100

<!-- b000686 | prose | pages [21] -->
7000

<!-- b000687 | prose | pages [21] -->
6900

<!-- b000688 | prose | pages [21] -->
6800

<!-- b000689 | prose | pages [21] -->
6700 10 15 20 25

<!-- b000690 | furniture | pages [21] -->


<!-- b000691 | prose | pages [21] -->
width

<!-- b000692 | prose | pages [21] -->
Figure 18 By simulating with numerical method with W (width of ramp) varying from 10 to 25, we can find the wider the ramp is, the faster the snowboarder can speed up before the fly and, consequently, the larger “Vertical Air” is.

<!-- b000693 | furniture | pages [21] -->


<!-- b000694 | prose | pages [21] -->
 H(height)

<!-- b000695 | prose | pages [21] -->
relationship between height & VerticalAir

<!-- b000696 | prose | pages [21] -->
9.5

<!-- b000697 | prose | pages [21] -->
9

<!-- b000698 | prose | pages [21] -->
8.5

<!-- b000699 | prose | pages [21] -->
8

<!-- b000700 | prose | pages [21] -->
VerticalAir

<!-- b000701 | prose | pages [21] -->
7.5

<!-- b000702 | prose | pages [21] -->
7

<!-- b000703 | prose | pages [21] -->
6.5

<!-- b000704 | prose | pages [21] -->
6

<!-- b000705 | prose | pages [21] -->
5.5 2 4 6 8 10 12 14 16 18 20

<!-- b000706 | prose | pages [21] -->
height

<!-- b000707 | prose | pages [21] -->
relationship between height & Velocityy

<!-- b000708 | prose | pages [21] -->
13.5

<!-- b000709 | prose | pages [21] -->
13

<!-- b000710 | prose | pages [21] -->
12.5

<!-- b000711 | prose | pages [21] -->
Velocityy

<!-- b000712 | prose | pages [21] -->
12

<!-- b000713 | prose | pages [21] -->
11.5

<!-- b000714 | prose | pages [21] -->
11

<!-- b000715 | prose | pages [21] -->
10.5 2 4 6 8 10 12 14 16 18 20

<!-- b000716 | furniture | pages [21] -->


<!-- b000717 | prose | pages [21] -->
height

<!-- b000718 | caption | pages [21] -->
Figure 19 relationship between “vertical air” vs. height (left) and

<!-- b000719 | prose | pages [21] -->
velocity along y axis vs. height(right)

<!-- b000720 | furniture | pages [21] -->


<!-- b000721 | prose | pages [21] -->
From numerical computation, within about 15 meter (possibly the same value of the width), higher ramp can results in higher velocity and larger “Vertical Air”. But when the ramp is higher than 15 meter, the velocity and the “Vertical Air” will decrease with height. Commonly, the height of ramp is around 3 meter to 6 meter, so we can accept that it is advisable to build a high ramp in this range.

<!-- b000722 | furniture | pages [22] -->
Team # 9582

<!-- b000723 | furniture | pages [22] -->


<!-- b000724 | prose | pages [22] -->
 B(length of flat bottom)

<!-- b000725 | prose | pages [22] -->
relationship between flat & VAf

<!-- b000726 | prose | pages [22] -->
6.8

<!-- b000727 | prose | pages [22] -->
6.7

<!-- b000728 | prose | pages [22] -->
6.6

<!-- b000729 | prose | pages [22] -->
6.5

<!-- b000730 | prose | pages [22] -->
VAf

<!-- b000731 | prose | pages [22] -->
6.4

<!-- b000732 | prose | pages [22] -->
6.3

<!-- b000733 | prose | pages [22] -->
6.2

<!-- b000734 | prose | pages [22] -->
6.1

<!-- b000735 | prose | pages [22] -->
6 0 1 2 3 4 5 6

<!-- b000736 | prose | pages [22] -->
flat

<!-- b000737 | furniture | pages [22] -->


<!-- b000738 | furniture | pages [22] -->


<!-- b000739 | furniture | pages [22] -->
Page 22 of 34

<!-- b000740 | prose | pages [22] -->
relationship between flat & Eleave

<!-- b000741 | prose | pages [22] -->
7400

<!-- b000742 | prose | pages [22] -->
7350

<!-- b000743 | prose | pages [22] -->
7300

<!-- b000744 | prose | pages [22] -->
Eleave

<!-- b000745 | prose | pages [22] -->
7250

<!-- b000746 | prose | pages [22] -->
7200

<!-- b000747 | prose | pages [22] -->
7150 0 1 2 3 4 5 6

<!-- b000748 | furniture | pages [22] -->


<!-- b000749 | prose | pages [22] -->
flat

<!-- b000750 | prose | pages [22] -->
Figure 20

<!-- b000751 | furniture | pages [22] -->


<!-- b000752 | prose | pages [22] -->
With other parameters fixed to default values, the effects of flat is complex. Longer flat provides larger “Vertical Air”. But the decreasing 𝐸𝑙𝑒𝑎𝑣𝑒 value means the potential maximum “Vertical Air” is decreased, the “Vertical Air” is affected by the direction the player flies to.

<!-- b000753 | furniture | pages [22] -->


<!-- b000754 | prose | pages [22] -->
 𝜃 𝑔𝑟𝑎𝑑𝑖𝑒𝑛𝑡 𝑎𝑛𝑔𝑙𝑒 𝑜𝑓 𝑡𝑕𝑒 𝑣𝑒𝑛𝑢𝑒

<!-- b000755 | prose | pages [22] -->
It is obvious that the steeper the venue is, the faster players can slide. Thus they will overcome gravity for longer time and “fly” higher.

<!-- b000756 | prose | pages [22] -->
relationship between theta & VAf

<!-- b000757 | prose | pages [22] -->
12

<!-- b000758 | prose | pages [22] -->
11

<!-- b000759 | prose | pages [22] -->
10

<!-- b000760 | prose | pages [22] -->
9

<!-- b000761 | prose | pages [22] -->
VAf

<!-- b000762 | prose | pages [22] -->
8

<!-- b000763 | prose | pages [22] -->
7

<!-- b000764 | prose | pages [22] -->
6

<!-- b000765 | prose | pages [22] -->
5

<!-- b000766 | prose | pages [22] -->
4 0 5 10 15 20 25 30 35 40 45

<!-- b000767 | prose | pages [22] -->
theta

<!-- b000768 | prose | pages [22] -->
relationship between theta & Eleave

<!-- b000769 | prose | pages [22] -->
10000

<!-- b000770 | prose | pages [22] -->
9500

<!-- b000771 | prose | pages [22] -->
9000

<!-- b000772 | prose | pages [22] -->
8500

<!-- b000773 | prose | pages [22] -->
8000

<!-- b000774 | prose | pages [22] -->
Eleave

<!-- b000775 | prose | pages [22] -->
7500

<!-- b000776 | prose | pages [22] -->
7000

<!-- b000777 | prose | pages [22] -->
6500

<!-- b000778 | prose | pages [22] -->
6000

<!-- b000779 | prose | pages [22] -->
5500

<!-- b000780 | prose | pages [22] -->
5000 0 5 10 15 20 25 30 35 40 45

<!-- b000781 | furniture | pages [22] -->


<!-- b000782 | prose | pages [22] -->
theta

<!-- b000783 | prose | pages [22] -->
Figure 21

<!-- b000784 | furniture | pages [22] -->


<!-- b000785 | prose | pages [22] -->
 𝑧𝑡(𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝑜𝑓𝑡𝑎𝑟𝑡 𝑝𝑜𝑖𝑛𝑡 𝑜𝑓 𝐹𝑙𝑦)

<!-- b000786 | prose | pages [22] -->
What path the snowboarder takes, which is defined by Zt in model, plays significant part for “Vertical Air”. As previous work *14+ suggests, steeper path provides the player higher speed, larger chance to fly farther down the pipe, but fewer tricks in a run. Shallower path means cutting straight across and straight up the wall, but provides less momentum and lower speed.

<!-- b000787 | furniture | pages [23] -->
Team # 9582

<!-- b000788 | prose | pages [23] -->
relationship between zlength & VA

<!-- b000789 | prose | pages [23] -->
10

<!-- b000790 | prose | pages [23] -->
9

<!-- b000791 | prose | pages [23] -->
8

<!-- b000792 | prose | pages [23] -->
VA

<!-- b000793 | prose | pages [23] -->
7

<!-- b000794 | prose | pages [23] -->
6

<!-- b000795 | prose | pages [23] -->
5

<!-- b000796 | prose | pages [23] -->
4 0 5 10 15

<!-- b000797 | prose | pages [23] -->
zlength

<!-- b000798 | furniture | pages [23] -->


<!-- b000799 | furniture | pages [23] -->


<!-- b000800 | furniture | pages [23] -->
Page 23 of 34

<!-- b000801 | prose | pages [23] -->
relationship between zlength & Eleave

<!-- b000802 | prose | pages [23] -->
8500

<!-- b000803 | prose | pages [23] -->
8000

<!-- b000804 | prose | pages [23] -->
7500

<!-- b000805 | prose | pages [23] -->
7000

<!-- b000806 | prose | pages [23] -->
Eleave

<!-- b000807 | prose | pages [23] -->
6500

<!-- b000808 | prose | pages [23] -->
6000

<!-- b000809 | prose | pages [23] -->
5500

<!-- b000810 | prose | pages [23] -->
5000 0 5 10 15

<!-- b000811 | furniture | pages [23] -->


<!-- b000812 | prose | pages [23] -->
zlength

<!-- b000813 | caption | pages [23] -->
Figure 22 relationship between “vertical air” v.s. Zt(left) and

<!-- b000814 | prose | pages [23] -->
between 𝐸𝑙𝑒𝑎𝑣𝑒v.s. Zt (right)

<!-- b000815 | furniture | pages [23] -->


<!-- b000816 | furniture | pages [23] -->


<!-- b000817 | furniture | pages [23] -->


<!-- b000818 | furniture | pages [23] -->


<!-- b000819 | prose | pages [23] -->
Our simulation coincide with this study and shows players’ skills (choose best path) can help them to optmize “Vertical Air”.

<!-- b000820 | furniture | pages [23] -->


<!-- b000821 | prose | pages [23] -->
The larger zt is, the steeper the path is and more momentum before the fly. But if the path is too steep (zt>5 meter) the player will fly more down the pipe instead of higher above the pipe. Shallower path (zt is smaller than 5 meter) could provide larger “Vertical Air”.

<!-- b000822 | furniture | pages [23] -->


<!-- b000823 | furniture | pages [23] -->


<!-- b000824 | prose | pages [23] -->
 Global Optimal

<!-- b000825 | prose | pages [23] -->
We enumerate width from 13m to 18m, height from 2 to 6, flat length from 4 to 6, Zt from 0 to 15 and 𝜃 from 15° to 20°. Use the kinetic energy before the fly (𝐸𝑙𝑒𝑎𝑣𝑒) and “Vertical Air” as criteria: Best parameters for “Vertical Air” defined in the Basic Model, when the snowboarder does not change his velocity direction right before the fly.

<!-- b000826 | prose | pages [23] -->
𝑊𝑖𝑑𝑡h = 18𝑚, 𝐻𝑒𝑖𝑔h𝑡= 3𝑚, 𝐹𝑙𝑎𝑡= 4𝑚, 𝑍𝑡= 6𝑚, 𝜃= 20°

<!-- b000827 | furniture | pages [23] -->


<!-- b000828 | furniture | pages [23] -->


<!-- b000829 | furniture | pages [23] -->


<!-- b000830 | prose | pages [23] -->
Also, the optimum shape of the course using Gene Algorithm is:

<!-- b000831 | furniture | pages [23] -->


<!-- b000832 | furniture | pages [23] -->


<!-- b000833 | prose | pages [23] -->
 Transition Shape Among these factors, the shape of transition plays a significant role since the curve directly determines the energy loss caused by friction along the path. We follow the following procedures, including random Generation of convex curves, controlling Splines (3rd) and Gene Algorithm, to find the optimal transition shape.

<!-- b000834 | furniture | pages [24] -->
Team # 9582

<!-- b000835 | prose | pages [24] -->
Define "Controling Points" of the curves

<!-- b000836 | furniture | pages [24] -->


<!-- b000837 | furniture | pages [24] -->


<!-- b000838 | furniture | pages [24] -->
Page 24 of 34

<!-- b000839 | prose | pages [24] -->
•satisfying the requests for transition part •connecting coping edge of ramp and flat bottom smoothly

<!-- b000840 | prose | pages [24] -->
Generate sampling points convex curves

<!-- b000841 | prose | pages [24] -->
•The curve is convex to the downwards and second-order differentiable •Use B-Spline, two-point method and three-point method •Become the 1st generation in Gene Algorithm

<!-- b000842 | prose | pages [24] -->
Define "Gene"

<!-- b000843 | prose | pages [24] -->
•the position of controling points

<!-- b000844 | prose | pages [24] -->
Define Fitness-Function

<!-- b000845 | prose | pages [24] -->
•the "Vertical Air"  determined by the shape defined by the controling point and the default parameters

<!-- b000846 | prose | pages [24] -->
Gene-Algorithm

<!-- b000847 | prose | pages [24] -->
•recursivly process •roulette wheel selection •uniform cross-over •random mutation but maintaining convex •optimize the Fitness of "Gene"

<!-- b000848 | prose | pages [24] -->
Optimize curve

<!-- b000849 | prose | pages [24] -->
•The optimal curve survives from Gene Algorithm

<!-- b000850 | furniture | pages [24] -->


<!-- b000851 | furniture | pages [24] -->


<!-- b000852 | prose | pages [24] -->
Here we use a random method to generate convex samplings, which smoothly connect two fixed points (the coping edge and bottom edge). We generate the sample points forming convex curve using following method:

<!-- b000853 | furniture | pages [24] -->


<!-- b000854 | prose | pages [24] -->
𝒈𝒊𝒗𝒆𝒏: h = 0.01, W = width −flat

<!-- b000855 | prose | pages [24] -->
, H = Height, 2

<!-- b000856 | prose | pages [24] -->
x n = nh, n = 1 … N, N = W

<!-- b000857 | furniture | pages [24] -->


<!-- b000858 | prose | pages [24] -->
h + 1

<!-- b000859 | prose | pages [24] -->
𝒈𝒐𝒂𝒍: to generate sampling points of  Convex curve as transition part

<!-- b000860 | prose | pages [24] -->
y = y x → x n , y n

<!-- b000861 | prose | pages [24] -->
s. t.  y n > 𝑦 n −1 , y 1 = 0, y N = H

<!-- b000862 | furniture | pages [24] -->


<!-- b000863 | prose | pages [24] -->
𝑴𝒆𝒕𝒉𝒐𝒅: we define k i = y i + 1 −y i , 1 < 𝑖< 𝑁, 𝑠𝑜 𝑘 i > 𝑘 i −1 > 0

<!-- b000864 | prose | pages [24] -->
N−1

<!-- b000865 | prose | pages [24] -->
N−1

<!-- b000866 | prose | pages [24] -->
= H

<!-- b000867 | prose | pages [24] -->
h = y N = H → k(i)

<!-- b000868 | prose | pages [24] -->
k(i)

<!-- b000869 | prose | pages [24] -->
i=2

<!-- b000870 | furniture | pages [24] -->


<!-- b000871 | prose | pages [24] -->
h

<!-- b000872 | prose | pages [24] -->
i=2

<!-- b000873 | furniture | pages [25] -->
Team # 9582

<!-- b000874 | furniture | pages [25] -->


<!-- b000875 | furniture | pages [25] -->


<!-- b000876 | furniture | pages [25] -->
Page 25 of 34

<!-- b000877 | prose | pages [25] -->
We generate random numbers and use the summation of previous i numbers as k(i).

<!-- b000878 | prose | pages [25] -->
H

<!-- b000879 | prose | pages [25] -->
h, we can acquire k(i). Finally, the locations of sampling points

<!-- b000880 | prose | pages [25] -->
After normalized by

<!-- b000881 | prose | pages [25] -->
are determined after all their tangent values have determined, and therefore the sampling points of a random convex curve (x(i),y(i)) is acquired.

<!-- b000882 | furniture | pages [25] -->


<!-- b000883 | prose | pages [25] -->
The result of Gene Algorithm leads to the best curve, which provide maximum “Vertical Air”

<!-- b000884 | furniture | pages [25] -->


<!-- b000885 | prose | pages [25] -->
0

<!-- b000886 | prose | pages [25] -->
0.1

<!-- b000887 | prose | pages [25] -->
0.09

<!-- b000888 | prose | pages [25] -->
-0.5

<!-- b000889 | prose | pages [25] -->
0.08

<!-- b000890 | prose | pages [25] -->
-1

<!-- b000891 | prose | pages [25] -->
0.07

<!-- b000892 | prose | pages [25] -->
0.06

<!-- b000893 | prose | pages [25] -->
-1.5

<!-- b000894 | prose | pages [25] -->
0.05

<!-- b000895 | prose | pages [25] -->
-2

<!-- b000896 | prose | pages [25] -->
0.04

<!-- b000897 | prose | pages [25] -->
0.03

<!-- b000898 | prose | pages [25] -->
-2.5

<!-- b000899 | prose | pages [25] -->
0.02

<!-- b000900 | prose | pages [25] -->
-3

<!-- b000901 | prose | pages [25] -->
0.01

<!-- b000902 | prose | pages [25] -->
-3.5

<!-- b000903 | prose | pages [25] -->
0

<!-- b000904 | prose | pages [25] -->
-10 -5 0 5 10

<!-- b000905 | prose | pages [25] -->
0 50 100

<!-- b000906 | prose | pages [25] -->
(a)

<!-- b000907 | prose | pages [25] -->
0 0

<!-- b000908 | prose | pages [25] -->
0.025

<!-- b000909 | prose | pages [25] -->
-0.5 -0.5

<!-- b000910 | prose | pages [25] -->
0.02

<!-- b000911 | prose | pages [25] -->
-1 -1

<!-- b000912 | prose | pages [25] -->
0.015

<!-- b000913 | prose | pages [25] -->
-1.5 -1.5

<!-- b000914 | prose | pages [25] -->
-2 -2

<!-- b000915 | prose | pages [25] -->
0.01

<!-- b000916 | prose | pages [25] -->
-2.5 -2.5

<!-- b000917 | prose | pages [25] -->
0.005

<!-- b000918 | prose | pages [25] -->
-3 -3

<!-- b000919 | prose | pages [25] -->
-3.5 -3.5

<!-- b000920 | prose | pages [25] -->
0

<!-- b000921 | prose | pages [25] -->
-10 -5 0 5 10

<!-- b000922 | prose | pages [25] -->
0 50 100

<!-- b000923 | furniture | pages [25] -->


<!-- b000924 | prose | pages [25] -->
(b)

<!-- b000925 | furniture | pages [25] -->


<!-- b000926 | prose | pages [25] -->
0

<!-- b000927 | prose | pages [25] -->
-1

<!-- b000928 | prose | pages [25] -->
-2

<!-- b000929 | prose | pages [25] -->
-3

<!-- b000930 | prose | pages [25] -->
-6 -4 -2 0 2 4 6

<!-- b000931 | furniture | pages [25] -->


<!-- b000932 | prose | pages [25] -->
(c)                          (d)

<!-- b000933 | caption | pages [25] -->
Figure 23 Result of optimizing transition shape using Gene Algorithm

<!-- b000934 | furniture | pages [25] -->


<!-- b000935 | prose | pages [25] -->
(a) initial “generation” of curves(blue) in Gene Algorithm and their fitness values (b) finishing “generation” of curves (blue) and their fitness values (c) the shape of the optimized shape of course (d) fitting the resulting curve with 2nd order curve, which ends up into an ellipse

<!-- b000936 | furniture | pages [25] -->


<!-- b000937 | prose | pages [25] -->
We fit the optimistic curve as second order differentiable curves and it ends up into an ellipse and adding a ‘Vert’ about half meter long. This result matches the previous work claiming the transition should be an ellipse [4].

<!-- b000938 | furniture | pages [25] -->


<!-- b000939 | furniture | pages [25] -->


<!-- b000940 | furniture | pages [26] -->
Team # 9582

<!-- b000941 | prose | pages [26] -->
 Global Optimum

<!-- b000942 | furniture | pages [26] -->


<!-- b000943 | furniture | pages [26] -->


<!-- b000944 | furniture | pages [26] -->
Page 26 of 34

<!-- b000945 | prose | pages [26] -->
To compute the global optimal shape of course, we just set width, height of the ramp and gradient angle to 15m, 3.5m and 18°respectively (recommended value by FIS) and use Gene Algorithm to optimize the entire curve.

<!-- b000946 | furniture | pages [26] -->


<!-- b000947 | prose | pages [26] -->
10

<!-- b000948 | prose | pages [26] -->
5

<!-- b000949 | prose | pages [26] -->
0

<!-- b000950 | prose | pages [26] -->
-5 0

<!-- b000951 | prose | pages [26] -->
-20

<!-- b000952 | prose | pages [26] -->
-40

<!-- b000953 | prose | pages [26] -->
-60

<!-- b000954 | prose | pages [26] -->
0

<!-- b000955 | prose | pages [26] -->
-0.5

<!-- b000956 | prose | pages [26] -->
-1

<!-- b000957 | prose | pages [26] -->
-1.5

<!-- b000958 | prose | pages [26] -->
-2

<!-- b000959 | prose | pages [26] -->
-2.5

<!-- b000960 | prose | pages [26] -->
-3

<!-- b000961 | prose | pages [26] -->
-3.5 -8 -6 -4 -2 0 2 4 6 8

<!-- b000962 | prose | pages [26] -->
(b)

<!-- b000963 | prose | pages [26] -->
10 5 0

<!-- b000964 | prose | pages [26] -->
-5

<!-- b000965 | prose | pages [26] -->
-10 -10

<!-- b000966 | furniture | pages [26] -->


<!-- b000967 | prose | pages [26] -->
(a)

<!-- b000968 | prose | pages [26] -->
Ellipse Fitting for Optimal Shape of Course 2

<!-- b000969 | prose | pages [26] -->
1

<!-- b000970 | prose | pages [26] -->
0

<!-- b000971 | prose | pages [26] -->
-1

<!-- b000972 | prose | pages [26] -->
-2

<!-- b000973 | prose | pages [26] -->
-3

<!-- b000974 | prose | pages [26] -->
-4

<!-- b000975 | furniture | pages [26] -->


<!-- b000976 | prose | pages [26] -->
-8 -6 -4 -2 0 2 4 6

<!-- b000977 | prose | pages [26] -->
(c)

<!-- b000978 | caption | pages [26] -->
Figure 24 global optimized result of the shape of course for largest “vertical air”

<!-- b000979 | prose | pages [26] -->
(a) Course of half-pipe and path of snowboarder (b) The shape of course cross-section (c) Fitting the optimal curve with an ellipse This optimized shape provides largest “Vertical Air”, and it is also close to an ellipse.

<!-- b000980 | furniture | pages [26] -->


<!-- b000981 | heading | pages [26] -->
Conclusion 1:

<!-- b000982 | prose | pages [26] -->
Wider and higher ramp, larger gradient angle, g, chosen by skilled snowboarder all contribute to “Vertical Air”.

<!-- b000983 | furniture | pages [26] -->


<!-- b000984 | prose | pages [26] -->
While the width and height of the course is fixed, the shape of the course is close to an ellipse.

<!-- b000985 | furniture | pages [26] -->


<!-- b000986 | prose | pages [26] -->
Sometimes, a short ‘Vert’ and ‘Flat’ is also preferred.

<!-- b000987 | furniture | pages [26] -->


<!-- b000988 | furniture | pages [27] -->
Team # 9582

<!-- b000989 | prose | pages [27] -->
Question2:

<!-- b000990 | furniture | pages [27] -->


<!-- b000991 | furniture | pages [27] -->


<!-- b000992 | furniture | pages [27] -->
Page 27 of 34

<!-- b000993 | prose | pages [27] -->
Tailor the shape to optimize other possible requirements, such as maximum twist in the air.

<!-- b000994 | furniture | pages [27] -->


<!-- b000995 | prose | pages [27] -->
Answer2:

<!-- b000996 | prose | pages [27] -->
We have tailored the shape of the course and optimize degree of rotation which correlates to following requirements respectively.

<!-- b000997 | heading | pages [27] -->
1) Optimize total duration of fly

<!-- b000998 | heading | pages [27] -->
2) Optimize initial angular momentum along z-direction

<!-- b000999 | heading | pages [27] -->
3) Optimize total degree of rotation

<!-- b001000 | furniture | pages [27] -->


<!-- b001001 | heading | pages [27] -->
1) Optimize total duration of fly

<!-- b001002 | prose | pages [27] -->
Default Values W(width) 15m B(length of flat bottom) 5m

<!-- b001003 | prose | pages [27] -->
𝑧𝑡(𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝑜𝑓𝑡𝑎𝑟𝑡 𝑝𝑜𝑖𝑛𝑡 𝑜𝑓 𝐹𝑙𝑦) 10m

<!-- b001004 | furniture | pages [27] -->


<!-- b001005 | prose | pages [27] -->
H(height) 3.5m 𝜃 (gradient angle of the venue, the

<!-- b001006 | prose | pages [27] -->
18°

<!-- b001007 | prose | pages [27] -->
angle between z axis and ground)

<!-- b001008 | prose | pages [27] -->
Transition Shape Standard

<!-- b001009 | prose | pages [27] -->
ellipse

<!-- b001010 | prose | pages [27] -->
Using the parameters as above table shows, we got following results concerning the factors to duration of fly, which are also known as “air time”.

<!-- b001011 | furniture | pages [27] -->


<!-- b001012 | prose | pages [27] -->
relationship between width & FlyTime/s

<!-- b001013 | prose | pages [27] -->
3

<!-- b001014 | prose | pages [27] -->
2.95

<!-- b001015 | prose | pages [27] -->
2.9

<!-- b001016 | prose | pages [27] -->
2.85

<!-- b001017 | prose | pages [27] -->
2.8

<!-- b001018 | prose | pages [27] -->
FlyTime/s

<!-- b001019 | prose | pages [27] -->
FlyTime/s

<!-- b001020 | prose | pages [27] -->
2.75

<!-- b001021 | prose | pages [27] -->
2.7

<!-- b001022 | prose | pages [27] -->
2.65

<!-- b001023 | prose | pages [27] -->
2.6

<!-- b001024 | prose | pages [27] -->
2.55

<!-- b001025 | prose | pages [27] -->
2.5 12 14 16 18 20 22 24 26

<!-- b001026 | prose | pages [27] -->
width

<!-- b001027 | prose | pages [27] -->
relationship between flat & FlyTime/s

<!-- b001028 | prose | pages [27] -->
3 3

<!-- b001029 | prose | pages [27] -->
2.95 2.95

<!-- b001030 | prose | pages [27] -->
2.9 2.9

<!-- b001031 | prose | pages [27] -->
2.85 2.85

<!-- b001032 | prose | pages [27] -->
2.8 2.8

<!-- b001033 | prose | pages [27] -->
2.75 2.75

<!-- b001034 | prose | pages [27] -->
2.7 2.7

<!-- b001035 | prose | pages [27] -->
2.65 2.65

<!-- b001036 | prose | pages [27] -->
2.6 2.6

<!-- b001037 | prose | pages [27] -->
2.55 2.55

<!-- b001038 | prose | pages [27] -->
2.5 2.5 0 0 1 2 3 4 5 6

<!-- b001039 | furniture | pages [27] -->


<!-- b001040 | prose | pages [27] -->
flat

<!-- b001041 | prose | pages [27] -->
(a)                               (b)

<!-- b001042 | furniture | pages [28] -->
Team # 9582

<!-- b001043 | prose | pages [28] -->
relationship between zlength & FlyTime/s

<!-- b001044 | prose | pages [28] -->
3

<!-- b001045 | prose | pages [28] -->
2.95

<!-- b001046 | prose | pages [28] -->
2.9

<!-- b001047 | prose | pages [28] -->
2.85

<!-- b001048 | prose | pages [28] -->
2.8

<!-- b001049 | prose | pages [28] -->
FlyTime/s

<!-- b001050 | prose | pages [28] -->
FlyTime/s

<!-- b001051 | prose | pages [28] -->
2.75

<!-- b001052 | prose | pages [28] -->
2.7

<!-- b001053 | prose | pages [28] -->
2.65

<!-- b001054 | prose | pages [28] -->
2.6

<!-- b001055 | prose | pages [28] -->
2.55

<!-- b001056 | prose | pages [28] -->
2.5 0 5 10 15

<!-- b001057 | prose | pages [28] -->
zlength

<!-- b001058 | furniture | pages [28] -->


<!-- b001059 | furniture | pages [28] -->


<!-- b001060 | furniture | pages [28] -->
Page 28 of 34

<!-- b001061 | prose | pages [28] -->
relationship between height & FlyTime/s

<!-- b001062 | prose | pages [28] -->
3 3

<!-- b001063 | prose | pages [28] -->
2.95 2.95

<!-- b001064 | prose | pages [28] -->
2.9 2.9

<!-- b001065 | prose | pages [28] -->
2.85 2.85

<!-- b001066 | prose | pages [28] -->
2.8 2.8

<!-- b001067 | prose | pages [28] -->
2.75 2.75

<!-- b001068 | prose | pages [28] -->
2.7 2.7

<!-- b001069 | prose | pages [28] -->
2.65 2.65

<!-- b001070 | prose | pages [28] -->
2.6 2.6

<!-- b001071 | prose | pages [28] -->
2.55 2.55

<!-- b001072 | prose | pages [28] -->
2.5 2.5 2 2 2.5 3 3.5 4 4.5 5 5.5 6

<!-- b001073 | furniture | pages [28] -->


<!-- b001074 | prose | pages [28] -->
height

<!-- b001075 | prose | pages [28] -->
(c)                              (d)

<!-- b001076 | prose | pages [28] -->
relationship between theta & FlyTime/s

<!-- b001077 | prose | pages [28] -->
4.5

<!-- b001078 | prose | pages [28] -->
4

<!-- b001079 | prose | pages [28] -->
3.5

<!-- b001080 | prose | pages [28] -->
FlyTime/s

<!-- b001081 | prose | pages [28] -->
3

<!-- b001082 | prose | pages [28] -->
2.5

<!-- b001083 | prose | pages [28] -->
2 0 5 10 15 20 25 30 35 40 45

<!-- b001084 | furniture | pages [28] -->


<!-- b001085 | prose | pages [28] -->
theta

<!-- b001086 | prose | pages [28] -->
(e)

<!-- b001087 | caption | pages [28] -->
Figure 25 Effects on “air time” by width(a), flat length(b), 𝑍𝑡 points before fly(c),

<!-- b001088 | prose | pages [28] -->
height(d) and gradient angle 𝜃 (e)

<!-- b001089 | furniture | pages [28] -->


<!-- b001090 | furniture | pages [28] -->


<!-- b001091 | prose | pages [28] -->
Simulation results show that the duration of fly (tf) is almost positive linear to ramp width, ramp height and the flat length. Duration of fly reaches locally optimum when zt is around 6 meter, indicating that snowboarders’ choice for path can help them to fly for a longer time. Moreover, the larger the gradient angle 𝜃 is, the longer the fly lasts.

<!-- b001092 | furniture | pages [28] -->


<!-- b001093 | heading | pages [28] -->
Conclusion for (1):

<!-- b001094 | prose | pages [28] -->
Here we enumerate width from 13 to 18, height from 2 to 6, flat length from 4 to 6, zt from 0 to 15 and 𝜃 from 15° to 20° to optimize the fly time and obtain the optimal shape of course:

<!-- b001095 | furniture | pages [28] -->


<!-- b001096 | prose | pages [28] -->
Width = 18m, Height = 5m, Flat = 6m, zt = 4m, 𝜽 = 20° tf = 2.749s

<!-- b001097 | furniture | pages [28] -->


<!-- b001098 | heading | pages [28] -->
2) Optimize initial angular momentum along z-axis

<!-- b001099 | prose | pages [28] -->
As we have computed before,

<!-- b001100 | prose | pages [28] -->
xt 2 + yt 2

<!-- b001101 | prose | pages [28] -->
Lz0 =

<!-- b001102 | prose | pages [28] -->
𝑙2m 3ρ0

<!-- b001103 | furniture | pages [29] -->
Team # 9582

<!-- b001104 | furniture | pages [29] -->


<!-- b001105 | furniture | pages [29] -->


<!-- b001106 | furniture | pages [29] -->
Page 29 of 34

<!-- b001107 | prose | pages [29] -->
Thus, the transition shape is dominant so we use Gene Algorithm to maximize the production of angular momentum:

<!-- b001108 | furniture | pages [29] -->


<!-- b001109 | heading | pages [29] -->
Conclusion for (2):

<!-- b001110 | prose | pages [29] -->
We use the parameter recommended by FIS, which also match the optimal parameters from our previous analysis of velocity before fly

<!-- b001111 | furniture | pages [29] -->


<!-- b001112 | prose | pages [29] -->
W(width) 18m B(length of flat bottom) 5m

<!-- b001113 | prose | pages [29] -->
𝑧𝑡(𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝑜𝑓𝑡𝑎𝑟𝑡 𝑝𝑜𝑖𝑛𝑡 𝑜𝑓 𝐹𝑙𝑦) 10m

<!-- b001114 | furniture | pages [29] -->


<!-- b001115 | prose | pages [29] -->
H(height) 3.5m 𝜃 (gradient angle of the

<!-- b001116 | prose | pages [29] -->
18°

<!-- b001117 | prose | pages [29] -->
venue, the angle between z

<!-- b001118 | prose | pages [29] -->
axis and ground)

<!-- b001119 | prose | pages [29] -->
Transition Shape To Be Optimized

<!-- b001120 | prose | pages [29] -->
Using Gene Algorithm, we obtain the optimal shape as follows:

<!-- b001121 | furniture | pages [29] -->


<!-- b001122 | prose | pages [29] -->
0

<!-- b001123 | prose | pages [29] -->
-0.5

<!-- b001124 | prose | pages [29] -->
-1

<!-- b001125 | prose | pages [29] -->
-1.5

<!-- b001126 | prose | pages [29] -->
-2

<!-- b001127 | prose | pages [29] -->
-2.5

<!-- b001128 | prose | pages [29] -->
-3

<!-- b001129 | prose | pages [29] -->
-3.5

<!-- b001130 | prose | pages [29] -->
-4 -8 -6 -4 -2 0 2 4 6 8

<!-- b001131 | prose | pages [29] -->
Ellipse Fitting of Optimal Shape of Course for Angular Momentum 3 3

<!-- b001132 | prose | pages [29] -->
2 2

<!-- b001133 | prose | pages [29] -->
1 1

<!-- b001134 | prose | pages [29] -->
0 0

<!-- b001135 | prose | pages [29] -->
-1 -1

<!-- b001136 | prose | pages [29] -->
-2 -2

<!-- b001137 | prose | pages [29] -->
-3 -3

<!-- b001138 | prose | pages [29] -->
-4 -4 -8 -8 -6 -4 -2 0 2 4

<!-- b001139 | furniture | pages [29] -->


<!-- b001140 | caption | pages [29] -->
Figure 26 The optimized shape of ramp cross-section for angular momentum (left)

<!-- b001141 | prose | pages [29] -->
and fitting the shape with 2nd order curve (right)

<!-- b001142 | furniture | pages [29] -->


<!-- b001143 | furniture | pages [29] -->


<!-- b001144 | prose | pages [29] -->
After fitting with second order curve, we found it is also closed to ellipse. And this curve is tailored from the other optimal curve for “Vertical Air” in question 1. The “Vert” and “Flat” is much shorter. This result makes sense since “Vert” and a long “Flat” will result in large (actually infinite) radius of curvature.

<!-- b001145 | furniture | pages [29] -->


<!-- b001146 | heading | pages [29] -->
3) Optimize total degree of rotation

<!-- b001147 | furniture | pages [29] -->


<!-- b001148 | prose | pages [29] -->
Plus, the total degree of rotation also is affect by duration of fly.

<!-- b001149 | furniture | pages [29] -->


<!-- b001150 | prose | pages [29] -->
Θ = 𝜔𝑡𝑓 and 𝜔∝𝐿0

<!-- b001151 | furniture | pages [29] -->


<!-- b001152 | prose | pages [29] -->
So, we use Gene Algorithm to optimize the shape of the course with recommended width (15m) and height (3.5m) of ramp, in order to obtain largest production of initial angular momentum and duration of fly.

<!-- b001153 | furniture | pages [29] -->


<!-- b001154 | furniture | pages [30] -->
Team # 9582

<!-- b001155 | heading | pages [30] -->
Conclusion for 3):

<!-- b001156 | furniture | pages [30] -->


<!-- b001157 | furniture | pages [30] -->


<!-- b001158 | furniture | pages [30] -->
Page 30 of 34

<!-- b001159 | prose | pages [30] -->
The resulting optimum of Gene Algorithm is shown below.

<!-- b001160 | prose | pages [30] -->
0

<!-- b001161 | prose | pages [30] -->
-0.5

<!-- b001162 | prose | pages [30] -->
-1

<!-- b001163 | prose | pages [30] -->
-1.5

<!-- b001164 | prose | pages [30] -->
-2

<!-- b001165 | prose | pages [30] -->
-2.5

<!-- b001166 | prose | pages [30] -->
-3

<!-- b001167 | prose | pages [30] -->
-3.5 -8 -6 -4 -2 0 2 4 6 8

<!-- b001168 | prose | pages [30] -->
10 10

<!-- b001169 | prose | pages [30] -->
5 5

<!-- b001170 | prose | pages [30] -->
0 0

<!-- b001171 | prose | pages [30] -->
-5 -5 0 0

<!-- b001172 | prose | pages [30] -->
10

<!-- b001173 | prose | pages [30] -->
-20

<!-- b001174 | prose | pages [30] -->
5 0

<!-- b001175 | prose | pages [30] -->
-40

<!-- b001176 | prose | pages [30] -->
-5

<!-- b001177 | prose | pages [30] -->
-60

<!-- b001178 | prose | pages [30] -->
-10

<!-- b001179 | furniture | pages [30] -->


<!-- b001180 | caption | pages [30] -->
Figure 27 The optimized shape of ramp cross-section for total degree of rotation (left)

<!-- b001181 | prose | pages [30] -->
and the course of optimal pipe and the path of snowboarder (right)

<!-- b001182 | furniture | pages [30] -->


<!-- b001183 | furniture | pages [30] -->


<!-- b001184 | prose | pages [30] -->
This curve can also be fitted with second order curve, which is an ellipse as well.

<!-- b001185 | prose | pages [30] -->
Ellipse Fitting of Optimal Shape of Course for Total Degree of Rotation 3

<!-- b001186 | prose | pages [30] -->
2

<!-- b001187 | prose | pages [30] -->
1

<!-- b001188 | prose | pages [30] -->
0

<!-- b001189 | prose | pages [30] -->
-1

<!-- b001190 | prose | pages [30] -->
-2

<!-- b001191 | prose | pages [30] -->
-3

<!-- b001192 | prose | pages [30] -->
-4 -8 -6 -4 -2 -2 0 2 4

<!-- b001193 | caption | pages [30] -->
Figure 28  fitting the result with 2nd order curve

<!-- b001194 | furniture | pages [30] -->


<!-- b001195 | prose | pages [30] -->
Tailor the course

<!-- b001196 | furniture | pages [30] -->


<!-- b001197 | prose | pages [30] -->
We have also modified the objective function and implemented Gene Algorithm for the tradeoff between “Vertical Air” and Total Degree of Rotation. As the perception model[9] and automated scoring system[10], developed by Harding JW, etc, has shown, the overall performance of half-pipe snowboard can be treated as a complex combination of “Vertical Air”, Average Air Time(AAT) and Average Degree of Rotation (ADR). They also put forward an equation to predict score of snowboarder automatically.

<!-- b001198 | prose | pages [30] -->
Predicted Score = 11.424AAT + 0.013ADR −2.223

<!-- b001199 | furniture | pages [30] -->


<!-- b001200 | prose | pages [30] -->
This function is justified empirically and also makes good sense. (As we have derived before, air time (flying time) is almost proportion to the square root of “Vertical Air” in the motion of Projectile, so they can be regarded as a single criterion) We set objective function in Gene Algorithm to become the “Predicted Score”. In this way,

<!-- b001201 | furniture | pages [31] -->
Team # 9582

<!-- b001202 | furniture | pages [31] -->


<!-- b001203 | furniture | pages [31] -->


<!-- b001204 | furniture | pages [31] -->
Page 31 of 34

<!-- b001205 | prose | pages [31] -->
we are able to find the optimal shape of course, as shown below. It enjoys the characteristics of previous optimized shapes based on different objective functions, which may provide the eclectically best snowboard performance to certain extent.

<!-- b001206 | furniture | pages [31] -->


<!-- b001207 | prose | pages [31] -->
Fitting with 2nd order curves, we found this curve is perfectly fitting by two ellipse which fit optimal curves for “vertical air” and total degree of rotation respectively. Judging by the formula of predicted score, this course could get more than 46, supporting the validity of this combined criterion.

<!-- b001208 | furniture | pages [31] -->


<!-- b001209 | prose | pages [31] -->
8

<!-- b001210 | prose | pages [31] -->
6

<!-- b001211 | prose | pages [31] -->
4

<!-- b001212 | prose | pages [31] -->
2

<!-- b001213 | prose | pages [31] -->
0

<!-- b001214 | prose | pages [31] -->
-2

<!-- b001215 | prose | pages [31] -->
0

<!-- b001216 | prose | pages [31] -->
-10

<!-- b001217 | prose | pages [31] -->
-20

<!-- b001218 | prose | pages [31] -->
-30

<!-- b001219 | prose | pages [31] -->
-40

<!-- b001220 | prose | pages [31] -->
0 -50 -5

<!-- b001221 | prose | pages [31] -->
0

<!-- b001222 | prose | pages [31] -->
-0.5

<!-- b001223 | prose | pages [31] -->
-1

<!-- b001224 | prose | pages [31] -->
-1.5

<!-- b001225 | prose | pages [31] -->
-2

<!-- b001226 | prose | pages [31] -->
-2.5

<!-- b001227 | prose | pages [31] -->
-3

<!-- b001228 | prose | pages [31] -->
-3.5

<!-- b001229 | prose | pages [31] -->
5 5

<!-- b001230 | prose | pages [31] -->
-8 -6 -4 -2 0 2 4 6 8

<!-- b001231 | furniture | pages [31] -->


<!-- b001232 | prose | pages [31] -->
(a)                             (b)

<!-- b001233 | prose | pages [31] -->
3

<!-- b001234 | furniture | pages [31] -->


<!-- b001235 | prose | pages [31] -->
Vertical Air

<!-- b001236 | prose | pages [31] -->
Optimal Shape for Scoring System

<!-- b001237 | prose | pages [31] -->
2

<!-- b001238 | prose | pages [31] -->
1

<!-- b001239 | prose | pages [31] -->
0

<!-- b001240 | prose | pages [31] -->
-1

<!-- b001241 | prose | pages [31] -->
-2

<!-- b001242 | prose | pages [31] -->
-3

<!-- b001243 | prose | pages [31] -->
-4

<!-- b001244 | furniture | pages [31] -->


<!-- b001245 | prose | pages [31] -->
-8 -6 -4

<!-- b001246 | prose | pages [31] -->
Total Degree Hybrid Scoring Fit 1 Fit 2

<!-- b001247 | prose | pages [31] -->
-2 -2 0 2 4 6

<!-- b001248 | prose | pages [31] -->
(c)

<!-- b001249 | caption | pages [31] -->
Figure 29 global eclectically optimal results

<!-- b001250 | furniture | pages [31] -->


<!-- b001251 | prose | pages [31] -->
(a) Course and path (b) the optimal shape of the course, judging by eclectic scoring (c) Fitting the resulting optimum with 2nd order curves.

<!-- b001252 | furniture | pages [31] -->


<!-- b001253 | prose | pages [31] -->
Question3:

<!-- b001254 | prose | pages [31] -->
What tradeoffs may be required to develop a “practical” course?

<!-- b001255 | furniture | pages [32] -->
Team # 9582

<!-- b001256 | prose | pages [32] -->
Answer 3:

<!-- b001257 | prose | pages [32] -->
a. Radius of Curvature

<!-- b001258 | furniture | pages [32] -->


<!-- b001259 | furniture | pages [32] -->


<!-- b001260 | furniture | pages [32] -->
Page 32 of 34

<!-- b001261 | prose | pages [32] -->
The radius of curvature of the half-pipe cross-section cannot be too small, or the snow may fall off[12]. And due to the fact that the snowboard is more than one meter long, it is obvious that a too small radius of curvature is dangerous and infeasible.

<!-- b001262 | furniture | pages [32] -->


<!-- b001263 | prose | pages [32] -->
b. Flat bottom Since the 1980s, half-pipes have had extended flat ground (the flat bottom) added between the quarter-pipes; the original-style half-pipes have become deprecated. The flat ground gives the athlete time to regain balance after landing and more time to prepare for the next trick.[1]

<!-- b001264 | furniture | pages [32] -->


<!-- b001265 | prose | pages [32] -->
Moreover, according to our numerical computation, when a half-pipe has wider flat bottom, Ereach and Eleave decreases, whereas the duration of fly, yt  and vertical air increases. The change in number of cycles is negligible.

<!-- b001266 | furniture | pages [32] -->


<!-- b001267 | prose | pages [32] -->
c. Ereach Ereach represents the final kinetic energy of a cycle, as well as the E0 of the next cycle. Considering that the snowboarder experiences more than one cycle, it is not wise to chase a higher jump at the cost of less Ereach .

<!-- b001268 | furniture | pages [32] -->


<!-- b001269 | prose | pages [32] -->
According to our numerical computation, the wider the course is, the larger the vertical air is. However, wider course leads to lower final kinetic energy (Ereach), which is unwelcomed. It is similar with the height of the half-pipe: as long as height is less than width, higher course results in larger vertical air while less Ereach. And flat is also has the same effect here (as shown in Figure 30).

<!-- b001270 | furniture | pages [32] -->


<!-- b001271 | prose | pages [32] -->
Therefore, the half-pipe should not be too wide, too high or too flat.

<!-- b001272 | furniture | pages [32] -->


<!-- b001273 | prose | pages [32] -->
width Vs Ereach

<!-- b001274 | prose | pages [32] -->
4 1.39 x 10

<!-- b001275 | prose | pages [32] -->
1.38

<!-- b001276 | prose | pages [32] -->
1.37

<!-- b001277 | prose | pages [32] -->
1.36

<!-- b001278 | prose | pages [32] -->
Ereach

<!-- b001279 | prose | pages [32] -->
1.35

<!-- b001280 | prose | pages [32] -->
1.34

<!-- b001281 | prose | pages [32] -->
1.33

<!-- b001282 | prose | pages [32] -->
1.32 13 14 15 16 17 18

<!-- b001283 | prose | pages [32] -->
width

<!-- b001284 | prose | pages [32] -->
width Vs VerticalAir

<!-- b001285 | prose | pages [32] -->
9.9

<!-- b001286 | prose | pages [32] -->
9.8

<!-- b001287 | prose | pages [32] -->
9.7

<!-- b001288 | prose | pages [32] -->
9.6

<!-- b001289 | prose | pages [32] -->
VerticalAir

<!-- b001290 | prose | pages [32] -->
9.5

<!-- b001291 | prose | pages [32] -->
9.4

<!-- b001292 | prose | pages [32] -->
9.3

<!-- b001293 | prose | pages [32] -->
9.2

<!-- b001294 | prose | pages [32] -->
9.1

<!-- b001295 | prose | pages [32] -->
9 13 14 15 16 17 18

<!-- b001296 | prose | pages [32] -->
width

<!-- b001297 | furniture | pages [32] -->


<!-- b001298 | furniture | pages [33] -->
Team # 9582

<!-- b001299 | prose | pages [33] -->
height Vs Ereach

<!-- b001300 | prose | pages [33] -->
4 1.44 x 10

<!-- b001301 | prose | pages [33] -->
1.42

<!-- b001302 | prose | pages [33] -->
1.4

<!-- b001303 | prose | pages [33] -->
1.38

<!-- b001304 | prose | pages [33] -->
Ereach

<!-- b001305 | prose | pages [33] -->
1.36

<!-- b001306 | prose | pages [33] -->
1.34

<!-- b001307 | prose | pages [33] -->
1.32

<!-- b001308 | prose | pages [33] -->
1.3 1 2 3 4 5 6

<!-- b001309 | prose | pages [33] -->
height

<!-- b001310 | prose | pages [33] -->
flat Vs Ereach

<!-- b001311 | prose | pages [33] -->
4 1.405 x 10

<!-- b001312 | prose | pages [33] -->
1.4

<!-- b001313 | prose | pages [33] -->
1.395

<!-- b001314 | prose | pages [33] -->
1.39

<!-- b001315 | prose | pages [33] -->
1.385

<!-- b001316 | prose | pages [33] -->
Ereach

<!-- b001317 | prose | pages [33] -->
1.38

<!-- b001318 | prose | pages [33] -->
1.375

<!-- b001319 | prose | pages [33] -->
1.37

<!-- b001320 | prose | pages [33] -->
1.365

<!-- b001321 | prose | pages [33] -->
1.36

<!-- b001322 | prose | pages [33] -->
1.355 0 1 2 3 4 5 6

<!-- b001323 | prose | pages [33] -->
flat

<!-- b001324 | furniture | pages [33] -->


<!-- b001325 | furniture | pages [33] -->


<!-- b001326 | furniture | pages [33] -->
Page 33 of 34

<!-- b001327 | prose | pages [33] -->
height Vs VerticalAir

<!-- b001328 | prose | pages [33] -->
10.2

<!-- b001329 | prose | pages [33] -->
10

<!-- b001330 | prose | pages [33] -->
9.8

<!-- b001331 | prose | pages [33] -->
9.6

<!-- b001332 | prose | pages [33] -->
VerticalAir

<!-- b001333 | prose | pages [33] -->
9.4

<!-- b001334 | prose | pages [33] -->
9.2

<!-- b001335 | prose | pages [33] -->
9

<!-- b001336 | prose | pages [33] -->
8.8

<!-- b001337 | prose | pages [33] -->
8.6

<!-- b001338 | prose | pages [33] -->
8.4

<!-- b001339 | prose | pages [33] -->
8.2 1 2 3 4 5 6

<!-- b001340 | prose | pages [33] -->
height

<!-- b001341 | furniture | pages [33] -->


<!-- b001342 | prose | pages [33] -->
flat Vs VerticalAir

<!-- b001343 | prose | pages [33] -->
9.45

<!-- b001344 | prose | pages [33] -->
9.4

<!-- b001345 | prose | pages [33] -->
9.35

<!-- b001346 | prose | pages [33] -->
9.3

<!-- b001347 | prose | pages [33] -->
VerticalAir

<!-- b001348 | prose | pages [33] -->
9.25

<!-- b001349 | prose | pages [33] -->
9.2

<!-- b001350 | prose | pages [33] -->
9.15

<!-- b001351 | prose | pages [33] -->
9.1

<!-- b001352 | prose | pages [33] -->
9.05

<!-- b001353 | prose | pages [33] -->
9 0 1 2 3 4 5 6

<!-- b001354 | prose | pages [33] -->
flat

<!-- b001355 | furniture | pages [33] -->


<!-- b001356 | prose | pages [33] -->
Figure 30

<!-- b001357 | furniture | pages [33] -->


<!-- b001358 | prose | pages [33] -->
d. number of cycles In the Winter Olympic Games, a snowboarder must perform 5 to 8 acrobatic tricks in a run. Thus, a snowboarder should complete 5 to 8 cycles in the half-pipe’s 110m extent.

<!-- b001359 | furniture | pages [33] -->


<!-- b001360 | prose | pages [33] -->
From the numerical computation above, it can be learnt that both vertical air and Ereach would become larger if 𝜃 (the angle between z axis and the horizontal plane) increases. Nonetheless, since Sf (the displacement along z direction during the fly) increases as 𝜃 increases, a snowboarder would find it difficult to perform enough acrobatic tricks on a very steep half-pipe.

<!-- b001361 | furniture | pages [33] -->


<!-- b001362 | prose | pages [33] -->
Hence, 𝜃 should not be too large.

<!-- b001363 | furniture | pages [33] -->


<!-- b001364 | heading | pages [33] -->
Strength and Weakness

<!-- b001365 | prose | pages [33] -->
 The model describes the entire proceeding of movement in a detailed manner,

<!-- b001366 | prose | pages [33] -->
which pertains to intricate correlation between many physical quantities and is well-organized.

<!-- b001367 | furniture | pages [34] -->
Team # 9582

<!-- b001368 | furniture | pages [34] -->


<!-- b001369 | furniture | pages [34] -->
Page 34 of 34

<!-- b001370 | prose | pages [34] -->
 Precise numerical computation.  The results generated by numerical computation and the empirical data are in

<!-- b001371 | prose | pages [34] -->
agreement, lending support to the model and the corresponding computer codes.  The model takes the subjective influence of snowboarders into account and

<!-- b001372 | prose | pages [34] -->
notes the difference among them.  We established an objective evaluating function to compare different shapes of

<!-- b001373 | prose | pages [34] -->
courses.  We analyzed local optimal course (in order to learn the individual impact of the

<!-- b001374 | prose | pages [34] -->
parameters) as well as global optimal course (so as to shed light on the design of a half-pipe), and obtained numerical solution of them.

<!-- b001375 | furniture | pages [34] -->


<!-- b001376 | prose | pages [34] -->
 The model does not provide analytic solution of optimal course.  The model does not take the detailed mechanical characteristics and the

<!-- b001377 | prose | pages [34] -->
on-snow performance of snowboards into account.

<!-- b001378 | furniture | pages [34] -->


<!-- b001379 | prose | pages [34] -->
Reference

<!-- b001380 | prose | pages [34] -->
[1] en.wikipedia.org/wiki/Half-pipe [2] Jason William Harding, Colin Gordon Mackintosh, David Thomas Martin, Allan Geoffrey Hahn and Daniel Arthur James. Automated scoring for elite half-pipe snowboard competition: important sporting development or techno distraction? Sports Technol. 2008, 1, No. 6, 277–290 [3] www.ehow.com/way_5150384_olympic-half-pipe-snowboarding-rules.html [4] FIS SNOWBOARD JUDGES MANUAL 2003/2004 [5] Harding JW, Toohey K, Martin DT, Mackintosh C, Lindh AM, James DA. Automated Inertial Feedback For Half-pipe Snowboard Competition And The Community Perception. The Impact of Technology on Sport Ⅱ Fuss F.K., Subic A., Ujihashi S. Taylor & Francis London 2008; 20:845-850 [6] Harding JW, Toohey K, Martin DT, Hahn AG, James DA. Technology and Half-Pipe Snowboard Competition-Insight From Elite-Level Judges. The Engineering of Sport 7 Estivalet, M., Brisson, P.Springer-Verlag France 2008;2:467-476. [7] Performance Assessment innovations for Elite Snowboarding [8] 闫红光,刘平,郭峰 影响U 型场地单板雪上技巧出槽速度因素分析 Journal of Shenyang Sport University Vol.28 No.3 Jun. 2009 [9] 陈兢,李润,关佐恒 跳台滑雪运动雪板与雪面间摩擦系数研究 China Winter Sports No.04 1992. [10] 闫乃鹏 影响高山滑雪运动员滑行阻力的主要因素China Winter Sports No．5 0ct．2006 [11] FIS  SNOWBOARD RESORT INFORMATION SHEET Snowboard World Cup [12] wenku.baidu.com/view/e78ef328647d27284b735100.html

<!-- b001381 | furniture | pages [34] -->

