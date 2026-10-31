# P-B-2020-2010821-2af4f390

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2020

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | title | pages [1] -->
B

<!-- b000005 | furniture | pages [1] -->
2010821

<!-- b000006 | prose | pages [1] -->
MCM/ICM

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
How to build a durable sandcastle foundation?

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In recent years, as sand castle art has become more popular, more and more ingenious sand castle art works have been created. However, perfect works of art will disappear, and how to be preserved for a long time becomes an obstacle to the advancement of Sandcastle art.

<!-- b000011 | prose | pages [1] -->
First, the optimal geometry considering the dual erosion effects of waves and tides is determined. On the basis of reasonably limiting the shape selection range,by establishing the Dynamic Model of the Sandcastle Foundation based on the evaluation index of the comprehensive sand and sand carrying capacity of waves and tides, we use COMSOL to accurately simulate the movement state of the sand castle foundation. On this basis, by creating the Sandcastle Foundation Damage Index, we reasonably determine the duration of the sandcastle. Finally, we use a Discrete Global Optimization Algorithm Based on Successive Descent Methods to determine the shape of the optimal sandcastle foundation as a cylinder.

<!-- b000012 | prose | pages [1] -->
Secondly, the optimal water-sand mixing ratio is determined. Based on Model 1, a model of Water-sand Aggregation-water-sand Ratio Relationship was first established. By limiting the allowed degree of polymerization, the water-sand ratio is limited to a reasonable range. We again use the discrete global optimization algorithm based on the successive descent method to efficiently find the optimal water-sand mix ratio of 0.739.

<!-- b000013 | prose | pages [1] -->
Further, an optimal geometry considering rain erosion is determined. We define the sandcastle collapse limit coefficient, and comprehensively establish the Rainwater Erosion Resistance Quantification Model by integrating the ability to resist rainwater infiltration and the evacuation ratio of the sandcastle structure. Further, A Quantified Model of Sandcastle's Ability to Resist Wave Erosion was established. Considering two indicators of anti-erosion ability and establishing a fuzzy comprehensive evaluation model, we determine that the optimal shape is still a cylinder.

<!-- b000014 | prose | pages [1] -->
Finally, we use the method of humidifying and spraying the adhesive when the air humidity is the lowest to improve the stability of the sand castle foundation. A Humidity Prediction Model Based on the RBF Neural Network Algorithm was established, and we used the model to test the humidity of Venice Beach on August 1. Based on the air humidity data obtained in the previous month, we divided the weather conditions into sunny and cloudy days, and predicted the air humidity trends for sunny and cloudy days on August 1, respectively. Finally, we decided to humidify the sandcastle foundation and spray the adhesive at 13:30 on a cloudy day and 13:00 on a sunny day.

<!-- b000015 | furniture | pages [1] -->
关注数学模型

<!-- b000016 | furniture | pages [1] -->
2

<!-- b000017 | furniture | pages [1] -->
MATHmodels

<!-- b000018 | furniture | pages [1] -->
获取更多资讯

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1. Introduction............................................................................................................................................3

<!-- b000021 | contents | pages [2] -->
1.1 Background.....................................................................................................................................3

<!-- b000022 | contents | pages [2] -->
1.2 Restatement of the Problem............................................................................................................3

<!-- b000023 | contents | pages [2] -->
2.Assumption and Justification................................................................................................................ 3

<!-- b000024 | contents | pages [2] -->
3.Glossary and Notation............................................................................................................................4

<!-- b000025 | contents | pages [2] -->
3.1 Glossary..........................................................................................................................................4

<!-- b000026 | contents | pages [2] -->
3.2 Notation..........................................................................................................................................4

<!-- b000027 | contents | pages [2] -->
4. Optimal Shape Model Based on Sandcastle Foundation Dynamics Model......................................4

<!-- b000028 | contents | pages [2] -->
4.1 Model Overview.............................................................................................................................4

<!-- b000029 | contents | pages [2] -->
4.2 Quantitative model of sand-bearing capacity................................................................................5

<!-- b000030 | contents | pages [2] -->
4.3 Sandcastle Foundation dynamics equation model.........................................................................5

<!-- b000031 | contents | pages [2] -->
4.4 Solution of Sandcastle Foundation Dynamics Equation Model....................................................6

<!-- b000032 | contents | pages [2] -->
4.5 Geometric Shape Solving Model Based on Discrete Global Optimization Algorithm..................9

<!-- b000033 | contents | pages [2] -->
5. Optimal water and sand ratio model................................................................................................. 11

<!-- b000034 | contents | pages [2] -->
5.1 Model Overview...........................................................................................................................11

<!-- b000035 | contents | pages [2] -->
5.2 Quantitative model of Water and sand polymerization degree.................................................... 11

<!-- b000036 | contents | pages [2] -->
5.3 Solving the Model........................................................................................................................ 12

<!-- b000037 | contents | pages [2] -->
6.Fuzzy comprehensive evaluation model based on rain erosion resistance......................................13

<!-- b000038 | contents | pages [2] -->
6.1 Model Overview...........................................................................................................................13

<!-- b000039 | contents | pages [2] -->
6.2 Evaluation model for rain erosion resistance.............................................................................. 13

<!-- b000040 | contents | pages [2] -->
6.3 Optimal Shape Fuzzy Comprehensive Evaluation Model............................................................14

<!-- b000041 | contents | pages [2] -->
7. Humidity Prediction Model Based on RBF Neural Network Algorithm....................................... 16

<!-- b000042 | contents | pages [2] -->
7.1 Model Overviw.............................................................................................................................16

<!-- b000043 | contents | pages [2] -->
7.2 Model Preparation........................................................................................................................ 16

<!-- b000044 | contents | pages [2] -->
7.3 RBF neural network algorithm.....................................................................................................17

<!-- b000045 | contents | pages [2] -->
8. Sensitivity Analysis.............................................................................................................................. 18

<!-- b000046 | contents | pages [2] -->
8.1 Sensitivity Analysis of Most Shaped Model ............................................................................... 18

<!-- b000047 | contents | pages [2] -->
8.2 Sensitivity Analysis of Optimal Water-Sand Mixing Model....................................................... 18

<!-- b000048 | contents | pages [2] -->
8.3 Sensitivity Analysis of A Fuzzy Comprehensive Evaluation Mode............................................ 20

<!-- b000049 | contents | pages [2] -->
8.4 Sensitivity Analysis of Sandcastle warning protection Model.....................................................20

<!-- b000050 | contents | pages [2] -->
9. Evaluation and Promotion of Model..................................................................................................21

<!-- b000051 | contents | pages [2] -->
9.1 Strength and Weakness.................................................................................................................21

<!-- b000052 | contents | pages [2] -->
9.2 Promotion..................................................................................................................................... 22

<!-- b000053 | contents | pages [2] -->
10. Conclusions.........................................................................................................................................22

<!-- b000054 | contents | pages [2] -->
References..................................................................................................................................................23

<!-- b000055 | contents | pages [2] -->
Memo.........................................................................................................................................................24

<!-- b000056 | contents | pages [2] -->
Appendix....................................................................................................................................................25

<!-- b000057 | furniture | pages [2] -->
关注数学模型

<!-- b000058 | furniture | pages [2] -->
2

<!-- b000059 | furniture | pages [2] -->
MATHmodels

<!-- b000060 | furniture | pages [2] -->
获取更多资讯

<!-- b000061 | furniture | pages [3] -->
Team # 2010821

<!-- b000062 | furniture | pages [3] -->
Page 3 of 24

<!-- b000063 | heading | pages [3] -->
1. Introduction

<!-- b000064 | heading | pages [3] -->
1.1 Background

