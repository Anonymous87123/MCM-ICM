# P-B-2023-2318300-14fd0bd6

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2023

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | title | pages [1] -->
B

<!-- b000005 | title | pages [1] -->
2318300

<!-- b000006 | prose | pages [1] -->
MCM/ICM

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
0.1 Background: Since its creation in 1961, the Maasai Mara National Preserve has walked a fine line between preserving local flora and fauna, exploring its inherent touristic potential, and catering to the needs of the local Maasai population. Over time, the Kenyan government has advanced policy to attempt to ensure the preserve’s prosperity. This report explores the gamut of policies and management strategies plausibly available for Maasai Mara and presents an optimal solution set for implementation.

<!-- b000009 | prose | pages [1] -->
Our project is a four-part mission. We aim to (1) simulate the Maasai Mara as a dynamic system of interdependent processes across time, balancing the human and environmental factors. We will then (2) perturb model parameters that are within the scope of the Kenyan government and then (3) gauge the resulting long-term behavior changes of the model, thereby making explicit how policy changes affect the Maasai Mara ecosystem. Finally, we will (4) propose actionable policy and management recommendations based on this model, ranked by how much they contribute to total utility in the region. We will also comment on how extensible our model is to other wildlife preserves.

<!-- b000010 | prose | pages [1] -->
0.2 Methods: We modelled 6 interdependent areas of the Maasai Mara preserve: prey, predators, tourism, environ- mental degradation, poaching, and retaliatory killings. The pairs of processes are grouped by thematic affinity. We modelled fauna interactions through a modified Lotka-Volterra system of predator and prey populations. We considered tourism and environmental degradation as macroscopic human influences on the preserve, adapting the minimum model from literature. Finally, localized human effects on fauna were represented by poaching of prey and retaliatory killings of predators, inspired from the Gordon-Schaefer bioeconomic model for fisheries to calculate the effects of poaching as a harvesting of a population.

<!-- b000011 | prose | pages [1] -->
To generate policy we created a utility function to estimate the social benefit of input parameters. The function calculates the long-term behavior of the Maasai Mara system as a function of select key parameters. We then used the L-BFGS-B algorithm to identify parameters that maximize social benefit. Our proposals then targeted each of the most influential parameters, ranked by parameter influence.

<!-- b000012 | prose | pages [1] -->
0.3

<!-- b000013 | heading | pages [1] -->
Results:

<!-- b000014 | prose | pages [1] -->
Our 6 function model was asymptotically stable, facilitating inference of long-term behavior by varying parameters. Out of the 26 parameters in our system, we qualitatively decided on 8 parameters that the Kenyan Tourism and Wildlife Committee could directly influence with government investment. Given a limited budget, the utility function showed that maximum social benefit was achieved by investing primarily in 5 of them, in this order: (1) anti-poaching law enforcement rate per tourists, (2-3) baseline investment in anti-poaching law enforcement, (2-3) baseline investment in the environment, (4) investment in the local population, and (5) opportunity cost of poaching. We developed 13 policies, each targeting specific parameters, and ranked them based on the parameters they modified. Long-term analysis of the system brings confidence in our recommendations.

<!-- b000015 | prose | pages [1] -->
0.4

<!-- b000016 | heading | pages [1] -->
Conclusion:

<!-- b000017 | prose | pages [1] -->
We propose a budget of KSh379 million, a 46% increase over the budget allocated to the preserve in fiscal year 2019 −2020. According to our optimizations, we would see an equilibrium with 24% greater prey count, 78% greater predator count, lower environmental degradation by 19%, reduced retaliatory killings by 97%, and cut poaching rates by 50%, and increase tourism rate by 7.5%.

<!-- b000018 | keywords | pages [1] -->
KEYWORDS: ODEs, utility function, long-term behavior, optimization, stability, Jacobian linearization.

<!-- b000019 | furniture | pages [2] -->
Team 2318300

<!-- b000020 | furniture | pages [2] -->
Page 1

<!-- b000021 | prose | pages [2] -->
The Preservation Equation: A Mathematical Approach to

<!-- b000022 | prose | pages [2] -->
Sustaining the Maasai Mara Preserve’s Ecosystem,

<!-- b000023 | prose | pages [2] -->
Economy, and Communities

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | heading | pages [2] -->
Introduction

<!-- b000027 | prose | pages [2] -->
2

<!-- b000028 | heading | pages [2] -->
Brief overview of our dynamic model

<!-- b000029 | prose | pages [2] -->
3

<!-- b000030 | heading | pages [2] -->
Assumptions

<!-- b000031 | prose | pages [2] -->
4

<!-- b000032 | heading | pages [2] -->
Building our dynamic model

<!-- b000033 | prose | pages [2] -->
5

<!-- b000034 | heading | pages [2] -->
Final model

<!-- b000035 | prose | pages [2] -->
6 Parameter Estimation

<!-- b000036 | prose | pages [2] -->
7

<!-- b000037 | heading | pages [2] -->
Long-term Behavior of Solutions

<!-- b000038 | prose | pages [2] -->
8 Policy

<!-- b000039 | prose | pages [2] -->
9

<!-- b000040 | heading | pages [2] -->
Results

<!-- b000041 | heading | pages [2] -->
10 Sensitivity analysis

<!-- b000042 | heading | pages [2] -->
11 Solution and results

<!-- b000043 | heading | pages [2] -->
12 Discussion

<!-- b000044 | heading | pages [2] -->
13 Conclusion

<!-- b000045 | heading | pages [2] -->
14 Appendix

<!-- b000046 | prose | pages [2] -->
2

<!-- b000047 | prose | pages [2] -->
2

<!-- b000048 | prose | pages [2] -->
3

<!-- b000049 | prose | pages [2] -->
5

<!-- b000050 | prose | pages [2] -->
8

<!-- b000051 | prose | pages [2] -->
8

<!-- b000052 | prose | pages [2] -->
11

<!-- b000053 | prose | pages [2] -->
13

<!-- b000054 | prose | pages [2] -->
18

<!-- b000055 | prose | pages [2] -->
18

<!-- b000056 | prose | pages [2] -->
19

<!-- b000057 | prose | pages [2] -->
20

<!-- b000058 | prose | pages [2] -->
21

<!-- b000059 | prose | pages [2] -->
21

<!-- b000060 | heading | pages [2] -->
15 Report for the Kenyan Tourism and Wildlife Committee

<!-- b000061 | prose | pages [2] -->
22

<!-- b000062 | furniture | pages [3] -->
Team 2318300

<!-- b000063 | furniture | pages [3] -->
Page 2

<!-- b000064 | prose | pages [3] -->
1

<!-- b000065 | heading | pages [3] -->
Introduction

<!-- b000066 | prose | pages [3] -->
Over the last few decades, the Maasai Mara Natural Preserve has faced increasingly severe strains on its natural resources and threats to its existence. There is the challenge of growing tourism while keeping the practice sustainable. Then too, in addition to historical threats such as poaching, new threats like climate change have begun to contribute to the degradation of the Maasai Mara. Additionally, the Maasai people, whose population has exploded from less than 400,000 in 1989 to over 1.1 million today, are an increasingly numerous local stakeholder in the process.

<!-- b000067 | prose | pages [3] -->
Response to these threats has been varied. Since 2005, the Kenyan government has invested in various anti-poaching policies such as dog tracking units.

<!-- b000068 | prose | pages [3] -->
In response to concerns expressed by the Maasai stakeholders themselves, the Kenyan government has created various so-called “Maasai conservancies” adjacent to the park. These conservancies are lands leased from the Mara people for sustainable economic exploration, like tourism. In addition, increased fortification of Maasai bomas (housing units for the Maasai, especially important to protect their cattle from predators) have served to reduce the incidence of revenge killings against species of predators that harass their cattle[7].

<!-- b000069 | prose | pages [3] -->
Given the government’s interest in the prosperity of the Maasai Mara, we wish to investigate what the optimal policies and management decisions for the preserve might be. To this end, we seek to develop a model for the preserve as a dynamic system that takes into consideration the behavior of predator-prey interactions, the tourism-environmental degradation interplay, and the effects on the local fauna resulting from retaliatory killings of predators by the Maasai and poaching of prey. Through this model, we can then predict the changes in the Maasai Mara that results from changes in our inputs, which can then inform policy recommendations for the preserve, and even be extended to other wildlife conservation efforts.

<!-- b000070 | prose | pages [3] -->
2

<!-- b000071 | heading | pages [3] -->
Brief overview of our dynamic model

<!-- b000072 | prose | pages [3] -->
Our model is a dynamic system that encompasses relationships between 6 key processes in the preserve, with their interdependence highlighted in Figure 1 on the next page. These processes are best understood by grouping them into 3 themes:

<!-- b000073 | prose | pages [3] -->
• Fauna population – Predators and Prey: Predator and prey populations are directly dependent on each other, but are also influenced externally: predators by retaliatory killings and tourism, and prey by poaching and migration.

<!-- b000074 | prose | pages [3] -->
Macroscopic Human Influence – Environmental Degradation and Tourism Revenue: Human • presence in the Maasai Mara, overwhelmingly due to tourism, leads to negative large-scale ecosystem impact in the form of environmental degradation. Conversely, this touristic presence can also benefit populations in the area by generating revenue invested in stronger bomas and in preservation efforts.

<!-- b000075 | prose | pages [3] -->
• Localized human effects on the fauna – Retaliatory Killings and Poaching: Local human action also has a measurable effect on the fauna population. Maasai cattle farmers often participate in revenge killings on predators that harass their bomas. Furthermore, many prey animals in the preserve have highly desirable items, making them the target of poaching efforts.

<!-- b000076 | prose | pages [3] -->
The black nodes in the graph of Figure 1 are all the time-dependent processes of the dynamic system. The nodes in orange may help conceptualize the flow of the model, but are not independently modelled processes themselves.

<!-- b000077 | prose | pages [3] -->
Green arrows mean that there exists a positive causal relationship from the origin node to the target node while red arrows mean a negative causal relationship. For example, we modelled that there

<!-- b000078 | furniture | pages [4] -->
Team 2318300

<!-- b000079 | furniture | pages [4] -->
Page 3

<!-- b000080 | caption | pages [4] -->
Figure 1: The dependencies of our model

<!-- b000081 | prose | pages [4] -->
is a green arrow from prey to poaching, meaning a growth in prey implies a growth in poaching. Similarly, there is a red arrow from poaching to prey, meaning a growth in poaching decreases the amount of prey.

<!-- b000082 | prose | pages [4] -->
Also, note that the word “boma” is a contextual term that describes a housing unit typical of the Maasai people, notable for protecting farmers’ cattle from predators.

<!-- b000083 | prose | pages [4] -->
Interpreting this graph, we see that tourism revenue leads to greater investment in bomas (green arrow), which decreases retaliatory killings (red arrow) because predators will be less able to harass cattle, thereby decreasing the incidence of revenge killings.

