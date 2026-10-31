T1 F1 T2 F2 T3 F3 Problem Chosen

T4 F4

MCM/ICM

Summary Sheet

Summary

After performing data analysis and modeling, we finally determine a set of develop- ment goals for the new four-state energy compact.

First, we preprocess the data provided, which includes default value processing, ab- normal value process and data classification. For the sake of analysis, we divide various energy into two broad categories. One is cleaner renewable energy (CRE), the other is traditional fossil energy (TFE). After that, we select 11 important variables from the given data to create the energy profile for each of the four states. We call the 11 variables the basic variables Next, we apply the decoupling theory to characterize the dynamic relationship be- tween economic development and energy utilization, which can reflect the evolutionof energy profile. We find that the four states differ in production and usage of various energy significantly. Todetermine the underlying factors that lead to the differences, we construct the simultaneous equations model. Combining natural environment informa- tion further, we find out the factors and know the respective strengths of the fourstates in CRE.

Then, we establish a multi-dimensional evaluation system to identify the state that has the“best”energy profile on the whole. We introduce the index, comprehensive utilization performance (CUP) to measure the energy profile. The CUP is composed of three parts, energy performance, economic performance and environment performance. And each of the three parts includes three indexes respectively, all of which are synthe- sized by the basic variables. We use the PCA method to integrate the nine indexes into an overall index, namely the CUP. Ranking CUP, we find that California is the“best”.

Finally, we construct BP neural network to predict the energy profile. Analogous to Cobb-Douglas Production Function in economics, we define the CUP in a new way for predicting. Through setting various development scenarios, we get the predictions successfully. After that, we regard the four states as a whole to determine renewable energy usage targets for 2025 and 2050. In this process, we use the BP neutral network and previous models again. Wecollect real data from 2010 to 2015 to calculate the values of CUP. Compare them to the predicted value, we test our predicting system. The result shows that our predicting system works well.

8 Conclusions

21

9 Strengths and Weaknesses

21 Strengths..................................................................................................................... 21 9.1 Weaknesses................................................................................................................. 22 9.2

Appendices

23

Appendix A Profiles of Arizona

23

Appendix B Profile of New Mexico

25

Appendix C Profiles of Texas

25

MEMO

From: Team 73767, MCM 2018 To: The group of Governors Date: February 13, 2018 Subject: Goals for the interstate energy compact

Dear governors, we are honored to inform you our achievement after performing data analysis and modeling.

First, we introduce the energy profiles of your states in 2009. We use comprehensive utilization performance (CUP) to reflect the energy profile on the whole. Ranking the CUP of your four states, California appears to be the best. In terms of the usage of cleaner renewable energy, California, Arizona, Texas and New Mexico has the largest consumption successively in the water power, nuclear power, wind power and solar power. It is decided by the natural environment of your four states, such as geography and climate.

Then, we provide you the goals for the interstate energy compact. Through predict- ing, your four states’ average CUP will increase to 16.98 by 2025 and to 26.05 by 2050,if your four states can cooperate adequately. Based on the predictions, we set the develop- ment goals as follows:

• Building a community of energy utilization and economic development, so as to realize manual benefit and win-win result.

• Promoting the production and usage of new energy sources and reducing the de- pendence on traditional fossil fuels.

• Increasing the whole economy’s comprehensive utilization performance to 16.98 by 2025 and to 26.05 by 2050, and achieving the harmony of economy, energy and environment ultimately.

According to the goals above and the characteristics of each of your four states, we offer you the following suggestions to meet the goals.

• Building an energy investment bank to integrate money for developing the clear renewable energy.

• Enhancing residuals’ environmental protection consciousness.

• Adjusting the industrial structure properly.

We sincerely hope that you can achieve the goals above!

Please contact us if you have any problems.

1 Introduction

1.1 Problem Statement

Energy is the main material base and driving force for human’s daily production and life. The proper utilization of all kinds of energy are closely link to the sustainability of economic development. The excessive consumption of traditional fossil fuels not only restricts the economic development, but also causes a series of environmental problems, such as global warming. Therefore, in America, many states have been trying to im- prove the production and usage of energy. A successful practice is that some states with different strengths and weaknesses unite to form an interstate compact, for promoting the usage of cleaner, renewable energy sources, through cooperation and adherence to specific policies.

