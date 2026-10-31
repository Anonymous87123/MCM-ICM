# P-C-2019-1922154-b7129095

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
1922154

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only T1 _______________ F1 _______________ T2 _______________ F2 _______________ T3 _______________ F3 _______________ T4 _______________ Problem Chosen F4 _______________

<!-- b000004 | front_matter | pages [1] -->
C

<!-- b000005 | prose | pages [1] -->
2019 MCM/ICM

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | prose | pages [1] -->
The Current Status, Future and Strategy of Opioid

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
The United States is experiencing a crisis regarding the abuse of opioids which poses a great threat to the development prospects of the United States. Based on the idea of cellular automata, we not only describe the spread and characteristics of reported synthetic opioid and heroin cases in Ohio, Kentucky, West Virginia, Virginia, and Pennsylvania, but also develop a possible strategy countering the opioid crisis.

<!-- b000010 | prose | pages [1] -->
We define a county and the nearest k counties around it as an “environment”. Based on the idea of KNN, we determine the m “environments” that are most similar to the “environment” of the county, and then use the cellular automata to predict the number of cases in the county next year with the growth rate of m “environments”. At the same time, we define the opioid incidents concentration index (CI) to characterize the degree of aggregation of cases by reference to the HHI index. Finally, we obtain the distribution of synthetic opioids and heroin incidents in five states. Cases are still concentrated in transportation hubs and there is a tendency to spread. Heroin spread to the southwest in Kentucky with Lexington as the center and has a tendency to spread throughout Pennsylvania and Virginia. Based on historical data and prediction, we determine the drug identification threshold levels for each state. In 2026, Ohio will reach its threshold of 120,000, making it difficult for the government to control the amount of opioid use and the speed of spread.

<!-- b000011 | prose | pages [1] -->
In order to determine whether certain socio-economic factors have a significant impact on the trend of opioid usage, we select the first 25% and the last 25% of the data for all state cases in 2010-2016 for analysis of variance if the data passes the test of variance homogeneity. Correlation analysis is performed on data that do not pass the test for variance homogeneity to determine the correlation between socio-economic factors and trends in opioids usage. The final selection of significant factors is marital status, educational attainment, ancestry, and language spoken at home. Adding the important factors selected above to the “environment” similarity considerations, we have obtained a modified model that considers socio-economic factors.

<!-- b000012 | prose | pages [1] -->
Based on the above analysis, we develop a strategy contains two actions for dealing with opioid crisis. The first one is giving couples a discount on tax and mortgage rates to encourage people to marry at legal age. The other is opening a low-cost English language training institution to improve the English proficiency of non-native English speakers.

<!-- b000013 | keywords | pages [1] -->
Key words: Opioid; Cellular automata; Concentration index; Spread; Characteristics

<!-- b000014 | heading | pages [2] -->
MEMO

<!-- b000015 | prose | pages [2] -->
From: Team # 1922154 To: Chief Administrator Data: January 27, 2019 Subject: How to deal with the opioid crisis Dear chief administrator, we are honored to inform you our achievement after performing data analysis and modeling.

<!-- b000016 | prose | pages [2] -->
First, we introduce the spread and characteristics of synthetic opioid and heroin usage between the five states and their counties from 2010 to 2017. Combining the provided data with the collected latitude and longitude data, we notice that the aggregation point of opioid incidents is mainly in the areas with developed traffic, and there is a tendency to spread around. The distribution of synthetic opioid in Virginia is the most extensive, moreover, the distribution in Pennsylvania is the most concentrated. Heroin once had a tendency to spread. However, perhaps for some reason, this trend has been arrested. Nowadays Heroin is spreading again in some states, such as Virginia.

<!-- b000017 | prose | pages [2] -->
Then, we forecast the synthetic opioid and heroin usage in each county from 2017 to 2026. According to the prediction, synthetic opioids will spread throughout Kentucky in the future. And the synthetic opioids usage of counties around Washington is growing from the forecasting.

<!-- b000018 | prose | pages [2] -->
Based on our observation on provided data and Calculated data, we think about the U.S. government is concern about two points:

<!-- b000019 | prose | pages [2] -->
 The opioid usage should be restricted to a certain level.

<!-- b000020 | prose | pages [2] -->
 The spread of the opioid should be controlled within a certain range.

<!-- b000021 | prose | pages [2] -->
According to the historical data and prediction, we can identify the drug identification threshold levels to predict when and where the government’s concern will occur. For example, the threshold level of Ohio is 120,000. government’s concern has occurred in Ohio in 2026.

<!-- b000022 | prose | pages [2] -->
By analyzing the Census socio-economic data, we notice that some important variables such as marital status, educational attainment, ancestry and the language spoken will impact on the use of the opioid in each county.

<!-- b000023 | prose | pages [2] -->
Based on the above analysis, we propose a strategy that includes two actions.

<!-- b000024 | prose | pages [2] -->
 Give couples a discount on tax and mortgage rates to encourage people to marry at legal age.

<!-- b000025 | prose | pages [2] -->
 Open a low-cost English language training institution to improve the English proficiency of non-native English speakers.

<!-- b000026 | prose | pages [2] -->
Our strategy can effectively reduce opioid use.

<!-- b000027 | prose | pages [2] -->
 By taking the action 1, the opioid cases will reduce from 257496 to 231073  By taking the action 2, the opioid cases will reduce from 257496 to 225873.

<!-- b000028 | prose | pages [2] -->
The above is the summary of our study. We sincerely hope that it will provide you with useful information.

<!-- b000029 | prose | pages [2] -->
Thanks!

<!-- b000030 | heading | pages [3] -->
Contents

<!-- b000031 | contents | pages [3] -->
1 Introduction ................................................................................................................... 1

<!-- b000032 | contents | pages [3] -->
1.1 Background ......................................................................................................... 1

<!-- b000033 | contents | pages [3] -->
1.2 Planned Approach ............................................................................................... 1

<!-- b000034 | contents | pages [3] -->
2 Terminology, Symbols and Assumptions ...................................................................... 2

<!-- b000035 | contents | pages [3] -->
2.1 Terms .................................................................................................................. 2

<!-- b000036 | contents | pages [3] -->
2.2 Symbols .............................................................................................................. 2

<!-- b000037 | contents | pages [3] -->
2.3 General Assumptions .......................................................................................... 3

<!-- b000038 | contents | pages [3] -->
3 Spread and Characteristics of Opioid Incidents ............................................................ 3

<!-- b000039 | contents | pages [3] -->
3.1 Preprocess Data .................................................................................................. 3

<!-- b000040 | contents | pages [3] -->
3.1.1 Missing value processing ........................................................................ 3

<!-- b000041 | contents | pages [3] -->
3.1.2 Geographic coordinate acquisition .......................................................... 4

<!-- b000042 | contents | pages [3] -->
3.1.3 Overview of drug cases distribution ........................................................ 4

<!-- b000043 | contents | pages [3] -->
3.2 Spread of Opioid Incidents base on CA Model .................................................. 4

<!-- b000044 | contents | pages [3] -->
3.2.1 Introduction to the idea of method .......................................................... 4

<!-- b000045 | contents | pages [3] -->
3.2.2 Attributes of a Cell ................................................................................... 5

<!-- b000046 | contents | pages [3] -->
3.2.3 Self-defined Rules ................................................................................... 5

<!-- b000047 | contents | pages [3] -->
3.2.4 Concentration index (CI) ......................................................................... 7

<!-- b000048 | contents | pages [3] -->
3.3 Results & analysis .............................................................................................. 7

<!-- b000049 | contents | pages [3] -->
3.3.1 Spread and Characteristics....................................................................... 7

<!-- b000050 | contents | pages [3] -->
3.3.2 Concern and Occur .................................................................................. 9

<!-- b000051 | contents | pages [3] -->
3.4 Sensitivity analysis of model ............................................................................ 10

<!-- b000052 | contents | pages [3] -->
4 Model Modification Considering Socio-economic Factors.......................................... 11

<!-- b000053 | contents | pages [3] -->
4.1 Preprocess Data ................................................................................................. 11

<!-- b000054 | contents | pages [3] -->
4.1.1 Data overview ......................................................................................... 11

<!-- b000055 | contents | pages [3] -->
4.1.2 Data selection & Analysis ..................................................................... 12

