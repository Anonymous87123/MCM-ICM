# P-C-2011-11893-6a9ea7d9

Status: machine-draft; not source-verified.


<!-- b000001 | heading | pages [1] -->
Summary

<!-- b000002 | prose | pages [1] -->
Because of serious global pollution problems and energy shortages, the study of the environmental and economic effects of developing electric vehicles has become increasingly important. In this paper, we focus on and provide comprehensive solutions to the following issues:  How does tax rate influence the numbers of Conventional Vehicles (CV) and Electric Vehicles (EV)?  What impacts will the replacement of CVs by EVs on oil stock?  What is the upper-limit proportion of EVs under the condition of the present power generation ability?

<!-- b000003 | prose | pages [1] -->
A Static Supply-Demand Model is set up to answer these questions. According to the influence of tax rate on supply-demand relationship, we analyze the change in the demand of CVs over tax rate. Then, we estimate how long the oil will be consumed up by PHEVs using the supply-price relationship. Finally, we provide an estimation of the upper-limit proportion of EVs under the condition of the present power generation ability.  What is the relationship between the change in the numbers of CVs and EVs?  How do factors such as government control, corporation decision influence the change in the numbers of CVs and EVs?

<!-- b000004 | prose | pages [1] -->
We successfully develop a Competing Ordinary Differential Equation Model to solve these problems. We first build up the equations using linear approximation, and then we fit the real data using least-squares principle and get an ordinary differential equation. With the help of the previous Static Supply-Demand Model, we discuss the real meanings of the fitted variables and the interaction between CVs and EVs.  How does the development of EVs influence the environment?  Whether the development of EVs can save fossil fuels?  Whether different types of EVs have the same benefits to environment, energy, or society?

<!-- b000005 | prose | pages [1] -->
To answer these questions, we build up a linear programming model and set minimum environmental cost as the destination. We find the impact of popularizing EVs on the environment. We also demonstrate the advantages and disadvantages of three types of EVs. In the end, we give recommendations for the government on its role to support and guide the development of EVs.

<!-- b000006 | furniture | pages [2] -->
Team#11893                                             Page 1 of 20

<!-- b000007 | prose | pages [2] -->
An Analysis of the Future Development of

<!-- b000008 | prose | pages [2] -->
Electric Vehicles

<!-- b000009 | heading | pages [2] -->
Introduction:

<!-- b000010 | prose | pages [2] -->
Our models and key factors are shown as follows:

<!-- b000011 | prose | pages [2] -->
Fig. 1

<!-- b000012 | prose | pages [2] -->
In accessing the impacts brought from a new commodity, it often involves many connected or unconnected aspects. Electric vehicles (EVs) are considered to be one of the most promising means to alleviate current shortage and unbalance distribution in power demand. However, on the other hand, the widespread use of EVs is constrained or promoted by the economical, social and technical factors. In our model, we analyzed these factors in a system dependently, we also made a comprehensive evaluation of their influence on EVs.

<!-- b000013 | prose | pages [2, 3] -->
To consider the economical factors, we set up a Static Supply-Demand Model (SSDM) in which relations between oil supply, mileage demand and oil price are introduced. A balance point is calculated in this model and tax rate is regarded as an adjustment factor to it. In the PHEVs-dominant market, a new predicted oil-exhausting year is given due to the decreasing consumption of oil. More information of the consumption by resources types and purpose is offered in LPM. Further, we also give a simple static estimate for the up-bound of the percentage of PHEVs. A more comprehensive dynamic estimate of it is followed in CM.

<!-- b000014 | furniture | pages [3] -->
Team#11893                                             Page 2 of 20

<!-- b000016 | prose | pages [3] -->
Thinking over the social and technical factors, a Competing Ordinary Differential Equation Model (CM) is set up. Different types of EVs (BEVs/HEVs/PHEVs) result into different coefficients in ODEs. According to the variations of coefficients, we get different dynamic amount-trend of EVs and CVs. The environmental impaction of different types of EVs is introduced in LPM by different constrains.

<!-- b000017 | prose | pages [3] -->
With regard to the factors of environment and resources, we set up a Linear Programming Model (LPM) for Optimum Energy Distribution. The optimum energy flows of different type resources are given with Energy Flow by Source and Sector Diagram. The result is also affected by the type of EVs according to different combined energy efficient.

<!-- b000018 | heading | pages [3] -->
Static Supply-Demand Model

<!-- b000019 | heading | pages [3] -->
Notations

<!-- b000020 | prose | pages [3] -->
S :Daily oil supply amount in Thousand Barrels per day(TB)

<!-- b000021 | prose | pages [3] -->
D :Yearly vehicle travel demand in Billion Km(BK)

<!-- b000022 | prose | pages [3] -->
P :Oil price in Dollars per Barrel ($/bbI)

<!-- b000023 | prose | pages [3] -->
Smax :Maximum daily oil supply amount

<!-- b000024 | prose | pages [3] -->
Dmin :Minimum yearly vehicle travel demand

<!-- b000025 | prose | pages [3] -->
Smin :Daily oil supply amount except for transportation

<!-- b000026 | prose | pages [3] -->
C :Oil consumption per 100 kilometers in Liter/Hundred Kilometers(L/HK)

<!-- b000027 | prose | pages [3] -->
μ1 :Proportion of oil consumption for transportation

<!-- b000028 | prose | pages [3] -->
μ2 : Efficiency of converting petroleum to gasoline

<!-- b000029 | prose | pages [3] -->
V : Volume of one barrel of oil in liter (L)

<!-- b000030 | prose | pages [3] -->
R : Tax rate

<!-- b000031 | heading | pages [3] -->
Assumptions

<!-- b000032 | prose | pages [3] -->
1． In a buyer’s market (i.e. in such a market, supply is greater than demand), the relationship between market price and consumption reflects the relationship between price and demand.

<!-- b000033 | prose | pages [3] -->
2． In a seller’s market (i.e. in such a market, demand is greater than supply), the relationship between market price and consumption reflects the relationship between price and production.

<!-- b000034 | prose | pages [3] -->
3． Supply-demand relationship is the main factor in determining price, without regard to other factors such as political or economic state.

<!-- b000035 | prose | pages [3] -->
4． The consumption amount of oil will not have direct influence over power generation amount or electricity price.

<!-- b000036 | prose | pages [3] -->
5． The relationships above are independent of time, that is, they will not change over time.

<!-- b000037 | furniture | pages [4] -->
Team#11893                                             Page 3 of 20

<!-- b000038 | heading | pages [4] -->
The Foundation of Model

<!-- b000039 | prose | pages [4] -->
dS S   k 1( ) 1 d P S max dD D   k 1( ) 2 d P D min   D k ( S S ) 3 min

<!-- b000040 | prose | pages [4] -->
1k 2k Where , are undetermined coefficients. They demonstrate the relationship between  1 V  k3 S,D and P. stands for the travel distance provided by the energy in one 2 C    S S 1( ) barrel of oil. . min total 1

<!-- b000041 | prose | pages [4] -->
The solutions of the differential equation are:

<!-- b000042 | prose | pages [4] -->
   k P / S S S C 1 e 1 max max    k P D / D D C 2 e 2 max max   D k ( S S ) 3 min

<!-- b000043 | heading | pages [4] -->
The Solution of the Model

<!-- b000044 | heading | pages [4] -->
1. The determination of variables

<!-- b000045 | prose | pages [4] -->
C Conventional oil-fuel car: =10(L/HK)

<!-- b000046 | prose | pages [4] -->
  Hybrid electric car:       C =5(L/HK), V = 159L = 20% = 72% , , 2 1

<!-- b000047 | prose | pages [4] -->
3  k 0.0458 In conclusion, for conventional oil-fuel cars, (BK/TB), while for hybrid 3  k 0.0916 electric cars, (BK/TB).

<!-- b000048 | prose | pages [4] -->
 min S 84000 S 23520 (TB) (Data in 2009), (TB). total

<!-- b000049 | heading | pages [4] -->
2. The fitting of equation

