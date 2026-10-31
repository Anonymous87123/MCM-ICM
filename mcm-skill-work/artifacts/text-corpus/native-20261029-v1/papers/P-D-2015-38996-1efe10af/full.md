# P-D-2015-38996-1efe10af

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | prose | pages [1] -->
38996

<!-- b000007 | prose | pages [1] -->
T1 ________________

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | prose | pages [1] -->
T2 ________________

<!-- b000010 | prose | pages [1] -->
F1 ________________

<!-- b000011 | prose | pages [1] -->
F2 ________________

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T3 ________________

<!-- b000014 | prose | pages [1] -->
F3 ________________

<!-- b000015 | title | pages [1] -->
D

<!-- b000016 | prose | pages [1] -->
T4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | prose | pages [1] -->
F4 ________________

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | prose | pages [1] -->
2015 Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

<!-- b000021 | prose | pages [1] -->
Sustainable Development Evaluation System

<!-- b000022 | heading | pages [1] -->
Summary

<!-- b000023 | prose | pages [1] -->
Sustainable development has attracted plenty of attention from all over the word for recent decades. While the definition of sustainable development is very comprehensive.

<!-- b000024 | prose | pages [1] -->
To evaluate sustainability of a country, devise an evaluation model for sustainable development. Based on our analysis of sustainable development, we depart the meaning of sustainable development into two dimension: social-economic development and environment- resource development. We design the index system by expanding ecological footprint into our model, and then we invoke entropy evaluation method and the subject-object weighting method based on CRITIC to derive the calculation process of two overall indices. By scaling the indices in coordinate system and calculate the direction by regression analysis, we devise the harmonious development (included angle between actual development direction and ideal development direction) and valid development (projection of actual development on standard development pattern) of a country to evaluate the sustainability thought two aspects. Their product, a hyperbolic sustainable distance, is the final result of our model, which represent the hyperbolic distance between the current development and goal development point. We show an implementation of our model that takes America, China, France, Nepal and South Africa as example. It turns out that America, France (the Best one) and South Africa are all sustainable, while the others are not. We also compare our model with other possible approaches, which turns out that our model is more appropriate for sustainable development.

<!-- b000025 | prose | pages [1] -->
We choose Nepal in our further investigation, where we invoke ARIMA model to forecast without intervention and system dynamics to forecast with intervention. Because of the limited data resources, we estimate the parameters of structure equations in each subsystem by Three-Stage Least Squares method, then we list the exact formulas of dynamic equations. After exploring the current development situation and geological characteristics of Nepal, we utilize sensitivity analysis and our forecast results to propose a sustainable development plan for Nepal, among which modernization program performs best according to our system- dynamics simulation results.

<!-- b000026 | prose | pages [1] -->
Finally, we discuss the strengths and weaknesses of our model.

<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [2] -->
Page 1 of 20

<!-- b000029 | furniture | pages [2] -->
Team # 38996

<!-- b000030 | furniture | pages [2] -->


<!-- b000031 | heading | pages [2] -->
Contents

<!-- b000032 | contents | pages [2] -->
1. Introduction ............................................................................................................................... 2

<!-- b000033 | contents | pages [2] -->
1.1. Background ................................................................................................................... 2

<!-- b000034 | contents | pages [2] -->
1.2. Our Work ........................................................................................................................ 2

<!-- b000035 | contents | pages [2] -->
2. Assumption ................................................................................................................................ 3

<!-- b000036 | contents | pages [2] -->
3. Sustainability of a Country and Policy ............................................................................. 4

<!-- b000037 | contents | pages [2] -->
3.1. Analysis of Sustainable Development ................................................................. 4

<!-- b000038 | contents | pages [2] -->
3.2. Ecological Footprint ................................................................................................... 5

<!-- b000039 | contents | pages [2] -->
3.2.1. Calculation ......................................................................................................... 5

<!-- b000040 | contents | pages [2] -->
3.2.2. Discussion on EF Model ............................................................................... 5

<!-- b000041 | contents | pages [2] -->
3.3. The Model ...................................................................................................................... 6

<!-- b000042 | contents | pages [2] -->
3.3.1. Index System .................................................................................................... 6

<!-- b000043 | contents | pages [2] -->
3.3.2. Sustainability Measurement ....................................................................... 8

<!-- b000044 | contents | pages [2] -->
3.3.3. An Implementation of Our model .......................................................... 10

<!-- b000045 | contents | pages [2] -->
3.3.4. Further Discussion ....................................................................................... 12

<!-- b000046 | contents | pages [2] -->
4. Sustainability Development Plan .................................................................................... 13

<!-- b000047 | contents | pages [2] -->
4.1. Current Situation and Forecast without intervention................................. 13

<!-- b000048 | contents | pages [2] -->
4.2. Details of the Plan ..................................................................................................... 14

<!-- b000049 | contents | pages [2] -->
4.2.1. Effectiveness Judgment by Sensitivity Analysis ................................ 14

<!-- b000050 | contents | pages [2] -->
4.2.2. Reasonability Judgment by Actual Conditions .................................. 15

<!-- b000051 | contents | pages [2] -->
4.2.3. Ultimate Plan for Sustainable development ....................................... 15

<!-- b000052 | contents | pages [2] -->
5. Dynamic Improvement ........................................................................................................ 16

<!-- b000053 | contents | pages [2] -->
5.1. System Dynamics and Structure Equations .................................................... 16

<!-- b000054 | contents | pages [2] -->
5.2. Simulation Run and Results .................................................................................. 18

<!-- b000055 | contents | pages [2] -->
5.3. Conclusion.................................................................................................................... 19

<!-- b000056 | contents | pages [2] -->
6. Analysis of the Model ........................................................................................................... 19

<!-- b000057 | contents | pages [2] -->
6.1. Strengths ...................................................................................................................... 19

<!-- b000058 | contents | pages [2] -->
6.2. Weaknesses ................................................................................................................. 20

<!-- b000059 | contents | pages [2] -->
References ......................................................................................................................................... 20

<!-- b000060 | furniture | pages [2] -->


<!-- b000061 | furniture | pages [2] -->


<!-- b000062 | furniture | pages [2] -->


<!-- b000063 | furniture | pages [2] -->


<!-- b000064 | furniture | pages [3] -->
Page 2 of 20

<!-- b000065 | furniture | pages [3] -->
Team # 38996

<!-- b000066 | furniture | pages [3] -->


<!-- b000067 | heading | pages [3] -->
1. Introduction

<!-- b000068 | heading | pages [3] -->
1.1. Background

<!-- b000069 | prose | pages [3] -->
Broadly speaking, Defined by the 1987 Brundtland Report Our Common World [1], sustainable development meets the needs of the present without compromising the ability of future generations to meet their own needs. Sustainable development can we developed into various aspect such as nature, society, ecology, policy and so on. To be specific, sustainable development is to balance the development of nature, society, ecology, population and economy.

<!-- b000070 | prose | pages [3] -->
In terms of the profound definition of sustainable development, scientist have already come up with some essential principal of sustainable develop, and they are principal of equality, principal of sustainability and principal of commonality. The principal of equality refers to the fair and equitable resources between generations, intergenerational equity allocation and utilization. While the principal of sustainability indicates that economic and social development of mankind cannot exceed the carrying capacity of resources and the environment. And the principal of commonality represents that although national sustainable development patterns are different, the principles of equality and sustainability are common.

<!-- b000071 | prose | pages [3] -->
Unfortunately, many developing countries are suffering from the unsustainable development as they lack sufficient international aids and technological path pattern to cope with the intense contradiction between the pressing needs of contemporary citizens and the responsibility of protecting the environment. Meanwhile, numerous international organizations do not equip with scientific enough methods to evaluate the sustainability of each country. Nor can they efficiently figure out which country is most worth providing aids to.

<!-- b000072 | prose | pages [3] -->
The International Conglomerate of Money (ICM) wants to use their extensive financial resources and influence to create a more sustainable world. They are particularly interested in developing countries, where they believe they can see the greatest results of their investments.

<!-- b000073 | heading | pages [3] -->
1.2. Our Work

<!-- b000074 | prose | pages [3] -->
We devise a mathematical model to measure the sustainability of given countries and policy after analyzing the concept of sustainable development. To be specific, we invoke the emergy based ecological footprint in our model after finding its drawbacks while measuring the sustainability of a country. Then we design a new evaluation system to perfect the objects that have been taken into consider. We also show our model results in a coordinate system so that they can be understood by any people who are interested in the issue but do not equip with much background knowledge. The model can tell when and how a country is sustainable or unsustainable explicitly. We also have some further discussion on approaches to sharpen our model.

<!-- b000075 | furniture | pages [3] -->


<!-- b000076 | furniture | pages [4] -->
Page 3 of 20

<!-- b000077 | furniture | pages [4] -->
Team # 38996

<!-- b000078 | furniture | pages [4] -->


<!-- b000079 | prose | pages [4] -->
Having devised a model for sustainability, we investigate Nepal from 48 LDC list. We first explore the current situation of Nepal by means of non-interference prediction with ARIMA model. Base on the results we derived from the analysis, we propose a 20-year sustainable development plan for Nepal, and the plan includes programs, policies, and a direction that indicates what ICM should do according to a specific state within Nepal.

<!-- b000080 | prose | pages [4] -->
We eventually devise a dynamic version of our model for the purpose to forecast the effect of each program and policy. The improved model comes back to the previous one if no programs or policies are carried out. We run the simulation each program and policy and draw the conclusion about which suggestions we had given are the highly effective strategies to be implemented by ICM.

<!-- b000081 | prose | pages [4] -->
Finally, we test the sensitivity of our model and discuss the strengths and weakness of our model.

<!-- b000082 | heading | pages [4] -->
2. Assumption

<!-- b000083 | prose | pages [4] -->
The consumption of resources and production of waste are determined and can  be measured by statistic method. As the consumption of resources and production of waste includes countless details which is hard to measure accurately, and the main purpose of our model is to measure the sustainability of a country or policy instead of measuring the explicit statistic data.

<!-- b000084 | prose | pages [4] -->
The country measured is relatively stable. That is to say, extremely dramatic  change does not happen in the chosen country while we are measuring its sustainability. For example, devastating natural disasters and devastating war which might possibly exterminate the country will not be taken into consideration.

