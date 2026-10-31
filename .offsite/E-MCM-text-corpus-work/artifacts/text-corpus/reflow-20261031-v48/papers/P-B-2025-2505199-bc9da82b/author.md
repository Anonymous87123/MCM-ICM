MCM/ICM

Summary Sheet

Summary

This study focuses on developing a sustainable tourism model for Juneau, Alaska, which is facing numerous problems caused by overtourism. In 2023, Juneau received 1.6 mil- lion cruise passengers, generating $375 million in revenue. However, it also encountered issues

such as glacier retreat, strained infrastructure, and social discontent. A multi - objective opti- mization model is constructed in this study, taking into account factors like the number of tourists, economic income, hidden costs, environmental protection, and measures to stabilize the tourism industry. The model aims to maximize tourism revenue, minimize ecological and environmental pressure, and enhance the overall satisfaction of residents and tourists. Decision variables include the number of tourists, government restrictions on numbers and consumption, tourism tax, tourist fees, and various government investments in infrastructure, environmental protection, and promotion. The constraints cover aspects such as tourist number limits, glacier protection, resource carrying capacity, and minimum - standard requirements.

The gradient descent method is used for data processing and fitting in the research, and the Non - dominated Sorting Genetic Algorithm II (NSGA - II) is employed to solve the model, accompanied by visualization processing. A comprehensive optimal solution is selected from the obtained results. The optimal solution shows that receiving 12,000 tourists per day, imposing an 8% tourism tax, charging a $15 tourist fee per person, and allocating 30% of the revenue from tourism tax and tourist fees to environmental protection, 40% to infra- structure construction, and 20% to tourism promotion can achieve the sustainable devel- opment of the tourism industry. Sensitivity analysis indicates that the number of tourists, alco- hol consumption restrictions, infrastructure construction, and key coefficients have a signifi- cant impact on the model results, and attention should also be paid to investment in environ- mental protection.

This model can be applied to other tourist destinations. For regions with high ecological pressure like Hawaii, the focus of adjustment lies on the environmental impact part of the model. Through model adjustment and calculation, it can be concluded that more emphasis should be placed on the ecological protection of this region. For areas with weak infrastructure, such as Yosemite National Park, strengthening infrastructure construction is the key. In areas with unique cultures, like New Orleans, cultural factors need to be considered. For regions with unbalanced tourism resource development, such as New York State, publicity and tourism re- source development are crucial. Finally, a memo is submitted to the Juneau Tourism Commit- tee, elaborating on the research findings, the effects of various measures, and suggestions for optimizing tourism outcomes, aiming to balance economic growth, environmental protection, and social well - being in the development of Juneau's tourism industry.

1 Introduction

1.1 Problem Background

Tourism is vital to the global economy, but overtourism is a growing concern, exemplified by Juneau, Alaska. With a population of around 30,000, Juneau hosted 1.6 million cruise pas- sengers in 2023, earning $375 million. However, this has led to significant issues. The Menden- hall Glacier is receding faster due to increased carbon emissions from tourism. Infrastructure is strained, with challenges in water supply and waste management. Residents face housing shortages and crowded spaces, and uncivilized tourist behavior has caused discontent.[1][4]

1,670,000

1,306,000 1,167,000 1,151,000 1,072,000 1,015,000 983,000 961,000

117,000

2015 2016 2017 2022 2023 2014 2018 2019 2020 2021 Source: City and Borough of Juneau; Cruise Line Agencies of Alaska

In response, Juneau has limited tourist numbers and increased taxes, but this has raised concerns among those dependent on tourism revenue. This situation is common globally. Bal- ancing tourism growth, environmental sustainability, and social well-being to create a sustain- able tourism model is a pressing issue.

1.2 Restatement of the Problem

Based on the above background, this study aims to:

• Develop a Sustainable Tourism Model for Juneau: Consider tourist numbers, reve- nue, and stabilizing measures. Identify optimization and constraint factors, plan additional in- come expenditure, and conduct sensitivity analysis to pinpoint key factors.

• Analyze Model Adaptability: Discuss applying the model to other overtourism-af- fected destinations, considering geographical impacts on measure selection and promoting lesser-known sites for balanced resource development.

• Write a Memo to Juneau's Tourism Committee: Summarize research findings, meas- ure impacts, and suggest ways to enhance sustainable tourism outcomes.

1.3 Our Work

Since economic, social, and environmental factors in Juneau's tourism are mutually re- strictive, and multiple goals like maximizing tourism revenue, minimizing environmental pres- sure, and enhancing satisfaction are pursued, traditional single - objective optimization models can't meet the needs. Thus, a multi - objective optimization model is chosen. It integrates mul- tiple goals, reflects the complex tourism system through decision variables and objective func- tions, balances objectives, and supports sustainable tourism strategies.

When solving the multi - objective optimization model, the NSGA - II algorithm stands out due to the non - linear objective functions and goal conflicts. It uses non - dominated sorting for hierarchical search, gets Pareto optimal solutions, maintains population diversity with crowding distance calculation, avoids premature convergence, and offers diverse decision - making options. Its genetic operations provide strong global search ability, helping to avoid local optima. So, the NSGA - II algorithm is used for model solving.

Moreover, the sustainable tourism model developed in this study is applicable not only to Juneau but also to other tourist areas. Different regions face diverse tourism issues. In Hawaii, with high ecological pressure, the model's environmental impact section needs adjustment, in- cluding adding variables and restrictions. Yosemite National Park in California, lacking infra- structure, requires strengthening the infrastructure - building part of the model. New Orleans, Louisiana, a culturally unique area, needs cultural factors incorporated into the model. New York State, with unbalanced tourism resource development, must optimize the resource - de- velopment part, adjust calculations, and improve tourist diversion. Such targeted model adjust- ments can support sustainable global tourism.

Last, we write a one-page memo to the tourist council of Juneau.

The work we have done is mainly shown in the following Figure 2:

2 Preparation of the Model

2.1 Assumptions and Explanations

To construct a sustainable tourism model for Juneau, the following assumptions are made

关注数学模型 to simplify complex real-world scenarios, allowing the model to focus on key factors and more clearly demonstrate the relationships between various elements of the tourism industry, provid- ing a foundation for subsequent modeling, analysis, and decision-making.

·Assumption 1: The maximum number of tourists in Juneau is stable.

·Explanations: Tourist consumption patterns are stable. Fixed per - capita spending and unchanging preferences simplify the model, helping determine Juneau's max tourist number 微信公众号：数学模型 based on other factors.

·Assumption 2: Tourist consumption patterns are stable with fixed per - capita spending and unchanging preferences.

·Explanations: This simplifies total tourism revenue calculation, bypassing complex consumer behavior.

·Assumption 3: Tourism revenue only comes from tourists and is not affected by ex- ternal economic factors. Extra income is accurately allocated.

·Explanations: It enables clear tracking of extra income's role in sustainable tourism.

微信号：MATHmodels ·Assumption 4: The local ecological environment's carrying capacity is stable, and nat- ural landscape changes are only due to known factors.

·Explanations: This allows for precise measurement of environmental stress from tour- ism.

·Assumption 5: Local infrastructure capacity is fixed, not affected by aging or technol- ogy, with a set tourist - capacity threshold.

·Explanations: It clarifies the link between infrastructure pressure and tourist numbers for control strategies.

·Assumption 6: Local residents' attitudes towards tourism depend only on tourist num-

bers, economic benefits, and living - environment changes, with a linear response.

·Explanations: This simplifies quantifying residents' satisfaction and analyzing tour- ism's social impact.

2.2 Notations

The key mathematical notations used in this paper are listed in Table 1.

Symbol

Description x Number of tourists 1y Restricted daily number of tourists Restricted sales and consumption of alcohol 2y Tourism tax 3y 4y Tourist fee Environmental protection expenditure 5y Infrastructure construction expenditure 6y 7y Tourism promotion expenditure Indicator for restricting the intensity of offshore activities 8y Z1 Tourism revenue Z2 Overall satisfaction of residents and tourists m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Z3 Ecological and environmental pressure A Basic number of tourists B Fluctuating number of tourists C Catering revenue D Transportation revenue E Accommodation revenue F Shopping revenue G Energy consumption costs H Management costs I Infrastructure costs J Drinking water supply costs K Waste disposal costs L Carbon footprint costs M Carbon emissions N Glacier retreat rate O Main tourism revenue P Additional tourism revenue Q Implicit costs of tourism R Additional income from other attractions S Residents' income T Residents' living pressure U Degree of congestion and noise V Residents' cost of living W Maximum glacier retreat rate to be preserved in certain years X Seawater pollution index Y Cultural heritage damage risk index Coefficients 𝜆i Constants 𝜀i

3  Model establishment

3.1 Optimization Objectives Setting

Based on the above analysis, the key optimization objectives are set as follows:

➢ Maximize tourism revenue ➢ Minimize ecological and environmental stress ➢ Enhance the overall satisfaction of residents and tourists[5] We have drawn the following figure to help sort out the situation of various optimization objectives, facilitating the subsequent model construction.

关注数学模型 微信公众号：数学模型 微信号：MATHmodels

3.2 Definition of Decision Variables

In the selection process of decision variables, we mainly consider two dimensions. The first is the number of tourists (x), which is a crucial variable for the construction of the entire optimization model. Fluctuations in the number of tourists can significantly impact various indicators. For example, an increase in the number of tourists may directly lead to an increase in tourism revenue (Z1), but it may also increase ecological and environmental stress (Z3) and decrease the overall satisfaction of residents and tourists (Z2). However, the number of tourists is not a variable that we can directly control, as it is influenced by a combination of factors such as market trends, seasonal changes, and the macroeconomic environment. We can only make reasonable predictions and indirect adjustments to the number of tourists based on government policy orientations, such as tourism promotion efforts and visa policies, as well as related tourism investments, such as the construction of tourism facilities and the improvement of service quality.

Based on this, we further introduce another set of decision variables that the government can directly regulate. These parameters cover data explicitly stipulated in government policies, specifically including: the daily tourist limit (y1), which can effectively control the flow of tourists and avoid the pressure on the environment and society caused by overcrowding; re- strictions on individual alcohol sales and consumption (y2), aimed at reducing undesirable behaviors caused by tourists' drinking and maintaining social order; tourism tax (y3), including various taxes such as hotel taxes, and additional fees charged to tourists (y4), which can not only bring additional income to the government but also regulate tourists' consumption behav- ior and guide them to use local resources more rationally; in addition, it also includes the gov- ernment's various investments in local tourism, such as environmental protection expendi-

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ture (y5), used to protect natural landscapes and the ecological environment to ensure the sus- tainable development of tourism; infrastructure construction costs (y6), used to improve transportation, accommodation, catering, and other infrastructure to enhance the tourism expe- rience of visitors; and tourism promotion expenditure (y7), used to promote local tourism resources to attract more tourists and also to enhance the brand image of local tourism.

These decision variables together form the core of our model. By reasonably setting and adjusting them, we can achieve the optimization goals, i.e., maximizing tourism revenue (Z1), minimizing ecological and environmental stress (Z3), and enhancing the overall satisfac- tion of residents and tourists (Z2), while meeting the constraints. In the process of model construction, we will analyze in detail the interrelationships among these decision variables and their impact on the optimization goals, thereby providing strong support for formulating scientific and reasonable sustainable tourism policies.

3.3 Construction of the Objective Function

⚫

Data Preparation

We recognize that many indicators are significantly correlated with the number of tour- ists (x), and most of these indicators have a positive correlation with the number of tourists. Therefore, we use the following formulas to calculate the relevant data to ensure the accuracy of the model.

➢ Catering Revenue:

y 2 − (1)  =  −  +  C x e 5 1 5 1 Catering revenue mainly comes from the consumption of tourists in catering venues. How- ever, restrictions on alcohol sales and consumption in the policy have a negative impact on catering revenue. To quantify this impact, we subtract the reduced part caused by the policy when calculating the catering revenue. We use an exponential function to fit this reduced in- come, which has been optimized through the asymptote and the slope at the zero point.

on the Decreased Amounts of Profits in Related Industries

➢ Transportation Revenue:

=  +  D x (2) 2 2 Transportation revenue mainly comes from the travel expenses of tourists, such as public transportation and car rentals. Transportation revenue has a linear positive correlation with the number of tourists. Therefore, we use a simple linear function to describe it.

关注数学模型 ➢ Accommodation Revenue:

=  +  E x (3) 3 3 Accommodation revenue is derived from the consumption of tourists in lodging facilities such as hotels and bed-and-breakfasts. Similar to transportation revenue, accommodation rev- enue also has a linear positive correlation with the number of tourists.

➢ Shopping Revenue:

y 2 − (4)  =  −  +  F x e 6 4 6 4 Shopping revenue mainly comes from the consumption of tourists in shopping malls, sou- venir stores, and other venues. Similarly, policies that restrict alcohol sales and consumption also have a negative impact on shopping revenue. Therefore, when calculating shopping reve- nue, we also subtract the reduced part caused by the policy and use an exponential function for 微信公众号：数学模型 fitting.

Since the profit is equal to the total revenue minus the cost, and both total revenue and cost are roughly positively correlated with the number of tourists, we can infer that the profit is also approximately positively correlated with the number of tourists. Based on this, the rev- enue calculated here is directly taken as the profit.

➢ Drinking Water Supply Costs:

=  +  J x (5) 7 7 Drinking water supply costs have a linear positive correlation with the number of tourists.

微信号：MATHmodels These costs primarily stem from the infrastructure and operational expenses required to provide drinking water to tourists.

➢ Waste Disposal Costs:

=  +  K x (6) 8 8 Waste disposal costs also have a linear positive correlation with the number of tourists. These costs mainly originate from the cleaning and processing expenses associated with the waste generated by tourists.

➢ Management Costs:

=  +  H x (7) 9 9 Management costs are linearly and positively correlated with the number of tourists. These include operational expenses related to tourism management, security, services, and other as- pects. ⚫ Economic Aspect The goal in the economic aspect is to maximize the profit, that is, the normal tourism revenue. However, in addition to the normal tourism revenue, due to factors such as relevant tourism taxes and tourist fees set by policies, we also have some additional income beyond tourism. This additional income can be used to support environmental protection, improve in- frastructure, develop community projects, and so on.

In addition, recent reports have emphasized the hidden costs of the tourism industry, in- cluding the pressure on local infrastructure and the increase in carbon footprint. Therefore, we define the final profit as the normal tourism revenue plus the additional income minus the hid- den costs, that is:

= + − Z O P Q (8) 1 ➢ Normal tourism revenue:

Normal tourism revenue can be recorded as the sum of various incomes, plus the income from the development of other less popular tourist attractions resources promoted by policies. The income from the development of other less popular tourist attractions resources has a roughly positive correlation with government policies and various government expenses. Therefore, it is described using a positive proportionality coefficient, that is:

= + + + + O

C D

E F R (9) =  +  +  R y y y (10) 10 5 11 6 12 7 Among them, R represents the income from the development of other less popular tourist attractions resources promoted by government policies. It is related to environmental protec- tion expenditure (y5), infrastructure construction expenditure (y6), and tourism promotion expenditure (y7). We have collected relevant information and data, and roughly estimated the proportion of each component of tourism revenue, as shown in the following figure.

➢ Additional income:

The additional income mainly consists of tourist fees, tourism taxes, etc. The tourism taxes include various taxes such as hotel taxes, and these taxes can be directly regulated by the gov- ernment. Tourist fees are mainly positively correlated with the number of tourists, while tour- ism taxes are mainly positively correlated with normal tourism revenue, that is:

= + P y x y O (11) 4 3 Among them, y4 represents the additional fees charged to tourists, and y3 represents the tourism tax.

➢ Hidden costs:

The scope of hidden costs is relatively wide. Here, we consider infrastructure - related costs, environmental protection - related costs, management costs, various government expend- itures, etc. Among them, infrastructure - related costs can be further divided into several costs such as drinking water supply costs and waste disposal costs, and the rest of the expenditures can also be subdivided. It can be expressed by the following formula:

关注数学模型 = + + + Q

I L

H y (12) 7 = + + I J K y (13) 6 =  +

L M

y (14) 13 5 The calculation method of carbon emissions M will be presented in detail in the next section. ⚫ Social Aspect The social aspect primarily focuses on enhancing the overall satisfaction of residents and tourists. The function for overall satisfaction of residents and tourists (Z2) is constructed as 微信公众号：数学模型 follows:

S ( , x y y , , y , y , y , y ) S ( , x y y , , y , y , y , y ) (15) =   +  resident 1 3 4 5 6 7 tourist 1 3 4 5 6 7 Z [ ] 2 14 1 2 max( S ) max( S ) resident tourist

Among them, S ( , x y y y , , , y y , , y ) represents the satisfaction function of resi- resident 1 3 4 5 6 7

dents, which is a function of the number of tourists (x) and various decision varia- bles(y1,y3,y4,y5,y6,y7). The income of residents mainly comes from the consumption of tourists in catering, accommodation, shopping, and other aspects, and can be expressed as:

微信号：MATHmodels (16) =  +  +  S

C E

F 16 17 18 The living pressure of residents is related to the degree of congestion and noise, as well as the increase in the cost of living for local residents, and can be expressed as:

=  +  T U V (17) 19 20 =  +  U x (18) 21 21 =  +  V x (19) 22 22 The resident satisfaction function can be constructed as:

S T x =  −  −  S ( , x y y , , y , y , y , y ) (20) resident 1 3 4 5 6 7 1 2 3 max( ) S max( ) T max( ) x Among them, α1 measures the impact of tourism-generated economic benefits on resident satisfaction, α2 measures the impact of living pressure on resident satisfaction, and 𝛼3 measures the impact of the number of tourists exceeding the limit on resident satisfaction. Through the setting of these weights, the comprehensive consideration of the impact of economic benefits, living pressure, and congestion on resident satisfaction is achieved.

S ( , x y y y , , , y y , , y ) represents the tourist satisfaction function, which can be tourist 1 3 4 5 6 7

constructed as:

+ ( y y ) y x =  − −  5 6 S ( , x y y , , y , y , y , y ) 4 (21) tourist 1 3 4 5 6 7 1 2 3 + max( y y ) max( y ) max( ) x 5 6 4 Among them, 𝛽1 measures the impact of environmental protection and infrastructure con- struction investment on tourist satisfaction, 𝛽2 measures the impact of tourism cost on tourist satisfaction, and 𝛽3 measures the impact of congestion on tourist satisfaction. These weights reflect the impact of tourism investment and congestion on tourist satisfaction.

𝜔1 and 𝜔2 are the weights of resident satisfaction and tourist satisfaction in the overall satisfaction, respectively, and 𝜔1+𝜔2=1. By adjusting these weights, the satisfaction of resi- dents and tourists can be balanced according to actual needs. ⚫ Environmental Aspect The environmental objective is to minimize ecological and environmental stress. This stress primarily stems from carbon emissions generated by tourist activities, resource consump- tion (such as drinking water usage), and disturbances to local ecosystems (for example, the impact of tourists on the ecology around the glacier). The calculation of carbon emissions(M) is crucial, as it mainly includes energy consumption hidden in major conventional income costs, as well as carbon emissions produced in the handling of waste and infrastructure construction, and can be expressed as:

=  +  + 

M G

K y (22) 23 24 25 6 =  +  +  G

C D

E (23) 26 27 28 Among them, G represents the carbon emissions from energy consumption implied in catering, transportation, and accommodation revenues, and 𝜆23, 𝜆24, and 𝜆25 are the contribution coefficients of each part's carbon emissions to the total carbon emissions.

Taking into account factors such as carbon emissions, drinking water supply costs (re- flecting water resource consumption), and waste disposal costs (reflecting the environmental impact of waste emissions), the ecological and environmental stress function (Z3) is con- structed as follows:

M J K =   +  +  Z [ ] (24) 3 15 3 4 5 max( M ) max( ) J max( K ) Among them, 𝜔3, 𝜔4, and 𝜔5 are the weights of carbon emissions, drinking water supply costs, and waste disposal costs in the ecological and environmental stress, respectively, and 𝜔3 +𝜔4+𝜔5=1. By adjusting these weights, the impact of each factor on the ecological and envi- ronmental stress can be determined according to local environmental characteristics and key environmental issues of concern.

3.4 Setting of Constraints

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m When constructing a sustainable tourism model for Juneau, to ensure the feasibility and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m practicality of the model and take into account the sustainable development of the economy, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m society, and environment, the following key constraints are set to balance the economic benefits m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m of tourism activities with their impacts on local society and the environment. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ⚫ Tourist Number Constraints The number of tourists is a core factor affecting the sustainability of tourism activities. Excessive tourists can negatively impact the local environment and social order, while too few tourists may not fully realize economic benefits. Therefore, we set constraints based on local government policies to ensure a reasonable number of tourists.

➢ Daily Tourist Limit:

 x 365 y (25) 1 where x is the number of tourists and y1 represents the restricted daily number of tourists. This ensures that the total number of tourists within a year does not exceed the sum of the maximum daily tourist numbers set by the local government, controlling the tourist flow and

关注数学模型 reducing environmental and social pressure.

➢ Dynamic Tourist Number Constraints:

 + x 365( A B ) (26) where A and B represent the base number of tourists and the fluctuating number of tourists, 微信公众号：数学模型 respectively, and are calculated as follows:

y 1 − (27)  =  − + A 29( e 1) 29

=  +  +  −  −  B y y y y y (28) 30 5 31 6 32 7 33 3 34 4 Here, A represents the base number of tourists under restricted conditions. When the re- stricted number of tourists is small, it has a significant impact on the number of tourists in Juneau, almost determining the number of tourists on a given day. However, when the restricted number of tourists is large, the impact is smaller, and the difference with the original number of tourists is not significant. Regardless of how the restricted number of tourists increases, the 微信号：MATHmodels final number will not exceed the number of tourists who would have arrived. Therefore, based on the characteristics of this function, we have adopted the above formula for fitting. Addition- ally, the characteristics of A are similar to the impact caused by policies restricting alcohol sales and consumption.

B represents the changes in the number of tourists due to government investments (envi- ronmental protection expenditure y5, infrastructure construction expenditure y6, tourism pro- motion expenditure y7) and tax policies (tourism tax y3, tourist fees y4). The dynamic constraints on the number of tourists can be adjusted flexibly according to policies and investments. ⚫ Glacier Protection Constraints Glaciers are important natural landscapes in Juneau, and their protection is crucial for maintaining the local ecological balance and tourism appeal. To protect the glaciers and ensure that tourism activities do not cause irreversible damage, we have set glacier protection con- straints. Specifically, we limit the retreat rate of the glacier to ensure that it maintains a certain scale within a certain number of years. The retreat of the glacier is highly correlated with carbon emissions, and the maximum retreat rate of the glacier is calculated by another formula. The meaning is that the current scale of the glacier, minus the amount of retreat per year multiplied by time, must be greater than a given critical value. The specific constraint is as follows:

 N W (29) where N represents the glacier retreat rate, and W represents the maximum retreat rate to m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m preserve the glacier within a certain number of years. The specific calculation is as follows:

= M   N (30) 35 Here, M represents the carbon emissions, and 𝝀35 is the proportionality coefficient be- tween the glacier retreat rate and carbon emissions. Through this constraint, we can control the retreat rate of the glacier within a sustainable range, thereby protecting the glacier from the negative impacts of tourism activities.

 −     W (31) 43 44 45 This constraint ensures that the glacier maintains a given scale after a certain number of years, considering the goal of glacier protection. By setting this constraint, we can further strengthen the protection of the glacier and ensure that it continues to maintain its unique nat- ural landscape and ecological value in future tourism activities. ⚫ Resource Capacity Constraints:

Resource capacity constraints ensure that tourism activities do not exceed the carrying capacity of local resources, including infrastructure, human resources, and natural resources.[4] These constraints aim to prevent the overdevelopment of tourism activities from leading to the overconsumption of local resources and environmental degradation. The specific constraints are as follows:

➢ Drinking Water Supply Costs:

  J (32) 36 ➢ Waste Disposal Costs:

  K (33) 37 ➢ Energy Consumption Costs:

  G (34) 38 Here, 𝜆36, 𝜆37, and λ38 are their respective maximum allowable values. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ⚫ Minimum Level Constraints m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m To ensure that tourism activities bring certain economic and social benefits to the local m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m area while ensuring the quality of life and social stability of residents, we have set minimum m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m level constraints to ensure that various indicators do not fall below a certain basic level. The m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m specific constraints are as follows:

➢ Overall Satisfaction of Residents and Tourists:

  Z (35) 2 39 ➢ Ecological and Environmental Stress:

  Z (36) 3 40 ➢ Environmental Protection Expenditure:

  y (37) 5 41 ➢ Infrastructure Construction Expenditure:

  y (38) 6 42 Here, 𝜆39, 𝜆40, 𝜆41, and 𝜆42 are their respective highest and lowest allowable values. ⚫ Data Range Constraints To ensure the stability and reliability of the model and avoid model failure due to abnormal data, we have set reasonable range constraints for all input data. The specific constraints are as

关注数学模型 follows:

All calculated data must be greater than or equal to 0, i.e., W  x y , , Z , A 0 (39) 1 7 1 3 By setting this constraint, we can ensure that all data are within a reasonable range, thereby ensuring the stability and reliability of the model. 微信公众号：数学模型

4 Model Solution

4.1 Data Processing and Function fitting

In the process of constructing the sustainable tourism model for Juneau, data fitting is a crucial step in determining the relationships among various variables in the model, which has a significant impact on the research conclusions. Our team collected a large amount of data related to Juneau, such as tourism revenue, the number of tourists, and the rate of glacier retreat. After carefully studying these data, we found that most of these variables have a simple linear 微信号：MATHmodels relationship. For example, Transportation revenue:

=  +  D x (40) 2 2 We use the gradient descent method. Based on a set of collected data   n ( , x D ) , we i i = i 1

use the mean - square error loss function:

n 1    2 −  +  D ( x ) (41) i 2 i 2 n = i 1 We calculate the gradient, set the learning rate, and then update the parameters:

 n 2    +  =  + −  +  ( k 1) ( ) k ( ) k ( ) k D ( x ) x (42)   2 2 i 2 i 2 i n = i 1  n 2    +  =  + −  +  ( k 1) ( ) k ( ) k ( ) k D ( x ) (43)   2 2 i 2 i 2 n = i 1 Then we start the iterative calculation, and finally converge to obtain the optimal solution parameters.

Next, by using professional mathematical software and the above - mentioned method, we successfully calculated the coefficients of multiple functions and fitted multiple curves.

Coefficients Value Coefficients Value Coefficients Value λ1 λ8 λ15 1257.94 14.67 0.75 λ2 λ9 λ16 1051.23 1.88 0.17 λ3 λ10 λ17 1944.38 19.48 0.21 λ4 λ11 λ18 768.4 4.68 0.15 λ5 λ12 λ19 599.37 15.61 0.63 λ6 λ13 λ20 762.39 46 0.38 λ7 λ14 λ21 23.88 0.005 0.22 m m m m m m m m m m m m m m m m m m m m m m Coefficients Value Coefficients Value Coefficients Value m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m λ22 λ29 λ36 0.33 10053.49 288000000 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m λ23 λ30 λ37 0.86 0.36 63360000 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m λ24 λ31 λ38 0.08 0.48 839000000 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m λ25 λ32 λ39 0.56 0.57 0.92 λ26 λ33 λ40 52.44 0.28 0.66 λ27 λ34 λ41 34.67 0.34 24600 λ28 λ35 λ42 26.78 0.000001 162800

4.2 Model Solution Based on NSGA-II

Considering that this model is a multi-objective optimization model with non-linear char- acteristics in the objective functions and involves multiple conflicting objectives (maximizing tourism revenue, minimizing ecological and environmental stress, and enhancing the overall satisfaction of residents and tourists), the Non-dominated Sorting Genetic Algorithm II (NSGA-II) is selected for solving. [2][3] This algorithm performs excellently in handling multi- objective optimization problems, effectively managing conflicts among objectives and search- ing for a set of evenly distributed Pareto optimal solutions, providing decision-makers with various trade-off options.

◆ Population Initialization Randomly generate an initial population of size N0. Each individual consists of decision variables[x,y1,y2,y3,y4,y5,y6,y7]. Each decision variable is randomly assigned a value within a reasonable range. ◆ Fitness Calculation (Multi-objective Evaluation) For each individual in the population, calculate the values of the three objective functions: economic, social, and environmental.

➢ Economic Objective Function (Maximizing Tourism Revenue):

= + − Z O P Q (44) 1

关注数学模型 ➢ Social Objective Function (Maximizing Overall Satisfaction of Residents and Tourists):

