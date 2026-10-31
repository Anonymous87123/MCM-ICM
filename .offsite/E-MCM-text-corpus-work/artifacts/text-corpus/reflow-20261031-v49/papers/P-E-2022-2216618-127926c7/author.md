Problem Chosen 2022

MCM/ICM

Summary Sheet

Summary

Current forest management plans prioritize economical proﬁtability with little con- sideration of the forest’s ecological e↵ects. Thus, the managers fail to delibrately utilize their precious and natural resource of forests as the source of carbon sequestration, the process of decreasing the stocks of carbon dioxide from the atmosphere mechanically or by the biosphere. Undoubtedly, this has led to severe climatic changes and environmental unsustainability.

Incorporating social, economical, and ecological sectors, the model we present serves as a novel approach to balance various factors involved in forestry. It re-optimizes the pre-existing forest management plans and enhances eﬃciency, from a global perspective.

A sophisticated but limited model in real-life is The Faustmann Model[1]. It calcu- lates the present value of the income stream for forest rotation and infers the optimal time to cut the forest but is completely based on the economical portion of our world.

We designed the Comprehensive Index of Forest (CIF) to measure the synthetical value of a forest, consisting of three indices: CSI, EI and BDI. The CSI takes the total carbon dioxide sequestrated by a forest and its products into account; the EI values the economical worth provided by the products; and the BDI is an important indicator of the inﬂuence on biodiversity by the harvest. And we use AHP to determine the weights for developed and developing countries. Moreover, considering the topology, we designed AVF to measure the comprehensive quality of the forest more accurately.

Next we selected two forests from developed and developing countries as our case studies for the model:

Quaking aspen forests: (representative for developed sector)

• Developed countries concentrate more on achieving social and ecological goals, so the CSI weights more than the others and the tendency to cut down trees is low.

• Surprisingly, we found out that it is actually better to not harvest any trees.

Amazon rainforest: (representative for developing sector)

• Developing countries rely more on the economical e↵ects that the forest may bring about, and hence has a much higher chance to cut down the trees.

• Being di↵erent from its developed counterpart, developing countries must consider harvesting in the management plan to optimize CIF.

We also commented about the strengths and weaknesses of our models, and pointed out the aspects for further improvement. And the sensitivity analysis is conducted at the end. We focused on the analysis of the estimation of the average lifespan of products.

Finally, we wrote a newspaper article persuading some communities that well-prepared harvesting may actually elevate the overall beneﬁts socially, economically and ecologi- cally, rather than destroying the environment.

1 Introduction

1.1 Problem Background

Drastic global climate change is in an urgent need to be resolved. Since the late 19th century, the temperatures of global surface have increased by 0.8◦C and 11 out of the 12 warmest years on record have occurred since 1995 [2].

To mitigate the risks of global warming, people have built a strong interest in stabiliz- ing the atmospheric abundance of CO2 and other GHGs[3]. Indeed, there’s a natural pro- cess called carbon sequestration: enhancing our stocks of carbon dioxide sequestered out of the atmosphere by the biosphere or by mechanical means.

Forests and forest products are the most direct and natural sources for such process to be realized. Globally, The total area of forests is 4.06 billion hectares(ha), which takes up 31 percent of the land area. Analogously, it is equivalent to 0.52 ha per person[4]. Hence, there’s great potential in forest carbon sequestration. In fact, forestry experts with the Intergovernmental Panel on Climate Change (IPCC) suggest that up to 87 billion tons of carbon can be sequestered in the world’s forests by 2050[5].

Nevertheless, forest management is a very complicated topic. In the short term, re- ducing harvests and increasing forest biomass is the best strategy in carbon sequestration [6][7]. However, when the trees get old and stands become too dense, as the growth rate of trees decreases, it may become better to harvest trees to make space for new trees to take place and restart the process.

Additionally, climatic di↵erence is a huge attribute that results in di↵erent lifespans for trees, and hence the harvesting methodology would be distinctive. Moreover, each type of climatic domain takes up di↵erent percentage of the total forest family, so their weights are also inconsistent. The above diagram shows the exact distribution.

1.2 Problem Restatement

• To design a model that calculates the approximate amount of carbon dioxide that a forest and its products can sequestrate over a certain period of time and then determine the most e↵ective management plan in terms of sequestering carbon dioxide.