<!-- b000085 | prose | pages [4] -->
The economic state, demographics, resource consumption data and  environment data of each the chosen country is available. The complicated situations in all developing country make it impracticable to investigate one by one, so we mainly focus on using these data to estimate whether a country is sustainably developing.

<!-- b000086 | prose | pages [4] -->
The statistical data is valid. We suppose that the true value of every index locates  right nearby the statistic data. Consequently, we assume that the data is believable.

<!-- b000087 | prose | pages [4] -->
The operating property and mechanism of a country is relatively independent  from others. We hypothesize that every country all over the world respects the state sovereignty each other. In another word, the institutional structure and the operating mechanism within each country depends on the country itself only and will not be interfered by others. It is because every country has its sovereignty to determine which economic structure or political system to implement. And the inner political and economic structure will, to a great extent, determines various economic operating property and mechanism.

<!-- b000088 | furniture | pages [4] -->


<!-- b000089 | furniture | pages [5] -->
Page 4 of 20

<!-- b000090 | furniture | pages [5] -->
Team # 38996

<!-- b000091 | furniture | pages [5] -->


<!-- b000092 | heading | pages [5] -->
3. Sustainability of a Country and Policy

<!-- b000093 | heading | pages [5] -->
3.1. Analysis of Sustainable Development

<!-- b000094 | prose | pages [5] -->
Sustainable development should takes care of two basic concepts: the contemporary people’s need and their descendants’ ability to meet their needs. To meet the requirement, we should economize natural resource, protect the environment and develop our society and economic at the same time. What is more important is to keep these aspects in a relatively balanced relation and position. Only if we succeed in balance them all, can we satisfy contemporary needs without depriving our offspring of their ability to meet their needs in the future, and make sure of the development of our posterity without sacrificing contemporary social and economic development. In a word, three dimensions of human development (economic, society, and environment) should develop in a balance state.

<!-- b000095 | prose | pages [5] -->
Recall the fishing model which derives an ideal point of fishing amount. At this point, the fish will keep reproducing at a highest rate so that the entire fishing industry can keep doing so for a long time. We can actually regard this point as a situation that meets a sustainable development. It is because both contemporary people’s needs and the interest of their posterity are satisfied as much as possible. That is to say, with the highest reproduction of fish, people can get most amount of fish from fishing, and the entire ecosystem is protect from ecological degradation. In another word, the fish ecosystem and fishing economic (which fosters and flourishes social development) keeps a balance relationship. We can also say the three dimensions meet an equilibrium state at this good point.

<!-- b000096 | prose | pages [5] -->
It is, however, very hard to find this balanced point in reality. We can merely describe this situation in a fuzzy word. Therefore, we must clarify some main factors that typically contribute to these three dimensions.

<!-- b000097 | prose | pages [5] -->
To start with, we explore social development of a country. It is clear that the population (including gross, density, and rate of change), public service (including medical treatment and public health, telecom service, transport service, etc.), and culture (including education, science, and technology) all contribute to level of social development. The higher level of the public service and culture, the better social development, while the population is a crucial control variate that provides the average level of these two components above.

<!-- b000098 | prose | pages [5] -->
We also seek principal factors that represent the development of social economy, which is the foundation of social development. We invoke some basic results of economics, and we figure the principal elements as follow: Gross Domestic Product, added value of agriculture, industry (including heavy industry, manufacture, service, and investment), laboring population, technology and so on. The more prosperous these elements are, the better a country’s economy is.

<!-- b000099 | prose | pages [5] -->
Last but not least, we will discuss some variates that can well indicate the level of environment and natural resources consumption in Section 3.2 in detail.

<!-- b000100 | furniture | pages [5] -->


<!-- b000101 | furniture | pages [6] -->
Page 5 of 20

<!-- b000102 | furniture | pages [6] -->
Team # 38996

<!-- b000103 | furniture | pages [6] -->


<!-- b000104 | prose | pages [6] -->
Now we are discussing the relation between these aspects of a country’s development and sustainability. In terms of two meanings of sustainable development, we divide these aspects into two parts respectively. What calls for special attention is that the division is not absolutely clear, and we devise the division only for explanation purpose. For contemporary people, the essential needs are to promote the culture and boom the production as much and fast as possible, which can be explained by social and economy development. As for posterity, the amount of remained natural resources and the friendliness of environment at that time would definitely determine their ability to meet their needs.

<!-- b000105 | heading | pages [6] -->
3.2. Ecological Footprint

<!-- b000106 | prose | pages [6] -->
Ecological footprint (EF) is originally proposed by Rees (1992) and improved by Wackernagel [2] to measure the sustainability. According to the thought of ecological footprint, every individual or group of units can consume natural resources and produce waste back into ecology system. The natural resources consumption and produced waste can be converse into biologically productive area. Subtracting appropriated carrying capacity, the positive result indicates sustainable development while the negative one means the development is unsustainable and the ecology is in a deficit state (ecological deficit).

<!-- b000107 | prose | pages [6] -->
3.2.1.

<!-- b000108 | prose | pages [6] -->
Calculation

<!-- b000109 | prose | pages [6] -->
The computational formula of ecological footprint is

<!-- b000110 | prose | pages [6] -->
𝐸𝐹= 𝑁× 𝑑𝑓= ∑𝑟𝑗× 𝐴𝑖= ∑𝑟𝑗× 𝑃𝑖−𝐼𝑖−𝐸𝑖

<!-- b000111 | prose | pages [6] -->
, (𝑗= 1,2, … ) 𝑌𝑖× 𝑁

<!-- b000112 | prose | pages [6] -->
where 𝐸𝐹is ecological footprint; 𝑒𝑓 is per capita ecological footprint; 𝑖 is consumption item; 𝑌𝑖 is per capita biologically productive area’s output for item 𝑖 per annum; 𝐴𝑖 is the conversed per capita biological productive area’s output for item 𝑖 per annum; 𝑃𝑖 is the production amount of item 𝑖 per annum; 𝐼𝑖 is the import volume of item 𝑖; 𝐸𝑖 is the export volume of item 𝑖; 𝑁 is population; and 𝑟𝑗 is balance factor.

<!-- b000113 | prose | pages [6] -->
The computational formula of appropriated carrying capacity is

<!-- b000114 | prose | pages [6] -->
𝐸𝐶= 𝑁× 𝑒𝑐= 𝑎𝑗× 𝑟𝑗× 𝑦𝑗, (𝑗= 1,2, … ) where 𝐸𝐶 is total appropriated carrying capacity; 𝑒𝑐 is per capita EC; 𝑎𝑗 is per capita biologically productive area; 𝑟𝑗 is equivalence factor; 𝑦𝑖 is productive factor.

<!-- b000115 | prose | pages [6] -->
Let 𝐴= 𝐸𝐹−𝐸𝐶, then EF model evaluates the sustainability by value of 𝐴. If 𝐴< 0, then the country is sustainable, otherwise unsustainable.

<!-- b000116 | prose | pages [6] -->
3.2.2.

<!-- b000117 | heading | pages [6] -->
Discussion on EF Model

<!-- b000118 | prose | pages [6] -->
 The balance factor lacks enough explanation

<!-- b000119 | prose | pages [6] -->
From the computational formula, we find that the balancing factor represents ratio of the productivity of a certain biologically productive area to overall average productivity

<!-- b000120 | furniture | pages [6] -->


<!-- b000121 | furniture | pages [7] -->
Team # 38996

<!-- b000122 | furniture | pages [7] -->
Page 6 of 20

<!-- b000123 | furniture | pages [7] -->


<!-- b000124 | furniture | pages [7] -->


<!-- b000125 | prose | pages [7] -->
biologically productive area. That means different type of land with similar balance factor can replace each other. What’s more, the balance factors are constant which is obviously irrational.

<!-- b000126 | prose | pages [7] -->
 The calculation of EF may be extremely hard and may lead to huge error

<!-- b000127 | prose | pages [7] -->
For example, EF model converts the consumption of fossil fuel into the area that can absorb the CO2 produced by burning them. However, the waste gas produced while burning the fossil fuel is not merely limited to carbon dioxide, and SO2 is another important pollutant that cannot be neglected.

<!-- b000128 | prose | pages [7] -->
In order to make the computational process more accurate, we can invoke the thought of emergy analysis. Emergy analysis theory is original proposed by H. T. Odum (1988) [3] and its main idea is to converse every items considered into a single form, emergy which is measured by solar energy, so that enhance the accuracy of EF calculation, compared with the traditional one.

<!-- b000129 | prose | pages [7] -->
 Controversy representative of sustainability

<!-- b000130 | prose | pages [7] -->
Ecological footprint only takes the environmental and natural resources factor into consideration, but economic and social development are neglected. As a consequent, EF model is not necessarily sufficient to measure the sustainability of a country or policy. What’s more, EF model does not reflect the balance concept of sustainable development according to the analysis in Section 3.1.

<!-- b000131 | prose | pages [7] -->
In what follows, we devise a model for sustainable development that makes up the drawbacks of EF model and equips with strong visible and understandable results.

<!-- b000132 | heading | pages [7] -->
3.3. The Model

<!-- b000133 | prose | pages [7] -->
3.3.1.

<!-- b000134 | prose | pages [7] -->
Index System

<!-- b000135 | prose | pages [7] -->
According to the analysis in Section 3.1, we divide diverse aspects of a country development level into two overall indices: SE (Society-Economy) indices and ER (Environment-natural Resources) indices. To measure these indices, we design an index system.

<!-- b000136 | prose | pages [7] -->
First, we invoke principal component analysis to create a set of each overall indices respectively. We rank all the indices decreasingly by sum of the first two principal component loadings. Then we choose the indices on the top of the list on condition that their practical implications are reasonable. Meanwhile, the process must make sure that each overall indices have approximate number of indices.

<!-- b000137 | prose | pages [7] -->
Second, we inverse the negative indices and scale all the chosen indices as follow:

<!-- b000138 | prose | pages [7] -->
Positive:𝑥∗=

<!-- b000139 | prose | pages [7] -->
Negative: 𝑥∗=

<!-- b000140 | furniture | pages [7] -->


<!-- b000141 | prose | pages [7] -->
𝑥−𝑥min

<!-- b000142 | prose | pages [7] -->
,

<!-- b000143 | prose | pages [7] -->
𝑥max −𝑥min

<!-- b000144 | prose | pages [7] -->
𝑥max −𝑥

<!-- b000145 | prose | pages [7] -->
.

