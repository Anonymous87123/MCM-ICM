# P-A-2023-2300336-6b706496

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
2023

<!-- b000002 | prose | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | title | pages [1] -->
A

<!-- b000005 | title | pages [1] -->
2300336

<!-- b000006 | title | pages [1] -->
MCM/ICM

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Community Succession Simulation: Surviving Drought

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
The species richness of plant communities has a significant influence on their ability to withstand drought. From an ecological niche perspective, we simulate plant community succession under drought conditions and analyze the effects of various factors.

<!-- b000011 | prose | pages [1] -->
First, we develop the Plant Community Succession Model based on niche theory to simulate community succession under drought conditions. The model applies changes in niche width as the indicator to simulate community succession and utilizes competition matrix to describe in- teractions between species, including competition and facilitation. Then, the Niche Width Model is established, comprehensively considering the effects of reproduction, mortality, and uncer- tainties. Among them, reproduction depends on the degree of drought, niche width, interspecific relationships, and environmental capacity, while mortality depends on the degree of drought and the niche width. Uncertainties are measured with Gaussian white noise.

<!-- b000012 | prose | pages [1] -->
A niche width differential equation model is built based on the Beverton-Holt and the Lotka- Volterra equations. To account for various irregular weather cycles, we utilize random variables

<!-- b000013 | prose | pages [1] -->
obeying normal distribution to simulate the extent and duration of drought. As a case study, we simulate the evolution of a three-species community and draw the conclusion that the total niche width of the community increases, suggesting long-term survival.

<!-- b000014 | prose | pages [1] -->
To investigate the influence of species number on community dynamics, we utilize the Plant Community Evolution Model to simulate communities containing one to four species separately. The results demonstrate that three species are necessary for the community to benefit. Additionally, as the number of species increases, the drought resistance improves and then stabilizes.

<!-- b000015 | prose | pages [1] -->
Based on the competition matrix, we set up three distinct communities and discuss their drought resistance through simulations. It can be concluded that facilitation-dominated relationships en- hance drought resistance and increase the community’s survival time. Moreover, we vary the frequency and intensity of drought and then conclude that species extinction is more likely to occur during severe droughts.

<!-- b000016 | prose | pages [1] -->
Pollution and habitat shrinkage affect plant communities’ niche width and competitive rela- tionships. Therefore, we adjust the niche width and competition matrix accordingly. The results indicate that pollution and habitat shrinkage may cause the extinction of certain species.

<!-- b000017 | prose | pages [1] -->
Finally, based on the impact of various factors, we recommend some measures to ensure the long-term viability of a plant community. Additionally, we also analyze the significance of protecting vulnerable communities for the overall health of ecosystems.

<!-- b000018 | keywords | pages [1] -->
Keywords: Community succession; Drought resistance; Niche width; Population interactions;

<!-- b000019 | prose | pages [1] -->
Beverton-Holt equation

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1

<!-- b000022 | heading | pages [2] -->
Introduction

<!-- b000023 | prose | pages [2] -->
2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000024 | prose | pages [2] -->
2

<!-- b000025 | heading | pages [2] -->
Notations and Assumptions

<!-- b000026 | prose | pages [2] -->
2

<!-- b000027 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000028 | heading | pages [2] -->
Notations

<!-- b000029 | prose | pages [2] -->
4 Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000030 | prose | pages [2] -->
3

<!-- b000031 | heading | pages [2] -->
Plant Community Evolution Model

<!-- b000032 | prose | pages [2] -->
4

<!-- b000033 | prose | pages [2] -->
5 Model Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 5 Initial Conditions and Niche Characteristics of Species 3.2 . . . . . . . . . . . . . . .

<!-- b000034 | prose | pages [2] -->
6 Rules of Plant Community Evolution . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 7 Effects of Species Reproduction on Niche Width 3.3.1 . . . . . . . . . . . . . .

<!-- b000035 | prose | pages [2] -->
8 Effects of Species Mortality on Niche Width . . . . . . . . . . . . . . . . . 3.3.2 9 Irregular Weather Cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 10 Simulation of Plant Community Evolution . . . . . . . . . . . . . . . . . . . . . . 3.5 11 Plant Species and Initial Parameters . . . . . . . . . . . . . . . . . . . . . 3.5.1 11 Irregular Weather Simulation . . . . . . . . . . . . . . . . . . . . . . . . . 3.5.2 12 Simulation Results of Species Evolution . . . . . . . . . . . . . . . . . . . 3.5.3 13

<!-- b000036 | heading | pages [2] -->
Application of Plant Community Evolution Model

<!-- b000037 | prose | pages [2] -->
4 15 Effect of the Number of Species on the Community . . . . . . . . . . . . . . . . . 4.1 15 The Minimal Number of Species for the Community to Benefit . . . . . . . 4.1.1 15 The Effect of Increasing Species Number on Community . . . . . . . . . . 4.1.2 17 Impact of the Types of Species on Community Evolution . . . . . . . . . . . . . . 4.2 17 The Effects of the Severity of Drought . . . . . . . . . . . . . . . . . . . . . . . . 4.3 18 The impact of Pollution and Habitat Reduction . . . . . . . . . . . . . . . . . . . . 4.4 19 Measures that Allow a Plant Community to Live Longer . . . . . . . . . . . . . . . 4.5

<!-- b000038 | prose | pages [2] -->
5

<!-- b000039 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000040 | prose | pages [2] -->
5.1 Sensitivity to Unpredictable Factors

<!-- b000041 | prose | pages [2] -->
20

<!-- b000042 | prose | pages [2] -->
21 . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | prose | pages [2] -->
21 Sensitivity to Drought Coefficient . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2

<!-- b000044 | prose | pages [2] -->
6

<!-- b000045 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000046 | prose | pages [2] -->
22

<!-- b000047 | prose | pages [2] -->
23 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 23 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000048 | prose | pages [2] -->
7

<!-- b000049 | heading | pages [2] -->
Conclusion

<!-- b000050 | prose | pages [2] -->
Referrence

<!-- b000051 | prose | pages [2] -->
23

<!-- b000052 | prose | pages [2] -->
23

<!-- b000053 | prose | pages [2] -->
24

<!-- b000054 | furniture | pages [3] -->
Team # 2300336

<!-- b000055 | furniture | pages [3] -->
Page 2 of 24

<!-- b000056 | prose | pages [3] -->
1

<!-- b000057 | heading | pages [3] -->
Introduction

<!-- b000058 | prose | pages [3] -->
1.1

<!-- b000059 | heading | pages [3] -->
Background

<!-- b000060 | prose | pages [3] -->
Plants of different species possess varying susceptibilities and abilities to resist drought[1]. Ex- tensive observations have indicated that the species richness of plant communities significantly impacts their ability to adapt to water scarcity over the long term[2]. Communities containing a larger number of species tend to exhibit higher resistance to drought stress in subsequent genera- tions, whereas those with fewer species exhibit lower resistance. Thus, analyzing the association between drought adaptability and the number of species in plant communities is critical for their survival over extended periods.

<!-- b000061 | caption | pages [3] -->
Figure 1: World drought situation from NIDIS

<!-- b000062 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000063 | prose | pages [3] -->
• Develop a model to predict the evolution of plant communities under various irregular weather cycles and consider the interactions between species.

