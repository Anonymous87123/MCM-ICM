Problem Chosen 2023

MCM/ICM

Summary Sheet

Summary

Under climate change, there will probably be an increase in inter-annual variability in precipitation regimes and more intense and frequent extreme weather and climate events, including multi-year droughts. Therefore, it’s necessary to focus on the drought adaptability of plant community. Our team build the following mathematical model to explore the responsive mechanism of plant community to drought in this paper.

Firstly, to consider the influence of plants’ interspecific interactions, we have improved on the classical model Lotka-Volterra Model by adjusting the equation between two species to multispecies differential equations based on Logistic Equation. We use Spearman Correlation Analysis to get the coefficients to measure the interaction between different species. When the distribution of two species is positively correlated, we believe that the two species are mutually beneficial to a certain extent.

Then, we consider the impact of environmental factors. Collecting the weather data for the past 15 years, we fit the linear relationship between precipitation, temperature, and soil moisture. We also define a environmental impact factor Q, adding it to the basic differential equations. Then We use the computer to set up temperature and precipitation and control changing period to simulate irregular weather cycles. The stochastic simulation is based on real data and can be adjusted artificially. By this model we predict the change trend of plant communities over time.

Next, by measuring the Shannno-Wiener index and ICV (the reciprocal of variation coefficient of species’ biomass), we get specific quantitative indicators for the drought adaptability of plant community. We calculate the change rates of the two indexes of plant communities after a period of time under different situations. Measuring each community with different species from 2 to 7, We find that the minimal number of plant species is 5 if the community want to benefit from this biodiversity. The more species, the better drought adaptability of community.

Furthermore, we further analyze potential impact of more complex environment to make our model more complete and comprehensive. We take the habitat reduction, environmental pollution, and climate warming into consideration. For each factor, we draw the biomass of species changing curve over time to intuitively show the influence of this factor.

Finally, we use Analytic hierarchy process (AHP) Model to assess the importance of each factor. We obtain four weight indicators as 0.257, 0.543, 0.131, and 0.069 for the number of species, the types of species, the weather cycles, and other environmental factors. These indicators help us to better analyze the ways to ensure the long-term viability of a plant community. The larger the indicators, the more it takes precedence over other factors that we need to pay more attention to it.

Community stability Biodiversity Drought Differential equation AHP Model

1 Introduction

1.1 Problem Background

In recent years, with global warming under climate change, extreme drought events have been increasing in frequency and intensity, which have a great impact on the structure and function of ecosystems. Precipitation has been identified as a primary factor limiting ecosystem processes. [1] Thus, there is an urgent need to investigate species interaction effects on resilience in more depth to adapt plants to increasing drought stress [2].

Different plants respond to drought in different ways and have different adaptations to dry envi- ronments. For plant communities, there is a close relationship between their ability to adapt to drought cycles and the number of species. Drought may also alter community structure as it represents a kind of stress to plants which negatively affects population density and enhances the probability of extinction of less abundant species. [3] Communities with a variety of plants are more resilient to drought than those with just one. This is very similar to the biological stability of resistance.

Resistant stability refers to the ability of an ecosystem to resist external disturbances and keep its structure and function intact. Generally speaking, the more complex the ecosystem, the higher the resistance stability. The study on the resistance stability of plant communities provides a new perspective to explain this phenomenon.

1.2 Restatement of the Problem

Considering the background information and restricted conditions identified the problem state- ment,we need to solve the following problems:

1) Firstly we are required to establish a model to predict how plant communities will change over time during irregular weather cycles. Competition and mutualism among species must be considered.

2) Then we need to calculate the minimum number of species needed for plant communities to benefit from localized biodiversity and predict the consequences of increased species numbers and changes in species composition.

3) Based on the previous model, we need to extend it to more complex environments. For example:

changes in drought frequency, environmental pollution, and habitat reduction.

4) Finally,we need to propose ways to ensure the long-term viability of plant communities.

1.3 Our Approach

In order to analysis the drought adaptability of plant communities, we will proceed as Figure 1.

• Define Environmental Impact Factor and Interspecific Interaction Impact Factor. We define arid environments and take into account interactions between species.

• Design the Plant Community Change Model. We design the plant community change and modify our model parameters to simulate larger environment.

