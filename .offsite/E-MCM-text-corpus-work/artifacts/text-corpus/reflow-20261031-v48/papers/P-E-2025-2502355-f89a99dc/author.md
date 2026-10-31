MCM/ICM

Summary Sheet

Summary

Forests, often referred to as the "lungs of the Earth" and home to countless species, have been increasingly deforested in recent years. The cleared forests become converted forest areas, raising a critical challenge: how can we best utilize this land for sustainable purposes?

For Problem 1, we mainly employ differential equations and develop the equations pro- gressively. We begin by constructing a simple food chain model, gradually advancing to a more complex food web model. This includes the introduction of pesticide and herbicide, followed by the incorporation of agriculture cycle and its seasonality into the model. The final model

considers various factors such as temperature, fertilization, and the periodic application of pesticides and herbicides. By using numerical simulating the dynamics of the food web over the course of one year, we analyze the biomass changes of the species involved. As shown in Figure 9, the impact of agricultural cycles and seasonality on the system: Crop-like producers, grass-like producers, and primary consumers undergo periodic oscillations in response to the periodic application of pesticides and herbicides.

For Problem 2, a network is established using graph theory, with populations as nodes. The carbon flow, calculated based on the biomass from the equilibrium simulations in Problem 1, serves as the arc weight. Different network scenarios are constructed by sequentially incor- porating factors such as the reemergence of two species, the application of pesticides and herb- icides, and the inclusion of bats and bees. The stability, biodiversity, and centrality indicators of the network are then evaluated and assessed, providing a comprehensive understanding of the system's dynamics. Bats (29.29) and Bees (43.37) both result in greater stability, with the removal of pesticides and herbicides and doing nothing yielding a stability of 56.99.

For Problem 3, we propose three specific measures to achieve organic farming: improving soil nutrients, pest management, and regular manual weeding. These measures are tested in pairs, all three combined, and a blank control solution. We evaluate their effectiveness by nu- merically simulating the differential equations from Problem 1 to determine the stable bio- mass of each species under each solution. Using data from the differential equations, calculated metrics, and expert evaluations, we analyze economic, ecological, sustainability, and social benefits. An EWM-AHP model is developed to assess these schemes for organic farming. Based on the results, we recommend the optimal solution for farmers: improving soil condi- tions combined with regular manual weeding.

Finally, a sensitivity analysis of the herbicide power (alpha value) in our Problem 1 food web model shows that the selected alpha value is reasonable and appropriate for the simulation. Based on the ranking results of the methods combination for organic farming, we drafted a one- page letter offering clear and practical suggestions for farmers looking to transition to organic farming. These suggestions carefully balance economic trade-offs with sustainability consid- erations, ensuring that the advice is both actionable and aligned with long-term ecological and economic goals.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

1 Introduction

1.1 Problem Background

Forests, as the largest living entities on Earth, function like living, breathing organisms. They are not only a rich reservoir of plant and animal resources but also serve as the core engine of the Earth’s ecological balance, holding immense potential for sustainable development. 微信公众号：数学模型 However, due to the demands of human progress and extensive agricultural practices, along with insufficient awareness of sustainability, vast areas of forests have been repurposed, lead- ing to severe ecological degradation.

Taking the Amazon Rainforest, often referred to as the "lungs of the Earth," as an example, it has suffered significant deforestation and forest fires since the 20th century, resulting in a loss of approximately 20% of its area. This loss has caused profound impacts on its ecological environment. However, forest degradation is not inevitable. With societal transformation, the possibility of achieving a harmonious coexistence between agriculture and forest ecosystems remains. Therefore, investigating how to balance sustainability and cost-effectiveness in post- 微信号：MATHmodels conversion forest ecosystems has become an urgent issue that needs to be addressed.

1.2 Restatement of the Problem

Considering the background information and restricted conditions identified in the prob- lem statement, we need to solve the following problems:

For Problem 1, develop a model for the converted forest area, including producers and consumers, and considering the impact of agricultural cycles and seasonal variations on eco- system dynamics. Also, account for the changes on herbicides and pesticides on plants, insects, and birds.

For Problem 2, we need to develop a comprehensive assessment model that considers both the overall stability of the ecosystem and the individual changes of species. Using this model, we can examine the impacts of the reemergence of two species, the removal of herbicides, and the introduction of bats and other species.

Problem 3 requires proposing several combinations of organic farming methods and eval- uating their impact on factors such as pest management, plant vitality, reproduction processes, ecosystem diversity, long-term viability, and economic feasibility.

Problem 4, We need to write a one-page letter advising a farmer on organic farming meth- ods while balancing costs and sustainability, and recommending policies to promote agricul- tural conservation.

1.3 Our Work

To avoid complicated description, intuitively reflect our work process, the flow chart is show as the following Figure 2:

2 Assumptions and Justifications

To simplify the problem, we make the following basic assumptions, each of which is properly justified.

 Assumption1: The population dynamics of specific species in the agricultural eco- system can be simplified to the changes in biomass at various trophic levels. Justification: Agricultural ecosystems are highly homogenized, with species popula- tions at each trophic level being relatively similar. Abstracting specific species into trophic level biomass is conducive to improving the universality of the model.

 Assumption2: The pesticide we use are broad-spectrum and have a certain extermi- nating effect on all insects. Justification: Pesticides have an eradication effect on the majority of insect popula- tions, and insects in agricultural ecosystems are typically common species. Therefore, it can be assumed that the pesticide exerts a certain level of lethal effect on all insect popula- tions.

 Assumption 3: The herbicide used is assumed to affect only grass-like producers. Justification: While herbicides contain toxic substances that inevitably affect various producers, there are physiological and genetic differences between them, which allow herb- icides to selectively target weeds. We assume the herbicide has minimal impact on crop- like producers, and this can be reasonably neglected.

 Assumption 4: Farmers complete their agricultural tasks in a negligible period.

关注数学模型

Justification: The chosen agricultural ecosystem model represents a small, typical