<!-- b000050 | prose | pages [4] -->
When looking at the trend of oil price and oil consumption, we can find that between 1980 and 1994, the oil price went up as production declined, while between 1999 and 2006, the oil price increased as production went up. Therefore, we can take the market as buyer’s market between 1980 and 1994, as seller’s market between 1999 and 2006, and as supply-demand balance market between 1995 and 1998. We use data [Scott M. Festin 1996] between 1980 and 1994 to fit demand-price equation, and use data between 1999 and 2006 to fit supply-price equation. The results are as following:

<!-- b000051 | prose | pages [4] -->
max  min  1  S 90300 D 636.27 k 2339 (TB) (BK)

<!-- b000052 | prose | pages [4] -->
2  C  C  k 13 . 23 1 20859 2 -3988

<!-- b000053 | heading | pages [4] -->
3. The equilibrium points

<!-- b000054 | prose | pages [4] -->
Returning the values of the variables back to the equations, we can find the equilibrium points of completely employing conventional oil-fuel car or completely employing hybrid electric car:

<!-- b000055 | furniture | pages [5] -->
Team#11893                                             Page 4 of 20

<!-- b000056 | prose | pages [5] -->
Type of Vehicle P($/bbI) S(TB) D(BK)

<!-- b000057 | prose | pages [5] -->
PHEV(Plug-in Hybrid 17.33 76983.19 3417.51 Electric Vehicle)

<!-- b000058 | prose | pages [5] -->
CV(Conventional Vehicle) 55.27 85315.55 1899.53

<!-- b000059 | prose | pages [5] -->
Tbl. 1

<!-- b000060 | prose | pages [5] -->
According the data of 2006, our result of CV’s equilibrium point is closed to the realistic value. So this model is reliable basing on above analysis.

<!-- b000061 | prose | pages [5] -->
4000

<!-- b000062 | prose | pages [5] -->
3500

<!-- b000063 | prose | pages [5] -->
3000

<!-- b000064 | prose | pages [5] -->
2500 D 3 1 2000

<!-- b000065 | prose | pages [5] -->
1500

<!-- b000066 | prose | pages [5] -->
1000

<!-- b000067 | prose | pages [5] -->
2 20 40 2 60 4 80 6 100 8 120 140 10 4 P x 10 S Fig. 2

<!-- b000068 | prose | pages [5] -->
Line 1 and line 2 stand for the relationship between oil price and demand from consumer’s perspective. Line 3 stands for the relationship between oil price and supply amount from supplier’s perspective. Their intersections are equilibrium points. The point denoted by a circle is the equilibrium point of PHEV. The point denoted by a block is the equilibrium point of CV. We can see that if CVs were totally replaced by PHEVs, both the price and demand of oil would decline, while the travel distance would extend under equilibrium.

<!-- b000069 | heading | pages [5] -->
4. PHEV and Tax

<!-- b000070 | heading | pages [5] -->
1) The PHEVs’ impaction on the oil tax

<!-- b000071 | prose | pages [5] -->
A main reason that the government levies high tax on oil is to keep the supply and demand of oil in balance. If we used the PHEVs to replace most of the CVs, the pressure on oil demand would be remarkably relieved. Suppose that the tax rate on oil (R) is in proportion to the oil price (P). By collecting correlating data,We obtain:

<!-- b000072 | prose | pages [5, 6] -->
R    R P 13 . 27 HEV HEV P R    R P 42 . 38 CV CV P  R S     HEV HEV 100 % 28 . 25 % The tax rate ratio:  R S CV CV

<!-- b000073 | furniture | pages [6] -->
Team#11893                                             Page 5 of 20

<!-- b000075 | prose | pages [6] -->
The calculations above are based on the static supply-demand model, so we did not take into account the impact of tax rate on S-P curve, or the change of D-P curve over time. The result shows that after the employment of PHEVs, under the dual effects of the declination of oil consumption and oil tax rate, the total amount of tax on oil will decrease notably.

<!-- b000076 | prose | pages [6] -->
2)The oil tax’s impaction on the PHEVs

<!-- b000077 | prose | pages [6] -->
In the oil market, the variation of oil tax rate will result in change of the S-P relation. One part of the increasing tax is included in the increasing price of oil, the other part is P balanced with the decreasing profits. We define the as the percentage of increasing oil rise  D % price. The sensitivity analysis of is followed. cv

<!-- b000078 | prose | pages [6] -->
22% 16% 12% 8% P rise

<!-- b000079 | prose | pages [6] -->
-14% -12% -8.5% -5.3%  D % cv

<!-- b000080 | prose | pages [6] -->
Tbl. 2

<!-- b000081 | prose | pages [6] -->
D To balance the demand of travel miles, the decreasing will lead to the rising cv

<!-- b000082 | prose | pages [6] -->
demand of PHEVs. As a result, enhancing the oil tax rate will promote the widespread use of PHEVs.

<!-- b000083 | heading | pages [6] -->
5. Impact on oil stock

<!-- b000084 | prose | pages [6] -->
In the above, we only considered the impact of supply-demand relationship on price. From the results we have obtained, we know that using PHEVs fails to remarkably decrease the consumption of oil (76983.19 VS 85315.55), but we can also see that after using PHEVs, the same amount of oil consumption could meet larger demand. Therefore, in order to balance the oil consumption, we define the consuming efficiency of oil as the travel distance demand satisfied when consuming one unit of oil:

<!-- b000085 | prose | pages [6] -->
      4 D / 356 S .1 25 10 （ ） HEV SEV HEV  ）

<!-- b000086 | heading | pages [6] -->
D S

<!-- b000087 | prose | pages [6] -->
/ 365 （       5 D / 356 S .6 26 10 （ ） CV CV CV

<!-- b000088 | prose | pages [6] -->
 6 S = 1,143.355 10 TB From data we know: (2007) reserve

<!-- b000089 | prose | pages [6, 7] -->
     5 D ( total ) S .1 42 10 SEV reserve HEV More travel distance it can still supply:      4 D ( total ) S .7 16 10 CV reserve CV 5 x 10 7

<!-- b000090 | furniture | pages [7] -->
Team#11893                                             Page 6 of 20

<!-- b000092 | prose | pages [7] -->
6 Accumulative D from 1980 5

<!-- b000093 | prose | pages [7] -->
4

<!-- b000094 | prose | pages [7] -->
3 D(HEV)

<!-- b000095 | prose | pages [7] -->
D(CV) 2

<!-- b000096 | prose | pages [7] -->
1

<!-- b000097 | prose | pages [7] -->
0 1980 1990 2000 2010 2020 2030 2040 2050 2060 2070 year

<!-- b000098 | prose | pages [7] -->
Fig. 3

<!-- b000099 | prose | pages [7] -->
From the figure above we can see that according to the present trend of demand, completely using CVs will consume up present oil stock in 2020, while completely using CVs will consume up present oil stock in 2029.

<!-- b000100 | heading | pages [7] -->
6. Computation of Electricity Margin

<!-- b000101 | prose | pages [7] -->
Reasonably, the increasing widespread use of electricity vehicles will lead to the rising of electricity consumption. However, the realistic amount of EVs has a up bound due to the limitation of total electricity installed capacity.

<!-- b000102 | prose | pages [7] -->
We defineas the rate of electricity generation (i.e., the ratio of total electricity production to total installed capacity times working hours):

<!-- b000103 | prose | pages [7] -->
total electricit y production   i denotes the type of electricit y generation ，   working hours installed capacity i i i We made the assumption that the power plants except for thermal ones work under full load, which means they work 24 hours per day (hpd). The-year curve is the upper one in Fig. 4 when there is no additional production of thermal electricity, the middle one when thermal power plants work 16 hpd, the lower one when thermal power plants work 20 hpd. Fig. 4 shows the rise of electricity demand.

<!-- b000104 | prose | pages [7] -->
0.9

<!-- b000105 | prose | pages [7] -->
0.85 Percentage of Electricity Capacity no additional thermal electricity 20hpd full load 16hpd full load 0.8

<!-- b000106 | prose | pages [7] -->
0.75

<!-- b000107 | prose | pages [7] -->
0.7

