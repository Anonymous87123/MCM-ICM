Summary Sheet

Due to the eﬀects of global warming, rising ocean water temperatures are causing ﬁsh to migrate northward in search of cooler waters. With the success of ﬁshing companies dependent on their proximity to ﬁsh, this poses a problem for small ﬁshing companies who do not have the resources to reach migrating ﬁsh. Particularly worrisome is the northward migration of Atlantic herring and Atlantic mackerel - the two most valuable species in the Scottish ﬁshing industry.

First, to predict future ocean temperatures in the Scotland region, we computed a linear regression equation for each geographic coordinate that predicts temperature as a function of time based on historical sea surface temperature data. This allows for diﬀerent geographical locations in our model to change temperature at diﬀerent rates. Overall, we found that Scotland region ocean temperature increases an average of 1.59°C over 50 years.

Then, to predict ﬁsh migration patterns, we developed an agent-based model with ﬁsh schools stochastically moving on a dynamic ﬁeld of ocean temperatures that change according to the linear regression equations, which is used to represent gradient and partial derivative equations that form the basis for each ﬁsh’s decision making behavior on a micro-scale. This model took into account a wide variety of relevant factors and parameters, including total population, initial spatial density distributions, and optimal temperature ranges for each species, number of ﬁshing vessels, vessel capacity, ﬁshing area radius, catch proportion, etc., all based on information from reputable sources. Our scalable model allows for visualization of migration patterns over time - overall, herring and mackerel migrate to the northeast towards Iceland, though herring migrate much more rapidly due to their colder preferred temperatures.

Next, to assess the impact of ﬁsh migration on small ﬁshing companies, we evaluated viability of diﬀerent ﬁshery locations by measuring time until ﬁsh migrate out of range and total revenue for each of 87 spots along Scotland’s coastline. Additionally, to test the sensitivity of our model, we used the statistical variation in the sea surface temperature data to estimate the most likely, best, and worst case scenarios for both herring and mackerel. Herring are projected to leave the coast of Scotland by 2051 (2038 in the worst case, 2056 in the best case); with their higher temperature tolerance, the earliest mackerel are projected to migrate out of reach by the early 2060s.

By utilizing the temperature-dependent migratory patterns of our simulated ﬁsh, we were able to determine revenue through a time-sensitive assessment of the number of schools within ﬁshing radius for each location. Herring is expected to return a maximum of $42 million, while mackerel can return up to $204 million in the Shetland Islands. Although mackerel were more proﬁtable in the long run than herring, the revenue, regardless, substantially decreases both over time and for more southern locations for both species.

In order to recoup the loss in revenue, we proposed and tested 3 solutions: relocating ﬁshing ports, harvesting haddock (a diﬀerent species), and upgrading vessel assets. Out of the 87 possible coastal locations, the Shetland Islands were the best possible location, with revenue generally decreasing moving southward. Harvesting haddock proved to be more constantly proﬁtable, as their range is more southern and they migrate into Scotland waters. Finally, upgrading ﬁshing vessels to include on-board refrigeration was found to increase revenue by around 43% in the north to over 1700% in the south.

We created an eﬀective and robust model to predict the patterns of ﬁsh migration over time due to climate change and their impact on small ﬁshing companies on the coasts of Scotland. Additionally, our thorough analysis of the impacts of parameter variation and possible solutions for ﬁshing companies allows for ﬁshermen to understand the severity of the oncoming crisis.

A Fishy Situation

As the eﬀects of climate change continue to have a widespread impact on the environment, with the Australia bushﬁre crisis being the latest example, the ﬁsh are no exception. The rising ocean water temperatures have forced ﬁsh to migrate to cooler waters in order to ﬁnd more suitable habitats. Particularly of concern for Scotland are the forced migration of the Atlantic herring and Atlantic mackerel, two of the most valuable species for our ﬁshing industry.

With temperatures in Scotland region predicted to increase by 1.59°C in the next 50 years, current models project the Atlantic mackerel to migrate away from northwestern Scotland and towards the general direction of Iceland. While populations of mackerel may still dot the coasts of Scotland in the future, the numbers are predicted to be substantially less than current values. Even worse, the models for Atlantic herring forecast herring to move northwest to the region just east of Iceland by 2070, leaving no herring within ﬁshing radius from the coasts of Scotland. The southern and western coasts of Scotland are expected to be most impacted by this migration, losing access to the herring within the next 20 years.

Additionally, with the migration of the ﬁsh into Iceland and Greenland’s exclusive economic zones, these territories will gain a larger say on the ﬁshing quota distribution having free reign to decrease the quota of ﬁsh that Scotland is allowed to harvest. This may cause a trickle-down eﬀect, limiting the quantity of ﬁsh available to small ﬁshing companies.

With the realization that empty oceans and empty pockets will soon become a reality, it is more important than ever to prepare now for the future. In an eﬀort to combat the forecasted loss in revenue, we suggest the following 4 strategies:

1. Relocate northward to a better situated ﬁshing port (ex. Shetland Islands) - Financial models project ﬁshing companies in the north to generate over $42 million in revenue in the next 50 years with current methods, compared to a paltry half a million for companies in the south.

2. Transition from harvesting herring to harvesting more mackerel - Although not immune, mackerel are expected to be more resistant to temperature changes in the upcoming years.

3. Begin harvesting haddock - With a large population south of Scotland that will only move northwards, haddock are a smart long-term harvest option.

4. Upgrade current ﬁshing vessels’ assets - If you’re not already ﬁlling your vessels’ capacities, upgrading to on-board refrigeration or faster motors can net an increase in revenue anywhere from 50% to over 1700%.

These are only a few of the many options possible to recoup the ﬁsh and the revenue. But without a doubt, the time is now to ensure no empty ﬁshing nets in the future. Take action now!

1 Introduction

1.1 Problem

In response to rising ocean temperatures, ﬁsh species such as Atlantic herring and Atlantic mackerel are migrating to ﬁnd more suitable habitats. However, these migrations come at a cost to coastal ﬁshing companies, especially small ones, whose livelihood relies on the ﬁsh’s proximity to their ﬁshing ports. Given the potentially devastating eﬀects of rising ocean temperature, careful analysis is necessary to determine the best path forward for small ﬁshing companies.

As consultants for the Scottish North Atlantic Fishery Management Consortium, our objective is to model the change in location of the Atlantic herring and Atlantic mackerel species over the next 50 years and the consequent economic impact on small Scottish ﬁshing companies. We also aim to explore possible strategic improvements to the ﬁshing companies’ operations to combat the detrimental eﬀects while taking into account the restrictions set forth by territorial water restrictions and international boundaries.

1.2 Problem Analysis

With ocean temperatures rising due to heat absorption caused by excess atmospheric greenhouse gases, many ﬁsh species are migrating away from their current locations to seek cooler waters [1]. Of particular economic importance for the North Atlantic Scotland region are the Atlantic herring and Atlantic mackerel species, which respectively account for 8% and 30% of the total value of Scottish landings in 2016, with the latter being the most valuable species [2]. Known to be sensitive to water temperature, herring and mackerel migrations have already been recorded. For example, between 1968 and 2008, the overwintering distribution of the Northwest Atlantic mackerel stock shifted 250 km north and 50 km east [3]. Consequently, small ﬁshing companies, lacking the ﬁnancial resources to quickly adapt their ﬁshing vessels and practices, are faced with the stark reality that the number of harvestable ﬁsh within their reach is slowly decreasing to zero.

Companies have several options to combat these changes, including relocating their ﬁshing ports (following the path of the migrating ﬁsh), harvesting a new species of ﬁsh, or upgrading their ﬁshing vessels to allow for longer ﬁsh storage. However, these options have substantial upfront costs. For instance, renting or buying a new ﬁshery costs up to $400,000, plus the overhead cost of transferring or hiring new ﬁshermen. Harvesting diﬀerent species of ﬁsh requires new ﬁshing permits as well as upgrading ﬁshing vessels to include diﬀerent types of nets and traps [4]. Finally, adding on-board refrigeration can cost up to $10,000 per vessel [5]. Thus, it is particularly important to model the options and propose guidelines to mitigate the ﬁsh migration problem.

Here, we list out the aspects of the problem that we aim to address along with the section(s) in this paper where they are discussed:

• How has the ocean temperature near Scotland changed, and how will it continue to change in the next 50 years? (Methods in Section 2.3; Results in Section 3.1)

• How does the changing ocean temperature aﬀect the long-term migration of herrings and mackerels? (Section 3.2)

• How long will it be before the ﬁsh populations move beyond the ﬁshing areas of the small ﬁshing companies, for the best and worst case scenarios of temperature change? (Section 3.3)

• What is the economic impact of the migrating ﬁsh on small ﬁshing companies? How can the ﬁshing companies attempt to combat the loss, either through moving port locations, ﬁshing for new species, or upgrading vessel assets? (Methods in Section 2.5.3; Results in Section 3.3)

