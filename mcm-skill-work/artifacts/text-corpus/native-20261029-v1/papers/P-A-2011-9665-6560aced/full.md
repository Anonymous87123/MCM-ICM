# P-A-2011-9665-6560aced

Status: machine-draft; not source-verified.


<!-- b000001 | heading | pages [1] -->
2011 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | title | pages [1] -->
9665

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | prose | pages [1] -->
T2 ________________

<!-- b000007 | prose | pages [1] -->
T3 ________________

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
F1 ________________

<!-- b000010 | prose | pages [1] -->
F2 ________________

<!-- b000011 | prose | pages [1] -->
F3 ________________

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T4 ________________

<!-- b000014 | prose | pages [1] -->
F4 ________________

<!-- b000015 | title | pages [1] -->
A

<!-- b000016 | title | pages [1] -->
A

<!-- b000017 | heading | pages [1] -->
Summary

<!-- b000018 | prose | pages [1] -->
As is known to all, in half-pipe games, the shape of the half-pipe has some influences on the performances of the snowboarders in many aspects, such as the “vertical air” and the average degree of rotation. It’s a big challenge for the snowboard designers to determine the shape of the half-pipe so as to achieve the desired performances. This problem can be attributed to an optimization problem.

<!-- b000019 | prose | pages [1] -->
For Question One, an interesting optimization model is constructed for the “vertical air” based on the theory of Dynamics. In particular, in order to achieve the maximum vertical distance above the edge of the half-pipe, we have derived the best height of the platform, which is 6.241 meters. On the other hand, by the relationship between the arc angle of the transitions and the vertical component of velocity, the best value for the arc angle of the transitions is determined to be 51.66°. Furthermore, according to the analytic expression of the curve of velocity recovery, we calculate the width of the flat is 19.18 meters. Finally, by the four steps method, the length of the U-shape bowl is calculated as 159.95 meters.

<!-- b000020 | prose | pages [1] -->
For Question Two, the mechanical characteristics model is constructed based on the theory of Sport Biomechanics. Particularly, we firstly derived the relationship between the torque and the horizontal twist angle. Then, the function relationship between the horizontal twist angle and the arc angle of the transitions is examined. Also, the situation of twist in the vertical direction can be discussed similarly and finally, in order to maximize the twist in the air, the best values of the arc angle of the transitions, the length and width of the U-shape bowl and the height of the platform are respectively calculated as 45°, 165.96 meters, 19.18 meters and 6.241 meters.

<!-- b000021 | prose | pages [1] -->
For Question Three, the weighted tradeoff model based on the “vertical air” and the twist angle is developed which ensures that the athlete would get the best scores. Based on the relationship among the “vertical air”, the twist angle and the corresponding scores obtained, we derived the appropriate weight coefficient and develop a practical course.

<!-- b000022 | prose | pages [1] -->
Moreover, the influences of other two different shapes of half-pipes on the “vertical air” and twist angle are also discussed. The model is tested by a numerical example and the sensitivity analysis about the initial velocity is performed. Finally, based on the analysis about the strengths and weaknesses of the proposed model, we have also considered the refinement of our model, taking the safety of the athlete and the air resistance into account.

<!-- b000023 | furniture | pages [2] -->
Team # 9665

<!-- b000024 | furniture | pages [2] -->
Page 1 of 30

<!-- b000025 | keywords | pages [2] -->
Keywords:

<!-- b000026 | prose | pages [2] -->
Snowboard Half-Pipe Theory of Dynamics Optimization Mechanical Characteristics

<!-- b000027 | prose | pages [2] -->
Fly Higher with More Twist: The Optimization of a Half-Pipe

<!-- b000028 | prose | pages [2] -->
Content

<!-- b000029 | prose | pages [2] -->
I Introduction..................................................................................................................2 II Symbol Definitions.....................................................................................................2 III Solution to Question One.......................................................................................... 3

<!-- b000030 | prose | pages [2] -->
3.1 Half Pipes......................................................................................................... 3 3.2 The Description of Half-Pipe We Focused.......................................................4 3.3 Basic Model......................................................................................................4 3.3.1 Assumptions and Notations...................................................................5 3.3.2 The Analysis of Snowboarder’s Movement.......................................... 6 3.3.3 The Calculation of W ......................................................................... 6 f

<!-- b000031 | prose | pages [2] -->
3.3.4 The Discussion of W ..........................................................................7 p 3.3.5 The Function of W ............................................................................. 8 p 3.3.6 Approach Parameters of Half-Pipe........................................................9 IVMechanical Characteristics Model of Question Two...............................................16

<!-- b000032 | prose | pages [2] -->
4.1 Assumptions................................................................................................... 16 4.2 Torque.............................................................................................................16 4.3Mechanical characteristics.............................................................................. 16 4.4 The Determination of Parameters of Half-Pipe..............................................17 V Tradeoffs Model to Question Three..........................................................................18

<!-- b000033 | prose | pages [2] -->
5.1 The Determination of Parameters...................................................................18

<!-- b000034 | prose | pages [2] -->
5.2 The Inclined Angle of Half-Pipe’s Placement................................................19 VI The Discussion of other Kinds of Half Pipe........................................................... 20

<!-- b000035 | prose | pages [2] -->
6.1 The Half Pipe whose Transitions are Ellipse..................................................20 6.2 The Half-Pipe whose Flat is a Arc..................................................................21 VII The Verification of Our Models.............................................................................21

<!-- b000036 | prose | pages [2] -->
7.1 The Verification by Living Example..............................................................21 7.2 Sensitivity Analysis........................................................................................22 VIII Strengths and Weaknesses....................................................................................23

<!-- b000037 | prose | pages [2] -->
8.1 Strengths.........................................................................................................23 8.2 Weaknesses.....................................................................................................24 IX The Refinement of our Model.................................................................................24

<!-- b000038 | prose | pages [2] -->
9.1 The Refined Model Considering the Air Resistance......................................24 9.2 The Refined Model Considering the Safety of Athlete.................................. 25 Reference......................................................................................................................26

<!-- b000039 | furniture | pages [3] -->
Team # 9665

<!-- b000040 | furniture | pages [3] -->
Page 2 of 30

<!-- b000041 | prose | pages [3] -->
Appendix...................................................................................................................... 27

<!-- b000042 | heading | pages [3] -->
I Introduction

<!-- b000043 | prose | pages [3] -->
The snowboarding was firstly introduced in the early 1970s and since then, it has become more and more popular all over the world.

<!-- b000044 | prose | pages [3] -->
However, with the rapid development of modern science and technology, there is no doubt that the sport equipment has played an important role for an athlete to improve the performance.

<!-- b000045 | prose | pages [3] -->
To meet the needs of skilled snowboarders, manufactures have introduced lots of different designs utilizing different materials and shapes for snowboarder courses, which are also currently known as half-pipes (Brennan, et al, 2003). In order to

<!-- b000046 | prose | pages [3] -->
achieve the desired performance, the key point in determining the shape of a half-pipe is to balance the possible requirements, such as the maximum production of “vertical air” and maximum twist in the air.

<!-- b000047 | prose | pages [3] -->
The performance of an athlete heavily depends on the total air time, average degree of rotation and the “vertical air”. In fact, these elements are also related to the shape of a half-pipe, especially the transition radius, the height and the length and width of the flat bottom of the half-pipe.

<!-- b000048 | prose | pages [3] -->
In this paper, the theory of Dynamics and Sport Biomechanics are employed to design the shape of a half-pipe for the purpose of maximizing the vertical distance and the twist in the air.

<!-- b000049 | prose | pages [3] -->
II Symbol Definitions

<!-- b000050 | prose | pages [3] -->
Symbol

<!-- b000051 | prose | pages [3] -->
xh

<!-- b000052 | prose | pages [3] -->
xr

<!-- b000053 | prose | pages [3] -->


<!-- b000054 | prose | pages [3] -->
Definition

<!-- b000055 | prose | pages [3] -->
the height of platform

<!-- b000056 | prose | pages [3] -->
the radius of transitions the arc angle of transitions

<!-- b000057 | prose | pages [3] -->
w x 

<!-- b000058 | prose | pages [3] -->
the width of flat

<!-- b000059 | prose | pages [3] -->
the twist angle of athlete in the sky

<!-- b000060 | prose | pages [3] -->
xa

<!-- b000061 | prose | pages [3] -->
 h  The length of platform vertical air the coefficient of sliding friction of the surface of half-pipe

<!-- b000062 | furniture | pages [4] -->
Team # 9665

<!-- b000063 | furniture | pages [4] -->
Page 3 of 30

<!-- b000064 | prose | pages [4] -->
the sustain force given by half pipe to snowboard an athlete

<!-- b000065 | prose | pages [4] -->
F N

<!-- b000066 | prose | pages [4] -->
 the angle between gravity and vertical direction of arc plane

<!-- b000067 | prose | pages [4] -->
S

<!-- b000068 | prose | pages [4] -->
the slide distance from backing to flat to completing acceleration

<!-- b000069 | prose | pages [4] -->
xr

<!-- b000070 | prose | pages [4] -->
the radius of transitions

<!-- b000071 | prose | pages [4] -->
sv

<!-- b000072 | prose | pages [4] -->
the velocity when athlete making flight part

<!-- b000073 | prose | pages [4] -->
v

<!-- b000074 | prose | pages [4] -->
the biggest velocity before sliding on the transitions

<!-- b000075 | prose | pages [4] -->
max

<!-- b000076 | prose | pages [4] -->
S

<!-- b000077 | prose | pages [4] -->
the slid distance during acceleration on the flat

<!-- b000078 | prose | pages [4] -->
max

<!-- b000079 | prose | pages [4] -->
f

<!-- b000080 | prose | pages [4] -->
the friction applied to snowboard

<!-- b000081 | prose | pages [4] -->
ca

<!-- b000082 | prose | pages [4] -->
the acceleration of athlete on the flat

<!-- b000083 | prose | pages [4] -->
tt

<!-- b000084 | prose | pages [4] -->
the time in the air for athlete  angular velocity of rotation

<!-- b000085 | prose | pages [4] -->
ˆ

<!-- b000086 | prose | pages [4] -->
M

<!-- b000087 | prose | pages [4] -->
the bending moment about x axis

<!-- b000088 | prose | pages [4] -->
x

<!-- b000089 | heading | pages [4] -->
III Solution to Question One

<!-- b000090 | heading | pages [4] -->
3.1 Half Pipes

<!-- b000091 | prose | pages [4] -->
A half-pipe is basically a U-shaped bowl that allows riders to move from one wall to the other by making jumps and performing Snowboarding Tricks on each transition (Half-pipe snowboarding).

<!-- b000092 | prose | pages [4] -->
There is a variety of different kinds of half-pipes utilized internationally and the main differences between them are:

<!-- b000093 | prose | pages [4] -->
 the bottom region is flat or arched,  the two side arches of the half-pipe are circular or other arches. Considering the possible differences mentioned above, we mainly divide the following three kinds of half-pipes: (1) The bottom region and its two sides are respectively flat and circular. This kind of

<!-- b000094 | prose | pages [4] -->
half-pipe is used in Winter Olympics. (2) The bottom region and its two sides are respectively arched and circular. This

<!-- b000095 | prose | pages [4] -->
kind of half-pipe is used in previous games. (3) The bottom region and its two sides are respectively flat and elliptical. This kind

<!-- b000096 | prose | pages [4] -->
of half-pipe is used in some local games.

<!-- b000097 | prose | pages [4] -->
For a skilled snowboarder, it’s obvious that the shape of a half-pipe will affect his achievement. In the following discussions, we shall develop a mathematical model and focus on analyzing the first kind of half-pipe. In addition, a few designs of some other kinds of half-pipes are also discussed and compared with respect to the influences on the athlete’s performances in games.

<!-- b000098 | furniture | pages [5] -->
Team # 9665

<!-- b000099 | furniture | pages [5] -->
Page 4 of 30

