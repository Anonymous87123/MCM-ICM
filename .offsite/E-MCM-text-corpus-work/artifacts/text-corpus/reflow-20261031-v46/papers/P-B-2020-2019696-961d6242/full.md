# P-B-2020-2019696-961d6242

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2020

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
2019696

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Optimal 3D Sandcastle Shape under Erosion

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Waves, tides and rainfall could erode the foundation of sandcastle. We used the fluid-structure interaction theory, considering the characteristics of sand, establishes sandcastle-erosion model and sandcastle-rain-erosion model, and solved them based on the genetic algorithm, multi-step design, iterative calculation, data analysis and optimization, finally confirmed the optimal three-dimensional geometry of sandcastle to resist erosion under different influence factors.

<!-- b000010 | prose | pages [1] -->
The effect of sea water on sandcastle is categorized as two modes: waves and tides. We study the simplified model of flow-solid interaction. The sand foundation is cut off by the crashing of waves layer by layer, while the tide rises slowly to immerse the sandcastle. Sand layer falls out of sandcastle when it is saturated with water which reduces cohesion between sand grains.

<!-- b000011 | prose | pages [1] -->
As for problem 1, it is referred that resistance to erosion reaches its maximum when the water-faced surface is smooth.[4] Thus, we take frustum of a cone (including cylinder but not cone, for castle will be built above it) as an initial research object, to investigate the value of radius of the bottom 𝑅𝑅, radius of the top 𝑟𝑟 and height 𝐻𝐻 to maximum remaining proportion of foundation 𝛼𝛼 in the same amount of time when initial volume 𝑉𝑉0 = 0.2𝑚𝑚3. Partial derivatives and genetic algorithms are used to obtain the maximum remaining proportion 𝛼𝛼, which is 62.4%, when 𝑹𝑹= 𝟎𝟎. 𝟔𝟔𝟔𝟔𝟔𝟔, 𝒓𝒓= 𝟎𝟎. 𝟐𝟐𝟐𝟐𝟐𝟐, 𝑯𝑯= 𝟎𝟎. 𝟑𝟑𝟑𝟑𝟑𝟑. For any fixed volume of sand, the optimal shape to resist seawater erosion is a frustum of a cone maintaining the ratio of the above 𝑹𝑹, 𝒓𝒓 and 𝑯𝑯 values. As the velocity and flux of the water-faced surface is bigger, more force is applied on water-faced surface, the geometry is optimized as a frustum of an ellipsoidal cone to maximum its effectiveness of resistance to erosion.

<!-- b000012 | prose | pages [1] -->
As for problem 2, relationship between water-to-sand proportion 𝛽𝛽 and the thickness of sand layers cut by waves is established. First assume the shape of sandcastle is given by problem 1, regard 𝛽𝛽 as a variable and solve the value of 𝛽𝛽 when 𝛼𝛼 reaches its maximum. Currently when 𝛼𝛼𝑚𝑚𝑚𝑚𝑚𝑚= 65.0%, 𝛽𝛽= 22%. Next, as 𝛽𝛽 is correlated to the shape of optimal geometry, based on problem 1 and relationship between the length cut under erosion and the rate of water absorption saturation to solve the value of 𝑅𝑅, 𝑟𝑟, 𝐻𝐻, 𝛽𝛽 when 𝛼𝛼 reaches its maximum. The result is 𝑅𝑅= 0.58𝑚𝑚, 𝑟𝑟= 0.23𝑚𝑚, 𝐻𝐻= 0.37𝑚𝑚, 𝛽𝛽= 24% when 𝛼𝛼 reaches its maximum 𝛼𝛼𝑚𝑚𝑚𝑚𝑚𝑚= 68.6%. Therefore, the optimal water-to-sand proportional is 24%.

<!-- b000013 | prose | pages [1] -->
Problem 3 is discussed in two cases: sandcastle is affected by both seawater and rainfall and sandcastle is only affected by rainfall. In the first case, the optimal geometry in problem 1 remains 𝛼𝛼= 55.7% after erosion, reducing a volume of 6.7% compared with not affected by rainfall. The geometry model is improved that 𝑅𝑅= 0.52𝑚𝑚, 𝑟𝑟= 0.16𝑚𝑚, 𝐻𝐻= 0.50𝑚𝑚, when 𝛼𝛼 reaches its maximum 𝛼𝛼𝑚𝑚𝑚𝑚𝑚𝑚= 59.2%. In the second case, the optimal geometry in problem 1 remains 𝛼𝛼= 92.6% after erosion. As 𝐻𝐻 increases, 𝛼𝛼 increases. Thus, in both cases, optimal geometry in problem 1 is not optimal in problem 3.

<!-- b000014 | prose | pages [1] -->
Four advice is given in problem 4: increase initial volume; build sandcastle away from the sea; add adhesive into sand-water mixture; build a sand wall around the sandcastle.

<!-- b000015 | prose | pages [1] -->
Finally, sensitivity analysis of coefficient of length cutting 𝜆𝜆𝑐𝑐, coefficient of saturated water absorption 𝜆𝜆𝑠𝑠, initial volume 𝑉𝑉0 is given.

<!-- b000016 | keywords | pages [1] -->
Key Words: 3D Sandcastle Model; Fluid-Structure Interaction; Optimizing Model;

<!-- b000017 | prose | pages [1] -->
关注数学模型

<!-- b000018 | furniture | pages [1] -->
2

<!-- b000019 | furniture | pages [1] -->
MATHmodels

<!-- b000020 | furniture | pages [1] -->
获取更多资讯

<!-- b000021 | furniture | pages [2] -->
Team # 2019696                                                                  Page 1 of 27

<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
1

<!-- b000024 | contents | pages [2] -->
Introduction ................................................................................................................................... 1

<!-- b000025 | contents | pages [2] -->
1.1

<!-- b000026 | contents | pages [2] -->
Background ........................................................................................................................... 1

<!-- b000027 | contents | pages [2] -->
1.2

<!-- b000028 | contents | pages [2] -->
Restatement of the Problem .................................................................................................. 1

<!-- b000029 | contents | pages [2] -->
2

<!-- b000030 | contents | pages [2] -->
Analysis of the problem ................................................................................................................ 1

<!-- b000031 | contents | pages [2] -->
2.1

<!-- b000032 | contents | pages [2] -->
Literature Review ................................................................................................................. 1

<!-- b000033 | contents | pages [2] -->
2.2

<!-- b000034 | contents | pages [2] -->
Problem Analysis .................................................................................................................. 2

<!-- b000035 | contents | pages [2] -->
3

<!-- b000036 | contents | pages [2] -->
Assumptions and Justifications .................................................................................................... 3

<!-- b000037 | contents | pages [2] -->
4

<!-- b000038 | contents | pages [2] -->
Notations......................................................................................................................................... 4

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
Model and Solution ....................................................................................................................... 5

<!-- b000041 | contents | pages [2] -->
5.1

<!-- b000042 | contents | pages [2] -->
Sandcastle-Erosion Model .................................................................................................... 5

<!-- b000043 | contents | pages [2] -->
5.2

<!-- b000044 | contents | pages [2] -->
Solution to Optimal Water-to-Sand Mixture Proportion .................................................... 12

<!-- b000045 | contents | pages [2] -->
5.3

<!-- b000046 | contents | pages [2] -->
Sandcastle-Rain-Erosion Model ......................................................................................... 14

<!-- b000047 | contents | pages [2] -->
6

<!-- b000048 | contents | pages [2] -->
Advice on Building a Sandcastle ................................................................................................ 17

<!-- b000049 | contents | pages [2] -->
7

<!-- b000050 | contents | pages [2] -->
Sensitivity Analysis ...................................................................................................................... 18

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
Strengths and Weakness ............................................................................................................. 20

<!-- b000053 | contents | pages [2] -->
8.1

<!-- b000054 | contents | pages [2] -->
Strengths ............................................................................................................................. 20

<!-- b000055 | contents | pages [2] -->
8.2

<!-- b000056 | contents | pages [2] -->
Weakness ............................................................................................................................ 20

<!-- b000057 | contents | pages [2] -->
Article for Fun in the Sun ................................................................................................................. 21