• Evaluate Plant Community Benefit.By combining Shannon-Weiner Index and M.Godron sta- bility determination method, we can quantify the drought adaptability of plant community.

• Provide methods to ensure the long-term survival of plant community.Based on previous model, We identify the effects of different factors on plant communities and offer ways to ensure the long-term viability of a plant community.

2 Assumptions and Justification

In order to simplify the problem and make it convenient for us to simulate the real conditions, we make the following assumptions, and each of them is properly justified.

• All the data we have collected are accurate.We collected climate data, soil moisture data, vegetation amount data from various sources. And data measuring equipment inevitably has some measurement errors. So in our model, we assume that all the data we collect are accurate.

• With the exception of drought, plants is not affected by other weather extremes. The probability of extreme weather events is usually less than 5 or 10 percent. However, with the global warming, the occurrence frequency of extreme weather and climate events has changed, showing an increasing trend. The model considers only the possible extreme drought and does not consider other extreme weather conditions.

• Ignoring animal factors. Animals are also an important part of the ecosystem. There is a predation relationship between animals and plants, which affects the number of plants. At the same time, possible pests and diseases will also have an important impact on the number of plants. Since our model mainly focuses on plant community, the influence of animal factors can be ignored.

• Soil pH and soil microorganism are suitable.The pH of the soil will promote or inhibit plant growth depending on whether the plant is adapted or not. The microorganisms in the soil will also promote or inhibit plant growth. To simply our model we assume that they are all suitable.

3 Notations

Symbol Definition Unit

◦C T Temperature R mm Precipitation h Soil moisture - Q Environmental impact factor - n Number of species - kg/hm2 N1, N2, · · · , Nn Biomass of different species kg/hm2 K1, K2, · · · , Kn Environmental capacity of different species day−1 r1, r2, · · · , rn The population growth rate of different species aij Influence factors of species i on species j - H Shannon-Wiener Index - Pi Relative frequency of species i - Ni Indivisual number of species i - ICV Inverse of coefficient of vatiation - kg/hm2 τ Average biomass of each species σ Standard deviation of biomass of each species - ∆ICV Growth rate of ICV - CR Consistency Ratio - CI Consistency Index - RI Random Index - λmax Maximun eigenvalue of the judgement matrix - k Indicator to measure the concentration of SO2 - c Current SO2 concentration ppm c0 Standard value of SO2 concentration ppm D Habitat reduction ratio -

where we define the main parameters while specific value of those parameters will be given later.

4 Plant Community Change Model

4.1 Environmental Impact Factor

This model only considers arid environment when determining environmental impact factors.

Drought refers to the agricultural meteorological disaster caused by the lack of soil moisture and the destruction of crop water balance. It can be divided into soil drought, atmospheric drought and physiological drought three types.

Soil drought is caused by a lack of water in the soil, and plant roots cannot absorb enough water to compensate for the damage caused by transpiration.

Atmospheric drought is the dry water in the air, often accompanied by a certain amount of wind, although the soil is not short of water, but due to the strong transpiration, so that the plant water shortage and the formation of harm.

Physiological drought is the damage caused by the imbalance of water balance of plants caused by the obstacle of physiological process of crops caused by poor soil environment conditions. Such undesirable conditions include soil temperature is too high, too low, soil ventilation is poor, soil solution concentration is too high, and the accumulation of some toxic chemicals in the soil.

Many factors can affect the degree of drought, among which temperature (T) and precipitation (R) are the two main factors. And temperature and precipitation can directly affect soil moisture. Therefore, we can normalize the data. Soil moisture was used to reflect the influence of temperature and precipitation on the degree of drought.

We define soil moisture h as Equation (1).

h = µT + θR (1)

where µ and θ are parameters. Parameters need to be determined based on specific climate data.

Because we are required to consider the relationship of drought adaptability with respect to the number of species in a plant community, the climate data needs to have a continuous drought cycle. Meanwhile, it should not stay dry for a long time, such as tropical desert climate.Finally, we choose the temperate continental climate, characterized by cold winters and hot summers with concentrated precipitation. In the temperate continental climate of the region, we choose Xinjiang, China, becauce it is rich in forest and grassland plants, as well as meadows, swamps and aquatic plants.

By collecting data from National Tibetan Plateau Scientific Data Center [4], we can quantify the relationship between soil moisture, temperature and precipitation. The calculation results show that µ = 4.7 × 10−4 and θ = 4.8 × 10−3.

