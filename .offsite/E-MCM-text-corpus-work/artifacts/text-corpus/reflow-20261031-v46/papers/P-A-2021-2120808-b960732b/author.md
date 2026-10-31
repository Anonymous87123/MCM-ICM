Problem Chosen MCM/ICM

Summary Sheet

Summary

Fungi decompose organics into inorganics through their respiration, playing a crucial role in the ecosystem. In this paper, in order to discuss their decomposition ability, multiple species interaction, and significance of biodiversity, we establish three models: Fungal Decomposition Model, Fungai Propagation Model and Fungal Population Competition Model.

To begin with, we collect the original experimental data in literature. After clean- ing off redundant values, we finally obtain 34 fungal samples. Then we examine their credibility through conclusions of reference paper offered in requirement. Further, we sort these 34 samples into 3 categories through hierarchical clustering method in light of their moisture tolerance and hyphal extension rate. It covers Sprinter, Middle-dis- tance runner, and Long-distance runner. Moreover, we put forward 4 potential mod- els for fungal decomposition. Then, applying multiple linear regression analysis, we

obtain Fungal Decomposition Model for multi species after comparison.

Then, we establish population growth model for single species based on the dif- ferential equation. Further, we obtain the Fungal Propagation Model by introducing a relative environmental impact factor. Besides, we build Fungal Population Compe- tition model. Likewise, we quantify the interaction between fungi and environment by the introduction of relative environmental impact factor. Based on these models, we conduct simulations and find that multiple species community’s population scale is 1.5 times that of single species and its decomposition rate will be 1.45 times on the condition of optimal environment and same initial proportions.

Next, we clarified the concrete form of environmental fluctuations. We assume that moisture in environment and temperature change periodically like trigonometric functions. Further, combining the models we established before, we analyze the sen- sitivity of fungal population scale and decomposition rate to rapid fluctuations in the environment both in short-term and long-term. We find that fungi, especially multiple species community, are susceptible to environmental fluctuations in the short term but stay stable in the long term. Likewise, we conduct simulations and find that mul- tiple species community’s population scale will be 1.18 times that of single species and decomposition rate will be 0.93 times under environmental fluctuations.

Besides, we predict the performance of 4 combination of multiple species in differ- ent environment respectively, which includes arid, semi-arid, temperate, arboreal, and tropical rain forests. Moreover, we propose the best combination, the relative ad- vantages and disadvantages of each species in these environments. We also find that fungi community which contains more species tend to survive more easily. Further, we compare the composition rate of single species and multiple species under optimal environmental conditions and fluctuations to illustrate the role and significance of bi- odiversity. We conclude that fungi system with rich biodiversity are more stable and propagate better under environmental fluctuations.

Finally, we discuss the advantages and disadvantages of the models and offer scientific-based and introductory article for college students.

关注数学模型

1 Introduction

1.1 Problem Background

Recent years have witnessed spurt progress in industry and a sharp increase in 微信公众号：数学模型 carbon emission. Therefore, public concerns about striking carbon balance run deep. The carbon element is the fundamental element of all creatures on the earth. It trans- fers among the biosphere, lithosphere, hydrosphere, and atmosphere by various sub- stances. Thus, a carbon cycle has formed. The carbon cycle consists of four steps in- cludes photosynthesis, decomposition, respiration, and combustion. Fungi play a cru- cial role in the decomposition part, attracting people’s attention a lot. They feed on dead plants and animals, acquire nutrients by absorbing dissolved molecules, and re- productive by growing hyphae. It is of great significance to research different factors’ influence on fungal growth, such as temperature and humidity (namely moisture). Then we can get an insight into how to strike a carbon balance.

微信号：MATHmodels (a) Carbon cycle’s four steps (b) Fungal hyphae [1]

1.2 Restatement of the Problem

Considering the background information of fungi and limiting conditions identi- fied in the problem statement, we are supposed to address the following problems:

 Problem 1: Build a mathematical model to describes the breakdown of ground litter and woody fibers under fungal decomposition. Notably, we are supposed to consider the interactions between different species with different growth rates and moisture tolerances.

 Problem 2: Analyze the sensitivity of the model on condition of rapid fluctu- ations in the environment. Describe the interactions between different types of fungi both in the short-term and long-term. Characterize the dynamics of the interactions. What’s more, we should determine the overall impact of changing atmospheric trends to assess the impact of variation of local weather patterns.

 Problem 3: Predict the relative pros and cons for each species and their po- tential combinations and do so for some specific environments.

 Problem 4: Describe how the diversity of fungal communities of a system im- pacts the overall efficiency of a system concerning the breakdown of ground

关注数学模型 litter. Eventually, predict the importance and role of biodiversity in the pres- ence of different degrees of variability in the local environment.

1.3 Literature Review

微信公众号：数学模型 Fungi’s prominent and salient function in terrestrial ecosystems and biodiversity is widely acknowledged. A large number of experiments concerning fungi are carried out. After reviewing the literature, we find that the mainstream analysis method is based on its traits [2-6].

