# P-B-2020-2011873-0d3ec7b7

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
2020

<!-- b000004 | prose | pages [1] -->
Problem Chosen

<!-- b000005 | furniture | pages [1] -->
Team Control Number

<!-- b000006 | furniture | pages [1] -->
2011873

<!-- b000007 | prose | pages [1] -->
MCM/ICM

<!-- b000008 | title | pages [1] -->
B

<!-- b000009 | heading | pages [1] -->
Summary Sheet

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | furniture | pages [1] -->


<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | prose | pages [1] -->
The Longest Lasting Sandcastle

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | prose | pages [1] -->
A variety of sandcastles can be found on the seashore, range from simple mounds of sand to complex castle replicas. Over time, there is no doubt that rain and waves will gradually erode the sandcastle. However, the degree of erosion of different types of sandcastles is different. Even if the building size and the distance from the water on the same beach are roughly same. Therefore, we wonder if there exits an optimal 3D geometric shape to use as sandcastle foundation.

<!-- b000017 | prose | pages [1] -->
In task 1, in order to identity the best 3D geometric shape of sandcastle foundation, firstly, our team choose six common geometric shapes to analyze. Then, we introduce Mohr-Coulomb Yielding Criteria to check the strength of sandcastle foundation, Horton’s equation to calculate infiltration rate of seawater, further Van Genuchten Model to obtain water retention curve. Based on the study of water content, we use internal friction angle to determine whether the sandcastle is stable or not. Finally,we work out the cuboid is the best, of which lasting time is 50min.What’s more, by traversing the aspect ratio of the cuboid, we find that the narrower the width of the water surface is, the longer lasting time is.

<!-- b000018 | prose | pages [1] -->
In task 2, take sand-to-water mixture proportion into consideration. Because the sand-to-water ratio is related to the structural stability of the sandcastle, by establishing the function relationship between sand-to-water mixing ratio and internal friction angle, then programming traversal, we find that the optimal solution is when the water-to-sand ratio is 15%, and lasting time of the sandcastle 64.43min.

<!-- b000019 | prose | pages [1] -->
In task 3, we divide the impact of rainwater on the sandcastle into two parts: scour and infiltration. We find that the cuboid is still the optimal geometry, confirming the reliability of our model. Besides, ANSYS simulation analysis is used to verify the theoretical results, and results are very similar.

<!-- b000020 | prose | pages [1] -->
To sum up, by consulting a large amount of data, we establish wave erosion, tidal immersion, rain scour, and rain immersion models. The model establishment has a gradual optimization process, and the results of rain immersion are analyzed using ANSYS simulation. It is in good agreement with the theoretical calculation, which verifies the correctness of our model.

<!-- b000021 | keywords | pages [1] -->
Keywords: Mohr-Coulomb Yielding Criteria, Horton’s equation, Van Genuchten Model, Internal

<!-- b000022 | prose | pages [1] -->
friction angle, ANSYS simulation.

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | prose | pages [1] -->
关注数学模型

<!-- b000025 | furniture | pages [1] -->
2

<!-- b000026 | furniture | pages [1] -->
MATHmodels

<!-- b000027 | furniture | pages [1] -->
获取更多资讯

<!-- b000028 | furniture | pages [2] -->
Team #2011873                                                                 Page 1 of 22

<!-- b000029 | prose | pages [2] -->
Content

<!-- b000030 | furniture | pages [2] -->


<!-- b000031 | prose | pages [2] -->
1. Introduction ............................................................................................................................ 2

<!-- b000032 | prose | pages [2] -->
1.1Background ...................................................................................................................... 2

<!-- b000033 | prose | pages [2] -->
1.2 Our work .......................................................................................................................... 2

<!-- b000034 | prose | pages [2] -->
2. Assumptions .......................................................................................................................... 2

<!-- b000035 | prose | pages [2] -->
3. Symbols ................................................................................................................................. 3

<!-- b000036 | prose | pages [2] -->
4. Task 1: Identify the Best Three-Dimensional Geometric Shape ........................................... 3

<!-- b000037 | prose | pages [2] -->
4.1 Only consider the force of seawater on the sandcastle .................................................... 4

<!-- b000038 | prose | pages [2] -->
4.1.1 Airy wave theory ...................................................................................................... 4

<!-- b000039 | prose | pages [2] -->
4.1.2 The Morison Equation .............................................................................................. 5

<!-- b000040 | prose | pages [2] -->
4.1.3 Mohr-Coulomb Yielding Criteria ............................................................................. 6

<!-- b000041 | prose | pages [2] -->
4.2 Consider changes of water content in Sandcastle ............................................................ 8

<!-- b000042 | prose | pages [2] -->
4.2.1 Horton’s equation ..................................................................................................... 8

<!-- b000043 | prose | pages [2] -->
4.2.2 Van Genuchten Model .............................................................................................. 8

<!-- b000044 | prose | pages [2] -->
4.3 Conclusion ....................................................................................................................... 9

<!-- b000045 | prose | pages [2] -->
4.3.1 Take the cuboid as an example ................................................................................. 9

<!-- b000046 | prose | pages [2] -->
4.3.2 Best Three-dimensional geometric shape ............................................................... 10

<!-- b000047 | prose | pages [2] -->
4.3.3 Sensitivity analysis ................................................................................................. 11

<!-- b000048 | prose | pages [2] -->
5. Task 2: Take Sand-to-Water Mixture Proportion into Consideration ................................. 12

<!-- b000049 | prose | pages [2] -->
6. Task 3: Take Effect of Rain into Consideration .................................................................. 13

<!-- b000050 | prose | pages [2] -->
6.1 Precipitation model ........................................................................................................ 13

<!-- b000051 | prose | pages [2] -->
6.2 Sartor-Boyd scour model ............................................................................................... 14

<!-- b000052 | prose | pages [2] -->
6.3 Seepage process ............................................................................................................. 15

<!-- b000053 | prose | pages [2] -->
6.4 ANSYS simulation ........................................................................................................ 17

<!-- b000054 | prose | pages [2] -->
7. Task 4：Other Strategies to Make Sandcastles Last Longer .............................................. 17

<!-- b000055 | prose | pages [2] -->
8. Strengths and Weaknesses ................................................................................................... 18

<!-- b000056 | prose | pages [2] -->
8.1 Strengths ........................................................................................................................ 18

<!-- b000057 | prose | pages [2] -->
8.2 Weaknesses ................................................................................................................... 18

<!-- b000058 | prose | pages [2] -->
Article ...................................................................................................................................... 19

<!-- b000059 | prose | pages [2] -->
Reference ................................................................................................................................. 21

<!-- b000060 | prose | pages [2] -->
关注数学模型

<!-- b000061 | furniture | pages [2] -->
2

<!-- b000062 | furniture | pages [2] -->
MATHmodels

<!-- b000063 | furniture | pages [2] -->
获取更多资讯

<!-- b000064 | furniture | pages [3] -->
Team #2011873                                                                 Page 2 of 22

<!-- b000065 | furniture | pages [3] -->


<!-- b000066 | furniture | pages [3] -->


<!-- b000067 | prose | pages [3] -->
A variety of sandcastles can be found on the seashore, range from simple mounds

<!-- b000068 | prose | pages [3] -->
of sand to complex castle replicas. In all these, one typically forms an initial foundation

<!-- b000069 | prose | pages [3] -->
consisting of a single, nondescript mound of wetted sand, and then proceeds to cut and

<!-- b000070 | prose | pages [3] -->
shape this base into a recognizable 3-dimensional geometric shape, thereby building

<!-- b000071 | prose | pages [3] -->
more castle-defining features.

<!-- b000072 | prose | pages [3] -->
Over time, there is no doubt that rain and waves will gradually erode the sandcastle.

<!-- b000073 | prose | pages [3] -->
However, the degree of erosion of different types of sandcastles is different. Even if the

<!-- b000074 | prose | pages [3] -->
building size and the distance from the water on the same beach are roughly same.

<!-- b000075 | prose | pages [3] -->
Therefore, in order to achieve highest robustness and longest lasting time, we

<!-- b000076 | prose | pages [3] -->
wonder if there exits an optimal 3D geometric shape to use as the foundation of a

<!-- b000077 | prose | pages [3] -->
sandcastle.

<!-- b000078 | furniture | pages [3] -->


<!-- b000079 | prose | pages [3] -->
To further present our solutions, we arrange our paper as follows:

<!-- b000080 | prose | pages [3] -->
⚫ In task 1, we use six common geometric shapes for research. By establishing

<!-- b000081 | prose | pages [3] -->
tide immersion model and wave erosion model, we calculate that the cuboid is

<!-- b000082 | prose | pages [3] -->
the optimal geometric model. Further research, through the study of cuboids

<!-- b000083 | prose | pages [3] -->
with different aspect ratios, we find that the smaller the width of the cuboid

<!-- b000084 | prose | pages [3] -->
facing the water, the longer the model exists.

