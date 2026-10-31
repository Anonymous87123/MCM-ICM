Summary

Because of serious global pollution problems and energy shortages, the study of the environmental and economic effects of developing electric vehicles has become increasingly important. In this paper, we focus on and provide comprehensive solutions to the following issues:  How does tax rate influence the numbers of Conventional Vehicles (CV) and Electric Vehicles (EV)?  What impacts will the replacement of CVs by EVs on oil stock?  What is the upper-limit proportion of EVs under the condition of the present power generation ability?

A Static Supply-Demand Model is set up to answer these questions. According to the influence of tax rate on supply-demand relationship, we analyze the change in the demand of CVs over tax rate. Then, we estimate how long the oil will be consumed up by PHEVs using the supply-price relationship. Finally, we provide an estimation of the upper-limit proportion of EVs under the condition of the present power generation ability.  What is the relationship between the change in the numbers of CVs and EVs?  How do factors such as government control, corporation decision influence the change in the numbers of CVs and EVs?

We successfully develop a Competing Ordinary Differential Equation Model to solve these problems. We first build up the equations using linear approximation, and then we fit the real data using least-squares principle and get an ordinary differential equation. With the help of the previous Static Supply-Demand Model, we discuss the real meanings of the fitted variables and the interaction between CVs and EVs.  How does the development of EVs influence the environment?  Whether the development of EVs can save fossil fuels?  Whether different types of EVs have the same benefits to environment, energy, or society?

To answer these questions, we build up a linear programming model and set minimum environmental cost as the destination. We find the impact of popularizing EVs on the environment. We also demonstrate the advantages and disadvantages of three types of EVs. In the end, we give recommendations for the government on its role to support and guide the development of EVs.

An Analysis of the Future Development of

Electric Vehicles

Introduction:

Our models and key factors are shown as follows:

Fig. 1

In accessing the impacts brought from a new commodity, it often involves many connected or unconnected aspects. Electric vehicles (EVs) are considered to be one of the most promising means to alleviate current shortage and unbalance distribution in power demand. However, on the other hand, the widespread use of EVs is constrained or promoted by the economical, social and technical factors. In our model, we analyzed these factors in a system dependently, we also made a comprehensive evaluation of their influence on EVs.

To consider the economical factors, we set up a Static Supply-Demand Model (SSDM) in which relations between oil supply, mileage demand and oil price are introduced. A balance point is calculated in this model and tax rate is regarded as an adjustment factor to it. In the PHEVs-dominant market, a new predicted oil-exhausting year is given due to the decreasing consumption of oil. More information of the consumption by resources types and purpose is offered in LPM. Further, we also give a simple static estimate for the up-bound of the percentage of PHEVs. A more comprehensive dynamic estimate of it is followed in CM.

Thinking over the social and technical factors, a Competing Ordinary Differential Equation Model (CM) is set up. Different types of EVs (BEVs/HEVs/PHEVs) result into different coefficients in ODEs. According to the variations of coefficients, we get different dynamic amount-trend of EVs and CVs. The environmental impaction of different types of EVs is introduced in LPM by different constrains.

With regard to the factors of environment and resources, we set up a Linear Programming Model (LPM) for Optimum Energy Distribution. The optimum energy flows of different type resources are given with Energy Flow by Source and Sector Diagram. The result is also affected by the type of EVs according to different combined energy efficient.

Static Supply-Demand Model

Notations

S :Daily oil supply amount in Thousand Barrels per day(TB)

D :Yearly vehicle travel demand in Billion Km(BK)

P :Oil price in Dollars per Barrel ($/bbI)

Smax :Maximum daily oil supply amount

Dmin :Minimum yearly vehicle travel demand

Smin :Daily oil supply amount except for transportation

C :Oil consumption per 100 kilometers in Liter/Hundred Kilometers(L/HK)

μ1 :Proportion of oil consumption for transportation

μ2 : Efficiency of converting petroleum to gasoline

V : Volume of one barrel of oil in liter (L)

R : Tax rate

Assumptions

1． In a buyer’s market (i.e. in such a market, supply is greater than demand), the relationship between market price and consumption reflects the relationship between price and demand.

2． In a seller’s market (i.e. in such a market, demand is greater than supply), the relationship between market price and consumption reflects the relationship between price and production.

3． Supply-demand relationship is the main factor in determining price, without regard to other factors such as political or economic state.