<!-- b000056 | contents | pages [3] -->
4.2 Important factor selection ................................................................................. 12

<!-- b000057 | contents | pages [3] -->
4.2.1 The general idea of factors selection ..................................................... 12

<!-- b000058 | contents | pages [3] -->
4.2.2 Grouping ................................................................................................ 12

<!-- b000059 | contents | pages [3] -->
4.2.3 Twofold filter ......................................................................................... 13

<!-- b000060 | contents | pages [3] -->
4.3 Model Modification .......................................................................................... 14

<!-- b000061 | contents | pages [3] -->
4.4 Results & analysis ............................................................................................ 14

<!-- b000062 | contents | pages [3] -->
4.5 Model Evaluation ............................................................................................. 16

<!-- b000063 | contents | pages [3] -->
4.6 Strategy ............................................................................................................. 17

<!-- b000064 | contents | pages [3] -->
4.6.1 Principles of strategy ............................................................................. 17

<!-- b000065 | contents | pages [3] -->
4.6.2 Action .................................................................................................... 17

<!-- b000066 | contents | pages [3] -->
5 Strength and Weakness ................................................................................................ 18

<!-- b000067 | contents | pages [3] -->
5.1 Strength ............................................................................................................. 18

<!-- b000068 | contents | pages [3] -->
5.2 Weakness .......................................................................................................... 18

<!-- b000069 | contents | pages [3] -->
6 Conclusion ................................................................................................................... 18

<!-- b000070 | contents | pages [3] -->
7 References ................................................................................................................... 19

<!-- b000071 | contents | pages [3] -->
Appendix ........................................................................................................................ 20

<!-- b000072 | furniture | pages [4] -->
Team # 1922154                                               Page 1 of 20

<!-- b000073 | heading | pages [4] -->
1 Introduction

<!-- b000074 | heading | pages [4] -->
1.1 Background

<!-- b000075 | prose | pages [4] -->
At present, the phenomenon of addiction and abuse of opioids in the United States is serious. The abuse of opioids not only imposes a heavy economic burden on the US government, but also affects the quantity and quality of the US workforce and the prospects for the US economy.

<!-- b000076 | prose | pages [4] -->
The DEA/National Forensic Laboratory Information System (NFLIS) of the Drug Enforcement Administration’s (DEA) Office publishes an annual report on drug identification results and associated information from drug cases. Specifically, they need:

<!-- b000077 | prose | pages [4] -->
 a description of the spread and characteristics of synthetic opioids and heroin events reported between five states and their counties over time and identify possible locations where specific opioids may have begun to be used in five states.

<!-- b000078 | prose | pages [4] -->
 an analysis of important factors affecting the use or use of opioids in socio- economic data from the US Census.

<!-- b000079 | prose | pages [4] -->
 a possible strategy for countering the opioid crisis.

<!-- b000080 | prose | pages [4] -->
A large amount of literature tracks the abuse of opioids in the United States: for example, Cicero, Inciardi, and Muñoz [1] specifically described the trend of abuse of opioids in the United States from 2002 to 2004 based on the Researched Abuse, Diversion and Addiction-Related Surveillance (RADARS®) system; Volkow, Jones, Einstein, and Wargo [2] analyzed the factors that triggered the opioid crisis and its further evolution, as well as interventions to manage and prevent opioid use disorders.

<!-- b000081 | prose | pages [4] -->
However, most of the literature does not scientifically summarize its propagation patterns and distribution characteristics over time based on the data of the opioid drug identification cases in various counties, so that the future predictions cannot accurately indicate the time and place where a drug identification may be transmitted. In addition, past work has not been able to propose effective strategies to deal with the opioid crisis.

<!-- b000082 | heading | pages [4] -->
1.2 Planned Approach

<!-- b000083 | prose | pages [4] -->
Based on the above analysis, we propose the framework model shown in Figure 1, which can be summarized as the following steps:  Characteristics and Spread Draw heat maps and other visualizations using NFLIS data and geographic data (latitude and longitude), and analyze the spread and characteristics of the reported synthetic opioid and heroin incidents in and between the five states and their counties over time. 

<!-- b000084 | heading | pages [4] -->
Cellular Automata Model

<!-- b000085 | prose | pages [4] -->
With the idea of cellular automata which is the state of the next moment is determined by the surrounding and its own state, a new cellular automata model is constructed by combining the ideas of clustering and KNN. This model will fully exploit the information of historical data to achieve a more accurate simulation.

<!-- b000086 | furniture | pages [5] -->
Team # 1922154                                                        Page 2 of 20

<!-- b000087 | prose | pages [5] -->
 Analyze Socio-economic Factors We plan to use statistical one-way ANOVA and correlation analysis to find socioeconomic factors that have a significant impact on the model and to correct the model.  Identify a Possible Strategies We will consider the results of the cellular automata model and the influential socio- economic factors of the analysis, and then develop a possible strategy for countering the opioid crisis. The model will also be used to verify the effectiveness of the strategy.

<!-- b000088 | caption | pages [5] -->
Figure 1: Model framework

<!-- b000089 | heading | pages [5] -->
2 Terminology, Symbols and Assumptions

<!-- b000090 | heading | pages [5] -->
2.1 Terms

<!-- b000091 | prose | pages [5] -->
 Opioids[3]: medically they are primarily used for pain relief, including anesthesia and they are also frequently used non-medically for their euphoric effects or to prevent withdrawal.

<!-- b000092 | prose | pages [5] -->
 Heroin[4]: an opioid most commonly used as a recreational drug for its euphoric effects. It is generally illegal to make, possess, or sell heroin without a license.

<!-- b000093 | prose | pages [5] -->
 HHI[5]: the Herfindahl-Hirschman index is a statistical measure of concentration.

<!-- b000094 | prose | pages [5] -->
For example, it can be used to measure the market concentration. It is calculated by squaring the market shares of all firms in a market and then summing the squares.

<!-- b000095 | heading | pages [5] -->
2.2 Symbols

<!-- b000096 | caption | pages [5] -->
Table 1: Variable description

<!-- b000097 | heading | pages [5] -->
Symbol

<!-- b000098 | prose | pages [5] -->
Definition The ith county 𝐶𝑖

<!-- b000099 | prose | pages [5] -->
𝐶𝑖𝑛⃗⃗⃗⃗⃗ The environment(vector) related to ith county in the nth year

<!-- b000100 | prose | pages [5, 6] -->
The growth rate of opioid usage in the ith county in the nth year 𝑛 𝑟𝑖 𝑦 The error in 𝑦𝑡ℎ year when the value of parameters are k and m 𝑅𝑀𝑆𝐸(𝑘,𝑚)

<!-- b000101 | furniture | pages [6] -->
Team # 1922154                                                        Page 3 of 20

<!-- b000103 | prose | pages [6] -->
The concentration index CI Marital status MS Educational attainment EA Ancestry AN Language spoken at home LS

<!-- b000104 | heading | pages [6] -->
2.3 General Assumptions

<!-- b000105 | prose | pages [6] -->
 Assumption 1: The change in the number of a county opioid incidents is greatly affected by the surrounding counties, and the historical data can reflect the development of opioids to a certain extent.

<!-- b000106 | prose | pages [6] -->
Reason: This assumption was made to ensure the validity of the cellular automata model we constructed.

<!-- b000107 | prose | pages [6] -->
 Assumption 2: The government will not have excessive rectification of opioids from now until 2026, and the changes in the opioids of each county will follow the historical law of 2010-2017.

<!-- b000108 | prose | pages [6] -->
Reason: The reason for this assumption is to ensure the validity of the results predicted by the model to some extent.

<!-- b000109 | prose | pages [6] -->
 Assumption 3: The data used in this paper is realistic and accurate to a certain degree.

<!-- b000110 | prose | pages [6] -->
Reason: Although the data is incomplete and there are some tolerable errors in the statistics, we make this assumption to ensure an effective solution.

<!-- b000111 | prose | pages [6] -->
 Assumption 4: Counties, which are not involved in NFLIS Data is not considered in our model.

<!-- b000112 | prose | pages [6] -->
Reason: We believe the counties not involved in NFLIS Data are of little significance to the problem studied

