MCM/ICM

Summary Sheet

Summary

Current food system prioritizes efficiency and profitability while ignoring the sustainability and equity. The problem mainly is reflected two aspects. One is environment damage due to overproduction and chemical abuse. The other is hunger and inequity problem. So, it is urgent to optimize the current food system.

First, we propose the Production Model, which can estimate every coun- try’s food output under different production condition. To consider the model more comprehensively, we divide the whole food system into three subsystems (planting, husbandry and fisheries) and introduce various indicators affecting production in every subsystem. The system optimization for sustainability is-

sues calls governments to impose some policy interventions and we can evaluate the influence of the interventions on food output by using Production Model.

Second, we design an Equitable Distribution Model to tackle the equity issues, in which countries of food surplus will subsidize the Low-Income Food- Deficit Countries (LIFDCs) voluntarily. The Hand-in-Hand initiative is designed based on the principle of minimizing the transportation cost between donor coun- ties and beneficiary countries.

We also establish the growth model after introducing the time dimension. The model is created to response the future population growth.

Furthermore, we apply our model in one developed country USA and one developing country Nepal to evaluate the benefits and costs of system opti- mization and compare the difference between developed country and developing country. Specifically, the food output value of USA’s planting, husbandry, and fishery industry will decline 2.1%,1.1% and 1.2% respectively, and USA need pay 20.55 million dollars for transportation cost to assist the least developed country Haiti and Guatemala. The benefit is that USA can experience the envi- ronmental improvement. Environmental damage to air, water and land will all be mitigated. For Nepal, the number of starving people will decline because of more access to food. One source is the donation from Ukraine and the other source is increased food output due to the accessible chemicals. The food output value of Nepal’s planting, husbandry, and fishery industry will increase 5.4%,2.9% and 1.5% respectively.

Finally, we analyze the scalability and adaptability of our model and point out our strength and weakness.

1 Introduction

微信公众号：数学模型

1.1 Problem Background

Food is fundamental to human wellbeing, and food production involves all aspects of social life. However, we think the current food system has severe limitations.

One disadvantage is that our current global system causes severe environ- mental damage to the environment due to overproduction and chemical abuse. The other is the food distribution is very desigual across continents and regions of the world. Millions of people suffer hunger although there are abundant global 微信号：MATHmodels food output.

Consequently, it is reasonable and critical to transform our food systems to be more environmentally sustainable and able to deliver healthy and nutritious diets to all as equally as possible.

1.2 Our Works

First, we propose the Production Model, which estimates the maximum lev- els of the country’s food production to reflect its potential food productivity based on the priority to efficiency and profitability. Specifically, we divide the whole food system into three subsystems (planting, husbandry and fisheries) and con- sider various indicators affecting production in every subsystem. Then we can figure out how the implementation of sustainability policies influence the food productivity using the Production Model.

Second, we design an Equitable Distribution Model to tackle the equity is- sues, in which countries of food surplus will subsidize the Low-Income Food- Deficit Countries (LIFDCs) voluntarily. We devote to calculating the most eco- nomical redistribution approach of the current food possessions to achieve the goal of improving nutrition in LIFDCs.

Based on the static production model, we introduce the time dimension and establish the growth model. It is obvious that labor and ASTI in Production Model are factors that vary with time, so we can come to a further comprehensive food system model considering the dynamic trend of population and scientific development.

Thereafter, we can make predictions of future trends after changing prior- ities, assess the process of its implement and then further discuss the benefits and costs of the optimized system between developing countries and developed countries. To compare the difference more clearly, we specifically applied the model to two countries：one is the USA, a developed country and the other is 微信公众号：数学模型 Nepal, a developing country.

Finally, we are also required to test the scalability and adaptability of our model and make necessary sensitive analysis. The whole modeling process is shown in Fig 1.

微信号：MATHmodels Figure 1

1.3 General Assumptions