4． The consumption amount of oil will not have direct influence over power generation amount or electricity price.

5． The relationships above are independent of time, that is, they will not change over time.

The Foundation of Model

dS S   k 1( ) 1 d P S max dD D   k 1( ) 2 d P D min   D k ( S S ) 3 min

1k 2k Where , are undetermined coefficients. They demonstrate the relationship between  1 V  k3 S,D and P. stands for the travel distance provided by the energy in one 2 C    S S 1( ) barrel of oil. . min total 1

The solutions of the differential equation are:

   k P / S S S C 1 e 1 max max    k P D / D D C 2 e 2 max max   D k ( S S ) 3 min

The Solution of the Model

1. The determination of variables

C Conventional oil-fuel car: =10(L/HK)

  Hybrid electric car:       C =5(L/HK), V = 159L = 20% = 72% , , 2 1

3  k 0.0458 In conclusion, for conventional oil-fuel cars, (BK/TB), while for hybrid 3  k 0.0916 electric cars, (BK/TB).

 min S 84000 S 23520 (TB) (Data in 2009), (TB). total

2. The fitting of equation

When looking at the trend of oil price and oil consumption, we can find that between 1980 and 1994, the oil price went up as production declined, while between 1999 and 2006, the oil price increased as production went up. Therefore, we can take the market as buyer’s market between 1980 and 1994, as seller’s market between 1999 and 2006, and as supply-demand balance market between 1995 and 1998. We use data [Scott M. Festin 1996] between 1980 and 1994 to fit demand-price equation, and use data between 1999 and 2006 to fit supply-price equation. The results are as following:

max  min  1  S 90300 D 636.27 k 2339 (TB) (BK)

2  C  C  k 13 . 23 1 20859 2 -3988

3. The equilibrium points

Returning the values of the variables back to the equations, we can find the equilibrium points of completely employing conventional oil-fuel car or completely employing hybrid electric car:

Type of Vehicle P($/bbI) S(TB) D(BK)

PHEV(Plug-in Hybrid 17.33 76983.19 3417.51 Electric Vehicle)

CV(Conventional Vehicle) 55.27 85315.55 1899.53

Tbl. 1

According the data of 2006, our result of CV’s equilibrium point is closed to the realistic value. So this model is reliable basing on above analysis.

4000

3500

3000

2500 D 3 1 2000

1500

1000

2 20 40 2 60 4 80 6 100 8 120 140 10 4 P x 10 S Fig. 2

Line 1 and line 2 stand for the relationship between oil price and demand from consumer’s perspective. Line 3 stands for the relationship between oil price and supply amount from supplier’s perspective. Their intersections are equilibrium points. The point denoted by a circle is the equilibrium point of PHEV. The point denoted by a block is the equilibrium point of CV. We can see that if CVs were totally replaced by PHEVs, both the price and demand of oil would decline, while the travel distance would extend under equilibrium.

4. PHEV and Tax

1) The PHEVs’ impaction on the oil tax

A main reason that the government levies high tax on oil is to keep the supply and demand of oil in balance. If we used the PHEVs to replace most of the CVs, the pressure on oil demand would be remarkably relieved. Suppose that the tax rate on oil (R) is in proportion to the oil price (P). By collecting correlating data,We obtain:

R    R P 13 . 27 HEV HEV P R    R P 42 . 38 CV CV P  R S     HEV HEV 100 % 28 . 25 % The tax rate ratio:  R S CV CV

The calculations above are based on the static supply-demand model, so we did not take into account the impact of tax rate on S-P curve, or the change of D-P curve over time. The result shows that after the employment of PHEVs, under the dual effects of the declination of oil consumption and oil tax rate, the total amount of tax on oil will decrease notably.

2)The oil tax’s impaction on the PHEVs

In the oil market, the variation of oil tax rate will result in change of the S-P relation. One part of the increasing tax is included in the increasing price of oil, the other part is P balanced with the decreasing profits. We define the as the percentage of increasing oil rise  D % price. The sensitivity analysis of is followed. cv

22% 16% 12% 8% P rise

-14% -12% -8.5% -5.3%  D % cv

Tbl. 2

D To balance the demand of travel miles, the decreasing will lead to the rising cv

demand of PHEVs. As a result, enhancing the oil tax rate will promote the widespread use of PHEVs.

5. Impact on oil stock

