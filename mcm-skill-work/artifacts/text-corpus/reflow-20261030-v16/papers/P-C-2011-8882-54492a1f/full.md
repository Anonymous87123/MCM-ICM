# P-C-2011-8882-54492a1f

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #8882

<!-- b000002 | furniture | pages [1] -->
Page 1of 27

<!-- b000003 | heading | pages [1] -->
CONTENTS

<!-- b000004 | contents | pages [1] -->
1. Introduction...........................................................................................................................1

<!-- b000005 | contents | pages [1] -->
2. Assumptions..........................................................................................................................2

<!-- b000006 | contents | pages [1] -->
3. A Brief View of CV, EV and HEV........................................................................................2

<!-- b000007 | contents | pages [1] -->
4. Simulation of Quantities of CV, EV and HEV......................................................................3

<!-- b000008 | contents | pages [1] -->
4.1 Increase of Number of Total Vehicles .........................................................................3

<!-- b000009 | contents | pages [1] -->
4.2 Growth of Quantities of CV, EV and HEV .................................................................5

<!-- b000010 | contents | pages [1] -->
5. Energy Demand and Supply from/for EV and HEV.............................................................7

<!-- b000011 | contents | pages [1] -->
5.1 Electricity Demand from EV/HEV .............................................................................8

<!-- b000012 | contents | pages [1] -->
5.2 Off-Peak Charging Supply for EV and HEV ..............................................................8

<!-- b000013 | contents | pages [1] -->
5.3 Extra Energy Supply for EV/HEV and Its Optimization ..........................................10

<!-- b000014 | contents | pages [1] -->
6. Environmental, Economic, Social and Health Impacts of EV/HEV...................................14

<!-- b000015 | contents | pages [1] -->
6.1 EV/HEV Consumes Less Fossil Fuels......................................................................14

<!-- b000016 | contents | pages [1] -->
6.2 Driving EV and HEV Costs Less..............................................................................18

<!-- b000017 | contents | pages [1] -->
6.3 New Vehicle Industry Provides More Job Opportunities..........................................19

<!-- b000018 | contents | pages [1] -->
6.4 Invest in New Vehicle Industry is Rewarding...........................................................21

<!-- b000019 | contents | pages [1] -->
6.5 EV/HEV Reduce Pollutions and Do Good for Health ..............................................23

<!-- b000020 | contents | pages [1] -->
7. Conclusion ..........................................................................................................................24

<!-- b000021 | contents | pages [1] -->
8. References...........................................................................................................................26

<!-- b000022 | furniture | pages [2] -->
Team #8882

<!-- b000023 | furniture | pages [2] -->
Page 1of 27

<!-- b000024 | heading | pages [2] -->
1. Introduction

<!-- b000025 | prose | pages [2] -->
Today we have 800 million vehicles in the world with roughly 70 million new ones built each year. By current vehicle growth rate, we will end up with 3 billion cars on the planet by 2035.1 The majority of vehicles on the road in 2010 are conventional vehicles (CV) based on ICEs. [1] Considering the average amount of petroleum each vehicle takes annually, it will need several times the volume of oil reserves currently known in Saudi Arabia just to fuel them2. How would we be able to power such huge number of vehicles? How to deal with the staggering emission from them? The gloomy answers to these questions compel us to strive for sustainable road transportation. It seems that electric vehicle (EV) could address this issue positively.[2] For detailed analysis, we classify vehicle into three kinds: conventional vehicle (CV), electric vehicle (EV) and hybrid-electric vehicle (HEV). [8]

<!-- b000026 | prose | pages [2] -->
In this paper, we will model the environmental, economical, social and health impacts of EV/HEV within the next 50 years and in three typical areas—China, USA and France. The formation of our paper is shown in Figure 1.

<!-- b000027 | caption | pages [2] -->
Figure 1. Formation of our paper

<!-- b000028 | prose | pages [2] -->
First of all, we will simulate the quantity of CV, EV and HEV in France, USA and China. Logistic model is introduced and historic data of vehicle quantities is collected to fit the coefficients of logistic model. At the same time, the role of government will take place to control and optimize the quantities of CV, EV and HEV, in order to achieve lower fossil fuel consumption.

<!-- b000029 | prose | pages [2] -->
Next, we will respond to the demand for electrical energy from EV/HEV in these countries. Supply plans of amount and type of electricity generation will be designed by model that involves the following concerns. (1) During this process, the supply plan will be in conformity with domestic energy allowance. (2) Government should

<!-- b000030 | prose | pages [2] -->
1 http://www.hybridcars.com/fuels/will-electric-cars-rule-future-25049.html 2 http://www.hybridcars.com/fuels/will-electric-cars-rule-future-25049.html

<!-- b000031 | prose | pages [2, 3] -->
1 also take steps to reduce the reliance of electricity generation upon fossil fuels. (3) It is also desirable to strive for the lowest costs of the energy supply plan as much as possible.

<!-- b000032 | furniture | pages [3] -->
Team #8882

<!-- b000033 | furniture | pages [3] -->
Page 2of 27

<!-- b000035 | prose | pages [3] -->
Finally, we model the environmental, social, economic, and health impacts of the widespread use of EV/HEV. Environmental impact is mainly considered as the consumption of fossil fuels. Social impact is viewed from the savings of driving EV/HEV for individuals. Economic impact involves new job opportunities from EV/HEV and power industry. Health impact will be measured by the nitrogen generation. We compare all these figures under two different scenarios. One scenario is where quantities of CV, EV and HEV accord with our simulation. The other one is where all EVs/HEVs are replaced by CV. In other words, we will compare all these impacts between “mixed-vehicle world” and “pure-CV world”. Thus the impacts of EV/HEV will be clearly revealed.

<!-- b000036 | heading | pages [3] -->
2. Assumptions

<!-- b000037 | prose | pages [3] -->
1. We will select one vehicle mode to represent CV, EV and HEV each. 2. We assume there is no difference in performance of each vehicle type. 3. We select France, USA, and China to represent European countries, American countries and Asian countries. 4. We assume performance of CV, EV and HEV will not change in the future. 5. Based on common sense, we assume each vehicle travels 10,000 km every year. 6 We will not specify different types of power plants and assume that each plant will generate 10,000,000kwh annually on average. 7. We do not consider the dissipation during energy conversion.

<!-- b000038 | heading | pages [3] -->
3. A Brief View of CV, EV and HEV

<!-- b000039 | prose | pages [3] -->
Currently there are three types of vehicles. Conventional vehicle is driven by internal combustion engine. The majority of vehicles on the road in 2010 are conventional vehicles based on ICEs. Electric vehicles (EVs) are propelled by an electric motor (or motors) powered by rechargeable battery packs.[3] EV is also born with hybrid-electric vehicle (HEV) that could switch between electric-only mode and oil-only mode. [9] The advantages of electric power are apparent, as it could avoid tailpipe emission, enhance energy efficiency at low speed and utilize off-peak electricity; the disadvantages are equally obvious, considering a certain amount of electricity is ultimately generated by fossil fuels with pollutions released, the current battery capacity could not support high sustaining speed driving, and battery pollution is still a threat to our environment.

<!-- b000040 | prose | pages [3] -->
In the following chapters, a lot of discussions, analyses and computation would require data related to features of CV, EV and HEV. As different vehicle modes have

<!-- b000041 | prose | pages [3, 4] -->
2 different characteristics, we would select typical modes to represent different types in vehicle family, as shown in Table 1.

<!-- b000042 | furniture | pages [4] -->
Team #8882

<!-- b000043 | furniture | pages [4] -->
Page 3of 27

<!-- b000045 | caption | pages [4] -->
Table 1. Features of CV, EV and HEV

