MCM/ICM

Summary Sheet

Summary

The current food system is unstable. Many food insecurity problems occur because of neglecting of equity, sustainability and resilience. In order to obtain a robust food system, we conduct a comprehensive examination of the current system and optimize it.

We develop an activities-outcomes-goals food system to make the system more robust and comprehensive. The new food system is divided into food system activities (FSA), food system outcome index (FOI), and food system goals index (FGI). Goals are used to optimize food system outcomes. Through the entropy weight method (EWM) and the coefficient of variation method (CVM), specific indicators are incorporated into FOI and FGI. We first im- prove the resilience of the food system, and on this basis solve the following problems.

⚫ We determine the optimization of specific indicators in FOI by adjusting the level of

equity and sustainability in FGI. Compared with the current system, the optimized system reduces the environmental footprint and makes food distribution more equi- table. According to the estimates of the intervention plans, the new food system will take a long time to implement.

⚫ We made environment security in the food system a priority. The direct and indirect effects of reduced arable land are counted as costs, while the improvement in ecosys- tem services is counted as benefits. Cost-benefit models are used in developed and developing countries to analyze their food systems. We find that the two curves of cost and benefit over time intersect earlier in developed countries than in developing ones. In other words, developed countries can benefit more quickly from making eco- logical security a priority in their food systems.

⚫ We apply the model to Japan and India. We apply the model to Japan and India to analyze the costs and benefits needed to improve equity and sustainability in ecolog- ical services. The original ecosystem services scores for Japan and India are 68.5384 and 23.8331, respectively. After investing the same cost, scores are 75.392 and 26.213, respectively. The grey prediction model optimized by particle swarm optimization algorithm predicts that the time for Japan and India to reach the optimization goal is 2036 and 2040 respectively.

⚫ We discuss the different situations of larger and smaller food systems, and then apply our model to Yemen, a country with extreme food insecurity. By appropriately mod- ifying our indicators and weights, our model has good scalability and adaptability.

The optimization of the food system needs to be driven by specific interventions, thus we propose intervention plans in terms of equity, sustainability and resilience.

关注数学模型

1 Introduction

1.1 Problem Background

微信公众号：数学模型 There are many definitions of the food system in previous studies. The World Food Pro- gramme defines the food system as the networks that are needed to produce and transform food and ensures it reaches consumers[1]. If you simply define the food system in this way, thus it is not comprehensive because it ignores the impact of environmental, social, economic and other factors. We redefine the food system as: the interaction between biogeophysics and the human environment and within it determines a series of activities in the food system from production to consumption, and the results of these activities[2].

Food security is the main result of the food system. The 2007 International Conference on Organic Agriculture and Food Security proposed that the multi-dimensional nature of food se- curity includes food availability, access, stability and utilization. [3].

There are many loopholes in the current food system, because it mainly considers effi- 微信号：MATHmodels ciency and profit. Food scarcity and abuse of the environment are problems that need to be solved urgently in the current system. Therefore, we need to think more about equity, sustain- ability and resilience in the food system.

1.2 Our Work

We develop a new food system model, which optimizing the current model by re-imagin- ing and re-prioritizing. Then, we apply the established model to various countries so as to verify the accuracy of the model and propose amendments to improve it.

We need the following work to solve the problem:

⚫ State assumptions and make notations. In order to better establish models and analysis, we simplified some of the secondary factors and narrowed the core of our food system and optimization direction. Then, we will list some symbols, which are very important for us to clarify the model and determine its definition.

⚫ Develop a new food system. Food system is optimized in the direction of equity and sustainability. Compare it with the previous food system. We estimate the time that the new food system implements.

⚫ Calculate the costs and benefits required to optimize the food system. Differences are analyzed in costs and benefits between developed and developing countries. We apply it to specific countries to predict when the net benefit will occur.

⚫ Verify the scalability and adaptability of the model. Models are used in countries of different sizes and states to validate and analyze food systems.

⚫ Sensitivity analysis and model evaluation. We evaluate the reliability of the model through sensitivity analysis. Then, we will discuss the strengths and weaknesses of the model.

The entire modeling process is as follows:

关注数学模型 Analysis problem Basic model Method Model/Methed VCM EWM 微信公众号：数学模型 T=max{Ti} Social EWM economy

Food system Five Specific Calculate the FOI activities indicators(Ⅱ) target time

TASK Environ 1 ment Sustainability Profitability Optimal target Get Efficiency Resilience Equity Problem PSO- Solve GM(1,1) problem TASK TASK TASK 4 3 2

