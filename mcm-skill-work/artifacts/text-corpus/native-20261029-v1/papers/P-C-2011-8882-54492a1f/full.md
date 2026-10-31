# P-C-2011-8882-54492a1f

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #8882

<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
Page 1of 27

<!-- b000004 | heading | pages [1] -->
CONTENTS

<!-- b000005 | contents | pages [1] -->
1. Introduction...........................................................................................................................1

<!-- b000006 | contents | pages [1] -->
2. Assumptions..........................................................................................................................2

<!-- b000007 | contents | pages [1] -->
3. A Brief View of CV, EV and HEV........................................................................................2

<!-- b000008 | contents | pages [1] -->
4. Simulation of Quantities of CV, EV and HEV......................................................................3

<!-- b000009 | contents | pages [1] -->
4.1 Increase of Number of Total Vehicles .........................................................................3

<!-- b000010 | contents | pages [1] -->
4.2 Growth of Quantities of CV, EV and HEV .................................................................5

<!-- b000011 | contents | pages [1] -->
5. Energy Demand and Supply from/for EV and HEV.............................................................7

<!-- b000012 | contents | pages [1] -->
5.1 Electricity Demand from EV/HEV .............................................................................8

<!-- b000013 | contents | pages [1] -->
5.2 Off-Peak Charging Supply for EV and HEV ..............................................................8

<!-- b000014 | contents | pages [1] -->
5.3 Extra Energy Supply for EV/HEV and Its Optimization ..........................................10

<!-- b000015 | contents | pages [1] -->
6. Environmental, Economic, Social and Health Impacts of EV/HEV...................................14

<!-- b000016 | contents | pages [1] -->
6.1 EV/HEV Consumes Less Fossil Fuels......................................................................14

<!-- b000017 | contents | pages [1] -->
6.2 Driving EV and HEV Costs Less..............................................................................18

<!-- b000018 | contents | pages [1] -->
6.3 New Vehicle Industry Provides More Job Opportunities..........................................19

<!-- b000019 | contents | pages [1] -->
6.4 Invest in New Vehicle Industry is Rewarding...........................................................21

<!-- b000020 | contents | pages [1] -->
6.5 EV/HEV Reduce Pollutions and Do Good for Health ..............................................23

<!-- b000021 | contents | pages [1] -->
7. Conclusion ..........................................................................................................................24

<!-- b000022 | contents | pages [1] -->
8. References...........................................................................................................................26

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [2] -->
Team #8882

<!-- b000029 | heading | pages [2] -->
1. Introduction

<!-- b000030 | furniture | pages [2] -->


<!-- b000031 | furniture | pages [2] -->


<!-- b000032 | furniture | pages [2] -->
Page 1of 27

<!-- b000033 | prose | pages [2] -->
Today we have 800 million vehicles in the world with roughly 70 million new

<!-- b000034 | furniture | pages [2] -->


<!-- b000035 | prose | pages [2] -->
ones built each year. By current vehicle growth rate, we will end up with 3 billion cars on the planet by 2035.1 The majority of vehicles on the road in 2010 are conventional vehicles (CV) based on ICEs. [1] Considering the average amount of petroleum each vehicle takes annually, it will need several times the volume of oil reserves currently known in Saudi Arabia just to fuel them2. How would we be able to power such huge number of vehicles? How to deal with the staggering emission from them? The gloomy answers to these questions compel us to strive for sustainable road transportation. It seems that electric vehicle (EV) could address this issue positively.[2] For detailed analysis, we classify vehicle into three kinds: conventional vehicle (CV), electric vehicle (EV) and hybrid-electric vehicle (HEV). [8]

<!-- b000036 | furniture | pages [2] -->


<!-- b000037 | prose | pages [2] -->
In this paper, we will model the environmental, economical, social and health impacts of EV/HEV within the next 50 years and in three typical areas—China, USA and France. The formation of our paper is shown in Figure 1.

<!-- b000038 | furniture | pages [2] -->


<!-- b000039 | caption | pages [2] -->
Figure 1. Formation of our paper

<!-- b000040 | furniture | pages [2] -->


<!-- b000041 | furniture | pages [2] -->


<!-- b000042 | prose | pages [2] -->
First of all, we will simulate the quantity of CV, EV and HEV in France, USA and

<!-- b000043 | furniture | pages [2] -->


<!-- b000044 | prose | pages [2] -->
China. Logistic model is introduced and historic data of vehicle quantities is collected to fit the coefficients of logistic model. At the same time, the role of government will take place to control and optimize the quantities of CV, EV and HEV, in order to achieve lower fossil fuel consumption.

<!-- b000045 | furniture | pages [2] -->


<!-- b000046 | prose | pages [2] -->
Next, we will respond to the demand for electrical energy from EV/HEV in these

<!-- b000047 | furniture | pages [2] -->


<!-- b000048 | prose | pages [2] -->
countries. Supply plans of amount and type of electricity generation will be designed by model that involves the following concerns. (1) During this process, the supply plan will be in conformity with domestic energy allowance. (2) Government should

<!-- b000049 | furniture | pages [2] -->


<!-- b000050 | prose | pages [2] -->
1 http://www.hybridcars.com/fuels/will-electric-cars-rule-future-25049.html 2 http://www.hybridcars.com/fuels/will-electric-cars-rule-future-25049.html

<!-- b000051 | furniture | pages [2] -->


<!-- b000052 | prose | pages [2] -->
1

<!-- b000053 | furniture | pages [3] -->
Team #8882

<!-- b000054 | furniture | pages [3] -->


<!-- b000055 | furniture | pages [3] -->
Page 2of 27

<!-- b000056 | prose | pages [3] -->
also take steps to reduce the reliance of electricity generation upon fossil fuels. (3) It is also desirable to strive for the lowest costs of the energy supply plan as much as possible.

<!-- b000057 | furniture | pages [3] -->


<!-- b000058 | furniture | pages [3] -->


<!-- b000059 | prose | pages [3] -->
Finally, we model the environmental, social, economic, and health impacts of the widespread use of EV/HEV. Environmental impact is mainly considered as the consumption of fossil fuels. Social impact is viewed from the savings of driving EV/HEV for individuals. Economic impact involves new job opportunities from EV/HEV and power industry. Health impact will be measured by the nitrogen generation. We compare all these figures under two different scenarios. One scenario is where quantities of CV, EV and HEV accord with our simulation. The other one is where all EVs/HEVs are replaced by CV. In other words, we will compare all these impacts between “mixed-vehicle world” and “pure-CV world”. Thus the impacts of EV/HEV will be clearly revealed.

<!-- b000060 | heading | pages [3] -->
2. Assumptions

<!-- b000061 | prose | pages [3] -->
1. We will select one vehicle mode to represent CV, EV and HEV each. 2. We assume there is no difference in performance of each vehicle type. 3. We select France, USA, and China to represent European countries, American countries and Asian countries. 4. We assume performance of CV, EV and HEV will not change in the future. 5. Based on common sense, we assume each vehicle travels 10,000 km every year. 6 We will not specify different types of power plants and assume that each plant will generate 10,000,000kwh annually on average. 7. We do not consider the dissipation during energy conversion.

<!-- b000062 | heading | pages [3] -->
3. A Brief View of CV, EV and HEV

<!-- b000063 | prose | pages [3] -->
Currently there are three types of vehicles. Conventional vehicle is driven by internal combustion engine. The majority of vehicles on the road in 2010 are conventional vehicles based on ICEs. Electric vehicles (EVs) are propelled by an electric motor (or motors) powered by rechargeable battery packs.[3] EV is also born with hybrid-electric vehicle (HEV) that could switch between electric-only mode and oil-only mode. [9] The advantages of electric power are apparent, as it could avoid tailpipe emission, enhance energy efficiency at low speed and utilize off-peak electricity; the disadvantages are equally obvious, considering a certain amount of electricity is ultimately generated by fossil fuels with pollutions released, the current battery capacity could not support high sustaining speed driving, and battery pollution is still a threat to our environment.

<!-- b000064 | furniture | pages [3] -->


<!-- b000065 | prose | pages [3] -->
In the following chapters, a lot of discussions, analyses and computation would require data related to features of CV, EV and HEV. As different vehicle modes have

<!-- b000066 | furniture | pages [3] -->


<!-- b000067 | prose | pages [3] -->
2

<!-- b000068 | furniture | pages [4] -->
Team #8882

<!-- b000069 | furniture | pages [4] -->


<!-- b000070 | furniture | pages [4] -->


<!-- b000071 | furniture | pages [4] -->
Page 3of 27

<!-- b000072 | prose | pages [4] -->
different characteristics, we would select typical modes to represent different types in vehicle family, as shown in Table 1.

<!-- b000073 | furniture | pages [4] -->


<!-- b000074 | caption | pages [4] -->
Table 1. Features of CV, EV and HEV

<!-- b000075 | furniture | pages [4] -->


<!-- b000076 | prose | pages [4] -->
Typical Mode

<!-- b000077 | prose | pages [4] -->
2010 Focus 1.4 Duratec CV

<!-- b000078 | prose | pages [4] -->
Features

<!-- b000079 | prose | pages [4] -->
Price: from £39,995 3 Produce 155gCO2/km 4

<!-- b000080 | furniture | pages [4] -->


<!-- b000081 | prose | pages [4] -->
Price: $108,000 Travel up to 220 miles without a recharge 5

<!-- b000082 | prose | pages [4] -->
Tesla Roadster EV

<!-- b000083 | prose | pages [4] -->
Consume 450kJ/km 6

<!-- b000084 | furniture | pages [4] -->


<!-- b000085 | prose | pages [4] -->
Price: $41000 7 Consumes 770kj/km in electric-only mode

<!-- b000086 | prose | pages [4] -->
Chevrolet Volt HEV

<!-- b000087 | prose | pages [4] -->
Produces 108gCO2/km in oil-only mode Run 50km without recharging and 420km without refueling

<!-- b000088 | heading | pages [4] -->
4. Simulation of Quantities of CV, EV and HEV

<!-- b000089 | heading | pages [4] -->
4.1 Increase of Number of Total Vehicles

<!-- b000090 | prose | pages [4] -->
The number of vehicles has increased more in the past decade than in the

<!-- b000091 | furniture | pages [4] -->


<!-- b000092 | prose | pages [4] -->
previous one century, and such trend will continue in the future. Although the alarm of fossil fuels has been around for years, the need for transportation is still expanding vehicle ownership, whether such need is met by driving CV, EV or HEV. Therefore, total vehicle quantity should be simulated first.

<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | prose | pages [4] -->
There are two major factors that influence the number of vehicles. The first one is population. Countries with larger population are more likely to have more vehicles, as the need for transportation is basically same for each common person. The second one is the geographic condition such as area of this region. Typically, larger area and good road condition are indicative of higher road capacity, and thus higher allowance for vehicles. If we put these two factors together, we are considering the density of population. In this sense, the growth of vehicle is comparable to the growth of biota with limited (sometimes fluctuated) natural resources where logistic mode is widely used to predict the growth of population. Thus, we seek similar approach to simulate the growth of vehicles with logistic mode as shown below.

<!-- b000095 | furniture | pages [4] -->


<!-- b000096 | prose | pages [4] -->
3 http://www.ciao.co.uk/Ford_Fiesta_LX_1_4_TDCi_5dr__Review_5711296

<!-- b000097 | prose | pages [4] -->
4 http://www.ford.co.uk/Cars/Focus/BrochurePricesSpecifications 5 http://www.leftlanenews.com/tesla-roadster.html# 6 www.teslamotors.com 7 http://www.cardekho.com/carmodels/Chevrolet/Chevrolet_Volt

<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | prose | pages [4] -->
3

<!-- b000100 | furniture | pages [5] -->
Team #8882

<!-- b000101 | prose | pages [5] -->
⎧

<!-- b000102 | prose | pages [5] -->
dx

<!-- b000103 | furniture | pages [5] -->


<!-- b000104 | furniture | pages [5] -->


<!-- b000105 | furniture | pages [5] -->
Page 4of 27

<!-- b000106 | prose | pages [5] -->
x

<!-- b000107 | prose | pages [5] -->
= ⋅⋅ ⎪⎨

<!-- b000108 | prose | pages [5] -->
dt

<!-- b000109 | prose | pages [5] -->
⎪

<!-- b000110 | prose | pages [5] -->
x

<!-- b000111 | prose | pages [5] -->
(0)

<!-- b000112 | prose | pages [5] -->
⎩ −

<!-- b000113 | prose | pages [5] -->
r x

<!-- b000114 | prose | pages [5] -->
(1 )

<!-- b000115 | prose | pages [5] -->
M

<!-- b000116 | furniture | pages [5] -->


<!-- b000117 | prose | pages [5] -->
(1)

<!-- b000118 | prose | pages [5] -->
= =

<!-- b000119 | prose | pages [5] -->
x

<!-- b000120 | prose | pages [5] -->
0

<!-- b000121 | prose | pages [5] -->
According to (1), we can deduct the expression for the total vehicle number in the t year:

<!-- b000122 | prose | pages [5] -->
=

<!-- b000123 | prose | pages [5] -->
( )

<!-- b000124 | prose | pages [5] -->
x t M

<!-- b000125 | prose | pages [5] -->
+

<!-- b000126 | prose | pages [5] -->
1 ( x

<!-- b000127 | prose | pages [5] -->
Where

<!-- b000128 | prose | pages [5] -->
M

<!-- b000129 | prose | pages [5] -->
(2)

<!-- b000130 | prose | pages [5] -->
−

<!-- b000131 | prose | pages [5] -->
− ⋅

<!-- b000132 | prose | pages [5] -->
rt 1) e

