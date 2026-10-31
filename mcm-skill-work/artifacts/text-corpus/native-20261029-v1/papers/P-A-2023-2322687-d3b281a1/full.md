# P-A-2023-2322687-d3b281a1

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2023

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
A

<!-- b000006 | title | pages [1] -->
2322687

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Is There Space for More? A Spatiotemporal Partial Differential

<!-- b000009 | title | pages [1] -->
Equations Model for Plant Growth During Drought Cycles

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
Droughts pose a significant risk to the survival of a community of plants. Although individual plants may struggle to adapt to a lack of water caused by a drought, existing literature has suggested a positive relationship between the biodiversity of a plant community and its ability to survive drought cycles. We have been tasked to verify this claim and build a generalized biome-independent model that predicts changes in a plant community through cycles of drought.

<!-- b000012 | prose | pages [1] -->
Our approach was to develop a parameterized partial differential equations model for the growth of multiple plant species over time on the basis of the amount of water available. Crucially, we also incorporate spatial dimensions and analysis into the model, which allows us to consider plant dispersal and water diffusion across physical boundaries. To support this growth model, we also implement a sub-model for rainfall that can simulate the effect of a variety of droughts by changing drought timing and severity. Incorporating this into the plant growth model, we model plant growth in Mathematica using numerical analysis of the partial differential equations. We conduct a sensitivity analysis of the model’s parameters, simulating the effects of biodiversity by steadily increasing the number of unique species starting from a control of just one species. We also analyze the impact of different types of droughts, as well as different types of plants as measured by their resistance and resilience. We conclude by studying the impacts of external factors, such as pollution or habitat reduction.

<!-- b000013 | prose | pages [1] -->
Ultimately, we find that although increasing the number of unique plants in a given community generates inter-species competition, it cumulatively benefits the overall system by increasing the total amount of long-term plant biomass. However, marginal benefit decreases as total number of unique species increases: going from one to two unique species generates significant benefits in total biomass, but changes are smaller when going from two to three, and the transition from three to four actually decreases total biomass. Meanwhile, our sensitivity analysis finds that changes in resilience and resistance correspondingly impact total plant biomass but do not affect the general behavior of the model. In addition, we determine that habitat destruction can cause individual species to dominate a plant community due to increased spatial competition. We find under certain extreme conditions, a given species of plants can either survive and dominate in the long-term or go extinct depending on their initial conditions.

<!-- b000014 | prose | pages [1] -->
The main advantage of our unique spatial approach over traditional, space-independent models that only depend upon time, like the classic Lotka-Volterra model, is the the ability to account for fundamental physical behaviors of plants and ground water—that is, dispersal and diffusion across a 2D space.

<!-- b000015 | prose | pages [1] -->
Without spatial considerations, one cannot accurately model the fact that generally, plants and water can only spread to adjacent locations. This also allows us to model phenomenon like competition for habitation or water at a given location. Finally, the spatial approach also provides the ability to simulate random initial locations, mirroring the stochasticity of real-world environments, as well as forecast the impacts of habitat reduction easily. Combined with a realistic model for rainfall data and drought conditions, our model serves as a comprehensive general phenomenological model for simulating plant growth in any given community under cycles of droughts.

<!-- b000016 | keywords | pages [1] -->
Keywords: Partial Differential Equations, Spatiotemporal Analysis, Drought Modeling

<!-- b000017 | furniture | pages [2] -->
Team # 2322687

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
1

<!-- b000020 | heading | pages [2] -->
Introduction

<!-- b000021 | furniture | pages [2] -->
Page 2 of 25

<!-- b000022 | prose | pages [2] -->
3 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 Existing Literature

<!-- b000023 | prose | pages [2] -->
2

<!-- b000024 | heading | pages [2] -->
Developing the Plant Community Model

<!-- b000025 | prose | pages [2] -->
4

<!-- b000026 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000027 | heading | pages [2] -->
Assumptions

<!-- b000028 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 Model Overview and Justification 5 Variables and Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 7 Plant Biomass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.5 Water and Rainfall 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.6 Species Competition 8 Rainfall, Droughts, Species Types, and Pollution . . . . . . . . . . . . . . . . . . . . . 2.7 8 Initial and Boundary Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.8 9 Model Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.9

<!-- b000029 | prose | pages [2] -->
3

<!-- b000030 | heading | pages [2] -->
Rainfall and Drought Model

<!-- b000031 | prose | pages [2] -->
9

<!-- b000032 | prose | pages [2] -->
10 General Rain Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 10 Drought-Adjusted Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000033 | prose | pages [2] -->
4

<!-- b000034 | heading | pages [2] -->
Results

<!-- b000035 | prose | pages [2] -->
10

<!-- b000036 | prose | pages [2] -->
11 Number of Unique Plant Species . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 11 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Different Types of Droughts

<!-- b000037 | prose | pages [2] -->
5

<!-- b000038 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000039 | prose | pages [2] -->
15

<!-- b000040 | prose | pages [2] -->
17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Types of Species 17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 Resistance and Pollution 19 Habitat Reduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000041 | prose | pages [2] -->
6

<!-- b000042 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000043 | prose | pages [2] -->
21

<!-- b000044 | prose | pages [2] -->
23 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Strengths 23 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000045 | prose | pages [2] -->
7

<!-- b000046 | heading | pages [2] -->
Conclusion

<!-- b000047 | prose | pages [2] -->
8 Future Exploration

<!-- b000048 | heading | pages [2] -->
References

<!-- b000049 | references | pages [2] -->
23

<!-- b000050 | references | pages [2] -->
23

<!-- b000051 | references | pages [2] -->
24

<!-- b000052 | references | pages [2] -->
25

<!-- b000053 | furniture | pages [3] -->
Team # 2322687

<!-- b000054 | furniture | pages [3] -->
Page 3 of 25

<!-- b000055 | references | pages [3] -->
1

<!-- b000056 | heading | pages [3] -->
Introduction

<!-- b000057 | prose | pages [3] -->
1.1

<!-- b000058 | heading | pages [3] -->
Background

<!-- b000059 | prose | pages [3] -->
The study of how drought cycles impact plant communities is crucial for understanding the impacts of climate change on ecosystems and agriculture. Droughts can significantly alter plant growth, distri- bution, and productivity, which can have cascading effects on ecosystem functions and services, such as nutrient cycling, soil stability, and carbon storage. Moreover, droughts can impact agricultural pro- ductivity, as they reduce crop yields, increase irrigation demands, and exacerbate soil erosion and land degradation [1]. By studying how droughts affect plant communities, scientists can develop effective management strategies to mitigate the impacts of droughts on ecosystems. This includes developing drought-resistant crop varieties, improving water use efficiency, and implementing sustainable land management practices. Ultimately, understanding the effects of drought on plant communities is cru- cial for maintaining ecosystem health and supporting sustainable agriculture in the face of climate change.

<!-- b000060 | prose | pages [3] -->
Plant species are often geographically grouped together into communities to better understand species interaction and relationships [2]. The relative composition of the species within communities is not static, but rather it changes as a response responds to stimuli and stresses. In particular, one common source of stress that can drastically change the composition of a community is a period of drought [3].

<!-- b000061 | prose | pages [3] -->
As different organisms have different characteristics, they react and adapt differently to extreme conditions. Such responses are well described by the notions of resilience (ability to recover after extreme conditions) and resistance (ability to persist and grow despite extreme conditions) [4]. Past research has suggested that localized biodiversity within these communities strengthens the overall ability of the community to adapt to periods of drought, relative to a more homogeneous community. Studies have suggested the possibility that the genetic diversity offered by a diverse community provides a higher chance for species-diverse communities to effectively thrive even during extended periods of little to no rainfall [5]. However, little research has been done to explore the quantitative extent to which biodiversity strengthens a community’s ability to persist and grow amid drought, and how this survivability changes depending on the specific number of species.

<!-- b000062 | prose | pages [3] -->
1.2

<!-- b000063 | heading | pages [3] -->
Problem Restatement

<!-- b000064 | prose | pages [3] -->
To address this question, our team has been tasked to develop a model to predict how the composition of a plant community changes through drought cycles. The model and its analysis must:

<!-- b000065 | prose | pages [3] -->
1. Account for species interaction, both competition and mutual support, during drought

<!-- b000066 | prose | pages [3] -->
2. Evaluate how many species are required to benefit from the biodiversity phenomenon, as well as assess the impact of an increase in species within a community.

<!-- b000067 | prose | pages [3] -->
3. Consider the impact of changes in the frequency and severity of droughts