Model Finding Jpan&India Costs&Benefits Finding adjustment is supported are selected Analysis 微信号：MATHmodels The model for Problem food system solved

Figure.1 The flow chart of our work

2 Assumptions and Justifications

In order to simplify the given problem and modify it to be more suitable for simulating real life conditions, we make the following basic assumptions. ⚫ Assumption: The data we collect from the online database are accurate, broad and con- sistent.

Justification: Since our data sources are all websites of international organizations, we can reasonably assume the high quality of their data. For some indicators of missing data, other available data can be used instead. Because all aspects of the food system are not only reflected by a certain indicator. It can be the result of many factors working together.

⚫ Assumption: Environmental and socio-economic driving factors can be analyzed from the

perspective of considering the results of food system activities.

Justification: Although the model is simplified, environmental and socio-economic fac- tors are still taken into consideration when evaluating the food system. At the same time, the influence of environmental and socio-economic factors as driving factors will be re- flected in other results. ⚫ Assumption: When analyzing the world, the country is balanced. In the analysis of spe- cific countries, it is not balanced internally.

Justification: If we think of the world as a large food system, thus we can assume that countries are balanced, which simplifies the calculation. And, on a global scale, different countries are uneven, and equity still needs to be considered. ⚫ Assumption: The costs and benefits of analyzing the optimization of the food system can be partially obtained by calculating ecosystem services.

关注数学模型 ⚫ Justification: The ecological damage caused by the food system is mainly concentrated in the link of production. Therefore, the cost consumption and benefit acquisition generated by optimizing the food system are mainly reflected in production.

微信公众号：数学模型

3 Notations

The key mathematical notations used in this paper are listed in Table 1.

Symbol

Description FSA Food system activities model FOI Food system outcomes index FGI Food system goals index PoMS Prevalence of moderate or severe food insecurity in the population IDA IDA resource allocation index 微信号：MATHmodels CPI Corruption perception index IDEA Freedom of religion Index PoU Prevalence of undernourishment PoPD Percentage of population using safely managed drinking water sources PoPS Percentage of population using safely managed sanitation services

4 Food System Model

We have re-established a new food system model, based on a comprehensive examination of the current food system model. The new food system model includes the interactions be- tween biogeophysics and the human environment, activities and the outcomes of activities.

4.1 Food System Activities

The activities of the food system include the production, processing, distribution, con- sumption and waste of food. The following picture shows the flow chart of the activities of the food system.

Figure.2 Food system activities

4.1.1 Production

The production of food includes all activities involving the production of food raw mate-

关注数学模型 rials. This process includes access to land and labor, raising animals, growing crops or acquir- ing populations of young animals, caring for growing food materials, and then harvesting or slaughtering. These activities are determined by a variety of factors, from climatic conditions to land tenure, input prices, agricultural technologies and government subsidy provisions aimed 微信公众号：数学模型 at protecting or promoting production.

4.1.2 Processing

Processing food includes the various transformations that raw materials undergo before being sent to retail markets for sale. All these activities add value to raw materials in an eco- nomic sense, but these activities may also significantly change the appearance, storage period, nutritional value and content of raw materials. The determinants of these activities are quite different from the determinants of food production.

4.1.3 Distribution and Retail

The distribution and retail of food includes all the activities involved in moving food from one place to another and conducting marketing. Distribution is largely affected by transporta- tion infrastructure, trade regulations, government transfer plans and storage requirements. Re- 微信号：MATHmodels tailing is influenced by how markets are organized and where they are located, advertising, and any niche or premium category the product may fit in to.

4.1.4 Consumption

Consuming food involves everything from deciding what to choose to preparing, eating, and digesting food. Prices are influential, as are income levels, cultural traditions or preferences, social values, education, and health. With the globalization of the diet and the globalization of the food system, the structure of advertising and the food supply chain also has a great impact on people's dietary choices.

4.1.5 Waste

Wasting food refers to food that is not digested except inedible, existing in all parts of the food system activity. Such as deterioration due to poor transportation and harvesting methods or rot in the trash bins of consumers and retailers. About one-third of food is wasted every year.

4.2 Food System Outcomes Index

The evaluation of food system results is an important part of the overall inspection and re- establishment of the food system. Food system results mainly consider food security, which includes three aspects: food availability, food access and food utilization.

At the same time, the results of the food system also include environmental and socio- economic drivers, and in the whole food system, it will have environmental and socio-eco- nomic results. Therefore, when we analyze the environmental and socio-economic factors of the food system, we consider the results of the food system, and then re-determine the propor- tion of each part by determining the optimization direction, so as to consider the interaction between the various parts of the food system.

