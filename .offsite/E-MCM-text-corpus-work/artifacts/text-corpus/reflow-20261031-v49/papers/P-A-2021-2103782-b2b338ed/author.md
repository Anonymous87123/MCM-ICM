MCM/ICM

Summary Sheet

Summary

Fungi, as almost the only lignin-decomposing species on Earth, play an important role in the global carbon cycle. In this paper, a mathematical model is established to analyze various factors affecting the decomposition rate of woody fibers by fungi, so as to deepen the understanding of the relationship between fungal communities and ecosystem functions.

Firstly，we establish a Logistic Growth Model based on the interactions between different species of fungi. Considering the growth model and the moisture tolerance of the fungus, the decomposition rate model of fungi on woody fibers is constructed. Then, we use the collected fungal dataset and obtain the unknown parameters of the model. Next, we choose a combination of fungi to test the model. The relative error between the calculated decomposition rate and the actual value is as low as 5.5%. Meanwhile, the interactions between different species of fungi in a fixed patch of land are analyzed.

Secondly, considering the rapid environmental fluctuations, we analyze the effect of humidity on fungal activity in detail. We select a typical climate to study the short-term and long-term trends of fungal growth and decomposition rate, as well as the interaction between fungi. We find that the increase of environmental humidity can promote the growth of fungi with different promotion degree. Meanwhile, the relative competitive advantages of various fungi are different when atmospheric trends change. This will lead to the succession of fungal communities in different directions. Moreover, we also find that fungi with stronger moisture tolerance are more likely to occupy a dominant position in the arid environment.

Thirdly, we employ K-means algorithm to cluster the collected dataset of fungi and analyze the advantages and disadvantages of fungal species and combinations of species in different environments. In terms of the difference of environmental humidity, we find that fungal communities with stable characteristics are more dominant in low humidity environments. When the changing rate of environmental humidity is different, fungi with slower hyphal extension rate and stronger moisture tolerance are more robust to the environmental changes. For the environment with little climate change, such as tropical rain forest, fungi with faster growth rate and weaker moisture tolerance are more dominant. What’s more, fungi with similar characteristics are more likely to coexist.

Fourthly, the result of negative impact of environmental changes on a relatively single fungal community indicates that the more abundant species diversity, the more capable of adapting to the environmental changes. Thus, the decomposition rate can be maintained at a high level, which is conducive to the carbon cycle.

Finally, we analyze the sensitivity of the unknown parameters, and it shows that the model has strong adaptability and is easier to popularize. In addition, the advantages and disadvantages of the model are also analyzed.

Relations; Biodiversity

1 Introduction

1.1 Problem Restatement

微信公众号：数学模型 As the dominant decomposers of organic plant material, fungi play an important role in the global carbon cycle. Fungi can decompose plant material and woody fibers, allowing carbon to be renewed and used in other forms. The diversity of fungal communities can provide a tangible link between biological communities and ecosystem functions. Therefore, fungi are the key driver of ecosystem function, and researches on fungal function have great significance on exploring biodiversity and realizing the material cycle in the ecosystem.

In order to explore the large-scale modeling of the carbon cycle and global climate models, we will conduct research on the factors that affect the decomposition rate of fungi to wood based on the growth rate of the fungus and the fungus’ tolerance to moisture. Our research needs to include the following tasks: ⚫ Establish a mathematical model to describe the decomposition of woody fibers in the 微信号：MATHmodels presence of multiple species of fungi. ⚫ Incorporate the interactions between different species of fungi. ⚫ Make dynamic analysis of the model and the interactions between different kinds of fungi, and consider the influence of environmental fluctuations on the model. ⚫ Analyze the relative advantages and disadvantages of each species or species combination, and predict the wood decomposition rate for different environments. ⚫ Explore the effect of fungal community diversity on decomposition rate, and predict the importance of biodiversity when the environment changes.

1.2 Literature Review

A number of researchers have previously contributed to wood decomposition by fungi. Diogenis A. Kiziridis et al. used ordinary and partial differential equations to establish spatially explicit simulation models to incorporate factors that influence fungal interactions, thus predicting the dynamics of fungal communities[1]. The study of Tiina Rajala et al. found that fungal communities in wood depend on C : N ratio which is different in different regions, thereby affecting the decomposition rate of woody fibers[2]. Daniel S. Maynard et al. designed a trait-based approach to explore the dominance-tolerance trade-offs of fungi at broad spatial scales, strengthening the understanding of fungal biogeography[3]. In recent studies, Nicky Lustenhouwer et al. found that the decomposition rates were consistent with dominance- tolerance life-history trade-off of fungi through detailed trait-based assays, which improved the ability to predict wood decay[4]. The above studies provide a wide range of ideas for our model establishment.

