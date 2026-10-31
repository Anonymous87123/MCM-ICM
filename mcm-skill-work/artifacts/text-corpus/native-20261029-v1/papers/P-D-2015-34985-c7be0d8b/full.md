# P-D-2015-34985-c7be0d8b

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [1] -->
Team Control Number

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
34985

<!-- b000010 | prose | pages [1] -->
T1 ________________

<!-- b000011 | furniture | pages [1] -->


<!-- b000012 | prose | pages [1] -->
T2 ________________

<!-- b000013 | prose | pages [1] -->
Problem Chosen

<!-- b000014 | prose | pages [1] -->
T3 ________________

<!-- b000015 | title | pages [1] -->
D

<!-- b000016 | prose | pages [1] -->
T4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
2015

<!-- b000020 | prose | pages [1] -->
For office use only F1 ________________ F2 ________________ F3 ________________ F4 ________________

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | prose | pages [1] -->
Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | prose | pages [1] -->
A Particle Swarm Optimization of an Iterative Function Map for Sustainable

<!-- b000025 | prose | pages [1] -->
Development in Zambia

<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | prose | pages [1] -->
Our team’s objective was to find a way to model sustainability of a country, and then use our model and research to create a 20­year sustainable development plan for one of the countries on the UN 48 Least Developed Countries (LDC) list. Therefore, we first wanted to be able to quantitatively determine sustainability, which is affected not just by environmental health but also by human well­being and overall wealth. We devised two metrics for sustainability ­ the (based on inequality­accounted income distribution, health, Socioeconomic Development Index D and education) and the Ecological Impact Index

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | prose | pages [1] -->
E E (based on pollution and non­renewable energy

<!-- b000030 | furniture | pages [1] -->


<!-- b000031 | prose | pages [1] -->
consumption). We plotted these two metrics against each other and found a strong negative correlation. Underdeveloped countries tended to have low human­economic development and high ecosystem health, while developed countries leaned towards high socioeconomic development but low ecosystem health. However, a true measure of sustainability can only be obtained from these two supporting values only if the desire for environmental responsibility is known so that the two D+αE factors can be accordingly weighted; we found true sustainability to be defined by , where α 1+α represents the importance ICM places on environmental sustainability.

<!-- b000032 | furniture | pages [1] -->


<!-- b000033 | prose | pages [1] -->
Our team decided to look at Zambia, an underdeveloped country in sub­Saharan Africa, and design a 20 year plan for sustainable development. The Socioeconomic Development Index and the Ecosystem Impact Index were expanded to include Zambia­specific human and environmental factors on a function map that related number of factors, as seen below. To evaluate this map, we iterated over the functions each year for twenty years with cost inputs from the ICM going towards variable values in the map. We then ran a Particle Swarm Optimization on the iterative function map using data from Zambia in order to find thebest distribution of monetary investment for sustainable development.  In addition, we developed a 2­dimensional cellular automata model that allows the ICM to pinpoint which geographic locations within the country the investments should be focused in. We graphed cost vs. sustainability with varying values of ( α ), and found budget

<!-- b000034 | furniture | pages [1] -->


<!-- b000035 | prose | pages [1] -->
plans for the ICM and Zambia’s government to optimize development and give Zambia “most bang for their buck”.

<!-- b000036 | furniture | pages [1] -->


<!-- b000037 | furniture | pages [1] -->


<!-- b000038 | furniture | pages [1] -->


<!-- b000039 | prose | pages [2] -->
A Particle Swarm Optimization of an Iterative Function Map

<!-- b000040 | prose | pages [2] -->
for Sustainable Development in Zambia

<!-- b000041 | furniture | pages [2] -->
Team # 34985

<!-- b000042 | prose | pages [2] -->
February 9, 2015

<!-- b000043 | prose | pages [2] -->
1

<!-- b000044 | furniture | pages [3] -->
Team # 34985

<!-- b000045 | heading | pages [3] -->
Contents

<!-- b000046 | contents | pages [3] -->
1

<!-- b000047 | contents | pages [3] -->
Problem Statement

<!-- b000048 | contents | pages [3] -->
2

<!-- b000049 | contents | pages [3] -->
Plan of Attack

<!-- b000050 | contents | pages [3] -->
3

<!-- b000051 | heading | pages [3] -->
Assumptions

<!-- b000052 | furniture | pages [3] -->
Page 2 of 19

<!-- b000053 | prose | pages [3] -->
3

<!-- b000054 | prose | pages [3] -->
3

<!-- b000055 | prose | pages [3] -->
3

<!-- b000056 | heading | pages [3] -->
Environmental Resource Management Model

<!-- b000057 | prose | pages [3] -->
4 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Quantifying Pollution 4 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2

<!-- b000058 | prose | pages [3] -->
5 Development for Better Life Quality

<!-- b000059 | prose | pages [3] -->
5

<!-- b000060 | prose | pages [3] -->
6 Human Development Index . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 6 Socioeconomic Development Index . . . . . . . . . . . . . . . . . . . . . . . 5.2 6 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000061 | prose | pages [3] -->
6 Ecological-Economic Trade oﬀ

<!-- b000062 | prose | pages [3] -->
7 20-year plan for Zambia

<!-- b000063 | prose | pages [3] -->
7

<!-- b000064 | prose | pages [3] -->
8

<!-- b000065 | prose | pages [3] -->
9 Population Growth and Economic Development . . . . . . . . . . . . . . . . 7.1 10 Iterated Function Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 11 . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3 Function Map Justiﬁcation 12 Disease and Health . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3.1 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3.2 Wealth 13 Nelder-Mead, Powell, and Genetic Optimization . . . . . . . . . . . . . . . . 7.4 13 Particle Swarm Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . 7.5 13 Evaluating the 20-year Plan . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.6 15 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . 7.6.1 16 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.7

<!-- b000066 | prose | pages [3] -->
8

<!-- b000067 | heading | pages [3] -->
Conclusion

<!-- b000068 | heading | pages [3] -->
References

<!-- b000069 | references | pages [3] -->
16

<!-- b000070 | references | pages [3] -->
17

<!-- b000071 | references | pages [3] -->
18

<!-- b000072 | heading | pages [3] -->
Appendix A Equations for Iterated Function Map

<!-- b000073 | prose | pages [3] -->
19

<!-- b000074 | furniture | pages [4] -->
Team # 34985

<!-- b000075 | furniture | pages [4] -->
Page 3 of 19

<!-- b000076 | prose | pages [4] -->
1 Problem Statement

<!-- b000077 | prose | pages [4] -->
With the United Nations (UN) predicting that the world’s population will be over 9 billion by 2050, the strain on the Earth’s ﬁnite resources will be signiﬁcant.

<!-- b000078 | prose | pages [4] -->
Concerns regarding the balance of human needs with ecosystem health have drawn attention to the concept of sustainable development. The International Conglomerate of Money (ICM) has asked us to help them understand how positive economic development can be achieved while still ensuring the sustainable consumption of resources so that the environment will not be compromised for future generations. The solution proposed within this paper will oﬀer an insight to these problems.

<!-- b000079 | prose | pages [4] -->
2 Plan of Attack

