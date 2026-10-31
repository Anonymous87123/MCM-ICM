# P-A-2016-54164-57a2b533

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000003 | front_matter | pages [1] -->
54164

<!-- b000004 | front_matter | pages [1] -->
T1 ________________ F1 ________________ T2 ________________ F2 ________________ Problem Chosen T3 ________________ F3 ________________

<!-- b000005 | front_matter | pages [1] -->
A

<!-- b000006 | front_matter | pages [1] -->
T4 ________________ F4 ________________

<!-- b000007 | front_matter | pages [1] -->
2016

<!-- b000008 | prose | pages [1] -->
MCM/ICM

<!-- b000009 | heading | pages [1] -->
Summary Sheet

<!-- b000010 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000011 | heading | pages [1] -->
Abstract

<!-- b000012 | prose | pages [1] -->
We present a user-friendly strategy for keeping the water in a bathtub as close as possible to a certain preferred temperature. This strategy consists in two main constituents: adjusting the hot water flow from the faucet to keep the bathtub temperature suitably high, and using hand motions to distribute the heat evenly throughout the bath water.

<!-- b000013 | prose | pages [1] -->
As for determining the necessary water flow, we first create a model that determines the temperature of the bath water at any point in time. We posit that the temperature of the water in the bath is dependent on the cooling due to the ambient temperature of the room, which obeys the proportionality given by Newton’s Law of Cooling; and the heating due to the added hot water from the faucet. Our model combines the temperature changes over time from these two entities into one consummate differential equation.

<!-- b000014 | prose | pages [1] -->
We determine the experimental constant of proportionality for Newton’s Law of Cooling by proposing that this constant itself is dependent on a combination of volume of the water and surface area exposed to the air. Taking experimental data from varied sources, including an experiment we conducted and documented over the time frame of the MCM competition, we were able to extrapolate values for the constant attributable to any bathtub given its volume and surface area exposed to air.

<!-- b000015 | prose | pages [1] -->
We then run a computer simulation to model the temperature changes over time in a standard bathtub with our differential equation, determining how much hot water needs to flow in to keep the total deviance over time of the temperature of the bath from a desired temperature at a minimum. We found the optimal flow rate for a standard bathtub at standard conditions to be 1.81 gallons/minute, or about 11% of the maximum flow rate.

<!-- b000016 | prose | pages [1] -->
Our model was able to predict optimal flow rates for many different combinations of volume, surface area, tub material, and additives. We found that more effective insulating materials led to lower optimal flow rates (less hot water needed), as did the addition of additives. Volume and surface area, surprisingly, showed no clear trend.

<!-- b000017 | prose | pages [1] -->
As for keeping the temperature roughly even in the bathtub, we suggest that the user swirl his hands counter-clockwise with respect to the faucet as shown in Figure 1. This is a simple yet effective way to distribute the heat acceptably evenly throughout the tub water.

<!-- b000018 | prose | pages [1] -->
As alternatives for those who do not wish to make their bath into an exercise session, we invented an original product (Home Jacuzzi) that is low-cost and aids in heating the water evenly.

<!-- b000019 | prose | pages [2] -->
The Math Behind the Bath: A ”Cool” Investigation on Cooling

<!-- b000020 | furniture | pages [2] -->
Team #54164

<!-- b000021 | prose | pages [2] -->
February 2016

<!-- b000022 | furniture | pages [3] -->
Team #54164

<!-- b000023 | furniture | pages [3] -->
Page 1 of 42

<!-- b000024 | heading | pages [3] -->
1 Abstract

<!-- b000025 | prose | pages [3] -->
We present a user-friendly strategy for keeping the water in a bathtub as close as possible to a certain preferred temperature. This strategy consists in two main constituents: adjusting the hot water ﬂow from the faucet to keep the bathtub temperature suitably high, and using hand motions to distribute the heat evenly throughout the bath water.

<!-- b000026 | prose | pages [3] -->
As for determining the necessary water ﬂow, we ﬁrst create a model that determines the tem- perature of the bath water at any point in time. We posit that the temperature of the water in the bath is dependent on the cooling due to the ambient temperature of the room, which obeys the proportionality given by Newton’s Law of Cooling; and the heating due to the added hot water from the faucet. Our model combines the temperature changes over time from these two entities into one consummate diﬀerential equation.

<!-- b000027 | prose | pages [3] -->
We determine the experimental constant of proportionality for Newton’s Law of Cooling by proposing that this constant itself is dependent on a combination of volume of the water and surface area exposed to the air. Taking experimental data from varied sources, including an experiment we conducted and documented over the time frame of the MCM competition, we were able to extrapolate values for the constant attributable to any bathtub given its volume and surface area exposed to air.

<!-- b000028 | prose | pages [3] -->
We then run a computer simulation to model the temperature changes over time in a standard bathtub with our diﬀerential equation, determining how much hot water needs to ﬂow in to keep the total deviance over time of the temperature of the bath from a desired temperature at a minimum. We found the optimal ﬂow rate for a standard bathtub at standard conditions to be 1.81 gallons/minute, or about 11% of the maximum ﬂow rate.

<!-- b000029 | prose | pages [3] -->
Our model was able to predict optimal ﬂow rates for many diﬀerent combinations of volume, surface area, tub material, and additives. We found that more eﬀective insulating materials led to lower optimal ﬂow rates (less hot water needed), as did the addition of additives. Volume and surface area, surprisingly, showed no clear trend.

<!-- b000030 | prose | pages [3] -->
As for keeping the temperature roughly even in the bathtub, we suggest that the user swirl his hands counter-clockwise with respect to the faucet as shown in Figure 1. This is a simple yet eﬀective way to distribute the heat acceptably evenly throughout the tub water.

<!-- b000031 | prose | pages [3] -->
As alternatives for those who do not wish to make their bath into an exercise session, we invented an original product (Home Jacuzzi) that is low-cost and aids in heating the water evenly.

<!-- b000032 | heading | pages [3] -->
1.1 Non-Technical Explanation

<!-- b000033 | prose | pages [3] -->
Why is it so diﬃcult to keep the temperature of the water even throughout when taking a bath? In a standard single-faucet bathtub, hot water comes out of the faucet on only one side of the bath, leaving the other side of the bath colder until enough time passes for the temperature to even out. When left running, this might take more time than a user wants to wait for.

<!-- b000034 | prose | pages [3] -->
To further complicate things, hot water is also slightly less dense than cold water, and will thus be more concentrated on the surface of the bathtub than the bottom of the tub.

<!-- b000035 | prose | pages [3] -->
To make the temperature consistent, the easiest solution is to cup your hands and circulate the hot water from the side with the faucet to the other side of the tub, and also circulate the hot water from the water surface to the bottom of the top.

<!-- b000036 | prose | pages [3] -->
Another option, however, for those of us who don’t want to spend the duration of our bath ﬂailing our arms, is to use our invention, ”Home Jacuzzi.” Our invention spans the length and

<!-- b000037 | prose | pages [3] -->
Page 1

<!-- b000038 | furniture | pages [4] -->
Team #54164

<!-- b000039 | furniture | pages [4] -->
Page 2 of 42

<!-- b000040 | contents | pages [4] -->
width of the bathtub, and attaches onto the faucet. The hot water from the faucet is then funneled

<!-- b000041 | contents | pages [4] -->
through the device towards the bottom of the tub, creating a Jacuzzi-like eﬀect. The hot water

<!-- b000042 | contents | pages [4] -->
then rises to the surface, mixing with the water above it and creating an evenly distributed, uniform

<!-- b000043 | contents | pages [4] -->
temperature throughout the tub.

<!-- b000044 | contents | pages [4] -->
Now that we can keep the temperature consistent throughout the tub, we’re still left to ﬁgure

<!-- b000045 | contents | pages [4] -->
out how high we should turn our faucet to keep the water from going cold.

<!-- b000046 | contents | pages [4] -->
Of course, turning it too high is a waste of water and, on top of that, can increase the temperature

