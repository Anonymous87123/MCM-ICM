# P-B-2020-2011873-0d3ec7b7

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2020

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | furniture | pages [1] -->
2011873

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
B

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
The Longest Lasting Sandcastle

<!-- b000009 | prose | pages [1] -->
A variety of sandcastles can be found on the seashore, range from simple mounds of sand to complex castle replicas. Over time, there is no doubt that rain and waves will gradually erode the sandcastle. However, the degree of erosion of different types of sandcastles is different. Even if the building size and the distance from the water on the same beach are roughly same. Therefore, we wonder if there exits an optimal 3D geometric shape to use as sandcastle foundation.

<!-- b000010 | prose | pages [1] -->
In task 1, in order to identity the best 3D geometric shape of sandcastle foundation, firstly, our team choose six common geometric shapes to analyze. Then, we introduce Mohr-Coulomb Yielding Criteria to check the strength of sandcastle foundation, Horton’s equation to calculate infiltration rate of seawater, further Van Genuchten Model to obtain water retention curve. Based on the study of water content, we use internal friction angle to determine whether the sandcastle is stable or not. Finally,we work out the cuboid is the best, of which lasting time is 50min.What’s more, by traversing the aspect ratio of the cuboid, we find that the narrower the width of the water surface is, the longer lasting time is.

<!-- b000011 | prose | pages [1] -->
In task 2, take sand-to-water mixture proportion into consideration. Because the sand-to-water ratio is related to the structural stability of the sandcastle, by establishing the function relationship between sand-to-water mixing ratio and internal friction angle, then programming traversal, we find that the optimal solution is when the water-to-sand ratio is 15%, and lasting time of the sandcastle 64.43min.

<!-- b000012 | prose | pages [1] -->
In task 3, we divide the impact of rainwater on the sandcastle into two parts: scour and infiltration. We find that the cuboid is still the optimal geometry, confirming the reliability of our model. Besides, ANSYS simulation analysis is used to verify the theoretical results, and results are very similar.

<!-- b000013 | prose | pages [1] -->
To sum up, by consulting a large amount of data, we establish wave erosion, tidal immersion, rain scour, and rain immersion models. The model establishment has a gradual optimization process, and the results of rain immersion are analyzed using ANSYS simulation. It is in good agreement with the theoretical calculation, which verifies the correctness of our model.

<!-- b000014 | keywords | pages [1] -->
Keywords: Mohr-Coulomb Yielding Criteria, Horton’s equation, Van Genuchten Model, Internal

<!-- b000015 | prose | pages [1] -->
friction angle, ANSYS simulation.

<!-- b000016 | prose | pages [1] -->
关注数学模型

<!-- b000017 | furniture | pages [1] -->
2

<!-- b000018 | furniture | pages [1] -->
MATHmodels

<!-- b000019 | furniture | pages [1] -->
获取更多资讯

<!-- b000020 | furniture | pages [2] -->
Team #2011873                                                                 Page 1 of 22

<!-- b000021 | heading | pages [2] -->
Content

<!-- b000022 | contents | pages [2] -->
1. Introduction ............................................................................................................................ 2

<!-- b000023 | contents | pages [2] -->
1.1Background ...................................................................................................................... 2

<!-- b000024 | contents | pages [2] -->
1.2 Our work .......................................................................................................................... 2

<!-- b000025 | contents | pages [2] -->
2. Assumptions .......................................................................................................................... 2

<!-- b000026 | contents | pages [2] -->
3. Symbols ................................................................................................................................. 3

<!-- b000027 | contents | pages [2] -->
4. Task 1: Identify the Best Three-Dimensional Geometric Shape ........................................... 3

<!-- b000028 | contents | pages [2] -->
4.1 Only consider the force of seawater on the sandcastle .................................................... 4

<!-- b000029 | contents | pages [2] -->
4.1.1 Airy wave theory ...................................................................................................... 4

<!-- b000030 | contents | pages [2] -->
4.1.2 The Morison Equation .............................................................................................. 5

<!-- b000031 | contents | pages [2] -->
4.1.3 Mohr-Coulomb Yielding Criteria ............................................................................. 6

<!-- b000032 | contents | pages [2] -->
4.2 Consider changes of water content in Sandcastle ............................................................ 8

<!-- b000033 | contents | pages [2] -->
4.2.1 Horton’s equation ..................................................................................................... 8

<!-- b000034 | contents | pages [2] -->
4.2.2 Van Genuchten Model .............................................................................................. 8

<!-- b000035 | contents | pages [2] -->
4.3 Conclusion ....................................................................................................................... 9

<!-- b000036 | contents | pages [2] -->
4.3.1 Take the cuboid as an example ................................................................................. 9

<!-- b000037 | contents | pages [2] -->
4.3.2 Best Three-dimensional geometric shape ............................................................... 10

<!-- b000038 | contents | pages [2] -->
4.3.3 Sensitivity analysis ................................................................................................. 11

<!-- b000039 | contents | pages [2] -->
5. Task 2: Take Sand-to-Water Mixture Proportion into Consideration ................................. 12

<!-- b000040 | contents | pages [2] -->
6. Task 3: Take Effect of Rain into Consideration .................................................................. 13

<!-- b000041 | contents | pages [2] -->
6.1 Precipitation model ........................................................................................................ 13

<!-- b000042 | contents | pages [2] -->
6.2 Sartor-Boyd scour model ............................................................................................... 14

<!-- b000043 | contents | pages [2] -->
6.3 Seepage process ............................................................................................................. 15

<!-- b000044 | contents | pages [2] -->
6.4 ANSYS simulation ........................................................................................................ 17

<!-- b000045 | contents | pages [2] -->
7. Task 4：Other Strategies to Make Sandcastles Last Longer .............................................. 17

<!-- b000046 | contents | pages [2] -->
8. Strengths and Weaknesses ................................................................................................... 18

<!-- b000047 | contents | pages [2] -->
8.1 Strengths ........................................................................................................................ 18

<!-- b000048 | contents | pages [2] -->
8.2 Weaknesses ................................................................................................................... 18

<!-- b000049 | contents | pages [2] -->
Article ...................................................................................................................................... 19

<!-- b000050 | contents | pages [2] -->
Reference ................................................................................................................................. 21

<!-- b000051 | contents | pages [2] -->
关注数学模型

<!-- b000052 | furniture | pages [2] -->
2

<!-- b000053 | furniture | pages [2] -->
MATHmodels

<!-- b000054 | furniture | pages [2] -->
获取更多资讯

<!-- b000055 | furniture | pages [3] -->
Team #2011873                                                                 Page 2 of 22

<!-- b000056 | contents | pages [3] -->
A variety of sandcastles can be found on the seashore, range from simple mounds

<!-- b000057 | contents | pages [3] -->
of sand to complex castle replicas. In all these, one typically forms an initial foundation

<!-- b000058 | contents | pages [3] -->
consisting of a single, nondescript mound of wetted sand, and then proceeds to cut and

<!-- b000059 | contents | pages [3] -->
shape this base into a recognizable 3-dimensional geometric shape, thereby building

<!-- b000060 | contents | pages [3] -->
more castle-defining features.

<!-- b000061 | contents | pages [3] -->
Over time, there is no doubt that rain and waves will gradually erode the sandcastle.

<!-- b000062 | contents | pages [3] -->
However, the degree of erosion of different types of sandcastles is different. Even if the

<!-- b000063 | contents | pages [3] -->
building size and the distance from the water on the same beach are roughly same.

<!-- b000064 | contents | pages [3] -->
Therefore, in order to achieve highest robustness and longest lasting time, we

<!-- b000065 | contents | pages [3] -->
wonder if there exits an optimal 3D geometric shape to use as the foundation of a

<!-- b000066 | contents | pages [3] -->
sandcastle.

<!-- b000067 | contents | pages [3] -->
To further present our solutions, we arrange our paper as follows:

<!-- b000068 | contents | pages [3] -->
⚫ In task 1, we use six common geometric shapes for research. By establishing

<!-- b000069 | contents | pages [3] -->
tide immersion model and wave erosion model, we calculate that the cuboid is

<!-- b000070 | contents | pages [3] -->
the optimal geometric model. Further research, through the study of cuboids

<!-- b000071 | contents | pages [3] -->
with different aspect ratios, we find that the smaller the width of the cuboid

<!-- b000072 | contents | pages [3] -->
facing the water, the longer the model exists.

<!-- b000073 | contents | pages [3] -->
⚫ In task 2, different sand-to-water mixing ratios will affect the strength of

<!-- b000074 | contents | pages [3] -->
sandcastles. By establishing the function relationship between different sand-

<!-- b000075 | contents | pages [3] -->
to-water mixing ratios and internal friction angles, we find 15% is the best.

<!-- b000076 | contents | pages [3] -->
⚫ In task 3, we divide the impact of rainwater on the sandcastle into two parts:

<!-- b000077 | contents | pages [3] -->
scour and infiltration. Through ANSYS simulation. we get the effects of

<!-- b000078 | contents | pages [3] -->
rainfall on the six geometries, which are very similar to the theory.

<!-- b000079 | contents | pages [3] -->
⚫ In task 4, we consider two aspects of reducing seawater infiltration and

<!-- b000080 | contents | pages [3] -->
reducing wave erosion to extend the lasting time of the sandcastle

<!-- b000081 | contents | pages [3] -->
⚫ Assume that the bottom of the model is at a horizontal plane.

<!-- b000082 | contents | pages [3] -->
⚫ Suppose the waves are moving without amplitude attenuation.

<!-- b000083 | contents | pages [3] -->
⚫ Disregard the impact of sandcastle's own gravity.

