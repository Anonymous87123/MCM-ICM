Problem Chosen 2024

MCM/ICM

Summary Sheet

Summary

While having great food and research value, the lamprey has long been a cause for concern because it is an invasive species in some areas. Because of this complexity, it has long been in the spotlight. Is this a gift or a curse? To explore this phenomenon, we modeled the iterative process of lamprey populations and analyzed the effects of adaptive-sex on lamprey populations and the larger ecosystem.

Several models are established: Model I: Lamprey Population Iteration Model; Model II: BDS Assessment Model, etc.

Before all the models are established, based on the special characteristics of lamprey metamorphosis, we divided the lamprey population into two parts: larval and adult bank, so as to simulate the ecosystem with higher simulation. In addition, we collected data and set reasonable parameters through calculation.

For Model I, we established three sub-models to form the Lamprey Population Iter- ation Model. The sub-model i is based on Lotka-Volterra basic model, modiﬁed for the nature of the larval and adult bank, which describes the competition between lamprey and other species in the ecosystem. The sub-model ii is based on bioenergetic theory and establishes the relationship between resource availability and sex ratio. The sub- model iii is based on the cost of reproduction, and establishes the relationship between sex ratio and fertility rate, which serves as a bridge between sub-models i and ii.

• For task 2, we simulated the iteration with and without adaptive sex lamprey population respectively, and adjusted the environmental parameters downward and upward at the two time points for comparative analysis, and the results show that adaptive sex enhances the resilience stability of the population and reduces the resistance stability of the population, for details, see 4.1.3.

• For task 4, we added a reasonably set Correlation Matrix that covers the basic components of the ecosystem. From it, we selected parasites and parasitized ﬁsh for comparative analysis, and the results and conclusions are presented in 4.2.3.

For Model II, we established a complete ecological system assessment model cover- ing Biomass, Diversity and Stability, in which Shannon-Wiener diversity index was introduced to measure the ecosystem’s The Shannon-Wiener diversity index is intro- duced to measure ecosystem diversity, and a new variance-based measure of Stability, S, is introduced. By substituting the results of Model I into Model II, we are able to compare and analyze the effects of adaptive sex on ecosystems in the three dimen- sions.

• For task 3, the results show that adaptive has a positive effect on ecosystem sta- bility, and the optimization rate R reaches 73.3%.

• For task 1, the results showed that adaptive sex promoted Biomass and diversity, but the optimization rate R reached 5.87% and 5.90%, respectively, compared with that of stability.

Finally, weconverted ratio k from adult to larval and the endowment growth rate b0 for sensitivity analysis. The results show the stability of our model is good. Finally, we discussed the strengths and weaknesses of the model and made a conclusion.

1 Introduction

1.1 Problem Background

In the world, the lamprey can be regarded as a "star creature" that has attracted much attention. On one hand, lamprey has long been a favorite food for humans in Europe and Southeast Asia, and even captured the hearts of medieval European aris- tocrats; on the other hand, as a major invasive species in the Great Lakes of North America, it has caused local authorities to struggle to curb its development. Whether you’re a fan or a opponent, there’s no denying that the lamprey is valuable to study because of its unique ecology and adaptive sex.

The picture above shows the ecological appearance of lamprey. Lacking paired ﬁns, adult lampreys have one nostril atop the head and seven gill pores on each side of the head.During the larval period (called ammocoetes),they burrow in silt, mud and detritus, taking up an existence as ﬁlter feeders, collecting detritus, algae, and microor- ganisms. The rate of water moving across the ammocoetes’ feeding apparatus is the lowest recorded in any suspension feeding animal, and they therefore require water rich in nutrients to fulﬁll their nutritional needs [1].As adults, they acquire nutrients by parasitizing other ﬁsh to reach sexual maturity. After spawning is over, all adults die.In addition to double life due to metamorphic development, it is also amazing in its ability to differentiate the sexes according to the environment,also known as adaptive sex ratio variation.

1.2 Restatement of the Problem

Under the above background,in order to explore the value of the ability for a species to alter its sex ratio depending on resource availability, our group will study the ecosystem- population interactions and accomplish the following tasks:

(1) Study the impact on the larger ecological system when the population of lampreys can alter its sex ratio.

(2) Study the advantages and disadvantages to the population of lampreys.

(3) Study the impact on the stability of the ecosystem given the changes in the sex ratios of lampreys.

(4) Research whether an ecosystem with variable sex ratios in the lamprey population offer advantages to others in the ecosystem, such as parasites.

1.3 Literature Review

