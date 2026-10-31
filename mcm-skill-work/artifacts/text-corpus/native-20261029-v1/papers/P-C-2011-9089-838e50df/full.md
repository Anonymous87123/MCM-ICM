# P-C-2011-9089-838e50df

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team # 9089                                                                                      Page 1 of 20

<!-- b000002 | prose | pages [1] -->
What will Electric Vehicle Bring to the World?

<!-- b000003 | heading | pages [1] -->
1  Introduction

<!-- b000004 | prose | pages [1] -->
To define the environmental and economical characteristics of electric vehicles and to judge the feasibility and practicability of electric vehicles’ widespread use, we plan to accomplish goals as follows: (1) To analyze the environmental and economical impact of the widespread use of electric vehicles, so do the influence on health and social aspects. (2) To ascertain some key factors that should be considered when determining whether and how to support the promotion. (3) To project the consumption of fossil fuels the world would save by this promotion. (4) To optimize the energy grid suiting the wide use of electric vehicles, so that the environment, society, business and individuals will get the largest number of benefits.

<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | prose | pages [1] -->
The approaches we use to realize such goals are: (1) We use Bass Model based on the Art Colony Optimization algorithm for prediction of sales of electric vehicles. We also predict the import of crude oil in USA. Then we make a contrast between one conventional vehicle and one electric vehicle in terms of pollutant emissions. We improve BP Artificial Neutral Network Model by combining with Grey Model and use it to predict world’s total vehicles annually in the next decade and calculate the reduction of emission. With those projections we analyze the related effects. (2) Based on the predicted vehicles number, we respectively calculate the oil consumptions base on two supposes: All vehicles are CVs; There are vehicles of CVs and EVs. To be more general, we convert the consumptions to barrels oil equivalent. (3) To optimize the current energy structure, meaning to obtain a better benefit by changing the ratio of clean sources in electricity generation, we establish a Multi-goal Programming Model. By using Analytic Hierarchy Process we simplify the model to a Mono-goal Programming Model and solve it.

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | heading | pages [1] -->
2  Solutions

<!-- b000009 | prose | pages [1] -->
In contrast to internal-combustion-engine-based Conventional Vehicle (CV), electric-engine-based Electric Vehicle (EV) offers a more-efficiency and less-pollutant transportation method. Here are some contrasts with three types of EVs.

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | prose | pages [1] -->
Table.1 Contrasts among Three Types of EVs[1] Type Description

<!-- b000012 | prose | pages [1] -->
HEV combines both an internal combustion engine with an electric engine, with electrical

<!-- b000013 | prose | pages [1] -->
Hybrid electric

<!-- b000014 | prose | pages [1] -->
energy stored in batteries. HEV is more fuel efficient than regular CV as it takes advantage of

<!-- b000015 | prose | pages [1] -->
vehicles (HEV)

<!-- b000016 | prose | pages [1] -->
the complementary power generating characteristics of the two technologies.

<!-- b000017 | prose | pages [1] -->
PHEV is similar to HEV that it combines the use of combustion and electric motors.

<!-- b000018 | prose | pages [1] -->
Plug-in hybrid

<!-- b000019 | prose | pages [1] -->
However PHEV is capable of being recharged by plugging in to the electricity grid. The

<!-- b000020 | prose | pages [1] -->
electric vehicles

<!-- b000021 | prose | pages [1] -->
batteries in a PHEV are typically larger than those in a HEV leading to a greater all-electric

<!-- b000022 | prose | pages [1] -->
(PHEV)

<!-- b000023 | prose | pages [1] -->
range that is sufficient for average metropolitan use.

<!-- b000024 | furniture | pages [2] -->
Team # 9089                                                                                      Page 2 of 20

<!-- b000025 | prose | pages [2] -->
BEV is fully electric. Power is only by electricity stored in batteries. BEV faces similar

<!-- b000026 | prose | pages [2] -->
Battery Electric

<!-- b000027 | prose | pages [2] -->
limitations as HEV and PHEV due to the need for batteries while BEV’s battery

<!-- b000028 | prose | pages [2] -->
vehicles (BEV)

<!-- b000029 | prose | pages [2] -->
shortcomings are highlighted as there is no ICE to boost range and acceleration. In the coming parts, we model impacts of widespread use of EVs in environmental and economical aspects, with environmental influence also affects people’s health. All of those impacts play a role in social progress.

<!-- b000030 | furniture | pages [2] -->


<!-- b000031 | heading | pages [2] -->
2.1  Impacts of Widespread use of EVs

<!-- b000032 | prose | pages [2] -->
Usually when considering whether to promote a new production into a widespread use, we should focus on its impacts on economical, environmental, social and health aspects. Only by estimate the benefits from the new production can we clearly understand the changes it will bring. So we analyze those impacts respectively in the four aspects. However, we find that health is related to environment, and together with economical influence they affect the society.

<!-- b000033 | furniture | pages [2] -->


<!-- b000034 | heading | pages [2] -->
2.1.1  Economical Impacts

<!-- b000035 | prose | pages [2] -->
In order to investigate the market adoption on wide use of EV, we conduct a prediction about the sales of EV. The Bass Diffusion Model is right a model which well suits this situation. This model has been widely influential in marketing and management science.[2]

<!-- b000036 | furniture | pages [2] -->


<!-- b000037 | prose | pages [2] -->
The Bass model is based on the following differential equation:[3]

<!-- b000038 | prose | pages [2] -->
dN q  

<!-- b000039 | prose | pages [2] -->
t (

<!-- b000040 | prose | pages [2] -->
p N

<!-- b000041 | prose | pages [2] -->
)(

<!-- b000042 | prose | pages [2] -->
t dt m   

<!-- b000043 | furniture | pages [2] -->


<!-- b000044 | prose | pages [2] -->
m m N

<!-- b000045 | prose | pages [2] -->
) ;

<!-- b000046 | prose | pages [2] -->
N

<!-- b000047 | prose | pages [2] -->
0

<!-- b000048 | furniture | pages [2] -->


<!-- b000049 | prose | pages [2] -->
t t

<!-- b000050 | prose | pages [2] -->
0

<!-- b000051 | prose | pages [2] -->
While considering the discrete condition, the equation should be revised as:

<!-- b000052 | prose | pages [2] -->
   N N p m ( N  t t 1 q  

<!-- b000053 | furniture | pages [2] -->


<!-- b000054 | prose | pages [2] -->
) N ( m N )     t t 1 1 t 1 t 1 m

<!-- b000055 | prose | pages [2] -->
Nt is the number of sold production in the tth period. The following three parameters appeared in the equation above are introduced to make prediction, which respectively mean: m: market potential, also the total latent demand.

<!-- b000056 | furniture | pages [2] -->


<!-- b000057 | prose | pages [2] -->
p: the coefficient of innovation, meaning a probability that those who has not purchase the new production but going to use it by influence of mass media or other external factors. q: the coefficient of imitation, meaning a probability that those who has not purchase the new production but going to use it by influence of other users.

<!-- b000058 | furniture | pages [2] -->


<!-- b000059 | prose | pages [2] -->
To estimate the parameters, we assume that those parameters are time invariant. We have several conventional method such as Ordinary Least Squares Method(OLS), Nonlinear Least Squares Method(NLS), Maximum Likelihood Estimation Method(MLE) and so on. But there are some restrictions, like the high dependence on enough data. So we introduce Ant Colony Optimization (ACO).

<!-- b000060 | furniture | pages [2] -->


<!-- b000061 | prose | pages [2] -->
Ant Colony Optimization is an artificial intelligence optimization. How it works determines that this algorithm has less dependence on data. Although there are no abundent data, to estimate the parameters using ACO is still able to obtain satisfactorily results.

<!-- b000062 | furniture | pages [2] -->


<!-- b000063 | prose | pages [2] -->
We simplify the estimation to an optimization problem:[4]

<!-- b000064 | furniture | pages [3] -->
Team # 9089                                                                                      Page 3 of 20

<!-- b000065 | prose | pages [3] -->
Model: Nt=F[C,t], where C is the set of undetermined parameters. C={m,p,q}. Here is a data set D={(Nl,tl) | l=1,2,…,T}. There should be a set Nl=F{C,tl}. Actually based on the given data, we can only get a set Nl’ =F{C,tl}. So the problem is how to obtain a best estimation of the parameters to reach a minimum error:

<!-- b000066 | prose | pages [3] -->
C*=arg min{Σ( |Nl-Nl’| )}.

<!-- b000067 | furniture | pages [3] -->


<!-- b000068 | furniture | pages [3] -->


<!-- b000069 | prose | pages [3] -->
Step1. Initialization. According to the range of parameters, initialize randomly A ants and the maximum iteration times K. As to each ant, make a set Ca and initial position (N0,t0,dir). So N0=F[Ca,t0]. dir=1 means moving forward while dir=0 means moving backward. Step2. A new cycle of ant Colony movement. To each ant, it obeys the corresponding curve N=F[Ca,t] and move one step to direction dir. Then calcuate the distance d between the current position and the nearest given datum. After that, it should determine the step length and the pheromone density to release, and release pheromone in the path. With Newton Gradient Descent Method[5], we adjust Ca to Ca’ according to distance d. Step3. Pheromone Evaporation. We use the conventional evaporation strategy to evaporate the global pheromone. Step4. Go to Step2 until K times movements finish. Step5. Obtain the final result by calculate the average of all the ants’ parameters:

<!-- b000070 | prose | pages [3] -->
 C  * 1 C

<!-- b000071 | furniture | pages [3] -->


<!-- b000072 | prose | pages [3] -->
  C C C

<!-- b000073 | furniture | pages [3] -->


<!-- b000074 | prose | pages [3] -->
2 2 A A

<!-- b000075 | prose | pages [3] -->
According to the data in Figure.1, we use MATLAB to conduct the algorithm and obtain the estimations of the parameters as:

<!-- b000076 | prose | pages [3] -->
p=0.0152, q=0.1937.

<!-- b000077 | furniture | pages [3] -->


<!-- b000078 | prose | pages [3] -->
Figure.1 Global EV Numbers[6]

<!-- b000079 | furniture | pages [3] -->


<!-- b000080 | prose | pages [3] -->
We forecast the global Electric Vehicle Sales to the year 2020 as shown in Figure.2.

<!-- b000081 | furniture | pages [4] -->
Team # 9089                                                                                      Page 4 of 20

<!-- b000082 | furniture | pages [4] -->


<!-- b000083 | prose | pages [4] -->
Figure.2 Predicted Global EV Sales

<!-- b000084 | prose | pages [4] -->
Further, we change the parameters p and q about ±5% to test the sensitivity fo this model and get an error range as fine ‘I’ shaped strings in Figure.2 shown. From figure we believe the errors are acceptable that this model is steady.

<!-- b000085 | furniture | pages [4] -->


<!-- b000086 | prose | pages [4] -->
So we can see that, until 2020, EVs are still popular worldwidely, meaning promoting EV is quite feasible and economical. Making accumulation to the base number, we predict the global number of EVs as following figure shows.

<!-- b000087 | furniture | pages [4] -->


<!-- b000088 | prose | pages [4] -->
Figure.3 Predicted Global Number of EVs

<!-- b000089 | prose | pages [4] -->
Based on the increasing demand of EV, other macroeconomical aspects are influenced. Due to the widely used EV, the numbers of CV are decreasing. As a result, the fuel burned by CVs is declining, which means USA are less depending on crude oil production and import. Here is statistical USA oil production and import published by Energy Information Agency shown in Table.2.

<!-- b000090 | prose | pages [4] -->
Table.2 Production and Import of Oil in USA (Unit: Thousand Barrels Daily)[7]

<!-- b000091 | prose | pages [4] -->
2003 Year 1999 2000 2001 2002 2004 2005 2006 2007 2008 2009

<!-- b000092 | prose | pages [4] -->
7400 7731 7733 7669 7626 Production 7228 6895 6841 6847 6734 7196

<!-- b000093 | prose | pages [4] -->
12254 10550 11092 11618 11357 Import 12898 13525 13612 13632 12872 11444

<!-- b000094 | furniture | pages [4] -->


<!-- b000095 | furniture | pages [4] -->


<!-- b000096 | prose | pages [4] -->
Taking the wider use of EV into consideration, we make a projection by Regression Prediction about oil imports from 2010 to 2020 in USA shown in Figure.4.

<!-- b000097 | furniture | pages [5] -->
Team # 9089                                                                                      Page 5 of 20

<!-- b000098 | furniture | pages [5] -->


<!-- b000099 | prose | pages [5] -->
Figure.4 Predicted Oils Import in USA

<!-- b000100 | furniture | pages [5] -->


<!-- b000101 | prose | pages [5] -->
Also the price of crude oil will appearently cut off. Since the storage of crude oil has been shortening, the price has been rapidly rising up. Widely use of EV will save global oil as said above. As a result, also projected and reported in Annual Energy Outlook 2009 published by EIA, ratio of crude oil price to natural gas price follows the trend shown in Figure.5. That is, the price should be decreasing in the near future under the circumstance that EVs are promoted to widely use.

<!-- b000102 | furniture | pages [5] -->


<!-- b000103 | prose | pages [5] -->
Figure.5 Ratio of Crude Oil Price to Natural Gas Price[8]

<!-- b000104 | furniture | pages [5] -->


<!-- b000105 | prose | pages [5] -->
Furthermore, the new technique will surely promote other economical and social effects. Due to the widely use of this new production, a new industry which manufacture and maintain the batteries will rise. As a result, new jobs are created, which may increase employment of new industries and cut down employment of some other industries like gas station. What’s more, progressing the new techniques will be a new hot research field and will be invested by many enterprices. All of these attached impacts will be discussed in the next section.

<!-- b000106 | furniture | pages [5] -->


<!-- b000107 | heading | pages [5] -->
2.1.2  Environmental Impacts

<!-- b000108 | prose | pages [5] -->
To significantly reduce the greenhouse gas emission is mainly by reducing the transportation emissions since the transportation uses about 30% of USA's energy while emits 20% of the greenhouse gas.[9] Electric vehicles may control the air pollution, so we analyze the impact of electric vehicles on the pollutants. Obviously EVs emit no gas while CVs emit hydrocarbons (CxHy), nitrogen oxides (NOx), carbon oxides (COx) and other pollutants when gasoline is burning.[10] From the collected data, we get the emissions of one CV as shown in Table.3.

<!-- b000109 | furniture | pages [6] -->
Team # 9089                                                                                      Page 6 of 20

<!-- b000110 | prose | pages [6] -->
Table.3 Emissions of One CV(Unit: g/km) [1]

<!-- b000111 | prose | pages [6] -->
NOx CO2e

<!-- b000112 | prose | pages [6] -->
0.581 181.000

<!-- b000113 | furniture | pages [6] -->


<!-- b000114 | prose | pages [6] -->
CO PM10

<!-- b000115 | prose | pages [6] -->
4.400 0.083

<!-- b000116 | prose | pages [6] -->
We also get the efficiency of electricity of One EV from the same source[1], being 0.2kW·h/km. We obtain data of emissions to generate per kilowatt hour’s electricity in a typical coal-combustion heat-engine plant.

<!-- b000117 | prose | pages [6] -->
Table.4 Emissions of a Typical Plant (Unit: g/kW·h) [11]

<!-- b000118 | prose | pages [6] -->
NOx CO2e

<!-- b000119 | prose | pages [6] -->
1.257 1085.000

<!-- b000120 | furniture | pages [6] -->


<!-- b000121 | prose | pages [6] -->
CO PM10

<!-- b000122 | prose | pages [6] -->
0.047 0.310

<!-- b000123 | prose | pages [6] -->
If we maintain the USA’s energy grid in 2009, the electricity will be generated from 5 sources as follows.

<!-- b000124 | prose | pages [6] -->
Table.5 Emissions of a Typical Plant (Unit: %) [12]

<!-- b000125 | prose | pages [6] -->
Petroleum Coal Natural Gas

<!-- b000126 | prose | pages [6] -->
48 18 1

<!-- b000127 | furniture | pages [6] -->


<!-- b000128 | prose | pages [6] -->
Renewable Energy Nuclear Electric Power

<!-- b000129 | prose | pages [6] -->
11 22

<!-- b000130 | prose | pages [6] -->
And we also find that gas power plant produces 50% of CO2’s magnitude, 40% of CO’s magnitude and 15% of NOx’s magnitude compared with thermal power plant[13][14]. Electricity generated by petroleum is so little that we can ignore it. Renewable energy and nuclear electric power hardly emit air pollutant. Under this circumstance, we figure out the indirect emissions of EVs as shown in Table.6.

<!-- b000131 | prose | pages [6] -->
Table.6 Indirect Emissions of One EV (Unit: g/km)

<!-- b000132 | prose | pages [6] -->
NOx CO2e

<!-- b000133 | prose | pages [6] -->
0.362 142.702

<!-- b000134 | prose | pages [6] -->
CO PM10

<!-- b000135 | prose | pages [6] -->
0.014 0.030 Obviously, EV is more environmentally friendly than CV since the four emissions from one EV are less than from one CV.

<!-- b000136 | furniture | pages [6] -->


<!-- b000137 | prose | pages [6] -->
In order to estimate overall pollutions, we must figure out global total vehicles. We are going to use Grey Model[15], GM(1,1) to be most widely known, for prediction the emissions. We mark E(i) as the total number of worldwide vehicles in year i, as Figure.6 shows:

<!-- b000138 | furniture | pages [6] -->


<!-- b000139 | prose | pages [6] -->
 [16] E i Figure.6 the Value of

<!-- b000140 | furniture | pages [7] -->
Team # 9089                                                                                      Page 7 of 20

<!-- b000141 | prose | pages [7] -->
We mark E0 as a sequence E(i) ,

<!-- b000142 | prose | pages [7] -->
   E E 1 , E 0    2 , , E n .

<!-- b000143 | prose | pages [7] -->
And E1 is the first-order accumulation of E0 , and so

<!-- b000144 | prose | pages [7] -->
   E E 1 , E 1 1

<!-- b000145 | prose | pages [7] -->
k

<!-- b000146 | prose | pages [7] -->


