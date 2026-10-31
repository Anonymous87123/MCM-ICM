# P-A-2015-32722-037c369c

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team # 32722

<!-- b000002 | furniture | pages [1] -->
Page 1 of 37

<!-- b000003 | title | pages [1] -->
Turning the Tables: Modeling the Fight against Ebola

<!-- b000004 | prose | pages [1] -->
Team 32722

<!-- b000005 | heading | pages [1] -->
Abstract

<!-- b000006 | prose | pages [1] -->
We have constructed a multi-layer state-based model that appears to hold promise for providing insight into not only how the Ebola outbreak in West Africa will continue to de- velop, but also the best course of intervention in the event an eﬀective vaccine or cure should be created. This model considers a large number of parameters thought to be important to or characteristic of the outbreak, including the impact of the infection’s unique progression in humans, transmission to new individuals from infected persons at diﬀerent stages of the infection, and the eﬀects of geographic connections on the movement of infected persons and pharmaceuticals.

<!-- b000007 | prose | pages [1] -->
The aforementioned multi-layer approach includes interactions on the level of the individ- ual, a collection of individuals (or “region”), and a collection of regions, in order to capture behaviors at each scale. Individuals transition through states, representing the various stages of an Ebola infection, in a stochastic way with some probabilities being intrinsic to the illness and some being related to the current state-of-aﬀairs in the region.

<!-- b000008 | prose | pages [1] -->
Individuals are treated as homogeneously mixed within regions, but are capable of moving between regions with probabilities determined by the various characteristics of each region. Distribution of medicines occurs at the local level through hospitals and at the regional levels through transit, with medicines and vaccines entering the simulation through deﬁned transportation “hubs”, then being distributed along deﬁned delivery routes from region to region.

<!-- b000009 | prose | pages [1] -->
Our model focuses exclusively on the three countries still suﬀering from an active presence of Ebola (Guinea, Liberia, and Sierra Leone), making predictions across the next 6 months.

<!-- b000010 | prose | pages [1] -->
Speciﬁc attention is given to the sensitivity of our model to variations in its fundamental parameters, whose values are based largely on inadequate and varied statistical data from regions aﬀected by the outbreak. We attempt to use our model to identify important factors related to the eﬀectiveness of distributing a cure for Ebola, and show simulation results related to the inﬂuence of geographic factors, delivery frequency/quantity, and distribution tactics in comparison to baseline predictions.

<!-- b000011 | prose | pages [1] -->
Ultimately, we have concluded that given the complex nature of this scenario and the limited quantity and quality of detailed information concerning the outbreak, it is not possible at this time to quantitatively predict the eﬀectiveness of a vaccine/cure distribution plan. Instead, the results presented here qualitatively show how our baseline model responds to changes in the parameters that govern its behavior. These qualitative results are then used to craft a tentative deployment strategy for these hypothetical vaccines and cures.

<!-- b000012 | furniture | pages [2] -->
Team # 32722

<!-- b000013 | heading | pages [2] -->
Contents

<!-- b000014 | contents | pages [2] -->
1

<!-- b000015 | contents | pages [2] -->
Introduction

<!-- b000016 | furniture | pages [2] -->
Page 2 of 37

<!-- b000017 | contents | pages [2] -->
4

<!-- b000018 | contents | pages [2] -->
Context of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000019 | contents | pages [2] -->
1.1

<!-- b000020 | contents | pages [2] -->
4

<!-- b000021 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000022 | contents | pages [2] -->
1.2

<!-- b000023 | contents | pages [2] -->
The Task at Hand

<!-- b000024 | contents | pages [2] -->
5

<!-- b000025 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
1.3

<!-- b000027 | contents | pages [2] -->
Previous Work

<!-- b000028 | contents | pages [2] -->
6

<!-- b000029 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
1.4

<!-- b000031 | contents | pages [2] -->
The GLEAM Simulator

<!-- b000032 | contents | pages [2] -->
2

<!-- b000033 | contents | pages [2] -->
Our Model

<!-- b000034 | contents | pages [2] -->
6

<!-- b000035 | contents | pages [2] -->
7

<!-- b000036 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
2.1

<!-- b000038 | contents | pages [2] -->
Modeling Objectives

<!-- b000039 | contents | pages [2] -->
7

<!-- b000040 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
2.2

<!-- b000042 | contents | pages [2] -->
Problem Space

<!-- b000043 | contents | pages [2] -->
7

<!-- b000044 | contents | pages [2] -->
The Multi-Layer State Based Stochastic Epidemic Model . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
2.3

<!-- b000046 | contents | pages [2] -->
8

<!-- b000047 | contents | pages [2] -->
Individual Layer - Stochastic State Based Model . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
2.3.1

<!-- b000049 | contents | pages [2] -->
9

<!-- b000050 | contents | pages [2] -->
Inter-Region Layer modeling . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
2.3.2

<!-- b000052 | contents | pages [2] -->
12

<!-- b000053 | contents | pages [2] -->
Human Mobility Model . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
2.3.3

<!-- b000055 | contents | pages [2] -->
12

<!-- b000056 | contents | pages [2] -->
Supply Distribution Model . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
2.3.4

<!-- b000058 | contents | pages [2] -->
14

<!-- b000059 | contents | pages [2] -->
A note on GLEAM . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
2.3.5

<!-- b000061 | contents | pages [2] -->
14

<!-- b000062 | contents | pages [2] -->
Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
2.4

<!-- b000064 | contents | pages [2] -->
15

<!-- b000065 | contents | pages [2] -->
Additional Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
2.5

<!-- b000067 | contents | pages [2] -->
15

<!-- b000068 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
2.5.1

<!-- b000070 | contents | pages [2] -->
Modeling of Hospitals

<!-- b000071 | contents | pages [2] -->
15

<!-- b000072 | contents | pages [2] -->
Consequences of Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
2.6

<!-- b000074 | contents | pages [2] -->
3

<!-- b000075 | contents | pages [2] -->
Sensitivity Analysis and Results

<!-- b000076 | contents | pages [2] -->
16

<!-- b000077 | contents | pages [2] -->
16

<!-- b000078 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
3.0.1

<!-- b000080 | contents | pages [2] -->
Individual Region Tests

<!-- b000081 | contents | pages [2] -->
17

<!-- b000082 | contents | pages [2] -->
Initial Number of Infected . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
3.0.1.1

<!-- b000084 | contents | pages [2] -->
3.0.1.2

<!-- b000085 | contents | pages [2] -->
Hospital Bed Number

<!-- b000086 | contents | pages [2] -->
17

<!-- b000087 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
18

<!-- b000089 | contents | pages [2] -->
Population Scale . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
3.0.1.3

<!-- b000091 | contents | pages [2] -->
18

<!-- b000092 | contents | pages [2] -->
Medicine Eﬃcacy . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
3.0.1.4

<!-- b000094 | contents | pages [2] -->
19

<!-- b000095 | contents | pages [2] -->
Vaccine Quantity and Frequency of Shipments . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
3.0.2

<!-- b000097 | contents | pages [2] -->
20

<!-- b000098 | contents | pages [2] -->
Multiple-Region Simulations . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
3.0.3

<!-- b000100 | contents | pages [2] -->
22

<!-- b000101 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [2] -->
3.0.4

<!-- b000103 | contents | pages [2] -->
Vaccine Distribution

<!-- b000104 | contents | pages [2] -->
22

<!-- b000105 | contents | pages [2] -->
Cure Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
3.0.5

<!-- b000107 | contents | pages [2] -->
24

<!-- b000108 | contents | pages [2] -->
Initial Distribution of Infected . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
3.0.5.1

<!-- b000110 | contents | pages [2] -->
26

<!-- b000111 | contents | pages [2] -->
Movement Parameter Variation . . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [2] -->
3.0.5.2

<!-- b000113 | contents | pages [2] -->
26

<!-- b000114 | contents | pages [2] -->
Inter-Regional Parameter Variation . . . . . . . . . . . . . .

<!-- b000115 | contents | pages [2] -->
3.0.5.3

<!-- b000116 | contents | pages [2] -->
3.1

<!-- b000117 | contents | pages [2] -->
Further Sensitivities and Limitations

<!-- b000118 | contents | pages [2] -->
27

<!-- b000119 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000120 | contents | pages [2] -->
28

<!-- b000121 | contents | pages [2] -->
Weather Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000122 | contents | pages [2] -->
3.1.1

<!-- b000123 | contents | pages [2] -->
28

<!-- b000124 | contents | pages [2] -->
Burial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [2] -->
3.1.2

<!-- b000126 | contents | pages [2] -->
4

<!-- b000127 | contents | pages [2] -->
Conclusion

<!-- b000128 | contents | pages [2] -->
28

<!-- b000129 | contents | pages [2] -->
28

<!-- b000130 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000131 | contents | pages [2] -->
4.1

<!-- b000132 | contents | pages [2] -->
Future Epidemic Trajectories

<!-- b000133 | contents | pages [2] -->
28

<!-- b000134 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000135 | contents | pages [2] -->
4.2

<!-- b000136 | contents | pages [2] -->
Summary and Recommendations

<!-- b000137 | contents | pages [2] -->
29

<!-- b000138 | contents | pages [2] -->
The Art of Eradicating Ebola . . . . . . . . . . . . . . . . . . . . . .

<!-- b000139 | contents | pages [2] -->
4.2.1

<!-- b000140 | contents | pages [2] -->
30

<!-- b000141 | contents | pages [2] -->
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000142 | contents | pages [2] -->
4.3

<!-- b000143 | contents | pages [2] -->
4.3.1

<!-- b000144 | contents | pages [2] -->
Geography Based Modeling

<!-- b000145 | contents | pages [2] -->
31

<!-- b000146 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000147 | contents | pages [2] -->
31

<!-- b000148 | furniture | pages [3] -->
Team # 32722

<!-- b000149 | furniture | pages [3] -->
Page 3 of 37

<!-- b000150 | contents | pages [3] -->
Placement of Distribution Centers . . . . . . . . . . . . . . . . . . . .

<!-- b000151 | contents | pages [3] -->
4.3.2

<!-- b000152 | contents | pages [3] -->
32

<!-- b000153 | contents | pages [3] -->
Distribution Laws . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000154 | contents | pages [3] -->
4.3.3

<!-- b000155 | contents | pages [3] -->
Appendix A

<!-- b000156 | contents | pages [3] -->
Assumptions

<!-- b000157 | contents | pages [3] -->
32

<!-- b000158 | contents | pages [3] -->
34

<!-- b000159 | contents | pages [3] -->
Diﬀerential Equation Model

<!-- b000160 | contents | pages [3] -->
Appendix B

<!-- b000161 | contents | pages [3] -->
35

<!-- b000162 | furniture | pages [4] -->
Team # 32722

<!-- b000163 | furniture | pages [4] -->
Page 4 of 37

<!-- b000164 | contents | pages [4] -->
1. Introduction

<!-- b000165 | contents | pages [4] -->
1.1. Context of the Problem

<!-- b000166 | contents | pages [4] -->
The ongoing outbreak of Ebola Virus Disease in Western Africa represents one of the

<!-- b000167 | contents | pages [4] -->
most serious acute human health crises in the last thirty years, far exceeding the impact of

<!-- b000168 | contents | pages [4] -->
SARS and the much maligned bird and swine ﬂus. Detected in March of 2014, the disease

<!-- b000169 | contents | pages [4] -->
has infected more than 20,000 people and killed nearly half of that number over the course

<!-- b000170 | contents | pages [4] -->
of the past ten months [1].

<!-- b000171 | contents | pages [4] -->
The Ebola virus is a fairly recent addition to mankind’s stable of aﬄictions, having been

<!-- b000172 | contents | pages [4] -->
ﬁrst reported in 1976 in both Sudan and the Democratic Republic of the Congo. Due to

<!-- b000173 | contents | pages [4] -->
the highly infectious and deadly nature of the virus, all outbreaks of Ebola prior to 2014

<!-- b000174 | contents | pages [4] -->
had been on the order of several hundred people; most infections had a tendency to ﬂare

<!-- b000175 | contents | pages [4] -->
out before they could spread signiﬁcantly. The sporadic nature of these “ﬂare-up, ﬂare-out”

<!-- b000176 | contents | pages [4] -->
cycles stalled research into the disease, its natural reservoirs, and potential treatments.

<!-- b000177 | contents | pages [4] -->
Ebola Zaire (the strain of Ebola currently aﬄicting West Africa and hereafter referred to

<!-- b000178 | contents | pages [4] -->
as Ebola) is a virus that is transmitted primarily through direct contact with bodily ﬂuids,

<!-- b000179 | contents | pages [4] -->
entering the human body through breaks in the skin or mucus membranes. This means that

<!-- b000180 | contents | pages [4] -->
transmission of the disease is easily stunted through protective equipment and procedures—

<!-- b000181 | contents | pages [4] -->
gloves, masks, and face shields will prevent transmission through ﬂuids and contact, and

<!-- b000182 | contents | pages [4] -->
judicious procedure to replace and clean such equipment will prevent cross-contamination

<!-- b000183 | contents | pages [4] -->
[2].

<!-- b000184 | caption | pages [4] -->
Figure 1: The Ebola virus [3]

<!-- b000185 | contents | pages [4] -->
Once an individual is exposed to Ebola, there is a 2 to 21 day incubation period in which

<!-- b000186 | contents | pages [4] -->
the individual is asymptomatic and not contagious [4]. On average, symptoms develop in 8 to

<!-- b000187 | contents | pages [4] -->
10 days. Early symptoms resemble inﬂuenza and a variety of other, more common diseases,

<!-- b000188 | contents | pages [4] -->
complicating detection and treatment eﬀorts. Over a span of days, symptoms go from ﬂu-like

<!-- b000189 | contents | pages [4] -->
(fever, chills, headache, weakness, sore throat, stomach pain) to much more severe symptoms

<!-- b000190 | contents | pages [4] -->
characteristic to hemorrhagic fevers, including dramatic bleeding, extremely high fever, and

<!-- b000191 | contents | pages [4] -->
organ failure [4].

<!-- b000192 | contents | pages [4] -->
Fatality rates from Ebola Virus Disease range from 40%-90% percent

<!-- b000193 | contents | pages [4] -->
depending on the outbreak; in the current West African outbreak, the reported fatality rate

<!-- b000194 | contents | pages [4] -->
is approximately 50% to 61% [1].

<!-- b000195 | furniture | pages [5] -->
Team # 32722

<!-- b000196 | furniture | pages [5] -->
Page 5 of 37

<!-- b000197 | caption | pages [5] -->
Figure 2: Senegal, Nigeria, Guinea, Sierra Leone, and Liberia constitute the critical Ebola nations of West

<!-- b000198 | contents | pages [5] -->
Africa. Currently, only Sierra Leone, Guinea, and Liberia have an active outbreak [1].

<!-- b000199 | contents | pages [5] -->
The Ebola outbreak in West Africa spans several nations in the region, but is most severe

<!-- b000200 | contents | pages [5] -->
in Guinea, Liberia, and Sierra Leone. Nigeria, Senegal, and Mali have also reported cases,

<!-- b000201 | contents | pages [5] -->
but disease response measures have proven eﬀective in preventing further spread of the virus,

<!-- b000202 | contents | pages [5] -->
and these nations are considered free of the virus as of February 4, 2015 [1]. A scattering

<!-- b000203 | contents | pages [5] -->
of imported cases have also been reported in Spain, the United Kingdom, and the United

<!-- b000204 | contents | pages [5] -->
States; however these nations have by and large leveraged their enormous medical resources

<!-- b000205 | contents | pages [5] -->
to prevent further cases, containing it to a handful of persons. To eﬀectively model the

<!-- b000206 | contents | pages [5] -->
factors that made it possible for the normally ﬂare-out prone Ebola to so devastate these

<!-- b000207 | contents | pages [5] -->
nations, it is important to understand the region’s current state and issues.

<!-- b000208 | contents | pages [5] -->
Demographically, the population of West Africa is both large and young, with a total

<!-- b000209 | contents | pages [5] -->
population of approximately 340 million people and an average age of 18 [5]. While there are

<!-- b000210 | contents | pages [5] -->
three major language groups, the ethnic population of the region deﬁes simple classiﬁcation,

<!-- b000211 | contents | pages [5] -->
consisting of a mosaic of tribal and ethnic ties. As mentioned previously, the region suﬀers

<!-- b000212 | contents | pages [5] -->
from a dire lack of both transportation and medical infrastructure owing partially to its

<!-- b000213 | contents | pages [5] -->
prior status as European resource-extraction colonies and military dictatorships. Liberia,

<!-- b000214 | contents | pages [5] -->
for example, had only ﬁfty physicians in the entire country prior to the outbreak. This lack

<!-- b000215 | contents | pages [5] -->
of medical infrastructure is further compounded by other ongoing medical crises, such as

<!-- b000216 | contents | pages [5] -->
the AIDS epidemic and malaria. In addition, years of despotic rule and war have severely

<!-- b000217 | contents | pages [5] -->
reduced the ability of the populace to trust both their own government and ediﬁcies of

<!-- b000218 | contents | pages [5] -->
foreign intervention, complicating control eﬀorts from local governments, the World Health

<!-- b000219 | contents | pages [5] -->
organization, and Doctors without Borders.

<!-- b000220 | contents | pages [5] -->
1.2. The Task at Hand

<!-- b000221 | contents | pages [5] -->
Should a cure or vaccine for Ebola be developed, it is extremely likely that its initial

<!-- b000222 | contents | pages [5] -->
supply will be extremely limited. At the same time, given the current spread of the out-

<!-- b000223 | contents | pages [5] -->
break and the number of lives at risk, it will be critical to utilize the available medicines to

<!-- b000224 | furniture | pages [6] -->
Team # 32722

<!-- b000225 | furniture | pages [6] -->
Page 6 of 37

<!-- b000226 | contents | pages [6] -->
combat and eventually eradicate Ebola as rapidly as possible. Our team aims to develop a

<!-- b000227 | contents | pages [6] -->
mathematical model to formulate eﬀective strategies for vaccine/cure delivery in this region,

<!-- b000228 | contents | pages [6] -->
so as to minimize loss of life as well as the global impact and ﬁnancial burden associated

<!-- b000229 | contents | pages [6] -->
with this outbreak.

<!-- b000230 | contents | pages [6] -->
1.3. Previous Work

<!-- b000231 | contents | pages [6] -->
* Modeling epidemics using mathematics is a practice that dates back before the widespread

<!-- b000232 | contents | pages [6] -->
acceptance of germ theory, starting instead with Bernoulli’s model of the spread of smallpox