• How are the proposed solutions impacted by the limitations placed on ﬁshing by territorial waters? (Section 5)

Taking into account the changing ocean temperatures, the processes of ﬁsh migration on a population-by-population basis form a complex system consisting of species-speciﬁc interactions and the behavior within the species. To represent such a random system, we choose an agent-based model that simulates the proﬁt of small ﬁshing companies in relation to the moving ﬁsh populations in a stochastic manner.

By implementing initial spatial densities for the ﬁsh, an adaptive temperature portfolio for the Scotland region, and appropriate ﬁsh decision-making behavior into the agent-based model, we aim to create a robust and accurate model to predict the movement of ﬁsh populations, the proﬁt available to the small ﬁshing companies, and the best possible operational strategies moving forward.

2 Methodology

Our primary objective is to create a model to estimate the location of herrings and mackerels over the next 50 years based on changing ocean temperatures in the Scotland North Atlantic region. Using this base model, we plan to identify the range of possible temperature changes to explore the best and worst cases for the small ﬁshing companies. Finally, by analyzing our model’s results, we will propose initiatives and guidelines to reduce the detrimental costs for small ﬁshing companies associated with the migration of the ﬁsh while keeping in mind the restrictions imposed by territorial waters.

2.1 General Deﬁnitions

Catch Proportion: The proportion of ﬁsh gained per harvesting attempt.

Disappearance Time: The amount of time, in days elapsed since Jan. 1st 2006, until all schools of ﬁsh migrate out of a port’s harvesting radius. It diﬀers for each possible ﬁshing port location.

Exclusive Economic Zone (EEZ): Exclusive economic zone is a sea zone over which a state has special rights regarding the exploration and use of marine resources. It extends no more than 200 nautical miles from the coastline [6].

Harvestable Radius/Harvesting Range: The radius that a ﬁshing vessel from a small ﬁshing company can harvest ﬁsh from, an average distance of 51 km for vessels under 12 m in length [7].

Fishing Port/Company Location: Where the ﬁshing vessels of a company depart from.

Herring: Refers to Atlantic herring (Clupea harengus), which are prevalent in the North Sea.

Mackerel: Refers to Atlantic mackerel (Scomber scombrus), which are the most abundant pelagic species landed in the Scottish ﬂeet by weight [2].

Migration: Migration refers to the long-term movement of the ﬁsh to a diﬀerent central location. Unless otherwise noted, it does NOT refer to seasonal migrations of ﬁsh throughout a year.

On-Board Refrigeration: On-board refrigeration includes mechanical cooling and freezing equip- ment. A ﬁshing vessel may still utilize icing methods without on-board refrigeration.

School of Fish: Herrings and mackerel, travel in groups, or schools, of up to 100,000 ﬁsh [8].

Scotland Region: Deﬁned from N50° to N60° in latitude and W15° to E5° longitude. This includes all of the British Isles as well as other sovereign territory.

Small Fishing Company: A company with limited ﬁnancial resources that harvests ﬁsh and has a ﬂeet of 10 small ﬁshing vessels. Note that the number of vessels a small ﬁshing company has is inconsequential to migration pattern and revenue trends.

Small Fishing Vessel: The boat used by commercial ﬁsherman to harvest ﬁsh, usually a trawler when harvesting mackerel or herring. Classiﬁcations for small vessels under the European Maritime and Fisheries Fund denote vessel length to be less than 12 meters [7].

Territorial Waters: A belt of coastal water that extends to at most 12 nautical miles from the edge of a coastal state. It is under the jurisdiction of the land state and ﬁshing is reserved to nationals of the controlling state. [9]

2.2 General Assumptions

Assumption: With no on-board refrigeration, the ﬁsherman gut and ice the ﬁsh as soon as they are pulled out of the water.

Justiﬁcation: In order to preserve the freshness of the ﬁsh, the general recommended method is to gut the ﬁsh and ice it, with the water from the melted ice removed periodically [10]. Assumption: The price of herrings and mackerel remain constant across Scotland.

Justiﬁcation: Macroscopically thinking, the markets along the coast of Scotland are impacted by the same factors, causing the variation of prices between markets to be insigniﬁcant. Assumption: The population of harvestable herrings and mackerels reside near the surface of the water, making temperature changes in relation to ocean depth inconsequential.

Justiﬁcation: While herring and mackerel reside between the surface and deep in the water depending on the time of the day [2], ﬁsherman are more likely to harvest ﬁsh near the surface of the water. Since our populations of interest reside near the surface, diﬀerent depths of water are not relevant. Assumption: The small ﬁshing companies are equipped with trawlers, which travel no faster than 4 knots and speciﬁcally use midwater trawling methods [11].

Justiﬁcation: Trawlers are generally used for small scale ﬁsheries [12], and pelagic ﬁsh, the category of ﬁsh that herring and mackerel fall under, are ﬁshed using trawling methods. Assumption: Advanced technology has allowed vessels to quickly identify the location of various ﬁshing population.

Justiﬁcation: Using ultrasound waves, acoustics, and other ﬁsh detecting machinery, ﬁsher- men are able to quickly detect and harvest their target ﬁsh [13]. Assumption: Herring and mackerel population size stay constant over the next half century.

Justiﬁcation: With female herring having the ability to produce between 30,000 and 200,000 eggs and female mackerel between 285,000 and 2,000,000, the birth rate of the ﬁsh compen- sates for eﬀects of natural death and ﬁshing [14]. Additionally, governments issue ﬁshing quotas to prevent overﬁshing and keep the population size constant [15]. Assumption: The time to capture ﬁsh is insigniﬁcant in comparison to the travel time for the boats.

Justiﬁcation: The process of midwater/pelagic trawling involves sending a net into the middle (depth-wise) of the ocean and scooping ﬁsh up. Thus, the capture of ﬁsh occurs simultaneously with the movement of a vessel to a population location and does not require additional time. Assumption: The eﬀects of global warming, and speciﬁcally sea surface temperature, will continue to increase at a similar rate as today for the next 50 years.

Justiﬁcation: Despite valiant eﬀorts, it will take decades to fully cease unsustainable prac- tices and slow the eﬀects of climate change. See Section 2.3 for quantitative justiﬁcation. Assumption: Seasonal changes in regards to temperature ﬂuctuations are unnecessary to take into account when attempting to observe the global trend of increasing temperature and its eﬀects.

Justiﬁcation: Although seasonal variation would cause annual oscillations of the region location for a ﬁsh’s optimum temperature, it is inconsequential as we are more interested in the overall movement of this region through a long-term time period of 50 years.

2.3 Ocean Temperature Projections

Using the National Oceanic and Atmospheric Administration (NOAA)’s measurements of sea surface temperature (SST) from 1982 to present day [16], we plotted SST in our Scotland region at a resolution of 0.25° in both latitude and longitude, eﬀectively creating an 80 by 64 grid of cells with length ∼27.75 km. The SST in °C maps to a color gradient, with warmer red tones seen in the southern waters transitioning to cooler purple and blue tones in the north (Fig. 1).

water bodies, and major landmarks are labeled.

For each (latitude, longitude) coordinate (푖, 푗), a linear regression line was ﬁtted using Python in the form 푇(푖,푗) = 퐴∗(days since Jan. 1st 1982) + 퐵 (1) where 푇is SST, 퐴represents the change in SST per day, and 퐵represents the starting SST in °C (e.g., Fig. 2). This allows each geographical coordinate to change temperature independently at a rate that is calculated based on historical data.

The residual plots show no high level structure, suggesting that a linear ﬁt is appropriate and supporting the prior assumption. Note that although temperatures ﬂuctuate greatly based on time of year, the ﬁsh’s natural seasonal migration patterns should allow them to mitigate this; the linear regression lines can be thought of as representing temperature in spring and fall and accurately represent average temperature trends in the long run.

Heat maps showing the 퐴and 퐵values for each latitude and longitude coordinate are shown in

1982 varies from 3°C to 13°C.

(a) A values (b) B values

time at each geographical coordinate.

From the linear regression lines, the SST at any latitude and longitude at any number of days in the future can be projected.

2.4 Fish Migration Model

An agent-based model was programmed in NetLogo to account for the random variation inherently present in such a system of interacting components in a changing environment; it models the migration of ﬁsh schools in response to rising ocean temperatures. Each agent represents a school of ﬁsh, which moves around the map according to a stochastic process that is constrained by deﬁned behavioral rules.

2.4.1 Agent-based Model Assumptions

Assumption: A school of ﬁsh dies after spending 7 days in intolerable temperature.

Justiﬁcation: A population consisting of hundreds and thousands of individuals would not die in a single day; however, prolonged exposure to temperatures above a ﬁsh’s tolerable limit would stress them out and eventually kill them. Assumption: Schools are not aﬀected by population density.

