1  Introduction

To define the environmental and economical characteristics of electric vehicles and to judge the feasibility and practicability of electric vehicles’ widespread use, we plan to accomplish goals as follows: (1) To analyze the environmental and economical impact of the widespread use of electric vehicles, so do the influence on health and social aspects. (2) To ascertain some key factors that should be considered when determining whether and how to support the promotion. (3) To project the consumption of fossil fuels the world would save by this promotion. (4) To optimize the energy grid suiting the wide use of electric vehicles, so that the environment, society, business and individuals will get the largest number of benefits.

The approaches we use to realize such goals are: (1) We use Bass Model based on the Art Colony Optimization algorithm for prediction of sales of electric vehicles. We also predict the import of crude oil in USA. Then we make a contrast between one conventional vehicle and one electric vehicle in terms of pollutant emissions. We improve BP Artificial Neutral Network Model by combining with Grey Model and use it to predict world’s total vehicles annually in the next decade and calculate the reduction of emission. With those projections we analyze the related effects. (2) Based on the predicted vehicles number, we respectively calculate the oil consumptions base on two supposes: All vehicles are CVs; There are vehicles of CVs and EVs. To be more general, we convert the consumptions to barrels oil equivalent. (3) To optimize the current energy structure, meaning to obtain a better benefit by changing the ratio of clean sources in electricity generation, we establish a Multi-goal Programming Model. By using Analytic Hierarchy Process we simplify the model to a Mono-goal Programming Model and solve it.

2  Solutions

In contrast to internal-combustion-engine-based Conventional Vehicle (CV), electric-engine-based Electric Vehicle (EV) offers a more-efficiency and less-pollutant transportation method. Here are some contrasts with three types of EVs.

Table.1 Contrasts among Three Types of EVs[1] Type Description HEV combines both an internal combustion engine with an electric engine, with electrical Hybrid electric energy stored in batteries. HEV is more fuel efficient than regular CV as it takes advantage of vehicles (HEV) the complementary power generating characteristics of the two technologies.

PHEV is similar to HEV that it combines the use of combustion and electric motors. Plug-in hybrid However PHEV is capable of being recharged by plugging in to the electricity grid. The electric vehicles batteries in a PHEV are typically larger than those in a HEV leading to a greater all-electric (PHEV) range that is sufficient for average metropolitan use.

BEV is fully electric. Power is only by electricity stored in batteries. BEV faces similar Battery Electric limitations as HEV and PHEV due to the need for batteries while BEV’s battery vehicles (BEV) shortcomings are highlighted as there is no ICE to boost range and acceleration. In the coming parts, we model impacts of widespread use of EVs in environmental and economical aspects, with environmental influence also affects people’s health. All of those impacts play a role in social progress.

2.1  Impacts of Widespread use of EVs

Usually when considering whether to promote a new production into a widespread use, we should focus on its impacts on economical, environmental, social and health aspects. Only by estimate the benefits from the new production can we clearly understand the changes it will bring. So we analyze those impacts respectively in the four aspects. However, we find that health is related to environment, and together with economical influence they affect the society.

2.1.1  Economical Impacts

In order to investigate the market adoption on wide use of EV, we conduct a prediction about the sales of EV. The Bass Diffusion Model is right a model which well suits this situation. This model has been widely influential in marketing and management science.[2]

The Bass model is based on the following differential equation:[3] dN q      t ( p N )( m N ) ; N 0 t t t 0 dt m While considering the discrete condition, the equation should be revised as:

q      N N p m ( N ) N ( m N )     t t 1 t 1 t 1 t 1 m Nt is the number of sold production in the tth period. The following three parameters appeared in the equation above are introduced to make prediction, which respectively mean: m: market potential, also the total latent demand. p: the coefficient of innovation, meaning a probability that those who has not purchase the new production but going to use it by influence of mass media or other external factors. q: the coefficient of imitation, meaning a probability that those who has not purchase the new production but going to use it by influence of other users.

