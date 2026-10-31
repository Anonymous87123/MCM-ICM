Summary Sheet

Summary

The decomposition of organics by fungi plays a vital role in the natural carbon cycle. We are expected to determine the interactions among diﬀerent fungi and the impact of environmental ﬂuctuations. In this paper, white-rot fungi, brown-rot fungi and Aspergillus niger are the main research objects for analysis. Three models are established.

Model I: Multi-Fungi Decomposition Model. First, based on the enzymatic reaction kinetic equation and Michaelis-Menten equation, we establish a single fungus decomposition model. Then, by introducing competitiveness index, the interactions of multiple fungi are described, and a multi-fungi decomposition model is established. It is found that the combination of white-rot fungi and Aspergillus niger (WR & AN) would promote the decomposition of cellulose by Aspergillus niger; the combination of white-rot fungi and brown-rot fungi would inhibit the decomposition of lignin by white-rot fungi.

Model II: Multi-Fungi Interactions Model. We establish Logistic growth retardation model and Lotka-Volterra population competition model to consider the impact of short-term and long-term interactions on fungal growth, respectively. In the short term (7 days), the growth of the three fungi is linear due to the suﬃcient resource; in the long term (500 days), the combination of white-rot fungi and Aspergillus niger, as well as the combination of brown-rot fungi and Aspergillus niger (BR & AN) can coexist, showing a promoting eﬀect. However, the combination of white-rot fungi and brown-rot fungi has been eliminated from the population and cannot coexist.

Model III: Multi-Fungi-Interactions-Environment Model. First, we establish the relationship model of the growth rate with the environment, and determine the inﬂuence of two environmental variables on the fungal decomposition rate. Then, through sensitivity analysis of rapid environmental ﬂuctuations, the decomposition rate trends under temperature and humidity changes are obtained. It is found that when the temperature changes, the fungi and their combinations that are suitable for the corresponding temperature have advantages; in the case of relatively low humidity, the fungi with high moisture tolerance and their combinations have advantages.

In addition, we predict the relative advantages and disadvantages in species and species combinations by calculating the decomposition rate under diﬀerent temperature and humidity conditions. We ﬁnd that all species are at a disadvantage in the colder season of temperate zone and arid environment; in the warm season of temperate zone and semi-arid environment, BR and combinations of BR & AN have advantages, and WR and combinations of WR & AN have disadvantages; in tropical rain forests environments, the situation is reversed.

Finally, we describe the impact of fungal species diversity on the ecosystem and summarize the importance of biodiversity: the increase in biodiversity can improve the environment’s resilience.

8 Model Evaluation

21

8.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

微信公众号：数学模型 8.2 Weaknesses and Possible Improvements . . . . . . . . . . . . . . . . . . . . . . . 21

9 An Article

21

1 Introduction

1.1 Problem Background

微信公众号：数学模型 The carbon cycle refers to the exchange of carbon elements in the biosphere, lithosphere, soil sphere, hydrosphere and atmosphere, which includes the decomposition of some compounds, mainly the decomposition of woody ﬁbers and ground litter [1]. In this process, carbon is converted into other forms to be used by the earth again.

Fungi are an essential factor in the decomposition of lignocellulosic ﬁbers, which have many typical characteristics. Among them, growth rate and moisture tolerance play a vital role in the decomposition of lignocellulosic ﬁbers and dead plant materials.

微信号：MATHmodels (a) White-Rot Fungi [2] (b) Brown-Rot Fungi [3] (c) Aspergillus Niger [4]

1.2 Restatement of the Problem

Based on the background information, the main tasks of this paper are as follows:

• Based on multiple fungi, establish a mathematical model to describe ground litter and woody ﬁbers decomposition through fungal activity. In the model, the interaction between diﬀerent types of fungi (with diﬀerent growth rates and moisture tolerance) needs to be included.

• Analyze the interactions between diﬀerent types of fungi (including short-term and long-term trends). Perform sensitivity analysis of rapid environmental ﬂuctuations and determine the overall impact of changes in atmospheric trends to evaluate the impact of changes in local weather patterns.

• Predict relative advantages and disadvantages of each species and combinations of species that may continue to exist, and make predictions in arid, semi-arid, temperate, arboreal, and tropical rain forests.

