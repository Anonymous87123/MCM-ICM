MCM/ICM

Summary Sheet

Summary

In recent years, as sand castle art has become more popular, more and more ingenious sand castle art works have been created. However, perfect works of art will disappear, and how to be preserved for a long time becomes an obstacle to the advancement of Sandcastle art.

First, the optimal geometry considering the dual erosion effects of waves and tides is determined. On the basis of reasonably limiting the shape selection range,by establishing the Dynamic Model of the Sandcastle Foundation based on the evaluation index of the comprehensive sand and sand carrying capacity of waves and tides, we use COMSOL to accurately simulate the movement state of the sand castle foundation. On this basis, by creating the Sandcastle Foundation Damage Index, we reasonably determine the duration of the sandcastle. Finally, we use a Discrete Global Optimization Algorithm Based on Successive Descent Methods to determine the shape of the optimal sandcastle foundation as a cylinder.

Secondly, the optimal water-sand mixing ratio is determined. Based on Model 1, a model of Water-sand Aggregation-water-sand Ratio Relationship was first established. By limiting the allowed degree of polymerization, the water-sand ratio is limited to a reasonable range. We again use the discrete global optimization algorithm based on the successive descent method to efficiently find the optimal water-sand mix ratio of 0.739.

Further, an optimal geometry considering rain erosion is determined. We define the sandcastle collapse limit coefficient, and comprehensively establish the Rainwater Erosion Resistance Quantification Model by integrating the ability to resist rainwater infiltration and the evacuation ratio of the sandcastle structure. Further, A Quantified Model of Sandcastle's Ability to Resist Wave Erosion was established. Considering two indicators of anti-erosion ability and establishing a fuzzy comprehensive evaluation model, we determine that the optimal shape is still a cylinder.

Finally, we use the method of humidifying and spraying the adhesive when the air humidity is the lowest to improve the stability of the sand castle foundation. A Humidity Prediction Model Based on the RBF Neural Network Algorithm was established, and we used the model to test the humidity of Venice Beach on August 1. Based on the air humidity data obtained in the previous month, we divided the weather conditions into sunny and cloudy days, and predicted the air humidity trends for sunny and cloudy days on August 1, respectively. Finally, we decided to humidify the sandcastle foundation and spray the adhesive at 13:30 on a cloudy day and 13:00 on a sunny day.

1. Introduction

1.1 Background

Nowadays, people always face heavy schooling or busy work, and spending some time at the beach allows people to enjoy the cool sea breeze, warm sunshine, and soft beaches. Therefore, more and more people choose to go to the beach for leisure. Building sandcastles is a must-do item for beach leisure. It can develop children's creativity and reduce adults' stress to a great extent. When people build sandcastles, they always want their sandcastles to be beautiful and to last longer. Therefore, it is necessary to study how to keep the sandcastle on the beach for the longest time.

1.2 Restatement of the Problem

Building sandcastles is one of the most popular activities item for children on the beach. Every child wants his sandcastle to last for a long time on the beach. Therefore, we were asked to study the persistent retention of sandcastles on the beach. The specific issues are as follows:

Below environmental factors are assumed to be the same, such as: the distance of the beach from  the water, the kind of sand, the amount of sand, the same water-sand ratio. We were asked to build a model under the action of waves and tides to explore the basic geometry of the sandcastle that can last for the longest time on the beach.

Without using any additional additives, how to change the water-sand ratio of the sandcastle  foundation can make our sandcastle last for the longest time on the beach.

Built on the original model, we have considered the impact of rain on the foundation of the  sandcastle, and upgrade and optimize the model to further explore the optimal geometry of the sandcastle.

By consulting some relevant literatures, other strategies have been investigated to improve the  retention time of sandcastles.

2.Assumption and Justification

We make some general assumptions to simplify our model. These assumptions and corresponding justification are listed below:

It is assumed that the base area and height of each considered shape are the same, and that there is  no significant difference in the sand quality and sand quantity of our sandcastle foundation.

Sandcastle foundations are built at approximately the same distance from the water.  In the process of natural erosion, ignore the situation of huge waves and winds sweeping the  sandcastle far from the original location.

We only consider the impact of waves, tides and rain on the water-sand ratio of the sandcastle  foundation.

The sand particles at the sandcastle foundation are evenly distributed.  Assume that people will spray the adhesive in time after the warning occurs, and the adhesive  viscosity lasts at least 8 hours.

More detailed assumptions will be listed if needed.

3.Glossary and Notation

3.1 Glossary

Wave current: refers to the combined effect of waves and tides.  Damage index: It takes the change of the base area and height of the sandcastle as a measuring  factor to describe the damage degree of the sandcastles.