<!-- b000084 | prose | pages [4] -->
3

<!-- b000085 | heading | pages [4] -->
Assumptions

<!-- b000086 | prose | pages [4] -->
In order to construct our model, we made various simplifying assumptions for the Maasai Mara itself, and for the interactions between each of the processes we modelled in the preservation, as follows:

<!-- b000087 | prose | pages [4] -->
3.1 Maasai Mara

<!-- b000088 | prose | pages [4] -->
M-1. Dynamical uniformity: We treat the Maasai Mara in its entirety as one dynamical system, rather than

<!-- b000089 | prose | pages [4] -->
multiple systems interacting with each other. In reality, areas like the Mara Triangle (which is even administered by a different entity to the rest of the preserve) may present different dynamic patterns.

<!-- b000090 | prose | pages [4] -->
M-2. Mara conservancies The Mara conservancies were all created in the 21st century as alternatives to

<!-- b000091 | prose | pages [4] -->
the natural preserve. Our model does not consider the effect of these conservancies on poaching,

<!-- b000092 | furniture | pages [5] -->
Team 2318300

<!-- b000093 | furniture | pages [5] -->
Page 4

<!-- b000094 | prose | pages [5] -->
tourism, and environmental degradation, though it is likely they do have some effect, by diluting activity beyond just the preserve.

<!-- b000095 | prose | pages [5] -->
3.2 Fauna

<!-- b000096 | prose | pages [5] -->
F-1. Classifying fauna: Fauna will fit into two categories – predators and prey.

<!-- b000097 | prose | pages [5] -->
F-2. Prey growth rate: The population of prey grows in a logistic fashion, limited by a baseline carrying

<!-- b000098 | prose | pages [5] -->
capacity that is negatively affected by the incidence of environmental degradation. That is, greater degradation decreases the carrying capacity for prey.

<!-- b000099 | prose | pages [5] -->
F-3. Predator growth rate: The predator growth rate is proportional to the population of prey. That is,

<!-- b000100 | prose | pages [5] -->
an increase in the amount of prey will lead to predator population growth, as there is more food availability.

<!-- b000101 | prose | pages [5] -->
F-4. Negative external influences on prey population: The prey population is hindered by predators and

<!-- b000102 | prose | pages [5] -->
poaching, both of which are proportional to the current prey population.

<!-- b000103 | prose | pages [5] -->
F-5. Migration rate: The outward migratory rate of prey is proportional to the environmental degradation.

<!-- b000104 | prose | pages [5] -->
Inherent inward migratory rate is taken to be a positive constant. Because environmental degradation is assumed to be periodic, this makes migratory patterns periodic too. Predators are assumed not to follow migratory patterns, so their population is not affected by migration.

<!-- b000105 | prose | pages [5] -->
F-6. Human influence on predators: The predator population is hindered by both retaliatory killings by

<!-- b000106 | prose | pages [5] -->
the Maasai people and tourism, which are both proportional to the current predator population. More predators means a greater likelihood of attacks on farmers’ cattle, while greater tourist populations hinders normal activity of predators.

<!-- b000107 | prose | pages [5] -->
3.3 Tourism

<!-- b000108 | prose | pages [5] -->
T-1. Existence: Tourism is an intrinsic phenomenon. Regardless of the status of the preservation, there

<!-- b000109 | prose | pages [5] -->
will be a non-zero level of tourism.

<!-- b000110 | prose | pages [5] -->
T-2. Tourists do not like crowding: There is an inherent propensity for tourists to prefer less crowded

<!-- b000111 | prose | pages [5] -->
and better maintained destinations, regulated by some “attractiveness” factor. So, few tourists in a destination will attract a proportionally larger amount of new tourists than a large amount.

<!-- b000112 | prose | pages [5] -->
T-3. Environmental Degradation: The only factors that affect tourism are itself (more tourism makes a

<!-- b000113 | prose | pages [5] -->
growth in tourism hard due to the aforementioned crowding) and environmental degradation, which has a negative effect. That is, the presence of poaching or retaliatory killings, and the relative health of fauna populations does not affect tourism.

<!-- b000114 | prose | pages [5] -->
T-4. Uniform behavior: Variation in tourist background and behavior is not modelled; that is, all tourists

<!-- b000115 | prose | pages [5] -->
are assumed to fall under the same bucket, instead of splitting them into luxury travellers, adventure travellers, etc. Their effects are thus also all identical at the individual level.

<!-- b000116 | furniture | pages [6] -->
Team 2318300

<!-- b000117 | furniture | pages [6] -->
Page 5

<!-- b000118 | prose | pages [6] -->
3.4 Environmental Degradation

<!-- b000119 | prose | pages [6] -->
E-1. Effect of Tourism: There is an inherent and proportional negative effect on the environment from the

<!-- b000120 | prose | pages [6] -->
amount of tourists in the preserve.

<!-- b000121 | prose | pages [6] -->
E-2. Investment in Sustainability: A portion of the revenue per tourist is invested in protecting the

<!-- b000122 | prose | pages [6] -->
environment; however, the positive impact of this investment is strictly less than the negative impact of the average pollution per tourist. This way, tourism will maintain a net negative effect on the environment.

<!-- b000123 | prose | pages [6] -->
E-3. Baseline investment: There is a baseline government investment in environmental preservation.

<!-- b000124 | prose | pages [6] -->
E-4. Climate change: Climate change has a fixed positive effect on environmental degradation. In reality,

<!-- b000125 | prose | pages [6] -->
this is a change we expect to increase over time, as global warming becomes worse, rather than a fixed constant.

<!-- b000126 | prose | pages [6] -->
3.5 Poaching

<!-- b000127 | prose | pages [6] -->
P-1. Delay factor: The change in poaching is regulated by a delay of information factor. That is, poachers

<!-- b000128 | prose | pages [6] -->
respond to changes in fauna population with some delay.

<!-- b000129 | prose | pages [6] -->
P-2. Focus of Poaching: Poaching only affects prey. Literature shows that poaching effect on prey is of a

<!-- b000130 | prose | pages [6] -->
significantly higher magnitude than towards predators [7].

<!-- b000131 | prose | pages [6] -->
P-3. textitBaseline investment in anti-poaching: There is a non-zero baseline government investment in

<!-- b000132 | prose | pages [6] -->
anti-poaching measures.

<!-- b000133 | prose | pages [6] -->
P-4. Per capita investment in anti-poaching: A portion of per-tourist income in diverted to anti-poaching

<!-- b000134 | prose | pages [6] -->
law enforcement.

<!-- b000135 | prose | pages [6] -->
P-5. Poaching Feedback loop: The change in poaching is affected by the current level of poaching, as

<!-- b000136 | prose | pages [6] -->
seen in literature[16][9].

<!-- b000137 | prose | pages [6] -->
3.6 Retaliatory Killings

<!-- b000138 | prose | pages [6] -->
RK-1 Effect of Predators: The incidence of the practice is proportional to the number of predators.

<!-- b000139 | prose | pages [6] -->
RK-2 Bomas: A portion of tourism revenue is diverted to investment in the Mara people through the

<!-- b000140 | prose | pages [6] -->
construction of stronger bomas, which reduces the rate of predator attacks on livestock and hence decreases the incidence of retaliatory killings.

<!-- b000141 | prose | pages [6] -->
RK-3 Focus of Retaliatory Killings: Retaliatory killings only affect predators.

<!-- b000142 | prose | pages [6] -->
4

<!-- b000143 | heading | pages [6] -->
Building our dynamic model

<!-- b000144 | prose | pages [6] -->
As components of a dynamic system evolving over time, the processes modelled can naturally be described as ordinary differential equations with respect to time. We created a system of 6 ordinary differential equations to encapsulate these relationships, with the first 2 (predator population and prey population) describing the fauna population, the next 2 (number of tourists and environmental degradation) describing the macroscopic human influence, and the final 2 (poaching likelihood and retaliatory killings likelihood)

<!-- b000145 | furniture | pages [7] -->
Team 2318300

<!-- b000146 | furniture | pages [7] -->
Page 6

<!-- b000147 | prose | pages [7] -->
describing the localized human effects on fauna. Below we elaborate on the model construction process, culminating in the 6 final equations.

<!-- b000148 | prose | pages [7] -->
Note that Table 1 describes all parameters in the equations.

<!-- b000149 | prose | pages [7] -->
4.1 Constructing the equations for fauna population

<!-- b000150 | prose | pages [7] -->
For our predator-prey interactions, we modified the esteemed Lotka-Volterra model, which is widely used to describe the dynamics of biological systems in which two populations interact with one as predator and one as prey [15]. Writing our two equations in the following way makes their relationship to Lotka-Volterra explicit:

<!-- b000151 | prose | pages [7] -->
𝑑Prey

<!-- b000152 | prose | pages [7] -->
Prey

<!-- b000153 | prose | pages [7] -->


<!-- b000154 | prose | pages [7] -->


<!-- b000155 | prose | pages [7] -->
1 −

<!-- b000156 | prose | pages [7] -->
·Prey−ℎ0 ·Predator·Prey−𝛼·Poaching·Prey+𝑚0−𝑚·Degradation

<!-- b000157 | prose | pages [7] -->
= 𝑏

<!-- b000158 | prose | pages [7] -->
𝑘−𝜂· Degradation

<!-- b000159 | prose | pages [7] -->
𝑑𝑡

<!-- b000160 | prose | pages [7] -->
𝑑Predator

<!-- b000161 | prose | pages [7] -->
= ℎ1 · Prey · Predator −𝑑· Predator −(𝛽· Retaliatory Killings · Predator + 𝑆· Tourism · Predator) 𝑑𝑡

<!-- b000162 | prose | pages [7] -->
Here, the Lotka-Volterra model would be the truncation of these two equations to their first two terms[15]. The remaining terms in both equations represent external influences of our overall model on these equations.

<!-- b000163 | prose | pages [7] -->
In the prey model, our extra terms are 𝛼· Poaching · Prey and 𝑚0 −𝑚· Degradation. The first term represents the negative effect of poaching on prey population size. This term is a ”harvest function”, in accordance with the Gordon-Schaefer model for population harvesting in fisheries, which is also widely used to model poaching patterns in a biological population system [12]. The final two terms model migration, where 𝑚0 is the baseline inward migration (positive effect) and 𝑚· Degradation is the outward migration rate modified by environmental degradation (negative effect).

<!-- b000164 | prose | pages [7] -->
In the predator model, our extra terms are −𝛽· Retaliatory Killings · Predator −𝑆· Tourism. Each of these terms represents a different effect, both negative (hence both are subtracted). The first one is the effect of Retaliatory Killings. According to literature, it is common for predators such as lions to attack Maasai cattle, provoking retaliatory killings of the predators[16]. The second term represents the sensitivity of predators to tourist distractions. This is an important consideration to make because tourist presence can indeed disrupt predator mating effectiveness, among other negative influences on their population levels[3]