<!-- b000046 | prose | pages [4] -->
Typical Mode Features Price: from £39,995 3 CV 2010 Focus 1.4 Duratec Produce 155gCO2/km 4 Price: $108,000 Travel up to 220 miles without a recharge 5 Tesla Roadster EV Consume 450kJ/km 6 Price: $41000 7 Consumes 770kj/km in electric-only mode HEV Chevrolet Volt Produces 108gCO2/km in oil-only mode Run 50km without recharging and 420km without refueling

<!-- b000047 | heading | pages [4] -->
4. Simulation of Quantities of CV, EV and HEV

<!-- b000048 | heading | pages [4] -->
4.1 Increase of Number of Total Vehicles

<!-- b000049 | prose | pages [4] -->
The number of vehicles has increased more in the past decade than in the previous one century, and such trend will continue in the future. Although the alarm of fossil fuels has been around for years, the need for transportation is still expanding vehicle ownership, whether such need is met by driving CV, EV or HEV. Therefore, total vehicle quantity should be simulated first.

<!-- b000050 | prose | pages [4] -->
There are two major factors that influence the number of vehicles. The first one is population. Countries with larger population are more likely to have more vehicles, as the need for transportation is basically same for each common person. The second one is the geographic condition such as area of this region. Typically, larger area and good road condition are indicative of higher road capacity, and thus higher allowance for vehicles. If we put these two factors together, we are considering the density of population. In this sense, the growth of vehicle is comparable to the growth of biota with limited (sometimes fluctuated) natural resources where logistic mode is widely used to predict the growth of population. Thus, we seek similar approach to simulate the growth of vehicles with logistic mode as shown below.

<!-- b000051 | prose | pages [4] -->
3 http://www.ciao.co.uk/Ford_Fiesta_LX_1_4_TDCi_5dr__Review_5711296 4 http://www.ford.co.uk/Cars/Focus/BrochurePricesSpecifications 5 http://www.leftlanenews.com/tesla-roadster.html# 6 www.teslamotors.com 7 http://www.cardekho.com/carmodels/Chevrolet/Chevrolet_Volt

<!-- b000052 | prose | pages [4, 5] -->
3 ⎧ dx x = ⋅⋅ − r x (1 ) ⎪⎨ dt M (1) ⎪ = x (0) x ⎩ 0

<!-- b000053 | furniture | pages [5] -->
Team #8882

<!-- b000054 | furniture | pages [5] -->
Page 4of 27

<!-- b000056 | prose | pages [5] -->
According to (1), we can deduct the expression for the total vehicle number in the t year:

<!-- b000057 | prose | pages [5] -->
M = x t ( ) (2) M − + − ⋅ rt 1 ( 1) e x 0

<!-- b000058 | prose | pages [5] -->
Where x t is the total vehicle number in ( ) t year, r is intrinsic growth rate of

<!-- b000059 | prose | pages [5] -->
M is the ceiling of vehicle number and vehicle number, 0x is the vehicle number in

<!-- b000060 | prose | pages [5] -->
2010.

<!-- b000061 | prose | pages [5] -->
We adopt historic data and obtain the values of coefficients by fitting. As we will simulate situation in France, USA and China, we collect their quantities of total vehicles and list them in Table 2.

<!-- b000062 | caption | pages [5] -->
Table 2. Quantities of total vehicle in France, USA and China from 2005 to 2010

<!-- b000063 | prose | pages [5] -->
Vehicle Quantity\Year 2005 2006 2007 2008 2009 2010 France(107) 3 3.17 3.34 3.51 3.68 3.8 USA(108) 2.4 2.5 2.9 3.0 3.1 3.2 China(108) 1 1.11 1.24 1.37 1.52 1.68

<!-- b000064 | prose | pages [5] -->
The result of fitting is shown in Table 3.

<!-- b000065 | prose | pages [5] -->
Tabel 3. Values of coefficients in logistic mode acquired by fitting France USA China xm 60,000,000 600,000,000 1,400,000,000 0.115 0.115 0.115 r

<!-- b000066 | prose | pages [5] -->
Given the values of coefficients, our model could simulate the growth of quantities of vehicles. The result is shown in Figure 2, 3 and 4.

<!-- b000067 | prose | pages [5, 6] -->
4 Figure 2 Figure 3 Figure 4

<!-- b000068 | furniture | pages [6] -->
Team #8882

<!-- b000069 | furniture | pages [6] -->
Page 5of 27

<!-- b000071 | caption | pages [6] -->
Figure 2 shows the increase of vehicles in France, USA and China. In France, the

<!-- b000072 | prose | pages [6] -->
number will keep rising and become stable after 2030. The ultimate number is 60,000,000. In USA, the quantity of total vehicles increase steadily from 2010 to 2030, and remain almost unchanged after 2030. The ultimate number of vehicles will be about 600,000,000. In china, the number of vehicles will increase rapidly from 2015, and such rapid growth period will not end until 2050. The ultimate number will be about 1,400,000,000.

<!-- b000073 | heading | pages [6] -->
4.2 Growth of Quantities of CV, EV and HEV

<!-- b000074 | prose | pages [6] -->
Once the total number of vehicle each year in the future is known, we are going to simulate the quantities of CV, EV and HEV. There are many factors that would influence the distribution. EV and HEV have strong potentials to reduce the reliance upon fossil fuels, as electricity could come from other sources other than thermal power. When fossil fuels run out, we could power EV one way or another. HEV is an eclectic solution that could be a good choice at this moment. Therefore, EA and HEV (especially EA) should gradually take the place of CV. It is ideal that all vehicles will be converted to EA when fossil fuels run out. But exactly when will that time come? No one can answer. There are many different opinions and calculations and none really agree on the exact timing. Many different factors need to be considered including how much of each deposit is left in the Earth, how fast we are using each fossil fuel at the moment, and how this is likely to change in the future. If we start switching to alternative fuel sources that are renewable rather than non-renewable, the reserves that we have will obvious last longer. [4] Therefore, it is impossible to predict the fossil fuel reserve in 50 years. It is also impossible to determine the limit that fossil fuel poses upon vehicle oil consumption.

<!-- b000075 | prose | pages [6] -->
What we know for sure is that oil reserve will be running very low in 2055 according to current consumption and reserve. So we deem that government should reduce the oil consumption of vehicles by 90% of current consumption within 50 years. By achieving such goal, the reliance upon oil will be reduced and the impact of sudden drain of oil will be cushioned. Oil is consumed by CV and HEV during its

<!-- b000076 | prose | pages [6, 7] -->
5 oil-only mode that on average takes up 8/9 of this total travel distance8. We estimate the ratio of light vehicle to heavy one to be 3. As EVs are of smaller power, shorter range and HEV could provide bigger drive and longer range, EV would serve as light vehicle and HEV another. We speculate the ratio of EV to HEV in 2060 would also be 3. Thus we come up with the following equations.

<!-- b000077 | furniture | pages [7] -->
Team #8882

<!-- b000078 | furniture | pages [7] -->
Page 6of 27

<!-- b000080 | prose | pages [7] -->
⎧ 8 8 ⋅ + = ⋅ + ⋅ η z ( ) t z ( ) t [ z (2010) z (2010)] ( ) t ⎪ HEV CV HEV CV 9 9 ⎪ = z ( ) t z ( ) t R t ( ) ⎨ (3) EV HEV ⎪ + + = z ( ) t z ( ) t z ( ) t x t ( ) ⎪ CV EV HEV ⎩

<!-- b000081 | prose | pages [7] -->
Where z ( ) t is the number of CV in t year, z ( ) t is the number of EV in CV EV

<!-- b000082 | prose | pages [7] -->
t year, z ( ) t is the number of HEV in t year, x t is the total number of ( ) HEV

<!-- b000083 | prose | pages [7] -->
η vehicles in the t year, R t is the ratio of EV to HEV, R(2055) is 3, ( ) ( )t is

<!-- b000084 | prose | pages [7] -->
η coefficient that controls the reliance upon oil in t year and (2055) is 10%.