• We divide all countries into two categories: one is country with surplus food production and the other is country with deficit food production. Some of the former is blamed for overproduction and chemical abuse and some of the latter is susceptible to limited technology access.

• In production model, we choose the most classic one as a representative for countries with multiple types of climate and geographic characteristics. And we assume the labor force and population share the same growth rate.

• We assume countries with abundant food production are willing to assist the least developed countries for nothing.

• We assume most people suffering hunger come from the least developed countries. So only people from the least developed countries need assis- tance.

• When analyzing the production future trend, we assume every country shares the same rate of technology progress and population growth.

2 Food System Optimization

微信公众号：数学模型

2.1 Production Model

We define food production model in the country level. There are huge dif- ferences in food production capacity in different countries. So, the model is es- tablished to figure out every country’s largest food production ability. To con- sider the question comprehensively, we divide the whole food industry into three subindustries including planting, husbandry and fisheries. If we use the produc- tion volume reflecting the food production ability, we can’t add three industries’ volume together directly because the unit is different. So, we calculate the total 微信号：MATHmodels food production value.

2.1.1 Model

We use BP (back propagation) neural networks to describe the production model. The neuron model used here is the ”M-P neuron model” proposed by McCulloch and Pitts (1943), and the model is as follows:

Figure 2

In this model, neurons receive input signals from n other neurons, which are transmitted by weighted connection. The total input value received by neurons is compared with the threshold value of neurons, and then processed by ”activa- tion function” to produce the output of neurons. Multiple neurons connect with each other to form a specific network structure. Thus, a mathematical model is obtained, in which several functions (such as:y = f (∑ i wixi −θj) ) are nested into each other.

Our model uses single-layer feed for world neural networks, which is com- posed of input layer, single hidden layer and output layer, as shown in the figure 微信公众号：数学模型 Figure 3

微信号：MATHmodels above. The hidden layer contains eight neurons, each of which takes the relu function as the activation function. And, the output layer neuron takes as the activation function. The relu function is as follows:

Figure 4

The input layer neurons accept the external input; the hidden layer and out- put layer neurons process the input, and finally the output layer neurons output the results, that is, the input layer neurons only accept the input, not the function processing.

Suppose there is a single-layer feedforward neural network with d input neurons, l output neurons and q hidden layer neurons. θj is used to represent the threshold value of the jth neuron in the output layer; γh is used to represent the threshold value of the hth neuron in the hidden layer; vih is used to repre- sent the connection weight between the ith neuron in the input layer and the hth neuron in the hidden layer; whj is used to represent the connection weight be- tween the hth neuron in the hidden layer and thejth neuron in the output layer; αh = ∑d i=1 vin xi is used to represent the input received by the hth neuron in the hidden layer;βj = ∑q 微信公众号：数学模型 h=1 whjbh is used to represent the input received by the jth neuron in the output layer and use bh to represent the output of the hth neuron in the hidden layer. It is assumed that both hidden layer and output layer use sigmoid function as activation function f. So, we can get the back propagation algorithm used in the training model (Chauvin Rumelhart, 1995).BP algorithm.

Input：Training set D = {(xk, yk)}m k=1 ;Learning rate η.

Process:

1.In the range of (0,1), all weights of connections and thresholds in the neu- ral network are initialized randomly.

2.repeat for all (xk, yk) ∈D do 微信号：MATHmodels

• The output ˆyk of the current sample is calculated by ˆyk j = f (βj −θj) ( )2 ∑l

• The mean square error Ek is calculated by Ek = 1 ˆyk j −yk j=1 j 2

j · ∂ˆyk

• The gradient term gj of output layer neurons is calculated by gj = −∂Ek j ∂ˆyk ∂βj

• The gradient term eh of hidden layer neurons is calculated by eh = −∂Ek ∂bh · ∂bh ∂αh

• The connection weight whj ,vih and the threshold θj,γh are updated by ∆whj = ηgjbh and ∆γh = −ηeh