3.2 Notation

Symbols

Definition

sF sand-bearing capacity

G Damage Index

Q Water and sand polymerization degree

n Water-sand ratio p

i F ability to resist rainwater infiltration u

sandcastle structure evacuation ratio i R

i rain erosion resistance H1

i H 2 wave current erosion resistance

 g Neural Network Radial Basis Function

4. Optimal Shape Model Based on Sandcastle Foundation Dynamics

Model

4.1 Model Overview

In terms of shape selection, considering the common sandcastle basic shapes that people are accustomed to using, we only consider the most suitable ones from a cuboid with a certain aspect ratio, an elliptical cylinder with a certain aspect ratio, and a sector with a certain radius and arc length ratio. Excellent shape.First, we have established a model for assessing the sand-bearing capacity of waves. Based on this, the basic dynamics equation of the sandcastle foundation is established. Secondly, by creating a sandcastle foundation damage index, we have determined the duration of a sandcastle of a specific shape. Further, based on the duration of some specific shape sandcastles, we have used a discrete global optimization algorithm based on successive descent methods to determine the optimal sandcastle shape in the global state[1].

4.2 Quantitative model of sand-bearing capacity

Because wave and tide are the two main driving forces in the sand movement of sandcastles, we first have considered how the sandcastles are impacted under the action of waves and tides, and choose to define this ability using the capacity of sand-bearing.

Considering tidal and wave sand-bearing capacity:

(1) C C C   * * * C W The capacity of sand-bearing under tide effect can be expressed as:    n V 2 2 u v  p (2) C   * C C 2 1 n  C h  p z w s Where, n represents the initial value of the water-sand ratio of the sandcastle foundation, which is p determined by the volume ratio;V is the initial value of the sandy volume of the sandcastle foundation; u and v represents the components of the water flow velocity x and y the sum of the waves under the action of waves and tides; is the height of seawater level; is the positive definite coefficient; h w C indicates sand-bearing speed. s Regarding the capacity of sand-bearing under the action of waves, we consider the unbroken wave  and the broken wave respectively, which can be expressed as:

n V 3 1 f H D p (3) C     W rms B   * 1 2 W 3 1 1 n n h    3 sinh T gh kh  p p w s s w w Where, and are respectively the positive definite coefficients of the unbroken wave and the broken  1 2 wave; wf represents the wave friction coefficient; is the mean square wave height, 2 H H H  ， rms rms s H Is the effective wave height; T is the wave period; k is the wave quantization value of one period; s D represents the wave energy dissipation due to the wave breaking. B We build the capacity of sand-bearing sF as:    (4) F C V     * s r s Where,  indicates the sand settling coefficient. r

4.3 Sandcastle Foundation dynamics equation model

We use the right-angle vertex of the three-dimensional geometry as the coordinate center to establish a three-dimensional right-angle coordinate system. Then,changes of and h over timet of our x, y sandcastle foundation satisfy the following equations in dynamic             hV huV hvV hV hV            v v F      (5)   x y s t x y x x y y            Where, yv is the horizontal diffusion coefficient. h indicates the height of the sandcastle foundation; xv and In the dynamic simulation process, we give the constraint that the normal flux is 0 to determine the solid boundary condition as:

V  (6) 0   n  Where,  represents the total flux through the sandcastle foundation; nrepresents the normal vector.  At the same time, we give the time course of the sand volume as the open boundary condition:  t , , V V x y (7) 

4.4 Solution of Sandcastle Foundation Dynamics Equation Model

4.4.1 Solution of Cuboid Dynamics Simulation

Step1. Initialize the parameters of the sandcastle foundation dynamics equation. We take the  optimal shape of a cuboid as an example and define the aspect ratio of the bottom of the cuboid as x, y its shape factor, which is . The initial values of in the equation correspond to , l, w : e l w 1  respectively. In combination with relevant literature, the parameter initialization values in the given dynamic equation are shown in the following table

symbol Numerical value symbol Numerical value symbol Numerical value   0.023 0.300 5.000 T C 1 H C  0.249 0.001 5.185 rms 2 z Wf  D 1.489 1.570 6.301 s B

symbol Numerical value symbol Numerical value

n h 900 6.0 p w