=   +   Z [ S ( , x y y y , , , y y y , , ) S ( , x y y y , , , y y y , , )] (45) 微信公众号：数学模型 2 14 1 resident 1 3 4 5 6 7 2 tourist 1 3 4 5 6 7

➢ Environmental Objective Function (Minimizing Ecological and Environmental Stress):

M J K =    +   +   Z [ ] (46) 3 15 3 4 5 max( M ) max( ) J max( K ) ◆ Non-dominated Sorting Perform non-dominated sorting on the individuals in the population, dividing the popula- tion into different levels (fronts). In multi-objective optimization, if individual A is not worse 微信号：MATHmodels than individual B in all objectives and is better than individual B in at least one objective, then individual A is said to dominate individual B.

Individuals in level 1 are non-dominated (no other individuals dominate them).

Individuals in level 2 are the remaining non-dominated individuals after excluding level 1 individuals, and so on. Through non-dominated sorting, individuals in the population are layered according to their degree of superiority, enabling the algorithm to prioritize the search for better solutions. ◆ Crowding Distance Calculation For individuals of the same level, calculate their crowding distance. The crowding dis- tance reflects the degree of congestion of individuals in the objective space and is used to maintain the diversity of the population. The calculation method is to calculate the sum of the distances between an individual and its adjacent individuals in each objective dimension. The greater the distance, the sparser the solutions around that individual. Assuming there are m objectives in the objective space (in this model, m=3, tourism revenue, ecological and environ- mental stress, and overall satisfaction of residents and tourists), the crowding distance(di) for individual i is calculated as:

+ − − i 1 i 1 f f m  k k = d (47) i − max min f f = k 1 k k i max kf represents the function value of individual i in the j-th objective, and kf where min kf and are the maximum and minimum values of all individuals in the j-th objective. When selecting individuals for genetic operations, individuals with larger crowding distances are pre- ferred to avoid the algorithm converging too early and ensure that the Pareto optimal solutions found have good distribution. ◆ Genetic Operations ·Selection: Use tournament selection, randomly select n individuals from the population (the tournament size is set as n), and choose the individual with the highest level and the largest crowding distance to enter the next generation population. Repeat this process until the number of selected individuals is the same as the current population size, forming the parent population.

·Crossover: Perform crossover operations on the individuals in the parent population to generate new individuals. Use the Simulated Binary Crossover (SBX) method. For two parent individuals P1 and P2, perform crossover with a certain probability to generate offspring C1 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and C₂. The formulas for generating offspring are:

ηc +1 |P_ −-P_2|· βq, C1 (48) 2 2 ηc +1 |P −-P2|· βq C2 (49) 2 2 where βq is a parameter related to crossover, calculated based on a random number r :(110) 1 = (2r)n+1 , 0 ≤ r ≤ 0.5 β (50) 1 1 ηc +1 β ,0.5 < r ≤1 二 2(1−r) q

ηeis the distribution index for crossover, usually set to a large value to control the intensity of the crossover operation. The crossover operation allows the offspring to inherit the charac- teristics of the parent individuals in the decision variables, helping to search for new solution spaces.

• Mutation: Perform mutation operations on the individuals after crossover to increase the diversity of the population. Use the polynomial mutation method. For each individual, per- form mutation on its decision variables with a certain probability (Pm). For decision variable x (other decision variables are similar), the formula for the mutated variable x' is:

(51) x′= x + ∆(x) Among them, ∫(xmax − x) · δ,0 ≤ r ≤ 0.5 (52) ∆(x) = (x − χmax)·δ,0.5 < r ≤1 1 (53) δ = (2r)η+1 −1 where ηm is the distribution index for mutation, usually set to a large value (e.g., 20-30) to control the intensity of the mutation operation. The mutation operation causes the decision variables of individuals to change randomly within a certain range, avoiding the algorithm fall- ing into local optimal solutions.

Population Update C

Combine the mutated individuals with the parent population to form a mixed population. Perform non-dominated sorting and crowding distance calculation on the mixed population again, and select individuals with high levels and large crowding distances to form a new pop- ulation, which will serve as the next generation population. Repeat the steps of fitness calcula- tion, non-dominated sorting, crowding distance calculation, genetic operations, and population update until the termination condition is met.

4.3 Analysis of the solution results and selection of the optimal solution

We used the NSGA - II algorithm to solve Juneau's sustainable tourism multi - objective optimization model, getting decision variable solutions and corresponding objective function values. Figure 8 shows the Pareto optimal surface of economic, social, and environmental ob- jectives. It reveals the trade - offs in multi - objective optimization. We can see that maximizing

关注数学模型 tourism revenue, minimizing environmental pressure, and boosting satisfaction are mutually restrictive. For instance, improving economic indicators like tourism revenue may worsen en- vironmental ones. This helps us choose the optimal solution.

微信公众号：数学模型

the Economy, Community, and Environment 微信号：MATHmodels From an economic angle, tourism revenue is crucial. In practice, more tourists usually mean more revenue, but too many can spoil the experience and cut into earnings. Our analysis shows that with 12,000 daily tourists , an 8% tourism tax, and $15 - per - person tourism fees, tourism revenue can be substantial and sustainable. This tourist volume guarantees consump- tion while maintaining service quality, and the tax boosts revenue without scaring tourists away.

The environment is greatly affected by the number of tourists. More visitors mean more environmental stress. To safeguard Juneau's environment, we need to limit tourists and invest more in conservation. When there are 12,000 daily tourists, using 30% of tourism revenue for environmental projects like glacier protection and rainforest restoration can ease environmental degradation and balance tourism and the ecosystem.

Social satisfaction depends on factors like tourist numbers, economic gains, and infra- structure stress. A proper number of tourists benefits residents economically and raises social satisfaction. When there are 12,000 daily tourists, allocating 40% of revenue to infrastructure (e.g., improving transport and accommodation) and 30% to community development (such as training and building public facilities) can increase residents' income, enhance their quality of life, and thus boost social satisfaction.