end for ∑m 3. until The minimum value of 1 k=1 Ek is reached m Output：Multilayer feedforward neural network connecting weight and thresh- old determination.

2.1.2 Planting industry

For planting industry, we mainly think about following aspects.Labor1 de- notes the number of people who engage in planting production in this coun- try.Chemical1 denotes the chemicals such as fertilizers and pesticides use vol- ume per unit of cropland. It is common knowledge that chemical is a double- edged sword. On the one hand, chemical fertilizers can promote food produc- tion, on the other hand, they are harmful to the environment. Another important thing is that the use of chemicals is not the more the better. There exists a limit value beyond which any marginal increase on chemicals is not only useless to the growth of the crops, but will kill plants.Area1 denotes the country’s arable area. The larger the arable area, the more food production.Intensity index is an index describing crop planting density and its value varies from 1 to 10. With 微信公众号：数学模型 increasing index, the production will increase. When the intensity index exceeds the limit value 10 , too high density will cause harm to the crop growth.The land quality itself is also a factor affecting production. One reason why African coun- tries produce so low food production is that the majority of land in Africa is not very suitable for farming. The level of quality can be measured by the content of beneficial and harmful microorganisms in the soil and we can rank them for three levels: “good, ordinary, and bad”.Climate denotes the country’s climate type which can also affect the food production. There are five main climate types including temperate marine climate, tropical rainforest climate, temperate conti- nental climate, savanna climate and tropical desert climate. Land production in different climate area has significant difference. Based on the geographic knowl- 微信号：MATHmodels edge and historical food production data, rank from large to small by superior- ity as follows: tropical rainforest climate, temperate marine climate, temperate continental climate, savanna climate and tropical desert climate.Topography de- notes the country’s terrain. Major topography in the world includes mountains, plateaus, plains, hills and basins and rank from large to small by superiority as follows: plains, basins, hills and plateaus. The last indicator is ASTI (Agricul- ture Science and Technology Indicators) which denotes the country’s technology level.

Based on above indicators, we’ll construct planting production model for every country as follows:

Firstly, we randomly collected planting production samples of 30 countries over the years, which can be expressed as Labori,Chemicalsi, Areai, Intensity indexi,Land qualityi ,Climatei,topographyi,Technologyi, Output valuei and obtained a total of 782 samples from 1993 to 2018. Then we use 70% of the samples to train the model, and the remaining 30% to test the training effect of the model.The train test results are shown in the figure below. As we can see, the model effect is good.

Based on the model we got above, we can calculate that every country’s planting production value maximum. When inputting variables, we use the Chemicals limit value as chemicals data and Intensity index limit value as intensity index data. For the indicator Labor and ASTI, we substitute the current value into the model. The rest of indicators including the arablearea,landquality, climate and topography are all essential attributes for a given country.

微信公众号：数学模型 Figure 5 Figure 6

微信号：MATHmodels Figure 7

2.1.3 Husbandry industry

For husbandry industry, we mainly think about following aspects. Labor2 denotes the number of people who engage in husbandry production in this coun- try.Chemical2 denotes the chemicals use volume used in husbandry industry. Similar to Chemical1 in planting industry, the limit value of chemicals used in husbandry also exists. Area2 denotes the country’s total pasture area including grassland for cows, sheep and so on and venue for chicken, pigs, etc. The larger the pasture area, the more food production. Grazing density is an important fac- tor affecting husbandry production. So the Intensity index is also applied in husbandry model. As we have mentioned above, the index varies between 1 and 10. Feedaccess & quality is critical to husbandry industry development. The easier the access for feed, and the higher the feed quality, the more husbandry industry production. However, it is difficult to acquire direct data about food access and quality. Many researches show that the development of husbandry is closely related to the development of planting. When crops are harvested well, raised animals have a higher probability of obtaining high-quality feeds. So we consider planting development condition as substitution variable. Also, we intro- duce the indicator ASTI describing the country’s technology level. The climate and topography can also affect the husbandry production but the effect is small so we ignore them.