Justiﬁcation: There are enough nutrient resources within the approximately 27.75 km2 cells of the map to support any number of ﬁsh schools. Assumption: A school’s migration is aﬀected only by water temperature.

Justiﬁcation: Temperatures rising above the optimal levels for herring and mackerel are the most potentially fatal problem for the ﬁsh and thus govern where a school migrates. Factors such as predation and pollution are diﬃcult to assess and in the long-term will not aﬀect populations as drastically in the coming years.

2.4.2 Number of Schools in the North Sea

Since there is no direct data on the total harvestable population size of herring and mackerel, population sizes were estimated using the number of captured ﬁsh in Scotland in 2018 [2] and the average mass of each ﬁsh [17]:

38138 푚푒푡푟푖푐푡표푛푠∗1000000 푔푟푎푚푠 ∗1 ℎ푒푟푟푖푛푔 250 푔푟푎푚푠= 1.525 ∗108 ℎ푒푟푟푖푛푔 (2) 1 푚푒푡푟푖푐푡표푛 Since herring traveling in schools numbering 20,000 ﬁsh, we estimated that the total number of schools in the Scotland area is 8, 000. Utilizing 75, 022 tonnage of ﬁsh and 400 grams as the average weight for one mackerel, we found that the 1.875 ∗108 accessible mackerel travel in approximately 4, 000 total schools.

2.4.3 Initial Distribution of Fish

In order to initially distribute the schools of ﬁsh within the Scotland region, we utilized spatial density distribution data for herring and mackerel in the form of a latitude-longitude graph divided into ICES statistical rectangles (area deﬁned by 30 miles latitude and 1° longitude) [18]. Each statistical rectangle had the mean amount of herring/mackerel observed from that location from 2003-2006. The NetLogo model took the rectangle coordinates and scaled density values as input to distribute 70% of the total schools according to these distributions. To account for schools not recorded in this particular data-set, the remaining 30% of schools were randomly distributed in the remaining Scotland region. In this way, the initial distributions take into account real species densities, allowing the model to more accurately represent the diﬀerences between herring and mackerel, and how their populations are aﬀected by rising ocean temperatures.

2.4.4 Path of Fish Schools

In order to model ﬁsh migration, we imagine a temperature scheme in which each longitude- latitude coordinate pair (푥, 푦) correlates to a singular value which can be represented by the function 푇푠(푥, 푦). More important for understanding a school’s direction of travel than simply the temperature of a cell is the absolute diﬀerence (퐷푡) between this temperature and a ﬁsh’s optimum temperature (퐹표푡), 퐷푡= |푇푠−퐹표푡| (3) By taking the partial derivatives of 퐷푡with respect to 푥and 푦, we can create a gradient vector

∇퐷푡=< 휕퐷푡 휕푥, 휕퐷푡 휕푦> (4)

which points in the direction a ﬁsh would move to be in temperatures further away from its optimum. Thus the true direction a ﬁsh would move is represented by −∇퐷푡.

The path the ﬁsh actually take can be thought of as a vector-valued function ®푅(푡) which produces vectors that point to the ﬁsh’s coordinate location at some point in time. The direction in which they are moving in is deﬁned by the tangent vectors created by the function ®푅(푡) and thus can be thought of as ®푅′(푡). Understanding that ®푅′(푡) and −∇퐷푡are equivalent allows us to derive the equation for the path of the school.

−휕퐷푡 휕푥= 푑푥 −휕퐷푡 휕푦= 푑푦 (5) 푑푡 푑푡 푑푡and 푑푦 Integrating 푑푥 푑푡with respect to time gives the function that represents the path of the ﬁsh,

®푅(푡) =< 푥(푡), 푦(푡), 0 > (6)

It is important to note that both the temperature of the ocean and the path of the ﬁsh are dependent on the variable 푡, so they are both changing with respect to the same time increments.

2.4.5 Path of the Schools of Fish in NetLogo

To implement the above movement pattern, our Netlogo model follows an equivalent logic but on a discrete temperature surface that is updated daily based on the linear regression equations. Instead of following gradient vectors, the schools were programmed to move to one out of the eight adjacent patches that has a temperature closest to their optimal.

To model realistic movement patterns, each school has an optimal, a staying, and a tolerable temperature that depend on the species (Table 1). A school by default does not move if it is comfortable where it is; it only looks to move if the current ocean temperature is greater than their staying temperature. In this case, it steps in the direction closest to its optimal temperature to ﬁnd a cooler region. However, if it wants to move but is stuck in a local minimum, it enters "escape mode", stepping in a random direction for a random number of days (≤10) in search of a better path.

Finally, if the school is in a patch with ocean temperature exceeding its intolerable temperature for 7 days, it dies.

Optimal Temperature Staying Temperature Tolerable Temperature Herring 4.6°C 9°C 12°C Mackerel 5°C 12°C 25°C

The model is started in year 2006, when the spatial density distribution is known. Each time step represents a single day. In a day, each school is allowed to take a small step forward according to the rules described above. Then, each cell’s temperature is recalculated for the following day according to the linear regression equations, before the schools move again. This dynamic process of moving schools and updating temperatures is iterated until the desired year is reached.

2.5 Fishing Company Model

2.5.1 Capacity of Fishing Vessel

To estimate the capacity of a ﬁshing vessel, we used Scottish Fleet data on the number of vessels, 1539 vessels under the length of 10 m, and the corresponding tonnes of mackerel captured, 1070 tonnes by these vessels [2] resulting in

1079 푚푒푡푟푖푐푡표푛푠 ∗1, 000, 000 푔푟푎푚푠 ∗1 푚푎푐푘푒푟푒푙 400 푔푟푎푚푠= 1750 푀푎푐푘푒푟푒푙/푉푒푠푠푒푙 (7) 1539 푣푒푠푠푒푙푠 1 푚푒푡푟푖푐푡표푛

With the maximum capacity of the ﬁshing vessel dependent on the amount of weight a ﬁshing vessel can carry, we use the weight of a herring, 250 grams, to calculate that the carrying capacity of herring for a vessel is approximately 2800 herring.

2.5.2 Catch Proportion

A ﬁlled net weighs around 45 kilograms with the net itself weighing around 5 kg [22]. Relating the total weight of the ﬁsh caught in one trip to the maximum capacity of the ﬁshing vessel, we have (45 푘푔−40 푘푔) ∗1000 푔 1 퐹푖푠ℎ 1 푉푒푠푠푒푙 푉푒푠푠푒푙퐶푎푝푎푐푖푡푦표푓퐹푖푠ℎ= 5.7% ∗ 푊푒푖푔ℎ푡표푓1 퐹푖푠ℎ푔∗ (8) 1 푘푔

as the catch proportion for herring and mackerel.

However, for every pound of target ﬁsh (herring or mackerel) harvested, approximately 20 pounds of unwanted bycatch is harvested as well [23]. Consequently, we set catch proportion to vary randomly from 3-7% for every harvesting attempt to account for the bycatch variation and the possibility of obtaining more than 40 kg of ﬁsh in one harvesting attempt.

2.5.3 Price of Fish

In order to understand the speciﬁc impacts of the migration on a ﬁshing company’s revenue, we calculated price per harvested ﬁsh. Using the tonnage of each ﬁsh caught and their associated value in the ﬁshing industry [2], we computed the price of mackerel as

e163, 699, 000 ∗ $ 1 e0.92 = $ 0.50 (9) 106 푔 1 푚푒푡푟푖푐푡표푛∗1 푚푎푐푘푒푟푒푙 153, 000 푚푒푡푟푖푐푡표푛푠푚푎푐푘푒푟푒푙∗ 400 푔 The equation above can be used to calculate the price per herring by using 64, 622 tons as the tonnage of herring caught, 250 g as the average weight of one ﬁsh, and e 24, 377, 000 as the value of total harvested herring,

2.5.4 Fishing Companies in NetLogo

As the ﬁsh dynamically follow their temperature-dependent paths, the impact of their movement on a ﬁshing company is simultaneously simulated. A ﬁshing port located at a single speciﬁed coastline point sends out 10 ﬁshing vessels every day, which visit each school of ﬁsh within the port’s ﬁshing radius. At each school, a vessel catches 3-7% of ﬁsh until it either reaches maximum capacity or there is no more schools in the radius. The revenue is simply computed as the total number of ﬁsh caught times the price per ﬁsh. The disappearance time is recorded as the last day that any school of ﬁsh is within the port’s ﬁshing radius (Fig. 4).

3 Results and Analysis

3.1 Ocean Temperature Projection Results

Using the linear regression lines unique to each geographical coordinate, we predicted the ocean water temperature in 50 years (Fig. 3b). Consistent with historical trends, the average ocean temperature in the Scotland region rose 1.59°C over 50 years, from 10.46 °C in 2020 to 12.05°C in 2070. Graphically, red dominates the 2070 map even more than in 2020.