To estimate the parameters, we assume that those parameters are time invariant. We have several conventional method such as Ordinary Least Squares Method(OLS), Nonlinear Least Squares Method(NLS), Maximum Likelihood Estimation Method(MLE) and so on. But there are some restrictions, like the high dependence on enough data. So we introduce Ant Colony Optimization (ACO).

Ant Colony Optimization is an artificial intelligence optimization. How it works determines that this algorithm has less dependence on data. Although there are no abundent data, to estimate the parameters using ACO is still able to obtain satisfactorily results.

We simplify the estimation to an optimization problem:[4] Model: Nt=F[C,t], where C is the set of undetermined parameters. C={m,p,q}. Here is a data set D={(Nl,tl) | l=1,2,…,T}. There should be a set Nl=F{C,tl}. Actually based on the given data, we can only get a set Nl’ =F{C,tl}. So the problem is how to obtain a best estimation of the parameters to reach a minimum error:

C*=arg min{Σ( |Nl-Nl’| )}.

Step1. Initialization. According to the range of parameters, initialize randomly A ants and the maximum iteration times K. As to each ant, make a set Ca and initial position (N0,t0,dir). So N0=F[Ca,t0]. dir=1 means moving forward while dir=0 means moving backward. Step2. A new cycle of ant Colony movement. To each ant, it obeys the corresponding curve N=F[Ca,t] and move one step to direction dir. Then calcuate the distance d between the current position and the nearest given datum. After that, it should determine the step length and the pheromone density to release, and release pheromone in the path. With Newton Gradient Descent Method[5], we adjust Ca to Ca’ according to distance d. Step3. Pheromone Evaporation. We use the conventional evaporation strategy to evaporate the global pheromone. Step4. Go to Step2 until K times movements finish. Step5. Obtain the final result by calculate the average of all the ants’ parameters:

   C C C  * 1 2 A C A

According to the data in Figure.1, we use MATLAB to conduct the algorithm and obtain the estimations of the parameters as:

p=0.0152, q=0.1937.

Figure.1 Global EV Numbers[6]

We forecast the global Electric Vehicle Sales to the year 2020 as shown in Figure.2.

Figure.2 Predicted Global EV Sales Further, we change the parameters p and q about ±5% to test the sensitivity fo this model and get an error range as fine ‘I’ shaped strings in Figure.2 shown. From figure we believe the errors are acceptable that this model is steady.

So we can see that, until 2020, EVs are still popular worldwidely, meaning promoting EV is quite feasible and economical. Making accumulation to the base number, we predict the global number of EVs as following figure shows.

Figure.3 Predicted Global Number of EVs Based on the increasing demand of EV, other macroeconomical aspects are influenced. Due to the widely used EV, the numbers of CV are decreasing. As a result, the fuel burned by CVs is declining, which means USA are less depending on crude oil production and import. Here is statistical USA oil production and import published by Energy Information Agency shown in Table.2.

Table.2 Production and Import of Oil in USA (Unit: Thousand Barrels Daily)[7] Year 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009

7731 7733 7669 7626 7400 7228 6895 6841 6847 6734 7196 Production

10550 11092 11618 11357 12254 12898 13525 13612 13632 12872 11444 Import

Taking the wider use of EV into consideration, we make a projection by Regression Prediction about oil imports from 2010 to 2020 in USA shown in Figure.4.

Figure.4 Predicted Oils Import in USA

Also the price of crude oil will appearently cut off. Since the storage of crude oil has been shortening, the price has been rapidly rising up. Widely use of EV will save global oil as said above. As a result, also projected and reported in Annual Energy Outlook 2009 published by EIA, ratio of crude oil price to natural gas price follows the trend shown in Figure.5. That is, the price should be decreasing in the near future under the circumstance that EVs are promoted to widely use.

Figure.5 Ratio of Crude Oil Price to Natural Gas Price[8]

Furthermore, the new technique will surely promote other economical and social effects. Due to the widely use of this new production, a new industry which manufacture and maintain the batteries will rise. As a result, new jobs are created, which may increase employment of new industries and cut down employment of some other industries like gas station. What’s more, progressing the new techniques will be a new hot research field and will be invested by many enterprices. All of these attached impacts will be discussed in the next section.