<!-- b000147 | prose | pages [7] -->
 

<!-- b000148 | prose | pages [7] -->


<!-- b000149 | prose | pages [7] -->
E k E

<!-- b000150 | prose | pages [7] -->
In the equation above, we define 1 0

<!-- b000151 | prose | pages [7] -->


<!-- b000152 | prose | pages [7] -->
i

<!-- b000153 | prose | pages [7] -->
1

<!-- b000154 | prose | pages [7] -->
We mark Z as a sequence

<!-- b000155 | prose | pages [7] -->
 

<!-- b000156 | prose | pages [7] -->
   2 , , E n . 1 1 1

<!-- b000157 | prose | pages [7] -->


<!-- b000158 | prose | pages [7] -->
i i

<!-- b000159 | prose | pages [7] -->
, ,

<!-- b000160 | prose | pages [7] -->
k

<!-- b000161 | prose | pages [7] -->
1,2, ,

<!-- b000162 | prose | pages [7] -->
n

<!-- b000163 | prose | pages [7] -->
.

<!-- b000164 | prose | pages [7] -->
1   , where      Z z 2 , z 3 , , z n

<!-- b000165 | prose | pages [7] -->


<!-- b000166 | prose | pages [7] -->


<!-- b000167 | prose | pages [7] -->


<!-- b000168 | prose | pages [7] -->
 

<!-- b000169 | prose | pages [7] -->
 

<!-- b000170 | prose | pages [7] -->
E

<!-- b000171 | prose | pages [7] -->
2

<!-- b000172 | prose | pages [7] -->
z

<!-- b000173 | prose | pages [7] -->
2 1

<!-- b000174 | prose | pages [7] -->
 

<!-- b000175 | prose | pages [7] -->
 

<!-- b000176 | prose | pages [7] -->


<!-- b000177 | prose | pages [7] -->


<!-- b000178 | prose | pages [7] -->


<!-- b000179 | prose | pages [7] -->
E

<!-- b000180 | prose | pages [7] -->
3

<!-- b000181 | prose | pages [7] -->
z

<!-- b000182 | prose | pages [7] -->
3 1

<!-- b000183 | prose | pages [7] -->
 

<!-- b000184 | prose | pages [7] -->
 

<!-- b000185 | prose | pages [7] -->


<!-- b000186 | prose | pages [7] -->


<!-- b000187 | prose | pages [7] -->
Y

<!-- b000188 | prose | pages [7] -->
B

<!-- b000189 | prose | pages [7] -->
Then we denote

<!-- b000190 | prose | pages [7] -->
,

<!-- b000191 | prose | pages [7] -->
.

<!-- b000192 | prose | pages [7] -->


<!-- b000193 | prose | pages [7] -->


<!-- b000194 | prose | pages [7] -->
 

<!-- b000195 | prose | pages [7] -->
 

<!-- b000196 | prose | pages [7] -->


<!-- b000197 | prose | pages [7] -->


<!-- b000198 | prose | pages [7] -->


<!-- b000199 | prose | pages [7] -->
E n

<!-- b000200 | prose | pages [7] -->
z n

<!-- b000201 | prose | pages [7] -->
1

<!-- b000202 | prose | pages [7] -->
 

<!-- b000203 | prose | pages [7] -->
 

<!-- b000204 | prose | pages [7] -->
 

<!-- b000205 | prose | pages [7] -->
 

<!-- b000206 | prose | pages [7] -->
      z k E k E k 1 . 1 1 2

<!-- b000207 | prose | pages [7] -->
After doing so, we can find that the Least Square Estimate (LSE) of parameters in equation

<!-- b000208 | prose | pages [7] -->
      E k az k b GM 1,1 obeying the following equation: from

<!-- b000209 | prose | pages [7] -->
 

<!-- b000210 | prose | pages [7] -->
T  

<!-- b000211 | prose | pages [7] -->
ˆ

<!-- b000212 | prose | pages [7] -->
a a b

<!-- b000213 | prose | pages [7] -->
,

<!-- b000214 | prose | pages [7] -->
Thus, we can get:

<!-- b000215 | prose | pages [7] -->
 

<!-- b000216 | prose | pages [7] -->


<!-- b000217 | prose | pages [7] -->
b  1 ˆ

<!-- b000218 | prose | pages [7] -->
  

<!-- b000219 | prose | pages [7] -->
E k 1 T 1

<!-- b000220 | prose | pages [7] -->


<!-- b000221 | prose | pages [7] -->
a

<!-- b000222 | prose | pages [7] -->


<!-- b000223 | prose | pages [7] -->
  

<!-- b000224 | prose | pages [7] -->


<!-- b000225 | prose | pages [7] -->
1

<!-- b000226 | prose | pages [7] -->
T T B B B Y .

<!-- b000227 | prose | pages [7] -->
 

<!-- b000228 | prose | pages [7] -->
b

<!-- b000229 | prose | pages [7] -->
  

<!-- b000230 | prose | pages [7] -->
ak e , k 1,2, n

<!-- b000231 | furniture | pages [7] -->


<!-- b000232 | prose | pages [7] -->
 

<!-- b000233 | prose | pages [7] -->
a

<!-- b000234 | prose | pages [7] -->
 

<!-- b000235 | prose | pages [7] -->
We can obtain the fitting discrete value for prediction is

<!-- b000236 | prose | pages [7] -->
ˆ ˆ ˆ    , and residual mean error E k ( ) E k ( ) E k ( 1) 1 1  

<!-- b000237 | prose | pages [7] -->
1

<!-- b000238 | prose | pages [7] -->
n

<!-- b000239 | prose | pages [7] -->


<!-- b000240 | prose | pages [7] -->
ˆ( )

<!-- b000241 | prose | pages [7] -->
   E i E i

<!-- b000242 | prose | pages [7] -->
( )

<!-- b000243 | prose | pages [7] -->
. n 

<!-- b000244 | prose | pages [7] -->
i

<!-- b000245 | prose | pages [7] -->
1

<!-- b000246 | prose | pages [7] -->
We are now able to fit the prediction curves for each kind of emissions.

<!-- b000247 | furniture | pages [7] -->


<!-- b000248 | prose | pages [7] -->
Before we do these predictions, let’s first consider the advantages and disadvantages about the GM. GM can be based on a small-size set of data, and it also succeeds in the convenience with less consideration of the data’s distribution. However, it is valid only when predicting the data obeying the exponential growth distribution. What’s worse, some data may be invalid in some random predictions, leading to the results not optimal.

<!-- b000249 | furniture | pages [7] -->


<!-- b000250 | prose | pages [7] -->
Under this circumstance, we combine the Grey Model to Back Propagation Artificial Neural Network Model(BP-ANN). BP-ANN has the ability to approximate arbitrary functions, but may impact the generalization due to excessive approximation. While GM fails to approximate complex nonlinear functions, but can better predict the changing trends. Secondly, BP-ANN needs abundant hidden nodes to be well trained, which also enlarge the number of parameters and the sample data. While GM only needs a little sample data. As a whole, combining GM and BP-ANN may make

<!-- b000251 | furniture | pages [8] -->
Team # 9089                                                                                      Page 8 of 20

<!-- b000252 | prose | pages [8] -->
prediction more accurate.

<!-- b000253 | furniture | pages [8] -->


<!-- b000254 | prose | pages [8] -->
From the previous analysis, we take advantage of GM and BP-ANN to establish a forecasting model. In details, we select the Accumulated Generating Operation (AGO) and Inverse Accumulated Generating Operation(IAGO) from GM, and use BP-ANN to solve out the parameters and make the final prediction.

<!-- b000255 | furniture | pages [8] -->


<!-- b000256 | prose | pages [8] -->
According to data from Figure.6, with our improved GM-BPANN model we make a projection of global numbers of highway vehicles. The result is shown in Figure.7. We define that large scale use means the occupation reaches upper 80%. And up to 2020, the ratio of EVs to total vehicles is 81.9%, so in 2020 EVs will have been in large scale use.

<!-- b000257 | furniture | pages [8] -->


<!-- b000258 | prose | pages [8] -->
Figure.7 Projection of Global Vehicle Number against Global EV Number

<!-- b000259 | furniture | pages [8] -->


<!-- b000260 | prose | pages [8] -->
We make a contrast of emission of CO2e in the future decade between two assumed scenarios that CVs are large-scale-used and EVs are large-scale-used (Figure.8).

<!-- b000261 | furniture | pages [8] -->


<!-- b000262 | prose | pages [8] -->
Figure.8 Prediction of CO2e Emission in the Next Decade (Unit: Million Tons) And we estimate that by large scale use of EV, reduction of emitted CO2 by transportation will be 3.704 billion tons in the next decade. With the same method, we also figure out the reductions of NO2, CO and PM10. The results are 406.56 million tons, 1.194 billion tons and 67.8 million tons respectively. To explain the reductions of emissions well, we introduce shadow price. Take CO2 as

<!-- b000263 | furniture | pages [9] -->
Team # 9089                                                                                      Page 9 of 20

<!-- b000264 | prose | pages [9] -->
an example, the shadow price is $39.97/ton[17], so in the following decade, $37 billion is saved worldwide.