In the southwest of the U.S., there are four states – California (CA), Arizona (AZ), New Mexico (NM), and Texas (TX) – that hope to form a realistic new energy compact as well. Asked by the four governors of these sates, we determine a set of development goals for the energy compact.

1.2 Our Goals

Based on our understanding of the problem, we set the following goals:

• Use the given data to found an energy profile for each state.

• Develop a model system to show the dynamic relationships between various en- ergy consumption and economic development of each of the four states, and ex- plore the underlying factors that lead to these relationships.

• Define the“best”profile for use of cleaner, renewable energy, then set up a system of evaluation to determine the state that has the“best”profile in2009.

• According to the analysis above, develop a model and set different scenarios to predict the energy profile of each state for 2025 and 2050.

• Based on the established models, decide the usage targets of cleaner and renewable energy for 2025 and 2050. Then provide three actions for the four states to achieve the goals.

1.3 Our Thinking

This is a typical big data problem, so we solve it from the point of view of statistical analysis. Here is our thinking.

First, we preprocess the data provided, which includes default value processing, ab- normal value processing and data synthesis and classification. Based on our definitions, we select some major energy sources for analysis and divide them into two categories. One is called cleaner renewable energy (CRE), the other is called traditional fossil en- ergy (TFE). The specific definitions will be given later.

Second, we select some important data from the dataset provided to construct the energy profile. Through statistical charts, we visualize them. In this way, we found an energy profile for each state. Comparing the energy files of the four states, we find dif- ferences in their utilization of the two kinds of energy sources. To further clarify the dif- ferences, we learn from the decoupling theory and use coefficients of elasticity to show the dynamic relationships between various energy consumption and economic devel- opment of each state. Then we use the simultaneous equations model to respectively analyze the four states’ economy systems, in which way, we find out the reasons why the differences exist.

Third, weintroduce the conceptof thecomprehensive utilization performance (CUP) to evaluate which of the four states appeared to have the“best”profile. Since different states have their own characteristics, therefore, we establish a multi-dimensional evalua- tion system to measure the comprehensive utilization performance in case of bias. Then we use principle component analysis (PCA) to integrate each evaluation index into an overall index, namely the comprehensive utilization performance.

Finally, we build the BP neural network to predict the energy profile of each state. By setting various change trajectory of independent variables, we get the predictions successfully. After that, we regard the four states as a whole to determine renewable energy usage targets for 2025 and 2050.

2 Assumptions and Notations

2.1 Assumptions

Due to lack of necessary data and limitation of our knowledge, we make the follow- ing assumptions to help us perform modeling. These assumptions are the premise for our subsequent analysis.

• For the four states, all kinds of energy they produce are consumed by themselves each year. Thus we can replace energy output with energy consumption in calcu- lation.

• The policy of each state will not change in the future. This assumption may be not realistic, but it is essential for us when predicting the energy profile in 2025 and 2050.

• The natural environment of the each states will not change. So we can see it as constant. This assumption simplify our analysis, and it is reasonable, since the natural environment is usually stable.

• Once forming an interstate energy compact, the four states can develop and utilize resources together. Thus they can realize manual benefit and win-win result.

2.2 Notations

Here are the notations and their meanings in our paper:

Notation

Meaning Epd Electricity production Tpd Total energy production Rce Renewable energy expenditure ttdp GDP Cpd Renewable energy production Pri Price energy Ind Secondary industry consumption Pop Population Wcs Wood consumption Tcs TFE consumption Enc Total energy consumption Cep Carbon emission per capita K Energy expenditures as share of GDP

3 Data Preprocessing

For data-analysis problem, there are usually some incomplete and abnormal datain the large amount of raw data, which may seriously affect the efficiency of modeling and the accuracy of conclusions. So it is quite important to preprocess the data.

3.1 Default Value Processing