<!-- b000065 | prose | pages [3] -->
Nowadays, people always face heavy schooling or busy work, and spending some time at the beach allows people to enjoy the cool sea breeze, warm sunshine, and soft beaches. Therefore, more and more people choose to go to the beach for leisure. Building sandcastles is a must-do item for beach leisure. It can develop children's creativity and reduce adults' stress to a great extent. When people build sandcastles, they always want their sandcastles to be beautiful and to last longer. Therefore, it is necessary to study how to keep the sandcastle on the beach for the longest time.

<!-- b000066 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000067 | prose | pages [3] -->
Building sandcastles is one of the most popular activities item for children on the beach. Every child wants his sandcastle to last for a long time on the beach. Therefore, we were asked to study the persistent retention of sandcastles on the beach. The specific issues are as follows:

<!-- b000068 | prose | pages [3] -->
Below environmental factors are assumed to be the same, such as: the distance of the beach from  the water, the kind of sand, the amount of sand, the same water-sand ratio. We were asked to build a model under the action of waves and tides to explore the basic geometry of the sandcastle that can last for the longest time on the beach.

<!-- b000069 | prose | pages [3] -->
Without using any additional additives, how to change the water-sand ratio of the sandcastle  foundation can make our sandcastle last for the longest time on the beach.

<!-- b000070 | prose | pages [3] -->
Built on the original model, we have considered the impact of rain on the foundation of the  sandcastle, and upgrade and optimize the model to further explore the optimal geometry of the sandcastle.

<!-- b000071 | prose | pages [3] -->
By consulting some relevant literatures, other strategies have been investigated to improve the  retention time of sandcastles.

<!-- b000072 | prose | pages [3] -->
2.Assumption and Justification

<!-- b000073 | prose | pages [3] -->
We make some general assumptions to simplify our model. These assumptions and corresponding justification are listed below:

<!-- b000074 | prose | pages [3] -->
It is assumed that the base area and height of each considered shape are the same, and that there is  no significant difference in the sand quality and sand quantity of our sandcastle foundation.

<!-- b000075 | prose | pages [3] -->
Sandcastle foundations are built at approximately the same distance from the water.  In the process of natural erosion, ignore the situation of huge waves and winds sweeping the  sandcastle far from the original location.

<!-- b000076 | prose | pages [3] -->
We only consider the impact of waves, tides and rain on the water-sand ratio of the sandcastle  foundation.

<!-- b000077 | prose | pages [3] -->
The sand particles at the sandcastle foundation are evenly distributed.  Assume that people will spray the adhesive in time after the warning occurs, and the adhesive  viscosity lasts at least 8 hours.

<!-- b000078 | prose | pages [3] -->
More detailed assumptions will be listed if needed.

<!-- b000079 | furniture | pages [3] -->
关注数学模型

<!-- b000080 | furniture | pages [3] -->
2

<!-- b000081 | furniture | pages [3] -->
MATHmodels

<!-- b000082 | furniture | pages [3] -->
获取更多资讯

<!-- b000083 | furniture | pages [4] -->
Team # 2010821

<!-- b000084 | furniture | pages [4] -->
Page 4 of 24

<!-- b000085 | prose | pages [4] -->
3.Glossary and Notation

<!-- b000086 | heading | pages [4] -->
3.1 Glossary

<!-- b000087 | prose | pages [4] -->
Wave current: refers to the combined effect of waves and tides.  Damage index: It takes the change of the base area and height of the sandcastle as a measuring  factor to describe the damage degree of the sandcastles.

<!-- b000088 | heading | pages [4] -->
3.2 Notation

<!-- b000089 | caption | pages [4] -->
Table 1 Notation

<!-- b000090 | heading | pages [4] -->
Symbols

<!-- b000091 | prose | pages [4] -->
Definition

<!-- b000092 | prose | pages [4] -->
sF sand-bearing capacity

<!-- b000093 | prose | pages [4] -->
G Damage Index

<!-- b000094 | prose | pages [4] -->
Q Water and sand polymerization degree

<!-- b000095 | prose | pages [4] -->
n Water-sand ratio p

<!-- b000096 | prose | pages [4] -->
i F ability to resist rainwater infiltration u

<!-- b000097 | prose | pages [4] -->
sandcastle structure evacuation ratio i R

<!-- b000098 | prose | pages [4] -->
i rain erosion resistance H1

<!-- b000099 | prose | pages [4] -->
i H 2 wave current erosion resistance

<!-- b000100 | prose | pages [4] -->
 g Neural Network Radial Basis Function

<!-- b000101 | heading | pages [4] -->
4. Optimal Shape Model Based on Sandcastle Foundation Dynamics

<!-- b000102 | heading | pages [4] -->
Model

<!-- b000103 | heading | pages [4] -->
4.1 Model Overview

<!-- b000104 | prose | pages [4, 5] -->
In terms of shape selection, considering the common sandcastle basic shapes that people are accustomed to using, we only consider the most suitable ones from a cuboid with a certain aspect ratio, an elliptical cylinder with a certain aspect ratio, and a sector with a certain radius and arc length ratio. Excellent shape.First, we have established a model for assessing the sand-bearing capacity of waves. Based on this, the basic dynamics equation of the sandcastle foundation is established. Secondly, by creating a sandcastle foundation damage index, we have determined the duration of a sandcastle of a specific shape. Further, based on the duration of some specific shape sandcastles, we have used a discrete global optimization algorithm based on successive descent methods to determine the optimal sandcastle shape in the global state[1].

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

<!-- b000112 | heading | pages [5] -->
4.2 Quantitative model of sand-bearing capacity

<!-- b000113 | prose | pages [5] -->
Because wave and tide are the two main driving forces in the sand movement of sandcastles, we first have considered how the sandcastles are impacted under the action of waves and tides, and choose to define this ability using the capacity of sand-bearing.

<!-- b000114 | prose | pages [5] -->
Considering tidal and wave sand-bearing capacity:

<!-- b000115 | prose | pages [5] -->
(1) C C C   * * * C W The capacity of sand-bearing under tide effect can be expressed as:    n V 2 2 u v  p (2) C   * C C 2 1 n  C h  p z w s Where, n represents the initial value of the water-sand ratio of the sandcastle foundation, which is p determined by the volume ratio;V is the initial value of the sandy volume of the sandcastle foundation; u and v represents the components of the water flow velocity x and y the sum of the waves under the action of waves and tides; is the height of seawater level; is the positive definite coefficient; h w C indicates sand-bearing speed. s Regarding the capacity of sand-bearing under the action of waves, we consider the unbroken wave  and the broken wave respectively, which can be expressed as:

<!-- b000116 | prose | pages [5] -->
n V 3 1 f H D p (3) C     W rms B   * 1 2 W 3 1 1 n n h    3 sinh T gh kh  p p w s s w w Where, and are respectively the positive definite coefficients of the unbroken wave and the broken  1 2 wave; wf represents the wave friction coefficient; is the mean square wave height, 2 H H H  ， rms rms s H Is the effective wave height; T is the wave period; k is the wave quantization value of one period; s D represents the wave energy dissipation due to the wave breaking. B We build the capacity of sand-bearing sF as:    (4) F C V     * s r s Where,  indicates the sand settling coefficient. r

<!-- b000117 | heading | pages [5] -->
4.3 Sandcastle Foundation dynamics equation model

<!-- b000118 | prose | pages [5, 6] -->
We use the right-angle vertex of the three-dimensional geometry as the coordinate center to establish a three-dimensional right-angle coordinate system. Then,changes of and h over timet of our x, y sandcastle foundation satisfy the following equations in dynamic             hV huV hvV hV hV            v v F      (5)   x y s t x y x x y y            Where, yv is the horizontal diffusion coefficient. h indicates the height of the sandcastle foundation; xv and In the dynamic simulation process, we give the constraint that the normal flux is 0 to determine the solid boundary condition as:

<!-- b000119 | furniture | pages [5] -->
关注数学模型

<!-- b000120 | furniture | pages [5] -->
2

<!-- b000121 | furniture | pages [5] -->
MATHmodels

<!-- b000122 | furniture | pages [5] -->
获取更多资讯