<!-- b000133 | prose | pages [5] -->
0 0

<!-- b000134 | furniture | pages [5] -->


<!-- b000135 | prose | pages [5] -->
year, r is intrinsic growth rate of x t is the total vehicle number in ( )

<!-- b000136 | prose | pages [5] -->
t

<!-- b000137 | prose | pages [5] -->
M is the ceiling of vehicle number and

<!-- b000138 | prose | pages [5] -->
vehicle number,

<!-- b000139 | prose | pages [5] -->
2010.

<!-- b000140 | furniture | pages [5] -->


<!-- b000141 | prose | pages [5] -->
0x is the vehicle number in

<!-- b000142 | prose | pages [5] -->
We adopt historic data and obtain the values of coefficients by fitting. As we will simulate situation in France, USA and China, we collect their quantities of total vehicles and list them in Table 2.

<!-- b000143 | furniture | pages [5] -->


<!-- b000144 | furniture | pages [5] -->


<!-- b000145 | caption | pages [5] -->
Table 2. Quantities of total vehicle in France, USA and China from 2005 to 2010

<!-- b000146 | prose | pages [5] -->
Vehicle Quantity\Year 2005

<!-- b000147 | prose | pages [5] -->
France(107) 3

<!-- b000148 | prose | pages [5] -->
USA(108) 2.4

<!-- b000149 | prose | pages [5] -->
China(108) 1

<!-- b000150 | furniture | pages [5] -->


<!-- b000151 | prose | pages [5] -->
2006 2007 2008 2009 2010

<!-- b000152 | prose | pages [5] -->
3.17 3.34 3.51 3.68 3.8

<!-- b000153 | prose | pages [5] -->
2.5 2.9 3.0 3.1 3.2

<!-- b000154 | prose | pages [5] -->
1.11 1.24 1.37 1.52 1.68

<!-- b000155 | prose | pages [5] -->
The result of fitting is shown in Table 3.

<!-- b000156 | prose | pages [5] -->
Tabel 3. Values of coefficients in logistic mode acquired by fitting

<!-- b000157 | furniture | pages [5] -->


<!-- b000158 | prose | pages [5] -->
France USA China

<!-- b000159 | prose | pages [5] -->
600,000,000 60,000,000 xm

<!-- b000160 | prose | pages [5] -->
0.115 r

<!-- b000161 | furniture | pages [5] -->


<!-- b000162 | prose | pages [5] -->
1,400,000,000

<!-- b000163 | prose | pages [5] -->
0.115 0.115

<!-- b000164 | prose | pages [5] -->
Given the values of coefficients, our model could simulate the growth of quantities of vehicles. The result is shown in Figure 2, 3 and 4.

<!-- b000165 | furniture | pages [5] -->


<!-- b000166 | prose | pages [5] -->
4

<!-- b000167 | furniture | pages [6] -->
Team #8882

<!-- b000168 | furniture | pages [6] -->


<!-- b000169 | furniture | pages [6] -->


<!-- b000170 | furniture | pages [6] -->
Page 5of 27

<!-- b000171 | furniture | pages [6] -->


<!-- b000172 | prose | pages [6] -->
Figure 3 Figure 2

<!-- b000173 | furniture | pages [6] -->


<!-- b000174 | furniture | pages [6] -->


<!-- b000175 | furniture | pages [6] -->


<!-- b000176 | furniture | pages [6] -->


<!-- b000177 | furniture | pages [6] -->


<!-- b000178 | furniture | pages [6] -->


<!-- b000179 | furniture | pages [6] -->


<!-- b000180 | furniture | pages [6] -->


<!-- b000181 | furniture | pages [6] -->


<!-- b000182 | furniture | pages [6] -->


<!-- b000183 | furniture | pages [6] -->


<!-- b000184 | furniture | pages [6] -->


<!-- b000185 | prose | pages [6] -->
Figure 4

<!-- b000186 | caption | pages [6] -->
Figure 2 shows the increase of vehicles in France, USA and China. In France, the

<!-- b000187 | furniture | pages [6] -->


<!-- b000188 | prose | pages [6] -->
number will keep rising and become stable after 2030. The ultimate number is 60,000,000. In USA, the quantity of total vehicles increase steadily from 2010 to 2030, and remain almost unchanged after 2030. The ultimate number of vehicles will be about 600,000,000. In china, the number of vehicles will increase rapidly from 2015, and such rapid growth period will not end until 2050. The ultimate number will be about 1,400,000,000.

<!-- b000189 | heading | pages [6] -->
4.2 Growth of Quantities of CV, EV and HEV

<!-- b000190 | prose | pages [6] -->
Once the total number of vehicle each year in the future is known, we are going to simulate the quantities of CV, EV and HEV. There are many factors that would influence the distribution. EV and HEV have strong potentials to reduce the reliance upon fossil fuels, as electricity could come from other sources other than thermal power. When fossil fuels run out, we could power EV one way or another. HEV is an eclectic solution that could be a good choice at this moment. Therefore, EA and HEV (especially EA) should gradually take the place of CV. It is ideal that all vehicles will be converted to EA when fossil fuels run out. But exactly when will that time come? No one can answer. There are many different opinions and calculations and none really agree on the exact timing. Many different factors need to be considered including how much of each deposit is left in the Earth, how fast we are using each fossil fuel at the moment, and how this is likely to change in the future. If we start switching to alternative fuel sources that are renewable rather than non-renewable, the reserves that we have will obvious last longer. [4] Therefore, it is impossible to predict the fossil fuel reserve in 50 years. It is also impossible to determine the limit that fossil fuel poses upon vehicle oil consumption.

<!-- b000191 | furniture | pages [6] -->


<!-- b000192 | prose | pages [6] -->
What we know for sure is that oil reserve will be running very low in 2055 according to current consumption and reserve. So we deem that government should reduce the oil consumption of vehicles by 90% of current consumption within 50 years. By achieving such goal, the reliance upon oil will be reduced and the impact of sudden drain of oil will be cushioned. Oil is consumed by CV and HEV during its

<!-- b000193 | furniture | pages [6] -->


<!-- b000194 | prose | pages [6] -->
5

<!-- b000195 | furniture | pages [7] -->
Team #8882

<!-- b000196 | furniture | pages [7] -->


<!-- b000197 | furniture | pages [7] -->


<!-- b000198 | furniture | pages [7] -->
Page 6of 27

<!-- b000199 | prose | pages [7] -->
oil-only mode that on average takes up 8/9 of this total travel distance8. We estimate the ratio of light vehicle to heavy one to be 3. As EVs are of smaller power, shorter range and HEV could provide bigger drive and longer range, EV would serve as light vehicle and HEV another. We speculate the ratio of EV to HEV in 2060 would also be 3. Thus we come up with the following equations.

<!-- b000200 | prose | pages [7] -->
⎧

<!-- b000201 | prose | pages [7] -->
8

<!-- b000202 | prose | pages [7] -->
⋅ + =

<!-- b000203 | prose | pages [7] -->
z t z t z

<!-- b000204 | prose | pages [7] -->
( ) ( ) [

<!-- b000205 | prose | pages [7] -->
⎪

<!-- b000206 | prose | pages [7] -->
HEV CV

<!-- b000207 | prose | pages [7] -->
9

<!-- b000208 | prose | pages [7] -->
⎪ =

<!-- b000209 | prose | pages [7] -->
( ) ( ) ( )

<!-- b000210 | prose | pages [7] -->
z t z t R t

<!-- b000211 | prose | pages [7] -->
⎨

<!-- b000212 | prose | pages [7] -->
EV HEV

<!-- b000213 | prose | pages [7] -->
⎪ + +

<!-- b000214 | prose | pages [7] -->
( ) ( ) ( )

<!-- b000215 | prose | pages [7] -->
z t z t z

<!-- b000216 | prose | pages [7] -->
⎪

<!-- b000217 | prose | pages [7] -->
CV EV HEV

<!-- b000218 | prose | pages [7] -->
⎩

<!-- b000219 | prose | pages [7] -->
z t

<!-- b000220 | prose | pages [7] -->
8

<!-- b000221 | prose | pages [7] -->
⋅ + ⋅ η

<!-- b000222 | prose | pages [7] -->
z t

<!-- b000223 | prose | pages [7] -->
(2010) (2010)] ( )

<!-- b000224 | prose | pages [7] -->
HEV CV

<!-- b000225 | prose | pages [7] -->
9

<!-- b000226 | furniture | pages [7] -->


<!-- b000227 | furniture | pages [7] -->


<!-- b000228 | prose | pages [7] -->
(3)

<!-- b000229 | prose | pages [7] -->
=

<!-- b000230 | prose | pages [7] -->
( )

<!-- b000231 | prose | pages [7] -->
t t x t

<!-- b000232 | prose | pages [7] -->
t z t

<!-- b000233 | prose | pages [7] -->
is the number of CV in Where

<!-- b000234 | prose | pages [7] -->
( ) CV

<!-- b000235 | prose | pages [7] -->
t

<!-- b000236 | prose | pages [7] -->
z t ( )

<!-- b000237 | prose | pages [7] -->
year,

<!-- b000238 | prose | pages [7] -->
( )

<!-- b000239 | prose | pages [7] -->
is the number of EV in

<!-- b000240 | prose | pages [7] -->
EV

<!-- b000241 | prose | pages [7] -->
x t is the total number of ( ) t

<!-- b000242 | prose | pages [7] -->
is the number of HEV in year,

<!-- b000243 | prose | pages [7] -->
HEV

<!-- b000244 | prose | pages [7] -->
year,

<!-- b000245 | prose | pages [7] -->
η R t is the ratio of EV to HEV, R(2055) is 3, t ( ) vehicles in the year, ( )t is

<!-- b000246 | prose | pages [7] -->
η t (2055) is 10%. coefficient that controls the reliance upon oil in

<!-- b000247 | furniture | pages [7] -->


<!-- b000248 | prose | pages [7] -->
year and

<!-- b000249 | prose | pages [7] -->
In Europe, EVs have been projected to reach 500 thousand by the year 1999. In Japan, the government's plan calls for 200 thousand EVs by the year 2000. Here in the US, air pollution regulations could translate into a production requirement of around 300--400 thousand EVs per year [5] Thus, we estimate the current EV/HEV number to be 5% of the total vehicle number in each country.

<!-- b000250 | furniture | pages [7] -->


<!-- b000251 | prose | pages [7] -->
Government will also play a role in controlling the distribution of CV, EV and

<!-- b000252 | furniture | pages [7] -->


<!-- b000253 | prose | pages [7] -->
HEV to strive for largest number of benefits to the environment, society, business, and individuals. Thus we have our optimization model (4) and (5).

<!-- b000254 | prose | pages [7] -->
∑ η + max E R ( , ) S R

<!-- b000255 | prose | pages [7] -->
⎧

<!-- b000256 | prose | pages [7] -->
η + η + η ( , ) B R ( , ) I R ( , )

<!-- b000257 | furniture | pages [7] -->


<!-- b000258 | furniture | pages [7] -->


<!-- b000259 | furniture | pages [7] -->


<!-- b000260 | prose | pages [7] -->
(4)

<!-- b000261 | prose | pages [7] -->
≤

<!-- b000262 | prose | pages [7] -->
η

<!-- b000263 | prose | pages [7] -->
E R

<!-- b000264 | prose | pages [7] -->
⎪

<!-- b000265 | prose | pages [7] -->
S R

<!-- b000266 | prose | pages [7] -->
⎪⎨

<!-- b000267 | prose | pages [7] -->
s t

<!-- b000268 | prose | pages [7] -->
. .

<!-- b000269 | prose | pages [7] -->
B R

<!-- b000270 | prose | pages [7] -->
⎪ ⎪

<!-- b000271 | prose | pages [7] -->
I R

<!-- b000272 | prose | pages [7] -->
⎩

<!-- b000273 | prose | pages [7] -->
O

<!-- b000274 | prose | pages [7] -->
( , )

<!-- b000275 | prose | pages [7] -->
≥

<!-- b000276 | prose | pages [7] -->
η

<!-- b000277 | prose | pages [7] -->
H

<!-- b000278 | prose | pages [7] -->
( , )

<!-- b000279 | furniture | pages [7] -->


<!-- b000280 | furniture | pages [7] -->


<!-- b000281 | furniture | pages [7] -->


<!-- b000282 | furniture | pages [7] -->


<!-- b000283 | furniture | pages [7] -->


<!-- b000284 | furniture | pages [7] -->


<!-- b000285 | furniture | pages [7] -->


<!-- b000286 | prose | pages [7] -->
(5)

<!-- b000287 | prose | pages [7] -->
≥

<!-- b000288 | prose | pages [7] -->
η

<!-- b000289 | prose | pages [7] -->
C

<!-- b000290 | prose | pages [7] -->
( , )

<!-- b000291 | prose | pages [7] -->
≥Δ

<!-- b000292 | prose | pages [7] -->
η

<!-- b000293 | prose | pages [7] -->
P

<!-- b000294 | prose | pages [7] -->
( , )

<!-- b000295 | furniture | pages [7] -->


<!-- b000296 | furniture | pages [7] -->


<!-- b000297 | prose | pages [7] -->
is the environmental factor, Where E factor, I is the individual factor, is the social factor, B is the business S

<!-- b000298 | prose | pages [7] -->
H

<!-- b000299 | prose | pages [7] -->
is the ceiling of the environmental factor,

<!-- b000300 | prose | pages [7] -->
O

<!-- b000301 | prose | pages [7] -->
is

<!-- b000302 | prose | pages [7] -->
Δ

