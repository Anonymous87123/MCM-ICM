# P-C-2011-11325-4609137d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only T1 ________________ T2 ________________ T3 ________________

<!-- b000003 | prose | pages [1] -->
For office use only F1 ________________ F2 ________________ F3 ________________

<!-- b000004 | prose | pages [1] -->
Problem Chosen

<!-- b000005 | prose | pages [1] -->
T4 ________________

<!-- b000006 | prose | pages [1] -->
F4 ________________

<!-- b000007 | heading | pages [1] -->
2011 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000008 | prose | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000009 | prose | pages [1] -->
Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000010 | heading | pages [1] -->
Executive Summary

<!-- b000011 | prose | pages [1] -->
The electric car market needs to be stimulated by investments in technol- ogy, infrastructure, and buying incentives. Modeling results have shown that without these inﬂuences, low market penetration rates will persist for decades. When coupled with investments in renewable electrical generation capacity, widespread use of battery electric vehicles has the potential to reduce yearly carbon emissions from the transportation sector by 53%. Annual oil consump- tion can likewise be reduced by 70% in 20 years. Furthermore, these investments would have the eﬀect of creating several million jobs, reducing tailpipe emissions and decreasing human health costs.

<!-- b000012 | prose | pages [1] -->
Eﬀorts to introduce electric vehicle ﬂeets into urban environments are on the cusp of breaking through. Such a large scale shift in transportation technology could have wide-ranging eﬀects that should be examined. This report analyzes the potential economic, environmental, social and health beneﬁts and possible consequences of this market change. Though data for electric vehicle operation is limited, a simulation model was developed to predict the competition and interaction of two types of electric vehicles on the road. Model results were then used to quantify the consequences of the predicted market shifts.

<!-- b000013 | prose | pages [1] -->
A Lotka-Volterra ecological competition model was adapted to describe the behavior of the passenger vehicle market.

<!-- b000014 | prose | pages [1] -->
The separate populations of gasoline-powered internal combustion engine vehicles (ICE), plug-in hybrid ve- hicles (PHEV) and battery-electric vehicles (BEVs) are assumed to perform in a similar manner to organisms competing for a shared, but limited resource. For organisms, this resource might be a food supply; in the vehicle market, man- ufacturers compete for consumer dollars. The Lotka-Volterra equations used describe the time rate of change for three dependent variables. These variables represent the population of registered vehicles of each type in an auto market. The model parameters describe growth rates, interspecies competition and a population carrying capacity. These parameters indirectly relate to consumer preferences, economic conditions, government inﬂuences and improvements in automotive technologies. Variables used in the model are listed in Table 0.1.

<!-- b000015 | prose | pages [1] -->
Intrinsic growth rates were assumed to be constant, but reﬁnements to the

<!-- b000016 | furniture | pages [2] -->
Team # 11325

<!-- b000017 | furniture | pages [2] -->
Page 2 of 20

<!-- b000018 | prose | pages [2] -->
model could describe them as functions of time, market forces, or stochastic variables. The carrying capacity was assumed to grow at 1%, consistent with the human population growth rate of the US (The World Bank Group, 2011). Model parameters were assumed to be lumped, deterministic variables reﬂect- ing all aspects inﬂuencing consumer choice. Five scenarios were investigated to simulate changes in conditions aﬀecting the auto market. A base scenario used current yearly growth rates and current populations of each vehicle class. Other scenarios investigated eﬀects of high oil prices, increased battery performance, government investment, and high electricity rates.

<!-- b000019 | prose | pages [2] -->
Furthermore, an economic analysis was conducted to compare the present day value of two vehicle models currently available. The analysis These results were used to examine the current competitiveness of these vehicles and consider the level of government support that would be adequate to encourage consumer investment in BEVs. Taking into account the time value of money and a discount rate equal to the rate of inﬂation, the present value of each vehicle was calculated. This analysis showed that without current government subsidies, the Nissan Leaf has lower present value than the Honda Civic and so competes at a ﬁscal disadvantage against the Civic. A best-case scenario showed that the Leaf is competitive without subsidies. This scenario postulated a linear rise in gas prices to $5 /gallon, increased BEV vehicle eﬃciency (in kWh/mile driven) and higher resale values due to improving battery technology.

<!-- b000020 | prose | pages [2] -->
The primary weakness of this model is the lack of data available for model calibration and testing. Because so few purely electric vehicles are on the road, and even fewer statistics are available to describe the history of market shares of BEVs, the model could not be cal- ibrated. Reﬁnements of the parameters and growth rates would signiﬁcantly improve the validity of the model. Unfortunately an analysis of the model’s sensitivity to perturbations in its input parameters was not completed due to time constraints.

<!-- b000021 | prose | pages [2] -->
The scenarios investigated gave long term projections for a shift to BEVs from traditional ICE vehicles. All scenarios predicted an eventual shift but the timing varied signiﬁcantly depending on the growth rates and the values of the competitiveness parameters. With a signiﬁcant initial investment to increase the numbers of BEVs on the road, corresponding to an increase in the initial value of E and H, the equilibrium point between ICEs and BEVs occurs in the year 2030, compared to the base case of 2035.

<!-- b000022 | prose | pages [2] -->
If coal is expensive and battery prices remain high this point does not occur until 2043. If oil prices rise rapidly, increasing the competitiveness coeﬃcients of BEVs, this point occurs in 2028. When all factors combine to create the best case scenario for BEVs - oil prices are high, battery technology improves, and electricity is comparatively inexpensive- then the model predicts that BEVs, ICEs, and PHEVs would all be present in approximately equal numbers as early as 2027.

<!-- b000023 | furniture | pages [3] -->
Page 3 of 20

<!-- b000024 | furniture | pages [3] -->
Team # 11325

<!-- b000025 | heading | pages [3] -->
Growth Model

<!-- b000026 | prose | pages [3] -->
description variable units number of ICE vehicles G(t) - number of BEVs E(t) - number of PHEVs G(t) -

<!-- b000027 | prose | pages [3] -->
intrinsic ICE growth rate rG 1/year maximum ICE population KG - eﬀect of ICE on BEV βG - eﬀect of ICE on PHEV γG -

<!-- b000028 | prose | pages [3] -->
intrinsic BEV growth rate rE 1/year maximum BEV population KE - eﬀect of BEV on ICE αE - eﬀect of BEV on PHEV γE -

<!-- b000029 | prose | pages [3] -->
intrinsic PHEV growth rate rH 1/year maximum PHEV population KH - eﬀect of PHEV on ICE αH - eﬀect of PHEV on BEV βH -

<!-- b000030 | heading | pages [3] -->
Economic Model

<!-- b000031 | prose | pages [3] -->
initial capital investment C0 US $ salvage value at end of life cycle L US $ net beneﬁt after each year Bt US $ net cost after each year Rt US $

<!-- b000032 | prose | pages [3] -->
nominal interest rate I % compounding period k - vehicle life cycle n yr eﬀective annual interest rate ieff % annual maintenance cost Mc US $

<!-- b000033 | caption | pages [3] -->
Table 0.1: Variables used throughout the model.

<!-- b000034 | prose | pages [4] -->
Electric cars as a widespread

<!-- b000035 | prose | pages [4] -->
means of transportation

<!-- b000036 | prose | pages [4] -->
Exploring impacts on the environment and society using an adapted ecological competition

<!-- b000037 | heading | pages [4] -->
model

<!-- b000038 | prose | pages [4] -->
ICM Team # 11325

<!-- b000039 | heading | pages [4] -->
14 February, 2011

<!-- b000040 | prose | pages [5] -->
Page i of iii

<!-- b000041 | furniture | pages [5] -->
Team # 11325

<!-- b000042 | heading | pages [5] -->
Contents

<!-- b000043 | contents | pages [5] -->
1

<!-- b000044 | heading | pages [5] -->
Introduction

<!-- b000045 | prose | pages [5] -->
1 Problem Formulation . . . . . . . . . . . . . . . . . . . . . . . . 1.1 1 Model Goals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000046 | prose | pages [5] -->
2 Methodology

<!-- b000047 | prose | pages [5] -->
2

<!-- b000048 | prose | pages [5] -->
2 Mathematical Model . . . . . . . . . . . . . . . . . . . . . . . . 2.1 2 . . . . . . . . . . . . . . . . . . . . . 2.1.1 Numerical Method 2 . . . . . . . . . . . . . . . . . . . . . 2.1.2 Model Calibration 3 Economic Eﬀects . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 4 Eﬀects of Changing Technology . . . . . . . . . . . . . . 2.2.1 4 Present Worth Model . . . . . . . . . . . . . . . . . . . . 2.2.2 4 Eﬀects on the Environment 2.2.3 . . . . . . . . . . . . . . . .

<!-- b000049 | prose | pages [5] -->
4 . . . . . . . . . . . . . . . . . . . . . 2.2.4 Renewable Energy 5 Eﬀects on Society . . . . . . . . . . . . . . . . . . . . . . 2.2.5 5 Eﬀects on Human Health . . . . . . . . . . . . . . . . . . 2.2.6