• To come up with a decision model that balances multiple values which are related to forests from the perspective of both the society and nature. Then,

– Clarify the general composition of our decision model.

– Introduce a circumstance where a forest should be left uncut.

– Point out whether if there exist common transition points between manage- ment plans that are applicable to all forests.

– Demonstrate how a speciﬁc forest’s characteristics are used to determine tran- sition points between management plans.

• To apply our model to a certain forest, predict its e↵ects of sequestration over a period of 100 years, prove that it is the best forest management plan for this forest, and design a transitioning strategy to shift the management plan so that time gaps of 10 years or longer between two harvesting dates are included.

• Write a one- to two-page article explaining the reasons why a certain forest should consider harvesting in its ultimate management plan and convincing the locals that it’s the best decision to be made.

1.3 Assumptions and Justiﬁcations

1. The environment around a forest is stable. That is, the occurrence of natural haz- ards is neglected.

Justiﬁcation:The rate of having such events taking place is very low and hence we do not take consideration as it would be meaningless to introduce extreme condi- tions.

2. Human activities other than harvesting are manageable.

Justiﬁcation:Since our model’s main focus is harvesting, we do not take other human activities into consideration in order to simplify calculations.

3. The lifespan of the products has no direct relationship with the age of the trees when harvested. If the longevity of the tree is too small, then it will not be consid- ered as a source for products.

Justiﬁcation:We only examine the physical properties of tree products, and hence we perceive all harvested woods as equal objects.

4. In stable state, within the scope of the problem, the distribution of ages of trees is uniform.

Justiﬁcation:In stable natural environment, the mortality of mature trees is so small that we can ignore it[8].

2 Notations

Nomenclature that we use in the model are shown in the following table. Other none- frequent-used notations will be introduced in the context where they are used.

symbol meaning y Harvest age of trees ˜T Total carbon sequestration of forests and products per hectare T(y) Total carbon sequestration of forests and products per hectare at time y P(y) Total carbon sequestration of prod- ucts per hectare when harvested at time y C(t) Cumulative carbon sequestration of forests per hectare at time t V(t) Rate of carbon sequestration of forests per hectare at time t Proportion of tree that is utilized β ym Average age of tree xi Average lifespan of each kind of product Primary recovery rate of the wood ↵i material of the ith product w Weighted factor of carbon sequestra- tion within products DR Deforestation rate/Proportion of a forest that is harvested CIF Comprehensive Index of Forest Proportion of the woods of the forest ⇢ TCVF Total comprehensive value of forest AVF Average value of a forest

3 The model of carbon sequestration

In our model, we deﬁne the deforestation rate (DR) and we assume that if we decide to harvest some of the forests, we may regularly harvest DR of those trees when they get to the age of y years old.

In the assessment of the total carbon sequestration, with harvest considered, we may separate it into two parts: the carbon sequestration of forests and the carbon sequestra- tion within products. Both of them are determined by y, the harvest age of tree, and other relevant coordinates.

In our model, considering the time when the system gets to the stable state, we deﬁne T(y) as the total carbon sequestration of forests and products, while P(y) and C(y) denote the parts of trees and the parts within the products when harvested at time y, respectively. If a tree is remained till it naturally disappears, then we calculate it by P(ym) = T(ym). In Subsections 3.1 to 3.4, we ﬁrstly assume that every tree in a forest is harvested, so DR = 1 holds true. Evidently, we have

˜T = DR · T(y) + (1 −DR) · T(ym) = P(y) + C(y) = T(y) (1)

3.1 Carbon sequestration of forests

As is known to all, the carbon sequestration of forests can be seen as a comprehensive result of the counteraction of synthesis and destruction of organic substance. The main part of the synthesis process of forests is photosynthesis while the destruction process is a complex mixture of respiration, catabolism, defoliation and other procedures.

However, we may simplify the two parts according to Bertalan↵y’s model[9], which is later modiﬁed by Lenthall, D.[10]. In such model, we deﬁne V(t) as the rate of carbon sequestration of forests at time t. And then, at the steady state, we may express V(t) in a general formula: V(t) = dC(t) = ⌘C(t)m −C(t) (2) dt In other word, the rate of change of cumulative carbon sequestration is determined by the di↵erence between the processes of building up and breaking down, both of which are proportional to some di↵erent powers of cumulative carbon sequestration; ⌘and are the constants of synthesis and destruction of organic substance, respectively.

