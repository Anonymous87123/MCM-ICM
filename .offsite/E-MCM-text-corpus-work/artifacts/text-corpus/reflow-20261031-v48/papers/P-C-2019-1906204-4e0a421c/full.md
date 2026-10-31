# P-C-2019-1906204-4e0a421c

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
1906204

<!-- b000004 | prose | pages [1] -->
T1 F1

<!-- b000005 | prose | pages [1] -->
T2 F2 Problem Chosen T3 F3

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | prose | pages [1] -->
T4 F4

<!-- b000008 | title | pages [1] -->
2019

<!-- b000009 | prose | pages [1] -->
MCM/ICM

<!-- b000010 | heading | pages [1] -->
Summary Sheet

<!-- b000011 | title | pages [1] -->
Analysis of the opioid crisis and strategies

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
The United States is undergoing an unprecedented opioid crisis. Opioid drugs have been widely used as medicine in a variety of treatments. The fast pace of life and ﬁerce social competition put a lot of pressure on people. People with mental or physical illness will probably be treated with many drugs and they are likely to get addicted to them, especially to opioid drugs. Thus, more and more drug identiﬁcation cases have been conﬁrmed in recent years.

<!-- b000014 | prose | pages [1] -->
The goal of our model is to ﬁnd the spread and characteristics of the reported synthetic opioid and heroin incidents and do possible explanation for current situation and prediction for future case distribution, based on provided data. Speciﬁcally, our model is inspired from "Recommendation System". The ﬁrst step of our model has the similar purpose as "Recommendation System" does that is to ﬁnd similarity and corre- lation between different zones and drugs. It is rough and inaccurate to directly address the data regardless of plenty of factors behind this sophisticated problem. In order to ﬁnd how graphical location, marital status, education level, age distribution and other factors contribute to the opioid crisis, one appropriate method is to ﬁrst ﬁnd similar zones based on social structure, then compare that how their drug spread and opioid drug identiﬁcation cases distribution relates each other and then we extend our model to serve different purposes, such as tracing the drug source, predicting the drug spread.

<!-- b000015 | prose | pages [1] -->
For the ﬁrst part, we construct a weighted directed graph based on the similarity(described above) and use "Walk Around" strategy to simulate the drug spread process to trace the drug start source. Still based on similarity, we use SVR regression to ﬁt the data distribution over time and predict the following two years of synthetic opioid drug identiﬁcation and heroin cases distribution situation. Then we use a SVM discriminator to predict whether a county will be in the risk of opioid crisis. A county in opioid crisis will face a continues increase in drug abuse.

<!-- b000016 | prose | pages [1] -->
For the second part,We ﬁrst binarize all the data through the Kmeans algorithm, then we use association rule learning algorithms to look for factors that lead to opioids and drug addiction. We then introduced the time factor, further streamlined the factors through correlation analysis methods, and found people who abused opioids.After these steps we can ﬁnd all the main factors. However, due to the large number of these factors, we also need to use the PCA algorithm to reduce the output factors to make the prediction model simpler.Our model ﬁnds that difference in population distribution has a huge impact on the abuse of opioids.

<!-- b000017 | prose | pages [1] -->
For the third part, we extract three main features from part two, reintegrate the data and invoke this into our previous model, making our model do regression with multiple dimensions. We design some strategy aimed for different groups and use our model to verify the effectiveness of our strategies. Our model ﬁnds that special attention should be payed to female householder without husband as well as householder who is 65 years old or older and improving overall education level can also decrease opioid addiction rate.

<!-- b000018 | keywords | pages [1] -->
Keywords: Recommendation System, Regression, PCA, Association Rule Learning

<!-- b000019 | title | pages [2] -->
Analysis of the opioid crisis and strategies

<!-- b000020 | furniture | pages [2] -->
team # 1906204

<!-- b000021 | prose | pages [2] -->
January 29, 2019

<!-- b000022 | heading | pages [2] -->
Summary

<!-- b000023 | prose | pages [2] -->
The United States is undergoing an unprecedented opioid crisis. Opioid drugs have been widely used as medicine in a variety of treatments. The fast pace of life and ﬁerce social competition put a lot of pressure on people. People with mental or physical illness will probably be treated with many drugs and they are likely to get addicted to them, especially to opioid drugs. Thus, more and more drug identiﬁcation cases have been conﬁrmed in recent years.

<!-- b000024 | prose | pages [2] -->
The goal of our model is to ﬁnd the spread and characteristics of the reported synthetic opioid and heroin incidents and do possible explanation for current situation and prediction for future case distribution, based on provided data. Speciﬁcally, our model is inspired from "Recommendation System". The ﬁrst step of our model has the similar purpose as "Recommendation System" does that is to ﬁnd similarity and corre- lation between different zones and drugs. It is rough and inaccurate to directly address the data regardless of plenty of factors behind this sophisticated problem. In order to ﬁnd how graphical location, marital status, education level, age distribution and other factors contribute to the opioid crisis, one appropriate method is to ﬁrst ﬁnd similar zones based on social structure, then compare that how their drug spread and opioid drug identiﬁcation cases distribution relates each other and then we extend our model to serve different purposes, such as tracing the drug source, predicting the drug spread.

<!-- b000025 | prose | pages [2] -->
For the ﬁrst part, we construct a weighted directed graph based on the similarity(described above) and use "Walk Around" strategy to simulate the drug spread process to trace the drug start source. Still based on similarity, we use SVR regression to ﬁt the data distribution over time and predict the following two years of synthetic opioid drug identiﬁcation and heroin cases distribution situation. Then we use a SVM discriminator to predict whether a county will be in the risk of opioid crisis. A county in opioid crisis will face a continues increase in drug abuse.

<!-- b000026 | prose | pages [2] -->
For the second part,We ﬁrst binarize all the data through the Kmeans algorithm, then we use association rule learning algorithms to look for factors that lead to opioids and drug addiction. We then introduced the time factor, further streamlined the factors through correlation analysis methods, and found people who abused opioids.After these steps we can ﬁnd all the main factors. However, due to the large number of these factors, we also need to use the PCA algorithm to reduce the output factors to make the prediction model simpler.Our model ﬁnds that difference in population distribution has a huge impact on the abuse of opioids.

<!-- b000027 | prose | pages [2] -->
For the third part, we extract three main features from part two, reintegrate the data and invoke this into our previous model, making our model do regression with multiple dimensions. We design some strategy aimed for different groups and use our model to verify the effectiveness of our strategies. Our model ﬁnds that special attention should be payed to female householder without husband as well as householder who is 65 years old or older and improving overall education level can also decrease opioid addiction rate.

<!-- b000028 | keywords | pages [2] -->
Keywords: Recommendation System, Regression, PCA, Association Rule Learning

<!-- b000029 | furniture | pages [3] -->
Team # 1906204

<!-- b000030 | furniture | pages [3] -->
Page 1 of 38

<!-- b000031 | heading | pages [3] -->
Contents

<!-- b000032 | contents | pages [3] -->
1 Introduction

<!-- b000033 | contents | pages [3] -->
3

<!-- b000034 | contents | pages [3] -->
1.1

<!-- b000035 | contents | pages [3] -->
Background

<!-- b000036 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [3] -->
3

<!-- b000038 | contents | pages [3] -->
2 Analysis of the Problem

<!-- b000039 | contents | pages [3] -->
3

<!-- b000040 | contents | pages [3] -->
2.1

<!-- b000041 | contents | pages [3] -->
Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [3] -->
3

<!-- b000043 | contents | pages [3] -->
2.1.1

<!-- b000044 | contents | pages [3] -->
Use K-means to Divide Areas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [3] -->
3

<!-- b000046 | contents | pages [3] -->
2.2

<!-- b000047 | contents | pages [3] -->
Basic Assumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [3] -->
4

<!-- b000049 | contents | pages [3] -->
2.3

<!-- b000050 | contents | pages [3] -->
Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [3] -->
5

<!-- b000052 | contents | pages [3] -->
3 Models

<!-- b000053 | contents | pages [3] -->
5

<!-- b000054 | contents | pages [3] -->
3.1

<!-- b000055 | contents | pages [3] -->
Basic Model Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [3] -->
5

<!-- b000057 | contents | pages [3] -->
3.1.1

<!-- b000058 | contents | pages [3] -->
Recommendation System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [3] -->
5

<!-- b000060 | contents | pages [3] -->
3.1.2

<!-- b000061 | contents | pages [3] -->
Mathematical Formulation

<!-- b000062 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [3] -->
6

<!-- b000064 | contents | pages [3] -->
3.1.3

<!-- b000065 | contents | pages [3] -->
Similarity Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [3] -->
6

<!-- b000067 | contents | pages [3] -->
3.2

<!-- b000068 | contents | pages [3] -->
"Walk Around" in Graph to ﬁnd Origin

<!-- b000069 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [3] -->
6

<!-- b000071 | contents | pages [3] -->
3.3

<!-- b000072 | contents | pages [3] -->
SVM Discriminator in Evaluate Drug Identiﬁcation Threshold Levels . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [3] -->
9

<!-- b000074 | contents | pages [3] -->
3.3.1

<!-- b000075 | contents | pages [3] -->
SVM Discriminator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [3] -->
9

<!-- b000077 | contents | pages [3] -->
3.3.2

<!-- b000078 | contents | pages [3] -->
One Class SVM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [3] -->
9

<!-- b000080 | contents | pages [3] -->
3.3.3

<!-- b000081 | contents | pages [3] -->
Threshold Identiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [3] -->
9

<!-- b000083 | contents | pages [3] -->
3.4

<!-- b000084 | contents | pages [3] -->
Use SVR Regression to make Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | contents | pages [3] -->
10

<!-- b000086 | contents | pages [3] -->
3.4.1

<!-- b000087 | contents | pages [3] -->
Algorithm Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [3] -->
10

<!-- b000089 | contents | pages [3] -->
3.5

<!-- b000090 | contents | pages [3] -->
Advantage of SVR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [3] -->
11

<!-- b000092 | contents | pages [3] -->
3.5.1

<!-- b000093 | contents | pages [3] -->
Determine the best parameter for SVR . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [3] -->
11

<!-- b000095 | contents | pages [3] -->
3.6

<!-- b000096 | contents | pages [3] -->
Evaluate County Opioid Problem in the Future . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [3] -->
12

<!-- b000098 | contents | pages [3] -->
3.6.1

<!-- b000099 | contents | pages [3] -->
Model Prediction Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [3] -->
12

<!-- b000101 | contents | pages [3] -->
3.6.2

<!-- b000102 | contents | pages [3] -->
Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [3] -->
13

<!-- b000104 | contents | pages [3] -->
3.7

<!-- b000105 | contents | pages [3] -->
Choosing Factors: Using the U.S. Census socio-economic data . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [3] -->
13

<!-- b000107 | contents | pages [3] -->
3.7.1

<!-- b000108 | contents | pages [3] -->
Association rule learning: Apriori

<!-- b000109 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [3] -->
13

<!-- b000111 | contents | pages [3] -->
3.7.2

<!-- b000112 | contents | pages [3] -->
Correlation Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [3] -->
16

<!-- b000114 | contents | pages [3] -->
3.7.3

<!-- b000115 | contents | pages [3] -->
PCA Feature Extraction

<!-- b000116 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000117 | contents | pages [3] -->
16

<!-- b000118 | contents | pages [3] -->
4 Strategy for Countering Opioid Crisis

<!-- b000119 | contents | pages [3] -->
16

<!-- b000120 | contents | pages [3] -->
4.1

<!-- b000121 | contents | pages [3] -->
Brief Explanation for Factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000122 | contents | pages [3] -->
16

<!-- b000123 | contents | pages [3] -->
4.2

<!-- b000124 | contents | pages [3] -->
Possible Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [3] -->
17

<!-- b000126 | contents | pages [3] -->
4.2.1

<!-- b000127 | contents | pages [3] -->
For the Elder

<!-- b000128 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000129 | contents | pages [3] -->
17

<!-- b000130 | contents | pages [3] -->
4.2.2

<!-- b000131 | contents | pages [3] -->
About Education Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000132 | furniture | pages [4] -->
Team # 1906204

<!-- b000133 | furniture | pages [4] -->
Page 2 of 38

<!-- b000134 | contents | pages [4] -->
4.2.3

<!-- b000135 | contents | pages [4] -->
For Female Householder Without Husband . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000136 | contents | pages [4] -->
17

<!-- b000137 | contents | pages [4] -->
4.2.4

<!-- b000138 | contents | pages [4] -->
Considering Other Factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000139 | contents | pages [4] -->
17

<!-- b000140 | contents | pages [4] -->
4.3

<!-- b000141 | contents | pages [4] -->
Strategies Veriﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000142 | contents | pages [4] -->
18

<!-- b000143 | contents | pages [4] -->
4.3.1

<!-- b000144 | contents | pages [4] -->
Validation for Equivalent Veriﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000145 | contents | pages [4] -->
18

<!-- b000146 | contents | pages [4] -->
4.3.2

<!-- b000147 | contents | pages [4] -->
Veriﬁcation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000148 | contents | pages [4] -->
18

<!-- b000149 | contents | pages [4] -->
4.3.3

<!-- b000150 | contents | pages [4] -->
Findings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000151 | contents | pages [4] -->
19

<!-- b000152 | heading | pages [4] -->
5 Model Analysis

<!-- b000153 | prose | pages [4] -->
19

<!-- b000154 | heading | pages [4] -->
6 Memo

<!-- b000155 | prose | pages [4] -->
21

<!-- b000156 | prose | pages [4] -->
6.1 Origin of the Opioid Drug Abuse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

<!-- b000157 | prose | pages [4] -->
6.2 Prediction of Opioid Abuse Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

<!-- b000158 | prose | pages [4] -->
6.3 Correlated Factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

<!-- b000159 | prose | pages [4] -->
6.4 Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000160 | prose | pages [4] -->
6.4.1 For Elder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000161 | prose | pages [4] -->
6.4.2 About Education Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000162 | prose | pages [4] -->
6.4.3 For Female Householder Without Husband . . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000163 | prose | pages [4] -->
6.4.4 Considering Other Factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000164 | heading | pages [4] -->
Appendices

<!-- b000165 | prose | pages [4] -->
23

<!-- b000166 | furniture | pages [5] -->
Team # 1906204

<!-- b000167 | furniture | pages [5] -->
Page 3 of 38

<!-- b000168 | heading | pages [5] -->
1 Introduction

<!-- b000169 | heading | pages [5] -->
1.1 Background

<!-- b000170 | prose | pages [5] -->
A drug crisis is storming in the United States, regarding to the use of synthetic and non-synthetic opioids, either for the treatment and the management of the pain or for recreational purpose. Ofﬁcial organizations such as Centers for Disease Control are struggling to control the spread of infectious diseases and mitigate the negative impact of opioid drugs, especially for the well-educated people with advanced degrees and the elder.

<!-- b000171 | prose | pages [5] -->
The DEA/National Forensic Laboratory Information System has published a data-heavy annual report addressing ”drug identiﬁcation results” recently, which has caused widespread concern. In order to have a deeper insight of this problem, researches mainly focus on the individual counties located in ﬁve U.S. states: Ohio, Kentucky, West Virginia, Virginia and Tennessee. The relative data covers drug identiﬁcation counts in years 2010-2017 for synthetic opioids and heroin in each of the counties from these ﬁve states. Ad- ditional data contains extracts from the U.S. Census Bureau that represent a common set of socio-economic factors collected for the counties of these ﬁve states during each of the years 2010-2016.

<!-- b000172 | heading | pages [5] -->
2 Analysis of the Problem

<!-- b000173 | heading | pages [5] -->
2.1 Data Preprocessing