<!-- b000068 | prose | pages [3] -->
4. Consider the impact of differing types of species within a community

<!-- b000069 | prose | pages [3] -->
5. Consider the impact of pollution and habitat destruction

<!-- b000070 | furniture | pages [4] -->
Team # 2322687

<!-- b000071 | furniture | pages [4] -->
Page 4 of 25

<!-- b000072 | prose | pages [4] -->
1.3 Existing Literature

<!-- b000073 | prose | pages [4] -->
Prior to developing our customized model, we researched and analyzed several existing models. Below are two important examples.

<!-- b000074 | prose | pages [4] -->
First, we examined the classic Lotka-Volterra Model as a basis to consider competition between plant species and impacts on growth [6]. An abstracted version of the predator-prey equations are:

<!-- b000075 | prose | pages [4] -->
𝑑𝑥

<!-- b000076 | prose | pages [4] -->
𝑑𝑡= 𝛼𝑥−𝛽𝑥𝑦

<!-- b000077 | prose | pages [4] -->
𝑑𝑦

<!-- b000078 | prose | pages [4] -->
𝑑𝑡= 𝛿𝑥𝑦−𝜙𝑦

<!-- b000079 | prose | pages [4] -->
where 𝛼and 𝛿are the growth rates of each of the prey predator species respectively, while 𝛽and 𝛿 represent the competitive interaction between the two species.

<!-- b000080 | prose | pages [4] -->
Although the Lotka-Volterra Model provided a method to factor in competition, we believed its specificity towards a predator-prey relationship made it difficult to accurately model plant interactions since those interactions could potentially also be mutually beneficial. At the same time, perhaps the most important issue regarding the model for our task was the assumption of a constant growth rate. It does not take into consideration the relationship that growth rate and water scarcity.

<!-- b000081 | prose | pages [4] -->
To address this resource utilization aspect of plant modeling, we also considered Monod’s equation for modeling microbial growth rate [7].

<!-- b000082 | prose | pages [4] -->
𝑆

<!-- b000083 | prose | pages [4] -->
𝜇= 𝜇𝑚𝑎𝑥

<!-- b000084 | prose | pages [4] -->
𝐾𝑆+ 𝑆 where 𝜇, the growth rate, is determined by the product of the maximum growth rate and a fraction where S represents the concentration of a limiting substrate, or resource and K is a constant.

<!-- b000085 | prose | pages [4] -->
These two models provided a fundamental starting point for our work but were ultimately insufficient for the problem at hand. In particular, we hoped to account for the following factors that were not considered in these systems:

<!-- b000086 | prose | pages [4] -->
1. Multiple species interaction

<!-- b000087 | prose | pages [4] -->
2. Storage of groundwater

<!-- b000088 | prose | pages [4] -->
3. The spatial dimensions of the community, which influences plant and water dispersal

<!-- b000089 | prose | pages [4] -->
4. Different types of droughts

<!-- b000090 | prose | pages [4] -->
5. Resilience and resistance of plants

<!-- b000091 | prose | pages [4] -->
6. External factors like pollution and habitat reduction

<!-- b000092 | prose | pages [4] -->
2

<!-- b000093 | heading | pages [4] -->
Developing the Plant Community Model

<!-- b000094 | prose | pages [4] -->
2.1

<!-- b000095 | heading | pages [4] -->
Assumptions

<!-- b000096 | prose | pages [4] -->
To simplify the modeling, we establish a few fundamental assumptions, as well as provide justifications for them:

<!-- b000097 | furniture | pages [5] -->
Team # 2322687

<!-- b000098 | furniture | pages [5] -->
Page 5 of 25

<!-- b000099 | prose | pages [5] -->
• Assumption: Plant biomass is increased solely through plant growth.

<!-- b000100 | prose | pages [5] -->
– Justification: The problem statement revolves around analyzing the growth plants relative

<!-- b000101 | prose | pages [5] -->
to weather conditions. Therefore, we find it necessary to only discuss how plant biomass changes based on plant growth or death, and to ignore other external factors like human development, predators, etc.

<!-- b000102 | prose | pages [5] -->
• Assumption: New species of plants do not emerge suddenly in the environment throughout a given simulation.

<!-- b000103 | prose | pages [5] -->
– Justification: Similar to the above assumption, we do not consider external influences that

<!-- b000104 | prose | pages [5] -->
may cause a plant to suddenly arise in an ecosystem. Instead, we will focus our analysis on the existing plants in an ecosystem and study how their biomasses change with time.

<!-- b000105 | prose | pages [5] -->
• Assumption: Plants are differentiated solely by their resistance (how easily they die) and resilience (how easily they grow).

<!-- b000106 | prose | pages [5] -->
– In the context of analyzing plant growth under extreme weather conditions, the most

<!-- b000107 | prose | pages [5] -->
important factor to consider is how plants survive within these conditions.

<!-- b000108 | prose | pages [5] -->
Therefore, we don’t consider factors like plant structure, shape, or size, and instead assume that the resistance and resilience of a given plant are able to encapsulate its other defining qualities.

<!-- b000109 | prose | pages [5] -->
2.2

<!-- b000110 | heading | pages [5] -->
Model Overview and Justification

<!-- b000111 | prose | pages [5] -->
To explore this problem, our model will attempt to predict how the amount of water in the ground, as well the total biomass of each species of plant, will change—these factors will serve as the dependent variables. Specifically, because we are interested in studying the transition rates of these quantities, we will develop a model based upon differential equations that can naturally characterize changes over time.

<!-- b000112 | prose | pages [5] -->
However, we argue that analyzing the system across time alone is insufficient, as the physical dimensions of an ecological community are highly influential in its development. For one, unlike models for animals or microorganisms, plants generally do not move, which therefore limits their water consumption and interactions with other plants at non-adjacent locations. For instance, different species of plants may not be able to occupy the same physical location in the habitat due water shortages in that particular location, and the size of the habitat will limit plant growth.

<!-- b000113 | prose | pages [5] -->
In addition, water dispersal is highly motivated by its diffusion across space and concentration gradients. Modeling the spatial movement of water within a given area also provides us the ability to use a more accurate measurement of the amount of water in a given location, rather than total water in the system, which is far less accurate to plant growth. For instance, the growth of a plant at a given location is not dependent on the amount of water in the overall system, but rather at the particular location that it occupies.

<!-- b000114 | prose | pages [5] -->
Therefore, our model will, in addition to time, consider spatial dimensions as independent variables, pointing to a need for partial rather than ordinary differential equations; this will also allow us to study the impact of habitat reduction in later sensitivity analysis.

<!-- b000115 | prose | pages [5] -->
Within the model, we will incorporate parameters that allow us to explore and capture the following conditions:

<!-- b000116 | furniture | pages [6] -->
Team # 2322687

<!-- b000117 | furniture | pages [6] -->
Page 6 of 25

<!-- b000118 | prose | pages [6] -->
• The number of unique plant species

<!-- b000119 | prose | pages [6] -->
• The resilience and resistance of each species

<!-- b000120 | prose | pages [6] -->
• The amount of weekly rainfall

<!-- b000121 | prose | pages [6] -->
• The frequency and magnitude of droughts

<!-- b000122 | prose | pages [6] -->
Note that as a whole, except for the independent variable of time, the model is dimensionless; that is, we are not measuring specific amounts of biomass, groundwater, rainfall, etc. This is done because the purpose of this research is to determine the broader qualitative and relative impacts of different factors on plant growth, rather than predict the precise amount of plants that exist in a particular region under a precise set of parameter values. The latter investigation can likely not be conducted with a phenomenological, mechanistic mathematical model that yields deep insight into the nature and behavior of plant interactions with their communities, which is the ultimate goal of this research and the overall problem statement. Therefore, we believe it is much more meaningful to produce a dimensionless model that can be adapted to any given plant community, whose results provide fundamental information about how species interact under different conditions, both internal—like plant resilience and resistance—and external—like drought, pollution, or habitat reduction.

<!-- b000123 | prose | pages [6] -->
The independent variable of time is dimensionalized for the purpose of parameter value calculations and to provide some basic context to our findings, but even it can be nondimensionalized without changing the underlying validity of the model.

<!-- b000124 | caption | pages [6] -->
Figure 1: A visual representation of the model and its dynamics

<!-- b000125 | furniture | pages [7] -->
Team # 2322687

<!-- b000126 | prose | pages [7] -->
2.3

<!-- b000127 | heading | pages [7] -->
Variables and Notation