<!-- b000085 | prose | pages [7] -->
In Europe, EVs have been projected to reach 500 thousand by the year 1999. In Japan, the government's plan calls for 200 thousand EVs by the year 2000. Here in the US, air pollution regulations could translate into a production requirement of around 300--400 thousand EVs per year [5] Thus, we estimate the current EV/HEV number to be 5% of the total vehicle number in each country.

<!-- b000086 | prose | pages [7] -->
Government will also play a role in controlling the distribution of CV, EV and HEV to strive for largest number of benefits to the environment, society, business, and individuals. Thus we have our optimization model (4) and (5).

<!-- b000087 | prose | pages [7] -->
∑ η + η + η + η max E R ( , ) S R ( , ) B R ( , ) I R ( , ) (4)

<!-- b000088 | prose | pages [7] -->
η ≤ ⎧ E R ( , ) O ⎪ η ≥ S R ( , ) H ⎪⎨ s t . . (5) η ≥ B R ( , ) C ⎪ ⎪ η ≥Δ I R ( , ) P ⎩

<!-- b000089 | prose | pages [7] -->
Where E is the environmental factor, is the social factor, B is the business S factor, I is the individual factor, is the ceiling of the environmental factor, H is O Δ the lower limit of the social factor, is the lower limit of the business factor, P C is the lower limit of the individuals factor.

<!-- b000090 | prose | pages [7] -->
Thus we could simulate quantities of CV, EV and HEV in France, USA and China.

<!-- b000091 | prose | pages [7] -->
8 Vanderwerp D. 2011 Chevrolet volt full test – road test. Car and driver; 2010.

<!-- b000092 | prose | pages [7, 8] -->
6 The result is shown in Figure 5, 6 and 7.

<!-- b000093 | furniture | pages [8] -->
Team #8882

<!-- b000094 | furniture | pages [8] -->
Page 7of 27

<!-- b000096 | caption | pages [8] -->
Figure 5.

<!-- b000097 | caption | pages [8] -->
Figure 6.

<!-- b000098 | prose | pages [8] -->
Figure 7 Number of CV, EV and HEV in France Number of CV, EV and HEV in USA Number of CV, EV and HEV in China

<!-- b000099 | prose | pages [8] -->
R t ( ) The R(t) is decreasing in all three Figures, indicating the decline of oil consumption.

<!-- b000100 | prose | pages [8] -->
is rising, so EV will dominate the vehicle world in the future.

<!-- b000101 | caption | pages [8] -->
Figure 5 pictures the trend of vehicle quantities in France. As we can see, EV will

<!-- b000102 | prose | pages [8] -->
rise rapidly during the first 15 years from 0.4×107 to 4×107. It is due to less geographic limitation on traffic. CV would decrease from 2.5×107 to 0.54×107. Thus the reduction of CV is effective.

<!-- b000103 | caption | pages [8] -->
Figure 6 depicts the trend of vehicle quantities in USA. The situation is similar to

<!-- b000104 | prose | pages [8] -->
that of France. CV will decrease from 1.9×108 to 0.65×108; EV will increase from 0.25×108 to 4×108; HEV will increase from 0.25×108 to 1.4×108.

<!-- b000105 | caption | pages [8] -->
Figure 7 shows the trends of vehicle quantities in China. The increase of

<!-- b000106 | prose | pages [8] -->
EV/HEV is even more obvious than that of France and USA, from 0.11×108/0.11× 108 to 9.1×108/3.03×108. This indicates a huge EV/HEV market in China and a huge demand for electricity power. The control of CV quantity is not as effective as it seems in France and USA. It will rise from 0.9×108 to 2.3×108 and drop to 1.6× 108. The peak time appears in 2035. It is because the quantity of total vehicle will enter a rapid increase period at that time and increase of EV/HEV is not able to follow that trend. Although the total quantity of CV will ultimately increase, the proportion of CV in the entire vehicle will drop significantly, from 90% to 10%.

<!-- b000107 | heading | pages [8] -->
5. Energy Demand and Supply from/for EV and HEV

<!-- b000108 | prose | pages [8] -->
The surge of EV/HEV quantities in France, USA and China will definitely create huge demand for electricity, and supply plan is also needed. In this chapter, we will model the energy demand first. Then we will model the amount and type of electricity

<!-- b000109 | prose | pages [8, 9] -->
7 generation that would be needed to support the EV/HEV development under our plan. This model will provide us solutions to meet energy demand of huge quantity of EV and HEV in the future. Model will be established to consider environmental, social and economic effects.

<!-- b000110 | furniture | pages [9] -->
Team #8882

<!-- b000111 | furniture | pages [9] -->
Page 8of 27

<!-- b000113 | heading | pages [9] -->
5.1 Electricity Demand from EV/HEV

<!-- b000114 | prose | pages [9] -->
The demand for electricity can be modeled easily by (6).

<!-- b000115 | prose | pages [9] -->
∑ = ⋅ A t ( ) C Z t ( ) (6) i i i

<!-- b000116 | prose | pages [9] -->
Where A t ( ) is the electricity demanded in t year , C is the average electricity i

<!-- b000117 | prose | pages [9] -->
consumption per vehicle, iz t is th ( ) e num ber of i vehicle  the t year. ni

<!-- b000118 | prose | pages [9] -->
From Table 1 we know EV will consume 450kJ/km and HEV will take up 770kJ/km in electric mode. Also we have assumed each vehicle will travel 10,000km, and 1/8 of the distance traveled by HEV will be under electric-only mode. Thus we can figure out electricity demand from EV/HEV in France, USA and China.

<!-- b000119 | heading | pages [9] -->
5.2 Off-Peak Charging Supply for EV and HEV

<!-- b000120 | prose | pages [9] -->
Two typical electricity demand curves are shown in Figure 8. Peak period and off-peak period are colored differently. As we can see, a conspicuous rise and fall in electricity demand usually happens during a 24 hours electricity usage circle. The reason is quite simple, human activity in daytime is much more than that in the nighttime, creating a peak period in daytime and an off-peak period in nighttime. The fluctuations in power demand have always been an adverse factor for electricity generation. The generators have to run at full power in order to meet peak power demand. Yet when demand drops significantly, however, the power of generators can not simply follow down. Otherwise it will damage the gird system.[8] Thus electricity supply could only drop lightly during off-peak. Hence significant energy would be generated for no use, and the flow back of such energy is also undesirable for grid system. Such situation is very common in urban areas.

<!-- b000121 | prose | pages [9, 10] -->
8 The conventional method to deal with “extra electricity” is to store it by pulling up water or something else during off-peak period. In peak period, the lifted water could be used to generate electricity to meet soared energy demand. This process inevitably involves energy dissipation. Now we propose to directly use “extra electricity” to charge EV and HEV. In the left figure above, there are 66 blocks that shows the overall electricity generation, and there are 18 blocks in the “extra energy” areas during off-peak period. Thus, we estimate 27.3% of total electricity could be used for charging EV and HEV. If off-peak charging still cannot suffice the energy need from EV and HEV, other solution is needed. Now the effect of off-peak charging on general energy supply could be described in (7).

<!-- b000122 | furniture | pages [10] -->
Team #8882

<!-- b000123 | furniture | pages [10] -->
Page 9of 27

<!-- b000124 | caption | pages [10] -->
Figure 8. Electricity Supply in 24-hour-circle

<!-- b000126 | prose | pages [10] -->
= − ⎧ ( ) ( ) ( ) C t A t O t (7) ⎨ = ⋅ ( ) 27.3% ( ) O t G t ⎩

<!-- b000127 | prose | pages [10] -->
Where C t ( ) is the electricity needed in t year to power EV and HEV by extra

<!-- b000128 | prose | pages [10] -->
power stations,  A(t) is defined in (6), O t ( ) is the quantity of extra electrical energy

<!-- b000129 | prose | pages [10] -->
at off-peak times which can be used to charge EV/HEV in t year, G(t) is the overall electricity generation in each country.

<!-- b000130 | prose | pages [10] -->
The overall electricity generation data in 2005 is listed in Table 4.

