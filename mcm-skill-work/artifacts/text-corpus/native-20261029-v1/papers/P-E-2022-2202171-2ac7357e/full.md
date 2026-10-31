# P-E-2022-2202171-2ac7357e

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2022

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | title | pages [1] -->
E

<!-- b000005 | title | pages [1] -->
2202171

<!-- b000006 | prose | pages [1] -->
MCM/ICM

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Better Strategy: Carbon Sequestration by Forests Logging

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Carbon neutrality is mainly achieved by reducing carbon emission and increasing carbon sequestration. Forests have an important impact on enhancing carbon sequestration. In this paper, we developed a forest system carbon sequestration prediction model and a forest value balance decision model to study the carbon stock changes of forest system (forest and forest products) and the optimal management plan, and to reveal the beneficial effects of certain deforestation on the carbon sequestration of forest system.

<!-- b000011 | prose | pages [1] -->
In Task1, the change of carbon stock in the forest growth cycle satisfies the logistic law, so we obtain the deforestation intensity and the age of deforestation when the forest is stable and the carbon sequestration is maximum. In order to accelerate forest restoration, new trees need to be planted in the deforested area. Thus, forest system carbon sequestration prediction model is developed. We explored the effects of deforestation interval and forest size on carbon stock, and obtained the optimal management scheme. The results show that the optimal forest management plan is to cut old-growth trees annually, to produce high-lived forest products, to set the cutting intensity at half the inherent growth rate of forest carbon stocks, and simultaneously to plant both the cut and increased areas. Under our optimal scenario, Beijing's deforestation is stabilized at

<!-- b000012 | prose | pages [1] -->
6 3 , and carbon neutrality is achieved around 2063. 3.2 10 m  In Task2, considering the social demand, economic benefits and ecological influence of forests, forest value balance decision model is constructed and the balance point between the values is studied. And we analyze the scope of application of management plans and the prerequisites for no deforestation. Using genetic algorithms and characteristic parameters of each forest, we determine the optimal management plans and transition points for forests in different temperature zones and forests with different uses. The results indicate that our model is mainly applicable to general forests. Some forests can not be deforested for biodiversity or cultural reasons. The transition points in optimal management plans of different types of forests are different, and the transition points can be divided into phased and final. However, all types of forests can effectively increase or be in a stable state of carbon sequestration while satisfying social needs under optimal plans.

<!-- b000013 | prose | pages [1] -->
In Task3, we choose Tien Shan forest as the research object. Based on the above decision model, we obtain the optimal forest management plan when each value of Tien Shan forest is balanced, and the change of its carbon stock in the next 100 years. The results show that the optimal management plan is to carry out annual felling of old trees and produce long life forest products, and to plant the felled areas. Under the optimal plan, the economic benefits of the Tien Shan forest stabilize at 8 , the carbon stock increases year by year and stabilizes at 1.52 10 USD  7 . The logging volume gradually gets to meet the demand and eventually there is a 11 10 tC  surplus. In addition, we explore the transition strategy of extending the logging interval by 10 years to ensure the growth of the forest and meet the demand of the society for forest products.

<!-- b000014 | prose | pages [1] -->
In Task4, based on the above models and conclusions, a non-technical newspaper article is written to reveal that a certain amount of deforestation is beneficial for increasing forest carbon sequestration and achieving carbon neutrality.

<!-- b000015 | keywords | pages [1] -->
Key Words: Carbon sequestration, Logistic model, Multi-objective decision

<!-- b000016 | prose | pages [2] -->
Content

<!-- b000017 | prose | pages [2] -->
1. Introduction...........................................................................................................................1

<!-- b000018 | prose | pages [2] -->
1.1 Background.................................................................................................................... 1 1.2 Our work........................................................................................................................ 1

<!-- b000019 | prose | pages [2] -->
2. Assumptions and Justification............................................................................................. 2

<!-- b000020 | prose | pages [2] -->
3. Notations................................................................................................................................ 3

<!-- b000021 | prose | pages [2] -->
4. Forest System Carbon Sequestration Prediction Model................................................... 3

<!-- b000022 | prose | pages [2] -->
4.1 Carbon stock changes in forest systems.........................................................................3 4.1.1 Characteristics of temporal changes in forest carbon stocks............................... 4 4.1.2 Forecast of carbon stock in forest system............................................................ 4 4.2 Forest management plan selection................................................................................. 6 5. Management Plans Balancing The Values of The Forest.................................................. 8 5.1 Forest value balance decision model..............................................................................8 5.1.1 Objectives.............................................................................................................9 5.1.2 Constraints........................................................................................................... 9 5.2 Scope of application of the plan and the premise of no logging..................................11 5.3 Transition point analysis.............................................................................................. 12 5.3.1 Genetic algorithm for solving the optimal solution........................................... 13 5.3.2 Transition point analysis of different temperature zone forests.........................13 5.3.3 Transition point analysis of timber forests and charcoal-fuel forests................ 15 6. Forest Management Plan for Tien Shan........................................................................... 16 6.1 Carbon stock and management plan of Tien Shan.......................................................16 6.2 Transition strategy to extend the 10-year cutting interval............................................17

<!-- b000023 | prose | pages [2] -->
7. Sensitivity Analysis..............................................................................................................18

<!-- b000024 | prose | pages [2] -->
8. Strengths and Weaknesses..................................................................................................19

<!-- b000025 | prose | pages [2] -->
8.1 Strengths.......................................................................................................................19 8.2 Weaknesses...................................................................................................................19

<!-- b000026 | prose | pages [2] -->
9 Non-technical Newspaper Article....................................................................................... 20

<!-- b000027 | prose | pages [2] -->
References................................................................................................................................ 22

<!-- b000028 | furniture | pages [3] -->
Team#2202171

<!-- b000029 | furniture | pages [3] -->
Page 1 of 22

<!-- b000030 | heading | pages [3] -->
1. Introduction

<!-- b000031 | heading | pages [3] -->
1.1 Background

<!-- b000032 | prose | pages [3] -->
With the increased attention to environmental issues, how to achieve carbon neutrality or even negative carbon emissions has become a hot research topic. Carbon neutrality means that the emission and absorption of carbon dioxide or greenhouse gases can offset each other positively and negatively within a certain period of time. In order to achieve carbon neutrality and mitigate the impact of climate change, we need to further improve carbon sequestration while reducing carbon emissions.

<!-- b000033 | prose | pages [3] -->
As the main carbon reservoir of terrestrial ecosystems, forests play a key role in maintaining the global carbon balance and mitigating climate change by fixing atmospheric CO2 in vegetation and forest products through photosynthesis. Afforestation is the most common forest management measure, which can effectively expand the forest area, promote the absorption of atmospheric CO2 by forests, and mitigate climate change with great cost advantages.

<!-- b000034 | prose | pages [3] -->
In fact, appropriate harvesting in forest management strategies is beneficial for carbon sequestration. Forest products sequester CO2 during their life cycle, and some of them outlive the trees, and carbon sequestration can be achieved over time due to the growth of young trees after deforestation. However, excessive logging can limit carbon sequestration. Forest managers must therefore consider multiple perspectives and balance the value of forest products against the value of forests as living organisms to sequester carbon.

<!-- b000035 | heading | pages [3] -->
1.2 Our work

<!-- b000036 | prose | pages [3] -->
Based on the characteristics of forest carbon sequestration, we constructed a carbon sequestration model under ecological optimum conditions to predict the carbon stock changes of forests and forest products as well as to explore the optimal forest management plan. Then, we integrated the values of social demand, economic benefits, and ecological influence of the forest and constructed a multi-objective optimization model to analyze the optimal forest management plan and the transition point. Finally, we apply the above model to different forests to predict their carbon sequestration and find the optimal plan.

<!-- b000037 | prose | pages [3] -->
We will proceed as follows for the sake of tackling these problems:

<!-- b000038 | prose | pages [3] -->
State assumptions and making statements. We ignore some relevant but insignificant  effects and impose some restrictions on our core approaches to predict carbon sequestration and explore optimal management plans, allowing for simplification. We will then list some notations that are important for us to clarify the models and define them. Establish the prediction model of the carbon sequestration of the forest system. The  carbon stock changes in the life cycle of the forest are in accordance with the logistic model, which leads to the optimal logging intensity model and the carbon stock prediction model of the forest system (forest and forest products). We analyze the carbon stock changes under different scenarios when the logging intensity is optimal, and explore the optimal forest management plan.

<!-- b000039 | furniture | pages [4] -->
Team#2202171

<!-- b000040 | furniture | pages [4] -->
Page 2 of 22