Analyzing speciﬁc geographic coordinates, we observe the variations in temperature change between diﬀerent locations. For instance, the temperature east of Iceland barely changes, while the temperature east of England increases by around 2°C.

3.2 Projected Migration of Fish

From our predictive ocean water temperature model, we projected the eventual location of Atlantic herring and Atlantic mackerel.

3.2.1 Herring Migration

As described in Section 2.4.3, the initial distribution of harvestable herring in the Scotland Re- gion was based on 2006 mean catch density with additional random distribution in the surrounding areas. The majority of herrings populate the area between the NE coast of Scotland and Shetland Islands (Fig. 6a). By 2020, the majority of herring have migrated northward towards the cool region of water extending east from Iceland; however, there is still clustering around the NE Scottish coast, Shetland Islands, and Faroe Islands (Denmark) due to the slightly cooler temperatures surrounding land (Fig. 6b). Over time, these remaining populations grow sparse, and all herring migrate past Scottish lands by 2070 into the waters east of Iceland (Fig. 6f).

(b) 2020 projection (a) Jan. 1st, 2006 distribution (c) 2030 projection

(d) 2050 projection (f) 2070 projection (e) 2060 projection

Each yellow ﬁsh represents a school of herring numbering around 20,000 individuals.

3.2.2 Mackerel Migration

According to the 2006 initial spatial density distributions, mackerel schools populate an arc shape oﬀthe western coast of Ireland and the northwestern coast of Scotland, extending past the Shetland Islands (Fig. 7d). Then, over the next 25 years, the ﬁsh slowly migrate northward in a wave-like fashion, moving past Ireland and congregating in the region northwest of Ireland (Fig. 7c). The ﬁsh continue to migrate northwards in response to increasing temperatures; by 2070, the population around the Shetland Islands remains, tiny scattered clusters exist south of Aberdeenshire, and the remaining population forms a line between Scotland and the Faroe Islands (Fig. 7f).

Compared to herring, mackerel are able to exist in higher temperatures without moving, so their population does not show as much northward movement. Additionally, unlike with herring, scattered mackerel populations are still stuck as far south as below England, attributable to the fact that mackerel do not actually die until 25°C.

(a) Jan. 1st, 2006 distribution (b) 2020 projection (c) 2030 projection

(d) 2050 projection (e) 2060 projection (f) 2070 projection

Each green ﬁsh represents a school of mackerel numbering around 20,000 individuals.

3.3 Disappearance Time and Revenue

To understand how disappearance time and revenue vary based on the location of the ﬁshing company, 3 repeat NetLogo simulations were run for each of the 87 Scottish coastline locations where a ﬁshing port could be located. The disappearance times and revenues recorded for each location were averaged to produce maps geographically colored by disappearance time and revenue (Fig. 8). Note that the disappearance times do not produce true averages, since if ﬁsh were still present in 2070, the disappearance time was cut oﬀthere.

coastline locations.

For herring, the estimated average disappearance time is 16,584 days from 2006, which is around 2052. Fishing ports in the Orkney Islands, south of Aberdeenshire, and the Shetland Islands recorded the longest disappearance times, and subsequently the greatest revenues of $26 million, $36.3 million, and $44 million, respectively (Fig. 8a and b). This is due to the initial concentration of herring in these areas (Fig. 6a). However, the herring distribution is very non-uniform, so in the southwest side of Scotland, it is observed that more inland locations tend to lose access to ﬁsh faster and post a lower revenue (with the lowest being $2,540). Thus, for herring ﬁshing over the next 50 years, Orkney Islands, south of Aberdeenshire, and Shetland Islands are the recommended locations; if these are not possible, northern and coastal locations are preferred.

For mackerel, the estimated average disappearance time is 21,168 days from 2006, which is around 2064, over 8 years after the herring. Due to the widespread initial distribution of mackerel and their higher temperature tolerance, mackerel migrate at a slow rate (Fig. 7). Consequently, a majority remain in the Scotland region after 50 years, as seen by the prevalence of neon green along most of the coast of Scotland (Fig. 8c). The best places for mackerel revenue are the Shetland Islands, the northern Highlands, and the Outer Hebrides, projected to make $204 million, $163 million, and $65 million respectively (Fig. 8d). However, companies in the eastern Firth of Forth inlet suﬀer a more pessimistic forecast of less than $30,000, as their initial accessibility to mackerel was already severely limited (Fig. 7d). Thus, for mackerel ﬁshing over the next 50 years, Outer Hebrides, Shetland Islands, and the northern coast are the recommended locations, with the peninsulas on the southwest side also serving as viable options. Additionally, in general, mackerel ﬁshing is more lucrative than herring due to the more widespread range and higher price per ﬁsh.

3.3.1 Sensitivity Analysis: Best and Worst Cases

In addition to the baseline SST recordings, the NOAA provides an estimated standard deviation associated with each measurement. To assess sensitivity to ocean temperature, the model was run under the lower and upper limit ocean temperature change conditions, calculated by respectively subtracting and adding 1.96 ∗푠푡푑. 푑푒푣. to the baseline measurements to cover a 95% conﬁdence interval. After re-running linear regressions for each coordinate in both scenarios, we re-ran the NetLogo simulations to measure the impact of the temperature gradient on disappearance time of the herring and mackerel (Fig. 9).

change scenarios.

For herrings, as expected, the lower limit temperature change scenario increases average disap- pearance time by nearly 5 years (i.e., herring stay within ﬁshing radii for 5 more years) (Table 2). This is especially clear in southwest Scotland, which is greener than the baseline scenario (Fig. 9a). This is due to the fact that the herring take longer to migrate northwards if the ocean temperature in- creases at a slower rate. On the other hand, if ocean temperature increases faster in the upper limit scenario, disappearance time signiﬁcantly decreases, apparent in the whitish-colored southwest coastlines (Fig. 9b). The large changes in disappearance time when the temperature increase rate changes shows the ocean water temperature has a signiﬁcant impact on school migration patterns.

Interestingly, the eﬀect seems reversed for mackerel. In the lower limit temperature change case, more locations in west Scotland are colored white (never see mackerel come within ﬁshing range), and average disappearance time decreases by 556 days (Fig. 9c). On the other hand, in the upper limit case, the average disappearance time actually increases slightly by 286 days (Table 2). The randomly distributed mackerels southeast of Scotland are responsible for this seemingly backwards eﬀect. When the temperature increase is slower, it does not rise enough to force these schools to move northward. However, when the temperature increases at upper limit, the schools migrate north, passing by the east coast of Scotland and beneﬁting the ﬁshing ports there. Over a longer time period, perhaps 100 years, as mackerel follow herring and move northwards, the upper limit scenario would indeed perform worst as expected; however, with the initial mackerel distribution already favoring the east side and with rising temperatures not greatly aﬀecting disappearance time, 50 years is not a long enough time to see rising ocean temperatures aﬀect mackerel ﬁshing in most of Scotland, which is why the north, west, and south coasts are always green (Fig. 9c,d).

Herring Disappearance Time Mackerel Disappearance Time Upper limit temp. increase 11974 21454 Baseline 16584 21168 Lower limit temp. increase 18328 20612

scenarios of ocean temperature increase in coastline locations.

4 Suggested Strategies and Guidelines

Due to the northward migration of herring and mackerel, small ﬁshing companies will soon be unable to reach them. To alleviate the economic strain caused by this phenomenon, we propose the following strategies and use our model to explore each.

4.1 Relocating Fishing Ports

Perhaps the most direct and obvious solution is to follow the path of the migrating ﬁsh and relocate and/or construct new ﬁshing ports towards the north of Scotland. To assess the potential gains in revenue from this strategy, the monthly revenue from herring ﬁshing was modeled for 4 possible ﬁshery port locations in Scotland: Shetland (north), Aberdeenshire (east), Dumfries (south), and Hebrides (west), representing the four cardinal directions (Fig. 10, right).

Using the same parameters as described in Section 2.4, the projected monthly revenue for herring at each of those locations over time were graphed over time (Fig. 10, left). From our model, a ﬁshing company in Shetland maintains the maximum revenue for a small ﬁshing company of around $89,000/month for over 30 years before decreasing. Companies in Aberdeenshire will experience a more gradual decrease from maximum revenue, but the decrease begins after just a few years. Both Hebrides and Dumfries have much lower initial monthly revenues that quickly drop to 0 within 35 years.

shire (teal), Dumfries (light green), and Hebrides (blue) from 2006-2070.

The oscillations seen throughout the monthly revenue trend for each location can be attributed to the inherent random movement of ﬁsh throughout the ocean, causing the number of ﬁsh harvested to slightly vary. Over the time, the consistently substantial increase in monthly revenue will result in millions of additional proﬁt to those in the northern region. While the cost of relocation can reach over $400,000, as shown by our model, the relocation will allow the companies to ﬁsh for many more years without the need to upgrade vessels or other mechanical changes. Thus, we recommend relocating northward for all ﬁshing companies, particularly towards Shetland, if possible. This is not as critical for mackerel, since they do not migrate northwards quite as much as herring do.