<!-- b000108 | prose | pages [7] -->
0.65

<!-- b000109 | prose | pages [7] -->
0.6

<!-- b000110 | prose | pages [7] -->
0.55

<!-- b000111 | prose | pages [7] -->
0.5 1980 1985 1990 1995 2000 2005 2010 year

<!-- b000112 | prose | pages [7] -->
Fig. 4

<!-- b000113 | prose | pages [7] -->
To access the capacity of producing additional electricity, we define as the electricity  1   margin:

<!-- b000114 | furniture | pages [8] -->
Team#11893                                             Page 7 of 20

<!-- b000115 | prose | pages [8] -->
Thermal electricity No additional 16phd full load 20phd full load

<!-- b000116 | prose | pages [8] -->
averagefrom 2002 to 2006 12% 28% 42%

<!-- b000117 | prose | pages [8] -->
Tbl. 3

<!-- b000118 | prose | pages [8] -->
Fig. 5

<!-- b000119 | prose | pages [8] -->
Source: Lawrence Berkeley National Laboratory

<!-- b000120 | prose | pages [8] -->
http://www.mpoweruk.com/electricity_demand.htm

<!-- b000121 | caption | pages [8] -->
Fig. 5 is the electricity daily demand:(1)As to the BEVs, their endurance mileage is

<!-- b000122 | prose | pages [8] -->
relatively small so that a part of their charging would be in on-peak hours(daytime, especially at noon). The electricity margin of BEVs is small because the electricity generation in on-peak hours is nearly under full load. We set it to be the  under 16 phd; (2)As to the PHEVs, because of their longer endurance mileage, most of their charging world be in off-peak hours when the utilization of electricity is much lower than it in on-peak hours. In this sense, their electricity margin is larger. We set it to be the  under 20 phd. These two margins will be used in LPM

<!-- b000123 | prose | pages [8] -->
Without additional thermal electricity generation, we calculated the ratio of PHEVs to total vehicles and the ratio of CVs to total vehicles at the Critical point (upper bound) of 3k electricity margin. The result is 38.5% and 61.5% respectively. The coefficient is 0.0634 accordingly.

<!-- b000124 | prose | pages [8] -->
Type of Vehicle P($/bbI) S(TB) D(BK)

<!-- b000125 | prose | pages [8] -->
38.5%PHEV and 61.5%CV 36 82000 2520

<!-- b000126 | prose | pages [8] -->
Tbl. 4

<!-- b000127 | prose | pages [8] -->
The result shows that present thermal power generation amount will limit the number of electric cars. If we want to further popularize electric cars, we need to generate more electricity, which will lead to more new energy demand or more pollution. To comprehensively access the impact of using more fossil fuels to generate electricity on environment, we need analyze how to choose and arrange the types of power generation so that the pollution will be the least. We will give an analysis in LPM. As shown above, here we give a static upper bound of the PHEVs’ percentage. To have a dynamic result of the amount of CVs and different type EVs, we set up following Competition Model.

<!-- b000128 | furniture | pages [9] -->
Team#11893                                             Page 8 of 20

<!-- b000129 | heading | pages [9] -->
Competing Ordinary Differential Equation Model

<!-- b000130 | heading | pages [9] -->
Notations

<!-- b000131 | prose | pages [9] -->
1x : The total number of electric cars

<!-- b000132 | prose | pages [9] -->
2x : The total number of all kinds of cars (conventional cars)

<!-- b000133 | prose | pages [9] -->
ia :The influential parameter

<!-- b000134 | prose | pages [9] -->
ib : The influential parameter

<!-- b000135 | prose | pages [9] -->
W :Covering rate of infrastructure

<!-- b000136 | prose | pages [9] -->
S :Endurance mileage

<!-- b000137 | prose | pages [9] -->
E :Maximum power generation ability max

<!-- b000138 | heading | pages [9] -->
Basic Assumptions

<!-- b000139 | prose | pages [9] -->
1. Electric cars mainly refer to hybrid electric cars.

<!-- b000140 | prose | pages [9] -->
1a , 2a , 1b , 2b are constants, because they are determined by the specifications 2. of the cars themselves instead of exterior factors.

<!-- b000141 | prose | pages [9] -->
0a , 0b will change according to exterior factors. 3.

<!-- b000142 | heading | pages [9] -->
The Foundation of Ordinary Differential Equation Model

<!-- b000143 | prose | pages [9] -->
We build the model below to analyze the relationship of quantity change between conventional and electric cars. The model is based on a two-element ordinary differential equation:

<!-- b000144 | prose | pages [9] -->
 dx    1 a a x a x  0 1 1 2 2 dt  dx     2 b b x b x 0 1 1 2 2  dt

<!-- b000145 | prose | pages [9] -->
dx1 is the change rate of the total of electric cars dx2 is the change rate 1x where dt , dt 2x of the total of conventional cars . Because we do not know the exact relations dx1 , 1x x2 between and , here we follow the engineers’ advice: Using linear relation where dt you don’t know the exact relation.

<!-- b000146 | prose | pages [9] -->
2a 1a 2b 1b 0a In this equation group, the meanings of unknown parameters , , , , , 0b are :

<!-- b000147 | prose | pages [9] -->
Correlated coefficient of change rate of the total number of electric cars, 2a which is determined by factors such as competition between two types of cars, etc.

<!-- b000148 | prose | pages [9] -->
Coefficient of change rate of the total number of electric cars, which is 1a determined by factors such as the saturation of electric car market, etc.

<!-- b000149 | furniture | pages [10] -->
Team#11893                                             Page 9 of 20

<!-- b000150 | prose | pages [10] -->
Change rate of the total number of electric cars, which is determined by other 0a factors such as the fluctuation of electricity price, etc.

<!-- b000151 | prose | pages [10] -->
Coefficient of change rate of the total number of conventional cars, which is 2b determined by factors such as the saturation of conventional car market, etc.

<!-- b000152 | prose | pages [10] -->
Correlated coefficient of change rate of the total number of conventional cars, 1b which is determined by factors such as competition between two types of cars, the impact of the popularization of electric cars on conventional cars, etc.

<!-- b000153 | prose | pages [10] -->
Change rate of the total number of conventional cars, which is determined by 0b other factors such as the fluctuation of fuel price, etc.

<!-- b000154 | prose | pages [10] -->
Tbl. 5

<!-- b000155 | prose | pages [10] -->
The steady solution of the ODE above is:

<!-- b000156 | prose | pages [10] -->
  a b a b  2 0 0 2 x   1  a b a b 1 2 2 1   a b a b   0 1 1 0 x  2   a b a b  1 2 2 1

<!-- b000157 | heading | pages [10] -->
The Solution of the Previous Model

<!-- b000158 | prose | pages [10] -->
According to the data in Appendix_2,and from the theory of ordinary differential equation, we can deduce the solutions of the equations have the forms below:

<!-- b000159 | prose | pages [10] -->
    t x m m L 1 0 1     t x n n L  2 0 1

<!-- b000160 | prose | pages [10] -->
By using least squares fitting, we obtain

<!-- b000161 | prose | pages [10] -->
      6 6 t x .1 272 10 .1 673 10 .0 8294 1       8 7 t x .2 592 10 .3 921 10 .0 8294  2

<!-- b000162 | prose | pages [10] -->
1      7 a .1 741 a .0 0822 a .1 910 10 Thus, , , , 2 0    103   9 2 b .4 915 b .1 10 b .1 347 10 , , . 2 0 1

<!-- b000163 | heading | pages [10] -->
Validation of a1,b1, a2,b2

<!-- b000164 | prose | pages [10] -->
1  1  a 0 b 0 , shows that the use of electric cars will promote the use of both conventional cars and electric cars. According to the static supply-demand balance model, the use of electric cars can lower the oil price, which leads to the decline of the using cost of both electric cars and conventional cars. The decline of fuel fee further motivates the demand in the car market.

<!-- b000165 | prose | pages [10] -->
2  2  a 0 b 0 , demonstrates that the use of conventional oil-fuel cars will restrict the demand in the car market. The reason is also based on the static supply-demand balance model: the use of conventional oil-fuel cars will raise the oil price, which is negative for the demand.