<!-- b000047 | contents | pages [4] -->
to uncomfortably high levels. Too low, and we get to wade around in lukewarm to cold waters that

<!-- b000048 | contents | pages [4] -->
make us not want to take a bath at all. So we want to ﬁnd the optimal ﬂow rate on our faucet that

<!-- b000049 | contents | pages [4] -->
gets our temperature to where we want it to be.

<!-- b000050 | contents | pages [4] -->
Not all bathtubs were created equal. The optimal ﬂow rate isn’t a set rate for all bathtubs.

<!-- b000051 | contents | pages [4] -->
For the standard 60”x30”x14” bathtub, we suggest turning the faucet up to about a ninth of

<!-- b000052 | contents | pages [4] -->
its max.

<!-- b000053 | contents | pages [4] -->
To conserve even more hot water, you even have the option of purchasing products like the

<!-- b000054 | contents | pages [4] -->
”Water Blanket” (”Water Blanket”) to keep the temperature of the bath warmer. Interestingly

<!-- b000055 | contents | pages [4] -->
enough, even bubble bath can keep your bath water hotter for longer. And no, it’s not ”just for

<!-- b000056 | contents | pages [4] -->
kids.”

<!-- b000057 | heading | pages [4] -->
Contents

<!-- b000058 | contents | pages [4] -->
1 Abstract

<!-- b000059 | contents | pages [4] -->
1

<!-- b000060 | contents | pages [4] -->
1.1

<!-- b000061 | contents | pages [4] -->
Non-Technical Explanation

<!-- b000062 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [4] -->
1

<!-- b000064 | contents | pages [4] -->
2 Introduction

<!-- b000065 | contents | pages [4] -->
3

<!-- b000066 | contents | pages [4] -->
2.1

<!-- b000067 | contents | pages [4] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [4] -->
3

<!-- b000069 | contents | pages [4] -->
2.2

<!-- b000070 | contents | pages [4] -->
Restatement of Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [4] -->
3

<!-- b000072 | contents | pages [4] -->
3 The Strategy

<!-- b000073 | contents | pages [4] -->
4

<!-- b000074 | contents | pages [4] -->
3.1

<!-- b000075 | contents | pages [4] -->
Distribution: A Simple Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [4] -->
4

<!-- b000077 | contents | pages [4] -->
3.2

<!-- b000078 | contents | pages [4] -->
Global Assumptions

<!-- b000079 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [4] -->
4

<!-- b000081 | contents | pages [4] -->
4 Simulating Heat Transfer

<!-- b000082 | contents | pages [4] -->
5

<!-- b000083 | contents | pages [4] -->
4.1

<!-- b000084 | contents | pages [4] -->
Local Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | contents | pages [4] -->
5

<!-- b000086 | contents | pages [4] -->
4.1.1

<!-- b000087 | contents | pages [4] -->
Variable Nomenclature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [4] -->
6

<!-- b000089 | contents | pages [4] -->
4.2

<!-- b000090 | contents | pages [4] -->
Creation of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [4] -->
6

<!-- b000092 | contents | pages [4] -->
4.2.1

<!-- b000093 | contents | pages [4] -->
Cooling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [4] -->
6

<!-- b000095 | contents | pages [4] -->
4.2.2

<!-- b000096 | contents | pages [4] -->
Experimental Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [4] -->
7

<!-- b000098 | contents | pages [4] -->
4.2.3

<!-- b000099 | contents | pages [4] -->
Heating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [4] -->
12

<!-- b000101 | contents | pages [4] -->
4.3

<!-- b000102 | contents | pages [4] -->
Simulation Design

<!-- b000103 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [4] -->
13

<!-- b000105 | contents | pages [4] -->
4.3.1

<!-- b000106 | contents | pages [4] -->
Selecting Optimal Flow Rate . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [4] -->
14

<!-- b000108 | contents | pages [4] -->
4.3.2

<!-- b000109 | contents | pages [4] -->
Validation of Model

<!-- b000110 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000111 | contents | pages [4] -->
16

<!-- b000112 | contents | pages [4] -->
5 Sensitivity Analysis: Varying Bathtub Characteristics

<!-- b000113 | contents | pages [4] -->
16

<!-- b000114 | contents | pages [4] -->
5.1

<!-- b000115 | contents | pages [4] -->
Varying Surface Area Under Constant Volume

<!-- b000116 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000117 | contents | pages [4] -->
16

<!-- b000118 | contents | pages [4] -->
5.2

<!-- b000119 | contents | pages [4] -->
Varying Volume Under Constant Surface Area

<!-- b000120 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000121 | contents | pages [4] -->
24

<!-- b000122 | contents | pages [4] -->
5.3

<!-- b000123 | contents | pages [4] -->
Observations

<!-- b000124 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [4] -->
32

<!-- b000126 | contents | pages [4] -->
Page 2

<!-- b000127 | furniture | pages [5] -->
Team #54164

<!-- b000128 | furniture | pages [5] -->
Page 3 of 42

<!-- b000129 | contents | pages [5] -->
5.4

<!-- b000130 | contents | pages [5] -->
Material of Bathtub

<!-- b000131 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000132 | contents | pages [5] -->
34

<!-- b000133 | contents | pages [5] -->
5.5

<!-- b000134 | contents | pages [5] -->
Additives (bubble bath) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000135 | contents | pages [5] -->
35

<!-- b000136 | heading | pages [5] -->
6 Conclusion

<!-- b000137 | prose | pages [5] -->
36 6.1 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 6.2 Strengths of Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 6.3 Limitations of Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 6.4 Future Work/Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 6.5 Home Jacuzzi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

<!-- b000138 | heading | pages [5] -->
Appendices

<!-- b000139 | prose | pages [5] -->
39

<!-- b000140 | prose | pages [5] -->
A Experimental Design for Real-World Bathtub Data 39

<!-- b000141 | prose | pages [5] -->
B Simulation Code 39

<!-- b000142 | heading | pages [5] -->
2 Introduction

<!-- b000143 | heading | pages [5] -->
2.1 Background

<!-- b000144 | prose | pages [5] -->
Baths, the best way we had to cleanse ourselves–until we became teens and discovered showers, at which point baths became ”uncool.” Yet, whenever we want to slow life down and relax a little, we can rest assured that the bath will always be there to ease our nerves. The health beneﬁts of taking a bath are plentiful (”5 Reasons You Need To Take A Bath”), but no one wants to hop into a steaming hot tub only to ﬁnd him or herself in cold or lukewarm water a half-hour later. Then, how can one keep a bath warm long enough to last a preferred duration? Most people own simple bathtubs, unequipped with secondary heating systems or circulating jets. Several factors can aﬀect the temperature change of bath water, including:

<!-- b000145 | prose | pages [5] -->
• the surface area of water exposed to air

<!-- b000146 | prose | pages [5] -->
• the volume of water that is being cooled

<!-- b000147 | prose | pages [5] -->
• the surrounding air temperature

<!-- b000148 | prose | pages [5] -->
• the rate of hot water ﬂow into the bathtub

<!-- b000149 | prose | pages [5] -->
• the material the bathtub is made out of (and how well it is able to provide insulation)

<!-- b000150 | prose | pages [5] -->
• whether any additives are introduced to the water, such as a bubble bath solution

<!-- b000151 | heading | pages [5] -->
2.2 Restatement of Problem

<!-- b000152 | prose | pages [5] -->
A person has settled into a bathtub for a long, relaxing bath, only to ﬁnd that after some time, the water has become noticeably cooler. In an attempt to salvage his satisfaction, he elects to turn on the faucet and let in some hot water to bring the temperature back up. Excess tub water leaves the tub through an overﬂow drain. Of course, he runs into a set of issues:

<!-- b000153 | prose | pages [5, 6] -->
Page 3 • The water in the tub is of inconsistent temperature, being hotter in some areas and cooler in others.

<!-- b000154 | furniture | pages [6] -->
Team #54164

<!-- b000155 | furniture | pages [6] -->
Page 4 of 42

<!-- b000157 | prose | pages [6] -->
• Turning the hot water ﬂow too high is a waste of water (and money).

