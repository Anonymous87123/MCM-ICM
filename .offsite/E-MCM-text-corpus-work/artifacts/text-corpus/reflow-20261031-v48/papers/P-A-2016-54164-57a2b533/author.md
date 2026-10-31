Abstract

We present a user-friendly strategy for keeping the water in a bathtub as close as possible to a certain preferred temperature. This strategy consists in two main constituents: adjusting the hot water flow from the faucet to keep the bathtub temperature suitably high, and using hand motions to distribute the heat evenly throughout the bath water.

As for determining the necessary water flow, we first create a model that determines the temperature of the bath water at any point in time. We posit that the temperature of the water in the bath is dependent on the cooling due to the ambient temperature of the room, which obeys the proportionality given by Newton’s Law of Cooling; and the heating due to the added hot water from the faucet. Our model combines the temperature changes over time from these two entities into one consummate differential equation.

We determine the experimental constant of proportionality for Newton’s Law of Cooling by proposing that this constant itself is dependent on a combination of volume of the water and surface area exposed to the air. Taking experimental data from varied sources, including an experiment we conducted and documented over the time frame of the MCM competition, we were able to extrapolate values for the constant attributable to any bathtub given its volume and surface area exposed to air.

We then run a computer simulation to model the temperature changes over time in a standard bathtub with our differential equation, determining how much hot water needs to flow in to keep the total deviance over time of the temperature of the bath from a desired temperature at a minimum. We found the optimal flow rate for a standard bathtub at standard conditions to be 1.81 gallons/minute, or about 11% of the maximum flow rate.

Our model was able to predict optimal flow rates for many different combinations of volume, surface area, tub material, and additives. We found that more effective insulating materials led to lower optimal flow rates (less hot water needed), as did the addition of additives. Volume and surface area, surprisingly, showed no clear trend.

As for keeping the temperature roughly even in the bathtub, we suggest that the user swirl his hands counter-clockwise with respect to the faucet as shown in Figure 1. This is a simple yet effective way to distribute the heat acceptably evenly throughout the tub water.

As alternatives for those who do not wish to make their bath into an exercise session, we invented an original product (Home Jacuzzi) that is low-cost and aids in heating the water evenly.

1 Abstract

We present a user-friendly strategy for keeping the water in a bathtub as close as possible to a certain preferred temperature. This strategy consists in two main constituents: adjusting the hot water ﬂow from the faucet to keep the bathtub temperature suitably high, and using hand motions to distribute the heat evenly throughout the bath water.

As for determining the necessary water ﬂow, we ﬁrst create a model that determines the temperature of the bath water at any point in time. We posit that the temperature of the water in the bath is dependent on the cooling due to the ambient temperature of the room, which obeys the proportionality given by Newton’s Law of Cooling; and the heating due to the added hot water from the faucet. Our model combines the temperature changes over time from these two entities into one consummate diﬀerential equation.

We determine the experimental constant of proportionality for Newton’s Law of Cooling by proposing that this constant itself is dependent on a combination of volume of the water and surface area exposed to the air. Taking experimental data from varied sources, including an experiment we conducted and documented over the time frame of the MCM competition, we were able to extrapolate values for the constant attributable to any bathtub given its volume and surface area exposed to air.

We then run a computer simulation to model the temperature changes over time in a standard bathtub with our diﬀerential equation, determining how much hot water needs to ﬂow in to keep the total deviance over time of the temperature of the bath from a desired temperature at a minimum. We found the optimal ﬂow rate for a standard bathtub at standard conditions to be 1.81 gallons/minute, or about 11% of the maximum ﬂow rate.

Our model was able to predict optimal ﬂow rates for many diﬀerent combinations of volume, surface area, tub material, and additives. We found that more eﬀective insulating materials led to lower optimal ﬂow rates (less hot water needed), as did the addition of additives. Volume and surface area, surprisingly, showed no clear trend.

As for keeping the temperature roughly even in the bathtub, we suggest that the user swirl his hands counter-clockwise with respect to the faucet as shown in Figure 1. This is a simple yet eﬀective way to distribute the heat acceptably evenly throughout the tub water.

As alternatives for those who do not wish to make their bath into an exercise session, we invented an original product (Home Jacuzzi) that is low-cost and aids in heating the water evenly.

1.1 Non-Technical Explanation

Why is it so diﬃcult to keep the temperature of the water even throughout when taking a bath? In a standard single-faucet bathtub, hot water comes out of the faucet on only one side of the bath, leaving the other side of the bath colder until enough time passes for the temperature to even out. When left running, this might take more time than a user wants to wait for.