Thus, an evaluation system consisting of food availability, food access, food utilization, environmental security and socio-economic welfare is established. Figure.3 shows the specific components of the evaluation system.

关注数学模型 微信公众号：数学模型 微信号：MATHmodels Figure.3 Food system outcomes

4.2.1 Food Availability

Food availability refers to the quantity, type and quality of food available for consumption per unit. It mainly includes three parts, the production, distribution and exchange of food.

(1) Production Production refers to how much and what type of food is available through local production. We determine food production by considering the area of land in agriculture and the number of agricultural workers in a region, combined with the food production index[5].

(2) Distribution Food distribution refers to how food for consumption is physically transferred to available, in what form, when and to whom. We consider food distribution by considering the proportion of transport services in the national import and export services[6][7].

(3) Exchange Food exchange means that the amount of food available to a unit is obtained through ex- change mechanisms such as barter, trade, purchase, or loan, rather than through local produc- tion. We determine the food exchange by considering the share of food imports and exports in the country’s commodities[8].

4.2.2 Food Access

Access to food refers to the ability and channel of a unit to obtain the type, quality and quantity of the food it needs. It mainly includes food affordability, distribution, and preference.

(1) Affordability Food burden refers to the purchasing power of a family or community relative to food prices. Different from other indicators, we can determine the prevalence of moderate or se- vere food insecurity in the population[9]. Many people are food insecure because they cannot

关注数学模型 afford food.

(2) Allocation Food allocation refers to the mechanisms governing when, where, and how food can be accessed by consumers. The difference from distribution is that it is often related to policy and 微信公众号：数学模型 society. We determine it through the IDA resource allocation index and corruption percep- tion Index[10].

(3) Preference Food preferences affect the social or cultural norms and values that consumers demand for specific types of food. It can be partially considered through the Freedom of religion Index (IDEA).

4.2.3 Food Utilization

Food utilization is mainly considered from two aspects, one is nutritional index and the other is food safety.

(1) Nutritional value 微信号：MATHmodels Nutritional value refers to how much of the daily requirements of calories, vitamins, pro- tein, and micronutrients are provided by the food consumed. It can be determined by the prev- alence of undernourishment in the population.

(2) Food safety Food safety includes the dangers of adding chemicals during production, processing and packaging, as well as food-borne diseases such as Salmonella and CJD. It can be determined by the percentage of the population using a safely managed drinking water source and the percentage of the population using a safely managed sanitation service.

4.2.4 Environmental security

The food system leaves a huge environmental footprint. Although the environment will act as a driving factor to influence the food system, it is more convenient to analyze as a result. We select the following three factors as indicators of environmental security.

(1) Fresh water The growth of crops is inseparable from water resources, and most of the crops are rela- tively high in water-rich areas. Although some crops can grow well in arid environments, water resources can still play a role in promoting growth.

(2) Forest area No crops grow independently, they can grow better in a diversified environment. Forest is the best diversified growth environment, so forest area can also reflect the quality of the food system to some extent.

(3) Carbon dioxide emissions Carbon dioxide is the main raw material for photosynthesis of plants. In an environment with high carbon dioxide concentration, it is helpful for photosynthesis of plants, so carbon dioxide emissions can also be used to evaluate food systems.

关注数学模型

4.2.5 Socioeconomic welfare

In a country or region with good social welfare, people have enough wealth to obtain food. Therefore, social welfare can also be used as an important indicator to evaluate the food system. We select the following two factors as indicators for evaluating socioeconomic welfare. 微信公众号：数学模型 (1) Gross Domestic Production(GDP) The GDP of a country can reflect the overall economic status of the country, and the eco- nomic status of a country will affect its social welfare. So GDP can be used to analyze the country’s Socioeconomic welfare.

(2) Employment to population ratio This indicator can reflect the per capita working status. If the social welfare in a region is better, then the per capita working status will also be better. Therefore, Employment to popu- lation ratio can reversely reflect the socioeconomic welfare status of a region.

4.3 Weights of indicators

微信号：MATHmodels

4.3.1 Entropy weight method

Entropy weight method is an objective weighting method, which is based on the principle that the smaller the variation degree of the index is, the less information it reflects, so the weight value of the index should be lower. Thus, we use it to determine the weight of the indicators. The calculation process is as follows：

Step1 Data normalization:

Step2 Calculate the proportion of the sample of the index:

Step3 Get the entropy weight of each index according to the following formula：

Step4 Calculate the sample’s score:

Subsequently, the weights of five comprehensive evaluation indicators can be calculated by the entropy weight method: food availability, access, utilization, environmental safety and social economic welfare. Based on these calculated weights, we have:

关注数学模型 (1) 微信公众号：数学模型 4.3.2 coefficient of variation method The basic idea of CVM is: in the multi-indicator comprehensive evaluation, if an indicator has a large degree of variation in the observed values of all the evaluated objects, indicates that it is difficult for the indicator to reach the average level when executed by the evaluation com- pany, which would make it possible to clearly distinguish the competence of each evaluation object in the specific area, then the weights of indicators should be given greater. On the con- trary, a smaller weight should be given.

Step1 Cost-type index is transformed into benefit-type index: 微信号：MATHmodels Step2 Data standardization：

Step3 Calculate the mean and standard deviation of each indicator：

Step4 The variation coefficient and weight of each indicator are calculated:

Step5 Calculate the total score of each evaluation object:

Subsequently, the food system outcomes index can be calculated by the coefficient of variation method as follows:

(2) The calculated weight index results are as follows:

关注数学模型 Table.2 Index weights for food system outcomes Indicator(Ⅰ) Indicators(Ⅱ) Weights Indicators(Ⅲ) Weights Agriculture land 0.2916 Agriculture 微信公众号：数学模型 Availability 0.2706 0.1549 workers (Ava) Food production 0.4378 Index PoMS 0.0987 CPI 0.3621 Access 0.2316 (Acc) IDEA 0.2398 IDA 0.2994 PoPD 0.3461 Utilization Food system 0.1134 PoU 0.4783 (Uti) Outcome PPU 0.1756 微信号：MATHmodels Biodiversity 0.2189 Environmental Fresh water 0.1932 Security 0.2467 Forest coverage 0.3097 (Ens) CO2 emissions 0.2782 Income 0.2341 Employment 0.5213 Soc-economic wel- fare 0.2534 Wealth 0.1123 (Sef) Human capital 0.1323 Index

4.4 Model verification

Figure.4 2019 Global hungry index

关注数学模型 strength and weakness of each country's food system.

We used the weights and data from the World Bank to calculate the combined index score for each country. We also visualized the FOI, which was obtained in Figure 5. We converted 微信公众号：数学模型 the FOI into a value between 1 and 100, and the higher the value, the better the food system.

微信号：MATHmodels Figure.5 FOI of each country By comparing the two maps, we can see that although there are differences, they are within acceptable limits. In the FIO visualization, for example, Brazil scores at a higher level than it does in the Hunger Index visualization. This is because our model takes the index of ecological security into consideration and occupies a relatively large proportion. Brazil, on the other hand, has had a poor environmental performance in recent years and therefore scores badly in our model.To sum up, our model can reflect the real situation and has good practicability.

4.5 Food system goals index

To ensure the stability of the model we built，we plan to propose optimization objectives for our model from the aspects of resilience, efficiency, profitability , sustainability and equity.

4.5.1 Resilience

Sudden disturbances are common in the food systems, thus we find resilience to measure the food system's ability to resist disturbances. According to D.M. Tendall et al, food system resilience can be defined as follows: capacity over time of a food system and its units at mul- tiple levels, to provide sufficient, appropriate and accessible food to all, in the face of various and even unforeseen disturbances[11].

A food system’s resilience can be broken down into various components:

(1) robustness, or the capacity to withstand the disturbance in the first place before any food security lost;

关注数学模型 (2) redundancy, or the extent to which elements of the system are replaceable, affecting the capacity to absorb the perturbing effect of the disturbance and avoid as much food insecu- rity as possible;

(3) the flexibility and thus rapidity with which the food system is able to recover any lost 微信公众号：数学模型 food security;

(4) resourcefulness and adaptability, which determines just how much of the lost food security is recovered. Together, these capacities form the basis of the food system resilience action cycle.

Applying the concept of resilience to our model, we select four indicators from our pri- mary model to measure the four parts of the resilience respectively. The four indicators are Frequency of extreme events(FE), Food diversity(FD), Wealth level(WL), Governmental effi- ciency(GE). The Figure.6 below shows the impact of varying resilience on the food system over time.

微信号：MATHmodels Figure.6 Resilience of food system Also, We construct a formula to measure the resilience of a food system based on the four indicators selected above:

(3) Where, are the coefficients of the variables. They represent the extent to which the four components contribute to resilience.

4.5.2 Profitability

To make it more convenient to calculate the profitability of the food system, we narrowly understand the food system as only including production, processing&packaging, distribu- tion&retail and consumption. Then we select several economy-related indicators from the model established in Task 1 to construct the profitability formula. The indicators we selected include: Local prices(LP), Labor costs(LC), Transportation facilities(TF), Advertising(AD), agriculture land(AL). The profitability of sell food per unit is given by the following formula:

(4)

Where, represent transportation costs per mile, production per unit of agricul- tural land, profit changes caused by emergencies respectively.

4.5.3 Efficiency

Similar to the above, when considering the efficiency of the food system, we ignore the

关注数学模型 influence of environmental factors and only pay attention to the process of the food system in a narrow sense. So the indicators that we pick for calculating efficiency are: Transportation facilities(TF) and Pattern of payment(PP), in which distribution process and consumption are considered respectively. Thus, the formula of calculating efficiency is obtained: 微信公众号：数学模型 (5) Where, represents efficiency caused by emergencies. PP=0.5 when the pattern of payment is cash payment , PP=1 when the pattern of payment is e-payment.

4.5.4 Equity

In some areas where the food system is well developed, there are still many food insecure people. Therefore, it is one-sided to evaluate a food system only from profit and efficiency. In order to optimize the model we built in Task 1, we used equity as the optimization objective. More specifically, we selected several indicators related to improving equity from the model established by Task 1 to construct the equity index of the food system. In terms of food distri- bution, transportation is an important factor in ensuring equity. Areas with better transport fa- 微信号：MATHmodels cilities tend to take better care of the poor because food is easier to get to. Government policies often are designed to correct market failures by allocating food to remote areas or at lower prices, so the role of government cannot be ignored. In addition, Gender equity(GE) and In- come equity(IE) should be also considered. Therefore, we construct the following formula to evaluate the Equity index(EI) of the food system:

(6) Where, are the coefficients of the variables. CPI represents the Corruption Perception Index, which can reflect the possibility that the government will make the right decision. And the smaller CPI is , the more likely the government is to make the right decision.

4.5.5 Sustainability

According to Maleksaedi and Karami, sustainability is defined as the capacity to achieve today's goals without compromising the future capacity to achieve them. Therefore, evaluating the sustainability of the food system needs to consider comprehensively, rather than looking at only one aspect of the food system。Based on this, we choose these four indicators to measure the food system from the four aspects of safety, stability and ecology. Then, the Sustainability index of food system(SI) can be calculated by the formula below:

(7)

Where, are the coefficients of the variables.

5 Answers to Questions

5.1 Food systems optimized for equity and Sustainability

5.1.1 Optimize food systems

In the previous paper, a comprehensive evaluation model of the food system is established and four optimization targets of food system are put forward. In today's world, despite the high

关注数学模型 economic level of many countries, food insecure people are common. This shows that the cur- rent food system has problems in the distribution link, and the equity of the food system needs to be improved urgently. In addition, the current food system leaves a massive environmental footprint accounting for “29% of green-house gas emissions, up to 80% of biodiversity loss, 微信公众号：数学模型 80% of deforestation, and 70% of all freshwater use.” So future food systems should focus more on sustainability.

To start, the optimization target value of the current food system is set. Specifically, we intend to increase the value of equity by 50 percent, and the value of sustainability by 50 per- cent.

Then, the entropy weight method is used to calculate the coefficients in the formula(6) and (7) ,the results are:0.5643, 0.1314, 0.1491, 0.1552, 0.2491, 0.4214, 0.3295.

Next, this 50% increase is allocated to each index according to the weight, and the distri- bution is shown in the following table3.

Table.3 The weight of each indicator Optimizations targets indicators targets 微信号：MATHmodels TF (0.5643) +28.2% CPI (0.1314) -6.6% Equity Index 50% GE (0.1491) +7.5% IE (0.1552) +7.8% FW (0.2491) +12.5% Sustainability Index 50% CE (0.4214) +21.1% From the above table, we can see the difference between the improved food system and the current one:

(1) ( Transportation facility)：transport facilities improved by 28%, the largest im- provement among all indicators. It is easy to understand that the better the road network, the less difficult the distribution of food, and the more equitable.

(2) ( Corruption Perception Index): Its value decreased by 6%, indicating that the im- provement of fairness does not require high government efficiency. Often a country's govern- ment is so complex that it is difficult to make big changes.

(3) (Gender equity and Income equity): As can be seen from the index names, these two indicators are closely related to equity.

(4) (Fresh water, CO2 emission and Forest coverage): There are many indi- cators we can find to measure the sustainability, we choose these three representative ones finally. And when sustainability is increased by 50%, their improvement goals are 12.5%, 21.1% and 16.5%.

5.1.2 Calculate the implement time

Because the above indicators cover different fields, and each indicator has a different goal for improvement. Therefore, we use the maximum amount of time it takes to achieve each goal individually as the total amount of time. The formula of calculating the time cost is :

