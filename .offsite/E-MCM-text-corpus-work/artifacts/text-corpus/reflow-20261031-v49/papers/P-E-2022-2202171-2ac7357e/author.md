Problem Chosen 2022

MCM/ICM

Summary Sheet

Summary

Carbon neutrality is mainly achieved by reducing carbon emission and increasing carbon sequestration. Forests have an important impact on enhancing carbon sequestration. In this paper, we developed a forest system carbon sequestration prediction model and a forest value balance decision model to study the carbon stock changes of forest system (forest and forest products) and the optimal management plan, and to reveal the beneficial effects of certain deforestation on the carbon sequestration of forest system. In Task1, the change of carbon stock in the forest growth cycle satisfies the logistic law, so we obtain the deforestation intensity and the age of deforestation when the forest is stable and the carbon sequestration is maximum. In order to accelerate forest restoration, new trees need to be planted in the deforested area. Thus, forest system carbon sequestration prediction model is developed. We explored the effects of deforestation interval and forest size on carbon stock, and obtained the optimal management scheme. The results show that the optimal forest management plan is to cut old-growth trees annually, to produce high-lived forest products, to set the cutting intensity at half the inherent growth rate of forest carbon stocks, and simultaneously to plant both the cut and increased areas. Under our optimal scenario, Beijing's deforestation is stabilized at 6 3 , and carbon neutrality is achieved around 2063. 3.2 10 m  In Task2, considering the social demand, economic benefits and ecological influence of forests, forest value balance decision model is constructed and the balance point between the values is studied. And we analyze the scope of application of management plans and the prerequisites for no deforestation. Using genetic algorithms and characteristic parameters of each forest, we determine the optimal management plans and transition points for forests in different temperature zones and forests with different uses. The results indicate that our model is mainly applicable to general forests. Some forests can not be deforested for biodiversity or cultural reasons. The transition points in optimal management plans of different types of forests are different, and the transition points can be divided into phased and final. However, all types of forests can effectively increase or be in a stable state of carbon sequestration while satisfying social needs under optimal plans.

In Task3, we choose Tien Shan forest as the research object. Based on the above decision model, we obtain the optimal forest management plan when each value of Tien Shan forest is balanced, and the change of its carbon stock in the next 100 years. The results show that the optimal management plan is to carry out annual felling of old trees and produce long life forest products, and to plant the felled areas. Under the optimal plan, the economic benefits of the Tien Shan forest stabilize at 8 , the carbon stock increases year by year and stabilizes at 1.52 10 USD  7 . The logging volume gradually gets to meet the demand and eventually there is a 11 10 tC  surplus. In addition, we explore the transition strategy of extending the logging interval by 10 years to ensure the growth of the forest and meet the demand of the society for forest products.

In Task4, based on the above models and conclusions, a non-technical newspaper article is written to reveal that a certain amount of deforestation is beneficial for increasing forest carbon sequestration and achieving carbon neutrality.

1. Introduction

1.1 Background

With the increased attention to environmental issues, how to achieve carbon neutrality or even negative carbon emissions has become a hot research topic. Carbon neutrality means that the emission and absorption of carbon dioxide or greenhouse gases can offset each other positively and negatively within a certain period of time. In order to achieve carbon neutrality and mitigate the impact of climate change, we need to further improve carbon sequestration while reducing carbon emissions.

As the main carbon reservoir of terrestrial ecosystems, forests play a key role in maintaining the global carbon balance and mitigating climate change by fixing atmospheric CO2 in vegetation and forest products through photosynthesis. Afforestation is the most common forest management measure, which can effectively expand the forest area, promote the absorption of atmospheric CO2 by forests, and mitigate climate change with great cost advantages.

In fact, appropriate harvesting in forest management strategies is beneficial for carbon sequestration. Forest products sequester CO2 during their life cycle, and some of them outlive the trees, and carbon sequestration can be achieved over time due to the growth of young trees after deforestation. However, excessive logging can limit carbon sequestration. Forest managers must therefore consider multiple perspectives and balance the value of forest products against the value of forests as living organisms to sequester carbon.

1.2 Our work

Based on the characteristics of forest carbon sequestration, we constructed a carbon sequestration model under ecological optimum conditions to predict the carbon stock changes of forests and forest products as well as to explore the optimal forest management plan. Then, we integrated the values of social demand, economic benefits, and ecological influence of the forest and constructed a multi-objective optimization model to analyze the optimal forest management plan and the transition point. Finally, we apply the above model to different forests to predict their carbon sequestration and find the optimal plan.

We will proceed as follows for the sake of tackling these problems:

State assumptions and making statements. We ignore some relevant but insignificant  effects and impose some restrictions on our core approaches to predict carbon sequestration and explore optimal management plans, allowing for simplification. We will then list some notations that are important for us to clarify the models and define them.