微信公众号：数学模型 The establishment of husbandry production model is similar to the estab- lishment of neural network model of planting production. So we do not repeated more. And the train and test results are not shown in the paper because of the limited space. The model effect is also excellent.

Based on the husbandry production model we got above，we can calculate that every country’s husbandry production value maximum. Variables includ- ing Labor, ASTI, Chemicals and Intensity index are handled in the same way as planting. We think the indicators Pasture area and Feed access and quality are both essential attributes for a given country.

微信号：MATHmodels Figure 8 Figure 9

2.1.4 Fisheries Industry

For fisheries industry, we mainly think about following aspects. Labor3 denotes the number of people who engage in fisheries production in this coun- try.Chemical3 denotes the chemicals use volume used in fisheries industry. Sim- ilar to Chemical1 in planting industry, there also exists a limit value of chemicals used in fisheries industry. Area3 is also an important indicator. The access to ocean or river and the area of ocean or river can directly affect fisheries product. The factor Intensity index is the same as the one in planting industry model. Water quality is another main indicator affecting fisheries production. The logic is quite easy. The better water quality, the more fisheries production. To be more specific, we divide water condition into three levels “good, ordinary, and bad”. And then we use math method to quantify the level. ASTI is also intro- duced to depict the country’s technology level. The climate and topography can also affect the husbandry production but the effect is small so we ignore them.

The establishment of fishery production model is similar to the establish- ment of neural network model of planting production ,so we do not be repeated here. Also, we don’t show the train and test results due to the limited space.

微信公众号：数学模型 Based on the model we got above, we can calculate that every country’s fisheries production value maximum. Following the same logic, Labor, ASTI, Chemicals and Intensity Index are handled in the same way as planting. Water area and Water quality are both considered as essential attributes for a given country.

Adding three industries together, we can obtain every country’s total food production value. The Figure 10 shows the regional distribution of total food production value.

微信号：MATHmodels Figure 10

2.2 Sustainable Policy Intervention

Achieving sustainability goal calls for the government’s intervention. Specif- ically, for countries with experiencing overproduction, governments should pro- pose efficient policies to curb the phenomenon of excessive production. In plant- ing industry, governments can ask farmers to lower crop planting density and stop reclaiming land. For example, Chinese government propose the policy called “return farmland to forest and grassland”. The same restriction can also be ap- plied in husbandry and fisheries system. Governments can give punishments to the farmers engaged in overgrazing and set a fishing quota for fishmen.

The control for chemicals use may be more complex. Chemicals are a double-edged sword. Proper use can increase crop yields but excessive use can cause environmental damage. Some Asian countries who pursue the production maximization use excessive chemicals at the expense of environment. How- ever, some African countries only have low food production because they don’t have access to chemicals. For countries with chemical abuse, it is necessary for 微信公众号：数学模型 governments to restrict excessive use. For poor countries with limited access to chemicals, local governments may invest more public money to assist food industry to enhance local food productivity.

The implementation of these policies can be reflected on production model because the policies can directly change the value of Chemicals and Intensity index. The restriction on overproduction can reduce the country’s Intensity index value and African government’ s investment will increase the value of Chemicals for these countries. The amplitude of increase or decrease is associated with policy implementation effect.

One thing worth noting is that the increase or decrease is not limitless, we can’t put all emphasis on environmental protection fully ignoring the efficiency. 微信号：MATHmodels Here we set the average value of Intensity index and Chemicals from several most developed countries as a criterion. Take control for chemicals abuse as an example, the called “criterion”means that under this chemicals use level, the harm to the environment can be restored naturally, that is, it will not cause damage to the environment, and at the same time we can ensure that the food output will not be greatly reduced.

2.3 Equitable Distribution Model