<!-- b000303 | prose | pages [7] -->
is the lower limit of the business factor, the lower limit of the social factor,

<!-- b000304 | prose | pages [7] -->
C

<!-- b000305 | prose | pages [7] -->
is the lower limit of the individuals factor.

<!-- b000306 | furniture | pages [7] -->


<!-- b000307 | furniture | pages [7] -->


<!-- b000308 | prose | pages [7] -->
P

<!-- b000309 | prose | pages [7] -->
Thus we could simulate quantities of CV, EV and HEV in France, USA and China.

<!-- b000310 | furniture | pages [7] -->


<!-- b000311 | furniture | pages [7] -->


<!-- b000312 | prose | pages [7] -->
8 Vanderwerp D. 2011 Chevrolet volt full test – road test. Car and driver; 2010.

<!-- b000313 | furniture | pages [7] -->


<!-- b000314 | prose | pages [7] -->
6

<!-- b000315 | furniture | pages [8] -->
Team #8882

<!-- b000316 | prose | pages [8] -->
The result is shown in Figure 5, 6 and 7.

<!-- b000317 | furniture | pages [8] -->


<!-- b000318 | furniture | pages [8] -->


<!-- b000319 | furniture | pages [8] -->
Page 7of 27

<!-- b000320 | furniture | pages [8] -->


<!-- b000321 | caption | pages [8] -->
Figure 6.

<!-- b000322 | caption | pages [8] -->
Figure 5.

<!-- b000323 | furniture | pages [8] -->


<!-- b000324 | furniture | pages [8] -->


<!-- b000325 | furniture | pages [8] -->


<!-- b000326 | furniture | pages [8] -->


<!-- b000327 | furniture | pages [8] -->


<!-- b000328 | furniture | pages [8] -->


<!-- b000329 | furniture | pages [8] -->


<!-- b000330 | furniture | pages [8] -->


<!-- b000331 | furniture | pages [8] -->


<!-- b000332 | furniture | pages [8] -->


<!-- b000333 | furniture | pages [8] -->


<!-- b000334 | prose | pages [8] -->
Figure 7 Number of CV, EV and HEV in USA Number of CV, EV and HEV in France

<!-- b000335 | furniture | pages [8] -->


<!-- b000336 | furniture | pages [8] -->


<!-- b000337 | furniture | pages [8] -->


<!-- b000338 | prose | pages [8] -->
Number of CV, EV and HEV in China

<!-- b000339 | prose | pages [8] -->
R t ( ) The R(t) is decreasing in all three Figures, indicating the decline of oil consumption.

<!-- b000340 | furniture | pages [8] -->


<!-- b000341 | prose | pages [8] -->
is rising, so EV will dominate the vehicle world in the future.

<!-- b000342 | furniture | pages [8] -->


<!-- b000343 | caption | pages [8] -->
Figure 5 pictures the trend of vehicle quantities in France. As we can see, EV will

<!-- b000344 | prose | pages [8] -->
rise rapidly during the first 15 years from 0.4×107 to 4×107. It is due to less geographic limitation on traffic. CV would decrease from 2.5×107 to 0.54×107. Thus the reduction of CV is effective.

<!-- b000345 | furniture | pages [8] -->


<!-- b000346 | caption | pages [8] -->
Figure 6 depicts the trend of vehicle quantities in USA. The situation is similar to

<!-- b000347 | prose | pages [8] -->
that of France. CV will decrease from 1.9×108 to 0.65×108; EV will increase from 0.25×108 to 4×108; HEV will increase from 0.25×108 to 1.4×108.

<!-- b000348 | furniture | pages [8] -->


<!-- b000349 | caption | pages [8] -->
Figure 7 shows the trends of vehicle quantities in China. The increase of

<!-- b000350 | prose | pages [8] -->
EV/HEV is even more obvious than that of France and USA, from 0.11×108/0.11× 108 to 9.1×108/3.03×108. This indicates a huge EV/HEV market in China and a huge demand for electricity power. The control of CV quantity is not as effective as it seems in France and USA. It will rise from 0.9×108 to 2.3×108 and drop to 1.6× 108. The peak time appears in 2035. It is because the quantity of total vehicle will enter a rapid increase period at that time and increase of EV/HEV is not able to follow that trend. Although the total quantity of CV will ultimately increase, the proportion of CV in the entire vehicle will drop significantly, from 90% to 10%.

<!-- b000351 | heading | pages [8] -->
5. Energy Demand and Supply from/for EV and HEV

<!-- b000352 | prose | pages [8] -->
The surge of EV/HEV quantities in France, USA and China will definitely create

<!-- b000353 | furniture | pages [8] -->


<!-- b000354 | prose | pages [8] -->
huge demand for electricity, and supply plan is also needed. In this chapter, we will model the energy demand first. Then we will model the amount and type of electricity

<!-- b000355 | furniture | pages [8] -->


<!-- b000356 | prose | pages [8] -->
7

<!-- b000357 | furniture | pages [9] -->
Team #8882

<!-- b000358 | furniture | pages [9] -->


<!-- b000359 | furniture | pages [9] -->


<!-- b000360 | furniture | pages [9] -->
Page 8of 27

<!-- b000361 | prose | pages [9] -->
generation that would be needed to support the EV/HEV development under our plan. This model will provide us solutions to meet energy demand of huge quantity of EV and HEV in the future. Model will be established to consider environmental, social and economic effects.

<!-- b000362 | heading | pages [9] -->
5.1 Electricity Demand from EV/HEV

<!-- b000363 | prose | pages [9] -->
The demand for electricity can be modeled easily by (6).

<!-- b000364 | furniture | pages [9] -->


<!-- b000365 | prose | pages [9] -->
= A t ( ) ∑ ⋅ C Z t ( )

<!-- b000366 | furniture | pages [9] -->


<!-- b000367 | furniture | pages [9] -->


<!-- b000368 | furniture | pages [9] -->


<!-- b000369 | furniture | pages [9] -->


<!-- b000370 | furniture | pages [9] -->


<!-- b000371 | furniture | pages [9] -->


<!-- b000372 | furniture | pages [9] -->


<!-- b000373 | prose | pages [9] -->
(6) i i i i

<!-- b000374 | prose | pages [9] -->
is the electricity demanded in t year Where

<!-- b000375 | prose | pages [9] -->
A t ( )

<!-- b000376 | prose | pages [9] -->
iz t is th consumption per vehicle, ( )

<!-- b000377 | prose | pages [9] -->
e num

<!-- b000378 | prose | pages [9] -->
C is the average electricity

<!-- b000379 | prose | pages [9] -->
,

<!-- b000380 | prose | pages [9] -->
i

<!-- b000381 | prose | pages [9] -->
ber of i vehicle  the t year.

<!-- b000382 | prose | pages [9] -->
ni

<!-- b000383 | prose | pages [9] -->
From Table 1 we know EV will consume 450kJ/km and HEV will take up

<!-- b000384 | furniture | pages [9] -->


<!-- b000385 | prose | pages [9] -->
770kJ/km in electric mode. Also we have assumed each vehicle will travel 10,000km, and 1/8 of the distance traveled by HEV will be under electric-only mode. Thus we can figure out electricity demand from EV/HEV in France, USA and China.

<!-- b000386 | heading | pages [9] -->
5.2 Off-Peak Charging Supply for EV and HEV

<!-- b000387 | prose | pages [9] -->
Two typical electricity demand curves are shown in Figure 8. Peak period and

<!-- b000388 | furniture | pages [9] -->


<!-- b000389 | prose | pages [9] -->
off-peak period are colored differently. As we can see, a conspicuous rise and fall in electricity demand usually happens during a 24 hours electricity usage circle. The reason is quite simple, human activity in daytime is much more than that in the nighttime, creating a peak period in daytime and an off-peak period in nighttime. The fluctuations in power demand have always been an adverse factor for electricity generation. The generators have to run at full power in order to meet peak power demand. Yet when demand drops significantly, however, the power of generators can not simply follow down. Otherwise it will damage the gird system.[8] Thus electricity supply could only drop lightly during off-peak. Hence significant energy would be generated for no use, and the flow back of such energy is also undesirable for grid system. Such situation is very common in urban areas.

<!-- b000390 | furniture | pages [9] -->


<!-- b000391 | furniture | pages [9] -->


<!-- b000392 | furniture | pages [9] -->


<!-- b000393 | furniture | pages [9] -->


<!-- b000394 | prose | pages [9] -->
8

<!-- b000395 | furniture | pages [10] -->
Team #8882

<!-- b000396 | furniture | pages [10] -->


<!-- b000397 | furniture | pages [10] -->


<!-- b000398 | furniture | pages [10] -->
Page 9of 27

<!-- b000399 | caption | pages [10] -->
Figure 8. Electricity Supply in 24-hour-circle

<!-- b000400 | furniture | pages [10] -->


<!-- b000401 | furniture | pages [10] -->


<!-- b000402 | prose | pages [10] -->
The conventional method to deal with “extra electricity” is to store it by pulling up water or something else during off-peak period. In peak period, the lifted water could be used to generate electricity to meet soared energy demand. This process inevitably involves energy dissipation. Now we propose to directly use “extra electricity” to charge EV and HEV. In the left figure above, there are 66 blocks that shows the overall electricity generation, and there are 18 blocks in the “extra energy” areas during off-peak period. Thus, we estimate 27.3% of total electricity could be used for charging EV and HEV. If off-peak charging still cannot suffice the energy need from EV and HEV, other solution is needed. Now the effect of off-peak charging on general energy supply could be described in (7).

<!-- b000403 | prose | pages [10] -->
= ⎧ ( ) ( ) C t A t ⎨ = − ( ) O t

<!-- b000404 | furniture | pages [10] -->


<!-- b000405 | furniture | pages [10] -->


<!-- b000406 | furniture | pages [10] -->


<!-- b000407 | furniture | pages [10] -->


<!-- b000408 | furniture | pages [10] -->


<!-- b000409 | furniture | pages [10] -->


<!-- b000410 | furniture | pages [10] -->


<!-- b000411 | prose | pages [10] -->
(7)

<!-- b000412 | prose | pages [10] -->
⋅ 27.3% ( ) O t ⎩

<!-- b000413 | prose | pages [10] -->
C t ( )

<!-- b000414 | prose | pages [10] -->
( ) G t

<!-- b000415 | prose | pages [10] -->
t

<!-- b000416 | prose | pages [10] -->
is the electricity needed in Where

<!-- b000417 | prose | pages [10] -->
O t

<!-- b000418 | prose | pages [10] -->
power stations,  A(t) is defined in (6),

<!-- b000419 | prose | pages [10] -->
year to power EV and HEV by extra

<!-- b000420 | prose | pages [10] -->
( )

<!-- b000421 | prose | pages [10] -->
is the quantity of extra electrical energy

<!-- b000422 | prose | pages [10] -->
t

<!-- b000423 | prose | pages [10] -->
at off-peak times which can be used to charge EV/HEV in electricity generation in each country.

<!-- b000424 | furniture | pages [10] -->


<!-- b000425 | prose | pages [10] -->
year, G(t) is the overall

<!-- b000426 | prose | pages [10] -->
The overall electricity generation data in 2005 is listed in Table 4.

<!-- b000427 | furniture | pages [10] -->


<!-- b000428 | furniture | pages [10] -->


<!-- b000429 | furniture | pages [10] -->


<!-- b000430 | caption | pages [10] -->
Table 4. Annual Electricity Generation in France, USA and China

<!-- b000431 | furniture | pages [10] -->


<!-- b000432 | prose | pages [10] -->
Electricity Generation(1014kJ)9

<!-- b000433 | furniture | pages [10] -->


<!-- b000434 | prose | pages [10] -->
C(t) is shown in Figure 9, 10 and 11.

<!-- b000435 | prose | pages [10] -->
France USA China

<!-- b000436 | prose | pages [10] -->
19.46 142.24 131.42

<!-- b000437 | furniture | pages [10] -->


<!-- b000438 | prose | pages [10] -->
Figure 10 Figure 9

<!-- b000439 | furniture | pages [10] -->


<!-- b000440 | furniture | pages [10] -->


<!-- b000441 | furniture | pages [10] -->


<!-- b000442 | furniture | pages [10] -->


<!-- b000443 | furniture | pages [10] -->


<!-- b000444 | furniture | pages [10] -->


<!-- b000445 | furniture | pages [10] -->


<!-- b000446 | furniture | pages [10] -->


<!-- b000447 | furniture | pages [10] -->


<!-- b000448 | furniture | pages [10] -->


<!-- b000449 | furniture | pages [10] -->


<!-- b000450 | furniture | pages [10] -->


<!-- b000451 | furniture | pages [10] -->


<!-- b000452 | prose | pages [10] -->
Figure 11

<!-- b000453 | prose | pages [10] -->
9 http://en.wikipedia.org/wiki/Nuclear_power_in_France; http://en.wikipedia.org/wiki/Nuclear_power_in_china; http://en.wikipedia.org/wiki/Nuclear_power_in_the_United_States

<!-- b000454 | furniture | pages [10] -->


<!-- b000455 | prose | pages [10] -->
9

<!-- b000456 | furniture | pages [11] -->
Team #8882

<!-- b000457 | furniture | pages [11] -->


<!-- b000458 | furniture | pages [11] -->


<!-- b000459 | furniture | pages [11] -->
Page 10of 27

<!-- b000460 | prose | pages [11] -->
Electricity needed to be generated in USA Electricity needed to be generated in France Electricity needed to be generated in China

<!-- b000461 | furniture | pages [11] -->


<!-- b000462 | furniture | pages [11] -->


