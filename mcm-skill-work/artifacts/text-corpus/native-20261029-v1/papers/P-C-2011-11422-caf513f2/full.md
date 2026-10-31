# P-C-2011-11422-caf513f2

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Putting the Spark Back in the

<!-- b000002 | title | pages [1] -->
Electric Car

<!-- b000003 | furniture | pages [1] -->
Team #11422

<!-- b000004 | prose | pages [1] -->
February 14, 2011

<!-- b000005 | prose | pages [1] -->
1

<!-- b000006 | furniture | pages [2] -->
Team #11422

<!-- b000007 | heading | pages [2] -->
Contents

<!-- b000008 | contents | pages [2] -->
1

<!-- b000009 | contents | pages [2] -->
Clariﬁcation of Problem

<!-- b000010 | contents | pages [2] -->
2

<!-- b000011 | contents | pages [2] -->
Plan of Attack

<!-- b000012 | contents | pages [2] -->
3

<!-- b000013 | heading | pages [2] -->
Assumptions

<!-- b000014 | prose | pages [2] -->
4 On Types of Cars

<!-- b000015 | prose | pages [2] -->
5

<!-- b000016 | heading | pages [2] -->
Model for Number of Cars

<!-- b000017 | prose | pages [2] -->
6

<!-- b000018 | heading | pages [2] -->
Microeconomic Model

<!-- b000019 | furniture | pages [2] -->
Page 2 of 20

<!-- b000020 | prose | pages [2] -->
3

<!-- b000021 | prose | pages [2] -->
3

<!-- b000022 | prose | pages [2] -->
3

<!-- b000023 | prose | pages [2] -->
4

<!-- b000024 | prose | pages [2] -->
4

<!-- b000025 | prose | pages [2] -->
5 . . . . . . . . . . . . . . . . . . . . . . . 6.1 Global Inﬂuence Model 5 Strengths & Weaknesses . . . . . . . . . . . . . . . . . . . 6.1.1 7 Localized Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 8 . . . . . . . . . . . . . . . . . . . . . . 6.2.1 Cellular automata 8 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . 6.3 9

<!-- b000026 | heading | pages [2] -->
Macroeconomic Model: Meeting the Energy Demand

<!-- b000027 | prose | pages [2] -->
7 10 Current Energy Source and Demand . . . . . . . . . . . . . . . . 7.1 10 Current Pollution rates . . . . . . . . . . . . . . . . . . . . . . . . 7.2 11 Quantizing Pollution . . . . . . . . . . . . . . . . . . . . . . . . . 7.3 11 Health . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3.1 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.4 Quantizing Cost 12 α Parameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.5 13 Minimizing X: Genetic and Nelder-Mead Methods 7.6 . . . . . . . .

<!-- b000028 | prose | pages [2] -->
14 Using Alpha to Determine Cost, and Vice Versa 7.7 . . . . . . . . .

<!-- b000029 | prose | pages [2] -->
14 Example Calculation . . . . . . . . . . . . . . . . . . . . . . . . . 7.8 16 Fossil Fuels Saved . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.9 17 7.10 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | prose | pages [2] -->
17

<!-- b000031 | heading | pages [2] -->
Meshing the Micro and Macro Models

<!-- b000032 | prose | pages [2] -->
8

<!-- b000033 | prose | pages [2] -->
9

<!-- b000034 | heading | pages [2] -->
Conclusion

<!-- b000035 | prose | pages [2] -->
18

<!-- b000036 | prose | pages [2] -->
19

<!-- b000037 | furniture | pages [3] -->
Team #11422

<!-- b000038 | furniture | pages [3] -->
Page 3 of 20

<!-- b000039 | prose | pages [3] -->
1 Clariﬁcation of Problem

<!-- b000040 | prose | pages [3] -->
With the recent introduction of the Nissan Leaf and Chevy Volt to the world car ﬂeet and the fading supply of petroleum, the possibility of electric vehicles replacing standard petroleum cars is increasing. Questions arise concerning the feasibility of such vehicles, speciﬁcally regarding the amount of fossil fuels saved through widespread use of electric cars, and the economic feasibility. It is of great concern to auto-manufacturers and environmentalists alike to determine how to cause electric cars to ’catch on,’ and of equally great concern to govern- ments to determine how to augment the power grid to meet the demand of the electric car ﬂeet. The models proposed within this paper will oﬀer an insight to these problems.

<!-- b000041 | prose | pages [3] -->
2 Plan of Attack

<!-- b000042 | prose | pages [3] -->
Our objective is to model the eﬀects of electric vehicles on the environment, public health, and economy. We need to determine which methods would be most eﬀective in causing widespread use of electric vehicles, within a reasonable time scale. Large scale use of electric vehicles would also put an increased strain on the power grid, which would have to be corrected. To determine the most eﬃcient way to do this, we will proceed as follows:

<!-- b000043 | prose | pages [3] -->
1. Create a model for the amount of electric cars at any given point in time.

<!-- b000044 | prose | pages [3] -->
(Micro)

<!-- b000045 | prose | pages [3] -->
2. Create a model that gives a single value to the eﬀect electric cars have on the environment, health, and economy. (Macro)

<!-- b000046 | prose | pages [3] -->
3. Connect these models so that, by giving setup conditions, we can deter- mine the cost to minimize the pollution values.

<!-- b000047 | prose | pages [3] -->
3

<!-- b000048 | heading | pages [3] -->
Assumptions

<!-- b000049 | prose | pages [3] -->
Due to the extrapolative nature of our model, and the diﬃculty in obtaining reliable global information, several assumptions were made in order to complete our model. These simplifying assumptions will be used throughout the paper and could feasibly be replaced with reliable data when it becomes available.

<!-- b000050 | prose | pages [3] -->
• The cost of building more coal, oil, and natural gas plants is negligible to the cost of yearly fossil fuel production. That is to say, energy costs simply rely on production prices from the plants themselves, and not creation of the plants.

<!-- b000051 | prose | pages [3] -->
• We assume 100% eﬃciency of converting fossil fuels to energy for electric- ity. This makes the calculations for energy easier, removing the need to know the electric energy conversion rate for electric generators.

<!-- b000052 | prose | pages [3] -->
• World Governments can control addition of power plants to determine the proportions of energy from each source. This is essential in changing the

<!-- b000053 | furniture | pages [4] -->
Team #11422