<!-- b000064 | prose | pages [3] -->
• Determine the minimum number of species required for the community to benefit and the impact of increased species numbers on the community.

<!-- b000065 | prose | pages [3] -->
• Analyze the effect of species type on community evolution

<!-- b000066 | prose | pages [3] -->
• Discuss the impact of the greater or less frequency and width of drought.

<!-- b000067 | prose | pages [3] -->
• Analyze the impact of other factors such as pollution and habitat reduction on the model

<!-- b000068 | prose | pages [3] -->
• According to the model, determine what should be done to ensure the long-term viability of a plant community and the impacts on the larger environment.

<!-- b000069 | prose | pages [3] -->
1.3 Our Work

<!-- b000070 | prose | pages [3] -->
To sum up the full article, we

<!-- b000071 | furniture | pages [4] -->
Team # 2300336

<!-- b000072 | furniture | pages [4] -->
Page 3 of 24

<!-- b000073 | prose | pages [4] -->
• develop an ecological niche model considering uncertain weather cycles to simulate plant community evolution. The model accounts for species interactions and successional pro- cesses based on inter-species competition, and establishes competition matrices to describe population interactions within the community.

<!-- b000074 | prose | pages [4] -->
• use the model to determine the minimum number of species required for a community to benefit from increased species numbers. The model considers the ecological niche width of each population under uncertain drought conditions, using differential equations based on the Beverton-Holt and Lotka-Volterra equations.

<!-- b000075 | prose | pages [4] -->
• analyze the impact of different species types on community evolution. The model shows that populations of different types have different interactions, and mutualism may lead to greater drought resistance. However, competition predominance during severe and prolonged droughts may cause population extinction, reducing species richness and community stability.

<!-- b000076 | prose | pages [4] -->
• study the effects of various drought cycles on community evolution using the model. The analysis reveals that frequent and longer droughts may have negative impacts on populations, while less frequent droughts may make populations more adaptable to drought environments.

<!-- b000077 | prose | pages [4] -->
• discuss the impact of other factors, such as pollution and habitat reduction, on community evolution. The model sets pollution and habitat reduction coefficients to affect ecological niche width and species interactions, thereby influencing community succession. Pollution and habitat reduction increase competition, allowing more competitive populations to occupy resources, but may lead to species extinction and affect community stability.

<!-- b000078 | prose | pages [4] -->
• propose measures to ensure the long-term viability of plant communities and their impacts on the larger environment. Increasing the number of species in a community may improve drought adaptability, but must be balanced with avoiding competition, ensuring mutualism, and reducing environmental pollution and habitat reduction to ensure community stability and long-term viability.

<!-- b000079 | caption | pages [4] -->
Figure 2: The flow chart of our work

<!-- b000080 | furniture | pages [5] -->
Team # 2300336

<!-- b000081 | furniture | pages [5] -->
Page 4 of 24

<!-- b000082 | prose | pages [5] -->
2

<!-- b000083 | heading | pages [5] -->
Notations and Assumptions

<!-- b000084 | prose | pages [5] -->
2.1

<!-- b000085 | heading | pages [5] -->
Notations

<!-- b000086 | heading | pages [5] -->
Symbols

<!-- b000087 | prose | pages [5] -->
Description

<!-- b000088 | prose | pages [5] -->
C Competition matrix of species

<!-- b000089 | prose | pages [5] -->
L Niche width of species

<!-- b000090 | prose | pages [5] -->
Γ Species’ sensitivity to drought

<!-- b000091 | prose | pages [5] -->
li(t) Niche width of the i-th species at time t

<!-- b000092 | prose | pages [5] -->
bi(t) Increase in niche width of the i-th species due to its reproduction

<!-- b000093 | prose | pages [5] -->
di(t) fraction of niche width of the i-th species reduced by death

<!-- b000094 | prose | pages [5] -->
σi(t) Gaussian white noise for unpredictability

<!-- b000095 | prose | pages [5] -->
K(t) Niche width of a community at time t

<!-- b000096 | prose | pages [5] -->
gi Growth rate of the i-th species under no competition condition

<!-- b000097 | prose | pages [5] -->
dr Drought coefficient that describes the extent of the drought

<!-- b000098 | prose | pages [5] -->
f(dr) Drought response function that impact death rate

<!-- b000099 | prose | pages [5] -->
tINR Time interval until the next drought

<!-- b000100 | prose | pages [5] -->
td Duration of the drought

<!-- b000101 | prose | pages [5] -->
2.2

<!-- b000102 | heading | pages [5] -->
Assumptions

<!-- b000103 | prose | pages [5] -->
To simplify the problem and make it convenient for us to simulate real-life conditions, we make the following basic assumptions, each of which is properly justified.

<!-- b000104 | prose | pages [5] -->
• Assumption 1: The number of species in the plant community will not increase. Justification: We assume a closed system where no new species are introduced or can colonize the plant community.

<!-- b000105 | prose | pages [5] -->
• Assumption 2: Species don’t mutate but the population and the resources it controls change over time. Justification: The timescale of the study is relatively short, and genetic changes and muta- tions that could lead to ecological changes are assumed to be negligible.

<!-- b000106 | heading | pages [5] -->
• Assumption 3: The competitive or mutually-beneficial relationship between species in a

<!-- b000107 | prose | pages [5] -->
community remains the same. Justification: The interactions between species in a community are complex and can change over time due to a variety of factors. This is to simplify the model and focus on the effects of drought on the community structure.

<!-- b000108 | prose | pages [5] -->
• Assumption 4: The drought sensitivity coefficient of each species in the community is fixed and does not change with time and space. Justification: To make the models simple and easy to understand, niche parameters for

<!-- b000109 | furniture | pages [6] -->
Team # 2300336

<!-- b000110 | furniture | pages [6] -->
Page 5 of 24

<!-- b000111 | prose | pages [6] -->
each species are often treated as invariants that can help us better understand the interactions between species and the effects of drought events on community structure.

<!-- b000112 | prose | pages [6] -->
3

<!-- b000113 | heading | pages [6] -->
Plant Community Evolution Model

<!-- b000114 | prose | pages [6] -->
Ecological niche refers to a species’ position in a community in terms of its functional relationships and roles with related species, considering time and space. Niche width is an indicator of the diversity of resources used by organisms [3]. The wider the niche width of a species, the less specialized it is, and the stronger its adaptability to the environment.

<!-- b000115 | prose | pages [6] -->
3.1

<!-- b000116 | heading | pages [6] -->
Model Overview

<!-- b000117 | prose | pages [6] -->
Ecological niche model describes plant community evolution based on interspecific interactions[4]. According to the ecological niche model, each species occupies a specific ecological niche with particular resource utilization strategies and environmental adaptability.

<!-- b000118 | prose | pages [6] -->
The model considers species interactions through resource competition and cooperation.

<!-- b000119 | prose | pages [6] -->
The basic steps of the ecological niche model to simulate plant community evolution are as follows.

<!-- b000120 | caption | pages [6] -->
Figure 3: Steps of the ecological niche model

<!-- b000121 | prose | pages [6] -->
The evolution process of community-based on niche model is shown in figure 4.

<!-- b000122 | furniture | pages [7] -->
Team # 2300336

<!-- b000123 | furniture | pages [7] -->
Page 6 of 24