1.3 Our Work

We mainly build two models to solve this problem. The influence of environment on the activity of fungi and the importance of biodiversity are studied by selecting the fungi combination with representative traits. After establishing and solving the model, we carry out a sensitivity analysis, providing the advantages and disadvantages of the model, and make a prospect for the future work. At the end, we write an article for a college biology textbook about our understanding of fungal activity in the ecological environment.

微信公众号：数学模型 微信号：MATHmodels

2 Assumptions and Justifications

In order to simplify the model, we make the following assumptions: ⚫ Fungi can only reproduce asexually. Since the model focus on the vegetative stage of fungi, we assume that there is no gender difference in the fungi studied. ⚫ The growth of mycelia spreads outward in a circular form and has a maximum growth radius. The growth of mycelium usually starts from the position of spores and spreads radially around. In addition, due to the limitation of environmental resources, mycelium cannot grow indefinitely. Considering the hyphal extension rate is the focus of research, we make this assumption to simplify the model. ⚫ The decomposition rate of fungi to ground litter and woody fibers is the mass loss rate of woody fibers over time. The decomposition of plant material and woody fibers is a key component of the carbon cycle, so we just focus on the role of fungi in the global carbon cycle. ⚫ Only fungal activity causes the decomposition of ground litter and woody fibers, and wood decomposition is regarded as the only nutrient source of fungi. Fungi are almost the only creatures on earth that can decompose lignin, so in order to better analyze fungal activity, we only consider the effect of this point on wood decomposition. ⚫ The effect of fungi on all stages of wood decomposition is consistent with the middle 微信公众号：数学模型 stage of wood decay cycle. According to the Research Article Synopsis provided by the problem, fungi are most associated with the decay of woody materials in the middle of their decay cycle. Therefore, for the purpose of modeling exercise, we make this assumption.

3 Notations

The primary notations used in this paper are listed in Table 1.

Symbol

Definition

Growth radius of the k-th fungus ( ) k r ( ) k Hyphal extension rate of the k-th fungus v 微信号：MATHmodels ex R Maximum value of the growth radius of a fungus m Standard value of the competitive ranking of the k-th fungus (scaled ( ) k Rank to the range of [0,1]) D

Standard value of the moisture niche width of the k-th fungus (scaled ( ) k Width to the range of [0,1]) M

Relative moisture tolerance of the k-th fungus ( ) k MT

( ) k v the rate of growth of the k-th fungus F

Relative value of the competitive ranking of the i-th fungus compared  ( ) k i with that of the k-th fungus Mass loss of woody fibers caused by the decomposition of the k-th ( ) k M L fungus

 M Maximum value of the mass loss of woody fibers L max

4 Wood Decomposition Model of Multiple Fungi in a Patch of land

4.1 Growth of fungi

In this paper, fungi grow through the extension of hypha, and the aggregation of hypha is mycelium. In addition, the fungi studied in this paper all propagate asexually through spores produced by hyphal differentiation. Since the growth of mycelium usually starts from the position of spores and spread radially around, we regard the growth of fungi as a concentric circle expansion process. The extension speed of the radius is the mycelial growth speed of fungi. The schematic diagram is shown in Figure 2.

微信公众号：数学模型

We first consider the ideal situation where the mycelium can reproduce endlessly in the case v , the of unlimited space and natural resources. Assuming that the hyphal extension rate is 微信号：MATHmodels ex growth radius r of mycelium should conform to the following equation:

dr dt = v r (1) ex

Due to the limited growth environment, the growth radius of mycelium has a maximum R , so the blocking factor of the maximum growth radius should be included on the right value m side of equation (1). Therefore, we introduce the Logistic Growth Model, then the equation (1) can be rewritten as follows:

dr r = − v r (1 ) (2) ex dt R m

In a fixed patch of land, we consider that there may be a variety of fungi, and each fungus ( ) k r has multiple colonies. Let denote the growth radius of the k-th fungus in the same land, which should meet the following equation:

( ) k ( ) k dr r = − ( ) k ( ) k v (1 ) r (3) ex dt R m

In addition, we should also choose the initial growth radius of fungi. The initial growth radius of all kinds of fungi is the same, which is 0r .

= = ( ) k r r (4) 0 t t 0

Finally, we can get the following first order linear differential equation that reflects the relationship between the growth radius of fungi and time.

 ( ) k ( ) k dr r = − ( ) k ( ) k v (1 ) r  ex dt R (5) m  = ( ) k r r 微信公众号：数学模型  0 = t t 0

