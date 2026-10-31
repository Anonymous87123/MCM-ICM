Summary

Through the analysis of the heat distribution along the edges of pans affected by different pan shapes, the article finds the reason for the overcooking of the product at the edges when using a rectangular pans. Furthermore, according to the requirements given by the problem, the authors propose the optimization model for designing the optimal baking pan.

The paper propose two models and one algorithm. Model one is established to investigate the heat distribution at the edges of pans in different shapes, while model two and the algorithm are used to design the ultimate pan.

Model one describes the heat distribution at the edges of polygons. Based on the equation of heat conduction while taking the convection effects into account, the authors design a model that can describe the thermal conduction inside the pan. Then, given certain Neumann boundary condition, Finite-Element Analysis derives the approximate result of heat distribution, where we can find the phenomena of overcooking at the edges, which matches the practical phenomena described in the problem. Through curve fitting, the authors also find that, for polygons, the standard deviation of temperature of the edges is in inversely proportional to the square of the number of edges.

Model two can be used to find the ultimate solution of baking pan. In the analysis of this model, according to the requirements given by the problem, the author proposed two factors: area utilization rate and the degree of uneven of temperature. Then, the paper analyzed the changing speed of the two factors as the number of edges increases, adding correction factors R and weight p in order to construct proper objective function. After modeling, the authors proposed three evaluation methods of the model in response to the three conditions given by the problem. For the first condition, integer programming is adopted to give the proper arrangement of rectangular pans; for the last two conditions, the authors use a new algorithm to give the proper arrangement of circular and regular polygon pans.

The new algorithm proposed in this paper is a polygon arrangement model based on Center Dot Matrix Statistics, which is used to test the maximum number of a certain kind of polygon or circles that can be put in a certain area. Then, based on this algorithm, the models are tested with several examples, the shapes and numbers of pan for different W/L and p are calculated.

Finally, the sensitivity analysis and model evaluation are performed. During sensitivity analysis, the sudden change phenomenon that emerged when W/L and p change are found. During model evaluation, strengths and weaknesses are analyzed for different models, and suggestion of using rounded corners and normal polygons are proposed for model two.

Abstract

Through the analysis of the heat distribution along the edges of pans affected by different pan shapes, the article finds the reason for the overcooking of the product at the edges when using a rectangular pans. Furthermore, according to the requirements given by the problem, the authors propose the optimization model for designing the optimal baking pan.

The paper propose two models and one algorithm. Model one is established to investigate the heat distribution at the edges of pans in different shapes, while model two and the algorithm are used to design the ultimate pan.

Model one describes the heat distribution at the edges of polygons. Based on the equation of heat conduction while taking the convection effects into account, the authors design a model that can describe the thermal conduction inside the pan. Then, given certain Neumann boundary condition, Finite-Element Analysis derives the approximate result of heat distribution, where we can find the phenomena of overcooking at the edges, which matches the practical phenomena described in the problem. Through curve fitting, the authors also find that, for polygons, the standard deviation of temperature of the edges is in inversely proportional to the square of the number of edges.

Model two can be used to find the ultimate solution of baking pan. In the analysis of this model, according to the requirements given by the problem, the author proposed two factors: area utilization rate and the degree of uneven of temperature. Then, the paper analyzed the changing speed of the two factors as the number of edges increases, adding correction factors R and weight p in order to construct proper objective function. After modeling, the authors proposed three evaluation methods of the model in response to the three conditions given by the problem. For the first condition, integer programming is adopted to give the proper arrangement of rectangular pans; for the last two conditions, the authors use a new algorithm to give the proper arrangement of circular and regular polygon pans.

The new algorithm proposed in this paper is a polygon arrangement model based on Center Dot Matrix Statistics, which is used to test the maximum number of a certain kind of polygon or circles that can be put in a certain area. Then, based on this algorithm, the models are tested with several examples, the shapes and numbers of pan for different W/L and p are calculated.

