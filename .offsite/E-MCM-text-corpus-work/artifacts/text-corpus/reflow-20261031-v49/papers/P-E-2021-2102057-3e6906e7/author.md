MCM/ICM

Summary Sheet

Summary

In the past few years, food system considered the efﬁciency and proﬁtability as priorities and ignored the environmental sustainability and social equity. The resulted severe environmental damage and hunger problem are hanging over our heads and waiting to be solved.

In this paper, we incorporate the Environment and Equity factors together with Economic factor to build an Environment-Equity-Economy Model (EEE Model) to re-optimize the current food system. EEE Model consists of three interlocking sub- models. They are Environmental Sustainability Model, Equity of Food Distribution Model and Economy Beneﬁt-Cost Analysis Model. By factoring in some parameters, sustainability and equity are upgraded to priorities at the sacriﬁce of economic proﬁt.

The ﬁrst E : Environment Model involves three environmental indicators which are Greenhouse gas (GHG) emission and Eutrophying emission from food system and

Land use for food production. After examining massive data, we ﬁnd that transform- ing the national citizens’ diet composition will have signiﬁcant effect on reduction of the above three indicators. We use Logistic Model to predict the future situation and time coefﬁcient r is introduced to measure the time needed to achieve environmental sustainability. Animal product tax is used to drive this transformation.

The second E : Equity Model is based on the social uneven food distribution. Our concept is to reduce hunger ratio by slowing down the increasing rate of food inse- cure people. To achieve this goal, government can deliver the redundant food to the food scarcity region and offer them to the food insecure people. The assistance factor A is applied to mearsure the intensity of government assistance. As for the freight, government can charge Food Equity Tax from food producers and distributers.

The third E : Economy Model considers the net proﬁt of food producers and dis- tributers. In our re-optimized food system model, the economy net proﬁt is not just the difference between beneﬁt and cost. It need to include the animal porduct tax and food equity tax from ﬁrst E and second E model.

We choose China and Finland to be the target countries and employ our model in case studies. After simulation, we obtian the result that

• China will have 25.79% fewer GHG emission, 16.15% fewer eutrophication and 32.79% more spared land. Also in 2021, the hunger ratio will begin to reduce, and there’s no food insecure people by 2029. And the cost is 5.14% fewer net proﬁt for food production.

• Finland will have 33.22% fewer GHG emission, 32.03% fewer eutrophication and 26.98% more spared land. Also in the ﬁrst month after the plan is carried out, the hunger ratio will begin to reduce, and there’s no food insecure people by the middle of 2027. And the cost is 9.77% fewer net proﬁt for food production.

We also discuss the scalability and proﬁtability of our model, determine the strength and weakness of our model, explore the probability of future work.

关注数学模型

1 Introduction

1.1 Problem Background

微信公众号：数学模型 According to the FAO1, the nowaday food systems has yielded many positive results over the last few decades. How- ever, the highly-developed food system has also resulted in in- creasingly severe problems, including many highly processed, high-calorie and low nutritional value food items, high levels of food loss and waste, ecological footprint associated with cur- rent food system, and most importantly, the unreasonable food distribution of food[1], just like Figure 1 from website2.

Challenged by ICM, we decide to build a model to modify the food system by considering the balance among Environ-

Barrier Be- ment, Equity and Economic. tween Hungry People 微信号：MATHmodels And Waste Food

1.2 Problem Restatement

Having understood the problem, we’re required to do the following work:

R Develop a food system model to optimize the priority levels of efﬁciency, proﬁtabil- ity, sustainability and equity. Then compare the re-optimized food system with the current one and predict the time needed to achieve it.

R Find the beneﬁts and costs of the changes of the re-optimized food system and predict when they’ll happen.

R Tell the differences of our model between developed and developing countries, and employ the model to the actual situations.

R Make further exploration of the scalability and adaptability of our model when used in different regions with different sizes.

1.3 Our Approach

For convenience, we draw a ﬂow chart to represent our spproach.

We begin by establishing our modiﬁed food system model : Environment-Equity- Economy Model, we’ll adress it as EEE Model in the following paper for short. Our EEE Model try to obtain the balance among environmental sustainability, social equity and economic proﬁt. The model consists of three submodels, each stands for a “E”. We shall show the principles of them in the following paper.

Then we choose China and Finland as our target countries for case study, employ- ing our model into the countries. We ﬁnd that our model has huge progress on environ- mental recovery and social equity. At last, we discuss the scalability and adaptability of our model, make a sensitivity analysis, and describe the future work.

1Food and Agriculture Organization of the United Nations.

关注数学模型 2https://medium.com/@wayneroberts/so-you-think-food-security-is-a-problem-3676317701cc 微信公众号：数学模型

2 Assumptions

微信号：MATHmodels To simiplify the problem, we make the following basic assumptions, each of which is properly justiﬁed.

Assumptions 1 : We only consider calories and proteins as the basic diet need of one person. ,→Justiﬁcation : For food insecure people, calories provide the sufﬁcient energy and proteins maintain a healthy body. Thus they’re the most needed nutrition. By contrast, other nutrients like vitamins and microelement can be neglected.