<!-- b000166 | prose | pages [10] -->
We can draw a figure to show the result:

<!-- b000167 | furniture | pages [11] -->
Team#11893                                             Page 10 of 20

<!-- b000168 | prose | pages [11] -->
8 2.6 x 10

<!-- b000169 | prose | pages [11] -->
2.55 fitting curve real data 2.5

<!-- b000170 | prose | pages [11] -->
Number of Ordinary Cars 2.45

<!-- b000171 | prose | pages [11] -->
2.4

<!-- b000172 | prose | pages [11] -->
2.35

<!-- b000173 | prose | pages [11] -->
2.3

<!-- b000174 | prose | pages [11] -->
2.25

<!-- b000175 | prose | pages [11] -->
2.2

<!-- b000176 | prose | pages [11] -->
2.15 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 Years

<!-- b000177 | prose | pages [11] -->
Fig. 6

<!-- b000178 | prose | pages [11] -->
8 x 10 3

<!-- b000179 | prose | pages [11] -->
2.5

<!-- b000180 | prose | pages [11] -->
Estimated Number of Electric Cars Estimated Number of Ordinary Cars 2 Real Data of Electric Cars Number of Cars Real Data of Ordinary Cars

<!-- b000181 | prose | pages [11] -->
1.5

<!-- b000182 | prose | pages [11] -->
1

<!-- b000183 | prose | pages [11] -->
0.5

<!-- b000184 | prose | pages [11] -->
0 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 Year

<!-- b000185 | prose | pages [11] -->
Fig. 7

<!-- b000186 | prose | pages [11] -->
The first figure gives a proof of the soundness of the model and the fitting variables. The second figure shows that the amount of conventional cars and electric cars will increase to a fixed value, not infinity. This is in accord with the fact.

<!-- b000187 | prose | pages [11] -->
Discussions about Parameters a0,b0

<!-- b000188 | prose | pages [11] -->
a and 0b are constants which are criteria for the competitive ability of cars 0 determined by factors such as technology level, infrastructures, and policies, etc. Because 0b technologies and infrastructures of conventional cars have been determined firmly, will not change a lot.

<!-- b000189 | prose | pages [11] -->
a As for , we can suppose it has the form as below: 0

<!-- b000190 | prose | pages [11] -->
a  k WSE 0 max

<!-- b000191 | prose | pages [11] -->
W k Where is an undetermined coefficient. is named as the covering rate of the W  0 1 S infrastructures of electric cars ( ). is the endurance mileage, which is determined E by battery and charging technology. is the maximum power generation ability. It will max exert restriction or motivation on electric cars.

<!-- b000192 | furniture | pages [12] -->
Team#11893                                             Page 11 of 20

<!-- b000193 | heading | pages [12] -->
Sensitivity analysis of a0 on electric cars :

<!-- b000194 | prose | pages [12] -->
7 x 10 3 a0'=a0 a0'=1.1*a0 a0'=1.2*a0 2.5 a0'=1.3*a0 a0'=1.4*a0 2 a0'=1.5*a0

<!-- b000195 | prose | pages [12] -->
x1 1.5

<!-- b000196 | prose | pages [12] -->
1

<!-- b000197 | prose | pages [12] -->
0.5

<!-- b000198 | prose | pages [12] -->
0 0 10 20 30 40 50 60 70 80 90 100 t

<!-- b000199 | prose | pages [12] -->
Fig. 8

<!-- b000200 | prose | pages [12] -->
a As shown in figure*, larger represents more competitiveness of EVs or more 0

<!-- b000201 | prose | pages [12] -->
a coverage of infrastructures, that is to say, includes the information about EVs’ type. 0

<!-- b000202 | prose | pages [12] -->
Competitiveness of EVs mainly includes the technique and the pollution. The more

<!-- b000203 | prose | pages [12] -->
a friendliness to environment, the more support from government will be given, so will be 0

<!-- b000204 | prose | pages [12] -->
larger. To access the environment impact of different type EVs, a model to optimize energy distribution is followed.

<!-- b000205 | heading | pages [12] -->
Linear Programming Model for Optimum Energy

<!-- b000206 | prose | pages [12] -->
Distribution

<!-- b000207 | heading | pages [12] -->
Notations

<!-- b000208 | prose | pages [12] -->
ijx : Energy transferred from Supply Source i to Demand Sector j

<!-- b000209 | prose | pages [12] -->
: Energy transferred from Electric Power sector to Transportation sector after cx the popularization of electric cars

<!-- b000210 | prose | pages [12] -->
B : Energy Demand Sector j j

<!-- b000211 | prose | pages [12] -->
i iA : Energy Supply Sources

<!-- b000212 | prose | pages [12, 13] -->
:Environmental cost (pollution produced) when converting energy from ijP Supply Source i to Demand Sector j  : Efficiency of converting heat to electricity 1

<!-- b000213 | furniture | pages [13] -->
Team#11893                                             Page 12 of 20

<!-- b000215 | prose | pages [13] -->
: Energy efficiency of electric cars compared to traditional cars, i.e., the ratio  of energy consumed by traditional cars to electric cars under the same 2

<!-- b000216 | prose | pages [13] -->
 : Combined energy efficiency of electric cars, which is  1  2

<!-- b000217 | prose | pages [13] -->
O : Fuel consumption per 100 kilometers of traditional cars 100

<!-- b000218 | prose | pages [13] -->
E : Energy produced by electric cars under the consumption of one unit of oil

<!-- b000219 | prose | pages [13] -->
E :Electricity consumption per 100 kilometers of traditional cars 100

<!-- b000220 | prose | pages [13] -->
:Environmental cost of the total amount of pollution caused by energy P ALL consumption

<!-- b000221 | heading | pages [13] -->
Assumptions

<!-- b000222 | prose | pages [13] -->
1. We only model under ideal situation, that is, the whole energy system is working under the condition which meets the optimal solution of linear programming.

<!-- b000223 | prose | pages [13] -->
2. The environmental cost can fully reflect the pollution caused by using different types of energy.

<!-- b000224 | prose | pages [13] -->
3. Most EVs are HEVs (Hybrid Electric Vehicles), but there are also BEVs (Battery Electric Vehicles) and PHEVs (Plug-in Electric Vehicles).

<!-- b000225 | heading | pages [13] -->
The Foundation of A Linear Programming Model for Optimum Energy

<!-- b000226 | prose | pages [13] -->
Distribution

<!-- b000227 | prose | pages [13] -->
x 11

<!-- b000228 | prose | pages [13] -->
Fig. 9

<!-- b000229 | prose | pages [13, 14] -->
The distribution of the energy network is shown as in Fig. 9.Considering that the demands must still be satisfied after the redistribution of energy flow, we can have the following constraints:

<!-- b000230 | furniture | pages [14] -->
Team#11893                                             Page 13 of 20

<!-- b000232 | prose | pages [14] -->
       . . S t x x x x B 11 21 41 1 2 c 1     x x x x B 12 22 32 42 2     x x x x B 13 23 33 43 3      x x x x x B 14 24 44 54 c 4  0 x ij