<!-- b000124 | caption | pages [7] -->
Figure 4: The evolution process of community

<!-- b000125 | prose | pages [7] -->
Initial Conditions and Niche Characteristics of Species 3.2

<!-- b000126 | prose | pages [7] -->
At the initial moment of community succession, there are m species, and the environmental capacity is K. Environmental capacity is the maximum number of populations a given environment can tolerate.

<!-- b000127 | prose | pages [7] -->
The drought sensitivity coefficient is a metric frequently used to characterize a plant species’ sensitivity to drought. This coefficient is typically a value between 0 and 1, where higher values indicate greater sensitivity to drought.

<!-- b000128 | prose | pages [7] -->
The susceptibility of a community to drought can be represented by the following vector:

<!-- b000129 | prose | pages [7] -->
Γ = [γ1, γ2, · · · , γm] (1)

<!-- b000130 | prose | pages [7] -->
where γi refers to the drought sensitivity coefficient of i-th species.

<!-- b000131 | prose | pages [7] -->
In the ecological niche model, the competition matrix is a matrix describing the competitive and mutually beneficial relationship [5] between different species, which is expressed as follows:

<!-- b000132 | prose | pages [7] -->


<!-- b000133 | prose | pages [7] -->
c11 c12 c21 c22

<!-- b000134 | prose | pages [7] -->


<!-- b000135 | prose | pages [7] -->
C =

<!-- b000136 | prose | pages [7] -->
... cm1 cm2

<!-- b000137 | prose | pages [7] -->


<!-- b000138 | prose | pages [7] -->
· · · c1m · · · c2m

<!-- b000139 | prose | pages [7] -->
 (2)

<!-- b000140 | prose | pages [7] -->
... ...

<!-- b000141 | prose | pages [7] -->
... ... · · · cmm

<!-- b000142 | prose | pages [7] -->
where cij refers to the competition coefficient between the i-th species and the j-th species.

<!-- b000143 | prose | pages [7] -->
When cij = 0, there is no competition between the two species. cij > 0 indicates that the i-th species harms the survival and reproduction of the j-th species, namely, competition. In contrast,

<!-- b000144 | furniture | pages [8] -->
Team # 2300336

<!-- b000145 | furniture | pages [8] -->
Page 7 of 24

<!-- b000146 | prose | pages [8] -->
cij < 0 indicates that the i-th species positively impacts the existence and reproduction of the j-th species, that is, symbiosis or mutualism. The greater the absolute value of the competition coefficient, the stronger the competitive or mutually beneficial relationship.

<!-- b000147 | prose | pages [8] -->
The competition matrix usually needs to be based on experimental data, ecological survey data, or other relevant data and knowledge to estimate. Considering that the competition between species is bidirectional and mutually influencing, the competition matrix is usually symmetric, namely cij = cji.

<!-- b000148 | caption | pages [8] -->
Figure 5: Schematic diagram of species’ competition

<!-- b000149 | prose | pages [8] -->
In ecology, an ecological niche refers to the function and role of a species in its ecosystem. It refers to the species’ position in an ecosystem, the way it uses resources, and the interaction between the species and its surroundings.

<!-- b000150 | prose | pages [8] -->
Niche width refers to the sum of all kinds of resources that organisms can use, which is an indicator of the diversity of resources used by organisms. Let the niche width of a community be:

<!-- b000151 | prose | pages [8] -->
L = [l1, l2, ..., lm] (3)

<!-- b000152 | prose | pages [8] -->
where li represents the sum of the resources used by i-th species. The larger the L value, the more resources the species can utilize.

<!-- b000153 | prose | pages [8] -->
Considering the expansion of the community, the sum K of the ecological niche of each species can change within a specific range.

<!-- b000154 | prose | pages [8] -->
K(t) =

<!-- b000155 | prose | pages [8] -->
m X

<!-- b000156 | prose | pages [8] -->
li(t) (4)

<!-- b000157 | prose | pages [8] -->
i=1

<!-- b000158 | prose | pages [8] -->
Rules of Plant Community Evolution 3.3

<!-- b000159 | prose | pages [8] -->
Niche width is affected by the population’s number of individual deaths and reproduction. To more accurately simulate the effects of climatic instability and drought on plant community evolution, a random disturbance term was taken to the niche model. The niche model is shown in the equation

<!-- b000160 | furniture | pages [9] -->
Team # 2300336

<!-- b000161 | prose | pages [9] -->
below:

<!-- b000162 | furniture | pages [9] -->
Page 8 of 24

<!-- b000163 | prose | pages [9] -->
li(t + 1) = li(t) + bi(t) −di(t) + σi(t)

<!-- b000164 | prose | pages [9] -->
where

<!-- b000165 | prose | pages [9] -->
(5)

<!-- b000166 | prose | pages [9] -->
• li(t) is the niche width of the i-th species at time t;

<!-- b000167 | prose | pages [9] -->
• bi(t) is the increase in niche width of the i-th species due to its reproduction;

<!-- b000168 | prose | pages [9] -->
• di(t) is the fraction of niche width of the i-th species reduced by death;

<!-- b000169 | prose | pages [9] -->
• σi(t) is Gaussian white noise with a mean of 0 and a variance of σ2.

<!-- b000170 | prose | pages [9] -->
It is worth noting that, in practice, we need to make appropriate adjustments to the random disturbance term to ensure that it does not have an excessive effect on the simulation results. In addition, the model requires sensitivity analysis and validation to ensure its reliability and repeatability.

<!-- b000171 | caption | pages [9] -->
Figure 6: Species interactions and community evolution

<!-- b000172 | prose | pages [9] -->
Effects of Species Reproduction on Niche Width 3.3.1

<!-- b000173 | prose | pages [9] -->
In this paper, the increase in the niche width of each species due to reproduction is influenced by the current niche width, environmental capacity, and interspecific competition. The larger the current niche width of a species or the environmental capacity, the more it reproduces, and the more it increases its niche width. On the contrary, the greater the competition between species, the less it breeds and the less they increase its niche width. Therefore, the expression of bi(t) is obtained based on the Beverton-Holt[6] equation and the Lotka-Volterra equation[7][8], as follows

<!-- b000174 | furniture | pages [9] -->


<!-- b000175 | prose | pages [9] -->
1 −

<!-- b000176 | prose | pages [9] -->
bi(t) = gili (t)

<!-- b000177 | prose | pages [9] -->
li (t) + Pj̸=i

<!-- b000178 | prose | pages [9] -->
!

<!-- b000179 | prose | pages [9] -->
j=1 cijlj (t)

<!-- b000180 | prose | pages [9] -->
(6)

<!-- b000181 | prose | pages [9] -->
K(t)

<!-- b000182 | furniture | pages [10] -->
Team # 2300336

<!-- b000183 | furniture | pages [10] -->
Page 9 of 24

<!-- b000184 | prose | pages [10] -->
where gi represents the non-competitive growth rate of the i-th species, which is only affected by environmental conditions. The more suitable the environmental conditions are for this species, the larger gi is.

<!-- b000185 | prose | pages [10] -->
Under drought environmental conditions, plants’ water resources decrease, and their growth rates are correspondingly lower. The more sensitive a species is to drought, its growth rate will be lower under drought conditions. The drought sensitivity coefficient is not static but varies with drought conditions. The non-competitive growth rate of species is