Assumptions 2 : The price of the food is stable and constant. ,→Justiﬁcation : As the problem says, there’re enough food to feed everyone in the world, thus the supply is more than the demand, the food producers and distributers can’t change the price of the food, it’s stable.

Assumptions 3 : The greenhouse gas emission of food transportation can be ne- glected. ,→Justiﬁcation : According to the statistic on website Our World In Data, the green- house gas emission of food transportation is much smaller compared to the food pro- duction, thus we can ignore this part of emission.

Assumptions 4 : We will ignore the inﬂuence of the extreme events. ,→Justiﬁcation : The tendency of development will not change as we predict the de- velopment of our modiﬁed food system. The inﬂuence of the force majeure won’t be considered. We assume our target countries are regular and stable.

Assumptions 5 : Those factors we don’t mention have few inﬂuence on the system. ,→Justiﬁcation : In reality, factors that can affect food system are too plenty to be con- sidered. Thus, this assumption is reasonable and helps avoid unnecessary troubles when building the model.

关注数学模型 Assumptions 6 : The statistic we captured from website are precise and reliable. ,→Justiﬁcation : We collect most data from the authoritative websites, which we con- 微信公众号：数学模型 sider it trustworthy. Also, this is a premise under which our model is practical.

Other speciﬁc assumption, if necessary, will be mentioned and illustrated while we’re building models.

3 Notation

For convenience, we introduce some notations below.

Symbol Meaning 微信号：MATHmodels T Tax Rate on Animal Products

δ Population Growth Rate

N(t) Total Population

µ(t) Percentage of calories provided from Vegetal Food

λ(t) Percentage of proteins provided from Vegetal Food

x Daily Need for Proteins

y Daily Need for Calories

α, β Preference Weights on Vegetal and Animals Food

H(t) Food Insecure People in Current System

H∗(t) Food Insecure People in Modiﬁed System

A Assistance Factor

R(t) People who Receive Help from Government

GA(t) Government Assistance Investment

h(t) Hunger Ratio

m f ood Total Food Sale

pnet Net Proﬁt of One Unit Food

Wnet Total Net Proﬁts of Food System

Other speciﬁc notations, if necessary, will be mentioned and illustrated while we’re building models.

关注数学模型

4 Basic Idea of Environment-Equity-Economy Model

(EEE Model)

微信公众号：数学模型 The current food system considers efﬁciency and proﬁtability as priorities, which can be seen as economic factors. The producers have the goals of chasing the maxima of economic proﬁts, which ignores the environmental sustainability and social equity. As time goes by, the consequence tends to be more severe. The natural environment becomes worse, more people suffer from food scarcity, causing larger gap of wealth. To avoid the further deterioration in the future, we need to improve the current food system.

In short, the current food system ignores sustainability and equity and we need to make changes in seeking the balance among Environment, Equity and Economy.

To optimize the food system by considering efﬁciency, proﬁtability, sustainabil- ity and euqity, we establish our food system model : Environment-Equity-Economy Model, we shall call it EEE Model in the following paper for short. Our EEE Model is 微信号：MATHmodels combined of three submodels, including:

• First E : Environmental Sustainability Model To decrease the damage of the environment, we can transform the diet composi- tion by taxing on animal foods, then we will build a model based on this idea.

• Second E : Equity of Food Distribution Model To relieve the hunger problem of food insecure people, government could inter- vene by delivering redundant food to the people in need. The costs can be paid by food producers and distributers in the form of Food Equity Tax.

• Third E : Economy Beneﬁt-Cost Analysis Model We shall re-analyse the economy cost and beneﬁts because of the animal food tax and the food equity tax. We ﬁnd out that there’s economic proﬁts loss, which removes the priorities from efﬁciency and proﬁtability to make sustainable de- velopment.

5 First E : Environmental Sustainability Model

5.1 Selection of Indicators

According to the website Our World in Data[2] and inspired by the information given in the problem, the environmental impacts of food and agriculture are nega- tive in many aspects. For convenience, three major indicators are selected to measure the environmental sustainability of one country’s food system. They are respectively greenhouse gas emission from food system per year, eutrophying emission from food system per year, land use for food system.

• Greenhouse Gas (GHG) Emission Food is responsible for approximately 26% of global GHG emissions[2], causing global warming, glacier melting, and elevation of the sea level. Therefore, man-

agement and control of agricultural greenhouse gas emission by adjusting cur-关注数学模型 rent food system is key to emission reduction.CO2 is the most important green- house gas, but not the only one. According to Our World In Data[2], to include all GHG emissions from food system, we can therefore express them in kilograms of “carbon dioxide equivalents”, denote it as GHE. 微信公众号：数学模型 As we shall mention in the following subsection, production of animal food emits much more GHG than vegetal food. Thus one of the useful methods of decreas- ing level of GHG emission is to change the citizens’ diet composition.

• Eutrophication Emission (EUE)

