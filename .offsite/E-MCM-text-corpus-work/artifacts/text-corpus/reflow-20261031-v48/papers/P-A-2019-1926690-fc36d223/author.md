Abstract

A truly terrifying future may await inhabitants of the earth: the release of three full-grown dragons into the world. In this analysis, we examine the ecological impacts of dragon introduction, in particular for the purposes of informing ﬁctional literature and advancing real-world population assessments.

First, we present a global agent-based model which we designed to understand the global distribution of dragons and their environmental impact, as well as to evaluate the potential result of human intervention strategies. Three dragons are initialized in the object-oriented model and given individual-level characteristics that contribute to their decision-making and the ecological havoc they eventually wreak.

Next, we develop a regional diﬀerential equation model that zooms in on a single dragon and investigates the dynamics of this dragon’s growth and its impact on and the population of prey species and the vegetation cover in its range. Examining a wide range of parameter sets, we ﬁnd that our dragons are voracious eaters that will likely prove to be a nuisance for human populations. In response, we posit that a likely outcome of the dragon introduction event is management of the creatures by housing them in zoos, and we calculate the food resources necessary to support dragons held in captivity. Given that the caloric requirements of our modeled dragons require them to consume thousands of deer each year, we recommend that the dragons be held to a strict diet to limit their growth, in which case the dragons still require hundreds of deer at their physiological minima.

Our models indicate that releasing dragons into the wild could have disastrous ecological impacts, including the elimination of forests, melting of sea ice, and decimation of many prey populations. However, since dragons may provide beneﬁts, such as regulation of nuisance populations and provenance of resources to humans, careful management could turn the ecology of the situation around. Because of the volatile nature of this problem, we devised multiple complementary models to best capture the problem and its potential solution. This approach is of value to population managers dealing with similar environmental concerns with real-world nuisance species and human-caused habitat destruction.

Letter to George R.R. Martin

Team 1926690

Dragon Den Modeling Agency

George R.R. Martin

Super Secret Medieval Lair

Santa Fe, NM

Dear Mr. Martin:

Our team has conducted an analysis regarding the likely outcome if the three ﬁctional dragons from Game of Thrones were to be released into the world, encompassing their prey requirements, land use strategy, and reproductive success. We based our modeled dragons on your story A Song of Ice and Fire, with some notable modiﬁcations to accommodate the likely needs and preferences of ﬁctitious dragons released into the real world. We wish to present some recommendations for how you might incorporate this ﬁctional element of your book meeting the real world into your next story.

To begin, we devised an agent-based model which randomly placed the three dragons, with semi-randomly assigned characteristics, somewhere on the map, which we represented as a series of 45 connected regions. While we did not initially place limitations on the areas in which the dragons could live, it quickly became apparent that these dragons would gravitate toward semi-arid temperature or tropical regions, given an assumed preference of these cold-blooded creatures for warmer climates and ample land availability for nesting. Although we did not encode the volcanic activity of any particular region, we did assign the 45 map locations a number of caverns in which the dragons could nest. Given the requirement of mature dragons in our model to locate gold nuggets to create a permanent den, which we derived from detailed dragon analysis, natural resource availability quickly emerged as an important constraint on dragon growth and population expansion.

Through our agent-based model, we found that the habitat range of dragons tended to be relatively limited and that dragon populations, if left unchecked, tend to completely rob a region of its natural resources. For this reason, if you choose to write a story on the real-world implications of dragon escape, it is likely that you will either need to imagine a post-apocalyptic world, or will need to design a mechanism through which humans can manage the dragon population. In our model, we included the potential intervention strategy of people removing a maximum of one dragon from each region each day in response to habitat destruction imposed by the dragons. People were also able to restore some of the removed forest habitat in our model. We found that the most likely regions for dragon dominance were tropical or sub-tropical regions of the globe where there is a lot of land (thus many available caverns), including the Americas (in particular, the continental United States and northern South America) and some parts of Asia and Africa.

We ﬁnd that dragons are unlikely to be able to live for long periods of time in the arctic regions due to their requirement for prey species. Dragons are, however, likely to ﬁnd a home in wetter, more temperate climates as opposed to more arid regions. Dragons that prefer to live in the arctic would probably need to travel long distances to accommodate their appetites, especially given potential forthcoming population declines in the arctic.

In response to the constraints we found on global resource availability, we explored both the baseline ecological impacts of these dragons and the potential interactions humans might have with the newest member of the animal kingdom. To gain a better understanding of the impact a single dragon might have on a region, we designed a diﬀerential equation model to simulate the lifespan of a dragon and its impact on prey species (assumed to be deer) and local vegetation. We found that, in order to grow to full size, a dragon must be able to meet its nutritional needs, meaning that there must be an ample supply of deer available and the dragon must be somewhat good at hunting. Speciﬁcally, there must be a sizeable herd of deer initially available, and these deer must multiply at at least a rate of 15% per year in order for the dragon to have enough food to eventually reach at least 83% of its target weight. We computed the caloric demands of a dragon using a power law and found that a fully grown 6,000 kg dragon (the mass of an elephant) needs to consume at minimum 2,647 deer per year to sustain its metabolism. As a high estimate for deer population density would be 45 per square mile, a dragon would need at least 58 square miles of land to have enough deer for a year, and then it wouldn’t have any left for the next year. Although we are supportive of the ﬂourishing of dragons, unfortunately, in most scenarios we explored, these ruinous reptiles decimated the deer and evicted the vegetation in the areas they inhabited.

Since the energy requirements for a dragon are so great and ecological impacts so dire, we ﬁnd it probable that these dragons would not be allowed to run amok in the wild, but would rather be kept in captivity. This could be an interesting plot element in your story that is a realistic outcome, but it requires that you set your story in modern times. We propose that dragons, either before or after initially wreaking havoc on global ecosystems, could be kept in zoos. We conducted a detailed analysis of the resources that must be furnished to a captive dragon, and have found that a dragon kept in captivity restricted to only 250 kg in eventual size would require 158 deer per year to sustain, or 2,627 deer to approximate what the dragon would likely eat in the wild. This would warrant a tremendous investment in the care of each animal, which would be possible for only the world’s largest and most capable zoos, and would also present an animal rights quandary if the dragons were only provided with the bare minimum. The spectacle of an in-house dragon would be a signiﬁcant attractor for visitors to said zoo, likely visiting from locations around the globe. This high concentration of people would be perfect for a plot twist involving some dramatic action terrorizing the crowd.

We also posit that dragons could become part of human culture by serving as a food source, in addition to their ecological role in managing extremely large prey populations. This would be a particularly interesting plot element in a story set in medieval times. We ﬁnd through our modeling that dragon populations have the potential to grow substantially in number and would likely require management, in particular through hunting. Humans could also use dragons for transportation, increasing the likelihood that they would overlook their role in habitat destruction, thus improving the probability that the dragons could peacefully cohabit with people.

After completing this ecological assessment of the potential woes of global dragon infestation, we are conﬁdent that, although the situation may mean environmental calamity, it is rich with content for your potential use as a writer. We welcome additional inquiries about the ecological dimensions of a dragon release event.

Most sincerely,

Team 1926690 of the Dragon Den Modeling Agency

1. Introduction Dragons have long captivated the human psyche. From the ancient Near East and Mesopotamia to the High Middle Ages of western culture to the present, dragons repeatedly appear as large, reptilian creatures in folklore and mythology [1]. Modern audiences may imagine dragons as sinister hoarders of gold and jewels, as depicted in Tolkien’s The Hobbit [2], magniﬁcent and perhaps misunderstood in J.K. Rowling’s Harry Potter series [3], and even alluring suitors of donkeys in Dreamworks’ Shrek franchise [4]. While conceptions of dragons have varied with geography and time, the typical dragon in western culture today is a large, winged, ﬁre-breathing reptile of enormous strength and often capricious temperament, with build ranging from serpentine to Tyrannosaurus rex-esque.

