# P-C-2011-11893-6a9ea7d9

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
Because of serious global pollution problems and energy shortages, the study of the environmental and economic effects of developing electric vehicles has become increasingly important. In this paper, we focus on and provide comprehensive solutions to the following issues:  How does tax rate influence the numbers of Conventional Vehicles (CV) and Electric Vehicles (EV)?  What impacts will the replacement of CVs by EVs on oil stock?  What is the upper-limit proportion of EVs under the condition of the present power generation ability? A Static Supply-Demand Model is set up to answer these questions. According to the influence of tax rate on supply-demand relationship, we analyze the change in the demand of CVs over tax rate. Then, we estimate how long the oil will be consumed up by PHEVs using the supply-price relationship. Finally, we provide an estimation of the upper-limit proportion of EVs under the condition of the present power generation ability.  What is the relationship between the change in the numbers of CVs and EVs?  How do factors such as government control, corporation decision influence the change in the numbers of CVs and EVs? We successfully develop a Competing Ordinary Differential Equation Model to solve these problems. We first build up the equations using linear approximation, and then we fit the real data using least-squares principle and get an ordinary differential equation. With the help of the previous Static Supply-Demand Model, we discuss the real meanings of the fitted variables and the interaction between CVs and EVs.  How does the development of EVs influence the environment?  Whether the development of EVs can save fossil fuels?  Whether different types of EVs have the same benefits to environment, energy, or society? To answer these questions, we build up a linear programming model and set minimum environmental cost as the destination. We find the impact of popularizing EVs on the environment. We also demonstrate the advantages and disadvantages of three types of EVs. In the end, we give recommendations for the government on its role to support and guide the development of EVs.

<!-- b000013 | furniture | pages [2] -->
Team#11893                                             Page 1 of 20

<!-- b000014 | prose | pages [2] -->
An Analysis of the Future Development of

<!-- b000015 | prose | pages [2] -->
Electric Vehicles

<!-- b000016 | heading | pages [2] -->
Introduction:

<!-- b000017 | prose | pages [2] -->
Our models and key factors are shown as follows:

<!-- b000018 | furniture | pages [2] -->


<!-- b000019 | prose | pages [2] -->
Fig. 1

<!-- b000020 | prose | pages [2] -->
In accessing the impacts brought from a new commodity, it often involves many connected or unconnected aspects. Electric vehicles (EVs) are considered to be one of the most promising means to alleviate current shortage and unbalance distribution in power demand. However, on the other hand, the widespread use of EVs is constrained or promoted by the economical, social and technical factors. In our model, we analyzed these factors in a system dependently, we also made a comprehensive evaluation of their influence on EVs.

<!-- b000021 | prose | pages [2] -->
To consider the economical factors, we set up a Static Supply-Demand Model (SSDM) in which relations between oil supply, mileage demand and oil price are introduced. A balance point is calculated in this model and tax rate is regarded as an adjustment factor to it. In the PHEVs-dominant market, a new predicted oil-exhausting year is given due to the decreasing consumption of oil. More information of the consumption by resources types and

<!-- b000022 | furniture | pages [3] -->
Team#11893                                             Page 2 of 20

<!-- b000023 | prose | pages [3] -->
purpose is offered in LPM. Further, we also give a simple static estimate for the up-bound of the percentage of PHEVs. A more comprehensive dynamic estimate of it is followed in CM.

<!-- b000024 | prose | pages [3] -->
Thinking over the social and technical factors, a Competing Ordinary Differential Equation Model (CM) is set up. Different types of EVs (BEVs/HEVs/PHEVs) result into different coefficients in ODEs. According to the variations of coefficients, we get different dynamic amount-trend of EVs and CVs. The environmental impaction of different types of EVs is introduced in LPM by different constrains.

<!-- b000025 | prose | pages [3] -->
With regard to the factors of environment and resources, we set up a Linear Programming Model (LPM) for Optimum Energy Distribution. The optimum energy flows of different type resources are given with Energy Flow by Source and Sector Diagram. The result is also affected by the type of EVs according to different combined energy efficient.

<!-- b000026 | heading | pages [3] -->
Static Supply-Demand Model

<!-- b000027 | heading | pages [3] -->
Notations

<!-- b000028 | prose | pages [3] -->
S :Daily oil supply amount in Thousand Barrels per day(TB)

<!-- b000029 | prose | pages [3] -->
D :Yearly vehicle travel demand in Billion Km(BK)

<!-- b000030 | prose | pages [3] -->
P :Oil price in Dollars per Barrel ($/bbI)

<!-- b000031 | prose | pages [3] -->
Smax :Maximum daily oil supply amount

<!-- b000032 | prose | pages [3] -->
Dmin :Minimum yearly vehicle travel demand

<!-- b000033 | prose | pages [3] -->
Smin :Daily oil supply amount except for transportation

<!-- b000034 | prose | pages [3] -->
C :Oil consumption per 100 kilometers in Liter/Hundred Kilometers(L/HK)

<!-- b000035 | prose | pages [3] -->
μ1 :Proportion of oil consumption for transportation

<!-- b000036 | prose | pages [3] -->
μ2 : Efficiency of converting petroleum to gasoline

<!-- b000037 | prose | pages [3] -->
V : Volume of one barrel of oil in liter (L)

<!-- b000038 | prose | pages [3] -->
R : Tax rate

<!-- b000039 | heading | pages [3] -->
Assumptions

<!-- b000040 | prose | pages [3] -->
1． In a buyer’s market (i.e. in such a market, supply is greater than demand), the relationship between market price and consumption reflects the relationship between price and demand.

<!-- b000041 | prose | pages [3] -->
2． In a seller’s market (i.e. in such a market, demand is greater than supply), the relationship between market price and consumption reflects the relationship between price and production.

<!-- b000042 | prose | pages [3] -->
3． Supply-demand relationship is the main factor in determining price, without regard to other factors such as political or economic state.

<!-- b000043 | prose | pages [3] -->
4． The consumption amount of oil will not have direct influence over power generation amount or electricity price.

<!-- b000044 | prose | pages [3] -->
5． The relationships above are independent of time, that is, they will not change over time.

<!-- b000045 | furniture | pages [4] -->
Team#11893                                             Page 3 of 20

<!-- b000046 | heading | pages [4] -->
The Foundation of Model

<!-- b000047 | prose | pages [4] -->
dS S

<!-- b000048 | prose | pages [4] -->
 

<!-- b000049 | prose | pages [4] -->
1( )

<!-- b000050 | prose | pages [4] -->
k

<!-- b000051 | prose | pages [4] -->
1

<!-- b000052 | prose | pages [4] -->
d

<!-- b000053 | prose | pages [4] -->
P

<!-- b000054 | prose | pages [4] -->
S

<!-- b000055 | prose | pages [4] -->
max

<!-- b000056 | prose | pages [4] -->
dD D

<!-- b000057 | prose | pages [4] -->
 

<!-- b000058 | prose | pages [4] -->
k

<!-- b000059 | prose | pages [4] -->
1( )

<!-- b000060 | furniture | pages [4] -->


<!-- b000061 | prose | pages [4] -->
2

<!-- b000062 | prose | pages [4] -->
d

<!-- b000063 | prose | pages [4] -->
P

<!-- b000064 | prose | pages [4] -->
D

<!-- b000065 | prose | pages [4] -->
min

<!-- b000066 | prose | pages [4] -->
 

<!-- b000067 | prose | pages [4] -->
D k

<!-- b000068 | prose | pages [4] -->
(

<!-- b000069 | prose | pages [4] -->
S S

<!-- b000070 | prose | pages [4] -->
)

<!-- b000071 | prose | pages [4] -->
3 min

<!-- b000072 | prose | pages [4] -->
1k 2k

<!-- b000073 | prose | pages [4] -->
are undetermined coefficients. They demonstrate the relationship between Where ,

<!-- b000074 | prose | pages [4] -->
 1 V  k3

<!-- b000075 | prose | pages [4] -->
S,D and P.

<!-- b000076 | prose | pages [4] -->
stands for the travel distance provided by the energy in one

<!-- b000077 | prose | pages [4] -->
2 C

<!-- b000078 | prose | pages [4] -->
   S S 1( ) barrel of oil.

<!-- b000079 | prose | pages [4] -->
. total

<!-- b000080 | prose | pages [4] -->
min

<!-- b000081 | prose | pages [4] -->
1

<!-- b000082 | prose | pages [4] -->
The solutions of the differential equation are:

<!-- b000083 | prose | pages [4] -->


<!-- b000084 | prose | pages [4] -->
 

<!-- b000085 | prose | pages [4] -->
k P S

<!-- b000086 | prose | pages [4] -->
/

<!-- b000087 | prose | pages [4] -->
S S C

<!-- b000088 | prose | pages [4] -->
1

<!-- b000089 | prose | pages [4] -->
e

<!-- b000090 | prose | pages [4] -->
1 max

<!-- b000091 | prose | pages [4] -->
max

<!-- b000092 | prose | pages [4] -->


<!-- b000093 | prose | pages [4] -->
 

<!-- b000094 | prose | pages [4] -->
k P D

<!-- b000095 | prose | pages [4] -->
/

<!-- b000096 | prose | pages [4] -->
D D C

<!-- b000097 | prose | pages [4] -->
2

<!-- b000098 | prose | pages [4] -->
e

<!-- b000099 | furniture | pages [4] -->


<!-- b000100 | prose | pages [4] -->
2 max

<!-- b000101 | prose | pages [4] -->
max

<!-- b000102 | prose | pages [4] -->
 

<!-- b000103 | prose | pages [4] -->
D k

<!-- b000104 | prose | pages [4] -->
(

<!-- b000105 | prose | pages [4] -->
S S

<!-- b000106 | prose | pages [4] -->
)

<!-- b000107 | prose | pages [4] -->
3 min

<!-- b000108 | heading | pages [4] -->
The Solution of the Model

<!-- b000109 | heading | pages [4] -->
1. The determination of variables

<!-- b000110 | prose | pages [4] -->
C =10(L/HK) Conventional oil-fuel car:

<!-- b000111 | prose | pages [4] -->
  = 20% = 72% Hybrid electric car:       C =5(L/HK), V = 159L , ,

<!-- b000112 | furniture | pages [4] -->


<!-- b000113 | prose | pages [4] -->
2 1

<!-- b000114 | prose | pages [4] -->
3  k 0.0458 (BK/TB), while for hybrid In conclusion, for conventional oil-fuel cars,

<!-- b000115 | prose | pages [4] -->
3  k 0.0916 electric cars, (BK/TB).

<!-- b000116 | prose | pages [4] -->
 S 84000 S (TB) (Data in 2009), total

<!-- b000117 | heading | pages [4] -->
2. The fitting of equation

<!-- b000118 | prose | pages [4] -->
min 23520 (TB).

<!-- b000119 | prose | pages [4] -->
When looking at the trend of oil price and oil consumption, we can find that between 1980 and 1994, the oil price went up as production declined, while between 1999 and 2006, the oil price increased as production went up. Therefore, we can take the market as buyer’s market between 1980 and 1994, as seller’s market between 1999 and 2006, and as supply-demand balance market between 1995 and 1998. We use data [Scott M. Festin 1996] between 1980 and 1994 to fit demand-price equation, and use data between 1999 and 2006 to fit supply-price equation. The results are as following:

<!-- b000120 | prose | pages [4] -->
max  min  S 90300 1  636.27 D (TB)

<!-- b000121 | prose | pages [4] -->
2  C  k 13 . 23 1 20859

<!-- b000122 | furniture | pages [4] -->


<!-- b000123 | furniture | pages [4] -->


<!-- b000124 | furniture | pages [4] -->


<!-- b000125 | heading | pages [4] -->
3. The equilibrium points

<!-- b000126 | prose | pages [4] -->
k 2339 (BK)

<!-- b000127 | furniture | pages [4] -->


<!-- b000128 | prose | pages [4] -->
C  2 -3988

<!-- b000129 | furniture | pages [4] -->


<!-- b000130 | furniture | pages [4] -->


<!-- b000131 | furniture | pages [4] -->


<!-- b000132 | furniture | pages [4] -->


<!-- b000133 | prose | pages [4] -->
Returning the values of the variables back to the equations, we can find the equilibrium points of completely employing conventional oil-fuel car or completely employing hybrid electric car:

<!-- b000134 | furniture | pages [5] -->
Team#11893                                             Page 4 of 20

<!-- b000135 | prose | pages [5] -->
Type of Vehicle P($/bbI)

<!-- b000136 | prose | pages [5] -->
PHEV(Plug-in Hybrid

<!-- b000137 | prose | pages [5] -->
17.33

<!-- b000138 | prose | pages [5] -->
Electric Vehicle)