Establish the prediction model of the carbon sequestration of the forest system. The  carbon stock changes in the life cycle of the forest are in accordance with the logistic model, which leads to the optimal logging intensity model and the carbon stock prediction model of the forest system (forest and forest products). We analyze the carbon stock changes under different scenarios when the logging intensity is optimal, and explore the optimal forest management plan.

Establish a value balance decision model for the forest. Analyze the value of forests  from three perspectives: social demand, economic benefits, and ecological influence.

To find the balance between each value, a multi-objective optimization model is developed. The scope of application of the management plan obtained from this model is explored, as well as the specific conditions when no deforestation takes place. The transition points of the management plans corresponding to each type of forest are also analyzed.

Apply the above model to a specific forest. To investigate the optimal forest  management plan and the carbon stock of the forest system after 100. And analyze the transition strategy required if the logging interval is extended by 10 years, under the criteria of meeting social needs and ecological requirements.

Sensitivity analysis and model evaluation. With the evaluation criteria defined before,  we evaluate the reliability of our model and do the sensitivity analysis. Then, we will discuss the strengths and weaknesses about our model.

Write non-technical newspaper articles. Explain the significance of harvesting on  forest carbon sequestration based on the above model with conclusions. Help forest managers to make optimal management plans.

The whole modeling process can be shown as follows：

2. Assumptions and Justification

To simplify the given problems and modify it more appropriate for simulating real-life conditions, we make the following basic hypotheses, each of which is properly justified.

We assume the forest as a whole unit, without considering the differences in areas  within the forest. This assumption is a prerequisite for our in-depth study. This is because for forests covering a wide area, trees grow differently with different natural conditions such as latitude and altitude.

We assume that the profits from buying and selling timber are consistent across  regions within a country. Profits for forest products produced from ordinary forests should fluctuate above and below the same price, without considering special forest products.

3. Notations

We list the symbols and notations used in this paper in Table 1.

Symbols Definition x Carbon stock of the forest ( ) f x Carbon sequestration rate r Inherent growth rate of the forest N The maximum carbon storage of the forest h Carbon stock of felled trees P Carbon stocks in forest systems

4. Forest System Carbon Sequestration Prediction Model

Forests sequester carbon in living plants and forest products through photosynthesis, and a certain amount of deforestation is beneficial for carbon sequestration. Therefore, this task considers the forest and forest products as a system and develops a carbon sequestration prediction model to predict the carbon stock changes in the forest and forest products over a certain period of time and to select the most effective forest management plan for carbon sequestration.

4.1 Carbon stock changes in forest systems

For the system made up of forest and forest products, it is carbon cycling all the time, as shown in Fig.2. Forests increase their carbon stocks by sequestering carbon dioxide in their bodies through photosynthesis. When trees are created into products, carbon is sequestered in forest products. Carbon sequestration in that forest can be increased by means of seed loading, etc. In contrast, the respiration of the forest, consumption during production, and loss of products all carry out carbon emissions, thus reducing the carbon stock of the forest and forest products as a whole.

4.1.1 Characteristics of temporal changes in forest carbon stocks

According to the study, the carbon stock per unit area of forest, i.e. carbon density, is different for different age groups. As the growth time increases, the carbon density of the forest also increases and stabilizes at maturity[1]. Although the carbon stock of mature forests is larger than that of young forests, because the growth of trees in mature forests has basically stopped and the carbon stock is in a stable stage, the effect of CO2 absorption in mature forests on the atmosphere is not obvious. As the forest grows, its carbon sequestration capacity per unit leaf area continues to increase, and when it reaches its peak growth period, the carbon sequestration capacity per unit leaf area is the strongest, and then the carbon sequestration capacity per unit leaf area continues to decrease as the forest matures; when the tree is fully mature, the carbon sequestration capacity per unit leaf area continues to decrease. When the trees are fully mature, the carbon sequestration capacity per unit leaf area of the trees decreases to the lowest[2].

Based on the changes of carbon stock and carbon sequestration rate in different growth periods of the forest, we set the changes of carbon stock with time in the undisturbed forest to satisfy the logistic model, as shown in Fig.3. From this, we can obtain the mathematical expression of carbon sequestration rate as follows:

dx x (1) ( ) (1 ) f x rx    dt N where, is the amount of carbon sequestered per unit time growth, is the carbon ( ) f x x stock of the forest, r is the inherent growth rate of the forest, and is the maximum N carbon storage of the forest, i.e., the carbon stock of the forest at full maturity.

4.1.2 Forecast of carbon stock in forest system

