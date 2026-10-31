Problem Chosen 2023

MCM/ICM

Summary Sheet

The Comprehensive Prediction Model for Drought-Striken Plant Communities

Summary

Global warming is becoming more and more serious, which has also led to increased drought in some areas. It seriously affects the long-term viability of local plant communities. In order to understand the changing patterns of plant communities in arid regions, we propose three models, a Logistic model that takes into account drought and intermediate interactions, a new model that measures changes in biomass and benefits, and a modified model that takes into account pollution and habitat reduction.

First, we establish a Logistic model considering drought and interspecific interactions to pre- dict the population changes of four plant species in the Tengger Desert, Northwest China. Through the comparison of plant quantity changes under regular and irregular drought cycles, it is found that different plants have different adaptability to drought environment because of their own char- acteristics. At the same time, we find that heavy rainfall followed by rapid drought processes can seriously threaten plant survival.

Second, we use biomass to construct a new model to measure the benefit degree of plant com- munities, and randomly select 2, 3 and 4 species from the four plant species for analysis. On the one hand, we find that as the number of species increases, more and more selected combinations show positive benefits, and the benefits are gradually increasing.On the other hand, we divide the plants into sensitive types and drought-tolerant types, and find that the biomass of sensitive types is more susceptible to fluctuation of drought intensity, while the biomass of drought-tolerant types remain stable under drought, but decrease due to increased competition under sufficient rainfall.

Third, we use the Monte Carlo method to generate two new precipitation distributions with greater and lesser drought frequency and severity, and analyzed four plant species using the pre- vious model. We find that plant biomass remain stable in both conditions, but not in the same amount.

Fourth, we modify the previous model by introducing pollution degree and habitat reduction index, and analyze the changes in the number of four plants again in combination with the actual situation of factory construction. We find that habitat loss has a bigger side effect than pollution, and the combination of the two keeps plant populations lower over time.

Fifth, we conduct sensitivity analysis of some initial parameters of the four plants to explore how these parameters affect the model and simulation experiment.We find that the maximum num- ber of individual plants under ideal conditions has a relatively large effect on the experiment, but it is within the acceptable range. This reflects the robustness of our model.

At last, we optimize the solving method of the model. We use the fourth order Runge-Kutta method to solve the model and get more accurate prediction results. We also use the analysis results to make valuable suggestions on how to improve the viability of plant communities under drought conditions and contribute to environmental governance.

1 Introduction

1.1 Background

At present, the impact of global warming on ecological environment is more and more serious. Climate warming will lead to increased drought and desertification in some areas. Drought-hit areas are not conducive to maintaining biological diversity and species stability. The production and living of people has also been affected.

Take Tengger Desert for example, it is the fourth largest desert in China. In recent years, the phenomenon of desertification near the Tengger Desert cannot be ignored. In addition, groundwater in the Tengger Desert was found to have been polluted for years by factory emissions, seriously affecting the stability of the region’s ecosystem.We use this as a background to explore changes of plant species in drought-hit areas and provide valuable advice for maintaining the long-term viability of plant communities.

(a) A drought-hit area[12] (b) The Tengger Desert[13]

1.2 Problem Restatement

• Establish a mathematical model to predict the changes of plant communities in irregular drought cycles. The model needs to take into account the interactions between plant species.

• Explore how many plant species are needed to benefit a plant community. Describe the variation pattern of plant community benefit degree and species number.

• Explore how different plant types affect changes in the number and benefit of plants under drought cycles.

• Explore how different frequency and degree of drought affect plant community changes. At this point, analyze the effect of the number of plant species on the change of the whole population.

• Explore changes in plant abundance and benefits with drought cycles that take into account changes in environmental pollution and habitat reduction.

• Give advise on maintaining the long-term viability of plant communities and their impact on the environment

1.3 Our Work

According to the requirements, our work is as follows.

2 Assumptions

• When there is no drought and no interaction, the population growth of a species under ideal conditions with sufficient environmental resources conforms to the logistic curve.

• There are only two types of interaction between multiple species: competition and mutual benefit. There are no other complex interactions.

• Suppose that the degree of drought is only related to precipitation, not to other factors.