<!-- b000100 | heading | pages [5] -->
3.2 The Description of Half-Pipe We Focused

<!-- b000101 | prose | pages [5] -->
The Halfpipe Schematic drawn in Figure 1:

<!-- b000102 | caption | pages [5] -->
Figure 1. Snowboarding Half-pipe Schematic (Half-pipe snowboarding)

<!-- b000103 | prose | pages [5] -->
Sources: http://www.abc-of-snowboarding.com/snowboardinghalfpipe.asp To illustrate the half-pipe more specific, we throw light upon its main elements.

<!-- b000104 | prose | pages [5] -->
Flat

<!-- b000105 | prose | pages [5] -->
Is the center flat floor of the Half-pipe

<!-- b000106 | prose | pages [5] -->
Transitions

<!-- b000107 | prose | pages [5] -->
The curved transition between the horizontal flat and the vertical walls

<!-- b000108 | prose | pages [5] -->
Verticals

<!-- b000109 | prose | pages [5] -->
The vertical parts of the walls between the Lip and the Transitions

<!-- b000110 | prose | pages [5] -->
Platform/Deck

<!-- b000111 | prose | pages [5] -->
The horizontal flat platform on top of the wall

<!-- b000112 | prose | pages [5] -->
Entry Ramp

<!-- b000113 | prose | pages [5] -->
The beginning of the half-pipe where athlete start their run

<!-- b000114 | heading | pages [5] -->
3.3 Basic Model

<!-- b000115 | prose | pages [5] -->
In this section, a basic model is developed in order to model the design of a half-pipe and analyze its influence on the performance of an athlete.

<!-- b000116 | furniture | pages [6] -->
Team # 9665

<!-- b000117 | furniture | pages [6] -->
Page 5 of 30

<!-- b000118 | heading | pages [6] -->
3.3.1 Assumptions and Notations

<!-- b000119 | prose | pages [6] -->
For the sake of convenience of the following discussions, we firstly assume that: (1) The “ vertical air “ for an specific athlete is a constant. (2) The snowboard and snowboarder are an entity and the internal action of them can

<!-- b000120 | prose | pages [6] -->
be ignored. (3) The air resistance is ignored. (4) The coefficient of sliding friction of the half pipe surface is fixed.

<!-- b000121 | prose | pages [6] -->
Now, we are to introduce some notations which will be used in the subsequent Sections.

<!-- b000122 | prose | pages [6] -->
xh : denotes the height of platform;

<!-- b000123 | prose | pages [6] -->
xr : denotes the radius of transitions;

<!-- b000124 | prose | pages [6] -->
: denotes the arc angle of transitions;

<!-- b000125 | prose | pages [6] -->
w : denotes the width of the flat; x

<!-- b000126 | prose | pages [6] -->
xt : denotes the thickness of flat;

<!-- b000127 | prose | pages [6] -->
xa : denotes the length of U-shape bowl;

<!-- b000128 | prose | pages [6] -->
xb : denotes the width of the U-shape bowl.

<!-- b000129 | prose | pages [6] -->
In particular, a scheme of a half-pipe with the notions introduced above is drawn and presented in Figure 2.

<!-- b000130 | caption | pages [6] -->
Figure 2. A scheme of a half-pipe with notations.

<!-- b000131 | furniture | pages [7] -->
Team # 9665

<!-- b000132 | prose | pages [7] -->
Based on the discussions above, we have

<!-- b000133 | prose | pages [7] -->
 

<!-- b000134 | prose | pages [7] -->
h

<!-- b000135 | prose | pages [7] -->
(

<!-- b000136 | prose | pages [7] -->
r

<!-- b000137 | prose | pages [7] -->
x x

<!-- b000138 | prose | pages [7] -->
 

<!-- b000139 | prose | pages [7] -->
b w

<!-- b000140 | prose | pages [7] -->
x x

<!-- b000141 | furniture | pages [7] -->
Page 6 of 30

<!-- b000142 | prose | pages [7] -->


<!-- b000143 | prose | pages [7] -->


<!-- b000144 | prose | pages [7] -->


<!-- b000145 | prose | pages [7] -->
r r

<!-- b000146 | prose | pages [7] -->
cos )

<!-- b000147 | prose | pages [7] -->
t

<!-- b000148 | prose | pages [7] -->
,

<!-- b000149 | prose | pages [7] -->
x x x

<!-- b000150 | prose | pages [7] -->


<!-- b000151 | prose | pages [7] -->


<!-- b000152 | prose | pages [7] -->


<!-- b000153 | prose | pages [7] -->
2 2

<!-- b000154 | prose | pages [7] -->
r r

<!-- b000155 | prose | pages [7] -->
sin 2 .

<!-- b000156 | prose | pages [7] -->
t

<!-- b000157 | prose | pages [7] -->
x x

<!-- b000158 | prose | pages [7] -->
Obviously, in order to complete the design of a half-pipe, we should find the numerical solutions of each variable defined in Figure 2.

<!-- b000159 | heading | pages [7] -->
3.3.2 The Analysis of Snowboarder’s Movement

<!-- b000160 | prose | pages [7] -->
As shown in Figure 2, when an athlete starts from point O to a random extreme A , there only exists the gravity and friction which are in work in the whole point process.

<!-- b000161 | prose | pages [7] -->
According to the law of conservation of energy, we can get

<!-- b000162 | prose | pages [7] -->
 

<!-- b000163 | prose | pages [7] -->
W W

<!-- b000164 | prose | pages [7] -->
p

<!-- b000165 | prose | pages [7] -->
h

<!-- b000166 | prose | pages [7] -->
  

<!-- b000167 | prose | pages [7] -->
mg h

<!-- b000168 | prose | pages [7] -->
,

<!-- b000169 | prose | pages [7] -->
f f

<!-- b000170 | prose | pages [7] -->
 

<!-- b000171 | prose | pages [7] -->
h h h

<!-- b000172 | prose | pages [7] -->
,

<!-- b000173 | prose | pages [7] -->
x

<!-- b000174 | prose | pages [7] -->
denotes the work done by the snowboarder on the flat and it is used for where

<!-- b000175 | prose | pages [7] -->
W p

<!-- b000176 | prose | pages [7] -->
denotes the work done by friction. acceleration, W f

<!-- b000177 | prose | pages [7] -->
Obviously, in order to maximize the “vertical air”, we should maximize and W p

<!-- b000178 | prose | pages [7] -->
, respectively. Note that the resistant function of friction for the minimize W f

<!-- b000179 | prose | pages [7] -->
snowboard is much smaller than the work done by the snowboarder, the achievement

<!-- b000180 | prose | pages [7] -->
of maximizing the “vertical air” can approximately be obtained only by maximizing

<!-- b000181 | prose | pages [7] -->
W . p

<!-- b000182 | heading | pages [7] -->
3.3.3 The Calculation of

<!-- b000183 | prose | pages [7] -->
W f

<!-- b000184 | prose | pages [7] -->
    . Firstly, it’s known that the work done by friction is given by W f l F l f N F , we consider the following two different situations: In order to compute the force N  F mg , where m When the snowboarder is on the flat, then we have is N the total weight including both the snowboard and the athlete. When the snowboarder is on the transition, then the centripetal force is

<!-- b000185 | prose | pages [7] -->
provided by the support force of arch and the gravity. Thus, we have

<!-- b000186 | prose | pages [7] -->
 F mg

<!-- b000187 | prose | pages [7] -->
N

<!-- b000188 | prose | pages [7] -->
where v is the velocity, ( 0   

<!-- b000189 | prose | pages [7] -->
2

<!-- b000190 | prose | pages [7] -->
mv     ,

<!-- b000191 | prose | pages [7] -->
cos 2

<!-- b000192 | prose | pages [7] -->
 ) is the angle between the gravity and the   d dl r vertical direction of arch. We can also get that the snowboarder is presented in Figure 3.

<!-- b000193 | prose | pages [7] -->
and the force analysis of x

<!-- b000194 | furniture | pages [8] -->
Team # 9665

<!-- b000195 | prose | pages [8] -->


<!-- b000196 | furniture | pages [8] -->
Page 7 of 30

<!-- b000197 | caption | pages [8] -->
Figure 3. Force analysis of the snowboarder.

<!-- b000198 | prose | pages [8] -->
n Assume that the snowboarder has completed times flight actions, we can approximately calculate the distance l by the following equation:

<!-- b000199 | prose | pages [8] -->
  l n ( w x

<!-- b000200 | prose | pages [8] -->
Thus, we can get

<!-- b000201 | prose | pages [8] -->
  

<!-- b000202 | prose | pages [8] -->
nmg w

<!-- b000203 | prose | pages [8] -->
   

<!-- b000204 | prose | pages [8] -->
x

<!-- b000205 | prose | pages [8] -->
W

<!-- b000206 | prose | pages [8] -->
f

<!-- b000207 | prose | pages [8] -->


<!-- b000208 | prose | pages [8] -->
cos

<!-- b000209 | prose | pages [8] -->
  r    2 )/cos .

<!-- b000210 | prose | pages [8] -->
2

<!-- b000211 | prose | pages [8] -->
mv

<!-- b000212 | prose | pages [8] -->
      

<!-- b000213 | prose | pages [8] -->
n mg

<!-- b000214 | prose | pages [8] -->
( cos ) 2

<!-- b000215 | prose | pages [8] -->
r d

<!-- b000216 | prose | pages [8] -->
.

<!-- b000217 | prose | pages [8] -->
x

<!-- b000218 | prose | pages [8] -->
r

<!-- b000219 | prose | pages [8] -->
0 0

<!-- b000220 | prose | pages [8] -->
x

<!-- b000221 | prose | pages [8] -->
Note that it is difficult to deal with the friction changes of the transitions and the work done by the friction is much less than that done by the athlete used for  acceleration, we approximate the value of the friction of the transitions as and mg it will not induce a big difference. So, we have

<!-- b000222 | prose | pages [8] -->
    W nmg f

<!-- b000223 | heading | pages [8] -->
3.3.4 The Discussion of

<!-- b000224 | prose | pages [8] -->
W p