Finally, the sensitivity analysis and model evaluation are performed. During sensitivity analysis, the sudden change phenomenon that emerged when W/L and p change are found. During model evaluation, strengths and weaknesses are analyzed for different models, and suggestion of using rounded corners and normal polygons are proposed for model two.

Introduction

The authors are intended to model the process of oven baking, analyze the distribution of heat along the edges of pans affected by different pan shapes, in order to find the reason for overcooking of food at the corners when using rectangular pans. Afterwards, the authors construct a model that can optimize the ultimate pan shape and arrangement according to the following conditions.

1. Maximize number of pans that can fit in the oven (N).

2. Maximize even distribution of heat (H) for the pan.

3. Optimize a combination of conditions (1) and (2) where weights p and (1- p) are assigned to illustrate how the results vary with different values of W/L and p.

In this article, the authors decompose the problem into the following steps when modeling and solving:

1. Construct the uneven degree index of pans of different shapes; (also the analysis result of model one) 2. Construct the objective function of the combination optimal problem and uniform the optimization direction of different subgoals;

3. Pick and determine the proper combination of types and numbers of pans;

4. Construct arrangement model, use the model to arrange the results of step 3, and then find the optimal solution.

Basic Assumptions

1. The temperature in the oven is constant and forced air convection is adopted.

2. The pans are made of isotropic material with good thermal conductivity properties.

3. Basic notations in the article are list as follow.

Symbol Meaning A, S Area T Temperature t Time ρ Density m Edge number of polygon x, y, z Axis of the rectangular coordinates Q Heat λ Coefficient of thermal conductivity h Coefficient of convection heat transfer c Specific heat capacity L, l Length W, w Width N, n Number q Heat flux Outward normal vector of a plane 𝑛⃑ Utilization rate of Area 𝜂 Standard deviation 𝜎

4. The shape of pan is approximately rectangular box with no lid. The shapes and the basic model are given as follow:

Model 1:    The Distribution of Heat at the Edges of Polygon

According to heat-transfer principles, there are three ways for heat to transfer: heat radiation, heat conductivity and heat convection.

In a baking oven, the hot air flows over the baking material either by natural convection or forced by a fan, the convection heat transfer from the air, the radiation heat transfer from the oven heating surfaces, and the conduction heat transfer across contact area between product and metal surface. [1] In most heat-controllable ovens, as the temperature inside the oven can be kept constant, the main source of heat that will result in the overcooking of food is the metal pan. So this model mainly focuses on the heat conductivity inside the metal pans.

The basic model of heat flow launched into the metal pan is as follow.

As we assume that the pan is isotropic, the heat flux received by different facets of the pan should be the same inside the oven. As a result, the non-uniformity is resulted from the heat convection between the pan and air and the heat transfer inside the metal material. According to the heat-transfer equation (Eq. 1), [2, 3]