In the above, we only considered the impact of supply-demand relationship on price. From the results we have obtained, we know that using PHEVs fails to remarkably decrease the consumption of oil (76983.19 VS 85315.55), but we can also see that after using PHEVs, the same amount of oil consumption could meet larger demand. Therefore, in order to balance the oil consumption, we define the consuming efficiency of oil as the travel distance demand satisfied when consuming one unit of oil:

      4 D / 356 S .1 25 10 （ ） HEV SEV HEV  ）

D S

/ 365 （       5 D / 356 S .6 26 10 （ ） CV CV CV

 6 S = 1,143.355 10 TB From data we know: (2007) reserve

     5 D ( total ) S .1 42 10 SEV reserve HEV More travel distance it can still supply:      4 D ( total ) S .7 16 10 CV reserve CV 5 x 10 7

6 Accumulative D from 1980 5

4

3 D(HEV)

D(CV) 2

1

0 1980 1990 2000 2010 2020 2030 2040 2050 2060 2070 year

Fig. 3

From the figure above we can see that according to the present trend of demand, completely using CVs will consume up present oil stock in 2020, while completely using CVs will consume up present oil stock in 2029.

6. Computation of Electricity Margin

Reasonably, the increasing widespread use of electricity vehicles will lead to the rising of electricity consumption. However, the realistic amount of EVs has a up bound due to the limitation of total electricity installed capacity.

We defineas the rate of electricity generation (i.e., the ratio of total electricity production to total installed capacity times working hours):

total electricit y production   i denotes the type of electricit y generation ，   working hours installed capacity i i i We made the assumption that the power plants except for thermal ones work under full load, which means they work 24 hours per day (hpd). The-year curve is the upper one in Fig. 4 when there is no additional production of thermal electricity, the middle one when thermal power plants work 16 hpd, the lower one when thermal power plants work 20 hpd. Fig. 4 shows the rise of electricity demand.

0.9

0.85 Percentage of Electricity Capacity no additional thermal electricity 20hpd full load 16hpd full load 0.8

0.75

0.7

0.65

0.6

0.55

0.5 1980 1985 1990 1995 2000 2005 2010 year

Fig. 4

To access the capacity of producing additional electricity, we define as the electricity  1   margin:

Thermal electricity No additional 16phd full load 20phd full load

averagefrom 2002 to 2006 12% 28% 42%

Tbl. 3

Fig. 5

Source: Lawrence Berkeley National Laboratory

http://www.mpoweruk.com/electricity_demand.htm

relatively small so that a part of their charging would be in on-peak hours(daytime, especially at noon). The electricity margin of BEVs is small because the electricity generation in on-peak hours is nearly under full load. We set it to be the  under 16 phd; (2)As to the PHEVs, because of their longer endurance mileage, most of their charging world be in off-peak hours when the utilization of electricity is much lower than it in on-peak hours. In this sense, their electricity margin is larger. We set it to be the  under 20 phd. These two margins will be used in LPM

Without additional thermal electricity generation, we calculated the ratio of PHEVs to total vehicles and the ratio of CVs to total vehicles at the Critical point (upper bound) of 3k electricity margin. The result is 38.5% and 61.5% respectively. The coefficient is 0.0634 accordingly.

Type of Vehicle P($/bbI) S(TB) D(BK)

38.5%PHEV and 61.5%CV 36 82000 2520

Tbl. 4

The result shows that present thermal power generation amount will limit the number of electric cars. If we want to further popularize electric cars, we need to generate more electricity, which will lead to more new energy demand or more pollution. To comprehensively access the impact of using more fossil fuels to generate electricity on environment, we need analyze how to choose and arrange the types of power generation so that the pollution will be the least. We will give an analysis in LPM. As shown above, here we give a static upper bound of the PHEVs’ percentage. To have a dynamic result of the amount of CVs and different type EVs, we set up following Competition Model.

Competing Ordinary Differential Equation Model

Notations

1x : The total number of electric cars

2x : The total number of all kinds of cars (conventional cars)

ia :The influential parameter

ib : The influential parameter

W :Covering rate of infrastructure

S :Endurance mileage

E :Maximum power generation ability max

Basic Assumptions

1. Electric cars mainly refer to hybrid electric cars.

1a , 2a , 1b , 2b are constants, because they are determined by the specifications 2. of the cars themselves instead of exterior factors.

0a , 0b will change according to exterior factors. 3.