This issue focuses on the implications of the adaptive sex-ratio of lamprey. In recent years, research on population models for lamprey has focused on both the biological nature of lamprey and suitable basic models.

Biologically, Lamprey differs from the most commonly studied unicellular organ- isms and mammals in three biological properties: metamorphosis, postnatal-death and adaptive-sex. ﬁrst, the development of Lamprey involves a metamorphosis pro- cess. lamprey’s larval are ﬁlter feeders, while adults are parasitic [2].Second, adults die after reproduction, which implies a cycle of peak mortality [3]. Finally, the sex ratio of adults is affected by the growth rate of larval, which is the focus of our study [4].

As for the basic models, the most commonly used models are logistic models, lotka-volterra-like models, and food-web models.It is worth noting that neither the lotka-volterra model with lagged effects and functional reactivity functions [5] nor the food-web model [6] based on energy ﬂow can comprehensively take into account the lamprey’s three biological characteristics, which means we need to improve the basic models.

The advantages and disadvantages of the three basic models are shown below.

1.4 Our Work

Our solution mindmap is shown below.

2 Model Preparation

2.1 Assumptions and Justiﬁcations

• Assumption 1: The time for adult ﬁsh to migrate, lay eggs, die, and hatch into larval is negligible.

Justiﬁcation: Our model calculates in years, so ﬁner time scales will not be con- sidered. The only time we primarily consider is the time it takes for a larval to grow into an adult, which will be counted directly as a yearling after spawning.

• Assumption 2: Sea lampreys die immediately after spawning.

Justiﬁcation: Based on our review of the literature [7], lampreys die after spawn- ing in a short time, so we neglect the time after them ﬁnish spawning.

• Assumption 3: Temperatures are suitable and consistent throughout the year in all areas of the water body.

Justiﬁcation: Temperature plays a considerable role in larval survival, and dis- cussion of lamprey reproduction is only meaningful if temperatures are appro- priate. The assumption of consistent temperatures in all zones was made to sim- plify the model.

• Assumption 4: Suspended organic solid and dissolved oxygen concentration in the water column are not affected by lamprey and are consistent across re- gions.

Justiﬁcation: Lamprey’s large range and the mobility of the water imply that the environmental resources of the watershed are replenishable. Neglecting anthro- pogenic factors, we can assume that both are stable over large time scales. item Assumption 5: Ignoring major natural disasters and human impacts.

Justiﬁcation: Since major natural disasters and human disturbances are difﬁcult to predict, our model does not take them into account.

2.2 Notations

This chapter introduces the symbols and their descriptions mentioned in the article.

Notations

Deﬁnition

l1(t) Number of larval as a function of time l2(t) Number of adult lamprey as a function of time bi(t) The birth rate of the species i di(t) The death rate of the species i Mi(t) Biomass of larval individual i as a function of time µi(t) Biomass growth rate of larval individual i as a function of time r1 The birth rate of the species i r0 The initial birth rate of the species i (without the impact of sex ratio) 1 x Time required for larval to reach adulthood B Total ecosystem biomass D Shannon-Wiener index Wi The average biomass of an individual of species i C The correlation matrix of species among the ecosystem

2.3 Data Collection and Visualization

This article relies on the following table of data sources.

Database names Database website

Royal Society https://royalsocietypublishing.org/doi/full/10.1098/ rspb.2017.0262#d1e751 EDG- ANSL https://catalog.data.gov/dataset/aquatic-nuisance- species-locator1 GLENDA https://catalog.data.gov/dataset/great-lakes- environmental-database-glenda NARS-NLA2007 https://www.epa.gov/national-aquatic-resource- surveys/data-national-aquatic-resource-surveys

• From the Royal Society we obtained raw data on the sex of lamprey samples.

• From EDG we obtained data on the distribution of lamprey in the Great Lakes region.

• From GLENDA we obtained data on the suspended organic solid concentration of Great Lakes water bodies.

• From NARS- NLA2007 we obtained dissolved oxygen concentration data for Great Lakes water bodies.

The following ﬁgure visualizes the distribution data of Great Lakes lamprey(2021).

It can be seen that lamprey are more heavily concentrated in the more nutrient-rich lake areas; in these areas their densities are approximately the same.

3 Model Establishment

3.1 Model I: Lamprey Population Iteration Model

3.1.1 Research on the life cycle of lampreys