u x 30 1.0 y v 30 1.0 V 100 1 FIG 1. Cuboid simulation diagram when t is equal to zero We use COMSOL to solve the dynamic equations and simulate the pressure effect of wave current 0.1 e on the bottom surface of cuboid. The pressure distribution at time shown in the figure 1  0 t  above is obtained. Among them, the wave current starts from the red part and the pressure gradually decreases. Step2. Establish a damage index indicator model. In order to describe the degree of damage of  the sandcastle and better explain the meaning of duration, we take the change in base area and height as the measuring factor, and give the definition of damage index as (8) G S h       s h Where, and represent respectively the increase in the bottom area of the sandcastle and the decrease S h in the minimum height of the sandcastle, over a period of time; and are the influence factors of the s h change in the bottom area and the height, respectively.

It should be noted that in the real practice, changes are both uncertain of base areas and heights. The sandcastle foundation undergoes the process of waves and tidal effects. The sand at the bottom layer will spread under the effect of erosion, resulting in a reduction in the height of the sandcastle foundation and an increase in its bottom area. The impact of the simplified process on the sandcastle is shown in FIG 1. below:

FIG 2. Simplified model of sandcastle foundation erosion The cubic three-dimensional geometry in the figure represents the original state of the sandcastle foundation, and the dashed line represents the existing state after the sandcastle has been eroded. The increase of the base area and the decrease of the height of the existing state compared with the original state are the quantity of the damage index. Step3. Find the relationship between the damage index over time. We obtain that the sand level  is eroded by the waves and tides for a period of time, and the water level at the new time and ' h w ' n , and the wave current velocity in the x and y directions are 'u and 'v , the water-sand ratio S  p and of the sandcastle foundation. We discretize the time, set the completion time of the h  sandcastle to zero, that is, is the initial time point, and then take the time points at equal 0 t  intervals to draw a scatter plot as shown in the figure.

FIG 3. Damage index over time The diagram illustrates the damage indicator function established and the line connecting the points at equal intervals. It should be shown that the discrete points after point B are almost on the same horizontal line. As a result, it is revealed that the sandcastle is completely damaged, with a corresponding damage index . Based on that, damage factor is defined with coefficient G max being , that is, when , it is considered that the sandcastle has been damaged to the 0.52 0.52G G    max maximum bearing degree. On this basis, we take point A as the critical time point, which refers to the corresponding time to the maximum degree of damage which could bear, and the time corresponding to that point is the duration . T/ day At the same time, we define the duration of any sandcastle foundation constructed from a three- dimensional geometric shape from the stacking to the critical time point as T . The longer the duration, the better the shape corresponds to the sandcastle foundation.

We simulate the damage index and duration of 10 groups of cuboids with different shape 1e under the action of waves and tides. It should be noted that the 10 sets of data we have obtained factors are only the first step in obtaining the global optimal solution. The next step is shown in the next model. The 10 sets of data are shown in the following table:

Shape factor Duration Shape factor Duration 1.0 2.5 3.5 1.2 1.5 2.4 4.0 1.4 2.0 2.1 4.5 2.8 2.5 2 5.0 2.0 3.0 1.8 5.5 2.6

4.4.2 Simulation solution of dynamics equations of elliptic cylinder and sector cylinder

We consider the damage index and duration corresponding to the parameters of the other two common three-dimensional geometric shapes. The detailed data results of the simulation are shown in the appendix.

We define the ratio of the long axis to the short axis of the ellipse as its shape factor, which  is . Based on this, a dynamic equation solving model is established, and the simulation : e a b 2  1 e simulation graph at is shown as follows: 2  Taking the ratio of the radius r of the sector cylinder to the arc length l as the coefficient 3e , we  take the sector cylinder of as an example to make the following simulation: 1 e 3  

FIG 4. Cylinder simulation diagram FIG 5. Sector cylinder simulation diagram

4.5 Geometric Shape Solving Model Based on Discrete Global Optimization

Algorithm

4.5.1 Model Overview

  By solving the dynamic equation of the sandcastle foundation, we can get the duration 3,2,1 Ti i    3,2,1 of sandcastle foundation shape under the control of ei i . However, in order to find the optima  value of iT , we try to establish an optimal three-dimensional geometric model with a Discrete Global Optimization Algorithm as the core. On this basis, we can find the optimal coefficient value   of any of the three shapes, so that the shape we choose has the longest duration. 3,2,1 ei i 

4.5.2 Model establishment and solution

We still take the cuboid as an example. Through simulation, we can obtain the duration under multiple sets of coefficients. In this regard, we use these data to deduce the Discrete Global Optimization Algorithm based on the successive descent method. The specific steps are as follows:

Step1. Successive Descent method to find discrete local minimum points. (1) set the set E as    : \   f e d f e d the Cuboid shape factor selection point, satisfy n if   , let    , cycle this E  R k k step;determine whether is 0 to determine whether to update the  ke discrete local minima, after ,we get the discrete global minima .