To further complicate things, hot water is also slightly less dense than cold water, and will thus be more concentrated on the surface of the bathtub than the bottom of the tub.

To make the temperature consistent, the easiest solution is to cup your hands and circulate the hot water from the side with the faucet to the other side of the tub, and also circulate the hot water from the water surface to the bottom of the top.

Another option, however, for those of us who don’t want to spend the duration of our bath ﬂailing our arms, is to use our invention, ”Home Jacuzzi.” Our invention spans the length and width of the bathtub, and attaches onto the faucet. The hot water from the faucet is then funneled through the device towards the bottom of the tub, creating a Jacuzzi-like eﬀect. The hot water then rises to the surface, mixing with the water above it and creating an evenly distributed, uniform temperature throughout the tub.

Now that we can keep the temperature consistent throughout the tub, we’re still left to ﬁgure out how high we should turn our faucet to keep the water from going cold.

Of course, turning it too high is a waste of water and, on top of that, can increase the temperature to uncomfortably high levels. Too low, and we get to wade around in lukewarm to cold waters that make us not want to take a bath at all. So we want to ﬁnd the optimal ﬂow rate on our faucet that gets our temperature to where we want it to be.

Not all bathtubs were created equal. The optimal ﬂow rate isn’t a set rate for all bathtubs. For the standard 60”x30”x14” bathtub, we suggest turning the faucet up to about a ninth of its max.

To conserve even more hot water, you even have the option of purchasing products like the ”Water Blanket” (”Water Blanket”) to keep the temperature of the bath warmer. Interestingly enough, even bubble bath can keep your bath water hotter for longer. And no, it’s not ”just for kids.”

6 Conclusion

36 6.1 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 6.2 Strengths of Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 6.3 Limitations of Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 6.4 Future Work/Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 6.5 Home Jacuzzi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

Appendices

39

A Experimental Design for Real-World Bathtub Data 39

B Simulation Code 39

2 Introduction

2.1 Background

Baths, the best way we had to cleanse ourselves–until we became teens and discovered showers, at which point baths became ”uncool.” Yet, whenever we want to slow life down and relax a little, we can rest assured that the bath will always be there to ease our nerves. The health beneﬁts of taking a bath are plentiful (”5 Reasons You Need To Take A Bath”), but no one wants to hop into a steaming hot tub only to ﬁnd him or herself in cold or lukewarm water a half-hour later. Then, how can one keep a bath warm long enough to last a preferred duration? Most people own simple bathtubs, unequipped with secondary heating systems or circulating jets. Several factors can aﬀect the temperature change of bath water, including:

• the surface area of water exposed to air

• the volume of water that is being cooled

• the surrounding air temperature

• the rate of hot water ﬂow into the bathtub

• the material the bathtub is made out of (and how well it is able to provide insulation)

• whether any additives are introduced to the water, such as a bubble bath solution

2.2 Restatement of Problem

A person has settled into a bathtub for a long, relaxing bath, only to ﬁnd that after some time, the water has become noticeably cooler. In an attempt to salvage his satisfaction, he elects to turn on the faucet and let in some hot water to bring the temperature back up. Excess tub water leaves the tub through an overﬂow drain. Of course, he runs into a set of issues:

Page 3 • The water in the tub is of inconsistent temperature, being hotter in some areas and cooler in others.

• Turning the hot water ﬂow too high is a waste of water (and money).

3 The Strategy

Our ”strategy” presented to the person in the tub will be a combination of the solutions to queries 1 and 2—the person will have to take action to evenly distribute the heat in the bathtub water, and the person will have to set the hot water ﬂow in at a certain ﬂow rate to keep the bathtub water hot.

3.1 Distribution: A Simple Solution

We begin by addressing query number ”1”. In a standard single-faucet bathtub, water ﬂows from above on one side of the bathtub. Since hot water rises, more heat will be concentrated at the top of the bathtub. Because the faucet is only on one side of the tub, more heat will be concentrated on the side of the tub closest to the faucet. Therefore, we advise the person in the tub to cup his hands and make circles in the water as illustrated below:

3.2 Global Assumptions

• The standard bathtub is open and exposed to the air on the top surface, and built with acrylic material that is heavily insulated (”Bathtub Sizes”).

• Heat loss through heavily insulated surfaces is negligible.

• Heat loss through surfaces of poor insulation (thin glass, thin ﬁberglass) behaves as if that surface was directly exposed to air.

• The person in the bathtub follows the suggestion in Figure 1, allowing us to assume that water temperature is consistent throughout the tub at any point in time.

Page 4 • The temperature sensitivity of the human body is such that we begin noticing appreciable diﬀerences in temperature at ±1.4◦C from the original temperature (Davies et al. 171)