<!-- b000158 | heading | pages [6] -->
3 The Strategy

<!-- b000159 | prose | pages [6] -->
Our ”strategy” presented to the person in the tub will be a combination of the solutions to queries 1 and 2—the person will have to take action to evenly distribute the heat in the bathtub water, and the person will have to set the hot water ﬂow in at a certain ﬂow rate to keep the bathtub water hot.

<!-- b000160 | heading | pages [6] -->
3.1 Distribution: A Simple Solution

<!-- b000161 | prose | pages [6] -->
We begin by addressing query number ”1”. In a standard single-faucet bathtub, water ﬂows from above on one side of the bathtub. Since hot water rises, more heat will be concentrated at the top of the bathtub. Because the faucet is only on one side of the tub, more heat will be concentrated on the side of the tub closest to the faucet. Therefore, we advise the person in the tub to cup his hands and make circles in the water as illustrated below:

<!-- b000162 | caption | pages [6] -->
Figure 1: Proposed strategy for equalizing the temperature of the water in any single-faucet bathtub.

<!-- b000163 | heading | pages [6] -->
3.2 Global Assumptions

<!-- b000164 | prose | pages [6] -->
• The standard bathtub is open and exposed to the air on the top surface, and built with acrylic material that is heavily insulated (”Bathtub Sizes”).

<!-- b000165 | prose | pages [6] -->
• Heat loss through heavily insulated surfaces is negligible.

<!-- b000166 | prose | pages [6] -->
• Heat loss through surfaces of poor insulation (thin glass, thin ﬁberglass) behaves as if that surface was directly exposed to air.

<!-- b000167 | prose | pages [6] -->
• The person in the bathtub follows the suggestion in Figure 1, allowing us to assume that water temperature is consistent throughout the tub at any point in time.

<!-- b000168 | prose | pages [6, 7] -->
Page 4 • The temperature sensitivity of the human body is such that we begin noticing appreciable diﬀerences in temperature at ±1.4◦C from the original temperature (Davies et al. 171)

<!-- b000169 | furniture | pages [7] -->
Team #54164

<!-- b000170 | furniture | pages [7] -->
Page 5 of 42

<!-- b000172 | prose | pages [7] -->
• The target temperature for the bath water is human body temperature, which is approxi- mately 37◦C.

<!-- b000173 | prose | pages [7] -->
• Since the person inside the tub is at thermal equilibrium with the water in the tub, we can treat the person’s body as an extension of the bathtub water.

<!-- b000174 | prose | pages [7] -->
• Room temperature remains constant throughout the duration of the bath, at 21◦C, the ac- cepted value for ambient room temperature.

<!-- b000175 | prose | pages [7] -->
• The faucet from which the hot water ﬂows has a maximum ﬂow rate of 16 gallons/min (”Bathtub Faucets”), and the person is able to toggle the faucet’s ﬂow rate to any rate between 0 gallons/min and 16 gallons/min.

<!-- b000176 | prose | pages [7] -->
• The hottest water we can release from the faucet has a temperature of 48◦C to prevent injury from scalding (A.O. Smith Corporation 1). This will be the assumed temperature of the additional water from the faucet.

<!-- b000177 | prose | pages [7] -->
• All bathtubs used in this paper for simulation and data are ﬁlled to the brim with the com- bination of water and person.

<!-- b000178 | heading | pages [7] -->
4 Simulating Heat Transfer

<!-- b000179 | prose | pages [7] -->
To address our second query, we consider a thermodynamic system of ﬁve constituents: the water in the tub, the water entering and leaving the tub, the walls of the tub, the human in the tub, and the air outside the tub. Heat transfer with the human and the walls is negligible as justiﬁed in our global assumptions. Thus, we need only consider the cooling of the tub water due to the air outside, and the heating of the tub water due to the incoming hot water.

<!-- b000180 | heading | pages [7] -->
4.1 Local Assumptions

<!-- b000181 | prose | pages [7] -->
• The industry standard bathtub in America is 60” × 30” × 14”, which results in a volume of 60×30×14 = 25, 200in3 and surface area exposed to the air of 60×30 = 1, 800in2 (”Bathtub Sizes”).

<!-- b000182 | prose | pages [7] -->
• Since the majority of bathtubs in America are insulated, we assume that the bathtub that we are simulating is well insulated on all sides except for the top. Therefore, heat can only escape from the bathtub from the top surface.

<!-- b000183 | prose | pages [7] -->
• Water cooling obeys Newton’s Law of Cooling closely enough to approximate a model for temperature over time.

<!-- b000184 | prose | pages [7] -->
• The ambient temperature is 21◦C.

<!-- b000185 | prose | pages [7] -->
• The temperature of the hot water from the faucet is 48◦C.

<!-- b000186 | prose | pages [7] -->
Page 5

<!-- b000187 | furniture | pages [8] -->
Team #54164

<!-- b000188 | furniture | pages [8] -->
Page 6 of 42

<!-- b000189 | heading | pages [8] -->
4.1.1 Variable Nomenclature

<!-- b000190 | prose | pages [8] -->
Below are the variables used throughout our model:

<!-- b000191 | prose | pages [8] -->
• k = cooling constant

<!-- b000192 | prose | pages [8] -->
• T = temperature of the water minus ambient room temperature

<!-- b000193 | prose | pages [8] -->
• T0 = initial temperature of the bathtub

<!-- b000194 | prose | pages [8] -->
• t = time in minutes

<!-- b000195 | prose | pages [8] -->
• SAE = surface area exposed to air in square meters

<!-- b000196 | prose | pages [8] -->
• V = volume in liters

<!-- b000197 | prose | pages [8] -->
• Q = change in heat energy, in joules

<!-- b000198 | prose | pages [8] -->
• m = mass of the water in the tub, in grams

<!-- b000199 | prose | pages [8] -->
• Cp = speciﬁc heat of the water, in Joules per gram-degree ◦C

<!-- b000200 | heading | pages [8] -->
4.2 Creation of the Model

<!-- b000201 | prose | pages [8] -->
Since the temperature of the water is constantly being altered by the cooling due to the surrounding air temperature and the heating due to the incoming water ﬂow, we created an equation to model the changes in temperature, based on Newton’s Law of Cooling and the speciﬁc heat capacity formula.

<!-- b000202 | heading | pages [8] -->
4.2.1 Cooling

<!-- b000203 | prose | pages [8] -->
The ﬁrst part of the model accounts for the cooling of the water due to the temperature of the environment. We chose to model this cooling with Newton’s Law of Cooling, which states that the diﬀerence in temperature is directly proportional to the negative of the current temperature, or

<!-- b000204 | prose | pages [8] -->
dT dt = −kT (1)

<!-- b000205 | prose | pages [8] -->
where T is the temperature, and k is the cooling constant that is derived from experimentation. To derive the form we want our regression equation for our experimental data to be in, we solve our diﬀerential equation by integration with separation of variables:

<!-- b000206 | prose | pages [8] -->
1 T dT = −kdt (2)

<!-- b000207 | prose | pages [8] -->
1 Z Z −kdt T dT = (3)

<!-- b000208 | prose | pages [8] -->
ln(T) = −kt + C (4)

<!-- b000209 | prose | pages [8] -->
where C is a constant. Solving for T,

<!-- b000210 | prose | pages [8] -->
T = e−kt+C = Ce−kt (5)

<!-- b000211 | prose | pages [8, 9] -->
Page 6 To solve for this constant of integration, C, we substitute in the initial temperature T0 of the water at time t = 0.

<!-- b000212 | furniture | pages [9] -->
Team #54164

<!-- b000213 | furniture | pages [9] -->
Page 7 of 42

<!-- b000215 | prose | pages [9] -->
T0 = Ce−k×0 = C × 1 (6)

<!-- b000216 | prose | pages [9] -->
giving us the regression equation form

<!-- b000217 | prose | pages [9] -->
T = T0e−kt (7)