<!-- b000084 | contents | pages [3] -->
关注数学模型

<!-- b000085 | furniture | pages [3] -->
2

<!-- b000086 | furniture | pages [3] -->
MATHmodels

<!-- b000087 | furniture | pages [3] -->
获取更多资讯

<!-- b000088 | furniture | pages [4] -->
Team #2011873                                                                 Page 3 of 22

<!-- b000089 | contents | pages [4] -->
⚫ Assume that the seawater penetrates into the sandcastle uniformly.

<!-- b000090 | contents | pages [4] -->
Symbol

<!-- b000091 | contents | pages [4] -->
Description

<!-- b000092 | contents | pages [4] -->
V

<!-- b000093 | contents | pages [4] -->
Volume of sandcastle

<!-- b000094 | contents | pages [4] -->
a

<!-- b000095 | contents | pages [4] -->
Wave amplitude

<!-- b000096 | contents | pages [4] -->
u

<!-- b000097 | contents | pages [4] -->
Wave speed

<!-- b000098 | contents | pages [4] -->
u

<!-- b000099 | contents | pages [4] -->
Wave acceleration

<!-- b000100 | contents | pages [4] -->
Wave total inline force

<!-- b000101 | contents | pages [4] -->
F

<!-- b000102 | contents | pages [4] -->
w

<!-- b000103 | contents | pages [4] -->
Water content in sand

<!-- b000104 | contents | pages [4] -->


<!-- b000105 | contents | pages [4] -->
Normal stress on the cross section

<!-- b000106 | contents | pages [4] -->
n

<!-- b000107 | contents | pages [4] -->


<!-- b000108 | contents | pages [4] -->
Shear stress on the cross section

<!-- b000109 | contents | pages [4] -->
n

<!-- b000110 | contents | pages [4] -->


<!-- b000111 | contents | pages [4] -->
Internal friction angle

<!-- b000112 | contents | pages [4] -->
V

<!-- b000113 | contents | pages [4] -->
Average final speed of raindrops

<!-- b000114 | contents | pages [4] -->
m

<!-- b000115 | contents | pages [4] -->
In this problem, according to the situation of people building sandcastles on the

<!-- b000116 | contents | pages [4] -->
beach, we analyze six common 3D geometries with relatively stable structures to select

<!-- b000117 | contents | pages [4] -->
the best. Assume that they have the same volume and height.

<!-- b000118 | caption | pages [4] -->
Figure 1. Six 3D geometries we select

<!-- b000119 | contents | pages [4] -->
Considering that tide will destroy the sandcastle, and as the tide rises, the tide will

<!-- b000120 | contents | pages [4] -->
关注数学模型

<!-- b000121 | furniture | pages [4] -->
2

<!-- b000122 | furniture | pages [4] -->
MATHmodels

<!-- b000123 | furniture | pages [4] -->
获取更多资讯

<!-- b000124 | furniture | pages [5] -->
Team #2011873                                                                 Page 4 of 22

<!-- b000125 | contents | pages [5] -->
gradually flood the bottom of the sandcastle, and the water content of the sandcastle

<!-- b000126 | contents | pages [5] -->
will continue to rise. When the sandcastle is completely immersed in seawater, we have

<!-- b000127 | contents | pages [5] -->
no need to explore it. Therefore, we divide the whole process into three stages:

<!-- b000128 | contents | pages [5] -->
1) The sandcastle is not flooded. In this case, we mainly consider the force of tide

<!-- b000129 | contents | pages [5] -->
on the sandcastle.

<!-- b000130 | contents | pages [5] -->
2) Seawater begin to flood the sandcastle. In this case, water content of the

<!-- b000131 | contents | pages [5] -->
infiltrated part will change.

<!-- b000132 | contents | pages [5] -->
3) Seawater completely flood the sandcastle.

<!-- b000133 | contents | pages [5] -->
Taking a beach in Sandy Hook, USA as an example, we query the tide curve of the

<!-- b000134 | contents | pages [5] -->
place on March 6, 2020 [1].

<!-- b000135 | caption | pages [5] -->
Figure 2. Tide curve of Sandy Hook on March 6, 2020

<!-- b000136 | contents | pages [5] -->
As can be seen from the figure above, the initial height of the tide at 00:00 is 30cm,

<!-- b000137 | contents | pages [5] -->
and the relationship between tide height and time is:

<!-- b000138 | contents | pages [5] -->
=

<!-- b000139 | contents | pages [5] -->
+

<!-- b000140 | contents | pages [5] -->
+

<!-- b000141 | contents | pages [5] -->
−

<!-- b000142 | contents | pages [5] -->
（1）

<!-- b000143 | contents | pages [5] -->
h t

<!-- b000144 | contents | pages [5] -->
( )

<!-- b000145 | contents | pages [5] -->
1256sin(0.0008776

<!-- b000146 | contents | pages [5] -->
t

<!-- b000147 | contents | pages [5] -->
3.074)

<!-- b000148 | contents | pages [5] -->
70.98sin(0.4971

<!-- b000149 | contents | pages [5] -->
t

<!-- b000150 | contents | pages [5] -->
0.8185)

<!-- b000151 | contents | pages [5] -->
Where

<!-- b000152 | contents | pages [5] -->
h t is the height of tide relative to the tidal height datum plane.

<!-- b000153 | contents | pages [5] -->
t is time(h);

<!-- b000154 | contents | pages [5] -->
( )

<!-- b000155 | contents | pages [5] -->
To study the force of waves on the sandcastle, we need to know how waves move.

<!-- b000156 | contents | pages [5] -->
Airy wave theory [2] is often applied in ocean engineering and coastal engineering for

<!-- b000157 | contents | pages [5] -->
the modelling of random sea states. Airy wave theory is a linear theory for the

<!-- b000158 | contents | pages [5] -->
propagation of waves on the surface of a potential flow and above a horizontal bottom.

<!-- b000159 | contents | pages [5] -->
关注数学模型

<!-- b000160 | furniture | pages [5] -->
2

<!-- b000161 | furniture | pages [5] -->
MATHmodels

<!-- b000162 | furniture | pages [5] -->
获取更多资讯

<!-- b000163 | furniture | pages [6] -->
Team #2011873                                                                 Page 5 of 22

<!-- b000164 | contents | pages [6] -->
The free surface elevation (x,t) of one wave component is sinusoidal, as a function of

<!-- b000165 | contents | pages [6] -->
horizontal position x and time t.

<!-- b000166 | contents | pages [6] -->
(

<!-- b000167 | contents | pages [6] -->
)

<!-- b000168 | contents | pages [6] -->


<!-- b000169 | contents | pages [6] -->
=

<!-- b000170 | contents | pages [6] -->


<!-- b000171 | contents | pages [6] -->
−

<!-- b000172 | contents | pages [6] -->


<!-- b000173 | contents | pages [6] -->
（2）

<!-- b000174 | contents | pages [6] -->
x t

<!-- b000175 | contents | pages [6] -->
,

<!-- b000176 | contents | pages [6] -->
a

<!-- b000177 | contents | pages [6] -->
cos(

<!-- b000178 | contents | pages [6] -->
kx

<!-- b000179 | contents | pages [6] -->
t

<!-- b000180 | contents | pages [6] -->
)

<!-- b000181 | contents | pages [6] -->
Where

<!-- b000182 | contents | pages [6] -->
a is the wave amplitude in meter, here, we take a = 0.15m [3]. k is the angular

<!-- b000183 | contents | pages [6] -->


<!-- b000184 | contents | pages [6] -->
2

<!-- b000185 | contents | pages [6] -->
=

<!-- b000186 | contents | pages [6] -->
wavenumber in radian per meter, related to the wavelength  as

<!-- b000187 | contents | pages [6] -->
k

<!-- b000188 | contents | pages [6] -->
, here, we

<!-- b000189 | contents | pages [6] -->


<!-- b000190 | contents | pages [6] -->
assume  = 8.5m. is the angular frequency in radian per second, related to the period

<!-- b000191 | contents | pages [6] -->


<!-- b000192 | contents | pages [6] -->
2

<!-- b000193 | contents | pages [6] -->
=

<!-- b000194 | contents | pages [6] -->
T and frequency f by

<!-- b000195 | contents | pages [6] -->
, here, we assume T = 10s.

<!-- b000196 | contents | pages [6] -->
T

<!-- b000197 | contents | pages [6] -->
Then, we can get the speed (m/s) and acceleration (m/s2) of the waves.

<!-- b000198 | contents | pages [6] -->


<!-- b000199 | contents | pages [6] -->


<!-- b000200 | contents | pages [6] -->
=

<!-- b000201 | contents | pages [6] -->
=

<!-- b000202 | contents | pages [6] -->


<!-- b000203 | contents | pages [6] -->
−

<!-- b000204 | contents | pages [6] -->


<!-- b000205 | contents | pages [6] -->
u

<!-- b000206 | contents | pages [6] -->
a

<!-- b000207 | contents | pages [6] -->
sin(

<!-- b000208 | contents | pages [6] -->
kx

<!-- b000209 | contents | pages [6] -->
t

<!-- b000210 | contents | pages [6] -->
)

<!-- b000211 | contents | pages [6] -->
（3）

<!-- b000212 | contents | pages [6] -->


<!-- b000213 | contents | pages [6] -->
t

<!-- b000214 | contents | pages [6] -->


<!-- b000215 | contents | pages [6] -->
u