<!-- b000265 | furniture | pages [9] -->


<!-- b000266 | prose | pages [9] -->
As a conclusion, to generate electricity to support EVs seems to increase the emissions from power plant. However, from the analysis we see the air pollution will still be cut down significantly by large-scale use of EVs. Furthermore, this reduction is still limited. It is worth using non-polluting sources to generate electricity to drive EVs. So we optimize the energy grid in the Section 2.3.

<!-- b000267 | furniture | pages [9] -->


<!-- b000268 | heading | pages [9] -->
2.1.3  Health Impacts Resulted from Environmental Changes

<!-- b000269 | prose | pages [9] -->
Health impacts are mainly related to environmental quality. It s reported that air pollution aggravates respiratory and cardiovascular diseases and leads to premature mortality. Most recent studies have identified fine particles as a prime culprit. In addition there may be significant direct health impacts of SO2.[18]

<!-- b000270 | furniture | pages [9] -->


<!-- b000271 | prose | pages [9] -->
Health care cost also can be reduced by decline the emissions of pollutants. Report below (Table.7) shows the different impacts of the health impact of EV deployment when vehicles are charged using non-polluting sources of electricity[9]. Changing energy grid, which is resulted from the large scale use of EVs, benefits the health costs.

<!-- b000272 | furniture | pages [9] -->


<!-- b000273 | prose | pages [9] -->
Table.7 Savings of Healthcare Costs by Different Energy Grid[9]

<!-- b000274 | prose | pages [9] -->
Pollutant Value

<!-- b000275 | prose | pages [9] -->
Particulate Matter $29496 Nitrous Oxide

<!-- b000276 | prose | pages [9] -->
Current Grid

<!-- b000277 | prose | pages [9] -->
$25298 Sulfur Dioxide

<!-- b000278 | prose | pages [9] -->
Generation Mix

<!-- b000279 | prose | pages [9] -->
-$71025 Volatile Organic Compounds $27468

<!-- b000280 | prose | pages [9] -->
Total $11237

<!-- b000281 | prose | pages [9] -->
Particulate Matter $92440 Nitrous Oxide

<!-- b000282 | prose | pages [9] -->
Non-Carbon Power

<!-- b000283 | prose | pages [9] -->
$37680 Sulfur Dioxide

<!-- b000284 | prose | pages [9] -->
Generation

<!-- b000285 | prose | pages [9] -->
$51607 Volatile Organic Compounds $27538

<!-- b000286 | furniture | pages [9] -->


<!-- b000287 | heading | pages [9] -->
2.1.4  Social Effects

<!-- b000288 | prose | pages [9] -->
Total $209265

<!-- b000289 | prose | pages [9] -->
The social effects mainly include two aspects: social benefits and social costs. Throughout analyzing above, EVs have a lot of environmental advantages and economic benefits. What’s more, the improved environment also does good to the residents’ health. Of course rapidly developing EV industry and some attachment industries promote the employment significantly. And EV have the general equilibrium effects of changed tax revenues, which is particularly important in countries with high fuel taxes. All of these are social benefits of promoting EVs. However, this promotion need paid social costs. For example, manufacturing and maintaining EVs cost more than to CVs. Another, government need to do some public subsidies to help the EV industries. What’s more, EVs need extra infrastructure investments such as charging stations and new power plants to provide rapid charging. Figure.9 will clearly exhibit those relationships:

<!-- b000290 | furniture | pages [10] -->
Team # 9089                                                                                      Page 10 of 20

<!-- b000291 | furniture | pages [10] -->


<!-- b000292 | prose | pages [10] -->
Figure.9 Relationship around Social impacts

<!-- b000293 | furniture | pages [10] -->


<!-- b000294 | furniture | pages [10] -->


<!-- b000295 | prose | pages [10] -->
Now we evaluate EVs’ social effects. We obtain Table.8 from online data that social effects are converted to prices. This is a cost-benefit estimation model with multiple inputs and multiple outputs where social benefits are outputs while social costs are inputs. We use Data Envelopment Analysis (DEA) to evaluate the comparative validity.[19]

<!-- b000296 | furniture | pages [10] -->


<!-- b000297 | prose | pages [10] -->
Table.8 Costs and Benefits of Electric Vehicles[20]

<!-- b000298 | prose | pages [10] -->
Benefit per 10 million EV

<!-- b000299 | prose | pages [10] -->
Increasing Employment $351861/year

<!-- b000300 | prose | pages [10] -->
Improving Environment $277848/year

<!-- b000301 | prose | pages [10] -->
Reducing Healthcare Costs $6360000/year

<!-- b000302 | prose | pages [10] -->
Cost per 10 million EV

<!-- b000303 | prose | pages [10] -->
Increasing Investment $855/year

<!-- b000304 | prose | pages [10] -->
Government Subsidization $3460/year

<!-- b000305 | prose | pages [10] -->
Increasing Taxes $6410/year

<!-- b000306 | prose | pages [10] -->
DEA is mainly based on mathematical programming, evaluating the comparative validity of Decision Making Units (DMU) from the perspective of inputs and outputs. DMU terms are shown in Table.9.

<!-- b000307 | furniture | pages [10] -->


<!-- b000308 | prose | pages [10] -->
Table.9 DMU Terms Projects DMU Terms Quantity

<!-- b000309 | prose | pages [10] -->
Increasing Investment

<!-- b000310 | prose | pages [10] -->
Government Subsidization

<!-- b000311 | prose | pages [10] -->
Inputs

<!-- b000312 | prose | pages [10] -->
3

<!-- b000313 | prose | pages [10] -->
Increasing Taxes

<!-- b000314 | prose | pages [10] -->
Increasing Employment

<!-- b000315 | prose | pages [10] -->
Improving Environment

<!-- b000316 | prose | pages [10] -->
Outputs

<!-- b000317 | prose | pages [10] -->
3 Reducing Healthcare Costs

<!-- b000318 | furniture | pages [10] -->


<!-- b000319 | prose | pages [10] -->
Comparative validity means by some inputs to DMU, what the level will reach on scales and techniques and what are the outputs. The C2R model for DMU j0 is:

<!-- b000320 | furniture | pages [11] -->
Team # 9089                                                                                      Page 11 of 20

<!-- b000321 | prose | pages [11] -->


<!-- b000322 | prose | pages [11] -->
min

<!-- b000323 | prose | pages [11] -->


<!-- b000324 | prose | pages [11] -->
n

<!-- b000325 | prose | pages [11] -->


<!-- b000326 | prose | pages [11] -->


<!-- b000327 | prose | pages [11] -->


<!-- b000328 | prose | pages [11] -->
 

<!-- b000329 | prose | pages [11] -->


<!-- b000330 | prose | pages [11] -->
X s

<!-- b000331 | prose | pages [11] -->


<!-- b000332 | prose | pages [11] -->
j j

<!-- b000333 | prose | pages [11] -->


<!-- b000334 | prose | pages [11] -->


<!-- b000335 | prose | pages [11] -->
j

<!-- b000336 | prose | pages [11] -->
1

<!-- b000337 | prose | pages [11] -->


<!-- b000338 | prose | pages [11] -->
n

<!-- b000339 | prose | pages [11] -->


<!-- b000340 | prose | pages [11] -->


<!-- b000341 | prose | pages [11] -->


<!-- b000342 | prose | pages [11] -->
 

<!-- b000343 | prose | pages [11] -->
Y s Y

<!-- b000344 | prose | pages [11] -->


<!-- b000345 | prose | pages [11] -->
j j

<!-- b000346 | prose | pages [11] -->


<!-- b000347 | prose | pages [11] -->


<!-- b000348 | prose | pages [11] -->
j

<!-- b000349 | prose | pages [11] -->
1

<!-- b000350 | prose | pages [11] -->


<!-- b000351 | prose | pages [11] -->
 

<!-- b000352 | prose | pages [11] -->


<!-- b000353 | prose | pages [11] -->
 

<!-- b000354 | prose | pages [11] -->
0,

<!-- b000355 | prose | pages [11] -->
s

<!-- b000356 | prose | pages [11] -->
0,

<!-- b000357 | prose | pages [11] -->
s

<!-- b000358 | prose | pages [11] -->


<!-- b000359 | prose | pages [11] -->
j

<!-- b000360 | prose | pages [11] -->


<!-- b000361 | prose | pages [11] -->
In this model:

<!-- b000362 | prose | pages [11] -->
X

<!-- b000363 | prose | pages [11] -->
j

<!-- b000364 | prose | pages [11] -->
0

<!-- b000365 | furniture | pages [11] -->


<!-- b000366 | prose | pages [11] -->


<!-- b000367 | prose | pages [11] -->
j

<!-- b000368 | prose | pages [11] -->
1,2,...,

<!-- b000369 | prose | pages [11] -->
n

<!-- b000370 | prose | pages [11] -->
j j

<!-- b000371 | prose | pages [11] -->
0 0

<!-- b000372 | prose | pages [11] -->
 

<!-- b000373 | prose | pages [11] -->
0

<!-- b000374 | prose | pages [11] -->
 means relative efficiency ranging from 0 to 1. j means number of DMUs. Xj means the vector of indexes of inputs of jth DMU. Yj means the vector of indexes of outputs of jth DMU. Xj0 means the vector of indexes of inputs of j0