<!-- b000165 | prose | pages [7] -->
We also made the baseline prey population behave logistically, to avoid a scenario where there are very few predators relative to prey and thus the predator population experiences unrealistically steep Malthusian growth. Here, following examples from literature, we have 𝑏the birth rate of prey, multiplied by a logistic growth equation with carrying capacity 𝑘.[16]. We further chose to offset the carrying capacity by environmental degradation, as it seems reasonable that damages to the ecosystem would decrease its ability to sustain as many animals.

<!-- b000166 | prose | pages [7] -->
4.2 Constructing the equations for macroscopic human influence

<!-- b000167 | prose | pages [7] -->
𝑑Tourism

<!-- b000168 | prose | pages [7] -->
𝐴 = −𝛿· Degradation + Tourism 𝑑𝑡 𝑑Degradation

<!-- b000169 | prose | pages [7] -->
= (𝑃𝑡−𝐼𝑡) · Tourism −(𝐸𝑟+ 𝐼0) + 𝐺 𝑑𝑡

<!-- b000170 | prose | pages [7] -->
The two equations that model tourism revenue and environmental degradation were inspired by the “minimal model” of tourism modelling, which is widely used in literature[11][6][17].

<!-- b000171 | prose | pages [7] -->
This model

<!-- b000172 | furniture | pages [8] -->
Team 2318300

<!-- b000173 | furniture | pages [8] -->
Page 7

<!-- b000174 | prose | pages [8] -->
considers tourist numbers, environmental impact of the tourism, and the revenue generated from their activities. We focused on tourist numbers and environmental degradation.

<!-- b000175 | prose | pages [8] -->
At a glance, looking at the first term of either equation, it is clear that the derivative of tourist population is negatively related to environmental degradation. Similarly, the derivative of environmental degradation is positively related to tourism, barring the circumstance where ecological investment per tourist (𝐼𝑡) outpaces pollution per tourist (𝑃𝑡)(we assumed, however, that this is never the case). That is, the solutions to Tourism and Degradation will be nearly sinusoidal and balanced by each other.

<!-- b000176 | prose | pages [8] -->
Both equations also have additional terms, however, which encode other effects on their values.

<!-- b000177 | prose | pages [8] -->
𝐴 Tourism contains Tourism, which is a regulating factor meant to simulate the attractiveness of a destination that is under-visited. If the Tourism number is too small, this term grows dramatically 𝐴 in size, thus ensuring the equation’s sinusoidal behavior is less radical.

<!-- b000178 | prose | pages [8] -->
Notably, Tourism < 𝐴so 𝐴 simultaneously represents an upper bound on the growth of tourism given a non-improving system.

<!-- b000179 | prose | pages [8] -->
Environmental degradation, on the other hand, includes 𝐸𝑟+ 𝐼0 and 𝐺. The 𝐸𝑟+ 𝐼0 terms represent the baseline recovery rate for the environment (the recovery rate without any outside help) and the baseline government investment in recovery. Thus, clearly both have a negative effect on degradation. 𝐺represents the effects of climate change, which augments environmental degradation independently of all other factors in the equation.

<!-- b000180 | prose | pages [8] -->
These two processes were specifically designed to have an inverse relationship as to simulate the yearly seasonal cycle with respect to both the quality of the environment and the amount of tourists. Data show that the peak of tourism tends to happen in the months of July and August, while from April to May is when the environment is naturally at its lushest due to the influence of the rainy season[10]. The feedback loop created in the equations follows a yearly cycle and the initial conditions, discussed later, have been altered to align these events with their real-world counterparts.

<!-- b000181 | prose | pages [8] -->
Constructing the equations for localized human effects on fauna 4.3

<!-- b000182 | prose | pages [8] -->
𝑑Poaching

<!-- b000183 | prose | pages [8] -->
𝑟𝑝Prey −(Ω + 𝜎𝑝(𝜆0 + 𝜆· Tourism))

<!-- b000184 | prose | pages [8] -->
= 𝛾

<!-- b000185 | prose | pages [8] -->


<!-- b000186 | prose | pages [8] -->
𝑑𝑡

<!-- b000187 | prose | pages [8] -->
𝑑Retaliatory Killings

<!-- b000188 | prose | pages [8] -->
· Poaching

<!-- b000189 | prose | pages [8] -->


<!-- b000190 | prose | pages [8] -->
= 𝑐· Predator −𝐵· Tourism 𝑑𝑡

<!-- b000191 | prose | pages [8] -->
Poaching and retaliatory killings are thematically similar in that they both are negatively related to the fauna population. Specifically, poaching is related to prey population and retaliatory killings are related to the predator population. Note that these equations both yield the average poach or retaliatory kill propensity per day, not the overall number of attacks. The equation for poaching was modified from literature[9] and also draws inspiration from the “harvesting effort” described in the Gordon-Schaefer model[12], as the poaching equation represents the gains from poaching minus the costs, both monetary and otherwise.

<!-- b000192 | prose | pages [8] -->
The revenue from poaching is given by the term 𝑟𝑝·Prey where 𝑟𝑝represents the profit per prey poached. Similarly, Ω + 𝜎𝑝(𝜆0 + 𝜆· Tourism) can be thought of as a cost function for poaching. Its effects on poaching offset the revenue from all poaches cumulatively. Finally, this entire behavior is regulated by 𝛾, which is seen in literature to represent the adaptability of poachers to fluctuations in incentive[9].

<!-- b000193 | prose | pages [8] -->
The total cost is Ω, the opportunity cost of poaching (so the losses from poaching instead of some other activity) added to the overall law enforcement investment (both baseline and generated from tourism revenue) multiplied by 𝜎𝑝, which represents some measure of the risk of poaching. So, we have the relative losses from poaching added to the product of the risk of the activity and law enforcement presence. Since𝑟𝑝 is the revenue per poach, (𝑟𝑝·Prey) is the potential monetary upswing from poaching. So, subtracting this

<!-- b000194 | furniture | pages [9] -->
Team 2318300

<!-- b000195 | furniture | pages [9] -->
Page 8

<!-- b000196 | prose | pages [9] -->
cost function from that amount is an attempt to model the risk assessment of engaging in poaching activities.

<!-- b000197 | prose | pages [9] -->
As for the Retaliatory Killings equation, it is simply the rate of retaliatory killings per predator, 𝑐, multiplied by the number of predators, making it positively related to the overall number of predators. An offsetting term is created from diverting another fraction of tourism income to boma construction, represented by 𝐵, similar to other diversions to mitigating pollution and investing in law enforcement.

<!-- b000198 | prose | pages [9] -->
5

<!-- b000199 | heading | pages [9] -->
Final model

<!-- b000200 | prose | pages [9] -->
Uniting the six previous equations and simplifying the first two results in our dynamic model. All 6 functions are single-variable with respect to time, but we have omitted that time dependency in the system to avoid clutter. Furthermore, when running numerical simulations of the ODEs, we noticed that cycles lasted for approximately 150 units, so we added a damper to the variable 𝑡of 2

<!-- b000201 | prose | pages [9] -->
5 to align each unit of time to one day. This does not impact any of the short or long-term behaviours of the system and was done to facilitate inference. Here is a list of the equations:

<!-- b000202 | prose | pages [9] -->
𝑑Prey

<!-- b000203 | prose | pages [9] -->
Prey

<!-- b000204 | prose | pages [9] -->


<!-- b000205 | prose | pages [9] -->


<!-- b000206 | prose | pages [9] -->


<!-- b000207 | prose | pages [9] -->


<!-- b000208 | prose | pages [9] -->
−ℎ0 · Predator −𝛼· Poaching

<!-- b000209 | prose | pages [9] -->
1 −

<!-- b000210 | prose | pages [9] -->
𝑏

<!-- b000211 | prose | pages [9] -->
=

<!-- b000212 | prose | pages [9] -->
𝑘−𝜂· Degradation

<!-- b000213 | prose | pages [9] -->
𝑑𝑡

<!-- b000214 | prose | pages [9] -->
𝑑Predator

<!-- b000215 | prose | pages [9] -->
· Prey + 𝑚0 −𝑚· Degradation

<!-- b000216 | prose | pages [9] -->
(5.1)

<!-- b000217 | prose | pages [9] -->
= [ℎ1 · Prey −𝑑−𝛽· Retaliatory Killings −𝑆· Tourism] · Predator 𝑑𝑡

<!-- b000218 | prose | pages [9] -->
𝑑Tourism

<!-- b000219 | prose | pages [9] -->
𝐴 = −𝛿· Degradation + Tourism 𝑑𝑡

<!-- b000220 | prose | pages [9] -->
𝑑Degradation

<!-- b000221 | prose | pages [9] -->
= (𝑃𝑡−𝐼𝑡) · Tourism −(𝐸𝑟+ 𝐼0) + 𝐺 𝑑𝑡

<!-- b000222 | prose | pages [9] -->
𝑑Poaching

<!-- b000223 | prose | pages [9] -->
(5.2)

<!-- b000224 | prose | pages [9] -->
(5.3)

<!-- b000225 | prose | pages [9] -->
(5.4)

<!-- b000226 | prose | pages [9] -->
𝑟𝑝Prey −(Ω + 𝜎𝑝(𝜆0 + 𝜆· Tourism))

<!-- b000227 | prose | pages [9] -->
= 𝛾

<!-- b000228 | prose | pages [9] -->


<!-- b000229 | prose | pages [9] -->
𝑑𝑡

<!-- b000230 | prose | pages [9] -->
𝑑Retaliatory Killings

<!-- b000231 | prose | pages [9] -->
= 𝑐· Predator −𝐵· Tourism 𝑑𝑡

<!-- b000232 | prose | pages [9] -->
· Poaching (5.5)

<!-- b000233 | prose | pages [9] -->


<!-- b000234 | prose | pages [9] -->
(5.6)

<!-- b000235 | caption | pages [9] -->
Table 1 lists a summary of all variables used in this system of equations.

<!-- b000236 | prose | pages [9] -->
6 Parameter Estimation

<!-- b000237 | prose | pages [9] -->
There are a total of 26 different parameters in our model, as well as 6 starting conditions (when 𝑡= 0), Values for these parameters were found either from literature (in a one for each modelled process. peer-edited research paper), from data (in official data sets), or calculated (constructed from our model and assumptions), and are listed in tables 2 and 3.

<!-- b000238 | prose | pages [9] -->
6.1 Estimated from literature

<!-- b000239 | prose | pages [9] -->
The initial conditions for Prey, Predator, and Tourism were estimated from literature, with sources generally agreeing on a value of prey count in the low millions, predator count in the few thousands, and an annual tourist rate of about 300,000 visits to the Maasai Mara[7][9][16]. Furthermore, the initial conditions of Poaching and Retaliatory Killings, representing the effort towards poaching and retaliatory killings