• The target temperature for the bath water is human body temperature, which is approxi- mately 37◦C.

• Since the person inside the tub is at thermal equilibrium with the water in the tub, we can treat the person’s body as an extension of the bathtub water.

• Room temperature remains constant throughout the duration of the bath, at 21◦C, the ac- cepted value for ambient room temperature.

• The faucet from which the hot water ﬂows has a maximum ﬂow rate of 16 gallons/min (”Bathtub Faucets”), and the person is able to toggle the faucet’s ﬂow rate to any rate between 0 gallons/min and 16 gallons/min.

• The hottest water we can release from the faucet has a temperature of 48◦C to prevent injury from scalding (A.O. Smith Corporation 1). This will be the assumed temperature of the additional water from the faucet.

• All bathtubs used in this paper for simulation and data are ﬁlled to the brim with the com- bination of water and person.

4 Simulating Heat Transfer

To address our second query, we consider a thermodynamic system of ﬁve constituents: the water in the tub, the water entering and leaving the tub, the walls of the tub, the human in the tub, and the air outside the tub. Heat transfer with the human and the walls is negligible as justiﬁed in our global assumptions. Thus, we need only consider the cooling of the tub water due to the air outside, and the heating of the tub water due to the incoming hot water.

4.1 Local Assumptions

• The industry standard bathtub in America is 60” × 30” × 14”, which results in a volume of 60×30×14 = 25, 200in3 and surface area exposed to the air of 60×30 = 1, 800in2 (”Bathtub Sizes”).

• Since the majority of bathtubs in America are insulated, we assume that the bathtub that we are simulating is well insulated on all sides except for the top. Therefore, heat can only escape from the bathtub from the top surface.

• Water cooling obeys Newton’s Law of Cooling closely enough to approximate a model for temperature over time.

• The ambient temperature is 21◦C.

• The temperature of the hot water from the faucet is 48◦C.

Page 5

4.1.1 Variable Nomenclature

Below are the variables used throughout our model:

• k = cooling constant

• T = temperature of the water minus ambient room temperature

• T0 = initial temperature of the bathtub

• t = time in minutes

• SAE = surface area exposed to air in square meters

• V = volume in liters

• Q = change in heat energy, in joules

• m = mass of the water in the tub, in grams

• Cp = speciﬁc heat of the water, in Joules per gram-degree ◦C

4.2 Creation of the Model

Since the temperature of the water is constantly being altered by the cooling due to the surrounding air temperature and the heating due to the incoming water ﬂow, we created an equation to model the changes in temperature, based on Newton’s Law of Cooling and the speciﬁc heat capacity formula.

4.2.1 Cooling

The ﬁrst part of the model accounts for the cooling of the water due to the temperature of the environment. We chose to model this cooling with Newton’s Law of Cooling, which states that the diﬀerence in temperature is directly proportional to the negative of the current temperature, or

dT dt = −kT (1)

where T is the temperature, and k is the cooling constant that is derived from experimentation. To derive the form we want our regression equation for our experimental data to be in, we solve our diﬀerential equation by integration with separation of variables:

1 T dT = −kdt (2)

1 Z Z −kdt T dT = (3)

ln(T) = −kt + C (4)

where C is a constant. Solving for T,

T = e−kt+C = Ce−kt (5)

Page 6 To solve for this constant of integration, C, we substitute in the initial temperature T0 of the water at time t = 0.

T0 = Ce−k×0 = C × 1 (6)

giving us the regression equation form

T = T0e−kt (7)

Since k is dependent on the sum of physical conditions in each speciﬁc scenario, it can only be derived from experimental data. Then, to predict the value of k for our industry standard bathtub, we take sets of experimental data and analyze trends between them to extrapolate a value of k for our purposes.

4.2.2 Experimental Data

We created a graph to represent the data we found for temperature over time in 100mL, 300mL, and 800mL volumes of water (Gieseking). The ambient room temperature in this setting was 23◦C. We realized that it is wrong to model these data with exponential regressions that have horizontal asymptotes at 0◦C. Instead, since logically the temperature of the water should approach—but

Page 7 never dip below—the room temperature, we create exponential regressions with horizontal asymp- totes at 23◦C instead. The easiest way to do this is to subtract 23◦C from all points for the purpose of regression, and then modifying the regression equation to account for the diﬀerence. The results are as follows:

The resulting equations are:

y = 77e−0.029x + 23 (8) y = 77e−0.036x + 23 (9) y = 77e−0.052x + 23 (10)

for the 100mL beaker, 300mL beaker, and the 800mL beaker, respectively. Note that 23◦C has been added to each equation to account for the shift.