<!-- b000233 | contents | pages [6] -->
and the impact of the smallpox vaccine [6]. This model was one of the ﬁrst applications of

<!-- b000234 | contents | pages [6] -->
the now-common branch of diﬀerential equations known as population modeling. Bernoulli

<!-- b000235 | contents | pages [6] -->
was among the ﬁrst to demonstrate mathematically the eﬀectiveness of vaccination, a major

<!-- b000236 | contents | pages [6] -->
landmark that has been ignored by the superstitious ever since.

<!-- b000237 | contents | pages [6] -->
From these population models, a branch of the diﬀerential equations based modeling

<!-- b000238 | contents | pages [6] -->
approach known as compartmental models arose.

<!-- b000239 | contents | pages [6] -->
First seen in 1927 with Kermack and

<!-- b000240 | contents | pages [6] -->
McKendrick’s “Susceptible - Infected - Recovered” (SIR) approach, these models provide a

<!-- b000241 | contents | pages [6] -->
means of modeling the development of epidemics while taking into account the characteristics

<!-- b000242 | contents | pages [6] -->
of the disease being spread [7]. These SIR models have proven themselves to be extremely

<!-- b000243 | contents | pages [6] -->
adaptable, and are frequently used to deterministically analyze the spread of relatively non-

<!-- b000244 | contents | pages [6] -->
lethal diseases like Measles and Chickenpox in small populations. These models have served

<!-- b000245 | contents | pages [6] -->
as the framework for the bulk of the epidemic modeling work done in the mid to late 20th

<!-- b000246 | contents | pages [6] -->
century. The rise of computational power in the late 20th century has enabled the creation

<!-- b000247 | contents | pages [6] -->
of an entirely new category of numerical, agent-based models for simulating the spread of

<!-- b000248 | contents | pages [6] -->
epidemics.

<!-- b000249 | contents | pages [6] -->
1.4. The GLEAM Simulator

<!-- b000250 | contents | pages [6] -->
The Global Epidemic And Mobility simulation/visualizer suite (or GLEAMviz/GLEAM)

<!-- b000251 | contents | pages [6] -->
is a framework for the creation of extremely detailed models of disease spread on a global

<!-- b000252 | contents | pages [6] -->
scale. GLEAM uses a modular, multi-layer approach to incorporate many layers of informa-

<!-- b000253 | contents | pages [6] -->
tion into a high-ﬁdelity state-based simulation [8].

<!-- b000254 | contents | pages [6] -->
GLEAM’s primary beneﬁt is its extremely detailed mobility model, which incorporates

<!-- b000255 | contents | pages [6] -->
data from a variety of commercial and government sources on road, rail, sea, and air trans-

<!-- b000256 | contents | pages [6] -->
portation between deﬁned transportation “regions.” An accurate model of transportation

<!-- b000257 | contents | pages [6] -->
between regions is incredibly important for accurately simulating the spread of a disease

<!-- b000258 | contents | pages [6] -->
originating in discrete regions, and GLEAM delivers on this point.

<!-- b000259 | contents | pages [6] -->
Regional spread and disease progression characteristics are determined by stochastic,

<!-- b000260 | contents | pages [6] -->
state-based rules deﬁned within each region. Each simulated person has an associated state,

<!-- b000261 | contents | pages [6] -->
such as infected or recovered.

<!-- b000262 | contents | pages [6] -->
As time progresses in the simulation, each person has a

<!-- b000263 | contents | pages [6] -->
chance to change from their current state to another state. The possible states, as well

<!-- b000264 | contents | pages [6] -->
as the probability of changing to any given state, can be deﬁned using a directed graph

<!-- b000265 | contents | pages [6] -->
of states to states, with edges weighted by the probability of changing from one state to

<!-- b000266 | contents | pages [6] -->
another. GLEAM allows users to rapidly implement their own set of state-changing rules

<!-- b000267 | contents | pages [6] -->
using its convenient desktop client. Unfortunately we were unable to utilize this software for

<!-- b000268 | contents | pages [6] -->
our own purposes (due to limitations to be discussed later), though we did see merit in such

<!-- b000269 | contents | pages [6] -->
a novel and extensible state-based approach.

<!-- b000270 | furniture | pages [7] -->
Team # 32722

<!-- b000271 | furniture | pages [7] -->
Page 7 of 37

<!-- b000272 | contents | pages [7] -->
2. Our Model

<!-- b000273 | contents | pages [7] -->
2.1. Modeling Objectives

<!-- b000274 | contents | pages [7] -->
We aim to develop a model that captures the behavior of both the current Ebola outbreak

<!-- b000275 | contents | pages [7] -->
in West Africa and the impact that a hypothetical vaccine or cure for Ebola would have on

<!-- b000276 | contents | pages [7] -->
said outbreak. This aim is easily separated into two components: accurately accounting for

<!-- b000277 | contents | pages [7] -->
the various factors and implications behind the spread of Ebola, and providing a model of

<!-- b000278 | contents | pages [7] -->
the intricacies involved in the distribution and application of such treatments. This ﬂows

<!-- b000279 | contents | pages [7] -->
down and creates further issues that must be dealt with.

<!-- b000280 | contents | pages [7] -->
Ebola’s distinctive prognosis is a signiﬁcant enough factor in its spread that we feel the

<!-- b000281 | contents | pages [7] -->
need to incorporate it in our model. For an epidemic disease, Ebola tends to strike and

<!-- b000282 | contents | pages [7] -->
kill at an alarming rate, with only a brief symptomatic period before an infected individual

<!-- b000283 | contents | pages [7] -->
dies. This behavior, while frightening, has tended in the past to produce intense but short-

<!-- b000284 | contents | pages [7] -->
lived outbreaks as the disease strikes down individuals before they can spread it to others.

<!-- b000285 | contents | pages [7] -->
While this outbreak appears to buck the trend, it is still subject to the same fundamental

<!-- b000286 | contents | pages [7] -->
progression of symptoms as the others; by ensuring that these characteristics are modeled

<!-- b000287 | contents | pages [7] -->
faithfully, we can more carefully analyze scenarios that play oﬀthe natural tendency of the

<!-- b000288 | contents | pages [7] -->
virus to cause self-destroying outbreaks.

<!-- b000289 | contents | pages [7] -->
As mentioned in Sec. 1, the current outbreak has arisen from a complex combination of

<!-- b000290 | contents | pages [7] -->
social, political, economic, and ecological factors in West Africa, and many of these factors

<!-- b000291 | contents | pages [7] -->
continue to complicate the health response.

<!-- b000292 | contents | pages [7] -->
We make a decided eﬀort to capture these

<!-- b000293 | contents | pages [7] -->
“environmental” factors as they relate to the direct spread of Ebola, especially when they

<!-- b000294 | contents | pages [7] -->
are characteristic of the outbreak, cf. sections 2.3.1 and 2.3.3. Examples of characteristic

<!-- b000295 | contents | pages [7] -->
environmental factors inﬂuencing the spread of the outbreak include infection from burial

<!-- b000296 | contents | pages [7] -->
and human migration.

<!-- b000297 | contents | pages [7] -->
Our ﬁnal criterion for the model is that it faithfully and accurately shows the impacts

<!-- b000298 | contents | pages [7] -->
of a hypothetical vaccine on the ongoing epidemic, which is surprisingly even harder than it

<!-- b000299 | contents | pages [7] -->
sounds. The hypothetical nature of the vaccine or cure gives us control over its eﬀectiveness

<!-- b000300 | contents | pages [7] -->
and mechanism of action, but also presents a large unknown within our model that must be

<!-- b000301 | contents | pages [7] -->
able to be tuned. Likewise, the freedom inherent to the unspeciﬁed distribution mechanism

<!-- b000302 | contents | pages [7] -->
for the treatments requires us to model the impact of the geographic and infrastructure

<!-- b000303 | contents | pages [7] -->
constraints of the region.

<!-- b000304 | contents | pages [7] -->
2.2. Problem Space

<!-- b000305 | contents | pages [7] -->
Breaking down these aims into something we could feasibly create in 96 hours was not a

<!-- b000306 | contents | pages [7] -->
simple task. To simplify the problems our model must deal with, we have seen it prudent to

<!-- b000307 | contents | pages [7] -->
deﬁne a problem-space through the deﬁnition of boundary assumptions. The implications

<!-- b000308 | contents | pages [7] -->
of these boundary assumptions are expanded upon further in Sec. 3 and Appendix A.

<!-- b000309 | contents | pages [7] -->
Firstly, we have limited our model’s geographic scope to cover only the three most infected

<!-- b000310 | contents | pages [7] -->
countries over the next six months, Guinea, Liberia, and Sierra Leone. While this boundary

<!-- b000311 | contents | pages [7] -->
does not explicitly limit the ability of our model to deal with other nations or epidemics

<!-- b000312 | contents | pages [7] -->
outside of these nations, it does allow us to focus more heavily on those nations that are

<!-- b000313 | contents | pages [7] -->
hardest hit and therefore most likely to receive a coordinated eradication campaign and tailor

<!-- b000314 | contents | pages [7] -->
our model more closely to these critical regions.

<!-- b000315 | furniture | pages [8] -->
Team # 32722

<!-- b000316 | furniture | pages [8] -->
Page 8 of 37

<!-- b000317 | caption | pages [8] -->
Figure 3: The network and interaction of diﬀerent regions are mediated by the sub-network of cities in each

<!-- b000318 | contents | pages [8] -->
region, which is further mediated by the interaction of individuals in a city. Each individual is characterized

<!-- b000319 | contents | pages [8] -->
by a state in the compartment diagram, simulating progression through the epidemic at the base interaction

<!-- b000320 | contents | pages [8] -->
level, cf. Fig. 4 and Sec. 2.3.1.

<!-- b000321 | contents | pages [8] -->
Secondly, we expect our model to produce meaningful results only over a short term (i.e.

<!-- b000322 | contents | pages [8] -->
six month) period. The failure of other models devised by major medical associations to

<!-- b000323 | contents | pages [8] -->
forecast long-term conditions is indicative of the incredibly stochastic, complex, and deeply

<!-- b000324 | contents | pages [8] -->
time-varying behaviors lurking behind the epidemic. A short list of these factors includes

<!-- b000325 | contents | pages [8] -->
population growth, migration, seasonal change, and the international political will to support

<!-- b000326 | contents | pages [8] -->
aid eﬀorts. Rather than concerning ourselves with these long-term and varying causes, we

<!-- b000327 | contents | pages [8] -->
can instead concentrate on more immediate and clear factors that will impact near-term

<!-- b000328 | contents | pages [8] -->
results.

<!-- b000329 | contents | pages [8] -->
2.3. The Multi-Layer State Based Stochastic Epidemic Model

<!-- b000330 | contents | pages [8] -->
The relatively broad scope of our model necessitated the choice of a modeling framework

<!-- b000331 | contents | pages [8] -->
that supports a high level of detail at both the individual level, wherein persons can become

<!-- b000332 | contents | pages [8] -->
infected and progress through the disease with varying levels of infectiousness, to the level of

<!-- b000333 | contents | pages [8] -->
an entire nation and set of nations. The implicitly multi-layer nature of this problem space

<!-- b000334 | contents | pages [8] -->
drove us to use what we describe as a multi-layer state-based stochastic epidemic model, a

<!-- b000335 | contents | pages [8] -->
relatively recent approach.

<!-- b000336 | contents | pages [8] -->
At the most basic level, the simulation models individuals as state-based creatures that

<!-- b000337 | contents | pages [8] -->
are some quantized level of healthy ranging from susceptible to infected. Individuals tran-

<!-- b000338 | contents | pages [8] -->
sition between states in a stochastic manner, allowing for the simulation of transitions from

<!-- b000339 | contents | pages [8] -->
merely infected to extremely ill to dead. The same probability-based approach also governs

<!-- b000340 | furniture | pages [9] -->
Team # 32722

<!-- b000341 | furniture | pages [9] -->
Page 9 of 37

<!-- b000342 | contents | pages [9] -->
the likelihood that an individual will become infected from other infected individuals. More

<!-- b000343 | contents | pages [9] -->
details on the speciﬁc structure and function of this layer can be found in the following

<!-- b000344 | contents | pages [9] -->
section.

<!-- b000345 | contents | pages [9] -->
Moving one layer up from the individual models is the regional or “city” model. Each

<!-- b000346 | contents | pages [9] -->
city acts as a node in a larger network, with connections to nearby cities that allow for the

<!-- b000347 | contents | pages [9] -->
modeling of intercity movement and transportation dynamics. Although a city is comprised

<!-- b000348 | contents | pages [9] -->
of individual state-based persons, the interactions between cities can be governed by diﬀerent

<!-- b000349 | contents | pages [9] -->
rules that may not arise from individual modeling alone.

<!-- b000350 | contents | pages [9] -->
Cities can be likewise grouped into nations and further grouped into regions and conti-

<!-- b000351 | contents | pages [9] -->
nents ad absurdum, allowing for progressively larger (or smaller) levels of detail that can be

<!-- b000352 | contents | pages [9] -->
implemented in a modular way. A simulation done at the national level, for example, can

<!-- b000353 | contents | pages [9] -->
be further reﬁned by breaking nations into districts and modeling them separately, down to

<!-- b000354 | contents | pages [9] -->
the level of individual villages or neighborhoods. This implicit scalability and potential for

<!-- b000355 | contents | pages [9] -->
detail made the model extremely attractive for our purposes. Our speciﬁc implementation

<!-- b000356 | contents | pages [9] -->
of this model is described below.

<!-- b000357 | contents | pages [9] -->
2.3.1. Individual Layer - Stochastic State Based Model

<!-- b000358 | contents | pages [9] -->
At the beginning of each simulation, we designate a number of individuals as either

<!-- b000359 | contents | pages [9] -->
susceptible, latent, or infectious based oﬀof World Health Organization (WHO) data on the

<!-- b000360 | contents | pages [9] -->
outbreak. These individuals are accurately spread throughout the aﬄicted districts based

<!-- b000361 | contents | pages [9] -->
on the February 2015 Situation Report [1] and, as previously mentioned, progress through

<!-- b000362 | contents | pages [9] -->
the states deﬁned in Fig. 4.

<!-- b000363 | contents | pages [9] -->
Before even entering into the probability of a state transition, individuals that are sus-

<!-- b000364 | contents | pages [9] -->
ceptible, latent, or displaying early symptoms check to see if they “decide” to move based

<!-- b000365 | contents | pages [9] -->
on their region’s probability of movement, a factor whose determination is discussed in Sec.

<!-- b000366 | contents | pages [9] -->
2.3.3. Regardless of the outcome of this roll, individuals then proceed to check the modiﬁ-

<!-- b000367 | contents | pages [9] -->
cations of their state within the context of their starting region on that day.

<!-- b000368 | contents | pages [9] -->
Transitions between states are probabilistic at two levels, depending on the transition.

<!-- b000369 | contents | pages [9] -->
All transitions have a probability of occurring within the state model, deﬁned in Table 1

<!-- b000370 | contents | pages [9] -->
when an individual is in the preceding state.

<!-- b000371 | contents | pages [9] -->
Some interactions, speciﬁcally the chance

<!-- b000372 | contents | pages [9] -->
of a susceptible individual becoming infected and the chance of an individual becoming

<!-- b000373 | contents | pages [9] -->
hospitalized or vaccinated, must be triggered by the simulation before the aforementioned

<!-- b000374 | contents | pages [9] -->
probability calculation.

<!-- b000375 | contents | pages [9] -->
The probabilities of an individual triggering an interaction with an individual deemed

<!-- b000376 | contents | pages [9] -->
infectious (broken up into early stage symptomatic, late stage symptomatic, and unburied

<!-- b000377 | contents | pages [9] -->
individuals) is simulation dependent and calculated at each timestep from the following

<!-- b000378 | contents | pages [9] -->
equation:

<!-- b000379 | contents | pages [9] -->
Pinteract = Quantity of type of individual in region

<!-- b000380 | contents | pages [9] -->
Total number of individuals in region

<!-- b000381 | contents | pages [9] -->
After a state transition has been triggered, the simulation checks the probability of such

<!-- b000382 | contents | pages [9] -->
a transition occurring as governed by the probabilities listed in Table 1. These probabilities

<!-- b000383 | contents | pages [9] -->
attempt to ﬁt real-world data on the epidemic to an individual’s progression through the

<!-- b000384 | contents | pages [9] -->
disease, normalized to the average duration of each stage of the illness from available data

<!-- b000385 | contents | pages [9] -->
from Sierra Leone and Liberia. Guinea was discounted due to lack of available statistics,

<!-- b000386 | furniture | pages [10] -->
Team # 32722

<!-- b000387 | furniture | pages [10] -->
Page 10 of 37

<!-- b000388 | caption | pages [10] -->
Figure 4: The directed graph compartment model of the Ebola epidemic; red states both carry and are able

<!-- b000389 | contents | pages [10] -->
to spread the infection, the orange states carry the virus but are not able to spread it, and the blue states

<!-- b000390 | contents | pages [10] -->
do not further interact with the simulation. The grey nodes refer to the contact that must occur in order to

<!-- b000391 | contents | pages [10] -->
progress to the next state.

<!-- b000392 | contents | pages [10] -->
and when referenced used data from Liberia. This approach means that, on average, the

<!-- b000393 | contents | pages [10] -->
duration of an individual’s case will be similar if not identical to the average real individual.

<!-- b000394 | contents | pages [10] -->
In the case of susceptible individual triggering an interaction with a carrier of the virus,

<!-- b000395 | contents | pages [10] -->
the simulation checks to see if the susceptible individual deﬁnitively contracts the disease,

<!-- b000396 | contents | pages [10] -->
a probability governed by the parameters βc1, βc2, and βf respectively. These parameters

<!-- b000397 | contents | pages [10] -->
represent the probability of an individual becoming infected from contact with an early-stage

<!-- b000398 | contents | pages [10] -->
infected individual, a late stage infected individual, or a deceased but unburied individual,

<!-- b000399 | contents | pages [10] -->
respectively. Once an individual is determined to have contracted the disease, they transition

<!-- b000400 | contents | pages [10] -->
to the latent state.

<!-- b000401 | contents | pages [10] -->
Latent individuals will eventually transition to early-stage symptomatic individuals at

<!-- b000402 | contents | pages [10] -->
a rate governed by γw1. The rate γw1 is calculated by taking the inverse of the average

<!-- b000403 | contents | pages [10] -->
incubation period, consistent with the other data sets [9]. Latent individuals are assumed to