sample, where the biomass of crop-like producers is relatively low. As a result, farmers can complete tasks such as spraying herbicides, pesticides, and applying fertilizers in a short period, which can be approximated as one unit of time. 微信公众号：数学模型

 Assumption 5: Decomposers only decompose producers and soil nutrients. Justification: Decomposers mainly decompose producers and soil because producers provide directly abundant organic matter, while consumer carcasses decompose slowly and indirectly. Moreover, after consumer death, their carcasses enter the soil, and decomposers indirectly act through the material and energy exchange with the soil.

3 Notations and Data

The key mathematical notations used in this paper are listed in Table 1.

微信号：MATHmodels

Symbol

Description Unit 2 g cm− Carbon biomass of producers ⋅ X Carbon biomass of primary consumers (including animals like 2 g cm− ⋅ Y insects, rabbits) Carbon biomass of secondary consumers (including birds, 2 g cm− ⋅ Z foxes) X 2 g cm− ⋅ Carbon biomass of crop-like producers 1 X 2 g cm− Carbon biomass of grass-like producers ⋅ 2 2 g cm− Carbon biomass of decomposers ⋅ D 2 S g cm− Carbon biomass of soil nutrients ⋅ Temperature T C  t Time /

 Note: Some variables are not listed. Their specific meanings will be introduced below.

 Note: All our initial data are sourced from research papers.[2][7]

4 Problem 1: Agricultural Ecosystem Based on Differential Equa-

tion

4.1 Problem analysis

In Problem 1, we are required to develop a model for a new agricultural area that includes various creatures, species interactions, and human factors. To accomplish this, we begin with a food chain model consisting of only three trophic levels. Building upon this, we expand to a food web model that incorporates decomposers and soil components. Finally, we take into ac- count the effects of seasonal agricultural cycles. The final model, a food web model considering agricultural cycles, achieves the goal.

Model preparation

Specific Biomass colonies

Model 1: Dynamic Model of Tri-trophic Food Chain X Y Z Carbon biomass of Carbon biomass of Carbon biomass of producers secondary consumers primary consumers

crop-like grass-like

Model 2: Dynamic Model of Food Web X1 X2 D Z Carbon biomass of Carbon blomass of Carbon biomass of Carbon biomass of Carbon biomass of Carbon biomass of crop-tike secondary grass-like decomposers primary consumers soll nutrients producers producers consumers only both only pseticide herbicide

Food Web Model Considering Agricultural Cycles Model 3:

the growing season the fallow season cycle (April to October) (October to next April) Nutrient Return Weeding Harvesting Temperature Chemicals Fertilization After Harvest X1X2 XX2 X2Y X1 S

4.2 Model preparation

We investigate agricultural ecosystems and, based on our findings, identify typical exam- ples of organisms at different trophic levels. Agricultural systems, especially in intensively managed farms, tend to have relatively homogeneous populations at each trophic level due to the standardized management practices. For instance, the producers are more likely to be crops and grass This makes the substitution of biomass for specific species valid, as the diversity within trophic levels is often lower compared to natural ecosystems. To make our model more gener- alized and applicable across various agricultural ecosystems, we replace specific colonies with biomass, which allows us to account for the carbon flow in a more abstract way. We analyze several agricultural systems and other artificial ecosystems, and after processing the data, we calculate the average biomass at each trophic level.

4.3 Model 1: Dynamic Model of Tri-trophic Food Chain

We construct a standard food chain model consisting of three trophic levels, all of which follow logistic growth. The consumption of the primary consumer on the producer and the predation of the secondary consumer on the primary consumer level both follow the Holling- II functional response. The model can be represented by a system of nonlinear ordinary differ- ential equations.[1] AY dX X R (1) X B1 + X dt K

关注数学模型   dY A X A Z (2) Y D E = − + − 1 2   1 1 dt B X B Y + +   1 2   dZ A Y (3) Z D E = − + 2   2 2 dt B Y +   2 Where, R : Growth rate of the producer; K : Environmental carrying capacity of the pro- iA : Maximum predation rate of the primary consumer and secondary consumer; iB : Half- ducer;

D : Mortality rate of the primary consumer and secondary consumer; iE : saturation constant; i Conversion efficiency of the primary consumer for the producer and the secondary consumer for the primary consumer;t : Time.

After inputting the initial data, the biomass of different trophic levels stabilizes into a 微信公众号：数学模型 cyclical pattern within a short period.

微信号：MATHmodels

As shown in Figure 4, In the cycle, the biomass of producers increases first, followed by primary consumers and then secondary consumers. Afterward, the biomass of producers de- creases, leading to reductions in primary and secondary consumers. This cycle repeats. Also, Biomass decreases progressively from producers to primary consumers to secondary consum- ers.

4.4 Model 2：Dynamic Model of Food Web

Although the food chain model provides a basic relationship between the three trophic levels, the interactions it considers are too simplistic, only including the most basic predator- prey relationships, which clearly do not reflect the complexity of real agricultural ecosystems. Therefore, we have developed a food web dynamics model that divides the food web into four components: producers, consumers (including two trophic levels), decomposers, and soil nu- trients.

Compared to the food chain model, the optimization of this model includes:

X (which typically represents crops in real agri-  Dividing producers into two parts: 1 X (which typically represents weeds). The hypothesis previ- cultural systems) and 2 X (grass-like producers). ously mentioned that herbicides only affect 2  The impact of insecticides on the biomass of the insect population (which is part of Y ) has been considered, and the initial insect population has the same preference for both grass-like producers and crop-like producers.

 Incorporating decomposers into the ecological network, considering their interactions with producers, primary and secondary consumers, and soil nutrients.

 Accounting for the biomass of the soil nutrients, making the model more representa- tive of real agricultural ecosystems.

To simplify the complex interactions in the agricultural food web, especially with inter- twined food chains, we assume predator predation follows a linear relationship. This takes into account predator mobility and uncertain food sources. Compared to Holling-II, Holling-I better suits this scenario, as it assumes predation rate is unaffected by prey density, reflecting a linear increase in predation.

4.4.1 Food web model (without human intervention)