Eutrophication is the pollution of water bodies and ecosystems due to excess nutrients[2]. Excess nitrogen and other nutrients from food production system run into the surrounding environment. Eutrophication of water severely harms the balance of freshwater ecosystem and has a detrimental effect on the supply of drinking water. Precautions must be taken to curb the further pollution of water resulted from food system. 微信号：MATHmodels Again, we can express the degree of eutrophication in the unit of grams of phos- phate equivalents, since phosphate is the most important contaminant for it.

• Land Use (LU)

Food system requires farmland and most farmland is made from forests. The expansion of agriculture has great impacts on the environment, causing sharp decline of forest area and biodiversity. What’s more, as more land is turned into farmland, plenty of species lost their habitat and this could damage biodiverrsity.

To prevent the biodiversity and our forests getting worse and worse, we can take actions by returning some farmlands back to the nature.

5.2 Adjustment of Food System

As the global population increases, more food must be produced to feed people. If nothing is done, what follows is more greenhouse gas emission and eutrophying emission from food system per year, further deforestation and loss of biodiversity.

After examining the data from Our World in Data[2], we notice that offering the same protein and calories, animal products generally emit more greenhouse gas, more eutrophic materials and occupy more land than vegetal products.

Thus, we can change the diet composition of national citizens by providing more vegetal products and less animal products, so as to achieve the environmental sustain- ability of food system.

Governmnet can be the driving force in this adjustment by taxing on the animal products. Denote the tax rate as T, T ∈[0, 1]. This will raise the economic cost for food producers, so they’ll produce less animal products and gradually the national citizens’ diet composition is changed.

关注数学模型

5.3 Establishment of Environmental Sustainability Model (First E)

5.3.1 Model of Transformation of Diet Composition

微信公众号：数学模型 Calories and proteins are chosen as the basic nutrition need of a person. Calories provide the sufﬁcient energy and proteins maintain a healthy body of one person. To simplify the problem, other nutrients like vitamin and trace elements are neglected.

Since there’re enough food for human, we assume the population of a country in year t is N(t) given by N(t) = N0(1 + δ)t (1)

where N0 is population in 2020, δ is the population growth rate, and we set t = 0 in 2020.

Assume one person consumes x kcal calories and y g proteins per day. Here we deﬁne µ(t) as the percentage of calories offered by vegetal products and λ(t) as the percentage of proteins offered by vegetal products.

微信号：MATHmodels Thus, the food production of the whole country per year must offers 365Nx kcal calories and 365Ny g proteins, among which 365µNx kcal calories and 365λNy g pro- teins are provided by vegetal products.

We can enlarge µ and λ to transform the national citizens’ diet composition to vegetal-preferred state. The transformation takes time to completely accomplish and is expected to take 30-50 years. The increasement of µ and λ with time t satisﬁes the Logistic Model.  ( ) dµ µ  1 − dt = rµ , µ(0) = µ0 µmax ( ) (2)  dλ λ 1 − dt = rλ , λ(0) = λ0 λmax

The solution is  µmax  µ(t) = ( µmax )  e−rt µ(0) −1 1+ (3) λmax  λ(t) = ( )  λmax e−rt λ(0) −1 1+

in these functions, µmax and λmax are ﬁnal value of µ and λ after complete transfor- mation, which we expect to achieve. The value of µmax and λmax are different depend on the national conditions of different countries. r is the time coefﬁcient which deter- mines how long it will take to achieve the total conversion of diet composition. Larger r translates to shorter time needed to achieve the transformation.

5.3.2 Introducing the Parameters

Part I : Parameters of Vegetal Products

To calculate the greenhouse gas and eutrophic materials emissions per year due to vegetal products and areas of land used to cultivate vegetal products, we introduce the following parameters:

GHEcal,veg: GHG emission per 1000 kcal calories provided by vegetal products, kg CO2 eq/1000kcal calories.

GHEpro,veg: GHG emission per 100g proteins provided by vegetal products,

关注数学模型 kg CO2 eq/100g calories.

EUEcal,veg: Eutrophying emission per 1000 kcal calories provided by vegetal prod- ucts, g PO4 eq/1000kcal EUEpro,veg: Eutrophying emission per 100g proteins provided by vegetal products, g PO4 eq/100g 微信公众号：数学模型 LUcal,veg: Land use required to produce 1000 kcal calories provided by vegetal products, m2/1000kcal calories

LUpro,veg: Land use required to produce 100g proteins provided by vegetal prod- ucts, m2/100g proteins

Consider that different countries prefer different vegetal and animal products. There- fore, parameters above will be speciﬁcally calculated in the case study based on the eating habit of the target country. Their general form is

n ∑ αi × GHEcal,i GHEcal,veg = (4) i=1 微信号：MATHmodels where n is the number of typical vegetal food, GHEcal,i is greenhouse gas emission per 1000 kcal calories provided by the i th vegetal food, αi is the weight of the i th veg- etal food (0 < αi < 1). Other parameters are calculated in the similar way.

Part II : Parameters of Animal Products

Animal products cause the similar effects to the environment, the only difference is the amount. Here, we introduce the parameters of environmental effects:

GHEcal,ani: GHG emission per 1000 kcal calories provided by animal products, kg CO2 eq/1000kcal calories.