2.1.2  Environmental Impacts

To significantly reduce the greenhouse gas emission is mainly by reducing the transportation emissions since the transportation uses about 30% of USA's energy while emits 20% of the greenhouse gas.[9] Electric vehicles may control the air pollution, so we analyze the impact of electric vehicles on the pollutants. Obviously EVs emit no gas while CVs emit hydrocarbons (CxHy), nitrogen oxides (NOx), carbon oxides (COx) and other pollutants when gasoline is burning.[10] From the collected data, we get the emissions of one CV as shown in Table.3.

Table.3 Emissions of One CV(Unit: g/km) [1] NOx CO PM10 CO2e 0.581 181.000 4.400 0.083

We also get the efficiency of electricity of One EV from the same source[1], being 0.2kW·h/km. We obtain data of emissions to generate per kilowatt hour’s electricity in a typical coal-combustion heat-engine plant.

Table.4 Emissions of a Typical Plant (Unit: g/kW·h) [11] NOx CO PM10 CO2e 1.257 1085.000 0.047 0.310

If we maintain the USA’s energy grid in 2009, the electricity will be generated from 5 sources as follows.

Table.5 Emissions of a Typical Plant (Unit: %) [12] Coal Natural Gas Petroleum Renewable Energy Nuclear Electric Power 48 18 1 11 22

And we also find that gas power plant produces 50% of CO2’s magnitude, 40% of CO’s magnitude and 15% of NOx’s magnitude compared with thermal power plant[13][14]. Electricity generated by petroleum is so little that we can ignore it. Renewable energy and nuclear electric power hardly emit air pollutant. Under this circumstance, we figure out the indirect emissions of EVs as shown in Table.6.

Table.6 Indirect Emissions of One EV (Unit: g/km) NOx CO PM10 CO2e 0.362 142.702 0.014 0.030 Obviously, EV is more environmentally friendly than CV since the four emissions from one EV are less than from one CV.

In order to estimate overall pollutions, we must figure out global total vehicles. We are going to use Grey Model[15], GM(1,1) to be most widely known, for prediction the emissions. We mark E(i) as the total number of worldwide vehicles in year i, as Figure.6 shows:

 [16] E i Figure.6 the Value of We mark E0 as a sequence E(i) ,       E E 1 , E 2 , , E n . 0

And E1 is the first-order accumulation of E0 , and so       E E 1 , E 2 , , E n . 1 1 1 1 k      E k E i , k 1,2, , n In the equation above, we define . 1 0  i 1

We mark Z as a sequence

1     , where            Z z 2 , z 3 , , z n z k E k E k 1 . 1 1 2

       E 2 z 2 1        E 3 z 3 1       Y B Then we denote , .          E n z n 1         After doing so, we can find that the Least Square Estimate (LSE) of parameters in equation       E k az k b GM 1,1 from obeying the following equation:

     1 T   T T ˆ a a b , B B B Y .

Thus, we can get:

    b b  1 ˆ       ak E k 1 T 1 e , k 1,2, n    a  a

We can obtain the fitting discrete value for prediction is

  1 n  ˆ( ) ˆ ˆ ˆ      E i E i ( ) , and residual mean error . E k ( ) E k ( ) E k ( 1) 1 1 n  i 1

We are now able to fit the prediction curves for each kind of emissions.

Before we do these predictions, let’s first consider the advantages and disadvantages about the GM. GM can be based on a small-size set of data, and it also succeeds in the convenience with less consideration of the data’s distribution. However, it is valid only when predicting the data obeying the exponential growth distribution. What’s worse, some data may be invalid in some random predictions, leading to the results not optimal.