<!-- b000233 | prose | pages [14] -->
 is efficiency of converting heat to electricity. Based on data from where 1 is [http://en.wikipedia.org/wiki/Cogeneration], 1   3.0 when energy is generated by Electricti ty only plants    1    8.0 when energy is generated by combined heat and power ( CHP ) plants   O E   100 , it stands for energy efficiency of electric cars compared to traditional cars. 2 E 100     To obtain the combined efficiency, let , 1 2

<!-- b000234 | prose | pages [14] -->
The environmental cost of the total amount of pollution caused by energy consumption is

<!-- b000235 | prose | pages [14] -->
5 4    P x P ALL ij ij   i 1 j 1

<!-- b000236 | prose | pages [14] -->
P As our goal is to minimize the environmental cost , we propose the following LP ALL formulation for the single destination problem.

<!-- b000237 | prose | pages [14] -->
5 4   min x P ij ij   i 1 j 1         S .. t x x x x B 11 21 41 1 2 c 1     x x x x B 12 22 32 42 2     x x x x B 13 23 33 43 3      x x x x x B 14 24 44 54 c 4  x 0 ij

<!-- b000238 | heading | pages [14] -->
The Solution of The Linear Programming Model for Optimum Energy

<!-- b000239 | prose | pages [14] -->
Distribution

<!-- b000240 | heading | pages [14] -->
1. The Solution of the Basic Model

<!-- b000241 | prose | pages [14] -->
In economy, Environmental Cost is commonly used as a criterion to measure the extent of pollution. According to [Shuying Ding 2006] and taking reality into account, we list different conditions in the table below:

<!-- b000242 | prose | pages [14] -->
Mathematical No. Constraint Explanation Expression

<!-- b000243 | prose | pages [14, 15] -->
Constraint on the total Existing installed capacity of solar, wind 4  4  x 7.7 1 amount of energy of and water power determines the j Renewable Energy maximum amount of energy supplied by  j 1 Constraint on the total 54  x 2 amount of energy of Nuclear Electric Power

<!-- b000244 | furniture | pages [15] -->
Team#11893                                             Page 14 of 20

<!-- b000246 | prose | pages [15] -->
Constraint on the total 4  2  x 3 amount of energy of j Natural Gas  j 1

<!-- b000247 | prose | pages [15] -->
Constraint on the total 4  1  x 4 amount of energy of j Petroleum  j 1

<!-- b000248 | prose | pages [15] -->
cx Constraint on (energy transferred from Electric  Power sector to cx 5 Transportation sector after the popularization of electric cars)

<!-- b000249 | prose | pages [15] -->
x Constraint on (energy 11 transferred from Petroleum 11  12 x 6 source to Transportation sector)

<!-- b000250 | prose | pages [15] -->
x Constraint on (energy 11 transferred from Coal 34  x 15 7 source to Electric Power sector)

<!-- b000251 | prose | pages [15] -->
x Constraint on (energy 11 transferred from Renewable 44  x 8 Energy source to Electric Power sector) Renewable Energy.

<!-- b000252 | prose | pages [15] -->
Existing installed capacity of nuclear 3.8 power determines the maximum amount of energy supplied by nuclear power.

<!-- b000253 | prose | pages [15] -->
Existing natural gas drilling amount 23 4. determines the maximum amount of natural gas supply.

<!-- b000254 | prose | pages [15] -->
Obtained from the infinite value of the 38 fitted S-P curve in the supply-demand model.

<!-- b000255 | prose | pages [15] -->
Estimated from the energy transferred 10 from transportation to electric power.

<!-- b000256 | prose | pages [15] -->
Based on Assumption 3; and suppose that . 708 half of the energy consumed by HEVs are provided by gasoline.

<!-- b000257 | prose | pages [15] -->
Calculated by real power generation . 65 efficiency and installed capacity of coal.

<!-- b000258 | prose | pages [15] -->
Calculated by real power generation 7 efficiency and installed capacity of Renewable Energy.

<!-- b000259 | prose | pages [15] -->
Tbl. 6

<!-- b000260 | prose | pages [15] -->
Adding these constraints to previous model, we get the following figure:

<!-- b000261 | prose | pages [15] -->
120 Original Condition No Restriction Restriction No.3+No.4 100 Restriction No.3+No.4(loosed by 2 times) Restriction No.3+No.4+No.5 Restriction No.1~No.10 Energy(Quadrillion Btu) 80

<!-- b000262 | prose | pages [15] -->
60

<!-- b000263 | prose | pages [15] -->
40

<!-- b000264 | prose | pages [15] -->
20

<!-- b000265 | prose | pages [15] -->
0 Petroleum Natural Gas Coal Renewable Energy Nuclear Electric Power Different Kinds of Supply Sources

<!-- b000266 | prose | pages [15, 16] -->
Fig. 10 We can see, if there were no constraints, the optimal distribution of energy would be to use Renewable Energy as supply source completely, and the second best choice would be Nuclear Electric Power. Under real conditions, it is impossible to completely use Renewable Energy and Nuclear Electric Power as energy supply sources. Considering constraints No.3 and No. 4 (listed in Tbl. 6), we can find that the result of the LP formation shows it is more reasonable to use Natural Gas.

<!-- b000267 | furniture | pages [16] -->
Team#11893                                             Page 15 of 20

<!-- b000269 | prose | pages [16] -->
However, because of limited usable quantity, it is still impossible to use Natural Gas as first-choice energy supply source. Thus, we have to add constraint No.5 to improve our model. Considering other concrete factors, such as the structure of energy industry, the upper limit of energy, etc., we finally propose the linear programming model with constraints No.1-No.10.

<!-- b000270 | prose | pages [16] -->
Based on the discussions and analysis above, we can ensure the order of priority of energy supply sources as below: Renewable Energy>Nuclear Electric Power>Natural ijP Gas>Petroleum>Coal, which accords with the data of the environmental cost .

<!-- b000271 | prose | pages [16] -->
P Now we show the total amount of environmental cost of energy consumption under ALL six different combinations of constraints (listed in the legend of the figure above) in a new figure:

<!-- b000272 | prose | pages [16] -->
60

<!-- b000273 | prose | pages [16] -->
50

<!-- b000274 | prose | pages [16] -->
40

<!-- b000275 | prose | pages [16] -->
PALL 30

<!-- b000276 | prose | pages [16] -->
20

<!-- b000277 | prose | pages [16] -->
10

<!-- b000278 | prose | pages [16] -->
0 No Restriction Restriction No.3+No.4 Restriction No.3+No.4(loosed by 2 times) Restriction No.3+No.4+No.5 Restriction No.1-No.10 Different Kinds of Restrictions

<!-- b000279 | prose | pages [16] -->
Fig. 11

<!-- b000280 | prose | pages [16] -->
We can roughly observe that the looser the constraints, the lower the environmental P cost , correspondingly the better the environment. ALL

<!-- b000281 | heading | pages [16] -->
2. Sensitivity Analysis for Ordinary Condition

<!-- b000282 | prose | pages [16, 17] -->
Subsequently, by using the ultimate model with constraints No.1-No.8 and changing the value of , we create the figure below to demonstrate energy distribution and energy transferred from Electric Power sector to Transportation sector after the popularization of X electric cars( ). c 40 =0.5 Critical Point:=0.85 =0.6 35 =0.7 =0.8 =0.9 30 =1.0 Energy(Quadrillion Btu) =1.1 25 =1.2 =1.3 =1.4 20 =1.5 =2 Critical Point:=0.85 15 =3 =4 10

<!-- b000283 | furniture | pages [17] -->
Team#11893                                             Page 16 of 20

<!-- b000285 | prose | pages [17] -->
5

<!-- b000286 | prose | pages [17] -->
0 Petroleum Natural Gas Coal Renewable Energy Nuclear Electric Power  Energy Transmission(Xc) Different Kinds of Supply Sources and ...

<!-- b000287 | prose | pages [17] -->
Fig. 12

<!-- b000288 | prose | pages [17] -->
    .0 85 .0 85 From the figure above we can find a Critical Point: . That is, when ,   X .0 85 the demand of coal is a constant, and keeps being zero. But when , the c X demand of coal begins to decrease, while becomes a non-zero constant and starts to c  is larger than 1.4. decrease after

<!-- b000289 | prose | pages [17] -->
 values in a curve: P Now we show the environmental cost under different ALL

<!-- b000290 | prose | pages [17] -->
60

<!-- b000291 | prose | pages [17] -->
58

<!-- b000292 | prose | pages [17] -->
Critical Point: 56 =0.85

<!-- b000293 | prose | pages [17] -->
PALL 54

<!-- b000294 | prose | pages [17] -->
52

<!-- b000295 | prose | pages [17] -->
50

<!-- b000296 | prose | pages [17] -->
48 0.5 1 1.5 2 2.5 3 3.5 4 

<!-- b000297 | prose | pages [17] -->
Fig. 13

<!-- b000298 | prose | pages [17] -->
  .0 85 We can see that is still a Critical Point. Besides, it is easy to find that when   .0 85 P , the environmental cost is decreasing, which means the environment is ALL dPALL is going down, which shows the improving. However, we can also notice that  d effect of improving environment by lifting  is declining.

<!-- b000299 | furniture | pages [18] -->
Team#11893                                             Page 17 of 20

<!-- b000300 | heading | pages [18] -->
3. Sensitivity Analysis for BEV, HEV, and PHEV

<!-- b000301 | prose | pages [18] -->
The electric vehicles in the market can be categorized into three major types: BEV, HEV, and PHEV. Because their power generation mechanisms are different, the optimal environmental costs of them are different under same energy condition. Besides, the proportion of fossil fuels they consume will be different. Thus, based on previous results of linear programming and new constraints derived from the characteristics of different cars, we can give a new solution of the problem. Consider the conditions when the electric vehicles in the market are all BEVs, HEVs or PHEVs separately, and list the constraints under each condition as following:

<!-- b000302 | prose | pages [18] -->
Type Constraint Explanation

<!-- b000303 | prose | pages [18] -->
The source of energy for transportation will not be restricted 11  x 0 by oil now. BEV  cx 15 Calculated from electricity margin.

<!-- b000304 | prose | pages [18] -->
1 Suppose more than half of the amount of energy for   x 25 . 416 transportation is provide by oil. 11 2 PHEV  cx 28 Calculated from electricity margin.

<!-- b000305 | prose | pages [18] -->
Converted and estimated from the fuel consumption of 100 11  10 x kilometers of Toyota Prius and conventional cars. HEV  cx 0 HEVs cannot get power from electricity grid directly.

<!-- b000306 | prose | pages [18] -->
Tbl.7

<!-- b000307 | prose | pages [18] -->
Solving the three linear programming problems above, we can first get a curve which shows the change of the total environmental cost over the combined energy efficiency of electric cars :

<!-- b000308 | prose | pages [18] -->
60 Original Pollution BEV's Pullution PHEV's Pullution 55 HEV's Pullution

<!-- b000309 | prose | pages [18] -->
50

<!-- b000310 | prose | pages [18] -->
PALL 45

<!-- b000311 | prose | pages [18] -->
40

<!-- b000312 | prose | pages [18] -->
35

<!-- b000313 | prose | pages [18] -->
30 0 1 2 3 4 5 6 7 8 

<!-- b000314 | prose | pages [18] -->
Fig. 14

<!-- b000315 | prose | pages [18] -->
By analyzing this figure we can find:

<!-- b000316 | furniture | pages [19] -->
Team#11893                                             Page 18 of 20

<!-- b000317 | prose | pages [19] -->
 BEV is always better than PHEV in the respect of environment protection.

<!-- b000318 | prose | pages [19] -->
When the value of  is small, the environmental cost of HEV is lower than that  of BEV or PHEV. But as  increases, HEV is growing worse than BEV or PHEV.

<!-- b000319 | prose | pages [19] -->
To make BEV and PHEV perform better in environment protection,  must be  higher than its value at critical point, while HEV always perform better than current environment situation.

<!-- b000320 | prose | pages [19] -->
Then, we illustrate the energy distribution of the three EV types in separate pie charts   3 when (it means the EV technologies have developed fully):

<!-- b000321 | prose | pages [19] -->
13% 14%

<!-- b000322 | prose | pages [19] -->
< 1% < 1%

<!-- b000323 | prose | pages [19] -->
43%

<!-- b000324 | prose | pages [19] -->
25% 27% 59%

<!-- b000325 | prose | pages [19] -->
3% 16%

<!-- b000326 | prose | pages [19] -->
BEV PHEV

<!-- b000327 | prose | pages [19] -->
15%

<!-- b000328 | prose | pages [19] -->
< 1%

<!-- b000329 | prose | pages [19] -->
45%

<!-- b000330 | prose | pages [19] -->
29%

<!-- b000331 | prose | pages [19] -->
10%

<!-- b000332 | prose | pages [19] -->
HEV

<!-- b000333 | prose | pages [19] -->
Fig. 15

<!-- b000334 | prose | pages [19] -->
From the figures above we can obviously observe that the type of electric vehicles has a great impact on the distribution of electricity.

<!-- b000335 | heading | pages [19] -->
4. Model validation

<!-- b000336 | prose | pages [19] -->
From above analysis, when the  is small, we should popularize HEV to minimize the environmental cost. When  is large enough so that the environment cost of PHEV and BEV is lower than the one of HEV, we should popularize them.

<!-- b000337 | prose | pages [19] -->
Before Toyota Prius released PHEV in 2007, the HEV dominated the EVs’ market, which is in accord with situation of small. After its release, we can observe a decline of sales of HEV from the reference’s data. This validates the crossover point of P- curve in figure * between HEV and PHEV/BEV.

<!-- b000338 | heading | pages [19] -->
Conclusion

<!-- b000339 | furniture | pages [20] -->
Team#11893                                             Page 19 of 20

<!-- b000340 | heading | pages [20] -->
Strengths

<!-- b000341 | prose | pages [20] -->
 Our models are simple but comprehensive, covering five aspects;

<!-- b000342 | prose | pages [20] -->
 Our models have strong robustness due to their independence with types of EV;

<!-- b000343 | prose | pages [20] -->
 Our models validate and complement each other;

<!-- b000344 | prose | pages [20] -->
 Each model is aimed at a special perspective and offers practical recommendations.

<!-- b000345 | heading | pages [20] -->
Weakness

<!-- b000346 | prose | pages [20] -->
 Much of the coefficients in our models are simplified or estimated in statistic;

<!-- b000347 | prose | pages [20] -->
 Some solution plays a guiding role but is not practical or realizable in real world.

<!-- b000348 | heading | pages [20] -->
Recommendation

<!-- b000349 | prose | pages [20] -->
For the Governments

<!-- b000350 | prose | pages [20] -->
1) Governments should increase the oil tax rate to limit the demand of CVs and popularize EVs due to the analysis in SSDM;