<!-- b000123 | furniture | pages [6] -->
Team # 2010821

<!-- b000124 | furniture | pages [6] -->
Page 6 of 24

<!-- b000126 | prose | pages [6] -->
V  (6) 0   n  Where,  represents the total flux through the sandcastle foundation; nrepresents the normal vector.  At the same time, we give the time course of the sand volume as the open boundary condition:  t , , V V x y (7) 

<!-- b000127 | heading | pages [6] -->
4.4 Solution of Sandcastle Foundation Dynamics Equation Model

<!-- b000128 | heading | pages [6] -->
4.4.1 Solution of Cuboid Dynamics Simulation

<!-- b000129 | prose | pages [6] -->
Step1. Initialize the parameters of the sandcastle foundation dynamics equation. We take the  optimal shape of a cuboid as an example and define the aspect ratio of the bottom of the cuboid as x, y its shape factor, which is . The initial values of in the equation correspond to , l, w : e l w 1  respectively. In combination with relevant literature, the parameter initialization values in the given dynamic equation are shown in the following table

<!-- b000130 | caption | pages [6] -->
Table 2 Parameter Determination

<!-- b000131 | prose | pages [6] -->
symbol Numerical value symbol Numerical value symbol Numerical value   0.023 0.300 5.000 T C 1 H C  0.249 0.001 5.185 rms 2 z Wf  D 1.489 1.570 6.301 s B

<!-- b000132 | caption | pages [6] -->
Table 3 Assignment Table for Initialization Variables

<!-- b000133 | prose | pages [6] -->
symbol Numerical value symbol Numerical value

<!-- b000134 | prose | pages [6] -->
n h 900 6.0 p w

<!-- b000135 | prose | pages [6, 7] -->
u x 30 1.0 y v 30 1.0 V 100 1 FIG 1. Cuboid simulation diagram when t is equal to zero We use COMSOL to solve the dynamic equations and simulate the pressure effect of wave current 0.1 e on the bottom surface of cuboid. The pressure distribution at time shown in the figure 1  0 t  above is obtained. Among them, the wave current starts from the red part and the pressure gradually decreases. Step2. Establish a damage index indicator model. In order to describe the degree of damage of  the sandcastle and better explain the meaning of duration, we take the change in base area and height as the measuring factor, and give the definition of damage index as (8) G S h       s h Where, and represent respectively the increase in the bottom area of the sandcastle and the decrease S h in the minimum height of the sandcastle, over a period of time; and are the influence factors of the s h change in the bottom area and the height, respectively.

<!-- b000136 | furniture | pages [6] -->
关注数学模型

<!-- b000137 | furniture | pages [6] -->
2

<!-- b000138 | furniture | pages [6] -->
MATHmodels

<!-- b000139 | furniture | pages [6] -->
获取更多资讯

<!-- b000140 | furniture | pages [7] -->
Team # 2010821

<!-- b000141 | furniture | pages [7] -->
Page 7 of 24

<!-- b000143 | prose | pages [7] -->
It should be noted that in the real practice, changes are both uncertain of base areas and heights. The sandcastle foundation undergoes the process of waves and tidal effects. The sand at the bottom layer will spread under the effect of erosion, resulting in a reduction in the height of the sandcastle foundation and an increase in its bottom area. The impact of the simplified process on the sandcastle is shown in FIG 1. below:

<!-- b000144 | prose | pages [7, 8] -->
FIG 2. Simplified model of sandcastle foundation erosion The cubic three-dimensional geometry in the figure represents the original state of the sandcastle foundation, and the dashed line represents the existing state after the sandcastle has been eroded. The increase of the base area and the decrease of the height of the existing state compared with the original state are the quantity of the damage index. Step3. Find the relationship between the damage index over time. We obtain that the sand level  is eroded by the waves and tides for a period of time, and the water level at the new time and ' h w ' n , and the wave current velocity in the x and y directions are 'u and 'v , the water-sand ratio S  p and of the sandcastle foundation. We discretize the time, set the completion time of the h  sandcastle to zero, that is, is the initial time point, and then take the time points at equal 0 t  intervals to draw a scatter plot as shown in the figure.

<!-- b000145 | furniture | pages [7] -->
关注数学模型

<!-- b000146 | furniture | pages [7] -->
2

<!-- b000147 | furniture | pages [7] -->
MATHmodels

<!-- b000148 | furniture | pages [7] -->
获取更多资讯

<!-- b000149 | furniture | pages [8] -->
Team # 2010821

<!-- b000150 | furniture | pages [8] -->
Page 8 of 24

<!-- b000152 | prose | pages [8] -->
FIG 3. Damage index over time The diagram illustrates the damage indicator function established and the line connecting the points at equal intervals. It should be shown that the discrete points after point B are almost on the same horizontal line. As a result, it is revealed that the sandcastle is completely damaged, with a corresponding damage index . Based on that, damage factor is defined with coefficient G max being , that is, when , it is considered that the sandcastle has been damaged to the 0.52 0.52G G    max maximum bearing degree. On this basis, we take point A as the critical time point, which refers to the corresponding time to the maximum degree of damage which could bear, and the time corresponding to that point is the duration . T/ day At the same time, we define the duration of any sandcastle foundation constructed from a three- dimensional geometric shape from the stacking to the critical time point as T . The longer the duration, the better the shape corresponds to the sandcastle foundation.

<!-- b000153 | prose | pages [8] -->
We simulate the damage index and duration of 10 groups of cuboids with different shape 1e under the action of waves and tides. It should be noted that the 10 sets of data we have obtained factors are only the first step in obtaining the global optimal solution. The next step is shown in the next model. The 10 sets of data are shown in the following table:

<!-- b000154 | furniture | pages [8] -->
关注数学模型

<!-- b000155 | furniture | pages [8] -->
2

<!-- b000156 | furniture | pages [8] -->
MATHmodels

<!-- b000157 | furniture | pages [8] -->
获取更多资讯

<!-- b000158 | furniture | pages [9] -->
Team # 2010821

<!-- b000159 | furniture | pages [9] -->
Page 9 of 24

<!-- b000160 | caption | pages [9] -->
Table 4 Corresponding duration of cuboids with different aspect ratios

<!-- b000161 | prose | pages [9] -->
Shape factor Duration Shape factor Duration 1.0 2.5 3.5 1.2 1.5 2.4 4.0 1.4 2.0 2.1 4.5 2.8 2.5 2 5.0 2.0 3.0 1.8 5.5 2.6

<!-- b000162 | heading | pages [9] -->
4.4.2 Simulation solution of dynamics equations of elliptic cylinder and sector cylinder

<!-- b000163 | prose | pages [9] -->
We consider the damage index and duration corresponding to the parameters of the other two common three-dimensional geometric shapes. The detailed data results of the simulation are shown in the appendix.

<!-- b000164 | prose | pages [9] -->
We define the ratio of the long axis to the short axis of the ellipse as its shape factor, which  is . Based on this, a dynamic equation solving model is established, and the simulation : e a b 2  1 e simulation graph at is shown as follows: 2  Taking the ratio of the radius r of the sector cylinder to the arc length l as the coefficient 3e , we  take the sector cylinder of as an example to make the following simulation: 1 e 3  

<!-- b000165 | prose | pages [9] -->
FIG 4. Cylinder simulation diagram FIG 5. Sector cylinder simulation diagram

<!-- b000166 | heading | pages [9] -->
4.5 Geometric Shape Solving Model Based on Discrete Global Optimization

<!-- b000167 | heading | pages [9] -->
Algorithm

<!-- b000168 | heading | pages [9] -->
4.5.1 Model Overview