Under this circumstance, we combine the Grey Model to Back Propagation Artificial Neural Network Model(BP-ANN). BP-ANN has the ability to approximate arbitrary functions, but may impact the generalization due to excessive approximation. While GM fails to approximate complex nonlinear functions, but can better predict the changing trends. Secondly, BP-ANN needs abundant hidden nodes to be well trained, which also enlarge the number of parameters and the sample data. While GM only needs a little sample data. As a whole, combining GM and BP-ANN may make prediction more accurate.

From the previous analysis, we take advantage of GM and BP-ANN to establish a forecasting model. In details, we select the Accumulated Generating Operation (AGO) and Inverse Accumulated Generating Operation(IAGO) from GM, and use BP-ANN to solve out the parameters and make the final prediction.

According to data from Figure.6, with our improved GM-BPANN model we make a projection of global numbers of highway vehicles. The result is shown in Figure.7. We define that large scale use means the occupation reaches upper 80%. And up to 2020, the ratio of EVs to total vehicles is 81.9%, so in 2020 EVs will have been in large scale use.

Figure.7 Projection of Global Vehicle Number against Global EV Number

We make a contrast of emission of CO2e in the future decade between two assumed scenarios that CVs are large-scale-used and EVs are large-scale-used (Figure.8).

Figure.8 Prediction of CO2e Emission in the Next Decade (Unit: Million Tons) And we estimate that by large scale use of EV, reduction of emitted CO2 by transportation will be 3.704 billion tons in the next decade. With the same method, we also figure out the reductions of NO2, CO and PM10. The results are 406.56 million tons, 1.194 billion tons and 67.8 million tons respectively. To explain the reductions of emissions well, we introduce shadow price. Take CO2 as an example, the shadow price is $39.97/ton[17], so in the following decade, $37 billion is saved worldwide.

As a conclusion, to generate electricity to support EVs seems to increase the emissions from power plant. However, from the analysis we see the air pollution will still be cut down significantly by large-scale use of EVs. Furthermore, this reduction is still limited. It is worth using non-polluting sources to generate electricity to drive EVs. So we optimize the energy grid in the Section 2.3.

2.1.3  Health Impacts Resulted from Environmental Changes

Health impacts are mainly related to environmental quality. It s reported that air pollution aggravates respiratory and cardiovascular diseases and leads to premature mortality. Most recent studies have identified fine particles as a prime culprit. In addition there may be significant direct health impacts of SO2.[18]

Health care cost also can be reduced by decline the emissions of pollutants. Report below (Table.7) shows the different impacts of the health impact of EV deployment when vehicles are charged using non-polluting sources of electricity[9]. Changing energy grid, which is resulted from the large scale use of EVs, benefits the health costs.

Table.7 Savings of Healthcare Costs by Different Energy Grid[9] Pollutant Value Particulate Matter $29496 Nitrous Oxide $25298 Current Grid Sulfur Dioxide -$71025 Generation Mix Volatile Organic Compounds $27468 Total $11237 Particulate Matter $92440 Nitrous Oxide $37680 Non-Carbon Power Sulfur Dioxide $51607 Generation Volatile Organic Compounds $27538 Total $209265

2.1.4  Social Effects

The social effects mainly include two aspects: social benefits and social costs. Throughout analyzing above, EVs have a lot of environmental advantages and economic benefits. What’s more, the improved environment also does good to the residents’ health. Of course rapidly developing EV industry and some attachment industries promote the employment significantly. And EV have the general equilibrium effects of changed tax revenues, which is particularly important in countries with high fuel taxes. All of these are social benefits of promoting EVs. However, this promotion need paid social costs. For example, manufacturing and maintaining EVs cost more than to CVs. Another, government need to do some public subsidies to help the EV industries. What’s more, EVs need extra infrastructure investments such as charging stations and new power plants to provide rapid charging. Figure.9 will clearly exhibit those relationships:

Figure.9 Relationship around Social impacts

Now we evaluate EVs’ social effects. We obtain Table.8 from online data that social effects are converted to prices. This is a cost-benefit estimation model with multiple inputs and multiple outputs where social benefits are outputs while social costs are inputs. We use Data Envelopment Analysis (DEA) to evaluate the comparative validity.[19]