It’s unreasonable to hope that data from small beakers alone can accurately predict the tem- perature changes in a large bathtub. However, we could not ﬁnd any accessible experimental data for large volumes of water. This is likely due to the fact that when studying water cooling, most scientists will choose to use small quantities of water for convenience. Since it was diﬃcult to obtain large-scale water cooling data, we performed our own experiment with a bathtub to obtain a k-value that pertains to our model. The procedure of our experiment can be found in Appendix A.

The results of our experiment are as follows:

Page 8 The regression equation for our bathtub temperature versus time, then, is

which means our experimental k per minute is 0.00448 = 0.000075. However, this k was only 60 relevant to our speciﬁc bathtub. In order to ﬁnd k-values for bathtubs of varied volume and surface area, we needed to create a model for k.

We consider that there is a relationship between k and exposed surface area (SAE) and volume (V ). Reasoning through the fact that k is to be a constant, we assumed that k should be unitless.

V 2 Thus, when relating k to V and SAE, k should be dependent on a power of E to cancel the units SA3 of meters in the numerator and denominator.

The calculations for SAE must take into account the fact that bathtubs are heavily insulated on ﬁve of six faces, but beakers are not. The eﬀective SAE of the bathtub, then, is its top surface’s area, or 55 × 23 = 1, 265 in2. The eﬀective SAE of the beakers are their total surface area, because of our assumption that thin glass provides virtually no insulation. Then, their SAE is given by:

Page 9 SAcylinder = 2πr2 + πrh (11)

where r is the radius of the beaker and h is the height of the water in the beaker. Because the beakers were not ﬁlled in the experiments, we recalculate the eﬀective heights with the following relationship:

h = hbeaker × Vwater (12) Vbeaker giving us a surface area equation for the beakers of

SAcylinder = 2πr2 + rhbeaker × Vwater (13) Vbeaker V 2 Below is a table of V , SAE, E , and k values for our four data sets. SA3 SAE (m) V (L) k 0.052150438 0.8 0.026259385 0.030787608 0.3 0.030316642 0.015707963 0.1 0.040508908 0.8161274 269.48527 0.000075 V 2 Proceeding, we test an exponential regression on the four sets of data relating k to E . First SA3 V 2 we tested E , SA3

which gave us an R2 value of 0.99764. We then test ( V 2 E )2 SA3

Page 10 which gave us an R2 value of 0.996529. Seeing as this is worse, we test q V 2 E , SA3

which gave us an R2 value of 0.999294. Noticing improvement, we test 3q V 2 E , noting a possible SA3 connection between the three dimensions our heat transfer acts in, and the third-degree root we V 2 take on our E , SA3

Page 11 which gives us the regression equation:

r V 2 −0.1670819378576223 3 SA3 k = 0.385387190197681e (14) E

This model ﬁt the data with an accuracy of R2 = 0.99929854436231100000, which was even bet- ter than the previous attempts. Using this model for k, we predict a k-value of 0.385387190197681 for our standard 60” × 30” × 14” bathtub. Thus, our ﬁnal equation for the change in temperature due to the environment is

dT dt = −0.385387190197681T (15)

4.2.3 Heating

The second part of the model calculates the amount of heat added by the person as he turned on the water faucet to a certain ﬂow rate. To achieve this, we used the speciﬁc heat capacity formula, which is

∆Q = mCpT (16)

where ∆Q is the change in heat, m is mass, Cp is the speciﬁc heat capacity of water, and T is the change in temperature. There are two instances of heat change resulting from the addition of hot water: heat is being added through the addition of hot water from the faucet, and heat is being removed through the drainage of excess water. The heat contributed by the water ﬂowing in is given by the following equation:

Q1 = dm dt CpThot (17)

where Q1 is the heat from the water ﬂowing in, dm dt is the mass ﬂow rate of the water ﬂowing in, and T is the absolute temperature of the water ﬂowing in (Kelvins).

Page 12 The heat lost from excess water drainage is given by the following equation:

Q2 = dmlost CpTlost (18) dt dmlost where Q2 is the heat from the water draining out, is the mass ﬂow rate of the water dt draining out, and Tlost is the absolute temperature of the water draining out (Kelvins). By our global assumption that temperature is consistent throughout the tub, we have that Tlost is simply the temperature of the tub, T.

Because the volume of water ﬂowing in at any point in time is equivalent to the volume of water ﬂowing out due to overﬂow, the mass ﬂow rate out is equal to the mass ﬂow rate in, or dmlost = dm dt . Then, the heat change of the water in the tub can be obtained by subtracting the dt above two equations:

∆Q = dm dt Cp(Thot −T) (19)

