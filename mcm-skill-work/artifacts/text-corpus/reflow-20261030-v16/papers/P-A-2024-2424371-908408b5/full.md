# P-A-2024-2424371-908408b5

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2024

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
A

<!-- b000005 | title | pages [1] -->
2424371

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Magic Sex Ratio : Exploring the Important Role of

<!-- b000008 | title | pages [1] -->
Lampreys in the Ecosystem

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
As one of the oldest vertebrates, the sea lampreys has unique mechanisms of gender differentiation.In order to examine the advantages and disadvantages of the lampreys’ ability to change its sex ratio according to resource availability, we develop two main models, the Population Growth Model Induced by Sex Ratio and the 3-R Index Model of Ecosystem Stability.

<!-- b000011 | prose | pages [1] -->
Firstly, we develop a Population Growth Model based on differential equations, which mainly considers the factors of sex ratio, migration and inter-organism interac- tions of the lampreys. In terms of the induced factors and effects of sex ratio, we use the Least Squares Method to fit a functional relationship between the larval growth rate and food density of the lampreys, then establish a sex logistic function to determine the effect of larval growth rate on the sex differentiation of the lampreys. Lastly, we consider the effect of sex ratio on the growth rate. In terms of interactions among creatures, we mainly consider the parasitic relationship between lampreys and host-fish in the ocean and the predation relationship between lampreys and plankton in the river, and integrate the im- proved Logistic Model and the Lotka-Volterra Equations to establish differential equa- tions for biomass of different species over time. Finally, Finite Volume Method (FVM) is used to solve the numerical solution of the PDE.

<!-- b000012 | prose | pages [1] -->
For problem 1, given the same initial conditions and using a population growth model, consider the trends in biomass of different species when the lampreys can change the sex ratio and when it cannot change the sex ratio, respectively, and then analyse the impact of the lampreys on the larger ecosystem. (result:Figure 8-11)

<!-- b000013 | prose | pages [1] -->
For problem 2, we adjust the model parameters to simulate the impacts of harsh en- vironments on the ecosystems of lampreys, such as human killings, famine and habitat destruction, and find that lampreys can adjust the sex ratio, which is an advantage against harsh environments, but has a serious "time lag effect".

<!-- b000014 | prose | pages [1] -->
For problem 3, we establish a 3-R index model to measure ecosystem stability. Firstly, we use three quantitative indicators to measure the stability of ecosystems( Resistance, Resilience and Recovery) and then we perturb the ecosystems at a specific moment to change the sex ratio, and then calculate the 3-R Index with the help of the change of Shannon Index before and after the perturbation to get the effect of the sex ratio on the stability of ecosystem. (result:Figure 17)

<!-- b000015 | prose | pages [1] -->
For problem 4, we extend the model by adding more species to the analysis, intro- ducing competitive factors and analysing the advantages of sex change in lampreys over other different types of creatures. (result:Figure 19)

<!-- b000016 | keywords | pages [1] -->
Keywords: Lampreys, Sex Ratio, PDE, Finite Volume Method, 3-R Index

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1 Introduction

<!-- b000019 | contents | pages [2] -->
3

<!-- b000020 | contents | pages [2] -->
1.1

<!-- b000021 | contents | pages [2] -->
Background

<!-- b000022 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [2] -->
3

<!-- b000024 | contents | pages [2] -->
1.2

<!-- b000025 | contents | pages [2] -->
Restatement

<!-- b000026 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
3

<!-- b000028 | contents | pages [2] -->
1.3

<!-- b000029 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
2 Assumptions and Justifications

<!-- b000032 | contents | pages [2] -->
4

<!-- b000033 | contents | pages [2] -->
3 Notations

<!-- b000034 | contents | pages [2] -->
5

<!-- b000035 | contents | pages [2] -->
4 Model I : Population Growth Model Induced by Lampreys Sex Ratio

<!-- b000036 | contents | pages [2] -->
5

<!-- b000037 | contents | pages [2] -->
4.1

<!-- b000038 | contents | pages [2] -->
Model Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
4.2

<!-- b000041 | contents | pages [2] -->
Model Buliding

<!-- b000042 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
6

<!-- b000044 | contents | pages [2] -->
4.2.1

<!-- b000045 | contents | pages [2] -->
Migratory Sub-model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
7

<!-- b000047 | contents | pages [2] -->
4.2.2

<!-- b000048 | contents | pages [2] -->
Predisposing Factors and Effects of Sex Ratio . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
8

<!-- b000050 | contents | pages [2] -->
4.2.3

<!-- b000051 | contents | pages [2] -->
Population Growth Model in River . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
9

<!-- b000053 | contents | pages [2] -->
4.2.4

<!-- b000054 | contents | pages [2] -->
Population Growth Model in Ocean . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
9

<!-- b000056 | contents | pages [2] -->
4.3

<!-- b000057 | contents | pages [2] -->
Model Solution

<!-- b000058 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
12

<!-- b000060 | contents | pages [2] -->
4.4

<!-- b000061 | contents | pages [2] -->
Results of Problem I . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
12

<!-- b000063 | contents | pages [2] -->
4.5

<!-- b000064 | contents | pages [2] -->
the Results of Problem II . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
14

<!-- b000066 | contents | pages [2] -->
4.5.1

<!-- b000067 | contents | pages [2] -->
Advantages: strong resistance to harsh environments . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
14

<!-- b000069 | contents | pages [2] -->
4.5.2

<!-- b000070 | contents | pages [2] -->
Disadvantages: time lag in adjusting the sex ratio

<!-- b000071 | contents | pages [2] -->
. . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
16

<!-- b000073 | contents | pages [2] -->
5

<!-- b000074 | contents | pages [2] -->
Model II : the 3-R Index Model Based on Changes of Ecosystem Stability un-

<!-- b000075 | contents | pages [2] -->
der the Influence of Lampreys’ Sex Ratio

<!-- b000076 | contents | pages [2] -->
16

<!-- b000077 | contents | pages [2] -->
5.1

<!-- b000078 | contents | pages [2] -->
Model Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
16

<!-- b000080 | contents | pages [2] -->
5.2

<!-- b000081 | contents | pages [2] -->
Model Buliding

<!-- b000082 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
16

<!-- b000084 | contents | pages [2] -->
5.2.1

<!-- b000085 | contents | pages [2] -->
Selection of Indicators to Measure Ecosystem Stability . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
16

<!-- b000087 | contents | pages [2] -->
5.2.2

<!-- b000088 | contents | pages [2] -->
Quantification of indicators . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [2] -->
17

<!-- b000090 | contents | pages [2] -->
5.2.3

<!-- b000091 | contents | pages [2] -->
Internal system variables . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [2] -->
18

<!-- b000093 | contents | pages [2] -->
5.2.4

<!-- b000094 | contents | pages [2] -->
Ecosystem disturbance factors . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [2] -->
19

<!-- b000096 | contents | pages [2] -->
5.3

<!-- b000097 | contents | pages [2] -->
Results of Problem III . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000098 | contents | pages [2] -->
19

<!-- b000099 | contents | pages [2] -->
6 Model Expansion

<!-- b000100 | contents | pages [2] -->
20

<!-- b000101 | contents | pages [2] -->
7 Sensitivity Analysis

<!-- b000102 | contents | pages [2] -->
22

<!-- b000103 | contents | pages [2] -->
8 Strengths and Weaknesses

<!-- b000104 | contents | pages [2] -->
23

<!-- b000105 | contents | pages [2] -->
8.1

<!-- b000106 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [2] -->
23

<!-- b000108 | contents | pages [2] -->
8.2

<!-- b000109 | contents | pages [2] -->
Weaknesses and Possible Improvement

<!-- b000110 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000111 | contents | pages [2] -->
23

<!-- b000112 | contents | pages [2] -->
9 Conclusion

<!-- b000113 | contents | pages [2] -->
24