<!-- b000404 | contents | pages [10] -->
be blind to the fact that they have contracted Ebola, and behave identically to susceptible

<!-- b000405 | contents | pages [10] -->
individuals, including their attempts to seek vaccination and move. Unfortunately for them,

<!-- b000406 | contents | pages [10] -->
our simulated vaccines do not work on individuals who have already contracted the virus1

<!-- b000407 | contents | pages [10] -->
1In real life, this behavior has the potential for interesting second- and third- order eﬀects, such as

<!-- b000408 | contents | pages [10] -->
“vaccinated” individuals becoming ill and reducing public trust in the vaccine. Sadly, we do not attempt to

<!-- b000409 | furniture | pages [11] -->
Team # 32722

<!-- b000410 | furniture | pages [11] -->
Page 11 of 37

<!-- b000411 | contents | pages [11] -->
Liberia

<!-- b000412 | contents | pages [11] -->
Sierra Leone

<!-- b000413 | contents | pages [11] -->
Parameter

<!-- b000414 | contents | pages [11] -->
Value

<!-- b000415 | contents | pages [11] -->
Value

<!-- b000416 | contents | pages [11] -->
Factor

<!-- b000417 | contents | pages [11] -->
βc1

<!-- b000418 | contents | pages [11] -->
0.1600

<!-- b000419 | contents | pages [11] -->
0.1280

<!-- b000420 | contents | pages [11] -->
Early-stage contraction probability

<!-- b000421 | contents | pages [11] -->
βc2

<!-- b000422 | contents | pages [11] -->
0.3200

<!-- b000423 | contents | pages [11] -->
0.2560

<!-- b000424 | contents | pages [11] -->
Late-stage contraction probability

<!-- b000425 | contents | pages [11] -->
βf

<!-- b000426 | contents | pages [11] -->
0.4890

<!-- b000427 | contents | pages [11] -->
0.1110

<!-- b000428 | contents | pages [11] -->
Unburied contraction probability

<!-- b000429 | contents | pages [11] -->
γw1

<!-- b000430 | contents | pages [11] -->
0.0833

<!-- b000431 | contents | pages [11] -->
0.0800

<!-- b000432 | contents | pages [11] -->
Average rate of developing symptoms

<!-- b000433 | contents | pages [11] -->
γw2

<!-- b000434 | contents | pages [11] -->
0.1667

<!-- b000435 | contents | pages [11] -->
0.1600

<!-- b000436 | contents | pages [11] -->
Average rate of symptoms worsening [10]

<!-- b000437 | contents | pages [11] -->
γh1

<!-- b000438 | contents | pages [11] -->
0.0608

<!-- b000439 | contents | pages [11] -->
0.0478

<!-- b000440 | contents | pages [11] -->
Probability of an early-stage hospitalization

<!-- b000441 | contents | pages [11] -->
γh2

<!-- b000442 | contents | pages [11] -->
0.1216

<!-- b000443 | contents | pages [11] -->
0.0956

<!-- b000444 | contents | pages [11] -->
Probability of a late-stage hospitalization

<!-- b000445 | contents | pages [11] -->
γd

<!-- b000446 | contents | pages [11] -->
0.0335

<!-- b000447 | contents | pages [11] -->
0.0580

<!-- b000448 | contents | pages [11] -->
Probability of untreated late-stage death

<!-- b000449 | contents | pages [11] -->
γdh

<!-- b000450 | contents | pages [11] -->
0.0551

<!-- b000451 | contents | pages [11] -->
0.1198

<!-- b000452 | contents | pages [11] -->
Probability of hospitalized death

<!-- b000453 | contents | pages [11] -->
γR

<!-- b000454 | contents | pages [11] -->
0.0280

<!-- b000455 | contents | pages [11] -->
0.0280

<!-- b000456 | contents | pages [11] -->
Recovery rate and probability

<!-- b000457 | contents | pages [11] -->
γf

<!-- b000458 | contents | pages [11] -->
0.4975

<!-- b000459 | contents | pages [11] -->
0.2222

<!-- b000460 | contents | pages [11] -->
Rate of proper burials

<!-- b000461 | caption | pages [11] -->
Table 1: Model parameter values and explanation. Guinea shares the same parameters as Liberia. Most of

<!-- b000462 | contents | pages [11] -->
the parameter values were taken or derived from Rivers et al. [9]

<!-- b000463 | contents | pages [11] -->
Early-stage symptomatic individuals are faced with a choice: become hospitalized with

<!-- b000464 | contents | pages [11] -->
a probability γh1, which has some chance of curing them, or allow their infection to continue

<!-- b000465 | contents | pages [11] -->
to worsen at probability γw2. The probabilities of hospitalization, γh1 and γh2, are a product

<!-- b000466 | contents | pages [11] -->
of the portion of cases that are both reported and hospitalized, 0.197, and the inverse of

<!-- b000467 | contents | pages [11] -->
the average time from infection to hospitalization, 3.24 days. As we are considering two

<!-- b000468 | contents | pages [11] -->
stages of infectious, we make the assumption that the probability of hospitalization of a

<!-- b000469 | contents | pages [11] -->
late-stage person is double that of the early-stage. We believe that this reﬂects the fact that

<!-- b000470 | contents | pages [11] -->
more individuals will attempt to be admitted into a hospital once they realize that their

<!-- b000471 | contents | pages [11] -->
symptoms have advanced beyond a standard ﬂu.

<!-- b000472 | contents | pages [11] -->
Once an individual “decides” to seek hospitalization, the simulation checks to see if a

<!-- b000473 | contents | pages [11] -->
hospital bed is actually available in that region. If a bed is available, the individual transitions

<!-- b000474 | contents | pages [11] -->
to the hospitalized state and the number of available beds in the region decreases by 1.

<!-- b000475 | contents | pages [11] -->
The extremely deadly nature of Ebola is reﬂected in the probabilities of death from

<!-- b000476 | contents | pages [11] -->
hospitalization and untreated late-stage infection. The late-stage death probability, γd, is

<!-- b000477 | contents | pages [11] -->
derived from a number of factors. We factor in the percentage of cases that are reported but

<!-- b000478 | contents | pages [11] -->
not hospitalized, (1 −0.197), the current case mortality rate as of February 6, 2015, (0.555),

<!-- b000479 | contents | pages [11] -->
and the inverse of the average time from infection to death, 13.31 days. The probability of

<!-- b000480 | contents | pages [11] -->
death after hospitalization, γdh, is the product of the case mortality rate and the inverse of

<!-- b000481 | contents | pages [11] -->
the average time from hospitalization to death, 10.07 days.

<!-- b000482 | contents | pages [11] -->
On the other hand, the recovery rate, γR, is the product of the survival rate, (1 −0.555),

<!-- b000483 | contents | pages [11] -->
and the inverse of the average time of treated recovery, 15.88 days.

<!-- b000484 | contents | pages [11] -->
One of the reasons experts believe the current outbreak has been sustained for as long

<!-- b000485 | contents | pages [11] -->
as it has is regional attitudes on corpse-handling, with some traditional funerals calling for

<!-- b000486 | contents | pages [11] -->
a variety of close contact with the corpse (hugging, kissing, touching, et cetera) that allows

<!-- b000487 | contents | pages [11] -->
for infection to occur between individuals and highly infectious corpses. Rivers et al. report

<!-- b000488 | contents | pages [11] -->
model such behavior.

<!-- b000489 | furniture | pages [12] -->
Team # 32722

<!-- b000490 | furniture | pages [12] -->
Page 12 of 37

<!-- b000491 | contents | pages [12] -->
that the traditional funeral in Liberia will last 2.01 days on average. It is during this time

<!-- b000492 | contents | pages [12] -->
that a susceptible individual will be able to become infected by an unburied individual with

<!-- b000493 | contents | pages [12] -->
contact probability βf; hence, the probability to transition from unburied to buried, γf, is

<!-- b000494 | contents | pages [12] -->
essentially the rate of proper burials, 1/(2.01 days).

<!-- b000495 | contents | pages [12] -->
For the implementation of the vaccine, we assume the ideal situation of a 100% eﬀective

<!-- b000496 | contents | pages [12] -->
vaccine. Thus we do not have a probability for the transition of susceptible to vaccinated

<!-- b000497 | contents | pages [12] -->
after contact with the vaccination event. Rather, the probability of vaccination is determined

<!-- b000498 | contents | pages [12] -->
by the simulation itself through the supply and demand of the vaccine. In Fig. 4, the latent

<!-- b000499 | contents | pages [12] -->
individuals loop back to themselves upon the vaccination event, reﬂecting the fact that the

<!-- b000500 | contents | pages [12] -->
vaccination did not work since they are already infected and that they have used some of

<!-- b000501 | contents | pages [12] -->
the vaccine supply as well.

<!-- b000502 | contents | pages [12] -->
2.3.2. Inter-Region Layer modeling

<!-- b000503 | contents | pages [12] -->
Operating at a level above the individual is the region, which is broadly speaking a

<!-- b000504 | contents | pages [12] -->
representation of a discrete statistical region; in less abstract terms, regions represent villages,

<!-- b000505 | contents | pages [12] -->
cities, or entire national districts and nations themselves depending on the scale of the

<!-- b000506 | contents | pages [12] -->
simulation. Regions provide a number of beneﬁts to the ﬁdelity of the simulation that are

<!-- b000507 | contents | pages [12] -->
unwieldy to model at the individual level, especially with regards to the impact of geography

<!-- b000508 | contents | pages [12] -->
on the spread of disease.

<!-- b000509 | contents | pages [12] -->
Each region has a number of parameters that can be deﬁned and modiﬁed to reﬂect

<!-- b000510 | contents | pages [12] -->
geographic and statistical realities, cf. Table 1. Regions interact with other regions through

<!-- b000511 | contents | pages [12] -->
discrete, well-deﬁned set of connections in a graph-like manner. Each day, individual regions

<!-- b000512 | contents | pages [12] -->
ﬁrst check to update their stockpiles of vaccines and or cure2 as determined by the drug

<!-- b000513 | contents | pages [12] -->
distribution model (cf. Sec. 2.3.4), and then check to see what the quantity of migration

<!-- b000514 | contents | pages [12] -->
between regions occurs (cf. Sec. 2.3.3). These probabilities are then passed down to the

<!-- b000515 | contents | pages [12] -->
aforementioned individual layer to determine actual movement and cure usage.

<!-- b000516 | contents | pages [12] -->
An astute reader will recognize this setup as a subtype of the compartmental diﬀerential

<!-- b000517 | contents | pages [12] -->
equations approach to epidemic modeling outlined in Sec. 1.3

<!-- b000518 | contents | pages [12] -->
2.3.3. Human Mobility Model

<!-- b000519 | contents | pages [12] -->
There are two widely used theories for modeling human mobility, the so-called “radiation”

<!-- b000520 | contents | pages [12] -->
and “gravity” theories. The radiation model predicts the ﬂux of travel between two cities,

<!-- b000521 | contents | pages [12] -->
Tij by their respective populations, Pi and Pj, and the population density of the surrounding

<!-- b000522 | contents | pages [12] -->
area3, sij,

<!-- b000523 | contents | pages [12] -->
PiPj

<!-- b000524 | contents | pages [12] -->
Tij = Ti

<!-- b000525 | contents | pages [12] -->
(1)

<!-- b000526 | contents | pages [12] -->
(Pi + sij)(Pi + Pj + sij)

<!-- b000527 | contents | pages [12] -->
where Ti is the number of commuters from city i. The standard gravity model predicts the

<!-- b000528 | contents | pages [12] -->
ﬂux of travel as a function only of the population of the two cities and the inverse of the

<!-- b000529 | contents | pages [12] -->
2after all, if there was a life-threatening epidemic, isn’t that the ﬁrst thing you would do each morning?

<!-- b000530 | contents | pages [12] -->
3sij is formally deﬁned as the population within a circle centered at i extending to j excluding the

<!-- b000531 | contents | pages [12] -->
populations Pi and Pj.

<!-- b000532 | furniture | pages [13] -->
Team # 32722

<!-- b000533 | furniture | pages [13] -->
Page 13 of 37

<!-- b000534 | contents | pages [13] -->
Implication

<!-- b000535 | contents | pages [13] -->
Constant

<!-- b000536 | contents | pages [13] -->
Value

<!-- b000537 | contents | pages [13] -->
α

<!-- b000538 | contents | pages [13] -->
Prevalence of destination population

<!-- b000539 | contents | pages [13] -->
0.78

<!-- b000540 | contents | pages [13] -->
β

<!-- b000541 | contents | pages [13] -->
Prevalence of travel distance

<!-- b000542 | contents | pages [13] -->
1.60

<!-- b000543 | contents | pages [13] -->
γ

<!-- b000544 | contents | pages [13] -->
Prevalence of native city population

<!-- b000545 | contents | pages [13] -->
1.54

<!-- b000546 | contents | pages [13] -->
k

<!-- b000547 | contents | pages [13] -->
Chance factor, see Sec. 3.0.5.2

<!-- b000548 | contents | pages [13] -->
—

<!-- b000549 | caption | pages [13] -->
Table 2: Modiﬁed gravity mobility model constants for the best ﬁt to the Guinea mobility census microdata.

<!-- b000550 | contents | pages [13] -->
distance between them to a quadratic order,

<!-- b000551 | contents | pages [13] -->
i P β

<!-- b000552 | contents | pages [13] -->
Tij = P α

<!-- b000553 | contents | pages [13] -->
where α,β, and γ are ﬁtting constants.

<!-- b000554 | contents | pages [13] -->
j

<!-- b000555 | contents | pages [13] -->
(2)

<!-- b000556 | contents | pages [13] -->
rγ

<!-- b000557 | contents | pages [13] -->
ij

<!-- b000558 | contents | pages [13] -->
The literature reports that the radiation model

<!-- b000559 | contents | pages [13] -->
Unfortunately, our simulation is based around

<!-- b000560 | contents | pages [13] -->
more accurately matches empirical data.

<!-- b000561 | contents | pages [13] -->
interactions between distinct groups of people (“regions”) rather than continuous population

<!-- b000562 | contents | pages [13] -->
distributions. The consequence is that we would be unable to get a realistic value for sij

<!-- b000563 | contents | pages [13] -->
[11].

<!-- b000564 | contents | pages [13] -->
Data on human mobility is sparse for West Africa, and while this data set does not

<!-- b000565 | contents | pages [13] -->
fully encompass every aspect of human movement, we considered it the most relevant and

<!-- b000566 | contents | pages [13] -->
accurate data for the purpose of having a comparison for our simulation [12]. We initially

<!-- b000567 | contents | pages [13] -->
implemented the standard gravity model, yet quickly realized that we could not simulate

<!-- b000568 | contents | pages [13] -->
human movement in a manner that would make sense; cities became black holes that drained

<!-- b000569 | contents | pages [13] -->
the surrounding populations and lead to unreasonable population densities.

<!-- b000570 | contents | pages [13] -->
To capture a realistic movement of people as well as normalize the movement for the

<!-- b000571 | contents | pages [13] -->
simplicity of our simulation, we derived a modiﬁed gravity model, deﬁned as follows:

<!-- b000572 | contents | pages [13] -->


<!-- b000573 | contents | pages [13] -->
−1

<!-- b000574 | contents | pages [13] -->


<!-- b000575 | contents | pages [13] -->
φi(t)2βP γ

<!-- b000576 | contents | pages [13] -->
Φij(t) = k · φj(t)P α

<!-- b000577 | contents | pages [13] -->
j (t)

<!-- b000578 | contents | pages [13] -->
rβ

<!-- b000579 | contents | pages [13] -->
ij

<!-- b000580 | contents | pages [13] -->


<!-- b000581 | contents | pages [13] -->
φk(t)P α

<!-- b000582 | contents | pages [13] -->
k (t)

<!-- b000583 | contents | pages [13] -->
i (t)

<!-- b000584 | contents | pages [13] -->
X

<!-- b000585 | contents | pages [13] -->
+

<!-- b000586 | contents | pages [13] -->
(3)

<!-- b000587 | contents | pages [13] -->


<!-- b000588 | contents | pages [13] -->
rβ

<!-- b000589 | contents | pages [13] -->
rβ

<!-- b000590 | contents | pages [13] -->
P

<!-- b000591 | contents | pages [13] -->
ik

<!-- b000592 | contents | pages [13] -->
ik

<!-- b000593 | contents | pages [13] -->
k

<!-- b000594 | contents | pages [13] -->
k

<!-- b000595 | contents | pages [13] -->
−1

<!-- b000596 | contents | pages [13] -->


<!-- b000597 | contents | pages [13] -->
φi(t)2βP γ

<!-- b000598 | contents | pages [13] -->
Φi(t) = k · φi(t)2βP γ

<!-- b000599 | contents | pages [13] -->
i (t)

<!-- b000600 | contents | pages [13] -->
rβ

<!-- b000601 | contents | pages [13] -->
P

<!-- b000602 | contents | pages [13] -->
ik

<!-- b000603 | contents | pages [13] -->
k

<!-- b000604 | contents | pages [13] -->
φk(t)P α

<!-- b000605 | contents | pages [13] -->
i (t)

<!-- b000606 | contents | pages [13] -->
k (t)

<!-- b000607 | contents | pages [13] -->
X

<!-- b000608 | contents | pages [13] -->
+

<!-- b000609 | contents | pages [13] -->
(4)

<!-- b000610 | contents | pages [13] -->


<!-- b000611 | contents | pages [13] -->
rβ

<!-- b000612 | contents | pages [13] -->
rβ

<!-- b000613 | contents | pages [13] -->
P

<!-- b000614 | contents | pages [13] -->
ik

<!-- b000615 | contents | pages [13] -->
ik

<!-- b000616 | contents | pages [13] -->
k

<!-- b000617 | contents | pages [13] -->
k

<!-- b000618 | contents | pages [13] -->
Equation (3) is the probability that an individual will travel from city i to j. Equation

<!-- b000619 | contents | pages [13] -->
(4) is the probability that an individual will remain in city i. In addition to the population

<!-- b000620 | contents | pages [13] -->
density and distance between the cities, we also consider the conﬁdence factor, φi(t), of a

<!-- b000621 | contents | pages [13] -->
city. The conﬁdence factor represents the disposition of an individual considering traveling

<!-- b000622 | contents | pages [13] -->
to a certain city. We reasoned that an individual’s disposition to travel to a city would be

<!-- b000623 | contents | pages [13] -->
based on the number of infected (early-stage, late-stage) individuals, I(t), the number of

<!-- b000624 | contents | pages [13] -->
unburied corpses, U(t), the number of available hospital or treatment center beds, B(t), and