<!-- b000050 | prose | pages [5] -->
3

<!-- b000051 | heading | pages [5] -->
Results

<!-- b000052 | prose | pages [5] -->
5

<!-- b000053 | prose | pages [5] -->
5 Economics of current BEVs vs. ICEs . . . . . . . . . . . . . . . 3.1 5 . . . . . . . . . . . . . . . . . . . . . 3.2 Population Model Results 6 Base Scenario . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1 6 Scenario 1: Heavy investment in electric vehicles . . . . . 3.2.2 8 Scenario 2: Electricity becomes more expensive 3.2.3 . . . . .

<!-- b000054 | prose | pages [5] -->
9 Scenario 3: Oil prices rise 3.2.4 . . . . . . . . . . . . . . . . .

<!-- b000055 | prose | pages [5] -->
10 Scenario 4: Best case for BEVs 3.2.5 . . . . . . . . . . . . . .

<!-- b000056 | prose | pages [5] -->
11 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 Emissions 11 Airborne pollutants . . . . . . . . . . . . . . . . . . . . . 3.3.1 11 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.2 CO2 12 Oil consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 12 Electricity Demand . . . . . . . . . . . . . . . . . . . . . . . . . 3.5

<!-- b000057 | prose | pages [5] -->
4

<!-- b000058 | heading | pages [5] -->
Discussion

<!-- b000059 | prose | pages [5] -->
13

<!-- b000060 | prose | pages [5] -->
15 Model Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 15 Demand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 15 Power Supply . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 15 Health . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 16 Environment and Pollution . . . . . . . . . . . . . . . . . . . . . 4.5 16 Oil Consumption . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6 16 Economics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.7 16 Government Support . . . . . . . . . . . . . . . . . . . . . . . . 4.8

<!-- b000061 | prose | pages [5] -->
5

<!-- b000062 | heading | pages [5] -->
Conclusions

<!-- b000063 | prose | pages [5] -->
17

<!-- b000064 | prose | pages [5] -->
18 Recommendations for further study related to this model . . . . 5.1

<!-- b000065 | prose | pages [5] -->
6

<!-- b000066 | heading | pages [5] -->
Bibliography

<!-- b000067 | references | pages [5] -->
18

<!-- b000068 | references | pages [5] -->
19

<!-- b000069 | references | pages [6] -->
Page ii of iii

<!-- b000070 | furniture | pages [6] -->
Team # 11325

<!-- b000071 | references | pages [6] -->
List of Tables

<!-- b000072 | references | pages [6] -->
Variables used throughout the model. . . . . . . . . . . . . . . .

<!-- b000073 | references | pages [6] -->
0.1

<!-- b000074 | references | pages [6] -->
3

<!-- b000075 | references | pages [6] -->
Deﬁnitions of the dependant variable and the initial conditions.

<!-- b000076 | references | pages [6] -->
2.1

<!-- b000077 | references | pages [6] -->
3

<!-- b000078 | references | pages [6] -->
Deﬁnitions of the parameters used and their units. . . . . . . . .

<!-- b000079 | references | pages [6] -->
2.2

<!-- b000080 | references | pages [6] -->
3

<!-- b000081 | references | pages [6] -->
The economic model’s sensitivity to changes in interest rates,

<!-- b000082 | references | pages [6] -->
3.1

<!-- b000083 | references | pages [6] -->
salvage value, eﬃciency and maintenance costs.

<!-- b000084 | references | pages [6] -->
. . . . . . . . .

<!-- b000085 | references | pages [6] -->
6

<!-- b000086 | references | pages [6] -->
Change in emissions over the period 2010-2060 in the base scenario. 12

<!-- b000087 | references | pages [6] -->
3.2

<!-- b000088 | references | pages [6] -->
List of Figures

<!-- b000089 | references | pages [6] -->
Base scenario. The BEV enters the market with a competitive

<!-- b000090 | references | pages [6] -->
3.1

<!-- b000091 | references | pages [6] -->
advantage over the PHEVs and ICE cars, but the low initial

<!-- b000092 | references | pages [6] -->
market penetration hinders the speed at which they overtake the

<!-- b000093 | references | pages [6] -->
number of ICE cars on the road. . . . . . . . . . . . . . . . . . .

<!-- b000094 | references | pages [6] -->
7

<!-- b000095 | references | pages [6] -->
Scenario 1. Additional infrastructure stimulates accelerated adop-

<!-- b000096 | references | pages [6] -->
3.2

<!-- b000097 | references | pages [6] -->
tion of the BEV and PHEV, making their initial populations ten

<!-- b000098 | references | pages [6] -->
times larger than the base case. . . . . . . . . . . . . . . . . . .

<!-- b000099 | references | pages [6] -->
8

<!-- b000100 | references | pages [6] -->
Scenario 2. The BEV and PHEVs enter the market with a com-

<!-- b000101 | references | pages [6] -->
3.3

<!-- b000102 | references | pages [6] -->
petitive advantage over ICE cars, but this advantage is tempered

<!-- b000103 | references | pages [6] -->
The equivalence point is delayed by

<!-- b000104 | references | pages [6] -->
by high electricity rates.

<!-- b000105 | references | pages [6] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | references | pages [6] -->
several years, to 2042.

<!-- b000107 | references | pages [6] -->
9

<!-- b000108 | references | pages [6] -->
Scenario 3. The BEV and PHEVs enter the market with a com-

<!-- b000109 | references | pages [6] -->
3.4

<!-- b000110 | references | pages [6] -->
petitive advantage over ICE cars. This advantage is increased

<!-- b000111 | references | pages [6] -->
due to high oil prices. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000112 | references | pages [6] -->
10

<!-- b000113 | references | pages [6] -->
Scenario 4. The BEV and PHEVs enter the market with a com-

<!-- b000114 | references | pages [6] -->
3.5

<!-- b000115 | references | pages [6] -->
petitive advantage over ICE cars. This advantage is heightened

<!-- b000116 | references | pages [6] -->
by early infrastructure investment, cheap battery technology and

<!-- b000117 | references | pages [6] -->
high oil prices. Both PHEVs and BEVs are adopted early, but

<!-- b000118 | references | pages [6] -->
the BEV ultimately dominates the market due to reliance on

<!-- b000119 | references | pages [6] -->
non-petroleum energy sources. . . . . . . . . . . . . . . . . . . .

<!-- b000120 | references | pages [6] -->
11

<!-- b000121 | references | pages [6] -->
CO2 production drops as the BEV begins to dominate the mar-

<!-- b000122 | references | pages [6] -->
3.6

<!-- b000123 | references | pages [6] -->
ket. Advancing the competitiveness of the BEV and PHEV leads

<!-- b000124 | references | pages [6] -->
to the greatest reductions in CO2 by the transportation sector. .

<!-- b000125 | references | pages [6] -->
13

<!-- b000126 | references | pages [6] -->
Consumption of oil by the transportation sector drops at a faster

<!-- b000127 | references | pages [6] -->
3.7

<!-- b000128 | references | pages [6] -->
rate the quicker the electric car gains market share.

<!-- b000129 | references | pages [6] -->
. . . . . .

<!-- b000130 | references | pages [6] -->
14

<!-- b000131 | references | pages [6] -->
The added electrical burden due to charging BEVs and PHEVs

<!-- b000132 | references | pages [6] -->
3.8

<!-- b000133 | references | pages [6] -->
will require several billion MWh of electricity to be produced.

<!-- b000134 | references | pages [6] -->
.

<!-- b000135 | references | pages [6] -->
14

<!-- b000136 | furniture | pages [7] -->
Team # 11325

<!-- b000137 | furniture | pages [7] -->
Page 1 of 20

<!-- b000138 | references | pages [7] -->
1

<!-- b000139 | heading | pages [7] -->
Introduction

<!-- b000140 | prose | pages [7] -->
Electric cars have the potential to outperform traditional Internal Combus- tion Engine (ICE) vehicles, but whereas the eﬀects of driving ICE cars have been well studied, the eﬀects of Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) suﬀer from considerable uncertainty. This report attempts to answer some of the questions surrounding widespread BEV and PHEV use. An ecological competition model is adapted to describe the population dynamics between ICE cars, BEVs and PHEVs. Model results are interpreted using present-day ﬁgures of car ownership costs, tailpipe and power plant emissions, electrical generation capacity, job creation and oil consumption. This analysis allows a rough estimate of the greenhouse gas (GHG) emissions, extra electrical demands due to electric vehicle use, and speciﬁc measures for manufacturers and governments to speed electric vehicle adoption.

<!-- b000141 | prose | pages [7] -->
1.1 Problem Formulation

<!-- b000142 | prose | pages [7] -->
Alternative fuel vehicles present possible solutions to pollution and energy problems. The solutions are not simple and using an alternative fuel may not deliver the energy savings or pollution decreases anticipated. BEVs do not use oil, but because most electricity generated in the US comes from coal feedstocks, BEVs do not represent a wholesale movement away from fossil fuels. The en- vironmental impact of coal produced electricity varies by location depending on the infrastructure and applicable emissions regulations. Alternative sources of electricity are possible and research and development of solar, wind, wave and other sources of zero carbon electricity could make an electric car a viable alternative.