And the solution of equation (2) is 1 C(t) = {⌘/−[⌘/−C(0)(1−m)]e−(1−m)t} (3) 1−m, where C(0) is the initial carbon content of the forests, i.e., the carbon content of the seeds. Since in real world, the ratio of the carbon content of seeds and mature trees is so small that we can ignore C(0) and simply set it to 0. Then we have

C(t) = b1(1 −e−b2t)b3, (4)

1 1 where b1 = (⌘/) 1−m, b2 = (1 −m)and b3 = 1−m are coordinates of C(t), and they are a little di↵erent among all kinds of trees. And the function in (4) is called Chapman- Richards function. And when t = y, we have

C(y) = b1(1 −e−b2y)b3 (40)

However, if we harvest the trees at age y, the density of trees in the forest may be lower than the virgin forests. Hence we may modify the Chapman-Richards function by multiplying a factor γ(y) = ym y , then we have C(y) = ym y b1(1 −e−b2y)b3 = γ(y)b1(1 −e−b2y)b3. (5)

3.2 Carbon sequestration within products

In our model, when the trees grow up to the age of y, we will cut them down and make them into all kinds of wood products including sawn wood, wood-based panels and paper/paperboard (see Figure 2)[11].

Though, not all components of the tree can be fully utilized. For instance, the leaves and branches need to be removed before the stems are utilized as pillars in houses. Hence, we may deﬁne this factor, the proportion of a tree that is utilized for production, as β. Ac- cordingly, the average utilization rate is β = 30%[4].

In our model, we deﬁne mi(y) (i = 1, 2, 3) as the annual carbon sequestrations of primary wood materials for each kind of products, and wi(y) as the proportion of each kind of products (see Figure 2), where i = 1, 2, 3 denotes sawn wood, wood-based pan- els or paper & paperboard. Since we cut down all the trees at age y, and according to our assumption of uniform distribution of ages of trees, in the stable state, the carbon sequestration in the trees cut down each year is CS PY(y) = C(y) (6) y then we have mi(y) = wiβ · CS PY(y) = wiβC(y) (7) y

And with the development of recycling technologies of wood products, wood pro- cessing plants can recycle the wasted wood materials and mix them with primary wood materials to manufacture wood products. Hence, we can reduce the consumption of woods during the process. And the detailed procedures are shown below:

Suppose the primary recovery rate of the wood materials of the ith product is ↵i and the annual carbon sequestration of the ith kind within the products is pi(y) (i = 1, 2, 3), then we have ↵ipi(y) + mi(y) = pi(y), (8) and evidently the total recovery rate is i = pi(y) 1 ↵0 (9) . mi(y) = 1 −↵i Then, taking equations (7) and (9) together, we have wiβ pi(y) = (1 −↵i)yC(y). (10) Suppose the average lifespan of each kind of products is xi (i = 1, 2, 3), then the total carbon sequestration P(y) is X X 3 3 wixi βC(y) = w P(y) = xipi(y) = y C(y), (11) (1 −↵i) y i=1 i=1 where X 3 wixi w = (12) (1 −↵i)β i=1 is the weighted factor of carbon sequestration within products.

According to [11], we have found the primary recovery rates and average lifespans of all the three kinds of products, and we list the data below:

Parameters Sawn wood Wood-based panels Paper & paperboard 30% 10% 70% ↵ x(years) 35 25 2

And, by Table 2 and equation (12), we can get w = 8.674 years.

3.3 Total carbon sequestration

Take summation of equations (1), (5) and (11), we have ! ! ym 1 + w 1 + w y b1(1 −e−b2y)b3. T(y) = C(y) = (13) y y

But in stable cases, the total amount of products is constant, meaning that the renewal rate of products should not exceed the maximal depreciation rate of products. That is y > w. (14)