<!-- b000625 | contents | pages [13] -->
the number of doctors and health care staﬀ, D(t). We formally deﬁne the conﬁdence factor

<!-- b000626 | contents | pages [13] -->
as,

<!-- b000627 | furniture | pages [14] -->
Team # 32722

<!-- b000628 | furniture | pages [14] -->
Page 14 of 37

<!-- b000629 | contents | pages [14] -->
" 

<!-- b000630 | contents | pages [14] -->
#

<!-- b000631 | contents | pages [14] -->
−

<!-- b000632 | contents | pages [14] -->


<!-- b000633 | contents | pages [14] -->
 

<!-- b000634 | contents | pages [14] -->


<!-- b000635 | contents | pages [14] -->
B(t) + D(t)

<!-- b000636 | contents | pages [14] -->
I(t) + U(t)

<!-- b000637 | contents | pages [14] -->
φi(t) = exp

<!-- b000638 | contents | pages [14] -->
(5)

<!-- b000639 | contents | pages [14] -->
Pi(t)

<!-- b000640 | contents | pages [14] -->
Since our modiﬁed gravity model is dependent not only on the city populations but also

<!-- b000641 | contents | pages [14] -->
on the highly variant access to treatment and infected population, it is updated at each

<!-- b000642 | contents | pages [14] -->
time step to reﬂect an individual’s changing disposition as the epidemic situation unfolds.

<!-- b000643 | contents | pages [14] -->
In our modiﬁed gravity model we use the ﬁtting constants α, β, γ, and k, for which we have

<!-- b000644 | contents | pages [14] -->
chosen the following values to best ﬁt the data, cf. Table 2. With these values our modiﬁed

<!-- b000645 | contents | pages [14] -->
gravity model matched the Guinea census migration microdata for 33 cities with an average

<!-- b000646 | contents | pages [14] -->
standard deviation of 3.141% and a standard deviation of 4.75% [13]. Due to the lack of

<!-- b000647 | contents | pages [14] -->
mobility data for Liberia or Sierra Leone, we have assumed these same constant values for

<!-- b000648 | contents | pages [14] -->
those simulation sets as well.

<!-- b000649 | contents | pages [14] -->
2.3.4. Supply Distribution Model

<!-- b000650 | contents | pages [14] -->
Accurately simulating the distribution and logistics behind the distribution of anti-Ebola

<!-- b000651 | contents | pages [14] -->
medicines is central to the purpose and design of our model. Each geographic region has a

<!-- b000652 | contents | pages [14] -->
“stockpile” of cures and/or vaccines that can be used to treat aﬄicted persons as outlined in

<!-- b000653 | contents | pages [14] -->
the Disease section. Each time an individual in a region receives a vaccine or medicine, the

<!-- b000654 | contents | pages [14] -->
regional stockpile is depleted by one, regardless of whether or not the vaccine or medicine was

<!-- b000655 | contents | pages [14] -->
eﬀective at treating the disease. In addition, our model uses estimated medical infrastructure

<!-- b000656 | contents | pages [14] -->
capacities to determine the probability of an individual receiving a vaccine or treatment when

<!-- b000657 | contents | pages [14] -->
they are in stock, allowing us to model the impact of constructing additional treatment

<!-- b000658 | contents | pages [14] -->
facilities, the destruction of treatment facilities, and of overcrowding of treatment facilities

<!-- b000659 | contents | pages [14] -->
in light of the continued spread of the disease.

<!-- b000660 | contents | pages [14] -->
We make the assumption that any cure or vaccine would need to be imported into the

<!-- b000661 | contents | pages [14] -->
region, as opposed to it being manufactured locally. This complicates the logistics of vaccine

<!-- b000662 | contents | pages [14] -->
manufacture and distribution, as the limited transportation infrastructure of the region

<!-- b000663 | contents | pages [14] -->
makes transporting large quantities of medicine across thousands of kilometers diﬃcult. To

<!-- b000664 | contents | pages [14] -->
incorporate the implications of this issue, we have included a logistics model that operates

<!-- b000665 | contents | pages [14] -->
independently of the human mobility models.

<!-- b000666 | contents | pages [14] -->
To this end, we have worked out a ﬂexible “hub and spoke” distribution system, cf.

<!-- b000667 | caption | pages [14] -->
Fig. 13. Certain cities can be designated as hub cities, which will regenerate their supplies

<!-- b000668 | contents | pages [14] -->
of vaccine or cure at regular variables that can be changed or scaled to simulate diﬀerent

<!-- b000669 | contents | pages [14] -->
situations. From these hubs, cures and vaccines can travel by a predetermined and scenario-

<!-- b000670 | contents | pages [14] -->
dependent “travel rule” to other cities. This travel rule can be modiﬁed to represent varying

<!-- b000671 | contents | pages [14] -->
levels of loss or spoilage en route, various distribution tactics, and various rates of distribution

<!-- b000672 | contents | pages [14] -->
based on the availability of transportation. The variety of scenarios that can be modeled by

<!-- b000673 | contents | pages [14] -->
this system is a testament to its design.

<!-- b000674 | contents | pages [14] -->
2.3.5. A note on GLEAM

<!-- b000675 | contents | pages [14] -->
Despite its extremely high ﬁdelity data and network models, GLEAM’s closed-source

<!-- b000676 | contents | pages [14] -->
nature makes it unfortunately very diﬃcult to modify, and it lacks built-in support for

<!-- b000677 | contents | pages [14] -->
modifying many of the base parameters that we would be interested in changing, such as the

<!-- b000678 | contents | pages [14] -->
way hospitals and doctors interact with the infected population, production and distribution

<!-- b000679 | furniture | pages [15] -->
Team # 32722

<!-- b000680 | furniture | pages [15] -->
Page 15 of 37

<!-- b000681 | contents | pages [15] -->
of cures, and modiﬁcation of the underlying simulation, which are treated as a black box.

<!-- b000682 | contents | pages [15] -->
In the light of these issues, we found it prudent to develop our own simulation, drawing

<!-- b000683 | contents | pages [15] -->
inspiration from GLEAM.

<!-- b000684 | contents | pages [15] -->
2.4. Implementation

<!-- b000685 | contents | pages [15] -->
Our model uses a GLEAM-like combination of compartmental and metapopulation mod-

<!-- b000686 | contents | pages [15] -->
els to allow us to capture a variety of behaviors both within and between regions. This is

<!-- b000687 | contents | pages [15] -->
implemented in Python, with individuals, regions, and connections between regions deﬁned

<!-- b000688 | contents | pages [15] -->
as classes to allow for the addition of the wide variety of parameters we are interested in

<!-- b000689 | contents | pages [15] -->
modeling. Simulations were run using the PyPy interpreter [14]

<!-- b000690 | contents | pages [15] -->
To start, we deﬁne a list of geographic regions, their population, area, regional Ebola

<!-- b000691 | contents | pages [15] -->
parameters, and the latitude and longitude of their centroids. For toy models, some of these

<!-- b000692 | contents | pages [15] -->
parameters (latitude/longitude) can be deﬁned arbitrarily, but the program treats toy data

<!-- b000693 | contents | pages [15] -->
and real data as equal, so scaling to real-world data is trivial. After deﬁning these regions,

<!-- b000694 | contents | pages [15] -->
we create a list of people, each of which is assigned a starting region and an initial state, being

<!-- b000695 | contents | pages [15] -->
healthy, latent-infected, or otherwise. This state can change by reassignment at any point

<!-- b000696 | contents | pages [15] -->
in the simulation. Lastly, hospitals with a ﬁxed number of beds are created and assigned to

<!-- b000697 | contents | pages [15] -->
their respective regions. Any relevant parameters are saved to a ﬁle before the simulation

<!-- b000698 | contents | pages [15] -->
continues.

<!-- b000699 | contents | pages [15] -->
Once all object creation is ﬁnished, the simulation begins. Once each timestep all of

<!-- b000700 | contents | pages [15] -->
the regional statistics are updated - things such as “total number of open beds” or “total

<!-- b000701 | contents | pages [15] -->
number of stage-1 infected individuals”. These values are often used to calculate some of the

<!-- b000702 | contents | pages [15] -->
many probabilities used to advance people from state to state or region to region. Once these

<!-- b000703 | contents | pages [15] -->
statistics are calculated, the program iterates over the list of people, checking their current

<!-- b000704 | contents | pages [15] -->
state, generating a random number (using the Mersenne Twister engine), and seeing if the

<!-- b000705 | contents | pages [15] -->
person will move from their current state to another allowed state using said random number

<!-- b000706 | contents | pages [15] -->
(the allowed states being deﬁned by the Ebola state-ﬂow network diagram). Each person can

<!-- b000707 | contents | pages [15] -->
also attempt to move to another region, with probabilities deﬁned by our modiﬁed gravity

<!-- b000708 | contents | pages [15] -->
mobility model.

<!-- b000709 | contents | pages [15] -->
This process of updating and iterating continues on for a predeﬁned number of timesteps,

<!-- b000710 | contents | pages [15] -->
with data being outout to a ﬁle after each timestep. This data was then analyzed and plotted

<!-- b000711 | contents | pages [15] -->
using the Numpy and MatplotLib Python libraries [15] [16].

<!-- b000712 | contents | pages [15] -->
2.5. Additional Considerations

<!-- b000713 | contents | pages [15] -->
2.5.1. Modeling of Hospitals

<!-- b000714 | contents | pages [15] -->
For the purposes of treatment distribution, the simulation considers three levels of medical

<!-- b000715 | contents | pages [15] -->
technology: basic, in which doctors and hospitals have no cure save those available today for

<!-- b000716 | contents | pages [15] -->
Ebola patients; vaccine available, in which susceptible and latent individuals will attempt

<!-- b000717 | contents | pages [15] -->
to obtain innoculations without a dependence on hospitals or doctors; and cure available,

<!-- b000718 | contents | pages [15] -->
in which doctors and hospitals can use a stock of medicine to cure infected individuals in

<!-- b000719 | contents | pages [15] -->
the early stage of the illness. These levels can be mixed and matched to simulate varying

<!-- b000720 | contents | pages [15] -->
treatment regimes.

<!-- b000721 | contents | pages [15] -->
Cures are modeled as an additional path for individuals to enter the cured state at a

<!-- b000722 | contents | pages [15] -->
higher probability governed by the eﬀectiveness of the cure. Cure eﬀectiveness is described

<!-- b000723 | contents | pages [15] -->
in terms of the average number of days needed for an individual taking doses of the cure to

<!-- b000724 | furniture | pages [16] -->
Team # 32722

<!-- b000725 | furniture | pages [16] -->
Page 16 of 37

<!-- b000726 | contents | pages [16] -->
become cured; that is, models which state the cure has an eﬀectiveness of “5” mean that the

<!-- b000727 | contents | pages [16] -->
cure being modeled will, on average, result in individuals supplied with the cure becoming

<!-- b000728 | contents | pages [16] -->
cured after ﬁve simulated days. This applies only to hospitalized individuals. Unfortunately,

<!-- b000729 | contents | pages [16] -->
this means that our model does not make the cure less eﬀective for late stage individuals,

<!-- b000730 | contents | pages [16] -->
which is an oversight of the model; an additional state for hospitalized late-stage individuals

<!-- b000731 | contents | pages [16] -->
could be added to compensate, but for now, we treat this as an assumption.

<!-- b000732 | contents | pages [16] -->
2.6. Consequences of Complexity

<!-- b000733 | contents | pages [16] -->
Our attempted attention to detail in the construction of this model has inadvertently re-

<!-- b000734 | contents | pages [16] -->
vealed a small portion of the enormous potential parameter space belying the Ebola epidemic.

<!-- b000735 | contents | pages [16] -->
Between the stochastic and regional layers, we have more than twenty possible parameters

<!-- b000736 | contents | pages [16] -->
that can be modiﬁed and which will have eﬀects on the results and dynamics of our model.

<!-- b000737 | contents | pages [16] -->
This is a double-edged sword; on one hand, we have many potential avenues through which

<!-- b000738 | contents | pages [16] -->
to tune and adjust our model, but on the other hand, we are heavily dependent on many

<!-- b000739 | contents | pages [16] -->
parameters that are not currently well known, such as the state transition probabilities in

<!-- b000740 | caption | pages [16] -->
Table 1.

<!-- b000741 | contents | pages [16] -->
This extreme dependency on a large number of parameters that are calculated from

<!-- b000742 | contents | pages [16] -->
largely inaccurate data presents a severe problem for our model as a source of quantitative

<!-- b000743 | contents | pages [16] -->
predictions for the eﬀectiveness of cure strategies. Instead, we feel that the strengths of our

<!-- b000744 | contents | pages [16] -->
model’s focus on inclusion of dynamic eﬀects from disparate sources lies not with numerical

<!-- b000745 | contents | pages [16] -->
results but with qualitative behaviors. It is neither feasible nor desirable for us to sweep over

<!-- b000746 | contents | pages [16] -->
all of our tunable parameters and all possible combinations of the parameters in an attempt

<!-- b000747 | contents | pages [16] -->
to ﬁt our model to existing data, as even with our large set of parameters we are aware of

<!-- b000748 | contents | pages [16] -->
the components of the outbreak we are not modeling.

<!-- b000749 | contents | pages [16] -->
The result of these complications is that we are not able to compare the results of sim-

<!-- b000750 | contents | pages [16] -->
ulations in which multiple diﬀerent parameters were varied in an apples-to-apples way. The

<!-- b000751 | contents | pages [16] -->
number of parameters that can be varied makes multivariable analysis using a complex model

<!-- b000752 | contents | pages [16] -->
(such as ours) an exceedingly diﬃcult, if not impossible task.

<!-- b000753 | contents | pages [16] -->
3. Sensitivity Analysis and Results

<!-- b000754 | contents | pages [16] -->
Epidemic modeling, especially in the case of highly dynamic illnesses like Ebola, is no-

<!-- b000755 | contents | pages [16] -->
torious for its dependence on initial conditions and minor variable diﬀerences. While our

<!-- b000756 | contents | pages [16] -->
model is signiﬁcantly more complex than simple diﬀerential equations models, the large num-

<!-- b000757 | contents | pages [16] -->
ber of variables and components within our model makes it extremely vulnerable to chaotic

<!-- b000758 | contents | pages [16] -->
disturbances arising from minor factors.

<!-- b000759 | contents | pages [16] -->
To better characterize the sensitivity of our model to the natural variations and errors

<!-- b000760 | contents | pages [16] -->
present in our initial conditions and simulated components, we have performed a large num-

<!-- b000761 | contents | pages [16] -->
ber of simulations on so-called toy models. These sensitivity tests are divided into eﬀects

<!-- b000762 | contents | pages [16] -->
expected from errors arising at the single-region level (including initial number of infected,

<!-- b000763 | contents | pages [16] -->
number of hospital beds, variation in virus compartment-change probabilities, etc.) and

<!-- b000764 | contents | pages [16] -->
those eﬀects expected from interaction between regions (including initial distribution of the

<!-- b000765 | contents | pages [16] -->
infected, inter-region variation of parameters, human and equipment mobility model parame-

<!-- b000766 | contents | pages [16] -->
ter variation, etc.). The method, results, and implications of these tests are given a thorough

<!-- b000767 | contents | pages [16] -->
treatment below.

<!-- b000768 | furniture | pages [17] -->
Team # 32722

<!-- b000769 | furniture | pages [17] -->
Page 17 of 37

<!-- b000770 | contents | pages [17] -->
3.0.1. Individual Region Tests

<!-- b000771 | contents | pages [17] -->
All tests in this section were run on a hypothetical version of Sierra Leone’s Kailahun

<!-- b000772 | contents | pages [17] -->
District. Our baseline has a population of 350,000 persons, and a latitude and longitude of

<!-- b000773 | contents | pages [17] -->
9.18S and -12.822 W respectively.

<!-- b000774 | contents | pages [17] -->
3.0.1.1. Initial Number of Infected. One major diﬃculty health authorities have struggled

<!-- b000775 | contents | pages [17] -->
with since the beginning of the outbreak is understanding the real number of cases out there.

<!-- b000776 | contents | pages [17] -->
Early on, the West African health care system did not have the infrastructure in place to deal

<!-- b000777 | contents | pages [17] -->
with the region’s endemic diseases, such as HIV and malaria; during the Ebola outbreak,

<!-- b000778 | contents | pages [17] -->
gathering statistics took a back seat to saving lives.

<!-- b000779 | contents | pages [17] -->
The result of this is that the number of reported cases in the region ﬂuctuates signiﬁcantly

<!-- b000780 | contents | pages [17] -->
as reports come in and are adjusted. There is currently no standard for estimating the true

<!-- b000781 | contents | pages [17] -->
number of infected from reported data, and the ratio of reported to total cases ﬂuctuates

<!-- b000782 | contents | pages [17] -->
dramatically [1]. Under-reporting from rural districts, which make up a majority of the West

<!-- b000783 | contents | pages [17] -->
African population and tend to have the least medical and statistical infrastructure, adds

<!-- b000784 | contents | pages [17] -->
an additional and highly non-linear potential for varying the number of cases.

<!-- b000785 | contents | pages [17] -->
(a) 5% latent

<!-- b000786 | contents | pages [17] -->
(b) 20% latent

<!-- b000787 | caption | pages [17] -->
Figure 5: The rate of change in infected cases and death with 5% and 20% of the initial population starting

<!-- b000788 | contents | pages [17] -->
in the latent state.

<!-- b000789 | contents | pages [17] -->
Understanding the impact of this extremely non-linear factor was accomplished by vary-

<!-- b000790 | contents | pages [17] -->
ing the initial number of cases within a single region. Increasing the percentage of individuals

<!-- b000791 | contents | pages [17] -->
in a district that start out infected appears to increase the magnitude of the initial spike of

<!-- b000792 | contents | pages [17] -->
cases and deaths, but in all tests the net behavior of the outbreak is similar; the infection

<!-- b000793 | contents | pages [17] -->
rate appears to drop over time, with the number of new deaths initially increasing signif-

<!-- b000794 | contents | pages [17] -->
icantly and then remaining higher than the number of new infections for the duration of

<!-- b000795 | contents | pages [17] -->
the simulation; if this trend continues, the virus will inevitably ﬂare out, as victims do not

<!-- b000796 | contents | pages [17] -->
spread the disease faster than they die oﬀ. The point at which the death rate exceeds the

<!-- b000797 | contents | pages [17] -->
new infection rate also appears to hold steadily at roughly 25 days independent of the initial