4.2 Harvesting New Species: Haddock

Although herring and mackerel are two of the biggest sources of income for the ﬁshing industry of Scotland, it might be unfeasible for the small ﬁshing companies to change how they operate in terms of relocation or vessel quality, so turning to a diﬀerent species of ﬁsh could be beneﬁcial. Haddock (Melanogrammus aegleﬁnus) is a particularly suitable alternative, since it is the 3rd most harvested ﬁsh in Scotland (meaning that a niche in the market already exists) and has a density distribution that stretches south from the Iberian peninsula north to beyond Shetland (meaning that the ﬁsh’s northward migration will still keep them in harvestable range for all of Scotland).

The disappearance times for haddock for coastline companies is the longest and most consistent out of all 3 ﬁsh species (Fig. 11a). Although some locations, including the north tip of Scotland and Shetland, should still favor harvesting mackerel based on revenue (Fig. 8), haddock seem to be a uniformly eﬀective solution for the rest of Scotland, allowing for continued ﬁshing and proﬁt in the years to come.

The one drawback of this proposal is that haddock are demersal ﬁsh compared to mackerel and herring, which are pelagic. Although both types can be caught by trawling, bottom trawling is required for demersal ﬁsh, requiring new and diﬀerent nets.

4.3 Upgrading Fishing Vessels’ Assets

With only gutting and icing available to the ﬁsherman to keep the ﬁsh fresh, ﬁsh will only stay fresh for 5 days, limiting the duration of the ﬁshing trip and constraining current ﬁshery radius to 51 km [10]. However, with on-board refrigeration, the duration now extends to 15 days, allowing vessels to travel 3 times farther without having ﬁsh spoil [24]. Other changes to the vessel that could allow for longer distances to be traveled include motor upgrades which would let the vessels travel faster and thus cover more distance in the same amount of time.

To assess the eﬀects of adding on-board refrigeration, the agent-based model for herring ﬁshing was run for the 4 locations selected in subsection 4.1, comparing the total revenue using the gutting and icing radius and new, increased on-board refrigeration radius (Table 3).

Location Gutting and Icing On-board Refrigeration % Increase North (Shetland) $42,180,000 $60,288,000 42.9% East (Aberdeenshire) $23,134,000 $51,820,000 124.0% West (Hebrides) $2,657,000 $22,208,000 735.8% South (Dumfries) $494,000 $8,895,798 1700.8%

using diﬀerent ﬁsh storage methods.

The lower the initial revenue, the more that can be gained from switching to on-board refrig- eration. This is because high-ﬁsh-density locations like Shetland are already harvesting at their vessel capacity every day, making it useless to further increase ﬁshing radius. On the other hand, for a ﬁsh-sparse location like Dumfries, increasing radius allows each vessel to capture more ﬁsh, drastically increasing revenues. Thus, we recommend upgrading ﬁsh storage for companies who can currently harvest only a small portion of their daily capacity.

5 Territorial Water Limitations

Since only citizens of a nation are allowed to ﬁsh in the nation’s territorial waters, if ﬁsh were to move into the territorial waters of another country, Scottish ﬁshermen would simply be unable to ﬁsh there, or would have to obey the country’s laws and restrictions. The possible countries that our model predicted ﬁsh possibly moving northward into include Denmark (Faroe Islands) and Iceland. However, both of these locations are so far removed that the 22.2 km extensions from their coastlines do not conﬂict with our proposed ﬁshing port relocations in northern Scotland and the Shetland Islands, as elaborated on in Section 4.1. Thus, since Scotland is not bordered by another country on its northern border, there is not any issue with running into another country’s territorial water.

However, with the migration of the herring and mackerel populations into the exclusive eco- nomic zones (EEZ) of other countries, Scotland will have to give up a signiﬁcant amount of inﬂuence in the quota making. Initially, with the populations of the 2 species being mostly in the EEZs of the European Union and Norway, the European Union and Norway mostly decided the stock management of the species. But, with the species entering into the EEZs of Iceland and Greenland, these places will have a large say in the management of them [25]. Thus, the revenues that our model indicated could represent an overestimate due to the ﬁshing quotas that other countries may impose on Scotland.

6 Model Strengths and Weaknesses

6.1 Strengths

Our model is robust with all inputs based on real-world data from trusted websites and gov- ernmental agencies such as the National Oceanic and Atmospheric Administration and the Public Library of Science (PLOS). Moreover, our model was designed using information that is speciﬁc to the Scotland region, such as information from the Scottish government about the Scottish ﬁshery market for herrings and mackerels. With the large data set of information we accumulated, our agent-based model accounts for a large number of factors, ranging from the vessel capacity to the ﬁshery radius, that determine the quantity of ﬁsh a small ﬁshing company can obtain from its ﬁshing location.

Additionally, our agent-based model for ﬁsh movements allows for an accurate representation of the inherent randomness present within any system. The model is able to run a large sample size of random distributions of the initial location of the small ﬁshing companies’ ﬁshing ports and the harvestable number of ﬁsh for each population of ﬁsh, giving an accurate estimation of the quantity of ﬁsh the small ﬁshing company can collect.

Another advantage of our NetLogo simulation is that we can easily make predictions of ﬁsh density and distribution at whatever time in the future, be it 30 days or 30,000. This is particularly helpful for ﬁshing companies who want to make complex, multi-strategy plans that take into account the position of ﬁsh not only 50 years into the future, but also 10 years and 100 years into the future.

Finally, one of the most unique and powerful aspects of our model is our time-, latitude-, longitude- based equation which allows us to take into account how the temperature of the ocean water changes over time for a speciﬁc location in the ocean, deﬁned by latitude and longitude. This allows us to move past any over-generalized parameter describing the average increase in temperature for all of the global ocean, and makes our model vastly more accurate, Scotland- speciﬁc, and practically useful. Instead, our model accounts for the fact that at N20°, S20° the temperature may increase by 0.24°C over 10 years while only changing by 0.14°C at N20°, S30° over the same time period.

6.2 Weaknesses

One weakness lies in our assumption that the sole factor driving ﬁsh migration is the changing temperature of the ocean water. While the temperature of the water is a substantial factor, there are myriad other factors that determine the sustainability of migration (e.g., the relative abundance of predators and the availability of food). While the implementation of these factors along with our detailed temperature change analysis would allow for a more comprehensive model, it would also warrant a level of data complexity that would not be substantiated. However, the correlation between the temperature of the water and these factors allows them to be somewhat accounted for, mitigating this weakness. For instance, warmer water temperatures deplete vital nutrients [26], so the movement of the ﬁsh to its cooler ideal temperature range would also send it to a location of better food as well.

Additionally, there is an inconsistency in sources for related pieces of information due to speciﬁcity of information needed for diﬀerent inputs. For example, we pulled the information for the available of time for ﬁsh freshness from two diﬀerent websites for iced versus on-board refrigeration. This may have lead to a waterfall eﬀect with our need to compute some values, such as the ﬁshing area of a ﬁshing vessel, using values from diﬀerent sources. Luckily, this ﬂaw is lessened by the fact that we sought reputable and trusted sources for all of our data. Consequently, we can be ensured that all of our data, and our computed values, are a close approximation to a true value.

Finally, the model’s lack of seasonal data makes it impractical to use the model to predict the movement of the ﬁsh in a short period of time (< 1 year) or the speciﬁc location of the ﬁsh on a speciﬁc day. Due to seasonal weather, the ocean water’s temperature oscillates signiﬁcantly throughout the year, independent of the eﬀects of global warming. Due to our primary objective of modeling the long-term location of the ﬁsh 50 years from now, we did not take into account the oscillations of the ocean temperature throughout the year. However, our model still accurately predicts average ﬁsh locations and migration positions, since the ﬁsh’s natural seasonal migration behavior are designed to adapt to natural seasonal ocean temperature ﬂuctuations. In other words, the seasonal patterns of the ﬁsh and oceans that we did not explicitly account for in our model naturally account for each other in reality.

7 Conclusion

As consultants to a Scottish North Atlantic ﬁshery management consortium, our objective was to 1. Determine the location of the Atlantic herring and Atlantic mackerel in ﬁfty years, and 2. Assess the ﬁnancial impact of the migration on the livelihood of small ﬁshing companies and propose strategic improvements.

To accomplish our ﬁrst objective, we ﬁrst developed a stochastic agent-based model to simulate the migration trend of herring and mackerel caused by the ocean’s changing surface temperature. Based oﬀhistorical sea surface data, we ﬁrst began by predicting the ocean sea surface temperature. By our estimates, the temperature of the ocean surface on average will have risen 1.59°C by 2070 with speciﬁc geographic coordinates ranging from 8°C to 12°C.

