# P-C-2018-73767-a72d3a8a

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | front_matter | pages [1] -->
Team Control Number

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000004 | front_matter | pages [1] -->
73767

<!-- b000005 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen

<!-- b000006 | front_matter | pages [1] -->
C

<!-- b000007 | prose | pages [1] -->
T4 F4

<!-- b000008 | front_matter | pages [1] -->
2018

<!-- b000009 | prose | pages [1] -->
MCM/ICM

<!-- b000010 | heading | pages [1] -->
Summary Sheet

<!-- b000011 | title | pages [1] -->
A Setting System of Interstate Energy Cooperation

<!-- b000012 | title | pages [1] -->
Goals Based on Data Insight

<!-- b000013 | heading | pages [1] -->
Summary

<!-- b000014 | prose | pages [1] -->
After performing data analysis and modeling, we finally determine a set of develop- ment goals for the new four-state energy compact.

<!-- b000015 | prose | pages [1] -->
First, we preprocess the data provided, which includes default value processing, ab- normal value process and data classification. For the sake of analysis, we divide various energy into two broad categories. One is cleaner renewable energy (CRE), the other is traditional fossil energy (TFE). After that, we select 11 important variables from the given data to create the energy profile for each of the four states. We call the 11 variables the basic variables Next, we apply the decoupling theory to characterize the dynamic relationship be- tween economic development and energy utilization, which can reflect the evolutionof energy profile. We find that the four states differ in production and usage of various energy significantly. Todetermine the underlying factors that lead to the differences, we construct the simultaneous equations model. Combining natural environment informa- tion further, we find out the factors and know the respective strengths of the fourstates in CRE.

<!-- b000016 | prose | pages [1] -->
Then, we establish a multi-dimensional evaluation system to identify the state that has the“best”energy profile on the whole. We introduce the index, comprehensive utilization performance (CUP) to measure the energy profile. The CUP is composed of three parts, energy performance, economic performance and environment performance. And each of the three parts includes three indexes respectively, all of which are synthe- sized by the basic variables. We use the PCA method to integrate the nine indexes into an overall index, namely the CUP. Ranking CUP, we find that California is the“best”.

<!-- b000017 | prose | pages [1] -->
Finally, we construct BP neural network to predict the energy profile. Analogous to Cobb-Douglas Production Function in economics, we define the CUP in a new way for predicting. Through setting various development scenarios, we get the predictions successfully. After that, we regard the four states as a whole to determine renewable energy usage targets for 2025 and 2050. In this process, we use the BP neutral network and previous models again. Wecollect real data from 2010 to 2015 to calculate the values of CUP. Compare them to the predicted value, we test our predicting system. The result shows that our predicting system works well.

<!-- b000018 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000019 | furniture | pages [2] -->
Team # 73767

<!-- b000020 | furniture | pages [2] -->
Page 1 of 28

<!-- b000021 | heading | pages [2] -->
Contents

<!-- b000022 | contents | pages [2] -->
MEMO

<!-- b000023 | contents | pages [2] -->
3

<!-- b000024 | contents | pages [2] -->
1 Introduction

<!-- b000025 | contents | pages [2] -->
4

<!-- b000026 | contents | pages [2] -->
Problem Statement...................................................................................................... 4

<!-- b000027 | contents | pages [2] -->
1.1

<!-- b000028 | contents | pages [2] -->
Our Goals......................................................................................................................4

<!-- b000029 | contents | pages [2] -->
1.2

<!-- b000030 | contents | pages [2] -->
Our Thinking................................................................................................................4

<!-- b000031 | contents | pages [2] -->
1.3

<!-- b000032 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000033 | contents | pages [2] -->
5

<!-- b000034 | contents | pages [2] -->
Assumptions.................................................................................................................5

<!-- b000035 | contents | pages [2] -->
2.1

<!-- b000036 | contents | pages [2] -->
Notations.......................................................................................................................6

<!-- b000037 | contents | pages [2] -->
2.2

<!-- b000038 | contents | pages [2] -->
3 Data Preprocessing

<!-- b000039 | contents | pages [2] -->
6

<!-- b000040 | contents | pages [2] -->
Default Value Processing............................................................................................6

<!-- b000041 | contents | pages [2] -->
3.1

<!-- b000042 | contents | pages [2] -->
Abnormal Value Processing....................................................................................... 6

<!-- b000043 | contents | pages [2] -->
3.2

<!-- b000044 | contents | pages [2] -->
Data Synthesis and Classification............................................................................. 7

<!-- b000045 | contents | pages [2] -->
3.3

<!-- b000046 | contents | pages [2] -->
4 Energy Profile

<!-- b000047 | contents | pages [2] -->
7

<!-- b000048 | contents | pages [2] -->
5 Model Construction

<!-- b000049 | contents | pages [2] -->
10

<!-- b000050 | contents | pages [2] -->
Decoupling Analysis.................................................................................................10

<!-- b000051 | contents | pages [2] -->
5.1

<!-- b000052 | contents | pages [2] -->
The Simultaneous Equations Model.......................................................................10

<!-- b000053 | contents | pages [2] -->
5.2

<!-- b000054 | contents | pages [2] -->
The Multi-dimensional Evaluation System........................................................... 12

<!-- b000055 | contents | pages [2] -->
5.3

<!-- b000056 | contents | pages [2] -->
Construction of Indexes...............................................................................12

<!-- b000057 | contents | pages [2] -->
5.3.1

<!-- b000058 | contents | pages [2] -->
Principle Component Analysis...................................................................13

<!-- b000059 | contents | pages [2] -->
5.3.2

<!-- b000060 | contents | pages [2] -->
Energy Profile Predicting System............................................................................14

<!-- b000061 | contents | pages [2] -->
5.4

<!-- b000062 | contents | pages [2] -->
Determining the Predictors......................................................................... 14

<!-- b000063 | contents | pages [2] -->
5.4.1

<!-- b000064 | contents | pages [2] -->
Constructing BP Neural Network.............................................................. 15

<!-- b000065 | contents | pages [2] -->
5.4.2

<!-- b000066 | contents | pages [2] -->
Analyzing the Error......................................................................................17

<!-- b000067 | contents | pages [2] -->
5.4.3

<!-- b000068 | contents | pages [2] -->
Predicting the Target Values........................................................................17

<!-- b000069 | contents | pages [2] -->
5.4.4

<!-- b000070 | contents | pages [2] -->
6 Testing Our Model

<!-- b000071 | contents | pages [2] -->
19

<!-- b000072 | contents | pages [2] -->
Predicting Reliability Test.........................................................................................19

<!-- b000073 | contents | pages [2] -->
6.1

<!-- b000074 | contents | pages [2] -->
Sensitivity Analysis................................................................................................... 19

<!-- b000075 | contents | pages [2] -->
6.2