<!-- b000169 | prose | pages [9, 10] -->
  By solving the dynamic equation of the sandcastle foundation, we can get the duration 3,2,1 Ti i    3,2,1 of sandcastle foundation shape under the control of ei i . However, in order to find the optima  value of iT , we try to establish an optimal three-dimensional geometric model with a Discrete Global Optimization Algorithm as the core. On this basis, we can find the optimal coefficient value   of any of the three shapes, so that the shape we choose has the longest duration. 3,2,1 ei i 

<!-- b000170 | furniture | pages [9] -->
关注数学模型

<!-- b000171 | furniture | pages [9] -->
2

<!-- b000172 | furniture | pages [9] -->
MATHmodels

<!-- b000173 | furniture | pages [9] -->
获取更多资讯

<!-- b000174 | furniture | pages [10] -->
Team # 2010821

<!-- b000175 | furniture | pages [10] -->
Page 10 of 24

<!-- b000177 | heading | pages [10] -->
4.5.2 Model establishment and solution

<!-- b000178 | prose | pages [10] -->
We still take the cuboid as an example. Through simulation, we can obtain the duration under multiple sets of coefficients. In this regard, we use these data to deduce the Discrete Global Optimization Algorithm based on the successive descent method. The specific steps are as follows:

<!-- b000179 | prose | pages [10] -->
Step1. Successive Descent method to find discrete local minimum points. (1) set the set E as    : \   f e d f e d the Cuboid shape factor selection point, satisfy n if   , let    , cycle this E  R k k step;determine whether is 0 to determine whether to update the  ke discrete local minima, after ,we get the discrete global minima .

<!-- b000180 | prose | pages [10] -->
Step2. Construct a discrete fill function. Let initialization   -5 , ,2,1 , 10 V V p j n conditions   , , ;     . 1 0.01 r q  0   0 j The constructed discrete fill function is:

<!-- b000181 | prose | pages [10] -->
1         ,  , , max  0, F e e q r f e f e r     (9) k k q k k  q e e   k k

<!-- b000182 | prose | pages [10] -->
Step3 .If , the algorithm is terminated, and local r    ke variable can be used as the discrete global minimum, otherwise, the next step is performed.

<!-- b000183 | prose | pages [10] -->
Step4. If D   , go to step 6, otherwise, go to the next step.

<!-- b000184 | prose | pages [10] -->
10 Step5. If r  r 2 , then make , , 10 10 q q  0q   10 , go to the step 2, otherwise, let q  q , go to the step2 D  D 0 Step6. Take any direction , so that , enter d  D D D d   the inner loop phase, change the initial value of D , and cycle the corresponding steps. When the parameter r are sufficiently small, it is believed that there is no better local minimum point in the selected point set E .

<!-- b000185 | prose | pages [10] -->
From the dynamic model, we can get the corresponding duration T for each assignment, and with as the objective function, we optimize it by the algorithm: 1 K T     min , n K f e e R   (10) k k 1 max T  (11) K Similarly to the other two shape models, we can use the Discrete Global Optimization Algorithm to find the maximum T in the duration controlled by the three shape scale as shown in the following table:

<!-- b000186 | furniture | pages [10] -->
关注数学模型

<!-- b000187 | furniture | pages [10] -->
2

<!-- b000188 | furniture | pages [10] -->
MATHmodels

<!-- b000189 | furniture | pages [10] -->
获取更多资讯

<!-- b000190 | furniture | pages [11] -->
Team # 2010821

<!-- b000191 | furniture | pages [11] -->
Page 11 of 24

<!-- b000192 | caption | pages [11] -->
Table 5 Table of the best shape parameters for the three shapes

<!-- b000193 | prose | pages [11] -->
Geometric shape shape factor Duration Cuboid 1.46 2.9 1.00 4.8 Elliptic cylinder 3.0 3.7 Sector cylinder  From the data in the above table, we can clearly conclude that when the base area is constant and the ratio of the long axis to the short axis is 1, the sandcastle foundation can last the longest time. We approximate it as a cylinder with a maximum duration of 4.8 days.

<!-- b000194 | heading | pages [11] -->
5. Optimal water and sand ratio model

<!-- b000195 | heading | pages [11] -->
5.1 Model Overview

<!-- b000196 | prose | pages [11] -->
We use the optimal shape model based on the sandcastle foundation dynamics model to obtain the optimal shape of the sandcastle foundation with the longest duration when the water-sand ratio is constant. However, the size of the water-sand ratio will also directly affect the erosion resistance of the sandcastle foundation. We have introduced the equation of the relationship between the water-sand polymerization degree and the water-sand ratio, and at the same time limit the allowed polymerization degree range to obtain a reasonable water-sand ratio Range, and then by solving the model, the optimal water-sand ratio is obtained[2].

<!-- b000197 | heading | pages [11] -->
5.2 Quantitative model of Water and sand polymerization degree

<!-- b000198 | prose | pages [11] -->
We consider the aggregation of water and sand, leading to the concept of the degree of water-sand polymerization. We give the definition of the degree of polymerization of water and sand based on the volume change of the water and sand specific gravity before and after polymerization:

<!-- b000199 | prose | pages [11, 12] -->
1 1   V V    1 2     1 100 % Q    1 2 (12)   V V  1 2     Where, V , V respectively represent the volume of sand and water before mixing; and represent the 1  1 2 2 water absorption coefficient and water solubility coefficient, respectively. We use these two coefficients to express the polymerization ability of water and sand. We simplify the equation with the water-sand n : ratio p   n   1   p          1 2 1 100 % Q    (13)   1 n    p   We use MATLAB to solve this equation and get the relationship curve between the degree of Water and sand polymerization and the ratio of water and sand, as shown in FIG 6.

<!-- b000200 | furniture | pages [11] -->
关注数学模型

<!-- b000201 | furniture | pages [11] -->
2

<!-- b000202 | furniture | pages [11] -->
MATHmodels

<!-- b000203 | furniture | pages [11] -->
获取更多资讯

<!-- b000204 | furniture | pages [12] -->
Team # 2010821

<!-- b000205 | furniture | pages [12] -->
Page 12 of 24

<!-- b000207 | prose | pages [12] -->
FIG 6.Degree of convergence of water and sand The degree of water-sand polymerization increases with the increase of water-sand ratio. We must consider not only the relatively large cohesiveness, but also the optimization of erosion resistance, that is, the longest duration. In combination with the actual situation, we choose a two-point interval with a large viscosity range as shown in our figure as our optimization constraint.

<!-- b000208 | heading | pages [12] -->
5.3 Solving the Model

<!-- b000209 | prose | pages [12] -->
We use the sandcastle foundation dynamics model in Question 1 as the basis, use the optimal n as a variable proportion of the best shape we selected, and use the initial value of the water-sand ratio p to discretely process the target T in the same way:

<!-- b000210 | prose | pages [12] -->
S First put into the dynamic equation (1), according to the change of sandcastle foundations and  h , the relationship between the damage index and time is obtained, and the constraint condition is  added:

<!-- b000211 | prose | pages [12] -->
7.0 .0 85 n   (14) p n equally spaced points: Find the duration table record of p

<!-- b000212 | caption | pages [12] -->
Table 6 Corresponding duration of different water-sand ratios

<!-- b000213 | prose | pages [12, 13] -->
Water-sand ratio Duration Water-sand ratio Duration 0.70 4.7 0.78 5.1 0.72 4.9 0.80 5.0 0.74 5.2 0.82 4.3 0.76 4.8 0.84 4.2 Using the Discrete Global Optimization Algorithm of the best shape model in Problem 1, we can .0 739 n conclude that when the water-sand ratio is , the longest duration of the sandcastle foundation  p is achieved under the condition of ensuring good shape adhesion.

<!-- b000214 | furniture | pages [12] -->
关注数学模型

<!-- b000215 | furniture | pages [12] -->
2

<!-- b000216 | furniture | pages [12] -->
MATHmodels

<!-- b000217 | furniture | pages [12] -->
获取更多资讯

<!-- b000218 | furniture | pages [13] -->
Team # 2010821

<!-- b000219 | furniture | pages [13] -->
Page 13 of 24