<!-- b000174 | prose | pages [5] -->
Checking all the data in the ”MCM_NFLIS_DATA.xlsx”, it is easy to ﬁgure out that there are 69 different kinds of opioid drugs and 462 different counties in these ﬁve states. More speciﬁcally speaking, many kinds of drugs in some counties have almost no or very few ”Drug Reports”, which means the samples for a speciﬁc drug from a speciﬁc county are far from enough, which may mislead us to analyze the drug spread situation and prediction. To make the spread characters and tendency more apparent to observe, we use K-means Clustering to preprocess the data, dividing it into some larger areas called ”Zones”, the drug report in the zone is the sum of drug reports of all counties resident in the current zone.

<!-- b000175 | heading | pages [5] -->
2.1.1 Use K-means to Divide Areas

<!-- b000176 | prose | pages [5] -->
To implement regionalization appropriately, we ought to make ”Zone” neither too big or too smaller. By trying many times, we select the best case where we set parameter k as 100. Technically, we just used the basic K-means Algorithm and all 100 clusters have the same radius and each has number of counties roughly ranging from 2 to 8. Before clustering, we transform the ”FIPS_Combined” into corresponding Longitude and Latitude, then applied K-means algorithm. Finally, we integrated the all drug identiﬁcation reports for each kind of drug within the same zone. The following ﬁgures show the format of preprocessed data,

<!-- b000177 | caption | pages [5] -->
Figure 1: Data by Zone

<!-- b000178 | prose | pages [5] -->
YYYY Zone substanceName DrugReport TotalDrugReportZone 2010 0 Propoxyphene 1 327 2010 0 Oxycodone 4 327 2010 0 Hydrocodone 9 327 ... ... ... ... ...

<!-- b000179 | prose | pages [5] -->
After transforming data into this form, we can analyze the drug spread process from a higher level, then focus on several special zones and take a deep look into it conveniently. The following ﬁg. shows the visualization of the zones.

<!-- b000180 | furniture | pages [6] -->
Team # 1906204

<!-- b000181 | furniture | pages [6] -->
Page 4 of 38

<!-- b000182 | caption | pages [6] -->
Figure 2: ZoneCounty Map

<!-- b000183 | prose | pages [6] -->
Zone Latitude Longitude FIPS_Combined 0 37.6189 -75.8400 51001, 51620, 51115, 51119, 51131 1 41.5442 -84.0702 39001, 39047, 39051, 39095, 39173, 39171 1 39.9813 -77.2332 42001, 42041, 42055, 42133 ... ... ... ...

<!-- b000184 | caption | pages [6] -->
Figure 3: Clustered Zones

<!-- b000185 | prose | pages [6] -->
(Note: each zone ought to have one color, but we don’t have 100 colors, we only use 20 colors to distinguish)

<!-- b000186 | heading | pages [6] -->
2.2 Basic Assumption

<!-- b000187 | prose | pages [6] -->
• Trend of opioid addiction distribution changes over time. When doing prediction, we take time into account. The latest tendency will have a higher inﬂuence factor.

<!-- b000188 | prose | pages [6] -->
• Opioid abuse spread depends on graphical location. We assume that the spread of drug mainly from one place to adjacent places and will not across a great distance.

<!-- b000189 | prose | pages [6] -->
• When addressing data missing, we regard it as average value.

<!-- b000190 | furniture | pages [7] -->
Team # 1906204

<!-- b000191 | furniture | pages [7] -->
Page 5 of 38

<!-- b000192 | heading | pages [7] -->
2.3 Overview

<!-- b000193 | prose | pages [7] -->
ACS_1x_5YR_DP02 MCM_NFLIS_Data

<!-- b000194 | prose | pages [7] -->
Crawling geographic Preprocessing: numerical information Booleanization Processing ﬂow Part1 result Preprocessing: Kmeans Association rule learning: Groups inclined to Part2,3 result clustering Apriori algorithm abuse opioids

<!-- b000195 | prose | pages [7] -->
One class SVM: label Factors inﬂuencing Similarity calculation Correlation Analysis Generating graph model origin data opioid usage trend

<!-- b000196 | prose | pages [7] -->
SVR regression Simulation by PCA dimensionality Training SVM classiﬁer and veriﬁcation random walk reduction

<!-- b000197 | prose | pages [7] -->
Generating the source SVR regression Policy development Predicting abuse areas of opioids and veriﬁcation and veriﬁcation

<!-- b000198 | caption | pages [7] -->
Figure 4: Model overview

<!-- b000199 | prose | pages [7] -->
The above diagram introduces the main workﬂow of our model. The left part of the PART1 workﬂow is divided into data preprocessing, model training, and model validation. The right part is the workﬂow of PART2,3, which is mainly divided into data preprocessing, correlation analysis, association rule learning, model veriﬁcation, and rule making.

<!-- b000200 | heading | pages [7] -->
3 Models

<!-- b000201 | heading | pages [7] -->
3.1 Basic Model Description

<!-- b000202 | prose | pages [7] -->
In order to ﬁgure out what the spread and characteristics of the reported synthetic opioid and heroin incidents in and between the ﬁve states and their counties over time, identify the origin and predict the possible future drug use situation, we decide to use the Recommendation System.

<!-- b000203 | heading | pages [7] -->
3.1.1 Recommendation System

<!-- b000204 | prose | pages [7] -->
Imagine that you have just ﬁnished watching a ﬁlm, and feel deeply impressed by it and you even make an evaluation of 5 stars. Movie website accepts your evaluation and it will automatically recommend you some ﬁlms that you may like based on your recent behavior, such as evaluation behavior. The core part of the recommendation system is to ﬁnd similar users who share the same preference and these similar users may see some other ﬁlms which you haven’t seen but they thinks good. Thus, the system will recommend you these ﬁlms.

<!-- b000205 | prose | pages [7] -->
Our model reﬂects the main idea of "Recommendation System", that is to ﬁnd the similar zones. Those similar zones will share the similar spread and characteristics of reported synthetic opioid and heroin inci- dents to a great extent. These similar zones help us amplify the spread and characteristics as well as make prediction more accurate.

<!-- b000206 | furniture | pages [8] -->
Team # 1906204

<!-- b000207 | furniture | pages [8] -->
Page 6 of 38

<!-- b000208 | heading | pages [8] -->
3.1.2 Mathematical Formulation

<!-- b000209 | prose | pages [8] -->
Since there are 100 zones and 69 different opioids, we create a 100×69 matrix. Each line represents a zone number and each column stands for a opioid drug number. Then cell(i, j) in this matrix will represent some information of number j drug in zone i. The information will be somehow different for different purposes.

<!-- b000210 | heading | pages [8] -->
3.1.3 Similarity Design

<!-- b000211 | prose | pages [8] -->
How can we tell two zones are similar is closely related to the performance of the model. In our model, we carefully take three main factors into account. (1) Trend over time (2) Geographical factor (3) Drug identiﬁcation size.

<!-- b000212 | prose | pages [8] -->
• Factor (1): based on the mathematical formulation above, we store a list in each cell(i, j), which contains six years of data(2010-2016) for the j’th drug in i’th zone. When calculating the similarity be- tween any pair zones, we ﬁnd the correlation for each kind of drug, then make weighted summation.

<!-- b000213 | prose | pages [8] -->
The deﬁnition of correlation is as follows:

<!-- b000214 | prose | pages [8] -->
= E[(X −µX)(Y −µY )] Corr(X, Y ) = cov(X, Y ) σXσY σXσY

<!-- b000215 | prose | pages [8] -->
Using the numpy.corrcoef() method from "Numpy" package in python can implement the calculation quickly and conveniently.

<!-- b000216 | prose | pages [8] -->
• Factor (2): In practice, geographical factor plays critical role in drug spread. People are inclined to migrate from one zone to adjacent zones. This process may trigger drug spread, resulting that drug identiﬁcation situation in one zone is more likely to be similar to that in adjacent zones. We can easily calculate distance between any zone pair based on their longitudes and latitudes. According to our test, controlling distance within 200 km makes model perform well.

<!-- b000217 | prose | pages [8] -->
• Factor (3): The size of drug identiﬁcation is another signiﬁcant factor should be taken into account.

<!-- b000218 | prose | pages [8] -->
A zone with fewer drug identiﬁcation cases has the tendency to be stable and growth or decline may have mutation, compared to zones with larger size of drug identiﬁcation cases. When computing the similarity, we take summation of all six years of data and also invoke time decay factor.

<!-- b000219 | prose | pages [8] -->
2016 X dataiνi−1 Total = i=2010

<!-- b000220 | prose | pages [8] -->
with ν = 0.7, the later the data is, the more important the data should be.

<!-- b000221 | prose | pages [8] -->
For each zone, we use Factor (2) to ﬁnd the "close zones" and give each close zone a score based on the factor (1) and (3). Pick the 10 zones with highest score, by sorting.

<!-- b000222 | prose | pages [8] -->
3.2 "Walk Around" in Graph to ﬁnd Origin

<!-- b000223 | prose | pages [8] -->
In this part, we mainly want to ﬁnd the source of some opioids.Imagine that we are browsing the webpage, we will open a web address, browse the page, and then select the favorite topic according to the URL on the page. We will continue to open the new webpage along the link of the page.The spread of opioids has similar behavior. An opioid is popular from a city and slowly affects surrounding cities. However, due to the different characteristics of the city, the speed of transmission of speciﬁc opioids in surrounding cities will vary greatly. Here we assume that cities with similar characteristics will have similar patterns when opioids are transmitted. Therefore, the probability that opioids will spread to neighboring cities will be different. This probability is described by the similarity between the cities in the above sections.

<!-- b000224 | prose | pages [8] -->
The ﬁrst step in our model is to construct a propagation graph model for opioids.Suppose we are looking for the source of heroin. The ﬁrst step in our model is to construct a propagation map model for opioids.

<!-- b000225 | furniture | pages [9] -->
Team # 1906204

<!-- b000226 | furniture | pages [9] -->
Page 7 of 38

<!-- b000227 | prose | pages [9] -->
We selected heroin data for any given year. Each node in the ﬁgure represents a clustering point, and the weight of each node represents the number of people who smoked this drug in that place. When the number of nodes A (WA) is higher than the other node B (WB), a directed edge from A to B is generated(A– >B). The weight of the edge is the similarity of A and B (sim(A, B) = pA−>B). The graph generated for heroin is shown below.

<!-- b000228 | prose | pages [9] -->
69

<!-- b000229 | prose | pages [9] -->
10

<!-- b000230 | prose | pages [9] -->
37 1 97 57 59 68 49 54 63 38 55 50 56 9 75 33 8 91 79 20 36 61 64 12 98 30 4 92 80 46 2 65 16 41

<!-- b000231 | prose | pages [9] -->
32 52 13 19 67 11 51 28 35 94 22 7 88 71 58 34 25 24 40 27 42 77 82 78 44 39 73 31 93 72 23 70 86 74 83 62 0 26 47 76 95 29 85 15 17 43 21 89 53 6 66 81 14 45 18 90 48 5 87 99 96 60 84

<!-- b000232 | caption | pages [9] -->
Figure 5: Graph model of drug transmission. The light color of the node represents a large number of

<!-- b000233 | prose | pages [9] -->
people, and the color of the edge represents the magnitude of the transition probability.

<!-- b000234 | prose | pages [9] -->
The second step is to ﬁnd the nodes that may become the source of drugs according to the above graph model. We call this the candidate set. CandidateSet = {node1, node2, node3, ...}. In graph theory, the de- gree (or valency) of a vertex of a graph is the number of edges incident to the vertex, with loops counted twice. Here we change the deﬁnition to the number of edges scatter from the vertex. For every node we calculate its degree (Deg(v)), We select the largest 5 nodes and store them in the candidate set.

<!-- b000235 | prose | pages [9] -->
The third step is to simulate the propagation behavior of a drug by using the simulation method of random walk. Simulate the nodes in the Candidate Set separately, simulate 100 times for each node, record the number of visits of other nodes(ni), and calculate the score for each node by the following formula. The highest score is the source we want to ﬁnd.

<!-- b000236 | prose | pages [9] -->
99 X nj ∗Wi ∗pi−>j i ∈Candidate Set Scorei = j=0 and j̸=i

<!-- b000237 | prose | pages [9, 10] -->
Source = index(max(Score) Score ∈{Score1, Score2, Score3, ...})   transition  0.6 0.7 probability 0.7  0.9 0.4 0.6 0.2 0.99 

<!-- b000238 | furniture | pages [10] -->
Team # 1906204

<!-- b000239 | furniture | pages [10] -->
Page 8 of 38

<!-- b000241 | prose | pages [10] -->


<!-- b000242 | prose | pages [10] -->
Candidate Set: 

<!-- b000243 | prose | pages [10] -->
Score:   Source:   

<!-- b000244 | prose | pages [10] -->
Simple example(Source == 10) Heroin example(Source == 32)

<!-- b000245 | caption | pages [10] -->
Figure 6: The diagram on the left shows the implementation of the simulation algorithm for random walks.

<!-- b000246 | prose | pages [10] -->
The example on the right shows that after the simulation, the source of heroin is in the 32nd area.

<!-- b000247 | prose | pages [10] -->
Dihydrocodeine Butorphanol ANPP MT-45 Levorphanol Opium Alphaprodine Desmethylprodine 4-Fluoroisobutyryl fentanyl Remifentanil Acetyl fentanyl p-Fluorobutyryl fentanyl Fluorofentanyl U-47700 3-Methylfentanyl 3-Fluorofentanyl Phenyl fentanyl Cyclopropyl fentanyl Methoxyacetyl fentanyl U-48800 Benzylfentanyl U-51754 Crotonyl fentanyl Cyclopropyl/Crotonyl Fentanyl Cyclopentyl fentanyl 4-Methylfentanyl Metazocine'

<!-- b000248 | prose | pages [10] -->
Origin of drugs

<!-- b000249 | prose | pages [10] -->
Drugs’name Drug... Dextropropoxyphene Oxymorphone Fentanyl Morphine Oxycodone Meperidine Tramadol Heroin Pentazocine Propoxyphene Methadone Hydromorphone Opiates Buprenorphine Hydrocodone Codeine

<!-- b000250 | prose | pages [10] -->
Methorphan

<!-- b000251 | prose | pages [10] -->
Pethidine Mitragynine Acetyldihydrocodeine Hydrocodeinone Furanyl fentanyl Carfentanil Acryl fentanyl trans-3-Methylfentanyl p-methoxybutyryl fentanyl p-Fluorofentanyl o-Fluorofentanyl Furanyl/3-Furanyl fentanyl U-49900 3,4-Methylenedioxy U-47700 Isobutyryl fentanyl

<!-- b000252 | caption | pages [10] -->
Figure 7: Origin of all opioids

<!-- b000253 | prose | pages [10] -->
Result analysis, the above diagram shows the source of all opioids that appear in the problem.From this we can analyze many interesting phenomena. Trafﬁc factors:We can see the source of a lot of opioids, near the ocean, or near the Great Lakes. The proximity to the ocean has made it easier to import illegal drugs or opioids from abroad, making these areas a source of numerous opioids. Legal factors:We can see that Ohio is the source of many drugs. The reason for this situation may be related to the fact that local laws and regulations still have loopholes and the government’s supervision is not strong.

<!-- b000254 | furniture | pages [11] -->
Team # 1906204

<!-- b000255 | furniture | pages [11] -->
Page 9 of 38

<!-- b000256 | heading | pages [11] -->
3.3 SVM Discriminator in Evaluate Drug Identiﬁcation Threshold Levels

<!-- b000257 | prose | pages [11] -->
In some counties, number of opioids drug identiﬁcation counts is remarkably higher than other parts of the state. It reveals more severe drug abuse problem occurs in this county. A large number of drug incidents also reﬂect denser population, which has strong inﬂuence on drug spreads. In most cases, an outlier data reveals either a fault or should be highlighted. Here we assume that some counties are already facing opioid crisis. Through observation, a certain gap was found between counties with less drug reports and counties with more reports. So we use a SVM discriminator to separate these too kinds of counties. Counties in class with more drug reports are facing risk of opioid crisis

<!-- b000258 | heading | pages [11] -->
3.3.1 SVM Discriminator