<!-- b000240 | furniture | pages [10] -->
Team 2318300

<!-- b000241 | furniture | pages [10] -->
Page 9

<!-- b000242 | caption | pages [10] -->
Table 1: Variables used in the dynamic system with 6 equations

<!-- b000243 | prose | pages [10] -->
Equation Variable

<!-- b000244 | prose | pages [10] -->
(4.1): Prey Prey 𝑏 𝑘 𝜂 ℎ0 𝛼 𝑚0 𝑚

<!-- b000245 | prose | pages [10] -->
(4.2): Predator Predator ℎ1 𝑑 𝛽 𝑆

<!-- b000246 | prose | pages [10] -->
(4.3): Tourism Tourism 𝛿 𝐴

<!-- b000247 | prose | pages [10] -->
(4.4): Environment Degradation 𝐸𝑟 𝐼0 𝑃𝑡 𝐼𝑡 𝐺

<!-- b000248 | prose | pages [10] -->
(4.5): Poaching Poaching 𝛾 𝑟𝑝 Ω 𝜎𝑝 𝜆0 𝜆

<!-- b000249 | prose | pages [10] -->
(4.6): Retaliation Retaliatory Killings 𝑐 𝐵

<!-- b000250 | prose | pages [10] -->
Definition

<!-- b000251 | prose | pages [10] -->
Quantity of prey, in hundred-thousands Birth rate Carrying capacity Effect of degradation on total resources Hunting effect on prey Poaching effectiveness Baseline inwards migration Outward migration damper due to degradation

<!-- b000252 | prose | pages [10] -->
Quantity of predator, in thousands Conversion of prey biomass into predators Death rate Effectiveness of retaliatory killings Sensitivity of predators to tourist distractions

<!-- b000253 | prose | pages [10] -->
Tourist visits, in hundred-thousands Effect of degradation on tourism Tourism saturation damper

<!-- b000254 | prose | pages [10] -->
Degradation relative to baseline Baseline recovery rate Baseline government investment Average pollution per tourist Investment in environment per tourist Impact of climate change

<!-- b000255 | prose | pages [10] -->
Unit of effort exerted by poachers Speed of poaching adjustment Revenue per poach Opportunity cost of poaching Risk of poaching Base law enforcement rate Investment in law enforcement per tourist

<!-- b000256 | prose | pages [10] -->
Unit of effort exerted for retaliation Rate of retaliatory killings per predator Investment in strong bomas per tourist

<!-- b000257 | furniture | pages [11] -->
Team 2318300

<!-- b000258 | furniture | pages [11] -->
Page 10

<!-- b000259 | caption | pages [11] -->
Table 2: Baseline Values for Constants

<!-- b000260 | prose | pages [11] -->
Prey 𝑏 𝑘 𝜂 ℎ0 𝛼 𝑚0 Variables 0.3 120 1 0.05 0.01 1.5 Values

<!-- b000261 | prose | pages [11] -->
Degradation 𝐸𝑟 𝐼0 𝑃𝑡 𝐼𝑡 𝐺 𝛾 Variables 0.5 0.5 0.3 0.1 0.4 1 Values

<!-- b000262 | prose | pages [11] -->
Predator Tourism 𝑚 ℎ1 𝑑 𝛽 𝑆 𝛿 𝐴 0.5 0.05 0.17 0.1 0.01 0.01 0.01

<!-- b000263 | prose | pages [11] -->
Poaching Ret. Kill. 𝑟𝑝 𝜎𝑝 𝜆0 𝜆 𝑐 𝐵 Ω 0.05 0.6 0.01 5 35 0.375 0.5

<!-- b000264 | caption | pages [11] -->
Table 3: Starting condition values

<!-- b000265 | prose | pages [11] -->
Degradation Prey Predator Tourism Processes 34 4 3 Values Poaching Retaliatory killings 3 1.3 15

<!-- b000266 | prose | pages [11] -->
respectively, were chosen with literature in mind and modified to our model’s daily change in 𝑡as opposed to a yearly one[7][9].

<!-- b000267 | prose | pages [11] -->
The birth rate 𝑏is taken by dividing the total number of calves born in a year by the total population of wildebeests and then extrapolated to all prey species[2][14].

<!-- b000268 | prose | pages [11] -->
The hunting effect on prey ℎ0 and the conversion of prey biomass into predators ℎ1 are a modification of values from literature[16]. Notably, our implementations of these values have been reduced significantly due to interpreting 𝑡as change in days rather than years and also include a term for migratory changes, thus reducing the necessity of modelling all increases in prey populations.

<!-- b000269 | prose | pages [11] -->
Our value for effectiveness of retaliatory killings 𝛽, and the investment in strong bomas 𝐵are taken from the literature with slight modifications[16].

<!-- b000270 | prose | pages [11] -->
The values for poaching effectiveness 𝛼, speed of poaching adjustment 𝛾, revenue per poach 𝑟𝑝, opportunity cost of poaching Ω, and for risk of poaching 𝜎𝑝are taken with slight modification from the literature[9].

<!-- b000271 | prose | pages [11] -->
The parameter 𝑆was determined to be relevant from existing literature and the value is calculated relative to the units we chose to use for Prey and Tourism[8].

<!-- b000272 | prose | pages [11] -->
6.2 Estimated from data

<!-- b000273 | prose | pages [11] -->
For 𝑘, which denotes the carrying capacity of the prey in the Maasai Mara ecosystem, we looked at the stable population of wildebeest in the Serengeti-Maasai Mara region and then divided by the proportion of the area of the Maasai Mara relative to the whole region[19].

<!-- b000274 | prose | pages [11] -->
𝜂, which quantifies the sensitivity of the carrying capacity to environmental degradation, was obtained by observing the decline of the population of the wildebeest from 1980 to 2000 [4]. We arrived at a value of a 1% decrease per year.

<!-- b000275 | prose | pages [11] -->
To obtain a value for 𝑚0, we obtained the value from data provided by National Geographic [13].

<!-- b000276 | prose | pages [11] -->
6.3 Calculated

<!-- b000277 | prose | pages [11] -->
The unit-less Degradation initial value was chosen to simulate the seasonal dynamics of the natural ecosystem combined with the seasonal effects of tourism[10].

<!-- b000278 | prose | pages [11] -->
We can calculate the value of 𝐴through the ODE for Tourism. Assuming our constant of integration is 0 for ease of calculation, we can find a relationship between Tourism and 𝐴at a moment in time, as

<!-- b000279 | furniture | pages [12] -->
Team 2318300

<!-- b000280 | furniture | pages [12] -->
Page 11

<!-- b000281 | prose | pages [12] -->
follows:

<!-- b000282 | prose | pages [12] -->
Tourism =⇒Tourism2

<!-- b000283 | prose | pages [12] -->
√

<!-- b000284 | prose | pages [12] -->
𝑑Tourism

<!-- b000285 | prose | pages [12] -->
𝐴

<!-- b000286 | prose | pages [12] -->
≈𝐴𝑡=⇒Tourism ≈

<!-- b000287 | prose | pages [12] -->
2𝐴𝑡

<!-- b000288 | prose | pages [12] -->
≈

<!-- b000289 | prose | pages [12] -->
2

<!-- b000290 | prose | pages [12] -->
𝑑𝑡

<!-- b000291 | prose | pages [12] -->
Which we then set to be around 10−2 to fit existing upwards tourism trends in Kenya. This value is unbounded, but grows at such a pace that it does not become an issue in the model.

<!-- b000292 | prose | pages [12] -->
The remaining values, for 𝑚, 𝑆, 𝐸𝑟, 𝐼0, 𝑃𝑡, 𝐼𝑡, 𝐺, 𝜆0, 𝜆, 𝐶and 𝜎𝑝, were created based on subjective estimations, informed by the literature. [9][7][10][8]. Overall we found the model to not be immensely sensitive to these estimations, and we suggest changing the levels of 𝐼0, 𝑃𝑡, 𝐼𝑡, 𝜆0, and 𝜆during our later analysis.

<!-- b000293 | prose | pages [12] -->
6.4

<!-- b000294 | heading | pages [12] -->
Model Illustration and Analysis

<!-- b000295 | caption | pages [12] -->
Figure 2: Baseline model behaviour

<!-- b000296 | prose | pages [12] -->
Using these baseline constants, we can simulate the model using numerical methods and observe what sort of trends appear.

<!-- b000297 | prose | pages [12] -->
In Figure 2 a clear cyclical nature emerges, reflecting the real world cyclical nature of the Maasai Mara ecosystem. Some things to note should be the discrepancy in units; the predator variable is measured in hundred-thousands, while prey variables are measured thousands of animals. Tourism is measured in 100,000 tourists per year, so about 273 unique new tourists per day. Poaching, retaliatory killings and environmental degradation are abstracted variables. It is important to remember that one unit increase in poaching will not cause a one unit decrease in prey since both have been modelled on different scales. Instead, a one unit decrease in poaching will be multiplied by 𝛼·Prey and then this product will be subtracted from the derivative of prey. This explains why the variation in predators, prey, poaching, and retaliatory killing lines in Figure 2 are of different magnitude. Similarly, the magnitude of environmental degradation has been enhanced so that it is noticeable.

<!-- b000298 | prose | pages [12] -->
7

<!-- b000299 | heading | pages [12] -->
Long-term Behavior of Solutions

<!-- b000300 | prose | pages [12] -->
To propose adequate policy, knowledge of how the parameters affect the long-term behavior of the system is vital.

<!-- b000301 | furniture | pages [13] -->
Team 2318300

<!-- b000302 | prose | pages [13] -->
7.1

<!-- b000303 | heading | pages [13] -->
Existence of Equilibria Solutions

<!-- b000304 | furniture | pages [13] -->
Page 12

<!-- b000305 | prose | pages [13] -->
The model has the following non-trivial nullclines, obtained by setting each differential equation equal to zero and solving for each value in terms of the constants:

<!-- b000306 | prose | pages [13] -->
Tourism = 𝐸𝑟+ 𝐼0 −𝐺

<!-- b000307 | prose | pages [13] -->
𝑃𝑡−𝐼𝑡

<!-- b000308 | prose | pages [13] -->
Since most other nullclines can be expressed as a function of this value of tourism, let 𝜏= 𝐸𝑟+𝐼0−𝐺

<!-- b000309 | prose | pages [13] -->
can then obtain the following nullclines:

<!-- b000310 | prose | pages [13] -->
Predator = 𝐵

<!-- b000311 | prose | pages [13] -->
Deg = 𝐴 𝐶𝜏(= 𝜇)

<!-- b000312 | prose | pages [13] -->
𝛿𝜏(= 𝜔)

<!-- b000313 | prose | pages [13] -->
𝑃𝑡−𝐼𝑡. We

<!-- b000314 | prose | pages [13] -->
Prey = 1