In conclusion, the optimal solution is: 12,000 daily tourists(x), an 8% tourism tax(y3), a $15- per - person tourist fee(y4), 30% of total revenue for environmental protection(y5), 40% for infrastructure(y6), and 20% for tourism promotion(y7). This solution supports sus- tainable tourism, controls environmental impact, and raises social satisfaction, meeting Ju- neau's needs. It also aligns with the Pareto optimal surface, validating its rationality. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5 Sensitivity Analysis

The sensitivity analysis focuses on the impact of changes in model parameters and varia- bles on the results of Juneau's sustainable tourism model. The following analysis is carried out in conjunction with Figure 9 and Figure 10.

➢ Single-Parameter Sensitivity Analysis:

This study employs a single-parameter sensitivity analysis to evaluate how various objec- tive functions respond to changes in parameters. For the three figures in the Figure 9, the first one demonstrates that the negative economic index decreases with increasing step size, imply- ing that higher infrastructure investment enhances tourist capacity and boosts economic reve- nue. The second one reveals that the negative community index rises with step size, indicating that stringent alcohol consumption restrictions could reduce residents' income and satisfaction. The third one indicates that the environmental index increases with step size, suggesting that excessive infrastructure development leads to higher carbon emissions and necessitates in- creased environmental protection. These findings underscore the varying sensitivities of objec- tive functions to parameter changes, highlighting the need for a balanced approach in policy- making to ensure sustainable development. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ➢ Multi-Parameter Sensitivity Analysis: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

The Negative of the Economic Index

关注数学模型 In the multi-parameter sensitivity analysis for Objective 1, which is the negative of the economic index, it has been observed that parameter y6 exhibits the most significant influence on the objective value. This is evidenced by the prominent changes in the objective value across various step sizes for y6 when compared with other parameters. Additionally, the interaction 微信公众号：数学模型 between parameters y3, y4, y5, and y7 appears to be substantial, as indicated by the complex patterns observed in the corresponding plots. These interactions suggest that changes in one of these parameters can significantly affect the others, leading to a non-linear response in the economic index. Conversely, parameters y1 and y2 seem to have a relatively minor impact on the objective value, as the changes in the objective value are less pronounced and more uniform across the step sizes for these parameters.

6 Model Evaluation and Further Discussion

微信号：MATHmodels

6.1 Strengths

·The model integrates key factors like tourist numbers, revenue, infrastructure stress, environmental impact, and social satisfaction, building a multi - objective optimization model. It fully reflects Juneau's tourism reality, avoiding single - objective optimization's one - sided- ness.

·With a rational objective function design, it weights objectives to clarify their im- portance in overall optimization, allowing the model to balance among different goals.

·During model - solving, parameter adjustment, optimization, and result analysis ensure algorithm effectiveness and stability.

·The model fits historical data well, accurately predicting tourism trends by analyzing past data. Based on various assumptions and policies, it forecasts revenue, environmental im- pact, and satisfaction, supporting decision - making.

·Its output offers practical suggestions for Juneau's tourism policy - making.

6.2 Weaknesses

·The tourism market is dynamic. Tourist demands change, but the model based on his- torical data can't adapt fast.

·Policies have dynamic impacts, yet the model focusing on static effects can't assess long - term ones accurately.

·The tourism market is competitive. Juneau faces regional competition, but the model focused on its own development doesn't consider this fully.

6.3 Further Discussion

·In the future, relax model assumptions and incorporate real - world factors like diverse tourist behavior to make it more practical.

·Introduce variables like tourist satisfaction to enrich the model and enhance its accuracy.

·Add factors like demand prediction to reflect market dynamics and enable quick adap- tation.

·Adopt advanced algorithms like deep learning to boost efficiency and accuracy for de- cision - making support.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

7 The Promotion of the Model in Other Regions

This section analyzes the promotion of the Juneau sustainable tourism model in different tourist areas, explores model adjustments for their characteristics, and provides conclusions and suggestions.

1. Areas with high ecological pressure - Hawaii

Hawaii, famous for beaches, marine life and culture, is a popular tourist spot. But rising tourist numbers bring problems like marine pollution and coral reef degradation. When apply- ing the model in Hawaii, we must focus on adjusting the environmental impact part.[6][7] Due to the fragile marine ecosystem, add a seawater pollution index variable X, and adjust the formula to:

=  +  X x y (54) 43 44 8 Where x represents the number of tourists, y8 is the index for restricting the intensity of offshore activities, and 𝝀43、𝝀44 are coefficients.

Then we have, M J K X =   +  +  +  Z [ ] (55) 3 15 3 4 5 6 max( M ) max( ) J max( K ) max( X )  Meanwhile, set seawater quality standard limits

X X

,where X is set according max max to local marine ecological protection standards and relevant regulations. Additionally, we need to remove the constraint condition regarding the glacier retreat rate. The Pareto optimal surface diagram drawn after the model adjustment is as follows:

In Hawaii, environmental factors are more crucial. The increase in tourists exacerbates seawater pollution and coral reef degradation, so stricter tourist - number control is needed to protect the marine environment. Hawaii should strengthen offshore - activity management, limit the intensity of activities like diving and snorkeling, and boost investment in marine en- vironmental protection, including pollution treatment and coral - reef restoration.

关注数学模型

2. Areas with Weak Infrastructure - Yosemite National Park, California

Yosemite National Park in California has stunning natural scenery, but its infrastructure falls short. It can't meet tourists' needs, resulting in a bad experience and more environmental stress. So, we must strengthen the infrastructure part of the model. First, raise the value of the minimum infrastructure requirement 𝝀42 and significantly increase the infrastructure construc- tion coefficient 𝝀11. Second, adjust how we calculate infrastructure spending to better show its impact on tourists and the environment.