<!-- b000054 | furniture | pages [4] -->
Page 4 of 20

<!-- b000055 | prose | pages [4] -->
makeup of the power grid. By being able to change the ratio of the energy sources of our electricity production can we can change the ratio of the pollutants produced for each unit of electrical energy.

<!-- b000056 | prose | pages [4] -->
• Ratios of energy sources into demand sectors for the US in 2009 is the same as the ratios across the world. This allowed us to generalize the information that we had to the world-wide energy system.

<!-- b000057 | prose | pages [4] -->
• Price increases quadratically as demand increases for fossil fuels.

<!-- b000058 | prose | pages [4] -->
This allows us to extrapolate the past data, allowing us to produce a prediction of the cost of fossil fuels in the future.

<!-- b000059 | prose | pages [4] -->
• Population within the next 50 years can be modeled with a cubic ﬁt. This allows us to extrapolate the past data as well, ensuring that we know the amount of cars in a given year.

<!-- b000060 | prose | pages [4] -->
• A major factor in choosing which car to buy is what the people around you own. The movie ”Who Killed the Electric Car?” suggested that the main reason that electric cars did not become popular was because many people did not know about them or their properties. This assumption is the basis in the models for the spread of electric cars throughout a population. [9]

<!-- b000061 | prose | pages [4] -->
• It is economically and environmentally infeasible to increase current en- ergy contribution to the electric power grid for each power source by more than %25 percent. This is to establish upper bounds for the Nelder-Mead methods, and can be replaced with projected maximum contribution for 2060 if/when these values become available.

<!-- b000062 | prose | pages [4] -->
4 On Types of Cars

<!-- b000063 | prose | pages [4] -->
We have decided to base our model solely on electric vehicles versus gasoline vehicles, instead of including hybrid vehicles. We have chosen to do this because we are concerned with the widespread usage of electric vehicles.

<!-- b000064 | prose | pages [4] -->
If electric vehicle usage is widespread, then the idea of a hybrid car is useless, since electric cars can be used for most transportation usages and gas cars can be used for any transportation that electric cars cannot do. Hybrid models were created to transition from gas cars to electric cars.

<!-- b000065 | prose | pages [4] -->
However, if we are to consider widespread usage of electric vehicles, hybrids won’t be necessary. It is worth noting that electric vehicles do have limited range, causing some range anxiety. Modern estimates suggest that 90% of automobile users do not have needs that exceed the limitations of electric cars, however, so the range anxiety will only aﬀect 10% of the population[9].

<!-- b000066 | prose | pages [4] -->
5

<!-- b000067 | heading | pages [4] -->
Model for Number of Cars

<!-- b000068 | prose | pages [4] -->
In order to model the change towards electric cars and its impact on the environment, we need a model for the number of cars in the future. We found an estimated 134 motor vehicles per 1000 people in the top 130 developed countries. From this, an estimate of 120 vehicles per 1000 people in the world can be made.

<!-- b000069 | furniture | pages [5] -->
Team #11422

<!-- b000070 | furniture | pages [5] -->
Page 5 of 20

<!-- b000071 | prose | pages [5] -->
Using this and population data, we can expect to have C cars in t years after 1950 based on the following equation [10] :

<!-- b000072 | prose | pages [5] -->
C(t) = .002t(2.55 · 109 + 3.91 · 107t + 1.1 · 106t2 −9.38 · 103t3)

<!-- b000073 | prose | pages [5] -->
We decided upon a cubic ﬁt to model the population because it ﬁtted popu- lation data very well. However, this ﬁt will only accurately model population data until 2060, due to the cubic nature of the function. We have a multiplier of .002t because the number of cars per capita will increase over time, as data has shown[1]. We are going to let E equal the proportion of cars which are electric. The following 2 equations give the number of electric and gasoline vehicles over time in terms of E.

<!-- b000074 | prose | pages [5] -->
E(t) = E · C(t)

<!-- b000075 | prose | pages [5] -->
G(t) = (1 −E) · C(t)

<!-- b000076 | prose | pages [5] -->
In our microeconomic model, we examine how E will change 50 years in the future based on an initial proportion of electric cars.

<!-- b000077 | prose | pages [5] -->
This will allow us to see what must be done to make electric vehicle usage widespread.

<!-- b000078 | prose | pages [5] -->
For our macroeconomic model, we let E = .9 since we wish to examine the eﬀects of widespread electric vehicle usage.

<!-- b000079 | heading | pages [5] -->
Microeconomic Model

<!-- b000080 | prose | pages [5] -->
6

<!-- b000081 | prose | pages [5] -->
Through examination of how individuals react to electric car usage we can model the change from petroleum vehicles to electric vehicles. Our small-scale model needs to be based on the likelihood that individuals will switch to electric vehicles. We propose two models. Both of these models require a government subsidy for electric cars in order to ”jumpstart” their production, and explosion in popularity. The ﬁrst model is based on coupled diﬀerential equations for how one might expect the number of electric vehicles and the number of gasoline vehicles will change over a continuous time interval. The second model is a 2D cellular automata simulation to model the local inﬂuence as well as global inﬂuence of the number of electric vehicles, over a discrete time interval.

<!-- b000082 | prose | pages [5] -->
6.1

<!-- b000083 | heading | pages [5] -->
Global Inﬂuence Model

<!-- b000084 | prose | pages [5] -->
This model assumes that individuals are inﬂuenced by the global proportion of people who have electric cars. An individual who is going to buy a new car or replace a broken down gas car will buy an electric car with a probability equal to the proportion of people who have electric cars. This is because the more people who have electric cars, the more likely an individual is to hear about electric cars and be persuaded to switch to an electric car. This allows us to deﬁne the following coupled diﬀerential equations where BDE and BDG is the probability that an electric and gas car will break down during one year. Since gas cars last for about 8 years and electric cars last for about 20 years, we let 1 20 and BDG = 1 BDE = 8 [4].

<!-- b000085 | prose | pages [5] -->
E(t)

<!-- b000086 | prose | pages [5] -->


<!-- b000087 | prose | pages [5] -->


<!-- b000088 | prose | pages [5] -->
E(t)

<!-- b000089 | prose | pages [5] -->
E(t) + G(t) · (C′(t) + BDG · G(t)) −BDE · E(t) · E′(t) =