• Assume that environmental factors other than drought, pollution, habitat loss (such as wind, sunlight, temperature, animals, microorganisms...) are not taken into account.

• The types of plants are divided into sensitive and drought-tolerant types, without considering other types.

• The model is not suitable for extreme weather conditions, such as severe drought and flood.

3 List of Notation

Symbol Meaning xi The number of plants in a single species i ri The growth rate of species i Ni The maximum capacity of species i σij The interspecific relationship index between xj and xi. k(ij) The influence gradient of the interaction index σij and drought stress S. sigma S The degree of drought stress S0 Critical degree of drought stress. P Precipitation Pmax The maximum precipitation Li The maximum growth rate ki The influence gradient between the growth rate of species ri and precipitation P αi The influence gradient between the maximum number of plants Ni and the degree of drought stress S N 0 The ideal maximum number of plants in a single species uner the initial condition i Bi The biomass of species i. n The total number of species k The number of selected species(0 < k <= n) T The total stress degree PO The pollution degree δ The pollution of a single moment µi The purification factor of species i H The impact of habitat reduction A The habitat area A0 The initial habitat area

4 Model Establishment and Solution

4.1 The Model for Predicting Changes in a Plant Community

In this problem, we construct a modified Logistic model that takes into account the interactions between different species and the degree of drought stress. Using this model, combined with mete- orological data from the National Bureau of Statistics[1] and species data from relevant literature[2] , we predicted the population changes of four plant species during several irregular drought cycles in the area around the Tengger Desert in northwest China.

4.1.1 The Establishment of a Modified Logistic Model

Without considering the interaction between species and drought stress, the Logistic model of idealized population growth of a single species is shown in Formula 1.

dxi dt = rixi(1 −xi ) (1) Ni Where xi represents the number of plants in a single species, ri represents the growth rate of the species, and Ni represents the maximum number of plants in a single species under a specific environmental capacity. When considering interspecific relationships, A correction term needs to be introduced, as shown in Formula 2.

dxi dt = rixi(1 −xi xj X − σij ) (2) Ni Nj j

Where σij represents the interspecific relationship index between xjand xi. When σij > 0, the interspecific relationship is competition.The growth rate of species will decrease or even become negative. When σij < 0, the interspecific relationship is mutually beneficial.The rate of increase in the number of plants in a single species will be greater.

The index of interaction between species is also affected by the degree of drought stress. It has been shown that when drought stress is low and water is abundant, the relationships between species tend to be more competitive. When drought stress is high and water resources are scarce, the relation- ship between species tends to be mutually beneficial, so as to meet their own development needs and improve their adaptability in extreme environments. The relationship between the interaction index σij among species and the degree of drought stress S is shown in Formula 3.

σij = −k(ij) sigma(S −S0) (3)

Where k(ij) sigma is the influence gradient of the interaction index σij and drought stress S. S0 is the critical drought stress degree. When the drought stress degree is lower than the critical value, σij > 0. When the drought stress degree is higher than the critical value, σij < 0, the relationship between species is mutually beneficial. Therefore, a reasonable linear relationship between the interaction index of species and the degree of drought stress is established.

The precipitation P is used to describe the degree of drought stress S, and the value range of S is restricted between 0 and 1, as shown in Formula 4.

S(t) = 1 −P(t) (4) Pmax

It can be found that precipitation P is negatively correlated with the degree of drought stress S. Where Pmax is the maximum amount of precipitation in the area over a period of time.

We find that precipitation not only affects the interaction index between species by influencing the degree of drought stress, but also affects the growth rate of each species. Since plants can drown when there is too much rain in arid regions, growth rates do not increase indefinitely, but gradually slow down. So the growth rate is not simply linearly proportional to precipitation. We assume that the growth rate ri has a Logistic relationship with precipitation P , as shown in Formula 5.

Li ri(t) = (5) 1 + e−ki·P(t)

In the formula, Li represents the maximum growth rate of the species, ki represents the influence gradient between the growth rate of the species and precipitation.

In addition, the precipitation P also affects the maximum number of plants in a single species Ni, which is assumed to be linearly positive, as shown in Formula 6.

Ni(t) = (1 −αi(S(t) −S0)) · N 0 (6) i