<!-- b000186 | prose | pages [10] -->
gi = gmaxe−dr×γ (7)

<!-- b000187 | prose | pages [10] -->
where dr is the drought coefficient, which measures the degree of drought, γ is the drought sensitivity coefficient of i-th species, and gmax is the maximum growth rate of it.

<!-- b000188 | prose | pages [10] -->
Effects of Species Mortality on Niche Width 3.3.2

<!-- b000189 | prose | pages [10] -->
The decrease in niche width due to mortality is proportional to the niche width of the species. Considering that the mortality rate of plants increases during drought, a drought response function f(dr) is the response function of species to drought degree. This function can simulate the adverse effects of drought on plant communities. Therefore, the expression of di(t) is acquired as follows:

<!-- b000190 | prose | pages [10] -->
di(t) = f(dr)βili(t) (8)

<!-- b000191 | prose | pages [10] -->
where f(dr) describes the species mortality due to drought, and βi refers to the proportionality coefficient.

<!-- b000192 | prose | pages [10] -->
The greater the degree of drought, the greater the mortality rate of plant species. When the degree of drought is small, the environment is suitable for the growth of plants where the mortality rate of species is at a low level and does not change much. However, when the drought is severe, the environment is harsh. Hence, the mortality rate of plants will be at a high level. Therefore, f(dr) can be determined based on the Logistic function.

<!-- b000193 | prose | pages [10] -->
f (x) = 1 (9) 1 + e−x

<!-- b000194 | prose | pages [10] -->
Let x = 12(dr −0.5), namely, map dr from [0, 1] to [-6, 6].

<!-- b000195 | prose | pages [10] -->
f (dr) = 1 (10) 1 + e−12(dr−0.5)

<!-- b000196 | prose | pages [10] -->
The image of function f(dr) is shown below:

<!-- b000197 | furniture | pages [11] -->
Team # 2300336

<!-- b000198 | furniture | pages [11] -->
Page 10 of 24

<!-- b000199 | caption | pages [11] -->
Figure 7: The image of function f(dr)

<!-- b000200 | prose | pages [11] -->
By substituting Equation(6) and (8) into Equation (5), we obtain:

<!-- b000201 | prose | pages [11] -->
li (t) + Pj̸=i

<!-- b000202 | furniture | pages [11] -->


<!-- b000203 | prose | pages [11] -->
1 −

<!-- b000204 | prose | pages [11] -->
li (t + 1) = li (t) + gili (t)

<!-- b000205 | prose | pages [11] -->
!

<!-- b000206 | prose | pages [11] -->
j=1 cijlj (t)

<!-- b000207 | prose | pages [11] -->
−f (dr) βili(t) + σi(t) (11)

<!-- b000208 | prose | pages [11] -->
K(t)

<!-- b000209 | prose | pages [11] -->
Then, the differential form of niche width can be obtained.

<!-- b000210 | prose | pages [11] -->
li (t) + Pj̸=i

<!-- b000211 | furniture | pages [11] -->


<!-- b000212 | prose | pages [11] -->
!

<!-- b000213 | prose | pages [11] -->
j=1 cijlj (t)

<!-- b000214 | prose | pages [11] -->
dli (t)

<!-- b000215 | prose | pages [11] -->
1 −

<!-- b000216 | prose | pages [11] -->
= gili (t) dt

<!-- b000217 | prose | pages [11] -->
K(t)

<!-- b000218 | prose | pages [11] -->
3.4 Irregular Weather Cycles

<!-- b000219 | prose | pages [11] -->
−f (dr) βili(t) + σi(t) (12)

<!-- b000220 | prose | pages [11] -->
Considering the fluctuation of the climatic environment, the uncertainty of drought cycles, and drought levels, we simulate the effects of these uncertainties by introducing random variables. Cli- mate change is considered a stochastic process. The simulation of climate environment fluctuation is based on random numbers generated by a random number generator. Besides, the drought cycle and the degree of drought obey certain probability distributions.

<!-- b000221 | prose | pages [11] -->
This paper uses the exponential distribution to model the probability of drought events. The exponential distribution is the probability distribution of the time interval between events in a Poisson point process, i.e., a process in which events occur continuously and independently at a constant average rate.

<!-- b000222 | prose | pages [11] -->
λ is the parameter of the exponential distribution, which reflects the frequency of drought events. When λ is larger, the frequency of drought events is higher. Conversely, when λ is smaller, the frequency and degree of drought events are lower. Therefore, the frequency of drought occurrence is adjusted by the value of λ.

<!-- b000223 | prose | pages [11] -->
P (tINR) = 1 −e−λtINR (13)

<!-- b000224 | prose | pages [11] -->
where P (tINR) denotes the probability of a drought event occurring in the time interval tINR.

<!-- b000225 | furniture | pages [12] -->
Team # 2300336

<!-- b000226 | furniture | pages [12] -->
Page 11 of 24

<!-- b000227 | prose | pages [12] -->
The degree and duration of drought vary for each drought event. In an attempt to simplify matters, we consider that the degree and duration of drought satisfy a mutually independent one- dimensional normal distribution.

<!-- b000228 | prose | pages [12] -->
dr ∼N

<!-- b000229 | prose | pages [12] -->
td ∼N

<!-- b000230 | prose | pages [12] -->
µd, σ2

<!-- b000231 | prose | pages [12] -->
   

<!-- b000232 | prose | pages [12] -->


<!-- b000233 | prose | pages [12] -->
d

<!-- b000234 | prose | pages [12] -->
(14)

<!-- b000235 | prose | pages [12] -->
µt, σ2

<!-- b000236 | prose | pages [12] -->
   

<!-- b000237 | prose | pages [12] -->


<!-- b000238 | prose | pages [12] -->
t

<!-- b000239 | prose | pages [12] -->
where dr is the drought coefficient, which represents the degree of drought, and td is the duration of drought.

<!-- b000240 | prose | pages [12] -->
By adjusting the probability, intensity, and duration of drought, models can simulate the effects of changing climate conditions on plant community succession. When no drought occurs, dr is the given default value. The climate change process is shown in Figure 8.

<!-- b000241 | caption | pages [12] -->
Figure 8: Irregular weather cycles

<!-- b000242 | prose | pages [12] -->
Simulation of Plant Community Evolution 3.5

<!-- b000243 | prose | pages [12] -->
3.5.1 Plant Species and Initial Parameters

<!-- b000244 | prose | pages [12] -->
In this paper, the total time length of the community evolution simulated is 100 years with a time step of 1 year. Besides, in order to simplify the problem, there were three species in the community in the first place. For each species, its drought sensitivity coefficient, initial ecological niche width, and maximum growth coefficient are given in Table 1. Specific data can be obtained through field surveys or based on literature, and the following data are only to show how our model is applied.

<!-- b000245 | caption | pages [12] -->
Table 1: Related parameters of three species

<!-- b000246 | prose | pages [12] -->
gmax γi Species βi Initial li

<!-- b000247 | prose | pages [12] -->
0.23 1 0.5 0.1 2 0.15 2 0.7 0.1 2 0.33 3 0.2 0.1 2

<!-- b000248 | furniture | pages [13] -->
Team # 2300336

<!-- b000249 | furniture | pages [13] -->
Page 12 of 24