<!-- b000259 | prose | pages [11] -->
SVM Discriminator is used to separate counties with risk of getting into opioid crisis from others, given predicted number of opioid incidents. For 2D value, SVM discriminator trained a line called hyperplane to separate two different classes. Hyperplane was given by ωT x + γ = 0 where ω is the normal vector to the  ωT xi + γ > 0 for yi = 1 hyperplane and x is the points on the plane. A valid hyperplane satisﬁes: ωT xi + γ < 0 for yi = −1 Support vector is points closest to hyperplane, they are edges of two different sets.

<!-- b000260 | heading | pages [11] -->
3.3.2 One Class SVM

<!-- b000261 | prose | pages [11] -->
SVM discriminator is a supervised learning models, but with no labeled training data given, an unsuper- vised version of SVM should be applied. So one-class-SVM was introduced. The goal of one class SVM method is to separate data points and origin at feature mapped space as far as possible. Firstly use Gaus- sian kernel to project data points on to feature space, then we want to solve following quadratic program 2∥w∥2 + Pn minw,ζi,ρ 1 1  i=1 ζi −ρ νn  wT φ (xi)    > ρ −ζi, i = 1, . . . , n s.t. , where ξi is slack, to separate projected data points from origin:

<!-- b000262 | prose | pages [11] -->
ζi > 0  ν ∈(0, 1) determines upper limits of outliers. A line in featured map space was ﬁnally trained to separate origin from data. Then transform the line and data back to unprojected space, outside the line are outliers.

<!-- b000263 | heading | pages [11] -->
3.3.3 Threshold Identiﬁcation

<!-- b000264 | prose | pages [11] -->
Our SVM Discriminator combines one class SVM and linear SVM. We use one-class-SVM on opioid drug reports from 2010-2017 in total to determine outliers at ﬁrst. These outliers indicates counties in the danger of opioid crisis. Then we use the labeled data from one class SVM to train a linear SVM as threshold for opioid abuse alert. Since the drug abuse problem is not only shown by opioid usage but also other drugs, a county with much opioid incidents compared with total drug reports or a large number of total drug report without opioid incidents should all be considered as facing crisis. Therefore, we use total drug report of a county as y-axis and total opioid use as x-axis to include the situation above. Later, we will use this trained model as ﬁlter, predicted drug reports number as input, dangerous level as output. The following picture is showing the process of training, highlighted line is hyperplane:

<!-- b000265 | furniture | pages [12] -->
Team # 1906204

<!-- b000266 | furniture | pages [12] -->
Page 10 of 38

<!-- b000267 | prose | pages [12] -->
Outlier Detection via One-Class SVM 104 16 Observation Support Vector 14

<!-- b000268 | prose | pages [12] -->
12 Total Drug Report by County 10

<!-- b000269 | prose | pages [12] -->
8

<!-- b000270 | prose | pages [12] -->
6

<!-- b000271 | prose | pages [12] -->
4

<!-- b000272 | prose | pages [12] -->
2

<!-- b000273 | prose | pages [12] -->
0 0 500 1000 1500 2000 2500 Opioid Drug Reports

<!-- b000274 | caption | pages [12] -->
Figure 8: SVM Discriminator

<!-- b000275 | heading | pages [12] -->
3.4 Use SVR Regression to make Prediction

<!-- b000276 | prose | pages [12] -->
To predict when and where will some speciﬁc drug reaching the drug identiﬁcation threshold occur, we will combine the "Recommendation System" with Supporting Vector Regression(SVR).

<!-- b000277 | heading | pages [12] -->
3.4.1 Algorithm Details

<!-- b000278 | prose | pages [12] -->
Pseudocodes

<!-- b000279 | heading | pages [12] -->
Algorithm 1 Recommendation System Combined with SVR Regression

<!-- b000280 | prose | pages [12] -->
1: # 100×69×6 Info Matrix stores six years’ drug reports for each drug in each zone. 2: features ←empty dictionary 3: for Each zone zi do simi_zones ←zi’s all similar zones 4:

<!-- b000281 | prose | pages [12] -->
for Each Drug dj do 5:

<!-- b000282 | prose | pages [12] -->
feature ←empty set # to store regression results 6:

<!-- b000283 | prose | pages [12] -->
get SVR regression of its own as a feature, push to list feature 7:

<!-- b000284 | prose | pages [12] -->
for Each Training Sample sk do 8:

<!-- b000285 | prose | pages [12] -->
get SVR regression of its sample as a feature, push to list feature 9:

<!-- b000286 | prose | pages [12] -->
end for 10:

<!-- b000287 | prose | pages [12] -->
# weight ←empty set 11:

<!-- b000288 | prose | pages [12] -->
for Each feature do 12:

<!-- b000289 | prose | pages [12] -->
use feature to predict val and ﬁnd difference between predicted value and real value 13:

<!-- b000290 | prose | pages [12] -->
1 take 0.01+(difference)2 as weight of the current feature 14:

<!-- b000291 | prose | pages [12] -->
end for 15:

<!-- b000292 | prose | pages [12] -->
normalize weight 16:

<!-- b000293 | prose | pages [12] -->
store features[zi][dj] ←[feature, weight] 17:

<!-- b000294 | prose | pages [12] -->
end for 18: 19: end for

<!-- b000295 | prose | pages [12] -->
Explanation

<!-- b000296 | prose | pages [12] -->
• We ﬁrst create a 100×69×6 InfoMatrix to store six years’ drug reports for each drug in each zone. Then for each zone, we ﬁnd the 10 most similar zones, each of them will provide a sample. We use SVR to ﬁt each of the sample as one feature for the speciﬁc drug in the speciﬁc zone. After we obtained all features(11 in total, 1 from itself, 10 from samples), we modify each feature by multiplying a hyper- parameter – weight coefﬁcient, in order to make the model more reasonable and stable to predict the future.

<!-- b000297 | furniture | pages [13] -->
Team # 1906204

<!-- b000298 | furniture | pages [13] -->
Page 11 of 38

<!-- b000299 | prose | pages [13] -->
• Based on the idea from machine learning, we separate the data into 3 set, training set(data 2010-2015), held-out set(data 2016) and test set(data 2017). We extract features from training set and calculate hyper-parameter from held-out set. Finally, use test set to verify the performance of our model.

<!-- b000300 | prose | pages [13] -->
• Another problem is how we set the hyper-parameters. Intuitively, the more close between a predicted value and real value, the more important the feature is, roughly satisfying inverse proportion. After 1 trying many time, we set the formate of weight to 0.01+(difference)2 which has almost the smallest least square error when testing by date from test set.

<!-- b000301 | prose | pages [13] -->
• After we ﬁnd the best formate of hyper-parameter, we divide data into 2 parts, training set(2010-2016) and held-out set(2017), then train the model again which will be used for later prediction.

<!-- b000302 | heading | pages [13] -->
3.5 Advantage of SVR

<!-- b000303 | prose | pages [13] -->
The following reasons explain that we choose SVR instead of other method to do the regression,

<!-- b000304 | prose | pages [13] -->
• Suit for multiple dimensional regression

<!-- b000305 | prose | pages [13] -->
• Fast in computing (python has package off the shelf)

<!-- b000306 | prose | pages [13] -->
• There is no overﬁtting

<!-- b000307 | heading | pages [13] -->
3.5.1 Determine the best parameter for SVR

<!-- b000308 | prose | pages [13] -->
SRV is a mature model with many parameters used for different purposes. The most common modes are "rbf" and "poly". For "poly" mode, we can set degree to any integer we want. So we test this basic setting to ﬁnd the best model. The following test results shows the Least Square Error(difference between predicted 2017 date and real 2017 data) for each pair parameter settings,

<!-- b000309 | caption | pages [13] -->
Figure 9: Poly Tests

<!-- b000310 | prose | pages [13] -->
LSE Degree 1 2 3 4 kernel "Poly" 47116.0 39458.0 28908.0 48322(slow)

<!-- b000311 | caption | pages [13] -->
Figure 10: RBF Tests

<!-- b000312 | prose | pages [13] -->
LSE gamma 0.1 0.5 1 2 C 1e0 50332.0 50363.0 50496.0 50692.0 1e1 47804.0 48434.0 49189.0 49968.0 1e2 40161.0 41977.0 44438.0 46868.0 1e3 30788.0 32755.0 37597.0 42033.0

<!-- b000313 | prose | pages [13] -->
After the testing, we ﬁnd that set kernel to "poly" and set degree to 3 is the best option. (Note: when kernel mode is "poly", we still need to consider parameter C, but during our test C has almost no inﬂuence to the result, so we just use default value.)

<!-- b000314 | furniture | pages [14] -->
Team # 1906204

<!-- b000315 | furniture | pages [14] -->
Page 12 of 38

<!-- b000316 | heading | pages [14] -->
3.6 Evaluate County Opioid Problem in the Future

<!-- b000317 | heading | pages [14] -->
3.6.1 Model Prediction Flow

<!-- b000318 | prose | pages [14] -->
The SVR predictor introduced above uses NFLIS data 2010-2017 to predict number of opioid usage in total by areas. Since the given data only covers seven years, a prediction on further future based on these data are lacking ﬁdelity, we only predict opioids drug identiﬁcation counts in 2018 & 2019. The result is shown below, darker color indicates more opioid issues.

<!-- b000319 | caption | pages [14] -->
Figure 11: Prediction Opioid Reports 2018

<!-- b000320 | caption | pages [14] -->
Figure 12: Prediction Opioid Reports 2019

<!-- b000321 | prose | pages [14] -->
Then we train the SVM discriminator according to the data 2010-2017, and set the predicted result as input. Output is shown below, highlighted areas are areas in risk of opioid crisis.

<!-- b000322 | caption | pages [14] -->
Figure 13: Predicted area in risk 2018

<!-- b000323 | caption | pages [14] -->
Figure 14: Predicted area in risk 2019

<!-- b000324 | prose | pages [14] -->
Pennsylvania Adams Cumberland Franklin York Ohio Ashtabula Lake Pennsylvania Chester Lancaster Ohio Cuyahoga Geauga Henry Noble Summit

<!-- b000325 | caption | pages [14] -->
Figure 15: Counties in Crisis by 2017

<!-- b000326 | prose | pages [14] -->
The results for 2018 is in the appendix. The opioid incidents are increasing in total in high speed. In some area, the number may increase by thousands. However, we also notice a decline in prediction in some area from 2018-2019, these areas are shown in the chart below:

<!-- b000327 | prose | pages [14] -->
Kentucky Clark Ballard Fayette Madison Menifee Powell Trimble

<!-- b000328 | caption | pages [14] -->
Figure 16: Counties Possibly in Crisis variation from 2018-2019

<!-- b000329 | furniture | pages [15] -->
Team # 1906204

<!-- b000330 | furniture | pages [15] -->
Page 13 of 38

<!-- b000331 | heading | pages [15] -->
3.6.2 Analysis

<!-- b000332 | prose | pages [15] -->
In the result derived from our model, we can see decline in some area, but increasing opioid incidents in total. Opioid abuse problem are getting more severe in areas that are already facing opioid crisis. Counties in risk of getting opioid problem does not match with counties where opioid drugs started to spread. However, counties around counties where opioid drugs started to spread tend to have an increase in the number of opioid incidents. According to our estimation, area far from other area with drug problem are declining in ﬁgure. So we may draw to the conclusion that opioid problems appear to be regional. Apart from this, we also notice that areas around lake and seas have more severe opioid problem. This may caused by the denser population in these counties. More opioid incidents occur in larger crowd, denser population also makes drugs spread easier.

<!-- b000333 | caption | pages [15] -->
Figure 17: Drug Incidents Report Variation 2010-2017

<!-- b000334 | prose | pages [15] -->
From the historical data, we can see a similar trend, drug problems are getting more severe in areas already facing drug problems. It is also happening in area with more people.

<!-- b000335 | heading | pages [15] -->
3.7 Choosing Factors: Using the U.S. Census socio-economic data

<!-- b000336 | prose | pages [15] -->
Here we use the U.S. Census socio-economic data set in question to select factors that are highly relevant to opioids. Due to the large amount of data, it is difﬁcult to manually select features. So here we use machine learning algorithms to automate the selection of factors. We go through three steps to output the ﬁnal ex- tracted features. In the ﬁrst step we used the association rule learning algorithm to select the demographic characteristics associated with opioids. In the second part, we used the characteristics obtained in the ﬁrst step to ﬁnd out the factors positively related to the growth of opioids through correlation analysis. Since the data dimension in the second part is still very large, in the third step we use the PCA algorithm to reduce the dimensionality of the data obtained in the second step. We use the multidimensional vector output in the third step as the ﬁnal feature.

<!-- b000337 | heading | pages [15] -->
3.7.1 Association rule learning: Apriori

<!-- b000338 | prose | pages [15] -->
Association rule learning is a rule-based machine learning method for discovering interesting relations be- tween variables in large databases. It is intended to identify strong rules discovered in databases using some measures of interestingness. Association rule learning is ﬁrst applied for discovering regularities between products in large-scale transaction data recorded by point-of-sale systems in supermarkets. For example, the rule {bread, tea –> milk} found in the sales data of a supermarket would indicate that if a customer buys bread and tea together, they are likely to also buy milk.

<!-- b000339 | prose | pages [15, 16] -->
Finding relationships between opioids and demographics can also be addressed using a association rule learning. Here we imagine each city as a ’shopping basket’. Every demographic can be regarded as a commodity. We also add the quantity information of opioids to the ’shopping basket’, and our problem is transformed into ,When the customer buys which kinds of goods, he has a high probability to buy ’opioid goods’, that is to say, looking for which kind of demographic characteristices of a city obsess, the city’s crimes about opioids will rise sharply.

<!-- b000340 | furniture | pages [16] -->
Team # 1906204

<!-- b000341 | furniture | pages [16] -->
Page 14 of 38

<!-- b000343 | prose | pages [16] -->
First step data preprocessing. Since our association rule learning algorithm requires input as a Boolean form, and our data is in a continuous form, here we ﬁrst convert the data in the database into a Boolean form. Since each demographic has four types of data(HCxx_VC01, HCxx_VC02,HCxx_VC03, HCxx_VC04), here we use data in percentage form(HCxx_VC03)to eliminate the effects of different urban populations. Then we use the Kmeans algorithm to divide each demographic feature into two categories, and ﬁnally generate a new Boolean data table.

<!-- b000344 | prose | pages [16] -->
Fators HC03_VC04 HC03_VC06 HC03_VC07 HC03_VC08 HC03_VC09 ... DRUG ID 21001 0 1 0 0 0 ... 1 21003 0 0 0 0 1 ... 0 21005 0 1 0 0 0 ... 0 21007 0 0 0 0 1 ... 1 ... ... ... ... ... ... ... ...

<!-- b000345 | caption | pages [16] -->
Table 1: Data preprocessing instance, numerical Booleanization

<!-- b000346 | prose | pages [16] -->
The second step is to establish a formulaic description.Let I = {i1, i2, . . . , in} be a set of n binary at- tributes called items.Here I = {HC03_V C04, HC03_V C06, HC03_V C07, HC03_V C10, ...DRUG} . Let D = {t1, t2, . . . , tm} be a set of transactions called the database. Here D = {21001, 21003, 21005, ...} Each transaction in D has a unique transaction ID and contains a subset of the items in I. A rule is deﬁned as an implication of the form:

<!-- b000347 | prose | pages [16] -->
X ⇒Y, where X, Y ⊆I

<!-- b000348 | prose | pages [16] -->
Every rule is composed by two different sets of items, also known as itemsets, X and Y, where X is called antecedent or left-hand-side (LHS) andY consequent or right-hand-side (RHS).In order to select interesting rules from the set of all possible rules, constraints on various measures of signiﬁcance and interest are used. Here we use minimum thresholds on support and conﬁdence method, we ﬁrst need to deﬁne the deﬁnition of support and conﬁdence. The support of X with respect to T is deﬁned as the proportion of transactions t in the dataset which contains the itemset X.