<!-- b000090 | prose | pages [5] -->
1 − E(t) + G(t)

<!-- b000091 | furniture | pages [6] -->
Team #11422

<!-- b000092 | furniture | pages [6] -->
Page 6 of 20

<!-- b000093 | prose | pages [6] -->


<!-- b000094 | prose | pages [6] -->


<!-- b000095 | prose | pages [6] -->
E(t)

<!-- b000096 | prose | pages [6] -->
E(t)

<!-- b000097 | prose | pages [6] -->
G′(t) =

<!-- b000098 | prose | pages [6] -->
· (C′(t) + BDE · E(t)) −BDG · G(t) ·

<!-- b000099 | prose | pages [6] -->
1 − E(t) + G(t)

<!-- b000100 | prose | pages [6] -->
E(t) + G(t)

<!-- b000101 | prose | pages [6] -->
Since our C(t) and is only valid for ﬁfty years in the future, solving these equations outright is unnecessary. We use Euler’s Method to approximate E(t) and G(t). To do this, we need two points, one for E(t) and one for G(t). Since t is measured in years after 1950, we let G(60) = C(60). We cannot let E(60)=0 since the only way for the number of gas cars to grow is from the probability

<!-- b000102 | prose | pages [6] -->
E(t) C(t). This model requires that a certain number of electric cars be seeded into the population to jump start the growth of electric cars. In order to seed these cars, the government could pay the diﬀerence in cost between an electric vehicle and an average gas car to give people an incentive to buy an electric car. By spending this money to encourage people to use electric cars, the government would save money later by spending less money for fossil fuels, such as oil. We will examine how this works after we have built our macroeconomic model. To determine the seeding cost, we assume that the government will pay the diﬀer- ence between the cost of an electric vehicle and a gasoline vehicle. We decided this cost per car would be $41, 000 −$28, 400 = $12, 600. The following graphs demonstrate the rate at which the proportion of electric vehicles grows (with seeding values of .05 and .3) and the following table summarizes this data with varying proportions of seeding in 2011.

<!-- b000103 | furniture | pages [7] -->
Team #11422

<!-- b000104 | furniture | pages [7] -->
Page 7 of 20

<!-- b000105 | prose | pages [7] -->
Seeding Cost Seed Proportion E in 2060 1.0327 · 1011 0.01 0.267 5.16348 · 1011 0.05 0.667 1.0327 · 1012 0.1 0.815 1.54854 · 1012 0.15 0.877 2.06514 · 1012 0.2 0.912 2.58174 · 1012 0.25 0.933 3.09834 · 1012 0.3 0.948

<!-- b000106 | prose | pages [7] -->
The more money spent on jumpstarting electric vehicles, the larger E will be 50 years in the future. In order to determine which proportion of seeded cars would be most proﬁtable in the future, we would need to know the make up of the power grid, which we determine in our macroeconomic model. We will connect this model to the macroeconomic model later.

<!-- b000107 | prose | pages [7] -->
6.1.1

<!-- b000108 | heading | pages [7] -->
Strengths & Weaknesses

<!-- b000109 | prose | pages [7] -->
A strength of this model is that it allows the government to see what would need to be done in order for people to want to buy electric cars. By basing this model on the proportion of people who have electric cars, this model can realistically model an individual’s likelihood of switching to an electric car.

<!-- b000110 | prose | pages [7] -->
A weakness in this model is that seeding only occurs in one year, instead of a range of years. Another weakness of this model is that it does not include locality, which misses out on what seems to be a crucial point in the rise of electric vehicles. Another weakness of this model is it does not consider current sources of energy. Currently, electric cars are not better for the environment because the largest source of electrical energy is coal; this will be considered and changed in the macroeconomic model.

<!-- b000111 | furniture | pages [8] -->
Team #11422

<!-- b000112 | prose | pages [8] -->
6.2 Localized Behavior

<!-- b000113 | furniture | pages [8] -->
Page 8 of 20

<!-- b000114 | prose | pages [8] -->
The previous model assumes that the total percentage of electric cars inﬂuences the chance of a single person purchasing one. However, a person is aﬀected by the people closest to them in addition to the global behavior. This is why we decided to model the spread of electric cars using 2-dimensional cellular automata. First, we decided that a cell’s percentage to pick either electric or gas is based on the 8 cells that are adjacent, known as the Moore Neighborhood. The inﬂuence from locality is converted into a chance of buying an electric car based on the number of your neighbors who are electric cars (N) according to the following equation:

<!-- b000115 | prose | pages [8] -->
P(if electric stay electric)= 1

<!-- b000116 | prose | pages [8] -->
8 · (.1N + .1) P(if gas become electric)= 1

<!-- b000117 | prose | pages [8] -->
20 · (.1N + .1)

<!-- b000118 | prose | pages [8] -->
Global inﬂuence is also considered with this model, and is incorporated with what we call the ”snowball constant.” The diﬀerential equations given above can be applied to cellular automata rules by setting C′(t) = 0, since the number of E(t) cells is constant, which allows us to substitute E(t)+G(t) with Ept, the proportion of electric vehicles. Ultimately we can rewrite our diﬀerential equations as:

<!-- b000119 | prose | pages [8] -->
Epn+1(t) −Epn(t) = 3Ep(t)

<!-- b000120 | prose | pages [8] -->
· (1 −Ep(t)) 40

<!-- b000121 | prose | pages [8] -->
Gpn+1(t) −Gpn(t) = 3Ep(t)

<!-- b000122 | prose | pages [8] -->
· (Ep(t) −1) 40

<!-- b000123 | prose | pages [8] -->
To consider both the local and globalized behavior (L and W), we can simply weight these with the relative importance of localized behavior (due to the snowball eﬀect) with that of global behavior. Exact values of snowball constants will have to be determined through real world observations, and will likely vary throughout the population. For our data, we used a snowball constant k = 4, assuming that localized behavior is responsible for 80% of buying patterns. Our ﬁnal proportion looks like this:

<!-- b000124 | prose | pages [8] -->
P = k · L + W

<!-- b000125 | prose | pages [8] -->
1 + k

<!-- b000126 | prose | pages [8] -->
The amount of electric cars that are placed initially is changed in order to model the seeding program that the government has put in place. The output of the model gives the percentage of electric cars out of the total population of cars. This percentage can be traced from year to year to give you the eﬀect of governmental electric car seeding, both in the ﬁnal percent as well as the year when government seeding no longer plays a role in the percentage of cars.