<!-- b000250 | prose | pages [13] -->
Parameters of the ecosystem : 

<!-- b000251 | prose | pages [13] -->


<!-- b000252 | prose | pages [13] -->
0

<!-- b000253 | prose | pages [13] -->
  

<!-- b000254 | prose | pages [13] -->
C =

<!-- b000255 | prose | pages [13] -->
−0.2

<!-- b000256 | prose | pages [13] -->


<!-- b000257 | prose | pages [13] -->


<!-- b000258 | prose | pages [13] -->
   

<!-- b000259 | prose | pages [13] -->
0.4

<!-- b000260 | prose | pages [13] -->
   

<!-- b000261 | prose | pages [13] -->
K = 10

<!-- b000262 | prose | pages [13] -->


<!-- b000263 | prose | pages [13] -->


<!-- b000264 | prose | pages [13] -->
−0.2 0.4 0 0.6

<!-- b000265 | prose | pages [13] -->


<!-- b000266 | prose | pages [13] -->
0.6 0

<!-- b000267 | prose | pages [13] -->
(15)

<!-- b000268 | prose | pages [13] -->
dr ∼N (1.5, 0.32)

<!-- b000269 | prose | pages [13] -->
   

<!-- b000270 | prose | pages [13] -->
td ∼N (15, 52)

<!-- b000271 | prose | pages [13] -->
    

<!-- b000272 | prose | pages [13] -->
P(t; λ = 0.04) = 1 −e−λt

<!-- b000273 | prose | pages [13] -->
 

<!-- b000274 | prose | pages [13] -->
3.5.2 Irregular Weather Simulation

<!-- b000275 | prose | pages [13] -->
According to the rules of the weather simulation in Section 3.4, the weather for the next 100 months can be obtained. The algorithm for irregular weather simulation is shown below.

<!-- b000276 | heading | pages [13] -->
Algorithm 1 Irregular Weather Simulation

<!-- b000277 | prose | pages [13] -->
Input: Maximum iterations n Output: Drought coefficient dr at certain time point

<!-- b000278 | prose | pages [13] -->
1: P(tINR) ←1 −exp−λtINR, λ = 0.04; 2: dr0 ←0.2; 3: tINR ←0; 4: i ←0 5: while i ≤n do r ←rand(); 6:

<!-- b000279 | prose | pages [13] -->
p ←Exponential(λ, tINR); 7:

<!-- b000280 | prose | pages [13] -->
if r ≤p then 8:

<!-- b000281 | prose | pages [13] -->
dayn ←round(2 ∗randn() + 10); 9:

<!-- b000282 | prose | pages [13] -->
for j ←i: i + dayn −1 do 10:

<!-- b000283 | prose | pages [13] -->
drj = 0.15 ∗randn() + 0.6; 11:

<!-- b000284 | prose | pages [13] -->
end for 12:

<!-- b000285 | prose | pages [13] -->
i ←i + dayn; 13:

<!-- b000286 | prose | pages [13] -->
tINR ←0; 14:

<!-- b000287 | prose | pages [13] -->
else 15:

<!-- b000288 | prose | pages [13] -->
dri ←dr0; 16:

<!-- b000289 | prose | pages [13] -->
tINR ←tINR + 1; 17:

<!-- b000290 | prose | pages [13] -->
i ←i + 1; 18:

<!-- b000291 | prose | pages [13] -->
end if 19: 20: end while ▷The probability of drought

<!-- b000292 | prose | pages [13] -->
▷dayn is the duration of the drought

<!-- b000293 | prose | pages [13] -->
▷Update the time interval points ▷reset tINR to 0

<!-- b000294 | prose | pages [13] -->
▷Update the time interval since the last drought ▷Update the time points

<!-- b000295 | prose | pages [13] -->
The weather over the next 100 years can be acquired utilizing the irregular weather simulation algorithm, which is displayed in Figure 9.

<!-- b000296 | furniture | pages [14] -->
Team # 2300336

<!-- b000297 | furniture | pages [14] -->
Page 13 of 24

<!-- b000298 | caption | pages [14] -->
Figure 9: Irregular weather simulation for 100 years

<!-- b000299 | prose | pages [14] -->
As shown in Figure 9, in the beginning, the climate is in a normal state, and the environment is favorable. Over time, the plant community will face irregular drought, with various durations and degrees.

<!-- b000300 | caption | pages [14] -->
Figure 10: Succession process of plant community

<!-- b000301 | prose | pages [14] -->
3.5.3

<!-- b000302 | heading | pages [14] -->
Simulation Results of Species Evolution

<!-- b000303 | prose | pages [14] -->
According to equation(12), the difference equation of their niche widths can be obtained for each species. Thus, we get the niche widths of each species over 100 years by solving the differential equations.

<!-- b000304 | prose | pages [14] -->
We have

<!-- b000305 | prose | pages [14] -->


<!-- b000306 | prose | pages [14] -->


<!-- b000307 | prose | pages [14] -->


<!-- b000308 | prose | pages [14] -->
li(t)+Pj̸=i

<!-- b000309 | prose | pages [14] -->
j=1 cijlj(t)

<!-- b000310 | prose | pages [14] -->
dli(t)

<!-- b000311 | prose | pages [14] -->
1 −

<!-- b000312 | prose | pages [14] -->
−f (dr) βili(t) + σi(t)

<!-- b000313 | prose | pages [14] -->
= gili (t)

<!-- b000314 | prose | pages [14] -->


<!-- b000315 | prose | pages [14] -->
dt

<!-- b000316 | prose | pages [14] -->
K(t)

<!-- b000317 | prose | pages [14] -->
(16)

<!-- b000318 | prose | pages [14] -->
li (0) = li0

<!-- b000319 | prose | pages [14] -->


<!-- b000320 | furniture | pages [15] -->
Team # 2300336

<!-- b000321 | furniture | pages [15] -->
Page 14 of 24

<!-- b000322 | prose | pages [15] -->
where σi(t) obeys N(0, 0.52).

<!-- b000323 | prose | pages [15] -->
The niche widths of the three species in 100 years are displayed in Figure 11.

<!-- b000324 | caption | pages [15] -->
Figure 11: The niche widths of the three species in 100 years

<!-- b000325 | prose | pages [15] -->
From Figure 11, the niche widths of all three species are equal to 2 at the beginning. Under irregular weather, the niche widths of species 1 and 2 increase with fluctuation, while species one increases the fastest. In general, the niche width of species three increases first, decreases, and eventually levels off. Drought is bad for almost all species.

<!-- b000326 | prose | pages [15] -->
Under irregular weather conditions, the proportion of niche width for each species also varies over time. Figure 12 shows the proportion of niche width for each species in years 1, 20, 40, 60, 80, and 100.

<!-- b000327 | caption | pages [15] -->
Figure 12: The proportion of niche width for each species in years 1, 20, 40, 60, 80, and 100

<!-- b000328 | furniture | pages [16] -->
Team # 2300336

<!-- b000329 | furniture | pages [16] -->
Page 15 of 24

<!-- b000330 | prose | pages [16] -->
As can be seen in Figure 12, in the first year, we assume all three species had equal proportions of niche width. As time progresses, the proportion of niche width of species 1 increases. By the 60th year, the proportion of niche widths of each species stabilizes.