<!-- b000143 | prose | pages [7] -->
Economic considerations are important and similarly complex. Price ﬂuc- tuations for oil and coal are unavoidable and diﬃcult to predict, varying both regionally and temporally. Additionally, initial costs of new technology are high, but with increased production driving development prices can be expected to decrease. Government support in the early stages of development of new tech- nologies is critical, but cannot be undertaken without research into the viability and marketability of the technology.

<!-- b000144 | prose | pages [7] -->
Electric cars also have limitations in use that are not seen in internal combus- tion engines. Current models have fairly short ranges, and little infrastructure exists at this time for recharging in public locations. Both of these factors can be expected to improve as more vehicles are manufactured and commercial op- erations begin to provide services for BEV owners. Charging time is also a signiﬁcant consideration. Current estimates indicate a full charge takes approx- imately ﬁve hours (Perujo and Cuiﬀo, 2010). Rapid charging at the electric vehicle equivalent of a ﬁlling station would place huge demands on the elec- trical grid. Alternately, a battery exchange program would allow charging at a slower rate; however, higher initial capital costs would be required to store, maintain and stockpile the batteries. Incentive for potential vehicle owners to buy BEVs would depend strongly on the amount of infrastructure already in

<!-- b000145 | furniture | pages [8] -->
Page 2 of 20

<!-- b000146 | furniture | pages [8] -->
Team # 11325

<!-- b000147 | prose | pages [8] -->
place or under construction. Consumers need to know that a new automotive technology has the necessary resources for both convenience and sustainability.

<!-- b000148 | prose | pages [8] -->
1.2

<!-- b000149 | heading | pages [8] -->
Model Goals

<!-- b000150 | prose | pages [8] -->
To investigate the viability of a transition to electric vehicles a model was developed to estimate market penetration of electric vehicles under varying con- ditions. These conditions include the prices and availability of oil and coal, the investment in infrastructure, and the rate of development of battery technology and alternative energy sources. The Lotka-Volterra equations describing inter- species competition were used to simulate the competition between standard ICEs, BEVs, and PHEVs. The estimate of market share was used to calculate changes in CO2 production, oil consumption, and electricity demands. A sep- arate but related economic analysis was also performed comparing the Nissan Leaf and the Honda Civic SI to evaluate the cost to the consumer of each vehicle for an eight year life cycle.

<!-- b000151 | prose | pages [8] -->
2 Methodology

<!-- b000152 | prose | pages [8] -->
2.1

<!-- b000153 | heading | pages [8] -->
Mathematical Model

<!-- b000154 | prose | pages [8] -->
The interaction between gasoline, electric, and hybrid vehicles can be repre- sented by a system of ordinary diﬀerential equations. The dependant variables in the following model are listed in Table 2.1. G(t), E(t), and H(t) represent the total amount of ICEs, BEVs and PHEVs registered to owners at any time t. The initial values for these variables were determined from current data for registered vehicles (North American Transportation Statistics Database, 2011).

<!-- b000155 | prose | pages [8] -->
An ecological approach to competition modeling is represented in the Lotka- Volterra equations (Wolfram Demonstrations Project, 2010).

<!-- b000156 | prose | pages [8] -->
This approach considers the eﬀect of multiple species competing for the same resource. The three equations that are used to represent the rates of change in automotive populations are shown in Equations 1, 2, and 3.

<!-- b000157 | prose | pages [8] -->


<!-- b000158 | prose | pages [8] -->


<!-- b000159 | prose | pages [8] -->
1 −G + αEE + αHH

<!-- b000160 | prose | pages [8] -->
dG

<!-- b000161 | prose | pages [8] -->
dt =rGG

<!-- b000162 | prose | pages [8] -->


<!-- b000163 | prose | pages [8] -->
(1)

<!-- b000164 | prose | pages [8] -->
KG

<!-- b000165 | prose | pages [8] -->


<!-- b000166 | prose | pages [8] -->
1 −E + βGG + βHH

<!-- b000167 | prose | pages [8] -->
dE

<!-- b000168 | prose | pages [8] -->
dt =rEE

<!-- b000169 | prose | pages [8] -->


<!-- b000170 | prose | pages [8] -->
(2)

<!-- b000171 | prose | pages [8] -->
KE

<!-- b000172 | prose | pages [8] -->


<!-- b000173 | prose | pages [8] -->
1 −H + γEE + γGG

<!-- b000174 | prose | pages [8] -->
dH

<!-- b000175 | prose | pages [8] -->
dt =rHH

<!-- b000176 | prose | pages [8] -->
2.1.1 Numerical Method

<!-- b000177 | prose | pages [8] -->
(3)

<!-- b000178 | prose | pages [8] -->
KH

<!-- b000179 | prose | pages [8] -->
Frequently, a system of ODEs is diﬃcult to solve by hand and a numerical approximation is sought. For equations such as these, computer algorithms that generate numerical solutions within a speciﬁed error tolerance are an eﬃcient tool and are favored over tedious analytical eﬀorts (Chapra and Canale, 2002).

<!-- b000180 | furniture | pages [9] -->
Page 3 of 20

<!-- b000181 | furniture | pages [9] -->
Team # 11325

<!-- b000182 | caption | pages [9] -->
Table 2.1: Deﬁnitions of the dependant variable and the initial conditions.

<!-- b000183 | prose | pages [9] -->
representation variable description number of ICE vehicles G(t)

<!-- b000184 | prose | pages [9] -->
number of BEVs E(t)

<!-- b000185 | prose | pages [9] -->
number of PHEVs H(t)

<!-- b000186 | prose | pages [9] -->
initial condition source G(0) = 246 × 106

<!-- b000187 | prose | pages [9] -->
E(0) = .01 × 106

<!-- b000188 | prose | pages [9] -->
H(0) = .1 × 106

<!-- b000189 | caption | pages [9] -->
Table 2.2: Deﬁnitions of the parameters used and their units.

<!-- b000190 | prose | pages [9] -->
parameter intrinsic ICE growth rate maximum ICE population intrinsic BEV growth rate

<!-- b000191 | prose | pages [9] -->
maximum BEV population intrinsic PHEV growth rate maximum PHEV population

<!-- b000192 | prose | pages [9] -->
eﬀect of BEV on ICE eﬀect of PHEV on ICE eﬀect of ICE on BEV

<!-- b000193 | prose | pages [9] -->
eﬀect of PHEV on BEV eﬀect of BEV on PHEV eﬀect of ICE on PHEV

<!-- b000194 | prose | pages [9] -->
variable value units rG 1.52 1/year KG 300E6 vehicles rE 1.52 1/year

<!-- b000195 | prose | pages [9] -->
KE 300E6 vehicles rH 1.52 1/year KH 300E6 vehicles

<!-- b000196 | prose | pages [9] -->
αE 1.2 dimensionless αH 1.2 dimensionless βG 0.7 dimensionless

<!-- b000197 | prose | pages [9] -->
βH 1.0 dimensionless γE 0.8 dimensionless γG 1.2 dimensionless

<!-- b000198 | prose | pages [9] -->
The numerical method used to solve the system of ODEs was Runge-Kutta- Fehlberg, using coeﬃcients derived by Cash-Karp. This method minimizes func- tional evaluations to derive 4th and 5th error-order approximations to the so- lution. The error is estimated to be proportional to 4yi+1 and 5yi+1. In the Runge-Kutta-Fehlberg algorithm, the step size ∆t is adjusted at each iteration to keep the error estimate between upper and lower bounds. This method al- lows computationally eﬃcient solutions without introducing excessive round-oﬀ error due to the ﬁnite precision of ﬂoating point arithmetic. The Runge-Kutta- Fehlberg method requires one initial value for each DE in the system (Chapra and Canale, 2002).

<!-- b000199 | prose | pages [9] -->
2.1.2

<!-- b000200 | heading | pages [9] -->
Model Calibration

<!-- b000201 | prose | pages [9] -->
The limited amounts of data available on sales and demand of alternative fuel vehicles, as well as the unpredictability of future costs of oil and electricity make reliable calibration of the model extremely challenging. The model can therefore be best used for running various scenarios and comparing outcomes.

<!-- b000202 | furniture | pages [10] -->
Page 4 of 20

<!-- b000203 | furniture | pages [10] -->
Team # 11325

<!-- b000204 | prose | pages [10] -->
2.2 Economic Eﬀects

<!-- b000205 | prose | pages [10] -->
The cost of fuel (gasoline and electricity) can be represented in the growth model via the competition parameters. As gasoline prices rise, an increasing electric car population has an enhanced eﬀect on the ICE population. If the cost of electricity rises, gasoline engines should be more competitive than BEVs.

<!-- b000206 | prose | pages [10] -->
The proposed initial infrastructure investment will directly aﬀect the ini- tial conditions of the model. A larger investment in charging or battery swap stations, charging ports in public parking facilities and research to improve technology will result in a greater inﬂux of BEVs at the start of the simulation.