<!-- b000463 | prose | pages [11] -->
The electricity needed to be generated for EV/HEV in 2005 is shown in Table 5

<!-- b000464 | furniture | pages [11] -->


<!-- b000465 | caption | pages [11] -->
Table 5. Electricity needed to be generated for EV/HEV

<!-- b000466 | furniture | pages [11] -->


<!-- b000467 | prose | pages [11] -->
France USA China

<!-- b000468 | prose | pages [11] -->
Electricity Vacancy to power current EV and HEV(1014kJ)

<!-- b000469 | furniture | pages [11] -->


<!-- b000470 | prose | pages [11] -->
0.314 2.641 -2.45

<!-- b000471 | prose | pages [11] -->
In France and USA, we still need extra electricity to power existing EV and HEV. Yet in China (2005), the negative figure indicates that the off-peak charging should completely suffice the entire need for existing EV and HEV due to the smaller quantity of EV. Thus, off-peak charging is desirable to be promoted around the world, especially in countries like China, where current electricity generation could support entire EV/HEV and no other measures are required to meet the energy demand.

<!-- b000472 | furniture | pages [11] -->


<!-- b000473 | prose | pages [11] -->
Off-peak charging is also feasible and practical. EV and HEV can be simply left charging in nighttime while its owner goes to sleep, as long as he/she works and rests according to normal schedule. Government could also provide incentives to encourage off-peak charging. For example, the favored electricity price could be the most effective act to attract people charge their EVs or HEVs at night.

<!-- b000474 | furniture | pages [11] -->


<!-- b000475 | prose | pages [11] -->
With energy consumption per EV and HEV known, we could know how many EVs and HEVs can be powered merely by off-peak charging. The result is shown in

<!-- b000476 | caption | pages [11] -->
Table 6.

<!-- b000477 | furniture | pages [11] -->


<!-- b000478 | caption | pages [11] -->
Table 6. Number of EV/HEV supported by off-peak charging

<!-- b000479 | furniture | pages [11] -->


<!-- b000480 | prose | pages [11] -->
Number of EV fed by off-peak charging

<!-- b000481 | prose | pages [11] -->
Number of HEV fed by off-peak charging

<!-- b000482 | prose | pages [11] -->
France USA China

<!-- b000483 | prose | pages [11] -->
2,342,000 17,259,000 15,940,000

<!-- b000484 | prose | pages [11] -->
18,736,000 138,072,000 127,520,000

<!-- b000485 | heading | pages [11] -->
5.3 Extra Energy Supply for EV/HEV and Its Optimization

<!-- b000486 | prose | pages [11] -->
Off-peak charging will never suffice the electricity demand from EV/HEV in

<!-- b000487 | furniture | pages [11] -->


<!-- b000488 | prose | pages [11] -->
France and USA. And in China, it could only maintain the entire EV/HEV till 2012. After that off-peak charging will not be enough. Thus, we have to plan to extra energy supply for EV/HEV.

<!-- b000489 | furniture | pages [11] -->


<!-- b000490 | prose | pages [11] -->
The extra electricity vacancy could come from thermal power, hydroelectricity, nuclear energy, wind power or solar energy. Each type of generation has its particular traits, say its cost, price, potential capacity and limitation. As for government, it is desirable to manage new power industry to achieve maximum environmental, economic, and social benefits. Thus, not only should we provide more electricity, we should also optimize the energy plan among several options. We will discuss demand

<!-- b000491 | furniture | pages [11] -->


<!-- b000492 | prose | pages [11] -->
10

<!-- b000493 | furniture | pages [12] -->
Team #8882

<!-- b000494 | furniture | pages [12] -->


<!-- b000495 | furniture | pages [12] -->


<!-- b000496 | furniture | pages [12] -->
Page 11of 27

<!-- b000497 | prose | pages [12] -->
and limitation of new power energy first, and then strive for optimization of mix plan.

<!-- b000498 | furniture | pages [12] -->


<!-- b000499 | prose | pages [12] -->
First and foremost, new electricity generation should meet the electricity demand

<!-- b000500 | furniture | pages [12] -->


<!-- b000501 | prose | pages [12] -->
from EV and HEV. Second, each power option has its limit. For example, solar energy is limited by the energy the earth receives from the sun, which is abundant in desert; hydroelectricity is limited by water resources and geographic shape of landscape; wind power is also distributed without balance; nuclear power requires high level of technology and finance.

<!-- b000502 | furniture | pages [12] -->


<!-- b000503 | prose | pages [12] -->
Further more, an urgent task for government is to reduce the proportion of thermal power in the effort to rely less on fossil fuels. For example, in USA, the current proportion of thermal power is 67%10. We recommend government should reduce such figure to 10%. 10% is by no means an unrealistic goal, as France has achieved within 40 years.

<!-- b000504 | furniture | pages [12] -->


<!-- b000505 | prose | pages [12] -->
In addition, we recommend government to trade off between these energy options

<!-- b000506 | furniture | pages [12] -->


<!-- b000507 | prose | pages [12] -->
by achieving minimum electricity cost, as economic and financial factors are always the prioritized concerns of government and society.

<!-- b000508 | furniture | pages [12] -->


<!-- b000509 | prose | pages [12] -->
With these three major concerns, we will model the energy plan in (8) and (9)

<!-- b000510 | furniture | pages [12] -->


<!-- b000511 | prose | pages [12] -->
∑

<!-- b000512 | prose | pages [12] -->
min

<!-- b000513 | prose | pages [12] -->
∑

<!-- b000514 | prose | pages [12] -->
⎧

<!-- b000515 | prose | pages [12] -->
x t

<!-- b000516 | prose | pages [12] -->
( )

<!-- b000517 | prose | pages [12] -->
i

<!-- b000518 | prose | pages [12] -->
⎪⎪

<!-- b000519 | prose | pages [12] -->
i

<!-- b000520 | prose | pages [12] -->
≤

<!-- b000521 | prose | pages [12] -->
s t

<!-- b000522 | prose | pages [12] -->
. .

<!-- b000523 | prose | pages [12] -->
x t

<!-- b000524 | prose | pages [12] -->
( )

<!-- b000525 | prose | pages [12] -->
⎨

<!-- b000526 | prose | pages [12] -->
i

<!-- b000527 | prose | pages [12] -->
⎪ ≤

<!-- b000528 | prose | pages [12] -->
( )

<!-- b000529 | prose | pages [12] -->
x t

<!-- b000530 | prose | pages [12] -->
⎪⎩

<!-- b000531 | prose | pages [12] -->
1

<!-- b000532 | prose | pages [12] -->
⋅

<!-- b000533 | prose | pages [12] -->
( ) ( )

<!-- b000534 | prose | pages [12] -->
p t x t

<!-- b000535 | furniture | pages [12] -->


<!-- b000536 | furniture | pages [12] -->


<!-- b000537 | furniture | pages [12] -->


<!-- b000538 | furniture | pages [12] -->


<!-- b000539 | furniture | pages [12] -->


<!-- b000540 | furniture | pages [12] -->


<!-- b000541 | furniture | pages [12] -->


<!-- b000542 | prose | pages [12] -->
(8)

<!-- b000543 | prose | pages [12] -->
i i i i

<!-- b000544 | prose | pages [12] -->
≥

<!-- b000545 | prose | pages [12] -->
C t

<!-- b000546 | prose | pages [12] -->
( )

<!-- b000547 | prose | pages [12] -->
k t

<!-- b000548 | prose | pages [12] -->
( )

<!-- b000549 | furniture | pages [12] -->


<!-- b000550 | furniture | pages [12] -->


<!-- b000551 | furniture | pages [12] -->


<!-- b000552 | furniture | pages [12] -->


<!-- b000553 | furniture | pages [12] -->


<!-- b000554 | furniture | pages [12] -->


<!-- b000555 | prose | pages [12] -->
(9)

<!-- b000556 | prose | pages [12] -->
i i

<!-- b000557 | prose | pages [12] -->
∑

<!-- b000558 | prose | pages [12] -->
⋅

<!-- b000559 | prose | pages [12] -->
t

<!-- b000560 | prose | pages [12] -->
10% ( )

<!-- b000561 | prose | pages [12] -->
x

<!-- b000562 | prose | pages [12] -->
i i

<!-- b000563 | prose | pages [12] -->
ip t is the cost of per joule of Where ( ) i electrical energy in the t year, ix t ( )

<!-- b000564 | prose | pages [12] -->
type of electricity in the is the generation of i t year, x t is the thermal power 1( )

<!-- b000565 | prose | pages [12] -->
is the limit of generation in the

<!-- b000566 | prose | pages [12] -->
t

<!-- b000567 | prose | pages [12] -->
year,

<!-- b000568 | prose | pages [12] -->
( ) ik t

<!-- b000569 | prose | pages [12] -->
year, C t has been defined in (7).

<!-- b000570 | prose | pages [12] -->
t ( )

<!-- b000571 | furniture | pages [12] -->


<!-- b000572 | prose | pages [12] -->
type of electricity generation in the

<!-- b000573 | prose | pages [12] -->
i

<!-- b000574 | prose | pages [12] -->
We collect the prices of various kind of electricity in France, USA and China, as well as limitations of different types of electricity generation. The data is shown in

<!-- b000575 | caption | pages [12] -->
Table 7.

<!-- b000576 | furniture | pages [12] -->


<!-- b000577 | furniture | pages [12] -->


<!-- b000578 | furniture | pages [12] -->


<!-- b000579 | furniture | pages [12] -->


<!-- b000580 | furniture | pages [12] -->


<!-- b000581 | prose | pages [12] -->
10 http://www.eia.doe.gov/aer/pecss_diagram.html

<!-- b000582 | furniture | pages [12] -->


<!-- b000583 | prose | pages [12] -->
11

<!-- b000584 | furniture | pages [13] -->
Team #8882

<!-- b000585 | furniture | pages [13] -->


<!-- b000586 | furniture | pages [13] -->


<!-- b000587 | furniture | pages [13] -->


<!-- b000588 | furniture | pages [13] -->
Page 12of 27

<!-- b000589 | caption | pages [13] -->
Table 7. Values of coefficients in (8) and (9)

<!-- b000590 | prose | pages [13] -->
p1(t)

<!-- b000591 | prose | pages [13] -->
p2(t)

<!-- b000592 | prose | pages [13] -->
p3(t)

<!-- b000593 | prose | pages [13] -->
p4(t)

<!-- b000594 | furniture | pages [13] -->


<!-- b000595 | prose | pages [13] -->
Thermal

<!-- b000596 | prose | pages [13] -->
Hydro

<!-- b000597 | prose | pages [13] -->
Nuclear

<!-- b000598 | prose | pages [13] -->
Wind

<!-- b000599 | prose | pages [13] -->
Franc

<!-- b000600 | prose | pages [13] -->
3 c/kwh 6 c/kwh 4 c/kwh 8 c/kwh e

<!-- b000601 | prose | pages [13] -->
2 c/kwh 5 c/kwh 3 c/kwh 5 c/kwh USA

<!-- b000602 | prose | pages [13] -->
0.18

<!-- b000603 | prose | pages [13] -->
0.1

<!-- b000604 | prose | pages [13] -->
0.2

<!-- b000605 | prose | pages [13] -->
0.5

<!-- b000606 | prose | pages [13] -->
China

<!-- b000607 | prose | pages [13] -->
RMB/k

<!-- b000608 | prose | pages [13] -->
RMB/k

<!-- b000609 | prose | pages [13] -->
RMB/k

<!-- b000610 | prose | pages [13] -->
RMB/k

<!-- b000611 | prose | pages [13] -->
wh

<!-- b000612 | prose | pages [13] -->
wh

<!-- b000613 | prose | pages [13] -->
wh

<!-- b000614 | prose | pages [13] -->
wh

<!-- b000615 | prose | pages [13] -->
k1(t)

<!-- b000616 | prose | pages [13] -->
p5(t)

<!-- b000617 | prose | pages [13] -->
k2(t)

<!-- b000618 | prose | pages [13] -->
k3(t)

<!-- b000619 | prose | pages [13] -->
k4(t)

<!-- b000620 | prose | pages [13] -->
k5(t)

<!-- b000621 | prose | pages [13] -->
Therma

<!-- b000622 | prose | pages [13] -->
Solar

<!-- b000623 | prose | pages [13] -->
Hydro

<!-- b000624 | prose | pages [13] -->
Nuclear

<!-- b000625 | prose | pages [13] -->
Wind

<!-- b000626 | prose | pages [13] -->
Solar

<!-- b000627 | prose | pages [13] -->
l

<!-- b000628 | prose | pages [13] -->
4×

<!-- b000629 | prose | pages [13] -->
0.8×

<!-- b000630 | prose | pages [13] -->
70×

<!-- b000631 | prose | pages [13] -->
1.8×

<!-- b000632 | prose | pages [13] -->
1.8×

<!-- b000633 | prose | pages [13] -->
109kw

<!-- b000634 | prose | pages [13] -->
109kw

<!-- b000635 | prose | pages [13] -->
109kw

<!-- b000636 | prose | pages [13] -->
109kw

<!-- b000637 | prose | pages [13] -->
109kw

<!-- b000638 | prose | pages [13] -->
5 c/kwh h

<!-- b000639 | prose | pages [13] -->
h

<!-- b000640 | prose | pages [13] -->
h

<!-- b000641 | prose | pages [13] -->
h

<!-- b000642 | prose | pages [13] -->
h

<!-- b000643 | prose | pages [13] -->
1.2×

<!-- b000644 | prose | pages [13] -->
0.9×

<!-- b000645 | prose | pages [13] -->
6×