<!-- b000798 | contents | pages [17] -->
number of infected. The data does appear signiﬁcantly more sensitive to minute ﬂuctuations

<!-- b000799 | furniture | pages [18] -->
Team # 32722

<!-- b000800 | furniture | pages [18] -->
Page 18 of 37

<!-- b000801 | contents | pages [18] -->
at lower infection numbers; this relates to the size of the population being modeled and the

<!-- b000802 | contents | pages [18] -->
stochastic mechanism by which we model compartment transitions, and is expected. Overall,

<!-- b000803 | contents | pages [18] -->
the initial number of infected does not appear to have a substantial eﬀect on the qualitative

<!-- b000804 | contents | pages [18] -->
behavior of an individual city.

<!-- b000805 | contents | pages [18] -->
3.0.1.2. Hospital Bed Number. Outside of our model, there is no single cure or vaccine for

<!-- b000806 | contents | pages [18] -->
Ebola. Despite this, the medical community has shown that survival rates for Ebola can be

<!-- b000807 | contents | pages [18] -->
dramatically improved by providing supportive treatment for the disease—keeping patients

<!-- b000808 | contents | pages [18] -->
hygienic, hydrated, and isolated [17]. In addition, by isolating patients during treatment

<!-- b000809 | contents | pages [18] -->
(which typically coincides with highly infectious periods for the patient), hospitalization

<!-- b000810 | contents | pages [18] -->
further reduces the spread of the disease, which has many knock-on eﬀects for improving the

<!-- b000811 | contents | pages [18] -->
survival of the population as a whole.

<!-- b000812 | contents | pages [18] -->
Because of these factors, current aid eﬀorts have focused largely on the construction and

<!-- b000813 | contents | pages [18] -->
staﬃng of additional hospitals and treatment centers for Ebola. While the number of these

<!-- b000814 | contents | pages [18] -->
centers is relatively well known and public knowledge, it also changes frequently and rapidly:

<!-- b000815 | contents | pages [18] -->
prior to the outbreak, Liberia had only 0.8 hospital beds per thousand people to handle all

<!-- b000816 | contents | pages [18] -->
diseases in the nation; as of January 21, 2015, treatment centers are reporting a 2 to 1 ratio

<!-- b000817 | contents | pages [18] -->
of beds to reported cases, a dramatic improvement [18].

<!-- b000818 | contents | pages [18] -->
The importance and variation of the number of beds makes it a potentially decisive factor

<!-- b000819 | contents | pages [18] -->
within our simulation, as it directly aﬀects the number of individuals that can be hospitalized.

<!-- b000820 | contents | pages [18] -->
Hospitalized individuals present a highly non-linear component of our model; the probability

<!-- b000821 | contents | pages [18] -->
of an infected individual becoming hospitalized is governed not only by pure probability,

<!-- b000822 | contents | pages [18] -->
but also by the number of other individuals seeking hospitalization. This uncertainty is

<!-- b000823 | contents | pages [18] -->
compounded by the way our model handles infection chance; hospitalized individuals are

<!-- b000824 | contents | pages [18] -->
treated as quarantined, and are therefore unable to further spread their disease.

<!-- b000825 | contents | pages [18] -->
Analyzing this factor was accomplished by running our single-city simulation with several

<!-- b000826 | contents | pages [18] -->
diﬀerent bed multipliers, ranging from the initial number of beds—which is based oﬀof the

<!-- b000827 | contents | pages [18] -->
pre-outbreak per capita number of hospital beds and therefore the lower bound—to ten times

<!-- b000828 | contents | pages [18] -->
as many, comparable to that of a ﬁrst-world nation. The tests were run for the standard

<!-- b000829 | contents | pages [18] -->
population size of 350,000 and an initial latent fraction of ﬁve percent.

<!-- b000830 | contents | pages [18] -->
These graphs demonstrate the extreme importance of the number of hospitals in the

<!-- b000831 | contents | pages [18] -->
spread and development of the virus within our model. Although each case shows a passive

<!-- b000832 | contents | pages [18] -->
decline for Ebola, increasing the number of hospital beds—even by a linear scale—appears to

<!-- b000833 | contents | pages [18] -->
produce large results in the rate at which the outbreak diminishes. This has very important

<!-- b000834 | contents | pages [18] -->
implications for the results of our modeling endeavor, but the gist of it is that our model

<!-- b000835 | contents | pages [18] -->
is highly sensitive to variations in the number of beds, and activities such as construction

<!-- b000836 | contents | pages [18] -->
of new medical facilities will directly impact our results in a non-linear way; however, it is

<!-- b000837 | contents | pages [18] -->
reasonable to say that in all cases, increasing the amount of hospital beds improves outcomes

<!-- b000838 | contents | pages [18] -->
for the population in the model.

<!-- b000839 | contents | pages [18] -->
3.0.1.3. Population Scale. To test the behavior of our model when the total population size is

<!-- b000840 | contents | pages [18] -->
changed, we simulated one region with a baseline population with the same initial percentage

<!-- b000841 | contents | pages [18] -->
of the population as infected individuals, and varied both the size of the population and the

<!-- b000842 | contents | pages [18] -->
number of hospitals, scaling both down by a factor of ten from the actual scale.

<!-- b000843 | contents | pages [18] -->
The very clear dependence on the scale of the population/hospitals was surprising for

<!-- b000844 | contents | pages [18] -->
us to discover. Intuitively we could not understand it, as the hospital number is correct,

<!-- b000845 | furniture | pages [19] -->
Team # 32722

<!-- b000846 | furniture | pages [19] -->
Page 19 of 37

<!-- b000847 | contents | pages [19] -->
(a) ≈35, 000 people

<!-- b000848 | contents | pages [19] -->
(b) ≈350, 000 people

<!-- b000849 | caption | pages [19] -->
Figure 6: The total infection/hospitalization counts for a city of ≈35, 000 people (10x scale down) and a

<!-- b000850 | contents | pages [19] -->
city of ≈350, 000 people (actual scale).

<!-- b000851 | contents | pages [19] -->
and the rates of contact between individuals scale with the population size by deﬁnition.

<!-- b000852 | contents | pages [19] -->
We believe this strong dependence comes instead from parameters that govern hospital

<!-- b000853 | contents | pages [19] -->
dynamics, speciﬁcally the chance of an individual to seek medical attention, and the length

<!-- b000854 | contents | pages [19] -->
of their stay once accepted. These factors did not scale with population size or hospital

<!-- b000855 | contents | pages [19] -->
number, as the correct way of representing that dependency is not clear. This dependence is

<!-- b000856 | contents | pages [19] -->
clearly important, and would be interesting to study. Unfortunately due to computational

<!-- b000857 | contents | pages [19] -->
constraints, our simulations involving multiple cities/regions had to have the city size scaled

<!-- b000858 | contents | pages [19] -->
down so that the total global population was on the order of 1 million persons. This no doubt

<!-- b000859 | contents | pages [19] -->
has a poorly-deﬁned eﬀect on our results, though one could guess that overall hospitalization

<!-- b000860 | contents | pages [19] -->
rates would be higher in these scaled-down simulations.

<!-- b000861 | contents | pages [19] -->
3.0.1.4. Medicine Eﬃcacy. Our model attempts to determine the impact of a hypothetical

<!-- b000862 | contents | pages [19] -->
cure or vaccine for Ebola, a virus for which there is currently no such thing. This inherently

<!-- b000863 | contents | pages [19] -->
masochistic endeavor is heavily dependent upon the characteristics of such a cure or vaccine,

<!-- b000864 | contents | pages [19] -->
the most important of which is treatment/vaccine’s eﬀectiveness at curing/preventing the

<!-- b000865 | contents | pages [19] -->
disease. In the process of constructing the model, the eﬀect of an anti-Ebola cure is repre-

<!-- b000866 | contents | pages [19] -->
sented by an eﬃcacy factor that speeds the recovery rate of hospitalized individuals while

<!-- b000867 | contents | pages [19] -->
the region still has stockpiles of the cure available. Because our aims include a study of

<!-- b000868 | contents | pages [19] -->
how a cure should most eﬀectively be deployed, we expounded that it may be important to

<!-- b000869 | contents | pages [19] -->
see whether the eﬀectiveness of said cure impacts the simulation signiﬁcantly enough to be

<!-- b000870 | contents | pages [19] -->
considered when determining which distribution schemes to test.

<!-- b000871 | contents | pages [19] -->
A simulation of a single city was run with a set stockpile of medicine and 5 percent initial

<!-- b000872 | contents | pages [19] -->
infected. Medicine eﬃcacy multipliers were set at 2, 5 and 10, representing recovery times of

<!-- b000873 | contents | pages [19] -->
8 days, 3 days, and less than 1 day respectively. Speciﬁcally, these multipliers are applied to

<!-- b000874 | contents | pages [19] -->
the value of γR, the hospital recovery rate, in order to increase the chance of a hospitalized

<!-- b000875 | contents | pages [19] -->
person recovering.

<!-- b000876 | furniture | pages [20] -->
Team # 32722

<!-- b000877 | furniture | pages [20] -->
Page 20 of 37

<!-- b000878 | contents | pages [20] -->
(a) Medicine eﬃcacy of 2 (≈8 days)

<!-- b000879 | contents | pages [20] -->
(b) 5 ≈3 days)

<!-- b000880 | contents | pages [20] -->
(c) 10 ≈1 day)

<!-- b000881 | caption | pages [20] -->
Figure 7: The total infection/hospitalization counts for a city of ≈35, 000 people (10x scale down) and a

<!-- b000882 | contents | pages [20] -->
city of ≈350, 000 people (actual scale).

<!-- b000883 | contents | pages [20] -->
Visual inspection of the data makes it clear that introducing more eﬀective (i.e. faster)

<!-- b000884 | contents | pages [20] -->
cures will directly reduce the number of deaths and infections. It appears that the method

<!-- b000885 | contents | pages [20] -->
behind this action is two-fold—not only does the number of cured individuals increase with

<!-- b000886 | contents | pages [20] -->
eﬃcacy and the number of infected and dead decrease, but the number of persons hospitalized

<!-- b000887 | contents | pages [20] -->
also shows steady increases with increasing eﬃcacy. In our model, more eﬀective cures lessen

<!-- b000888 | contents | pages [20] -->
the duration that an infected individual will remain in a hospital. Shorter durations of stay

<!-- b000889 | contents | pages [20] -->
means that the hospital will have a higher throughput; because of the way we model eﬃcacy,

<!-- b000890 | contents | pages [20] -->
more eﬀective cures work not only because they reduce the chance of death during treatment

<!-- b000891 | contents | pages [20] -->
but also because they eﬀectively increase the capacity of hospitals.

<!-- b000892 | contents | pages [20] -->
3.0.2. Vaccine Quantity and Frequency of Shipments

<!-- b000893 | contents | pages [20] -->
Vaccines have a long and established history of eradicating disease, but are not always

<!-- b000894 | contents | pages [20] -->
100% eﬀective. In this case, we once again run into the issue of dealing with a hypothetical

<!-- b000895 | furniture | pages [21] -->
Team # 32722

<!-- b000896 | furniture | pages [21] -->
Page 21 of 37

<!-- b000897 | contents | pages [21] -->
vaccine with no deﬁned characteristics. We have already made the assumption that the

<!-- b000898 | contents | pages [21] -->
vaccine is perfectly eﬀective, i.e.

<!-- b000899 | contents | pages [21] -->
every susceptible individual given a dose of it will be

<!-- b000900 | contents | pages [21] -->
unable to be infected. In real life, this will most certainly not be the case, and our model

<!-- b000901 | contents | pages [21] -->
will under-predict the number of doses needed to introduce herd immunity and halt the virus.

<!-- b000902 | contents | pages [21] -->
At the same time, this perfect vaccine needs to be produced and shipped to the areas that

<!-- b000903 | contents | pages [21] -->
need it, a highly non-trivial process that is again complicated by Ebola’s highly infectious

<!-- b000904 | contents | pages [21] -->
nature (making the manufacturing processes behind a potential vaccine more rigorous and

<!-- b000905 | contents | pages [21] -->
safety focused) and the region’s limited transportation infrastructure.

<!-- b000906 | contents | pages [21] -->
To test our model’s response to wildly varying values for the quantity of vaccine deployed,

<!-- b000907 | contents | pages [21] -->
we ran the simulation with speciﬁed delivery quantities with a frequency of one delivery per

<!-- b000908 | contents | pages [21] -->
ﬁve days.

<!-- b000909 | contents | pages [21] -->
(a) 100 vaccines added every 5 days

<!-- b000910 | contents | pages [21] -->
(b) 1000 vaccines every 5 days

<!-- b000911 | contents | pages [21] -->
(c) 10000 vaccines every 5 days

<!-- b000912 | contents | pages [21] -->
(d) 20000 vaccines every 5 days

<!-- b000913 | caption | pages [21] -->
Figure 8: Total infection rate with changes in amount of vaccine distributed to a single city.

<!-- b000914 | contents | pages [21] -->
Our single-region results show that low quantities of vaccine actually do very little to slow

<!-- b000915 | contents | pages [21] -->
the outbreak, as the number of persons vaccinated is small when compared to the number of

<!-- b000916 | contents | pages [21] -->
new infections. However, when a large number of individuals can be vaccinated—more than

<!-- b000917 | contents | pages [21] -->
are infected every day—the vaccine tends to slow the spread of infection and therefore the

<!-- b000918 | contents | pages [21] -->
number of deaths. While we estimate the number of doses that could be produced per week

<!-- b000919 | contents | pages [21] -->
from manufacturing data on other vaccines, this result does have important implications for

<!-- b000920 | furniture | pages [22] -->
Team # 32722

<!-- b000921 | furniture | pages [22] -->
Page 22 of 37

<!-- b000922 | contents | pages [22] -->
the distribution of vaccinations: namely, that it may not be worthwhile to send vaccines into

<!-- b000923 | contents | pages [22] -->
a region where it is know that the rate of new infections will exceed the rate of vaccination.

<!-- b000924 | contents | pages [22] -->
Stated concisely, vaccines are only eﬀective when the rate at which they can be manufactured

<!-- b000925 | contents | pages [22] -->
and deployed is higher than the rate at which new individuals are infected. This is often the

<!-- b000926 | contents | pages [22] -->
case for regions surrounding a region undergoing a large outbreak; vaccinating these areas

<!-- b000927 | contents | pages [22] -->
may prove eﬀective at slowing the outward spread of the disease, which agrees with our

<!-- b000928 | contents | pages [22] -->
intuition.

<!-- b000929 | contents | pages [22] -->
3.0.3. Multiple-Region Simulations

<!-- b000930 | contents | pages [22] -->
Usage of multi-layer node models allows for the modeling of behaviors at varying scales

<!-- b000931 | contents | pages [22] -->
and levels of complexity, but also introduces the potential for highly chaotic and non-linear

<!-- b000932 | contents | pages [22] -->
behavior. With the behavior of each individual node now fairly well understood, we sought

<!-- b000933 | contents | pages [22] -->
to understand how the assumptions we made in modeling the connections and interactions

<!-- b000934 | contents | pages [22] -->
between regions comes into play.

<!-- b000935 | contents | pages [22] -->
Due to the extreme complexity intrinsic to modeling an entire geopolitical region of the

<!-- b000936 | contents | pages [22] -->
world, we used our four-city toy model to develop qualitative insights from our model before

<!-- b000937 | contents | pages [22] -->
attempting to tackle a large-scale simulation of the region.

<!-- b000938 | contents | pages [22] -->
City

<!-- b000939 | contents | pages [22] -->
Population

<!-- b000940 | contents | pages [22] -->
Latitude and Longitude

<!-- b000941 | contents | pages [22] -->
A

<!-- b000942 | contents | pages [22] -->
350,000

<!-- b000943 | contents | pages [22] -->
9.17N, -12.82E

<!-- b000944 | contents | pages [22] -->
B

<!-- b000945 | contents | pages [22] -->
500,000

<!-- b000946 | contents | pages [22] -->
9.31N , -12.16E

<!-- b000947 | contents | pages [22] -->
C

<!-- b000948 | contents | pages [22] -->
335,000

<!-- b000949 | contents | pages [22] -->
9.72N, -12.75E

<!-- b000950 | contents | pages [22] -->
D

<!-- b000951 | contents | pages [22] -->
400,000

<!-- b000952 | contents | pages [22] -->
9.65N, -11.68E

<!-- b000953 | contents | pages [22] -->
Initial Percent Infected (Latent)

<!-- b000954 | contents | pages [22] -->
Parameter Set

<!-- b000955 | contents | pages [22] -->
10%

<!-- b000956 | contents | pages [22] -->
Liberia

<!-- b000957 | contents | pages [22] -->
10%

<!-- b000958 | contents | pages [22] -->
Liberia

<!-- b000959 | contents | pages [22] -->
10%

<!-- b000960 | contents | pages [22] -->
Liberia

<!-- b000961 | contents | pages [22] -->
10%

<!-- b000962 | contents | pages [22] -->
Liberia

<!-- b000963 | caption | pages [22] -->
Table 3: Toy model cities, initial conditions, and parameter sets

<!-- b000964 | contents | pages [22] -->
3.0.4. Vaccine Distribution

<!-- b000965 | contents | pages [22] -->
Firstly, a simulation of the possible methods of distributing a vaccine was performed.

<!-- b000966 | contents | pages [22] -->
Four scenarios were devised:

<!-- b000967 | contents | pages [22] -->
1. Rural infection distribution, focus vaccine distribution to urban centers

<!-- b000968 | contents | pages [22] -->
2. Rural infection distribution, focus vaccine distribution to rural districts

<!-- b000969 | contents | pages [22] -->
3. Urban infection distribution, focus vaccine distribution to urban centers

<!-- b000970 | contents | pages [22] -->
4. Urban infection distribution, focus vaccine distribution to rural districts

<!-- b000971 | furniture | pages [23] -->
Team # 32722

<!-- b000972 | contents | pages [23] -->
(a) Rural regions infected,

<!-- b000973 | contents | pages [23] -->
vaccines dis-

<!-- b000974 | contents | pages [23] -->
tributed to rural regions

<!-- b000975 | contents | pages [23] -->
(c) Urban regions infected, vaccines dis-

<!-- b000976 | contents | pages [23] -->
tributed to urban regions

<!-- b000977 | furniture | pages [23] -->
Page 23 of 37

<!-- b000978 | contents | pages [23] -->
(b) Rural regions infected,

<!-- b000979 | contents | pages [23] -->
vaccines dis-

<!-- b000980 | contents | pages [23] -->
tributed to urban regions