<!-- b000131 | caption | pages [10] -->
Table 4. Annual Electricity Generation in France, USA and China

<!-- b000132 | prose | pages [10] -->
France USA China Electricity Generation(1014kJ)9 19.46 142.24 131.42

<!-- b000133 | prose | pages [10] -->
C(t) is shown in Figure 9, 10 and 11.

<!-- b000134 | prose | pages [10] -->
Figure 9 Figure 10 Figure 11

<!-- b000135 | prose | pages [10] -->
9 http://en.wikipedia.org/wiki/Nuclear_power_in_France; http://en.wikipedia.org/wiki/Nuclear_power_in_china; http://en.wikipedia.org/wiki/Nuclear_power_in_the_United_States

<!-- b000136 | prose | pages [10, 11] -->
9 Electricity needed to be generated in France Electricity needed to be generated in USA Electricity needed to be generated in China

<!-- b000137 | furniture | pages [11] -->
Team #8882

<!-- b000138 | furniture | pages [11] -->
Page 10of 27

<!-- b000140 | prose | pages [11] -->
The electricity needed to be generated for EV/HEV in 2005 is shown in Table 5

<!-- b000141 | caption | pages [11] -->
Table 5. Electricity needed to be generated for EV/HEV

<!-- b000142 | prose | pages [11] -->
France USA China Electricity Vacancy to power current EV and HEV(1014kJ) 0.314 2.641 -2.45

<!-- b000143 | prose | pages [11] -->
In France and USA, we still need extra electricity to power existing EV and HEV. Yet in China (2005), the negative figure indicates that the off-peak charging should completely suffice the entire need for existing EV and HEV due to the smaller quantity of EV. Thus, off-peak charging is desirable to be promoted around the world, especially in countries like China, where current electricity generation could support entire EV/HEV and no other measures are required to meet the energy demand.

<!-- b000144 | prose | pages [11] -->
Off-peak charging is also feasible and practical. EV and HEV can be simply left charging in nighttime while its owner goes to sleep, as long as he/she works and rests according to normal schedule. Government could also provide incentives to encourage off-peak charging. For example, the favored electricity price could be the most effective act to attract people charge their EVs or HEVs at night.

<!-- b000145 | prose | pages [11] -->
With energy consumption per EV and HEV known, we could know how many EVs and HEVs can be powered merely by off-peak charging. The result is shown in

<!-- b000146 | caption | pages [11] -->
Table 6.

<!-- b000147 | caption | pages [11] -->
Table 6. Number of EV/HEV supported by off-peak charging

<!-- b000148 | prose | pages [11] -->
France USA China Number of EV fed by off-peak charging 2,342,000 17,259,000 15,940,000 18,736,000 138,072,000 127,520,000 Number of HEV fed by off-peak charging

<!-- b000149 | heading | pages [11] -->
5.3 Extra Energy Supply for EV/HEV and Its Optimization

<!-- b000150 | prose | pages [11] -->
Off-peak charging will never suffice the electricity demand from EV/HEV in France and USA. And in China, it could only maintain the entire EV/HEV till 2012. After that off-peak charging will not be enough. Thus, we have to plan to extra energy supply for EV/HEV.

<!-- b000151 | prose | pages [11] -->
The extra electricity vacancy could come from thermal power, hydroelectricity, nuclear energy, wind power or solar energy. Each type of generation has its particular traits, say its cost, price, potential capacity and limitation. As for government, it is desirable to manage new power industry to achieve maximum environmental, economic, and social benefits. Thus, not only should we provide more electricity, we should also optimize the energy plan among several options. We will discuss demand

<!-- b000152 | prose | pages [11, 12] -->
10 and limitation of new power energy first, and then strive for optimization of mix plan.

<!-- b000153 | furniture | pages [12] -->
Team #8882

<!-- b000154 | furniture | pages [12] -->
Page 11of 27

<!-- b000156 | prose | pages [12] -->
First and foremost, new electricity generation should meet the electricity demand from EV and HEV. Second, each power option has its limit. For example, solar energy is limited by the energy the earth receives from the sun, which is abundant in desert; hydroelectricity is limited by water resources and geographic shape of landscape; wind power is also distributed without balance; nuclear power requires high level of technology and finance.

<!-- b000157 | prose | pages [12] -->
Further more, an urgent task for government is to reduce the proportion of thermal power in the effort to rely less on fossil fuels. For example, in USA, the current proportion of thermal power is 67%10. We recommend government should reduce such figure to 10%. 10% is by no means an unrealistic goal, as France has achieved within 40 years.

<!-- b000158 | prose | pages [12] -->
In addition, we recommend government to trade off between these energy options by achieving minimum electricity cost, as economic and financial factors are always the prioritized concerns of government and society.

<!-- b000159 | prose | pages [12] -->
With these three major concerns, we will model the energy plan in (8) and (9) ∑ ⋅ min p t ( ) x t ( ) (8) i i i ∑ ⎧ ≥ x t ( ) C t ( ) i ⎪⎪ i ≤ s t . . x t ( ) k t ( ) ⎨ (9) i i ⎪ ∑ ≤ ⋅ x t ( ) 10% x ( ) t ⎪⎩ 1 i i

<!-- b000160 | prose | pages [12] -->
Where ip t is the cost of per joule of ( ) i electrical energy in the t year, ix t ( )

<!-- b000161 | prose | pages [12] -->
is the generation of i type of electricity in the t year, x t is the thermal power 1( )

<!-- b000162 | prose | pages [12] -->
generation in the t year, ik t ( ) is the limit of i type of electricity generation in the

<!-- b000163 | prose | pages [12] -->
t year, C t has been defined in (7). ( )

<!-- b000164 | prose | pages [12] -->
We collect the prices of various kind of electricity in France, USA and China, as well as limitations of different types of electricity generation. The data is shown in

<!-- b000165 | caption | pages [12] -->
Table 7.

<!-- b000166 | prose | pages [12] -->
10 http://www.eia.doe.gov/aer/pecss_diagram.html

<!-- b000167 | prose | pages [12, 13] -->
11 k1(t) p1(t) p2(t) p3(t) p4(t) p5(t) k2(t) k3(t) k4(t) k5(t) Therma Thermal Hydro Nuclear Wind Solar Hydro Nuclear Wind Solar l 4× 0.8× 70× 1.8× 1.8× Franc 109kw 109kw 109kw 109kw 109kw 3 c/kwh 6 c/kwh 4 c/kwh 8 c/kwh 5 c/kwh e h h h h h 1.2× 0.9× 6× 0.9× 3× 1011kw 1011kw 1011kw 1011kw 1011kw 2 c/kwh 5 c/kwh 3 c/kwh 5 c/kwh 4 c/kwh USA h h h h h 0.18 0.1 0.2 0.5 0.3 1.8× 11× 5× 3× 4× 1011kw 1011kw 1011kw 1011kw 1011kw China RMB/k RMB/k RMB/k RMB/k RMB/k wh wh wh wh wh h h h h h

<!-- b000168 | furniture | pages [13] -->
Team #8882

<!-- b000169 | furniture | pages [13] -->
Page 12of 27

<!-- b000170 | caption | pages [13] -->
Table 7. Values of coefficients in (8) and (9)

<!-- b000172 | prose | pages [13] -->
Given the values of coefficients in this model, the result can be figured out and is shown in Figure 12. This is our electricity supply plan for France, USA and China.

<!-- b000173 | caption | pages [13] -->
Figure 12. Amount and type of electricity generation to meet energy demand from EV/HEV in France, USA and China

<!-- b000174 | prose | pages [13] -->
The left figure shows power supply in France. We can notice significant increase of nuclear energy. This is because the mature nuclear technology in France has greatly lowered the price of nuclear electricity. Thermal power, although increases slightly, will have decreasing proportion in overall electricity generation. Hydroelectricity, solar and wind energy hardly increase at all, since they are scarce in France. That’s why nuclear power will remain dominant in France.