The current food system which prioritizes efficiency and profitability also ignores the equity problem. A lot of people worldwide suffer from hunger, even though there is sufficient food produced to feed every people. Majority of them come from Low-Income Food-Deficit Countries (LIFDCs).These countries don’t have ability to produce enough food to raise local people because of their awful natural environment such as frequent drought or flooding and social environ- ment such as limited access to skilled workers and efficient production tools. From this point of view, the equity problem can’t be solved from production end but from distribution end. Therefore, we propose a Hand-in-Hand Initiative. Ac- cording to production model, we can acquire top ten countries with the highest food possession per capita. We assign these ten countries as donors. At the same time, we choose 18 the least developed countries from the UN report and these countries are receivers. How to determine which rich country to help which poor countries? We mainly think about the transportation cost. To minimize the trans- portation cost, we design a model to ensure the total distance between donors and their receivers is shortest.

2.3.1 Distance Minimization Model

We use Dijkstra algorithm below to find a few donated countries, so that the transportation cost between them to a donor country is minimum. 微信公众号：数学模型 Dijkstra algorithm

Input：Graph of transportation costs between n countries (V, E); Source country ; Target countries m.

Process：

• Let S = v, where v is the source country, and S is the set of target countries that have found the minimum transportation cost;

• Use D[i] to store the minimum transportation cost currently found from the source country to each country vi( ), and set the initial value of D [i] as:D[i] 微信号：MATHmodels ＝|v,vi| (Represents the transportation cost between two of countries);

• The country vj is selected so that D[j] = minyi ∈vs{D[i]}, and the country is incorporated into the set S;

• For all vertices vk in the set VS,if D[j] + |vj, Vk| < D[k] , the value of D[k] is modified as D[k] = D[j] + |vj, vk|;

• Repeat operation 2 and 3 for n-1 times.

Output：m target countries with the least transportation cost to the source countries.

2.3.2 The Determination of Donor Countries and Beneficiary

Countries

According to production model, we can figure out every country’s largest food production value. Considering the country’s population, we define food possession per capita:

Foodpossessionpercapita = thelargestfoodproodutionvalue/population

We determine the ten countries with highest food possession per capita as donor countries. And the result is shown in Figure 11.

微信公众号：数学模型 Figure 11 Figure 12

微信号：MATHmodels Figure 13

Figure 14

We also choose 18 least developed countries from UN report as beneficiary countries. The result is shown in Figure12.And all the countries’ geography lo- cation is shown in Figure13.

Based on above model, we finally determine the Hand-in-Hand initiative. The result is shown in Figure 14.

2.4 Growth Model

The above discussion does not consider the dimension of time. In the growth model, we define two indicators which can change with time. One is technology described by ASTI. The other is Labor which can change with future gradually rising population. Based on historical ASTI level data, we predict the future 微信公众号：数学模型 changes in ASTI level until 2100.And, according to the United Nations World Population Outlook, we predict the population growth until 2100.Until now, we can acquire a dynamic production model.

微信号：MATHmodels Figure 15 Figure 16

3 Model Application

After the stage of establishing model, we hope to apply specific countries into our model. To make the result more representative, we choose one developed country –USA and one least developed country –Nepal. For the USA, we collected the data of food output value of the planting, husbandry and fishery industry from 1993 to 2018 firstly. Then, the established production model is used to predict the output value of the three food production industries from 1993 to 2018, and compared with the actual value. The comparison results are as shown in Figure 17.

We can find that the predicted value of the output value of the husbandry is not stable, but the predicted value of two other industries is close to the actual output value of the industry. However, the model performance is quite well on the whole.

The same logic is applied in Nepal, and the comparison results are shown in Figure18. Similarly, we can also find that the neural model of the husbandry is not stable and the prediction error is large. But on the whole, the established production model still has good performance and is more practical.

微信公众号：数学模型 Figure 17 Figure 18