<!-- b000076 | contents | pages [2] -->
7 Determining Goals for the Energy Compact

<!-- b000077 | contents | pages [2] -->
20

<!-- b000078 | contents | pages [2] -->
Idea one: Don’t cooperate........................................................................................ 20

<!-- b000079 | contents | pages [2] -->
7.1

<!-- b000080 | contents | pages [2] -->
Idea two: Cooperate..................................................................................................20

<!-- b000081 | contents | pages [2] -->
7.2

<!-- b000082 | contents | pages [2] -->
Goals and Actions......................................................................................................20

<!-- b000083 | contents | pages [2] -->
7.3

<!-- b000084 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000085 | furniture | pages [3] -->
Team # 73767

<!-- b000086 | furniture | pages [3] -->
Page 2 of 28

<!-- b000087 | heading | pages [3] -->
8 Conclusions

<!-- b000088 | prose | pages [3] -->
21

<!-- b000089 | heading | pages [3] -->
9 Strengths and Weaknesses

<!-- b000090 | prose | pages [3] -->
21 Strengths..................................................................................................................... 21 9.1 Weaknesses................................................................................................................. 22 9.2

<!-- b000091 | heading | pages [3] -->
References

<!-- b000092 | references | pages [3] -->
22

<!-- b000093 | heading | pages [3] -->
Appendices

<!-- b000094 | prose | pages [3] -->
23

<!-- b000095 | heading | pages [3] -->
Appendix A Profiles of Arizona

<!-- b000096 | prose | pages [3] -->
23

<!-- b000097 | heading | pages [3] -->
Appendix B Profile of New Mexico

<!-- b000098 | prose | pages [3] -->
25

<!-- b000099 | heading | pages [3] -->
Appendix C Profiles of Texas

<!-- b000100 | prose | pages [3] -->
25

<!-- b000101 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000102 | furniture | pages [4] -->
Team # 73767

<!-- b000103 | furniture | pages [4] -->
Page 3 of 28

<!-- b000104 | heading | pages [4] -->
MEMO

<!-- b000105 | prose | pages [4] -->
From: Team 73767, MCM 2018 To: The group of Governors Date: February 13, 2018 Subject: Goals for the interstate energy compact

<!-- b000106 | prose | pages [4] -->
Dear governors, we are honored to inform you our achievement after performing data analysis and modeling.

<!-- b000107 | prose | pages [4] -->
First, we introduce the energy profiles of your states in 2009. We use comprehensive utilization performance (CUP) to reflect the energy profile on the whole. Ranking the CUP of your four states, California appears to be the best. In terms of the usage of cleaner renewable energy, California, Arizona, Texas and New Mexico has the largest consumption successively in the water power, nuclear power, wind power and solar power. It is decided by the natural environment of your four states, such as geography and climate.

<!-- b000108 | prose | pages [4] -->
Then, we provide you the goals for the interstate energy compact. Through predict- ing, your four states’ average CUP will increase to 16.98 by 2025 and to 26.05 by 2050,if your four states can cooperate adequately. Based on the predictions, we set the develop- ment goals as follows:

<!-- b000109 | prose | pages [4] -->
• Building a community of energy utilization and economic development, so as to realize manual benefit and win-win result.

<!-- b000110 | prose | pages [4] -->
• Promoting the production and usage of new energy sources and reducing the de- pendence on traditional fossil fuels.

<!-- b000111 | prose | pages [4] -->
• Increasing the whole economy’s comprehensive utilization performance to 16.98 by 2025 and to 26.05 by 2050, and achieving the harmony of economy, energy and environment ultimately.

<!-- b000112 | prose | pages [4] -->
According to the goals above and the characteristics of each of your four states, we offer you the following suggestions to meet the goals.

<!-- b000113 | prose | pages [4] -->
• Building an energy investment bank to integrate money for developing the clear renewable energy.

<!-- b000114 | prose | pages [4] -->
• Enhancing residuals’ environmental protection consciousness.

<!-- b000115 | prose | pages [4] -->
• Adjusting the industrial structure properly.

<!-- b000116 | prose | pages [4] -->
We sincerely hope that you can achieve the goals above!

<!-- b000117 | prose | pages [4] -->
Please contact us if you have any problems.

<!-- b000118 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000119 | furniture | pages [5] -->
Team # 73767

<!-- b000120 | furniture | pages [5] -->
Page 4 of 28

<!-- b000121 | heading | pages [5] -->
1 Introduction

<!-- b000122 | heading | pages [5] -->
1.1 Problem Statement

<!-- b000123 | prose | pages [5] -->
Energy is the main material base and driving force for human’s daily production and life. The proper utilization of all kinds of energy are closely link to the sustainability of economic development. The excessive consumption of traditional fossil fuels not only restricts the economic development, but also causes a series of environmental problems, such as global warming. Therefore, in America, many states have been trying to im- prove the production and usage of energy. A successful practice is that some states with different strengths and weaknesses unite to form an interstate compact, for promoting the usage of cleaner, renewable energy sources, through cooperation and adherence to specific policies.

<!-- b000124 | prose | pages [5] -->
In the southwest of the U.S., there are four states – California (CA), Arizona (AZ), New Mexico (NM), and Texas (TX) – that hope to form a realistic new energy compact as well. Asked by the four governors of these sates, we determine a set of development goals for the energy compact.

<!-- b000125 | heading | pages [5] -->
1.2 Our Goals

<!-- b000126 | prose | pages [5] -->
Based on our understanding of the problem, we set the following goals:

<!-- b000127 | prose | pages [5] -->
• Use the given data to found an energy profile for each state.

<!-- b000128 | prose | pages [5] -->
• Develop a model system to show the dynamic relationships between various en- ergy consumption and economic development of each of the four states, and ex- plore the underlying factors that lead to these relationships.

<!-- b000129 | prose | pages [5] -->
• Define the“best”profile for use of cleaner, renewable energy, then set up a system of evaluation to determine the state that has the“best”profile in2009.

<!-- b000130 | prose | pages [5] -->
• According to the analysis above, develop a model and set different scenarios to predict the energy profile of each state for 2025 and 2050.

<!-- b000131 | prose | pages [5] -->
• Based on the established models, decide the usage targets of cleaner and renewable energy for 2025 and 2050. Then provide three actions for the four states to achieve the goals.

<!-- b000132 | heading | pages [5] -->
1.3 Our Thinking

<!-- b000133 | prose | pages [5] -->
This is a typical big data problem, so we solve it from the point of view of statistical analysis. Here is our thinking.

<!-- b000134 | prose | pages [5] -->
First, we preprocess the data provided, which includes default value processing, ab- normal value processing and data synthesis and classification. Based on our definitions, we select some major energy sources for analysis and divide them into two categories. One is called cleaner renewable energy (CRE), the other is called traditional fossil en- ergy (TFE). The specific definitions will be given later.