GHEpro,ani: GHG emission per 100g proteins provided by animal products, kg CO2 eq/100g calories.

EUEcal,ani: Eutrophying emission per 1000 kcal calories provided by animal prod- ucts, g PO4 eq/1000kcal EUEpro,ani: Eutrophying emission per 100g proteins provided by animal products, g PO4 eq/100g LUcal,ani: Land use required to produce 1000 kcal calories provided by animal prod- ucts, m2/1000kcal calories

LUpro,ani: Land use required to produce 100g proteins provided by animal products, m2/100g proteins

Consider that different countries prefer different vegetal and animal products. There- fore, parameters above will be speciﬁcally calculated in the case study based on the eating habit of the target country. Their general form is

m ∑ βj × GHEcal,j GHEcal,ani = (5) j=1

where m is the number of typical animal food consumed by speciﬁc country citizens,

GHEcal,j is greenhouse gas emission per 1000 kcal calories provided by the j th animal关注数学模型 food, βj is the weight of the j th animal food (0 < βj < 1). And animal products provide 365(1 −µ)Nx kcal calories and 365(1 −λ)Ny g proteins per year.

微信公众号：数学模型

5.3.3 Effect of Changing Diet Composition

Since producing vegetal food emits less greenhouse gas, less eutrophic materials and occupy less land, as the proportion of vegetal food increases with time, environ- mental sustainability can be achieved through three signiﬁcant effects:

• Decrease of greenhouse gas emission from food system per year

• Reduction of eutrophying emission from food system per year

• Decline of land use for food system

Their functions with time are respectively 微信号：MATHmodels GHE(t) = 365µNx GHEcal,veg + 365λNy GHEpro,veg 1000 100 (6) + 365(1 −µ)Nx GHEcal,ani + 365(1 −λ)Ny GHEpro,ani 1000 100

EUE(t) = 365µNx EUEcal,veg + 365λNy EUEpro,veg 1000 100 (7) + 365(1 −µ)Nx EUEcal,ani + 365(1 −λ)Ny EUEpro,ani 1000 100

LU(t) = 365µNx LUcal,veg + 365λNy LUpro,veg 1000 100 (8) + 365(1 −µ)Nx LUcal,ani + 365(1 −λ)Ny LUpro,ani 1000 100

The total eutrophying emission EUE(t) and land use LU(t) can be calculated by changing the parameters of environmental factors. It will be shown in the following case study that three functions are decreasing with time after 2020 when national citi- zens’ diet composition starts to transform.

6 Second E : Equity of Food Distribution Model

6.1 Introduction

Since massive food producers and distributers prioritize efﬁciency and proﬁtability (Economic cost and beneﬁt), they have no responsibility for aiding hungry people, causing uneven food distribution and negative consequences, such as redundance of food in one place and famine in other place.

To achieve equity, government must take actions by delivering redundant food to the food insecure people. By doing this, we could save the wasted food and reduce the hunger ratio. What’s more, when the famine victim have enough to eat, they become

关注数学模型 healthy, indicating that they can work and produce more value to the society.

As for the freight of the food delivery, government can collect Food Equity Tax from the massive food producers and distributers. This may raise the economic cost but could bring beneﬁt to the equity.

微信公众号：数学模型

6.2 Food Equity Model

6.2.1 Current system

As we can see from above, the population N(t) is N(t) = N0(1 + δ)t (9) where N0 is the initial value of N(t), and δ is the population growth rate.

If we do nothing, the hunger ratio will stay constant, which means that the food insecure people population H(t) shall keep rising, causing the more severe social in- equality.

H′(t) N′(t) = H0 微信号：MATHmodels H(t) = H0(1 + δ)t, (10) N0 where N0 and H0 are the initial value of N(0) and H(0).

6.2.2 Modiﬁed system

To improve this situation, we need government to make interventions to deliver food. Our ultimate aim is to decrease the hunger ratio h(t) with time, we can express this goal by mathematical formulae. We denote the modiﬁed food insecure popula- tion function as H∗. To make the decreasement in hunger ratio, we can let the increas- ing rate of modiﬁed food insecure population smaller than that of population. That is H∗′(t) < N′(t) (11)

To be more speciﬁc, we can change (9) into an equation by denoting A as “Assis- tance Factor” to measure the degree of government assistance, larger A means larger intensity of government assistance and shorter time to decrease hunger ratio. There- fore we have an initial value problem.

H∗′(t) N′(t) = H0 −At, H∗(0) = H0 (12) N0

We solve this problem with MATLAB, and get the expression of H∗(t) ln (δ + 1) + A N0 (δ + 1)t A N0 H∗(t) = (H0 −A N0 t) (δ + 1)t − (13) ln (δ + 1)

which is the food insecure population in our modiﬁed system. Hence we can ﬁnd out the function of population who can receive assistance from government, denoted as R(t), that is R(t) = H(t) −H∗(t) ( ) ln (δ + 1) + A N0 (δ + 1)t A N0 (H0 −A N0 t) (δ + 1)t − = H0(δ + 1)t − ln (δ + 1) (14) ln (δ + 1) −A N0 (δ + 1)t A N0 = A N0 t (δ + 1)t +