<!-- b000146 | prose | pages [7] -->
𝑥max −𝑥min

<!-- b000147 | furniture | pages [8] -->
Team # 38996

<!-- b000148 | furniture | pages [8] -->
Page 7 of 20

<!-- b000149 | furniture | pages [8] -->


<!-- b000150 | furniture | pages [8] -->


<!-- b000151 | prose | pages [8] -->
For example, the carbon dioxide emissions is a negative index, so we inverse the statistic while scaling the data.

<!-- b000152 | prose | pages [8] -->
So far, we have attained all 𝑛 indices we need. It follows that establishing the hierarchy system all these indices. We invoke some existing model (such as Cobb-Douglas production function) to devise a four-stage indices system. The indices system is showed

<!-- b000153 | prose | pages [8] -->
in Figure 1. To clarify the calculation process of indices in level 2, we illustrate, for example, the agriculture index in detail.

<!-- b000154 | prose | pages [8] -->
Level 4

<!-- b000155 | prose | pages [8] -->
Level 3

<!-- b000156 | prose | pages [8] -->
Society

<!-- b000157 | furniture | pages [8] -->


<!-- b000158 | prose | pages [8] -->
Labor

<!-- b000159 | prose | pages [8] -->
Health

<!-- b000160 | prose | pages [8] -->
Education

<!-- b000161 | prose | pages [8] -->
Technology

<!-- b000162 | prose | pages [8] -->
Level 2

<!-- b000163 | furniture | pages [8] -->


<!-- b000164 | furniture | pages [8] -->


<!-- b000165 | furniture | pages [8] -->


<!-- b000166 | furniture | pages [8] -->


<!-- b000167 | prose | pages [8] -->
Labor

<!-- b000168 | prose | pages [8] -->
Communi

<!-- b000169 | prose | pages [8] -->
force

<!-- b000170 | prose | pages [8] -->
education

<!-- b000171 | prose | pages [8] -->
education

<!-- b000172 | prose | pages [8] -->
ty health

<!-- b000173 | prose | pages [8] -->
Level 1

<!-- b000174 | prose | pages [8] -->
participat

<!-- b000175 | prose | pages [8] -->
expenditu

<!-- b000176 | prose | pages [8] -->
expenditu

<!-- b000177 | prose | pages [8] -->
workers,

<!-- b000178 | prose | pages [8] -->
re, etc.

<!-- b000179 | prose | pages [8] -->
re, etc.

<!-- b000180 | prose | pages [8] -->
ion rate,

<!-- b000181 | prose | pages [8] -->
etc.

<!-- b000182 | prose | pages [8] -->
etc.

<!-- b000183 | prose | pages [8] -->
SE Index

<!-- b000184 | prose | pages [8] -->
Sustainable Development

<!-- b000185 | furniture | pages [8] -->


<!-- b000186 | prose | pages [8] -->
Economics

<!-- b000187 | prose | pages [8] -->
Environment

<!-- b000188 | furniture | pages [8] -->


<!-- b000189 | furniture | pages [8] -->


<!-- b000190 | prose | pages [8] -->
Agri-

<!-- b000191 | prose | pages [8] -->
Industry

<!-- b000192 | prose | pages [8] -->
Service

<!-- b000193 | prose | pages [8] -->
Natural

<!-- b000194 | prose | pages [8] -->
Pollution

<!-- b000195 | prose | pages [8] -->
culture

<!-- b000196 | furniture | pages [8] -->


<!-- b000197 | furniture | pages [8] -->


<!-- b000198 | prose | pages [8] -->
Resource

<!-- b000199 | furniture | pages [8] -->


<!-- b000200 | furniture | pages [8] -->


<!-- b000201 | furniture | pages [8] -->


<!-- b000202 | prose | pages [8] -->
Industry

<!-- b000203 | prose | pages [8] -->
Services,

<!-- b000204 | prose | pages [8] -->
Food

<!-- b000205 | prose | pages [8] -->
Nitrous

<!-- b000206 | prose | pages [8] -->
value

<!-- b000207 | prose | pages [8] -->
etc.,

<!-- b000208 | prose | pages [8] -->
Agricultur

<!-- b000209 | prose | pages [8] -->
productio

<!-- b000210 | prose | pages [8] -->
oxide

<!-- b000211 | prose | pages [8] -->
added,

<!-- b000212 | prose | pages [8] -->
al land,

<!-- b000213 | prose | pages [8] -->
value

<!-- b000214 | prose | pages [8] -->
n index,

<!-- b000215 | prose | pages [8] -->
emissions

<!-- b000216 | prose | pages [8] -->
etc.

<!-- b000217 | prose | pages [8] -->
etc.

<!-- b000218 | prose | pages [8] -->
added,

<!-- b000219 | prose | pages [8] -->
etc.

<!-- b000220 | prose | pages [8] -->
, etc.

<!-- b000221 | prose | pages [8] -->
etc.

<!-- b000222 | furniture | pages [8] -->


<!-- b000223 | prose | pages [8] -->
ER Index

<!-- b000224 | caption | pages [8] -->
Figure 1 Index System

<!-- b000225 | prose | pages [8] -->
In case of industry, Cobb-Douglas production function has form

<!-- b000226 | prose | pages [8] -->
𝑌= 𝐴𝐿𝛼𝐾𝛽𝑃1−𝛼−𝛽 where 𝑌, 𝐴, 𝐿, 𝐾, and 𝑃 are industrial production, technology factor, labors, investment, and land input respectively. And 𝛼, 𝛽 are parameter. As for agriculture case, the investment does not necessarily relate to agricultural output. Consequently, we devise the agricultural index which can be calculated by

<!-- b000227 | prose | pages [8] -->
𝑌= 𝐴𝐿𝛼𝑃1−𝛼 where 𝑌, 𝐴, 𝐿, 𝐾, and 𝑃 are industrial production, technology factor, labors, and land input respectively. And 𝛼 are parameter whose value can be attained by regression analysis of historical data.

<!-- b000228 | prose | pages [8] -->
When it comes to the calculation from level 2 to level 3, we combine entropy evaluation method [5] and subjectivity-objectivity weighting method based on CRITIC [6] to devise the calculating process.

<!-- b000229 | prose | pages [8] -->
To start with, we define the information entropy as

<!-- b000230 | prose | pages [8] -->
𝑚 𝑚

<!-- b000231 | prose | pages [8] -->
𝑒𝑗= −𝐾∑𝑦𝑖𝑗ln 𝑦𝑖𝑗

<!-- b000232 | furniture | pages [8] -->


<!-- b000233 | prose | pages [8] -->
𝑖=1 𝑖=1

<!-- b000234 | prose | pages [8] -->
where 𝐾= 1/ ln 𝑚  is a constant relates to sample size 𝑚. Let 𝑑𝑗= 1 −𝑒𝑗 representing

<!-- b000235 | prose | pages [8] -->
the valid value of information. Then we attain the initial weights of each index by normalize 𝑑𝑗

<!-- b000236 | prose | pages [8] -->
𝜔𝑗= 𝑑𝑗

<!-- b000237 | prose | pages [8] -->
.

<!-- b000238 | prose | pages [8] -->
𝑚 ∑ ∑ 𝑑𝑗 𝑗=1

<!-- b000239 | prose | pages [8] -->
As the weighting system has a strong professional background, we cannot merely determine them by statistic method. Therefore, we invoke subjectivity-objectivity

<!-- b000240 | furniture | pages [8] -->


<!-- b000241 | furniture | pages [9] -->
Team # 38996

<!-- b000242 | furniture | pages [9] -->
Page 8 of 20

<!-- b000243 | furniture | pages [9] -->


<!-- b000244 | furniture | pages [9] -->


<!-- b000245 | prose | pages [9] -->
weighting method here. In terms of ICM’s exclusive financial resources and influence, we can invite numerous professional experts to evaluate these compound index, and create a weighting set 𝐶𝑘⃗⃗⃗⃗ = (𝑐𝑘1, 𝑐𝑘2, … , 𝑐𝑘𝑛) for 𝑘= 1,2, … , 𝑙 where 𝑙 is the size of CRITIC weighting set (including entropy weights). The entire calculation flow is showed in Table 1.

<!-- b000246 | prose | pages [9] -->
Create the weighting set 𝐶𝑘⃗⃗⃗⃗ = (𝑐𝑘1, 𝑐𝑘2, … , 𝑐𝑘𝑛); Step 1

<!-- b000247 | prose | pages [9] -->
Step 2 Run Kendall’s consistency coefficient test [7] for each weighting proposal by CRITIC and entropy weights. If the result is significant, we accept the mean of weight set

<!-- b000248 | prose | pages [9] -->
𝐶 = 1

<!-- b000249 | prose | pages [9] -->
and go to Step 4;

<!-- b000250 | prose | pages [9] -->
Step 3

<!-- b000251 | prose | pages [9] -->
𝑙

<!-- b000252 | prose | pages [9] -->
𝑙∑𝐶𝑘⃗⃗⃗⃗

<!-- b000253 | prose | pages [9] -->
,

<!-- b000254 | prose | pages [9] -->
𝑘=1

<!-- b000255 | prose | pages [9] -->
𝜎𝑖∑(1−𝑟𝑖𝑗)

<!-- b000256 | prose | pages [9] -->
𝑗

<!-- b000257 | prose | pages [9] -->
Let 𝐶= 𝜃1𝐶1 + 𝜃2𝐶2 + ⋯+ 𝜃𝑙𝐶𝑙, where 𝜃𝑖=

<!-- b000258 | prose | pages [9] -->
, 𝑟𝑖𝑗 is

<!-- b000259 | prose | pages [9] -->
∑(𝜎𝑖∑(1−𝑟𝑖𝑗)

<!-- b000260 | prose | pages [9] -->
)

<!-- b000261 | prose | pages [9] -->
𝑗

<!-- b000262 | prose | pages [9] -->
𝑖

<!-- b000263 | prose | pages [9] -->
the correlation coefficient of index 𝑥𝑖 and 𝑥𝑗, and 𝜎𝑖 is the variance of index 𝑥𝑗.

<!-- b000264 | prose | pages [9] -->
Step 4 Run Spearman’s [8] post hoc test for rank correlation coefficient.

<!-- b000265 | caption | pages [9] -->
Table 1 The process of calculation of weighting process

<!-- b000266 | prose | pages [9] -->
So far we have finished our work in establishing the indices system. It follows Multi- dimensional scaling in a coordinate system.