<!-- b000646 | prose | pages [13] -->
0.9×

<!-- b000647 | prose | pages [13] -->
3×

<!-- b000648 | prose | pages [13] -->
1011kw

<!-- b000649 | prose | pages [13] -->
1011kw

<!-- b000650 | prose | pages [13] -->
1011kw

<!-- b000651 | prose | pages [13] -->
1011kw

<!-- b000652 | prose | pages [13] -->
1011kw

<!-- b000653 | prose | pages [13] -->
4 c/kwh h

<!-- b000654 | prose | pages [13] -->
h

<!-- b000655 | prose | pages [13] -->
h

<!-- b000656 | prose | pages [13] -->
h

<!-- b000657 | prose | pages [13] -->
h

<!-- b000658 | prose | pages [13] -->
0.3

<!-- b000659 | prose | pages [13] -->
1.8×

<!-- b000660 | prose | pages [13] -->
11×

<!-- b000661 | prose | pages [13] -->
5×

<!-- b000662 | prose | pages [13] -->
3×

<!-- b000663 | prose | pages [13] -->
4×

<!-- b000664 | prose | pages [13] -->
1011kw

<!-- b000665 | prose | pages [13] -->
1011kw

<!-- b000666 | prose | pages [13] -->
1011kw

<!-- b000667 | prose | pages [13] -->
1011kw

<!-- b000668 | prose | pages [13] -->
1011kw

<!-- b000669 | prose | pages [13] -->
RMB/k

<!-- b000670 | prose | pages [13] -->
wh

<!-- b000671 | prose | pages [13] -->
h

<!-- b000672 | prose | pages [13] -->
h

<!-- b000673 | prose | pages [13] -->
h

<!-- b000674 | prose | pages [13] -->
h

<!-- b000675 | prose | pages [13] -->
h

<!-- b000676 | furniture | pages [13] -->


<!-- b000677 | prose | pages [13] -->
Given the values of coefficients in this model, the result can be figured out and is shown in Figure 12. This is our electricity supply plan for France, USA and China.

<!-- b000678 | furniture | pages [13] -->


<!-- b000679 | caption | pages [13] -->
Figure 12. Amount and type of electricity generation to meet energy demand from EV/HEV in France, USA and China

<!-- b000680 | furniture | pages [13] -->


<!-- b000681 | furniture | pages [13] -->


<!-- b000682 | prose | pages [13] -->
The left figure shows power supply in France. We can notice significant increase of nuclear energy. This is because the mature nuclear technology in France has greatly lowered the price of nuclear electricity. Thermal power, although increases slightly, will have decreasing proportion in overall electricity generation. Hydroelectricity, solar and wind energy hardly increase at all, since they are scarce in France. That’s why nuclear power will remain dominant in France.

<!-- b000683 | furniture | pages [13] -->


<!-- b000684 | prose | pages [13] -->
The middle figure shows the power supply in USA. The electricity prices are similar among different types. Thus natural limitation will mainly determine the distribution among different types of energy generation. As the capacity of nuclear power is big, nuclear power will start from a small proportion in 2005 and end up with the highest in 2055. Solar energy, wind energy and hydroelectricity are all abundant in USA, so the distribution of these three energies is relatively even.

<!-- b000685 | furniture | pages [13] -->


<!-- b000686 | prose | pages [13] -->
12

<!-- b000687 | furniture | pages [14] -->
Team #8882

<!-- b000688 | furniture | pages [14] -->


<!-- b000689 | furniture | pages [14] -->


<!-- b000690 | furniture | pages [14] -->
Page 13of 27

<!-- b000691 | prose | pages [14] -->
Thermal power will be controlled under 10% of total electricity generation.

<!-- b000692 | furniture | pages [14] -->


<!-- b000693 | prose | pages [14] -->
The right figure shows the power supply in China. As hydroelectricity is relatively cheap and abundant in China, it will ultimately become the most popular energy generation type. Thermal power is also cheap. However, government is going control its weight under 10% of total electricity generation to fulfill its environmental responsibility. That’s why thermal power will rise in the first 30 years and then stop at a certain percentage of total power. Nuclear power is slightly more expensive than thermal power, but due to the fact that it will not be stifled, it will become the second largest energy in China. Though solar and wind energy also abound in China compared with France, their higher price determine their low proportion.

<!-- b000694 | furniture | pages [14] -->


<!-- b000695 | prose | pages [14] -->
Then we need to take one step further to find out how many more power plants will be constructed to provide power exclusively for EV and HEV. As the generated output varies greatly among different types of power plants, and even among the same type of power plant with different scales of construction, there is no easy way to calculate how many power plants of each type are needed. Thus, we will not specify different types of power plants and assume that each plant will generate 10,000,000kwh annually on average. The number of power stations can be calculated in (10).

<!-- b000696 | prose | pages [14] -->
n t ( )

<!-- b000697 | prose | pages [14] -->
1

<!-- b000698 | prose | pages [14] -->
C t ( ) =

<!-- b000699 | furniture | pages [14] -->


<!-- b000700 | furniture | pages [14] -->


<!-- b000701 | furniture | pages [14] -->


<!-- b000702 | furniture | pages [14] -->


<!-- b000703 | furniture | pages [14] -->


<!-- b000704 | furniture | pages [14] -->


<!-- b000705 | furniture | pages [14] -->


<!-- b000706 | prose | pages [14] -->
(10) E

<!-- b000707 | prose | pages [14] -->
0

<!-- b000708 | prose | pages [14] -->
Where C(t) has been defined in (7), E0 is the generated output per general power station and n1(t) is the number of power stations needed to exist in each year.

<!-- b000709 | furniture | pages [14] -->


<!-- b000710 | prose | pages [14] -->
Since five years could be a normal circle to build a typical power station, we will show how many new power plants will be established within a 5 years circle in France, USA and China. The result is shown in Figure 13.

<!-- b000711 | furniture | pages [14] -->


<!-- b000712 | caption | pages [14] -->
Figure 13. New power stations needed to be constructed in a five-year circle in France, USA and

<!-- b000713 | prose | pages [14] -->
China

<!-- b000714 | furniture | pages [14] -->


<!-- b000715 | furniture | pages [14] -->


<!-- b000716 | prose | pages [14] -->
In France and USA, more power stations are need in short term than that in long

<!-- b000717 | furniture | pages [14] -->


<!-- b000718 | prose | pages [14] -->
term. In China, thanks to the off-peak charging and low vehicles ownership, no power

<!-- b000719 | furniture | pages [14] -->


<!-- b000720 | prose | pages [14] -->
13

<!-- b000721 | furniture | pages [15] -->
Team #8882

<!-- b000722 | furniture | pages [15] -->


<!-- b000723 | furniture | pages [15] -->


<!-- b000724 | furniture | pages [15] -->
Page 14of 27

<!-- b000725 | prose | pages [15] -->
stations are need before 2010, then it will increase from zero to 1200 per year within 20 years. The small need for construction in short term is beneficial for a developing country. Thus government will be allowed with more time to prepare for the financing.

<!-- b000726 | heading | pages [15] -->
6. Environmental, Economic, Social and Health

<!-- b000727 | prose | pages [15] -->
Impacts of EV/HEV

<!-- b000728 | heading | pages [15] -->
6.1 EV/HEV Consumes Less Fossil Fuels

<!-- b000729 | prose | pages [15] -->
The discussion in previous chapter reveals the potential reliance upon fossil fuels

<!-- b000730 | furniture | pages [15] -->


<!-- b000731 | prose | pages [15] -->
of EV and HEV. In this chapter, we will model the impact of EV and HEV on total fossil fuel consumption. This will help us better evaluate whether EV and HEV would consume less fossil fuels. Such evaluation is of vital importance because it is widely questioned that EV and HEV might burn more fossil fuels. Since burning fossil fuels, whether oil or gas, to generate electricity will definitely release CO2, we will measure reliance upon fossil fuels by measuring CO2 emissions. In order to do this, we introduce CO2 intensity. CO2 intensity is the average amount of CO2 emitted per unit of electrical energy generated by all of the power production processes in a mix weighted.[6] Thus the emissions from EVs depend on their own energy consumption and on the CO2 intensity of the power generation mix from which the EV’s energy was obtained. The CO2 intensity varies considerably depending on the composition of the power generation mix. For instance, in countries like China where thermal power provides more than 75% of general electricity, EVs charging from the electric grid will be responsible for significantly more emissions than in a country like France that derives less than 10% of its power from fossil fuels [7]. The situation is similar in electric-only mode of HEV. For CV, its emission can be tested directly from the tailpipe. Thus we calculate the CO2 emission in (11)

<!-- b000732 | prose | pages [15] -->
= ⎧

<!-- b000733 | prose | pages [15] -->
S t

<!-- b000734 | prose | pages [15] -->
( )

<!-- b000735 | prose | pages [15] -->
S

<!-- b000736 | prose | pages [15] -->
CV

<!-- b000737 | prose | pages [15] -->
⎪ = + +

<!-- b000738 | prose | pages [15] -->
( )

<!-- b000739 | prose | pages [15] -->
t t S

<!-- b000740 | prose | pages [15] -->
( )

<!-- b000741 | prose | pages [15] -->
t S

<!-- b000742 | prose | pages [15] -->
( )

<!-- b000743 | prose | pages [15] -->
t

<!-- b000744 | prose | pages [15] -->
EV HEV

<!-- b000745 | prose | pages [15] -->
⋅ ⋅ ⋅

<!-- b000746 | prose | pages [15] -->
L v S

<!-- b000747 | prose | pages [15] -->
( )

<!-- b000748 | prose | pages [15] -->
t

<!-- b000749 | prose | pages [15] -->
⎪

<!-- b000750 | prose | pages [15] -->
CV

<!-- b000751 | prose | pages [15] -->
⎪ =

<!-- b000752 | prose | pages [15] -->
S

<!-- b000753 | prose | pages [15] -->
( )

<!-- b000754 | prose | pages [15] -->
t L

<!-- b000755 | prose | pages [15] -->
EV

<!-- b000756 | prose | pages [15] -->
⎪ = ⎨

<!-- b000757 | prose | pages [15] -->
S

<!-- b000758 | prose | pages [15] -->
( )

<!-- b000759 | prose | pages [15] -->
t

<!-- b000760 | prose | pages [15] -->
HEV

<!-- b000761 | prose | pages [15] -->
⎪ = ⋅

<!-- b000762 | prose | pages [15] -->
v I E

<!-- b000763 | prose | pages [15] -->
⎪

<!-- b000764 | prose | pages [15] -->
2 2

<!-- b000765 | prose | pages [15] -->
⎪ ⋅

<!-- b000766 | prose | pages [15] -->
'

<!-- b000767 | prose | pages [15] -->
a v

<!-- b000768 | prose | pages [15] -->
= ⎪

<!-- b000769 | prose | pages [15] -->
3

<!-- b000770 | prose | pages [15] -->
v

<!-- b000771 | prose | pages [15] -->
3

<!-- b000772 | prose | pages [15] -->
⎩

<!-- b000773 | prose | pages [15] -->
S t ( )

<!-- b000774 | prose | pages [15] -->
z

<!-- b000775 | prose | pages [15] -->
1 1 1 1

<!-- b000776 | prose | pages [15] -->
⋅ ⋅ ⋅

<!-- b000777 | prose | pages [15] -->
v z

<!-- b000778 | prose | pages [15] -->
2 2 2 2

<!-- b000779 | prose | pages [15] -->
⋅ ⋅

<!-- b000780 | furniture | pages [15] -->


<!-- b000781 | furniture | pages [15] -->


<!-- b000782 | furniture | pages [15] -->


<!-- b000783 | furniture | pages [15] -->


<!-- b000784 | prose | pages [15] -->
(11)

<!-- b000785 | prose | pages [15] -->
L v z

<!-- b000786 | prose | pages [15] -->
3 3 3 3

<!-- b000787 | prose | pages [15] -->
2 2

<!-- b000788 | prose | pages [15] -->
+ ⋅ ⋅

<!-- b000789 | prose | pages [15] -->
b I E

<!-- b000790 | prose | pages [15] -->
3 3

<!-- b000791 | prose | pages [15] -->
+

<!-- b000792 | prose | pages [15] -->
a a b

<!-- b000793 | prose | pages [15] -->
is the carbon dioxide emissions in the t year, Where

<!-- b000794 | prose | pages [15] -->
distance traveled by

<!-- b000795 | prose | pages [15] -->
i

<!-- b000796 | prose | pages [15] -->
type of vehicle in

<!-- b000797 | furniture | pages [15] -->


<!-- b000798 | prose | pages [15] -->
iL

<!-- b000799 | prose | pages [15] -->
(km) is the

<!-- b000800 | prose | pages [15] -->
iv t t

<!-- b000801 | prose | pages [15] -->
year, (gCO2/Km) is the emissions of

<!-- b000802 | prose | pages [15] -->
14

<!-- b000803 | furniture | pages [16] -->
Team #8882

<!-- b000804 | furniture | pages [16] -->


<!-- b000805 | furniture | pages [16] -->


<!-- b000806 | furniture | pages [16] -->
Page 15of 27

<!-- b000807 | prose | pages [16] -->
I is vehicle, carbon dioxide per kilometer by i iz is the number of i vehicle,

<!-- b000808 | prose | pages [16] -->
CO2 intensity, E (kj/km) indicates energy in terms of joule required to propel vehicle represents the oil-only mode and electric-only for unit distance, and

<!-- b000809 | prose | pages [16] -->
a b

<!-- b000810 | prose | pages [16] -->
1v