In the modern hit television series Game of Thrones, based on George R. R. Martin’s fantasy series A Song of Ice and Fire, three dragons are raised by Daeneryus Targaryen, the “Mother of Dragons.” While the setting of Game of Thrones is ﬁctional, its dragons raise the question of whether it could be sustainable to raise dragons on the earth. Dragons from the series tend to favor volcanic mountains as habitats, but as the series has begun to suggest, it is also possible these creatures might thrive in human-dominated habitats.

2. Problem Statement In this report, we analyze the feasibility of three dragons, based loosely on those in Game of Thrones, living on the earth. We analyze dragon characteristics, behavior, habits, diet, and environment and assess the dragons’ ecological impact and requirements, energy intake and expenditures, and land management requirements. We examine these questions in biomes with nine possible distinct temperature and dryness regimes, and we analyze both the impact of dragon migration between biomes and the inﬂuence of single-dragon introduction in a particular habitat range. For modeling purposes, we assume that the dragons are large reptiles that can ﬂy long distances, breathe ﬁre, and resist attack by any other species. The only assumptions we consistently maintain about the dragon’s growth and development is that dragons are born weighing 10 kg and grow to 30-40 kg within a year.

3. Data Sources and Modeling Approach To better inform our models, we assimilated some physiological data for comparable organisms from the scientiﬁc literature. We also set strict guidelines for dragon growth, reproduction, and feeding which we conserved across our diﬀerent modeling approaches. We thus cohesively investigate dragon life history, which could be important to understand dragon ecology.

We ﬁrst implemented a macroscale, agent-based model for dragon expansion across the globe, incorporating constraints on permanent settlement formation (“den” location), energetic requirements, habitat destruction by dragons, migration, and reproduction. We then implemented a microscale diﬀerential equation model of the growth and development of one dragon in a ﬁxed region and its ecological impacts.

Upon reviewing the results of the agent-based and regional diﬀerential equation models and realizing that allowing dragons to roam freely in the wild would be highly detrimental to the environment, we implemented a diﬀerential equation model for dragons in captivity to gain better insight into the support they would require.

4. Modeling Methodology

4.1. Unique Model Characteristics For the purposes of the agent-based model, we split the globe up into regions of a size which we deemed reasonable for daily dragon movement. Thus, the maximum distance a dragon can travel per day is the space of an “ecoregion” cell in model space. Each region was assigned traits which would help or hinder dragon development and reproduction as well as impact its environment.

Gold Nugget Nesting and Reproduction In a nod to Smaug from Tolkien’s The Hobbit [2], we decided that a unique feature of our dragons would be that they require gold in order to make their nests. To facilitate this, we mandated that each dragon would need to mine for gold resources according to known gold reserves in the territories it inhabits. Once a dragon garners enough gold to produce a suitable den, it settles down and is able to reproduce either sexually or asexually. Asexual reproduction comes at a greater energetic cost, thus is only chosen as a strategy when the dragon is suﬃciently healthy and no mates are available. For the purposes of simpliﬁcation, we assume that all interactions between adult (age ≥1 year) dragons can result in sexual reproduction, and do not make a distinction between male and female dragons.

representing a wet climate, orange a semi-arid climate, and yellow an arid climate. Credit for underlying map: Wikimedia Commons.

This decision to give dragons multiple reproductive strategies follows from biological phenomena observed in similar reptiles. In the Komodo dragon, reproduction may occur via either asexual reproduction through parthenogenesis (virgin birth) or sexual reproduction [5]. We assign a more substantial health cost to asexual reproduction in our model, but do not enforce that dragons substantially alter their behavior (i.e. migrate) in order to ﬁnd mates, particularly since we assume that a dragon must settle in a den before it is able to reproduce.

In the regional diﬀerential equation model, neither reproduction nor gold-mining behaviors are captured, as the primary focus of that model is to understand the ecological impacts and demands of an isolated dragon.

Dragon Prey We were not speciﬁc about the type of dragon prey in our global agent-based model; when we initialize prey species, we give them random caloric contents. In the regional diﬀerential equation model, we assume that the dragon, being at the top of the food chain, may eat a variety of prey animals; however, we refer to all prey animals as “deer” for succinctness and as a nod to the fact that we base the caloric content of the prey animals oﬀthat of a deer [6], one of the most widespread large land animals in the world.

4.2. Agent-based Modeling

Motivation To model worldwide population dynamics of dragons after initial release of three “mature” dragons into random global ecoregions, we opted for an agent-based model (ABM). These models are often used for population studies requiring the analysis of multiple individual-level characteristics [7], which may be stochastic in nature. We used our ABM, implemented as an object-oriented model in Python, to understand the extent of potential dragon population spread, both in terms of geography and sheer numbers. The results of this investigation inform our later modeling and data analysis approaches for the purposes of stress-testing diﬀerent environments under dragon pressure, and understand whether intervention measures are necessary.

Mapping To facilitate movement of dragons across diﬀerent areas of the globe, we divided the world into 45 distinct ecoregions, each of which we assume is sized such that our dragons could move from one to the other within the course of a day. We assigned several characteristics to each region, representing factors that would impact healthy growth and reproduction for each of the dragons.

Earth and Region Initialization In the agent-based model, ﬁrst an “Earth” object is created, into which each of the forty-ﬁve regions are placed. The three dragons are then randomly placed on the map, with the possibility that more than one dragon may initially be in the same region. These dragons are set to all be a year old or less, and weigh between 30 and 100 kg.

We give each ecoregion a dryness rating between 0 and 2 based on the dryness classiﬁcation shown in the map in Figure 1. In addition, we assign a decimal fraction to each ecoregion to signify the approximate percentage of land coverage, as we assume that dragons need to hunt and nest over/on land. Because one of the factors we are interested in is ice depletion due to ﬁre-breathing, we also assigned a decimal fraction to each ecoregion to indicate ice coverage.

When we initialize each ecoregion, we give it a label corresponding to hemisphere it is in and its climate type. We then assign a range of factors to each region such that the climate and geography of the region is captured, described in Table 1.

Factor Assignment Procedure Rationale & Details Temperature t tropics = 15, temperate = 5, arctic = 0 Roughly corresponds to average temperatures in ◦C. Number of Dens d (den density)×(total land area) Dens can occur on land, includ- ing ice-covered land, with equal probability. Den density is set to 50.

total land area −ice area   Number of Gold (random nugget density)× Accounts for fact that ice- 2 Nuggets n covered land is less likely to con- tain accessible gold. Maximum nugget density is set to 500.

(total land area - ice area) Forest Level f Does not allow forests to grow on 1 + dryness factor ice and causes drier areas to have fewer forests. Number of prey Randomly selected between 5 and 100 Animal habitation patterns vary. items p

To each of the p prey items initialized in a region, we randomly assign a “calorie content”, between 0 and 10. At each timestep, the calorie content of these prey items is incremented by 1. When the calorie content of a prey item surpasses 10, it is removed from the simulation. On each day of the simulation, we log the number of prey items consumed and calculate a “suitability index” for each region.

The suitability index takes into account the number of dens available, gold nuggets available, number of forests, and the temperature in the region in order to assign a score representing the suitability of that region to dragons. This index s is calculated as a weighted sum

D + f N + p d F + t T + n P s = , 5

Where D, F, T, N, and P are the maximum possible number of dens, forest level, temperature, number of nuggets, and number of prey items, respectively, that can occur in an ecoregion.