4 Analysis of the Optimized Food System

微信号：MATHmodels

4.1 Changes with the Implementation of the Optimized Food

System

Considering efficiency and profitability only, what needed is merely to max- imize the food production value in Production Model. However, in order to achieve sustainability, the use of chemical and the intensity of the Agriculture Production should be changed within a reasonable range which pursues to max- imize production but without bring negative impact on the environment. As for the equity, a help initiative need to be introduced.

Therefore, the optimized system mainly has the following changes com- pared to the current system.

4.1.1 Intensity of the Industry

To measure the intensity of agriculture production, we build Intensity Index which is an index varying from 1 to 10. Higher number means higher production intensity. We also define a Criterion Intensity V alue. If a country’s Intensity Indicator in Planting is higher than the standard value, it means this country have the problem of intensive farming, deviating from the goal of sustainability. The same meaning goes for Husbandry and Fisheries.

So in the optimized system, the Intensity Index of a country should ap- proach the criterion value gradually.

4.1.2 Use of the Chemicals

Following the same logic, we also define the Criterion V olume of Chemical Subsystem Planting Husbandry Fisheries Criterion Intensity V alue 6.0 4.7 5.3 微信公众号：数学模型 Use.It is an optimum level taking both production and environment into account. So in the optimized system, the V olumeofChemicalUse in a country should approach the standard value gradually.

Subsystem Planting Husbandry Fisheries Criterion Chemical Utilization Indicator 251.482 150.8892 75.4446

微信号：MATHmodels 4.1.3 the Formulation of Help Initiative

At the beginning, we have assumed that people in hunger generally come from Low-Income Food-Deficit Countries (LIFDCs). To promote equity issues, countries with food surplus should make donations to them. So the Help Initiative need be proposed to enable more people suffering huger have access to food. The initiative is designed based on the principle of minimizing transportation cost.

4.2 How Long It Can Be Implemented

The first aspect that we take into major consideration is sustainability. As we have mentioned before, improvement in sustainability can be achieved only in two ways (Curbing excessive production and Restricting Chemical Abuse), which requires the government’s action. So when the sustainability policy can be implemented depends on whether the government has a set of effective policy communication mechanism. The higher the government creditability, the shorter time it takes for sustainable policies to play the role.

And for equity, how long the redistribution of the food system can take effect is up to the negotiation process internationally because the achievement of this goal is determined by the donor countries’ positivity. Although there is the Hand- in-Hand Initiative proposed by FAO, the scale is still small with immature system. Making more countries actively embrace the initiative we put forward is the key point to accelerate the redistribution process.

4.3 Benefits and Costs

微信公众号：数学模型

4.3.1 The Change in Food Production

After implementing environment policy intervention, direct change is re- flected in food production. For countries with surplus food production such as USA, the food production will decrease slightly because of the control for over- production and chemical use. However, the policy effect is unclear, that means we can’t know the accurate change of chemicals use volume and production in- tensity. The Figure 19 shows the effect of different change combination of these two indicators on planting industry output value. (The figures for other two industries are ignored because of the limited space).The Figure 20 shows the output value change in three subindustries when both chemicals use volume 微信号：MATHmodels and production intensity decrease to the criterion value accurately.

Figure 19 Figure 20

For food-deficit countries such as Nepal, the output value will experience a slight increase because they have the access to chemicals. Different from the developed countries, there is no overproduction in developing countries. So the only factor affecting the output value is chemicals use volume. The Figure 21 shows the output value increases with the increasing percentage of chemicals use volume.

In Nepal, the chemicals use volume will reach the criterion value when the current amount increases by 120%. So according to the production model, we can know Nepal’s output value maximum is nearly 50 million dollars at current labor and technology level. The Figure 22 shows the output value increase in three subindustries when chemicals use volume reaches the criterion value accurately.

4.3.2 The Cost for Transportation