<!-- b000114 | contents | pages [2] -->
References

<!-- b000115 | contents | pages [2] -->
24

<!-- b000116 | contents | pages [2] -->
2

<!-- b000117 | furniture | pages [3] -->
Team # 2424371

<!-- b000118 | furniture | pages [3] -->
Page 3 of 25

<!-- b000119 | heading | pages [3] -->
1 Introduction

<!-- b000120 | heading | pages [3] -->
1.1 Background

<!-- b000121 | prose | pages [3] -->
Historically, the sea lamprey has been considered a prized ingredient and favored by many. Zoologically, the sea lamprey is one of the oldest surviving vertebrates and is a key species in the study of vertebrate origins and evolution. From an ecological point of view, the sea lamprey is a carnivorous ectoparasite and can change its sex ratio in response to changes in the external environment, which is crucial to the stability of the ecosystem.

<!-- b000122 | caption | pages [3] -->
Figure 1: sea lamprey (https://baijiahao.baidu.com/)

<!-- b000123 | prose | pages [3] -->
Since the invasion of sea lampreys into the Great Lakes beginning in the 1950s, with impacts on the ecology and fisheries of the Great Lakes, there is an urgent need for re- search on the ecosystem impacts of sea lamprey sex ratio in support of real-life control and protection of sea lampreys [1], [2].

<!-- b000124 | heading | pages [3] -->
1.2 Restatement

<!-- b000125 | prose | pages [3] -->
Considering the background information and limiting conditions identified in the prob- lem statement, we are supposed to address the following issues:

<!-- b000126 | prose | pages [3] -->
• Build a model to determine the effects on the ecosystem of a sea lamprey population that can change its sex ratio.

<!-- b000127 | prose | pages [3] -->
• Analyze the advantages and disadvantages of the sea lamprey population in the sur- vival of the ecosystem.

<!-- b000128 | prose | pages [3] -->
• Develop a model to determine the impacts on ecosystem stability based on the sex ratio of sea lampreys.

<!-- b000129 | prose | pages [3] -->
• Estimating the impact of sea lampreys on other species in ecosystems containing populations of sea lampreys with variable sex ratio.

<!-- b000130 | heading | pages [3] -->
1.3 Our Work

<!-- b000131 | prose | pages [3] -->
According to the requirements, our work is as follows:

<!-- b000132 | furniture | pages [4] -->
Team # 2424371

<!-- b000133 | furniture | pages [4] -->
Page 4 of 25

<!-- b000134 | caption | pages [4] -->
Figure 2: the flow chart of our work

<!-- b000135 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000136 | prose | pages [4] -->
To simplify the problem and make it convenient for us to simulate real-life conditions, we make the following basic assumptions, each of which is properly justified:

<!-- b000137 | prose | pages [4] -->
Assumption 1: The sea lamprey feeds on plankton in rivers and parasitizes large fish • in the ocean.

<!-- b000138 | prose | pages [4] -->
Justification: Juvenile sea lampreys have immature organ development and do not have the conditions for parasitism, and generally feed on tiny plankton, such as al- gae and small invertebrates[3]. The majority of sea lampreys in rivers are juvenile individuals, so it is approximated that sea lampreys feed on plankton in rivers.

<!-- b000139 | heading | pages [4] -->
Assumption 2: Neglect the effects of water temperature, climate and other external

<!-- b000140 | prose | pages [4] -->
• environmental factors on the abundance of sea lamprey species.

<!-- b000141 | prose | pages [4] -->
Justification: Sea lampreys live primarily in waters of temperate and boreal climate types. They are usually found in temperate oceans, rivers and lakes, especially in areas where the water is clean, moderately warm and well oxygenated. Because of their ability to adapt to different water temperature ranges, sea lampreys can ignore the effects of environmental climate factors[4].

<!-- b000142 | prose | pages [4] -->
Assumption 3: Chemical agents such as steroids can directly alter the sex ratio of sea • lampreys, but not their birth and death rates.

<!-- b000143 | furniture | pages [5] -->
Team # 2424371

<!-- b000144 | furniture | pages [5] -->
Page 5 of 25

<!-- b000145 | prose | pages [5] -->
Justification: Chemicals such as steroids can induce sex change in juvenile sea lam- preys, and since most sea lampreys are in their juvenile years, it can be assumed that the use of steroids can directly change the sex ratio of sea lamprey populations.

<!-- b000146 | prose | pages [5] -->
Assumption 4: It is assumed that sea lampreys die immediately after spawning or • oviposition.

<!-- b000147 | prose | pages [5] -->
Justification: Studies have shown that most sea lamprey females and males stop feeding after mating and wait for a natural death[5]. During this time, sea lampreys have no impact on other organisms or the ecosystem, so it can be assumed that sea lampreys die immediately after spawning or oviposition.

<!-- b000148 | prose | pages [5] -->
Assumption 5: The ecosystem in which the lamprey is found has sufficient producers • to supply the survival of organisms at the bottom of the food chain.

<!-- b000149 | prose | pages [5] -->
Justification: Since the oceans have a very high biodiversity, it can be assumed that producers provide sufficient external nutrients to the ecosystem we construct.

<!-- b000150 | heading | pages [5] -->
3 Notations

<!-- b000151 | caption | pages [5] -->
Table 1: the list of notation

<!-- b000152 | heading | pages [5] -->
Symbol

<!-- b000153 | prose | pages [5] -->
Meaning

<!-- b000154 | prose | pages [5] -->
M1 the biomass of the male sea lampreys living in river M2 the biomass of the male sea lampreys living in different locations in ocean N1male the biomass of male lampreys migrating from the sea to the river N2male the biomass of male lampreys migrating from the river to the sea Rmale the biamass of males differentiated from the newborn larvae of lampreys P(t) the biomass of plankton in the river at moment t Hi the biomass of host-fish that are parasitized at moment t

<!-- b000155 | heading | pages [5] -->
4 Model I : Population Growth Model Induced by Lam-

<!-- b000156 | prose | pages [5] -->
preys Sex Ratio

<!-- b000157 | heading | pages [5] -->
4.1 Model Overview

<!-- b000158 | prose | pages [5] -->
According to the physiological activities and ranges of the sea lamprey, the life cycle of the sea lamprey is divided into three stages: the juvenile stage of metamorphosis in the river, the adult stage of survival by migrating to seawater, and the reproductive stage of migrating to the river. We focus on the effects of sea lamprey sex ratio, two migrations and biotic interactions on the abundance of different species in the community.

<!-- b000159 | prose | pages [5, 6] -->
When considering the sex ratio of the sea lamprey, we first use the least squares method to fit the relationship between the growth rate of the newborn sea lamprey and the concentration of food, and define the sex logistic function to determine the relation- ship between the sex ratio and the concentration of food, and then consider the effect of the sex ratio on the reproduction of the sea lamprey. When considering the two mi- grations of the sea lamprey, the population migration models in rivers and seawater at different times are established based on the characteristics of its two migrations. When considering the interactions between organisms, differential equations for the population of different species in the St. Lawrence River and the Gulf of St. Lawrence over time are presented based on the intraspecific (reproduction, intraspecific competition) and inter- specific (including interspecific competition, parasitism, and predation) relationships of the sea lamprey at different stages.

<!-- b000160 | furniture | pages [6] -->
Team # 2424371

<!-- b000161 | furniture | pages [6] -->
Page 6 of 25

<!-- b000163 | prose | pages [6] -->
Finally, the numerical solution of the system of partial differential equations is ob- tained using the finite volume method, and the changes of different species in a specific water area over time are obtained in communities that could change the sex ratio of the sea lamprey and those that could not change the sex ratio of the sea lamprey, all other things being the same, and it is analyzed that the sex ratio could be varied in a positive way for the ecosystem.

<!-- b000164 | heading | pages [6] -->
4.2 Model Buliding

<!-- b000165 | prose | pages [6] -->
The sea lamprey has a complex life cycle. Juvenile lampreys are hatched in freshwater rivers, and after metamorphosis and development into adults, they migrate to seawater to continue to survive, and then migrate back to freshwater rivers to spawn during the reproduction period.

<!-- b000166 | caption | pages [6] -->
Figure 3: the life history of the sea lampreys

<!-- b000167 | prose | pages [6, 7] -->
The Gulf of St. Lawrence is an important site for adult lampreys, and we focus on the survival of the species in waters ranging from 59° to 63.5° W longitude and from 46° to 50.5° N latitude. For simplicity of study, although in reality the range studied by the model is a spherical quadrilateral, we assume that spatial locations are divided equally by latitude and longitude, which in turn can be abstracted into planar rectan- gles with horizontal and vertical coordinates in a planar rectangular coordinate system according to latitude and longitude. All calculations of the shortest spherical distance be- tween two points represented using latitude and longitude in the model are transformed using Haversine’s formula [6] as shown below:

<!-- b000168 | furniture | pages [7] -->
Team # 2424371

<!-- b000169 | furniture | pages [7] -->
Page 7 of 25

<!-- b000171 | prose | pages [7] -->
s δ1 −δ2  α1 −α2  sin2 + cos δ1 cos δ2 sin2 d = 2 arcsin 2 2

<!-- b000172 | prose | pages [7] -->
where d denotes the shortest spherical distance and δ1, δ2, α1, α2 are the latitude and lon- gitude of the two points, respectively.

<!-- b000173 | caption | pages [7] -->
Figure 4: abstracting a spherical quadrilateral into a planar rectangle

<!-- b000174 | prose | pages [7] -->
The St. Lawrence River is home to juvenile and reproductive lampreys, and since species and environmental changes within the St. Lawrence River are not significant [7], and the succession of communities within the river is similar, we consider this portion of the water as a whole.

<!-- b000175 | prose | pages [7] -->
After the above analysis, we can set M1 to be the biomass of the male sea lampreys living in the St. Lawrence River and F1 to be female, which are both functions of time t. Let M2, F2 be the biomass of sea lampreys living in different locations in the St. Lawrence Lake, and they are functions of time t, longitude x, and latitude y.

<!-- b000176 | heading | pages [7] -->
4.2.1 Migratory Sub-model

<!-- b000177 | prose | pages [7] -->
There are two important migrations in the life cycle of the sea lampreys. The first occurs from March to April each year, during the northern hemisphere spring, when large num- bers of adult-bodied lampreys of varying ages (mostly 5-7 years old) migrate upstream from the ocean to freshwater rivers for subsequent mating and spawning [8]. The second time is in May to June each year, when most of the larvae undergo a long metamorphosis into adults (mostly 3-5 years old) and migrate toward the ocean for more food[9].

<!-- b000178 | prose | pages [7, 8] -->
ZZ N1male =δ(t −t1) · m1 · M2dxdy (1) (x,y) N2male =δ(t −t2) · m2 · M1 (2) ZZ N1female =δ(t −t1) · m1 · F2dxdy (3) (x,y) N2female =δ(t −t2) · m2 · F1 (4) where N1 is the biomass of lampreys migrating from the sea to the river at moment t, N2 is the biomass of lampreys migrating from the river to the sea at moment t and m1 and m2 are the migration rates of the two migrations, respectively. The reason the first equation needs to be integrated over spatial variables is that adults in all seas have the potential to migrate, and δ in the above equation can be expressed as:

<!-- b000179 | furniture | pages [8] -->
Team # 2424371

<!-- b000180 | furniture | pages [8] -->
Page 8 of 25

<!-- b000182 | prose | pages [8] -->
( 1 if t = 0 δ(t) = (5) 0 others

<!-- b000183 | heading | pages [8] -->
4.2.2 Predisposing Factors and Effects of Sex Ratio

<!-- b000184 | prose | pages [8] -->
Sea lampreys typically spawn in spring nesting habitats, and the gonads of larvae can remain histologically undifferentiated for extended periods of time. Field studies have shown that sex determination in sea lampreys is directly influenced by larval growth rates, with slower growth of larvae in non-productive environments allowing for more male-biased larvae and faster growth in productive environments allowing for more female- biased larvae[10]. Therefore define the sex logistic function:

<!-- b000185 | prose | pages [8] -->
1 η(v) = (6) 1 + e−(αv+β)

<!-- b000186 | prose | pages [8] -->
In the above equation η(v) denotes the probability of differentiating into a female when the growth rate of the larvae is v, where α and β are corrections for the growth rate.

<!-- b000187 | prose | pages [8] -->
In more studies it has been shown[11] that the larval growth rate of sea lampreys is primarily related to the density of edible plankton, and that if the density of plankton is ρ, then the relationship is:

<!-- b000188 | prose | pages [8] -->
v = A · eµρ + M (7)

<!-- b000189 | prose | pages [8] -->
Based on the literature [11] and related research data, we use the least squares method for parameter fitting to obtain A = −0.76, µ = −0.02, M = 0.67. The R2 = 0.9804 indicates that the fit is very good, and also shows that the growth rate of lampreys larval growth rate gradually slows down with the increase of food concentration.

<!-- b000190 | prose | pages [8] -->
Mating and spawning in lampreys usually begins after the spring migration, and their mating system is predominantly polygynous, with eggs fertilized in vitro, and the biomass of males is usually more dominant [12], which means that the birth rate of lam- preys tends to receive constraints from a smaller number of eggs. Therefore, when mea- suring the birth rate of lampreys, it is only necessary to consider the number of females during mating. Let Rmale and Rfemale be the biomass of males and females differentiated from the newborn larvae of lampreys at moment t, and c be the number of viable larvae that can be produced by one female per unit of time, then we can get the effect of sex ratio on birth rate:

<!-- b000191 | prose | pages [8] -->
Rmale = c · N1female(1 −η) (8) Rfemale = c · N1femaleη (9)

<!-- b000192 | furniture | pages [9] -->
Team # 2424371

<!-- b000193 | furniture | pages [9] -->
Page 9 of 25

<!-- b000194 | heading | pages [9] -->
4.2.3 Population Growth Model in River

<!-- b000195 | prose | pages [9] -->
According to the results of related studies [3], juvenile sea lampreys growing in rivers tend to be non-parasitic and feed mainly on tiny plankton, such as algae and small inver- tebrates. Therefore, the main consideration is the variation in the abundance of plankton and sea lampreys.

<!-- b000196 | prose | pages [9] -->
Plankton

<!-- b000197 | prose | pages [9] -->
Plankton consists mainly of phytoplankton (diatoms, green algae and cyanobacteria) and plankton (ciliates, rotifers). One part of the plankton survives by converting sun- light and carbon dioxide into organic matter through photosynthesis, and the other part survives by feeding on other plankton. Regardless of that type of survival, the growth of plankton is characterized by resource limitation and density dependence, so that its growth can be described by a logistic model. In addition to this, plankton will be preyed upon by sea lampreys, so the change in the biomass of plankton in the river can be ex- pressed as:

<!-- b000198 | prose | pages [9] -->
dP dt = rP · P · (1 −P ) −δP · (M1 + F1) (10) KP where P(t) = ρ(t)Vriver/m denotes the biomass of plankton in the river at moment t, rP denotes the growth rate of plankton, KP denotes the environmental holding capacity of plankton in the St. Lawrence River, and δP denotes the predation effect of lampreys on plankton.

<!-- b000199 | prose | pages [9] -->
Lamprey in the river

<!-- b000200 | prose | pages [9] -->
Surviving in rivers are usually juvenile lampreys and adult lampreys that migrate during the breeding season. Since adult lampreys no longer obtain food after mating and die within a short period of time, this portion of the river is present for a shorter period of time, and we ignore the effect of this portion of the river on the number of species in the river. The natural enemies of lampreys have strong food substitution, so we only consider the predation effect of natural enemies on lampreys, and do not consider the changes in the number of natural enemies. Therefore, the change in the biomass of lampreys in the river is:

<!-- b000201 | prose | pages [9] -->
dM1 = −δ1 · M1 −N2male + Rmale (11) dt dF1 dt = −δ1 · F1 −N2female + Rfemale (12)

<!-- b000202 | prose | pages [9] -->
where δ1 denotes the predation effect of human activities and other natural enemies on lampreys, the second term of the equation denotes the effect of migration from the river to the ocean, and the third term denotes the spawning effect of adult lampreys migrating from the ocean to the river.

<!-- b000203 | heading | pages [9] -->
4.2.4 Population Growth Model in Ocean

<!-- b000204 | prose | pages [9, 10] -->
Most lampreys in the ocean are adult lampreys, which basically live a parasitic life, attach- ing themselves to larger fish with their disc-like mouths and then sucking blood through their teeth and sucker-like mouth structures. Therefore, in the ocean, we mainly consider changes in the abundance of host-fish (e.g., salmon, cod, bass, etc.) and lampreys. Unlike organisms in rivers, biomass in the ocean is a ternary function of longitude, latitude, and time, so not only do we have to consider interspecific competition and parasitism among organisms, but also dispersal and enemy avoidance strategies of different species in their spatial locations.

<!-- b000205 | furniture | pages [10] -->
Team # 2424371

<!-- b000206 | furniture | pages [10] -->
Page 10 of 25

<!-- b000207 | caption | pages [10] -->
Figure 5: biological relationships of the lampreys

<!-- b000209 | prose | pages [10] -->
Host-fish

<!-- b000210 | prose | pages [10] -->
Existing studies have demonstrated that [13], parasitism may reduce host density and induce extinction of the host population. Let the biomass of host-fish be H = H(x, y, t), and divide the hosts into those that are parasitized, Hi = Hi(x, y, t), and those that are not, Hu = Hu(x, y, t), then the change in the population should be expressed as follows: Hi = Hu(x, y, t), and Hu = Hu(x, y, t). Then the change in the biomass of host-fish should be expressed as:

<!-- b000211 | prose | pages [10] -->
) −dHu −βHu(M2 + F2) + D(∂2H ∂x2 + ∂2H ∂Hu =rHH(1 −H ∂y2 ) (13) ∂t KH ∂t = βHu(M2 + F2) −(d + α)Hi + D(∂2H ∂x2 + ∂2H ∂Hi ∂y2 ) (14)

<!-- b000212 | prose | pages [10] -->
where rH denotes the growth rate of the host and KH denotes the environmental hold- ing capacity of the host-fish; in this equation, newly born fish are unparasitized individu- als, regardless of whether or not the parent is parasitized. d denotes the natural mortality rate of healthy hosts, and α denotes the effect of host mortality due to parasitism. D de- notes the dispersal efficiency, reflecting the free dispersal of fish across spatial locations.

<!-- b000213 | prose | pages [10] -->
Lamprey in the ocean

<!-- b000214 | prose | pages [10] -->
Changes in the population of lampreys in the ocean are mainly considered to be af- fected by mortality, migration and spatial dispersal caused by predation by humans or natural enemies, and the following results can be obtained:

<!-- b000215 | furniture | pages [11] -->
Team # 2424371

<!-- b000216 | furniture | pages [11] -->
Page 11 of 25

<!-- b000217 | prose | pages [11] -->
∂2M2 ∂x2 + ∂2M2  + G(∂H ∂x + ∂H Wmale = −δ2M2 −δ (t −t1) m1M2 + E ∂y ) (15) ∂y2

<!-- b000218 | prose | pages [11] -->
( if (x, y)̸ = (x0, y0) Wmale ∂M2 = (16) ∂t Wmale + N2male if (x, y) = (x0, y0)

<!-- b000219 | prose | pages [11] -->
∂2F2 ∂x2 + ∂2F2  + G(∂H ∂x + ∂H Wfemale = −δ2F2 −δ (t −t1) m1F2 + E ∂y ) (17) ∂y2

<!-- b000220 | prose | pages [11] -->
( if (x, y)̸ = (x0, y0) Wfemale ∂F2 ∂t = (18) Wfemale + N2female if (x, y) = (x0, y0)

<!-- b000221 | prose | pages [11] -->
where δ2 denotes the mortality rate of sea lampreys, E denotes the diffusion coeffi- cient of lampreys in the sea, and G denotes the tracking coefficient of sea lampreys. The first term in the expression of W denotes the effect of human activities and predation by natural enemies, the second term denotes the effect of migration of sea lampreys from the sea to the river, the third term denotes the free dispersal of sea lampreys in the sea, and the last term denotes that sea lampreys always move towards the place where there are more hosts. Synthesizing the above analysis, the above system of differential equations is plotted in the following flow chart:

<!-- b000222 | caption | pages [11] -->
Figure 6: biomass dynamics in ecosystem

<!-- b000223 | furniture | pages [12] -->
Team # 2424371

<!-- b000224 | furniture | pages [12] -->
Page 12 of 25

<!-- b000225 | heading | pages [12] -->
4.3 Model Solution

<!-- b000226 | prose | pages [12] -->
During the modeling process, many parameters to be determined were generated, and in order to determine the specific values of these parameters, we review a large num- ber of literature and online resources [13]–[16], estimation of the parameters used in the model The finite volume method(FVM) is a numerical method for solving systems of partial differential equations that transforms a continuous PDE problem into a discrete algebraic problem by discretizing the continuous solution domain into a finite number of subregions (elements), applying numerical integration in each control volume, and thus transforming the continuous PDE problem into a discrete algebraic problem.

<!-- b000227 | prose | pages [12] -->
In the modeling of different species populations over time, longitude and latitude, the waters from 59° to 63.5° W longitude and from 46° to 50.5° N latitude are equally divided into 15*15 subregions, and time is divided according to 1 day, i.e., ∆x = 0.5, ∆y = 0.5, ∆t = 1d. By programming, we obtain the distribution of host-fish at t = 360, t = 3600, t = 18000 :

<!-- b000228 | caption | pages [12] -->
Figure 7: schematic diagram of the FAM for solving PDE

<!-- b000229 | heading | pages [12] -->
4.4 Results of Problem I

<!-- b000230 | prose | pages [12] -->
In order to investigate the effect of the ability of lampreys to change sex ratio on the larger ecosystem, the changes in the abundance of different species over time are modeled when lampreys populations could and could not change their sex ratio, given the same initial value conditions. In order to make the model more general, the given initial values do not necessarily make the community in a stable state.

<!-- b000231 | prose | pages [12] -->
In the following, we set the male ratio of lampreys at p = 0.56, p = 0.67, p = 0.78, p = 0.82 at the initial moment and plot the changes of relative biomass of different species over time.

<!-- b000232 | furniture | pages [13] -->
Team # 2424371

<!-- b000233 | furniture | pages [13] -->
Page 13 of 25

<!-- b000234 | caption | pages [13] -->
Figure 8: sex ratio can be changed (left) and cannot be changed (right) at p = 0.56.

<!-- b000235 | caption | pages [13] -->
Figure 9: sex ratio can be changed (left) and cannot be changed (right) at p = 0.67.

<!-- b000236 | caption | pages [13] -->
Figure 10: sex ratio can be changed (left) and cannot be changed (right) at p = 0.78.

<!-- b000237 | caption | pages [13] -->
Figure 11: sex ratio can be changed (left) and cannot be changed (right) at p = 0.82.

<!-- b000238 | furniture | pages [14] -->
Team # 2424371

<!-- b000239 | furniture | pages [14] -->
Page 14 of 25

<!-- b000240 | prose | pages [14] -->
Based on the results above, we can get that lampreys sex ratio can change the impact on the ecosystem:

<!-- b000241 | prose | pages [14] -->
Enhance the ability of lampreys themselves to resist the harsh environment.Except for the different initial sex ratio, the initial conditions are exactly the same, and it can be seen from all the diagrams on the left that the biomass of lampreys all went through the process of decreasing and then increasing to reach a stable process after 4000-5000 days. This shows that when food resources are unfavorable for their reproduction, lampreys can resist the harsh external environment by changing their sex ratio and thus adjusting the population size.

<!-- b000242 | prose | pages [14] -->
Able to maintain the stability of the host-fish and plankton population. From the comparison of (8), it can be seen that lampreys are able to control their own overpro- liferation by changing their sex ratio when the host is insufficient, thus stabilizing the host population. From the comparison of (11), it can be seen that lampreys can restrain the overproliferation of plankton by changing the sex ratio, thus making the biomass of plankton stable.

<!-- b000243 | prose | pages [14] -->
Utilizing feedback to regulate the ecosystem. Effectively regulate the interspecies relationship of the ecosystem and maintain the stability of the ecosystem.

<!-- b000244 | prose | pages [14] -->
4.5 the Results of Problem II

<!-- b000245 | heading | pages [14] -->
4.5.1 Advantages: strong resistance to harsh environments

<!-- b000246 | prose | pages [14] -->
In order to prove that the lampreys population has a strong resistance to harsh environ- ments, the parameters in the model are adjusted to simulate the harsh environments that the lampreys might suffer in real life, so as to analyze the anti-disturbance ability of the lampreys population.

<!-- b000247 | prose | pages [14] -->
(1) Encounter natural disasters, resulting in a sudden decrease in the plankton pop- ulation. It is assumed that at t = 7000, which makes P change to 0.75P.

<!-- b000248 | caption | pages [14] -->
Figure 12: plot of biomass of different species over time(p →0.75p)

<!-- b000249 | furniture | pages [15] -->
Team # 2424371

<!-- b000250 | furniture | pages [15] -->
Page 15 of 25

<!-- b000251 | prose | pages [15] -->
It is found that the lampreys population don’t change significantly, and there is only a slight change at about 10000 days, but it recover quickly. This indicates that the lampreys population can well resist the damage caused by famine.

<!-- b000252 | prose | pages [15] -->
(2) Deterioration of the living environment or increased hunting by humans has led to an increase in the natural mortality rate of lampreys. Suppose we start from t = 6000 and adjust δ1, δ2 to become 2δ1, 2δ2.

<!-- b000253 | caption | pages [15] -->
Figure 13: plot of biomass of different species over time(δ1 →2δ1, δ2 →2δ2)

<!-- b000254 | prose | pages [15] -->
It is found that the biomass of lampreys species gradually decline after the increase in mortality rate until the new stable population reach equilibrium. This suggests that lampreys will not go extinct when their living environment deteriorates or when they are subjected to anthropogenic hunting, but will maintain a lower number of individuals to continue the reproduction.

<!-- b000255 | prose | pages [15] -->
(3)Human use of sexual inhibitors or destruction of the original habitat leads to a decrease in the fecundity of lampreys. Assuming c changes to 0.5c starting from t = 5000, the number of larvae that a female can produce per unit of time changes from c to 0.5c.

<!-- b000256 | caption | pages [15] -->
Figure 14: plot of biomass of different species over time(c →0.5c)

<!-- b000257 | furniture | pages [16] -->
Team # 2424371

<!-- b000258 | furniture | pages [16] -->
Page 16 of 25

<!-- b000259 | prose | pages [16] -->
Similar to the previous scenario, lampreys do not become extinct when fecundity is affected, but rather maintain a low number of individuals to continue the reproduction.

<!-- b000260 | heading | pages [16] -->
4.5.2 Disadvantages: time lag in adjusting the sex ratio

<!-- b000261 | prose | pages [16] -->
Observing the pictures in the model results, it can be found that although the lampreys population can reach a relatively stable state in the end, it adjusts the time slowly, and even comes close to extinction in (8). The possible reason for this is that the lampreys population only adjusts the sex ratio of fertile juvenile lampreys according to the current food density, but juvenile lampreys need to become adults before they can participate in reproduction to affect the birth rate, which has an obvious time lag effect. In the event of drastic long-term changes in the environment, lampreys are likely to become extinct due to the time lag effect and the failure to adjust the population size in a timely manner.

<!-- b000262 | heading | pages [16] -->
5 Model II : the 3-R Index Model Based on Changes of

<!-- b000263 | prose | pages [16] -->
Ecosystem Stability under the Influence of Lampreys’ Sex Ratio

<!-- b000264 | heading | pages [16] -->
5.1 Model Overview

<!-- b000265 | prose | pages [16] -->
The sex ratio of sea lampreys acts in the ecosystem and affects the stability of the ecosys- tem. Ecosystem stability refers to the ability of an ecosystem to maintain its structure and function in the face of external perturbations (e.g., natural disasters, climate change, human activities, etc.). The aim of the model in this study is to quantitatively assess this effect.

<!-- b000266 | prose | pages [16] -->
In Model I, we obtain a dynamic relationship between the sex ratio of sea lampreys and the biomass of other species in the ecosystem. Based on this, in order to measure its impact on the stability of the ecosystem, we first select the indicators used for mea- surement (3-R Index: Resistance, Resilience, Recovery) and then quantify the indicators. Then we construct the internal variable S of the ecosystem using Shannon Index [17], and further analyze the stability of the ecosystem from three aspects by establishing its relationship with the sex ratio of lampreys.

<!-- b000267 | heading | pages [16] -->
5.2 Model Buliding

<!-- b000268 | heading | pages [16] -->
5.2.1 Selection of Indicators to Measure Ecosystem Stability

<!-- b000269 | prose | pages [16] -->
Ecosystem stability refers to the ability of ecosystems to maintain their structure and function in the face of natural and anthropogenic disturbances. This stability is a key characteristic of ecosystem health and sustainability and is essential for the provision of ecosystem services (e.g., food supply, water regulation, carbon storage, etc.).Indicators of ecosystem stability include resistance, resilience, recovery, persistence, tolerance, etc.[18].

<!-- b000270 | prose | pages [16] -->
Resistance: The ability to resist changes in system variables in response to a perturba- tion.

<!-- b000271 | furniture | pages [17] -->
Team # 2424371

<!-- b000272 | furniture | pages [17] -->
Page 17 of 25

<!-- b000273 | prose | pages [17] -->
Resilience: The rate at which a system variable returns to its reference condition fol- lowing a perturbation.

<!-- b000274 | prose | pages [17] -->
Recovery: The ability to fully return to the reference condition after a perturbation.

<!-- b000275 | prose | pages [17] -->
Persistence: The length of time a system maintains a certain reference condition.

<!-- b000276 | prose | pages [17] -->
Tolerance: The ability of a system to tolerate perturbations, independent from the degree of change and the rate of return after a perturbation.

<!-- b000277 | prose | pages [17] -->
Resistance, resilience and recovery are chosen as indicators of ecosystem stability be- cause they can comprehensively reflect the response and recovery capacity of ecosystems in the face of disturbance. Resistance reflects the initial stability of an ecosystem, resilience reflects the rapid recovery ability of an ecosystem, and recovery reflects the long-term stability and adaptability of an ecosystem. Considering these three indicators together allows for a more comprehensive assessment of ecosystem stability and provides a scien- tific basis for ecological protection and environmental management.

<!-- b000278 | heading | pages [17] -->
5.2.2 Quantification of indicators

<!-- b000279 | prose | pages [17] -->
When constructing a quantitative model of an indicator, we need to follow the following points:[19]

<!-- b000280 | prose | pages [17] -->
(a) It should be dimensionless and normalized and it should be a monotonic function of stability;

<!-- b000281 | prose | pages [17] -->
(b) It should be bounded for all possible values, and no values tending to infinity can occur;

<!-- b000282 | prose | pages [17] -->
(c) It should be applicable to all types of ecosystem and system variables.

<!-- b000283 | prose | pages [17] -->
On this basis, we develop quantitative models of resistance, resilience, and recovery for system variables [18], respectively.

<!-- b000284 | prose | pages [17] -->
Resistance (Rst)

<!-- b000285 | prose | pages [17] -->
Resistance = 1 −2 × |SR −SX| (19) SR + |SR −SX|

<!-- b000286 | prose | pages [17] -->
where SR is the reference value of the system variable and SX is the value of the system variable at the standard time period X after the perturbation occurrence time tP.

<!-- b000287 | prose | pages [17] -->
Considering the stochasticity and variability of the system under study, SR should be chosen as the mean value for a longer stabilization time. For this particular period of time X, ecology often makes the assumption that SX = S0[18], where S0 is the value of the system variable at the maximum deviation from the reference value. Thus, the resistance model equation becomes

<!-- b000288 | prose | pages [17, 18] -->
Resistance = 1 −2 × |SR −S0| (20) SR + |SR −S0| Resilience(Rsl)

<!-- b000289 | furniture | pages [18] -->
Team # 2424371

<!-- b000290 | furniture | pages [18] -->
Page 18 of 25

<!-- b000292 | prose | pages [18] -->
2 × |SR −S0| |SR −S0| + |SR −SY | −1 Resilience = (21)

<!-- b000293 | prose | pages [18] -->
where SR ,S0 are as above , t0 is the time at which the maximum deviation is observed and SY is the value of the system variable after a standardised period of time Y following t0.

<!-- b000294 | prose | pages [18] -->
Recovery(Rc)

<!-- b000295 | prose | pages [18] -->
Recovery = 1 −2 × |SR −SR′| (22) SR + |SR −SR′| where SR is as above and SR′ is the value of the system variable at the reference condition after perturbation.

<!-- b000296 | caption | pages [18] -->
Figure 15: meanings of 3-R represented in the image

<!-- b000297 | prose | pages [18] -->
It is worth noting that all three of the above equations take values between -1 and 1. Resistance = 1 corresponds to no change. The closer the resistance is to 1, the better the resistance of the ecosystem. Resilience = 1 corresponds to full resilience. The closer the resilience is to 1, the more resilient the ecosystem is represented. Recovery = 1 cor- responds to its original state. The closer the recovery is to 1, the more recoverable the ecosystem is.

<!-- b000298 | heading | pages [18] -->
5.2.3 Internal system variables

<!-- b000299 | prose | pages [18, 19] -->
By solving Model I, we obtain the relationship between the sex ratio of the sea lampreys and the biomass of each species, i.e., the population growth pattern under the influence of the sex ratio of the sea lampreys, and thus analyze its influence on the stability of the ecosystem. Shannon’s index is a comprehensive diversity measure, which not only con- siders the richness of species, but also the evenness of species. This comprehensive nature makes the Shannon index more comprehensively reflect the characteristics of the ecosys- tem, and the Shannon index has the sensitivity to detect the small changes of species in the ecosystem, which can provide important information for the monitoring of the stabil- ity of the ecosystem. In this model we choose the Shannon index as the system variable S.

<!-- b000300 | furniture | pages [19] -->
Team # 2424371

<!-- b000301 | furniture | pages [19] -->
Page 19 of 25

<!-- b000303 | prose | pages [19] -->
X S = − pilog(pi) (23) i According to the conclusion of model 1, we can get the relationship between the sex ratio of sea lampreys and S = f(ρ), which is brought into the quantitative formula of the 3-R index, and we can get the effect of the sex ratio of lampreys on the ecosystem resistance, resilience, and recovery (3-R).

<!-- b000304 | heading | pages [19] -->
5.2.4 Ecosystem disturbance factors

<!-- b000305 | prose | pages [19] -->
In order to solve the effect of the sex ratio of lampreys on the ecosystem, considering a single variable, the external disturbances we chose should only change the sex ratio of lampreys. In addition to receiving genetic control, the sex ratio of lampreys can also be regulated by exogenous steroids [20], i.e., at moment tP, human intervention adopts hormones to make the sex ratio of the lampreys change, and thus study its impact on the stability of the ecosystem. We assume that the lampreys population respond immediately by changing a particular sex ratio.

<!-- b000306 | heading | pages [19] -->
5.3 Results of Problem III

<!-- b000307 | prose | pages [19] -->
On the basis of model I, we make the perturbation of exogenous steroids to the ecosystem at Day=5115, and get the changes of biomass of each species, and from that, we calculate its Shannon index, and the results are presented in the following graph:

<!-- b000308 | caption | pages [19] -->
Figure 16: Shannon Index and biomass of each species over time

<!-- b000309 | prose | pages [19] -->
We took the change in male sex ratio,∆p, as the independent variable, and the resulting 3-R indicator calculated to measure ecosystem stability as the dependent variable, and the results are presented in the figure below.

<!-- b000310 | furniture | pages [20] -->
Team # 2424371

<!-- b000311 | furniture | pages [20] -->
Page 20 of 25

<!-- b000312 | caption | pages [20] -->
Figure 17: 3-R Index - ∆p

<!-- b000313 | prose | pages [20] -->
According to the results, we can see that the sex ratio of sea lampreys has little effect on the recovery of the ecosystem (Rc), while the effect on the resilience of the ecosystem (Rsl) is relatively large, and from the general trend, we can see that the resilience of the sea lampreys is greater when there is a higher proportion of males in the population, while the resistance (Rst) slightly decreases, which is a result of the unique characteristics of the life cycle of the sea lampreys, the resistance of the environment to disturbances. This is a result of the unique life cycle characteristics of the sea lamprey, its resistance to environmental disturbance, and its ecological niche in the ecosystem. Environmental influences that result in a higher proportion of males also affect the reproductive capacity of lampreys populations, reflecting the interactions and adaptations between the species and the ecosystem, a complex feedback mechanism that not only reveals the dynamics within the species, but is also essential for maintaining the diversity of a complex and diverse ecosystem.

<!-- b000314 | heading | pages [20] -->
6 Model Expansion

<!-- b000315 | prose | pages [20] -->
In Model 1, we have discussed the effects of the sex ratio of lampreys on the ecosystem. Now, we are going to put two more different organisms into the ecosystem and explore whether the sex ratio of lampreys provides some benefits to them. The two organisms being considered are:

<!-- b000316 | prose | pages [20] -->
• A species of parasite, denoted A, which is in a competitive relationship with lam- preys, and both parasitize the same host. • A species of fish, denoted B, which is the main source of food for the host-fish.

<!-- b000317 | prose | pages [20] -->
We construct the food web of the ecosystem in which the lampreys are located, as shown in Figure (18):

<!-- b000318 | prose | pages [20, 21] -->
Now we can analyze their interactions more completely. Since we introduce the para- site A and the fish B, we need to consider the competition between A and lampreys, the parasitism of A on the host, and the predation of B by the host, and build the correspond- ing differential equations. For the sake of space, the specific formulas will not be listed here. At the same time, we artificially reduce the female proportion of juvenile lampreys during the period of 8000 ≤t ≤9000, and investigate the role of sex ratio change on parasite A and fish B through this perturbation. Specific results are shown in Figure (19).

<!-- b000319 | furniture | pages [21] -->
Team # 2424371

<!-- b000320 | furniture | pages [21] -->
Page 21 of 25

<!-- b000321 | caption | pages [21] -->
Figure 18: the food web of the ecosystem in which the lampreys are located

<!-- b000323 | caption | pages [21] -->
Figure 19: plot of biomass of different species over time(5 species)

<!-- b000324 | prose | pages [21, 22] -->
As can be seen on the graph, initially, due to the interference of external factors, lam- preys bring themselves into balance by changing their sex ratio. In the decreasing stage, the competitive pressure from the parasites is reduced, which allows for more resources to be accessed, which in turn increases the biomass. In the rising stage, the host-fish is more affected and has a lower biomass. In turn, the probability of predation will decrease, thus favoring fish B. And a similar conclusion can be obtained from the graph after arti- ficially altering the sex ratio of the larvae. Therefore, we can argue that variable sex ratio in the lamprey population offer advantages to parasite A and fish B to some extent.

<!-- b000325 | furniture | pages [22] -->
Team # 2424371

<!-- b000326 | furniture | pages [22] -->
Page 22 of 25

<!-- b000328 | heading | pages [22] -->
7 Sensitivity Analysis

<!-- b000329 | prose | pages [22] -->
During the modeling process, we have verified (see 5.3) that when the ecosystem is in a period of stabilization and the sex ratio of lampreys is perturbed on a small scale, the ecosystem can be allowed to equilibrate the interspecific relationship through its own strong resistance. Therefore, the sex ratio p of lampreys is relatively stable.

<!-- b000330 | prose | pages [22] -->
On the other hand, the growth rate rH of the host-fish is more sensitive, and its per- turbation may bring larger impacts to the whole ecosystem. In our model, rH = 0.026 , and in the following, we will increase and decrease rH respectively to observe its ef- fect on the ecosystem. In order to concisely illustrate the relationship between sex ratio, lampreys population, plankton biomass and host fish, the effects of parasite A and fish B on the system are not considered here for the time being. rH increases: we consider (k = 0, 1, 2, · · · , 7)scenarios and count the Shannon index of the the rH = 0.03 + 0.01k ecosystems separately, as shown in table (2):

<!-- b000331 | caption | pages [22] -->
Table 2: Shannon Index corresponding to different rH

<!-- b000332 | prose | pages [22] -->
rH 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1

<!-- b000333 | prose | pages [22] -->
1.0344 0.9631 0.9377 0.9283 0.9187 0.9096 0.9044 0.8998 Shannon Index/nat

<!-- b000334 | prose | pages [22] -->
From the above table, it can be seen that the Shannon index of the system is gradually decreasing as rH increases. In other words, the diversity of the ecosystem is decreasing. Figure (7) gives a graph of the relationship between species whenrH = 0.1. It can be seen from the figure that when the system reaches stability, the biomass of host-fish has been in a state close to the environmental capacity. This is mainly due to the drastic perturbation in the initial stage that let to a sudden decrease in lampreys as well as a sudden increase in host-fish, which eventually reach equilibrium through a series of interactions.

<!-- b000335 | prose | pages [22] -->
Decrease in rH: When rH decreases, a slowdown in host-fish growth may lead to an insufficient supply of food for lampreys, which in turn may lead to a disruption of the system equilibrium. We investigate the maximum number of days that the ecosystem could be sustained when rH = 0.02 + 0.001k(k = 0, 1, 2, · · · 5), as shown in Table (3):

<!-- b000336 | caption | pages [22] -->
Table 3: Time of ecosystem collapse corresponding to different rH

<!-- b000337 | prose | pages [22] -->
rH 0.02 0.021 0.022 0.023 0.024 0.025

<!-- b000338 | prose | pages [22, 23] -->
488 1736 3158 6225 > 24000 > 24000 Time of ecosystem collapse/day plot of biomass of different time(rH = 0.02) species over time(rH = 0.1)

<!-- b000339 | furniture | pages [23] -->
Team # 2424371

<!-- b000340 | furniture | pages [23] -->
Page 23 of 25

<!-- b000341 | caption | pages [23] -->
Figure 20: plot of ecosystem collapse over

<!-- b000342 | caption | pages [23] -->
Figure 21:

<!-- b000344 | heading | pages [23] -->
8 Strengths and Weaknesses

<!-- b000345 | heading | pages [23] -->
8.1 Strengths

<!-- b000346 | prose | pages [23] -->
• Modeling according to the complex life cycle of sea lampreys is close to the real life course of sea lampreys.

<!-- b000347 | prose | pages [23] -->
• The partial differential equation model is a natural description of the multivariate system, which can accurately represent the changes of the species. And it has great advantages in studying the initial sex ratio and the influence of special disturbing ground in the system.

<!-- b000348 | prose | pages [23] -->
• The numerical solution of the partial differential equation is solved by the finite vol- ume method, which simplifies the time complexity of the model solution, is highly efficient, and has a fast solution speed.

<!-- b000349 | prose | pages [23] -->
• Multiple quantifiable indicators are chosen to innovatively measure ecosystem sta- bility. When considering the influence of gender ratio on ecosystem stability, it can comprehensively measure the anti-disturbance ability and recovery ability of the ecosystem in the face of adverse environment, and show the long-term impact on the ecosystem.

<!-- b000350 | heading | pages [23] -->
8.2 Weaknesses and Possible Improvement

<!-- b000351 | prose | pages [23] -->
• Due to the complex interactions between organisms in ecosystems, it is difficult for us to analyze the interactions between all species, and we can only select specific species for analysis.

<!-- b000352 | prose | pages [23] -->
• In the online literature and related resources, we get less data related to lampreys species, so we had difficulty in obtaining more accurate and stable initial values, and the parameter estimates may not be precise enough.

<!-- b000353 | furniture | pages [24] -->
Team # 2424371

<!-- b000354 | furniture | pages [24] -->
Page 24 of 25

<!-- b000355 | heading | pages [24] -->
9 Conclusion

<!-- b000356 | prose | pages [24] -->
This paper combines the Population Growth Model Induced by Lampreys Sex Ratio and the 3-R Model Based on Changes of Ecosystem Stability under the Influence of Lampreys’ Sex Ratio , and obtain the following results:

<!-- b000357 | prose | pages [24] -->
• When the lamprey can change the sex ratio through food concentration, he can ad- just the population size and enhance the lamprey’s ability to withstand harsh envi- ronments. When the biomass of hosts is insufficient, lampreys can control their own reproduction, thus stabilising the biomass of hosts; when the biomass of plankton is too high, lampreys can inhibit the excessive biomass of plankton, thus stabilising the number of plankton. In conclusion, lampreys regulate the ecosystem through feed- back by changing the sex ratio, effectively regulating the biomass of species in the ecosystem.

<!-- b000358 | prose | pages [24] -->
• The advantage of the lampreys population is that it has strong resistance to external disturbances, while the disadvantage is that there is an obvious time lag in the pro- cess of adjusting the birth rate and the biomass of species in the lampreys population.

<!-- b000359 | prose | pages [24] -->
• The sex ratio of sea lampreys has little effect on ecosystem recovery (Rc), while it has a relatively large effect on ecosystem resilience (Rsl). When sea lampreys had a higher proportion of males in their population, they are more resilient, while resistance (Rst) decrease slightly.

<!-- b000360 | prose | pages [24] -->
• Sea lampreys that can change sex ratio are able to create favorable factors for para- sites that compete with them, and for host food.

<!-- b000361 | heading | pages [24] -->
References

<!-- b000362 | references | pages [24] -->
[1]

<!-- b000363 | references | pages [24] -->
M. F. Docker, J. B. Hume, and B. J. Clemens, “Introduction: A surfeit of lampreys,”

<!-- b000364 | references | pages [24] -->
Lampreys: Biology, Conservation and Control: Volume 1, pp. 1–34, 2015.

<!-- b000365 | references | pages [24] -->
B. J. Clemens, H. Arakawa, C. Baker, et al., “Management of anadromous lampreys:

<!-- b000366 | references | pages [24] -->
[2]

<!-- b000367 | references | pages [24] -->
Common threats, different approaches,” Journal of Great Lakes Research, vol. 47, S129–

<!-- b000368 | references | pages [24] -->
S146, 2021.

<!-- b000369 | references | pages [24] -->
[3]

<!-- b000370 | references | pages [24] -->
M. F. Docker and I. C. Potter, “Life history evolution in lampreys: Alternative mi-

<!-- b000371 | references | pages [24] -->
gratory and feeding types,” in Lampreys: Biology, Conservation and Control: Volume 2,

<!-- b000372 | references | pages [24] -->
Springer, 2019, pp. 287–409.

<!-- b000373 | references | pages [24] -->
[4]

<!-- b000374 | references | pages [24] -->
F. L. Kelly and J. J. King, “A review of the ecology and distribution of three lamprey

<!-- b000375 | references | pages [24] -->
species, lampetra fluviatilis (l.), lampetra planeri (bloch) and petromyzon marinus

<!-- b000376 | references | pages [24] -->
(l.): A context for conservation and biodiversity considerations in ireland,” in biology

<!-- b000377 | references | pages [24] -->
and environment: Proceedings of the Royal Irish Academy, JSTOR, 2001, pp. 165–185.

<!-- b000378 | references | pages [24] -->
V. C. Applegate, Natural history of the sea lamprey, Petromyzon marinus, in Michigan.

<!-- b000379 | references | pages [24] -->
[5]

<!-- b000380 | references | pages [24] -->
University of Michigan, 1950.

<!-- b000381 | references | pages [24] -->
C. C. Robusto, “The cosine-haversine formula,” The American Mathematical Monthly,

<!-- b000382 | references | pages [24] -->
[6]

<!-- b000383 | references | pages [24] -->
vol. 64, no. 1, pp. 38–40, 1957.

<!-- b000384 | furniture | pages [25] -->
Team # 2424371

<!-- b000385 | furniture | pages [25] -->
Page 25 of 25

<!-- b000386 | references | pages [25] -->
[7]

<!-- b000387 | references | pages [25] -->
D. R. Lean, “Some secrets of a great river: An overview of the st. lawrence river

<!-- b000388 | references | pages [25] -->
supplement,” Canadian Journal of Fisheries and Aquatic Sciences, vol. 57, no. S1, pp. 1–

<!-- b000389 | references | pages [25] -->
6, 2000.

<!-- b000390 | references | pages [25] -->
[8]

<!-- b000391 | references | pages [25] -->
J. V. Adams and M. L. Jones, “Estimation of lake-scale stock-recruitment models

<!-- b000392 | references | pages [25] -->
for great lakes sea lampreys,” Ecological Modelling, vol. 467, p. 109 916, 2022, ISSN:

<!-- b000393 | references | pages [25] -->
0304-3800. DOI: https://doi.org/10.1016/j.ecolmodel.2022.109916.

<!-- b000394 | references | pages [25] -->
[Online]. Available: https://www.sciencedirect.com/science/article/

<!-- b000395 | references | pages [25] -->
pii/S0304380022000394.

<!-- b000396 | references | pages [25] -->
[9]

<!-- b000397 | references | pages [25] -->
D. Pavlov, D. Y. Nazarov, A. Zvezdin, and A. Kucheryavyi, “Downstream migra-

<!-- b000398 | references | pages [25] -->
tion of early larvae of the european river lamprey lampetra fluviatilis,” in Doklady

<!-- b000399 | references | pages [25] -->
Biological Sciences, Springer Nature BV, vol. 459, 2014, p. 344.

<!-- b000400 | references | pages [25] -->
[10]

<!-- b000401 | references | pages [25] -->
N. S. Johnson, W. D. Swink, and T. O. Brenden, “Field study suggests that sex deter-

<!-- b000402 | references | pages [25] -->
mination in sea lamprey is directly influenced by larval growth rate,” Proceedings of

<!-- b000403 | references | pages [25] -->
the Royal Society B: Biological Sciences, vol. 284, no. 1851, p. 20 170 262, 2017.

<!-- b000404 | references | pages [25] -->
[11]

<!-- b000405 | references | pages [25] -->
J. Mallatt, “Laboratory growth of larval lampreys (lampetra (entosphenus) triden-

<!-- b000406 | references | pages [25] -->
tata richardson) at different food concentrations and animal densities,” Journal of

<!-- b000407 | references | pages [25] -->
Fish Biology, vol. 22, no. 3, pp. 293–301, 1983.

<!-- b000408 | references | pages [25] -->
N. S. Johnson, T. J. Buchinger, and W. Li, “Reproductive ecology of lampreys,” Lam-

<!-- b000409 | references | pages [25] -->
[12]

<!-- b000410 | references | pages [25] -->
preys: Biology, Conservation and Control: Volume 1, pp. 265–303, 2015.

<!-- b000411 | references | pages [25] -->
[13]

<!-- b000412 | references | pages [25] -->
D. Ebert, M. Lipsitch, and K. L. Mangin, “The effect of parasites on host population

<!-- b000413 | references | pages [25] -->
density and extinction: Experimental epidemiology with daphnia and six micropar-

<!-- b000414 | references | pages [25] -->
asites,” The American Naturalist, vol. 156, no. 5, pp. 459–477, 2000.

<!-- b000415 | references | pages [25] -->
[14]

<!-- b000416 | references | pages [25] -->
J. V. Adams and M. L. Jones, “Estimation of lake-scale stock-recruitment models for

<!-- b000417 | references | pages [25] -->
great lakes sea lampreys,” Ecological Modelling, vol. 467, p. 109 916, 2022.

<!-- b000418 | references | pages [25] -->
[15]

<!-- b000419 | references | pages [25] -->
L. A. Weitkamp, S. A. Hinton, and P. J. Bentley, “Seasonal abundance, size, and host

<!-- b000420 | references | pages [25] -->
selection of western river (lampetra ayresii) and pacific (entosphenus tridentatus)

<!-- b000421 | references | pages [25] -->
lampreys in the columbia river estuary.,” Fishery Bulletin, vol. 113, no. 2, 2015.

<!-- b000422 | references | pages [25] -->
[16]

<!-- b000423 | references | pages [25] -->
P. J. Manion and L. H. Hanson, “Spawning behavior and fecundity of lampreys

<!-- b000424 | references | pages [25] -->
from the upper three great lakes,” Canadian Journal of Fisheries and Aquatic Sciences,

<!-- b000425 | references | pages [25] -->
vol. 37, no. 11, pp. 1635–1640, 1980.

<!-- b000426 | references | pages [25] -->
P. Fedor and M. Zvarıková, “Biodiversity indices,” Encycl. Ecol, vol. 2, pp. 337–346,

<!-- b000427 | references | pages [25] -->
[17]

<!-- b000428 | references | pages [25] -->
2019.

<!-- b000429 | references | pages [25] -->
[18]

<!-- b000430 | references | pages [25] -->
K. Van Meerbeek, T. Jucker, and J.-C. Svenning, “Unifying the concepts of stability

<!-- b000431 | references | pages [25] -->
and resilience in ecology,” Journal of Ecology, vol. 109, no. 9, pp. 3114–3132, 2021.

<!-- b000432 | references | pages [25] -->
[19]

<!-- b000433 | references | pages [25] -->
K. H. Orwin and D. A. Wardle, “New indices for quantifying the resistance and

<!-- b000434 | references | pages [25] -->
resilience of soil biota to exogenous disturbances,” Soil Biology and Biochemistry,

<!-- b000435 | references | pages [25] -->
vol. 36, no. 11, pp. 1907–1912, 2004.

<!-- b000436 | references | pages [25] -->
[20]

<!-- b000437 | references | pages [25] -->
R. H. Devlin and Y. Nagahama, “Sex determination and sex differentiation in fish:

<!-- b000438 | references | pages [25] -->
An overview of genetic, physiological, and environmental influences,” Aquaculture,

<!-- b000439 | references | pages [25] -->
vol. 208, no. 3-4, pp. 191–364, 2002.