Dragon Initialization When we initialize the three original dragons in the model we assign each an age between 1 and 4 years old and a weight between 30 and 100 kg. We also give the dragon a health of 100 and a fullness of 5. If dragons drop to 0 or lower in health, they are removed from the simulation, and dropping below a fullness of 5 warrants health deductions. Dragons produced via reproduction are born and introduced into the model at 0 years old weighing 10 kg.

Daily Timestep: Globe On each day, we simulate dragon dynamics in all ecoregoins. After we complete the daily timestep function for each of the individual regions, we call a daily statistics function which logs the ecological characteristics of each ecoregion for evaluation.

Daily Timestep: Ecoregion On each day for each ecoregion, we deﬁne or maintain the seasonal classiﬁ- cation based on its local season. We determine the daily temperature for each ecoregion using a calculation that incorporates substantial temperature variation, yet is realistic based on climate:

T(t) = U(4S −4(4 −C), 4S) + U(C, 4.25) · S · C,

where S is the season (between 0 and 1.5 for winter, between 2.5 and 4 for summer, and between 0.5 and 3.5 for fall and spring), and C is the climate (0 for arctic, 1 for temperature, 2 for tropical). 4(S −4 + C) represents the fact that, in summer when S = 4, S −4 + C will never be below zero, and it will remain warmer in the tropics in summer and winter. We choose from the second random distribution because we never want the temperature to exceed 50oC, in keeping with recent air temperature records. Maximum temperature is attained in the summer in the tropics. Figure 2 is an example of the simulated temperatures in ecoregion number 20.

Daily Timestep: Dragon The daily timestep function is called for each dragon in each ecoregion of the globe. The age of each dragon is updated by one day, and then the dragon moves through a number of phases:

I. Gold Nugget Mining As a ﬁrst order of business the dragon mines gold nuggets, for which it requires a minimum health of 20. We calculate the “nugget richness” in the ecoregion as the ratio between the number of nuggets currently in our region and the maximum number of nuggets possible in a region, n N .

We sample a base number of nuggets to mine from a uniform distribution of size 20 centered around our current health level, and multiply this number by the “nugget richness” to moderate our expectations of success. This calculation becomes the number of nuggets the dragon receives, unless it exceeds the number of nuggets available, in which case the dragon gets all remaining nuggets. Health decreases by 5 after nugget mining is complete.

II. Den Searching After gold mining, the dragon may search for a den if it is currently homeless and has at least 50 nuggets. A searching dragon has a 50% probability of ﬁnding a den on each timestep (day). Once a region has no more available dens, a new dragon will need to migrate if it wants to settle permanently.

III. Hunting Next, the dragon needs to hunt for food to improve its fullness levels.

The amount of food required by the dragon is based on a power law equation for its metabolic functioning, scaled to accommodate the integer rating system we chose to represent the caloric content of diﬀerent prey items.

Based on the work of Nagy, Girard, and Brown scaled to appropriate units and forced to take integer values, the predation equation is

aw(t)b   p(t) = , 365 · 5000

where a and b are known parameters, p(t) is in prey calorie units per day, and ⌈·⌉indicates the ceiling function. For each prey item eaten, the “number of forests” is decreased by one to account for deforestation due to trampling and ﬁre-breathing associated with hunting. In addition, if ice is present in the region, ice coverage is reduced by 0.1% for each hunting activity performed. The fullness of the dragon increases by the caloric rating of the prey item consumed, and fullness decreases by 5 at the end of each day.

IV. Migration The next decision the dragon makes is whether to migrate. If the suitability index in its present region is less than 0.1 or if it has been unable to ﬁnd a den and is eligible for one, it will migrate.

Dragons can travel diagonally, horizontally, or vertically to regions adjacent to the one they’re currently in. Depending on the simulation, we either enforced that the dragon migrate to the adjacent cell with Activity Health Cost Health Requirement Environmental Cost Asexual Reproduction 25 40 N/A Sexual Reproduction 10 25 Forests - 15, Ice - 0.05 % Hunting for Food 2 per prey 0 Forests - 10, Ice - 0.1% per prey Mine for Gold Nuggets 5 20 Nugget Reduction

Health requirements are the minimum health levels required for the dragon to perform each activity.

V. Reproduction We assume that reproduction can occur on any given day with 25% probability. Though this may result in frequent mating and reproductive events, we note that many reptile species have large clutch sizes [8]. Because our dragons only produce one oﬀspring per birth, we increase reproduction frequency to better match the fecundity of real reptiles.

If a dragon’s health surpasses 25, it occupies a den, and its age is ≥1 year, it may mate sexually if it can ﬁnd a suitable mate. Sexual reproduction can occur with any other fully mature dragon in the same ecoregion, and results in a health deduction of 10 due to the physical demands of reproduction, and also results in forest and ice loss due to courtship rituals involving ﬁre-breathing.

If sexual reproduction does not occur, and if the dragon has health ≥40, a den, and age ≥1 year, it can reproduce asexually, which results in a health deduction of 25.

Each day, a dragon’s health is incremented by 15 points to reward survival, and is incremented by an additional 10 points if the its fullness surpasses 25. If fullness is between 10 and 25, the dragon gains 0.25 kg per day, and if it is greater than 25, the dragon gains 0.50 kg per day. If a dragon has less than 10 fullness, it loses 0.25 kg if it is at least a year old and weighs at least 30 kg. If it has less than 10 fullness and is less than a year old, it still gains 0.25 kg. If fullness goes below 5, the dragon loses 10 health per day.

4.3. Regional Diﬀerential Equation Modeling

To understand on a ﬁner scale the eﬀects of a dragon on an individual region, we designed a diﬀerential equation model capturing the growth of the dragon and its environmental impact. We assume that the 40 ecosystem is stable before introduction of the dragon and that the dragon, being a very large, potentially very destructive reptile, is the biggest inﬂuencer of 30 Temperature (Celsius) the ecosystem once it is introduced. We assume that the dragon is a carnivore at the top of the food chain, 20 and since native predators are relatively scarce, we assume that the dragon is the only predator in the system once introduced. 10

Equations Governing the Dragon To under- 0 stand the dragon, we focused on its mass in kg, w(t), where t is in years. We assume that the growth of the dragon follows a logistic growth curve (see Fig- 0 50 100 150 200 250 300 350 Julian Day ure 3), as in [9], modulated by food availability,

 food available   dw 1 −w(t) food needed −1 dt = r(t)w(t) ,

wmax climate in the Southern Hemisphere. where t is in years and wmax is the highest weight the dragon can attain. We deﬁne r(t) to represent the dragon’s growth rate, which we assume depends solely on the extent to which the dragon is able to feed. We model r(t) as an optimal growth rate, ropt, scaled by the dragon’s level of access to food, that is

f(t) r(t) = ropt m(t),

where f(t) is the amount of food the dragon is able to eat in a year, and m(t) is the dragon’s yearly caloric requirement. It is known in biology that an organism’s metabolic requirements can be well-approximated using a power law with weight, so we assume that the dragon’s metabolism m(t) has the form

m(t) = aw(t)b,

where m(t) is in units of calories per year and a and b are parameters. Nagy, Girard, and Brown [10] found these parameters to be a = 139065 and b = 0.889 for reptiles with metabolism in calories/year and weight in kg.