McGill et al. (2006) confirm that the trait-based method within the community requires consideration of the interaction milieu (biotic interactions) [2]. Nicky Lus- tenhouwer, Daniel S. Maynard, and Mark A. Bradford (2020) explored a large number of different fungal traits and their effects on the decomposition of wood [3]. From their research, we decide to use the hyphal extension rate to represent the growth rate, which will be also verified in Data Description part. Further, according to A. van der Wal’s research, we get that wood moisture content and species richness of the fungal community are the best predictors for mass loss in the older stumps [7]. Therefore, we 微信号：MATHmodels will fix our eyes on these two factors when predict. Besides, from Schimel, J.’s study, maintaining water potential is essential to keep turgor pressure, nutrients via sub- strate diffusion [8].

1.4 Our Work & Model Overview

After pre-process the data, we establish three models including fungi decompo- sition model, fungi propagation model and population competition model. Analysis of single species under environmental fluctuations is aimed to test sensitivity. Inter- action effects among multiple species are illustrated by multiple species under optimal environmental conditions.

2 Assumptions and Justifications

To simplify the given problem, we make the following basic assumptions, each of which is properly justified.

 Assumption 1: Moisture Tolerance is a constant for the same fungal com- munity, while presents a linear scale with fungal composing proportion in

关注数学模型 multiple species of fungi.

Justification：From G Ayerst’s research, differences of water activity op- tima, which equals to Moisture Niche Width in our paper, among isolates of individual species are small [9]. Therefore, we reckon that this assump- 微信公众号：数学模型 tion is credible and authentic.

 Assumption 2: The breaking down process of woody materials goes

through multiple stages, during which stages are consistent for the middle cycle.

Justification：The attachment Research Article Synopsis of literature [3] hints that we can focus on the middle stage and make this assumption.

 Assumption 3: Environmental fluctuations are only reflected in changes in temperature and moisture.

Justification：Two major elements of climate are temperature and mois- ture. Moreover, the growth of fungi closely relates to temperature and moisture, so the changes of temperature and moisture can represent the environmental fluctuations. 微信号：MATHmodels  Assumption 4: The interaction between fungi species is mainly reflected in population competition Justification：The relationships between species can be competition and interdependency. But different species of fungi belong to the same kind of creature, and their interdependency is not obvious. Therefore, we only consider their competition to express interaction.

3 Notations

The key mathematical notations used in this paper are listed in Table 1.

Symbol

Description Unit Decomposition rate % mass loss over 122 days Hyphal extension rate mm/day Moisture tolerance - Growth rate mm/day Time day Strain/ Fungi population size Moisture niche width MPa Temperature niche width ℃ Environmental moisture MPa Environmental temperature ℃

4 Data Description

4.1 Data Acquisition & Pre-processing

We utilize Nicky Lustenhouwer’s experimental data in the appendix of his liter- ature [3] and Daniel S. Maynard’s archived data in a dedicated GitHub repository [10]. The archived dataset mainly contains fungal trait data and fungal climate data. The

关注数学模型 supplementary information concludes the decomposition rate. Both of them are con- sistent with the given question’s data. We carefully comb three files, retain the same fungal samples and delete the discrepant data. Finally, we get 34 fungal samples, in- cluding decomposition rate, growth rate, density, competitive ranking, moisture niche 微信公众号：数学模型 width, etc. Moreover, the corresponding websites are as following:

Dataset Website Source https://github.com/dsmaynard/fungal_biogeog- fungal trait and climate raphy https://www.pnas.org/con- supplementary information tent/suppl/2020/05/13/1909166117.DCSupple- mental

4.2 Data Visualization & Validity Examination

As mentioned in the literature [2], fungi with a slow growth rate prone to be better 微信号：MATHmodels able to survive and grow under environmental changes concerning moisture and tem- perature, while faster-growing groups tend to be less robust to the same changes. Fur- ther, adaptive capacity can be represented by moisture niche width and moisture tol- erance stands for the difference between a fungus’ competitive ranking and it. There- fore, the growth rate is supposed to be positively correlated with moisture. After nor- malizing the data with different dimensions, we get the scatter diagram between growth rate and moisture tolerance, which are expected to be positively correlated. Fortunately, as Figure 3 demonstrated, the result is as predicted:

1 0.8 0.6 0.4 Moisture Tolerance 0.2 0 0 2 4 6 8 10 12 -0.2 -0.4 -0.6 -0.8 -1 Growth Rate (mm/day)

Moreover, to verify the relationship between the hyphal extension rate and fungal growth rate, we also depict their scatter graph between them. As Figure 4 demon- strated, the fungal growth rate is consistent with the hyphal extension rate. Since hy- phal extension rate is approximately linearly dependent, it is confirmed that the fea- sibility of using the hyphal extension rate to represent the fungal growth rate. Last but

