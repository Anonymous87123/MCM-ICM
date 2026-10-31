# P-B-2020-2010821-2af4f390

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2020

<!-- b000003 | title | pages [1] -->
B

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | furniture | pages [1] -->
2010821

<!-- b000006 | prose | pages [1] -->
MCM/ICM

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
How to build a durable sandcastle foundation?

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In recent years, as sand castle art has become more popular, more and more ingenious sand castle art works have been created. However, perfect works of art will disappear, and how to be preserved for a long time becomes an obstacle to the advancement of Sandcastle art.

<!-- b000011 | prose | pages [1] -->
First, the optimal geometry considering the dual erosion effects of waves and tides is determined. On the basis of reasonably limiting the shape selection range,by establishing the Dynamic Model of

<!-- b000012 | prose | pages [1] -->
the Sandcastle Foundation based on the evaluation index of the comprehensive sand and sand carrying capacity of waves and tides, we use COMSOL to accurately simulate the movement state of the sand castle foundation. On this basis, by creating the Sandcastle Foundation Damage Index, we reasonably determine the duration of the sandcastle. Finally, we use a Discrete Global Optimization Algorithm Based on Successive Descent Methods to determine the shape of the optimal sandcastle foundation as a cylinder.

<!-- b000013 | prose | pages [1] -->
Secondly, the optimal water-sand mixing ratio is determined. Based on Model 1, a model of Water-sand Aggregation-water-sand Ratio Relationship was first established. By limiting the allowed degree of polymerization, the water-sand ratio is limited to a reasonable range. We again use the discrete global optimization algorithm based on the successive descent method to efficiently find the optimal water-sand mix ratio of 0.739.

<!-- b000014 | prose | pages [1] -->
Further, an optimal geometry considering rain erosion is determined. We define the sandcastle collapse limit coefficient, and comprehensively establish the Rainwater Erosion Resistance Quantification Model by integrating the ability to resist rainwater infiltration and the evacuation ratio of the sandcastle structure. Further, A Quantified Model of Sandcastle's Ability to Resist Wave Erosion was established. Considering two indicators of anti-erosion ability and establishing a fuzzy comprehensive evaluation model, we determine that the optimal shape is still a cylinder.

<!-- b000015 | prose | pages [1] -->
Finally, we use the method of humidifying and spraying the adhesive when the air humidity is the lowest to improve the stability of the sand castle foundation. A Humidity Prediction Model Based on the RBF Neural Network Algorithm was established, and we used the model to test the humidity of Venice Beach on August 1. Based on the air humidity data obtained in the previous month, we divided the weather conditions into sunny and cloudy days, and predicted the air humidity trends for sunny and cloudy days on August 1, respectively. Finally, we decided to humidify the sandcastle foundation and spray the adhesive at 13:30 on a cloudy day and 13:00 on a sunny day.

<!-- b000016 | furniture | pages [1] -->
关注数学模型

<!-- b000017 | furniture | pages [1] -->
2

<!-- b000018 | furniture | pages [1] -->
MATHmodels

<!-- b000019 | furniture | pages [1] -->
获取更多资讯

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1. Introduction............................................................................................................................................3

<!-- b000022 | contents | pages [2] -->
1.1 Background.....................................................................................................................................3

<!-- b000023 | contents | pages [2] -->
1.2 Restatement of the Problem............................................................................................................3

<!-- b000024 | contents | pages [2] -->
2.Assumption and Justification................................................................................................................ 3

<!-- b000025 | contents | pages [2] -->
3.Glossary and Notation............................................................................................................................4

<!-- b000026 | contents | pages [2] -->
3.1 Glossary..........................................................................................................................................4

<!-- b000027 | contents | pages [2] -->
3.2 Notation..........................................................................................................................................4

<!-- b000028 | contents | pages [2] -->
4. Optimal Shape Model Based on Sandcastle Foundation Dynamics Model......................................4

<!-- b000029 | contents | pages [2] -->
4.1 Model Overview.............................................................................................................................4

<!-- b000030 | contents | pages [2] -->
4.2 Quantitative model of sand-bearing capacity................................................................................5

<!-- b000031 | contents | pages [2] -->
4.3 Sandcastle Foundation dynamics equation model.........................................................................5

<!-- b000032 | contents | pages [2] -->
4.4 Solution of Sandcastle Foundation Dynamics Equation Model....................................................6

<!-- b000033 | contents | pages [2] -->
4.5 Geometric Shape Solving Model Based on Discrete Global Optimization Algorithm..................9

<!-- b000034 | contents | pages [2] -->
5. Optimal water and sand ratio model................................................................................................. 11

<!-- b000035 | contents | pages [2] -->
5.1 Model Overview...........................................................................................................................11

<!-- b000036 | contents | pages [2] -->
5.2 Quantitative model of Water and sand polymerization degree.................................................... 11

<!-- b000037 | contents | pages [2] -->
5.3 Solving the Model........................................................................................................................ 12

<!-- b000038 | contents | pages [2] -->
6.Fuzzy comprehensive evaluation model based on rain erosion resistance......................................13

<!-- b000039 | contents | pages [2] -->
6.1 Model Overview...........................................................................................................................13

<!-- b000040 | contents | pages [2] -->
6.2 Evaluation model for rain erosion resistance.............................................................................. 13

<!-- b000041 | contents | pages [2] -->
6.3 Optimal Shape Fuzzy Comprehensive Evaluation Model............................................................14

<!-- b000042 | contents | pages [2] -->
7. Humidity Prediction Model Based on RBF Neural Network Algorithm....................................... 16

<!-- b000043 | contents | pages [2] -->
7.1 Model Overviw.............................................................................................................................16

<!-- b000044 | contents | pages [2] -->
7.2 Model Preparation........................................................................................................................ 16

<!-- b000045 | contents | pages [2] -->
7.3 RBF neural network algorithm.....................................................................................................17

<!-- b000046 | contents | pages [2] -->
8. Sensitivity Analysis.............................................................................................................................. 18

<!-- b000047 | contents | pages [2] -->
8.1 Sensitivity Analysis of Most Shaped Model ............................................................................... 18

<!-- b000048 | contents | pages [2] -->
8.2 Sensitivity Analysis of Optimal Water-Sand Mixing Model....................................................... 18

<!-- b000049 | contents | pages [2] -->
8.3 Sensitivity Analysis of A Fuzzy Comprehensive Evaluation Mode............................................ 20

<!-- b000050 | contents | pages [2] -->
8.4 Sensitivity Analysis of Sandcastle warning protection Model.....................................................20

<!-- b000051 | contents | pages [2] -->
9. Evaluation and Promotion of Model..................................................................................................21

<!-- b000052 | contents | pages [2] -->
9.1 Strength and Weakness.................................................................................................................21

<!-- b000053 | contents | pages [2] -->
9.2 Promotion..................................................................................................................................... 22

<!-- b000054 | contents | pages [2] -->
10. Conclusions.........................................................................................................................................22

<!-- b000055 | contents | pages [2] -->
References..................................................................................................................................................23

<!-- b000056 | contents | pages [2] -->
Memo.........................................................................................................................................................24

<!-- b000057 | contents | pages [2] -->
Appendix....................................................................................................................................................25

<!-- b000058 | furniture | pages [2] -->
关注数学模型

<!-- b000059 | furniture | pages [2] -->
2

<!-- b000060 | furniture | pages [2] -->
MATHmodels

<!-- b000061 | furniture | pages [2] -->
获取更多资讯

<!-- b000062 | furniture | pages [3] -->
Team # 2010821

<!-- b000063 | heading | pages [3] -->
1. Introduction

<!-- b000064 | heading | pages [3] -->
1.1 Background

<!-- b000065 | furniture | pages [3] -->
Page 3 of 24

<!-- b000066 | prose | pages [3] -->
Nowadays, people always face heavy schooling or busy work, and spending some time at the beach allows people to enjoy the cool sea breeze, warm sunshine, and soft beaches. Therefore, more and more people choose to go to the beach for leisure. Building sandcastles is a must-do item for beach leisure. It can develop children's creativity and reduce adults' stress to a great extent. When people build sandcastles, they always want their sandcastles to be beautiful and to last longer. Therefore, it is necessary to study how to keep the sandcastle on the beach for the longest time.

<!-- b000067 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000068 | prose | pages [3] -->
Building sandcastles is one of the most popular activities item for children on the beach. Every child wants his sandcastle to last for a long time on the beach. Therefore, we were asked to study the persistent retention of sandcastles on the beach. The specific issues are as follows:

<!-- b000069 | prose | pages [3] -->
Below environmental factors are assumed to be the same, such as: the distance of the beach from  the water, the kind of sand, the amount of sand, the same water-sand ratio. We were asked to build a model under the action of waves and tides to explore the basic geometry of the sandcastle that can last for the longest time on the beach. Without using any additional additives, how to change the water-sand ratio of the sandcastle  foundation can make our sandcastle last for the longest time on the beach. Built on the original model, we have considered the impact of rain on the foundation of the  sandcastle, and upgrade and optimize the model to further explore the optimal geometry of the sandcastle. By consulting some relevant literatures, other strategies have been investigated to improve the  retention time of sandcastles.

<!-- b000070 | heading | pages [3] -->
2.Assumption and Justification

<!-- b000071 | prose | pages [3] -->
We make some general assumptions to simplify our model. These assumptions and corresponding justification are listed below:

<!-- b000072 | prose | pages [3] -->
It is assumed that the base area and height of each considered shape are the same, and that there is  no significant difference in the sand quality and sand quantity of our sandcastle foundation. Sandcastle foundations are built at approximately the same distance from the water.  In the process of natural erosion, ignore the situation of huge waves and winds sweeping the  sandcastle far from the original location. We only consider the impact of waves, tides and rain on the water-sand ratio of the sandcastle  foundation. The sand particles at the sandcastle foundation are evenly distributed.  Assume that people will spray the adhesive in time after the warning occurs, and the adhesive  viscosity lasts at least 8 hours.

<!-- b000073 | prose | pages [3] -->
More detailed assumptions will be listed if needed.

<!-- b000074 | furniture | pages [3] -->
关注数学模型

<!-- b000075 | furniture | pages [3] -->
2

<!-- b000076 | furniture | pages [3] -->
MATHmodels

<!-- b000077 | furniture | pages [3] -->
获取更多资讯

<!-- b000078 | furniture | pages [4] -->
Team # 2010821

<!-- b000079 | heading | pages [4] -->
3.Glossary and Notation

<!-- b000080 | heading | pages [4] -->
3.1 Glossary

<!-- b000081 | furniture | pages [4] -->
Page 4 of 24