We use different methods to process variables with various degrees of data loss. (1) For variables with large amount of data missing, we just delete it. Because small data cannot provide enough and valuable information for our modeling. (2) For variables with a small amount of data missing, we use interpolation method to compensate the data. More specifically, we first use existing data points to establish an appropriate in- terpolation function, and then replace the missing value with the function value f(xi) at the corresponding point xi.

3.2 Abnormal Value Processing

If a value in a set of data is more than twice the standard deviation of the average, we call it the abnormal value. Statistically we can use a box-plot to identify the abnormal values. For the abnormal value, we fix it with the average value of its two adjacent observations.

3.3 Data Synthesis and Classification

There are 605 variables in the dataset provided. Not all of them are used in our model. Thus, we sort the data we need into a new dataset. Besides, we divide the energy sources into two categories for the further analysis, One is called cleaner renewable en- ergy, which includes the hydroenergy, the wind energy, the geothermal energy, the solar energy and the ethanol; the other is called traditional fossil energy, which includes the coal, the petroleum, the natural gas and other fuels.

Definition:

• Cleaner renewable energy is the energy that produces little pollution and can be used directly in the production and life.

• Traditional fossil energy is non−renewable energy and will cause air pollution after burning.

In our model, some synthesized variables are used, for example, the average price of cleaner renewable energy. It can be calculated according to formula (1). Other synthe- sized variables will be explained later.

Σ

4 Energy Profile

After data preprocessing, we choose 11 important variables to create the energy pro- file. we call them the basic variables

Notation

Abbreviation in the original data set GDP GDPRX Total population TPOPP TFE consumption FFTCB Total consumption TETCB Wood consumption WWTCB Electricity production ESTCB Total energy production TEPRB Price of renewable energy AVACD Renewable energy production REPRB Renewable energy expenditure RFEIV Secondary industry consumption TEICB

Descriptive statistics is usually the first step in statistical analysis, which can shows the important features of the data visually through graphs and tables. In view of this, we adopt the descriptive statistics method to show the energy profile of each state. Here is the energy profile of California, those of other states are attached to the appendix.

Pic1 Trend graph of TFE and its price Pic2 Trend graph of CRE and itsprice Pic3 Trend graph of totalconsumption(TC) and its price Pic4 Trend graph of the ratio of TFE to TC and CRE to TC

F Fuel enthanol C Coal HY Hydroelectricity PE Petroleum products GE Geothermal energy NG Natural gas WE Wind energy OT Other PH&SO Photovoltaic and so- lar thermal energy (Only the unit of "F"is Thausand Barrels)

Variable Quantitative Change Rate of Change Energy total production 510310.93(Billion Btu) 156.56% Renewable energy total production 28262.33(Billion Btu) 383.32% Fossil fuels, total production 482048.60(Billion Btu) 151.32% Electricity production 16995.11(Billion Btu) 2279.84% Wood consumption 4244.64(Billion Btu) 64.04% Secondary industry consumption 414753.42(Billion Btu) 199.64% Renewable energy total end-use expenditures 750.17(Million dollars) 873.31% GDP 59090(Million dollars) 593.15% By comparing the energy profiles of the four states, we preliminarily reached the following conclusions:

Overall, the four states differ in their utilization and consumption of the two types • of energy (CRE&TFE).

Each of the four states has a growing share of CRE consumption, while the share • of TFE is still high.

California ranks the first in terms of the amount of CRE consumption; Arizona • ranks the first in terms of the share of CRE consumption. However, New Mexico lags behind in the usage and consumption of CRE.

5 Model Construction

5.1 Decoupling Analysis

Since having had a general idea of the energy profiles of the four states, we now in- tend to calculate the coefficients of elasticity to deeply analyze the dependency between economic development and the various energy consumption of each state. According to the decoupling theory, the higher the absolute value of the elasticity, the stronger the [1]The formula of coefficient of elasticity is asfollow. dependency.

The calculation results are shown in figure 4. From the figure, we can intuitively know that generally the dependency between economic development and CRE con- sumption is on the rise for each state, but the intensity of the dependency differs among the four states.

5.2 The Simultaneous Equations Model