<!-- b000221 | prose | pages [13] -->
6.Fuzzy comprehensive evaluation model based on rain erosion resistance

<!-- b000222 | heading | pages [13] -->
6.1 Model Overview

<!-- b000223 | prose | pages [13] -->
Aiming at the erosion of sandcastles by waves and tides, we have established some models to obtain the optimal shape of the sandcastle foundation as a cylinder.However, the actual erosion risk facing sandcastles is not limited to the effects of waves and tides. We should also consider the erosion of rainwater.Based on the cuboids, ellipses, and sectors at the optimal shape coefficients obtained in Problem 1, we have further addressed the problem of rain erosion., we define the sandcastle collapse limit coefficient, and comprehensively establish the rain erosion resistance assessment model by comprehensively ability to resist rainwater infiltration and sandcastle structure evacuation ratio. On this basis, an evaluation model of sandcastle anti-wave erosion ability is constructed. Finally, a fuzzy comprehensive evaluation model is established to evaluate the optimal sandcastle shape under the action of waves and rain[3].

<!-- b000224 | heading | pages [13] -->
6.2 Evaluation model for rain erosion resistance

<!-- b000225 | heading | pages [13] -->
6.2.1 Establishment of Model

<!-- b000226 | prose | pages [13] -->
Before establishing a fuzzy comprehensive evaluation model for the optimal shape of the sandcastle foundation, we set up the evaluation model of rain erosion resistance as follows:

<!-- b000227 | prose | pages [13] -->
First, the sandcastle's ability to resist rainwater infiltration is established as follows[4]:   i 2 i 1 i 2 i 1 (15) F R R R      u a a a Where,   F i 3,2,1 i represents the ability of the cuboid, cylinder and sector cylinder to resist rain  u i Q infiltration. represents the degree of aggregation of the three shapes of gravel, respectively.

<!-- b000228 | prose | pages [13] -->
  . represents positive definite coefficient. represents the sandcastle i i ni 3,2,1 R n n i      1 1 a p collapse collapse collapse limit coefficients of the three shapes, respectively.

<!-- b000229 | prose | pages [13] -->
Secondly, the evacuation ratio indicators for establishing the sandcastle structure are as follows:     i = i R Q V V   (16)   2 f DL Where,   V .  represents positive definite coefficient. represents the shear capacity of Ri 3,2,1 i  2 f V sandcastle gravel. represents the shear force on the sand under the rain gravity load. DL Finally, an assessment model for rainwater erosion resistance is established:

<!-- b000230 | prose | pages [13, 14] -->
i i i i H F n R   (17) 1 u collapse Where,   represents rainwater erosion resistance of the three shapes. H i 3,2,1 i  1

<!-- b000231 | furniture | pages [13] -->
关注数学模型

<!-- b000232 | furniture | pages [13] -->
2

<!-- b000233 | furniture | pages [13] -->
MATHmodels

<!-- b000234 | furniture | pages [13] -->
获取更多资讯

<!-- b000235 | furniture | pages [14] -->
Team # 2010821

<!-- b000236 | furniture | pages [14] -->
Page 14 of 24

<!-- b000238 | heading | pages [14] -->
6.2.2 Solution of Model

<!-- b000239 | prose | pages [14] -->
In order to solve the model, we consulted some literatures and defined below parameters as shown in the following table:

<!-- b000240 | caption | pages [14] -->
Table 7 Number of rain erosion resistance model

<!-- b000241 | heading | pages [14] -->
Symbols

<!-- b000242 | prose | pages [14] -->
Numerical value     10.6， 12.1 ，  1 2 0.125 np     .1,1 24 .1, 56 1 2 3 n n n ， ， collapse collapse collapse V 305 f V 355 DL Then, we obtained the rainwater erosion resistance of cuboids, cylinders, and sectors as shown in the following table:

<!-- b000243 | caption | pages [14] -->
Table 8 Resistance to rain erosion

<!-- b000244 | prose | pages [14] -->
Geometric shape Numerical value 50.6 cuboid 63.5 cylinder 68.1 thick sector

<!-- b000245 | heading | pages [14] -->
6.3 Optimal Shape Fuzzy Comprehensive Evaluation Model

<!-- b000246 | heading | pages [14] -->
6.3.1 Establishment of Model

<!-- b000247 | prose | pages [14] -->
Based on the evaluation model of sandcastle resistance to rain erosion, we first establish the evaluation model of sandcastle resistance to wave current erosion as follows:

<!-- b000248 | prose | pages [14] -->
i H T   (18) 2 3 i Where,   represents the resistance to wave current erosion of the three shapes. stands for H i 3,2,1 i   2 3 positive definite coefficient.

<!-- b000249 | prose | pages [14] -->
It should be noted that, in order to determine whether the cuboid, elliptic cylinder and fan-shaped body are still optimal with the optimal shape coefficient, we have established the optimal shape fuzzy synthesis based on the numerical values of the different capabilities of the three shapes. The evaluation model is as follows:

<!-- b000250 | furniture | pages [14] -->
关注数学模型

<!-- b000251 | furniture | pages [14] -->
2

<!-- b000252 | furniture | pages [14] -->
MATHmodels

<!-- b000253 | furniture | pages [14] -->
获取更多资讯

<!-- b000254 | furniture | pages [15] -->
Team # 2010821

<!-- b000255 | furniture | pages [15] -->
Page 15 of 24

<!-- b000256 | prose | pages [15] -->
Step1.Determine membership function. We take the ratio of the ability to resist wave current  erosion or rain erosion to the total shape of the three shapes as the membership, so we establish membership functions as follows:

<!-- b000257 | prose | pages [15] -->
i H   i H   1 1 1 H 3 (19)  i H 1 1 i  i H   i H   2 2 2 H (20) 3  i H 2 1 i  Step2.Calculate membership table based on membership function. We substitute the values of  the two capabilities of the three shapes into Formula   , calculate the membership table of the 19 , 20 optimal shape, and establish a fuzzy relation matrix.

<!-- b000258 | prose | pages [15] -->
Step3.Determine the weight of the two capabilities in the optimal evaluation. We have  considered that when our sandcastle faces seawater, tidal erosion and rainwater erosion at the same time, the erosion degree of rainwater on sandcastle is much greater than that of seawater and tide on   7.0,3.0 A  sandcastle. Therefore, we set the weight of the two capabilities in decision making to :

<!-- b000259 | prose | pages [15] -->
Step4：Calculate comprehensive evaluation results. The calculation formula for the  comprehensive evaluation results is as follows:

<!-- b000260 | prose | pages [15] -->
(21) B A R  

<!-- b000261 | heading | pages [15] -->
6.3.2 Solution of Model

<!-- b000262 | prose | pages [15] -->
In order to solve the model, we have determined the calculation parameters and calculation results by referring to the online information and citing reference parameters:

<!-- b000263 | caption | pages [15] -->
Table 9 Number of wave current erosion resistance model

<!-- b000264 | heading | pages [15] -->
Symbols

<!-- b000265 | prose | pages [15] -->
Numerical value 13.44  3     2.5,8.6,6.2 , , T T T 1 2 3

<!-- b000266 | prose | pages [15] -->
Then, we obtained the anti-wave erosion ability of cuboid, cylinder and fan-shape cylinder as shown in the following table:

<!-- b000267 | caption | pages [15] -->
Table 10 Resistance to wave erosion

<!-- b000268 | prose | pages [15, 16] -->
Geometric shape Numerical value rectangle 34.94 roundness 91.39 sector 69.89 The membership degrees corresponding to the three shapes according to the membership function are shown in Table 11:

<!-- b000269 | furniture | pages [15] -->
关注数学模型

<!-- b000270 | furniture | pages [15] -->
2

<!-- b000271 | furniture | pages [15] -->
MATHmodels

<!-- b000272 | furniture | pages [15] -->
获取更多资讯