<!-- b000139 | prose | pages [5] -->
CV(Conventional Vehicle) 55.27

<!-- b000140 | prose | pages [5] -->
S(TB) D(BK)

<!-- b000141 | prose | pages [5] -->
76983.19 3417.51

<!-- b000142 | prose | pages [5] -->
85315.55 1899.53

<!-- b000143 | prose | pages [5] -->
Tbl. 1

<!-- b000144 | prose | pages [5] -->
According the data of 2006, our result of CV’s equilibrium point is closed to the realistic value. So this model is reliable basing on above analysis.

<!-- b000145 | prose | pages [5] -->
4000

<!-- b000146 | prose | pages [5] -->
3500

<!-- b000147 | prose | pages [5] -->
3000

<!-- b000148 | prose | pages [5] -->
2500

<!-- b000149 | prose | pages [5] -->
D

<!-- b000150 | prose | pages [5] -->
2000

<!-- b000151 | prose | pages [5] -->
1500

<!-- b000152 | prose | pages [5] -->
1000

<!-- b000153 | prose | pages [5] -->
2

<!-- b000154 | prose | pages [5] -->
2 4 6

<!-- b000155 | furniture | pages [5] -->


<!-- b000156 | prose | pages [5] -->
8

<!-- b000157 | prose | pages [5] -->
4

<!-- b000158 | prose | pages [5] -->
x 10

<!-- b000159 | prose | pages [5] -->
S

<!-- b000160 | furniture | pages [5] -->


<!-- b000161 | prose | pages [5] -->
3 1 1

<!-- b000162 | prose | pages [5] -->
20 40 60 80 100 120 140

<!-- b000163 | prose | pages [5] -->
10

<!-- b000164 | prose | pages [5] -->
P

<!-- b000165 | furniture | pages [5] -->


<!-- b000166 | prose | pages [5] -->
Fig. 2

<!-- b000167 | prose | pages [5] -->
Line 1 and line 2 stand for the relationship between oil price and demand from consumer’s perspective. Line 3 stands for the relationship between oil price and supply amount from supplier’s perspective. Their intersections are equilibrium points. The point denoted by a circle is the equilibrium point of PHEV. The point denoted by a block is the equilibrium point of CV. We can see that if CVs were totally replaced by PHEVs, both the price and demand of oil would decline, while the travel distance would extend under equilibrium.

<!-- b000168 | heading | pages [5] -->
4. PHEV and Tax

<!-- b000169 | heading | pages [5] -->
1) The PHEVs’ impaction on the oil tax

<!-- b000170 | prose | pages [5] -->
A main reason that the government levies high tax on oil is to keep the supply and demand of oil in balance. If we used the PHEVs to replace most of the CVs, the pressure on oil demand would be remarkably relieved. Suppose that the tax rate on oil (R) is in proportion to the oil price (P). By collecting correlating data,We obtain:

<!-- b000171 | prose | pages [5] -->
R

<!-- b000172 | prose | pages [5] -->
  

<!-- b000173 | prose | pages [5] -->
P 13 . 27

<!-- b000174 | prose | pages [5] -->
R

<!-- b000175 | prose | pages [5] -->
HEV HEV

<!-- b000176 | prose | pages [5] -->
P

<!-- b000177 | furniture | pages [5] -->


<!-- b000178 | prose | pages [5] -->
R

<!-- b000179 | prose | pages [5] -->
  

<!-- b000180 | prose | pages [5] -->
P 42 . 38

<!-- b000181 | prose | pages [5] -->
R

<!-- b000182 | prose | pages [5] -->
CV

<!-- b000183 | prose | pages [5] -->
CV

<!-- b000184 | prose | pages [5] -->
P

<!-- b000185 | furniture | pages [6] -->
Team#11893                                             Page 5 of 20

<!-- b000186 | prose | pages [6] -->


<!-- b000187 | prose | pages [6] -->
R S 

<!-- b000188 | prose | pages [6] -->
 

<!-- b000189 | prose | pages [6] -->
HEV HEV

<!-- b000190 | prose | pages [6] -->
The tax rate ratio:

<!-- b000191 | prose | pages [6] -->


<!-- b000192 | prose | pages [6] -->
R S

<!-- b000193 | prose | pages [6] -->
CV CV

<!-- b000194 | prose | pages [6] -->
 100 % 28 . 25 %

<!-- b000195 | furniture | pages [6] -->


<!-- b000196 | prose | pages [6] -->
The calculations above are based on the static supply-demand model, so we did not take into account the impact of tax rate on S-P curve, or the change of D-P curve over time. The result shows that after the employment of PHEVs, under the dual effects of the declination of oil consumption and oil tax rate, the total amount of tax on oil will decrease notably.

<!-- b000197 | prose | pages [6] -->
2)The oil tax’s impaction on the PHEVs

<!-- b000198 | prose | pages [6] -->
In the oil market, the variation of oil tax rate will result in change of the S-P relation. One part of the increasing tax is included in the increasing price of oil, the other part is

<!-- b000199 | prose | pages [6] -->
P

<!-- b000200 | prose | pages [6] -->
balanced with the decreasing profits. We define the

<!-- b000201 | prose | pages [6] -->
 % D

<!-- b000202 | prose | pages [6] -->
price. The sensitivity analysis of

<!-- b000203 | prose | pages [6] -->
as the percentage of increasing oil

<!-- b000204 | prose | pages [6] -->
rise is followed. cv

<!-- b000205 | prose | pages [6] -->
22% 16% P

<!-- b000206 | furniture | pages [6] -->


<!-- b000207 | prose | pages [6] -->
rise 12% 8%

<!-- b000208 | prose | pages [6] -->
-12% -14%  D %

<!-- b000209 | furniture | pages [6] -->


<!-- b000210 | prose | pages [6] -->
cv -8.5% -5.3%

<!-- b000211 | prose | pages [6] -->
Tbl. 2

<!-- b000212 | prose | pages [6] -->
D

<!-- b000213 | prose | pages [6] -->
To balance the demand of travel miles, the decreasing will lead to the rising

<!-- b000214 | prose | pages [6] -->
cv

<!-- b000215 | prose | pages [6] -->
demand of PHEVs. As a result, enhancing the oil tax rate will promote the widespread use of PHEVs.

<!-- b000216 | heading | pages [6] -->
5. Impact on oil stock

<!-- b000217 | prose | pages [6] -->
In the above, we only considered the impact of supply-demand relationship on price. From the results we have obtained, we know that using PHEVs fails to remarkably decrease the consumption of oil (76983.19 VS 85315.55), but we can also see that after using PHEVs, the same amount of oil consumption could meet larger demand. Therefore, in order to balance the oil consumption, we define the consuming efficiency of oil as the travel distance demand satisfied when consuming one unit of oil:

<!-- b000218 | prose | pages [6] -->
 ） D / 365 S （

<!-- b000219 | furniture | pages [6] -->


<!-- b000220 | prose | pages [6] -->
From data we know:

<!-- b000221 | prose | pages [6] -->
More travel distance it can still supply:

<!-- b000222 | prose | pages [6] -->


<!-- b000223 | prose | pages [6] -->


<!-- b000224 | prose | pages [6] -->
   

<!-- b000225 | prose | pages [6] -->
4

<!-- b000226 | prose | pages [6] -->
D

<!-- b000227 | prose | pages [6] -->
/ 356

<!-- b000228 | prose | pages [6] -->
S

<!-- b000229 | prose | pages [6] -->
.1 25 10

<!-- b000230 | prose | pages [6] -->
（ ）

<!-- b000231 | prose | pages [6] -->
HEV SEV HEV

<!-- b000232 | furniture | pages [6] -->


<!-- b000233 | prose | pages [6] -->


<!-- b000234 | prose | pages [6] -->


<!-- b000235 | prose | pages [6] -->
   

<!-- b000236 | prose | pages [6] -->
5

<!-- b000237 | prose | pages [6] -->
D

<!-- b000238 | prose | pages [6] -->
/ 356

<!-- b000239 | prose | pages [6] -->
S

<!-- b000240 | prose | pages [6] -->
.6 26 10

<!-- b000241 | prose | pages [6] -->
（ ）

<!-- b000242 | prose | pages [6] -->
CV CV CV

<!-- b000243 | prose | pages [6] -->
 6 S = 1,143.355 10 TB (2007) reserve

<!-- b000244 | prose | pages [6] -->
 

<!-- b000245 | prose | pages [6] -->


<!-- b000246 | prose | pages [6] -->
 

<!-- b000247 | prose | pages [6] -->
5

<!-- b000248 | prose | pages [6] -->
D

<!-- b000249 | prose | pages [6] -->
(

<!-- b000250 | prose | pages [6] -->
total

<!-- b000251 | prose | pages [6] -->
)

<!-- b000252 | prose | pages [6] -->
S

<!-- b000253 | prose | pages [6] -->
.1 42 10

<!-- b000254 | prose | pages [6] -->
SEV reserve HEV

<!-- b000255 | furniture | pages [6] -->


<!-- b000256 | prose | pages [6] -->


<!-- b000257 | prose | pages [6] -->
   

<!-- b000258 | prose | pages [6] -->
4

<!-- b000259 | prose | pages [6] -->
D

<!-- b000260 | prose | pages [6] -->
(

<!-- b000261 | prose | pages [6] -->
total

<!-- b000262 | prose | pages [6] -->
)

<!-- b000263 | prose | pages [6] -->
S

<!-- b000264 | prose | pages [6] -->
.7 16 10

<!-- b000265 | prose | pages [6] -->
CV reserve CV

<!-- b000266 | furniture | pages [7] -->
Team#11893                                             Page 6 of 20

<!-- b000267 | prose | pages [7] -->
5

<!-- b000268 | prose | pages [7] -->
x 10 7

<!-- b000269 | prose | pages [7] -->
6

<!-- b000270 | prose | pages [7] -->
Accumulative D from 1980

<!-- b000271 | prose | pages [7] -->
5

<!-- b000272 | prose | pages [7] -->
4

<!-- b000273 | prose | pages [7] -->
3

<!-- b000274 | prose | pages [7] -->
D(HEV)

<!-- b000275 | prose | pages [7] -->
D(CV)

<!-- b000276 | prose | pages [7] -->
2

<!-- b000277 | prose | pages [7] -->
1

<!-- b000278 | prose | pages [7] -->
0

<!-- b000279 | furniture | pages [7] -->


<!-- b000280 | prose | pages [7] -->
1980 1990 2000 2010

<!-- b000281 | furniture | pages [7] -->


<!-- b000282 | prose | pages [7] -->
2020 2030 2040 2050 2060 2070

<!-- b000283 | prose | pages [7] -->
year

<!-- b000284 | furniture | pages [7] -->


<!-- b000285 | prose | pages [7] -->
Fig. 3

<!-- b000286 | prose | pages [7] -->
From the figure above we can see that according to the present trend of demand, completely using CVs will consume up present oil stock in 2020, while completely using CVs will consume up present oil stock in 2029.

<!-- b000287 | heading | pages [7] -->
6. Computation of Electricity Margin

<!-- b000288 | prose | pages [7] -->
Reasonably, the increasing widespread use of electricity vehicles will lead to the rising of electricity consumption. However, the realistic amount of EVs has a up bound due to the limitation of total electricity installed capacity.

<!-- b000289 | prose | pages [7] -->
We defineas the rate of electricity generation (i.e., the ratio of total electricity production to total installed capacity times working hours):

<!-- b000290 | prose | pages [7] -->
total

<!-- b000291 | furniture | pages [7] -->


<!-- b000292 | prose | pages [7] -->
electricit y production

<!-- b000293 | prose | pages [7] -->


<!-- b000294 | prose | pages [7] -->
  

<!-- b000295 | prose | pages [7] -->
i denotes the type

<!-- b000296 | furniture | pages [7] -->


<!-- b000297 | prose | pages [7] -->
of

<!-- b000298 | furniture | pages [7] -->


<!-- b000299 | prose | pages [7] -->
electricit y generation

<!-- b000300 | furniture | pages [7] -->


<!-- b000301 | prose | pages [7] -->
，

<!-- b000302 | prose | pages [7] -->
capacity working

<!-- b000303 | furniture | pages [7] -->


<!-- b000304 | prose | pages [7] -->
hours installed

<!-- b000305 | furniture | pages [7] -->


<!-- b000306 | prose | pages [7] -->
i

<!-- b000307 | prose | pages [7] -->
i

<!-- b000308 | prose | pages [7] -->
i

<!-- b000309 | prose | pages [7] -->
We made the assumption that the power plants except for thermal ones work under full load, which means they work 24 hours per day (hpd). The-year curve is the upper one in Fig. 4 when there is no additional production of thermal electricity, the middle one when thermal power plants work 16 hpd, the lower one when thermal power plants work 20 hpd. Fig. 4 shows the rise of electricity demand.