<!-- b000349 | prose | pages [16] -->
supp(X) = |{t ∈T; X ⊆t}| |T|

<!-- b000350 | prose | pages [16] -->
Conﬁdence is an indication of how often the rule has been found to be true.The conﬁdence value of a rule,X ⇒Y , with respect to a set of transactions T, is the proportion of the transactions that containsX which also contains Y.Conﬁdence is deﬁned as:

<!-- b000351 | prose | pages [16] -->
conf(X ⇒Y ) = supp(X ∪Y ) supp(X)

<!-- b000352 | prose | pages [16] -->
The lift of a rule is deﬁned as: supp(X ∪Y ) lift(X ⇒Y ) = supp(X) × supp(Y )

<!-- b000353 | prose | pages [16] -->
If the lift is > 1, that lets us know the degree to which those two occurrences are dependent on one another, and makes those rules potentially useful for predicting the consequent in future data sets.This represents the greater lift, the stronger the credibility of the association rules.

<!-- b000354 | prose | pages [16] -->
The third step is to ﬁnd the association rules related to opioids.We use the Apriori algorithm to ﬁnd fre- quent sets.Then use the frequent itemset to construct a rule that satisﬁes the minimum trust of the user.The speciﬁc method of Apriori algorithm is: ﬁrst ﬁnd out the frequent 1-item set, denoted as L1; then use L1 to generate candidate set C2, and judge the items in C2 to mine L2, which is frequent 2-item set; Loop until you can’t ﬁnd more frequent k-items. Every time you dig a layer of Lk, you need to scan the entire database.The algorithm utilizes the Apriori principle:

<!-- b000355 | furniture | pages [17] -->
Team # 1906204

<!-- b000356 | furniture | pages [17] -->
Page 15 of 38

<!-- b000357 | prose | pages [17] -->
• An item set is frequent, then all its subsets are also frequent

<!-- b000358 | prose | pages [17] -->
• If an item set is an infrequent item set, then all its supersets are also infrequent itemsets

<!-- b000359 | prose | pages [17] -->
Using this principle, you can avoid exponential growth in the number of itemsets, thus calculating frequent itemsets in a reasonable amount of time.

<!-- b000360 | prose | pages [17] -->
1. Calculate the single element set: Init Init 1 2 3 4 5

<!-- b000361 | prose | pages [17] -->
3 3 2. Shave the elements that do not meet 0 1 2 0 1 2 the minimum support:

<!-- b000362 | prose | pages [17] -->
1 2 4 5 13 13 12 23 12 23 01 02 03 01 02 03 3. Calculate the two-element collection:

<!-- b000363 | prose | pages [17] -->
4. Shave the elements that do not meet the minimum support:

<!-- b000364 | prose | pages [17] -->
012 012 013 013 123 123 023 023 1 2 3 3 5 3 2 5

<!-- b000365 | prose | pages [17] -->
5. .... repeat the above steps until the collection 0123 0123 element contains all the single elements 6. Get the ﬁnal frequent set

<!-- b000366 | prose | pages [17] -->
Apriori principle Apriori algorithm

<!-- b000367 | caption | pages [17] -->
Figure 18: Aporior principle and Aporiori algorithm

<!-- b000368 | prose | pages [17] -->
In the ﬁgure we can see that the known gray part {2,3} is a non-frequent item set, then with the above knowledge, we can know {0,2,3} {1,2,3} {0,1 , 2, 3} are all infrequent. In other words, after calculating the support of {2,3}, knowing that it is infrequent, you do not need to calculate {0,2,3} {1,2,3} {0,1,2,3} Support because we know that these collections will not meet our requirements.Below we generate association rules based on frequent itemsets. As with our previous frequent item set generation, we can generate many asso- ciation rules for each frequent item set. If you can reduce the number of rules to ensure that the problem is resolvable, then the calculation will be much better. By observing, we can know that if a rule does not meet the minimum credibility requirement, then all subsets of the rule will not meet the minimum credibility requirement. The above property attributes of the association rules can be utilized to reduce the number of rules that need to be tested, just like the previous Apriori algorithm.

<!-- b000369 | prose | pages [17] -->
The fourth part produced the ﬁnal factor that had the greatest impact on the spread of opioids.Since it is unrealistic to run the Apriori algorithm directly on all facotrs, here we divide the data in the table into 16 categories,and run the Apriori algorithm for each category, and the ﬁnal result is .

<!-- b000370 | prose | pages [17] -->
1 2 3 4 HOUSEHOLDS HC03_VC11 HC03_VC09 HC03_VC12 HC03_VC07 RELATIONSHIP HC03_VC31 HC03_VC30 HC03_VC25 MARITAL HC03_VC35 HC03_VC42 HC03_VC45 HC03_VC38 GRANDPARENTS HC03_VC67 HC03_VC64 HC03_VC65 EDUCATIONAL HC03_VC91 HC03_VC89 HC03_VC88 RESIDENCE HC03_VC120 HC03_VC123 HC03_VC122 BIRTH PLACE HC03_VC133 HC03_VC128 LANGUAGE SPOKEN HC03_VC172 HC03_VC171 HC03_VC173 HC03_VC170 ANCESTRY HC03_VC198 HC03_VC185 HC03_VC194 HC03_VC182 YEAR OF ENTRY HC03_VC146 HC03_VC150 HC03_VC144

<!-- b000371 | caption | pages [17] -->
Table 2: Factor that may had the greatest impact on the spread of opioids

<!-- b000372 | prose | pages [17] -->
After analyzing the data, we conclude that the following groups may be more inclined to abuse opioids.

<!-- b000373 | furniture | pages [18] -->
Team # 1906204

<!-- b000374 | furniture | pages [18] -->
Page 16 of 38

<!-- b000375 | prose | pages [18] -->
People type ID HC03_VC11 Female_householder_no_husband_present HC03_VC09 Male_householder_no_wife_present HC03_VC35 Males_15_years_and_over HC03_VC45 Separated HC03_VC67 Responsible_for_grandchildren_5_or_more_years HC03_VC88 Some_college_no_degree HC03_VC89 Associate’s_degree HC03_VC172 Language_other_than_Spanish HC03_VC170 Speak_English_less_than_"very_well"

<!-- b000376 | caption | pages [18] -->
Table 3: Groups may be more inclined to abuse opioids.

<!-- b000377 | heading | pages [18] -->
3.7.2 Correlation Analysis

<!-- b000378 | prose | pages [18] -->
Given several possible inﬂuencing factors, we still have to determine whether these factors are has positive correlation or negative correlation, so we still needs to calculate correlation between several ﬁltered factors and opioid incidents during 2010-2017 years. Here we use Pearson correlation coefﬁcient, given by:

<!-- b000379 | prose | pages [18] -->
E[XY ] −E[X]E[Y ] ρX,Y = p E [X2] −[E[X]]2p E [Y 2] −[E[Y ]]2

<!-- b000380 | prose | pages [18] -->
In consider with counties, we do autocorrelation to observer if the plot was smooth. It indicates whether there are too many variations in correlations. Here we assume 0.8 as strong correlated, calculate the number of |corr| > 0.8 to testify positive correlated or negative correlated. We chose three factors as most important factors inﬂuencing opioid usage:

<!-- b000381 | prose | pages [18] -->
Households with one or more people 65 years and over Graduate or professional degree Family households (families) - Female householder, no husband present, family

<!-- b000382 | heading | pages [18] -->
3.7.3 PCA Feature Extraction

<!-- b000383 | prose | pages [18] -->
Three features are selected, however still too large for input for model introduced above. So we use PCA to project three features into one line. PCA calculate the covariance matrix of the data matrix, and then obtaining the eigenvalue eigenvectors of the covariance matrix, the matrix composed of the eigenvectors corresponding to the k features with the largest eigenvalue is selected. In this way, the data matrix can be transformed into a new space to achieve dimensionality reduction. We used SVD to implement PCA, the result was reduced to a n*1 matrix and applied to our model

<!-- b000384 | heading | pages [18] -->
4 Strategy for Countering Opioid Crisis

<!-- b000385 | prose | pages [18] -->
As the results from above model, three critical factors in opioid crisis are (1) the percentage of female householder without husband; (2) The percentage of people with advanced education level; (3) percentages of households with one or more people 65 years and over.

<!-- b000386 | heading | pages [18] -->
4.1 Brief Explanation for Factors

<!-- b000387 | prose | pages [18, 19] -->
• Factor(1): Divorce or the death of a partner can trigger women’s substance use or other mental health disorders. A female householder would bear much more burden of life and face more social pressure, if they could’t get support from their companions. In addition, women, different from men, have a higher possibility to be addicted to opioid drug duo to physiological factors, such as sex hormone, etc.

<!-- b000388 | furniture | pages [19] -->
Team # 1906204

<!-- b000389 | furniture | pages [19] -->
Page 17 of 38

<!-- b000391 | prose | pages [19] -->
• Factor(2): People with high education level are less likely to be addicted to opioid drugs. Although they may also face much work and social pressure, they can adjust them to adapt to it and education can make people aware of the danger of opioid drug and help them prevent addiction to opioid drugs.

<!-- b000392 | prose | pages [19] -->
• Factor(3): The elder people are more likely to suffer both physical and mental illness. Drug treatment become a crucial way to alleviate symptoms and manage pain. Similarly, long-term treatment may trigger same addiction occurred in the elder, especially for those elder people who have lost their children or lack of care from their sons or daughters.

<!-- b000393 | heading | pages [19] -->
4.2 Possible Strategies

<!-- b000394 | prose | pages [19] -->
Opioid are always considered as drug not too harmful, cheap and easy to get, to reduce usage of Opioid, there are several things federal government can do.

<!-- b000395 | heading | pages [19] -->
4.2.1 For the Elder

<!-- b000396 | prose | pages [19] -->
Elder people is a key factor inﬂuencing Opioid abuse problem. Opioid drugs are widely used for medi- cal usages to reduce pain, these kind of drugs are especially reachable for the elder. Besides, doctors are not restricted in providing patients opioid painkillers, some elder people use opioid painkillers too often and get addicted. Government can restrict doctors of providing opioid drugs or encourage pharmaceuti- cal factories to produce inexpensive, effective painkiller in replace of opioids. Government can organize community nursing homes to help these elder people ﬁnd companions. Common interests and hobbies are beneﬁcial to their psychological and physical health.

<!-- b000397 | heading | pages [19] -->
4.2.2 About Education Level

<!-- b000398 | prose | pages [19] -->
Our model shows that higher education level may reduce usage of opioids. Educated people tend to avoid using drugs considering the risk of damaging their social status. Government can provide more opportuni- ties for citizens to enroll in colleges, such as offering scholarship or starting community college. Education about drug abuse in communities are also important. Some promotional slogans about knowledge of opi- oids can be attached billboard in communities or even attached to the packages of opioid drugs.

<!-- b000399 | heading | pages [19] -->
4.2.3 For Female Householder Without Husband

<!-- b000400 | prose | pages [19] -->
Females are sometimes ignored in researches on medicine. Some medicine may have different inﬂuence on female, for example, easier to get addicted. Apart from this, female householders without husband are mostly under greater pressure. They are more likely to use drugs to release pressure. Government can supervise pharmaceutical factories to consider more about female during research and development. Governments can also provide job opportunities and welfare for female householders without husbands. Community staff members should visit those female householder more frequently, not only care about their physical health but also care about their mental health.

<!-- b000401 | heading | pages [19] -->
4.2.4 Considering Other Factors

<!-- b000402 | prose | pages [19] -->
• Laws varies among states, from drug spread diagram, most opioids are spread from Ohio and Vir- ginia, laws in these two states are more tolerant to drugs. Stricter law should be made to restrict opioid production and trade.

<!-- b000403 | prose | pages [19] -->
• From drug spread diagram, opioids spread easier in area with developed trafﬁc, for example, adjacent to coast. Stocks in transportation can be checked in a stricter way.

<!-- b000404 | furniture | pages [20] -->
Team # 1906204

<!-- b000405 | furniture | pages [20] -->
Page 18 of 38

<!-- b000406 | heading | pages [20] -->
4.3 Strategies Veriﬁcation

<!-- b000407 | prose | pages [20] -->
All the strategies above are aimed to decrease inﬂuence from opioid drug on these groups. In our model, we consider the factor as ﬁxed that a speciﬁc group is affected by opioid drug. An equivalent way to verify our strategy is to decrease the percentage of corresponding group. In reality, we can’t actually "decrease" its percentage, but the "decrease" here serves the same purpose as lower the inﬂuence factor for speciﬁc group.

<!-- b000408 | heading | pages [20] -->
4.3.1 Validation for Equivalent Veriﬁcation

<!-- b000409 | prose | pages [20] -->
Suppose there are k kinds of groups in total. Let {α1, α2, ..., αk} represents the proportion of each group to the total population. Let {β1, β2, ..., βk} represents the proportion of opioid addicted people in i’th group to the total population of that group. Let S be the number of total population. Then the origin total addicted people accounts for,

<!-- b000410 | prose | pages [20] -->
k X OriginTotal = S × (α1β1 + α2β2 + ... + αkβk) = S αiβi i=1

<!-- b000411 | prose | pages [20] -->
Now we use strategy to decrease the βi, however, βi is not speciﬁc in our model because we can’t ﬁgure it out based on our current information. To verify our strategy, one reasonable way is to decrease αi to reach the same purpose. Assume our strategy decreases βj to β′ j. Now we try to ﬁgure out new α′ j based on our equivalence idea. The total addicted people after strategy is implemented is,

<!-- b000412 | prose | pages [20] -->
NewTotal = S × (α1β1 + α2β2 + ... + αjβ′ j + ... + αkβk) k (1) X αiβj + Sαjβ′ = S j i=1,i̸=j

<!-- b000413 | prose | pages [20] -->
Then we ﬁx βj, set αj to α′ j and keep other parameter unchanged. As a result, the total addicted are decreased by S(αj −α′ j), denoted by S’. The new total addicted people can be calculated as,

<!-- b000414 | prose | pages [20] -->
NewTotal = S′ × (α1β1 + α2β2 + ... + α′ jβj + ... + αkβk) k (2) X = S′ αiβj + S′α′ jβj i=1,i̸=j

<!-- b000415 | prose | pages [20] -->
According to equation (1) and (2) above, for simplicity, we assume S ≈S′ and in order to make the assump- tion reasonable, our model can’t verify when ∆α = αj −α′ j is large. Temporarily, we make assumption satisﬁed, then k k X X αiβj + Sαjβ′ j = S′ αiβj + S′α′ S jβj i=1,i̸=j i=1,i̸=j

<!-- b000416 | prose | pages [20] -->
β′ so we get, α′ j i = αj βj . In practice, if a strategy can decrease a factor β by 20 percents, that strategy is said very successful(So it is reasonable and practical to assume the β will decrease by k percents, where k is smaller than 20). Since the α for the main factors are 12%, 8% and 27% percents, respectively. We can change αi at most 2.4%, 1.6% and 4$ percents, correspondingly. Thus, we can roughly say S ≈S′ because the changes are acceptably small.

<!-- b000417 | heading | pages [20] -->
4.3.2 Veriﬁcation Results

<!-- b000418 | prose | pages [20, 21] -->
The following table shows the results, Factor ≥65 years older householder female householder people with advanced degree Total Decrease Rate Level origin level 12% 8.0% 27% 0% adjusted level 12% 8.0% 26% 0.34% adjusted level 12% 8.0% 25% 1.33% adjusted level 12% 8.0% 24% 2.57%

<!-- b000419 | furniture | pages [21] -->
Team # 1906204

<!-- b000420 | furniture | pages [21] -->
Page 19 of 38

<!-- b000421 | caption | pages [21] -->
Figure 19: Strategy A Tests for zone 88

<!-- b000423 | caption | pages [21] -->
Figure 20: Strategy B Tests for zone 88