<!-- b000981 | contents | pages [23] -->
(d) Urban regions infected, vaccines dis-

<!-- b000982 | contents | pages [23] -->
tributed to rural regions

<!-- b000983 | caption | pages [23] -->
Figure 9: Changes in infection count with diﬀerences in vaccine distribution.

<!-- b000984 | contents | pages [23] -->
Interestingly, the two urban distribution cases and the two rural distribution cases show

<!-- b000985 | contents | pages [23] -->
opposite results; vaccinating city dwellers during a primarily rural infection appears to

<!-- b000986 | contents | pages [23] -->
slightly reduce the total number of deaths and infections, while focusing the vaccination

<!-- b000987 | contents | pages [23] -->
eﬀort on rural areas during a largely urban outbreak tends to slightly increase the number

<!-- b000988 | contents | pages [23] -->
of infections and deaths.

<!-- b000989 | contents | pages [23] -->
Discounting the implicit assumptions behind the vaccination characteristics we have cho-

<!-- b000990 | contents | pages [23] -->
sen, we can infer a number of trends from this population data. Rural outbreaks – which

<!-- b000991 | contents | pages [23] -->
are assumed to be small due to the low population density in these regions – do tend to

<!-- b000992 | contents | pages [23] -->
move towards urban centers, making vaccinating urban centers during the early stages of an

<!-- b000993 | contents | pages [23] -->
outbreak very eﬀective while it is still largely contained in rural regions. Urban outbreaks,

<!-- b000994 | contents | pages [23] -->
on the other hand, tend to be large but do not spread as readily to rural areas. The high

<!-- b000995 | contents | pages [23] -->
rate of growth of these outbreaks means that vaccination during the middle of a large, urban

<!-- b000996 | contents | pages [23] -->
outbreak does not appear to have a signiﬁcant impact on the number of infections or deaths.

<!-- b000997 | contents | pages [23] -->
However, as shown in our sensitivity analysis, vaccination campaigns in large cities with

<!-- b000998 | contents | pages [23] -->
outbreaks can be successful if it is possible to ﬂood the city with vaccinations faster than

<!-- b000999 | contents | pages [23] -->
the disease will spread (i.e. vaccinations must outpace new infections).

<!-- b001000 | furniture | pages [24] -->
Team # 32722

<!-- b001001 | furniture | pages [24] -->
Page 24 of 37

<!-- b001002 | contents | pages [24] -->
However, it is important to remember that our human mobility model is gravity-based,

<!-- b001003 | contents | pages [24] -->
with large urban centers tending to draw in more individuals than rural ones in order to

<!-- b001004 | contents | pages [24] -->
represent them as hubs of travel and commerce. This simple model is likely to blame for

<!-- b001005 | contents | pages [24] -->
some of the diﬀerence in results between the two scenarios; while rural cases will readily

<!-- b001006 | contents | pages [24] -->
move into the urban nodes, urban cases do not return the favor, leading to a bias towards

<!-- b001007 | contents | pages [24] -->
urban cases. Whether this accurately describes human behavior is discussed in Appendix

<!-- b001008 | contents | pages [24] -->
A.

<!-- b001009 | contents | pages [24] -->
Qualitatively, we can say that this simulation reinforces our previously discussed notion

<!-- b001010 | contents | pages [24] -->
of the role of vaccines during very large outbreaks.

<!-- b001011 | contents | pages [24] -->
When it is possible to manufacture

<!-- b001012 | contents | pages [24] -->
and distribute doses of the vaccine faster than the outbreak spreads, vaccination campaigns

<!-- b001013 | contents | pages [24] -->
reduce the number of infections and deaths. Otherwise, the campaigns—while having some

<!-- b001014 | contents | pages [24] -->
impact—do not appear to signiﬁcantly impact the health outcomes for the region.

<!-- b001015 | contents | pages [24] -->
3.0.5. Cure Distribution

<!-- b001016 | contents | pages [24] -->
Following from the ﬁndings in the vaccine distribution case, a similar set of tests was run

<!-- b001017 | contents | pages [24] -->
with doses of the cure4:

<!-- b001018 | contents | pages [24] -->
1. Rural infection distribution, focus cure distribution to rural districts

<!-- b001019 | contents | pages [24] -->
2. Rural infection distribution, focus cure distribution to urban centers

<!-- b001020 | contents | pages [24] -->
3. Urban infection distribution, focus cure distribution to urban centers

<!-- b001021 | contents | pages [24] -->
4. Urban infection distribution, focus cure distribution to rural districts

<!-- b001022 | contents | pages [24] -->
4We do not show results of our tests concerning the eﬀect of increasing medicine quantities, as hospitals

<!-- b001023 | contents | pages [24] -->
were shown to be the limiting factor in that case by a very large margin.

<!-- b001024 | furniture | pages [25] -->
Team # 32722

<!-- b001025 | contents | pages [25] -->
(a) Rural regions infected, medicine dis-

<!-- b001026 | contents | pages [25] -->
tributed to rural regions

<!-- b001027 | contents | pages [25] -->
(c) Urban regions infected, medicine dis-

<!-- b001028 | contents | pages [25] -->
tributed to urban regions

<!-- b001029 | furniture | pages [25] -->
Page 25 of 37

<!-- b001030 | contents | pages [25] -->
(b) Rural regions infected, medicine dis-

<!-- b001031 | contents | pages [25] -->
tributed to urban regions

<!-- b001032 | contents | pages [25] -->
(d) Urban regions infected, medicine dis-

<!-- b001033 | contents | pages [25] -->
tributed to rural regions

<!-- b001034 | caption | pages [25] -->
Figure 10: Total infection count with diﬀerences in medicine distribution.

<!-- b001035 | contents | pages [25] -->
In all of the scenarios, it appears that distributing doses of the cure to the regions

<!-- b001036 | contents | pages [25] -->
most heavily aﬄicted by the illness is the most eﬀective at reducing the number of deaths

<!-- b001037 | contents | pages [25] -->
and infections. This is highly intuitive—curing individuals with Ebola both prevents them

<!-- b001038 | contents | pages [25] -->
from spreading the illness and allows them to leave the hospitals, freeing up that room for

<!-- b001039 | contents | pages [25] -->
additional patients. This allows further patients to be admitted, isolating them to prevent

<!-- b001040 | contents | pages [25] -->
further spread and steadily slowing the cycle of infections.

<!-- b001041 | contents | pages [25] -->
These scenarios do not appear to be heavily impacted by our transportation model, likely

<!-- b001042 | contents | pages [25] -->
owing to the more straightforward mode of action by which supplying the cure defeats the

<!-- b001043 | contents | pages [25] -->
outbreak. Curing individuals in rural regions prevents them from spreading the illness to

<!-- b001044 | contents | pages [25] -->
the urban region; curing individuals in the urban region prevents further spread to either

<!-- b001045 | contents | pages [25] -->
region.

<!-- b001046 | contents | pages [25] -->
However, we do have a constant number of hospital beds in each region, which is deﬁned in

<!-- b001047 | contents | pages [25] -->
relation to data on the total number of beds in the country as a whole. This assumption is not

<!-- b001048 | contents | pages [25] -->
valid, as there is little doubt that most hospitals lie in large urban centers. In order for these

<!-- b001049 | contents | pages [25] -->
results to be more valid, hospitals or treatment centers capable of eﬀectively distributing

<!-- b001050 | contents | pages [25] -->
medicine to those in need would need to be set up in rural settings. How the system will

<!-- b001051 | furniture | pages [26] -->
Team # 32722

<!-- b001052 | furniture | pages [26] -->
Page 26 of 37

<!-- b001053 | contents | pages [26] -->
behave without this condition was not studied, but would be very interesting.

<!-- b001054 | contents | pages [26] -->
3.0.5.1. Initial Distribution of Infected. As mentioned previously, the health care response in

<!-- b001055 | contents | pages [26] -->
this outbreak has suﬀered tremendously in the face of inadequate statistical data, especially

<!-- b001056 | contents | pages [26] -->
in rural areas. Similar to the single-region test of the number of initial infected, we sought to

<!-- b001057 | contents | pages [26] -->
identify the behavioral changes stemming from varying distributions of the initial population

<!-- b001058 | contents | pages [26] -->
of infected individuals.

<!-- b001059 | contents | pages [26] -->
For any given n regions and k initial distributions of infected persons, there exist a very

<!-- b001060 | contents | pages [26] -->
large number of potential distributions that can be tested. Rather than gaze into that abyss

<!-- b001061 | contents | pages [26] -->
of a parameter space, we looked at three simple initial conﬁgurations; mostly rural infections,

<!-- b001062 | contents | pages [26] -->
mostly urban infections, and an even mix of both urban and rural.

<!-- b001063 | contents | pages [26] -->
3.0.5.2. Movement Parameter Variation. Like the rest of the statistical data from West

<!-- b001064 | contents | pages [26] -->
Africa, information on the motion and mobility of people remains scattered at best and has

<!-- b001065 | contents | pages [26] -->
been a major sticking point for models of this outbreak. Our model, which uses a small set

<!-- b001066 | contents | pages [26] -->
of empirical data from mobile phones, is vulnerable to both over- and under-estimation of

<!-- b001067 | contents | pages [26] -->
the number of persons that migrate around the region [13].

<!-- b001068 | contents | pages [26] -->
Evaluating the eﬀect of larger or smaller quantities of moving persons was accomplished

<!-- b001069 | contents | pages [26] -->
by varying a so-called chance factor, k, that multiplies the probability that an individual

<!-- b001070 | contents | pages [26] -->
will chose to move between cities. We tested the multi-region simulation at chance factors

<!-- b001071 | contents | pages [26] -->
of k =1, and 5, where 1 represents a higher transportation rate than 5 (essentially the

<!-- b001072 | contents | pages [26] -->
probability of moving is divided by k).

<!-- b001073 | contents | pages [26] -->
(a) Movement factor k = 1, higher movement

<!-- b001074 | contents | pages [26] -->
(b) Movement factor k = 5, lower movement

<!-- b001075 | contents | pages [26] -->
rate

<!-- b001076 | contents | pages [26] -->
rate

<!-- b001077 | caption | pages [26] -->
Figure 11: Changes in infection count with varying movement factos.

<!-- b001078 | contents | pages [26] -->
The results of this simulation show surprisingly little dependence on the rate at which

<!-- b001079 | contents | pages [26] -->
people migrate. The end quantities of cure used, number of infected, and number of dead tend

<!-- b001080 | contents | pages [26] -->
to increase with increasing mobility, but remain within roughly ten percent of one another;

<!-- b001081 | contents | pages [26] -->
more importantly, the overall behavior of the simulation appears unchanged. This remains

<!-- b001082 | contents | pages [26] -->
only somewhat reassuring—the aﬀect of individual migration scales non-linearly with the

<!-- b001083 | contents | pages [26] -->
number of cities and their population, and so the eﬀect of variations in this parameter will

<!-- b001084 | furniture | pages [27] -->
Team # 32722

<!-- b001085 | furniture | pages [27] -->
Page 27 of 37

<!-- b001086 | contents | pages [27] -->
likely become more apparent at very large scales. This implicit issue is discussed further in

<!-- b001087 | contents | pages [27] -->
Appendix A.

<!-- b001088 | contents | pages [27] -->
3.0.5.3. Inter-Regional Parameter Variation. The parameters governing the characteristics

<!-- b001089 | contents | pages [27] -->
of Ebola vary from country to country. We study this behaviour by setting the parameters

<!-- b001090 | contents | pages [27] -->
for each city to diﬀerent sets of values, i.e. one simulation where all of the cities are “in”

<!-- b001091 | contents | pages [27] -->
Libera, one where they are all in Sierra Leone, and one where they are mixed.

<!-- b001092 | contents | pages [27] -->
(a) All cities in Liberia

<!-- b001093 | contents | pages [27] -->
(b) All cities in Sierra Leone

<!-- b001094 | contents | pages [27] -->
(c) 2 cities in Liberia, 2 cities in Sierra Leone

<!-- b001095 | caption | pages [27] -->
Figure 12: The total infection counts for a 4 city system, with various region-speciﬁc Ebola parameters

<!-- b001096 | contents | pages [27] -->
chosen.

<!-- b001097 | contents | pages [27] -->
Our simulation shows a high dependence on the local parameter sets of a region, cf.

<!-- b001098 | caption | pages [27] -->
Table 1. This is evident in the data as well when identifying the number of cases, deaths,

<!-- b001099 | contents | pages [27] -->
and primary vectors of the spread for Guinea, Liberia, and Sierra Leone [1]. Unfortunately,

<!-- b001100 | contents | pages [27] -->
the values of the parameters vary in the literature and Guinea completely lacks enough data

<!-- b001101 | contents | pages [27] -->
to compile an appropriate parameter set. These results do eﬀectively rule out the possibility

<!-- b001102 | furniture | pages [28] -->
Team # 32722

<!-- b001103 | furniture | pages [28] -->
Page 28 of 37

<!-- b001104 | contents | pages [28] -->
of generalizing “West Africa” into one region for the purposes of modelling, as Ebola spreads

<!-- b001105 | contents | pages [28] -->
very diﬀerently in diﬀerent regions, and these eﬀects do not “even out”. Furthermore, a

<!-- b001106 | contents | pages [28] -->
limitation of our approach is claiming that the parameter sets do not change within any

<!-- b001107 | contents | pages [28] -->
given region - an assumption that is likely unjustiﬁed, but hard to get around without

<!-- b001108 | contents | pages [28] -->
extraordinarily better data on this region.

<!-- b001109 | contents | pages [28] -->
3.1. Further Sensitivities and Limitations

<!-- b001110 | contents | pages [28] -->
In addition to the model sensitivities that we were able to easily study, we identiﬁed

<!-- b001111 | contents | pages [28] -->
many other potential sensitivities and limitations of our model arising from the assumptions

<!-- b001112 | contents | pages [28] -->
listed in Appendix A. To provide a better portrait of our model before discussing any formal

<!-- b001113 | contents | pages [28] -->
results of our modeled scenarios, these further limitations are discussed here.

<!-- b001114 | contents | pages [28] -->
3.1.1. Weather Dynamics

<!-- b001115 | contents | pages [28] -->
Seasonal changes aside, there is no support in the literature for local weather directly

<!-- b001116 | contents | pages [28] -->
aﬀecting the transmission of the disease. The primary sensitivity would be during the of

<!-- b001117 | contents | pages [28] -->
the wet season from May to October, as many remote areas will no longer be accessible.

<!-- b001118 | contents | pages [28] -->
The most eﬀective way to represent these regions in our model would be to represent their

<!-- b001119 | contents | pages [28] -->
connections to other regions as time-varying—we chose to simply ignore them for the pur-

<!-- b001120 | contents | pages [28] -->
poses of our study. As this is the ﬁrst Ebola outbreak of such magnitude, data on eﬀective

<!-- b001121 | contents | pages [28] -->
transportation measures for such a large amount of aid during the wet season is absent and

<!-- b001122 | contents | pages [28] -->
diﬃcult to postulate. Typical vehicles would likely not be useable, and air-drops may be

<!-- b001123 | contents | pages [28] -->
more appropriate, though more costly.

<!-- b001124 | contents | pages [28] -->
This aside, the climate of West Africa remains constant for the most part throughout

<!-- b001125 | contents | pages [28] -->
the year and does not experiece any wide ﬂuctuations in temperature. While a local climate

<!-- b001126 | contents | pages [28] -->
may have an eﬀect on the outbreak, it is not considered in our current study of West Africa.

<!-- b001127 | contents | pages [28] -->
3.1.2. Burial

<!-- b001128 | contents | pages [28] -->
The literature almost unanimously agrees on the predominance of proper body disposal.

<!-- b001129 | contents | pages [28] -->
One of the initial surges of Ebola in Guinea originated at a single funeral in which over 300

<!-- b001130 | contents | pages [28] -->
individuals became infected. Guinea still reports almost 60% of its cases related to funeral

<!-- b001131 | contents | pages [28] -->
practices [19]. Even now that the outbreak is well known among the population, the most

<!-- b001132 | contents | pages [28] -->
recent WHO Ebola Situation Report has documented 35 unsafe burials for Guinea and 11

<!-- b001133 | contents | pages [28] -->
unsafe burials for Sierra Leone [1]. One could potentially model this burial behavior with

<!-- b001134 | contents | pages [28] -->
“bursts” of new infections at various points in time, but whether or not this is more or less

<!-- b001135 | contents | pages [28] -->
accurate is not clear.

<!-- b001136 | contents | pages [28] -->
4. Conclusion

<!-- b001137 | contents | pages [28] -->
4.1. Future Epidemic Trajectories

<!-- b001138 | contents | pages [28] -->
An interesting and unexpected result of all of our models is that, in every case we looked

<!-- b001139 | contents | pages [28] -->
at, the Ebola outbreak always displayed self-limiting behavior.

<!-- b001140 | contents | pages [28] -->
Indeed, a deﬁning char-

<!-- b001141 | contents | pages [28] -->
acteristic of our simulations is that the total number of infected appears to grow either

<!-- b001142 | contents | pages [28] -->
logarithmically or as a decaying exponential up to a point, after which growth stops and the

<!-- b001143 | contents | pages [28] -->
outbreak ends.

<!-- b001144 | furniture | pages [29] -->
Team # 32722

<!-- b001145 | furniture | pages [29] -->
Page 29 of 37

<!-- b001146 | contents | pages [29] -->
In addition to the reassuring nature of this ﬁnding, it is consistent with both recent

<!-- b001147 | contents | pages [29] -->
WHO situation reports [1] and the indication of previous outbreaks. Currently, the WHO is

<!-- b001148 | contents | pages [29] -->
reporting that the number of new outbreaks being reported in Guinea, Liberia, and Sierra

<!-- b001149 | contents | pages [29] -->
Leone is decreasing steadily, similar to the behavior predicted by our model. Prior outbreaks

<!-- b001150 | contents | pages [29] -->
have also universally shown self-limiting behavior over their relatively brief durations, and

<!-- b001151 | contents | pages [29] -->
this behavior is highly characteristic of Ebola and other diseases with high mortality rates.

<!-- b001152 | contents | pages [29] -->
Ultimately, this demonstrated behavior lends credence to the behavioral accuracy of our

<!-- b001153 | contents | pages [29] -->
model and allows us to focus our advice on optimizing the usage of a hypothetical cure or

<!-- b001154 | contents | pages [29] -->
vaccine to bring an end to the illness, rather than simply controlling it.

<!-- b001155 | contents | pages [29] -->
4.2. Summary and Recommendations