<!-- b000375 | prose | pages [11] -->
Yj0 means the vector of indexes of outputs of j0 th DMU.

<!-- b000376 | prose | pages [11] -->
th DMU.

<!-- b000377 | prose | pages [11] -->
— and S+ are assistance variables.

<!-- b000378 | prose | pages [11] -->
is the decision variable. S j

<!-- b000379 | prose | pages [11] -->
Now there are three inputs (investment increase, government’s subsidization and taxes increase) and three outputs (employment increase, environment improving, healthcare cost reduction). We use LINGO software to solve the model and figure out the comparative validity of promoting EVs is 1 while that of promoting CVs is 0.7. As a whole, though the widespread use of electric vehicles could lead to some social cost, however, in the long term, this promotion will have significant social benefits. Conclusively, positive social effects will be introduced by widespread use of EVs.

<!-- b000380 | furniture | pages [11] -->


<!-- b000381 | heading | pages [11] -->
2.1.5  Battery

<!-- b000382 | prose | pages [11] -->
Improved as environment is by EVs, the cost is high however, especially for PHEV and BEV, since they use Li-ion batteries. There are also some factors should be considered about battery.

<!-- b000383 | furniture | pages [11] -->


<!-- b000384 | prose | pages [11] -->
 Charging One way to cut down the cost of EVs is to plug the EV into the electricity grid. Many corporations begin to research how to charge the batteries while cars are parked in garages. At the same time batteries are storing the electricity power from the grid. However, to do extra charging too often will shorten the life period of battery sharply. Nowadays charging stations rise around, bringing benefit that these infrastructures support the EV industries and also shortcomings that battery’s life is in danger. Further, the intermittent power source such as wind and solar is quite hot-discussed. Due to their intermittence, how to store their power attracts researchers. We suppose to plug the second-hand batteries to the grid as the power reservoir and off-peak charging can also make battery able to store energy.

<!-- b000385 | furniture | pages [11] -->


<!-- b000386 | prose | pages [11] -->
 Recycling Batteries with little economical value after a period of using will be removed by some automobile services. Usually the batteries are quite heavy, making it a problem to dispose them. Actually recycling Li-ion battery is not for Li, but Cu, Al, Ni, and Co. The cost to recycle is extremely high.

<!-- b000387 | furniture | pages [12] -->
Team # 9089                                                                                      Page 12 of 20

<!-- b000388 | prose | pages [12] -->
Along with the development of technology, Li-ion battery may not be the main source of EV. For example, Si-O2 battery is a better choice because Si and O2 is abundant from the environment and even when the battery is scrapped, there will be no pollution or dangerous substance. So developing new battery technique is a way to future.

<!-- b000389 | furniture | pages [12] -->


<!-- b000390 | heading | pages [12] -->
2.1.6  Human Issues

<!-- b000391 | prose | pages [12] -->
By efforts from government and manufacturers, EV can be more easy to use. Most EVs can only travel about 100-200 miles before recharging, while gasoline vehicle can go over 300 miles before refueling. However, the capacity of battery will improve with the development of EV techniques. Thus, EV can be used for long-range transportation, not just in the situation of short range.

<!-- b000392 | furniture | pages [12] -->


<!-- b000393 | heading | pages [12] -->
2.1.7  Key Factors

<!-- b000394 | prose | pages [12] -->
When considering how to promote EVs, some key factors must be considered by manufacturers and governments.

<!-- b000395 | furniture | pages [12] -->


<!-- b000396 | prose | pages [12] -->
To detail the key factors that governments and vehicle manufacturers should consider when determining if and how to support the development and use of electric vehicles, we conduct Sensitivity Analysis to the C2R model in the previous subsection. So we can get the ranges of each input and output if we want to make the whole model be steady. Result is shown in Table.10.

<!-- b000397 | furniture | pages [12] -->


<!-- b000398 | heading | pages [12] -->
Table.10 Results of Sensitivity Analysis

<!-- b000399 | prose | pages [12] -->
Benefit Per 10 Million Employment

<!-- b000400 | prose | pages [12] -->
Min:0

<!-- b000401 | prose | pages [12] -->
Increase

<!-- b000402 | prose | pages [12] -->
Max:100000

<!-- b000403 | prose | pages [12] -->
Environment

<!-- b000404 | prose | pages [12] -->
Min:0

<!-- b000405 | prose | pages [12] -->
Improve

<!-- b000406 | prose | pages [12] -->
Max:1367.23

<!-- b000407 | prose | pages [12] -->
Healthcare cost

<!-- b000408 | prose | pages [12] -->
Min:0

<!-- b000409 | prose | pages [12] -->
Reduction

<!-- b000410 | prose | pages [12] -->
Max:2308.56

<!-- b000411 | furniture | pages [12] -->


<!-- b000412 | prose | pages [12] -->
Cost Per 10 Million

<!-- b000413 | prose | pages [12] -->
Investment

<!-- b000414 | prose | pages [12] -->
Min:0

<!-- b000415 | prose | pages [12] -->
Increase

<!-- b000416 | prose | pages [12] -->
Max:224.56

<!-- b000417 | prose | pages [12] -->
Government

<!-- b000418 | prose | pages [12] -->
Min:0

<!-- b000419 | prose | pages [12] -->
Subsidization

<!-- b000420 | prose | pages [12] -->
Max:67.23

<!-- b000421 | prose | pages [12] -->
Taxes

<!-- b000422 | prose | pages [12] -->
Min:0

<!-- b000423 | prose | pages [12] -->
Increase

<!-- b000424 | prose | pages [12] -->
Max:132.61

<!-- b000425 | prose | pages [12] -->
Among the three factors of social benefits, environment improve has the least range. That means, the comparative validity is most sensitive to environment improve. As a result, if we want to maintain the efficiency of investment on EV, the environmental improve must be highlighted considered. As to vehicle manufacturer, they must try best to develop cleaning techniques to reduce the pollution from batteries producing. They also need considering to reduce the indirect pollution from EVs. As to governments, they should promote the improving of power plants’ energy grid to reduce pollution when generate electricity for batteries.

<!-- b000426 | furniture | pages [12] -->


<!-- b000427 | prose | pages [12] -->
Among those three factors, investment increase has the largest range. That means, governments and enterprises can expand their investing on related infrastructures to ensure the convenience of EVs’ use.

<!-- b000428 | furniture | pages [12] -->


<!-- b000429 | prose | pages [12] -->
Among factors of social costs, government subsidization has the least range. That means, the comparative validity is most sensitive to government subsidization. Governments should properly subsidize the EV industries. In terms of taxes government should also be careful.

<!-- b000430 | furniture | pages [13] -->
Team # 9089                                                                                      Page 13 of 20

<!-- b000431 | prose | pages [13] -->
Conclusively, environment, investment and subsidization are the most vital considerations to promote EVs to widespread use.

<!-- b000432 | furniture | pages [13] -->


<!-- b000433 | heading | pages [13] -->
2.2  Reduction of Fossil Fuels Using

<!-- b000434 | prose | pages [13] -->
Petroleum, natural gas and coal are all fossil fuels. Thus savings of one of those three substances means savings of fossil fuels. To calculate the reduction of oil using, we analyze its consumptions of CVs and EVs respectively. We make a contrast between the following two scenarios: All vehicles are CVs; There are vehicles of CVs and EVs as Figure.7 shown.

<!-- b000435 | furniture | pages [13] -->


<!-- b000436 | prose | pages [13] -->
For the former assumption, we investigate the consumption of CV.

<!-- b000437 | furniture | pages [13] -->


<!-- b000438 | prose | pages [13] -->
Table.11 Consumption of CV (Unit: 1011J per vehicle)[21]

<!-- b000439 | prose | pages [13] -->
Year 1991 1992 1993 1994 Consumption 1995 1996 1997 1998 1999 1.2561 1.2491 1.25127 1.2492

<!-- b000440 | prose | pages [13] -->
Year 2000 2001 2002 2003 Consumption

<!-- b000441 | prose | pages [13] -->
1.2502 1.2516 1.2585 1.2656 1.267

<!-- b000442 | prose | pages [13] -->
2004 2005 2006 2007 2008 1.2352 1.2666 1.2081 1.2354

<!-- b000443 | furniture | pages [13] -->


<!-- b000444 | prose | pages [13] -->
1.2449 1.2464 1.2486 1.2458 1.2371

<!-- b000445 | prose | pages [13] -->
We find the data are steady. Considering that oil consumption would not change much in the next 10 years, we use the average number of Table.11 as CV’s consumption. According to 2009’s energy grid[22], 97% energy consumption of transportation is from fossil fuel, while the overall fuel efficiency of CV is 14%. To be more general, we convert the energy consumption to barrel oil equivalent[23], by 1 barrel = 6.117×109 J. With the global number of vehicles, we figure out the barrel oil consumption.

<!-- b000446 | furniture | pages [13] -->


<!-- b000447 | prose | pages [13] -->
Table.12 Scenario One’s Consumption (Unit: billion barrels) 2011 2012 2013 2014 Year 2015 2016 2017 2018 2019 2020