Where is αi the influence gradient between the maximum number of plants in a single species and the degree of drought stress, and N 0 i is the ideal maximum number of plants in a single species under the initial condition.

By substituting the expression of ri, S, Ni, σij into Formula 2, we can get the differential equation describing the number of plants in a single species as well as the interaction between species and precipitation, and successfully construct the mathematical model.

4.1.2 Population Predictions Using Modified Models

Combined with data from the National Bureau of Statistics[1] and related literature[2], we make population predictions for four plant species in the southeastern Tengger Desert of China. They are Salsola passerina, Reaumuria soongarica, Ceratoides latens and Kalidium foliatum. For convenience, we’d like to call them plant A, B, C and D.

The average monthly precipitation for the region from 2018 to 2021 is shown in Figure 1. We will predict and analyze the changes of the number of four plants in the 48 months through the modified model.

Taking the number of plants in the article as a reference, we analyze the changes in the number of plants in the following 48 months and got the number of four plants in each month. The initial numbers xi of plants A,B,C and D are 34, 34, 29 and 33 respectively.

In addition, according to the different adaptive capacities of the four plants involved in the paper to drought, the initial ideal maximum capacity N 0 i is set proportionally, which is respectively 200, 153, 137, 36. It can be seen that plant D has poor adaptability to drought, so its initial ideal maximum capacity is the lowest.

According to the different root lengths of the four plants in the paper, the maximum growth rate Li can be estimated as 5, 3.5 and 5, 2.5 plants per month respectively. It can be found that the longer the root system is, the stronger the ability to absorb water from the soil and the faster the growth rate. Therefore, this hypothesis is reasonable.

Through data fitting and empirical analysis, the quantitative values of other coefficients in the differential equation model can be reasonably estimated, which are αi = 0.6, S0 = 0.5, k(ij) sigma = 0.002, ki = 0.01, as shown in Table 2.

k(ij) N 0 xi Li αi S0 ki Plant i sigma A 34 200 5 B 34 153 3.5 0.6 0.5 0.002 0.01 C 29 137 5 D 33 36 2.5

Since the time data were discrete, we converted the differential equation into a difference equa- tion, and iterated through matlab to calculate the changes in the number of four plants in the drought cycle, as shown in appendices-Listing 1 and Figure 4(a).

(a) regular drought cycles (b) irregular drought cycles

As can be seen from Figure 4(a), with the change of precipitation in Figure 3, the number of the four plant species will reach the peak in the period of high precipitation, and maintain a relatively low level in the period of low precipitation. At the same time, it can be found that in the peak period of population, the inter-specific competition is intensified, and there are significant differences in the number of the four plants. During periods of precipitation scarcity, all four species would stabilize at a low level and not become extinct due to mutualism. In addition, plant D fluctuates only at a low level due to its weak drought resilience and small initial ideal maximum capacity.

The comparison between Figure 4(a) and Figure 3 further shows that the number of four plants changes dramatically during the period of rapid precipitation changes, especially during the 20th month when the number of plants A,B and C drops sharply. This shows that the rapid drought process will seriously threaten the survival of plants, which provides a certain reference value for desert management in the future.

It can be seen from the precipitation data in Figure 3 that the precipitation changes periodically every year. In order to simulate the extremely irregular drought cycle, we changed the precipitation in the 18th month to one-tenth of the original data, and then used the model to predict the result, as shown in Figure 4(b).

As can be seen from the figure, since the precipitation at this time does not change dramatically in the eighteenth month or so, the number of plants A,B and C will not decline rapidly and will remain at a stable level, indicating that plants are very sensitive to drastic changes in precipitation conditions.

Through the analysis of the changes in the number of four plant species in regular and irregular drought cycles, it is found that the established model has certain robustness. The model is reasonable and accurate, and can reflect the changes of plant quantity in arid areas to a certain extent. It provides a certain reference value for guiding desert planting in the future.

4.2 Further Analysis of the Modified Model

4.2.1 The Relationship between the Number of Species and Benefits

(1)Build Models that Describe the Benefits