关注数学模型 not least, due to the characteristic of the two papers’ consistency, we confirm the va- lidity of the data applied in this paper, which can also be proved from Figures 3 and 4.

12 微信公众号：数学模型 10 Growth Rate (mm/day) 8

6

4

2

0 0 1 2 3 4 5 6 7 8 Hyphal Extension Rate (mm/day) 微信号：MATHmodels

4.3 Clustering Analysis

Since we are expected to describe the interactions between different types of fungi, we infer that we need to classify different species into different types in light of their characteristics. In the beginning, the number of clusters has not been determined, so we applied the Systematic Clustering Method for analysis with the help of SPSS. Ac- cording to the Elbow Method, the optimal number of clusters can be estimated.

12.000

10.000 coefficient of polymerization 8.000

6.000

4.000

2.000

0.000 0 5 10 15 20 25 30 35

the number of classes in the cluster

As Figure 5 illustrates, when the number of classes varies from 1 to 3, the coeffi- cient of polymerization decreases sharply. But it ebbs as K continues to expand. There- fore, we assume it will be more reasonable to set K value as 3. Thus, we cluster them again. The results are as following Figures demonstrated:

关注数学模型 微信公众号：数学模型 微信号：MATHmodels

(a) Clustering algorithm flow chart

(b) Clustering pedigree diagram

According to the pedigree diagram and result figure above, we assume that fungi samples can be divided into three types: faster growth rate with high moisture toler- ance (namely worse ability to survive and grow under environmental changes), slower growth rate with low moisture tolerance (namely better ability) and mild growth rate with adequate moisture tolerance. In Figure 6, a faster growth rate group corresponds to the green-dot group (clustering number for 3), a slower growth rate

关注数学模型 community corresponds to the blue-dot group (clustering number for 1), and the last one, the red-dot is for mild growth rate. Also, clustering result can be sorted as the following Table 3:

微信公众号：数学模型 Fungus Features MNW TNW MT category Grow fastest with most narrow Sprinter 1.488 17.82 0.838093895 moisture niche width Middle distance Grow milder with wider mois- 1.75 15.32 0.432854017 runner ture niche width Long distance Grow slowest with widest mois- 3.19 19.9 -0.304769188 runner ture niche width Note: Moisture Niche Width abbreviated as MNW, Temperature Niche Width abbre- viated as TNW and Moisture Tolerance abbreviated as MT.

In Table 3, we set the arithmetic mean value of each species moisture tolerance as the whole category’s moisture tolerance value after clustering. 微信号：MATHmodels

5 Fungal Decomposition Model

In literature [3], researchers measure mass loss in woodblocks to quantify the de- composition process of ground litter and woody fibers. Likewise, we quantify the fun- gal decomposition ability as their decomposition rate over a while (usually %mass loss over 122 days). However, there are many factors that contribute to the fungal de- composition rate. As the required, we only consider moisture tolerance and growth rate.

5.1 Multiple Linear Regression Model

Careful observation of the two figures provided reveals a rough relationship of decomposition rate with hyphal extension rate and moisture trade-off. In order to study the relationship further, we still depict the scatter graph, applying the data we collect, as following figure 8 showed:

关注数学模型 According to the characteristic of our data collected, we reckon several potential types of regression equations as followed:

微信公众号：数学模型 (1)

Where, 𝐷 refers to the decomposition rate, 𝑚 means the moisture tolerance of fungi and 𝐻 represents the hyphal extension rate. As fungal hyphal extension rate closely related to environment temperature and we have got the data of hyphal exten- sion rate under 10℃, 16℃ and 22℃, considering the consistency with the data set processing method, we decide to adopt the arithmetic root mean square value of these three value to comprehensively express the hyphal extension rate. Therefore, 𝐻′ value can be presented as:

(2)

5.2 Parameter Estimation

微信号：MATHmodels We adopt Ordinary Least Squares Method to estimate the parameters in equation (3) with the help of Stata.

Model RMES F P Adj R2 E1 4.031002*** 2.357067 1.396638*** 0.4714 5.2765 15.71 0.0000 E2 5.780003*** 0.3297277*** 3.21938 0.4723 5.2721 15.77 0.0000 E3 2.208966 2.153228** 1.829412 0.4752 5.2573 15.94 0.0000 E4 2.518892 0.2980319** 3.059665 0.4754 5.2566 15.95 0.0000 Note: *** means 99% confidence interval, ** means 95% In light of the regression results above, it is obvious that the corresponding P value (the last column in Table 4) of all the four models’ F value is less than 0.01, so all the four models have passed the joint significance test.

Then, we conduct their heteroscedasticity BP test. The null hypothesis is that there is no heteroscedasticity in the perturbation term of the four models. The test results are as follows:

Model P value E1 0.2279 0.2448 E2 0.2345 E3 0.2788 E4 Also, we can observe that all models’ p value has surpassed 0.05. Therefore, we accept the null hypothesis and conclude that there is no heteroscedasticity in the per- turbation term of the four models.

As all potential models have passed the joint significance test and the heterosce- dasticity BP test. As for the problem of multicollinearity in regression, it is clear that hyphal extension rate has certain connection with moisture tolerance, combining the

关注数学模型 prediction, not explaining, we care for the goodness of fit and its prediction ability more. Therefore, we could neglect the problem of multicollinearity. Although it may expand the error, it makes no difference for its prediction ability. Weighing pros and cons, the model with largest Adj -R2 value is selected, namely Equation 4 in (3) and 微信公众号：数学模型 obtain the equation as follows:

(3)

5.3 Model for Multi Species

Considering interactions between different species of fungi, we regard the multi groups as a whole. Therefore, as for the decomposition model of multi species, we need to figure out H and M values under interactions, and then utilize equation (5) to obtain the decomposition rate for multi species. Besides, our targets are three types of fungi, namely Sprinter, Middle-distance runner, and Long-distance runner in table 3. Here we build the following model according to experience:

(4) Where 𝐻1, 𝐻2and 𝐻3 stand for three types of fungi’s hyphal extension rate respec- 微信号：MATHmodels tively. Moisture Tolerance for multi species is obtained according to assumption 1 in the part of Assumptions and Justifications:

(5) Where 𝑎1, 𝑎2and 𝑎3 represent three types of fungi’s proportion respectively and 𝑚1, 𝑚2 and 𝑚3 stand for three types of fungi’s moisture tolerance accordingly. Therefore, combine equation (5)(6)(7), model for multi species can be expressed as following:

(6)

6 Fungal Propagation Model

6.1 Single Species Propagation without Environmental Fluctuations

As fungi continue to reproduce, their population size 𝑛 increases with time goes by, which can be expressed as:

(7)

However, due to limited natural resources and water produced and heat released in the process, hyphal extension rate 𝐻 will diminish as population size enlarges, namely 𝑛 increases. Therefore, 𝐻 is supposed to be function with 𝑛:

(8) Besides, when , . Therefore, we get:

(9)

(10)

6.2 Single Species Propagation with Environmental Fluctuations

To start with, we clarified the concrete form of fluctuations. Judging from the re- ality, we assume that moisture in environment and temperature change periodically

关注数学模型 like trigonometric functions. Therefore, we set an original trigonometric function of environmental moisture and temperature. As required, we only consider moisture and temperature and reckon 8 potential circumstances as the following Table 6 demonstrates: 微信公众号：数学模型

Moisture Temperature Original trigonometric func- Moisture changes but tions Remain temperature remains Amplitude increase Angular velocity increases Original trigonometric Temperature changes functions Remain but moisture remains Amplitude increase Angular velocity increases Temperature changes Original trigonometric functions with the same frequency and moisture changes Original trigonometric functions with different frequency 微信号：MATHmodels According to literature [10], fungi can live between 0 and 50 ℃, while the best temperature ranges from 22 to 32. Besides, they can live between -5 to 0 MPa moisture, while the best ranges from -1 to -0.2 MPa. When environmental moisture 𝑥 remains and temperature 𝑦 changes periodically, for example 𝑦= 32 + 5𝑠𝑖𝑛(0.1𝜏), we need to forward control these interval type indicators as:

(11)

(12)

Where, 𝑦′ is the positive indicator of environment temperature. Positive moisture value 𝑥′ can be obtained from the remained 𝑥 value. We introduce a relative envi- ronmental impact factor σ to quantify the influence of environment fluctuations. Population size can be expressed as:

(13)

(14) Where 𝜔′ stands for relative moisture niche width, while 𝜈′ stands for relative tem- perature niche width. 𝑘1 and 𝑘2 are proportional constants.

Besides, the situations of when temperature 𝑦 remains and environmental mois- ture 𝑥 changes periodically and when both environmental moisture 𝑥 and temper- ature 𝑦 changes periodically follow the same approach.

关注数学模型

6.3 Simulation Results

For single species propagation without environmental fluctuations, we set 𝐻1=0.8, 𝐻2=0.4, 𝐻3=0.2, 𝑁1=𝑁2=𝑁3=2000 and observe three kinds of fungi commu- nity’ situation: 微信公众号：数学模型 (a) Group scale (b) Decomposition rate 微信号：MATHmodels

From Figure 9(a), under the optimal environmental temperature, the group scale of three fungi types levels off eventually with time goes by. Besides, in this case, Sprinters seem to be winner as their growth rate is greater than the others. Long dis- tance runners are left behind. Also, their decomposition rate become a constant even- tually, which is evident from Figure 9(b).

For single species propagation with environmental fluctuations, we assume that when 𝜏= 60, moisture 𝑥 changes periodically or temperature 𝑦 changes periodi- cally:

(a) Moisture changes (b) Temperature changes