We define the arid environment when soil moisture is below h0 = 12%.

Then we consider the effect of soil moisture on plant growth. According to plant physiology, when the soil moisture is too high, it is easy to cause plant root rot. When soil moisture is too low, plant roots cannot absorb enough water, and plant growth is inhibited. Plants grow fastest when the humidity is suitable. Therefore, when only consider about drought, environmental impact factor (Q) is quadratic functions of soil moisture [5]. Q = mh2 + nh + c (2)

where m, n, and c are parameters.

According to the plants’ demand for soil mois- ture, we take Q = 1 when h = 12%, Q = 0 when h = 5% or h = 19%. It means when the soil moisture is 12%, it’s the optimum humidity for plants, so Q can reach can reach the maximum value of 1. When the soil moisture is under 5%, it’s too dry for the plants to survival and grow. So the value of Q is neg- ative, which means that the growth rate of the species is negative and the biomass will decline. When the soil moisture is above 19%, it’s too wet. The cal- culation results show that m = −10000 2400 49 , n = 49 ,

and c = −95 49. The quadratic function image of Q is shown in Figure 2.

Combined with the data we collect, we take 10 days as a weather change cycle and simulate various irregular cycles with the computer.

4.2 Relation Between Plant Species Model Based on Lotka-Volterra Model and

Spearman Correlation Analysis

The interaction between species is the basis for the formation of biomes. According to the relationship between species, interactions can be classified as positive and negative interactions. Posi- tive interactions include favoritism, primitive cooperation and mutualism, while negative interactions include competition, predation and parasitism. For the plant community in this model, we mainly consider mutualism and competition.

Lotka-Volterra model is a very classical model of interspecific competition based on Logistic model. We extend this model and establish a model of multi-species competition and mutualism relationship.

Assume that there are n species in this plant community. We define that N is biomass of a species, K is environmental capacity of a species, r is the population growth rate of a species.According to Logistic model, we have Equation (3).

dN dt = r · N · (1 −N K ) · Q (3)

where N K can be understood as the space already used and (1 −N K) can be understood as unused space.

When multiple species compete or use the same space, the following equation can be listed

dN1 dt = r1 · N1 · (1 −N1 N2 N3 Nn −a21 −a31 −· · · −an1 ) · Q K1 K2 K3 K1 dN2 dt = r2 · N2 · (1 −N2 N1 N3 Nn −a12 −a32 −· · · −an1 ) · Q K2 K1 K3 K2 · · · dNn = rn · Nn · (1 −Nn N1 N2 Nn−1 −a1n −a2n −· · · −an−1n ) · Q dt Kn K1 K2 Kn Initial Biomass (kg/hm2) Number Species

Species 1 Populus euphratica 154.57 Species 2 Haloxylon ammodendron 9.47 Species 3 Poacynum hendersonii 2.45 Species 4 Nitraria tangutorum 54.31 Species 5 Halimodendron halodendron 3.92 Species 6 Kalidium foliatum 95.38 Species 7 Tamarix chinensis 38.41 Species 8 Reaumuria songonica 83.90 Species 9 Alhagi sparsifolia 1.88 Species 10 Seriphidium kaschgaricum 9.08

where aij is the influence factors of species i on species j. When the relationship between plant species is competition, aij > 0. When the relationship between plant species is mutualism, aij < 0.

In this model, we select 10 representative plants in Xinjiang. They vary in height and include herbs, shrubs and arbors. The Latin names of the 10 plants and their initial biomass are shown in Table 1 and some of their basic information [6–10] are shown in Figure 3.

When determining the value of influence factor aij, we consider using spearman correlation analysis. Spearman correlation analysis requires two conditions:

1) Variables contain rank variables, or variables do not follow normal distribution or distribution type is unknown.

2) There is a monotonous relationship between the two variables.

We search the composition of major species and their important values in typical community plots [11]. According to biological knowledge, when the interspecific relationship is competition, the number of species is negatively correlated. When the interspecific relationship is mutualistic, the number of species is positively correlated. The data can satisfy both of the above conditions.

After calculation, we can get the correlation thermal map in Figure 4.

4.3 Results

In solving differential equations, we use Runge-Kutta Methods. It is an important iterative method for solving nonlinear ordinary differential equations. Its high precision is very suitable for solving this model.