To explore the relationship between the number of species and the benefit, we need to measure the benefit according to biomass rather than just the number of plants in different species. Biomass is the total amount of organic matter living in a unit area at any given time. Because each species varies greatly in mass, size, and physiological structure, so does its biomass.

At the same time, we can quantify the benefits mathematically. First, suppose there are n species, and only one species is allowed to grow in the environment. The numerical curves of each species in this environment over time can be obtained by using the established model. Multiply the number of each species by the corresponding biomass. Compare these data at each moment and build a curve using the largest data. The curve is called the baseline, as shown in the formula 7,where xi is the number of a species, Bi is the biomass of the species.

B0(t) = max{Bi · xi(t)|i = 1, 2, 3, · · ·, n} (7)

Next, k of the n species are selected to be placed in the environment. The numerical curves of k species in this environment were obtained by using the model. Multiply the number by the corresponding biomass and sum together to get the change curve of the total biomass. Finally, the difference between the curve and the base line reflects the degree of benefit B, as shown in the Formula 8.

k X Bi · xi(t) −B0(t) B(t) = (8) i=1

Only when B > 0 can the whole plant community get benefits, and different k values can be selected for more detailed analysis.

(2)Make Benefit Analysis according to the Actual Situation

Based on the data from the first question, combined with relevant information from the Bureau of Statistics and literature, a benefit analysis was made for four plant species in Tengger Desert. Due to the differences in plant interaction and ability to adapt to drought, the influence gradient k(ij) sigma mentioned in Formula 3 is also different, and so is the critical degree of drought stress S0. According to the measurement of root-shoot ratio in literature[2], the quantitative values of both can be reasonably estimated and given in matrix form, as shown in formula 9 and 10.Compared with the first question, the data is accurate and reasonable.

  0 0.763 1.10 4.11 1.31 0 1.45 5.39   Ksigma = 0.1 × (9) 0.905 0.691 0 3.72 0.243 0.185 0.269 0

  0 0.523 0.533 0.624 0.318 0 0.544 0.663   S0 = (10) 0.374 0.404 0 0.612 0.466 0.474 0.463 0

In the matrix, K(ij) sigma, S(ij) respectively represents the influence of plant j on plant i, j=1,2,3,4, 0 i=1,2,3,4, The numbers 1, 2, 3, and 4 represent plants A,B,C, and D.

The data in the references for the settings of the other parameters are basically consistent with question 1. Data about biomass B is added in the table

N 0 xi Li B αi ki Plant i A 34 200 5 371.49 B 34 153 3.5 156.32 0.002 0.01 C 29 137 5 230.66 D 33 36 2.5 178.71

At this point, we still assume that αi, ki is a constant relative to the four plants, and we will change it in later problems to get closer to the real situation.

When k=2, two plants are selected from the four plants, and there are six results in total, which are AB, AC, AD, BD, BC and CD respectively. The biomass change curves of each plant were obtained by using the model and compared with the baseline named "single", as shown in Figure 5.

Type AB AC AD BC BD CD B(×104) 2.1257 2.7259 1.2740 -2.8521 -1.0951 -2.2441

By averaging the benefit values at all times, the average benefit of each combination is ob- tained.As can be seen from the Figure 5 and Table 4, when k=2, benefits are positive in three cases, and negative in the other three, and the overall relationship is that B(AC) > B(AB) > B(AD) > 0 > B(BD) > B(CD) > B(BC).

When k=3, three plants ware selected from the four plants, and there are four results in total, which are ABC, ABD, ACD, BCD respectively. The biomass change curves of each plant were obtained by using the model and compared with the baseline named "single", as shown in Figure 6.

Type ABC ABD ACD BCD B(×104) 5.1470 3.6501 4.3094 -0.1416

By averaging the benefit values at all times, the average benefit of each combination is ob- tained.As can be seen from the Figure 6 and Table 5, when k=3, benefits are positive in three cases, and negative in the other one, and the overall relationship is that B(ABC) > B(ACD) > B(ABD) > 0 > B(BCD).

When k=n=4, there is one results in total, which is ABCD. The biomass change curves obtained by using the model and compared with the baseline named "single", as shown in Figure 7.

Under this circumstance, B(ABCD)=6.987×104, which is the largest comparied to k=2 and k=3.