To explore the underlying factors that leads to the differences of energy files among the four states, we develop a simultaneous equations model, as shown below. Different syste m from single equation regression, simultaneous more equations model can explain the complex economic comp rehensively and accurately. We introduce three (3)

equations into the model, since there are interactions between each two of the three elements, eco- nomic development, energy consumption, and [2] environmental pollution.

where X is a set of controlling variables on the natural environment Lack of variable data on the natural environment, we neglect the set of controlling variables X to solve the model. The regression results of equation ln(Enc) are shown in the following table. The regression coefficients reflect the influence of explanatory variables on dependent variables, from which we can determine the impact of different factors on the energy variable.

TFE CRE Equation 1 AZ CA NM TX AZ CA NM TX

ln(ttdp) 0.2189*** 0.5122** 0.4896** 1.2368*** 0.1904*** 0.4915** 0.2167* 0.4532**

ln(Cep) 0.0012 0.0104** 0.1326** 0.1725** 0.0031 0.0113* 0.0682** 0.1651***

ln(K) 0.2169** 0.3481** 0.2018* 0.3018** 0.2267** 0.4162** 0.2481*** 0.3156*

ln(Pop) 0.0104 0.0341 0.0361* -0.2214 0.0133 0.0265 0.0421* -0.2153

ln(Pri) 0.1152* 0.1421 0.1102** 0.2451 0.1842* 0.1821* 0.2012** 0.2201

ln(Ind) 0.1421* 0.4142*** 0.2269* 0.2684** 0.1723* 0.3841*** 0.2362* 0.2758*

Constant 17.6421* 19.2364* 13.2631* 50.3641* 16.6372* 37.6298* 13.2156* 61.2571*

*，**，*** respectively represent the confidence of 10%,5%,1% From the Table 5, we can see that population has no significant influence on the en- ergy consumption. While the the economic development and the share of secondary industy have significant influence on the energy consumption.

To determine the influence of geography and climate, we collect information about the natural environment of the four states, which is shown in Figure 5. It shows the resource distribution of solar power, wind power and hydroelectric power.

From Figure 5, we know that the four states differ in the potential of CRE production. The differences are caused by the various natural environment of the four states, such as climate and geography.

5.3 The Multi-dimensional Evaluation System

In this part, we will determine which of the four states has the“best”energy profile in 2009. Through the above analysis, we know that the four states differ in strengths and weaknesses congenitally. Thus, for avoiding bias, we establish a multi-dimensional evaluation system to measure their energy profile.

5.3.1 Construction of Indexes

The core indexes of our evaluation system is called comprehensive utilization perfor- mance (CUP), which reflects the development and utilization level of CRE. The CUP is composed of three parts, energy performance, economic performance and environment performance. And each of the three parts includes three indexes as well. These indexes and their formulas are detailed in the Table 6.

Name of Index Meaning Formula Reflects the status of the CRE De = Cpd Development development and utilization in Epd Efficiency (De) the electricity industry.

Reflects the sustainability of Dp = (Cpdt −Cpdt−1) Development Energy CRE development and Cpdt−1 Potential (Dp) performance utilization. (Ep) Reflects the contribution of Development Dpa = Cpd CRE development and Achievements Tpd utilization to the state energy (Dpa) structure.

Reflect the state’s support for Es = Rce Economic renewable energy at the ttdp support (Es) investment level Reflect the efficiency and Roi = Cpd Economic Rate of return on profitability of investment on proformance investment (Roi) Rce renewable energy (Epf ) Equilibrium of 1 Reflect supply’s satisfaction Esd = supply and with demand Pc demand (Esd) Secondary Reflects the dependence on Sip = Scs industry polluting industries in each T ocs proportion (Sip) state.

Reflectis the situation of the Cep = Tcs Carbon emission Environment greenhouse gas emission per Tpo per capita (Cep) performance capita. (Enp) Consumption of Reflects the situation of natural Cnr = Wcs natural resources resources consumption per Tpo per capita (Csr) capita.

5.3.2 Principle Component Analysis

We use the PCA method to integrate each evaluation index into an overall index, namely the comprehensive utilization performance. Then through the comparison of the CUP values of the four states, we determine the“best”state.