<!-- b000331 | prose | pages [16] -->
The evolution of the plant community is mainly affected by drought. Figure 13 demonstrates the effect of drought occurrence on the total niche width of the community.

<!-- b000332 | caption | pages [16] -->
Figure 13: Variation of drought coefficient dr and niche width over time

<!-- b000333 | prose | pages [16] -->
As shown in Figure 13, it can be seen that when no drought occurred, the total niche width of the community showed an increasing trend. This indicates that the environment is suitable for the growth of plants and the population reproduces more at this time. However, when drought occurred, the total niche width showed a decreasing trend. Besides, the more severe the drought, i.e., the greater the dr, the faster the total niche width decreases. It demonstrates that drought inhibits the reproduction of the population and the inhibitory effect increases as the degree of drought increases.

<!-- b000334 | prose | pages [16] -->
4

<!-- b000335 | heading | pages [16] -->
Application of Plant Community Evolution Model

<!-- b000336 | prose | pages [16] -->
4.1 Effect of the Number of Species on the Community

<!-- b000337 | prose | pages [16] -->
In natural environments, species have competitive and mutualistic relationships with each other. When the environment is harsher, such as drought, the mutualistic relationships between species are enhanced in order to survive. As a result, the overall drought resistance of the community is enhanced. To investigate the effect of species number on the community, we simulate the evolution of communities containing one to four species separately using the Plant Community Evolution Model in Section 3.

<!-- b000338 | prose | pages [16] -->
4.1.1 The Minimal Number of Species for the Community to Benefit

<!-- b000339 | prose | pages [16] -->
According to the Plant Community Evolution Model in Section 3, the evolution of communities containing 1, 2, 3 and 4 species can be simulated, which is shown in Figure 14.

<!-- b000340 | furniture | pages [17] -->
Team # 2300336

<!-- b000341 | furniture | pages [17] -->
Page 16 of 24

<!-- b000342 | prose | pages [17] -->
(a) One species

<!-- b000343 | prose | pages [17] -->
(b) Two species

<!-- b000344 | prose | pages [17] -->
(c) Three species

<!-- b000345 | prose | pages [17] -->
(d) Four species

<!-- b000346 | caption | pages [17] -->
Figure 14: Prediction of seawater temperature for 4 years respectively

<!-- b000347 | prose | pages [17] -->
From Figure 14, we can see that when there is only one species in a community, the species will slowly die out under irregular drought conditions. When there are two species, the ecological niche width of each species fluctuates drastically with the occurrence of drought. It indicates that the population is not able to survive stably in the long term when facing irregular drought.

<!-- b000348 | prose | pages [17] -->
When there are three species, the niche width of each species increases with fluctuation. It demonstrates that this community can improve drought resistance through interspecific mutualism,

<!-- b000349 | furniture | pages [18] -->
Team # 2300336

<!-- b000350 | furniture | pages [18] -->
Page 17 of 24

<!-- b000351 | prose | pages [18] -->
thus enabling the community for long-term survival. The situation of the four species was similar to that of the three species. Therefore, it can be concluded that the minimal number of species for the community to benefit is three.

<!-- b000352 | prose | pages [18] -->
The Effect of Increasing Species Number on Community 4.1.2

<!-- b000353 | prose | pages [18] -->
According to the four community evolution simulation results in section 4.1.1, we can draw the conclusion that as the number of species grows, the greater the width of the ecological niche of the community, the stronger its drought resistance. When the number of species increases to a certain value, its drought resistance tends to stabilize or may even decrease.

<!-- b000354 | prose | pages [18] -->
Single-species communities tend to be less drought-resistant than communities of multiple species. Communities of multiple species tend to have higher resource utilization, facilitation effects, and species diversity effects. Therefore, they can be better adapted to drought environments, exhibiting greater drought resistance. The principle is as follows:

<!-- b000355 | prose | pages [18] -->
• Ecological niche partitioning: It refers to the difference in resource utilization between different species, thus avoiding competition between plants. It allows the community to take advantage of the limited resources and enhances its resistance to drought.

<!-- b000356 | prose | pages [18] -->
• Facilitation effect: There may be reciprocal symbiosis among multiple species, thus im- proving the efficiency of water and nutrient utilization and enhancing the resistance of plants to drought.

<!-- b000357 | prose | pages [18] -->
• Species diversity effect: Diversity is a measure of the number and diversity of species in an ecosystem. An increase in diversity can increase the stability of the system and reduce its exposure to external disturbances, thus enhancing the drought resistance of the community.

<!-- b000358 | prose | pages [18] -->
However, from the perspective of the ecological niche model, the drought resistance of commu- nities with too many species is not necessarily stronger. Too many species will lead to overlapping ecological niches and more intense interspecific competition. It also results in a decrease in the stability of the community, thus making the community less resistant to drought.

<!-- b000359 | prose | pages [18] -->
Impact of the Types of Species on Community Evolution 4.2

<!-- b000360 | prose | pages [18] -->
The types of species in different plant communities vary. Therefore, the interactions between species also vary. Some communities have more intense species competition among them, while others have predominant interspecific mutualism among them. In this paper, based on the species competition relationships in Section 3, we design competitive communities and mutualistic communities by changing the competition matrix.

<!-- b000361 | prose | pages [18] -->
• General plant community There are both competitive-dominated and facilitation-dominated relationships among species of the plant community which are denoted by the competition matrix in Section 3.

<!-- b000362 | prose | pages [18] -->


<!-- b000363 | prose | pages [18] -->


<!-- b000364 | prose | pages [18] -->
−0.2 0 0 0.4 −0.2

<!-- b000365 | prose | pages [18] -->
C =

<!-- b000366 | prose | pages [18] -->


<!-- b000367 | prose | pages [18] -->
0.4 0 0.6

<!-- b000368 | prose | pages [18] -->
(17) 

<!-- b000369 | prose | pages [18] -->
0.6 0

<!-- b000370 | furniture | pages [19] -->
Team # 2300336

<!-- b000371 | prose | pages [19] -->
• Competitive plant community

<!-- b000372 | furniture | pages [19] -->
Page 18 of 24

<!-- b000373 | prose | pages [19] -->
Competitive plant communities are dominated by competitive relationships between species. The competition matrix is as follows:

<!-- b000374 | prose | pages [19] -->


<!-- b000375 | prose | pages [19] -->
C =

<!-- b000376 | prose | pages [19] -->


<!-- b000377 | prose | pages [19] -->
• Mutualistic plant community

<!-- b000378 | prose | pages [19] -->


<!-- b000379 | prose | pages [19] -->
0 0 1.0 0.8 1.0 0 0.9

<!-- b000380 | prose | pages [19] -->
(18) 

<!-- b000381 | prose | pages [19] -->
0.8 0.9 0

<!-- b000382 | prose | pages [19] -->
Mutualistic plant communities are dominated by mutualistic relationships between species. The competition matrix is as follows:

<!-- b000383 | prose | pages [19] -->


<!-- b000384 | prose | pages [19] -->
0 −0.3

<!-- b000385 | prose | pages [19] -->
C =

<!-- b000386 | prose | pages [19] -->


<!-- b000387 | prose | pages [19] -->
−0.2

<!-- b000388 | prose | pages [19] -->