<!-- b000082 | prose | pages [4] -->
Wave current: refers to the combined effect of waves and tides.  Damage index: It takes the change of the base area and height of the sandcastle as a measuring  factor to describe the damage degree of the sandcastles.

<!-- b000083 | heading | pages [4] -->
3.2 Notation

<!-- b000084 | caption | pages [4] -->
Table 1 Notation

<!-- b000085 | heading | pages [4] -->
Symbols

<!-- b000086 | prose | pages [4] -->
sF

<!-- b000087 | prose | pages [4] -->
Definition

<!-- b000088 | prose | pages [4] -->
sand-bearing capacity

<!-- b000089 | prose | pages [4] -->
G

<!-- b000090 | prose | pages [4] -->
Q

<!-- b000091 | prose | pages [4] -->
Damage Index

<!-- b000092 | prose | pages [4] -->
Water and sand polymerization degree

<!-- b000093 | prose | pages [4] -->
n p

<!-- b000094 | prose | pages [4] -->
i F

<!-- b000095 | prose | pages [4] -->
Water-sand ratio

<!-- b000096 | prose | pages [4] -->
ability to resist rainwater infiltration u

<!-- b000097 | prose | pages [4] -->
sandcastle structure evacuation ratio i R

<!-- b000098 | prose | pages [4] -->
i rain erosion resistance H1

<!-- b000099 | prose | pages [4] -->
i wave current erosion resistance H 2

<!-- b000100 | prose | pages [4] -->
 g Neural Network Radial Basis Function

<!-- b000101 | heading | pages [4] -->
4. Optimal Shape Model Based on Sandcastle Foundation Dynamics

<!-- b000102 | heading | pages [4] -->
Model

<!-- b000103 | heading | pages [4] -->
4.1 Model Overview

<!-- b000104 | prose | pages [4] -->
In terms of shape selection, considering the common sandcastle basic shapes that people are accustomed to using, we only consider the most suitable ones from a cuboid with a certain aspect ratio, an elliptical cylinder with a certain aspect ratio, and a sector with a certain radius and arc length ratio. Excellent shape.First, we have established a model for assessing the sand-bearing capacity of waves. Based on this, the basic dynamics equation of the sandcastle foundation is established. Secondly, by creating a sandcastle foundation damage index, we have determined the duration of a sandcastle of a

<!-- b000105 | furniture | pages [4] -->
关注数学模型

<!-- b000106 | furniture | pages [4] -->
2

<!-- b000107 | furniture | pages [4] -->
MATHmodels

<!-- b000108 | furniture | pages [4] -->
获取更多资讯

<!-- b000109 | furniture | pages [5] -->
Team # 2010821

<!-- b000110 | furniture | pages [5] -->
Page 5 of 24

<!-- b000111 | prose | pages [5] -->
specific shape. Further, based on the duration of some specific shape sandcastles, we have used a discrete global optimization algorithm based on successive descent methods to determine the optimal sandcastle shape in the global state[1].

<!-- b000112 | heading | pages [5] -->
4.2 Quantitative model of sand-bearing capacity

<!-- b000113 | prose | pages [5] -->
Because wave and tide are the two main driving forces in the sand movement of sandcastles, we first have considered how the sandcastles are impacted under the action of waves and tides, and choose to define this ability using the capacity of sand-bearing.

<!-- b000114 | prose | pages [5] -->
Considering tidal and wave sand-bearing capacity:

<!-- b000115 | prose | pages [5] -->
C  * (1) C C C  * * * C W The capacity of sand-bearing under tide effect can be expressed as: 

<!-- b000116 | prose | pages [5] -->
C

<!-- b000117 | prose | pages [5] -->


<!-- b000118 | prose | pages [5] -->


<!-- b000119 | prose | pages [5] -->
*

<!-- b000120 | prose | pages [5] -->
C C

<!-- b000121 | prose | pages [5] -->
1

<!-- b000122 | prose | pages [5] -->
Where,

<!-- b000123 | prose | pages [5] -->
 

<!-- b000124 | prose | pages [5] -->
n n V

<!-- b000125 | prose | pages [5] -->
2 2

<!-- b000126 | prose | pages [5] -->
u v

<!-- b000127 | prose | pages [5] -->


<!-- b000128 | prose | pages [5] -->
p p

<!-- b000129 | prose | pages [5] -->
(2)

<!-- b000130 | prose | pages [5] -->
2

<!-- b000131 | prose | pages [5] -->
n

<!-- b000132 | prose | pages [5] -->
 

<!-- b000133 | prose | pages [5] -->
C h

<!-- b000134 | prose | pages [5] -->


<!-- b000135 | prose | pages [5] -->
p z w s

<!-- b000136 | prose | pages [5] -->
n represents the initial value of the water-sand ratio of the sandcastle foundation, which is p

<!-- b000137 | prose | pages [5] -->
determined by the volume ratio;V is the initial value of the sandy volume of the sandcastle foundation;

<!-- b000138 | prose | pages [5] -->
u and v represents the components of the water flow velocity x and y the sum of the waves under the is the height of seawater level; action of waves and tides;

<!-- b000139 | prose | pages [5] -->
h w

<!-- b000140 | prose | pages [5] -->
indicates sand-bearing speed. s

<!-- b000141 | prose | pages [5] -->
is the positive definite coefficient; C

<!-- b000142 | prose | pages [5] -->
Regarding the capacity of sand-bearing under the action of waves, we consider the unbroken wave  and the broken wave respectively, which can be expressed as:

<!-- b000143 | prose | pages [5] -->
n V

<!-- b000144 | prose | pages [5] -->
p

<!-- b000145 | prose | pages [5] -->
C  

<!-- b000146 | prose | pages [5] -->
* 1

<!-- b000147 | prose | pages [5] -->
W

<!-- b000148 | prose | pages [5] -->
1

<!-- b000149 | prose | pages [5] -->
n

<!-- b000150 | prose | pages [5] -->
 3

<!-- b000151 | prose | pages [5] -->
T gh

<!-- b000152 | prose | pages [5] -->
p

<!-- b000153 | prose | pages [5] -->
Where,

<!-- b000154 | prose | pages [5] -->
3

<!-- b000155 | prose | pages [5] -->
1

<!-- b000156 | prose | pages [5] -->
f f H

<!-- b000157 | prose | pages [5] -->
D

<!-- b000158 | prose | pages [5] -->
(3)

<!-- b000159 | prose | pages [5] -->
 

<!-- b000160 | prose | pages [5] -->
W rms

<!-- b000161 | prose | pages [5] -->
B

<!-- b000162 | prose | pages [5] -->
 

<!-- b000163 | prose | pages [5] -->
2 3 1

<!-- b000164 | prose | pages [5] -->
n

<!-- b000165 | prose | pages [5] -->
h

<!-- b000166 | prose | pages [5] -->
  sinh

<!-- b000167 | prose | pages [5] -->
kh

<!-- b000168 | prose | pages [5] -->
 

<!-- b000169 | prose | pages [5] -->
p

<!-- b000170 | prose | pages [5] -->
w s

<!-- b000171 | prose | pages [5] -->
s s w w

<!-- b000172 | prose | pages [5] -->
are respectively the positive definite coefficients of the unbroken wave and the broken and  1 2

<!-- b000173 | prose | pages [5] -->
wave;

<!-- b000174 | prose | pages [5] -->
wf represents the wave friction coefficient;

<!-- b000175 | prose | pages [5] -->
H is the mean square wave height, 2 H H  ， rms s rms

<!-- b000176 | prose | pages [5] -->
H Is the effective wave height; T is the wave period; k is the wave quantization value of one period; s

<!-- b000177 | prose | pages [5] -->
D represents the wave energy dissipation due to the wave breaking. B We build the capacity of sand-bearing sF as: 

<!-- b000178 | prose | pages [5] -->
F  s Where,

<!-- b000179 | prose | pages [5] -->
 indicates the sand settling coefficient. r

<!-- b000180 | prose | pages [5] -->
  (4) C V    * r s

<!-- b000181 | heading | pages [5] -->
4.3 Sandcastle Foundation dynamics equation model

<!-- b000182 | prose | pages [5] -->
We use the right-angle vertex of the three-dimensional geometry as the coordinate center to and h over timet of our establish a three-dimensional right-angle coordinate system. Then,changes of x, y sandcastle foundation satisfy the following equations in dynamic

<!-- b000183 | furniture | pages [5] -->
关注数学模型

<!-- b000184 | furniture | pages [5] -->
2

<!-- b000185 | furniture | pages [5] -->
MATHmodels

<!-- b000186 | furniture | pages [5] -->
获取更多资讯

<!-- b000187 | furniture | pages [6] -->
Team # 2010821

<!-- b000188 | prose | pages [6] -->
     

<!-- b000189 | prose | pages [6] -->
hV huV hvV

<!-- b000190 | prose | pages [6] -->
     

<!-- b000191 | prose | pages [6] -->
t x y

<!-- b000192 | prose | pages [6] -->
  

<!-- b000193 | prose | pages [6] -->


<!-- b000194 | prose | pages [6] -->
Where,

<!-- b000195 | furniture | pages [6] -->
Page 6 of 24

<!-- b000196 | prose | pages [6] -->
   

<!-- b000197 | prose | pages [6] -->


<!-- b000198 | prose | pages [6] -->


<!-- b000199 | prose | pages [6] -->
hV hV

<!-- b000200 | prose | pages [6] -->
 

<!-- b000201 | prose | pages [6] -->


<!-- b000202 | prose | pages [6] -->


<!-- b000203 | prose | pages [6] -->


<!-- b000204 | prose | pages [6] -->
 

<!-- b000205 | prose | pages [6] -->


<!-- b000206 | prose | pages [6] -->
 v v F

<!-- b000207 | prose | pages [6] -->


<!-- b000208 | prose | pages [6] -->


<!-- b000209 | prose | pages [6] -->
(5)

<!-- b000210 | prose | pages [6] -->
 

<!-- b000211 | prose | pages [6] -->
x y s x x x y y

<!-- b000212 | prose | pages [6] -->


<!-- b000213 | prose | pages [6] -->
 

<!-- b000214 | prose | pages [6] -->
 

<!-- b000215 | prose | pages [6] -->


<!-- b000216 | prose | pages [6] -->


<!-- b000217 | prose | pages [6] -->
yv is the horizontal diffusion coefficient. h indicates the height of the sandcastle foundation;

<!-- b000218 | prose | pages [6] -->
xv and

<!-- b000219 | prose | pages [6] -->
In the dynamic simulation process, we give the constraint that the normal flux is 0 to determine the solid boundary condition as:

<!-- b000220 | prose | pages [6] -->


<!-- b000221 | prose | pages [6] -->


<!-- b000222 | prose | pages [6] -->


<!-- b000223 | prose | pages [6] -->
Where,