By solving the above differential equations, we can get the relationship between the growth radius of fungi and time.

R = ( ) k m r   R (6) t   + − − − ( ) k 1 ( 1)exp v ( t t ) m   ex 0 r 0

4.2 Competition among different species of fungi

When a variety of fungi exist in the same patch of land, certain interactions will occur among different species of fungi. In this paper, the interaction is regarded as the competition among different fungal communities. Since we assume that woody materials are the only nutrient 微信号：MATHmodels source of fungi, the competition among different species of fungi is the competition for nutrients.

Competitive ranking is the advantage measure of a fungus in competition compared with other fungi under the same conditions. We introduce it into the logistic model of fungus growth. For a species of fungus, when it competes with other types of fungi, there is a relative value between the advantages of other kinds of fungi and that of this kind of fungus. This relative value will become a factor that block the growth of this fungus.

Assuming that there are n kinds of fungal colonies in a fixed patch of land, then we study the effects of other kinds of fungi (i) on the k-th kind of fungi. The equation (3) that the growth radius of the k-th kind of fungi satisfies should be rewritten as:

( ) k ( ) k ( ) i n -1 dr r r − = −  ( ) k ( ) k ( ) k v (1 ) r (7) ex i dt R R i m m

 ( ) k Where is the relative value of the competitive ranking of the i-th fungus compared with that i of the k-th fungus, i.e., ( ) i Rank D  = ( ) k (8) i ( ) k Rank D

( ) k The variable Rank whose value is the standard values that are scaled to the range of [0,1] D represents the competitive ranking of the k-th fungus.

Therefore, we introduce the competition relationship between different species of fungi into the model. This competition relationship will block the growth of fungi, and then affect the decomposition rate of wood by fungi.

4.3 Decomposition of woody fibers

The mycelium as the basic structure is compatible with its nutritional mode. It can be found from the figures provided in the problem that fungi are affected by factors such as hyphal extension rate, moisture tolerance and temperature during the decomposition of woody fibers.

Therefore, we divide the factors affecting the decomposition rate into two aspects: fungal traits impact factors and ambient impact factors when establishing the mathematical model of the decomposition process of woody fibers by fungi.

微信公众号：数学模型 The decomposition rate of fungi to woody fibers is the mass loss rate of woody fibers, that   d M ( ) / t dt M ( ) t is , where is the mass loss in woody fibers. L L

4.3.1 Fungal traits impact factors

In this part, we analyze a certain kind of fungus( ) k in a given patch of land.

( ) k v ⚫ Growth rate F The extension speed of fungus radius is regarded as the rate of growth of a fungus, i.e.,

( ) k dr = ( ) k (9) v F dt We obtained the trend of the relationship between the growth rate and the decomposition 微信号：MATHmodels rate from the dataset of 34 species of fungi, as shown in Figure 3.

( ) k MT ⚫ Relative moisture tolerance The equation of relative moisture tolerance is as follows:

( ) k ( ) k (10) = − ( ) k MT Rank Width D M

( ) k Width The variable whose value is the standard value that scaled to the range of [0,1]. M represents moisture niche width. The definition of moisture niche width is the humidity range that can make the hyphal extension rate greater than or equal to 50% of its maximum value. The ( ) k MT range of is [-1,1].

It is found that moisture niche width is negatively correlated with hyphal extension rate and competitive ranking, which is consistent with the conclusion in the references given in the problem. Fungi that can be better able to survive in more diverse humidity conditions have ( ) k MT slower decomposition rate of wood. Therefore, the smaller the value of is, the stronger moisture tolerance of the fungus is and the slower the decomposition rate of the fungus is.

We explore the relationship between relative moisture tolerance and decomposition rate of 34 kinds of fungi, and obtain the relationship curve shown in Figure 4. Finally, it is found that the decomposition rate has a logarithmic relationship with relative moisture tolerance, i.e.,   ( ) k dM 微信公众号：数学模型 ( ) k ln L MT .   dt  

微信号：MATHmodels

4.3.2 Ambient impact factors

Related studies[3] have shown that ambient humidity, etc. can also affect the rate of decomposition of woody fibers by fungi. However, in this part, we only discuss the decomposition process in a certain patch of land, and regard the environmental variables as constant values. In the follow-up discussion of the effect of environmental changes on the rate of decomposition of woody fibers, we will make a detailed analysis of the ambient impact factors.

4.3.3 Decomposition model of wood fiber