• Analyze how the diversity of fungal communities in a system aﬀects the overall eﬃciency in decomposing ground litter. When there are varying degrees of variation in the local environment, analyze the importance and role of biodiversity.

1.3 Our Work

• First of all, by solving the enzymatic reaction kinetic equation and Michaelis-Menten equa- tion, a single fungus decomposition model was established. Then, competitiveness index was introduced to describe the interactions of multiple fungi, and a model of multiple fungi decomposition was established. Finally, the changes in the decomposition rate of organics when various fungi interact were determined;

微信公众号：数学模型

• We established Logistic growth model and Lotka-Volterra competition model to consider the impact of short-term and long-term interactions on fungal growth, and determined the speciﬁc relationship between the competition coeﬃcient and the growth rate of fungi, including population elimination and coexistence.

• When analyzing the impact of diﬀerent environments, we identiﬁed two environmental variables: temperature and humidity. Then, through the analysis of rapid environmental ﬂuctuations and the relationship between fungal interactions and growth, the changes of decomposition rate under diﬀerent temperature and humidity were obtained. Finally, we an- alyzed the impact of interactions when the local environment changes caused by atmospheric trends.

微信号：MATHmodels

• We have divided the environments according to their diﬀerent characteristics and determined the typical values of temperature or humidity. Then, we predicted the relative dominant species and inferior species among single species and species combinations through the de- composition rate under diﬀerent temperature and humidity conditions. Finally, we described the impact of fungal species diversity on the system, and summarized the importance and role of biodiversity.

In summary, the whole modeling process can be shown as follows:

Decomposition rate of a single

Lokta-Volterra Model

fungus

Introduce competitation index

Model I

Model II

Define parameters s and r Ic according to m and u

Decomposition rate of The effect of interaction on the multiple fungal interactions growth of fungal communities

Introduce environmental variables temperature and humidity

Model III

The impact of rapid environmental Interaction between fungi fluctuations

Changes in the decomposition rate of different environments

2 Assumptions and Justiﬁcations

To simplify our model, we make the following assumptions in this paper. All assumptions will be restated once they are used in our model. 微信公众号：数学模型

1. Simplify woody ﬁbers and ground litter into cellulose, hemicellulose and lignin.

The main component of woody ﬁbers and ground litter is lignocellulose, which is composed of cellulose, hemicellulose and lignin[5].

2. Assume that the various stages of decay are consistent with the middle stage of decay, and the competitiveness index of each fungus is ﬁxed. Since the decay process is divided into diﬀerent stages, and the continuous process of each stage will not change much, the competitiveness index can be approximately stay unchanged in a ﬁxed stage.

3. Assume that the decomposition of organics by fungi is an enzyme-catalyzed reaction, and the decomposition of each organics does not interact with each other and react indepen- 微信号：MATHmodels dently. The rate of a multi-substrate enzyme-catalyzed reaction mainly depends on the enzyme activity, and the enzymes that decompose these three substances do not have a strong synergistic or inhibitory eﬀect[6]. In addition, most of the products in the decomposition process are inorganic substances such as carbon dioxide and water, which will not produce chain reactions, so that they can be ignored.

4. Assume that each type of fungus decomposes only one substance. White-rot fungi and

brown-rot fungi decompose lignin, and Aspergillus niger decomposes cellulose. Lignin is harder to be decomposed than cellulose. By consulting the information, we found that white-rot fungi and brown-rot fungi have a greater advantage in decomposing lignin, and they are the primary fungi for lignin decomposition, so we assumed that their ability to decompose cellulose can be ignored[7]. Aspergillus niger can only decompose cellulose.

3 Notations

Important notations used in this paper are listed in Table 1.

Symbol Deﬁnition

kd Enzyme inactivation rate coeﬃcient Km Michaelis constant, characteristic constant of enzyme m Moisture tolerance index u Hyphal extension rate r Growth rate(Dry weight of mycelium pellet/day) T Temperature(℃) H Humidity(%) s Competition coeﬃcient

4 Model I: Multi-Fungi Decomposition Model

4.1 Fungi Decomposition Model