(8)

关注数学模型

5.2 Benefits and costs Analysis

The cost-benefit analysis of changing food system priorities is complex. It involves mul- tiple aspects of food system outcomes. We need to consider many aspects, such as availability, 微信公众号：数学模型 access and utilization etc. The specific realization of the cost benefit is through the driver, and we will specify later which intervention plans are required. In order to simplify the calculation, we mainly consider the cost and benefit of food system in the ecosystem. From the first ques- tion to optimize the food system and improve the specific changes in indicators. Environment is often more important.

5.2.1 Costs Analysis

If the ecological security of the food system is given priority, we plan to reduce the agri- culture land in the food system and turn it into forest or grassland to improve the ecological environment. For the convenience of analysis we consider only terrestrial food production and not aquatic food. Therefore, in Task 3, we selected countries that mainly rely on terrestrial food 微信号：MATHmodels as their main food source.

Based on the above analysis, the cost of prioritizing ecological factors can be broken down into the following aspects[4].

(1) The cost of grain production reduction caused by the reduction of cultivated land area ； (2) Due to the reduction of arable land area, some farmers are unemployed. Thus the cost of resettling these farmers for employment should be considered； (3) The cost of additional food imports resulting from reduced production ； (4) The cost of ecological restoration of abandoned land 。 Therefore, the total cost can be calculated using the following formula： (9) Where, is the expense caused by uncertainty.

5.2.2 Benefit Analysis

Because of the priority given to ecology, our benefit analysis starts with ecosystem. In order to quantify ecosystem services, we look up relevant materials and obtain the classification of ecosystem services[12]. The results are shown in the table below： Table.4 Ecological system services Provisioning Regulating Culture Supporting services Services Services Services

⚫ Spiritual religious ⚫ Food ⚫ Recreation ecotour- ⚫ Soil for- ⚫ Fresh water ⚫ Climate regulation ism mation ⚫ Fuelwood ⚫ Disease regulation ⚫ Aesthetic ⚫ Nutrient cy- ⚫ Fiber ⚫ Water regulation ⚫ Inspirational cling ⚫ Biochemicals ⚫ Water purification ⚫ Educational ⚫ Primary pro- ⚫ Genetic re- ⚫ Pollination ⚫ Sense of place duction sources ⚫ Cultural heritage

关注数学模型 In consideration of the availability of data and the representativeness of indicators, ac- cording to the contents in the above table4 , fresh water(provisioning services), forest cover- age(provisioning services), air pollution(regulating services) and water pollution(regulating services) are selected to represent the country's ecosystem services. So the benefits can be cal- 微信公众号：数学模型 culated by the following formula:

(10) Where, are the coefficients of each variable.

5.2.3 profitability analysis（Benefits-Costs） Adapt specific food systems based on our analysis above. At the beginning, because of various unstable factors, the cost will continue to climb. But as time go on, the abandoned farmers are resettled, and the country gradually adapt to the economic structure of importing cereals, and the maintenance of the ecosystem enter into a phase of low consumption. As a result, costs tend to be stable.

As for the benefit, thanks to the gradual restoration of the ecosystem, all parts of the eco- 微信号：MATHmodels system services are slowly improved, so the benefit is also in a state of slow improvement.

Figure.7 Costs and Benefits analysis of food system From the Figure.7,we can obtain that when T0 the food system become profitable and after T0, it become more and more profitable.

5.2.4 Difference between developed and developing countries

In developed countries, given the high level of urbanization, less agriculture land, food production is low and food imports account for a large proportion. In addition, because the developed countries achieve economic development earlier, they are in a state of conservation rather than exploitation of the ecosystem.

Based on the above analysis, we can conclude that in developed countries, because the area of arable land is already small, the amount of food lost due to abandoned arable land is small. Losses from increased imports to supplement food are also relatively small. In addition, due to the high level of ecosystem services in developed countries before the food system im- proved, the time and economic costs required to restore abandoned farmland were relatively low.

关注数学模型 As a result, Figure.7 is no longer a good description of costs-benefits change in developed countries.

微信公众号：数学模型 Figure.8 Analysis in developed countries From the Figure.8, we find that in contrast to the previous graph, the starting point of benefits is higher and the point of profit is earlier.

微信号：MATHmodels While in developing countries, the main source of food is cultivation rather than importa- tion because of the relatively backward economic development. Because the area of agricul- tural land is so large, developing countries lose more food when the same proportion of agri- cultural land is turned over for restoration. In addition, due to the relatively weak awareness and capacity of ecological protection in developing countries, the time cost and economic cost of ecological restoration will be greater. The following figure shows the results.

