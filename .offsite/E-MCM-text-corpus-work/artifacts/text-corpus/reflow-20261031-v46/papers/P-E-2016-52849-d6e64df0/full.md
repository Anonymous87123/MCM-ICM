# P-E-2016-52849-d6e64df0

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only 52849 T1 ________________ F1 ________________ T2 ________________ F2 ________________ Problem Chosen T3 ________________ F3 ________________

<!-- b000003 | front_matter | pages [1] -->
E

<!-- b000004 | front_matter | pages [1] -->
T4 ________________ F4 ________________

<!-- b000005 | front_matter | pages [1] -->
2016

<!-- b000006 | prose | pages [1] -->
MCM/ICM

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.)

<!-- b000009 | prose | pages [1] -->
Type a summary of your results on this page.

<!-- b000010 | prose | pages [1] -->
Do not include the name of your school, advisor, or team members on this page.

<!-- b000011 | prose | pages [1] -->
To address the “wicked problem” of water scarcity, our team adopted a three-pronged interdisciplinary approach combining theoretical mathematics, statistics, environmental science, physics, economics, cultural anthropology, geography, epidemiology, computational science, and history to perform a fresh analysis of global water scarcity. Using a systems-network model, an agent-based network model, and a particle- optimization model, we characterized current forms of water scarcity, both physical and economic, and analyzed possible interventions on a global scope. After gaining a comprehensive analysis of the sources of the water crisis in the poorest country in the western hemisphere, Haiti, we designed interventions that addressed this largely economic crisis in a culturally-aware manner. Beginning with a systems-network model created using Vensim, we characterized water flow across the global network, taking into account locked, available, and potable water storage and its agricultural, industrial, and residential uses. The resulting system of differential equations was then solved in specification to Haiti, creating a comparison of the effects of possible interventions, concluding that both physical and social infrastructure for transportation and dissemination of potable water ought to be prioritized. Next, optimizing the distribution of such water required considering societal structure and the behavior of individuals. To model this, we created an agent-based network customized to Haiti using NetLogo software, representing each individual as a node on the network connected to others by links. We compared various distribution methods using metrics grounded in mathematical philosophy like Rawlsian logic, concluding that building on existing distribution centers that employ locals is the most efficient way to tailor distribution to the entirety of the social network, especially in regards to future water scarcity. Then, we adopted a broader perspective to general groundwater collection. A groundwater flow analysis algorithm was constructed in Python that can determine water loss to the ocean and hydraulic head in any region. The outputs of this algorithm, as well as geographical and climactic data, were used as inputs in a particle swarm optimization algorithm to determine optimal solutions to provide clean water at the minimum cost. This analysis concluded that using localized rainwater collection is both sufficient and most cost-effective to meet Haiti’s needs. All three models were tested for sensitivity and robustness to ensure their broader viability, such that they can be adopted by organizations in any region to analyze local water demands and intervention possibilities.

<!-- b000012 | prose | pages [2] -->
Where’s My Water?

<!-- b000013 | prose | pages [2] -->
Global Water Scarcity and Haiti’s Water Crisis 2016 Interdisciplinary Contest in Modeling

<!-- b000014 | prose | pages [2] -->
Team 52849 Problem E Page 1

<!-- b000015 | prose | pages [2] -->
January 2016

<!-- b000016 | heading | pages [2] -->
1 Introduction

<!-- b000017 | heading | pages [2] -->
1.1 Problem

<!-- b000018 | prose | pages [2] -->
According to the the United Nations, 1.6 billion people experience water scarcity. There are two components of water scarcity: economic and physical scarcity. Either the water exists in the region but money to clean or transport the water is lacking, or the supply of water in the region is less than the demand in the region.

<!-- b000019 | prose | pages [2] -->
In this paper, we use diﬀerent models to determine a region’s ability to provide water on the basis of multiple factors. We aim to use these models to understand the behavior of a speciﬁc system currently and how it is projected to behave 15 years in the future. We then use this behavior to propose an intervention plan and apply our models with intervention plans to determine whether they are viable.

<!-- b000020 | heading | pages [2] -->
1.2 Analysis of the Problem

<!-- b000021 | prose | pages [2] -->
According to Dr. Brian Davidson of University of Melbourne, water management and distribution should be classiﬁed as a “wicked problem” (1). “Wicked problems,” he writes, “do not have a single, once-oﬀ, optimal solution. They have a temporary solution. And it is a solution that has to change over time in response to changing circumstances.”

<!-- b000022 | prose | pages [2] -->
This wicked problem is dependent on the interplay of multiple factors and thus is inherently interdisciplinary, as shown below.

<!-- b000023 | prose | pages [2, 3] -->
1 Discipline Relevance to Problem Environmental Science Aﬀects how much water is “available” to take without hurting ecosystems and incurring environmental cost (can also be measured monetarily) Economics Monetary availability constrains the optimal solution Cultural Anthropology, Psychology Accurate assumptions of behavior behind models for the region, viability for solution/intervention plan to be adopted Epidemiology Disease aﬀects demand and supply of water History Understanding the reasons for the current water crisis and past attempted solutions can help in understanding constraints of the region

<!-- b000024 | furniture | pages [3] -->
Team 52849

<!-- b000025 | furniture | pages [3] -->
MCM/ICM

<!-- b000026 | furniture | pages [3] -->
Page 2 of 31

<!-- b000028 | prose | pages [3] -->
To come up with viable models to create viable solutions, we must have models which not only take into account environmental, economic, cultural, psychological and epidemiological perspec- tives but which also are robust enough to adapt to changes in the systems they address.

<!-- b000029 | heading | pages [3] -->
1.3 General Metric

<!-- b000030 | prose | pages [3] -->
Multiple requirements must be met for a solution to be considered viable and eﬀective, as mea- surable by the following general metric.

<!-- b000031 | prose | pages [3] -->
success = (mi −ms −me) + as + bc

<!-- b000032 | prose | pages [3] -->
where ms and me represent the direct cost of the solution and the environmental cost of the solution respectively, mi represents the money available to the region, s represents the ability of the solution to be self-sustainable, and c represents the ability of the solution to be culturally adopted/socially viable. These factors were considered in the formulation of each model, which each has its own metrics for eﬀective comparison within model solutions.

<!-- b000033 | heading | pages [3] -->
2 Haiti: A Case of Extreme Economic Water Scarcity

<!-- b000034 | prose | pages [3] -->
Once, it was the wealthiest colony in the world. Now, 300 years later, it’s the poorest country in the western hemisphere with the lowest access rates to improved water and sanitation.

<!-- b000035 | heading | pages [3] -->
2.1 From Riches to Rags: The Historical Sources of Haiti’s Water

<!-- b000036 | prose | pages [3] -->
Crisis

<!-- b000037 | prose | pages [3, 4] -->
Haiti was once the world’s wealthiest colony, but a series of revolutions that made Haiti the world’s ﬁrst free slave nation sparked Haiti’s present poverty and declining infrastructure. In exchange for Haitian freedom, France extorted an “independence debt” amounting to $21 billion in today’s dollars. Experts say the crushing burden of the debt is the principal historic cause of Haiti’s un- derdevelopment, directly responsible for today’s grinding poverty, but as France continues to resist pressure to repay Haiti, there is little evidence of poverty in Haiti declining in the near future. (33) This fundamental inability of the Haitian government to signiﬁcantly invest in water infras- tructure will continue if the situation does not change. Moreover, water infrastructure destruction was perpetuated by a series of US-supported Haitian dictators that enforced water-controlling regimes, using militias to cut oﬀpipe access to locals. (36) This lack of pipe access for water still persists, compounding reliance on external water sources.

<!-- b000038 | furniture | pages [4] -->
Team 52849

<!-- b000039 | furniture | pages [4] -->
MCM/ICM

<!-- b000040 | furniture | pages [4] -->
Page 3 of 31

<!-- b000042 | heading | pages [4] -->
2.2 Current Situation

<!-- b000043 | caption | pages [4] -->
Figure 1: A) The UNEP characterized multiple regions in Haiti as moderately exploited or over-

<!-- b000044 | prose | pages [4] -->
exploited based on Water Stress Indicators (WSI) in 2004. (5) B) According to the UNEP, “This 2008 update of the ‘Vital Water Graphics’ is aimed at giving an overview of the state of water resources in the world.” As shown, Haiti is the only country in the western hemisphere where less than 65% of the population has access to an improved water source. (6)

<!-- b000045 | prose | pages [4, 5] -->
Haiti’s water crisis was exacerbated by the 2010 earthquake (which ruptured most remaining water piping systems) (8) and the cholera epidemic, compounding both physical and economic scarcity, such that Haiti now has the lowest rates of access to improved water and sanitation infrastructure in the western hemisphere (7). Moreover, water-borne diseases like cholera are the leading cause for mortality of children in Haiti, linked to 50% of overall deaths (9). This has drawn tens of thousands of non-governmental organizations (NGOs) to Haiti, which is now known as the “Republic of NGOs” because there are more NGOs there per capita than anywhere else in the world, providing 80% of the country’s basic services (10). These organizations often alleviate short-term burdens, but since most do not train locals, they are often un-sustainable as other issues break out around the world and the NGOs Haitians have grown dependent on leave. Furthermore, due to the lack of coordination between NGOs, there is frequent duplication of work and ineﬃcient use of resources (11). It’s clear that this model is ineﬃcient and a long- term solution should involve coordination by a central authority. Because the current water and sanitation situation has evolved over decades of limited attention and resources, it will take a long- term, sustained eﬀort to improve the situation. Sanitation and clean water is key in the long-term, although short-term methods also need to be improved until the former is fully developed.

<!-- b000046 | furniture | pages [5] -->
Team 52849

<!-- b000047 | furniture | pages [5] -->
MCM/ICM

<!-- b000048 | furniture | pages [5] -->
Page 4 of 31

<!-- b000050 | heading | pages [5] -->
2.2.1 Comparison of Current Common Interventions in Haiti (2)