微信公众号：数学模型 The chemical mechanism of fungi decomposing organics can be expressed as an enzyme-catalyzed reaction, which is generally described by the following conversion relationship.

Where A represents the organics decomposed by fungi (in this paper, lignin, cellulose, hemicel- lulose); E0 represents extracellular enzymes (enzymes that work outside the cell and play a catalytic role in the reaction); E0A is an enzyme complex substance (transition state intermediate formed by the combination of enzyme and substrate); P represents the product of biological decomposition. The rate of this reaction directly depends on the concentration of extracellular enzymes, while the biomass of fungi does not directly aﬀect the rate of decomposition[8]. 微信号：MATHmodels According to the Michaelis-Menten equation, the rate rc at which the extracellular enzyme decomposes the target organics is:

rc = VEEC (1) Km + C Where Ve is the initial speed of the reaction; Km is the characteristic constant of the enzyme (under certain conditions, the value of Km of diﬀerent enzymes is constant); E is the concentration of extracellular active enzyme; C is the concentration of organics.

The activity of extracellular enzymes gradually decreases with the decomposition process. It is assumed that the inactivation process of extracellular enzymes is a ﬁrst-order reaction:

rE, deact = kdE (2)

Where Kd is the enzyme inactivation rate coeﬃcient.

Assuming that the concentration of the fungus at t0 = 0 is P0, the concentration of extracellular enzyme E0 is E0 = aP0, and this formula is used as the initial concentration of extracellular enzyme. According to the above analysis, the following diﬀerential equation can be obtained:

dE dt = −kdE (3)

dC dt = −VEEC (4) Km + C Among them, dE dt describes the rate of enzyme inactivation, dC dt describes the rate of decomposition of organic matter, and the terms on the right side of the equation are deﬁned in equation(2) and equation(1), respectively.

According to the initial conditions: when t = 0, CE0 = aP0, C = C0, it can be solved,

E = aP0 exp (−kdt) (5) {−kd [Km ln (C/C0) + (C −C0)] } t = −1 ln + 1 (6) kd VEP0a

4.2 The Estimation of Kd: Competitiveness Index

In the above description of the enzyme inactivation process, the enzyme inactivation coeﬃcient Kd is introduced. A large amount of experimental data shows that in the environment where various 微信公众号：数学模型 fungi coexist, their interaction has a signiﬁcant impact on the enzyme inactivation rate. Therefore, we redeﬁne the enzyme inactivation coeﬃcient as the competitiveness index of fungi.

Since the competition of the population is mainly related to the growth rate, we ﬁrst assumed that the competitiveness index Ic = f(u). However, moisture tolerance is also an important feature that distinguishes diﬀerent fungi. Therefore, we introduce the moisture tolerance index to modify the Ic of a single inﬂuencing factor:

Ic = f(u, m) (7) Where f(·) is an undetermined relation equation. We will determine the speciﬁc expression form of it next.

We obtained the moisture tolerance index by analyzing the relationship between moisture 微信号：MATHmodels tolerance and decomposition rate through the OLS method.

0.85

0.8

0.75 Decomposition Rate Index 0.7

0.65

0.6

0.55

0.5

0.45

0.4 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 Moisture Tolerance Index

• Moisture tolerance index: describes the degree of fungi’s moisture resistance. The closer the index is to 1.0, the less resistant to humidity, and the closer to 0, the more resistant to humidity.

We veriﬁed that the better the moisture tolerance, the lower the decomposition rate of the strain. Since fungal strains with low growth rates are often able to survive and grow better under conditions of humidity changes. We can also ﬁt the growth rate and moisture tolerance index into a linear relationship and assume that m = g(u). Combining the above problems, we get the competitiveness equation, Ic = 0.00176u (8) By looking up the growth rate of diﬀerent fungi, we obtained the following competitiveness index in Table 2:

微信公众号：数学模型

White-Rot Fungus Brown-Rot Fungus Aspergillus Niger

Ic 0.015 0.009 0.021

4.3 Results