<!-- b000424 | prose | pages [21] -->
Factor ≥65 years older householder female householder people with advanced degree Total Drug Reports Level origin level 12% 8.0% 27% 0% adjusted level 11.2% 8.0% 27% 0.43% adjusted level 10.4% 8.0% 27% 1.17% adjusted level 9.6% 8.0% 27% 2.11%

<!-- b000425 | caption | pages [21] -->
Figure 21: Strategy C Tests for zone 88

<!-- b000426 | prose | pages [21] -->
Factor ≥65 years older householder female householder people with advanced degree Total Drug Reports Level origin level 12% 8.0% 27% 0% adjusted level 12% 8.5% 27% 0.15% adjusted level 12% 9.0% 27% 0.34% adjusted level 12% 9.5% 27% 0.71%

<!-- b000427 | prose | pages [21] -->
Note: Zone 88 consists of CAMPBELL, BUTLER, CALDWELL and KENTON. All 4 counties locate in Kentucky.

<!-- b000428 | heading | pages [21] -->
4.3.3 Findings

<!-- b000429 | prose | pages [21] -->
The above results show that special attention should be attached to female householders without husband and 65 years and more older householders. These two special groups are the main parts in this opioid crisis and strategies focusing on them should be taken into account carefully. Education also plays a crucial role in this opioid crisis, improving people’s overall education level can help the United States go through this opioid crisis.

<!-- b000430 | heading | pages [21] -->
5 Model Analysis

<!-- b000431 | prose | pages [21] -->
Although we think our model is better than most existing models, but it still has some weakness to notice.

<!-- b000432 | prose | pages [21] -->
• When considering graphical location inﬂuence, we set inﬂuence radius to 200km based on life expe- rience, which is not speciﬁc enough. However, we haven’t found an efﬁcient way to ﬁgure out which radius is most suitable.

<!-- b000433 | prose | pages [21] -->
• When considering time inﬂuence, our attempt is to make latest tendency have more impact than previous ones. However, determining time decay factor is another difﬁcult problem that we haven’t solved in such short time.

<!-- b000434 | prose | pages [21] -->
• Based on our correlation analysis, there are many inﬂuence factors behind this opioid crisis. However, our regression model is not accurate enough for high dimension data. In practice, we consider three main inﬂuence factors to train our model to predict at the same time. If possible, we should invoke more factors to analyze simultaneously.

<!-- b000435 | furniture | pages [22] -->
Team # 1906204

<!-- b000436 | furniture | pages [22] -->
Page 20 of 38

<!-- b000437 | heading | pages [22] -->
References

<!-- b000438 | references | pages [22] -->
[1] https://www.drugabuse.gov/publications/drugfacts/substance-use-in-women

<!-- b000439 | references | pages [22] -->
1

<!-- b000440 | references | pages [22] -->
2

<!-- b000441 | references | pages [22] -->
[2] Bernhard SchÃ˝ulkopf, Williamson, R. C. , Smola, A. J. , Shawe-Taylor, J. , & Platt, J. C. . (1999). Support

<!-- b000442 | references | pages [22] -->
Vector Method for Novelty Detection. Advances in Neural Information Processing Systems 12, [NIPS

<!-- b000443 | references | pages [22] -->
Conference, Denver, Colorado, USA, November 29 - December 4, 1999]. MIT Press.

<!-- b000444 | references | pages [22] -->
3

<!-- b000445 | references | pages [22] -->
[3] Jogi. Suresh1, T. R. (2013). Mining frequent itemsets using apriori algorithm. International Journal of

<!-- b000446 | references | pages [22] -->
Computer Trends & Technology, 4(4).

<!-- b000447 | references | pages [22] -->
4

<!-- b000448 | references | pages [22] -->
[4] Hands-on machine learning with Scikit-Learn & tensorﬂow

<!-- b000449 | references | pages [22] -->
5

<!-- b000450 | references | pages [22] -->
[5] Fouss, F. , Pirotte, A. , Renders, J. M. , & Saerens, M. . (2007). Random-walk computation of similarities

<!-- b000451 | references | pages [22] -->
between nodes of a graph with application to collaborative recommendation. IEEE Transactions on

<!-- b000452 | references | pages [22] -->
Knowledge and Data Engineering, 19(3), 355-369.

<!-- b000453 | references | pages [22] -->
6

<!-- b000454 | references | pages [22] -->
[6] Recht, B. . (2009). A simpler approach to matrix completion. Journal of Machine Learning Research.

<!-- b000455 | references | pages [22] -->
7

<!-- b000456 | references | pages [22] -->
[7] Castroneto, M. , Jeong, Y. S. , Jeong, M. K. , & Han, L. D. . (2009). Online-svr for short-term trafﬁc

<!-- b000457 | references | pages [22] -->
ﬂow prediction under typical and atypical trafﬁc conditions. Expert Systems with Applications An

<!-- b000458 | references | pages [22] -->
International Journal, 36(3), 6164-6173.

<!-- b000459 | references | pages [22] -->
8

<!-- b000460 | references | pages [22] -->
[8] Lin, M. Y. , Lee, P. Y. , & Hsueh, S. C. . (2012). Apriori-based frequent itemset mining algorithms on

<!-- b000461 | references | pages [22] -->
MapReduce. International Conference on Ubiquitous Information Management & Communication.

<!-- b000462 | references | pages [22] -->
ACM.

<!-- b000463 | furniture | pages [23] -->
Team # 1906204

<!-- b000464 | furniture | pages [23] -->
Page 21 of 38

<!-- b000465 | heading | pages [23] -->
6 Memo

<!-- b000466 | heading | pages [23] -->
6.1 Origin of the Opioid Drug Abuse

<!-- b000467 | prose | pages [23] -->
From origin of the opioid drug abuse we can analyze many interesting phenomena. The origin of most opioids is concentrated and concentrated in Ohio and Virginia. There may be many factors that contribute to the characteristics of this distribution. We mainly analyze trafﬁc characteristics and legal characteristics.

<!-- b000468 | prose | pages [23] -->
Trafﬁc factors:We can see the source of a lot of opioids near the ocean, or near the Great Lakes. The prox- imity to the ocean has made it easier to import illegal drugs or opioids from abroad, making these areas a source of numerous opioids.

<!-- b000469 | prose | pages [23] -->
Legal factors:We can see that Ohio is the source of many drugs. The reason for this situation may be related to the fact that local laws and regulations still have loopholes and the government’s supervision is not strong.

<!-- b000470 | heading | pages [23] -->
6.2 Prediction of Opioid Abuse Distribution

<!-- b000471 | prose | pages [23] -->
According to our prediction, opioid abuse decline in some area, but increasing in total. Opioid abuse problem are getting more severe in areas that are already facing opioid crisis and areas adjacent.Most part of Ohio, east coast of Kentucky and west coast of Virginia, Pennsylvania are at the threat of opioid crisis.

<!-- b000472 | caption | pages [23] -->
Figure 22: Prediction Opioid Reports 2018

<!-- b000473 | caption | pages [23] -->
Figure 23: Prediction Opioid Reports 2019

<!-- b000474 | heading | pages [23] -->
6.3 Correlated Factors

<!-- b000475 | prose | pages [23] -->
From our observation, Elder people, female household without husbands are related to the increase of opioid abuse. Education also plays a crucial role in opioid crisis.

<!-- b000476 | prose | pages [23] -->
People type ID HC03_VC11 Female_householder_no_husband_present HC03_VC09 Male_householder_no_wife_present HC03_VC35 Males_15_years_and_over HC03_VC45 Separated HC03_VC67 Responsible_for_grandchildren_5_or_more_years HC03_VC88 Some_college_no_degree HC03_VC89 Associate’s_degree HC03_VC172 Language_other_than_Spanish HC03_VC170 Speak_English_less_than_"very_well"

<!-- b000477 | caption | pages [23] -->
Table 4: Groups may be more inclined to abuse opioids.

<!-- b000478 | furniture | pages [24] -->
Team # 1906204

<!-- b000479 | furniture | pages [24] -->
Page 22 of 38

<!-- b000480 | heading | pages [24] -->
6.4 Strategies

<!-- b000481 | heading | pages [24] -->
6.4.1 For Elder

<!-- b000482 | prose | pages [24] -->
Government can restrict doctors of providing opioid drugs or encourage pharmaceutical factories to pro- duce inexpensive, effective painkiller in replace of opioids, making elder people less likely to access opioid drugs and use alternative medicine to treat illness. Government can organize community nursing homes to help these elder people to ﬁnd companions. Common interests and hobbies are beneﬁcial to their psy- chological and physical health.

<!-- b000483 | heading | pages [24] -->
6.4.2 About Education Level

<!-- b000484 | prose | pages [24] -->
Government can provide more opportunities for citizens to enroll in colleges, such as offering scholarship or starting community college. Education about drug abuse in communities are also important. Some pro- motional slogans about knowledge of opioids can be attached billboard in communities or even attached to the packages of opioid drugs.

<!-- b000485 | heading | pages [24] -->
6.4.3 For Female Householder Without Husband

<!-- b000486 | prose | pages [24] -->
Government can supervise pharmaceutical factories to consider more about female during research and development. Governments can also provide job opportunities and welfare for female householders with- out husbands. Community staff members should visit those female householder more frequently, not only care about their physical health but also care about their mental health.

<!-- b000487 | heading | pages [24] -->
6.4.4 Considering Other Factors

<!-- b000488 | prose | pages [24] -->
• Laws varies among states, from drug spread diagram, most opioids are spread from Ohio and Vir- ginia, laws in these two states are more tolerant to drugs. Stricter law should be made to restrict opioid production and trade.

<!-- b000489 | prose | pages [24] -->
• From drug spread diagram, opioids spread easier in area with developed trafﬁc, for example, adjacent to coast. Stocks in transportation can be checked in a stricter way.

<!-- b000490 | prose | pages [24] -->
Dihydrocodeine Butorphanol ANPP MT-45 Levorphanol Opium Alphaprodine Desmethylprodine 4-Fluoroisobutyryl fentanyl Remifentanil Acetyl fentanyl p-Fluorobutyryl fentanyl Fluorofentanyl U-47700 3-Methylfentanyl 3-Fluorofentanyl Phenyl fentanyl Cyclopropyl fentanyl Methoxyacetyl fentanyl U-48800 Benzylfentanyl U-51754 Crotonyl fentanyl Cyclopropyl/Crotonyl Fentanyl Cyclopentyl fentanyl 4-Methylfentanyl Metazocine'

<!-- b000491 | prose | pages [24] -->
Origin of drugs

<!-- b000492 | prose | pages [24] -->
Drugs’name Drug...

<!-- b000493 | prose | pages [24] -->
Dextropropoxyphene Oxymorphone Fentanyl Morphine Oxycodone Meperidine Tramadol Heroin Pentazocine Propoxyphene Methadone Hydromorphone Opiates Buprenorphine Hydrocodone Codeine

<!-- b000494 | prose | pages [24] -->
Methorphan

<!-- b000495 | prose | pages [24] -->
Pethidine Mitragynine Acetyldihydrocodeine Hydrocodeinone Furanyl fentanyl Carfentanil Acryl fentanyl trans-3-Methylfentanyl p-methoxybutyryl fentanyl p-Fluorofentanyl o-Fluorofentanyl Furanyl/3-Furanyl fentanyl U-49900 3,4-Methylenedioxy U-47700 Isobutyryl fentanyl

<!-- b000496 | caption | pages [24] -->
Figure 24: Origin of all opioids

<!-- b000497 | furniture | pages [25] -->
Team # 1906204

<!-- b000498 | furniture | pages [25] -->
Page 23 of 38

<!-- b000499 | heading | pages [25] -->
Appendices

<!-- b000500 | prose | pages [25] -->
Here are programmes we used in our model.

<!-- b000501 | heading | pages [25] -->
Data preprocessing, Kmeans algorithm

<!-- b000502 | prose | pages [25] -->
import xlrd import pandas as pd import numpy as np from math import radians, cos, sin, asin, sqrt import xlwt import operator import copy from functools import reduce

<!-- b000503 | prose | pages [25] -->
# initialize def init(table):

<!-- b000504 | prose | pages [25] -->
nrows = table.nrows ncols = table.ncols # use FIPS_combined as key to record info county = {} for i in range(1, nrows):

<!-- b000505 | prose | pages [25] -->
FIPS_Combined = table.row_values(i)[6] if FIPS_Combined not in county.keys():

<!-- b000506 | prose | pages [25] -->
lat = table.row_values(i)[12] lon = table.row_values(i)[13] county[FIPS_Combined] = (lon, lat) return county

<!-- b000507 | prose | pages [25] -->
def haversine(pos1, pos2):

<!-- b000508 | prose | pages [25] -->
""" Calculate the great circle distance between two points on the earth (specified in decimal degrees) """ # convert decimal into arc system lon1, lat1 = pos1 lon2, lat2 = pos2 lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

<!-- b000509 | prose | pages [25] -->
# haversine formula dlon = lon2 - lon1 dlat = lat2 - lat1 a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 c = 2 * asin(sqrt(a)) r = 6371 # radius of earth, unit as kilometer return c * r * 1000

<!-- b000510 | prose | pages [25] -->
def renew_cluster(centers, pos, cities):

<!-- b000511 | prose | pages [25] -->
label = dict().fromkeys([i for i in range(len(centers))], []) for city in cities:

<!-- b000512 | prose | pages [25] -->
dist = [] for center in centers:

<!-- b000513 | prose | pages [25] -->
dist.append(haversine(pos[city], center)) index = dist.index(min(dist)) cluster = copy.deepcopy(label[index]) cluster.append(city) label[index] = cluster new_centers = []

<!-- b000514 | prose | pages [25] -->
for i in range(len(centers)):

<!-- b000515 | prose | pages [25] -->
positions = list(map(lambda x: pos[x], label[i])) new_centers.append(np.mean(positions, axis=0)) return new_centers, label

<!-- b000516 | prose | pages [25] -->
# convert positions into k clusters def k_means(k, pos):

<!-- b000517 | prose | pages [25] -->
cities = list(pos.keys()) if k > len(cities):

<!-- b000518 | furniture | pages [26] -->
Team # 1906204

<!-- b000519 | furniture | pages [26] -->
Page 24 of 38

<!-- b000520 | prose | pages [26] -->
print("K too large") return False else:

<!-- b000521 | prose | pages [26] -->
# initial centers old_centers = [list(pos[cities[i]]) for i in range(k)] new_centers = [] # itartion until convergence while True:

<!-- b000522 | prose | pages [26] -->
new_centers, cluster = renew_cluster(old_centers, pos, cities) # print(new_centers) break; if (np.array(new_centers) == np.array(old_centers)).all():

<!-- b000523 | prose | pages [26] -->
break else:

<!-- b000524 | prose | pages [26] -->
old_centers = new_centers

<!-- b000525 | prose | pages [26] -->
zone = {} for key in cluster:

<!-- b000526 | prose | pages [26] -->
for city in cluster[key]:

<!-- b000527 | prose | pages [26] -->
zone[city] = key return new_centers, cluster, zone

<!-- b000528 | prose | pages [26] -->
def output(centers, cluster, zone, data):

<!-- b000529 | prose | pages [26] -->
# new_file = xlwt.Workbook(encoding = ’utf-8’) # new_table = file.add_sheet(’data’)

<!-- b000530 | prose | pages [26] -->
table = [] for i in range(1,data.nrows):

<!-- b000531 | prose | pages [26] -->
YYYY = data.row_values(i)[1] FIPS_Combined = data.row_values(i)[6] substanceName = data.row_values(i)[7] DrugReport = data.row_values(i)[8] TotalDrugReport = data.row_values(i)[9] label = zone[FIPS_Combined] entry = [YYYY, label, substanceName, DrugReport, TotalDrugReport] table.append(entry)

<!-- b000532 | prose | pages [26] -->
# def f(x, y): # if (np.array(x[:3]) == np.array(y[:3])).all(): # return x[:3] + [x[3]+y[3]] + [x[4]+y[4]] # reduce(lambda x, y: f , table) return table

<!-- b000533 | prose | pages [26] -->
if __name__ == ’__main__’:

<!-- b000534 | prose | pages [26] -->
data = xlrd.open_workbook(’excel_output_add.xls’).sheets()[0]

<!-- b000535 | prose | pages [26] -->
county = init(data) centers, cluster, zone = k_means(100, county) table = output(centers, cluster, zone, data)

<!-- b000536 | prose | pages [26] -->
#write data into excel excel = xlwt.Workbook() sheet1 = excel.add_sheet("Date based on Zone") sheet2 = excel.add_sheet("ZoneCounty Correspondence Table") sheet3 = excel.add_sheet("County Position")

<!-- b000537 | prose | pages [26] -->
sheet1.write(0, 0, "YYYY") sheet1.write(0, 1, "Zone") sheet1.write(0, 2, "substanceName") sheet1.write(0, 3, "DrugReportZone") sheet1.write(0, 4, "TotalDrugReportZone") for row, entry in enumerate(table):

<!-- b000538 | prose | pages [26] -->
for col in range(len(entry)):

<!-- b000539 | prose | pages [26] -->
sheet1.write(row+1, col, entry[col])

<!-- b000540 | prose | pages [26, 27] -->
sheet2.write(0, 0, "Zone") sheet2.write(0, 1, "Latitude") sheet2.write(0, 2, "Longitude") for row, key in enumerate(list(cluster.keys())):

<!-- b000541 | furniture | pages [27] -->
Team # 1906204

<!-- b000542 | furniture | pages [27] -->
Page 25 of 38

<!-- b000544 | prose | pages [27] -->
sheet2.write(row+1, 0, row) sheet2.write(row+1, 1, centers[row][1]) sheet2.write(row+1, 2, centers[row][0]) for col in range(len(cluster[key])):

<!-- b000545 | prose | pages [27] -->
sheet2.write(row+1, col+3, cluster[key][col]) sheet3.write(0, 0, "County") sheet3.write(0, 1, "FIS_Combined") sheet3.write(0, 2, "Latitude") sheet3.write(0, 3, "Longitude") written = [] row_num = 0 for row in range(1, data.nrows):

<!-- b000546 | prose | pages [27] -->
entry = data.row_values(row) if entry[6] not in written:

<!-- b000547 | prose | pages [27] -->
row_num += 1 written.append(entry[6]) info = [entry[6], entry[2]+’+’+entry[3], entry[12], entry[13]] for col in range(4):

<!-- b000548 | prose | pages [27] -->
sheet3.write(row_num, col, info[col])

<!-- b000549 | prose | pages [27] -->
excel.save("/Users/lsd/Desktop/code/K-means/kmeans.xls")

<!-- b000550 | prose | pages [27] -->
Looking for the source of opioids import xlrd import pandas as pd import numpy as np from math import * import xlwt import operator import copy from functools import reduce import matplotlib.pyplot as plt import matplotlib import networkx as nx from itertools import combinations from igraph import * import seaborn as sns import pylab import random sns.set_style(’darkgrid’)

<!-- b000551 | prose | pages [27] -->
def adjMatrix(medical_name, time, distance_threshold):

<!-- b000552 | prose | pages [27] -->
G=nx.DiGraph() H=nx.DiGraph() M=nx.DiGraph() excel_path = ’kmeans.xls’ klocation = pd.read_excel(excel_path, sheet_name=’ZoneCounty Correspondence Table’) kdata = pd.read_excel(excel_path, sheet_name=’Date based on Zone’) distance = pd.read_excel(’distance.xls’, sheet_name=’distance’).values simi = pd.read_excel(’similarity.xls’,sheet_name = ’sim’).values

<!-- b000553 | prose | pages [27] -->
edges = [] medical_data = kdata[(kdata[’substanceName’] == medical_name) & (kdata[’YYYY’] == time)] combins = [list(c) for c in combinations(set(medical_data[’Zone’].values.tolist()), 2)] weights = [] for i in range(len(combins)):

<!-- b000554 | prose | pages [27] -->
x = combins[i][0] y = combins[i][1] if distance[x, y] < distance_threshold:

<!-- b000555 | prose | pages [27] -->
#print(medical_data[medical_data[’Zone’] == x]) #print(medical_data[medical_data[’Zone’] == y]) if (sum(medical_data[medical_data[’Zone’] == x][’DrugReportZone’].values) >= sum(medical_data[medical_data[’Zone’] == y][’DrugReportZone’].values)):

<!-- b000556 | prose | pages [27] -->
edges.append(combins[i]) G.add_edges_from([combins[i]], weight = round(simi[combins[i][0],combins[i][1]],1)) weights.append(round(simi[combins[i][0],combins[i][1]],1)) else:

<!-- b000557 | furniture | pages [28] -->
Team # 1906204

<!-- b000558 | furniture | pages [28] -->
Page 26 of 38

<!-- b000559 | prose | pages [28] -->
combins[i].reverse() edges.append(combins[i]) #print(combins[i].reverse()) G.add_edges_from([combins[i]], weight = round(simi[combins[i][0], combins[i][1]],1)) weights.append(round(simi[combins[i][0], combins[i][1]],1)) print(edges)

<!-- b000560 | prose | pages [28] -->
degree = [[x,0] for x in range(100)] for i in range(len(edges)):

<!-- b000561 | prose | pages [28] -->
degree[edges[i][0]][1] += 1 degree.sort(key=lambda x: x[1],reverse = True) ra = random.randint(0,3) origin = degree[ra][0]

<!-- b000562 | prose | pages [28] -->
print(degree) #Draw the picture #G.add_edges_from(edges) ind = [] posi = [] for i in range(100):

<!-- b000563 | prose | pages [28] -->
ind.append(i) posi.append((klocation[’Longitude’].iloc[i], klocation[’Latitude’].iloc[i])) position = dict(zip(ind, posi))

<!-- b000564 | prose | pages [28] -->
vals = [] for i in range(100):

<!-- b000565 | prose | pages [28] -->
vals.append(int(sum(medical_data[medical_data[’Zone’] == i][’DrugReportZone’].values))) values_dic = dict(zip(ind, vals)) values = [values_dic.get(node, 1.0) for node in G.nodes()] for i in range(len(values)):

<!-- b000566 | prose | pages [28] -->
values[i] = values[i] - 10 if (values[i] > 210):

<!-- b000567 | prose | pages [28] -->
values[i] = 210 edge_labels=dict([((u,v,),d[’weight’]) for u,v,d in G.edges(data=True)]) plt.figure() nx.draw_networkx_edge_labels(G,pos = position ,edge_labels=edge_labels) #nx.draw_networkx_edges(G, pos = position, width = 2, alpha = 0.5, arrows = True, arrowstyle=’->’,e nx.draw(G, pos = position, node_color = "skyblue", node_size = 2000, edge_cmp = plt.cm.Blues, with_labels=True) fig = matplotlib.pyplot.gcf() fig.set_size_inches(40, 20) plt.savefig("./FIG/"+ str(medical_name) + ’_’ + str(time) + "_" + "0.pdf") # save as png #flow_value = nx.shortest_path(G, 41, 32) #pos=nx.spring_layout(G) # positions for all nodes #nx.draw_networkx_nodes(G,pos = position,cmap=plt.get_cmap(’jet’), node_size=500, node_color=values #nx.draw_networkx_edge_labels(G,pos = position ,edge_labels=edge_labels) plt.figure() #nx.draw_networkx_nodes(G,pos = position,cmap=plt.get_cmap(’jet’), node_size=1000, node_shape="o", #nx.draw_networkx_edges(G, pos = position, width = 2, alpha = 0.5, arrows = True, arrowstyle=’->’,e #nx.draw_networkx_edge_labels(G,pos = position ,edge_labels=edge_labels) nx.draw(G, pos = position, node_color = values, node_size = 2000, edge_cmp = plt.cm.Blues, edge_color=weights, with_labels=True) # plt.axis(’off’) # plt.legend(loc=’upper right’) fig = matplotlib.pyplot.gcf() fig.set_size_inches(40, 20) plt.savefig("./FIG/"+ str(medical_name) + ’_’ + str(time) + "_" + "1.pdf") # save as png #plt.show() # display #pylab.savefig("weighted_graph.png", dpi = 500) # save as png # graphStyle = {’vertex_size’: 20} # g = Graph(edges = edges, directed = True) # g.write_svg("example.svg", width=3000, height = 3000, **graphStyle)

<!-- b000568 | prose | pages [28] -->
plt.figure() plt.axis(’off’) new_edges, edges_colors = get_new_edges(edges, origin) for i in range(len(new_edges)):

<!-- b000569 | prose | pages [28, 29] -->
H.add_edges_from([new_edges[i]], weight = round(simi[new_edges[i][0],new_edges[i][1]])) # real_color = [] # elarge = [(u, v) for (u, v, d) in G.edges(data=True)] # for i in range(len(elarge)): # for k in range(len(edges_colors)): # #print(edges_colors[k][0], elarge[i]) # if ((edges_colors[k][0][0] == elarge[i][0]) and (edges_colors[k][0][1] == elarge[i][1])): # real_color.append(edges_colors[k][1]) # elif(k == (len(edges_colors) - 1)): # real_color.append(’mediumslateblue’) #print(len(elarge), len(real_color)) nx.draw_networkx_nodes(H,pos = position,cmap=plt.get_cmap(’jet’), node_size=2000, node_shape="o",a node_color = ’skyblue’) nx.draw_networkx_edges(H, pos = position, width = 1, alpha = 0.5, arrowstyle=’->’) plt.scatter(position[origin][0], position[origin][1], color=’royalblue’, marker=’o’, edgecolors=’g’ plt.text(position[origin][0], position[origin][1], str(origin), fontsize=20, style=’oblique’, ha=’c plt.xlabel(’lng’) plt.ylabel(’lat’) #nx.draw(H, pos = position, node_color =’skyblue’, node_size = 1000, edge_cmp = plt.cm.Reds) fig = matplotlib.pyplot.gcf() fig.set_size_inches(40, 20) pylab.savefig("./FIG/"+ str(medical_name) + ’_’ + str(time) + "_" + "2.pdf") # save as png

<!-- b000570 | furniture | pages [29] -->
Team # 1906204

<!-- b000571 | furniture | pages [29] -->
Page 27 of 38

<!-- b000573 | prose | pages [29] -->
def get_new_edges(edges, origin):

<!-- b000574 | prose | pages [29] -->
new_edges = [] color_mat = [] for i in range(len(edges)):

<!-- b000575 | prose | pages [29] -->
if(edges[i][0] == origin):

<!-- b000576 | prose | pages [29] -->
new_edges.append(edges[i]) color_mat.append([edges[i],’salmon’]) s_edges = new_edges for i in range(len(new_edges)):

<!-- b000577 | prose | pages [29] -->
tem = new_edges[i][1] for k in range(len(edges)):

<!-- b000578 | prose | pages [29] -->
if (edges[k][0] == tem):

<!-- b000579 | prose | pages [29] -->
s_edges.append(edges[k]) color_mat.append([edges[k],’navajowhite’]) t_edges = s_edges print(s_edges) for i in range(len(s_edges)):

<!-- b000580 | prose | pages [29] -->
tem1 = s_edges[i][1] for k in range(len(edges)):

<!-- b000581 | prose | pages [29] -->
if(edges[k][0] == tem1):

<!-- b000582 | prose | pages [29] -->
t_edges.append(edges[k]) color_mat.append([edges[k], ’mediumslateblue’]) return t_edges, color_mat

<!-- b000583 | prose | pages [29] -->
def get_all_origin(time, distance_threshold):

<!-- b000584 | prose | pages [29] -->
excel_path = ’kmeans.xls’ klocation = pd.read_excel(excel_path, sheet_name=’ZoneCounty Correspondence Table’) kdata = pd.read_excel(excel_path, sheet_name=’Date based on Zone’) distance = pd.read_excel(’distance.xls’, sheet_name=’distance’).values simi = pd.read_excel(’similarity.xls’,sheet_name = ’sim’).values

<!-- b000585 | prose | pages [29] -->
medical = [] def opoid_extract(x):

<!-- b000586 | prose | pages [29] -->
if not (x in medical):

<!-- b000587 | prose | pages [29] -->
medical.append(x) kdata[’substanceName’].apply(opoid_extract)

<!-- b000588 | prose | pages [29] -->
all_origins = [] for kk in range(len(medical)):

<!-- b000589 | prose | pages [29] -->
medical_name = medical[kk] edges = [] medical_data = kdata[(kdata[’substanceName’] == medical_name) & (kdata[’YYYY’] == time)] combins = [list(c) for c in combinations(set(medical_data[’Zone’].values.tolist()), 2)] weights = [] for i in range(len(combins)):

<!-- b000590 | furniture | pages [30] -->
Team # 1906204

<!-- b000591 | furniture | pages [30] -->
Page 28 of 38

<!-- b000592 | prose | pages [30] -->
x = combins[i][0] y = combins[i][1] if distance[x, y] < distance_threshold:

<!-- b000593 | prose | pages [30] -->
#print(medical_data[medical_data[’Zone’] == x]) #print(medical_data[medical_data[’Zone’] == y]) if (sum(medical_data[medical_data[’Zone’] == x][’DrugReportZone’].values) >= sum(medical_data[medical_data[’Zone’] == y][’DrugReportZone’].values)): edges.append(combins[i]) #G.add_edges_from([combins[i]], weight = round(simi[combins[i][0],combins[i][1]],1) #weights.append(round(simi[combins[i][0],combins[i][1]],1)) else:

<!-- b000594 | prose | pages [30] -->
combins[i].reverse() edges.append(combins[i]) #print(combins[i].reverse()) #G.add_edges_from([combins[i]], weight = round(simi[combins[i][0], combins[i][1]],1 #weights.append(round(simi[combins[i][0], combins[i][1]],1)) degree = [[x,0] for x in range(100)] for i in range(len(edges)):

<!-- b000595 | prose | pages [30] -->
degree[edges[i][0]][1] += 1 degree.sort(key=lambda x: x[1],reverse = True) ra = random.randint(0,3) origin = degree[ra][0] all_origins.append([medical[kk], origin]) print([medical[kk], origin]) print(all_origins)

<!-- b000596 | prose | pages [30] -->
if __name__ == ’__main__’:

<!-- b000597 | prose | pages [30] -->
data = xlrd.open_workbook(’kmeans.xls’) drug2num, num2drug, dataslice, center = init(data) trainingMatrix = np.zeros((100,69,7),dtype = np.int) # print(len(num2drug)) for year in range(7):

<!-- b000598 | prose | pages [30] -->
tmp = sparseMatrix(dataslice[year], drug2num, num2drug) for i in range(100):

<!-- b000599 | prose | pages [30] -->
for j in range(len(num2drug)):

<!-- b000600 | prose | pages [30] -->
trainingMatrix[i][j][year] += tmp[i][j] held_outMatrix = sparseMatrix(dataslice[7], drug2num, num2drug) # print(trainingMatrix)

<!-- b000601 | prose | pages [30] -->
#print(similarity(2, trainingMatrix, center, 300000)) adjMatrix(’Heroin’, 2014, 200000) #get_all_origin(2010, 200000)

<!-- b000602 | prose | pages [30] -->
Data prediction import xlrd import pandas as pd import numpy as np from math import * import xlwt import operator import copy from functools import reduce from sklearn import svm from sklearn.decomposition import PCA

<!-- b000603 | prose | pages [30] -->
def haversine(pos1, pos2):

<!-- b000604 | prose | pages [30] -->
""" Calculate the great circle distance between two points on the earth (specified in decimal degrees) """ # convert decimal into arc system lon1, lat1 = pos1 lon2, lat2 = pos2 lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

<!-- b000605 | prose | pages [30, 31] -->
# haversine formula dlon = lon2 - lon1 dlat = lat2 - lat1 a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 c = 2 * asin(sqrt(a)) r = 6371 # radius of earth, unit as kilometer return c * r * 1000

<!-- b000606 | furniture | pages [31] -->
Team # 1906204