关注数学模型 ln (δ + 1) According to the previous section, one person needs x kcal calories and y g proteins per day to guarantee health. And we denote Fcal and Fpro as the calories and proteins food delivery freight. Therefore the total expense of Government Assistance is

微信公众号：数学模型 GA(t) = R(t) × 365(xFcal + yFpro) (15)

This expense could be paid by massive food producers and distributers in the form of “Food Equity Tax”. Although this may reduce the economic proﬁt, this assistance contributes to the social equity.

7 Third E : Economy Beneﬁt-Cost Analysis Model

7.1 Economic Costs

We consider that there’re three main ecnomic cost in food system, including mate- 微信号：MATHmodels rial, land and labor. Then we assume that these three costs have linear relation with the amount of food production, and the slope is the price p of raw material, labor and land, therefore we have the following equations   k   m f ood,i × pmat,i Cmat = ∑     i=1  k m f ood,i × plabor,i Clabor = (16) ∑   i=1    k   m f ood,i × pland,i Cland = ∑  i=1

where m f ood,i and pi means the amount and the price of producing i th food, there’re k k kinds of foods in total. We add the sign because there’re different types of foods, ∑ i=1 k and the ∑ means we calculate the sum of all foods. The same signs in the passage are i=1 similar.

Thus we deﬁne the economic costs as

Economic Costs = Cmat + Clabor + Cland (17)

7.2 Economic Beneﬁts

In our modiﬁed food system, food producers and distributers are just sellers, we ignore their ﬁnancial activities, and as it’s mentioned in Assumption 2, the price of the food is stable, thus the economic beneﬁts is

k ∑ m f ood,i × p f ood,i Economic Bene f its = (18) i=1

where p f ood,i is the price of i th food.

关注数学模型

7.3 Proﬁts

Thus the economic proﬁts are

微信公众号：数学模型 W(t) = Economic Bene f its −Economic Costs k ∑ m f ood,i × (p f ood,i −pmat,i −plabor,i −pland,i) = (19) i=1 k ∑ m f ood,i × pnet,i = i=1

for convenience, we denote pnet as the combination of four prices and it can also be seen as the net proﬁt of one unit of food. Then m f ood is the amount of food sold to the customer per year, where customers are the people who are neither food insecure nor receiving assistance, that is

m f ood(t) = 365(x + y) × (N(t) −H(t)) (20) 微信号：MATHmodels Note that because of the environmental adjustment, government need to charge animal products taxes, with the tax rate T, and then together with the Food Equity Tax, we can obtain the net proﬁt of our modiﬁed food system, that is

Wnet(t) = Wtaxed(t) −GA(t) (21) = Wveg(t) + (1 −T)Wani(t) −GA(t)

8 Difference from Currnet System

After introducing the principles of our EEE model, we summarize our essential concept in this section. The biggest difference between our modiﬁed system and the current system is that we remove the priorities from the efﬁciency and proﬁtability by considering the environmental and social factors into our model and by tranform- ing the diet composition and taxing for food equity.

As we have mentioned before, after putting the statistics into the programme cal- culation, we obtain the results and list them :

• The greenhouse gas emission will decrease. (Beneﬁt)

• The degree of eutrophication shall reduce. (Beneﬁt)

• More land would be released back to the nature for recovery of biodiversity.

(Beneﬁt)

• More food insecure people will have food to eat and the hunger ratio will fall to zero. (Beneﬁt)

• The net economy proﬁt of food producers and distributers will decrease to a cer- tain limit. (Costs)

关注数学模型 Judging from the beneﬁts and costs that the beneﬁts are in the aspect of environ- mental sustainability and social equity, while the costs are economic. As we shall men- tion in the following case study that the amount of increasement of environmental and social factors. 微信公众号：数学模型 In the following case studies, we apply our formula of net proﬁt to analyse the food system of our target countries : China and Finland.

9 Case Study : China

We choose China to be our ﬁrst target country, China is a developing country with relatively large scale in population, economy and land area.

China has the largest food system in the world, which has to feed nearly one ﬁfth of the world population. During the last few decades, Chinese food system development considers efﬁciency and proﬁtability as their priorities, ignoring the environmental and 微信号：MATHmodels social adverse impact. Thus, China has severe environmental problems and hunger problems which need to be mitigated by adjusting the current food system.

In the following subsections, we use our model to improve Chinese food system. After the simulation of our model, we illustrate the beneﬁts and costs of our modiﬁca- tion.

9.1 Environmental Beneﬁt from First E

Considering that China has a huge population, the transformation of citizens diet composition takes relatively long time. We expect 30 years for the complete transfor- mation to achieve, with the corresponding time coefﬁcient r = 0.01. And our plan is that µ increase from 0.8 to 0.9, λ increase from 0.6 to 0.8. For Chinese, we choose rice and wheat as representative vegetal products; pig, poultry, beef, mutton and eggs as representative animal products. Their weights are listed at Table 2. Accroding to the website Our World In Data and our reasonable assumptions, we determine the follow- ing constants of Chinese food system in Table 2, including the preferrence of Chinese citizens’ diet, essential need for nutrition and so on.