<!-- b000216 | contents | pages [6] -->
2 cos(

<!-- b000217 | contents | pages [6] -->
=

<!-- b000218 | contents | pages [6] -->
= −

<!-- b000219 | contents | pages [6] -->


<!-- b000220 | contents | pages [6] -->
−

<!-- b000221 | contents | pages [6] -->


<!-- b000222 | contents | pages [6] -->
u

<!-- b000223 | contents | pages [6] -->
a

<!-- b000224 | contents | pages [6] -->
kx

<!-- b000225 | contents | pages [6] -->
t

<!-- b000226 | contents | pages [6] -->
)

<!-- b000227 | contents | pages [6] -->
（4）

<!-- b000228 | contents | pages [6] -->


<!-- b000229 | contents | pages [6] -->
t

<!-- b000230 | contents | pages [6] -->
Knowing the equation of motion of the wave, we further explore the total inline

<!-- b000231 | contents | pages [6] -->
force on the wave. The Morison Equation [4] is the sum of two force components: an

<!-- b000232 | contents | pages [6] -->
inertia force in phase with the local flow acceleration and a drag force proportional to

<!-- b000233 | contents | pages [6] -->
the square of the instantaneous flow velocity.

<!-- b000234 | contents | pages [6] -->
1

<!-- b000235 | contents | pages [6] -->
=

<!-- b000236 | contents | pages [6] -->


<!-- b000237 | contents | pages [6] -->
+

<!-- b000238 | contents | pages [6] -->


<!-- b000239 | contents | pages [6] -->
F

<!-- b000240 | contents | pages [6] -->
C Vu

<!-- b000241 | contents | pages [6] -->
C Au u

<!-- b000242 | contents | pages [6] -->
（5）

<!-- b000243 | contents | pages [6] -->
m

<!-- b000244 | contents | pages [6] -->
d

<!-- b000245 | contents | pages [6] -->
2

<!-- b000246 | contents | pages [6] -->
Where

<!-- b000247 | contents | pages [6] -->
C is the inertia coefficient, here, we take

<!-- b000248 | contents | pages [6] -->
F is the total inline force on the wave;

<!-- b000249 | contents | pages [6] -->
m

<!-- b000250 | contents | pages [6] -->
C =1.5; V is the volume of sandcastle; is the density of seawater, =1.03g/cm3;

<!-- b000251 | contents | pages [6] -->
m

<!-- b000252 | contents | pages [6] -->
C is the drag coefficient, which is related to the shape of the material. A is the area of

<!-- b000253 | contents | pages [6] -->
d

<!-- b000254 | contents | pages [6] -->
the surface facing the sea water.

<!-- b000255 | contents | pages [6] -->
关注数学模型

<!-- b000256 | furniture | pages [6] -->
2

<!-- b000257 | furniture | pages [6] -->
MATHmodels

<!-- b000258 | furniture | pages [6] -->
获取更多资讯

<!-- b000259 | furniture | pages [7] -->
Team #2011873                                                                 Page 6 of 22

<!-- b000260 | caption | pages [7] -->
Figure 3. Drag coefficient of different shapes

<!-- b000261 | contents | pages [7] -->
In order to discuss the effect of waves on the structure of the sandcastle, we consult

<!-- b000262 | contents | pages [7] -->
relevant data and select the internal friction angle of the sandcastle as the research

<!-- b000263 | contents | pages [7] -->
object.

<!-- b000264 | contents | pages [7] -->
Mohr-Coulomb Yielding Criteria [6] is short for C-M Criteria. The C-M criteria is a

<!-- b000265 | contents | pages [7] -->
yield theory that takes into account the maximum or single shear stress acting on normal

<!-- b000266 | contents | pages [7] -->
or average stress, that is, when the ratio of shear stress to normal stress on the shear

<!-- b000267 | contents | pages [7] -->
plane reaches the maximum, the material yields to failure. Its expression is:

<!-- b000268 | contents | pages [7] -->


<!-- b000269 | contents | pages [7] -->
=

<!-- b000270 | contents | pages [7] -->
+

<!-- b000271 | contents | pages [7] -->


<!-- b000272 | contents | pages [7] -->


<!-- b000273 | contents | pages [7] -->
C

<!-- b000274 | contents | pages [7] -->
tan

<!-- b000275 | contents | pages [7] -->
（6）

<!-- b000276 | contents | pages [7] -->
n

<!-- b000277 | contents | pages [7] -->
n

<!-- b000278 | contents | pages [7] -->
F

<!-- b000279 | contents | pages [7] -->
=

<!-- b000280 | contents | pages [7] -->
（7）

<!-- b000281 | contents | pages [7] -->
n

<!-- b000282 | contents | pages [7] -->
S

<!-- b000283 | contents | pages [7] -->
F

<!-- b000284 | contents | pages [7] -->
=

<!-- b000285 | contents | pages [7] -->
（8）

<!-- b000286 | contents | pages [7] -->
n

<!-- b000287 | contents | pages [7] -->
A

<!-- b000288 | contents | pages [7] -->
Where

<!-- b000289 | contents | pages [7] -->
 is the normal

<!-- b000290 | contents | pages [7] -->
C is cohesion of sand;  is internal friction angle of sand;

<!-- b000291 | contents | pages [7] -->
n

<!-- b000292 | contents | pages [7] -->
 is the shear stress on the cross section; A is the area of

<!-- b000293 | contents | pages [7] -->
stress on the cross section;

<!-- b000294 | contents | pages [7] -->
n

<!-- b000295 | contents | pages [7] -->
shear plane; S is the area of the force contact surface.

<!-- b000296 | contents | pages [7] -->
To sand, C =0 [7], therefore:

<!-- b000297 | contents | pages [7] -->
关注数学模型

<!-- b000298 | furniture | pages [7] -->
2

<!-- b000299 | furniture | pages [7] -->
MATHmodels

<!-- b000300 | furniture | pages [7] -->
获取更多资讯

<!-- b000301 | furniture | pages [8] -->
Team #2011873                                                                 Page 7 of 22

<!-- b000302 | contents | pages [8] -->


<!-- b000303 | contents | pages [8] -->
=

<!-- b000304 | contents | pages [8] -->


<!-- b000305 | contents | pages [8] -->


<!-- b000306 | contents | pages [8] -->
tan

<!-- b000307 | contents | pages [8] -->
（9）

<!-- b000308 | contents | pages [8] -->
n

<!-- b000309 | contents | pages [8] -->
n

<!-- b000310 | contents | pages [8] -->


<!-- b000311 | contents | pages [8] -->
−

<!-- b000312 | contents | pages [8] -->


<!-- b000313 | contents | pages [8] -->
=

<!-- b000314 | contents | pages [8] -->
1

<!-- b000315 | contents | pages [8] -->
（10）

<!-- b000316 | contents | pages [8] -->
n

<!-- b000317 | contents | pages [8] -->
tan (

<!-- b000318 | contents | pages [8] -->
)

<!-- b000319 | contents | pages [8] -->


<!-- b000320 | contents | pages [8] -->
n

<!-- b000321 | contents | pages [8] -->
Experiments show that the water content has a certain effect on the internal friction

<!-- b000322 | contents | pages [8] -->
angle, and different water content corresponds to different internal friction angles.

<!-- b000323 | contents | pages [8] -->
According to the relevant data found [8] [9], we find the relationship between internal

<!-- b000324 | contents | pages [8] -->
friction angle and water content of the sand, the formula is as follows:

<!-- b000325 | contents | pages [8] -->
( )

<!-- b000326 | contents | pages [8] -->
= −

<!-- b000327 | contents | pages [8] -->
+

<!-- b000328 | contents | pages [8] -->
+

<!-- b000329 | contents | pages [8] -->
2

<!-- b000330 | contents | pages [8] -->
（11）

<!-- b000331 | contents | pages [8] -->
g w

<!-- b000332 | contents | pages [8] -->
140

<!-- b000333 | contents | pages [8] -->
w

<!-- b000334 | contents | pages [8] -->
56

<!-- b000335 | contents | pages [8] -->
w

<!-- b000336 | contents | pages [8] -->
28.5

<!-- b000337 | contents | pages [8] -->
Where, w is water content in sand.

<!-- b000338 | caption | pages [8] -->
Figure 4. Curve of internal friction angle and water content

<!-- b000339 | contents | pages [8] -->
From the figure we can see that, as the water content increases, the internal friction

<!-- b000340 | contents | pages [8] -->
angle increases first and then decreases. The main reason is that sand particles exhibit

<!-- b000341 | contents | pages [8] -->
cohesiveness under a certain water content. To make the sand slide relative to each other,

<!-- b000342 | contents | pages [8] -->
it must overcome not only the friction between sand, but also the cohesion between

<!-- b000343 | contents | pages [8] -->
sand. Beyond a certain water content, all the sand particles are infiltrated in the water,

<!-- b000344 | contents | pages [8] -->
and the lubricating effect of water reduces the friction between the particles.

<!-- b000345 | contents | pages [8] -->
( )

<!-- b000346 | contents | pages [8] -->


<!-- b000347 | contents | pages [8] -->


<!-- b000348 | contents | pages [8] -->
g w

<!-- b000349 | contents | pages [8] -->
Therefore, we assume that, when

<!-- b000350 | contents | pages [8] -->
, that is, when the internal friction

<!-- b000351 | contents | pages [8] -->
angle of the external force acting on the sandcastle is greater than the value of the

<!-- b000352 | contents | pages [8] -->
maximum internal friction angle that can be stabilized at the water content of the sand,

<!-- b000353 | contents | pages [8] -->
( )

<!-- b000354 | contents | pages [8] -->


<!-- b000355 | contents | pages [8] -->


<!-- b000356 | contents | pages [8] -->
g w

<!-- b000357 | contents | pages [8] -->
the sandcastle will collapse; when

<!-- b000358 | contents | pages [8] -->
, The sandcastle will not collapse.