Lignocellulose is mainly composed of lignin and cellulose. We considered the eﬀects of single fungus and combinations of fungi separately on the decomposition rate of lignin and cellulose. Through equation 5 and equation 6, we determine that the decomposition rate of fungi will increase with time ﬁrst, and then stabilize. Since the competitiveness index of fungi is diﬀerent, their 微信号：MATHmodels performance in the decomposition of single fungus and their contribution to the decomposition of fungi combination are also diﬀerent.

(a) Cellulose Decomposition Rate (b) Lignin Decomposition Rate

alone or in combination

• Combination of Aspergillus Niger and White-Rot Fungi

Firstly, we assume that Aspergillus niger only decomposes cellulose and white-rot fungi only decomposes lignin. In nature, the lignin and cellulose in dead branches and fallen leaves are often entangled with each other, which increases the diﬃculty of fungal decomposition.

Therefore, the mixture of fungi will facilitate their decomposition. The species combination is synergistic, and the decomposition rate is higher than that of a single fungus.

• Combination of White-Rot fungi and Brown-Rot Fungi We assume that both white-rot fungi and brown-rot fungi decompose lignin. Due to the competitive relationship between them, the combined decomposition rate will be lower than 微信公众号：数学模型 that of white-rot fungi alone.

5 Model II: Multi-Fungi Interactions Model

6 Model III: Multi-Fungi-Interaction-Environment Model

6.1 The Impact of Rapid Environmental Fluctuations

Since the temperature and humidity in the environment have the most signiﬁcant impact on fungi, and the growth rate is signiﬁcantly aﬀected by temperature and humidity, we assume that rapid environmental ﬂuctuations (including temperature and humidity) only aﬀect the growth rate of fungi. However, moisture tolerance is the appearance of changes in growth rate.

6.1.1 Sensitivity Analysis of Temperature Fluctuations

• Growth Rate Change with Temperature

We found that for fungi, the temperature has an important inﬂuence on cell stability and enzyme activity. Its growth rate will increase with temperature within a speciﬁc range, but it will rapidly decrease after the maximum temperature is exceeded. Based on this experience, we assume that the fungal growth rate has a linear relationship with the temperature before reaching the maximum temperature, and the fungus will die directly after the maximum temperature is exceeded. Therefore, the change of fungal growth rate with temperature was determined.

Based on the diﬀerent optimum temperatures of the three fungi, we calculated the changes in their respective growth rates with temperature, which is shown in Figure 7.

0.08 Aspergillus Niger 0.07 Brown-Rot Fungus G=0.0015625*T White-Rot Fungus Growth Rate Dip Line 微信公众号：数学模型 0.06 Growth Rate / (g/d) 0.05

0.04

G=0.001825*T 0.03

0.02 G=0.0009615*T 0.01

0 0 5 10 15 20 25 30 35 40

微信号：MATHmodels

• Sensitivity analysis of temperature ﬂuctuations

In this section, we mainly conducted sensitivity analysis on diﬀerent temperatures. By analyzing the functional relationship between growth rate and temperature, we can determine the growth rate of diﬀerent fungi at diﬀerent temperatures, and then bring them back into the Lotka-Volterra population interaction model for calculation.

Analysis:

• Combinations of White-Rot Fungi and Brown-Rot Fungi

0.5 0.5 0.5 White-Rot Fungus White-Rot Fungus White-Rot Fungus Dry Weight of Mycelium Pellet / g Dry Weight of Mycelium Pellet / g Dry Weight of Mycelium Pellet / g Brown-Rot Fungus Brown-Rot Fungus Brown-Rot Fungus 0.4 0.4 0.4

When the temperature is low, Growth rate increases Dominant strains become 0.3 0.3 0.3 the competition is not fierce with increasing temperature more competitive

0.2 0.2 0.2 The growth rate of Competition Brown-Rot Fungus is 0 becomes fierce 0.1 0.1 0.1

0 0 0 0 200 400 600 800 1000 0 200 400 600 800 1000 0 200 400 600 800 1000 Time / d Time / d Time / d

10℃→20℃: The increase in temperature causes the growth rate of both fungi to in- crease, which makes competition intensiﬁes. Therefore, the number of white-rot fungi with population advantages will reach the peak faster, and the other (brown-rot fungi) will be eliminated.