<!-- b000207 | prose | pages [10] -->
Eﬀects of Changing Technology 2.2.1

<!-- b000208 | prose | pages [10] -->
Battery technology has been improving rapidly. Prices, life cycles, range, and eﬃciencies of batteries will dictate the strength of the BEV population. Increases in vehicle eﬃciency through technologies such as regenerative braking, decreased vehicle weight, and more eﬃcient vehicle systems will also reduce operating costs.

<!-- b000209 | prose | pages [10] -->
2.2.2

<!-- b000210 | heading | pages [10] -->
Present Worth Model

<!-- b000211 | prose | pages [10] -->
The economic viability of the BEV and the PHEV can be quantiﬁed in the present worth method. The EIA forecast gasoline prices and electricity rates were converted to cost per year based on driving an average of 11,720 miles per year (US Energy Information Agency, 2010b).

<!-- b000212 | prose | pages [10] -->
This amount was added to average maintenance and repair costs of approximately $500/year given by Automotive.com (2011) to yield a cost per year to operate the vehicle (Rt). Equation 4 was used to compute the present value (PV ) of a nonuniform series of costs (Willis and Finney, 2004).

<!-- b000213 | prose | pages [10] -->
With data for the Nissan Leaf and the Honda Civic Si obtained from Callaway (2011) and Penn (2011), a comparison was made for the cost of purchasing and operating each vehicle for eight years. The model can easily be adjusted for changes in interest rate, resource costs, maintenance costs, driving distance, battery technology, and resale percentage (Equation 4).

<!-- b000214 | prose | pages [10] -->
n

<!-- b000215 | prose | pages [10] -->
Bt −Rt

<!-- b000216 | prose | pages [10] -->
X

<!-- b000217 | prose | pages [10] -->
PV = −C0 + L[SPPW(i, n)] +

<!-- b000218 | prose | pages [10] -->
where

<!-- b000219 | prose | pages [10] -->
i = ieff =

<!-- b000220 | prose | pages [10] -->
2.2.3 Eﬀects on the Environment

<!-- b000221 | prose | pages [10] -->
(4) (1 + i)t

<!-- b000222 | prose | pages [10] -->
t=1

<!-- b000223 | prose | pages [10] -->
k −1

<!-- b000224 | prose | pages [10] -->
1 + I

<!-- b000225 | prose | pages [10] -->
   

<!-- b000226 | prose | pages [10] -->
k

<!-- b000227 | prose | pages [10] -->
Though the cost per kWh for electricity is low compared to fuel prices in a miles per dollar comparison, conservation of electricity will be essential. Using ﬁgures from Perujo and Cuiﬀo (2010), the potential power demand of 100,000 electric vehicles charging simultaneously is calculated to be 440 GW. If the

<!-- b000228 | furniture | pages [11] -->
Team # 11325

<!-- b000229 | furniture | pages [11] -->
Page 5 of 20

<!-- b000230 | prose | pages [11] -->
charging cycle were not regulated, and coincided with the peak demand, elec- tricity suppliers would have to build extra generation capacity to meet the additional demand. Considering that a typical coal-ﬁred generator has a capac- ity of 236 MW of power (US Energy Information Agency, 2009), this inﬂux of electricity demanding vehicles would require an additional 1,865 generators or their equivalents.

<!-- b000231 | prose | pages [11] -->
2.2.4 Renewable Energy

<!-- b000232 | prose | pages [11] -->
The availability of renewable energy resources needs to be fully exploited to accommodate a large spike in electricity consumption. The type and amount of non fossil fuel energy available varies by region, but maximum exploitation of these sources will signiﬁcantly reduce pollution.

<!-- b000233 | prose | pages [11] -->
2.2.5 Eﬀects on Society

<!-- b000234 | prose | pages [11] -->
Social beneﬁts can be quantiﬁed in terms of jobs. More production facili- ties, research positions, construction of infrastructure, vehicle design and main- tenance will be needed. The Political Economy Research Institute estimates that 18,000 jobs are created for every billion dollars spent on infrastructure, including direct and indirect employment (Heintz et al., 2010).

<!-- b000235 | prose | pages [11] -->
2.2.6 Eﬀects on Human Health

<!-- b000236 | prose | pages [11] -->
In this model, potential health risks are determined from the amount of pollutants emitted from vehicles when driven, including tailpipe emissions and emissions from coal ﬁred power plants. Health risks associated with NOx, SOx, and particulate matter can be represented monetarily. Health risks per ICE have been estimated to cost $103 per vehicle annually from particulate matter (Guo et al., 2010). These costs are incurred as a result of assigning monetary values to premature deaths and increased illness rates associated with particu- late pollution levels from cars.

<!-- b000237 | prose | pages [11] -->
3

<!-- b000238 | heading | pages [11] -->
Results

<!-- b000239 | prose | pages [11] -->
As represented in Equations 1–3, the behavior of G, E, and H is mostly controlled by the value of the interspeciﬁc competition coeﬃcients. Model pa- rameters were matched to the best available data describing growth rates of PHEVs, BEVs and ICEs, their relative competitiveness and the total number of registered cars. To describe the competition between BEVs and ICEs, the economic model predicted the BEV has a competitive edge against the ICE. The PHEV was assumed to be described by a competition factor of equal value.

<!-- b000240 | prose | pages [11] -->
3.1 Economics of current BEVs vs. ICEs

<!-- b000241 | prose | pages [11] -->
A 2003 Honda Civic sold for an average of $16,680 (HowStuﬀWorks.com, 2011) and a current good condition trade in value after 8 years and 100k miles

<!-- b000242 | furniture | pages [12] -->
Page 6 of 20

<!-- b000243 | furniture | pages [12] -->
Team # 11325

<!-- b000244 | prose | pages [12] -->
is about $4,000 (Kelley Blue Book, 2011). This is an average resale value of 24%. However, this does not factor in the time value of money. Multiplying the 2003 MSRP by the Single Payment Compound Amount, SPCA = (1 + i)n, factor, with a nominal interest rate (I) of 2% compounded monthly (k = 12), the present value is $19,571. which is a resale value of about 20%. Assuming a similar resale value, the 8 year, 100k mile salvage value (L) of a 2011 Honda Civic is : MSRP × 20% = 22, 405 × 0.2 = $4,551. With these values, PV = $33,487.

<!-- b000245 | prose | pages [12] -->
Lack of long term data on electric vehicles made estimating salvage values for the Nissan Leaf diﬃcult. If the maintenance costs and resale values are assumed to be equivalent to the Civic an initial comparison can be made strictly on the cost of fuel and capital costs. For the Leaf, with a MSRP of $32,780, an incentive tax credit of $7,500 (Penn, 2011), and an eight year salvage value of $6,556, PV = $27,803, $5,684 less than the Civic. Since it is not yet possible to determine the resale value of a BEV or its battery, sensitivity to these model inputs is useful. Table 3.1 presents a sensitivity analysis of the economic model.

<!-- b000246 | caption | pages [12] -->
Table 3.1: The economic model’s sensitivity to changes in interest rates, salvage

<!-- b000247 | prose | pages [12] -->
value, eﬃciency and maintenance costs.

<!-- b000248 | prose | pages [12] -->
Percent Change Civic Leaf L ± 5% Cost diﬀerential ∓24.3% - - −16.0% L + 5% - L −5% - Mc ± 20% +18.0% ∓12.7% - - Mc ± 20% - $/kWh ±5% kWh/km −5% ± 12.7% ∓2.0% - - - - + 3.9% $/gal ±5% - ± 9.8% −26.3% i + 3 i + 3

<!-- b000249 | heading | pages [12] -->
Population Model Results

<!-- b000250 | prose | pages [12] -->
3.2

<!-- b000251 | prose | pages [12] -->
As a comparison across several future scenarios, the time at which G is equal to E was used. Because the populations of vehicles span several orders of magnitude over the model time period, a semi-log scale is used to display the results.

<!-- b000252 | prose | pages [12] -->
3.2.1 Base Scenario

<!-- b000253 | prose | pages [12] -->
As a base case, the BEV and PHEV were presumed to be more competitive than the ICE vehicle. The projected increase in battery technology, combined with rising oil prices led this assumption. Further evidence of the BEV’s com- petitive advantage in the market is given by the economic analysis of the Nissan

<!-- b000254 | furniture | pages [13] -->
Team # 11325

<!-- b000255 | furniture | pages [13] -->
Page 7 of 20

<!-- b000256 | prose | pages [13] -->
Leaf against the Honda Civic (Section 3.1). For the base case, the model pa- rameters are those in Table 2.2. Results are given in Figure 3.1; G and E are equal in 2035.

<!-- b000257 | prose | pages [13] -->
1000

<!-- b000258 | prose | pages [13] -->
100

<!-- b000259 | prose | pages [13] -->
Number of cars (millions)

<!-- b000260 | prose | pages [13] -->
10

<!-- b000261 | prose | pages [13] -->
1

<!-- b000262 | prose | pages [13] -->
0.1

<!-- b000263 | prose | pages [13] -->
Gasoline cars