<!-- b000359 | contents | pages [8] -->
关注数学模型

<!-- b000360 | furniture | pages [8] -->
2

<!-- b000361 | furniture | pages [8] -->
MATHmodels

<!-- b000362 | furniture | pages [8] -->
获取更多资讯

<!-- b000363 | furniture | pages [9] -->
Team #2011873                                                                 Page 8 of 22

<!-- b000364 | contents | pages [9] -->
When seawater begins to submerge the sandcastle, in order to learn how the water

<!-- b000365 | contents | pages [9] -->
content of the sandcastle changes, we must first know the infiltration rate of waves.

<!-- b000366 | contents | pages [9] -->
Horton’s equation is an empirical formula for calculating the infiltration curve, and

<!-- b000367 | contents | pages [9] -->
its expression is [10]:

<!-- b000368 | contents | pages [9] -->
( )

<!-- b000369 | contents | pages [9] -->
f e−

<!-- b000370 | contents | pages [9] -->
=

<!-- b000371 | contents | pages [9] -->
+

<!-- b000372 | contents | pages [9] -->
−

<!-- b000373 | contents | pages [9] -->
kt

<!-- b000374 | contents | pages [9] -->
f t

<!-- b000375 | contents | pages [9] -->
f

<!-- b000376 | contents | pages [9] -->
(

<!-- b000377 | contents | pages [9] -->
f

<!-- b000378 | contents | pages [9] -->
)

<!-- b000379 | contents | pages [9] -->
（12）

<!-- b000380 | contents | pages [9] -->
c

<!-- b000381 | contents | pages [9] -->
0

<!-- b000382 | contents | pages [9] -->
c

<!-- b000383 | contents | pages [9] -->
Where

<!-- b000384 | contents | pages [9] -->
( )

<!-- b000385 | contents | pages [9] -->
f t is the infiltration rate at time t;

<!-- b000386 | contents | pages [9] -->
0f is the initial infiltration rate, take

<!-- b000387 | contents | pages [9] -->
f

<!-- b000388 | contents | pages [9] -->
0=0

<!-- b000389 | contents | pages [9] -->
;

<!-- b000390 | contents | pages [9] -->
cf  is the constant infiltration rate after the roil has been saturated or minimum

<!-- b000391 | contents | pages [9] -->
mm/min; k is the decay constant specific to the

<!-- b000392 | contents | pages [9] -->
infiltration rate, here, we assume

<!-- b000393 | contents | pages [9] -->
cf

<!-- b000394 | contents | pages [9] -->
=1

<!-- b000395 | contents | pages [9] -->
[12].

<!-- b000396 | contents | pages [9] -->
k

<!-- b000397 | contents | pages [9] -->
=2

<!-- b000398 | contents | pages [9] -->
sand, take

<!-- b000399 | contents | pages [9] -->
We already know the infiltration rate at time t, and what is the relationship between

<!-- b000400 | contents | pages [9] -->
( )

<!-- b000401 | contents | pages [9] -->
f t and water content of the sandcastle? Here, we use Van Genuchten Model.

<!-- b000402 | contents | pages [9] -->
The shape of water retention curves can be characterized by several models, one of

<!-- b000403 | contents | pages [9] -->
them as the Van Genuchten Model [12] [13].

<!-- b000404 | contents | pages [9] -->


<!-- b000405 | contents | pages [9] -->
−

<!-- b000406 | contents | pages [9] -->


<!-- b000407 | contents | pages [9] -->
( )

<!-- b000408 | contents | pages [9] -->


<!-- b000409 | contents | pages [9] -->
=

<!-- b000410 | contents | pages [9] -->


<!-- b000411 | contents | pages [9] -->
+

<!-- b000412 | contents | pages [9] -->
s

<!-- b000413 | contents | pages [9] -->
r

<!-- b000414 | contents | pages [9] -->
（13）

<!-- b000415 | contents | pages [9] -->
r

<!-- b000416 | contents | pages [9] -->
1

<!-- b000417 | contents | pages [9] -->
−

<!-- b000418 | contents | pages [9] -->
1

<!-- b000419 | contents | pages [9] -->


<!-- b000420 | contents | pages [9] -->


<!-- b000421 | contents | pages [9] -->
n

<!-- b000422 | contents | pages [9] -->
+

<!-- b000423 | contents | pages [9] -->


<!-- b000424 | contents | pages [9] -->
n

<!-- b000425 | contents | pages [9] -->
1 (

<!-- b000426 | contents | pages [9] -->
)

<!-- b000427 | contents | pages [9] -->


<!-- b000428 | contents | pages [9] -->


<!-- b000429 | contents | pages [9] -->
Where

<!-- b000430 | contents | pages [9] -->
( )

<!-- b000431 | contents | pages [9] -->
 is the water retention curve;  is cm of water;

<!-- b000432 | contents | pages [9] -->
s  is saturated water

<!-- b000433 | contents | pages [9] -->
[14];  is

<!-- b000434 | contents | pages [9] -->
s

<!-- b000435 | contents | pages [9] -->
r  is residual water content, take

<!-- b000436 | contents | pages [9] -->
r

<!-- b000437 | contents | pages [9] -->
[14];

<!-- b000438 | contents | pages [9] -->
=0.3

<!-- b000439 | contents | pages [9] -->
=0.05

<!-- b000440 | contents | pages [9] -->
content, take

<!-- b000441 | contents | pages [9] -->


<!-- b000442 | contents | pages [9] -->


<!-- b000443 | contents | pages [9] -->
cm-1 [14]; n is a

<!-- b000444 | contents | pages [9] -->
0

<!-- b000445 | contents | pages [9] -->
=0.01

<!-- b000446 | contents | pages [9] -->
related to the inverse of the air entry suction,

<!-- b000447 | contents | pages [9] -->
, take

<!-- b000448 | contents | pages [9] -->
n , take

<!-- b000449 | contents | pages [9] -->
1

<!-- b000450 | contents | pages [9] -->
n

<!-- b000451 | contents | pages [9] -->
=3

<!-- b000452 | contents | pages [9] -->
measure of the pore-size distribution,

<!-- b000453 | contents | pages [9] -->
.

<!-- b000454 | contents | pages [9] -->
( )

<!-- b000455 | contents | pages [9] -->
Note that  and

<!-- b000456 | contents | pages [9] -->
f t have the same physical meaning, so we take equation (12)

<!-- b000457 | contents | pages [9] -->
into (13) to get the water retention curve.

<!-- b000458 | contents | pages [9] -->
关注数学模型

<!-- b000459 | furniture | pages [9] -->
2

<!-- b000460 | furniture | pages [9] -->
MATHmodels

<!-- b000461 | furniture | pages [9] -->
获取更多资讯

<!-- b000462 | furniture | pages [10] -->
Team #2011873                                                                 Page 9 of 22

<!-- b000463 | caption | pages [10] -->
Figure 5. Curve of water retention

<!-- b000464 | contents | pages [10] -->
Then use formula (11) to calculate the internal friction angle of the submerged part

<!-- b000465 | contents | pages [10] -->
and compare it with .

<!-- b000466 | contents | pages [10] -->
Assume that the size of the cuboid is 0.4m0.3m0.3m, where the height is 0.3m.

<!-- b000467 | contents | pages [10] -->
Considering that the larger the area, the greater the force, so we choose the surface with

<!-- b000468 | contents | pages [10] -->
size 0.3m0.3m as water-side face. Then, the area of shear plane A=0.4m0.3m, the

<!-- b000469 | contents | pages [10] -->
area of the force contact surface S=0.3m0.3m.

<!-- b000470 | contents | pages [10] -->
According to Figure 2, initial height of the tide is 30cm, and a = 0.15m( formula

<!-- b000471 | contents | pages [10] -->
(2)), we place the sandcastle at 45cm relative to the tidal height datum plane, which is

<!-- b000472 | contents | pages [10] -->
the maximum height of the tide.

<!-- b000473 | contents | pages [10] -->
Then, it can be obtained from Figure 2 that the time taken for the tide to rise from

<!-- b000474 | contents | pages [10] -->
the initial value to the location of the sandcastle is 40 minutes, which is the first stage

<!-- b000475 | contents | pages [10] -->
in our model. It takes 50 minutes for the tide to continue rising to just completely

<!-- b000476 | contents | pages [10] -->
submerge the sandcastle, which is the second stage.

<!-- b000477 | contents | pages [10] -->
Assume that the initial moisture content of the sandcastle is 20%. The internal

<!-- b000478 | contents | pages [10] -->
( )

<!-- b000479 | contents | pages [10] -->
g w under this water content can be obtained from

<!-- b000480 | contents | pages [10] -->
friction angle of the sandcastle

<!-- b000481 | caption | pages [10] -->
Figure 4.

<!-- b000482 | contents | pages [10] -->
关注数学模型

<!-- b000483 | furniture | pages [10] -->
2

<!-- b000484 | furniture | pages [10] -->
MATHmodels

<!-- b000485 | furniture | pages [10] -->
获取更多资讯

<!-- b000486 | furniture | pages [11] -->
Team #2011873                                                                 Page 10 of 22

<!-- b000487 | contents | pages [11] -->
In the first stage, it is calculated that the internal friction angle generated by wave

<!-- b000488 | contents | pages [11] -->
( )

<!-- b000489 | contents | pages [11] -->
 is smaller than

<!-- b000490 | contents | pages [11] -->
g w , that is, the cuboid model can exist stably in the first stage.

<!-- b000491 | contents | pages [11] -->
In the second stage, as the seawater began to submerge the sandcastle, the water

<!-- b000492 | contents | pages [11] -->
content of the sandcastle gradually increased with time. From Figure 4, it can be seen