The Foundation of Ordinary Differential Equation Model

We build the model below to analyze the relationship of quantity change between conventional and electric cars. The model is based on a two-element ordinary differential equation:

 dx    1 a a x a x  0 1 1 2 2 dt  dx     2 b b x b x 0 1 1 2 2  dt

dx1 is the change rate of the total of electric cars dx2 is the change rate 1x where dt , dt 2x of the total of conventional cars . Because we do not know the exact relations dx1 , 1x x2 between and , here we follow the engineers’ advice: Using linear relation where dt you don’t know the exact relation.

2a 1a 2b 1b 0a In this equation group, the meanings of unknown parameters , , , , , 0b are :

Correlated coefficient of change rate of the total number of electric cars, 2a which is determined by factors such as competition between two types of cars, etc.

Coefficient of change rate of the total number of electric cars, which is 1a determined by factors such as the saturation of electric car market, etc.

Change rate of the total number of electric cars, which is determined by other 0a factors such as the fluctuation of electricity price, etc.

Coefficient of change rate of the total number of conventional cars, which is 2b determined by factors such as the saturation of conventional car market, etc.

Correlated coefficient of change rate of the total number of conventional cars, 1b which is determined by factors such as competition between two types of cars, the impact of the popularization of electric cars on conventional cars, etc.

Change rate of the total number of conventional cars, which is determined by 0b other factors such as the fluctuation of fuel price, etc.

Tbl. 5

The steady solution of the ODE above is:

  a b a b  2 0 0 2 x   1  a b a b 1 2 2 1   a b a b   0 1 1 0 x  2   a b a b  1 2 2 1

The Solution of the Previous Model

According to the data in Appendix_2,and from the theory of ordinary differential equation, we can deduce the solutions of the equations have the forms below:

    t x m m L 1 0 1     t x n n L  2 0 1

By using least squares fitting, we obtain

      6 6 t x .1 272 10 .1 673 10 .0 8294 1       8 7 t x .2 592 10 .3 921 10 .0 8294  2

1      7 a .1 741 a .0 0822 a .1 910 10 Thus, , , , 2 0    103   9 2 b .4 915 b .1 10 b .1 347 10 , , . 2 0 1

Validation of a1,b1, a2,b2

1  1  a 0 b 0 , shows that the use of electric cars will promote the use of both conventional cars and electric cars. According to the static supply-demand balance model, the use of electric cars can lower the oil price, which leads to the decline of the using cost of both electric cars and conventional cars. The decline of fuel fee further motivates the demand in the car market.

2  2  a 0 b 0 , demonstrates that the use of conventional oil-fuel cars will restrict the demand in the car market. The reason is also based on the static supply-demand balance model: the use of conventional oil-fuel cars will raise the oil price, which is negative for the demand.

We can draw a figure to show the result:

8 2.6 x 10

2.55 fitting curve real data 2.5

Number of Ordinary Cars 2.45

2.4

2.35

2.3

2.25

2.2

2.15 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 Years

Fig. 6

8 x 10 3

2.5

Estimated Number of Electric Cars Estimated Number of Ordinary Cars 2 Real Data of Electric Cars Number of Cars Real Data of Ordinary Cars

1.5

1

0.5

0 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 Year

Fig. 7

The first figure gives a proof of the soundness of the model and the fitting variables. The second figure shows that the amount of conventional cars and electric cars will increase to a fixed value, not infinity. This is in accord with the fact.

Discussions about Parameters a0,b0

a and 0b are constants which are criteria for the competitive ability of cars 0 determined by factors such as technology level, infrastructures, and policies, etc. Because 0b technologies and infrastructures of conventional cars have been determined firmly, will not change a lot.

a As for , we can suppose it has the form as below: 0

a  k WSE 0 max

W k Where is an undetermined coefficient. is named as the covering rate of the W  0 1 S infrastructures of electric cars ( ). is the endurance mileage, which is determined E by battery and charging technology. is the maximum power generation ability. It will max exert restriction or motivation on electric cars.

Sensitivity analysis of a0 on electric cars :

7 x 10 3 a0'=a0 a0'=1.1*a0 a0'=1.2*a0 2.5 a0'=1.3*a0 a0'=1.4*a0 2 a0'=1.5*a0

x1 1.5

1

0.5

0 0 10 20 30 40 50 60 70 80 90 100 t

Fig. 8