<!-- b000315 | prose | pages [13] -->
 Ω + 𝜎𝑝(𝜆0 + 𝜆𝜏) (= 𝜋)

<!-- b000316 | prose | pages [13] -->
𝑟𝑝

<!-- b000317 | prose | pages [13] -->
To find our nullclines for Poaching and Revenge Killing, let 𝜋equal the above value for Prey, let 𝜇 equal the above value of Pred, and let 𝜔equal the above value for Deg. We then obtain the nullcines as follows:

<!-- b000318 | prose | pages [13] -->
Revenge Killings = ℎ1𝜋−𝑆𝜏−𝑑

<!-- b000319 | prose | pages [13] -->
𝛽

<!-- b000320 | prose | pages [13] -->
Poaching = 1

<!-- b000321 | prose | pages [13] -->
𝜋

<!-- b000322 | prose | pages [13] -->


<!-- b000323 | prose | pages [13] -->


<!-- b000324 | prose | pages [13] -->
1 −

<!-- b000325 | prose | pages [13] -->
𝑏

<!-- b000326 | prose | pages [13] -->
𝛼

<!-- b000327 | prose | pages [13] -->
𝑘−𝜂𝜔

<!-- b000328 | prose | pages [13] -->
(= 𝜐)

<!-- b000329 | prose | pages [13] -->
+ 1

<!-- b000330 | prose | pages [13] -->
 

<!-- b000331 | prose | pages [13] -->


<!-- b000332 | prose | pages [13] -->
−ℎ𝑜𝜇

<!-- b000333 | prose | pages [13] -->
𝛼𝜋(𝑚0 −𝑚𝜔) (= 𝜙)

<!-- b000334 | prose | pages [13] -->
For future simplicity, allow the value of the Poaching nullcline to equal 𝜙. Also, allow the value for the Revenge Killings nullcline obtained above to equal 𝜖. There is a point in which all non-trivial nullclines intersect, allowing us to determine a non-trivial equilibrium point, where the dimensions are listed in the order (Prey, Predator, Tourism, Degradation, Poaching, Retaliatory Killings).

<!-- b000335 | prose | pages [13] -->
𝑏−

<!-- b000336 | furniture | pages [13] -->


<!-- b000337 | prose | pages [13] -->
Ω + 𝜎𝑝𝜆0

<!-- b000338 | prose | pages [13] -->
+ 𝜎𝑝𝜆

<!-- b000339 | prose | pages [13] -->
𝜏, 𝐵

<!-- b000340 | prose | pages [13] -->
𝑐𝜏, 𝐸𝑟+ 𝐼0 −𝐺

<!-- b000341 | prose | pages [13] -->
, 𝐴

<!-- b000342 | prose | pages [13] -->
𝛿𝜏,

<!-- b000343 | prose | pages [13] -->
𝑟𝑝

<!-- b000344 | prose | pages [13] -->
𝑟𝑝

<!-- b000345 | prose | pages [13] -->
𝑃𝑡−𝐼𝑡

<!-- b000346 | prose | pages [13] -->
𝑏𝜋 𝑘−𝜂𝜔−ℎ0𝜇+ 𝑚0 + 𝑚𝜔

<!-- b000347 | prose | pages [13] -->
!

<!-- b000348 | prose | pages [13] -->
, ℎ1𝜋−𝑆𝜏−𝑑

<!-- b000349 | prose | pages [13] -->
(7.1)

<!-- b000350 | prose | pages [13] -->
𝛼𝜋

<!-- b000351 | prose | pages [13] -->
𝛽

<!-- b000352 | prose | pages [13] -->
Note that the third coordinate stated in equation 7.1, representing the equilibrium coordinate of tourism at the point introduced, is written purely as a sum and quotient of the constant coefficient variables from the model which are held constant. This equilibrium point is very useful, as it allows us to linearize the system by calculating the Jacobian at this point.

<!-- b000353 | prose | pages [13] -->
7.2 Eigenvalue Analysis of the Jacobian

<!-- b000354 | prose | pages [13] -->
To find the long-term behaviour of the solutions, we need to find the eigenvalues of the Jacobian of the system at the relevant equilibrium point[15]. We continue to use 𝜏, 𝜋, 𝜔, 𝜐and 𝜙from above. To present the Jacobian in a simpler manner, we have designated 𝑇, Π, and 𝑀as the following equations:

<!-- b000355 | prose | pages [13] -->
2𝜋 Π = ℎ1𝜋−𝑑−𝛽𝜐−𝑆𝜏, 𝑘−𝜂𝜔−ℎ0𝜇−𝛼𝜙, 𝑇= 𝑏−

<!-- b000356 | prose | pages [13] -->
The resulting matrix is our Jacobian:

<!-- b000357 | prose | pages [13] -->
𝑀= 𝛾𝑟𝑝𝜋−𝛾(Ω + 𝜎𝑝𝜆0) −𝛾𝜎𝑝𝜆𝜏

<!-- b000358 | furniture | pages [14] -->
Team 2318300

<!-- b000359 | prose | pages [14] -->
0 −ℎ0𝜋 T

<!-- b000360 | prose | pages [14] -->


<!-- b000361 | prose | pages [14] -->
ℎ1𝜇 −𝑆𝜇 𝚷 −𝐴 0 0

<!-- b000362 | prose | pages [14] -->
𝐽eq =

<!-- b000363 | prose | pages [14] -->
𝜏2 0 0 𝑃𝑡−𝐼𝑡 0 𝛾𝑟𝑝𝜙 −𝛾𝑟𝑝𝜆𝜙 0 𝑐 −𝐵

<!-- b000364 | furniture | pages [14] -->
Page 13

<!-- b000365 | prose | pages [14] -->
𝜂𝜋2

<!-- b000366 | prose | pages [14] -->
0 (𝑘−𝜂𝜔)2 −𝑚 −𝛼𝜋

<!-- b000367 | prose | pages [14] -->


<!-- b000368 | prose | pages [14] -->
0 0 −𝛽𝜇

<!-- b000369 | prose | pages [14] -->
0 0 −𝛿

<!-- b000370 | prose | pages [14] -->
(7.2)

<!-- b000371 | prose | pages [14] -->
0 0 0 0 0 M 0 0 0

<!-- b000372 | prose | pages [14] -->
We can then compute the eigenvalues through software to determine the long-term behavior of the solutions, see Appendix 14 for code. Using the values from Table 2, all six eigenvalues of the Jacobian cal- culated at the non-trivial equilibrium point all indicate asymptotic stability - the real part of all eigenvalues are negative.

<!-- b000373 | caption | pages [14] -->
Figure 3: Long-term model behavior

<!-- b000374 | prose | pages [14] -->
This matches our simulation results, seen in Figure 3. As we increase time to an arbitrarily large value, the six variables seem to converge to stable values as long as the initial values are all positive.

<!-- b000375 | prose | pages [14] -->
Observing Figure 4 we see that the behavior of the system spirals inwards towards the equilibrium point, analogous to the behaviour of a spiral sink in a 2-dimensional system of linear equations. This provides computational confirmation to the asymptotic equilibrium calculations.

<!-- b000376 | prose | pages [14] -->
8 Policy

<!-- b000377 | prose | pages [14] -->
To provide useful policy recommendations, we need to identify which constant coefficients the government is able to directly influence and measure their impact on the different areas of the Maasai Mara preserve. To make rational policy we decided to construct a utility function 𝑈which takes these constants as input variables. We then maximize utility within a reasonable domain and interpret what these results tell us. The last step of policy suggestion is to then combine the objective utility analysis with a subjective analysis of the non-modeled consequences of these policy.

<!-- b000378 | furniture | pages [15] -->
Team 2318300

<!-- b000379 | furniture | pages [15] -->
Page 14

<!-- b000380 | caption | pages [15] -->
Figure 4: Long-term behavior of the prey, predator, and poaching interactions

<!-- b000381 | prose | pages [15] -->
8.1 Parameter Effects

<!-- b000382 | prose | pages [15] -->
To formulate policy, we identified 8 model parameters that government policy is able to influence. These are: 𝐴, 𝐼0, 𝑃𝑡, 𝐼𝑡, 𝜆0, 𝜆, 𝐵, and Ω, see Table 1 for descriptions and Table 2 for the baseline values we chose. Observing the coordinates of the equilibrium point 7.1, we immediately notice that all 8 parameters play a role in determining the location of the equilibrium, emphasising their importance.

<!-- b000383 | prose | pages [15] -->
We begin with the policy parameters that are present in the tourism nullcline, as the effect of tourism cause a domino effect which changes every other aspect of the model, seen in 1. The parameters 𝐼0 (baseline investment), 𝑃𝑡(pollution per tourist), and 𝐼𝑡(investment per tourist) are present in the Tourism nullcline and in our variable 𝜏, so they are natural first candidates to examine. However, since 𝑃𝑡−𝐼𝑡represent a balance, we will only graph 𝑃𝑡vs 𝐼0, and we note that an increase in 𝑃𝑡is analogous to a decrease in 𝐼𝑡, and vice versa.

<!-- b000384 | caption | pages [15] -->
Figure 5: Effect of varying 𝐼0 and 𝑃𝑡on the equilibrium

<!-- b000385 | furniture | pages [16] -->
Team 2318300

<!-- b000386 | furniture | pages [16] -->
Page 15

<!-- b000387 | prose | pages [16] -->
As seen in Figure 5, varying the values of 𝑃𝑡and 𝐼0 have a significant effect on the nullcline of Tourism. As 𝑃𝑡increases, the equilibrium of Tourism decreases significantly with only minor changes in the value, implying a negative correlation between the two values. Similarly, as 𝐼𝑡increases, the equilibrium of Tourism increases significantly, implying a positive correlation between the two values. As 𝐼0 increases in our model, the equilibrium point for Tourism shifts upwards, implying a positive correlation between the two values. Notably, variation of 𝑃𝑡has a much greater effect the equilibrium value than 𝐼0.

<!-- b000388 | caption | pages [16] -->
Figure 6: Effect of varying 𝜆0 and 𝜆on the equilibrium

<!-- b000389 | prose | pages [16] -->
Next, we can analyze the effects that changes in base law enforcement rate 𝜆0 and the law enforcement rate per tourist 𝜆have on our equilibrium solution for both Prey and Poaching, as seen in Figure 6. Increasing 𝜆0 has the effect of increasing the stability of our solution and shifting our Prey solution upwards and our Poaching solution downwards, as expected. 𝜆also has a similar effect, but with much greater effect. In fact, in the bottom scenarios, large increase in 𝜆leads to a drastic decrease in poaching and a drastic increase in Prey. Notably, the effect of increasing 𝜆on our solutions is much greater than the effect of increasing 𝜆0.