We also have that

∆Q = mtubCpTtub (20)

Since ∆Q is common to both equations, we can substitute the expression dm dt Cp(Thot −T) for ∆Q in the second equation and solve for Ttub, which becomes:

4.3 Simulation Design

All that is left now is to combine the cooling and heating of the water to simulate the overall temperature change.

In order to simulate the cooling of the water when the person has not turned on the faucet, we use the Newton’s law diﬀerential obtained earlier:

dT dt = −0.385387190197681T (21)

And to simulate the change in temperature due to the addition of hot water, we add the equation obtained in the previous section to the above:

dT dt = −0.385387190197681T + dm dt (Thot −T)mtub (22)

We used a computer program written in Python (code included in Appendix B) to simulate the change in temperature of the bathtub according to the diﬀerential equation over a period of 40 minutes. All units are converted to standard SI units in the simulation. The simulation accounts for the loss of heat to the environment, as well as the heating of the water due to the person operating the faucet. In order to achieve this, we set up a loop to run the simulation between time t = 0 minutes to t = 40 minutes, what we assumed to be the end of the bath. During each one-minute ”frame” in this interval, we calculated the new temperature of the water using the previous temperature with the two equations for change in temperature per minute calculated in the previous section.

The simulation will begin by applying the ﬁrst equation to the temperature of the water every frame, since the hot water faucet is initially oﬀ. When the temperature of the water reaches a

Page 13 noticeably cooler temperature (of 1.4◦C below its initial temperature), the person will turn on the hot water, and the simulation will no longer apply the ﬁrst equation, but instead the second equation, in order to account for the temperature gained from the hot water.

4.3.1 Selecting Optimal Flow Rate

In order to evaluate the results for the various ﬂow rates, we used the deviance value, obtained by ﬁnding the sum of the squares of the diﬀerences between the ”current” temperature and the initial temperature every frame:

N X (xn −¯x)2 ∆total = (23) n Comparing the deviance of every ﬂow rate produces the following:

Now, selecting the optimal ﬂow rate is trivial. Since the optimal ﬂow rate is characterized by the least diﬀerence from the original temperature, it is represented by the point indicated at the bottom of the graph, at (1.81, 10.179381314125882). This means that our optimal ﬂow rate to be recommended to the person is 1.81 gallons/minute, which results in a total deviance of 10.179 from the original temperature of his bath. The following is a temperature vs. time graph of the simulation using the optimal ﬂow rate of 1.81 gallons per minute. Note that the curve initially decreases, as the temperature of the water is only aﬀected by the cooler temperature of the room. However, once the temperature of the water has dropped below 1.4◦C from the initial temperature of 37◦C, the person turns on the hot water faucet which begins to increase the temperature of the water.

Page 14 Page 15

4.3.2 Validation of Model

To conﬁrm that our cooling simulation accurately models what occurs in the real world, we ran the simulation on the circumstances of our real-world experiment in Appendix B. Fitting the temperatures predicted by the simulation to the actual experimentally obtained data, we ﬁnd that the simulation is able to very accurately predict the temperatures at given points in time retroactively.

As a matter of fact, this diﬀerential simulation is even more accurate than the previous regression model we had obtained for the data:

y = 16e−0.00448x + 21 (24)

as that regression led to an R-squared value of 0.97326, and the simulation gave an R-squared value of 0.999836.

While the relationship between temperature and time in this graph appears to be linear, it is still exponential–the very small k-value is what makes it appear linear. Indeed, there is a very slight, hardly noticeable curvature to the above graph.

5 Sensitivity Analysis: Varying Bathtub Characteristics

We now address query number ”3” by creating various bathtub designs, varying the surface areas exposed and volumes, to observe the eﬀect of the surface area to volume ratio on the rate of cooling. The changes in surface area and volume change the k value, so we recalculate k for each case and test each bathtub design with our simulation.

5.1 Varying Surface Area Under Constant Volume

The standard bathtub model has a volume of 25, 200 in3 (”Bathtub Sizes”), so we keep that volume constant while creating three other common bathtub designs. Using our model, we predict the

Page 16 optimal ﬂow rate for following designs created using Autodesk Inventor, choosing ﬂow rates with the lowest total deviance from initial temperature.

Page 17 Standard bathtub model Dimensions (length x width x height): 60” × 30” × 14” Surface area: 1, 800 in2 Volume: 25, 200 in3 The standard bathtub model has a predicted optimal ﬂow rate of 1.81 gallons/minute and a deviance of 10.18◦C2.