Based on the carbon flux between different components and their respective biomasses, we have established dynamic equations for each of the four components.

The food model is shown in Figure 5:

The increase in producer biomass of agriculture ecosystem is driven by photosynthesis, while the decrease in producer biomass results from inter-taxon competition, consumption, and X non-predatory mortality.[2] Thus, the temporal dynamics of producer biomass, including 1 X (grass-like producers), can be expressed as: (crop-like producers) and 2 dX X X +   (4) 1 r X c X Y c X D a c SX d X = − − − + − 1 1 2   1 1 13 1 15 1 61 61 1 1 1 dt K   dX X X +   (5) 1 r X c X Y c X D a c SX d X = − − − + − 2 1 2   2 2 23 2 25 2 62 62 2 2 2 dt K   Where, 1r and 2r represent the maximum specific growth rates of X and X , respectively, 1 2 and K denotes the maximum environmental carrying capacity. Utilizing the Holling-I func- c X Y , c X D , c X Y , and c X D represent the carbon flow from producers tional response, 13 1 15 1 23 2 25 2 c indicating the maximum consumption rate when taxonomic to primary consumers, with jk 1d and d are the mortality rates of X and X , respec- group k consumes group j . Parameters 2 1 2 tively.

The increase in biomass of consumers (comprising two trophic levels) is driven by the assimilation of consumed resources, while the decrease in consumer biomass is a result of pre- dation and respiration. Therefore, the dynamic changes in the biomass of consumers, including

关注数学模型 Y (primary consumers), Z (secondary consumers), and D (decomposers), can be expressed as follows:

dY a c X Y a c X Y c YZ I Y (6) dt = + − − 13 13 1 23 23 2 34 3 dZ a c YZ I Z (7) dt = − 34 34 4 微信公众号：数学模型 dD a c X D a c X D a c SD I D (8) dt = + + − 15 15 1 25 25 2 65 65 5 iI represents the respiration rate of the consumeri . The parameter a indicates the Where, jk assimilation efficiency corresponding to the case where consumer k consumes taxonomic group c indicates the maximum consumption rate corresponding to the case where j . The parameter jk taxonomic group k consumes taxonomic group j .

The increase in biomass of soil nutrients comes from inputs such as remnants of the forest, the bodies of producers, and the feces of consumers, while the decrease in soil nutrients is due to the consumption by decomposers and producers and outflow. The dynamic change of S (soil 微信号：MATHmodels nutrients) is expressed as follows:

dS I d X d X e c X Y e c X Y e c YZ e c X D e c X D = + + + + + + + 1 1 2 2 13 13 1 23 23 2 34 34 15 15 1 25 25 2 S (9) dt e c SX c SX e c SX c SX e c SD c SD T S + − + − + − − 61 61 1 61 1 62 62 2 62 2 65 65 65 r SI represents the input of suspended organic matter from forest remnants, and rT Where, e indicates the egestion rate when taxonomic denotes the total output rate. The parameter jk group k consumes group j .

After the initial data is inputted, the system undergoes dynamic changes for a period of time before eventually reaching a stable state.

As shown in Figure 6, the biomass of grass-like producers increases rapidly at first, indi- cating a competitive advantage over crop-like producers in the absence of human interference. Over time, crop-like producers' biomass declines and eventually disappears, likely due to their higher resource demands and lower assimilation efficiency compared to grass-like producers. As a result, the biomass of crop-like producers reaches zero. The decline in grass-like producers leads to a significant reduction in soil nutrient consumption, and soil nutrients stabilize at a higher level.

Primary consumer numbers increase rapidly at first due to the excess biomass of grass- like producers, then stabilize. Secondary consumer biomass gradually decreases, reflecting the system's ecological balance. In this model, the decline in secondary consumer biomass is due to migration, not extinction. For example, birds migrate based on food availability, and while they may disappear from certain areas, their overall population remains intact in the ecosystem.

Eventually, the biomass of all species stabilizes, indicating equilibrium in interactions like predation, competition, and mortality. While no noticeable fluctuations occur, this does not imply the absence of change, but rather that the rate of change is too slow to be observed over a short timeframe. This stable state reflects the long-term coexistence of species in the ecosys- tem.

4.4.2 Food web model (with human intervention)

X (grass-like producers), farmers begin using To address the issue of excessive growth of 2 herbicides and insecticides. These chemicals are reflected in our model in different ways: in- secticides have a more direct effect on the biomass of insects (included inY ), typically leading X (grass-like producers) by to a significant reduction in their biomass, while herbicides affect 2 gradually increasing their mortality rate over time.

Since the effect of herbicides is not instantaneous but accumulates over time, this gradual increase in mortality is modeled using an exponential function. Herbicides slowly reduce the plants' growth ability, causing their mortality rate to rise over time. Specifically, the dynamic changes in the biomass of grass-like producers can be expressed as:

dX X X +   ( ) t t (10) 1 ( 1 − − ) r X c X Y c X D a c SX d e X = − − − + − + α 2 1 2 0   2 2 23 2 25 2 62 62 2 2 2 dt K  Where the effect of herbicides on grass-like producers is expressed through the mortality ( ) t t (1 − − ) d e X X to herbicides. rate term + α , and the parameterα represents the sensitivity of 0 2 2 2 In contrast, insecticides directly affect the biomass of insects. Insects respond rapidly to insecticides, so their biomass decreases quickly, leading to a reduction inY . The dynamic changes in the biomass of primary consumers can be expressed as:

dY ( ) t t − − a c X Y a c X Y c YZ I Y e (11) = + − − − β 0 13 13 1 23 23 2 34 3 dt ( ) t t − − e Where the effect of insecticides on insects is reflected in the term β , and the param- 0 eter β represents the sensitivity ofY to insecticides.

We considered the cases of using insecticides alone, herbicides alone, and both insecti- cides and herbicides together. After incorporating several sets ofα and β values, we processed the results for different groups and presented them on the same graph. The final results are shown below.

关注数学模型 apply herbicide a=e1 a=e3 MW sen 1) Dnxeseonpoud rXxz) Grass-like producers(X2)