<!-- b000135 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000136 | furniture | pages [6] -->
Team # 73767

<!-- b000137 | furniture | pages [6] -->
Page 5 of 28

<!-- b000138 | prose | pages [6] -->
Second, we select some important data from the dataset provided to construct the energy profile. Through statistical charts, we visualize them. In this way, we found an energy profile for each state. Comparing the energy files of the four states, we find dif- ferences in their utilization of the two kinds of energy sources. To further clarify the dif- ferences, we learn from the decoupling theory and use coefficients of elasticity to show the dynamic relationships between various energy consumption and economic devel- opment of each state. Then we use the simultaneous equations model to respectively analyze the four states’ economy systems, in which way, we find out the reasons why the differences exist.

<!-- b000139 | prose | pages [6] -->
Third, weintroduce the conceptof thecomprehensive utilization performance (CUP) to evaluate which of the four states appeared to have the“best”profile. Since different states have their own characteristics, therefore, we establish a multi-dimensional evalua- tion system to measure the comprehensive utilization performance in case of bias. Then we use principle component analysis (PCA) to integrate each evaluation index into an overall index, namely the comprehensive utilization performance.

<!-- b000140 | prose | pages [6] -->
Finally, we build the BP neural network to predict the energy profile of each state. By setting various change trajectory of independent variables, we get the predictions successfully. After that, we regard the four states as a whole to determine renewable energy usage targets for 2025 and 2050.

<!-- b000141 | heading | pages [6] -->
2 Assumptions and Notations

<!-- b000142 | heading | pages [6] -->
2.1 Assumptions

<!-- b000143 | prose | pages [6] -->
Due to lack of necessary data and limitation of our knowledge, we make the follow- ing assumptions to help us perform modeling. These assumptions are the premise for our subsequent analysis.

<!-- b000144 | prose | pages [6] -->
• For the four states, all kinds of energy they produce are consumed by themselves each year. Thus we can replace energy output with energy consumption in calcu- lation.

<!-- b000145 | prose | pages [6] -->
• The policy of each state will not change in the future. This assumption may be not realistic, but it is essential for us when predicting the energy profile in 2025 and 2050.

<!-- b000146 | prose | pages [6] -->
• The natural environment of the each states will not change. So we can see it as constant. This assumption simplify our analysis, and it is reasonable, since the natural environment is usually stable.

<!-- b000147 | prose | pages [6] -->
• Once forming an interstate energy compact, the four states can develop and utilize resources together. Thus they can realize manual benefit and win-win result.

<!-- b000148 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000149 | furniture | pages [7] -->
Team # 73767

<!-- b000150 | furniture | pages [7] -->
Page 6 of 28

<!-- b000151 | heading | pages [7] -->
2.2 Notations

<!-- b000152 | prose | pages [7] -->
Here are the notations and their meanings in our paper:

<!-- b000153 | heading | pages [7] -->
Notation

<!-- b000154 | prose | pages [7] -->
Meaning Epd Electricity production Tpd Total energy production Rce Renewable energy expenditure ttdp GDP Cpd Renewable energy production Pri Price energy Ind Secondary industry consumption Pop Population Wcs Wood consumption Tcs TFE consumption Enc Total energy consumption Cep Carbon emission per capita K Energy expenditures as share of GDP

<!-- b000155 | caption | pages [7] -->
Table 1: notation

<!-- b000156 | heading | pages [7] -->
3 Data Preprocessing

<!-- b000157 | prose | pages [7] -->
For data-analysis problem, there are usually some incomplete and abnormal datain the large amount of raw data, which may seriously affect the efficiency of modeling and the accuracy of conclusions. So it is quite important to preprocess the data.

<!-- b000158 | heading | pages [7] -->
3.1 Default Value Processing

<!-- b000159 | prose | pages [7] -->
We use different methods to process variables with various degrees of data loss. (1) For variables with large amount of data missing, we just delete it. Because small data cannot provide enough and valuable information for our modeling. (2) For variables with a small amount of data missing, we use interpolation method to compensate the data. More specifically, we first use existing data points to establish an appropriate in- terpolation function, and then replace the missing value with the function value f(xi) at the corresponding point xi.

<!-- b000160 | heading | pages [7] -->
3.2 Abnormal Value Processing

<!-- b000161 | prose | pages [7] -->
If a value in a set of data is more than twice the standard deviation of the average, we call it the abnormal value. Statistically we can use a box-plot to identify the abnormal values. For the abnormal value, we fix it with the average value of its two adjacent observations.

<!-- b000162 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000163 | furniture | pages [8] -->
Team # 73767

<!-- b000164 | furniture | pages [8] -->
Page 7 of 28

<!-- b000165 | heading | pages [8] -->
3.3 Data Synthesis and Classification

<!-- b000166 | prose | pages [8] -->
There are 605 variables in the dataset provided. Not all of them are used in our model. Thus, we sort the data we need into a new dataset. Besides, we divide the energy sources into two categories for the further analysis, One is called cleaner renewable en- ergy, which includes the hydroenergy, the wind energy, the geothermal energy, the solar energy and the ethanol; the other is called traditional fossil energy, which includes the coal, the petroleum, the natural gas and other fuels.

<!-- b000167 | prose | pages [8] -->
Definition:

<!-- b000168 | prose | pages [8] -->
• Cleaner renewable energy is the energy that produces little pollution and can be used directly in the production and life.

<!-- b000169 | prose | pages [8] -->
• Traditional fossil energy is non−renewable energy and will cause air pollution after burning.

<!-- b000170 | prose | pages [8] -->
In our model, some synthesized variables are used, for example, the average price of cleaner renewable energy. It can be calculated according to formula (1). Other synthe- sized variables will be explained later.

<!-- b000171 | prose | pages [8] -->
Σ

<!-- b000172 | heading | pages [8] -->
4 Energy Profile

<!-- b000173 | prose | pages [8] -->
After data preprocessing, we choose 11 important variables to create the energy pro- file. we call them the basic variables

<!-- b000174 | heading | pages [8] -->
Notation

<!-- b000175 | prose | pages [8] -->
Abbreviation in the original data set GDP GDPRX Total population TPOPP TFE consumption FFTCB Total consumption TETCB Wood consumption WWTCB Electricity production ESTCB Total energy production TEPRB Price of renewable energy AVACD Renewable energy production REPRB Renewable energy expenditure RFEIV Secondary industry consumption TEICB

<!-- b000176 | caption | pages [8] -->
Table 2: basic variable

<!-- b000177 | prose | pages [8] -->
Descriptive statistics is usually the first step in statistical analysis, which can shows the important features of the data visually through graphs and tables. In view of this, we adopt the descriptive statistics method to show the energy profile of each state. Here is the energy profile of California, those of other states are attached to the appendix.