<!-- b000310 | prose | pages [7] -->
0.9

<!-- b000311 | prose | pages [7] -->
0.85

<!-- b000312 | prose | pages [7] -->
Percentage of Electricity Capacity

<!-- b000313 | prose | pages [7] -->
0.8

<!-- b000314 | prose | pages [7] -->
0.75

<!-- b000315 | prose | pages [7] -->
0.7

<!-- b000316 | prose | pages [7] -->
0.65

<!-- b000317 | prose | pages [7] -->
0.6

<!-- b000318 | prose | pages [7] -->
0.55

<!-- b000319 | prose | pages [7] -->
0.5

<!-- b000320 | furniture | pages [7] -->


<!-- b000321 | prose | pages [7] -->
1980 1985 1990

<!-- b000322 | furniture | pages [7] -->


<!-- b000323 | prose | pages [7] -->
no additional thermal electricity 20hpd full load 16hpd full load

<!-- b000324 | prose | pages [7] -->
1995 2000 2005 2010

<!-- b000325 | prose | pages [7] -->
year

<!-- b000326 | furniture | pages [7] -->


<!-- b000327 | prose | pages [7] -->
Fig. 4

<!-- b000328 | prose | pages [7] -->
To access the capacity of producing additional electricity, we define as the electricity  1   margin:

<!-- b000329 | furniture | pages [7] -->


<!-- b000330 | furniture | pages [8] -->
Team#11893                                             Page 7 of 20

<!-- b000331 | prose | pages [8] -->
Thermal electricity No additional

<!-- b000332 | prose | pages [8] -->
averagefrom 2002 to 2006 12%

<!-- b000333 | prose | pages [8] -->
16phd full load 20phd full load

<!-- b000334 | prose | pages [8] -->
28% 42%

<!-- b000335 | prose | pages [8] -->
Tbl. 3

<!-- b000336 | furniture | pages [8] -->


<!-- b000337 | prose | pages [8] -->
Fig. 5

<!-- b000338 | prose | pages [8] -->
Source: Lawrence Berkeley National Laboratory

<!-- b000339 | prose | pages [8] -->
http://www.mpoweruk.com/electricity_demand.htm

<!-- b000340 | caption | pages [8] -->
Fig. 5 is the electricity daily demand:(1)As to the BEVs, their endurance mileage is

<!-- b000341 | prose | pages [8] -->
relatively small so that a part of their charging would be in on-peak hours(daytime, especially at noon). The electricity margin of BEVs is small because the electricity generation in on-peak hours is nearly under full load. We set it to be the  under 16 phd; (2)As to the PHEVs, because of their longer endurance mileage, most of their charging world be in off-peak hours when the utilization of electricity is much lower than it in on-peak hours. In this sense, their electricity margin is larger. We set it to be the  under 20 phd. These two margins will be used in LPM

<!-- b000342 | prose | pages [8] -->
Without additional thermal electricity generation, we calculated the ratio of PHEVs to total vehicles and the ratio of CVs to total vehicles at the Critical point (upper bound) of

<!-- b000343 | prose | pages [8] -->
3k

<!-- b000344 | prose | pages [8] -->
electricity margin. The result is 38.5% and 61.5% respectively. The coefficient accordingly.

<!-- b000345 | prose | pages [8] -->
Type of Vehicle P($/bbI)

<!-- b000346 | prose | pages [8] -->
38.5%PHEV and 61.5%CV 36

<!-- b000347 | prose | pages [8] -->
is 0.0634

<!-- b000348 | prose | pages [8] -->
S(TB) D(BK)

<!-- b000349 | prose | pages [8] -->
82000 2520

<!-- b000350 | prose | pages [8] -->
Tbl. 4

<!-- b000351 | prose | pages [8] -->
The result shows that present thermal power generation amount will limit the number of electric cars. If we want to further popularize electric cars, we need to generate more electricity, which will lead to more new energy demand or more pollution. To comprehensively access the impact of using more fossil fuels to generate electricity on environment, we need analyze how to choose and arrange the types of power generation so that the pollution will be the least. We will give an analysis in LPM. As shown above, here we give a static upper bound of the PHEVs’ percentage. To have a dynamic result of the amount of CVs and different type EVs, we set up following Competition Model.

<!-- b000352 | furniture | pages [9] -->
Team#11893                                             Page 8 of 20

<!-- b000353 | heading | pages [9] -->
Competing Ordinary Differential Equation Model

<!-- b000354 | heading | pages [9] -->
Notations

<!-- b000355 | prose | pages [9] -->
1x : The total number of electric cars

<!-- b000356 | prose | pages [9] -->
2x : The total number of all kinds of cars (conventional cars)

<!-- b000357 | prose | pages [9] -->
ia :The influential parameter

<!-- b000358 | prose | pages [9] -->
ib : The influential parameter

<!-- b000359 | prose | pages [9] -->
W :Covering rate of infrastructure

<!-- b000360 | prose | pages [9] -->
S :Endurance mileage

<!-- b000361 | prose | pages [9] -->
E

<!-- b000362 | furniture | pages [9] -->


<!-- b000363 | prose | pages [9] -->
:Maximum power generation ability max

<!-- b000364 | heading | pages [9] -->
Basic Assumptions

<!-- b000365 | prose | pages [9] -->
1.

<!-- b000366 | prose | pages [9] -->
Electric cars mainly refer to hybrid electric cars.

<!-- b000367 | prose | pages [9] -->
2b are constants, because they are determined by the specifications 1a , 2a , 1b , 2. of the cars themselves instead of exterior factors.

<!-- b000368 | prose | pages [9] -->
0b will change according to exterior factors. 0a , 3.

<!-- b000369 | heading | pages [9] -->
The Foundation of Ordinary Differential Equation Model

<!-- b000370 | prose | pages [9] -->
We build the model below to analyze the relationship of quantity change between conventional and electric cars. The model is based on a two-element ordinary differential equation:

<!-- b000371 | prose | pages [9] -->


<!-- b000372 | prose | pages [9] -->
dx

<!-- b000373 | prose | pages [9] -->
  

<!-- b000374 | prose | pages [9] -->
1

<!-- b000375 | prose | pages [9] -->
a a x a x

<!-- b000376 | prose | pages [9] -->


<!-- b000377 | prose | pages [9] -->
0 1 1 2 2

<!-- b000378 | prose | pages [9] -->
dt

<!-- b000379 | prose | pages [9] -->


<!-- b000380 | furniture | pages [9] -->


<!-- b000381 | prose | pages [9] -->
dx

<!-- b000382 | prose | pages [9] -->


<!-- b000383 | prose | pages [9] -->
  

<!-- b000384 | prose | pages [9] -->
2

<!-- b000385 | prose | pages [9] -->
b b x b x

<!-- b000386 | prose | pages [9] -->
0 1 1 2 2

<!-- b000387 | prose | pages [9] -->


<!-- b000388 | prose | pages [9] -->
dt

<!-- b000389 | prose | pages [9] -->
dx1 is the change rate of the total of electric cars

<!-- b000390 | prose | pages [9] -->
where dt

<!-- b000391 | prose | pages [9] -->
2x

<!-- b000392 | prose | pages [9] -->
dx2 is the change rate 1x , dt

<!-- b000393 | prose | pages [9] -->
. Because we do not know the exact relations of the total of conventional cars

<!-- b000394 | prose | pages [9] -->
dx1 ,

<!-- b000395 | prose | pages [9] -->
1x x2

<!-- b000396 | prose | pages [9] -->
, here we follow the engineers’ advice: Using linear relation where and

<!-- b000397 | prose | pages [9] -->
between

<!-- b000398 | prose | pages [9] -->
dt

<!-- b000399 | prose | pages [9] -->
you don’t know the exact relation.

<!-- b000400 | prose | pages [9] -->
2a 1a 2b 1b 0a

<!-- b000401 | prose | pages [9] -->
In this equation group, the meanings of unknown parameters

<!-- b000402 | prose | pages [9] -->
0b

<!-- b000403 | prose | pages [9] -->
are :

<!-- b000404 | prose | pages [9] -->
, , , , ,

<!-- b000405 | prose | pages [9] -->
Correlated coefficient of change rate of the total number of electric cars, 2a which is determined by factors such as competition between two types of cars, etc.

<!-- b000406 | prose | pages [9] -->
Coefficient of change rate of the total number of electric cars, which is 1a determined by factors such as the saturation of electric car market, etc.

<!-- b000407 | furniture | pages [10] -->
Team#11893                                             Page 9 of 20

<!-- b000408 | prose | pages [10] -->
Change rate of the total number of electric cars, which is determined by other 0a factors such as the fluctuation of electricity price, etc.

<!-- b000409 | prose | pages [10] -->
Coefficient of change rate of the total number of conventional cars, which is 2b determined by factors such as the saturation of conventional car market, etc.

<!-- b000410 | prose | pages [10] -->
Correlated coefficient of change rate of the total number of conventional cars, 1b which is determined by factors such as competition between two types of cars, the impact of the popularization of electric cars on conventional cars, etc.

<!-- b000411 | prose | pages [10] -->
Change rate of the total number of conventional cars, which is determined by 0b other factors such as the fluctuation of fuel price, etc.

<!-- b000412 | prose | pages [10] -->
Tbl. 5

<!-- b000413 | prose | pages [10] -->
The steady solution of the ODE above is:

<!-- b000414 | prose | pages [10] -->


<!-- b000415 | prose | pages [10] -->


<!-- b000416 | prose | pages [10] -->
a b a b

<!-- b000417 | prose | pages [10] -->


<!-- b000418 | prose | pages [10] -->
2 0 0 2

<!-- b000419 | prose | pages [10] -->
x

<!-- b000420 | prose | pages [10] -->


<!-- b000421 | prose | pages [10] -->


<!-- b000422 | prose | pages [10] -->
1

<!-- b000423 | prose | pages [10] -->


<!-- b000424 | prose | pages [10] -->
a b a b

<!-- b000425 | prose | pages [10] -->
1 2 2 1

<!-- b000426 | prose | pages [10] -->


<!-- b000427 | furniture | pages [10] -->


<!-- b000428 | prose | pages [10] -->


<!-- b000429 | prose | pages [10] -->
a b a b

<!-- b000430 | prose | pages [10] -->


<!-- b000431 | prose | pages [10] -->


<!-- b000432 | prose | pages [10] -->
0 1 1 0

<!-- b000433 | prose | pages [10] -->
x

<!-- b000434 | prose | pages [10] -->


<!-- b000435 | prose | pages [10] -->
2

<!-- b000436 | prose | pages [10] -->


<!-- b000437 | prose | pages [10] -->


<!-- b000438 | prose | pages [10] -->
a b a b

<!-- b000439 | prose | pages [10] -->


<!-- b000440 | prose | pages [10] -->
1 2 2 1

<!-- b000441 | heading | pages [10] -->
The Solution of the Previous Model

<!-- b000442 | prose | pages [10] -->
According to the data in Appendix_2,and from the theory of ordinary differential equation, we can deduce the solutions of the equations have the forms below:

<!-- b000443 | prose | pages [10] -->


<!-- b000444 | prose | pages [10] -->
  

<!-- b000445 | prose | pages [10] -->
t

<!-- b000446 | prose | pages [10] -->
x m m L

<!-- b000447 | prose | pages [10] -->
1 0 1

<!-- b000448 | prose | pages [10] -->


<!-- b000449 | furniture | pages [10] -->


<!-- b000450 | prose | pages [10] -->
  

<!-- b000451 | prose | pages [10] -->
t

<!-- b000452 | prose | pages [10] -->
x n n L

<!-- b000453 | prose | pages [10] -->


<!-- b000454 | prose | pages [10] -->
2 0 1

<!-- b000455 | prose | pages [10] -->
By using least squares fitting, we obtain

<!-- b000456 | prose | pages [10] -->


<!-- b000457 | prose | pages [10] -->
    

<!-- b000458 | prose | pages [10] -->
6 6

<!-- b000459 | prose | pages [10] -->
x

<!-- b000460 | prose | pages [10] -->
.1 272 10 .1 673 10 .0

<!-- b000461 | prose | pages [10] -->
1

<!-- b000462 | prose | pages [10] -->


<!-- b000463 | prose | pages [10] -->
    

<!-- b000464 | prose | pages [10] -->
8 7

<!-- b000465 | prose | pages [10] -->
x

<!-- b000466 | prose | pages [10] -->
.2 592 10 .3 921 10 .0

<!-- b000467 | prose | pages [10] -->


<!-- b000468 | prose | pages [10] -->
2