Through the longitudinal comparison of different k values, it can be found that the greater the number of species, the greater the proportion of cases with positive benefits. In addition, the maximum positive benefit increased with the increase of the number of species.

4.2.2 The Effects of Different Species Type

We can divide plants into standard, sensitive and drought-tolerant types. Formula 6 is corrected by multiplying the coefficient βi in front of αi, as shown in Formula 11. βi of standard, sensitive and drought-tolerant types are 1,0.5 and 1.5, indicating the sensitivity of Ni with S.

Ni(t) = (1 −βiαi(S(t) −S0)) · N 0 (11) i

By substituting the revised formula 11 into the differential equation model, a model considering different plant types is established.

(1)The Relationship between Species Type and Population Size (a) Sensitive type (b) Drought tolerant type

(c) Standard type

As can be seen from Figure 8(c), the stability of the standard type is good, and the population remains stable within a certain range when precipitation fluctuates greatly.

It can be seen from 8(a) that the population of sensitive type fluctuates greatly with precipitation and has poor stability. According to 8(b), the population of drought-tolerant types can still maintain a high level when precipitation drops sharply, but there will be an abnormal decline in the period when precipitation rises sharply. This is because when precipitation is higher, the inter-specific competition of drought-tolerant types will be more intense, leading to population decline.

(2)The Relationship between Species Type and Benefits

According to 9(a),9(c) and 9(e), it can be seen that for sensitive type, after reaching stability, with the increase of species number k, the biomass under partial combination conditions increases substantially, and the benefits are also increasing.

From 9(b),9(d),9(f), it can be seen that for drought-tolerant types, after reaching stabilization, with the increase of k, more and more cases still become beneficial, despite the abnormal decline in competition.

As can be seen from Table 6 and 7, the average benefit of sensitive type is greater than that of drought-tolerant type. As the number of species k increased, the benefit of sensitive type increased faster.

(a) k=2, Sensitive type (b) k=2, Drought tolerant type

(c) k=3, Sensitive type (d) k=3, Drought tolerant type

(e) k=4, Sensitive type (f) k=4, Drought tolerant type

Type AB AC AD BC BD CD B of sensitive type(×104) 0.0000 -1.5088 4.0707 0.6203 0.0000 -1.1004 B of drought-tolerant type(×104) 2.4879 3.2105 1.3025 -3.6076 -1.4339 -2.8891

Type ABC ABD ACD BCD B of sensitive type(×104) 0.0000 6.1294 6.6526 2.9947 B of drought-tolerant type(×104) 5.9455 4.0524 4.8102 -0.3003 Further considering the more complex case, when one of the four plants is drought-tolerant and the other three are sensitive, the benefit analysis for k=2,3, and 4 is given, as shown in Figure 10 and Table 8, 9. The results showed that the benefits of mixed types were not much different from those of all drought-tolerant types.

(a) k=2 (b) k=3

(c) k=4

Type AB AC AD BC BD CD B(×104) 2.4735 2.9990 1.1841 -3.4156 -1.3137 -2.8962

Type ABC ABD ACD BCD B(×104) 5.7179 3.9472 4.5077 -0.2993

4.2.3 The Effects of Drought Severity and Frequency

(1)Establish precipitation with different frequency and degree of drought

First draw the frequency histogram of the original 48-month precipitation distribution. The fre- quency of the part with less precipitation was increased through reasonable setting to construct a new frequency histogram,as shown in Figure 11.

(a) The original distribution (b) The new distribution

Each segment in the frequency histogram represents the probability of being in that precipitation interval.

It can be found that each precipitation interval corresponds to a certain probability range, and the sum of these probability ranges is 1. First, using the Monte Carlo method, we randomly generate 60 numbers between 0 and 1, representing 60 months. Secondly, each number will correspond to a probability range, indicating that the precipitation of the day can only be within the corresponding precipitation range of the probability range. Finally, the months falling within the same precipitation range are evenly distributed to get the precipitation of each month, as shown in appendices-Listing 2.

(a) The precipitation with greater drought (b) The precipitation with less drought The Figure 12(a) show the new precipitation distributions with greater drought frequency and degree. By bringing the new precipitation distribution data into the previous model, we can first predict the changes in the number of four plants under the condition of greater frequency and degree of drought, as shown in Figure 13.