<!-- b000264 | prose | pages [13] -->
BEV cars

<!-- b000265 | prose | pages [13] -->
0.01

<!-- b000266 | prose | pages [13] -->
PHEV cars

<!-- b000267 | prose | pages [13] -->
Total cars

<!-- b000268 | prose | pages [13] -->
0.001

<!-- b000269 | prose | pages [13] -->
2010 2020 2030 2040 2050 2060

<!-- b000270 | prose | pages [13] -->
Simulation year

<!-- b000271 | caption | pages [13] -->
Figure 3.1: Base scenario.

<!-- b000272 | prose | pages [13] -->
The BEV enters the market with a competitive advantage over the PHEVs and ICE cars, but the low initial market penetration hinders the speed at which they overtake the number of ICE cars on the road.

<!-- b000273 | furniture | pages [14] -->
Team # 11325

<!-- b000274 | furniture | pages [14] -->
Page 8 of 20

<!-- b000275 | prose | pages [14] -->
3.2.2 Scenario 1: Heavy investment in electric vehicles

<!-- b000276 | prose | pages [14] -->
Additional investment will permit a larger initial BEV and PHEV popula- tion. This investment is assumed consist of measures that:

<!-- b000277 | prose | pages [14] -->
• Support converting ICE manufacturing plants to produce BEVs and PHEVs

<!-- b000278 | prose | pages [14] -->
• Encourage consumers to purchase BEVs and PHEVs instead of ICEs

<!-- b000279 | prose | pages [14] -->
• Support infrastructure development such as electrical grid improvements and charging stations

<!-- b000280 | prose | pages [14] -->
• Promote research into improving battery capacity and reducing battery cost

<!-- b000281 | prose | pages [14] -->
• Incentivize zero carbon electricity generation capacity

<!-- b000282 | prose | pages [14] -->
These measures are assumed to eﬀect a tenfold increase in initial BEVs and PHEVs populations in 2010. This change moves the ICE and BEV equilibrium point forward ten years with respect to the base scenario: G and E are equal in 2025 (Figure 3.1).

<!-- b000283 | prose | pages [14] -->
1000

<!-- b000284 | prose | pages [14] -->
100

<!-- b000285 | prose | pages [14] -->
Number of cars (millions)

<!-- b000286 | prose | pages [14] -->
10

<!-- b000287 | prose | pages [14] -->
1

<!-- b000288 | prose | pages [14] -->
Gasoline cars

<!-- b000289 | prose | pages [14] -->
0.1

<!-- b000290 | prose | pages [14] -->
BEV cars PHEV cars

<!-- b000291 | prose | pages [14] -->
Total cars

<!-- b000292 | prose | pages [14] -->
0.01

<!-- b000293 | prose | pages [14] -->
2010 2020 2030 2040 2050 2060

<!-- b000294 | prose | pages [14] -->
Simulation year

<!-- b000295 | caption | pages [14] -->
Figure 3.2: Scenario 1. Additional infrastructure stimulates accelerated adop-

<!-- b000296 | prose | pages [14] -->
tion of the BEV and PHEV, making their initial populations ten times larger than the base case.

<!-- b000297 | furniture | pages [15] -->
Team # 11325

<!-- b000298 | furniture | pages [15] -->
Page 9 of 20

<!-- b000299 | prose | pages [15] -->
3.2.3 Scenario 2: Electricity becomes more expensive

<!-- b000300 | prose | pages [15] -->
In the event that electricity becomes much more expensive, growth of BEVs would be hindered. PHEVs may still be able to hold a market share but battery performance will dictate to what degree. For this analysis, battery technology is assumed to improve slowly, while the price of oil continues to climb. Eventually the BEV becomes competitive and overtakes ICE vehicles. However, the timing of the equivalence point timing is retarded with respect to the base case (Figure 3.3). G equals E in 2042.

<!-- b000301 | prose | pages [15] -->
1000

<!-- b000302 | prose | pages [15] -->
100

<!-- b000303 | prose | pages [15] -->
Number of cars (millions)

<!-- b000304 | prose | pages [15] -->
10

<!-- b000305 | prose | pages [15] -->
1

<!-- b000306 | prose | pages [15] -->
0.1

<!-- b000307 | prose | pages [15] -->
Gasoline cars

<!-- b000308 | prose | pages [15] -->
BEV cars

<!-- b000309 | prose | pages [15] -->
0.01

<!-- b000310 | prose | pages [15] -->
PHEV cars

<!-- b000311 | prose | pages [15] -->
Total cars

<!-- b000312 | prose | pages [15] -->
0.001

<!-- b000313 | prose | pages [15] -->
2010 2020 2030 2040 2050 2060

<!-- b000314 | prose | pages [15] -->
Simulation year

<!-- b000315 | caption | pages [15] -->
Figure 3.3: Scenario 2. The BEV and PHEVs enter the market with a competi-

<!-- b000316 | prose | pages [15] -->
tive advantage over ICE cars, but this advantage is tempered by high electricity rates. The equivalence point is delayed by several years, to 2042.

<!-- b000317 | prose | pages [15] -->
In this scenario, PHEVs enjoy a decided market advantage over BEVs until oil prices rise too high. The increased price of driving the PHEV then causes a slide in the competitiveness against the purely electric powered BEV. To accomplish this change in the model the intrinsic growth rate of the BEV, rE, was decreased to 1.2, or a 20% year over year. This simulates the reluctance of customers to purchase a vehicle with high per-mile costs.

<!-- b000318 | furniture | pages [16] -->
Team # 11325

<!-- b000319 | furniture | pages [16] -->
Page 10 of 20

<!-- b000320 | prose | pages [16] -->
3.2.4 Scenario 3: Oil prices rise

<!-- b000321 | prose | pages [16] -->
This scenario assumes oil prices rise and stay high throughout the modeling period. The increased cost to operate the ICE is reﬂected in decreased compet- itiveness factors against the BEV and PHEV. αE and αB were both increased to 1.3, while βH was decreased to 0.6 and γG was decreased to 0.7. These mea- sures were to simulate the penalties the fossil fuel burning vehicles face against a purely electric BEV. The equivalence point occurred in 2028, only three years after the equivalence point in the base scenario.

<!-- b000322 | prose | pages [16] -->
1000

<!-- b000323 | prose | pages [16] -->
100

<!-- b000324 | prose | pages [16] -->
Number of cars (millions)

<!-- b000325 | prose | pages [16] -->
10

<!-- b000326 | prose | pages [16] -->
1

<!-- b000327 | prose | pages [16] -->
0.1

<!-- b000328 | prose | pages [16] -->
Gasoline cars

<!-- b000329 | prose | pages [16] -->
BEV cars

<!-- b000330 | prose | pages [16] -->
0.01

<!-- b000331 | prose | pages [16] -->
PHEV cars

<!-- b000332 | prose | pages [16] -->
Total cars

<!-- b000333 | prose | pages [16] -->
0.001

<!-- b000334 | prose | pages [16] -->
2010 2020 2030 2040 2050 2060

<!-- b000335 | prose | pages [16] -->
Simulation year

<!-- b000336 | caption | pages [16] -->
Figure 3.4: Scenario 3. The BEV and PHEVs enter the market with a com-

<!-- b000337 | prose | pages [16] -->
petitive advantage over ICE cars. This advantage is increased due to high oil prices.

<!-- b000338 | furniture | pages [17] -->
Team # 11325

<!-- b000339 | furniture | pages [17] -->
Page 11 of 20

<!-- b000340 | prose | pages [17] -->
3.2.5 Scenario 4: Best case for BEVs

<!-- b000341 | prose | pages [17] -->
For a best case scenario, Scenarios 1 and 3 were combined and advancements in battery technology were incorporated. This case produced an equilibrium point in 2018 (Figure 3.5).

<!-- b000342 | prose | pages [17] -->
1000

<!-- b000343 | prose | pages [17] -->
100

<!-- b000344 | prose | pages [17] -->
Number of cars (millions)

<!-- b000345 | prose | pages [17] -->
10

<!-- b000346 | prose | pages [17] -->
1

<!-- b000347 | prose | pages [17] -->
Gasoline cars

<!-- b000348 | prose | pages [17] -->
0.1

<!-- b000349 | prose | pages [17] -->
BEV cars PHEV cars

<!-- b000350 | prose | pages [17] -->
Total cars

<!-- b000351 | prose | pages [17] -->
0.01

<!-- b000352 | prose | pages [17] -->
2010 2020 2030 2040 2050 2060

<!-- b000353 | prose | pages [17] -->
Simulation year

<!-- b000354 | caption | pages [17] -->
Figure 3.5: Scenario 4. The BEV and PHEVs enter the market with a competi-

<!-- b000355 | prose | pages [17] -->
tive advantage over ICE cars. This advantage is heightened by early infrastruc- ture investment, cheap battery technology and high oil prices. Both PHEVs and BEVs are adopted early, but the BEV ultimately dominates the market due to reliance on non-petroleum energy sources.

<!-- b000356 | prose | pages [17] -->
3.3 Emissions