<!-- b000448 | prose | pages [13] -->
Consumption 35.986 36.549 37.182 37.977 38.460 38.938 39.420 39.948 40.476 40.410

<!-- b000449 | furniture | pages [13] -->


<!-- b000450 | prose | pages [13] -->
For the latter assumption, we figure out the CVs’ numbers of each year and each year’s consumption of CVs with the same method. Then we investigate EVs’ mileages traveled yearly [21].

<!-- b000451 | furniture | pages [13] -->


<!-- b000452 | prose | pages [13] -->
Table.13 CV’s Mileage (Unit: km) Year 1991 1992 1993 1994

<!-- b000453 | prose | pages [13] -->
Mileage 18534.3 18951.0 18997.0 19111.5

<!-- b000454 | prose | pages [13] -->
Year 2000 2001 2002 2003

<!-- b000455 | prose | pages [13] -->
Mileage 19911.6 19438.0 19963.3 20053.9

<!-- b000456 | furniture | pages [13] -->


<!-- b000457 | prose | pages [13] -->
1995 1996 1997 1998 1999

<!-- b000458 | prose | pages [13] -->
19300.0 19338.6 19795.1 19964.0 19972.5

<!-- b000459 | prose | pages [13] -->
2004 2005 2006 2007 2008

<!-- b000460 | prose | pages [13] -->
20062.2 19897.4 19819.6 19688.4 19236.5

<!-- b000461 | prose | pages [13] -->
According to the electricity consumption of each vehicle 0.2kW·h/km[1], and from  2009’s energy grid[22], 67% energy consumption of transportation is from fossil fuel, while the overall fuel efficiency of EV is 28%, we figure out the barrel oil consumption of EVs. Finally we get the consumptions of this scenario.

<!-- b000462 | prose | pages [13] -->
Table.14 Scenario Two’s Consumption (Unit: billion barrels) 2011 2012 2013 2014 Year

<!-- b000463 | prose | pages [13] -->
Consumption 35.288 35.688 35.888 35.807

<!-- b000464 | prose | pages [13] -->
2015 2016 2017 2018 2019 2020

<!-- b000465 | prose | pages [13] -->
34.660 32.296 28.456 23.180 16.692 8.606

<!-- b000466 | furniture | pages [14] -->
Team # 9089                                                                                      Page 14 of 20

<!-- b000467 | prose | pages [14] -->
From Table.12 and Table.14, we estimate the total savings of oils of each year in the next decade shown in Table.15.

<!-- b000468 | prose | pages [14] -->
Table.15 Oils Savings Estimated (Unit: billion barrels) 2011 2012 2013 2014 Year

<!-- b000469 | prose | pages [14] -->
Saving 0.698 0.861 1.293 2.170

<!-- b000470 | furniture | pages [14] -->


<!-- b000471 | prose | pages [14] -->
2015 2016 2017 2018 2019 2020

<!-- b000472 | prose | pages [14] -->
3.801 6.642 10.964 16.768 23.783 31.803

<!-- b000473 | prose | pages [14] -->
The trend of savings is shown in Figure.10. Comparing with EIA data[7], with widespread use of EVs, in the year 2011 world savings of oils will be 1.1% of total. And in the year 2020 the saving ratio could be 49% if the annual consumption of oil maintains the 2009’s level. So the model we established suits the actual scenario.

<!-- b000474 | furniture | pages [14] -->


<!-- b000475 | prose | pages [14] -->
Figure.10 Oils Savings in the Next Decade

<!-- b000476 | furniture | pages [14] -->


<!-- b000477 | heading | pages [14] -->
2.3  Optimization of Energy Grid

<!-- b000478 | prose | pages [14] -->
To take EVs’ impacts on environment, society, business and individuals, we establish a multi-goal programming model to analyze the amount and type of electricity generation. Firstly, we adopt Analytic Hierarchy Process (AHP) to estimate the impact levels on environment, society, business and individuals. Thus we empower the four aspects and define an overall evaluation index as the objective function to conduct optimization.

<!-- b000479 | furniture | pages [14] -->


<!-- b000480 | prose | pages [14] -->
Figure.11 AHP Structure We make pairwise comparisons of environment, society, business and individuals and get the comparison matrix[24]:

<!-- b000481 | furniture | pages [15] -->
Team # 9089                                                                                      Page 15 of 20

<!-- b000482 | prose | pages [15] -->


<!-- b000483 | prose | pages [15] -->
1

<!-- b000484 | prose | pages [15] -->


<!-- b000485 | prose | pages [15] -->
1

<!-- b000486 | prose | pages [15] -->
 

<!-- b000487 | prose | pages [15] -->
5

<!-- b000488 | prose | pages [15] -->
 

<!-- b000489 | prose | pages [15] -->
A

<!-- b000490 | prose | pages [15] -->
1

<!-- b000491 | prose | pages [15] -->


<!-- b000492 | prose | pages [15] -->
7

<!-- b000493 | prose | pages [15] -->
 

<!-- b000494 | prose | pages [15] -->
1

<!-- b000495 | prose | pages [15] -->
 

<!-- b000496 | prose | pages [15] -->
9

<!-- b000497 | prose | pages [15] -->


<!-- b000498 | prose | pages [15] -->
5 5 7 9

<!-- b000499 | prose | pages [15] -->
 

<!-- b000500 | prose | pages [15] -->
1 1 6 5

<!-- b000501 | prose | pages [15] -->
 

<!-- b000502 | furniture | pages [15] -->


<!-- b000503 | prose | pages [15] -->
1 1

<!-- b000504 | prose | pages [15] -->


<!-- b000505 | prose | pages [15] -->
1 2 6 6

<!-- b000506 | prose | pages [15] -->
 

<!-- b000507 | prose | pages [15] -->
1 1 1 1

<!-- b000508 | prose | pages [15] -->
 

<!-- b000509 | prose | pages [15] -->
5 5 2

<!-- b000510 | prose | pages [15] -->
We figure out the maximum eigenvalues and the corresponding eigenvectors and the normalized data are:

<!-- b000511 | prose | pages [15] -->
   max

<!-- b000512 | furniture | pages [15] -->


<!-- b000513 | prose | pages [15] -->
(0.5048,0.2635,0.1245,0.1071) 4.2656, v max

<!-- b000514 | prose | pages [15] -->
Make a consistency test:

<!-- b000515 | prose | pages [15] -->
 4.2656 4   CI 0.088533, RI 3 CI     0.96, CR 0.0922 0.1

<!-- b000516 | furniture | pages [15] -->


<!-- b000517 | prose | pages [15] -->
RI

<!-- b000518 | prose | pages [15] -->
Thus matrix A passes the consistency test, meaning that this multi-goal programming model can be simplified to a mono-goal programming model.

<!-- b000519 | furniture | pages [15] -->


<!-- b000520 | prose | pages [15] -->
According to Table.8, we convert the impacts on environment, society, business and individuals to prices denoted as ξ1, ξ2, ξ3 and ξ4. We also denote Psumt as the total electricity generated by electricity grid for EVs in year t. And mark α1, α2, α3 and α4 to represent the ratio of electricity generated respectively by thermal power plant, hydropower plant, nuclear power plant and wind power plant in the year t. Also we suppose R(t) is the overall benefits to the environment, society, business and individuals in the year t.

<!-- b000521 | furniture | pages [15] -->


<!-- b000522 | prose | pages [15] -->
Thus，the first-order objective function is:

<!-- b000523 | prose | pages [15] -->
   max R t ( ) (0.5048 0.2635 1 1     

<!-- b000524 | furniture | pages [15] -->


<!-- b000525 | prose | pages [15] -->
0.1245 0.1071 ) P 2 2 2 3 3 4 4 sumt

<!-- b000526 | prose | pages [15] -->
The second-order objective function is: (aiming at the least energy conception of thermal power unit)

<!-- b000527 | prose | pages [15] -->
min U t   ( ) ( ) P

<!-- b000528 | furniture | pages [15] -->


<!-- b000529 | prose | pages [15] -->
1 sumt

<!-- b000530 | prose | pages [15] -->
Constraints are as follows: (Suppose there are abundant sources for thermal power plant and nuclear power plant):

<!-- b000531 | furniture | pages [15] -->


<!-- b000532 | prose | pages [15] -->
 To thermal power plant:

<!-- b000533 | prose | pages [15] -->
n n

<!-- b000534 | prose | pages [15] -->
1

<!-- b000535 | prose | pages [15] -->
 

<!-- b000536 | prose | pages [15] -->
(

<!-- b000537 | prose | pages [15] -->
b P

<!-- b000538 | prose | pages [15] -->
)

<!-- b000539 | prose | pages [15] -->
i t

<!-- b000540 | prose | pages [15] -->
,

<!-- b000541 | prose | pages [15] -->
i t

<!-- b000542 | prose | pages [15] -->
,

<!-- b000543 | prose | pages [15] -->
 

<!-- b000544 | prose | pages [15] -->
i

<!-- b000545 | prose | pages [15] -->
1

<!-- b000546 | prose | pages [15] -->
j

<!-- b000547 | prose | pages [15] -->
1

<!-- b000548 | prose | pages [15] -->
D