<!-- b000811 | prose | pages [16] -->
proportion of HEV respectively. From previous chapters we know

<!-- b000812 | prose | pages [16] -->
11,

<!-- b000813 | prose | pages [16] -->
'v 3

<!-- b000814 | prose | pages [16] -->
is

<!-- b000815 | prose | pages [16] -->
E

<!-- b000816 | prose | pages [16] -->
is—108gCO2/km, E

<!-- b000817 | prose | pages [16] -->
155gCO2/km, is 450kj/km

<!-- b000818 | prose | pages [16] -->
2

<!-- b000819 | prose | pages [16] -->
and b is 420km.

<!-- b000820 | prose | pages [16] -->
—770kj/km, a is 50km

<!-- b000821 | prose | pages [16] -->
3

<!-- b000822 | prose | pages [16] -->
iI , the CO2 intensity, varies among countries. It depends on how much electricity

<!-- b000823 | prose | pages [16] -->
is generated from fossil fuel combustion, as well as how much CO2 is emitted while burning fossil fuel in order to generate unit electricity. We collect information of France, USA and China as list them in Table 8.

<!-- b000824 | furniture | pages [16] -->


<!-- b000825 | caption | pages [16] -->
Table 8. Information related with CO2 intensity

<!-- b000826 | furniture | pages [16] -->


<!-- b000827 | prose | pages [16] -->
France USA China

<!-- b000828 | prose | pages [16] -->
10% 67% 75% Proportion of electricity generated by fossil fuel

<!-- b000829 | prose | pages [16] -->
0.0833 0.0833 0.0833

<!-- b000830 | prose | pages [16] -->
How much CO2 is emitted to make 1jk by burning fossil fuels

<!-- b000831 | prose | pages [16] -->
(gCO2/kj)?

<!-- b000832 | prose | pages [16] -->
CO2 intensity(gCO2/kj)

<!-- b000833 | furniture | pages [16] -->


<!-- b000834 | furniture | pages [16] -->


<!-- b000835 | prose | pages [16] -->
0.00833 0.055811 0.062475

<!-- b000836 | prose | pages [16] -->
Then we can figure out how much CO2 EV and HEV will release by running one

<!-- b000837 | furniture | pages [16] -->


<!-- b000838 | prose | pages [16] -->
kilometer. We list such figure in Table 9. In this table, we will also show the gCO2/km of CV to compare their fossil fuel consumption.

<!-- b000839 | furniture | pages [16] -->


<!-- b000840 | caption | pages [16] -->
Table 9. CO2 consumption of CV, EV and HEV in France, USA and China

<!-- b000841 | furniture | pages [16] -->


<!-- b000842 | prose | pages [16] -->
France

<!-- b000843 | prose | pages [16] -->
155 CV(gCO2/km)

<!-- b000844 | prose | pages [16] -->
3.75 EV(gCO2/km)

<!-- b000845 | prose | pages [16] -->
138.116 HEV(gCO2/km)

<!-- b000846 | furniture | pages [16] -->


<!-- b000847 | furniture | pages [16] -->


<!-- b000848 | prose | pages [16] -->
USA China

<!-- b000849 | prose | pages [16] -->
155 155

<!-- b000850 | prose | pages [16] -->
25.125 28.125

<!-- b000851 | prose | pages [16] -->
140.49 140.825

<!-- b000852 | prose | pages [16] -->
This figure finally reveals the widely asked question that whether EV will save

<!-- b000853 | furniture | pages [16] -->


<!-- b000854 | prose | pages [16] -->
fossil fuel. And the answer is yes! In France, as its thermal power only takes up 10% of its general electricity generation, its electricity contributes far less CO2 emissions and fossil fuels consumption. Thus driving EV in France merely generates 3.75gCO2 per km compared to 155gCO2 of CV. Even in USA and China, where a major part of electricity is made from fossil fuels, and where electricity contain more fossil fuel energy, driving EV could also achieve 25.125gCO2/km and 28.125gCO2/km respectively, contributing a great save on fossil fuels. This might be the result of high energy conversion efficiency of electric motor. Thus, we believe EV would help saving fossil fuel around the world. As for HEV, the gCO2/km figure is only lightly

<!-- b000855 | furniture | pages [16] -->


<!-- b000856 | prose | pages [16] -->
11 www.teslamotors.com

<!-- b000857 | furniture | pages [16] -->


<!-- b000858 | prose | pages [16] -->
15

<!-- b000859 | furniture | pages [17] -->
Team #8882

<!-- b000860 | furniture | pages [17] -->


<!-- b000861 | furniture | pages [17] -->


<!-- b000862 | furniture | pages [17] -->
Page 16of 27

<!-- b000863 | prose | pages [17] -->
lower than that of CV. This is resulted from the low ratio of electric-only distance to oil-only distance which is merely 1:8. However, electric-only mode is mainly used in starting and low speed, when the use of combustion engine only achieves a very low efficiency. Moreover, with the development of technology, the battery will be endowed with stronger capacity which will lift the electric-only distance. Hence in the future the HEV will also become a conscientious fossil fuel saver.

<!-- b000864 | furniture | pages [17] -->


<!-- b000865 | prose | pages [17] -->
Then we are anxious to know the fossil fuel consumption when EV and HEV are

<!-- b000866 | furniture | pages [17] -->


<!-- b000867 | prose | pages [17] -->
gradually replacing CV. We run the model in matlab and show the result in Figure 14, 15 and 16.

<!-- b000868 | furniture | pages [17] -->


<!-- b000869 | caption | pages [17] -->
Figure 15. CO2 emission in USA

<!-- b000870 | caption | pages [17] -->
Figure 14. CO2 emission in France

<!-- b000871 | furniture | pages [17] -->


<!-- b000872 | furniture | pages [17] -->


<!-- b000873 | furniture | pages [17] -->


<!-- b000874 | furniture | pages [17] -->


<!-- b000875 | caption | pages [17] -->
Figure 16. CO2 emission in China

<!-- b000876 | prose | pages [17] -->
As we can see, the carbon emission cause by vehicles in France is initially about 1/3 of USA and 1/10 of China. Its CO2 containment in electricity is also lower than USA and China. With the decline in the number of CV and rise in the number of EV and HEV, the carbon emission will go down from the very beginning, indicating the decline in the consumption of fossil fuels. So introduction of EV/HEV is very successful in saving fossil fuels. In USA, the number of CV will also decline; the number EV and HEV will rise. Yet its CO2 containment in electricity is 6.7 times of France. Consequently, the CO2 emission will rise slightly in the next five years, and then the emission will head down. In China, the CO2 containment in electricity is even higher. The number of CV will increase till 2035 and then go down. The number of EV and HEV will also increase. Therefore, the carbon emission will increase till 2040 and then drop. It is likely that the increase of CV before 2035 and high CO2 containment in electricity result in the increase of carbon emission before 2040. After 2040, the carbon emission begins to fall rapidly while the number of EV and HEV is still increasing. Therefore, we conclude that the massive use of EV and HEV will reduce the reliance upon fossil fuels effectively. And it is worthy in environmental concerns to promote EV and HEV.

<!-- b000877 | furniture | pages [17] -->


<!-- b000878 | prose | pages [17] -->
Then we will examine how much oil will be saved. Given the total number of

<!-- b000879 | furniture | pages [17] -->


<!-- b000880 | prose | pages [17] -->
vehicles each year from 2005 to 2055 in France, USA and China, we could calculate

<!-- b000881 | furniture | pages [17] -->


<!-- b000882 | prose | pages [17] -->
16

<!-- b000883 | furniture | pages [18] -->
Team #8882

<!-- b000884 | furniture | pages [18] -->


<!-- b000885 | furniture | pages [18] -->


<!-- b000886 | furniture | pages [18] -->
Page 17of 27

<!-- b000887 | prose | pages [18] -->
the consumption of oil if all of the vehicles are CV. This will simulate the scenario that EV/HEV doesn’t contribute to consumption of fossil fuels at all. Given the number of CV, EV and HEV from 2005 to 2055 in these three countries, we can calculate the consumption of oil under the situation where EV/HEV is replacing CV according to our estimation. By comparing oil consumption with and without EV/HEV, we could see if and how much EV/HEV will save oil. Following such analysis, we have the following model.

<!-- b000888 | furniture | pages [18] -->


<!-- b000889 | prose | pages [18] -->
∑ = ⋅ Q t C ( ) cv

<!-- b000890 | prose | pages [18] -->
Q t

<!-- b000891 | prose | pages [18] -->
∑ − ⋅ z t C z t ( ) ( )

<!-- b000892 | furniture | pages [18] -->


<!-- b000893 | furniture | pages [18] -->


<!-- b000894 | furniture | pages [18] -->


<!-- b000895 | furniture | pages [18] -->


<!-- b000896 | furniture | pages [18] -->


<!-- b000897 | prose | pages [18] -->
(12) i i i i i i

<!-- b000898 | prose | pages [18] -->
is the quantity of oil one specific country can save by widely using Where

<!-- b000899 | prose | pages [18] -->
( )

<!-- b000900 | prose | pages [18] -->
C i

<!-- b000901 | prose | pages [18] -->
vehicle in the t is the average consumption of oil per electrical vehicles,

<!-- b000902 | prose | pages [18] -->
i

<!-- b000903 | prose | pages [18] -->
iz t i ( ) t

<!-- b000904 | prose | pages [18] -->
vehicle in the year, is the quantity of

<!-- b000905 | furniture | pages [18] -->


<!-- b000906 | prose | pages [18] -->
The result is shown in Figure 17.

<!-- b000907 | prose | pages [18] -->
year.

<!-- b000908 | furniture | pages [18] -->


<!-- b000909 | caption | pages [18] -->
Figure 17. Oil saved by EV/HEV in France, USA and China

<!-- b000910 | furniture | pages [18] -->


<!-- b000911 | prose | pages [18] -->
Q t

<!-- b000912 | prose | pages [18] -->
of the China, USA, and France, we can calculate the According to the

<!-- b000913 | prose | pages [18] -->
( )

<!-- b000914 | prose | pages [18] -->
quantity of oil the world can save by widely using electrical vehicles based on bound weight coefficients.

<!-- b000915 | prose | pages [18] -->
= ⋅ Total t r Q ( )

<!-- b000916 | furniture | pages [18] -->


<!-- b000917 | prose | pages [18] -->
1 China

<!-- b000918 | prose | pages [18] -->
ir

<!-- b000919 | prose | pages [18] -->
+ ⋅ + ⋅ r Q r Q

<!-- b000920 | furniture | pages [18] -->


<!-- b000921 | furniture | pages [18] -->


<!-- b000922 | furniture | pages [18] -->


<!-- b000923 | furniture | pages [18] -->


<!-- b000924 | prose | pages [18] -->
(13) 2 3 USA Frace

<!-- b000925 | prose | pages [18] -->
Q t ( )

<!-- b000926 | prose | pages [18] -->
is the weight coefficient of each country, Where

<!-- b000927 | prose | pages [18] -->
Total t ( )

<!-- b000928 | prose | pages [18] -->
is the quantity of oil

<!-- b000929 | prose | pages [18] -->
i

<!-- b000930 | prose | pages [18] -->
is the quantity of oil the world can save by widely each country can save,

<!-- b000931 | prose | pages [18] -->
using electrical vehicles.

<!-- b000932 | furniture | pages [18] -->


<!-- b000933 | furniture | pages [18] -->


<!-- b000934 | furniture | pages [18] -->


<!-- b000935 | prose | pages [18] -->
17

<!-- b000936 | furniture | pages [19] -->
Team #8882

<!-- b000937 | prose | pages [19] -->
r1

<!-- b000938 | furniture | pages [19] -->


<!-- b000939 | furniture | pages [19] -->


<!-- b000940 | furniture | pages [19] -->
Page 18of 27

<!-- b000941 | prose | pages [19] -->
r2 r2 r3

<!-- b000942 | prose | pages [19] -->
2.4333 2．6462

<!-- b000943 | furniture | pages [19] -->


<!-- b000944 | prose | pages [19] -->
12.1333

<!-- b000945 | prose | pages [19] -->
Then we figure out the total oil saved in the world, as is shown in Figure 18

<!-- b000946 | furniture | pages [19] -->


<!-- b000947 | furniture | pages [19] -->


<!-- b000948 | caption | pages [19] -->
Figure 18. Oil saved in the world

<!-- b000949 | furniture | pages [19] -->


<!-- b000950 | furniture | pages [19] -->


<!-- b000951 | prose | pages [19] -->
As we can see, if all EV/HEV are replaced by CV, the oil consumption will skyrocket. It

<!-- b000952 | furniture | pages [19] -->


<!-- b000953 | prose | pages [19] -->
means that introduction of EV/HEV will save a significant amount of oil. The oil saved just in 2055 will be 2.5 billion L.

<!-- b000954 | heading | pages [19] -->
6.2 Driving EV and HEV Costs Less

<!-- b000955 | prose | pages [19] -->
EVs and HEVs will save fossil fuels, which is desirable in the eyes of environmentalist. However, to be environmentally friendly cannot always guarantee public popularity. Its promotion among societies and governments depends upon the economic and social benefits. In this and following two chapters, we are going to examine the feasibility to promote EV hand HEV among common families and governments, with economic and social incentives, not by regulations.

<!-- b000956 | furniture | pages [19] -->


<!-- b000957 | prose | pages [19] -->
One huge benefit of electric vehicles is their low fuel costs as compared to

<!-- b000958 | furniture | pages [19] -->