Step2. Construct a discrete fill function. Let initialization   -5 , ,2,1 , 10 V V p j n conditions   , , ;     . 1 0.01 r q  0   0 j The constructed discrete fill function is:

1         ,  , , max  0, F e e q r f e f e r     (9) k k q k k  q e e   k k

Step3 .If , the algorithm is terminated, and local r    ke variable can be used as the discrete global minimum, otherwise, the next step is performed.

Step4. If D   , go to step 6, otherwise, go to the next step.

10 Step5. If r  r 2 , then make , , 10 10 q q  0q   10 , go to the step 2, otherwise, let q  q , go to the step2 D  D 0 Step6. Take any direction , so that , enter d  D D D d   the inner loop phase, change the initial value of D , and cycle the corresponding steps. When the parameter r are sufficiently small, it is believed that there is no better local minimum point in the selected point set E .

From the dynamic model, we can get the corresponding duration T for each assignment, and with as the objective function, we optimize it by the algorithm: 1 K T     min , n K f e e R   (10) k k 1 max T  (11) K Similarly to the other two shape models, we can use the Discrete Global Optimization Algorithm to find the maximum T in the duration controlled by the three shape scale as shown in the following table:

Geometric shape shape factor Duration Cuboid 1.46 2.9 1.00 4.8 Elliptic cylinder 3.0 3.7 Sector cylinder  From the data in the above table, we can clearly conclude that when the base area is constant and the ratio of the long axis to the short axis is 1, the sandcastle foundation can last the longest time. We approximate it as a cylinder with a maximum duration of 4.8 days.

5. Optimal water and sand ratio model

5.1 Model Overview

We use the optimal shape model based on the sandcastle foundation dynamics model to obtain the optimal shape of the sandcastle foundation with the longest duration when the water-sand ratio is constant. However, the size of the water-sand ratio will also directly affect the erosion resistance of the sandcastle foundation. We have introduced the equation of the relationship between the water-sand polymerization degree and the water-sand ratio, and at the same time limit the allowed polymerization degree range to obtain a reasonable water-sand ratio Range, and then by solving the model, the optimal water-sand ratio is obtained[2].

5.2 Quantitative model of Water and sand polymerization degree

We consider the aggregation of water and sand, leading to the concept of the degree of water-sand polymerization. We give the definition of the degree of polymerization of water and sand based on the volume change of the water and sand specific gravity before and after polymerization:

1 1   V V    1 2     1 100 % Q    1 2 (12)   V V  1 2     Where, V , V respectively represent the volume of sand and water before mixing; and represent the 1  1 2 2 water absorption coefficient and water solubility coefficient, respectively. We use these two coefficients to express the polymerization ability of water and sand. We simplify the equation with the water-sand n : ratio p   n   1   p          1 2 1 100 % Q    (13)   1 n    p   We use MATLAB to solve this equation and get the relationship curve between the degree of Water and sand polymerization and the ratio of water and sand, as shown in FIG 6.

FIG 6.Degree of convergence of water and sand The degree of water-sand polymerization increases with the increase of water-sand ratio. We must consider not only the relatively large cohesiveness, but also the optimization of erosion resistance, that is, the longest duration. In combination with the actual situation, we choose a two-point interval with a large viscosity range as shown in our figure as our optimization constraint.

5.3 Solving the Model

We use the sandcastle foundation dynamics model in Question 1 as the basis, use the optimal n as a variable proportion of the best shape we selected, and use the initial value of the water-sand ratio p to discretely process the target T in the same way:

S First put into the dynamic equation (1), according to the change of sandcastle foundations and  h , the relationship between the damage index and time is obtained, and the constraint condition is  added:

7.0 .0 85 n   (14) p n equally spaced points: Find the duration table record of p

Water-sand ratio Duration Water-sand ratio Duration 0.70 4.7 0.78 5.1 0.72 4.9 0.80 5.0 0.74 5.2 0.82 4.3 0.76 4.8 0.84 4.2 Using the Discrete Global Optimization Algorithm of the best shape model in Problem 1, we can .0 739 n conclude that when the water-sand ratio is , the longest duration of the sandcastle foundation  p is achieved under the condition of ensuring good shape adhesion.

6.Fuzzy comprehensive evaluation model based on rain erosion resistance

6.1 Model Overview