<!-- b000127 | prose | pages [8] -->
6.2.1 Cellular automata

<!-- b000128 | prose | pages [8] -->
Initial seeding is important as there is no point to seeding more cars if fewer

<!-- b000129 | prose | pages [8] -->
cars will get you to your goal percentage of electric cars on the road by a certain year. By using both the global and the local model, we determined

<!-- b000130 | prose | pages [8] -->
that the ﬁnal percentage of cars that are electric, for a given number of

<!-- b000131 | furniture | pages [9] -->
Team #11422

<!-- b000132 | furniture | pages [9] -->
Page 9 of 20

<!-- b000133 | prose | pages [9] -->
seeding, is less in the local model than in the global model, meaning that these local interactions seem to slow down the distribution of cars. The ﬁnal state of

<!-- b000134 | prose | pages [9] -->
one simulation and a chart of the proportion of electric vehicles versus time

<!-- b000135 | prose | pages [9] -->
are shown below:

<!-- b000136 | prose | pages [9] -->
6.3

<!-- b000137 | heading | pages [9] -->
Strengths and Weaknesses

<!-- b000138 | prose | pages [9] -->
The beneﬁts of a cellular automata model are many: this model diﬀers from all others in this report int that there is no population increase, which means that this model is independent of the ﬂawed population model, and is free from all ﬂaws that come with that. This means that this model can more accurately model years after 1960. Modiﬁcations can be made to increase the chances of buying an electric car as time goes on, due to improvements in technology and the decrease in electric car cost. Furthermore, the eﬀects of localized behav- ior are well documented, and completely overlooked with diﬀerential equation models. The eﬀects of these localized behavior can be combined with the diﬀer- ential equation model with the snowball constant– an option unavailable to the

<!-- b000139 | furniture | pages [10] -->
Team #11422

<!-- b000140 | furniture | pages [10] -->
Page 10 of 20

<!-- b000141 | prose | pages [10] -->
diﬀerential equation model. This localized model is not without it’s weakness. Because of the ﬁnite number of cells, it is diﬃcult to incorporate growth of the population (of total cars) into the CA model. Much of our values for proba- bilities rely on rough probabilities and assumptions of the snowball constant. These can be adjusted on a product-by-product, or even a cell-by-cell basis, but it complicates the model greatly. We also could have overlooked crucial values in our probability models percentages needed to factor into the lifetime cost of a car, relative usability values like the average range an electric car can go without recharging, and more qualitative values like sticker shock.

<!-- b000142 | prose | pages [10] -->
7

<!-- b000143 | heading | pages [10] -->
Macroeconomic Model: Meeting the Energy

<!-- b000144 | prose | pages [10] -->
Demand

<!-- b000145 | prose | pages [10] -->
Whereas our microeconomic model focused on the necessary parameters to en- sure a large number of electric cars in the future, our macroeconomic model focuses on the changes that need to be made to accommodate the increased demand of electricity. It is important to consider both the costs required to produce these new amounts of electric energy, and the ”hidden” costs of pollu- tion. Without considering these ”hidden” costs, our model would simply gener- ate the cheapest solution to the increased power demand, which could possibly just trade one fossil fuel (gasoline) for another (coal, etc.). Thus, we’ve gener- ated an equation to determine the cost associated with the increased electricity demand, depending upon how much of each energy source we utilize, and a variable parameter equating pollution to cost.

<!-- b000146 | prose | pages [10] -->
7.1 Current Energy Source and Demand

<!-- b000147 | prose | pages [10] -->
Data from the EIA has shown that 38.075 quadrillion BTU was used for elec- tricity in 2009, producing 11.159 trillion kWh [7]. The breakdown of energy sources contributing to this statistic is summarized in the following chart. Since it is assumed that this breakdown is roughly equal for all highly-developed coun- tries,the countries who will have the largest number of electric cars, and thus increased demand for electricity.

<!-- b000148 | prose | pages [10] -->
[7]

<!-- b000149 | furniture | pages [11] -->
Team #11422

<!-- b000150 | furniture | pages [11] -->
Page 11 of 20

<!-- b000151 | prose | pages [11] -->
The most recent electric cars from Li-ion Motors Corp have a range of 120 miles and require 8 hours of charging from a 110V source [4]. This means that 52.8 kWh are needed for a full charge, or .44kWh per mile of travel.

<!-- b000152 | prose | pages [11] -->
This translates to 1501.3 BTU needed a mile in an electric vehicle. The average pas- senger car can travel 31 miles on a gallon of gasoline. Since a gallon of gasoline contains roughly 116,090 BTU, the average gas car runs on 3744.84 BTU per mile [1]. This is more than twice as much energy required by electric cars, so switching to electric cars decreases the amount of energy required worldwide for transportation purposes, but also requires a switch from the 100% gasoline power source for gas cars, to the medley of power sources used for electricity.

<!-- b000153 | prose | pages [11] -->
7.2 Current Pollution rates

<!-- b000154 | prose | pages [11] -->
Burning fossil fuels creates pollutants that damage the environment, increasing acid rain, respiratory illness, and photochemical smog. Using current energy source quantities, the pounds per mile of use of electric and gas cars is sum- marized in the following table. Though nuclear power sources have not gained widespread popularity due to social fears of nuclear accidents and the relative cost of creating a network of reactors, their carbon footprints are negligible. It also goes without saying that the footprint of renewable energy sources are also negligible.

<!-- b000155 | prose | pages [11] -->
Pollutant Electric Car Carbon Dioxide 0.183969302 Carbon Monoxide 0.000161195

<!-- b000156 | prose | pages [11] -->
Nitrogen Oxides 0.000360913 Sulfur Dioxide 0.001884252 Particulates 0.001980545 1.16351 · 10−8 Mercury

<!-- b000157 | prose | pages [11] -->
Gasoline Car Diﬀerence 0.61415376 0.430184458 −3.76149 · 10−5 0.00012358

<!-- b000158 | prose | pages [11] -->
0.001677688 0.001316776 0.00420171 0.002317459 0.000314567 -0.001665978 2.62139 · 10−8 1.45788 · 10−8