The amount which the dragon is able to feed, f(t), will depend on how eﬀective it is at hunting and on the availability of prey species. We Standard Logistic Curve model dragon feeding by interactions between the dragons and prey 1.0 species (discussed below) 0.8 f(t) = ke(t)p(t) w(t) , 0.6 wmax logistic(t) 0.4 where p(t) is the prey population level, e(t) is the dragon’s hunting eﬀectiveness, and k converts from prey animals to calories. We include 0.2 w(t) the factor wmax in order to increase the dragon’s feeding rate as it grows in size. We deﬁne e(t) piecewise as linearly increasing until the 0.0 −6 −4 −2 0 2 4 6 dragon reaches maturity, and then constant thereafter t

( e0 + emax−e0

tmature t t < tmature e(t) = , 1 ﬁned f(t) = 1+e−t , satisfying the t ≥tmature emax diﬀerential equation f ′(t) = f(t)(1 −f(t)) where tmature is the age at which the dragon reaches maturity. Sub- stituting the expressions above into our expression for r(t), we have

ke(t)w(t) ke(t)p(t)w(t) = kropt e(t)p(t)w(t)1−b. r(t) = ropt wmaxm(t) = ropt aw(t)bwmax awmax

Therefore, returning to dw dt , we have

  food available  dw dt = kropt 1 −w(t) e(t)p(t)w(t)2−b food needed −1 . awmax wmax

Using the conversion factor k between prey species and calories, the amount of calories available to the dragon at time t is kp(t). Using the power law for metabolism, the amount of food needed by the dragon at time t is aw(t)b, so substituting we obtain   kp(t)   dw dt = kropt 1 −w(t) e(t)p(t)w(t)2−b aw(t)b −1 . awmax wmax

Writing c = k a, the diﬀerential equation has the form

    dw dt = cropt 1 −w(t) c p(t) e(t)p(t)w(t)2−b w(t)b −1 (1) . wmax wmax Equations Governing the Environment In addition to the growth of the dragon, we are interested in the dragon’s impact on the environment. We assume that dragons are carnivores at the top of the food chain and eat deer, and that other predators are insigniﬁcant in light of a massive, murderous, meat-eating monster from Middle Earth [2]. We model the availability of prey species, p(t) with a simple predator-prey model dt = jp(t) −e(t)p(t) w(t) dp (2) , wmax

where j represents the natural population growth rate of the prey species and e(t) deﬁnes dragon’s hunting eﬀectiveness (discussed previously). Since we are modeling interactions between deer and just one dragon, rather than a group of dragons, we scale the interactions by the dragon’s weight, such that more massive dragons eat more deer.

Dragons may cause environmental damage by trampling vegetation and breathing ﬁre as they hunt, and we assume that they are the main source of environmental degradation in our system. Letting v(t) denote the proportion of the dragon’s environment that is covered in vegetation, we model vegetation growth and damage by dt = ℓv(t) −g w(t)v(t) dv (3) , wmax

where g is a parameter representing the frequency of dragon-damage, and ℓrepresents the natural growth rate of the vegetation.

Parameter Identiﬁcation The following is a table of each parameter in our model, its interpretation, and initial values chosen based on outside literature or desired model characteristics.

Parameter Interpretation calories per deer c = k/a calories needed by dragon per (kg of mass)b

Optimal dragon growth rate ropt

Maximum dragon weight wmax

Exponent in metabolic power law re- b lationship Population growth rate of prey j species Vegetation growth rate ℓ Dragon destructiveness g

Dragon’s initial hunting eﬀective- e0 ness Dragon’s hunting eﬀectiveness at emax maturity

Dragon age of maturity tmature

Dragon weight at birth w0 Initial prey species population p0

Initial proportion of ground covered v0 by vegetation Initial Value Rationale 119040 Based oﬀtotal calories available in a 139065 = 0.856 deer [6] and reptile growth rate [10] 0.035 Chosen such that weight is 30-40 kg at one year of age, as per problem statement 6000 kg Dragon is roughly as heavy as an ele- phant 0.889 Nagy, Girard, and Brown [10]

0.25 Chosen to be high

0.09 Situationally dependent 0.2 Dragon is 20% destructive largely due to ﬁre-breathing 0.1 Chosen so that baby dragons are bad hunters 0.5 Dragon’s can’t be that good at hunt- ing; they are very large predators seeking relatively small prey 21 A dragon is only an adult once it can legally drink. 10 kg Problem statement 5,000 Corresponds to 45 deer/square mile over 111 square miles 0.5 Represents an urban/suburban area

5. Model Results

5.1. Agent-Based Model

Without Resource Controls When we ran the agent-based model without resource controls on the dragons (i.e., the dragons are not aﬀected by the decimation of the environment, but prey are), we obtained the following heatmaps for dragon populations, suitability index, and forests:

1 1 0.75 3 3 5 5 25 7 7 9 9 0.60 11 11 13 13 20 15 15 17 17 0.45 19 19 21 21 15 Region Region 23 23 25 25 0.30 27 27 29 29 10 31 31 33 33 0.15 35 35 37 37 5 39 39 41 41 0.00 43 43 45 45 0 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 Day Day

2000 1 0 3 2 5 4 200 7 6 9 8 1600 11 10 13 12 160 15 14 17 16 1200 19 18 21 20 Region Region 120 23 22 25 24 27 26 800 29 28 80 31 30 33 32 35 34 400 37 36 40 39 38 41 40 43 42 45 44 0 0 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 Day Day

right) in the agent-based model in the absence of dragon-speciﬁc population controls.

As can be seen, not many dragons remain by the end of the simulation and the environment becomes severely depleted. However, if we mandate that dragons stop expending health on nugget mining after ﬁnding a den, this shifts fairly dramatically to much higher dragon populations (see Appendix A) .

Forest Removal In the above example, we used the Resource Controls on Prey Proliferation:

ensured that prey levels do not go down below zero in several of the ecoregions, because the suitability index is partially determined by the climate. However, if we also multiply the prey produced in each interval by the forest fraction f/F, we can simulate the loss of forest’s eﬀect on prey species. When we do this, we do not see a rebound in dragons subsequent to initial declines due to low suitability indices. Instead, the dragon populations quickly decline, but the forests do not suﬀer as dramatically.

15.0 1 1 3 3 0.8 5 5 7 7 12.5 9 9 11 11 13 13 0.6 15 15 10.0 17 17 19 19 21 21 Region Region 23 7.5 23 0.4 25 25 27 27 29 29 5.0 31 31 33 33 0.2 35 35 37 37 2.5 39 39 41 41 0.0 43 43 45 45 0.0 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 Day Day

2000 1 0 3 2 5 4 7 6 160 9 8 1600 10 11 13 12 15 14 17 16 120 1200 19 18 21 20 Region Region 23 22 25 24 80 27 26 800 29 28 31 30 33 32 35 34 40 400 37 36 39 38 41 40 43 42 45 44 0 0 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 Day Day

right) when forest cover inﬂuences prey populations.

Conservation Intervention Simulation It became clear following our initial analysis that, given our parameterization of the dragon as creature with dual reproductive modality, large size, and destructive territorial behavior, dragons released into the wild cause complete destruction of the ecosystems best for them (warm climates with forests containing ample prey species). In response to this issue, we implemented some conservation measures in our ABM.

First, we simply restored the tree levels by the amount of losses whenever losses in trees surpassed a deﬁned to oﬀset natural resource losses. It turned out that, in this secondary scenario, the threshold value for forest loss at which humans intervened played a major role in governing the ﬁnal number of dragons present in the population, but only up to a certain point (restoration after about 10% of losses in the maximum scenario). This is because dragon removal too early in the simulation would be prohibitive of successful dragon reproduction and proliferation. Tree replenishment is a somewhat unrealistic idea due to challenges associated with habitat restoration eﬀorts, but this version of our ABM does capture the potential impact of human hunting on the expansion of dragon populations.

Threshold Loss for Intervention Final Dragon Population after 100 Days 50 2 100 0 200 39 400 42 1000 40