<!-- b000267 | prose | pages [9] -->
Sustainability Measurement 3.3.2.

<!-- b000268 | prose | pages [9] -->
According to the analysis of sustainable development in Section 3.1 and the indices system, we can further determine the accurate coordinate 𝐴(𝑥, 𝑦) of each country for every particular year, as is showed in Figure 2. The vertical coordinate refers to ER indices and the horizon coordinate refers to SE indices. The higher the coordinate, the better performance it is. Recall that the data basket consist of several typical country all over the world, so the diagonal line actually represents the relatively balanced state of

<!-- b000269 | prose | pages [9] -->
development. Consequently, we can reasonably treat the diagonal line 𝑶𝑺⃗⃗⃗⃗⃗ = (𝟏, 𝟏) as an ideal development (standard sustainable development) pattern for every country. In

<!-- b000270 | prose | pages [9] -->
this case, the ligature between a specific country and the goal development node 𝑆, 𝑨𝑺⃗⃗⃗⃗⃗ = (1 −𝑥, 1 −𝑦), is naturally an ideal development direction of a country itself.

<!-- b000271 | prose | pages [9] -->
As we have analyzed before, the sustainability refers to a benign development state of a country. To measure the sustainability of a country clearly, we demonstrate the result through two aspects.

<!-- b000272 | furniture | pages [9] -->


<!-- b000273 | furniture | pages [10] -->
Team # 38996

<!-- b000274 | prose | pages [10] -->
1

<!-- b000275 | furniture | pages [10] -->
Page 9 of 20

<!-- b000276 | furniture | pages [10] -->


<!-- b000277 | furniture | pages [10] -->


<!-- b000278 | prose | pages [10] -->
S

<!-- b000279 | prose | pages [10] -->
Ideal development direction

<!-- b000280 | prose | pages [10] -->
2009

<!-- b000281 | prose | pages [10] -->
A

<!-- b000282 | prose | pages [10] -->
2011

<!-- b000283 | prose | pages [10] -->
θ

<!-- b000284 | prose | pages [10] -->
2010 2012

<!-- b000285 | prose | pages [10] -->
ER Index

<!-- b000286 | prose | pages [10] -->
Valid Development

<!-- b000287 | prose | pages [10] -->
Standard Development Line

<!-- b000288 | prose | pages [10] -->
O

<!-- b000289 | prose | pages [10] -->
A’

<!-- b000290 | prose | pages [10] -->
Development direction (Calculated by regression)

<!-- b000291 | furniture | pages [10] -->


<!-- b000292 | prose | pages [10] -->
1

<!-- b000293 | prose | pages [10] -->
SE Index

<!-- b000294 | caption | pages [10] -->
Figure 2 Sustainability Measurement

<!-- b000295 | prose | pages [10] -->
 Harmonious Development

<!-- b000296 | prose | pages [10] -->
Unfortunately, the ideal development is rare and hard to implement in reality. And actual development usually deviate from ideal one. Therefore, we have to evaluate the actual development direction by comparing with ideal one. We invoke regression analysis to estimate the direction vector of a certain period.

<!-- b000297 | prose | pages [10] -->
We can calculate each tangent angle much accurately by using Bézier spline function to fit a series of coordinates. Bézier spline function is much more precise at fitting an incontinuous function with smooth curvature, so it can perform better for this task and tell exact curvature (tangent angle) for every year. So it helps us to determine the exact time point if we are required to tell when a country is sustainable.

<!-- b000298 | prose | pages [10] -->
Harmonious development is the degree that a country’s development approaches to the ideal pattern. We measure the harmonious development as the magnitude of intersection angle 𝜃 between ideal development direction and actual development direction. It depicts the degree that a country’s development direction deviate away from

<!-- b000299 | prose | pages [10] -->
the ideal one. Figure 3 shows the relation between these two direction and the intersection angle. It is obvious that a small 𝜃 indicates well harmonious development.

<!-- b000300 | prose | pages [10] -->
Ideal development direction

<!-- b000301 | prose | pages [10] -->
θ θ1

<!-- b000302 | prose | pages [10] -->
θ4

<!-- b000303 | prose | pages [10] -->
θ3

<!-- b000304 | prose | pages [10] -->
θ2

<!-- b000305 | furniture | pages [10] -->


<!-- b000306 | caption | pages [10] -->
Figure 3 Ideal development direction

<!-- b000307 | prose | pages [10] -->
It is worth noticing that the ideal development direction is always a vector in first quadrant. It means ER indices and SE indices should both goes optimized. It follows that a sustainable development direction should always point to the upper right corner in the

<!-- b000308 | furniture | pages [10] -->


<!-- b000309 | furniture | pages [11] -->
Page 10 of 20

<!-- b000310 | furniture | pages [11] -->
Team # 38996

<!-- b000311 | furniture | pages [11] -->


<!-- b000312 | prose | pages [11] -->
coordinate system.

<!-- b000313 | prose | pages [11] -->
 Valid Development

<!-- b000314 | prose | pages [11] -->
Given that ideal development is hardly exist in reality, some countries might develop in an unhealthy way which runs more and more away from the standard sustainable development pattern. A perpendicular deviation, for example, should actually be treat as in vain in terms of valid development.

<!-- b000315 | prose | pages [11] -->
Valid development is the degree that a country’s development that can reflect on standard development pattern line. In another word, the valid development is the

<!-- b000316 | prose | pages [11] -->
projection vector 𝑂𝐴′⃗⃗⃗⃗⃗⃗⃗  of actual development vector 𝑂𝑆⃗⃗⃗⃗⃗  on vector 𝑂𝐴⃗⃗⃗⃗⃗  (Figure 2). The module of 𝑂𝐴′⃗⃗⃗⃗⃗⃗⃗  is defined as valid development level.

<!-- b000317 | prose | pages [11] -->
In a similar way, we can define the potential development as module of vector 𝐴′𝑆⃗⃗⃗⃗⃗⃗ . We can infer from its magnitude about the potential sustainable development in the future (in another word, the weakness of current development), and bigger its magnitude, the more passive the current development is.

<!-- b000318 | prose | pages [11] -->
 When and How

<!-- b000319 | prose | pages [11] -->
We have define two possible methods to evaluate sustainability so far, and each one will perform perfectly as we verify the concept of sustainable development. To combine these methods and make the meaning of our measurement standard more clear. We further develop these to method by multiplying them together, whose product 𝐷𝑡 is a hyperbolic distance, and call it sustainable distance

<!-- b000320 | prose | pages [11] -->
𝐷𝑡= 𝜃⋅|𝐴′𝑆⃗⃗⃗⃗⃗⃗ |, where 𝑡 represents the time.

<!-- b000321 | prose | pages [11] -->
We have so far attained explicit evaluation system for sustainable development on condition that we determine a threshold value 𝐷0 = π/3 × 0.75 = 0.7854 for sustainable distance 𝐷𝑡. If the hyperbolic sustainable distance 𝐷𝑡≤𝐷0, then we assert that the country develops sustainably at that time, otherwise unsustainably. In this way, we can determine when and how a country is sustainable development.

<!-- b000322 | prose | pages [11] -->
3.3.3.

<!-- b000323 | heading | pages [11] -->
An Implementation of Our model

<!-- b000324 | prose | pages [11] -->
As an illustration of our model, we choose 5 diverse countries (America, China, France, Nepal, and South Africa) to show our model’s performance. We will show some significant results with diagrams and explanation. We omit 4 indices in the implementation because of lacks of data for these indices.

<!-- b000325 | prose | pages [11] -->
 Missing Data

<!-- b000326 | prose | pages [11] -->
We use the data from the World Bank [9] to implement our model, among which there are a few missing data. In order to make sure that our model functions well and make full use of existing data. We invoke Multiple Imputation to supplement the missing data.

<!-- b000327 | prose | pages [11] -->
Based on Bayes estimation, Multiple Imputation treats the supplement data as random one, which we can derive from observed data. We invoke Monte Carlo method to create

<!-- b000328 | furniture | pages [11] -->


<!-- b000329 | furniture | pages [12] -->
Team # 38996

<!-- b000330 | furniture | pages [12] -->
Page 11 of 20

<!-- b000331 | furniture | pages [12] -->


<!-- b000332 | furniture | pages [12] -->


<!-- b000333 | prose | pages [12] -->
the simulate set of missing data with R 3.1.2 and package “mi” and “mice”.

<!-- b000334 | prose | pages [12] -->
 Sustainability of five countries

<!-- b000335 | prose | pages [12] -->
We evaluate the development of five countries from 2003 to 2012, and Figure 4 shows our implementation result, and we label the first year and the last year of our data in the figure to clarify the development direction of each country. Invoking regression analysis, we draw the development direction of each country, which implies the harmonious development. We can also draw an auxiliary diagonal line indicating the standard development pattern. Then we can evaluate the valid development of each country by projecting their center coordinate (mean coordinate) vector on the auxiliary line. It follows their hyperbolic distance from the ideal development.

<!-- b000336 | prose | pages [12] -->
1

<!-- b000337 | prose | pages [12] -->
0.9

<!-- b000338 | prose | pages [12] -->
2003

<!-- b000339 | prose | pages [12] -->
0.8

<!-- b000340 | prose | pages [12] -->
0.7

<!-- b000341 | prose | pages [12] -->
2012

<!-- b000342 | prose | pages [12] -->
0.6

<!-- b000343 | prose | pages [12] -->
2003

<!-- b000344 | prose | pages [12] -->
ER Index

<!-- b000345 | prose | pages [12] -->
2012

<!-- b000346 | prose | pages [12] -->
2003

<!-- b000347 | prose | pages [12] -->
0.5

<!-- b000348 | prose | pages [12] -->
2012

<!-- b000349 | prose | pages [12] -->
0.4

<!-- b000350 | prose | pages [12] -->
0.3

<!-- b000351 | prose | pages [12] -->
0.2

<!-- b000352 | prose | pages [12] -->
0.1

<!-- b000353 | prose | pages [12] -->
0

<!-- b000354 | prose | pages [12] -->
0 0.1 0.2 0.3 0.4 0.5

<!-- b000355 | prose | pages [12] -->
SE Index

<!-- b000356 | prose | pages [12] -->
China

<!-- b000357 | prose | pages [12] -->
2012

<!-- b000358 | prose | pages [12] -->
America