<!-- b000351 | prose | pages [20] -->
2) More electricity production and installed capacity is needed to promote the widespread use of EVs, the additional amount is determined by the EV type;

<!-- b000352 | prose | pages [20] -->
3) More charging infrastructures are necessary;

<!-- b000353 | prose | pages [20] -->
cx 4) Based on the linear programming model considering (energy transferred from

<!-- b000354 | prose | pages [20] -->
Electric Power sector to Transportation sector), the order of priority of five energy supply sources is: Renewable Energy>Nuclear Electric Power>Natural Gas>Petroleum>Coal

<!-- b000355 | prose | pages [20] -->
Therefore, the government should first take into consideration the development of supply sources such as Renewable Energy or Nuclear Electric Power so that they could help electric cars produce benefits to environment. As for the benefits of developing different types of energy, we can refer to Fig. 10 and Fig. 11.

<!-- b000356 | prose | pages [20] -->
5) Strategies for developing which type of the electric cars: If our technology developing ability is powerful enough, i.e.,  is high enough, we should develop BEV in priority to gain the most benefits to environment. If our technology developing ability is limited, we should develop HEV in priority, whose benefits to environment have nothing to do with .

<!-- b000357 | prose | pages [20] -->
6) Can we save fossil fuels by widely using electric vehicles? According to the results

<!-- b000358 | prose | pages [20] -->
  .0 85 we have obtained, under the premise that , coals can be saved. Because under the

<!-- b000359 | prose | pages [20] -->
optimal condition, the demands of petroleum and natural gas will exceed their supply amount. Unfortunately, under no conditions could petroleum or natural gas be saved.

<!-- b000360 | prose | pages [20, 21] -->
For the vehicle manufacturers 1) Manufactures should increase the endurance mileage by improve the technique of battery, so that more EVs don’t need charge in on-peak hours.

<!-- b000361 | furniture | pages [21] -->
Team#11893                                             Page 20 of 20

<!-- b000363 | prose | pages [21] -->
  .0 85 2) In the sensitivity analysis section in LPM, we find a critical point , and