<!-- b000357 | prose | pages [17] -->
Widespread adoption of the electric car did not reduce emissions of all pol- lutants; although the emission rates of some pollutants appeared to be driven by economic growth irrespective of the vehicle choice. While electric vehicles do not have tailpipe emissions particulate matter from coal burning can increase tenfold from the gasoline engine (Argonne National Laboratories, 2011)

<!-- b000358 | prose | pages [17] -->
3.3.1 Airborne pollutants

<!-- b000359 | prose | pages [17] -->
While widespread use of the electric car is expected to reduce emissions in cities and in dense population centers, the overall eﬀect on emissions was mixed. Using data from the GREET model (Argonne National Laboratories, 2011) and

<!-- b000360 | furniture | pages [18] -->
Team # 11325

<!-- b000361 | furniture | pages [18] -->
Page 12 of 20

<!-- b000362 | prose | pages [18] -->
assuming a power generation mix of the present-day US, emissions of various pollutants were found to change over the modeled period as shown in Table 3.2.

<!-- b000363 | caption | pages [18] -->
Table 3.2: Change in emissions over the period 2010-2060 in the base scenario.

<!-- b000364 | prose | pages [18] -->
Pollutant Change Pollutant Change CH4 +39% N2O -64% GHGs +24% VOCs -84% CO -87% NOx +94% PM10 +940% PM2.5 +580% SOx +860%

<!-- b000365 | prose | pages [18] -->
Data from Argonne National Laboratories (2011) was used to describe to- tal emissions produced per mile driven of each type of vehicle. Although the model predicted a tenfold increase in PM2.5 and PM10 when electric vehicles became widespread, the model was not designed to describe the spatial distri- bution of particulate pollution. Higher concentration of particulate pollution emitted from power plants in areas with low population density may have a less costly eﬀect than the relatively low particulate pollution density emitted at ICE tailpipes in much more densely populated areas. The scrubbers and other emissions equipment added to new generation equipment may cause the overall emissions distribution from electric generators to decline over time. The estimates in Table 3.2 do not take these changes into account.

<!-- b000366 | prose | pages [18] -->
3.3.2 CO2

<!-- b000367 | prose | pages [18] -->
Using information from Environmental Protection Agency (2011), the data from each scenario were analyzed to predict CO2 emissions attributable to the transportation sector. As shown in Figure 3.6, the greatest reduction in CO2 production corresponded to bringing the more energy eﬃcient PHEVs and BEVs to market dominance the fastest. The worst case scenario modeled led to a drop in CO2 emissions, but on a signiﬁcantly lagged timescale. The rising trend evi- dent in the left and right hand sides of the curve reﬂect assumptions about the growth rate of the number of registered vehicles. Because the CO2 emissions of BEVs and PHEVs occur at power generation facilities rather than at the vehicle tailpipe, a growing population of BEVs and PHEVs will still cause higher emis- sions. However, because their energy eﬃciency is higher than ICEs, substantial carbon savings can be realized by switching to electric vehicles. Generating a greater proportion of the nation’s electricity from non-carbon sources, such as nuclear or wind, will allow further reductions in carbon produced by electric vehicles.

<!-- b000368 | prose | pages [18] -->
3.4 Oil consumption

<!-- b000369 | prose | pages [18] -->
Important considerations driving interest and investment into electric vehi- cles are the eﬀects of importing the vast majority of oil needed to fuel the grow-

<!-- b000370 | furniture | pages [19] -->
Page 13 of 20

<!-- b000371 | furniture | pages [19] -->
Team # 11325

<!-- b000372 | prose | pages [19] -->
1500

<!-- b000373 | prose | pages [19] -->
1400

<!-- b000374 | prose | pages [19] -->
1300

<!-- b000375 | prose | pages [19] -->
CO2/year (Million Metric Tons)

<!-- b000376 | prose | pages [19] -->
1200

<!-- b000377 | prose | pages [19] -->
1100

<!-- b000378 | prose | pages [19] -->
1000

<!-- b000379 | prose | pages [19] -->
900

<!-- b000380 | prose | pages [19] -->
800

<!-- b000381 | prose | pages [19] -->
700

<!-- b000382 | prose | pages [19] -->
600

<!-- b000383 | prose | pages [19] -->
2010 2015 2020 2025 2030

<!-- b000384 | prose | pages [19] -->
Base Case

<!-- b000385 | prose | pages [19] -->
Expensive Coal

<!-- b000386 | prose | pages [19] -->
Significant Investment Expensive Oil

<!-- b000387 | prose | pages [19] -->
Best Case

<!-- b000388 | prose | pages [19] -->
2035 2040 2045 2050 2055 2060

<!-- b000389 | prose | pages [19] -->
Simulation Year

<!-- b000390 | caption | pages [19] -->
Figure 3.6: CO2 production drops as the BEV begins to dominate the market.

<!-- b000391 | prose | pages [19] -->
Advancing the competitiveness of the BEV and PHEV leads to the greatest reductions in CO2 by the transportation sector.

<!-- b000392 | prose | pages [19] -->
ing transportation sector. Because the transportation sector consumes roughly three quarters of the US oil supply (US Energy Information Agency, 2010b), oil consumption will not be eliminated entirely, but may be signiﬁcantly reduced.

<!-- b000393 | prose | pages [19] -->
3.5 Electricity Demand

<!-- b000394 | prose | pages [19] -->
The US consumed 3,950 million MWh of electricity in 2009 (US Energy Information Agency, 2011). The greatest additional electrical demand projected by the model was 1,040 million MWh (Figure 3.8) in 2060. This demand is due to the need to charge the electric vehicle between trips. Although infrastructure improvements may be required to supply the added demand, the electrical grid appears capable of meeting the increase in demand due to the charging needs of electric vehicles.

<!-- b000395 | furniture | pages [20] -->
Page 14 of 20

<!-- b000396 | furniture | pages [20] -->
Team # 11325

<!-- b000397 | prose | pages [20] -->
3500

<!-- b000398 | prose | pages [20] -->
3000

<!-- b000399 | prose | pages [20] -->
2500

<!-- b000400 | prose | pages [20] -->
Barrels of Oil (in millions)

<!-- b000401 | prose | pages [20] -->
2000

<!-- b000402 | prose | pages [20] -->
1500

<!-- b000403 | prose | pages [20] -->
1000

<!-- b000404 | prose | pages [20] -->
500

<!-- b000405 | prose | pages [20] -->
0

<!-- b000406 | prose | pages [20] -->
2010 2015 2020 2025 2030

<!-- b000407 | prose | pages [20] -->
Base Case

<!-- b000408 | prose | pages [20] -->
Expensive Coal

<!-- b000409 | prose | pages [20] -->
Investment

<!-- b000410 | prose | pages [20] -->
Expensive Oil

<!-- b000411 | prose | pages [20] -->
Best Case

<!-- b000412 | prose | pages [20] -->
2035 2040 2045 2050 2055 2060

<!-- b000413 | prose | pages [20] -->
Simulation Year

<!-- b000414 | caption | pages [20] -->
Figure 3.7: Consumption of oil by the transportation sector drops at a faster

<!-- b000415 | prose | pages [20] -->
rate the quicker the electric car gains market share.

<!-- b000416 | prose | pages [20] -->
1.20E+09

<!-- b000417 | prose | pages [20] -->
Base Case

<!-- b000418 | prose | pages [20] -->
Expensive Coal

<!-- b000419 | prose | pages [20] -->
Investment

<!-- b000420 | prose | pages [20] -->
1.00E+09

<!-- b000421 | prose | pages [20] -->
Expensive Oil

<!-- b000422 | prose | pages [20] -->
Best Case

<!-- b000423 | prose | pages [20] -->
8.00E+08

<!-- b000424 | prose | pages [20] -->
Electricity Use (MWh)

<!-- b000425 | prose | pages [20] -->
6.00E+08

<!-- b000426 | prose | pages [20] -->
4.00E+08

<!-- b000427 | prose | pages [20] -->
2.00E+08

<!-- b000428 | prose | pages [20] -->
0.00E+00

<!-- b000429 | prose | pages [20] -->
2010 2015 2020 2025 2030 2035 2040 2045 2050 2055 2060

<!-- b000430 | prose | pages [20] -->
Simulation Year

<!-- b000431 | caption | pages [20] -->
Figure 3.8: The added electrical burden due to charging BEVs and PHEVs will

<!-- b000432 | prose | pages [20] -->
require several billion MWh of electricity to be produced.

<!-- b000433 | furniture | pages [21] -->
Team # 11325

<!-- b000434 | furniture | pages [21] -->
Page 15 of 20

<!-- b000435 | prose | pages [21] -->
4

<!-- b000436 | heading | pages [21] -->
Discussion

<!-- b000437 | prose | pages [21] -->
4.1

<!-- b000438 | heading | pages [21] -->
Model Parameters

<!-- b000439 | prose | pages [21] -->
The parameters α, β, and γ, as well as the initial conditions and the K values will all be region speciﬁc. Once data is collected on the amount of BEV impact on the sales and operation of gasoline vehicles, these parameters can be estimated more accurately. The values of rG, rE, and rH are the growth rates for the various types of vehicles. The numbers used for the base case are based on current trends and were assumed constant. In reality, these rates will be functions of supply and demand and could change dramatically with time.