<!-- b000359 | prose | pages [12] -->
2003

<!-- b000360 | prose | pages [12] -->
Nepal

<!-- b000361 | prose | pages [12] -->
France

<!-- b000362 | prose | pages [12] -->
θ South Africa

<!-- b000363 | prose | pages [12] -->
2012

<!-- b000364 | prose | pages [12] -->
2003

<!-- b000365 | prose | pages [12] -->
0.6 0.6 0.7 0.8 0.9 1

<!-- b000366 | furniture | pages [12] -->


<!-- b000367 | caption | pages [12] -->
Figure 4 Implementation of five countries

<!-- b000368 | prose | pages [12] -->
Specifically, although America is in a bad ER situation (manifesting the bad performance in environment and natural resources development in the past), its development direction is heading right at ideal direction (the huge fluctuation in 2009 might because of economic depression), in another word, America develops harmoniously. The valid development is by and large okay for development in America. By means of calculation, the hyperbolic distance turns out 𝐷𝑡= 0.7647 < 𝐷0 , so we draw the conclusion that American development is sustainable in this period.

<!-- b000369 | prose | pages [12] -->
Country America China France Nepal South Africa

<!-- b000370 | prose | pages [12] -->
Sustainable Distance 0.764749 1.401829 0.570225 1.114179 0.685853

<!-- b000371 | caption | pages [12] -->
Table 2 Sustainable Distance of five countries from 2003 to 2012

<!-- b000372 | prose | pages [12] -->
We invoke the same method to evaluate remaining countries’ development. It turns out that both France and South Africa develops sustainably. Meanwhile, by calculating the

<!-- b000373 | prose | pages [12] -->
sustainable distance of each country (Table 2), we draw the conclusion that France is the most sustainable development country among these five countries. On the other hand,

<!-- b000374 | furniture | pages [12] -->


<!-- b000375 | furniture | pages [13] -->
Page 12 of 20

<!-- b000376 | furniture | pages [13] -->
Team # 38996

<!-- b000377 | furniture | pages [13] -->


<!-- b000378 | prose | pages [13] -->
China and Nepal are both unsustainable development countries, but the reasons are different. Chinese actual development direction diverge far away from the ideal

<!-- b000379 | heading | pages [13] -->
sustainable development direction, and it results in the unsustainability of China. While

<!-- b000380 | prose | pages [13] -->
both inharmonious direction and low valid development lead to Nepalese unsustainability. As Nepal is our choice from UN’s LDCs list, we suspend the discussion on Nepal here, and we will discuss on Nepal in Section 4 in detail.

<!-- b000381 | prose | pages [13] -->
3.3.4.

<!-- b000382 | heading | pages [13] -->
Further Discussion

<!-- b000383 | heading | pages [13] -->
 The Dynamic Process of Our Model

<!-- b000384 | prose | pages [13] -->
To predict the sustainability of a country in coming 20 years, we classify the task into two situation: forecast without intervention & forecast with intervention.

<!-- b000385 | prose | pages [13] -->
The first situation is much handier than another one. We invoke time series analysis to cope with the prediction without intervention. To be specific, we forecast each index by

<!-- b000386 | heading | pages [13] -->
Autoregressive Integrated Moving Average (ARIMA) Model [10], and then we use the

<!-- b000387 | prose | pages [13] -->
predicted data to evaluate a country’s development sustainability. We will discuss the reason we invoke ARIMA model and implement this method in Section 4.1 and do some explanation. As for prediction with interference, we improve our model by utilizing the concepts of system dynamics [11] and structure equation modeling. We devise a dynamic system for all indices we have chosen, and we will describe the improved model in Section

<!-- b000388 | heading | pages [13] -->
5 in detail. We also implement the model to simulate and forecast some programs and

<!-- b000389 | prose | pages [13] -->
policy.

<!-- b000390 | prose | pages [13] -->
 Policy Sustainability

<!-- b000391 | prose | pages [13] -->
To evaluate a specific policy, we regard a policy as an intervention of a country’s running process. Hence we transform this task into forecast with intervention, which we have just mentioned above, and we will not repeat it again.

<!-- b000392 | prose | pages [13] -->
 Comparison with other Method

<!-- b000393 | prose | pages [13] -->
There are actually quite many methods that focus on evaluate sustainability. EF model, for instance, which we have discussed before our model, is a typical one, and we have already expand it to design our model. We are now make some comparison with other models.

<!-- b000394 | prose | pages [13] -->
To start with, we would like to mention some traditional statistical or artificial weighting methods such as principal component method, SVM (support vector machine), AHP (Analytic Hierarchy Process), and fuzzy synthetic evaluation model (FCEM). These methods are either too objective to explain with professional background knowledge or too subjective to make themselves convinced.

<!-- b000395 | prose | pages [13] -->
On the contrary, our model considers both subjective and objective factor, and our model has a strong professional (sustainability) background to support itself.

<!-- b000396 | prose | pages [13] -->
The other kind of methods invoke heuristic search algorithm such as ant colony algorithm, simulated annealing algorithm, GA (Genetic Algorithm), BP artificial neural network. These methods, however, are essentially improvement of random search. So the

<!-- b000397 | furniture | pages [13] -->


<!-- b000398 | furniture | pages [14] -->
Team # 38996

<!-- b000399 | furniture | pages [14] -->
Page 13 of 20

<!-- b000400 | furniture | pages [14] -->


<!-- b000401 | furniture | pages [14] -->


<!-- b000402 | prose | pages [14] -->
running results depend on something uncertain. What’s worse, heuristic search algorithm would possibly attain very inaccurate results, especially in high-dimension situation. As a result, heuristic search algorithm is hardly appropriate for measuring sustainability, let alone apply to forecast.

<!-- b000403 | prose | pages [14] -->
By contrast, our model is much more stable. We invoke a series of statistical significance test to ensure the rationality and reasonability of results and the result is certain as long as the data is valid. In addition, the implementation of our model is handy.

<!-- b000404 | heading | pages [14] -->
4. Sustainability Development Plan

<!-- b000405 | prose | pages [14] -->
Our choice is Nepal, and we implement our model using the data from the World Bank. In what follow, we will analyze the current situation of Nepal and the forecast result. And then we propose our plan for Nepal.

<!-- b000406 | heading | pages [14] -->
4.1. Current Situation and Forecast without intervention

<!-- b000407 | prose | pages [14] -->
We implement our model.

<!-- b000408 | caption | pages [14] -->
Figure 5 shows the Nepalese development from 2003 to 2012. We infer from the result

<!-- b000409 | prose | pages [14] -->
that Nepal develops in a sustainable way, as the sustainable distance 𝐷𝑡 is greater than the threshold value 𝐷0 . Further on, in order to propose a 20 years sustainable development plan, we need to firstly predict the development 20 years forward so that we can draw the plan according to it development trend.

<!-- b000410 | prose | pages [14] -->
As is mentioned in Section 3.3.4, we invoke ARIMA model to forecast each index for

<!-- b000411 | heading | pages [14] -->
20 years with R 3.1.2 and package “tseries” and “forecast”. The reason we invoke ARIMA

<!-- b000412 | prose | pages [14] -->
model is the indices we consider are most nonstationary time series data. In addition, most of them are seasonal data such as added value of agriculture, which invalidate ARMA model. Consequently, ARIMA model turns out the best choice for forecast. As an example,

<!-- b000413 | prose | pages [14] -->
we show the forecast result of GDP (per capita) in Figure 6. The grey color area and the light blue color area represent confidence level of 0.8 and 0.95 respectively.

<!-- b000414 | prose | pages [14] -->
0.8

<!-- b000415 | prose | pages [14] -->
0.78

<!-- b000416 | prose | pages [14] -->
0.76

<!-- b000417 | prose | pages [14] -->
0.74

<!-- b000418 | prose | pages [14] -->
0.72

<!-- b000419 | prose | pages [14] -->
ER Index

<!-- b000420 | prose | pages [14] -->
0.7

<!-- b000421 | prose | pages [14] -->
Nepal

<!-- b000422 | prose | pages [14] -->
0.68

<!-- b000423 | prose | pages [14] -->
0.66

<!-- b000424 | prose | pages [14] -->
0.64

<!-- b000425 | prose | pages [14] -->
0.62

<!-- b000426 | prose | pages [14] -->
0.6

<!-- b000427 | prose | pages [14] -->
0.1 0.15 0.2

<!-- b000428 | prose | pages [14] -->
SE Index

<!-- b000429 | caption | pages [14] -->
Figure 5 Profile of Nepalese development

<!-- b000430 | prose | pages [14] -->
2000

<!-- b000431 | prose | pages [14] -->
1500

<!-- b000432 | prose | pages [14] -->
1000

<!-- b000433 | prose | pages [14] -->
500

<!-- b000434 | furniture | pages [14] -->


<!-- b000435 | furniture | pages [14] -->


<!-- b000436 | prose | pages [14] -->
0 5 10 15 20 25 30

<!-- b000437 | furniture | pages [14] -->


<!-- b000438 | caption | pages [14] -->
Figure 6 Forecast GDP (per capita) from

<!-- b000439 | prose | pages [14] -->
ARIMA(0,1,0)

<!-- b000440 | prose | pages [14] -->
We can observe from the forecast result that Nepalese development trend are roughly pointing to lower right corner (environmental deterioration), and the trend is more and

<!-- b000441 | furniture | pages [14] -->


<!-- b000442 | furniture | pages [15] -->
Team # 38996

<!-- b000443 | furniture | pages [15] -->
Page 14 of 20

<!-- b000444 | furniture | pages [15] -->


<!-- b000445 | furniture | pages [15] -->


<!-- b000446 | prose | pages [15] -->
more fierce year by year (in another word, geometric progression trend). It means Nepalese development tends to scarify the environment to foster it social-economic development. And that is an omen of unsustainable development.

<!-- b000447 | heading | pages [15] -->
4.2. Details of the Plan

<!-- b000448 | prose | pages [15] -->
Here, we propose two criteria of sustainable development plan:

<!-- b000449 | prose | pages [15] -->
Effective 

<!-- b000450 | prose | pages [15] -->
In our model in task 1, various indices are included to determine when and how a country is sustainable. We will apply sensitivity analysis to obtain a set of indices which are more effective than others. That is to say, changing the value of these indices will effectively enhance the level of sustainable development. And our plan will base on that effective indices set.