First, we use the given data and the formulas in Table 6 to calculate the evaluation indexes. And then, we use the equation below to standardize the values of these indexes.

The results of PCA is showed in table 7. from the table, we can see that California has the“best”energy profile in 2009.

Rank State PCA Score 1 California 0.9433 2 Texas 0.5561 3 Arizona 0.2466 4 New Mexico -1.7459

5.4 Energy Profile Predicting System

5.4.1 Determining the Predictors

In part 5.3, we measured the energy file in three dimensions, energy performance, economic performance and environment performance. For the following analysis, we selectan index fromeach of them to calculate the comprehensive utilization performance (CUP) in a different way.

The indexes we select are Dpa, Roi and Cep. Analogous to Cobb-Douglas Production Function in economics, we derive the following formula.

CUP = A (Dpa)α (Roi)β Cepγ (9) · · · where :

A is unit correction factor;

α,β,γ are weight coefficients of variables;

α + β + γ = 1.

In the previous analysis, we pointed out that, there is an interaction between each [3] Therefore, we choose tow of the three elements, economy, energy and environment. ttDP per capital (ttdp) , Secondary industry proportion (Sip) and carbon emission per capita (Cep) as the independent variables in prediction. Then we can drive the following equation.

(10) CUP = θ0 + θ1ttdp + θ2Sip + θ3Cep + ε

5.4.2 Constructing BP Neural Network

Since we have to predict the energy profiles of the four states respectively, it is a heavy task. Thus, we utilize the intelligent algorithm (BP neural network) with high prediction efficiency to finish this work. It has been proved theoretically that BP neural network can approach any nonlinear function with higher precision. The flow chart below shows the principle of BP neural network.

There are two steps in the process of constructing BP neural network. First, we should set the network parameter k that represents the numbers of neurons. Here we let k = 9. Second, we use existing data of input and output to train the network. We now

drive the core formulas of the BP Network.

5.4.3 Predicting the TargetValues

Topredict the dependent variable, we have to know the independent variablesfirst. Unfortunately, we lack the values of ttdp, Sip and Cep for 2025 and 2050. So we can only predict the dependent variable by setting the change trajectory of the three independent [4] variables in advance. Weset two scenarios in total.

Scenario one: Linear trend • As is shown in figure 9, if the change of the three independent variables follows the linear trend. We can use the formula 15 to characterize their trajectory.

(20) xt = xt−1 + a

Scenario two: Smooth fluctuation • As is shown in figure 10, if the change of the three independent variables follow the smooth fluctuation. Wecan use autoregressive moving average model, ARMA(p,q) [5] to characterize their trajectory.

(21) xt = φ0 + φ1xt−1 + φ2xt−2 + φpxt−p + εt −θ1εt−1 + θ2εt−2 −θqεt−q + µ Once determining the change trajectory of independent variables, we can estimate their values. Entering them to the BP networks, we get the predicted values of the CUP of each states. The results are shown in table 9.

Scenario 1 Scenario 2 Year DPA ROI CEC CUP DPA ROI CEC CUP 2025 0.06 25.16 170.97 23.92 0.05 22.15 190.26 23.49 AZ 2050 0.07 50.45 100.45 40.19 0.06 50.15 120.15 35.22 2025 0.08 30.04 138.63 28.39 0.10 29.36 145.26 26.14 CA 2050 0.09 57.87 89.14 45.15 0.12 55.86 108.15 39.15 2025 0.07 50.14 350.45 8.20 0.07 41.26 351.22 7.89 NM 2050 0.08 59.85 282.43 15.16 0.09 57.12 301.86 14.12 2025 0.05 20.60 348.15 7.84 0.05 19.26 369.15 6.95 TX 2050 0.08 48.29 321.53 14.50 0.08 44.12 348.85 12.19

6 Testing Our Model

6.1 Predicting Reliability Test

To test the predicting reliability of the BP network, we collect relevant data of each state from 2010 to 2015, and use them to predict the CUP. Then we use formula 15 again to compute the average error between the predicted values and the actual ones. Here are the results.

