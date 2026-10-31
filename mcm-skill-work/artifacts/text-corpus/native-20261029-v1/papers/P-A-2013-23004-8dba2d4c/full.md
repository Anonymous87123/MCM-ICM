# P-A-2013-23004-8dba2d4c

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
23004

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
T1 ________________

<!-- b000005 | prose | pages [1] -->
T2 ________________

<!-- b000006 | furniture | pages [1] -->


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

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | title | pages [1] -->
A

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | heading | pages [1] -->
2013 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000019 | prose | pages [1] -->
(Attach a copy of this page to your solution paper.)

<!-- b000020 | prose | pages [1] -->
Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | heading | pages [1] -->
Summary

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | prose | pages [1] -->
Through the analysis of the heat distribution along the edges of pans affected by different pan shapes, the article finds the reason for the overcooking of the product at the edges when using a rectangular pans. Furthermore, according to the requirements given by the problem, the authors propose the optimization model for designing the optimal baking pan.

<!-- b000026 | prose | pages [1] -->
The paper propose two models and one algorithm. Model one is established to investigate the heat distribution at the edges of pans in different shapes, while model two and the algorithm are used to design the ultimate pan.

<!-- b000027 | prose | pages [1] -->
Model one describes the heat distribution at the edges of polygons. Based on the equation of heat conduction while taking the convection effects into account, the authors design a model that can describe the thermal conduction inside the pan. Then, given certain Neumann boundary condition, Finite-Element Analysis derives the approximate result of heat distribution, where we can find the phenomena of overcooking at the edges, which matches the practical phenomena described in the problem. Through curve fitting, the authors also find that, for polygons, the standard deviation of temperature of the edges is in inversely proportional to the square of the number of edges.

<!-- b000028 | prose | pages [1] -->
Model two can be used to find the ultimate solution of baking pan. In the analysis of this model, according to the requirements given by the problem, the author proposed two factors: area utilization rate and the degree of uneven of temperature. Then, the paper analyzed the changing speed of the two factors as the number of edges increases, adding correction factors R and weight p in order to construct proper objective function. After modeling, the authors proposed three evaluation methods of the model in response to the three conditions given by the problem. For the first condition, integer programming is adopted to give the proper arrangement of rectangular pans; for the last two conditions, the authors use a new algorithm to give the proper arrangement of circular and regular polygon pans.

<!-- b000029 | prose | pages [1] -->
The new algorithm proposed in this paper is a polygon arrangement model based on Center Dot Matrix Statistics, which is used to test the maximum number of a certain kind of polygon or circles that can be put in a certain area. Then, based on this algorithm, the models are tested with several examples, the shapes and numbers of pan for different W/L and p are calculated.

<!-- b000030 | prose | pages [1] -->
Finally, the sensitivity analysis and model evaluation are performed. During sensitivity analysis, the sudden change phenomenon that emerged when W/L and p change are found. During model evaluation, strengths and weaknesses are analyzed for different models, and suggestion of using rounded corners and normal polygons are proposed for model two.

<!-- b000031 | furniture | pages [1] -->


<!-- b000032 | prose | pages [2] -->
The Design of Ultimate Brownie Pan

<!-- b000033 | furniture | pages [2] -->
Team # 23004

<!-- b000034 | furniture | pages [2] -->


<!-- b000035 | furniture | pages [2] -->


<!-- b000036 | heading | pages [2] -->
Abstract

<!-- b000037 | furniture | pages [2] -->


<!-- b000038 | prose | pages [2] -->
Through the analysis of the heat distribution along the edges of pans affected by different pan shapes, the article finds the reason for the overcooking of the product at the edges when using a rectangular pans. Furthermore, according to the requirements given by the problem, the authors propose the optimization model for designing the optimal baking pan.

<!-- b000039 | prose | pages [2] -->
The paper propose two models and one algorithm. Model one is established to investigate the heat distribution at the edges of pans in different shapes, while model two and the algorithm are used to design the ultimate pan.

<!-- b000040 | prose | pages [2] -->
Model one describes the heat distribution at the edges of polygons. Based on the equation of heat conduction while taking the convection effects into account, the authors design a model that can describe the thermal conduction inside the pan. Then, given certain Neumann boundary condition, Finite-Element Analysis derives the approximate result of heat distribution, where we can find the phenomena of overcooking at the edges, which matches the practical phenomena described in the problem. Through curve fitting, the authors also find that, for polygons, the standard deviation of temperature of the edges is in inversely proportional to the square of the number of edges.

<!-- b000041 | prose | pages [2] -->
Model two can be used to find the ultimate solution of baking pan. In the analysis of this model, according to the requirements given by the problem, the author proposed two factors: area utilization rate and the degree of uneven of temperature. Then, the paper analyzed the changing speed of the two factors as the number of edges increases, adding correction factors R and weight p in order to construct proper objective function. After modeling, the authors proposed three evaluation methods of the model in response to the three conditions given by the problem. For the first condition, integer programming is adopted to give the proper arrangement of rectangular pans; for the last two conditions, the authors use a new algorithm to give the proper arrangement of circular and regular polygon pans.

<!-- b000042 | prose | pages [2] -->
The new algorithm proposed in this paper is a polygon arrangement model based on Center Dot Matrix Statistics, which is used to test the maximum number of a certain kind of polygon or circles that can be put in a certain area. Then, based on this algorithm, the models are tested with several examples, the shapes and numbers of pan for different W/L and p are calculated.

<!-- b000043 | prose | pages [2] -->
Finally, the sensitivity analysis and model evaluation are performed. During sensitivity analysis, the sudden change phenomenon that emerged when W/L and p change are found. During model evaluation, strengths and weaknesses are analyzed for different models, and suggestion of using rounded corners and normal polygons are proposed for model two.

<!-- b000044 | furniture | pages [2] -->


<!-- b000045 | keywords | pages [2] -->
Keywords:  Heat distribution, Finite-Element Analysis, PDE, 2-D Arrangement

<!-- b000046 | furniture | pages [2] -->


<!-- b000047 | furniture | pages [2] -->


<!-- b000048 | furniture | pages [3] -->
Team # 23004                                                                                                                                                                    Page  2  of  20

<!-- b000049 | heading | pages [3] -->
Introduction

<!-- b000050 | prose | pages [3] -->
The authors are intended to model the process of oven baking, analyze the distribution of heat along the edges of pans affected by different pan shapes, in order to find the reason for overcooking of food at the corners when using rectangular pans. Afterwards, the authors construct a model that can optimize the ultimate pan shape and arrangement according to the following conditions.

<!-- b000051 | prose | pages [3] -->
1. Maximize number of pans that can fit in the oven (N). 2. Maximize even distribution of heat (H) for the pan. 3. Optimize a combination of conditions (1) and (2) where weights p and (1- p) are assigned to illustrate how the results vary with different values of W/L and p.

<!-- b000052 | prose | pages [3] -->
In this article, the authors decompose the problem into the following steps when modeling and solving:

<!-- b000053 | prose | pages [3] -->
1. Construct the uneven degree index of pans of different shapes; (also the analysis result of model one) 2. Construct the objective function of the combination optimal problem and uniform the optimization direction of different subgoals; 3. Pick and determine the proper combination of types and numbers of pans; 4. Construct arrangement model, use the model to arrange the results of step 3, and then find the optimal solution.

<!-- b000054 | heading | pages [3] -->
Basic Assumptions

<!-- b000055 | prose | pages [3] -->
1. The temperature in the oven is constant and forced air convection is adopted. 2. The pans are made of isotropic material with good thermal conductivity properties. 3. Basic notations in the article are list as follow.