<!-- b000051 | prose | pages [5] -->
Intervention Cost Maintenance Sustainability Culturally Accepted? Impact Water Sachets $ none none yes individual Puriﬁcation Tablets $ none none yes individual Passive Solar Disinfection (in bottles) $ low high yes individual Boiling $$ medium medium very homes In-Situ Filtration Wells $$ low high yes commune Chlorinators $$$ some high yes commune

<!-- b000052 | heading | pages [5] -->
3 Models

<!-- b000053 | heading | pages [5] -->
3.1 Systems-Network Model

<!-- b000054 | caption | pages [5] -->
Figure 2: We created a systems model for water usage systems using Vensim software (3). Global

<!-- b000055 | prose | pages [5] -->
water systems involve agriculture, industry, and residential water usage, with adjustable rates based on inputted variables. This model can be customized to ﬁt any region.

<!-- b000056 | heading | pages [5] -->
3.1.1 System Flow Based on Model

<!-- b000057 | prose | pages [5] -->
Change in agricultural water:

<!-- b000058 | prose | pages [5] -->
d(agricultural) = d(funnel) −d(runoffa) −d(runoffl) dt dt dt dt Change in industrial water:

<!-- b000059 | prose | pages [5, 6] -->
d(industrial) = d(transporti) −d(contamination) −d(wastei) dt dt dt dt Change in residential water:

<!-- b000060 | furniture | pages [6] -->
Team 52849

<!-- b000061 | furniture | pages [6] -->
MCM/ICM

<!-- b000062 | furniture | pages [6] -->
Page 5 of 31

<!-- b000064 | prose | pages [6] -->
+ d(transportp) d(residential) = d(personalfiltration) −d(waster) dt dt dt dt Change in locked water:

<!-- b000065 | prose | pages [6] -->
d(locked) = d(contamination) + d(runoffl) −d(unlock) dt dt dt dt Change in available water:

<!-- b000066 | prose | pages [6] -->
d(available) = dt d(unlock) + d(wastei) + d(waster) + d(runoffa) −d(funnel) −d(transporti) −d(personalfiltration) −d(filter) dt dt dt dt dt dt dt dt Change in potable water:

<!-- b000067 | prose | pages [6] -->
−d(transportp) d(potable) = d(filter) + d(donate) −d(corruption) dt dt dt dt dt

<!-- b000068 | heading | pages [6] -->
3.1.2 Applied to Haiti

<!-- b000069 | prose | pages [6] -->
This network system of interaction allows for consideration of all possible factors involved in the water system, justifying the use of this systems model. By comparing the connectedness of each factor to the target variable (in Haiti’s case, residential water for drinking), the yield/change ratio of interventions in diﬀerent areas can be compared for eﬀectiveness. Applied to Haiti, there is an economic crisis of potable water, speciﬁcally the drinking water that individuals receive. Thus, in relation to the system above, we must ﬁnd a way to maximize the amount of water available for drinking.

<!-- b000070 | prose | pages [6] -->
Assumption: In Haiti, there is a large amount of available water (water that is currently not potable but which can be cleaned for use). Justiﬁcation: The water crisis in Haiti is mainly an economic one with regards to a lack of potable water for drinking, which contributes to the severe death rate caused by dehydration and compounded by cholera (7). Assumption: Haiti’s current transportation rate of potable water is extremely low. Justiﬁcation: The country currently lacks a pipe system, so mass transportation to the public is very minimal, leaving most residents to rely on purchased external water sachets or barrels for consumption (8). Assumption: In terms of drinking water wastage, waste rates cannot signiﬁcantly change. Justiﬁcation: All water that humans drink is passed through the body at some point, and there is neither a need nor a way to change this bodily function. Assumption: Haitian water corruption rates are non-negligible. Justiﬁcation: With high rates of gang violence and local corruption, especially compared to other countries, it is important to consider water lost to corruption which never makes it to the poor (33). Assumption: Haitian water donation rates are high. Justiﬁcation: As the “Republic of NGOs,” water donation rates from external organizations are high (10).

<!-- b000071 | prose | pages [6] -->
Determining Scarcity-Drivers By integrating the diﬀerential equation for residential water, we ﬁnd that:

<!-- b000072 | prose | pages [6] -->
residential = personallyfilteredwater + transportedwater −wastedwater + C

<!-- b000073 | prose | pages [6, 7] -->
With regards to drinking water, water lost to waste cannot be changed, and the constant of in- tegration representing current drinking water cannot be changed, so the relevant equation becomes:

<!-- b000074 | furniture | pages [7] -->
Team 52849

<!-- b000075 | furniture | pages [7] -->
MCM/ICM

<!-- b000076 | furniture | pages [7] -->
Page 6 of 31

<!-- b000078 | prose | pages [7] -->
drinkingwater = personallyfilteredwater + transportedwater

<!-- b000079 | prose | pages [7] -->
. Using the rates from the network-system above, we get:

<!-- b000080 | prose | pages [7] -->
drinkingwater = r ∗e ∗A + t ∗P

<!-- b000081 | prose | pages [7] -->
, where r is personal ﬁltration rate, e is personal ﬁltration eﬃciency, A is available water, t is trans- portation rate, and P is potable water. Further substituting the integrated rates from the model, we get the following summary of the most relevant drivers of drinking water scarcity:

<!-- b000082 | prose | pages [7] -->
drinkingwater = r ∗e ∗A + t ∗(f ∗A + d ∗E −c)

<!-- b000083 | prose | pages [7] -->
, where f is ﬁltration rate of available water, d is donation rate, E is external water, and c is loss to corruption.

<!-- b000084 | heading | pages [7] -->
3.1.3 Sensitivity: Comparing Scarcity-Driver Eﬀects

<!-- b000085 | prose | pages [7] -->
This base equation allows us to determine the most eﬀective interventions, based on two simple principles. 1) Increases in variables that are multiplied by fractions dampens the eﬀect of the increase:

<!-- b000086 | prose | pages [7] -->
(x) ∗1 n−> (x + c) ∗1 n = x ∗1 n + c ∗1 n 2) Increases in variables that are multiplied by numbers greater than 1 ampliﬁes the eﬀect of the increase, which is further ampliﬁed based on the magnitude of the value:

<!-- b000087 | prose | pages [7] -->
(x) ∗N−> (x + c) ∗N = x ∗N + c ∗N

<!-- b000088 | heading | pages [7] -->
3.1.4 Solution Comparison Based on Yield Ratios

<!-- b000089 | prose | pages [7] -->
In order of highest yield/change ratio, interventions include:

<!-- b000090 | heading | pages [7] -->
1) Increase transportation of potable water to homes (ex: Pipes)

<!-- b000091 | prose | pages [7] -->
The systems variable with the greatest change in drinking water per small changes in magnitude is t, since it is ampliﬁed by P (which is in turn ampliﬁed by A and E)and not mitigated by any fractional rates. Moreover, as Haiti’s pipe situation is already known to be in shambles, modest increases in pipe access would signiﬁcantly change the total transportation of water, further am- plifying this eﬀect.

<!-- b000092 | heading | pages [7] -->
2) Increase ﬁltration of available water (ex: In-Situ Wells)

<!-- b000093 | prose | pages [7, 8] -->
The ﬁltration f is ampliﬁed by both t and A, so the second best intervention is to increase ﬁltra- tion of available water to drive up potable water rates. The only caveat here is that if corruption were to rise in the future such that c > f ∗A + d ∗E, this intervention would be ineﬀective as the ﬁltered water would never reach the general populace. 3)Increase prevalence and eﬃciency of personal ﬁlters (ex: LifeStraws) For r and e, a small change results in a high change in yield magnitude due to the largeness of A. Changing ﬁlter eﬃciency may take a while on the scientiﬁc side, but spreading access to personal ﬁlters like LifeStraws will result in huge increases in drinking water due to the relative magnitude of A compared to e, which will always result in large values.

<!-- b000094 | furniture | pages [8] -->
Team 52849

<!-- b000095 | furniture | pages [8] -->
MCM/ICM

<!-- b000096 | furniture | pages [8] -->
Page 7 of 31

<!-- b000098 | heading | pages [8] -->
4) Increase donated water (ex: from NGO distribution of water sachets)

<!-- b000099 | prose | pages [8] -->
Increases in donations (d) are ampliﬁed by the coeﬃcient of E, respectively. Unfortunately, in current Haiti, this is the level on the priority table that is frequently the main resort, but this reliance on external water cannot be self-sustainable or a practical long-term solution.

<!-- b000100 | heading | pages [8] -->
5) Decrease corruption (ex: use diﬀerent distribution methods)

<!-- b000101 | prose | pages [8] -->
A decrease in corruption (c) is ampliﬁed by t to detract from public drinking water. 6) Changing the available amount of water has the least eﬀect in Haiti The systems-network indicates that in Haiti, a change in A will produce the least visible eﬀect, as it is already very large and changes to it will be mitigated by all of the fractional rates it is multiplied by. This is consistent with the analysis that Haiti’s water crisis is primarily one of distribution and dissemination, and less so based on physical scarcity.

<!-- b000102 | prose | pages [8] -->
Broader Impacts: Water scarcity is not a localized issue. For example, the leading cause of death in Haiti is water-borne disease like cholera; with characteristic symptoms of dehydration and diarrhea, this is both exacerbated by and exacerbating of the lack of access to potable water. As the epidemic has spread to other countries, like the Dominican Republic, Honduras, and Mex- ico, decreases in cholera spread will beneﬁt other countries as well. Moreover, a transition from dependence on external sources of water to a utilization of the physical water present in Haiti will increase self-sustainability of Haiti and allow for increased stabilization of the global economy.

<!-- b000103 | heading | pages [8] -->
3.2 Algorithmic Approach

<!-- b000104 | prose | pages [8] -->
We begin with an algorithmic approach in order to minimize the cost of providing clean water to the entirety of the population. This allows us to better analyze available solutions for a region to combat water scarcity.

<!-- b000105 | heading | pages [8] -->
3.2.1 Assumptions