Figure.9 Analysis in developing countries

5.3 Applied to Japan and India

We select India and Japan, respectively, to verify our conclusions in Task 2.

In order to find the weight of each variable in formula (14), we have data from the World Bank for 190 countries. The Matlab2019b software is used to process the data and calculate the weights. The results are:0.4612, 0.2156, 0.1876, 0.1347. Then, data from Japan and India are substituted into the formula to obtain a score (Japan: 68.5384 , India : 23.8331) to measure the ecosystem services of the two countries. To obtain the year of balance of payments for both countries, we use the GM (1,1) -PSO prediction model to predict optimized ecosystem service scores for India and Japan.

关注数学模型

5.3.1 GM(1,1) prediction model

Grey system theory[14] is a relatively important method of studying discrete data series with small numbers of samples and incomplete information. By fully developing and utilizing the explicit and implicit information in the existing data, the randomness that is present in the 微信公众号：数学模型 series is cumulatively weakened. The laws governing the changes in the system are thus gen- erated and can be used to research the future time distributions for specific time intervals. The core formula of GM(1,1) model is . Where, is a parameter of the model and its value determines the accuracy of the model.

5.3.2 The PSO Algorithm

The PSO algorithm[13] is aimed at stimulating the foraging behavior of birds. That is, we imagine a flock of birds randomly searching for food in a fixed field and mimic their behavior by randomly changing flight velocity. Each bird's position represents a solution, and the closer it is to the optimal value, the more likely it is to become the direction of the flock. The formulae

for calculating the change in velocity and position of the particle are given by:

(11) 微信号：MATHmodels (12) According to Niu et al. [14], the PSO algorithm can be used to find the best value of param-

eter to improve the accuracy of the prediction model.

5.3.3 Model application

Because the costs of optimizing food systems is not easy to measure and cannot be directly compared with ecosystem service scores. So we assume that when the incremental value of the ecosystem service score reaches 5% of the base score, the costs and benefits are equal. Thus, the target values for Japan's and India's ecosystem services scores are 75.392 and 26.213 re- spectively. The predicted results are shown in the figure below:

Figure.10 Prediction of ecosystem service scores in India

关注数学模型 微信公众号：数学模型 Figure.11 Prediction of ecosystem service scores in Japan 微信号：MATHmodels As can be seen from the above two graphs, Japan will reach its balance of payments in 2036, while India will reach its balance of payments even later in 2040. Thus, Japan, as a de- veloped country, achieve cost and benefit parity much earlier than India, as a developing coun- try, which is a good proof of the conclusion we made in Task 2.

5.4 Scalability and Adaptability

5.4.1 Scalability

When analyzing large and small food systems, our model uses the variation of coefficients to make more accurate predictions. Note that this is not just an expansion of activity in the food system itself, but also in relation to environmental, socio-economic and other indicators.

For larger food systems, we do a global analysis. When we analyze continents, we look more at trade between countries, such as trade and food exchange between rich and developing countries. If a country has a low food self-sufficiency rate due to ecosystem services, it is more important for these countries to consider food imports. Large countries have more human and energy resources that can be fully deployed in an emergency. As a combination of nations, continents have an inherent advantage in making flexible decisions. In the face of extreme situations, the degree of policy coordination in all regions in the context of social resilience is essential to rearrange the evaluation system.

When we think about smaller food systems, like cities, we need to think about urban and rural populations, and urban infrastructure tends to be more manageable in terms of re- source concentration. Moreover, national policies can easily affect cities, and the level of po- litical corruption often needs to be considered。 The concept of urban regional food system (CRF) includes a complex network of actors, processes and relationships that exist in a specific geographic region, including a more or less concentrated urban center and its surrounding suburban and rural hinterland. A regional land- scape that manages the flow of people, goods, and ecosystem services. Thus, the national re-

关注数学模型 porting framework approach is able to look at this complex problem from a practical perspec- tive and provide concrete solutions through the strengthening of rural-urban linkages.

The Food for Cities Initiative has been promoting dialogue and partnership with institu- tions at international and national levels, in particular with municipalities. 微信公众号：数学模型

5.4.2 Adaptability

In order to better verify the applicability of our model, we selected a country with a low ranking from the global hunger index for analysis. The results of our analysis are compared with the real situation and the corresponding intervention measures are proposed.

Yemen ranks 116th out of 117 participating countries in the 2020 Global Hunger Index. So we chose Yemen for our analysis. We obtained the data for Yemen from the World Bank and calculated Yemen's scores for each tier based on the FIO model we developed above and com- pared them to the world average, resulting in the radar chart below.