𝜕2𝑇 𝜕2𝑇 𝜕2𝑇 𝜕𝑇 𝜕𝑧2) = 𝑄𝑔,                                                                                  (Eq. 1) 𝜌𝑐 𝜕𝑡−𝜆( 𝜕𝑥2 + 𝜕𝑦2 +

Where T represents temperature, 𝑄𝑔 represents inner heat source, 𝜌 represents density, 𝑐 represents specific heat capacity，𝜆 represents thermal conductivity, when balance is achieved, the temperature stops to change. So

𝜕𝑇 𝜕𝑡= 0, (𝑡→∞).                                                                                                                               (Eq. 2)

From Eq. 2, we can derive the equation of steady state heat transfer without inner heat source, concerning the coefficient of convection heat transfer, which is the steady state heat transfer equation (Eq. 3) of baking pan.

𝜕2𝑇 𝜕2𝑇 𝜕2𝑇 𝜕𝑧2) = ℎ(𝑇𝑒𝑥𝑡−𝑇)                                                                                           (Eq. 3) −𝜆( 𝜕𝑥2 + 𝜕𝑦2 +

In Eq. 3, the ℎ represents the coefficient of heat convection. The 𝑇𝑒𝑥𝑡 represents outer temperature of the air. The boundary condition is Neumann boundary condition, which is used when all facets’ heat flux density of normal vector 𝑞𝑒𝑑𝑔𝑒 are known. The 𝑛⃑  represents the outward normal vector of a plane.

𝜕𝑇 𝜕𝑛⃑ = 𝑞(𝑥, 𝑦, 𝑧, 𝑡)                                                                                                         (Eq. 4) 𝑞𝑒𝑑𝑔𝑒= −𝜆

Eq. 4 is a third-order partial differential equation (PDE). However, if we assume that only the heat from the bottom of the pan is considered, the distribution of heat on the surface of the pan will be even. Thus, the unevenness of heat distribution is mainly resulted from the heat received by side facets. As a result, the three-dimensional model can be simplified into a two-dimensional model as follow.

𝜕2𝑇 𝜕2𝑇 𝜕𝑦2) = ℎ(𝑇𝑒𝑥𝑡−𝑇) −𝜆( 𝜕𝑥2 + { .                                                                                                  (Eq. 5) 𝜕𝑇 𝑞𝑒𝑑𝑔𝑒= −𝜆 𝜕𝑛⃑ = 𝑞0

The steady state solution can be calculated using finite element analysis method. Using the PDE Toolbox provided by Matlab, we can get the numerical solution of this model. [4] Now, the heat distribution on a square pan made of certain kind of experimental material are calculated using the following parameters and boundary condition. These parameters and boundary conditions are regarded as the standard state of tests in this paper.

Physical Quantity Value 50 [ W / ( K · m ) ] 𝜆 100 [ W / ( K · m2 ) ] ℎ 330 [ K ] 𝑇𝑒𝑥𝑡 1000 [ W / ( s · m ) ] 𝑞0 The calculation results are presented as follow.

We can see that the temperatures at the corners are high while the temperature at the center is the lowest. The change of temperature along the edge is significant. If circular pan is chosen, the heat distribution at the edge will be even, while the temperature at the center is also relatively low.

Then, the area of pan are kept constant, while the number of edges is increased, which will make the pan approach circle in shape. We can see the following pattern of change where we can find that the heat distribution at the edges is approximately parabolic. Also, as the number of edges increases, the heat distribution will tend to be even, the variance of temperature will decrease.

Meanwhile, standard deviations as listed below are calculated to represent the uniformity.

We can see that as the number of lateral increases, the trend of overall standard deviation and standard deviations at the edges are of the same direction, which is decreasing. Also, we can see that as the number of edges increases, the overall standard deviation approaches a certain value, while the standard deviation at the edges approached zero. Thus, the shape determines the heat distribution at the edges, and also affects the overall heat distribution. The more edges it has, the more even the heat is distributed.

As a result, we can use the standard deviation of temperature at the edges to denote the overall degree of even distribution of heat.

Number of Overall standard Deviation at the Standard deviation at Per-unit 2 ） value edges（m） deviation（𝜎𝑤） edges（𝜎𝑚 the edges（𝜎𝑚） 4 4.3236 2.2918 1.5139 1 5 3.2438 0.6959 0.8342 0.5510 6 2.8923 0.3416 0.5845 0.3861 7 2.7342 0.1716 0.4142 0.2736 8 2.6159 0.0961 0.3100 0.2048 10 2.5089 0.0535 0.2313 0.1528 14 2.4155 0.0090 0.0949 0.0627 16 2.3754 0.0057 0.0755 0.0499 1.0041 0 0.0000 0.0000 ∞（Circle） Using Matlab to do the curve fitting, we can get the approximate relationship between the number of edges and the even distribution degree of heat represented by standard deviation at the edges.

23.605 23.605 1 𝑚2.                                                                                      (Eq. 6) 𝜎= + 0.035 ≈ ∝ 𝑚2 𝑚2

This model properly explains the reason for the problem of uneven heating at the edges of pans. Meanwhile, we can see how the heat distribution changes as the shape of pan changes from polygon to circle.

Model 2:    Baking Pan Optimization Design Model

Determination of the objective function

We have already known from the problem and the results of model one that the uniformity of heat distribution changes as the shape of pan changes. In order to design and optimize pan shape, we need to consider two factors of pan’s characteristics.

Factor One: The Area Utilization Rate of Rack η This is defined as follow,

𝑁𝐴 2𝑆  .                                                                                                                       (Eq. 7) 𝜂= 1 −

In Eq. 7, A is the area of a single pan. N is the total number of all pans. S is the area of a rack. The smaller η is, the higher the utilization rate of area is achieved.

According to the 2-D arrangement principle, only rectangle and hexagon can be used to cover an infinite plane area without overlap and leaving intervals, while other shapes cannot be used to do the job.

As a result, the only way to achieve maximum rack area utilization rate is to use pans of rectangle or hexagon shapes. When it comes to finite plain area, because of the constraint of boundary, the arrangement job may become more complex. We will address the problem later in this paper.

Factor Two: the Temperature Discrepancy Rate σ In model one, we discussed the feasibility of using the standard deviation of temperature at the edges to indicate the degree of even distribution rate.

We define the temperature discrepancy rate as follow:

∑𝑛𝑖𝜎𝑖 𝜎0𝑁,                                                                                                                             (Eq. 8) 𝜎=

Where 𝜎𝑖 is the standard deviation of temperature at the edges of pans with shape No. i, 𝑛𝑖 is the number of pan with shape No. i. In order to facilitate optimization, we convert the standard deviation to per-unit value, using the largest standard deviation 𝜎0 (which is the standard deviation for rectangular pan) as the base value. A smaller 𝜎 indicate smaller temperature discrepancy between parts of the pan and more even distribution of heat.

The conclusion of model one tells that the degree of even distribution of heat at the edges of regular polygon is inversely proportional to the square of its number of edges. So the heat distribution of circle is most even while the rectangles’ are the worst.

According to the different demands of user, we use p as the weight of factor one, (1-p) as the weight of factor two. The optimization directions of the two indicators are the same. So the indicator of demand and the optimization direction are as follow:

𝑚𝑖𝑛   [𝑅× 𝜂𝑝+ 𝜎(1 −𝑝)],                                                                                                 (Eq. 9)

Where R is the correction factor, which is used to correct the changing speeds of the two factors. This factor will help reduce the imbalance during optimization. When the shape changes, R can make the changing speeds of them tend to be the same. The setting of R will be discussed later in the paper.

Then, general constraints are listed as follow,

2𝑆−𝑁𝐴≥0 ∑𝑛𝑖= 𝑁,  𝑛𝑖∈𝑍+    .                                                                                        (Eq. 10) 𝑆. 𝑇.     {

Now, we will do the optimization according to the following three kind of requirements of users. (3 condition) 1. Maximize number of pans that can fit in the oven (N).

2. Maximize even distribution of heat (H) for the pan.

3. Optimize a combination of conditions (1) and (2) where weights p and (1- p) are assigned to illustrate how the results vary with different values of W/L and p.

Condition 1:   To Achieve Maximum Number of Pans. (p=1)

𝑁𝐴 𝑆) ⇒ 𝑚𝑎𝑥 𝑁 .                                                                             (Eq. 11) 𝑚𝑖𝑛  𝜂= 𝑚𝑖𝑛 (1 −

In order to achieve maximum number of pans, close packed structure must be used. Meanwhile, because of the constraint of the shape of rack, only rectangular pans can leave the least space at the edges of rack. So the number of pans will be: ([x] represents the largest integer which is less than x)

𝑆 𝐴] .                                                                                                                   (Eq. 12) 𝑁𝑚𝑎𝑥= 2 [

Now, we need to model the close package of rectangles to get the final arranging pattern.

Geometric constraints (the width and length ration W/L is not constant):

𝐴= 𝑤𝑙, 𝑆= 𝑊𝐿, 𝑁𝑚𝑎𝑥 ≥𝑛𝑤𝑛𝑙, (Eq. 13) 𝑆. 𝑇.     { 2 𝑊 𝐿 1 ≤𝑛𝑤≤[ 𝑤] , 1 ≤𝑛𝑙≤[ 𝑙] .

This model may not be able to give a clos package. So, we will firstly make the pans closely attached to the certain three edges, and then splice the left space into (𝑁𝑚𝑎𝑥−𝑛𝑤𝑛𝑙) rectangles with different areas.

We can see from the above result that only if the area of rack S is the integral multiple of area of a single pan A, it is possible to achieve close package with rectangles, which means that any other condition will not achieve close package.

Condition 2:   The Most Even Distribution of Heat. (p=0)

∑𝑛𝑖𝜎𝑖 𝜎0𝑁 .                                                                                                       (Eq. 14) 𝑚𝑖𝑛  𝜎= 𝑚𝑖𝑛

It requires that the heat distribution should be as even as possible while ignoring the utilization rate. So we will totally use circular pans. That is:

𝑆 𝐴].                                                                                                           (Eq. 15) 𝑁≤𝑁𝑚𝑎𝑥= 2 [

The number of pans will be less than the maximum possible number. Now we need to establish a model for arranging circles to get the final arranging pattern. There are two possible patterns:

The distance between the centers of basic units for close package is equal to the diameter of circle. The basic units of the dot matrix of centers are triangles and squares respectively. So optimization should be done for each pattern. Considering that the arrangement of circles is like the arrangement of regular polygons, we propose an algorithm based on center matrix statics, which will be illustrated later in this paper.

Condition 3:    0<p<1

𝑚𝑖𝑛   [𝑅× 𝜂𝑝+ 𝜎(1 −𝑝)] .                                                                                             (Eq. 16)

For some users, both the even distribution of heat, which will reduce the possible overcooking at edges, and the high utilization rate of pan area are supposed to achieve, or that a slight overcooking cake is desired for better taste. So we wish that weight p and (1-p) will be used to reflect the users’ specific requirement.

The first step is to determine the correction factor R to correct the objective function. In model one, we have analyzed how 𝜎 changes with the shape of pans. Then, we need to do further analysis on the rules that the unused area changes as the shape of pans changes.

In order to reduce the unused area at the rack, we need to arrange the pans as closely as possible. Now, the arrangement of different kinds of polygons are listed as follow.

1. Rectangle Unused space only appears at the edges.

2. Regular octagon There will be two kinds of unused space: at the edges and the holes in-between.

3. Regular hexagon Unused space only appears at the edges.

4. Regular m-gon (m>=12) The shape will be like circle. In an attempt to reduce cost, we will use circles instead of such polygons.

5. Other polygons It will be impossible to achieve overlap of edges because the inner angles are not 60 or 90 degree. There will be much more unused space, so such arrangements will not be considered.

Now we only need to analyze the arrangement of rectangles (including squares), regular hexagons, regular octagons and circles.

For any regular polygon with an edge number of 4l (l>1), when we arrange them as the edges overlap with adjacent polygons, the area they encompass will be regular polygon with an edge number of 4(l-1), the relationship between area and number of edges is:

𝑐𝑜𝑡 𝜋 −1).                                                                                                           (Eq. 17) 4𝑙 𝑆𝑙= 𝐴( 𝑙

The changing speed of the value of this function will be approximately the same with the changing speed of σ in the above conditions (rectangles, regular hexagons, regular octagons and circles), but with opposite direction. So the correction factor will have a constant value, which means:

𝑅= 𝑐𝑜𝑛𝑠𝑡.                                                                                                                       (Eq. 18)

Finally, when 0<p<1, the arrangement model will be further divided into the following conditions to facilitate further discussion, that is, rectangle, regular hexagon, regular octagon, circle and the combination of them.

Now, we use the following model:

𝑚𝑖𝑛   [𝑅× 𝜂𝑝+ 𝜎(1 −𝑝)].                                                                                              (Eq. 19)

2𝑆−𝑁𝐴≥0 𝑛4 + 𝑛6 + 𝑛8 + 𝑛∞= 𝑁,  𝑛𝑖∈𝑍+ .                                                                     (Eq. 20) 𝑆. 𝑇.     { 𝜎𝑖∈{  𝜎4,  𝜎6,  𝜎8,  𝜎∞}

The solution of the model will be a vector n, where all the terms are integer. Considering the constraints of the actual area of two racks and the maximum number of pans, we only allow the combination of a maximum number of two shapes of pans appears simultaneously on a rack. Then we will use the algorithm illustrated as follow to calculate the arrangement and compare the result of objective function, and then find the optimal solution.

Algorithm:    Regular Polygon Arrangement Based on Center Matrix Statics

Every kind of polygon has several unique close package arranging patterns. As a result, we can draw the matrix of centers on graph paper. Make the axis overlap with edges of polygons as much as possible. Thus, we only need to determine whether the polygon with a certain center can be put inside the rectangle or the boundaries. Take rectangle rack boundaries as the example.

For any point that lays inside the rectangle, it must comply the following conditions: 1. The least distance between this point and the edges of the rectangle must not be less than the radius of its inscribed circle; 2. For hexagon, the least distance between this point and the edges of the rectangle must not be less than the radius of its circumcircle; For regular hexagon, because of that the distance between dots along x axis and along y axis are different, we need to rotate the rack 90 degree when one analysis is finished and do the analysis again, and then pick the optimal arrangement.

The flow chart of Algorithm is listed as follow. In tests with actual examples, we will use the method described above to give the optimal pan design when different p and W/L are given.

Start

Input Boundary equations and the shapes of polygon No Build the center dot matrix of an arrangement Select a dot dot within ranges ?

Output N as No Yes the result

End The dot within boundaries ?

Yes 1.The least distance Calculate the distance Initialize the Number of polygon in this arrangement N = 0 No

Algorithm Flowchart

for 2-D Arrangement Based on Center Dot Matrix between this point and between the dot and the edges of the rectangle all the boundaries must not be less than the radius of its inscribed circle; 2.For hexagon, the least Dot meets the arranging distance between this conditions ?

point and the edges of Yes the rectangle must not be less than the radius of its N=N+1 circumcircle;

Model test

We picked Countertop Oven with Convection and Rotisserie (31100) with two 9”x13” racks (The pictures are picked from http://www.hamiltonbeach.com/products/toaster-ovens-countertop- oven-with-convection-and-rotisserie-3110).

We suppose that the oven is used to bake many brownie cakes with area of 30 cm2. The environment inside the oven and of the pan is standard. We pick the correction factor R as 1, and then the objective function will be:

𝑚𝑖𝑛   [𝜂𝑝+ 𝜎(1 −𝑝)]

∑𝑛𝑖𝜎𝑖 𝑁𝐴 𝜎0𝑁].                                                                            (Eq. 21) 2𝑆) + (1 −𝑝) = 𝑚𝑖𝑛  [𝑝(1 −

2𝑆−𝑁𝐴≥0 𝑛4 + 𝑛6 + 𝑛8 + 𝑛∞= 𝑁,  𝑛𝑖∈𝑍+ .                                                                   (Eq. 22) 𝑆. 𝑇.     { 𝜎𝑖∈{  𝜎4,  𝜎6,  𝜎8,  𝜎∞}

Arranging patterns are as follow:

Shape Arranging pattern 1 Arranging pattern 2

Rectangle

Square See Condition 1

Regular hexagon

Regular octagon Shape Arranging pattern 1 Arranging pattern 2

Circle

Basic parameters:

𝑆= 9’’ × 13’’ = 22.86 𝑐𝑚 × 33.02 𝑐𝑚= 754.8372 𝑐𝑚2 ,                                          (Eq. 23)

𝐴= 30 𝑐𝑚2 ,                                                                                                                    (Eq. 24)

𝑆 𝐴] = 50.                                                                                        (Eq. 25) 𝑁≤𝑁𝑚𝑎𝑥= 2 [

Test 1:   p = 0.5, W/L = 9/13 = 0.6923.

(For polygon, m is the number of edges, a is the length of edges.)

𝑁= 40，𝑚= 6，𝑎= 3.3981 𝑐𝑚.                                                                                (Eq. 26)

Then, find the minimum value of the objective function, which is:

40×30 2×754.8372) + 0.5 × 0.3861 = 0.2956.                                 (Eq. 27) 𝑓(𝑝= 0.5)𝑚𝑖𝑛= 0.5 (1 −

Test 2:  p = 0.25, W/L = 9/13 = 0.6923.

(For polygon, m is the number of edges, a is the length of edges.)

𝑁= 30，𝑚= 8，𝑎= 2.4926 𝑐𝑚.                                                                                (Eq. 28) Then, find the minimum value of the objective function, which is:

30×30 2×754.8372) + 0.75 × 0.2048 = 0.2546.                         (Eq. 29) 𝑓(𝑝= 0.25)𝑚𝑖𝑛= 0.25 (1 −

Test 3:  p = 0.5, W/L = 0.6833.

With slightly changes in W/L, the optimal arrangement changes. (For polygon, m is the number of edges, a is the length of edges.)

𝑁= 40，𝑚= 8，𝑎= 2.4926 𝑐𝑚.                                                                               (Eq. 30)

Then, find the minimum value of the objective function, which is:

40×30 2×754.8372) + 0.5 × 0.2048 = 0.2050.                                 (Eq. 31) 𝑓(𝑝= 0.5)𝑚𝑖𝑛= 0.5 (1 − From the above three cases, we can find that when W/L is kept constant, the weight p will cause changes in the optimal solution and arrangement. When p is kept constant and W/L changes, the optimal solution and the arrangement will also change greatly.

Sensitivity analysis

The optimization model proposed by the paper is integer programming, which means that as parameters p and W/L change, the optimal solution will be discrete. Such characteristic makes the kind of pans finite, which will reduce producing cost and make large volume production possible. Meanwhile, because of the consideration of the weight p, which denotes the demand of users, we can design many kind of pans which will fulfill their requirements.

However, because of this characteristic, the optimal solution will change suddenly as some parameters change (such as W/L). For example, when p = 0.5, W/L change from 9/13 to 0.683, only a slight change of 0.01 will cause the optimal solution and arrangement to change suddenly. So when designing the W/L of pan, we must try to pick more values at the boundary point, or avoid using the boundary point, to avoid wrong optimization.

Strengths and Weaknesses

Model 1

Strengths

This model starts from heat transfer theory, considers the constant temperature working state of baking ovens, proposes proper assumptions and establishes heat transfer equation for pans based on heat transfer which considers convection. Through simplification and solving, we get the steady-state solution and find the reason for overcooking at the corners and how it changes. Because we took both heat conductivity and convection, it will makes our solution more compelling.

Weakness

Before solving the model, we simplified the three-dimensional model to a two-dimensional model. So the result will be not exactly the same as the real heat distribution.

Model 2

Strengths

As we built this model, we correct two parameters of the objective function, which make the changing speeds approximately the same to facilitate weighting optimization.

In addition, when solving the model, we propose an algorithm based on Center Matrix Statistics to solve 2-D polygon arrangement problem.

Weakness

This model neglects some polygons with odd lateral number, such as regular pentagon， regular heptagon and so on. Meanwhile, we consider polygons with too many edges (m>10) approximately as circle, which will confine our results in finite kinds of arrangement patterns.

Improvement

Firstly, all the pan shapes designed in the paper are of sharp corners. If rounded corners are used, the heat distribution will be more even.

Secondly, all the pan shapes designed in the paper are of either rectangles or regular shapes. If normal polygon are used, the heat distribution would be more even.

Advertising Sheet

The authors provided advertising sheets attached at the end of the article. The Brownie Cake photo on the Sheet is picked from http://e.weibo.com/2278459747/app_4048278376. We promise not let the photo for commercial uses.

See advertising Sheets on Next Two Pages.

Acknowledgment

The authors thank Hamilton Beach Company, the author Cakedear for permission to use data and photos of Ovens, Pans and Brownie cakes from their website.