<!-- b000041 | prose | pages [4] -->
Establish a value balance decision model for the forest. Analyze the value of forests  from three perspectives: social demand, economic benefits, and ecological influence. To find the balance between each value, a multi-objective optimization model is developed. The scope of application of the management plan obtained from this model is explored, as well as the specific conditions when no deforestation takes place. The transition points of the management plans corresponding to each type of forest are also analyzed. Apply the above model to a specific forest. To investigate the optimal forest  management plan and the carbon stock of the forest system after 100. And analyze the transition strategy required if the logging interval is extended by 10 years, under the criteria of meeting social needs and ecological requirements. Sensitivity analysis and model evaluation. With the evaluation criteria defined before,  we evaluate the reliability of our model and do the sensitivity analysis. Then, we will discuss the strengths and weaknesses about our model. Write non-technical newspaper articles. Explain the significance of harvesting on  forest carbon sequestration based on the above model with conclusions. Help forest managers to make optimal management plans. The whole modeling process can be shown as follows：

<!-- b000042 | caption | pages [4] -->
Fig.1 Technology route for the creation of our paper.

<!-- b000043 | heading | pages [4] -->
2. Assumptions and Justification

<!-- b000044 | prose | pages [4] -->
To simplify the given problems and modify it more appropriate for simulating real-life conditions, we make the following basic hypotheses, each of which is properly justified.

<!-- b000045 | prose | pages [4] -->
We assume the forest as a whole unit, without considering the differences in areas  within the forest. This assumption is a prerequisite for our in-depth study. This is because for forests covering a wide area, trees grow differently with different natural conditions such as latitude and altitude. We assume that the profits from buying and selling timber are consistent across  regions within a country. Profits for forest products produced from ordinary forests should fluctuate above and below the same price, without considering special forest products.

<!-- b000046 | furniture | pages [5] -->
Team#2202171

<!-- b000047 | furniture | pages [5] -->
Page 3 of 22

<!-- b000048 | heading | pages [5] -->
3. Notations

<!-- b000049 | prose | pages [5] -->
We list the symbols and notations used in this paper in Table 1.

<!-- b000050 | caption | pages [5] -->
Table 1 Notations

<!-- b000051 | prose | pages [5] -->
Symbols Definition

<!-- b000052 | prose | pages [5] -->
x Carbon stock of the forest

<!-- b000053 | prose | pages [5] -->
( ) f x Carbon sequestration rate

<!-- b000054 | prose | pages [5] -->
r Inherent growth rate of the forest

<!-- b000055 | prose | pages [5] -->
N The maximum carbon storage of the forest

<!-- b000056 | prose | pages [5] -->
h Carbon stock of felled trees

<!-- b000057 | prose | pages [5] -->
P Carbon stocks in forest systems

<!-- b000058 | heading | pages [5] -->
4. Forest System Carbon Sequestration Prediction Model

<!-- b000059 | prose | pages [5] -->
Forests sequester carbon in living plants and forest products through photosynthesis, and a certain amount of deforestation is beneficial for carbon sequestration. Therefore, this task considers the forest and forest products as a system and develops a carbon sequestration prediction model to predict the carbon stock changes in the forest and forest products over a certain period of time and to select the most effective forest management plan for carbon sequestration.

<!-- b000060 | heading | pages [5] -->
4.1 Carbon stock changes in forest systems

<!-- b000061 | prose | pages [5] -->
For the system made up of forest and forest products, it is carbon cycling all the time, as shown in Fig.2. Forests increase their carbon stocks by sequestering carbon dioxide in their bodies through photosynthesis. When trees are created into products, carbon is sequestered in forest products. Carbon sequestration in that forest can be increased by means of seed loading, etc. In contrast, the respiration of the forest, consumption during production, and loss of products all carry out carbon emissions, thus reducing the carbon stock of the forest and forest products as a whole.

<!-- b000062 | caption | pages [5] -->
Fig.2 Schematic diagram of carbon cycle of forest system (forest and forest products)

<!-- b000063 | furniture | pages [6] -->
Team#2202171

<!-- b000064 | furniture | pages [6] -->
Page 4 of 22

<!-- b000065 | heading | pages [6] -->
4.1.1 Characteristics of temporal changes in forest carbon stocks

<!-- b000066 | prose | pages [6] -->
According to the study, the carbon stock per unit area of forest, i.e. carbon density, is different for different age groups. As the growth time increases, the carbon density of the forest also increases and stabilizes at maturity[1]. Although the carbon stock of mature forests is larger than that of young forests, because the growth of trees in mature forests has basically stopped and the carbon stock is in a stable stage, the effect of CO2 absorption in mature forests on the atmosphere is not obvious. As the forest grows, its carbon sequestration capacity per unit leaf area continues to increase, and when it reaches its peak growth period, the carbon sequestration capacity per unit leaf area is the strongest, and then the carbon sequestration capacity per unit leaf area continues to decrease as the forest matures; when the tree is fully mature, the carbon sequestration capacity per unit leaf area continues to decrease. When the trees are fully mature, the carbon sequestration capacity per unit leaf area of the trees decreases to the lowest[2].

<!-- b000067 | prose | pages [6] -->
Based on the changes of carbon stock and carbon sequestration rate in different growth periods of the forest, we set the changes of carbon stock with time in the undisturbed forest to satisfy the logistic model, as shown in Fig.3. From this, we can obtain the mathematical expression of carbon sequestration rate as follows:

<!-- b000068 | prose | pages [6] -->
dx ( ) f x  dt x (1) (1 ) rx    N

<!-- b000069 | prose | pages [6] -->
is the amount of carbon sequestered per unit time growth, where, ( ) f x is the carbon x is the inherent growth rate of the forest, and stock of the forest, r is the maximum N carbon storage of the forest, i.e., the carbon stock of the forest at full maturity.

<!-- b000070 | caption | pages [6] -->
Fig.3 Schematic diagram of forest carbon stock change pattern

<!-- b000071 | heading | pages [6] -->
4.1.2 Forecast of carbon stock in forest system

<!-- b000072 | prose | pages [6] -->
(1) Carbon stock of the forest

<!-- b000073 | prose | pages [6] -->
When there is no human interference such as logging, the change of carbon stock of the forest satisfies the logistic model rule. However, based on the law of change in the carbon sequestration capacity of the forest and the fact that forest products still sequester carbon during their life cycle, a certain degree of deforestation is required to make the forest sequester as much carbon as possible. We set the carbon stock of the felled trees to be

<!-- b000074 | furniture | pages [7] -->
Team#2202171

<!-- b000075 | furniture | pages [7] -->
Page 5 of 22

<!-- b000076 | prose | pages [7] -->
proportional to the carbon stock of the whole forest.

<!-- b000077 | prose | pages [7] -->
( ) h x (2) Ex  

<!-- b000078 | prose | pages [7] -->
is the carbon stock of cut trees and E is the cutting intensity. where, ( ) h x Carbon sequestration in forests can be increased by cutting old trees with weak carbon sequestration capacity, but it needs to be ensured that the forest can grow stably, i.e., the carbon stock within the forest is stable:

<!-- b000079 | prose | pages [7] -->
Equilibrium conditions:

<!-- b000080 | prose | pages [7] -->
( ) f x (3) ( ) h x  

<!-- b000081 | prose | pages [7] -->
As a result, the deforestation intensity condition E in the case of stable forest growth r  can be obtained, as shown in Figure 4. Since the carbon sequestration rate in the forest is the fastest when the carbon stock is half of the maximum carbon stock, the optimal deforestation intensity obtained for a stable forest with optimal carbon sequestration is:

<!-- b000082 | prose | pages [7] -->
E  r (4) 2

<!-- b000083 | caption | pages [7] -->
Fig.4 Diagram of different deforestation intensity

<!-- b000084 | prose | pages [7] -->
In summary, the carbon stock of the forest for the current year can be obtained from the carbon stock of the previous year and the inherent growth rate of the forest:

<!-- b000085 | prose | pages [7] -->
x x f x   1 i i 

<!-- b000086 | prose | pages [7] -->
is the forest carbon stock in year i . where, ix  1