In addition, we also use the Monte Carlo method to make a 60-month precipitation distribution with less frequency and degree of drought, as shown in the Figure 12(b).

We compared two conditions of greater and less drought severity and frequency with the number of species k=2,3,4.,and analyzed the effects of drought severity and frequency on the benefits of different species, just the same operation in 4.2.1 and 4.2.2.

With the increase and decrease of drought frequency and intensity, the biomass changes became stable and kept at a high level. As the number of species increases, the biomass becomes more stable.The specific benefit analysis is shown in the Table 10 and 11.

Type AB AC AD BC BD CD B of greater drought(×104) 2.1050 2.7134 1.2109 -2.9592 -1.1804 -2.3689 B of drought-tolerant type(×104) 2.3048 2.8819 1.3063 -3.2511 -1.2454 -2.5550

Type ABC ABD ACD BCD B of greater drought(×104) 5.0631 3.6418 4.2837 -0.1046 B of less drought(×104) 5.5306 3.6953 4.4305 -0.2784

4.2.4 The Effects of Pollution and Habitat Reduction

(1)Establish models that take into account pollution and habitat reduction

When pollution is considered, the total stress degree T is determined jointly by drought degree S and pollution degree PO, as shown in the Formula 12. t is a discrete point in time

T(t) = S(t) + PO(t) (12)

By substituting T for S into the original model, we can obtain the model after taking pollution into account.

The PO of this moment depends on the total PO of the previous moments, the pollution of the last moment and the purification degree of the plant, as shown in Formula 13.

n X PO(t + 1) = PO(t) + δ(t) − µixi (13) i=1

µi refers to the purification factor of plant i. δ is a random result within a small range, ,greater than 0, much less than 1. µi also satisfies this requirement.

We use H to describe the impact of habitat reduction. It can be seen that habitat reduction affects the value of Ni, as shown in the Formula 14.

Ni(t) = N i 0 · H(t) (14)

Where H can be determined by the proportion of habitat reduction, A is the current habitat area and A0 is the initial habitat area, as shown in the Formula 15.

H(t) = A(t) (15) A0 (2)Simulation using real situations

Considering the following real situation, the factory was built in this area from the 25th month. In the following three months, pollution δ remain stable, while the habitat area A decreased with the construction progress. After three months, pollution no longer increased and the habitat area still remain stable, as shown in Table 12.

month [1,24] 25 26 27 [28,48] H 1 0.9 0.8 0.7 0.7 δ 0 [0.02,0.06]

The following is the change in the number of the four plants when only pollution is considered, only habitat change is considered and both are considered, as shown in Figure 16(a), 16(b), 16(c). The code is in appendices-Listing 4.

It can be found that only habitat reduction compared to only pollution shows a significant decline in plant numbers at the 25th month. When both are considered, the number of plants drops sharply to a low level after the 25th month, more severe than the other two situations.

(a) Pollution (b) Habitat reduction

(c) Pollution and habitat reduction

4.2.5 Suggestions to Ensure the Viability of a Community

Firstly, through the change of irregular drought cycle on the number of plants in 4.1.1 and the influence of drought frequency in 4.2.3, it can be found that the growth of plants is better under the condition of adequate precipitation and long-term stability. Therefore, we can ensure the stability and diversity of plant communities by performing appropriate artificial rainfall during dry months.

Secondly, it can be found from 4.2.1 that an appropriate increase in the number of species is also beneficial to ensure the long-term viability of the plant community.In addition, 4.2.2 shows that the number of sensitive types fluctuates greatly with precipitation, while the drought-tolerant types compete strongly in the period of sufficient precipitation. Therefore, the mixed planting of the two types of plants is also conducive to the stability of the community by making use of their strengths and avoiding their weaknesses.

Finally, reducing pollution emissions from nearby areas, improving the living environment in arid areas, and increasing the number of plant habitats will also play a positive role in maintaining the viability of the community.

4.3 Sensitivity Analysis