<!-- b000224 | prose | pages [6] -->


<!-- b000225 | prose | pages [6] -->
V V (6)

<!-- b000226 | prose | pages [6] -->
0 

<!-- b000227 | prose | pages [6] -->
n n

<!-- b000228 | prose | pages [6] -->
represents the total flux through the sandcastle foundation; nrepresents the normal vector.

<!-- b000229 | prose | pages [6] -->


<!-- b000230 | prose | pages [6] -->
At the same time, we give the time course of the sand volume as the open boundary condition:

<!-- b000231 | prose | pages [6] -->
V V    t , , x x y (7)

<!-- b000232 | heading | pages [6] -->
4.4 Solution of Sandcastle Foundation Dynamics Equation Model

<!-- b000233 | heading | pages [6] -->
4.4.1 Solution of Cuboid Dynamics Simulation

<!-- b000234 | prose | pages [6] -->
Step1. Initialize the parameters of the sandcastle foundation dynamics equation. We take the  optimal shape of a cuboid as an example and define the aspect ratio of the bottom of the cuboid as x, y . The initial values of its shape factor, which is : e l w 1  in the equation correspond to , l, w respectively. In combination with relevant literature, the parameter initialization values in the given dynamic equation are shown in the following table

<!-- b000235 | caption | pages [6] -->
Table 2 Parameter Determination

<!-- b000236 | prose | pages [6] -->
Numerical value

<!-- b000237 | heading | pages [6] -->
symbol

<!-- b000238 | prose | pages [6] -->
Numerical value

<!-- b000239 | heading | pages [6] -->
symbol

<!-- b000240 | prose | pages [6] -->
  0.023 C 1

<!-- b000241 | prose | pages [6] -->
C  0.249 2 z

<!-- b000242 | prose | pages [6] -->
Wf  1.489 s

<!-- b000243 | heading | pages [6] -->
symbol

<!-- b000244 | prose | pages [6] -->
Numerical value

<!-- b000245 | prose | pages [6] -->
0.300 5.000 T

<!-- b000246 | prose | pages [6] -->
H 0.001 5.185 rms

<!-- b000247 | prose | pages [6] -->
D 1.570 6.301 B

<!-- b000248 | caption | pages [6] -->
Table 3 Assignment Table for Initialization Variables

<!-- b000249 | heading | pages [6] -->
symbol

<!-- b000250 | prose | pages [6] -->
Numerical value

<!-- b000251 | prose | pages [6] -->
h 900 w

<!-- b000252 | prose | pages [6] -->
u 30

<!-- b000253 | prose | pages [6] -->
v 30

<!-- b000254 | prose | pages [6] -->
V 100 1

<!-- b000255 | heading | pages [6] -->
symbol

<!-- b000256 | prose | pages [6] -->
Numerical value

<!-- b000257 | prose | pages [6] -->
n 6.0 p

<!-- b000258 | prose | pages [6] -->
x 1.0

<!-- b000259 | prose | pages [6] -->
y 1.0

<!-- b000260 | furniture | pages [6] -->
关注数学模型

<!-- b000261 | furniture | pages [6] -->
2

<!-- b000262 | furniture | pages [6] -->
MATHmodels

<!-- b000263 | furniture | pages [6] -->
获取更多资讯

<!-- b000264 | furniture | pages [7] -->
Team # 2010821

<!-- b000265 | furniture | pages [7] -->
Page 7 of 24

<!-- b000266 | prose | pages [7] -->
FIG 1. Cuboid simulation diagram when t is equal to zero

<!-- b000267 | prose | pages [7] -->
We use COMSOL to solve the dynamic equations and simulate the pressure effect of wave current 0.1 e cuboid. The pressure distribution at time on the bottom surface of 1  shown in the figure 0 t  above is obtained. Among them, the wave current starts from the red part and the pressure gradually decreases.

<!-- b000268 | prose | pages [7] -->
Step2. Establish a damage index indicator model. In order to describe the degree of damage of  the sandcastle and better explain the meaning of duration, we take the change in base area and height as the measuring factor, and give the definition of damage index as

<!-- b000269 | prose | pages [7] -->
G   Where, (8) S h      s s h

<!-- b000270 | prose | pages [7] -->
represent respectively the increase in the bottom area of the sandcastle and the decrease and S h in the minimum height of the sandcastle, over a period of time;

<!-- b000271 | prose | pages [7] -->
and are the influence factors of the s h change in the bottom area and the height, respectively.

<!-- b000272 | prose | pages [7] -->
It should be noted that in the real practice, changes are both uncertain of base areas and heights. The sandcastle foundation undergoes the process of waves and tidal effects. The sand at the bottom layer will spread under the effect of erosion, resulting in a reduction in the height of the sandcastle foundation and an increase in its bottom area. The impact of the simplified process on the sandcastle is shown in FIG 1. below:

<!-- b000273 | prose | pages [7] -->
FIG 2. Simplified model of sandcastle foundation erosion

<!-- b000274 | furniture | pages [7] -->
关注数学模型

<!-- b000275 | furniture | pages [7] -->
2

<!-- b000276 | furniture | pages [7] -->
MATHmodels

<!-- b000277 | furniture | pages [7] -->
获取更多资讯

<!-- b000278 | furniture | pages [8] -->
Team # 2010821

<!-- b000279 | furniture | pages [8] -->
Page 8 of 24

<!-- b000280 | prose | pages [8] -->
The cubic three-dimensional geometry in the figure represents the original state of the sandcastle foundation, and the dashed line represents the existing state after the sandcastle has been eroded. The increase of the base area and the decrease of the height of the existing state compared with the original state are the quantity of the damage index.

<!-- b000281 | prose | pages [8] -->
Step3. Find the relationship between the damage index over time. We obtain that the sand level  is eroded by the waves and tides for a period of time, and the water level at the new time and ' h w

<!-- b000282 | prose | pages [8] -->
' n , and the wave current velocity in the x and y directions are 'u and 'v , the water-sand ratio S  p

<!-- b000283 | prose | pages [8] -->
of the sandcastle foundation. We discretize the time, set the completion time of the and h  is the initial time point, and then take the time points at equal sandcastle to zero, that is, 0 t  intervals to draw a scatter plot as shown in the figure.

<!-- b000284 | prose | pages [8] -->
FIG 3. Damage index over time

<!-- b000285 | prose | pages [8] -->
The diagram illustrates the damage indicator function established and the line connecting the points at equal intervals. It should be shown that the discrete points after point B are almost on the same horizontal line. As a result, it is revealed that the sandcastle is completely damaged, with a . Based on that, damage factor is defined with coefficient corresponding damage index G max , it is considered that the sandcastle has been damaged to the being , that is, when 0.52 0.52G G    max maximum bearing degree. On this basis, we take point A as the critical time point, which refers to the corresponding time to the maximum degree of damage which could bear, and the time corresponding to that point is the duration . T/ day At the same time, we define the duration of any sandcastle foundation constructed from a three- dimensional geometric shape from the stacking to the critical time point as T . The longer the duration, the better the shape corresponds to the sandcastle foundation.

<!-- b000286 | prose | pages [8] -->
We simulate the damage index and duration of 10 groups of cuboids with different shape 1e under the action of waves and tides. It should be noted that the 10 sets of data we have obtained factors are only the first step in obtaining the global optimal solution. The next step is shown in the next model. The 10 sets of data are shown in the following table:

<!-- b000287 | furniture | pages [8] -->
关注数学模型

<!-- b000288 | furniture | pages [8] -->
2

<!-- b000289 | furniture | pages [8] -->
MATHmodels

<!-- b000290 | furniture | pages [8] -->
获取更多资讯

<!-- b000291 | furniture | pages [9] -->
Team # 2010821

<!-- b000292 | furniture | pages [9] -->
Page 9 of 24

<!-- b000293 | caption | pages [9] -->
Table 4 Corresponding duration of cuboids with different aspect ratios

<!-- b000294 | prose | pages [9] -->
Shape factor Duration

<!-- b000295 | prose | pages [9] -->
1.0 2.5

<!-- b000296 | prose | pages [9] -->
1.5 2.4

<!-- b000297 | prose | pages [9] -->
2.0 2.1

<!-- b000298 | prose | pages [9] -->
2.5 2

<!-- b000299 | prose | pages [9] -->
3.0 1.8

<!-- b000300 | prose | pages [9] -->
Shape factor Duration

<!-- b000301 | prose | pages [9] -->
3.5 1.2

<!-- b000302 | prose | pages [9] -->
4.0 1.4

<!-- b000303 | prose | pages [9] -->
4.5 2.8

<!-- b000304 | prose | pages [9] -->
5.0 2.0

<!-- b000305 | prose | pages [9] -->
5.5 2.6

<!-- b000306 | heading | pages [9] -->
4.4.2 Simulation solution of dynamics equations of elliptic cylinder and sector cylinder

<!-- b000307 | prose | pages [9] -->
We consider the damage index and duration corresponding to the parameters of the other two common three-dimensional geometric shapes. The detailed data results of the simulation are shown in the appendix.

<!-- b000308 | prose | pages [9] -->
We define the ratio of the long axis to the short axis of the ellipse as its shape factor, which  . Based on this, a dynamic equation solving model is established, and the simulation is : e a b 2  1 e simulation graph at is shown as follows: 2  Taking the ratio of the radius r of the sector cylinder to the arc length l as the coefficient  3e , we as an example to make the following simulation: take the sector cylinder of 1 e 3  

<!-- b000309 | prose | pages [9] -->
FIG 4. Cylinder simulation diagram FIG 5. Sector cylinder simulation diagram

<!-- b000310 | heading | pages [9] -->
4.5 Geometric Shape Solving Model Based on Discrete Global Optimization

<!-- b000311 | heading | pages [9] -->
Algorithm

<!-- b000312 | heading | pages [9] -->
4.5.1 Model Overview

<!-- b000313 | prose | pages [9] -->
  By solving the dynamic equation of the sandcastle foundation, we can get the duration of sandcastle foundation shape under the control of 3,2,1 Ti i    3,2,1 ei i . However, in order to find the optima 

<!-- b000314 | furniture | pages [9] -->
关注数学模型

<!-- b000315 | furniture | pages [9] -->
2

<!-- b000316 | furniture | pages [9] -->
MATHmodels

<!-- b000317 | furniture | pages [9] -->
获取更多资讯

<!-- b000318 | furniture | pages [10] -->
Team # 2010821

<!-- b000319 | furniture | pages [10] -->
Page 10 of 24

<!-- b000320 | prose | pages [10] -->
iT , we try to establish an optimal three-dimensional geometric model with a Discrete Global value of Optimization Algorithm as the core. On this basis, we can find the optimal coefficient value