(1) Carbon stock of the forest When there is no human interference such as logging, the change of carbon stock of the forest satisfies the logistic model rule. However, based on the law of change in the carbon sequestration capacity of the forest and the fact that forest products still sequester carbon during their life cycle, a certain degree of deforestation is required to make the forest sequester as much carbon as possible. We set the carbon stock of the felled trees to be proportional to the carbon stock of the whole forest.

(2) ( ) h x Ex 

is the carbon stock of cut trees and E is the cutting intensity. where, ( ) h x Carbon sequestration in forests can be increased by cutting old trees with weak carbon sequestration capacity, but it needs to be ensured that the forest can grow stably, i.e., the carbon stock within the forest is stable: Equilibrium conditions: (3) ( ) ( ) f x h x 

As a result, the deforestation intensity condition E in the case of stable forest growth r  can be obtained, as shown in Figure 4. Since the carbon sequestration rate in the forest is the fastest when the carbon stock is half of the maximum carbon stock, the optimal deforestation intensity obtained for a stable forest with optimal carbon sequestration is:

r (4) E  2

In summary, the carbon stock of the forest for the current year can be obtained from the carbon stock of the previous year and the inherent growth rate of the forest:

(5) ( ) ( ) x x f x h x    1 1 1 i i i i   

where, is the forest carbon stock in year i . ix  1 In order to restore the forest faster and to increase the carbon sequestration in the forest, the deforested area can be planted with young trees, when the intrinsic growth rate of the forest will become larger, the carbon sequestration rate will increase and the forest carbon stock will change:

 (6) ( ) ( ) x x f x h x    1 1 1 1 i i i i    

 is the rate of carbon sequestration when the intrinsic growth rate becomes r. where, ( ) f x (2) Carbon stock of forest products Without considering the actual demand of the society, all the cut wood is made into forest products with long life cycle, and only the carbon stock depreciation at the time of production is considered without considering the carbon stock depreciation in the process of use. Then the carbon stock of forest products satisfies： (7) ( ) P h x P     1 1 i i i  

where, ( ) is the cumulative carbon stock of forest products in year t and  is the P t discount rate in production.

In summary, the maximum carbon stock of the forest system obtained by controlling the amount of cutting under the conditions of stable forest growth is： (8) ( ) ( ) ( ) s t x t P t  

4.2 Forest management plan selection

Based on the research of Feng Zhang on the carbon stock of Beijing forest, the carbon stock of Beijing forest in 2008 was 7.11 Mt, and the carbon density of mature forest was 50 MgC/hm2. Therefore, Based on the above equation of optimal logging intensity, the change in carbon stock of the forest system can be predicted under different logging intervals corresponding to the optimal logging scenarios with constant forest area. However, the actual forest area in Beijing is increasing year by year and the upper limit of the estimated area is 800,000 hm2[3]. Therefore, we solve for the carbon stock change under the optimal logging scenario when the forest area increases. The results are shown in Fig.5.

is optimal. Grey shading shows the carbon stock of new forests.

As shown in Fig.5, the carbon stock of the forest system at the optimal cutting intensity varies with different cutting intervals and different forest areas. The carbon stock is the largest when the forest is cut every year and the forest area increases every year. The carbon stock in the forest system increases slowly and eventually level off when no deforestation occurs. At 5-year or 10-year intervals, carbon stocks increase slightly faster than without deforestation, but eventually remain at a lower rate of sequestration. At the time of annual deforestation, there is a significant increase in carbon stock and the rate of carbon sequestration is more stable. When the forest area becomes larger while cutting each year, the carbon stock is significantly higher than the other cases with optimal cutting intensity, and the carbon sequestration rate is also significantly higher and tends to be stable.

Therefore, in terms of carbon sequestration, under the condition that forest growth is guaranteed, forest managers cut mature trees every year according to the cutting scheme obtained from the optimal cutting intensity formula, and plant the cut area, while increasing the forest area year by year up to the upper limit. At this point, the forest system is sequestering the most carbon. This is the optimal forest management plan.

amount of wood cut.

As shown in Fig.6, the amount of wood cut per year increases year by year and stabilizes 6 3 after about 2060, with the carbon stock of wood cut per year being 2 Mt, i.e. of 3.2 10 m  volume. As the forest area increases year by year, the increment of wood cut per year also increases year by year; after the forest area reaches the upper limit, the amount of wood cut per year increases year by year, but the increment decreases year by year.

The research results of the Chinese Academy of Sciences in 2018 indicate that forests are the main carbon sink, and the amount of carbon that needs to be sequestered is about 24% of all carbon emissions. Therefore, based on the carbon emission data of Beijing over the years, we discuss the future trend of carbon emissions that need to be sequestered by Beijing's forests under different policies[8]. Combined with the optimal forest management plan, the future changes of carbon dioxide in Beijing's atmosphere are studied, as shown in Fig.7.