<!-- b000549 | prose | pages [15] -->


<!-- b000550 | prose | pages [15] -->


<!-- b000551 | prose | pages [15] -->


<!-- b000552 | prose | pages [15] -->
D

<!-- b000553 | prose | pages [15] -->
P P

<!-- b000554 | furniture | pages [15] -->


<!-- b000555 | prose | pages [15] -->
max,

<!-- b000556 | prose | pages [15] -->
t

<!-- b000557 | prose | pages [15] -->
1

<!-- b000558 | prose | pages [15] -->
sumt

<!-- b000559 | prose | pages [15] -->
means the maximum load demand in the year t.  is a coefficient to meet P

<!-- b000560 | prose | pages [15] -->
In this equation:

<!-- b000561 | prose | pages [15] -->
max,

<!-- b000562 | prose | pages [15] -->
t b is a coefficient meaning the avail of thermal power unit remained in the maximum load demand.

<!-- b000563 | prose | pages [15] -->
,i t P means the installed capacity of thermal power unit in the year t. the year t.

<!-- b000564 | prose | pages [15] -->
,i t

<!-- b000565 | furniture | pages [15] -->


<!-- b000566 | prose | pages [15] -->
 To hydropower plant:

<!-- b000567 | furniture | pages [16] -->
Team # 9089                                                                                      Page 16 of 20

<!-- b000568 | prose | pages [16] -->
  min Q it 2

<!-- b000569 | prose | pages [16] -->
min

<!-- b000570 | prose | pages [16] -->
 max

<!-- b000571 | furniture | pages [16] -->


<!-- b000572 | prose | pages [16] -->
P P Q sumt it

<!-- b000573 | prose | pages [16] -->
is the minimum water supply to hydropower plant at its location in the year t. In this equation:

<!-- b000574 | prose | pages [16] -->
Q it

<!-- b000575 | prose | pages [16] -->
max is the maximum water supply to hydropower plant at its location in the year t. Q it

<!-- b000576 | prose | pages [16] -->
T

<!-- b000577 | prose | pages [16] -->
 w dt jt

<!-- b000578 | prose | pages [16] -->
0

<!-- b000579 | prose | pages [16] -->
   W

<!-- b000580 | prose | pages [16] -->
0

<!-- b000581 | furniture | pages [16] -->


<!-- b000582 | prose | pages [16] -->
jT

<!-- b000583 | prose | pages [16] -->
w is the water consumption rate at a certain interval in the year t. In this equation:

<!-- b000584 | prose | pages [16] -->
jt total water supply from the year t to T.

<!-- b000585 | furniture | pages [16] -->


<!-- b000586 | prose | pages [16] -->
 To nuclear power plant:

<!-- b000587 | prose | pages [16] -->
n n

<!-- b000588 | prose | pages [16] -->
1

<!-- b000589 | prose | pages [16] -->
 

<!-- b000590 | prose | pages [16] -->
(

<!-- b000591 | prose | pages [16] -->
c K

<!-- b000592 | prose | pages [16] -->
)

<!-- b000593 | prose | pages [16] -->
i t

<!-- b000594 | prose | pages [16] -->
,

<!-- b000595 | prose | pages [16] -->
i t

<!-- b000596 | prose | pages [16] -->
,

<!-- b000597 | prose | pages [16] -->
 

<!-- b000598 | prose | pages [16] -->
i

<!-- b000599 | prose | pages [16] -->
1

<!-- b000600 | prose | pages [16] -->
j

<!-- b000601 | prose | pages [16] -->
1

<!-- b000602 | prose | pages [16] -->
W is the jT

<!-- b000603 | prose | pages [16] -->


<!-- b000604 | prose | pages [16] -->


<!-- b000605 | prose | pages [16] -->


<!-- b000606 | prose | pages [16] -->
D

<!-- b000607 | prose | pages [16] -->
K P

<!-- b000608 | furniture | pages [16] -->


<!-- b000609 | prose | pages [16] -->
max,

<!-- b000610 | prose | pages [16] -->
t

<!-- b000611 | prose | pages [16] -->
3

<!-- b000612 | prose | pages [16] -->
sumt

<!-- b000613 | prose | pages [16] -->
means the maximum load demand in the year t.  is a coefficient to meet

<!-- b000614 | prose | pages [16] -->
D

<!-- b000615 | prose | pages [16] -->
K

<!-- b000616 | prose | pages [16] -->
In this equation:

<!-- b000617 | prose | pages [16] -->
max,

<!-- b000618 | prose | pages [16] -->
t c is a coefficient meaning the avail of nuclear power unit remained in the maximum load demand.

<!-- b000619 | prose | pages [16] -->
,i t K means the installed capacity of nuclear power unit in the year t. the year t.

<!-- b000620 | prose | pages [16] -->
,i t

<!-- b000621 | furniture | pages [16] -->


<!-- b000622 | prose | pages [16] -->
 To wind power plant:

<!-- b000623 | prose | pages [16] -->
  min F it 4

<!-- b000624 | prose | pages [16] -->
min

<!-- b000625 | prose | pages [16] -->
 max P P F

<!-- b000626 | furniture | pages [16] -->


<!-- b000627 | prose | pages [16] -->
sumt it

<!-- b000628 | prose | pages [16] -->
is the minimum wind supply to wind power plant at its location in the year t. In this equation:

<!-- b000629 | prose | pages [16] -->
F it

<!-- b000630 | prose | pages [16] -->
max is the maximum wind supply to wind power plant at its location in the year t. F it

<!-- b000631 | furniture | pages [16] -->


<!-- b000632 | prose | pages [16] -->
 Balance between electricity supply and demand:

<!-- b000633 | prose | pages [16] -->
 P n C sumt 1

<!-- b000634 | prose | pages [16] -->
1n is total number of BEVs.

<!-- b000635 | prose | pages [16] -->
C In this equation:

<!-- b000636 | prose | pages [16] -->


<!-- b000637 | furniture | pages [16] -->


<!-- b000638 | prose | pages [16] -->
n C bev bev 2 phev

<!-- b000639 | prose | pages [16] -->
2n is total is electricity consumption per BEV. bev bev number of PHEVs. Cphev is electricity consumption per PHEV. Then we can solve this model by following steps: Step1. Initialize t=1. Step2. According to optimization criterion, we optimize the first-order objective function by decision

<!-- b000640 | prose | pages [16] -->
variable [α1, α2, α3, α4]T. If the optimal solutions do not exist, feasible solutions are acceptable. Otherwise we obtain the optimal solutions. Step3. Observe the solutions from Step2. If [α1, α2, α3, α4]T are unique, go to Step5. Otherwise go to

<!-- b000641 | prose | pages [16] -->
Step4. Step4. According to optimization criterion, we optimize the second-order objective function by

<!-- b000642 | prose | pages [16] -->
decision variable α1t. If the optimal solutions do not exist, feasible solutions are acceptable. Otherwise we obtain the optimal solutions. Step5. t=t+1. Go to Step2 to calculate the amount of each type of electricity generation in the next

<!-- b000643 | prose | pages [16] -->
year. Take the conditions of USA as an example. We collect data[25] from EIA’s website about USA, and figure out the amount and type of electricity generation in 2020 in Figure.12.

<!-- b000644 | furniture | pages [17] -->
Team # 9089                                                                                      Page 17 of 20

<!-- b000645 | furniture | pages [17] -->


<!-- b000646 | prose | pages [17] -->
Figure.11 Amount and Type of Electricity Generation in 2020 in USA And in the next decade, the amounts and types of electricity generation every year are in Figure.12.

<!-- b000647 | furniture | pages [17] -->


<!-- b000648 | prose | pages [17] -->
Figure.12 Amount and Type of Electricity Generation in the Next Decade in USA

<!-- b000649 | furniture | pages [17] -->


<!-- b000650 | heading | pages [17] -->
3. Assessments of Models

<!-- b000651 | heading | pages [17] -->
3.1 Bass Diffusion Model

<!-- b000652 | prose | pages [17] -->
When estimate the feasibility to introduce EVs, one of factors we consider is the market adoption. We establish Bass Diffusion Model to predict the sales of EVs in the next decade. We use ACO to calculate the parameters instead of conventional methods. By ACO, the shortcoming of the basic Bass Model, high dependence on data, is overcome. By sensitivity analysis, the model has an acceptable sensitivity level.

<!-- b000653 | heading | pages [17] -->
3.2 Improved BP Artificial Neutral Network

<!-- b000654 | prose | pages [17] -->
We combine BP Artificial Neutral Network with GM. BP-ANN has the ability to approximate arbitrary functions, but may impact the generalization due to excessive approximation. While GM fails to approximate complex nonlinear functions, but can better predict the changing trends. Also, BP-ANN needs abundant hidden nodes to be well trained, which also enlarge the number of parameters and the sample data. While GM only needs a little sample data. Our improved model takes the advantages from the two models and can make prediction more accurate.

<!-- b000655 | furniture | pages [18] -->
Team # 9089                                                                                      Page 18 of 20

<!-- b000656 | heading | pages [18] -->
3.3 Data Envelopment Analysis