<!-- b000959 | prose | pages [19] -->
gasoline vehicles. Let’s work out the driving cost of CV, EV and HEV and compare them together.  The average consumption of oil by CV worldwide is 8L/100Km. The average electricity consumption of EV and HEV is 20Kwh/100Km. The current oil price in France, USA and China is 1.38€/L, 58.17$/barrel and 7RMB/L. The current electricity price in France, USA and China is 0.12€/kwh, 6$/kwh and 56RMB/100kwh. As vehicle will run 10,000Km on average in each year worldwide.

<!-- b000960 | furniture | pages [19] -->


<!-- b000961 | furniture | pages [19] -->


<!-- b000962 | prose | pages [19] -->
18

<!-- b000963 | furniture | pages [20] -->
Team #8882

<!-- b000964 | furniture | pages [20] -->


<!-- b000965 | furniture | pages [20] -->


<!-- b000966 | furniture | pages [20] -->
Page 19of 27

<!-- b000967 | prose | pages [20] -->
Further more, because there are no moving parts in an electric motor (as opposed to many in an internal combustion engine), there are many fewer things that can go wrong with an electric car, which means they'll probably save considerable money on maintenance costs as well. Electric vehicles have roughly 90% fewer parts than gasoline-powered vehicles. On RepairTrust.com, the maintenance costs for a typical car is $272.03 per 30,000 miles.12 That is $56.6 a year on average. A rough estimate is that number of parts in vehicle is in linear correlation with maintenance fee. So driving EV will save another $51 a year.

<!-- b000968 | furniture | pages [20] -->


<!-- b000969 | prose | pages [20] -->
Now we can figure out the driving cost of EV, HEV and CV, as shown in Table 10. Note that 1/9 of the distance of HEV will be covered under electric-only mode.

<!-- b000970 | furniture | pages [20] -->


<!-- b000971 | caption | pages [20] -->
Table 10. Cost and Saving of driving CV, EV and HEV

<!-- b000972 | furniture | pages [20] -->


<!-- b000973 | prose | pages [20] -->
France USA China

<!-- b000974 | prose | pages [20] -->
14.9 6.3 8.61 Cost of driving CV(also driving HEV on oil-mode)( $/100Km)

<!-- b000975 | prose | pages [20] -->
3.25 1.2 1.72 Cost of driving EV(also driving HEV on electric-mode)( $/100Km)

<!-- b000976 | prose | pages [20] -->
1165 510 689 Cost saved in one year by driving with electricity per vehicle($)

<!-- b000977 | furniture | pages [20] -->


<!-- b000978 | heading | pages [20] -->
6.3 New Vehicle Industry Provides More Job Opportunities

<!-- b000979 | prose | pages [20] -->
Automobile-related business will provide considerable jobs for the society. The

<!-- b000980 | furniture | pages [20] -->


<!-- b000981 | prose | pages [20] -->
potential new business may consist of the jobs in electrical power station, electrical charging station, and automobile manufacture industry. Therefore, we establish the following formula to predict the total quantity of jobs related with automobile.

<!-- b000982 | furniture | pages [20] -->


<!-- b000983 | prose | pages [20] -->
= ⋅ + H t h n t ( ) ( ) 1 1

<!-- b000984 | prose | pages [20] -->
1h

<!-- b000985 | prose | pages [20] -->
∑ ⋅ + ⋅ h h n t g z t ( ) ( )

<!-- b000986 | furniture | pages [20] -->


<!-- b000987 | furniture | pages [20] -->


<!-- b000988 | furniture | pages [20] -->


<!-- b000989 | furniture | pages [20] -->


<!-- b000990 | prose | pages [20] -->
(14) 2 2 2 i i i

<!-- b000991 | prose | pages [20] -->
is the average quantity of jobs provided by per electrical power station, Where

<!-- b000992 | prose | pages [20] -->
1n t 2h

<!-- b000993 | prose | pages [20] -->
is the quantity of electrical power station in the year, is the average quantity

<!-- b000994 | prose | pages [20] -->
2n

<!-- b000995 | prose | pages [20] -->
of jobs provided by per electrical charging station,

<!-- b000996 | prose | pages [20] -->
t ig

<!-- b000997 | prose | pages [20] -->
is the quantity of electrical

<!-- b000998 | prose | pages [20] -->
i

<!-- b000999 | prose | pages [20] -->
is the average quantity of jobs provided by per charging station in the year,

<!-- b001000 | furniture | pages [20] -->


<!-- b001001 | prose | pages [20] -->
H t ( )

<!-- b001002 | prose | pages [20] -->
vehicle in the t year,

<!-- b001003 | prose | pages [20] -->
iz i

<!-- b001004 | prose | pages [20] -->
vehicle, is the quantity of

<!-- b001005 | prose | pages [20] -->
jobs.

<!-- b001006 | furniture | pages [20] -->


<!-- b001007 | prose | pages [20] -->
is the total quantity of

<!-- b001008 | prose | pages [20] -->
The number of power stations—N1(t)—has been calculated in the chapter 5.3 “Extra Energy Supply for EV/HEV and Its Optimization”. The number of charging

<!-- b001009 | furniture | pages [20] -->


<!-- b001010 | prose | pages [20] -->
12 http://www.repairtrust.com/car_maintenance_costs.html

<!-- b001011 | furniture | pages [20] -->


<!-- b001012 | prose | pages [20] -->
19

<!-- b001013 | furniture | pages [21] -->
Team #8882

<!-- b001014 | furniture | pages [21] -->


<!-- b001015 | furniture | pages [21] -->


<!-- b001016 | furniture | pages [21] -->
Page 20of 27

<!-- b001017 | prose | pages [21] -->
station is limited by their task to supply electricity and provide services. Then we can use the following formula to calculate the quantity of charging stations.

<!-- b001018 | prose | pages [21] -->
z HEV

<!-- b001019 | prose | pages [21] -->
=

<!-- b001020 | prose | pages [21] -->
n t

<!-- b001021 | prose | pages [21] -->
( )

<!-- b001022 | prose | pages [21] -->
2

<!-- b001023 | prose | pages [21] -->
0n

<!-- b001024 | furniture | pages [21] -->


<!-- b001025 | furniture | pages [21] -->


<!-- b001026 | prose | pages [21] -->
1

<!-- b001027 | prose | pages [21] -->
⋅ +

<!-- b001028 | prose | pages [21] -->
t t z t

<!-- b001029 | prose | pages [21] -->
( ) ( ) ( )

<!-- b001030 | prose | pages [21] -->
EV

<!-- b001031 | prose | pages [21] -->
9

<!-- b001032 | furniture | pages [21] -->


<!-- b001033 | furniture | pages [21] -->


<!-- b001034 | furniture | pages [21] -->


<!-- b001035 | furniture | pages [21] -->


<!-- b001036 | furniture | pages [21] -->


<!-- b001037 | furniture | pages [21] -->


<!-- b001038 | prose | pages [21] -->
(15)

<!-- b001039 | prose | pages [21] -->
n

<!-- b001040 | prose | pages [21] -->
0

<!-- b001041 | prose | pages [21] -->
is the average quantity of vehicles that one electrical charging station Where

<!-- b001042 | prose | pages [21] -->
n t

<!-- b001043 | prose | pages [21] -->
is the number of charging stations in t year. can support for and

<!-- b001044 | prose | pages [21] -->
2( )

<!-- b001045 | prose | pages [21] -->
We collect the values of coefficients in this model (some of them are estimated because they are not available on internet) and show them in Table 11.

<!-- b001046 | caption | pages [21] -->
Table 11. Coefficients

<!-- b001047 | furniture | pages [21] -->


<!-- b001048 | prose | pages [21] -->
h1 h2

<!-- b001049 | prose | pages [21] -->
400 5 China

<!-- b001050 | prose | pages [21] -->
200 5 USA

<!-- b001051 | prose | pages [21] -->
400 5 France

<!-- b001052 | furniture | pages [21] -->


<!-- b001053 | prose | pages [21] -->
g1 E0 n0

<!-- b001054 | prose | pages [21] -->
7 5 10 10 1/20

<!-- b001055 | prose | pages [21] -->
7 5 10 10 1/20

<!-- b001056 | prose | pages [21] -->
7 5 10 10 1/20

<!-- b001057 | prose | pages [21] -->
Now we can figure out the newly created jobs by EV and HEV industry in France, USA and France in each year. They are shown in Figure 19.

<!-- b001058 | furniture | pages [21] -->


<!-- b001059 | caption | pages [21] -->
Figure 19. New job positions provided by new industries in France, USA and China.

<!-- b001060 | furniture | pages [21] -->


<!-- b001061 | furniture | pages [21] -->


<!-- b001062 | prose | pages [21] -->
More jobs mean less unemployed people and enhance in family income. It could

<!-- b001063 | furniture | pages [21] -->


<!-- b001064 | prose | pages [21] -->
even affect social stability. That’s why it is a major concern of politicians and economists. In all three countries, the number of jobs that new energy industry would hold in 2060 would account approximately for 10% of their current population. Nevertheless, power stations are expensive to build. So later we will take the effect of new jobs into consideration and see whether the investment in massive construction of power plants is economically worthy.

<!-- b001065 | furniture | pages [21] -->


<!-- b001066 | prose | pages [21] -->
20

<!-- b001067 | furniture | pages [22] -->
Team #8882

<!-- b001068 | furniture | pages [22] -->


<!-- b001069 | furniture | pages [22] -->


<!-- b001070 | furniture | pages [22] -->
Page 21of 27

<!-- b001071 | heading | pages [22] -->
6.4 Invest in New Vehicle Industry is Rewarding

<!-- b001072 | prose | pages [22] -->
Currently big vehicle manufactures are increasing their investment in EV cars.

<!-- b001073 | furniture | pages [22] -->


<!-- b001074 | prose | pages [22] -->
For example, Japanese automaker Nissan plans to invest $642 million into expanding its plant in Sunderland, UK to produce the upcoming LEAF electric sedan as well as lithium-ion batteries for vehicles from Nissan and alliance partner Renault. Ford Motor said its European division will invest $2.3 billion in the development of green car technology, grouped under the company's Econetic brand, over the next five years.13 This reflects the promising future of EV technology. For government that also seeks good-looking economic performance, EV industry will be rewarding other than environmentally beneficial.

<!-- b001075 | furniture | pages [22] -->


<!-- b001076 | prose | pages [22] -->
The previous chapters have shown the economic rewards from EV

<!-- b001077 | furniture | pages [22] -->


<!-- b001078 | prose | pages [22] -->
industry—more jobs and less driving cost for individuals. Now we would consider the input into EV industry. That is to say, what we pay to get the rewards.

<!-- b001079 | furniture | pages [22] -->


<!-- b001080 | prose | pages [22] -->
First of all, when off-peak charging will not suffice the rising number of EV and

<!-- b001081 | furniture | pages [22] -->


<!-- b001082 | prose | pages [22] -->
HEV, new power plants will be established. Second, when EV and HEV prevail in street, facilities like charging station will become a public welfare, just like street phone booth (Although we pay for the phone call, the phone booth is constructed by government). Thus government should also pay for the construction fee for charging stations. Third, as an environmental friendly industry, EV and HEV deserve financial subsidies from government especially in the early stage of its development when costs are relatively high. We consider these three aspects as government responsibilities.

<!-- b001083 | furniture | pages [22] -->


<!-- b001084 | prose | pages [22] -->
Therefore, we establish government investment model shown as follows:

<!-- b001085 | furniture | pages [22] -->


<!-- b001086 | prose | pages [22] -->
= ⋅ cap t p n t ( ) ( ) 1 1 ∑ + + ⋅ + ⋅ p n t s z t ( ) ( )

<!-- b001087 | furniture | pages [22] -->


<!-- b001088 | furniture | pages [22] -->


<!-- b001089 | furniture | pages [22] -->


<!-- b001090 | furniture | pages [22] -->


<!-- b001091 | prose | pages [22] -->
(16) 2 2 i i i

<!-- b001092 | prose | pages [22] -->
1p is the average cost of per electrical power station, Where

<!-- b001093 | prose | pages [22] -->
t

<!-- b001094 | prose | pages [22] -->
of electrical power station in the year,

<!-- b001095 | prose | pages [22] -->
2n

<!-- b001096 | prose | pages [22] -->
1n

<!-- b001097 | prose | pages [22] -->
is the quantity

<!-- b001098 | prose | pages [22] -->
2p is the average cost of per electrical

<!-- b001099 | prose | pages [22] -->
t is

<!-- b001100 | prose | pages [22] -->
is the quantity of electrical charging station in the charging station,

<!-- b001101 | prose | pages [22] -->
i

<!-- b001102 | prose | pages [22] -->
year,

<!-- b001103 | furniture | pages [22] -->


<!-- b001104 | prose | pages [22] -->
iz i

<!-- b001105 | prose | pages [22] -->
vehicle, is the subsidies provided for per

<!-- b001106 | prose | pages [22] -->
t

<!-- b001107 | prose | pages [22] -->
year, cap

<!-- b001108 | prose | pages [22] -->
( )t

<!-- b001109 | prose | pages [22] -->
is the quantity of vehicle in the

<!-- b001110 | prose | pages [22] -->
t

<!-- b001111 | prose | pages [22] -->
is the subsidies provided by the government in the

<!-- b001112 | furniture | pages [22] -->


<!-- b001113 | prose | pages [22] -->
year.

<!-- b001114 | prose | pages [22] -->
We obtain the data needed in this model and list them in Table 12.

<!-- b001115 | furniture | pages [22] -->


<!-- b001116 | furniture | pages [22] -->


<!-- b001117 | furniture | pages [22] -->


<!-- b001118 | prose | pages [22] -->
13 http://www.greenmomentum.com/wb3/wb/gm/gm_content?id_content=5348