Soil nutrients(8)

wwww

α=e{ 20 60 80 100 Time (a) (b) apply herbicide apply pesticide and pesticide

(xisnad -rs) Grass-like producers(X2) Grass-lika producers(X2)

Time (c) (d)

With Herbicide and Pesticide As shown in Figure 7, We considered three scenarios: using pesticide alone, herbicide alone, and both simultaneously, incorporating several sets ofα and β data. The results from these groups were summarized in a single figure, leading to the following outcomes.

Compared to Figure (a), Figures (b), (c), and (d) show some changes.

As shown in Figure (b), we tested three sets of α data: α = e , e³ and e⁵ . As α increases, the appearance of grass-like producers is delayed, and when α = e⁵ , their biomass eventually sta- bilizes at zero. At this point, crop-like producers stabilize at a certain biomass level. This sug- gests that herbicide is crucial in the current agricultural ecosystem and needs to be used long- term, as it is impossible to completely eliminate all grass-like producers in real ecosystems.

As shown in Figure (c), we tested three sets of β data: β = e0.5 , e1.0 and e1⁵ . The results show no significant differences between the three sets. Although the reduction in insect con- sumption of crop-like producers initially causes a slight increase in their biomass, competition between grass-like producers and crops persists, and the biomass of crop-like producers ulti- mately remains low.

As shown in Figure (d), we tested three sets ofα and β data. In the model with pesticide alone, the concentration of β had little significant effect, and a high sensitivity would lead to community collapse. Therefore, we set β to 0.5 and tested different α values (α = e , e³ and e⁵ ). The results confirmed that herbicide has a consistent effect, similar to Figure (b).

4.5 Model 3: Food Web Model Considering Agricultural Cycles

The food web model effectively captures the development of agricultural ecosystems un-

der certain human interventions. However, compared to real agricultural ecosystems, it still lacks one important factor—the agricultural cycle, which includes the stages from sowing and planting crops to harvesting and crop preparation.

To better understand the impact of the agricultural cycle on the food web model, we chose rice, a typical crop in China. Unlike the double-cropping rice commonly grown in central China, we selected a single-season rice crop, as grown in Northeast China, a major rice-producing region. The planting season typically starts in mid-April to mid-May, and harvesting occurs in early October. Therefore, in the subsequent model, all crop-like producers are assumed to be single-season rice, grown in Northeast China, with the region’s climate conditions considered. In this model, X represents the biomass of rice. 1 The specific parameters required for constructing the food web model are listed in the table below.

To optimize the food web model and eventually develop a biological model that incorpo- rates the agricultural cycle, we defined several key intervention actions that occur during the agricultural cycle: Weeding: Before the planting season begins each year, farmers remove weeds to pre-  vent competition with crops, which could lead to crop death. This is reflected in the initial biomass, where the crop biomass is much larger than the weed biomass. Fertilization: Before the planting season, farmers typically apply fertilizers, as crops  generally require more nutrients from the soil. This is reflected in a sharp increase in the biomass of soil nutrients at the start of the planting season. Temperature: Temperature has a significant impact on the growth rate of producers,  specifically in a parabolic relationship with average temperature. We selected the av- erage temperature data from Wuchang City in Northeast China from 2016 to 2018 for fitting[3], and the resulting quartic polynomial curve is as follows:

First, we assume that a year is divided into discrete time units, with each month compris- ing a subset of these units. In the model to be introduced, activities such as fertilization, weed- ing, pest control, and the cyclical growth of crops all exhibit periodic patterns, though their cycles differ. Therefore, we introduce the functions f t , ( ) g t , and ( ) k t to describe the system's ( ) position within a year, a month, or a specific fertilization cycle at any given time. Based on this assumption, we have established a measurement equation f t for a specific point in time dur- ( ) ing the year:

( ) ( ) t f t f t    (12) ( ) , ( ) , ( ) ( ) f t t n g t k t f t h = − ⋅ = = − ⋅    1 n h    n 12 Where, h represents the length of chemical application cycle.

Finally, Using the temperature data from the past three years in Wuchang City, we fitted a functional relationship betweenT and ( ) g t with an 2 R > 0.99588.

( ) ( ) ( ) ( ) 2 3 4 4.2071 5.1125 0.6947 0.0250 19.57054 (13) T g t g t g t g t = − + − + −

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (a)                                  (b)

关注数学模型 2016 to 2018 was used for fitting;(b) The resulting quartic polynomial curve Chemicals (Herbicides + Pesticides): The effects of chemicals, such as herbicides  and pesticides, have been incorporated into the food web model, where the biomass of rice and the biomass of primary consumers are reduced. 微信公众号：数学模型 Harvesting: When crops mature, they are harvested, temporarily removing them  from the food chain. This is represented by the removal of all X1 (crop-like produc- ers). Nutrient Return After Harvest: Organic waste decomposes and returns nutrients to  the soil. Considering that after rice harvesting, organic matter (such as residues from plants like buckwheat) returns to the farmland, this is represented by a portion of the total biomass of X1 being returned to soil nutrients. Ultimately, we divide the agricultural cycle into two main phases: the growing season (April to October) and the fallow season (October to April of the following year). We have further refined the biomass expressions for different trophic levels based on the characteristics of these two phases. 微信号：MATHmodels

4.5.2 The growing season

During the growing season, the primary factors we consider include herbicide application, fertilization, temperature, and chemicals. These factors affect various components of the eco- X , X ,Y , and S . Herbicide application leads to a significant change in system, particularly 1 2 : 10:1 X to X , which we set as X X = the ratio of . Temperature is modeled through the func- 1 2 1 2 X and X . For fertilization, we tionT (13), which describes the impact on the growth rates of 1 2 assume that the soil nutrient levels increase by a constant value each growing season. Lastly, we assume that herbicides and insecticides are sprayed simultaneously, and that this spraying occurs once every h cycles, to fulfill the requirement for repeated applications. The related ex- pressions are as follows:

dX X X +    2  ( ) (14) 0.005( 16) 2 1 ( 1 k t ) − T r X d e X = − − + − +⋅⋅⋅⋅⋅⋅− + α 1 1 2     1 1 1 1 dt K   dX X X +   (15)  2  ( ) 0.005( 16) 2 1 ( 1 k t ) − T r X d e X = − − + − +⋅⋅⋅⋅⋅⋅− + α 2 1 2     2 2 2 2 dt K   dD (16) a c X D a c X D a c SD I D dt = + + − 15 15 1 25 25 2 65 65 5 (17) 10 S S = + p Where, S represents the biomass of soil nutrients before fertilization at the start of the p X can be found in(4); The omitted part of X can second growing season; The omitted part of 1 1 be found in(5).

Z , D and S are not directly influenced by the agricultural cycle during the growing season, so the equation for Z is referenced from(7), the equation for D is referenced from(8), the equa- tion for S is referenced from(9).

4.5.3 The Fallow Season

During the fallow period, the agricultural cycle factors to consider include harvesting, temperature, and nutrient return after harvest. Since rice harvesting occurs in October, we as- X ) remains zero during the fallow period. Consequently, related sume that the biomass of rice ( 1 X , and species such asY , D , and S are affected. Specifically,Y and D can no longer consume 1

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m X . Meanwhile, as X disappears, temperature only in- S can no longer obtain nutrients from 1 1 X . D will benefit from post-harvest nutrient recycling, which is represented by the fluences 2 X ’s nutrients from the harvest. Meanwhile, since it is the fallow acquisition of a portion of 1 period, pesticides and herbicides are no longer used. The related expressions are as follows:

dX X X +   (18)  2  0.005( 16) 2 1 T r X d X = − − + − +⋅⋅⋅⋅⋅⋅− 2 1 2     2 2 2 2 dt K   dY (19) a c X Y c YZ I Y dt = − − 23 23 2 34 3 dD (20) a c X D a c SD I D dt = + − 25 25 2 65 65 5 dS I d X e c X Y e c YZ e c X D = + + + + 2 2 23 23 2 34 34 25 25 2 S dt (21) 1 e c SX c SX e c SD c SD T S X + − + − − + 62 62 2 62 2 65 65 65 r p 2 X harvested this year. Where, X represents the total biomass of 1 p The equation for Z is referenced from(7).

4.5.4 The result of food web model considering agricultural cycles

After inputting the initial values, we obtained the biomass changes of each component throughout an agricultural cycle. Since the quantities at the beginning of each year are roughly the same, the results for each cycle are consistent. Below, we present the results for a single cycle.

As shown in Figure 9, rice biomass remains stable during the growing season, drops to zero after harvesting, and stays at zero during the fallow period. Grass-like producers' biomass

关注数学模型 decreases after herbicide application but recovers before the next application, indicating a rea- sonable spraying interval. During the fallow period, their growth is initially vigorous but de- clines due to low temperatures. Primary consumers follow a similar trend, with insecticide causing slight interference, but they grow steadily during the growing season and die in the fallow period due to lack of food. Secondary consumers and decomposers show minimal bio- mass changes, while soil nutrients increase as other components die, preparing for the next growing season. 微信公众号：数学模型

5 Problem 2: Ecosystem Assessment

5.1 Problem analysis

In Problem 1, the food web model that takes into account the agricultural cycle effectively captures the changes in the biomass of various components within a single cycle. However, it cannot give a comprehensive evaluation of ecosystem advantages and disadvantages report of the ecosystem. When considering issues such as species return and herbicide removal, contin- uing to use the food web model to calculate biomass changes of all components would further complicate the problem. Therefore, we have established a network model based on stability as 微信号：MATHmodels the evaluation criterion, aimed at measuring the stability of the ecosystem when it reaches equilibrium and making comparisons.

In this framework, we chose to simplify the model and primarily considered the impacts of chemical interventions.

5.2 Model preparation

We used two methods to calculate stability. The first method—Food Web Connectivity- Chain Length Stability Calculation Method—introduces the concepts of connectivity and average food chain length. As food web stability is directly related to both its diversity and complexity[4], The ideal stability typically occurs when the connectivity is within the optimal range of 0.3 to 0.6, the average food chain length is between 2.5 and 3.5, and the final product falls between 0.7 and 2.5.

use connectivity to represent diversity and average food chain length to represent com- plexity. The second method—Maximum Eigenvalue Method—introduces the concept of car- bon flux, which is related to biomass. This can integrate some of the results from Problem 1. Two-method Calculation Network Model for Stability

5.2.1 Food Web Connectivity-Chain Length Stability Calculation Method

Since the stability of a food web is directly related to both its diversity and complexity, aL represents complexity, the respective calculation formulas whereC represents diversity and for these are as follows: ∑ L M ij (22) , C L = = a N N M ⋅ Where, N represents the total number of species, M represents the actual number of con- nections in the network, and L represents food chain length between of group k and group j . ij The product of these two, S , can be used to represent the stability of the ecosystem. The results indicate that a larger value of S signifies greater stability for the ecosystem.

5.2.2 Maximum Eigenvalue Method

The Maximum Eigenvalue Method assesses the stability of an ecological system by cal- culating the eigenvalues of the network's adjacency matrix. Eigenvalues reflect the dynamic characteristics of the system, and in ecological networks, they can be interpreted as indicators of population growth or decay rates. By taking the maximum real part of the eigenvalues, we m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m can evaluate the stability of the system, as the real part directly reflects growth or decay trends, while the imaginary part is related to oscillatory behaviors. The element of( , ) i j in the matrix m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m represents CF (the carbon flow from groupi to group j ). m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m jk m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (23) CF c BM BM = ⋅ ⋅ m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m jk jk j k m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The formula is expressed as: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ( ) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m max Re( ) (24) λ = λ max i λ iλ represents is thei -th eigenvalue Where, represents the maximum real eigenvalue; max of the adjacency matrix; Re( ) λ represents denotes the real part of the eigenvalue;

By computing the maximum real eigenvalue, we can quantify the stability of the network.

λ Larger values of typically indicate the presence of unstable modes, while smaller values max suggest a tendency toward system stability.

To verify that our chosen values are consistent with ecological principles, we introduced Ecotrophic Efficiency ( EE ) to assess the rationality of our parameter selections. The formula for calculating EE is as follows:

C pe (25) EE = T p Where, C refers to the amount of production of a species that is consumed by predators, pe as well as the amount removed through non-predatory pathways. T refers to the total produc- p tion of a species or trophic component, including all parts used for maintaining life activities, growth, and reproduction.

In the ecological model, the value of EE is typically considered reasonable when it falls between 0 and 1, and all of our values are within this range.

5.3 Assessment of Food Chain and Food Web

We conducted stability analyses of the food chain and food web models in Problem 1 using two different methods, as shown in Table 2：

aL (Average food chain tS (Pro- C (Connectiv- λ Type ity) max length) duction) Food chain 0.22 1.50 0.33 0.00 Food web 0.36 2.00 0.72 8.61 The food chain model, with lower connectivity and average length, has a simpler structure and fewer energy transfer processes, resulting in poorer stability and higher vulnerability to external disturbances, as reflected in its production output. In contrast, the food web model, with higher connectivity and greater complexity, exhibits stronger stability and adaptability due to increased species interactions. However, the smaller maximum eigenvalue of the food chain suggests that its simpler structure, less affected by external factors, allows more effective feed- back mechanisms, leading to better stability in eigenvalue-based analysis.

5.4 Assessment of the Food Web After Introducing New Species

We then introduced two new species: a pest population and suspension decomposers. After their inclusion, we reanalyzed the stability using both methods, and the results are shown in the following Figure 10 and Table 3：

关注数学模型 aL (Average food chain tS (Pro- C (Connectiv- λ Type ity) max length) duction) New food 0.31 1.8 0.56 8.65 web 微信公众号：数学模型 微信号：MATHmodels

We can observe that after introducing new species, all indicators of the new food web tend to reflect a decrease in stability. However, the decrease is only slight, which indirectly suggests that the pesticide still has an effect on the pest population. Futhermore, this does not necessarily mean that the introduction of species always leads to negative outcomes.

To better assess the impact, we introduced a new evaluation metric: the Shannon-Wiener index. This index reflects the diversity of carbon flow pathways in the system. By applying this, we can gain insights into:

 The complexity of energy/material transfer within the food web,  The diversity of carbon cycling pathways in the ecosystem,  The functional complexity of the ecosystem.

The calculation formula for the Shannon-Wiener index is as follows:

= −∑ ln (26) H CF CF ij ij , i j The calculated result shows that after introducing the new species, the Shannon-Wiener index ( H ) of the food web is 1.74, compared to 1.45 before the introduction. Therefore, in terms of diversity, the food web with the new species is better.

5.5 Assessment of the Food Web After Removing Chemicals (Herbicides +

Pesticides) Based on the inclusion of the new species, we further assessed the ecosystem's perfor- mance after removing herbicides and insecticides. We first analyzed the system's stability under these conditions, and the results are shown in Table 4:

aL (Average tS (Pro- C (Con- H (Shannon- λ Type food chain Wiener index) nectivity) max duction) length) New food web 0.31 0.56 0.17 56.99 1.86 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m without chemi- cals As can be seen, with the removal of chemicals, all stability indices tend to worsen, indi- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m cating that the system has become highly unstable. Notably, the stability index reached 56.99, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m almost seven times higher than the previous system. The diversity index ( H ) remained un- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m changed, as expected. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m To more intuitively explore the impact of chemical removal on the ecosystem, we intro- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m duced a new evaluation metric—centrality. This metric is further divided into three sub-indices: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Betweenness Centrality, Closeness Centrality, and Eigenvector Centrality. These can be used to assess the importance of individual groups within the ecosystem, which is particularly useful for evaluating the results of crop-like producers, a key focus of our study.

1.Betweenness Centrality ( C ) B Betweenness centrality measures the importance of a species as a "bridge" or "mediator" in a network. Species with high betweenness centrality frequently appear on the shortest paths between other species, playing a key role in information or material flow.

( ) i σ = ∑ (27) ( ) C i st B σ , s t i ≠ st Where, σ is the number of shortest paths between nodes s andt , and is the number ( ) st i σ st of shortest paths passing through nodei . Betweenness centrality calculates how often species i acts as a mediator on the shortest paths.

2.Closeness Centrality ( C ): C Closeness centrality measures the average distance of a species to all other species in the network. Species with high closeness centrality can reach other species more quickly, giving them an advantage in information dissemination or resource acquisition.

1 = ∑ ( ) (28) C i C ( , ) d i j j i ≠ Where, ( , ) d i j is the shortest path distance between speciesi and species j . High closeness centrality indicates that a species is close to others, allowing faster information spread.

3.Eigenvector Centrality ( C ): E Eigenvector centrality considers both the number of direct connections a species has and the importance of the species it connects to. A species connected to other key species increases its own importance.

1 = ∑ (29) ( ) ( ) C i CF C j E ij E λ j Where, CF is the carbon flow between speciesi and j , andλ is the largest eigenvalue of ij the matrix. Eigenvector centrality is determined by solving the eigenvector, usually requiring an iterative method.

In the equation, the solution for i depends on j , making it impossible to solve ( ) ( ) C C E E using traditional methods. Therefore, we utilize Python's networkx library, along with the ei- genvector, centrality and numpy functions, to apply the Power Iteration method to solve for the eigenvector, and subsequently calculate the centrality of the eigenvector.

We only used Eigenvector Centrality because chemical substances primarily affect group centrality by influencing carbon flow, which leads to minimal changes in the other two types of centrality. Therefore, we will only present the results based on EC here, as shown in the figure below:

关注数学模型 (a)                                  (b) 微信公众号：数学模型

genvector centrality analysis of food web without chemicals As shown in Figure 11, it is clear that when chemicals are considered, the centrality of crop-like producers is much higher than that of grass-like producers, whereas the opposite is true when chemicals are not considered. This further highlights the necessity of herbicides. Additionally, we observe that soil nutrients have slightly lower centrality when chemicals are used compared to when they are not, suggesting that the use of chemicals still has some impact on soil nutrients. As for the centrality of pests, it is higher when insecticides are used. This is likely because the centrality of crop-like producers is so high, and pests tend to consume crop- like producers. The effect of this predation outweighs the negative impact of insecticides, 微信号：MATHmodels which explains why the centrality of pests increases instead of decreasing.

5.6 Assessment of the Food Web After Introducing Bats (or Bees)

Based on the introduction of a new species and the removal of chemical agents, we con- ducted a comprehensive assessment of the food web with the introduction of bats, evaluating its stability, diversity, and centrality. The results are as follows. In this scenario, we assume that bats only prey on pest populations and assist crop-like producers with pollination, thereby en- hancing their growth rate. Additionally, we explored replacing bats with bees, assuming that bees are solely involved in pollination activities, and thus, they only contribute to increasing the growth rate of crop-like producers. The result is shown in Figure 12 and Table 5:

aL (Average food tS (Pro- C (Connec- H (Shannon- λ Type Wiener index) tivity) max chain length) duction) Bats 0.28 0.61 0.17 29.29 2.20 Bees 0.31 1.81 0.56 43.37 1.97

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

son of centrality in degrees in food web with bats From the stability results, we can observe that although the stability after introducing bats did not fully return to the level observed with chemical agents, it still showed a significant improvement compared to the scenario without chemicals. Bees, on the other hand, only en- hance the growth rate of crop-like producers without preying on pests, which results in a rela- tively lower stability of the system. From a diversity perspective, bats contribute more to in- creasing biodiversity than bees. From the perspective of centrality, introducing bats leads to a reduction in the centrality of pests across various metrics, and this effect is more pronounced than the increase in centrality for crop-like producers due to pollination by bees. This is because bats not only assist in pollination but also help reduce the biomass of pests.

6 Problem 3: Towards Green Agriculture

6.1 Problem background

Green agriculture has been a hot issue of research in recent years, which is an agricultural production method that mimics natural farming while taking into account environmental pro- tection, efficient use of resources and economic benefits. For a farmer, he wants to maximize the sustainable and considerable income that the land brings him.

In this context, we propose three solution pathways to achieve green agriculture. Then we combine them to obtain seven schemes, as well as a blank control group. Based on the set of differential equations in Problem 1, we change the initial assignments or coefficients of the equations, which can obtain the biomass of each species under the steady state of the ecosystem in different solutions. From this, a series of evaluation indexes such as Shannon index can be calculated. After the data were normalized, we applied the EWM-AHP to obtain the respective weights of the evaluation indicators, and then calculate the scores of different solutions. The weight setting in AHP is subjective; therefore, the EWM is employed to capture the variability within the data. The objectivity of the weights calculated through EWM effectively compen- sates for the limitations of AHP. Before applying the model, we carry out necessary preparation.

关注数学模型

6.2 Model preparation

6.2.1 Determination of Scheme layer D

Do nothing D1

Applying organic fertilizer, introducing earthworms and D2 other soil decomposers to im-prove soil conditions

D3 Introduce predators to control pests

D4 Manual weeding Scheme layer D D5 D2+D3

D2+D4 D6

D3+D4 D7 7

D8 D2+D3+D4

6.2.2 Determination of Indicator C As shown in Table 6, the comprehensive benefits of an agro-ecosystem can be taken as the target layer, which can be evaluated through four standard layers. These four aspects can in turn be reflected through a number of indicators.

Index Standard Unit Indicator C Target layer A layer B type Biomass of X1 (C1) Positive ·cm

-2 g·cm Biomass of X2 (C2) Negative Economic benefit B1 Biomass of P (C3) -2 g·cm Negative

Cost(C4) Negative Comprehensive Positive Shannon index(C5) Ecological benefit A benefit B2 Ecosystem stability(C6) Positive

-2 g·cm Positive Biomass of D (C7) Sustainable benefit B3 -2 g·cm Positive Biomass ofS (C8) Social Positive Social support(C9) benefit B4 Supplementary note to C4: The C4 indicator is a subjective scoring indicator. We mainly consider money costs, time costs and labor costs. For example, manual weed- ing significantly increases labor and time costs, and fertilizer application takes time from implementation to effect, so time costs increase.

 Supplementary note to C6: In the previous section, we have used two methods to characterize ecosystem stability, namely the Food Web Connectivity-Chain Length Stability Calculation Method and the Maximum Eigenvalue Method. Here we use the same method to reflect the ecosystem stability.

 Supplementary note to C9: Social support is a scoring indicator. When a farmer adopts a higher number of green measures, the produce is more advantageous in terms of advertising and marketing, government organic certification, etc., and therefore the rating will be higher. The score is obtained by subjective scoring by experts.

6.2.3 Calculation of other indicators

The basis for the work here is equations (4)-(9). Depending on the choice of scheme layer, we change the initial assignments or coefficients of the system of equations so as to obtain the stabilized biomass of each species, which is analyzed as follows.

If we choose scheme D2, we change the initial assignment of soil nutrients to +10 from the original; and we change the initial assignment of the decomposer D to 3 times the original.

If we choose scheme D3, we add β to the end of equation (6) as a way to reduce the − growth rate of the pests.

If we choose scheme D4, we add to the end of equation (5) as a way to get an expo- X − α 2 nential reduction in weeds.

If we choose schemes D5-D9, we are doing a combination of the above operations, from which we calculate the biomass of each species in the ecosystem's steady state.

6.3 EWM-AHP

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

6.3.1 Data preprocessing

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Data positivizaton, we want to convert negative data into positive data with the following m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m formula: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m { } m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ' max , , , , , 1,2, , (30) X X X X X X i n = − =   m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1 2 3 i n i { } , , , , is a set of negative data. X X X X  1 2 3 n Data dimensionless, we use the following formula to eliminate the effect of data magni- tude on the entropy weighting method:

x (31) z i i n =∑ 2 x i 1 i

6.3.2 The application of EWM-AHP

Calculate the weight of evaluation objecti under the indicator j In the previous step, we have obtained normalized data. Let the normalized data for the indicator j of the evaluation objecti be ijz (i =1,2,……,n; j =1,2,……,m), then the weight ofi under the indicator j is:

z ij ( 1,2, , ; 1,2, , ). (32) p i n j m = = =   ij n ∑ z ij 1 i = Calculate the entropy of the indicator j 1 n ∑ (33) ln ( 1,2, , ) e p p j m = − =  j ij ij ln n 1 i = Determine the weight for indicator j

关注数学模型 1 e − j (34) ( 1,2, , ) w j m = =  j m ∑ g k 1 k = Calculate the comprehensive score ofi m =∑ (35) f w p i j ij 1 j =

6.4 Analysis of results

By analyzing the weights of the indicators and the scores of the evaluators in each indica- tor, we can draw the following interesting conclusions:

 Considering the biomass weight corresponding to each species, crop like producers and soil hold the greatest weight, highlighting their critical importance. This is con- sistent with agricultural practices and findings from related academic research. Nu- 微信公众号：数学模型 merous studies have emphasized the critical role of soil organic matter in sustainable agricultural systems.[5][6]  The results indicate that simply improving soil conditions alone will not lead to crop growth. However, introducing natural predators of pests or implementing regular man- ual weeding can significantly enhance crop growth.

 Among the 9 evaluation criteria, ecosystem stability stands out as the most critical, accounting for over 30% of the total weight. Ecosystem stability reflects the system's ability to withstand external changes, making it essential for the sustainable develop- ment of agricultural systems.

 Manual weeding is indispensable for maintaining ecosystem stability. Unlike the 微信号：MATHmodels short-sighted approach of using herbicides, regular manual weeding, though time-con- suming and labor-intensive, delivers significant and lasting results.

mate scores of standard layers

as their weighted overall scores. Notably, D1 serves as the blank control group, highlighting the rigor of the modeling process. D6 achieved the highest score, indicating that the solution combining improving soil conditions and manual weeding, should be adopted by farmers to achieve sustainable green agriculture.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

7 Sensitivity Analysis

In Problem 1, we developed a dynamic food web model with herbicide. In the result of that model, we proposed Figure 7(b), with α choosing e¹, e³ and e⁵ deliberately. Alpha is proportional to the herbicide dosage. Therefore, alpha denotes the power of the herbicide. With higher alpha, the herbicide will have a greater impact on the grass-like producer, thereby indi- rectly affecting other species and the stability of the agricultural ecosystem. As a result, we adjusted alpha within the range of e0 to e1o, producing a series of bifurcation diagrams, which are combined to Figure 16.

X2 Bifurcation Diagram Y Bifurcation Diagram X1 Bifurcation Diagram 30 30

25 26 20 20 Blomass 1.5 1.0

0.5

00 8 10 10 10 Power cf a (a = ex) Power of e (a = φx) Power of e (z = e) S Bifurcation Diagram Z Bifurcation Diagram D Bifurcation Diagram 10 32.5 0.22 30.0 0.9 0.20 27.5 0.8 0.18 25.0 5 220 0.7 20.0 0.14 0.6 17.5 0.12 0.5 16.0 0.10 8 10 10 8 10 Power of e (a= e) Power of e (a = e)

in [e⁰, e¹0], demonstrating the shift of dynamical states with the parameter variation. Two different dynamical states are present: blue for periodic oscillation and red for ex- tinction. Corresponding to one given value of alpha, the maxima biomass of each taxo- nomic group would exhibit one of the two dynamical states. For the periodic oscillations, the maxima for the biomass of X1, X2, Y, Z, D, S, respectively, is utilized in plotting the graphs.

Figure demonstrates the shift of food web dynamics when the value of parameter alpha starts from e1 and ends at e10. One significant finding is that when alpha reaches around e4.3, a sharp change occurs within the ecosystem, with crop-like producers prospering (increas- ing rapidly from 0 to 3.0) and grass-like producers dropping almost suddenly from 25 to ex- tinction. This represents a critical point for the herbicide to completely eliminate grass-like producers. As a result, crop-like producers win the competition with the grass-like producers. Due to Y 's food reliance on X1 and X2 , the sudden change directly affects Y 's biomass. How- ever, this impact slowly propagates through the food chain to Z , causing a gradual decrease in its biomass. On the other hand, D is less affected and declines in a relatively stable manner. The rapid decline of S shows that an excessively high herbicide dosage can seriously affect the soil's nutrients and structure. This observation partially explains the necessity and importance of replacing herbicides with manual weeding in organic agriculture.

This sensitivity analysis of alpha also provides a reasonable explanation for the choice of alpha value as e³ in Model 3 of the Food Web Model Considering Agricultural Cycles in Problem 1. Specifically, this herbicide power is moderate, as it does not completely disrupt the stability of the entire system or the nutrient content and structure of the soil.

关注数学模型

8 Model Evaluation and Further Discussion

8.1 Advantages

After a thorough evaluation, our model offers several notable advantages:  Our model effectively addresses all objectives with a progressive structure across the problems. Problem 1 designs increasingly complex differential equations; Problem 2 微信公众号：数学模型 calculates network arc weights using balanced biomass from Problem 1; Problem 3 integrates balanced biomass and multi-criteria evaluations to provide organic farming recommendations.  The model is versatile, incorporating differential equations, network diagrams, and EWM-AHP decision evaluations. Its diverse and intuitive visualizations offer clear insights.  Sensitivity analysis validates parameter choices, particularly the herbicide power pa- rameter. Bifurcation diagrams further demonstrate the model's robustness across var- 微信号：MATHmodels ying conditions.

8.2 Limitations and Extension of the model

Our model has the following limitations and related improvements:  There is currently no universally accepted method for calculating ecosystem stability.

While we adopted a widely used approach, some studies suggest its results may di- verge from real-world conditions.  Our case study focuses on rice paddies, a well-researched scenario, providing an op- portunity to test the model's applicability and scalability in different contexts.