The predicting error State California Arizona New Mexico Texas Error 5.89% 6.24% 7.98% 10.07%

6.2 Sensitivity Analysis

In the process of constructing BP network, we let the network parameter k = 9. How does the change of kinfluence the predicting results? Weanalyze the average deviation of CUP caused by changing k slightly.

State k-2 k-1 k+1 k+2 AZ 11.08% 4.43% 3.54% 8.51% CA 8.19% 3.15% 4.66% 10.80% NM 9.78% 5.39% 4.66% 12.28% TX 6.66% 2.19% 2.28% 12.33% Mean 8.93% 3.79% 3.79% 10.98%

From table 11, we can find that the influence of k is not big, which we can bear.

7 Determining Goals for the Energy Compact

7.1 Idea one: Don’t cooperate

If the four states don’t cooperate, which means they develop independently, they can only utilize their own resources to enhance the level of renewable energy usage. In this condition, we can just use the predicted values in part 5.4 as their respective targets.

For the two scenarios in part 5.4, we think that scenario two is more reasonable and realistic. Because the evolution of the macro-economy is usually stable, especially for [6] So we just take scenario two into consider- advanced economies like the United States. ation.

In scenario two, the average comprehensive utilization performance can increase to 16.12 and 25.17 successively in 2025 and 2050.

7.2 Idea two: Cooperate

Given that the four-state energy compact is an interstate compact, it is necessary for the tour states to cooperate. We presume that they can develop and utilize resources together. In this case, we regard the four states as a whole economy. Then we use pre- vious method and models to predict the whole economy’s comprehensive utilization performance for 2025 and 2050.

Year 2025 2050 The whole 16.98 26.05 economy’s CUP

The results shows that the whole economy’s comprehensive utilization performance can increase to 16.98 and 26.05 successively in 2025 and 2050, and each of them is higher than that in idea one. Maybe it is because cooperation enables the four states to give full play to their own advantages and promote the development and utilization of cleaner [7] renewable energy.

7.3 Goals and Actions

Based on the results in idea two and the previous analysis, we set the following goals for the four-state energy compact.

Building a community of energy utilization and economic development, so as to • realize manual benefit and win-win result.

Promoting the production and usage of new energy sources and reducing then • dependence on traditional fossil fuels.

Increasing the whole economy’s comprehensive utilization performance to 16.98 • by 2025 and to 26.05 by 2050, and achieving the harmony of economy, energy and environment ultimately.

According to the goals above and the characteristics of each state, we propose the actions and measures for the four states.

Focus on developing their own advantageous energy resource and share their en- • ergy and achievements with others.

Make more investment in scientific research to make better use of renewable en- • ergy to improve the low utilization efficiency of new energy sources.

Introduce a proper subsidy policy to award the enterprises who develop new en- • ergy source.

Make certain quantitative index and do statistic periodically to make sure the di- • rection of energy development is going well.

8 Conclusions

We are asked by the governors of the four states to set some goals for their interstate energy compact. After performing data analysis and modeling, we have finished the task successfully. First, Using decoupling theory and simultaneous equations model, we characterize the evolution of energy profile of each state from 1960 – 2009, and find out the influential factors. We have known that it is the differences of economic level, indus- trial structure and natural environment that lead to the distinct energy profiles of each state. In terms the production and usage of cleaner renewable energy, each of the four states has a growing share of CRE consumption, while the share of TFE consumptionis still high.

Second, we construct a multi-dimensional Evaluation System and introduce the core concept in this paper, named comprehensive utilization performance (CUP), which re- flects the development and utilization level of CRE. Through the PCA method, we de- termine that California has the“best”energy profile.

Finally, based on the previous analysis, we build BP neural network for predicting the energy profile of each state. By setting various change trajectory of independent variables, we get the target values successfully. After that, we regard the four states as a whole to determine renewable energy usage targets for 2025 and 2050. In this process, we use BP neutral network again.

9 Strengths and Weaknesses

9.1 Strengths

Data preprocessing.When faced with big data problem, the data processing is very • important. Through this step, we greatly improve the quality of the data. Thus, it is more efficient and convenient for us to solve theproblem.