In local tourism development, infrastructure is key. Good facilities can boost tourist satis- 微信公众号：数学模型 faction, ease environmental pressure, and help use tourism resources sustainably. California should invest more in Yosemite's infrastructure, like improving transport, accommodation, and dining. Also, manage tourists better, plan visitor flows well, and prevent overcrowding.

3. Areas with Special Cultures - New Orleans, Louisiana

New Orleans, Louisiana, draws many tourists with its unique music, food and culture. But in tourism development, it faces cultural protection and inheritance challenges, plus pressure from more tourists. When applying the model here, consider cultural factors' impact on tourism. Add cultural heritage damage risk index variable Y, and adjust the formula to:

=  Y x 微信号：MATHmodels (56) 45 Among them, 𝝀45 is the coefficient of the proportion of tourists in a specific area. Also   x x limit the tourist numbers to protect cultural heritage. − 45 special max Cultural factors are crucial to New Orleans' tourism. More tourists threaten cultural herit- age. So, Louisiana should step up protection and management, make strict policies, boost awareness through promotion, and encourage civilized tourism.

4. Regions with Unbalanced Tourism Resource Development - New York State

New York State has abundant tourism resources, but development is unbalanced and in- sufficient. Some areas' resources are underused while popular spots are overcrowded. We need to optimize the tourism resource development part in the model. Increase the publicity invest- ment coefficient 𝝀12, adjust how to calculate tourism revenue, considering resources' value and development potential in different regions to reflect the development accurately. Also, optimize tourist diversion strategies to guide tourists to less - developed areas for balanced resource use.

Tourism resource development and tourist diversion are vital for New York State's tourism. Rational development and optimized diversion can boost resource efficiency and sustainable tourism growth. New York State should strengthen resource development and integration, in- vest more in less - developed areas, enrich tourism products, and enhance appeal. It should also make proper diversion strategies to guide tourists' distribution and prevent overcrowding at popular attractions.

8 Memo

From: Team 2505199 To: the tourist council of Juneau Date: January 27th, 2025 Subject: Sustainable Tourism Strategies for Juneau Dear Tourism Committee Members, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m This memo summarizes our research on sustainable tourism in Juneau and offers practical m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m strategies to optimize tourism development. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Research Findings m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m In 2023, Juneau welcomed 1.6 million cruise passengers, bringing in $375 million. How- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

ever, this boom caused problems like the faster retreat of Mendenhall Glacier, infrastructure stress, and social unrest. We created a multi - objective optimization model considering tourist numbers, revenue, and regulatory measures to address these.

Key Results

Optimal Solutions: Model results suggest 12,000 daily tourists, an $80 - per - person tour- ism tax, and a $15 - per - person fee can balance economic, environmental, and social goals. Allocating 30% of revenue to environmental protection, 40% to infrastructure, and 30% to community development can enhance satisfaction and ensure sustainable growth.

Sensitivity Analysis: Tourist numbers, tourism tax, and key coefficients strongly influence the model. More tourists initially increase revenue but also heighten environmental stress and lower satisfaction. A higher tourism tax raises government income but may drive away tourists.

Effects of Measures ·Tourist Number Limitation: Limiting tourists (12,000 daily) reduces environmental and infrastructure stress, ensuring a quality tourism experience.

·Tax and Fee Adjustment: Raising taxes and fees can fund environmental and infrastruc- ture projects. But rates need careful setting to avoid scaring off tourists.

·Investment in Tourism: Investing in environmental protection, infrastructure, and pro- motion can attract more tourists. Good infrastructure improves satisfaction, and environmental efforts preserve Juneau's beauty.

Recommendations

·Policy - making: Regulate tourist numbers according to capacity, factoring in seasons and market trends when setting daily limits.

·Revenue Allocation: Wisely distribute extra revenue, prioritizing environmental and in- frastructure improvements for sustainable tourism.

·Promotion: Promote Juneau's unique features to draw high - spending tourists. Highlight its natural and cultural assets, and sustainable tourism concept to enhance its brand.

Implementing these strategies can help Juneau achieve sustainable tourism, balancing economic, environmental, and social interests.

Best regards, Team 2505199

关注数学模型

Model - Building Incorporation: The suggestions from Doubao regarding decision varia-

bles and objective - function construction were carefully considered. We conducted additional research and analysis to determine whether these suggestions were applicable to our model. If they were, we incorporated them into our model after proper modification and verification. Data - Analysis Incorporation: The data - analysis and visualization advice from Kimi were used as references for our data - analysis process. We compared Kimi's suggestions with our own analysis methods and selected the most appropriate approaches. For example, we com- bined Kimi's recommended time - series analysis method with our existing data - analysis techniques to more accurately predict tourist flow trends.

4. Assurance of Originality and Compliance

Originality Assurance: All key aspects of our work, including problem - solving ideas, model construction, data analysis, and conclusion - drawing, were the result of our team's in- dependent thinking and efforts. AI tools were used as aids to provide inspiration and supple- mentary information. For example, although Doubao provided suggestions on decision varia- bles, the final selection and determination of decision variables were based on our in - depth understanding of the problem and the actual situation in Juneau.

Verification and Validation: We thoroughly verified all AI - generated outputs. For the literature resources recommended by Doubao, we checked their academic reliability and rele- vance. For the data - analysis and hypothesis - testing advice from Kimi, we conducted inde- pendent verification using our own data and analysis methods. Only after verification were the AI - generated outputs incorporated into our work.

Compliance with COMAP AI Use Policy: We strictly adhered to the COMAP AI use policy. AI tools were not used to generate complete sections of our report. All written content in our submission, such as the description of the model - solving process, sensitivity analysis, and discussion of results, was created by our team members. The use of AI tools was only for the purpose of assisting in research, analysis, and idea - generation, which fully complied with the competition's regulations.

In conclusion, our use of Doubao and Kimi in this competition was a well - planned and controlled process. It effectively enhanced our research efficiency and the quality of our work while ensuring the originality and compliance required by the competition.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

关注数学模型