<!-- b000493 | contents | pages [11] -->
that the internal friction angle continue to decrease. When it decrease to less than the

<!-- b000494 | contents | pages [11] -->
internal friction angle generated by wave, the sandcastle will collapse. The specific

<!-- b000495 | contents | pages [11] -->
change process is shown in the following figure.

<!-- b000496 | caption | pages [11] -->
Figure 6. Curve of internal friction angle changing with time

<!-- b000497 | contents | pages [11] -->
It can be seen from the figure above that the lasting time of the cuboid sandcastle

<!-- b000498 | contents | pages [11] -->
in the second stage is 10 minutes, that is, the total lasting time is about 50 minutes.

<!-- b000499 | contents | pages [11] -->
When analyzing the stability of the other five geometries, the method is similar.

<!-- b000500 | contents | pages [11] -->
Due to space limitations, it will not be described again.

<!-- b000501 | contents | pages [11] -->
We obtain the lasting time of the six geometries with the same volume and height,

<!-- b000502 | contents | pages [11] -->
and the effective height of the first wave action. The specific results are shown in the

<!-- b000503 | contents | pages [11] -->
following table.

<!-- b000504 | contents | pages [11] -->
关注数学模型

<!-- b000505 | furniture | pages [11] -->
2

<!-- b000506 | furniture | pages [11] -->
MATHmodels

<!-- b000507 | furniture | pages [11] -->
获取更多资讯

<!-- b000508 | furniture | pages [12] -->
Team #2011873                                                                 Page 11 of 22

<!-- b000509 | caption | pages [12] -->
Table 1. Lasting time and effective wave height in the first stage of six geometries

<!-- b000510 | contents | pages [12] -->
Effective wave height in

<!-- b000511 | contents | pages [12] -->
Geometric shapes

<!-- b000512 | contents | pages [12] -->
Lasting time（min）

<!-- b000513 | contents | pages [12] -->
the first stage（m）

<!-- b000514 | contents | pages [12] -->
Cuboid

<!-- b000515 | contents | pages [12] -->
about 50min

<!-- b000516 | contents | pages [12] -->
>0.2

<!-- b000517 | contents | pages [12] -->
Cylinder

<!-- b000518 | contents | pages [12] -->
Less than 40min

<!-- b000519 | contents | pages [12] -->
<0.18

<!-- b000520 | contents | pages [12] -->
Equilateral triangular

<!-- b000521 | contents | pages [12] -->
Less than 40min

<!-- b000522 | contents | pages [12] -->
<0.13

<!-- b000523 | contents | pages [12] -->
cylinder

<!-- b000524 | contents | pages [12] -->
Frustum of a cone

<!-- b000525 | contents | pages [12] -->
Less than 40min

<!-- b000526 | contents | pages [12] -->
<0.10

<!-- b000527 | contents | pages [12] -->
Three trustum of a

<!-- b000528 | contents | pages [12] -->
Collapse in a short time

<!-- b000529 | contents | pages [12] -->
<0.17

<!-- b000530 | contents | pages [12] -->
pyramid

<!-- b000531 | contents | pages [12] -->
Four trustum of a

<!-- b000532 | contents | pages [12] -->
Less than 40min

<!-- b000533 | contents | pages [12] -->
<0.14

<!-- b000534 | contents | pages [12] -->
pyramid

<!-- b000535 | contents | pages [12] -->
As can be seen from the table, except for the cuboid, the other five geometries

<!-- b000536 | contents | pages [12] -->
collapse in the first stage. We know that the higher the wave, the greater the impact

<!-- b000537 | contents | pages [12] -->
force, so a larger value of the effective height of the wave indicates that the geometry

<!-- b000538 | contents | pages [12] -->
is more stable. In summary, the cuboid is an optimal 3D geometric shape.

<!-- b000539 | contents | pages [12] -->
It can be known from equations (7) and (8) that the larger the area of A and S, the

<!-- b000540 | contents | pages [12] -->
smaller the damage to the sandcastle. So next we change the length and width of the

<!-- b000541 | contents | pages [12] -->
cuboid, and further analyze the effect of the size on the stability of the sandcastle.

<!-- b000542 | contents | pages [12] -->
Use formula (10) to calculate the change of the internal friction angle with length-

<!-- b000543 | contents | pages [12] -->
width ratio, and draw the figure.

<!-- b000544 | caption | pages [12] -->
Figure 7. Curve of internal friction angle changing with length-width ratio

<!-- b000545 | contents | pages [12] -->
关注数学模型

<!-- b000546 | furniture | pages [12] -->
2

<!-- b000547 | furniture | pages [12] -->
MATHmodels

<!-- b000548 | furniture | pages [12] -->
获取更多资讯

<!-- b000549 | furniture | pages [13] -->
Team #2011873                                                                 Page 12 of 22

<!-- b000550 | contents | pages [13] -->
From the figure above, we learn that the larger length-width ratio, the smaller the

<!-- b000551 | contents | pages [13] -->
internal friction angle generated by external forces, and the more stable the sandcastle.

<!-- b000552 | contents | pages [13] -->
This is consistent with the actual situation.

<!-- b000553 | contents | pages [13] -->
In Task 1, we set the initial water content to 20% and use the internal friction angle

<!-- b000554 | contents | pages [13] -->
to determine whether the sandcastle structure is stable. The internal friction angle is

<!-- b000555 | contents | pages [13] -->
related to the water content, so it is necessary to find the optimal sand-water ratio to

<!-- b000556 | contents | pages [13] -->
make the sandcastle last longer.

<!-- b000557 | contents | pages [13] -->
First, by changing the initial water content and then the internal friction angle, the

<!-- b000558 | contents | pages [13] -->
( )

<!-- b000559 | contents | pages [13] -->


<!-- b000560 | contents | pages [13] -->


<!-- b000561 | contents | pages [13] -->
g w

<!-- b000562 | contents | pages [13] -->
sandcastle satisfies

<!-- b000563 | contents | pages [13] -->
, and the sand-to-water mixing ratio range that keeps the

<!-- b000564 | contents | pages [13] -->
sandcastle intact in the first stage is 5% -25%. Then, in the second stage, a curve of the

<!-- b000565 | contents | pages [13] -->
sandcastle collapse time changing with the initial water content in the sand is drawn.

<!-- b000566 | caption | pages [13] -->
Figure 8. Curve of the sandcastle collapse time with the initial water content

<!-- b000567 | contents | pages [13] -->
We can see that as the initial water content in the sand increases, the lasting time

<!-- b000568 | contents | pages [13] -->
of the sandcastle gradually decreases. When the initial water content is 5%, the total

<!-- b000569 | contents | pages [13] -->
lasting time of the sandcastle is the longest, which is 67 min.

<!-- b000570 | contents | pages [13] -->
However, in Figure 4, when the water content w = 15%, the internal friction angle

<!-- b000571 | contents | pages [13] -->
is the largest and the sandcastle has the best stability. From the above figure, we get that

<!-- b000572 | contents | pages [13] -->
the total lasting time of the sandcastle under this condition is 64.43min.

<!-- b000573 | contents | pages [13] -->
In fact, there is no contradiction between the two. Because when the initial water

<!-- b000574 | contents | pages [13] -->
关注数学模型

<!-- b000575 | furniture | pages [13] -->
2

<!-- b000576 | furniture | pages [13] -->
MATHmodels

<!-- b000577 | furniture | pages [13] -->
获取更多资讯

<!-- b000578 | furniture | pages [14] -->
Team #2011873                                                                 Page 13 of 22

<!-- b000579 | contents | pages [14] -->
content is small, the starting point of the rise is low, and accordingly the duration of the

<!-- b000580 | contents | pages [14] -->
sandcastle is longer. Considering the viscosity of the sand [15], and the difference

<!-- b000581 | contents | pages [14] -->
between the two is not large, we choose 15% as the best water-to-sand mixing ratio.

<!-- b000582 | contents | pages [14] -->
In order to study the impact of rain on sandcastles, we first need to understand some

<!-- b000583 | contents | pages [14] -->
of the motion characteristics of rain.

<!-- b000584 | contents | pages [14] -->
Suppose the rain drops vertically. The falling raindrops have large kinetic energy.

<!-- b000585 | contents | pages [14] -->
When they hit the sandcastle, they will destroy the structure of the sandcastle and also

<!-- b000586 | contents | pages [14] -->
change the water content of the sandcastle. Therefore, we divide the impact of rainwater

<!-- b000587 | contents | pages [14] -->
on the sandcastle into two parts: scour and infiltration.

<!-- b000588 | contents | pages [14] -->
Raindrop final speed calculation formula [16]:

<!-- b000589 | contents | pages [14] -->


<!-- b000590 | contents | pages [14] -->
2

<!-- b000591 | contents | pages [14] -->


<!-- b000592 | contents | pages [14] -->


<!-- b000593 | contents | pages [14] -->


<!-- b000594 | contents | pages [14] -->


<!-- b000595 | contents | pages [14] -->
+

<!-- b000596 | contents | pages [14] -->
−

<!-- b000597 | contents | pages [14] -->


<!-- b000598 | contents | pages [14] -->
38.9

<!-- b000599 | contents | pages [14] -->
2400

<!-- b000600 | contents | pages [14] -->
gd

<!-- b000601 | contents | pages [14] -->
38.9

<!-- b000602 | contents | pages [14] -->
d

<!-- b000603 | contents | pages [14] -->
3mm

<!-- b000604 | contents | pages [14] -->


<!-- b000605 | contents | pages [14] -->


<!-- b000606 | contents | pages [14] -->


<!-- b000607 | contents | pages [14] -->
d