We adopt solid line to stands for the original trigonometric function, dotted line for the case of amplitude increases and the trajectory of dash-dotted line shows the angular velocity increases.

6.4 Sensitivity Analysis

In Figure 10 (a) and (b), it is remarkable that decomposition rate soars dramati- cally during the first cycle for all three lines, but the amplitude presents a trend of

关注数学模型 decline later on. Therefore, we infer that decomposition rate feels the great pinch of environmental fluctuations in the short term but this kind of influence will ebb as time goes by. In other words, its impact will diminish in the long term.

Because of the environmental fluctuations, hyphal extension rate, affected by 微信公众号：数学模型 moisture or temperature changes, starts to reduced and even becomes a negative value. The expansion rate of population scale begins to decline and even shrinks. Therefore, competition among fungi becomes less fierce. Besides, fungus individual’s decomposition abilities are no longer suppressed, obtaining a modest increase, which makes the single fungi species’ overall decomposition rate fluctuate in a small range. Further, decomposition rate rises rather than declines under fluctuations.

Comparing the solid line and the dashed line in Figure 10 (a) and (b), we can find that when the amplitude of moisture change expands, the extent of decomposition rate increase becomes larger, indicating that the decomposition rate of single species is sensitive to the magnitude of moisture change in this case. Likewise, comparing the solid line with the dotted line, when the angular velocity of moisture change increases, the trend of decomposition rate change gets advanced, suggesting that the faster mois- 微信号：MATHmodels ture changes in this model, the faster decomposition rate of single species changes. Therefore, decomposition rate is sensitive to the changing rate of moisture change. Analysis for temperature is the same.

7 Fungal Population Competition Model

7.1 Population Competition without Environmental Fluctuations

We set the maximum number of A, B and C’s population as 𝑁1, 𝑁2, 𝑁3 respec- tively. Because of the species competition for room and nutrients in the multiple fungi community, reproduction of single group will be affected by the reproduction of other groups. Moreover, growth rate of single fungi group declines as the number of indi- vidual groups increases. Therefore, we obtain:

(15)

Where, 𝜎21 indicates a relative ratio between the woody fibers’ mass consumed by unit amount of group B (compared with 𝑁2), which is originally used to feed group A and the mass consumed by unit amount of group A (compared with 𝑁1). In other words, if 𝜎21 < 1, group B is less competitive than group A when they are combatting for food. Likewise, others share the same rule. Following equation (13), we can get:

(16)

(17)

Where , , .

7.2 Population Competition with Environmental Fluctuations

As fungi group who extend hyphae faster tends to be endowed with smaller moisture niche width and temperature niche width. When it is humid and hot, their hyphal extension rate is more susceptible compared with other types. We also intro- duce a relative environmental impact factor 𝜎 to quantify the effect of environment

关注数学模型 and forward control interval type indicators 𝑥 and 𝑦. Besides, 𝜔′ stands for relative moisture niche width, while 𝜈′ stands for relative temperature niche width. In other words:

微信公众号：数学模型 (18)

(19)

Therefore, growth rate for group A can be expressed as:

(20)

Where 𝑘1 and 𝑘2 are proportional constants.

We only consider two kinds of conditions including when moisture changes but 微信号：MATHmodels temperature remains and when temperature remains but moisture changes. As for the circumstance for both of them change, it can be considered as the superposition of above two conditions, so we do not repeat it here.

7.3 Simulation Results

For Multi Species Grow Model without environmental fluctuations, we set the initial scale of Middle-distance runner and Long-distance runner as 200 per square meter, while 100 per square meter for Sprinters. We deliberately decrease the initial scale of Sprinters at the convenience of comparison. Other initial values are displayed in Table 7:

Symbol Value Symbol Value Symbol Value Symbol Value 0.8 2000 0.7 0.8 𝐻1 𝑁1 𝜎21 𝜎23 0.4 2000 0.8 0.56 𝐻2 𝑁2 𝜎12 𝜎31 0.2 2000 0.7 0.64 𝐻3 𝑁3 𝜎32 𝜎13 With the help of MATLAB, we obtain their scale trend with time goes by. From Figure 11(a), it is notable that their scales still level off in the end. At that time, Sprint- ers are at the majority while Middle distance runners are at the minority. Nevertheless, the sum of these three types fungi rockets at first and flatten out in the end. From Figure 11(b), it is crystal clear that the decomposition rate surges and reach the peak in such a while, but steadily falls to a stable value later on. We reckon that it is because Sprinters grow dramatically in the beginning but Long-distance runners are at the majority later on. Moreover, according to Figure 1C in literature [3], decomposition rate is positively related to hyphal extension rate. Long-distance runner’s proportion becomes larger later on, leading to a lower rate. Therefore, its performance shows as Figure 11(b).

Moreover, we find that multiple species community’s population scale is 1.5 times that of single species and its decomposition rate will be 1.45 times that of single species on the condition of optimal environment and same initial proportions.