<!-- b000469 | prose | pages [10] -->
1    7 a .1 741 a .1 910 10 Thus, , 0

<!-- b000470 | prose | pages [10] -->
  103   9 2 b b .1 10 b .1 347 10 , , 2 0 1

<!-- b000471 | heading | pages [10] -->
Validation of a1,b1, a2,b2

<!-- b000472 | prose | pages [10] -->
1 

<!-- b000473 | prose | pages [10] -->
1 

<!-- b000474 | prose | pages [10] -->
a 0

<!-- b000475 | prose | pages [10] -->
b 0

<!-- b000476 | prose | pages [10] -->
t

<!-- b000477 | prose | pages [10] -->
8294

<!-- b000478 | furniture | pages [10] -->


<!-- b000479 | prose | pages [10] -->
t

<!-- b000480 | prose | pages [10] -->
8294

<!-- b000481 | prose | pages [10] -->
  a .0 0822 , ,

<!-- b000482 | prose | pages [10] -->
,

<!-- b000483 | prose | pages [10] -->
2

<!-- b000484 | prose | pages [10] -->
 

<!-- b000485 | prose | pages [10] -->
.4 915

<!-- b000486 | prose | pages [10] -->
.

<!-- b000487 | prose | pages [10] -->
shows that the use of electric cars will promote the use of both , conventional cars and electric cars. According to the static supply-demand balance model, the use of electric cars can lower the oil price, which leads to the decline of the using cost of both electric cars and conventional cars. The decline of fuel fee further motivates the demand in the car market.

<!-- b000488 | prose | pages [10] -->
2 

<!-- b000489 | prose | pages [10] -->
2 

<!-- b000490 | prose | pages [10] -->
a

<!-- b000491 | prose | pages [10] -->
b 0

<!-- b000492 | prose | pages [10] -->
0 demonstrates that the use of conventional oil-fuel cars will restrict the , demand in the car market. The reason is also based on the static supply-demand balance model: the use of conventional oil-fuel cars will raise the oil price, which is negative for the demand.

<!-- b000493 | prose | pages [10] -->
We can draw a figure to show the result:

<!-- b000494 | furniture | pages [11] -->
Team#11893                                             Page 10 of 20

<!-- b000495 | prose | pages [11] -->
8 2.6 x 10

<!-- b000496 | prose | pages [11] -->
2.55

<!-- b000497 | prose | pages [11] -->
2.5

<!-- b000498 | prose | pages [11] -->
Number of Ordinary Cars

<!-- b000499 | prose | pages [11] -->
2.45

<!-- b000500 | prose | pages [11] -->
2.4

<!-- b000501 | prose | pages [11] -->
2.35

<!-- b000502 | prose | pages [11] -->
2.3

<!-- b000503 | prose | pages [11] -->
2.25

<!-- b000504 | prose | pages [11] -->
2.2

<!-- b000505 | prose | pages [11] -->
2.15

<!-- b000506 | furniture | pages [11] -->


<!-- b000507 | furniture | pages [11] -->


<!-- b000508 | prose | pages [11] -->
fitting curve real data

<!-- b000509 | prose | pages [11] -->
1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019

<!-- b000510 | prose | pages [11] -->
8

<!-- b000511 | prose | pages [11] -->
x 10 3

<!-- b000512 | prose | pages [11] -->
2.5

<!-- b000513 | prose | pages [11] -->
2

<!-- b000514 | prose | pages [11] -->
Number of Cars

<!-- b000515 | prose | pages [11] -->
1.5

<!-- b000516 | prose | pages [11] -->
1

<!-- b000517 | prose | pages [11] -->
0.5

<!-- b000518 | prose | pages [11] -->
0

<!-- b000519 | furniture | pages [11] -->


<!-- b000520 | prose | pages [11] -->
1999 2000 2001 2002 2003 2004 2005 2006

<!-- b000521 | prose | pages [11] -->
Years

<!-- b000522 | furniture | pages [11] -->


<!-- b000523 | prose | pages [11] -->
Fig. 6

<!-- b000524 | furniture | pages [11] -->


<!-- b000525 | prose | pages [11] -->
Estimated Number of Electric Cars Estimated Number of Ordinary Cars Real Data of Electric Cars Real Data of Ordinary Cars

<!-- b000526 | prose | pages [11] -->
2007 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019

<!-- b000527 | prose | pages [11] -->
Year

<!-- b000528 | furniture | pages [11] -->


<!-- b000529 | prose | pages [11] -->
Fig. 7

<!-- b000530 | prose | pages [11] -->
The first figure gives a proof of the soundness of the model and the fitting variables. The second figure shows that the amount of conventional cars and electric cars will increase to a fixed value, not infinity. This is in accord with the fact.

<!-- b000531 | prose | pages [11] -->
Discussions about Parameters a0,b0

<!-- b000532 | prose | pages [11] -->
a and

<!-- b000533 | prose | pages [11] -->
0b

<!-- b000534 | prose | pages [11] -->
are constants which are criteria for the competitive ability of cars 0 determined by factors such as technology level, infrastructures, and policies, etc. Because

<!-- b000535 | prose | pages [11] -->
0b

<!-- b000536 | prose | pages [11] -->
technologies and infrastructures of conventional cars have been determined firmly, not change a lot.

<!-- b000537 | prose | pages [11] -->
a

<!-- b000538 | prose | pages [11] -->
will

<!-- b000539 | prose | pages [11] -->
, we can suppose it has the form as below: As for 0

<!-- b000540 | prose | pages [11] -->
a  k WSE

<!-- b000541 | furniture | pages [11] -->


<!-- b000542 | prose | pages [11] -->
0 max

<!-- b000543 | prose | pages [11] -->
k W

<!-- b000544 | prose | pages [11] -->
is an undetermined coefficient. Where

<!-- b000545 | prose | pages [11] -->
W  0 1

<!-- b000546 | prose | pages [11] -->
infrastructures of electric cars (

<!-- b000547 | prose | pages [11] -->
E

<!-- b000548 | prose | pages [11] -->
by battery and charging technology.

<!-- b000549 | prose | pages [11] -->
max

<!-- b000550 | prose | pages [11] -->
is named as the covering rate of the

<!-- b000551 | prose | pages [11] -->
S

<!-- b000552 | prose | pages [11] -->
). ).

<!-- b000553 | prose | pages [11] -->
is the endurance mileage, which is determined is the maximum power generation ability. It will exert restriction or motivation on electric cars.

<!-- b000554 | furniture | pages [12] -->
Team#11893                                             Page 11 of 20

<!-- b000555 | heading | pages [12] -->
Sensitivity analysis of a0 on electric cars :

<!-- b000556 | prose | pages [12] -->
7

<!-- b000557 | prose | pages [12] -->
x 10 3

<!-- b000558 | prose | pages [12] -->
2.5

<!-- b000559 | prose | pages [12] -->
2

<!-- b000560 | prose | pages [12] -->
x1

<!-- b000561 | prose | pages [12] -->
1.5

<!-- b000562 | prose | pages [12] -->
1

<!-- b000563 | prose | pages [12] -->
0.5

<!-- b000564 | prose | pages [12] -->
0

<!-- b000565 | furniture | pages [12] -->


<!-- b000566 | prose | pages [12] -->
0 10 20 30 40

<!-- b000567 | prose | pages [12] -->
a

<!-- b000568 | furniture | pages [12] -->


<!-- b000569 | prose | pages [12] -->
a0'=a0 a0'=1.1*a0 a0'=1.2*a0 a0'=1.3*a0 a0'=1.4*a0 a0'=1.5*a0

<!-- b000570 | prose | pages [12] -->
50 60 70 80 90 100

<!-- b000571 | prose | pages [12] -->
t

<!-- b000572 | furniture | pages [12] -->


<!-- b000573 | prose | pages [12] -->
Fig. 8

<!-- b000574 | prose | pages [12] -->
represents more competitiveness of EVs or more As shown in figure*, larger

<!-- b000575 | prose | pages [12] -->
0

<!-- b000576 | prose | pages [12] -->
coverage of infrastructures, that is to say,

<!-- b000577 | prose | pages [12] -->
a

<!-- b000578 | prose | pages [12] -->
includes the information about EVs’ type.

<!-- b000579 | prose | pages [12] -->
0

<!-- b000580 | prose | pages [12] -->
Competitiveness of EVs mainly includes the technique and the pollution. The more

<!-- b000581 | prose | pages [12] -->
a

<!-- b000582 | prose | pages [12] -->
friendliness to environment, the more support from government will be given, so will be

<!-- b000583 | prose | pages [12] -->
0

<!-- b000584 | prose | pages [12] -->
larger. To access the environment impact of different type EVs, a model to optimize energy distribution is followed.

<!-- b000585 | heading | pages [12] -->
Linear Programming Model for Optimum Energy

<!-- b000586 | prose | pages [12] -->
Distribution

<!-- b000587 | heading | pages [12] -->
Notations

<!-- b000588 | prose | pages [12] -->
ijx : Energy transferred from Supply Source i to Demand Sector j

<!-- b000589 | prose | pages [12] -->
: Energy transferred from Electric Power sector to Transportation sector after

<!-- b000590 | prose | pages [12] -->
cx

<!-- b000591 | prose | pages [12] -->
the popularization of electric cars

<!-- b000592 | prose | pages [12] -->
B : Energy Demand Sector j j

<!-- b000593 | prose | pages [12] -->
iA : Energy Supply Sources i i

<!-- b000594 | prose | pages [12] -->
:Environmental cost (pollution produced) when converting energy from

<!-- b000595 | prose | pages [12] -->
ijP

<!-- b000596 | prose | pages [12] -->
Supply Source i to Demand Sector j

<!-- b000597 | furniture | pages [13] -->
Team#11893                                             Page 12 of 20

<!-- b000598 | prose | pages [13] -->
 : Efficiency of converting heat to electricity 1

<!-- b000599 | prose | pages [13] -->
: Energy efficiency of electric cars compared to traditional cars, i.e., the ratio

<!-- b000600 | prose | pages [13] -->


<!-- b000601 | prose | pages [13] -->
of energy consumed by traditional cars to electric cars under the same

<!-- b000602 | prose | pages [13] -->
2

<!-- b000603 | prose | pages [13] -->
 : Combined energy efficiency of electric cars, which is

<!-- b000604 | prose | pages [13] -->
O

<!-- b000605 | prose | pages [13] -->
 1 

<!-- b000606 | furniture | pages [13] -->


<!-- b000607 | prose | pages [13] -->
2

<!-- b000608 | prose | pages [13] -->
: Fuel consumption per 100 kilometers of traditional cars 100

<!-- b000609 | prose | pages [13] -->
E : Energy produced by electric cars under the consumption of one unit of oil

<!-- b000610 | prose | pages [13] -->
E :Electricity consumption per 100 kilometers of traditional cars 100

<!-- b000611 | prose | pages [13] -->
:Environmental cost of the total amount of pollution caused by energy

<!-- b000612 | prose | pages [13] -->
P

<!-- b000613 | furniture | pages [13] -->


<!-- b000614 | prose | pages [13] -->
ALL

<!-- b000615 | prose | pages [13] -->
consumption

<!-- b000616 | heading | pages [13] -->
Assumptions

<!-- b000617 | prose | pages [13] -->
1.

<!-- b000618 | prose | pages [13] -->
We only model under ideal situation, that is, the whole energy system is working under the condition which meets the optimal solution of linear programming.

<!-- b000619 | prose | pages [13] -->
2.

<!-- b000620 | prose | pages [13] -->
The environmental cost can fully reflect the pollution caused by using different types of energy.

<!-- b000621 | prose | pages [13] -->
3.

<!-- b000622 | prose | pages [13] -->
Most EVs are HEVs (Hybrid Electric Vehicles), but there are also BEVs (Battery Electric Vehicles) and PHEVs (Plug-in Electric Vehicles).

<!-- b000623 | heading | pages [13] -->
The Foundation of A Linear Programming Model for Optimum Energy

<!-- b000624 | prose | pages [13] -->
Distribution

<!-- b000625 | prose | pages [13] -->
x 11

<!-- b000626 | furniture | pages [13] -->


<!-- b000627 | furniture | pages [13] -->


<!-- b000628 | prose | pages [13] -->
Fig. 9

<!-- b000629 | prose | pages [13] -->
The distribution of the energy network is shown as in Fig. 9.Considering that the

<!-- b000630 | furniture | pages [14] -->
Team#11893                                             Page 13 of 20

<!-- b000631 | prose | pages [14] -->
demands must still be satisfied after the redistribution of energy flow, we can have the following constraints:

<!-- b000632 | prose | pages [14] -->
      

<!-- b000633 | prose | pages [14] -->
. .

<!-- b000634 | prose | pages [14] -->
S t x x x x B