a As shown in figure*, larger represents more competitiveness of EVs or more 0

a coverage of infrastructures, that is to say, includes the information about EVs’ type. 0

Competitiveness of EVs mainly includes the technique and the pollution. The more

a friendliness to environment, the more support from government will be given, so will be 0

larger. To access the environment impact of different type EVs, a model to optimize energy distribution is followed.

Linear Programming Model for Optimum Energy

Distribution

Notations

ijx : Energy transferred from Supply Source i to Demand Sector j

: Energy transferred from Electric Power sector to Transportation sector after cx the popularization of electric cars

B : Energy Demand Sector j j

i iA : Energy Supply Sources

:Environmental cost (pollution produced) when converting energy from ijP Supply Source i to Demand Sector j  : Efficiency of converting heat to electricity 1

: Energy efficiency of electric cars compared to traditional cars, i.e., the ratio  of energy consumed by traditional cars to electric cars under the same 2

 : Combined energy efficiency of electric cars, which is  1  2

O : Fuel consumption per 100 kilometers of traditional cars 100

E : Energy produced by electric cars under the consumption of one unit of oil

E :Electricity consumption per 100 kilometers of traditional cars 100

:Environmental cost of the total amount of pollution caused by energy P ALL consumption

Assumptions

1. We only model under ideal situation, that is, the whole energy system is working under the condition which meets the optimal solution of linear programming.

2. The environmental cost can fully reflect the pollution caused by using different types of energy.

3. Most EVs are HEVs (Hybrid Electric Vehicles), but there are also BEVs (Battery Electric Vehicles) and PHEVs (Plug-in Electric Vehicles).

The Foundation of A Linear Programming Model for Optimum Energy

Distribution

x 11

Fig. 9