<!-- b000128 | furniture | pages [7] -->
Page 7 of 25

<!-- b000129 | prose | pages [7] -->
In the model, we will introduce several variables and parameters. A summary is provided here:

<!-- b000130 | prose | pages [7] -->
Variable

<!-- b000131 | heading | pages [7] -->
Notation

<!-- b000132 | prose | pages [7] -->
𝑘 number of species 𝑛𝑖 species biomass 𝑁 total plant biomass 𝑤 water 𝑥, 𝑦 spatial dimensions 𝑡 time 𝑐𝑖 plant growth rate 𝑚𝑖 plant mortality rate water flow from concentration 𝑣 differences 𝑑 water flow from diffusion 𝑎𝑡 rainfall habitat size L Meaning the number of unique species in the system the total plant biomass of species 𝑖 total plant biomass of all species total ground water the 2D space being modeled time, measured in week the growth rate of species 𝑖 the mortality rate of species 𝑖 speed of water in moving from high to low concentration speed of water along flat terrain rainfall per week at time 𝑡 length and width of the (square) habitat

<!-- b000133 | caption | pages [7] -->
Table 1: A summary of the variables and parameters that will be introduced in the model.

<!-- b000134 | prose | pages [7] -->
2.4 Plant Biomass

<!-- b000135 | prose | pages [7] -->
We first derive an equation modeling the total biomass of each species 𝑖, represented by 𝑛𝑖(𝑥, 𝑦, 𝑡), which can be influenced by three factors: plant growth, plant death, and plant dispersal across the habitat.

<!-- b000136 | prose | pages [7] -->
Plant growth is determined by the growth rate of the given species, the amount of water available, and the amount of plants there currently are. Literature suggests that plant growth is not linear, and that an abundance of the same species of plants in a given area encourages further plant growth [8]. Therefore, we propose an interaction term defined by the plant growth rate, a quadratic form of current plant biomass, and water availability. Plant biomass is lost solely through plant death, which is dependent on the current plant biomass and the mortality rate of the species, 𝑚𝑖. Finally, plant dispersal can be modeled by a general diffusion equation across 𝑥and 𝑦. Taken together, this produces the following PDE:

<!-- b000137 | prose | pages [7] -->
𝑖−𝑚𝑛𝑖+ 𝜕2𝑛𝑖

<!-- b000138 | prose | pages [7] -->
𝜕𝑛𝑖

<!-- b000139 | prose | pages [7] -->
𝜕𝑡= 𝑐𝑖𝑤𝑛2

<!-- b000140 | prose | pages [7] -->
2.5 Water and Rainfall

<!-- b000141 | prose | pages [7] -->
𝜕𝑥2 + 𝜕2𝑛𝑖

<!-- b000142 | prose | pages [7] -->
(1) 𝜕𝑦2

<!-- b000143 | prose | pages [7] -->
We next derive an equation modeling the amount of water in the ground, which is affected by rainfall, drainage (which includes evaporation), and dispersal across the habitat. Water enters the system through

<!-- b000144 | furniture | pages [8] -->
Team # 2322687

<!-- b000145 | furniture | pages [8] -->
Page 8 of 25

<!-- b000146 | prose | pages [8] -->
time-dependent rainfall, 𝑎𝑡, and is lost due to drainage at a rate proportional to the current amount of water in the ground. Water also is lost due to plant consumption, which should also be modeled by a quadratic interaction of the total plant biomass and water availability, given the idea that a higher biomass further encourages future growth.

<!-- b000147 | prose | pages [8] -->
Regarding dispersal, water flows from high to low concentration at a speed 𝑣, introducing an interaction term between 𝑣and the gradient of 𝑤. Water can also flow across flatland at a speed 𝑑, introducing a scaled diffusion equation for 𝑤. Therefore, we propose:

<!-- b000148 | prose | pages [8] -->
𝜕𝑡= 𝑎𝑡−𝑤−𝑤𝑁2 + 𝑣( 𝜕𝑤

<!-- b000149 | prose | pages [8] -->
𝜕𝑤

<!-- b000150 | prose | pages [8] -->
2.6 Species Competition

<!-- b000151 | prose | pages [8] -->
𝜕𝑥+ 𝜕𝑤

<!-- b000152 | prose | pages [8] -->
𝜕𝑦) + 𝑑( 𝜕2𝑤

<!-- b000153 | prose | pages [8] -->
𝜕𝑥2 + 𝜕2𝑤

<!-- b000154 | prose | pages [8] -->
𝜕𝑦2 ) (2)

<!-- b000155 | prose | pages [8] -->
A crucial component of our model is the ability to study the interactions between multiple unique species in the system. Such is why we separate total plant biomass 𝑁into the biomass of each plant species 𝑖, which allows us to write separate equations for each plant species and the total biomass as the sum of these equations. Mathematically, this produces the system:

<!-- b000156 | prose | pages [8] -->
1 −𝑚𝑛1 + 𝜕2𝑛1

<!-- b000157 | prose | pages [8] -->
𝜕𝑛1

<!-- b000158 | prose | pages [8] -->
𝜕𝑥2 + 𝜕2𝑛1

<!-- b000159 | prose | pages [8] -->
𝜕𝑡= 𝑐1𝑤𝑛2

<!-- b000160 | prose | pages [8] -->
...

<!-- b000161 | prose | pages [8] -->
𝜕𝑛𝑘

<!-- b000162 | prose | pages [8] -->
𝜕𝑦2

<!-- b000163 | prose | pages [8] -->
𝜕𝑥2 + 𝜕2𝑛𝑘

<!-- b000164 | prose | pages [8] -->
𝑘−𝑚𝑛𝑘+ 𝜕2𝑛𝑘

<!-- b000165 | prose | pages [8] -->
𝜕𝑡= 𝑐𝑘𝑤𝑛2

<!-- b000166 | prose | pages [8] -->
𝜕𝑁

<!-- b000167 | prose | pages [8] -->
𝜕𝑡= 𝜕𝑛1

<!-- b000168 | prose | pages [8] -->
𝜕𝑡+ . . . + 𝜕𝑛𝑘

<!-- b000169 | prose | pages [8] -->
𝜕𝑡 𝜕𝑤

<!-- b000170 | prose | pages [8] -->
(3)

<!-- b000171 | prose | pages [8] -->
𝜕𝑦2

<!-- b000172 | prose | pages [8] -->
𝜕𝑡= 𝑎𝑡−𝑤−𝑤𝑁2 + 𝑣( 𝜕𝑤

<!-- b000173 | prose | pages [8] -->
𝜕𝑥+ 𝜕𝑤

<!-- b000174 | prose | pages [8] -->
𝜕𝑦) + 𝑑( 𝜕2𝑤

<!-- b000175 | prose | pages [8] -->
𝜕𝑥2 + 𝜕2𝑤

<!-- b000176 | prose | pages [8] -->
𝜕𝑦2 )

<!-- b000177 | prose | pages [8] -->
To study the phenomenon of how unique species interact, compete, cooperate, and ultimately influence the drought adaptability of the plant community, we can increase the total number of species, 𝑘.

<!-- b000178 | prose | pages [8] -->
Rainfall, Droughts, Species Types, and Pollution 2.7

<!-- b000179 | prose | pages [8] -->
Through the time-dependent parameter 𝑎𝑡, we can change the amount of rainfall that the system receives over a given period of time. In doing so, we can consider periods of drought (i.e., reduced rainfall), as well as tune the length, frequency, and magnitude of such droughts. Finally, through the parameters 𝑐𝑖 and 𝑚𝑖, which control the resilience and resistance of plants, respectively, we can simulate the impact of different types of plant species with different properties, as well as varying amount of pollution, which would affect plants’ abilities to grow and their tendencies to die. We will conduct sensitivity analysis of these parameters during our analysis of the model.

<!-- b000180 | furniture | pages [9] -->
Team # 2322687

<!-- b000181 | furniture | pages [9] -->
Page 9 of 25

<!-- b000182 | prose | pages [9] -->
2.8 Initial and Boundary Conditions

<!-- b000183 | prose | pages [9] -->
As with all systems of PDEs, we must also establish initial and boundary conditions. The initial biomass of each plant species will be taken to be the value of 1 at a random location within the habitat, representing a small cluster of seeds or spores dispersed randomly at the beginning of the simulation. The initial amount of water in the ground will be the amount of rainfall at 𝑡= 0.