<!-- b000080 | prose | pages [4] -->
Our objective is to develop a metric to determine the sustainability of a given country and then quantify the trade-oﬀbetween maintaining ecosystem health and economic de- velop. To determine the most eﬀective mathematical model for this system, we will ﬁrst create a 2-part metric in order to assess the country’s ecological responsibility and socioeco- nomic development (the two main pillars of sustainability). Then, we will design a Zambia speciﬁc 20 year sustainable development plan by optimizing microeconomic and macroeco- nomic models of sustainability indicators. Lastly, we will project and evaluate the eﬀect of the plan with our 2 part metric.

<!-- b000081 | prose | pages [4] -->
3

<!-- b000082 | heading | pages [4] -->
Assumptions

<!-- b000083 | prose | pages [4] -->
• Based on Kuznet’s Curve hypothesis, we assumed only air pollution to be important in quantifying net pollution of a developing country [1]. Because there is no readily available data for water/ground pollution in most countries, this allowed us to quantify the relationship between pollution and our Ecological Impact Index.

<!-- b000084 | prose | pages [4] -->
• There are numerous trends in worldwide development of countries based on a variety of indicators (GDP, population, industry, etc.). Because these relationships generally hold true, we assume Zambia will follow these trends. This allowed for relationship quantiﬁcation between a number of indicators based on world wide data to predict Zambian growth, based on an initial seed that is Zambia’s current values for each indicator.

<!-- b000085 | prose | pages [4] -->
• We assume that ICM funding over 20 years follows a discrete model rather than continuous (i.e. funding for Zambia is paid for incrementally over the course of 20 years). This allows us to simplify our optimization model by only optimizing a ﬁnite number of resource allocations instead of inﬁnite over the twenty year period.

<!-- b000086 | prose | pages [4] -->
• While eﬀects of money may be semi-erratic, we assumed a deterministic instead of probabilistic eﬀect of ICM spending. This allowed us to create a solvable and repro- ducable optimization function that gives a distribution of resource allocation based on an input spending cost by the ICM and desire for Ecological over Developmental growth.

<!-- b000087 | furniture | pages [5] -->
Team # 34985

<!-- b000088 | furniture | pages [5] -->
Page 4 of 19

<!-- b000089 | prose | pages [5] -->
• Because industry growth and decay in Zambia is small [2], we assumed Zambia’s net change in industry size to be 0 (i.e. only redistribution of wealth between industries would occur) without ICM funding. This allowed us to quantify the eﬀect of ICM spending in Zambia and help use determine what measures would give the ICM the most bang for their buck.

<!-- b000090 | prose | pages [5] -->
• Zambia is politically stable with little history of political corruption when receiving external funding. Thus, we assume that ICM funding was not squandered, and used in full for the programs ICM allotted the money for. This allowed us to quantify the eﬀect of ICM spending on sustainable development.

<!-- b000091 | heading | pages [5] -->
Environmental Resource Management Model

<!-- b000092 | prose | pages [5] -->
4

<!-- b000093 | prose | pages [5] -->
4.1 Quantifying Pollution

<!-- b000094 | prose | pages [5] -->
A ﬁnal measurement of the ecological aspect of sustainability would be a weighted pollution index. Since not all pollutants damage the environment and peoples health as much as others, each would be individually weighted by a value indicative of the its current yearly damage on the environment. Global warming potential, or GWP, is a measure of how much heat - which damages the environment through global warming - is entrapped in the environment due to an atmospheric pollutant [3]. GWPs of various greenhouse gases are calculated based on the amount of heat they trap relative to the amount of heat trapped by the same mass of CO2 gas (whose GWP is normalized to 1) over a speciﬁed time frame [4]. The Intergovernmental Panel on Climate Change (IPCC) and Kyoto Protocol both use GWP measures as the de facto standard to measure emission damage when creating environmental policy [5]. We used the standard 100-year GWP values, shown below for the air pollutants that we were able to get country emission data for:

<!-- b000095 | prose | pages [5] -->
Global Warming Potentials (IPCC 2013) [6] Pollutant 100-year GWP

<!-- b000096 | prose | pages [5] -->
Carbon Dioxide

<!-- b000097 | prose | pages [5] -->
1

<!-- b000098 | prose | pages [5] -->
(CO2)

<!-- b000099 | prose | pages [5] -->
Methane (CH4) 28 Nitrous Oxide (N2O) 265

<!-- b000100 | prose | pages [5] -->
Pollutant 100-year GWP

<!-- b000101 | prose | pages [5] -->
Hydroﬂuorocarbons 12400

<!-- b000102 | prose | pages [5] -->
Perﬂuorocompounds 11100 Sulfur Hexaﬂuoride 23500

<!-- b000103 | prose | pages [5] -->
For each country, we calculated pollution as:

<!-- b000104 | prose | pages [5] -->
Pollutants

<!-- b000105 | prose | pages [5] -->
Pollution =

<!-- b000106 | prose | pages [5] -->
X

<!-- b000107 | prose | pages [5] -->
Ap ∗Wp (1)

<!-- b000108 | prose | pages [5] -->
p

<!-- b000109 | prose | pages [5] -->
where A is amount of pollutant p emitted per capita and W is the damage-based weighting of that pollutant based on normalized GWP data.

<!-- b000110 | furniture | pages [6] -->
Team # 34985

<!-- b000111 | furniture | pages [6] -->
Page 5 of 19

<!-- b000112 | caption | pages [6] -->
Figure 1: Worldwide view of country Ecological Impact Index (Di) values

<!-- b000113 | prose | pages [6] -->
Finally, we combined the pollution data with normalized nonrenewable energy use per capita data equally, transformed the sum onto a [0, 1] scale, and subtract the new value from 1 to ﬁnd an Ecological Impact Index Ei per country i. Therefore, low Ei represents high pollution and nonrenewable energy consumption, and vice versa for a high Ei. We ran our Ecological Impact Index on all countries with available pollution and energy use data. Countries colored grey have missing data.

<!-- b000114 | prose | pages [6] -->
4.2

<!-- b000115 | heading | pages [6] -->
Strengths and Weaknesses

<!-- b000116 | prose | pages [6] -->
Our metric for ecological impact of a country, Ei, is both easily calculable (for it is, in essence, a measure of CO2 equivalence and Non-renewable energy consumption) and encompasses all of the primary environmental impacts of a developing country, based on the Kuznet Curve. Because the Kuznet Curve has been extensively studied in literature and is a widely accepted relationship, we know our model for Ei is sound for the eﬀect of development on pollution.

<!-- b000117 | prose | pages [6] -->
Regarding weaknesses, this metric overlooks ground and water pollution in favor of air pollution. Because some underdeveloped countries suﬀer from a lack of clean water, this model should be readjusted (if suﬃcient data exists) to incorporate water pollution and better model Ei.

<!-- b000118 | furniture | pages [7] -->
Team # 34985

<!-- b000119 | furniture | pages [7] -->
Page 6 of 19

<!-- b000120 | prose | pages [7] -->
5 Development for Better Life Quality

<!-- b000121 | prose | pages [7] -->
5.1 Human Development Index