<!-- b000218 | prose | pages [9] -->
Since k is dependent on the sum of physical conditions in each speciﬁc scenario, it can only be derived from experimental data. Then, to predict the value of k for our industry standard bathtub, we take sets of experimental data and analyze trends between them to extrapolate a value of k for our purposes.

<!-- b000219 | heading | pages [9] -->
4.2.2 Experimental Data

<!-- b000220 | prose | pages [9] -->
We created a graph to represent the data we found for temperature over time in 100mL, 300mL, and 800mL volumes of water (Gieseking). The ambient room temperature in this setting was 23◦C. We realized that it is wrong to model these data with exponential regressions that have horizontal asymptotes at 0◦C. Instead, since logically the temperature of the water should approach—but

<!-- b000221 | prose | pages [9, 10] -->
Page 7 never dip below—the room temperature, we create exponential regressions with horizontal asymp- totes at 23◦C instead. The easiest way to do this is to subtract 23◦C from all points for the purpose of regression, and then modifying the regression equation to account for the diﬀerence. The results are as follows:

<!-- b000222 | furniture | pages [10] -->
Team #54164

<!-- b000223 | furniture | pages [10] -->
Page 8 of 42

<!-- b000225 | prose | pages [10] -->
The resulting equations are:

<!-- b000226 | prose | pages [10] -->
y = 77e−0.029x + 23 (8) y = 77e−0.036x + 23 (9) y = 77e−0.052x + 23 (10)

<!-- b000227 | prose | pages [10] -->
for the 100mL beaker, 300mL beaker, and the 800mL beaker, respectively. Note that 23◦C has been added to each equation to account for the shift.

<!-- b000228 | prose | pages [10] -->
It’s unreasonable to hope that data from small beakers alone can accurately predict the tem- perature changes in a large bathtub. However, we could not ﬁnd any accessible experimental data for large volumes of water. This is likely due to the fact that when studying water cooling, most scientists will choose to use small quantities of water for convenience. Since it was diﬃcult to obtain large-scale water cooling data, we performed our own experiment with a bathtub to obtain a k-value that pertains to our model. The procedure of our experiment can be found in Appendix A.

<!-- b000229 | prose | pages [10] -->
The results of our experiment are as follows:

<!-- b000230 | prose | pages [10, 11] -->
Page 8 The regression equation for our bathtub temperature versus time, then, is

<!-- b000231 | furniture | pages [11] -->
Team #54164

<!-- b000232 | furniture | pages [11] -->
Page 9 of 42

<!-- b000234 | prose | pages [11] -->
which means our experimental k per minute is 0.00448 = 0.000075. However, this k was only 60 relevant to our speciﬁc bathtub. In order to ﬁnd k-values for bathtubs of varied volume and surface area, we needed to create a model for k.

<!-- b000235 | prose | pages [11] -->
We consider that there is a relationship between k and exposed surface area (SAE) and volume (V ). Reasoning through the fact that k is to be a constant, we assumed that k should be unitless.

<!-- b000236 | prose | pages [11] -->
V 2 Thus, when relating k to V and SAE, k should be dependent on a power of E to cancel the units SA3 of meters in the numerator and denominator.

<!-- b000237 | prose | pages [11] -->
The calculations for SAE must take into account the fact that bathtubs are heavily insulated on ﬁve of six faces, but beakers are not. The eﬀective SAE of the bathtub, then, is its top surface’s area, or 55 × 23 = 1, 265 in2. The eﬀective SAE of the beakers are their total surface area, because of our assumption that thin glass provides virtually no insulation. Then, their SAE is given by:

<!-- b000238 | prose | pages [11, 12] -->
Page 9 SAcylinder = 2πr2 + πrh (11)

<!-- b000239 | furniture | pages [12] -->
Team #54164

<!-- b000240 | furniture | pages [12] -->
Page 10 of 42

<!-- b000242 | prose | pages [12] -->
where r is the radius of the beaker and h is the height of the water in the beaker. Because the beakers were not ﬁlled in the experiments, we recalculate the eﬀective heights with the following relationship:

<!-- b000243 | prose | pages [12] -->
h = hbeaker × Vwater (12) Vbeaker giving us a surface area equation for the beakers of

<!-- b000244 | prose | pages [12] -->
SAcylinder = 2πr2 + rhbeaker × Vwater (13) Vbeaker V 2 Below is a table of V , SAE, E , and k values for our four data sets. SA3 SAE (m) V (L) k 0.052150438 0.8 0.026259385 0.030787608 0.3 0.030316642 0.015707963 0.1 0.040508908 0.8161274 269.48527 0.000075 V 2 Proceeding, we test an exponential regression on the four sets of data relating k to E . First SA3 V 2 we tested E , SA3

<!-- b000245 | prose | pages [12] -->
which gave us an R2 value of 0.99764. We then test ( V 2 E )2 SA3

<!-- b000246 | prose | pages [12, 13] -->
Page 10 which gave us an R2 value of 0.996529. Seeing as this is worse, we test q V 2 E , SA3

<!-- b000247 | furniture | pages [13] -->
Team #54164

<!-- b000248 | furniture | pages [13] -->
Page 11 of 42

<!-- b000250 | prose | pages [13] -->
which gave us an R2 value of 0.999294. Noticing improvement, we test 3q V 2 E , noting a possible SA3 connection between the three dimensions our heat transfer acts in, and the third-degree root we V 2 take on our E , SA3

<!-- b000251 | prose | pages [13, 14] -->
Page 11 which gives us the regression equation:

<!-- b000252 | furniture | pages [14] -->
Team #54164

<!-- b000253 | furniture | pages [14] -->
Page 12 of 42

<!-- b000255 | prose | pages [14] -->
r V 2 −0.1670819378576223 3 SA3 k = 0.385387190197681e (14) E

<!-- b000256 | prose | pages [14] -->
This model ﬁt the data with an accuracy of R2 = 0.99929854436231100000, which was even bet- ter than the previous attempts. Using this model for k, we predict a k-value of 0.385387190197681 for our standard 60” × 30” × 14” bathtub. Thus, our ﬁnal equation for the change in temperature due to the environment is

<!-- b000257 | prose | pages [14] -->
dT dt = −0.385387190197681T (15)

<!-- b000258 | heading | pages [14] -->
4.2.3 Heating

<!-- b000259 | prose | pages [14] -->
The second part of the model calculates the amount of heat added by the person as he turned on the water faucet to a certain ﬂow rate. To achieve this, we used the speciﬁc heat capacity formula, which is

<!-- b000260 | prose | pages [14] -->
∆Q = mCpT (16)

<!-- b000261 | prose | pages [14] -->
where ∆Q is the change in heat, m is mass, Cp is the speciﬁc heat capacity of water, and T is the change in temperature. There are two instances of heat change resulting from the addition of hot water: heat is being added through the addition of hot water from the faucet, and heat is being removed through the drainage of excess water. The heat contributed by the water ﬂowing in is given by the following equation:

<!-- b000262 | prose | pages [14] -->
Q1 = dm dt CpThot (17)

<!-- b000263 | prose | pages [14] -->
where Q1 is the heat from the water ﬂowing in, dm dt is the mass ﬂow rate of the water ﬂowing in, and T is the absolute temperature of the water ﬂowing in (Kelvins).

<!-- b000264 | prose | pages [14, 15] -->
Page 12 The heat lost from excess water drainage is given by the following equation:

<!-- b000265 | furniture | pages [15] -->
Team #54164

<!-- b000266 | furniture | pages [15] -->
Page 13 of 42

<!-- b000268 | prose | pages [15] -->
Q2 = dmlost CpTlost (18) dt dmlost where Q2 is the heat from the water draining out, is the mass ﬂow rate of the water dt draining out, and Tlost is the absolute temperature of the water draining out (Kelvins). By our global assumption that temperature is consistent throughout the tub, we have that Tlost is simply the temperature of the tub, T.