And due to our assumption that the ages of trees follows uniform distribution, we need the harvest age y is smaller than the average lifespan of trees, meaning that y < ym. (15) Finally, taking equations (12), (13), (14) and (15) together, we have the following for- mula: ! ym 8>>>>>>>>>>><>>>>>>>>>>>: 1 + w y b1(1 −e−b2y)b3 T(y) = y w < y < ym (16) X 3 wixi w = (1 −↵i)β i=1

3.4 The optimal forest management plan

By equations in (16), if for some y < ym, T(y) gets maximum, then it indicates that the optimal forest management plan is that we harvest those trees if and only if they are in the age of y years old; otherwise, we should never harvest these trees.

For forests in tropical, temperate and frigid zones, since they grow in entirely di↵er- ent climates, they have distinct growth types and (average) lifespans, thus the b1, b2, b3 and ym are various among all the three kinds of forests.

The data mentioned above are listed in the table below (where tC means metric ton carbon equivalent)[12][13]:

Coordinates Tropical Temperate Frigid b1(tC/ha) 428.01 198.6 103.067 b2(year−1) 0.0253 0.0253 0.0245 b3 2.64 2.64 2.69 ym(years) 186 322 322

And the T(y) curves w.r.t y for the three cases are shown in Figure 4.

In cases of tropical and temperate zones, when y = 59.90(years), T(y) gets maxi- mum, and max(TTropical(y)) = 790.4(tC/ha), max(TTemperate(y)) = 634.9(tC/ha); while in forests in frigid zones, when y = 63.45(years), T(y) gets maximum, and max(TFrigid(y)) = 314.0(tC/ha). And evidently for all the three cases, we have w < y < ym.

Hence according to our model, in order to maximize the total amount of carbon se- questration, we suggest that for forests in tropical and temperate zones, it is recommended to only regularly harvest those trees which get to 59.90 years old, and make them into products; and for boreal forests, it is best to only harvest those trees growing up to 63.45 years old, and utilize these trees for wood processing industry.

3.5 Further adjusted model

In our previous discussions, we did not make speciﬁcation about the exact tree types. For instance, if certain tree species whose average longevity is 200 yrs have very high carbon sequestration e↵ects, then it should not be our target when harvesting.

Hence, to further study the relationship, let ¯ym1, ¯ym2 and ¯ym be the average age of harvested trees, remained trees and trees in general (the ym in our previous discussion), respectively. And recall that DR is the proportion of a forest that is harvested. Then we have revised T as a multi-variable function.

˜T = DR · T(y, ¯ym1) + (1 −DR) · T(¯ym2, ¯ym2) (17)

At this stage, DR = 1 does not hold anymore as we are selectively harvesting the trees in a forest. And, for the sake of maintaining the ecological balance and protecting some valuable trees, it is not appropriate to cut down all the trees exceeding certain ages.

Using the formerly computed y, or ˆy to stress the distinction, we can make an estima- tion by ﬁrstly substituting it to equation (17). Next, by the deﬁnition of ¯ym1, ¯ym2 and ¯ym, note the following equation:

DR · ¯ym1 + (1 −DR) · ¯ym2 = ¯ym (18)

Then, by expressing ¯ym2 in terms of ¯ym1 in equation (17), ˜T can be represented as a function of ¯ym1:

◆ ✓¯ym −DR · ¯ym1 , ¯ym −DR · ¯ym1 ˜T = DR · T(ˆy, ¯ym1) + (1 −DR) · T (19) 1 −DR 1 −DR Now it follows immediately that the ideal harvest age ¯ym1 locates at the value where ˜T reaches optimum and therefore the strategy is that we cut down the portion of the forests whose maximum age situates closely to ¯ym1.

For the discussion later, we will use the previous T(y) in calculation for simplicity. So, this section only serves as a further discussion that takes the certain types of trees into our consideration. Still, we will include this in a case study to illustrate its usage.

4 Comprehensive Index of Forest

Since the contribution of a forest is not only limited to its carbon sequestration, we have to consider the comprehensive e↵ects by this forest such as promoting the local eco- nomic development by providing raw materials for wood processing industry, bolstering biodiversity and environment conservation, and providing recreational places for local people and maybe tightly relating to the culture of local society. Hence we will modify our initial model by adding economic and ecological items and cultural factor, and we deliberate the Comprehensive Index of Forest (CIF).