One Species:

When there is only one species, we choose Species 1 for analysis. Plug the data from Species 1 into Equation (3), we can get the curve in Figure 5.

As can be seen from Figure 5, the biomass of Species 1 as a whole shows a downward trend over time, indicating that a single plant species has a weak ability to adapt to drought.

Multiple Species:

When considering multiple species, we choose Species 1-5 (n = 5) for analysis. Their interspecific influencing factor matrix is shown below.

  −0.33 1 0.284 0.164 0.093 −0.165 0.284 1 0.336 0.163     −0.084 0.164 0.336 1 0.073     −0.165 0.093 0.073 1 0.33   −0.33 −0.084 0.163 0.33 1

By substituting the data into the system of differential equations, we can obtain curves in Figure 6.

The curves show that the biomass of each species fluctuates to a certain extent, but the overall biomass is relatively stable. At about 800 days, the biomass curve of each species peaks and valleys. The reason why this phenomenon occurs is dry weather occurs more frequently during this period in the weather simulation.

By comparing the biomass-time curves of single species and multi-species, we can find that multi-species can better adapt to drought environment.

5 Community Benefit Model Based on Shannon-Wiener Index

and ICV

5.1 Species Diversity Evaluation Model

Shannon-Wiener Index is a biodiversity index that measures the diversity and abundance of species in an ecosystem. The basic principle is that the higher the diversity of species, the higher the entropy, and vice versa. The higher the entropy, the higher the diversity of species, the higher the diversity of the ecosystem.

We extend the Shannon-Wiener Index to plant communities and use it to evaluate the species diversity of plant communities.

Shannon-Wiener Index (H) can be expressed by Equation (4).

H = −ΣPi · ln(Pi) (4)

where Pi is relative frequency of species i. It can be calculated by Equation (5).

Pi = Ni (5) N where Ni is individual number of species i. N is the total individual number of the plant community.

5.2 Community Stability Evaluation Model

Stability is the necessary condition and function performance of ecosystem, and also one of the important characteristics that determine whether the structure and function of ecosystem can operate normally.When the external interference exceeds the threshold value that the ecosystem can bear, the structure and function of the ecosystem will be changed accordingly, and the stability of the system will be reduced, thus destroying the ecological balance and causing the degradation of the ecosystem [12]. In general, the greater the number of species, the greater the stability.

In this model, we used community stability to assess the benefit of plant species.

Plant community stability is assessed by calculating the inverse of coefficient of variation (ICV ) as Equation (6). ICV = τ (6) σ where τ represents the average biomass of each species and σ represents standard deviation of biomass of each species.

τ can be calculated by Equantion (7).

τ = ΣNi (7) n σ can be calculated by Equation (8).

p Σn i=1(Ni −τ)2 σ = (8)

In particular, plant communities with higher values of ICV possess greater stability compared with those with lower values of ICV [13].

We define the growth rate of ICV as ∆ICV . When ∆ICV > 0, community stability increases. If ∆ICV > 0 is close to 0, community stability is almost unchanged.

5.3 Results

5.3.1 Results of Species Number Effect

Take n = 2, 3, 4, 5, 6, 7 and substitute corresponding data to get biomass-time curve and ∆ICV . The results are shown in Figure 7 and Figure 8.

As can be seen from Figure 8, when n = 5, change rate of Shannon-Weiner Index and ICV is close to 0. As n increases, change rate of Shannon-Weiner Index and ICV is almost constant. Therefore, we can predict that when n ⩾5, the stability of the plant community is almost unchanged. The minimum number of species needed for plant communities to benefit from localized biodiversity is 5.

5.3.2 Results of Species Composition Effect

From Figure 4, we can see that the competition between Species 1 and Species 6 is strong. As for mutualism, there is no strong mutual benefit, but the mutualism between Species 1 and Species 5, Species 1 and Species 10 is stronger than others. We think that different interspecific relationships will influence the ability of plant communities to adapt to drought.

In addition to differences in the relationships between species, drought tolerance of the species itself also influenced the results. When a plant community has species that are not tolerant to drought, the adaptability of the community to drought also changes.

Therefore, We will discuss four cases: strong competition, weak competition, mutualism, and drought intolerant species exist.