For the ten donor countries, it is costly to transport food to beneficiary coun- 微信公众号：数学模型 Figure 21 Figure 22

tries.

We have designed model to minimize the total distance between donors and beneficiary countries, thus minimizing transportation cost. We define the trans- portation cost equation for one country as following:

微信号：MATHmodels transportationcost = unitprice × distance ∗volume

Where unit price denotes dollars per kilometer distance and per kilogram food donation.

Food transport volume is an important factor that affects transportation costs. The more food donated, the higher the transportation cost. However, our produc- tion model can only calculate food output value not volume. Through analysis of the factors that influence donations of one country, we define Food Donations Function in a country, which has three independent variables: Value of Pro- duction, GDP growth and participation rate in International Aid Projects. (The logic is shown in Figure 23). The higher the country’s food production and the better its economic development, the more likely it is to donate more food. We can use growth model to predict one country’s future food output value. We can also analyze the macroeconomic cycle to predict the economic trend of a country. Participation rate in International Aid Projects can reflects one country’s attitude to donation issue. One country with high participation rate in International Aid Projects is more likely to donate more food. For simplicity, we set the indicator is constant over time.

Based on above analysis, to calculate the one donor’s transportation cost, we need to know the amount of donation food. Furthermore, to get the donation volume, we first need to obtain the country’s output value, which is one of factor affecting the donation volume.

Now we apply our thinking to calculate USA’s transportation cost. We get the USA’s food output value for every year by using growth model first and the result is shown in Figure 24. Then considering USA’ future food output value, analyzing future USA’s economic trend and referring USA historical participa- 微信公众号：数学模型 Figure 23

tion performance in International Aid Projects, we obtain the USA’ s donation 微信号：MATHmodels volume in the future. The result is shown in Figure25.

Figure 24 Figure 25

The beneficiary countries from USA is Haiti and Guatemala. The distance between USA and Haiti is 700 kilometers and the distance between USA and Guatemala is 1754 kilometers. The present donation volume of USA (shown in Figure) is 120500 tons according to the Food Donations Function.Consequently, according to distance and donation volume, we can calculate the total transporta- tion cost is 20.55 million dollars.

4.3.3 Environmental Damage Mitigation

a. The Control for Chemical Use The new food system requires reducing chemicals level to the “criterion level”for countries with chemicals abuse and increasing chemicals level to the “criterion level”for countries which have limited access to chemicals. As men- tioned earlier, the called “criterion”means that under this chemicals use level, the harm to the environment can be restored naturally, that is, it will not cause damage to the environment, and at the same time we can ensure that the food output will not be greatly reduced. In this sense, the new food system can alle- viate environmental damage in a large extent and the benefit mainly comes from 微信公众号：数学模型 chemicals-overusing countries.

Specifically, environmental damage mitigation can be reflected in three as- pects: air, water and land. The degree of environmental pollution caused by the use of chemicals in different industries (including agriculture, husbandry and fishery) is also different.

Air pollution is evaluated based on two aspects: contributions to global warming and emission of noxious gas.

3 ∑ Air = (w1ia + w2ia) ∗Chemicals i (1) i=1 微信号：MATHmodels Where Chemicalsi refers to the amount of reduced chemicals in different industry. w1ia and w2ia respectively being the coefficients describing chem- icals’ ability of emitting CO2 and noxious gas based on its chemistry element composition.

Water pollution focus on water contamination of both oceans and rivers. We mainly evaluate the contamination based on two aspects: inorganic contamina- tion and organic contamination.

3 ∑ (w1iw + w2iw) ∗Chemicals i Water = (2) i=1 Where w1iw refers to the coefficient describing chemicals’ inorganic water contamination such as acids, alkalis, oxidants, heavy metals and w2iw reveals the chemicals’ organic water contamination mainly including organic poison.

Land pollution similar to water pollution, is assessed by two factors: inor- ganic contamination and organic contamination.