<!-- b000087 | prose | pages [7] -->
(5) ( ( ) ( ) h x  1 1 i i i  

<!-- b000088 | prose | pages [7] -->
In order to restore the forest faster and to increase the carbon sequestration in the forest, the deforested area can be planted with young trees, when the intrinsic growth rate of the forest will become larger, the carbon sequestration rate will increase and the forest carbon stock will change:

<!-- b000089 | prose | pages [7] -->
x x f   1 1 i i     (6) ( ( ) ( ) x h x  1 1 i i  

<!-- b000090 | prose | pages [7] -->
is the rate of carbon sequestration when the intrinsic growth rate becomes r.  where, ( ) f x (2) Carbon stock of forest products

<!-- b000091 | prose | pages [7] -->
Without considering the actual demand of the society, all the cut wood is made into forest products with long life cycle, and only the carbon stock depreciation at the time of production

<!-- b000092 | furniture | pages [8] -->
Team#2202171

<!-- b000093 | furniture | pages [8] -->
Page 6 of 22

<!-- b000094 | prose | pages [8] -->
is considered without considering the carbon stock depreciation in the process of use. Then the carbon stock of forest products satisfies：

<!-- b000095 | prose | pages [8] -->
P h x    i (7) ( ( ) P  1 1 i i i  

<!-- b000096 | prose | pages [8] -->
is the cumulative carbon stock of forest products in year t and  where, ( ) P t discount rate in production.

<!-- b000097 | prose | pages [8] -->
is the

<!-- b000098 | prose | pages [8] -->
In summary, the maximum carbon stock of the forest system obtained by controlling the amount of cutting under the conditions of stable forest growth is：

<!-- b000099 | prose | pages [8] -->
( ) s t x t  (8) ( ) ( ) ( ) P t 

<!-- b000100 | heading | pages [8] -->
4.2 Forest management plan selection

<!-- b000101 | prose | pages [8] -->
Based on the research of Feng Zhang on the carbon stock of Beijing forest, the carbon stock of Beijing forest in 2008 was 7.11 Mt, and the carbon density of mature forest was 50 MgC/hm2. Therefore, Based on the above equation of optimal logging intensity, the change in carbon stock of the forest system can be predicted under different logging intervals corresponding to the optimal logging scenarios with constant forest area. However, the actual forest area in Beijing is increasing year by year and the upper limit of the estimated area is 800,000 hm2[3]. Therefore, we solve for the carbon stock change under the optimal logging scenario when the forest area increases. The results are shown in Fig.5.

<!-- b000102 | caption | pages [8] -->
Fig.5 Changes in forest system carbon stocks under different logging scenarios when logging effort

<!-- b000103 | prose | pages [8] -->
is optimal. Grey shading shows the carbon stock of new forests.

<!-- b000104 | prose | pages [8] -->
As shown in Fig.5, the carbon stock of the forest system at the optimal cutting intensity varies with different cutting intervals and different forest areas. The carbon stock is the largest when the forest is cut every year and the forest area increases every year. The carbon stock in the forest system increases slowly and eventually level off when no deforestation occurs. At 5-year or 10-year intervals, carbon stocks increase slightly faster than without deforestation, but eventually remain at a lower rate of sequestration. At the time of annual deforestation, there is a significant increase in carbon stock and the rate of carbon sequestration is more

<!-- b000105 | furniture | pages [9] -->
Team#2202171

<!-- b000106 | furniture | pages [9] -->
Page 7 of 22

<!-- b000107 | prose | pages [9] -->
stable. When the forest area becomes larger while cutting each year, the carbon stock is significantly higher than the other cases with optimal cutting intensity, and the carbon sequestration rate is also significantly higher and tends to be stable.

<!-- b000108 | prose | pages [9] -->
Therefore, in terms of carbon sequestration, under the condition that forest growth is guaranteed, forest managers cut mature trees every year according to the cutting scheme obtained from the optimal cutting intensity formula, and plant the cut area, while increasing the forest area year by year up to the upper limit. At this point, the forest system is sequestering the most carbon. This is the optimal forest management plan.

<!-- b000109 | caption | pages [9] -->
Fig.6 Carbon stock of trees cut by the optimal solution. The higher the carbon stock, the higher the

<!-- b000110 | prose | pages [9] -->
amount of wood cut.

<!-- b000111 | prose | pages [9] -->
As shown in Fig.6, the amount of wood cut per year increases year by year and stabilizes 6 3 after about 2060, with the carbon stock of wood cut per year being 2 Mt, i.e.

<!-- b000112 | prose | pages [9] -->
of 3.2 10 m  volume. As the forest area increases year by year, the increment of wood cut per year also increases year by year; after the forest area reaches the upper limit, the amount of wood cut per year increases year by year, but the increment decreases year by year.

<!-- b000113 | prose | pages [9] -->
The research results of the Chinese Academy of Sciences in 2018 indicate that forests are the main carbon sink, and the amount of carbon that needs to be sequestered is about 24% of all carbon emissions. Therefore, based on the carbon emission data of Beijing over the years, we discuss the future trend of carbon emissions that need to be sequestered by Beijing's forests under different policies[8]. Combined with the optimal forest management plan, the future changes of carbon dioxide in Beijing's atmosphere are studied, as shown in Fig.7.

<!-- b000114 | prose | pages [9] -->
As shown in Fig.7, carbon emissions continue to increase in the absence of intervention, and carbon neutrality cannot be achieved in the future. Under a moderate level of policy intervention, carbon neutrality will be achieved after the 22nd century. Under the strong policy intervention scenario, the Beijing forest could be carbon neutral by about 2063, which is similar to the year China achieves its carbon neutrality goal. In reality, the changes in carbon emissions that need to be sequestered in Beijing's forests are similar to the simulated scenario of strong intervention, so Beijing's current intervention policy is better and is expected to achieve carbon neutral by the specified time.

<!-- b000115 | furniture | pages [10] -->
Team#2202171

<!-- b000116 | furniture | pages [10] -->
Page 8 of 22

<!-- b000117 | caption | pages [10] -->
Fig.7 Simulation of future Beijing forest carbon neutrality possibility. Gray shading indicates the

<!-- b000118 | prose | pages [10] -->
carbon emissions that could be reduced with policy intervention

<!-- b000119 | heading | pages [10] -->
5. Management Plans Balancing The Values of The Forest

<!-- b000120 | prose | pages [10] -->
This task constructs a multi-objective optimization model that is used to synthesize various values of the forest and develop an optimal forest management plan. Also, the scope of application of the decision model is explored, as well as the scenarios of forests that are not subject to deforestation. It also investigates the determination of transition points of management plans for different forests.

<!-- b000121 | heading | pages [10] -->
5.1 Forest value balance decision model

<!-- b000122 | caption | pages [10] -->
Fig.8 Diagram of each value of the forest

<!-- b000123 | furniture | pages [11] -->
Team#2202171

<!-- b000124 | furniture | pages [11] -->
Page 9 of 22

<!-- b000125 | prose | pages [11] -->
Forests purify the air, regulate the climate, and provide timber. Its value is reflected in social, economic and ecological dimensions. Therefore, we analyze the way to balance the various values of forests in a comprehensive way from three perspectives: social needs, economic benefits and ecological influence.

<!-- b000126 | heading | pages [11] -->
5.1.1 Objectives

<!-- b000127 | prose | pages [11] -->
(1) Social demand Forest products are necessary for the survival of society, so the felling of trees needs to meet social demand as much as possible. There are many types of forest products, and to simplify the model, we divide forest products into those that depreciate year by year (e.g., furniture) and those that depreciate entirely in the current year (e.g., fuel), based on the depreciation of forest products. From this we can obtain the social demand target for forests:

<!-- b000128 | prose | pages [11] -->
min T  1 i (9) Z Z T Z   1 1 2 2 i i i i

<!-- b000129 | prose | pages [11] -->
are the production of entirely depreciated products and year-by-year where, and 1iT iT 2 depreciated products in year i , respectively;

<!-- b000130 | prose | pages [11] -->
and are the demand of entirely 1iZ iZ 2 depreciated products and year-by-year depreciated products in year i , respectively. (2) Economic benefits

<!-- b000131 | prose | pages [11] -->
To simplify the model, this paper only considers the net profit of producing forest products and the cost of planting trees. From this, we can obtain the economic efficiency target of the forest as:

<!-- b000132 | prose | pages [11] -->
max T v 1 1 i (10) T v W    2 2 i i

<!-- b000133 | prose | pages [11] -->
are the net profit per unit of production for the entirely depreciated where, and 1v 2v product and the year-by-year depreciated product, respectively, and trees per unit area. (3) Ecological influence is the cost of planting W i

<!-- b000134 | prose | pages [11] -->
Forests have many ecological values, such as climate regulation, wind and sand control, etc. Forests are the largest carbon reservoir in terrestrial ecosystems. Therefore, this paper focuses on the effect of carbon sequestration in forest systems (forests and forest products). This results in the following ecological influence objectives for forests:

<!-- b000135 | prose | pages [11] -->
max (11) x x P  i i

<!-- b000136 | prose | pages [11] -->
is the carbon stock of the forest in year i and where, ix remaining forest products in year i .

<!-- b000137 | heading | pages [11] -->
5.1.2 Constraints

<!-- b000138 | prose | pages [11] -->
iP is the total carbon stock of all

<!-- b000139 | prose | pages [11] -->
For a forest, its annual carbon stock is determined by the carbon stock remaining in the previous year, the carbon stock added in that year, and the carbon stock in the wood cut, which is obtained from the model in Task 1：

<!-- b000140 | prose | pages [11] -->
( ) x x f x h    1 1 i i i i   x  (12) (1 ) x r x h      i 1 i i i  N

<!-- b000141 | prose | pages [11] -->
is the new carbon stock in year i where, ( ) f x  1 i cut in that year. r and is the carbon stock in the wood ih is the inherent growth rate of the forest after planting and is the N

<!-- b000142 | furniture | pages [12] -->
Team#2202171

<!-- b000143 | prose | pages [12] -->
maximum carbon stock of the forest.

<!-- b000144 | prose | pages [12] -->
N 

<!-- b000145 | furniture | pages [12] -->
Page 10 of 22

<!-- b000146 | prose | pages [12] -->
(13) S    all

<!-- b000147 | prose | pages [12] -->
where, is the carbon density of the forest at maturity, the total area of the forest. S all The carbon stocks of forest products are inevitably depleted both during production and during use. There is no surplus of products that are all depleted in the current year. From this, we can obtain the carbon stock of forest products remaining in each year:

<!-- b000148 | prose | pages [12] -->
p p

<!-- b000149 | prose | pages [12] -->


<!-- b000150 | prose | pages [12] -->
1 2

<!-- b000151 | prose | pages [12] -->
i i

<!-- b000152 | prose | pages [12] -->
(1

<!-- b000153 | prose | pages [12] -->
P

<!-- b000154 | prose | pages [12] -->
 

<!-- b000155 | prose | pages [12] -->


<!-- b000156 | prose | pages [12] -->
i

<!-- b000157 | prose | pages [12] -->
h

<!-- b000158 | prose | pages [12] -->
 

<!-- b000159 | prose | pages [12] -->


<!-- b000160 | prose | pages [12] -->
i

<!-- b000161 | prose | pages [12] -->
(14)

<!-- b000162 | prose | pages [12] -->
) )

<!-- b000163 | prose | pages [12] -->
P p

<!-- b000164 | prose | pages [12] -->


<!-- b000165 | prose | pages [12] -->
1 2

<!-- b000166 | prose | pages [12] -->
i i

<!-- b000167 | prose | pages [12] -->


<!-- b000168 | prose | pages [12] -->
is the inherent rate of depreciation during production and where,  is the rate of  are the carbon stocks of the two products produced in depreciation during use.

<!-- b000169 | prose | pages [12] -->
and 1ip ip 2 year i .

<!-- b000170 | prose | pages [12] -->
Based on the characteristics of carbon stock changes during the forest growth cycle, the harvesting intensity should not exceed the intrinsic growth rate in order to maintain forest growth

<!-- b000171 | prose | pages [12] -->
h

<!-- b000172 | prose | pages [12] -->
i

<!-- b000173 | prose | pages [12] -->
x

<!-- b000174 | prose | pages [12] -->
i

<!-- b000175 | prose | pages [12] -->
 (15)

<!-- b000176 | prose | pages [12] -->
r

<!-- b000177 | prose | pages [12] -->
 

<!-- b000178 | prose | pages [12] -->
The cost of planting trees is determined by the cost of planting trees per unit area and the size of the felling area. In order to secure as much carbon sequestration as possible, therefore, mainly mature trees with weak carbon sequestration capacity are cut down. Therefore, the cost of planting trees is:

<!-- b000179 | prose | pages [12] -->
W w S  

<!-- b000180 | prose | pages [12] -->
i i new

<!-- b000181 | prose | pages [12] -->
h (16) w  

<!-- b000182 | prose | pages [12] -->
i

<!-- b000183 | prose | pages [12] -->
, ,

<!-- b000184 | prose | pages [12] -->
p

<!-- b000185 | prose | pages [12] -->


<!-- b000186 | prose | pages [12] -->
The forest stock is mainly the stock of wood, and the stock of wood is proportional to the carbon stock in wood, so the for relationship between the carbon stock of the produced product and the production is obtained as follows:

<!-- b000187 | prose | pages [12] -->
 T p  ij  (17) 1,2 j  ij ij

<!-- b000188 | prose | pages [12] -->
is the storage volume per unit area of the forest. where,  Of course, the annual carbon stock of the trees cut should not exceed the existing carbon stock of the forest, the economic efficiency of the whole production process should not lose money at least, and the production and demand of forest products should not be too much different according to the actual situation:

<!-- b000189 | prose | pages [12] -->
h x

<!-- b000190 | prose | pages [12] -->


<!-- b000191 | prose | pages [12] -->
i i

<!-- b000192 | prose | pages [12] -->
T V T V

<!-- b000193 | prose | pages [12] -->


<!-- b000194 | prose | pages [12] -->
1 1 2

<!-- b000195 | prose | pages [12] -->
i i

<!-- b000196 | prose | pages [12] -->
(0.5

<!-- b000197 | prose | pages [12] -->
T

<!-- b000198 | prose | pages [12] -->


<!-- b000199 | prose | pages [12] -->
ij

<!-- b000200 | prose | pages [12] -->
(18)

<!-- b000201 | prose | pages [12] -->
0

<!-- b000202 | prose | pages [12] -->
W

<!-- b000203 | prose | pages [12] -->
 

<!-- b000204 | prose | pages [12] -->
2 2

<!-- b000205 | prose | pages [12] -->
i

<!-- b000206 | prose | pages [12] -->
,1.5 )

<!-- b000207 | prose | pages [12] -->
Z Z Z

<!-- b000208 | prose | pages [12] -->
ij ij ij

<!-- b000209 | prose | pages [12] -->
In summary, we obtain the forest integrated value balance decision model as：

<!-- b000210 | prose | pages [12] -->
min

<!-- b000211 | prose | pages [12] -->
T

<!-- b000212 | prose | pages [12] -->


<!-- b000213 | prose | pages [12] -->
1

<!-- b000214 | prose | pages [12] -->
i

<!-- b000215 | prose | pages [12] -->
max

<!-- b000216 | prose | pages [12] -->
T V

<!-- b000217 | prose | pages [12] -->
1 1

<!-- b000218 | prose | pages [12] -->
i

<!-- b000219 | prose | pages [12] -->
max

<!-- b000220 | prose | pages [12] -->
x P

<!-- b000221 | prose | pages [12] -->


<!-- b000222 | prose | pages [12] -->
i

<!-- b000223 | prose | pages [12] -->
Z Z T Z

<!-- b000224 | prose | pages [12] -->
 

<!-- b000225 | prose | pages [12] -->
1 1 2 2

<!-- b000226 | prose | pages [12] -->
i i i i

<!-- b000227 | prose | pages [12] -->
（19）

<!-- b000228 | prose | pages [12] -->
T V W

<!-- b000229 | prose | pages [12] -->
  

<!-- b000230 | prose | pages [12] -->
2 2

<!-- b000231 | prose | pages [12] -->
i i i

<!-- b000232 | prose | pages [12] -->
i i

<!-- b000233 | furniture | pages [13] -->
Team#2202171

<!-- b000234 | prose | pages [13] -->


<!-- b000235 | prose | pages [13] -->
x x

<!-- b000236 | prose | pages [13] -->
  

<!-- b000237 | prose | pages [13] -->
1

<!-- b000238 | prose | pages [13] -->
i i

<!-- b000239 | prose | pages [13] -->


<!-- b000240 | prose | pages [13] -->


<!-- b000241 | prose | pages [13] -->
h

<!-- b000242 | prose | pages [13] -->
 

<!-- b000243 | prose | pages [13] -->
r

<!-- b000244 | prose | pages [13] -->


<!-- b000245 | prose | pages [13] -->
i

<!-- b000246 | prose | pages [13] -->


<!-- b000247 | prose | pages [13] -->
x

<!-- b000248 | prose | pages [13] -->
i

<!-- b000249 | prose | pages [13] -->


<!-- b000250 | prose | pages [13] -->
p p

<!-- b000251 | prose | pages [13] -->
 

<!-- b000252 | prose | pages [13] -->
1 2

<!-- b000253 | prose | pages [13] -->
i i

<!-- b000254 | prose | pages [13] -->


<!-- b000255 | prose | pages [13] -->
(1

<!-- b000256 | prose | pages [13] -->
P

<!-- b000257 | prose | pages [13] -->
 

<!-- b000258 | prose | pages [13] -->


<!-- b000259 | prose | pages [13] -->


<!-- b000260 | prose | pages [13] -->
i

<!-- b000261 | prose | pages [13] -->


<!-- b000262 | prose | pages [13] -->
. .

<!-- b000263 | prose | pages [13] -->
s t W w

<!-- b000264 | prose | pages [13] -->
  

<!-- b000265 | prose | pages [13] -->
i

<!-- b000266 | prose | pages [13] -->
 

<!-- b000267 | prose | pages [13] -->


<!-- b000268 | prose | pages [13] -->
T p

<!-- b000269 | prose | pages [13] -->
 

<!-- b000270 | prose | pages [13] -->
ij ij

<!-- b000271 | prose | pages [13] -->


<!-- b000272 | prose | pages [13] -->
 

<!-- b000273 | prose | pages [13] -->
T v T v

<!-- b000274 | prose | pages [13] -->


<!-- b000275 | prose | pages [13] -->
1 1 2

<!-- b000276 | prose | pages [13] -->
i i

<!-- b000277 | prose | pages [13] -->


<!-- b000278 | prose | pages [13] -->
h x

<!-- b000279 | prose | pages [13] -->


<!-- b000280 | prose | pages [13] -->
i

<!-- b000281 | prose | pages [13] -->


<!-- b000282 | prose | pages [13] -->
(0.5

<!-- b000283 | prose | pages [13] -->
T Z

<!-- b000284 | prose | pages [13] -->
 

<!-- b000285 | prose | pages [13] -->
ij

<!-- b000286 | prose | pages [13] -->


<!-- b000287 | furniture | pages [13] -->
Page 11 of 22

<!-- b000288 | prose | pages [13] -->
x

<!-- b000289 | prose | pages [13] -->
 

<!-- b000290 | prose | pages [13] -->
(1 )

<!-- b000291 | prose | pages [13] -->
r x h

<!-- b000292 | prose | pages [13] -->
 

<!-- b000293 | prose | pages [13] -->
i i i

<!-- b000294 | prose | pages [13] -->
N

<!-- b000295 | prose | pages [13] -->
h

<!-- b000296 | prose | pages [13] -->
 

<!-- b000297 | prose | pages [13] -->


<!-- b000298 | prose | pages [13] -->
i

<!-- b000299 | prose | pages [13] -->
) )

<!-- b000300 | prose | pages [13] -->
P p

<!-- b000301 | prose | pages [13] -->


<!-- b000302 | prose | pages [13] -->
1 2

<!-- b000303 | prose | pages [13] -->
i i

<!-- b000304 | prose | pages [13] -->


<!-- b000305 | prose | pages [13] -->
h h

<!-- b000306 | prose | pages [13] -->
i i

<!-- b000307 | prose | pages [13] -->
 

<!-- b000308 | prose | pages [13] -->
0

<!-- b000309 | prose | pages [13] -->
W

<!-- b000310 | prose | pages [13] -->
 

<!-- b000311 | prose | pages [13] -->
2 2

<!-- b000312 | prose | pages [13] -->
i

<!-- b000313 | prose | pages [13] -->
,1.5 )

<!-- b000314 | prose | pages [13] -->
Z

<!-- b000315 | prose | pages [13] -->
ij ij ij

<!-- b000316 | heading | pages [13] -->
5.2 Scope of application of the plan and the premise of no logging

<!-- b000317 | prose | pages [13] -->
(1) Analysis of plan applications for different forests

<!-- b000318 | prose | pages [13] -->
According to the use of forests, we classify forests into five categories: protection forests, timber forests, economic forests, charcoal forests and special purpose forests. The decision model we developed is applicable to different types of forests.

<!-- b000319 | prose | pages [13] -->
Protective forests: Forests whose main  purpose is protection, including water conservation forests and soil and water conservation forests. For this type of forest, the forest management plan obtained from the above decision model cannot be used. The reason is that for protection forests, the main purpose is ecological and there is no need to consider social needs and economic benefits. It is only necessary to ensure that the forest growth is stable and the carbon sequestration is high and the protection purpose is achieved. The target strain of the decision model at this point is:

<!-- b000320 | prose | pages [13] -->
max

<!-- b000321 | prose | pages [13] -->
max

<!-- b000322 | prose | pages [13] -->
where, is the degree of protection Q i

<!-- b000323 | prose | pages [13] -->
x x P

<!-- b000324 | prose | pages [13] -->


<!-- b000325 | prose | pages [13] -->
i i

<!-- b000326 | prose | pages [13] -->
(20)

<!-- b000327 | prose | pages [13] -->
Q

<!-- b000328 | prose | pages [13] -->
i

<!-- b000329 | prose | pages [13] -->
Timber forest: The forest whose main purpose is to produce wood, including bamboo  forest whose main purpose is to produce bamboo timber, etc. For this forest, the forest management plus care obtained from the decision model cannot be used directly. Because this forest mainly produces timber, it is a forest product that depreciates carbon stock year by year, so products that are entirely depreciated in the current year in the model should be removed from consideration, i.e. set . 0 iZ  1 1 Economic forests: Forests with the main purpose of producing fruits, edible oils,  beverages, spices, industrial raw materials and medicinal herbs, etc. For this type of forest the forest management plan obtained from the decision model cannot be used. This is because the forest products we set up in the model are considered to be products

<!-- b000330 | furniture | pages [14] -->
Team#2202171

<!-- b000331 | furniture | pages [14] -->
Page 12 of 22

<!-- b000332 | prose | pages [14] -->
produced by cutting wood, and economic forests are not in our consideration. Fuelwood forests: Forests whose main purpose is to produce fuel. For this forest, the  forest management plus care obtained from the decision model cannot be used directly. Because this forest mainly produces fuel, it is a forest product that all the carbon stock is depreciated in the current year, so the product that is depreciated year by year in the model should be deleted from consideration, i.e. set Special purpose forests:

<!-- b000333 | prose | pages [14] -->
Forests with  . 0 iZ  2 the main purpose of national defense, environmental protection, scientific experiments, etc., including national defense forests, experimental forests, mother forests, forests of nature reserves, etc. The model we build is based on the general forest, and these forests have their own special purposes, and their planning considerations have their own biased perspectives, so our decision model to get the management plan cannot be applied to this forest. (2) Prerequisites for no logging

<!-- b000334 | prose | pages [14] -->
The value balance decision model of the forest we have developed is an optimal forest management plan obtained by balancing the values of social needs, economic benefits, and ecological influence of a normally growing common forest. However, for some special forests, their values may focus on ecological aspects or their unique values, and these forests cannot be deforested when the expression of values and deforestation contradict each other.

<!-- b000335 | prose | pages [14] -->
Transitional deforestation: When ix   , it indicates that the carbon stock in the x x lower limit forest is less than the lower limit, when the forest is in a period of transitional deforestation. For the transitional deforestation, it is not possible to continue to cut down again for social needs, which will lead to the aggravation of ecological harshness and the sharp weakening of its ability to regulate climate and prevent wind and sand. Therefore, forest managers should focus on ecological restoration rather than logging in the early stage of transitional deforestation. Ecological reserve forest: For ecological reserve, the forest focuses on the ecological  impacts, do not consider the social needs and economic benefits, so in order to protect its biodiversity, protect rare species and other roles, the ecological reserve can’t be cut down. Endangered species forests: For endangered trees, their wild populations are small and  in danger of extinction for a considerable period of time. Therefore, forest managers are mainly concerned with the conservation role of such trees and ensure their existence. The number of endangered trees is already very small, so of course they cannot be cut down. Minority forests: If the forest provides a place for minorities to live, such as the Amazon  forest, there are 20 million indigenous people who have called the Amazon River basin home for generations and have never had contact with modern society. Therefore, this type of forest cannot be deforested at will.

<!-- b000336 | heading | pages [14] -->
5.3 Transition point analysis

<!-- b000337 | prose | pages [14] -->
Different forests have different characteristics with different growth conditions, major tree species, product uses, etc. Therefore, there is no one transition point that can be applied to all forests. Specific parameters in the model need to be determined according to the characteristics of each forest, such as making the inherent growth rate of the forest, carbon density at maturity, etc., and then the transition point for its optimal solution is obtained by the

<!-- b000338 | furniture | pages [15] -->
Team#2202171

<!-- b000339 | furniture | pages [15] -->
Page 13 of 22

<!-- b000340 | prose | pages [15] -->
model. This task analyzes the determination and difference of transition points for different geographical locations as well as forests with different uses.

<!-- b000341 | heading | pages [15] -->
5.3.1 Genetic algorithm for solving the optimal solution

<!-- b000342 | prose | pages [15] -->
Various possible forest management plans are taken as individuals, and the cutting volume of two forest products is taken as genes, thus forming a genetic population. Using the planning objective as the fitness function, the optimal forest management plan that balances the various values of the forest can be solved by the genetic algorithm with the adaptation of the constraints. The process is shown in Fig.9.

<!-- b000343 | caption | pages [15] -->
Fig.9 Flow chart of optimal plan solving

<!-- b000344 | prose | pages [15] -->
According to the research of Zhou Jian et al. on forest carbon sink[4] and the data provided by FOA[5], the initial parameters for solving the optimal plan are set, as shown in Table 2.

<!-- b000345 | caption | pages [15] -->
Table 2 Initial parameters

<!-- b000346 | prose | pages [15] -->
S Z Parameters 1 all

<!-- b000347 | prose | pages [15] -->
Value 4 2 4 3 50 10 hm 160 10 m  

<!-- b000348 | prose | pages [15] -->
w  Parameters

<!-- b000349 | prose | pages [15] -->
Value 0.95 3 3 / USD m

<!-- b000350 | prose | pages [15] -->
Z 1v 2v 2

<!-- b000351 | prose | pages [15] -->
4 3 3 3 400 10 m 675 / 450 / USD m USD m 

<!-- b000352 | prose | pages [15] -->
  0x

<!-- b000353 | prose | pages [15] -->
15Mt 0.95 3 3 2 8 10 /  m m 

<!-- b000354 | heading | pages [15] -->
5.3.2 Transition point analysis of different temperature zone forests

<!-- b000355 | prose | pages [15] -->
The main tree species of different temperature zone forests are different. In this paper, we mainly discuss the transition points of management plans for subtropical, temperate and sub-frigid forests. The corresponding forests are evergreen broadleaf forest, deciduous broadleaf forest and mixed coniferous forest.

<!-- b000356 | caption | pages [15] -->
Fig.10 Diagram of tree species in different temperature zones

<!-- b000357 | prose | pages [15] -->
and the intrinsic growth rate rare different for different forest The carbon density 

<!-- b000358 | furniture | pages [16] -->
Team#2202171

<!-- b000359 | furniture | pages [16] -->
Page 14 of 22

<!-- b000360 | prose | pages [16] -->
maturity periods, therefore the forest management plans obtained are different and the transition points are different. Referring to Zhou Yurong et al. for the carbon stock study of each temperature zone forest[6], the corresponding modified values of parameters for each temperature zone forest are shown in Table 3.

<!-- b000361 | caption | pages [16] -->
Table 3 Forest parameters for each temperature zone

<!-- b000362 | prose | pages [16] -->
Forest subtropical forest  80

<!-- b000363 | prose | pages [16] -->
r 0.4

<!-- b000364 | prose | pages [16] -->
temperate forest sub-frigid forest 50 60

<!-- b000365 | prose | pages [16] -->
0.4 0.5

<!-- b000366 | prose | pages [16] -->
Therefore, the optimal forest management plan that balances each value of the forest and the corresponding changes in the carbon stock of the forest system (forest and forest products) can be obtained based on the model. The calculation results are shown in Fig.11.

<!-- b000367 | prose | pages [16] -->
(a) Carbon stock (b) Transition points

<!-- b000368 | caption | pages [16] -->
Fig.11 Changes in carbon stocks in forests system in various temperature zones and transition points

<!-- b000369 | prose | pages [16] -->
for optimal management options

<!-- b000370 | prose | pages [16] -->
As shown in Fig.11, under the optimal forest management plan obtained from the decision model, the carbon stocks of the forest systems in all three different temperature zones continue to increase and then gradually level off. This indicates that when using the obtained management plan, it is still possible to increase the carbon sequestration of the forest while meeting the needs of society. This further validates the optimality of the scheme and the benefits of a certain amount of deforestation.

<!-- b000371 | prose | pages [16] -->
The management plans for forests in different temperature zones are different, but the final deforestation amount is stable at 6 6 3 , which may be related to the initial set of 5 10 m  consistent forest area. The management plans for forests in different temperature zones are divided into two types of transition points, namely the phased transition point and the final transition point. In this case, the subtropical forest reaches the staged transition point in about 8 years, and the first significant increase in deforestation is achieved. It reaches the final transition point in the 23rd year and thereafter enters a stable logging phase. Similarly, temperate forests start with a linear increase in deforestation and remain stable between the first and second transition points, after which deforestation increases until it plateaus. Sub-frigid forests, on the other hand, do not have a clear transition point and reach the final

<!-- b000372 | furniture | pages [17] -->
Team#2202171

<!-- b000373 | furniture | pages [17] -->
Page 15 of 22

<!-- b000374 | prose | pages [17] -->
transition point after about 39 years. The optimal management plan for forests in different geographical locations differs and the transition points also differ, so it is necessary to obtain parameters based on the characteristics of specific forests and bring them into the model to obtain the optimal plan as well as its transition points.

<!-- b000375 | heading | pages [17] -->
5.3.3 Transition point analysis of timber forests and charcoal-fuel forests

<!-- b000376 | prose | pages [17] -->
Timber forests and charcoal-fueled forests have different types of trees and therefore and intrinsic growth rate rat maturity. Charcoal-fueled forests different carbon density  are mainly fast-growing trees used for burning, while timber forests are mainly robust trees used for wood production. Therefore, the social demand for timber and charcoal fuelwood forests varies, as does the cost of planting them. The parameters are modified as in Table 4.

<!-- b000377 | caption | pages [17] -->
Table 4 Parameters of timber forests and charcoal forests

<!-- b000378 | prose | pages [17] -->
Forest Social demand

<!-- b000379 | prose | pages [17] -->
0 iZ  Timber forests 1

<!-- b000380 | prose | pages [17] -->
0 iZ  Charcoal-fueled forests 2

<!-- b000381 | prose | pages [17] -->
w r 

<!-- b000382 | prose | pages [17] -->
0.3 50 3 3 / USD m

<!-- b000383 | prose | pages [17] -->
0.9 40 3 2 / USD m

<!-- b000384 | prose | pages [17] -->
As a result, the optimal forest management plan that balances each value of the forest and the carbon stock of the forest system (forest and forest products) under the optimal plan can be obtained according to the model. The results are shown in Fig.12.

<!-- b000385 | prose | pages [17] -->
(a) Carbon stock (b) Transition points

<!-- b000386 | caption | pages [17] -->
Fig.12 Carbon stock changes and optimal management plans for forests of different uses

<!-- b000387 | prose | pages [17] -->
As shown in Fig12, under the optimal management plan, the amount of carbon sequestered in timber forests increases year by year and eventually stabilizes, while the amount of carbon sequestered in charcoal-fueled forests is always stable, i.e., the forest growth in charcoal-fueled forests is always stable. And the cutting volume of charcoal-fueled 6 3 , which can meet the social demand it supplies or even have a forests is stable at 4.2 10 m  surplus, and there is no transition point. The cut volume of timber forest increases from 3*106 6 year by year and finally stabilizes at 5 10 m  3 3 . There is a transition point in about 23 years. The transition point is different for timber forests and charcoal forests, which have different uses. The optimal plan and its transition points need to be obtained for a specific forest based on the characteristic parameters of the forest.

<!-- b000388 | furniture | pages [18] -->
Team#2202171

<!-- b000389 | furniture | pages [18] -->
Page 16 of 22

<!-- b000390 | heading | pages [18] -->
6. Forest Management Plan for Tien Shan

<!-- b000391 | heading | pages [18] -->
6.1 Carbon stock and management plan of Tien Shan

<!-- b000392 | prose | pages [18] -->
The Tien Shan Mountain stretches across the central part of Xinjiang. Spruce is the most important zonal forest vegetation in the Tien Shan Mountains, with an area of about

<!-- b000393 | prose | pages [18] -->
4 2 , accounting for 44.9% of the natural forested area in Xinjiang, and is the main 52.84 10 hm  material body of the forest ecosystem in the Tien Shan Mountains and even in Xinjiang. The mild and humid habitat of the Tien Shan mountain belt provides a good place for the growth and development of snowy spruce, which leads to fast growth, high density and high lumbering rate. The trees here are 50-60 meters tall, with annual rings of 300-400 years or more. It can produce more than 1000 m3 of wood per hectare[7], and its wood is excellent, tough and durable, mainly used for furniture and other forest products.

<!-- b000394 | prose | pages [18] -->
Because of the characteristics of forest products in Tien Shan, the demand for the entire depreciated forest products in the year is therefore 0, i.e.

<!-- b000395 | prose | pages [18] -->
. Based on the study of Xu et 0 Z  1 al. on the carbon stock of Tien Shan forest and the data support of FOA[5], we can get the initial parameters of Tien Shan forest, as shown in Table 5.

<!-- b000396 | caption | pages [18] -->
Table 5 Model parameters of Tien Shan

<!-- b000397 | prose | pages [18] -->
S Parameters r all

<!-- b000398 | prose | pages [18] -->
Value 0.385 4 2 52.84 10 hm 

<!-- b000399 | prose | pages [18] -->
w  Parameters

<!-- b000400 | prose | pages [18] -->
Value 0.95 3 3 / USD m

<!-- b000401 | prose | pages [18] -->
 Z 2v 2

<!-- b000402 | prose | pages [18] -->
2 3 3 112.53 /t hm 413.86m 465 / USD m

<!-- b000403 | prose | pages [18] -->
 0x *

<!-- b000404 | prose | pages [18] -->
53.14Mt 0.95 *

<!-- b000405 | prose | pages [18] -->
From this, the optimal forest management plan that balances each value of the forest and the carbon stock of the forest system under the optimal plan can be obtained according to the model. The results are shown in Fig.13.

<!-- b000406 | prose | pages [18] -->
(a) Ecological anf ecconomic value (b) Social value

<!-- b000407 | caption | pages [18] -->
Fig.13 Various value changes in the Tien Shan forest and the optimal management plan

<!-- b000408 | prose | pages [18] -->
As shown in Fig.13, the optimal management scheme of Tien Shan forest after considering social demand, economic benefits and ecological influence is obtained by the

<!-- b000409 | furniture | pages [19] -->
Team#2202171

<!-- b000410 | furniture | pages [19] -->
Page 17 of 22

<!-- b000411 | prose | pages [19] -->
model - annual felling of old trees and production of long life forest products, and planting of felling areas, with the felling volume increasing year by year, as shown in the figure. Under this scenario, the carbon stock of the forest system increases year by year and finally 7 . The economic efficiency is a stable and profitable state, with an stabilizes at 11 10 tC  8 . the felling volume increases year by year, from annual profit of about 1.5 1.55 10 USD   6 3 slightly not meeting the demand at the beginning to finally stabilizing at surplus compared to the demand of , with a 5.2 10 m  6 6 3 . A good balance is reached between the 4.13 10 m  three, so this scheme is the optimal one.

<!-- b000412 | heading | pages [19] -->
6.2 Transition strategy to extend the 10-year cutting interval

<!-- b000413 | prose | pages [19] -->
The longer 10-year interval, the greater increase in the need to cut at once, and the greater ecological and sustainable impacts of the direct shift require the setting of a transition strategy. As the forest changes from an annual cutting management plan to a decadal cutting management plan, it needs to be modified on the basis of the above model to ensure healthy and sustainable growth of the forest, as well as to meet the requirements of social needs and other aspects.

<!-- b000414 | prose | pages [19] -->
Gradual increase in cutting intervals. For example, a policy of cutting once every two to  four years should be implemented first, and the forest area should be continuously expanded. When the forest area can ensure that the ecosystem can adapt to a larger cutting interval, the cutting interval should be adjusted until it becomes once every ten years. Balance timber supply through imports. Considering the demand for timber in the area in  the interval year (the year of non-cutting), it is necessary to meet the demand for timber in the interval year as much as possible in the year when the trees are cut. Therefore, the social demand objective in the integrated forest value balance decision model is changed to：

<!-- b000415 | prose | pages [19] -->
 min T  1 i

<!-- b000416 | prose | pages [19] -->
1iT, iT

<!-- b000417 | prose | pages [19] -->
    (21) Z Z T Z   1 1 2 2 i i i i

<!-- b000418 | prose | pages [19] -->
is the volume of two forest products cut at the interval of harvesting. where, 2

<!-- b000419 | prose | pages [19] -->
1iZ, iZ is the total demand for the interval year. 2 For some of the smaller forests, it is not possible to meet the demand for many years by  cutting them once. In such cases, the supply deficit should be made up locally by importing timber. Therefore, the above objective is further changed to：

<!-- b000420 | prose | pages [19] -->
h

<!-- b000421 | prose | pages [19] -->
(

<!-- b000422 | prose | pages [19] -->
W w

<!-- b000423 | prose | pages [19] -->
 

<!-- b000424 | prose | pages [19] -->
i

<!-- b000425 | prose | pages [19] -->


<!-- b000426 | prose | pages [19] -->
(

<!-- b000427 | prose | pages [19] -->
N S

<!-- b000428 | prose | pages [19] -->


<!-- b000429 | prose | pages [19] -->


<!-- b000430 | prose | pages [19] -->


<!-- b000431 | prose | pages [19] -->
i

<!-- b000432 | prose | pages [19] -->
where, is the expanded forest area. S ,i expand

<!-- b000433 | prose | pages [19] -->
)

<!-- b000434 | prose | pages [19] -->
S

<!-- b000435 | prose | pages [19] -->


<!-- b000436 | prose | pages [19] -->
i i

<!-- b000437 | prose | pages [19] -->
,

<!-- b000438 | prose | pages [19] -->
i expand

<!-- b000439 | prose | pages [19] -->
(22)

<!-- b000440 | prose | pages [19] -->
)

<!-- b000441 | prose | pages [19] -->
S

<!-- b000442 | prose | pages [19] -->


<!-- b000443 | prose | pages [19] -->
,

<!-- b000444 | prose | pages [19] -->
all all i expand

<!-- b000445 | prose | pages [19] -->
can be introduced, the reason being that a smaller number of Tree species with larger   trees can be used to meet the demand; or tree species with larger r allowing for a faster rate of forest recovery.

<!-- b000446 | prose | pages [19] -->
can be introduced,

<!-- b000447 | furniture | pages [20] -->
Team#2202171

<!-- b000448 | furniture | pages [20] -->
Page 18 of 22

<!-- b000449 | heading | pages [20] -->
7. Sensitivity Analysis

<!-- b000450 | prose | pages [20] -->
In real life, statistics are often inaccurate and there may be some biases in the inputs to our models. These biases may affect the results of our model. In order to test the robustness of our model, in this section, we will analyze the sensitivity of our decision model in the analysis. The results of the sensitivity analysis show that our model shows perfect stability.

<!-- b000451 | prose | pages [20] -->
Forest product depreciation rates have a significant impact on our analysis of optimal forest management plans. Different depreciation rates affect the carbon content of forest products sequestered, which may lead to misjudgment of the optimal management plan and make the balance between the various values of the forest problematic. The product depreciation rate is represented in the model as a constant . Therefore, we will investigate the depreciation rate in more depth. Since in the model mainly represents the depreciation  rate of long-lived forest products such as furniture, the depreciation rate is not very large. We change the value of and analyze the changes that make the carbon stock of the forest  system (forest and forest products). If the fluctuation is too large, we should reconsider the model.

<!-- b000452 | prose | pages [20] -->
(a) Carbon stock (b) Cutting volume

<!-- b000453 | caption | pages [20] -->
Fig.14 Program changes at different discount rates

<!-- b000454 | prose | pages [20] -->
As shown in Fig.14, our decision model is stable. When the discount rate fluctuates, the amount of deforestation and the carbon stock of the forest system fluctuate somewhat, but the fluctuations are not significant. When the discount rate fluctuates up and down, the carbon stock also fluctuates, but overall still both show an increasing to steady trend. There is also a relative decrease in the amount of cutting, but when the carbon stock gradually increases to a stable level, the amount of cutting also increases and finally stabilizes at the same level, which 6 3 can meet the demand of . Therefore, despite the fluctuation of the depreciation 4.13 10 m  rate, our decision model can still obtain the optimal forest management plan that balances all values of the forest. This demonstrates the stability of the model and can solve real-life practical problems.

<!-- b000455 | furniture | pages [21] -->
Team#2202171

<!-- b000456 | furniture | pages [21] -->
Page 19 of 22

<!-- b000457 | heading | pages [21] -->
8. Strengths and Weaknesses

<!-- b000458 | heading | pages [21] -->
8.1 Strengths

<!-- b000459 | prose | pages [21] -->
Considering the trend of carbon stock growth of forest system is in accordance with the  law of logistic model, the optimal strategy to maintain the ecological balance of forest is derived by combining the carbon stock of forest products caused by deforestation, and the method is innovative. In addition to analyzing the ideal strategy considering only the forest system, the social  and economic aspects are also considered for multi-objective optimization; at the same time, the optimal strategies for different kinds of forests and forests in different temperature zones are also analyzed, which is comprehensive and has application significance. The model is brought into the data of Tien Shan forest for verification, and the results are  consistent with reality, and the model is more accurate.

<!-- b000460 | heading | pages [21] -->
8.2 Weaknesses

<!-- b000461 | prose | pages [21] -->
Since some parameters are estimated values (e.g. wood demand for fuel is determined  from wood fuel data provided in FAO, while in reality wood chips, etc. are also considered as fuel), the results of the model may have small deviations. If more detailed data can be found, our model can be verified more precisely. In reality, the way trees are planted (spaced or concentrated), etc., may have an impact on  the parameters of the model, which is ignored in this paper. The model can be improved by measuring various parameters of the trees.

<!-- b000462 | furniture | pages [22] -->
Team#2202171

<!-- b000463 | furniture | pages [22] -->
Page 20 of 22

<!-- b000464 | heading | pages [22] -->
9 Non-technical Newspaper Article

<!-- b000465 | prose | pages [22] -->
The carbon cycle refers to the exchange of carbon in the biosphere, lithosphere, hydrosphere and atmosphere of the Earth, and the cycle continues with the movement of the Earth. The carbon cycle in the biosphere mainly involves green plants absorbing carbon dioxide from the atmosphere through photosynthesis and converting it into glucose, which is then used by organisms to synthesize other organic compounds. Organic compounds are passed through the food chain and become part of other organisms such as animals and bacteria. Carbohydrates in living organisms are oxidized to carbon dioxide and water through respiration.

<!-- b000466 | prose | pages [22] -->
The carbon cycle in nature is balanced, but humans produce large amounts of carbon dioxide when they burn fossil fuels.

<!-- b000467 | prose | pages [22] -->
The concentration of carbon dioxide in the atmosphere rises, which disrupts the original balance of nature and leads to global

<!-- b000468 | prose | pages [22] -->
warming with a series of negative effects. Thus, controlling carbon dioxide emissions is a key measure to curb global warming. The Report on the Impact of Global Warming of 1.5°C above Pre-industrial indicates that to achieve global Levels warming of no more than 1.5°C above pre-industrial levels, net global CO2 emissions must be reduced by about 45% by 2030 compared to 2010, and carbon neutrality should be achieved by 2050.

<!-- b000469 | prose | pages [22] -->
Forest systems are a key factor in achieving carbon neutrality, and increasing forest carbon sequestration and reducing CO2 emissions are two equally important

<!-- b000470 | furniture | pages [23] -->
Team#2202171

<!-- b000471 | prose | pages [23] -->
aspects of climate change mitigation. Forests play an irreplaceable role in carbon sequestration.

<!-- b000472 | prose | pages [23] -->
Terrestrial carbon sequestration can be enhanced through strong measures, such as afforestation and restoration of destroyed ecosystems. The replacement of energy-intensive materials with durable woody forest products and the recycling of harvesting residues can reduce greenhouse gas emissions.

<!-- b000473 | prose | pages [23] -->
By exploring the role of forests in sequestering carbon, we have discovered a different approach to increasing carbon sequestration in forests than is common: a certain amount of deforestation. Forests sequester carbon dioxide in plants and the products created from them, including furniture, paper, and fuel. These forest products sequester carbon dioxide during their life cycle. When the products outlive the trees that produce them, the forest is sequestering more carbon due to the regrowth of young forests than it would if it were not deforested at all.

<!-- b000474 | prose | pages [23] -->
Moreover, the change in carbon stocks over the life cycle of a forest follows the logistic law, which states that mature trees have more carbon in their bodies but less carbon sequestration capacity. Therefore, when harvesting, mature trees should be cut down as much as possible and then made into long-lived forest products. This has less impact on the forest's ability to sequester carbon, and the products sequester more carbon and for a longer period of time.

<!-- b000475 | prose | pages [23] -->
Forest management strategies that include harvesting can be beneficial for carbon sequestration. But over-harvesting can limit carbon sequestration.

<!-- b000476 | prose | pages [23] -->
Forest managers must find a balance between the value of the forest products generated by harvesting and the value of allowing the forest to continue to grow and perform functions such as carbon sequestration.

<!-- b000477 | furniture | pages [23] -->
Page 21 of 22

<!-- b000478 | prose | pages [23] -->
Therefore, for actual logging plans, practical factors must be considered, such as the use of the forest, its geographic location, the type of tree species, and the benefits and longevity of the forest products.

<!-- b000479 | prose | pages [23] -->
Forest management strategies that include harvesting can be beneficial for carbon sequestration.

<!-- b000480 | prose | pages [23] -->
Of course, over-harvesting can limit carbon sequestration. And, deforestation also needs to meet economic benefits. Forest managers must find a balance between economics and ecology. Under the condition of stable forest growth (E<r), the logging intensity should be within a certain suitable range, when the upper limit is higher than the upper limit, it will cause ecological transitional logging, while the lower limit is lower than the lower limit, it will cause economic transitional logging.

<!-- b000481 | prose | pages [23] -->
Therefore, for a forest, in order to increase the carbon sequestration of the forest, logging needs to be included within the management plan, but the specific logging plan, such as the timing of logging, the amount of logging, and the species to be logged, needs to take into account the economic, ecological, and social values of the forest to find a balance.

<!-- b000482 | furniture | pages [24] -->
Team#2202171

<!-- b000483 | heading | pages [24] -->
References

<!-- b000484 | furniture | pages [24] -->
Page 22 of 22

<!-- b000485 | references | pages [24] -->
[1] Zhang F, Peng Jodeng. Study on the economic value of forest carbon stock and

<!-- b000486 | references | pages [24] -->
carbon sink in Beijing[J]. Forest Resource Management,2021(06):52-58

<!-- b000487 | references | pages [24] -->
[2] Wang L, Wang Y, Chang X. An analysis of carbon sequestration and oxygen

<!-- b000488 | references | pages [24] -->
release

<!-- b000489 | references | pages [24] -->
capacity

<!-- b000490 | references | pages [24] -->
of

<!-- b000491 | references | pages [24] -->
common

<!-- b000492 | references | pages [24] -->
Agriculture,2012,6(05):54-56.

<!-- b000493 | references | pages [24] -->
garden

<!-- b000494 | references | pages [24] -->
tree

<!-- b000495 | references | pages [24] -->
species[J].

<!-- b000496 | references | pages [24] -->
Southern

<!-- b000497 | references | pages [24] -->
[3] Chen Xiaofeng. Study on the carbon stock of arboreal forests and their carbon

<!-- b000498 | references | pages [24] -->
sequestration potential in Beijing[D]. Beijing Forestry University, 2020.

<!-- b000499 | references | pages [24] -->
[4] Zhou Jian, Xiao Rongbo, Zhuang Changwei, DENG Yirong. Research on urban

<!-- b000500 | references | pages [24] -->
forest carbon sink and its effect of offsetting energy carbon emission--Guangzhou as

<!-- b000501 | references | pages [24] -->
an example[C]. The Seventh Workshop on Sustainable Development in Guangdong,

<!-- b000502 | references | pages [24] -->
Hong Kong and Macau. 2014

<!-- b000503 | references | pages [24] -->
[5] https://www.fao.org/faostat/en/#data.

<!-- b000504 | references | pages [24] -->
[6] Zhou YR, Yu ZL, Zhao SD. Carbon storage and carbon balance of major forest

<!-- b000505 | references | pages [24] -->
ecosystems in China[J]. Journal of Plant Ecology,2000(05):518-522.

<!-- b000506 | references | pages [24] -->
[7] Xu Wenqiang, Yang Liao,Chen Xi,Gao Yaqi,Wang Lei. Carbon stock pattern of

<!-- b000507 | references | pages [24] -->
forest ecosystems in Tien Shan and its influencing factors[J]. Journal of Plant

<!-- b000508 | references | pages [24] -->
Ecology,2016,40(04):364-373.

<!-- b000509 | references | pages [24] -->
[8] O'Neill B C, Tebaldi C, Van Vuuren D P, et al. The scenario model

<!-- b000510 | references | pages [24] -->
intercomparison

<!-- b000511 | references | pages [24] -->
project

<!-- b000512 | references | pages [24] -->
(ScenarioMIP)

<!-- b000513 | references | pages [24] -->
Development, 2016, 9(9): 3461-3482.

<!-- b000514 | references | pages [24] -->
for

<!-- b000515 | references | pages [24] -->
CMIP6[J].

<!-- b000516 | references | pages [24] -->
Geoscientific

<!-- b000517 | references | pages [24] -->
Model