Among the 10 plants, we mainly select 7 plants (Species 1 −6 and 10) for analysis. In all cases, the plant community consisted of 5 species (n = 5).

To assess community stability change, we defined the ICV at initial state as ICV1 and at 1600 days as ICV2.

Strong competition:

The species composition in this case is Species 1-4, and 6.

In the data we collected, the quantity of Species 6 in the quadrat with Species 1 as the main body is very small, and the quantity of Species 1 in the quadrat with Species 6 as the main body is very small. From this, we can infer that the competition between populus euphratica and kalidium foliatum is strong.

5 Species’ interspecific influencing factor matrix is shown below.

  1 0.284 0.164 0.093 0.629 −0.165 −0.023 0.284 1 0.336     −0.155 0.164 0.336 1 0.073     −0.165 0.093 0.073 1 0.13   −0.023 −0.155 −0.13 0.629 1

By substituting the data into the system of differential equations, we can obtain curves in Figure 9.

alism (right)

The curves show that the biomass of the other four species except Species 1 increase gradually over time,among which Species 6 become the dominant species. The biomass of Species 1 increases before 1200 days. After 1200 days under the influence of Species 6, its biomass tends to stay the same.

As for community stability, ICV1 = 0.6316, ICV2 = 0.6316. The ICV growth rate is 0.013%.This indicates that community stability is almost unchanged when there is strong competi- tion between species.

Weak Competition:

The species composition in this case is Species 1-5. Among the five species, there is competition, but there are no two species that cannot coexist.

The results is shown in Figure 9.

As for community stability, ICV1 = 0.6348, ICV2 = 0.6384. The ICV growth rate is 0.57%. This indicates that when there is weak competition between species, community stability increases, but the increase is small.

Mutualism:

The species composition in this case is Species 1-3, 5, and 10. Among these five species, more obvious mutually beneficial relationship exist between Species 1 and Species 5, Species 1 and Species 10.

5 Species’ interspecific influencing factor matrix is shown below.

  −0.33 −0.332 1 0.284 0.164 0.284 1 0.336 0.163 0.1     −0.084 0.164 0.336 1 0.4     −0.33 −0.084 0.163 1 0.117   −0.332 −0.1 0.4 0.117 1 By substituting the data into the system of differential equations, we can obtain curves in Figure 9.

The curves show that the biomass of each species show an overall increasing trend. The initial biomass of Species 10 and Species 2 is close. and species 10, Under the mutually beneficial of Species 1, biomass of Species 10 surpasses that of species 2 after about 1200 days.

As for community stability, ICV1 = 0.6415, ICV2 = 0.7936. The ICV growth rate is 23.72%. This indicates that community stability can be improved greatly when there is a strong mutually beneficial relationship between species.

Drought-Intolerant Species Exist:

We also use Species 1-5 for analysis.In this case, we assume that Species 1 and 3 are drought- intolerant.

In the previous article, we defined the optimum growth humidity for plants as 12%. For drought- intolerant plants, we define the optimal growth humidity as 15%. That is, in defining a drought- intolerant species, we simply change m, n, and c values in Equation (2).

When solving differential equations, Q is calculated using Equation (2) for Species 2, 4, and 5. For Species 1 and 3, Q′ is calculated using Equation (9).

Q′ = m′h2 + n′h + c′ (9) We take Q′ = 1 when h = 15%, Q′ = 0 when h = 8% or h = 22%. The calculation results show that m′ = −10000 49 , n′ = 3000 49 , and c′ = −176 49 .

We obtain the curves in Figure 10.

The curves show that the biomass of Species 3 decrease to 0 at about 400 days and that of Species 1 decrease to 0 at about 800 days. The biomass of species 2, 4, and 5 increase steadily. This indicates that drought-intolerant species that are not tolerant to drought will die quickly in arid environment, and the stability of plant community is low.

Result Analysis:

According to the results of the above classification discussion, when the species type is mutually beneficial species, the stability of the plant community can be greatly improved. When the species type is competitive, the plant community can remain basically stable. When drought-intolerant species exist, the plant community can not maintain stable.

6 Potential Impact of Complex Environment

6.1 Frequency and Variation of Drought

6.1.1 Frequency

The frequency of droughts may change. Under the influence of human activities, drought frequency may increase further in the future. To assess the effects of changing drought frequency on drought Species (right)