<!-- b000607 | furniture | pages [31] -->
Page 29 of 38

<!-- b000609 | prose | pages [31] -->
def init(data):

<!-- b000610 | prose | pages [31] -->
sheet1 = data.sheets()[0] # Date based on Zone sheet2 = data.sheets()[1] # ZoneCounty Correspondence Table sheet3 = data.sheets()[2] # County Position

<!-- b000611 | prose | pages [31] -->
# map substanceName to Drug number drug2num = {} num2drug = []

<!-- b000612 | prose | pages [31] -->
rank = 0 dataslice = [[], [], [], [], [], [], [], []] for row in range(1, sheet1.nrows):

<!-- b000613 | prose | pages [31] -->
entry = sheet1.row_values(row) YYYY = entry[0] substanceName = entry[2] if substanceName not in drug2num.keys():

<!-- b000614 | prose | pages [31] -->
drug2num[substanceName] = rank num2drug.append(substanceName) rank += 1

<!-- b000615 | prose | pages [31] -->
# seperate this data into 8 parts by year if YYYY == 2010:

<!-- b000616 | prose | pages [31] -->
dataslice[0].append(entry) if YYYY == 2011:

<!-- b000617 | prose | pages [31] -->
dataslice[1].append(entry) if YYYY == 2012:

<!-- b000618 | prose | pages [31] -->
dataslice[2].append(entry) if YYYY == 2013:

<!-- b000619 | prose | pages [31] -->
dataslice[3].append(entry) if YYYY == 2014:

<!-- b000620 | prose | pages [31] -->
dataslice[4].append(entry) if YYYY == 2015:

<!-- b000621 | prose | pages [31] -->
dataslice[5].append(entry) if YYYY == 2016:

<!-- b000622 | prose | pages [31] -->
dataslice[6].append(entry) if YYYY == 2017:

<!-- b000623 | prose | pages [31] -->
dataslice[7].append(entry)

<!-- b000624 | prose | pages [31] -->
# dict to store each zone’s position center = {} for row in range(1, sheet2.nrows):

<!-- b000625 | prose | pages [31] -->
entry = sheet2.row_values(row) zone = int(entry[0]) if zone not in center.keys():

<!-- b000626 | prose | pages [31] -->
lat = entry[1] lon = entry[2] center[zone] = (lon, lat) return drug2num, num2drug, dataslice, center

<!-- b000627 | prose | pages [31] -->
def init_feature(feature):

<!-- b000628 | prose | pages [31] -->
sheet = feature.sheet_by_name(u’extract_feature’) factor = [[],[],[]] for row in range(1, sheet.nrows):

<!-- b000629 | prose | pages [31] -->
entry = sheet.row_values(row) if entry[1] == 2010:

<!-- b000630 | prose | pages [31] -->
factor[0].append(entry[3:]) if entry[1] == 2011:

<!-- b000631 | prose | pages [31] -->
factor[1].append(entry[3:]) if entry[1] == 2012:

<!-- b000632 | prose | pages [31, 32] -->
factor[2].append(entry[3:]) return factor def sparseMatrix(data, drug2num, num2drug):

<!-- b000633 | furniture | pages [32] -->
Team # 1906204

<!-- b000634 | furniture | pages [32] -->
Page 30 of 38

<!-- b000636 | prose | pages [32] -->
’’’ Matrix has 100 zones, each forms a row each row represents the num of drug report in that zone for each drugs initially, we set it all to zeros ’’’ # len(num2drug) = 69 sparseMatrix = np.zeros([100, 69]) for row in range(len(data)):

<!-- b000637 | prose | pages [32] -->
zone = int(data[row][1]) drugName = data[row][2] drugNum = drug2num[drugName] drugReport = data[row][3] sparseMatrix[zone][drugNum] += drugReport

<!-- b000638 | prose | pages [32] -->
return sparseMatrix

<!-- b000639 | prose | pages [32] -->
’’’ find the similarity between any zones alpha is the distance coefficient we only care about pairs whose distance is within alpha ’’’ def similarity(zone, data, center, alpha):

<!-- b000640 | prose | pages [32] -->
adjacentZones = [] for i in range(100):

<!-- b000641 | prose | pages [32] -->
if i != zone and haversine(center[i], center[zone]) < alpha:

<!-- b000642 | prose | pages [32] -->
Sum = np.sum(np.sum(np.array(data[i])))+np.sum(np.sum(np.array(data[zone]))) corr = 0 for j in range(69):

<!-- b000643 | prose | pages [32] -->
tendency_i = data[i][j] tendency_zone = data[zone][j] sum_i = np.sum(np.array(tendency_i)) sum_zone = np.sum(np.array(tendency_zone)) if sum_zone == 0 or sum_i == 0:

<!-- b000644 | prose | pages [32] -->
continue por = sum_i + sum_zone coef = np.corrcoef(tendency_i, tendency_zone)[0,1] if isnan(coef) or coef == 0:

<!-- b000645 | prose | pages [32] -->
pass else:

<!-- b000646 | prose | pages [32] -->
corr += coef*1.0*por/Sum adjacentZones.append([i, corr]) if len(adjacentZones) > 10:

<!-- b000647 | prose | pages [32] -->
adjacentZones.sort(key=lambda x: x[1]) return list(map(lambda x: x[0], adjacentZones[-10:])) else:

<!-- b000648 | prose | pages [32] -->
return list(map(lambda x: x[0], adjacentZones))

<!-- b000649 | prose | pages [32] -->
def normalization(array):

<!-- b000650 | prose | pages [32] -->
Sum = np.sum(np.array(array)) return list(map(lambda x: x*1.0/Sum, array))

<!-- b000651 | prose | pages [32, 33] -->
’’’ the purpose is to predict the drug spread tendency in following years Note: (1) for each zone and its every drug, if drug report is too smaller, we can’t its tendency, we use the tendency from its similar zones to predict it (2) if the specific drug in current zone has enough samples, then we combine its tendency with that of its similar zones to predict ’’’ def find_SVR_coef(data, center, held_outMatrix):

<!-- b000652 | furniture | pages [33] -->
Team # 1906204

<!-- b000653 | furniture | pages [33] -->
Page 31 of 38

<!-- b000655 | prose | pages [33] -->
features = {} axis = [[0],[1],[2],[3],[4],[5],[6]] for i in range(100):

<!-- b000656 | prose | pages [33] -->
simi_zone = similarity(i, data, center, 200000) n = len(simi_zone) for j in range(69):

<!-- b000657 | prose | pages [33] -->
# find each sample’s tendency model feature = [] clf = svm.SVR(gamma=’auto’, degree = 3 , kernel=’poly’) clf.fit(axis, data[i][j]) feature.append(clf) for k in range(n):

<!-- b000658 | prose | pages [33] -->
clf = svm.SVR(gamma=’auto’, degree = 3 , kernel=’poly’) clf.fit(axis, data[simi_zone[k]][j]) feature.append(clf) # use held_out data to find the weight of each model weight = [] for f in feature:

<!-- b000659 | prose | pages [33] -->
pre = f.predict([[7]]) real = held_outMatrix[i][j] weight.append(1.0/(0.01+np.square(pre-real))) weight = normalization(weight) features[(i, j)] = [feature, weight] return features

<!-- b000660 | prose | pages [33] -->
def find_SVR_coef_Mul(data, center, held_outMatrix, factor):

<!-- b000661 | prose | pages [33] -->
features = {} for i in range(100):

<!-- b000662 | prose | pages [33] -->
axis = [] simi_zone = similarity(i, data, center, 200000) n = len(simi_zone) feature = [] for j in range(3):

<!-- b000663 | prose | pages [33] -->
# pca=PCA(n_components=1) # newaxis=pca.fit_transform(factor[j][i]) # axis.append([newaxis]) axis.append(factor[j][i]) clf = svm.SVR(gamma=’auto’, kernel=’poly’) # print(axis) # print([np.sum(list(map(lambda x: x[0],data[i]))), np.sum(list(map(lambda x: x[1],data[i])))]) clf.fit(axis, [np.sum(list(map(lambda x: x[0],data[i]))), np.sum(list(map(lambda x: x[1],data[i]))), np.sum(list(map(lambda x: x[2],data[i])))])

<!-- b000664 | prose | pages [33] -->
feature.append(clf)

<!-- b000665 | prose | pages [33] -->
for k in range(n):

<!-- b000666 | prose | pages [33] -->
axis=[] for t in range(3):