<!-- b000273 | furniture | pages [16] -->
Team # 2010821

<!-- b000274 | furniture | pages [16] -->
Page 16 of 24

<!-- b000276 | caption | pages [16] -->
Table 11 Competency assessment membership scale

<!-- b000277 | prose | pages [16] -->
Evaluation index Cuboid Cylinder Sector cylinder Rain erosion resistance 0.278 0.348 0.374 wave current erosion resistance 0.178 0.466 0.356

<!-- b000278 | prose | pages [16] -->
This determines the fuzzy relation matrix:

<!-- b000279 | prose | pages [16] -->
0.278 0.348 0.374   R  (22)   0.178 0.466 0.356   7.0,3.0 Since the weight of the project in decision-making is A ,the comprehensive evaluation  obtained is:

<!-- b000280 | prose | pages [16] -->
  = 0.208 0.430 0.361 B A R   (23) ， ，

<!-- b000281 | prose | pages [16] -->
It can be seen that the stability of cuboids, cylinders, and fan-shape cylinders under the combined action of wave erosion and rain erosion is 0.208, 0.430, and 0361, respectively. By comparison, we can know that the stability of cylinders under double erosion is the highest.

<!-- b000282 | heading | pages [16] -->
7. Humidity Prediction Model Based on RBF Neural Network Algorithm

<!-- b000283 | heading | pages [16] -->
7.1 Model Overviw

<!-- b000284 | prose | pages [16] -->
Sandcastles are products of mixing sand and water. In order to improve the duration of sandcastles, the most important thing is the humidity of the sandcastle and the protection after the production is completed. After consulting the relevant literature, we know that the adhesive protection after the production is also determined by the humidity of the sandcastle. Therefore, when we know the general trend of humidity, we can make the sandcastle last longer. We selected the RBF neural network algorithm as the prediction network, combined with the daily changing characteristics of the beach temperature as an input factor, and proposed a sandcastle humidity prediction model suitable for better extending the sandcastle duration[5].

<!-- b000285 | heading | pages [16] -->
7.2 Model Preparation

<!-- b000286 | prose | pages [16, 17] -->
We take a typical beach, Venice Beach, as an example. The humidity data from August 1 to 3, 2019 was obtained from the U.S. Meteorological Administration. It is worth mentioning that because of the similar sandy conditions and weather conditions of the beach, the Venice Beach we selected is very typical[6]. Index screening:  The humidity of the beach is the result of the combination of many factors, which are closely related to solar radiation, wind, beach temperature, and ground vegetation. We used principal component analysis to find that temperature changes caused by the sun's light intensity had the most significant effect on beach humidity. Therefore, we explore the change of the humidity of the beach under different time and different weather conditions.

<!-- b000287 | furniture | pages [16] -->
关注数学模型

<!-- b000288 | furniture | pages [16] -->
2

<!-- b000289 | furniture | pages [16] -->
MATHmodels

<!-- b000290 | furniture | pages [16] -->
获取更多资讯

<!-- b000291 | furniture | pages [17] -->
Team # 2010821

<!-- b000292 | furniture | pages [17] -->
Page 17 of 24

<!-- b000294 | prose | pages [17] -->
Through observation data, we found that there is a clear correlation between the beach environment humidity and beach temperature, specifically: no matter whether it is sunny or cloudy, as the beach temperature changes over time, the humidity will also change accordingly; however, under sunny weather, Humidity changes on the beach are greater than on cloudy days.

<!-- b000295 | prose | pages [17] -->
In summary, the humidity of the beach is indeed mainly affected by the change of the ambient temperature, and it has a negative correlation with it. We select the ambient temperature at different time periods of the day as the input factor, select 500 input samples, 50 simulated samples, and 50 predicted samples.

<!-- b000296 | heading | pages [17] -->
7.3 RBF neural network algorithm

<!-- b000297 | prose | pages [17] -->
The RBF neural network algorithm has strong non-linear fitting property. It not only has good best approximation performance for complex functions, but also has fast convergence speed.   T Assume that the input vector is , n is the number of input samples, , , , X x x nx   1 2    T h X is the output weight vector, m is the number of hidden nodes, d is the offset, , , , W w w w   1 2 n  is the network output, and g is the radial basis function. Gaussian functions are usually used:   2 /   2 exp g X C X C (24)      i i i Where, is the European norm, and C is the i data center in the network. In this case, the output i of the neural network is:

<!-- b000298 | prose | pages [17] -->
m     h X d w X C     (25) i i 1 i  Through the RBF neural network algorithm, we obtained the humidity change map under sunny and cloudy conditions. Starting from 7:00 am, samples were taken every 30 minutes, as shown in the figure below:

<!-- b000299 | prose | pages [17, 18] -->
FIG 7. Moderate forecast curves for sunny and cloudy days As can be seen from the figure, we should humidify the glue in a timely manner at 13:30 on a cloudy day and at 13:00 on a sunny day. We know that the glue can maintain its viscosity for at least 8 hours, so the humidity starts to increase to 15:00 sandcastles can be protected before reaching basic stability at 21:00. By predicting the change in humidity, humidity prediction of the sandcastle situation is carried out to ensure the longest lasting time.

<!-- b000300 | furniture | pages [17] -->
关注数学模型

<!-- b000301 | furniture | pages [17] -->
2

<!-- b000302 | furniture | pages [17] -->
MATHmodels

<!-- b000303 | furniture | pages [17] -->
获取更多资讯

<!-- b000304 | furniture | pages [18] -->
Team # 2010821

<!-- b000305 | furniture | pages [18] -->
Page 18 of 24

<!-- b000307 | heading | pages [18] -->
8. Sensitivity Analysis

<!-- b000308 | heading | pages [18] -->
8.1 Sensitivity Analysis of Most Shaped Model Based on Sandcastle Foundation

<!-- b000309 | heading | pages [18] -->
Dynamics Model

<!-- b000310 | prose | pages [18] -->
It should be noted that maximum damage coefficients can be selected differently by other people. If the value of is different, the maximum duration corresponding to each shape will change, and the change trend is complex and difficult to determine. Therefore, we need to explore whether there is a stable result (the cylinder has the strongest endurance) for different to prove the stability of the model. Here we continue to determine the stability of the cylinder by continuously taking the value to determine whether the cylinder is still the best shape. The results are as follows:

<!-- b000311 | prose | pages [18] -->
B(0.96,0) A(0.08,0)

<!-- b000312 | prose | pages [18] -->
FIG 8. Judging results As shown in the figure, with as the time interval, we take 24 sample points around 0.04     for analysis. Through graphical analysis, when , a cylinder is still the optimal 0.52   0.08， 0.96     shape. When , the optimal shape becomes a fan or cuboid. Therefore, we believe that our 0.08， 0.96     model is stable when it can withstand the maximum damage factor . In other words, our 0.08， 0.96   model is very robust.

<!-- b000313 | heading | pages [18] -->
8.2 Sensitivity Analysis of Optimal Water-Sand Mixing Model

<!-- b000314 | prose | pages [18, 19] -->
Based on the introduction of the equation of the relationship between water-sand polymerization degree and water-sand ratio, by limiting the allowable degree of polymerization, we have obtained a reasonable range of water-sand ratio. However, the relationship between the degree of polymerization   , , and the ratio of water to sand is affected by two parameters of   . When the value of   is not accurate, the results of the model could be questionable. Therefore, we continuously adjust the value of  ,   , as shown in FIG 9. Based on this, the robustness of the model is finally judged by calculating the error of the model result.

<!-- b000315 | furniture | pages [18] -->
关注数学模型

<!-- b000316 | furniture | pages [18] -->
2

<!-- b000317 | furniture | pages [18] -->
MATHmodels

<!-- b000318 | furniture | pages [18] -->
获取更多资讯

<!-- b000319 | furniture | pages [19] -->
Team # 2010821

<!-- b000320 | furniture | pages [19] -->
Page 19 of 24