Table.8 Costs and Benefits of Electric Vehicles[20] Benefit per 10 million EV Cost per 10 million EV

Increasing Employment $351861/year Increasing Investment $855/year

Improving Environment $277848/year Government Subsidization $3460/year

Reducing Healthcare Costs $6360000/year Increasing Taxes $6410/year DEA is mainly based on mathematical programming, evaluating the comparative validity of Decision Making Units (DMU) from the perspective of inputs and outputs. DMU terms are shown in Table.9.

Table.9 DMU Terms DMU Terms Projects Quantity Increasing Investment Inputs Government Subsidization 3 Increasing Taxes Increasing Employment Outputs Improving Environment 3 Reducing Healthcare Costs

Comparative validity means by some inputs to DMU, what the level will reach on scales and techniques and what are the outputs. The C2R model for DMU j0 is:

 min  n       X s X  j j j 0   j 1  n       Y s Y j 1,2,..., n  j j j 0   j 1        0, s 0, s 0  j 

In this model:

 means relative efficiency ranging from 0 to 1.

j means number of DMUs.

Xj means the vector of indexes of inputs of jth DMU.

Yj means the vector of indexes of outputs of jth DMU.

th DMU. Xj0 means the vector of indexes of inputs of j0 th DMU. Yj0 means the vector of indexes of outputs of j0 — and S+ are assistance variables. is the decision variable. S j

Now there are three inputs (investment increase, government’s subsidization and taxes increase) and three outputs (employment increase, environment improving, healthcare cost reduction). We use LINGO software to solve the model and figure out the comparative validity of promoting EVs is 1 while that of promoting CVs is 0.7. As a whole, though the widespread use of electric vehicles could lead to some social cost, however, in the long term, this promotion will have significant social benefits. Conclusively, positive social effects will be introduced by widespread use of EVs.

2.1.5  Battery

Improved as environment is by EVs, the cost is high however, especially for PHEV and BEV, since they use Li-ion batteries. There are also some factors should be considered about battery.

 Charging One way to cut down the cost of EVs is to plug the EV into the electricity grid. Many corporations begin to research how to charge the batteries while cars are parked in garages. At the same time batteries are storing the electricity power from the grid. However, to do extra charging too often will shorten the life period of battery sharply. Nowadays charging stations rise around, bringing benefit that these infrastructures support the EV industries and also shortcomings that battery’s life is in danger. Further, the intermittent power source such as wind and solar is quite hot-discussed. Due to their intermittence, how to store their power attracts researchers. We suppose to plug the second-hand batteries to the grid as the power reservoir and off-peak charging can also make battery able to store energy.

 Recycling Batteries with little economical value after a period of using will be removed by some automobile services. Usually the batteries are quite heavy, making it a problem to dispose them. Actually recycling Li-ion battery is not for Li, but Cu, Al, Ni, and Co. The cost to recycle is extremely high.

Along with the development of technology, Li-ion battery may not be the main source of EV. For example, Si-O2 battery is a better choice because Si and O2 is abundant from the environment and even when the battery is scrapped, there will be no pollution or dangerous substance. So developing new battery technique is a way to future.

2.1.6  Human Issues

By efforts from government and manufacturers, EV can be more easy to use. Most EVs can only travel about 100-200 miles before recharging, while gasoline vehicle can go over 300 miles before refueling. However, the capacity of battery will improve with the development of EV techniques. Thus, EV can be used for long-range transportation, not just in the situation of short range.

2.1.7  Key Factors

When considering how to promote EVs, some key factors must be considered by manufacturers and governments.

To detail the key factors that governments and vehicle manufacturers should consider when determining if and how to support the development and use of electric vehicles, we conduct Sensitivity Analysis to the C2R model in the previous subsection. So we can get the ranges of each input and output if we want to make the whole model be steady. Result is shown in Table.10.