<!-- b000175 | prose | pages [13] -->
The middle figure shows the power supply in USA. The electricity prices are similar among different types. Thus natural limitation will mainly determine the distribution among different types of energy generation. As the capacity of nuclear power is big, nuclear power will start from a small proportion in 2005 and end up with the highest in 2055. Solar energy, wind energy and hydroelectricity are all abundant in USA, so the distribution of these three energies is relatively even.

<!-- b000176 | prose | pages [13, 14] -->
12 Thermal power will be controlled under 10% of total electricity generation.

<!-- b000177 | furniture | pages [14] -->
Team #8882

<!-- b000178 | furniture | pages [14] -->
Page 13of 27

<!-- b000180 | prose | pages [14] -->
The right figure shows the power supply in China. As hydroelectricity is relatively cheap and abundant in China, it will ultimately become the most popular energy generation type. Thermal power is also cheap. However, government is going control its weight under 10% of total electricity generation to fulfill its environmental responsibility. That’s why thermal power will rise in the first 30 years and then stop at a certain percentage of total power. Nuclear power is slightly more expensive than thermal power, but due to the fact that it will not be stifled, it will become the second largest energy in China. Though solar and wind energy also abound in China compared with France, their higher price determine their low proportion.

<!-- b000181 | prose | pages [14] -->
Then we need to take one step further to find out how many more power plants will be constructed to provide power exclusively for EV and HEV. As the generated output varies greatly among different types of power plants, and even among the same type of power plant with different scales of construction, there is no easy way to calculate how many power plants of each type are needed. Thus, we will not specify different types of power plants and assume that each plant will generate 10,000,000kwh annually on average. The number of power stations can be calculated in (10).

<!-- b000182 | prose | pages [14] -->
C t ( ) = n t ( ) (10) 1 E 0

<!-- b000183 | prose | pages [14] -->
Where C(t) has been defined in (7), E0 is the generated output per general power station and n1(t) is the number of power stations needed to exist in each year.

<!-- b000184 | prose | pages [14] -->
Since five years could be a normal circle to build a typical power station, we will show how many new power plants will be established within a 5 years circle in France, USA and China. The result is shown in Figure 13.

<!-- b000185 | caption | pages [14] -->
Figure 13. New power stations needed to be constructed in a five-year circle in France, USA and

<!-- b000186 | prose | pages [14] -->
China

<!-- b000187 | prose | pages [14] -->
In France and USA, more power stations are need in short term than that in long term. In China, thanks to the off-peak charging and low vehicles ownership, no power

<!-- b000188 | prose | pages [14, 15] -->
13 stations are need before 2010, then it will increase from zero to 1200 per year within 20 years. The small need for construction in short term is beneficial for a developing country. Thus government will be allowed with more time to prepare for the financing.

<!-- b000189 | furniture | pages [15] -->
Team #8882

<!-- b000190 | furniture | pages [15] -->
Page 14of 27

<!-- b000192 | heading | pages [15] -->
6. Environmental, Economic, Social and Health

<!-- b000193 | prose | pages [15] -->
Impacts of EV/HEV

<!-- b000194 | heading | pages [15] -->
6.1 EV/HEV Consumes Less Fossil Fuels

<!-- b000195 | prose | pages [15] -->
The discussion in previous chapter reveals the potential reliance upon fossil fuels of EV and HEV. In this chapter, we will model the impact of EV and HEV on total fossil fuel consumption. This will help us better evaluate whether EV and HEV would consume less fossil fuels. Such evaluation is of vital importance because it is widely questioned that EV and HEV might burn more fossil fuels. Since burning fossil fuels, whether oil or gas, to generate electricity will definitely release CO2, we will measure reliance upon fossil fuels by measuring CO2 emissions. In order to do this, we introduce CO2 intensity. CO2 intensity is the average amount of CO2 emitted per unit of electrical energy generated by all of the power production processes in a mix weighted.[6] Thus the emissions from EVs depend on their own energy consumption and on the CO2 intensity of the power generation mix from which the EV’s energy was obtained. The CO2 intensity varies considerably depending on the composition of the power generation mix. For instance, in countries like China where thermal power provides more than 75% of general electricity, EVs charging from the electric grid will be responsible for significantly more emissions than in a country like France that derives less than 10% of its power from fossil fuels [7]. The situation is similar in electric-only mode of HEV. For CV, its emission can be tested directly from the tailpipe. Thus we calculate the CO2 emission in (11)

<!-- b000196 | prose | pages [15] -->
= + + ⎧ S t ( ) S ( ) t S ( ) t S ( ) t CV EV HEV ⎪ = ⋅ ⋅ S ( ) t L v z ⎪ CV 1 1 1 ⎪ = ⋅ ⋅ S ( ) t L v z EV 2 2 2 ⎪ = ⋅ ⋅ ⎨ (11) S ( ) t L v z HEV 3 3 3 ⎪ = ⋅ v I E ⎪ 2 2 2 ⎪ ⋅ + ⋅ ⋅ ' a v b I E = ⎪ v 3 3 3 3 + ⎩ a b

<!-- b000197 | prose | pages [15] -->
Where S t ( ) is the carbon dioxide emissions in the t year, iL (km) is the

<!-- b000198 | prose | pages [15] -->
distance traveled by i type of vehicle in t year, iv (gCO2/Km) is the emissions of

<!-- b000199 | prose | pages [15, 16] -->
14 carbon dioxide per kilometer by i vehicle, iz is the number of i vehicle, I is

<!-- b000200 | furniture | pages [16] -->
Team #8882

<!-- b000201 | furniture | pages [16] -->
Page 15of 27

<!-- b000203 | prose | pages [16] -->
CO2 intensity, E (kj/km) indicates energy in terms of joule required to propel vehicle for unit distance, and represents the oil-only mode and electric-only a b

<!-- b000204 | prose | pages [16] -->
proportion of HEV respectively. From previous chapters we know 1v is

<!-- b000205 | prose | pages [16] -->
11, 'v 3 E 155gCO2/km, E is 450kj/km is—108gCO2/km, —770kj/km, a is 50km 2 3

<!-- b000206 | prose | pages [16] -->
and b is 420km.

<!-- b000207 | prose | pages [16] -->
iI , the CO2 intensity, varies among countries. It depends on how much electricity

<!-- b000208 | prose | pages [16] -->
is generated from fossil fuel combustion, as well as how much CO2 is emitted while burning fossil fuel in order to generate unit electricity. We collect information of France, USA and China as list them in Table 8.

<!-- b000209 | caption | pages [16] -->
Table 8. Information related with CO2 intensity

<!-- b000210 | prose | pages [16] -->
France USA China 10% 67% 75% Proportion of electricity generated by fossil fuel How much CO2 is emitted to make 1jk by burning fossil fuels 0.0833 0.0833 0.0833 (gCO2/kj)?

<!-- b000211 | prose | pages [16] -->
0.00833 0.055811 0.062475 CO2 intensity(gCO2/kj)

<!-- b000212 | prose | pages [16] -->
Then we can figure out how much CO2 EV and HEV will release by running one kilometer. We list such figure in Table 9. In this table, we will also show the gCO2/km of CV to compare their fossil fuel consumption.

<!-- b000213 | caption | pages [16] -->
Table 9. CO2 consumption of CV, EV and HEV in France, USA and China

<!-- b000214 | prose | pages [16] -->
France USA China CV(gCO2/km) 155 155 155 3.75 25.125 28.125 EV(gCO2/km) HEV(gCO2/km) 138.116 140.49 140.825

<!-- b000215 | prose | pages [16] -->
This figure finally reveals the widely asked question that whether EV will save fossil fuel. And the answer is yes! In France, as its thermal power only takes up 10% of its general electricity generation, its electricity contributes far less CO2 emissions and fossil fuels consumption. Thus driving EV in France merely generates 3.75gCO2 per km compared to 155gCO2 of CV. Even in USA and China, where a major part of electricity is made from fossil fuels, and where electricity contain more fossil fuel energy, driving EV could also achieve 25.125gCO2/km and 28.125gCO2/km respectively, contributing a great save on fossil fuels. This might be the result of high energy conversion efficiency of electric motor. Thus, we believe EV would help saving fossil fuel around the world. As for HEV, the gCO2/km figure is only lightly