<!-- b000159 | prose | pages [11] -->
From our equation of the number of cars in terms of years since 1950, C(t), and the proportion of those which are electric E, we create the following equations for the pounds of pollutant reduced each year.

<!-- b000160 | prose | pages [11] -->
Pollutant Carbon Dioxide Pounds Saved 0.430 · 12, 200 · E · C(t) −3.76 · 10−5 · 12, 200 · E · C(t) Carbon Monoxide 0.00132·12, 200 · E · C(t) Nitrogen Oxides 0.00232·12, 200 · E · C(t) Sulfur Dioxide -0.00167·12, 200 · E · C(t) Particulates 1.46 · 10−8 · 12, 200 · E · C(t) Mercury

<!-- b000161 | prose | pages [11] -->
7.3 Quantizing Pollution

<!-- b000162 | prose | pages [11] -->
The pollution value is a metric that determines how good for the environment having a certain percentage of electric cars are. The ﬁrst value that determines this metric is the amount of pollution that is being saved in pounds per year. The second value is the percent pollutant decrease, which describes how much

<!-- b000163 | furniture | pages [12] -->
Team #11422

<!-- b000164 | furniture | pages [12] -->
Page 12 of 20

<!-- b000165 | prose | pages [12] -->
control of that pollutant is had. For example, if you could either cut 50% of the total carbon monoxide emissions or 25% of the total carbon dioxide emis- sions, that 50% decrease is weighted heavier, regardless of the actual pounds of emissions you are eliminating. A third, hypothetical, value would be the bad- ness of each pollutant. Since not all pollutants damage the environment and peoples health as much as others, this badness relates to the degree to which the current yearly amounts of pollutants are damaging the environment. In the trials we ran, we assumed that the total yearly emissions of every pollutant were equally bad, so each badness value was set at 1. Given the set of pollutants, {CO2, CO, NOx, SO2, Particulate}, where the subscripts, G, E, and T corre- spond to the amount emitted from gas cars, the amount saved by electric cars, and total emissions, respectively, our pollution can be deﬁned as follows:

<!-- b000166 | prose | pages [12] -->
pollutants

<!-- b000167 | prose | pages [12] -->
Pollution =

<!-- b000168 | prose | pages [12] -->
7.3.1 Health

<!-- b000169 | prose | pages [12] -->
jG + E · jE

<!-- b000170 | prose | pages [12] -->
X

<!-- b000171 | prose | pages [12] -->
jT

<!-- b000172 | prose | pages [12] -->
j j

<!-- b000173 | prose | pages [12] -->
In examining the eﬀects of pollution, we should also consider the eﬀects on health. This is incorporated in our Pollution function because if we can only change a small percent of the quantity of a pollutant, it will have a smaller eﬀect on health, whereas if we can change a larger percent of the quantity of a pollutant, it will have a larger eﬀect on health. However, some pollutants may be more damaging to the environment than others, meaning that eliminating 50 % of one pollutant would not be equivalent to eliminating 50% of another. By analyzing data concerning the eﬀects of the pollutants on health and the environment, a badness factor could be determined by which each pollution percentage change could be multiplied with. By minimizing X, which is a func- tion for cost and pollution, we will also be minimizing the eﬀects. However in this model, we assumed that the badness factor, or the relative damage each pollutant causes to the environment and health, of each pollutant is the same.

<!-- b000174 | prose | pages [12] -->
7.4 Quantizing Cost

<!-- b000175 | prose | pages [12] -->
Online sources can be used to estimate the small-scale cost of each BTU of each power source, in addition to the current production in the US [3]. Bereft of data of the maximum production limits of each power source, it can be assumed that it would be economically infeasible to increase the current production limits for each power source to electricity by a factor greater than 25%. This can be modiﬁed if more accurate statistics were obtained. Since widespread use of electric cars will require a major revamping of the power grid, demand will rise dramatically, potentially with no increase in supply. The prices of commodities increase with their scarcity, as seen by supply and demand curves. Again lacking data of supply and demand curves for power sources, we’ll be forced to make several assumptions. Given our maximum production limits, m, and our current production limits (deﬁned to be 0 here) and prices, i, we can deﬁne the price of a commoditiy to be ten times it’s current cost when we reach maximum production. We’ll also deﬁne the price to be 2.5 times current cost when we

<!-- b000176 | furniture | pages [13] -->
Team #11422

<!-- b000177 | furniture | pages [13] -->
Page 13 of 20

<!-- b000178 | prose | pages [13] -->
are halfway between current and maximum production limits. Using these data points, we can set up a quadratic ﬁt to model the price p(L) of one quadrillion BTU’s of a particular energy source per quadrillion BTU (L)more than current production as:

<!-- b000179 | prose | pages [13] -->
+ 12i · L2

<!-- b000180 | prose | pages [13] -->
p(L) = i −3i · L

<!-- b000181 | prose | pages [13] -->
m2

<!-- b000182 | prose | pages [13] -->
m m

<!-- b000183 | prose | pages [13] -->
to determine the total cost to increase production from current values to pro- duction l, we can simply integrate from 0 to l:

<!-- b000184 | prose | pages [13] -->
Z l

<!-- b000185 | prose | pages [13] -->
P(l) dl = l −3i · l2

<!-- b000186 | prose | pages [13] -->
Ptot(l) =

<!-- b000187 | prose | pages [13] -->
0

<!-- b000188 | prose | pages [13] -->
+ 4i · l3

<!-- b000189 | prose | pages [13] -->
m2

<!-- b000190 | prose | pages [13] -->
2m

<!-- b000191 | prose | pages [13] -->
So total cost for all power sources is equivalent to:

<!-- b000192 | prose | pages [13] -->
P ower Sources X

<!-- b000193 | prose | pages [13] -->
Cost =

<!-- b000194 | prose | pages [13] -->
j

<!-- b000195 | prose | pages [13] -->
+ 4ij · l3

<!-- b000196 | prose | pages [13] -->
lj −3ij · l2

<!-- b000197 | prose | pages [13] -->
j

<!-- b000198 | prose | pages [13] -->
j

<!-- b000199 | prose | pages [13] -->
m2

<!-- b000200 | prose | pages [13] -->
2mj

<!-- b000201 | prose | pages [13] -->
j

<!-- b000202 | prose | pages [13] -->
The current production, cost, and maximum values are shown in the following table, where all productions are in QBTU, and cost in dollars per QBTU[3].