20℃→30℃: The optimum temperature of brown-rot fungi is 26℃. If the optimum temperature is exceeded, the growth rate of brown-rot fungi will drop sharply to 0. Therefore, the growth rate of brown-rot fungi will decrease from the beginning at 30℃. The growth of 微信公众号：数学模型 white-rot fungi will further increase with high temperature, and their competitiveness will be further enhanced. As the dominant fungus, they will reach a higher peak faster.

• Combination of Brown-Rot Fungi and Aspergillus Niger:

0.5 0.5 0.5 Dry Weight of Mycelium Pellet / g Dry Weight of Mycelium Pellet / g Dry Weight of Mycelium Pellet / g 0.4 0.4 0.4 Temperature plays a decisive role in growth rate 0.3 0.3 0.3

The growth rate of Aspergillus Niger is 0 0.2 0.2 0.2

微信号：MATHmodels 0.1 0.1 0.1 Brown-Rot Fungus Aspergillus Niger Aspergillus Niger Aspergillus Niger Brown-Rot Fungus Brown-Rot Fungus 0 0 0 0 200 400 600 800 1000 0 200 400 600 800 1000 0 200 400 600 800 1000 Time / d Time / d Time / d

10℃→20℃: The synergistic eﬀect of brown-rot fungi and Aspergillus niger is not obvious in the change of temperature. The main reason for the changes of the two fungi is the increase in growth rate caused by the increase in temperature. The optimum temperature of Aspergillus niger is higher than that of brown-rot fungi. Therefore, the growth rate of Aspergillus niger caused by temperature changes will be greater than that of brown-rot fungi, and the number of Aspergillus niger will increase more.

20℃→30℃: The growth rate of brown-rot fungus has dropped to 0 at 30℃, while the growth rate of Aspergillus niger is increasing rapidly. Although the two fungi have a synergistic eﬀect, the temperature still plays a decisive role in the synergy, that is, the growth rate of Aspergillus niger at a suitable temperature is higher than the growth rate of combination of Aspergillus niger and brown-rot fungus at a lower temperature.

• Decompositon rate change with temperature

In this part, we mainly considered the inﬂuence of a single fungus and a combination of fungi on the decomposition rate of lignin at diﬀerent temperatures. In Model I, we analyzed the decomposition rate of diﬀerent fungi, deﬁned the competitiveness index, found its functional relationship with the growth rate, and introduced the moisture tolerance index to modify it, thereby analyzing the decomposition rate of diﬀerent fungi and fungi combinations. In this model, we only consider the decomposition of lignin.

For a single fungus, it is assumed that white-rot fungi and brown-rot fungi can decompose lignin. The optimal temperature of brown-rot fungi is lower than that of white-rot fungi. Therefore, when the temperature is about 26℃, the decomposition rate of brown-rot fungi is slightly higher Temperature Growth Rate Competitiveness Index Decomposition Rate T u ~ T Ic ~ u D ~ Ic 微信公众号：数学模型

than that of white-rot fungi, and the decomposition rate of white-rot fungi is the highest when the temperature is about 32℃. Besides, the highest decomposition rate is higher than that of brown rot fungi.

For fungicombinations, dueto thepreviousanalysisof thecoexistenceofdiﬀerent combinations, we found that white-rot fungi and brown-rot fungi cannot coexist continuously, so we do not consider 微信号：MATHmodels this combination. Since Aspergillus niger only decomposes cellulose, and the decomposition of cellulose by Aspergillus niger is beneﬁcial to the decomposition of lignin by white-rot fungi and brown-rot fungi, the combination of Aspergillus niger and these two fungi will have a synergistic eﬀect, that is, white-rot fungi and Aspergillus niger combination, brown rot fungi and Aspergillus niger combination has higher decomposition rate of lignin than a single white-rot fungi and brown- rot fungi. As Aspergillus niger is more adaptable to high temperature (40℃), the optimum temperature of the combined fungi will shift to high temperature overall.

6.1.2 Sensitivity Analysis of Humidity Fluctuations

When studying the inﬂuence of rapid humidity ﬂuctuations, we mainly consider the inﬂuence of humidity changes on the decomposition rate. The calculation idea is similar to temperature: 微信公众号：数学模型 Humidity Moisture Tolerance Index Growth Rate Competitiveness Index Decomposition Rate H m ~ H u ~ m Ic ~ u D ~ Ic