Through the above analysis, when multiple fungi exist in a fixed patch of land, the characteristics of fungi (including growth rate and relative moisture tolerance) and the competition between different kinds of fungi will affect the decomposition rate of woody fibers  ( ) k in this land. Therefore, assuming that M represents the mass loss of woody fibers caused by L the decomposition of the k-th fungus, the rate of mass loss can be expressed as:

 ( ) k d M ( ) k  =  MT ( ) k L v e 2 (11) 1 F dt ( ) k ( ) k MT Where v is the growth rate (determined by equation 9); is the relative moisture F  and  are the unknown parameters. tolerance (determined by equation 10); 1 2

The mass loss of the woody fibers in a fixed patch of land is the result of the combined action of all kinds of fungi in unit time. Meanwhile, considering that the mass of woody fibers  M cannot be lost indefinitely, we define a maximum mass loss value , which can also be L max regarded as the initial mass of wood. Thus, the decomposition rate of woody fibers in a patch of land satisfies the following equation:

  d M M    ( ) k  = −  MT ( ) k L (1 L ) v e (12) 2   微信公众号：数学模型   1 F  dt M k L max

4.4 Model Solving

4.4.1 Methods and results of solution

 and  of the above model are constant under We consider that the unknown parameters 1 2 the same conditions. In order to solve the unknown parameters in the model, we collect the experimental data of 34 species of fungi, including hyphal extension rate, moisture tolerance, competitive ranking and decomposition rate of wood fiber. And we select six groups of three kinds of fungi which are shown in Table 2 as the training set for our solution. Then we search  and  in a reasonable range, and use the obtained parameters to the values of parameters 1 2 calculate the decomposition rate of all combinations of fungi. By comparing the obtained 微信号：MATHmodels decomposition rate with the actual decomposition rate, we choose the parameters which can  and . minimize the error of decomposition rate as the values of 1 2

Fungus 1 Fungus 2 Fungus 3

Group 1 Armillaria_gallica_FP1 Hyphoderma_setigerum_F Merulius_tremellosus_FP15 02531_C6D P150263_B2C 0849_C3F Group 2 Armillaria_gallica_EL8 Armillaria_gallica_SH1_A Armillaria_tabescens_FP102 _A6F 4A 622_A3C Group 3 Armillaria_gallica_EL8 Armillaria_gallica_FP1025 Armillaria_gallica_FP10253 _A6F 34_A5A 5_A5D Group 4 Armillaria_gallica_FP1 Armillaria_gallica_OC1_A6 Armillaria_sinapina_PR9 02531_C6D E Group 5 Armillaria_gallica_SH1 Armillaria_tabescens_FP102 Armillaria_sinapina_PR9 _A4A 622_A3C Group 6 Phellinus_gilvus_HHB Phellinus_hartigii_DMR94 Porodisculus_pendulus_HH 11977_C4H _44_A10E B13576_B12C * The fungal data are available in ref. 3.

 and  are as follows： The specific steps for solving and testing parameters 1 2

Step 1: Select 6 groups of fungi among all 34 species.

 and  with the step size of 0.01 in the Step 2: Search for the unknown parameters 1 2 range of [0,0.5], and find the more accurate range of the parameters to minimize the error.

 and  with the step size of 0.01 in the accurate range to Step 3: Search the parameters 1 2  find the accurate values that minimize the error. The values are taken as the final parameters 1  of the decomposition model. and 2 微信公众号：数学模型 Step 4: Choose another combination of three kinds of bacteria, and use the calculated parameters to solve the decomposition rate. Use the relative error between the calculated value and the actual value to test the correctness of our model and the reliability of parameter selection.

The results of parameters are shown in Table 3.

  Root Mean Square Error 1 2 0.0033 0.1674 123.42

4.4.2 Model testing

We choose another three kinds of fungi (Armillaria_gallica_FP102542_A5B, 微信号：MATHmodels Hyphoderma_setigerum_HHB12156_B3H, Mycoacia_meridionalis_FP150352_C4E) in order to test the rationality of our model and parameters. Their actual decomposition rate is 29.61% in a certain environment. By computing the model, we get that the decomposition rate is 33.48% with the 5.5% relative error. The error is within the acceptable range, which proves that our model and parameters are reasonable.

radius of different fungi and time respectively.

- Time curve                                                                   per day – Time curve Some interactions between different species of fungi can be reflected from Figure 6. For the convenience of description, in the following analysis, the fungi represented by the blue, red, black lines are referred to as fungus in blue line, fungus in red line, fungus in black line. It can be seen from the figure that the growth radius of the fungus in black line increases to the maximum in a short period of time, while the fungus in blue line only survives for the first few days, and then die. The growth radius of the fungus in red line increases slowly in the early stage. In the later stage, the radius of the fungus in black line gradually decrease to 0, while the radius of the fungus in red line increase to the peak. Therefore, we can conclude that black strain is dominant in the short term, and its competitiveness is the strongest, followed by red, and the weakest is blue. However, for some reason, the competitiveness of the fungus in red line is higher than that of the fungus in black line in the later stage. The resources for the black are occupied by the red, causing the radius of the fungus in red line to reach the maximum and the black to die.