after habitat destruction occurs.

See Appendix A for insight on the inﬂuence the dragons had on ice and gold nugget availability.

5.2. Regional Diﬀerential Equation Model We performed a regional diﬀerential equation simulation using our initial parameter set to understand the dynamics of such an ecosystem and gain information on energy requirements. Additionally, we performed a range of parameter studies in order to understand how a dragon responds to diﬀerent environmental conditions and growth rates. All simulations were performed using forward Euler’s Method with a time step of one month, unless otherwise noted.

Initial Results Below are graphs displaying the weight of the dragon, the prey population level, the vegetation level, and the dragon’s metabolism over a ﬁfty year period (Figure 6).

Weight of One Dragon Over Time Deer Population Over Time 6000 25000

5000 20000 Dragon Weight (kg) 4000 Deer Population 15000 3000

10000 2000

5000 1000

0 0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years) Vegetation Cover Over Time Dragon Metabolism Over Time 1e8 0.8 Proportion of Land Covered by Vegetation 3.0 0.7 Dragon Metabolism (kcal/year) 2.5 0.6

0.5 2.0

0.4 1.5 0.3 1.0 0.2 0.5 0.1

0.0 0.0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years)

As can be seen, the dragon begins approaching its target weight of 6000 kg within 10 years, coming very close to attaining it with a weight of 5998 kg after 50 years. Due to the dragon’s high growth and consumption levels, the deer population, which during the dragon’s infancy actually spikes from 5,000 to almost 25,000, is decimated within 30 years, and after 50 years is at a mere 3 deer. The area’s vegetation levels fare similarly poorly due to the dragon’s ﬁery disposition. Responsible for this devastation is the dragon’s voracious appetite, which scales with its size. As an infant, the dragon’s metabolism is 1,077,005 calories, or 9 deer, per year. By the time the dragon reaches 12 years of age, it requires 315,165,197 calories - or 2,647 deer - per year. The dragon continues to require deer at this alarming level for the rest of its life, causing utter population destruction.

Parameter Studies In addition to running our model under the initial parameter set, we performed a range of studies to assess the impact of varying each parameter on the dragon’s development and on environmental factors.

I. Caloric ratio c = k/a

Dragon Growth for Varying c Deer Population for Varying c 0.05 6000 0.15 0.25 200000 0.35 5000 0.45 0.55 0.65 Dragon Weight (kg) 4000 Deer Population 0.75 150000 0.85 0.95 0.05 1.05 3000 0.15 1.15 0.25 100000 0.35 0.45 2000 0.55 0.65 50000 0.75 1000 0.85 0.95 1.05 1.15 0 0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years) Vegetation Cover for Varying c 0.05 0.15 1.75 0.25 0.35 0.45 1.50 0.55 0.65 Vegetation Level 1.25 0.75 0.85 0.95 1.00 1.05 1.15 0.75

0.50

0.25

0.00 0 10 20 30 40 50 Time (years)

Varying the parameter c = k/a, representing the ratio of the number of calories available in a single deer and number of calories required by a dragon per (kg of body mass)b (in the equation), had marked eﬀects on dragon growth outlook and deer population. For low values of c, the dragon had a hard time reaching its target weight and grew more slowly, indicating that dragons would struggle to fare well in the absence of high-calorie food sources. The deer, on the other hand, experience higher population spikes when they provide less sustenance to the dragons, but do eventually die out in all scenarios. Vegetation levels follow patterns analogous to deer population.

II. Initial deer population p0

Dragon Growth for Varying Initial Deer Populations Deer Population for Varying Initial Population 250 6000 25000 750 1250 1750 5000 2250 20000 2750 3250 Dragon Weight (kg) 4000 Deer Population 3750 4250 15000 4750 1000 3000 250 750 1250 10000 1750 2000 2250 2750 3250 5000 1000 3750 4250 4750 1000 0 0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years) Vegetation Cover for Varying Initial Deer Population 2.00 250 750 1250 1.75 1750 2250 1.50 2750 3250 Vegetation Level 3750 1.25 4250 4750 1000 1.00

0.75

0.50

0.25

0.00 0 10 20 30 40 50 Time (years)

Similarly, with metabolism exponent b and caloric ratio c, we see that the dragons suﬀer with low initial deer populations (less than roughly 2,250) and have a hard time reaching their target weight. Adding deer to the initial herd beyond 2,250 does not signiﬁcantly impact the dragon’s ﬁnal weight, but allows them to reach it faster. Conversely, for the deer, it does not appear that there is safety in numbers, because even though deer herds with higher initial populations spike to the highest peak populations, this spike occurs the earliest for them, and they begin to rapidly decline. Herds with lower initial populations last longer before experiencing this decline, and have higher populations during the decline phase as compared to herds with higher initial populations at the same point in time. Vegetation is also more successful with lower initial deer populations, with vegetation cover having the highest peak and declining the latest for lowest levels of deer population.

III. Dragon destructiveness g

Vegetation Cover for Varying Dragon Destructiveness 0.001 0.005 40 0.01 0.05 0.1 0.15 30 0.2 Vegetation Level 0.25 0.3 0.35 0.4 20 0.45 0.5

10

0 0 10 20 30 40 50 Time (years)

vegetation population, between g = 0.05 and g = 0.01.

Although the dragon destruction parameter g does not aﬀect the dragon’s growth or the deer population, we notice an interesting bifurcation in vegetation stability when we vary g between 0.001 and 0.5. For values of g at or below 0.05, the vegetation does not get decimated as we observed previously, but exhibits almost nonsensical exponential growth. For values of g at or above 0.1, we see the vegetation decay falls to almost nonexistent levels, as before. This phenomenon suggests that dragons that are only moderately destructive can peacefully coexist with the environment without torching it all to charcoal.

IV. Maximum hunting eﬀectiveness emax

Deer Population for Varying Dragon Maximum Hunting Effectiveness 0.2 400000 0.3 0.4 350000 0.5 0.6 0.7 300000 0.8 Deer Population 0.9 250000

200000

150000

100000

50000

0 0 10 20 30 40 50 Time (years)

While changes in emax don’t have drastic eﬀects on the dragon’s growth (other than slight drops in ﬁnal weight) or vegetation cover, we do observe an interesting eﬀect on the deer population. For emax values at or above 0.3, the deer population eventually dies out, albeit at slower rates for lower values, but for emax = 0.2 the deer population increases exponentially, even though the dragon doesn’t seem to be too adversely aﬀected. This result is hopeful, as it demonstrates that the deer herd can endure if a dragon is bad at hunting and that the dragon isn’t too adversely aﬀected by its poor hunting skills.

V. Deer population growth rate j

Dragon Growth for Varying Prey Population Growth Rates Dragon Growth for Varying Prey Population Growth Rates 6000 6000

5000 5000

Dragon Weight (kg) Dragon Weight (kg) 4000 4000

3000 3000

2000 2000

1000 1000

0.001 0.01 0.15 0.35 0.05 0.09 0.13 0.17 0.21 0.005 0.05 0.25 0.45 0.07 0.11 0.15 0.19 0.23 0 0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years)

Deer Population for Varying Growth Rates Vegetation Cover for Varying Prey Population Growth Rates 0.001 0.001 0.005 0.005 7 0.01 0.01 200000 0.05 0.05 6 0.15 0.15 0.25 0.25 0.35 0.35 5 Vegetation Level 150000 Deer Population 0.45 0.45

4 100000 3

2 50000 1

0 0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years)

j ∈[0.001, 0.45], and vegetation cover for for j ∈[0.001, 0.45]