<!-- b000106 | prose | pages [8, 9] -->
Assumption: Soil is homogeneous and isotropic. Justiﬁcation: Although this assumption does not fully reﬂect the true nature of soil compo- sitions, it makes groundwater ﬂow analysis a much more tractable problem. Error due to this assumption is mitigated by looking at average soil compositions and accounting for the pressure gradient and porosity changes in a column of groundwater. Assumption: Topography of a region is a proxy for hydraulic head of groundwater. Justiﬁcation: Given that a region is not actively removing groundwater, the bedrock should approximately match the terrain due to the manner in which the ground is layered. This does not account for irregularities beneath the surface, but large irregularities will have minimal eﬀect on groundwater ﬂow because the main factor is hydraulic head. Assumption: Water treatment costs are approximately consistent for most water. Justiﬁcation: Most water requires the same amount of resources to treat. The only exceptions are water with rare, harmful chemicals or extreme amounts of minerals. Most water does not contain such harmful chemicals, and water with high mineral content is accounted for in the de- salination aspect of the model. Assumption: Cost curves to treat water are approximately the same between countries. Justiﬁcation: The eﬃciency of treating water and the chemicals required to treat water are gen- erally universal. The main diﬀerence between countries lies in the minimum wage in the country and other factors that aﬀect the total cost only minimally.

<!-- b000107 | furniture | pages [9] -->
Team 52849

<!-- b000108 | furniture | pages [9] -->
MCM/ICM

<!-- b000109 | furniture | pages [9] -->
Page 8 of 31

<!-- b000111 | heading | pages [9] -->
3.2.2 Physical Scarcity Analysis

<!-- b000112 | prose | pages [9] -->
This section will ﬁrst look at the water scarcity problem by determining the maximum water intake that incurs minimal environmental damage. It will begin by predicting the maximum possible water collection from various methods without environmental impact. Because the groundwater is recharged only by precipitation (excluding minimal inﬁltration from the ocean), the amount of rainwater in the region is a limiting factor in water collection. Trivially, the amount of water naturally entering the region every year is bounded by the annual rainfall in that region. If the water demand exceeds the annual rainfall, then the country is forced to use water ﬂow from neighboring regions, desalination, or other expensive techniques. Our analysis will look only at the most popular methods and neglects future innovations, which we cannot predict as they do not yet exist.

<!-- b000113 | prose | pages [9] -->
Groundwater Availability In order to analyze this, we ﬁrst looked at how much water is ﬂowing into the ocean per year; this is considered wasted water because the cost of desalinating that water is far greater than that of treating the groundwater. So, our goal was to remove exactly as much water as is currently ﬂowing into the ocean. This of course ﬂuctuates due to the diﬀusion equation, but taking that amount of water from inland will decrease net outﬂow into the ocean (4). This will put minimal strain on ecosystems, as the water taken this way was lost to the ocean to begin with. First, we began by looking at how much water inﬁltrates the ground. This is given by (19) :

<!-- b000114 | prose | pages [9] -->
Infiltration = Rainfall −Evapotranspiration −Runoff whereRunoff = Rainfall ∗CoefficientRunoff Next, we imported topographical maps into Python and ran the following algorithm inspired by the diﬀusion equation to determine the amount of water ﬂowing into the ocean. Description of Groundwater Flow Algorithm

<!-- b000115 | caption | pages [9] -->
Figure 3: Logic Diagram of Groundwater Flow Algorithm

<!-- b000116 | prose | pages [9] -->
For each pixel on an input topographical map, approximate the hydraulic head according to the input color. Now, iteratively apply the following: For each pixel: look at the diﬀerence between it and it’s four neighbors (ni−n0). Sum this diﬀerence and denote it S. Next, set n0 = n0 + k ∗S. where k is a constant determined by groundwater ﬂow properties. If the pixel started as water and it receives water, reduce the hydraulic head of this pixel to 0 and move the water it received to a running total. Return the total.

<!-- b000117 | prose | pages [9] -->
Rainwater Availability Only so much water can be collected directly from rain water as the amount of space and money required to collect certain amounts of rainwater may be infeasible.

<!-- b000118 | furniture | pages [10] -->
Team 52849

<!-- b000119 | furniture | pages [10] -->
MCM/ICM

<!-- b000120 | furniture | pages [10] -->
Page 9 of 31

<!-- b000121 | prose | pages [10] -->
However, taking development into account leads to more reasonable methods of collecting water. Roads and land that has been cleared for agriculture have very high runoﬀcoeﬃcients. This contributes to increased amounts of runoﬀ, which causes increased erosion and predominantly ﬂows to the ocean. Thus, the amount of rainwater that can feasibly be collected without harming the environment is a function of how much humans have developed the region. The amount of water that should be taken from a region is given by:

<!-- b000122 | prose | pages [10] -->
Rainfall ∗(currentCoefficientRunoff −previousCoefficientRunoff)

<!-- b000123 | prose | pages [10] -->
Whether or not this amount can be obtained depends on the infrastructure of the region. Rain barrels would not cover enough area to collect this amount of water, but a combination of storm drains and other methods would.

<!-- b000124 | prose | pages [10] -->
Desalination Desalination is the most expensive of the methods. It requires considerably more energy because of the extreme salinity of ocean water. However, for coastal regions, water ob- tained by desalination is considered a limitless resource. Our model will treat desalination as such.

<!-- b000125 | prose | pages [10] -->
Water Collection Comparisons Groundwater collection is a good method of water collection because one well takes groundwater from a large area. It is also fairly consistent as opposed to rainwater collection, which is very dependent upon the weather. But, the rate of collection from groundwater is limited by a myriad of factors including the storage coeﬃcient, the cone of depression, and transmissibility. Rainwater collection can provide great amounts of fresh water. But, it is limited by the amount of space required to collect this water and the lack of consistency in weather patterns. This method is relatively inexpensive. Desalination is a good alternative for coastal regions because it is only limited by cost and en- ergy requirements. There is consistency in the amount of water obtained at all times, but it is considerably more expensive than other methods.

<!-- b000126 | heading | pages [10] -->
3.2.3 Economic Scarcity Analysis

<!-- b000127 | prose | pages [10] -->
Rainwater collection has varying costs depending on the method of collection. Collecting the water using barrels would require that trucks collect the water for treatment. This has a high operation cost, but has a relatively low initial cost. Using pipes to transport water from storm drains would have a low operating cost, but would have a high initial cost due to the cost of adding infrastructure. We will treat the cost of collecting the rainwater as the cost of transporting that water through pipes because truck costs are dependent upon many variables including eﬃciency, $ route, and terrain. It costs 2.31 ∗10−6 gal∗Km to transport water in pipes (26). Groundwater collection is extremely inexpensive. It has a low initial cost and takes water from a great area. The cost to collect groundwater is approximately .6$ (20). This ﬁgure varies depending on the hydraulic head and the energy source. Desalination cost is 1$ per thousand gallons (23).

<!-- b000128 | prose | pages [10] -->
Water Treatment Cost Analysis The cost to treat 1000 gallons can be accurately modeled by the following equation (24) :

<!-- b000129 | prose | pages [10, 11] -->
.6 x + .04 + .7 where x is in millions of gallons per day (MGD) and x > .1. Thus, the daily operation cost of a water treatment plant, when operating on average water quality, is given by:

<!-- b000130 | furniture | pages [11] -->
Team 52849

<!-- b000131 | furniture | pages [11] -->
MCM/ICM

<!-- b000132 | furniture | pages [11] -->
Page 10 of 31