<!-- b000364 | prose | pages [21] -->
  .0 85 through analysis we know that only when electric cars can demonstrate their

<!-- b000365 | prose | pages [21] -->
energy economic advantage. So the value of  should be as large as possible.

<!-- b000366 | prose | pages [21] -->
  O E   100 3.0 when energy is generated by Electricti ty only plants  E    1    100   O E 2      100 8.0 when energy is generated by combined heat and power ( CHP ) plants  E  100

<!-- b000367 | prose | pages [21] -->
It is impractical to increase the fuel consumption of traditional cars in order to protect environment. So what we can really do are:

<!-- b000368 | prose | pages [21] -->
E  Minimizing , that is, minimizing the energy consumption of electric cars by 100

<!-- b000369 | prose | pages [21] -->
technical innovations.

<!-- b000370 | prose | pages [21] -->
 Use combined-heat-and-power (CHP) plants to generate power as much as possible.

<!-- b000371 | heading | pages [21] -->
References

<!-- b000372 | references | pages [21] -->
[1] Frank R. Giordano, Maurice D. Weir, William P. Fox. (2005) A First Course in

<!-- b000373 | references | pages [21] -->
Mathematical Modeling, 3rd edition.

<!-- b000374 | references | pages [21] -->
[2] David Tilman. (1994) ‘Competition and Biodiversity in Spatially Structured Habits’,

<!-- b000375 | references | pages [21] -->
Ecology, 75(1), 1994, pp. 2-16

<!-- b000376 | references | pages [21] -->
[3] Sanjaka G. Wirasingha, Nigel Schofield and Ali Emadi. (2008) ‘Feasibility analysis

<!-- b000377 | references | pages [21] -->
of converting a Chicago Transit Authority (CTA) transit bus to a plug-in hybrid electric

<!-- b000378 | references | pages [21] -->
vehicle’, IEEE Vehicle Power and Propulsion Conference (VPPC), September 3-5, 2008,

<!-- b000379 | references | pages [21] -->
Harbin, China

<!-- b000380 | references | pages [21] -->
[4] Shuying Ding. (2006) ‘Calculations on the Cost of Electricity Generation’, Master’s

<!-- b000381 | references | pages [21] -->
Thesis in Zhejiang University, Hangzhou, China.

<!-- b000382 | references | pages [21] -->
[5] Mark M. Meerschaert. (2008) Mathematical Modeling, 3rd edition.

<!-- b000383 | references | pages [21] -->
[6] U.S. Hybrid-Electric Vehicle Sales, 1999-2010.

<!-- b000384 | references | pages [21] -->
http://www.afdc.energy.gov/afdc/data/.

<!-- b000385 | references | pages [21] -->
[7] U.S. Energy Information Administration. (August 2010) Annual Energy Review 2009

<!-- b000386 | references | pages [21] -->
[8] Scott M. Festin. SUMMARY OF NATIONAL AND REGIONAL TRAVEL RENDS:

<!-- b000387 | references | pages [21] -->
1970-1995, Office of Highway Information Management

<!-- b000388 | references | pages [22] -->
Appendix_1

<!-- b000389 | references | pages [22] -->
From International Energy Annual 2006’s data of oil and SUMMARY OF NATIONAL AND

<!-- b000390 | references | pages [22] -->
REGIONAL TRAVEL TRENDS:1970-1995,

<!-- b000391 | references | pages [22] -->
Year

<!-- b000392 | references | pages [22] -->
1980

<!-- b000393 | references | pages [22] -->
1981

<!-- b000394 | references | pages [22] -->
1982

<!-- b000395 | references | pages [22] -->
1983

<!-- b000396 | references | pages [22] -->
1984

<!-- b000397 | references | pages [22] -->
1985

<!-- b000398 | references | pages [22] -->
1986

<!-- b000399 | references | pages [22] -->
1987

<!-- b000400 | references | pages [22] -->
1988

<!-- b000401 | references | pages [22] -->
1989

<!-- b000402 | references | pages [22] -->
S

<!-- b000403 | references | pages [22] -->
63114

<!-- b000404 | references | pages [22] -->
60944

<!-- b000405 | references | pages [22] -->
59543

<!-- b000406 | references | pages [22] -->
58778

<!-- b000407 | references | pages [22] -->
59815

<!-- b000408 | references | pages [22] -->
60085

<!-- b000409 | references | pages [22] -->
61809

<!-- b000410 | references | pages [22] -->
63095

<!-- b000411 | references | pages [22] -->
64965

<!-- b000412 | references | pages [22] -->
66078

<!-- b000413 | references | pages [22] -->
P

<!-- b000414 | references | pages [22] -->
30.75

<!-- b000415 | references | pages [22] -->
38.85

<!-- b000416 | references | pages [22] -->
35.54

<!-- b000417 | references | pages [22] -->
31.40

<!-- b000418 | references | pages [22] -->
28.80

<!-- b000419 | references | pages [22] -->
27.49

<!-- b000420 | references | pages [22] -->
24.93

<!-- b000421 | references | pages [22] -->
16.45

<!-- b000422 | references | pages [22] -->
15.45

<!-- b000423 | references | pages [22] -->
16.04

<!-- b000424 | references | pages [22] -->
D

<!-- b000425 | references | pages [22] -->
2459

<!-- b000426 | references | pages [22] -->
2532

<!-- b000427 | references | pages [22] -->
2568

<!-- b000428 | references | pages [22] -->
2661

<!-- b000429 | references | pages [22] -->
2770

<!-- b000430 | references | pages [22] -->
2856

<!-- b000431 | references | pages [22] -->
2954

<!-- b000432 | references | pages [22] -->
3093

<!-- b000433 | references | pages [22] -->
3262

<!-- b000434 | references | pages [22] -->
3375

<!-- b000435 | references | pages [22] -->
Year

<!-- b000436 | references | pages [22] -->
1990

<!-- b000437 | references | pages [22] -->
1991

<!-- b000438 | references | pages [22] -->
1992

<!-- b000439 | references | pages [22] -->
1993

<!-- b000440 | references | pages [22] -->
1994

<!-- b000441 | references | pages [22] -->
1995

<!-- b000442 | references | pages [22] -->
1996

<!-- b000443 | references | pages [22] -->
1997

<!-- b000444 | references | pages [22] -->
1998

<!-- b000445 | references | pages [22] -->
1999

<!-- b000446 | references | pages [22] -->
S

<!-- b000447 | references | pages [22] -->
66689

<!-- b000448 | references | pages [22] -->
67296

<!-- b000449 | references | pages [22] -->
67490

<!-- b000450 | references | pages [22] -->
67610

<!-- b000451 | references | pages [22] -->
68930

<!-- b000452 | references | pages [22] -->
70133

<!-- b000453 | references | pages [22] -->
71671

<!-- b000454 | references | pages [22] -->
73427

<!-- b000455 | references | pages [22] -->
74053

<!-- b000456 | references | pages [22] -->
75727

<!-- b000457 | references | pages [22] -->
P

<!-- b000458 | references | pages [22] -->
20.51

<!-- b000459 | references | pages [22] -->
22.30

<!-- b000460 | references | pages [22] -->
16.10

<!-- b000461 | references | pages [22] -->
16.80

<!-- b000462 | references | pages [22] -->
12.93

<!-- b000463 | references | pages [22] -->
16.56

<!-- b000464 | references | pages [22] -->
17.48

<!-- b000465 | references | pages [22] -->
23.02

<!-- b000466 | references | pages [22] -->
14.33

<!-- b000467 | references | pages [22] -->
10.16

<!-- b000468 | references | pages [22] -->
D

<!-- b000469 | references | pages [22] -->
3452

<!-- b000470 | references | pages [22] -->
3497

<!-- b000471 | references | pages [22] -->
3618

<!-- b000472 | references | pages [22] -->
3698

<!-- b000473 | references | pages [22] -->
3800

<!-- b000474 | references | pages [22] -->
3869

<!-- b000475 | references | pages [22] -->
Year

<!-- b000476 | references | pages [22] -->
2000