<!-- b000056 | furniture | pages [3] -->


<!-- b000057 | caption | pages [3] -->
Table 1 Notation

<!-- b000058 | prose | pages [3] -->
Symbol Meaning A, S Area T Temperature t Time ρ Density m Edge number of polygon x, y, z Axis of the rectangular coordinates Q Heat λ Coefficient of thermal conductivity h Coefficient of convection heat transfer c Specific heat capacity L, l Length W, w Width N, n Number q Heat flux Outward normal vector of a plane 𝑛⃑ Utilization rate of Area 𝜂 Standard deviation 𝜎

<!-- b000059 | furniture | pages [3] -->


<!-- b000060 | prose | pages [3] -->
4. The shape of pan is approximately rectangular box with no lid. The shapes and the basic model are given as follow:

<!-- b000061 | furniture | pages [3] -->


<!-- b000062 | furniture | pages [4] -->
Team # 23004                                                                                                                                                                    Page  3  of  20

<!-- b000063 | furniture | pages [4] -->


<!-- b000064 | caption | pages [4] -->
Fig. 1 Basic Model of Baking Pan

<!-- b000065 | furniture | pages [4] -->


<!-- b000066 | heading | pages [4] -->
Model 1:    The Distribution of Heat at the Edges of Polygon

<!-- b000067 | prose | pages [4] -->
According to heat-transfer principles, there are three ways for heat to transfer: heat radiation, heat conductivity and heat convection.

<!-- b000068 | prose | pages [4] -->
In a baking oven, the hot air flows over the baking material either by natural convection or forced by a fan, the convection heat transfer from the air, the radiation heat transfer from the oven heating surfaces, and the conduction heat transfer across contact area between product and metal surface. [1]

<!-- b000069 | prose | pages [4] -->
In most heat-controllable ovens, as the temperature inside the oven can be kept constant, the main source of heat that will result in the overcooking of food is the metal pan. So this model mainly focuses on the heat conductivity inside the metal pans.

<!-- b000070 | prose | pages [4] -->
The basic model of heat flow launched into the metal pan is as follow.

<!-- b000071 | furniture | pages [4] -->


<!-- b000072 | furniture | pages [4] -->


<!-- b000073 | caption | pages [4] -->
Fig. 2 Heat Flow of the Pan

<!-- b000074 | furniture | pages [4] -->


<!-- b000075 | prose | pages [4] -->
As we assume that the pan is isotropic, the heat flux received by different facets of the pan should be the same inside the oven. As a result, the non-uniformity is resulted from the heat convection between the pan and air and the heat transfer inside the metal material. According to the heat-transfer equation (Eq. 1), [2, 3]

<!-- b000076 | prose | pages [4] -->
𝜕2𝑇

<!-- b000077 | prose | pages [4] -->
𝜕2𝑇

<!-- b000078 | prose | pages [4] -->
𝜕2𝑇

<!-- b000079 | prose | pages [4] -->
𝜕𝑇

<!-- b000080 | prose | pages [4] -->
𝜕𝑧2) = 𝑄𝑔,                                                                                  (Eq. 1)

<!-- b000081 | prose | pages [4] -->
𝜌𝑐

<!-- b000082 | prose | pages [4] -->
𝜕𝑡−𝜆(

<!-- b000083 | prose | pages [4] -->
𝜕𝑥2 +

<!-- b000084 | prose | pages [4] -->
𝜕𝑦2 +

<!-- b000085 | prose | pages [4] -->
Where T represents temperature, 𝑄𝑔 represents inner heat source, 𝜌 represents density, 𝑐 represents specific heat capacity，𝜆 represents thermal conductivity, when balance is achieved, the temperature stops to change. So

<!-- b000086 | prose | pages [4] -->
𝜕𝑇

<!-- b000087 | prose | pages [4] -->
𝜕𝑡= 0, (𝑡→∞).                                                                                                                               (Eq. 2)

<!-- b000088 | prose | pages [4] -->
From Eq. 2, we can derive the equation of steady state heat transfer without inner heat source, concerning the coefficient of convection heat transfer, which is the steady state heat transfer equation (Eq. 3) of baking pan.

<!-- b000089 | furniture | pages [5] -->
Team # 23004                                                                                                                                                                    Page  4  of  20

<!-- b000090 | prose | pages [5] -->
𝜕2𝑇

<!-- b000091 | prose | pages [5] -->
𝜕2𝑇

<!-- b000092 | prose | pages [5] -->
𝜕2𝑇

<!-- b000093 | prose | pages [5] -->
𝜕𝑧2) = ℎ(𝑇𝑒𝑥𝑡−𝑇)                                                                                           (Eq. 3)

<!-- b000094 | prose | pages [5] -->
−𝜆(

<!-- b000095 | prose | pages [5] -->
𝜕𝑥2 +

<!-- b000096 | prose | pages [5] -->
𝜕𝑦2 +

<!-- b000097 | prose | pages [5] -->
In Eq. 3, the ℎ represents the coefficient of heat convection. The 𝑇𝑒𝑥𝑡 represents outer temperature of the air. The boundary condition is Neumann boundary condition, which is used when all facets’ heat flux density of normal vector 𝑞𝑒𝑑𝑔𝑒 are known. The 𝑛⃑  represents the outward normal vector of a plane.

<!-- b000098 | prose | pages [5] -->
𝜕𝑇

<!-- b000099 | prose | pages [5] -->
𝜕𝑛⃑ = 𝑞(𝑥, 𝑦, 𝑧, 𝑡)                                                                                                         (Eq. 4)

<!-- b000100 | prose | pages [5] -->
𝑞𝑒𝑑𝑔𝑒= −𝜆

<!-- b000101 | prose | pages [5] -->
Eq. 4 is a third-order partial differential equation (PDE). However, if we assume that only the heat from the bottom of the pan is considered, the distribution of heat on the surface of the pan will be even. Thus, the unevenness of heat distribution is mainly resulted from the heat received by side facets. As a result, the three-dimensional model can be simplified into a two-dimensional model as follow.

<!-- b000102 | prose | pages [5] -->
𝜕2𝑇

<!-- b000103 | prose | pages [5] -->
𝜕2𝑇

<!-- b000104 | prose | pages [5] -->
𝜕𝑦2) = ℎ(𝑇𝑒𝑥𝑡−𝑇)