<!-- b000608 | contents | pages [14] -->


<!-- b000609 | contents | pages [14] -->
d

<!-- b000610 | contents | pages [14] -->
= 

<!-- b000611 | contents | pages [14] -->
（14）

<!-- b000612 | contents | pages [14] -->
V

<!-- b000613 | contents | pages [14] -->
m

<!-- b000614 | contents | pages [14] -->


<!-- b000615 | contents | pages [14] -->
d

<!-- b000616 | contents | pages [14] -->


<!-- b000617 | contents | pages [14] -->


<!-- b000618 | contents | pages [14] -->
3

<!-- b000619 | contents | pages [14] -->
d

<!-- b000620 | contents | pages [14] -->
6mm

<!-- b000621 | contents | pages [14] -->


<!-- b000622 | contents | pages [14] -->
+

<!-- b000623 | contents | pages [14] -->


<!-- b000624 | contents | pages [14] -->
0.113

<!-- b000625 | contents | pages [14] -->
0.845

<!-- b000626 | contents | pages [14] -->
d

<!-- b000627 | contents | pages [14] -->
Where   is viscosity coefficient of air movement. When T=20℃=293K, 

<!-- b000628 | contents | pages [14] -->
=1.81074155510-5PaS.

<!-- b000629 | contents | pages [14] -->
=

<!-- b000630 | contents | pages [14] -->
q

<!-- b000631 | contents | pages [14] -->
mV

<!-- b000632 | contents | pages [14] -->
Considering raindrops as spheres. According to the momentum formula

<!-- b000633 | contents | pages [14] -->
m

<!-- b000634 | contents | pages [14] -->
1

<!-- b000635 | contents | pages [14] -->
=

<!-- b000636 | contents | pages [14] -->
2

<!-- b000637 | contents | pages [14] -->
and energy formula

<!-- b000638 | contents | pages [14] -->
, the momentum and energy contained in each raindrop

<!-- b000639 | contents | pages [14] -->
E

<!-- b000640 | contents | pages [14] -->
mV

<!-- b000641 | contents | pages [14] -->
m

<!-- b000642 | contents | pages [14] -->
2

<!-- b000643 | contents | pages [14] -->
can be obtained, and the relationship between raindrop diameter and momentum and

<!-- b000644 | contents | pages [14] -->
energy can be further obtained.

<!-- b000645 | contents | pages [14] -->
However, in the actual calculation of rainfall kinetic energy and other rainfall

<!-- b000646 | contents | pages [14] -->
characteristics, there is often only data of rainfall or rainfall intensity, and observation

<!-- b000647 | contents | pages [14] -->
data of raindrop diameter is lacking. In order to facilitate production applications, the

<!-- b000648 | contents | pages [14] -->
final raindrop speed can be expressed as a function of rain intensity. According to the

<!-- b000649 | contents | pages [14] -->
analysis of measured data, there is a power function relationship between the median

<!-- b000650 | contents | pages [14] -->
diameter of raindrops and the rain intensity [16]:

<!-- b000651 | contents | pages [14] -->
=

<!-- b000652 | contents | pages [14] -->
0.32

<!-- b000653 | contents | pages [14] -->
d

<!-- b000654 | contents | pages [14] -->
2.52

<!-- b000655 | contents | pages [14] -->
i

<!-- b000656 | contents | pages [14] -->
（15）

<!-- b000657 | contents | pages [14] -->
50

<!-- b000658 | contents | pages [14] -->
d is median diameter of raindrops(mm); i is rain intensity(mm/min).

<!-- b000659 | contents | pages [14] -->
Where

<!-- b000660 | contents | pages [14] -->
50

<!-- b000661 | contents | pages [14] -->
By taking equation (15) into (14), we get the formula for calculating the average

<!-- b000662 | contents | pages [14] -->
final speed of raindrops from rainfall intensity.

<!-- b000663 | contents | pages [14] -->
关注数学模型

<!-- b000664 | furniture | pages [14] -->
2

<!-- b000665 | furniture | pages [14] -->
MATHmodels

<!-- b000666 | furniture | pages [14] -->
获取更多资讯

<!-- b000667 | furniture | pages [15] -->
Team #2011873                                                                 Page 14 of 22

<!-- b000668 | contents | pages [15] -->


<!-- b000669 | contents | pages [15] -->
2

<!-- b000670 | contents | pages [15] -->


<!-- b000671 | contents | pages [15] -->


<!-- b000672 | contents | pages [15] -->


<!-- b000673 | contents | pages [15] -->


<!-- b000674 | contents | pages [15] -->
+

<!-- b000675 | contents | pages [15] -->
−

<!-- b000676 | contents | pages [15] -->


<!-- b000677 | contents | pages [15] -->
0.23

<!-- b000678 | contents | pages [15] -->
1.544

<!-- b000679 | contents | pages [15] -->
6.048

<!-- b000680 | contents | pages [15] -->
gi

<!-- b000681 | contents | pages [15] -->
1.544

<!-- b000682 | contents | pages [15] -->
i

<!-- b000683 | contents | pages [15] -->
2.13

<!-- b000684 | contents | pages [15] -->


<!-- b000685 | contents | pages [15] -->


<!-- b000686 | contents | pages [15] -->


<!-- b000687 | contents | pages [15] -->
0.23

<!-- b000688 | contents | pages [15] -->
0.23

<!-- b000689 | contents | pages [15] -->


<!-- b000690 | contents | pages [15] -->
i

<!-- b000691 | contents | pages [15] -->
i

<!-- b000692 | contents | pages [15] -->
= 

<!-- b000693 | contents | pages [15] -->
V

<!-- b000694 | contents | pages [15] -->
（16）

<!-- b000695 | contents | pages [15] -->
m

<!-- b000696 | contents | pages [15] -->


<!-- b000697 | contents | pages [15] -->
0.23

<!-- b000698 | contents | pages [15] -->
i

<!-- b000699 | contents | pages [15] -->


<!-- b000700 | contents | pages [15] -->
2.13

<!-- b000701 | contents | pages [15] -->
i

<!-- b000702 | contents | pages [15] -->
43.46

<!-- b000703 | contents | pages [15] -->


<!-- b000704 | contents | pages [15] -->
+

<!-- b000705 | contents | pages [15] -->


<!-- b000706 | contents | pages [15] -->
0.23

<!-- b000707 | contents | pages [15] -->
0.0448

<!-- b000708 | contents | pages [15] -->
0.0845

<!-- b000709 | contents | pages [15] -->
i

<!-- b000710 | contents | pages [15] -->
Through calculation, we get the relationship between precipitation and raindrop

<!-- b000711 | contents | pages [15] -->
speed, energy and momentum, as shown in the following figure:

<!-- b000712 | caption | pages [15] -->
Figure 9. Relationship between precipitation and raindrop speed, energy, momentum

<!-- b000713 | contents | pages [15] -->
After knowing the relevant motion parameters of raindrops, we also need to

<!-- b000714 | contents | pages [15] -->
analyze the impact of raindrops on the sandcastle.

<!-- b000715 | contents | pages [15] -->
The Sartor-Boyd scour model [17] is mainly applicable to the rainfall process with

<!-- b000716 | contents | pages [15] -->
initial scouring effect, as shown in formula (17):

<!-- b000717 | contents | pages [15] -->
dP

<!-- b000718 | contents | pages [15] -->
t =

<!-- b000719 | contents | pages [15] -->
K

<!-- b000720 | contents | pages [15] -->
Pr

<!-- b000721 | contents | pages [15] -->
（17）

<!-- b000722 | contents | pages [15] -->
2

<!-- b000723 | contents | pages [15] -->
d

<!-- b000724 | contents | pages [15] -->
K is the erosion coefficient (empirical value), mm-1; P is the volume of

<!-- b000725 | contents | pages [15] -->
Where

<!-- b000726 | contents | pages [15] -->
2

<!-- b000727 | contents | pages [15] -->
sandcastle at the beginning, m3; r is rainwater runoff per unit time per unit area, that is,

<!-- b000728 | contents | pages [15] -->
rainfall intensity, mm / min; t is time, min.

<!-- b000729 | contents | pages [15] -->
K is taken as 0.201 [17] to obtain the change of the volume of sand

<!-- b000730 | contents | pages [15] -->
In our model,

<!-- b000731 | contents | pages [15] -->
2

<!-- b000732 | contents | pages [15] -->
washed away with precipitation, as shown in the figure below:

<!-- b000733 | contents | pages [15] -->
关注数学模型

<!-- b000734 | furniture | pages [15] -->
2

<!-- b000735 | furniture | pages [15] -->
MATHmodels

<!-- b000736 | furniture | pages [15] -->
获取更多资讯

<!-- b000737 | furniture | pages [16] -->
Team #2011873                                                                 Page 15 of 22

<!-- b000738 | caption | pages [16] -->
Figure 10. Change of the volume of sand washed away with precipitation

<!-- b000739 | caption | pages [16] -->
Figure 11. Flow chart for seepage process

<!-- b000740 | contents | pages [16] -->
When the sandcastle is affected by rain, we use Matlab to fit the relationship

<!-- b000741 | contents | pages [16] -->
between the internal friction angle of the sandcastle and the water content, as follows

<!-- b000742 | contents | pages [16] -->
[18]:

<!-- b000743 | contents | pages [16] -->
关注数学模型

<!-- b000744 | furniture | pages [16] -->
2

<!-- b000745 | furniture | pages [16] -->
MATHmodels

<!-- b000746 | furniture | pages [16] -->
获取更多资讯

<!-- b000747 | furniture | pages [17] -->
Team #2011873                                                                 Page 16 of 22