The distribution of the energy network is shown as in Fig. 9.Considering that the demands must still be satisfied after the redistribution of energy flow, we can have the following constraints:

       . . S t x x x x B 11 21 41 1 2 c 1     x x x x B 12 22 32 42 2     x x x x B 13 23 33 43 3      x x x x x B 14 24 44 54 c 4  0 x ij

 is efficiency of converting heat to electricity. Based on data from where 1 is [http://en.wikipedia.org/wiki/Cogeneration], 1   3.0 when energy is generated by Electricti ty only plants    1    8.0 when energy is generated by combined heat and power ( CHP ) plants   O E   100 , it stands for energy efficiency of electric cars compared to traditional cars. 2 E 100     To obtain the combined efficiency, let , 1 2

The environmental cost of the total amount of pollution caused by energy consumption is

5 4    P x P ALL ij ij   i 1 j 1

P As our goal is to minimize the environmental cost , we propose the following LP ALL formulation for the single destination problem.

5 4   min x P ij ij   i 1 j 1         S .. t x x x x B 11 21 41 1 2 c 1     x x x x B 12 22 32 42 2     x x x x B 13 23 33 43 3      x x x x x B 14 24 44 54 c 4  x 0 ij

The Solution of The Linear Programming Model for Optimum Energy

Distribution

1. The Solution of the Basic Model

In economy, Environmental Cost is commonly used as a criterion to measure the extent of pollution. According to [Shuying Ding 2006] and taking reality into account, we list different conditions in the table below:

Mathematical No. Constraint Explanation Expression

Constraint on the total Existing installed capacity of solar, wind 4  4  x 7.7 1 amount of energy of and water power determines the j Renewable Energy maximum amount of energy supplied by  j 1 Constraint on the total 54  x 2 amount of energy of Nuclear Electric Power

Constraint on the total 4  2  x 3 amount of energy of j Natural Gas  j 1

Constraint on the total 4  1  x 4 amount of energy of j Petroleum  j 1

cx Constraint on (energy transferred from Electric  Power sector to cx 5 Transportation sector after the popularization of electric cars)

x Constraint on (energy 11 transferred from Petroleum 11  12 x 6 source to Transportation sector)

x Constraint on (energy 11 transferred from Coal 34  x 15 7 source to Electric Power sector)

x Constraint on (energy 11 transferred from Renewable 44  x 8 Energy source to Electric Power sector) Renewable Energy.

Existing installed capacity of nuclear 3.8 power determines the maximum amount of energy supplied by nuclear power.

Existing natural gas drilling amount 23 4. determines the maximum amount of natural gas supply.

Obtained from the infinite value of the 38 fitted S-P curve in the supply-demand model.

Estimated from the energy transferred 10 from transportation to electric power.

Based on Assumption 3; and suppose that . 708 half of the energy consumed by HEVs are provided by gasoline.

Calculated by real power generation . 65 efficiency and installed capacity of coal.

Calculated by real power generation 7 efficiency and installed capacity of Renewable Energy.

Tbl. 6

Adding these constraints to previous model, we get the following figure:

120 Original Condition No Restriction Restriction No.3+No.4 100 Restriction No.3+No.4(loosed by 2 times) Restriction No.3+No.4+No.5 Restriction No.1~No.10 Energy(Quadrillion Btu) 80

60

40

20

0 Petroleum Natural Gas Coal Renewable Energy Nuclear Electric Power Different Kinds of Supply Sources

Fig. 10 We can see, if there were no constraints, the optimal distribution of energy would be to use Renewable Energy as supply source completely, and the second best choice would be Nuclear Electric Power. Under real conditions, it is impossible to completely use Renewable Energy and Nuclear Electric Power as energy supply sources. Considering constraints No.3 and No. 4 (listed in Tbl. 6), we can find that the result of the LP formation shows it is more reasonable to use Natural Gas.

However, because of limited usable quantity, it is still impossible to use Natural Gas as first-choice energy supply source. Thus, we have to add constraint No.5 to improve our model. Considering other concrete factors, such as the structure of energy industry, the upper limit of energy, etc., we finally propose the linear programming model with constraints No.1-No.10.

Based on the discussions and analysis above, we can ensure the order of priority of energy supply sources as below: Renewable Energy>Nuclear Electric Power>Natural ijP Gas>Petroleum>Coal, which accords with the data of the environmental cost .

P Now we show the total amount of environmental cost of energy consumption under ALL six different combinations of constraints (listed in the legend of the figure above) in a new figure:

60

50

40

PALL 30

20

10

0 No Restriction Restriction No.3+No.4 Restriction No.3+No.4(loosed by 2 times) Restriction No.3+No.4+No.5 Restriction No.1-No.10 Different Kinds of Restrictions

Fig. 11

We can roughly observe that the looser the constraints, the lower the environmental P cost , correspondingly the better the environment. ALL

2. Sensitivity Analysis for Ordinary Condition

Subsequently, by using the ultimate model with constraints No.1-No.8 and changing the value of , we create the figure below to demonstrate energy distribution and energy transferred from Electric Power sector to Transportation sector after the popularization of X electric cars( ). c 40 =0.5 Critical Point:=0.85 =0.6 35 =0.7 =0.8 =0.9 30 =1.0 Energy(Quadrillion Btu) =1.1 25 =1.2 =1.3 =1.4 20 =1.5 =2 Critical Point:=0.85 15 =3 =4 10

5

0 Petroleum Natural Gas Coal Renewable Energy Nuclear Electric Power  Energy Transmission(Xc) Different Kinds of Supply Sources and ...

Fig. 12

    .0 85 .0 85 From the figure above we can find a Critical Point: . That is, when ,   X .0 85 the demand of coal is a constant, and keeps being zero. But when , the c X demand of coal begins to decrease, while becomes a non-zero constant and starts to c  is larger than 1.4. decrease after

 values in a curve: P Now we show the environmental cost under different ALL

60

58

Critical Point: 56 =0.85

PALL 54

52

50

48 0.5 1 1.5 2 2.5 3 3.5 4 

Fig. 13

  .0 85 We can see that is still a Critical Point. Besides, it is easy to find that when   .0 85 P , the environmental cost is decreasing, which means the environment is ALL dPALL is going down, which shows the improving. However, we can also notice that  d effect of improving environment by lifting  is declining.

3. Sensitivity Analysis for BEV, HEV, and PHEV

The electric vehicles in the market can be categorized into three major types: BEV, HEV, and PHEV. Because their power generation mechanisms are different, the optimal environmental costs of them are different under same energy condition. Besides, the proportion of fossil fuels they consume will be different. Thus, based on previous results of linear programming and new constraints derived from the characteristics of different cars, we can give a new solution of the problem. Consider the conditions when the electric vehicles in the market are all BEVs, HEVs or PHEVs separately, and list the constraints under each condition as following:

Type Constraint Explanation

The source of energy for transportation will not be restricted 11  x 0 by oil now. BEV  cx 15 Calculated from electricity margin.

1 Suppose more than half of the amount of energy for   x 25 . 416 transportation is provide by oil. 11 2 PHEV  cx 28 Calculated from electricity margin.

Converted and estimated from the fuel consumption of 100 11  10 x kilometers of Toyota Prius and conventional cars. HEV  cx 0 HEVs cannot get power from electricity grid directly.

Tbl.7

Solving the three linear programming problems above, we can first get a curve which shows the change of the total environmental cost over the combined energy efficiency of electric cars :

60 Original Pollution BEV's Pullution PHEV's Pullution 55 HEV's Pullution

50

PALL 45

40

35

30 0 1 2 3 4 5 6 7 8 

Fig. 14

By analyzing this figure we can find:

 BEV is always better than PHEV in the respect of environment protection.

When the value of  is small, the environmental cost of HEV is lower than that  of BEV or PHEV. But as  increases, HEV is growing worse than BEV or PHEV.

To make BEV and PHEV perform better in environment protection,  must be  higher than its value at critical point, while HEV always perform better than current environment situation.

Then, we illustrate the energy distribution of the three EV types in separate pie charts   3 when (it means the EV technologies have developed fully):

13% 14%

< 1% < 1%

43%

25% 27% 59%

3% 16%

BEV PHEV

15%

< 1%

45%

29%

10%

HEV

Fig. 15

From the figures above we can obviously observe that the type of electric vehicles has a great impact on the distribution of electricity.

4. Model validation

From above analysis, when the  is small, we should popularize HEV to minimize the environmental cost. When  is large enough so that the environment cost of PHEV and BEV is lower than the one of HEV, we should popularize them.

Before Toyota Prius released PHEV in 2007, the HEV dominated the EVs’ market, which is in accord with situation of small. After its release, we can observe a decline of sales of HEV from the reference’s data. This validates the crossover point of P- curve in figure * between HEV and PHEV/BEV.

Conclusion

Strengths

 Our models are simple but comprehensive, covering five aspects;

 Our models have strong robustness due to their independence with types of EV;

 Our models validate and complement each other;

 Each model is aimed at a special perspective and offers practical recommendations.

Weakness

 Much of the coefficients in our models are simplified or estimated in statistic;

 Some solution plays a guiding role but is not practical or realizable in real world.

Recommendation

For the Governments

1) Governments should increase the oil tax rate to limit the demand of CVs and popularize EVs due to the analysis in SSDM;