As shown in Fig.7, carbon emissions continue to increase in the absence of intervention, and carbon neutrality cannot be achieved in the future. Under a moderate level of policy intervention, carbon neutrality will be achieved after the 22nd century. Under the strong policy intervention scenario, the Beijing forest could be carbon neutral by about 2063, which is similar to the year China achieves its carbon neutrality goal. In reality, the changes in carbon emissions that need to be sequestered in Beijing's forests are similar to the simulated scenario of strong intervention, so Beijing's current intervention policy is better and is expected to achieve carbon neutral by the specified time.

carbon emissions that could be reduced with policy intervention

5. Management Plans Balancing The Values of The Forest

This task constructs a multi-objective optimization model that is used to synthesize various values of the forest and develop an optimal forest management plan. Also, the scope of application of the decision model is explored, as well as the scenarios of forests that are not subject to deforestation. It also investigates the determination of transition points of management plans for different forests.

5.1 Forest value balance decision model

Forests purify the air, regulate the climate, and provide timber. Its value is reflected in social, economic and ecological dimensions. Therefore, we analyze the way to balance the various values of forests in a comprehensive way from three perspectives: social needs, economic benefits and ecological influence.

5.1.1 Objectives

(1) Social demand Forest products are necessary for the survival of society, so the felling of trees needs to meet social demand as much as possible. There are many types of forest products, and to simplify the model, we divide forest products into those that depreciate year by year (e.g., furniture) and those that depreciate entirely in the current year (e.g., fuel), based on the depreciation of forest products. From this we can obtain the social demand target for forests:

(9) min T Z T Z    1 1 2 2 i i i i

where, and are the production of entirely depreciated products and year-by-year 1iT iT 2 depreciated products in year i , respectively; and are the demand of entirely 1iZ iZ 2 depreciated products and year-by-year depreciated products in year i , respectively. (2) Economic benefits To simplify the model, this paper only considers the net profit of producing forest products and the cost of planting trees. From this, we can obtain the economic efficiency target of the forest as:

(10) max T v T v W   1 1 2 2 i i i

where, and are the net profit per unit of production for the entirely depreciated 1v 2v product and the year-by-year depreciated product, respectively, and is the cost of planting W i trees per unit area. (3) Ecological influence Forests have many ecological values, such as climate regulation, wind and sand control, etc. Forests are the largest carbon reservoir in terrestrial ecosystems. Therefore, this paper focuses on the effect of carbon sequestration in forest systems (forests and forest products). This results in the following ecological influence objectives for forests:

(11) max x P  i i

where, is the carbon stock of the forest in year i and iP is the total carbon stock of all ix remaining forest products in year i .

5.1.2 Constraints

For a forest, its annual carbon stock is determined by the carbon stock remaining in the previous year, the carbon stock added in that year, and the carbon stock in the wood cut, which is obtained from the model in Task 1： x  (12) ( ) (1 ) x x f x h x r x h        i 1 1 1 i i i i i i i    N where, is the new carbon stock in year i and is the carbon stock in the wood ( ) f x  ih 1 i cut in that year. r is the inherent growth rate of the forest after planting and is the N maximum carbon stock of the forest.

(13) N S    all

where, is the carbon density of the forest at maturity, the total area of the forest. S all The carbon stocks of forest products are inevitably depleted both during production and during use. There is no surplus of products that are all depleted in the current year. From this, we can obtain the carbon stock of forest products remaining in each year:

p p h    1 2 i i i (14) (1 ) P P p     1 2 i i i  where,  is the inherent rate of depreciation during production and is the rate of  depreciation during use. and are the carbon stocks of the two products produced in 1ip ip 2 year i .

Based on the characteristics of carbon stock changes during the forest growth cycle, the harvesting intensity should not exceed the intrinsic growth rate in order to maintain forest growth h  (15) r  i x i The cost of planting trees is determined by the cost of planting trees per unit area and the size of the felling area. In order to secure as much carbon sequestration as possible, therefore, mainly mature trees with weak carbon sequestration capacity are cut down. Therefore, the cost of planting trees is:

h (16) W w S w     i , i i new p  The forest stock is mainly the stock of wood, and the stock of wood is proportional to the carbon stock in wood, so the for relationship between the carbon stock of the produced product and the production is obtained as follows:

 (17) 1,2 T p j   ij ij  where,  is the storage volume per unit area of the forest.

Of course, the annual carbon stock of the trees cut should not exceed the existing carbon stock of the forest, the economic efficiency of the whole production process should not lose money at least, and the production and demand of forest products should not be too much different according to the actual situation:

h x  i i (18) 0 T V T V W    1 1 2 2 i i i (0.5 ,1.5 ) T Z Z  ij ij ij In summary, we obtain the forest integrated value balance decision model as： min T Z T Z    1 1 2 2 i i i i （19） max T V T V W   1 1 2 2 i i i max x P  i i x   (1 ) x x r x h     i  1 i i i i  N  h   r  i  x i  p p h     1 2 i i i  (1 ) P P p      1 2 i i i  h  . . s t W w   i  i     T p   ij ij    0 T v T v W    1 1 2 2 i i i  h x  i  (0.5 ,1.5 ) T Z Z   ij ij ij 

5.2 Scope of application of the plan and the premise of no logging

(1) Analysis of plan applications for different forests According to the use of forests, we classify forests into five categories: protection forests, timber forests, economic forests, charcoal forests and special purpose forests. The decision model we developed is applicable to different types of forests.

Protective forests: Forests whose main purpose is protection, including water  conservation forests and soil and water conservation forests. For this type of forest, the forest management plan obtained from the above decision model cannot be used. The reason is that for protection forests, the main purpose is ecological and there is no need to consider social needs and economic benefits. It is only necessary to ensure that the forest growth is stable and the carbon sequestration is high and the protection purpose is achieved. The target strain of the decision model at this point is:

max x P  i i (20) max Q i where, is the degree of protection Q i Timber forest: The forest whose main purpose is to produce wood, including bamboo  forest whose main purpose is to produce bamboo timber, etc. For this forest, the forest management plus care obtained from the decision model cannot be used directly. Because this forest mainly produces timber, it is a forest product that depreciates carbon stock year by year, so products that are entirely depreciated in the current year in the model should be removed from consideration, i.e. set . 0 iZ  1 Economic forests: Forests with the main purpose of producing fruits, edible oils,  beverages, spices, industrial raw materials and medicinal herbs, etc. For this type of forest the forest management plan obtained from the decision model cannot be used. This is because the forest products we set up in the model are considered to be products produced by cutting wood, and economic forests are not in our consideration.

Fuelwood forests: Forests whose main purpose is to produce fuel. For this forest, the  forest management plus care obtained from the decision model cannot be used directly.

Because this forest mainly produces fuel, it is a forest product that all the carbon stock is depreciated in the current year, so the product that is depreciated year by year in the model should be deleted from consideration, i.e. set . 0 iZ  2 Special purpose forests: Forests with the main purpose of national defense,  environmental protection, scientific experiments, etc., including national defense forests, experimental forests, mother forests, forests of nature reserves, etc. The model we build is based on the general forest, and these forests have their own special purposes, and their planning considerations have their own biased perspectives, so our decision model to get the management plan cannot be applied to this forest. (2) Prerequisites for no logging The value balance decision model of the forest we have developed is an optimal forest management plan obtained by balancing the values of social needs, economic benefits, and ecological influence of a normally growing common forest. However, for some special forests, their values may focus on ecological aspects or their unique values, and these forests cannot be deforested when the expression of values and deforestation contradict each other.

Transitional deforestation: When , it indicates that the carbon stock in the ix x   lower limit forest is less than the lower limit, when the forest is in a period of transitional deforestation. For the transitional deforestation, it is not possible to continue to cut down again for social needs, which will lead to the aggravation of ecological harshness and the sharp weakening of its ability to regulate climate and prevent wind and sand. Therefore, forest managers should focus on ecological restoration rather than logging in the early stage of transitional deforestation.

Ecological reserve forest: For ecological reserve, the forest focuses on the ecological  impacts, do not consider the social needs and economic benefits, so in order to protect its biodiversity, protect rare species and other roles, the ecological reserve can’t be cut down.

Endangered species forests: For endangered trees, their wild populations are small and  in danger of extinction for a considerable period of time. Therefore, forest managers are mainly concerned with the conservation role of such trees and ensure their existence. The number of endangered trees is already very small, so of course they cannot be cut down.

Minority forests: If the forest provides a place for minorities to live, such as the Amazon  forest, there are 20 million indigenous people who have called the Amazon River basin home for generations and have never had contact with modern society. Therefore, this type of forest cannot be deforested at will.

5.3 Transition point analysis

Different forests have different characteristics with different growth conditions, major tree species, product uses, etc. Therefore, there is no one transition point that can be applied to all forests. Specific parameters in the model need to be determined according to the characteristics of each forest, such as making the inherent growth rate of the forest, carbon density at maturity, etc., and then the transition point for its optimal solution is obtained by the model. This task analyzes the determination and difference of transition points for different geographical locations as well as forests with different uses.

5.3.1 Genetic algorithm for solving the optimal solution

Various possible forest management plans are taken as individuals, and the cutting volume of two forest products is taken as genes, thus forming a genetic population. Using the planning objective as the fitness function, the optimal forest management plan that balances the various values of the forest can be solved by the genetic algorithm with the adaptation of the constraints. The process is shown in Fig.9.