<!-- b000390 | prose | pages [16] -->
Finally, we can analyze the effects of changing 𝐴and 𝐵, which represent the tourism saturation damper and the strength of bomas, respectively, as seen in Figure 7. Notably, varying 𝐴does not seem to have a noticeable effect on the equilibrium solutions, since the graphs do not vary vertically. On the other hand, 𝐵has a significant effect on both stability of the system and the equilibrium solutions for Predator, Retaliatory Killings, and Tourism. Namely, as B increases, the average rate of retaliatory killings drops significantly indicating a negative relationship, while the equilibrium population of predators sees a marked increase, indicating a positive relationship. Tourism remains unchanged.

<!-- b000391 | prose | pages [16] -->
8.2 Utility function

<!-- b000392 | prose | pages [16] -->
The utility function 𝑈takes as input the 8 parameters we mentioned in Section 8.1, calculates the long- term behavior of the system, calculates a the cost of implementing these parameters based off of a set of pre-determined weights, then returns an arbitrary ’social benefit’ weighing the impacts on the fauna, tourism, the environment, poaching, the interests of the Maasai population, and the implementation cost. Policy construction is a subjective field and by balancing the weights we can change the emphasis

<!-- b000393 | furniture | pages [17] -->
Team 2318300

<!-- b000394 | furniture | pages [17] -->
Page 16

<!-- b000395 | caption | pages [17] -->
Figure 7: Effect of varying 𝐴and 𝐵on the equilibrium

<!-- b000396 | prose | pages [17] -->
of different areas within the preserve. The way we measure long-term behavior will be through analysing the values of our six main variables at the equilibrium point seen in equation 7.1. Let Prey𝑒𝑞represent the value of the Prey variable at the equilibrium, extrapolating to the other five main variables we get the vector ®𝑌. We then represent the weights as ®𝑤and the 8 influential parameters as ®𝑋. It is vital to note that the values of ®𝑌depend on the values of ®𝑋since the equilibrium point is affected by the values in ®𝑋.

<!-- b000397 | prose | pages [17] -->
Prey𝑒𝑞

<!-- b000398 | prose | pages [17] -->
𝐴

<!-- b000399 | prose | pages [17] -->


<!-- b000400 | prose | pages [17] -->


<!-- b000401 | prose | pages [17] -->


<!-- b000402 | prose | pages [17] -->
𝑤0

<!-- b000403 | prose | pages [17] -->


<!-- b000404 | prose | pages [17] -->


<!-- b000405 | prose | pages [17] -->


<!-- b000406 | prose | pages [17] -->
Predators𝑒𝑞

<!-- b000407 | prose | pages [17] -->
𝐼0

<!-- b000408 | prose | pages [17] -->
®𝑋=

<!-- b000409 | prose | pages [17] -->
®𝑌= ,

<!-- b000410 | prose | pages [17] -->
...

<!-- b000411 | prose | pages [17] -->
𝑤1

<!-- b000412 | prose | pages [17] -->
, ®𝑤=

<!-- b000413 | prose | pages [17] -->
... ...

<!-- b000414 | prose | pages [17] -->
...

<!-- b000415 | prose | pages [17] -->
Retaliatory Killings𝑒𝑞

<!-- b000416 | prose | pages [17] -->
Ω

<!-- b000417 | prose | pages [17] -->
𝑤5

<!-- b000418 | prose | pages [17] -->
We may then construct the utility function 𝑈which takes ®𝑋as input

<!-- b000419 | prose | pages [17] -->
𝑈( ®𝑋) = ®𝑌· ®𝑤−𝐶𝑜𝑠𝑡( ®𝑋), 𝐶𝑜𝑠𝑡( ®𝑋) ≈𝑐( ®𝑋· ®𝑋)

<!-- b000420 | prose | pages [17] -->
Where 𝐶𝑜𝑠𝑡represents the cost of implementing these policies and 𝑐is a weight. We chose to model cost quadratically, with some slight alterations due to the different magnitude of variables, to simulate diminishing returns, but similar results were seen when modelling costs exponentially. We then implement these functions in software, see Appendix 14 for code.

<!-- b000421 | prose | pages [17] -->
8.3 Policy Generation

<!-- b000422 | prose | pages [17] -->
To generate policy suggestions, we need to report on optimum allocation of resources into each of the 8 parameters. Optimum allocations arises from maximizing the utility function, which was done by

<!-- b000423 | heading | pages [17] -->
implementing a “limited memory quasi-Newton algorithm for solving large nonlinear optimization

<!-- b000424 | prose | pages [17] -->
problems with simple bounds on the variables” referred to as L-BFGS-B[5]. This algorithm is vital for our problem due to the boundary constraints of our variables.

<!-- b000425 | furniture | pages [18] -->
Team 2318300

<!-- b000426 | furniture | pages [18] -->
Page 17

<!-- b000427 | prose | pages [18] -->
Determining the weight vector ®𝑤is a subjective activity. We chose to heavily prioritise prey, predator, and tourist count by weighing 𝑤0 = 106, 𝑤1 = 103, and 𝑤2 = 106, effectively turning the sum of these terms into an estimation of the total fauna population of the Maasai Mara and total yearly tourist count. Poaching was given a weight of 𝑤3 = 0 to discourage it, and retaliatory killings were given a large negative weight of 𝑤4 = −103 since they are a proxy to represent the attack of predators on Maasai livestock and one of our key considerations are the needs of the Maasai population. Environmental degradation has arbitrary units and fluctuates with tourism, so was given a similar weight. Finally, we looked at the current government budget and estimated the total amount of KSh invested into the Maasai Mara to determine 𝑐= 5 · 105.

<!-- b000428 | caption | pages [18] -->
Table 4: Utility function output

<!-- b000429 | prose | pages [18] -->
𝐴 𝐼0 𝑃𝑡−𝐼𝑡 𝜆 Parameters 0.01 8.71 0.01 27.1 Values 100k 87.1m 100k 271m Cost (KSh) Total Investment 𝜆0 𝐵 Ω 8.71 1.19 0.950 ... 87.1m 11.9m 9.50m ∼KSh379 million

<!-- b000430 | prose | pages [18] -->
Based on Table 4, by far the most important parameter to invest in is 𝜆, (the unit investment in anti- poaching measures per 100 thousand tourists). 𝐼0 (baseline government investment) and 𝜆0 (base law enforcement rate) are the next most important parameters to invest in, following by 𝐵(boma strength) and Ω (opportunity cost) as the third priority. Finally, we have the balance 𝑃𝑡−𝐼𝑡and 𝐴. Investing in increasing the opportunity cost of poaching is rather abstract, but we interpreted this as bolstering the local economy such that potential future poachers decide to adopt civilian professions instead.

<!-- b000431 | prose | pages [18] -->
One immediately notices that the estimated investment cost across parameters is just the value of the parameter multiplied by the weight 𝑐. This is a current flaw of the model which has a general cost weight instead of one per parameter.

<!-- b000432 | prose | pages [18] -->
8.4 Subjective Policy

<!-- b000433 | prose | pages [18] -->
Based on the results from the utility function, it is apparent that 𝐴and 𝑃𝑡−𝐼𝑡were only allocated a modicum of investment, and thus, given a limited budget, shifting their values does not increase utility relatively much. Therefore, we have decided not to consider policy that specifically tackles those parameters, focusing instead on the others, ordered from largest to smallest budget allocations:

<!-- b000434 | prose | pages [18] -->
1. 𝜆: (Anti-poaching law enforcement rate per tourists)

<!-- b000435 | prose | pages [18] -->
(a) Diverting a portion of tourism revenue to the purchasing of anti-poaching equipment.

<!-- b000436 | prose | pages [18] -->
(b) Implement a large donation campaign for the training and deployment of an anti-poaching force

<!-- b000437 | prose | pages [18] -->
and advertise it among tourist areas.

<!-- b000438 | prose | pages [18] -->
(c) Require tourist establishments that operate within the preserve to provide CCTV footage of the

<!-- b000439 | prose | pages [18] -->
areas around their lodging to the anti-poaching force.

<!-- b000440 | prose | pages [18] -->
2. 𝜆0: (Baseline investment in anti-poaching law enforcement)

<!-- b000441 | prose | pages [18] -->
(a) Increased investment in transportation infrastructure for rangers to intercept poachers, including

<!-- b000442 | prose | pages [18] -->
the gravelling of roads and airstrips.

<!-- b000443 | prose | pages [18] -->
(b) Establish training programs in anti-poaching practices for rangers to specialize in.

<!-- b000444 | furniture | pages [19] -->
Team 2318300

<!-- b000445 | furniture | pages [19] -->
Page 18

<!-- b000446 | prose | pages [19] -->
(c) Establish lodging specific for anti-poachers close to the preserve.

<!-- b000447 | prose | pages [19] -->
3. 𝐼0: (Baseline investment in the environment)

<!-- b000448 | prose | pages [19] -->
(a) Increased investment in environment protecting infrastructure, including dams, solar panels,

<!-- b000449 | prose | pages [19] -->
and the Maasai Stoves & Solar initiative.

<!-- b000450 | prose | pages [19] -->
(b) Incentivize the development of eco-friendly infrastructure in tourist establishments.

<!-- b000451 | prose | pages [19] -->
4. 𝐵: (Investment in the local population)

<!-- b000452 | prose | pages [19] -->
(a) Directly fund the identification and strengthening of the bomas most vulnerable to predators.

<!-- b000453 | prose | pages [19] -->
(b) Promote open-air markets for families to have better access to high-quality construction mate-

<!-- b000454 | prose | pages [19] -->
rial.

<!-- b000455 | prose | pages [19] -->
(c) Invest in the existing Maasai Stove & Solar initiative.

<!-- b000456 | prose | pages [19] -->
5. Ω (Opportunity cost of poaching)

<!-- b000457 | prose | pages [19] -->
(a) Plan the transformation of Narok Town into a resort city through infrastructure, branding, and

<!-- b000458 | prose | pages [19] -->
development incentive policy for investors.

<!-- b000459 | prose | pages [19] -->
(b) Open trade schools and apprenticeship programs for technical professions in the region.

<!-- b000460 | prose | pages [19] -->
(c) Highlight the national importance of the preserve through cultural festivals.

<!-- b000461 | prose | pages [19] -->
9

<!-- b000462 | heading | pages [19] -->
Results

<!-- b000463 | prose | pages [19] -->
According to the optimization conducted in Section 8.3, we would suggeset the optimal investments seen in Table 4. Comparing a model with the original coefficients we determined in Table 2 to ones with the optimal coefficients lead to and equilibrium point with 24% greater prey count, 78% greater predator count, lower environmental degradation by 19%, reduce retaliatory killings by 97%, and cut poaching rates by 50%, and increase the average yearly expected tourists by 7.5%. See code in Appendix 14 for how these numbers were derived.

<!-- b000464 | prose | pages [19] -->
10

<!-- b000465 | heading | pages [19] -->
Sensitivity analysis