<!-- b000085 | prose | pages [3] -->
⚫ In task 2, different sand-to-water mixing ratios will affect the strength of

<!-- b000086 | prose | pages [3] -->
sandcastles. By establishing the function relationship between different sand-

<!-- b000087 | prose | pages [3] -->
to-water mixing ratios and internal friction angles, we find 15% is the best.

<!-- b000088 | prose | pages [3] -->
⚫ In task 3, we divide the impact of rainwater on the sandcastle into two parts:

<!-- b000089 | prose | pages [3] -->
scour and infiltration. Through ANSYS simulation. we get the effects of

<!-- b000090 | prose | pages [3] -->
rainfall on the six geometries, which are very similar to the theory.

<!-- b000091 | prose | pages [3] -->
⚫ In task 4, we consider two aspects of reducing seawater infiltration and

<!-- b000092 | prose | pages [3] -->
reducing wave erosion to extend the lasting time of the sandcastle

<!-- b000093 | furniture | pages [3] -->


<!-- b000094 | prose | pages [3] -->
⚫ Assume that the bottom of the model is at a horizontal plane.

<!-- b000095 | prose | pages [3] -->
⚫ Suppose the waves are moving without amplitude attenuation.

<!-- b000096 | prose | pages [3] -->
⚫ Disregard the impact of sandcastle's own gravity.

<!-- b000097 | prose | pages [3] -->
关注数学模型

<!-- b000098 | furniture | pages [3] -->
2

<!-- b000099 | furniture | pages [3] -->
MATHmodels

<!-- b000100 | furniture | pages [3] -->
获取更多资讯

<!-- b000101 | furniture | pages [4] -->
Team #2011873                                                                 Page 3 of 22

<!-- b000102 | prose | pages [4] -->
⚫ Assume that the seawater penetrates into the sandcastle uniformly.

<!-- b000103 | furniture | pages [4] -->


<!-- b000104 | prose | pages [4] -->
Symbol

<!-- b000105 | prose | pages [4] -->
V

<!-- b000106 | prose | pages [4] -->
a

<!-- b000107 | prose | pages [4] -->
u

<!-- b000108 | prose | pages [4] -->
u

<!-- b000109 | prose | pages [4] -->
Description

<!-- b000110 | prose | pages [4] -->
Volume of sandcastle

<!-- b000111 | prose | pages [4] -->
Wave amplitude

<!-- b000112 | prose | pages [4] -->
Wave speed

<!-- b000113 | prose | pages [4] -->
Wave acceleration

<!-- b000114 | prose | pages [4] -->
Wave total inline force F

<!-- b000115 | prose | pages [4] -->
w

<!-- b000116 | prose | pages [4] -->


<!-- b000117 | prose | pages [4] -->
Water content in sand

<!-- b000118 | prose | pages [4] -->
Normal stress on the cross section n

<!-- b000119 | prose | pages [4] -->
 Shear stress on the cross section n

<!-- b000120 | prose | pages [4] -->


<!-- b000121 | prose | pages [4] -->
V

<!-- b000122 | prose | pages [4] -->
Internal friction angle

<!-- b000123 | prose | pages [4] -->
Average final speed of raindrops m

<!-- b000124 | furniture | pages [4] -->


<!-- b000125 | furniture | pages [4] -->


<!-- b000126 | prose | pages [4] -->
In this problem, according to the situation of people building sandcastles on the

<!-- b000127 | prose | pages [4] -->
beach, we analyze six common 3D geometries with relatively stable structures to select

<!-- b000128 | prose | pages [4] -->
the best. Assume that they have the same volume and height.

<!-- b000129 | furniture | pages [4] -->


<!-- b000130 | caption | pages [4] -->
Figure 1. Six 3D geometries we select

<!-- b000131 | furniture | pages [4] -->


<!-- b000132 | furniture | pages [4] -->


<!-- b000133 | prose | pages [4] -->
Considering that tide will destroy the sandcastle, and as the tide rises, the tide will

<!-- b000134 | prose | pages [4] -->
关注数学模型

<!-- b000135 | furniture | pages [4] -->
2

<!-- b000136 | furniture | pages [4] -->
MATHmodels

<!-- b000137 | furniture | pages [4] -->
获取更多资讯

<!-- b000138 | furniture | pages [5] -->
Team #2011873                                                                 Page 4 of 22

<!-- b000139 | prose | pages [5] -->
gradually flood the bottom of the sandcastle, and the water content of the sandcastle

<!-- b000140 | prose | pages [5] -->
will continue to rise. When the sandcastle is completely immersed in seawater, we have

<!-- b000141 | prose | pages [5] -->
no need to explore it. Therefore, we divide the whole process into three stages:

<!-- b000142 | prose | pages [5] -->
1) The sandcastle is not flooded. In this case, we mainly consider the force of tide

<!-- b000143 | prose | pages [5] -->
on the sandcastle.

<!-- b000144 | prose | pages [5] -->
2) Seawater begin to flood the sandcastle. In this case, water content of the

<!-- b000145 | prose | pages [5] -->
infiltrated part will change.

<!-- b000146 | prose | pages [5] -->
3) Seawater completely flood the sandcastle.

<!-- b000147 | prose | pages [5] -->
Taking a beach in Sandy Hook, USA as an example, we query the tide curve of the

<!-- b000148 | prose | pages [5] -->
place on March 6, 2020 [1].

<!-- b000149 | furniture | pages [5] -->


<!-- b000150 | caption | pages [5] -->
Figure 2. Tide curve of Sandy Hook on March 6, 2020

<!-- b000151 | furniture | pages [5] -->


<!-- b000152 | furniture | pages [5] -->


<!-- b000153 | prose | pages [5] -->
As can be seen from the figure above, the initial height of the tide at 00:00 is 30cm,

<!-- b000154 | prose | pages [5] -->
and the relationship between tide height and time is:

<!-- b000155 | prose | pages [5] -->
= +

<!-- b000156 | furniture | pages [5] -->