According to the research of Zhou Jian et al. on forest carbon sink[4] and the data provided by FOA[5], the initial parameters for solving the optimal plan are set, as shown in Table 2.

S Z Z 1v 2v Parameters 1 2 all Value 4 2 4 3 4 3 3 3 50 10 hm 160 10 m 400 10 m 675 / 450 / USD m USD m      w 0x  Parameters 15Mt Value 0.95 0.95 3 3 3 2 3 / 8 10 /  USD m m m 

5.3.2 Transition point analysis of different temperature zone forests

The main tree species of different temperature zone forests are different. In this paper, we mainly discuss the transition points of management plans for subtropical, temperate and sub-frigid forests. The corresponding forests are evergreen broadleaf forest, deciduous broadleaf forest and mixed coniferous forest.

and the intrinsic growth rate rare different for different forest The carbon density  maturity periods, therefore the forest management plans obtained are different and the transition points are different. Referring to Zhou Yurong et al. for the carbon stock study of each temperature zone forest[6], the corresponding modified values of parameters for each temperature zone forest are shown in Table 3.

Forest subtropical forest temperate forest sub-frigid forest  80 50 60 r 0.4 0.4 0.5 Therefore, the optimal forest management plan that balances each value of the forest and the corresponding changes in the carbon stock of the forest system (forest and forest products) can be obtained based on the model. The calculation results are shown in Fig.11.

(a) Carbon stock (b) Transition points

for optimal management options

As shown in Fig.11, under the optimal forest management plan obtained from the decision model, the carbon stocks of the forest systems in all three different temperature zones continue to increase and then gradually level off. This indicates that when using the obtained management plan, it is still possible to increase the carbon sequestration of the forest while meeting the needs of society. This further validates the optimality of the scheme and the benefits of a certain amount of deforestation.

The management plans for forests in different temperature zones are different, but the 6 3 final deforestation amount is stable at , which may be related to the initial set of 5 10 m  consistent forest area. The management plans for forests in different temperature zones are divided into two types of transition points, namely the phased transition point and the final transition point. In this case, the subtropical forest reaches the staged transition point in about 8 years, and the first significant increase in deforestation is achieved. It reaches the final transition point in the 23rd year and thereafter enters a stable logging phase. Similarly, temperate forests start with a linear increase in deforestation and remain stable between the first and second transition points, after which deforestation increases until it plateaus. Sub-frigid forests, on the other hand, do not have a clear transition point and reach the final transition point after about 39 years. The optimal management plan for forests in different geographical locations differs and the transition points also differ, so it is necessary to obtain parameters based on the characteristics of specific forests and bring them into the model to obtain the optimal plan as well as its transition points.

5.3.3 Transition point analysis of timber forests and charcoal-fuel forests

Timber forests and charcoal-fueled forests have different types of trees and therefore and intrinsic growth rate rat maturity. Charcoal-fueled forests different carbon density  are mainly fast-growing trees used for burning, while timber forests are mainly robust trees used for wood production. Therefore, the social demand for timber and charcoal fuelwood forests varies, as does the cost of planting them. The parameters are modified as in Table 4.

w Forest Social demand r  0 iZ  Timber forests 0.3 50 3 3 / USD m 1 0 iZ  Charcoal-fueled forests 0.9 40 3 2 / USD m 2

As a result, the optimal forest management plan that balances each value of the forest and the carbon stock of the forest system (forest and forest products) under the optimal plan can be obtained according to the model. The results are shown in Fig.12.

(a) Carbon stock (b) Transition points

As shown in Fig12, under the optimal management plan, the amount of carbon sequestered in timber forests increases year by year and eventually stabilizes, while the amount of carbon sequestered in charcoal-fueled forests is always stable, i.e., the forest growth in charcoal-fueled forests is always stable. And the cutting volume of charcoal-fueled 6 3 forests is stable at , which can meet the social demand it supplies or even have a 4.2 10 m  surplus, and there is no transition point. The cut volume of timber forest increases from 3*106 year by year and finally stabilizes at 6 3 . There is a transition point in about 23 years. 5 10 m  The transition point is different for timber forests and charcoal forests, which have different uses. The optimal plan and its transition points need to be obtained for a specific forest based on the characteristic parameters of the forest.

6. Forest Management Plan for Tien Shan

6.1 Carbon stock and management plan of Tien Shan

The Tien Shan Mountain stretches across the central part of Xinjiang. Spruce is the most important zonal forest vegetation in the Tien Shan Mountains, with an area of about 4 2 , accounting for 44.9% of the natural forested area in Xinjiang, and is the main 52.84 10 hm  material body of the forest ecosystem in the Tien Shan Mountains and even in Xinjiang. The mild and humid habitat of the Tien Shan mountain belt provides a good place for the growth and development of snowy spruce, which leads to fast growth, high density and high lumbering rate. The trees here are 50-60 meters tall, with annual rings of 300-400 years or more. It can produce more than 1000 m3 of wood per hectare[7], and its wood is excellent, tough and durable, mainly used for furniture and other forest products.