Aiming at the erosion of sandcastles by waves and tides, we have established some models to obtain the optimal shape of the sandcastle foundation as a cylinder.However, the actual erosion risk facing sandcastles is not limited to the effects of waves and tides. We should also consider the erosion of rainwater.Based on the cuboids, ellipses, and sectors at the optimal shape coefficients obtained in Problem 1, we have further addressed the problem of rain erosion., we define the sandcastle collapse limit coefficient, and comprehensively establish the rain erosion resistance assessment model by comprehensively ability to resist rainwater infiltration and sandcastle structure evacuation ratio. On this basis, an evaluation model of sandcastle anti-wave erosion ability is constructed. Finally, a fuzzy comprehensive evaluation model is established to evaluate the optimal sandcastle shape under the action of waves and rain[3].

6.2 Evaluation model for rain erosion resistance

6.2.1 Establishment of Model

Before establishing a fuzzy comprehensive evaluation model for the optimal shape of the sandcastle foundation, we set up the evaluation model of rain erosion resistance as follows:

First, the sandcastle's ability to resist rainwater infiltration is established as follows[4]:   i 2 i 1 i 2 i 1 (15) F R R R      u a a a Where,   F i 3,2,1 i represents the ability of the cuboid, cylinder and sector cylinder to resist rain  u i Q infiltration. represents the degree of aggregation of the three shapes of gravel, respectively.

  . represents positive definite coefficient. represents the sandcastle i i ni 3,2,1 R n n i      1 1 a p collapse collapse collapse limit coefficients of the three shapes, respectively.

Secondly, the evacuation ratio indicators for establishing the sandcastle structure are as follows:     i = i R Q V V   (16)   2 f DL Where,   V .  represents positive definite coefficient. represents the shear capacity of Ri 3,2,1 i  2 f V sandcastle gravel. represents the shear force on the sand under the rain gravity load. DL Finally, an assessment model for rainwater erosion resistance is established:

i i i i H F n R   (17) 1 u collapse Where,   represents rainwater erosion resistance of the three shapes. H i 3,2,1 i  1

6.2.2 Solution of Model

In order to solve the model, we consulted some literatures and defined below parameters as shown in the following table:

Symbols

Numerical value     10.6， 12.1 ，  1 2 0.125 np     .1,1 24 .1, 56 1 2 3 n n n ， ， collapse collapse collapse V 305 f V 355 DL Then, we obtained the rainwater erosion resistance of cuboids, cylinders, and sectors as shown in the following table:

Geometric shape Numerical value 50.6 cuboid 63.5 cylinder 68.1 thick sector

6.3 Optimal Shape Fuzzy Comprehensive Evaluation Model

6.3.1 Establishment of Model

Based on the evaluation model of sandcastle resistance to rain erosion, we first establish the evaluation model of sandcastle resistance to wave current erosion as follows:

i H T   (18) 2 3 i Where,   represents the resistance to wave current erosion of the three shapes. stands for H i 3,2,1 i   2 3 positive definite coefficient.

It should be noted that, in order to determine whether the cuboid, elliptic cylinder and fan-shaped body are still optimal with the optimal shape coefficient, we have established the optimal shape fuzzy synthesis based on the numerical values of the different capabilities of the three shapes. The evaluation model is as follows:

Step1.Determine membership function. We take the ratio of the ability to resist wave current  erosion or rain erosion to the total shape of the three shapes as the membership, so we establish membership functions as follows:

i H   i H   1 1 1 H 3 (19)  i H 1 1 i  i H   i H   2 2 2 H (20) 3  i H 2 1 i  Step2.Calculate membership table based on membership function. We substitute the values of  the two capabilities of the three shapes into Formula   , calculate the membership table of the 19 , 20 optimal shape, and establish a fuzzy relation matrix.

Step3.Determine the weight of the two capabilities in the optimal evaluation. We have  considered that when our sandcastle faces seawater, tidal erosion and rainwater erosion at the same time, the erosion degree of rainwater on sandcastle is much greater than that of seawater and tide on   7.0,3.0 A  sandcastle. Therefore, we set the weight of the two capabilities in decision making to :

Step4：Calculate comprehensive evaluation results. The calculation formula for the  comprehensive evaluation results is as follows:

(21) B A R  

6.3.2 Solution of Model

In order to solve the model, we have determined the calculation parameters and calculation results by referring to the online information and citing reference parameters:

Symbols

Numerical value 13.44  3     2.5,8.6,6.2 , , T T T 1 2 3

Then, we obtained the anti-wave erosion ability of cuboid, cylinder and fan-shape cylinder as shown in the following table:

Geometric shape Numerical value rectangle 34.94 roundness 91.39 sector 69.89 The membership degrees corresponding to the three shapes according to the membership function are shown in Table 11:

Evaluation index Cuboid Cylinder Sector cylinder Rain erosion resistance 0.278 0.348 0.374 wave current erosion resistance 0.178 0.466 0.356

This determines the fuzzy relation matrix:

0.278 0.348 0.374   R  (22)   0.178 0.466 0.356   7.0,3.0 Since the weight of the project in decision-making is A ,the comprehensive evaluation  obtained is:

  = 0.208 0.430 0.361 B A R   (23) ， ，

It can be seen that the stability of cuboids, cylinders, and fan-shape cylinders under the combined action of wave erosion and rain erosion is 0.208, 0.430, and 0361, respectively. By comparison, we can know that the stability of cylinders under double erosion is the highest.

7. Humidity Prediction Model Based on RBF Neural Network Algorithm

7.1 Model Overviw

Sandcastles are products of mixing sand and water. In order to improve the duration of sandcastles, the most important thing is the humidity of the sandcastle and the protection after the production is completed. After consulting the relevant literature, we know that the adhesive protection after the production is also determined by the humidity of the sandcastle. Therefore, when we know the general trend of humidity, we can make the sandcastle last longer. We selected the RBF neural network algorithm as the prediction network, combined with the daily changing characteristics of the beach temperature as an input factor, and proposed a sandcastle humidity prediction model suitable for better extending the sandcastle duration[5].

7.2 Model Preparation

We take a typical beach, Venice Beach, as an example. The humidity data from August 1 to 3, 2019 was obtained from the U.S. Meteorological Administration. It is worth mentioning that because of the similar sandy conditions and weather conditions of the beach, the Venice Beach we selected is very typical[6]. Index screening:  The humidity of the beach is the result of the combination of many factors, which are closely related to solar radiation, wind, beach temperature, and ground vegetation. We used principal component analysis to find that temperature changes caused by the sun's light intensity had the most significant effect on beach humidity. Therefore, we explore the change of the humidity of the beach under different time and different weather conditions.

Through observation data, we found that there is a clear correlation between the beach environment humidity and beach temperature, specifically: no matter whether it is sunny or cloudy, as the beach temperature changes over time, the humidity will also change accordingly; however, under sunny weather, Humidity changes on the beach are greater than on cloudy days.

In summary, the humidity of the beach is indeed mainly affected by the change of the ambient temperature, and it has a negative correlation with it. We select the ambient temperature at different time periods of the day as the input factor, select 500 input samples, 50 simulated samples, and 50 predicted samples.

7.3 RBF neural network algorithm

The RBF neural network algorithm has strong non-linear fitting property. It not only has good best approximation performance for complex functions, but also has fast convergence speed.   T Assume that the input vector is , n is the number of input samples, , , , X x x nx   1 2    T h X is the output weight vector, m is the number of hidden nodes, d is the offset, , , , W w w w   1 2 n  is the network output, and g is the radial basis function. Gaussian functions are usually used:   2 /   2 exp g X C X C (24)      i i i Where, is the European norm, and C is the i data center in the network. In this case, the output i of the neural network is:

m     h X d w X C     (25) i i 1 i  Through the RBF neural network algorithm, we obtained the humidity change map under sunny and cloudy conditions. Starting from 7:00 am, samples were taken every 30 minutes, as shown in the figure below:

FIG 7. Moderate forecast curves for sunny and cloudy days As can be seen from the figure, we should humidify the glue in a timely manner at 13:30 on a cloudy day and at 13:00 on a sunny day. We know that the glue can maintain its viscosity for at least 8 hours, so the humidity starts to increase to 15:00 sandcastles can be protected before reaching basic stability at 21:00. By predicting the change in humidity, humidity prediction of the sandcastle situation is carried out to ensure the longest lasting time.

8. Sensitivity Analysis

8.1 Sensitivity Analysis of Most Shaped Model Based on Sandcastle Foundation

Dynamics Model

It should be noted that maximum damage coefficients can be selected differently by other people. If the value of is different, the maximum duration corresponding to each shape will change, and the change trend is complex and difficult to determine. Therefore, we need to explore whether there is a stable result (the cylinder has the strongest endurance) for different to prove the stability of the model. Here we continue to determine the stability of the cylinder by continuously taking the value to determine whether the cylinder is still the best shape. The results are as follows:

B(0.96,0) A(0.08,0)

FIG 8. Judging results As shown in the figure, with as the time interval, we take 24 sample points around 0.04     for analysis. Through graphical analysis, when , a cylinder is still the optimal 0.52   0.08， 0.96     shape. When , the optimal shape becomes a fan or cuboid. Therefore, we believe that our 0.08， 0.96     model is stable when it can withstand the maximum damage factor . In other words, our 0.08， 0.96   model is very robust.

8.2 Sensitivity Analysis of Optimal Water-Sand Mixing Model