<!-- b000451 | prose | pages [15] -->
Reasonable 

<!-- b000452 | prose | pages [15] -->
Plans that based on effective indices are not necessarily suitable for the chosen country. Hence we will judge a plan by various aspects such as costs, resources and political conditions. Only reasonable plans will be included in our final plan.

<!-- b000453 | prose | pages [15] -->
Now we introduce how we utilize the two criteria to derive the final plan.

<!-- b000454 | heading | pages [15] -->
Effectiveness Judgment by Sensitivity Analysis

<!-- b000455 | prose | pages [15] -->
4.2.1.

<!-- b000456 | prose | pages [15] -->
Sensitivity analysis is always used to test the robustness of a model. And we invoke sensitivity analysis to evaluate the ability of each index to influence the results. In another word, we rank indices decreasingly by absolute value of difference quotient by index 𝑖 of sustainable distance 𝐷𝑡 as

<!-- b000457 | prose | pages [15] -->
𝑑𝑖(𝐷𝑡) = 𝐷𝑡(𝑥+ Δ𝑖𝑥) −𝐷𝑡(𝑥)

<!-- b000458 | prose | pages [15] -->
, Δ𝑖𝑥

<!-- b000459 | prose | pages [15] -->
where 𝑥 represents origin data, and Δ𝑖𝑥 is the variation of index 𝑖.

<!-- b000460 | prose | pages [15] -->
Using this approach, we obtain the effective indices list for Nepal (2003~2012) in Table 3, and Figure 7 shows the result of each index.

<!-- b000461 | prose | pages [15] -->
education expenditure 16 CO2 emissions 4 19 access to electricity

<!-- b000462 | prose | pages [15] -->
GINI coefficient 7 Technology index 2 12 Services (added)

<!-- b000463 | prose | pages [15] -->
Manufacturing (added) 10 Industry (added) 11

<!-- b000464 | furniture | pages [15] -->


<!-- b000465 | furniture | pages [15] -->


<!-- b000466 | caption | pages [15] -->
Table 3 Effective indices list

<!-- b000467 | prose | pages [15] -->
Based on these influential index, we propose some possible directions for our final plan as follow:

<!-- b000468 | prose | pages [15] -->
 Reduce CO2 emissions (Index 16)  Education program (Index 4)  Modernization support (Indices 19 and 7)  Effort to reduce the gap between the rich and poor (Index 2)  Economic assistance (Indices 10, 11, 12)

<!-- b000469 | furniture | pages [15] -->


<!-- b000470 | furniture | pages [16] -->
Team # 38996

<!-- b000471 | prose | pages [16] -->
0.0015 0.001 0.0005 0

<!-- b000472 | furniture | pages [16] -->
Page 15 of 20

<!-- b000473 | furniture | pages [16] -->


<!-- b000474 | furniture | pages [16] -->


<!-- b000475 | prose | pages [16] -->
Sensitivity

<!-- b000476 | prose | pages [16] -->
10 11 12 13 14 15 16 17 18 19 20 21 22 1 2 3 4 5 6 7 8 9

<!-- b000477 | prose | pages [16] -->
0.005

<!-- b000478 | prose | pages [16] -->
0

<!-- b000479 | prose | pages [16] -->
1 2 3 4 5 6 7 8 9 10 11 12

<!-- b000480 | prose | pages [16] -->
Sensitivity

<!-- b000481 | prose | pages [16] -->
13 14 15 16 17 18 19 20 21 22

<!-- b000482 | furniture | pages [16] -->


<!-- b000483 | caption | pages [16] -->
Figure 7 Sensitivity of each index

<!-- b000484 | prose | pages [16] -->
Reasonability Judgment by Actual Conditions 4.2.2.

<!-- b000485 | prose | pages [16] -->
Given that our model provides several rough directions of our plan, it remains to refine and substantiate them by reality. To this end we list some basic characteristic of Nepal: backward agricultural country, low and medium political stability (Nepalese Political Instability Index is 7.5 in 2009-2010)1, distinctive tourism resources (Mt Everest, Largest forest park in south Asia, lots of rare animals). In addition, Nepalese education plan in 1971 fastened the development of Education and the current education status has improved dramatically. Based on these cases, the draw a decision on possible solution in

<!-- b000486 | caption | pages [16] -->
Table 4.

<!-- b000487 | prose | pages [16] -->
Actual Requirement Possible Direction Demands Decision

<!-- b000488 | prose | pages [16] -->
Political stability Cost

<!-- b000489 | prose | pages [16] -->
Reduce CO2 emissions

<!-- b000490 | prose | pages [16] -->
Resource

<!-- b000491 | prose | pages [16] -->
Rejected High High

<!-- b000492 | prose | pages [16] -->
Education program

<!-- b000493 | prose | pages [16] -->
Medium Low

<!-- b000494 | prose | pages [16] -->
Accepted Medium Flexible

<!-- b000495 | prose | pages [16] -->
Modernization program

<!-- b000496 | prose | pages [16] -->
- Medium

<!-- b000497 | prose | pages [16] -->
Accepted Medium Flexible

<!-- b000498 | prose | pages [16] -->
Reduce GINI index

<!-- b000499 | prose | pages [16] -->
- High

<!-- b000500 | prose | pages [16] -->
Accepted Medium High

<!-- b000501 | prose | pages [16] -->
Economic assistance

<!-- b000502 | prose | pages [16] -->
Medium High

<!-- b000503 | prose | pages [16] -->
Accepted Medium High Medium High

<!-- b000504 | caption | pages [16] -->
Table 4 Possible proposal trade-off

<!-- b000505 | prose | pages [16] -->
Ultimate Plan for Sustainable development 4.2.3.

<!-- b000506 | prose | pages [16] -->
We propose our sustainable development plan (including programs and aids) for Nepal:

<!-- b000507 | heading | pages [16] -->
1. Education program

<!-- b000508 | prose | pages [16] -->
Nepalese secondary school enrollment rate is 65.82% in 2012. Although the education status of Nepal has progresses dramatically, the low-income, women, and indigenous people can hardly get equal access to education. This education program will provide access of education to these people and raise the secondary enrollment. And the program expects to enhance the education expenditure by 1.4% every year.

<!-- b000509 | heading | pages [16] -->
2. Modernization program

<!-- b000510 | prose | pages [16] -->
We propose a program that aims to support Nepalese modernization, especially

<!-- b000511 | furniture | pages [16] -->


<!-- b000512 | furniture | pages [16] -->