<!-- b000203 | prose | pages [13] -->
Current Production Power Source Petroleum 0.383

<!-- b000204 | prose | pages [13] -->
Natural Gas 6.894

<!-- b000205 | prose | pages [13] -->
Coal 18.384

<!-- b000206 | prose | pages [13] -->
Renewable Energy 4.213

<!-- b000207 | prose | pages [13] -->
Nuclear Energy 8.426

<!-- b000208 | prose | pages [13] -->
7.5 α Parameter

<!-- b000209 | prose | pages [13] -->
Max Production Current Cost 3.63 ∗1010 .479

<!-- b000210 | prose | pages [13] -->
1.47 ∗1010 8.6175

<!-- b000211 | prose | pages [13] -->
8.7 ∗109 22.98

<!-- b000212 | prose | pages [13] -->
2.2 ∗1010 5.266

<!-- b000213 | prose | pages [13] -->
5.9 ∗109 10.5325

<!-- b000214 | prose | pages [13] -->
With cost and pollution both quantized, we can deﬁne an objective function as

<!-- b000215 | prose | pages [13] -->
X = Cost + α · Pollution

<!-- b000216 | prose | pages [13] -->
Where the number of electric cars, and hence their energy demand, is held constant. X is dependent on the number of quadrillion BTU’s we add to each power source and the alpha value, because cost is dependent on the power sources, and pollution is dependent on both power sources and α. Since we want to minimize both cost and pollution, our goal is to minimize X. The α value simply serves as a constant deﬁning how much the government values cost to environment. For example, if α = 0, damage to the environment is not taken into eﬀect and minimizing X is simply minimizing Cost. In and of itself, α is a relative value, as the relationship between it and pollution is very messy (again, dependent on all power sources). However, given a maximum amount of allowable pollutants, an α can be determined. Possible values for α and their meaning will be discussed further in this report.

<!-- b000217 | furniture | pages [14] -->
Team #11422

<!-- b000218 | furniture | pages [14] -->
Page 14 of 20

<!-- b000219 | prose | pages [14] -->
7.6 Minimizing X: Genetic and Nelder-Mead Methods

<!-- b000220 | prose | pages [14] -->
With X being a function of six variables (ﬁve power sources, and alpha), there are several methods that we can use search for global minimum, subject to the constraints that each power source is never to decrease from current pro- duction standards (under the assumption that removal of production facilities is both costly and creates largescale unemployment), and is never to exceed previously deﬁned maximum production standards. However, the nonlinear of nature eliminates the possibility of linear algebra techniques. Instead, we’ll rely heavily upon a Nelder-Mead iterative search technique and a genetic algorithm to deﬁne global minima. Though both of our techniques warrant equivalent so- lutions, we found that the Nelder-Mead search was much more computationally eﬃcient, so the genetic methods were ruled out.

<!-- b000221 | prose | pages [14] -->
Thus, we run a minimiza- tion of X = Cost + α · Pollution subject to the following constraints, with variables {Petr, Nat, Coal, Ren, Nuc} deﬁning the amount of qBTU’s added to the power grid for petroleum, natural gas, coal, renewable energy and nuclear power, respectively :

<!-- b000222 | prose | pages [14] -->
Minimize X = Cost + α · Pollution Subject to

<!-- b000223 | prose | pages [14] -->
Petr + Nat + Coal + Ren + Nuc ≤Total Energy Demand

<!-- b000224 | prose | pages [14] -->
Current Production ≤Petr ≤Current Production · 1.25

<!-- b000225 | prose | pages [14] -->
With the ﬁnal constraint repeated for all power sources.

<!-- b000226 | prose | pages [14] -->
7.7 Using Alpha to Determine Cost, and Vice Versa

<!-- b000227 | prose | pages [14] -->
Since α simply refers to the amount to which we care about the environment, something that is diﬃcult to assign a concrete value to, we’ve allowed for α to vary. By iterating the Nelder-Mead optimization for a range of α values, we can generate plots of each of the Power sources versus alpha. In plainspeak, that is to say that by choosing some α value (e.g., we care x much about damage to the environment), we can locate the values of each power source qBTU by simply reading the graph. Since Cost is simply a function of the power sources and is monotonically increasing with α, we can generate a graph showing cost versus alpha, by simply repeating the above procedure, and then calculating the cost from the values of each power source, plotting this to a particular alpha value. Shown below are graphs of ’cost Vs. α’ and ’Power Sources Vs. α’ with 90% of the motor ﬂeet being electric cars, 50 years from today:

<!-- b000228 | furniture | pages [15] -->
Team #11422

<!-- b000229 | furniture | pages [15] -->
Page 15 of 20

<!-- b000230 | prose | pages [15] -->
These graphs allow us to oﬀer some insight into the behavior of the relation- ship between α (how much we care about the environment) and how we should augment the power grid. As is intuitive, a high reliance on coal and natural gas are necessary with α = 0. Nuclear power seems constantly limited by our maxi- mum production value, suggesting that nuclear power, if production levels could be raised high enough, could be utilized in generating a low-cost, low-footprint power grid. Also intuitive is the monotonic behavior of the cost vs α graph. The piecewise behavior is likely a result of certain ’feasible pockets’ within the polytope scanned with the Nelder-Mead method.

<!-- b000231 | furniture | pages [16] -->
Team #11422

<!-- b000232 | furniture | pages [16] -->
Page 16 of 20

<!-- b000233 | prose | pages [16] -->
7.8 Example Calculation

<!-- b000234 | prose | pages [16] -->
Knowing that governments tend to care about budgets, the following example will demonstrate how one could utilize these plots to calculate the beneﬁt to the environment on a constrained budget. Working from a $200 Billion dollar budget. We simply draw a horizontal line at 2 ∗1011, and then a vertical line at the point of intersection. This will become the α value used to lookup the power source values.

<!-- b000235 | prose | pages [16] -->
From here, one could either input this α, in this case, ≈37500, and use the

<!-- b000236 | prose | pages [16] -->
Nelder-Mead minimization to generate power source values, or one could graphically look up the values of the power sources. Pollution values can be calculated from these values, in percent change from the current emissions [2]

<!-- b000237 | furniture | pages [17] -->
Team #11422

<!-- b000238 | furniture | pages [17] -->
Page 17 of 20