<!-- b000157 | prose | pages [5] -->
+ − （1） 3.074) h t ( ) 1256sin(0.0008776 t

<!-- b000158 | prose | pages [5] -->
Where

<!-- b000159 | prose | pages [5] -->
70.98sin(0.4971 t 0.8185)

<!-- b000160 | prose | pages [5] -->
h t is the height of tide relative to the tidal height datum plane. t is time(h);

<!-- b000161 | prose | pages [5] -->
( )

<!-- b000162 | prose | pages [5] -->
To study the force of waves on the sandcastle, we need to know how waves move.

<!-- b000163 | prose | pages [5] -->
Airy wave theory [2] is often applied in ocean engineering and coastal engineering for

<!-- b000164 | prose | pages [5] -->
the modelling of random sea states. Airy wave theory is a linear theory for the

<!-- b000165 | prose | pages [5] -->
propagation of waves on the surface of a potential flow and above a horizontal bottom.

<!-- b000166 | prose | pages [5] -->
关注数学模型

<!-- b000167 | furniture | pages [5] -->
2

<!-- b000168 | furniture | pages [5] -->
MATHmodels

<!-- b000169 | furniture | pages [5] -->
获取更多资讯

<!-- b000170 | furniture | pages [6] -->
Team #2011873                                                                 Page 5 of 22

<!-- b000171 | prose | pages [6] -->
The free surface elevation (x,t) of one wave component is sinusoidal, as a function of

<!-- b000172 | prose | pages [6] -->
horizontal position x and time t.

<!-- b000173 | prose | pages [6] -->
( )  =

<!-- b000174 | furniture | pages [6] -->


<!-- b000175 | prose | pages [6] -->
x t ,

<!-- b000176 | prose | pages [6] -->
Where

<!-- b000177 | prose | pages [6] -->
  − 

<!-- b000178 | furniture | pages [6] -->


<!-- b000179 | prose | pages [6] -->
（2） a a cos( kx t )

<!-- b000180 | prose | pages [6] -->
a is the wave amplitude in meter, here, we take a = 0.15m [3]. k is the angular

<!-- b000181 | prose | pages [6] -->
 2 = wavenumber in radian per meter, related to the wavelength  as k , here, we 

<!-- b000182 | prose | pages [6] -->
assume  = 8.5m. is the angular frequency in radian per second, related to the period

<!-- b000183 | prose | pages [6] -->


<!-- b000184 | prose | pages [6] -->
2

<!-- b000185 | prose | pages [6] -->
=

<!-- b000186 | prose | pages [6] -->
T and frequency f by

<!-- b000187 | prose | pages [6] -->
, here, we assume T = 10s.

<!-- b000188 | prose | pages [6] -->
T

<!-- b000189 | prose | pages [6] -->
Then, we can get the speed (m/s) and acceleration (m/s2) of the waves.

<!-- b000190 | prose | pages [6] -->
  = = u

<!-- b000191 | furniture | pages [6] -->


<!-- b000192 | prose | pages [6] -->
 t

<!-- b000193 | prose | pages [6] -->
 u = = − u

<!-- b000194 | furniture | pages [6] -->


<!-- b000195 | prose | pages [6] -->
 t

<!-- b000196 | prose | pages [6] -->
 −  a a sin( kx t )

<!-- b000197 | furniture | pages [6] -->


<!-- b000198 | prose | pages [6] -->
（3）

<!-- b000199 | prose | pages [6] -->
2 cos(  −  a a kx t )

<!-- b000200 | furniture | pages [6] -->


<!-- b000201 | prose | pages [6] -->
（4）

<!-- b000202 | prose | pages [6] -->
Knowing the equation of motion of the wave, we further explore the total inline

<!-- b000203 | prose | pages [6] -->
force on the wave. The Morison Equation [4] is the sum of two force components: an

<!-- b000204 | prose | pages [6] -->
inertia force in phase with the local flow acceleration and a drag force proportional to

<!-- b000205 | prose | pages [6] -->
the square of the instantaneous flow velocity.

<!-- b000206 | prose | pages [6] -->
=  F C Vu

<!-- b000207 | furniture | pages [6] -->


<!-- b000208 | prose | pages [6] -->
m

<!-- b000209 | prose | pages [6] -->
Where

<!-- b000210 | prose | pages [6] -->
F is the total inline force on the wave;

<!-- b000211 | prose | pages [6] -->
1 +  C Au u

<!-- b000212 | furniture | pages [6] -->


<!-- b000213 | prose | pages [6] -->
（5） d 2

<!-- b000214 | prose | pages [6] -->
C is the inertia coefficient, here, we take m

<!-- b000215 | prose | pages [6] -->
C =1.5; V is the volume of sandcastle; is the density of seawater, =1.03g/cm3; m

<!-- b000216 | prose | pages [6] -->
C is the drag coefficient, which is related to the shape of the material. A is the area of d

<!-- b000217 | prose | pages [6] -->
the surface facing the sea water.

<!-- b000218 | prose | pages [6] -->
关注数学模型

<!-- b000219 | furniture | pages [6] -->
2

<!-- b000220 | furniture | pages [6] -->
MATHmodels

<!-- b000221 | furniture | pages [6] -->
获取更多资讯

<!-- b000222 | furniture | pages [7] -->
Team #2011873                                                                 Page 6 of 22

<!-- b000223 | furniture | pages [7] -->


<!-- b000224 | caption | pages [7] -->
Figure 3. Drag coefficient of different shapes

<!-- b000225 | furniture | pages [7] -->


<!-- b000226 | furniture | pages [7] -->


<!-- b000227 | prose | pages [7] -->
In order to discuss the effect of waves on the structure of the sandcastle, we consult

<!-- b000228 | prose | pages [7] -->
relevant data and select the internal friction angle of the sandcastle as the research

<!-- b000229 | prose | pages [7] -->
object.

<!-- b000230 | prose | pages [7] -->
Mohr-Coulomb Yielding Criteria [6] is short for C-M Criteria. The C-M criteria is a

<!-- b000231 | prose | pages [7] -->
yield theory that takes into account the maximum or single shear stress acting on normal

<!-- b000232 | prose | pages [7] -->
or average stress, that is, when the ratio of shear stress to normal stress on the shear

<!-- b000233 | prose | pages [7] -->
plane reaches the maximum, the material yields to failure. Its expression is:

<!-- b000234 | prose | pages [7] -->
 = C

<!-- b000235 | furniture | pages [7] -->


<!-- b000236 | prose | pages [7] -->
n +   tan

<!-- b000237 | furniture | pages [7] -->


<!-- b000238 | prose | pages [7] -->
（6） n

<!-- b000239 | prose | pages [7] -->
F

<!-- b000240 | prose | pages [7] -->
=

<!-- b000241 | furniture | pages [7] -->


<!-- b000242 | furniture | pages [7] -->


<!-- b000243 | prose | pages [7] -->
（7）

<!-- b000244 | prose | pages [7] -->
n n

<!-- b000245 | prose | pages [7] -->
S

<!-- b000246 | prose | pages [7] -->
F

<!-- b000247 | prose | pages [7] -->
=

<!-- b000248 | furniture | pages [7] -->


<!-- b000249 | prose | pages [7] -->
Where

<!-- b000250 | furniture | pages [7] -->


<!-- b000251 | prose | pages [7] -->
（8）

<!-- b000252 | prose | pages [7] -->
n n

<!-- b000253 | prose | pages [7] -->
A

<!-- b000254 | prose | pages [7] -->
 is the normal C is cohesion of sand;  is internal friction angle of sand;

<!-- b000255 | prose | pages [7] -->
n

<!-- b000256 | prose | pages [7] -->
 is the shear stress on the cross section; A is the area of stress on the cross section;

<!-- b000257 | prose | pages [7] -->
n

<!-- b000258 | prose | pages [7] -->
shear plane; S is the area of the force contact surface.

<!-- b000259 | prose | pages [7] -->
To sand, C =0 [7], therefore:

<!-- b000260 | prose | pages [7] -->
关注数学模型

<!-- b000261 | furniture | pages [7] -->
2

<!-- b000262 | furniture | pages [7] -->
MATHmodels

<!-- b000263 | furniture | pages [7] -->
获取更多资讯

<!-- b000264 | furniture | pages [8] -->
Team #2011873                                                                 Page 7 of 22

<!-- b000265 | prose | pages [8] -->
 =

<!-- b000266 | furniture | pages [8] -->


<!-- b000267 | prose | pages [8] -->
n

<!-- b000268 | prose | pages [8] -->


<!-- b000269 | prose | pages [8] -->
=

<!-- b000270 | furniture | pages [8] -->


<!-- b000271 | prose | pages [8] -->
  tan

<!-- b000272 | furniture | pages [8] -->


<!-- b000273 | prose | pages [8] -->
（9） n

<!-- b000274 | prose | pages [8] -->


<!-- b000275 | prose | pages [8] -->
−

<!-- b000276 | prose | pages [8] -->
1

<!-- b000277 | furniture | pages [8] -->


<!-- b000278 | prose | pages [8] -->
（10）

<!-- b000279 | prose | pages [8] -->
n tan ( )

<!-- b000280 | prose | pages [8] -->


<!-- b000281 | prose | pages [8] -->
n

<!-- b000282 | prose | pages [8] -->
Experiments show that the water content has a certain effect on the internal friction

<!-- b000283 | furniture | pages [8] -->


<!-- b000284 | prose | pages [8] -->
angle, and different water content corresponds to different internal friction angles.

<!-- b000285 | prose | pages [8] -->
According to the relevant data found [8] [9], we find the relationship between internal

<!-- b000286 | prose | pages [8] -->
friction angle and water content of the sand, the formula is as follows:

<!-- b000287 | prose | pages [8] -->
( )

<!-- b000288 | prose | pages [8] -->
= −

<!-- b000289 | furniture | pages [8] -->


<!-- b000290 | prose | pages [8] -->
g w 140

<!-- b000291 | prose | pages [8] -->
Where, w is water content in sand.

<!-- b000292 | furniture | pages [8] -->


<!-- b000293 | prose | pages [8] -->
+ + 2

<!-- b000294 | furniture | pages [8] -->


<!-- b000295 | prose | pages [8] -->
（11） w 56 w 28.5

<!-- b000296 | furniture | pages [8] -->


<!-- b000297 | caption | pages [8] -->
Figure 4. Curve of internal friction angle and water content

<!-- b000298 | furniture | pages [8] -->


<!-- b000299 | furniture | pages [8] -->


<!-- b000300 | prose | pages [8] -->
From the figure we can see that, as the water content increases, the internal friction

<!-- b000301 | prose | pages [8] -->
angle increases first and then decreases. The main reason is that sand particles exhibit

<!-- b000302 | prose | pages [8] -->
cohesiveness under a certain water content. To make the sand slide relative to each other,

<!-- b000303 | prose | pages [8] -->
it must overcome not only the friction between sand, but also the cohesion between

<!-- b000304 | prose | pages [8] -->
sand. Beyond a certain water content, all the sand particles are infiltrated in the water,

<!-- b000305 | prose | pages [8] -->
and the lubricating effect of water reduces the friction between the particles.

<!-- b000306 | prose | pages [8] -->
( )   g w

<!-- b000307 | furniture | pages [8] -->


<!-- b000308 | prose | pages [8] -->
Therefore, we assume that, when , that is, when the internal friction

<!-- b000309 | prose | pages [8] -->
angle of the external force acting on the sandcastle is greater than the value of the

<!-- b000310 | prose | pages [8] -->
maximum internal friction angle that can be stabilized at the water content of the sand,

<!-- b000311 | prose | pages [8] -->
( ) g w the sandcastle will collapse; when    , The sandcastle will not collapse.

<!-- b000312 | prose | pages [8] -->
关注数学模型

<!-- b000313 | furniture | pages [8] -->
2

<!-- b000314 | furniture | pages [8] -->
MATHmodels

<!-- b000315 | furniture | pages [8] -->
获取更多资讯

<!-- b000316 | furniture | pages [9] -->
Team #2011873                                                                 Page 8 of 22

<!-- b000317 | prose | pages [9] -->
When seawater begins to submerge the sandcastle, in order to learn how the water

<!-- b000318 | prose | pages [9] -->
content of the sandcastle changes, we must first know the infiltration rate of waves.

<!-- b000319 | prose | pages [9] -->
Horton’s equation is an empirical formula for calculating the infiltration curve, and

<!-- b000320 | prose | pages [9] -->
its expression is [10]:

<!-- b000321 | prose | pages [9] -->
( ) = f t f

<!-- b000322 | furniture | pages [9] -->


<!-- b000323 | prose | pages [9] -->
Where

<!-- b000324 | prose | pages [9] -->
( ) f t is the infiltration rate at time t;

<!-- b000325 | prose | pages [9] -->
f e− + + − kt ( f )

<!-- b000326 | furniture | pages [9] -->


<!-- b000327 | prose | pages [9] -->
（12） c c 0 c

<!-- b000328 | prose | pages [9] -->
0f is the initial infiltration rate, take f 0=0 ;

<!-- b000329 | prose | pages [9] -->
cf  is the constant infiltration rate after the roil has been saturated or minimum

<!-- b000330 | prose | pages [9] -->
mm/min; k is the decay constant specific to the cf =1 infiltration rate, here, we assume

<!-- b000331 | prose | pages [9] -->
[12]. k =2 sand, take

<!-- b000332 | prose | pages [9] -->
We already know the infiltration rate at time t, and what is the relationship between

<!-- b000333 | prose | pages [9] -->
( ) f t and water content of the sandcastle? Here, we use Van Genuchten Model.

<!-- b000334 | prose | pages [9] -->
The shape of water retention curves can be characterized by several models, one of

<!-- b000335 | prose | pages [9] -->
them as the Van Genuchten Model [12] [13].

<!-- b000336 | prose | pages [9] -->
( )

<!-- b000337 | prose | pages [9] -->


<!-- b000338 | prose | pages [9] -->
=

<!-- b000339 | prose | pages [9] -->


<!-- b000340 | prose | pages [9] -->
+

<!-- b000341 | furniture | pages [9] -->


<!-- b000342 | prose | pages [9] -->
r

<!-- b000343 | prose | pages [9] -->
Where

<!-- b000344 | prose | pages [9] -->
( )

<!-- b000345 | prose | pages [9] -->


<!-- b000346 | prose | pages [9] -->
−

<!-- b000347 | prose | pages [9] -->


<!-- b000348 | prose | pages [9] -->
s r

<!-- b000349 | furniture | pages [9] -->


<!-- b000350 | prose | pages [9] -->
（13）

<!-- b000351 | prose | pages [9] -->
1

<!-- b000352 | prose | pages [9] -->
−

<!-- b000353 | prose | pages [9] -->
1

<!-- b000354 | prose | pages [9] -->
  

<!-- b000355 | prose | pages [9] -->
n

<!-- b000356 | prose | pages [9] -->
+

<!-- b000357 | prose | pages [9] -->


<!-- b000358 | prose | pages [9] -->
n

<!-- b000359 | prose | pages [9] -->
1 ( )

<!-- b000360 | prose | pages [9] -->
  

<!-- b000361 | prose | pages [9] -->
 is the water retention curve;  is cm of water;

<!-- b000362 | prose | pages [9] -->
s  is saturated water

<!-- b000363 | prose | pages [9] -->
[14];  is r  is residual water content, take s [14]; =0.3 content, take r =0.05

<!-- b000364 | prose | pages [9] -->
  cm-1 [14]; n is a 0 =0.01 related to the inverse of the air entry suction, , take

<!-- b000365 | prose | pages [9] -->
n , take measure of the pore-size distribution,

<!-- b000366 | prose | pages [9] -->
( ) Note that  and

<!-- b000367 | prose | pages [9] -->
1 1 n =3 .

<!-- b000368 | prose | pages [9] -->
f t have the same physical meaning, so we take equation (12)

<!-- b000369 | prose | pages [9] -->
into (13) to get the water retention curve.

<!-- b000370 | prose | pages [9] -->
关注数学模型

<!-- b000371 | furniture | pages [9] -->
2

<!-- b000372 | furniture | pages [9] -->
MATHmodels

<!-- b000373 | furniture | pages [9] -->
获取更多资讯

<!-- b000374 | furniture | pages [10] -->
Team #2011873                                                                 Page 9 of 22

<!-- b000375 | furniture | pages [10] -->


<!-- b000376 | caption | pages [10] -->
Figure 5. Curve of water retention

<!-- b000377 | furniture | pages [10] -->


<!-- b000378 | prose | pages [10] -->
Then use formula (11) to calculate the internal friction angle of the submerged part

<!-- b000379 | prose | pages [10] -->
and compare it with .

<!-- b000380 | prose | pages [10] -->
Assume that the size of the cuboid is 0.4m0.3m0.3m, where the height is 0.3m.

<!-- b000381 | furniture | pages [10] -->


<!-- b000382 | prose | pages [10] -->
Considering that the larger the area, the greater the force, so we choose the surface with

<!-- b000383 | prose | pages [10] -->
size 0.3m0.3m as water-side face. Then, the area of shear plane A=0.4m0.3m, the

<!-- b000384 | prose | pages [10] -->
area of the force contact surface S=0.3m0.3m.

<!-- b000385 | prose | pages [10] -->
According to Figure 2, initial height of the tide is 30cm, and a = 0.15m( formula

<!-- b000386 | prose | pages [10] -->
(2)), we place the sandcastle at 45cm relative to the tidal height datum plane, which is

<!-- b000387 | prose | pages [10] -->
the maximum height of the tide.

<!-- b000388 | prose | pages [10] -->
Then, it can be obtained from Figure 2 that the time taken for the tide to rise from

<!-- b000389 | prose | pages [10] -->
the initial value to the location of the sandcastle is 40 minutes, which is the first stage

<!-- b000390 | prose | pages [10] -->
in our model. It takes 50 minutes for the tide to continue rising to just completely

<!-- b000391 | prose | pages [10] -->
submerge the sandcastle, which is the second stage.

<!-- b000392 | prose | pages [10] -->
Assume that the initial moisture content of the sandcastle is 20%. The internal

<!-- b000393 | prose | pages [10] -->
( ) g w under this water content can be obtained from friction angle of the sandcastle

<!-- b000394 | caption | pages [10] -->
Figure 4.

<!-- b000395 | prose | pages [10] -->
关注数学模型

<!-- b000396 | furniture | pages [10] -->
2

<!-- b000397 | furniture | pages [10] -->
MATHmodels

<!-- b000398 | furniture | pages [10] -->
获取更多资讯

<!-- b000399 | furniture | pages [11] -->
Team #2011873                                                                 Page 10 of 22

<!-- b000400 | prose | pages [11] -->
In the first stage, it is calculated that the internal friction angle generated by wave

<!-- b000401 | prose | pages [11] -->
( )  is smaller than g w , that is, the cuboid model can exist stably in the first stage.

<!-- b000402 | prose | pages [11] -->
In the second stage, as the seawater began to submerge the sandcastle, the water

<!-- b000403 | prose | pages [11] -->
content of the sandcastle gradually increased with time. From Figure 4, it can be seen

<!-- b000404 | prose | pages [11] -->
that the internal friction angle continue to decrease. When it decrease to less than the

<!-- b000405 | prose | pages [11] -->
internal friction angle generated by wave, the sandcastle will collapse. The specific

<!-- b000406 | prose | pages [11] -->
change process is shown in the following figure.

<!-- b000407 | furniture | pages [11] -->


<!-- b000408 | caption | pages [11] -->
Figure 6. Curve of internal friction angle changing with time

<!-- b000409 | furniture | pages [11] -->


<!-- b000410 | prose | pages [11] -->
It can be seen from the figure above that the lasting time of the cuboid sandcastle

<!-- b000411 | prose | pages [11] -->
in the second stage is 10 minutes, that is, the total lasting time is about 50 minutes.

<!-- b000412 | prose | pages [11] -->
When analyzing the stability of the other five geometries, the method is similar.

<!-- b000413 | prose | pages [11] -->
Due to space limitations, it will not be described again.

<!-- b000414 | prose | pages [11] -->
We obtain the lasting time of the six geometries with the same volume and height,

<!-- b000415 | prose | pages [11] -->
and the effective height of the first wave action. The specific results are shown in the

<!-- b000416 | prose | pages [11] -->
following table.

<!-- b000417 | furniture | pages [11] -->


<!-- b000418 | furniture | pages [11] -->


<!-- b000419 | furniture | pages [11] -->


<!-- b000420 | furniture | pages [11] -->


<!-- b000421 | prose | pages [11] -->
关注数学模型

<!-- b000422 | furniture | pages [11] -->
2

<!-- b000423 | furniture | pages [11] -->
MATHmodels

<!-- b000424 | furniture | pages [11] -->
获取更多资讯

<!-- b000425 | furniture | pages [12] -->
Team #2011873                                                                 Page 11 of 22

<!-- b000426 | caption | pages [12] -->
Table 1. Lasting time and effective wave height in the first stage of six geometries

<!-- b000427 | prose | pages [12] -->
Effective wave height in Lasting time（min） Geometric shapes

<!-- b000428 | prose | pages [12] -->
the first stage（m）

<!-- b000429 | prose | pages [12] -->
about 50min Cuboid >0.2

<!-- b000430 | prose | pages [12] -->
Less than 40min Cylinder

<!-- b000431 | prose | pages [12] -->
Equilateral triangular

<!-- b000432 | prose | pages [12] -->
<0.18

<!-- b000433 | prose | pages [12] -->
Less than 40min cylinder <0.13

<!-- b000434 | prose | pages [12] -->
Less than 40min Frustum of a cone

<!-- b000435 | prose | pages [12] -->
Three trustum of a

<!-- b000436 | prose | pages [12] -->
<0.10

<!-- b000437 | prose | pages [12] -->
Collapse in a short time pyramid

<!-- b000438 | prose | pages [12] -->
Four trustum of a

<!-- b000439 | prose | pages [12] -->
<0.17

<!-- b000440 | prose | pages [12] -->
Less than 40min pyramid

<!-- b000441 | furniture | pages [12] -->


<!-- b000442 | prose | pages [12] -->
<0.14

<!-- b000443 | prose | pages [12] -->
As can be seen from the table, except for the cuboid, the other five geometries

<!-- b000444 | prose | pages [12] -->
collapse in the first stage. We know that the higher the wave, the greater the impact

<!-- b000445 | prose | pages [12] -->
force, so a larger value of the effective height of the wave indicates that the geometry

<!-- b000446 | prose | pages [12] -->
is more stable. In summary, the cuboid is an optimal 3D geometric shape.

<!-- b000447 | prose | pages [12] -->
It can be known from equations (7) and (8) that the larger the area of A and S, the

<!-- b000448 | prose | pages [12] -->
smaller the damage to the sandcastle. So next we change the length and width of the

<!-- b000449 | prose | pages [12] -->
cuboid, and further analyze the effect of the size on the stability of the sandcastle.

<!-- b000450 | prose | pages [12] -->
Use formula (10) to calculate the change of the internal friction angle with length-

<!-- b000451 | prose | pages [12] -->
width ratio, and draw the figure.

<!-- b000452 | furniture | pages [12] -->


<!-- b000453 | caption | pages [12] -->
Figure 7. Curve of internal friction angle changing with length-width ratio

<!-- b000454 | prose | pages [12] -->
关注数学模型

<!-- b000455 | furniture | pages [12] -->
2

<!-- b000456 | furniture | pages [12] -->
MATHmodels

<!-- b000457 | furniture | pages [12] -->
获取更多资讯

<!-- b000458 | furniture | pages [13] -->
Team #2011873                                                                 Page 12 of 22

<!-- b000459 | prose | pages [13] -->
From the figure above, we learn that the larger length-width ratio, the smaller the

<!-- b000460 | prose | pages [13] -->
internal friction angle generated by external forces, and the more stable the sandcastle.

<!-- b000461 | prose | pages [13] -->
This is consistent with the actual situation.

<!-- b000462 | furniture | pages [13] -->


<!-- b000463 | prose | pages [13] -->
In Task 1, we set the initial water content to 20% and use the internal friction angle

<!-- b000464 | prose | pages [13] -->
to determine whether the sandcastle structure is stable. The internal friction angle is

<!-- b000465 | prose | pages [13] -->
related to the water content, so it is necessary to find the optimal sand-water ratio to

<!-- b000466 | prose | pages [13] -->
make the sandcastle last longer.

<!-- b000467 | prose | pages [13] -->
First, by changing the initial water content and then the internal friction angle, the

<!-- b000468 | prose | pages [13] -->
( )   g w sandcastle satisfies , and the sand-to-water mixing ratio range that keeps the

<!-- b000469 | prose | pages [13] -->
sandcastle intact in the first stage is 5% -25%. Then, in the second stage, a curve of the

<!-- b000470 | prose | pages [13] -->
sandcastle collapse time changing with the initial water content in the sand is drawn.

<!-- b000471 | furniture | pages [13] -->


<!-- b000472 | caption | pages [13] -->
Figure 8. Curve of the sandcastle collapse time with the initial water content

<!-- b000473 | furniture | pages [13] -->


<!-- b000474 | prose | pages [13] -->
We can see that as the initial water content in the sand increases, the lasting time

<!-- b000475 | prose | pages [13] -->
of the sandcastle gradually decreases. When the initial water content is 5%, the total

<!-- b000476 | prose | pages [13] -->
lasting time of the sandcastle is the longest, which is 67 min.

<!-- b000477 | prose | pages [13] -->
However, in Figure 4, when the water content w = 15%, the internal friction angle

<!-- b000478 | prose | pages [13] -->
is the largest and the sandcastle has the best stability. From the above figure, we get that

<!-- b000479 | prose | pages [13] -->
the total lasting time of the sandcastle under this condition is 64.43min.

<!-- b000480 | prose | pages [13] -->
In fact, there is no contradiction between the two. Because when the initial water

<!-- b000481 | prose | pages [13] -->
关注数学模型

<!-- b000482 | furniture | pages [13] -->
2

<!-- b000483 | furniture | pages [13] -->
MATHmodels

<!-- b000484 | furniture | pages [13] -->
获取更多资讯

<!-- b000485 | furniture | pages [14] -->
Team #2011873                                                                 Page 13 of 22

<!-- b000486 | prose | pages [14] -->
content is small, the starting point of the rise is low, and accordingly the duration of the

<!-- b000487 | prose | pages [14] -->
sandcastle is longer. Considering the viscosity of the sand [15], and the difference

<!-- b000488 | prose | pages [14] -->
between the two is not large, we choose 15% as the best water-to-sand mixing ratio.

<!-- b000489 | furniture | pages [14] -->


<!-- b000490 | prose | pages [14] -->
In order to study the impact of rain on sandcastles, we first need to understand some

<!-- b000491 | prose | pages [14] -->
of the motion characteristics of rain.

<!-- b000492 | prose | pages [14] -->
Suppose the rain drops vertically. The falling raindrops have large kinetic energy.

<!-- b000493 | prose | pages [14] -->
When they hit the sandcastle, they will destroy the structure of the sandcastle and also

<!-- b000494 | prose | pages [14] -->
change the water content of the sandcastle. Therefore, we divide the impact of rainwater

<!-- b000495 | prose | pages [14] -->
on the sandcastle into two parts: scour and infiltration.

<!-- b000496 | prose | pages [14] -->
Raindrop final speed calculation formula [16]:

<!-- b000497 | prose | pages [14] -->


<!-- b000498 | prose | pages [14] -->
2

<!-- b000499 | prose | pages [14] -->
   +

<!-- b000500 | prose | pages [14] -->
38.9 2400

<!-- b000501 | prose | pages [14] -->
  

<!-- b000502 | prose | pages [14] -->
d

<!-- b000503 | prose | pages [14] -->
 = 

<!-- b000504 | furniture | pages [14] -->


<!-- b000505 | prose | pages [14] -->
V

<!-- b000506 | prose | pages [14] -->
m

<!-- b000507 | prose | pages [14] -->


<!-- b000508 | prose | pages [14] -->
d

<!-- b000509 | prose | pages [14] -->
 + 

<!-- b000510 | prose | pages [14] -->
0.113 0.845

<!-- b000511 | prose | pages [14] -->
d

<!-- b000512 | prose | pages [14] -->
 − 

<!-- b000513 | prose | pages [14] -->
gd

<!-- b000514 | prose | pages [14] -->
38.9

<!-- b000515 | prose | pages [14] -->
d

<!-- b000516 | prose | pages [14] -->
3mm

<!-- b000517 | prose | pages [14] -->
d

<!-- b000518 | furniture | pages [14] -->


<!-- b000519 | prose | pages [14] -->
（14）

<!-- b000520 | prose | pages [14] -->
 

<!-- b000521 | prose | pages [14] -->
3

<!-- b000522 | prose | pages [14] -->
d

<!-- b000523 | prose | pages [14] -->
6mm

<!-- b000524 | prose | pages [14] -->
Where   is viscosity coefficient of air movement. When T=20℃=293K, 

<!-- b000525 | prose | pages [14] -->
=1.81074155510-5PaS.

<!-- b000526 | prose | pages [14] -->
= q mV Considering raindrops as spheres. According to the momentum formula

<!-- b000527 | prose | pages [14] -->
1 = 2

<!-- b000528 | prose | pages [14] -->
m

<!-- b000529 | prose | pages [14] -->
, the momentum and energy contained in each raindrop and energy formula E mV m 2

<!-- b000530 | prose | pages [14] -->
can be obtained, and the relationship between raindrop diameter and momentum and

<!-- b000531 | prose | pages [14] -->
energy can be further obtained.

<!-- b000532 | prose | pages [14] -->
However, in the actual calculation of rainfall kinetic energy and other rainfall

<!-- b000533 | prose | pages [14] -->
characteristics, there is often only data of rainfall or rainfall intensity, and observation

<!-- b000534 | prose | pages [14] -->
data of raindrop diameter is lacking. In order to facilitate production applications, the

<!-- b000535 | prose | pages [14] -->
final raindrop speed can be expressed as a function of rain intensity. According to the

<!-- b000536 | prose | pages [14] -->
analysis of measured data, there is a power function relationship between the median

<!-- b000537 | prose | pages [14] -->
diameter of raindrops and the rain intensity [16]:

<!-- b000538 | prose | pages [14] -->
d

<!-- b000539 | furniture | pages [14] -->


<!-- b000540 | prose | pages [14] -->
50 = = 0.32 2.52 i

<!-- b000541 | furniture | pages [14] -->


<!-- b000542 | prose | pages [14] -->
（15）

<!-- b000543 | prose | pages [14] -->
d is median diameter of raindrops(mm); i is rain intensity(mm/min).

<!-- b000544 | furniture | pages [14] -->


<!-- b000545 | prose | pages [14] -->
Where 50

<!-- b000546 | prose | pages [14] -->
By taking equation (15) into (14), we get the formula for calculating the average

<!-- b000547 | prose | pages [14] -->
final speed of raindrops from rainfall intensity.

<!-- b000548 | prose | pages [14] -->
关注数学模型

<!-- b000549 | furniture | pages [14] -->
2

<!-- b000550 | furniture | pages [14] -->
MATHmodels

<!-- b000551 | furniture | pages [14] -->
获取更多资讯

<!-- b000552 | furniture | pages [15] -->
Team #2011873                                                                 Page 14 of 22

<!-- b000553 | prose | pages [15] -->


<!-- b000554 | prose | pages [15] -->
2

<!-- b000555 | prose | pages [15] -->
   +

<!-- b000556 | prose | pages [15] -->
1.544 6.048

<!-- b000557 | prose | pages [15] -->
  

<!-- b000558 | prose | pages [15] -->
0.23

<!-- b000559 | prose | pages [15] -->


<!-- b000560 | prose | pages [15] -->
i

<!-- b000561 | prose | pages [15] -->
= 

<!-- b000562 | prose | pages [15] -->
V

<!-- b000563 | furniture | pages [15] -->


<!-- b000564 | prose | pages [15] -->
m

<!-- b000565 | prose | pages [15] -->


<!-- b000566 | prose | pages [15] -->
0.23

<!-- b000567 | prose | pages [15] -->
i

<!-- b000568 | prose | pages [15] -->
 + 

<!-- b000569 | prose | pages [15] -->
0.23

<!-- b000570 | prose | pages [15] -->
0.0448 0.0845

<!-- b000571 | prose | pages [15] -->
i

<!-- b000572 | prose | pages [15] -->
 − 

<!-- b000573 | prose | pages [15] -->
0.23

<!-- b000574 | prose | pages [15] -->
gi gi

<!-- b000575 | prose | pages [15] -->
1.544

<!-- b000576 | prose | pages [15] -->
i

<!-- b000577 | prose | pages [15] -->
2.13

<!-- b000578 | prose | pages [15] -->
0.23

<!-- b000579 | prose | pages [15] -->
i

<!-- b000580 | prose | pages [15] -->
（16）

<!-- b000581 | prose | pages [15] -->


<!-- b000582 | prose | pages [15] -->
2.13

<!-- b000583 | prose | pages [15] -->
i

<!-- b000584 | prose | pages [15] -->
43.46

<!-- b000585 | prose | pages [15] -->
Through calculation, we get the relationship between precipitation and raindrop

<!-- b000586 | prose | pages [15] -->
speed, energy and momentum, as shown in the following figure:

<!-- b000587 | furniture | pages [15] -->


<!-- b000588 | furniture | pages [15] -->


<!-- b000589 | furniture | pages [15] -->


<!-- b000590 | caption | pages [15] -->
Figure 9. Relationship between precipitation and raindrop speed, energy, momentum

<!-- b000591 | furniture | pages [15] -->


<!-- b000592 | furniture | pages [15] -->


<!-- b000593 | prose | pages [15] -->
After knowing the relevant motion parameters of raindrops, we also need to

<!-- b000594 | prose | pages [15] -->
analyze the impact of raindrops on the sandcastle.

<!-- b000595 | prose | pages [15] -->
The Sartor-Boyd scour model [17] is mainly applicable to the rainfall process with

<!-- b000596 | prose | pages [15] -->
initial scouring effect, as shown in formula (17):

<!-- b000597 | prose | pages [15] -->
dP t =

<!-- b000598 | furniture | pages [15] -->


<!-- b000599 | prose | pages [15] -->
d

<!-- b000600 | furniture | pages [15] -->


<!-- b000601 | prose | pages [15] -->
（17） K Pr 2

<!-- b000602 | prose | pages [15] -->
K is the erosion coefficient (empirical value), mm-1; P is the volume of

<!-- b000603 | furniture | pages [15] -->


<!-- b000604 | prose | pages [15] -->
Where 2

<!-- b000605 | prose | pages [15] -->
sandcastle at the beginning, m3; r is rainwater runoff per unit time per unit area, that is,

<!-- b000606 | prose | pages [15] -->
rainfall intensity, mm / min; t is time, min.

<!-- b000607 | prose | pages [15] -->
K is taken as 0.201 [17] to obtain the change of the volume of sand In our model, 2

<!-- b000608 | prose | pages [15] -->
washed away with precipitation, as shown in the figure below:

<!-- b000609 | prose | pages [15] -->
关注数学模型

<!-- b000610 | furniture | pages [15] -->
2

<!-- b000611 | furniture | pages [15] -->
MATHmodels

<!-- b000612 | furniture | pages [15] -->
获取更多资讯

<!-- b000613 | furniture | pages [16] -->
Team #2011873                                                                 Page 15 of 22

<!-- b000614 | furniture | pages [16] -->


<!-- b000615 | caption | pages [16] -->
Figure 10. Change of the volume of sand washed away with precipitation

<!-- b000616 | furniture | pages [16] -->


<!-- b000617 | furniture | pages [16] -->


<!-- b000618 | caption | pages [16] -->
Figure 11. Flow chart for seepage process

<!-- b000619 | furniture | pages [16] -->


<!-- b000620 | prose | pages [16] -->
When the sandcastle is affected by rain, we use Matlab to fit the relationship

<!-- b000621 | prose | pages [16] -->
between the internal friction angle of the sandcastle and the water content, as follows

<!-- b000622 | prose | pages [16] -->
[18]:

<!-- b000623 | prose | pages [16] -->
关注数学模型

<!-- b000624 | furniture | pages [16] -->
2

<!-- b000625 | furniture | pages [16] -->
MATHmodels

<!-- b000626 | furniture | pages [16] -->
获取更多资讯

<!-- b000627 | furniture | pages [17] -->
Team #2011873                                                                 Page 16 of 22

<!-- b000628 | prose | pages [17] -->
=

<!-- b000629 | furniture | pages [17] -->


<!-- b000630 | prose | pages [17] -->
+

<!-- b000631 | furniture | pages [17] -->


<!-- b000632 | prose | pages [17] -->
（18） 0.8462 w 5.256

<!-- b000633 | furniture | pages [17] -->


<!-- b000634 | caption | pages [17] -->
Figure 12. Relationship between internal friction angle and water content when the

<!-- b000635 | prose | pages [17] -->
sandcastle is affected by rain

<!-- b000636 | furniture | pages [17] -->


<!-- b000637 | furniture | pages [17] -->


<!-- b000638 | prose | pages [17] -->
In precipitation model, we have obtained the formula for calculating the final

<!-- b000639 | prose | pages [17] -->
velocity of raindrops. Then, bring it into equation (13) to get the water content of the

<!-- b000640 | prose | pages [17] -->
sandcastle. According to formula (18), we can get internal friction angle of sandcastle

<!-- b000641 | prose | pages [17] -->
( ) while raining. Finally, compare the relationship between and

<!-- b000642 | prose | pages [17] -->
conclusion.

<!-- b000643 | prose | pages [17] -->
g w , and draw the

<!-- b000644 | caption | pages [17] -->
Table 2. Effective height of the six geometries when it rains

<!-- b000645 | prose | pages [17] -->
Geometric shapes Cuboid Cylinder Equilateral triangular

<!-- b000646 | prose | pages [17] -->
cylinder

<!-- b000647 | prose | pages [17] -->
Frustum of a cone Three trustum of a

<!-- b000648 | prose | pages [17] -->
pyramid

<!-- b000649 | prose | pages [17] -->
Four trustum of a

<!-- b000650 | prose | pages [17] -->
pyramid

<!-- b000651 | furniture | pages [17] -->


<!-- b000652 | prose | pages [17] -->
Effective height 0.20m 0.15m

<!-- b000653 | prose | pages [17] -->
0.11m

<!-- b000654 | prose | pages [17] -->
0.08m

<!-- b000655 | prose | pages [17] -->
0.15m

<!-- b000656 | prose | pages [17] -->
0.15m

<!-- b000657 | prose | pages [17] -->
The results show that rainwater has a certain effect on the structural stability of

<!-- b000658 | prose | pages [17] -->
sand castles. Comparing the effective heights of the six geometries, we find that the

<!-- b000659 | prose | pages [17] -->
cuboid is still the optimal geometry, confirming the reliability of our model.

<!-- b000660 | prose | pages [17] -->
关注数学模型

<!-- b000661 | furniture | pages [17] -->
2

<!-- b000662 | furniture | pages [17] -->
MATHmodels

<!-- b000663 | furniture | pages [17] -->
获取更多资讯

<!-- b000664 | furniture | pages [18] -->
Team #2011873                                                                 Page 17 of 22

<!-- b000665 | prose | pages [18] -->
After theoretical calculations, ANSYS simulation analysis is used to verify the

<!-- b000666 | prose | pages [18] -->
theoretical results. Through the simulation analysis of the rainfall scouring model, we

<!-- b000667 | prose | pages [18] -->
get the pressure, tension and deformation maps of the model. By comparing with the

<!-- b000668 | prose | pages [18] -->
theoretical results, the results are very similar. The following figure shows the

<!-- b000669 | prose | pages [18] -->
simulation analysis of six models:

<!-- b000670 | furniture | pages [18] -->


<!-- b000671 | furniture | pages [18] -->


<!-- b000672 | furniture | pages [18] -->


<!-- b000673 | caption | pages [18] -->
Figure 13. The pressure, tension and deformation cloud of the cuboid

<!-- b000674 | furniture | pages [18] -->


<!-- b000675 | furniture | pages [18] -->


<!-- b000676 | furniture | pages [18] -->


<!-- b000677 | furniture | pages [18] -->


<!-- b000678 | furniture | pages [18] -->


<!-- b000679 | furniture | pages [18] -->


<!-- b000680 | furniture | pages [18] -->


<!-- b000681 | caption | pages [18] -->
Figure 14. Pressure distribution of the other five models

<!-- b000682 | furniture | pages [18] -->


<!-- b000683 | furniture | pages [18] -->


<!-- b000684 | prose | pages [18] -->
：

<!-- b000685 | prose | pages [18] -->
From the analysis of the first three questions, in order to extend the lasting time of

<!-- b000686 | prose | pages [18] -->
the sandcastle, we can consider two aspects: reducing seawater infiltration and reducing

<!-- b000687 | prose | pages [18] -->
wave erosion.

<!-- b000688 | prose | pages [18] -->
On the one hand, we can cover the sandcastle, for example, placing a shield in front

<!-- b000689 | prose | pages [18] -->
关注数学模型

<!-- b000690 | furniture | pages [18] -->
2

<!-- b000691 | furniture | pages [18] -->
MATHmodels

<!-- b000692 | furniture | pages [18] -->
获取更多资讯

<!-- b000693 | furniture | pages [19] -->
Team #2011873                                                                 Page 18 of 22

<!-- b000694 | prose | pages [19] -->
of the sandcastle to reduce the impact of the waves on the sandcastle. Another example

<!-- b000695 | prose | pages [19] -->
is to use a plastic bag to wrap the sandcastle. This can eliminate the infiltration of

<!-- b000696 | prose | pages [19] -->
rainwater and seawater, also avoid contact with the waves, thereby reducing the erosion

<!-- b000697 | prose | pages [19] -->
of the waves.

<!-- b000698 | prose | pages [19] -->
On the other hand, we can also place some stone or wooden supports in the

<!-- b000699 | prose | pages [19] -->
sandcastle, which can improve the sandcastle's ability to resist the waves. Alternatively,

<!-- b000700 | prose | pages [19] -->
we can also mix some clay into the sand. Because clay absorbs water less than sand,

<!-- b000701 | prose | pages [19] -->
and its internal friction angle is greater than sand. Therefore, adding other materials into

<!-- b000702 | prose | pages [19] -->
the sandcastle can improve the ability to resist sea waves and reduce the penetration of

<!-- b000703 | prose | pages [19] -->
waves.

<!-- b000704 | furniture | pages [19] -->


<!-- b000705 | prose | pages [19] -->
⚫ We select six types of 3-dimensional geometric shape for analysis and comparison,

<!-- b000706 | prose | pages [19] -->
and finally determine that the cuboid is the optimal model by calculating the lasting

<!-- b000707 | prose | pages [19] -->
time of the sandcastle and the effective height of the wave action, which has a

<!-- b000708 | prose | pages [19] -->
certain rationality.

<!-- b000709 | prose | pages [19] -->
⚫ When analyzing the effect of the waves on the sandcastle, we establish a wave force

<!-- b000710 | prose | pages [19] -->
equation and perform a strong check using the Mohr-Coulomb Yielding Criteria

<!-- b000711 | prose | pages [19] -->
⚫ By consulting the data, Horton’s equation is used to measure the infiltration rate,

<!-- b000712 | prose | pages [19] -->
and the Van Genuchen Model is used to establish the relationship between the

<!-- b000713 | prose | pages [19] -->
infiltration rate and water content in sand.

<!-- b000714 | prose | pages [19] -->
⚫ The structure of the entire model is rigorous and reasonable. It is suitable for the

<!-- b000715 | prose | pages [19] -->
problem conditions and can be applied to beaches in any area. It has good

<!-- b000716 | prose | pages [19] -->
universality.

<!-- b000717 | prose | pages [19] -->
⚫ When considering wave motion, Airy Wave Theory simply considers the wave as

<!-- b000718 | prose | pages [19] -->
a sinusoidal form, but in fact, the amplitude of the wave is not constant as it moves

<!-- b000719 | prose | pages [19] -->
forward.

<!-- b000720 | prose | pages [19] -->
⚫ Water seepage is not a uniform process. The water content on the surface of an

<!-- b000721 | prose | pages [19] -->
object should be greater than the water content inside the object, but for the sake

<!-- b000722 | prose | pages [19] -->
of calculation, we consider this a uniform process.

<!-- b000723 | prose | pages [19] -->
⚫ Raindrops are uneven when falling and with the change of the tilt angle, it is

<!-- b000724 | prose | pages [19] -->
difficult to deduce its effect on the sandcastle by formula.

<!-- b000725 | prose | pages [19] -->
关注数学模型

<!-- b000726 | furniture | pages [19] -->
2

<!-- b000727 | furniture | pages [19] -->
MATHmodels

<!-- b000728 | furniture | pages [19] -->
获取更多资讯

<!-- b000729 | furniture | pages [20] -->
Team #2011873                                                                 Page 19 of 22

<!-- b000730 | prose | pages [20] -->
The Longest Lasting Sandcastle

<!-- b000731 | prose | pages [20] -->
The sea has infinite appeal to people. When you play on the coast, have you noticed

<!-- b000732 | prose | pages [20] -->
the countless sandcastles of different sizes and shapes on the beach? Some are broken

<!-- b000733 | prose | pages [20] -->
by the wash of the waves, while others remain intact. It is true that they may not be built

<!-- b000734 | prose | pages [20] -->
in time, but have you thought of any other factors that have caused this result and how

<!-- b000735 | prose | pages [20] -->
this will guide us in the construction of sandcastles?

<!-- b000736 | prose | pages [20] -->
In order to answer this question, we take Sandy Hooke in the United States as an

<!-- b000737 | prose | pages [20] -->
example to build a model of a sandcastle under the impact of waves and tide. Based on

<!-- b000738 | prose | pages [20] -->
this model, we studied sandcastles of six basic geometries of the same volume-cuboids,

<!-- b000739 | prose | pages [20] -->
cylinders, triangular prisms, triangular pyramids, quadrangular pyramids, and circular

<!-- b000740 | prose | pages [20] -->
pyramids.

<!-- b000741 | prose | pages [20] -->
We can see that the cuboid sandcastle can exist for the longest time. At the same

<!-- b000742 | prose | pages [20] -->
time, we should keep the width of the water front as small as possible while maintaining

<!-- b000743 | prose | pages [20] -->
a certain cross-section of the sandcastle. This will make the sandcastle exist longer.

<!-- b000744 | prose | pages [20] -->
In addition, we also considered that as the tide rises, the seawater will gradually

<!-- b000745 | prose | pages [20] -->
flood the sandcastle, causing the water content of the sandcastle to change, which will

<!-- b000746 | prose | pages [20] -->
affect the age of the sandcastle. Therefore, we studied the relationship between the

<!-- b000747 | prose | pages [20] -->
water content in the sandcastle and its age. We have reached the conclusion that the

<!-- b000748 | prose | pages [20] -->
optimal moisture content of the sandcastle should be 15%. When the water content is

<!-- b000749 | prose | pages [20] -->
too large, the sand castle will collapse under the impact of the waves. In fact, we will

<!-- b000750 | prose | pages [20] -->
not measure the specific value of sand moisture content during the construction of the

<!-- b000751 | prose | pages [20] -->
sand castle. Therefore, we can do a small experiment at the beach. we gradually add

<!-- b000752 | prose | pages [20] -->
water to the sand, and then see how tight they are. When we feel that the sand is the

<!-- b000753 | prose | pages [20] -->
strongest, stop adding water and use this as the material for building the sandcastle.

<!-- b000754 | prose | pages [20] -->
Finally, we studied the impact of rain on the sandcastle. On the one hand, the

<!-- b000755 | prose | pages [20] -->
infiltration of rainwater will increase the water content of the sandcastle. On the other

<!-- b000756 | prose | pages [20] -->
hand, rainwater on the sandcastle will have a strong effect on it. These will accelerate

<!-- b000757 | prose | pages [20] -->
the collapse of the sand castle so rain is not good for sand castles.

<!-- b000758 | prose | pages [20] -->
In short, in order to make the sandcastle have the longest lasting, we should choose

<!-- b000759 | prose | pages [20] -->
to use sand with a higher degree of tightness in rainless weather, build a cuboid as the

<!-- b000760 | prose | pages [20] -->
foundation of the sand castle, and make the width of the water front as narrow as

<!-- b000761 | prose | pages [20] -->
possible, so that we can build a "perfect" sandcastle. Of course, some people may say

<!-- b000762 | prose | pages [20] -->
that we can wrap a sandcastle with a plastic sheet, or add stones and soil to the sand.

<!-- b000763 | prose | pages [20] -->
关注数学模型

<!-- b000764 | furniture | pages [20] -->
2

<!-- b000765 | furniture | pages [20] -->
MATHmodels

<!-- b000766 | furniture | pages [20] -->
获取更多资讯

<!-- b000767 | furniture | pages [21] -->
Team #2011873                                                                 Page 20 of 22

<!-- b000768 | prose | pages [21] -->
These can also make the sandcastle exist longer. However, we do not recommend doing

<!-- b000769 | prose | pages [21] -->
this. After people leave, if these materials are not taken away in time, they will become

<!-- b000770 | prose | pages [21] -->
rubbish and pollute the sea. At the same time, stones on the beach will leave danger to

<!-- b000771 | prose | pages [21] -->
people who don't pay attention. When we enjoy life at the beach, we must remember to

<!-- b000772 | prose | pages [21] -->
protect the environment and others.

<!-- b000773 | furniture | pages [21] -->


<!-- b000774 | furniture | pages [21] -->


<!-- b000775 | prose | pages [21] -->
关注数学模型

<!-- b000776 | furniture | pages [21] -->
2

<!-- b000777 | furniture | pages [21] -->
MATHmodels

<!-- b000778 | furniture | pages [21] -->
获取更多资讯

<!-- b000779 | furniture | pages [22] -->
Team #2011873                                                                 Page 21 of 22

<!-- b000780 | prose | pages [22] -->
[1]  https://www.cnss.com.cn/tide/

<!-- b000781 | prose | pages [22] -->
[2]  https://en.wikipedia.org/wiki/Airy_wave_theory

<!-- b000782 | prose | pages [22] -->
[3]  https://en.wikipedia.org/wiki/Wind_wave

<!-- b000783 | prose | pages [22] -->
[4]  https://en.wikipedia.org/wiki/Morison_equatio

<!-- b000784 | prose | pages [22] -->
[5]  Zhang Boping, Wang Li, Yuan Haizhi. Quantitative analysis of the effect of water

<!-- b000785 | prose | pages [22] -->
content on the structural strength of loess [J]. Journal of Northwest Agricultural

<!-- b000786 | prose | pages [22] -->
University, 1994 (01): 54-60.

<!-- b000787 | prose | pages [22] -->
[6]  https://en.wikipedia.org/wiki/Mohr%E2%80%93Coulomb_theory?wprov=sfla1

<!-- b000788 | prose | pages [22] -->
[7]  https://wenku.baidu.com/view/4eb7356cbed5b9f3f80f1c1c.html

<!-- b000789 | prose | pages [22] -->
[8]  Chen Lei, Zhao Jian. Effect of moisture content on shear strength parameters of

<!-- b000790 | prose | pages [22] -->
clay in dumping ground [J]. Coal Technology, 2016, 35 (12): 170-172.

<!-- b000791 | prose | pages [22] -->
[9]  Fan Zhijie, Qu Jianjun, Zhou Huan. The relationship between the friction angle

<!-- b000792 | prose | pages [22] -->
in sand and the particle size, water content and natural slope angle [J] .China Desert,

<!-- b000793 | prose | pages [22] -->
2015,35 (02): 301-305.

<!-- b000794 | prose | pages [22] -->
[10] https://en.wikipedia.org/wiki/Infiltration_(hydrology)

<!-- b000795 | prose | pages [22] -->
[11] http://www.soilmanagementindia.com/soil/permeability-of-

<!-- b000796 | prose | pages [22] -->
soils/permeability-of-soil-definition-darcys-law-and-tests-soil-engineering/16472

<!-- b000797 | prose | pages [22] -->
[12] Young-Suk Song, Kyeong-Su Kim, Sueng-Won Jeong, and Choon-Oh Lee.

<!-- b000798 | prose | pages [22] -->
Estimation on unsaturated characteristic curves of tailings obtained from waste

<!-- b000799 | prose | pages [22] -->
dump of imgi mine in busan.Journal of the Korean Geotechnical Society, 30:47–

<!-- b000800 | prose | pages [22] -->
58, 03 2014.

<!-- b000801 | prose | pages [22] -->
[13] https://en.wikipedia.org/wiki/Water_retention_curve

<!-- b000802 | prose | pages [22] -->
[14] Stingaciu, L. R., et al. "Determination of pore size distribution and hydraulic

<!-- b000803 | prose | pages [22] -->
properties using nuclear magnetic resonance relaxometry: A comparative study of

<!-- b000804 | prose | pages [22] -->
laboratory methods." Water Resources Research 46.11 (2010).

<!-- b000805 | prose | pages [22] -->
[15] Zhang Junhong, Shi Xuchao, Zhang Xinjuan. Experimental Study on the

<!-- b000806 | prose | pages [22] -->
Influence of Water Content of Loess on Structure [J]. Henan Science, 2010, 28 (12):

<!-- b000807 | prose | pages [22] -->
1575-1578.

<!-- b000808 | prose | pages [22] -->
[16] Yao Wenyi, Chen Guoxiang.Rainfall Drop Speed and Final Speed Formula

<!-- b000809 | prose | pages [22] -->
[J] .Journal of Hohai University, 1993 (03): 21-27.

<!-- b000810 | prose | pages [22] -->
[17] Zhao Xiaojia, Wang Shaopo, Yu He, Qiu Chunsheng, Sun Liping, Wang

<!-- b000811 | prose | pages [22] -->
Chenchen, Zhao Lejun, Song Xiancai.Characteristics of Erosion and Pollution

<!-- b000812 | prose | pages [22] -->
Erosion by Rainfall and Runoff on Typical Underlying Surfaces in Tianjin City

<!-- b000813 | prose | pages [22] -->
Center [J] .Environmental Engineering, 2019,37 (07): 34-38 + 87 .

<!-- b000814 | prose | pages [22] -->
关注数学模型

<!-- b000815 | furniture | pages [22] -->
2

<!-- b000816 | furniture | pages [22] -->
MATHmodels

<!-- b000817 | furniture | pages [22] -->
获取更多资讯

<!-- b000818 | furniture | pages [23] -->
Team #2011873                                                                 Page 22 of 22

<!-- b000819 | prose | pages [23] -->
[18] Estela Nadal-Romero, Teodoro Lasanta, David Regües, N. Lana-

<!-- b000820 | prose | pages [23] -->
Renault, and Artemi Cerdà. Hydrological response and sediment production unde

<!-- b000821 | prose | pages [23] -->
r different land cover in abandoned farmland fields in a mediterranean mountain e

<!-- b000822 | prose | pages [23] -->
nvironment. Boletín de la Asociación de Geógrafos Españoles, 55:303-

<!-- b000823 | prose | pages [23] -->
323, 01 2011.

<!-- b000824 | prose | pages [23] -->
关注数学模型

<!-- b000825 | furniture | pages [23] -->
2

<!-- b000826 | furniture | pages [23] -->
MATHmodels

<!-- b000827 | furniture | pages [23] -->
获取更多资讯