<!-- b000058 | contents | pages [2] -->
References ........................................................................................................................................... 23

<!-- b000059 | contents | pages [2] -->
Appendix ............................................................................................................................................. 24

<!-- b000060 | contents | pages [2] -->
关注数学模型

<!-- b000061 | furniture | pages [2] -->
2

<!-- b000062 | furniture | pages [2] -->
MATHmodels

<!-- b000063 | furniture | pages [2] -->
获取更多资讯

<!-- b000064 | furniture | pages [3] -->
Team # 2019696                                                                  Page 1 of 27

<!-- b000065 | heading | pages [3] -->
1 Introduction

<!-- b000066 | heading | pages [3] -->
1.1 Background

<!-- b000067 | prose | pages [3] -->
Beach is a paradise for children, while sandcastle is an indispensable part of it. Various kinds of sandcastles are constructed, decorated with roofs, turrets, windows and steps. Every child who played on a beach knows that dry sand could only loosely pile up like a comicalness, and will collapse while mixed up with too much water. Thus, what is the golden ratio of sand and water that will keep the sandcastle standing? Naturally, here comes the question of how to make the sandcastle survive longer under the erosion of waves and tides. This article aims to discuss “perfect sandcastle” in consideration of factors as waves, tides and rainfall.

<!-- b000068 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000069 | prose | pages [3] -->
Considering the background information and restricted conditions identified in the problem statement to address the following issues:

<!-- b000070 | prose | pages [3] -->
 Problem 1. On the premise of ensuring the use of sand with the same kind of material and same water-to-sand proportion with similar quality of sand, establish a mathematical model to determine the geometry that mostly remains intact for the longest time under the influence of waves and tides.

<!-- b000071 | prose | pages [3] -->
 Problem 2. Use the same model in Problem1 to solve the most suitable water-to-sand proportion to make foundation remain longer.

<!-- b000072 | prose | pages [3] -->
 Problem 3. Change the mathematical model of the first question to determine whether the geometry solved above is still optimal when rainfall conditions are considered.

<!-- b000073 | prose | pages [3] -->
 Problem 4. Give advice on how to make sandcastles last longer.

<!-- b000074 | heading | pages [3] -->
2 Analysis of the problem

<!-- b000075 | heading | pages [3] -->
2.1 Literature Review

<!-- b000076 | prose | pages [3] -->
The problem with building a sandcastle for the longest duration is essentially one of wet granular materials. Torsten, G. and David, M. modelled and measured the cohesion in wet granular materials by using a Cohesive Discrete Element Method (CDEM)[1]. Nowak, S., Samadani, A. and Kudrolli, A. had taken a model called frictionless liquid-bridge model to observe dependence of the stability angle on some paraments of the system, such as system size

<!-- b000077 | prose | pages [3, 4] -->
关注数学模型 and surface tension[2].

<!-- b000078 | furniture | pages [3] -->
2

<!-- b000079 | furniture | pages [3] -->
MATHmodels

<!-- b000080 | furniture | pages [3] -->
获取更多资讯

<!-- b000081 | furniture | pages [4] -->
Team # 2019696                                                                  Page 2 of 27

<!-- b000083 | prose | pages [4] -->
As for the physical property of granular media mixed with wetting liquid, Hornbaker, D., Albert, R., Albert, I. et al. reached that nanometer-scale layers of liquid on millimeter-scaled grains could sharply change the properties of granular media, which could even cause new physical phenomena not found in dry materials[3]. The ratio of raw materials is important in industrial production, because the ratio of raw materials will determine the physical properties of the product. Emiroğlu, M., Yalama, A., & Erdoğdu, Y. proved by experiment that there is a great difference in the physical properties of ready-mixed clay plaster produced in different clay/sand proportions [4].

<!-- b000084 | prose | pages [4] -->
For the consideration of the bond between sand grain and water in a certain proportion, Kudrolli, A. states that the inherit cohesion is highly relevant with volume fractions [5], which could explain the importance of water-to-sand ratio in the process of building a sandcastle. As to the reason that causes the sandcastle to collapse, Thomas C. Halsey and Alex J. Levine states that the failure point occurs in the majority of the sandpile rather than on the surface [6], which mainly points to the dry sandpile. Finally, Pakpour, M., Habibi, M., Møller, P., and Bonn, D.  gave a model on investigating the maximum height of wet sand column while considering the stability of sandcastle [7].

<!-- b000085 | heading | pages [4] -->
2.2 Problem Analysis

<!-- b000086 | prose | pages [4] -->
fluid-structure interaction is a branch of mechanics theory that studies the interaction between fluids and solids. We simplify the model involved in this theory and only study the flow to solid one-way interaction.

<!-- b000087 | prose | pages [4] -->
Problem 1: The goal of problem 1 is to establish the geometry of the sandcastle with the longest duration under the erosion of waves and tides, with the constraints that the sandcastles have 1) roughly same volume, 2) the same raw material, 3) the same sand-to-water ratio and 4) roughly the same distance from the water source (that is, the distance from the erosion source). In order to simplify and solve problem 1, a sandcastle-erosion model with geometric parameters as independent variables is established to find the most defensively geometry.

<!-- b000088 | prose | pages [4] -->
Problem 2: The goal of problem 2 is to investigate the optimal sand-to-water mixture proportion to make the sandcastle most defensible. In addition to the constraints of problem 1, and regardless of the impact of changes in the geometry of the sandcastle, problem 2 requires that raw materials of the sandcastle could be nothing but sand and water. In order to solve problem 2, the sandcastle-erosion model based on problem 1 is changed, which takes the sand-to-water mixture proportion as independent variable. The algorithm of solving the optimization model is used to solve the optimal value of the sand-to-water mixture proportion.

<!-- b000089 | prose | pages [4, 5] -->
关注数学模型 Problem 3: The goal of problem 3 is to investigate the geometry of the sandcastle that could remain longest time under the erosion of not only waves and tides, but the effect of rainfall as well. The solution of problem 3 is to establish a sandcastle-rain-erosion model based on the sandcastle-erosion model of problem 1, adding rainfall factors besides the influence of waves and tides. Problem 3 could be solved by using same algorithm in problem 1.

<!-- b000090 | furniture | pages [4] -->
2

<!-- b000091 | furniture | pages [4] -->
MATHmodels

<!-- b000092 | furniture | pages [4] -->
获取更多资讯

<!-- b000093 | furniture | pages [5] -->
Team # 2019696                                                                  Page 3 of 27

<!-- b000095 | prose | pages [5] -->
Problem 4: Problem 4 asks for advice to increase the survival time of sandcastles. The solution method is to discuss the model results of problems 1-3 to obtain useful advice. Besides, theoretical analysis based on literature, sandcastle structures and common sense will also be conducted in this article.

<!-- b000096 | heading | pages [5] -->
3 Assumptions and Justifications

<!-- b000097 | prose | pages [5] -->
• The initial volume of the sandcastle before the erosion process began was large enough that all the sandcastles of different shapes which we investigate have positive volumes at the end of the observation period. If there are sandcastles with zero volume (that is, the sandcastle is completely destroyed) after the erosion process, or all sandcastles are in volume of zero after the erosion process, it is impossible to compare the influence of shape and geometric parameters on the stability of sandcastles in the modelling process.

<!-- b000098 | prose | pages [5] -->
• Sand falls out of the sandcastle simply because the sand is saturated with water and a tiny external force is applied on the sand. When there is no liquid between the sand grains, cohesion is negligible, which explains why dry sand could not construct sandcastles. At small volume fractions, liquid bridges which induce cohesion between grains are formed. At higher volume fractions, large contiguous wet clusters form. However, when the volume fractions exceed the threshold value, cohesion becomes negligible again [5], which is the main reason that causes sand fall out.

<!-- b000099 | prose | pages [5] -->
• The crash of the waves causes the sand to absorb water more quickly than it would if it were simply immersed in seawater. Since the initial velocity is not zero when the waves hit the outer surface of the sandcastle, while some of the water carried in the waves will penetrate into the sandcastle, the crashing process can be regarded as the speed of water penetration into the sandcastle is accelerated.