Page 18 Page 19 Circular bathtub model Dimensions (radius x height): 23.14” × 15” Surface area: 1, 680 in2 Volume: 25, 200 in3 The circular bathtub model has a predicted optimal ﬂow rate of 1.61 gallons/minute and a deviance of 7.86◦C2.

Page 20 Page 21 Triangular bathtub model Dimensions (side1 x side2 x side3 x height): 57.02” × 57.02” × 80.64” × 15.5” Surface area: 1, 625.81 in2 Volume: 25, 200 in3 The triangular bathtub model has a predicted optimal ﬂow rate of 1.95 gallons/minute and a deviance of 5.16◦C2.

Page 22 Page 23 Square bathtub model Dimensions (side x height): 39.69” × 16” Surface area: 1, 575 in2 Volume: 25, 200 in3 The square bathtub model has a predicted optimal ﬂow rate of 4.7 gallon- s/minute and a deviance of 1.20◦C2.

5.2 Varying Volume Under Constant Surface Area

We also investigated the eﬀect of volume on optimal ﬂow rate. We construct four designs of varying volumes while keeping surface area constant at 1600 in2. Using our model, we predict the optimal ﬂow rate for following designs, choosing ﬂow rates with the lowest total deviance from initial temperature.

Page 24 Page 25 Hemisphere bathtub model Dimensions (radius): 22.57” Surface area: 1, 600 in2 Volume: 24, 079.82 in3 The hemisphere bathtub model has a predicted optimal ﬂow rate of 1.58 gallons/minute and a deviance of 6.44◦C2.

Page 26 Page 27 Oval bathtub model Dimensions (rectLength x rectWidth x arcRadius x height): 50” × 23.4” × 11.7” × 15” Surface area: 1, 600 in2 Volume: 24, 000 in3 The oval bathtub model has a predicted optimal ﬂow rate of 1.6 gallons/minute and a deviance of 6.67◦C2.

Page 28 Page 29 Quarter-circle bathtub model Dimensions (radius x height): 45.14” × 14” Surface area: 1, 600 in2 Volume: 22, 400 in3 The quarter-circle bathtub model has a predicted optimal ﬂow rate of 1.41 gallons/minute and a deviance of 9.00◦C2.

Page 30 Page 31 Trapezoidal bathtub model Dimensions (topLength x topWidth x bottomLength x bottomWidth x height): 50” × 32” × 36” × 24” × 15” Surface area: 1, 600 in2 Volume: 18, 200 in3 The trapezoid bathtub model has a predicted optimal ﬂow rate of 2.15 gallons/minute and a deviance of 9.35◦C2.

5.3 Observations

We at ﬁrst expected to discover a consistently increasing or decreasing trend between volume and optimal ﬂow rate, and surface area and optimal ﬂow rate. However, as we increment surface area under constant volume, we note that the optimal ﬂow rate decreases, but then increases again, following no set pattern.

Page 32 Similar ﬂuctuation occurs as we vary volume under constant surface area.

Page 33 While increasing surface area does understandably increase the rate of cooling, the changes in temperature at any given moment also change how much the incoming hot water heats the water. Because of this, we can’t reliably use a trend to predict what the optimal ﬂow rate is until we test the design with our simulation.

5.4 Material of Bathtub

Although bathtubs are typically made with material that provides very eﬀective insulation, some tubs are made of less insulating material, such as ﬁberglass (”Bathtubs”). To test the impact of the insulating material on the rate of cooling, we can use our simulation with the total surface area of the tub instead of just the surface area of water exposed to the air. This is due to our global assumption that heat loss through heavily insulated surfaces is negligible, but heat loss through poorly insulated surfaces is equivalent to direct heat loss to surrounding air.

Using the standard bathtub model with ﬁberglass material, the total surface area is 6, 120 in2. However, only ﬁve of the sides are made with insulating material while the top is still exposed to the air. We assume the ﬁberglass material insulates 1 8 as well as acrylic material does. Diﬀerent builds of ﬁberglass will have diﬀerent insulation properties, so we select this one simply to show the eﬀect. To account for the insulation, we use an adjusted additional surface area of 2, 340 in2, which 8, added to the 1, 800 in2 of the exposed is the surface area of the ﬁve sides with a multiplier of 1

Page 34 top surface. The volume is kept the same as the standard model at 25, 200 in3.

The predicted optimal ﬂow rate is 7.52 gallons/minute, with a deviance of 1.92 ◦C2. The ﬂow rate of a tub made of ﬁberglass material is higher than the standard tub design created with acrylic material, which had a predicted optimal ﬂow rate of 1.81 gallons/minute and a deviance of 10.18 ◦C2. The increased ﬂow rate in less insulating material is expected, as the lower insulation results in greater heat loss over time.