<!-- b000635 | prose | pages [14] -->
11 21 41 1 2

<!-- b000636 | prose | pages [14] -->
c

<!-- b000637 | prose | pages [14] -->
   

<!-- b000638 | prose | pages [14] -->
x x x x B

<!-- b000639 | prose | pages [14] -->
12 22 32 42 2

<!-- b000640 | prose | pages [14] -->
   

<!-- b000641 | prose | pages [14] -->
x x x x B

<!-- b000642 | prose | pages [14] -->
13 23 33 43 3

<!-- b000643 | prose | pages [14] -->
    

<!-- b000644 | prose | pages [14] -->
x x x x x B

<!-- b000645 | prose | pages [14] -->
c

<!-- b000646 | prose | pages [14] -->
14 24 44 54 4

<!-- b000647 | prose | pages [14] -->


<!-- b000648 | prose | pages [14] -->
0

<!-- b000649 | prose | pages [14] -->
x

<!-- b000650 | prose | pages [14] -->
ij

<!-- b000651 | prose | pages [14] -->
1 1

<!-- b000652 | furniture | pages [14] -->


<!-- b000653 | furniture | pages [14] -->


<!-- b000654 | prose | pages [14] -->
 is efficiency of converting heat to electricity. Based on data from where 1

<!-- b000655 | prose | pages [14] -->
[http://en.wikipedia.org/wiki/Cogeneration],

<!-- b000656 | prose | pages [14] -->


<!-- b000657 | prose | pages [14] -->
3.0

<!-- b000658 | prose | pages [14] -->
is 1

<!-- b000659 | prose | pages [14] -->


<!-- b000660 | prose | pages [14] -->
generated when energy is

<!-- b000661 | prose | pages [14] -->


<!-- b000662 | prose | pages [14] -->


<!-- b000663 | prose | pages [14] -->


<!-- b000664 | prose | pages [14] -->
1

<!-- b000665 | prose | pages [14] -->
8.0

<!-- b000666 | prose | pages [14] -->
by Electricti ty only plants

<!-- b000667 | prose | pages [14] -->
  

<!-- b000668 | prose | pages [14] -->
( )

<!-- b000669 | prose | pages [14] -->
generated when energy is

<!-- b000670 | prose | pages [14] -->


<!-- b000671 | prose | pages [14] -->
 E O  

<!-- b000672 | prose | pages [14] -->
100

<!-- b000673 | prose | pages [14] -->
by combined heat and power CHP plants

<!-- b000674 | prose | pages [14] -->
, it stands for energy efficiency of electric cars compared to traditional cars.

<!-- b000675 | prose | pages [14] -->
2 E

<!-- b000676 | prose | pages [14] -->
100

<!-- b000677 | prose | pages [14] -->
     To obtain the combined efficiency, let , 1 1 2

<!-- b000678 | prose | pages [14] -->
The environmental cost of the total amount of pollution caused by energy consumption is

<!-- b000679 | prose | pages [14] -->
5

<!-- b000680 | prose | pages [14] -->
4

<!-- b000681 | prose | pages [14] -->


<!-- b000682 | prose | pages [14] -->
 

<!-- b000683 | prose | pages [14] -->
P x P

<!-- b000684 | furniture | pages [14] -->


<!-- b000685 | prose | pages [14] -->
ALL ij ij

<!-- b000686 | prose | pages [14] -->
 

<!-- b000687 | prose | pages [14] -->
i

<!-- b000688 | prose | pages [14] -->
1

<!-- b000689 | prose | pages [14] -->
j 1

<!-- b000690 | prose | pages [14] -->
P

<!-- b000691 | prose | pages [14] -->
As our goal is to minimize the environmental cost , we propose the following LP

<!-- b000692 | prose | pages [14] -->
ALL

<!-- b000693 | prose | pages [14] -->
formulation for the single destination problem.

<!-- b000694 | prose | pages [14] -->
5

<!-- b000695 | prose | pages [14] -->
4

<!-- b000696 | prose | pages [14] -->
 

<!-- b000697 | prose | pages [14] -->
x P

<!-- b000698 | prose | pages [14] -->
min

<!-- b000699 | prose | pages [14] -->
ij ij

<!-- b000700 | prose | pages [14] -->
 

<!-- b000701 | prose | pages [14] -->
i j

<!-- b000702 | prose | pages [14] -->
1

<!-- b000703 | prose | pages [14] -->
1

<!-- b000704 | prose | pages [14] -->
     

<!-- b000705 | prose | pages [14] -->
 

<!-- b000706 | prose | pages [14] -->
S t x x x x

<!-- b000707 | prose | pages [14] -->
..

<!-- b000708 | prose | pages [14] -->
c

<!-- b000709 | prose | pages [14] -->
11 21 41 1 2

<!-- b000710 | prose | pages [14] -->
   

<!-- b000711 | prose | pages [14] -->
x x x x B

<!-- b000712 | prose | pages [14] -->
12 22 32 42 2

<!-- b000713 | prose | pages [14] -->
   

<!-- b000714 | prose | pages [14] -->
x x x x B

<!-- b000715 | prose | pages [14] -->
13 23 33 43 3

<!-- b000716 | prose | pages [14] -->
    

<!-- b000717 | prose | pages [14] -->
x x x x x B

<!-- b000718 | prose | pages [14] -->
c

<!-- b000719 | prose | pages [14] -->
14 24 44 54

<!-- b000720 | prose | pages [14] -->


<!-- b000721 | prose | pages [14] -->
x

<!-- b000722 | prose | pages [14] -->
0

<!-- b000723 | prose | pages [14] -->
ij

<!-- b000724 | prose | pages [14] -->
B B

<!-- b000725 | prose | pages [14] -->
1 1

<!-- b000726 | furniture | pages [14] -->


<!-- b000727 | prose | pages [14] -->
4 4

<!-- b000728 | heading | pages [14] -->
The Solution of The Linear Programming Model for Optimum Energy

<!-- b000729 | prose | pages [14] -->
Distribution

<!-- b000730 | heading | pages [14] -->
1. The Solution of the Basic Model

<!-- b000731 | prose | pages [14] -->
In economy, Environmental Cost is commonly used as a criterion to measure the extent of pollution. According to [Shuying Ding 2006] and taking reality into account, we list different conditions in the table below:

<!-- b000732 | prose | pages [14] -->
Mathematical No.

<!-- b000733 | prose | pages [14] -->
Constraint

<!-- b000734 | prose | pages [14] -->
Explanation Expression

<!-- b000735 | prose | pages [14] -->
Constraint on the total

<!-- b000736 | prose | pages [14] -->
4

<!-- b000737 | prose | pages [14] -->
 4 

<!-- b000738 | prose | pages [14] -->
x

<!-- b000739 | prose | pages [14] -->
1

<!-- b000740 | prose | pages [14] -->
amount of energy of

<!-- b000741 | prose | pages [14] -->
j

<!-- b000742 | prose | pages [14] -->
Renewable Energy

<!-- b000743 | prose | pages [14] -->


<!-- b000744 | prose | pages [14] -->
1

<!-- b000745 | prose | pages [14] -->
j

<!-- b000746 | prose | pages [14] -->
Existing installed capacity of solar, wind

<!-- b000747 | prose | pages [14] -->
7.7

<!-- b000748 | prose | pages [14] -->
and water power determines the maximum amount of energy supplied by

<!-- b000749 | furniture | pages [15] -->
Team#11893                                             Page 14 of 20

<!-- b000750 | prose | pages [15] -->
Constraint on the total

<!-- b000751 | prose | pages [15] -->
54  x

<!-- b000752 | prose | pages [15] -->
2

<!-- b000753 | prose | pages [15] -->
amount of energy of Nuclear Electric Power

<!-- b000754 | prose | pages [15] -->
Constraint on the total

<!-- b000755 | prose | pages [15] -->
4

<!-- b000756 | prose | pages [15] -->
 2 

<!-- b000757 | prose | pages [15] -->
x

<!-- b000758 | prose | pages [15] -->
3

<!-- b000759 | prose | pages [15] -->
amount of energy of

<!-- b000760 | prose | pages [15] -->
j

<!-- b000761 | prose | pages [15] -->
Natural Gas

<!-- b000762 | prose | pages [15] -->
 j

<!-- b000763 | prose | pages [15] -->
1

<!-- b000764 | prose | pages [15] -->
Constraint on the total

<!-- b000765 | prose | pages [15] -->
4

<!-- b000766 | prose | pages [15] -->
 1 

<!-- b000767 | prose | pages [15] -->
x

<!-- b000768 | prose | pages [15] -->
4

<!-- b000769 | prose | pages [15] -->
amount of energy of

<!-- b000770 | prose | pages [15] -->
j

<!-- b000771 | prose | pages [15] -->
Petroleum

<!-- b000772 | prose | pages [15] -->
 j

<!-- b000773 | prose | pages [15] -->
1

<!-- b000774 | prose | pages [15] -->
cx

<!-- b000775 | prose | pages [15] -->
Constraint on (energy transferred from Electric

<!-- b000776 | prose | pages [15] -->


<!-- b000777 | prose | pages [15] -->
Power sector to

<!-- b000778 | prose | pages [15] -->
cx

<!-- b000779 | prose | pages [15] -->
5

<!-- b000780 | prose | pages [15] -->
Transportation sector after

<!-- b000781 | prose | pages [15] -->
the popularization of

<!-- b000782 | prose | pages [15] -->
electric cars)

<!-- b000783 | prose | pages [15] -->
x

<!-- b000784 | prose | pages [15] -->
Constraint on (energy

<!-- b000785 | prose | pages [15] -->
11

<!-- b000786 | prose | pages [15] -->
transferred from Petroleum

<!-- b000787 | prose | pages [15] -->
11  12 x

<!-- b000788 | prose | pages [15] -->
6

<!-- b000789 | prose | pages [15] -->
source to Transportation

<!-- b000790 | prose | pages [15] -->
sector)

<!-- b000791 | prose | pages [15] -->
x

<!-- b000792 | prose | pages [15] -->
Constraint on (energy

<!-- b000793 | prose | pages [15] -->
11

<!-- b000794 | prose | pages [15] -->
transferred from Coal

<!-- b000795 | prose | pages [15] -->
34  x 15

<!-- b000796 | prose | pages [15] -->
7

<!-- b000797 | prose | pages [15] -->
source to Electric Power

<!-- b000798 | prose | pages [15] -->
sector)

<!-- b000799 | prose | pages [15] -->
x

<!-- b000800 | prose | pages [15] -->
Constraint on (energy

<!-- b000801 | prose | pages [15] -->
11

<!-- b000802 | prose | pages [15] -->
transferred from Renewable

<!-- b000803 | prose | pages [15] -->
44  x

<!-- b000804 | prose | pages [15] -->
8

<!-- b000805 | prose | pages [15] -->
Energy source to Electric

<!-- b000806 | prose | pages [15] -->
Power sector)

<!-- b000807 | prose | pages [15] -->
Renewable Energy.

<!-- b000808 | prose | pages [15] -->
Existing installed capacity of nuclear

<!-- b000809 | prose | pages [15] -->
3.8 3.8

<!-- b000810 | furniture | pages [15] -->


<!-- b000811 | prose | pages [15] -->
power determines the maximum amount

<!-- b000812 | prose | pages [15] -->
of energy supplied by nuclear power.

<!-- b000813 | prose | pages [15] -->
Existing natural gas drilling amount

<!-- b000814 | prose | pages [15] -->
23 4.

<!-- b000815 | prose | pages [15] -->
determines the maximum amount of

<!-- b000816 | prose | pages [15] -->
natural gas supply.

<!-- b000817 | prose | pages [15] -->
Obtained from the infinite value of the

<!-- b000818 | prose | pages [15] -->
38

<!-- b000819 | furniture | pages [15] -->


<!-- b000820 | prose | pages [15] -->
fitted S-P curve in the supply-demand

<!-- b000821 | prose | pages [15] -->
model.

<!-- b000822 | prose | pages [15] -->
Estimated from the energy transferred 10 10

<!-- b000823 | furniture | pages [15] -->


<!-- b000824 | prose | pages [15] -->
from transportation to electric power.

<!-- b000825 | prose | pages [15] -->
Based on Assumption 3; and suppose that

<!-- b000826 | prose | pages [15] -->
. . 708

<!-- b000827 | prose | pages [15] -->
half of the energy consumed by HEVs

<!-- b000828 | prose | pages [15] -->
are provided by gasoline.

<!-- b000829 | prose | pages [15] -->
Calculated by real power generation . . 65

<!-- b000830 | furniture | pages [15] -->


<!-- b000831 | prose | pages [15] -->
efficiency and installed capacity of coal.

<!-- b000832 | prose | pages [15] -->
Calculated by real power generation

<!-- b000833 | prose | pages [15] -->
7 7

<!-- b000834 | furniture | pages [15] -->


<!-- b000835 | furniture | pages [15] -->


<!-- b000836 | prose | pages [15] -->
efficiency and installed capacity of

<!-- b000837 | prose | pages [15] -->
Renewable Energy.

<!-- b000838 | prose | pages [15] -->
Tbl. 6

<!-- b000839 | prose | pages [15] -->
Adding these constraints to previous model, we get the following figure:

<!-- b000840 | prose | pages [15] -->
120

<!-- b000841 | prose | pages [15] -->
Original Condition No Restriction Restriction No.3+No.4

<!-- b000842 | prose | pages [15] -->
100

<!-- b000843 | furniture | pages [15] -->


<!-- b000844 | prose | pages [15] -->
Restriction No.3+No.4(loosed by 2 times) Restriction No.3+No.4+No.5 Restriction No.1~No.10

<!-- b000845 | prose | pages [15] -->
Energy(Quadrillion Btu)

<!-- b000846 | prose | pages [15] -->
80

<!-- b000847 | prose | pages [15] -->
60

<!-- b000848 | prose | pages [15] -->
40

<!-- b000849 | prose | pages [15] -->
20

<!-- b000850 | prose | pages [15] -->
0

<!-- b000851 | furniture | pages [15] -->


<!-- b000852 | prose | pages [15] -->
Petroleum Natural Gas Coal Renewable Energy Nuclear Electric Power

<!-- b000853 | prose | pages [15] -->
Different Kinds of Supply Sources

<!-- b000854 | furniture | pages [15] -->


<!-- b000855 | prose | pages [15] -->
Fig. 10

<!-- b000856 | furniture | pages [16] -->
Team#11893                                             Page 15 of 20

<!-- b000857 | prose | pages [16] -->
We can see, if there were no constraints, the optimal distribution of energy would be to use Renewable Energy as supply source completely, and the second best choice would be Nuclear Electric Power. Under real conditions, it is impossible to completely use Renewable Energy and Nuclear Electric Power as energy supply sources. Considering constraints No.3 and No. 4 (listed in Tbl. 6), we can find that the result of the LP formation shows it is more reasonable to use Natural Gas.

<!-- b000858 | prose | pages [16] -->
However, because of limited usable quantity, it is still impossible to use Natural Gas as first-choice energy supply source. Thus, we have to add constraint No.5 to improve our model. Considering other concrete factors, such as the structure of energy industry, the upper limit of energy, etc., we finally propose the linear programming model with constraints No.1-No.10.

<!-- b000859 | prose | pages [16] -->
Based on the discussions and analysis above, we can ensure the order of priority of energy supply sources as below: Renewable Energy>Nuclear Electric Power>Natural ijP Gas>Petroleum>Coal, which accords with the data of the environmental cost .

<!-- b000860 | prose | pages [16] -->
P

<!-- b000861 | prose | pages [16] -->
Now we show the total amount of environmental cost of energy consumption under

<!-- b000862 | prose | pages [16] -->
ALL

<!-- b000863 | prose | pages [16] -->
six different combinations of constraints (listed in the legend of the figure above) in a new figure:

<!-- b000864 | prose | pages [16] -->
60

<!-- b000865 | prose | pages [16] -->
50

<!-- b000866 | prose | pages [16] -->
40

<!-- b000867 | prose | pages [16] -->
PALL

<!-- b000868 | prose | pages [16] -->
30

<!-- b000869 | prose | pages [16] -->
20

<!-- b000870 | prose | pages [16] -->
10

<!-- b000871 | prose | pages [16] -->
0 No Restriction Restriction No.3+No.4 Restriction No.3+No.4(loosed by 2 times) Restriction No.3+No.4+No.5 Restriction No.1-No.10

<!-- b000872 | prose | pages [16] -->
Different Kinds of Restrictions

<!-- b000873 | furniture | pages [16] -->


<!-- b000874 | prose | pages [16] -->
Fig. 11

<!-- b000875 | prose | pages [16] -->
We can roughly observe that the looser the constraints, the lower the environmental P , correspondingly the better the environment. cost ALL

<!-- b000876 | heading | pages [16] -->
2. Sensitivity Analysis for Ordinary Condition

<!-- b000877 | prose | pages [16] -->
Subsequently, by using the ultimate model with constraints No.1-No.8 and changing the value of , we create the figure below to demonstrate energy distribution and energy transferred from Electric Power sector to Transportation sector after the popularization of X electric cars( ). c

<!-- b000878 | furniture | pages [17] -->
Team#11893                                             Page 16 of 20

<!-- b000879 | prose | pages [17] -->
40

<!-- b000880 | furniture | pages [17] -->


<!-- b000881 | prose | pages [17] -->
=0.5

<!-- b000882 | prose | pages [17] -->
Critical Point:=0.85

<!-- b000883 | prose | pages [17] -->
35

<!-- b000884 | prose | pages [17] -->
30

<!-- b000885 | prose | pages [17] -->
Energy(Quadrillion Btu)

<!-- b000886 | prose | pages [17] -->
25

<!-- b000887 | prose | pages [17] -->
20

<!-- b000888 | prose | pages [17] -->
15

<!-- b000889 | prose | pages [17] -->
10

<!-- b000890 | prose | pages [17] -->
5

<!-- b000891 | prose | pages [17] -->
0

<!-- b000892 | furniture | pages [17] -->


<!-- b000893 | prose | pages [17] -->
Petroleum Natural Gas

<!-- b000894 | prose | pages [17] -->
=0.6

<!-- b000895 | prose | pages [17] -->
=0.7

<!-- b000896 | prose | pages [17] -->
=0.8

<!-- b000897 | prose | pages [17] -->
=0.9

<!-- b000898 | prose | pages [17] -->
=1.0

<!-- b000899 | prose | pages [17] -->
=1.1

<!-- b000900 | prose | pages [17] -->
=1.2

<!-- b000901 | prose | pages [17] -->
=1.3

<!-- b000902 | prose | pages [17] -->
=1.4

<!-- b000903 | prose | pages [17] -->
=1.5

<!-- b000904 | prose | pages [17] -->
=2

<!-- b000905 | prose | pages [17] -->
Critical Point:=0.85

<!-- b000906 | prose | pages [17] -->
=3

<!-- b000907 | prose | pages [17] -->
=4

<!-- b000908 | prose | pages [17] -->
Coal Renewable Energy Nuclear Electric Power  Energy Transmission(Xc)

<!-- b000909 | prose | pages [17] -->
Different Kinds of Supply Sources and ...

<!-- b000910 | furniture | pages [17] -->


<!-- b000911 | prose | pages [17] -->
Fig. 12

<!-- b000912 | prose | pages [17] -->
    .0 85 .0 85 From the figure above we can find a Critical Point:

<!-- b000913 | prose | pages [17] -->
X

<!-- b000914 | prose | pages [17] -->
. That is, when ,

<!-- b000915 | prose | pages [17] -->
  .0 85 , the keeps being zero. But when the demand of coal is a constant, and c

<!-- b000916 | prose | pages [17] -->
demand of coal begins to decrease, while

<!-- b000917 | prose | pages [17] -->
 is larger than 1.4.

<!-- b000918 | prose | pages [17] -->
decrease after

<!-- b000919 | prose | pages [17] -->
Now we show the environmental cost

<!-- b000920 | prose | pages [17] -->
60

<!-- b000921 | prose | pages [17] -->
58

<!-- b000922 | prose | pages [17] -->
Critical Point:

<!-- b000923 | prose | pages [17] -->
56

<!-- b000924 | prose | pages [17] -->
=0.85

<!-- b000925 | prose | pages [17] -->
PALL

<!-- b000926 | prose | pages [17] -->
54

<!-- b000927 | prose | pages [17] -->
52

<!-- b000928 | prose | pages [17] -->
50

<!-- b000929 | prose | pages [17] -->
48 0.5 1 1.5

<!-- b000930 | prose | pages [17] -->
  .0 85

<!-- b000931 | prose | pages [17] -->
X X

<!-- b000932 | prose | pages [17] -->
becomes a non-zero constant and starts to

<!-- b000933 | prose | pages [17] -->
c c

<!-- b000934 | prose | pages [17] -->
 values in a curve: P P under different ALL

<!-- b000935 | prose | pages [17] -->
2 2 2.5 3 3.5 4

<!-- b000936 | prose | pages [17] -->


<!-- b000937 | furniture | pages [17] -->


<!-- b000938 | prose | pages [17] -->
Fig. 13

<!-- b000939 | prose | pages [17] -->
is still a Critical Point. Besides, it is easy to find that when We can see that   .0 85

<!-- b000940 | prose | pages [17] -->
P

<!-- b000941 | prose | pages [17] -->
is decreasing, which means the environment is , the environmental cost

<!-- b000942 | prose | pages [17] -->
ALL

<!-- b000943 | prose | pages [17] -->
improving. However, we can also notice that

<!-- b000944 | prose | pages [17] -->
dPALL is going down, which shows the  d

<!-- b000945 | prose | pages [17] -->
effect of improving environment by lifting  is declining.

<!-- b000946 | furniture | pages [18] -->
Team#11893                                             Page 17 of 20

<!-- b000947 | heading | pages [18] -->
3. Sensitivity Analysis for BEV, HEV, and PHEV

<!-- b000948 | prose | pages [18] -->
The electric vehicles in the market can be categorized into three major types: BEV, HEV, and PHEV. Because their power generation mechanisms are different, the optimal environmental costs of them are different under same energy condition. Besides, the proportion of fossil fuels they consume will be different. Thus, based on previous results of linear programming and new constraints derived from the characteristics of different cars, we can give a new solution of the problem. Consider the conditions when the electric vehicles in the market are all BEVs, HEVs or PHEVs separately, and list the constraints under each condition as following:

<!-- b000949 | prose | pages [18] -->
Type Constraint Explanation

<!-- b000950 | prose | pages [18] -->
The source of energy for transportation will not be restricted 11  0 x

<!-- b000951 | furniture | pages [18] -->


<!-- b000952 | prose | pages [18] -->
BEV

<!-- b000953 | prose | pages [18] -->
 cx 15

<!-- b000954 | furniture | pages [18] -->


<!-- b000955 | prose | pages [18] -->
1

<!-- b000956 | prose | pages [18] -->
by oil now.

<!-- b000957 | prose | pages [18] -->
Calculated from electricity margin.

<!-- b000958 | prose | pages [18] -->
Suppose more than half of the amount of energy for  

<!-- b000959 | prose | pages [18] -->
25 . 416

<!-- b000960 | prose | pages [18] -->
x

<!-- b000961 | furniture | pages [18] -->


<!-- b000962 | prose | pages [18] -->
11

<!-- b000963 | prose | pages [18] -->
2

<!-- b000964 | prose | pages [18] -->
PHEV

<!-- b000965 | prose | pages [18] -->
 28 cx

<!-- b000966 | furniture | pages [18] -->


<!-- b000967 | prose | pages [18] -->
transportation is provide by oil.

<!-- b000968 | prose | pages [18] -->
Calculated from electricity margin.

<!-- b000969 | prose | pages [18] -->
Converted and estimated from the fuel consumption of 100 11  10 x

<!-- b000970 | furniture | pages [18] -->


<!-- b000971 | prose | pages [18] -->
kilometers of Toyota Prius and conventional cars. HEV

<!-- b000972 | prose | pages [18] -->
 0 cx

<!-- b000973 | furniture | pages [18] -->


<!-- b000974 | prose | pages [18] -->
HEVs cannot get power from electricity grid directly.

<!-- b000975 | prose | pages [18] -->
Tbl.7

<!-- b000976 | prose | pages [18] -->
Solving the three linear programming problems above, we can first get a curve which shows the change of the total environmental cost over the combined energy efficiency of electric cars :

<!-- b000977 | prose | pages [18] -->
60

<!-- b000978 | prose | pages [18] -->
55

<!-- b000979 | prose | pages [18] -->
50

<!-- b000980 | prose | pages [18] -->
PALL

<!-- b000981 | prose | pages [18] -->
45

<!-- b000982 | prose | pages [18] -->
40

<!-- b000983 | prose | pages [18] -->
35

<!-- b000984 | prose | pages [18] -->
30

<!-- b000985 | furniture | pages [18] -->


<!-- b000986 | prose | pages [18] -->
0 1 2

<!-- b000987 | prose | pages [18] -->
By analyzing this figure we can find:

<!-- b000988 | furniture | pages [18] -->


<!-- b000989 | prose | pages [18] -->
Original Pollution BEV's Pullution PHEV's Pullution HEV's Pullution

<!-- b000990 | prose | pages [18] -->
3 3 4 5 6 7 8

<!-- b000991 | prose | pages [18] -->


<!-- b000992 | furniture | pages [18] -->


<!-- b000993 | prose | pages [18] -->
Fig. 14

<!-- b000994 | furniture | pages [19] -->
Team#11893                                             Page 18 of 20

<!-- b000995 | prose | pages [19] -->
 BEV is always better than PHEV in the respect of environment protection.

<!-- b000996 | prose | pages [19] -->
When the value of  is small, the environmental cost of HEV is lower than that  of BEV or PHEV. But as  increases, HEV is growing worse than BEV or PHEV.

<!-- b000997 | prose | pages [19] -->
To make BEV and PHEV perform better in environment protection,  must be  higher than its value at critical point, while HEV always perform better than current environment situation.

<!-- b000998 | prose | pages [19] -->
Then, we illustrate the energy distribution of the three EV types in separate pie charts   3 when (it means the EV technologies have developed fully):

<!-- b000999 | prose | pages [19] -->
13%

<!-- b001000 | prose | pages [19] -->
< 1%

<!-- b001001 | prose | pages [19] -->
25%

<!-- b001002 | prose | pages [19] -->
59%

<!-- b001003 | prose | pages [19] -->
3%

<!-- b001004 | furniture | pages [19] -->


<!-- b001005 | prose | pages [19] -->
BEV

<!-- b001006 | prose | pages [19] -->
15%

<!-- b001007 | prose | pages [19] -->
< 1%

<!-- b001008 | prose | pages [19] -->
45%

<!-- b001009 | prose | pages [19] -->
29%

<!-- b001010 | prose | pages [19] -->
10%

<!-- b001011 | prose | pages [19] -->
HEV

<!-- b001012 | prose | pages [19] -->
14%

<!-- b001013 | prose | pages [19] -->
< 1%

<!-- b001014 | prose | pages [19] -->
43%

<!-- b001015 | prose | pages [19] -->
27%

<!-- b001016 | prose | pages [19] -->
16%

<!-- b001017 | prose | pages [19] -->
PHEV

<!-- b001018 | furniture | pages [19] -->


<!-- b001019 | furniture | pages [19] -->


<!-- b001020 | prose | pages [19] -->
Fig. 15

<!-- b001021 | prose | pages [19] -->
From the figures above we can obviously observe that the type of electric vehicles has a great impact on the distribution of electricity.

<!-- b001022 | heading | pages [19] -->
4. Model validation

<!-- b001023 | prose | pages [19] -->
From above analysis, when the  is small, we should popularize HEV to minimize the environmental cost. When  is large enough so that the environment cost of PHEV and

<!-- b001024 | prose | pages [19] -->
BEV is lower than the one of HEV, we should popularize them.

<!-- b001025 | prose | pages [19] -->
Before Toyota Prius released PHEV in 2007, the HEV dominated the EVs’ market, which is in accord with situation of small. After its release, we can observe a decline of sales of HEV from the reference’s data. This validates the crossover point of P- curve in

<!-- b001026 | prose | pages [19] -->
figure * between HEV and PHEV/BEV.

<!-- b001027 | heading | pages [19] -->
Conclusion

<!-- b001028 | furniture | pages [20] -->
Team#11893                                             Page 19 of 20

<!-- b001029 | heading | pages [20] -->
Strengths

<!-- b001030 | prose | pages [20] -->
 Our models are simple but comprehensive, covering five aspects;

<!-- b001031 | prose | pages [20] -->
 Our models have strong robustness due to their independence with types of EV;

<!-- b001032 | prose | pages [20] -->
 Our models validate and complement each other;

<!-- b001033 | prose | pages [20] -->
 Each model is aimed at a special perspective and offers practical recommendations.

<!-- b001034 | heading | pages [20] -->
Weakness

<!-- b001035 | prose | pages [20] -->
 Much of the coefficients in our models are simplified or estimated in statistic;

<!-- b001036 | prose | pages [20] -->
 Some solution plays a guiding role but is not practical or realizable in real world.

<!-- b001037 | heading | pages [20] -->
Recommendation

<!-- b001038 | prose | pages [20] -->
For the Governments

<!-- b001039 | prose | pages [20] -->
1) Governments should increase the oil tax rate to limit the demand of CVs and popularize EVs due to the analysis in SSDM;