<!-- b000100 | prose | pages [5] -->
• The effectiveness of seawater erosion on sandcastle is not correlated with time. That is, the volume reduction caused by the part of water penetrating into the sandcastle caused by waves is ignored. Compared with sandcastle, the volume of sea water is extremely massive, so the loss of water caused by each wave crash could be ignored, which explains the effectiveness of seawater

<!-- b000101 | prose | pages [5, 6] -->
关注数学模型 erosion on sandcastle is not affected by time.

<!-- b000102 | furniture | pages [5] -->
2

<!-- b000103 | furniture | pages [5] -->
MATHmodels

<!-- b000104 | furniture | pages [5] -->
获取更多资讯

<!-- b000105 | furniture | pages [6] -->
Team # 2019696                                                                  Page 4 of 27

<!-- b000107 | prose | pages [6] -->
• Ignore crash effects caused by tide on sandcastle. According to the tidal conditions in different sea areas around the world [8] sea surfaces in different sea areas rises and falls at a relatively steady and slow speed. Only the penetrating influence caused by the tide on the sandcastle is considered.

<!-- b000108 | prose | pages [6] -->
• Ignore the evaporation of water in the sand. As the sand-to-water mixture proportion plays an important role under lots of circumstances, not considering the evaporation can achieve goals more directly by removing interference.

<!-- b000109 | prose | pages [6] -->
•The sandcastle stands on the beach which is horizontal. If the sandcastle stands on a slope, calculations like saturated time for water-positive surface and top surface will become too much complicated, which causes unnecessary trouble when solving our core question.

<!-- b000110 | heading | pages [6] -->
4 Notations

<!-- b000111 | prose | pages [6] -->
Definitions Descriptions Remaining proportion of the sandcastle 𝛼𝛼 Water-to-sand mixture proportion 𝛽𝛽 𝜆𝜆𝑐𝑐 Coefficient of length cutting Coefficient of saturated water absorption 𝜆𝜆𝑠𝑠 𝜈𝜈𝑡𝑡 Velocity that tide rises and falls Maximum height of tide ℎ𝑒𝑒 Height of tide ℎ𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑙𝑙𝑖𝑖 Length cut in different conditions Time when sea level reaches its peak at the first time 𝑡𝑡𝑒𝑒 𝑡𝑡𝑓𝑓 Time when sea level reaches the top of sandcastle at the first time Cohesion between sand grains 𝐹𝐹 Height of sandcastle 𝐻𝐻 𝐿𝐿𝑝𝑝 Saturated water absorption at the bottom of water-position surface Saturated water absorption at the bottom of water-negative surface 𝐿𝐿𝑛𝑛 𝐿𝐿𝑡𝑡 Saturated water absorption at the top surface Initial volume of the sandcastle 𝑉𝑉0 Radius of top surface of a frustum-shaped sandcastle 𝑟𝑟 𝑅𝑅 Radius of bottom surface of a frustum-shaped sandcastle Constants 𝑘𝑘1, 𝑘𝑘2, 𝑘𝑘3

<!-- b000112 | prose | pages [6] -->
关注数学模型

<!-- b000113 | furniture | pages [6] -->
2

<!-- b000114 | furniture | pages [6] -->
MATHmodels

<!-- b000115 | furniture | pages [6] -->
获取更多资讯

<!-- b000116 | furniture | pages [7] -->
Team # 2019696                                                                  Page 5 of 27

<!-- b000117 | heading | pages [7] -->
5 Model and Solution

<!-- b000118 | heading | pages [7] -->
5.1 Sandcastle-Erosion Model

<!-- b000119 | prose | pages [7] -->
It is referred that resistance to erosion reaches its maximum when the water-faced surface is smooth[4]. That means the shape with corner angle is easier to be eroded than cylinders. Thus, we take frustum of a cone (including cylinder but not cone, for castle will be built) as an initial research object. In this section, the sandcastle-erosion model is discussed in detail and a concrete calculation method to evaluate the stability of sandcastles is proposed to obtain the optimal geometry required in problem 1.

<!-- b000120 | prose | pages [7] -->
In order to more concisely and accurately quantify the effect of erosion on the sandcastle, the following two-dimensional surfaces of sandcastle are defined:

<!-- b000121 | prose | pages [7] -->
Water-positive surface: the surface of the sandcastle facing the sea, that is, the curved surface of the sandcastle that is visible from the direction of the sea.

<!-- b000122 | prose | pages [7] -->
Water-positive section: the maximum section of sandcastle visible from the direction of the sea.

<!-- b000123 | prose | pages [7] -->
Water-negative surface: the surface of the sandcastle back to the sea, that is, the curved surface of the sandcastle that is invisible from the direction of the sea.

<!-- b000124 | prose | pages [7] -->
Top surface: the surface that is parallel to the bottom surface.

<!-- b000125 | prose | pages [7] -->
Whole surface: the surface that involves water-positive surface, water-negative surface and top surface.

<!-- b000126 | caption | pages [7] -->
Figure 1 The sketch of each position（the yellow part）

<!-- b000127 | prose | pages [7, 8] -->
关注数学模型 According to the tidal data of various of places in the world [8], the variation of tide height is rather obvious in 24 hours. In order to study the influence of tidal change on sandcastle, the following model takes the tidal data of Dandong, China on March 6, 2020 as an example for analysis. Meanwhile, in order to avoid the excessive impact of the tide on the sandcastle, which was immersed in the sea for most of the observation time, the model choose to build the sandcastle at a height of 200cm, and the maximum height of the sandcastle is required to be less than 1m, so as to reflect the erosion effect of both tide and waves.

<!-- b000128 | furniture | pages [7] -->
2

<!-- b000129 | furniture | pages [7] -->
MATHmodels

<!-- b000130 | furniture | pages [7] -->
获取更多资讯

<!-- b000131 | furniture | pages [8] -->
Team # 2019696                                                                  Page 6 of 27

<!-- b000133 | prose | pages [8] -->
The goal of problem 1 is to seek the sandcastle that has the longest duration under the erosion of waves and tides. The duration is defined as the time it takes for the volume of the sandcastle to decrease (the surface sand falls off the main body) to a certain value, which is equivalent to the maximum volume retained by the sandcastle under the same erosion of waves and tides.

<!-- b000134 | caption | pages [8] -->
Figure 2 Tidal data from Dandong, China on March 6, 2020

<!-- b000135 | prose | pages [8] -->
Assuming that the wave height is small enough, so when the sea level is less than 200 centimeters, it can be regarded as sandcastle is not affected by the tide and waves, as sandcastle is built at the height of 200 centimeters. According to the tidal table, the erosion condition of sandcastle is studied only for four hours, from 18:00 to 24:00. It has also assumed that the initial volume 𝑉𝑉0 of the sandcastle is large enough that the all sandcastles can maintain a positive volume after four hours of erosion, while the roughly shape of sandcastle remains largely unchanged after the erosion.

<!-- b000136 | prose | pages [8] -->
Due to the slow rising speed of the tide (approximately 50𝑐𝑐𝑐𝑐/ℎ), the crashing impact of the tide on the sandcastle is neglected, the immersing impact of the tide on the sandcastle is merely considered. In contrast to the long impacting period of tides, waves crash rather rapidly (approximately 10 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡/𝑚𝑚𝑚𝑚𝑚𝑚), which is regarded as a continuous impact on the sandcastle. Since the wave height is assumed to be small relative to the height of the sandcastle, while the

<!-- b000137 | prose | pages [8, 9] -->
关注数学模型 waves hit the sandcastle continuously and the sea water rises at a constant speed, the time length that every part of water-position surface was impacted remains same.

<!-- b000138 | furniture | pages [8] -->
2

<!-- b000139 | furniture | pages [8] -->
MATHmodels

<!-- b000140 | furniture | pages [8] -->
获取更多资讯

<!-- b000141 | furniture | pages [9] -->
Team # 2019696                                                                  Page 7 of 27