5.5 Additives (bubble bath)

To address the last of our queries, we consider the eﬀects of adding a substance like bubble bath to the water.

Bubble bath solutions provide additional insulation to the water through the layer of bubbles on the surface of the water. The insulation decreases the rate of cooling of the water. The amount of insulation provided by the bubble bath is dependent on the speciﬁc type of bubble bath, the amount of bubble bath used, etc. Thus we choose a particular insulation value of bubble bath as example. We assume the bubble bath has an insulation factor of .95, and so account for the insulation by multiplying the surface area of the water exposed to air by the insulation factor, to get a surface area of 1, 710 in2.

Using this value for surface area in our simulation and the standard volume of 25, 200 in3, we obtain a predicted ﬂow rate of 1.58 gallons/minute and a deviance of 8.75 ◦C2. The origi- nal standard bathtub model without bubble bath additive had a predicted optimal ﬂow rate of 1.81 gallons/minute and a deviance of 10.18 ◦C2.

The ﬂow rate with bubble bath additive decreased, which is expected as the layer adds insulation and reduces the rate of cooling.

Page 35

6 Conclusion

6.1 Results

For a standard bathtub 60” × 30” × 14” in size in a room of temperature 21◦C, we suggest for the person to turn the faucet to a ﬂow rate of 1.81 gallons/minute.

6.2 Strengths of Model

• Our model is able to accurately and retroactively determine the temperature cooling of a relatively large body of water, and was conﬁrmed by the data in our experiment in Appendix A.

• Our model is also able to conclusively produce a speciﬁc numerical optimal ﬂow rate given parameters of the standard bathtub, using the deviance rating.

• Additionally, our model is able to accommodate bathtubs of diﬀerent shapes and dimensions, given their surface areas and volumes, as well as other materials and additives.

6.3 Limitations of Model

Many assumptions were necessary to simplify the problem enough so that it could be tackled.

• Firstly, our model assumes that the strategy provided in ”A Simple Solution” ensures that the water heats perfectly evenly and instantaneously. In reality, unless the person is extremely skilled at wading the water, the temperature of the water will still not be exactly the same at every point in the bathtub, ﬂuctuating due to convection currents.

Page 36 • Secondly, the ambient room temperature is assumed to remain constant, but in reality, the ambient temperature should also increase as a result of the heat loss from the water, but to model this requires consideration of other external factors including the dimensions of the room and any possible air currents.

• The strategy we suggest has the user ﬂailing his arms constantly throughout the duration of the bath; in reality this is not plausible given that a bath is meant to be a relaxing experience.

We address this issue more closely in ”Future Work.”

6.4 Future Work/Discussion

Much work has already been done in an eﬀort to keep bath water from cooling over time. Be- sides heat-preserving ﬁlms like bubble bath, there even exists a ”Water Blanket” product that insulates the top surface of the bathtub to reduce heat loss (”Water Blanket”). Such a product is understandably a reasonable investment for one who wants to keep his bath water hotter for longer.

But we can do better.

The glaring issue with our strategy is that nobody wants to swirl their arms for his entire bath time. Even with a product like the ”Water Blanket,” hot water will still rise to the top of the bath and the bottom of the bathtub will have disproportionately cooler water.

We decided to lay out a prototype design of our own original invention theorized during this MCM competition, a cost-eﬃcient product that will keep the temperature on the bottom of the tub as hot as the top. This product also doubles as a converter from standard bathtub to Jacuzzi-esque hot tub with water jets.

6.5 Home Jacuzzi

The following constructions were rendered using Autodesk Inventor.

Our product is a low-tech tubing that connects to the faucet of any standard bathtub and, at this stage of development, ﬁts the dimensions of the standard bathtub.

Page 37 Page 38 The water from the faucet then ﬂows out not directly down into the tub, but instead through the tube and out the horizontal holes, heating the bottom of the tub before the top. The hot water from the bottom then rises to the top, as in any bathtub. This counteracts the loss of heat at the surface of the tub to equalize the temperature in the tub.

The jets of water exiting the holes also create the eﬀect of Jacuzzi jets without the high costs of installing actual Jacuzzi jets.

Appendices

A Experimental Design for Real-World Bathtub Data

Materials

• Bathtub in the shape of a rectangular prism, insulated on ﬁve faces and exposed to the air on the top surface

• Thermometer

Procedure First, we use the thermometer to record the ambient temperature of the room in Celsius. We also record the dimensions of the bathtub, calculating surface area and volume. We turn on the faucet to the max heat setting and ﬁll the tub to its volume capacity. When this is done, we use the thermostat to record the initial temperature of the water in the tub. From then on, we record the temperature again once every minute for 60 minutes. The independent variable was time, while the dependent variable was temperature of the water in Celsius.