Based on the relevant literature, we can understand that the life cycle of lampreys can be divided into approximately two stages. The ﬁrst stage is the larval stage, where adult lampreys migrate from the sea to the river to spawn and hatch as ammocoetes. During the larval stage, these ammocoetes tend to reside in the substrate, with only a single mouth exposed to the surface. This submerged life helps them avoid predators and utilize the organic matter in the substrate. They are ﬁlter feeders, feeding primar- ily on microorganisms suspended in the water, organic particles and organic matter in the substrate. They obtain nutrients by ﬁltering through most of the small gill slits near the mouth. The length of their larval growth period varies among lampreys, with the average length of the larval stage being about 4 to 6 years. After the end of the larval stage, the young ﬁsh will undergo a metamorphosis and grow into a new form that is completely different from the previous one. In the adult stage, the lamprey, as a parasitic ﬁsh, mainly feeds on the body ﬂuids or blood of other ﬁsh, which is very different from the larval stage. Because of the different living environments, biomor- phology, and ecological niches, we can divide the lamprey population into two parts, larval and adult, and model the population for each of the two parts. [8]

The model mindmap is shown below.

3.1.2 Larval versus adult ﬁsh banking

Based on the description just given, we innovatively divided the lamprey popu- lation into two parts, larval and adult, and each part was calculated separately for indicators such as its birth and death rates. The number of larval can be calculated as follows:

∑ li l1(t) = 1(t) (1) i where li 1(t) is the number of larval aged i year(s) as a function of time.

The number of adult ﬁsh is equal to:

(t) + lfemale l2(t) = lmale (t) (2) 2 2

(t) is the number of male adult ﬁsh and lfemale where lmale (t) is the number of female 2 2 adult ﬁsh.

Interestingly, when we divide the lamprey population into these two parts, we can no longer describe it using the simple Lotka-Volterra model, but have to make a simple modiﬁcation to it.

The formula for the Lotka-Volterra model with multiple population interactions is as follows: n ∑ dli lj dt = rili(1 + aij ) (3) Kj j=1

where ri refers to the endowment growth rate of species i, aij refers to the intrinsic relationship between species i and species j, which is usually described by a correlation matrix, and Ki refers to species i’s environmental carrying capacity.

It is worth noting that in our model, larval and adult ﬁsh are interchangeable. lar- val grow into adults after metamorphosis, while adults die after mating and spawning, which can be viewed as converting into larval, and thus the two, the larval and adult pools, are in an interchangeable relationship. Therefore, we cannot directly decom- pose these two components into two species for calculation, because we cannot use the number of larval themselves to portray the birth rate of larval alone, nor can we use the number of adults to portray the birth rate of adults alone. Therefore, we split the equation of the Lotka-Volterra model into two parts, with the ﬁrst half representing the birth rate of a species and the second half representing the mortality rate of a species.

n ∑ dli lj dt = bi + di = rili + rili aij (4) Kj j=1

where the ﬁrst half of the equation represents the birth rate of the species, inscribed in terms of the endowment growth rate, while the second half represents the death rate of the species, described in terms of the interrelationships between the species.

In our model, we ﬁnd that the relationship between the larval and adult pools is very special: while the birth rate of the adult pool should originate from the larval pool, the birth rate of the larval pool originates from the adult pool. However, the mortality rates of both are derived from themselves. Therefore, we need to modify the formula, i.e., the birth rate of the larval pool is calculated through the number of adult pools, and the birth rate of the adult pool needs to be calculated through the number of larval growing into adults. In order to simplify the model calculation, we portray the population in terms of years, and consider the growth rate of the population as the ﬁrst-order difference of the population size, we can get the growth rate of the larval and adult pools respectively as follows:

n ∑ ∑ dl1 lj dt = l1(t + 1) −l1(t) = kl2(t)r1 + r0 − 1l1(t) a1j si + σ1(t) (5) Kj j=1 i n ∑ ∑ dl2 lj si + r0 dt = l2(t + 1) −l2(t) = −2r1l2(t) + σ2(t) 1l2(t) a2j (6) Kj i j=1 where ∑ si represents the number of larval converted to adults at all ages, and s should i obey a binomial distribution, which will be given later. σ1 and σ2 represents a random perturbation.

3.1.3 Measurement of growth rate in larval

From the literature [2], we know that lamprey larval are ﬁlter feeders. Based on the basic bioenergetic growth model, we can get the biomass growth rate of an individual:

µi(t) = dMi(t) = aM b i (t) (7) dt

where W is the individual biomass and a depends on food concentration (C), assimila- tion efﬁciency (AE) and metabolic cost (Rg/G).b is related to the ﬁltration rate of ﬁlter feeders and can be considered as a constant value 3/4 [9] for larval lamprey,a stationary ﬁlter-feeding population.