<!-- b000440 | prose | pages [21] -->
4.2 Demand

<!-- b000441 | prose | pages [21] -->
The demand for BEVs will be restricted by range and infrastructure. Cur- rent buyers would likely be urban commuters, who may also own another vehicle for use on longer trips. Improvements in infrastructure allowing charging or bat- tery exchange at public locations would increase the appeal to individuals who require one vehicle for all purposes.

<!-- b000442 | prose | pages [21] -->
4.3 Power Supply

<!-- b000443 | prose | pages [21] -->
The demand on electricity could potentially be unmanageable. The model predicts increased annual electricity demands of more than a billion MWh over 50 years regardless of the scenario (Figure 3.8). This increased demand reﬂects an almost complete switch to electric vehicles. Half of this increase could occur in less than 20 years in the ”best case” scenario. To avoid a power supply short- age, additional electricity generation and conservation will almost certainly be necessary. Certain technologies have the potential to reduce the demand or change the timing of charging to reduce the need for extra generation capacity. Encouraging oﬀpeak charging would reduce the need for additional power gen- eration. Smart devices that delay charging to oﬀpeak hours regardless of when consumers plug in could decrease the need for additional power sources as well as the cost of operation for the consumer (Perujo and Cuiﬀo, 2010). Further improvements to battery technology could increase the battery energy density while decreasing the battery mass. This in turn would lead to increased energy eﬃciency (in kWh/mile driven by BEVs), thus lowering charging demands. Other technology could utilize the electric storage of the grid-connected electric vehicles to provide extra capacity without building generation plants (Perujo and Cuiﬀo, 2010).

<!-- b000444 | prose | pages [21] -->
Commercial operations that provide day-time charging from renewable sources could also reduce the impact on existing supplies while reducing the carbon emissions from electric vehicles. Businesses could provide free charging while customers shop as a marketing strategy. Battery exchanges at service stations may yield better results for public charging than rapid charging due to the power demands of rapid charging. Low interest loans to cities to provide metered park- ing spaces with alternative power supplies could provide infrastructure. Simply

<!-- b000445 | furniture | pages [22] -->
Team # 11325

<!-- b000446 | furniture | pages [22] -->
Page 16 of 20

<!-- b000447 | prose | pages [22] -->
generating more electricity from the prototypical coal-ﬁred power plant and in- creasing grid capacity will have environmental consequences beyond the savings from reduced ICE emissions. However, estimates by Perujo and Cuiﬀo (2010) indicate the BEV’s superior energy eﬃciency would still oﬀset the production of electricity from high carbon sources. Furthermore, predictions by US Energy Information Agency indicate the proportion of electricity generated by coal will steadily decrease (2010a).

<!-- b000448 | prose | pages [22] -->
This trend would decrease transportation sector- related CO2 emissions by an even greater margin than that provided merely by the switch to electric vehicles.

<!-- b000449 | prose | pages [22] -->
4.4 Health

<!-- b000450 | prose | pages [22] -->
Health impacts are diﬃcult to quantify, but have both social and economic impacts.

<!-- b000451 | prose | pages [22] -->
Healthcare costs have been estimated at $103 per vehicle driven (Guo et al., 2010). These costs were estimated based on tailpipe emissions. BEVs have zero tailpipe emissions but increase emissions from power genera- tion. While electric vehicles represent an overall decrease in CO2 and other harmful pollutants, it is important to note that they also relocate the emissions from congested urban areas to the rural and industrial locations of power plants.

<!-- b000452 | prose | pages [22] -->
4.5 Environment and Pollution

<!-- b000453 | prose | pages [22] -->
Predictions of peak CO2 production range from approximately 1200 to 1400 million metric tonnes per year (Figure 3.6) from transportation. Since BEVs have lower CO2 production the amount produced depends on the number of ICEs replaced by BEVs. This is an improvement and BEVs can be part of a comprehensive energy solution, but must go hand in hand with development of renewable energy sources. Developing BEVs without developing renewable energy sources may slow the rate of climate change, but will not provide a permanent solution.

<!-- b000454 | prose | pages [22] -->
4.6 Oil Consumption

<!-- b000455 | prose | pages [22] -->
Just as the model predicts increasing electricity demand as more BEVs are on the road it predicts declining oil usage from transportation. Figure 3.7 shows the expected oil demand under all scenarios as electric vehicles replace gasoline automobiles. In the model the decline of oil consumption is strongly dependent on the αE and αH. Ideally, all competition variables should be functions of the prices of the vehicles respective fuels.

<!-- b000456 | prose | pages [22] -->
4.7 Economics

<!-- b000457 | prose | pages [22] -->
The results from Table 3.1 divulge useful information on the economic fea- sibility of electric cars. The largest eﬀect is seen from the salvage value for the Nissan Leaf. The actual value of the car and its battery after the 8 year war- ranty are not yet known but the model could be updated as data is collected. An important factor to consider is the The $7500 tax credit for buying the Leaf

<!-- b000458 | furniture | pages [23] -->
Team # 11325

<!-- b000459 | furniture | pages [23] -->
Page 17 of 20

<!-- b000460 | prose | pages [23] -->
which ﬁts with Scenario 1. To overcome this incentive and make the two cars equal in overall cost, the resale value of the Leaf would need to be 26%, or 6% higher than the Civic. However, over the the eight year lifespan of the vehicles, technology is expected to improve and resource costs are going to vary.

<!-- b000461 | prose | pages [23] -->
Scenario 2 considers a rise in electricity costs along with rising oil prices. Since gasoline engines require more fuel per mile, the rising costs of oil have a larger eﬀect on the cost diﬀerential.

<!-- b000462 | prose | pages [23] -->
Even with electricity rates ($/kWh) increasing 10% from the predicted rates, the Leaf still costs $5500 less than the Civic. If the rate increase and the increase in vehicle eﬃciency (kWh/km) are both considered, the cost diﬀerential in Scenario 2 is equal to Scenario 1. However, if the tax credit is removed, only a 33% increase in BEV eﬃciency coupled with a 10% decrease in electricity and a 10% increase in gas prices would make the cost two cars approximately equal.

<!-- b000463 | prose | pages [23] -->
The degree to which technology will improve the eﬃciency of electric vehicles also remains to be seen. Scenario 3 assumes the status quo in BEV technology but incorporates higher oil prices alone. If gasoline were to become $5/gal in eight years and increase linearly, The Leaf would be $8438 cheaper than the Civic, a 47% increase in cost diﬀerential. This is more than enough to overcome the need for a tax credit to make the BEV competitive.

<!-- b000464 | prose | pages [23] -->
The best case, Scenario 4, includes rising gasoline prices with improved technology and initial investments. This increases the car and battery resale value, the BEV eﬃciency, and the cost of gasoline.

<!-- b000465 | prose | pages [23] -->
Keeping the tax credit in place, the consumer would save $10,585 by purchasing a Leaf over a Civic. Without the tax credit, the diﬀerential is still $3,085. Though this situation is optimistic, it is not unreasonable.

<!-- b000466 | prose | pages [23] -->
There are many factors unaccounted for in the economic model but the eﬀect that certain changes will have can be predicted. With very little data to use for BEVs comparison in future costs may not have validity in pure dollar amount but the change in costs and an overall cost comparison indicate realistic behaviors. The interest rate used is also a signiﬁcant factor since a change from 2% to 5% changed the cost diﬀerential by 26%. The true value for the nominal interest rate to use in the model would need to be determined accurately.

<!-- b000467 | prose | pages [23] -->
4.8 Government Support

<!-- b000468 | prose | pages [23] -->
The role of government in supporting new technology has a great impact on the degree of market penetration. Early subsidies that increase the number of vehicles on the road have a large eﬀect on model results. This is due to predictions based on percentage growth rates, and assumes that the number of cars produced in a given year depends on the number already on the road. In a practical sense this should be applicable since familiarity increases con- sumer willingness to purchase the vehicles. A larger number of vehicles on the road also spurs investment in supporting infrastructure as commercial interests recognize a new market. Government support for research and development to speed technology improvements in battery eﬃciency, vehicle range and cost could improve market penetration as well as decrease the electricity demand

<!-- b000469 | furniture | pages [24] -->
Team # 11325

<!-- b000470 | furniture | pages [24] -->
Page 18 of 20

<!-- b000471 | prose | pages [24] -->
per vehicle.

<!-- b000472 | prose | pages [24] -->
5

<!-- b000473 | heading | pages [24] -->
Conclusions

<!-- b000474 | prose | pages [24] -->
The electric car oﬀers many beneﬁts over the internal combustion-powered car.

<!-- b000475 | prose | pages [24] -->
Chief among these factors is its higher energy eﬃciency.

<!-- b000476 | prose | pages [24] -->
To compete with the ICE, however, battery technology improvements and infrastructure investment is needed to boost market growth. The analysis presented here shows the savings in CO2 and oil become greater the faster the electric car is able to dominate the market. The rate at which the BEV are able to overtake ICEs was determined to be a factor of advanced technology, infrastructure investment, and government incentives.