<!-- b000178 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000179 | furniture | pages [9] -->
Team # 73767

<!-- b000180 | furniture | pages [9] -->
Page 8 of 28

<!-- b000181 | caption | pages [9] -->
Figure 1: change trend of price and energy consumption in California

<!-- b000182 | caption | pages [9] -->
Figure 2: energy consumption of different items in California

<!-- b000183 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000184 | furniture | pages [10] -->
Team # 73767

<!-- b000185 | furniture | pages [10] -->
Page 9 of 28

<!-- b000186 | caption | pages [10] -->
Figure 2 :

<!-- b000187 | prose | pages [10] -->
Pic1 Trend graph of TFE and its price Pic2 Trend graph of CRE and itsprice Pic3 Trend graph of totalconsumption(TC) and its price Pic4 Trend graph of the ratio of TFE to TC and CRE to TC

<!-- b000188 | caption | pages [10] -->
Figure 3 :

<!-- b000189 | prose | pages [10] -->
F Fuel enthanol C Coal HY Hydroelectricity PE Petroleum products GE Geothermal energy NG Natural gas WE Wind energy OT Other PH&SO Photovoltaic and so- lar thermal energy (Only the unit of "F"is Thausand Barrels)

<!-- b000190 | caption | pages [10] -->
Table 3: the cutline in Figure 2 and Figure 3

<!-- b000191 | caption | pages [10] -->
Figure 3: constitution of total energy consumption in California in 2009

<!-- b000192 | prose | pages [10, 11] -->
Variable Quantitative Change Rate of Change Energy total production 510310.93(Billion Btu) 156.56% Renewable energy total production 28262.33(Billion Btu) 383.32% Fossil fuels, total production 482048.60(Billion Btu) 151.32% Electricity production 16995.11(Billion Btu) 2279.84% Wood consumption 4244.64(Billion Btu) 64.04% Secondary industry consumption 414753.42(Billion Btu) 199.64% Renewable energy total end-use expenditures 750.17(Million dollars) 873.31% GDP 59090(Million dollars) 593.15% By comparing the energy profiles of the four states, we preliminarily reached the following conclusions:

<!-- b000193 | caption | pages [10] -->
Table 4: quantitative change and rate of change of typical variables from 1960 to 2009

<!-- b000194 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000195 | furniture | pages [11] -->
Team # 73767

<!-- b000196 | furniture | pages [11] -->
Page 10 of 28

<!-- b000198 | prose | pages [11] -->
Overall, the four states differ in their utilization and consumption of the two types • of energy (CRE&TFE).

<!-- b000199 | prose | pages [11] -->
Each of the four states has a growing share of CRE consumption, while the share • of TFE is still high.

<!-- b000200 | prose | pages [11] -->
California ranks the first in terms of the amount of CRE consumption; Arizona • ranks the first in terms of the share of CRE consumption. However, New Mexico lags behind in the usage and consumption of CRE.

<!-- b000201 | heading | pages [11] -->
5 Model Construction

<!-- b000202 | heading | pages [11] -->
5.1 Decoupling Analysis

<!-- b000203 | prose | pages [11] -->
Since having had a general idea of the energy profiles of the four states, we now in- tend to calculate the coefficients of elasticity to deeply analyze the dependency between economic development and the various energy consumption of each state. According to the decoupling theory, the higher the absolute value of the elasticity, the stronger the [1]The formula of coefficient of elasticity is asfollow. dependency.

<!-- b000204 | prose | pages [11] -->
The calculation results are shown in figure 4. From the figure, we can intuitively know that generally the dependency between economic development and CRE con- sumption is on the rise for each state, but the intensity of the dependency differs among the four states.

<!-- b000205 | caption | pages [11] -->
Figure 4: elasticity coefficient of FTE(left) and CRE(right)

<!-- b000206 | heading | pages [11] -->
5.2 The Simultaneous Equations Model

<!-- b000207 | prose | pages [11, 12] -->
To explore the underlying factors that leads to the differences of energy files among the four states, we develop a simultaneous equations model, as shown below. Different syste m from single equation regression, simultaneous more equations model can explain the complex economic comp rehensively and accurately. We introduce three (3)

<!-- b000208 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000210 | furniture | pages [12] -->
Team # 73767

<!-- b000211 | furniture | pages [12] -->
Page 11 of 28

<!-- b000212 | prose | pages [12] -->
equations into the model, since there are interactions between each two of the three elements, eco- nomic development, energy consumption, and [2] environmental pollution.

<!-- b000213 | prose | pages [12] -->
where X is a set of controlling variables on the natural environment Lack of variable data on the natural environment, we neglect the set of controlling variables X to solve the model. The regression results of equation ln(Enc) are shown in the following table. The regression coefficients reflect the influence of explanatory variables on dependent variables, from which we can determine the impact of different factors on the energy variable.

<!-- b000214 | prose | pages [12] -->
TFE CRE Equation 1 AZ CA NM TX AZ CA NM TX

<!-- b000215 | prose | pages [12] -->
ln(ttdp) 0.2189*** 0.5122** 0.4896** 1.2368*** 0.1904*** 0.4915** 0.2167* 0.4532**

<!-- b000216 | prose | pages [12] -->
ln(Cep) 0.0012 0.0104** 0.1326** 0.1725** 0.0031 0.0113* 0.0682** 0.1651***

<!-- b000217 | prose | pages [12] -->
ln(K) 0.2169** 0.3481** 0.2018* 0.3018** 0.2267** 0.4162** 0.2481*** 0.3156*

<!-- b000218 | prose | pages [12] -->
ln(Pop) 0.0104 0.0341 0.0361* -0.2214 0.0133 0.0265 0.0421* -0.2153

<!-- b000219 | prose | pages [12] -->
ln(Pri) 0.1152* 0.1421 0.1102** 0.2451 0.1842* 0.1821* 0.2012** 0.2201

<!-- b000220 | prose | pages [12] -->
ln(Ind) 0.1421* 0.4142*** 0.2269* 0.2684** 0.1723* 0.3841*** 0.2362* 0.2758*

<!-- b000221 | prose | pages [12] -->
Constant 17.6421* 19.2364* 13.2631* 50.3641* 16.6372* 37.6298* 13.2156* 61.2571*

<!-- b000222 | caption | pages [12] -->
Table 5: the regression results of Equation 1

<!-- b000223 | prose | pages [12] -->
*，**，*** respectively represent the confidence of 10%,5%,1% From the Table 5, we can see that population has no significant influence on the en- ergy consumption. While the the economic development and the share of secondary industy have significant influence on the energy consumption.

<!-- b000224 | prose | pages [12] -->
To determine the influence of geography and climate, we collect information about the natural environment of the four states, which is shown in Figure 5. It shows the resource distribution of solar power, wind power and hydroelectric power.