3 ∑ (w1il + w2il) ∗Chemicals i Land = (3) i=1 Where w1il refers to the coefficient describing chemicals’ inorganic land contamination mainly including heavy metal pollution and radioactive element pollution and w2il refers to the coefficient describing chemicals’ organic land contamination such as pesticide.

Take USA as analysis object, the coefficients are shown in Table 3 and the

b. The Restriction for Overproduction Table 3

Industry W_{1ia} W_{2ia} W_{1il} W_{2il} W_{1iw} W_{2iw} Agriculture 1.2 0.35 0.13 0.09 0.075 0.053 微信公众号：数学模型 Husbandry 0.7 0.4 0.08 0.06 0.06 0.049 Fishery 0.21 0.3 0.009 0.003 0.19 0.11

微信号：MATHmodels Figure 26

Another requirement of the new system is to curb the phenomenon of over- production. Curbing overproduction may not have immediate effect on environ- ment, but the environment wellbeing is long and lasting. We have reasons to believe that the environment problem including degradation of land, deforesta- tion and the loss of vegetation, the loss of biodiversity will be mitigated in the future.

4.3.4 Inequity Issue Mitigation

Our food system proposes an initiative to solve the inequity problem. After the implementation of new food system, countries with deficit food production will have more access to food. Take Nepal as analysis object, one source is in- creased food production because of accessible chemicals, and the output value change after using more chemicals have been shown in Figure 21 and Figure 22. Another increased food source is the donations from Ukraine. When ana- lyzing the transportation cost, we have proposed Food Donation Function and using the function to predict USA’s every year’s donations. Because the calcu- lation is the same, here we do not calculate Ukraine’s donations any more.

5 Scalability and Adaptability

微信公众号：数学模型

5.1 Scalability

In order to discuss the scalability of the model, we randomly collected the food output data of another 20 countries that did not participate in the model training from 1993 to 2018, and divided these 20 countries into two groups ac- cording to their land area. The land area of one group was generally larger than that of the other group. Then, the established model is used to predict their re- spective food output value. Compared with the actual value, we can obtain the predicted error rate.

The predicted error rate can be calculated as following equation:

微信号：MATHmodels Predictederrorrate = (Predictedvalue −Actualvalue)/Actualvalue (4)

The average error rate of each group is taken as the error rate of the group. The results are shown in Figure 27：

Figure 27

It can be seen that the performance of the model is better in small area coun- tries. The main reason is probably that the data can describe the country’s unique characteristics better in small area, or say the accurate data is more difficult to ob- tain in large area country. Compared with small area country, countries with large area have multiple regional characteristics. For example, in planting production model, we take Climate and Topography as influence factors. However, for large area countries, they may cover more than one geographic characteristic.

The characteristic difference in inner country for large countries may be blamed for the bad model performance.

微信公众号：数学模型

5.2 Adaptability

In theory, the production model trained by lots of data can be used to calcu- late every country’s food output value and we have analyzed all countries food output value maximum before (the result is shown in Figure 10). On the whole, the model performance is good. So we can say our model has relatively strong adaptability.

6 Strengths and Weaknesses

微信号：MATHmodels

6.1 Strengths

a. The data used in our paper is the most accurate and latest from official website to guarantee the reliability of results. Also, we consider various factors trying to think about the problem comprehensively. So our results have high reference value.

b. Our model starts from both production end and distribution end and is established in the country level. We can obtain the level of Food Production before and after food system optimization and predict the future trend of food production. By applying model on specific countries, we illustrate the benefits and costs of food system optimization in detail.

c. The neural network model used in this paper itself has obvious advantage. It can approximate a continuous function of any complexity with any precision by only one hidden layer containing enough neurons. Compared with other linear models, the neural network model performance is more excellent.

6.2 Weaknesses

a. Some data is difficult to obtain probability causing sample error.

b. We set several assumptions so the whole model is a bit idealized.