<!-- b000113 | heading | pages [6] -->
3 Spread and Characteristics of Opioid Incidents

<!-- b000114 | heading | pages [6] -->
3.1 Preprocess Data

<!-- b000115 | heading | pages [6] -->
3.1.1 Missing value processing

<!-- b000116 | prose | pages [6] -->
The first file (MCM_NFLIS_Data.xlsx) contains most of the county’s drug identification counts in year 2010-2017, but some counties still have missing data for a certain year or even years. We suspect that the county has a drug identification count in the absence of these years, but the name of the drug identified cannot be determined. Therefore, we fill in the missing value of variable County total count of all substances identified as follows:

<!-- b000117 | furniture | pages [7] -->
Team # 1922154                                                        Page 4 of 20

<!-- b000118 | prose | pages [7] -->
𝑋𝑖= 𝑋𝑖−1 + 𝑋𝑖+1 (1) 2 where 𝑋𝑖 indicates the missing total count of all substances identified in the county in the ith year, 𝑋𝑖−1 indicates the total count of all substances identified in the previous year, 𝑋𝑖+1 indicates the total count of all substances identified in the following year.

<!-- b000119 | prose | pages [7] -->
Notes: If the county has more than three missing data, we believe that the county data is invalid. We give up filling in missing values and abandon them.

<!-- b000120 | heading | pages [7] -->
3.1.2 Geographic coordinate acquisition

<!-- b000121 | prose | pages [7] -->
In order to see the geographical distribution of the submitted cases, we obtained five states: the latitude and longitude data of all counties in Ohio, Kentucky, West Virginia, Virginia, and Pennsylvania from the United States Cities Database website [6]. And then we calculate the distance between each county using the Haversine formula [7]. Suppose the latitude and longitude of the two counties are (𝜑1, 𝜆1) and (𝜑2, 𝜆2), respectively.

<!-- b000122 | prose | pages [7] -->
𝑑= 2𝑟· 𝑎𝑟𝑐𝑠𝑖𝑛 (√𝑠𝑖𝑛2 (𝜑2 −𝜑1 ) + 𝑐𝑜𝑠𝜑1 · 𝑐𝑜𝑠𝜑2 · 𝑠𝑖𝑛2 (𝜆2 −𝜆1 ))     (2) 2 2

<!-- b000123 | prose | pages [7] -->
where d is the distance between the two counties, r is the radius of the earth.

<!-- b000124 | heading | pages [7] -->
3.1.3 Overview of drug cases distribution

<!-- b000125 | prose | pages [7] -->
We draw heat maps using the latitude and longitude data of each state and the data of drug identification counts for narcotic analgesics (synthetic opioids) and heroin in each of the five states, to have a general understanding of the distribution of reported cases.

<!-- b000126 | prose | pages [7] -->
Take the case reported in 2010 as an example (shown in Figure 2). It can be roughly seen from the heat map that the proportion in the transportation hubs and along the lake and coastal areas is high.

<!-- b000127 | caption | pages [7] -->
Figure 2: Distribution of drug identification cases in 2010

<!-- b000128 | heading | pages [7] -->
3.2 Spread of Opioid Incidents base on CA Model

<!-- b000129 | heading | pages [7] -->
3.2.1 Introduction to the idea of method

<!-- b000130 | prose | pages [7, 8] -->
To help us understand the spread of opioid usage between the five states and their counties in the past, we propose a model to simulate the use of opioids over the past eight years in various regions. The simulation results of the model are then used to identify any possible locations in five states that may have begun to use a specific opioid.

<!-- b000131 | furniture | pages [8] -->
Team # 1922154                                                        Page 5 of 20

<!-- b000133 | prose | pages [8] -->
Based on the analysis of the problem and data, we summarize the following challenges:

<!-- b000134 | prose | pages [8] -->
 The model should be able to reflect the interaction between the use of opioid each county.

<!-- b000135 | prose | pages [8] -->
 The model should be able to reflect the impact of the historical development of each county on its future.

<!-- b000136 | prose | pages [8] -->
 Models must be able to simulate changes in the number of opioid cases in all counties.

<!-- b000137 | prose | pages [8] -->
In view of these challenges, we adopt the Cellular Automata [8] (CA), a grid dynamics model, in which time, space, and state are all discrete and have the ability to simulate the evolution process of complex systems. Cellular Automata is a widely used model to analyze the spread problems [9]. In this case, the map is divided into cells, and each county occupies a separate cell. A cell records the total drug reports of the county. The state of the cell update based on its current state and the current state of the surrounding cells. We apply the self-defined update rules to simulate the evolution of each county’s opioid usage in our model.

<!-- b000138 | heading | pages [8] -->
3.2.2 Attributes of a Cell

<!-- b000139 | prose | pages [8] -->
In our model, each cell can only represent at most one county. A cell has 3 attributes:

<!-- b000140 | prose | pages [8] -->
 An integer c (0 or 1) to represent the cell status, 0 for no county, 1 for one county  Current number of opioid cases in the county 𝐶𝑖.

<!-- b000141 | prose | pages [8] -->
 The rate of change in the number of opioid cases in the county that year 𝑟𝑖 The other two properties only make sense when c is non-zero. In each step of the simulation, 𝐶𝑖 is updated by the 𝑟𝑖. Self-defined rules are introduced in following sections.

<!-- b000142 | heading | pages [8] -->
3.2.3 Self-defined Rules

<!-- b000143 | prose | pages [8] -->
The key to the cellular automata that can be used to describe the use of opioids in each county is to develop rules that are close to reality. In this case, we develop update rules based on given historical data.

<!-- b000144 | prose | pages [8] -->
First we calculate the distance between them by the latitude and longitude of each county. Then we take each county and its nearest 𝑘 counties as a set of vectors what we called “environment ” based on the idea of cluster. The mathematical expression for each set of vectors is as follows:

<!-- b000145 | prose | pages [8] -->
𝐶𝑖𝑛⃗⃗⃗⃗⃗ = (𝑟𝑖 𝑛, 𝐶𝑖 𝑛(0), 𝐶𝑖 𝑛(1), 𝐶𝑖 𝑛(2), 𝐶𝑖 𝑛(3),···, 𝐶𝑖 𝑛(𝑘))

<!-- b000146 | prose | pages [8] -->
where 𝐶𝑖𝑛⃗⃗⃗⃗⃗  is the environment(vector) related to ith county in the nth year, 𝑟𝑖 𝑛 is the

<!-- b000147 | prose | pages [8] -->
growth rate of opioid usage in the ith county in the nth year (growth rate can be negative).

<!-- b000148 | prose | pages [8] -->
𝑛(0) is the opioid usage of itself 𝐶𝑖 𝑛(1) represents the opioid usage of the county with 𝐶𝑖 the shortest distance from ith county in the nth year. A set of vectors can be generated based on the annual data of each county.

<!-- b000149 | furniture | pages [9] -->
Team # 1922154                                                        Page 6 of 20

<!-- b000150 | prose | pages [9] -->
So we have 3003 groups environment(vector). We believe that the growth in the number of opioid cases in a county is determinable. It can be found similar environment to determine the growth rate of the county’s opioid cases in historical data. Before we look for the similar environment, we’re going to do something with environment(vector).