<!-- b000105 | prose | pages [5] -->
−𝜆(

<!-- b000106 | prose | pages [5] -->
𝜕𝑥2 +

<!-- b000107 | prose | pages [5] -->
{

<!-- b000108 | prose | pages [5] -->
.                                                                                                  (Eq. 5)

<!-- b000109 | prose | pages [5] -->
𝜕𝑇

<!-- b000110 | prose | pages [5] -->
𝑞𝑒𝑑𝑔𝑒= −𝜆

<!-- b000111 | prose | pages [5] -->
𝜕𝑛⃑ = 𝑞0

<!-- b000112 | prose | pages [5] -->
The steady state solution can be calculated using finite element analysis method. Using the PDE Toolbox provided by Matlab, we can get the numerical solution of this model. [4]

<!-- b000113 | prose | pages [5] -->
Now, the heat distribution on a square pan made of certain kind of experimental material are calculated using the following parameters and boundary condition. These parameters and boundary conditions are regarded as the standard state of tests in this paper.

<!-- b000114 | caption | pages [5] -->
Table 2 Parameters of Standard State

<!-- b000115 | prose | pages [5] -->
Physical Quantity Value 50 [ W / ( K · m ) ] 𝜆 100 [ W / ( K · m2 ) ] ℎ 330 [ K ] 𝑇𝑒𝑥𝑡 1000 [ W / ( s · m ) ] 𝑞0

<!-- b000116 | prose | pages [5] -->
The calculation results are presented as follow.

<!-- b000117 | furniture | pages [5] -->


<!-- b000118 | caption | pages [5] -->
Fig. 3 3D - Plot of Heat Distribution of Square Baking Pan Model

<!-- b000119 | furniture | pages [6] -->
Team # 23004                                                                                                                                                                    Page  5  of  20

<!-- b000120 | furniture | pages [6] -->


<!-- b000121 | caption | pages [6] -->
Fig. 4 Temperature Curve of the Edge of the Square Pan

<!-- b000122 | furniture | pages [6] -->


<!-- b000123 | prose | pages [6] -->
We can see that the temperatures at the corners are high while the temperature at the center is the lowest. The change of temperature along the edge is significant. If circular pan is chosen, the heat distribution at the edge will be even, while the temperature at the center is also relatively low.

<!-- b000124 | furniture | pages [6] -->


<!-- b000125 | caption | pages [6] -->
Fig. 5 3D - Plot of Heat Distribution of Circle Baking Pan Model

<!-- b000126 | furniture | pages [6] -->


<!-- b000127 | prose | pages [6] -->
Then, the area of pan are kept constant, while the number of edges is increased, which will make the pan approach circle in shape. We can see the following pattern of change where we can find that the heat distribution at the edges is approximately parabolic. Also, as the number of edges increases, the heat distribution will tend to be even, the variance of temperature will decrease.

<!-- b000128 | furniture | pages [7] -->
Team # 23004                                                                                                                                                                    Page  6  of  20

<!-- b000129 | furniture | pages [7] -->


<!-- b000130 | caption | pages [7] -->
Fig. 6 Temperature Curves of Edge of the Different Polygon Pan

<!-- b000131 | furniture | pages [7] -->


<!-- b000132 | prose | pages [7] -->
Meanwhile, standard deviations as listed below are calculated to represent the uniformity.

<!-- b000133 | prose | pages [7] -->
We can see that as the number of lateral increases, the trend of overall standard deviation and standard deviations at the edges are of the same direction, which is decreasing. Also, we can see that as the number of edges increases, the overall standard deviation approaches a certain value, while the standard deviation at the edges approached zero. Thus, the shape determines the heat distribution at the edges, and also affects the overall heat distribution. The more edges it has, the more even the heat is distributed.

<!-- b000134 | prose | pages [7] -->
As a result, we can use the standard deviation of temperature at the edges to denote the overall degree of even distribution of heat.

<!-- b000135 | furniture | pages [7] -->


<!-- b000136 | caption | pages [7] -->
Table 3 the Deviation of Temperature of Different polygons

<!-- b000137 | prose | pages [7] -->
Deviation at the

<!-- b000138 | prose | pages [7] -->
Number of

<!-- b000139 | prose | pages [7] -->
Overall standard

<!-- b000140 | prose | pages [7] -->
Standard deviation at

<!-- b000141 | prose | pages [7] -->
Per-unit

<!-- b000142 | prose | pages [7] -->
2 ）

<!-- b000143 | prose | pages [7] -->
value

<!-- b000144 | prose | pages [7] -->
edges（𝜎𝑚

<!-- b000145 | prose | pages [7] -->
edges（m）

<!-- b000146 | prose | pages [7] -->
deviation（𝜎𝑤）

<!-- b000147 | prose | pages [7] -->
4 4.3236 5 3.2438 6 2.8923 7 2.7342 8 2.6159 10 2.5089 14 2.4155 16 2.3754 1.0041 ∞（Circle）

<!-- b000148 | prose | pages [7] -->
the edges（𝜎𝑚）

<!-- b000149 | prose | pages [7] -->
2.2918 1.5139 1 0.6959 0.8342 0.5510 0.3416 0.5845 0.3861 0.1716 0.4142 0.2736 0.0961 0.3100 0.2048 0.0535 0.2313 0.1528 0.0090 0.0949 0.0627 0.0057 0.0755 0.0499 0 0.0000 0.0000

<!-- b000150 | furniture | pages [8] -->
Team # 23004                                                                                                                                                                    Page  7  of  20

<!-- b000151 | furniture | pages [8] -->


<!-- b000152 | caption | pages [8] -->
Fig. 7 Curve Fitting Result

<!-- b000153 | prose | pages [8] -->
Using Matlab to do the curve fitting, we can get the approximate relationship between the number of edges and the even distribution degree of heat represented by standard deviation at the edges.

<!-- b000154 | prose | pages [8] -->
23.605

<!-- b000155 | prose | pages [8] -->
23.605

<!-- b000156 | prose | pages [8] -->
1

<!-- b000157 | prose | pages [8] -->
𝑚2.                                                                                      (Eq. 6)

<!-- b000158 | prose | pages [8] -->
𝜎=

<!-- b000159 | prose | pages [8] -->
+ 0.035 ≈

<!-- b000160 | prose | pages [8] -->
∝

<!-- b000161 | prose | pages [8] -->
𝑚2

<!-- b000162 | prose | pages [8] -->
𝑚2

<!-- b000163 | prose | pages [8] -->
This model properly explains the reason for the problem of uneven heating at the edges of pans. Meanwhile, we can see how the heat distribution changes as the shape of pan changes from polygon to circle.

<!-- b000164 | heading | pages [8] -->
Model 2:    Baking Pan Optimization Design Model

<!-- b000165 | prose | pages [8] -->
Determination of the objective function

<!-- b000166 | prose | pages [8] -->
We have already known from the problem and the results of model one that the uniformity of heat distribution changes as the shape of pan changes. In order to design and optimize pan shape, we need to consider two factors of pan’s characteristics.

<!-- b000167 | prose | pages [8] -->
Factor One: The Area Utilization Rate of Rack η

<!-- b000168 | prose | pages [8] -->
This is defined as follow,

<!-- b000169 | prose | pages [8] -->
𝑁𝐴

<!-- b000170 | prose | pages [8] -->
2𝑆  .                                                                                                                       (Eq. 7)

<!-- b000171 | prose | pages [8] -->
𝜂= 1 −

<!-- b000172 | prose | pages [8] -->
In Eq. 7, A is the area of a single pan. N is the total number of all pans. S is the area of a rack. The smaller η is, the higher the utilization rate of area is achieved.

<!-- b000173 | prose | pages [8] -->
According to the 2-D arrangement principle, only rectangle and hexagon can be used to cover an infinite plane area without overlap and leaving intervals, while other shapes cannot be used to do the job.

<!-- b000174 | furniture | pages [9] -->
Team # 23004                                                                                                                                                                    Page  8  of  20

<!-- b000175 | furniture | pages [9] -->


<!-- b000176 | caption | pages [9] -->
Fig. 8 Several 2-D Arrangement Methods

<!-- b000177 | prose | pages [9] -->
As a result, the only way to achieve maximum rack area utilization rate is to use pans of rectangle or hexagon shapes. When it comes to finite plain area, because of the constraint of boundary, the arrangement job may become more complex. We will address the problem later in this paper.

<!-- b000178 | prose | pages [9] -->
Factor Two: the Temperature Discrepancy Rate σ

<!-- b000179 | prose | pages [9] -->
In model one, we discussed the feasibility of using the standard deviation of temperature at the edges to indicate the degree of even distribution rate.

<!-- b000180 | prose | pages [9] -->
We define the temperature discrepancy rate as follow:

<!-- b000181 | prose | pages [9] -->
∑𝑛𝑖𝜎𝑖

<!-- b000182 | prose | pages [9] -->
𝜎0𝑁,                                                                                                                             (Eq. 8)

<!-- b000183 | prose | pages [9] -->
𝜎=

<!-- b000184 | prose | pages [9] -->
Where 𝜎𝑖 is the standard deviation of temperature at the edges of pans with shape No. i, 𝑛𝑖 is the number of pan with shape No. i. In order to facilitate optimization, we convert the standard deviation to per-unit value, using the largest standard deviation 𝜎0 (which is the standard deviation for rectangular pan) as the base value. A smaller 𝜎 indicate smaller temperature discrepancy between parts of the pan and more even distribution of heat.

<!-- b000185 | prose | pages [9] -->
The conclusion of model one tells that the degree of even distribution of heat at the edges of regular polygon is inversely proportional to the square of its number of edges. So the heat distribution of circle is most even while the rectangles’ are the worst.

<!-- b000186 | prose | pages [9] -->
According to the different demands of user, we use p as the weight of factor one, (1-p) as the weight of factor two. The optimization directions of the two indicators are the same. So the indicator of demand and the optimization direction are as follow:

<!-- b000187 | prose | pages [9] -->
𝑚𝑖𝑛   [𝑅× 𝜂𝑝+ 𝜎(1 −𝑝)],                                                                                                 (Eq. 9)

<!-- b000188 | prose | pages [9] -->
Where R is the correction factor, which is used to correct the changing speeds of the two factors. This factor will help reduce the imbalance during optimization. When the shape changes, R can make the changing speeds of them tend to be the same. The setting of R will be discussed later in the paper.

<!-- b000189 | prose | pages [9] -->
Then, general constraints are listed as follow,

<!-- b000190 | prose | pages [9] -->
2𝑆−𝑁𝐴≥0 ∑𝑛𝑖= 𝑁,  𝑛𝑖∈𝑍+    .                                                                                        (Eq. 10) 𝑆. 𝑇.     {

<!-- b000191 | prose | pages [9] -->
Now, we will do the optimization according to the following three kind of requirements of users. (3 condition)

<!-- b000192 | furniture | pages [10] -->
Team # 23004                                                                                                                                                                    Page  9  of  20

<!-- b000193 | prose | pages [10] -->
1. Maximize number of pans that can fit in the oven (N). 2. Maximize even distribution of heat (H) for the pan. 3. Optimize a combination of conditions (1) and (2) where weights p and (1- p) are assigned to illustrate how the results vary with different values of W/L and p.

<!-- b000194 | prose | pages [10] -->
Condition 1:   To Achieve Maximum Number of Pans. (p=1)

<!-- b000195 | prose | pages [10] -->
𝑁𝐴

<!-- b000196 | prose | pages [10] -->
𝑆) ⇒ 𝑚𝑎𝑥 𝑁 .                                                                             (Eq. 11)

<!-- b000197 | prose | pages [10] -->
𝑚𝑖𝑛  𝜂= 𝑚𝑖𝑛 (1 −

<!-- b000198 | prose | pages [10] -->
In order to achieve maximum number of pans, close packed structure must be used. Meanwhile, because of the constraint of the shape of rack, only rectangular pans can leave the least space at the edges of rack. So the number of pans will be: ([x] represents the largest integer which is less than x)

<!-- b000199 | prose | pages [10] -->
𝑆

<!-- b000200 | prose | pages [10] -->
𝐴] .                                                                                                                   (Eq. 12)

<!-- b000201 | prose | pages [10] -->
𝑁𝑚𝑎𝑥= 2 [

<!-- b000202 | prose | pages [10] -->
Now, we need to model the close package of rectangles to get the final arranging pattern.

<!-- b000203 | furniture | pages [10] -->


<!-- b000204 | caption | pages [10] -->
Fig. 9  Geometric Sketch

<!-- b000205 | furniture | pages [10] -->


<!-- b000206 | prose | pages [10] -->
Geometric constraints (the width and length ration W/L is not constant):

<!-- b000207 | prose | pages [10] -->
𝐴= 𝑤𝑙, 𝑆= 𝑊𝐿,

<!-- b000208 | prose | pages [10] -->
𝑁𝑚𝑎𝑥

<!-- b000209 | prose | pages [10] -->
≥𝑛𝑤𝑛𝑙,

<!-- b000210 | prose | pages [10] -->
(Eq. 13)

<!-- b000211 | prose | pages [10] -->
𝑆. 𝑇.     {

<!-- b000212 | prose | pages [10] -->
2

<!-- b000213 | prose | pages [10] -->
𝑊

<!-- b000214 | prose | pages [10] -->
𝐿

<!-- b000215 | prose | pages [10] -->
1 ≤𝑛𝑤≤[

<!-- b000216 | prose | pages [10] -->
𝑤] , 1 ≤𝑛𝑙≤[

<!-- b000217 | prose | pages [10] -->
𝑙] .

<!-- b000218 | prose | pages [10] -->
This model may not be able to give a clos package. So, we will firstly make the pans closely attached to the certain three edges, and then splice the left space into (𝑁𝑚𝑎𝑥−𝑛𝑤𝑛𝑙) rectangles with different areas.

<!-- b000219 | furniture | pages [10] -->


<!-- b000220 | caption | pages [10] -->
Fig. 10  An Arrangement of Rectangles

<!-- b000221 | furniture | pages [11] -->
Team # 23004                                                                                                                                                                    Page  10  of  20

<!-- b000222 | prose | pages [11] -->
We can see from the above result that only if the area of rack S is the integral multiple of area of a single pan A, it is possible to achieve close package with rectangles, which means that any other condition will not achieve close package.

<!-- b000223 | prose | pages [11] -->
Condition 2:   The Most Even Distribution of Heat. (p=0)

<!-- b000224 | prose | pages [11] -->
∑𝑛𝑖𝜎𝑖

<!-- b000225 | prose | pages [11] -->
𝜎0𝑁 .                                                                                                       (Eq. 14)

<!-- b000226 | prose | pages [11] -->
𝑚𝑖𝑛  𝜎= 𝑚𝑖𝑛

<!-- b000227 | prose | pages [11] -->
It requires that the heat distribution should be as even as possible while ignoring the utilization rate. So we will totally use circular pans. That is:

<!-- b000228 | prose | pages [11] -->
𝑆

<!-- b000229 | prose | pages [11] -->
𝐴].                                                                                                           (Eq. 15)

<!-- b000230 | prose | pages [11] -->
𝑁≤𝑁𝑚𝑎𝑥= 2 [

<!-- b000231 | prose | pages [11] -->
The number of pans will be less than the maximum possible number. Now we need to establish a model for arranging circles to get the final arranging pattern. There are two possible patterns:

<!-- b000232 | furniture | pages [11] -->


<!-- b000233 | caption | pages [11] -->
Fig. 11 Pattern 1 of Circle Arrangement

<!-- b000234 | furniture | pages [11] -->


<!-- b000235 | furniture | pages [11] -->


<!-- b000236 | caption | pages [11] -->
Fig. 12 Pattern 2 of Circle Arrangement

<!-- b000237 | furniture | pages [11] -->


<!-- b000238 | prose | pages [11] -->
The distance between the centers of basic units for close package is equal to the diameter of circle. The basic units of the dot matrix of centers are triangles and squares respectively. So optimization should be done for each pattern. Considering that the arrangement of circles is like the arrangement of regular polygons, we propose an algorithm based on center matrix statics, which will be illustrated later in this paper.

<!-- b000239 | prose | pages [11] -->
Condition 3:    0<p<1

<!-- b000240 | prose | pages [11] -->
𝑚𝑖𝑛   [𝑅× 𝜂𝑝+ 𝜎(1 −𝑝)] .                                                                                             (Eq. 16)

<!-- b000241 | prose | pages [11] -->
For some users, both the even distribution of heat, which will reduce the possible overcooking at edges, and the high utilization rate of pan area are supposed to achieve, or that a slight overcooking cake is desired for better taste. So we wish that weight p and (1-p) will be used to reflect the users’ specific requirement.

<!-- b000242 | prose | pages [11] -->
The first step is to determine the correction factor R to correct the objective function. In model one, we have analyzed how 𝜎 changes with the shape of pans. Then, we need to do further analysis on the rules that the unused area changes as the shape of pans changes.

<!-- b000243 | prose | pages [11] -->
In order to reduce the unused area at the rack, we need to arrange the pans as closely as possible. Now, the arrangement of different kinds of polygons are listed as follow.

<!-- b000244 | furniture | pages [12] -->
Team # 23004                                                                                                                                                                    Page  11  of  20

<!-- b000245 | prose | pages [12] -->
1. Rectangle

<!-- b000246 | prose | pages [12] -->
Unused space only appears at the edges.

<!-- b000247 | prose | pages [12] -->
2. Regular octagon

<!-- b000248 | prose | pages [12] -->
There will be two kinds of unused space: at the edges and the holes in-between.

<!-- b000249 | prose | pages [12] -->
3. Regular hexagon

<!-- b000250 | prose | pages [12] -->
Unused space only appears at the edges.

<!-- b000251 | furniture | pages [12] -->


<!-- b000252 | furniture | pages [12] -->


<!-- b000253 | caption | pages [12] -->
Fig. 13 Different Arrangements

<!-- b000254 | prose | pages [12] -->
4. Regular m-gon (m>=12)

<!-- b000255 | prose | pages [12] -->
The shape will be like circle. In an attempt to reduce cost, we will use circles instead of such polygons.

<!-- b000256 | furniture | pages [12] -->


<!-- b000257 | caption | pages [12] -->
Fig. 14 Regular Dodecagon and Circle

<!-- b000258 | prose | pages [12] -->
5. Other polygons

<!-- b000259 | prose | pages [12] -->
It will be impossible to achieve overlap of edges because the inner angles are not 60 or 90 degree. There will be much more unused space, so such arrangements will not be considered.

<!-- b000260 | furniture | pages [12] -->


<!-- b000261 | furniture | pages [12] -->


<!-- b000262 | caption | pages [12] -->
Fig. 15 the Arrangement of Heptagon, etc.

<!-- b000263 | furniture | pages [12] -->


<!-- b000264 | furniture | pages [12] -->


<!-- b000265 | prose | pages [12] -->
Now we only need to analyze the arrangement of rectangles (including squares), regular hexagons, regular octagons and circles.

<!-- b000266 | furniture | pages [13] -->
Team # 23004                                                                                                                                                                    Page  12  of  20

<!-- b000267 | prose | pages [13] -->
For any regular polygon with an edge number of 4l (l>1), when we arrange them as the edges overlap with adjacent polygons, the area they encompass will be regular polygon with an edge number of 4(l-1), the relationship between area and number of edges is:

<!-- b000268 | prose | pages [13] -->
𝑐𝑜𝑡 𝜋

<!-- b000269 | prose | pages [13] -->
−1).                                                                                                           (Eq. 17) 4𝑙

<!-- b000270 | prose | pages [13] -->
𝑆𝑙= 𝐴(

<!-- b000271 | prose | pages [13] -->
𝑙

<!-- b000272 | prose | pages [13] -->
The changing speed of the value of this function will be approximately the same with the changing speed of σ in the above conditions (rectangles, regular hexagons, regular octagons and circles), but with opposite direction. So the correction factor will have a constant value, which means:

<!-- b000273 | prose | pages [13] -->
𝑅= 𝑐𝑜𝑛𝑠𝑡.                                                                                                                       (Eq. 18)

<!-- b000274 | prose | pages [13] -->
Finally, when 0<p<1, the arrangement model will be further divided into the following conditions to facilitate further discussion, that is, rectangle, regular hexagon, regular octagon, circle and the combination of them.

<!-- b000275 | prose | pages [13] -->
Now, we use the following model:

<!-- b000276 | prose | pages [13] -->
𝑚𝑖𝑛   [𝑅× 𝜂𝑝+ 𝜎(1 −𝑝)].                                                                                              (Eq. 19)

<!-- b000277 | prose | pages [13] -->
2𝑆−𝑁𝐴≥0 𝑛4 + 𝑛6 + 𝑛8 + 𝑛∞= 𝑁,  𝑛𝑖∈𝑍+

<!-- b000278 | prose | pages [13] -->
.                                                                     (Eq. 20)

<!-- b000279 | prose | pages [13] -->
𝑆. 𝑇.     {

<!-- b000280 | prose | pages [13] -->
𝜎𝑖∈{  𝜎4,  𝜎6,  𝜎8,  𝜎∞}

<!-- b000281 | prose | pages [13] -->
The solution of the model will be a vector n, where all the terms are integer. Considering the constraints of the actual area of two racks and the maximum number of pans, we only allow the combination of a maximum number of two shapes of pans appears simultaneously on a rack. Then we will use the algorithm illustrated as follow to calculate the arrangement and compare the result of objective function, and then find the optimal solution.

<!-- b000282 | furniture | pages [13] -->


<!-- b000283 | heading | pages [13] -->
Algorithm:    Regular Polygon Arrangement Based on Center Matrix Statics

<!-- b000284 | furniture | pages [13] -->


<!-- b000285 | caption | pages [13] -->
Fig. 16  Edges and Center Matrix of Octagon

<!-- b000286 | prose | pages [13] -->
Every kind of polygon has several unique close package arranging patterns. As a result, we can draw the matrix of centers on graph paper. Make the axis overlap with edges of polygons as much as possible. Thus, we only need to determine whether the polygon with a certain center can be put inside the rectangle or the boundaries. Take rectangle rack boundaries as the example.

<!-- b000287 | furniture | pages [14] -->
Team # 23004                                                                                                                                                                    Page  13  of  20

<!-- b000288 | prose | pages [14] -->
For any point that lays inside the rectangle, it must comply the following conditions:

<!-- b000289 | prose | pages [14] -->
1. The least distance between this point and the edges of the rectangle must not be less than the radius of its inscribed circle; 2. For hexagon, the least distance between this point and the edges of the rectangle must not be less than the radius of its circumcircle;

<!-- b000290 | prose | pages [14] -->
For regular hexagon, because of that the distance between dots along x axis and along y axis are different, we need to rotate the rack 90 degree when one analysis is finished and do the analysis again, and then pick the optimal arrangement.

<!-- b000291 | furniture | pages [14] -->


<!-- b000292 | furniture | pages [14] -->


<!-- b000293 | caption | pages [14] -->
Fig. 17 Special Condition of Hexagon

<!-- b000294 | furniture | pages [14] -->


<!-- b000295 | prose | pages [14] -->
The flow chart of Algorithm is listed as follow. In tests with actual examples, we will use the method described above to give the optimal pan design when different p and W/L are given.

<!-- b000296 | prose | pages [14] -->
Start

<!-- b000297 | prose | pages [14] -->
Input Boundary equations and the shapes of polygon

<!-- b000298 | prose | pages [14] -->
No

<!-- b000299 | prose | pages [14] -->
Build the center dot matrix of an

<!-- b000300 | prose | pages [14] -->
arrangement

<!-- b000301 | prose | pages [14] -->
Select a dot dot within ranges ?

<!-- b000302 | prose | pages [14] -->
Output N as

<!-- b000303 | prose | pages [14] -->
No

<!-- b000304 | prose | pages [14] -->
Yes

<!-- b000305 | heading | pages [14] -->
the result

<!-- b000306 | prose | pages [14] -->
End

<!-- b000307 | prose | pages [14] -->
The dot within

<!-- b000308 | prose | pages [14] -->
boundaries ?

<!-- b000309 | prose | pages [14] -->
Yes

<!-- b000310 | prose | pages [14] -->
1.The least distance

<!-- b000311 | prose | pages [14] -->
Calculate the distance

<!-- b000312 | prose | pages [14] -->
Initialize the Number of polygon in this arrangement

<!-- b000313 | prose | pages [14] -->
N = 0

<!-- b000314 | prose | pages [14] -->
No

<!-- b000315 | heading | pages [14] -->
Algorithm Flowchart

<!-- b000316 | prose | pages [14] -->
for 2-D Arrangement Based on Center Dot

<!-- b000317 | prose | pages [14] -->
Matrix

<!-- b000318 | prose | pages [14] -->
between this point and

<!-- b000319 | prose | pages [14] -->
between the dot and

<!-- b000320 | prose | pages [14] -->
the edges of the rectangle

<!-- b000321 | prose | pages [14] -->
all the boundaries

<!-- b000322 | prose | pages [14] -->
must not be less than the radius of its inscribed circle; 2.For hexagon, the least

<!-- b000323 | prose | pages [14] -->
Dot meets the

<!-- b000324 | prose | pages [14] -->
arranging

<!-- b000325 | prose | pages [14] -->
distance between this

<!-- b000326 | prose | pages [14] -->
conditions ?

<!-- b000327 | prose | pages [14] -->
point and the edges of

<!-- b000328 | prose | pages [14] -->
Yes

<!-- b000329 | prose | pages [14] -->
the rectangle must not be less than the radius of its

<!-- b000330 | prose | pages [14] -->
N=N+1

<!-- b000331 | prose | pages [14] -->
circumcircle;

<!-- b000332 | furniture | pages [14] -->


<!-- b000333 | caption | pages [14] -->
Fig. 18 Algorithm Flowchart for 2-D Arrangement Based on Center Dot Matrix

<!-- b000334 | furniture | pages [15] -->
Team # 23004                                                                                                                                                                    Page  14  of  20

<!-- b000335 | heading | pages [15] -->
Model test

<!-- b000336 | prose | pages [15] -->
We picked Countertop Oven with Convection and Rotisserie (31100) with two 9”x13” racks (The pictures are picked from http://www.hamiltonbeach.com/products/toaster-ovens-countertop- oven-with-convection-and-rotisserie-3110).

<!-- b000337 | furniture | pages [15] -->


<!-- b000338 | caption | pages [15] -->
Fig. 19 Testing Oven and Baking Pan

<!-- b000339 | furniture | pages [15] -->


<!-- b000340 | prose | pages [15] -->
We suppose that the oven is used to bake many brownie cakes with area of 30 cm2. The environment inside the oven and of the pan is standard. We pick the correction factor R as 1, and then the objective function will be:

<!-- b000341 | prose | pages [15] -->
𝑚𝑖𝑛   [𝜂𝑝+ 𝜎(1 −𝑝)]

<!-- b000342 | prose | pages [15] -->
∑𝑛𝑖𝜎𝑖

<!-- b000343 | prose | pages [15] -->
𝑁𝐴

<!-- b000344 | prose | pages [15] -->
𝜎0𝑁].                                                                            (Eq. 21)

<!-- b000345 | prose | pages [15] -->
2𝑆) + (1 −𝑝)

<!-- b000346 | prose | pages [15] -->
= 𝑚𝑖𝑛  [𝑝(1 −

<!-- b000347 | prose | pages [15] -->
2𝑆−𝑁𝐴≥0

<!-- b000348 | prose | pages [15] -->
.                                                                   (Eq. 22)

<!-- b000349 | prose | pages [15] -->
𝑛4 + 𝑛6 + 𝑛8 + 𝑛∞= 𝑁,  𝑛𝑖∈𝑍+

<!-- b000350 | prose | pages [15] -->
𝑆. 𝑇.     {

<!-- b000351 | prose | pages [15] -->
𝜎𝑖∈{  𝜎4,  𝜎6,  𝜎8,  𝜎∞}

<!-- b000352 | prose | pages [15] -->
Arranging patterns are as follow:

<!-- b000353 | caption | pages [15] -->
Table 4 All the Arrangements for Optimization (1)

<!-- b000354 | prose | pages [15] -->
Arranging pattern 1 Shape

<!-- b000355 | prose | pages [15] -->
Rectangle

<!-- b000356 | prose | pages [15] -->
Arranging pattern 2

<!-- b000357 | furniture | pages [15] -->


<!-- b000358 | furniture | pages [15] -->


<!-- b000359 | prose | pages [15] -->
Square

<!-- b000360 | prose | pages [15] -->
See Condition 1

<!-- b000361 | prose | pages [15] -->
Regular hexagon

<!-- b000362 | prose | pages [15] -->
Regular octagon

<!-- b000363 | furniture | pages [15] -->


<!-- b000364 | furniture | pages [15] -->


<!-- b000365 | furniture | pages [15] -->


<!-- b000366 | furniture | pages [16] -->
Team # 23004                                                                                                                                                                    Page  15  of  20

<!-- b000367 | furniture | pages [16] -->


<!-- b000368 | caption | pages [16] -->
Table 5 All the Arrangements for Optimization (2)

<!-- b000369 | prose | pages [16] -->
Shape Arranging pattern 1 Arranging pattern 2

<!-- b000370 | prose | pages [16] -->
Circle

<!-- b000371 | furniture | pages [16] -->


<!-- b000372 | furniture | pages [16] -->


<!-- b000373 | prose | pages [16] -->
Basic parameters:

<!-- b000374 | prose | pages [16] -->
𝑆= 9’’ × 13’’ = 22.86 𝑐𝑚 × 33.02 𝑐𝑚= 754.8372 𝑐𝑚2 ,                                          (Eq. 23)

<!-- b000375 | prose | pages [16] -->
𝐴= 30 𝑐𝑚2 ,                                                                                                                    (Eq. 24)

<!-- b000376 | prose | pages [16] -->
𝑆

<!-- b000377 | prose | pages [16] -->
𝐴] = 50.                                                                                        (Eq. 25)

<!-- b000378 | prose | pages [16] -->
𝑁≤𝑁𝑚𝑎𝑥= 2 [

<!-- b000379 | prose | pages [16] -->
Test 1:   p = 0.5, W/L = 9/13 = 0.6923.

<!-- b000380 | prose | pages [16] -->
(For polygon, m is the number of edges, a is the length of edges.)

<!-- b000381 | prose | pages [16] -->
𝑁= 40，𝑚= 6，𝑎= 3.3981 𝑐𝑚.                                                                                (Eq. 26)

<!-- b000382 | furniture | pages [16] -->


<!-- b000383 | caption | pages [16] -->
Fig. 20 Best Arrangement for Test One

<!-- b000384 | prose | pages [16] -->
Then, find the minimum value of the objective function, which is:

<!-- b000385 | prose | pages [16] -->
40×30

<!-- b000386 | prose | pages [16] -->
2×754.8372) + 0.5 × 0.3861 = 0.2956.                                 (Eq. 27)

<!-- b000387 | prose | pages [16] -->
𝑓(𝑝= 0.5)𝑚𝑖𝑛= 0.5 (1 −

<!-- b000388 | furniture | pages [16] -->


<!-- b000389 | prose | pages [16] -->
Test 2:  p = 0.25, W/L = 9/13 = 0.6923.

<!-- b000390 | prose | pages [16] -->
(For polygon, m is the number of edges, a is the length of edges.)

<!-- b000391 | prose | pages [16] -->
𝑁= 30，𝑚= 8，𝑎= 2.4926 𝑐𝑚.                                                                                (Eq. 28)

<!-- b000392 | furniture | pages [17] -->
Team # 23004                                                                                                                                                                    Page  16  of  20

<!-- b000393 | furniture | pages [17] -->


<!-- b000394 | caption | pages [17] -->
Fig. 21  Best Arrangement for Test Two

<!-- b000395 | prose | pages [17] -->
Then, find the minimum value of the objective function, which is:

<!-- b000396 | prose | pages [17] -->
30×30

<!-- b000397 | prose | pages [17] -->
2×754.8372) + 0.75 × 0.2048 = 0.2546.                         (Eq. 29)

<!-- b000398 | prose | pages [17] -->
𝑓(𝑝= 0.25)𝑚𝑖𝑛= 0.25 (1 −

<!-- b000399 | furniture | pages [17] -->


<!-- b000400 | prose | pages [17] -->
Test 3:  p = 0.5, W/L = 0.6833.

<!-- b000401 | prose | pages [17] -->
With slightly changes in W/L, the optimal arrangement changes. (For polygon, m is the number of edges, a is the length of edges.)

<!-- b000402 | prose | pages [17] -->
𝑁= 40，𝑚= 8，𝑎= 2.4926 𝑐𝑚.                                                                               (Eq. 30)

<!-- b000403 | furniture | pages [17] -->


<!-- b000404 | caption | pages [17] -->
Fig. 22 Best Arrangement for Test Three

<!-- b000405 | prose | pages [17] -->
Then, find the minimum value of the objective function, which is:

<!-- b000406 | prose | pages [17] -->
40×30

<!-- b000407 | prose | pages [17] -->
2×754.8372) + 0.5 × 0.2048 = 0.2050.                                 (Eq. 31)

<!-- b000408 | prose | pages [17] -->
𝑓(𝑝= 0.5)𝑚𝑖𝑛= 0.5 (1 −

<!-- b000409 | furniture | pages [18] -->
Team # 23004                                                                                                                                                                    Page  17  of  20

<!-- b000410 | prose | pages [18] -->
From the above three cases, we can find that when W/L is kept constant, the weight p will cause changes in the optimal solution and arrangement. When p is kept constant and W/L changes, the optimal solution and the arrangement will also change greatly.

<!-- b000411 | heading | pages [18] -->
Sensitivity analysis

<!-- b000412 | prose | pages [18] -->
The optimization model proposed by the paper is integer programming, which means that as parameters p and W/L change, the optimal solution will be discrete. Such characteristic makes the kind of pans finite, which will reduce producing cost and make large volume production possible. Meanwhile, because of the consideration of the weight p, which denotes the demand of users, we can design many kind of pans which will fulfill their requirements.

<!-- b000413 | prose | pages [18] -->
However, because of this characteristic, the optimal solution will change suddenly as some parameters change (such as W/L). For example, when p = 0.5, W/L change from 9/13 to 0.683, only a slight change of 0.01 will cause the optimal solution and arrangement to change suddenly. So when designing the W/L of pan, we must try to pick more values at the boundary point, or avoid using the boundary point, to avoid wrong optimization.

<!-- b000414 | heading | pages [18] -->
Strengths and Weaknesses

<!-- b000415 | heading | pages [18] -->
Model 1

<!-- b000416 | heading | pages [18] -->
Strengths

<!-- b000417 | prose | pages [18] -->
This model starts from heat transfer theory, considers the constant temperature working state of baking ovens, proposes proper assumptions and establishes heat transfer equation for pans based on heat transfer which considers convection. Through simplification and solving, we get the steady-state solution and find the reason for overcooking at the corners and how it changes. Because we took both heat conductivity and convection, it will makes our solution more compelling.

<!-- b000418 | heading | pages [18] -->
Weakness

<!-- b000419 | prose | pages [18] -->
Before solving the model, we simplified the three-dimensional model to a two-dimensional model. So the result will be not exactly the same as the real heat distribution.

<!-- b000420 | furniture | pages [18] -->


<!-- b000421 | heading | pages [18] -->
Model 2

<!-- b000422 | heading | pages [18] -->
Strengths

<!-- b000423 | prose | pages [18] -->
As we built this model, we correct two parameters of the objective function, which make the changing speeds approximately the same to facilitate weighting optimization.

<!-- b000424 | prose | pages [18] -->
In addition, when solving the model, we propose an algorithm based on Center Matrix Statistics to solve 2-D polygon arrangement problem.

<!-- b000425 | heading | pages [18] -->
Weakness

<!-- b000426 | prose | pages [18] -->
This model neglects some polygons with odd lateral number, such as regular pentagon， regular heptagon and so on. Meanwhile, we consider polygons with too many edges (m>10) approximately as circle, which will confine our results in finite kinds of arrangement patterns.

<!-- b000427 | prose | pages [18] -->
Improvement

<!-- b000428 | prose | pages [18] -->
Firstly, all the pan shapes designed in the paper are of sharp corners. If rounded corners are used, the heat distribution will be more even.

<!-- b000429 | furniture | pages [19] -->
Team # 23004                                                                                                                                                                    Page  18  of  20

<!-- b000430 | furniture | pages [19] -->


<!-- b000431 | caption | pages [19] -->
Fig. 23 Changes on Round Corners

<!-- b000432 | prose | pages [19] -->
Secondly, all the pan shapes designed in the paper are of either rectangles or regular shapes. If normal polygon are used, the heat distribution would be more even.

<!-- b000433 | prose | pages [19] -->
Advertising Sheet

<!-- b000434 | prose | pages [19] -->
The authors provided advertising sheets attached at the end of the article. The Brownie Cake photo on the Sheet is picked from http://e.weibo.com/2278459747/app_4048278376. We promise not let the photo for commercial uses.

<!-- b000435 | prose | pages [19] -->
See advertising Sheets on Next Two Pages.

<!-- b000436 | prose | pages [19] -->
Acknowledgment

<!-- b000437 | prose | pages [19] -->
The authors thank Hamilton Beach Company, the author Cakedear for permission to use data and photos of Ovens, Pans and Brownie cakes from their website.

<!-- b000438 | heading | pages [19] -->
References

<!-- b000439 | references | pages [19] -->
[1] Melike Sakin, Figen Kaymak-Ertekin, Coskan Ilicali1, Convection and radiation combined

<!-- b000440 | references | pages [19] -->
surface heat transfer coefficient in baking ovens, Journal of Food Engineering, Volume 94, Issues

<!-- b000441 | references | pages [19] -->
3–4, October 2009, Pages 344–349.

<!-- b000442 | references | pages [19] -->
[2] Frank Kreith, Raj M. Manglik, Mark S. Bohn, Principles of Heat Transfer, SI ed., Cengage

<!-- b000443 | references | pages [19] -->
Learning, 2010.

<!-- b000444 | references | pages [19] -->
[3] Donald Pitts, Leighton Sissom, Schaum’s Outline of Theory and Problems of Heat Transfer,

<!-- b000445 | references | pages [19] -->
Second Edition, McGraw-Hill, 2002.

<!-- b000446 | references | pages [19] -->
[4] Zhu Qiumin, Chen Xiaoping, Application of PDE Toolbox and Least Square Method in Heat

<!-- b000447 | references | pages [19] -->
Conduction of Metal, Process Automation Instrumentation, Volume 32, No.6, June 2011, Pages

<!-- b000448 | references | pages [19] -->
26-31.

<!-- b000449 | furniture | pages [20] -->


<!-- b000450 | references | pages [20] -->
T E A M # 2 3 0 0 4      P A G E 1 9 O F 2 0

<!-- b000451 | references | pages [20] -->
The Ultimate Brownie Pan

<!-- b000452 | references | pages [20] -->
That will reduce overcooking at the edges and fit your demand in a

<!-- b000453 | references | pages [20] -->
maximum extent.

<!-- b000454 | furniture | pages [20] -->


<!-- b000455 | references | pages [20] -->
How it works

<!-- b000456 | references | pages [20] -->
Why?

<!-- b000457 | references | pages [20] -->
The figure above shows

<!-- b000458 | references | pages [20] -->
the temperature distribution of a

<!-- b000459 | references | pages [20] -->
rectangular pan. We can see

<!-- b000460 | references | pages [20] -->
that it’s much hotter in 4 corners

<!-- b000461 | references | pages [20] -->
Our research on the optimization of heat distribution of

<!-- b000462 | references | pages [20] -->
than other places.

<!-- b000463 | references | pages [20] -->
baking pan has greatly progressed. We have already

<!-- b000464 | references | pages [20] -->
known the reasons and rules of heat distribution of the

<!-- b000465 | references | pages [20] -->
Thus when using traditional

<!-- b000466 | references | pages [20] -->
Rectangular baking pan, your

<!-- b000467 | references | pages [20] -->
baking pan. We develop a model to design different

<!-- b000468 | references | pages [20] -->
Brownie cakes would be over-

<!-- b000469 | references | pages [20] -->
kinds of pans to meet your requirements, both for

<!-- b000470 | references | pages [20] -->
home users and food processing factory.

<!-- b000471 | references | pages [20] -->
cooked at 4 corners.

<!-- b000472 | references | pages [20] -->
This brochure will guide you to know and choose

<!-- b000473 | references | pages [20] -->
your own Pans!

<!-- b000474 | references | pages [20] -->
The temperature distribu-

<!-- b000475 | references | pages [20] -->
tion is more even in circle pan

<!-- b000476 | references | pages [20] -->
as the figure below.

<!-- b000477 | references | pages [20] -->
Different Shapes, Different Tastes!

<!-- b000478 | furniture | pages [20] -->


<!-- b000479 | references | pages [20] -->
Design for U

<!-- b000480 | references | pages [20] -->
Easy Baking

<!-- b000481 | references | pages [20] -->
More little

<!-- b000482 | furniture | pages [20] -->


<!-- b000483 | furniture | pages [20] -->


<!-- b000484 | references | pages [20] -->
Pans

<!-- b000485 | references | pages [20] -->
Combining both

<!-- b000486 | references | pages [20] -->
For beginner,

<!-- b000487 | references | pages [20] -->
Crisp tastes in

<!-- b000488 | references | pages [20] -->
factors, and

<!-- b000489 | references | pages [20] -->
Easier in control-

<!-- b000490 | references | pages [20] -->
cake corners,

<!-- b000491 | references | pages [20] -->
generating your

<!-- b000492 | references | pages [20] -->
ling temperature,

<!-- b000493 | references | pages [20] -->
require higher

<!-- b000494 | references | pages [20] -->
own baking

<!-- b000495 | references | pages [20] -->
soft tastes.

<!-- b000496 | references | pages [20] -->
baking skills.

<!-- b000497 | furniture | pages [20] -->


<!-- b000498 | furniture | pages [21] -->


<!-- b000499 | furniture | pages [21] -->
TEAM # 23004                                  PAGE 20 OF 20

<!-- b000500 | references | pages [21] -->
THE ULTIMATE BROWNIE PAN

<!-- b000501 | furniture | pages [21] -->


<!-- b000502 | furniture | pages [21] -->


<!-- b000503 | references | pages [21] -->
Pick From Four Choices or Customize Your Own

<!-- b000504 | references | pages [21] -->
Do you enjoy baking your own Brownie

<!-- b000505 | references | pages [21] -->
Cakes at home?

<!-- b000506 | references | pages [21] -->
Are you tired of baking corner-overcooked

<!-- b000507 | references | pages [21] -->
cakes?

<!-- b000508 | references | pages [21] -->
Rectangular Size with more pans

<!-- b000509 | references | pages [21] -->
This kind of pan is based on rectangular shapes.

<!-- b000510 | references | pages [21] -->
It will bring you more Crisp Tastes in the corner of

<!-- b000511 | references | pages [21] -->
cakes. With more little pans, you can bake more

<!-- b000512 | references | pages [21] -->
cakes at once. In other words, this kind of pan

<!-- b000513 | references | pages [21] -->
will Save Your Money, or reducing carbon

<!-- b000514 | references | pages [21] -->
emissions in production. It’s more suitable for

<!-- b000515 | references | pages [21] -->
food processing factory.

<!-- b000516 | references | pages [21] -->
Regular Hexagon Pans

<!-- b000517 | references | pages [21] -->
The cake baked in this pan is crisper but softer.

<!-- b000518 | references | pages [21] -->
And it’s easier to handle. With a smaller amount

<!-- b000519 | references | pages [21] -->
of pans，it is more suitable for Home Users. We

<!-- b000520 | references | pages [21] -->
can customize the sizes for your own oven.

<!-- b000521 | references | pages [21] -->
Regular Octagon Pans

<!-- b000522 | references | pages [21] -->
This kind of pan is more exquisite for those

<!-- b000523 | references | pages [21] -->
people who Enjoy Cooking. It will bake lovely

<!-- b000524 | references | pages [21] -->
cakes. If you have children in your home, we

<!-- b000525 | references | pages [21] -->
suggest you1 prefer this kind. With better

<!-- b000526 | references | pages [21] -->
shapes of cakes, Stronger Appetite will

<!-- b000527 | references | pages [21] -->
stimulate!

<!-- b000528 | references | pages [21] -->
Circle Pans for Beginner

<!-- b000529 | references | pages [21] -->
If you are a beginner in baking or cooking, circle

<!-- b000530 | references | pages [21] -->
Pans are strongly recommended for you. Tastes

<!-- b000531 | references | pages [21] -->
of cakes in this kind of pan will be soft and loose.

<!-- b000532 | references | pages [21] -->
Customize Your Own

<!-- b000533 | references | pages [21] -->
If you have other requirements, you are

<!-- b000534 | references | pages [21] -->
welcomed to contact us. We will do our best to

<!-- b000535 | references | pages [21] -->
meet your demand and satisfaction.

<!-- b000536 | furniture | pages [21] -->


<!-- b000537 | furniture | pages [21] -->