<!-- b000184 | prose | pages [9] -->
We will impose periodic boundary conditions for both the biomass of each plant species and the water in the ground. This is a fair and commonly used condition statement in mathematical modeling, as we are attempting to approximate a large, semi-infinite system by using a unit cell. Topologically, the space made by the two-dimensional periodic boundary conditions can be thought of as being mapped onto a compact space. Taken together, and recalling the parameter 𝐿, this yields:

<!-- b000185 | prose | pages [9] -->
𝑛1(𝑥, 𝑦, 0) = 𝑛10(𝑥, 𝑦)

<!-- b000186 | prose | pages [9] -->
...

<!-- b000187 | prose | pages [9] -->
(4)

<!-- b000188 | prose | pages [9] -->
𝑛𝑘(𝑥, 𝑦, 0) = 𝑛𝑘0(𝑥, 𝑦)

<!-- b000189 | prose | pages [9] -->
𝑁(𝑥, 𝑦, 0) = 𝑛10(𝑥, 𝑦) + . . . + 𝑛𝑘0(𝑥, 𝑦) 𝑤(𝑥, 𝑦, 0) = 𝑎0

<!-- b000190 | prose | pages [9] -->
for initial conditions, and

<!-- b000191 | prose | pages [9] -->
𝑛1(0, 𝑦, 𝑡) = 𝑛1(𝐿, 𝑦, 𝑡) 𝑛1(𝑥, 0, 𝑡) = 𝑛1(𝑥, 𝐿, 𝑡)

<!-- b000192 | prose | pages [9] -->
... 𝑛𝑘(0, 𝑦, 𝑡) = 𝑛𝑘(𝐿, 𝑦, 𝑡)

<!-- b000193 | prose | pages [9] -->
(5)

<!-- b000194 | prose | pages [9] -->
𝑛𝑘(𝑥, 0, 𝑡) = 𝑛𝑘(𝑥, 𝐿, 𝑡)

<!-- b000195 | prose | pages [9] -->
𝑁(0, 𝑦, 𝑡) = 𝑁(𝐿, 𝑦, 𝑡) 𝑁(𝑥, 0, 𝑡) = 𝑁(𝑥, 𝐿, 𝑡) 𝑤(0, 𝑦, 𝑡) = 𝑤(𝐿, 𝑦, 𝑡) 𝑤(𝑥, 0, 𝑡) = 𝑤(𝑥, 𝐿, 𝑡)

<!-- b000196 | prose | pages [9] -->
for boundary conditions.

<!-- b000197 | prose | pages [9] -->
2.9

<!-- b000198 | heading | pages [9] -->
Model Analysis

<!-- b000199 | prose | pages [9] -->
Because of its highly nonlinear nature, the PDEs developed do not have analytical solutions. There- fore, to study the system given in (3), we conduct numerical analysis of the PDEs in Mathematica. Specifically, we use the numerical method of lines, which solves PDEs by discretizing the equation in all but one dimension, then integrating the semi-discrete problem as a system of ordinary differential equations (ODEs) or differential-algebraic equations (DAEs).

<!-- b000200 | furniture | pages [10] -->
Team # 2322687

<!-- b000201 | furniture | pages [10] -->
Page 10 of 25

<!-- b000202 | prose | pages [10] -->
3

<!-- b000203 | heading | pages [10] -->
Rainfall and Drought Model

<!-- b000204 | prose | pages [10] -->
3.1

<!-- b000205 | heading | pages [10] -->
General Rain Model

<!-- b000206 | prose | pages [10] -->
Alongside the Plant Community Model, we also developed a rainfall model to simulate natural rainfall and periods of drought and recovery. To this end, we began with a general rain model, with an average rainfall chance and rainfall volume. After uniform randomization on the rainfall chance to determine the chance of rain on a week-to-week basis, another layer of randomization was applied to the average volume of rain.

<!-- b000207 | prose | pages [10] -->
We then modified the two values with a seasonal variability index, which represents the magnitude of seasonal variation. For example, certain communities may experience seasonal monsoons while others, such as in a desert, may have minimal seasonal variability. Because of the periodic nature of seasons, we applied this seasonal variability to a sine function to appropriately model a seasonal coefficient applied to each week’s rainfall:

<!-- b000208 | prose | pages [10] -->
𝑉∗(sin(2𝜋

<!-- b000209 | prose | pages [10] -->
mod 52)) + 51 52 (𝑑

<!-- b000210 | prose | pages [10] -->
52)

<!-- b000211 | prose | pages [10] -->
where V is the seasonal variability index, d is the week number, and where sin( 2𝜋

<!-- b000212 | prose | pages [10] -->
52𝑥) has period of 52 weeks.

<!-- b000213 | prose | pages [10] -->
3.2

<!-- b000214 | heading | pages [10] -->
Drought-Adjusted Model

<!-- b000215 | caption | pages [10] -->
Figure 2: Weekly rainfall for 1000 weeks of data containing three separate. Specifically, droughts

<!-- b000216 | prose | pages [10] -->
occur from 𝑡= 200 to 𝑡= 250, 𝑡= 500 to 𝑡= 600, and 𝑡= 750 to 𝑡= 900

<!-- b000217 | prose | pages [10] -->
After developing a rain model, we then overlaid periods of droughts over a 1000 week general rain model. Some droughts were also deliberately placed within the rainy season to address the problem statement’s task of including drought in times when precipitation is abundant.

<!-- b000218 | prose | pages [10] -->
We also created parameters to limit the ranges of the length of the drought and the severity (as in the percent decrease in the amount of rain when it does rain). With the three parameters of drought appearance, length, and severity we thus could generate unique ”drought scenarios”, which provides a more comprehensive model of droughts than a usage of uniformly long and severe droughts.

<!-- b000219 | prose | pages [10] -->
Once we decided on parameters, we then applied our set drought model on a randomized thousand- week rain period with the general rain model. We analyze the impact of different drought scenarios derived from different parameters in section 4.2.

<!-- b000220 | furniture | pages [11] -->
Team # 2322687

<!-- b000221 | furniture | pages [11] -->
Page 11 of 25

<!-- b000222 | caption | pages [11] -->
Figure 3: Rainfall and Drought Diagram. The first line of circles represent modifiers that change the

<!-- b000223 | prose | pages [11] -->
chance of the following conditional—whether or not there will be rain. Each iteration represents the decision tree for a week, with the loop occurring for 1000 weeks.

<!-- b000224 | prose | pages [11] -->
4

<!-- b000225 | heading | pages [11] -->
Results

<!-- b000226 | prose | pages [11] -->
4.1 Number of Unique Plant Species

<!-- b000227 | prose | pages [11] -->
One primary purpose of this research is to investigate the interactions between different species amid cycles of drought, which are undeniably related [9, 10, 11]. Therefore, we first study how the system changes depending upon the number of unique species, beginning first with 𝑘= 1 (i.e., a plant community with just one type of plant), which will serve both as a control group and validation of the model’s performance.

<!-- b000228 | furniture | pages [12] -->
Team # 2322687

<!-- b000229 | prose | pages [12] -->
𝑡= 200

<!-- b000230 | prose | pages [12] -->
𝑡= 750

<!-- b000231 | prose | pages [12] -->
(a) 𝑡= 200 𝑡= 200:

<!-- b000232 | prose | pages [12] -->
(b) 𝑡= 750 𝑡= 750:

<!-- b000233 | prose | pages [12] -->
before the

<!-- b000234 | prose | pages [12] -->
before the

<!-- b000235 | prose | pages [12] -->
first drought. The plants

<!-- b000236 | prose | pages [12] -->
third drought. The plants

<!-- b000237 | prose | pages [12] -->
appear to be forming vege-

<!-- b000238 | prose | pages [12] -->
still form strips, though

<!-- b000239 | prose | pages [12] -->
tative strips within the habi-

<!-- b000240 | prose | pages [12] -->
each strip is thicker and

<!-- b000241 | prose | pages [12] -->
tat

<!-- b000242 | prose | pages [12] -->
more concentrated.

<!-- b000243 | furniture | pages [12] -->
Page 12 of 25

<!-- b000244 | prose | pages [12] -->
𝑡= 900

<!-- b000245 | prose | pages [12] -->
𝑡= 1000

<!-- b000246 | prose | pages [12] -->
(c) 𝑡= 900 𝑡= 900: after the third

<!-- b000247 | prose | pages [12] -->
𝑡= 1000 𝑡= 1000:

<!-- b000248 | prose | pages [12] -->
recover- (d)

<!-- b000249 | prose | pages [12] -->
drought.