Data Ambient room temperature = 21◦C Dimensions of bathtub = 55 × 23 × 13 , which yields a volume of 16, 455 in3 and a surface area of 1265 in2.

The rest of the data is included in the body of the paper as a graph.

B Simulation Code

#!/ usr / bin /python

import logging import math import os import sys import time

import pygal

i f len ( sys . argv ) < 3:

print ”Usage : %s <surface area> <volume>” % sys . argv [ 0 ]

Page 39 print ” where surface area i s in square inches ” print ” and volume i s in cubic inches ” sys . e x i t (1)

s u r f a c e a r e a = float ( sys . argv [ 1 ] ) volume = float ( sys . argv [ 2 ] ) filename = ”SA%s V%s ” % ( int ( s u r f a c e a r e a ) , int ( volume )) points = [ ]

BATH DURATION = 40 INITIAL TEMPERATURE = 37 HOTWATERTEMPERATURE = 48 ROOMTEMPERATURE = 21 volume ∗1.0 / AREA, HEIGHT = surface area , s u r f a c e a r e a

l o g d i r = ” logs ” outdir = ”output” for f o l d e r in [ logdir , outdir ] :

i f not ( os . path . e x i s t s ( f o l d e r ) and os . path . i s d i r ( f o l d e r ) ) :

os . mkdir ( f o l d e r )

def d e f a u l t l o g g e r (msg ) :

print ”[%( time ) s ] %(msg) s ” % { ”time” : time . asctime () ,\ ”msg” : msg }

def l o g t o f i l e ( filename ) :

def func (msg ) :

fout = open( filename , ”a+” ) fout . write ( ”%s \n” % ( ”[%( time ) s ] %(msg) s ” % \ { ”time” : time . asctime () , ”msg” : msg })) fout . c l o s e () return func

def room cool ( temperature , frame ) :

VOLUME = AREA ∗HEIGHT ∗0.0163871 SURFACE AREA = AREA ∗0.00064516 K = 0.385387190197681 ∗math . e ∗∗( −0.167081937857622 \ ∗pow(pow(VOLUME, 2) / pow(SURFACE AREA, 3) , 1.0 / 3))

dT = −1 ∗K ∗( temperature −ROOMTEMPERATURE) ∗60

return dT

def water heat ( temperature , f lo w r a t e ) :

Cp = 4.179 # s p e c i f i c heat of water ∗3785.4118 # mass ( g ) flow rate mass = f l o w r a t e of water

Page 40 tub mass = AREA ∗HEIGHT ∗16.3870640693 # mass ( g ) of tub

dT = flow rate mass ∗(HOTWATERTEMPERATURE −temperature ) \ / tub mass

return dT

def run simulation ( f l o w r a t e =1, log=d e f a u l t l o g g e r ) :

frame = 0 deviance = 0.0 temperature = INITIAL TEMPERATURE WATER RUNNING = False

while frame < BATH DURATION:

dT cool = room cool ( temperature , frame ) temperature += dT cool abs( temperature −INITIAL TEMPERATURE) > 1.4 \ i f and not(WATER RUNNING) :

WATER RUNNING = True \ dT heat = water heat ( temperature , f lo w r a t e ) i f WATER RUNNING else 0 temperature += dT heat i f WATER RUNNING:

E1 = INITIAL TEMPERATURE E2 = temperature deviance += (INITIAL TEMPERATURE \ −temperature ) ∗∗2 frame += 1

return deviance

−1): for x in range (1600 , 1 , f l o w r a t e = x / 100.0 log = l o g t o f i l e ( ” logs /” + filename + ” . log ” ) deviance = run simulation ( f l o w r a t e=flow rate , log=log ) points . append (( flow rate , deviance ))

minimum = (9999999 , 9999999) for point in points :

x , y = point minx , miny = minimum i f y < miny :

minimum = (x , y)

l o g t o f i l e ( ” logs /” + filename + ” . log ” )( ”minimum : %s ” % str (minimum))

Page 41 chart = pygal .XY( stroke=True ) chart . t i t l e = ”Optimal Flow Rate (SA: %s , V: %s ) ” % \ ( int ( s u r f a c e a r e a ) , int ( volume )) chart . x t i t l e = ”Flow Rate (GPM) ” chart . y t i t l e = ”Deviance” chart . add ( ”Bathtub” , points ) [{ ” value ” : minimum , } ] ) chart . add ( ”Minimum” , ” l a b e l ” : str (minimum) chart . render to png ( ”output/” + filename + ” . png” )

sys . e x i t (0)