<!-- b000466 | prose | pages [19] -->
To have confidence in our mathematical model we must show its robustness through sensitivity analysis. We conducted a One-At-a-Time (OAT) sensitivity analysis on the input parameters for the model. We perturbed each variable throughout their maximum range and then calculating the eigenvalues of the Jacobian at the non-trivial equilibrium point discussed in 7.2. This provides insight on how each variable affects the long-term behaviour of the system. See Appendix 14 for code.

<!-- b000467 | prose | pages [19] -->
Iterating over each of the parameters individually reveals that adjusting the majority of the parameters does not change the classification of the equilibrium point. The exceptions are 𝐼𝑡, 𝑃𝑡and 𝑚, which require 𝐼𝑡< 𝑃𝑡and 𝑚< 53.77. Breaking these rules causes an unstable equilibrium. The first condition, 𝐼𝑡< 𝑃𝑡, is part of our assumptions. The restriction on 𝑚is due to the fact that excessive migrations will cause the system to go over the logistic limit of growth we had as an assumption.

<!-- b000468 | furniture | pages [20] -->
Team 2318300

<!-- b000469 | furniture | pages [20] -->
Page 19

<!-- b000470 | prose | pages [20] -->
11

<!-- b000471 | heading | pages [20] -->
Solution and results

<!-- b000472 | prose | pages [20] -->
11.1 Generalizing to other wildlife management areas

<!-- b000473 | prose | pages [20] -->
Our model can be reasonably generalized to other wildlife preservations simply by modifying parameters to the new context, with some considerations in mind:

<!-- b000474 | prose | pages [20] -->
1. The environment we are modelling is a relatively small, somewhat homogeneous preserve, allowing us to treat the entire area as one cell. For larger, more variable preserves, it may be necessary to split the location up into smaller cells and then model each one individually.

<!-- b000475 | prose | pages [20] -->
2. Our model considers the effects of adjacency to a large, autonomous local population, by modelling revenge killings and boma investments. These phenomenon, however, are unique to the Maasai Mara, so any generalization would require modification. For example, in other preserves, our term for boma strength, which is directly proportional to the investment into the local populace, could be replaced by a direct investment in the local populace term. Similarly, the term for revenge killings can be replaced by a term that details the effects of poaching on predators.

<!-- b000476 | prose | pages [20] -->
3. The Maasai Mara budget is limited by the funds of the Narok County local government, which is quite low. Meanwhile, in places with much higher budgets, new technologies or ideas can be plausibly explored which change how efficiently government investment is used. As such, modeling any such wildlife preserve would require rethinking how exactly government investment affects the different players.

<!-- b000477 | prose | pages [20] -->
4. The makeup of the flora and the fauna is a key consideration. In our case, we included poaching as a factor since the Maasai Mara is an ecosystem that is conducive to poaching. Other ecosystems, however, do not necessarily suffer from poaching. On the other hand, our model does not take into account other threats such as the presence of invasive species, which is a monumental threat in various national parks[1]. As such, our model is best suited for parks that suffer from poaching but not from other large-scale threats such as invasive species.

<!-- b000478 | prose | pages [20] -->
11.2

<!-- b000479 | heading | pages [20] -->
Strengths and weaknesses

<!-- b000480 | prose | pages [20] -->
11.2.1

<!-- b000481 | heading | pages [20] -->
Strengths

<!-- b000482 | heading | pages [20] -->
1. The dynamic system had an asymptotically stable equilibrium for our parameter selection,

<!-- b000483 | prose | pages [20] -->
which improves inference ability and allows far better analysis of how changing parameters affects the entire system.

<!-- b000484 | heading | pages [20] -->
2. Our model has a clear periodic oscillatory behavior. This mirrors how, in reality, the Maasai

<!-- b000485 | prose | pages [20] -->
Mara has an intense fauna migratory period from July to October, which thus also concentrates most tourism activities and poaching efforts during this period.

<!-- b000486 | heading | pages [20] -->
3. Our systems of differential equations were heavily inspired by literature, specifically the Lotka-

<!-- b000487 | prose | pages [20] -->
Volterra equations, the Gordon-Schaefer model for bioeconomic population harvesting, and the

<!-- b000488 | prose | pages [20] -->
minimal model of tourism. All 3 of these models are tried-and-tested in the field, leading a strong backbone to our processes.

<!-- b000489 | furniture | pages [21] -->
Team 2318300

<!-- b000490 | furniture | pages [21] -->
Page 20

<!-- b000491 | prose | pages [21] -->
11.2.2

<!-- b000492 | heading | pages [21] -->
Weaknesses

<!-- b000493 | heading | pages [21] -->
1. Our model groups all fauna into two simple “predator” and “prey” buckets. It is true that

<!-- b000494 | prose | pages [21] -->
large-scale biodiverse ecosystems can indeed be modelled by processes similar to Lotka-Volterra, but such a simplification does disregard certain nuances like how large predators primarily hunt large prey.

<!-- b000495 | heading | pages [21] -->
2. In our system, environmental degradation and tourism are not causally influenced by any of the

<!-- b000496 | prose | pages [21] -->
other processes, being influenced exclusively by each other. This does not match the likely behavior of these processes in reality. For example, most tourism in the area is ecological, to observe the fauna – so, if the fauna population becomes far smaller, we would expect tourism to decrease as well. Similarly, a decrease in fauna ought to create ecosystem imbalances that may lead to increased environmental degradation.

<!-- b000497 | heading | pages [21] -->
3. We assumed that the pollution generated per tourist is always larger than the investment revenue

<!-- b000498 | prose | pages [21] -->
generated per tourist, so that tourism always has a direct negative effect on the environment. So, this does not allow us to consider policies that may lead to reinvesting enough tourism revenue or decreasing tourism pollution sufficiently that investment per tourist outmatches pollution per tourism.

<!-- b000499 | heading | pages [21] -->
4. We modelled the effects of climate change as a deterministic constant, 𝐺. In reality, climate

<!-- b000500 | prose | pages [21] -->
change ought to be a function of time, as it will tend to become more pronounced with time. Additionally, the effect itself is not a chronic influence, but more likely a continuous stochastic process that peaks at random intervals representative of climate catastrophes. Because we did not model 𝐺this way, we cannot propose policies for increased climate resiliency for the preserve.

<!-- b000501 | prose | pages [21] -->
5. The Maasai people population has grown from under 400,000 in 1989 to over 1.1 million today.

<!-- b000502 | prose | pages [21] -->
However, we did not model this population growth at all, even though it is clear a larger population likely leads to more retaliatory killings and indeed even to more environmental degradation.

<!-- b000503 | heading | pages [21] -->
6. In the utility function, we assumed that a 1 unit increase in the parameters we are fluctuating

<!-- b000504 | prose | pages [21] -->
costs the same across all parameters. This does not match reality, where some variables may be substantially harder to change through policy (like Ω, which is the opportunity cost of poaching, changeable by making the economy generally more prosperous).

<!-- b000505 | prose | pages [21] -->
12

<!-- b000506 | heading | pages [21] -->
Discussion

<!-- b000507 | prose | pages [21] -->
Based on our model, we found that the most effective form of investment would be one that increases the 𝜆parameter, which is the relative amount of investment into anti-poaching activities based on the amount of tourism. Second to that, baseline investments into 𝜆0 and 𝐼0 were also considered vital, representing investment into anti-poaching infrastructure and environmental protection infrastructure respectively. In addition to our numerical analysis, however, there are some subjective factors that are important to consider.

<!-- b000508 | prose | pages [21] -->
12.1

<!-- b000509 | heading | pages [21] -->
Subjective analysis of the effects of our recommendations on the Mara people

<!-- b000510 | prose | pages [21] -->
The effect of our policy recommendations on the Mara people is modeled through the incidence of retaliatory killings. Policy recommendation 4 is an increased investment in the strength of bomas, which would result in a decrease in the incidence of retaliatory killings decreases, subsequently decreasing cow losses from the Mara people. This indirectly models the benefit of investment into the Mara people, since

<!-- b000511 | furniture | pages [22] -->
Team 2318300

<!-- b000512 | furniture | pages [22] -->
Page 21

<!-- b000513 | prose | pages [22] -->
the investment into bomas is implicitly modeled as a proportion of overall investment. However, this does not fully capture the effects of our policy recommendations on them. For example, some of the investment into the Mara could easily be diverted into higher quality water, better education, and the Stoves & Solar program. While this would result in a smaller increase in boma strength, the overall estimated social benefit would be higher. As such, the overall effect on the Mara is likely more significant that what is modeled.

<!-- b000514 | prose | pages [22] -->
12.2

<!-- b000515 | heading | pages [22] -->
Subjective analysis of the economic effects of our recommendations

<!-- b000516 | prose | pages [22] -->
When analysing the local economy we need to hold two factors into consideration, policy impact on tourism and direct policy of investment in the local economy. Tourism is the main economic driver of the region around the Maasai Mara and it a vital parameter to consider when analyzing changes in the ecosystem [10]. The human effect of a reduction in tourism is massive, not only is the local economy damaged by the decrease in its main industry, but the national economy of Kenya as a whole. This human effect was observed and quantified during the COVID-19 pandemic, and the consequences are something we held in consideration when analysing the intricate balance between tourism and the environment [18]. None of our subjective suggested policy in Section 8.4 outline investments which would directly increase the attractiveness of the Maasai Mara to tourists, but the changes we suggest include a significant increase in 𝐼0 which, according to our assumptions and model, would have a secondary impact on tourism. Two of the 5 main policy we outlined were investment into the local population and local economy. Direct investment in infrastructure is a more guaranteed method of uplifting the local economy compared to investing in tourism. Furthermore, investing in anti-poaching infrastructure also strengthens the local economy due to use of local labor and potentially even local materials. Pairing policy points 4.b) and 2.c) go hand-in-hand, as 4.b) facilitates the development of construction industries in the local area and 2.c) invests in infrastructure that requires construction.

<!-- b000517 | prose | pages [22] -->
13

<!-- b000518 | heading | pages [22] -->
Conclusion

<!-- b000519 | prose | pages [22] -->
Based on our model, we propose a budget of KSh379 million, a 46% increase over the budget allocated to the preserve in the fiscal year 2019 −2020. This was derived through rational means, but required a significant amount of subjective analysis. According to our optimization of the distribution of this budget, over the long term this investment would result in 24% greater prey count, 78% greater predator count, lower environmental degradation by 19%, reduce retaliatory killings by 97%, cut poaching rates by 50%, and increase tourism rate by 7.5%. Equipped with this model, we expect that the Kenyan Tourism and Wildlife Committee will be able to optimize its usage of funds to ensure the long term health of the preservation, as well as allow tourists to enjoy its beauty for generations to come.

<!-- b000520 | prose | pages [22] -->
14

<!-- b000521 | heading | pages [22] -->
Appendix