<!-- b000269 | prose | pages [15] -->
Because the volume of water ﬂowing in at any point in time is equivalent to the volume of water ﬂowing out due to overﬂow, the mass ﬂow rate out is equal to the mass ﬂow rate in, or dmlost = dm dt . Then, the heat change of the water in the tub can be obtained by subtracting the dt above two equations:

<!-- b000270 | prose | pages [15] -->
∆Q = dm dt Cp(Thot −T) (19)

<!-- b000271 | prose | pages [15] -->
We also have that

<!-- b000272 | prose | pages [15] -->
∆Q = mtubCpTtub (20)

<!-- b000273 | prose | pages [15] -->
Since ∆Q is common to both equations, we can substitute the expression dm dt Cp(Thot −T) for ∆Q in the second equation and solve for Ttub, which becomes:

<!-- b000274 | heading | pages [15] -->
4.3 Simulation Design

<!-- b000275 | prose | pages [15] -->
All that is left now is to combine the cooling and heating of the water to simulate the overall temperature change.

<!-- b000276 | prose | pages [15] -->
In order to simulate the cooling of the water when the person has not turned on the faucet, we use the Newton’s law diﬀerential obtained earlier:

<!-- b000277 | prose | pages [15] -->
dT dt = −0.385387190197681T (21)

<!-- b000278 | prose | pages [15] -->
And to simulate the change in temperature due to the addition of hot water, we add the equation obtained in the previous section to the above:

<!-- b000279 | prose | pages [15] -->
dT dt = −0.385387190197681T + dm dt (Thot −T)mtub (22)

<!-- b000280 | prose | pages [15] -->
We used a computer program written in Python (code included in Appendix B) to simulate the change in temperature of the bathtub according to the diﬀerential equation over a period of 40 minutes. All units are converted to standard SI units in the simulation. The simulation accounts for the loss of heat to the environment, as well as the heating of the water due to the person operating the faucet. In order to achieve this, we set up a loop to run the simulation between time t = 0 minutes to t = 40 minutes, what we assumed to be the end of the bath. During each one-minute ”frame” in this interval, we calculated the new temperature of the water using the previous temperature with the two equations for change in temperature per minute calculated in the previous section.

<!-- b000281 | prose | pages [15] -->
The simulation will begin by applying the ﬁrst equation to the temperature of the water every frame, since the hot water faucet is initially oﬀ. When the temperature of the water reaches a

<!-- b000282 | prose | pages [15, 16] -->
Page 13 noticeably cooler temperature (of 1.4◦C below its initial temperature), the person will turn on the hot water, and the simulation will no longer apply the ﬁrst equation, but instead the second equation, in order to account for the temperature gained from the hot water.

<!-- b000283 | furniture | pages [16] -->
Team #54164

<!-- b000284 | furniture | pages [16] -->
Page 14 of 42

<!-- b000286 | heading | pages [16] -->
4.3.1 Selecting Optimal Flow Rate

<!-- b000287 | prose | pages [16] -->
In order to evaluate the results for the various ﬂow rates, we used the deviance value, obtained by ﬁnding the sum of the squares of the diﬀerences between the ”current” temperature and the initial temperature every frame:

<!-- b000288 | prose | pages [16] -->
N X (xn −¯x)2 ∆total = (23) n Comparing the deviance of every ﬂow rate produces the following:

<!-- b000289 | prose | pages [16] -->
Now, selecting the optimal ﬂow rate is trivial. Since the optimal ﬂow rate is characterized by the least diﬀerence from the original temperature, it is represented by the point indicated at the bottom of the graph, at (1.81, 10.179381314125882). This means that our optimal ﬂow rate to be recommended to the person is 1.81 gallons/minute, which results in a total deviance of 10.179 from the original temperature of his bath. The following is a temperature vs. time graph of the simulation using the optimal ﬂow rate of 1.81 gallons per minute. Note that the curve initially decreases, as the temperature of the water is only aﬀected by the cooler temperature of the room. However, once the temperature of the water has dropped below 1.4◦C from the initial temperature of 37◦C, the person turns on the hot water faucet which begins to increase the temperature of the water.

<!-- b000290 | prose | pages [16, 17] -->
Page 14 Page 15

<!-- b000291 | furniture | pages [17] -->
Team #54164

<!-- b000292 | furniture | pages [17] -->
Page 15 of 42

<!-- b000294 | furniture | pages [18] -->
Team #54164

<!-- b000295 | furniture | pages [18] -->
Page 16 of 42

<!-- b000296 | heading | pages [18] -->
4.3.2 Validation of Model

<!-- b000297 | prose | pages [18] -->
To conﬁrm that our cooling simulation accurately models what occurs in the real world, we ran the simulation on the circumstances of our real-world experiment in Appendix B. Fitting the temperatures predicted by the simulation to the actual experimentally obtained data, we ﬁnd that the simulation is able to very accurately predict the temperatures at given points in time retroactively.

<!-- b000298 | prose | pages [18] -->
As a matter of fact, this diﬀerential simulation is even more accurate than the previous regression model we had obtained for the data:

<!-- b000299 | prose | pages [18] -->
y = 16e−0.00448x + 21 (24)

<!-- b000300 | prose | pages [18] -->
as that regression led to an R-squared value of 0.97326, and the simulation gave an R-squared value of 0.999836.

<!-- b000301 | prose | pages [18] -->
While the relationship between temperature and time in this graph appears to be linear, it is still exponential–the very small k-value is what makes it appear linear. Indeed, there is a very slight, hardly noticeable curvature to the above graph.

<!-- b000302 | heading | pages [18] -->
5 Sensitivity Analysis: Varying Bathtub Characteristics

<!-- b000303 | prose | pages [18] -->
We now address query number ”3” by creating various bathtub designs, varying the surface areas exposed and volumes, to observe the eﬀect of the surface area to volume ratio on the rate of cooling. The changes in surface area and volume change the k value, so we recalculate k for each case and test each bathtub design with our simulation.

<!-- b000304 | heading | pages [18] -->
5.1 Varying Surface Area Under Constant Volume

<!-- b000305 | prose | pages [18] -->
The standard bathtub model has a volume of 25, 200 in3 (”Bathtub Sizes”), so we keep that volume constant while creating three other common bathtub designs. Using our model, we predict the

<!-- b000306 | prose | pages [18, 19] -->
Page 16 optimal ﬂow rate for following designs created using Autodesk Inventor, choosing ﬂow rates with the lowest total deviance from initial temperature.

<!-- b000307 | furniture | pages [19] -->
Team #54164

<!-- b000308 | furniture | pages [19] -->
Page 17 of 42

<!-- b000310 | prose | pages [19, 20] -->
Page 17 Standard bathtub model Dimensions (length x width x height): 60” × 30” × 14” Surface area: 1, 800 in2 Volume: 25, 200 in3 The standard bathtub model has a predicted optimal ﬂow rate of 1.81 gallons/minute and a deviance of 10.18◦C2.

<!-- b000311 | furniture | pages [20] -->
Team #54164

<!-- b000312 | furniture | pages [20] -->
Page 18 of 42

<!-- b000314 | prose | pages [20, 21, 22] -->
Page 18 Page 19 Circular bathtub model Dimensions (radius x height): 23.14” × 15” Surface area: 1, 680 in2 Volume: 25, 200 in3 The circular bathtub model has a predicted optimal ﬂow rate of 1.61 gallons/minute and a deviance of 7.86◦C2.

<!-- b000315 | furniture | pages [21] -->
Team #54164

<!-- b000316 | furniture | pages [21] -->
Page 19 of 42

<!-- b000318 | furniture | pages [22] -->
Team #54164

<!-- b000319 | furniture | pages [22] -->
Page 20 of 42

<!-- b000321 | prose | pages [22, 23, 24] -->
Page 20 Page 21 Triangular bathtub model Dimensions (side1 x side2 x side3 x height): 57.02” × 57.02” × 80.64” × 15.5” Surface area: 1, 625.81 in2 Volume: 25, 200 in3 The triangular bathtub model has a predicted optimal ﬂow rate of 1.95 gallons/minute and a deviance of 5.16◦C2.