Through ﬁtting, we found that when the humidity is low, brown-rot fungi have higher moisture tolerance and can better adapt to ﬂuctuations in environmental humidity, and their decomposition 微信号：MATHmodels rate is slightly greater than that of white-rot fungi. When the humidity is high, the white-rot fungi has lower moisture tolerance, and its growth rate is faster in a suitable environment, and the decomposition rate will be greater than that of the brown-rot fungus. For species combinations, consider adding Aspergillus niger. First, due to the synergistic eﬀect, the decomposition rate of lignin by white-rot fungi and brown rot fungi will increase overall. Besides, due to the higher moisture tolerance of Aspergillus niger (minimum humidity of 75%), the minimum humidity tolerance of the combined fungi will slightly shift to lower humidity overall.

6.2 The Inﬂuence of Atmospheric

6.2.1 The Inﬂuence of Global Atmospheric Trends on Fungal Interactions

微信公众号：数学模型 Atmospheric Change Trend

The Increasing of Carbon Dioxide

High Temperature Fluctuation Temperature

微信号：MATHmodels Uneven Precipitation Drought

Dominant Species Selection

Since the 21st century, climate changes caused by global atmospheric changes have had a signiﬁcant impact on ecosystems. The two most important features are[10]:

• The temperature ﬂuctuates wildly, and the surface temperature rises.

• The global precipitation is uneven, and the "urban heat island" eﬀect has intensiﬁed.

Diﬀerent fungi have diﬀerent adaptability to rapid environmental ﬂuctuations. Therefore, changes in their growth environment will speed up the selection of dominant species. Speciﬁcally, fungi that are more adaptable to temperature and humidity will gain an advantage in population competition.

6.2.2 Prediction of relative advantages and disadvantages of species in diﬀerent environ-

ments

When introducing species and species combinations with relative advantages or disadvantages in 微信公众号：数学模型 diﬀerent environments, we have divided the environmental types of each region.

微信号：MATHmodels

• Temperature

Although there is a big diﬀerence in annual rainfall between tropical and temperate zones, the humidity does not change much in the same region. Therefore, in tropical and temperate regions, we only consider the impact of temperature on the relative advantages and disadvantages of species. When we considered the species combination, we did not consider the species combination in a competitive state. To simplify the topic, we only considered the species combination under long- term conditions. Under long-term conditions, competing combinations will be eliminated and eventually evolve into a single species.

,→Temperate Zone:

In temperate zones, we mainly consider the regions with temperate oceanic climate. The temperature of this kind of region generally has two representative temperatures. In cold weather, the typical temperature is about 7℃[11]. Comparing the eﬀect of temperature on the decomposition rate that we have studied, we can know that the dominant species at the time are brown-rot fungi (when considering a single species), the species combination of brown-rot fungi and Aspergillus niger (when considering combined species). In hot weather, the typical temperature is about 23℃, and the results are consistent with the cold weather.

,→Tropical rain forests:

For tropical rain forests climate, we can easily know that the annual temperature of the tropical rainforest climate is generally maintained at 25-30℃[12]. At this time, the dominant species are white-rot fungi (considering a single species), and white-rot fungi and Aspergillus niger (consider species combination).

Analysis:

The reason for this situation is that the optimum temperature of brown rot fungi is lower than that of white-rot fungi, so when the temperature is lower, they grow faster. However, when the 微信公众号：数学模型 temperature gradually increased, the high temperature inhibited the brown-rot fungus. Obviously, this trend is also satisﬁed in species combination. Therefore, if we extend the consideration, at low temperatures, the species with the most suitable temperature and the combination of species with promoting eﬀect will become the relative dominant species; while at high temperature, the species with the most suitable temperature and the combination of species will become the dominant species. These two situations are applicable to any species and combination.

微信号：MATHmodels

• Humidity

For arid, semi-arid, and tropical rain forest environments, the most typical diﬀerence is humidity. As with temperature, we do not consider competing species combinations.

,→Arid:

In arid environments, the typical humidity is below 20%[13]. According to our ﬁtting, we can know that all fungi will not grow properly at this time, that is, species and species combinations that have no relative advantages or disadvantages.

,→Semi-arid:

For semi-arid environments, the typical humidity is 20-60%[14]. In our report, the relative dom- inant species at this time are brown-rot fungus (single species), brown-rot fungus and Aspergillus niger (species combination).

,→Tropical rain forests:

For tropical rain forest environments, the typical humidity is generally above 90%. At this time, the dominant species are white-rot fungi (consider a single species), white-rot fungi and Aspergillus niger (consider species combinations).

Analysis:

The reason for this situation is that brown rot fungi have higher moisture resistance than white- rot fungi. Therefore, when the humidity is low, brown rot fungi have begun to grow. However, when 微信公众号：数学模型 the humidity gradually rises, the growth of white-rot fungi will surpass that of brown rot fungi, because species with low moisture tolerance have a higher growth rate. Obviously, this trend is also satisﬁed in species combination. Therefore, if we take an extended consideration, we will ﬁnd that the relative advantages and disadvantages of species caused by humidity are similar to temperature. When the humidity is low, the species with high humidity resistance and the combination of species with promoting eﬀect will become the relative dominant species; while when the humidity is high, the species with low humidity resistance and the combination of species will become the dominant species, because of the Species with lower tolerance in the environment will grow faster in a suitable environment. Obviously, these two situations are applicable to any species and its combination.

微信号：MATHmodels

7 Further Discussions: The Impact of Biodiversity

7.1 The Eﬀect of Fungal Diversity on Ground Litter

The better the diversity of the fungal community, the faster and more complete the decomposition of ground litter in the system. At the same time, because in diﬀerent environments, there will be diﬀerent dominant species and their combinations. This diﬀerent dominant species also constitutes the diversity of the fungal community in the system.

7.2 The Importance of Biodiversity When Environment Changes

• In diﬀerent environments, the diversity of fungal species is diﬀerent, and the diﬀerences are signiﬁcant with environmental changes. This is because the environment has a signiﬁcant impact on fungi (diﬀerent environments have diﬀerent advantages and disadvantages)

• The diversity of fungi will be less in places with harsh environments; obviously, the diversity of fungi will be higher in places with suitable environments. The reason is that diﬀerent fungi have diﬀerent characteristics, and fungi that can adapt to harsh environments grow more slowly, so when the environment is suitable, their competitiveness is not as good as 微信公众号：数学模型 fungi with poor environmental adaptability.

• When the local environment changes. The importance and role of biodiversity: When the environment changes, if the local biodiversity is good, that is, the ecosystem has better versatility, it can adjust the local environment more quickly, and make its environmental resilience change. Larger, the environment can recover better and faster.

8 Model Evaluation

8.1 Strengths

• When multiple fungi exist at the same time, we consider the competitiveness index as their 微信号：MATHmodels interaction. In the same environment, this model is scientiﬁc and reasonable, and the results are acceptable.

• We established the change in fungal growth rate caused by the interaction between fungi according to the Lotka-Volterra equation, and then tested the short-term and long-term changes, making this model more convincing;

• When considering the sensitivity analysis of temperature, we selected the possible tempera- ture span, which proved the interaction change of the species combination under the inﬂuence of the environment, and proved the stability of the model;

• After analyzing environmental changes, we substituted the parameters of diﬀerent regions into the test results, and obtained good results, indicating that our model has a rigorous structure and is suitable for species combinations in multiple regions.

8.2 Weaknesses and Possible Improvements

• As it is assumed that lignin, cellulose and hemicellulose are lignin, cellulose and hemicellu- lose, the consideration of decomposition rate will be lacking;

• When considering the relationship between moisture tolerance index and growth rate, due to the lack of available data, the ﬁtting eﬀect may not be ideal;

• When considering the combination of fungi, only pairwise combinations are typical. When there are more types of fungi, there may be errors in the results.

9 An Article

A UNIVERSITY BIOLOGY TEXTBOOK

Fungi in the Ecosystem