<!-- b000321 | prose | pages [10] -->
  of any of the three shapes, so that the shape we choose has the longest duration. 3,2,1 ei i 

<!-- b000322 | heading | pages [10] -->
4.5.2 Model establishment and solution

<!-- b000323 | prose | pages [10] -->
We still take the cuboid as an example. Through simulation, we can obtain the duration under multiple sets of coefficients. In this regard, we use these data to deduce the Discrete Global Optimization Algorithm based on the successive descent method. The specific steps are as follows:

<!-- b000324 | prose | pages [10] -->
Step1. Successive Descent method to find discrete local minimum points. (1) set the set E as the Cuboid shape factor selection point, satisfy E     :

<!-- b000325 | prose | pages [10] -->
\   f e d f e d n if , let , cycle this      R k k step;determine whether is 0 to determine whether to update the  ke discrete local minima, after ,we get the discrete global minima . Step2. Construct a discrete fill function. Let initialization conditions    -5 , ,2,1 , 10 V V p j n     , , ;

<!-- b000326 | prose | pages [10] -->
.   0.01 1 q r 0    0 j

<!-- b000327 | prose | pages [10] -->
The constructed discrete fill function is:

<!-- b000328 | prose | pages [10] -->
   , , , F e e q r k k

<!-- b000329 | prose | pages [10] -->
Step3 .If  ke

<!-- b000330 | prose | pages [10] -->
1        max 0, f e f e r      (9) q k k  q e e   k k

<!-- b000331 | prose | pages [10] -->
, the algorithm is terminated, and local r   can be used as the discrete global minimum, otherwise, variable the next step is performed.

<!-- b000332 | prose | pages [10] -->
Step4. If Step5. If D   , go to step 6, otherwise, go to the next step.

<!-- b000333 | prose | pages [10] -->
10 r  r , then make , , 2 10 10 q  0q q  

<!-- b000334 | prose | pages [10] -->
10 q  q , go to the step 2, otherwise, let D  D 0 , go to the step2 Step6. Take any direction , so that , enter d  D D D d   the inner loop phase, change the initial value of D , and cycle the corresponding steps. When the parameter r are sufficiently small, it is believed that there is no better local minimum point in the selected point set E .

<!-- b000335 | prose | pages [10] -->
From the dynamic model, we can get the corresponding duration T for each assignment, and with

<!-- b000336 | prose | pages [10] -->
as the objective function, we optimize it by the algorithm: 1 K T 

<!-- b000337 | prose | pages [10] -->
min K    , n f e e R    (10) k k

<!-- b000338 | prose | pages [10] -->
1 max T  (11) K

<!-- b000339 | prose | pages [10] -->
Similarly to the other two shape models, we can use the Discrete Global Optimization Algorithm to find the maximum T in the duration controlled by the three shape scale as shown in the following table:

<!-- b000340 | furniture | pages [10] -->
关注数学模型

<!-- b000341 | furniture | pages [10] -->
2

<!-- b000342 | furniture | pages [10] -->
MATHmodels

<!-- b000343 | furniture | pages [10] -->
获取更多资讯

<!-- b000344 | furniture | pages [11] -->
Team # 2010821

<!-- b000345 | furniture | pages [11] -->
Page 11 of 24

<!-- b000346 | caption | pages [11] -->
Table 5 Table of the best shape parameters for the three shapes

<!-- b000347 | prose | pages [11] -->
shape factor Geometric shape

<!-- b000348 | prose | pages [11] -->
Cuboid

<!-- b000349 | prose | pages [11] -->
Elliptic cylinder

<!-- b000350 | prose | pages [11] -->
Sector cylinder

<!-- b000351 | prose | pages [11] -->
Duration

<!-- b000352 | prose | pages [11] -->
1.46 2.9

<!-- b000353 | prose | pages [11] -->
1.00 4.8

<!-- b000354 | prose | pages [11] -->
3.0 3.7 

<!-- b000355 | prose | pages [11] -->
From the data in the above table, we can clearly conclude that when the base area is constant and the ratio of the long axis to the short axis is 1, the sandcastle foundation can last the longest time. We approximate it as a cylinder with a maximum duration of 4.8 days.

<!-- b000356 | heading | pages [11] -->
5. Optimal water and sand ratio model

<!-- b000357 | heading | pages [11] -->
5.1 Model Overview

<!-- b000358 | prose | pages [11] -->
We use the optimal shape model based on the sandcastle foundation dynamics model to obtain the optimal shape of the sandcastle foundation with the longest duration when the water-sand ratio is constant. However, the size of the water-sand ratio will also directly affect the erosion resistance of the sandcastle foundation. We have introduced the equation of the relationship between the water-sand polymerization degree and the water-sand ratio, and at the same time limit the allowed polymerization degree range to obtain a reasonable water-sand ratio Range, and then by solving the model, the optimal water-sand ratio is obtained[2].

<!-- b000359 | heading | pages [11] -->
5.2 Quantitative model of Water and sand polymerization degree

<!-- b000360 | prose | pages [11] -->
We consider the aggregation of water and sand, leading to the concept of the degree of water-sand polymerization. We give the definition of the degree of polymerization of water and sand based on the volume change of the water and sand specific gravity before and after polymerization:

<!-- b000361 | prose | pages [11] -->
1

<!-- b000362 | prose | pages [11] -->


<!-- b000363 | prose | pages [11] -->


<!-- b000364 | prose | pages [11] -->


<!-- b000365 | prose | pages [11] -->


<!-- b000366 | prose | pages [11] -->
1

<!-- b000367 | prose | pages [11] -->
Q

<!-- b000368 | prose | pages [11] -->
 

<!-- b000369 | prose | pages [11] -->
 

<!-- b000370 | prose | pages [11] -->


<!-- b000371 | prose | pages [11] -->
Where,

<!-- b000372 | prose | pages [11] -->
1

<!-- b000373 | prose | pages [11] -->


<!-- b000374 | prose | pages [11] -->
V V V

<!-- b000375 | prose | pages [11] -->


<!-- b000376 | prose | pages [11] -->


<!-- b000377 | prose | pages [11] -->
1 2

<!-- b000378 | prose | pages [11] -->


<!-- b000379 | prose | pages [11] -->


<!-- b000380 | prose | pages [11] -->
100 %

<!-- b000381 | prose | pages [11] -->
 1 1 2

<!-- b000382 | prose | pages [11] -->
(12)

<!-- b000383 | prose | pages [11] -->


<!-- b000384 | prose | pages [11] -->
V V V

<!-- b000385 | prose | pages [11] -->


<!-- b000386 | prose | pages [11] -->
1 2

<!-- b000387 | prose | pages [11] -->


<!-- b000388 | prose | pages [11] -->


<!-- b000389 | prose | pages [11] -->
V respectively represent the volume of sand and water before mixing; V , 1 2 and represent the 1  2 water absorption coefficient and water solubility coefficient, respectively. We use these two coefficients to express the polymerization ability of water and sand. We simplify the equation with the water-sand n : ratio p

<!-- b000390 | prose | pages [11] -->


<!-- b000391 | prose | pages [11] -->


<!-- b000392 | prose | pages [11] -->


<!-- b000393 | prose | pages [11] -->


<!-- b000394 | prose | pages [11] -->


<!-- b000395 | prose | pages [11] -->


<!-- b000396 | prose | pages [11] -->
1

<!-- b000397 | prose | pages [11] -->
Q

<!-- b000398 | prose | pages [11] -->
 

<!-- b000399 | prose | pages [11] -->
 

<!-- b000400 | prose | pages [11] -->


<!-- b000401 | prose | pages [11] -->


<!-- b000402 | prose | pages [11] -->
n n

<!-- b000403 | prose | pages [11] -->


<!-- b000404 | prose | pages [11] -->
1

<!-- b000405 | prose | pages [11] -->


<!-- b000406 | prose | pages [11] -->
p

<!-- b000407 | prose | pages [11] -->


<!-- b000408 | prose | pages [11] -->


<!-- b000409 | prose | pages [11] -->
  

<!-- b000410 | prose | pages [11] -->


<!-- b000411 | prose | pages [11] -->


<!-- b000412 | prose | pages [11] -->
1 1 2

<!-- b000413 | prose | pages [11] -->
100 %

<!-- b000414 | prose | pages [11] -->


<!-- b000415 | prose | pages [11] -->
(13)

<!-- b000416 | prose | pages [11] -->


<!-- b000417 | prose | pages [11] -->
1

<!-- b000418 | prose | pages [11] -->
n

<!-- b000419 | prose | pages [11] -->


<!-- b000420 | prose | pages [11] -->


<!-- b000421 | prose | pages [11] -->
p

<!-- b000422 | prose | pages [11] -->


<!-- b000423 | furniture | pages [11] -->
关注数学模型

<!-- b000424 | furniture | pages [11] -->
2

<!-- b000425 | furniture | pages [11] -->
MATHmodels

<!-- b000426 | furniture | pages [11] -->
获取更多资讯

<!-- b000427 | furniture | pages [12] -->
Team # 2010821

<!-- b000428 | furniture | pages [12] -->
Page 12 of 24

<!-- b000429 | prose | pages [12] -->
We use MATLAB to solve this equation and get the relationship curve between the degree of Water and sand polymerization and the ratio of water and sand, as shown in FIG 6.

<!-- b000430 | prose | pages [12] -->
FIG 6.Degree of convergence of water and sand

<!-- b000431 | prose | pages [12] -->
The degree of water-sand polymerization increases with the increase of water-sand ratio. We must consider not only the relatively large cohesiveness, but also the optimization of erosion resistance, that is, the longest duration. In combination with the actual situation, we choose a two-point interval with a large viscosity range as shown in our figure as our optimization constraint.

<!-- b000432 | heading | pages [12] -->
5.3 Solving the Model

<!-- b000433 | prose | pages [12] -->
We use the sandcastle foundation dynamics model in Question 1 as the basis, use the optimal n as a variable proportion of the best shape we selected, and use the initial value of the water-sand ratio to discretely process the target T in the same way:

<!-- b000434 | prose | pages [12] -->
p

<!-- b000435 | prose | pages [12] -->
S First put into the dynamic equation (1), according to the change of sandcastle foundations h and  , the relationship between the damage index and time is obtained, and the constraint condition is  added:

<!-- b000436 | prose | pages [12] -->
7.0 n  .0 85  (14) p p n equally spaced points: Find the duration table record of p

<!-- b000437 | caption | pages [12] -->
Table 6 Corresponding duration of different water-sand ratios

<!-- b000438 | prose | pages [12] -->
Water-sand ratio Duration

<!-- b000439 | prose | pages [12] -->
0.70 4.7

<!-- b000440 | prose | pages [12] -->
0.72 4.9