<!-- b000250 | prose | pages [12] -->
ing from drought.

<!-- b000251 | prose | pages [12] -->
Following the

<!-- b000252 | prose | pages [12] -->
The

<!-- b000253 | prose | pages [12] -->
drought, the clusters are

<!-- b000254 | prose | pages [12] -->
plants are able to make a

<!-- b000255 | prose | pages [12] -->
plants are smaller and less

<!-- b000256 | prose | pages [12] -->
full recovery following the

<!-- b000257 | prose | pages [12] -->
concentrated.

<!-- b000258 | prose | pages [12] -->
drought.

<!-- b000259 | prose | pages [12] -->
(e) Total biomass of the system over time.

<!-- b000260 | caption | pages [12] -->
Figure 4: The change of a community with just one species of plant over time.

<!-- b000261 | prose | pages [12] -->
Figures 4a-4d provide spatial density plots of the plant community at a given point in time; that is, for any given spatial coordinate in the habitat, the color of the location represents the biomass of the plant at that given location at the specified point in time. Figure 4e represents a graph of the total plant biomass in over the 1000 week period. Note how the periods of sudden decline correspond to the periods of drought shown in Figure 2.

<!-- b000262 | prose | pages [12] -->
The results shown in Figure 4 verify the model’s validity. Indeed, the patterns shown in Figures 4a-4d match real-world plant formations in communities with just one species (see Figure 5).

<!-- b000263 | prose | pages [12] -->
(a) Patterned vegetation formations in South Africa, which mirror the forma- tions in Figure 4a and 4c.

<!-- b000264 | prose | pages [12] -->
(b) Striped vegetation formations in Niger, which mirror the formations in Figure 4b and 4d.

<!-- b000265 | caption | pages [12] -->
Figure 5: Real-world plant formations that mirror the model’s results [12]

<!-- b000266 | furniture | pages [13] -->
Team # 2322687

<!-- b000267 | furniture | pages [13] -->
Page 13 of 25

<!-- b000268 | prose | pages [13] -->
With this functional model, we then expand the model to include two unique species (𝑘= 2).

<!-- b000269 | prose | pages [13] -->
(a) Species 1 of 2 (b) Species 2 of 2

<!-- b000270 | prose | pages [13] -->
(c) Total biomass of the system over time.

<!-- b000271 | caption | pages [13] -->
Figure 6: The change of a community with two species of plants over time. All snapshots are taken

<!-- b000272 | prose | pages [13] -->
at 𝑡= 1000.

<!-- b000273 | prose | pages [13] -->
Figure 6a and 6b provide fascinating insight into the behavior of the two plants, which appear to be directly competing for space. Indeed, in any given location, either the first species or second species thrives, but never both—this makes sense under the model’s definition, as only one species of plant is ultimately able to utilize the water at any given spatial coordinate in the long-term.

<!-- b000274 | prose | pages [13] -->
Figure 6c, when observed relative to Figure 4e, shows us that in spite of the species competition, the total biomass increases significantly—in fact by over two times. This indicates the existence of species cooperation, which can be explained mechanistically by the fact that more plants in the system preserves water by optimizing water utilization; that is, less water is allowed to leave the system through drainage because it is being conserved within plants. In addition, observe that in the two-species scenario, plants physically occupy the entire system, while the plants in the one-species scenario form clusters and strips that fail to occupy the entire habitat. This mirrors the process of diversification: with a more diverse array of plant species, more spatial domains within the habitat can be occupied.

<!-- b000275 | prose | pages [13] -->
We will now explore whether these results hold as the number of unique plant species continues to rise. In particular, we hope to investigate how patterns of species competition change and evolve as there multiple competitive interaction occurring over space and water at any given time and spatial coordinate. Therefore, we first the system to 𝑘= 3, which simulates a plant community with three unique species.

<!-- b000276 | furniture | pages [14] -->
Team # 2322687

<!-- b000277 | furniture | pages [14] -->
Page 14 of 25

<!-- b000278 | prose | pages [14] -->
(a) Species 1 of 3 (b) Species 2 of 3 (c) Species 3 of 3

<!-- b000279 | prose | pages [14] -->
(d) Total biomass of the system over time.

<!-- b000280 | caption | pages [14] -->
Figure 7: The change of a community with three species of plants over time. All snapshots are

<!-- b000281 | prose | pages [14] -->
taken at 𝑡= 1000.

<!-- b000282 | prose | pages [14] -->
Unlike the 𝑘= 2 instance, where at any given spatial coordinate only one plant is able to thrive, species competition is not as easily observed in the 𝑘= 3 case. However, the phenomenon of the three species competing with each other for water can still be identified: for instance, consider the small region, roughly defined by ((0, 100), (100, 200)), where species 3—which occupies most of the habitat—fails to grow, as shown in Figure 7c. Within this region, the upper portion is occupied by species 1, while the lower-left portion is occupied by species 2—the boundaries are simply not as well-defined as in the two-species scenario. In addition, one may observe that at any given spatial coordinate, not all three species appear to thrive.

<!-- b000283 | prose | pages [14] -->
However, we are again interested in measuring the success and growth of the overall system, as measured by total plant biomass. Figure 7c shows that again, despite inter-species competition, the total amount of biomass in the system increases—though by a notably less margin than the increase from one to two species. Indeed, the total biomass now peaks about 20% higher than it did in the two-plant scenario between droughts, which is significant but not nearly as significant as in the increase from one to two plants. This suggests that the system does not benefit indefinitely from more biodiversity, and that as the number of unique species rises, the increased inter-species competition that results produces increasingly detrimental effects on the total biomass of the system.

<!-- b000284 | prose | pages [14] -->
To investigate this phenomenon further, we experiment with 𝑘= 4.

<!-- b000285 | furniture | pages [15] -->
Team # 2322687

<!-- b000286 | furniture | pages [15] -->
Page 15 of 25

<!-- b000287 | prose | pages [15] -->
(a) Species 1 of 4 (b) Species 2 of 4 (c) Species 3 of 4 (d) Species 4 of 4

<!-- b000288 | prose | pages [15] -->
(e) Total biomass of the system over time. Note that the sim- ulation begins roughly one-third of the way through, at 𝑡= 350. This was done to save computation time, as numerically solving a system of five PDEs can be incredibly time-consuming.

<!-- b000289 | caption | pages [15] -->
Figure 8: The change of a community with four species of plants over time. All snapshots are taken

<!-- b000290 | prose | pages [15] -->
at 𝑡= 1000.

<!-- b000291 | prose | pages [15] -->
This scenario also raises fascinating insight into the nature of inter-species competition. As Figure 8 shows, in the four-species case, the total biomass at the end of the simulation is lower than in the three-species case, suggesting that the number of unique plant species cannot increase indefinitely at the benefit of the overall system. Indeed, at a certain point, the amount of competition generated between the plant species for water negates the total amount of water conserved within the system due to the plants. This threshold is not necessary four species, and can depend on the random initial conditions and the parameters; however, this insight reveals the fact that phenomenologically, increasing the amount of unique plant species infinitely does not necessarily benefit the overall system.

<!-- b000292 | prose | pages [15] -->
4.2 Different Types of Droughts

<!-- b000293 | prose | pages [15] -->
We can also consider different types of droughts that impact the system; in particular, we examine their severity (how significant the decline in rainfall is), duration (how long the drought is), and their frequency (how many droughts occur within the simulation). To ensure that the qualities of the drought are affecting the model’s results, we will keep all other parameters constant. We select 𝑘= 2 for the sake of reducing computation times while still considering the effect of inter-species competition.

<!-- b000294 | prose | pages [15] -->
First, we examine a more severe drought of the one used initially, where the levels of rainfall during periods of drought are even lower than the ones shown in Figure 2.

<!-- b000295 | furniture | pages [16] -->
Team # 2322687

<!-- b000296 | prose | pages [16] -->
𝑡= 200

<!-- b000297 | prose | pages [16] -->
𝑡= 600

<!-- b000298 | furniture | pages [16] -->
Page 16 of 25

<!-- b000299 | prose | pages [16] -->
𝑡= 750

<!-- b000300 | prose | pages [16] -->
𝑡= 1000

<!-- b000301 | prose | pages [16] -->
𝑡= 600: species 1 after

<!-- b000302 | prose | pages [16] -->
(a) 𝑡= 200 𝑡= 200: species 1 before

<!-- b000303 | prose | pages [16] -->
(b) 𝑡= 600

<!-- b000304 | prose | pages [16] -->
the first drought.