Constant Value Weights Value

αrice Calories(kcal) x 2500 0.5

αwheat Protein(g) y 80 0.5

µ0 βpig 0.8 0.3

λ0 βpoultry 0.6 0.2

µmax βbee f 0.9 0.1

λmax βmutton 0.8 0.1

βegg Time Coefﬁcient r 0.1 0.3

关注数学模型 Using weights and environmental parameters (GHE, EUE, LU) of selected food from website Our World In Data, we calculate the parameters for vegetal animal prod- ucts, indicated in Figure 3.

微信公众号：数学模型 0 2 4 6 8 10 12 14 0 10 20 30 40 50 0 10 20 30 40 50 Figure (c) : Land Use(m2) (a) : GHG Emission (kg CO2 eq) (b) : Eutrophication (g PO4 eq) Green : Environmental Effects of Red : Environmental Effects of Vegetal Food Animal Food

Effects from Animal Food Supplying Calories Effects from Vegetal Food Supplying Calories Effects from Animal Food Supplying Proteins Effects from Vegetal Food Supplying Proteins 微信号：MATHmodels

It is obvious to see that all parameters for animal products are much larger than parameters for vegetal products. This means that offering the same amount of calo- ries and proteins, animals food cause more severe consequences than vegetals. Thus, it can be reasonably deduced that the transformation of diet composition will have signiﬁcant effect on the environmental protection.

We insert all parameters into function GHE(t), EUE(t), LU(t) and plot the result in Figure 4.

Figure (a) : GHG Emission Figure (b) : Eutrophication Figure (c) : Land Use

In ﬁgure (a) and (b), the blue dotted line represents the future situation when noth- ing is done, while the red full line means the future situation in our modiﬁed food system. In ﬁgure (c), blue line is the total area of farmland, and the red line is spared land.

From Figure 4, we can see that in our modiﬁed food system, GHE(t), EUE(t), LU(t) immediately declines due to adjustment. After 30 years in 2050, the future environ- ment has huge progress, we list our improvement quantitatively, including :

• Total GHG emission per year will decrease 25.79% in 2050.

• To slow down the rate of eutrophication, total amount of PO− 4 will reduce 16.15%

关注数学模型 in 2050.

• There’ll be 32.79% of land given back to the environment for recovering biodi- versity in 2050.

Judging from ﬁgures and our results, we can draw a conclusion that our modiﬁed 微信公众号：数学模型 food system is feasible in keeping environmental sustainability.

9.2 Food Delivery and Net Proﬁts from Second and Third E

According to the website Our World In Data, the hunger ratio of China is 1%. To improve this inequal situation, government can make inverventions by delivering the redundant food to the food insecure area. This may need investment as the freight of the food delivery, government can charge “Food Equity Tax” to the massive food producers and distributers.

Considering the Chinese national comprehensive power, we set the assistance fac- tor A = 0.01, and the “Animals Products Tax” T = 0.05, then put the numbers into MATLAB calculation, we obtain the R(t) population which government can assistance 微信号：MATHmodels and the Wnet(t) net proﬁt. We plot our result in Figure 5.

Figure (a) : Hunger Ratio Figure (b) : Net Profit

In ﬁgure (a), red line is the hunger population H∗(t), blue line is hunger ratio h(t).

In ﬁgure (b),the blue line represent the future proﬁt per year when nothing is done, while the red line means the future proﬁt in our modiﬁed food system, and cyan area is the loss of net proﬁt

As we can see from ﬁgure 5-(a), when government make interventions by delivery- ing food to the food insecure people, things are getting better, the hunger population start to decrease in 2021, and by 2029 there’s no food insecure people in China.

Such progress requires cost. When we apply our modiﬁed food system and simu- late the future net proﬁt, we ﬁnd that Wnet(t) shall decrease 5.14% per year. We con- sider that it’s reasonable sacriﬁce for sustainable development.

9.3 Conclusions for Chinese Food System

To summarize the effects of our re-optimizing food system, we list all the conse-

关注数学模型 quences in Table 3 Aspects Effects

Modiﬁcation Remove the priorities from efﬁciency and proﬁtability 微信公众号：数学模型 25.79%Fewer GHG emission in 2050 16.15%Fewer eutrophication in 2050 Beneﬁts 32.79%More spared land back to the nature in 2050 More people are fed and smaller hunger rate

5.14% Fewer economic proﬁt Costs

Implement Time Hunger ratio begin to reduce by 2021

Accomplish Time No food insecure people by 2029

To sum up, in our case study of Chinese food system, we sacriﬁce a part of economic 微信号：MATHmodels proﬁt, with the return of a better nature environment and a more equal country, we consider our model meets the criterion of sustainable development.

10 Case Study : Finland

We choose Finland to be our second target country, Finland is a developed country with relatively small scale in population, economy and land area.