<!-- b000225 | prose | pages [12] -->
From Figure 5, we know that the four states differ in the potential of CRE production. The differences are caused by the various natural environment of the four states, such as climate and geography.

<!-- b000226 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000227 | furniture | pages [13] -->
Team # 73767

<!-- b000228 | furniture | pages [13] -->
Page 12 of 28

<!-- b000229 | caption | pages [13] -->
Figure 5: resource distribution of CRE

<!-- b000230 | heading | pages [13] -->
5.3 The Multi-dimensional Evaluation System

<!-- b000231 | prose | pages [13] -->
In this part, we will determine which of the four states has the“best”energy profile in 2009. Through the above analysis, we know that the four states differ in strengths and weaknesses congenitally. Thus, for avoiding bias, we establish a multi-dimensional evaluation system to measure their energy profile.

<!-- b000232 | heading | pages [13] -->
5.3.1 Construction of Indexes

<!-- b000233 | prose | pages [13] -->
The core indexes of our evaluation system is called comprehensive utilization perfor- mance (CUP), which reflects the development and utilization level of CRE. The CUP is composed of three parts, energy performance, economic performance and environment performance. And each of the three parts includes three indexes as well. These indexes and their formulas are detailed in the Table 6.

<!-- b000234 | caption | pages [13] -->
Figure 6: evaluation index systerm

<!-- b000235 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000236 | furniture | pages [14] -->
Team # 73767

<!-- b000237 | furniture | pages [14] -->
Page 13 of 28

<!-- b000238 | prose | pages [14] -->
Name of Index Meaning Formula Reflects the status of the CRE De = Cpd Development development and utilization in Epd Efficiency (De) the electricity industry.

<!-- b000239 | prose | pages [14] -->
Reflects the sustainability of Dp = (Cpdt −Cpdt−1) Development Energy CRE development and Cpdt−1 Potential (Dp) performance utilization. (Ep) Reflects the contribution of Development Dpa = Cpd CRE development and Achievements Tpd utilization to the state energy (Dpa) structure.

<!-- b000240 | prose | pages [14] -->
Reflect the state’s support for Es = Rce Economic renewable energy at the ttdp support (Es) investment level Reflect the efficiency and Roi = Cpd Economic Rate of return on profitability of investment on proformance investment (Roi) Rce renewable energy (Epf ) Equilibrium of 1 Reflect supply’s satisfaction Esd = supply and with demand Pc demand (Esd) Secondary Reflects the dependence on Sip = Scs industry polluting industries in each T ocs proportion (Sip) state.

<!-- b000241 | prose | pages [14] -->
Reflectis the situation of the Cep = Tcs Carbon emission Environment greenhouse gas emission per Tpo per capita (Cep) performance capita. (Enp) Consumption of Reflects the situation of natural Cnr = Wcs natural resources resources consumption per Tpo per capita (Csr) capita.

<!-- b000242 | caption | pages [14] -->
Table 6: indexes and their formulas

<!-- b000243 | heading | pages [14] -->
5.3.2 Principle Component Analysis

<!-- b000244 | prose | pages [14] -->
We use the PCA method to integrate each evaluation index into an overall index, namely the comprehensive utilization performance. Then through the comparison of the CUP values of the four states, we determine the“best”state.

<!-- b000245 | prose | pages [14] -->
First, we use the given data and the formulas in Table 6 to calculate the evaluation indexes. And then, we use the equation below to standardize the values of these indexes.

<!-- b000246 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000247 | furniture | pages [15] -->
Team # 73767

<!-- b000248 | furniture | pages [15] -->
Page 14 of 28

<!-- b000249 | prose | pages [15] -->
The results of PCA is showed in table 7. from the table, we can see that California has the“best”energy profile in 2009.

<!-- b000250 | prose | pages [15] -->
Rank State PCA Score 1 California 0.9433 2 Texas 0.5561 3 Arizona 0.2466 4 New Mexico -1.7459

<!-- b000251 | caption | pages [15] -->
Table 7: PCA scores

<!-- b000252 | heading | pages [15] -->
5.4 Energy Profile Predicting System

<!-- b000253 | heading | pages [15] -->
5.4.1 Determining the Predictors

<!-- b000254 | prose | pages [15, 16] -->
In part 5.3, we measured the energy file in three dimensions, energy performance, economic performance and environment performance. For the following analysis, we selectan index fromeach of them to calculate the comprehensive utilization performance (CUP) in a different way.

<!-- b000255 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000256 | furniture | pages [16] -->
Team # 73767

<!-- b000257 | furniture | pages [16] -->
Page 15 of 28

<!-- b000259 | prose | pages [16] -->
The indexes we select are Dpa, Roi and Cep. Analogous to Cobb-Douglas Production Function in economics, we derive the following formula.

<!-- b000260 | prose | pages [16] -->
CUP = A (Dpa)α (Roi)β Cepγ (9) · · · where :

<!-- b000261 | prose | pages [16] -->
A is unit correction factor;

<!-- b000262 | prose | pages [16] -->
α,β,γ are weight coefficients of variables;

<!-- b000263 | prose | pages [16] -->
α + β + γ = 1.

<!-- b000264 | prose | pages [16] -->
In the previous analysis, we pointed out that, there is an interaction between each [3] Therefore, we choose tow of the three elements, economy, energy and environment. ttDP per capital (ttdp) , Secondary industry proportion (Sip) and carbon emission per capita (Cep) as the independent variables in prediction. Then we can drive the following equation.

<!-- b000265 | prose | pages [16] -->
(10) CUP = θ0 + θ1ttdp + θ2Sip + θ3Cep + ε

<!-- b000266 | heading | pages [16] -->
5.4.2 Constructing BP Neural Network

<!-- b000267 | prose | pages [16] -->
Since we have to predict the energy profiles of the four states respectively, it is a heavy task. Thus, we utilize the intelligent algorithm (BP neural network) with high prediction efficiency to finish this work. It has been proved theoretically that BP neural network can approach any nonlinear function with higher precision. The flow chart below shows the principle of BP neural network.

<!-- b000268 | caption | pages [16] -->
Figure 7: the principle of BP neural network

<!-- b000269 | prose | pages [16, 17] -->
There are two steps in the process of constructing BP neural network. First, we should set the network parameter k that represents the numbers of neurons. Here we let k = 9. Second, we use existing data of input and output to train the network. We now

<!-- b000270 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000272 | furniture | pages [17] -->
Team # 73767

<!-- b000273 | furniture | pages [17] -->
Page 16 of 28

<!-- b000274 | prose | pages [17] -->
drive the core formulas of the BP Network.

<!-- b000275 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000276 | furniture | pages [18] -->
Team # 73767