微信公众号：数学模型

5 Effects of environmental changes on interactions between fungi

The focus of this paper are two traits of a fungus: the growth rate of the fungus and the fungus’ moisture tolerance. In fact, fungal activity is not only affected by fungal traits, but also by a variety of environmental factors. The study of Daniel S. Maynard et al. [3] finds that ambient humidity has a great influence on the growth rate of the fungus, and they are positively correlated, which can be approximately regarded as a linear relationship. There is also a positive correlation between growth rate and decomposition rate. Meanwhile, when the humidity condition changes, the fungi with different moisture tolerance will show different activity characteristics, and then affect the decomposition rate. Therefore, we will analyze the effects of ambient humidity changes on fungal activities and the interactions between the different types of fungi in detail. 微信号：MATHmodels

5.1 Introduction of humidity

In this part, we study the influence of ambient humidity (in time dimension) on the number of different kinds of fungi. The change of the number of fungi can reflect the interaction between different types of fungi. We choose 3 types of fungi as a group, and study the short-term and long-term activity trends in tropical monsoon climate. The species and characteristics of fungi are shown in Table 4.

No. Name Moisture tolerance Robustness

1 Armillaria_gallica_FP102542_A5B 0.00156 Strong 2 Hyphoderma_setigerum_HHB12156_B3H 0.75337 Weak 3 Mycoacia_meridionalis_FP150352_C4E 0.5695 Ordinary

We first select the annual precipitation data of Mumbai, a representative city of tropical monsoon climate, as is shown in Figure 7. The data can represent the annual humidity change with time of Mumbai. In the existing fungal data, the humidity range corresponding to growth rate is [-5,0], and is adjusted to [0,1] through data standardization. Then, the growth rate and humidity are linearly fitted. Finally, we obtain the three equations of the humidity and growth rate of the fungi, which are as follows:

= + y 0.1421 x 0.1214 1 = − y 5.4363 x 0.3293 (13) 2 = − y 6.9485 x 1.3943 3

y y y represent the growth rate of three fungi respectively. , , Where x is ambient humidity, and 1 2 3 微信公众号：数学模型

Corresponding to the above humidity, the range of annual precipitation data of Mumbai is also adjusted to [0,1]. Thus, the growth rate of different fungi under a certain precipitation condition can be calculated.

5.2 The short-term trends

微信号：MATHmodels Based on the time span of three months, we divided the trend of humidity change into three categories: increasing humidity, decreasing humidity and ligering drought. Then, we use the established model to solve the change of the decomposition rate of fungi, so as to analyze the short-term interaction between fungi.

a. Increasing humidity (6, b. Decreasing humidity (8, c. Lingering drought 7, 8 months) 9, 10 months) (10, 11,12 months)

It can be seen from Figure 7 that the decomposition rate of fungi in 6, 7, 8, 9 months with more precipitation is much better than that in 10, 11, 12 with less precipitation. As shown in

decomposition stops shortly after. This is because fungus 1 has strong moisture tolerance and slow growth rate, so it is at a disadvantage in the early stage and is eliminated. It can be seen from equation (13) that the growth rate of fungus 3 changes faster with humidity changes than fungus 2. Due to the decomposition rate is proportional to the growth rate, when the humidity increases from June to July, fungus 3 is dominant in the decomposition system; when the humidity decreases from January to August, fungus 3 is at a disadvantage due to its faster growth rate.

As for Figure 7 (b), similar to the above analysis, during the period of declining humidity from August to October, fungus 2 has an advantage over fungus 3 because of its slower growth rate.  It can be seen from Figure 7 (c) that when the environment is relatively arid and the humidity change range is not large, the fungus 1 gradually shows an advantage in the 微信公众号：数学模型 competition process. Therefore, we believe that when the decomposition rate of the strains is at a low level, fungi with stronger moisture tolerance are more likely to occupy a dominant position in arid environments.

In summary, when there are differences in the level and changing trend of atmospheric humidity, there are differences in the interaction between fungal communities, which will cause fungal communities to succeed in different directions in the short-term, that is, the dominant species of the communities are different.

5.3 The long-term trends

We take June as the initial date to analyze the growth of various fungi and the decomposition rate of wood in this year. The results are shown in Figure 9 and Figure 10.

微信号：MATHmodels