Table.10 Results of Sensitivity Analysis Benefit Per 10 Million Cost Per 10 Million Employment Min:0 Investment Min:0 Increase Max:100000 Increase Max:224.56 Environment Min:0 Government Min:0 Improve Max:1367.23 Subsidization Max:67.23 Healthcare cost Min:0 Taxes Min:0 Reduction Max:2308.56 Increase Max:132.61

Among the three factors of social benefits, environment improve has the least range. That means, the comparative validity is most sensitive to environment improve. As a result, if we want to maintain the efficiency of investment on EV, the environmental improve must be highlighted considered. As to vehicle manufacturer, they must try best to develop cleaning techniques to reduce the pollution from batteries producing. They also need considering to reduce the indirect pollution from EVs. As to governments, they should promote the improving of power plants’ energy grid to reduce pollution when generate electricity for batteries.

Among those three factors, investment increase has the largest range. That means, governments and enterprises can expand their investing on related infrastructures to ensure the convenience of EVs’ use.

Among factors of social costs, government subsidization has the least range. That means, the comparative validity is most sensitive to government subsidization. Governments should properly subsidize the EV industries. In terms of taxes government should also be careful.

Conclusively, environment, investment and subsidization are the most vital considerations to promote EVs to widespread use.

2.2  Reduction of Fossil Fuels Using

Petroleum, natural gas and coal are all fossil fuels. Thus savings of one of those three substances means savings of fossil fuels. To calculate the reduction of oil using, we analyze its consumptions of CVs and EVs respectively. We make a contrast between the following two scenarios: All vehicles are CVs; There are vehicles of CVs and EVs as Figure.7 shown.

For the former assumption, we investigate the consumption of CV.

Table.11 Consumption of CV (Unit: 1011J per vehicle)[21] Year 1991 1992 1993 1994 1995 1996 1997 1998 1999 Consumption 1.2491 1.25127 1.2492 1.2561 1.2502 1.2516 1.2585 1.2656 1.267 Year 2000 2001 2002 2003 2004 2005 2006 2007 2008 Consumption 1.2666 1.2081 1.2354 1.2352 1.2449 1.2464 1.2486 1.2458 1.2371

We find the data are steady. Considering that oil consumption would not change much in the next 10 years, we use the average number of Table.11 as CV’s consumption. According to 2009’s energy grid[22], 97% energy consumption of transportation is from fossil fuel, while the overall fuel efficiency of CV is 14%. To be more general, we convert the energy consumption to barrel oil equivalent[23], by 1 barrel = 6.117×109 J. With the global number of vehicles, we figure out the barrel oil consumption.

Table.12 Scenario One’s Consumption (Unit: billion barrels) 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 Year Consumption 35.986 36.549 37.182 37.977 38.460 38.938 39.420 39.948 40.476 40.410

For the latter assumption, we figure out the CVs’ numbers of each year and each year’s consumption of CVs with the same method. Then we investigate EVs’ mileages traveled yearly [21].

Table.13 CV’s Mileage (Unit: km) Year 1991 1992 1993 1994 1995 1996 1997 1998 1999 Mileage 18534.3 18951.0 18997.0 19111.5 19300.0 19338.6 19795.1 19964.0 19972.5 Year 2000 2001 2002 2003 2004 2005 2006 2007 2008 Mileage 19911.6 19438.0 19963.3 20053.9 20062.2 19897.4 19819.6 19688.4 19236.5

According to the electricity consumption of each vehicle 0.2kW·h/km[1], and from  2009’s energy grid[22], 67% energy consumption of transportation is from fossil fuel, while the overall fuel efficiency of EV is 28%, we figure out the barrel oil consumption of EVs. Finally we get the consumptions of this scenario.

Table.14 Scenario Two’s Consumption (Unit: billion barrels) Year 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 Consumption 35.288 35.688 35.888 35.807 34.660 32.296 28.456 23.180 16.692 8.606 From Table.12 and Table.14, we estimate the total savings of oils of each year in the next decade shown in Table.15.

Table.15 Oils Savings Estimated (Unit: billion barrels) Year 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 Saving 0.698 0.861 1.293 2.170 3.801 6.642 10.964 16.768 23.783 31.803