<!-- b000748 | contents | pages [17] -->
=

<!-- b000749 | contents | pages [17] -->
+

<!-- b000750 | contents | pages [17] -->
（18）

<!-- b000751 | contents | pages [17] -->
0.8462

<!-- b000752 | contents | pages [17] -->
w

<!-- b000753 | contents | pages [17] -->
5.256

<!-- b000754 | caption | pages [17] -->
Figure 12. Relationship between internal friction angle and water content when the

<!-- b000755 | contents | pages [17] -->
sandcastle is affected by rain

<!-- b000756 | contents | pages [17] -->
In precipitation model, we have obtained the formula for calculating the final

<!-- b000757 | contents | pages [17] -->
velocity of raindrops. Then, bring it into equation (13) to get the water content of the

<!-- b000758 | contents | pages [17] -->
sandcastle. According to formula (18), we can get internal friction angle of sandcastle

<!-- b000759 | contents | pages [17] -->
( )

<!-- b000760 | contents | pages [17] -->
while raining. Finally, compare the relationship between and

<!-- b000761 | contents | pages [17] -->
g w , and draw the

<!-- b000762 | contents | pages [17] -->
conclusion.

<!-- b000763 | caption | pages [17] -->
Table 2. Effective height of the six geometries when it rains

<!-- b000764 | contents | pages [17] -->
Geometric shapes

<!-- b000765 | contents | pages [17] -->
Effective height

<!-- b000766 | contents | pages [17] -->
Cuboid

<!-- b000767 | contents | pages [17] -->
0.20m

<!-- b000768 | contents | pages [17] -->
Cylinder

<!-- b000769 | contents | pages [17] -->
0.15m

<!-- b000770 | contents | pages [17] -->
Equilateral triangular

<!-- b000771 | contents | pages [17] -->
0.11m

<!-- b000772 | contents | pages [17] -->
cylinder

<!-- b000773 | contents | pages [17] -->
Frustum of a cone

<!-- b000774 | contents | pages [17] -->
0.08m

<!-- b000775 | contents | pages [17] -->
Three trustum of a

<!-- b000776 | contents | pages [17] -->
0.15m

<!-- b000777 | contents | pages [17] -->
pyramid

<!-- b000778 | contents | pages [17] -->
Four trustum of a

<!-- b000779 | contents | pages [17] -->
0.15m

<!-- b000780 | contents | pages [17] -->
pyramid

<!-- b000781 | contents | pages [17] -->
The results show that rainwater has a certain effect on the structural stability of

<!-- b000782 | contents | pages [17] -->
sand castles. Comparing the effective heights of the six geometries, we find that the

<!-- b000783 | contents | pages [17] -->
cuboid is still the optimal geometry, confirming the reliability of our model.

<!-- b000784 | contents | pages [17] -->
关注数学模型

<!-- b000785 | furniture | pages [17] -->
2

<!-- b000786 | furniture | pages [17] -->
MATHmodels

<!-- b000787 | furniture | pages [17] -->
获取更多资讯

<!-- b000788 | furniture | pages [18] -->
Team #2011873                                                                 Page 17 of 22

<!-- b000789 | contents | pages [18] -->
After theoretical calculations, ANSYS simulation analysis is used to verify the

<!-- b000790 | contents | pages [18] -->
theoretical results. Through the simulation analysis of the rainfall scouring model, we

<!-- b000791 | contents | pages [18] -->
get the pressure, tension and deformation maps of the model. By comparing with the

<!-- b000792 | contents | pages [18] -->
theoretical results, the results are very similar. The following figure shows the

<!-- b000793 | contents | pages [18] -->
simulation analysis of six models:

<!-- b000794 | caption | pages [18] -->
Figure 13. The pressure, tension and deformation cloud of the cuboid

<!-- b000795 | caption | pages [18] -->
Figure 14. Pressure distribution of the other five models

<!-- b000796 | contents | pages [18] -->
：

<!-- b000797 | contents | pages [18] -->
From the analysis of the first three questions, in order to extend the lasting time of

<!-- b000798 | contents | pages [18] -->
the sandcastle, we can consider two aspects: reducing seawater infiltration and reducing

<!-- b000799 | contents | pages [18] -->
wave erosion.

<!-- b000800 | contents | pages [18] -->
On the one hand, we can cover the sandcastle, for example, placing a shield in front

<!-- b000801 | contents | pages [18] -->
关注数学模型

<!-- b000802 | furniture | pages [18] -->
2

<!-- b000803 | furniture | pages [18] -->
MATHmodels

<!-- b000804 | furniture | pages [18] -->
获取更多资讯

<!-- b000805 | furniture | pages [19] -->
Team #2011873                                                                 Page 18 of 22

<!-- b000806 | contents | pages [19] -->
of the sandcastle to reduce the impact of the waves on the sandcastle. Another example

<!-- b000807 | contents | pages [19] -->
is to use a plastic bag to wrap the sandcastle. This can eliminate the infiltration of

<!-- b000808 | contents | pages [19] -->
rainwater and seawater, also avoid contact with the waves, thereby reducing the erosion

<!-- b000809 | contents | pages [19] -->
of the waves.

<!-- b000810 | contents | pages [19] -->
On the other hand, we can also place some stone or wooden supports in the

<!-- b000811 | contents | pages [19] -->
sandcastle, which can improve the sandcastle's ability to resist the waves. Alternatively,

<!-- b000812 | contents | pages [19] -->
we can also mix some clay into the sand. Because clay absorbs water less than sand,

<!-- b000813 | contents | pages [19] -->
and its internal friction angle is greater than sand. Therefore, adding other materials into

<!-- b000814 | contents | pages [19] -->
the sandcastle can improve the ability to resist sea waves and reduce the penetration of

<!-- b000815 | contents | pages [19] -->
waves.

<!-- b000816 | contents | pages [19] -->
⚫ We select six types of 3-dimensional geometric shape for analysis and comparison,

<!-- b000817 | contents | pages [19] -->
and finally determine that the cuboid is the optimal model by calculating the lasting

<!-- b000818 | contents | pages [19] -->
time of the sandcastle and the effective height of the wave action, which has a

<!-- b000819 | contents | pages [19] -->
certain rationality.

<!-- b000820 | contents | pages [19] -->
⚫ When analyzing the effect of the waves on the sandcastle, we establish a wave force

<!-- b000821 | contents | pages [19] -->
equation and perform a strong check using the Mohr-Coulomb Yielding Criteria

<!-- b000822 | contents | pages [19] -->
⚫ By consulting the data, Horton’s equation is used to measure the infiltration rate,

<!-- b000823 | contents | pages [19] -->
and the Van Genuchen Model is used to establish the relationship between the

<!-- b000824 | contents | pages [19] -->
infiltration rate and water content in sand.

<!-- b000825 | contents | pages [19] -->
⚫ The structure of the entire model is rigorous and reasonable. It is suitable for the

<!-- b000826 | contents | pages [19] -->
problem conditions and can be applied to beaches in any area. It has good

<!-- b000827 | contents | pages [19] -->
universality.

<!-- b000828 | contents | pages [19] -->
⚫ When considering wave motion, Airy Wave Theory simply considers the wave as

<!-- b000829 | contents | pages [19] -->
a sinusoidal form, but in fact, the amplitude of the wave is not constant as it moves

<!-- b000830 | contents | pages [19] -->
forward.

<!-- b000831 | contents | pages [19] -->
⚫ Water seepage is not a uniform process. The water content on the surface of an

<!-- b000832 | contents | pages [19] -->
object should be greater than the water content inside the object, but for the sake

<!-- b000833 | contents | pages [19] -->
of calculation, we consider this a uniform process.

<!-- b000834 | contents | pages [19] -->
⚫ Raindrops are uneven when falling and with the change of the tilt angle, it is

<!-- b000835 | contents | pages [19] -->
difficult to deduce its effect on the sandcastle by formula.

<!-- b000836 | contents | pages [19] -->
关注数学模型

<!-- b000837 | furniture | pages [19] -->
2

<!-- b000838 | furniture | pages [19] -->
MATHmodels

<!-- b000839 | furniture | pages [19] -->
获取更多资讯

<!-- b000840 | furniture | pages [20] -->
Team #2011873                                                                 Page 19 of 22

<!-- b000841 | contents | pages [20] -->
The Longest Lasting Sandcastle

<!-- b000842 | contents | pages [20] -->
The sea has infinite appeal to people. When you play on the coast, have you noticed

<!-- b000843 | contents | pages [20] -->
the countless sandcastles of different sizes and shapes on the beach? Some are broken

<!-- b000844 | contents | pages [20] -->
by the wash of the waves, while others remain intact. It is true that they may not be built

<!-- b000845 | contents | pages [20] -->
in time, but have you thought of any other factors that have caused this result and how

<!-- b000846 | contents | pages [20] -->
this will guide us in the construction of sandcastles?

<!-- b000847 | contents | pages [20] -->
In order to answer this question, we take Sandy Hooke in the United States as an

<!-- b000848 | contents | pages [20] -->
example to build a model of a sandcastle under the impact of waves and tide. Based on

<!-- b000849 | contents | pages [20] -->
this model, we studied sandcastles of six basic geometries of the same volume-cuboids,

<!-- b000850 | contents | pages [20] -->
cylinders, triangular prisms, triangular pyramids, quadrangular pyramids, and circular

<!-- b000851 | contents | pages [20] -->
pyramids.

<!-- b000852 | contents | pages [20] -->
We can see that the cuboid sandcastle can exist for the longest time. At the same

<!-- b000853 | contents | pages [20] -->
time, we should keep the width of the water front as small as possible while maintaining