<!-- b000277 | furniture | pages [18] -->
Page 17 of 28

<!-- b000278 | heading | pages [18] -->
5.4.3 Predicting the TargetValues

<!-- b000279 | prose | pages [18] -->
Topredict the dependent variable, we have to know the independent variablesfirst. Unfortunately, we lack the values of ttdp, Sip and Cep for 2025 and 2050. So we can only predict the dependent variable by setting the change trajectory of the three independent [4] variables in advance. Weset two scenarios in total.

<!-- b000280 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000281 | furniture | pages [19] -->
Team # 73767

<!-- b000282 | furniture | pages [19] -->
Page 18 of 28

<!-- b000283 | caption | pages [19] -->
Figure 8: the fitting results

<!-- b000284 | caption | pages [19] -->
Figure 9: Scenario one

<!-- b000285 | caption | pages [19] -->
Figure 10: Scenario two

<!-- b000286 | prose | pages [19] -->
Scenario one: Linear trend • As is shown in figure 9, if the change of the three independent variables follows the linear trend. We can use the formula 15 to characterize their trajectory.

<!-- b000287 | prose | pages [19] -->
(20) xt = xt−1 + a

<!-- b000288 | prose | pages [19] -->
Scenario two: Smooth fluctuation • As is shown in figure 10, if the change of the three independent variables follow the smooth fluctuation. Wecan use autoregressive moving average model, ARMA(p,q) [5] to characterize their trajectory.

<!-- b000289 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000290 | furniture | pages [20] -->
Team # 73767

<!-- b000291 | furniture | pages [20] -->
Page 19 of 28

<!-- b000292 | prose | pages [20] -->
(21) xt = φ0 + φ1xt−1 + φ2xt−2 + φpxt−p + εt −θ1εt−1 + θ2εt−2 −θqεt−q + µ Once determining the change trajectory of independent variables, we can estimate their values. Entering them to the BP networks, we get the predicted values of the CUP of each states. The results are shown in table 9.

<!-- b000293 | prose | pages [20] -->
Scenario 1 Scenario 2 Year DPA ROI CEC CUP DPA ROI CEC CUP 2025 0.06 25.16 170.97 23.92 0.05 22.15 190.26 23.49 AZ 2050 0.07 50.45 100.45 40.19 0.06 50.15 120.15 35.22 2025 0.08 30.04 138.63 28.39 0.10 29.36 145.26 26.14 CA 2050 0.09 57.87 89.14 45.15 0.12 55.86 108.15 39.15 2025 0.07 50.14 350.45 8.20 0.07 41.26 351.22 7.89 NM 2050 0.08 59.85 282.43 15.16 0.09 57.12 301.86 14.12 2025 0.05 20.60 348.15 7.84 0.05 19.26 369.15 6.95 TX 2050 0.08 48.29 321.53 14.50 0.08 44.12 348.85 12.19

<!-- b000294 | caption | pages [20] -->
Table 9: the predicting results

<!-- b000295 | heading | pages [20] -->
6 Testing Our Model

<!-- b000296 | heading | pages [20] -->
6.1 Predicting Reliability Test

<!-- b000297 | prose | pages [20] -->
To test the predicting reliability of the BP network, we collect relevant data of each state from 2010 to 2015, and use them to predict the CUP. Then we use formula 15 again to compute the average error between the predicted values and the actual ones. Here are the results.

<!-- b000298 | prose | pages [20] -->
The predicting error State California Arizona New Mexico Texas Error 5.89% 6.24% 7.98% 10.07%

<!-- b000299 | caption | pages [20] -->
Table 10: the predicting error

<!-- b000300 | heading | pages [20] -->
6.2 Sensitivity Analysis

<!-- b000301 | prose | pages [20] -->
In the process of constructing BP network, we let the network parameter k = 9. How does the change of kinfluence the predicting results? Weanalyze the average deviation of CUP caused by changing k slightly.

<!-- b000302 | prose | pages [20] -->
State k-2 k-1 k+1 k+2 AZ 11.08% 4.43% 3.54% 8.51% CA 8.19% 3.15% 4.66% 10.80% NM 9.78% 5.39% 4.66% 12.28% TX 6.66% 2.19% 2.28% 12.33% Mean 8.93% 3.79% 3.79% 10.98%

<!-- b000303 | caption | pages [20] -->
Table 11: the influence by changing k

<!-- b000304 | prose | pages [20] -->
From table 11, we can find that the influence of k is not big, which we can bear.

<!-- b000305 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000306 | furniture | pages [21] -->
Team # 73767

<!-- b000307 | furniture | pages [21] -->
Page 20 of 28

<!-- b000308 | heading | pages [21] -->
7 Determining Goals for the Energy Compact

<!-- b000309 | heading | pages [21] -->
7.1 Idea one: Don’t cooperate

<!-- b000310 | prose | pages [21] -->
If the four states don’t cooperate, which means they develop independently, they can only utilize their own resources to enhance the level of renewable energy usage. In this condition, we can just use the predicted values in part 5.4 as their respective targets.

<!-- b000311 | prose | pages [21] -->
For the two scenarios in part 5.4, we think that scenario two is more reasonable and realistic. Because the evolution of the macro-economy is usually stable, especially for [6] So we just take scenario two into consider- advanced economies like the United States. ation.

<!-- b000312 | prose | pages [21] -->
In scenario two, the average comprehensive utilization performance can increase to 16.12 and 25.17 successively in 2025 and 2050.

<!-- b000313 | heading | pages [21] -->
7.2 Idea two: Cooperate

<!-- b000314 | prose | pages [21] -->
Given that the four-state energy compact is an interstate compact, it is necessary for the tour states to cooperate. We presume that they can develop and utilize resources together. In this case, we regard the four states as a whole economy. Then we use pre- vious method and models to predict the whole economy’s comprehensive utilization performance for 2025 and 2050.

<!-- b000315 | prose | pages [21] -->
Year 2025 2050 The whole 16.98 26.05 economy’s CUP

<!-- b000316 | caption | pages [21] -->
Table 12: predictions of the whole economy

<!-- b000317 | prose | pages [21] -->
The results shows that the whole economy’s comprehensive utilization performance can increase to 16.98 and 26.05 successively in 2025 and 2050, and each of them is higher than that in idea one. Maybe it is because cooperation enables the four states to give full play to their own advantages and promote the development and utilization of cleaner [7] renewable energy.

<!-- b000318 | heading | pages [21] -->
7.3 Goals and Actions

<!-- b000319 | prose | pages [21] -->
Based on the results in idea two and the previous analysis, we set the following goals for the four-state energy compact.

<!-- b000320 | prose | pages [21] -->
Building a community of energy utilization and economic development, so as to • realize manual benefit and win-win result.

<!-- b000321 | prose | pages [21] -->
Promoting the production and usage of new energy sources and reducing then • dependence on traditional fossil fuels.