Considering that some initial parameters of the model do not change during the simulation ex- periment, such as Li, N 0 i and ki. Therefore, based on the mixed type in 4.2.2, we adjusted each of the above parameters of plant A,B,C and D by ±5% and ±10%, and calculated the average total biomass of the four plants in 48 months, as shown in the Figure 17. For accurate quantitative analysis, we calculated the proportion of change in average total biomass when parameters of plants A,B,C and D changed by ±5%,±10%, as shown in the Table 13.

(b) N 0 (a) Li (c) ki i

N 0 Li ki i Plant -10% -5% 5% 10% -10% -5% 5% 10% -10% -5% 5% 10% A(%) 0.164 0.100 0.148 0.366 1.656 0.829 0.829 1.66 B(%) 0.081 0.044 0.051 0.107 3.38 1.69 1.69 3.38 0.071 0.035 0.035 0.070 C(%) 0.094 0.052 0.064 0.144 4.23 2.11 2.11 4.23 D(%) 0.053 0.029 0.033 0.067 0.737 0.369 0.369 0.737

From the data in the Figure 17 and Table 13, it is found that the change of total biomass with N 0 i is relatively obvious. However,the influence of the three parameters on the total biomass is small and within the acceptable range, which reflects the robustness of the model to some extent.

4.4 Optimization of the Model

In 4.1.2, we used a first-order difference equation to solve the changes in the number of four plants over 48 months. Now, the fourth-order Runge-Kutta formula is used to optimize the solu- tion model. The code is shown in the appendices-Listing3.

By comparing Figure 4 and Figure 18, it can be found that the population change in Figure 18 is smoother and does not decrease significantly, so the optimized model can predict the population change more accurately.

5 Model Evaluation

5.1 Strengths

• The Logistic growth model is used to innovatively construct a modified model considering multiple factors such as species interaction, drought degree, pollution and habitat reduction.

• The biomass is used to construct a reasonable model for evaluating the degree of benefit in a certain plant community.

• Use the Monte Carlo Method to build different drought frequency and degree of precipitation distribution.

• The fourth order Runge-Kutta method is used to solve the model. The results are more accurate.

5.2 Weaknesses

• There is no complete consideration of more plant types and number of species.

• The model is not robust to extreme climate.

• Functions of some variables can change from linear to more complex relationships.

Appendices

Here are some partial key code we used in our model as follow.

Listing 1: Prediction of changes in the number of four plants for j = 1:(NumofMonth-1) 1 ri = 0.5*Li./(1+exp(k*D(j))); 2 ksigma = 0.002*ones(4,4); 3 s0 = 0.5*ones(4,4); 4 sigma = -ksigma.*(s(j)-s0); 5 for counti = 1:4 6 for countj = 1:4 7 if countj == counti 8 sigma(countj,counti) = 1; 9 end 10 end 11 end 12 tmp1 = 1- sigma*(x(j,:)./Ni)’; 13 Ni = (1-0.6*(s(j+1)-0.5))*[200 153 137 36]; 14 x(j+1,:) = x(j,:) + x(j,:).*ri.*(tmp1’); 15 end 16

Listing 2: Generate precipitation data with greater frequency and degree of drought clear 1 % genarate a new kind of climate 2 P = xlsread("T and rainfall.xlsx",’sheet2’,’E2:E49’); 3 4 h = histogram(P,0:5:120); 5 times = h.Values; 6 7 f0 = times/sum(times); 8 % stem(2.5:5:117.5,f0) 9 reference0 = cumsum(f0); 10 myrand = rand(60,1); 11 myrainfall0 = zeros(60,1); 12 for i = 1:60 13 for j = 1:24 14 if myrand(i)<=reference0(j) 15 myrainfall0(i) = unifrnd(5*(j-1),5*j); 16 break 17 end 18 end 19 end 20 21 plot(myrainfall0) 22 23 f1 = f0; 24 f1(24) = 0; 25 f1(18) = 0.1*f0(18); 26 f1(3) = f0(3)+0.9*f0(18)+f0(24); 27 reference1 = cumsum(f1); 28 myrand = rand(60,1); 29 myrainfall1 = zeros(60,1); 30 for i = 1:60 31 for j = 1:24 32 if myrand(i)<=reference1(j) 33 myrainfall1(i) = unifrnd(5*(j-1),5*j); 34 break 35 end 36 end 37 end 38 plot(myrainfall1) 39 % save myrainfall1.mat myrainfall1 40 41 f2 = f0; 42 f2(9:10) = f0(1:2); 43 f2(1:2) = f0(9:10); 44 reference2 = cumsum(f2) 45 myrand = rand(60,1); 46 myrainfall2 = zeros(60,1); 47 for i = 1:60 48 for j = 1:24 49 if myrand(i)<=reference2(j) 50 myrainfall2(i) = unifrnd(5*(j-1),5*j); 51 break 52 end 53 end 54 end 55 plot(myrainfall2) 56 % save myrainfall2.mat myrainfall2 57