<!-- b000522 | prose | pages [22] -->
Code is viewable here.

<!-- b000523 | furniture | pages [23] -->
Team 2318300

<!-- b000524 | furniture | pages [23] -->
Page 22

<!-- b000525 | prose | pages [23] -->
Report for the Kenyan Tourism and Wildlife Committee 15

<!-- b000526 | prose | pages [23] -->
The Maasai Mara is one of the most iconic wildlife management areas in the world.

<!-- b000527 | prose | pages [23] -->
After lengthy analysis of both the historic development of the preserve and the current issues present, we have developed a mathematical model which simulates the fauna, environment, and human activities surrounding the Maasai Mara. More specifically, we analyse the interactions between predators, prey, poachers, tourists, the Maasai people, and the degradation of the environment. This has allowed us to learn some key insights on how investing into different policy affects the Maasai Mara ecosystem and economy as a whole, and formulate policy recommendations to preserve this unique environment.

<!-- b000528 | prose | pages [23] -->
15.1 Budget allocation

<!-- b000529 | prose | pages [23] -->
We suggest a budget of circa KSh380 million to be invested into the Maasai Mara annually. We recognize this figure represents a 46% increase on the current annual investment, but we believe that there will be returns due to an increased tourist count and increased economic activity among the Maasai Population. If the budget is to be decreased, we recommend that an equal proportion is decreased from all suggested areas equally.

<!-- b000530 | caption | pages [23] -->
Table 5: Suggested sectors to invest in. Total Investment: ∼KSh379 million

<!-- b000531 | prose | pages [23] -->
Tourism Promotion Areas 100k Cost (KSh) Environment Anti-pollution Anti-poaching 87.1m 100k 271m Maasai People Anti-poaching infrastructure Areas 87.1m Cost (KSh)

<!-- b000532 | prose | pages [23] -->
15.2

<!-- b000533 | heading | pages [23] -->
Policy suggestions

<!-- b000534 | prose | pages [23] -->
Local Economy 11.9m 9.50m

<!-- b000535 | prose | pages [23] -->
Based on the budget allocation suggestions, we have developed a set of policy and management suggestions, to be considered by the Committee. These are ordered by priority, based on the funding availability for each area. All or just some of these policies can be implemented, and other policies can be implemented instead, as the most important consideration is the budget allocations per area. We have ranked the five most important areas of investment from 1 to 5.

<!-- b000536 | heading | pages [23] -->
1. Diverting tourism revenue into anti-poaching law enforcement

<!-- b000537 | prose | pages [23] -->
(a) Diverting a portion of tourism revenue to the purchasing of anti-poaching equipment.

<!-- b000538 | prose | pages [23] -->
(b) Implement a large donation campaign for the training and deployment of an anti-poaching force

<!-- b000539 | prose | pages [23] -->
and advertise it among tourist areas.

<!-- b000540 | prose | pages [23] -->
(c) Require tourist establishments that operate within the preserve to provide CCTV footage of the

<!-- b000541 | prose | pages [23] -->
areas around their lodging to the anti-poaching force.

<!-- b000542 | heading | pages [23] -->
2. Baseline investment in anti-poaching law enforcement infrastructure

<!-- b000543 | prose | pages [23] -->
(a) Increased investment in transportation infrastructure for rangers to intercept poachers, including

<!-- b000544 | prose | pages [23] -->
the gravelling of roads and airstrips.

<!-- b000545 | prose | pages [23] -->
(b) Establish training programs in anti-poaching practices for rangers to specialize in.

<!-- b000546 | furniture | pages [24] -->
Team 2318300

<!-- b000547 | furniture | pages [24] -->
Page 23

<!-- b000548 | prose | pages [24] -->
(c) Establish lodging specific for anti-poachers close to the preserve.

<!-- b000549 | heading | pages [24] -->
3. Baseline investment in the environment

<!-- b000550 | prose | pages [24] -->
(a) Increased investment in environment protecting infrastructure, including dams, solar panels,

<!-- b000551 | prose | pages [24] -->
and the Maasai Stoves & Solar initiative.

<!-- b000552 | prose | pages [24] -->
(b) Incentivize the development of eco-friendly infrastructure in tourist establishments.

<!-- b000553 | heading | pages [24] -->
4. Investment in the local population

<!-- b000554 | prose | pages [24] -->
(a) Directly fund the identification and strengthening of the bomas most vulnerable to predators.

<!-- b000555 | prose | pages [24] -->
(b) Promote open-air markets for families to have better access to high-quality construction mate-

<!-- b000556 | prose | pages [24] -->
rial.

<!-- b000557 | prose | pages [24] -->
(c) Invest in the existing Maasai Stove & Solar initiative.

<!-- b000558 | heading | pages [24] -->
5. Investment in the local economy

<!-- b000559 | prose | pages [24] -->
(a) Plan the transformation of Narok Town into a resort city through infrastructure, branding, and

<!-- b000560 | prose | pages [24] -->
development incentive policy for investors.

<!-- b000561 | prose | pages [24] -->
(b) Open trade schools and apprenticeship programs for technical professions in the region.

<!-- b000562 | prose | pages [24] -->
(c) Highlight the national importance of the preserve through cultural festivals.

<!-- b000563 | prose | pages [24] -->
15.3 Predicted effects

<!-- b000564 | prose | pages [24] -->
The committee should note that mathematical models come with some inherent uncertainty. Nevertheless, according to our model’s predictions, following the budget proposed would increase the stable animal populations in the preserve by about 25%, lower environmental degradation by about 20%, almost wholly eliminate retaliatory killings, and cut poaching rates in half, and, most vitally, increase the average yearly expected tourists by 7.5%.

<!-- b000565 | prose | pages [24] -->
15.4 Potential limitations

<!-- b000566 | prose | pages [24] -->
The committee should be aware of the potential limitations of our mathematical model. Our predictions of fauna population does not discern the differences between fauna species and no special emphasis was placed on the number of species, so any policy recommendations should be considered with their effect on ecosystem diversity in mind. Furthermore, while our model incorporates some of the needs of the Maasai people, their population growth is not included in the model, so it is vital to analyse our policy recommendations with the long-term impact on the Maasai in mind. Finally, what is vital for the committee to consider is that our model predicts how the Maasai Mara will develop in the long-term, so it is important for the committee to recognize any potential short-term obstacles that were looked over.

<!-- b000567 | furniture | pages [25] -->
Team 2318300

<!-- b000568 | furniture | pages [25] -->
Page 24

<!-- b000569 | heading | pages [25] -->
References

<!-- b000570 | references | pages [25] -->
[1] Invasive species, national parks, and you (u.s. national park service).

<!-- b000571 | references | pages [25] -->
[2] Wildebeest: National geographic. Accessed: 2023-02-19.

<!-- b000572 | references | pages [25] -->
[3] Tourism development as a threat to the great masai mara ecosystem, Sep 2017.

<!-- b000573 | references | pages [25] -->
[4] Serengeti wildebeest population regulation, Jul 2018.

<!-- b000574 | references | pages [25] -->
[5] R. H. Byrd, P. Lu, J. Nocedal, and C. Zhu, A limited memory algorithm for bound constrained

<!-- b000575 | references | pages [25] -->
optimization, SIAM Journal on Scientific Computing, 16 (1995), pp. 1190–1208.

<!-- b000576 | references | pages [25] -->
[6] R. Casagrandi and S. Rinaldi, A theoretical approach to tourism sustainability, Conservation

<!-- b000577 | references | pages [25] -->
Ecology, 6 (2002), p. 15. Accessed: 2023-02-19.

<!-- b000578 | references | pages [25] -->
[7] I. Dennis and P. Craig, Ritual vs. retaliatory killing of african lions in the ngorongoro conservation

<!-- b000579 | references | pages [25] -->
area, Endangered Species Research, 6, pp. 67–74. Accessed: 2023-02-19.

<!-- b000580 | references | pages [25] -->
[8] K. Higginbottom, Wildlife Tourism: Impacts, Management and Planning, Common Ground Pub-

<!-- b000581 | references | pages [25] -->
lishing, Pty. Ltd., 2004.

<!-- b000582 | references | pages [25] -->
[9] M. H. Holden and J. Lockyer, Poacher-population dynamics when legal trade of naturally deceased

<!-- b000583 | references | pages [25] -->
organisms funds anti-poaching enforcement, Journal of Theoretical Biology, 517 (2021), p. 110618.

<!-- b000584 | references | pages [25] -->
[10] L. Juma, I. Bakos Phd, and A. Khademi-Vidra, Nature interpretation and visitor management

<!-- b000585 | references | pages [25] -->
objectives: A survey of tourist attitudes at maasai mara national reserve, kenya, Sustainability, 12

<!-- b000586 | references | pages [25] -->
(2020).

<!-- b000587 | references | pages [25] -->
[11] E. Kaslik and M. Neamtu, Dynamics of a tourism sustainability model with distributed delay,

<!-- b000588 | references | pages [25] -->
Chaos, Solitons & Fractals, 133 (2020), p. 109610. Accessed: 2023-02-19.

<!-- b000589 | references | pages [25] -->
[12] F. Mansal, T. Nguyen-Huu, P. Auger, and M. Balde, A mathematical model of a fishery with

<!-- b000590 | references | pages [25] -->
variable market price: Sustainable fishery/over-exploitation, Acta Biotheoretica, 62 (2014), pp. 305–

<!-- b000591 | references | pages [25] -->
323. Accessed: 2023-02-19.

<!-- b000592 | references | pages [25] -->
[13] N. Page, Wildebeest migration.

<!-- b000593 | references | pages [25] -->
[14] Parks, Wildebeest, (2023). Accessed: 2023-02-19.

<!-- b000594 | references | pages [25] -->
[15] J. C. Polking, A. Boggess, and D. Arnold, Differential equations with boundary value problems,

<!-- b000595 | references | pages [25] -->
Pearson, 2 ed., 2018.

<!-- b000596 | references | pages [25] -->
[16] S. T. D., S. N., N. C. L., and M. O. D., Optimal control of a threatened wildebeest-lion prey-predator

<!-- b000597 | references | pages [25] -->
system in the serengeti ecosystem. Accessed: 2023-02-19.

<!-- b000598 | references | pages [25] -->
[17] W. W., A. I., and M. S., A theoretical approach to tourism sustainability, Ecological Modelling, 251

<!-- b000599 | references | pages [25] -->
(2013), pp. 103–113. Accessed: 2023-02-19.

<!-- b000600 | references | pages [25] -->
[18] K. Wanjala, The economic impact assessment of the novel coronavirus on tourism and trade in

<!-- b000601 | references | pages [25] -->
kenya: Lessons from preceding epidemics, Finance amp; Economics Review, 2 (2020), p. 1–10.

<!-- b000602 | references | pages [25] -->
[19] A. v. Zandbergen, Masai mara vs serengeti – which park should you choose? – safaribookings.