adaptability of plant communities,we modify the parameters of the simulated weather conditions to make droughts occur more frequently or less frequently.

When there is a greater frequency of occurrence of droughts in weather cycle, the curves in Figure 11 are obtained by substituting the relevant data into the differential equation.

The curves show that when the drought frequency increased, the biomass of all species decreased with time. This suggests that the effect of localized biodiversity on drought adaptability of plant community is limited.

We can speculate that plant community will growing well when droughts are less frequent. However, at the same time, individual plants are less affected by drought. Therefore, when drought frequency is lower, the effect of localized diversity on drought adaptability of plant communities is lower than when drought frequency is higher.

6.1.2 Wider Variation

We define the wider variation of the occurrence of droughts as droughts occur more widely and last longer.

For droughts to occur on a larger scale, it means that drought can extend to areas that should be wet. And the plants that grow in these areas are mostly species that don’t tolerate drought. From the above analysis, drought can be fatal to drought-intolerant plants. It will seriously destabilize the local ecosystem.

For droughts to last longer, we can simulate this by changing the length of weather change cycle. We take 30 days as a weather change cycle. Compared with previous 10 days circle, 30 days circle obviously improve the duration of weather conditions. When the computer-simulated weather conditions are drought, a prolonged drought has a greater impact on plant community.

Changing the weather cycle, we can get the curves in Figure 12.

The curves show that when droughts last longer, in a single time period, the biomass decrease more if the simulation condition is drought. As degradation continues to accumulate, the biomass becomes less and less.

6.2 Adverse Factors

There are many other adverse factors affecting plant communities. Three adverse factors are mainly considered: air pollution, climate warming and habitat reduction. Air Pollution:

Under the influence of human activities, some pollutants are discharged into the atmosphere and gradually accumulate. Air pollution seriously damages the ecosystem. Common air pollutants include dust, smoke, fog and other small particulate pollutants, as well as gaseous pollutants such as SO2 and CO2.

In this model, we mainly consider the effects of SO2 on plant communities.

SO2 has bleaching effect on chlorophyll, which degrades chlorophyll molecules into demag- mochrome without photosynthetic activity, resulting in inhibition of photosynthesis and growth and development. The results shows that the chlorophyll content of plants is negatively correlated with the concentration of SO2 in the atmosphere, and the correlation could be fitted as linear [14]. We inferred that the atmospheric SO2 content would lead to a decrease in plant biomass.

We define the number of indicator to measure the concentration of SO2 as k. k can be represented by Equation (10).

k = c −c0 (10) c where c is current SO2 concentration and c0 is standard value of SO2 concentration. Climate Warming:

In the past century, human beings have been using fossil fuels (such as coal, oil, etc.) in large quantities, which has emitted a lot of CO2 and other greenhouse gases. With the continuous accumulation of greenhouse effect, there is an imbalance between the energy absorbed and emitted by the earth-atmosphere system. As a result, energy accumulates continuously in the earth-atmosphere system, leading to rising temperature and global warming.

Warming affects plant growth by affecting the rate of photosynthesis and respiration. In general, rising temperatures decrease the rate of photosynthesis and increase the rate of respiration. With the further increase of temperature, the rate of respiration decreases.

We assume that warming inhibits plant growth. The annual temperature rise rate can be expressed as dT dt . Habitat Reduction:

With the expansion of cities and the development of industry, large areas of land have been developed and used, making the creatures lose their habitats. At the same time, deforestation, blind clearing, blind grazing of grasslands, irrational development of marshes and construction of water conservancy projects have further reduced the habitat.

Habitat reduction inevitably leads to plant reduction. We define habitat reduction ratio as D.

By combining the above three factors, Equation (3) can be rewritten as Equation (11).

dNj dt = rj · Nj · (1 −D −dT Ni dt −Σaij ) · Q · (1 −k) (11) Kj

We set the standard values of the three factors. k = 0.0167, dT dt = 0.025, and D = 0.08.

In these three factors, we fix two factors unchanged, and change one factor. The changing factors are respectively 1, 2, and 3 times of the standard values.

When k changes, we can get the corresponding biomass-time curve in Figure 13.

The curses show that under the influence of SO2, the biomass of all species decrease with the increase of time. When k gradually increases, the biomass decline rate gradually increases, and even species extinction occurs.