<!-- b000322 | prose | pages [21] -->
Increasing the whole economy’s comprehensive utilization performance to 16.98 • by 2025 and to 26.05 by 2050, and achieving the harmony of economy, energy and environment ultimately.

<!-- b000323 | prose | pages [21] -->
According to the goals above and the characteristics of each state, we propose the actions and measures for the four states.

<!-- b000324 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000325 | furniture | pages [22] -->
Team # 73767

<!-- b000326 | furniture | pages [22] -->
Page 21 of 28

<!-- b000327 | prose | pages [22] -->
Focus on developing their own advantageous energy resource and share their en- • ergy and achievements with others.

<!-- b000328 | prose | pages [22] -->
Make more investment in scientific research to make better use of renewable en- • ergy to improve the low utilization efficiency of new energy sources.

<!-- b000329 | prose | pages [22] -->
Introduce a proper subsidy policy to award the enterprises who develop new en- • ergy source.

<!-- b000330 | prose | pages [22] -->
Make certain quantitative index and do statistic periodically to make sure the di- • rection of energy development is going well.

<!-- b000331 | heading | pages [22] -->
8 Conclusions

<!-- b000332 | prose | pages [22] -->
We are asked by the governors of the four states to set some goals for their interstate energy compact. After performing data analysis and modeling, we have finished the task successfully. First, Using decoupling theory and simultaneous equations model, we characterize the evolution of energy profile of each state from 1960 – 2009, and find out the influential factors. We have known that it is the differences of economic level, indus- trial structure and natural environment that lead to the distinct energy profiles of each state. In terms the production and usage of cleaner renewable energy, each of the four states has a growing share of CRE consumption, while the share of TFE consumptionis still high.

<!-- b000333 | prose | pages [22] -->
Second, we construct a multi-dimensional Evaluation System and introduce the core concept in this paper, named comprehensive utilization performance (CUP), which re- flects the development and utilization level of CRE. Through the PCA method, we de- termine that California has the“best”energy profile.

<!-- b000334 | prose | pages [22] -->
Finally, based on the previous analysis, we build BP neural network for predicting the energy profile of each state. By setting various change trajectory of independent variables, we get the target values successfully. After that, we regard the four states as a whole to determine renewable energy usage targets for 2025 and 2050. In this process, we use BP neutral network again.

<!-- b000335 | heading | pages [22] -->
9 Strengths and Weaknesses

<!-- b000336 | heading | pages [22] -->
9.1 Strengths

<!-- b000337 | prose | pages [22] -->
Data preprocessing.When faced with big data problem, the data processing is very • important. Through this step, we greatly improve the quality of the data. Thus, it is more efficient and convenient for us to solve theproblem.

<!-- b000338 | prose | pages [22] -->
Accuracy and stability.We use BP neutral network to make predictions. It is a pow- • erful algorithm with great nonlinear approximation ability. The error test shows that our predicting results are more accurate. Besides, when changing the network parameter k, its influence is not large. So the BP network is morestable.

<!-- b000339 | prose | pages [22] -->
Good expansibility and flexibility. There are three parameters α, β and γ in our • CUP equation, which can be used to reflect the importance of corresponding indi- cators. In different situations, we can adjust them flexibly.

<!-- b000340 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000341 | furniture | pages [23] -->
Team # 73767

<!-- b000342 | furniture | pages [23] -->
Page 22 of 28

<!-- b000343 | heading | pages [23] -->
9.2 Weaknesses

<!-- b000344 | prose | pages [23] -->
Subjectivity.The calculation of some synthesized variables is subjective. It can • cause extra error of our models.

<!-- b000345 | prose | pages [23] -->
Lack necessary data. Lack of data on energy production, we can only use data on • energy consumption to replace them.

<!-- b000346 | prose | pages [23] -->
Simplifying assumption.For convenience of modeling, we neglect the elements • about import and export, which play import roles in economy.

<!-- b000347 | heading | pages [23] -->
References

<!-- b000348 | references | pages [23] -->
[1] Carley S.State renewable energy electricity policies: An empirical evaluation of Ef-

<!-- b000349 | references | pages [23] -->
fectiveness [J]. Energy Policy, 2009, 37(8): 3071–3081.

<!-- b000350 | references | pages [23] -->
[2] Verbruggen A, Fischedick M, Moomaw W,et al. Renewable energy costs, potentials,

<!-- b000351 | references | pages [23] -->
Barriers: Conceptual issues [J]. Energy Policy 2010, 38(2): 850–861.

<!-- b000352 | references | pages [23] -->
[3] Vries B J M D, Vuuren D P V, Hoogwijk M M. Renewable energy sources: Their

<!-- b000353 | references | pages [23] -->
global potential for the first-half of the 21st century at a global level: Anintegrated

<!-- b000354 | references | pages [23] -->
Approach [J]. Energy Policy, 2007, 35(4):2590-2610. [36] Sliz-Szkliniarz B. Assess-

<!-- b000355 | references | pages [23] -->
ment of the renewable energy-mix and land use trade-off at a regional level: A

<!-- b000356 | references | pages [23] -->
case stud for the Kujawsko–Pomorskie Voivodship [J]. Land Use Policy, 2013, 35:

<!-- b000357 | references | pages [23] -->
257–270.

<!-- b000358 | references | pages [23] -->
[4] Al-Badi A H, Malik A, Gastli A. Assessment of renewable energy resources poten-

<!-- b000359 | references | pages [23] -->
tial in Oman and identification of barrier to their significant utilization[J]. Renew-

<!-- b000360 | references | pages [23] -->
able and Sustainable Energy Reviews, 2009, 13(9): 2734–2739.

<!-- b000361 | references | pages [23] -->
[5] Akella A K, Saini R P,Sharma M P.Social, economic and environmental impacts of

<!-- b000362 | references | pages [23] -->
renewable energy systems [J]. Renewable Energy, 2009, 34 (2): 390–396

<!-- b000363 | references | pages [23] -->
[6] Kaygusuz K. Environmental impacts of the solar energy systems [J]. Energy Sources

<!-- b000364 | references | pages [23] -->
Part A:Recovery Utilization and Environmental Effects, 2009, 31: 1366-1376.

<!-- b000365 | references | pages [23] -->
[7] Wee H M, Yang W H, Chou C W, et al. Renewable energy supply chains, perfor-

<!-- b000366 | references | pages [23] -->
mance, application barriers, and strategies for further development [J]. Renewable

<!-- b000367 | references | pages [23] -->
and Sustainable Energy Reviews, 2012, 16 (8): 5451–5465.

<!-- b000368 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000369 | furniture | pages [24] -->
Team # 73767

<!-- b000370 | furniture | pages [24] -->
Page 23 of 28