Because of the characteristics of forest products in Tien Shan, the demand for the entire depreciated forest products in the year is therefore 0, i.e. . Based on the study of Xu et 0 Z  1 al. on the carbon stock of Tien Shan forest and the data support of FOA[5], we can get the initial parameters of Tien Shan forest, as shown in Table 5.

 S Z 2v Parameters r 2 all Value 0.385 4 2 2 3 3 52.84 10 hm 112.53 /t hm 413.86m 465 / USD m   w 0x  Parameters * 53.14Mt Value 0.95 0.95 * 3 3 / USD m

From this, the optimal forest management plan that balances each value of the forest and the carbon stock of the forest system under the optimal plan can be obtained according to the model. The results are shown in Fig.13.

(a) Ecological anf ecconomic value (b) Social value

As shown in Fig.13, the optimal management scheme of Tien Shan forest after considering social demand, economic benefits and ecological influence is obtained by the model - annual felling of old trees and production of long life forest products, and planting of felling areas, with the felling volume increasing year by year, as shown in the figure. Under this scenario, the carbon stock of the forest system increases year by year and finally stabilizes at 7 . The economic efficiency is a stable and profitable state, with an 11 10 tC  8 annual profit of about . the felling volume increases year by year, from 1.5 1.55 10 USD   slightly not meeting the demand at the beginning to finally stabilizing at 6 3 , with a 5.2 10 m  surplus compared to the demand of 6 3 . A good balance is reached between the 4.13 10 m  three, so this scheme is the optimal one.

6.2 Transition strategy to extend the 10-year cutting interval

The longer 10-year interval, the greater increase in the need to cut at once, and the greater ecological and sustainable impacts of the direct shift require the setting of a transition strategy. As the forest changes from an annual cutting management plan to a decadal cutting management plan, it needs to be modified on the basis of the above model to ensure healthy and sustainable growth of the forest, as well as to meet the requirements of social needs and other aspects.

Gradual increase in cutting intervals. For example, a policy of cutting once every two to  four years should be implemented first, and the forest area should be continuously expanded. When the forest area can ensure that the ecosystem can adapt to a larger cutting interval, the cutting interval should be adjusted until it becomes once every ten years.

Balance timber supply through imports. Considering the demand for timber in the area in  the interval year (the year of non-cutting), it is necessary to meet the demand for timber in the interval year as much as possible in the year when the trees are cut. Therefore, the social demand objective in the integrated forest value balance decision model is changed to：     (21) min T Z T Z    1 1 2 2 i i i i

where, 1iT, iT is the volume of two forest products cut at the interval of harvesting. 2 1iZ, iZ is the total demand for the interval year. 2 For some of the smaller forests, it is not possible to meet the demand for many years by  cutting them once. In such cases, the supply deficit should be made up locally by importing timber. Therefore, the above objective is further changed to： h ( ) W w S    i , i i expand  (22) ( ) N S S     , i all i expand where, is the expanded forest area. S ,i expand Tree species with larger  can be introduced, the reason being that a smaller number of  trees can be used to meet the demand; or tree species with larger r can be introduced, allowing for a faster rate of forest recovery.

7. Sensitivity Analysis

In real life, statistics are often inaccurate and there may be some biases in the inputs to our models. These biases may affect the results of our model. In order to test the robustness of our model, in this section, we will analyze the sensitivity of our decision model in the analysis. The results of the sensitivity analysis show that our model shows perfect stability.

Forest product depreciation rates have a significant impact on our analysis of optimal forest management plans. Different depreciation rates affect the carbon content of forest products sequestered, which may lead to misjudgment of the optimal management plan and make the balance between the various values of the forest problematic. The product depreciation rate is represented in the model as a constant . Therefore, we will investigate the depreciation rate in more depth. Since in the model mainly represents the depreciation  rate of long-lived forest products such as furniture, the depreciation rate is not very large. We change the value of and analyze the changes that make the carbon stock of the forest  system (forest and forest products). If the fluctuation is too large, we should reconsider the model.

(a) Carbon stock (b) Cutting volume

As shown in Fig.14, our decision model is stable. When the discount rate fluctuates, the amount of deforestation and the carbon stock of the forest system fluctuate somewhat, but the fluctuations are not significant. When the discount rate fluctuates up and down, the carbon stock also fluctuates, but overall still both show an increasing to steady trend. There is also a relative decrease in the amount of cutting, but when the carbon stock gradually increases to a stable level, the amount of cutting also increases and finally stabilizes at the same level, which 6 3 can meet the demand of . Therefore, despite the fluctuation of the depreciation 4.13 10 m  rate, our decision model can still obtain the optimal forest management plan that balances all values of the forest. This demonstrates the stability of the model and can solve real-life practical problems.