<!-- b001119 | furniture | pages [22] -->


<!-- b001120 | prose | pages [22] -->
21

<!-- b001121 | furniture | pages [23] -->
Team #8882

<!-- b001122 | furniture | pages [23] -->


<!-- b001123 | furniture | pages [23] -->


<!-- b001124 | furniture | pages [23] -->
Page 22of 27

<!-- b001125 | caption | pages [23] -->
Table 12. Data needed for (16)

<!-- b001126 | prose | pages [23] -->
Cost of charging

<!-- b001127 | prose | pages [23] -->
Cost per power

<!-- b001128 | furniture | pages [23] -->


<!-- b001129 | prose | pages [23] -->
station

<!-- b001130 | prose | pages [23] -->
station

<!-- b001131 | prose | pages [23] -->
Subsidy on each

<!-- b001132 | prose | pages [23] -->
Salary per

<!-- b001133 | prose | pages [23] -->
EV/HEV

<!-- b001134 | prose | pages [23] -->
year 1.67×105€ 0.167×108€ France 1.5×108$ 10×105$ USA €9000 €2,4770 $10000 $37,610 10×106RMB 10×108RMB China

<!-- b001135 | furniture | pages [23] -->


<!-- b001136 | prose | pages [23] -->
80000 RMB $1100

<!-- b001137 | prose | pages [23] -->
The result of government investment in each year is shown in Figure 20.

<!-- b001138 | furniture | pages [23] -->


<!-- b001139 | caption | pages [23] -->
Figure 20. Investment for EV/HEV in France, USA and China

<!-- b001140 | furniture | pages [23] -->


<!-- b001141 | furniture | pages [23] -->


<!-- b001142 | prose | pages [23] -->
With the investment known, we will compare it with the outcome. That is, the benefits of more jobs and lower driving cost. As the investment has been measured in terms of money, we would also measure such benefits in the same way. The economic benefits of EV/HEV consist of two major aspects. The first one is extra job opportunities created by more power stations and charging stations. We will measure this effect by calculating the total salary provided by these jobs. The second one is savings of each EV or HEV that has been discussed in chapter 7.1 “Driving EV and HEV Costs Less”. We know driving electrically will annually save 1156, 510 and 689 dollars in France, USA and China respectively. We have also predicted the number of EV and HEV in these countries. Thus the totally saving from driving EV/HEV could be figured out.

<!-- b001143 | prose | pages [23] -->
= Output t ( )

<!-- b001144 | prose | pages [23] -->
R t is the input-output ratio, Where ( )

<!-- b001145 | prose | pages [23] -->
cap t

<!-- b001146 | prose | pages [23] -->
∑ ⋅ + Δ ⋅ w H t p z t (17) ( ) ( )

<!-- b001147 | furniture | pages [23] -->


<!-- b001148 | furniture | pages [23] -->


<!-- b001149 | furniture | pages [23] -->


<!-- b001150 | furniture | pages [23] -->


<!-- b001151 | prose | pages [23] -->
i i i

<!-- b001152 | prose | pages [23] -->
Δ ip is the average wage per job, is w

<!-- b001153 | prose | pages [23] -->
is the subsidies provided by the government the saving of driving per vehicle,

<!-- b001154 | prose | pages [23] -->
( )

<!-- b001155 | prose | pages [23] -->
t H t ( )

<!-- b001156 | prose | pages [23] -->
is the total quantity of jobs. in the year,

<!-- b001157 | furniture | pages [23] -->


<!-- b001158 | prose | pages [23] -->
The average salary in France, USA and China is €2,4770, $37,610 and $1100. Then the outcome is shown in Figure 21.

<!-- b001159 | furniture | pages [23] -->


<!-- b001160 | prose | pages [23] -->
22

<!-- b001161 | furniture | pages [24] -->
Team #8882

<!-- b001162 | furniture | pages [24] -->


<!-- b001163 | furniture | pages [24] -->
Page 23of 27

<!-- b001164 | furniture | pages [24] -->


<!-- b001165 | caption | pages [24] -->
Figure 21. Monetary output of new industries in France, USA and China

<!-- b001166 | furniture | pages [24] -->


<!-- b001167 | prose | pages [24] -->
If we compare Figure 21 and Figure 20, we could be find out the output exceeds the input greatly. Thus, it is rewarding to invest in industries related to EV/HEV.

<!-- b001168 | heading | pages [24] -->
6.5 EV/HEV Reduce Pollutions and Do Good for Health

<!-- b001169 | prose | pages [24] -->
Driving a car (CV) is the most air polluting act an average citizen commits.14 The

<!-- b001170 | furniture | pages [24] -->


<!-- b001171 | prose | pages [24] -->
exhaust from CV will poison the air we breath, help spread disease from airborne pathogens and particles. The CO2 emission will also change interactions between the atmosphere and sun, weather effects, effects on plants and oceans. Here we only consider the short term effects of introducing EV and HEV. We select several indicators of human health. Then simulate how they will change with EV and without EV. By comparison the effect of EV could be revealed.

<!-- b001172 | furniture | pages [24] -->


<!-- b001173 | furniture | pages [24] -->


<!-- b001174 | prose | pages [24] -->
Nitrogen is a major component of exhaust and known to cause several health effects:15

<!-- b001175 | prose | pages [24] -->
z Reactions with hemoglobin in blood, causing the oxygen carrying capacity of

<!-- b001176 | prose | pages [24] -->
the blood to decrease (nitrite) z Decreased functioning of the thyroid gland (nitrate) z Vitamin A shortages (nitrate) z Fashioning of nitro amines, which are known as one of the most common

<!-- b001177 | prose | pages [24] -->
causes of cancer (nitrates and nitrites)

<!-- b001178 | furniture | pages [24] -->


<!-- b001179 | prose | pages [24] -->
Nitrogen is created during combustion. In CV the combustion engine will create nitrogen by burning oil. In thermal power plant, nitrogen will also be created by burning oil. As there is a fixed ratio of CO2 and nitrogen in oil combustion, we could estimate nitrogen the emission of nitrogen easily. The ratio of nitrogen to CO2 generated in oil combustion is 0.685.16 Thus, the nitrogen generation is shown in

<!-- b001180 | caption | pages [24] -->
Figure 22.

<!-- b001181 | furniture | pages [24] -->


<!-- b001182 | prose | pages [24] -->
14 http://www.nutramed.com/environment/cars.htm 15 http://www.lenntech.com/periodic/elements/n.htm 16 http://www.engineeringtoolbox.com/co2-emission-fuels-d_1085.html

<!-- b001183 | furniture | pages [24] -->


<!-- b001184 | prose | pages [24] -->
23

<!-- b001185 | furniture | pages [25] -->
Team #8882

<!-- b001186 | furniture | pages [25] -->


<!-- b001187 | furniture | pages [25] -->


<!-- b001188 | furniture | pages [25] -->
Page 24of 27

<!-- b001189 | furniture | pages [25] -->


<!-- b001190 | caption | pages [25] -->
Figure 22. Nitrogen Generation in France, USA and China

<!-- b001191 | heading | pages [25] -->
7. Conclusion

<!-- b001192 | prose | pages [25] -->
The effects of EV/HEV could be clearly revealed by comparing environmental,

<!-- b001193 | furniture | pages [25] -->


<!-- b001194 | prose | pages [25] -->
social, economic and health impacts between two scenarios. One scenario is where quantities of CV, EV and HEV accord with our simulation. The other one is where all EV/HEV will be replaced by CV. In order to help decision for the whole world, we synthesize the figure in France, USA and China. Results are shown in Figure 23, 24, 25, 26.

<!-- b001195 | caption | pages [25] -->
Figure 23 World’s CO2 emission

<!-- b001196 | furniture | pages [25] -->


<!-- b001197 | furniture | pages [25] -->


<!-- b001198 | furniture | pages [25] -->


<!-- b001199 | furniture | pages [25] -->


<!-- b001200 | furniture | pages [25] -->


<!-- b001201 | furniture | pages [25] -->


<!-- b001202 | furniture | pages [25] -->


<!-- b001203 | caption | pages [25] -->
Figure 24 World’s new job positions

<!-- b001204 | prose | pages [25] -->
24

<!-- b001205 | furniture | pages [26] -->
Team #8882

<!-- b001206 | caption | pages [26] -->
Figure 25 World’s monetary reward

<!-- b001207 | furniture | pages [26] -->


<!-- b001208 | furniture | pages [26] -->


<!-- b001209 | furniture | pages [26] -->


<!-- b001210 | furniture | pages [26] -->


<!-- b001211 | furniture | pages [26] -->
Page 25of 27

<!-- b001212 | furniture | pages [26] -->


<!-- b001213 | furniture | pages [26] -->


<!-- b001214 | furniture | pages [26] -->


<!-- b001215 | furniture | pages [26] -->


<!-- b001216 | caption | pages [26] -->
Figure 26 World’s nitrogen production

<!-- b001217 | prose | pages [26] -->
As we can see from Figure 23, the world with EV/HEV will have less carbon

<!-- b001218 | furniture | pages [26] -->


<!-- b001219 | prose | pages [26] -->
emissions than CV, thus consume less fossil fuel consumption. EV/HEV will also help create more jobs and greater fortune than CV will. In addition, air pollutions will be greatly lowed.

<!-- b001220 | furniture | pages [26] -->


<!-- b001221 | prose | pages [26] -->
“How environmentally and economically sound are electric vehicles?” The

<!-- b001222 | furniture | pages [26] -->


<!-- b001223 | prose | pages [26] -->
answer is very. The indirect consumption of fossil fuels by an EV (or HEV in electric-only mode) is 2.42% of CV in China, 16.2% of CV in USA and 18.1% of that in China. The widespread use of EV/HEV in France and USA will cause immediate drop of fossil fuels consumption. In China, such consumption drop will happen after 2040. Consequently, a significant among of fossil fuels will be saved. What’s more, driving EV/HEV cost little as compared to driving CV in all countries. And there is no big different of driving performance and price between CV and EV. This will attract individuals and facilitate its promotion among public. The market promotion on big scale would be promising.

<!-- b001224 | furniture | pages [26] -->


<!-- b001225 | furniture | pages [26] -->


<!-- b001226 | prose | pages [26] -->
The widespread use of EV/HEV would also be attractive for government. New

<!-- b001227 | furniture | pages [26] -->


<!-- b001228 | prose | pages [26] -->
power industry and EV manufactures would be needed, which would provide more job positions. Our model shows the monetary reward will greatly exceed the investment. In addition, we also model the impact of EV/HEV on air pollutions. Model shows encouraging results in reduction of nitrogen generation that pose a threat to human health. Therefore, if we put together the economic profits in the new industry, the government’s responsibility to conserve fossil fuel energy and protect human health, we think government will strongly support the widespread use of EV/HEV.

<!-- b001229 | furniture | pages [26] -->


<!-- b001230 | furniture | pages [26] -->


<!-- b001231 | prose | pages [26] -->
25

<!-- b001232 | furniture | pages [27] -->
Team #8882

<!-- b001233 | furniture | pages [27] -->


<!-- b001234 | furniture | pages [27] -->
Page 26of 27

<!-- b001235 | heading | pages [27] -->
8. References

<!-- b001236 | references | pages [27] -->
[1] T.J. Wallington, E.W. Kaiser and J.T. Farrell, Automotive fuels and internal

<!-- b001237 | references | pages [27] -->
combustion engines: a chemical perspective, Chem Soc Rev 35 (2005), pp. 335–347.

<!-- b001238 | furniture | pages [27] -->


<!-- b001239 | references | pages [27] -->
[2] Electric Vehicle charge forward by C.C Chan and Y.S. Wong

<!-- b001240 | furniture | pages [27] -->


<!-- b001241 | references | pages [27] -->
[3] http://www.fueleconomy.gov/feg/evtech.shtml

<!-- b001242 | furniture | pages [27] -->


<!-- b001243 | references | pages [27] -->
[4] http://www.carboncounted.co.uk/when-will-fossil-fuels-run-out.html

<!-- b001244 | furniture | pages [27] -->


<!-- b001245 | references | pages [27] -->
[5] Proc. Int. Conf. Urban Electric Vehicle, Stockholm, Sweden, May 1992, OECD,

<!-- b001246 | references | pages [27] -->
IEA, Paris, France.

<!-- b001247 | furniture | pages [27] -->


<!-- b001248 | references | pages [27] -->
[6] Reed T. Doucette ⇑, Malcolm D. McCulloch Modeling the prospects of plug-in

<!-- b001249 | references | pages [27] -->
hybrid electric vehicles to reduce CO2 emissions

<!-- b001250 | furniture | pages [27] -->


<!-- b001251 | references | pages [27] -->
[7] Carfolio. 2010 Ford focus specifications; 2010. <www.carfolio.com> [accessed

<!-- b001252 | references | pages [27] -->
August 2010]

<!-- b001253 | furniture | pages [27] -->


<!-- b001254 | references | pages [27] -->
[8] Universal Charging Station and Method for Charging Electrical Vehicle Batteries

<!-- b001255 | references | pages [27] -->
By Bradley J.Hesse.Syacuse; Philip J.Gentile, East Syracuse, both of N.Y

<!-- b001256 | furniture | pages [27] -->


<!-- b001257 | references | pages [27] -->
[9] Hybrid Electric Vehicle by Alex J.Severinsky, 10904 Pebble Run, Silver Spring,

<!-- b001258 | references | pages [27] -->
Md.20902

<!-- b001259 | furniture | pages [27] -->


<!-- b001260 | references | pages [27] -->
26