Listing 3: Optimized model using the fourth-order Runge-Kutta method for j = 1:(NumofMonth-1) 1 ri = 0.5*Li./(1+exp(-k*s(j))); 2 sigma = -ksigma.*(s(j)-s0); 3 for counti = 1:4 4 for countj = 1:4 5 if countj == counti 6 sigma(countj,counti) = 1; 7 end 8 end 9 end 10 % Runge-Kutta method 11 f = zeros(4,4); 12 f(1,:) = fi(x,sigma,Ni,ri,j,0); 13 f(2,:) = fi(x,sigma,Ni,ri,j,f(1, :)); 14 f(3,:) = fi(x,sigma,Ni,ri,j,f(2, :)); 15 f(4,:) = fi(x,sigma,Ni,ri,j,2*f(3, :)); 16 17 x(j+1,:) = x(j,:) + 1/6*(f(1,:)+2*f(2,:)+2*f(3,:)+f(4,:)); 18 for count = 1:4 19 if x(j+1,count)<0 20 x(j+1,count) = 0; 21 end 22 end 23 Ni = (1-0.6*(s(j+1)-0.5))*[200 153 137 36]; 24 end 25 function dx = fi(x,sigma,Ni,ri,j,f) 26 x(j,:) = x(j,:) + 0.5*f; 27 tmp0 = zeros(1,4); 28 for count = 1:4 29 if Ni(count)<1 30 tmp0(count) = 0; 31 else 32 tmp0(count) = x(j,count)/Ni(count); 33 end 34 end 35 tmp1 = 1- sigma*(x(j,:)./Ni)’; 36 dx = x(j,:).*ri.*(tmp1’); 37 end 38

Listing 4: Simulation considering the pollution and habitat reduction for j = 1:(NumofMonth-1) 1 ri = 0.5*Li./(1+exp(-k*T(j))); 2 sigma = -ksigma.*(T(j)-s0); 3 = PO+delta(j)-mu*sum(x(j,:)); PO 4 if PO<0 5 PO = 0; 6 end 7 T(j) = s(j)+PO; 8 for counti = 1:4 9 for countj = 1:4 10 if countj == counti 11 sigma(countj,counti) = 1; 12 end 13 end 14 end 15 f = zeros(4,4); 16 f(1,:) = fi(x,sigma,Ni,ri,j,0); 17 f(2,:) = fi(x,sigma,Ni,ri,j,f(1, :)); 18 f(3,:) = fi(x,sigma,Ni,ri,j,f(2, :)); 19 f(4,:) = fi(x,sigma,Ni,ri,j,2*f(3, :)); 20 21 x(j+1,:) = x(j,:) + 1/6*(f(1,:)+2*f(2,:)+2*f(3,:)+f(4,:)); 22 for count = 1:4 23 if x(j+1,count)<0 24 x(j+1,count) = 0; 25 end 26 end 27 Ni = H(j)*(1-0.6*(T(j)-0.5))*[200 153 137 36]; 28 29 end 30 function dx = fi(x,sigma,Ni,ri,j,f) 31 x(j,:) = x(j,:) + 0.5*f; 32 33 tmp0 = zeros(1,4); 34 for count = 1:4 35 if Ni(count)<1 36 tmp0(count) = 0; 37 else 38 tmp0(count) = x(j,count)/Ni(count); 39 end 40 end 41 42 tmp1 = 1- sigma*(x(j,:)./Ni)’; 43 dx = x(j,:).*ri.*(tmp1’); 44 end 45