Accuracy and stability.We use BP neutral network to make predictions. It is a pow- • erful algorithm with great nonlinear approximation ability. The error test shows that our predicting results are more accurate. Besides, when changing the network parameter k, its influence is not large. So the BP network is morestable.

Good expansibility and flexibility. There are three parameters α, β and γ in our • CUP equation, which can be used to reflect the importance of corresponding indi- cators. In different situations, we can adjust them flexibly.

9.2 Weaknesses

Subjectivity.The calculation of some synthesized variables is subjective. It can • cause extra error of our models.

Lack necessary data. Lack of data on energy production, we can only use data on • energy consumption to replace them.

Simplifying assumption.For convenience of modeling, we neglect the elements • about import and export, which play import roles in economy.

Appendices

Appendix A

Profiles of Arizona Pic1 Trend graph of TFE and its price Pic2 Trend graph of CRE and itsprice Pic3 Trend graph of totalconsumption(TC) and its price Pic4 Trend graph of the ratio of TFE to TC and CRE to TC

F Fuel enthanol C Coal HY Hydroelectricity PE Petroleum products GE Geothermal energy NG Natural gas WE Wind energy OT Other PH&SO Photovoltaic and so- lar thermal energy (Only the unit of "F"is Thausand Barrels)

Data from 1960 to 2009 Variable Quantitative Change Rate of Change Energy total production 1116104.735(Billion Btu) 374.35% Renewable energy total production 67311.832(Billion Btu) 186.04% Fossil fuelS, total production 1048792.903(Billion Btu) 400.36% Electricity production 672434.71972(Billion Btu) 2090.35% Wood consumption 6547.67591(Billion Btu) 171.44% Secondary industry consumption 1127324.01293(Billion Btu) 816.29% Renewable energy total end-use expenditures 4885.009(Million dollars) 4728.95% GDP 201016(Million dollars) 6.736912662

Appendix B

Profile of New Mexico

Appendix C

Profiles of Texas Pic1 Trend graph of TFE and its price Pic2 Trend graph of CRE and itsprice Pic3 Trend graph of totalconsumption(TC) and its price Pic4 Trend graph of the ratio of TFE to TC and CRE to TC

F Fuel enthanol C Coal HY Hydroelectricity PE Petroleum products GE Geothermal energy NG Natural gas WE Wind energy OT Other PH&SO Photovoltaic and so- lar thermal energy (Only the unit of "F"is Thausand Barrels)

Data from 1960 to 2009 Variables Quantitative Change Rate of Change Energy total production 510310.930(Billion Btu) 156.56% Renewable energy total production 28262.327(Billion Btu) 383.32% Fossil fuelS, total production 482048.602(Billion Btu) 151.32% Electricity production 16995.11376(Billion Btu) 2279.84% Wood consumption 4244.64258(Billion Btu) 64.04% Secondary industry consumption 414753.41587(Billion Btu) 199.64% Renewable energy total end-use expenditures 750.173(Million dollars) 873.31% GDP 59090(Million dollars) 593.15%

Pic1 Trend graph of TFE and its price Pic2 Trend graph of CRE and itsprice Pic3 Trend graph of totalconsumption(TC) and its price Pic4 Trend graph of the ratio of TFE to TC and CRE to TC

F Fuel enthanol C Coal HY Hydroelectricity PE Petroleum products GE Geothermal energy NG Natural gas WE Wind energy OT Other PH&SO Photovoltaic and so- lar thermal energy (Only the unit of "F"is Thausand Barrels)

Variable Quantitative Change Rate of Change Energy total production 6319816.106(Billion Btu) 142.26% Renewable energy total production 306479.838(Billion Btu) 611.07% Fossil fuelS, total production 6013336.268(Billion Btu) 136.90% Electricity production 1061765.94759(Billion Btu) 8953.51% Wood consumption 23236.12241(Billion Btu) 60.67% Secondary industry consumption 5556015.3619(Billion Btu) 158.61% Renewable energy total end-use expenditures 24323.858(Million dollars) 5688.46% GDP 876004(Million dollars) 460.01%