<!-- b000477 | references | pages [22] -->
2001

<!-- b000478 | references | pages [22] -->
2002

<!-- b000479 | references | pages [22] -->
2003

<!-- b000480 | references | pages [22] -->
2004

<!-- b000481 | references | pages [22] -->
2005

<!-- b000482 | references | pages [22] -->
2006

<!-- b000483 | references | pages [22] -->
S

<!-- b000484 | references | pages [22] -->
76712

<!-- b000485 | references | pages [22] -->
77444

<!-- b000486 | references | pages [22] -->
78089

<!-- b000487 | references | pages [22] -->
79660

<!-- b000488 | references | pages [22] -->
82408

<!-- b000489 | references | pages [22] -->
84005

<!-- b000490 | references | pages [22] -->
84979

<!-- b000491 | references | pages [22] -->
P

<!-- b000492 | references | pages [22] -->
25.29

<!-- b000493 | references | pages [22] -->
24.49

<!-- b000494 | references | pages [22] -->
17.04

<!-- b000495 | references | pages [22] -->
30.30

<!-- b000496 | references | pages [22] -->
30.11

<!-- b000497 | references | pages [22] -->
37.56

<!-- b000498 | references | pages [22] -->
55.85

<!-- b000499 | references | pages [22] -->
Appendix_2

<!-- b000500 | references | pages [22] -->
According to data obtained from U.S. Federal Highway Administration, we make a list:

<!-- b000501 | references | pages [22] -->
Year

<!-- b000502 | references | pages [22] -->
1999

<!-- b000503 | references | pages [22] -->
2000

<!-- b000504 | references | pages [22] -->
2001

<!-- b000505 | references | pages [22] -->
2002

<!-- b000506 | references | pages [22] -->
2003

<!-- b000507 | references | pages [22] -->
2004

<!-- b000508 | references | pages [22] -->
2005

<!-- b000509 | references | pages [22] -->
2006

<!-- b000510 | references | pages [22] -->
2007

<!-- b000511 | references | pages [22] -->
2008

<!-- b000512 | references | pages [22] -->
2009

<!-- b000513 | references | pages [22] -->
Number

<!-- b000514 | references | pages [22] -->
of

<!-- b000515 | references | pages [22] -->
Electric

<!-- b000516 | references | pages [22] -->
Cars

<!-- b000517 | references | pages [22] -->
0

<!-- b000518 | references | pages [22] -->
0.009

<!-- b000519 | references | pages [22] -->
0.030

<!-- b000520 | references | pages [22] -->
0.065

<!-- b000521 | references | pages [22] -->
0.113

<!-- b000522 | references | pages [22] -->
0.197

<!-- b000523 | references | pages [22] -->
0.407

<!-- b000524 | references | pages [22] -->
0.660

<!-- b000525 | references | pages [22] -->
1.012

<!-- b000526 | references | pages [22] -->
1.324

<!-- b000527 | references | pages [22] -->
1.615

<!-- b000528 | references | pages [22] -->


<!-- b000529 | references | pages [22] -->
6

<!-- b000530 | references | pages [22] -->
10

<!-- b000531 | references | pages [22] -->
(

<!-- b000532 | references | pages [22] -->
)

<!-- b000533 | references | pages [22] -->
Number

<!-- b000534 | references | pages [22] -->
of

<!-- b000535 | references | pages [22] -->
Conventional

<!-- b000536 | references | pages [22] -->
2.205

<!-- b000537 | references | pages [22] -->
2.258

<!-- b000538 | references | pages [22] -->
2.353

<!-- b000539 | references | pages [22] -->
2.346

<!-- b000540 | references | pages [22] -->
2.368

<!-- b000541 | references | pages [22] -->
2.430

<!-- b000542 | references | pages [22] -->
2.474

<!-- b000543 | references | pages [22] -->
2.508

<!-- b000544 | references | pages [22] -->
2.544

<!-- b000545 | references | pages [22] -->
2.559

<!-- b000546 | references | pages [22] -->
2.460

<!-- b000547 | references | pages [22] -->


<!-- b000548 | references | pages [22] -->
8

<!-- b000549 | references | pages [22] -->
10

<!-- b000550 | references | pages [22] -->
Cars (

<!-- b000551 | references | pages [22] -->
)

<!-- b000552 | references | pages [22] -->
Tbl. 6

<!-- b000553 | references | pages [23] -->
Code

<!-- b000554 | references | pages [23] -->
f=[2*P1;1.5*P1;1.5*P1;P1;2*P2;1.5*P2;1.5*P2;P2;1.5*P3;1.5*P3;P3;2*P4;

<!-- b000555 | references | pages [23] -->
1.5*P4;1.5*P4;P4;P5;0.25*P4];

<!-- b000556 | references | pages [23] -->
neta=8;

<!-- b000557 | references | pages [23] -->
ii=15;

<!-- b000558 | references | pages [23] -->
Aeq=[1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1*neta;

<!-- b000559 | references | pages [23] -->
0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0 0;

<!-- b000560 | references | pages [23] -->
0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0;

<!-- b000561 | references | pages [23] -->
0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 1 -1;];

<!-- b000562 | references | pages [23] -->
%  A=[0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0;

<!-- b000563 | references | pages [23] -->
%     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0];

<!-- b000564 | references | pages [23] -->
A=[0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0;   %ÔÙÉúÄÜÔ´Ô¼Êø<7.7

<!-- b000565 | references | pages [23] -->
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0;   %ºËÄÜÔ¼Êø<8.3

<!-- b000566 | references | pages [23] -->
0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0;   %ÌìÈ»ÆøÔ¼Êø<23.4

<!-- b000567 | references | pages [23] -->
-1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;    %x11Ô¼Êø>25.416/2

<!-- b000568 | references | pages [23] -->
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1;    %xcÔ¼Êø<10

<!-- b000569 | references | pages [23] -->
1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0;     %Ê¯ÓÍÔ¼Êø<38

<!-- b000570 | references | pages [23] -->
0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0;    %Ãº·¢µçÔ¼Êø>15.65

<!-- b000571 | references | pages [23] -->
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0];    %ÔÙÉúÄÜÔ´·¢µçÔ¼Êø<7

<!-- b000572 | references | pages [23] -->
%B=[7.7;8.3]

<!-- b000573 | references | pages [23] -->
B=[7.7;8.3;23.4;-25.416/2;28;38;-15.65;7];

<!-- b000574 | references | pages [23] -->
Beq=[27;18.8;10.6;38.3];

<!-- b000575 | references | pages [23] -->
lb=zeros(17,1)

<!-- b000576 | references | pages [23] -->
[x,fval_netaa,exitflag,output,lamda]=linprog(f,A,B,Aeq,Beq,lb);

<!-- b000577 | references | pages [23] -->
X1=x(1)+x(2)+x(3)+x(4);

<!-- b000578 | references | pages [23] -->
X2=x(5)+x(6)+x(7)+x(8);

<!-- b000579 | references | pages [23] -->
X3=x(9)+x(10)+x(11);

<!-- b000580 | references | pages [24] -->
X4=x(12)+x(13)+x(14)+x(15);

<!-- b000581 | references | pages [24] -->
X5=x(16);

<!-- b000582 | references | pages [24] -->
Xc=x(17);

<!-- b000583 | references | pages [24] -->
XXALL_neta=[x(1),x(2),x(3),x(4),x(5),x(6),x(7),x(8),x(9),x(10),x(11),

<!-- b000584 | references | pages [24] -->
x(12),x(13),x(14),x(15),x(16),x(17)];

<!-- b000585 | references | pages [24] -->
XALL_neta=[X1,X2,X3,X4,X5,Xc];

<!-- b000586 | references | pages [24] -->
XXALL_type2_neta_con(:,ii)=XXALL_neta;

<!-- b000587 | references | pages [24] -->
XALL_type2_neta_con(:,ii)=XALL_neta;

<!-- b000588 | references | pages [24] -->
fval_type2_neta_con(ii)=fval_netaa;

<!-- b000589 | references | pages [24] -->
bar(XALL_neta)