The deer population growth rate j has a substantial eﬀect on the dragon’s growth, with low values of j causing the dragon to grow to less than 1/3 of its target weight. For values of j less than 0.05, the dragon grows to less than half of its its weight, and j must be at least 0.15 for the dragon to even reach 5,000 kg (83% of its target weight). As would be expected, the deer die oﬀquickly with low population growth rates, and due to the devouring dragon, the only value of j we tested that produced a non-negligible deer population at the end of 50 years was j = 0.45, which is quite high. These results indicate that if the deer population growth cannot keep up with the dragon’s growth, the dragon will suﬀer and the deer will perhaps suﬀer more. Additionally, we observe an interesting bifurcation in vegetation behavior around j = 0.05. For j ≤0.05, the vegetation ﬂourishes, because the deer aren’t multiplying enough to feed the dragon, so it doesn’t become as destructive as it would normally.

VI. Dragon maximum weight wmax

Dragon Growth for Varying Maximum Weights Deer Population for Varying Maximum Dragon Weights 500 500 1000 1000 6000 25000 1500 1500 2000 2000 2500 2500 5000 3000 3000 20000 3500 3500 Dragon Weight (kg) Deer Population 4000 4000 4000 4500 4500 5000 5000 15000 5500 5500 6000 6000 3000 6500 6500 10000 2000

5000 1000

0 0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years)

Vegetation Cover for Varying Maximum Dragon Weights 0.8 500 1000 1500 0.7 2000 2500 0.6 3000 3500 Vegetation Level 4000 0.5 4500 5000 5500 0.4 6000 6500 0.3

0.2

0.1

0.0 0 10 20 30 40 50 Time (years)

While changing wmax produces very predictable changes in the dragon’s growth, of note is the fact that of all values of wmax we tested, even the smallest of dragons (with the lowest of metabolisms) still exterminates the deer population and destroys the vegetation.

5.3. Dragons Kept in Zoos Because, based on the preliminary results we obtained from our global agent- based and regional diﬀerential equation models, it seemed like dragon-related damage to human societies and the environment is inevitable, we decided to explore an alternative fate for the dragons based on our base diﬀerential equation model. In this scenario, after dragons proliferated naturally or were bred in captivity, intervention would keep the dragons alive (and away from fragile ecosystems).

As can be noted in our base diﬀerential equation model, supporting a single dragon up to 6000 kg in body size could require a deer population of thousands. Given that the average whitetail deer may have a home range of 2 miles [11] or 907 acres [12], it is unreasonable to suggest that a zoo might be able to support a deer herd of this size if deer were supplied naturally. Much like management of zoo populations for naturally occurring animals, it would be necessary to consider to what extent we might alter the natural feeding patterns and living conditions of the dragons to suit life in captivity [13]. Even if animals are allowed to hunt naturally in distances, would be happy in a small enclosure. Additionally, zoos spend up to millions of dollars each year on feeding programs [14]. As a result, if a dragon were to be housed in a zoo, care would have to be taken to manage the dragon’s diet such that it did not grow past a certain size and could be managed in captivity.

Using the components of our regional diﬀerential equation model, we modeled the amount of deer which would be needed each year to sustain the dragon at diﬀerent maximum weights. We summarize the maximum number of deer needed over the lifespan of the dragon for diﬀerent initial weights, and the number of calories per year this corresponds to, in the table below. We also present a sample curve for number of deer/calories consumed per year over the ﬁrst 15 years of the dragon’s life. These estimates are within range for animals of similar size, for example the African elephant’s estimated 25,550,000 yearly caloric budget [15].

Maximum Minimum Minimum Yearly Maximum Maximum Yearly Weight (kg) Yearly Deer Calories Yearly Deer Calories 1.9 × 107 3.1 × 108 250 158 2627 3.5 × 107 3.3 × 108 500 293 2793 6.5 × 107 3.8 × 108 1000 543 3200 1.2 × 108 4.8 × 108 2000 1005 4074 1.7 × 108 5.9 × 108 3000 1441 4954 3.2 × 108 8.9 × 108 6000 2666 7507

a 15-year period. Minima are based on metabolic rates and maxima are based on observed feeding in the wild, which is modulated by prey availability.

Deer Eaten/Year, max size: 250 kg 1e8 Calories Eaten/Year, max size: 250 kg 3.0 2500

2.5 2000 Calories Eaten Deer Eaten 2.0 1500 1.5 1000 1.0 500 0.5 2.5 5.0 7.5 10.0 12.5 15.0 2.5 5.0 7.5 10.0 12.5 15.0 Year Year

at 250 kg.

6. Model Analysis

6.1. Agent-Based Model

Model Strengths and Insights The ABM allowed us to evaluate global scenarios of dragon population expansion without being overly speciﬁc about the ecological niche that the dragons will adopt.

– Our model shows that the most likely scenario is that dragons will congregate in the most suitable habitat for them.

– Despite this grouping, dragons are likely to wreak havoc on the environment no matter how long they occupy a region due to their rapid migration and destructive habits.

– Human intervention can have a considerable inﬂuence on the size and eﬀects of the dragon population.

Using the ABM, we can evaluate human-dragon interaction at the macroscale, which is particularly important given our speculation that dragon may become a valuable game species.

– The ABM allows us to consider a general prey species, and requires that we set the regeneration rate of prey to be fairly high to accommodate the dragons. This may be an overly optimistic environment for the dragons, but the ABM allows us to easily tune changes in prey availability in accordance with improved understanding of dragon physiological demands (as well as new knowledge about the extent to which the creatures hunt for recreation).

Climate Factors It quickly became clear that, while habitat suitability plays a major role in the population distributions observed, this is highly dependent on whether we assume that dragons form permanent nests. In our initial agent-based model runs, we observed that while the suitability of the regions quickly decreased, the regions with the highest suitability scores still supported the highest dragon populations later due to legacy nesting. This eﬀect decreases if (1) you decrease the number of available nests or (2) you reduce or eliminate the need of the dragons to form permanent nests.

Model Limitations While our agent-based model allowed us to understand long-term global dragon dy- namics in relation to climate and geography and incorporate stochasticity, there were some major limitations of the approach. These limitations, which inspired our adoption of the diﬀerential equation modeling ap- proach to ﬁll in the gaps, included:

– Our model was unable to appreciate the changing habitat requirements of growing dragons. Because of the way we designed the model, no matter how big the dragons got, we could not consider the possibility of necessary permanent range expansion beyond the span of a single cell.

– The assumption that dragons live in caverns made it impractical to consider expanding a dragon’s home base. Because dragons are limited to the cavern in which they reside, they may be isolated geographically from other caverns, and hence other dragons.

– The assumption that each cavern is a uniform, unspeciﬁed size did not allow for the possibility of dragons outgrowing their homes. In response to this, in one version of the simulation, we limited dragon growth after it reached a certain size until it obtained additional gold nuggets. This approach enabled us to see how the dragons might be physiologically limited by their physical environment outside of food issues.

– A pressing concern that is left out of the model is encroachment of dragon populations on human populations. We did not take into account either physical/territorial altercations between dragons or their potential interactions with humans that fall outside the realm of resource consumption. While we did explore the result of human intervention for conservation purposes, we did not consider the social pressure associated with a growing dragon population. It is possible that safety concerns could lead to human support of dragon population control. We address this scenario via the zoo management scenario in our third presented model.

6.2. Regional Diﬀerential Equation Model

Model Strengths and Insights Using diﬀerential equations to model the impacts and demands of one dragon in a speciﬁc region allowed us to not only observe dragon growth and environmental damage under a speciﬁc set of parameter values that we selected as reasonably aligned with existing knowledge, but also enabled us to understand the dragon’s and environment’s response to variations in these parameters. Some conclusions of note are:

– The caloric demands of a dragon are very high and scale with its weight, which in all simulations increased very rapidly. We encountered very few scenarios in which the prey herd size and growth rate were suﬃcient to sustain the dragon without an eventual extinction.

– A dragon’s ﬁnal weight is very sensitive to the growth rate of its prey population, requiring an annual prey growth rate of at least 15% to even reach 83% of its target weight. The deer in this case, however, do not beneﬁt from the suﬀering of the dragon, and are all eventually eaten even when the dragon’s growth is severely stunted.

– Prey growth rates (and herd sizes, which also aﬀected the dragon’s growth) can be viewed as corre- sponding to environmental conditions of varying harshness, and as such dragons may do poorly in cold or arid environments where prey is scarcer or is replenished at a slower rate.

– The deer were devoured and the vegetation vanquished by the dragon in almost all of our parameter studies, suggesting that the likelihood of an “actual” dragon being extremely destructive if released into the wild is very high. Although there were a few instances in which the deer and/or vegetation were able to endure, these were rare, and couldn’t be counted on to occur under more stochastic, real-world settings. As such, we do not recommend letting dragons run amok unchecked in the wild, and propose some strategies for controlling them in our conclusion.

Model Limitations While we were able to perform substantial analysis on our model in its present form, there were areas which we wish our model could have addressed more precisely and improvements that could be made:

– The regional diﬀerential equation model is not impacted by the size of the region the dragon inhabits, as it only accounts for the size of the deer herd present and vegetation coverage rate. Interactions between dragons and deer would likely increase with higher deer density, but we were unable to capture this in our model.

– While the dragon majorly impacts the region’s vegetation levels, the dragon and the prey experience no adverse eﬀects from environmental degradation. While the dragon is certainly the main driver of deer destruction, this simpliﬁcation may not be realistic because destruction of habitat would lead to a decrease in available prey, which would in turn cause less food to be available to the dragon.

– Due to time constraints, we only varied one parameter at a time in our parameter studies, while it may have provided additional insight to vary two or more at a time.

– We solved for the equilibria of the system and did not ﬁnd them physically meaningful, aside from the trivial solutions.

7. Real World Applications and Approach Validity Although our analysis concerns a ﬁctitious

dragon species, the approach that we used could be of use to population managers in the real world. Our dragons are large reptiles that require a signiﬁcant amount of resources and are highly mobile, and these characteristics match, to some extent, other known animal species. The parameters of our model could also be modiﬁed to correspond to animals much diﬀerent from dragons, and while the globe is an atypically large scale for an agent-based model, a global ABM could be appropriate for some species, whale sharks, for example [16]. Additionally, because we model climate ourselves, the model could easily be adapted to model the response of predator-prey dynamics to climate change.

The predatory nature of the dragons can be seen as a double-edged sword: on one hand, it poses serious threats to prey species populations, but on the other could aid in the elimination of nuisance species. For deer, the prey animal we based our analysis on, much focus has been placed on managing their numbers for the purposes of reducing tick transmission and automobile accidents [17–19], and the suggestion has often been that people should take to hunting them. Our approach could be used to model a real predator serving as moderator of deer populations for human beneﬁt, or to model deer populations under scenarios of human management, rather than dragon consumption. Modeling a territorial animal could be useful for understanding species that tend to nest for life and do not have the need to reproduce sexually, namely to track their global distributions and enable conservation strategies [20]. In the face of climate change, agent-based modeling techniques can reveal diﬀerential clustering of species based on their reproductive rate under particular conditions and with certain habitat preferences [21].

8. Conclusions Using both a global agent-based model and a regional diﬀerential equation model to

simulate potential dragon dynamics, we have found that the consequences of releasing dragons into the wild are indubitably dire. With our ABM we ﬁnd that the most likely outcome of dragon release is settlement in, and subsequent devastation of, a particular ecoregion due to the dragon’s need to form a permanent home in a cavern. It is common in the model output to see dragons congregating in the regions to which they are best suited (tropical to semi-arid climates), especially as a single established dragon can reproduce asexually and populate that region. For this reason, we ﬁnd it unlikely that dragons will need an excessive home range, particularly if political pressures limit dragon occupation. When dragons are allowed to multiply unchecked, this environmental devastation inevitably spreads to most of the globe. In response to this outcome, we simulated population control and environmental restoration by humans in later iterations of our ABM, and found these measures to be somewhat eﬀective at curbing dragon-caused calamity. However, we note that small changes to the model, such as timing the onset of human intervention, has relatively drastic implications for dragon population size and the ecological impact of the dragons, in particular resource consumption and ice melt.

With our diﬀerential equation model, we were able to simulate dragon and environmental responsiveness to changes in parameters controlling dynamics of the system. In particular, we found that such a single predator- multiple prey system is sensitive to changes its parameters, and particularly sensitive to the growth rate of the prey species, which dramatically impacted the dragon’s ﬁnal weight. While we were able to simulate regional dragon dynamics over a wide range of possible parameter values, almost all of these simulations led us to the conclusion that, because the caloric demands of a dragon are so high, the peaceful coexistence of a dragon and an existing ecosystem is almost impossible. Dragons have monstrous appetites which are diﬃcult to sate and cause catastrophic ecological damage even independent of their tendency to rampage their environment while hunting and reproducing and the destructive nature of their ﬁre breath.

Because our approach captures both the spatial elements of dragon proliferation via the agent-based model and the ﬁne-scale ecological interactions of each dragon via the diﬀerential equation modeling, we are able to make balanced recommendations for management, including human hunting activities and zoo-based management. In almost all scenarios explored for both the global agent-based model and the regional diﬀerential equation model, the dragons caused massive environmental devastation, including the melting of sea ice in addition to deforestation and extinction of prey species. In light of these dismal results, we adamantly advise against the release of dragons into the wild unchecked. Alternative strategies for hosting a dragon population on earth could include captivity in zoos, which would require enormous resources including hundreds to thousands of deer per year (and potential animal rights concerns), or a well-managed dragon hunting season (see Appendix C for tasty dragon recipes). For the purposes of George R.R. Martin’s imagination, however, the possibilities are endless (and, quite possibly, satisfying, even where irresponsible).

9. Appendix A: Additional Agent-Based Model Data Ice cover loss from dragon ﬁre breathing

exercises was a process we hoped to explore in modeling. We found a full range of results when playing with the parameters, from complete ice loss over Antarctica to very moderate ice loss in most of the sectors (and no ice loss in those completely covered by ice). This was principally because the ice loss was directly controlled by whether dragon population growth was successful in the middle latitudes. Otherwise, the creatures never spread in suﬃcient numbers to the ice-covered regions.

0 0 2 2 4 4 0.60 0.60 6 6 8 8 10 10 12 12 14 14 0.45 0.45 16 16 18 18 20 20 Region Region 22 22 24 24 0.30 0.30 26 26 28 28 30 30 32 32 34 34 0.15 0.15 36 36 38 38 40 40 42 42 44 44 0.00 0.00 0 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96 100 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 Day Day

(left), and dragons are able to ﬂourish (right).

When we placed the constraint that dragons would stop looking for gold once their dens were produced, we found that the dragons had a lot more of their health available for reproduction. While this may be more realistic, we wanted to keep dragon populations in check and thus left this constraint out of the model for a short-term run of the model. Antarctic sea ice is completely decimated by the dragons in this simulation.

0 0 0.75 2 2 50 4 4 6 6 8 8 0.60 10 10 40 12 12 14 14 16 16 0.45 18 18 30 20 20 Region Region 22 22 24 24 0.30 26 26 28 28 20 30 30 32 32 0.15 34 34 36 36 10 38 38 40 40 0.00 42 42 44 44 0 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 Day Day