The CIF is the weighted summation of CS I (Carbon Sequestration Index), EI (Eco- nomical Index) and BDI (Biodiversity Index). It is expressed as below where !i are the relative weights:

CIF = !1CS I + !2EI + !3BDI (20)

4.1 Carbon Sequestration Index

Due to our previous model, we can evaluate the contribution to carbon sequestration by various kinds of forest ecosystems. And the Carbon Sequestration Index (CS I) is proportional to the amount of carbon sequestration. In other word, CS I = T(y) (21) u where we normalize the amount of carbon sequestration by simply divide a regulariza- tion factor u. But take the harvest rate DR into consideration, we can not simply use equation (13), but the total CS I is the weighted average of harvest part and the part that not harvested. And it should be modiﬁed as ! ym 1 + w y b1(1 −e−b2y)b3 + (1 −DR)b1(1 −e−b2ym)b3 (130) T(y) = DR · y

To make the model truthfully and accurately reﬂect the actual comprehensive value of the forest, it is signiﬁcant to select u carefully. In our model, we set u as the average of total carbon sequestration for the primary forests worldwide. That means X u = Ajb1j (22) j where Aj denotes the area of each forest, and b1j is one of the coordinates in the expres- sion of C(y) indicating the total cumulative carbon sequestration of the primary forests. According to [4] (see Figure 1), we have calculated that u = 274.1 (tC/ha).

4.2 Economical Index

The Economical Index(EI) evaluates the comprehensive economical value that forestry products provides. Evidently the harvest rate DR is proportional to the beneﬁt of forest industry, and the harvest age y also e↵ects the beneﬁts. Since the amount of woods pro- vided by the forests is proportional to the average volume of trees, to normalize the EI, according to equation (4’), we gives the following expression:

2 1 + e−y −1)(1 −e−b2y)b3 EI = DR · ( (23)

Here we multiply a sigmoid term since it is hard for too young trees to be made for products. And it is acknowledged that there is no economic value within too young trees for the forest industry, hence we may consider the limitation of inequality (14), i.e.,

y > w. (14)

4.3 Biodiversity Index

In our model, the harvesting rate DR and the harvest age y can both e↵ect the biodi- versity of the forests. In detail, the harvesting rate is proportional to the negative e↵ect by the harvest process; while the negative e↵ect is increasing when the harvest age y changes from w to ym. But the marginal e↵ect is decreasing, which is consistent to the common sense. Hence we deliberate the Biodiversity Index (BDI) and it is calculated by:

! 2 BDI = 1 −DR · log2 2 − (24) 1 + e−y/ym

Speciﬁcally when DR = 0, there is no harvest, and the case when BDI = 1 means that it is in the best state of ecological environment; and when DR = 1, the negative e↵ect for the biodiversity resulted by harvest is increasing w.r.t. the harvest age y. Moreover, due to the property of sigmoid function, the derivative of BDI is decreasing when y increases.

Next, when y = 0, it holds that BDI = 1 −DR, and this means that the BDI is completely proportional to the una↵ected area; when y = ym, the logarithm term is not 0, since the harvest age can near the average lifespan of the trees, but it is nearly 0, so that the e↵ect of the harvest can be ignored and can smoothly transit to the case with no harvest.

4.4 Analytic Hierarchy Process (AHP)

When evaluating the weights, the methodology that we exploit here, AHP, is most widely adopted. Practically, subjective method preserves more scientiﬁc rationality as objective method cannot realize certain criteria. Using this method can reﬂect the relative signiﬁcance among the three indexes in spite of the essence of each and deﬁne the weights naturally. As a result we take the subjective AHP as our main approach rather than other more objective models when deciding the weights.

Considering that there’s di↵erence in preference between developing and developed countries, we set up two sets of weights and calculate two sets of data as follows:

Finally, when the harvest rate DR is deﬁnite, the CIF is a function of y, but the limitations of inequalities (14) and (15) also work, i.e., the model makes sense only when (160) w < y < ym.

And just like the initial model, if for some y < ym, CIF(y) gets maximum, then it indicates that the optimal forest management plan is that we harvest those trees if and only if they are in the age of y years old; otherwise we should never harvest these trees.

4.5 Evaluating the total value of a forest

In the model above, we have calculated the Comprehensive Index of Forest, which reﬂects the comprehensive value of the forest for unit area. In this way, a simple idea is that the total value of the forest is simply the product of CIF and its area S 0, or its tree coverage area S . However, take the topography of the forest into consideration, we have to modify it a lot.

Concretely, we deﬁne the Total Comprehensive Value of Forest(TCVF) as follows:

TCVF = !1TCS V + !2TEV + !3T BDV (25) where TCS V, TEV and T BDV denotes Total Carbon Sequestration Value, Total Eco- nomical Value and Total Biodiversity Value.

There is many kinds of regions not covered by woods in the forest, including wet- lands, lakes and grasslands. Since they can also absorb a lot of carbon, we express the Total Carbon Sequestration Value (TCS V) as:

TCS V = S 0 · CS I (26) Although the regions not covered by woods have ecological signiﬁcance, we can not get wood materials from them, even if they can provide other by-products such as ﬁsh and aquatic plants. To simplify our model, we only consider the harvest of woods, hence we evaluate the Total Economical Value (TEV) as follows:

TEV = S · EI (27)

Ecologist have found that wetlands, lakes and even grasslands can have much eco- logical signiﬁcance. Hence we separate the forest into woods and non-wood regions.

In the woods, due to the harvest of trees, the environment is e↵ected and hence in- ﬂuence the biodiversity; and in the non-wood regions, there is no deforestation, hence harvest process have little inﬂuence on the biodiversity in these regions. Then the Total Biodiversity Value (T BDV) is:

! 2 −y T BDV = S · BDI + (S 0 −S ) = S 0 −S · DR · log2 (28) ym

Since we have considered the topography of the forest, the average value of a forest (AVF) is a little di↵erent from CIF. According to equations (25), (26), (27) and (28), we deﬁne AVF as:

AVF = TCVF = !1CS I + S !2EI + !3[1 −S (1 −BDI)] (29) S 0 S 0 S 0

If we deﬁne ⇢= S S 0 as the proportion of the woods of the forest, then, we can rewrite equation (29) as

(280) AVF = !1CS I + ⇢!2EI + !3[1 −⇢(1 −BDI)]

5 Case Studies

5.1 Case 1: Quaking aspen forests in temperate climate

Quaking aspen (Populus tremuloides) is the most widely distributed tree in North America[14]. It is broadly distributed in temperate and boreal regions such as the north- ern United States and most parts of Canada (see Figure 6). In this case, we will only consider the quaking aspen forests distributed in temperate climate.

According to the National Wildlife Federation, most of the quaking aspens have a lifespan of 50 to 60 years[14]. In our model, we take the average lifespan ym = 55 years. Using our model of Comprehensive Index of Forest for developed countries, we can get the relationship between CIF and y when the harvest rate DR = 1. And the y−CIF curve is shown in Figure 7.

And the part of y < w where w = 8.674 years according to Section 3.2 is meaningless due to limitation of inequality (14). Evidently the CIF is increasing when harvest age y changes from w to ym. And according to our model, since CIF(y) never gets maximum when y < ym, it indicates that we should never harvest these trees.

Since the United States and Canada are both developed countries, in our model, they may pay much more signiﬁcant attention to the ecological value of quaking aspen forests than the economic value of the forests, hence the CIF value goes up when y increases, which is basically consistent with the facts.

According to the previous analysis, it is found that if the lifespan of trees in the forest is small and it is considered that the conservation of environment and biodiversity is quite important, there are cases when it is optimal to leave the forests uncut.

5.2 Case 2: Amazon rainforests in Brazil

The protection of Amazon rainforests has attracted worldwide attention. Considering that the country is the main power to conduct the regulation to protect forests and every countries have di↵erent laws and cultures, we just consider the main part, Brazil part, of Amazon rainforests.

Centennial carbon sequestration of Norway forests

The Amazon rainforests is mainly located between 10◦S and 10◦N, and the climate there is the tropical rain forest climate, i.e., it is hot and rainy all year round[16]. So in our calculation we assume that all of the Amazon rainforests are tropical forests.

To calculate the centennial carbon sequestration of Amazon rainforests in Brazil, it is appropriate to use the initial model, i.e., to minimize the T(y). In Section 3, we have calculated that the best harvest time for such category of trees is y = 59.90 years. Ac- cording to the model, the annual carbon sequestration of Amazon rainforests in Brazil is the average cumulative carbon sequestration among trees between 0 and y years old, i.e., C0(y) = C(y) (30) y where C(y) = ym y b1(1 −e−b2y)b3 (5)

Then, when a period of 100 years is considered, the total amount of carbon sequestration is calculated by:

100 · C(y) · Forested Area (31) y According to the data in Section 3, we can get that C(y) = 690.40(tC/ha). Moreover, since the total forested area of Amazon rainforests is 5.5 ⇥108ha and there is an area of 3.212 ⇥108ha[16] located in Brazil, the total amount of carbon dioxide sequestered by the Amazon rainforests in Brazil in 100 years is hence 3.702 ⇥1011 (tC).

Comprehensive Index of Forest for Amazon rainforests in Brazil

In Section 4, we have deﬁned the Comprehensive Index of Forest (CIF), and then we will conclude the optimal management plan for Amazon rainforests in Brazil by calcu- lating the y −CIF curve and ﬁnd the maximum point for CIF.

According to [18], the gross domestic product of Brazil per capita is 8228.79 US dollars, which indicates that Brazil is a typical developing country. Hence in this model the weight for economic should be quite high, and we will use the data for developing countries in Section 4.4 (see Figure 5).

And we also need to estimate the deforestation rate. According to [16], in the Amazon rainforests, the regions that are conserved well is approximately 1.0 ⇥108ha. Then we can estimate that the deforestation rate DR is 0.818, and summing up all the available data, we can have the following y −CIF curve (see Figure 9).

From the curve, we can get than the optimal harvest age is y = 134.15 years and the optimal plan is to harvest the trees which get to 134.15 years (with the current deforesta- tion rate DR = 0.818).

Improvement of the current management plan

According to [19], by the year 2018, 17% of the Amazon forest was reported as having been lost, and in some year, there could be over 10,000 square miles (about 2.59⇥106ha) razed within 12 month periods. Since the deforestation rate is DR = 0.818, we can calculate the equivalent harvest age currently is y0 = 173.70 years.

If we prolong the gap between two harvests by 10 years, i.e., change the harvest age to y00 = 183.70 years, according to our model, the ecological indices such as Carbon Sequestration Index and Biodiversity Index will increase but the Economical Index may decrease. Hence the Brazil government need to compensate for the economic loss of forestry industry in the Amazon rainforests in Brazil.

In our model, the Economical Index (EI) evaluates the comprehensive economical values that forestry products provides, indicating the degree of the development of the forests. And the y −EI curve is shown in Figure 10.

According to equation (23), before the change, the EI(y0) = 0.8477 and after the change, the EI(y00) = 0.8074. Hence the relative change of the EI is

⌘0 = EI(y0) −EI(y00) = 4.754% (32) EI(y0)

According to [20], the forestry industry production of 2019 in Brazil is 20 billion Brazilian reals (about 3.892 billion US dollars). To smoothly transit from the current management plan to the improved one, the loss of the Brazilian forestry industry produc- tion should be compensate by the Brazil government.

According to [22], the Brazilian government monthly revenue (in December 2021) is 193.9 Billion Brazilian reals (about 37.73 billon US dollars), i.e., the annual revenue can get to 2326.8 Billion Brazilian reals (about 452.8 billon US dollars).

If the Brazil government spare 1% of the current annual revenue for the compensation of the forestry industry production, then it may need 61 years to fully cover the economic loss and then the expenditure of Brazil government can decrease to 20 billion Brazilian reals.

Since the GDP of Brazil increases by 4.5% in 2021, it will put less and less pressure on the Brazil government, and it will bring lots of ecological beneﬁts for the local resi- dents and the human beings. Hence, it is recommended to practice such an environment- friendly management plan.

5.3 further study

In this part, we would like to use the further adjusted model presented in section 3.5 to give more details analysis.

Using our model, we found out that it is better to cut down the portion that belongs to tree types whose longevity sits around 231 years old, such as Cymbopetalum baillonii and Poulsenia armata[21].

Hence, under the same condition, we would choose to cut the trees whose age is over 59.9 years old and prioritize the ones that have a longevity around 231 years old, just as the diagram below illustrates:

6 Sensitivity analysis

In this section, we test the sensitivity of our models through changing parameters and comparing the di↵erence between the original results and changed results.

Firstly, in equation (13), the total carbon sequestration of forests and products per hectare at time y is related to the coordinates b1, b2 and b3, and it is proportional to the average lifespan of the trees. Moreover, it is also relevant to w, the weighted factor of carbon sequestration within products, but not linearly. When the type of wood products changes, w also changes and the shape of T(y) changes, too. And we check the cases when w changes from 2 (Paper & paperboard) to 35 (Sawn wood) years. Take tropical forests as example, when w changes, the di↵erent T(y) curves are shown below (see Figure 12).

As we can see, the abscissae of maximum points change from 66 to 43.5 years when w changes from 2 to 35 years. Hence di↵erent types of products may a↵ect the optimal harvest years.

7 Strengths and weaknesses

Strengths

• Data are reliable and accurate. We collected data from authorized sites such as FAO and they are all up-to-date, i.e., most of the numbers are recorded within 5 years dating back from 2022.

• The results of our models are coherent with real-world data and common sense.

We use AHP and existing models such as The Faustmann Model, so our model is scientiﬁcally reasonable.

• We have covered various aspects and factors in our model, making it organized and versatile, i.e., can be applied widely for di↵erent climatic zones.

Weaknesses

• Sudden factors are ignored in our calculation. In fact, ﬁre events and earthquakes are inﬂuential for most forests in the world, and they actually take place quite frequent.

• Real-world forest compositions are not fully considered. In our model, we break- down the forest into harvestable and unharvestable regions as an analogous ap- proach to distinguish between trees and non-tree areas.

ICM Time‘

MCM/ICM Contest Problem E

VOL.I. . . No.1

Deforestion, yes or no?

By #2216618

Deforestation is one of the strictest global issues that emerges in the ﬁeld of politics, sociology and economics.

Throughout the history, most citizens are educated that over deforestation breaks the environment’s stability, as trees are the main sources that contribute to the remediation of earth’s atmosphere by se- questering carbon dioxide out of it. FEBRUARY 21, 2022

Due to the fact that the theoretical op- The model we present values whether According to the World Wide Fund for timum for cutting down is greater than the a forest’s trees are to be cut or not by an Nature, "up to 15 billion trees are now average life expectancy, we end up with index called the "Comprehensive Index being cut down every year across the no harvesting at all as the best approach. of Forest". (⇠퐼퐹). It serves as a number world". that calculates a forest’s value if some of Amazon rainforests: Because Brazil the trees are cut at a certain year after its plantation. Seemingly, there’s an urgent need for the world to take actions, slowing and is a developing nation, well-organized cut- ting is beneﬁcial in both ecology and econ- omy. Additionally, it has the potential to The ⇠퐼퐹is deliberately calculated even completely stopping deforestation. generate funds for local governments to that it incorporates carbon sequestration invest more for the environments. eﬀects, economical beneﬁts and biodiver- However, a new study led by members sity values simultaneously. of our team from The International Car- bon Management Collaboration (ICM) Hence, we end up with some planned cutting. In fact, it is better to cut down As a result, we can make estimation will yield an astonishing impact to the trees when they are 59.9 years old. And of the best year to harvest trees in any society. since we can only cut part of the trees, we type of forests by ﬁnding the year such prefer tree types that has a longevity close that ⇠퐼퐹reaches an optimum. A ﬁrst principal that guides their in- vestigation is: The regrowth of younger to 231 years old. We chose two forests as our real-life forests has the potential to allow for more In a nutshell, we advocate most com- case studies: Quaking aspen forests and carbon sequestration over time when com- munities in the developing countries and Amazon rainforests. The conclusions are pared to the carbon sequestration beneﬁts very impressive. of not cutting forests at all. forests that meet the criteria of cutting trees (i.e. the expected year of trees cut- ting calculated in the model is much ear- Quaking aspen forests: Because lier than the lifespan): do you still think Canada and the US are developed nations, Sensing this pattern, our team devel- that deforestation and harvesting are bad they can shift their focus on elevating the oped a forest management plan that com- when it is just the right time to maximize? overall social and ecological eﬀects of the bines social, economical, and ecological factors altogether. forest.