The trend of savings is shown in Figure.10. Comparing with EIA data[7], with widespread use of EVs, in the year 2011 world savings of oils will be 1.1% of total. And in the year 2020 the saving ratio could be 49% if the annual consumption of oil maintains the 2009’s level. So the model we established suits the actual scenario.

Figure.10 Oils Savings in the Next Decade

2.3  Optimization of Energy Grid

To take EVs’ impacts on environment, society, business and individuals, we establish a multi-goal programming model to analyze the amount and type of electricity generation. Firstly, we adopt Analytic Hierarchy Process (AHP) to estimate the impact levels on environment, society, business and individuals. Thus we empower the four aspects and define an overall evaluation index as the objective function to conduct optimization.

Figure.11 AHP Structure We make pairwise comparisons of environment, society, business and individuals and get the comparison matrix[24]:

  1 5 7 9   1   1 6 5   5    A 1 1   1 2 7 6     1 1 1 1     9 5 2 We figure out the maximum eigenvalues and the corresponding eigenvectors and the normalized data are:

   max 4.2656, v (0.5048,0.2635,0.1245,0.1071) max

Make a consistency test:

 4.2656 4 CI       CI 0.088533, RI 0.96, CR 0.0922 0.1 3 RI

Thus matrix A passes the consistency test, meaning that this multi-goal programming model can be simplified to a mono-goal programming model.

According to Table.8, we convert the impacts on environment, society, business and individuals to prices denoted as ξ1, ξ2, ξ3 and ξ4. We also denote Psumt as the total electricity generated by electricity grid for EVs in year t. And mark α1, α2, α3 and α4 to represent the ratio of electricity generated respectively by thermal power plant, hydropower plant, nuclear power plant and wind power plant in the year t. Also we suppose R(t) is the overall benefits to the environment, society, business and individuals in the year t.

Thus，the first-order objective function is:

        max R t ( ) (0.5048 0.2635 0.1245 0.1071 ) P 1 1 2 2 3 3 4 4 sumt

The second-order objective function is: (aiming at the least energy conception of thermal power unit)

  min U t ( ) P 1 sumt Constraints are as follows: (Suppose there are abundant sources for thermal power plant and nuclear power plant):

 To thermal power plant:

n n 1      D ( b P ) P P i t , i t , max, t 1 sumt   i 1 j 1 D means the maximum load demand in the year t.  is a coefficient to meet P In this equation: max, t the maximum load demand. b is a coefficient meaning the avail of thermal power unit remained in ,i t the year t. P means the installed capacity of thermal power unit in the year t. ,i t

 To hydropower plant:

   min max Q P Q it 2 sumt it

min In this equation: is the minimum water supply to hydropower plant at its location in the year t. Q it max is the maximum water supply to hydropower plant at its location in the year t. Q it T    w dt W 0 jt jT 0 In this equation: w is the water consumption rate at a certain interval in the year t. W is the jt jT total water supply from the year t to T.

 To nuclear power plant:

n n 1      D ( c K ) K P i t , i t , max, t 3 sumt   i 1 j 1

means the maximum load demand in the year t.  is a coefficient to meet D K In this equation: max, t the maximum load demand. c is a coefficient meaning the avail of nuclear power unit remained in ,i t the year t. K means the installed capacity of nuclear power unit in the year t. ,i t

 To wind power plant:

   min max F P F it 4 sumt it

min In this equation: is the minimum wind supply to wind power plant at its location in the year t. F it max is the maximum wind supply to wind power plant at its location in the year t. F it

 Balance between electricity supply and demand:

  P n C n C sumt 1 bev 2 phev

1n is total number of BEVs. C 2n is total In this equation: is electricity consumption per BEV. bev number of PHEVs. Cphev is electricity consumption per PHEV. Then we can solve this model by following steps: Step1. Initialize t=1. Step2. According to optimization criterion, we optimize the first-order objective function by decision variable [α1, α2, α3, α4]T. If the optimal solutions do not exist, feasible solutions are acceptable. Otherwise we obtain the optimal solutions. Step3. Observe the solutions from Step2. If [α1, α2, α3, α4]T are unique, go to Step5. Otherwise go to Step4. Step4. According to optimization criterion, we optimize the second-order objective function by decision variable α1t. If the optimal solutions do not exist, feasible solutions are acceptable.