<!-- b000305 | prose | pages [16] -->
the second drought.

<!-- b000306 | prose | pages [16] -->
𝑡= 200

<!-- b000307 | prose | pages [16] -->
𝑡= 750

<!-- b000308 | prose | pages [16] -->
(c) 𝑡= 750 𝑡= 750: species 1 before

<!-- b000309 | prose | pages [16] -->
(d) 𝑡= 1000 𝑡= 1000: species 1 in re-

<!-- b000310 | prose | pages [16] -->
the third drought.

<!-- b000311 | prose | pages [16] -->
covery from drought

<!-- b000312 | prose | pages [16] -->
𝑡= 600

<!-- b000313 | prose | pages [16] -->
𝑡= 1000

<!-- b000314 | prose | pages [16] -->
𝑡= 750: species 2 before

<!-- b000315 | prose | pages [16] -->
(e) 𝑡= 200 𝑡= 200: species 2 before

<!-- b000316 | prose | pages [16] -->
(f) 𝑡= 750

<!-- b000317 | prose | pages [16] -->
the first drought.

<!-- b000318 | prose | pages [16] -->
the third drought.

<!-- b000319 | prose | pages [16] -->
(g) 𝑡= 600 𝑡= 600: species 2 after

<!-- b000320 | prose | pages [16] -->
(h) 𝑡= 1000 𝑡= 1000: species 2 in re-

<!-- b000321 | prose | pages [16] -->
the second drought.

<!-- b000322 | prose | pages [16] -->
covery from drought

<!-- b000323 | prose | pages [16] -->
(i) Total biomass of the system over time

<!-- b000324 | caption | pages [16] -->
Figure 9: Dynamics of the two-plant system with severe drought cycles.

<!-- b000325 | prose | pages [16] -->
Figure 9c shows the impact of the increased severity: following periods of drought, there are almost no plants remaining, though the clustered shapes of the plants remain. However, the plants are able to make a quick recovery from these periods of drought, as they have not completely gone extinct, as shown in Figures 9e-9h. Figure 9i highlights the drastic peaks and troughs that occur as a result of the severe droughts, with the total biomass of the system nearly falling to zero at certain points.

<!-- b000326 | prose | pages [16] -->
Next, we consider greater frequencies of droughts, where the severity of the droughts is lower but they occur more often. Specifically, we expand upon the rainfall model shown in Figure 2, and incorporate droughts from 𝑡= 200 to 𝑡= 300, 𝑡= 400 to 𝑡= 500, 𝑡= 600 to 𝑡= 700, and 𝑡= 800 to 𝑡= 900.

<!-- b000327 | furniture | pages [17] -->
Team # 2322687

<!-- b000328 | prose | pages [17] -->
𝑡= 200

<!-- b000329 | prose | pages [17] -->
𝑡= 650

<!-- b000330 | furniture | pages [17] -->
Page 17 of 25

<!-- b000331 | prose | pages [17] -->
𝑡= 1000

<!-- b000332 | prose | pages [17] -->
𝑡= 650: species 1 after a second

<!-- b000333 | prose | pages [17] -->
(a)𝑡= 200 𝑡= 200: species 1 before the first

<!-- b000334 | prose | pages [17] -->
(b) 𝑡= 650

<!-- b000335 | prose | pages [17] -->
drought.

<!-- b000336 | prose | pages [17] -->
drought.

<!-- b000337 | prose | pages [17] -->
𝑡= 200

<!-- b000338 | prose | pages [17] -->
𝑡= 650

<!-- b000339 | prose | pages [17] -->
(c) 𝑡= 1000 𝑡= 1000: species 1 in recovery from drought

<!-- b000340 | prose | pages [17] -->
𝑡= 1000

<!-- b000341 | prose | pages [17] -->
𝑡= 650: species 2 after a second

<!-- b000342 | prose | pages [17] -->
(d)𝑡= 200 𝑡= 200: species 2 before the first

<!-- b000343 | prose | pages [17] -->
(e) 𝑡= 650

<!-- b000344 | prose | pages [17] -->
drought.

<!-- b000345 | prose | pages [17] -->
drought.

<!-- b000346 | prose | pages [17] -->
(f) 𝑡= 1000 𝑡= 1000: species 2 in recovery from drought

<!-- b000347 | prose | pages [17] -->
(g) Total biomass of the system over time

<!-- b000348 | caption | pages [17] -->
Figure 10: Dynamics of the two-plant system with more frequent drought cycles.

<!-- b000349 | caption | pages [17] -->
Figure 10 shows that more frequent droughts, unlike more severe droughts, do not ever threaten

<!-- b000350 | prose | pages [17] -->
the overall existence of the plant community. Indeed, Figure 10c and 10d show that the plants are still considerably alive after periods of drought, while Figure 10g illustrates that the differences between drought and non-drought periods are not as extreme. This suggests that generally, more frequent but less severe droughts are preferable to their alternative.

<!-- b000351 | prose | pages [17] -->
5

<!-- b000352 | heading | pages [17] -->
Sensitivity Analysis

<!-- b000353 | prose | pages [17] -->
We are also interested in studying the types of plant species within the system, as well as other factors such as pollution and habitat reduction.

<!-- b000354 | prose | pages [17] -->
5.1 Types of Species

<!-- b000355 | prose | pages [17] -->
The parameterization of growth rates and mortality rates allow us to study different types of plants—in particular, we focus on two main characteristics that are commo in ecological classification: resilience

<!-- b000356 | furniture | pages [18] -->
Team # 2322687

<!-- b000357 | furniture | pages [18] -->
Page 18 of 25

<!-- b000358 | prose | pages [18] -->
and resistance. Resilience is defined as the ability of a plant as a species to recover after a drought; that is, its ability to reproduce to return to its previous biomass. Resistance is defined as the ability of individual plants within a species to survive environmental stress

<!-- b000359 | prose | pages [18] -->
Thus, we can use the growth rate parameter 𝑐𝑖as a proxy to measure the impact of plant species resilience. Specifically, recalling a baseline value of 𝑐𝑖= 1, we investigate two cases: 𝑐𝑖= 0.8, where plants are less resilient, and 𝑐𝑖= 1.2, where plants are more resilient.

<!-- b000360 | prose | pages [18] -->
𝑐= 0.8 (a) Species 1 of 2 with 𝑐= 0.8 𝑐= 0.8 .

<!-- b000361 | prose | pages [18] -->
𝑐= 0.8 (b) Species 2 of 2 with 𝑐= 0.8 𝑐= 0.8.

<!-- b000362 | prose | pages [18] -->
𝑐= 0.8 (c) Biomass over time with 𝑐= 0.8 𝑐= 0.8.

<!-- b000363 | caption | pages [18] -->
Figure 11: A two-plant community with lower resilience levels. All snapshots are taken at 𝑡= 1000.

<!-- b000364 | prose | pages [18] -->
Introducing species of plants with lower resilience (i.e., lower growth rates), produces similar results to the original simulation shown in Figure 6. However, as expected, observe that the overall biomass of each plant species has been significantly reduced. In particular, though the growth factor was reduced by just 20%, the overall biomass of the system—when compared to the results shown in Figure 6c—increased by significantly more, suggesting that plant resilience drives growth in more than just a linear fashion. This makes sense when examined against the model itself, where the system of PDEs are composed of several interaction terms that generate complex, nonlinear relationships between the parameters and dependent variables.

<!-- b000365 | furniture | pages [19] -->
Team # 2322687

<!-- b000366 | prose | pages [19] -->
𝑐= 1.2 (a) Species 1 of 2 with 𝑐= 1.2 𝑐= 1.2.

<!-- b000367 | furniture | pages [19] -->
Page 19 of 25

<!-- b000368 | prose | pages [19] -->
𝑐= 1.2 (b) Species 2 of 2 with 𝑐= 1.2 𝑐= 1.2.

<!-- b000369 | prose | pages [19] -->
𝑐= 1.2 (c) Biomass over time with 𝑐= 1.2 𝑐= 1.2

<!-- b000370 | caption | pages [19] -->
Figure 12: A two-plant community with higher resilience levels. All snapshots are taken at 𝑡= 1000.

<!-- b000371 | prose | pages [19] -->
Meanwhile, introducing plants with greater resilience (higher growth rates), yields similarly corre- sponding effects. While Figure 12c shows that the overall behavior of the system is relatively consistent as the original example, the overall biomass of each species is significant higher. Again, the resulting increases in biomass are greater than the raw increase in resilience, suggesting a nonlinear relationship that is produced by the highly interconnected nature of the model. Specifically, as the biomass of plants increases, more water is conserved in the overall system, meaning less water is lost out of the system from evaporation.