<!-- b000389 | prose | pages [19] -->
−0.3 −0.2 −0.25 0

<!-- b000390 | prose | pages [19] -->
(19) 

<!-- b000391 | prose | pages [19] -->
−0.25 0

<!-- b000392 | prose | pages [19] -->
Evolution of the three communities is demonstrated in Figure 15. It can be seen that mutualistic- dominated community would have a larger ecological niche width and more species reproduction. This indicates that the more drought resistant it is.

<!-- b000393 | prose | pages [19] -->
On the contrary, When there is intense competition between species in a community, the smaller the width of its ecological niche, the less the population reproduces, indicating its weaker drought resistance.

<!-- b000394 | caption | pages [19] -->
Figure 15: Evolution of communities with three distinct compositions

<!-- b000395 | prose | pages [19] -->
The Effects of the Severity of Drought 4.3

<!-- b000396 | prose | pages [19] -->
An increase in the degree and duration of drought can negatively affect plant communities. The severity of drought can be simulated by adjusting the drought coefficient dr and drought duration td in Plant Community Evolution Model. When the drought becomes more severe, dr and td obey the following normal distribution:

<!-- b000397 | prose | pages [19] -->
dr ∼N

<!-- b000398 | prose | pages [19] -->
td ∼N

<!-- b000399 | prose | pages [19] -->
0.8, 0.12

<!-- b000400 | prose | pages [19] -->
   

<!-- b000401 | prose | pages [19] -->
(20) 12, 32

<!-- b000402 | prose | pages [19] -->
   

<!-- b000403 | furniture | pages [20] -->
Team # 2300336

<!-- b000404 | furniture | pages [20] -->
Page 19 of 24

<!-- b000405 | prose | pages [20] -->
When the drought is more mild, dr and td obey the following normal distribution:

<!-- b000406 | prose | pages [20] -->
 

<!-- b000407 | prose | pages [20] -->
dr ∼N

<!-- b000408 | prose | pages [20] -->
 

<!-- b000409 | prose | pages [20] -->
td ∼N

<!-- b000410 | prose | pages [20] -->
0.45, 0.152

<!-- b000411 | prose | pages [20] -->
(21) 8, 1.52

<!-- b000412 | prose | pages [20] -->
Based on Plant Community Evolution Model, the process of community succession in the three drought conditions is shown in Figure 16.

<!-- b000413 | caption | pages [20] -->
Figure 16: Community succession in the three drought conditions

<!-- b000414 | prose | pages [20] -->
From figure 16, we can see that as drought intensifies, the niche width of the community decreases, which means more species die. Therefore, the community can survive for a shorter period of time.

<!-- b000415 | prose | pages [20] -->
The impact of Pollution and Habitat Reduction 4.4

<!-- b000416 | prose | pages [20] -->
Pollution and habitat shrinkage can decrease the ecological niche width, limiting the number of available resources for organisms. This reduction in resources increases competition intensity, allowing more competitive species to dominate and exert additional pressure on other species, resulting in their decline or extinction.

<!-- b000417 | prose | pages [20] -->
In the Plant Community Evolution model, extinct species will be removed from the competition matrix. This may lead to changes in competitive relationships, which may affect the competitive ability of other species and the community succession process.

<!-- b000418 | prose | pages [20] -->
Pollution and habitat shrinkage will affect the ecological niche width and competitive relation- ships of plant communities. Therefore, the ecological niche width and competition matrix can be adjusted as follows.

<!-- b000419 | prose | pages [20] -->
L′ = L(1 −Pr)H (22) C′ = C(1 −Pr)H

<!-- b000420 | prose | pages [20] -->
where L′ refers to the adjusted niche width, C′ refers to the adjusted competition matrix, Pr refers to the contamination degree of plant community, H refers to the habitat reduction coefficient.

<!-- b000421 | furniture | pages [21] -->
Team # 2300336

<!-- b000422 | furniture | pages [21] -->
Page 20 of 24

<!-- b000423 | prose | pages [21] -->
According to the Plant Community Evolution Model, the evolution of communities facing pollution and shrinking habitats can be simulated. The result is displayed in Figure 17.

<!-- b000424 | caption | pages [21] -->
Figure 17: Evolution of plant communities facing pollution and shrinking habitats

<!-- b000425 | prose | pages [21] -->
As shown in Figure 17, the community ecological niche width is relatively reduced when pollution is light and habitat reduction is less. At this time, the plant community is still able to survive stably for a long time. When the pollution is heavy and the habitat is reduced more, the ecological niche width is close to 0, that is, many species in the community will become extinct at this time.

<!-- b000426 | prose | pages [21] -->
4.5 Measures that Allow a Plant Community to Live Longer

<!-- b000427 | prose | pages [21] -->
The analysis of the ecological niche model reveals that diverse plant communities have higher drought resistance in arid environments. This is due to the complementary ecological niches of different species that reduce competition and enable better adaptation to the challenges of drought.

<!-- b000428 | prose | pages [21] -->
To ensure the long-term survival of plant communities, the following measures can be taken:

<!-- b000429 | prose | pages [21] -->
1. Protect the natural environment, maintain the integrity and stability of the ecosystem, and reduce human activities’ damage to the natural environment. In particular, vegetation and water sources should be protected to prevent excessive logging and overgrazing, excessive use of fertilizers and pesticides, and excessive exploitation of water resources, etc.

<!-- b000430 | prose | pages [21] -->
2. Encourage plant diversity and maintain the diversity of communities. By planting different types of plants, the diversity of the plant community can be increased, the adaptability and resistance of plants can be improved, competition between plants can be reduced, and the stability of the community can be maintained.

<!-- b000431 | prose | pages [21] -->
3. Promote water-saving measures. Water is an important resource for maintaining life. Humans can adopt water-saving measures such as the rational use and conservation of water resources,

<!-- b000432 | furniture | pages [22] -->
Team # 2300336

<!-- b000433 | furniture | pages [22] -->
Page 21 of 24

<!-- b000434 | prose | pages [22] -->
reducing pollution and destruction of natural water sources, and providing a better growth environment for plants.

<!-- b000435 | prose | pages [22] -->
4. Cultivate drought-resistant varieties.

<!-- b000436 | prose | pages [22] -->
Drought-resistant plant varieties can be developed through breeding or gene editing technology to improve plants’ drought resistance and better adapt to arid environments.

<!-- b000437 | caption | pages [22] -->
Figure 18: Save the planet and Protect our common home

<!-- b000438 | prose | pages [22] -->
In summary, the niche model suggests that each species in a biological community has a specific niche and interacts with each other through competition and mutualism. Protecting fragile communities can maintain ecosystem stability and ecological diversity. Furthermore, protecting fragile communities is essential for human self-interest as plants and animals in the ecosystem provide resources for human needs, and damage to the ecosystem can affect human production and livelihood. Therefore, protecting fragile communities is significant for maintaining ecosystem stability, ecological diversity, and safeguarding human self-interest.

<!-- b000439 | prose | pages [22] -->
5

<!-- b000440 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000441 | prose | pages [22] -->
5.1

<!-- b000442 | heading | pages [22] -->
Sensitivity to Unpredictable Factors