<!-- b001040 | prose | pages [20] -->
2) More electricity production and installed capacity is needed to promote the widespread use of EVs, the additional amount is determined by the EV type;

<!-- b001041 | prose | pages [20] -->
3) More charging infrastructures are necessary;

<!-- b001042 | prose | pages [20] -->
cx

<!-- b001043 | prose | pages [20] -->
4) Based on the linear programming model considering (energy transferred from

<!-- b001044 | prose | pages [20] -->
Electric Power sector to Transportation sector), the order of priority of five energy supply sources is: Renewable Energy>Nuclear Electric Power>Natural Gas>Petroleum>Coal

<!-- b001045 | prose | pages [20] -->
Therefore, the government should first take into consideration the development of supply sources such as Renewable Energy or Nuclear Electric Power so that they could help electric cars produce benefits to environment. As for the benefits of developing different types of energy, we can refer to Fig. 10 and Fig. 11.

<!-- b001046 | prose | pages [20] -->
5) Strategies for developing which type of the electric cars: If our technology developing ability is powerful enough, i.e.,  is high enough, we should develop BEV in

<!-- b001047 | prose | pages [20] -->
priority to gain the most benefits to environment. If our technology developing ability is limited, we should develop HEV in priority, whose benefits to environment have nothing to do with .