<!-- b000441 | prose | pages [12] -->
0.74 5.2

<!-- b000442 | prose | pages [12] -->
0.76 4.8

<!-- b000443 | prose | pages [12] -->
Water-sand ratio Duration

<!-- b000444 | prose | pages [12] -->
0.78 5.1

<!-- b000445 | prose | pages [12] -->
0.80 5.0

<!-- b000446 | prose | pages [12] -->
0.82 4.3

<!-- b000447 | prose | pages [12] -->
0.84 4.2

<!-- b000448 | furniture | pages [12] -->
关注数学模型

<!-- b000449 | furniture | pages [12] -->
2

<!-- b000450 | furniture | pages [12] -->
MATHmodels

<!-- b000451 | furniture | pages [12] -->
获取更多资讯

<!-- b000452 | furniture | pages [13] -->
Team # 2010821

<!-- b000453 | furniture | pages [13] -->
Page 13 of 24

<!-- b000454 | prose | pages [13] -->
Using the Discrete Global Optimization Algorithm of the best shape model in Problem 1, we can 739 .0 n conclude that when the water-sand ratio is  p , the longest duration of the sandcastle foundation is achieved under the condition of ensuring good shape adhesion.

<!-- b000455 | heading | pages [13] -->
6.Fuzzy comprehensive evaluation model based on rain erosion resistance

<!-- b000456 | heading | pages [13] -->
6.1 Model Overview

<!-- b000457 | prose | pages [13] -->
Aiming at the erosion of sandcastles by waves and tides, we have established some models to obtain the optimal shape of the sandcastle foundation as a cylinder.However, the actual erosion risk facing sandcastles is not limited to the effects of waves and tides. We should also consider the erosion of rainwater.Based on the cuboids, ellipses, and sectors at the optimal shape coefficients obtained in Problem 1, we have further addressed the problem of rain erosion., we define the sandcastle collapse limit coefficient, and comprehensively establish the rain erosion resistance assessment model by comprehensively ability to resist rainwater infiltration and sandcastle structure evacuation ratio. On this basis, an evaluation model of sandcastle anti-wave erosion ability is constructed. Finally, a fuzzy comprehensive evaluation model is established to evaluate the optimal sandcastle shape under the action of waves and rain[3].

<!-- b000458 | heading | pages [13] -->
6.2 Evaluation model for rain erosion resistance

<!-- b000459 | heading | pages [13] -->
6.2.1 Establishment of Model

<!-- b000460 | prose | pages [13] -->
Before establishing a fuzzy comprehensive evaluation model for the optimal shape of the sandcastle foundation, we set up the evaluation model of rain erosion resistance as follows:

<!-- b000461 | prose | pages [13] -->
First, the sandcastle's ability to resist rainwater infiltration is established as follows[4]:

<!-- b000462 | prose | pages [13] -->
i i 2 1 F R   u a

<!-- b000463 | prose | pages [13] -->
Where,

<!-- b000464 | prose | pages [13] -->
  3,2,1 F i i

<!-- b000465 | prose | pages [13] -->
  i i 2 1 (15) R R     a a

<!-- b000466 | prose | pages [13] -->
represents the ability of the cuboid, cylinder and sector cylinder to resist rain

<!-- b000467 | prose | pages [13] -->


<!-- b000468 | prose | pages [13] -->
u

<!-- b000469 | prose | pages [13] -->
i Q represents the degree of aggregation of the three shapes of gravel, respectively. infiltration.

<!-- b000470 | prose | pages [13] -->
  represents positive definite coefficient. . i i R n n     1 1 a p collapse

<!-- b000471 | prose | pages [13] -->
represents the sandcastle

<!-- b000472 | prose | pages [13] -->
ni 3,2,1 i 

<!-- b000473 | prose | pages [13] -->
collapse

<!-- b000474 | prose | pages [13] -->
collapse limit coefficients of the three shapes, respectively.

<!-- b000475 | prose | pages [13] -->
Secondly, the evacuation ratio indicators for establishing the sandcastle structure are as follows:

<!-- b000476 | prose | pages [13] -->


<!-- b000477 | prose | pages [13] -->
i =

<!-- b000478 | prose | pages [13] -->
R  

<!-- b000479 | prose | pages [13] -->
2

<!-- b000480 | prose | pages [13] -->
Where,

<!-- b000481 | prose | pages [13] -->
 

<!-- b000482 | prose | pages [13] -->
 

<!-- b000483 | prose | pages [13] -->


<!-- b000484 | prose | pages [13] -->
i i

<!-- b000485 | prose | pages [13] -->
Q V V  (16)  f DL

<!-- b000486 | prose | pages [13] -->
V represents positive definite coefficient. .  Ri 3,2,1 i  2

<!-- b000487 | prose | pages [13] -->
V

<!-- b000488 | prose | pages [13] -->
represents the shear capacity of f

<!-- b000489 | prose | pages [13] -->
represents the shear force on the sand under the rain gravity load. sandcastle gravel.

<!-- b000490 | prose | pages [13] -->
DL Finally, an assessment model for rainwater erosion resistance is established:

<!-- b000491 | prose | pages [13] -->
i H F  1 u i i i i n R   (17) collapse

<!-- b000492 | furniture | pages [13] -->
关注数学模型

<!-- b000493 | furniture | pages [13] -->
2

<!-- b000494 | furniture | pages [13] -->
MATHmodels

<!-- b000495 | furniture | pages [13] -->
获取更多资讯

<!-- b000496 | furniture | pages [14] -->
Team # 2010821

<!-- b000497 | prose | pages [14] -->
Where,

<!-- b000498 | prose | pages [14] -->
 

<!-- b000499 | furniture | pages [14] -->
Page 14 of 24

<!-- b000500 | prose | pages [14] -->
represents rainwater erosion resistance of the three shapes. H i 3,2,1 i  1

<!-- b000501 | heading | pages [14] -->
6.2.2 Solution of Model

<!-- b000502 | prose | pages [14] -->
In order to solve the model, we consulted some literatures and defined below parameters as shown in the following table:

<!-- b000503 | caption | pages [14] -->
Table 7 Number of rain erosion resistance model

<!-- b000504 | heading | pages [14] -->
Symbols

<!-- b000505 | prose | pages [14] -->
  ，  1 2

<!-- b000506 | prose | pages [14] -->
np

<!-- b000507 | prose | pages [14] -->
  1 2 3 n n n ， ， collapse collapse collapse

<!-- b000508 | prose | pages [14] -->
V f

<!-- b000509 | prose | pages [14] -->
V DL

<!-- b000510 | prose | pages [14] -->
Numerical value

<!-- b000511 | prose | pages [14] -->
  10.6， 12.1

<!-- b000512 | prose | pages [14] -->
0.125

<!-- b000513 | prose | pages [14] -->
  .1,1 24 .1, 56

<!-- b000514 | prose | pages [14] -->
305

<!-- b000515 | prose | pages [14] -->
355

<!-- b000516 | prose | pages [14] -->
Then, we obtained the rainwater erosion resistance of cuboids, cylinders, and sectors as shown in the following table:

<!-- b000517 | caption | pages [14] -->
Table 8 Resistance to rain erosion

<!-- b000518 | prose | pages [14] -->
Geometric shape

<!-- b000519 | prose | pages [14] -->
cuboid

<!-- b000520 | prose | pages [14] -->
cylinder

<!-- b000521 | prose | pages [14] -->
thick sector

<!-- b000522 | prose | pages [14] -->
Numerical value

<!-- b000523 | prose | pages [14] -->
50.6

<!-- b000524 | prose | pages [14] -->
63.5

<!-- b000525 | prose | pages [14] -->
68.1

<!-- b000526 | heading | pages [14] -->
6.3 Optimal Shape Fuzzy Comprehensive Evaluation Model

<!-- b000527 | heading | pages [14] -->
6.3.1 Establishment of Model

<!-- b000528 | prose | pages [14] -->
Based on the evaluation model of sandcastle resistance to rain erosion, we first establish the evaluation model of sandcastle resistance to wave current erosion as follows:

<!-- b000529 | prose | pages [14] -->
i H  2 Where,

<!-- b000530 | prose | pages [14] -->
 

<!-- b000531 | prose | pages [14] -->
T   (18) 3 3 i

<!-- b000532 | prose | pages [14] -->
represents the resistance to wave current erosion of the three shapes. H i 3,2,1 i  2 positive definite coefficient.

<!-- b000533 | prose | pages [14] -->
stands for  3

<!-- b000534 | prose | pages [14] -->
It should be noted that, in order to determine whether the cuboid, elliptic cylinder and fan-shaped body are still optimal with the optimal shape coefficient, we have established the optimal shape fuzzy synthesis based on the numerical values of the different capabilities of the three shapes. The evaluation model is as follows:

<!-- b000535 | furniture | pages [14] -->
关注数学模型

<!-- b000536 | furniture | pages [14] -->
2

<!-- b000537 | furniture | pages [14] -->
MATHmodels

<!-- b000538 | furniture | pages [14] -->
获取更多资讯

<!-- b000539 | furniture | pages [15] -->
Team # 2010821

<!-- b000540 | furniture | pages [15] -->
Page 15 of 24

<!-- b000541 | prose | pages [15] -->
Step1.Determine membership function. We take the ratio of the ability to resist wave current  erosion or rain erosion to the total shape of the three shapes as the membership, so we establish membership functions as follows:

<!-- b000542 | prose | pages [15] -->


<!-- b000543 | prose | pages [15] -->
H 

<!-- b000544 | prose | pages [15] -->
1

<!-- b000545 | prose | pages [15] -->
H

<!-- b000546 | prose | pages [15] -->


<!-- b000547 | prose | pages [15] -->
H 

<!-- b000548 | prose | pages [15] -->
2

<!-- b000549 | prose | pages [15] -->
H

<!-- b000550 | prose | pages [15] -->
i

<!-- b000551 | prose | pages [15] -->
H

<!-- b000552 | prose | pages [15] -->
 

<!-- b000553 | prose | pages [15] -->
i i

<!-- b000554 | prose | pages [15] -->


<!-- b000555 | prose | pages [15] -->
1 1 1

<!-- b000556 | prose | pages [15] -->
3

<!-- b000557 | prose | pages [15] -->
(19)

<!-- b000558 | prose | pages [15] -->


<!-- b000559 | prose | pages [15] -->
i

<!-- b000560 | prose | pages [15] -->
H

<!-- b000561 | prose | pages [15] -->
1 1

<!-- b000562 | prose | pages [15] -->
i

<!-- b000563 | prose | pages [15] -->


<!-- b000564 | prose | pages [15] -->
i

<!-- b000565 | prose | pages [15] -->
H

<!-- b000566 | prose | pages [15] -->
 