<!-- b000477 | prose | pages [24] -->
Economic analysis of the Nissan Leaf against a conventional Honda Civic indicates subsidies are currently needed to make the Leaf competitive against the Civic. As battery technology and charging infrastructure improve, the BEV is expected to improve its competitiveness against the ICE. In the event gasoline prices hit $5/gal in 2019, the cost of owning and operating a Leaf would be thousands less than a Civic

<!-- b000478 | prose | pages [24] -->
The model suﬀers from considerable uncertainty.

<!-- b000479 | prose | pages [24] -->
Because data for BEV performance and durability over time is not yet available, preliminary simulation may not provide accurate predictions. However, it is believed that the behavior of both the growth and the economic model can represent realistic trends. As data becomes available, the parameters can be calibrated and the model can be veriﬁed. The scenarios considered in these models can also relate changes in economic conditions to to the feasibility of sustaining an electric vehicle market.

<!-- b000480 | prose | pages [24] -->
5.1

<!-- b000481 | heading | pages [24] -->
Recommendations for further study related to this

<!-- b000482 | heading | pages [24] -->
model

<!-- b000483 | prose | pages [24] -->
• Incorporate expected changes in vehicle technology and emissions stan- dards into the growth model parameters

<!-- b000484 | prose | pages [24] -->
• Couple the economic model with the growth model to predict present values of future trends

<!-- b000485 | prose | pages [24] -->
• Calibrate the model using market and performance data as they become available

<!-- b000486 | prose | pages [24] -->
• Introduce stochastic variation to describe more realistic charging periods and energy demand

<!-- b000487 | furniture | pages [25] -->
Page 19 of 20

<!-- b000488 | furniture | pages [25] -->
Team # 11325

<!-- b000489 | prose | pages [25] -->
6

<!-- b000490 | heading | pages [25] -->
Bibliography

<!-- b000491 | references | pages [25] -->
Argonne National Laboratories (2011), GREET1.8c.0 model, Online, http:

<!-- b000492 | references | pages [25] -->
//greet.es.anl.gov/.

<!-- b000493 | references | pages [25] -->
Automotive.com (2011), 2011 honda civic ownership costs, online, http://www.

<!-- b000494 | references | pages [25] -->
automotive.com/2011/12/honda/civic/ownership-costs/index.html.

<!-- b000495 | references | pages [25] -->
Callaway, S. (2011), Diary of an electric commuter, Fortune, 163(1), 31–33.

<!-- b000496 | references | pages [25] -->
Chapra, S., and R. Canale (2002), Numerical Methods for Engineers: With

<!-- b000497 | references | pages [25] -->
Software and Programming Applications, McGraw Hill Companies, Inc.

<!-- b000498 | references | pages [25] -->
Environmental Protection Agency (2011), Calculations and References, online,

<!-- b000499 | references | pages [25] -->
http://www.epa.gov/cleanenergy/energy-resources/refs.html.

<!-- b000500 | references | pages [25] -->
Guo, X., S. Cheng, D. Chen, Y. Zhou, and H. Wang (2010), Estimation of

<!-- b000501 | references | pages [25] -->
economic costs of particulate air pollution from road transport in china, At-

<!-- b000502 | references | pages [25] -->
mospheric Environment, 44, 3369–3377.

<!-- b000503 | references | pages [25] -->
Heintz, J., R. Pollin, and H. Garrett-Peltier (2010), How infrastructure in-

<!-- b000504 | references | pages [25] -->
vestments support the u.s. economy: Employment, productivity and growth,

<!-- b000505 | references | pages [25] -->
Tech. rep., Alliance for American Manufacturing with Political Economy

<!-- b000506 | references | pages [25] -->
Research Institute, http://www.americanmanufacturing.org/wordpress/

<!-- b000507 | references | pages [25] -->
wp-content/uploads/2009/01/peri_aam_finaljan16_new.pdf.

<!-- b000508 | references | pages [25] -->
HowStuﬀWorks.com (2011), 2003 honda civic:

<!-- b000509 | references | pages [25] -->
Overview, online, http://

<!-- b000510 | references | pages [25] -->
consumerguideauto.howstuffworks.com/2003-honda-civic.htm.

<!-- b000511 | references | pages [25] -->
Kelley

<!-- b000512 | references | pages [25] -->
Blue

<!-- b000513 | references | pages [25] -->
Book

<!-- b000514 | references | pages [25] -->
(2011),

<!-- b000515 | references | pages [25] -->
2003

<!-- b000516 | references | pages [25] -->
honda

<!-- b000517 | references | pages [25] -->
civic

<!-- b000518 | references | pages [25] -->
lx

<!-- b000519 | references | pages [25] -->
sedan

<!-- b000520 | references | pages [25] -->
4d,

<!-- b000521 | references | pages [25] -->
online,

<!-- b000522 | references | pages [25] -->
http://www.kbb.com/used-cars/honda/civic/2003/trade-in-value/

<!-- b000523 | references | pages [25] -->
pricing-report?condition=good&id=2501&mileage=100000.

<!-- b000524 | references | pages [25] -->
North American Transportation Statistics Database (2011), Number of Trans-

<!-- b000525 | references | pages [25] -->
online,

<!-- b000526 | references | pages [25] -->
portation Vehicles/Equipment,

<!-- b000527 | references | pages [25] -->
sys/tables.jsp?i=3&id=25.

<!-- b000528 | references | pages [25] -->
http://nats.sct.gob.mx/nats/

<!-- b000529 | references | pages [25] -->
Penn, I. (2011), All-electric nissan leaf appeal grows as gas prices rise, St. Pe-

<!-- b000530 | references | pages [25] -->
tersburgh Times, http://www.tampabay.com/features/consumer/all-electric-

<!-- b000531 | references | pages [25] -->
nissan-leaf-appeal-grows-as-gas-prices-rise/1151082.

<!-- b000532 | references | pages [25] -->
Perujo, A., and B. Cuiﬀo (2010), The introduction of electric vehicles in the

<!-- b000533 | references | pages [25] -->
private ﬂeet: Potential impact on the electric supply system and on the en-

<!-- b000534 | references | pages [25] -->
vironment. A case study for the Province of Milan, Italy, Energy Policy, 38,

<!-- b000535 | references | pages [25] -->
4549–4561.

<!-- b000536 | references | pages [25] -->
The World Bank Group (2011), United States: Data, online, http://data.

<!-- b000537 | references | pages [25] -->
worldbank.org/country/united-states.

<!-- b000538 | references | pages [25] -->
US Energy Information Agency (2009), Existing Capacity by Energy Source,

<!-- b000539 | references | pages [25] -->
Online, http://www.eia.gov/cneaf/electricity/epa/epat1p2.html.

<!-- b000540 | furniture | pages [26] -->
Team # 11325

<!-- b000541 | furniture | pages [26] -->
Page 20 of 20

<!-- b000542 | references | pages [26] -->
US Energy Information Agency (2010a), AEO2011 Early Release Overview,

<!-- b000543 | references | pages [26] -->
online, http://www.eia.gov/forecasts/aeo/pdf/0383er(2011).pdf.

<!-- b000544 | references | pages [26] -->
US Energy Information Agency (2010b), Annual Energy Review, Online, http:

<!-- b000545 | references | pages [26] -->
//www.eia.doe.gov/aer/pecss_diagram.html.

<!-- b000546 | references | pages [26] -->
US Energy Information Agency (2011), Electricity, Data, Analysis, Surveys,

<!-- b000547 | references | pages [26] -->
online, http://www.eia.doe.gov/cneaf/electricity/epa/epa_sum.html.

<!-- b000548 | references | pages [26] -->
Willis, R., and B. Finney (2004), Environmental Systems Engineering and Eco-

<!-- b000549 | references | pages [26] -->
nomics, Kluwer Academic Publishers, Boston.

<!-- b000550 | references | pages [26] -->
Wolfram

<!-- b000551 | references | pages [26] -->
Demonstrations

<!-- b000552 | references | pages [26] -->
Project

<!-- b000553 | references | pages [26] -->
(2010),

<!-- b000554 | references | pages [26] -->
The

<!-- b000555 | references | pages [26] -->
Lotka-

<!-- b000556 | references | pages [26] -->
Volterra

<!-- b000557 | references | pages [26] -->
Equations

<!-- b000558 | references | pages [26] -->
for

<!-- b000559 | references | pages [26] -->
Competition

<!-- b000560 | references | pages [26] -->
between

<!-- b000561 | references | pages [26] -->
Two

<!-- b000562 | references | pages [26] -->
Species,

<!-- b000563 | references | pages [26] -->
online,

<!-- b000564 | references | pages [26] -->
http://demonstrations.wolfram.com/

<!-- b000565 | references | pages [26] -->
TheLotkaVolterraEquationsForCompetitionBetweenTwoSpecies/.

<!-- b000566 | references | pages [26] -->
This document was typeset in LATEX.