<!-- b000216 | prose | pages [16] -->
11 www.teslamotors.com

<!-- b000217 | prose | pages [16, 17] -->
15 lower than that of CV. This is resulted from the low ratio of electric-only distance to oil-only distance which is merely 1:8. However, electric-only mode is mainly used in starting and low speed, when the use of combustion engine only achieves a very low efficiency. Moreover, with the development of technology, the battery will be endowed with stronger capacity which will lift the electric-only distance. Hence in the future the HEV will also become a conscientious fossil fuel saver.

<!-- b000218 | furniture | pages [17] -->
Team #8882

<!-- b000219 | furniture | pages [17] -->
Page 16of 27

<!-- b000221 | prose | pages [17] -->
Then we are anxious to know the fossil fuel consumption when EV and HEV are gradually replacing CV. We run the model in matlab and show the result in Figure 14, 15 and 16.

<!-- b000222 | caption | pages [17] -->
Figure 14. CO2 emission in France

<!-- b000223 | caption | pages [17] -->
Figure 15. CO2 emission in USA

<!-- b000224 | caption | pages [17] -->
Figure 16. CO2 emission in China

<!-- b000225 | prose | pages [17] -->
As we can see, the carbon emission cause by vehicles in France is initially about 1/3 of USA and 1/10 of China. Its CO2 containment in electricity is also lower than USA and China. With the decline in the number of CV and rise in the number of EV and HEV, the carbon emission will go down from the very beginning, indicating the decline in the consumption of fossil fuels. So introduction of EV/HEV is very successful in saving fossil fuels. In USA, the number of CV will also decline; the number EV and HEV will rise. Yet its CO2 containment in electricity is 6.7 times of France. Consequently, the CO2 emission will rise slightly in the next five years, and then the emission will head down. In China, the CO2 containment in electricity is even higher. The number of CV will increase till 2035 and then go down. The number of EV and HEV will also increase. Therefore, the carbon emission will increase till 2040 and then drop. It is likely that the increase of CV before 2035 and high CO2 containment in electricity result in the increase of carbon emission before 2040. After 2040, the carbon emission begins to fall rapidly while the number of EV and HEV is still increasing. Therefore, we conclude that the massive use of EV and HEV will reduce the reliance upon fossil fuels effectively. And it is worthy in environmental concerns to promote EV and HEV.

<!-- b000226 | prose | pages [17] -->
Then we will examine how much oil will be saved. Given the total number of vehicles each year from 2005 to 2055 in France, USA and China, we could calculate

<!-- b000227 | prose | pages [17, 18] -->
16 the consumption of oil if all of the vehicles are CV. This will simulate the scenario that EV/HEV doesn’t contribute to consumption of fossil fuels at all. Given the number of CV, EV and HEV from 2005 to 2055 in these three countries, we can calculate the consumption of oil under the situation where EV/HEV is replacing CV according to our estimation. By comparing oil consumption with and without EV/HEV, we could see if and how much EV/HEV will save oil. Following such analysis, we have the following model.

<!-- b000228 | furniture | pages [18] -->
Team #8882

<!-- b000229 | furniture | pages [18] -->
Page 17of 27

<!-- b000231 | prose | pages [18] -->
∑ ∑ = ⋅ − ⋅ Q t ( ) C z t ( ) C z t ( ) (12) cv i i i i i

<!-- b000232 | prose | pages [18] -->
Where Q t ( ) is the quantity of oil one specific country can save by widely using

<!-- b000233 | prose | pages [18] -->
electrical vehicles, C is the average consumption of oil per i vehicle in the t i

<!-- b000234 | prose | pages [18] -->
year, iz t ( ) is the quantity of i vehicle in the t year.

<!-- b000235 | prose | pages [18] -->
The result is shown in Figure 17.

<!-- b000236 | caption | pages [18] -->
Figure 17. Oil saved by EV/HEV in France, USA and China

<!-- b000237 | prose | pages [18] -->
According to the Q t ( ) of the China, USA, and France, we can calculate the

<!-- b000238 | prose | pages [18] -->
quantity of oil the world can save by widely using electrical vehicles based on bound weight coefficients.

<!-- b000239 | prose | pages [18] -->
= ⋅ + ⋅ + ⋅ Total t ( ) r Q r Q r Q (13) 1 China 2 USA 3 Frace

<!-- b000240 | prose | pages [18] -->
Where ir is the weight coefficient of each country, Q t ( ) is the quantity of oil i

<!-- b000241 | prose | pages [18] -->
each country can save, Total t ( ) is the quantity of oil the world can save by widely

<!-- b000242 | prose | pages [18] -->
using electrical vehicles.

<!-- b000243 | prose | pages [18, 19] -->
17 r1 r2 r3

<!-- b000244 | furniture | pages [19] -->
Team #8882

<!-- b000245 | furniture | pages [19] -->
Page 18of 27

<!-- b000247 | prose | pages [19] -->
2．6462 2.4333 12.1333

<!-- b000248 | prose | pages [19] -->
Then we figure out the total oil saved in the world, as is shown in Figure 18

<!-- b000249 | caption | pages [19] -->
Figure 18. Oil saved in the world

<!-- b000250 | prose | pages [19] -->
As we can see, if all EV/HEV are replaced by CV, the oil consumption will skyrocket. It means that introduction of EV/HEV will save a significant amount of oil. The oil saved just in 2055 will be 2.5 billion L.

<!-- b000251 | heading | pages [19] -->
6.2 Driving EV and HEV Costs Less

<!-- b000252 | prose | pages [19] -->
EVs and HEVs will save fossil fuels, which is desirable in the eyes of environmentalist. However, to be environmentally friendly cannot always guarantee public popularity. Its promotion among societies and governments depends upon the economic and social benefits. In this and following two chapters, we are going to examine the feasibility to promote EV hand HEV among common families and governments, with economic and social incentives, not by regulations.

<!-- b000253 | prose | pages [19] -->
One huge benefit of electric vehicles is their low fuel costs as compared to gasoline vehicles. Let’s work out the driving cost of CV, EV and HEV and compare them together.  The average consumption of oil by CV worldwide is 8L/100Km. The average electricity consumption of EV and HEV is 20Kwh/100Km. The current oil price in France, USA and China is 1.38€/L, 58.17$/barrel and 7RMB/L. The current electricity price in France, USA and China is 0.12€/kwh, 6$/kwh and 56RMB/100kwh. As vehicle will run 10,000Km on average in each year worldwide.

<!-- b000254 | prose | pages [19, 20] -->
18 Further more, because there are no moving parts in an electric motor (as opposed to many in an internal combustion engine), there are many fewer things that can go wrong with an electric car, which means they'll probably save considerable money on maintenance costs as well. Electric vehicles have roughly 90% fewer parts than gasoline-powered vehicles. On RepairTrust.com, the maintenance costs for a typical car is $272.03 per 30,000 miles.12 That is $56.6 a year on average. A rough estimate is that number of parts in vehicle is in linear correlation with maintenance fee. So driving EV will save another $51 a year.

<!-- b000255 | furniture | pages [20] -->
Team #8882

<!-- b000256 | furniture | pages [20] -->
Page 19of 27

<!-- b000258 | prose | pages [20] -->
Now we can figure out the driving cost of EV, HEV and CV, as shown in Table 10. Note that 1/9 of the distance of HEV will be covered under electric-only mode.

<!-- b000259 | caption | pages [20] -->
Table 10. Cost and Saving of driving CV, EV and HEV