<!-- b001048 | prose | pages [20] -->
6) Can we save fossil fuels by widely using electric vehicles? According to the results

<!-- b001049 | prose | pages [20] -->
we have obtained, under the premise that    .0 85 , coals can be saved. Because under the

<!-- b001050 | prose | pages [20] -->
optimal condition, the demands of petroleum and natural gas will exceed their supply amount. Unfortunately, under no conditions could petroleum or natural gas be saved.

<!-- b001051 | prose | pages [20] -->
For the vehicle manufacturers

<!-- b001052 | furniture | pages [21] -->
Team#11893                                             Page 20 of 20

<!-- b001053 | prose | pages [21] -->
1) Manufactures should increase the endurance mileage by improve the technique of battery, so that more EVs don’t need charge in on-peak hours.

<!-- b001054 | prose | pages [21] -->
  .0 85 , and 2) In the sensitivity analysis section in LPM, we find a critical point

<!-- b001055 | prose | pages [21] -->
  .0 85 through analysis we know that only when electric cars can demonstrate their

<!-- b001056 | prose | pages [21] -->
energy economic advantage. So the value of  should be as large as possible.

<!-- b001057 | prose | pages [21] -->


<!-- b001058 | prose | pages [21] -->


<!-- b001059 | prose | pages [21] -->
O E

<!-- b001060 | prose | pages [21] -->
 

<!-- b001061 | prose | pages [21] -->
100

<!-- b001062 | prose | pages [21] -->
3.0

<!-- b001063 | prose | pages [21] -->
when energy is generated by Electricti ty only plants

<!-- b001064 | prose | pages [21] -->


<!-- b001065 | prose | pages [21] -->
E

<!-- b001066 | prose | pages [21] -->
  1 

<!-- b001067 | prose | pages [21] -->
  

<!-- b001068 | prose | pages [21] -->
100

<!-- b001069 | prose | pages [21] -->


<!-- b001070 | prose | pages [21] -->


<!-- b001071 | prose | pages [21] -->
O E

<!-- b001072 | prose | pages [21] -->
2

<!-- b001073 | prose | pages [21] -->


<!-- b001074 | prose | pages [21] -->
   

<!-- b001075 | prose | pages [21] -->
100

<!-- b001076 | prose | pages [21] -->
when energy is generated by combined heat and power CHP plants

<!-- b001077 | prose | pages [21] -->
8.0 ( )

<!-- b001078 | prose | pages [21] -->


<!-- b001079 | prose | pages [21] -->
E

<!-- b001080 | prose | pages [21] -->


<!-- b001081 | prose | pages [21] -->
100

<!-- b001082 | prose | pages [21] -->
It is impractical to increase the fuel consumption of traditional cars in order to protect environment. So what we can really do are:

<!-- b001083 | prose | pages [21] -->
E  , that is, minimizing the energy consumption of electric cars by Minimizing 100

<!-- b001084 | prose | pages [21] -->
technical innovations.

<!-- b001085 | prose | pages [21] -->
 Use combined-heat-and-power (CHP) plants to generate power as much as possible.

<!-- b001086 | heading | pages [21] -->
References

<!-- b001087 | references | pages [21] -->
[1] Frank R. Giordano, Maurice D. Weir, William P. Fox. (2005) A First Course in

<!-- b001088 | references | pages [21] -->
Mathematical Modeling, 3rd edition.

<!-- b001089 | references | pages [21] -->
[2] David Tilman. (1994) ‘Competition and Biodiversity in Spatially Structured Habits’,

<!-- b001090 | references | pages [21] -->
Ecology, 75(1), 1994, pp. 2-16

<!-- b001091 | references | pages [21] -->
[3] Sanjaka G. Wirasingha, Nigel Schofield and Ali Emadi. (2008) ‘Feasibility analysis

<!-- b001092 | references | pages [21] -->
of converting a Chicago Transit Authority (CTA) transit bus to a plug-in hybrid electric

<!-- b001093 | references | pages [21] -->
vehicle’, IEEE Vehicle Power and Propulsion Conference (VPPC), September 3-5, 2008,

<!-- b001094 | references | pages [21] -->
Harbin, China

<!-- b001095 | references | pages [21] -->
[4] Shuying Ding. (2006) ‘Calculations on the Cost of Electricity Generation’, Master’s

<!-- b001096 | references | pages [21] -->
Thesis in Zhejiang University, Hangzhou, China.

<!-- b001097 | references | pages [21] -->
[5] Mark M. Meerschaert. (2008) Mathematical Modeling, 3rd edition.

<!-- b001098 | references | pages [21] -->
[6] U.S. Hybrid-Electric Vehicle Sales, 1999-2010.

<!-- b001099 | references | pages [21] -->
http://www.afdc.energy.gov/afdc/data/.

<!-- b001100 | references | pages [21] -->
[7] U.S. Energy Information Administration. (August 2010) Annual Energy Review 2009

<!-- b001101 | references | pages [21] -->
[8] Scott M. Festin. SUMMARY OF NATIONAL AND REGIONAL TRAVEL RENDS:

<!-- b001102 | references | pages [21] -->
1970-1995, Office of Highway Information Management

<!-- b001103 | references | pages [22] -->
Appendix_1

<!-- b001104 | references | pages [22] -->
From International Energy Annual 2006’s data of oil and SUMMARY OF NATIONAL AND

<!-- b001105 | references | pages [22] -->
REGIONAL TRAVEL TRENDS:1970-1995,

<!-- b001106 | references | pages [22] -->
Year

<!-- b001107 | references | pages [22] -->
1980

<!-- b001108 | references | pages [22] -->
1981

<!-- b001109 | references | pages [22] -->
1982

<!-- b001110 | references | pages [22] -->
1983

<!-- b001111 | references | pages [22] -->
1984

<!-- b001112 | references | pages [22] -->
1985

<!-- b001113 | references | pages [22] -->
1986

<!-- b001114 | references | pages [22] -->
1987

<!-- b001115 | references | pages [22] -->
1988

<!-- b001116 | references | pages [22] -->
1989

<!-- b001117 | references | pages [22] -->
59815

<!-- b001118 | references | pages [22] -->
S

<!-- b001119 | references | pages [22] -->
63114

<!-- b001120 | references | pages [22] -->
60944

<!-- b001121 | references | pages [22] -->
59543

<!-- b001122 | references | pages [22] -->
58778

<!-- b001123 | references | pages [22] -->
60085

<!-- b001124 | references | pages [22] -->
61809

<!-- b001125 | references | pages [22] -->
63095

<!-- b001126 | references | pages [22] -->
64965

<!-- b001127 | references | pages [22] -->
66078

<!-- b001128 | references | pages [22] -->
28.80

<!-- b001129 | references | pages [22] -->
P

<!-- b001130 | references | pages [22] -->
30.75

<!-- b001131 | references | pages [22] -->
38.85

<!-- b001132 | references | pages [22] -->
35.54

<!-- b001133 | references | pages [22] -->
31.40

<!-- b001134 | references | pages [22] -->
27.49

<!-- b001135 | references | pages [22] -->
24.93

<!-- b001136 | references | pages [22] -->
16.45

<!-- b001137 | references | pages [22] -->
15.45

<!-- b001138 | references | pages [22] -->
16.04