Based on the introduction of the equation of the relationship between water-sand polymerization degree and water-sand ratio, by limiting the allowable degree of polymerization, we have obtained a reasonable range of water-sand ratio. However, the relationship between the degree of polymerization   , , and the ratio of water to sand is affected by two parameters of   . When the value of   is not accurate, the results of the model could be questionable. Therefore, we continuously adjust the value of  ,   , as shown in FIG 9. Based on this, the robustness of the model is finally judged by calculating the error of the model result.

FIG 9. Degree of polymerization curve As shown in the figure, based on the original coefficients, we increase and decrease the data by 1%  1.56 , 2.86 and 2% respectively (note that its initial parameter     ), so as to obtain the graph of the degree of aggregation-water-sand ratio in five cases. Based on this, we apply Model 2 again and combine the initial results of Model 2 to calculate the error table of the three shapes as follows:

   ,   Cuboid Cylinder Sector cylinder Error/%   1.58， 2.88 2.3 3.9 3.6   1.59， 2.89 4.9 4.9 5.0   1.54， 2.84 3.1 3.3 2.9   1.53， 2.83 3.8 4.8 4.6

 , From the above table, we can observe that when   increases and decreases 1% and 2% respectively, the final error of all shapes is within 5%. Therefore, it shows that our model is more robust  , when   has some errors.

8.3 Sensitivity Analysis of A Fuzzy Comprehensive Evaluation Model Based on the

Ability to Resist Rain Erosion In order to make the fuzzy comprehensive evaluation model valid, we must ensure that the fuzzy comprehensive evaluation index (resistance to rainwater erosion and resistance to wave erosion) is accurate and reliable. In determining the values of the two capabilities, we have introduced three positive definite coefficients to assist the calculation. However, since the values of the three , ,    1 2 3 positive definite coefficients are not very reliable, we continuously adjust the values of the three positive definite coefficients to determine whether the cylinder has always been the optimal shape and thus to judge the stability of the model. The judgment results are as follows:

FIG 10. Stability judgment By observing the figure, we clearly know that when increases to 130% and above, the cylinder  1 is no longer the optimal shape, and the optimal shape is the fan-shape cylinder. When is reduced to  2 75% and below, the cylinder is no longer the optimal shape, and the optimal shape is a cuboid. When fluctuates at 30% of its original value, the cylinder is still the optimal shape. Therefore, we can tell 3 that when the three positive definite coefficients fluctuate within 25% of the original value, the results of our model have not changed much and have shown strong robustness.

8.4 Sensitivity Analysis of Sandcastle warning protection Model

The advantage of the sandcastle humidity prediction model is that it can predict the trend graph of beach humidity in advance and remediate sandcastles in time. If the error between the actual value and the predicted value of the beach humidity does not exceed 10%, we consider that the sandcastle humidity prediction model based on the RBF neural network algorithm is highly reliable.

The simulated was performed using MATLAB. First, we choose the mean square error to be 0.02 and the expansion speed of the radial basis function to be 0.8. Then we input the samples to build the RBF neural network and simulate the model. Finally, the average relative error between the predicted value and the actual value of the beach humidity is 4.32%. The comparison chart between the predicate value and the actual value using ORIGIN fitting is shown in FIG 11, which illustrates that the sandcastle humidity prediction model based on the RBF neural network algorithm can predict the humidity basic trend.

FIG 11. Actual vs. predicted curve

9. Evaluation and Promotion of Model

9.1 Strength and Weakness

9.1.1 Strengths

Have fully considered the erosion of sandcastles caused by waves and tidal effects and established a sand-bearing capability indicator. Considering the change in the bottom area and height of the sandcastle foundation during the movement, we create a sandcastle damage index to quantify the sandcastle damage reasonably.

Based on some solutions obtained from the sandcastle dynamics simulation, the discrete global  optimization method based on the successive descent has been used to obtain the global optimal solution.

The equation of the relationship between water-sand polymerization degree and water-sand ratio is  introduced.The reasonable water-sand ratio range is obtained by limiting the allowable polymerization degree range.

On the issue of rain erosion, we put forward the collapse limit coefficient of sandcastle specifically.  Considering the ability of resisting rain infiltration and the evacuation ratio of sandcastle structure comprehensively, we established an evaluation model to determine the stability of the selected shape. Because the RBF neural network overcomes slow convergence and local minimization of the other neural network algorithms, when designing the sandcastle early warming protection mechanism, we have chosen the RBF neural network model to predict when to apply adhesive to enhance the duration of sandcastle When using the RBF neural network algorithm, we have selected input factors based on the changing characteristics of the ambient temperature to accurately and reasonably predict the daily humidity change trend, thereby effectively humidity prediction the sandcastle and extending its duration.