关注数学模型 微信公众号：数学模型 (a) Population scale (b) Decomposition rate

7.4 Sensitivity Analysis

For Multi Species Grow Model with environmental fluctuations, when moisture 微信号：MATHmodels 𝑥 changes periodically but temperature remains:

(a) Population scale (b) Decomposition rate

In Figure 12(a), we notice that when the moisture concentration has great changes, the relative advantages and disadvantages of population scales will also change. Be- sides, the racing outcome is hard to identify as it does not reach a balance. Therefore, in this case, moisture is the main factor for population competition. In Figure 12(b), for the first cycle of three kinds of line, decomposition rate all diminish abruptly. Be- sides, its extent grows in the later several cycles, indicating that when moisture changes but temperature remains, the decomposition rate of multiple fungi species is susceptible to environmental fluctuations largely in the short term. Due to the accu- mulation effect of this fluctuations, the influence runs deeper. Therefore, the decom- position rate in this case will be increasingly tiny, continuously changing fungal abil- ity to break down ground litters. Further, compared with the phenomenon that the population scale of multiple species tends to be stable in the long term in the case, which is showed in Figure 12(a), it suggests fungus individuals in the multiple species

关注数学模型 community are more likely to reduce their breaking down ability to ensure the stabil- ity of their own population scale when encountering environmental fluctuations. At this time, the sensitivity to environmental fluctuations of multiple species community is similar to that of single species. When the amplitude of changes becomes greater, 微信公众号：数学模型 the declining extent of multiple species community When temperature changes periodically but moisture remains:

微信号：MATHmodels (a) Population scale (b) Decomposition rate

Comparing Figure 13 with Figure 12, we can find that they are similar, except that the amplitude of changes in Figure 13 is more salient. In this case, multiple species community is more sensitive to temperature fluctuations than moisture changes.

7.5 Species Competition under Different Climates

To start with, we collect the climate information of arid, semi-arid, temperate, arboreal, and tropical rain forests on website [11-15].

Tropical Climate Arid Semi-arid Temperate Arboreal rain forests Moisture -5 -3.6 -3.3 -2.8 0 Temperature 50 26 24 26 28 Note: the unit of moisture is MPa and temperature refers to summer daytime (℃) According to equation (15) (16) (17), with the help of MATLAB, we can predict different species combinations’ performance. Considering the combination of all po- tential combinations for these three species, we get the trend curve of their behaviors in five different regions. In Figure 14(a), all combinations of species are dying out, which is consistent with the common sense that fungi usually do not grow well in arid areas. However, under such trying conditions like arid climate, Long-distance runners still dominate as they survive longer. So, they have a relative advantage. In Figure 14(b), we can notice that Long-distance runners stand out no matter what kind of com- bination. Middle-distance runners dominate when grow with sprinters, but pale in comparison with Long-distance runners. Besides, sprinters have no advantages at all.

关注数学模型 微信公众号：数学模型 (a) Arid region (b) Semi-arid region

The situations in temperate region and arboreal region are quite similar with semi-arid region. The only difference between them is that sprinters can survive but 微信号：MATHmodels still at a disadvantage when competing with middle-distance runner. The reason why sprinters can still survive may be their excellent hyphal extension ability. Therefore, despite the tremendous environmental stress, they can still keep a small population scale. Due to pages’ limit, we do not repeat it here. As for tropical rain forests circum- stances:

(a) Arboreal region (b) Tropical rain forests region

From Figure 15(b), when it comes to tropical rain forests, we can see another pic- ture. Sprinters are at absolute dominance compared with the other two. Further, the conclusion summary is as following:

Tropical Climate Arid Semi-arid Temperate Arboreal rain forests Best partners none none S+M S+M all Advantage L L L L S, L Disadvantage S, M S, M S, M S, M M Note: S stands for Sprinters, M stands for Middle-distance runner and L stands for

关注数学模型 Long-distance runner. Best Partners mean the situation when the combination of mul- tiple species could keep the relationship of continuing friendly co-existence. Ad- vantage refers to the dominant species in that case, while Disadvantage refers to vul- nerable species in that case. 微信公众号：数学模型

7.6 Diversity of Fungal Communities

In order to describe how the diversity of fungal communities of a system impacts the overall efficiency of a system concerning the breakdown of ground litter and pre- dict the importance and role of biodiversity, we compare the performance of single species and multiple species when environmental moisture and temperature are both making chances. As for the situation of single species, we take middle-distance runner as example.

微信号：MATHmodels (a) Single species population scale (b) Single species decomposition rate

(c) Multiple species population scale (d) Multiple species decomposition rate

By comparing Figure 16(a) and (c), we find that on condition of the same initial population scale and optimal climate, multiple species’ population scale is larger than single species’ scale. When both of them encounter environmental fluctuations (𝜏= 60), it is remarkable that population scale of multiple species is more stable and the balance value in the end is also larger than single species. Therefore, it vividly demon- strates that biodiversity makes great contribution to ecosystem stability and propaga- tion.