<!-- b000143 | prose | pages [9] -->
Assume 𝑡𝑡0 represents the crashing time length of waves of the same height on water-positive surface at each point as the sea surface rises at a constant speed. In a fixed interval of time 𝑡𝑡0, the length cut by waves from water-positive sand surface stands for 𝑙𝑙1, while 𝑙𝑙1 is in proportion to the ratio of the area of water-positive surface 𝑆𝑆1 and the area of water-positive section 𝑆𝑆1′, that is

<!-- b000144 | prose | pages [9] -->
(1) Among them, 𝜆𝜆𝑐𝑐 represents coefficient of length cutting, which is corelated to water-to-sand mixture proportion and considered a constant in problem 1.

<!-- b000145 | prose | pages [9] -->
In order to simply the calculation, it is assumed that after the sand on the water-position surface was crashed, part of the sand should have fallen out but remains saturated slightly attaching to the majority of sandcastle.

<!-- b000146 | prose | pages [9] -->
The following discussion is based on the initial height of 200 centimeters, while initial time is based on the moment sea level reaches initial height. As the tide rises and falls at a constant speed, the height of tide ℎ𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 satisfies:

<!-- b000147 | prose | pages [9] -->
(2)

<!-- b000148 | prose | pages [9] -->
Among them, 𝜈𝜈𝑡𝑡 represents the velocity that tide rises and falls, ℎ𝑒𝑒 represents maximum height of tides, 𝑡𝑡𝑒𝑒 represents the time at which the sea level reaches its peak.

<!-- b000149 | prose | pages [9] -->
In unit interval, the length that immersion causes the water to penetrate vertically from the whole surface of the sand stands for 𝑙𝑙2, that is, (3)

<!-- b000150 | prose | pages [9] -->
Among them, 𝜆𝜆𝑠𝑠 represents coefficient of saturated water absorption, which is corelated to water-to-sand mixture proportion and considered a constant in problem 1.

<!-- b000151 | prose | pages [9] -->
𝜆𝜆𝑐𝑐= 9.8 × 10−2, 𝜆𝜆𝑠𝑠= 7.0 × 10−6 is assumed[7]. The following is a schematic of the reduction of sandcastle:

<!-- b000152 | prose | pages [9, 10] -->
关注数学模型  The outermost green section is the part that is saturated with the increase of the tide height.

<!-- b000153 | furniture | pages [9] -->
2

<!-- b000154 | furniture | pages [9] -->
MATHmodels

<!-- b000155 | furniture | pages [9] -->
获取更多资讯

<!-- b000156 | furniture | pages [10] -->
Team # 2019696                                                                  Page 8 of 27

<!-- b000157 | caption | pages [10] -->
Figure 3 The schematic of the reduction of sandcastle

<!-- b000159 | prose | pages [10] -->
Since the water absorption of different part reaches saturation at the same rate, the lower part has a rather longer time interval to contact with the seawater and absorbs more, while the upper part absorbs less.

<!-- b000160 | prose | pages [10] -->
 The purple section is the sand layer on the water-positive surface cut by the waves. Since the waves are continuously having an impact on the sandcastle is assumed, and the wave height is rather small, while sea water is rising slowly at a constant speed, the length of the upper and lower parts cut by the waves remains approximately same.

<!-- b000161 | prose | pages [10] -->
 Considering that the sand piles formed at the same volume are of different heights and the maximum height of rising tide ℎ𝑒𝑒 is fixed, thus, if different shapes are located in the same position, the sandcastle with a small height will be submerged. The blue section represents the length of water absorption saturation. As the whole sandcastle is immersed in the sea, the water absorption length of each surface of the sandcastle is the same.

<!-- b000162 | prose | pages [10] -->
 The green section of the inner part is the saturated water absorption length of the sandcastle at falling tide, while the purple section of the inner part is the length of the sandcastle cut by waves during the falling tide.  The red part is the remaining sandcastle after a whole period of rising and falling tide.

<!-- b000163 | prose | pages [10] -->
The segmentation process is shown as follows

<!-- b000164 | prose | pages [10, 11] -->
关注数学模型 Assume 𝑡𝑡𝑓𝑓 stands for time that sea level rises just above the sandcastle (the rise of height equals to 𝐻𝐻, where 𝐻𝐻 represents the height of the sandcastle).  Step 1: From time 𝑡𝑡= 0 to 𝑡𝑡= 𝑡𝑡𝑓𝑓, when the sea level rises from exactly touching the bottom of the sandcastle to exactly reaching the top of the sandcastle, the length of water-positive surface cut by waves add on the length that the lowest level absorbs water to reach saturation could be described as

<!-- b000165 | furniture | pages [10] -->
2

<!-- b000166 | furniture | pages [10] -->
MATHmodels

<!-- b000167 | furniture | pages [10] -->
获取更多资讯

<!-- b000168 | furniture | pages [11] -->
Team # 2019696                                                                  Page 9 of 27

<!-- b000169 | caption | pages [11] -->
Figure 4 The segmentation process

<!-- b000171 | prose | pages [11] -->
(4)

<!-- b000172 | prose | pages [11] -->
 Step 2 (completely immersed): from time 𝑡𝑡= 𝑡𝑡𝑓𝑓 to 𝑡𝑡= 𝑡𝑡𝑒𝑒, when the sea level rises from the top of the sandcastle to the top water level, the length that the lowest level of water-position surface absorbs water to reach saturation could be described as

<!-- b000173 | prose | pages [11] -->
(5)

<!-- b000174 | prose | pages [11] -->
 Step 3 (completely immersed): from time 𝑡𝑡= 𝑡𝑡𝑒𝑒 to 𝑡𝑡= 𝑡𝑡𝑒𝑒+ (𝑡𝑡𝑒𝑒−𝑡𝑡𝑓𝑓), when the sea level falls from the top water level to the top of the sandcastle, the length that the lowest level of water-position surface absorbs water to reach saturation could be described as

<!-- b000175 | prose | pages [11] -->
(6)

<!-- b000176 | prose | pages [11] -->
 Step 4: from time 𝑡𝑡= 𝑡𝑡𝑒𝑒+ (𝑡𝑡𝑒𝑒−𝑡𝑡𝑓𝑓) to 𝑡𝑡= 2𝑡𝑡𝑒𝑒, when the sea level falls from the top of the sandcastle to completely have no contact with sandcastle, the length of water-positive surface cut by waves add on the length that the lowest level absorbs water to reach saturation could be described as

<!-- b000177 | prose | pages [11] -->
(7)

<!-- b000178 | prose | pages [11, 12] -->
关注数学模型 In the whole process, the saturated water absorption length 𝐿𝐿𝑝𝑝 at the bottom of the water-positive surface is the sum of equation (4)~(7), that is:

<!-- b000179 | furniture | pages [11] -->
2

<!-- b000180 | furniture | pages [11] -->
MATHmodels

<!-- b000181 | furniture | pages [11] -->
获取更多资讯

<!-- b000182 | furniture | pages [12] -->
Team # 2019696                                                                  Page 10 of 27

<!-- b000184 | prose | pages [12] -->
(8)

<!-- b000185 | prose | pages [12] -->
In a similar way, the saturated water absorption length 𝐿𝐿𝑛𝑛 at the bottom of the water-negative surface is described as:

<!-- b000186 | prose | pages [12] -->
(9)

<!-- b000187 | prose | pages [12] -->
The saturated water absorption length 𝐿𝐿𝑡𝑡 at the top surface is described as (10)

<!-- b000188 | prose | pages [12] -->
The radius 𝑅𝑅′ of the bottom of the sandcastle after erosion is

<!-- b000189 | prose | pages [12] -->
(11)

<!-- b000190 | prose | pages [12] -->
The radius 𝑟𝑟′ of the top of the sandcastle after erosion is

<!-- b000191 | prose | pages [12] -->
(12)

<!-- b000192 | prose | pages [12] -->
The height 𝐻𝐻′ of the sandcastle after erosion is (13)

<!-- b000193 | prose | pages [12] -->
As the initial volume of sandcastle 𝑉𝑉0 = 0.2𝑚𝑚3 is constant,

<!-- b000194 | prose | pages [12] -->
(14)

<!-- b000195 | prose | pages [12] -->
To maximize the remaining proportion 𝛼𝛼, that is,