<!-- b000122 | prose | pages [7] -->
The Human Development Index, or HDI, is a composite measurement used to measure the quality of life in countries around the world. The HDI consists of real GDP per capita, life expectancy, adult literacy and years of schooling, which are combined to give a single value between 0 and 1. However, a major weakness of the HDI is that it uses GDP per capita while taking no account of income distribution [7]. This signiﬁes that, if income in unevenly distribution, then the GDP per capita is a misleading and inaccurate measure of the ﬁnancial well being of the people.

<!-- b000123 | prose | pages [7] -->
5.2 Socioeconomic Development Index

<!-- b000124 | prose | pages [7] -->
To make up for the ﬂaws of the HDI, we decided to use an inequality-adjusted measure- ment of monetary well-being. We deﬁned the function I(x) as the purchasing power (income in terms of local commodities), with x ∈(0, 1) being the income distribution percentile. We accounted for income inequality in an adjusted income distribution by multiplying I(x) for each x with a weight of 1 −x. We summed this value, I(x)(1 −x), for all x.

<!-- b000125 | caption | pages [7] -->
Figure 2: Graph of the theoretical income distribution I(x) and adjusted income distribution

<!-- b000126 | prose | pages [7] -->
A(x)

<!-- b000127 | prose | pages [7] -->
We also deﬁne E as the average years of education and LE as the average life expectancy. This results in a ﬁnal adjusted economic development function Di for any given country i of:

<!-- b000128 | prose | pages [7] -->
Di = 2

<!-- b000129 | prose | pages [7] -->
I(x)(1 −x)) + 2

<!-- b000130 | prose | pages [7] -->
5 Norm(LE) + 1