<!-- b000443 | prose | pages [22] -->
When establishing the differential equation for the population niche width, we added white noise to simulate the effect of unpredictable factors on community succession. The variance of white noise needs to be within a certain range. If the variance is too small, it cannot simulate the effect of unpredictable factors. If the variance is too large, it will affect the correctness of the community succession process.

<!-- b000444 | furniture | pages [23] -->
Team # 2300336

<!-- b000445 | furniture | pages [23] -->
Page 22 of 24

<!-- b000446 | caption | pages [23] -->
Figure 19: Sum of niche widths of community under different white noise

<!-- b000447 | prose | pages [23] -->
The variance of white noise has a minor effect on the overall ecological niche width of the community. This is because we calculate the white noise of each species independently, and when there are many species or sufficient simulation times, the overall ecological niche width of the community changes little. However, certain accidental factors may have a negative impact on all species in the community, rather than independent effects on each species. Therefore, more complex models are needed to obtain better results when considering unpredictable interference.

<!-- b000448 | prose | pages [23] -->
5.2

<!-- b000449 | heading | pages [23] -->
Sensitivity to Drought Coefficient

<!-- b000450 | prose | pages [23] -->
The drought coefficient is used to describe the sensitivity of species to drought, and we adjust the drought coefficient to observe the performance of species and communities with different drought adaptability.

<!-- b000451 | caption | pages [23] -->
Figure 20: Niche widths of species under different drought coefficients

<!-- b000452 | furniture | pages [24] -->
Team # 2300336

<!-- b000453 | furniture | pages [24] -->
Page 23 of 24

<!-- b000454 | prose | pages [24] -->
It can be seen from the figure that the more sensitive a species is to drought, the smaller its ecological niche width will be, and the smaller the ecological niche width of the entire community will be.

<!-- b000455 | prose | pages [24] -->
6

<!-- b000456 | heading | pages [24] -->
Strengths and Weaknesses

<!-- b000457 | prose | pages [24] -->
6.1

<!-- b000458 | heading | pages [24] -->
Strengths

<!-- b000459 | prose | pages [24] -->
• The ecological niche model provides a comprehensive understanding of the ecological rela- tionship between different species, including competition and cooperation, and can simulate the evolution of plant communities over time.

<!-- b000460 | prose | pages [24] -->
• The model is flexible and can be adapted to different environmental conditions, such as drought events or habitat loss, which allows for the assessment of the potential impact of these disturbances on the community.

<!-- b000461 | prose | pages [24] -->
• The ecological niche model can incorporate empirical observations of plant species’ inter- actions, making it a useful tool for testing ecological theories and predicting community responses to environmental change.

<!-- b000462 | prose | pages [24] -->
6.2

<!-- b000463 | heading | pages [24] -->
Weaknesses

<!-- b000464 | prose | pages [24] -->
• The model can be sensitive to the initial conditions of the community, and small changes in these conditions can result in significant differences in community evolution over time.

<!-- b000465 | prose | pages [24] -->
• The model assumes that species interactions are solely based on competition and cooperation for resources, which may not capture all ecological interactions in a community, such as predation or parasitism.

<!-- b000466 | prose | pages [24] -->
• The conditions that the parameters of the competition matrix need to satisfy may not be consistent with the actual situation in nature, such as the competition matrix not necessarily being a symmetric matrix.

<!-- b000467 | prose | pages [24] -->
7

<!-- b000468 | heading | pages [24] -->
Conclusion

<!-- b000469 | prose | pages [24] -->
• A community of multiple species generally exhibits stronger drought resistance than a com- munity of a single species due to the greater resource utilization efficiency, and species diversity effects.

<!-- b000470 | prose | pages [24] -->
• When the number of species increases to a certain level, their drought resistance tends to become stable or even decrease. This is because too many species will lead to ecological niche overlap, resulting in intensified interspecific competition.

<!-- b000471 | prose | pages [24] -->
• Communities dominated by mutualistic relationships have stronger drought adaptation abili- ties.

<!-- b000472 | furniture | pages [25] -->
Team # 2300336

<!-- b000473 | furniture | pages [25] -->
Page 24 of 24

<!-- b000474 | prose | pages [25] -->
• When droughts occur more frequently and last longer, species may not be able to adapt quickly to the changing environment, resulting in a reduction in the population size of some species, which disrupts the ecological equilibrium. Instead, if drought occurs less frequently, species may be more likely to adapt to the arid environment, as they have more time to adjust to the drought conditions.

<!-- b000475 | prose | pages [25] -->
• Habitat population and reduction both lead to a decrease in the ecological niche width, intensifying the degree of competition. Competitive species probably occupy more resources, exerting greater competition pressure on other species, leading to a decrease or extinction of other species.

<!-- b000476 | heading | pages [25] -->
References

<!-- b000477 | references | pages [25] -->
DT Rosenow et al. “Drought tolerant sorghum and cotton germplasm”. In: Agricultural Water

<!-- b000478 | references | pages [25] -->
[1]

<!-- b000479 | references | pages [25] -->
Management 7.1-3 (1983), pp. 207–222.

<!-- b000480 | references | pages [25] -->
[2]

<!-- b000481 | references | pages [25] -->
J Sardans and Josep Peñuelas. “Plant-soil interactions in Mediterranean forest and shrublands:

<!-- b000482 | references | pages [25] -->
impacts of climatic change”. In: Plant and soil 365 (2013), pp. 1–33.

<!-- b000483 | references | pages [25] -->
[3]

<!-- b000484 | references | pages [25] -->
Mustaqeem Ahmad et al. “Niche width analyses facilitate identification of high-risk en-

<!-- b000485 | references | pages [25] -->
demic species at high altitudes in western Himalayas”. In: Ecological Indicators 126 (2021),

<!-- b000486 | references | pages [25] -->
p. 107653.

<!-- b000487 | references | pages [25] -->
Jitka Polechová and David Storch. “Ecological niche”. In: Encyclopedia of ecology 2 (2008),

<!-- b000488 | references | pages [25] -->
[4]

<!-- b000489 | references | pages [25] -->
pp. 1088–1097.

<!-- b000490 | references | pages [25] -->
[5]

<!-- b000491 | references | pages [25] -->
Andrew D Letten, Po-Ju Ke, and Tadashi Fukami. “Linking modern coexistence theory and

<!-- b000492 | references | pages [25] -->
contemporary niche theory”. In: Ecological Monographs 87.2 (2017), pp. 161–177.

<!-- b000493 | references | pages [25] -->
[6]

<!-- b000494 | references | pages [25] -->
M De la Sen. “The generalized Beverton–Holt equation and the control of populations”. In:

<!-- b000495 | references | pages [25] -->
Applied Mathematical Modelling 32.11 (2008), pp. 2312–2328.

<!-- b000496 | references | pages [25] -->
[7]

<!-- b000497 | references | pages [25] -->
S Das and PK Gupta. “A mathematical model on fractional Lotka–Volterra equations”. In:

<!-- b000498 | references | pages [25] -->
Journal of Theoretical Biology 277.1 (2011), pp. 1–6.

<!-- b000499 | references | pages [25] -->
[8]

<!-- b000500 | references | pages [25] -->
Martin Bohner and Rotchana Chieochan. “The Beverton–Holt q-difference equation”. In:

<!-- b000501 | references | pages [25] -->
Journal of Biological Dynamics 7.1 (2013), pp. 86–95.