2) More electricity production and installed capacity is needed to promote the widespread use of EVs, the additional amount is determined by the EV type;

3) More charging infrastructures are necessary;

cx 4) Based on the linear programming model considering (energy transferred from

Electric Power sector to Transportation sector), the order of priority of five energy supply sources is: Renewable Energy>Nuclear Electric Power>Natural Gas>Petroleum>Coal

Therefore, the government should first take into consideration the development of supply sources such as Renewable Energy or Nuclear Electric Power so that they could help electric cars produce benefits to environment. As for the benefits of developing different types of energy, we can refer to Fig. 10 and Fig. 11.

5) Strategies for developing which type of the electric cars: If our technology developing ability is powerful enough, i.e.,  is high enough, we should develop BEV in priority to gain the most benefits to environment. If our technology developing ability is limited, we should develop HEV in priority, whose benefits to environment have nothing to do with .

6) Can we save fossil fuels by widely using electric vehicles? According to the results

  .0 85 we have obtained, under the premise that , coals can be saved. Because under the

optimal condition, the demands of petroleum and natural gas will exceed their supply amount. Unfortunately, under no conditions could petroleum or natural gas be saved.

For the vehicle manufacturers 1) Manufactures should increase the endurance mileage by improve the technique of battery, so that more EVs don’t need charge in on-peak hours.

  .0 85 2) In the sensitivity analysis section in LPM, we find a critical point , and

  .0 85 through analysis we know that only when electric cars can demonstrate their

energy economic advantage. So the value of  should be as large as possible.

  O E   100 3.0 when energy is generated by Electricti ty only plants  E    1    100   O E 2      100 8.0 when energy is generated by combined heat and power ( CHP ) plants  E  100

It is impractical to increase the fuel consumption of traditional cars in order to protect environment. So what we can really do are:

E  Minimizing , that is, minimizing the energy consumption of electric cars by 100

technical innovations.

 Use combined-heat-and-power (CHP) plants to generate power as much as possible.