<!-- b001139 | references | pages [22] -->
2770

<!-- b001140 | references | pages [22] -->
D

<!-- b001141 | references | pages [22] -->
2459

<!-- b001142 | references | pages [22] -->
2532

<!-- b001143 | references | pages [22] -->
2568

<!-- b001144 | references | pages [22] -->
2661

<!-- b001145 | references | pages [22] -->
Year

<!-- b001146 | references | pages [22] -->
1990

<!-- b001147 | references | pages [22] -->
1991

<!-- b001148 | references | pages [22] -->
1992

<!-- b001149 | references | pages [22] -->
1993

<!-- b001150 | references | pages [22] -->
1994

<!-- b001151 | references | pages [22] -->
2856

<!-- b001152 | references | pages [22] -->
2954

<!-- b001153 | references | pages [22] -->
3093

<!-- b001154 | references | pages [22] -->
3262

<!-- b001155 | references | pages [22] -->
3375

<!-- b001156 | references | pages [22] -->
1995

<!-- b001157 | references | pages [22] -->
1996

<!-- b001158 | references | pages [22] -->
1997

<!-- b001159 | references | pages [22] -->
1998

<!-- b001160 | references | pages [22] -->
1999

<!-- b001161 | references | pages [22] -->
68930

<!-- b001162 | references | pages [22] -->
S

<!-- b001163 | references | pages [22] -->
66689

<!-- b001164 | references | pages [22] -->
67296

<!-- b001165 | references | pages [22] -->
67490

<!-- b001166 | references | pages [22] -->
67610

<!-- b001167 | references | pages [22] -->
70133

<!-- b001168 | references | pages [22] -->
71671

<!-- b001169 | references | pages [22] -->
73427

<!-- b001170 | references | pages [22] -->
74053

<!-- b001171 | references | pages [22] -->
75727

<!-- b001172 | references | pages [22] -->
12.93

<!-- b001173 | references | pages [22] -->
P

<!-- b001174 | references | pages [22] -->
20.51

<!-- b001175 | references | pages [22] -->
22.30

<!-- b001176 | references | pages [22] -->
16.10

<!-- b001177 | references | pages [22] -->
16.80

<!-- b001178 | references | pages [22] -->
16.56

<!-- b001179 | references | pages [22] -->
17.48

<!-- b001180 | references | pages [22] -->
23.02

<!-- b001181 | references | pages [22] -->
14.33

<!-- b001182 | references | pages [22] -->
10.16

<!-- b001183 | references | pages [22] -->
3800

<!-- b001184 | references | pages [22] -->
D

<!-- b001185 | references | pages [22] -->
3452

<!-- b001186 | references | pages [22] -->
3497

<!-- b001187 | references | pages [22] -->
3618

<!-- b001188 | references | pages [22] -->
3698

<!-- b001189 | references | pages [22] -->
Year

<!-- b001190 | references | pages [22] -->
2000

<!-- b001191 | references | pages [22] -->
2001

<!-- b001192 | references | pages [22] -->
2002

<!-- b001193 | references | pages [22] -->
2003

<!-- b001194 | references | pages [22] -->
2004

<!-- b001195 | references | pages [22] -->
3869

<!-- b001196 | furniture | pages [22] -->


<!-- b001197 | furniture | pages [22] -->


<!-- b001198 | furniture | pages [22] -->


<!-- b001199 | furniture | pages [22] -->


<!-- b001200 | references | pages [22] -->
2005

<!-- b001201 | references | pages [22] -->
2006

<!-- b001202 | references | pages [22] -->
82408

<!-- b001203 | references | pages [22] -->
S

<!-- b001204 | references | pages [22] -->
76712

<!-- b001205 | references | pages [22] -->
77444

<!-- b001206 | references | pages [22] -->
78089

<!-- b001207 | references | pages [22] -->
79660

<!-- b001208 | references | pages [22] -->
84005

<!-- b001209 | references | pages [22] -->
84979

<!-- b001210 | furniture | pages [22] -->


<!-- b001211 | furniture | pages [22] -->


<!-- b001212 | references | pages [22] -->
30.11

<!-- b001213 | references | pages [22] -->
P

<!-- b001214 | references | pages [22] -->
25.29

<!-- b001215 | references | pages [22] -->
24.49

<!-- b001216 | references | pages [22] -->
17.04

<!-- b001217 | references | pages [22] -->
30.30

<!-- b001218 | furniture | pages [22] -->


<!-- b001219 | references | pages [22] -->
Appendix_2

<!-- b001220 | references | pages [22] -->
37.56

<!-- b001221 | references | pages [22] -->
55.85

<!-- b001222 | furniture | pages [22] -->


<!-- b001223 | furniture | pages [22] -->


<!-- b001224 | references | pages [22] -->
According to data obtained from U.S. Federal Highway Administration, we make a list:

<!-- b001225 | references | pages [22] -->
2003

<!-- b001226 | references | pages [22] -->
Year

<!-- b001227 | references | pages [22] -->
1999

<!-- b001228 | references | pages [22] -->
2000

<!-- b001229 | references | pages [22] -->
2001

<!-- b001230 | references | pages [22] -->
2002

<!-- b001231 | references | pages [22] -->
Number

<!-- b001232 | references | pages [22] -->
of

<!-- b001233 | references | pages [22] -->
Electric

<!-- b001234 | references | pages [22] -->
Cars

<!-- b001235 | references | pages [22] -->
2004

<!-- b001236 | references | pages [22] -->
2005

<!-- b001237 | references | pages [22] -->
2006

<!-- b001238 | references | pages [22] -->
2007

<!-- b001239 | references | pages [22] -->
2008

<!-- b001240 | references | pages [22] -->
2009

<!-- b001241 | references | pages [22] -->
0.113

<!-- b001242 | references | pages [22] -->
0.009

<!-- b001243 | references | pages [22] -->
0.030

<!-- b001244 | references | pages [22] -->
0.065

<!-- b001245 | references | pages [22] -->
0

<!-- b001246 | references | pages [22] -->


<!-- b001247 | references | pages [22] -->
6

<!-- b001248 | references | pages [22] -->
10

<!-- b001249 | references | pages [22] -->
(

<!-- b001250 | references | pages [22] -->
)

<!-- b001251 | references | pages [22] -->
Number

<!-- b001252 | references | pages [22] -->
of

<!-- b001253 | references | pages [22] -->
Conventional

<!-- b001254 | references | pages [22] -->
0.197

<!-- b001255 | references | pages [22] -->
0.407

<!-- b001256 | references | pages [22] -->
0.660

<!-- b001257 | references | pages [22] -->
1.012

<!-- b001258 | references | pages [22] -->
1.324

<!-- b001259 | references | pages [22] -->
1.615

<!-- b001260 | references | pages [22] -->
2.368

<!-- b001261 | references | pages [22] -->
2.205

<!-- b001262 | references | pages [22] -->
2.258

<!-- b001263 | references | pages [22] -->
2.353

<!-- b001264 | references | pages [22] -->
2.346

<!-- b001265 | references | pages [22] -->


<!-- b001266 | references | pages [22] -->
8

<!-- b001267 | references | pages [22] -->
10

<!-- b001268 | references | pages [22] -->
Cars (

<!-- b001269 | references | pages [22] -->
)

<!-- b001270 | furniture | pages [22] -->


<!-- b001271 | furniture | pages [22] -->


<!-- b001272 | furniture | pages [22] -->


<!-- b001273 | furniture | pages [22] -->


<!-- b001274 | references | pages [22] -->
2.430

<!-- b001275 | references | pages [22] -->
2.474

<!-- b001276 | references | pages [22] -->
2.508

<!-- b001277 | references | pages [22] -->
2.544

<!-- b001278 | references | pages [22] -->
2.559

<!-- b001279 | references | pages [22] -->
2.460

<!-- b001280 | references | pages [22] -->
Tbl. 6

<!-- b001281 | references | pages [23] -->
Code

<!-- b001282 | furniture | pages [23] -->


<!-- b001283 | references | pages [23] -->
f=[2*P1;1.5*P1;1.5*P1;P1;2*P2;1.5*P2;1.5*P2;P2;1.5*P3;1.5*P3;P3;2*P4;

<!-- b001284 | references | pages [23] -->
1.5*P4;1.5*P4;P4;P5;0.25*P4];

<!-- b001285 | furniture | pages [23] -->


<!-- b001286 | furniture | pages [23] -->


<!-- b001287 | references | pages [23] -->
neta=8;

<!-- b001288 | references | pages [23] -->
ii=15;

<!-- b001289 | furniture | pages [23] -->


<!-- b001290 | furniture | pages [23] -->


<!-- b001291 | references | pages [23] -->
Aeq=[1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1*neta;

<!-- b001292 | references | pages [23] -->
0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0 0;

<!-- b001293 | references | pages [23] -->
0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0;

<!-- b001294 | references | pages [23] -->
0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 1 -1;];

<!-- b001295 | furniture | pages [23] -->


<!-- b001296 | furniture | pages [23] -->


<!-- b001297 | furniture | pages [23] -->


<!-- b001298 | references | pages [23] -->
%  A=[0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0;

<!-- b001299 | references | pages [23] -->
%     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0];

<!-- b001300 | furniture | pages [23] -->


<!-- b001301 | furniture | pages [23] -->


<!-- b001302 | furniture | pages [23] -->


<!-- b001303 | references | pages [23] -->
A=[0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0;   %ÔÙÉúÄÜÔ´Ô¼Êø<7.7

<!-- b001304 | references | pages [23] -->
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0;   %ºËÄÜÔ¼Êø<8.3

<!-- b001305 | references | pages [23] -->
0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0;   %ÌìÈ»ÆøÔ¼Êø<23.4

<!-- b001306 | references | pages [23] -->
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;    %x11Ô¼Êø>25.416/2

<!-- b001307 | references | pages [23] -->
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1;    %xcÔ¼Êø<10

<!-- b001308 | references | pages [23] -->
1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0;     %Ê¯ÓÍÔ¼Êø<38

<!-- b001309 | references | pages [23] -->
0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0;    %Ãº·¢µçÔ¼Êø>15.65

<!-- b001310 | references | pages [23] -->
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0];    %ÔÙÉúÄÜÔ´·¢µçÔ¼Êø<7

<!-- b001311 | references | pages [23] -->
%B=[7.7;8.3]

<!-- b001312 | furniture | pages [23] -->


<!-- b001313 | references | pages [23] -->
B=[7.7;8.3;23.4;-25.416/2;28;38;-15.65;7];

<!-- b001314 | furniture | pages [23] -->


<!-- b001315 | furniture | pages [23] -->


<!-- b001316 | furniture | pages [23] -->


<!-- b001317 | references | pages [23] -->
Beq=[27;18.8;10.6;38.3];

<!-- b001318 | references | pages [23] -->
lb=zeros(17,1)

<!-- b001319 | references | pages [23] -->
[x,fval_netaa,exitflag,output,lamda]=linprog(f,A,B,Aeq,Beq,lb);

<!-- b001320 | furniture | pages [23] -->


<!-- b001321 | references | pages [23] -->
X1=x(1)+x(2)+x(3)+x(4);

<!-- b001322 | references | pages [23] -->
X2=x(5)+x(6)+x(7)+x(8);

<!-- b001323 | references | pages [23] -->
X3=x(9)+x(10)+x(11);

<!-- b001324 | references | pages [24] -->
X4=x(12)+x(13)+x(14)+x(15);

<!-- b001325 | references | pages [24] -->
X5=x(16);

<!-- b001326 | references | pages [24] -->
Xc=x(17);

<!-- b001327 | furniture | pages [24] -->


<!-- b001328 | references | pages [24] -->
XXALL_neta=[x(1),x(2),x(3),x(4),x(5),x(6),x(7),x(8),x(9),x(10),x(11),

<!-- b001329 | references | pages [24] -->
x(12),x(13),x(14),x(15),x(16),x(17)];

<!-- b001330 | furniture | pages [24] -->


<!-- b001331 | references | pages [24] -->
XALL_neta=[X1,X2,X3,X4,X5,Xc];

<!-- b001332 | furniture | pages [24] -->


<!-- b001333 | furniture | pages [24] -->


<!-- b001334 | furniture | pages [24] -->


<!-- b001335 | references | pages [24] -->
XXALL_type2_neta_con(:,ii)=XXALL_neta;

<!-- b001336 | references | pages [24] -->
XALL_type2_neta_con(:,ii)=XALL_neta;

<!-- b001337 | references | pages [24] -->
fval_type2_neta_con(ii)=fval_netaa;

<!-- b001338 | references | pages [24] -->
bar(XALL_neta)

<!-- b001339 | furniture | pages [24] -->


<!-- b001340 | furniture | pages [24] -->

