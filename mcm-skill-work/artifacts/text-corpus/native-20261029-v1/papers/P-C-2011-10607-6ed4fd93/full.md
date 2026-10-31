# P-C-2011-10607-6ed4fd93

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
[Team #10607]

<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
[Page 1 of 20]

<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | heading | pages [1] -->
Contents

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | contents | pages [1] -->
1. Introduction ..................................................................................................... 2

<!-- b000008 | contents | pages [1] -->
1.1 The Development of EVs ............................................................................... 2

<!-- b000009 | contents | pages [1] -->
1.2 Tasks and Approaches  .................................................................................. 2

<!-- b000010 | contents | pages [1] -->
2. Basic Assumptions ......................................................................................... 3

<!-- b000011 | contents | pages [1] -->
3. The Economic Comparison Model .................................................... 3

<!-- b000012 | contents | pages [1] -->
3.1 The Life Cycle Cost Model(LCC Model) ....................................................... 3

<!-- b000013 | contents | pages [1] -->
3.1.1 The Preparation Work for Model .................................................................... 3

<!-- b000014 | contents | pages [1] -->
3.1.2 Establishing the LCC Model ........................................................................... 4

<!-- b000015 | contents | pages [1] -->
3.2 Data Collection .............................................................................................. 5

<!-- b000016 | contents | pages [1] -->
3.3 Results of the Calculation .............................................................................. 6

<!-- b000017 | contents | pages [1] -->
3.4 Sensitivity Analysis........................................................................................ 6

<!-- b000018 | contents | pages [1] -->
4. The Environmental Impact Model .................................................... 7

<!-- b000019 | contents | pages [1] -->
4.1 The Primary Pollution:Air Pollution ............................................................... 7

<!-- b000020 | contents | pages [1] -->
4.1.1 Modeling the Emission Dispersion ................................................................ 7

<!-- b000021 | contents | pages [1] -->
4.1.1.1 The Gaussian Plume Model ................................................................ 7

<!-- b000022 | contents | pages [1] -->
4.1.1.2 Simulation of Gaussian Plume Model .............................................. 8

<!-- b000023 | contents | pages [1] -->
4.1.1.3 Results and Discussions of the Simulation ...................................... 9

<!-- b000024 | contents | pages [1] -->
4.1.2 Evalutions of Our Model ................................................................................ 10

<!-- b000025 | contents | pages [1] -->
4.1.2.1 Strengths ................................................................................................ 10

<!-- b000026 | contents | pages [1] -->
4.1.2.2 Weakness ................................................................................ 10

<!-- b000027 | contents | pages [1] -->
4.1.3 The Statistical Prediction of the Amount of Emissions ........................... 10

<!-- b000028 | contents | pages [1] -->
4.1.4 Conclusion ......................................................................................................... 10

<!-- b000029 | contents | pages [1] -->
4.2 Hidden Pollution .......................................................................................... 12

<!-- b000030 | contents | pages [1] -->
4.2.1 Noise Pollution ................................................................................................. 12

<!-- b000031 | contents | pages [1] -->
4.2.2 Used Batteries Pollution ................................................................................. 12

<!-- b000032 | contents | pages [1] -->
5. The health impact of EVs ................................................................ 12

<!-- b000033 | contents | pages [1] -->
6. Prediction of the Future Development of EVs ................................ 12

<!-- b000034 | contents | pages [1] -->
6.1 External-influence Model and Internal-influence Model ............................... 14

<!-- b000035 | contents | pages [1] -->
6.2 Establishing Norton Model for EVs and CVs ............................................... 14

<!-- b000036 | contents | pages [1] -->
6.3 Results and Conclusion ................................................................................ 15

<!-- b000037 | contents | pages [1] -->
6.4 Evalutions of Our Model .............................................................................. 15

<!-- b000038 | contents | pages [1] -->
6.4.1 Strengths ............................................................................................................ 15

<!-- b000039 | contents | pages [1] -->
6.4.2 Weakness ........................................................................................................... 15

<!-- b000040 | contents | pages [1] -->
7. Analysis of Key Factors ................................................................... 15

<!-- b000041 | contents | pages [1] -->
8. Analysis of the Energy Consumption .............................................. 16

<!-- b000042 | contents | pages [1] -->
8.1 The Comparison of the Energy Efficiency  .................................................. 16

<!-- b000043 | contents | pages [1] -->
8.2 Estimate of Saved Fossil Fuels  ................................................................... 17

<!-- b000044 | contents | pages [1] -->
9. Determining the Weight of Different Electricity Generation ......... 18

<!-- b000045 | contents | pages [1] -->
10. References .....................................................................................................20

<!-- b000046 | furniture | pages [1] -->


<!-- b000047 | furniture | pages [2] -->
[Team #10607]

<!-- b000048 | furniture | pages [2] -->


<!-- b000049 | furniture | pages [2] -->
[Page 2 of 20]

<!-- b000050 | heading | pages [2] -->
I. Introduction

<!-- b000051 | prose | pages [2] -->
Due to the concerns over urban environment, high oil costs and the improvements of battery technology, the electric vehicle (EV), which uses electric motors for propulsion, has been propelled to the forefront in recent years. Unlike the vehicle propelled by internal combustion engines (ICEs), the EVs are with the advantage of zero tailpipe emissions and an essentially silent, energy efficient motor. If batteries and cars can be perfectly combined, the EVs will lead a green revolution in realm of vehicle transportation. In order to analyse electric vehicles’ environmentally and economically sound, the following background is worth mentioning.

<!-- b000052 | heading | pages [2] -->
1.1 The Development of EVs

<!-- b000053 | prose | pages [2] -->
Electric vehicles first came into existence in the mid-19th century, when electricity was supposed to the preferred methods for motor vehicle propulsion. Due to low energy density of batteries, it was discontinued. As the new generation of ICEs emerged, it rapidly became the dominant propulsion method for motor vehicles but electric power has remained commonplace in other vehicle types, such as trains and smaller vehicles of all types. [Wikipedia Foundation,2011]

<!-- b000054 | prose | pages [2] -->
In the early 1970s, some countries, compelled by the energy crisis, started the rekindling of interests in EVs. [C.C.Chan,2002] The improvements in battery technology over the past two decades have made it possible to design and manufacture electric vehicles with better performance. Though the number of electric vehicles on the roads is currently in the thousands, that number will soon change. Spurred by the breakthroughs in battery and automotive technology, many vehicle manufacturers have indicated their intention to begin mass producing electric vehicles with Lithium-ion batteries within the next five years. [Thomas A et al.,2009]

<!-- b000055 | heading | pages [2] -->
1.2 Tasks and Approaches

<!-- b000056 | prose | pages [2] -->
The above work has focused on the history and development of EVs. It seems that EVs could be the urban commuters’ panacea were it not for its high purchase price [Karina Funk et al.,1999]. However, the electricity used for EVs is produced by burning fossil fuels in power plants. That brings people to an important question: Is EVs widespread use feasible and practical?

<!-- b000057 | prose | pages [2] -->
So our goal is pretty clear:  Model the environmental, economic, and health impacts of the widespread

<!-- b000058 | prose | pages [2] -->
use of EVs  Detail the key factors that governments and vehicle manufacturers should

<!-- b000059 | prose | pages [2] -->
consider when determining if and how to support the development and use of EVs  Estimate the amount of oil (fossil fuels) the world would save by widely

<!-- b000060 | prose | pages [2] -->
using electric vehicles.  Provide a model of the amount and type of electricity generation that

<!-- b000061 | prose | pages [2] -->
would be needed to support the recommendations regarding the amount and type of electric vehicle use that will produce the largest number of benefits.

<!-- b000062 | furniture | pages [3] -->
[Team #10607]

<!-- b000063 | furniture | pages [3] -->


<!-- b000064 | furniture | pages [3] -->
[Page 3 of 20]

<!-- b000065 | prose | pages [3] -->
Our approach mainly contributes on the following aspects:  In order to deeply analyze economic outlook of EVs, the life cycle cost

<!-- b000066 | prose | pages [3] -->
model (LCC Model) is come up with to compare the market prospect and economic benefits of EVs and t conventional vehicle.

<!-- b000067 | prose | pages [3] -->
 We focus on studying air pollution caused by EVs and CVs. Our purpose

<!-- b000068 | prose | pages [3] -->
is to study the emissions from the space perspective. Gaussian Plume Model is applied here to simulate and predict the emission dispersion.

<!-- b000069 | prose | pages [3] -->
 Establish Norton model for EVs and CVs to make a prediction about the

<!-- b000070 | prose | pages [3] -->
future development of EVs

<!-- b000071 | prose | pages [3] -->
 Do discussion based on our work such as analysis on the key factors

<!-- b000072 | prose | pages [3] -->
influencing the development of EVs, health impact.  Use our models to calculate the amount of saved crude and the amount of

<!-- b000073 | prose | pages [3] -->
extra coal and electricity.  Applying AHP model to determining the weight of different types of

<!-- b000074 | prose | pages [3] -->
electricity generation.

<!-- b000075 | heading | pages [3] -->
II. Basic Assumptions

<!-- b000076 | prose | pages [3] -->
 The related parameters of the EVs and conventional vehicles can reflect

<!-- b000077 | prose | pages [3] -->
their features in the near future.  There will be no new type of vehicles, which has an impact on the

<!-- b000078 | prose | pages [3] -->
development of the conventional vehicles, appearing in the market.  The EVs discussed in the paper refer to pure electric vehicles. We do not

<!-- b000079 | prose | pages [3] -->
consider the hybrid EVs and hydrogen fuel cell vehicles.  The assumptions of Norton model and the Gaussian Plume Model will be

<!-- b000080 | prose | pages [3] -->
mentioned during the process of modeling.  The data we used is accurate and reliable.

<!-- b000081 | furniture | pages [3] -->


<!-- b000082 | heading | pages [3] -->
III. The Economic Comparison Model

<!-- b000083 | heading | pages [3] -->
3.1 The Life Cycle Cost Model (LCC Model)

<!-- b000084 | prose | pages [3] -->
Although the EV is not yet a completely mature technology, the great focus and interest on it still arises from a combination of concerns for urban air quality and high dependence on foreign supplies of oil. In the meantime, the advances in the EV battery and motor technology also have contributed the increasing interest.

<!-- b000085 | heading | pages [3] -->
3.1.1 Preparation Work for Model

<!-- b000086 | prose | pages [3] -->
The EVs can simply divide into pure electric vehicle (PEV), hybrid electric vehicle (HEV) and Fuel cell vehicles (FCV). In the elements, PEV is the technique base of EVs and can be applied to the future field of vehicle transportation. Thus, we take PEV as an example and recommend the life cycle cost model (LCC Model) to compare the market prospect and economic benefits of EVs and t conventional vehicle.

<!-- b000087 | prose | pages [3] -->
Life-cycle cost is known as a pivotal criterion in a comparative evaluation of EVs and conventional vehicle[M. DeLuchi et al.,2009]. From the standpoint of consumers, the life cycle cost include the following 3 aspects: acquisition costs ( C ), maintenance costs ( C ), reclamation income ( iR ).Due to the worsening pi mi environmental pollution, we also take the cost of dealing with environmental

<!-- b000088 | furniture | pages [4] -->
[Team #10607]

<!-- b000089 | furniture | pages [4] -->


<!-- b000090 | furniture | pages [4] -->


<!-- b000091 | furniture | pages [4] -->
[Page 4 of 20]

<!-- b000092 | prose | pages [4] -->
C 、mi C 、iR and C ) into account. The life cycle cost is the sum total of matters ( ei pi

<!-- b000093 | prose | pages [4] -->
i  represents the LCC of traditional automobile, C ,where 1 ei the LCC of EVs.

<!-- b000094 | heading | pages [4] -->
3.1.2 Establishing the LCC Model

<!-- b000095 | prose | pages [4] -->
 Acquisition Costs

<!-- b000096 | prose | pages [4] -->
stands for i  2

<!-- b000097 | prose | pages [4] -->
In this section, the cost of purchase is composed of the expenses of purchase and the related poundage. So acquisition cost can be expressed as following:

<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | prose | pages [4] -->
C  pi

<!-- b000100 | prose | pages [4] -->
Where, p is the expense of purchase, vi as tax, license fee.

<!-- b000101 | prose | pages [4] -->
 Maintenance Costs

<!-- b000102 | prose | pages [4] -->
(1) p p h  vi i

<!-- b000103 | prose | pages [4] -->
ih represents the related poundage, such

<!-- b000104 | prose | pages [4] -->
The vehicle is known as a kind of durable goods and its cost of maintenance occupies 50% even more in the Life Cycle Cost Model. Conventional vehicles’ maintenance cost depends on the expenditure of repairing and vehicles refueling. We suppose the cost of repairing and refueling are

<!-- b000105 | prose | pages [4] -->
C

<!-- b000106 | furniture | pages [4] -->


<!-- b000107 | prose | pages [4] -->
 m 1

<!-- b000108 | prose | pages [4] -->
m and 1o ,then we obtain : 1

<!-- b000109 | prose | pages [4] -->
(2) m m o  1 1 1 1L is total kilometers, Where, , o L k p    g 1 1 1 1k means fuel consumption per

<!-- b000110 | prose | pages [4] -->
p represents fuel cost per liter ($ / L ). 100 km, g

<!-- b000111 | prose | pages [4] -->
As for EVs, electric charge replaces the role of fuel. Since the maintenance of the battery account for a large part of Maintenance costs, we consider the battery maintenance costs as an independent factor b ,the total sum of maintenance costs can be described as below:

<!-- b000112 | prose | pages [4] -->
C m

<!-- b000113 | furniture | pages [4] -->


<!-- b000114 | prose | pages [4] -->
 m 2 (3) o b   2 2 2 m is components maintenance costs of EVs and has the same method of Where, 2 2o means the battery charging fees and can be denote as calculation as m . 1 o L

<!-- b000115 | furniture | pages [4] -->


<!-- b000116 | prose | pages [4] -->
  2 2 (4) p p k  2 /  e e ep means the cost of electricity per kw h Where, L is total kilometers, 2 , 2k is electricity consumption per 100 km,  is charging efficiency.

<!-- b000117 | prose | pages [4] -->
The performance of battery will be poorer with time going by. As a result, the corresponding maintenance costs will increase. In order to describe the above bl denoting the total mileage of EVs during the life cycle of a process, we define battery. Suppose the purchase price of battery as bp . c is the charge for trouble when changing battery .Then the battery maintenance costs can be calculated as

<!-- b000118 | prose | pages [4] -->
L b 

<!-- b000119 | furniture | pages [4] -->


<!-- b000120 | prose | pages [4] -->
l

<!-- b000121 | prose | pages [4] -->
 Reclamation Income

<!-- b000122 | prose | pages [4] -->
2 ( 2 (

<!-- b000123 | prose | pages [4] -->
(5) p c 

<!-- b000124 | prose | pages [4] -->
) b b b

<!-- b000125 | prose | pages [4] -->
Reclamation income consists of the money raised by selling assets and the subsidy policy for the reject and renovation of the old and used cars, something like the government-sponsored scrappage projects. Different types of cars have different reclamation income which can be found on the internet. We consume the reclamation income of EVs and conventional vehicles to be

<!-- b000126 | prose | pages [4] -->
 Environmental Costs

<!-- b000127 | prose | pages [4] -->
R and R . 1 2

<!-- b000128 | furniture | pages [5] -->
[Team #10607]

<!-- b000129 | furniture | pages [5] -->


<!-- b000130 | furniture | pages [5] -->


<!-- b000131 | furniture | pages [5] -->
[Page 5 of 20]

<!-- b000132 | prose | pages [5] -->
Conventional vehicles release at the place where they are operated, the emissions of hydrocarbons (HC) and nitrogen oxides (NOx) exceed 2000 tons per day. These pollutants react in the presence of sunshine to form ozone concentrations that are roughly three times larger than the federal health standard.[South Coast Air Quality Management District,1989]Therefore, to timely collect environmental taxation is imperative.

<!-- b000133 | prose | pages [5] -->
Now there is no standard way to calculate environmental costs. Like some Europe nation collecting environmental pollution tax, we use the same method to 1r is the taxation of fuel per liter. obtain the environmental costs. Thus, suppose Then Environmental costs of conventional vehicles can be denoted as:

<!-- b000134 | prose | pages [5] -->
C

<!-- b000135 | furniture | pages [5] -->


<!-- b000136 | prose | pages [5] -->
 e 1 (6) r r L k   1 1 1 1 While EVs have reduced tailpipe carbon emissions, the energy they consume is produced by means that have environmental impacts. In addition, the manufacturing and depletion processing of batteries also have an impact to environment which also. The government needs comprehensive effort to curb the pollution which may cause a large amount of fiscal charges.

<!-- b000137 | prose | pages [5] -->
As for EVs, government should collecting environmental pollution tax for the battery recycle .The tax cost is stated as following:

<!-- b000138 | prose | pages [5] -->
C 

<!-- b000139 | furniture | pages [5] -->


<!-- b000140 | prose | pages [5] -->
e 2

<!-- b000141 | prose | pages [5] -->
L

<!-- b000142 | prose | pages [5] -->
2

<!-- b000143 | prose | pages [5] -->
r r  (7)

<!-- b000144 | prose | pages [5] -->
2 2

<!-- b000145 | prose | pages [5] -->
l

<!-- b000146 | prose | pages [5] -->
b

<!-- b000147 | prose | pages [5] -->
2r is the taxation of battery pack. According to discussion above, we Where obtain the full life cycle cost:

<!-- b000148 | furniture | pages [5] -->


<!-- b000149 | prose | pages [5] -->
LCC C  i pi

<!-- b000150 | heading | pages [5] -->
3.2 Data Collection

<!-- b000151 | prose | pages [5] -->
(8) C R C     mi i ei

<!-- b000152 | prose | pages [5] -->
After accessing relevant information, we take the RAV4 EV and RAV4 manufactured by Toyota as an example to compare the LCC of EVs and conventional vehicles. As we know the RAV4 EV is an all-electric version of the popular RAV4 [Wikipedia Foundation,2011]. The relevant parameters are listed in

<!-- b000153 | caption | pages [5] -->
Table 1.

<!-- b000154 | prose | pages [5] -->
Relevant Parameters

<!-- b000155 | prose | pages [5] -->
p （$） Purchase Expense vi ih ($) Related Poundage 2k Electricity Consumption per 100 km (kw.h)

<!-- b000156 | prose | pages [5] -->
1k Oil Consumption per 100 km (L) Total Mileage of vehicle  (km) Maintenance Costs per year  ($) bp Price of Battery ($) Total Mileage of battery (km)

<!-- b000157 | prose | pages [5] -->
RAV 4EV RAV4

<!-- b000158 | prose | pages [5] -->
60673 30336 6067 3033 0 20

<!-- b000159 | prose | pages [5] -->
0 8.5 500000 500000 455 1516 3033 0 40000 0

<!-- b000160 | caption | pages [5] -->
Table 1.  The relevant parameters of RAV4 EV and RAV.

<!-- b000161 | prose | pages [5] -->
(Data come from the reference [Yang Feng et al.,2009])

<!-- b000162 | prose | pages [5] -->
As is revealed in the table, the related poundage is calculated by no more than 10% of the expenses of purchase. According to the of a latest believable reference, the expected life cycle of RAV4 EV and RAV4 is 10 years and the total mileage is set as 500000 km. As electric vehicles don't have clutch, gearbox and the other

<!-- b000163 | furniture | pages [6] -->
[Team #10607]

<!-- b000164 | furniture | pages [6] -->


<!-- b000165 | furniture | pages [6] -->


<!-- b000166 | furniture | pages [6] -->
[Page 6 of 20]

<!-- b000167 | prose | pages [6] -->
mechanical transmission equipment, maintenance costs of EVs is 70% less than Conventional vehicles. And the publicly recognized value of the battery charging efficiency is 85%. Users can obtain $3033 as reclamation income. Then due to the imperfect running of the current policy, users don’t need to undertake environmental costs. Thus, we don’t take environmental costs into calculation.

<!-- b000168 | heading | pages [6] -->
3.3 Results of the Calculation

<!-- b000169 | prose | pages [6] -->
So after many times calculation under the conditions discussed above, we obtain statistic results as follow:

<!-- b000170 | prose | pages [6] -->
C m p ih

<!-- b000171 | furniture | pages [6] -->


<!-- b000172 | prose | pages [6] -->
pi vi

<!-- b000173 | prose | pages [6] -->
RAV4 EV 60673 6067 66740 455 RAV4 30336 3033 33370 1516

<!-- b000174 | prose | pages [6] -->
o C

<!-- b000175 | furniture | pages [6] -->


<!-- b000176 | prose | pages [6] -->
b R LCC mi

<!-- b000177 | prose | pages [6] -->
8922 37920 51393 3033 115100 422224 0 57393 3033 87728

<!-- b000178 | caption | pages [6] -->
Table 2.  The calculated results of relevant parameters and LCC($)

<!-- b000179 | prose | pages [6] -->
It can be seen from the statistics that the LCC of EVs is higher than the conventional vehicles while the cost on energy consumption is only 21.3% of conventional vehicles. And its failure rate as well as maintenance costs are lower than conventional vehicles. In the condition of reasonable acquisition cost and acceptable price of battery packs, the economic advantage of EVs is obvious.

<!-- b000180 | heading | pages [6] -->
3.4 Sensitivity Analysis

<!-- b000181 | prose | pages [6] -->
Then, in order to identify the most sensitive factor of impacting market prospect and economic benefits, we do sensitivity analysis about the above data. When the parameters are changed within 5%, we observe how much LCC change. The purpose is to analyze the sensitivity of iR and C , C . C , mi ei pi Before calculation, we choose the oil and electricity price, battery packs price, acquisition cost, mileage as the related parameters, because they may change over time and then produce a great fluctuation in price. We change the parameters within 5%, and then obtain the changing rate of LCC.

<!-- b000182 | prose | pages [6] -->
Oil/Electricity Price Acquisition cost RAV4 EV Battery PacksPrice Mileage 0.38% 2.89% RAV4 1.64% -1.56% 2.40% 1.90% - -

<!-- b000183 | caption | pages [6] -->
Table 3.  The Sensitivity Analysis between relevant parameters and LCC

<!-- b000184 | prose | pages [6] -->
As can be revealed in Table 3, the order of parameters sensitivity is proved to be: acquisition cost > battery packs price > mileage > electricity price. As for CVs, the results indicate as following: the oil price > acquisition cost.

<!-- b000185 | prose | pages [6] -->
Based on the discussion above, the LCC of the CVs is less sensitive to the acquisition cost, as compared with the LCC of EVs. The LCC of CVs is more sensitive to oil and electricity price than the LCC of EVs. We can see that the LCC can, to some extent, be influenced by the price of battery packs and mileage. However, come to analyses from the long-term eyes, it is the inexorable trend to cut down the acquisition cost of EVs as well as the battery packs price. While with the large-scale exploitation of oil and mine, oil price will reveal a trend of increasing. According to the sensitivity analysis, the LCC of the conventional vehicles will increase gradually with the increasing of oil price. We can draw a conclusion that EVs has a lot of scope for improvement, which means that EVs are

<!-- b000186 | furniture | pages [7] -->
[Team #10607]

<!-- b000187 | furniture | pages [7] -->


<!-- b000188 | furniture | pages [7] -->
[Page 7 of 20]

<!-- b000189 | prose | pages [7] -->
more economical in the future.

<!-- b000190 | prose | pages [7] -->
The economic impact of EVs is obvious. First of all, the development of EVs can lower the cost of maintenance and with some technical improvements, the acquisition cost will also be much lower, which make more people afford a car. Besides, the large scale use of EVs also will create lots of new jobs and promote the development of economy.

<!-- b000191 | heading | pages [7] -->
IV. The Environmental Impact Model

<!-- b000192 | prose | pages [7] -->
There are two major types of pollution caused by vehicles. One is the primary pollution. The biggest part of primary pollution is the air pollution which is also the center of this section. And the other is the hidden pollution. It also plays a significant role in the impact on the environment.

<!-- b000193 | prose | pages [7] -->
We have already known the conventional vehicle is a tremendous threat to the environment. But after the comparison of electric vehicles (EVs) and conventional vehicles (CVs) presented by following sections, we can find out the environmental impact of large scale use of electric vehicles.

<!-- b000194 | heading | pages [7] -->
4.1 The primary pollution: Air pollution

<!-- b000195 | prose | pages [7] -->
Electric cars produce no pollution at the tailpipe which will contribute to cleaner air in cities, but their use increases demand for electricity generation. The amount of carbon dioxide emitted depends on the emission intensity of the power source used to charge the vehicle, the efficiency of the said vehicle and the energy wasted in the charging process [Wikipedia Foundation,2011] And meantime the power station will discharge extra emissions. So in fact EVs is not a vehicle with no emissions.

<!-- b000196 | prose | pages [7] -->
The pollutants produced by conventional vehicles mainly account for nitrites of oxygen, vehicle-born monoxide, hydrocarbon and carbon dioxide pollution. To simplify, environmental impact is considered by examining air pollution (AP) and greenhouse gas (GHG). [Mikhail Granovskii et al., 2006 ] The main gases in GHG emissions are CO and CH while the AP emissions includeCO , SO , NO x 2 4 and HC .

<!-- b000197 | prose | pages [7] -->
In order to better study the air pollution caused by EVs and CVs, we focus on the emissions dispersion and the amount of emissions.

<!-- b000198 | heading | pages [7] -->
4.1.1 Modeling the Emission Dispersion

<!-- b000199 | heading | pages [7] -->
4.1.1.1 The Gaussian Plume Model

<!-- b000200 | prose | pages [7] -->
Our purpose is to study the emissions from the space perspective. As the most classic model for emission dispersion, Gaussian Plume Model is applied here to simulate and predict the emission dispersion.

<!-- b000201 | prose | pages [7] -->
Before we establish the Gaussian Plume Model, we need to come up with these following assumptions.

<!-- b000202 | prose | pages [7] -->
 The electric vehicle is regarded as a still point source at ground-level.  The direction of wind is parallel to X axis. So the pollutants are

<!-- b000203 | prose | pages [7] -->
continuously discharged to one certain direction.  The speed of wind is uniform and invariable.  The mass of emissions is always conserved in the dispersion process.

<!-- b000204 | furniture | pages [8] -->
[Team #10607]

<!-- b000205 | furniture | pages [8] -->


<!-- b000206 | furniture | pages [8] -->


<!-- b000207 | furniture | pages [8] -->
[Page 8 of 20]

<!-- b000208 | prose | pages [8] -->
 The concentration of the pollution source is normally distributed in the y

<!-- b000209 | prose | pages [8] -->
and z dimensions  The ground can’t absorb pollutants.

<!-- b000210 | furniture | pages [8] -->


<!-- b000211 | caption | pages [8] -->
Figure 1. The coordinate plot of the point source and its polluted area

<!-- b000212 | prose | pages [8] -->
According to the assumptions, the source of emissions can be regarded as a point source. To start with, we use Cartesian Coordinate System to analyze the point source. For the point source on the ground, the Gaussian dispersion formula is shown as Eq.9.

<!-- b000213 | prose | pages [8] -->
q C x y z

<!-- b000214 | furniture | pages [8] -->


<!-- b000215 | prose | pages [8] -->
( , , )

<!-- b000216 | prose | pages [8] -->


<!-- b000217 | prose | pages [8] -->
u

<!-- b000218 | prose | pages [8] -->


<!-- b000219 | prose | pages [8] -->
2 2

<!-- b000220 | prose | pages [8] -->
y z

<!-- b000221 | prose | pages [8] -->


<!-- b000222 | prose | pages [8] -->
0.5(

<!-- b000223 | prose | pages [8] -->


<!-- b000224 | prose | pages [8] -->
) 2 2

<!-- b000225 | prose | pages [8] -->
 

<!-- b000226 | prose | pages [8] -->
e

<!-- b000227 | prose | pages [8] -->
(9)

<!-- b000228 | prose | pages [8] -->
y x

<!-- b000229 | furniture | pages [8] -->


<!-- b000230 | prose | pages [8] -->
y y z

<!-- b000231 | prose | pages [8] -->
C x y z stands for the concentration of the emission (in micrograms Where, ( , , ) per cubic meter) at any point in the polluted area. q is denoted as the quantity or mass of the emission (in grams) per unit of time (seconds) and u is the wind speed (in meters per second).

<!-- b000232 | prose | pages [8] -->
 and y  stand for the standard deviations of a x x statistically normal plume in the y and z dimensions, respectively.

<!-- b000233 | prose | pages [8] -->
According to the assumptions, we can obtain

<!-- b000234 | prose | pages [8] -->
  q

<!-- b000235 | prose | pages [8] -->
 (10)

<!-- b000236 | prose | pages [8] -->
uCdydz

<!-- b000237 | prose | pages [8] -->
 

<!-- b000238 | prose | pages [8] -->
After putting specific number into all the coefficients, we can get the concentration of the emission at the stable state. Using this model, we can also figure out how far the pollutants may affect.

<!-- b000239 | heading | pages [8] -->
4.1.1.2 Simulation of Gaussian Plume Model

<!-- b000240 | prose | pages [8] -->
Now we use Matlab to simulate the emission dispersion of conventional  be 1.5 and u be 2. According to relevant reference, vehicles. Let  be 1.5, x y we obtain Table 4.

<!-- b000241 | prose | pages [8] -->
CVs Type of vehicle (gasoline)

<!-- b000242 | prose | pages [8] -->
Mass of vehicle 1000 Kg HC 0.018 CO 0.91 NO2 0.0771 CO2 83 SOx 0.0045-0.4356

<!-- b000243 | prose | pages [8] -->
EVs

<!-- b000244 | prose | pages [8] -->
EVs

<!-- b000245 | prose | pages [8] -->
(thermal power)

<!-- b000246 | prose | pages [8] -->
(Natural gas ) 1200 Kg 1200 Kg 0.0008 0.0022 0.0091 0.0182 0.2948 0.1814 91 41 0.1814-0.7711 0.0003

<!-- b000247 | caption | pages [8] -->
Table 4. the comparison of emissions from different types of vehicles (kg/per car)

<!-- b000248 | prose | pages [8] -->
(Source: The Electric Vehicle Technical Report from General Motors)

<!-- b000249 | furniture | pages [9] -->
[Team #10607]

<!-- b000250 | furniture | pages [9] -->


<!-- b000251 | furniture | pages [9] -->
[Page 9 of 20]

<!-- b000252 | prose | pages [9] -->
As mentioned above, the electric vehicle is a vehicle with no emissions. But the emissions shown in Table 4 are produced by the power stations which provide extra electricity for the electric vehicles. Here we just regard the emissions produced by power stations as the direct emissions produced by EVs (But EV itself is a no-emission vehicle).

<!-- b000253 | prose | pages [9] -->
EV (thermal power) means the electricity of electric vehicles are supplied by thermal power and EV (Natural gas) means the electricity of electric vehicles are supplied by natural gas.

<!-- b000254 | prose | pages [9] -->
We can see from Table 4, we divide all the emissions into two types: air pollution (AP) and greenhouse gas (GHG). So we calculate the amount of AP and GHG as well as normalize the AP value and GHG value of all types of vehicles. The normalized weighting coefficients of CVs, EVs (thermal power) and EVs(Natural gas) are 6.11, 3.86 and 1 respectively. The weighting coefficients are used to determine the amount of AP (the number of circles) in the simulation. And now we start the simulation of emission dispersion.

<!-- b000255 | heading | pages [9] -->
4.1.1.3 Results and Discussions of the Simulation

<!-- b000256 | furniture | pages [9] -->


<!-- b000257 | caption | pages [9] -->
Figure 2. AP dispersion of CVs (gasoline)

<!-- b000258 | caption | pages [9] -->
Figure 2 shows that the emissions of CVs spread farthest and affect the largest

<!-- b000259 | prose | pages [9] -->
area in all types of vehicles in the comparison. And its total amount of AP (represented by the number of circles) is also the maximum value. Of all the compared vehicles, CVs is the culprit that should be blamed for worsening air quality.

<!-- b000260 | furniture | pages [9] -->


<!-- b000261 | caption | pages [9] -->
Figure 3. AP dispersion of EVs (thermal power)

<!-- b000262 | caption | pages [9] -->
Figure 3 shows that the emissions of EVs (thermal power) rank the second in

<!-- b000263 | prose | pages [9] -->
the affected area and the amount of AP. So if EVs are powered by a thermal power station, the pollution to the environment is still big but not bigger than CVs(gasoline).

<!-- b000264 | furniture | pages [10] -->
[Team #10607]

<!-- b000265 | furniture | pages [10] -->


<!-- b000266 | furniture | pages [10] -->


<!-- b000267 | furniture | pages [10] -->
[Page 10 of 20]

<!-- b000268 | furniture | pages [10] -->


<!-- b000269 | caption | pages [10] -->
Figure 4. AP dispersion of EVs (natural gas)

<!-- b000270 | caption | pages [10] -->
Figure 4 shows that EVs(natural gas) is the greenest vehicles in the compared

<!-- b000271 | prose | pages [10] -->
types. From this point, if the electricity is generated by a clean and efficient energy such as solar energy and wind energy, the EVs will be much more environmentally friendly.

<!-- b000272 | prose | pages [10] -->
Besides, we can also use the same method to analyze the dispersion of GHG. Because the dispersion is similar, we will not go to details.

<!-- b000273 | heading | pages [10] -->
4.1.2 Evaluation of the model

<!-- b000274 | heading | pages [10] -->
4.1.2.1 Strengths

<!-- b000275 | prose | pages [10] -->
 Gaussian plume model can precisely describe the dispersion of emissions. It

<!-- b000276 | prose | pages [10] -->
builds up an equation to calculate the concentration of every point in the polluted area.  Gaussian plume has a strong flexibility. It can be applied to all kinds of gases

<!-- b000277 | prose | pages [10] -->
and point sources.

<!-- b000278 | heading | pages [10] -->
4.1.2.2 Weaknesses

<!-- b000279 | prose | pages [10] -->
 Gaussian plume model considers the dispersion of emissions too ideally and it

<!-- b000280 | prose | pages [10] -->
can’t consider the influence of other factors.  Gaussian plume model can only be used to describe the point source. If we

<!-- b000281 | prose | pages [10] -->
consider a moving vehicle, the model has to be improved.

<!-- b000282 | heading | pages [10] -->
4.1.3 The Statistical Prediction of the Amount of Emissions

<!-- b000283 | prose | pages [10] -->
According to relevant references, we get the emission data as shown in

<!-- b000284 | caption | pages [10] -->
Table 5.

<!-- b000285 | prose | pages [10] -->
Type of vehicle Air pollution(AP)

<!-- b000286 | prose | pages [10] -->
emissions

<!-- b000287 | prose | pages [10] -->
Greenhouse gas(GHG)

<!-- b000288 | prose | pages [10] -->
emissions

<!-- b000289 | prose | pages [10] -->
CVs EVs

<!-- b000290 | prose | pages [10] -->
20.64 5.023

<!-- b000291 | prose | pages [10] -->
320 130

<!-- b000292 | caption | pages [10] -->
Table 5. the average emissions of CVs and EVs (g/per km, per car)

<!-- b000293 | prose | pages [10] -->
(Source: The Electric Vehicle Technical Report from General Motors)

<!-- b000294 | prose | pages [10] -->
We establish three scenarios (Table 6) in order to analyze the impact of large scale use of EVs on the amount of emissions.

<!-- b000295 | prose | pages [10] -->
Proportion of CVs

<!-- b000296 | furniture | pages [10] -->


<!-- b000297 | prose | pages [10] -->
Scenario 1 80% Scenario 2 50% Scenario 3 20% Proportion of EVs 20% 50% 80%

<!-- b000298 | caption | pages [10] -->
Table 6. Three scenarios of different proportion of CVs and EVs

<!-- b000299 | furniture | pages [11] -->
[Team #10607]

<!-- b000300 | furniture | pages [11] -->


<!-- b000301 | furniture | pages [11] -->


<!-- b000302 | furniture | pages [11] -->
[Page 11 of 20]

<!-- b000303 | prose | pages [11] -->
Eq.11 and Eq.12 are established here to calculate the total amount of air i and Greenhouse gas emissions S ( ) pollution emissions AP S i CV p n ( )   AP AP S i CV ( )  GHG GHG

<!-- b000304 | prose | pages [11] -->
CV CV

<!-- b000305 | prose | pages [11] -->
S i . ( ) GHG EV q n   (11) i i AP i p n EV q n     (12) i GHG i

<!-- b000306 | prose | pages [11] -->
are AP emissions of a CV and GHG emissions of Where, and AP GHG EV a CV respectively. Similarly, and AP EV are AP emissions of a EV and GHG ip is the proportion of CVs in scenario i GHG emissions of a EV respectively.

<!-- b000307 | prose | pages [11] -->
iq is the proportion of EVs in scenario i . n stands for the number of while vehicles in the world.

<!-- b000308 | prose | pages [11] -->
Year 2004 2005 the amount of

<!-- b000309 | prose | pages [11] -->
851 896 vehicles

<!-- b000310 | prose | pages [11] -->
2006 2007 2008 2009

<!-- b000311 | prose | pages [11] -->
943 993 1047 1100

<!-- b000312 | caption | pages [11] -->
Table 7. The total number of vehicles in the world (million)

<!-- b000313 | prose | pages [11] -->
Source: U.S Census Bureau

<!-- b000314 | furniture | pages [11] -->


<!-- b000315 | prose | pages [11] -->
According to Table 7, we roughly estimate the number of vehicles around the world is 1.15 billion. Using Eq.11 and Eq.12 we can calculate the amount of AP emissions and GHG emissions in all the scenarios (Figure 5. and Figure 6.)

<!-- b000316 | furniture | pages [11] -->


<!-- b000317 | caption | pages [11] -->
Figure 5. The amount of AP emissions in three scenarios

<!-- b000318 | furniture | pages [11] -->


<!-- b000319 | caption | pages [11] -->
Figure 6. The amount of GHG emissions in three scenarios

<!-- b000320 | prose | pages [11] -->
The statistical prediction describes the amount of AP and GHG emissions when electric vehicles are used in a small scale and a large scale.

<!-- b000321 | heading | pages [11] -->
4.1.4 Conclusion

<!-- b000322 | prose | pages [11] -->
Generally speaking, large scale use of EVs can greatly improve the environment especially the air quality.

<!-- b000323 | prose | pages [11] -->
To be specific, large scale use of EVs can improve the air quality near the

<!-- b000324 | furniture | pages [12] -->
[Team #10607]

<!-- b000325 | furniture | pages [12] -->


<!-- b000326 | furniture | pages [12] -->


<!-- b000327 | furniture | pages [12] -->
[Page 12 of 20]

<!-- b000328 | prose | pages [12] -->
road and narrow down the polluted area. And the spread of the emissions will be slowed down as well. The amount of emissions will also significantly go down, which may control the air pollution.

<!-- b000329 | heading | pages [12] -->
4.2 Hidden Pollution

<!-- b000330 | heading | pages [12] -->
4.2.1 Noise Pollution

<!-- b000331 | prose | pages [12] -->
The noise pollution caused by the conventional vehicles may be ridiculous to some people. But if you live by the main road, you will know it suffers a lot.

<!-- b000332 | prose | pages [12] -->
We find out some data about the comparison of noise pollution caused by CVs and EVs. (Table 8)

<!-- b000333 | prose | pages [12] -->
Noise Speed CVs EVs Inside

<!-- b000334 | prose | pages [12] -->
35 km/h Uniform Velocity 50 km/h

<!-- b000335 | prose | pages [12] -->
35 km/h Acceleration 50 km/h

<!-- b000336 | prose | pages [12] -->
Outside Inside Outside

<!-- b000337 | prose | pages [12] -->
73 67 67 66 70 69 70 66

<!-- b000338 | prose | pages [12] -->
81 75 72 66 76 72 71 66

<!-- b000339 | caption | pages [12] -->
Table 8. The noise of CVs and EVs in different speed and state (dB)

<!-- b000340 | prose | pages [12] -->
From Table 8, we can large scale use of EVs is an efficient way to reduce noise. So if the EVs had been used widely, it would improve the living conditions near the road. People who live near road may have a sweet sleep.

<!-- b000341 | furniture | pages [12] -->


<!-- b000342 | heading | pages [12] -->
4.2.2 Used Batteries Pollution

<!-- b000343 | prose | pages [12] -->
The widespread use of batteries has already created many environmental concerns, such as toxic metal pollution which is the most serious problem. If the large scale use of EVs becomes reality, the used batteries pollution will be much more serious than nowadays.

<!-- b000344 | prose | pages [12] -->
There exist so many toxic metals in the battery such as mercury, cadmium, manganese, nickel and lead. Take mercury as an example. Mercury is the main cause of Japanese Minamata disease. If mercury is ingested by mistake, it may trigger unimaginable consequence.

<!-- b000345 | furniture | pages [12] -->


<!-- b000346 | heading | pages [12] -->
V. The Health Impact of EVs

<!-- b000347 | prose | pages [12] -->
On one hand, the environmental impact is closely related to the health impact. For example, the air pollution of CVs will greatly affect people’s respiratory health. So large scale use of EVs can help to control air pollution, which is good news for us humans. But the battery pollution may contaminate the food and water people eat, poisoning some people. On the other hand, the Harmonic from charging station may do harm to humans’ heart and brain.

<!-- b000348 | furniture | pages [12] -->


<!-- b000349 | heading | pages [12] -->
VI. Prediction of the Future Development of EVs

<!-- b000350 | prose | pages [12] -->
Having analyzed the environmental, economic and health impact of widespread use of EVs, we find out that EVs have the potential to take place of CVs. The technical difficulties are basically solved nowadays. With some technical improvements and the government’s Omni-directional support, EVs can become the main current vehicles. So generally speaking, we are optimistic about

<!-- b000351 | furniture | pages [13] -->
[Team #10607]

<!-- b000352 | furniture | pages [13] -->


<!-- b000353 | furniture | pages [13] -->


<!-- b000354 | furniture | pages [13] -->
[Page 13 of 20]

<!-- b000355 | prose | pages [13] -->
the future of EVs. Based on this point of view, we use a diffusion theory model of substitution (Norton Model) to simulate the process of substitution. Through Norton Model, we can see how the number of EVs changes.

<!-- b000356 | prose | pages [13] -->
The purpose of this section is to demonstrate the feasibility of EVs and predict the future development of EVs.

<!-- b000357 | furniture | pages [13] -->


<!-- b000358 | heading | pages [13] -->
6.1 External-influence Model and Internal-influence Model

<!-- b000359 | prose | pages [13] -->
Before establishing the Norton Model, we introduce the External-influence Model and Internal-influence Model. The external-influence model is made up with an ordinary differential equation (Eq.13) and used to describe the diffusion of technical innovation in the potential market.

<!-- b000360 | prose | pages [13] -->
dN t ( )

<!-- b000361 | furniture | pages [13] -->


<!-- b000362 | prose | pages [13] -->
n t ( )   dt   (13) p M N t  ( )

<!-- b000363 | prose | pages [13] -->
N t is the accumulated number of people who have used the Where, ( ) innovation by time t . M is the upper limit of the number of potential users. p n t is the number of people who use the innovation is the innovation coefficient.

<!-- b000364 | prose | pages [13] -->
( ) at time t , namely the probability of using the innovation at time t . From Eq.13, N t is an exponential function. The model attributes the we can know the plot of ( ) innovation diffusion to the people who haven’t used the innovation. So this is why the model is called external-influence model.

<!-- b000365 | prose | pages [13] -->
Similarly, the internal-influence model is also described by an ordinary differential equation (Eq.14). It is also used to simulate the diffusion of technical innovation.

<!-- b000366 | prose | pages [13] -->
dN t ( )

<!-- b000367 | furniture | pages [13] -->


<!-- b000368 | prose | pages [13] -->
n t ( )   dt M q q   (14) N t M N t ( ) - ( )

<!-- b000369 | prose | pages [13] -->
n t are the same as the external-influence The meaning of N t , M and ( ) ( ) model. q is the imitation coefficient. The internal-influence model assumes the diffusion speed is in proportion to the number of innovation users and the number of non users. That means the innovation diffusion is only driven by the number of N t is a logistic curve. innovation users. The plot of ( )

<!-- b000370 | prose | pages [13] -->
Both External-influence model and Internal-influence model can’t describe the innovation diffusion well. So we need to combine two models to one in order to precisely simulate the innovation diffusion.

<!-- b000371 | prose | pages [13] -->
dN t ( )  n t p M N t ( )   - ( ) dt

<!-- b000372 | prose | pages [13] -->
Where, the meaning of N t , M , ( ) models mentioned above.

<!-- b000373 | prose | pages [13] -->
  p M N t  ( )

<!-- b000374 | prose | pages [13] -->
q N t

<!-- b000375 | prose | pages [13] -->
q     (15) N t M N t  ( ) - ( ) M

<!-- b000376 | prose | pages [13] -->
n t , q and p are the same as the ( ) represents the external influence while

<!-- b000377 | prose | pages [13] -->
stands for the internal influence.   M N t ( )  ( ) M

<!-- b000378 | prose | pages [13] -->
We solve the ordinary differential equation and obtain

<!-- b000379 | prose | pages [13] -->
N t M

<!-- b000380 | prose | pages [13] -->
( )

<!-- b000381 | prose | pages [13] -->


<!-- b000382 | prose | pages [13] -->
1

<!-- b000383 | prose | pages [13] -->
Where, m  0 q , 0   1 , 0 p 

<!-- b000384 | prose | pages [13] -->
p q t

<!-- b000385 | prose | pages [13] -->
-(

<!-- b000386 | prose | pages [13] -->


<!-- b000387 | prose | pages [13] -->
)

<!-- b000388 | prose | pages [13] -->
e

<!-- b000389 | prose | pages [13] -->
1- 1-

<!-- b000390 | prose | pages [13] -->
(16)

<!-- b000391 | prose | pages [13] -->
q e p q t

<!-- b000392 | prose | pages [13] -->
-(

<!-- b000393 | prose | pages [13] -->


<!-- b000394 | prose | pages [13] -->
)

<!-- b000395 | prose | pages [13] -->
 

<!-- b000396 | prose | pages [13] -->
p

<!-- b000397 | prose | pages [13] -->
. The inflection point of is N t   1 ( )

<!-- b000398 | furniture | pages [14] -->
[Team #10607]

<!-- b000399 | prose | pages [14] -->
2  

<!-- b000400 | furniture | pages [14] -->


<!-- b000401 | furniture | pages [14] -->


<!-- b000402 | furniture | pages [14] -->
[Page 14 of 20]

<!-- b000403 | prose | pages [14] -->
and the curve is symmetrical about the inflection point.

<!-- b000404 | prose | pages [14] -->
q m p q 1 (  ) In ( ),   p q p q  4  

<!-- b000405 | prose | pages [14] -->
According to the researches of Bass, Lawrence and Sultan, q is usually larger than 10p . So the internal influence is the determining factor.

<!-- b000406 | heading | pages [14] -->
6.2 Establishing Norton Model for EVs and CVs

<!-- b000407 | prose | pages [14] -->
Both External-influence model and Internal-influence model study the diffusion of one innovation. In order to simulate the substitution of EVs and CVs, a diffusion model based on External-influence model and Internal-influence model can be established here.

<!-- b000408 | prose | pages [14] -->
Eq.16 can be simplified as

<!-- b000409 | prose | pages [14] -->
N t ( ) 

<!-- b000410 | furniture | pages [14] -->


<!-- b000411 | prose | pages [14] -->
Mf t ( ) (17) f t is a probability of using the innovation. ( )

<!-- b000412 | prose | pages [14] -->
1

<!-- b000413 | furniture | pages [14] -->


<!-- b000414 | prose | pages [14] -->
f t

<!-- b000415 | prose | pages [14] -->
( )

<!-- b000416 | prose | pages [14] -->


<!-- b000417 | prose | pages [14] -->
1

<!-- b000418 | prose | pages [14] -->
p q t

<!-- b000419 | prose | pages [14] -->


<!-- b000420 | prose | pages [14] -->
(

<!-- b000421 | prose | pages [14] -->


<!-- b000422 | prose | pages [14] -->
)

<!-- b000423 | prose | pages [14] -->
e

<!-- b000424 | prose | pages [14] -->
 

<!-- b000425 | prose | pages [14] -->
(18)

<!-- b000426 | prose | pages [14] -->
q e p q t

<!-- b000427 | prose | pages [14] -->


<!-- b000428 | prose | pages [14] -->
(

<!-- b000429 | prose | pages [14] -->


<!-- b000430 | prose | pages [14] -->
)

<!-- b000431 | prose | pages [14] -->
 

<!-- b000432 | prose | pages [14] -->
p

<!-- b000433 | prose | pages [14] -->
We come up with the following assumption to establish the Norton model and apply to simulate the substitution process.

<!-- b000434 | prose | pages [14] -->
 The EV drivers will not use CVs again.  The average purchase rate for EVs is approximately invariable.  EVs can not only take place of CVs, but it also may attract new users.

<!-- b000435 | prose | pages [14] -->
The diffusion equation of CVs :

<!-- b000436 | furniture | pages [14] -->


<!-- b000437 | prose | pages [14] -->
  (19) M f t N t ( )  1 1 1 The diffusion equation of EVs :

<!-- b000438 | furniture | pages [14] -->


<!-- b000439 | prose | pages [14] -->
N t f t ( )  ( - 2 2

<!-- b000440 | prose | pages [14] -->
Where, , the meaning of

<!-- b000441 | prose | pages [14] -->
f t  ( ) 1- ( - ) 2 2

<!-- b000442 | prose | pages [14] -->
  (20) M M f t   ) - ( ) 2 2 1 1

<!-- b000443 | prose | pages [14] -->
if t and M are the same as the N t , t   2 ( ) ( ) i i i  is the time when EVs enter the market. When models mentioned above.

<!-- b000444 | prose | pages [14] -->
2 i , 1 , it stands for EVs. Coefficients q and p are usually it stands for CVs. When i  2 estimated by the previous data.

<!-- b000445 | prose | pages [14] -->
Norton model can simulate the variation trend and the number of EVs and CVs. To some extent, it can predict the future development of EVs especially in the amount of EVs.

<!-- b000446 | heading | pages [14] -->
6.3 Results and Conclusion

<!-- b000447 | prose | pages [14] -->
We take the private cars in China as an example. Assume EVs come to the market completely in 2015. We find the number of private cars in China from 1985 to 2008 and then calculate the coefficients q and p through MatLab (curve fitting tool). We get the result as shown in Figure 7.

<!-- b000448 | furniture | pages [15] -->
[Team #10607]

<!-- b000449 | furniture | pages [15] -->


<!-- b000450 | furniture | pages [15] -->
[Page 15 of 20]

<!-- b000451 | furniture | pages [15] -->


<!-- b000452 | caption | pages [15] -->
Figure 7. The number of EVs and CVs (prediction)

<!-- b000453 | prose | pages [15] -->
From Figure 7, we can see the number of CVs reach the maximum in 2028, and then goes down gradually. As for EVs, the number will not increase quickly after the launch. But After 2030, its increase becomes more and more obvious. The growth peak will arise in 2042 and eventually the number of EVs will gradually reach the market capacity.

<!-- b000454 | prose | pages [15] -->
We think our prediction is basically reasonable. One of the most important reasons that EVs can finally take place of CVs is that our petroleum resource will run out in nearly 2060 or even sooner.

<!-- b000455 | heading | pages [15] -->
6.4 Evaluations of Our Model

<!-- b000456 | heading | pages [15] -->
6.4.1 Strengths

<!-- b000457 | prose | pages [15] -->
  Norton model's strength is its enormous edibility. For instance, not only it

<!-- b000458 | prose | pages [15] -->
can be applied to EVs, but it can also be used to simulate the other technical substitutions.   Norton model can precisely simulate the number of EVs and CVs at all

<!-- b000459 | prose | pages [15] -->
time.   Both internal and external market information is considered in Norton

<!-- b000460 | prose | pages [15] -->
Model. So the model can thoroughly analyze the change of EVs and CVs.

<!-- b000461 | heading | pages [15] -->
6.4.2 Weaknesses

<!-- b000462 | prose | pages [15] -->
   Some special data can’t be found, and it makes that we have to do some

<!-- b000463 | prose | pages [15] -->
proper assumption before the solution of our models. A more abundant data resource can guarantee a better result in our models.    The algorithm used to estimate the coefficients may not be that precise.

<!-- b000464 | prose | pages [15] -->
Because the innovation coefficient and imitation coefficient may be different when the technology of EVs is improved. So here if we use GA(Genetic Algorithm) to estimate the coefficients, it may improve the accuracy of our model. But the mode of growth will not be changed.

<!-- b000465 | furniture | pages [15] -->


<!-- b000466 | heading | pages [15] -->
VII. Analysis of the Key Factors

<!-- b000467 | prose | pages [15] -->
For government

<!-- b000468 | prose | pages [15] -->
   According to our model of the environmental impact, we find out the

<!-- b000469 | prose | pages [15] -->
proportion of different kinds of power stations is one of the key factor

<!-- b000470 | furniture | pages [16] -->
[Team #10607]

<!-- b000471 | furniture | pages [16] -->


<!-- b000472 | furniture | pages [16] -->
[Page 16 of 20]

<!-- b000473 | prose | pages [16] -->
influencing the development of EVs. If a country’s thermal power stations take up a large proportion in all the power stations, EVs will also pollute the environment a lot, which makes EVs lose competitiveness. So government should use more clean and renewable energy to generate electricity and decrease the number of thermal power stations.    In our analysis on the economic impact, the EV allowance provided by

<!-- b000474 | prose | pages [16] -->
government is also a key factor. The more allowance government provides, the sooner the large scale use of EVs will be.    In the light of our economic impact analysis, government can impose

<!-- b000475 | prose | pages [16] -->
environment pollution tax and encourage people to use EVs.    Government should build more EV charging stations in order to make

<!-- b000476 | prose | pages [16] -->
charging convenient.    In the health impact analysis, we can know EVs are good for humans’

<!-- b000477 | prose | pages [16] -->
health. Government should enhance the propaganda about the benefits of EVs.

<!-- b000478 | furniture | pages [16] -->


<!-- b000479 | prose | pages [16] -->
For vehicle manufacturers

<!-- b000480 | prose | pages [16] -->
   In the economic impact, the cost of an EV is the most important factor

<!-- b000481 | prose | pages [16] -->
because the price directly determines whether people will buy an EV. So vehicle manufacturers should improve the EV technology and lower the cost of an EV.    Another key factor is the performance of EVs. The performance of EVs is

<!-- b000482 | prose | pages [16] -->
not as good as CVs, which will prevent a number of people purchase EVs. So vehicle manufacturers should increase R&D investment to improve the performance of EVs.    Vehicle manufacturers should enhance the propaganda about the health,

<!-- b000483 | prose | pages [16] -->
economic and environmental benefits of EVs.

<!-- b000484 | furniture | pages [16] -->


<!-- b000485 | prose | pages [16] -->
VIII.Analysis of Energy Consumption

<!-- b000486 | prose | pages [16] -->
8.1The Comparison of the Energy Efficiency

<!-- b000487 | prose | pages [16] -->
After looking up related references, we find out the energy conversion efficiency from crude to driving power of CVs as shown in Figure 8.

<!-- b000488 | furniture | pages [16] -->


<!-- b000489 | caption | pages [16] -->
Figure 8. The energy conversion efficiency of CVs

<!-- b000490 | prose | pages [16] -->
And the energy conversion efficiency of EVs is also shown in Figure 9.

<!-- b000491 | furniture | pages [16] -->


<!-- b000492 | caption | pages [16] -->
Figure 9. The energy conversion efficiency of EVs

<!-- b000493 | furniture | pages [17] -->
[Team #10607]

<!-- b000494 | furniture | pages [17] -->


<!-- b000495 | furniture | pages [17] -->


<!-- b000496 | furniture | pages [17] -->
[Page 17 of 20]

<!-- b000497 | prose | pages [17] -->
Using Figure 8 and Figure 9, we figure out the energy conversion efficiency WTW(well to wheel) of CV is 15.2%. And WTW of EV is 28.1%. The result also proves that EVs is more efficient in energy using than CVs.

<!-- b000498 | heading | pages [17] -->
8.2 Estimate of Saved Fossil Fuels

<!-- b000499 | prose | pages [17] -->
In order to Estimate of saved fossil fuels by widely using EVs, we establish Eq.21 to calculate the crude a CV consumes in one year.

<!-- b000500 | furniture | pages [17] -->


<!-- b000501 | prose | pages [17] -->
S

<!-- b000502 | prose | pages [17] -->
crude

<!-- b000503 | prose | pages [17] -->
c (21)   r

<!-- b000504 | prose | pages [17] -->
Where, r is the ratio of fuel oil to the crude and c (kg) is the average amount of fuel oil a CV consumes in one year.

<!-- b000505 | prose | pages [17] -->
According to relevant data from China National Petroleum, 1 ton crude can be refined to 0.25 ton gasoline and 0.45 ton diesel (international average). And each CV consumes 1.5 ton fuel oil per year. As a result, we can get and r  0.7 . As mentioned in the previous section, the total number of automobiles c kg  1500 is nearly 1.15 billion.

<!-- b000506 | prose | pages [17] -->
Assume EVs take up 70% in all the vehicles nowadays. The saved crude is nearly 2.46 billion ton. If EVs take up 80% and 90% in all the vehicles nowadays, the saved crude is up to 2.82 billion ton and 3.18 billion ton respectively.

<!-- b000507 | prose | pages [17] -->
Although the crude is saved by widely using EVs, the electricity will be consumed more. We focus on the amount of used coal in generating electricity for EVs. So Eq.2 is established to calculate the electricity a EV consume in one year

<!-- b000508 | prose | pages [17] -->
E 

<!-- b000509 | furniture | pages [17] -->


<!-- b000510 | prose | pages [17] -->
extra

<!-- b000511 | prose | pages [17] -->
ce (22) a

<!-- b000512 | prose | pages [17] -->
Where, c (kg) is the average amount of fuel oil a CV consumes in one year and a (kg) is the hundred kilometer oil consumption. e ( kw h ) stands for the  hundred kilometer electricity consumption.

<!-- b000513 | prose | pages [17] -->
According to relevant references, we get a  c  e  8 1500 20 , and . So

<!-- b000514 | prose | pages [17] -->
is 3750. If EVs take up 70%, 80% and 90% in all the vehicles nowadays, the E extra amount of electricity consumed by EVs is up to 3018.7 billion kw h , 3450 billion  respectively. We get 0.3kg coal can generate one , 3881.2 billion kw h kw h kilowatt-hour electricity. So according to the proportion of the thermal power stations, the amount of coal that is used to generate electricity for EVs is 905.61kg, 1035kg and 1164.3kg.

<!-- b000515 | prose | pages [17] -->
The estimate results mentioned above is based on the number of vehicles now. We just substitute a certain proportion of the CVs into EVs and calculate how much fossil fuel we can save and how much extra electricity and coal we may consume.

<!-- b000516 | prose | pages [17] -->
If we use the result of the Norton model (mentioned in previous section), we can estimate when the EVs will be large scale used and how much fossil fuel we will save at that time. According to our calculation, EVs will take up 80% in all the vehicles in 2045. The number of EVs will reach 1.95 billion and the number of CVs will reach 0.49 billion. So the amount of fossil fuel we will save in 2045 is 4.18 billion ton.

<!-- b000517 | furniture | pages [17] -->


<!-- b000518 | furniture | pages [17] -->


<!-- b000519 | furniture | pages [17] -->


<!-- b000520 | furniture | pages [18] -->
[Team #10607]

<!-- b000521 | furniture | pages [18] -->


<!-- b000522 | furniture | pages [18] -->


<!-- b000523 | furniture | pages [18] -->
[Page 18 of 20]

<!-- b000524 | prose | pages [18] -->
IX.Determining the Weight of Different Electricity

<!-- b000525 | prose | pages [18] -->
Generation

<!-- b000526 | prose | pages [18] -->
In order to determine the proportion of different types of electricity generation and maximum the environmental, social, commercial and individual

<!-- b000527 | heading | pages [18] -->
benefits, we apply AHP(Analytic Hierarchy Process)[ Thomas L.,1980] model to

<!-- b000528 | prose | pages [18] -->
determining the best proportion of electricity generation.

<!-- b000529 | prose | pages [18] -->
The hierarchy diagram of the electricity generation is shown in Figure 10.

<!-- b000530 | furniture | pages [18] -->


<!-- b000531 | caption | pages [18] -->
Figure 10.The hierarchy diagram

<!-- b000532 | prose | pages [18] -->
The AHP model divides the problem into three aspects: goal, criteria and alternatives. Here, our goal is to achieve maximum environmental, social and commercial benefits. The cost, efficiency, pollution, safety and development of EVs are our choosing criteria. All the four types of power are our alternatives.

<!-- b000533 | prose | pages [18] -->
Our aim is to determine the weights for thermal power, hydroenergy, nuclear power and others (solar power, wind power).

<!-- b000534 | prose | pages [18] -->
O C  C C 1 2

<!-- b000535 | prose | pages [18] -->
C 1.00 3.00 1

<!-- b000536 | prose | pages [18] -->
C 0.33 1.00 2

<!-- b000537 | prose | pages [18] -->
C 0.33 0.50 3

<!-- b000538 | prose | pages [18] -->
C 0.20 0.25 4

<!-- b000539 | prose | pages [18] -->
C 0.50 1.00 5

<!-- b000540 | prose | pages [18] -->
C C C 3 4 5

<!-- b000541 | prose | pages [18] -->
3.00 5.00 2.00

<!-- b000542 | prose | pages [18] -->
2.00 4.00 1.00

<!-- b000543 | prose | pages [18] -->
1.00 3.00 1.00

<!-- b000544 | prose | pages [18] -->
0.33 1.00 0.33

<!-- b000545 | prose | pages [18] -->
1.00 3.00 1.00

<!-- b000546 | caption | pages [18] -->
Table 9. The O-C judging matrix

<!-- b000547 | prose | pages [18] -->
Based on the analysis of each criterion and types of electricity generation, we develop judging matrixes (Table 9) to analyze the weight of each criterion. Take matrix as an example. The element the O C  C represents the importance of 12

<!-- b000548 | prose | pages [18] -->
C . We obtain the maximum eigenvalue of the O C to 1 1

<!-- b000549 | prose | pages [18] -->
 max The weight vector is

<!-- b000550 | prose | pages [18] -->
matrix. C 

<!-- b000551 | prose | pages [18] -->
 5.102 .

<!-- b000552 | prose | pages [18] -->
(0.7975,0.3941,0.2787,0.1130,0.3439)T w  1 We make the and get

<!-- b000553 | prose | pages [18] -->
n   max

<!-- b000554 | furniture | pages [18] -->


<!-- b000555 | prose | pages [18] -->
CI   0.03 n  1

<!-- b000556 | prose | pages [18] -->
(23)

<!-- b000557 | prose | pages [18] -->
0.03 (24) CR   0.02  0.1 1.12

<!-- b000558 | prose | pages [18] -->
matrix passes the consistency test. So the O C 

<!-- b000559 | furniture | pages [19] -->
[Team #10607]

<!-- b000560 | furniture | pages [19] -->


<!-- b000561 | furniture | pages [19] -->


<!-- b000562 | furniture | pages [19] -->
[Page 19 of 20]

<!-- b000563 | prose | pages [19] -->
Using the same method, we can develop the other judging matrixes , C P  1

<!-- b000564 | prose | pages [19] -->
. All , , and C P C P C P C P     2 3 4 5 matrixes are shown in Table 10.

<!-- b000565 | prose | pages [19] -->
Criteria

<!-- b000566 | prose | pages [19] -->
C C 1

<!-- b000567 | furniture | pages [19] -->


<!-- b000568 | prose | pages [19] -->
1b

<!-- b000569 | prose | pages [19] -->
Alternatives

<!-- b000570 | prose | pages [19] -->
1P

<!-- b000571 | prose | pages [19] -->
and CI of the other judging  max j j

<!-- b000572 | prose | pages [19] -->
C C C 2 2 3 4 5

<!-- b000573 | prose | pages [19] -->
2b 2b 3b 4b 5b

<!-- b000574 | prose | pages [19] -->
0.3261 0.9084

<!-- b000575 | prose | pages [19] -->
2P

<!-- b000576 | prose | pages [19] -->
0.1255 0.3865 0.1971

<!-- b000577 | prose | pages [19] -->
0.3999 0.3483

<!-- b000578 | prose | pages [19] -->
3P

<!-- b000579 | prose | pages [19] -->
0.6578 0.6396 0.4278

<!-- b000580 | prose | pages [19] -->
0.8427 0.1971

<!-- b000581 | prose | pages [19] -->
4P

<!-- b000582 | prose | pages [19] -->
0.3446 0.1801 0.6782

<!-- b000583 | prose | pages [19] -->
0.1535 0.1212

<!-- b000584 | furniture | pages [19] -->


<!-- b000585 | prose | pages [19] -->


<!-- b000586 | prose | pages [19] -->
0.6578 0.6396 0.5641

<!-- b000587 | prose | pages [19] -->
4.0205 4.0357 max j

<!-- b000588 | prose | pages [19] -->
CI

<!-- b000589 | prose | pages [19] -->
4.0019 4.0529 4.1659

<!-- b000590 | prose | pages [19] -->
0.0068 0.0119 j

<!-- b000591 | prose | pages [19] -->
CR

<!-- b000592 | prose | pages [19] -->
0.0006 0.0176 0.0553

<!-- b000593 | prose | pages [19] -->
0.0076 0.0132 j 0.0007 0.0196 0.0614

<!-- b000594 | prose | pages [19] -->
CI of the other judging matrixes  and

<!-- b000595 | caption | pages [19] -->
Table 10.

<!-- b000596 | prose | pages [19] -->
max j j j

<!-- b000597 | prose | pages [19] -->
We can see from Table 10 that all the judging matrixes have passed the consistency test. And the random consistency ratio of all the judging matrixes is shown in Eq.25

<!-- b000598 | prose | pages [19] -->
5

<!-- b000599 | prose | pages [19] -->


<!-- b000600 | prose | pages [19] -->
a CI

<!-- b000601 | prose | pages [19] -->
i

<!-- b000602 | prose | pages [19] -->
CR

<!-- b000603 | furniture | pages [19] -->


<!-- b000604 | prose | pages [19] -->


<!-- b000605 | prose | pages [19] -->
5

<!-- b000606 | prose | pages [19] -->


<!-- b000607 | prose | pages [19] -->
a RI

<!-- b000608 | prose | pages [19] -->
i

<!-- b000609 | prose | pages [19] -->
j j j

<!-- b000610 | prose | pages [19] -->


<!-- b000611 | prose | pages [19] -->
0.0192

<!-- b000612 | prose | pages [19] -->
(25)

<!-- b000613 | prose | pages [19] -->
j j j

<!-- b000614 | prose | pages [19] -->
So we get the weight vector we need as shown in Eq.26.

<!-- b000615 | furniture | pages [19] -->


<!-- b000616 | prose | pages [19] -->
w  (26) (0.3044,0.2553,0.2555,0.1848) 2 w is the proportion of different types of electricity The weight vector 2 generation. Thermal power takes up 0.3044, Hydroenergy takes up 0.2553, nuclear power takes up 0.2555 and others (solar power, wind power) takes up 0.1848. If the electricity generation is distributed by the weight vector w , not only can it greatly support the development of EVs, but it also gets the largest environmental, commercial and social benefits. According to the section above, we have known the electricity all the EVs (if EVs take up 80% in all the vehicles) need is 3450 billion kw h  in one year. So the amount of electricity needed to support EVs is 1050.18 billion kw h  by  by hydroenergy, 881.475 billion kw h thermal power, 880.785 billion kw h  by  by others.(See Figure 11) nuclear power and 637.56 billion kw h

<!-- b000617 | furniture | pages [19] -->


<!-- b000618 | caption | pages [19] -->
Figure 11. The proportion of different types of electric generation

<!-- b000619 | furniture | pages [20] -->
[Team #10607]

<!-- b000620 | furniture | pages [20] -->


<!-- b000621 | furniture | pages [20] -->
[Page 20 of 20]

<!-- b000622 | furniture | pages [20] -->


<!-- b000623 | heading | pages [20] -->
References

<!-- b000624 | references | pages [20] -->
Camilla Kazimi,1997. Evaluating the Environmental Impact of Alternative-Fuel

<!-- b000625 | references | pages [20] -->
Vehicles.Journal of Environmental Economics and Management. p:163-185.

<!-- b000626 | references | pages [20] -->
C. C. Chan ,2002.The State of the Art of Electric and Hybrid Vehicles. Proceedings of

<!-- b000627 | references | pages [20] -->
the Ieee, Vol. 90, No. 2, February 2002

<!-- b000628 | references | pages [20] -->
Karina Funk , Ari Rabl, 1999.Electric versus conventional vehicles: social costs

<!-- b000629 | references | pages [20] -->
and benefits in France. Transportation Research Part D 4 (1999): 397-411

<!-- b000630 | references | pages [20] -->
M. DeLuchi, Q. Wang and D. Sperling, 1989. Electric vehicles: performance, life

<!-- b000631 | references | pages [20] -->
cycle costs, emissions and recharging requirements, Transport. Res., 23A (3)

<!-- b000632 | references | pages [20] -->
(1989) p:255-278.

<!-- b000633 | references | pages [20] -->
Mikhail Granovskii,Ibrahim Dincer,Marc A. Rosen,2006. Economic aspects of

<!-- b000634 | references | pages [20] -->
greenhouse gas emissions reduction by utilisation of wind and solar

<!-- b000635 | references | pages [20] -->
energies to produce electricity and hydrogen. 2006 IEEE EIC Climate

<!-- b000636 | references | pages [20] -->
Change Conference (CCC 2006), vol.1.

<!-- b000637 | references | pages [20] -->
Ren Yulong, Li Haifeng, Sun Rui, Guan Ling, 2009. Analysis on Model of Life

<!-- b000638 | references | pages [20] -->
Cycle Cost of Electric Vehicle Based on Consumer Perspective. Technology

<!-- b000639 | references | pages [20] -->
Economics, Vol28:NO.11

<!-- b000640 | references | pages [20] -->
Saaty,Thomas L.,1980. The analytic hierarchy process: Planning, priority setting,

<!-- b000641 | references | pages [20] -->
resource allocation. McGraw-Hill International Book Co.

<!-- b000642 | references | pages [20] -->
South Coast Air Quality Management District, Air Quality Management Plan:

<!-- b000643 | references | pages [20] -->
South Coast Air Basin, Mar. 1989.

<!-- b000644 | references | pages [20] -->
Thomas A. Becker, Ikhlaq Sidhu , Burghardt Tenderich ,2009.Electric Vehicles in

<!-- b000645 | references | pages [20] -->
the United States, A New Model with Forecasts to 2030. Center for

<!-- b000646 | references | pages [20] -->
Entrepreneurship & Technology,2009.1.v.2.0 .P 1-2

<!-- b000647 | references | pages [20] -->
Wang Wen ,YuLei ,Pei Wen ,YangFang,2008 .Review of Emis sion Dispersion

<!-- b000648 | references | pages [20] -->
Models Ba sed on Gaus sian Line2Source Model. School of Traffic and

<!-- b000649 | references | pages [20] -->
Transportation ,Beijing Jiaotong University

<!-- b000650 | references | pages [20] -->
Wikimedia Foundation,2011. Electric vehicle. Accessed Feb.12 2011, form

<!-- b000651 | references | pages [20] -->
http://en.wikipedia.org/wiki/Electric_vehicles#cite_note-RSC-1.

<!-- b000652 | references | pages [20] -->
Wikimedia Foundation,2011. Toyota RAV4 EV. Accessed Feb.12 2011 form

<!-- b000653 | references | pages [20] -->
http://en.wikipedia.org/wiki/Toyota_RAV4_EV

<!-- b000654 | references | pages [20] -->
Yang Feng , Fu Jun, 2009. Analysis and Comparison of the Economical

<!-- b000655 | references | pages [20] -->
Efficiency of Pure Electric Vehicles. Journal of Wuhan University Of

<!-- b000656 | references | pages [20] -->
Technology (Information & Management Engineering). 2009, 31(2) p:7-10

<!-- b000657 | references | pages [20] -->
Yang Jinghui ,Wu Chun you,2005.  The application for a diffusion theory of

<!-- b000658 | references | pages [20] -->
adoption and substitution for successive generations with Norton

<!-- b000659 | references | pages [20] -->
model--Taking the modes of connecting with internet in China for example.

<!-- b000660 | references | pages [20] -->
Studies in Science of Science 2005, 23(5).p 682-687