<!-- b000657 | prose | pages [18] -->
We use DEA to make assessment on EV’s social effects. It identifies the efficient and inefficient units in a sample of decision making units and provides targets for inefficient ones. The problem of sorting the frontier resident units to accomplish some goal is very important especially when a large number of units are deemed efficient.

<!-- b000658 | furniture | pages [18] -->


<!-- b000659 | heading | pages [18] -->
3.4 Multi-Goal Programming Model

<!-- b000660 | prose | pages [18] -->
We establish a multi-goal programming model to optimize the electricity generation structure. We use AHP to convert the multi-goal programming model to mono-goal programming model. This makes the model solvable. However, we simplify the constraints deeply. This may result in some errors.

<!-- b000661 | furniture | pages [18] -->


<!-- b000662 | heading | pages [18] -->
4. Conclusions and Suggestions

<!-- b000663 | heading | pages [18] -->
4.1 Conclusions

<!-- b000664 | prose | pages [18] -->
By large scale use of EVs, aspects about economy, environment, health and society will be affected. The impacts are mainly positive. In details, this promotion improves the environment by reducing emissions of air pollutants, so that people’s health levels up. Wide use of EVs will also have economical benefits since its marketing has bright prospects with fat profits. It will also bring increases to a series of industries’ development. By analyzing these, we are sure that widespread use of EVs can be and should be promoted.

<!-- b000665 | furniture | pages [18] -->


<!-- b000666 | prose | pages [18] -->
From the calculation in Section 2.2, the introduction of EVs significantly reduces the energy consumption. Also, this introduction also leads to a progress of current structure energy grid to achieve a maximum benefit.

<!-- b000667 | furniture | pages [18] -->


<!-- b000668 | prose | pages [18] -->
Government and manufacturers should take care of investing and subsidizing the EV industries to ensure the healthy development of industries related to EVs. Among all of the impacts, environment factor may be the core consideration of them.

<!-- b000669 | furniture | pages [18] -->


<!-- b000670 | heading | pages [18] -->
4.2 Suggestions

<!-- b000671 | prose | pages [18] -->
 Researchers and manufacturers According to our analyzing, the costs (mainly consisting of batteries costs), infrastructures and mileage of EV will have backward effects on the promotion of EV. Due to the developing techniques, the sales cost and mileage of EV will be improved and meet the market demands without any doubts. Thus, removal of supply constraints and improving battery charging and recycling should be the main technique considerations by researchers and manufacturers.

<!-- b000672 | furniture | pages [18] -->


<!-- b000673 | prose | pages [18] -->
 Governments To make this introduction more meaningful and efficient, reduce the indirect pollution from EV is the key point. Furthermore, governments should play a right role in the revolution process, avoiding improper subsidization and tax. Meanwhile, governments should take advantage of the uprising industry to improve the employment by increase jobs available in charging stations and battery services, for example.

<!-- b000674 | furniture | pages [18] -->


<!-- b000675 | furniture | pages [19] -->
Team # 9089                                                                                      Page 19 of 20

<!-- b000676 | prose | pages [19] -->
 Cooperation Though use of EV can sharply cut down the emissions of air pollutants, a social cooperation should be established, including governments, researchers, manufacturers and other related people, to create a platform to improve the techniques of EV. The final aim is surely to supply a maximum protection to environment and make people live better.

<!-- b000677 | furniture | pages [19] -->


<!-- b000678 | heading | pages [19] -->
5. References

<!-- b000679 | references | pages [19] -->
[1] Economic Viability of Electric Vehicles, Department of Environment, Climate Change and Water

<!-- b000680 | references | pages [19] -->
NSW (DECCW) by AECOM Australia Pty Ltd, Sep.4, 2009.

<!-- b000681 | references | pages [19] -->
[2] http://en.wikipedia.org/wiki/Bass_diffusion_model

<!-- b000682 | references | pages [19] -->
[3] Abbas A.Kurawarwala, Hirofumi Matsuo. Forecasting and inventory management of short

<!-- b000683 | references | pages [19] -->
life-cycle products. 1994

<!-- b000684 | references | pages [19] -->
[4] http://en.wikipedia.org/wiki/Ant_colony_optimization

<!-- b000685 | references | pages [19] -->
[5]http://www.ce.berkeley.edu/~bayen/ce191www/lecturenotes/lecture10v01_descent2.pdf

<!-- b000686 | references | pages [19] -->
[6] Haitao Fu. Implementations of electric vehicle system based on solar energy in Singapore:

<!-- b000687 | references | pages [19] -->
Assessment of lithium ion batteries for automobiles. Electrical and Electronic Engineering, Nanyang

<!-- b000688 | references | pages [19] -->
Technological University. 2008.

<!-- b000689 | references | pages [19] -->
[7]http://www.bp.com/liveassets/bp_internet/globalbp/globalbp_uk_english/reports_and_publication

<!-- b000690 | references | pages [19] -->
s/statistical_energy_review_2008/STAGING/local_assets/2010_downloads/statistical_review_of_wo

<!-- b000691 | references | pages [19] -->
rld_energy_full_report_2010.pdf

<!-- b000692 | references | pages [19] -->
[8] Annual Energy Outlook 2009 with projections to 2030. Energy Information Administration,

<!-- b000693 | references | pages [19] -->
Office of Integrated Analysis and Forecasting, U.S. Department of Energy. March 2009.

<!-- b000694 | references | pages [19] -->
[9] Thomas A.Becker, Ikhlaq Sidhu, Burghardt Tenderich. Electric Vehicle in the United States: A

<!-- b000695 | references | pages [19] -->
new Model with Forecasts to 2030. Center for Entrepreneurship & Technology(CET) , University of

<!-- b000696 | references | pages [19] -->
California, Berkeley.

<!-- b000697 | references | pages [19] -->
[10] Andrew Ford. The impacts of large scale use of electric vehicles in southern California. Energy

<!-- b000698 | references | pages [19] -->
and Buildings. 22 (1995) 207-218.

<!-- b000699 | references | pages [19] -->
[11] Li Zhigang, Feng Shuzhe. Investigation on charges calculation for disposing waste gas from

<!-- b000700 | references | pages [19] -->
coal-fired heat-engine plant. Energy Environmental Protection. Vol.18, No.3. Jun.2004.

<!-- b000701 | references | pages [19] -->
[12] http://www.eia.doe.gov/aer/pecss_diagram.html

<!-- b000702 | references | pages [19] -->
[13] http://www.cceec.com.cn/html/Gas/LPG/News/2010/1116/15006.html

<!-- b000703 | references | pages [19] -->
[14] http://www.world-nuclear.org/education/ehs.html

<!-- b000704 | references | pages [19] -->
[15] Xiao Xinping, Deng Julong , A New Modified GM (1,1) Model: Grey Optimization

<!-- b000705 | references | pages [19] -->
Model,Journal of Systems Engineering and Electronics, 2001 12(2)

<!-- b000706 | references | pages [19] -->
[16] http://cta.ornl.gov/data/tedb29/Edition19_chapter03.pdf

<!-- b000707 | references | pages [19] -->
[17] Eric Harkness. CO2 shadow prices in the U.S. electric utility industry: Calculating the costs of

<!-- b000708 | references | pages [19] -->
reducing CO2 emissions. University of Tennessee.

<!-- b000709 | references | pages [19] -->
[18] Karina Funk, Ari Rabl. Electric versus conventional vehicles: social costs and benefits in France.

<!-- b000710 | references | pages [19] -->
Transportation Research. Part D 4 (1999) 397-411.

<!-- b000711 | references | pages [19] -->
[19] T. Sowlati. Information systems project prioritization using data envelopment analysis.

<!-- b000712 | references | pages [19] -->
Mathematical and computer modeling. 41(2005) 1279-1298.

<!-- b000713 | references | pages [19] -->
[20] Fredrik Carlsson, Olof Johansson-Stenman. Costs and Benefits of Electric Vehicles. Journal of

<!-- b000714 | references | pages [19] -->
Transport Economics and Policy. Vol.37, Part.1, Jan,2003,1-28.

<!-- b000715 | references | pages [19] -->
[21] http://cta.ornl.gov/data/chapter3.shtml

<!-- b000716 | furniture | pages [20] -->
Team # 9089                                                                                      Page 20 of 20

<!-- b000717 | references | pages [20] -->
[22] http://www.eia.doe.gov/aer/pecss_diagram.html

<!-- b000718 | references | pages [20] -->
[23] http://en.wikipedia.org/wiki/Barrel_of_oil_equivalent

<!-- b000719 | references | pages [20] -->
[24] Kamal M.Al-Subhi Al-Harbi. Application of the AHP in projection management. International

<!-- b000720 | references | pages [20] -->
Journal of Project Management. 19 (2001) 19-27.

<!-- b000721 | references | pages [20] -->
[25] http://www.eia.doe.gov/cneaf/electricity/epa/epa_sum.html

<!-- b000722 | furniture | pages [20] -->


<!-- b000723 | furniture | pages [20] -->


<!-- b000724 | furniture | pages [20] -->


<!-- b000725 | furniture | pages [20] -->


<!-- b000726 | furniture | pages [20] -->


<!-- b000727 | furniture | pages [20] -->