<!-- b000513 | prose | pages [16] -->
1 Social unrest – ViewsWire (http://viewswire.eiu.com/site_info.asp?info_name=social_unrest_table)

<!-- b000514 | furniture | pages [16] -->


<!-- b000515 | furniture | pages [17] -->
Page 16 of 20

<!-- b000516 | furniture | pages [17] -->
Team # 38996

<!-- b000517 | furniture | pages [17] -->


<!-- b000518 | prose | pages [17] -->
infrastructural services. It will support Nepal to build a wide electricity reticulation system and telephone network, raising the proportion of access to electricity and telecom service. The program expects to increase the access to electricity (per capita) by 11.7% every year or the amount of telephone lines (per 100) by 14.8% every year.

<!-- b000519 | heading | pages [17] -->
3. Economic aid

<!-- b000520 | prose | pages [17] -->
As is mentioned above, Nepal has abundant tourism resources. This aid will support Nepal’s tourism and light industry, thus providing more job opportunity which reduces GINI index as well as promoting economic development. The aid project would provide 5.6% economic investment for Nepalese industry.

<!-- b000521 | heading | pages [17] -->
5. Dynamic Improvement

<!-- b000522 | heading | pages [17] -->
5.1. System Dynamics and Structure Equations

<!-- b000523 | prose | pages [17] -->
As is mentioned previously, we use system dynamics to improve our model so as to predict sustainability with intervention.

<!-- b000524 | heading | pages [17] -->
System Dynamics model is developed for predicting consequences of interactions among

<!-- b000525 | prose | pages [17] -->
subsystems and analyzing the implications of different policies and programs [12]. In our case, sustainable development system consists of three subsystems: environment- resources (ER) system, society system, and economy system. These subsystems affect each other. For example, economic indices and environmental indices react to policy change. Meanwhile, they will impact on each other conversely. These interactions in dynamic system is complicated not only because they simultaneously involve various factors but also because they dynamically change over time. Therefore, System Dynamics is an appropriate approach to improve our model. Also, it is handy to analyze our suggestions for sustainability of country development.

<!-- b000526 | prose | pages [17] -->
We design the dynamic system for our indices and show the relationship between

<!-- b000527 | prose | pages [17] -->
these indices in Figure 8. It is worthy noticing that because of the lack of data, the dynamic system is not complete. That is to say, the system is not closed, and we invoke regression analysis to remedy. To quantitatively calculate the interaction between indices, we invoke concept of structure equation modeling and use Three-Stage Least Squares (3SLS) to estimate the parameters in dynamic system equations with R 3.1.2 and package “systemfit”.

<!-- b000528 | heading | pages [17] -->
The parameter estimation result is showed in Table 5, where 𝑃𝑂𝑃-population; 𝐵𝑅-

<!-- b000529 | prose | pages [17] -->
birth rate; 𝐷𝑅-death rate; 𝐺𝐷𝑃- GDP per capita; 𝐶𝐻𝑊-community health workers; 𝑆𝐸𝑅-secondary school enrollment rate; 𝐴𝑆𝐸𝐸-adjusted savings: education expenditure; 𝑅𝑆𝐸𝐶=road sector energy consumption per capita; 𝑇𝐿-telephone lines; 𝐴𝐸-access to electricity; 𝐶𝑅𝑊-combustible renewables and waste; 𝐼-industry (added value); 𝑀- manufacturing (added value); 𝐿𝐹𝑃𝑅-labor force participation rate; 𝑆-service (added value); 𝐴-agriculture (added value); 𝐴𝐿-agricultural land; 𝐹𝑃𝐼-food production index; 𝐶𝐷𝐸-carbon dioxide emissions; 𝑁𝑂𝐸-nitrous oxide emissions; 𝐴𝐹𝑊𝐷-annual freshwater withdrawals domestic; 𝐴𝐹𝑊𝐼-annual freshwater withdrawals industry;

<!-- b000530 | furniture | pages [17] -->


<!-- b000531 | furniture | pages [18] -->
Team # 38996

<!-- b000532 | furniture | pages [18] -->
Page 17 of 20

<!-- b000533 | furniture | pages [18] -->


<!-- b000534 | furniture | pages [18] -->


<!-- b000535 | prose | pages [18] -->
𝐴𝐹𝑊𝐴-annual freshwater withdrawals agriculture.

<!-- b000536 | prose | pages [18] -->
+

<!-- b000537 | prose | pages [18] -->
Access to

<!-- b000538 | prose | pages [18] -->
School

<!-- b000539 | prose | pages [18] -->
electricity

<!-- b000540 | prose | pages [18] -->
enrollment,

<!-- b000541 | prose | pages [18] -->
secondary

<!-- b000542 | prose | pages [18] -->
+

<!-- b000543 | prose | pages [18] -->
+

<!-- b000544 | prose | pages [18] -->
Adjusted

<!-- b000545 | prose | pages [18] -->
Telephone lines

<!-- b000546 | prose | pages [18] -->
savings: education expenditure

<!-- b000547 | prose | pages [18] -->
-

<!-- b000548 | prose | pages [18] -->
Labor force participation

<!-- b000549 | prose | pages [18] -->
rate, total

<!-- b000550 | prose | pages [18] -->
+

<!-- b000551 | prose | pages [18] -->
Economic

<!-- b000552 | prose | pages [18] -->
GDP per capita

<!-- b000553 | prose | pages [18] -->
+

<!-- b000554 | prose | pages [18] -->
Industry, value

<!-- b000555 | prose | pages [18] -->
Services, etc.,

<!-- b000556 | prose | pages [18] -->
added

<!-- b000557 | prose | pages [18] -->
value added

<!-- b000558 | prose | pages [18] -->
+

<!-- b000559 | prose | pages [18] -->
+

<!-- b000560 | prose | pages [18] -->
Agriculture,

<!-- b000561 | prose | pages [18] -->
Manufacturing,

<!-- b000562 | prose | pages [18] -->
value added

<!-- b000563 | prose | pages [18] -->
value added

<!-- b000564 | prose | pages [18] -->
+

<!-- b000565 | prose | pages [18] -->
+

<!-- b000566 | prose | pages [18] -->
+

<!-- b000567 | prose | pages [18] -->
Society

<!-- b000568 | prose | pages [18] -->
Population,

<!-- b000569 | prose | pages [18] -->
-

<!-- b000570 | prose | pages [18] -->
total

<!-- b000571 | prose | pages [18] -->
+

<!-- b000572 | prose | pages [18] -->
Food

<!-- b000573 | prose | pages [18] -->
+

<!-- b000574 | prose | pages [18] -->
Community

<!-- b000575 | prose | pages [18] -->
production

<!-- b000576 | prose | pages [18] -->
health workers

<!-- b000577 | prose | pages [18] -->
index

<!-- b000578 | prose | pages [18] -->
-

<!-- b000579 | prose | pages [18] -->
Birth rate,

<!-- b000580 | prose | pages [18] -->
Death rate,

<!-- b000581 | prose | pages [18] -->
crude

<!-- b000582 | prose | pages [18] -->
crude

<!-- b000583 | prose | pages [18] -->
+

<!-- b000584 | prose | pages [18] -->
+

<!-- b000585 | prose | pages [18] -->
Annual

<!-- b000586 | prose | pages [18] -->
Annual

<!-- b000587 | prose | pages [18] -->
+ +

<!-- b000588 | prose | pages [18] -->
-

<!-- b000589 | prose | pages [18] -->
Agricultural

<!-- b000590 | prose | pages [18] -->
freshwater

<!-- b000591 | prose | pages [18] -->
freshwater

<!-- b000592 | prose | pages [18] -->
land

<!-- b000593 | prose | pages [18] -->
withdrawals,

<!-- b000594 | prose | pages [18] -->
withdrawals,

<!-- b000595 | prose | pages [18] -->
industry

<!-- b000596 | prose | pages [18] -->
agriculture

<!-- b000597 | prose | pages [18] -->
+ +

<!-- b000598 | prose | pages [18] -->
Road sector

<!-- b000599 | prose | pages [18] -->
Annual

<!-- b000600 | prose | pages [18] -->
Combustible

<!-- b000601 | prose | pages [18] -->
energy

<!-- b000602 | prose | pages [18] -->
freshwater

<!-- b000603 | prose | pages [18] -->
renewables and

<!-- b000604 | prose | pages [18] -->
consumption

<!-- b000605 | prose | pages [18] -->
withdrawals,

<!-- b000606 | prose | pages [18] -->
waste

<!-- b000607 | prose | pages [18] -->
per capita

<!-- b000608 | prose | pages [18] -->
domestic

<!-- b000609 | prose | pages [18] -->
+

<!-- b000610 | prose | pages [18] -->
Nitrous oxide

<!-- b000611 | prose | pages [18] -->
Environment

<!-- b000612 | prose | pages [18] -->
CO2 emissions

<!-- b000613 | prose | pages [18] -->
emissions in

<!-- b000614 | prose | pages [18] -->
+

<!-- b000615 | prose | pages [18] -->
& Resources

<!-- b000616 | prose | pages [18] -->
energy sector

<!-- b000617 | prose | pages [18] -->
+

<!-- b000618 | prose | pages [18] -->
+

<!-- b000619 | caption | pages [18] -->
Figure 8 System dynamics of development

<!-- b000620 | furniture | pages [18] -->


<!-- b000621 | prose | pages [18] -->
Environment & Resources Society Subsystem Economic Subsystem

<!-- b000622 | prose | pages [18] -->
Subsystem

<!-- b000623 | prose | pages [18] -->
𝑃𝑂𝑃= 𝑃𝑂𝑃/1000 ∗(𝐵𝑅−𝐷𝑅)

<!-- b000624 | prose | pages [18] -->
𝐼= −4.1019 + 0.0804 ∗𝐶𝑅𝑊

<!-- b000625 | prose | pages [18] -->
𝑅𝑆𝐸𝐶= 0.6841 + 0.0342 × 𝐺𝐷𝑃

<!-- b000626 | prose | pages [18] -->
𝐵𝑅= 34.1109 −0.0183 × 𝐺𝐷𝑃

<!-- b000627 | prose | pages [18] -->
𝑀= −31.7202 + 0.3703 × 𝐿𝐹𝑃𝑅

<!-- b000628 | prose | pages [18] -->
𝐴𝐿= 30.0478 −0.0010 × 𝐺𝐷𝑃

<!-- b000629 | prose | pages [18] -->
𝐷𝑅= 6.7491 + 0.0799 × 𝐷𝑁

<!-- b000630 | prose | pages [18] -->
+ 0.0949𝑅𝑆𝐸𝐶

<!-- b000631 | prose | pages [18] -->
+ 0.0090 × 𝐼

<!-- b000632 | prose | pages [18] -->
𝐶𝐻𝑊= 11.0975 −0.0714 × 𝑆𝑆𝐸𝑅

<!-- b000633 | prose | pages [18] -->
𝑆= 73.3006 −0.7910 × 𝐿𝐹𝑃𝑅

<!-- b000634 | prose | pages [18] -->
𝐶𝑅𝑊= 90.4809 + 0.0762 × 𝐼

<!-- b000635 | prose | pages [18] -->
𝑆𝐸𝑅= 24.9289 + 8.4137 × 𝐴𝑆𝐸𝐸

<!-- b000636 | prose | pages [18] -->
Δ𝐺𝐷𝑃= 170.5256 + 23.7031

<!-- b000637 | prose | pages [18] -->
−0.0093 × 𝐺𝐷𝑃

<!-- b000638 | prose | pages [18] -->
𝐴𝑆𝐸𝐸= 1.4993 + 0.0042 × 𝐺𝐷𝑃

<!-- b000639 | prose | pages [18] -->
× 𝐴+ 17.0251 × 𝐼

<!-- b000640 | prose | pages [18] -->
𝐶𝐷𝐸= 0.1249 −0.0005 × 𝐼

<!-- b000641 | prose | pages [18] -->
𝑇𝐿= −72.8756 + 1.0145 × 𝐴𝐸

<!-- b000642 | prose | pages [18] -->
+ 3.098 × 𝑀 𝐴= 46.2932 −0.0319 × 𝐴𝐿

<!-- b000643 | prose | pages [18] -->
𝑁𝑂𝐸= 1858.4 −14.3 × 𝐶𝑅𝑊

<!-- b000644 | prose | pages [18] -->
−0.0021 × 𝐺𝐷𝑃

<!-- b000645 | prose | pages [18] -->
𝐴𝐹𝑊𝐷= 2.0305 −0.0008 × 𝐺𝐷𝑃

<!-- b000646 | prose | pages [18] -->
𝐹𝑃𝐼= 887.6671 −26.3282 × 𝐴𝐿

<!-- b000647 | prose | pages [18] -->
−1.354 × 𝐿𝑃𝑅

<!-- b000648 | prose | pages [18] -->
𝐴𝐹𝑊𝐼= 0.3366 −0.0013 × 𝐼

<!-- b000649 | prose | pages [18] -->
𝐴𝐸= 72.8242 + 0.0054 × 𝐺𝐷𝑃

<!-- b000650 | prose | pages [18] -->
𝐴𝐹𝑊𝐴= 98.0524 −0.0135 × 𝐴

<!-- b000651 | prose | pages [18] -->
𝐿𝐹𝑃𝑅=  87.8768 −0.0033 × 𝐺𝐷𝑃

<!-- b000652 | caption | pages [18] -->
Table 5 Estimated equations of each subsystem

<!-- b000653 | prose | pages [18] -->
It is worth noticing that the simulation without intervention of our improved model should perform right identical to the forecast result in Section 4.1. We depict these two

<!-- b000654 | furniture | pages [18] -->


<!-- b000655 | furniture | pages [19] -->
Team # 38996

<!-- b000656 | furniture | pages [19] -->
Page 18 of 20

<!-- b000657 | furniture | pages [19] -->


<!-- b000658 | furniture | pages [19] -->


<!-- b000659 | prose | pages [19] -->
methods in one coordinate system in Figure 9. It turns out that our dynamic improvement is reasonable, and we can use the dynamic model to predict effects of each policy.

<!-- b000660 | prose | pages [19] -->
0.8

<!-- b000661 | prose | pages [19] -->
0.75

<!-- b000662 | prose | pages [19] -->
0.7

<!-- b000663 | prose | pages [19] -->
0.65

<!-- b000664 | prose | pages [19] -->
0.6

<!-- b000665 | prose | pages [19] -->
0.55

<!-- b000666 | prose | pages [19] -->
0.08 0.13 0.18

<!-- b000667 | prose | pages [19] -->
Simulation

<!-- b000668 | prose | pages [19] -->
Time Series

<!-- b000669 | prose | pages [19] -->
0.23 0.23 0.28 0.33

<!-- b000670 | caption | pages [19] -->
Figure 9 Comparison to ARIMA model without intervention

<!-- b000671 | heading | pages [19] -->
5.2. Simulation Run and Results

<!-- b000672 | prose | pages [19] -->
We implement the improvement of our model by simulate our proposal one by one with MATLAB. We compare their sustainable distance by every five years with each other and finally determine the most effective proposal for ICM.

<!-- b000673 | prose | pages [19] -->
We apply the expectation achievement of each item in our plan (education program, modernization program, and economic aid) to the dynamic system, and then forecast the development line for 20 year. To make the simulation results comparable, we draw the

<!-- b000674 | prose | pages [19] -->
development locus of each proposal in the same coordinate system in Figure 10, and we show the sustainable distance 𝐷𝑡 of every five year in Table 6.

<!-- b000675 | prose | pages [19] -->
0.8

<!-- b000676 | prose | pages [19] -->
0.75

<!-- b000677 | prose | pages [19] -->
0.7

<!-- b000678 | prose | pages [19] -->
0.65

<!-- b000679 | prose | pages [19] -->
0.6

<!-- b000680 | prose | pages [19] -->
0.55

<!-- b000681 | prose | pages [19] -->
0.08 0.13 0.18 0.23

<!-- b000682 | prose | pages [19] -->
No change

<!-- b000683 | prose | pages [19] -->
Economic Aid

<!-- b000684 | prose | pages [19] -->
Education Program

<!-- b000685 | prose | pages [19] -->
Modernization Program

<!-- b000686 | prose | pages [19] -->
0.28 0.33

<!-- b000687 | furniture | pages [19] -->


<!-- b000688 | caption | pages [19] -->
Figure 10 Simulation results of three programs compared with no intervention

<!-- b000689 | furniture | pages [19] -->


<!-- b000690 | furniture | pages [20] -->
Page 19 of 20

<!-- b000691 | furniture | pages [20] -->
Team # 38996

<!-- b000692 | furniture | pages [20] -->


<!-- b000693 | furniture | pages [20] -->


<!-- b000694 | prose | pages [20] -->
2015 2020 2025 2030

<!-- b000695 | prose | pages [20] -->
No Intervention 0.852894 0.984006 0.964756 0.29873

<!-- b000696 | prose | pages [20] -->
Economic Aid 0.853072 0.984272 0.965149 0.299622

<!-- b000697 | prose | pages [20] -->
Education Program 0.852192 0.982975 0.96332 0.294641

<!-- b000698 | prose | pages [20] -->
Modernization Program 0.848138 0.977041 0.955021 0.272045

<!-- b000699 | caption | pages [20] -->
Table 6 Sustainable distance of each proposal (every five year)

<!-- b000700 | prose | pages [20] -->
The implementation result indicates different effect of each proposal. On the one hand,

<!-- b000701 | prose | pages [20] -->
we observe from Figure 10 that modernization program develops in a more environmental friendly way, as the vertical coordinate of green line keeps higher than others. It follows that the harmonious development of modernization program is better. On the other hand, modernization program pushes the social-economic development forward most. It means the valid development improve most effectively by modernization program.

<!-- b000702 | heading | pages [20] -->
5.3. Conclusion

<!-- b000703 | prose | pages [20] -->
To sum up, as the modernization program performs better in both harmonious development and valid development, it deserves to perform better in minimizing the

<!-- b000704 | prose | pages [20] -->
magnitude of sustainable distance. We compare the sustainable distance in Table 6 and assert that the modernization proposal produces the greatest effect on the sustainability measure of our model. So it is the most highly effective strategy to be implemented by ICM.

<!-- b000705 | heading | pages [20] -->
6. Analysis of the Model

<!-- b000706 | heading | pages [20] -->
6.1. Strengths

<!-- b000707 | prose | pages [20] -->
Our model invokes and expand the concept of ecological footprint. We take  economic development, social development, environment and natural resources development in to consider instead of merely environment and natural resources.

<!-- b000708 | prose | pages [20] -->
The solving process is handy and the solution is stable. (see Section 3.3.4) 

<!-- b000709 | prose | pages [20] -->
The result of our model is visible and easy to understand. We demonstrate the  result of our model in a coordinate system, and the result can be understood from the geometric relation easily. Consequently, anyone can comprehend the evaluation without any background knowledge.

<!-- b000710 | prose | pages [20] -->
Our model has a strong sense of professional background. Our model bases on  both subjective and objective methods estimate the indices system, which provides professional support for our model.

<!-- b000711 | prose | pages [20] -->
Our model can be extended into higher dimension. As the coordinate system can  extend into three or higher dimension, our model can explain the sustainability in a more explicit way.

<!-- b000712 | prose | pages [20] -->
The dynamic improvement can be easily tracked year by year. The mechanism of 

<!-- b000713 | furniture | pages [20] -->


<!-- b000714 | furniture | pages [21] -->
Page 20 of 20

<!-- b000715 | furniture | pages [21] -->
Team # 38996

<!-- b000716 | furniture | pages [21] -->


<!-- b000717 | prose | pages [21] -->
system dynamics offers a handy way to determine every crucial index.

<!-- b000718 | heading | pages [21] -->
6.2. Weaknesses

<!-- b000719 | heading | pages [21] -->
The model does not take devastating natural disasters and devastating war into

<!-- b000720 | prose | pages [21] -->


<!-- b000721 | heading | pages [21] -->
consider. The model cannot forecast devastating disasters for a country, thus the

<!-- b000722 | prose | pages [21] -->
sustainability is not necessarily exact in terms of these unpredictable factors.

<!-- b000723 | prose | pages [21] -->
The statistical data used in implementing of model is not complete achievable.  We cannot find all data we required for sustainability (4 indices). Fortunately, ICM’s extensive financial resources and influence would definitely help ICM to attain the data.

<!-- b000724 | prose | pages [21] -->
The dynamic system can only explain the linear part of the indices system. We  invoke 3SLS to solve the model which estimate the parameters by linear regression. Consequently, only linear part of indices relation are utilized in our simulation. Meanwhile, the dynamic system is not complete because of lack of data.

<!-- b000725 | heading | pages [21] -->
References

<!-- b000726 | references | pages [21] -->
[1] Burton I. Report on Reports: Our Common Future: The World Commission on

<!-- b000727 | references | pages [21] -->
Environment and Development[J]. Environment: Science and Policy for Sustainable

<!-- b000728 | references | pages [21] -->
Development, 1987, 29(5): 25-29.

<!-- b000729 | references | pages [21] -->
[2] Wackernagel M. An evaluation of the ecological footprint[J]. Ecological Economics, 1999,

<!-- b000730 | references | pages [21] -->
31(3): 317-318.

<!-- b000731 | references | pages [21] -->
[3] Odum H T, Nilsson P O. Environmental Accounting--EMERGY and Environmental Decision

<!-- b000732 | references | pages [21] -->
Making[J]. Forest Science, 1997, 43(2): 305-305.

<!-- b000733 | references | pages [21] -->
[4] Zhang F Y, Pu L J, Zhang J. A modified model of ecological footprint calculation based on

<!-- b000734 | references | pages [21] -->
the theory of emergy analysis—Taking Jiangsu Province as an example[J]. Journal of

<!-- b000735 | references | pages [21] -->
Natural Resources, 2006, 21(4): 653-660.

<!-- b000736 | references | pages [21] -->
[5] Zou Z H, Yi Y, Sun J N. Entropy method for determination of weight of evaluating indicators

<!-- b000737 | references | pages [21] -->
in fuzzy synthetic evaluation for water quality assessment[J]. Journal of Environmental

<!-- b000738 | references | pages [21] -->
Sciences, 2006, 18(5): 1020-1023.

<!-- b000739 | references | pages [21] -->
[6] Diakoulaki D, Mavrotas G, Papayannakis L. Determining objective weights in multiple

<!-- b000740 | references | pages [21] -->
criteria problems: the CRITIC method[J]. Computers & Operations Research, 1995, 22(7):

<!-- b000741 | references | pages [21] -->
763-770.

<!-- b000742 | references | pages [21] -->
[7] Hollon S D, Kendall P C. Cognitive self-statements in depression: Development of an

<!-- b000743 | references | pages [21] -->
automatic thoughts questionnaire[J]. Cognitive therapy and research, 1980, 4(4): 383-

<!-- b000744 | references | pages [21] -->
395.

<!-- b000745 | references | pages [21] -->
[8] Fieller E C, Hartley H O, Pearson E S. Tests for rank correlation coefficients. I[J]. Biometrika,

<!-- b000746 | references | pages [21] -->
1957: 470-481.

<!-- b000747 | references | pages [21] -->
[9] World Bank Data (http://data.worldbank.org )

<!-- b000748 | references | pages [21] -->
[10] Box J, Jenkins G M. Reinsel. Time Series Analysis, Forecasting and Control[J]. 1994.

<!-- b000749 | references | pages [21] -->
[11] Forrester J W. Industrial dynamics: a major breakthrough for decision makers[J]. Harvard

<!-- b000750 | references | pages [21] -->
business review, 1958, 36(4): 37-66.

<!-- b000751 | references | pages [21] -->
[12] Guo H C, Liu L, Huang G H, et al. A system dynamics approach for regional environmental

<!-- b000752 | references | pages [21] -->
planning and management: a study for the Lake Erhai Basin.[J]. Journal of Environmental

<!-- b000753 | references | pages [21] -->
Management, 2001, 61(1):93–111.

<!-- b000754 | references | pages [21] -->
[13] Deepak Raj Parajuli , Tapash Das. "Performanc e Of Community Schools In Nepal : A Macro

<!-- b000755 | references | pages [21] -->
Level Analysis". International Journal of Scientific and Technology Research. Retrieved 9

<!-- b000756 | references | pages [21] -->
Feb 2015

<!-- b000757 | furniture | pages [21] -->