9.1.2 Weaknesses

We did not consider three-dimensional shapes other than cuboids, elliptical cylinders, and sector cylinders, and only selected the three types of shapes most commonly used in sandcastles. We only have considered sandcastles under various water erosion conditions, but not the impact of other factors in nature. The accuracy of some selected coefficients from other literatures may affect some final conclusions. We only have considered the situation when the waves and tides are relatively calm. When the waves and tides significantly fluctuate, the sandcastle might not collapse in the way we have expected.

9.2 Promotion

Considering the impact of water erosion on sandcastle alone, our model is very robust. Therefore, our model is suitable when the quantitative factors of water erosion fluctuate within a certain range. However, under objective natural conditions, the factors affecting the stability of sandcastles may not be limited to water erosion (such as wind erosion, light, etc.). Therefore, our strategy may need to be slightly modified to cope with the sandcastle foundation under different natural and objective conditions. Further, based on the original model, we tried to establish the basic dynamics equation of the sandcastle considering the combined effects of wind erosion and light, making the solution of the problem more practical. In addition, we believe that the final choice of the cylinder is the most stable of the three proposed shapes, but the problem is that the shape is diverse and there is no guarantee that the cylinder will still be the best of all shapes. Therefore, it is necessary to solve the problem of limited shape being considered.

We have two potential solutions to address that only three shapes have been investigated: 1. Perform cluster analysis on multiple shapes to find more sandcastle foundations that are applicable to actual situations. 2. Introduce the proportion of base area and height, have more shapes under consideration and find out the best three-dimensional aspect ratio of each shape.

10. Conclusions

A detailed strategy to extend the duration of sandcastle foundation was provided in this paper. Firstly, the most stable shape of the sandcastle which was affected by both of the wave and tide was found to be the cylinder. It showed the highest resistance to the wave current erosion among all the considered shapes, according to the optimal shape model based on the dynamics equation of sandcastle foundation. Secondly, the optimum water-sand ratio was worked out to be 0.32 by taking the water- sand polymerization degree into account. Then, the cylinder was confirmed to be the most stable shape by fuzzy comprehensive evaluation, and the rain erosion resistance and resistance to wave current erosion of the sandcastle were also taken into account. Finally, an humidity prediction model of sandcastle was proposed based on RBF neural network, and the daily humidity trend was predicted accurately by the model. When the predicted humidity reached its limit, adhesive should be used in time to keep the bonding effect and stabilize the sandcastle foundation.

Memo

TO:Fun in the Sun Topic: Teach you how to build the longest-lasting sandcastle Dear Vacation Magazine Editor： In recent years, the sandcastle related art works have become increasingly popular. After the creation of great sandcastle art works, how to preserve these art works for a long time becomes an obstacle to promoting this type of activities. Our team has developed a complete sandcastle humidity prediction strategy to achieve the purpose of extending the duration of sandcastles. We appreciate this opportunity to introduce you to our strategy.

The most stable shape of a sandcastle under the action of sea waves and tides: In general, the most durable sandcastle can be piled with the optimal size ratio. These sandcastle shapes have the longest duration: the cuboid with an aspect ratio of 1.46, the elliptical cylinder with an aspect ratio of 1.00, and the fan-shape cylinder with a radius and arc length ratio of A.

The best mixing ratio of water and sand: sandcastles are products of the mixture of sand and water. When the water and sand ratio is 0.739, the sandcastle has the longest duration.

The most stable shape choice for rainy days: Rainy days are also a huge threat for sandcastles. It has been proven that the cylinder is the most stable and longest lasting sandcastle shape.

Measures to extend the duration of the sandcastle: The sandcastles cannot last long without proper humidity. We have found the lowest humidity on sunny and cloudy days happens at 13: 00-13: 30 in the afternoon. Adhesive is recommended to be used to enhance the sandcastle duration during this time period with low humidity.

The above is the optimal sandcastle shape and humidity prediction system that we have proposed. We are eager to help you build the longest lasting sandcastles. If you have any questions about our solution, please feel free to contact us. Our team members are willing to solve any questions you have.

Regards，

March 9 2020

Appendix

Shape factor Duration Shape factor Duration 1.0 4.8 3.5 3 1.5 3.4 4.0 4.6 2.0 2.5 4.5 4.7 2.5 4 5.0 2.0 3.0 4.2 5.5 3.6

Shape factor Duration Shape factor Duration 0.1 0.6 3.5 3.2   0.2 0.7 3.6 2.8  

0.8 0.3 3.7 2.9  

0.9 0.4 2 3  

0.5 1.8 3.5  