<!-- b000239 | prose | pages [17] -->
7.9 Fossil Fuels Saved

<!-- b000240 | prose | pages [17] -->
Using data on average annual mileage of vehicles, we are going to assume that the annual mileage of a car stays constant from year to year, at 12,200 miles/year. The average miles per gallon is 31mpg. We also have our function C(t) for the number of cars at year t. This formula expresses the amount of fossil fuel saved over one year.

<!-- b000241 | prose | pages [17] -->
F(t) = 12, 200

<!-- b000242 | prose | pages [17] -->
31 · 20 · E · C(t) ≈19.68 · E · C(t)

<!-- b000243 | prose | pages [17] -->
7.10

<!-- b000244 | heading | pages [17] -->
Strengths and Weaknesses

<!-- b000245 | prose | pages [17] -->
Our macroeconomic model provides a quantitative and computationally inten- sive outlook of how to augment the power grid to attend to the increased demand caused by electric vehicles. It’s strength resides in its ability to minimize cost and pollution on the global scale. For a given α, say the budget to be spent on energy augmentations, we’ll be able to determine the amount of QBTU’s that need to be added to the current power grid, and how good that will be for the environment. We can also run this model in the opposite direction, so given an acceptable pollution, we can determine the cost needed to meet the energy demand. On the other hand, our model relies on many simplifying assumptions due to a lack of data. Certain things cannot be ﬁgured out, such as the demand curve behaviors and the maximum production limitations. Thus, given reliable data on these values, we can easily reconﬁgure our model and oﬀer a more ac- curate estimate. Additionally, the α value has an ambiguous, or at least veiled, meaning. It requires further interpretation to give real world values.

<!-- b000246 | furniture | pages [18] -->
Team #11422

<!-- b000247 | furniture | pages [18] -->
Page 18 of 20

<!-- b000248 | heading | pages [18] -->
Meshing the Micro and Macro Models

<!-- b000249 | prose | pages [18] -->
8

<!-- b000250 | prose | pages [18] -->
The government’s incentive program will allow a proportion of all cars in the ﬁrst year to be electric. Based on this seeding proportion, our diﬀerential equations microeconomic model predicts what proportion of vehicles will be electric in 2060. We can use these E values in our macroeconomic model to minimize pollution and cost. Adding the cost for the power grid in 2060 and the cost for seeding cars in 2011 will allow us to see what proportion should be seeded in order to save the most money. The following table shows sample seed proportions and the corresponding E values for 2060.

<!-- b000251 | prose | pages [18] -->
Proportion of Seeds 0.05 0.1 E in 2060 0.667 0.815 0.15 0.2 0.25 0.3 0.35 0.877 0.912 0.933 0.948 0.959

<!-- b000252 | prose | pages [18] -->
The following tables show the cost of the power grid and the total cost for a given α and the E values resulting from seeding.

<!-- b000253 | prose | pages [18] -->
If α = 0:

<!-- b000254 | prose | pages [18] -->
Power Grid Cost Seed Seeding Cost Total Cost 8.90292 · 1010 5.16348 · 1011 0.05 6.05377 · 1011

<!-- b000255 | prose | pages [18] -->
1.15992 · 1011 1.0327 · 1012 0.1 1.14869 · 1012

<!-- b000256 | prose | pages [18] -->
1.27262 · 1011 1.54854 · 1012 0.15 1.6758 · 1012

<!-- b000257 | prose | pages [18] -->
1.33811 · 1011 2.06514 · 1012 0.2 2.19895 · 1012

<!-- b000258 | prose | pages [18] -->
1.37837 · 1011 2.58174 · 1012 0.25 2.71958 · 1012

<!-- b000259 | prose | pages [18] -->
1.40766 · 1011 3.09834 · 1012 0.3 3.23911 · 1012

<!-- b000260 | prose | pages [18] -->
1.42946 · 1011 3.61494 · 1012 0.35

<!-- b000261 | prose | pages [18] -->
If α = 50, 000:

<!-- b000262 | prose | pages [18] -->
3.75789 · 1012

<!-- b000263 | prose | pages [18] -->
Power Grid Cost Seed Seeding Cost 5.16348 · 1011 0.05 Total Cost 1.6473 · 1011 6.81078 · 1011

<!-- b000264 | prose | pages [18] -->
1.94567 · 1011 1.0327 · 1012 0.1 1.22726 · 1012

<!-- b000265 | prose | pages [18] -->
2.09133 · 1011 1.54854 · 1012 0.15 1.75767 · 1012

<!-- b000266 | prose | pages [18] -->
2.18027 · 1011 2.06514 · 1012 0.2 2.28317 · 1012

<!-- b000267 | prose | pages [18] -->
2.23616 · 1011 2.58174 · 1012 0.25

<!-- b000268 | prose | pages [18] -->
3.09834 · 1012 0.3

<!-- b000269 | prose | pages [18] -->
2.80536 · 1012

<!-- b000270 | prose | pages [18] -->
2.2773 · 1011 3.32607 · 1012

<!-- b000271 | prose | pages [18] -->
2.30813 · 1011 3.61494 · 1012 0.35

<!-- b000272 | prose | pages [18] -->
If α = 200, 000:

<!-- b000273 | prose | pages [18] -->
3.84575 · 1012

<!-- b000274 | prose | pages [18] -->
Power Grid Cost Seed Seeding Cost Total Cost 2.20897 · 1011 5.16348 · 1011 0.05 7.37245 · 1011

<!-- b000275 | prose | pages [18] -->
2.47626 · 1011 1.0327 · 1012 0.1 1.28032 · 1011

<!-- b000276 | prose | pages [18] -->
2.59299 · 1011 1.54854 · 1012 0.15 1.80784 · 1012

<!-- b000277 | prose | pages [18] -->
2.66206 · 1011 2.06514 · 1012 0.2 2.33135 · 1012

<!-- b000278 | prose | pages [18] -->
2.70493 · 1011 2.58174 · 1012 0.25 2.85223 · 1012

<!-- b000279 | prose | pages [18] -->
2.73629 · 1011 3.09834 · 1012 0.3 3.37197 · 1012

<!-- b000280 | prose | pages [18] -->
2.75971 · 1011 3.61494 · 1012 0.35

<!-- b000281 | prose | pages [18] -->
If α = 500, 000:

<!-- b000282 | prose | pages [18] -->
3.89091 · 1012

<!-- b000283 | furniture | pages [19] -->
Team #11422

<!-- b000284 | furniture | pages [19] -->
Page 19 of 20

<!-- b000285 | prose | pages [19] -->
Power Grid Cost Seed Seeding Cost Total Cost 2.20897 · 1011 5.16348 · 1011 0.05 7.37245 · 1011

<!-- b000286 | prose | pages [19] -->
2.47626 · 1011 1.0327 · 1012 0.1 1.28032 · 1012

<!-- b000287 | prose | pages [19] -->
2.59299 · 1011 1.54854 · 1012 0.15 1.80784 · 1012

<!-- b000288 | prose | pages [19] -->
2.66206 · 1011 2.06514 · 1012 0.2 2.33135 · 1012

<!-- b000289 | prose | pages [19] -->
2.70493 · 1011 2.58174 · 1012 0.25 2.85223 · 1012

<!-- b000290 | prose | pages [19] -->
2.73629 · 1011 3.09834 · 1012 0.3 3.37197 · 1012

<!-- b000291 | prose | pages [19] -->
2.73629 · 1011 3.61494 · 1012 0.35 7.37245 · 1012

<!-- b000292 | prose | pages [19] -->
When α = 0, α = 50, 000, and α = 500, 000 the best seed is 5% of cars since this is when the total cost is the least. Even though the power grid cost is increasing with the seed proportion, the total cost between paying to seed cars and paying for the power grid is lowest when the seed is 5 −10%. When α = 200, 000, the best seed is 1% of cars. Once a government has determined the α value they would like to use, they could ﬁnd more E values corresponding to seed proportions and determine the total costs associated with that seed proportion. This would allow the government to spend just enough money on an incentive program to shift people towards electric cars while minimizing total cost between the incentive program and the pay oﬀin 50 years. For a seed of 10% and an α of 200,000, energy sources should be as follows:

<!-- b000293 | prose | pages [19] -->
Energy Source Petroleum Natural Gas Coal Renewable Nuclear

<!-- b000294 | prose | pages [19] -->
9

<!-- b000295 | heading | pages [19] -->
Conclusion

<!-- b000296 | prose | pages [19] -->
Quadrillion BTUs 35.3 26.15 25.95 10.45 10.3

<!-- b000297 | prose | pages [19] -->
We have modeled the eﬀects of electrical vehicle usage by examining their envi- ronmental, social, economic, and health eﬀects. First, we examined the spread of electrical vehicle usage based on the individual. We did this in two ways: using coupled diﬀerential equations to model global inﬂuence, and using a two- dimensional cellular automata to model local and global inﬂuence. In order to initiate the transition to widespread electric vehicle usage, the government could create an incentive program to seed a proportion of electric vehicles. Secondly, we used algorithms to minimize cost and pollution for a given year based on the proportion of cars which are electric and the value of α. The value of α allows governments to measure how much they value decreasing pollution with minimizing cost. Finally, we combined these models to determine the propor- tion of cars which would need to become electric in 2011, for a given α, which would transition the population to electric cars and minimize overall cost. Our model suggests that the government should create an incentive program so that 5%-10% of cars are electric in 2011. This will allow for the minimal cost. In order to support the increase in electric cars, the power grid should increase by the following quadrillion btus: petroleum: 0, natural gas: 2.75, coal: 6.25, renewable: 2.75, and nuclear: 2.

<!-- b000298 | furniture | pages [20] -->
Team #11422

<!-- b000299 | furniture | pages [20] -->
Page 20 of 20

<!-- b000300 | heading | pages [20] -->
References

<!-- b000301 | references | pages [20] -->
[1] Average fuel eﬃciency of u.s. passenger cars and light trucks. (2010, Novem-

<!-- b000302 | references | pages [20] -->
ber 30). Retrieved from: http://www.bts.gov/publications/national_

<!-- b000303 | references | pages [20] -->
transportation_statistics/html/table_04_23.html

<!-- b000304 | references | pages [20] -->
[2] BP Statistical Review of World Energ. (2010,

<!-- b000305 | references | pages [20] -->
Jun). Retrieved from:

<!-- b000306 | references | pages [20] -->
http://www.bp.com/liveassets/bp_internet/globalbp/globalbp_

<!-- b000307 | references | pages [20] -->
uk_english/reports_and_publications/statistical_energy_review_

<!-- b000308 | references | pages [20] -->
2008/STAGING/local_assets/2010_downloads/statistical_review_

<!-- b000309 | references | pages [20] -->
of_world_energy_full_report_2010.pdf

<!-- b000310 | references | pages [20] -->
[3] International Energy Annual. (2009, Jan 21). Retrieved from http://www.

<!-- b000311 | references | pages [20] -->
eia.doe.gov/emeu/iea/

<!-- b000312 | references | pages [20] -->
[4] Li-Ion Motors. (2011). Retrieved from http://ceocentral.com/m/store/

<!-- b000313 | references | pages [20] -->
view/LMCO-Li-ion-Motors-Corp

<!-- b000314 | references | pages [20] -->
[5] Manaham, S.E. (1991). Environmental Chemistry. Chelsea, MI: Lewis Pub-

<!-- b000315 | references | pages [20] -->
lishers.

<!-- b000316 | references | pages [20] -->
[6] Natural gas and the environment. (2010). Retrieved from: http://www.

<!-- b000317 | references | pages [20] -->
naturalgas.org/environment/naturalgas.asp

<!-- b000318 | references | pages [20] -->
[7] U.S. Primary Energy Flow by Source and Sector. (2009). Retrieved from:

<!-- b000319 | references | pages [20] -->
http://www.eia.doe.gov/aer/pecss_diagram.html

<!-- b000320 | references | pages [20] -->
[8] Wright, R.T. (2005). Environmental Science. Uppder Saddle River, NJ:

<!-- b000321 | references | pages [20] -->
Pearson Prentice Hall.

<!-- b000322 | references | pages [20] -->
[9] Paine, Chris (Director). (2006). Who Killed The Electric Car? [DVD].

<!-- b000323 | references | pages [20] -->
[10] U.S. Census Bureau, (2010). World population: 1950-2050 Retrieved from

<!-- b000324 | references | pages [20] -->
http://www.census.gov/ipc/www/idb/worldpopinfo.php