We wish to highlight the effect of resource availability on the growth rate of lar- val, so next we will simplify the reality of the situation by establishing a relationship between a and resource availability.

As shown in the ﬁgure, we equate the body of water to a rectangular body. lar- val exchange energy with the outside world through holes located on the surface of the riverbed. According to Assumption 4, the resource available to all larval within this water body is inversely proportional to the density of larval, i.e., the size of the population. We obtain the formula as follows:

l1S|individualResource|individual = S|areaResource|area (8) The main food source for ﬁlter feeders is the suspended organic solid in the water, and the amount of dissolved oxygen affects the assimilation efﬁciency. Characterizing the concentration of both, the equation can be obtained as follows

Os a = γ1 arctan(γ2Do) (9) l1

where γ1 is the ﬁltration rate factor and γ2 is the assimilation efﬁciency factor; Os is the suspended organic solid concentration and Do is the dissolved oxygen concentra- tion; and the arctan function is an approximate ﬁt of aerobic respiration efﬁciency to available oxygen. Combining Eq(7), we obtained the differential biomass system of equations for lamprey larval:

{ 3 dMi(t) Os = γ1 l1 arctan(γ2Do)M i (t) 4 dt Mi(0) = M0

where M0 is the fertilized egg biomass.Solving the above equation gives the relation- ship between individual larval biomass(M) and growth time(τ) ∫τ Mi(t) = M0 + µi(t) dτ (10) 0

For metamorphic organisms, reaching a sufﬁcient biomass is a critical point for quali- tative change. Based on probability theory, it is approximated that the probability of a larval starting to metamorphose(P|grown−up) follows a normal distribution:

1 2πσe−(M−Mb)2 √ P|grown−up = (11) 2σ2

where Mb is the baseline biomass for metamorphosis. When a larval larval begins to metamorphose and develop, according to assumption 1 we consider that it transforms into an adult ﬁsh and note that at this time

x = τ|grown−up (12)

Inverse mapping of Mb M−1 (t) i −→xb Mb (13)

Obviously we were able to get x ∼N(xb, σ2) (14)

3.1.4 Effects between growth rate, sex ratio and birth rate

The sex ratio of lamprey larval is directly determined by their growth rate. [10] The probability of a larval transforming into an adult male(P) can be calculated by the following formula:

P = 1 −eα+βx (15)

Where α and β are coefﬁcients and x represents the year of growth of larval. β < 0.

From the formula, we can see that when the year of growth of larval is longer, the probability of their transformation into males is higher, while when the year of growth of larval is shorter, the probability of their transformation into females is higher. This conclusion is consistent with the current state of the study, in which the more deprived the growing conditions, the slower the growth rate of larval and the longer the time required for growth, the higher the probability of becoming male. This characteristic may enable lamprey populations to adapt to the ecological environment faster, and when the ecosystem is damaged, lamprey populations can adjust the sex ratio to re- duce the birth rate, so that the population can reach a new equilibrium point faster.

Next, we will describe the effect of sex ratio on the birth rate of the population through an equation. Although the lamprey population is monogamous [7], its op- timal sex ratio is most likely not 1:1 as it autonomously adjusts its sex ratio when it encounters environmental changes [11]. According to the literature reviewed, ﬁsh tend to have more females spawning and females require more energy to spawn than males to sperm, with a very large number of egg cells not actually being fertilized. Thus when environmental capacity declines, ﬁsh may need more males to reduce the energy overhead and enhance egg fertilization, so the appropriate sex ratio is shifted in a male-biased direction. Conversely, when environmental accommodation rises, more energy is available to the ﬁsh, and they may tend to lay more eggs to increase the over- all rate of population development more quickly. [12] Based on the above theory, we have ﬁtted a relatively reasonable function to describe the relationship between sex ratio and birth rate in a population.

r0 1 r1 = (16) 1 + ln2 lfemale (l1+l2) 2 lmale (K1+K2) 2

3.2 Model II: BDS Assessment Model

In order to determine how the ecosystem is affected by the change of the sex ratio of the seven-gill eel, we established a BDS Evaluation Model using the total ecosystem biomass, ecosystem species diversity, and ecosystem stability as the evaluation criteria. The idea of modeling is shown below:

3.2.1 Total Ecosystem Biomass

Total ecosystem biomass is one of the most important indicators of ecosystems, which can reﬂect the development of biomes in ecosystems. Suppose there are n species in the ecosystem, where the population density of the ith species is li and the biomass of that species is si The formula for calculating total ecosystem biomass B is as follows: n n ∑ ∑ B = si = liWi (17) i=1 i=1

3.2.2 Shannon-Wiener Diversity Index

Evaluating species diversity is an indispensable step in assessing ecosystem con- dition. Generally speaking, the higher the species richness, the more balanced the biomass among species, and the better the ecosystem condition.

Therefore, we apply the Shannon-Wiener diversity index to consider the species richness and evenness, which is derived from the "entropy" in physics, the higher the species diversity, the greater the degree of disorder, and the higher the value of "en- tropy", the greater the index will be. [13] The higher the value of "entropy", the larger the index will be, and the Shannon-Wiener index D is deﬁned as:

n ∑ D = − pi ln pi (18) i=1 where pi = si B, representing the proportion of the biomass of species i in ecosystem.

3.2.3 Ecosystem Stability Assessment

Stability is one of the necessary conditions for maintaining the normal function- ing of an ecosystem. When the external environment changes, the internal biomass distribution within the ecosystem will also undergo changes through the interactions and regulations among species. In this case, ecosystems with more species and com- plex food webs can adjust their structure and function more quickly, and the resulting changes in biomass distribution tend to be relatively stable. Therefore, in this model, we evaluate the stability of an ecosystem by analyzing the changes in the proportion of biomass for each species in response to external environmental changes.

Based on the Lamprey Population Iteration Model mentioned earlier, we simulate changes in the external environment by altering the food supply in the ecosystem. When the food remains constant and the population sizes of various species reach a sta- ble point, we change the food supply condition and record the changes in the biomass proportions of each species in subsequent years. The calculation for the stability index is as follows: n m ∑ ∑ (pi −pij)2 S = 1 (19) n m i=1 j=1 Here, S represents the stability index after adjusting the food supply to the correspond- ing value, and pij is the proportion of biomass for species i after j years of change.

The smaller the value of S, the smaller the relative change in biomass proportions of various species after adjusting the food supply for n years, indicating a stronger stability of the ecosystem.

4 Modeling Applications and Problem Solving

4.1 Simulation of the Lamprey Population Iteration Model

4.1.1 Algorithm of the Model

Our model performs calculations in a differential form, with the results of each calculation derived from the previous one, to simulate iterations of the lamprey popu- lation based on the input parameters and to investigate whether it is able to maintain stability over time.

Algorithm 1 Lamprey Population Iteration Simulation

Input:

The maximum iterations, G Initial amount of larval ﬁsh l1 Initial amount of adult male ﬁsh lmale 2 Initial amount of adult female ﬁsh lfemale 2 Output:

Larval ﬁsh amount in G year(s) l1 Adult ﬁsh amount in G year(s) l2 Total amount in G year(s) l Gender ratio in G year(s) gk 1: for i ←1 : G do Calculate the decrease amount of lmale 2: 2 Calculate the decrease amount of lfemale 3: 2 b0 b ← 4: (1+ln2 lfemale (l1+l2) 2 ) lmale K 2 + lfemale mate ←round((lmale )b + rand()) 5: 2 2 lmale = lmale −mate 6: 2 2 lfemale = lfemale −mate 7: 2 2 for j ←1 : 100 do 8:

Calculate the decrease amount of lj 9: 1 Calculate the amount of ﬁsh that grows into adulthood change 10:

p ←1 −pow2(α + βj) 11:

male ←round(change ∗p + rand()) 12:

lmale = lmale + male 13: 2 2 lfemale = lfemale + change −male 14: 2 2 end for 15:

for j ←99 : −1 : 1 do 16:

lj+1 = lj 17: 1 1 end for 18:

l1(i) ←sum(l1) 19:

+ lfemale l2(i) ←lmale 20: 2 2 l(i) ←l1(i) + l2(i) 21:

gk(i) ←lmale 2 22: l2(i) 23: end for

4.1.2 Model Parameter Settings

First, all the formulas in the model will be shown below:

 n∑ Kj −∑  lj dl1 dt = kl2(t)r1 + r0  1l1(t) a1j si + σ1(t)    j=1 i   dt = ∑ n∑   lj dl2 si + r0  Kj −2r1l2(t) + σ2(t) 1l2(t) a2j  i j=1 (20) r0  r1 = 1   1+ln2 lfemale  (l1+l2) 2   lmale (K1+K2)  2  P = 1 −eα+βx    x ∼N(xb, σ2)

Using Great Lakes’ data as a reference,we set some of the parameters in the model to appropriate values and adjusted them to see how the model performs with different parameters. Eventually, we determined the model parameters to the following values and used the model to solve the results.

It is worth noting that our model is highly adaptive and does not apply only to the Great Lakes region. When the model is migrated to other regions, local data are needed to support it.

Parameter Value Parameter Value

k α 5 0 −ln 2 r0 β 0.05 1 5 σ2 K2 2 10000 Os Do 45 8 γ1 γ2 168.05 1.50

4.1.3 Result of the Simulation

We input G = 500, l1 = 6000 (1,000 lampreys each from one to six years old), = 5000, lfemale lmale = 5000. 2 2 In order to obtain the advantages and disadvantages of the sex ratio adjustment mechanism for the lamprey population, We adjust Os downward to 50% of the origi- nal value(22.5) and the environmental capacity K2 to same 50% of the original value (5,000) at the 100th year, and then adjusted Os, K2 to the initial value at the 300th year to observe the population evolution. At the same time, we set up a control group, canceled the sex ratio adjustment mechanism, i.e., the probability of larval transform- ing into females and males at any time was the same, and other parameters remained unchanged, simulated the population evolution, and observed the pattern of the evo- lution of the two populations against each other. The simulation results are shown below.

In order to see the differences between the experimental and control groups more clearly, we plotted the population size of the experimental and control lamprey pop- ulations in a single graph and extended G to 1000, with the rest of the conditions un- changed, and the results are shown below.

Lamprey Population Iteration

Lamprey Population Iteration Model (With Operational Sex Ratio) Model (Without Operational Sex Ratio)

We can see from the ﬁgure that:

• In the 100th year, there is a sudden change in the environment and the environ- mental capacity drops to half of its original size, and in the following period of time both populations decline, but the one with the sex-ratio regulation mecha- nism declines faster and is able to reach a new equilibrium in a shorter period of time.

• In the 300th year, the environment changed for the better and the environmental holding capacity returned to its initial state. After that, both populations rose, but it was clear that the sex-ratio-regulated population rose much faster and was slightly more numerous than the other group after recovery.

To quantify the advantages, we deﬁne an optimization rate formula:

R = kbefore −1 (21) kafter

where kbefore represents the metrics before optimization and kafter represents the metrics after optimization. kbefore ≥kafter. From the experimental data we can get that the optimization rate R=202% when K decreases and R=288% when K restores. The optimization effect is quite good.

Through this model, we can give an answer to the question 2.

• The sex-ratio regulation mechanism of lamprey populations enables the entire population to better adapt to new environments, and the population is more re- silient and able to quickly adapt to complex and changing environments.This is also likely what led to the lamprey population’s emergence as an invasive species in the vicinity of the Great Lakes. [14]

• However, this mechanism has some negative consequences in that the popula- tion’s resistance to harsh environments may be reduced. When the environment is very poor, lamprey populations may be endangered for a time.

4.2 Simulation of Ecological System Assessment Model

4.2.1 Lamprey sex ratio and ecosystem stability

As we noted above, lamprey larvae grow at different rates under different food conditions, and the growth rate of larvae determines their probability of differentiat- ing into males or females. Therefore, the effects of ecosystem changes on lamprey are different from those on other populations. Here, we still discuss larval and adults sep- arately, and use the Ecosystem stability assessment model developed above to analyze the relationship between changes in sex ratio and ecosystem stability.

First, we simpliﬁed it after carefully examining the biotope relationships of the ecosystem in which lamprey are found. Four base species were added. The relation- ship between the four species and adult larval is shown below:

• c1 larval lamprey

• c2 Adult lamprey

• c3 Predator of adult lamprey (Species 1)

• c4 Competitor of adult lamprey (Species 2)

• c5 Fish-1 parasitized by adults and capturing larvae (Species 3)

• c6 Fish-2 parasitized by adults and capturing larvae (Species 4) After this, we introduced a correlation matrix to describe the interrelationships be- tween species in the ecosystem, which is expressed as follows:

  −1 · · · a12 a13 a1n   −1 · · · a21 a23 a2n −1 · · · a31 a32 a3n C = (22) ... ... ... ... ...

· · · −1 an1 an2 an3

where aij represents the coefﬁcient of inﬂuence of cj on ci (i̸ = j), with an inﬂuence coefﬁcient between -1 and 1. When aij = 0, there is no direct impact between the two species. Conversely, a positive impact coefﬁcient represents a favorable impact of cj on ci survival, and a negative impact coefﬁcient represents a negative impact of cj on ci survival. A larger |aij| represents a larger effect.

With the known interrelationships between the species, based on the Lamprey Pop- ulation Iteration Model, we were able to calculate the population densities x3, x4, x5, x6 for c3, c4, c5, c6. The calculation formula is shown in Eq.3.

The biomass of each population is obtained by multiplying the population density of that ecosystem species by the average weight of individuals in each population.

Next, based on the relevant data we have collected, we give the weight matrix W = [0.69, 3.7, 40.3, 1.2, 15.8, 14.0], and the value of C is shown in the heatmap below.

Simulations were carried out under two scenarios, one with a change in the sex ratio of lampreys and one without, and when the population biomass in both scenarios stabilized, the food supply of the ecosystem was changed so that the environmental capacity decreased, and then the food supply of the ecosystem was changed to the initial food supply after the population biomass in both scenarios had stabilized again. From this, we were able to draw a graph of the changes in the biomass of the various populations in the ecosystem under different scenarios:

Substituting the results into the Ecosystem Stability Assessment Model and taking m = 100, we get Indicators of ecosystem stability S1 = 3.7175 · 10−4 for lamprey with change in sex ratio; Indicators of ecosystem stability S2 = 6.4414 · 10−4 for lamprey without change in sex ratio in 100 years after the ﬁrst modiﬁcation of K from 100th to 200th year. Since S1 is smaller than S2, we can get the conclusion of question 3, when there is a change in the sex ratio of lamprey, the ecosystem can adjust its own structure and function more quickly and the biomass distribution is more stable, i.e., the ecosystem stability is better. The optimization rate of ecosystem stability by the sex ratio adjustment mechanism was calculated to be R = 73.3%.

4.2.2 In-depth Assessment of Impacts on Ecosystem

In order to obtain more aspects of the effects of sex ratio regulation mechanisms on ecosystems, we calculated the total biomass and Shannon-Wiener Index for each year of the model in the previous section as a way to obtain optimization rates of B and Model (With Operational Sex Ratio) Model (Without Operational Sex Ratio)

(With Operational Sex Ratio) (Without Operational Sex Ratio)

D for an ecosystem. Keeping the model parameters constant, the effects of lamprey populations on the ecosystem were simulated with and without the sex ratio regulation mechanism. The results are shown below.

Since we need to study the effect of the sex ratio regulation mechanism when the environmental holding capacity of the ecosystem is changed, in order to amplify the effect, we chose the 300th to the 400th year for analysis. The mean value of ecosys- tem biomass and the mean value of Shannon-Wiener Index are calculated for this pe- riod of time, and by comparison we can ﬁnd that the biomass of ecosystems with sex- regulation mechanisms is 3.7117 · 105, and the Shannon-Wiener Index is 1.4588; while the two indexes of ecosystems without sex-regulation mechanisms are 3.5059 · 105, and 1.3775, respectively.

At this point, we can answer question 1.

• After calculation, the optimization rate of ecosystem biomass for the sex ratio reg- ulation mechanism was R = 5.87% and the optimization rate of Shannon-Wiener Index was R = 5.90%. The optimization rate is not signiﬁcant.

• From the ﬁgure, we can see that the ecosystems with sex ratio regulation mech- anism have a slightly shorter time to re-establish equilibrium when the environ- mental holding capacity is changed.

• This may be due to the fact that the effect of sex ratio on the lamprey population is partially masked by its overall optimization effect when it is scaled up to the ecosystem due to the interactions of a very large number of other species. Com- bining the result in question 3, however, it can still serve to accelerate ecosystem regulation.

4.2.3 Detailed Impacts on Other Species

In the previous chapter, we explored the macroscopic effects of the sex ratio regula- tion mechanism on the ecosystem as a whole, and this chapter will focus on analyzing the effects of this mechanism on different species in the ecosystem. We analyzed the effects of this mechanism on ﬁsh parasites and lamprey parasitic species of the same status as lampreys. Keeping other parameters constant, the ecosystem was simulated and the changes in population density of the above species with and without the sex ratio regulation mechanism were plotted.

First we analyze the changes in parasites (Species 2). Because the sex ratio mech- anism can increase the resilience of lamprey populations, when the ecosystem envi- ronment improves, lamprey populations will reach a new equilibrium point faster and take over the resources of other organisms, resulting in the suppression of parasites competing with them. As a result, Species 2 will recover and equilibrate with slightly fewer species than an ecosystem without sex ratio regulation.

The effects on lamprey hosts were analyzed next. We set Species 3 to be more com- petitive relative to Species 4, so Species 3 would be more affected by lampreys. After the experiment, we found that due to the sex ratio regulation mechanism of lampreys, the population density of Species 3 became smaller, while the population density of Species 4 increased instead, suggesting that this mechanism prompted the reproduc- tion of the lamprey population, which caused Species 3 to be suppressed more, and thus brought more room for Species 4 to survive.

At this point, we can answer question 4.

• The sex ratio regulation mechanism of the lamprey population affects changes in its own population density while also affecting other organisms in the ecosystem.

• For the lamprey’s competitors (other ﬁsh parasites), it will make the survival of these competitors are suppressed, so it is not conducive to the survival of these competitors.

• For the lamprey parasitic hosts, it will be a better balance of the whole ecosystem of the size of the population density, which is conducive to the coordination and alleviation of the competitive relationship between the different species.

5 Model Evaluation and Discussion

5.1 Sensitivity Analysis

In this article, we have developed two models: the Lamprey Population Iteration Model and the Ecological System Assessment Model, and we focus on the former in our sensitivity analysis. In our model, there are many parameters that need to be given by human, and most of them have been simulated to obtain appropriate values. How- ever, there are still some parameters that may vary in real situations. For example, the conversion ratio k from adult to larval and the endowment growth rate b0 may ﬂuctuate within a small range by environmental factors, so we change k and b0 respec- tively, and other parameters remain unchanged, and re-simulate the lamprey popula- tion model in 5.1, and observe the results of the model calculations.

First, we set the value of k to 4.5, 5 and 5.5 to simulate the slight ﬂuctuation of spawning rate and survival rate in the population; then we adjusted b0 to 0.04, 0.05 and 0.06 to simulate the ﬂuctuation of endowment growth rate in the population, and observed the changes in the number of lampreys in the population and the proportion of the sexes. The results showed that when k and b0 ﬂuctuated within a certain range, the population size and sex ratio did not change greatly, and the trend was basically consistent, indicating that the stability of the model was good.

In fact, we also did a sensitivity analysis of the effects of k and b0 on indicators such as total biomass under the multiple population model. However, due to the complex- ity of the interactions between different species in the multiple population model, the indicators of lamprey population do not signiﬁcantly affect the total biomass of the whole ecosystem in the case of a small ﬂuctuation, therefore, to save space, the sensi- tivity analysis graphs of the multiple population model were not listed. Overall, the model is stable enough to be applied in real-world scenarios.

5.2 Strengths and Weaknesses

5.2.1 Strengths

• The growth habit of lampreys was considered. We have reviewed many related literatures to fully understand the development and metamorphosis process of lamprey in depth. The body size, living environment and food source of lamprey larval and adults are very different, so our model divides lampreys into larval and adult pools, which makes the model more relevant to the current situation.

• The life cycle of lampreys was taken into account. Adult lampreys will die di- rectly after spawning, which is different from the common Lotka-Volterra, so we divided the larval and adult lampreys into two parts to be considered separately, and the larval lampreys originated from the adult lampreys and the adult lam- preys originated from the larval lampreys, which formed a cycle and made the model more in line with the reality.

• When the model is calculated, we assign each larval a label of growth year and weight, and each larval is calculated separately for its maturity time. This makes the model calculations more accurate and more convincing.

• The parameter indicators of the model were determined by reviewing relevant literature and extensive experiments. Our model indicators are not given by hu- man, but more accurate calculation parameters based on relevant data and sim- ulation experiments, which makes the model more stable and precise.

• Multi-dimensional indicators are used to assess the ecological environment. We adopt Biomass, Shannon-Wiener Index, Stability Index to evaluate an ecological environment comprehensively. The multidimensional evaluation can reﬂect the impact of lamprey population on the whole ecosystem more comprehensively.

5.2.2 Weaknesses

• As there is less literature related to the sex ratio regulation mechanism of lam- prey, the formulas of our model in terms of sex ratio regulation are given by ourselves based on the relevant data reviewed, which may have some deviation from the reality.

• When we modeled ecosystems with multiple populations, we generalized some species into uniform species, such as predators of lampreys, parasitic hosts of lampreys, and so on. The reality may be more complex than our modeling, as there are often thousands of species in an ecosystem.

• We ﬁxed the environmental factors of the ecosystem for our calculations, but in reality these metrics also change over time. However, our model iteration time is in years, so stability is guaranteed.

5.3 Conclusion

The mechanism of sex ratio regulation in lampreys is also a very complex issue in biology. So far it is inconclusive, and it may take more and longer to get to a good explanation of the laws embedded in it.The earth is inclusive, life is marvelous, the ex- istence of each species must have its meaning, and there are still many secrets waiting to be unveiled by human beings. We hope that our model can provide some help for the further study of the lamprey species, and we also hope that readers can give us some suggestions to improve our model.