<!-- b000260 | prose | pages [20] -->
France USA China 14.9 6.3 8.61 Cost of driving CV(also driving HEV on oil-mode)( $/100Km) Cost of driving EV(also driving HEV on electric-mode)( $/100Km) 3.25 1.2 1.72 1165 510 689 Cost saved in one year by driving with electricity per vehicle($)

<!-- b000261 | heading | pages [20] -->
6.3 New Vehicle Industry Provides More Job Opportunities

<!-- b000262 | prose | pages [20] -->
Automobile-related business will provide considerable jobs for the society. The potential new business may consist of the jobs in electrical power station, electrical charging station, and automobile manufacture industry. Therefore, we establish the following formula to predict the total quantity of jobs related with automobile.

<!-- b000263 | prose | pages [20] -->
∑ = ⋅ + ⋅ + ⋅ H t h n t h n t g z t ( ) ( ) ( ) ( ) (14) 1 1 2 2 i i i

<!-- b000264 | prose | pages [20] -->
Where 1h is the average quantity of jobs provided by per electrical power station,

<!-- b000265 | prose | pages [20] -->
1n is the quantity of electrical power station in the t year, 2h is the average quantity

<!-- b000266 | prose | pages [20] -->
of jobs provided by per electrical charging station, 2n is the quantity of electrical

<!-- b000267 | prose | pages [20] -->
charging station in the t year, ig is the average quantity of jobs provided by per i

<!-- b000268 | prose | pages [20] -->
vehicle, iz is the quantity of i vehicle in the t year, H t ( ) is the total quantity of

<!-- b000269 | prose | pages [20] -->
jobs.

<!-- b000270 | prose | pages [20] -->
The number of power stations—N1(t)—has been calculated in the chapter 5.3 “Extra Energy Supply for EV/HEV and Its Optimization”. The number of charging

<!-- b000271 | prose | pages [20] -->
12 http://www.repairtrust.com/car_maintenance_costs.html

<!-- b000272 | prose | pages [20, 21] -->
19 station is limited by their task to supply electricity and provide services. Then we can use the following formula to calculate the quantity of charging stations.

<!-- b000273 | furniture | pages [21] -->
Team #8882

<!-- b000274 | furniture | pages [21] -->
Page 20of 27

<!-- b000276 | prose | pages [21] -->
1 ⋅ + z ( ) t z ( ) t HEV EV 9 = n t ( ) (15) 2 n 0

<!-- b000277 | prose | pages [21] -->
Where 0n is the average quantity of vehicles that one electrical charging station

<!-- b000278 | prose | pages [21] -->
can support for and n t 2( ) is the number of charging stations in t year.

<!-- b000279 | prose | pages [21] -->
We collect the values of coefficients in this model (some of them are estimated because they are not available on internet) and show them in Table 11.

<!-- b000280 | caption | pages [21] -->
Table 11. Coefficients

<!-- b000281 | prose | pages [21] -->
h1 h2 g1 E0 n0

<!-- b000282 | prose | pages [21] -->
7 5 10 10 China 400 5 1/20

<!-- b000283 | prose | pages [21] -->
7 5 200 5 1/20 10 10 USA

<!-- b000284 | prose | pages [21] -->
7 5 10 10 France 400 5 1/20

<!-- b000285 | prose | pages [21] -->
Now we can figure out the newly created jobs by EV and HEV industry in France, USA and France in each year. They are shown in Figure 19.

<!-- b000286 | caption | pages [21] -->
Figure 19. New job positions provided by new industries in France, USA and China.

<!-- b000287 | prose | pages [21] -->
More jobs mean less unemployed people and enhance in family income. It could even affect social stability. That’s why it is a major concern of politicians and economists. In all three countries, the number of jobs that new energy industry would hold in 2060 would account approximately for 10% of their current population. Nevertheless, power stations are expensive to build. So later we will take the effect of new jobs into consideration and see whether the investment in massive construction of power plants is economically worthy.

<!-- b000288 | prose | pages [21, 22] -->
20 6.4 Invest in New Vehicle Industry is Rewarding

<!-- b000289 | furniture | pages [22] -->
Team #8882

<!-- b000290 | furniture | pages [22] -->
Page 21of 27

<!-- b000292 | prose | pages [22] -->
Currently big vehicle manufactures are increasing their investment in EV cars. For example, Japanese automaker Nissan plans to invest $642 million into expanding its plant in Sunderland, UK to produce the upcoming LEAF electric sedan as well as lithium-ion batteries for vehicles from Nissan and alliance partner Renault. Ford Motor said its European division will invest $2.3 billion in the development of green car technology, grouped under the company's Econetic brand, over the next five years.13 This reflects the promising future of EV technology. For government that also seeks good-looking economic performance, EV industry will be rewarding other than environmentally beneficial.

<!-- b000293 | prose | pages [22] -->
The previous chapters have shown the economic rewards from EV industry—more jobs and less driving cost for individuals. Now we would consider the input into EV industry. That is to say, what we pay to get the rewards.

<!-- b000294 | prose | pages [22] -->
First of all, when off-peak charging will not suffice the rising number of EV and HEV, new power plants will be established. Second, when EV and HEV prevail in street, facilities like charging station will become a public welfare, just like street phone booth (Although we pay for the phone call, the phone booth is constructed by government). Thus government should also pay for the construction fee for charging stations. Third, as an environmental friendly industry, EV and HEV deserve financial subsidies from government especially in the early stage of its development when costs are relatively high. We consider these three aspects as government responsibilities.

<!-- b000295 | prose | pages [22] -->
Therefore, we establish government investment model shown as follows:

<!-- b000296 | prose | pages [22] -->
∑ = ⋅ + ⋅ + ⋅ cap t ( ) p n t ( ) p n t ( ) s z t ( ) (16) 1 1 2 2 i i i

<!-- b000297 | prose | pages [22] -->
Where 1p is the average cost of per electrical power station, 1n is the quantity

<!-- b000298 | prose | pages [22] -->
of electrical power station in the t year, 2p is the average cost of per electrical

<!-- b000299 | prose | pages [22] -->
charging station, 2n is the quantity of electrical charging station in the t year, is

<!-- b000300 | prose | pages [22] -->
is the subsidies provided for per i vehicle, iz is the quantity of i vehicle in the

<!-- b000301 | prose | pages [22] -->
t year, cap ( )t is the subsidies provided by the government in the t year.

<!-- b000302 | prose | pages [22] -->
We obtain the data needed in this model and list them in Table 12.

<!-- b000303 | prose | pages [22] -->
13 http://www.greenmomentum.com/wb3/wb/gm/gm_content?id_content=5348

<!-- b000304 | prose | pages [22, 23] -->
21 Cost per power Cost of charging Subsidy on each Salary per station station EV/HEV year 0.167×108€ 1.67×105€ €9000 €2,4770 France 1.5×108$ 10×105$ $10000 $37,610 USA 10×108RMB 10×106RMB 80000 RMB $1100 China

<!-- b000305 | furniture | pages [23] -->
Team #8882

<!-- b000306 | furniture | pages [23] -->
Page 22of 27

<!-- b000307 | caption | pages [23] -->
Table 12. Data needed for (16)

<!-- b000309 | prose | pages [23] -->
The result of government investment in each year is shown in Figure 20.

<!-- b000310 | caption | pages [23] -->
Figure 20. Investment for EV/HEV in France, USA and China

<!-- b000311 | prose | pages [23] -->
With the investment known, we will compare it with the outcome. That is, the benefits of more jobs and lower driving cost. As the investment has been measured in terms of money, we would also measure such benefits in the same way. The economic benefits of EV/HEV consist of two major aspects. The first one is extra job opportunities created by more power stations and charging stations. We will measure this effect by calculating the total salary provided by these jobs. The second one is savings of each EV or HEV that has been discussed in chapter 7.1 “Driving EV and HEV Costs Less”. We know driving electrically will annually save 1156, 510 and 689 dollars in France, USA and China respectively. We have also predicted the number of EV and HEV in these countries. Thus the totally saving from driving EV/HEV could be figured out.