Located in Northern Europe, Finland has highly-developed economy, and yet Finnish food system still exists some problems in environmental sustainability and social eq- uity, according to website Our World In Data, the current hunger rate of Finland is 2%, which is worse than China.

Thus in the following subsections,we’ll simulate our modiﬁed food system in Fin- land to see whether there’ll be some improvement in sustainability and equity.

10.1 Environmental Beneﬁt from First E

Consider that Finland has a relatively small population, the transformation of citi- zens diet composition takes a shorter time than China. Thus We expect 20 years for the complete transformation to achieve, with the corresponding time coefﬁcient r = 0.2. And our plan is that µ increase from 0.5 to 0.7, λ increase from 0.4 to 0.6.

For Finnish, we choose potato and wheat as representative vegetal products; pig, poultry, beef, ﬁsh and milk as representative animal products. Their weights are listed at Table 4

Accroding to the website Our World In Data and our reasonable assumption, we determine the following constant of Finnish food system in Table 4, including the pre- ferrence of Finnish citizens’ diet, essential need for nutrition and so on.

Using weights and environmental parameters (GHE, EUE, LU) of selected food from website Our World In Data, we calculate the parameters for vegetal animal prod-

ucts, indicated in Figure 6. 关注数学模型 Constant Value Weights Value

αpotato Calories(kcal) x 3000 0.7 微信公众号：数学模型 αwheat Protein(g) y 110 0.3

µ0 βpig 0.5 0.1

λ0 βpoultry 0.4 0.1

µmax β f ish 0.7 0.3

λmax βbee f 0.6 0.3

βmilk Time Coefﬁcient r 0.2 0.2

微信号：MATHmodels 0 5 10 15 20 25 0 20 40 60 80 100 0 10 20 30 40 50 60 70 Figure (c) : Land Use(m2) (a) : GHG Emission (kg CO2 eq) (b) : Eutrophication (g PO4 eq) Blue : Environmental Effects of Yellow : Environmental Effects of Vegetal Food Animal Food

Effects from Animal Food Supplying Calories Effects from Vegetal Food Supplying Calories Effects from Animal Food Supplying Proteins Effects from Vegetal Food Supplying Proteins

It is obvious to see that all parameters for animal products are much larger than pa- rameters for vegetal products. We insert all parameters into function GHE(t), EUE(t), LU(t) and plot the result in Figure 7.

In ﬁgure (a) and (b), the blue dotted line represent the future situation when noth- ing is done, while the red full line means the future situation in our modiﬁed situation. In ﬁgure (c), blue line is the total area of farmland, and the red line is spared land.

From Figure 7, we can see that in our modiﬁed food system, GHE(t), EUE(t), LU(t) immediately declines due to adjustment. After 20 years in 2040, the future environ- ment has huge progress, we list our improvement quantitatively, including :

• Total GHG emission per year will decrease 33.22% in 2040.

• To slow down the rate of eutrophication, amount of PO− 4 will reduce 32.03% in 2040.

• There’ll be 26.98% of land given back to the environment for recovering biodi- versity in 2040.

关注数学模型 微信公众号：数学模型 Figure (a) : GHG Emission Figure (b) : Eutrophication Figure (c) : Land Use

10.2 Food Delivery and Net Proﬁts from Second and Third E

According to the website Our World In Data, the hunger ratio of Finland is 2%. To 微信号：MATHmodels improve this inequal situation, government can make inverventions by delivering the redundant food to the food insecure area. This may need investment as the freight of the food delivery, government can charge “Food Equity Tax” to the massive food producers and distributers.

Considering the Finnish national comprehensive power, we set the assistance factor A = 0.2, then put the numbers into MATLAB calculation, we obtain the R(t) popula- tion which government can assistance and the Wnet(t) net proﬁt. We plot our result in

According to the website Our World In Data, the hunger ratio of Finland is 2%. To improve this inequal situation, government can make inverventions by delivering the redundant food to the food insecure area. This may need investment as the freight of the food delivery, government can charge “Food Equity Tax” to the massive food producers and distributers.

Considering the Finnish national comprehensive power, we set the assistance factor A = 0.2, and the “Animals Products Tax” T = 0.1, then put the numbers into MATLAB calculation, we obtain the R(t) population which government can assistance and the Wnet(t) net proﬁt. We plot our result in Figure 8.

Figure (a) : Hunger Ratio Figure (b) : Net Profit

关注数学模型 In ﬁgure (a), red line is the hunger population H∗(t), blue line is hunger ratio h(t). In ﬁgure (b),the blue line represent the future situation when nothing is done, while the red line means the future situation in our modiﬁed situation, and cyan area is the decreasement of net proﬁt 微信公众号：数学模型 As we can see from ﬁgure 8-(a), when government make interventions by delivery- ing food to the food insecure people, things are getting better, the hunger population start to decrease within one month, and by the middle of 2027 there’s no food insecure people in Finland.

Such progress requires investment, when we apply our modiﬁed food system and simulate the future net proﬁt, we ﬁnd that Wnet(t) shall decrease 9.77% per year, we consider that it’s reasonable sacriﬁce for sustainable development.