<!-- b000225 | prose | pages [8] -->
    . ( ( w 2 r ) / cos x

<!-- b000226 | prose | pages [8] -->
Snowboarders get higher velocity by stomping or rising leg on the flat. However,

<!-- b000227 | prose | pages [8] -->
v as to friction of half-pipe, the velocity has a maximum value

<!-- b000228 | prose | pages [8] -->
v

<!-- b000229 | prose | pages [8] -->
. When the velocity max

<!-- b000230 | prose | pages [8] -->
, snowboarder can’t improve it by snowboarding skills. We assume the achieves max

<!-- b000231 | prose | pages [8] -->
work done by snowboarder when he accelerate for i th on the flat as W . However, pi

<!-- b000232 | prose | pages [8] -->
in the process of design the half-pipe, we don’t care about the numerical solution of

<!-- b000233 | prose | pages [8] -->
W . The reason of discussing it is to ensure the integrity and accuracy of our model. pi

<!-- b000234 | prose | pages [8] -->
Combing with the equations derived above, we obtain

<!-- b000235 | furniture | pages [9] -->
Team # 9665

<!-- b000236 | prose | pages [9] -->
n

<!-- b000237 | prose | pages [9] -->
 

<!-- b000238 | prose | pages [9] -->


<!-- b000239 | prose | pages [9] -->
W

<!-- b000240 | prose | pages [9] -->
pi

<!-- b000241 | prose | pages [9] -->


<!-- b000242 | prose | pages [9] -->
i

<!-- b000243 | prose | pages [9] -->
1

<!-- b000244 | prose | pages [9] -->
h

<!-- b000245 | prose | pages [9] -->
 h

<!-- b000246 | furniture | pages [9] -->
Page 8 of 30

<!-- b000247 | prose | pages [9] -->


<!-- b000248 | prose | pages [9] -->
 

<!-- b000249 | prose | pages [9] -->
nmg w

<!-- b000250 | prose | pages [9] -->
( 2

<!-- b000251 | prose | pages [9] -->
r

<!-- b000252 | prose | pages [9] -->
) / cos

<!-- b000253 | prose | pages [9] -->
x

<!-- b000254 | prose | pages [9] -->
mg

<!-- b000255 | prose | pages [9] -->
.

<!-- b000256 | prose | pages [9] -->
is decided by Obviously, the value of directly. For the process of every W p

<!-- b000257 | prose | pages [9] -->
slid motion done by athlete is same basically, we can calculate

<!-- b000258 | prose | pages [9] -->
 W p

<!-- b000259 | prose | pages [9] -->
by W p

<!-- b000260 | prose | pages [9] -->
n 1 1

<!-- b000261 | prose | pages [9] -->
 W pi n n  i

<!-- b000262 | prose | pages [9] -->
1

<!-- b000263 | prose | pages [9] -->
By analyzing the above equations, we can get that the “vertical air” is maximum if

<!-- b000264 | prose | pages [9] -->
the velocity when athlete make flight action is limit value.

<!-- b000265 | heading | pages [9] -->
3.3.5 The Function of

<!-- b000266 | prose | pages [9] -->
W p

<!-- b000267 | prose | pages [9] -->
is the work done by athlete used for accelerating and it is used to compensate W p

<!-- b000268 | prose | pages [9] -->
the lose caused by the work done by friction.

<!-- b000269 | caption | pages [9] -->
Figure 4 shows the specific situation we investigate.

<!-- b000270 | caption | pages [9] -->
Figure 4. The scheme of slid motion done by athlete

<!-- b000271 | prose | pages [9] -->
As is shown in Figure 4, from point A to B, the velocity of athlete decreases because of the friction. In this process, the following equations are obeyed.

<!-- b000272 | prose | pages [9] -->


<!-- b000273 | prose | pages [9] -->
1

<!-- b000274 | prose | pages [9] -->
2

<!-- b000275 | prose | pages [9] -->
mv

<!-- b000276 | prose | pages [9] -->


<!-- b000277 | prose | pages [9] -->
max

<!-- b000278 | prose | pages [9] -->
2

<!-- b000279 | prose | pages [9] -->
 

<!-- b000280 | prose | pages [9] -->
W f

<!-- b000281 | prose | pages [9] -->


<!-- b000282 | prose | pages [9] -->
f

<!-- b000283 | prose | pages [9] -->
1

<!-- b000284 | prose | pages [9] -->
1

<!-- b000285 | prose | pages [9] -->
1

<!-- b000286 | prose | pages [9] -->
  

<!-- b000287 | prose | pages [9] -->
2

<!-- b000288 | prose | pages [9] -->
mv W

<!-- b000289 | prose | pages [9] -->
B f

<!-- b000290 | prose | pages [9] -->
2

<!-- b000291 | prose | pages [9] -->
.

<!-- b000292 | prose | pages [9] -->
1

<!-- b000293 | prose | pages [9] -->
  

<!-- b000294 | prose | pages [9] -->
( (

<!-- b000295 | prose | pages [9] -->
AA

<!-- b000296 | prose | pages [9] -->
'

<!-- b000297 | prose | pages [9] -->
BB

<!-- b000298 | prose | pages [9] -->
')

<!-- b000299 | prose | pages [9] -->
From point B to C, the velocity recoveries to the maximum value with the help of

<!-- b000300 | furniture | pages [10] -->
Team # 9665

<!-- b000301 | prose | pages [10] -->
W . So we have, p

<!-- b000302 | prose | pages [10] -->


<!-- b000303 | prose | pages [10] -->
1

<!-- b000304 | prose | pages [10] -->


<!-- b000305 | prose | pages [10] -->
2

<!-- b000306 | prose | pages [10] -->
mv

<!-- b000307 | prose | pages [10] -->


<!-- b000308 | prose | pages [10] -->
max

<!-- b000309 | prose | pages [10] -->
2

<!-- b000310 | prose | pages [10] -->
  

<!-- b000311 | prose | pages [10] -->
W f BC

<!-- b000312 | prose | pages [10] -->


<!-- b000313 | prose | pages [10] -->
f

<!-- b000314 | prose | pages [10] -->
2

<!-- b000315 | prose | pages [10] -->
2

<!-- b000316 | prose | pages [10] -->
1f

<!-- b000317 | furniture | pages [10] -->
Page 9 of 30

<!-- b000318 | prose | pages [10] -->
1 1

<!-- b000319 | prose | pages [10] -->
 

<!-- b000320 | prose | pages [10] -->
2

<!-- b000321 | prose | pages [10] -->
mv W W

<!-- b000322 | prose | pages [10] -->
B f p 2 2

<!-- b000323 | prose | pages [10] -->
,

<!-- b000324 | prose | pages [10] -->
2

<!-- b000325 | prose | pages [10] -->
2f is the friction applied to snowboard of where,

<!-- b000326 | prose | pages [10] -->
BC and

<!-- b000327 | prose | pages [10] -->
and BB , is that of AA ' '

<!-- b000328 | prose | pages [10] -->
1f 2f . Thus, we have are the corresponding work done by

<!-- b000329 | prose | pages [10] -->
W ,

<!-- b000330 | prose | pages [10] -->
W

<!-- b000331 | prose | pages [10] -->
1f

<!-- b000332 | prose | pages [10] -->
2f

<!-- b000333 | prose | pages [10] -->
 W p

<!-- b000334 | heading | pages [10] -->
3.3.6 Approach Parameters of Half-Pipe

<!-- b000335 | prose | pages [10] -->
and

<!-- b000336 | prose | pages [10] -->
 W W f f 1 2

<!-- b000337 | prose | pages [10] -->
The height of the platform and the radius of transition

<!-- b000338 | prose | pages [10] -->
The height of platform is related to the original velocity of athletes. In the process of sliding down from the entrance, there is almost no loss of energy, namely, the gravitational potential energy translates into kinetic energy totally. So we have

<!-- b000339 | prose | pages [10] -->
 mg h 1  2 mv x x 0 2

<!-- b000340 | prose | pages [10] -->
The original velocity decides the achievement of athletes in competition and is related to the “vertical air”. Thus , it is very important to consider it in the design of the height of platform.

<!-- b000341 | prose | pages [10] -->
According the study by Huang and his team, in order to get a relative good score, athlete should ensure the original velocity when he or she enters the half-pipe to be 11.06 m s at least. / Since the abusive high of platform will result in the big loss of velocity before the flight part made, the relative suitable original velocity for design platform is the least one. Thus,

<!-- b000342 | prose | pages [10] -->
v  h

<!-- b000343 | prose | pages [10] -->
x 2

<!-- b000344 | prose | pages [10] -->
The arc angle of transitions

<!-- b000345 | prose | pages [10] -->
2 2

<!-- b000346 | prose | pages [10] -->


<!-- b000347 | prose | pages [10] -->
0 0 6.241 m

<!-- b000348 | prose | pages [10] -->
. g g

<!-- b000349 | prose | pages [10] -->
Athletes make flight part on the top of transitions and his velocity of flight can be resolute in the three directions-x, y and z. Namely,

<!-- b000350 | prose | pages [10] -->
    v v cos , v v x s x y s

<!-- b000351 | prose | pages [10] -->
xv , zv

<!-- b000352 | prose | pages [10] -->
      v v cos and , cos z s z y

<!-- b000353 | prose | pages [10] -->
sv are the component velocities of where, and yv in the directions of x,

<!-- b000354 | furniture | pages [11] -->
Team # 9665

<!-- b000355 | prose | pages [11] -->
,   y and z respectively and and x z y

<!-- b000356 | prose | pages [11] -->
shows the specific situation.

<!-- b000357 | furniture | pages [11] -->
Page 10 of 30

<!-- b000358 | prose | pages [11] -->
xv , zv . Figure 5 are the angle of and yv

<!-- b000359 | prose | pages [11] -->
sv

<!-- b000360 | caption | pages [11] -->
Figure 5. The scheme of resolution of

<!-- b000361 | prose | pages [11] -->
What is more, in vertical plane, just like what is shown in Figure 6 , the

<!-- b000362 | prose | pages [11] -->
 relationship of ,  obeys the following equations approximately. and x y

<!-- b000363 | prose | pages [11] -->
  

<!-- b000364 | furniture | pages [11] -->


<!-- b000365 | prose | pages [11] -->
and x

<!-- b000366 | prose | pages [11] -->
Thus,

<!-- b000367 | prose | pages [11] -->
   v v cos x s

<!-- b000368 | prose | pages [11] -->
     90

<!-- b000369 | furniture | pages [11] -->


<!-- b000370 | prose | pages [11] -->
.

<!-- b000371 | prose | pages [11] -->
y

<!-- b000372 | prose | pages [11] -->
   and . v v sin y s

<!-- b000373 | caption | pages [11] -->
Figure 6. The scheme of component velocities in vertical plane.

<!-- b000374 | prose | pages [11] -->
 h increase with the vertical component velocity The height of flight yv . As is

<!-- b000375 | prose | pages [11] -->
A , the relationship of energy obeys shown in Figure 4, from point A to '

<!-- b000376 | prose | pages [11] -->


<!-- b000377 | prose | pages [11] -->
2

<!-- b000378 | prose | pages [11] -->
m v

<!-- b000379 | prose | pages [11] -->
1

<!-- b000380 | prose | pages [11] -->
  

<!-- b000381 | prose | pages [11] -->
s

<!-- b000382 | prose | pages [11] -->
m v

<!-- b000383 | prose | pages [11] -->
2 2

<!-- b000384 | prose | pages [11] -->
Namely,

<!-- b000385 | prose | pages [11] -->
    

<!-- b000386 | prose | pages [11] -->
2 2

<!-- b000387 | prose | pages [11] -->
. f AA mg h

<!-- b000388 | prose | pages [11] -->
max max 1

<!-- b000389 | prose | pages [11] -->
x

<!-- b000390 | furniture | pages [12] -->
Team # 9665

<!-- b000391 | prose | pages [12] -->
2 1

<!-- b000392 | prose | pages [12] -->
 

<!-- b000393 | prose | pages [12] -->
2

<!-- b000394 | prose | pages [12] -->
v

<!-- b000395 | prose | pages [12] -->
(

<!-- b000396 | prose | pages [12] -->
mv f

<!-- b000397 | prose | pages [12] -->
(

<!-- b000398 | prose | pages [12] -->
s

<!-- b000399 | prose | pages [12] -->
max 1

<!-- b000400 | prose | pages [12] -->
m

<!-- b000401 | prose | pages [12] -->
2

<!-- b000402 | prose | pages [12] -->
Then, we can get

<!-- b000403 | prose | pages [12] -->
w

<!-- b000404 | prose | pages [12] -->
2 1

<!-- b000405 | prose | pages [12] -->
 

<!-- b000406 | prose | pages [12] -->
2

<!-- b000407 | prose | pages [12] -->
v

<!-- b000408 | prose | pages [12] -->
(

<!-- b000409 | prose | pages [12] -->
mv f

<!-- b000410 | prose | pages [12] -->
(

<!-- b000411 | prose | pages [12] -->
y

<!-- b000412 | prose | pages [12] -->
max 1

<!-- b000413 | prose | pages [12] -->
m

<!-- b000414 | prose | pages [12] -->
2 cos

<!-- b000415 | furniture | pages [12] -->
Page 11 of 30

<!-- b000416 | prose | pages [12] -->
 

<!-- b000417 | prose | pages [12] -->
w w r

<!-- b000418 | prose | pages [12] -->
  

<!-- b000419 | prose | pages [12] -->
x x x

<!-- b000420 | prose | pages [12] -->
)

<!-- b000421 | prose | pages [12] -->
mgr

<!-- b000422 | prose | pages [12] -->
(1 cos ))

<!-- b000423 | prose | pages [12] -->
x

<!-- b000424 | prose | pages [12] -->


<!-- b000425 | prose | pages [12] -->
cos

<!-- b000426 | prose | pages [12] -->
.

<!-- b000427 | prose | pages [12] -->
  

<!-- b000428 | prose | pages [12] -->
r

<!-- b000429 | prose | pages [12] -->
    

<!-- b000430 | prose | pages [12] -->
x x x

<!-- b000431 | prose | pages [12] -->
)

<!-- b000432 | prose | pages [12] -->
mgr

<!-- b000433 | prose | pages [12] -->
(1 cos )) sin

<!-- b000434 | prose | pages [12] -->
x

<!-- b000435 | prose | pages [12] -->


<!-- b000436 | prose | pages [12] -->
is the friction force in the inclined plane, which decrease with . For 1f Where

<!-- b000437 | prose | pages [12] -->
the variation of it is not significant, we regard it as a constant.

<!-- b000438 | prose | pages [12] -->
  0.1 We assume that , m 75 kg , then the solution of   and is 5

<!-- b000439 | prose | pages [12] -->
transformed as a question which calculating the maximum of function of one variable.

<!-- b000440 | prose | pages [12] -->
Utilizing the MATLAB software, we can get the value of  corresponding to the

<!-- b000441 | prose | pages [12] -->
max component velocity in vertical direction is 51.66°.

<!-- b000442 | prose | pages [12] -->
The relationship of  is shown in Figure 7 and yv

<!-- b000443 | prose | pages [12] -->
14

<!-- b000444 | prose | pages [12] -->
co m p o n en t sp eed in th e v ertical d irectio n

<!-- b000445 | prose | pages [12] -->
12

<!-- b000446 | prose | pages [12] -->
10

<!-- b000447 | prose | pages [12] -->
8

<!-- b000448 | prose | pages [12] -->
6

<!-- b000449 | prose | pages [12] -->
4

<!-- b000450 | prose | pages [12] -->
2

<!-- b000451 | prose | pages [12] -->
0 0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6

<!-- b000452 | prose | pages [12] -->
the arc angle o f transitio ns

<!-- b000453 | caption | pages [12] -->
Figure 7 .The relationship of 

<!-- b000454 | prose | pages [12] -->
and yv

<!-- b000455 | prose | pages [12] -->
Just as shown in Figure7, the relationship of two variables obeys parabola

<!-- b000456 | prose | pages [12] -->
 , the approximately. When yv 51.66

<!-- b000457 | prose | pages [12] -->
According the equation

<!-- b000458 | prose | pages [12] -->
2 yv

<!-- b000459 | prose | pages [12] -->
reaches the maximum value.

<!-- b000460 | prose | pages [12] -->
  , 2 g h

<!-- b000461 | prose | pages [12] -->
 . So, the radius of we can derive the “vertical air” is maximal when transitions can be calculated as

<!-- b000462 | prose | pages [12] -->
h  r

<!-- b000463 | prose | pages [12] -->
x

<!-- b000464 | prose | pages [12] -->


<!-- b000465 | prose | pages [12] -->
1 cos

<!-- b000466 | prose | pages [12] -->
51.66

<!-- b000467 | prose | pages [12] -->
 .

<!-- b000468 | prose | pages [12] -->
x x

<!-- b000469 | prose | pages [12] -->
16.44

<!-- b000470 | prose | pages [12] -->
m 

<!-- b000471 | furniture | pages [13] -->
Team # 9665

<!-- b000472 | prose | pages [13] -->
The width of flat

<!-- b000473 | furniture | pages [13] -->
Page 12 of 30

<!-- b000474 | prose | pages [13] -->
The process of athlete doing work for acceleration can’t be completed in a very

<!-- b000475 | prose | pages [13] -->
S short distance. It must reach the minimum distance

<!-- b000476 | prose | pages [13] -->
v

<!-- b000477 | prose | pages [13] -->
for accelerating velocity to max

<!-- b000478 | prose | pages [13] -->
. Base on this, we promote the curve of velocity recovery. max

<!-- b000479 | prose | pages [13] -->
Just as shown in Figure 8, the curve has following characteristics:

<!-- b000480 | prose | pages [13] -->
(1) Horizontal axis presents the slid distance to the start point, and vertical axis

<!-- b000481 | prose | pages [13] -->
presents the maximum velocity can be achieved corresponding to a fixed slid

<!-- b000482 | prose | pages [13] -->
distance.

<!-- b000483 | prose | pages [13] -->
(2) The recovery function to velocity decreases with the increment of slid

<!-- b000484 | prose | pages [13] -->
distance S , namely the slope in figure decreases with S .

<!-- b000485 | prose | pages [13] -->
v S should be slid at least. (3) In order to obtain , max max

<!-- b000486 | prose | pages [13] -->
(4) If the slid distance is longer than S , the achieved velocity at last can be max

<!-- b000487 | prose | pages [13] -->
regarded as a constant approximately.

<!-- b000488 | caption | pages [13] -->
Figure 8. The curve of velocity recovery

<!-- b000489 | prose | pages [13] -->
Fortunately, Harding, et al. (2007) investigate the relationship between the

<!-- b000490 | prose | pages [13] -->
acceleration and the time used for sliding by utilizing a sliding Fast Fourier Transform

<!-- b000491 | prose | pages [13] -->
(FFT) window and subsequent power analysis and characterize it in Figure 9 .

<!-- b000492 | furniture | pages [14] -->
Team # 9665

<!-- b000493 | furniture | pages [14] -->
Page 13 of 30

<!-- b000494 | caption | pages [14] -->
Figure 9. A unfiltered accelerometer trance associated with a snowboarding run

<!-- b000495 | prose | pages [14] -->
M characterizes the time when athlete attach flat after In Figure 9, the point leaving transitions. The acceleration is very big at the moment of M . The point N

<!-- b000496 | prose | pages [14] -->
presents the slid distance of an athlete reaches and the velocity is max. The S max P characterizes the time when athlete attach the other transition after point completing the slide on flat.

<!-- b000497 | prose | pages [14] -->
We can get, by analyzing, the conclusion that the velocity of athlete will not change after acceleration for some time in the condition of the length of flat is long enough. To investigate it more deeply, we distill the relationship in the figure into a approximate broken line which shown in Figure 10.

<!-- b000498 | caption | pages [14] -->
Figure 10 .The distilled relationship between acceleration and time

<!-- b000499 | prose | pages [14] -->
Combing the data shown in Figure 9, The relationship between the acceleration and time when athlete accelerate in flat can be characterized by the following equation.

<!-- b000500 | prose | pages [14] -->


<!-- b000501 | prose | pages [14] -->
2.5

<!-- b000502 | prose | pages [14] -->
g  a

<!-- b000503 | prose | pages [14] -->
c

<!-- b000504 | prose | pages [14] -->
  

<!-- b000505 | prose | pages [14] -->
2.5

<!-- b000506 | prose | pages [14] -->
gt

<!-- b000507 | prose | pages [14] -->
,      t 1s

<!-- b000508 | prose | pages [14] -->
.

<!-- b000509 | prose | pages [14] -->
0                          t>1s

<!-- b000510 | prose | pages [14] -->


<!-- b000511 | furniture | pages [15] -->
Team # 9665

<!-- b000512 | furniture | pages [15] -->
Page 14 of 30

<!-- b000513 | prose | pages [15] -->
Thus, the velocity of athlete at random can be calculated by

<!-- b000514 | prose | pages [15] -->
1     v v 0 (2.5 g 2.5 1    2 gt dt ) v 2.5 gt 1.25 gt . 1

<!-- b000515 | prose | pages [15] -->
 t 1 s The slid distance when the acceleration decreased to 0 at the time of

<!-- b000516 | prose | pages [15] -->
S , which can be calculated by max

<!-- b000517 | prose | pages [15] -->
1    S 0 ( v max 1

<!-- b000518 | prose | pages [15] -->
  v 11.06 m s / S Note that , we get 1 max

<!-- b000519 | prose | pages [15] -->
is

<!-- b000520 | prose | pages [15] -->
 2 2.5 gt 1.25 gt ) dt .

<!-- b000521 | prose | pages [15] -->
19.27 m .

<!-- b000522 | prose | pages [15] -->
 , we get In addition, combing the discussion above and the assumption that

<!-- b000523 | prose | pages [15] -->


<!-- b000524 | prose | pages [15] -->
5

<!-- b000525 | prose | pages [15] -->
    max cos w S x 19.18 m

<!-- b000526 | heading | pages [15] -->
The solution of the length of a half-pipe

<!-- b000527 | prose | pages [15] -->
The length of a half-pipe is decided by the slid distance between two continuous

<!-- b000528 | prose | pages [15] -->
fight part and the times of flight parts made by athlete simultaneously. Thus,

<!-- b000529 | prose | pages [15] -->
.

<!-- b000530 | caption | pages [15] -->
Figure 11. The scheme of process of sliding

<!-- b000531 | prose | pages [15] -->
From Figure 11, we can get that

<!-- b000532 | prose | pages [15] -->
    a DD sin 0

<!-- b000533 | prose | pages [15] -->
In order to get the numerical solution of

<!-- b000534 | prose | pages [15] -->
applied.

<!-- b000535 | prose | pages [15] -->
Step1: Calculating sv

<!-- b000536 | prose | pages [15] -->
From Figure 4, we have

<!-- b000537 | prose | pages [15] -->
       . 2 r sin v t x x t

<!-- b000538 | prose | pages [15] -->
xa , the following 4 steps should be

<!-- b000539 | furniture | pages [16] -->
Team # 9665

<!-- b000540 | prose | pages [16] -->
1 1  2 mv mv s 2 2

<!-- b000541 | prose | pages [16] -->
Thus,

<!-- b000542 | prose | pages [16] -->
2 1  2 v ( mv s max m 2

<!-- b000543 | furniture | pages [16] -->
Page 15 of 30

<!-- b000544 | prose | pages [16] -->
   2 2 ’ . f AA mgh max max 1 x

<!-- b000545 | prose | pages [16] -->
      mg AA mgh ) . x

<!-- b000546 | prose | pages [16] -->
sv , the parameters m , In order to calculate known.

<!-- b000547 | prose | pages [16] -->
, and should be v sv AA ' max

<!-- b000548 | prose | pages [16] -->
We assume that m is 75kg which is the average weight of a snowboarder.

<!-- b000549 | prose | pages [16] -->
Then,

<!-- b000550 | prose | pages [16] -->
   v ( v 2.5 gt max 1  2 . 1.25 gt )| 23.31 m s /  t 1

<!-- b000551 | prose | pages [16] -->
Note that the range of coefficient of sliding friction is from 0.03 to 0.2, we assume

<!-- b000552 | prose | pages [16] -->
that it is 0.1. From Figure 4, we can also get that

<!-- b000553 | prose | pages [16] -->
AA

<!-- b000554 | prose | pages [16] -->
Thus, can be calculated. sv

<!-- b000555 | prose | pages [16] -->
  xr   . 

<!-- b000556 | prose | pages [16] -->
cos

<!-- b000557 | prose | pages [16] -->
by utilizing

<!-- b000558 | heading | pages [16] -->
Step2: The solution of

<!-- b000559 | prose | pages [16] -->
and xv tt

<!-- b000560 | prose | pages [16] -->
      v v cos v cos x s x s

<!-- b000561 | heading | pages [16] -->
Step3: The solution of DD

<!-- b000562 | prose | pages [16] -->
Step4: Getting by calculation of xa

<!-- b000563 | prose | pages [16] -->
sv

<!-- b000564 | prose | pages [16] -->
v

<!-- b000565 | prose | pages [16] -->
y

<!-- b000566 | prose | pages [16] -->


<!-- b000567 | prose | pages [16] -->
  

<!-- b000568 | prose | pages [16] -->
t

<!-- b000569 | prose | pages [16] -->
2 , , and v v sin t y s

<!-- b000570 | prose | pages [16] -->
g

<!-- b000571 | prose | pages [16] -->
w  x DD 

<!-- b000572 | prose | pages [16] -->
cos

<!-- b000573 | prose | pages [16] -->
0a 0a

<!-- b000574 | prose | pages [16] -->
Combing the above derivation, we can get that

<!-- b000575 | prose | pages [16] -->
a  0

<!-- b000576 | heading | pages [16] -->
22.85 m

<!-- b000577 | prose | pages [16] -->
According the current investigations, the times of flight part for a athlete is about

<!-- b000578 | prose | pages [16] -->
7. Therefore, we have

<!-- b000579 | prose | pages [16] -->
 xa 159.95 m

<!-- b000580 | furniture | pages [17] -->
Team # 9665

<!-- b000581 | furniture | pages [17] -->
Page 16 of 30

<!-- b000582 | heading | pages [17] -->
IVMechanical Characteristics Model of Question Two

<!-- b000583 | heading | pages [17] -->
4.1 Assumptions

<!-- b000584 | prose | pages [17] -->
 Athlete can transform the horizontal velocity to the one twist with the central

<!-- b000585 | prose | pages [17] -->
axis of snowboarder.

<!-- b000586 | prose | pages [17] -->
 The path of sliding and the “ vertical air” are unchangeable

<!-- b000587 | prose | pages [17] -->
 The velocity of athlete can reach

<!-- b000588 | heading | pages [17] -->
4.2 Torque

<!-- b000589 | prose | pages [17] -->
v v max

<!-- b000590 | prose | pages [17] -->
In order to maxim twist in the air, athlete must bend his body. A torque, which is perpendicular to snowboard’s axis of rotation, is generated simultaneously when snowboarder bending his body. Figure 12 describe the specific situation.

<!-- b000591 | caption | pages [17] -->
Figure 12. Torque applied to the snowboard and the angle of twist

<!-- b000592 | prose | pages [17] -->
Source: Brennan, et al. Modelling the mechanical characteristics and on-snow performance of snow boards.

<!-- b000593 | prose | pages [17] -->
4.3Mechanical characteristics

<!-- b000594 | prose | pages [17] -->
We treat the snowboard as a thin beam and relate the applied moment and applied torque to the radius of curvature and the rate of twist by the relationship (Kollár & Springer 2003):

<!-- b000595 | prose | pages [17] -->
 

<!-- b000596 | prose | pages [17] -->
1

<!-- b000597 | prose | pages [17] -->


<!-- b000598 | prose | pages [17] -->
W

<!-- b000599 | prose | pages [17] -->
 

<!-- b000600 | prose | pages [17] -->


<!-- b000601 | prose | pages [17] -->
   

<!-- b000602 | prose | pages [17] -->
x

<!-- b000603 | prose | pages [17] -->
W

<!-- b000604 | prose | pages [17] -->
  

<!-- b000605 | prose | pages [17] -->


<!-- b000606 | furniture | pages [17] -->


<!-- b000607 | prose | pages [17] -->
 

<!-- b000608 | prose | pages [17] -->
ˆ

<!-- b000609 | prose | pages [17] -->
  

<!-- b000610 | furniture | pages [17] -->


<!-- b000611 | prose | pages [17] -->
W M

<!-- b000612 | prose | pages [17] -->
 

<!-- b000613 | prose | pages [17] -->
22 22 24

<!-- b000614 | prose | pages [17] -->
x

<!-- b000615 | prose | pages [17] -->
,

<!-- b000616 | prose | pages [17] -->
  

<!-- b000617 | prose | pages [17] -->
ˆ

<!-- b000618 | furniture | pages [17] -->


<!-- b000619 | prose | pages [17] -->
W

<!-- b000620 | prose | pages [17] -->
 

<!-- b000621 | furniture | pages [17] -->


<!-- b000622 | prose | pages [17] -->
T

<!-- b000623 | prose | pages [17] -->
 

<!-- b000624 | prose | pages [17] -->
24 24 44

<!-- b000625 | furniture | pages [18] -->
Team # 9665

<!-- b000626 | prose | pages [18] -->
ˆ

<!-- b000627 | prose | pages [18] -->
M

<!-- b000628 | furniture | pages [18] -->
Page 17 of 30

<!-- b000629 | prose | pages [18] -->
1 is the bending moment about the x axis,

<!-- b000630 | prose | pages [18] -->
where

<!-- b000631 | prose | pages [18] -->
x

<!-- b000632 | prose | pages [18] -->
ˆT

<!-- b000633 | prose | pages [18] -->
is the curvature of the  x

<!-- b000634 | prose | pages [18] -->
is the applied torque,  longitudinal y axis (Figure 4),

<!-- b000635 | prose | pages [18] -->
which is related to the angle of twist 

<!-- b000636 | prose | pages [18] -->
W

<!-- b000637 | prose | pages [18] -->
is the rate of twist

<!-- b000638 | prose | pages [18] -->


<!-- b000639 | prose | pages [18] -->
d

<!-- b000640 | prose | pages [18] -->
 W W

<!-- b000641 | prose | pages [18] -->
by the expression:

<!-- b000642 | prose | pages [18] -->
and 22 24

<!-- b000643 | prose | pages [18] -->
dy

<!-- b000644 | prose | pages [18] -->
  are the elements of the compliance matrix. The origin of the local x and 44 y z

<!-- b000645 | prose | pages [18] -->
co-ordinate system is at the centroid（Brennan, et al，2003）.

<!-- b000646 | prose | pages [18] -->
When only a bending moment is applied we have:

<!-- b000647 | prose | pages [18] -->
1 ˆ

<!-- b000648 | prose | pages [18] -->
 W M

<!-- b000649 | prose | pages [18] -->
22

<!-- b000650 | prose | pages [18] -->
x x

<!-- b000651 | prose | pages [18] -->
W

<!-- b000652 | prose | pages [18] -->
24 ˆ  W M and . x

<!-- b000653 | prose | pages [18] -->
is decided by the intrinsic property of half pipe. we only need to calculate Since, 24 ˆ

<!-- b000654 | prose | pages [18] -->
ˆ

<!-- b000655 | prose | pages [18] -->
M (the mass of half pipe) and the projection of

<!-- b000656 | prose | pages [18] -->
M . Note that

<!-- b000657 | prose | pages [18] -->
M is the product of u

<!-- b000658 | prose | pages [18] -->
x

<!-- b000659 | prose | pages [18] -->
x

<!-- b000660 | prose | pages [18] -->
transition arc at the direction of x . Namely,

<!-- b000661 | prose | pages [18] -->
ˆ  M M    r sin , u u x

<!-- b000662 | prose | pages [18] -->
is determined by . Thus, in order to maxim the angle of twist, we xr where

<!-- b000663 | prose | pages [18] -->
should maximize and can get that

<!-- b000664 | prose | pages [18] -->
 24 ˆ W M d y x

<!-- b000665 | heading | pages [18] -->
4.4 The Determination of Parameters of Half-Pipe

<!-- b000666 | prose | pages [18] -->
ˆ

<!-- b000667 | prose | pages [18] -->
M

<!-- b000668 | prose | pages [18] -->
In order to maximize the twist angle, the bending moment

<!-- b000669 | prose | pages [18] -->
should be x

<!-- b000670 | prose | pages [18] -->
maximized. The method of determination of parameters of half-pipe is similar to that

<!-- b000671 | prose | pages [18] -->
of question 1.

<!-- b000672 | prose | pages [18] -->
v Athlete accelerates his velocity to on the flat, slides to transition at this max max

<!-- b000673 | prose | pages [18] -->
velocity and makes flight part. The key of ensuring the maximum of twist angle of

<!-- b000674 | prose | pages [18] -->
athlete is design of height and arc of transition.

<!-- b000675 | prose | pages [18] -->
sv when athlete begins his flight part, and get: We resolute the velocity

<!-- b000676 | prose | pages [18] -->
    v v cos , v v x s x y s

<!-- b000677 | prose | pages [18] -->
xv zv

<!-- b000678 | prose | pages [18] -->
      v v cos and . cos z s z y

<!-- b000679 | prose | pages [18] -->
xv are unchangeable, and athlete can convert After the flight part, and

<!-- b000680 | prose | pages [18] -->
xv ) whose central axis is that of snowboard. So, into the rotational velocity (

<!-- b000681 | prose | pages [18] -->
   is the efficiency of converting and only related to the , where v v x x

<!-- b000682 | furniture | pages [19] -->
Team # 9665

<!-- b000683 | furniture | pages [19] -->
Page 18 of 30

<!-- b000684 | prose | pages [19] -->
competence of athlete. In addition, with the consideration of benefitting athlete to

<!-- b000685 | prose | pages [19] -->
 should be relative big. return back snowboarding run, z

<!-- b000686 | prose | pages [19] -->
l , we can get the Since the radius of rotation after athlete making fight part is

<!-- b000687 | prose | pages [19] -->
angular velocity of rotation    (

<!-- b000688 | prose | pages [19] -->
 tt (

<!-- b000689 | prose | pages [19] -->
0 2

<!-- b000690 | prose | pages [19] -->
  ). In addition, the total time for xv xv / ( l / 2) 0

<!-- b000691 | prose | pages [19] -->
) can be calculated. athlete flight t 2 v / g t y

<!-- b000692 | prose | pages [19] -->
Thus, the angle of twist could be calculated as

<!-- b000693 | prose | pages [19] -->


<!-- b000694 | prose | pages [19] -->
       

<!-- b000695 | prose | pages [19] -->
    tt

<!-- b000696 | prose | pages [19] -->
, we can get For and

<!-- b000697 | furniture | pages [19] -->


<!-- b000698 | prose | pages [19] -->
90

<!-- b000699 | furniture | pages [19] -->


<!-- b000700 | prose | pages [19] -->
x y

<!-- b000701 | prose | pages [19] -->
   v v cos x s

<!-- b000702 | prose | pages [19] -->
Thus, we can derive that

<!-- b000703 | prose | pages [19] -->
       

<!-- b000704 | prose | pages [19] -->
2

<!-- b000705 | prose | pages [19] -->
t v

<!-- b000706 | prose | pages [19] -->
sin

<!-- b000707 | prose | pages [19] -->
t s

<!-- b000708 | prose | pages [19] -->
   and . v v sin y s

<!-- b000709 | prose | pages [19] -->
   

<!-- b000710 | prose | pages [19] -->
2

<!-- b000711 | prose | pages [19] -->
v

<!-- b000712 | prose | pages [19] -->
sin 2

<!-- b000713 | prose | pages [19] -->
   

<!-- b000714 | prose | pages [19] -->
s

<!-- b000715 | prose | pages [19] -->
.

<!-- b000716 | prose | pages [19] -->
cos 2

<!-- b000717 | prose | pages [19] -->
above investigation, we can get the following conclusion. Based on the

<!-- b000718 | prose | pages [19] -->
When the arc angle of transition  equals 45 degree, the twist angle is maximal.

<!-- b000719 | prose | pages [19] -->
Regarding twist angle as an optimizing object and by the method used in question

<!-- b000720 | prose | pages [19] -->
one, we obtain

<!-- b000721 | prose | pages [19] -->
xh 

<!-- b000722 | heading | pages [19] -->
6.241 m

<!-- b000723 | prose | pages [19] -->
.

<!-- b000724 | prose | pages [19] -->
And the radius of transitions can be calculated as

<!-- b000725 | prose | pages [19] -->
     / (1 cos ) r h x x 21.3 m

<!-- b000726 | prose | pages [19] -->
The method used in calculating the width of half pipe is similar to the one used in

<!-- b000727 | prose | pages [19] -->
question one. However, the arch angles of transitions in two methods are different.

<!-- b000728 | prose | pages [19] -->
 xa 165.96 m The numerical solution is .

<!-- b000729 | heading | pages [19] -->
V Tradeoffs Model to Question Three

<!-- b000730 | heading | pages [19] -->
5.1 The Determination of Parameters

<!-- b000731 | prose | pages [19] -->
Base on analysis we have done, we can conclude that the parameters calculated

<!-- b000732 | prose | pages [19] -->
with different objectives- “vertical air” or twist in the air-are different. In order to

<!-- b000733 | prose | pages [19] -->
design the half-pipe which is most suitable to athletes, we tradeoff the two kinds of

<!-- b000734 | furniture | pages [20] -->
Team # 9665

<!-- b000735 | furniture | pages [20] -->
Page 19 of 30

<!-- b000736 | prose | pages [20] -->
objectives and get the corresponding parameters.

<!-- b000737 | prose | pages [20] -->
Objective of optimization: the best achievement of athlete in the competition.

<!-- b000738 | prose | pages [20] -->
Harding and his team (2008) provide the relationship among the “vertical air”,

<!-- b000739 | prose | pages [20] -->
degree of rotation and the predicted scores of athlete obeys the following equation.

<!-- b000740 | prose | pages [20] -->
 PS 3.42 AVA

<!-- b000741 | prose | pages [20] -->
PS

<!-- b000742 | prose | pages [20] -->
   0.011 ADR 1.794 ,

<!-- b000743 | prose | pages [20] -->
AVA is the predicted scores of athletes in the competition, where is the

<!-- b000744 | prose | pages [20] -->
average “vertical air” of athletes, and ADR is the average degree of rotation.

<!-- b000745 | prose | pages [20] -->
Basing on the above equation, we can find that the “vertical air” is much more

<!-- b000746 | prose | pages [20] -->
important than the degree rotation for the scores of athletes.

<!-- b000747 | prose | pages [20] -->
For the objective of optimization is the scores given by judges, we regard the

<!-- b000748 | prose | pages [20] -->
coefficients of AVA and ADR as weight when designing half-pipe.

<!-- b000749 | prose | pages [20] -->
The weight of “vertical air” is

<!-- b000750 | prose | pages [20] -->
3.421 k  1 3.421

<!-- b000751 | prose | pages [20] -->
And , the weight of degree of rotation is

<!-- b000752 | prose | pages [20] -->
 . 0.997   0.011

<!-- b000753 | prose | pages [20] -->
0.011 k  2 3.421  . 0.003   0.011

<!-- b000754 | prose | pages [20] -->
As the width of flat and the height of platform are equal in the calculations with

<!-- b000755 | prose | pages [20] -->
different objective, there is no need to weight them. Namely,

<!-- b000756 | prose | pages [20] -->
 xh 6.241 m

<!-- b000757 | prose | pages [20] -->
xa xr To the remain parameters, and

<!-- b000758 | prose | pages [20] -->
 w 19.18 m and x

<!-- b000759 | prose | pages [20] -->
can be decided by , xh w . Thus, and x

<!-- b000760 | prose | pages [20] -->
in order to complete the design of half-pipe in the tradeoff model, the only things to

<!-- b000761 | prose | pages [20] -->
do is to determine the value of .

<!-- b000762 | prose | pages [20] -->
According to the principle of weighting, the most suitable arc angle of transitions

<!-- b000763 | prose | pages [20] -->
t should be calculated by

<!-- b000764 | prose | pages [20] -->
   k t 1 1

<!-- b000765 | prose | pages [20] -->
1 

<!-- b000766 | prose | pages [20] -->
    , k k 51.63 2 2

<!-- b000767 | prose | pages [20] -->
are arc angle of transitions in question one and two where the and 2

<!-- b000768 | prose | pages [20] -->
respectively.

<!-- b000769 | prose | pages [20] -->
It is easy to get the following parameters

<!-- b000770 | prose | pages [20] -->
 xr 16.37 m  xa 160.19 m and .

<!-- b000771 | heading | pages [20] -->
5.2 The Inclined Angle of Half-Pipe’s Placement

<!-- b000772 | prose | pages [20] -->
The inclined angle of half-pipe’s placement refers to the angle of flat plane and

<!-- b000773 | furniture | pages [21] -->
Team # 9665

<!-- b000774 | furniture | pages [21] -->
Page 20 of 30

<!-- b000775 | prose | pages [21] -->
horizontal one, which is unrelated to the size of half-pipe and only decided the method

<!-- b000776 | prose | pages [21] -->
of placement.

<!-- b000777 | prose | pages [21] -->
The angle is used for benefitting to capture the high velocity and reducing the

<!-- b000778 | prose | pages [21] -->
friction force. And a multitude of researchers have done the investigation of inclined

<!-- b000779 | prose | pages [21] -->
angle. Combing them, we get a recommended value which is 18 ° . If the size of

<!-- b000780 | prose | pages [21] -->
half-pipe is relative small, the angle should decrease slightly, however, it should in the

<!-- b000781 | prose | pages [21] -->
range of 15~18°.

<!-- b000782 | heading | pages [21] -->
VI The Discussion of other Kinds of Half Pipe

<!-- b000783 | heading | pages [21] -->
6.1 The Half Pipe whose Transitions are Ellipse

<!-- b000784 | prose | pages [21] -->
The design parameters of this kind half pipe can be applied by two methods, as is

<!-- b000785 | prose | pages [21] -->
shown in Figure 13.

<!-- b000786 | caption | pages [21] -->
Figure 13 a. The first method for designing half-pipe

<!-- b000787 | caption | pages [21] -->
Figure 13 b. The second method for designing half-pipe

<!-- b000788 | prose | pages [21] -->
To the fist method, for the slope of transition is too steep, it is very hard for athlete sliding to the top which used for making flight part. Even though he or she can reach the top of half pipe, the huge loss on velocity can be ignored too. Thus, the difficulty of snowboarding on this kind of half-pipe is relative big, and it is suit for the snowboarder who pursuit high difficulty.

<!-- b000789 | prose | pages [21] -->
To the second one, it is equivalent to extend a distance at each sides of flat. In the condition that the width of flat is wide enough, this method will waste the resource of half-pipe. What is more, the arc angle of transitions is difficult to control and it is easy to result in athlete flying out the half-pipe for the reason of the slope of transition is

<!-- b000790 | furniture | pages [22] -->
Team # 9665

<!-- b000791 | prose | pages [22] -->
too gentle.

<!-- b000792 | furniture | pages [22] -->
Page 21 of 30

<!-- b000793 | heading | pages [22] -->
6.2 The Half-Pipe whose Flat is a Arc

<!-- b000794 | prose | pages [22] -->
The transition of this kind of half-pipe is the same to that of the one we mainly

<!-- b000795 | prose | pages [22] -->
discussed, but, the flat of it is arced. For a variety of reasons such as athlete is more

<!-- b000796 | prose | pages [22] -->
vulnerable when he or she sliding on it for it is difficult to stop on the arc run, the

<!-- b000797 | prose | pages [22] -->
effect of acceleration is not obvious for it rely on the static friction, this kind of

<!-- b000798 | prose | pages [22] -->
half-pipe have been abolished.

<!-- b000799 | caption | pages [22] -->
Figure 14 shows the shape of this kind of the half-pipe.

<!-- b000800 | caption | pages [22] -->
Figure 14. The shape of half-pipe whose flat is arced.

<!-- b000801 | heading | pages [22] -->
VII The Verification of Our Models

<!-- b000802 | heading | pages [22] -->
7.1 The Verification by Living Example

<!-- b000803 | prose | pages [22] -->
We design three kinds of U-shape half-pipes, and their parameters are shown in

<!-- b000804 | caption | pages [22] -->
Table 1. In order to compare the difference between the current half-pipes used in the

<!-- b000805 | prose | pages [22] -->
competition and the one we design, we collect 6 sets of data which character the

<!-- b000806 | prose | pages [22] -->
parameters of 6 different kinds of practical half-pipe, see Table 2.

<!-- b000807 | caption | pages [22] -->
Table 1. The parameters of half-pipes we design

<!-- b000808 | prose | pages [22] -->
unit (m)

<!-- b000809 | prose | pages [22] -->
Half-pipe in Parameters

<!-- b000810 | prose | pages [22] -->
Half-pipe in

<!-- b000811 | prose | pages [22] -->
Half-pipe in

<!-- b000812 | prose | pages [22] -->
Unit

<!-- b000813 | prose | pages [22] -->
question 1

<!-- b000814 | prose | pages [22] -->
The arc angle of transitions 51.66 The length of half-pipe 159.95 The width of flat 19.18 The height of platform 6.241

<!-- b000815 | prose | pages [22] -->
question 2

<!-- b000816 | prose | pages [22] -->
question 3

<!-- b000817 | prose | pages [22] -->
45 51.63 degree 165.96 160.19 m 19.18 19.18 m 6.241 6.241 m

<!-- b000818 | furniture | pages [23] -->
Team # 9665

<!-- b000819 | furniture | pages [23] -->
Page 22 of 30

<!-- b000820 | caption | pages [23] -->
Table 2. The parameters of current half-pipes

<!-- b000821 | prose | pages [23] -->
unit (m)

<!-- b000822 | prose | pages [23] -->
Data appeared in different reference Parameters The length of half-pipe 160-220 The width of flat 18 The height of platform 7~8 160 80 100-110 160-200 18 18 13-15 18 6 5 3-3.5 5-6

<!-- b000823 | prose | pages [23] -->
By Table 1, we can find, obviously, our half-pipe belongs to the relative big one. This is because of the original velocity used for designing the height of platform is that of athlete who competing in big games. Thus, the half-pipe decided by the parameters has a relative big size and can be used for big competitions, such as Winter Olympics.

<!-- b000824 | prose | pages [23] -->
Combing the analysis of the two tables, the parameters of our half-pipes are close to that of current big one. And this phenomenon can verify the correctness of our model.

<!-- b000825 | heading | pages [23] -->
7.2 Sensitivity Analysis

<!-- b000826 | prose | pages [23] -->
By changing the original velocity used for designing and utilizing our model, xh we calculating a set of parameters of half-pipe. The range of original velocity is from 7m/s to 12m/s, and we take 11 velocities totally with the interval of 0.5 m/s. The data of parameters with different velocity is drawn in Figure 15.

<!-- b000827 | prose | pages [23] -->
the height of platform 8

<!-- b000828 | prose | pages [23] -->
6

<!-- b000829 | prose | pages [23] -->
4

<!-- b000830 | prose | pages [23] -->
2 6 8 10 12

<!-- b000831 | prose | pages [23] -->
the length of halfpipe 180

<!-- b000832 | prose | pages [23] -->
160

<!-- b000833 | prose | pages [23] -->
140

<!-- b000834 | prose | pages [23] -->
120 6 8 10 12

<!-- b000835 | prose | pages [23] -->
the arc angle of trans tions 1

<!-- b000836 | prose | pages [23] -->
0.9

<!-- b000837 | prose | pages [23] -->
0.8

<!-- b000838 | prose | pages [23] -->
0.7

<!-- b000839 | prose | pages [23] -->
0.6 6 8 10 12

<!-- b000840 | prose | pages [23] -->
the w idth of flat 22

<!-- b000841 | prose | pages [23] -->
20

<!-- b000842 | prose | pages [23] -->
18

<!-- b000843 | prose | pages [23] -->
16

<!-- b000844 | prose | pages [23] -->
14 6 8 10 12

<!-- b000845 | caption | pages [23] -->
Figure 15 The trend of half-pipe parameters in sensitivity analysis

<!-- b000846 | furniture | pages [24] -->
Team # 9665

<!-- b000847 | prose | pages [24] -->
As Figure 15 showing, we can get that

<!-- b000848 | prose | pages [24] -->
 The size of half-pipe increase with

<!-- b000849 | prose | pages [24] -->
 xh , xa and are linear with w 0v x

<!-- b000850 | prose | pages [24] -->


<!-- b000851 | furniture | pages [24] -->
Page 23 of 30

<!-- b000852 | prose | pages [24] -->
0v

<!-- b000853 | prose | pages [24] -->
approximately

<!-- b000854 | prose | pages [24] -->
The arc angle of transitions has the broken line relationship with 0v , and the

<!-- b000855 | prose | pages [24] -->
is relatively big. linearity is better when 0v

<!-- b000856 | prose | pages [24] -->
The specific data of them are shown in Table 3

<!-- b000857 | caption | pages [24] -->
Table 3. The data calculated in sensitivity analysis

<!-- b000858 | prose | pages [24] -->
v 0 m/s

<!-- b000859 | prose | pages [24] -->
7 7.5 8 8.5 9

<!-- b000860 | prose | pages [24] -->
xa m

<!-- b000861 | prose | pages [24] -->
124.31 128.72 135.12 139.78 144.25

<!-- b000862 | prose | pages [24] -->
xh m

<!-- b000863 | prose | pages [24] -->
2.50 2.89 3.27 3.69 4.13

<!-- b000864 | prose | pages [24] -->
w m

<!-- b000865 | prose | pages [24] -->
15.22 15.73 16.23 16.73 17.23

<!-- b000866 | prose | pages [24] -->
x

<!-- b000867 | prose | pages [24] -->
 degree

<!-- b000868 | prose | pages [24] -->
40.69 40.79 44.67 46.03 47.17

<!-- b000869 | prose | pages [24] -->
9.5 10 10.5 11 11.5 12

<!-- b000870 | prose | pages [24] -->
148.47 152.45 156.15 159.1 162.94 165.94 4.60 5.10 5.63 6.17 6.75 7.35 17.73 18.24 18.74 19.24 19.74 20.24 48.29 49.39 50.49 51.58 52.64 53.70

<!-- b000871 | prose | pages [24] -->
takes the value of 8, 9, 10 and 11m/s, the theoretical From Table 3, when 0v results match the current half-pipe very well, which agrees with our model.

<!-- b000872 | prose | pages [24] -->
Base on the data in Table 3, we divide the half pipes into three kinds-small, medium and big and recommend the relative classic parameters of them.

<!-- b000873 | prose | pages [24] -->
The big half-pipe:

<!-- b000874 | prose | pages [24] -->
xa  xh  , 159.71 6.17

<!-- b000875 | prose | pages [24] -->
The medium half-pipe:

<!-- b000876 | prose | pages [24] -->
xa  xh  , 139.78 3.69

<!-- b000877 | prose | pages [24] -->
The small half-pipe:

<!-- b000878 | prose | pages [24] -->
xa  xh  , 128.72 2.89

<!-- b000879 | prose | pages [24] -->
 w  51.58 , , and . 19.24 x

<!-- b000880 | prose | pages [24] -->
 w  46.03 , , and . 16.73 x

<!-- b000881 | prose | pages [24] -->
 w  40.79 , , and . 15.73 x

<!-- b000882 | prose | pages [24] -->
On the condition of other requirement required, the designer can look up Table 3 to get the corresponding parameters of half-pipe. Obviously, by sensitivity analysis, the range available is extended largely.

<!-- b000883 | heading | pages [24] -->
VIII Strengths and Weaknesses

<!-- b000884 | heading | pages [24] -->
8.1 Strengths

<!-- b000885 | prose | pages [24] -->


<!-- b000886 | heading | pages [24] -->
Simplicity: The mathematical model we construct is simple enough to

<!-- b000887 | prose | pages [24] -->
understand with a small amount of mathematical skill. And, the calculation of it can solved by simple mathematical software such as Matlab.

<!-- b000888 | furniture | pages [25] -->
Team # 9665

<!-- b000889 | prose | pages [25] -->


<!-- b000890 | furniture | pages [25] -->
Page 24 of 30

<!-- b000891 | heading | pages [25] -->
Flexibility: Models in this paper consider influence on the performance of

<!-- b000892 | prose | pages [25] -->
athletes given by the parameters-height, width, angle and so on –of half pipe to ensure the flexibility and entity of the design. By doing so, it can design different shape of half pipes with different requirements.

<!-- b000893 | prose | pages [25] -->


<!-- b000894 | heading | pages [25] -->
Operability: Our models take into account the criteria of snowboarding and

<!-- b000895 | prose | pages [25] -->
promote the design plan, which helps athlete perform better in the competitions.

<!-- b000896 | prose | pages [25] -->
 Developed from history data: All the data we used are from the records of Olympic Games.

<!-- b000897 | prose | pages [25] -->
 Refinement: Base on considering other factors such as injures of athlete, we

<!-- b000898 | prose | pages [25] -->
refine our model.

<!-- b000899 | heading | pages [25] -->
8.2 Weaknesses

<!-- b000900 | prose | pages [25] -->


<!-- b000901 | heading | pages [25] -->
Assumptions: Simplifying assumptions such as ignoring air resistance had to

<!-- b000902 | prose | pages [25] -->
be made in order to create a calculable model.

<!-- b000903 | prose | pages [25] -->


<!-- b000904 | heading | pages [25] -->
Inputs：This verification of model requires a multitude data, some of which is

<!-- b000905 | prose | pages [25] -->
difficult to obtain.

<!-- b000906 | heading | pages [25] -->
IX The Refinement of our Model

<!-- b000907 | heading | pages [25] -->
9.1 The Refined Model Considering the Air Resistance

<!-- b000908 | prose | pages [25] -->
As the equation (Answer.com) of calculating the air resistance is

<!-- b000909 | prose | pages [25] -->
1  f a 2     2 c c S v w

<!-- b000910 | prose | pages [25] -->
is the air resistance, c is the coefficient of air resistance,  where, af is the

<!-- b000911 | prose | pages [25] -->
is the frontal area of object and v is density of air.

<!-- b000912 | prose | pages [25] -->
S w

<!-- b000913 | prose | pages [25] -->
 and air. In addition, c

<!-- b000914 | prose | pages [25] -->
relative velocity of object

<!-- b000915 | prose | pages [25] -->
are constants. And and

<!-- b000916 | prose | pages [25] -->
variation is very small.

<!-- b000917 | prose | pages [25] -->
is variable, however, the S w

<!-- b000918 | prose | pages [25] -->
Based on the analysis above, we can conclude that

<!-- b000919 | furniture | pages [26] -->
Team # 9665

<!-- b000920 | furniture | pages [26] -->
Page 25 of 30

<!-- b000921 | prose | pages [26] -->
In the process of sliding, the air resistance is proportional to the square of velocity.

<!-- b000922 | prose | pages [26] -->
In horizontal direction,

<!-- b000923 | prose | pages [26] -->
dS

<!-- b000924 | prose | pages [26] -->
And the work done by air resistance is

<!-- b000925 | prose | pages [26] -->
S

<!-- b000926 | prose | pages [26] -->
max

<!-- b000927 | prose | pages [26] -->


<!-- b000928 | prose | pages [26] -->


<!-- b000929 | prose | pages [26] -->
W

<!-- b000930 | prose | pages [26] -->
fa

<!-- b000931 | prose | pages [26] -->
0

<!-- b000932 | prose | pages [26] -->
S

<!-- b000933 | prose | pages [26] -->
max

<!-- b000934 | prose | pages [26] -->


<!-- b000935 | prose | pages [26] -->


<!-- b000936 | furniture | pages [26] -->


<!-- b000937 | prose | pages [26] -->
0

<!-- b000938 | prose | pages [26] -->
dt  v

<!-- b000939 | prose | pages [26] -->
.

<!-- b000940 | prose | pages [26] -->
f dS

<!-- b000941 | prose | pages [26] -->
a a

<!-- b000942 | prose | pages [26] -->
 c S

<!-- b000943 | prose | pages [26] -->


<!-- b000944 | prose | pages [26] -->
2

<!-- b000945 | prose | pages [26] -->
w

<!-- b000946 | prose | pages [26] -->
( ( )

<!-- b000947 | prose | pages [26] -->
v dS

<!-- b000948 | prose | pages [26] -->
2

<!-- b000949 | prose | pages [26] -->
.

<!-- b000950 | prose | pages [26] -->
The equation of velocity on the flat investigated in question is applicable and

<!-- b000951 | prose | pages [26] -->
 t 1 s is reached when . Thus, S max

<!-- b000952 | prose | pages [26] -->


<!-- b000953 | prose | pages [26] -->
1 1

<!-- b000954 | prose | pages [26] -->
c S

<!-- b000955 | prose | pages [26] -->
 

<!-- b000956 | prose | pages [26] -->
  

<!-- b000957 | prose | pages [26] -->
3

<!-- b000958 | prose | pages [26] -->
w

<!-- b000959 | prose | pages [26] -->
W

<!-- b000960 | prose | pages [26] -->
( )

<!-- b000961 | prose | pages [26] -->
v dt

<!-- b000962 | prose | pages [26] -->
(

<!-- b000963 | prose | pages [26] -->
fa

<!-- b000964 | prose | pages [26] -->
2

<!-- b000965 | prose | pages [26] -->
0 0

<!-- b000966 | prose | pages [26] -->


<!-- b000967 | prose | pages [26] -->
c S

<!-- b000968 | prose | pages [26] -->
2425 95

<!-- b000969 | prose | pages [26] -->
  

<!-- b000970 | prose | pages [26] -->
3

<!-- b000971 | prose | pages [26] -->
w

<!-- b000972 | furniture | pages [26] -->


<!-- b000973 | prose | pages [26] -->
(

<!-- b000974 | prose | pages [26] -->
g

<!-- b000975 | prose | pages [26] -->
2 224

<!-- b000976 | prose | pages [26] -->
S ,  For the given c ,

<!-- b000977 | prose | pages [26] -->


<!-- b000978 | prose | pages [26] -->
c S

<!-- b000979 | prose | pages [26] -->
  

<!-- b000980 | prose | pages [26] -->
2 3

<!-- b000981 | prose | pages [26] -->
w

<!-- b000982 | prose | pages [26] -->
) ( 1

<!-- b000983 | prose | pages [26] -->
v

<!-- b000984 | prose | pages [26] -->
2.5

<!-- b000985 | prose | pages [26] -->
gt

<!-- b000986 | prose | pages [26] -->
1.25

<!-- b000987 | prose | pages [26] -->
gt

<!-- b000988 | prose | pages [26] -->
)

<!-- b000989 | prose | pages [26] -->
dt

<!-- b000990 | prose | pages [26] -->
2

<!-- b000991 | prose | pages [26] -->
 

<!-- b000992 | prose | pages [26] -->
2 2 3

<!-- b000993 | prose | pages [26] -->
g

<!-- b000994 | prose | pages [26] -->
5

<!-- b000995 | prose | pages [26] -->
v g v

<!-- b000996 | prose | pages [26] -->
)

<!-- b000997 | prose | pages [26] -->
1 1

<!-- b000998 | prose | pages [26] -->
8 8

<!-- b000999 | prose | pages [26] -->
1v , the numerical solution of and w

<!-- b001000 | prose | pages [26] -->
Thus, just by substituting the sum of W f

<!-- b001001 | prose | pages [26] -->
parameters of half-pipe can be calculated.

<!-- b001002 | prose | pages [26] -->
is a constant. W fa

<!-- b001003 | prose | pages [26] -->
and W into the models we construct, the fa

<!-- b001004 | heading | pages [26] -->
9.2 The Refined Model Considering the Safety of Athlete

<!-- b001005 | prose | pages [26] -->
Snowboarders are vulnerable in the competition, and combing the safety factor

<!-- b001006 | prose | pages [26] -->
into the design of half-pipe is necessary. By analyzing the relationship of safety and

<!-- b001007 | prose | pages [26] -->
the twist angle, we can get the function between them. Then, by substituting the factor

<!-- b001008 | prose | pages [26] -->
of safety by the twist angle into the model we constructed, the parameters of half-pipe

<!-- b001009 | prose | pages [26] -->
are also be calculated.

<!-- b001010 | furniture | pages [27] -->
Team # 9665

<!-- b001011 | prose | pages [27] -->
Reference

<!-- b001012 | furniture | pages [27] -->
Page 26 of 30

<!-- b001013 | prose | pages [27] -->
[1] Brennan,S.M. et al. 2003. Modelling the mechanical characteristics and on-snow

<!-- b001014 | prose | pages [27] -->
performance of snowboards. Sports Engineering 6, 193-206. [2] ABC-OF-SNOWBOARDING. Halfpipe Snowboarding/ Half Pipes Halfpipes.

<!-- b001015 | prose | pages [27] -->
http://www.abc-of-snowboarding.com/snowboardinghalfpipe.asp. [3] Hongguang,Yuan.et al.2009.Factors Influencing Velocity Away from Decks in

<!-- b001016 | prose | pages [27] -->
Snowboard Half-pipe.Journal of Shenyang Sport University 28(3),16-28. [4] Harding,J.W. et al. 2007. Feature Extraction of Performance Variables in Elite

<!-- b001017 | prose | pages [27] -->
Half-Pipe Snowboarding Using Body Mounted Inertial Sensors. http://www.anarchistathlete.com/wp-content/uploads/2009/05/harding-et-al-_200 7_-feature-extraction-hp-kpvs-inertial-sesnors.pdf. [5] Kollár, L.P. and Springer, G.S. 2003. Mechanics of Composite Structures, p. 209.

<!-- b001018 | prose | pages [27] -->
Cambridge University Press, New York, NY, USA. [6] Answers.com. What is the formula for air resistance please state what each

<!-- b001019 | prose | pages [27] -->
symbol or letter stands for? http://wiki.answers.com/Q/What_is_the_formula_for _air_resistance_please_state_what_each_symbol_or_letter_stands_for. [7] Harding, J.W and James,D.A.2010. Performance Assessment Innovations for

<!-- b001020 | prose | pages [27] -->
Elite Snowboarding. 8th Conference of the International Sports Engineering Association. [8] Harding,J.W. et al. 2008. Automated scoring for elite half-pipe snowboard

<!-- b001021 | prose | pages [27] -->
competition: important sporting development or techno distraction? Sports Technology Journal. No.6, 277-290.

<!-- b001022 | prose | pages [27] -->
Construction: [9] Snowboarding.

<!-- b001023 | prose | pages [27] -->
Halfpipe The Shape of Things to Come. http://snowboarding.transworld.net/1000022552/how-to/halfpipe-construction-the -shape-of-things-to-come/ [10]Wikipedia, the free encyclopedia. Half-pipe, http://en.wikipedia.org/wiki/Half

<!-- b001024 | prose | pages [27] -->
pipe.

<!-- b001025 | prose | pages [27] -->
Experimental [11]Subic, Aleksandar,et al.2010.

<!-- b001026 | prose | pages [27] -->
installation for evaluation of snowboard simulated on snow dynamic performance.8th Conference of the International Sports Engineering Association [12]Buffinton, Keith W.2003.Laboratory, computational and field studies of snowboard dynamics, Sports Engineering 6,129-137. [13]Thomas, H, et al.2010.Recognizing Turns and Other Snowboarding Activities

<!-- b001027 | prose | pages [27] -->
with a Gyroscope.http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber= 5648406

<!-- b001028 | furniture | pages [28] -->
Team # 9665

<!-- b001029 | heading | pages [28] -->
Appendix

<!-- b001030 | heading | pages [28] -->
A 1. The solution of in question 1

<!-- b001031 | furniture | pages [28] -->
Page 27 of 30

<!-- b001032 | prose | pages [28] -->
f = @(x)-sqrt(2/75*(0.5*75*23.31^2-0.1*75*9.8*(19.81+25.*x)/cos(5*pi/180)

<!-- b001033 | prose | pages [28] -->
-75*9.8*25*(1-cos(x)))).*sin(x); % The positive number of

<!-- b001034 | prose | pages [28] -->
x = fminbnd(f, 0, 2) y = -f(x)

<!-- b001035 | prose | pages [28] -->
yv

<!-- b001036 | prose | pages [28] -->
A2. The Figure characterizes the relationship between arch angle and velocity

<!-- b001037 | prose | pages [28] -->
syms o; o=0.001:0.001:pi/2; g=9.8;a=5*pi/180;rx=25;wx=19.81; m=75;vmax=23.31;f1=0.1*m*g; vy=sqrt(2/m*(0.5*m*vmax^2-f1*(wx+rx.*o)/cos(a)-m*g*rx*(1-cos(o)))).*sin(o); plot(o,vy)

<!-- b001038 | heading | pages [28] -->
A3. The solution of width of half-pipe

<!-- b001039 | prose | pages [28] -->
a=5*pi/180;rx=16.44;o=51.66*pi/180;smax=19.27;rx=16.44; hx=6.241;u=0.1;m=75;g=9.8;vmax=23.31;wx=19.18;n=7; AB=rx*o/cos(a); CD=smax+2*AB; vs=sqrt(2/m*(0.5*m*vmax^2-u*m*g*AB-m*g*hx)); vx=vs*cos(o); vy=vs*sin(o); tt=2*vy/g; a0=CD*sin(a) +2*rx*o*sin(a) +vx*tt; ax=a0*n

<!-- b001040 | heading | pages [28] -->
A4. Sensitivity Analysis

<!-- b001041 | prose | pages [28] -->
% the solution for horizontal distance

<!-- b001042 | prose | pages [28] -->
% The solution for parameters of half-pipe thta=[40.6857 40.7889 44.6735 48.2889 49.3947 50.4948 o=thta*pi/180; vmax=[19.2500 19.7500 20.2500 22.2500 22.7500 23.2500 wx=[15.2246 15.7265 16.2284 18.2361 18.7380 19.2399 smax=[15.1667 15.6667 16.1667 46.0314 47.1659... 51.5777 52.6434 53.6976];

<!-- b001043 | prose | pages [28] -->
20.7500 21.2500 21.7500... 23.7500 24.2500]; 16.7303 17.2322 17.7342... 19.7418 20.2437]; 16.6667 17.1667 17.6667...

<!-- b001044 | furniture | pages [29] -->
Team # 9665

<!-- b001045 | prose | pages [29] -->
18.1667 18.6667 19.1667

<!-- b001046 | furniture | pages [29] -->
Page 28 of 30

<!-- b001047 | prose | pages [29] -->
19.6667 20.1667]; hx=[2.5 2.89 3.27 3.69 4.13 4.60 5.1 5.63 6.17 6.75 7.35]; % The parameter matrix corresponding to the chosen data a=5*pi/180;rx=16.37; u=0.1;m=75;g=9.8; AB=rx*o/cos(a); CD=smax+2*AB; vs=sqrt(2/m*(0.5*m*vmax.^2-u*m*g*AB-m*g*hx)); vx=vs.*cos(o); vy=vs.*sin(o); tt=2*vy/g; a0=(CD*sin(a) +2*rx*o*sin(a) +vx.*tt); a1=a0*7

<!-- b001048 | prose | pages [29] -->
% Plotting the relationship figures of

<!-- b001049 | prose | pages [29] -->
v0=7:0.5:12;

<!-- b001050 | prose | pages [29] -->
subplot(231) plot(v0,hx,'r-o') title('hx'),xlabel('v0')

<!-- b001051 | prose | pages [29] -->
subplot(232) plot(v0,smax,'b-d') title('smax'),xlabel('v0')

<!-- b001052 | prose | pages [29] -->
subplot(233) plot(v0,o,'k-*') title('o'),xlabel('v0')

<!-- b001053 | prose | pages [29] -->
subplot(234) plot(v0,a1,'m-p') title('a1'),xlabel('v0')

<!-- b001054 | prose | pages [29] -->
subplot(235) plot(v0,vmax,'K-+') title('vmax'),xlabel('v0')

<!-- b001055 | prose | pages [29] -->
subplot(236) plot(v0,wx,'c-<') title('wx'),xlabel('v0')

<!-- b001056 | prose | pages [29] -->
A5. The data appeared in references

<!-- b001057 | prose | pages [29] -->
and parameters of half-pipe yv yv

<!-- b001058 | prose | pages [29] -->
Data appeared in different reference Parameters The length of half-pipe 160-220 160 80 100-110

<!-- b001059 | furniture | pages [30] -->
Team # 9665

<!-- b001060 | prose | pages [30] -->
The width of flat 18 The height of platform

<!-- b001061 | prose | pages [30] -->
7~8

<!-- b001062 | prose | pages [30] -->
The inclined angle

<!-- b001063 | prose | pages [30] -->
18

<!-- b001064 | furniture | pages [30] -->
Page 29 of 30

<!-- b001065 | prose | pages [30] -->
18 18 13-15

<!-- b001066 | prose | pages [30] -->
6 5 3-3.5 18 15 15~18

<!-- b001067 | prose | pages [30] -->
Data appeared in different reference Parameters The length of half-pipe 135 The width of flat 17.5 The height of platform

<!-- b001068 | prose | pages [30] -->
4.8

<!-- b001069 | prose | pages [30] -->
The inclined angle

<!-- b001070 | prose | pages [30] -->
16.5

<!-- b001071 | heading | pages [30] -->
A6. The results calculated in the solution

<!-- b001072 | prose | pages [30] -->
0v

<!-- b001073 | prose | pages [30] -->
7 7.5 8 8.5 9 m/s

<!-- b001074 | prose | pages [30] -->
xa

<!-- b001075 | prose | pages [30] -->
124.31 128.72 135.12 139.78 144.25 m

<!-- b001076 | prose | pages [30] -->
xh

<!-- b001077 | prose | pages [30] -->
2.50 2.89 3.27 3.69 4.13 m

<!-- b001078 | prose | pages [30] -->
w

<!-- b001079 | prose | pages [30] -->
15.22 15.73 16.23 16.73 17.23 m

<!-- b001080 | prose | pages [30] -->
x

<!-- b001081 | prose | pages [30] -->


<!-- b001082 | prose | pages [30] -->
40.69 40.79 44.67 46.03 47.17 degree

<!-- b001083 | prose | pages [30] -->
S

<!-- b001084 | prose | pages [30] -->
15.17 15.67 16.17 16.67 17.17 m

<!-- b001085 | prose | pages [30] -->
max

<!-- b001086 | prose | pages [30] -->
v

<!-- b001087 | prose | pages [30] -->
19.25 19.75 20.25 20.75 21.25 m

<!-- b001088 | prose | pages [30] -->
max

<!-- b001089 | prose | pages [30] -->
sv

<!-- b001090 | prose | pages [30] -->
17.28 17.62 17.91 18.23 18.55 m/s

<!-- b001091 | prose | pages [30] -->
tt

<!-- b001092 | prose | pages [30] -->
2.30 2.35 2.57 2.68 2.78 s

<!-- b001093 | prose | pages [30] -->
135 120 130 17.5 17.0 16.0

<!-- b001094 | prose | pages [30] -->
4.8 4.5 4.6 16.5 16.0 16.5

<!-- b001095 | prose | pages [30] -->
9.5 10 10.5 11 11.5 12

<!-- b001096 | prose | pages [30] -->
148.47 152.45 156.15 159.1 162.94 165.94

<!-- b001097 | prose | pages [30] -->
4.60 5.10 5.63 6.17 6.75 7.35

<!-- b001098 | prose | pages [30] -->
17.73 18.24 18.74 19.24 19.74 20.24

<!-- b001099 | prose | pages [30] -->
48.29 49.39 50.49 51.58 52.64 53.70

<!-- b001100 | prose | pages [30] -->
17.67 18.17 18.67 19.17 19.67 20.17

<!-- b001101 | prose | pages [30] -->
21.75 22.25 22.75 23.25 23.75 24.25

<!-- b001102 | prose | pages [30] -->
18.86 19.17 19.46 19.76 20.05 20.34

<!-- b001103 | prose | pages [30] -->
2.87 2.97 3.06 3.16 3.25 3.35