关注数学模型 By comparing Figure 16(b) and (d), we find that on condition of the same initial population scale and optimal climate, multiple species’ overall decomposition rate is larger than single species’ rate. However, when both of them encounter environmen- tal fluctuations (𝜏= 60), it is notable that decomposition rate of single species is more 微信公众号：数学模型 stable and the balance value in the end is also larger than multiple species. Therefore, the diversity of fungal communities could boost the breakdown of ground litter when at appropriate climate conditions but not helpful when encountering environmental fluctuations.

Moreover, multiple species community’s population scale will be 1.18 times that of single species and decomposition rate will be 0.93 times that of single species under environmental fluctuations.

Last but not least, according to the analysis in the part of Species Competition under Different Climates, we can obtain the same conclusion. Combinations with a large number of species tend to survive more and have greater impact on the environ- ment than combinations with little number of species.

8 Model Evaluation and Possible Improvements

微信号：MATHmodels

8.1 Strengths

⚫ Before proposing our model, we pre-processed the data with the help of SPSS.

We sort available fungi samples into three categories by clustering analysis, which sets clear research target and pave way for the later work.

⚫ Population propagation model and competition model based on differential equation are scientific and reasonable.

⚫ The model has better generality and scalability. If we need to consider other factors’ impact, we could modify the differential equation to upgrade the model.

8.2 Weaknesses

⚫ Due to insufficient data, our range of research is limited to the species covered in collected data. Therefore, the model is still not comprehensive enough.

⚫ We do not consider predators, PH value, sunshine and other common factors.

Despite these weaknesses, we hope our model is helpful to the research of fungi and biology improvement.

8.3 Possible Improvements

In fact, fungal growth is affected by various factors. Quantify predators, PH value, sunshine and others and We will modify the differential equation to make it more suitable for common situations. Besides, the analysis and simulation of fungi commu- nity can be more accurate if more data can be available.

9 Conclusion

Our paper provides a detailed analysis of interactions among multiple fungi spe- cies and the biodiversity of fungal communities of a system’s impact. Before introduc- ing the model, we analyze the characteristics of different fungi types and classified them into three categories by clustering analysis. Then Fungi Decomposition Model, Fungi Propagation Model and Fungi Population Competition Model are proposed.

关注数学模型 We utilize real experimental statistics to simulate various situation including sin- gle species and multiple species, with environmental fluctuations and without envi- ronmental fluctuations, and trends both for short-term and long-term. The simulating results fit the reality and common sense very well. From the predictions about the 微信公众号：数学模型 relative advantages and disadvantages for each species and their potential combina- tions, we simulate three types of fungal behaviors in different environments including arid, semi-arid, temperate, arboreal, and tropical rain forests. Moreover, we put for- ward the best combination and the most advantageous species of different species un- der different environment. Further, as for the analysis of significance of the biodiver- sity in ecosystem, we conclude that the diversity of fungal communities could accel- erate the breakdown of ground litter when at appropriate climate conditions but not helpful when encountering environmental fluctuations.

微信号：MATHmodels

关注数学模型 Advanced Biology

10 Article

P a g e 2 2 o f 2 5

微信公众号：数学模型 Unit 1 Cleaner of the Earth: Fungi

◼ Study Targets:

1. Understand fungi’s roles in ecosystems. 2. Understand fungi’s reproductive method. 3. Master the characteristics of fungi. 4. Master the growth rhythm of individual fungi and multi species’ effect on commu- nity.

1.1 What’s Fungi?

1.2 Fungi’s Role in Ecosystem

For a long-term sustainable ecosystem, there must be producers, consumers, and decomposers. Producers are creatures including green plants and autotrophic microorganisms (for example, thiobacil- lus, nitrifying bacteria, cyanobacteria and so on), providing materials and energies for various organ- isms in the ecosystem. Animals and parasitic micro- 微信号：MATHmodels A fungus (plural: fungi) is member of the group of eukaryotic organisms including microorganisms like yeasts, molds and mushrooms. These organisms are separate from the other eukaryotic creatures like plants and animals due to their unique characteris- tics. Despite discrepancy among various species, some shared features as following: ✓ Fungi have true cell nuclei; ✓ Without chlorophyll, fungi cannot conduct pho- tosynthesis and must live on absorbing nutri- ents; ✓ Fungi grow by filamentous hyphae; ✓ Asexual reproduction and sexual reproduction are both available for them; ✓ Spores are produced to start their new genera- tion; ✓ Fungal cell wall mainly consists of chitin or cel- lulose or both of them.

organisms (such as viruses) are consumers, whose role is promoting the circulation and flow of materi- als in the ecosystem. Saprophytic microorganisms like fungi are the decomposer, cleaning the body of dead animals and plants and supplying carbon di- oxide for green plants to reuse.

