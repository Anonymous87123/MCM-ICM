# P-C-2011-10607-6ed4fd93

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
[Team #10607]

<!-- b000002 | furniture | pages [1] -->
[Page 1 of 20]

<!-- b000003 | heading | pages [1] -->
Contents

<!-- b000004 | contents | pages [1] -->
1. Introduction ..................................................................................................... 2

<!-- b000005 | contents | pages [1] -->
1.1 The Development of EVs ............................................................................... 2

<!-- b000006 | contents | pages [1] -->
1.2 Tasks and Approaches  .................................................................................. 2

<!-- b000007 | contents | pages [1] -->
2. Basic Assumptions ......................................................................................... 3

<!-- b000008 | contents | pages [1] -->
3. The Economic Comparison Model .................................................... 3

<!-- b000009 | contents | pages [1] -->
3.1 The Life Cycle Cost Model(LCC Model) ....................................................... 3

<!-- b000010 | contents | pages [1] -->
3.1.1 The Preparation Work for Model .................................................................... 3

<!-- b000011 | contents | pages [1] -->
3.1.2 Establishing the LCC Model ........................................................................... 4

<!-- b000012 | contents | pages [1] -->
3.2 Data Collection .............................................................................................. 5

<!-- b000013 | contents | pages [1] -->
3.3 Results of the Calculation .............................................................................. 6

<!-- b000014 | contents | pages [1] -->
3.4 Sensitivity Analysis........................................................................................ 6

<!-- b000015 | contents | pages [1] -->
4. The Environmental Impact Model .................................................... 7

<!-- b000016 | contents | pages [1] -->
4.1 The Primary Pollution:Air Pollution ............................................................... 7

<!-- b000017 | contents | pages [1] -->
4.1.1 Modeling the Emission Dispersion ................................................................ 7

<!-- b000018 | contents | pages [1] -->
4.1.1.1 The Gaussian Plume Model ................................................................ 7

<!-- b000019 | contents | pages [1] -->
4.1.1.2 Simulation of Gaussian Plume Model .............................................. 8

<!-- b000020 | contents | pages [1] -->
4.1.1.3 Results and Discussions of the Simulation ...................................... 9

<!-- b000021 | contents | pages [1] -->
4.1.2 Evalutions of Our Model ................................................................................ 10

<!-- b000022 | contents | pages [1] -->
4.1.2.1 Strengths ................................................................................................ 10

<!-- b000023 | contents | pages [1] -->
4.1.2.2 Weakness ................................................................................ 10

<!-- b000024 | contents | pages [1] -->
4.1.3 The Statistical Prediction of the Amount of Emissions ........................... 10

<!-- b000025 | contents | pages [1] -->
4.1.4 Conclusion ......................................................................................................... 10

<!-- b000026 | contents | pages [1] -->
4.2 Hidden Pollution .......................................................................................... 12

<!-- b000027 | contents | pages [1] -->
4.2.1 Noise Pollution ................................................................................................. 12

<!-- b000028 | contents | pages [1] -->
4.2.2 Used Batteries Pollution ................................................................................. 12

<!-- b000029 | contents | pages [1] -->
5. The health impact of EVs ................................................................ 12

<!-- b000030 | contents | pages [1] -->
6. Prediction of the Future Development of EVs ................................ 12

<!-- b000031 | contents | pages [1] -->
6.1 External-influence Model and Internal-influence Model ............................... 14

<!-- b000032 | contents | pages [1] -->
6.2 Establishing Norton Model for EVs and CVs ............................................... 14

<!-- b000033 | contents | pages [1] -->
6.3 Results and Conclusion ................................................................................ 15

<!-- b000034 | contents | pages [1] -->
6.4 Evalutions of Our Model .............................................................................. 15

<!-- b000035 | contents | pages [1] -->
6.4.1 Strengths ............................................................................................................ 15

<!-- b000036 | contents | pages [1] -->
6.4.2 Weakness ........................................................................................................... 15

<!-- b000037 | contents | pages [1] -->
7. Analysis of Key Factors ................................................................... 15

<!-- b000038 | contents | pages [1] -->
8. Analysis of the Energy Consumption .............................................. 16

<!-- b000039 | contents | pages [1] -->
8.1 The Comparison of the Energy Efficiency  .................................................. 16

<!-- b000040 | contents | pages [1] -->
8.2 Estimate of Saved Fossil Fuels  ................................................................... 17

<!-- b000041 | contents | pages [1] -->
9. Determining the Weight of Different Electricity Generation ......... 18

<!-- b000042 | contents | pages [1] -->
10. References .....................................................................................................20

<!-- b000043 | furniture | pages [2] -->
[Team #10607]

<!-- b000044 | furniture | pages [2] -->
[Page 2 of 20]

<!-- b000045 | heading | pages [2] -->
I. Introduction

<!-- b000046 | prose | pages [2] -->
Due to the concerns over urban environment, high oil costs and the improvements of battery technology, the electric vehicle (EV), which uses electric motors for propulsion, has been propelled to the forefront in recent years. Unlike the vehicle propelled by internal combustion engines (ICEs), the EVs are with the advantage of zero tailpipe emissions and an essentially silent, energy efficient motor. If batteries and cars can be perfectly combined, the EVs will lead a green revolution in realm of vehicle transportation. In order to analyse electric vehicles’ environmentally and economically sound, the following background is worth mentioning.

<!-- b000047 | heading | pages [2] -->
1.1 The Development of EVs

<!-- b000048 | prose | pages [2] -->
Electric vehicles first came into existence in the mid-19th century, when electricity was supposed to the preferred methods for motor vehicle propulsion. Due to low energy density of batteries, it was discontinued. As the new generation of ICEs emerged, it rapidly became the dominant propulsion method for motor vehicles but electric power has remained commonplace in other vehicle types, such as trains and smaller vehicles of all types. [Wikipedia Foundation,2011] In the early 1970s, some countries, compelled by the energy crisis, started the rekindling of interests in EVs. [C.C.Chan,2002] The improvements in battery technology over the past two decades have made it possible to design and manufacture electric vehicles with better performance. Though the number of electric vehicles on the roads is currently in the thousands, that number will soon change. Spurred by the breakthroughs in battery and automotive technology, many vehicle manufacturers have indicated their intention to begin mass producing electric vehicles with Lithium-ion batteries within the next five years. [Thomas A et al.,2009]

<!-- b000049 | heading | pages [2] -->
1.2 Tasks and Approaches

<!-- b000050 | prose | pages [2] -->
The above work has focused on the history and development of EVs. It seems that EVs could be the urban commuters’ panacea were it not for its high purchase price [Karina Funk et al.,1999]. However, the electricity used for EVs is produced by burning fossil fuels in power plants. That brings people to an important question: Is EVs widespread use feasible and practical?

<!-- b000051 | prose | pages [2] -->
So our goal is pretty clear:

<!-- b000052 | prose | pages [2] -->
 Model the environmental, economic, and health impacts of the widespread use of EVs  Detail the key factors that governments and vehicle manufacturers should consider when determining if and how to support the development and use of EVs  Estimate the amount of oil (fossil fuels) the world would save by widely using electric vehicles.

<!-- b000053 | prose | pages [2] -->
 Provide a model of the amount and type of electricity generation that would be needed to support the recommendations regarding the amount and type of electric vehicle use that will produce the largest number of benefits.

<!-- b000054 | furniture | pages [3] -->
[Team #10607]

<!-- b000055 | furniture | pages [3] -->
[Page 3 of 20]

<!-- b000056 | prose | pages [3] -->
Our approach mainly contributes on the following aspects:

<!-- b000057 | prose | pages [3] -->
 In order to deeply analyze economic outlook of EVs, the life cycle cost model (LCC Model) is come up with to compare the market prospect and economic benefits of EVs and t conventional vehicle.

<!-- b000058 | prose | pages [3] -->
 We focus on studying air pollution caused by EVs and CVs. Our purpose is to study the emissions from the space perspective. Gaussian Plume Model is applied here to simulate and predict the emission dispersion.

<!-- b000059 | prose | pages [3] -->
 Establish Norton model for EVs and CVs to make a prediction about the future development of EVs  Do discussion based on our work such as analysis on the key factors influencing the development of EVs, health impact.

<!-- b000060 | prose | pages [3] -->
 Use our models to calculate the amount of saved crude and the amount of extra coal and electricity.

<!-- b000061 | prose | pages [3] -->
 Applying AHP model to determining the weight of different types of electricity generation.

<!-- b000062 | heading | pages [3] -->
II. Basic Assumptions

<!-- b000063 | prose | pages [3] -->
 The related parameters of the EVs and conventional vehicles can reflect their features in the near future.

<!-- b000064 | prose | pages [3] -->
 There will be no new type of vehicles, which has an impact on the development of the conventional vehicles, appearing in the market.

<!-- b000065 | prose | pages [3] -->
 The EVs discussed in the paper refer to pure electric vehicles. We do not consider the hybrid EVs and hydrogen fuel cell vehicles.

<!-- b000066 | prose | pages [3] -->
 The assumptions of Norton model and the Gaussian Plume Model will be mentioned during the process of modeling.

<!-- b000067 | prose | pages [3] -->
 The data we used is accurate and reliable.

<!-- b000068 | heading | pages [3] -->
III. The Economic Comparison Model

<!-- b000069 | heading | pages [3] -->
3.1 The Life Cycle Cost Model (LCC Model)

<!-- b000070 | prose | pages [3] -->
Although the EV is not yet a completely mature technology, the great focus and interest on it still arises from a combination of concerns for urban air quality and high dependence on foreign supplies of oil. In the meantime, the advances in the EV battery and motor technology also have contributed the increasing interest.

<!-- b000071 | heading | pages [3] -->
3.1.1 Preparation Work for Model

<!-- b000072 | prose | pages [3] -->
The EVs can simply divide into pure electric vehicle (PEV), hybrid electric vehicle (HEV) and Fuel cell vehicles (FCV). In the elements, PEV is the technique base of EVs and can be applied to the future field of vehicle transportation. Thus, we take PEV as an example and recommend the life cycle cost model (LCC Model) to compare the market prospect and economic benefits of EVs and t conventional vehicle.

<!-- b000073 | prose | pages [3, 4] -->
Life-cycle cost is known as a pivotal criterion in a comparative evaluation of EVs and conventional vehicle[M. DeLuchi et al.,2009]. From the standpoint of consumers, the life cycle cost include the following 3 aspects: acquisition costs ( C ), maintenance costs ( C ), reclamation income ( iR ).Due to the worsening pi mi environmental pollution, we also take the cost of dealing with environmental C 、mi C 、iR and matters ( C ) into account. The life cycle cost is the sum total of ei pi C ,where i  represents the LCC of traditional automobile, stands for 1 i  2 ei the LCC of EVs.

<!-- b000074 | furniture | pages [4] -->
[Team #10607]

<!-- b000075 | furniture | pages [4] -->
[Page 4 of 20]

<!-- b000077 | heading | pages [4] -->
3.1.2 Establishing the LCC Model

<!-- b000078 | prose | pages [4] -->
 Acquisition Costs In this section, the cost of purchase is composed of the expenses of purchase and the related poundage. So acquisition cost can be expressed as following:

<!-- b000079 | prose | pages [4] -->
(1) C  p  h pi vi i Where, p is the expense of purchase, ih represents the related poundage, such vi as tax, license fee.

<!-- b000080 | prose | pages [4] -->
 Maintenance Costs The vehicle is known as a kind of durable goods and its cost of maintenance occupies 50% even more in the Life Cycle Cost Model. Conventional vehicles’ maintenance cost depends on the expenditure of repairing and vehicles refueling. We suppose the cost of repairing and refueling are m and 1o ,then we obtain : 1 (2) C m o   m 1 1 1 Where, , 1L is total kilometers, 1k means fuel consumption per o  L  k  p 1 1 1 g 100 km, p represents fuel cost per liter ($ / L ). g

<!-- b000081 | prose | pages [4] -->
As for EVs, electric charge replaces the role of fuel. Since the maintenance of the battery account for a large part of Maintenance costs, we consider the battery maintenance costs as an independent factor b ,the total sum of maintenance costs can be described as below:

<!-- b000082 | prose | pages [4] -->
(3) C  m  o  b m 2 2 2 Where, m is components maintenance costs of EVs and has the same method of 2 calculation as m . 2o means the battery charging fees and can be denote as 1 (4) o  L  p  k 2 /  2 2 e Where, L is total kilometers, ep means the cost of electricity per kw h , 2k is 2 electricity consumption per 100 km,  is charging efficiency.

<!-- b000083 | prose | pages [4] -->
The performance of battery will be poorer with time going by. As a result, the corresponding maintenance costs will increase. In order to describe the above process, we define bl denoting the total mileage of EVs during the life cycle of a battery. Suppose the purchase price of battery as bp . c is the charge for trouble when changing battery .Then the battery maintenance costs can be calculated as L 2 ( (5) b  p  c ) b l b  Reclamation Income Reclamation income consists of the money raised by selling assets and the subsidy policy for the reject and renovation of the old and used cars, something like the government-sponsored scrappage projects. Different types of cars have different reclamation income which can be found on the internet. We consume the reclamation income of EVs and conventional vehicles to be R and R . 1 2

<!-- b000084 | prose | pages [4, 5] -->
 Environmental Costs Conventional vehicles release at the place where they are operated, the emissions of hydrocarbons (HC) and nitrogen oxides (NOx) exceed 2000 tons per day. These pollutants react in the presence of sunshine to form ozone concentrations that are roughly three times larger than the federal health standard.[South Coast Air Quality Management District,1989]Therefore, to timely collect environmental taxation is imperative.

<!-- b000085 | furniture | pages [5] -->
[Team #10607]

<!-- b000086 | furniture | pages [5] -->
[Page 5 of 20]

<!-- b000088 | prose | pages [5] -->
Now there is no standard way to calculate environmental costs. Like some Europe nation collecting environmental pollution tax, we use the same method to 1r is the taxation of fuel per liter. obtain the environmental costs. Thus, suppose Then Environmental costs of conventional vehicles can be denoted as:

<!-- b000089 | prose | pages [5] -->
(6) C  r  L  k e 1 1 1 1 While EVs have reduced tailpipe carbon emissions, the energy they consume is produced by means that have environmental impacts. In addition, the manufacturing and depletion processing of batteries also have an impact to environment which also. The government needs comprehensive effort to curb the pollution which may cause a large amount of fiscal charges.

<!-- b000090 | prose | pages [5] -->
As for EVs, government should collecting environmental pollution tax for the battery recycle .The tax cost is stated as following:

<!-- b000091 | prose | pages [5] -->
L 2 C  r  (7) e 2 2 l b Where 2r is the taxation of battery pack. According to discussion above, we obtain the full life cycle cost:

<!-- b000092 | prose | pages [5] -->
LCC C C R C (8)     i pi mi i ei

<!-- b000093 | heading | pages [5] -->
3.2 Data Collection

<!-- b000094 | prose | pages [5] -->
After accessing relevant information, we take the RAV4 EV and RAV4 manufactured by Toyota as an example to compare the LCC of EVs and conventional vehicles. As we know the RAV4 EV is an all-electric version of the popular RAV4 [Wikipedia Foundation,2011]. The relevant parameters are listed in

<!-- b000095 | caption | pages [5] -->
Table 1.

<!-- b000096 | prose | pages [5] -->
Relevant Parameters RAV 4EV RAV4 p （$） Purchase Expense 60673 30336 vi ih ($) Related Poundage 6067 3033 Electricity Consumption per 100 km 2k 0 20 (kw.h) Oil Consumption per 100 km 1k (L) 0 8.5 Total Mileage of vehicle  (km) 500000 500000 Maintenance Costs per year  ($) 455 1516 Price of Battery bp ($) 3033 0 Total Mileage of battery (km) 40000 0

<!-- b000097 | caption | pages [5] -->
Table 1.  The relevant parameters of RAV4 EV and RAV.

<!-- b000098 | prose | pages [5] -->
(Data come from the reference [Yang Feng et al.,2009])

<!-- b000099 | prose | pages [5, 6] -->
As is revealed in the table, the related poundage is calculated by no more than 10% of the expenses of purchase. According to the of a latest believable reference, the expected life cycle of RAV4 EV and RAV4 is 10 years and the total mileage is set as 500000 km. As electric vehicles don't have clutch, gearbox and the other mechanical transmission equipment, maintenance costs of EVs is 70% less than Conventional vehicles. And the publicly recognized value of the battery charging efficiency is 85%. Users can obtain $3033 as reclamation income. Then due to the imperfect running of the current policy, users don’t need to undertake environmental costs. Thus, we don’t take environmental costs into calculation.

<!-- b000100 | furniture | pages [6] -->
[Team #10607]

<!-- b000101 | furniture | pages [6] -->
[Page 6 of 20]

<!-- b000103 | heading | pages [6] -->
3.3 Results of the Calculation

<!-- b000104 | prose | pages [6] -->
So after many times calculation under the conditions discussed above, we obtain statistic results as follow:

<!-- b000105 | prose | pages [6] -->
C p ih m o C b R LCC pi vi mi RAV4 EV 60673 6067 66740 455 8922 37920 51393 3033 115100 RAV4 30336 3033 33370 1516 422224 0 57393 3033 87728

<!-- b000106 | caption | pages [6] -->
Table 2.  The calculated results of relevant parameters and LCC($)

<!-- b000107 | prose | pages [6] -->
It can be seen from the statistics that the LCC of EVs is higher than the conventional vehicles while the cost on energy consumption is only 21.3% of conventional vehicles. And its failure rate as well as maintenance costs are lower than conventional vehicles. In the condition of reasonable acquisition cost and acceptable price of battery packs, the economic advantage of EVs is obvious.

<!-- b000108 | heading | pages [6] -->
3.4 Sensitivity Analysis

<!-- b000109 | prose | pages [6] -->
Then, in order to identify the most sensitive factor of impacting market prospect and economic benefits, we do sensitivity analysis about the above data. When the parameters are changed within 5%, we observe how much LCC change. The purpose is to analyze the sensitivity of iR and C , C , C . pi mi ei Before calculation, we choose the oil and electricity price, battery packs price, acquisition cost, mileage as the related parameters, because they may change over time and then produce a great fluctuation in price. We change the parameters within 5%, and then obtain the changing rate of LCC.

<!-- b000110 | prose | pages [6] -->
Acquisition cost Oil/Electricity Price Battery PacksPrice Mileage RAV4 EV 2.89% 0.38% 1.64% -1.56% RAV4 1.90% 2.40% - -

<!-- b000111 | caption | pages [6] -->
Table 3.  The Sensitivity Analysis between relevant parameters and LCC

<!-- b000112 | prose | pages [6] -->
As can be revealed in Table 3, the order of parameters sensitivity is proved to be: acquisition cost > battery packs price > mileage > electricity price. As for CVs, the results indicate as following: the oil price > acquisition cost.

<!-- b000113 | prose | pages [6, 7] -->
Based on the discussion above, the LCC of the CVs is less sensitive to the acquisition cost, as compared with the LCC of EVs. The LCC of CVs is more sensitive to oil and electricity price than the LCC of EVs. We can see that the LCC can, to some extent, be influenced by the price of battery packs and mileage. However, come to analyses from the long-term eyes, it is the inexorable trend to cut down the acquisition cost of EVs as well as the battery packs price. While with the large-scale exploitation of oil and mine, oil price will reveal a trend of increasing. According to the sensitivity analysis, the LCC of the conventional vehicles will increase gradually with the increasing of oil price. We can draw a conclusion that EVs has a lot of scope for improvement, which means that EVs are more economical in the future.

<!-- b000114 | furniture | pages [7] -->
[Team #10607]

<!-- b000115 | furniture | pages [7] -->
[Page 7 of 20]

<!-- b000117 | prose | pages [7] -->
The economic impact of EVs is obvious. First of all, the development of EVs can lower the cost of maintenance and with some technical improvements, the acquisition cost will also be much lower, which make more people afford a car. Besides, the large scale use of EVs also will create lots of new jobs and promote the development of economy.

<!-- b000118 | heading | pages [7] -->
IV. The Environmental Impact Model

<!-- b000119 | prose | pages [7] -->
There are two major types of pollution caused by vehicles. One is the primary pollution. The biggest part of primary pollution is the air pollution which is also the center of this section. And the other is the hidden pollution. It also plays a significant role in the impact on the environment.

<!-- b000120 | prose | pages [7] -->
We have already known the conventional vehicle is a tremendous threat to the environment. But after the comparison of electric vehicles (EVs) and conventional vehicles (CVs) presented by following sections, we can find out the environmental impact of large scale use of electric vehicles.

<!-- b000121 | heading | pages [7] -->
4.1 The primary pollution: Air pollution

<!-- b000122 | prose | pages [7] -->
Electric cars produce no pollution at the tailpipe which will contribute to cleaner air in cities, but their use increases demand for electricity generation. The amount of carbon dioxide emitted depends on the emission intensity of the power source used to charge the vehicle, the efficiency of the said vehicle and the energy wasted in the charging process [Wikipedia Foundation,2011] And meantime the power station will discharge extra emissions. So in fact EVs is not a vehicle with no emissions.

<!-- b000123 | prose | pages [7] -->
The pollutants produced by conventional vehicles mainly account for nitrites of oxygen, vehicle-born monoxide, hydrocarbon and carbon dioxide pollution. To simplify, environmental impact is considered by examining air pollution (AP) and greenhouse gas (GHG). [Mikhail Granovskii et al., 2006 ] The main gases in GHG emissions are CO and CH while the AP emissions includeCO , SO , NO x 2 4 and HC .

<!-- b000124 | prose | pages [7] -->
In order to better study the air pollution caused by EVs and CVs, we focus on the emissions dispersion and the amount of emissions.

<!-- b000125 | heading | pages [7] -->
4.1.1 Modeling the Emission Dispersion

<!-- b000126 | heading | pages [7] -->
4.1.1.1 The Gaussian Plume Model

<!-- b000127 | prose | pages [7] -->
Our purpose is to study the emissions from the space perspective. As the most classic model for emission dispersion, Gaussian Plume Model is applied here to simulate and predict the emission dispersion.

<!-- b000128 | prose | pages [7] -->
Before we establish the Gaussian Plume Model, we need to come up with these following assumptions.

<!-- b000129 | prose | pages [7] -->
 The electric vehicle is regarded as a still point source at ground-level.

<!-- b000130 | prose | pages [7] -->
 The direction of wind is parallel to X axis. So the pollutants are continuously discharged to one certain direction.

<!-- b000131 | prose | pages [7] -->
 The speed of wind is uniform and invariable.

<!-- b000132 | prose | pages [7] -->
 The mass of emissions is always conserved in the dispersion process.

<!-- b000133 | furniture | pages [8] -->
[Team #10607]

<!-- b000134 | furniture | pages [8] -->
[Page 8 of 20]

<!-- b000135 | prose | pages [8] -->
 The concentration of the pollution source is normally distributed in the y and z dimensions  The ground can’t absorb pollutants.

<!-- b000136 | caption | pages [8] -->
Figure 1. The coordinate plot of the point source and its polluted area

<!-- b000137 | prose | pages [8] -->
According to the assumptions, the source of emissions can be regarded as a point source. To start with, we use Cartesian Coordinate System to analyze the point source. For the point source on the ground, the Gaussian dispersion formula is shown as Eq.9.

<!-- b000138 | prose | pages [8] -->
2 2 y z  0.5(  ) q 2 2   C x y z e ( , , )  (9) y x  u y z Where, C x y z stands for the concentration of the emission (in micrograms ( , , ) per cubic meter) at any point in the polluted area. q is denoted as the quantity or mass of the emission (in grams) per unit of time (seconds) and u is the wind speed (in meters per second).  and  stand for the standard deviations of a y x statistically normal plume in the y and z dimensions, respectively.

<!-- b000139 | prose | pages [8] -->
According to the assumptions, we can obtain   q  (10) uCdydz   After putting specific number into all the coefficients, we can get the concentration of the emission at the stable state. Using this model, we can also figure out how far the pollutants may affect.

<!-- b000140 | heading | pages [8] -->
4.1.1.2 Simulation of Gaussian Plume Model

<!-- b000141 | prose | pages [8] -->
Now we use Matlab to simulate the emission dispersion of conventional vehicles. Let  be 1.5,  be 1.5 and u be 2. According to relevant reference, y x we obtain Table 4.

<!-- b000142 | prose | pages [8] -->
CVs EVs EVs Type of vehicle (gasoline) (thermal power) (Natural gas ) Mass of vehicle 1000 Kg 1200 Kg 1200 Kg HC 0.018 0.0008 0.0022 CO 0.91 0.0091 0.0182 NO2 0.0771 0.2948 0.1814 CO2 83 91 41 SOx 0.0045-0.4356 0.1814-0.7711 0.0003

<!-- b000143 | caption | pages [8] -->
Table 4. the comparison of emissions from different types of vehicles (kg/per car)

<!-- b000144 | prose | pages [8] -->
(Source: The Electric Vehicle Technical Report from General Motors)

<!-- b000145 | furniture | pages [9] -->
[Team #10607] [Page 9 of 20]

<!-- b000146 | prose | pages [9] -->
As mentioned above, the electric vehicle is a vehicle with no emissions. But the emissions shown in Table 4 are produced by the power stations which provide extra electricity for the electric vehicles. Here we just regard the emissions produced by power stations as the direct emissions produced by EVs (But EV itself is a no-emission vehicle).

<!-- b000147 | prose | pages [9] -->
EV (thermal power) means the electricity of electric vehicles are supplied by thermal power and EV (Natural gas) means the electricity of electric vehicles are supplied by natural gas.

<!-- b000148 | prose | pages [9] -->
We can see from Table 4, we divide all the emissions into two types: air pollution (AP) and greenhouse gas (GHG). So we calculate the amount of AP and GHG as well as normalize the AP value and GHG value of all types of vehicles. The normalized weighting coefficients of CVs, EVs (thermal power) and EVs(Natural gas) are 6.11, 3.86 and 1 respectively. The weighting coefficients are used to determine the amount of AP (the number of circles) in the simulation. And now we start the simulation of emission dispersion.

<!-- b000149 | heading | pages [9] -->
4.1.1.3 Results and Discussions of the Simulation

<!-- b000150 | caption | pages [9] -->
Figure 2. AP dispersion of CVs (gasoline)

<!-- b000151 | prose | pages [9] -->
Figure 2 shows that the emissions of CVs spread farthest and affect the largest area in all types of vehicles in the comparison. And its total amount of AP (represented by the number of circles) is also the maximum value. Of all the compared vehicles, CVs is the culprit that should be blamed for worsening air quality.

<!-- b000152 | caption | pages [9] -->
Figure 3. AP dispersion of EVs (thermal power)

<!-- b000153 | prose | pages [9] -->
Figure 3 shows that the emissions of EVs (thermal power) rank the second in the affected area and the amount of AP. So if EVs are powered by a thermal power station, the pollution to the environment is still big but not bigger than CVs(gasoline).

<!-- b000154 | furniture | pages [10] -->
[Team #10607] [Page 10 of 20]

<!-- b000155 | caption | pages [10] -->
Figure 4. AP dispersion of EVs (natural gas)

<!-- b000156 | prose | pages [10] -->
Figure 4 shows that EVs(natural gas) is the greenest vehicles in the compared types. From this point, if the electricity is generated by a clean and efficient energy such as solar energy and wind energy, the EVs will be much more environmentally friendly.

<!-- b000157 | prose | pages [10] -->
Besides, we can also use the same method to analyze the dispersion of GHG. Because the dispersion is similar, we will not go to details.

<!-- b000158 | heading | pages [10] -->
4.1.2 Evaluation of the model

<!-- b000159 | heading | pages [10] -->
4.1.2.1 Strengths

<!-- b000160 | list | pages [10] -->
 Gaussian plume model can precisely describe the dispersion of emissions. It builds up an equation to calculate the concentration of every point in the polluted area.

<!-- b000161 | list | pages [10] -->
 Gaussian plume has a strong flexibility. It can be applied to all kinds of gases and point sources.

<!-- b000162 | heading | pages [10] -->
4.1.2.2 Weaknesses

<!-- b000163 | list | pages [10] -->
 Gaussian plume model considers the dispersion of emissions too ideally and it can’t consider the influence of other factors.

<!-- b000164 | list | pages [10] -->
 Gaussian plume model can only be used to describe the point source. If we consider a moving vehicle, the model has to be improved.

<!-- b000165 | heading | pages [10] -->
4.1.3 The Statistical Prediction of the Amount of Emissions

<!-- b000166 | prose | pages [10] -->
According to relevant references, we get the emission data as shown in Table 5.

<!-- b000167 | source_object | pages [10] -->
Type of vehicle CVs EVs Air pollution(AP) emissions 20.64 5.023 Greenhouse gas(GHG) emissions 320 130

<!-- b000168 | caption | pages [10] -->
Table 5. the average emissions of CVs and EVs (g/per km, per car) (Source: The Electric Vehicle Technical Report from General Motors)

<!-- b000169 | prose | pages [10] -->
We establish three scenarios (Table 6) in order to analyze the impact of large scale use of EVs on the amount of emissions.

<!-- b000170 | source_object | pages [10] -->
Proportion of CVs Proportion of EVs Scenario 1 80% 20% Scenario 2 50% 50% Scenario 3 20% 80%

<!-- b000171 | caption | pages [10] -->
Table 6. Three scenarios of different proportion of CVs and EVs

<!-- b000172 | furniture | pages [11] -->
[Team #10607]

<!-- b000173 | furniture | pages [11] -->
[Page 11 of 20]

<!-- b000174 | prose | pages [11] -->
Eq.11 and Eq.12 are established here to calculate the total amount of air S ( ) i and Greenhouse gas emissions S ( ) i . pollution emissions AP GHG S ( ) i  CV  p n  EV  q n (11) AP AP i AP i S ( ) i  CV  p n  EV  q n (12) GHG GHG i GHG i CV CV Where, and are AP emissions of a CV and GHG emissions of AP GHG EV EV a CV respectively. Similarly, and are AP emissions of a EV and AP GHG ip is the proportion of CVs in scenario i GHG emissions of a EV respectively.

<!-- b000175 | prose | pages [11] -->
iq is the proportion of EVs in scenario i . n stands for the number of while vehicles in the world.

<!-- b000176 | prose | pages [11] -->
Year 2004 2005 2006 2007 2008 2009 the amount of 851 896 943 993 1047 1100 vehicles

<!-- b000177 | caption | pages [11] -->
Table 7. The total number of vehicles in the world (million)

<!-- b000178 | prose | pages [11] -->
Source: U.S Census Bureau

<!-- b000179 | prose | pages [11] -->
According to Table 7, we roughly estimate the number of vehicles around the world is 1.15 billion. Using Eq.11 and Eq.12 we can calculate the amount of AP emissions and GHG emissions in all the scenarios (Figure 5. and Figure 6.)

<!-- b000180 | caption | pages [11] -->
Figure 5. The amount of AP emissions in three scenarios

<!-- b000181 | caption | pages [11] -->
Figure 6. The amount of GHG emissions in three scenarios

<!-- b000182 | prose | pages [11] -->
The statistical prediction describes the amount of AP and GHG emissions when electric vehicles are used in a small scale and a large scale.

<!-- b000183 | heading | pages [11] -->
4.1.4 Conclusion

<!-- b000184 | prose | pages [11] -->
Generally speaking, large scale use of EVs can greatly improve the environment especially the air quality.

<!-- b000185 | prose | pages [11, 12] -->
To be specific, large scale use of EVs can improve the air quality near the road and narrow down the polluted area. And the spread of the emissions will be slowed down as well. The amount of emissions will also significantly go down, which may control the air pollution.

<!-- b000186 | furniture | pages [12] -->
[Team #10607]

<!-- b000187 | furniture | pages [12] -->
[Page 12 of 20]

<!-- b000189 | heading | pages [12] -->
4.2 Hidden Pollution

<!-- b000190 | heading | pages [12] -->
4.2.1 Noise Pollution

<!-- b000191 | prose | pages [12] -->
The noise pollution caused by the conventional vehicles may be ridiculous to some people. But if you live by the main road, you will know it suffers a lot.

<!-- b000192 | prose | pages [12] -->
We find out some data about the comparison of noise pollution caused by CVs and EVs. (Table 8) CVs EVs Noise Speed Inside Outside Inside Outside 35 km/h 73 67 67 66 Uniform Velocity 50 km/h 70 69 70 66 35 km/h 81 75 72 66 Acceleration 50 km/h 76 72 71 66

<!-- b000193 | caption | pages [12] -->
Table 8. The noise of CVs and EVs in different speed and state (dB)

<!-- b000194 | prose | pages [12] -->
From Table 8, we can large scale use of EVs is an efficient way to reduce noise. So if the EVs had been used widely, it would improve the living conditions near the road. People who live near road may have a sweet sleep.

<!-- b000195 | heading | pages [12] -->
4.2.2 Used Batteries Pollution

<!-- b000196 | prose | pages [12] -->
The widespread use of batteries has already created many environmental concerns, such as toxic metal pollution which is the most serious problem. If the large scale use of EVs becomes reality, the used batteries pollution will be much more serious than nowadays.

<!-- b000197 | prose | pages [12] -->
There exist so many toxic metals in the battery such as mercury, cadmium, manganese, nickel and lead. Take mercury as an example. Mercury is the main cause of Japanese Minamata disease. If mercury is ingested by mistake, it may trigger unimaginable consequence.

<!-- b000198 | heading | pages [12] -->
V. The Health Impact of EVs

<!-- b000199 | prose | pages [12] -->
On one hand, the environmental impact is closely related to the health impact. For example, the air pollution of CVs will greatly affect people’s respiratory health. So large scale use of EVs can help to control air pollution, which is good news for us humans. But the battery pollution may contaminate the food and water people eat, poisoning some people. On the other hand, the Harmonic from charging station may do harm to humans’ heart and brain.

<!-- b000200 | heading | pages [12] -->
VI. Prediction of the Future Development of EVs

<!-- b000201 | prose | pages [12, 13] -->
Having analyzed the environmental, economic and health impact of widespread use of EVs, we find out that EVs have the potential to take place of CVs. The technical difficulties are basically solved nowadays. With some technical improvements and the government’s Omni-directional support, EVs can become the main current vehicles. So generally speaking, we are optimistic about the future of EVs. Based on this point of view, we use a diffusion theory model of substitution (Norton Model) to simulate the process of substitution. Through Norton Model, we can see how the number of EVs changes.

<!-- b000202 | furniture | pages [13] -->
[Team #10607]

<!-- b000203 | furniture | pages [13] -->
[Page 13 of 20]

<!-- b000205 | prose | pages [13] -->
The purpose of this section is to demonstrate the feasibility of EVs and predict the future development of EVs.

<!-- b000206 | heading | pages [13] -->
6.1 External-influence Model and Internal-influence Model

<!-- b000207 | prose | pages [13] -->
Before establishing the Norton Model, we introduce the External-influence Model and Internal-influence Model. The external-influence model is made up with an ordinary differential equation (Eq.13) and used to describe the diffusion of technical innovation in the potential market.

<!-- b000208 | prose | pages [13] -->
dN t ( )   n t ( )   p M  N t ( ) (13) dt Where, N t is the accumulated number of people who have used the ( ) innovation by time t . M is the upper limit of the number of potential users. p is the innovation coefficient. n t is the number of people who use the innovation ( ) at time t , namely the probability of using the innovation at time t . From Eq.13, we can know the plot of N t is an exponential function. The model attributes the ( ) innovation diffusion to the people who haven’t used the innovation. So this is why the model is called external-influence model.

<!-- b000209 | prose | pages [13] -->
Similarly, the internal-influence model is also described by an ordinary differential equation (Eq.14). It is also used to simulate the diffusion of technical innovation.

<!-- b000210 | prose | pages [13] -->
dN t ( ) q   n t ( )   N t ( ) M - N t ( ) (14) dt M The meaning of n t are the same as the external-influence N t , M and ( ) ( ) model. q is the imitation coefficient. The internal-influence model assumes the diffusion speed is in proportion to the number of innovation users and the number of non users. That means the innovation diffusion is only driven by the number of innovation users. The plot of N t is a logistic curve. ( ) Both External-influence model and Internal-influence model can’t describe the innovation diffusion well. So we need to combine two models to one in order to precisely simulate the innovation diffusion.

<!-- b000211 | prose | pages [13, 14] -->
dN t ( ) q     n t ( )   p M - N t ( )  N t ( ) M - N t ( ) (15) dt M Where, the meaning of n t , q and p are the same as the N t , M , ( ) ( ) models mentioned above. represents the external influence while   p M  N t ( ) q N t stands for the internal influence.   ( ) M  N t ( ) M We solve the ordinary differential equation and obtain -( p q t  ) 1- e N t ( )  M (16) q e -( p q t  ) 1  p Where, . The inflection point of is m  0 , 0  q  1 , 0  p  1 N t ( ) 2   and the curve is symmetrical about the inflection point. 1 q m p (  q ) In ( ),   p  q p 4 q   According to the researches of Bass, Lawrence and Sultan, q is usually larger than 10p . So the internal influence is the determining factor.

<!-- b000212 | furniture | pages [14] -->
[Team #10607]

<!-- b000213 | furniture | pages [14] -->
[Page 14 of 20]

<!-- b000215 | heading | pages [14] -->
6.2 Establishing Norton Model for EVs and CVs

<!-- b000216 | prose | pages [14] -->
Both External-influence model and Internal-influence model study the diffusion of one innovation. In order to simulate the substitution of EVs and CVs, a diffusion model based on External-influence model and Internal-influence model can be established here.

<!-- b000217 | prose | pages [14] -->
Eq.16 can be simplified as N t ( )  Mf t ( ) (17) f t is a probability of using the innovation. ( )  ( p q t  ) 1  e (18) f t ( )  q e  ( p q t  ) 1  p We come up with the following assumption to establish the Norton model and apply to simulate the substitution process.

<!-- b000218 | prose | pages [14] -->
 The EV drivers will not use CVs again.

<!-- b000219 | prose | pages [14] -->
 The average purchase rate for EVs is approximately invariable.

<!-- b000220 | prose | pages [14] -->
 EVs can not only take place of CVs, but it also may attract new users.

<!-- b000221 | prose | pages [14] -->
The diffusion equation of CVs :

<!-- b000222 | prose | pages [14] -->
  N t ( )  M f t ( ) 1- f t  ( - ) (19) 1 1 1 2 2 The diffusion equation of EVs :

<!-- b000223 | prose | pages [14] -->
  (20) N t ( )  f t ( -  ) M - M f t ( ) 2 2 2 2 1 1 Where, , the meaning of if t and M are the same as the t   N t , ( ) ( ) 2 i i models mentioned above.  is the time when EVs enter the market. When i , 1 2 it stands for CVs. When , it stands for EVs. Coefficients q and p are usually i  2 estimated by the previous data.

<!-- b000224 | prose | pages [14] -->
Norton model can simulate the variation trend and the number of EVs and CVs. To some extent, it can predict the future development of EVs especially in the amount of EVs.

<!-- b000225 | heading | pages [14] -->
6.3 Results and Conclusion

<!-- b000226 | prose | pages [14] -->
We take the private cars in China as an example. Assume EVs come to the market completely in 2015. We find the number of private cars in China from 1985 to 2008 and then calculate the coefficients q and p through MatLab (curve fitting tool). We get the result as shown in Figure 7.

<!-- b000227 | furniture | pages [15] -->
[Team #10607]

<!-- b000228 | furniture | pages [15] -->
[Page 15 of 20]

<!-- b000229 | caption | pages [15] -->
Figure 7. The number of EVs and CVs (prediction)

<!-- b000230 | prose | pages [15] -->
From Figure 7, we can see the number of CVs reach the maximum in 2028, and then goes down gradually. As for EVs, the number will not increase quickly after the launch. But After 2030, its increase becomes more and more obvious. The growth peak will arise in 2042 and eventually the number of EVs will gradually reach the market capacity.

<!-- b000231 | prose | pages [15] -->
We think our prediction is basically reasonable. One of the most important reasons that EVs can finally take place of CVs is that our petroleum resource will run out in nearly 2060 or even sooner.

<!-- b000232 | heading | pages [15] -->
6.4 Evaluations of Our Model

<!-- b000233 | heading | pages [15] -->
6.4.1 Strengths

<!-- b000234 | prose | pages [15] -->
  Norton model's strength is its enormous edibility. For instance, not only it can be applied to EVs, but it can also be used to simulate the other technical substitutions.

<!-- b000235 | prose | pages [15] -->
  Norton model can precisely simulate the number of EVs and CVs at all time.

<!-- b000236 | prose | pages [15] -->
  Both internal and external market information is considered in Norton Model. So the model can thoroughly analyze the change of EVs and CVs.

<!-- b000237 | heading | pages [15] -->
6.4.2 Weaknesses

<!-- b000238 | prose | pages [15] -->
   Some special data can’t be found, and it makes that we have to do some proper assumption before the solution of our models. A more abundant data resource can guarantee a better result in our models.

<!-- b000239 | prose | pages [15] -->
   The algorithm used to estimate the coefficients may not be that precise.

<!-- b000240 | prose | pages [15] -->
Because the innovation coefficient and imitation coefficient may be different when the technology of EVs is improved. So here if we use GA(Genetic Algorithm) to estimate the coefficients, it may improve the accuracy of our model. But the mode of growth will not be changed.

<!-- b000241 | heading | pages [15] -->
VII. Analysis of the Key Factors

<!-- b000242 | prose | pages [15, 16] -->
For government    According to our model of the environmental impact, we find out the proportion of different kinds of power stations is one of the key factor influencing the development of EVs. If a country’s thermal power stations take up a large proportion in all the power stations, EVs will also pollute the environment a lot, which makes EVs lose competitiveness. So government should use more clean and renewable energy to generate electricity and decrease the number of thermal power stations.

<!-- b000243 | furniture | pages [16] -->
[Team #10607]

<!-- b000244 | furniture | pages [16] -->
[Page 16 of 20]

<!-- b000246 | prose | pages [16] -->
   In our analysis on the economic impact, the EV allowance provided by government is also a key factor. The more allowance government provides, the sooner the large scale use of EVs will be.

<!-- b000247 | prose | pages [16] -->
   In the light of our economic impact analysis, government can impose environment pollution tax and encourage people to use EVs.

<!-- b000248 | prose | pages [16] -->
   Government should build more EV charging stations in order to make charging convenient.

<!-- b000249 | prose | pages [16] -->
   In the health impact analysis, we can know EVs are good for humans’ health. Government should enhance the propaganda about the benefits of EVs.

<!-- b000250 | prose | pages [16] -->
For vehicle manufacturers    In the economic impact, the cost of an EV is the most important factor because the price directly determines whether people will buy an EV. So vehicle manufacturers should improve the EV technology and lower the cost of an EV.

<!-- b000251 | prose | pages [16] -->
   Another key factor is the performance of EVs. The performance of EVs is not as good as CVs, which will prevent a number of people purchase EVs.

<!-- b000252 | prose | pages [16] -->
So vehicle manufacturers should increase R&D investment to improve the performance of EVs.

<!-- b000253 | prose | pages [16] -->
   Vehicle manufacturers should enhance the propaganda about the health, economic and environmental benefits of EVs.

<!-- b000254 | prose | pages [16] -->
VIII.Analysis of Energy Consumption

<!-- b000255 | heading | pages [16] -->
8.1The Comparison of the Energy Efficiency

<!-- b000256 | prose | pages [16] -->
After looking up related references, we find out the energy conversion efficiency from crude to driving power of CVs as shown in Figure 8.

<!-- b000257 | caption | pages [16] -->
Figure 8. The energy conversion efficiency of CVs

<!-- b000258 | prose | pages [16] -->
And the energy conversion efficiency of EVs is also shown in Figure 9.

<!-- b000259 | caption | pages [16] -->
Figure 9. The energy conversion efficiency of EVs

<!-- b000260 | furniture | pages [17] -->
[Team #10607]

<!-- b000261 | furniture | pages [17] -->
[Page 17 of 20]

<!-- b000262 | prose | pages [17] -->
Using Figure 8 and Figure 9, we figure out the energy conversion efficiency WTW(well to wheel) of CV is 15.2%. And WTW of EV is 28.1%. The result also proves that EVs is more efficient in energy using than CVs.

<!-- b000263 | heading | pages [17] -->
8.2 Estimate of Saved Fossil Fuels

<!-- b000264 | prose | pages [17] -->
In order to Estimate of saved fossil fuels by widely using EVs, we establish Eq.21 to calculate the crude a CV consumes in one year.

<!-- b000265 | prose | pages [17] -->
c (21) S  crude r Where, r is the ratio of fuel oil to the crude and c (kg) is the average amount of fuel oil a CV consumes in one year.

<!-- b000266 | prose | pages [17] -->
According to relevant data from China National Petroleum, 1 ton crude can be refined to 0.25 ton gasoline and 0.45 ton diesel (international average). And each CV consumes 1.5 ton fuel oil per year. As a result, we can get and r  0.7 . As mentioned in the previous section, the total number of automobiles c  1500 kg is nearly 1.15 billion.

<!-- b000267 | prose | pages [17] -->
Assume EVs take up 70% in all the vehicles nowadays. The saved crude is nearly 2.46 billion ton. If EVs take up 80% and 90% in all the vehicles nowadays, the saved crude is up to 2.82 billion ton and 3.18 billion ton respectively.

<!-- b000268 | prose | pages [17] -->
Although the crude is saved by widely using EVs, the electricity will be consumed more. We focus on the amount of used coal in generating electricity for EVs. So Eq.2 is established to calculate the electricity a EV consume in one year ce E  (22) extra a Where, c (kg) is the average amount of fuel oil a CV consumes in one year and a (kg) is the hundred kilometer oil consumption. e ( kw h ) stands for the  hundred kilometer electricity consumption. According to relevant references, we get a  8 c  1500 e  20 , and . So is 3750. If EVs take up 70%, 80% and 90% in all the vehicles nowadays, the E extra amount of electricity consumed by EVs is up to 3018.7 billion kw h , 3450 billion , 3881.2 billion kw h  respectively. We get 0.3kg coal can generate one kw h kilowatt-hour electricity. So according to the proportion of the thermal power stations, the amount of coal that is used to generate electricity for EVs is 905.61kg, 1035kg and 1164.3kg.

<!-- b000269 | prose | pages [17] -->
The estimate results mentioned above is based on the number of vehicles now. We just substitute a certain proportion of the CVs into EVs and calculate how much fossil fuel we can save and how much extra electricity and coal we may consume.

<!-- b000270 | prose | pages [17] -->
If we use the result of the Norton model (mentioned in previous section), we can estimate when the EVs will be large scale used and how much fossil fuel we will save at that time. According to our calculation, EVs will take up 80% in all the vehicles in 2045. The number of EVs will reach 1.95 billion and the number of CVs will reach 0.49 billion. So the amount of fossil fuel we will save in 2045 is 4.18 billion ton.

<!-- b000271 | furniture | pages [18] -->
[Team #10607]

<!-- b000272 | furniture | pages [18] -->
[Page 18 of 20]

<!-- b000273 | prose | pages [18] -->
IX.Determining the Weight of Different Electricity Generation In order to determine the proportion of different types of electricity generation and maximum the environmental, social, commercial and individual benefits, we apply AHP(Analytic Hierarchy Process)[ Thomas L.,1980] model to determining the best proportion of electricity generation.

<!-- b000274 | prose | pages [18] -->
The hierarchy diagram of the electricity generation is shown in Figure 10.

<!-- b000275 | caption | pages [18] -->
Figure 10.The hierarchy diagram

<!-- b000276 | prose | pages [18] -->
The AHP model divides the problem into three aspects: goal, criteria and alternatives. Here, our goal is to achieve maximum environmental, social and commercial benefits. The cost, efficiency, pollution, safety and development of EVs are our choosing criteria. All the four types of power are our alternatives.

<!-- b000277 | prose | pages [18] -->
Our aim is to determine the weights for thermal power, hydroenergy, nuclear power and others (solar power, wind power).

<!-- b000278 | prose | pages [18] -->
O  C C C C C C 1 2 3 4 5 C 1.00 3.00 3.00 5.00 2.00 1 C 0.33 1.00 2.00 4.00 1.00 2 C 0.33 0.50 1.00 3.00 1.00 3 C 0.20 0.25 0.33 1.00 0.33 4 C 0.50 1.00 1.00 3.00 1.00 5

<!-- b000279 | caption | pages [18] -->
Table 9. The O-C judging matrix

<!-- b000280 | prose | pages [18, 19] -->
Based on the analysis of each criterion and types of electricity generation, we develop judging matrixes (Table 9) to analyze the weight of each criterion. Take the O matrix as an example. The element C represents the importance of  C 12 C to C . We obtain the maximum eigenvalue of the O matrix.  C 1 1   5.102 . max The weight vector is (0.7975,0.3941,0.2787,0.1130,0.3439)T w  (23) 1 We make the and get   n 0.03 max CI   0.03 CR   0.02  0.1 (24) n  1 1.12 So the O matrix passes the consistency test.  C Using the same method, we can develop the other judging matrixes , C  P 1 , , and . All and CI of the other judging C  P C  P C  P C  P  2 3 4 5 max j j matrixes are shown in Table 10.

<!-- b000281 | furniture | pages [19] -->
[Team #10607]

<!-- b000282 | furniture | pages [19] -->
[Page 19 of 20]

<!-- b000284 | prose | pages [19] -->
Criteria C C C C C 1 2 3 4 5 1b 2b 3b 4b 5b Alternatives 1P 0.9084 0.3261 0.1255 0.3865 0.1971 2P 0.3483 0.3999 0.6578 0.6396 0.4278 3P 0.1971 0.8427 0.3446 0.1801 0.6782 4P 0.1212 0.1535 0.6578 0.6396 0.5641  4.0357 4.0205 4.0019 4.0529 4.1659 max j CI 0.0119 0.0068 0.0006 0.0176 0.0553 j CR 0.0132 0.0076 0.0007 0.0196 0.0614 j  CI of the other judging matrixes and

<!-- b000285 | caption | pages [19] -->
Table 10.

<!-- b000286 | prose | pages [19] -->
max j j We can see from Table 10 that all the judging matrixes have passed the consistency test. And the random consistency ratio of all the judging matrixes is shown in Eq.25 5  a CI j j i CR   0.0192 (25) 5  a RI j j i So we get the weight vector we need as shown in Eq.26.

<!-- b000287 | prose | pages [19] -->
(26) w  (0.3044,0.2553,0.2555,0.1848) 2 The weight vector w is the proportion of different types of electricity 2 generation. Thermal power takes up 0.3044, Hydroenergy takes up 0.2553, nuclear power takes up 0.2555 and others (solar power, wind power) takes up 0.1848. If the electricity generation is distributed by the weight vector w , not only can it greatly support the development of EVs, but it also gets the largest environmental, commercial and social benefits. According to the section above, we have known the electricity all the EVs (if EVs take up 80% in all the vehicles) need is 3450 billion kw h  in one year. So the amount of electricity needed to support EVs is 1050.18 billion kw h  by thermal power, 880.785 billion kw h  by hydroenergy, 881.475 billion kw h  by nuclear power and 637.56 billion kw h  by others.(See Figure 11)

<!-- b000288 | caption | pages [19] -->
Figure 11. The proportion of different types of electric generation

<!-- b000289 | furniture | pages [20] -->
[Team #10607]

<!-- b000290 | furniture | pages [20] -->
[Page 20 of 20]

<!-- b000291 | heading | pages [20] -->
References

<!-- b000292 | references | pages [20] -->
Camilla Kazimi,1997. Evaluating the Environmental Impact of Alternative-Fuel

<!-- b000293 | references | pages [20] -->
Vehicles.Journal of Environmental Economics and Management. p:163-185.

<!-- b000294 | references | pages [20] -->
C. C. Chan ,2002.The State of the Art of Electric and Hybrid Vehicles. Proceedings of

<!-- b000295 | references | pages [20] -->
the Ieee, Vol. 90, No. 2, February 2002

<!-- b000296 | references | pages [20] -->
Karina Funk , Ari Rabl, 1999.Electric versus conventional vehicles: social costs

<!-- b000297 | references | pages [20] -->
and benefits in France. Transportation Research Part D 4 (1999): 397-411

<!-- b000298 | references | pages [20] -->
M. DeLuchi, Q. Wang and D. Sperling, 1989. Electric vehicles: performance, life

<!-- b000299 | references | pages [20] -->
cycle costs, emissions and recharging requirements, Transport. Res., 23A (3)

<!-- b000300 | references | pages [20] -->
(1989) p:255-278.

<!-- b000301 | references | pages [20] -->
Mikhail Granovskii,Ibrahim Dincer,Marc A. Rosen,2006. Economic aspects of

<!-- b000302 | references | pages [20] -->
greenhouse gas emissions reduction by utilisation of wind and solar

<!-- b000303 | references | pages [20] -->
energies to produce electricity and hydrogen. 2006 IEEE EIC Climate

<!-- b000304 | references | pages [20] -->
Change Conference (CCC 2006), vol.1.

<!-- b000305 | references | pages [20] -->
Ren Yulong, Li Haifeng, Sun Rui, Guan Ling, 2009. Analysis on Model of Life

<!-- b000306 | references | pages [20] -->
Cycle Cost of Electric Vehicle Based on Consumer Perspective. Technology

<!-- b000307 | references | pages [20] -->
Economics, Vol28:NO.11

<!-- b000308 | references | pages [20] -->
Saaty,Thomas L.,1980. The analytic hierarchy process: Planning, priority setting,

<!-- b000309 | references | pages [20] -->
resource allocation. McGraw-Hill International Book Co.

<!-- b000310 | references | pages [20] -->
South Coast Air Quality Management District, Air Quality Management Plan:

<!-- b000311 | references | pages [20] -->
South Coast Air Basin, Mar. 1989.

<!-- b000312 | references | pages [20] -->
Thomas A. Becker, Ikhlaq Sidhu , Burghardt Tenderich ,2009.Electric Vehicles in

<!-- b000313 | references | pages [20] -->
the United States, A New Model with Forecasts to 2030. Center for

<!-- b000314 | references | pages [20] -->
Entrepreneurship & Technology,2009.1.v.2.0 .P 1-2

<!-- b000315 | references | pages [20] -->
Wang Wen ,YuLei ,Pei Wen ,YangFang,2008 .Review of Emis sion Dispersion

<!-- b000316 | references | pages [20] -->
Models Ba sed on Gaus sian Line2Source Model. School of Traffic and

<!-- b000317 | references | pages [20] -->
Transportation ,Beijing Jiaotong University

<!-- b000318 | references | pages [20] -->
Wikimedia Foundation,2011. Electric vehicle. Accessed Feb.12 2011, form

<!-- b000319 | references | pages [20] -->
http://en.wikipedia.org/wiki/Electric_vehicles#cite_note-RSC-1.

<!-- b000320 | references | pages [20] -->
Wikimedia Foundation,2011. Toyota RAV4 EV. Accessed Feb.12 2011 form

<!-- b000321 | references | pages [20] -->
http://en.wikipedia.org/wiki/Toyota_RAV4_EV

<!-- b000322 | references | pages [20] -->
Yang Feng , Fu Jun, 2009. Analysis and Comparison of the Economical

<!-- b000323 | references | pages [20] -->
Efficiency of Pure Electric Vehicles. Journal of Wuhan University Of

<!-- b000324 | references | pages [20] -->
Technology (Information & Management Engineering). 2009, 31(2) p:7-10

<!-- b000325 | references | pages [20] -->
Yang Jinghui ,Wu Chun you,2005.  The application for a diffusion theory of

<!-- b000326 | references | pages [20] -->
adoption and substitution for successive generations with Norton

<!-- b000327 | references | pages [20] -->
model--Taking the modes of connecting with internet in China for example.

<!-- b000328 | references | pages [20] -->
Studies in Science of Science 2005, 23(5).p 682-687