<!-- b000196 | prose | pages [12] -->
(15)

<!-- b000197 | prose | pages [12] -->
Genetic algorithm toolbox in MATLAB and partial derivative method are used to solve the problem. Results are as follows:

<!-- b000198 | prose | pages [12, 13] -->
关注数学模型 That is, at the value of 𝑉𝑉0 = 0.2𝑚𝑚3, 𝑅𝑅= 0.64𝑚𝑚, 𝑟𝑟= 0.20𝑚𝑚, 𝐻𝐻= 0.33𝑚𝑚, remaining proportion 𝛼𝛼 takes the maximum value 𝛼𝛼𝑚𝑚𝑚𝑚𝑚𝑚 = 62.4%.

<!-- b000199 | furniture | pages [12] -->
2

<!-- b000200 | furniture | pages [12] -->
MATHmodels

<!-- b000201 | furniture | pages [12] -->
获取更多资讯

<!-- b000202 | furniture | pages [13] -->
Team # 2019696                                                                  Page 11 of 27

<!-- b000203 | caption | pages [13] -->
Figure 5 The result of sandcastle-erosion model

<!-- b000205 | prose | pages [13] -->
The shape and proportion of the optimal 3D shape are shown in figure 6.

<!-- b000206 | caption | pages [13] -->
Figure 6 the optimal 3D model

<!-- b000207 | prose | pages [13] -->
Because the velocity and flux of the water-positive surface is bigger, more force is applied on water-positive surface. Similarly, there is less force applied on the water-negative surface and side of the geometry. On this aspect, the model could be further optimized as ellipsoidal cone sets to make water-positive side more stable. The optimized geometric model is eroded proportionally from four directions to maximize the resistance of the geometry. Optimized three-dimensional geometry model shows as follows(the blue one):

<!-- b000208 | caption | pages [13] -->
Figure 7 The optimized three-dimensional geometry model

<!-- b000209 | prose | pages [13] -->
关注数学模型

<!-- b000210 | furniture | pages [13] -->
2

<!-- b000211 | furniture | pages [13] -->
MATHmodels

<!-- b000212 | furniture | pages [13] -->
获取更多资讯

<!-- b000213 | furniture | pages [14] -->
Team # 2019696                                                                  Page 12 of 27

<!-- b000214 | heading | pages [14] -->
5.2 Solution to Optimal Water-to-Sand Mixture Proportion

<!-- b000215 | prose | pages [14] -->
As is discussed in problem analysis, the goal of problem 2 is to investigate the optimal sand-to-water mixture proportion to make the sandcastle most defensible. Water-to-sand proportion 𝛽𝛽 is defined as the volume of water divided by the volume of sandcastle (based on the hypothesis that the volume of sandcastle would not increase when the sandcastle absorbs water).

<!-- b000216 | prose | pages [14] -->
When 𝛽𝛽 is of small magnitude, the cohesion between sand grains turns to be weak, while cohesion increases sharply as 𝛽𝛽 increases. The cohesion of sand is considered to quickly disappear when the sand is saturated with water.

<!-- b000217 | prose | pages [14] -->
It is assumed that 𝐹𝐹 and 𝛽𝛽 have a relationship of (16)

<!-- b000218 | prose | pages [14] -->
at certain realms. Among them, 𝑘𝑘1 is a constant.

<!-- b000219 | prose | pages [14] -->
Cohesion 𝐹𝐹 is required to have a lower bound to make sure the sandcastle would not collapse without the influence of water. Correspondingly, 𝛽𝛽 is required to have a lower bound 𝛽𝛽𝑚𝑚𝑚𝑚𝑚𝑚≈ 10%.[2] Thus, the range of 𝛽𝛽 should be

<!-- b000220 | prose | pages [14] -->
(17)

<!-- b000221 | prose | pages [14] -->
Among them, 𝛽𝛽𝑚𝑚𝑚𝑚𝑚𝑚 represents water-to-sand mixture proportion when the whole sandcastle is saturated with water. It is referred that 𝛽𝛽𝑚𝑚𝑚𝑚𝑚𝑚≈30%.[2] Assume 𝑡𝑡0 represents the crashing time of waves on every point of the water-positive surface with sea level rises in a constant speed. The thickness 𝑇𝑇 cut by the waves and cohesion 𝐹𝐹 have an inverse relationship at a fixed duration 𝑡𝑡0, that is,

<!-- b000222 | prose | pages [14] -->
(18)

<!-- b000223 | prose | pages [14] -->
Among them, 𝑘𝑘2 is a constant. Thus, coefficient of length cutting 𝜆𝜆𝑐𝑐 and 𝑇𝑇 have a relationship of (19)

<!-- b000224 | prose | pages [14] -->
According to equations (1), (16)~(19), it is concluded that the length 𝑙𝑙1 which is cut perpendicularly of the water-positive surface and water-to-sand mixture proportion 𝛽𝛽 have a relationship of

<!-- b000225 | prose | pages [14] -->
(20)

<!-- b000226 | prose | pages [14] -->
Among them, 𝑆𝑆1 represents the area of water-positive surface, 𝑆𝑆1′ represents the area of

<!-- b000227 | prose | pages [14, 15] -->
关注数学模型 water-positive section.

<!-- b000228 | furniture | pages [14] -->
2

<!-- b000229 | furniture | pages [14] -->
MATHmodels

<!-- b000230 | furniture | pages [14] -->
获取更多资讯

<!-- b000231 | furniture | pages [15] -->
Team # 2019696                                                                  Page 13 of 27

<!-- b000233 | prose | pages [15] -->
When the sand is in the condition of absorbing water, 𝛽𝛽 and the time to reach saturated have a relationship of power function with exponent 1/2. Thus, the coefficient of saturated water absorption 𝜆𝜆𝑠𝑠 and water-to-sand proportion 𝛽𝛽 have a relationship of (21)

<!-- b000234 | prose | pages [15] -->
Among them, 𝑘𝑘3 is a constant. According to equations (3) and (21), it is concluded that (22)

<!-- b000235 | prose | pages [15] -->
It is referred that 𝑘𝑘2/𝑘𝑘1 = 1 × 10−2, 𝑘𝑘3 = 7 × 10−4.[3] Equation(22) indicates that in the same time, the larger the water-to-sand ratio is, the longer the sand layer reaches saturated.

<!-- b000236 | prose | pages [15] -->
To simplify calculation, we first calculate the water-to-sand mixture proportion based on the geometry of problem 1. Results are as follows:

<!-- b000237 | caption | pages [15] -->
Figure 8  The best 𝛽𝛽 of the optimal shape in problem 1

<!-- b000238 | prose | pages [15] -->
Within the limitation of (17), when 𝛽𝛽 takes the value of 𝛽𝛽1 = 22%, the remaining proportion of sandcastle could take its maximum value, which is approximately 65.0%. The optimal water-to-sand proportion is 22%, based on the geometry of problem 1. That is, for every 100 volumes of sand pile (with gaps in the sand), about 22 volumes of water are added to make the sandcastle.

<!-- b000239 | prose | pages [15] -->
Since the best structure of foundation is related to water-to-sand mixture proportion, in the following calculations 𝛽𝛽 is considered as an independent variable of ratio 𝛼𝛼, to compute the value of 𝛽𝛽 under the restricted conditions of (17).

<!-- b000240 | prose | pages [15, 16] -->
关注数学模型 Similarly, genetic algorithm toolbox of MATLAB and partial derivative method are used to solve the problem. As the function of three variables 𝛼𝛼(𝑅𝑅, 𝑟𝑟, 𝛽𝛽) is involved, the graph of the function is inconvenient to be shown. Only numerical results are given as follows:

<!-- b000241 | furniture | pages [15] -->
2

<!-- b000242 | furniture | pages [15] -->
MATHmodels

<!-- b000243 | furniture | pages [15] -->
获取更多资讯

<!-- b000244 | furniture | pages [16] -->
Team # 2019696                                                                  Page 14 of 27

<!-- b000246 | caption | pages [16] -->
Table 1 The result of optimal Water-to-Sand mixture proportion