Otherwise we obtain the optimal solutions. Step5. t=t+1. Go to Step2 to calculate the amount of each type of electricity generation in the next year. Take the conditions of USA as an example. We collect data[25] from EIA’s website about USA, and figure out the amount and type of electricity generation in 2020 in Figure.12.

Figure.11 Amount and Type of Electricity Generation in 2020 in USA And in the next decade, the amounts and types of electricity generation every year are in Figure.12.

Figure.12 Amount and Type of Electricity Generation in the Next Decade in USA

3. Assessments of Models

3.1 Bass Diffusion Model

When estimate the feasibility to introduce EVs, one of factors we consider is the market adoption. We establish Bass Diffusion Model to predict the sales of EVs in the next decade. We use ACO to calculate the parameters instead of conventional methods. By ACO, the shortcoming of the basic Bass Model, high dependence on data, is overcome. By sensitivity analysis, the model has an acceptable sensitivity level.

3.2 Improved BP Artificial Neutral Network

We combine BP Artificial Neutral Network with GM. BP-ANN has the ability to approximate arbitrary functions, but may impact the generalization due to excessive approximation. While GM fails to approximate complex nonlinear functions, but can better predict the changing trends. Also, BP-ANN needs abundant hidden nodes to be well trained, which also enlarge the number of parameters and the sample data. While GM only needs a little sample data. Our improved model takes the advantages from the two models and can make prediction more accurate.

3.3 Data Envelopment Analysis

We use DEA to make assessment on EV’s social effects. It identifies the efficient and inefficient units in a sample of decision making units and provides targets for inefficient ones. The problem of sorting the frontier resident units to accomplish some goal is very important especially when a large number of units are deemed efficient.

3.4 Multi-Goal Programming Model

We establish a multi-goal programming model to optimize the electricity generation structure. We use AHP to convert the multi-goal programming model to mono-goal programming model. This makes the model solvable. However, we simplify the constraints deeply. This may result in some errors.

4. Conclusions and Suggestions

4.1 Conclusions

By large scale use of EVs, aspects about economy, environment, health and society will be affected. The impacts are mainly positive. In details, this promotion improves the environment by reducing emissions of air pollutants, so that people’s health levels up. Wide use of EVs will also have economical benefits since its marketing has bright prospects with fat profits. It will also bring increases to a series of industries’ development. By analyzing these, we are sure that widespread use of EVs can be and should be promoted.

From the calculation in Section 2.2, the introduction of EVs significantly reduces the energy consumption. Also, this introduction also leads to a progress of current structure energy grid to achieve a maximum benefit.

Government and manufacturers should take care of investing and subsidizing the EV industries to ensure the healthy development of industries related to EVs. Among all of the impacts, environment factor may be the core consideration of them.

4.2 Suggestions

 Researchers and manufacturers According to our analyzing, the costs (mainly consisting of batteries costs), infrastructures and mileage of EV will have backward effects on the promotion of EV. Due to the developing techniques, the sales cost and mileage of EV will be improved and meet the market demands without any doubts. Thus, removal of supply constraints and improving battery charging and recycling should be the main technique considerations by researchers and manufacturers.

 Governments To make this introduction more meaningful and efficient, reduce the indirect pollution from EV is the key point. Furthermore, governments should play a right role in the revolution process, avoiding improper subsidization and tax. Meanwhile, governments should take advantage of the uprising industry to improve the employment by increase jobs available in charging stations and battery services, for example.

 Cooperation Though use of EV can sharply cut down the emissions of air pollutants, a social cooperation should be established, including governments, researchers, manufacturers and other related people, to create a platform to improve the techniques of EV. The final aim is surely to supply a maximum protection to environment and make people live better.