<!-- b000151 | prose | pages [9] -->
𝑛(1), 𝐶𝑖 𝑛(2), 𝐶𝑖 𝑛(3),···, 𝐶𝑖 𝑛(𝑘) in ascending order. If we do not make ascending We sort 𝐶𝑖 𝑛(𝑘) , we will amplify the error. For example, we think order ranking to the 𝐶𝑖 𝑛, 1,2,3,4,5)  should equal to the (𝑟𝑗 𝑛, 1,5,4,3,2,1) . But when we calculate the (𝑟𝑖

<!-- b000152 | prose | pages [9] -->
Euclidean distance between them, the result shows that they are different.

<!-- b000153 | prose | pages [9] -->
We can calculate the Euclidean distance between each environment(vector) 𝐶𝑖𝑛⃗⃗⃗⃗⃗ . The

<!-- b000154 | prose | pages [9] -->
Euclidean distance calculation formula is as follows:

<!-- b000155 | prose | pages [9] -->
𝑘 2 𝑛−𝐶𝑗 𝑛) (3) 𝑑𝑖𝑗= √∑(𝐶𝑖 𝑖=0,𝑗=0

<!-- b000156 | prose | pages [9] -->
Based on the idea of KNN, we use the formula to find the m vectors closest to 𝐶𝑖𝑛⃗⃗⃗⃗⃗ .

<!-- b000157 | prose | pages [9] -->
𝑛 in the m vectors, we can determine the annual growth rate of the number Based on the 𝑟𝑖 of opioid cases in 𝑖 county in 2010 by inverse distance weighting calculation. The inverse distance weighting formula is as follows:

<!-- b000158 | prose | pages [9] -->
1 𝑑𝑖𝑗 (4) 𝑤𝑗= 1 𝑚 ∑ 𝑗=1 𝑑𝑖𝑗 where 𝑤𝑗 is the weight of each vector’s influence on the growth rate in 𝑖 county.

<!-- b000159 | caption | pages [9] -->
Figure 3: Updating Rule

<!-- b000160 | caption | pages [9] -->
Figure 3 shows how the rule works in practice. The points indicate counties, and the

<!-- b000161 | prose | pages [9] -->
colors of the point indicate different values. In this case, we choose k=3 and m=3. So we

<!-- b000162 | prose | pages [9, 10] -->
can find environment 𝐴𝑛⃗⃗⃗⃗⃗ = [𝑟𝐴 𝑛, 4,1,5,6]. From the historical data, the three most similar historical environments are 𝐵𝑛⃗⃗⃗⃗⃗ = [𝑟𝐵 𝑛𝑏, 4,1,5,6], 𝐶𝑛⃗⃗⃗⃗⃗ = [𝑟𝐶 𝑛𝑐, 4,2,5,6],

<!-- b000163 | furniture | pages [10] -->
Team # 1922154                                                        Page 7 of 20

<!-- b000165 | prose | pages [10] -->
𝐷𝑛⃗⃗⃗⃗⃗ = [𝑟𝐷 𝑛𝑑, 3,1,5,6] . Then we can calculate the Euclidean distance between each

<!-- b000166 | prose | pages [10] -->
environment.

<!-- b000167 | prose | pages [10] -->
Finally, we can determine the growth rate 𝑟𝑖 of the county in the current year to calculate the number of specific opioid cases in the next year. The formula for calculating the growth rate is as follows:

<!-- b000168 | prose | pages [10] -->
𝑚 𝑛 (5) 𝑟𝑖= ∑𝑤𝑗𝑟𝑗 𝑗=1 Through the above method, we can determine the evolution rules of each cell in the cellular automata.

<!-- b000169 | heading | pages [10] -->
3.2.4 Concentration index (CI)

<!-- b000170 | prose | pages [10] -->
In economics, the industrial concentration is generally measured by the Hirschman index [5] which is not affected by the number and size of the company. It can better measure the changes in the concentration of the industry. Here we want to portray the concentration of opioids, so we define the opioid incidents concentration index (CI) by reference to the HHI index.

<!-- b000171 | prose | pages [10] -->
At first, we determined to take the state as the research unit. The general idea is to select all counties in the certain state as a whole to calculate the CI to represent the concentration of drug identification cases in the certain state. The formula is as follows:

<!-- b000172 | prose | pages [10] -->
𝑘 2 𝐶𝑖 (7) CI = ∑( ) 𝑘 ∑ 𝐶𝑖 𝑖=1 𝑖=1 where 𝐶𝑖 is the drug identification count in the ith county, 𝑘 is the number of counties in a state.

<!-- b000173 | heading | pages [10] -->
3.3 Results & analysis

<!-- b000174 | prose | pages [10] -->
In section 3.3.1. We will draw conclusions of spread and characteristics of the reported synthetic opioid and heroin incidents by analyzing the result of the model to at first. We then consider heroin as a specific opioid, we will use our model to find any possible county where heroin use in five states.

<!-- b000175 | prose | pages [10] -->
In section 3.3.2. We will talk about the government’s specific concerns. And then we will find the threshold levels to determine when and where the government’s concerns will occur in the future by using our model to predict the change of opioid usage.

<!-- b000176 | heading | pages [10] -->
3.3.1 Spread and Characteristics

<!-- b000177 | prose | pages [10] -->
To help us have a good grasp of opioid usage, identifying the way of opioid spread is very important. We have already built CA model and have defined our rule to change the status of cell. Based on the historical data, we use our model to predict the spread of opioids from 2017 to 2026.

<!-- b000178 | prose | pages [10, 11] -->
 Spread The result of synthetic opioid and heroin spread in the future is solved by the CA model. The spread of synthetic opioid in 2017 and 2020 are shown in Figure 4:

<!-- b000179 | furniture | pages [11] -->
Team # 1922154                                                        Page 8 of 20

<!-- b000181 | caption | pages [11] -->
Figure 4 (a) 2017 synthetic opioid

<!-- b000182 | caption | pages [11] -->
Figure 4 (b) 2020 synthetic opioid

<!-- b000183 | prose | pages [11] -->
By comparing Figure 3(a) and Figure 3(b), We find that some areas have begun to form new aggregation points. At the same time, some of the old aggregation points are transferred or disappeared. The aggregation point is still mainly in the areas with developed traffic, and there is a tendency to spread around. According to the prediction, synthetic opioids will spread throughout Kentucky in the future. And the synthetic opioids usage of counties around Washington is growing from the forecasting.

<!-- b000184 | prose | pages [11] -->
The spread results of heroin in 2017 and 2020 are shown in Figure 5.

<!-- b000185 | caption | pages [11] -->
Figure 5 (a) Heroin opioid in 2017         Figure 5 (b) Heroin opioid in 2020

<!-- b000186 | prose | pages [11] -->
By comparing Figure 5(a) and Figure 5(b), we find that heroin spread to the southwest in Kentucky with Lexington as the center according to the prediction. Based on the forecasting, it can be seen that the aggregation points gradually disappear in the Ohio. That's probably because Ohio is starting to crack down on drugs. But in Pennsylvania and Virginia, heroin still has tendency to spread across wide areas of these two states.

<!-- b000187 | prose | pages [11] -->
 Characteristics In order to portray the characteristics of the synthetic opioid and heroin, we calculate the concentration index of them based on the historical data.

<!-- b000188 | prose | pages [11] -->
By calculation, we can obtain the concentration index of the synthetic opioid. The result is shown in Figure 6. We notice that the value of concentration index is periodic. According to the formula of concentration index, we know that the smaller the value, the stronger the degree of diffusion.

<!-- b000189 | furniture | pages [12] -->
Team # 1922154                                                        Page 9 of 20

<!-- b000190 | prose | pages [12] -->
KY OH PA VA WV 0.14 Concentration Index 0.12 0.1 0.08 0.06 0.04 0.02 0

<!-- b000191 | prose | pages [12] -->
Time

<!-- b000192 | caption | pages [12] -->
Figure 6: CI of the synthetic opioid

<!-- b000193 | prose | pages [12] -->
From the Figure 6, we find the distribution of synthetic opioid in Virginia is the most extensive. Moreover, the distribution in Pennsylvania is the most concentrated. From the Figure 5, we can also find the cases of opioid mainly occur in metropolis in Pennsylvania.

<!-- b000194 | prose | pages [12] -->
The result of heroin’s concentration index is shown in Figure 7.

<!-- b000195 | prose | pages [12] -->
KY OH PA VA WV 0.25

<!-- b000196 | prose | pages [12] -->
Concentration Index 0.2

<!-- b000197 | prose | pages [12] -->
0.15

<!-- b000198 | prose | pages [12] -->
0.1

<!-- b000199 | prose | pages [12] -->
0.05

<!-- b000200 | prose | pages [12] -->
0

<!-- b000201 | prose | pages [12] -->
Time

<!-- b000202 | caption | pages [12] -->
Figure 7: Heroin’s concentration index

<!-- b000203 | prose | pages [12] -->
From the Figure 7, we notice that heroin once had a tendency to spread. However, perhaps for some reason, this trend has been arrested. According to the Figure 7, it can be seen that heroin is spreading again in some states, such as Virginia.

<!-- b000204 | heading | pages [12] -->
3.3.2 Concern and Occur

<!-- b000205 | prose | pages [12] -->
Based on our observation on provided data and calculated data, we think about the U.S. government is concern about two aspects:

<!-- b000206 | prose | pages [12] -->
 The opioid usage should be restricted to a certain level.

<!-- b000207 | prose | pages [12] -->
 The spread of the opioid should be controlled within a certain range.

<!-- b000208 | prose | pages [12] -->
When the number of reported cases reaches to a certain level, government will take action to limit its development.

<!-- b000209 | furniture | pages [13] -->
Team # 1922154                                                        Page 10 of 20

<!-- b000210 | caption | pages [13] -->
Figure 8: The use of opioid from 2010 to 2026

<!-- b000211 | prose | pages [13] -->
According to the historical data and prediction, we notice that the reported cases of each state is be limited to a certain. For instance, the reported cases in Ohio is be restricted under the 120000 from 2010 to 2023. Consequently, we can identify the drug identification threshold levels to predict when and where the government’s concern will occur. From the Figure 8, we can determine the threshold level of Ohio is 120,000. But the number of incidents exceed the threshold level of Ohio in 2026 according to the prediction. Then we think the government’s concern has occurred in 2026.

<!-- b000212 | heading | pages [13] -->
3.4 Sensitivity analysis of model

<!-- b000213 | prose | pages [13] -->
Based on a simple analysis, we notice that our model is sensitive to particular parameters. We run the model with different parameter values based on the provided data. Take the 2010 data as the initial state of the model.

<!-- b000214 | prose | pages [13] -->
Then we will analyze how the parameters in our model influences our result. Finally, we will determine the value of the parameter based on the results of the sensitivity analysis.

<!-- b000215 | prose | pages [13] -->
At first, we choose root-mean-square error (RMSE) to evaluate the error between the result of the CA model and the actual value under different parameter values. The formula of RMSE is:

<!-- b000216 | prose | pages [13] -->
2 𝑛 = √∑(𝐶𝑖̂ −𝐶𝑖) 𝑦 𝑖 (8) 𝑅𝑀𝑆𝐸(𝑘,𝑚) 𝑛

<!-- b000217 | prose | pages [13] -->
𝑦 represents the error in 𝑦𝑡ℎ year when the value of parameters are k where 𝑅𝑀𝑆𝐸(𝑘,𝑚)

<!-- b000218 | prose | pages [13] -->
and m, 𝐶𝑖̂ is the estimated value, 𝐶𝑖 is the actual value.

<!-- b000219 | prose | pages [13] -->
In order to evaluate the accuracy of the CA model from a global perspective, we should take RMSE of every year into account. The mathematical expression that is ultimately used to estimate the accuracy of the model is:

<!-- b000220 | prose | pages [13] -->
𝑦 𝑎 ∑ 𝑅𝑀𝑆𝐸(𝑘,𝑚) 𝑦=1 (9) 𝑅𝑀𝑆𝐸(𝑘,𝑚) = 𝑎 Then we can obtain the integrated 𝑅𝑀𝑆𝐸 to depict the accuracy of the model.

<!-- b000221 | furniture | pages [14] -->
Team # 1922154                                                        Page 11 of 20

<!-- b000222 | caption | pages [14] -->
Figure 9: Heat map for RMSE

<!-- b000223 | prose | pages [14] -->
According to the Figure 9, we can find when k is 12 and m is 2, the RMSE is lowest, the value is 104.21. Therefore, we determine the value of k and m. The specific values are shown in Appendix I.

<!-- b000224 | heading | pages [14] -->
4 Model Modification Considering Socio-economic Factors

<!-- b000225 | heading | pages [14] -->
4.1 Preprocess Data

<!-- b000226 | heading | pages [14] -->
4.1.1 Data overview

<!-- b000227 | prose | pages [14] -->
We currently have a common set of socio-economic factors collected for the counties of these five states during each of the years 2010-2016 from the U.S. Census Bureau. Except for the three special identification attributes of “GEO.id”, “GEO.id2” and “GEO.display-label”, the remaining attributes include relationship, marital status, grandparents, educational attainment, ancestors, etc. in each year’s socio-economic factors data set. And each attribute has four values (Estimate、Estimate Margin of Error、 Percent、Percent Margin of Error). The overall data frame is shown in Figure 10.

<!-- b000228 | caption | pages [14] -->
Figure 10: The data frame

<!-- b000229 | furniture | pages [15] -->
Team # 1922154                                                        Page 12 of 20

<!-- b000230 | heading | pages [15] -->
4.1.2 Data selection & Analysis

<!-- b000231 | prose | pages [15] -->
Here we only study the two values of estimate and percent, and do not consider the estimation error temporarily. After selecting the attributes that have a significant impact on the model, the margin of error can be used to measure whether the attribute is valid.

<!-- b000232 | prose | pages [15] -->
In addition, we remove some of the data based on the following considerations:

<!-- b000233 | prose | pages [15] -->
 The attribute that have an '(X)' in the margin of error column We can abandon the attribute directly because an '(X)' means that the estimate is not applicable or not available.

<!-- b000234 | prose | pages [15] -->
 Estimated data (not contain percent) The issue we are considering is the impact of certain important factors in the census socio-economic data on trends in opioid usage. In general, the reason for the increase or decrease in the estimates of certain socio-economic factors is that the overall situation is changing, and the trend of use at this time will also rise or fall with the overall trend. Therefore, we believe that the estimated quantity cannot be an effective factor, while we should pay more attention to the change of its proportional structure.

<!-- b000235 | prose | pages [15] -->
After analyzing the data, we found that the data attributes of 2010-2012 are slightly different from the attributes of 2013-2017. The comparison is shown in the following table:

<!-- b000236 | caption | pages [15] -->
Table 2: Data comparison

<!-- b000237 | prose | pages [15] -->
Year Number of counties Number of attributes Number of attributes studied 2010-2012 464 599 125 2013-2016 463 611 121 Based on the above analysis, we divided the 7-year census socio-economic data into 2010-2011 and 2012-2017 to analyze separately.

<!-- b000238 | heading | pages [15] -->
4.2 Important factor selection

<!-- b000239 | heading | pages [15] -->
4.2.1 The general idea of factors selection

<!-- b000240 | prose | pages [15] -->
Considering that we want to find out the attributes that have a significant impact on the drug cases of each county from a large number of attributes, we believe that it can be grouped according to the number of incident reports.

<!-- b000241 | prose | pages [15] -->
One-way ANOVA is used to analyze the difference of the same attribute between groups, and the attributes are initially screened out. However, the attributes selected do not necessarily have a significant impact on the number of cases. Therefore, we consider using correlation analysis to further screen and determine the final important factors.

<!-- b000242 | heading | pages [15] -->
4.2.2 Grouping

<!-- b000243 | prose | pages [15] -->
In order to discuss the impact of different factors on the trend of opioids’ usage, we can analyze the differences in socio-economic factors in the counties with high and low frequency of opioid use. Therefore, we select two sets of extreme data in order to see the difference more clearly. The specific description is as follows:

<!-- b000244 | caption | pages [15] -->
Table 3: Total drug reports in all counties

<!-- b000245 | prose | pages [15, 16] -->
Index 2010-2012 2013-2017 Mean 501.16 534.45 Std 1717.67 1646.28 Min 0 0 25%(Q1) 59 51 50%(Q2) 151 160 75%(Q3) 387 412 Max 33513 21761 We extract the first 25% (that is 0~25%) as a set of data and the last 25% (that is 75%~100%) as another set of data. Through the analysis of variance, we can analyze the difference between the two sets of data to achieve the purpose of preliminary screening.

<!-- b000246 | furniture | pages [16] -->
Team # 1922154                                                        Page 13 of 20

<!-- b000248 | heading | pages [16] -->
4.2.3 Twofold filter

<!-- b000249 | prose | pages [16] -->
We know that the variance analysis is used to make significant differences between the two groups of sample data, and the sample data needs to satisfy the homogeneity test of variance. If the data does not pass the homogeneity test, the correlation analysis can be used to analyze the correlation.

<!-- b000250 | prose | pages [16] -->
 ANOVA [10] Analysis of variance (ANOVA), also known as "coefficient of variation", was invented by the statistical expert R.A. Fisher for the significance test of the difference between two or more sample means. Its basic idea is to determine the influence of controllable factors on the research results by analyzing the contribution of variation from different sources to the total variation.

<!-- b000251 | prose | pages [16] -->
 Correlation Analysis [11] Correlation analysis refers to the analysis of two or more related variable elements to measure the closeness of the two variable factors. Relevance elements need to have a certain connection or probability before they can be correlated.

<!-- b000252 | prose | pages [16] -->
Through analysis of variance and correlation analysis, we screen for socio-economic factors that have a significant impact on the trends in opioid use, as shown in Table 4:

<!-- b000253 | caption | pages [16] -->
Table 4: Important factors

<!-- b000254 | prose | pages [16] -->
Factor group Explanation Percent; Males 15 years and over - Never married（Mn） Marital status（MS） Percent; Females 15 years and over - Never married（Fn） Educational Percent; Percent bachelor's degree or higher(Ph) attainment(EA) Percent; Arab(Ar) Percent; Greek(Gr) Percent; Irish(Ir) Ancestry(AN) Percent; Italian(It) Percent; Russian(Ru) Percent; Ukrainian(Uk) Language spoken at home Percent; Language other than English - Speak English less (LS) than “very well”(Lo)

<!-- b000255 | furniture | pages [17] -->
Team # 1922154                                                        Page 14 of 20

<!-- b000256 | heading | pages [17] -->
4.3 Model Modification

<!-- b000257 | prose | pages [17] -->
By analyzing the Census socio-economic data, we notice that some variables will impact on the use of the opioid in each county. After the analysis in the previous section, we find the important variables are about the marital status, educational attainment, ancestry and the language spoken. These variables have an impact on the opioid usage. Accordingly, we then add them to the cellular automata model to improve the accuracy of our model. The specific variables are listed in Table 4.

<!-- b000258 | prose | pages [17] -->
In cellular automata model, the basic idea of iterative rules is to rely on a similar environment to determine the current growth rate. Hence, we take MS, EA, AN and LS into environment. However, there is a question we find is the value of the variables is very small. It will lead us to ignore the effects of these new variables in our calculations. In order to solve this problem, we redefined the formula of the variables:

<!-- b000259 | prose | pages [17] -->
𝑀𝑆= 1 𝑀𝑛+ 1 𝐹𝑛                           (10) 𝐸𝐴= 1 𝑃ℎ                                (11) 𝐴𝑁= 1 Ar + 1 𝐺𝑟+ 1 𝐼𝑟+ 1 𝐼𝑡+ 1 𝑅𝑢+ 1 𝑈𝑘          (12)

<!-- b000260 | prose | pages [17] -->
𝐿𝑆= 1 𝐿𝑜                                (13) Then, we add these variables into the environment(vector). The mathematical expression for each set of new vectors is as follows:

<!-- b000261 | prose | pages [17] -->
𝐶𝑖𝑛⃗⃗⃗⃗⃗ = (𝑟𝑖 𝑛, 𝐶𝑖 𝑛(0), 𝑀𝑆𝑖, 𝐸𝐴𝑖, 𝐴𝑁𝑖, 𝐿𝑆𝑖, 𝐶𝑖 𝑛(1), 𝐶𝑖 𝑛(2), 𝐶𝑖 𝑛(3),···, 𝐶𝑖 𝑛(𝑘))

<!-- b000262 | prose | pages [17] -->
where 𝑀𝑆𝑖, 𝐸𝐴𝑖, 𝐴𝑁𝑖, 𝐿𝑆𝑖 is the marital status, educational attainment, ancestry and the language spoken of 𝑖 county.

<!-- b000263 | prose | pages [17] -->
Finally, we followed the update rules explained in section 3.2.3 to complete the iteration of cellular automata.

<!-- b000264 | heading | pages [17] -->
4.4 Results & analysis

<!-- b000265 | prose | pages [17] -->
We use two methods of significance analysis, analysis of variance and correlation analysis, to examine the significant impact of census socio-economic factors on the use of opioids. The data passes the test for variance homogeneity is analyzed by ANOVA, while the other are analyzed by correlation analysis.

<!-- b000266 | prose | pages [17] -->
It is fun that when we try to correlate the factors that passed the variance significance test, the correlation is at a lower level. After careful analysis, we find that the data samples selected by the two methods are inconsistent; we extract the first 25% and the last 25% number of data sets as samples in the analysis of variance, while we use all the samples in the correlation analysis. Therefore, it can be explained that the results obtained by the two methods are different, because these attributes are localized significantly, and when the sample size increases, the significance is weakened.

<!-- b000267 | furniture | pages [18] -->
Team # 1922154                                                        Page 15 of 20

<!-- b000268 | prose | pages [18] -->
We analyze the impact of significant factors on the trend of opioid usage in the following four areas:

<!-- b000269 | prose | pages [18] -->
 Marital status There is a positive correlation between the use of opioids in men and women aged 15 and over who have never been married.

<!-- b000270 | prose | pages [18] -->
The reason for this situation may be that men and women who are currently unmarried are the main opioid users. Because they are still pursuing personal entertainment and enjoyment who lack of family responsibility and social responsibility. There is little motivation to resist opioids, so it is easier to abuse drugs.

<!-- b000271 | prose | pages [18] -->
 Educational attainment In terms of educational attainment, we find that the results are contrary to our perception. Generally, we believe that people with higher degree are more aware of the dangers of the abuse of opioids, so they naturally contradict it.

<!-- b000272 | prose | pages [18] -->
On the contrary, the results show that people with a bachelor’s degree or higher are positively correlated with the usage of opioids. The reason for this may be that the higher the responsibility of those with high educational background, the greater the pressure of study and work. This leads them to seek exciting opioids to stay focused or to relieve stress.

<!-- b000273 | prose | pages [18] -->
 Ancestry People whose ancestors are Arab, Greek, Irish, Italian, Russian, and Ukrainian have significant effects on the use of opioids, and are positively correlated.

<!-- b000274 | prose | pages [18] -->
We suspect that it is due to the mixed population. The local population has a complex source and many unstable factors, which is an excellent environment for illegal trafficking of opioids.

<!-- b000275 | prose | pages [18] -->
 Language spoken at home In the United States, if English is not very good, you can’t communicate well with others. Hence, it's not easy to make friends. Therefore, in the process of dealing with people, it is easy to produce inferiority, and it is often easy to be criticized and addicted to drugs.

<!-- b000276 | prose | pages [18] -->
 Spread The result of synthetic opioid spread in the future is solved by the CA model and the modified CA model. The spread result of synthetic opioid predicted by original and modified model in 2020 are shown in Figure 11.

<!-- b000277 | caption | pages [18] -->
Figure 11 (a) 2020 synthetic opioid original    Figure 11 (b) 2020 synthetic opioid modified

<!-- b000278 | prose | pages [18, 19] -->
By comparing Figure 11(a) and Figure 11(b), the aggregation point is still mainly in the areas with developed traffic, and there is a tendency to spread around. There are more aggregation points appear in the Ohio. It means that we have observed more propagation rules. From the Figure 11(b), we notice the Synthetic opioids usage are more concentrated in Virginia. The spread result of heroin predicted by two model in 2020 are shown in Figure 12:

<!-- b000279 | furniture | pages [19] -->
Team # 1922154                                                        Page 16 of 20

<!-- b000281 | caption | pages [19] -->
Figure 12 (a) 2020 Heroin opioid original       Figure 12 (b) 2020 Heroin opioid modified

<!-- b000282 | prose | pages [19] -->
By comparing Figure 12(a) and Figure 12(b), we find that heroin spread to the southwest in Kentucky predicted by modified model is slower than the original one. Two model have the same prediction of the Heroin spread in the Ohio and Pennsylvania.

<!-- b000283 | prose | pages [19] -->
 Characteristics By calculating relevant formulas, we can obtain the concentration index of the synthetic opioid predicted by the modified model. The result is shown in Figure 13.

<!-- b000284 | prose | pages [19] -->
KY OH PA VA WV 0.14 Concentration Index 0.12 0.1 0.08 0.06 0.04 0.02 0

<!-- b000285 | prose | pages [19] -->
Time

<!-- b000286 | caption | pages [19] -->
Figure 13: CI of the synthetic opioid modified

<!-- b000287 | prose | pages [19] -->
From the Figure 13, we find the distribution of synthetic opioid predicted by the modified model in Virginia is the more concentrated than the original one. They have the same prediction of the Concentration Index in Pennsylvania and Ohio.

<!-- b000288 | heading | pages [19] -->
4.5 Model Evaluation

<!-- b000289 | prose | pages [19] -->
From the modeling process of the cellular automata, we can know that the key to improving the simulation and prediction capabilities of the model is the more effective updating rules. We think simulation results of CA model will be better after we introduce new variables into updating rule.

<!-- b000290 | prose | pages [19] -->
To evaluate whether our model performs better than the unmodified one. We used RMSE as described in section 3.4 to calculate the performance of the modified model. In section 3.4, we know that when k is 12 and m is 2, the average RMSE of the original model is the minimum. Interestingly, k=12 and m=2 are not the optimal combination of the modified model.

<!-- b000291 | furniture | pages [20] -->
Team # 1922154                                                        Page 17 of 20

<!-- b000292 | caption | pages [20] -->
Figure 14: Heat map of modified model

<!-- b000293 | prose | pages [20] -->
According to the Figure 14, it is obvious that when k is 5 and m is 2, the modified model has the smallest average RMSE. The smallest average RMSE is 98.70.

<!-- b000294 | heading | pages [20] -->
4.6 Strategy

<!-- b000295 | heading | pages [20] -->
4.6.1 Principles of strategy

<!-- b000296 | prose | pages [20] -->
 We split the strategy into separate operations, using the control variates approach, and consider only the impact of one action on opioid use;  The effect of the behavior will be directly reflected in the change in the value of the relevant variable;  When the variables change, we select the combination of parameters that have been determined in Section 4.3 to simulate the use of opioid from 2010 to 2017.

<!-- b000297 | prose | pages [20] -->
Based on the above principles, we propose the following 2 actions and quantitatively interpret their promising effects. The simulation data is the simulation result of total reported opioid incidents in 2017. The real data is the total reported opioid incidents in 2017.

<!-- b000298 | heading | pages [20] -->
4.6.2 Action

<!-- b000299 | prose | pages [20] -->
 Action One: Give couples a discount on tax and mortgage rates to encourage people to marry at legal age.

<!-- b000300 | prose | pages [20] -->
This action will influence the marital status(MS). Assume the change rate 𝑟 is 5%, 10%, 15%, 20%. According to the Table 1, we notice that when the 𝑟  is 5%, the simulation result exceed the real data in 2017. We think that might be the cause of the error. When 𝑟 is 10%, 15%, 20%, it is obvious that the simulation data is lower than real data. It means the action one is effective.

<!-- b000301 | caption | pages [20] -->
Table 5: Comparative Results

<!-- b000302 | prose | pages [20, 21] -->
Data 𝑟=5% 𝑟=10% 𝑟=15% 𝑟=20% Actual Data 257496 257496 257496 257496 Simulation Data 263529 238872 243077 231073  Action Two: Open a low-cost English language training institution to improve the English proficiency of non-native English speakers. This action will influence the percent of speak English less than "very well"(Lo). Assume the change rate 𝑟 is -5%, -10%, -15%, -20%. We note from our simulation that when r is -10%, the simulation data exceed the actual data in 2017. When r is at other values, the simulation data is lower than the actual data. It means the action two is effective.

<!-- b000303 | furniture | pages [21] -->
Team # 1922154                                                        Page 18 of 20

<!-- b000305 | caption | pages [21] -->
Table 6: Comparative Results

<!-- b000306 | prose | pages [21] -->
Data 𝑟=-5% 𝑟=-10% 𝑟=15% 𝑟=20% Actual Data 257496 257496 257496 257496 Simulation Data 239705 268312 237580 225873 In all, we can conclude that take action one and action two as our strategy can effectively reduce the number of opioid cases.

<!-- b000307 | heading | pages [21] -->
5 Strength and Weakness

<!-- b000308 | heading | pages [21] -->
5.1 Strength

<!-- b000309 | prose | pages [21] -->
 Based on the idea of cellular automata, we skillfully combine clustering and KNN ideas to innovate the model of this paper.  Our model fully exploits the information of historical data and simulates the changes of opioids in each county from the perspective of historical development.  Although the model based on clustering and KNN is sensitive to k values, we try multiple sets of different k values and choose the smallest k value of RMSE as the model parameter.  Our model is extensible and can add new influence variables in the process of building an 'environment' around itself.  We set goals in strict accordance with the optimization theory.

<!-- b000310 | heading | pages [21] -->
5.2 Weakness

<!-- b000311 | prose | pages [21] -->
 Our model predicts that the error of the results in the past one or two years is small, but the prediction of long-term results will be very large.  The model results may be over-fitted, because the number of real data used to validate the model is too small.  The model only considers the counties discussed in the original data set, but does not consider the spread of the county to the county where there is no abuse of opioids.

<!-- b000312 | heading | pages [21] -->
6 Conclusion

<!-- b000313 | prose | pages [21, 22] -->
In this paper, we first collect latitude and longitude data for each county in five states. After data preprocessing, we analyze the spread and characteristics of the reported synthetic opioid and heroin incidents in and between the five states and their counties over time combined the heat maps and concentration index (CI). Next, based on the idea of cellular automata, we built a cellular automata model based on the idea of clustering and KNN, and evolved the number of cases, and analyzed the error of the model. According to the results of the model simulation, we then analyze where specific opioid use might have started in each of the five states. And then, we use ANOVA and Pearson Correlation Analysis to find some socio-economic factors that have a significant impact on the model, and to modify the model. Moreover, we propose some possible strategies to deal with the opioid crisis, which are verified by our model. Finally, the advantages and disadvantages of the model are discussed.

<!-- b000314 | furniture | pages [22] -->
Team # 1922154                                                        Page 19 of 20

<!-- b000316 | heading | pages [22] -->
7 References

<!-- b000317 | references | pages [22] -->
[1] Cicero, T., Inciardi, J. and Muñoz, A. (2005). Trends in Abuse of OxyContin® and

<!-- b000318 | references | pages [22] -->
Other Opioid Analgesics in the United States: 2002-2004. The Journal of Pain, 6(10),

<!-- b000319 | references | pages [22] -->
pp.662-672.

<!-- b000320 | references | pages [22] -->
[2] Volkow, N., Jones, E., Einstein, E. and Wargo, E. (2018). Prevention and Treatment

<!-- b000321 | references | pages [22] -->
of Opioid Misuse and Addiction. JAMA Psychiatry.

<!-- b000322 | references | pages [22] -->
[3] Opioid. (2019). Retrieved from https://en.wikipedia.org/wiki/Opioid

<!-- b000323 | references | pages [22] -->
[4] Heroin. (2019). Retrieved from https://en.wikipedia.org/wiki/Heroin

<!-- b000324 | references | pages [22] -->
[5] Rhoades, S. A. (1993). The herfindahl-hirschman index. Fed. Res. Bull., 79, 188.

<!-- b000325 | references | pages [22] -->
[6] United States Cities Database. Retrieved from https://simplemaps.com/data/us-

<!-- b000326 | references | pages [22] -->
cities?tdsourcetag=s_pcqq_aiomsg

<!-- b000327 | references | pages [22] -->
[7] Haversine formula. (2019). Retrieved from

<!-- b000328 | references | pages [22] -->
https://en.wikipedia.org/wiki/Haversine_formula

<!-- b000329 | references | pages [22] -->
[8] Yang, J., Su, J., Chen, F., Xie, P., & Ge, Q. (2016). A Local Land Use Competition

<!-- b000330 | references | pages [22] -->
Cellular Automata Model and Its Application. ISPRS International Journal Of Geo-

<!-- b000331 | references | pages [22] -->
Information, 5(7), 106. doi: 10.3390/ijgi5070106

<!-- b000332 | references | pages [22] -->
[9] Pfeifer, B. (2008). A Cellular Automaton Framework for Infectious Disease Spread

<!-- b000333 | references | pages [22] -->
Simulation. The Open Medical Informatics Journal, 2(1), 70-81. doi:

<!-- b000334 | references | pages [22] -->
10.2174/1874431100802010070

<!-- b000335 | references | pages [22] -->
[10] FARAWAY, J. (2002). Practical Regression and Anova using R. [Bath]: [University

<!-- b000336 | references | pages [22] -->
of Bath].

<!-- b000337 | references | pages [22] -->
[11] Knapp, T. (1978). Canonical correlation analysis: A general parametric significance

<!-- b000338 | references | pages [22] -->
testing system. Psychological Bulletin, 85(2), 410-416. doi: 10.1037//0033-

<!-- b000339 | references | pages [22] -->
2909.85.2.410

<!-- b000340 | furniture | pages [23] -->
Team # 1922154                                                        Page 20 of 20

<!-- b000341 | heading | pages [23] -->
Appendix

<!-- b000342 | prose | pages [23] -->
I. RMSE of different combinations of k and m k4m2 k4m3 k4m4 k4m5 k4m6 k5m2 k5m3 k5m4 k5m5 k5m6 k6m2 k6m3 k6m4 2011 0.702974035 0.660225292 0.651338947 0.644141611 0.631348872 0.689582827 0.654907955 0.640512615 0.631348872 0.618291503 0.686194193 0.64954709 0.618291503 2012 6.382522756 6.227991553 6.993836781 7.969931839 9.086992163 4.858846736 7.678869381 7.768503739 8.055460439 9.061818257 6.812678432 6.943830587 7.560941222 2013 34.5552495 43.26408309 51.06440469 66.29665969 73.79199646 35.09461072 103.3068956 58.58633778 67.97781758 72.9797526 95.67006971 42.10246686 54.46951201 2014 118.5778098 133.7225235 173.3128395 205.9417903 231.547958 106.5340157 138.4434617 189.2682819 211.0507622 232.5925888 118.6640475 148.4046161 177.7839959 2015 179.7368771 246.459158 252.3333303 269.5203847 298.9185403 164.9199778 252.9398843 276.0128033 313.1720187 348.1102195 189.2682695 255.2801423 266.0224021 2016 451.2061458 573.3207221 440.7932323 473.3943688 336.5407286 191.3256417 565.5581953 547.2652012 499.3182182 396.6530281 221.4727564 438.9276082 317.7051638 2017 372.7998207 696.3578257 575.1554832 550.9506512 624.6561366 447.7870139 504.9906321 507.5659705 468.3214235 744.0179523 251.1995325 489.1281931 422.8964478 k4m2 k4m3 k4m4 k4m5 k4m6 k5m2 k5m3 k5m4 k5m5 k5m6 k6m2 k6m3 k6m4 mean 166.2801999 242.8589327 214.3292094 224.959704 225.0248144 135.8870985 224.7961209 226.7296587 224.0752928 257.719093 126.253364 197.3480577 178.1509649 std 181.0268378 283.2203141 223.5731777 220.9499227 222.671942 156.8786141 229.1343946 228.3187527 209.9527292 266.6617715 99.72903551 203.4261458 164.82979 k6m5 k6m6 k7m2 k7m3 k7m4 k7m5 k7m6 k8m2 k8m3 k8m4 k8m5 k8m6 2011 0.610704817 0.618291503 0.69295489 0.67936622 0.675926369 0.654907955 0.647750276 0.699650262 0.668993608 0.656685184 0.64954709 0.651338947 2012 8.630325456 9.028703258 4.464049611 5.923561267 7.193463752 8.454182011 9.475769615 5.501218344 6.570223144 7.409909575 8.553819741 9.530468867 2013 71.43347436 92.56316435 27.78748859 42.73791218 54.88778551 78.72786624 86.23140656 45.83951431 90.11657821 92.82732045 107.6172966 116.9397171 2014 194.4008247 206.4638508 81.23659653 160.0603252 190.9938429 230.9795297 251.8435245 144.6112464 219.3248115 233.5453915 247.5924823 260.5668601 2015 444.4392213 335.0241163 149.0443763 231.4022724 261.9961342 326.3630838 359.1618643 192.6916749 299.5087353 312.2190037 360.4894788 367.3190213 2016 494.8957744 423.0661336 404.1983404 420.4118638 327.4526888 395.2867066 431.6021948 552.3179129 490.9140089 389.7772809 677.3048365 625.2052567 2017 616.9209449 545.2829038 909.2514493 376.2977204 549.1471879 533.0649449 625.5960272 465.5550964 616.8661153 522.1177849 604.8729952 604.6975433 k6m5 k6m6 k7m2 k7m3 k7m4 k7m5 k7m6 k8m2 k8m3 k8m4 k8m5 k8m6 mean 261.6187528 230.2924519 225.2393222 176.7875745 198.9067185 224.7901744 252.079791 201.0309019 246.2813523 222.6504823 286.7257795 283.5586009 std 253.9350887 211.5791515 332.8141107 173.4923546 200.0109218 205.2761728 235.5100024 223.2626137 239.0649512 199.2557212 274.4817078 261.4978886

<!-- b000343 | prose | pages [23] -->
k9m2 k9m3 k9m4 k9m5 k9m6 k10m2 k10m3 k10m4 k10m5 k10m6 k11m2 2011 0.684493585 0.686194193 0.689582827 0.656685184 0.656685184 0.702974035 0.682788742 0.674199862 0.658457617 0.656685184 0.69295489 2012 7.120835183 14.1057445 14.0904504 14.20979996 14.54604457 8.450734786 14.08879599 12.28165953 14.34319604 14.52487618 8.444664251 2013 59.07880636 84.64556571 99.20734802 111.3241032 122.6053612 61.89817942 75.34132123 84.18581679 98.70752162 137.9641266 85.14030652 2014 127.0279598 166.5318102 182.0729381 208.7606899 251.9515669 103.818786 159.3326116 181.8095843 211.9986421 243.8577292 128.3012735 2015 174.7381724 234.855488 232.0894852 327.9651895 389.6765379 213.2507143 231.2633289 300.8321249 307.1571809 356.7766207 213.927171 2016 201.8843457 282.6825627 263.3484844 534.9816763 526.850235 179.1816154 239.8553128 315.1385569 660.3541396 648.3914074 575.7651077 2017 757.2435429 558.9201627 338.6156102 622.0920565 572.8990827 450.9889935 500.2835536 511.3414439 626.2145011 691.0289548 498.8250951 k9m2 k9m3 k9m4 k9m5 k9m6 k10m2 k10m3 k10m4 k10m5 k10m6 k11m2 mean 189.6825937 191.7753611 161.4448427 259.9986001 268.4550734 145.4702853 174.4068161 200.8947694 274.2048056 299.0286286 215.870939 std 262.2116446 193.6968913 128.2049746 246.2202988 235.1875612 156.803166 173.0293453 186.6657714 274.2056883 282.2549797 232.2630743

<!-- b000344 | prose | pages [23] -->
k11m3 k11m4 k11m5 k11m6 k12m2 k12m3 k12m4 k12m5 k12m6 2011 0.668993608 0.668993608 0.653125889 0.644141611 0.702974035 0.684493585 0.672468923 0.667249163 0.658457617 2012 7.456790838 8.110829044 9.927710741 10.80781466 3.19564097 4.891837071 6.155900007 6.82344785 8.610585993 2013 68.2665829 79.52509097 129.7653522 145.0459054 31.67462788 60.44919268 74.86483547 83.11639829 107.6360851 2014 196.4820792 184.6359614 207.0583006 240.8498163 83.36576525 169.4449323 200.8082445 226.0490437 255.054727 2015 300.2621271 259.1984282 330.2023749 385.1362336 137.3245437 250.5763008 331.2169656 354.8736011 355.0737538 2016 509.1044035 449.8267136 436.4830278 811.8192583 208.9219191 458.2980677 480.8881546 450.7891992 665.1452319 2017 506.6644407 505.8198681 831.256539 760.9899331 264.3423647 490.0159053 535.5806926 591.6666851 681.5557088 k11m3 k11m4 k11m5 k11m6 k12m2 k12m3 k12m4 k12m5 k12m6 mean 226.9864883 212.5408407 277.906633 336.4704433 104.2182622 204.9086756 232.8838945 244.8550892 296.2477929 std 219.3608208 203.9800991 291.4689724 334.9536692 103.5350184 204.702353 221.4074139 230.0692101 287.340526