<!-- b000247 | prose | pages [16] -->
𝑅𝑅 𝑟𝑟 𝛽𝛽 𝛼𝛼 0.58𝑚𝑚 0.23𝑚𝑚 24% 68.6%

<!-- b000248 | prose | pages [16] -->
Therefore, the optimal water-to-sand proportion is 𝜷𝜷= 𝟐𝟐𝟐𝟐% based on the consideration of various shapes of the frustrum of the cone. For every 100 volumes of sand pile (with gaps in the sand), about 24 volumes of water are added to make the sandcastle. The ratio of water to sand volume is about 1:5 when making the foundation of the sandcastle.

<!-- b000249 | heading | pages [16] -->
5.3 Sandcastle-Rain-Erosion Model

<!-- b000250 | prose | pages [16] -->
When rainfall is taken into consideration, in order to establish sandcastle-rain-erosion model, problem 3 is discussed in two situations: one is that sandcastle is eroded by both seawater and rainfall; the other is that sandcastle is eroded only by rainfall.

<!-- b000251 | prose | pages [16] -->
In situation 1, the impact of rainfall and the impact of seawater are superimposed directly, that is, rainfall directly affect the sandcastle that is eroded by seawater. Assume raindrops are particles with mass and vertically hit on the sandcastle, which have a same applied force compared with waves. Every part of the sandcastle was hit by the raindrops for the same time, which was represented as 𝑡𝑡1.

<!-- b000252 | prose | pages [16] -->
Assuming that the length that the raindrops vertically cut from the surface of the sandcastle stands for 𝑙𝑙4 in a period 𝑡𝑡1, which is proportional to the ratio of 𝑆𝑆2′ and 𝑆𝑆2.

<!-- b000253 | prose | pages [16] -->
(23)

<!-- b000254 | prose | pages [16] -->
Among them, 𝜆𝜆𝑐𝑐 represents coefficient of length cutting, 𝑆𝑆2𝑖𝑖′ represents the area of the vertical projection of top surface or side surface, 𝑆𝑆2𝑖𝑖 represents the area of top surface or side surface, 𝑖𝑖= 1,2 𝑜𝑜𝑜𝑜 3 represents situation on top surface, water-positive surface or water-negative surface.

<!-- b000255 | prose | pages [16, 17] -->
关注数学模型 In order to simplify subsequently processing steps, it is similarly assumed that after the sand on the surface was eroded by the rain, part of the sand should have fallen out but remains saturated slightly attaching to the majority of sandcastle. Another schematic of the reduction of sandcastle is showed below.

<!-- b000256 | furniture | pages [16] -->
2

<!-- b000257 | furniture | pages [16] -->
MATHmodels

<!-- b000258 | furniture | pages [16] -->
获取更多资讯

<!-- b000259 | furniture | pages [17] -->
Team # 2019696                                                                  Page 15 of 27

<!-- b000260 | caption | pages [17] -->
Figure 9 The sketch of vertical projection of each face

<!-- b000262 | caption | pages [17] -->
Figure 10 Another schematic of the reduction of sandcastle

<!-- b000263 | prose | pages [17] -->
Based on the schematic of problem 1, the yellow section is the part that is saturated by the rainfall, the angle of inclination of the sandcastle remains same after the erosion of the rain. The remaining height of sandcastle 𝐻𝐻1′′ superimposed with rain erosion is (24)

<!-- b000264 | prose | pages [17] -->
The radius of top surface of sandcastle 𝑟𝑟1′′ superimposed with rain erosion is

<!-- b000265 | prose | pages [17] -->
(25)

<!-- b000266 | prose | pages [17] -->
The radius of bottom surface of sandcastle 𝑅𝑅1′′ superimposed with rain erosion is

<!-- b000267 | prose | pages [17] -->
(26)

<!-- b000268 | prose | pages [17] -->
When the remaining proportion 𝛼𝛼1′′ is

<!-- b000269 | prose | pages [17, 18] -->
关注数学模型 (27)

<!-- b000270 | furniture | pages [17] -->
2

<!-- b000271 | furniture | pages [17] -->
MATHmodels

<!-- b000272 | furniture | pages [17] -->
获取更多资讯

<!-- b000273 | furniture | pages [18] -->
Team # 2019696                                                                  Page 16 of 27

<!-- b000275 | prose | pages [18] -->
′′ = According to the data processed in problem 1 (𝑅𝑅= 0.64𝑚𝑚,𝑟𝑟= 0.20𝑚𝑚), it is concluded that 𝛼𝛼1 55.7%. Using the algorithm similar to problem 1, results are as follows.

<!-- b000276 | caption | pages [18] -->
Figure 11 The result of Sandcastle-Rain-Erosion model for situation 1

<!-- b000277 | prose | pages [18] -->
That is, at the value of 𝑉𝑉0 = 0.2𝑚𝑚3, 𝑅𝑅= 0.52𝑚𝑚, 𝑟𝑟= 0.16𝑚𝑚, 𝐻𝐻= 0.50𝑚𝑚, remaining proportion ′′ ′′ 𝛼𝛼1 ′′ takes the maximum value 𝛼𝛼1𝑚𝑚𝑚𝑚𝑚𝑚 = 62.4%. As 𝛼𝛼1 ′′  reaches 𝛼𝛼1𝑚𝑚𝑚𝑚𝑚𝑚 , the remaining volume of the latter three-dimensional geometry model increases approximately 4% compared to the geometry model established in problem 1. Thus, three-dimensional geometry in problem 1 is not the optimum in the situation 1 of problem 3.

<!-- b000278 | prose | pages [18] -->
In situation 2, only the impact of rainfall is considered. The schematic of the reduction of sandcastle is showed below:

<!-- b000279 | caption | pages [18] -->
Figure 12 The schematic of the reduction of sandcastle

<!-- b000280 | prose | pages [18] -->
Similarly, the yellow section is the part that is saturated by the rainfall, the angle of inclination of the sandcastle remains same after the erosion of the rain.

<!-- b000281 | prose | pages [18, 19] -->
关注数学模型 The remaining height of sandcastle 𝐻𝐻2′′ only with rain erosion is (28)

<!-- b000282 | furniture | pages [18] -->
2

<!-- b000283 | furniture | pages [18] -->
MATHmodels

<!-- b000284 | furniture | pages [18] -->
获取更多资讯

<!-- b000285 | furniture | pages [19] -->
Team # 2019696                                                                  Page 17 of 27

<!-- b000287 | prose | pages [19] -->
The radius of the top surface of sandcastle 𝑟𝑟2′′ only with rain erosion is

<!-- b000288 | prose | pages [19] -->
(29)

<!-- b000289 | prose | pages [19] -->
The radius of the bottom surface of sandcastle 𝑅𝑅2′′ only with rain erosion is

<!-- b000290 | prose | pages [19] -->
(30)

<!-- b000291 | prose | pages [19] -->
When the remaining proportion 𝛼𝛼2′′ is

<!-- b000292 | prose | pages [19] -->
(31)

<!-- b000293 | prose | pages [19] -->
The results are as follows. ′′ = According to the data processed in problem 1 (𝑅𝑅= 0.64𝑚𝑚,𝑟𝑟= 0.20𝑚𝑚), it is concluded that 𝛼𝛼2 92.6%. It is observed that lim ℎ→+∞𝛼𝛼2′′ = 100%. As the relationship between the height and the

<!-- b000294 | prose | pages [19] -->
′′ is unsolvable. However, it is stability of the sandcastle was not considered in the model, 𝛼𝛼2𝑚𝑚𝑚𝑚𝑚𝑚 confirmed that three-dimensional geometry in problem 1 is not the optimum in this situation.

<!-- b000295 | heading | pages [19] -->
6 Advice on Building a Sandcastle

<!-- b000296 | prose | pages [19] -->
 Advice 1: Increase the initial volume of sandcastles. When the sandcastle is extremely small, it is difficult to withstand the waves and tides. The results of the sandcastle-erosion model also show that increasing the initial volume  𝑉𝑉0 within a certain range can increase the proportion of remaining sandcastle after the erosion of waves.