<!-- b000322 | furniture | pages [23] -->
Team #54164

<!-- b000323 | furniture | pages [23] -->
Page 21 of 42

<!-- b000325 | furniture | pages [24] -->
Team #54164

<!-- b000326 | furniture | pages [24] -->
Page 22 of 42

<!-- b000328 | prose | pages [24, 25, 26] -->
Page 22 Page 23 Square bathtub model Dimensions (side x height): 39.69” × 16” Surface area: 1, 575 in2 Volume: 25, 200 in3 The square bathtub model has a predicted optimal ﬂow rate of 4.7 gallon- s/minute and a deviance of 1.20◦C2.

<!-- b000329 | furniture | pages [25] -->
Team #54164

<!-- b000330 | furniture | pages [25] -->
Page 23 of 42

<!-- b000332 | furniture | pages [26] -->
Team #54164

<!-- b000333 | furniture | pages [26] -->
Page 24 of 42

<!-- b000335 | heading | pages [26] -->
5.2 Varying Volume Under Constant Surface Area

<!-- b000336 | prose | pages [26] -->
We also investigated the eﬀect of volume on optimal ﬂow rate. We construct four designs of varying volumes while keeping surface area constant at 1600 in2. Using our model, we predict the optimal ﬂow rate for following designs, choosing ﬂow rates with the lowest total deviance from initial temperature.

<!-- b000337 | prose | pages [26, 27, 28] -->
Page 24 Page 25 Hemisphere bathtub model Dimensions (radius): 22.57” Surface area: 1, 600 in2 Volume: 24, 079.82 in3 The hemisphere bathtub model has a predicted optimal ﬂow rate of 1.58 gallons/minute and a deviance of 6.44◦C2.

<!-- b000338 | furniture | pages [27] -->
Team #54164

<!-- b000339 | furniture | pages [27] -->
Page 25 of 42

<!-- b000341 | furniture | pages [28] -->
Team #54164

<!-- b000342 | furniture | pages [28] -->
Page 26 of 42

<!-- b000344 | prose | pages [28, 29, 30] -->
Page 26 Page 27 Oval bathtub model Dimensions (rectLength x rectWidth x arcRadius x height): 50” × 23.4” × 11.7” × 15” Surface area: 1, 600 in2 Volume: 24, 000 in3 The oval bathtub model has a predicted optimal ﬂow rate of 1.6 gallons/minute and a deviance of 6.67◦C2.

<!-- b000345 | furniture | pages [29] -->
Team #54164

<!-- b000346 | furniture | pages [29] -->
Page 27 of 42

<!-- b000348 | furniture | pages [30] -->
Team #54164

<!-- b000349 | furniture | pages [30] -->
Page 28 of 42

<!-- b000351 | prose | pages [30, 31, 32] -->
Page 28 Page 29 Quarter-circle bathtub model Dimensions (radius x height): 45.14” × 14” Surface area: 1, 600 in2 Volume: 22, 400 in3 The quarter-circle bathtub model has a predicted optimal ﬂow rate of 1.41 gallons/minute and a deviance of 9.00◦C2.

<!-- b000352 | furniture | pages [31] -->
Team #54164

<!-- b000353 | furniture | pages [31] -->
Page 29 of 42

<!-- b000355 | furniture | pages [32] -->
Team #54164

<!-- b000356 | furniture | pages [32] -->
Page 30 of 42

<!-- b000358 | prose | pages [32, 33, 34] -->
Page 30 Page 31 Trapezoidal bathtub model Dimensions (topLength x topWidth x bottomLength x bottomWidth x height): 50” × 32” × 36” × 24” × 15” Surface area: 1, 600 in2 Volume: 18, 200 in3 The trapezoid bathtub model has a predicted optimal ﬂow rate of 2.15 gallons/minute and a deviance of 9.35◦C2.

<!-- b000359 | furniture | pages [33] -->
Team #54164

<!-- b000360 | furniture | pages [33] -->
Page 31 of 42

<!-- b000362 | furniture | pages [34] -->
Team #54164

<!-- b000363 | furniture | pages [34] -->
Page 32 of 42

<!-- b000365 | heading | pages [34] -->
5.3 Observations

<!-- b000366 | prose | pages [34] -->
We at ﬁrst expected to discover a consistently increasing or decreasing trend between volume and optimal ﬂow rate, and surface area and optimal ﬂow rate. However, as we increment surface area under constant volume, we note that the optimal ﬂow rate decreases, but then increases again, following no set pattern.

<!-- b000367 | prose | pages [34, 35] -->
Page 32 Similar ﬂuctuation occurs as we vary volume under constant surface area.

<!-- b000368 | furniture | pages [35] -->
Team #54164

<!-- b000369 | furniture | pages [35] -->
Page 33 of 42

<!-- b000371 | prose | pages [35, 36] -->
Page 33 While increasing surface area does understandably increase the rate of cooling, the changes in temperature at any given moment also change how much the incoming hot water heats the water. Because of this, we can’t reliably use a trend to predict what the optimal ﬂow rate is until we test the design with our simulation.

<!-- b000372 | furniture | pages [36] -->
Team #54164

<!-- b000373 | furniture | pages [36] -->
Page 34 of 42

<!-- b000375 | heading | pages [36] -->
5.4 Material of Bathtub

<!-- b000376 | prose | pages [36] -->
Although bathtubs are typically made with material that provides very eﬀective insulation, some tubs are made of less insulating material, such as ﬁberglass (”Bathtubs”). To test the impact of the insulating material on the rate of cooling, we can use our simulation with the total surface area of the tub instead of just the surface area of water exposed to the air. This is due to our global assumption that heat loss through heavily insulated surfaces is negligible, but heat loss through poorly insulated surfaces is equivalent to direct heat loss to surrounding air.

<!-- b000377 | prose | pages [36] -->
Using the standard bathtub model with ﬁberglass material, the total surface area is 6, 120 in2. However, only ﬁve of the sides are made with insulating material while the top is still exposed to the air. We assume the ﬁberglass material insulates 1 8 as well as acrylic material does. Diﬀerent builds of ﬁberglass will have diﬀerent insulation properties, so we select this one simply to show the eﬀect. To account for the insulation, we use an adjusted additional surface area of 2, 340 in2, which 8, added to the 1, 800 in2 of the exposed is the surface area of the ﬁve sides with a multiplier of 1

<!-- b000378 | prose | pages [36, 37] -->
Page 34 top surface. The volume is kept the same as the standard model at 25, 200 in3.

<!-- b000379 | furniture | pages [37] -->
Team #54164

<!-- b000380 | furniture | pages [37] -->
Page 35 of 42

<!-- b000382 | prose | pages [37] -->
The predicted optimal ﬂow rate is 7.52 gallons/minute, with a deviance of 1.92 ◦C2. The ﬂow rate of a tub made of ﬁberglass material is higher than the standard tub design created with acrylic material, which had a predicted optimal ﬂow rate of 1.81 gallons/minute and a deviance of 10.18 ◦C2. The increased ﬂow rate in less insulating material is expected, as the lower insulation results in greater heat loss over time.

<!-- b000383 | heading | pages [37] -->
5.5 Additives (bubble bath)

<!-- b000384 | prose | pages [37] -->
To address the last of our queries, we consider the eﬀects of adding a substance like bubble bath to the water.

<!-- b000385 | prose | pages [37] -->
Bubble bath solutions provide additional insulation to the water through the layer of bubbles on the surface of the water. The insulation decreases the rate of cooling of the water. The amount of insulation provided by the bubble bath is dependent on the speciﬁc type of bubble bath, the amount of bubble bath used, etc. Thus we choose a particular insulation value of bubble bath as example. We assume the bubble bath has an insulation factor of .95, and so account for the insulation by multiplying the surface area of the water exposed to air by the insulation factor, to get a surface area of 1, 710 in2.