<!-- b000312 | prose | pages [23] -->
∑ = ⋅ + Δ ⋅ Output t ( ) w H t ( ) p z t ( ) (17) i i i

<!-- b000313 | prose | pages [23] -->
Δ Where R t is the input-output ratio, ( ) w is the average wage per job, ip is

<!-- b000314 | prose | pages [23] -->
the saving of driving per vehicle, cap t ( ) is the subsidies provided by the government

<!-- b000315 | prose | pages [23] -->
in the t year, H t ( ) is the total quantity of jobs.

<!-- b000316 | prose | pages [23] -->
The average salary in France, USA and China is €2,4770, $37,610 and $1100. Then the outcome is shown in Figure 21.

<!-- b000317 | prose | pages [23, 24] -->
22 If we compare Figure 21 and Figure 20, we could be find out the output exceeds the input greatly. Thus, it is rewarding to invest in industries related to EV/HEV.

<!-- b000318 | furniture | pages [24] -->
Team #8882

<!-- b000319 | furniture | pages [24] -->
Page 23of 27

<!-- b000320 | caption | pages [24] -->
Figure 21. Monetary output of new industries in France, USA and China

<!-- b000322 | heading | pages [24] -->
6.5 EV/HEV Reduce Pollutions and Do Good for Health

<!-- b000323 | prose | pages [24] -->
Driving a car (CV) is the most air polluting act an average citizen commits.14 The exhaust from CV will poison the air we breath, help spread disease from airborne pathogens and particles. The CO2 emission will also change interactions between the atmosphere and sun, weather effects, effects on plants and oceans. Here we only consider the short term effects of introducing EV and HEV. We select several indicators of human health. Then simulate how they will change with EV and without EV. By comparison the effect of EV could be revealed.

<!-- b000324 | prose | pages [24] -->
Nitrogen is a major component of exhaust and known to cause several health effects:15 z Reactions with hemoglobin in blood, causing the oxygen carrying capacity of the blood to decrease (nitrite) z Decreased functioning of the thyroid gland (nitrate) z Vitamin A shortages (nitrate) z Fashioning of nitro amines, which are known as one of the most common causes of cancer (nitrates and nitrites)

<!-- b000325 | prose | pages [24] -->
Nitrogen is created during combustion. In CV the combustion engine will create nitrogen by burning oil. In thermal power plant, nitrogen will also be created by burning oil. As there is a fixed ratio of CO2 and nitrogen in oil combustion, we could estimate nitrogen the emission of nitrogen easily. The ratio of nitrogen to CO2 generated in oil combustion is 0.685.16 Thus, the nitrogen generation is shown in

<!-- b000326 | caption | pages [24] -->
Figure 22.

<!-- b000327 | prose | pages [24] -->
14 http://www.nutramed.com/environment/cars.htm 15 http://www.lenntech.com/periodic/elements/n.htm 16 http://www.engineeringtoolbox.com/co2-emission-fuels-d_1085.html

<!-- b000328 | prose | pages [24] -->
23

<!-- b000329 | furniture | pages [25] -->
Team #8882

<!-- b000330 | furniture | pages [25] -->
Page 24of 27

<!-- b000331 | caption | pages [25] -->
Figure 22. Nitrogen Generation in France, USA and China

<!-- b000332 | heading | pages [25] -->
7. Conclusion

<!-- b000333 | prose | pages [25] -->
The effects of EV/HEV could be clearly revealed by comparing environmental, social, economic and health impacts between two scenarios. One scenario is where quantities of CV, EV and HEV accord with our simulation. The other one is where all EV/HEV will be replaced by CV. In order to help decision for the whole world, we synthesize the figure in France, USA and China. Results are shown in Figure 23, 24, 25, 26.

<!-- b000334 | caption | pages [25] -->
Figure 23 World’s CO2 emission

<!-- b000335 | caption | pages [25] -->
Figure 24 World’s new job positions

<!-- b000336 | prose | pages [25, 26] -->
24 As we can see from Figure 23, the world with EV/HEV will have less carbon emissions than CV, thus consume less fossil fuel consumption. EV/HEV will also help create more jobs and greater fortune than CV will. In addition, air pollutions will be greatly lowed.

<!-- b000337 | furniture | pages [26] -->
Team #8882

<!-- b000338 | furniture | pages [26] -->
Page 25of 27

<!-- b000339 | caption | pages [26] -->
Figure 25 World’s monetary reward

<!-- b000340 | caption | pages [26] -->
Figure 26 World’s nitrogen production

<!-- b000342 | prose | pages [26] -->
“How environmentally and economically sound are electric vehicles?” The answer is very. The indirect consumption of fossil fuels by an EV (or HEV in electric-only mode) is 2.42% of CV in China, 16.2% of CV in USA and 18.1% of that in China. The widespread use of EV/HEV in France and USA will cause immediate drop of fossil fuels consumption. In China, such consumption drop will happen after 2040. Consequently, a significant among of fossil fuels will be saved. What’s more, driving EV/HEV cost little as compared to driving CV in all countries. And there is no big different of driving performance and price between CV and EV. This will attract individuals and facilitate its promotion among public. The market promotion on big scale would be promising.

<!-- b000343 | prose | pages [26] -->
The widespread use of EV/HEV would also be attractive for government. New power industry and EV manufactures would be needed, which would provide more job positions. Our model shows the monetary reward will greatly exceed the investment. In addition, we also model the impact of EV/HEV on air pollutions. Model shows encouraging results in reduction of nitrogen generation that pose a threat to human health. Therefore, if we put together the economic profits in the new industry, the government’s responsibility to conserve fossil fuel energy and protect human health, we think government will strongly support the widespread use of EV/HEV.

<!-- b000344 | prose | pages [26] -->
25

<!-- b000345 | furniture | pages [27] -->
Team #8882

<!-- b000346 | furniture | pages [27] -->
Page 26of 27

<!-- b000347 | heading | pages [27] -->
8. References

<!-- b000348 | references | pages [27] -->
[1] T.J. Wallington, E.W. Kaiser and J.T. Farrell, Automotive fuels and internal

<!-- b000349 | references | pages [27] -->
combustion engines: a chemical perspective, Chem Soc Rev 35 (2005), pp. 335–347.

<!-- b000350 | references | pages [27] -->
[2] Electric Vehicle charge forward by C.C Chan and Y.S. Wong

<!-- b000351 | references | pages [27] -->
[3] http://www.fueleconomy.gov/feg/evtech.shtml

<!-- b000352 | references | pages [27] -->
[4] http://www.carboncounted.co.uk/when-will-fossil-fuels-run-out.html

<!-- b000353 | references | pages [27] -->
[5] Proc. Int. Conf. Urban Electric Vehicle, Stockholm, Sweden, May 1992, OECD,

<!-- b000354 | references | pages [27] -->
IEA, Paris, France.

<!-- b000355 | references | pages [27] -->
[6] Reed T. Doucette ⇑, Malcolm D. McCulloch Modeling the prospects of plug-in

<!-- b000356 | references | pages [27] -->
hybrid electric vehicles to reduce CO2 emissions

<!-- b000357 | references | pages [27] -->
[7] Carfolio. 2010 Ford focus specifications; 2010. <www.carfolio.com> [accessed

<!-- b000358 | references | pages [27] -->
August 2010]

<!-- b000359 | references | pages [27] -->
[8] Universal Charging Station and Method for Charging Electrical Vehicle Batteries

<!-- b000360 | references | pages [27] -->
By Bradley J.Hesse.Syacuse; Philip J.Gentile, East Syracuse, both of N.Y

<!-- b000361 | references | pages [27] -->
[9] Hybrid Electric Vehicle by Alex J.Severinsky, 10904 Pebble Run, Silver Spring,

<!-- b000362 | references | pages [27] -->
Md.20902

<!-- b000363 | references | pages [27] -->
26