Using our derived temperature gradient, we projected the location of herring and mackerel in ﬁfty years. According to our Netlogo model, herring are predicted to completely migrate away from Scotland and eventually reside east of Iceland whereas mackerel will be scattered throughout the north with a majority of them around Shetland Island.

Finally, for our second objective in determining the ﬁnancial impact, we ﬁrst considered the time the ﬁsh will stay in ﬁshing range. A majority of herring will leave the main Scotland with some still slightly surrounding Shetland Isles within the next ﬁfty years. On the other hand, a majority of the mackerel population will continue to populate the coast of Scotland after ﬁfty years. This is evident in the disappearance time with herring leaving by 2056 while mackerel staying until 2064.

To test the sensitivity of our model, we adjusted the temperature change gradient for the Scotland region. For herring, a more rapid temperature increase results in in much faster migration time with disappearance time decreasing by around ﬁve thousands days. On the contrary, mackerel follow the opposite trend with a higher rate of temperature change increasing the disappearance time because mackerel currently located in the southeast part of North sea will migrate north into ﬁshing range.

With the signiﬁcant loss in revenue expected in the coming decades, we propose the following three strategies: relocating northward to catch the migrating ﬁsh, upgrading vessels to continue harvesting the migrating ﬁsh without relocating, and begin harvesting haddock (a diﬀerent type of ﬁsh) as they stay within harvesting range for a longer period of time. Since some of the ﬁsh are projected to migrate into Iceland and Greenland waters and their economic exclusive zones, a decrease in Scotland’s quota share may have a potential trickle-down eﬀect on the number of ﬁsh that small ﬁshing companies are allowed to harvest.

In conclusion, we created a robust and ﬂexible agent based model to model the movement of ﬁsh, speciﬁcally herring and mackerel, based oﬀthe changing ocean water temperature. Varying With the calculated values of revenue for each species and the economic eﬀect of the migrating ﬁsh out of ﬁshing range. From our analysis, we proposed three strategic improvements (relocating, harvesting haddock, upgrading ﬁshing vessels) to the small ﬁshing company in order to recoup their loss revenue.

Appendices

A Linear Regression Coordinates

A sample section of the entire latitude-longitude coordinate system for the Scotland Region

퐴 퐵 Coordinate (50.0, -15.0) 3.676e-05 13.15971489 (50.0, -14.75) 3.761e-05 13.15950007 (50.0, -14.5) 3.894e-05 13.15289436 (50.0, -14.25) 4.025e-05 13.14484561 (50.0, -14.0) 4.162e-05 13.13263915 (50.0, -13.75) 4.298e-05 13.11939875 (50.0, -13.5) 4.348e-05 13.11254286 (50.0, -13.25) 4.292e-05 13.11537913 (50.0, -13.0) 4.313e-05 13.1124819 (50.0, -12.75) 4.351e-05 13.10884043 (50.0, -12.5) 4.369e-05 13.1074779 (50.0, -12.25) 4.383e-05 13.10756137 (50.0, -12.0) 4.381e-05 13.10853794 (50.0, -11.75) 4.324e-05 13.1071358 (50.0, -11.5) 4.235e-05 13.10082838 (50.0, -11.25) 4.098e-05 13.08550495 (50.0, -11.0) 3.998e-05 13.0487425 (50.0, -10.75) 3.987e-05 12.98266777 (50.0, -10.5) 3.97e-05 12.8936353 (50.0, -10.25) 3.95e-05 12.79626046 (50.0, -10.0) 3.976e-05 12.70757439 (50.0, -9.75) 4.028e-05 12.64584612 (50.0, -9.5) 4.04e-05 12.62079491 (50.0, -9.25) 4.051e-05 12.6212321 (50.0, -9.0) 4.168e-05 12.627375 (50.0, -8.75) 4.357e-05 12.62879648 (50.0, -8.5) 4.608e-05 12.61535937 (50.0, -8.25) 4.901e-05 12.59195985 (50.0, -8.0) 5.244e-05 12.56392924 (50.0, -7.75) 5.624e-05 12.53455851 (50.0, -7.5) 5.971e-05 12.50442058 (50.0, -7.25) 6.284e-05 12.46233606 (50.0, -7.0) 6.511e-05 12.40478053 (50.0, -6.75) 6.61e-05 12.3338548 (50.0, -6.5) 6.7e-05 12.25084511 Continued on next page Table A1 – Continued from previous page 퐴 퐵 Coordinate (50.0, -6.25) 6.873e-05 12.16335328 (50.0, -6.0) 7.098e-05 12.09457638 (50.0, -5.75) 7.357e-05 12.06103233 (50.0, -5.5) 7.679e-05 12.06628662 (50.0, -5.25) 7.965e-05 12.11064952 (50.0, -5.0) 8.188e-05 12.19596918 (50.0, -4.75) 8.237e-05 12.23036645 (50.0, -4.5) 8.185e-05 12.20427274 (50.0, -4.25) 8.14e-05 12.20873376 (50.0, -4.0) 8.079e-05 12.18631581 (50.0, -3.75) 8.05e-05 12.14703577 (50.0, -3.5) 8.148e-05 12.06571649 (50.0, -3.25) 8.128e-05 12.02539968 (50.0, -3.0) 8.071e-05 11.99106028 (50.0, -2.75) 8.037e-05 11.96336639 (50.0, -2.5) 8.114e-05 11.95162335 (50.0, -2.25) 8.405e-05 11.94635998 (50.0, -2.0) 8.828e-05 11.93561169 (50.0, -1.75) 9.136e-05 11.91920425 (50.0, -1.5) 9.312e-05 11.90556732 (50.0, -1.25) 9.301e-05 11.90412457 (50.0, -1.0) 9.19e-05 11.91148516 (50.0, -0.75) 9.146e-05 11.92515048 (50.0, -0.5) 9.256e-05 11.93250424 (50.0, -0.25) 9.498e-05 11.92357352 (50.0, 0.0) 9.81e-05 11.89288231 (50.0, 0.25) 9.997e-05 11.85247153 (50.0, 0.5) 0.0001011 11.81481233 (50.0, 0.75) 0.00010248 11.78113907 (50.0, 1.0) 0.00010378 11.74474518 (50.0, 1.25) 0.00010444 11.72201962 (50.0, 1.5) n/a (land) n/a (land) (50.0, 1.75) n/a (land) n/a (land) (50.0, 2.0) n/a (land) n/a (land) (50.0, 2.25) n/a (land) n/a (land) (50.0, 2.5) n/a (land) n/a (land) (50.0, 2.75) n/a (land) n/a (land) (50.0, 3.0) n/a (land) n/a (land) (50.0, 3.25) n/a (land) n/a (land) (50.0, 3.5) n/a (land) n/a (land) B Herring Accessible Time and Revenue