<!-- b000297 | prose | pages [19, 20] -->
关注数学模型  Advice 2: Build the sandcastle on a beach far from the sea. The beach is inclined to the sea in reality. The farther the sandcastle is from the sea and the higher the sandcastle is, the less sandcastle is affected by the waves. When the distance is far enough, the erosion of the sea can be completely eliminated.

<!-- b000298 | furniture | pages [19] -->
2

<!-- b000299 | furniture | pages [19] -->
MATHmodels

<!-- b000300 | furniture | pages [19] -->
获取更多资讯

<!-- b000301 | furniture | pages [20] -->
Team # 2019696                                                                  Page 18 of 27

<!-- b000302 | caption | pages [20] -->
Figure 13 The relationship between 𝛼𝛼𝑚𝑚𝑚𝑚𝑚𝑚 and 𝑉𝑉0

<!-- b000304 | prose | pages [20] -->
 Advice 3: Add some adhesive to the sand-water mixture. The adhesive can enhance the cohesion between sand grains, which helps the surface sand adhere to the main body of the sandcastle. Meanwhile, the adhesive can reduce the surface sand exposure to the gap in the sea water, reducing the rate of sand saturation to a certain extent. Using adhesive could also reduce the volume that sandcastle lost in the same period.

<!-- b000305 | prose | pages [20] -->
 Advice 4: Build a sand wall around the sandcastle. When kids are building sandcastles, moats around sandcastles are often built. On the one hand, sand walls absorb the force caused by the crashing of waves; on the other hand, sand walls can delay the time that sandcastle contacts tides.

<!-- b000306 | heading | pages [20] -->
7 Sensitivity Analysis

<!-- b000307 | prose | pages [20] -->
As coefficient of length cutting 𝜆𝜆𝑐𝑐 and coefficient of saturated water absorption 𝜆𝜆𝑠𝑠 and initial volume 𝑉𝑉0 have an important influence on the optimum, sensitivity analysis is processed. For three coefficients 𝜆𝜆𝑐𝑐, 𝜆𝜆𝑠𝑠 and 𝑉𝑉0, a change of ±5% is applied. The relative influence on the optimal radius of bottom surface 𝑅𝑅, radius of top surface 𝑟𝑟, height of the sandcastle 𝐻𝐻 and remaining proportion of the sandcastle 𝛼𝛼 is observed.

<!-- b000308 | prose | pages [20, 21] -->
关注数学模型 result 𝑟𝑟 𝛼𝛼 𝑅𝑅 𝐻𝐻 𝜆𝜆𝑐𝑐 +5% 0.73% 1.24% 1.92% 1.96% +4% 0.59% 1.00% 1.55% 1.57% +3% 0.44% 0.75% 1.18% 1.18% +2% 0.29% 0.50% 0.78% 0.78% +1% 0.15% 0.25% 0.40% 0.39% -1% 0.15% 0.25% 0.40% 0.34% -2% 0.29% 0.51% 0.81% 0.81% -3% 0.44% 0.77% 1.21% 1.20% -4% 0.58% 1.03% 1.61% 1.72% -5% 0.73% 1.29% 1.74% 2.01%

<!-- b000309 | furniture | pages [20] -->
2

<!-- b000310 | furniture | pages [20] -->
MATHmodels

<!-- b000311 | furniture | pages [20] -->
获取更多资讯

<!-- b000312 | furniture | pages [21] -->
Team # 2019696                                                                  Page 19 of 27

<!-- b000313 | caption | pages [21] -->
Table 2 The sensitivity analysis of  𝜆𝜆 𝑐𝑐

<!-- b000315 | caption | pages [21] -->
Table 3 The sensitivity analysis of 𝜆𝜆𝑠𝑠

<!-- b000316 | prose | pages [21] -->
result 𝑟𝑟 𝛼𝛼 𝑅𝑅 𝐻𝐻 𝜆𝜆𝑠𝑠 +5% 0.50% 1.05% 1.54% 3.50% +4% 0.42% 0.83% 1.31% 2.60% +3% 0.31% 0.63% 0.96% 1.93% +2% 0.21% 0.44% 0.65% 1.30% +1% 0.11% 0.22% 0.31% 0.64% -1% 0.11% 0.21% 0.30% 0.58% -2% 0.25% 0.44% 0.65% 1.30% -3% 0.35% 0.69% 1.04% 2.00% -4% 0.48% 0.92% 1.32% 2.73% -5% 0.55% 1.11% 1.60% 3.44%

<!-- b000317 | caption | pages [21] -->
Table 4 The sensitivity analysis of V0

<!-- b000318 | prose | pages [21] -->
result 𝑅𝑅 𝑟𝑟 𝛼𝛼 𝐻𝐻 𝑉𝑉0 +5% 1.60% 1.58% 1.76% 1.83% +4% 1.27% 1.27% 1.45% 1.52% +3% 0.94% 0.93% 1.09% 1.15% +2% 0.63% 0.62% 0.74% 0.78% +1% 0.32% 0.31% 0.37% 0.39% -1% 0.32% 0.30% 0.38% 0.38% -2% 0.65% 0.63% 0.74% 0.81% -3% 0.94% 0.93% 1.10% 1.19% -4% 1.30% 1.31% 1.48% 1.61% -5% 1.62% 1.61% 1.79% 2.02%

<!-- b000319 | prose | pages [21] -->
The results show that the coefficients  𝜆𝜆𝑐𝑐, 𝜆𝜆𝑠𝑠 and initial volume 𝑉𝑉0 have high stabilities. Thus, the error of the final results is within the acceptable range. The results that including the optimal

<!-- b000320 | prose | pages [21, 22] -->
关注数学模型 sandcastle shape under the influence of seawater based on sandcastle-erosion model, the optimal water-to-sand proportion and the optimal sandcastle shape under the influence of rainfall and seawater based on sandcastle-rain-erosion model are reliable.

<!-- b000321 | furniture | pages [21] -->
2

<!-- b000322 | furniture | pages [21] -->
MATHmodels

<!-- b000323 | furniture | pages [21] -->
获取更多资讯

<!-- b000324 | furniture | pages [22] -->
Team # 2019696                                                                  Page 20 of 27

<!-- b000326 | heading | pages [22] -->
8 Strengths and Weakness

<!-- b000327 | heading | pages [22] -->
8.1  Strengths

<!-- b000328 | prose | pages [22] -->
 In this article, the erosion effects of waves, tides and rainfall on sand grains are analyzed based on the related principles of fluid-structure interaction. The effect of seawater on sandcastle is simplified as the wave crashing to cut sand layer and the tide immersing to make the sand become saturated with water and be on the verge of falling off. More attention is paid to the main aspects of the solid-liquid interaction, and the tedious microscopic analysis is avoided.

<!-- b000329 | prose | pages [22] -->
 Sandcastle-erosion model simulates the scenario in which an ordinary family builds a sandcastle on the beach, based on the assumption that the amount of sand is appropriate, so that people can directly use the results of this model to build the foundation of sandcastle in their real lives.

<!-- b000330 | prose | pages [22] -->
 Combined with the partial derivative and MATLAB genetic algorithm toolbox to solve the result greatly reduce the computation time, while ensuring the accuracy of the result.

<!-- b000331 | heading | pages [22] -->
8.2  Weakness

<!-- b000332 | prose | pages [22] -->
 In order to facilitate calculation and reality constructions, only relatively regular three-dimensional geometries are considered, while the ignored geometries including frustum of elliptic cone and eccentric frustum of a cone may have a better resistance to erosion.

<!-- b000333 | prose | pages [22] -->
 It is assumed the waves have the same impact effect on each point of the water-positive surface of the sandcastle. However, the thickness of the sand layer crashed by the waves in the front is larger than the thickness of the sides.

<!-- b000334 | prose | pages [22] -->
 The saturated water absorption rate of different sand is different, so is the minimum water-to-sand proportion that makes sandcastle stable. As there are various kinds of sands, estimation in this article could cause much difference.

<!-- b000335 | prose | pages [22, 23] -->
关注数学模型 Article for Fun in the Sun

<!-- b000336 | furniture | pages [22] -->
2