<!-- b000371 | heading | pages [24] -->
Appendices

<!-- b000372 | heading | pages [24] -->
Appendix A

<!-- b000373 | prose | pages [24, 25] -->
Profiles of Arizona Pic1 Trend graph of TFE and its price Pic2 Trend graph of CRE and itsprice Pic3 Trend graph of totalconsumption(TC) and its price Pic4 Trend graph of the ratio of TFE to TC and CRE to TC

<!-- b000374 | caption | pages [24] -->
Figure 11: Energy profile of Arizona

<!-- b000375 | caption | pages [24] -->
Figure 12: Means of energy consumption in Arizona

<!-- b000376 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000377 | furniture | pages [25] -->
Team # 73767

<!-- b000378 | furniture | pages [25] -->
Page 24 of 28

<!-- b000379 | caption | pages [25] -->
Figure 12 :

<!-- b000381 | caption | pages [25] -->
Figure 13 :

<!-- b000382 | prose | pages [25] -->
F Fuel enthanol C Coal HY Hydroelectricity PE Petroleum products GE Geothermal energy NG Natural gas WE Wind energy OT Other PH&SO Photovoltaic and so- lar thermal energy (Only the unit of "F"is Thausand Barrels)

<!-- b000383 | caption | pages [25] -->
Table 13: the cutline in Figure 2 and Figure 3

<!-- b000384 | caption | pages [25] -->
Figure 13: The constitute of total energy consumption in Arizona in 2009

<!-- b000385 | prose | pages [25] -->
Data from 1960 to 2009 Variable Quantitative Change Rate of Change Energy total production 1116104.735(Billion Btu) 374.35% Renewable energy total production 67311.832(Billion Btu) 186.04% Fossil fuelS, total production 1048792.903(Billion Btu) 400.36% Electricity production 672434.71972(Billion Btu) 2090.35% Wood consumption 6547.67591(Billion Btu) 171.44% Secondary industry consumption 1127324.01293(Billion Btu) 816.29% Renewable energy total end-use expenditures 4885.009(Million dollars) 4728.95% GDP 201016(Million dollars) 6.736912662

<!-- b000386 | caption | pages [25] -->
Table 14: The quantitative change and the rate of change of typical variables

<!-- b000387 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000388 | furniture | pages [26] -->
Team # 73767

<!-- b000389 | furniture | pages [26] -->
Page 25 of 28

<!-- b000390 | heading | pages [26] -->
Appendix B

<!-- b000391 | prose | pages [26] -->
Profile of New Mexico

<!-- b000392 | caption | pages [26] -->
Figure 14: energy profile of New Mexico

<!-- b000393 | caption | pages [26] -->
Figure 15: means of energy consumption in New Mexico

<!-- b000394 | heading | pages [26] -->
Appendix C

<!-- b000395 | prose | pages [26, 27] -->
Profiles of Texas Pic1 Trend graph of TFE and its price Pic2 Trend graph of CRE and itsprice Pic3 Trend graph of totalconsumption(TC) and its price Pic4 Trend graph of the ratio of TFE to TC and CRE to TC

<!-- b000396 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000397 | furniture | pages [27] -->
Team # 73767

<!-- b000398 | furniture | pages [27] -->
Page 26 of 28

<!-- b000399 | caption | pages [27] -->
Figure 15 :

<!-- b000401 | caption | pages [27] -->
Figure 16 :

<!-- b000402 | prose | pages [27] -->
F Fuel enthanol C Coal HY Hydroelectricity PE Petroleum products GE Geothermal energy NG Natural gas WE Wind energy OT Other PH&SO Photovoltaic and so- lar thermal energy (Only the unit of "F"is Thausand Barrels)

<!-- b000403 | caption | pages [27] -->
Table 15: the cutline in Figure 2 and Figure 3

<!-- b000404 | caption | pages [27] -->
Figure 16: the constitute of total energy consumption in New Mexico in 2009

<!-- b000405 | caption | pages [27] -->
Table 16: The quantitative change and the rate of change of typical variables

<!-- b000406 | prose | pages [27] -->
Data from 1960 to 2009 Variables Quantitative Change Rate of Change Energy total production 510310.930(Billion Btu) 156.56% Renewable energy total production 28262.327(Billion Btu) 383.32% Fossil fuelS, total production 482048.602(Billion Btu) 151.32% Electricity production 16995.11376(Billion Btu) 2279.84% Wood consumption 4244.64258(Billion Btu) 64.04% Secondary industry consumption 414753.41587(Billion Btu) 199.64% Renewable energy total end-use expenditures 750.173(Million dollars) 873.31% GDP 59090(Million dollars) 593.15%

<!-- b000407 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000408 | furniture | pages [28] -->
Team # 73767

<!-- b000409 | furniture | pages [28] -->
Page 27 of 28

<!-- b000410 | caption | pages [28] -->
Figure 17: Energy profile of Texas

<!-- b000411 | caption | pages [28] -->
Figure 18: Means of energy consumption in Texas

<!-- b000412 | furniture | pages [29] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000413 | furniture | pages [29] -->
Team # 73767

<!-- b000414 | furniture | pages [29] -->
Page 28 of 28

<!-- b000415 | caption | pages [29] -->
Figure 18 :

<!-- b000416 | prose | pages [29] -->
Pic1 Trend graph of TFE and its price Pic2 Trend graph of CRE and itsprice Pic3 Trend graph of totalconsumption(TC) and its price Pic4 Trend graph of the ratio of TFE to TC and CRE to TC

<!-- b000417 | caption | pages [29] -->
Figure 19 :

<!-- b000418 | prose | pages [29] -->
F Fuel enthanol C Coal HY Hydroelectricity PE Petroleum products GE Geothermal energy NG Natural gas WE Wind energy OT Other PH&SO Photovoltaic and so- lar thermal energy (Only the unit of "F"is Thausand Barrels)

<!-- b000419 | caption | pages [29] -->
Table 17: the cutline in Figure 2 and Figure 3

<!-- b000420 | caption | pages [29] -->
Figure 19: The constitute of total energy consumption in Texas in 2009

<!-- b000421 | prose | pages [29] -->
Variable Quantitative Change Rate of Change Energy total production 6319816.106(Billion Btu) 142.26% Renewable energy total production 306479.838(Billion Btu) 611.07% Fossil fuelS, total production 6013336.268(Billion Btu) 136.90% Electricity production 1061765.94759(Billion Btu) 8953.51% Wood consumption 23236.12241(Billion Btu) 60.67% Secondary industry consumption 5556015.3619(Billion Btu) 158.61% Renewable energy total end-use expenditures 24323.858(Million dollars) 5688.46% GDP 876004(Million dollars) 460.01%

<!-- b000422 | caption | pages [29] -->
Table 18: The quantitative change and the rate of change of typical variables