<!-- b000322 | prose | pages [19] -->
FIG 9. Degree of polymerization curve As shown in the figure, based on the original coefficients, we increase and decrease the data by 1%  1.56 , 2.86 and 2% respectively (note that its initial parameter     ), so as to obtain the graph of the degree of aggregation-water-sand ratio in five cases. Based on this, we apply Model 2 again and combine the initial results of Model 2 to calculate the error table of the three shapes as follows:

<!-- b000323 | caption | pages [19] -->
Table 12 Error of the table

<!-- b000324 | prose | pages [19] -->
   ,   Cuboid Cylinder Sector cylinder Error/%   1.58， 2.88 2.3 3.9 3.6   1.59， 2.89 4.9 4.9 5.0   1.54， 2.84 3.1 3.3 2.9   1.53， 2.83 3.8 4.8 4.6

<!-- b000325 | prose | pages [19] -->
 , From the above table, we can observe that when   increases and decreases 1% and 2% respectively, the final error of all shapes is within 5%. Therefore, it shows that our model is more robust  , when   has some errors.

<!-- b000326 | furniture | pages [19] -->
关注数学模型

<!-- b000327 | furniture | pages [19] -->
2

<!-- b000328 | furniture | pages [19] -->
MATHmodels

<!-- b000329 | furniture | pages [19] -->
获取更多资讯

<!-- b000330 | furniture | pages [20] -->
Team # 2010821

<!-- b000331 | furniture | pages [20] -->
Page 20 of 24

<!-- b000332 | heading | pages [20] -->
8.3 Sensitivity Analysis of A Fuzzy Comprehensive Evaluation Model Based on the

<!-- b000333 | prose | pages [20] -->
Ability to Resist Rain Erosion In order to make the fuzzy comprehensive evaluation model valid, we must ensure that the fuzzy comprehensive evaluation index (resistance to rainwater erosion and resistance to wave erosion) is accurate and reliable. In determining the values of the two capabilities, we have introduced three positive definite coefficients to assist the calculation. However, since the values of the three , ,    1 2 3 positive definite coefficients are not very reliable, we continuously adjust the values of the three positive definite coefficients to determine whether the cylinder has always been the optimal shape and thus to judge the stability of the model. The judgment results are as follows:

<!-- b000334 | prose | pages [20] -->
FIG 10. Stability judgment By observing the figure, we clearly know that when increases to 130% and above, the cylinder  1 is no longer the optimal shape, and the optimal shape is the fan-shape cylinder. When is reduced to  2 75% and below, the cylinder is no longer the optimal shape, and the optimal shape is a cuboid. When fluctuates at 30% of its original value, the cylinder is still the optimal shape. Therefore, we can tell 3 that when the three positive definite coefficients fluctuate within 25% of the original value, the results of our model have not changed much and have shown strong robustness.

<!-- b000335 | heading | pages [20] -->
8.4 Sensitivity Analysis of Sandcastle warning protection Model

<!-- b000336 | prose | pages [20] -->
The advantage of the sandcastle humidity prediction model is that it can predict the trend graph of beach humidity in advance and remediate sandcastles in time. If the error between the actual value and the predicted value of the beach humidity does not exceed 10%, we consider that the sandcastle humidity prediction model based on the RBF neural network algorithm is highly reliable.

<!-- b000337 | prose | pages [20, 21] -->
The simulated was performed using MATLAB. First, we choose the mean square error to be 0.02 and the expansion speed of the radial basis function to be 0.8. Then we input the samples to build the RBF neural network and simulate the model. Finally, the average relative error between the predicted value and the actual value of the beach humidity is 4.32%. The comparison chart between the predicate value and the actual value using ORIGIN fitting is shown in FIG 11, which illustrates that the sandcastle humidity prediction model based on the RBF neural network algorithm can predict the humidity basic trend.

<!-- b000338 | furniture | pages [20] -->
关注数学模型

<!-- b000339 | furniture | pages [20] -->
2

<!-- b000340 | furniture | pages [20] -->
MATHmodels

<!-- b000341 | furniture | pages [20] -->
获取更多资讯

<!-- b000342 | furniture | pages [21] -->
Team # 2010821

<!-- b000343 | furniture | pages [21] -->
Page 21 of 24

<!-- b000345 | prose | pages [21] -->
FIG 11. Actual vs. predicted curve

<!-- b000346 | heading | pages [21] -->
9. Evaluation and Promotion of Model

<!-- b000347 | heading | pages [21] -->
9.1 Strength and Weakness

<!-- b000348 | heading | pages [21] -->
9.1.1 Strengths

<!-- b000349 | prose | pages [21] -->
Have fully considered the erosion of sandcastles caused by waves and tidal effects and established a sand-bearing capability indicator. Considering the change in the bottom area and height of the sandcastle foundation during the movement, we create a sandcastle damage index to quantify the sandcastle damage reasonably.

<!-- b000350 | prose | pages [21] -->
Based on some solutions obtained from the sandcastle dynamics simulation, the discrete global  optimization method based on the successive descent has been used to obtain the global optimal solution.

<!-- b000351 | prose | pages [21] -->
The equation of the relationship between water-sand polymerization degree and water-sand ratio is  introduced.The reasonable water-sand ratio range is obtained by limiting the allowable polymerization degree range.

<!-- b000352 | prose | pages [21, 22] -->
On the issue of rain erosion, we put forward the collapse limit coefficient of sandcastle specifically.  Considering the ability of resisting rain infiltration and the evacuation ratio of sandcastle structure comprehensively, we established an evaluation model to determine the stability of the selected shape. Because the RBF neural network overcomes slow convergence and local minimization of the other neural network algorithms, when designing the sandcastle early warming protection mechanism, we have chosen the RBF neural network model to predict when to apply adhesive to enhance the duration of sandcastle When using the RBF neural network algorithm, we have selected input factors based on the changing characteristics of the ambient temperature to accurately and reasonably predict the daily humidity change trend, thereby effectively humidity prediction the sandcastle and extending its duration.

<!-- b000353 | furniture | pages [21] -->
关注数学模型

<!-- b000354 | furniture | pages [21] -->
2

<!-- b000355 | furniture | pages [21] -->
MATHmodels

<!-- b000356 | furniture | pages [21] -->
获取更多资讯

<!-- b000357 | furniture | pages [22] -->
Team # 2010821

<!-- b000358 | furniture | pages [22] -->
Page 22 of 24

<!-- b000360 | heading | pages [22] -->
9.1.2 Weaknesses

<!-- b000361 | prose | pages [22] -->
We did not consider three-dimensional shapes other than cuboids, elliptical cylinders, and sector cylinders, and only selected the three types of shapes most commonly used in sandcastles. We only have considered sandcastles under various water erosion conditions, but not the impact of other factors in nature. The accuracy of some selected coefficients from other literatures may affect some final conclusions. We only have considered the situation when the waves and tides are relatively calm. When the waves and tides significantly fluctuate, the sandcastle might not collapse in the way we have expected.

<!-- b000362 | heading | pages [22] -->
9.2 Promotion

<!-- b000363 | prose | pages [22] -->
Considering the impact of water erosion on sandcastle alone, our model is very robust. Therefore, our model is suitable when the quantitative factors of water erosion fluctuate within a certain range. However, under objective natural conditions, the factors affecting the stability of sandcastles may not be limited to water erosion (such as wind erosion, light, etc.). Therefore, our strategy may need to be slightly modified to cope with the sandcastle foundation under different natural and objective conditions. Further, based on the original model, we tried to establish the basic dynamics equation of the sandcastle considering the combined effects of wind erosion and light, making the solution of the problem more practical. In addition, we believe that the final choice of the cylinder is the most stable of the three proposed shapes, but the problem is that the shape is diverse and there is no guarantee that the cylinder will still be the best of all shapes. Therefore, it is necessary to solve the problem of limited shape being considered.