different types in the long term                                              of fungi As shown in Figure 9, in the process of interaction between the three fungi, fungus 1 is always at a disadvantage due to the slow growth rate. In the early stage of the increase in humidity, fungus 2 was at a disadvantage in the competition, but in the later period, as the humidity gradually decreased, the growth rate of fungus 2 gradually accelerated, and finally occupied the dominant position. Combined with the analysis of short-term trends, this is related to its better robustness, that is, a more stable growth rate. At the same time, it also confirms that fungi with stronger moisture tolerance are more able to adapt to more drastic changes in the environment and are in an advantageous position.

Meanwhile, the change of growth rate affects the decomposition rate of woody fibers. It can be seen from Figure 10 that in the early stage, when fungus 3 are in a dominant position in the competition, the decomposition rate of woody fibers is also increasing. At the same time, the decomposition rate of fungi 2 is inhibited to a very low degree. It is worth noting that the ordinate in the Figure 10 represents the percentage of daily decomposed wood fiber mass in the total mass. However, the growth rate of fungus 2 increases and the decomposition rate of woody fibers also increases when the humidity drops later. Concurrently, the decomposition rate of woody fibers by fungus 3 is inhibited. In this fixed patch of land, fungus 2 is the dominant specie.

6 Predictions about fungal activities under the various ambient

changes

微信公众号：数学模型

6.1   Clustering of fungi

When analyzing single species and combinations of species, 34 species of fungi are clustered for convenience of discussion. Taking hyphal extension rate and relative moisture tolerance as characteristic quantities, we use K-means to get the clustering results as shown in

微信号：MATHmodels

Through the previous analysis, we conclude that the larger the relative moisture tolerance value, the weaker the robustness of fungi to ambient humidity changes. Therefore, according to the clustering results, we summarize the characteristics of four types of fungi and list them in

Clustering 1 Clustering 2 Clustering 3 Clustering 4

Growth rate fast slow slower slow

Robustness to weak weaker weaker stronger moisture changes

In order to analyze the influence of environmental humidity on different species and combinations of species, we make the relationship between the hyphal extension rate of the above four kinds of fungi and humidity, as shown in Figure 12. In order to describe the overall trend of the hyphal extension rate of each kind of fungi with the change of humidity, trend lines are added to distinguish the change rate. We think that extremely high humidity is rare in the natural environment, so we don't consider the decline stage of hyphal extension rate.

微信公众号：数学模型

The four trend lines’ equations in the figure are shown in Table 6.

微信号：MATHmodels

Clustering 1 Clustering 2 Clustering 3 Clustering 4 = − = − = − = + y 9.72 x 1.51 y 2.10 x 0.32 y 4.39 x 0.60 y 0.20 x 0.20 1 2 3 3

6.2   Advantages and disadvantages prediction

Here we use the wood decomposition rate of fungi to measure the advantages and disadvantages of species. If the decomposition rate of one species of fungus is larger than that of another over time, we think that the fungus with higher decomposition rate has the advantage.

6.2.1 Difference of ambient humidity

We select the value of the average annual precipitation in arid and semi-arid areas, and through the numerical range transformation, we get the relative humidity value of 0.08 in the arid area and 0.15 in the semi-arid area.

⚫ Arid area The wood decomposition rate of different types of fungi in the arid area is shown in Figure 13.

Curve 4 represents the fungal species with slow hyphal extension rate and strong moisture tolerance; curve 1 represents the fungal species with fast hyphal extension rate and weak moisture tolerance; the hyphal extension rate and moisture tolerance of curve 2, 3 are not outstanding. The wood decomposition rate of curve 4 increases at the beginning, and goes up to 微信公众号：数学模型 the peak after about 400 days, and then remains unchanged.

The figure indicates that even if the wood decomposition rate of fungus 1 is relatively large at a suitable temperature, due to the limitation of its moisture tolerance, its decomposition rate is lower than that of the other three fungi under drought conditions. In contrast, due to its excellent moisture tolerance, the decomposition rate of fungus 4 has little change compared with the best condition, and is higher than that of the other three kinds of fungi. Therefore, we get the first Prediction.

Prediction 1: In the case of low environmental humidity, the fungal community with more stable characteristics is in a dominant position. On the contrary, fungal community with unstable characteristics is also at a disadvantage even if its decomposition rate of woody fibers is high. ⚫ Semi-arid area 微信号：MATHmodels It can be seen from Figure 14 that the wood decomposition rate of fungus 1 is increasing. In the other three fungi, their wood decomposition rates increase first and then decrease.