<!-- b000386 | prose | pages [37] -->
Using this value for surface area in our simulation and the standard volume of 25, 200 in3, we obtain a predicted ﬂow rate of 1.58 gallons/minute and a deviance of 8.75 ◦C2. The origi- nal standard bathtub model without bubble bath additive had a predicted optimal ﬂow rate of 1.81 gallons/minute and a deviance of 10.18 ◦C2.

<!-- b000387 | prose | pages [37] -->
The ﬂow rate with bubble bath additive decreased, which is expected as the layer adds insulation and reduces the rate of cooling.

<!-- b000388 | prose | pages [37] -->
Page 35

<!-- b000389 | furniture | pages [38] -->
Team #54164

<!-- b000390 | furniture | pages [38] -->
Page 36 of 42

<!-- b000391 | heading | pages [38] -->
6 Conclusion

<!-- b000392 | heading | pages [38] -->
6.1 Results

<!-- b000393 | prose | pages [38] -->
For a standard bathtub 60” × 30” × 14” in size in a room of temperature 21◦C, we suggest for the person to turn the faucet to a ﬂow rate of 1.81 gallons/minute.

<!-- b000394 | heading | pages [38] -->
6.2 Strengths of Model

<!-- b000395 | prose | pages [38] -->
• Our model is able to accurately and retroactively determine the temperature cooling of a relatively large body of water, and was conﬁrmed by the data in our experiment in Appendix A.

<!-- b000396 | prose | pages [38] -->
• Our model is also able to conclusively produce a speciﬁc numerical optimal ﬂow rate given parameters of the standard bathtub, using the deviance rating.

<!-- b000397 | prose | pages [38] -->
• Additionally, our model is able to accommodate bathtubs of diﬀerent shapes and dimensions, given their surface areas and volumes, as well as other materials and additives.

<!-- b000398 | heading | pages [38] -->
6.3 Limitations of Model

<!-- b000399 | prose | pages [38] -->
Many assumptions were necessary to simplify the problem enough so that it could be tackled.

<!-- b000400 | prose | pages [38] -->
• Firstly, our model assumes that the strategy provided in ”A Simple Solution” ensures that the water heats perfectly evenly and instantaneously. In reality, unless the person is extremely skilled at wading the water, the temperature of the water will still not be exactly the same at every point in the bathtub, ﬂuctuating due to convection currents.

<!-- b000401 | prose | pages [38, 39] -->
Page 36 • Secondly, the ambient room temperature is assumed to remain constant, but in reality, the ambient temperature should also increase as a result of the heat loss from the water, but to model this requires consideration of other external factors including the dimensions of the room and any possible air currents.

<!-- b000402 | furniture | pages [39] -->
Team #54164

<!-- b000403 | furniture | pages [39] -->
Page 37 of 42

<!-- b000405 | prose | pages [39] -->
• The strategy we suggest has the user ﬂailing his arms constantly throughout the duration of the bath; in reality this is not plausible given that a bath is meant to be a relaxing experience.

<!-- b000406 | prose | pages [39] -->
We address this issue more closely in ”Future Work.”

<!-- b000407 | heading | pages [39] -->
6.4 Future Work/Discussion

<!-- b000408 | prose | pages [39] -->
Much work has already been done in an eﬀort to keep bath water from cooling over time. Be- sides heat-preserving ﬁlms like bubble bath, there even exists a ”Water Blanket” product that insulates the top surface of the bathtub to reduce heat loss (”Water Blanket”). Such a product is understandably a reasonable investment for one who wants to keep his bath water hotter for longer.

<!-- b000409 | prose | pages [39] -->
But we can do better.

<!-- b000410 | prose | pages [39] -->
The glaring issue with our strategy is that nobody wants to swirl their arms for his entire bath time. Even with a product like the ”Water Blanket,” hot water will still rise to the top of the bath and the bottom of the bathtub will have disproportionately cooler water.

<!-- b000411 | prose | pages [39] -->
We decided to lay out a prototype design of our own original invention theorized during this MCM competition, a cost-eﬃcient product that will keep the temperature on the bottom of the tub as hot as the top. This product also doubles as a converter from standard bathtub to Jacuzzi-esque hot tub with water jets.

<!-- b000412 | heading | pages [39] -->
6.5 Home Jacuzzi

<!-- b000413 | prose | pages [39] -->
The following constructions were rendered using Autodesk Inventor.

<!-- b000414 | caption | pages [39] -->
Figure 2: A blueprint of the dimensions for our product.

<!-- b000415 | prose | pages [39] -->
Our product is a low-tech tubing that connects to the faucet of any standard bathtub and, at this stage of development, ﬁts the dimensions of the standard bathtub.

<!-- b000416 | prose | pages [39, 40, 41] -->
Page 37 Page 38 The water from the faucet then ﬂows out not directly down into the tub, but instead through the tube and out the horizontal holes, heating the bottom of the tub before the top. The hot water from the bottom then rises to the top, as in any bathtub. This counteracts the loss of heat at the surface of the tub to equalize the temperature in the tub.

<!-- b000417 | furniture | pages [40] -->
Team #54164

<!-- b000418 | furniture | pages [40] -->
Page 38 of 42

<!-- b000419 | caption | pages [40] -->
Figure 3: The product.

<!-- b000420 | caption | pages [40] -->
Figure 4: Our product in use with a standard bathtub.

<!-- b000422 | furniture | pages [41] -->
Team #54164

<!-- b000423 | furniture | pages [41] -->
Page 39 of 42

<!-- b000425 | prose | pages [41] -->
The jets of water exiting the holes also create the eﬀect of Jacuzzi jets without the high costs of installing actual Jacuzzi jets.

<!-- b000426 | heading | pages [41] -->
Appendices

<!-- b000427 | prose | pages [41] -->
A Experimental Design for Real-World Bathtub Data

<!-- b000428 | prose | pages [41] -->
Materials

<!-- b000429 | prose | pages [41] -->
• Bathtub in the shape of a rectangular prism, insulated on ﬁve faces and exposed to the air on the top surface

<!-- b000430 | prose | pages [41] -->
• Thermometer

<!-- b000431 | prose | pages [41] -->
Procedure First, we use the thermometer to record the ambient temperature of the room in Celsius. We also record the dimensions of the bathtub, calculating surface area and volume. We turn on the faucet to the max heat setting and ﬁll the tub to its volume capacity. When this is done, we use the thermostat to record the initial temperature of the water in the tub. From then on, we record the temperature again once every minute for 60 minutes. The independent variable was time, while the dependent variable was temperature of the water in Celsius.

<!-- b000432 | prose | pages [41] -->
Data Ambient room temperature = 21◦C Dimensions of bathtub = 55 × 23 × 13 , which yields a volume of 16, 455 in3 and a surface area of 1265 in2.

<!-- b000433 | prose | pages [41] -->
The rest of the data is included in the body of the paper as a graph.

<!-- b000434 | prose | pages [41] -->
B Simulation Code

<!-- b000435 | prose | pages [41] -->
#!/ usr / bin /python

<!-- b000436 | prose | pages [41] -->
import logging import math import os import sys import time

<!-- b000437 | prose | pages [41] -->
import pygal

<!-- b000438 | prose | pages [41] -->
i f len ( sys . argv ) < 3:

<!-- b000439 | prose | pages [41] -->
print ”Usage : %s <surface area> <volume>” % sys . argv [ 0 ]

<!-- b000440 | prose | pages [41, 42] -->
Page 39 print ” where surface area i s in square inches ” print ” and volume i s in cubic inches ” sys . e x i t (1)

<!-- b000441 | furniture | pages [42] -->
Team #54164

<!-- b000442 | furniture | pages [42] -->
Page 40 of 42

<!-- b000444 | prose | pages [42] -->
s u r f a c e a r e a = float ( sys . argv [ 1 ] ) volume = float ( sys . argv [ 2 ] ) filename = ”SA%s V%s ” % ( int ( s u r f a c e a r e a ) , int ( volume )) points = [ ]

<!-- b000445 | prose | pages [42] -->
BATH DURATION = 40 INITIAL TEMPERATURE = 37 HOTWATERTEMPERATURE = 48 ROOMTEMPERATURE = 21 volume ∗1.0 / AREA, HEIGHT = surface area , s u r f a c e a r e a