<!-- b001156 | contents | pages [29] -->
We have developed a multi-layer, stochasic, state-based model that allows for the incor-

<!-- b001157 | contents | pages [29] -->
poration of real world data into the modeling of the Ebola outbreak and the impact of a

<!-- b001158 | contents | pages [29] -->
potential cure. As shown by our simulations, our model demonstrates behavioral stability

<!-- b001159 | contents | pages [29] -->
and predicts baseline results that are consistent with the predictions of major world health

<!-- b001160 | contents | pages [29] -->
organizations. We have also shown that it provides an extensible framework for the modeling

<!-- b001161 | contents | pages [29] -->
of various kinds of treatment for the cure and prevention of Ebola, including the modeling

<!-- b001162 | contents | pages [29] -->
of implications of diﬀerent distribution strategies for said treatments. In addition, we have

<!-- b001163 | contents | pages [29] -->
performed an introductory analysis of the sensitivity of our model to parameters that we

<!-- b001164 | contents | pages [29] -->
believe are critically important to the behavior of the system, providing future users with

<!-- b001165 | contents | pages [29] -->
some indication of how changes to parameters with physical signiﬁcance (such as the initial

<!-- b001166 | contents | pages [29] -->
number of infected and availability of hospital beds) will aﬀect the predictions of our model.

<!-- b001167 | contents | pages [29] -->
Our sensitivity analysis, when coupled with the actual results of our simulation, provides

<!-- b001168 | contents | pages [29] -->
valuable insight into the qualitative dynamics of the outbreak.

<!-- b001169 | contents | pages [29] -->
Our multi-layer modeling approach does appear to have several merits with regards types

<!-- b001170 | contents | pages [29] -->
of behavioral parameters it incorporates. First and foremost, our model has shown itself to

<!-- b001171 | contents | pages [29] -->
be highly adaptable, supporting a variety of potential geographic and geopolitical scenarios

<!-- b001172 | contents | pages [29] -->
through modiﬁcation of the region layer. This level of modeling allows analysts to perform

<!-- b001173 | contents | pages [29] -->
what-if simulations on the impact of various transportation and infrastructure changes in the

<!-- b001174 | contents | pages [29] -->
region, such as the construction of roads or how transportation logistics will change during

<!-- b001175 | contents | pages [29] -->
the wet season. This ability is doubly important due to the upcoming wet season in the

<!-- b001176 | contents | pages [29] -->
region, in which many rural areas become yet more isolated when the roads linking them to

<!-- b001177 | contents | pages [29] -->
the rest of the region are cut oﬀ.

<!-- b001178 | contents | pages [29] -->
In addition, the stochastic state modeling approach used to model individual agents

<!-- b001179 | contents | pages [29] -->
within the simulation has shown itself to be a ﬂexible method of incorporating the complex

<!-- b001180 | contents | pages [29] -->
and characteristic nature of both the Ebola virus and the region at large into the simulation.

<!-- b001181 | contents | pages [29] -->
The set of probabilities that govern transitions between states can be modiﬁed and tuned as

<!-- b001182 | contents | pages [29] -->
new data on the outbreak becomes available, and allows for the incorporation of individual

<!-- b001183 | contents | pages [29] -->
“willingness” or “preference” into the simulation.

<!-- b001184 | contents | pages [29] -->
However, we are acutely aware of our model’s extreme dependence on a large parameter

<!-- b001185 | contents | pages [29] -->
set that is itself dependent on information from the real-world that is unreliable and incom-

<!-- b001186 | contents | pages [29] -->
plete. Upon attempting to gather relevant statistics on the outbreak, we found that the

<!-- b001187 | contents | pages [29] -->
majority of available information was either not up to date, did not exist, or described itself

<!-- b001188 | contents | pages [29] -->
as inaccurate and approximate. Because of this, we conclude that it is neither possible nor

<!-- b001189 | furniture | pages [30] -->
Team # 32722

<!-- b001190 | furniture | pages [30] -->
Page 30 of 37

<!-- b001191 | contents | pages [30] -->
reasonable to draw quantitative conclusions from models that attempt to capture as much

<!-- b001192 | contents | pages [30] -->
behavior as ours.

<!-- b001193 | contents | pages [30] -->
4.2.1. The Art of Eradicating Ebola

<!-- b001194 | contents | pages [30] -->
Should a cure or vaccine for Ebola ever materialize, early results from our model—while

<!-- b001195 | contents | pages [30] -->
not deﬁnitive—shed some light on how such treatments would be best utilized. However, if

<!-- b001196 | contents | pages [30] -->
there is one thing developing this model has taught us, it is that making predictions for this

<!-- b001197 | contents | pages [30] -->
region of the world is more of an art than a science. This section aims to present a coherent set

<!-- b001198 | contents | pages [30] -->
of guidelines from our model’s preliminary, qualitative results to aid organizations intending

<!-- b001199 | contents | pages [30] -->
to deploy a cure or otherwise ﬁght the Ebola outbreak.

<!-- b001200 | contents | pages [30] -->
The “Zeroeth Law” of this strategem (one that we ourselves overlooked before attempting

<!-- b001201 | contents | pages [30] -->
this problem) is to mind always the extreme complexity and delicacy of the entire outbreak

<!-- b001202 | contents | pages [30] -->
system. The results of seemingly innocent modiﬁcations to parameters can have unexpect-

<!-- b001203 | contents | pages [30] -->
edly dramatic results. Additionally, the history of the present outbreak shows that funda-

<!-- b001204 | contents | pages [30] -->
mental and important parameters, such as the rate at which the virus can be transmitted,

<!-- b001205 | contents | pages [30] -->
can vary wildly based on factors that may not be immediately observable or predictable.

<!-- b001206 | contents | pages [30] -->
With this in mind, one should acknowledge that there are no hard and fast rules in the

<!-- b001207 | contents | pages [30] -->
realm of epidemic modeling, and least so when ﬁghting Ebola in West Africa.

<!-- b001208 | contents | pages [30] -->
First and foremost, it is apparent from our simulations that the existence or development

<!-- b001209 | contents | pages [30] -->
of a cure or vaccine does not preclude the continued development of medical infrastructure

<!-- b001210 | contents | pages [30] -->
within the region. Hospitals and treatment wards allow highly contagious Ebola patients to

<!-- b001211 | contents | pages [30] -->
be isolated, preventing further spread of the disease through quarantine. In our scenario,

<!-- b001212 | contents | pages [30] -->
such infrastructure is also a requirement to distribute a treatment that will cure individuals

<!-- b001213 | contents | pages [30] -->
already infected with Ebola, so halting investments in hospitals to fund cure or vaccine

<!-- b001214 | contents | pages [30] -->
research is likely poor practice. (Medical infrastructure will also help deal with the huge

<!-- b001215 | contents | pages [30] -->
number of other medical problems the region will face after dealing with this outbreak, but

<!-- b001216 | contents | pages [30] -->
that is a tangential beneﬁt from our perspective).

<!-- b001217 | contents | pages [30] -->
With regards to the distribution of medication, it is important to note the diﬀerence

<!-- b001218 | contents | pages [30] -->
between preventative medications (i.e. vaccines) and curative ones. Vaccination is a powerful

<!-- b001219 | contents | pages [30] -->
tool for preventing the spread of an epidemic, but due to herd immunity eﬀects, works best

<!-- b001220 | contents | pages [30] -->
when implemented on a scale that outpaces the rate of infection. Cures, on the other hand,

<!-- b001221 | contents | pages [30] -->
act in a more linear manner; each dose of a curative medicine supplied to a region will

<!-- b001222 | contents | pages [30] -->
increase the number of individuals in that region that survive. The type of treatment is

<!-- b001223 | contents | pages [30] -->
therefore fundamental to the strategy one employs to combat the virus.

<!-- b001224 | contents | pages [30] -->
As previously described, vaccines are most eﬀective when used in regions with few to no

<!-- b001225 | contents | pages [30] -->
cases of the virus. Inoculating these regions will prevent the spread of the virus, which has

<!-- b001226 | contents | pages [30] -->
the same eﬀect on a regional scale as hospitals do on a small scale. Using doses of vaccine to

<!-- b001227 | contents | pages [30] -->
keep the outbreak contained within the most aﬄicted regions, while ethically suspect, will

<!-- b001228 | contents | pages [30] -->
likely save more lives than attempting to vaccinate everyone equally and allowing the virus

<!-- b001229 | contents | pages [30] -->
to spread.

<!-- b001230 | contents | pages [30] -->
Cures, on the other hand, will linearly reduce the number of persons infected with the

<!-- b001231 | contents | pages [30] -->
virus and the number of persons occupying hospital beds. This one-two punch means that

<!-- b001232 | contents | pages [30] -->
cures, when supplied to a region, do even better than expected if the cure takes less time

<!-- b001233 | contents | pages [30] -->
to take eﬀect than the average duration of a recovery or death, as the cure will eﬀectively

<!-- b001234 | contents | pages [30] -->
free up additional hospital beds and improve the “eﬃciency” of hospitals at treating and

<!-- b001235 | furniture | pages [31] -->
Team # 32722

<!-- b001236 | furniture | pages [31] -->
Page 31 of 37

<!-- b001237 | contents | pages [31] -->
isolating patients.

<!-- b001238 | contents | pages [31] -->
Finally, we should note that in a scenario as complex as this one, models are not a

<!-- b001239 | contents | pages [31] -->
substitute for real data, and a close eye should be kept on both the actual trends predicted

<!-- b001240 | contents | pages [31] -->
from data and ground reports in addition to those produced by models. In addition, should

<!-- b001241 | contents | pages [31] -->
models be necessary, an eﬀort must be made to procure useful and accurate data on the

<!-- b001242 | contents | pages [31] -->
ground to provide background for these models, something we sorely lacked.

<!-- b001243 | contents | pages [31] -->
4.3. Future Work

<!-- b001244 | contents | pages [31] -->
Our model was intended to be used with a large number of regions corresponding to

<!-- b001245 | contents | pages [31] -->
actual geographic regions, with speciﬁc regional parameters derived from real-world data.

<!-- b001246 | contents | pages [31] -->
This would allow us to run simulations with speciﬁc geographic meaning with varying degrees

<!-- b001247 | contents | pages [31] -->
of ﬁdelity. However, gathering the data on the geographic speciﬁcs of each region, how they

<!-- b001248 | contents | pages [31] -->
connect, and how the outbreak is currently occurring in them turned out to be a monumental

<!-- b001249 | contents | pages [31] -->
task outside of the scope of this 96 hour project.

<!-- b001250 | contents | pages [31] -->
4.3.1. Geography Based Modeling

<!-- b001251 | contents | pages [31] -->
There comes a time in every model’s life when it must put away simple toy models and

<!-- b001252 | contents | pages [31] -->
attempt to tackle the things it was built to deal with. One of the core features of our multi-

<!-- b001253 | contents | pages [31] -->
layered approach is that it is a simple matter to expand a simulation to include additional

<!-- b001254 | contents | pages [31] -->
levels of detail, from adding new cities to new regions to new nations outright.

<!-- b001255 | contents | pages [31] -->
We had devised but did not implement an extremely simple model of the infected region

<!-- b001256 | contents | pages [31] -->
demonstrating this potential application of our approach, cf.13.

<!-- b001257 | contents | pages [31] -->
These nodes, and their

<!-- b001258 | contents | pages [31] -->
geographic positions, were chosen in an arbitrary manner but are intended to represent the

<!-- b001259 | contents | pages [31] -->
major urban centers of each nation and rural areas that are either largely isolated or closely

<!-- b001260 | contents | pages [31] -->
bordering other nations. We make no claims as to the accuracy of this model as it relates

<!-- b001261 | contents | pages [31] -->
to actual geopolitical connections between these nations, nor do we use it to make actual

<!-- b001262 | contents | pages [31] -->
claims about said region. It exists to serve as an example of the mixture of urban, rural,

<!-- b001263 | contents | pages [31] -->
and isolated communities present in the West Africa region and serve as an example of the

<!-- b001264 | contents | pages [31] -->
types of behaviors that emerge when dealing with such a system.

<!-- b001265 | furniture | pages [32] -->
Team # 32722

<!-- b001266 | furniture | pages [32] -->
Page 32 of 37

<!-- b001267 | caption | pages [32] -->
Figure 13: The generalized geography based network model. Background image from [20].

<!-- b001268 | contents | pages [32] -->
4.3.2. Placement of Distribution Centers

<!-- b001269 | contents | pages [32] -->
We have already covered at length the fact that the lack of infrastructure in the region

<!-- b001270 | contents | pages [32] -->
complicates aid eﬀorts due to the level of diﬃculty in getting persons and material from

<!-- b001271 | contents | pages [32] -->
one point to another.

<!-- b001272 | contents | pages [32] -->
At the same time, the distribution of population in the aﬄicted

<!-- b001273 | contents | pages [32] -->
countries typically features a few dense cities spread throughout low-density, semi-isolated

<!-- b001274 | contents | pages [32] -->
rural regions.

<!-- b001275 | contents | pages [32] -->
This raises an interesting conundrum: where do we ﬁrst ship our medicines, such that we

<!-- b001276 | contents | pages [32] -->
minimize the number of persons aﬄicted with the disease and the duration of the outbreak?

<!-- b001277 | contents | pages [32] -->
Our model allows us to attempt to answer this question by changing which nodes are

<!-- b001278 | contents | pages [32] -->
identiﬁed as transportation hubs and are therefore capable of receiving shipments of the

<!-- b001279 | contents | pages [32] -->
cure and vaccine from the outside world. Investigating the trade oﬀof placing distribution

<!-- b001280 | contents | pages [32] -->
centers—which are guaranteed to receive more doses of the cure and vaccine—in extremely

<!-- b001281 | contents | pages [32] -->
populated areas that are vulnerable to massive outbreaks versus extremely well-connected

<!-- b001282 | contents | pages [32] -->
regions without regard to the number of infected is an interesting one, and one that can be

<!-- b001283 | contents | pages [32] -->
potentially investigated with our model.

<!-- b001284 | contents | pages [32] -->
4.3.3. Distribution Laws

<!-- b001285 | contents | pages [32] -->
Considering data gathered with our 4-region model, it is apparent that diﬀerent methods

<!-- b001286 | contents | pages [32] -->
of splitting the limited quantity of drugs between nodes will produce diﬀerent outcomes, and

<!-- b001287 | contents | pages [32] -->
that some distributions are more favorable than others with regards to human survivability.

<!-- b001288 | contents | pages [32] -->
To examine the eﬀects of this behavior, our model could be forced to distribute med-

<!-- b001289 | contents | pages [32] -->
ications in accordance to a variety of additional distribution rules. For example, it may

<!-- b001290 | contents | pages [32] -->
make sense for individual regions to consider the regions it is connected to and distribute a

<!-- b001291 | furniture | pages [33] -->
Team # 32722

<!-- b001292 | furniture | pages [33] -->
Page 33 of 37

<!-- b001293 | contents | pages [33] -->
quantity of medicines that is proportional to the number of infected persons in those regions.

<!-- b001294 | contents | pages [33] -->
Or perhaps another approach more equitably reduces the number of deaths. In either case,

<!-- b001295 | contents | pages [33] -->
the modular framework for deﬁning distribution laws should allow for more modeling to be

<!-- b001296 | contents | pages [33] -->
done in this region, contingent on the ability of the modeler to obtain accurate and sensible

<!-- b001297 | contents | pages [33] -->
data on the geographic and infrastructure factors within a region.

<!-- b001298 | furniture | pages [34] -->
Team # 32722

<!-- b001299 | furniture | pages [34] -->
Page 34 of 37

<!-- b001300 | contents | pages [34] -->
Appendix A. Assumptions

<!-- b001301 | contents | pages [34] -->
1. Closed system: Regions in the simulation constitute the “world” as a whole, i.e.

<!-- b001302 | contents | pages [34] -->
there are no people able to enter from/leave to other undeﬁned regions. This limits

<!-- b001303 | contents | pages [34] -->
our ability to model the spread on a global scale without including the entire world in

<!-- b001304 | contents | pages [34] -->
our simulation.

<!-- b001305 | contents | pages [34] -->
2. Partial Motivation: Individuals in the simulation react to the overall state of the

<!-- b001306 | contents | pages [34] -->
epidemic in a city, φi(t), but are unable to have any further motivations, such as familial

<!-- b001307 | contents | pages [34] -->
ties. This does not allow us to encompass full human behavior.

<!-- b001308 | contents | pages [34] -->
3. Data collected on West African Countries is accurate, if it exists: Data from

<!-- b001309 | contents | pages [34] -->
this region is notoriously hard to ﬁnd, incomplete, and/or out of date. Since no other

<!-- b001310 | contents | pages [34] -->
data exists (aside from synthetic data, see [21]) we assume what we have is accurate.

<!-- b001311 | contents | pages [34] -->
4. Modiﬁed Gravity Mobility Model is accurate: The core of this model seems

<!-- b001312 | contents | pages [34] -->
sound, and its predictions match empirical data for this region, but the data from

<!-- b001313 | contents | pages [34] -->
speciﬁc regions tends to be unreliable and the ﬁtting parameters in this model may

<!-- b001314 | contents | pages [34] -->
not be consistent across diﬀerent regions.

<!-- b001315 | contents | pages [34] -->
5. Virus propagation parameters for Guinea and Liberia are the same: little to

<!-- b001316 | contents | pages [34] -->
no data could be found concerning Guinea’s sanitation/health infrastructure, region

<!-- b001317 | contents | pages [34] -->
speciﬁc virus behavior, etc. This prevented us from creating a set of parameters for

<!-- b001318 | contents | pages [34] -->
this critical nation. As Sierra Leone was harder-hit than both Liberia and Guinea, we

<!-- b001319 | contents | pages [34] -->
assume that Guinea would more likely share parameters with Liberia than with Sierra

<!-- b001320 | contents | pages [34] -->
Leone.

<!-- b001321 | contents | pages [34] -->
6. Virus propagation parameters are constant across any given country: These

<!-- b001322 | contents | pages [34] -->
parameters can in principle be aﬀected by changes in sanitation level, climate, edu-

<!-- b001323 | contents | pages [34] -->
cation, and other characteristics that can vary across a country. By assuming they

<!-- b001324 | contents | pages [34] -->
are constant, we lose some richness in our results, which may lead to some emergent

<!-- b001325 | contents | pages [34] -->
behaviors.

<!-- b001326 | contents | pages [34] -->
7. Vaccination attempts are limited solely by the quantity of vaccines in the