微信公众号：数学模型 The carbon cycle of the biosphere is an indispensable part of maintaining the balance of the ecosystem. In the carbon cycle, there is a population that plays a vital role: fungi. As a decomposer of the ecosystem, fungi participate in the decomposition of almost all organisms in the ecosystem and return most of the products of the decomposition to the ecosystem in order to supply the system for reuse. This is an essential part of the carbon cycle.

!

growth of fungi, which leads to further changes in the decomposition rate. The moisture toler- ance of fungi reflects the adaptation of fungi to 微信号：MATHmodels

1 The Specific Role of Fungi

F ungi decomposes the complex organic mat- ter fixed in the carcasses of animals and plants into simple compounds that can be reused by the producer and releases energy. Its effect is opposite to that of the producer. The role of fungi in the ecosystem is very important. Without fungi, dead animals and plants will accumulate and cause disasters. The carbon source will be locked in organic matter and no longer participate in the cycle. The material cycle function of the ecosystem will be terminated, which leads to the collapse of the ecosystem.

2 Important Characteristics of Fungi

By analyzing a large number of fungi and dif- ferent environmental factors, it can be known that the growth rate and moisture tolerance are the two most important characteristics of fungi.

The difference in growth rate results in different different environments. However, the higher the moisture tolerance of the fungi, that is, the higher its tolerance to the environment, the slower it will grow, and the fungi with low tolerance to the environment will grow faster in a suitable environment.

3 There will be Interactions between Fungi

Through our research, we found that in the same environment, the combination of fungi will also affect their decomposition rate. Taking white- rot fungi, brown-rot fungi and Aspergillus niger as examples, the combination of white-rot fungi and brown-rot fungi will inhibit each other; how- ever, the combination of white-rot fungi and As- pergillus niger will promote. Obviously, in a fixed environment, the diversity of fungi will also cause their interactions to be more complicated, and their impact on the decomposition rate will also be more complicated.

4 The Influence of Environment on its Inter-

actions

From the above, we can know that temperature and moisture tolerance are the two most essential traits of fungi. So here we mainly analyze the influence of temperature and humidity changes on their interactions and decomposition rate.

Take the three fungi analyzed above as exam-

ples.

A UNIVERSITY BIOLOGY TEXTBOOK

微信公众号：数学模型 微信号：MATHmodels

Under short-term conditions, because the en- vironment is rich in resources, we think that dif- ferent fungi have no interactions, and the growth rate is linear.

But in the long run, the impact of environ- mental changes on the interaction is huge. When the temperature in the temperate zone is low, we think that the dominant species are brown-rot fungi and Aspergillus niger; when the tempera- ture in the temperate zone is high, the dominant species we give are consistent with the low tem- perature, which is due to the interactions of tem- perature changes. The impact is not that great, so the dominant species has not changed. However, in the tropical rain forests climate, we consider the combination of white-rot fungi and Aspergillus niger as dominant species, because compared to the temperate zone, the tropical environment is more conducive to the growth of the fungi we exemplified.

The reason for this situation is that the fungi with higher tolerance to the environment (brown- rot fungi) will grow more slowly. In comparison, the fungi with lower tolerance to the environment (white-rot fungi) will grow faster.

5 Biodiversity

Forest is the most complex ecosystem on land, and

it is also the ecosystem with the most prosperous species and a number of fungi. Even most records of fungi originate from forests. Therefore, the diversity of fungi plays a vital role in maintaining the biodiversity of the forest. The diversity of fungi constitutes the detritus food chain in the forest ecosystem and is the main component of the material cycle in the forest ecosystem. It occupies a critical position in the development process of the entire ecosystem, such as restoration, succes- sion and maintenance.

Now more and more botanists, especially plant ecologists and forest ecologists, realize that the diversity of fungi plays an essential role in the ecosystem, and they are related to the result of the same evolution of the ecosystem.

The role of fungi in the ecosystem is through the understanding of disease phenomena. The phenomenon of decay and mutual symbiosis has been better understood. In all ecosystems, the interactions between fungi and all other organisms can be direct or indirect. With the direct and indirect effect of fungi, the ecosystem and the or- ganism, even the entire system can be maintained and continued. The root of all these effects lies in the critical role that fungi play in the process of material transformation and energy flow in the ecosystem.