In the semi-arid climate, fungus 1 is the most competitive among all types of fungi. Therefore, it can be inferred that the species with the largest increase rate of daily decomposition rate is more competitive. As for the other three fungi, their wood decomposition rates increase first and then decrease. The competitiveness of fungus 4 is close to that of fungus 1, thus can coexist with fungus 1 for a long time. In general, the combination of fungus 1 and fungus 4 has more competitive advantage than the other two species in semi-arid area.

6.2.2 Difference of the changing rate of ambient humidity

微信公众号：数学模型 b. decomposition rate changes with a．decomposition rate changes with the fast-changing rate of humidity the slow-changing rate of humidity 微信号：MATHmodels

First, we select the appropriate humidity range [0.1, 0.7], and adjust the humidity value with the rising rate of 0.005 and 0.2 respectively. The figure on the left shows the rising rate of 0.005, and the figure on the right shows the rising rate of 0.2.

It can be seen from the Figure 15 that when the changing rate of environmental humidity is slow, the time for fungus 4 to maintain the maximum wood decomposition rate is longer than that of fungus under the fast-changing rate of environmental humidity. So, we get the second prediction.

Prediction 2: Under the condition that the surrounding environment is suitable for living organisms, the slower the environmental changing rate is, the higher the possibility of coexistence of multiple species is, and the richer the biodiversity of the community is.

Using this analysis, we study the evolution of fungal communities in temperate marine climate and temperate monsoon climate, and find that the diversity of fungal communities in temperate marine climate is more abundant than that in temperate monsoon climate, which is consistent with our analysis.

What’s more, Figure 15 (b) also shows that fungus 4 has the stronger ability to maintain stability against environmental changes than fungus 3. Thus, we get the third prediction.

Prediction 3: Fungi with slower hyphal extension rate and stronger moisture tolerance are more robust to the environmental changes. That is to say, under the influence of repeated environmental changes, the fungi with stronger moisture tolerance have greater advantages.

6.2.3 Analysis of the advantages and disadvantages of fungi in tropical rain forest

The climate of tropical rain forest is characterized by high temperature and rainy all year round, so its environmental humidity is maintained at a high level and has little change. According to the data, the monthly average precipitation of tropical rainforest climate is 200 mm. Then, we draw the curve of the relationship between the wood decomposition rate and time under the tropical rainforest climate. It shows that fungus is dominant in this climate condition.

微信公众号：数学模型

Furthermore, we select another fungus in clustering 1 instead of that in clustering 2 and draw the following image. The result shows that the wood decomposition rate of red line and 微信号：MATHmodels blue line both maintain high values for a long time, so we can make the fourth prediction.

Prediction 4: Fungi with similar characteristics are more likely to coexist in a fixed patch of land.

7 How does fungal biodiversity impose magic to the carbon cycle

As we all know, without biodiversity, the planet would be at its wit's end in the event of a particular climate change. So how does biodiversity act on the ecological circulation system? In this section, fungi are used as an example to study their essential role in the carbon cycle.

We still use the three specific fungi (Armillaria_gallica_FP102542_A5B, Hyphoderma_setigerum_HHB12156_B3H, Mycoacia_meridionalis_FP150352_C4E) to qualitatively derive the influence of fungal biodiversity on the decomposition efficiency of ground litters by the system. In the analysis of the results in Capture 5, we have realized that in the tropical monsoon climate, the types of fungi decrease from 3 to 1, and the population gradually tends to be unitary (as is shown in Figure 18). Therefore, we can predict that if an environmental change with negative impact is added to a kind of still-living fungi, this fungus will also tend to die.

微信公众号：数学模型

微信号：MATHmodels In order to verify our conjecture, we reduced the humidity to 0.01 after the 175th day (this will have a negative impact on the surviving fungi Hyphoderma_setigerum_HHB12156_B3H). The result is shown in Figure 19. It can be clearly seen that under the influence of negative climate change, the decomposition rate of the surviving fungi gradually decreases, which will eventually make the entire fungal community extinct. Thus, the system cannot well adapt to drastic environmental changes.

On the contrary, if the species diversity of a system is very rich, and then, when the local climate changes, there will be different species to occupy the dominant position, so as to make up for the decreased decomposition rate of woody fibers caused by the decrease of the number of the original dominant fungi. Therefore, the decomposition system can well adapt to the changes of the environment, and the decomposition rate has been maintained at a high level, so the carbon cycle can continue smoothly.

8 Sensitivity Analysis

 and  are the unknown parameters, which are In the decomposition rate model, 1 2 calculated by our algorithm above. They have impact on the model’s result——the  and  artificially to assess the decomposition rate. In this part, we change the value of 1 2 sensitivity of our model.

8.1 Impact of α1 on decomposition rate