<!-- b000854 | contents | pages [20] -->
a certain cross-section of the sandcastle. This will make the sandcastle exist longer.

<!-- b000855 | contents | pages [20] -->
In addition, we also considered that as the tide rises, the seawater will gradually

<!-- b000856 | contents | pages [20] -->
flood the sandcastle, causing the water content of the sandcastle to change, which will

<!-- b000857 | contents | pages [20] -->
affect the age of the sandcastle. Therefore, we studied the relationship between the

<!-- b000858 | contents | pages [20] -->
water content in the sandcastle and its age. We have reached the conclusion that the

<!-- b000859 | contents | pages [20] -->
optimal moisture content of the sandcastle should be 15%. When the water content is

<!-- b000860 | contents | pages [20] -->
too large, the sand castle will collapse under the impact of the waves. In fact, we will

<!-- b000861 | contents | pages [20] -->
not measure the specific value of sand moisture content during the construction of the

<!-- b000862 | contents | pages [20] -->
sand castle. Therefore, we can do a small experiment at the beach. we gradually add

<!-- b000863 | contents | pages [20] -->
water to the sand, and then see how tight they are. When we feel that the sand is the

<!-- b000864 | contents | pages [20] -->
strongest, stop adding water and use this as the material for building the sandcastle.

<!-- b000865 | contents | pages [20] -->
Finally, we studied the impact of rain on the sandcastle. On the one hand, the

<!-- b000866 | contents | pages [20] -->
infiltration of rainwater will increase the water content of the sandcastle. On the other

<!-- b000867 | contents | pages [20] -->
hand, rainwater on the sandcastle will have a strong effect on it. These will accelerate

<!-- b000868 | contents | pages [20] -->
the collapse of the sand castle so rain is not good for sand castles.

<!-- b000869 | contents | pages [20] -->
In short, in order to make the sandcastle have the longest lasting, we should choose

<!-- b000870 | contents | pages [20] -->
to use sand with a higher degree of tightness in rainless weather, build a cuboid as the

<!-- b000871 | contents | pages [20] -->
foundation of the sand castle, and make the width of the water front as narrow as

<!-- b000872 | contents | pages [20] -->
possible, so that we can build a "perfect" sandcastle. Of course, some people may say

<!-- b000873 | contents | pages [20] -->
that we can wrap a sandcastle with a plastic sheet, or add stones and soil to the sand.

<!-- b000874 | contents | pages [20] -->
关注数学模型

<!-- b000875 | furniture | pages [20] -->
2

<!-- b000876 | furniture | pages [20] -->
MATHmodels

<!-- b000877 | furniture | pages [20] -->
获取更多资讯

<!-- b000878 | furniture | pages [21] -->
Team #2011873                                                                 Page 20 of 22

<!-- b000879 | contents | pages [21] -->
These can also make the sandcastle exist longer. However, we do not recommend doing

<!-- b000880 | contents | pages [21] -->
this. After people leave, if these materials are not taken away in time, they will become

<!-- b000881 | contents | pages [21] -->
rubbish and pollute the sea. At the same time, stones on the beach will leave danger to

<!-- b000882 | contents | pages [21] -->
people who don't pay attention. When we enjoy life at the beach, we must remember to

<!-- b000883 | contents | pages [21] -->
protect the environment and others.

<!-- b000884 | contents | pages [21] -->
关注数学模型

<!-- b000885 | furniture | pages [21] -->
2

<!-- b000886 | furniture | pages [21] -->
MATHmodels

<!-- b000887 | furniture | pages [21] -->
获取更多资讯

<!-- b000888 | furniture | pages [22] -->
Team #2011873                                                                 Page 21 of 22

<!-- b000889 | contents | pages [22] -->
[1]  https://www.cnss.com.cn/tide/

<!-- b000890 | contents | pages [22] -->
[2]  https://en.wikipedia.org/wiki/Airy_wave_theory

<!-- b000891 | contents | pages [22] -->
[3]  https://en.wikipedia.org/wiki/Wind_wave

<!-- b000892 | contents | pages [22] -->
[4]  https://en.wikipedia.org/wiki/Morison_equatio

<!-- b000893 | contents | pages [22] -->
[5]  Zhang Boping, Wang Li, Yuan Haizhi. Quantitative analysis of the effect of water

<!-- b000894 | contents | pages [22] -->
content on the structural strength of loess [J]. Journal of Northwest Agricultural

<!-- b000895 | contents | pages [22] -->
University, 1994 (01): 54-60.

<!-- b000896 | contents | pages [22] -->
[6]  https://en.wikipedia.org/wiki/Mohr%E2%80%93Coulomb_theory?wprov=sfla1

<!-- b000897 | contents | pages [22] -->
[7]  https://wenku.baidu.com/view/4eb7356cbed5b9f3f80f1c1c.html

<!-- b000898 | contents | pages [22] -->
[8]  Chen Lei, Zhao Jian. Effect of moisture content on shear strength parameters of

<!-- b000899 | contents | pages [22] -->
clay in dumping ground [J]. Coal Technology, 2016, 35 (12): 170-172.

<!-- b000900 | contents | pages [22] -->
[9]  Fan Zhijie, Qu Jianjun, Zhou Huan. The relationship between the friction angle

<!-- b000901 | contents | pages [22] -->
in sand and the particle size, water content and natural slope angle [J] .China Desert,

<!-- b000902 | contents | pages [22] -->
2015,35 (02): 301-305.

<!-- b000903 | contents | pages [22] -->
[10]

<!-- b000904 | contents | pages [22] -->
https://en.wikipedia.org/wiki/Infiltration_(hydrology)

<!-- b000905 | contents | pages [22] -->
[11]

<!-- b000906 | contents | pages [22] -->
http://www.soilmanagementindia.com/soil/permeability-of-

<!-- b000907 | contents | pages [22] -->
soils/permeability-of-soil-definition-darcys-law-and-tests-soil-engineering/16472

<!-- b000908 | contents | pages [22] -->
[12]

<!-- b000909 | contents | pages [22] -->
Young-Suk Song, Kyeong-Su Kim, Sueng-Won Jeong, and Choon-Oh Lee.

<!-- b000910 | contents | pages [22] -->
Estimation on unsaturated characteristic curves of tailings obtained from waste

<!-- b000911 | contents | pages [22] -->
dump of imgi mine in busan.Journal of the Korean Geotechnical Society, 30:47–

<!-- b000912 | contents | pages [22] -->
58, 03 2014.

<!-- b000913 | contents | pages [22] -->
[13]

<!-- b000914 | contents | pages [22] -->
https://en.wikipedia.org/wiki/Water_retention_curve

<!-- b000915 | contents | pages [22] -->
[14]

<!-- b000916 | contents | pages [22] -->
Stingaciu, L. R., et al. "Determination of pore size distribution and hydraulic

<!-- b000917 | contents | pages [22] -->
properties using nuclear magnetic resonance relaxometry: A comparative study of

<!-- b000918 | contents | pages [22] -->
laboratory methods." Water Resources Research 46.11 (2010).

<!-- b000919 | contents | pages [22] -->
[15]

<!-- b000920 | contents | pages [22] -->
Zhang Junhong, Shi Xuchao, Zhang Xinjuan. Experimental Study on the

<!-- b000921 | contents | pages [22] -->
Influence of Water Content of Loess on Structure [J]. Henan Science, 2010, 28 (12):

<!-- b000922 | contents | pages [22] -->
1575-1578.

<!-- b000923 | contents | pages [22] -->
[16]

<!-- b000924 | contents | pages [22] -->
Yao Wenyi, Chen Guoxiang.Rainfall Drop Speed and Final Speed Formula

<!-- b000925 | contents | pages [22] -->
[J] .Journal of Hohai University, 1993 (03): 21-27.

<!-- b000926 | contents | pages [22] -->
[17]

<!-- b000927 | contents | pages [22] -->
Zhao Xiaojia, Wang Shaopo, Yu He, Qiu Chunsheng, Sun Liping, Wang

<!-- b000928 | contents | pages [22] -->
Chenchen, Zhao Lejun, Song Xiancai.Characteristics of Erosion and Pollution

<!-- b000929 | contents | pages [22] -->
Erosion by Rainfall and Runoff on Typical Underlying Surfaces in Tianjin City

<!-- b000930 | contents | pages [22] -->
Center [J] .Environmental Engineering, 2019,37 (07): 34-38 + 87 .

<!-- b000931 | contents | pages [22] -->
关注数学模型

<!-- b000932 | furniture | pages [22] -->
2

<!-- b000933 | furniture | pages [22] -->
MATHmodels

<!-- b000934 | furniture | pages [22] -->
获取更多资讯

<!-- b000935 | furniture | pages [23] -->
Team #2011873                                                                 Page 22 of 22

<!-- b000936 | contents | pages [23] -->
[18]

<!-- b000937 | contents | pages [23] -->
Estela Nadal-Romero, Teodoro Lasanta, David Regües, N. Lana-

<!-- b000938 | contents | pages [23] -->
Renault, and Artemi Cerdà. Hydrological response and sediment production unde

<!-- b000939 | contents | pages [23] -->
r different land cover in abandoned farmland fields in a mediterranean mountain e

<!-- b000940 | contents | pages [23] -->
nvironment. Boletín de la Asociación de Geógrafos Españoles, 55:303-

<!-- b000941 | contents | pages [23] -->
323, 01 2011.

<!-- b000942 | contents | pages [23] -->
关注数学模型

<!-- b000943 | furniture | pages [23] -->
2

<!-- b000944 | furniture | pages [23] -->
MATHmodels

<!-- b000945 | furniture | pages [23] -->
获取更多资讯