As we all known, carbon element is the funda- mental element of all creatures on the earth. It trans- fers among biosphere, lithosphere, hydrosphere and atmosphere by virtue of various substance and thus forms carbon cycle, which consists of four steps in- cluding photosynthesis, decomposition, respiration and combustion. Fungi play a crucial role in the de- composition part as composers, transferring organic substances into inorganic substances through their respiration.

关注数学模型

Advanced Biology Advanced Biology

P a g e 2 3 o f 2 5

微信公众号：数学模型

1.3 Literature Review

Fungi’s prominent and salient function in ter- restrial ecosystems and biodiversity is widely acknowledged. Besides, a large number of experi- ments concerning fungi are carried out. Especially, the mainstream analysis method is based on its traits [2-6].

McGill et al. (2006) confirm that the trait-based method within the community requires considera- tion of the interaction milieu (biotic interactions) [2]. Nicky Lustenhouwer, Daniel S. Maynard, and Mark A. Bradford (2020) explored a large number of dif- Where, 𝜎21 indicates a relative ratio between the woody fibers’ mass consumed by unit amount of group B (compared with 𝑁2 ), which is originally used to feed group A and the mass consumed by unit amount of group A (compared with 𝑁1). In other words, if 𝜎21 < 1, group B is less competitive than group A when they are combatting for food. Like- wise, others share the same rule. Besides, , , .

1.4 Significance of Biodiversity

Multiple species community’s reaction towards 微信号：MATHmodels ferent fungal traits and their effects on the decom- position of wood. They also find that fungi with a slow growth rate prone to be better able to survive and grow under environmental changes concerning moisture and temperature, while faster-growing groups tend to be less robust to the same changes [3]. Therefore, to some extent, the hyphal extension rate can represent fungi growth rate. Further, ac- cording to A. van der Wal’s research, wood mois- ture content and species richness of the fungal com- munity are the best predictors for mass loss in the older stumps [7]. Besides, from Schimel, J.’s study, maintaining water potential is essential to keep tur- gor pressure, nutrients via substrate diffusion [8].

1.4 Fungal Population Competition Model

Set the maximum number of A, B and C’s pop- ulation as 𝑁1, 𝑁2, 𝑁3 respectively. Because of the competition for room and nutrients in the multiple fungi community, reproduction of single group will be affected by other groups. Moreover, growth rate of single fungi group will decline as the number of individual groups increases. Therefore, we obtain the fungal population competition model:

environmental fluctuations can be demonstrated as following:

(a) Moisture (b) Temperature

Comparing Figure 3 (a) with Figure 3 (b), we can find that they are similar, except that the amplitude of changes in Figure 3 (b) is more salient. In this case, multiple species community is more sensitive to tem- perature fluctuations than moisture changes.

We can also predict different species combina- tions’ performance in different regions. Take the ex- ample for arid region and tropical rainforests. We can also find that multiple species communities tend to survive more.

(a) Arid region (b) Tropical rainforests

关注数学模型

Advanced Biology

Appendices

Appendix 1

Introduce: Solving differential equations 微信公众号：数学模型 clear, clc global w v w = zeros(3, 1); w(1) = 1.488; w(2) = 1.75; w(3) = 3.19; v = zeros(3, 1); v(1) = 17.82; v(2) = 15.32; v(3) = 19.9; w = w./sum(w); v = v./sum(v); w = w'; v = v'; wa = -0.2; T = 26; [t, x] = ode45(@(t,x)func(t,x,wa,T), [0 150], [100 200 200]);

Appendix 2

Introduce: Functions used to solve differential equations function dx = func(t, x, wa, T) global w v dx = zeros(3, 1); 微信号：MATHmodels H1 = 0.8; H2 = 0.4; H3 = 0.2; N1 = 2000; N2 = 2000; N3 = 2000; sigma21 = 0.7; sigma32 = 0.7; sigma31 = 0.56; sigma12 = 0.8; sigma23 = 0.8; sigma13 = 0.64; k1 = 2; k2 =2.2; u = water(wa); y = temp(T); sigma = k1*u*(1-w)+k2*y*(1-v); dx(1) = H1*x(1)*(1 - x(1)/N1 - sigma21*x(2)/N2 - sigma31*x(3)/N3 - sigma(1)); dx(2) = H2*x(2)*(1 - x(2)/N2 - sigma12*x(1)/N1 - sigma32*x(3)/N3 - sigma(2)); dx(3) = H3*x(3)*(1 - x(3)/N3 - sigma13*x(1)/N1 - sigma23*x(2)/N2 - sigma(3)); end

Appendix 3

Introduce: Forward control interval index of temperature function y = temp(x) a = 22; b = 32; temp_min = 0; temp_max = 50; M = max(a-temp_min, temp_max-b); if x<a y = (a-x)/M; elseif x>b y = (x-b)/M; else y = 0; end end

关注数学模型