8. Strengths and Weaknesses

8.1 Strengths

Considering the trend of carbon stock growth of forest system is in accordance with the  law of logistic model, the optimal strategy to maintain the ecological balance of forest is derived by combining the carbon stock of forest products caused by deforestation, and the method is innovative. In addition to analyzing the ideal strategy considering only the forest system, the social  and economic aspects are also considered for multi-objective optimization; at the same time, the optimal strategies for different kinds of forests and forests in different temperature zones are also analyzed, which is comprehensive and has application significance. The model is brought into the data of Tien Shan forest for verification, and the results are  consistent with reality, and the model is more accurate.

8.2 Weaknesses

Since some parameters are estimated values (e.g. wood demand for fuel is determined  from wood fuel data provided in FAO, while in reality wood chips, etc. are also considered as fuel), the results of the model may have small deviations. If more detailed data can be found, our model can be verified more precisely. In reality, the way trees are planted (spaced or concentrated), etc., may have an impact on  the parameters of the model, which is ignored in this paper. The model can be improved by measuring various parameters of the trees.

9 Non-technical Newspaper Article

The carbon cycle refers to the exchange of carbon in the biosphere, lithosphere, hydrosphere and atmosphere of the Earth, and the cycle continues with the movement of the Earth. The carbon cycle in the biosphere mainly involves green plants absorbing carbon dioxide from the atmosphere through photosynthesis and converting it into glucose, which is then used by organisms to synthesize other organic compounds. Organic compounds are passed through the food chain and become part of other organisms such as animals and bacteria. Carbohydrates in living organisms are oxidized to carbon dioxide and water through respiration.

The carbon cycle in nature is balanced, but humans produce large amounts of carbon dioxide when they burn fossil fuels. The concentration of carbon dioxide in the atmosphere rises, which disrupts the original balance of nature and leads to global

warming with a series of negative effects. Thus, controlling carbon dioxide emissions is a key measure to curb global warming. The Report on the Impact of Global Warming of 1.5°C above Pre-industrial indicates that to achieve global Levels warming of no more than 1.5°C above pre-industrial levels, net global CO2 emissions must be reduced by about 45% by 2030 compared to 2010, and carbon neutrality should be achieved by 2050.

Forest systems are a key factor in achieving carbon neutrality, and increasing forest carbon sequestration and reducing CO2 emissions are two equally important aspects of climate change mitigation. Forests play an irreplaceable role in carbon sequestration. Terrestrial carbon sequestration can be enhanced through strong measures, such as afforestation and restoration of destroyed ecosystems. The replacement of energy-intensive materials with durable woody forest products and the recycling of harvesting residues can reduce greenhouse gas emissions.

By exploring the role of forests in sequestering carbon, we have discovered a different approach to increasing carbon sequestration in forests than is common: a certain amount of deforestation. Forests sequester carbon dioxide in plants and the products created from them, including furniture, paper, and fuel. These forest products sequester carbon dioxide during their life cycle. When the products outlive the trees that produce them, the forest is sequestering more carbon due to the regrowth of young forests than it would if it were not deforested at all.

Moreover, the change in carbon stocks over the life cycle of a forest follows the logistic law, which states that mature trees have more carbon in their bodies but less carbon sequestration capacity. Therefore, when harvesting, mature trees should be cut down as much as possible and then made into long-lived forest products. This has less impact on the forest's ability to sequester carbon, and the products sequester more carbon and for a longer period of time.

Forest management strategies that include harvesting can be beneficial for carbon sequestration. But over-harvesting can limit carbon sequestration. Forest managers must find a balance between the value of the forest products generated by harvesting and the value of allowing the forest to continue to grow and perform functions such as carbon sequestration.

Therefore, for actual logging plans, practical factors must be considered, such as the use of the forest, its geographic location, the type of tree species, and the benefits and longevity of the forest products.

Forest management strategies that include harvesting can be beneficial for carbon sequestration. Of course, over-harvesting can limit carbon sequestration. And, deforestation also needs to meet economic benefits. Forest managers must find a balance between economics and ecology. Under the condition of stable forest growth (E<r), the logging intensity should be within a certain suitable range, when the upper limit is higher than the upper limit, it will cause ecological transitional logging, while the lower limit is lower than the lower limit, it will cause economic transitional logging.

Therefore, for a forest, in order to increase the carbon sequestration of the forest, logging needs to be included within the management plan, but the specific logging plan, such as the timing of logging, the amount of logging, and the species to be logged, needs to take into account the economic, ecological, and social values of the forest to find a balance.