<!-- b000337 | furniture | pages [22] -->
MATHmodels

<!-- b000338 | furniture | pages [22] -->
获取更多资讯

<!-- b000339 | furniture | pages [23] -->
Team # 2019696                                                                  Page 21 of 27

<!-- b000341 | prose | pages [23] -->
How to build a perfect sandcastle?

<!-- b000342 | prose | pages [23] -->
Have you ever tried to build a sandcastle when you are at the beach? Of course, I have. However, the ‘sandcastle’ I built was just nothing but a shapeless mound of sand decorated with shells and other objects. I believe there are many people concerning about how to build a perfect sandcastle. If the tide rises, have you ever thought about what shape it will be in order to be more resistant to the erosion of the sea?

<!-- b000343 | prose | pages [23] -->
Some people may think that building sandcastle is just a mechanical building game like building a house, other people may consider it as a game identifying combinations of different shapes. However, the game of building a sandcastle may seem easy, it actually involves the mechanics of the interaction between fluid and solid. Specialized research in the knowledge of this area can be used in the construction of bridges, navigation and aviation industries. Now let’s talk about how to use knowledge to build a perfect sandcastle!

<!-- b000344 | prose | pages [23] -->
First, we need to understand why a sandcastle could stand before explaining the best method to build a perfect sandcastle. Kids who experienced playing on a beach are aware that dry sand create nothing useful. Sand becomes sticky only when it is mixed with water. This is because the water will disperse into small drops and fill in the gaps between the grains of sand. The bridge of water droplets between the grains creates an attraction called “surface tension” between the connected grains, and it is this attraction that makes sand grain difficult to separate. (If you don't know the surface tension, you can fill the glass with a glass of water, the circular projections at the top of the cup are the result of surface tension attraction between water droplets)

<!-- b000345 | prose | pages [23] -->
Now you have known the reason behind the sandcastle's standing. Anyone who has ever built a sandcastle will know that the first step in building a sandcastle is to build a large foundation on which to build a more elaborate sandcastle. The foundation is always very important, because you never know when the waves will rise and destroy the hard-built sandcastle. So how do we build a properly shaped sandcastle foundation that could mostly resist other effects? Don't worry, our team provides you with answers by building mathematical models.

<!-- b000346 | prose | pages [23] -->
In order to find the most suitable shape for building the sandcastle foundation, taking the factors that threaten the sandcastle into account, such as frequent and rapid waves and gradually rising tides, we built the sandcastle-erosion model. To ensure the accuracy of the model results, we used the same kind of sand and mixed it with water in the same proportion.

<!-- b000347 | prose | pages [23, 24] -->
关注数学模型 By simulating the residual states of sandcastles of different shapes under different erosion conditions under the same volume and comparing them, we finally get the best geometry for sandcastle foundation. It is a round platform with a height of about 30 cm and a bottom radius of about 64 cm. You’re going to make it a little bit narrower on the top, with a radius of about 20 centimeters on the top. When building the foundation, you can make the side facing the waves steeper to enhance the stability of the foundation.

<!-- b000348 | furniture | pages [23] -->
2

<!-- b000349 | furniture | pages [23] -->
MATHmodels

<!-- b000350 | furniture | pages [23] -->
获取更多资讯

<!-- b000351 | furniture | pages [24] -->
Team # 2019696                                                                  Page 22 of 27

<!-- b000353 | prose | pages [24] -->
Since the ratio of sand to water is important to the success of a sandcastle, the golden ratio of sand to water is also a concern for sandcastle builders. To find this best proportion, we also use the sandcastle-erosion model to determine the ratio of raw materials that can make the sandcastle the most stable, and this ratio is about 22%. In other words, during the construction process, foundation of sandcastles with about five parts of sand for one part of water is the most stable.

<!-- b000354 | prose | pages [24] -->
People usually choose to play by the beach on a sunny day. However, as the weather is unpredictable, sudden rain is often the case. Considering the factor of rainfall, in order to find the most stable geometry of sandcastle in rainy days, we improved the previous sandcastle-erosion model to the sandcastle-rain-erosion model. In this model, we found that the sandcastles that were most resistant to erosion on sunny days does not show the same strength on rainy days, but the basic shape was not much different. The final result is also a round platform with bottom radius of about 52 cm, top radius of about 16 cm, a height of about 50 cm. Our model also shows that sandcastles break down faster in rainy days.

<!-- b000355 | prose | pages [24] -->
How's that? After looking at the results of our models, I believe you can also build a perfect sandcastle. Try with your friends and family next time!

<!-- b000356 | prose | pages [24] -->
关注数学模型

<!-- b000357 | furniture | pages [24] -->
2

<!-- b000358 | furniture | pages [24] -->
MATHmodels

<!-- b000359 | furniture | pages [24] -->
获取更多资讯

<!-- b000360 | furniture | pages [25] -->
Team # 2019696                                                                  Page 23 of 27

<!-- b000361 | heading | pages [25] -->
References

<!-- b000362 | references | pages [25] -->
[1] Gröger, T., Tüzün, U., & Heyes, D. M. (2003). Modelling and measuring of cohesion in wet granular

<!-- b000363 | references | pages [25] -->
materials. Powder Technology, 133(1-3), 203–215.

<!-- b000364 | references | pages [25] -->
[2] Nowak, S., Samadani, A., & Kudrolli, A. (2005). Maximum angle of stability of a wet granular pile.

<!-- b000365 | references | pages [25] -->
Nature Physics, 1(1), 50–52.

<!-- b000366 | references | pages [25] -->
[3] Hornbaker, D. J., Albert, R., Albert, I., Barabási, A.-L., & Schiffer, P. (1997). What keeps sandcastles

<!-- b000367 | references | pages [25] -->
standing? Nature, 387(6635), 765–765.

<!-- b000368 | references | pages [25] -->
[4] Emiroğlu, M., Yalama, A., & Erdoğdu, Y. (2015). Performance of ready-mixed clay plasters produced

<!-- b000369 | references | pages [25] -->
with different clay/sand ratios. Applied Clay Science, 115, 221–229.

<!-- b000370 | references | pages [25] -->
[5] Kudrolli, A. (2008). Sticky sand. Nature Materials, 7(3), 174–175.

<!-- b000371 | references | pages [25] -->
[6] Halsey, T. C., & Levine, A. J. (1998). How Sandcastles Fall. Physical Review Letters, 80(14), 3141–

<!-- b000372 | references | pages [25] -->
3144.

<!-- b000373 | references | pages [25] -->
[7] Pakpour, M., Habibi, M., Møller, P., & Bonn, D. (2012). How to construct the perfect sandcastle.

<!-- b000374 | references | pages [25] -->
Scientific Reports, 2(1).

<!-- b000375 | references | pages [25] -->
[8] National Marine Data Information Center. [DB/OL]. https://www.cnss.com.cn/tide/2020.

<!-- b000376 | references | pages [25] -->
关注数学模型

<!-- b000377 | furniture | pages [25] -->
2

<!-- b000378 | furniture | pages [25] -->
MATHmodels

<!-- b000379 | furniture | pages [25] -->
获取更多资讯

<!-- b000380 | furniture | pages [26] -->
Team # 2019696                                                                  Page 24 of 27

<!-- b000381 | heading | pages [26] -->
Appendix

<!-- b000382 | prose | pages [26] -->
1. The partial derivative of problem 1

<!-- b000383 | prose | pages [26] -->
2. The partial derivative of problem 2

<!-- b000384 | prose | pages [26, 27] -->
关注数学模型 3. The partial derivative of problem 3

<!-- b000385 | furniture | pages [26] -->
2

<!-- b000386 | furniture | pages [26] -->
MATHmodels

<!-- b000387 | furniture | pages [26] -->
获取更多资讯

<!-- b000388 | furniture | pages [27] -->
Team # 2019696                                                                  Page 25 of 27

<!-- b000390 | prose | pages [27] -->
关注数学模型

<!-- b000391 | furniture | pages [27] -->
2

<!-- b000392 | furniture | pages [27] -->
MATHmodels

<!-- b000393 | furniture | pages [27] -->
获取更多资讯