<!-- b000372 | prose | pages [19] -->
5.2 Resistance and Pollution

<!-- b000373 | prose | pages [19] -->
Continuing our analysis to consider the impact of changes in the resistance of plant species, we can use the plant mortality rate, 𝑚𝑖, as a proxy for resistance. Logically, plants with higher resistance have lower mortality rates compared to plants with lower resistance during similar environmental conditions.

<!-- b000374 | prose | pages [19] -->
Our model also can accounts for changes in the system based on the presence of pollution within the system. We know that plants affected by pollution exhibit higher mortality rates at equivalent water consumption levels [13]. Indeed, the resilience characteristic of plants which measures its ability to handle stress can also be applied to the environmental stress of pollution.

<!-- b000375 | prose | pages [19] -->
Thus, we simulate the impact of the presence or absence of habitat-wide pollution on the basis of plant resistance by changing the mortality rate 𝑚𝑖of the plant species. Specifically, given our baseline value of 𝑚= 0.05, we simulated scenarios with 𝑚= 0.03, where there is reduced pollution, and 𝑚= 0.07, where there is increased pollution.

<!-- b000376 | furniture | pages [20] -->
Team # 2322687

<!-- b000377 | prose | pages [20] -->
𝑚= 0.03 (a) Species 1 of 2 with 𝑚= 0.03 𝑚= 0.03.

<!-- b000378 | furniture | pages [20] -->
Page 20 of 25

<!-- b000379 | prose | pages [20] -->
𝑚= 0.03 (b) Species 2 of 2 with 𝑚= 0.03 𝑚= 0.03.

<!-- b000380 | prose | pages [20] -->
𝑚= 0.03 (c) Biomass over time with 𝑚= 0.03 𝑚= 0.03.

<!-- b000381 | caption | pages [20] -->
Figure 13: A two-plant community as affected by lower levels pollution, producing a lower

<!-- b000382 | prose | pages [20] -->
mortality rates. All snapshots are taken at 𝑡= 1000.

<!-- b000383 | caption | pages [20] -->
Figure 13 shows the consequences of reducing pollution and therefore mortality rates. As expected,

<!-- b000384 | prose | pages [20] -->
total plant biomass is increased over time, though the overall behavior of the system remains similar. The clustering patterns of the plants are relatively consistent to previous findings.

<!-- b000385 | prose | pages [20] -->
𝑚= 0.07 (a) Species 1 of 2 with 𝑚= 0.07 𝑚= 0.07.

<!-- b000386 | prose | pages [20] -->
𝑚= 0.07 (b) Species 2 of 2 with 𝑚= 0.07 𝑚= 0.07.

<!-- b000387 | prose | pages [20] -->
𝑚= 0.07 (c) Biomass over time with 𝑚= 0.07 𝑚= 0.07.

<!-- b000388 | caption | pages [20] -->
Figure 14: Two-plant communities as affected by higher levels pollution, producing a higher

<!-- b000389 | prose | pages [20] -->
mortality rates. All snapshots are taken at 𝑡= 1000.

<!-- b000390 | furniture | pages [21] -->
Team # 2322687

<!-- b000391 | furniture | pages [21] -->
Page 21 of 25

<!-- b000392 | prose | pages [21] -->
Similarly, Figure 14 shows the consequences of increasing pollution levels, thereby driving up mortality rates of plants. In this case, plant biomass decreases at all periods of time, but again the behavior of the overall system remains consistent. Notice that in both scenarios, the total biomass of the system increases or decreases by a greater factor than just the raw change in mortality rate, emphasizing how the interconnected of the PDE system equates to nonlinear responses to parameter values.

<!-- b000393 | prose | pages [21] -->
5.3 Habitat Reduction

<!-- b000394 | prose | pages [21] -->
Habitat reduction is another key factor that should be considered when modeling plant growth, becoming increasingly important in modern-day climates. Due to the spatial capabilities of our model, we can easily model habitat reduction by reducing the total region available for plants, as governed by 𝐿.

<!-- b000395 | prose | pages [21] -->
We explore two possible reductions: one minor one, given by 𝐿= 300, and one major one, given by 𝐿= 100.

<!-- b000396 | prose | pages [21] -->
𝐿= 300 (a) Species 1 of 2 with 𝐿= 300 𝐿= 300.

<!-- b000397 | prose | pages [21] -->
𝐿= 300 (b) Species 2 of 2 with 𝐿= 300 𝐿= 300.

<!-- b000398 | prose | pages [21] -->
𝐿= 300 (c) Biomass over time with 𝐿= 300 𝐿= 300

<!-- b000399 | caption | pages [21] -->
Figure 15: System dynamics with a minor habitat reduction

<!-- b000400 | prose | pages [21] -->
When the habitat experiences a minor reduction in size, the behavior of the plant growth appears similar, though with fewer independent clusters, as shown in Figures 15a and 15b. This makes sense, as a reduction in the total area available for the plants to grow will naturally reduce the number of clusters they can form. However, as shown in Figure 15c, the overall dynamics of the system appear similar to the original; the only difference is the total biomass, which has reduced as expected.

<!-- b000401 | furniture | pages [22] -->
Team # 2322687

<!-- b000402 | prose | pages [22] -->
𝐿= 100 (a) Species 1 of 2 with 𝐿= 100 𝐿= 100.

<!-- b000403 | furniture | pages [22] -->
Page 22 of 25

<!-- b000404 | prose | pages [22] -->
𝐿= 100 (b) Species 2 of 2 with 𝐿= 100 𝐿= 100.

<!-- b000405 | prose | pages [22] -->
𝐿= 100 (c) Biomass over time with 𝐿= 100 𝐿= 100.

<!-- b000406 | caption | pages [22] -->
Figure 16: System dynamics with a major habitat reduction

<!-- b000407 | caption | pages [22] -->
Figure 16 provides another set of highly interesting results. Indeed, when the given habitat is

<!-- b000408 | prose | pages [22] -->
small enough, one plant dies completely while the other manages to survive, spreading throughout the entire system. This further supports the existence of spatial competition between species, which is emphasized when the habitat is reduced dramatically. Figure 16c highlights how the first species gradually dies over time and fails to revitalize, even in spite of periods of sufficient rainfall, while the second species takes over completely, presumably due to a more optimal set of initial conditions.

<!-- b000409 | prose | pages [22] -->
This test with two species reveals an a crucial overall negative effect of habitat destruction; there exists a point of when the smaller spatial habitat can no longer support two species due to intensified competition for limited resources, resulting in the extinction of one of the two species. This concept connecting habitat reduction and biodiversity reduction can be applied to any number of species. The eventual outcome of habitat destruction taken to the extreme is therefore arguably a single surviving species with is the best at competing against other species, but importantly not necessarily the best at surviving environmental stresses like drought.

<!-- b000410 | prose | pages [22] -->
Thus, when considering habitat destruction in conjunction with cycles of drought, we see from our plant community model that the resulting fewer species from habitat destruction implies that the community becomes more vulnerable and less stable to droughts.

<!-- b000411 | furniture | pages [23] -->
Team # 2322687

<!-- b000412 | furniture | pages [23] -->
Page 23 of 25

<!-- b000413 | prose | pages [23] -->
6

<!-- b000414 | heading | pages [23] -->
Strengths and Weaknesses

<!-- b000415 | prose | pages [23] -->
6.1

<!-- b000416 | heading | pages [23] -->
Strengths

<!-- b000417 | prose | pages [23] -->
• The use of a spatial model is dynamic and comprehensive. We not only consider rainfall but also the diffusion of groundwater which accounts for the natural permeability of the ground. Location-specific competition fits the reality of the localization of immobile plants and the natural clumping of plants through real-world drought scenarios.

<!-- b000418 | prose | pages [23] -->
• The randomization built into our two models simulates the real world. Random initial seeding results in more natural initial plant dispersion. The randomization of daily rainfall within certain ranges further conforms more to nature than a constant rain function.

<!-- b000419 | prose | pages [23] -->
• Our parameterized rain and drought model can simulate a wide range of different droughts. The choice in length, severity and appearance results in greater objectivity and control when analyzing the impact of drought cycles on the plant community model. This is in contrast to real-world data where all data is observational, potentially incomplete, and not as controlled to effectively isolate and test the three parameters.