<!-- b000446 | prose | pages [42] -->
l o g d i r = ” logs ” outdir = ”output” for f o l d e r in [ logdir , outdir ] :

<!-- b000447 | prose | pages [42] -->
i f not ( os . path . e x i s t s ( f o l d e r ) and os . path . i s d i r ( f o l d e r ) ) :

<!-- b000448 | prose | pages [42] -->
os . mkdir ( f o l d e r )

<!-- b000449 | prose | pages [42] -->
def d e f a u l t l o g g e r (msg ) :

<!-- b000450 | prose | pages [42] -->
print ”[%( time ) s ] %(msg) s ” % { ”time” : time . asctime () ,\ ”msg” : msg }

<!-- b000451 | prose | pages [42] -->
def l o g t o f i l e ( filename ) :

<!-- b000452 | prose | pages [42] -->
def func (msg ) :

<!-- b000453 | prose | pages [42] -->
fout = open( filename , ”a+” ) fout . write ( ”%s \n” % ( ”[%( time ) s ] %(msg) s ” % \ { ”time” : time . asctime () , ”msg” : msg })) fout . c l o s e () return func

<!-- b000454 | prose | pages [42] -->
def room cool ( temperature , frame ) :

<!-- b000455 | prose | pages [42] -->
VOLUME = AREA ∗HEIGHT ∗0.0163871 SURFACE AREA = AREA ∗0.00064516 K = 0.385387190197681 ∗math . e ∗∗( −0.167081937857622 \ ∗pow(pow(VOLUME, 2) / pow(SURFACE AREA, 3) , 1.0 / 3))

<!-- b000456 | prose | pages [42] -->
dT = −1 ∗K ∗( temperature −ROOMTEMPERATURE) ∗60

<!-- b000457 | prose | pages [42] -->
return dT

<!-- b000458 | prose | pages [42] -->
def water heat ( temperature , f lo w r a t e ) :

<!-- b000459 | prose | pages [42] -->
Cp = 4.179 # s p e c i f i c heat of water ∗3785.4118 # mass ( g ) flow rate mass = f l o w r a t e of water

<!-- b000460 | prose | pages [42, 43] -->
Page 40 tub mass = AREA ∗HEIGHT ∗16.3870640693 # mass ( g ) of tub

<!-- b000461 | furniture | pages [43] -->
Team #54164

<!-- b000462 | furniture | pages [43] -->
Page 41 of 42

<!-- b000464 | prose | pages [43] -->
dT = flow rate mass ∗(HOTWATERTEMPERATURE −temperature ) \ / tub mass

<!-- b000465 | prose | pages [43] -->
return dT

<!-- b000466 | prose | pages [43] -->
def run simulation ( f l o w r a t e =1, log=d e f a u l t l o g g e r ) :

<!-- b000467 | prose | pages [43] -->
frame = 0 deviance = 0.0 temperature = INITIAL TEMPERATURE WATER RUNNING = False

<!-- b000468 | prose | pages [43] -->
while frame < BATH DURATION:

<!-- b000469 | prose | pages [43] -->
dT cool = room cool ( temperature , frame ) temperature += dT cool abs( temperature −INITIAL TEMPERATURE) > 1.4 \ i f and not(WATER RUNNING) :

<!-- b000470 | prose | pages [43] -->
WATER RUNNING = True \ dT heat = water heat ( temperature , f lo w r a t e ) i f WATER RUNNING else 0 temperature += dT heat i f WATER RUNNING:

<!-- b000471 | prose | pages [43] -->
E1 = INITIAL TEMPERATURE E2 = temperature deviance += (INITIAL TEMPERATURE \ −temperature ) ∗∗2 frame += 1

<!-- b000472 | prose | pages [43] -->
return deviance

<!-- b000473 | prose | pages [43] -->
−1): for x in range (1600 , 1 , f l o w r a t e = x / 100.0 log = l o g t o f i l e ( ” logs /” + filename + ” . log ” ) deviance = run simulation ( f l o w r a t e=flow rate , log=log ) points . append (( flow rate , deviance ))

<!-- b000474 | prose | pages [43] -->
minimum = (9999999 , 9999999) for point in points :

<!-- b000475 | prose | pages [43] -->
x , y = point minx , miny = minimum i f y < miny :

<!-- b000476 | prose | pages [43] -->
minimum = (x , y)

<!-- b000477 | prose | pages [43] -->
l o g t o f i l e ( ” logs /” + filename + ” . log ” )( ”minimum : %s ” % str (minimum))

<!-- b000478 | prose | pages [43, 44] -->
Page 41 chart = pygal .XY( stroke=True ) chart . t i t l e = ”Optimal Flow Rate (SA: %s , V: %s ) ” % \ ( int ( s u r f a c e a r e a ) , int ( volume )) chart . x t i t l e = ”Flow Rate (GPM) ” chart . y t i t l e = ”Deviance” chart . add ( ”Bathtub” , points ) [{ ” value ” : minimum , } ] ) chart . add ( ”Minimum” , ” l a b e l ” : str (minimum) chart . render to png ( ”output/” + filename + ” . png” )

<!-- b000479 | furniture | pages [44] -->
Team #54164

<!-- b000480 | furniture | pages [44] -->
Page 42 of 42

<!-- b000482 | prose | pages [44] -->
sys . e x i t (0)

<!-- b000483 | heading | pages [44] -->
References

<!-- b000484 | references | pages [44] -->
[1] ”5 Reasons You Need To Take A Bath Tonight (No Matter How Busy You Are).” Prevention.

<!-- b000485 | references | pages [44] -->
N.p., n.d. Web. 31 Jan. 2016.

<!-- b000486 | references | pages [44] -->
[2] A.O. Smith Corporation. ”TEMPERATURE ADJUSTMENT - RESIDENTIAL ELECTRIC.”

<!-- b000487 | references | pages [44] -->
(n.d.): n. pag. Web. 31 Jan. 2016. ¡http://www.hotwater.com/lit/bulletin/bulletin31.pdf¿.

<!-- b000488 | references | pages [44] -->
[3] ”Bathtub Faucets.” Faucet.com. N.p., n.d. Web. 01 Feb. 2016.

<!-- b000489 | references | pages [44] -->
[4] ”Bathtub Material Review by Bathtub Experts.” Select the Right Bathtub Material. N.p., n.d.

<!-- b000490 | references | pages [44] -->
Web. 31 Jan. 2016.

<!-- b000491 | references | pages [44] -->
[5] ”Bathtub Sizes. Standard Bathtub Dimensions.” Bathtub Sizes. Standard Bathtub Dimensions.

<!-- b000492 | references | pages [44] -->
N.p., n.d. Web. 31 Jan. 2016.

<!-- b000493 | references | pages [44] -->
[6] ”Bathtubs.” Buying Guide: at The Home Depot. N.p., 06 Sept. 2013. Web. 01 Feb. 2016.

<!-- b000494 | references | pages [44] -->
[7] Davies, S N et al. “Facial Sensitivity to Rates of Temperature Change: Neurophysiological

<!-- b000495 | references | pages [44] -->
and Psychophysical Evidence from Cats and Humans.”The Journal of Physiology 344 (1983):

<!-- b000496 | references | pages [44] -->
161–175. Print.

<!-- b000497 | references | pages [44] -->
[8] Gieseking, Elizabeth. ”Newton’s Law of Cooling: An Experimental Investigation.” Jim Wilson,

<!-- b000498 | references | pages [44] -->
n.d. Web. 31 Jan. 2016.

<!-- b000499 | references | pages [44] -->
[9] ”Other Diﬀerential Equations.” Newton’s Law of Cooling. N.p., n.d. Web. 31 Jan. 2016.

<!-- b000500 | references | pages [44] -->
[10] ”Water Blanket.” Aquablanket. N.p., n.d. Web. 31 Jan. 2016.

<!-- b000501 | references | pages [44] -->
Page 42