<!-- b001327 | contents | pages [34] -->
region: In reality, doctors/aid workers are likely to be a part of the process of getting

<!-- b001328 | contents | pages [34] -->
vaccinated. We assume that this is not the case because it is simpler and the length

<!-- b001329 | contents | pages [34] -->
of time/amount of eﬀort required to vaccinate someone is not clear. For example, are

<!-- b001330 | contents | pages [34] -->
people being vaccinated after they go to a hospital, or are aid workers travelling the

<!-- b001331 | contents | pages [34] -->
city and rapidly vaccinating anyone that is eligible and willing?

<!-- b001332 | contents | pages [34] -->
8. Vaccine is 100% eﬀective for susceptible individuals and 0% eﬀective for all

<!-- b001333 | contents | pages [34] -->
others: As no vaccine for Ebola exists presently, judging the eﬃcacy of such a vaccine

<!-- b001334 | contents | pages [34] -->
is challenging. Modelling it after other vaccines is also not justiﬁed, as many diﬀerent

<!-- b001335 | contents | pages [34] -->
vaccination techniques exist, and viruses behave diﬀerently in each case.

<!-- b001336 | contents | pages [34] -->
9. An individual must remain in a hospital/treatment center throughout the

<!-- b001337 | contents | pages [34] -->
cure and recovery process: Since the cure does not yet exist, we postulated that it

<!-- b001338 | contents | pages [34] -->
would only be able to be administered in a hospital setting. This restricts the available

<!-- b001339 | contents | pages [34] -->
hospital space and hence, the number of individuals able to receive the cure.

<!-- b001340 | contents | pages [34] -->
10. Generalization of smaller administrative divisions: Computational expense pro-

<!-- b001341 | contents | pages [34] -->
hibits one from simulation large numbers of cities at once. We represented groups of

<!-- b001342 | contents | pages [34] -->
individual cities as a single large city, but by doing so we are unable to take into

<!-- b001343 | furniture | pages [35] -->
Team # 32722

<!-- b001344 | furniture | pages [35] -->
Page 35 of 37

<!-- b001345 | contents | pages [35] -->
account small variances that may give rise to important emergent behaviors at the

<!-- b001346 | contents | pages [35] -->
correct scale.

<!-- b001347 | contents | pages [35] -->
11. Population sizes are re-scalable to some extent: The simulations shows only

<!-- b001348 | contents | pages [35] -->
a slight sensitivity to the order of magnitude of the number of individuals in a city

<!-- b001349 | contents | pages [35] -->
or region—down to a lower bound. This is useful as it greatly lowers computational

<!-- b001350 | contents | pages [35] -->
expense. How the simulation behaves at very large orders of magnitude is not well

<!-- b001351 | contents | pages [35] -->
deﬁned.

<!-- b001352 | contents | pages [35] -->
12. Vaccine (and medicine) distribution follows a percentage-of-available rule:

<!-- b001353 | contents | pages [35] -->
Each city has their own quantity of vaccines, as well as a list of cities it is responsible for

<!-- b001354 | contents | pages [35] -->
shipping vaccines to. The quantity they ship is always some constant fraction of their

<!-- b001355 | contents | pages [35] -->
current vaccine supply. In reality, this fraction should depend on the need for vaccines

<!-- b001356 | contents | pages [35] -->
in both cities, as well as both cities’ current quantity of vaccines. This assumption

<!-- b001357 | contents | pages [35] -->
actually caused errors when we attempted large-scale simulations, as some cities acted

<!-- b001358 | contents | pages [35] -->
as “vaccine sinks”, accepting vaccines but not being responsible for shipping to any

<!-- b001359 | contents | pages [35] -->
other cities.

<!-- b001360 | contents | pages [35] -->
13. No averaging of simulations is needed to accurately capture behavior: This

<!-- b001361 | contents | pages [35] -->
assumption was only taken due to time constraints; upon visible inspection there were

<!-- b001362 | contents | pages [35] -->
slight changes in values from run to run for any given set of parameters.

<!-- b001363 | contents | pages [35] -->
14. Vaccines and Medication may be stored indeﬁnitely: Without an idea of how

<!-- b001364 | contents | pages [35] -->
long an actual vaccine would be able to be used, the simulation results would vary

<!-- b001365 | contents | pages [35] -->
signiﬁcantly. By assuming that vaccines and medicines have an inﬁnite shelf life, we

<!-- b001366 | contents | pages [35] -->
may not fully capture the true supply and demand behavior of vaccine-implementation.

<!-- b001367 | contents | pages [35] -->
15. Vaccination only requires a single dose: The feasibility and logistics of adminis-

<!-- b001368 | contents | pages [35] -->
tering a multiple dosage vaccination to a large percentage of the population would be

<!-- b001369 | contents | pages [35] -->
a herculean eﬀort. Individuals would need to not only be willing to get vaccinated, but

<!-- b001370 | contents | pages [35] -->
also be able to follow through with the multiple doses. Without this assumption, the

<!-- b001371 | contents | pages [35] -->
number of vaccines needed and the timeline for which they should be deployed would

<!-- b001372 | contents | pages [35] -->
be an even more severe challenge. Hence, we justify this assumption by focusing our

<!-- b001373 | contents | pages [35] -->
model on the most eﬀective and reasonable form of vaccination.

<!-- b001374 | contents | pages [35] -->
Appendix B. Diﬀerential Equation Model

<!-- b001375 | contents | pages [35] -->
The following equations can be used to describe the changes of state in our compartment

<!-- b001376 | contents | pages [35] -->
model on a more rigorous mathematical basis, cf. Fig. 4.

<!-- b001377 | contents | pages [35] -->
∂tS(t) = −βc1Ie(t) + βc2Il(t) + βfU(t)

<!-- b001378 | contents | pages [35] -->
S

<!-- b001379 | contents | pages [35] -->
(B.1)

<!-- b001380 | contents | pages [35] -->
Ptotal

<!-- b001381 | contents | pages [35] -->
∂tL(t) = −∂tS(t) −γw1L(t)

<!-- b001382 | contents | pages [35] -->
(B.2)

<!-- b001383 | contents | pages [35] -->
∂tIe(t) = γw1L(t) −(γw2 + γh1)Ie(t)

<!-- b001384 | contents | pages [35] -->
(B.3)

<!-- b001385 | contents | pages [35] -->
∂tIl(t) = γw2Ie(t) −(γh2 + γd)Il(t)

<!-- b001386 | contents | pages [35] -->
(B.4)

<!-- b001387 | contents | pages [35] -->
∂tH(t) = γh1Ie(t) + γh2Il(t) −(γdh + γR)H(t)

<!-- b001388 | contents | pages [35] -->
∂tC(t) = γRH(t)

<!-- b001389 | contents | pages [35] -->
(B.5)

<!-- b001390 | contents | pages [35] -->
(B.6)

<!-- b001391 | contents | pages [35] -->
∂tU(t) = γdIl(t) + γdhH(t) −γfU(t)

<!-- b001392 | contents | pages [35] -->
∂tB(t) = γfU(t)

<!-- b001393 | contents | pages [35] -->
(B.7)

<!-- b001394 | contents | pages [35] -->
(B.8)

<!-- b001395 | furniture | pages [36] -->
Team # 32722

<!-- b001396 | furniture | pages [36] -->
Page 36 of 37

<!-- b001397 | contents | pages [36] -->
References

<!-- b001398 | contents | pages [36] -->
[1] Ebola situation report - 4 february 2015. World Health Organization. [Online].

<!-- b001399 | contents | pages [36] -->
Available: http://apps.who.int/ebola/en/ebola-situation-report/situation-reports/

<!-- b001400 | contents | pages [36] -->
ebola-situation-report-4-february-2015

<!-- b001401 | contents | pages [36] -->
[2] (2014, November) Prevention. Centers for Disease Control and Prevention. [Online].

<!-- b001402 | contents | pages [36] -->
Available: http://www.cdc.gov/vhf/ebola/prevention/index.html

<!-- b001403 | contents | pages [36] -->
[3] (2014, August). [Online]. Available:

<!-- b001404 | contents | pages [36] -->
http://www.dw.de/ebola-outbreak-in-drc-same-virus-but-diﬀerent/a-17875656

<!-- b001405 | contents | pages [36] -->
[4] (2014, August) Frequently asked questions on ebola virus disease. World Health

<!-- b001406 | contents | pages [36] -->
Organization. [Online]. Available:

<!-- b001407 | contents | pages [36] -->
http://www.who.int/csr/disease/ebola/faq-ebola/en/

<!-- b001408 | contents | pages [36] -->
[5] C. Ezigbalike, “African statistical yearbook - 2014,” African Statistical Coordination

<!-- b001409 | contents | pages [36] -->
Committee, Tech. Rep., 2014.

<!-- b001410 | contents | pages [36] -->
[6] H. Hethcote, “The mathematics of infectious diseases,” SIAM Review, vol. 42, no. 4,

<!-- b001411 | contents | pages [36] -->
pp. 599–653, December 2000.

<!-- b001412 | contents | pages [36] -->
[7] A Contribution to the Mathematical Theory of Epidemics, vol. 115, no. 772.

<!-- b001413 | contents | pages [36] -->
Royal

<!-- b001414 | contents | pages [36] -->
Society of London. Series A, Containing Papers of a Mathematical and Physical

<!-- b001415 | contents | pages [36] -->
Character, August 1927.

<!-- b001416 | contents | pages [36] -->
[8] GLEAMviz Simulator Client Manual, The Global Epidemic and Mobility Model.

<!-- b001417 | contents | pages [36] -->
[9] C. M. Rivers, E. T. Lofgren, M. Marathe, S. Eubank, and B. L. Lewis, “Modeling the

<!-- b001418 | contents | pages [36] -->
Impact of Interventions on an Epidemic of Ebola in Sierra Leone and Liberia,” PLOS

<!-- b001419 | contents | pages [36] -->
Curr. Outbreaks, pp. 1–14, 2014.

<!-- b001420 | contents | pages [36] -->
[10] (2015, February) Ebola virus disease (evd) information for clinicians in u.s. healthcare

<!-- b001421 | contents | pages [36] -->
settings. Centers for Disease Control and Prevention. [Online]. Available:

<!-- b001422 | contents | pages [36] -->
http://www.cdc.gov/vhf/ebola/healthcare-us/preparing/clinicians.html

<!-- b001423 | contents | pages [36] -->
[11] F. Simini, M. C. Gonz´alez, A. Maritan, and A.-L. Barab´asi, “A universal model for

<!-- b001424 | contents | pages [36] -->
mobility and migration patterns,” Nature, vol. 484, pp. 96–100, 2012.

<!-- b001425 | contents | pages [36] -->
[12] M. E. Halloran, A. Vespignani, N. Bharti, L. R. Feldstein, K. A. Alexander,

<!-- b001426 | contents | pages [36] -->
M. Ferrari, J. Shaman, J. M. Drake, T. Porco, J. N. S. Eisenberg, S. Y. Del Valle,

<!-- b001427 | contents | pages [36] -->
E. Lofgren, S. V. Scarpino, M. C. Eisenberg, D. Gao, J. M. Hyman, S. Eubank, and

<!-- b001428 | contents | pages [36] -->
I. M. Longini, “Ebola: Mobility data,” Science, vol. 346, no. 6208, p. 433, 2014.

<!-- b001429 | contents | pages [36] -->
[Online]. Available: http://www.sciencemag.org/content/346/6208/433.1.short

<!-- b001430 | contents | pages [36] -->
[13] A. Tatem and L. Bengtsson. (2014, August) Ebola mobility estimates. [Online].

<!-- b001431 | contents | pages [36] -->
Available: http://www.worldpop.org.uk/ebola/

<!-- b001432 | contents | pages [36] -->
[14] A. Rigo et al.

<!-- b001433 | furniture | pages [37] -->
Team # 32722

<!-- b001434 | furniture | pages [37] -->
Page 37 of 37

<!-- b001435 | contents | pages [37] -->
[15] E. Jones, T. Oliphant, P. Peterson et al., “SciPy: Open source scientiﬁc tools for

<!-- b001436 | contents | pages [37] -->
Python,” 2015, [Online; accessed 2015-02-09]. [Online]. Available:

<!-- b001437 | contents | pages [37] -->
http://www.scipy.org/

<!-- b001438 | contents | pages [37] -->
[16] J. D. Hunter, “Matplotlib: A 2d graphics environment,” Computing In Science &

<!-- b001439 | contents | pages [37] -->
Engineering, vol. 9, no. 3, pp. 90–95, 2007.

<!-- b001440 | contents | pages [37] -->
[17] (2014, November) Treatment. Centers for Disease Control and Prevention. [Online].

<!-- b001441 | contents | pages [37] -->
Available: http://www.cdc.gov/vhf/ebola/treatment/index.html

<!-- b001442 | contents | pages [37] -->
[18] Ebola situation report - 21 january 2015. World Health Organization. [Online].

<!-- b001443 | contents | pages [37] -->
Available: http://apps.who.int/ebola/en/status-outbreak/situation-reports/

<!-- b001444 | contents | pages [37] -->
ebola-situation-report-21-january-2015

<!-- b001445 | contents | pages [37] -->
[19] (2014, September) Sierra leone: a traditional healer and a funeral. World Health

<!-- b001446 | contents | pages [37] -->
Organization. [Online]. Available:

<!-- b001447 | contents | pages [37] -->
http://www.who.int/csr/disease/ebola/ebola-6-months/sierra-leone/en/

<!-- b001448 | contents | pages [37] -->
[20] (2014, October). [Online]. Available:

<!-- b001449 | contents | pages [37] -->
http://www.dw.de/fearing-ebola-german-companies-leave-west-africa/a-17996012

<!-- b001450 | contents | pages [37] -->
[21] (2015) Ebola synthetic information. Network Dynamics and Simulation Science

<!-- b001451 | contents | pages [37] -->
Laboratory. [Online]. Available: http://www.vbi.vt.edu/ndssl/ebola/ebola-data

<!-- b001452 | furniture | pages [38] -->


<!-- b001453 | furniture | pages [38] -->


<!-- b001454 | furniture | pages [38] -->
Team #32722

<!-- b001455 | contents | pages [38] -->
February 10th, 2015

<!-- b001456 | contents | pages [38] -->
World Health And Medical Organization (WHAMO) Bulletin

<!-- b001457 | contents | pages [38] -->
Following millions of dollars in research and development funding and scores of human trials, we are

<!-- b001458 | contents | pages [38] -->
proud to announce that both a vaccine (Preventatine®) and cure (Curzimall®)  for Ebola have successfully

<!-- b001459 | contents | pages [38] -->
passed human trials and are entering full-scale production. In light of the current outbreak of Ebola in

<!-- b001460 | contents | pages [38] -->
the West African region, these drugs will provide us with additional tools to reduce and eventually

<!-- b001461 | contents | pages [38] -->
eradicate the virus from the region and, if all goes well, the world at large.

<!-- b001462 | contents | pages [38] -->
Serial production of Curzimall® and Preventatine® will begin in the coming months, during which time

<!-- b001463 | contents | pages [38] -->
their supply will be extremely limited. Beyond the dosages required for health and medical workers, the

<!-- b001464 | contents | pages [38] -->
distribution of these drugs remains an ethical and logistical nightmare. To provide us with unbiased,

<!-- b001465 | contents | pages [38] -->
reasonable, and accurate guidance, we have given three of our unpaid interns the last ninety-six hours

<!-- b001466 | contents | pages [38] -->
to develop a mathematical model of both the spread of Ebola and the mechanisms governing the

<!-- b001467 | contents | pages [38] -->
effectiveness and logistics surrounding a vaccine and cure distribution plan.

<!-- b001468 | contents | pages [38] -->
In response to the predictions of the model, we have identified the following as the focal points of our

<!-- b001469 | contents | pages [38] -->
plan to eradicate Ebola in the West African region:

<!-- b001470 | heading | pages [38] -->
1. Continued expansion of hospitals and Ebola Treatment Centers: For all scenarios analyzed by

<!-- b001471 | prose | pages [38] -->
the model, the most important factor in eliminating the prevalence of Ebola and containing its spread was the ability of the medical community to isolate symptomatic patients, which is closely tied to the capacity of local medical facilities.

<!-- b001472 | heading | pages [38] -->
2. Cure and Vaccine Production Targets: While unable to predict the exact quantity of Curzimall®

<!-- b001473 | prose | pages [38] -->
and Preventatine® required to eradicate Ebola in this region, our model has predicted that the quantities required will scale as a constant factor of the number of infected persons in the region. Though the exact number of infected is not known (and estimations are disputed), this knowledge has allowed us to set the pace for the expansion of our production facilities in a rational and sane way, assuming funding and public support remain high.

<!-- b001474 | heading | pages [38] -->
3. Distribution of Cures and Vaccines: Our model predicts that doses of the Curzimall® drug are

<!-- b001475 | prose | pages [38] -->
best utilized in regions where the medical facilities are at or exceeding capacity, as it will allow for the treatment and isolation of additional cases, whereas if the medical infrastructure is undertaxed (or extraordinarily small), the throughput of infected persons will be less than ideal. Doses of the vaccine Preventatine®, on the other hand, are most useful when delivered to locations that are at high risk of an increase in the number of infections, but currently have relatively few, thus allowing the region to `outpace' the infection. These utility models will guide our distribution plan for the first several batches of Curzimall® and Preventatine®.

<!-- b001476 | heading | pages [38] -->
4. Geographic location of regional distribution centers: Citing their lack of time, data, and sleep,

<!-- b001477 | prose | pages [38] -->
our team of interns was not able to fully incorporate geographic location data to tell us precisely where to send supplies. We must thus rely on our intuition and the existing (but poorly documented) transportation infrastructure of the region to decide where to set up distribution centers.

<!-- b001478 | furniture | pages [38] -->


<!-- b001479 | prose | pages [38] -->
Past experiences in releasing the explicit predictions of our models have dissuaded us from providing the specific predictions raised by this model to prevent wide-scale panic. With that being said, the

<!-- b001480 | furniture | pages [39] -->


<!-- b001481 | furniture | pages [39] -->


<!-- b001482 | furniture | pages [39] -->
Team #32722

<!-- b001483 | prose | pages [39] -->
model does predict that, barring any large breakouts due to uncontrollable evnets, the decline and demise of the Ebola virus in West Africa by late 2015 is inevitable even if the cures and vaccine turn out to be largely ineffective, and possibly as early as May of 2015 if they prove to be very effective.

<!-- b001484 | furniture | pages [39] -->


<!-- b001485 | furniture | pages [39] -->