2000 0 0 2 2 4 4 200 6 6 8 8 1600 10 10 12 12 160 14 14 16 16 1200 18 18 20 20 Region Region 120 22 22 24 24 26 26 800 28 28 80 30 30 32 32 34 34 400 36 36 40 38 38 40 40 42 42 44 44 0 0 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 Day Day

0 0 2 2 4 4 400 0.60 6 6 8 8 10 10 12 12 320 14 14 0.45 16 16 18 18 20 20 Region Region 240 22 22 24 24 0.30 26 26 28 28 160 30 30 32 32 34 34 0.15 36 36 80 38 38 40 40 42 42 44 44 0.00 0 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 0 17 34 51 68 85 102 119 136 153 170 187 204 221 238 255 272 289 306 323 340 357 374 391 408 425 442 459 476 493 Day Day

right), ice (bottom left) and gold nugget reserves (bottom right) when dragons stop seeking gold nuggets after their den is found.

10. Appendix B: Additional Diﬀerential Equation Model Parameter Studies

I. Metabolism power-law exponent b

Dragon Growth for Varying b Deer Population for Varying b 60000 0.55 6000 0.6 0.65 0.7 50000 5000 0.75 0.8 0.85 Dragon Weight (kg) 40000 4000 Deer Population 0.9 0.95 1.0 1.05 30000 3000 0.55 0.6 0.65 0.7 20000 2000 0.75 0.8 0.85 10000 1000 0.9 0.95 1.0 1.05 0 0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years)

Vegetation Cover for Varying b 0.55 1.0 0.6 0.65 0.7 0.75 0.8 0.8 0.85 Vegetation Level 0.9 0.95 0.6 1.0 1.05

0.4

0.2

0.0 0 10 20 30 40 50 Time (years)

Here we varied the exponent in the power law relationship between dragon size and metabolism, m(t) = aw(t)b, between 0.55 and 1.05. With all else being equal, dragons with lower metabolic ex- ponents took longer to reach their ﬁnal weights, and these weights were lower than those with higher metabolic exponents. For exponents above 0.65 the dragons eventually reached wmax = 6000 kg, but for lower values of b the dragon’s growth was stunted, suggesting that dragons with lower metabolisms either need access to more food or would beneﬁt from higher growth rates (ropt) to attain their full size.

As would be expected, the deer fared best with dragons with lower metabolisms (fewer of them were getting eaten and thus their population could grow more), but even with the lowest of metabolic ex- ponents all of the deer populations were eventually decimated. Similarly, vegetation lasted the longest with less voracious dragons, but even in the best case scenario was eventually mostly destroyed.

II. Dragon optimal growth rate ropt Dragon Growth for Varying Growth Rates Deer Population for Varying Dragon Growth Rates 100000 0.001 6000 0.005 0.01 0.05 80000 5000 0.1 0.15 0.2 Dragon Weight (kg) 4000 Deer Population 0.25 60000 0.3 0.35 0.001 0.4 3000 0.005 0.45 0.01 40000 0.05 0.1 2000 0.15 0.2 20000 0.25 1000 0.3 0.35 0.4 0.45 0 0 0 10 20 30 40 50 0 10 20 30 40 50 Time (years) Time (years)

Vegetation Cover for Varying Dragon Growth Rates 0.001 0.005 1.2 0.01 0.05 0.1 0.15 1.0 0.2 Vegetation Level 0.25 0.3 0.8 0.35 0.4 0.45 0.6

0.4

0.2

0.0 0 10 20 30 40 50 Time (years)

The value of ropt, the optimal dragon growth rate, has (as its name would imply) a pronounced eﬀect on how fast the dragon grows, and on the ﬁnal weight it reaches. For lower values of ropt, the dragon takes longer to reach its ﬁnal weight, and on the extreme lower end (ropt = 0.001 and ropt = 0.005) we observe a noticeable drop in its ﬁnal weight. As one might expect, the deer experience the highest peak populations latest in time when the dragons grow more slowly, but even for the lowest growth rates the deer are still devoured by the end of 50 years. Vegetation also tends to fare better for more slowly growing dragons, but is inevitably unviable.

Continuation

11. Appendix C: Recipes for Cooking Dragon

15 m   Level 3  5 m, Dragon Egg Omelette  2 Portions Health 500 calories  Anonymous concerned citizen

Use this recipe to concoct a delectable omelette from the aesthetically pleasing eggs of the common dragon. Do your part to prevent overpopulation!

Preparation Ingredients

Crack dragon egg into bowl containing cream; whip thoroughly 1 1 Dragon egg 4g Parsley Add remaining ingredients to the bowl and mix as much as 2 1/3 cup Cream possible 1 teaspoon Salt 1 tablespoon Butter Pour mixture onto a cast iron pan; make sure it’s whimsical & 3 To taste Pepper looks like something out of the Middle Ages

Say a prayer 4 Add some alcohol and light on ﬁre - ﬂambé! 5

Hint

Try diﬀerent mixtures of spices for truly unique taste!

30 m   350 °F  90 m, Dragon Meat 6-Step Lasagna  6-8 Portions Health 600 calories  Emmy & Max

Chow down on luscious dragon meat lasagna to make good use of your dragon hunting bounty.

Preparation Ingredients

Cook minced dragon meat from a freshly slain dragon in a large 1 1 box Lasagna noodles saucepan with black pepper and butter until completely brown 3 Eggs 100 ml Cream Meanwhile, boil noodles until tender; allow to sit until cool 2 100 ml Milk enough to touch comfortably with hands 400 g Mozzarella 4 sprigs Basil As soon as you can, melt 5 tbsp butter with ﬂour and slowly 3 1 tbsp Black pepper add cream and milk once melted. Once it starts getting thick, 10 tbsp Butter add about a cup and a half of red sauce and the nutmeg. This is 1 cup Ricotta cheese your bechamel sauce. Mix the ricotta with the eggs; add pepper.

1 jar Red sauce In layers, starting with bechamel, alternate between the follow- 4 1 tsp Nutmeg ing layers in a large deep baking pan: bechamel, pasta, red 1 cup Flour sauce, dragon meat, mozzarella, ricotta, bechamel, pasta 2 lbs Fresh dragon meat

Coat the top of the pie with a generous amount of cheese and 5 bechamel; top with basil and some more black pepper

Cook for an hour and a half at 350°F. Remove, cool, and enjoy! 6

Avoid Getting Sick:

Make sure you cook dragon meat completely before incorporating to avoid food poisoning!

Dragon Venom Bulletproof Coﬀee [SUPERFOOD] 7 m  One serving Health ???

 Scarbucks

Take your morning joe up a notch with an infusion of freshly-harvested dragon venom, widely lauded for its salutary properties.

Preparation Ingredients

With a nutcracker, crack open the dragon fang. While wearing 1 1 Dragon Fang gloves, extract the venom sac, being careful not to touch it 1 serving Coﬀee or Espresso with bare skin. Puncture the venom sac with a knife and drain into 2 Tbsp Butter a glass.

Brew a cup of coﬀee or espresso using your favorite method (we 2 personally recommend the Aeropress for its versatility and ease of use).

Working quickly, drop the butter and 2 tsp of the venom into the coﬀee and agitate with a whisk for 3 one minute. If the whisk dissolves by the end of this process, you did not stir fast enough and should discard the coﬀee to avoid possible poisoning.

Enjoy this rich, curative cup of coﬀee. Side eﬀects may include: increased energy, development of protective scales, ﬁre-breathing, asexual reproduction, and sudden, rapacious deer cravings.