Coordinate Accessible Time(days) Revenue(in dollars) (58.0, -7.0) 22347.0 3712933.92 (58.0, -7.25) 21941.0 7254608.98 (58.25, -7.0) 22200.33 4749190.83 (58.5, -7.5) 22056.0 6795795.13 (58.5, -7.75) 20104.33 5088108.86 (58.5, -8.75) 16835.67 7390127.2 (58.75, -7.75) 22298.67 2685179.43 (58.75, -8.5) 18736.67 1522537.4 (58.75, -8.75) 15824.33 6842266.88 (59.0, -8.0) 22363.33 583704.32 (59.0, -8.5) 12344.67 260717.08 (59.0, -8.75) 19158.0 3895989.04 (59.25, -7.5) 19370.33 3106960.22 (59.25, -7.75) 19884.33 482219.94 (59.25, -8.0) 16490.67 82415.33 (59.25, -8.25) 11957.0 56335.78 (59.25, -8.5) 10379.67 10484.35 (59.25, -8.75) 18144.67 807048.21 (59.25, -9.0) 17237.0 5139921.89 (59.25, -9.5) 16551.33 7281295.49 (59.25, -9.75) 19340.0 6922458.98 (59.5, -7.25) 22613.0 1922006.46 (59.5, -7.5) 19408.33 189682.77 (59.5, -9.0) 15872.0 200137.16 (59.5, -9.25) 15850.0 763430.03 (59.5, -9.5) 16830.0 2105658.22 (59.75, -7.0) 21950.67 2671015.93 (59.75, -7.25) 19018.0 167741.46 (59.75, -9.0) 13451.33 80060.31 (60.0, -6.75) 23375.0 4653717.16 (60.0, -7.0) 20653.0 299065.69 (60.0, -9.0) 10488.0 59942.47 (60.0, -9.25) 12816.67 695448.08 (60.0, -10.0) 13424.33 5355061.5 (60.25, -6.75) 22977.0 3599473.79 (60.25, -9.25) 11139.33 196470.22 (60.25, -9.75) 12936.33 715559.94 (60.25, -10.0) 15556.33 361588.97 (60.25, -10.25) 14674.0 2335737.18 Continued on next page Table A2 – Continued from previous page Coordinate Accessible Time (days) Revenue ($) (60.5, -6.75) 22967.67 3730496.83 (60.5, -9.25) 7915.67 2957.61 (60.5, -9.5) 10863.0 33313.04 (60.5, -9.75) 8986.67 15690.73 (60.5, -10.25) 14157.67 895221.34 (60.75, -6.75) 22871.33 4412280.63 (60.75, -7.0) 19818.67 102249.74 (60.75, -7.25) 17417.67 230342.36 (60.75, -7.5) 17739.33 92788.1 (60.75, -7.75) 15508.33 6418.8 (60.75, -10.25) 12528.33 598411.92 (61.0, -6.75) 22690.0 5166474.97 (61.0, -7.0) 21745.67 945015.96 (61.0, -7.75) 16076.33 50484.36 (61.0, -10.0) 11221.0 47502.68 (61.0, -10.25) 11422.33 752494.76 (61.25, -6.75) 23345.0 5912314.45 (61.25, -7.5) 18429.0 1192219.61 (61.25, -7.75) 16760.67 38703.63 (61.25, -10.0) 8898.67 137985.99 (61.5, -6.75) 23060.67 9302526.05 (61.5, -7.5) 22493.0 2553334.18 (61.5, -8.75) 11659.33 3687.87 (61.5, -9.0) 13084.33 12598.6 (61.5, -9.25) 6847.0 2540.11 (61.5, -10.0) 9775.33 66163.66 (61.75, -6.5) 23375.0 18762775.59 (61.75, -6.25) 23336.0 23566666.67 (61.75, -7.5) 23011.67 3810289.28 (61.75, -8.75) 18493.33 132161.41 (61.75, -9.25) 18931.67 52850.58 (62.0, -7.5) 23022.0 4792431.29 (62.0, -8.5) 22414.33 729132.16 (62.0, -8.75) 22714.33 2718631.3 (62.0, -9.25) 21456.33 482236.51 (62.25, -7.5) 22739.0 4868187.3 (62.25, -8.25) 23229.33 1412203.1 (62.25, -8.5) 22790.67 13366666.67 (62.25, -9.25) 22876.0 3484583.09 (62.5, -7.5) 23137.67 5577775.2 Continued on next page Table A2 – Continued from previous page Coordinate Accessible Time (days) Revenue ($) (62.5, -8.0) 23207.33 3813130.65 (62.5, -8.25) 23318.0 25100000.0 (62.5, -9.25) 22907.33 13800000.0 (62.75, -7.5) 23307.33 24266666.67 (62.75, -7.75) 23323.33 28666666.67 (62.75, -8.0) 23375.0 36300000.0 (63.5, -4.75) 23368.0 43933333.33 (63.75, -4.75) 23349.67 40833333.33

C Mackerel Accessible Time and Revenue

Coordinate Accessible Time(days) Revenue(in dollars) (58.0, -7.0) 23375.0 189000000.0 (58.0, -7.25) 23375.0 184000000.0 (58.25, -7.0) 23375.0 173000000.0 (58.5, -7.5) 23375.0 169000000.0 (58.5, -7.75) 23375.0 160000000.0 (58.5, -8.75) 23375.0 129000000.0 (58.75, -7.75) 23375.0 113000000.0 (58.75, -8.5) 23375.0 86200000.0 (58.75, -8.75) 23375.0 110000000.0 (59.0, -8.0) 23375.0 47700000.0 (59.0, -8.5) 23375.0 55500000.0 (59.0, -8.75) 23375.0 76900000.0 (59.25, -7.5) 23340.0 70700000.0 (59.25, -7.75) 23375.0 70200000.0 (59.25, -8.0) 23375.0 57400000.0 (59.25, -8.25) 23375.0 52200000.0 (59.25, -8.5) 23375.0 47000000.0 (59.25, -8.75) 23375.0 54900000.0 (59.25, -9.0) 23375.0 37400000.0 (59.25, -9.5) 23352.0 27700000.0 (59.25, -9.75) 23298.0 36000000.0 (59.5, -7.25) 23353.0 19100000.0 (59.5, -7.5) 23362.0 13400000.0 (59.5, -9.0) 23374.0 11000000.0 (59.5, -9.25) 23375.0 49000000.0 (59.5, -9.5) 23375.0 35100000.0 (59.75, -7.0) 23374.0 26500000.0 (59.75, -7.25) 23334.0 9920715.4 (59.75, -9.0) 23370.0 4736962.58 (60.0, -6.75) 23367.0 6568236.18 (60.0, -7.0) 23370.0 8304897.84 (60.0, -9.0) 23352.0 8415562.03 (60.0, -9.25) 23300.0 15900000.0 (60.0, -10.0) 23375.0 25200000.0 (60.25, -6.75) 23375.0 15900000.0 (60.25, -9.25) 23374.0 36300000.0 (60.25, -9.75) 23374.0 22800000.0 (60.25, -10.0) 23375.0 22800000.0 (60.25, -10.25) 23375.0 21100000.0 Continued on next page Table A3 – Continued from previous page Coordinate Accessible Time (days) Revenue ($) (60.5, -6.75) 23373.0 26700000.0 (60.5, -9.25) 23375.0 14000000.0 (60.5, -9.5) 23329.0 5515526.77 (60.5, -9.75) 23297.0 9589003.31 (60.5, -10.25) 23306.0 9434618.1 (60.75, -6.75) 23359.0 253566.13 (60.75, -7.0) 23267.0 1812232.86 (60.75, -7.25) 23279.0 1623393.68 (60.75, -7.5) 23036.0 7869525.47 (60.75, -7.75) 23278.0 33606.43 (60.75, -10.25) 22057.0 7740859.1 (61.0, -6.75) 22773.0 8198622.34 (61.0, -7.0) 23355.0 1190304.74 (61.0, -7.75) 23341.0 14700000.0 (61.0, -10.0) 23370.0 1009895.23 (61.0, -10.25) 23375.0 12800000.0 (61.25, -6.75) 23375.0 25600000.0 (61.25, -7.5) 23375.0 21900000.0 (61.25, -7.75) 23373.0 40700000.0 (61.25, -10.0) 23375.0 27100000.0 (61.5, -6.75) 23375.0 53200000.0 (61.5, -7.5) 23375.0 54600000.0 (61.5, -8.75) 23375.0 74100000.0 (61.5, -9.0) 23373.0 47000000.0 (61.5, -9.25) 23369.0 23800000.0 (61.5, -10.0) 23375.0 13900000.0 (61.75, -6.5) 23373.0 32400000.0 (61.75, -6.25) 23354.0 10000000.0 (61.75, -7.5) 23329.0 1784349.21 (61.75, -8.75) 23375.0 9688079.59 (61.75, -9.25) 23356.0 297683.92 (62.0, -7.5) 23346.0 10200000.0 (62.0, -8.5) 23312.0 11500000.0 (62.0, -8.75) 23339.0 12400000.0 (62.0, -9.25) 23328.0 10700000.0 (62.25, -7.5) 23363.0 7679214.2 (62.25, -8.25) 23369.0 26300000.0 (62.25, -8.5) 23325.0 23600000.0 (62.25, -9.25) 23374.0 9937079.13 (62.5, -7.5) 23373.0 37800000.0 Continued on next page Table A3 – Continued from previous page Coordinate Accessible Time (days) Revenue ($) (62.5, -8.0) 23374.0 39500000.0 (62.5, -8.25) 23375.0 29700000.0 (62.5, -9.25) 23318.0 9237859.99 (62.75, -7.5) 23364.0 9317971.25 (62.75, -7.75) 23330.0 1068101.03 (62.75, -8.0) 22081.0 5110138.13 (63.5, -4.75) 22365.0 111814.12 (63.75, -4.75) 23257.0 4900492.16

D NetLogo Model Code

;; 1 tick = 1 day

globals [ fisheries fishery-x ; x-coordinate of fishery fishery-y ; y-coordinate of fishery fishery-radius ; radius that the fishery can catch fish vessel-capacity ; number of fish that a vessel can hold min-catch-proportion ; max-catch-proportion ; the number of fish taken by a vessel from a population is ran last-catch ; last tick at which fishery caught fish fish-pops ; number of populations of fish scotland ; DO NOT CHANGE price-per-fish ; e.g. 10 cents = 0.1 revenue ; amount of money made from selling fish max-temp ; DO NOT CHANGE death-time ; number of days that a population can survive in too-warm water before i start-offset ; number of days after Jan. 1st, 1982 that the temperature gradient shou trips ; number of fishing trips taken per day

init-herring ; DO NOT CHANGE init-mackerel ; DO NOT CHANGE rand-dist-prop ; proportion of fish populations that are distributed randomly amongs

coefs ; DO NOT CHANGE intercepts ; DO NOT CHANGE ]