<!-- b000667 | prose | pages [33] -->
axis.append(factor[t][simi_zone[k]]) clf = svm.SVR(gamma=’auto’, kernel=’poly’) clf.fit(axis, [np.sum(list(map(lambda x: x[0],data[simi_zone[k]]))), np.sum(list(map(lambda x: x[1],data[simi_zone[k]]))), np.sum(list(map(lambda x: x[2],da feature.append(clf) weight = [] for f in feature:

<!-- b000668 | prose | pages [33] -->
pre = f.predict([factor[2][i]]) real = held_outMatrix[i] weight.append(1.0/(1+abs(pre-real))) weight = normalization(weight) features[i] = [feature, weight] return features

<!-- b000669 | prose | pages [33] -->
def predict(features, year):

<!-- b000670 | prose | pages [33] -->
t = year - 2010 predict = np.zeros([100, 69]) for i in range(100):

<!-- b000671 | prose | pages [33] -->
for j in range(69):

<!-- b000672 | furniture | pages [34] -->
Team # 1906204

<!-- b000673 | furniture | pages [34] -->
Page 32 of 38

<!-- b000674 | prose | pages [34] -->
f, w = features[(i, j)] pre = round(np.sum(list(map(lambda x, y: x.predict([[t]])*y, f, w))),0) if pre > 0:

<!-- b000675 | prose | pages [34] -->
predict[i][j] = pre else:

<!-- b000676 | prose | pages [34] -->
predict[i][j] = 0 return predict

<!-- b000677 | prose | pages [34] -->
def predict_Mul(features, new_factor):

<!-- b000678 | prose | pages [34] -->
predict = np.zeros([100, 1]) for i in range(100):

<!-- b000679 | prose | pages [34] -->
new_f = new_factor[i] f, w = features[i] pre = round(np.sum(list(map(lambda x, y: x.predict([new_f])*y, f, w))),0) if pre > 0:

<!-- b000680 | prose | pages [34] -->
predict[i] = pre else:

<!-- b000681 | prose | pages [34] -->
predict[i] = 0 return predict

<!-- b000682 | prose | pages [34] -->
if __name__ == ’__main__’:

<!-- b000683 | prose | pages [34] -->
data = xlrd.open_workbook(’../K-means/kmeans.xls’) drug2num, num2drug, dataslice, center = init(data)

<!-- b000684 | prose | pages [34] -->
trainingMatrix = np.zeros((100,69,7), dtype = np.int)

<!-- b000685 | prose | pages [34] -->
for year in range(7):

<!-- b000686 | prose | pages [34] -->
tmp = sparseMatrix(dataslice[year], drug2num, num2drug) for i in range(100):

<!-- b000687 | prose | pages [34] -->
for j in range(len(num2drug)):

<!-- b000688 | prose | pages [34] -->
trainingMatrix[i][j][year] += tmp[i][j] held_outMatrix = sparseMatrix(dataslice[7], drug2num, num2drug)

<!-- b000689 | prose | pages [34] -->
extract_feature = xlrd.open_workbook(’extract_feature.xls’) factor = init_feature(extract_feature)

<!-- b000690 | prose | pages [34] -->
# print(’------------real--------------’) real = np.zeros([100,1]) for i in range(len(dataslice[2])):

<!-- b000691 | prose | pages [34] -->
entry = dataslice[2][i] real[int(entry[1])] += entry[3] # print(real) # print([list(map(lambda x: x[2], dataslice[2][i])) for i in range(100)]) # print(’------------pre---------------’) train = find_SVR_coef_Mul(trainingMatrix, center, real, factor) pre = predict_Mul(train, factor[2]) # print(pre)

<!-- b000692 | prose | pages [34] -->
factor_new = [[12., 5, 27]]*100 pre_new = predict_Mul(train, factor_new)

<!-- b000693 | prose | pages [34] -->
# for i in range(100): # print(’real: {0} --- pre: {1} --- new: {2} --- zone: {3}’.format(real[i], pre[i], pre_new[i], i

<!-- b000694 | prose | pages [34] -->
print(’real: {0} --- pre: {1} --- new: {2} --- zone: {3}’.format(real[88], pre[88], pre_new[88], 88 # features = find_SVR_coef(trainingMatrix, center, held_outMatrix) # print(features) # print(’--------------2017predict---------------------’) # pred2017 = predict(features, 2017) # print(pred2017) # print(held_outMatrix[0][1]) # print(trainingMatrix[0][1]) # sim = similarity(0,trainingMatrix,center,300000) # print(sim) # for s in sim:

<!-- b000695 | furniture | pages [35] -->
Team # 1906204

<!-- b000696 | furniture | pages [35] -->
Page 33 of 38

<!-- b000697 | prose | pages [35] -->
# print(trainingMatrix[s][1],’---------------’) # print(’-----------------2017real----------------------’) # real2017 = sparseMatrix(dataslice[7], drug2num, num2drug) # print(real2017)

<!-- b000698 | prose | pages [35] -->
# diff = np.array(pred2017) - np.array(real2017) # d = np.sum(list(map(lambda x: abs(x), diff))) # print(d) # print(’-----------------2018predict---------------------’) # rel2018 = predict(features, 2018) # print(rel2018) # print(’-----------------2019predict---------------------’) # rel2019 = predict(features, 2019) # print(rel2019)

<!-- b000699 | prose | pages [35] -->
# excel = xlwt.Workbook() # sheet = excel.add_sheet("Predicted Date based on Zone") # sheet.write(0, 0, "YYYY") # sheet.write(0, 1, "Zone") # sheet.write(0, 2, "substanceName") # sheet.write(0, 3, "DrugReportZone")

<!-- b000700 | prose | pages [35] -->
# row = 0 # for zone in range(len(rel2018)): # for drug in range(69): # row += 1 # substanceName = num2drug[drug] # sheet.write(row, 0, 2018) # sheet.write(row, 1, zone) # sheet.write(row, 2, substanceName) # sheet.write(row, 3, rel2018[zone][drug]) # for zone in range(len(rel2019)): # for drug in range(69): # row += 1 # substanceName = num2drug[drug] # sheet.write(row, 0, 2019) # sheet.write(row, 1, zone) # sheet.write(row, 2, substanceName) # sheet.write(row, 3, rel2018[zone][drug])

<!-- b000701 | prose | pages [35] -->
# excel.save("/Users/lsd/Desktop/code/Model/predict.xls")

<!-- b000702 | prose | pages [35] -->
Data Classiﬁcation # -*- coding: utf-8 -*-

<!-- b000703 | prose | pages [35] -->
import pandas as pd import numpy as np import sklearn.preprocessing

<!-- b000704 | prose | pages [35] -->
label = [] data = [] opioid = pd.read_csv(’opioid_total.csv’, index_col=0) county = opioid[’FIPS_Combined’].unique() for i in range(10,17):

<!-- b000705 | prose | pages [35] -->
column = [’GEO.id2’] data_csv = pd.read_csv(’ACS_’+str(i)+’_5YR_DP02/ACS_’+str(i)+’_5YR_DP02_with_ann.csv’, index_col=0) for n in data_csv.columns.values:

<!-- b000706 | prose | pages [35] -->
if ’HC03’ in n:

<!-- b000707 | prose | pages [35] -->
column.append(n) data_csv = data_csv[column] data.append(data_csv) label = np.unique(np.append(label, data_csv.loc[’Id’].tolist())) label = label[1:len(label)]

<!-- b000708 | prose | pages [35] -->
df = pd.DataFrame(columns=label) for fips in county:

<!-- b000709 | furniture | pages [36] -->
Team # 1906204

<!-- b000710 | furniture | pages [36] -->
Page 34 of 38

<!-- b000711 | prose | pages [36] -->
for row in label:

<!-- b000712 | prose | pages [36] -->
A = [] B = [] for i in range(7):

<!-- b000713 | prose | pages [36] -->
try:

<!-- b000714 | prose | pages [36] -->
A.append(int(opioid.loc[(opioid[’FIPS_Combined’] == fips) &(opioid[’YYYY’] == i+2010), ’DrugReports’])) except:A.append(0) try:

<!-- b000715 | prose | pages [36] -->
B.append(float(data[i].loc[(data[i][’GEO.id2’] == str(fips)), (data[i].loc[’Id’] == row)].values[0][0])) except:B.append(0) A = sklearn.preprocessing.normalize(np.array([A]), norm = ’l2’) B = sklearn.preprocessing.normalize(np.array([B]), norm = ’l2’) corr = np.corrcoef(A,B)[0][1] df.loc[fips,row] = corr print(fips) for row in label:

<!-- b000716 | prose | pages [36] -->
df.loc[’avg’,row] = df[row].mean() df.to_csv(’rough_corr_result.csv’, encoding=’utf-8’)

<!-- b000717 | prose | pages [36] -->
Association rule learning

<!-- b000718 | prose | pages [36] -->
import xlrd import pandas as pd import numpy as np from math import * import xlwt import operator import copy from functools import reduce import matplotlib.pyplot as plt import matplotlib import networkx as nx from itertools import combinations from igraph import * import seaborn as sns import pylab import random from sklearn.cluster import KMeans import sklearn.preprocessing from mlxtend.frequent_patterns import apriori from mlxtend.frequent_patterns import association_rules from collections import Counter sns.set_style(’darkgrid’)

<!-- b000719 | prose | pages [36] -->
def get_drugReport(time, location, excel_output_add_new = pd.read_excel(’excel_output_add_new.xls’, sheet_name=’biubiu’)):

<!-- b000720 | prose | pages [36] -->
try:

<!-- b000721 | prose | pages [36] -->
return excel_output_add_new[(excel_output_add_new[’FIPS_Combined’] == location)&(excel_output_add_new[’YYYY’] == time)][’TotalDrugReportsCounty’].values[0] except:

<!-- b000722 | prose | pages [36] -->
return 0 #print(get_drugReport(2010, 51001))

<!-- b000723 | prose | pages [36] -->
def get_new_dataFile_with_drug(time):

<!-- b000724 | prose | pages [36] -->
problem2_data = pd.read_excel(’problem2_data.xlsx’, sheet_name=’Sheet1’) dat = [0] for i in range(1, len(problem2_data[’GEO.id2’])):

<!-- b000725 | prose | pages [36] -->
loc = problem2_data[’GEO.id2’].iloc[i] k = get_drugReport(time, loc) dat.append(get_drugReport(time, loc)) print(k) problem2_data[’drug’] = dat print(dat) return ’sucess’

<!-- b000726 | prose | pages [36] -->
def Kmean_sub(data):

<!-- b000727 | furniture | pages [37] -->
Team # 1906204

<!-- b000728 | furniture | pages [37] -->
Page 35 of 38

<!-- b000729 | prose | pages [37] -->
estimator = KMeans(n_clusters=2) estimator.fit(data) label_pred = estimator.labels_ centroids = estimator.cluster_centers_ inertia = estimator.inertia_ print(label_pred) print(centroids) print(inertia)

<!-- b000730 | prose | pages [37] -->
def softmax(x):

<!-- b000731 | prose | pages [37] -->
"""Compute softmax values for each sets of scores in x.""" e_x = np.exp(x - np.max(x)) return e_x / e_x.sum(axis=0) # only difference

<!-- b000732 | prose | pages [37] -->
def to_bool(problem2_data, alpha):

<!-- b000733 | prose | pages [37] -->
column_name = problem2_data.columns.values.tolist() column_name = [x for x in column_name if ((x[0] == ’H’) and (x[3] == ’3’) or (x == ’DRUG’))] all_info = [] new_column_name = [] for i in range(1, len(column_name)):

<!-- b000734 | prose | pages [37] -->
item = column_name[i] temp = [] try:

<!-- b000735 | prose | pages [37] -->
threshold = problem2_data[item].iloc[1:].quantile(alpha) for k in range(1, len(problem2_data[item])):

<!-- b000736 | prose | pages [37] -->
if (problem2_data[item][k] >= threshold):

<!-- b000737 | prose | pages [37] -->
temp.append(1) else:

<!-- b000738 | prose | pages [37] -->
temp.append(0) new_column_name.append(item) all_info.append(temp) except:

<!-- b000739 | prose | pages [37] -->
print("Don’t work:", item) bool_frame = pd.DataFrame(data = np.transpose(np.array(all_info)), columns = new_column_name, index = problem2_data[’GEO.id2’].iloc[1:].tolist()) print(bool_frame) print(new_column_name) bool_frame.to_excel(’bool_pro2.xls’,sheet_name=’biubiu’) return new_column_name

<!-- b000740 | prose | pages [37] -->
def get_corr(d, metadata, type_info):

<!-- b000741 | prose | pages [37] -->
d = d[d[’DRUG’] == 1] d = d[type_info] print(d.shape) #find_rule(d, support, confidence).to_excel(’rules.xls’) frequent_itemsets = apriori(d, min_support=0.05, use_colnames=True) print("apriori done!") rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1) print("association_rules done!") rules = rules[(rules[’lift’] >= 1) &(rules[’confidence’] >= 0.8)].sort_values("lift",ascending = Fa #rules = rules[rules[’consequents’].isin(["DRUG"])] dro = [] #df[df[’å´L˚UåˇR ’].isin([ç˙ZÿåžˇTçŽˇDå˘Aij])] rules.index = range(len(rules[’lift’])) for i in range(len(rules[’lift’])):

<!-- b000742 | prose | pages [37] -->
m = rules[’consequents’].iloc[i] if not ("DRUG" in m):

<!-- b000743 | prose | pages [37] -->
dro.append(i) rules = rules.drop(index = dro)

<!-- b000744 | prose | pages [37] -->
rules.index = range(len(rules[’lift’])) influence = rules[’antecedents’].values influence = [list(x) for x in influence] temp5 = [] for i in range(len(influence)):

<!-- b000745 | prose | pages [37] -->
for j in range(len(influence[i])):

<!-- b000746 | prose | pages [37, 38] -->
temp5.append(influence[i][j]) thre = pd.value_counts(temp5).quantile(0.7) freqence_temp5 = pd.value_counts(temp5) freqence_temp5 = freqence_temp5[freqence_temp5 >= thre] freIndex = freqence_temp5.index.tolist() metadata.index = metadata[’GEO.id’].values.tolist() final_result = [] for i in range(len(freIndex)):

<!-- b000747 | furniture | pages [38] -->
Team # 1906204

<!-- b000748 | furniture | pages [38] -->
Page 36 of 38

<!-- b000750 | prose | pages [38] -->
final_result.append([freIndex[i],freqence_temp5[freIndex[i]], metadata.loc[freIndex[i], ’Id’]]) print(final_result) return final_result #rules.to_csv(’rules.csv’)

<!-- b000751 | prose | pages [38] -->
def classfy(all_type, metadata, people_type):

<!-- b000752 | prose | pages [38] -->
result = [] for i in range(len(people_type)):

<!-- b000753 | prose | pages [38] -->
result.append([]) metadata.index = metadata[’GEO.id’].values.tolist() for i in range(len(all_type)-1):

<!-- b000754 | prose | pages [38] -->
temp = metadata.loc[all_type[i], ’Id’] for j in range(len(people_type)):

<!-- b000755 | prose | pages [38] -->
if (people_type[j] in temp):

<!-- b000756 | prose | pages [38] -->
result[j].append(all_type[i]) break #print(result) return result

<!-- b000757 | prose | pages [38] -->
def get_all_corr(all_type, d, metadata, people_type):

<!-- b000758 | prose | pages [38] -->
# slice_number = [] # for i in range(0, len(all_type)-1, split_number): # if ((i+split_number)<= (len(all_type)-1)): # slice_number.append([i, i+split_number]) # else: # slice_number.append([i, len(all_type)-1]) # print(slice_number) cls = classfy(all_type, metadata, people_type) all_info = [] for i in range(len(cls)):

<!-- b000759 | prose | pages [38] -->
#ty = all_type[slice_number[i][0]:slice_number[i][1]] ty = cls[i] ty.append("DRUG") all_info.append(get_corr(d, metadata, ty)) print("Test case:", cls[i]) print("People type:%s\n" %people_type[i]) print(all_info) print(’-----------------------\n\n’) all_info_new = [] for i in range(len(all_info)):

<!-- b000760 | prose | pages [38] -->
for j in range(len(all_info[i])):

<!-- b000761 | prose | pages [38] -->
all_info_new.append(all_info[i][j]) all_info_new.sort(key = lambda x: x[1], reverse = True) return all_info_new if __name__ == ’__main__’:

<!-- b000762 | prose | pages [38] -->
#excel_output_add_new = pd.read_excel(’excel_output_add_new.xls’, sheet_name=’biubiu’) #get_new_dataFile_with_drug(2010) problem2_data = pd.read_excel(’ACS_11_5YR_DP02_with_ann.xlsx’, sheet_name=’ACS_11_5YR_DP02_with_ann #print(problem2_data[’DRUG’].iloc[1:].quantile(0.6)) #predata = problem2_data[’DRUG’].values[1:].reshape(-1,1) #print(predata) #Kmean_sub(predata) all_type = to_bool(problem2_data, 0.5) support = 0.06 confidence = 0.75 ms = ’--’ d = pd.read_excel(’bool_pro2.xls’,sheet_name=’biubiu’) metadata = pd.read_excel(’ACS_11_5YR_DP02_metadata.xlsx’,sheet_name=’ACS_11_5YR_DP02_metadata’) #get_corr(d, metadata)

<!-- b000763 | prose | pages [38, 39] -->
#all_type = [’HC03_VC04’, ’HC03_VC06’, ’HC03_VC07’, ’HC03_VC08’, ’HC03_VC09 HC03_VC # ’HC03_VC12’, ’HC03_VC13’, ’HC03_VC14’, ’HC03_VC15’, ’HC03_VC17’, ’HC03_VC18’, ’HC03_VC25’, ’HC03_ # ’HC03_VC27’, ’HC03_VC28’, ’HC03_VC29’, ’HC03_VC30’, ’HC03_VC31’, ’HC03_VC35’, ’HC03_VC36’, ’HC03_ # ’HC03_VC38’, ’HC03_VC39’, ’HC03_VC40’, ’HC03_VC42’, ’HC03_VC43’, ’HC03_VC44’, ’HC03_VC45’, ’HC03_ # ’HC03_VC47’, ’HC03_VC51’, ’HC03_VC61’, ’HC03_VC62’, ’HC03_VC64’, ’HC03_VC65’, ’HC03_VC66’, ’HC03_ # ’HC03_VC69’, ’HC03_VC70’, ’HC03_VC71’, ’HC03_VC75’, ’HC03_VC76’, ’HC03_VC77’, ’HC03_VC78’, ’HC03_ # ’HC03_VC80’, ’HC03_VC84’, ’HC03_VC85’, ’HC03_VC86’, ’HC03_VC87’, ’HC03_VC88’, ’HC03_VC89’, ’HC03_ # ’HC03_VC91’, ’HC03_VC93’, ’HC03_VC94’, ’HC03_VC98’, ’HC03_VC99’, ’HC03_VC117’, ’HC03_VC118’, ’HC0 # ’HC03_VC120’, ’HC03_VC121’, ’HC03_VC122’, ’HC03_VC123’, ’HC03_VC124’, ’HC03_VC128’, ’HC03_VC129’ # ’HC03_VC131’, ’HC03_VC132’, ’HC03_VC133’, ’HC03_VC134’, ’HC03_VC138’, ’HC03_VC144’, ’HC03_VC146 # ’HC03_VC156’, ’HC03_VC166’, ’HC03_VC167’, ’HC03_VC168’, ’HC03_VC170’, ’HC03_VC171’, ’HC03_VC17 # ’HC03_VC174’, ’HC03_VC175’, ’HC03_VC176’, ’HC03_VC177’, ’HC03_VC178’, ’HC03_VC182’, ’HC03_VC18 # ’HC03_VC185’, ’HC03_VC186’, ’HC03_VC187’, ’HC03_VC188’, ’HC03_VC189’, ’HC03_VC190’, ’HC03_VC19 # ’HC03_VC193’, ’HC03_VC194’, ’HC03_VC195’, ’HC03_VC196’, ’HC03_VC197’, ’HC03_VC198’, ’HC03_VC1 # ’HC03_VC201’, ’HC03_VC202’, ’HC03_VC203’, ’HC03_VC204’, ’HC03_VC205’, ’HC03_VC206’, ’HC03_VC2 # ’HC03_VC209’, ’DRUG’]

<!-- b000764 | furniture | pages [39] -->
Team # 1906204

<!-- b000765 | furniture | pages [39] -->
Page 37 of 38

<!-- b000767 | prose | pages [39] -->
people_type = [’HOUSEHOLDS BY TYPE’, ’RELATIONSHIP’, ’MARITAL STATUS’, ’FERTILITY’, ’GRANDPARENTS’, ’SCHOOL ENROLLMENT’, ’EDUCATIONAL ATTAINMENT’, ’VETERAN STATUS’, ’DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION’, ’RESIDENCE 1 YEAR AGO’, ’PLACE OF BIRTH’, ’U.S. CITIZENSHIP STATUS’, ’YEAR OF ENTRY’, ’WORLD REGION OF BIRTH OF FOREIGN BORN’, ’LANGUAGE SPOKEN AT HOME’, ’ANCESTRY’]

<!-- b000768 | prose | pages [39] -->
print(’-----------------------\n\n’) print(get_all_corr(all_type, d, metadata, people_type)) # slice_number = [] # split_number = 25 # for i in range(0, len(all_type)-1, split_number): # if ((i+split_number)<= (len(all_type)-1)): # slice_number.append([i, i+split_number]) # else: # slice_number.append([i, len(all_type)-1]) # print(slice_number) # for i in range(len(slice_number)): # ty = all_type[slice_number[i][0]:slice_number[i][1]] # ty.append("DRUG") # print(ty)

<!-- b000769 | prose | pages [39] -->
SVM classiﬁer and threshold analysis report = opioidtotalbyzone.DrugReportZone; County = opioidtotalbyzone.TotalDrugReportZone; A = [report County]; idx = zeros(size(A,1),1); for i=1:1:size(A,1) if A(i,2)<125000-100*A(i,1) idx(i) = 1; else idx(i) = 2; end end

<!-- b000770 | prose | pages [39] -->
figure; plot(A(:,1).*(idx-1), A(:,2).*(idx-1),’r.’); hold on; plot(A(:,1).*-(idx-2),A(:,2).*-(idx-2),’b.’); idx(idx==2)=-1; svm = fitcsvm(A,idx);

<!-- b000771 | prose | pages [39] -->
svInd = svm.IsSupportVector;

<!-- b000772 | prose | pages [39] -->
figure

<!-- b000773 | prose | pages [39] -->
plot(A(:,1),A(:,2),’k.’) hold on plot(A(svInd,1),A(svInd,2),’ro’,’MarkerSize’,10) %input new data here score is the output 1 or -1 predict_data = predictopioidtotal.DrugReportZone;

<!-- b000774 | furniture | pages [40] -->
Team # 1906204

<!-- b000775 | furniture | pages [40] -->
Page 38 of 38

<!-- b000776 | prose | pages [40] -->
County = County(1:length(predict_data)); B = [predict_data County];

<!-- b000777 | prose | pages [40] -->
score = predict(svm,B);

<!-- b000778 | prose | pages [40] -->
title(’{\bf Outlier Detection via One-Class SVM}’) xlabel(’Opioid Drug Reports’) ylabel(’Total Drug Report by County’) legend(’Observation’,’Support Vector’) hold off