When dT dt changes, we can get the corresponding biomass-time curve in Figure 14.

dt

The effect of temperature rise on biomass is very similar to that of SO2. The biomass of all species decrease with the increase of time. When dT dt gradually increases, the biomass decline rate gradually increases, and even species extinction occurs.

When D changes, we can get the corresponding biomass-time curve in Figure 15.

The curves show that, under the influence of D, the biomass of all species decrease with the increase of time. When D increases, the biomass decline rate increases, but there will be no extinction.

6.3 Result Analysis

Based on the previous analysis, we find that many environmental factors will affect the adaptability of plant communities to arid environments.

Under the influence of most adverse factors, the biomass of plant community show a downward trend and the stability of the plant community is reduced. This indicates that the ability of a plant community to benefit from localized biodiversity,like the self-regulation capacity of ecosystems, has a certain limit. When conditions are harsh, plant community can benefit from localized biodiversity a lot and maintain stable. However, the benefits are not unlimited. As the environment deteriorates further, it can not counteract the effects of the environment on the plant community. The stability of the plant community is disrupted and some species will die out.

7 The Ways to Ensure the Long-term Viability of a Plant Com-

munity Based on AHP

7.1 AHP Model

To analyze the impact and importance of various factors on the long-term survival of plant communities, we use Analytic Hierarchy Process Model to get the weight of each factor.

The analytic hierarchy process is applicable to situations with subjectivity and uncertainty, using experience, intuition and insight logically, which is very suitable for our goal.

We consider the impact of four factors: species number, species type, weather cycle, and other environmental factors. By comparing each influencing factor in pairs, the following judgment matrix can be obtained according to the importance rating.

1   1 2 5 3 3 1 4 6   1 1   1 2   2 4 1 1 1 1 5 6 2

We need to check the consistency of the judgment matrix. It is evaluate by Consistency Ratio (CR). CR can be calculated by Equantion (12).

CR = CI (12) RI

where CI is Consistency Index and RI is Random Index. CI is calculated by Equation (13).

CI = λmax −n (13) n −1

where λmax is maximum eigenvalue of the judgment matrix. The correspondence between n and RI can be obtained by looking up the table.

After calculation, λmax = 4.07 and CR = 0.027 < 0.1. Conformance check pass. The weight of each factor is shown in Figure 16.

7.2 Suggestions for Long-term Viability of Plants

Suggestion 1: The habitats of plants need to match their habits while more mutually bene- ficial plants are advantageous to the community.

According to Figure 16, the types of species has the highest weight. Therefore, to ensure the long-term viability of a plant community, we should first consider species types. As concluded in 5.3.2, plant communities are most stable when the relationships between species are mutualism.

Suggestion 2: Increase the number of species appropriately. Ensure that there are enough number of species in a plant community.

The second highest weight is the number of species. A plant community can benefit from localized biodiversity. As concluded in 5.3.1, the minimum number of species needed for plant communities to benefit from localized biodiversity is 5. Therefore, for long-term viability, the more species, the better adaptability.

Suggestion 3: Everyone is responsible for protecting the environment !

The remaining two factors have less weight and are both related to the environment. In real life, environmental factors cannot be controlled artificially. However, environmental factors are actually directly or indirectly affected by human activities. So please protect the environment, both for ecosystem and ourselves.

7.3 the Impacts on the Larger Environment

The larger environment means more extreme weather changes, numerous types of plants, more complex interspecific interactions, and more influencing factors such as animals, species invasion and so on. Thus in a larger environment, there will be more irregular changing factors. According to our results mentioned before, When there are more external interference factors, the viability of the plant community is worse. So that when in a environment of wider variation, it’s necessary to make sure that the number of species is sufficient and the interactions between them.

8 Sensitivity Analysis

• In our previous model, we have already completed the sensitivity Analysis in each section. We adjust the variation range of various factors, such as the number of species (see Figure 7), the types of species (See Figure 9-10), the frequency and wider variation of drought (see Figure 11-12), and other environmental impacts(see Figure 13-15).

From the figures we can see that the survival conditions and the long-term viability of a plant community change regularly with the change of various factors. So It can be seen that our model has good sensitivity.

• In Figure 17, we analyzed simulated data for 5 species. The x axis is the time of growth, and the y axis is the comparative analysis of the changes of each species over time with respect to their respective initial values, which can be referred to as relative biomass.