turtles-own [ detect-radius ; radius that a fish population can search for better locations, measu opt-temp ; optimal temperature max-stay-temp ; maximum temperature at which a fish population is willing to stay wi max-tolerable-temp ; maximum temperature at which a fish population can exist withou death-counter ; counts up from 0 when max-tolerable-temp is exceeded, and kills the prev-patch ; DO NOT CHANGE escape-mode-counter ; number of days until random movement stops step ; distance moved per day ]

patches-own [ temp ; current temperature of the water in the patch fish-prop ; DO NOT CHANGE ] to initialize-variables set fisheries [[32 32] [32 31] [33 32] [34 30] [34 29] [34 25] [35 29] [35 26] [35 2 set fishery-x 34 set fishery-y 29 set fish-pops 4000 set fishery-radius 1.838 set vessel-capacity 1750 set min-catch-proportion 0.03 set max-catch-proportion 0.07 set scotland [[66 0] [67 0] [68 0] ... ; truncated for presentation set price-per-fish 0.5 set revenue 0 set max-temp 15 set death-time 7 set start-offset 25 * 365 set last-catch 0 set trips 10

set init-herring [[[24 26] [25 26] [26 26] ... ; truncated for presentation set init-mackerel [[[12 4] [13 4] [14 4] ... ; truncated for presentation set rand-dist-prop 0.3

set coefs [[3.6761664375989955e-05 3.760866491858817e-05 3.8943161380096653e-05 4.02 set intercepts [[13.1597148856797 13.159500071009676 13.152894363595287 13.144845609 end

to-report T [time lon lat] report (item lon item lat coefs) * time + (item lon item lat intercepts) end

to setup-world resize-world 0 80 0 64 ask patches [set pcolor white] ask patches at-points scotland [set pcolor black] ask patches with [pycor = 64] [set pcolor black] ask patches with [pxcor = 80] [set pcolor black] ask patches with [pcolor = black] [set temp 1e10] ask patch (item 0 item fishery fisheries) (item 1 item fishery fisheries) [set pcolo update-temp-gradient end to setup-fish set size 1 set color yellow set shape "fish" set detect-radius 1.5 set opt-temp 5.0 set max-stay-temp 12.0 set max-tolerable-temp 25.0 set death-counter 0 set fish-prop 0 set escape-mode-counter 0 set step 1 / 3 end

to setup clear-all reset-ticks initialize-variables setup-world let init-dist init-mackerel ; CHANGE FISH TO CHANGE INITIAL DISTRIBUTION let tot 0 foreach [0 1 2 3 4 5] [ i -> set tot tot + (length item i init-dist) * (i + 1) ] foreach [0 1 2 3 4 5] [ i -> foreach range (length item i init-dist) [ j -> ask patch (item 0 item j item i init-dist) (item 1 item j item i init-dist) [ sprout ((i + 1) / tot * (1 - rand-dist-prop) * fish-pops) [ setup-fish setxy (xcor - 0.5 + random-float 1) (ycor - 0.5 + random-float 1) ] ] ] ] crt fish-pops - count turtles [ setup-fish let test-xcor random-xcor let test-ycor random-ycor if [pcolor] of patch test-xcor test-ycor != black and [pcolor] of patch test-xcor setxy test-xcor test-ycor ] ] end

to go update-temp-gradient ask turtles [ set prev-patch patch-here if escape-mode-counter = 0 and [temp] of patch-here > max-stay-temp [ ; if not esc go-best-dir ] if escape-mode-counter > 0 [ ; if escaping, move towards a random neighbor face one-of neighbors with [ pcolor != black and pcolor != green ] forward step set escape-mode-counter escape-mode-counter - 1 ] if prev-patch = patch-here and ([temp] of patch-here > max-stay-temp or [temp] of set escape-mode-counter random 30 ] if [temp] of patch-here > max-tolerable-temp [ ; if too hot set death-counter death-counter + 1 ] if death-counter > death-time [ die ] ]

ask patch (item 0 item fishery fisheries) (item 1 item fishery fisheries) [ foreach range trips [ let trip-revenue 0 ask turtles in-radius fishery-radius [ set trip-revenue precision (trip-revenue + ((min-catch-proportion + random-flo ] set revenue revenue + (min list trip-revenue precision (vessel-capacity * price- ] if count turtles in-radius fishery-radius > 0 [ set last-catch ticks ] ] tick end

to go-best-dir let ot opt-temp let dr detect-radius let min-patch patch-here ask patch-here [ set min-patch min-one-of patches in-radius dr [abs(temp - ot)] ] face min-patch forward step end to update-temp-gradient ask patches with [pcolor != black and pcolor != green] [ set temp T (ticks + start-offset) pxcor pycor let normalized-value temp / max-temp let patch-value normalized-value * 255 if show-temps [ set plabel floor temp ] if show-temps = False [ set plabel "" ] set pcolor rgb patch-value 50 (255 - patch-value) ] end

to until-2070 while [ticks < 32141 - start-offset] [ go ] end

E Python Code

import wget import os import numpy as np from netCDF4 import Dataset import matplotlib.pyplot as plt import matplotlib from calendar import monthrange import pickle from sklearn.linear_model import LinearRegression

months = [’01’, ’02’, ’03’, ’04’, ’05’, ’06’, ’07’, ’08’, ’09’, ’10’, ’11’, ’12’]

for year in range(1982, 2020):

for month_idx, month in enumerate(months):

for date in range(1, monthrange(year, month_idx+1)[1]+1):

wget.download(’https://www.ncei.noaa.gov/data/sea-surface-temperature-optim str(year)+month, str(year)+month, (str(date) if date > 9 else ’0’+str(date))), ou

sst_scotland = np.empty((13879, 64, 80)) sst_scotland_best = np.empty((13879, 64, 80)) sst_scotland_worst = np.empty((13879, 64, 80)) day_idx = 0 for year in range(1982, 2020):

for month_idx, month in enumerate(months):

for date in range(1, monthrange(year, month_idx + 1)[1] + 1):

day_nc = Dataset(’./avhrr-only/{}/avhrr-only-v2.{}{}.nc’.format(str(year) day_nc_sst_scotland = np.roll(day_nc.variables[’sst’][0][0].data, 720, axi day_nc_sst_scotland_err = np.roll(day_nc.variables[’err’][0][0].data, 720, sst_scotland[day_idx] = day_nc_sst_scotland sst_scotland_best[day_idx] = np.subtract(day_nc_sst_scotland, 1.96*day_nc_ sst_scotland_worst[day_idx] = np.add(day_nc_sst_scotland, 1.96 * day_nc_ss day_idx += 1

with open("sst_scotland.txt", "wb") as file:

pickle.dump(sst_scotland, file)

with open("sst_scotland_best.txt", "wb") as file:

pickle.dump(sst_scotland_best, file)

with open("sst_scotland_worst.txt", "wb") as file:

pickle.dump(sst_scotland_worst, file)

with open("sst_scotland.txt", "rb") as file:

sst_scotland = pickle.load(file)

T_regs = np.empty((64, 80, 2)) T_regs.fill(np.nan) for lat in range(64):

for lon in range(80):

if sst_scotland[0,lat,lon] != -999:

x = np.array(list(range(13879))).reshape((-1,1)) y = sst_scotland[:,lat,lon] model = LinearRegression().fit(x, y) T_regs[lat][lon] = np.array([model.coef_[0], model.intercept_])

def forecast(day, lat, lon):

return T_regs[lat][lon][0] * day + T_regs[lat][lon][1]

plt.plot(np.linspace(1982, 2020, 13879), sst_scotland[:,lat,lon], label="SST data") plt.plot(np.linspace(1982, 2070, 31879), forecast(np.array(list(range(13879+18000))),l plt.legend() plt.title("SST at 50$^\circ$, -15$^\circ$ (1982-2070)") plt.ylabel("SST ($^\circ$C)") plt.xlabel("Year")

plt.plot(np.subtract(np.array(forecast(np.array(list(range(13879))), lat,lon)), np.arr coef_map = matplotlib.cm.plasma coef_map.set_bad(’black’) plt.imshow(T_regs[:,:,0], cmap=coef_map, origin=’lower’, extent=[-15,5,50,66]) plt.colorbar() plt.title("SST Regression Coefficients $\it{A}$ ($^\circ$C / day)") plt.xlabel("Longitude ($^\circ$)") plt.ylabel("Latitude ($^\circ$)")

int_map = matplotlib.cm.viridis int_map.set_bad(’black’) plt.imshow(T_regs[:,:,1], cmap=int_map, origin=’lower’, extent=[-15,5,50,66]) plt.colorbar() plt.title("SST Regression Intercepts $\it{B}$ ($^\circ$C)") plt.xlabel("Longitude ($^\circ$)") plt.ylabel("Latitude ($^\circ$)")

A = [[pair[0] for pair in lat] for lat in T_regs] B = [[pair[1] for pair in lat] for lat in T_regs]