<!-- b000364 | prose | pages [22] -->
We have two potential solutions to address that only three shapes have been investigated: 1. Perform cluster analysis on multiple shapes to find more sandcastle foundations that are applicable to actual situations. 2. Introduce the proportion of base area and height, have more shapes under consideration and find out the best three-dimensional aspect ratio of each shape.

<!-- b000365 | heading | pages [22] -->
10. Conclusions

<!-- b000366 | prose | pages [22, 23] -->
A detailed strategy to extend the duration of sandcastle foundation was provided in this paper. Firstly, the most stable shape of the sandcastle which was affected by both of the wave and tide was found to be the cylinder. It showed the highest resistance to the wave current erosion among all the considered shapes, according to the optimal shape model based on the dynamics equation of sandcastle foundation. Secondly, the optimum water-sand ratio was worked out to be 0.32 by taking the water- sand polymerization degree into account. Then, the cylinder was confirmed to be the most stable shape by fuzzy comprehensive evaluation, and the rain erosion resistance and resistance to wave current erosion of the sandcastle were also taken into account. Finally, an humidity prediction model of sandcastle was proposed based on RBF neural network, and the daily humidity trend was predicted accurately by the model. When the predicted humidity reached its limit, adhesive should be used in time to keep the bonding effect and stabilize the sandcastle foundation.

<!-- b000367 | furniture | pages [22] -->
关注数学模型

<!-- b000368 | furniture | pages [22] -->
2

<!-- b000369 | furniture | pages [22] -->
MATHmodels

<!-- b000370 | furniture | pages [22] -->
获取更多资讯

<!-- b000371 | furniture | pages [23] -->
Team # 2010821

<!-- b000372 | furniture | pages [23] -->
Page 23 of 24

<!-- b000374 | heading | pages [23] -->
References

<!-- b000375 | references | pages [23] -->
[1] Cui Jie. Research on two-dimensional mathematical model of sediment under the action of wave and

<!-- b000376 | references | pages [23] -->
current [D]. Tianjin University, 2014.

<!-- b000377 | references | pages [23] -->
[2] Yang Yongjian. Several deterministic algorithms for global optimization [D]. Shanghai University,

<!-- b000378 | references | pages [23] -->
2005.

<!-- b000379 | references | pages [23] -->
[3] Lu Yehong. Test and simulation of the damage resistance of building roof structure in rainy season

<!-- b000380 | references | pages [23] -->
[J]. Computer Simulation, 2018, 35 (12): 176-180.

<!-- b000381 | references | pages [23] -->
[4] Yu Gaofeng, Qiu Jinming. Analysis of Teaching Effect Analysis and Optimization of Mathematical

<!-- b000382 | references | pages [23] -->
Modeling Based on Fuzzy Comprehensive Evaluation——Taking Sanming University as an Example

<!-- b000383 | references | pages [23] -->
[J]. Journal of Lanzhou University of Arts and Sciences (Natural Science Edition), 2018, 32 (05): 112-

<!-- b000384 | references | pages [23] -->
115.

<!-- b000385 | references | pages [23] -->
[5] Xu Tongyu, Wang Yan, Zhang Xiaobo, Chen Chunling, Xu Hui, Zhou Yuncheng. Application of

<!-- b000386 | references | pages [23] -->
RBF neural network to the simulation and prediction of humidity in northern sunlight greenhouse [J].

<!-- b000387 | references | pages [23] -->
Journal of Shenyang Agricultural University, 2014, 45 (06): 726-730 .

<!-- b000388 | references | pages [23] -->
[6] Wang Chengwu, Guo Songlin, Wang Wei. Research on short-term power load forecasting by

<!-- b000389 | references | pages [23] -->
improved particle swarm optimization RBF neural network [J] .Electronic Test, 2020 (03): 45-46 + 101.

<!-- b000390 | furniture | pages [23] -->
关注数学模型

<!-- b000391 | furniture | pages [23] -->
2

<!-- b000392 | furniture | pages [23] -->
MATHmodels

<!-- b000393 | furniture | pages [23] -->
获取更多资讯

<!-- b000394 | furniture | pages [24] -->
Team # 2010821

<!-- b000395 | furniture | pages [24] -->
Page 24 of 24

<!-- b000396 | heading | pages [24] -->
Memo

<!-- b000397 | prose | pages [24] -->
TO:Fun in the Sun Topic: Teach you how to build the longest-lasting sandcastle Dear Vacation Magazine Editor： In recent years, the sandcastle related art works have become increasingly popular. After the creation of great sandcastle art works, how to preserve these art works for a long time becomes an obstacle to promoting this type of activities. Our team has developed a complete sandcastle humidity prediction strategy to achieve the purpose of extending the duration of sandcastles. We appreciate this opportunity to introduce you to our strategy.

<!-- b000398 | prose | pages [24] -->
The most stable shape of a sandcastle under the action of sea waves and tides: In general, the most durable sandcastle can be piled with the optimal size ratio. These sandcastle shapes have the longest duration: the cuboid with an aspect ratio of 1.46, the elliptical cylinder with an aspect ratio of 1.00, and the fan-shape cylinder with a radius and arc length ratio of A.

<!-- b000399 | prose | pages [24] -->
The best mixing ratio of water and sand: sandcastles are products of the mixture of sand and water. When the water and sand ratio is 0.739, the sandcastle has the longest duration.

<!-- b000400 | prose | pages [24] -->
The most stable shape choice for rainy days: Rainy days are also a huge threat for sandcastles. It has been proven that the cylinder is the most stable and longest lasting sandcastle shape.

<!-- b000401 | prose | pages [24] -->
Measures to extend the duration of the sandcastle: The sandcastles cannot last long without proper humidity. We have found the lowest humidity on sunny and cloudy days happens at 13: 00-13: 30 in the afternoon. Adhesive is recommended to be used to enhance the sandcastle duration during this time period with low humidity.

<!-- b000402 | prose | pages [24] -->
The above is the optimal sandcastle shape and humidity prediction system that we have proposed. We are eager to help you build the longest lasting sandcastles. If you have any questions about our solution, please feel free to contact us. Our team members are willing to solve any questions you have.

<!-- b000403 | prose | pages [24] -->
Regards，

<!-- b000404 | furniture | pages [24] -->
Team: 2010821

<!-- b000405 | prose | pages [24] -->
March 9 2020

<!-- b000406 | furniture | pages [24] -->
关注数学模型

<!-- b000407 | furniture | pages [24] -->
2

<!-- b000408 | furniture | pages [24] -->
MATHmodels

<!-- b000409 | furniture | pages [24] -->
获取更多资讯

<!-- b000410 | heading | pages [25] -->
Appendix

<!-- b000411 | caption | pages [25] -->
Table 13 Corresponding duration of Cylinder with different aspect ratios

<!-- b000412 | prose | pages [25] -->
Shape factor Duration Shape factor Duration 1.0 4.8 3.5 3 1.5 3.4 4.0 4.6 2.0 2.5 4.5 4.7 2.5 4 5.0 2.0 3.0 4.2 5.5 3.6

<!-- b000413 | caption | pages [25] -->
Table 14 Corresponding duration of sector Cylinder with different aspect ratios

<!-- b000414 | prose | pages [25] -->
Shape factor Duration Shape factor Duration 0.1 0.6 3.5 3.2   0.2 0.7 3.6 2.8  

<!-- b000415 | prose | pages [25] -->
0.8 0.3 3.7 2.9  

<!-- b000416 | prose | pages [25] -->
0.9 0.4 2 3  

<!-- b000417 | prose | pages [25] -->
0.5 1.8 3.5  

<!-- b000418 | furniture | pages [25] -->
关注数学模型

<!-- b000419 | furniture | pages [25] -->
2

<!-- b000420 | furniture | pages [25] -->
MATHmodels

<!-- b000421 | furniture | pages [25] -->
获取更多资讯