<!-- b000420 | prose | pages [23] -->
• The development of a phenomenological, mechanistic model (e.g. one that is based on the theoretical relationship between the variables) rather than a data-driven model allows us to model the interconnectedness of the system and robustly evaluate the relationship between various aspects of the plant community.

<!-- b000421 | prose | pages [23] -->
6.2

<!-- b000422 | heading | pages [23] -->
Weaknesses

<!-- b000423 | prose | pages [23] -->
• Our model requires the use of significant computational power, as our model considers water availability and plant competition for each point within a 500 by 500 spatial map for each of the 1000 weeks. The linear increase in the number of distinct species results in a non-linear increase in runtime due to the increased complexity of modeling competition for each of the species.

<!-- b000424 | prose | pages [23] -->
• Our model only considers the impact of the variability of water scarcity and its corresponding effect on plant competition and assumes other factors such as soil nutrients and exposure to sunlight are constant for all plant communities.

<!-- b000425 | prose | pages [23] -->
7

<!-- b000426 | heading | pages [23] -->
Conclusion

<!-- b000427 | prose | pages [23] -->
Our plant growth model provides evidence which supports the initial observation that increased bio- diversity can support a plant community’s survivability during drought cycles. Incorporating custom- generated rainfall data that simulates multiple cycles of droughts, we addressed each of the points presented in the initial problem restatement:

<!-- b000428 | prose | pages [23] -->
1. In spite of inter-species competition in times of drought, multiple species of plants mutually benefit from one another as an increase in total biomass of plants allows for greater water conservation from evaporation or drainage.

<!-- b000429 | furniture | pages [24] -->
Team # 2322687

<!-- b000430 | furniture | pages [24] -->
Page 24 of 25

<!-- b000431 | prose | pages [24] -->
2. Only two species are required to benefit from the biodiversity phenomenon. This is also where the greatest marginal benefit occurs, with diminishing returns for each additional species onward. As the number of plants increases, we see a greater spatial occupation of biomass within the spatial density plots. This simulates how differences in the environmental niches of distinct species improve plant coverage and thus reduce water loss from drainage.

<!-- b000432 | prose | pages [24] -->
3. The frequency of droughts is not as damaging to the overall biomass of a plant community as the severity. Plants generally recover from high frequency but low severity droughts while there remains a risk of extinction or near biomass disappearance for species during severe droughts.

<!-- b000433 | prose | pages [24] -->
4. Resilience and resistance characteristics of each species affects the species’ growth and mortality rate, respectively. A decrease in resilience and higher pollution result in reduced long-term biomass, as expected.

<!-- b000434 | prose | pages [24] -->
5. Given the spatial nature of our model, simulating habitat reduction was simply reduction in the total area available to plants to grow. We discovered that competition intensified given the same number of species, and that in highly restricted areas, species can even dominate the system or become extinct entirely.

<!-- b000435 | prose | pages [24] -->
Therefore, to ensure the long-term viability of a plant community, biodiversity must be protected and maintained. Presence of biodiversity in plant community comes at the cost of inter-species competition, which therefore naturally reduces the biomass of each individual species in the environment, but is helpful by increasing net total plant biomass and increasing the chances of surviving and adapting to cycles of drought and other unexpected stresses.

<!-- b000436 | prose | pages [24] -->
8 Future Exploration

<!-- b000437 | prose | pages [24] -->
Our current model assumes that regardless of the environment, water escapes at a rate proportional to the current amount of water with the same constant of proportionality for all biomes. Developing a system based on climate and soil data for different biomes will allow to apply our models to a more diverse set of conditions with no modifications to core model itself. Additionally, expanding our model to describe complex, non-flat terrain such as mountains and hills can offer more insights into which areas are most survivable for the plants in drought conditions.

<!-- b000438 | furniture | pages [25] -->
Team # 2322687

<!-- b000439 | heading | pages [25] -->
References

<!-- b000440 | furniture | pages [25] -->
Page 25 of 25

<!-- b000441 | references | pages [25] -->
[1] A. Kaisermann, F. T. de Vries, R. I. Griffiths, and R. D. Bardgett, “Legacy effects of drought

<!-- b000442 | references | pages [25] -->
on plant–soil feedbacks and plant–plant interactions,” New Phytologist, vol. 215, no. 4, pp.

<!-- b000443 | references | pages [25] -->
1413–1424, 2017.

<!-- b000444 | references | pages [25] -->
[2] S. Direct. Plant communities. [Online]. Available:

<!-- b000445 | references | pages [25] -->
https://www.sciencedirect.com/topics/

<!-- b000446 | references | pages [25] -->
agricultural-and-biological-sciences/plant-communities

<!-- b000447 | references | pages [25] -->
[3] F. T. de Vries, M. E. Liiri, L. Bjørnlund, H. M. Set¨al¨a, S. Christensen, and R. D. Bardgett, “Legacy

<!-- b000448 | references | pages [25] -->
effects of drought on plant growth and the soil food web,” Oecologia, vol. 170, pp. 821–833,

<!-- b000449 | references | pages [25] -->
2012.

<!-- b000450 | references | pages [25] -->
[4] T. S. Writer. Ecological resilience and resistance. [Online]. Available:

<!-- b000451 | references | pages [25] -->
https://www.

<!-- b000452 | references | pages [25] -->
thesciencewriter.org/resilience-stories/ecological-resilience-and-resistance

<!-- b000453 | references | pages [25] -->
[5] S. Yachi and M. Loreau, “Biodiversity and ecosystem productivity in a fluctuating environment:

<!-- b000454 | references | pages [25] -->
The insurance hypothesis,” Proceedings of the National Academy of Sciences, vol. 96, no. 4, pp.

<!-- b000455 | references | pages [25] -->
1463–1468, 1999.

<!-- b000456 | references | pages [25] -->
[6] A. J. Lotka, “Contribution to the theory of periodic reactions,” Jan. 1909.

<!-- b000457 | references | pages [25] -->
[7] J. Monod, “The growth of bacterial cultures,” Annual Review of Microbiology, vol. 3, no. 1, pp.

<!-- b000458 | references | pages [25] -->
371–394, 1949. [Online]. Available: https://doi.org/10.1146/annurev.mi.03.100149.002103

<!-- b000459 | references | pages [25] -->
[8] H. H. Elsalahy, S. D. Bellingrath-Kimura, C.-L. Roß, T. Kautz, and T. F. D¨oring, “Crop

<!-- b000460 | references | pages [25] -->
resilience to drought with and without response diversity,” Frontiers in Plant Science, vol. 11,

<!-- b000461 | references | pages [25] -->
2020. [Online]. Available: https://www.frontiersin.org/articles/10.3389/fpls.2020.00721

<!-- b000462 | references | pages [25] -->
[9] D. U. Hooper and P. M. Vitousek, “The effects of plant composition and diversity on ecosystem

<!-- b000463 | references | pages [25] -->
processes,” Science, vol. 277, no. 5330, pp. 1302–1305, 1997.

<!-- b000464 | references | pages [25] -->
[10] T. D., D. Wedin, and K. J., “Productivity and sustainability influenced by biodiversity in grassland

<!-- b000465 | references | pages [25] -->
ecosystems,” Nature, vol. 379, pp. 718–720, 1996.

<!-- b000466 | references | pages [25] -->
[11] S. Naeem, L. Thompson, and L. S., “Declining biodiversity can alter the performance of ecosys-

<!-- b000467 | references | pages [25] -->
tems,” Nature, vol. 368, pp. 734–747, 1994.

<!-- b000468 | references | pages [25] -->
[12] J. A. Sherratt, Vegetation Stripes in Semi-Arid Environments.

<!-- b000469 | references | pages [25] -->
[13] G.

<!-- b000470 | references | pages [25] -->
Tumble.

<!-- b000471 | references | pages [25] -->
What

<!-- b000472 | references | pages [25] -->
is

<!-- b000473 | references | pages [25] -->
the

<!-- b000474 | references | pages [25] -->
effect

<!-- b000475 | references | pages [25] -->
of

<!-- b000476 | references | pages [25] -->
University of Sheffield, 2006.

<!-- b000477 | references | pages [25] -->
the

<!-- b000478 | references | pages [25] -->
pollution

<!-- b000479 | references | pages [25] -->
on

<!-- b000480 | references | pages [25] -->
plants.

<!-- b000481 | references | pages [25] -->
[Online].

<!-- b000482 | references | pages [25] -->
Available:

<!-- b000483 | references | pages [25] -->
https://greentumble.com/effect-of-pollution-on-plants/