10.3 Conclusions for Finnish Food System

To summarize the effects of our re-optimizing food system, we list all the conse- 微信号：MATHmodels quences in Table 5

Aspects Effects

Modiﬁcation Remove the priorities from efﬁciency and proﬁtability

33.22% Fewer GHG emission in 2040 32.05% Fewer eutrophication in 2040 Beneﬁts 26.98% More spared land back to the nature in 2040 More people are fed and smaller hunger rate

9.77% Fewer economic proﬁt Costs

Implement Time Hunger ratio begin to reduce by one month after carried out

Accomplish Time No food insecure people by the middle of 2027

To sum up, in our case study of Finnish food system, we sacriﬁce a part of economic proﬁt, with the return of a better nature environment and a more equal country, we consider our model meets the criterion of sustainable development.

11 Discussion

11.1 Difference In Developed and Developing Countries

• Beneﬁts difference:

In developed countries, because they prefer animal food initially, changing the priorities of the food systems contributes to a higher decrement in greenhouse gas emission and eutrophying emission than developing countries. In addition, with highly-developed economy in developed countries, they have bigger assis- tance factor, so that the food insecure population will be cut down to zero more

关注数学模型 fast than developing countries.

• Costs difference:

For the reason of higher animal product tax in developed countries, their proﬁt has a higher decrement than developing countries.

微信公众号：数学模型

11.2 Scalability

Our ﬁrst target country China, has the largest population on the world (1.4billion), which means it has the largest food system in the world. Our second target coun- try Finland, has 5.5million population, which means the food system of Finland is 250 times smaller than Chinese food system.

To sum up, our model predicts and simulate well on both countries, which indicates that our modiﬁed food system model works well on both large and small system and behave well in scalability

However, our model mainly focus on the food system of one single country. There- fore, our model is limited in the food system much smaller than country like villages, 微信号：MATHmodels as well as food system much larger than country like continents or even the whole world. To make the model more adaptable, we can adjust model to be suitable for some much larger places like a continent and some much smaller place like a village.

11.3 Adaptability

Consider that people in some extremely poor regions almost dont consume animal products, the environmental aspect of our model cant work well on these regions. But also because of that, the environmental pollution from food system of these regions, which mainly produce vegetal products, is relatively small. These food systems can naturally satisfy the environmental sustainability.

In some highly developed countries, like Norway, Singapore, Sweden Luxembourg and so on, there are few hungry people and their government has sufﬁcient funding for these hungry people. The assistance expenses need not paid by food producers in the form of tax. So equity model may not work well on these hilghly developed regions.

To sum up, our model has relatively good adaptability in most regions but limited to some extremely poor and extremely rich area.

11.4 Sensitivity Analysis

We change the weights of speciﬁc foods in vegetal food and animal food, i.e. αi and βj. The following changes of environmental parameters for vegetal and animal food, i.e. GHEcal,veg, GHEcal,ani and so on, are slight.

We plot of our result of sensitivity analysis of cases in China and Finland. As we can see from the Figure 9 and Figure 10,the overall tendency of the curve of GHE(t), EUE(t) and LU(t) stays stable, which suggests the robustness of our model.

关注数学模型 微信公众号：数学模型

微信号：MATHmodels

12 Strengths and Weaknesses

12.1 Strengths

P Our sensitivity analyses show that our models are fairly robust to changes in pa- rameter value.

P The results of our models also agrees with common sense and experience.

P We consider various indicators in environmental and social aspects, making our model conprehensive and objective.

P After simulation, we ﬁnd that our model has signiﬁcant progress on four indica- tors(GHG eimission, eutrophication, land use, hunger rario), indicating that our model is effective.

P Our model works well on both large and small food systems, which means that our model is adaptable.

12.2 Weaknesses

C Some of the parameters are baesd on semi-educated guess because there’re some data are unavaliable.

C We only consider the calories and proteins as the main nutritions, other nutrition like vitamin and microelements aren’t considered.

关注数学模型 C As we’ve mentioned before that in extremely poor countries, people has severe lack of animal food, transformation of diet composition doesn’t work well. Thus it’s the limitation of our model.

微信公众号：数学模型 C The beneﬁt of our model won’t last forever, it’ll decrease as the rise of population, therefore our model may need upgrade for long-trem development. The most essential method is to restrict the excessive population growth.

12.3 Future Work

We notice from the case study that the effect of transformation of diet composition can last for decades, but can’t last forever due to the increasing of population. It is hard to produce more food while not causing elevation of emissions of greenhouse gas and eutrophic materials, as well as further land reclamation. Therefore, more work has to be done to deal with the future problem.

There are several practical plans. One of them is improving the pattern of agri- 微信号：MATHmodels cultural production and adopting environmentally friendly way. Soilless culture, for instance, has the advantage of producing more food of higher quality, with less use of water, fertilizer and labor. However, because of the higher investment and stricter production management, soilless culture can’t be widely extended. But we believe that with the development of agricultural technology, these environmentally friendly but economically unfriendly agricultural production pattern will one day be globally extended, which helps to build a more productive and sustainable food system.

关注数学模型