<!-- b000134 | prose | pages [11] -->
.6 x + .04 + .7) ∗x ∗1000 (

<!-- b000135 | heading | pages [11] -->
3.2.4 Finding an Optimal Solution

<!-- b000136 | prose | pages [11] -->
Although our analysis has made many assumptions to simplify the problem, we decided to pick an optimization algorithm that could easily extend to versions of the problem that account for increased complexity and nonlinearity. The cost functions, water treatment costs, and water collection costs are predominantly nonlinear. Thus, ﬁnding the least expensive solution to the problem can be computationally expensive. In considering the inherent nonlinearity and high dimensionality of the problem, we elected to use a Particle Swarm Optimization algorithm. Using this algorithm on geographical, climactic, and theoretical input, a country can determine their cheapest solution to their water crisis. Unfortunately, there may not be a solution and in that case, the algorithm will return a cost higher than the country can aﬀord.

<!-- b000137 | prose | pages [11] -->
Particle Swarm Optimization Given: constants, constraints, function to optimize Output: optimal solution 1. Create q vectors that satisfy the constraints and are in the domain of the function. Let us call these vectors particles. Each particle is able to remember its current position, its best position, the current global optimum position, and its current velocity. 2. For each particle, update its velocity and position based on the following two equations:

<!-- b000138 | prose | pages [11] -->
vi+1 = vi + c1 ∗r1 ∗(pbest −pcurrent) + c2 ∗r2 ∗(globalbest −pcurrent)

<!-- b000139 | prose | pages [11] -->
pi+1 = pi + vi + 1 where p is position (or vector value), c is a constant, r is a random number, and globalbest is the best position obtained by any particle. Next, set iterations = iterations + 1. If iterations < n, go to 2. Else, go to 3. 3. Return global optimum position and cost.

<!-- b000140 | heading | pages [11] -->
3.2.5 Applied to Haiti

<!-- b000141 | prose | pages [11] -->
When the algorithm was applied to Haiti, it determined that the minimum cost was approximately 10 million dollars a year using the method of rainwater collection, the most viable option for Haiti. This ﬁgure is a lower bound because it does not include yearly maintenance costs, initial infrastructure cost, or other implementation speciﬁc factors. For more details on calculations, please reference the algorithm implementations in the Appendix section. Since Haiti will not be able to provide this sum for themselves, international aid will be required to maintain such a system, indicating that the short term solution will require reliance on distribution as shown in the other models. To clarify, Haiti’s water is out of reach only due to economic, not physical, scarcity, as demonstrated by the model; water will not “run out” in the physical sense in the predictable future. Moreover, should the governmental ﬁnancial situation improve, it is possible that Haiti may be able to adopt this as a long-term, self-sustaining method.

<!-- b000142 | furniture | pages [12] -->
Team 52849

<!-- b000143 | furniture | pages [12] -->
MCM/ICM

<!-- b000144 | furniture | pages [12] -->
Page 11 of 31

<!-- b000145 | heading | pages [12] -->
3.2.6 Sensitivity Analysis

<!-- b000146 | prose | pages [12] -->
The algorithm performs consistently under repeated trials. Modiﬁcations to cost values within a margin of error produced essentially the same solution, but with diﬀerent end costs. The greatest factor that would aﬀect the model, in addition to greater knowledge about underlying equations instead of approximations, is the addition of the initial costs. This could be easily implemented with a multiple year amortized loan structure, in which the company pays back a company over time.

<!-- b000147 | heading | pages [12] -->
3.3 Agent-Based Networks Approach

<!-- b000148 | prose | pages [12] -->
For regions where inadequate piping and abundant pollution prevent the independent acquirement of water, a distribution system of clean water must be implemented. Here it is imperative to understand the best method of distribution. Since many countries and regions have a complex social structure, this social structure must be taken into account when deciding how to fully optimize the distribution of water such that the people who are in need– the ’Common Man’– get their fair share.

<!-- b000149 | prose | pages [12] -->
Questions to consider: are the common men “connected” to one another? That is, one, do they physically interact and, two, are they even willing to distribute a portion of the water they receive to others? Is there a central power that has more connections to the common man? Is it accurate to assume that they will distribute the water they receive as well? Who is the most strategic member of this community to whom we can give a water source to who is not only physically connected to the people who need the water but whose ties to them are also weighty enough to guarentee fair distribution? The disemination of given water is entirely dependent upon individual decisions, hence why an agent-based model must be taken into account.

<!-- b000150 | prose | pages [12] -->
While the approach is general, a “general” model cannot be conceived. Each model of this type is inherently unique to each community, as the entire structure of the network is dependent upon the social structure of the community. Metrics Mean Water

<!-- b000151 | prose | pages [12] -->
X meanwater = (water)c/n

<!-- b000152 | prose | pages [12] -->
where waterc refers to the water each common man has and n refers to the number of common men. This is helpful for understanding the average amount of water each common man will receive; larger numbers are better than small. The output is in liters per common man. Root Mean Squared Water

<!-- b000153 | prose | pages [12] -->
X 2 (demand −water)c standardizedneed = sqrt( u)/n

<!-- b000154 | prose | pages [12] -->
where (demand −water)c1 refers to the unmet need of each common man with need, cu, and n refers to the number of common men. The output is in liters per common man.

<!-- b000155 | prose | pages [12, 13] -->
A standardized root mean squared equation was used to weight the neediest people higher, based on the fairness theory posited by Harvard professor of philosophy John Rawls. Rawls conducted a thought experiment known as the “veil of ignorance,” concluding that when determining fairness for society as a whole one must adopt the “maximin” principle, choosing to help the least well oﬀ in society to establish security so that the amount of hardship any one individual experiences is minimized (34). This also makes sense in context, since a lack of water that is dangerously/deadly high should be addressed before trying to bridge the gap for the slightly needy, to minimize deaths by dehydration. We weighted the least well oﬀusing this method such that a higher number was indicative of more unmet need, so smaller numbers indicate a better solution.

<!-- b000156 | furniture | pages [13] -->
Team 52849

<!-- b000157 | furniture | pages [13] -->
MCM/ICM

<!-- b000158 | furniture | pages [13] -->
Page 12 of 31

<!-- b000160 | heading | pages [13] -->
3.3.1 Applied to Haiti

<!-- b000161 | prose | pages [13] -->
Since most Haitian citizens lack independent access to potable water, external water is often neces- sary. (7) In attempts to meet these needs, NGOs often implement distribution systems of potable water, like distributing jugs of water using trucks (8). However, to optimize the distribution of such water, the network of the society must be taken into account.

<!-- b000162 | prose | pages [13] -->
For this purpose, an agent-based networks model was created in NetLogo (27), as shown be- low. As per the social structure of Haiti, in this model, nodes (the common people), gangs, the elite/local government, hospital centers, and distributors employed by hospital centers interact. Water is moved along the network. The amount of water a person chooses to give its connections are dependent on the weight of the connections, and each agent keeps a set constant amount of water, value given by user input.

<!-- b000163 | caption | pages [13] -->
Figure 4: The user interface and structure of the Haitian speciﬁc agent based networks model

<!-- b000164 | heading | pages [13] -->
Assumption:

<!-- b000165 | prose | pages [13] -->
The amount each group demands in relation to one another is gang >elite >common man Justiﬁcation: The amount that each member demands is exactly what causes the discrepancy in which water is given to a community but does not reach the people in need. Gangs will ’demand’ more than the elite since they are made up of more members.

<!-- b000166 | heading | pages [13] -->
Assumption: Connections between the local government, gangs, hospice centers, distributors

<!-- b000167 | prose | pages [13] -->
employed by hospice centers, and the common people/citizens actually in need of water were weighted as follows:

<!-- b000168 | prose | pages [13, 14] -->
Local Government - Common Man: Weak Local Government - Gangs: Moderate Gangs - Gangs: Strong Gangs - Common Man: Weak Hospice Centers - Distributors: Strong Distributors - Common Man: Strong Common Man - Common Man: Moderate Justiﬁcation: The social inequalities perpetuated by the Duvalier regime persist to this day, compounding a large gap between the elites and the poor. Until the government has the ﬁnancial resources to overcome the eﬀects of France’s demanded debt, there is no evidence of governmental ability to fund large-scale social projects to decrease the wealth gap. (33). Furthermore, the language barrier between the general population, almost all of which speaks Creole, and the elites, who speak French, compounds this wealth gap in terms of job access and social mobility (35). Simulation 1: Current State By creating this network based oﬀof the social structure of Haiti, we can understand the behavior that occurs currently when water distribution is attempted through local distribution (36).

<!-- b000169 | furniture | pages [14] -->
Team 52849

<!-- b000170 | furniture | pages [14] -->
MCM/ICM

<!-- b000171 | furniture | pages [14] -->
Page 13 of 31

<!-- b000173 | prose | pages [14] -->
Testing was run under the parameters of an initial water amount given 30 L. We began by saying that the common man would keep some fraction of his water received, 0.5, and the elite and gangs would take slightly more, 0.6. By starting the water ﬂow at the common source of the elite and seeing how it disseminates along the network, the common man only obtained, on average, 0.81 L out of the original 30 L – that is, 0.2%– of the total water given to the population.

<!-- b000174 | prose | pages [14] -->
This shows an important facet of short term solutions. Though infrastructure may be built in the long-term, in order for Haitians’ basic needs to be met short-term, distribution of water is likely necessary. However, one must take into account the social and cultural factors of Haitian society, as in this network model; current methods of giving to the people in power are not as eﬀective as one would hope with all the money being put into obtaining and giving this water. Simulation 2: Future We can adjust testing parameters to account for likely changes to happen to society in 15 years that would impact the network, such as population growth. According to the United Nations Department of Economic and Social Aﬀairs’ World Population Prospects (the 2015 revision), the population of Haiti is predicted to increase by 17% in 15 years (28). To more accurately model Haiti in 15 years, this predicted population increase was taken into account in our simulations. We also ran simulations with a predicted 25% increase in population in the case that the number was an underestimation and to also test the robustness of our model.

<!-- b000175 | furniture | pages [15] -->
Team 52849

<!-- b000176 | furniture | pages [15] -->
MCM/ICM

<!-- b000177 | furniture | pages [15] -->
Page 14 of 31

<!-- b000178 | caption | pages [15] -->
Figure 5: We simulated 100 runs of the model for each factor, with no population growth, 17%

<!-- b000179 | prose | pages [15] -->
population growth (as predicted for Haiti), and 25% population growth (as an overestimate to measure robustness), with the currently used elite distribution method.

<!-- b000180 | prose | pages [15] -->
It is qualitatively observable that mean water per person decreases as the population increases. To quantify this, we ran a one-way ANOVA test yielding F=177.3 and p<.001, indicating that the diﬀerences are statistically signiﬁcant. They were conﬁrmed with a Tukey post hoc test with 0% vs 17% yielding p<.01, 0% vs 25% yielding p<.01, and 17% vs 25% yielding p<.01, indicating that mean water decreases as the population grows with this distribution method, meaning that the method is predicted to lose eﬃciency. Thus, as Haiti is expected to increase in population, current methods will lose eﬃciency.

<!-- b000181 | heading | pages [15] -->
3.3.2 Intervention Plan

<!-- b000182 | prose | pages [15] -->
Since the current distribution strategy in place is ineﬀective and is only projected to decrease in eﬃciency over time, we propose a new strategy, based on the operations of Partners in Health in Haiti (29). Using a system of holistic care, founded on knowledge that improvement in well-being can only occur if all aspects of health are addressed, Partners in Health already employs locals in 12 hospitals across the country as community health workers (30). They visit hard-to-reach rural villages on a regular basis, administering medicine and care involving adequate nutrition and water, because all aspects of health must be addressed for patient improvement. Experts agree that this method of care distribution in Haiti has been one of the most eﬀective methods (31) (32). We plan to piggyback on these existing systems of healthcare distribution to supplement their holistic care processes with water distribution.

<!-- b000183 | prose | pages [15] -->
With this new strategy implemented, additional assumptions need to be made about the be- havior of groups/people. Assumption: The hospital centers and distributors employed by the hospital centers will keep no fraction of the water for themselves, instead distributing all of it amongst their connections. Justiﬁcation: Hospitals and employed distributors only receive the water for the purpose of dis- tributing it, it is their job to do so without taking any portion.

<!-- b000184 | prose | pages [15] -->
Simulation 1: Current State Comparison We compared the standardized needs using our intervention method to the original/current method in place.

<!-- b000185 | furniture | pages [16] -->
Team 52849

<!-- b000186 | furniture | pages [16] -->
MCM/ICM

<!-- b000187 | furniture | pages [16] -->
Page 15 of 31

<!-- b000188 | caption | pages [16] -->
Figure 7: In the ﬁgure on the left, the mean waters received are compared between distribution

<!-- b000189 | prose | pages [16] -->
method A, the current method, and distribution method B, our proposed method. The higher mean water is indicative of a more favorable solution. As seen on the right, distribution method B also does a better job of minimizing the root mean squared need.

<!-- b000190 | prose | pages [16] -->
To conﬁrm qualitative observations, we ran an unpaired t-test with df=198 for the mean water values, yielding t=175.3 and p<.0001. We ran another unpaired t-test on standardized need val- ues, calculating a t value of 29.8, yielding p<.0001. Both tests support the alternative hypothesis that center distribution is more eﬀective than elite-based distribution, both in terms of mean wa- ter, and in terms of addressing the least well oﬀ.

<!-- b000191 | prose | pages [16] -->
Simulation 2: Future Comparison To simulate future conditions wherein the population increases, we tested this strategy with in- creasing levels of number of nodes.

<!-- b000192 | caption | pages [16] -->
Figure 9: Comparison of resistance to population growth among the two methods

<!-- b000193 | prose | pages [16, 17] -->
The results indicate that, while both methods are sensitive to population growth with each method working more eﬀectively on smaller populations, in each scenario the center distribution method still has increased mean water among the populace as compared to elite distribution.

<!-- b000194 | furniture | pages [17] -->
Team 52849

<!-- b000195 | furniture | pages [17] -->
MCM/ICM

<!-- b000196 | furniture | pages [17] -->
Page 16 of 31

<!-- b000198 | prose | pages [17] -->
To conﬁrm qualitative conclusions of relationship between the two methods with population growth, we ran a two-way ANOVA test on 100 runs each of the simulation with no population growth, 17% population growth (as predicted for Haiti), and 25% population growth (as an over- estimate to measure robustness). For the ANOVA, we placed distribution method across rows and percent growth across columns. The test yielded a p-value across rows of <.0001, across columns of <.0001, and with rows x columns of <.0001. This was conﬁrmed using a Tukey post hoc test with 0% vs 17% yielding p<.01, 0% vs 25% yielding p<.01, and 17% vs 25% yielding p<.01.

<!-- b000199 | heading | pages [17] -->
3.3.3 Sensitivity Analysis

<!-- b000200 | prose | pages [17] -->
Environment While the social structure of the network should remain the same in subenvironments of Haiti, the number of connections each person has to one another may vary in rural vs. more devel- oped areas. To test the eﬀect of this, we varied the average degree of the nodes (the number of connections each had to others).

<!-- b000201 | caption | pages [17] -->
Figure 10: We simulated 100 runs of the model for each ??ﬁll what we ran for degrees

<!-- b000202 | prose | pages [17] -->
We ran a one-way ANOVA test on the runs with varying degree among the elite distribution method, and found F=5159.06, yielding p<.0001. To corroborate our results, we used a Tukey post hoc test to determine p<.01 between every pair of means. This indicates that the interconnectivity of the people signiﬁcantly aﬀects the amount each receives using the current method.

<!-- b000203 | prose | pages [17] -->
The same tests on changes in average degree with the center distribution method yielded p>.9, indicating no signiﬁcant diﬀerence in values. This means that average degree had no signiﬁcant impact on the average amount of water each person received, further emphasizing the robustness of our solution.

<!-- b000204 | furniture | pages [18] -->
Team 52849

<!-- b000205 | furniture | pages [18] -->
MCM/ICM

<!-- b000206 | furniture | pages [18] -->
Page 17 of 31

<!-- b000207 | heading | pages [18] -->
4 Intervention Plans Proposed

<!-- b000208 | heading | pages [18] -->
4.1 Short Term

<!-- b000209 | prose | pages [18] -->
Until Haiti is able to redirect its money into building stronger infrastructure, as recommended in the long term plan, the current short-term plan of distributing water should be optimized. As supported by the agent-based networks model and comparison between distribution methods, dissemination along the social network is optimized if water is distributed through existing health distribution centers that are uniquely able to access hard-to-reach areas. We hope to build on existing medical centers in the area with good reputations of care and a focus on holistic treatment, like Partners in Health hospitals and Haiti Health Ministries, that employ community health workers to distribute medicine, food, and water to hard-to-reach locals, which tend to be the poorest. This is viable as we are simply building upon pre-existing systems that distribute medicine through locally-employed and is thereby also self-sustaining.

<!-- b000210 | heading | pages [18] -->
4.2 Long Term

<!-- b000211 | prose | pages [18] -->
The solution that would yield the highest change, according to the systems and algorithmic model, was increasing the transportation of potable water to homes through piping systems. If not possible, the second best long-term solution would be to increase mass ﬁltration through creating in-situ wells. Both of these, achievable by redirecting NGO help and donations towards this initiative and building on the proposed governmental DINEPA plan for water and sanitation(7), would make the region less susceptible to water scarcity.

<!-- b000212 | heading | pages [18] -->
5 Comparison of Strengths and Weaknesses

<!-- b000213 | heading | pages [18] -->
5.1 Systems Model

<!-- b000214 | heading | pages [18] -->
5.1.1 Strengths

<!-- b000215 | prose | pages [18] -->
The systems-based model accounts for water ﬂow across the global network and takes into account a variety of physical and social factors. The model considers agricultural, industrial, and residential uses, any of which can be analyzed for maximization and speciﬁed to a location. It also allows for prioritization of diﬀerent intervention areas based on their relative impacts on the desired outcome. Considering this ampliﬁcation and dampening of factors is important as it allows for optimization of eﬀorts.

<!-- b000216 | heading | pages [18] -->
5.1.2 Weaknesses

<!-- b000217 | prose | pages [18] -->
In situations of physical scarcity, large amounts of region-speciﬁc data are needed to draw speciﬁc conclusions from this model. Moreover, this model generalizes water systems into broad categories, but in some instances more speciﬁcity in terms of water usage may be necessary. In those cases, use of an agent-based model may be preferable.

<!-- b000218 | furniture | pages [19] -->
Team 52849

<!-- b000219 | furniture | pages [19] -->
MCM/ICM

<!-- b000220 | furniture | pages [19] -->
Page 18 of 31

<!-- b000221 | heading | pages [19] -->
5.2 Algorithmic Model

<!-- b000222 | heading | pages [19] -->
5.2.1 Strengths

<!-- b000223 | prose | pages [19] -->
This process takes into account multiple factors including groundwater ﬂow and evapotranspiration rates. Additionally, it accounts for overall development in the region considers environmental factors. Another strength of the model is that it attempts to solve the cost problem with the demand problem in mind as opposed to solving demand with cost constraints. This ﬁrst considers the population’s needs and ensures that any solution will satisfy the whole population. On the contrary, such a solution may not be obtainable due to economic scarcity, and the country must resort to other solutions. This beneﬁts the model as it provides an accurate analysis of the situation and determines if a country can provide clean water for it’s people under economic and environmental constraints. Likewise, if the algorithm reports that a country is unable to provide for it’s people due to physical scarcity, then the country can use a variation of the Groundwater Flow algorithm to determine how long they would be able to rely on overusing groundwater while the country ﬁnds an alternative solution. This can be done by simply incorporating wells into the Groundwater Flow algorithm and seeing how long before net groundwater ﬂow into the ocean is approximately zero. Thus, the model allows the country to look at its abilities to collect water. Additionally, although the model does not account for many underlying variables, the model can easily be extended to account for them. This allows the model to be applied for many purposes and gives it the ability to be improved upon. Someone attempting to ﬁnd the solution would be able to do so with increased amounts of data at their disposal.

<!-- b000224 | heading | pages [19] -->
5.2.2 Weaknesses

<!-- b000225 | prose | pages [19] -->
The algorithm does not directly take environmental impact into account when determining the optimal solution. Instead, it is up to the user to determine whether or not a solution to the water scarcity problem is environmentally friendly. Assuming that the country wants to protect the environment, the country can choose how much they want to factor in the environment when looking for an optimal solution. This was done to make the problem more tractable and allow for discretion of the user, but causes the algorithm to not always produce the most environmentally friendly solution, too. As with most complex problems, the quality of the solution depends greatly on the amount and quality of the data input into the algorithm. By using approximations or other assumptions, the accuracy of the solution decreases. But, provided that the approximations are good, the algorithm will still provide a solution that approximates the true solution well. Finally, the algorithm used is a stochastic algorithm as opposed to a deterministic algorithm. This was done to preserve the ability to increase the complexity of the algorithm and account for great nonlinearity. Although it may not give the optimal solution, it is able to ﬁnd a feasible solution (if one exists) in a reasonable amount of time. This is unlike its deterministic counterpart, which may render the problem intractable. However, the stochastic algorithm’s failure to guarantee the optimal solution makes it tractable.

<!-- b000226 | furniture | pages [20] -->
Team 52849

<!-- b000227 | furniture | pages [20] -->
MCM/ICM

<!-- b000228 | furniture | pages [20] -->
Page 19 of 31

<!-- b000229 | heading | pages [20] -->
5.3 Agent-Based Networks Model

<!-- b000230 | heading | pages [20] -->
5.3.1 Strengths

<!-- b000231 | prose | pages [20] -->
The agent-based networks model takes into account the individual decisions and factors that play a role in distribution of a resource. The model also considers unique social structure of a region to provide and optimize the short term solution of the dissemination of water. Since it is agent- based, it can track water ﬂow on both a broad level and on an interpersonal level, allowing for sophisticated data analysis.

<!-- b000232 | heading | pages [20] -->
5.3.2 Weaknesses

<!-- b000233 | prose | pages [20] -->
The model must be adjusted to the social structure of the region in question. Additionally, since the model is agent-based and often involves over 100 nodes, simulations using this model are more time-consuming than those with the systems-network or algorithmic models.

<!-- b000234 | heading | pages [20] -->
6 Conclusions

<!-- b000235 | prose | pages [20] -->
The combination of the three models allowed us to address physical and social factors of water scarcity from multiple perspectives. While the algorithmic model focused on the raw numbers and data analysis, the systems and agent-based networks models allowed for social and behavioral factors to be taken into account as well. These factors are important because optimal solutions are only meaningful if they can be reasonably adopted by the target population. The synthesis of our work was not only the creation of a region-speciﬁc intervention plan for Haiti, which is currently highly in need, but also the creation of three powerful models which can be adopted by organizations in any region to analyze local water demands and intervention possibilities.

<!-- b000236 | furniture | pages [21] -->
Team 52849

<!-- b000237 | furniture | pages [21] -->
MCM/ICM

<!-- b000238 | furniture | pages [21] -->
Page 20 of 31

<!-- b000239 | heading | pages [21] -->
References

<!-- b000240 | references | pages [21] -->
[1] Davidson, Brian. “Wicked Problems Demand Adaptive Responses: How Does the Murray

<!-- b000241 | references | pages [21] -->
Darling Plan Stack Up?” The Conversation. N.p., 20 Dec. 2011. Web. 31 Jan. 2016.

<!-- b000242 | references | pages [21] -->
[2] “Sustainable Safe Water Solutions for Haiti.” Grand Valley State University, n.d. Web. 01 Feb.

<!-- b000243 | references | pages [21] -->
2016.

<!-- b000244 | references | pages [21] -->
[3] Ventana Systems, Inc.. (2006). Vensim PLE Software, Ventana Systems Inc.. Retrieved at

<!-- b000245 | references | pages [21] -->
May 30, 2008, from the website temoa :

<!-- b000246 | references | pages [21] -->
Open Educational Resources (OER) Portal at

<!-- b000247 | references | pages [21] -->
http://www.temoa.info/node/3682

<!-- b000248 | references | pages [21] -->
[4] Summary of Diﬀerential Equations for Groundwater Flow. N.p.: Humboldt State University,

<!-- b000249 | references | pages [21] -->
n.d. PDF.

<!-- b000250 | references | pages [21] -->
[5] “Water Scarcity Map.” Vital Water Graphics. United Nations, n.d. Web. 31 Jan. 2016.

<!-- b000251 | references | pages [21] -->
[6] An Overview of the State of the World’s Fresh and Marine Waters. 2nd Edition, 2008.

<!-- b000252 | references | pages [21] -->
(http://www.unep.org/dewa/vitalwater/index.html).

<!-- b000253 | references | pages [21] -->
[7] Gelting, Richard et al. “Water, Sanitation and Hygiene in Haiti: Past, Present, and Future.”

<!-- b000254 | references | pages [21] -->
The American Journal of Tropical Medicine and Hygiene 89.4 (2013): 665–670. PMC. Web.

<!-- b000255 | references | pages [21] -->
31 Jan. 2016.

<!-- b000256 | references | pages [21] -->
[8] Knox, Richard. Water In The Time Of Cholera: Haiti’s Most Urgent Health Problem. National

<!-- b000257 | references | pages [21] -->
Public Radio. 16 April 2012. Web.

<!-- b000258 | references | pages [21] -->
[9] Sentlinger, Katherine. “Water In Crisis - Spotlight Haiti.” The Water Project. N.p., n.d. Web.

<!-- b000259 | references | pages [21] -->
31 Jan. 2016.

<!-- b000260 | references | pages [21] -->
[10] Edmonds, Kevin. “NGOs and the Business of Poverty in Haiti.” NACLA: Reporting on the

<!-- b000261 | references | pages [21] -->
Americas since 1967. North American Congress on Latin America, n.d. Web. 31 Jan. 2016.

<!-- b000262 | references | pages [21] -->
[11] US Army Corps. Water Resources Assessment of Haiti. Rep. N.p.: n.p., 1999. Print.

<!-- b000263 | references | pages [21] -->
[12] Haiti Physical Map. N.d. Maps. ¡i¿World and USA Maps¡/i¿. Web. 31 Jan. 2016.

<!-- b000264 | references | pages [21] -->
[13] “Recommended RunoﬀCoeﬃcient Values Table.” Gwinnett County Government, n.d. Web.

<!-- b000265 | references | pages [21] -->
31 Jan. 2016.

<!-- b000266 | references | pages [21] -->
[14] “Average Monthly Temperature and Rainfall in Haiti.” Climate Change Knowledge Portal.

<!-- b000267 | references | pages [21] -->
The World Bank Group, n.d. Web. 01 Feb. 2016.

<!-- b000268 | references | pages [21] -->
[15] “Springs - The Water Cycle.” US Geological Survey, n.d. Web. 01 Feb. 2016.

<!-- b000269 | references | pages [21] -->
[16] “Haiti.” The World Factbook. Central Intelligence Agency, n.d. Web. 01 Feb. 2016.

<!-- b000270 | references | pages [21] -->
[17] Dharmasena, P. B. “Estimating Runoﬀfrom Small Agricultural Lands.” (1992): n. pag. Web.

<!-- b000271 | references | pages [21] -->
[18] Hadden, and Minson. The Geology of Haiti: An Annotated Bibliography of Haiti’s Geology,

<!-- b000272 | references | pages [21] -->
Geography and Earth Science. Rep. N.p.: US Army Corps of Engineers, n.d. Print.

<!-- b000273 | furniture | pages [22] -->
Team 52849

<!-- b000274 | furniture | pages [22] -->
MCM/ICM

<!-- b000275 | furniture | pages [22] -->
Page 21 of 31

<!-- b000276 | references | pages [22] -->
[19] Abdullahi, Musa G. “Eﬀect of Rainfall on Groundwater Level Fluctuation in Terengganu,

<!-- b000277 | references | pages [22] -->
Malaysia.” Journal of Geophysics Remote Sensing J Geophys Remote Sens 04.02 (2015): n.

<!-- b000278 | references | pages [22] -->
pag. Web.

<!-- b000279 | references | pages [22] -->
[20] “Water Wells for Haiti.” Haiti Reconstruction. N.p., n.d. Web. 01 Feb. 2016.

<!-- b000280 | references | pages [22] -->
[21] Hu, Xiaohui. “Particle Swarm Optimization.” N.p., n.d. Web. 01 Feb. 2016.

<!-- b000281 | references | pages [22] -->
[22] Computation of Long-term Annual Renewable Water Resources (RWR) by Country (in

<!-- b000282 | references | pages [22] -->
Km3/year, Average) - Haiti. Rep. N.p.: Food and Agriculture Organization of the United

<!-- b000283 | references | pages [22] -->
Nations, n.d. Print.

<!-- b000284 | references | pages [22] -->
[23] Masters, Gilbert. “Introduction to Environmental Science amp; Engineering.” N.p.: George

<!-- b000285 | references | pages [22] -->
Mason U, n.d. N. pag. Print.

<!-- b000286 | references | pages [22] -->
[24] Cost Estimating Processes. Rep. N.p.: Guadalupe-Blanco River Authority, n.d. Print.

<!-- b000287 | references | pages [22] -->
[25] Desalination: A National Perspective. Washington, D.C.: National Academies, 2008. Print.

<!-- b000288 | references | pages [22] -->
[26] “Glacial Icebergs: Sources of Freshwater.” Mission 2012 : Clean Water. N.p., n.d. Web. 01

<!-- b000289 | references | pages [22] -->
Feb. 2016.

<!-- b000290 | references | pages [22] -->
[27] Wilensky, U. (1999). NetLogo. http://ccl.northwestern.edu/netlogo/. Center for Connected

<!-- b000291 | references | pages [22] -->
Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

<!-- b000292 | references | pages [22] -->
[28] “World Population Prospects - Haiti.” World Population Prospects. United Nations Depart-

<!-- b000293 | references | pages [22] -->
ment of Economic and Social Aﬀairs, n.d. Web. 31 Jan. 2016.

<!-- b000294 | references | pages [22] -->
[29] “Community Health Workers: Making House Calls.” Partners in Health, n.d. Web. 01 Feb.

<!-- b000295 | references | pages [22] -->
2016.

<!-- b000296 | references | pages [22] -->
[30] “Haiti.” Partners in Health, n.d. Web. 01 Feb. 2016.

<!-- b000297 | references | pages [22] -->
[31] Rich, Michael L., Ann C. Miller, Peter Niyigena, Molly F. Franke, Jean Bosco Niyonzima,

<!-- b000298 | references | pages [22] -->
Adrienne Socci, Peter C. Drobac, Massudi Hakizamungu, Alishya Mayﬁeld, Robert Ruhayisha,

<!-- b000299 | references | pages [22] -->
Henry Epino, Sara Stulac, Corrado Cancedda, Adolph Karamaga, Saleh Niyonzima, Chase

<!-- b000300 | references | pages [22] -->
Yarbrough, Julia Fleming, Cheryl Amoroso, Joia Mukherjee, Megan Murray, Paul Farmer,

<!-- b000301 | references | pages [22] -->
and Agnes Binagwaho. “Excellent Clinical Outcomes and High Retention in Care Among

<!-- b000302 | references | pages [22] -->
Adults in a Community-Based HIV Treatment Program in Rural Rwanda.” JAIDS Journal of

<!-- b000303 | references | pages [22] -->
Acquired Immune Deﬁciency Syndromes 59.3 (2012): n. pag. Web.

<!-- b000304 | references | pages [22] -->
[32] Jerome, Gregory, and Louise C. Ivers. “Community Health Workers in Health Systems

<!-- b000305 | references | pages [22] -->
Strengthening: A Qualitative Evaluation from Rural Haiti.” Aids 24.Suppl 1 (2010): n. pag.

<!-- b000306 | references | pages [22] -->
Web.

<!-- b000307 | references | pages [22] -->
[33] Institute for Justice and Democracy in Haiti. Institute for Justice and Democracy

<!-- b000308 | references | pages [22] -->
in Haiti. Web. 26 July 2014. (http://www.ijdh.org/2010/03/topics/economy/restitution-of-

<!-- b000309 | references | pages [22] -->
haitis-independence-debt/).

<!-- b000310 | references | pages [22] -->
[34] Rawls, John. A Theory of Justice. Revised ed. Cambridge: Harvard University Press, 1999.

<!-- b000311 | furniture | pages [23] -->
Team 52849

<!-- b000312 | furniture | pages [23] -->
MCM/ICM

<!-- b000313 | furniture | pages [23] -->
Page 22 of 31

<!-- b000314 | references | pages [23] -->
[35] DeGraﬀ, Michel. Language Barrier in Haiti. Boston Globe. 16 June 2010. Accessed 1 February

<!-- b000315 | references | pages [23] -->
2016.

<!-- b000316 | references | pages [23] -->
[36] Fass SM. “Political economy in Haiti: the drama of survival.” New Brunswick: transaction

<!-- b000317 | references | pages [23] -->
Books, 170. Quoted in Arnold AJ, 1990. Haiti’s misery amidst wretched poverty: political

<!-- b000318 | references | pages [23] -->
economy in Haiti: the drama of survival by Simon M. Fass. Caribbean Q. 1988;36:175–177.

<!-- b000319 | furniture | pages [24] -->
Team 52849

<!-- b000320 | furniture | pages [24] -->
MCM/ICM

<!-- b000321 | furniture | pages [24] -->
Page 23 of 31

<!-- b000322 | heading | pages [24] -->
7 Appendix

<!-- b000323 | heading | pages [24] -->
7.1 Algorithmic Water Flow Algorithm

<!-- b000324 | prose | pages [24] -->
from future import division import numpy as np import PIL, time from PIL import Image

<!-- b000325 | prose | pages [24] -->
startTime=time.time()

<!-- b000326 | prose | pages [24] -->
FILENAME=“haitirah.gif” image can be in gif jpeg or png format im=np.asarray(Image.open(FILENAME).convert(’RGB’)) im=Image.open(FILENAME).convert(’RGB’) startMatrix=im.load() w=im.size[0] h=im.size[1]

<!-- b000327 | prose | pages [24] -->
def colorConvert(Tuple):

<!-- b000328 | prose | pages [24] -->
if Tuple==(252,216,144):

<!-- b000329 | prose | pages [24] -->
return 1525 elif Tuple==(255,250,194):

<!-- b000330 | prose | pages [24] -->
return 610 elif Tuple==(130,199,80):

<!-- b000331 | prose | pages [24] -->
return 153 elif Tuple==(255,288,88):

<!-- b000332 | prose | pages [24] -->
return 3050 elif Tuple==(156,220,248):

<!-- b000333 | prose | pages [24] -->
return 0 elif Tuple==(0,0,0):

<!-- b000334 | prose | pages [24] -->
return 150 elif Tuple==(238,16,20):

<!-- b000335 | prose | pages [24] -->
return 610 elif Tuple==(224,231,148):

<!-- b000336 | prose | pages [24] -->
return 305 else:

<!-- b000337 | prose | pages [24] -->
return 1

<!-- b000338 | prose | pages [24] -->
def imageConvert(imageMatrix):

<!-- b000339 | prose | pages [24] -->
newMatrix=[] for i in range(w):

<!-- b000340 | prose | pages [24] -->
newRow=[] for j in range(h):

<!-- b000341 | prose | pages [24] -->
newRow.append(colorConvert(imageMatrix[i,j])) newMatrix.append(newRow) return newMatrix

<!-- b000342 | prose | pages [24, 25] -->
starter=imageConvert(startMatrix) startMat=[] for i in starter:

<!-- b000343 | furniture | pages [25] -->
Team 52849

<!-- b000344 | furniture | pages [25] -->
MCM/ICM

<!-- b000345 | furniture | pages [25] -->
Page 24 of 31

<!-- b000347 | prose | pages [25] -->
newRow=[] for j in i:

<!-- b000348 | prose | pages [25] -->
newRow.append(j) startMat.append(newRow)

<!-- b000349 | prose | pages [25] -->
def changeInHeight(matrix, startI, startJ):

<!-- b000350 | prose | pages [25] -->
coeﬃcient=.01 value=0 value+=matrix[startI+1][startJ]-matrix[startI][startJ] value+=matrix[startI-1][startJ]-matrix[startI][startJ] value+=matrix[startI][startJ+1]-matrix[startI][startJ] value+=matrix[startI][startJ-1]-matrix[startI][startJ] return coeﬃcient*value

<!-- b000351 | prose | pages [25] -->
waterGones=0 #50 km=58 pixels

<!-- b000352 | prose | pages [25] -->
def replenish(start, updaterMat):

<!-- b000353 | prose | pages [25] -->
annualRain=1.4/36 area=(1000*50/58)**2 runoﬀCoeﬃcient=.664*.7+.15*.036+.3*.6 a=len(start) b=len(start[0]) for i in range(a):

<!-- b000354 | prose | pages [25] -->
for j in range(b):

<!-- b000355 | prose | pages [25] -->
if updaterMat[i][j]!=0:

<!-- b000356 | prose | pages [25] -->
updaterMat[i][j]+=area*annualRain*(1-runoﬀCoeﬃcient) return updaterMat

<!-- b000357 | prose | pages [25] -->
def diﬀuse(startMatrix, prevMatrix, counter=False):

<!-- b000358 | prose | pages [25] -->
a=len(startMatrix) b=len(startMatrix[0]) waterGone=0 newMatrix=[] newMatrix.append([0]*b) for i in range(1,a-1):

<!-- b000359 | prose | pages [25] -->
newRow=[0] for j in range(1,b-1):

<!-- b000360 | prose | pages [25] -->
newRow.append(prevMatrix[i][j]+changeInHeight(prevMatrix, i, j)) newRow.append(0) newMatrix.append(newRow) newMatrix.append([0]*b) for i in range(a):

<!-- b000361 | prose | pages [25] -->
for j in range(len(startMatrix[i])):

<!-- b000362 | prose | pages [25] -->
if counter!=False:

<!-- b000363 | prose | pages [25] -->
if startMatrix[i][j]==0:

<!-- b000364 | furniture | pages [26] -->
Team 52849

<!-- b000365 | furniture | pages [26] -->
MCM/ICM

<!-- b000366 | furniture | pages [26] -->
Page 25 of 31

<!-- b000367 | prose | pages [26] -->
waterGone+=newMatrix[i][j] newMatrix[i][j]=0 elif startMatrix[i][j]==0:

<!-- b000368 | prose | pages [26] -->
newMatrix[i][j]=0 return (newMatrix, waterGone)

<!-- b000369 | prose | pages [26] -->
for i in range(36):

<!-- b000370 | prose | pages [26] -->
thing=diﬀuse(starter, startMat, True) startMat=thing[0] waterGones+=thing[1] startMat=replenish(starter, startMat)

<!-- b000371 | prose | pages [26] -->
print(“Time:”, time.time()-startTime) print(“Ocean Loses:”, waterGones)

<!-- b000372 | heading | pages [26] -->
7.2 Particle Swarm

<!-- b000373 | prose | pages [26] -->
from future import division “PSO/RPSO”

<!-- b000374 | prose | pages [26] -->
import math, random, itertools, time

<!-- b000375 | prose | pages [26] -->
Parameters method=’RPSO’ PSO/RPSO start=time.time() rainMax=4.75*10**12 wellMax=4.11*10**7

<!-- b000376 | prose | pages [26] -->
Gen Functions def setSubtract(a,b):

<!-- b000377 | prose | pages [26] -->
c=[ ] for i in a:

<!-- b000378 | prose | pages [26] -->
if i not in b:

<!-- b000379 | prose | pages [26] -->
c.append(i) return c

<!-- b000380 | prose | pages [26] -->
def counter(board):

<!-- b000381 | prose | pages [26] -->
count=0 for i in board:

<!-- b000382 | prose | pages [26] -->
for j in i:

<!-- b000383 | prose | pages [26] -->
if j!=0:

<!-- b000384 | prose | pages [26] -->
count+=1 return count

<!-- b000385 | prose | pages [26] -->
def particlePrinter(List):

<!-- b000386 | prose | pages [26] -->
for i in List:

<!-- b000387 | prose | pages [26, 27] -->
print(i[0],i[1],i[4]) return

<!-- b000388 | furniture | pages [27] -->
Team 52849

<!-- b000389 | furniture | pages [27] -->
MCM/ICM

<!-- b000390 | furniture | pages [27] -->
Page 26 of 31

<!-- b000392 | prose | pages [27] -->
numberVars=3

<!-- b000393 | prose | pages [27] -->
def satisﬁesConstraints(rainWaterCollection, wellWaterCollection,desalination, demand):

<!-- b000394 | prose | pages [27] -->
a=rainWaterCollection+ wellWaterCollection+ desalination if a >demand and rainWaterCollection <rainMax and wellWaterCollection <wellMax and rain- WaterCollection>0 and wellWaterCollection>0 and desalination >0:

<!-- b000395 | prose | pages [27] -->
return 1 else:

<!-- b000396 | prose | pages [27] -->
return 0

<!-- b000397 | prose | pages [27] -->
def equation(rainWaterCollection, wellWaterCollection, desalination):

<!-- b000398 | prose | pages [27] -->
dieselPrice=.97 aveDistance= 50 a=rainWaterCollection+ wellWaterCollection+ desalination collectionCost=(7.2*365*dieselPrice/2400)*wellWaterCollection +5.141*.001*desalination transportationCost=(2.31*(.001**2))*a*aveDistance a/=1000000 puts into MGD treatmentCost=a*1000*((.6/(a+.04))+.7) return treatmentCost+ collectionCost+transportationCost

<!-- b000399 | prose | pages [27] -->
bestParticleConﬁg=[[0, 0, [], [], []]]

<!-- b000400 | prose | pages [27] -->
def bestParticleUpdater():

<!-- b000401 | prose | pages [27] -->
for i in Particles:

<!-- b000402 | prose | pages [27] -->
if i[0]¡bestParticleConﬁg[0][0]:

<!-- b000403 | prose | pages [27] -->
bestParticleConﬁg.pop() bestParticleConﬁg.append(tuple(i)) return

<!-- b000404 | prose | pages [27] -->
def ParticleInitializer():

<!-- b000405 | prose | pages [27] -->
List=[] for i in range(100):

<!-- b000406 | prose | pages [27] -->
a=[] for j in range(numberVars):

<!-- b000407 | prose | pages [27] -->
a.append(random.randint(10**6,10**9)) currentParticleScore=equation(a[0],a[1],a[2]) bestParticleScore=currentParticleScore bestParticlePos=a currentVelocity=[0]*numberVars List.append([currentParticleScore, bestParticleScore, bestParticlePos, currentVelocity, a]) return List

<!-- b000408 | prose | pages [27, 28] -->
Particles=ParticleInitializer() bestParticleConﬁg.pop() bestParticleConﬁg.append(tuple(Particles[0])) bestParticleUpdater()

<!-- b000409 | furniture | pages [28] -->
Team 52849

<!-- b000410 | furniture | pages [28] -->
MCM/ICM

<!-- b000411 | furniture | pages [28] -->
Page 27 of 31

<!-- b000413 | prose | pages [28] -->
def Velocity(Particle):

<!-- b000414 | prose | pages [28] -->
inertialConstant=.7 Constants=[.5, .5] rand1=random.random() rand2=random.random() if method==’PSO’:

<!-- b000415 | prose | pages [28] -->
Constants.append(0) rand3=0 OtherParticle=bestParticleConﬁg elif method==’RPSO’:

<!-- b000416 | prose | pages [28] -->
Constants.append(.5) Constants[1]*=-1 rand3=random.random() OtherParticle=random.choice(Particles) while OtherParticle==Particle:

<!-- b000417 | prose | pages [28] -->
OtherParticle=random.choice(Particles) actualAnswer=[] for i in range(numberVars):

<!-- b000418 | prose | pages [28] -->
actualAnswer.append(inertialConstant*(Particle[3][i]+Constants[0]*rand1*(Particle[2][i]-Particle[4][i])+C Particle[4][i])+Constants[2]*rand3*OtherParticle[3][i])) return actualAnswer

<!-- b000419 | prose | pages [28] -->
def inRange(particle):

<!-- b000420 | prose | pages [28] -->
demand=365*3*10**6 if satisﬁesConstraints(particle[4][0],particle[4][1],particle[4][2], demand)==1:

<!-- b000421 | prose | pages [28] -->
return particle else:

<!-- b000422 | prose | pages [28] -->
x=random.randint(0,2) if particle[4][0]¿rainMax:

<!-- b000423 | prose | pages [28] -->
particle[4][0]=rainMax if particle[4][1]¿wellMax:

<!-- b000424 | prose | pages [28] -->
particle[4][1]=wellMax if particle[4][0]+particle[4][1]+particle[4][2]¡demand:

<!-- b000425 | prose | pages [28] -->
particle[4][0]=rainMax particle[4][1]=wellMax if particle[4][0]+particle[4][1]+particle[4][2]¡demand:

<!-- b000426 | prose | pages [28] -->
if demand-particle[4][0]-particle[4][1]¿0:

<!-- b000427 | prose | pages [28] -->
particle[4][2]=demand-particle[4][0]-particle[4][1] for i in range(3):

<!-- b000428 | prose | pages [28] -->
if particle[4][i]¡0:

<!-- b000429 | prose | pages [28] -->
particle[4][i]=0 return particle

<!-- b000430 | prose | pages [28] -->
def Swarm():

<!-- b000431 | prose | pages [28] -->
for i in Particles:

<!-- b000432 | furniture | pages [29] -->
Team 52849

<!-- b000433 | furniture | pages [29] -->
MCM/ICM

<!-- b000434 | furniture | pages [29] -->
Page 28 of 31

<!-- b000435 | prose | pages [29] -->
if i[0]==0:

<!-- b000436 | prose | pages [29] -->
break vel=Velocity(i) pos=[] for j in range(numberVars):

<!-- b000437 | prose | pages [29] -->
pos.append(i[4][j]+vel[j]) i[3]=vel i[4]=pos i=inRange(i) i[0]=equation(i[4][0],i[4][1],i[4][2]) if i[0]¡i[1]:

<!-- b000438 | prose | pages [29] -->
i[1]=i[0] i[2]=i[4] bestParticleUpdater() return

<!-- b000439 | prose | pages [29] -->
iterations=0

<!-- b000440 | prose | pages [29] -->
while iterations¡10000:

<!-- b000441 | prose | pages [29] -->
Swarm() iterations+=1 if iterations print(iterations)

<!-- b000442 | prose | pages [29] -->
print() particlePrinter(bestParticleConﬁg) print(bestParticleConﬁg)

<!-- b000443 | prose | pages [29] -->
print(“”,time.time()-start)

<!-- b000444 | heading | pages [29] -->
7.3 Agent-Based Model Code: Netlogo

<!-- b000445 | prose | pages [29] -->
extensions [ nw ] breed [ nodes node ] ;; the “common man” breed [ distributors distributor ] breed [ centers center ] breed [ elites elite ] breed [ gangs gang ] links-own [ weight ] turtles-own [ water given demand total-weight] globals [ total-weight-var linear standard theoretical-min] directed-link-breed [active-links active-link]

<!-- b000446 | prose | pages [29, 30] -->
to setup clear-all reset-ticks setup-network ;; give the water to the source depending on the user selected option ask turtles [ set water 0 ] if source = “elite” [ ask elites [ set water water-given set size 1 + 4 * sqrt(water) ] ] if source = “centers” [ ask centers [ set water water-given set size 1 + 4 * sqrt(water) ] ] end

<!-- b000447 | furniture | pages [30] -->
Team 52849

<!-- b000448 | furniture | pages [30] -->
MCM/ICM

<!-- b000449 | furniture | pages [30] -->
Page 29 of 31

<!-- b000451 | prose | pages [30, 31] -->
to setup-network create-nodes number-of-nodes [ ;; don’t put any nodes too close to the edges setxy (random-xcor * 0.8) (random-ycor * 0.8) set color white set water 0 set demand common-demand ] let num-links (avg-degree * number-of-nodes) / 2 while [count links <num-links ] [ ask one-of nodes [ let choice (min-one-of (other nodes with [not link-neighbor? myself]) [distance myself]) if choice != nobody [ create-link-with choice ] ] ] ;; space out nodes repeat 10 [ layout-spring turtles links 0.3 (world-width / (sqrt number-of-nodes)) 1 ] ;; people to people links are moderately strong ask links [ set weight 3 ] create-distributors 3 [ set label “distributor” setxy (random-xcor * 0.8) (random-ycor * 0.8) set color green while [count my-links <8] [ ;; distributor to people links are strong create-link-with one-of nodes with [not link-neighbor? one-of distributors] [ set weight 7 ] ] set demand 0 ] create-centers 1 [ set label “health center” setxy (random-xcor * 0.8) (random-ycor * 0.8) set color red ;; center to distributor links are strong create-links-with distributors [ set weight 7 ] set demand 0 ] create-elites 1 [ set label “elite” setxy (random-xcor * 0.8) (random-ycor * 0.8) set color yellow ;; create links with the people, same avg degree as them, but smaller weightage while [count my-links <avg-degree] [ create-link-with one-of nodes [set weight 0.5] ] set demand elite-demand ] create-gangs 2 [ set label “gang” setxy (random-xcor * 0.8) (random-ycor * 0.8) set color orange ;; links to elite are strong create-links-with elites [ set weight 7 ] ;; links to other gangs are strong create-links-with other gangs [ set weight 7 ] ;; create links with the people, same avg degree as them, but smaller weightage while [ count my-links <avg-degree ] [ create-link-with one-of nodes [set weight 0.5] ] set demand gang-demand ] set-default-shape turtles “circle” end

<!-- b000452 | furniture | pages [31] -->
Team 52849

<!-- b000453 | furniture | pages [31] -->
MCM/ICM

<!-- b000454 | furniture | pages [31] -->
Page 30 of 31

<!-- b000456 | prose | pages [31] -->
to go ﬂow-water tick end

<!-- b000457 | prose | pages [31, 32] -->
to ﬂow-water ask turtles with [ water >0 and given != 1 ] [ let giver self let recipients nw:turtles-in-radius 1 ;; ﬁlters recipients to only those who don’t have the amount of water they need ifelse breed = centers [ ] [ set recipients recipients with [ water ¡ demand ] ] ;; centers can never receive set recipients recipients with [ breed != centers ] ;; people only give to other people, not elite or gangs or distributors if breed = nodes [ set recipients recipients with [ breed = nodes ] ] set total-weight-var 0 ;; ﬁnd the total weighted distance from the giver node to their recipients ask recipients [ set total-weight-var total-weight-var + nw:weighted-distance-to giver “weight” ] set total-weight total-weight-var ;; give recipients a fraction of the giver’s water (after they have taken their demand) dependent upon the weight of their link ask recipients [ if [ water ] of giver >[ demand ] of giver [ set water ( [ water ] of giver - [ demand ] of giver ) * ( nw:weighted- distance-to giver “weight” / [ total-weight ] of giver ) ] ] if water >demand [ set water demand ] set given 1 ] ;; to visually see who has how much water ask turtles [ set size 1 + 4 * sqrt(water) ] ;; measures of centrality set linear 0 set standard 0 ;; ask those who don’t have the amount they need ;; by how much they do not have it ;; for linear, sum these needs ;; for standardized need, add the squares of individual needs and square root at end ask nodes with [ water ¡ demand ] [ set linear linear + ( demand - water ) set standard standard + ( demand - water ) 2 ] set theoretical-min common-demand * number-of-nodes - water-given set linear ( linear - theoretical-min ) / number-of-nodes ;; average need not met per person set standard sqrt(standard) / number-of-nodes ;; average need not met per person, amplifying the need unmet of the person with the maximum need unmet end

<!-- b000458 | furniture | pages [32] -->
Team 52849

<!-- b000459 | furniture | pages [32] -->
MCM/ICM

<!-- b000460 | furniture | pages [32] -->
Page 31 of 31