微信号：MATHmodels Figure.11 Yemen's scores compare with the world average As you can see from the chart above, Yemen's food system scores below the world average in all aspects. This is in line with Yemen's overall poverty, weak industry and constant conflict. Thus, it is necessary to take some measures to optimize the food system in Yemen, The following measures need to be taken:

⚫ United Nations agency says, to avoid the worst case, must immediately to ensure sus- tained and unhindered food aid, to save life, at the same time protect the food security and the livelihood of the displaced population.:

⚫ At the same time, must be immediately restore the water supply facilities damaged by the flood , and take measures to resist in and mitigate the effects of the flood of irrigation and water supply system in the future.

⚫ Farmers who have lost crops and pastures to pests and climate shocks urgently need support, the three agencies said, along with increased dietary nutrition, such as through home gardens, and education at the household level about food and water safety. Humanitarian agencies should further consolidate early warning and food

关注数学模型 safety monitoring systems and promote rapid and coordinated crisis response.

6 Intervention plans

微信公众号：数学模型

6.1 Resilience

Resilience are extremely cost-effective: they not only can reduce the cost of dealing with periodic crises, but also help overcome long-standing development gaps. Therefore, combining the search results, we make some suggestions as follows.

⚫ Establishing warning and preparedness systems early ⚫ Reducing the cost of periodic crises ⚫ Strengthening the national capacity of control disaster risk ⚫ Making the system of supporting social security

6.2 Equity

微信号：MATHmodels Equity distribution is an inevitable requirement for achieving fairness and harmonious, a necessary condition for making society be full of vitality, and a basic prerequisite for building a harmonious society. Therefore, fairness is also an indispensable feature for making a good food system. We also made a few suggestions to the government as follows.

⚫ Ensuring that members of society enjoy equal rights to education and employment, and achieve the starting point of incoming distribution fairly ⚫ Improving system of distribution according to work and distribution according to fac- tors, and realizing income distribution fairly ⚫ Adjusting the income gap and achieving income distribution result fairly

6.3 Sustainability

Sustainability refers to development that not only satisfies the needs of the present gener- ation, but does not harm the resources of future generations. While satisfying our food needs, we should not waste the resources of future generations. Therefore, Sustainability is an indis- pensable feature for making a good food system, too. We also made a few suggestions to the government as follows.

⚫ Family planning to limit the current population ⚫ Formulating a plan for the coordinated development of economy, population, re- sources and environment ⚫ Choosing an industrial structure and consumption mode that is conducive to resource conservation ⚫ Establishing a conservation-oriented national economic system

关注数学模型

7 Sensitivity Analysis

微信公众号：数学模型 (a) (b) 微信号：MATHmodels Figure.11 Sensitivity Analysis about the parameter e In this section, we make the sensitivity analysis about the parameter , which is based on GM(1,1)-PSO prediction model. The sensitivity analysis of the model is shown as fellows in Figure.11.(a) and Figure.11.(b).

Table.5 the mean absolute percentage error MAPE(%) Forecasting ability <10 High ability 10-20 Good ability 20-50 Reasonable ability >50 Weak ability

There, MAPE denotes the mean absolute percentage error, which reflects the accuracy of the prediction model. And the MAPE criterion used to assess accuracy is showed in Table.5. Figure.11.(a) reveals the process of PSO algorithm to find the global optimal solution , global optimal which is obtained when (where ). Figure.11.(b) shows that the MAPE value decreases as the number of iterations increases. Finally, after 18 iterations, the optimal solution is found ,namely the model has the best prediction accuracy.

8 Model Evaluation

8.1 Strengths

⚫ Our model not only optimizes the sustainability and equity of food systems, but also considers the resilience of the system to deal with the extremely situations, for exam- ple the new crown epidemic ⚫ Our model evaluating the food system is not only production and consumption, but also considering the results produced by these activities and driving factors of these activities, which is comprehensive and objective

关注数学模型 ⚫ We have established a multi-level indicator system, the first level indicators cover a wide range, and the second level indicators are more detail, so the model we built is comprehensive and detailed ⚫ The final score result of our model is very consistent with the global hunger index 微信公众号：数学模型 ranking, which shows that our model is reasonable and effective.

8.2 Weaknesses

⚫ Even though our food system evaluation model considers the problem indicators extremely comprehensive, but due to some indicator data missing and some indicators that we have not found, we can only choose the indicators that can be considered and the data is true and complete to analysis ⚫ When analyzing the benefit and cost, we mainly analyzes the benefit and cost of the food system in the environment, which is fault

微信号：MATHmodels

关注数学模型