<!-- b000567 | prose | pages [15] -->
i i

<!-- b000568 | prose | pages [15] -->


<!-- b000569 | prose | pages [15] -->
2 2 2

<!-- b000570 | prose | pages [15] -->
(20)

<!-- b000571 | prose | pages [15] -->
3

<!-- b000572 | prose | pages [15] -->


<!-- b000573 | prose | pages [15] -->
i

<!-- b000574 | prose | pages [15] -->
H

<!-- b000575 | prose | pages [15] -->
2 1

<!-- b000576 | prose | pages [15] -->
i

<!-- b000577 | prose | pages [15] -->


<!-- b000578 | prose | pages [15] -->
Step2.Calculate membership table based on membership function. We substitute the values of  the two capabilities of the three shapes into Formula   , calculate the membership table of the 19 , 20 optimal shape, and establish a fuzzy relation matrix.

<!-- b000579 | prose | pages [15] -->
Step3.Determine the weight of the two capabilities in the optimal evaluation. We have  considered that when our sandcastle faces seawater, tidal erosion and rainwater erosion at the same time, the erosion degree of rainwater on sandcastle is much greater than that of seawater and tide on   7.0,3.0 A  sandcastle. Therefore, we set the weight of the two capabilities in decision making to :

<!-- b000580 | heading | pages [15] -->
Step4：Calculate comprehensive evaluation results. The calculation formula for the

<!-- b000581 | prose | pages [15] -->
 comprehensive evaluation results is as follows:

<!-- b000582 | prose | pages [15] -->
B

<!-- b000583 | heading | pages [15] -->
6.3.2 Solution of Model

<!-- b000584 | prose | pages [15] -->
(21) A R   

<!-- b000585 | prose | pages [15] -->
In order to solve the model, we have determined the calculation parameters and calculation results by referring to the online information and citing reference parameters:

<!-- b000586 | caption | pages [15] -->
Table 9 Number of wave current erosion resistance model

<!-- b000587 | heading | pages [15] -->
Symbols

<!-- b000588 | prose | pages [15] -->
 3

<!-- b000589 | prose | pages [15] -->
  , , T T T 1 2 3

<!-- b000590 | prose | pages [15] -->
Numerical value

<!-- b000591 | prose | pages [15] -->
13.44

<!-- b000592 | prose | pages [15] -->
  2.5,8.6,6.2

<!-- b000593 | prose | pages [15] -->
Then, we obtained the anti-wave erosion ability of cuboid, cylinder and fan-shape cylinder as shown in the following table:

<!-- b000594 | caption | pages [15] -->
Table 10 Resistance to wave erosion

<!-- b000595 | prose | pages [15] -->
Geometric shape

<!-- b000596 | prose | pages [15] -->
rectangle

<!-- b000597 | prose | pages [15] -->
roundness

<!-- b000598 | prose | pages [15] -->
sector

<!-- b000599 | prose | pages [15] -->
Numerical value

<!-- b000600 | prose | pages [15] -->
34.94

<!-- b000601 | prose | pages [15] -->
91.39

<!-- b000602 | prose | pages [15] -->
69.89

<!-- b000603 | furniture | pages [15] -->
关注数学模型

<!-- b000604 | furniture | pages [15] -->
2

<!-- b000605 | furniture | pages [15] -->
MATHmodels

<!-- b000606 | furniture | pages [15] -->
获取更多资讯

<!-- b000607 | furniture | pages [16] -->
Team # 2010821

<!-- b000608 | furniture | pages [16] -->
Page 16 of 24

<!-- b000609 | prose | pages [16] -->
The membership degrees corresponding to the three shapes according to the membership function are shown in Table 11:

<!-- b000610 | caption | pages [16] -->
Table 11 Competency assessment membership scale

<!-- b000611 | prose | pages [16] -->
Evaluation index

<!-- b000612 | prose | pages [16] -->
Rain erosion resistance

<!-- b000613 | prose | pages [16] -->
wave current erosion resistance

<!-- b000614 | prose | pages [16] -->
This determines the fuzzy relation matrix:

<!-- b000615 | prose | pages [16] -->
0.278  R 

<!-- b000616 | prose | pages [16] -->


<!-- b000617 | prose | pages [16] -->
0.178

<!-- b000618 | prose | pages [16] -->
Cuboid Cylinder Sector cylinder

<!-- b000619 | prose | pages [16] -->
0.278 0.348 0.374

<!-- b000620 | prose | pages [16] -->
0.178 0.466 0.356

<!-- b000621 | prose | pages [16] -->
0.348 0.374

<!-- b000622 | prose | pages [16] -->


<!-- b000623 | prose | pages [16] -->
(22)

<!-- b000624 | prose | pages [16] -->


<!-- b000625 | prose | pages [16] -->
0.466 0.356

<!-- b000626 | prose | pages [16] -->
  7.0,3.0 A Since the weight of the project in decision-making is obtained is:

<!-- b000627 | prose | pages [16] -->


<!-- b000628 | prose | pages [16] -->
,the comprehensive evaluation 

<!-- b000629 | prose | pages [16] -->
 = 0.208 0.430 0.361 B A R   (23) ， ，

<!-- b000630 | prose | pages [16] -->
It can be seen that the stability of cuboids, cylinders, and fan-shape cylinders under the combined action of wave erosion and rain erosion is 0.208, 0.430, and 0361, respectively. By comparison, we can know that the stability of cylinders under double erosion is the highest.

<!-- b000631 | heading | pages [16] -->
7. Humidity Prediction Model Based on RBF Neural Network Algorithm

<!-- b000632 | heading | pages [16] -->
7.1 Model Overviw

<!-- b000633 | prose | pages [16] -->
Sandcastles are products of mixing sand and water. In order to improve the duration of sandcastles, the most important thing is the humidity of the sandcastle and the protection after the production is completed. After consulting the relevant literature, we know that the adhesive protection after the production is also determined by the humidity of the sandcastle. Therefore, when we know the general trend of humidity, we can make the sandcastle last longer. We selected the RBF neural network algorithm as the prediction network, combined with the daily changing characteristics of the beach temperature as an input factor, and proposed a sandcastle humidity prediction model suitable for better extending the sandcastle duration[5].

<!-- b000634 | heading | pages [16] -->
7.2 Model Preparation

<!-- b000635 | prose | pages [16] -->
We take a typical beach, Venice Beach, as an example. The humidity data from August 1 to 3, 2019 was obtained from the U.S. Meteorological Administration. It is worth mentioning that because of the similar sandy conditions and weather conditions of the beach, the Venice Beach we selected is very typical[6].

<!-- b000636 | prose | pages [16] -->
Index screening: 

<!-- b000637 | prose | pages [16] -->
The humidity of the beach is the result of the combination of many factors, which are closely related to solar radiation, wind, beach temperature, and ground vegetation. We used principal

<!-- b000638 | furniture | pages [16] -->
关注数学模型

<!-- b000639 | furniture | pages [16] -->
2

<!-- b000640 | furniture | pages [16] -->
MATHmodels

<!-- b000641 | furniture | pages [16] -->
获取更多资讯

<!-- b000642 | furniture | pages [17] -->
Team # 2010821

<!-- b000643 | furniture | pages [17] -->
Page 17 of 24

<!-- b000644 | prose | pages [17] -->
component analysis to find that temperature changes caused by the sun's light intensity had the most significant effect on beach humidity. Therefore, we explore the change of the humidity of the beach under different time and different weather conditions.

<!-- b000645 | prose | pages [17] -->
Through observation data, we found that there is a clear correlation between the beach environment humidity and beach temperature, specifically: no matter whether it is sunny or cloudy, as the beach temperature changes over time, the humidity will also change accordingly; however, under sunny weather, Humidity changes on the beach are greater than on cloudy days.

<!-- b000646 | prose | pages [17] -->
In summary, the humidity of the beach is indeed mainly affected by the change of the ambient temperature, and it has a negative correlation with it. We select the ambient temperature at different time periods of the day as the input factor, select 500 input samples, 50 simulated samples, and 50 predicted samples.

<!-- b000647 | heading | pages [17] -->
7.3 RBF neural network algorithm

<!-- b000648 | prose | pages [17] -->
The RBF neural network algorithm has strong non-linear fitting property. It not only has good best approximation performance for complex functions, but also has fast convergence speed.

<!-- b000649 | prose | pages [17] -->
 Assume that the input vector is

<!-- b000650 | prose | pages [17] -->
, X x  1  

<!-- b000651 | prose | pages [17] -->
T

<!-- b000652 | prose | pages [17] -->


<!-- b000653 | prose | pages [17] -->
T , n is the number of input samples, , , x x nx  2 2

<!-- b000654 | prose | pages [17] -->
 h X is the output weight vector, m is the number of hidden nodes, d is the offset, , , , W w w w   1 2 n

<!-- b000655 | prose | pages [17] -->
 g is the radial basis function. Gaussian functions are usually used: is the network output, and

<!-- b000656 | prose | pages [17] -->
  exp g X C   i    2 / 2 X C (24)    i i

<!-- b000657 | prose | pages [17] -->
C is the i data center in the network. In this case, the output Where, is the European norm, and i

<!-- b000658 | prose | pages [17] -->
of the neural network is:

<!-- b000659 | prose | pages [17] -->


<!-- b000660 | prose | pages [17] -->
h X d

<!-- b000661 | prose | pages [17] -->
 

<!-- b000662 | prose | pages [17] -->
m m

<!-- b000663 | prose | pages [17] -->
   

<!-- b000664 | prose | pages [17] -->
w X C

<!-- b000665 | prose | pages [17] -->


<!-- b000666 | prose | pages [17] -->


<!-- b000667 | prose | pages [17] -->
(25)

<!-- b000668 | prose | pages [17] -->
i i

<!-- b000669 | prose | pages [17] -->
1 1

<!-- b000670 | prose | pages [17] -->
i i

<!-- b000671 | prose | pages [17] -->
 

<!-- b000672 | prose | pages [17] -->
Through the RBF neural network algorithm, we obtained the humidity change map under sunny and cloudy conditions. Starting from 7:00 am, samples were taken every 30 minutes, as shown in the figure below:

<!-- b000673 | prose | pages [17] -->
FIG 7. Moderate forecast curves for sunny and cloudy days

<!-- b000674 | furniture | pages [17] -->
关注数学模型

<!-- b000675 | furniture | pages [17] -->
2

<!-- b000676 | furniture | pages [17] -->
MATHmodels

<!-- b000677 | furniture | pages [17] -->
获取更多资讯

<!-- b000678 | furniture | pages [18] -->
Team # 2010821

<!-- b000679 | furniture | pages [18] -->
Page 18 of 24