on decomposition rate, we fix the value of  as 0.1674. In order to assess the impact of 1 2  value as 0.0023, 0.0033, 0.0043 and plot the wood decomposition rate per day- Then, we set 1 Time Curve.As we can see in the Figure 20, the peak of wood decomposition rate per day . In conclusion, the value of  is varied, which has positive correlation with the value of 1 1 . It shows that crucial to the accuracy of the model, which means that the model is sensitive to 1 the model has strong adaptability and is easier to popularize.

8.2 Impact of α2 on decomposition rate

on decomposition rate, we fix the value of  as For the sake of evaluating the impact of 2 1  value as 0.1574, 0.1674, 0.1774 and plot the wood decomposition rate 0.0033. Then, we set 2 微信公众号：数学模型 per day-Time Curve. In the Figure 21, we can also see the various peak of wood decomposition  changes. However, compared to the impact of , the value of rate per day as the value of 2 1  is less significance to the accuracy of the model. The model is robust to the variation of . 2 2

微信号：MATHmodels

9 Model Evaluation and Further Discussion

9.1 Evaluation of Models

The decomposition of microorganisms is a very important part in the carbon cycle. By establishing models of wood decomposition and fungal growth, we have perfectly met the requirements of question, drawing a series of conclusions about the impact of environmental changes on bacterial species and the importance of biodiversity.

During our modeling process, we set reasonable assumptions to simplify our models. Also, we take the sensitivity analysis which verified the stability of the models.

The specific advantages of our models are as follows: ⚫ We adopt the Logistics growth model with the competition among fungi including in the model, so as to simulate the interaction between species well. Moreover, we reasonably analyze the advantages and dis advantages of species with different characteristics in various environments. ⚫ The calculation of unknown parameters is scientific. Reasonable training set and test set help us make sure the accuracy of parameters.

However, our models still have the following weaknesses: ⚫ Our hypothesis only considers two parameters affecting fungal decomposition, ignoring endogenous and exogenous factors.

⚫ We can only use the existing experimental dataset to calculate the unknown parameter values in our model, and most of the prediction in the biological field can only be predicted qualitatively.

微信公众号：数学模型 ⚫ Our model directly takes the values of humidity tolerance and elongation rate at the center of each cluster as the value to represent the characteristics of that cluster which may leads to some errors in the analysis of the interaction among species.

9.2 Further Discussion and future work

In our model, we only discuss the changes in fungal interactions and decomposition rates under different environmental conditions. But our work only restricted to the fungus point of view. Future work is supposed to focus on whether we can artificially alter the weather conditions to affect the fungal decomposition process in a way that would have a positive impact on the carbon cycle. This theoretical research may provide a plausible solution to the global warming.

微信号：MATHmodels

Appendix

⚫ Clustering results:

微信公众号：数学模型 Clustering Species of fungi Merulius_tremullosus_FP102301_C3E Merulius_tremellosus_FP150849_C3F Clustering 1 Phlebiopsis_flavidoalba_FP150451_A8G Phlebia_acerina_MR4280_B9G Phlebia_acerina_DR60_A8A Armillaria_gallica_FP102542_A5B Armillaria_gallica_SH1_A4A Armillaria_sinapina_PR9 Armillaria_tabescens_TJV93_261_A1E Fomes_fomentarius_TJV93_7_A3E Hyphoderma_setigerum_FP150263_B2C Clustering 2 微信号：MATHmodels Mycoacia_meridionalis_FP150352_C4E Phellinus_hartigii_DMR94_44_A10E Phellinus_robiniae_FP135708_A10G Phellinus_robiniae_AZ15_A10H Banik/Mark Pycnoporus_sanguineus_PR_SC_95_A11C Hyphodontia_crustosa_HHB13392_B7B Hyphoderma_setigerum_HHB12156_B3H Laetiporus_conifericola_HHB15411_C8B Lentinus_crinitus_PR2058_C1B Phlebiopsis_flavidoalba_FP102185_B12D Clustering 3 Phellinus_gilvus_HHB11977_C4H Porodisculus_pendulus_HHB13576_B12C Schizophyllum_commune_TJV93_5_A10A Schizophyllum_commune_PR1117 Tyromyces_chioneus_HHB11933_B10F Armillaria_gallica_FP102531_C6D Armillaria_gallica_EL8_A6F Armillaria_gallica_FP102534_A5A Armillaria_gallica_FP102535_A5D Clustering 4 Armillaria_gallica_HHB12551_C6C Armillaria_gallica_OC1_A6E Armillaria_tabescens_FP102622_A3C Xylobolus_subpileatus_FP102567_A11A