<!-- b000131 | prose | pages [7] -->
Z 5 log Norm(

<!-- b000132 | prose | pages [7] -->
5 Norm(E) (2)

<!-- b000133 | prose | pages [7] -->
where Norm indicates data normalization with respect to worldwide maxima and minima, a procedure utilized by the Human Development Index (HDI) [8]. We weighted education less, because the number of years of education has less of a factor on socioeconomic development

<!-- b000134 | furniture | pages [8] -->
Team # 34985

<!-- b000135 | furniture | pages [8] -->
Page 7 of 19

<!-- b000136 | prose | pages [8] -->
than life expectancy and income, and years of education already shares a strong correlation with those two values.

<!-- b000137 | prose | pages [8] -->
We ran our Socioeconomic development Index on all countries with available income distribution, life expectancy and years of education data.

<!-- b000138 | prose | pages [8] -->
Countries colored grey have missing data.

<!-- b000139 | caption | pages [8] -->
Figure 3: Worldwide view of country Development Index (Di) values

<!-- b000140 | prose | pages [8] -->
5.3

<!-- b000141 | heading | pages [8] -->
Strengths and Weaknesses

<!-- b000142 | prose | pages [8] -->
Our model, by accounting for income inequality and share of income by percentile, gives more weight to a fair distribution of wealth throughout the country, valuing equality over mean income. Additionally, because we integrate economic share and inequality within the same integral, we provide a more inclusive metric for measuring wealth than by separately calculating GDP and inequality, before combining values.

<!-- b000143 | prose | pages [8] -->
Thus, when this measure is combined with education and health, we have a more eﬀective measure of the evvect of wealth on the daily socioeconomic well-being of the populus. Thus, increasing this metric increases not just money but overall health and well-being.

<!-- b000144 | prose | pages [8] -->
Regarding weaknesses, because this model combines economy and well being into one value, it can be seen as weak compared to two values.

<!-- b000145 | prose | pages [8] -->
However, it is more eﬃcient to optimize one value than two, so having a sound one value metric is necessary for these purposes. Second, because this metric only combines three sources of information (albeit the three we value as most important), additional values unaccounted for by this metric will have an umeasured eﬀect on the country’s health and well being.

<!-- b000146 | furniture | pages [9] -->
Team # 34985

<!-- b000147 | furniture | pages [9] -->
Page 8 of 19

<!-- b000148 | prose | pages [9] -->
6 Ecological-Economic Trade oﬀ

<!-- b000149 | caption | pages [9] -->
Figure 4: Tradeoﬀdynamics. A: Socioeconomic Development Index (Di vs. Ecological

<!-- b000150 | prose | pages [9] -->
Impact Index Ei for any given country iB: Mean Index levels for underdeveloped vs. other nations.

<!-- b000151 | prose | pages [9] -->
It is very diﬃcult to optimize a country’s sustainability because there is often a trade oﬀbetween environmental protection and industrial development. This is highlighted in

<!-- b000152 | caption | pages [9] -->
Figure 4 below, where nations from the UN’s list of the 48 Least Developed Countries

<!-- b000153 | prose | pages [9] -->
(LDC) list [9] are clustered in the top left corner - representing low environmental damage and low human well-being. In comparison, more developed countries seem to have better life quality but much worse impact on the ecosystem. Therefore we can hypothesize that as countries develop, they follow the relatively negative trend between Di and Ei. An ideal conﬁguration - perfect sustainability - would be at the point (1, 1), where a country is both economically sustainable and environmentally sustainable.

<!-- b000154 | prose | pages [9] -->
We ranked the top 10 countries and compared it to the most recent Society Sustain- ability Index (SSI) rankings provided by the Sustainable Society Foundation (SSF) [10], a worldwide non-proﬁt organization that was established with the objective of aiding countries in sustainable development. The SSI is based on the deﬁnition of sustainability described in the Brundtland Commission’s 1987 United Nations General Assembly Report Our Com- mon Future: ”sustainable development is development that meets the needs of the present without compromising the ability of future generations to meet their own needs” [11]. The SSI includes 3 well-being dimensions: Human, Environmental and Economic Well-being. Similarly, our measure of sustainability includes an Ecological Impact (similar to the En- vironmental Well-being) and a Socioeconomic Development Index, which is comprised of elements from the SSI’s Human Well-being Index (education, life expectancy). The SSF has stated that development towards sustainability requires an integrated approach that si-

<!-- b000155 | furniture | pages [10] -->
Team # 34985

<!-- b000156 | furniture | pages [10] -->
Page 9 of 19

<!-- b000157 | prose | pages [10] -->
multaneously focuses on Human Well-being and Environmental Well-being, and that from an anthropocentric point of view, Economic Well-being (GDP, etc.) should be just a means to achieve these goals [12].

<!-- b000158 | prose | pages [10] -->
Only countries that both we and the SSF had data for were ranked. As seen in the table below, seven out of the top ten countries as determined by our Socioeconomic Development Index are found on the top ten rankings list of the SSF Human Well-being Index. Seven out of the top ten countries as determined by our Ecological Impact Index are also found on the top ten rankings list of the SST Environmental Well-being Index. We can see that the metrics we have created creates results that aﬃrms the results of UN accepted rankings. Our sustainability model has a clear, easy-to-understand basis in trends historically followed by countries as they change from underdeveloped countries to developed countries.

<!-- b000159 | prose | pages [10] -->
Top 10 Most Sustainable Countries Our Di SSF Human Well-being

<!-- b000160 | prose | pages [10] -->
Norway Finland Iceland Iceland Australia Germany Switzerland Japan Netherlands Sweden Ireland Denmark Sweden Norway Denmark Austria Germany Hungary Finland Ireland

<!-- b000161 | prose | pages [10] -->
7 20-year plan for Zambia

<!-- b000162 | prose | pages [10] -->
Our Ei SSF Enviro. Well-being Haiti Nepal Ethiopia Mozambique Mozambique Zambia Tanzania Tanzania Nepal Kenya Kenya Cameroon Nigeria Ethiopia Togo Tajikistan Bangladesh Benin Zambia Haiti

<!-- b000163 | prose | pages [10] -->
Zambia, an underdevloped, landlocked country in sub-Saharan Africa, is one of the 48 least developed nations, and currently has a Di = .339 and Ei = .742. In this section, we propose a set of programs, policies and aid that could be funded by the ICM in order to promote sustainable development in Zambia over 20 years. Key features we must consider in developing Zambia include [2]:

<!-- b000164 | prose | pages [10] -->
• High fertility and birth rates • Poor health care and high mortality rates • Signiﬁcantly understaﬀed doctors • Rampant levels of HIV/AIDS (over 15% of the population) • High income disparity (the top 10% control 47% of the income, GINI coeﬃcient = 0.6) • Agriculture, mining, and tourism form a signiﬁcant portion of Zambian industry

<!-- b000165 | prose | pages [10] -->
Our plan is built oﬀof the two indices we created to represent sustainability, so that we can ﬁnd how these features directly impact Di and Ei.

<!-- b000166 | furniture | pages [11] -->
Team # 34985

<!-- b000167 | furniture | pages [11] -->
Page 10 of 19

<!-- b000168 | prose | pages [11] -->
Population Growth and Economic Development 7.1

<!-- b000169 | prose | pages [11] -->
Knowing where to focus money and aid in a developing country is quintessential to the eﬃciency of country development. In order to optimize the ICM’s ”bang per buck” ratio, we created an automata model designed to determine optimal aid location with respect to both population density and wealth.

<!-- b000170 | prose | pages [11] -->
It is a known fact that wealth distribution and population dynamics are intertwined. To model the growth of population and wealth over time, we created a paired system of iterated microeconomic and agent-based behavioral functions to deﬁne the rules of of a 2-dimensional Cellular Automata, looking at the eﬀect of various starting paradigms. We modeled the diﬀusion of both wealth and population as cofactors of each other, based on an adjusted version of Epstein’s agent-based sugarscape model for social simulation [13].

<!-- b000171 | prose | pages [11] -->
dW

<!-- b000172 | prose | pages [11] -->
dt = dGiven

<!-- b000173 | prose | pages [11] -->
dt

<!-- b000174 | prose | pages [11] -->
dt = dGrowth

<!-- b000175 | prose | pages [11] -->
dP

<!-- b000176 | prose | pages [11] -->
dt

<!-- b000177 | prose | pages [11] -->
Approximating d

<!-- b000178 | prose | pages [11] -->
dt with ∆

<!-- b000179 | prose | pages [11] -->
+ dReceived

<!-- b000180 | prose | pages [11] -->
(3) dt

<!-- b000181 | prose | pages [11] -->
+ dMigration

<!-- b000182 | prose | pages [11] -->
(4) dt

<!-- b000183 | prose | pages [11] -->
∆t and setting ∆t = 1, we can translate the paired diﬀerentials for W(t) and P(t) into a system of iterated functions to calculate Population and Wealth of a country through Cellular Automata. These iterative functions can be written as shown below, with BR Birth Rate and LE = Life Expectancy. Both BR(Wn) and LE(Wn) are functions of wealth, such that BR(Wn) is a calculated best ﬁt logarithmic curve, and LE = LE(Wn) is the Preston curve for life expectancy as a function of national GDP (Appendix A) [14]. Thus, we can write our iterative equations as follows:

<!-- b000184 | prose | pages [11] -->
neighbors X

<!-- b000185 | prose | pages [11] -->
Wn+1 = (1 −8ϵ)Wn + ϵ

<!-- b000186 | prose | pages [11] -->
Pn+1 = Pn + Pn(BR(Wn) −

<!-- b000187 | prose | pages [11] -->
where

<!-- b000188 | prose | pages [11] -->
Wn

<!-- b000189 | prose | pages [11] -->
Wn,i (5)

<!-- b000190 | prose | pages [11] -->
i=0

<!-- b000191 | prose | pages [11] -->
1 LE(Wn)) + ∆Migration (6)

<!-- b000192 | prose | pages [11] -->
neighbors Wn X

<!-- b000193 | prose | pages [11] -->
P Wn,i ∆Migration = βPn(1 −

<!-- b000194 | prose | pages [11] -->
P Wn,j

<!-- b000195 | prose | pages [11] -->
) −β

<!-- b000196 | prose | pages [11] -->
Pn,i (7)

<!-- b000197 | prose | pages [11] -->
In this case, ϵ represents the coeﬃcient of employment (the percentage of wealth that is distributed via employment of a cell’s neighbors), and β represents the coeﬃcient of migration (the percentage of the population that migrates each iteration).

<!-- b000198 | prose | pages [11] -->
In essence, wealth is given to each neighbor as a fraction of current wealth, and population grows as both a function of itself and a function of migration.

<!-- b000199 | prose | pages [11] -->
Net migration is based oﬀof the migration percentage β of the population that exit the cell and enter the neighboring cells, in proportion with which neighbors have the highest wealth per person (GDP/capita). Equations 5 and 7 include summations of a cell’s neighbors, which represent the value of the entire neighborhood. The results of our cellular automata model over the course of 20 years are shown in Figure 5.

<!-- b000200 | furniture | pages [12] -->
Team # 34985

<!-- b000201 | furniture | pages [12] -->
Page 11 of 19

<!-- b000202 | prose | pages [12] -->
(a) Random initial wealth distribution.

<!-- b000203 | prose | pages [12] -->
(b) Trended initial wealth distribution.

<!-- b000204 | caption | pages [12] -->
Figure 5: Comparison of two seeds: random and biased wealth distribution with even initial

<!-- b000205 | prose | pages [12] -->
population distribution. For the red-blue gradients on the wealth and population automata, red indicates higher values of wealth and population while blue indicates lower values.

<!-- b000206 | caption | pages [12] -->
Figure 5 shows the results of both a random initial wealth distribution and biased

<!-- b000207 | prose | pages [12] -->
initial wealth distribution (concentrated in the bottom right corner) after 10 and 20 years, allowing us to see the spatial-economic equilibrium of wealth as a function of time. We see the natural segregation of wealth, and the corresponding segregation of population density, over the course of time, indicating natural increase in wealth inequality given no external factors.

<!-- b000208 | prose | pages [12] -->
Therefore, we can see that wealth segregates itself to areas of lower population, thus increasing income disparity. To counter this with external aid, we need to focus our eﬀorts on areas of increased poverty, which will adjust the seed distribution from biased (right) to more random (left), allowing for greater impact of monetary funds throughout Zambia.

<!-- b000209 | prose | pages [12] -->
A further suggestion is to introduce a progressive tax, which could be beneﬁcial for Zambia due to its uneven wealth distribution [15]. This income inequality is reﬂected in Zambia’s low Di value. By implementing this progressive tax, we ﬁnd that income disparity could be reduced and national GDP could be increased, and so we suggest looking further into a progressive taxation plan for increased Zambian development.

<!-- b000210 | prose | pages [12] -->
7.2 Iterated Function Map

<!-- b000211 | prose | pages [12] -->
Through the cellular automata model, we can geographically locate where the ICM should focus its eﬀorts. However, we also need to know in exactly what factors of Zambia’s economy and society the ICM can invest in. To accurately help plan Zambia’s 20 year plan for development, we created a map of the main factors that inﬂuence the Socioeconomic

<!-- b000212 | furniture | pages [13] -->
Team # 34985

<!-- b000213 | furniture | pages [13] -->
Page 12 of 19

<!-- b000214 | caption | pages [13] -->
Figure 6: Di and Ei with regards to features of Zambia, in terms of cost.

<!-- b000215 | prose | pages [13] -->
and Ecological Indices of Zambia. The factors in the map are interdependent, so we need to build oﬀof past iteration data as it is iterated over time. Thus we have resultant map that serves as a function map that allows us to quantify each index is indirectly a function of individual program cost. Given a budget that we must eﬀectively spend over 20 years, we must ﬁnd the optimal distribution of invested funds to the resources in the map. We will investigate four techniques (Genetic Algorithm, Nelder-Mead Search, Powell Search, and Particle Swarm Optimization) to ﬁnd the best investment distribution.

<!-- b000216 | prose | pages [13] -->
7.3 Function Map Justiﬁcation

<!-- b000217 | prose | pages [13] -->
7.3.1 Disease and Health

<!-- b000218 | prose | pages [13] -->
Zambia remains one of the top 10 HIV/AIDS killing zones in the world, with an average of 45,000 HIV related deaths recorded each year, and a prevalence of over 13.5% of the current population (over 980,000 people) [16]. HIV infected people often have weakened immune systems and thus can easily fall prey to infectious diseases such as tuberculosis. As a result, Zambia only has a life expectancy of 48 years, far below the world average, even when adjusted for Zambia’s poverty and lack of resources. More signiﬁcantly, the average citizen in Zambia at birth has a healthy life expectancy (HALE) of only 40 years [17].

<!-- b000219 | prose | pages [13] -->
Our goal is to implement programs in Zambia that can increase average life expectancy and decrease the prevalence of HIV. Using data from the World Health Organization and World Bank [17] [2], we developed a relationship that quantiﬁed life expectancy as a func-

<!-- b000220 | furniture | pages [14] -->
Team # 34985

<!-- b000221 | furniture | pages [14] -->
Page 13 of 19

<!-- b000222 | prose | pages [14] -->
tion of each variable linked to it in the map (HIV prevalence, Health Care Expenditures, Education, etc.). These equations are derived through best ﬁts of linearized relationship trends, and are found in Appendix A.

<!-- b000223 | prose | pages [14] -->
7.3.2 Wealth

<!-- b000224 | prose | pages [14] -->
Zambia is a struggling economy with great income disparity [18]. This is a signiﬁcant reason as to why they rank so low in development. With the goal in mind to increase the sustainable development of Zambia, we modeled weath’s eﬀect on both Ei and Di indeces in the sustainability-cost map (Figure 6) through a number of relationships. Intuitively, wealth increases with employment (jobs) and decreases with HIV prevalence [19]. Wealth also increases with renewable resource use, for it is the wealth saved from renewable energy that would otherwise have been spent on fossil fuel imports. Above wealth, we see the Ei is decreased with increased wealth, for increased wealth (when funneled into non renewwables) causes increased resource consumption and pollution. The Di index, intuitively, increases with wealth and income equality. The equations for each relationship are found in Appendix A.

<!-- b000225 | prose | pages [14] -->
7.4 Nelder-Mead, Powell, and Genetic Optimization

<!-- b000226 | prose | pages [14] -->
Both Nelder-Mead and Powell optimization methods start with a random distribution of investment money into various resources in the map, and proceed to optimize our investment by iteratively generating better distributions that we hoped would allow for more sucessful sustainable development [20] [21]. . Optimization using both of these algorithms for our iterative function map had the same two major ﬂaws: both methods quickly ﬁnd and lock to local optima, and neither of these methods are meant to be bounded, which reduces their ability to converge and therefore further decreased their eﬀectiveness.

<!-- b000227 | prose | pages [14] -->
To combat the weaknesses of Nelder-Mead and Powell’s optimization, we implemented a genetic algorithm to maximize the Sustainability measure of an investment distribution, where:

<!-- b000228 | prose | pages [14] -->
S(investments) = Di + α ∗Ei

<!-- b000229 | prose | pages [14] -->
(8) 1 + α

<!-- b000230 | prose | pages [14] -->
In this case, α is the country’s desire for environmental responsibility.

<!-- b000231 | prose | pages [14] -->
The genetic algorithm, because it is based on crossover and mutation of seed chromosomes, was able to be bounded and was more eﬀective than both Nelder-Mead and Powell’s method at ﬁnding global optima; however, it was far too slow to be useful in collecting the data we wanted for proper analysis. Therefore, we decided to forgo genetic algorithm based optimization.

<!-- b000232 | prose | pages [14] -->
7.5 Particle Swarm Optimization

<!-- b000233 | prose | pages [14] -->
Lastly, we set out to implement particle swarm optimization. This method works by initializing a set of particles to random positions in the investment distribution search space, each of with is attracted to both the optimal investment distribution it has found and the most optimal investment distribution any particle has found. The complex search and swarm behavior of the particles that results has been shown to be more eﬃcient and

<!-- b000234 | furniture | pages [15] -->
Team # 34985

<!-- b000235 | furniture | pages [15] -->
Page 14 of 19

<!-- b000236 | prose | pages [15] -->
successful at ﬁnding global optima than genetic algorithms for various applications [22]. Indeed, we found that by setting the size of the swarm to 128 particles, we were able to converge to optima faster than the genetic algorithm, and these optima were more likely to be the global optima.

<!-- b000237 | prose | pages [15] -->
Using the Particle Swarm Optimization, we found the optimal investment distributions and sustainability for varying values of investment and α. Due to processing power and time constraints, we split the 20 year plan into two 10 year plans instead of the year-by-year annual plans we had hoped to create. Figure 7 shows the relationship between investment and the resulting sustainability.

<!-- b000238 | caption | pages [15] -->
Figure 7: Eﬀect of alpha on resulting sustainability. The black line represents an example

<!-- b000239 | prose | pages [15] -->
budget/investment of 1.2 billion dollars.

<!-- b000240 | prose | pages [15] -->
For diﬀerent values of investment, there will be diﬀerent sustainability level outcomes depending on the α value. At any given investment, it would be most beneﬁcial in terms of ecosystem preservation to choose the plan with the highest resulting sustainability level, but this would depend on the government of Zambia’s desire for environmental responsibility and their preference for the corresponding investment distribution. For example, given an investment of 1.2 billion dollars (see vertical line in Figure 7), the following investment distributions are optimal:

<!-- b000241 | furniture | pages [16] -->
Team # 34985

<!-- b000242 | furniture | pages [16] -->
Page 15 of 19

<!-- b000243 | caption | pages [16] -->
Figure 8: Amount of money that should be invested based on the α level. Solid represents

<!-- b000244 | prose | pages [16] -->
the ﬁrst 10 years of the plan and striped represents the second 10 years. These numbers are based on a 1.2 billion dollar budget.

<!-- b000245 | prose | pages [16] -->
7.6 Evaluating the 20-year Plan

<!-- b000246 | prose | pages [16] -->
In evaluating our plan over the course of 20 years, we graph the trends in total sustain- ability (S) vs. time (t) for the optimal resource allocation plan as determined by Particle Swarm Optimization. The resulting graph demonstrate trends in Di, Ei and S as functions of time.

<!-- b000247 | caption | pages [16] -->
Figure 9: Di, Ei and S trends over time, respectively.

<!-- b000248 | prose | pages [16] -->
Blue represents α = 0.5, red represents α = 1, and green represents α = 1.5.

<!-- b000249 | prose | pages [16] -->
The trends in Figure 9 give us some insight on what to expect with an optimized ﬁnan- cial investment distribution at diﬀerent levels of α and an example budget of $ 1.2 billion. All three scenarios cause a rapid increase in socioeconomic development, and as a result, there is an increase in sustainability as well. However, this comes at a cost - a decrease in the ecological index Ei. After around 10-12 years, socioeconomic growth tapers oﬀand sustainability stabilizes to a value higher than it was before. The ecological index begins to increase. These trends show that for an underdeveloped country to undergo eﬃcient and sustainable development, factors of the socioeconomic index Di such as wealth, life

<!-- b000250 | furniture | pages [17] -->
Team # 34985

<!-- b000251 | furniture | pages [17] -->
Page 16 of 19

<!-- b000252 | prose | pages [17] -->
expectancy and education must ﬁrst increase positively at the expense of the environment. Then, once overall sustainability reaches a plateau higher than its initial value, ecosystem health can slowly be improved. Overall, we would recommend following the α = 0.5 tra- jectory for the ﬁrst 10 years, and then placing more emphasis on environmental impact by following the α = 1.5 trajectory to ensure more growth in overall sustainability.

<!-- b000253 | prose | pages [17] -->
7.6.1

<!-- b000254 | heading | pages [17] -->
Strengths and Weaknesses

<!-- b000255 | prose | pages [17] -->
The major strength of our team’s 20-year plan is that it successfully models a complex iterative network of relationships between a variety of factors, all of which are quantiﬁed in terms of cost. This allows us to algorithmically choose an optimal distribution of resources based on ICM funding and allow the ICM to maximize ”bang for the buck” return on investment with regards to how sustainable they desire development to be. By being able to combine and uncouple socioeconomic and environmental factors, our model demonstrates versatility and maximizes use of a variety of input factors uniquely tailored to Zambia, in order to both successfully ans sustainably enhance Zambia’s growth.

<!-- b000256 | prose | pages [17] -->
On the other hand, a weakness of the model is that it is calibrated on two iterations of 10 year long periods.

<!-- b000257 | prose | pages [17] -->
This is due to constraints in computer processing power and time limitations while devising the 20-year plan. However, given greater computing power, we envision our model being used to create yearly ICM investment distribution plans to maximize the overall increase in both socioeconomic and ecological sustainability over 20 years for Zambia. Another weakness is that since we do not include import or exports in our model, total wealth does not increase as much as it would had we accounted for imports and exports. This would aﬀect the value of our socioeconomic development index.

<!-- b000258 | prose | pages [17] -->
7.7

<!-- b000259 | heading | pages [17] -->
Sensitivity Analysis

<!-- b000260 | prose | pages [17] -->
It is a necessity of any strong model that it be tolerant to a small amount of error in its inputs.

<!-- b000261 | prose | pages [17] -->
For our model, this could result from incorrect population caps for job growth, Zambia not following world trends exactly regarding ﬁt relationships, slight over or under budgeting by the ICM, etc. Such errors could cause a poorly written algorithm to return incorrect, and very poorly aﬀected results. Thus, to test our model’s sensitivity, we intentionally created small sources of error in our data and compared the results to the results using unmodiﬁed seed data.

<!-- b000262 | prose | pages [17] -->
One error we introduced was the introduction of a higher population cap in the agricul- tural sector by 10%. We would believe this to have an impact in the increase in the number of total agriculture jobs, but little to no impact in the total economic and developmental indices, because our algorithms should have compensated for this cost elsewhere in the Zambian sustainability-cost web. We found the agricultural jobs increased by around 7.6% but the overall Ei and Di indices only were aﬀected by −0.2 and 0.1 percent respectively. Similar values (−0.3 and 0.4% were found when the process was repeated with the mining inductry.

<!-- b000263 | prose | pages [17] -->
To further test the robustness of our model, we introduced a second error: not accounting for solar energy in the calculation for wealth. In doing so, we believe that our algorithm should instead account for renewable energy with hydroelectric power, maintaining near constant values of Ei and Di. The results matched our expectations: our program instead

<!-- b000264 | furniture | pages [18] -->
Team # 34985

<!-- b000265 | furniture | pages [18] -->
Page 17 of 19

<!-- b000266 | prose | pages [18] -->
added dams instead of solar panels, accounting for a −0.2% in Di and no change in Ei These values make sense, for wealth should decrease with higher expenses of energy with dams than with solar panels.

<!-- b000267 | prose | pages [18] -->
Overall, we ﬁnd that our model successfully deals with errors in input and demonstrates solid robustness, matching expected behaviour with only fractions of a percent error, which are understandable because small input errors are only a fraction of a percent of the total sustainability metric.

<!-- b000268 | prose | pages [18] -->
8

<!-- b000269 | heading | pages [18] -->
Conclusion

<!-- b000270 | prose | pages [18] -->
We have modeled sustainability and devised a 20-year sustainable development plan for Zambia based on our ﬁndings. First, we devised two metrics to quantify the sustainability of a country: the Socioeconomic Development Index Di and the Ecological Impact Index Ei. We found that these two indices have a negative correlation - better human-economic life quality resulted in lower ecosystem health.

<!-- b000271 | prose | pages [18] -->
Therefore, we had to devise a 20-year plan that maximized economic expansion but also maintained a high level of environmental preservation. To see where to concentrate our aid geographically we used coupled diﬀerential equations to represent a wealth-population dynamic and implemented a two-dimensional cellular automata model. Then we created a personalized sustainability map for Zambia that included factors speciﬁc to the country. We found correlations between each of the factors by linearizing exponential and logarithmic relationships found from historical data. Finally we optimized this model using a particle swarm optimization and graphed ﬁnancial investment vs. sustainability for varying desires for environmental responsibility. Therefore, the ICM can identify which highly eﬀective strategies and programs to be implemented for a successful 20 years of sustainable development in Zambia.

<!-- b000272 | furniture | pages [19] -->
Team # 34985

<!-- b000273 | heading | pages [19] -->
References

<!-- b000274 | furniture | pages [19] -->
Page 18 of 19

<!-- b000275 | references | pages [19] -->
[1] M. Tucker. Carbon Dioxide Emissions and Global GDP. Ecological Economics, 15(3):215–223,

<!-- b000276 | references | pages [19] -->
1995.

<!-- b000277 | references | pages [19] -->
[2] World Bank Indicator Data. Retrieved from: http://data.worldbank.org/indicator.

<!-- b000278 | references | pages [19] -->
A guide to global warming potentials (GWPs).

<!-- b000279 | references | pages [19] -->
[3] L.D. Danny Harvey.

<!-- b000280 | references | pages [19] -->
106(28):11812–11817, 2009.

<!-- b000281 | references | pages [19] -->
Energy Policy,

<!-- b000282 | references | pages [19] -->
[4] D. Albritton, R. Derwent, I. Isaksen, M. Lal, and D. Wuebbles. Radiative forcing of climate

<!-- b000283 | references | pages [19] -->
change. Climate Change 1995, The Science of Climate Change, pages 118–131, 1996.

<!-- b000284 | references | pages [19] -->
[5] S. J. Smith and M. L. Wigley. Global warming potentials: Climatic implications of emissions

<!-- b000285 | references | pages [19] -->
reductions. Climate Change, 44(4):445–457, 2000.

<!-- b000286 | references | pages [19] -->
[6] G. Myhre, D. Shindell, F. M. Br´eon, W. Collins, J. Fuglestvedt, J. Huang, D. Koch, J. F.

<!-- b000287 | references | pages [19] -->
Lamarque, D. Lee, B. Mendoza, T. Nakajima, A. Robock, G. Stephens, T. Takemura, and

<!-- b000288 | references | pages [19] -->
H. Zhang. 2013: Anthropogenic and Natural Radiative Forcing in Report of the Intergovern-

<!-- b000289 | references | pages [19] -->
mental Panel on Climate Change. Cambridge University Press, Cambridge, United Kingdom,

<!-- b000290 | references | pages [19] -->
2013.

<!-- b000291 | references | pages [19] -->
[7] Elizabeth A. Stanton. The Human Development Index: A History. Working Paper Series,

<!-- b000292 | references | pages [19] -->
2007.

<!-- b000293 | references | pages [19] -->
Review of HDI Critiques and Potential Improvements.

<!-- b000294 | references | pages [19] -->
[8] Milorad Kovacevic.

<!-- b000295 | references | pages [19] -->
Development Research Paper, 2010.

<!-- b000296 | references | pages [19] -->
UNRP Human

<!-- b000297 | references | pages [19] -->
Countries.

<!-- b000298 | references | pages [19] -->
[9] UN

<!-- b000299 | references | pages [19] -->
list

<!-- b000300 | references | pages [19] -->
of

<!-- b000301 | references | pages [19] -->
Least

<!-- b000302 | references | pages [19] -->
Developed

<!-- b000303 | references | pages [19] -->
Retrieved

<!-- b000304 | references | pages [19] -->
from:

<!-- b000305 | references | pages [19] -->
http://unctad

<!-- b000306 | references | pages [19] -->
.org/en/pages/aldc/Least%20Developed%20Countries/UNlistofLeast DevelopedCountries.aspx.

<!-- b000307 | references | pages [19] -->
[10] Geurt van de Kerk and Arthur Manuel. A comprehensive index for a sustainable society: The

<!-- b000308 | references | pages [19] -->
SSI – the Sustainable Society Index. Ecological Economics, 66(2-3):228–242, 2008.

<!-- b000309 | references | pages [19] -->
[11] Brundtland Commission. World Commission on Environment and Development: Our Common

<!-- b000310 | references | pages [19] -->
Future. Oxford University Press, 1987.

<!-- b000311 | references | pages [19] -->
[12] Measuring

<!-- b000312 | references | pages [19] -->
wellbeing

<!-- b000313 | references | pages [19] -->
and

<!-- b000314 | references | pages [19] -->
progress

<!-- b000315 | references | pages [19] -->
towards

<!-- b000316 | references | pages [19] -->
sustainability.

<!-- b000317 | references | pages [19] -->
Retrieved

<!-- b000318 | references | pages [19] -->
from:

<!-- b000319 | references | pages [19] -->
http://ec.europa.eu/environment/beyond gdp/download/factsheets/bgdp vessi.pdf.

<!-- b000320 | references | pages [19] -->
[13] R. Axtell J.M. Epstein. Growing Artiﬁcial Societies: Social Science from the Bottom. UpMIT

<!-- b000321 | references | pages [19] -->
Press, Cambridge, MA, 1996.

<!-- b000322 | references | pages [19] -->
[14] Samuel H. Preston. The Changing Relation between Mortality and Level of Economic Devel-

<!-- b000323 | references | pages [19] -->
opment. Population Studies, 29(2):231–248, 1975.

<!-- b000324 | references | pages [19] -->
[15] Geurt van de Kerk and Arthur Manuel. The Case for a Progressive Tax: From Basic Research

<!-- b000325 | references | pages [19] -->
to Policy Recommendations. Ecological Economics, 25(4):165–190, 2011.

<!-- b000326 | references | pages [19] -->
[16] Major problems facing Zambia today.

<!-- b000327 | references | pages [19] -->
problemsfacingzambiatoday.

<!-- b000328 | references | pages [19] -->
Retrieved from:

<!-- b000329 | references | pages [19] -->
http://www.africaw. com/major-

<!-- b000330 | references | pages [19] -->
Retrieved

<!-- b000331 | references | pages [19] -->
[17] World

<!-- b000332 | references | pages [19] -->
Health

<!-- b000333 | references | pages [19] -->
Statistics

<!-- b000334 | references | pages [19] -->
2010.

<!-- b000335 | references | pages [19] -->
from:

<!-- b000336 | references | pages [19] -->
http://www.who.int/gho

<!-- b000337 | references | pages [19] -->
/publica-

<!-- b000338 | references | pages [19] -->
tions/world health statistics/EN WHS10 Full.pdf.

<!-- b000339 | references | pages [19] -->
[18] Zambia Institute for Policy Analysis & Research. The distribution of household income and

<!-- b000340 | references | pages [19] -->
the middle class in Zambia. 2013.

<!-- b000341 | references | pages [19] -->
Retrieved from:

<!-- b000342 | references | pages [19] -->
[19] HIV Impact on Economic Growth.

<!-- b000343 | references | pages [19] -->
http://www.un.org/esa/ popula-

<!-- b000344 | references | pages [19] -->
tion/publications/AIDSimpact/91 CHAP VIII.pdf.

<!-- b000345 | references | pages [19] -->
[20] J. A. Nelder and R. Mead. A simplex method for function minimization. The Computer Journal,

<!-- b000346 | references | pages [19] -->
1965.

<!-- b000347 | references | pages [19] -->
[21] M. J. D. Powell. An eﬃcient method for ﬁnding the minimum of a function of several variables

<!-- b000348 | references | pages [19] -->
without calculating derivatives. The Computer Journal, 1964.

<!-- b000349 | furniture | pages [20] -->
Team # 34985

<!-- b000350 | furniture | pages [20] -->
Page 19 of 19

<!-- b000351 | references | pages [20] -->
[22] R. Hassan, B. Cohanim, O. de Weck, and G. Venter. A comparison of particle swarm op-

<!-- b000352 | references | pages [20] -->
timization and the genetic algorithm. AIAA multidisciplinary design optimization specialist

<!-- b000353 | references | pages [20] -->
conference, 2005.

<!-- b000354 | references | pages [20] -->
Equations for Iterated Function Map

<!-- b000355 | references | pages [20] -->
A

<!-- b000356 | references | pages [20] -->
#

<!-- b000357 | references | pages [20] -->
Feature

<!-- b000358 | references | pages [20] -->
Inputs

<!-- b000359 | references | pages [20] -->
Equation

<!-- b000360 | references | pages [20] -->
x = Doctor Population

<!-- b000361 | references | pages [20] -->
1

<!-- b000362 | references | pages [20] -->
Life Expectancy

<!-- b000363 | references | pages [20] -->
5.058ln(x) + 65.02

<!-- b000364 | references | pages [20] -->
Density (per 1000)

<!-- b000365 | references | pages [20] -->
x = Years of Education

<!-- b000366 | references | pages [20] -->
2

<!-- b000367 | references | pages [20] -->
% Use of Con-

<!-- b000368 | references | pages [20] -->
traceptive

<!-- b000369 | references | pages [20] -->
2.07x + 27.54

<!-- b000370 | references | pages [20] -->
x = Government HIV

<!-- b000371 | references | pages [20] -->
3

<!-- b000372 | references | pages [20] -->
Years of Educa-

<!-- b000373 | references | pages [20] -->
1.4856ln(X) + 9.9122

<!-- b000374 | references | pages [20] -->
Health Care Expendi-

<!-- b000375 | references | pages [20] -->
tion

<!-- b000376 | references | pages [20] -->
ture per capita

<!-- b000377 | references | pages [20] -->
x = Total Health Care

<!-- b000378 | references | pages [20] -->
3

<!-- b000379 | references | pages [20] -->
Life Expectancy

<!-- b000380 | references | pages [20] -->
5.8066ln(x) + 33.7923

<!-- b000381 | references | pages [20] -->
Spending per capita

<!-- b000382 | references | pages [20] -->
.070428 −5.62ln(x)

<!-- b000383 | references | pages [20] -->
x = GDP per capita

<!-- b000384 | references | pages [20] -->
4

<!-- b000385 | references | pages [20] -->
Birth Rate

<!-- b000386 | references | pages [20] -->
x = GDP per capita

<!-- b000387 | references | pages [20] -->
5

<!-- b000388 | references | pages [20] -->
Life Expectancy

<!-- b000389 | references | pages [20] -->
6.6354ln(x) + 10.754

<!-- b000390 | references | pages [20] -->
1.41812x0.7587 ∗(1.628 ∗

<!-- b000391 | references | pages [20] -->
x = Wealth per capita,

<!-- b000392 | references | pages [20] -->
6

<!-- b000393 | references | pages [20] -->
Total

<!-- b000394 | references | pages [20] -->
Energy

<!-- b000395 | references | pages [20] -->
10−6) ∗P

<!-- b000396 | references | pages [20] -->
P = population

<!-- b000397 | references | pages [20] -->
Consumption

<!-- b000398 | references | pages [20] -->
HIVn + HIVn ∗(5.51 ∗

<!-- b000399 | references | pages [20] -->
HIVn = total # HIV

<!-- b000400 | references | pages [20] -->
7

<!-- b000401 | references | pages [20] -->
HIVn+1

<!-- b000402 | references | pages [20] -->
10−9(P −HIVn)(1 −.9 ∗

<!-- b000403 | references | pages [20] -->
in yr. n, U = Contra-

<!-- b000404 | references | pages [20] -->
ceptive Use

<!-- b000405 | references | pages [20] -->
U)) −0.02455 ∗HIVn

<!-- b000406 | references | pages [20] -->
Total Energy, Renew-

<!-- b000407 | references | pages [20] -->
8

<!-- b000408 | references | pages [20] -->
Non-Renewable

<!-- b000409 | references | pages [20] -->
Energy Use

<!-- b000410 | references | pages [20] -->
able

<!-- b000411 | references | pages [20] -->
Total Energy Consump-

<!-- b000412 | references | pages [20] -->
tion - Renewable

<!-- b000413 | references | pages [20] -->
(3.1536 ∗10−10) ∗x

<!-- b000414 | references | pages [20] -->
x = Total Wealth

<!-- b000415 | references | pages [20] -->
9

<!-- b000416 | references | pages [20] -->
Hydropower

<!-- b000417 | references | pages [20] -->
(−1.316ln(x)

<!-- b000418 | references | pages [20] -->
Popn = total pop. in

<!-- b000419 | references | pages [20] -->
10

<!-- b000420 | references | pages [20] -->
Popn+1

<!-- b000421 | references | pages [20] -->
+

<!-- b000422 | references | pages [20] -->
14.576)(.01)∗Popn+Popn

<!-- b000423 | references | pages [20] -->
yr. n, x = Wealth per

<!-- b000424 | references | pages [20] -->
capita

<!-- b000425 | references | pages [20] -->
11

<!-- b000426 | references | pages [20] -->
Wealthn+1

<!-- b000427 | references | pages [20] -->
Wealthn

<!-- b000428 | references | pages [20] -->
wealth

<!-- b000429 | references | pages [20] -->
in

<!-- b000430 | references | pages [20] -->
−

<!-- b000431 | references | pages [20] -->
∗

<!-- b000432 | references | pages [20] -->
=

<!-- b000433 | references | pages [20] -->
=

<!-- b000434 | references | pages [20] -->
total

<!-- b000435 | references | pages [20] -->
Wealthn(1

<!-- b000436 | references | pages [20] -->
0.06

<!-- b000437 | references | pages [20] -->
HIVn) + (1.58 ∗108) ∗x +

<!-- b000438 | references | pages [20] -->
yr.

<!-- b000439 | references | pages [20] -->
n,

<!-- b000440 | references | pages [20] -->
7000 ∗J

<!-- b000441 | references | pages [20] -->
x=Hydropower,

<!-- b000442 | references | pages [20] -->
jobs

<!-- b000443 | references | pages [20] -->
J

<!-- b000444 | references | pages [20] -->
=

<!-- b000445 | references | pages [20] -->
150000

<!-- b000446 | references | pages [20] -->
M = # of Mining jobs,

<!-- b000447 | references | pages [20] -->
12

<!-- b000448 | references | pages [20] -->
Jobs

<!-- b000449 | references | pages [20] -->
+

<!-- b000450 | references | pages [20] -->
1+2e−(2.9∗10−6)∗M

<!-- b000451 | references | pages [20] -->
T = # of Tourism jobs,

<!-- b000452 | references | pages [20] -->
150000

<!-- b000453 | references | pages [20] -->
+

<!-- b000454 | references | pages [20] -->
1+4.7692e−DiT ∗(7.5∗10−6)

<!-- b000455 | references | pages [20] -->
A = # of Agriculture

<!-- b000456 | references | pages [20] -->
jobs

<!-- b000457 | references | pages [20] -->
125000

<!-- b000458 | references | pages [20] -->
3 ∗e−(2.4∗10−6)∗A

<!-- b000459 | references | pages [20] -->
1+ 2

<!-- b000460 | references | pages [20] -->
The equations in the above table were derived through linearized plots of data extracted from

<!-- b000461 | references | pages [20] -->
Worldbank and WHO, giving net relationship trends between each variable connected by an arrow

<!-- b000462 | references | pages [20] -->
in the Figure 6 map