<!-- b000680 | prose | pages [18] -->
As can be seen from the figure, we should humidify the glue in a timely manner at 13:30 on a cloudy day and at 13:00 on a sunny day. We know that the glue can maintain its viscosity for at least 8 hours, so the humidity starts to increase to 15:00 sandcastles can be protected before reaching basic stability at 21:00. By predicting the change in humidity, humidity prediction of the sandcastle situation is carried out to ensure the longest lasting time.

<!-- b000681 | heading | pages [18] -->
8. Sensitivity Analysis

<!-- b000682 | heading | pages [18] -->
8.1 Sensitivity Analysis of Most Shaped Model Based on Sandcastle Foundation

<!-- b000683 | heading | pages [18] -->
Dynamics Model

<!-- b000684 | prose | pages [18] -->
It should be noted that maximum damage coefficients can be selected differently by other people. If the value of is different, the maximum duration corresponding to each shape will change, and the change trend is complex and difficult to determine. Therefore, we need to explore whether there is a stable result (the cylinder has the strongest endurance) for different to prove the stability of the model. Here we continue to determine the stability of the cylinder by continuously taking the value to determine whether the cylinder is still the best shape. The results are as follows:

<!-- b000685 | prose | pages [18] -->
A(0.08,0) B(0.96,0)

<!-- b000686 | prose | pages [18] -->
FIG 8. Judging results as the time interval, we take 24 sample points around As shown in the figure, with 0.04     for analysis. Through graphical analysis, when 0.52     , a cylinder is still the optimal 0.08， 0.96   , the optimal shape becomes a fan or cuboid. Therefore, we believe that our shape. When 0.08， 0.96     model is stable when it can withstand the maximum damage factor model is very robust.

<!-- b000687 | prose | pages [18] -->
. In other words, our 0.08， 0.96  

<!-- b000688 | heading | pages [18] -->
8.2 Sensitivity Analysis of Optimal Water-Sand Mixing Model

<!-- b000689 | prose | pages [18] -->
Based on the introduction of the equation of the relationship between water-sand polymerization degree and water-sand ratio, by limiting the allowable degree of polymerization, we have obtained a reasonable range of water-sand ratio. However, the relationship between the degree of polymerization

<!-- b000690 | furniture | pages [18] -->
关注数学模型

<!-- b000691 | furniture | pages [18] -->
2

<!-- b000692 | furniture | pages [18] -->
MATHmodels

<!-- b000693 | furniture | pages [18] -->
获取更多资讯

<!-- b000694 | furniture | pages [19] -->
Team # 2010821

<!-- b000695 | furniture | pages [19] -->
Page 19 of 24

<!-- b000696 | prose | pages [19] -->
  , , and the ratio of water to sand is affected by two parameters of . When the value of is not     accurate, the results of the model could be questionable. Therefore, we continuously adjust the value of

<!-- b000697 | prose | pages [19] -->
 ,   , as shown in FIG 9. Based on this, the robustness of the model is finally judged by calculating the error of the model result.

<!-- b000698 | prose | pages [19] -->
FIG 9. Degree of polymerization curve

<!-- b000699 | prose | pages [19] -->
As shown in the figure, based on the original coefficients, we increase and decrease the data by 1% and 2% respectively (note that its initial parameter  1.56 , 2.86 ), so as to obtain the graph of the     degree of aggregation-water-sand ratio in five cases. Based on this, we apply Model 2 again and combine the initial results of Model 2 to calculate the error table of the three shapes as follows:

<!-- b000700 | caption | pages [19] -->
Table 12 Error of the table

<!-- b000701 | prose | pages [19] -->
   ,   Cuboid

<!-- b000702 | prose | pages [19] -->
Error/%

<!-- b000703 | prose | pages [19] -->
  1.58， 2.88 2.3

<!-- b000704 | prose | pages [19] -->
  1.59， 2.89 4.9

<!-- b000705 | prose | pages [19] -->
  1.54， 2.84 3.1

<!-- b000706 | prose | pages [19] -->
  1.53， 2.83 3.8

<!-- b000707 | prose | pages [19] -->
Cylinder Sector cylinder

<!-- b000708 | prose | pages [19] -->
3.9 3.6

<!-- b000709 | prose | pages [19] -->
4.9 5.0

<!-- b000710 | prose | pages [19] -->
3.3 2.9

<!-- b000711 | prose | pages [19] -->
4.8 4.6

<!-- b000712 | prose | pages [19] -->
 , From the above table, we can observe that when increases and decreases 1% and 2%   respectively, the final error of all shapes is within 5%. Therefore, it shows that our model is more robust  , when has some errors.  

<!-- b000713 | furniture | pages [19] -->
关注数学模型

<!-- b000714 | furniture | pages [19] -->
2

<!-- b000715 | furniture | pages [19] -->
MATHmodels

<!-- b000716 | furniture | pages [19] -->
获取更多资讯

<!-- b000717 | furniture | pages [20] -->
Team # 2010821

<!-- b000718 | furniture | pages [20] -->
Page 20 of 24

<!-- b000719 | heading | pages [20] -->
8.3 Sensitivity Analysis of A Fuzzy Comprehensive Evaluation Model Based on the

<!-- b000720 | prose | pages [20] -->
Ability to Resist Rain Erosion

<!-- b000721 | prose | pages [20] -->
In order to make the fuzzy comprehensive evaluation model valid, we must ensure that the fuzzy comprehensive evaluation index (resistance to rainwater erosion and resistance to wave erosion) is accurate and reliable. In determining the values of the two capabilities, we have introduced three to assist the calculation. However, since the values of the three positive definite coefficients , ,    1 2 3 positive definite coefficients are not very reliable, we continuously adjust the values of the three positive definite coefficients to determine whether the cylinder has always been the optimal shape and thus to judge the stability of the model. The judgment results are as follows:

<!-- b000722 | prose | pages [20] -->
FIG 10. Stability judgment

<!-- b000723 | prose | pages [20] -->
By observing the figure, we clearly know that when increases to 130% and above, the cylinder  1 is no longer the optimal shape, and the optimal shape is the fan-shape cylinder. When is reduced to  2 75% and below, the cylinder is no longer the optimal shape, and the optimal shape is a cuboid. When

<!-- b000724 | prose | pages [20] -->
fluctuates at 30% of its original value, the cylinder is still the optimal shape. Therefore, we can tell 3 that when the three positive definite coefficients fluctuate within 25% of the original value, the results of our model have not changed much and have shown strong robustness.

<!-- b000725 | heading | pages [20] -->
8.4 Sensitivity Analysis of Sandcastle warning protection Model

<!-- b000726 | prose | pages [20] -->
The advantage of the sandcastle humidity prediction model is that it can predict the trend graph of beach humidity in advance and remediate sandcastles in time. If the error between the actual value and the predicted value of the beach humidity does not exceed 10%, we consider that the sandcastle humidity prediction model based on the RBF neural network algorithm is highly reliable.

<!-- b000727 | prose | pages [20] -->
The simulated was performed using MATLAB. First, we choose the mean square error to be 0.02 and the expansion speed of the radial basis function to be 0.8. Then we input the samples to build the RBF neural network and simulate the model. Finally, the average relative error between the predicted value and the actual value of the beach humidity is 4.32%. The comparison chart between the predicate

<!-- b000728 | furniture | pages [20] -->
关注数学模型

<!-- b000729 | furniture | pages [20] -->
2

<!-- b000730 | furniture | pages [20] -->
MATHmodels

<!-- b000731 | furniture | pages [20] -->
获取更多资讯

<!-- b000732 | furniture | pages [21] -->
Team # 2010821

<!-- b000733 | furniture | pages [21] -->
Page 21 of 24

<!-- b000734 | prose | pages [21] -->
value and the actual value using ORIGIN fitting is shown in FIG 11, which illustrates that the sandcastle humidity prediction model based on the RBF neural network algorithm can predict the humidity basic trend.

<!-- b000735 | prose | pages [21] -->
FIG 11. Actual vs. predicted curve

<!-- b000736 | heading | pages [21] -->
9. Evaluation and Promotion of Model

<!-- b000737 | heading | pages [21] -->
9.1 Strength and Weakness

<!-- b000738 | heading | pages [21] -->
9.1.1 Strengths

<!-- b000739 | prose | pages [21] -->
Have fully considered the erosion of sandcastles caused by waves and tidal effects and established a

<!-- b000740 | prose | pages [21] -->
sand-bearing capability indicator. Considering the change in the bottom area and height of the sandcastle foundation during the

<!-- b000741 | prose | pages [21] -->
movement, we create a sandcastle damage index to quantify the sandcastle damage reasonably. Based on some solutions obtained from the sandcastle dynamics simulation, the discrete global  optimization method based on the successive descent has been used to obtain the global optimal solution. The equation of the relationship between water-sand polymerization degree and water-sand ratio is  introduced.The reasonable water-sand ratio range is obtained by limiting the allowable On the issue of rain erosion, we put forward the collapse limit coefficient of sandcastle specifically. polymerization degree range.  Considering the ability of resisting rain infiltration and the evacuation ratio of sandcastle structure comprehensively, we established an evaluation model to determine the stability of the selected shape. Because the RBF neural network overcomes slow convergence and local minimization of the other

<!-- b000742 | prose | pages [21] -->
neural network algorithms, when designing the sandcastle early warming protection mechanism, we have chosen the RBF neural network model to predict when to apply adhesive to enhance the duration of sandcastle

<!-- b000743 | furniture | pages [21] -->
关注数学模型

<!-- b000744 | furniture | pages [21] -->
2

<!-- b000745 | furniture | pages [21] -->
MATHmodels

<!-- b000746 | furniture | pages [21] -->
获取更多资讯

<!-- b000747 | furniture | pages [22] -->
Team # 2010821

<!-- b000748 | furniture | pages [22] -->
Page 22 of 24

<!-- b000749 | prose | pages [22] -->
When using the RBF neural network algorithm, we have selected input factors based on the

<!-- b000750 | prose | pages [22] -->
changing characteristics of the ambient temperature to accurately and reasonably predict the daily humidity change trend, thereby effectively humidity prediction the sandcastle and extending its duration.

<!-- b000751 | heading | pages [22] -->
9.1.2 Weaknesses

<!-- b000752 | prose | pages [22] -->
We did not consider three-dimensional shapes other than cuboids, elliptical cylinders, and sector

<!-- b000753 | prose | pages [22] -->
cylinders, and only selected the three types of shapes most commonly used in sandcastles. We only have considered sandcastles under various water erosion conditions, but not the impact of

<!-- b000754 | prose | pages [22] -->
other factors in nature. The accuracy of some selected coefficients from other literatures may affect some final conclusions. We only have considered the situation when the waves and tides are relatively calm. When the