It can be seen that in the initial period of simulated drought, the relative biomass of each species changes greatly, and fluctuates up and down with the constant changes of simulated precipitation and simulated air temperature. However, after a period of changes, we observe the chart and find that the range of variation in biomass decreases. This indicates that with the extension of time, all species gradually adapt to the arid environment, and the growth situation gradually tends to be stable. Species become less sensitive to arid environments.

9 Model Evaluation and Further Discussion

9.1 Strength

• Novelty By spearman correlation coefficient, we get the coefficient of different plant species’ distribution. We give the interaction factors between plants based on this, which is very innovative and scientific.

• Comprehensive. In our model, we comprehensively use many classical and scientific mathe- matical models, such as Differential Equation Model for calculating the biomass changes and the AHP Model to evaluate the importance of different factors . We make some adjustments, sim- plification and modifications based on these models and finally build our whole comprehensive model.

• Unified and succinct. The basic framework and equation of our model are the same. When considering more complex factors, we just add parameter to our equation, and the new equation which becomes more complicated can give a good result and the model performs well. The whole Plant Community Prediction Model is unified and succinct.

• Accurate and rigorous. We use Shanno-Wiener index and ICV to specifically quantify the stability and biodiversity of plant communities, which can reflect the drought resistance of communities more accurately. And the specific data can also help us better extend our conclusion to the case of more plant species.

9.2 Weakness

• The numbers AHP Model’s judgment matrix are set subjectively when considering the weight of each factor. So it may be a little empty in objectivity and rationality.

• Real-life data is continuous. Temperature and precipitation are changing all the time. However, computer simulations are difficult to handle continuous data, so we disaggregate the data, which makes continuous data lose some information.

• Because of the time limit, we only analysis several plants which are generally distributed in the same area and have similar growth habits. More experimental evidences is needed from various plant species combination during and after extreme drought events, in order to forecast the susceptibility of trees under climate change. Our results may have some limits and not cover all the situations.

9.3 Further Discussion

There is evidence that under increasing drought stress, species interactions can shift from a positive to a negative interaction because of increasing niche overlap or competition effects. [2] The interaction factors between plants will be affected to some extent such as the soil moisture changes and species’ population density changes. For the next step, we can explore the changes of the interaction factors between plants with drought degree and other factors to improve our model.

10 Appendices

some more text Input Matlab source:

function D=k5 (m, n ) D = n ;

Q1 = weather1 ( ) ; Q2 = weather2 ( ) ; o p t i o n s = odeset ( ’ RelTol ’ ,1E−4, ’ AbsTol ’ ,[1E−5,1E−5,1E−5,1E−5,1E−5]) ; [T ,XYZPQ] = ode45 (@( t , y ) zq5 ( t , y , Q1 , Q2) ,m,D, o p t i o n s ) ; plot (T ,XYZPQ( : , 1 ) , ’ c o l o r ’ , ’#B395DF ’ , ’ LineWidth ’ , 1 . 5 ) ; hold on plot (T ,XYZPQ( : , 2 ) , ’ c o l o r ’ , ’ #86A8E5 ’ , ’ LineWidth ’ , 1 . 5 , ’ L i n e S t y l e ’ , ’−− ’ ) ; hold on plot (T ,XYZPQ( : , 3 ) , ’ c o l o r ’ , ’#CD5C5C ’ , ’ LineWidth ’ , 1 . 5 , ’ L i n e S t y l e ’ , ’−’ ) ; hold on plot (T ,XYZPQ( : , 4 ) , ’ c o l o r ’ , ’#E79FA6 ’ , ’ LineWidth ’ , 2 . 5 , ’ L i n e S t y l e ’ , ’ : ’ ) ; hold on plot (T ,XYZPQ( : , 5 ) , ’ c o l o r ’ , ’#A6B9A1 ’ , ’ LineWidth ’ , 1 . 5 , ’ L i n e S t y l e ’ , ’ −.

’ ) ;

x0 = XYZPQ( end : end , 1 ) ; y0 = XYZPQ( end : end , 2 ) ; z0 = XYZPQ( end : end , 3 ) ; p0 = XYZPQ( end : end , 4 ) ; q0 = XYZPQ( end : end , 5 ) ;

D = [ x0 , y0 , z0 , p0 , q0 ] ;