<!-- b000755 | prose | pages [22] -->
waves and tides significantly fluctuate, the sandcastle might not collapse in the way we have expected.

<!-- b000756 | heading | pages [22] -->
9.2 Promotion

<!-- b000757 | prose | pages [22] -->
Considering the impact of water erosion on sandcastle alone, our model is very robust. Therefore, our model is suitable when the quantitative factors of water erosion fluctuate within a certain range. However, under objective natural conditions, the factors affecting the stability of sandcastles may not be limited to water erosion (such as wind erosion, light, etc.). Therefore, our strategy may need to be slightly modified to cope with the sandcastle foundation under different natural and objective conditions. Further, based on the original model, we tried to establish the basic dynamics equation of the sandcastle considering the combined effects of wind erosion and light, making the solution of the problem more practical. In addition, we believe that the final choice of the cylinder is the most stable of the three proposed shapes, but the problem is that the shape is diverse and there is no guarantee that the cylinder will still be the best of all shapes. Therefore, it is necessary to solve the problem of limited shape being considered.

<!-- b000758 | prose | pages [22] -->
We have two potential solutions to address that only three shapes have been investigated: 1. Perform cluster analysis on multiple shapes to find more sandcastle foundations that are applicable to actual situations. 2. Introduce the proportion of base area and height, have more shapes under consideration and find out the best three-dimensional aspect ratio of each shape.

<!-- b000759 | heading | pages [22] -->
10. Conclusions

<!-- b000760 | prose | pages [22] -->
A detailed strategy to extend the duration of sandcastle foundation was provided in this paper. Firstly, the most stable shape of the sandcastle which was affected by both of the wave and tide was found to be the cylinder. It showed the highest resistance to the wave current erosion among all the considered shapes, according to the optimal shape model based on the dynamics equation of sandcastle foundation. Secondly, the optimum water-sand ratio was worked out to be 0.32 by taking the water- sand polymerization degree into account. Then, the cylinder was confirmed to be the most stable shape by fuzzy comprehensive evaluation, and the rain erosion resistance and resistance to wave current

<!-- b000761 | furniture | pages [22] -->
关注数学模型

<!-- b000762 | furniture | pages [22] -->
2

<!-- b000763 | furniture | pages [22] -->
MATHmodels

<!-- b000764 | furniture | pages [22] -->
获取更多资讯

<!-- b000765 | furniture | pages [23] -->
Team # 2010821

<!-- b000766 | furniture | pages [23] -->
Page 23 of 24

<!-- b000767 | prose | pages [23] -->
erosion of the sandcastle were also taken into account.

<!-- b000768 | prose | pages [23] -->
Finally, an humidity prediction model of sandcastle was proposed based on RBF neural network, and the daily humidity trend was predicted accurately by the model. When the predicted humidity reached its limit, adhesive should be used in time to keep the bonding effect and stabilize the sandcastle foundation.

<!-- b000769 | heading | pages [23] -->
References

<!-- b000770 | references | pages [23] -->
[1] Cui Jie. Research on two-dimensional mathematical model of sediment under the action of wave and

<!-- b000771 | references | pages [23] -->
current [D]. Tianjin University, 2014.

<!-- b000772 | references | pages [23] -->
[2] Yang Yongjian. Several deterministic algorithms for global optimization [D]. Shanghai University,

<!-- b000773 | references | pages [23] -->
2005.

<!-- b000774 | references | pages [23] -->
[3] Lu Yehong. Test and simulation of the damage resistance of building roof structure in rainy season

<!-- b000775 | references | pages [23] -->
[J]. Computer Simulation, 2018, 35 (12): 176-180.

<!-- b000776 | references | pages [23] -->
[4] Yu Gaofeng, Qiu Jinming. Analysis of Teaching Effect Analysis and Optimization of Mathematical

<!-- b000777 | references | pages [23] -->
Modeling Based on Fuzzy Comprehensive Evaluation——Taking Sanming University as an Example

<!-- b000778 | references | pages [23] -->
[J]. Journal of Lanzhou University of Arts and Sciences (Natural Science Edition), 2018, 32 (05): 112-

<!-- b000779 | references | pages [23] -->
115.

<!-- b000780 | references | pages [23] -->
[5] Xu Tongyu, Wang Yan, Zhang Xiaobo, Chen Chunling, Xu Hui, Zhou Yuncheng. Application of

<!-- b000781 | references | pages [23] -->
RBF neural network to the simulation and prediction of humidity in northern sunlight greenhouse [J].

<!-- b000782 | references | pages [23] -->
Journal of Shenyang Agricultural University, 2014, 45 (06): 726-730 .

<!-- b000783 | references | pages [23] -->
[6] Wang Chengwu, Guo Songlin, Wang Wei. Research on short-term power load forecasting by

<!-- b000784 | references | pages [23] -->
improved particle swarm optimization RBF neural network [J] .Electronic Test, 2020 (03): 45-46 + 101.

<!-- b000785 | furniture | pages [23] -->
关注数学模型

<!-- b000786 | furniture | pages [23] -->
2

<!-- b000787 | furniture | pages [23] -->
MATHmodels

<!-- b000788 | furniture | pages [23] -->
获取更多资讯

<!-- b000789 | furniture | pages [24] -->
Team # 2010821

<!-- b000790 | heading | pages [24] -->
Memo

<!-- b000791 | prose | pages [24] -->
TO:Fun in the Sun

<!-- b000792 | furniture | pages [24] -->
Page 24 of 24

<!-- b000793 | prose | pages [24] -->
Topic: Teach you how to build the longest-lasting sandcastle

<!-- b000794 | prose | pages [24] -->
Dear Vacation Magazine Editor：

<!-- b000795 | prose | pages [24] -->
In recent years, the sandcastle related art works have become increasingly popular. After the

<!-- b000796 | prose | pages [24] -->
creation of great sandcastle art works, how to preserve these art works for a long time becomes an

<!-- b000797 | prose | pages [24] -->
obstacle to promoting this type of activities. Our team has developed a complete sandcastle humidity

<!-- b000798 | prose | pages [24] -->
prediction strategy to achieve the purpose of extending the duration of sandcastles. We appreciate this

<!-- b000799 | prose | pages [24] -->
opportunity to introduce you to our strategy.

<!-- b000800 | prose | pages [24] -->
The most stable shape of a sandcastle under the action of sea waves and tides: In general, the

<!-- b000801 | prose | pages [24] -->
most durable sandcastle can be piled with the optimal size ratio. These sandcastle shapes have the

<!-- b000802 | prose | pages [24] -->
longest duration: the cuboid with an aspect ratio of 1.46, the elliptical cylinder with an aspect ratio of

<!-- b000803 | prose | pages [24] -->
1.00, and the fan-shape cylinder with a radius and arc length ratio of A.

<!-- b000804 | prose | pages [24] -->
The best mixing ratio of water and sand: sandcastles are products of the mixture of sand and

<!-- b000805 | prose | pages [24] -->
water. When the water and sand ratio is 0.739, the sandcastle has the longest duration.

<!-- b000806 | prose | pages [24] -->
The most stable shape choice for rainy days: Rainy days are also a huge threat for sandcastles. It

<!-- b000807 | prose | pages [24] -->
has been proven that the cylinder is the most stable and longest lasting sandcastle shape.

<!-- b000808 | prose | pages [24] -->
Measures to extend the duration of the sandcastle: The sandcastles cannot last long without

<!-- b000809 | prose | pages [24] -->
proper humidity. We have found the lowest humidity on sunny and cloudy days happens at 13: 00-13:

<!-- b000810 | prose | pages [24] -->
30 in the afternoon. Adhesive is recommended to be used to enhance the sandcastle duration during this

<!-- b000811 | prose | pages [24] -->
time period with low humidity.

<!-- b000812 | prose | pages [24] -->
The above is the optimal sandcastle shape and humidity prediction system that we have proposed.

<!-- b000813 | prose | pages [24] -->
We are eager to help you build the longest lasting sandcastles. If you have any questions about our

<!-- b000814 | prose | pages [24] -->
solution, please feel free to contact us. Our team members are willing to solve any questions you have.

<!-- b000815 | prose | pages [24] -->
Regards，

<!-- b000816 | furniture | pages [24] -->
Team: 2010821

<!-- b000817 | prose | pages [24] -->
March 9 2020

<!-- b000818 | furniture | pages [24] -->
关注数学模型

<!-- b000819 | furniture | pages [24] -->
2

<!-- b000820 | furniture | pages [24] -->
MATHmodels

<!-- b000821 | furniture | pages [24] -->
获取更多资讯

<!-- b000822 | heading | pages [25] -->
Appendix

<!-- b000823 | caption | pages [25] -->
Table 13 Corresponding duration of Cylinder with different aspect ratios

<!-- b000824 | prose | pages [25] -->
Shape factor Duration

<!-- b000825 | prose | pages [25] -->
1.0 4.8

<!-- b000826 | prose | pages [25] -->
1.5 3.4

<!-- b000827 | prose | pages [25] -->
2.0 2.5

<!-- b000828 | prose | pages [25] -->
2.5 4

<!-- b000829 | prose | pages [25] -->
3.0 4.2

<!-- b000830 | prose | pages [25] -->
Shape factor Duration

<!-- b000831 | prose | pages [25] -->
3.5 3

<!-- b000832 | prose | pages [25] -->
4.0 4.6

<!-- b000833 | prose | pages [25] -->
4.5 4.7

<!-- b000834 | prose | pages [25] -->
5.0 2.0

<!-- b000835 | prose | pages [25] -->
5.5 3.6

<!-- b000836 | caption | pages [25] -->
Table 14 Corresponding duration of sector Cylinder with different aspect ratios

<!-- b000837 | prose | pages [25] -->
Shape factor Duration

<!-- b000838 | prose | pages [25] -->
0.1 3.5 

<!-- b000839 | prose | pages [25] -->
0.2 3.6 

<!-- b000840 | prose | pages [25] -->
0.3 3.7 

<!-- b000841 | prose | pages [25] -->
0.4 2 

<!-- b000842 | prose | pages [25] -->
0.5 1.8 

<!-- b000843 | prose | pages [25] -->
Shape factor Duration

<!-- b000844 | prose | pages [25] -->
0.6 3.2 

<!-- b000845 | prose | pages [25] -->
0.7 2.8 

<!-- b000846 | prose | pages [25] -->
0.8 2.9 

<!-- b000847 | prose | pages [25] -->
0.9 3 

<!-- b000848 | prose | pages [25] -->
3.5 

<!-- b000849 | furniture | pages [25] -->
关注数学模型

<!-- b000850 | furniture | pages [25] -->
2

<!-- b000851 | furniture | pages [25] -->
MATHmodels

<!-- b000852 | furniture | pages [25] -->
获取更多资讯
