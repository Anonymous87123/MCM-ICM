# P-D-2024-2419588-1cc62ede

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2024

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [1] -->
2419588

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | prose | pages [1] -->
Optimizing Great Lakes Water Management: An Adaptive

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | prose | pages [1] -->
Hydrological Network Approach

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
The Great Lakes, holding 21% of the world's fresh surface water, face complex water level management challenges due to natural and human factors. This study presents an Adaptive Hydrological Network Simulation and an Equilibrium Stake- holder Satisfaction (ESS) Model to address these challenges. The network model represents the lakes as interconnected nodes and edges, simplifying the system's complexity and facilitating analysis. The ESS Model integrates stakeholder prefer- ences, prioritizing their diverse interests in water level management.

<!-- b000014 | prose | pages [1] -->
The study introduces a modified dam control algorithm based on Model Pre- dictive Control (MPC), enhancing the responsiveness of water level regulation to

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
environmental changes. The algorithm's performance is assessed using 2017 data, revealing its sensitivity to high water levels and the need for improved adaptation to extreme weather events. The ESS Model's stakeholder satisfaction functions are tailored to reflect the preferences of shipping companies, dock managers, environ- mentalists, property owners, recreational users, and hydro-power generation com- panies, with weights assigned to balance their influence.

<!-- b000017 | prose | pages [1] -->
The research concludes that the proposed models and algorithms show prom- ise in managing the Great Lakes' water levels effectively, considering ecological, so- cial, and economic factors. However, there are limitations, such as the model's sim- plification of natural factors and the need for empirical validation of stakeholder satisfaction functions. Future work should focus on refining the model to better cap- ture the system's complexity and improve predictive accuracy.

<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | keywords | pages [1] -->
Keywords: Adaptive Hydrological Network; Equilibrium Stakeholder Satisfaction;

<!-- b000020 | prose | pages [1] -->
Model Predictive Control; Great Lakes Water Management; Environmental Sensitiv- ity Analysis

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | prose | pages [1] -->
关注数学模型

<!-- b000029 | furniture | pages [1] -->
2

<!-- b000030 | furniture | pages [1] -->
MATHmodels

<!-- b000031 | furniture | pages [1] -->
获取更多资讯

<!-- b000032 | furniture | pages [2] -->


<!-- b000033 | prose | pages [2] -->
Content

<!-- b000034 | prose | pages [2] -->
1 Introduction· ................................................................................................... 1

<!-- b000035 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000036 | prose | pages [2] -->
1.1 Problem Background .................................................................................................... 1 1.2 Restatement of the Problem ......................................................................................... 1 1.3 Our Work ....................................................................................................................... 1

<!-- b000037 | prose | pages [2] -->
2 Assumptions and Justifications .................................................................. 2

<!-- b000038 | prose | pages [2] -->
3 Notations .......................................................................................................... 3

<!-- b000039 | prose | pages [2] -->
4 Adaptive Hydrological Network Simulation ........................................... 3 4.1 Introduction to the Network Model ........................................................................... 3 4.2 Model Framework: Representation of Nodes and Edges ....................................... 3 4.3 Mathematical Formulation of the Network Model .................................................. 4 4.4 River Flow between Lakes ........................................................................................... 4 4.5 Incorporating Uncontrollable Factors ........................................................................ 8

<!-- b000040 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000041 | prose | pages [2] -->
5 Equilibrium Stakeholder Satisfaction (ESS) Model ............................. 11 5.1 Overview of the ESS Model ....................................................................................... 11 5.2 Stakeholder Analysis .................................................................................................. 11 5.3 Stakeholder Satisfaction and Weighting .................................................................. 13 5.4 Calculation of Optimal Water Level ........................................................................ 15

<!-- b000042 | prose | pages [2] -->
6 Dam Control Algorithm Implementation ............................................... 16 6.1 Control Objectives and Performance Metrics ......................................................... 16 6.2 MPC Model .................................................................................................................. 16

<!-- b000043 | prose | pages [2] -->
7 Dam Control Algorithm ............................................................................. 17 7.1 Analysis of Plan2014 ................................................................................................... 17 7.2 The modification of the Rule Curve ......................................................................... 18

<!-- b000044 | prose | pages [2] -->
8 Assessing Control Algorithm Sensitivity in 2017 ................................. 18 8.1 Data Collection and Model Simulation.................................................................... 18 8.2 Simulation Results and Analysis .............................................................................. 19 8.3 Sensitivity Assessment of Control Algorithms ....................................................... 19 8.4 Stakeholder Impact Evaluation ................................................................................. 19 8.5 Algorithm Sensitivity to Environmental Changes ................................................. 20

<!-- b000045 | prose | pages [2] -->
9 Model Evaluation and Further Discussion ............................................. 20 9.1 Strengths ....................................................................................................................... 20 9.2 Weaknesses .................................................................................................................. 20 9.3 Further Discussion ...................................................................................................... 20

<!-- b000046 | prose | pages [2] -->
10 Conclusion ................................................................................................... 21

<!-- b000047 | prose | pages [2] -->
References ......................................................................................................... 22

<!-- b000048 | furniture | pages [2] -->


<!-- b000049 | furniture | pages [2] -->


<!-- b000050 | prose | pages [2] -->
关注数学模型

<!-- b000051 | furniture | pages [2] -->
2

<!-- b000052 | furniture | pages [2] -->
MATHmodels

<!-- b000053 | furniture | pages [2] -->
获取更多资讯

<!-- b000054 | furniture | pages [3] -->
Team # 2419588

<!-- b000055 | heading | pages [3] -->
1 Introduction·

<!-- b000056 | heading | pages [3] -->
1.1 Problem Background

<!-- b000057 | furniture | pages [3] -->


<!-- b000058 | furniture | pages [3] -->


<!-- b000059 | furniture | pages [3] -->
Page  1  of  22

<!-- b000060 | prose | pages [3] -->
Managing the Great Lakes' water levels, crucial for regional ecosystems, econo-

<!-- b000061 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000062 | prose | pages [3] -->
mies, and communities in the US and Canada, is complex. These lakes, with 21% of the world's fresh surface water, face seasonal changes due to natural phenomena like precip- itation and evaporation, and human impacts from industri- alization and water regulation structures, such as the Soo Locks and Moses-Saunders Dam. Overseen by the Interna- tional Joint Commission (IJC),

<!-- b000063 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000064 | prose | pages [3] -->
efforts to balance stakeholder interests are challenged by cli- mate change-induced fluctua-

<!-- b000065 | caption | pages [3] -->
Figure 1 Top view of the Great Lakes

<!-- b000066 | prose | pages [3] -->
tions. This urgency underscores the need for effective water level management strategies, highlighting the importance of addressing this trans- boundary environmental issue.

<!-- b000067 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000068 | prose | pages [3] -->
The core problem involves devising a method to regulate the water levels effec- tively, ensuring that the diverse needs of all stakeholders are met. This encompasses:

<!-- b000069 | prose | pages [3] -->
Problem 1: Determining the optimal water levels for the five Great Lakes  throughout the year, considering the varying desires and the associated costs and benefits for each stakeholder group.

<!-- b000070 | heading | pages [3] -->
Problem 2: Developing algorithms that can dynamically maintain these opti-

<!-- b000071 | prose | pages [3] -->
 mal water levels based on real-time inflow and outflow data.

<!-- b000072 | heading | pages [3] -->
Problem 3: Assessing the algorithms' sensitivity, particularly for dam outflows,

<!-- b000073 | prose | pages [3] -->
 using 2017 data to forecast stakeholder satisfaction.

<!-- b000074 | heading | pages [3] -->
Problem 4: Assessing the algorithms' responsiveness to environmental changes,

<!-- b000075 | prose | pages [3] -->
 such as variations in precipitation, winter snowpack, and ice jams, which could significantly impact water levels. Problem 5: Specifically focusing on Lake Ontario, given recent concerns over  its water level management, to analyze the factors and stakeholders uniquely influencing it.

<!-- b000076 | heading | pages [3] -->
1.3 Our Work

<!-- b000077 | prose | pages [3] -->
To avoid complicated description , intuitively reflect our work process, the flow chart is show as the following Figure 1：

<!-- b000078 | furniture | pages [3] -->


<!-- b000079 | prose | pages [3] -->
关注数学模型

<!-- b000080 | furniture | pages [3] -->
2

<!-- b000081 | furniture | pages [3] -->
MATHmodels

<!-- b000082 | furniture | pages [3] -->
获取更多资讯

<!-- b000083 | furniture | pages [4] -->
Team # 2419588

<!-- b000084 | furniture | pages [4] -->


<!-- b000085 | furniture | pages [4] -->


<!-- b000086 | furniture | pages [4] -->
Page  2  of  22

<!-- b000087 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000088 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000089 | furniture | pages [4] -->


<!-- b000090 | caption | pages [4] -->
Figure 1. Our Work

<!-- b000091 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000092 | prose | pages [4] -->
To quantify the demands of the various stakeholders, we make the following as- sumptions.

<!-- b000093 | prose | pages [4] -->
Assumption 1: The Great Lakes are considered as a complex network system.

<!-- b000094 | heading | pages [4] -->
Justification: This assumption simplifies the complexity of the

<!-- b000095 | prose | pages [4] -->
model by representing the relationships between lakes and rivers as a network, facilitating the analysis and understanding of interac- tions among the lakes. Assumption 2: The surface area of the lakes remains relatively stable over long pe-

<!-- b000096 | prose | pages [4] -->
riods.

<!-- b000097 | heading | pages [4] -->
Justification: This assumption is based on historical data and geo-

<!-- b000098 | prose | pages [4] -->
graphical studies, suggesting that the surface area of the lakes does not change significantly, thus serving as a basis for calculating wa- ter level changes.

<!-- b000099 | heading | pages [4] -->
Assumption 3: There is a stable relationship between lake water

<!-- b000100 | heading | pages [4] -->
Justification: This assumption is based on the relative stability of

<!-- b000101 | prose | pages [4] -->
lake geomorphological features and the typical relationship be- tween water levels and storage volume, known as the stage-storage curve. Assumption 4: River flow is primarily related to the water level of upstream lakes.

<!-- b000102 | heading | pages [4] -->
Justification: This assumption is grounded in the principles of fluid

<!-- b000103 | prose | pages [4] -->
dynamics, where water flows from higher to lower water levels, and the flow rate is influenced by the water level difference and river characteristics.

<!-- b000104 | furniture | pages [4] -->


<!-- b000105 | prose | pages [4] -->
关注数学模型

<!-- b000106 | furniture | pages [4] -->
2

<!-- b000107 | furniture | pages [4] -->
MATHmodels

<!-- b000108 | furniture | pages [4] -->
获取更多资讯

<!-- b000109 | furniture | pages [5] -->
Team # 2419588

<!-- b000110 | furniture | pages [5] -->


<!-- b000111 | furniture | pages [5] -->


<!-- b000112 | furniture | pages [5] -->
Page  3  of  22

<!-- b000113 | heading | pages [5] -->
Assumption 5: Precipitation is the main factor affecting lake storage volumes, and

<!-- b000114 | prose | pages [5] -->
evaporation is the primary pathway for water loss in the Great Lakes system.

<!-- b000115 | heading | pages [5] -->
Justification: This assumption is based on an understanding of the

<!-- b000116 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000117 | prose | pages [5] -->
Great Lakes' water balance studies, where precipitation and evapo- ration are key natural processes affecting the water balance. Assumption 6: Ice jams have a significant impact on the hydrodynamics of the

<!-- b000118 | prose | pages [5] -->
Great Lakes region.

<!-- b000119 | heading | pages [5] -->
Justification: This assumption takes into account the potential ef-

<!-- b000120 | prose | pages [5] -->
fects of ice jams on river flow during winter, which is crucial for simulating and predicting water level changes during the winter months.

<!-- b000121 | heading | pages [5] -->
3 Notations

<!-- b000122 | prose | pages [5] -->
In our paper, Lake Superior is referred to as 𝑁1, Lake Michigan and Lake Huron are referred to as 𝑁2, Lake Erie is referred to as 𝑁3, and Lake Ontario is referred to as

<!-- b000123 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000124 | prose | pages [5] -->
𝑁4.

<!-- b000125 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000126 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000127 | prose | pages [5] -->
Description

<!-- b000128 | heading | pages [5] -->
Symbol

<!-- b000129 | prose | pages [5] -->
Unit Water level of 𝑁𝑖 𝑊𝑖 𝑄𝑖𝑗 𝑚 Flow of the river connecting 𝑁𝑖,𝑁𝑗 𝑚3𝑡−1 Compensating Works of the Soo Locks 𝐶12

<!-- b000130 | furniture | pages [5] -->


<!-- b000131 | heading | pages [5] -->
4 Adaptive Hydrological Network Simulation

<!-- b000132 | heading | pages [5] -->
4.1 Introduction to the Network Model

<!-- b000133 | prose | pages [5] -->
Network models, graphing systems as interconnected nodes and edges, are key for complex system analysis. The Great Lakes' intricate water dynamics require ad- vanced hydrological modeling. This research uses a network model to understand the macro-level water interactions, focusing on system-wide insights. The model provides a theoretical basis for Great Lakes water management, improving control over com- plex system interactions.

<!-- b000134 | heading | pages [5] -->
4.2 Model Framework: Representation of Nodes and Edges

<!-- b000135 | prose | pages [5] -->
We view the Great Lakes Basin as a complex network system, with each lake con- sidered as a node within the system, denoted by 𝑁𝑖, where i represents the lake's se- quence number. The water level 𝑊𝑖 of each node is its key attribute. Notably, since Lake Michigan and Lake Huron are geographically adjacent without a clear river sep- aration and are often considered a single body of water based on multiple studies and provided data, we analyze these two lakes as one node in our network model. This approach simplifies the model's complexity while maintaining an accurate description of the lake system's overall dynamics.

<!-- b000136 | prose | pages [5] -->
Every river connecting two lakes is represented as an edge 𝐸𝑖𝑗 connecting nodes 𝑁𝑖 and 𝑁𝑗, with the flow rate from lake i to lake j denoted by 𝑄𝑖𝑗. For rivers controlled

<!-- b000137 | furniture | pages [5] -->


<!-- b000138 | prose | pages [5] -->
关注数学模型

<!-- b000139 | furniture | pages [5] -->
2

<!-- b000140 | furniture | pages [5] -->
MATHmodels

<!-- b000141 | furniture | pages [5] -->
获取更多资讯

<!-- b000142 | furniture | pages [6] -->
Team # 2419588

<!-- b000143 | furniture | pages [6] -->


<!-- b000144 | furniture | pages [6] -->


<!-- b000145 | furniture | pages [6] -->
Page  4  of  22

<!-- b000146 | prose | pages [6] -->
by dams, a control mechanism 𝐶𝑖𝑗 is added to these edges.

<!-- b000147 | heading | pages [6] -->
4.3 Mathematical Formulation of the Network Model

<!-- b000148 | prose | pages [6] -->
Water level serves as an indicator of the lake surface height, while flow rate re- flects the dynamic changes in the water volume of a lake. In studying the hydrological

<!-- b000149 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000150 | prose | pages [6] -->
characteristics of lakes, our goal is to reveal the intrinsic connection between water level and flow rate. Given that the geomorphological characteristics of each lake are relatively stable, we can anticipate a stable relationship between water level and water volume, i.e., the water stage-storage curve. However, the complexity of lake geomor- phology means this relationship can be influenced by various factors. According to the Great Lakes Commission, the surface area of the lakes remains relatively constant over long periods. Statistical analysis of historical data has yielded the following val- ues for average water levels and standard deviations:

<!-- b000151 | caption | pages [6] -->
Table 2: Average Water Levels and Standard Deviations for the Great Lakes

<!-- b000152 | prose | pages [6] -->
Average Water Level (m) Standard Deviation (m) Lake

<!-- b000153 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000154 | prose | pages [6] -->
183.35 Superior 0.25

<!-- b000155 | prose | pages [6] -->
176.33 Michigan and Huron 0.45

<!-- b000156 | prose | pages [6] -->
175.10 St. Clair 0.37

<!-- b000157 | prose | pages [6] -->
174.28 Erie 0.32

<!-- b000158 | prose | pages [6] -->
74.83 Ontario

<!-- b000159 | furniture | pages [6] -->


<!-- b000160 | prose | pages [6] -->
0.29

<!-- b000161 | prose | pages [6] -->
Given the relative stability of lake surface areas and the minor overall impact of water level changes on lakes, it is reasonable to use the lake's surface area as a basis for calculating water level changes.

<!-- b000162 | prose | pages [6] -->
In the Great Lakes system, for any given lake 𝑖, the change in water level 𝛥𝑊𝑖 over a given time interval 𝛥𝑡 can be represented by the following formula:

<!-- b000163 | furniture | pages [6] -->


<!-- b000164 | furniture | pages [6] -->


<!-- b000165 | prose | pages [6] -->
(1)

<!-- b000166 | prose | pages [6] -->
Here, Inflowtotal,𝑖 represents the total inflow into lake 𝑖, Outflowtotal,𝑖 represents the total outflow from lake 𝑖,𝑃𝑟𝑒𝑐𝑖𝑝𝑖 is the precipitation over lake 𝑖, 𝐸𝑣𝑎𝑝𝑖 is the evap- oration from lake 𝑖, and 𝐴𝑖 is the surface area of lake 𝑖.

<!-- b000167 | prose | pages [6] -->
The flow rate 𝑄𝑖𝑗 from lake 𝑖 to lake 𝑗 can be described by a function 𝑓, which re- flects the relationship between the water level difference (𝑊𝑖 and 𝑊𝑗) and the charac- teristics of the river connecting them. The function f may include the effects of dam control (𝐶𝑖𝑗) and can be linear or nonlinear; the specific model will be explored in detail in subsequent research.

<!-- b000168 | heading | pages [6] -->
4.4 River Flow between Lakes

<!-- b000169 | prose | pages [6] -->
In this section, we delve into the river flow rate 𝑄𝑖𝑗 from lake 𝑖 to lake 𝑗, defined as:

<!-- b000170 | furniture | pages [6] -->


<!-- b000171 | furniture | pages [6] -->


<!-- b000172 | prose | pages [6] -->
(2) with the aim of identifying the unknown function 𝑓.

<!-- b000173 | furniture | pages [6] -->


<!-- b000174 | prose | pages [6] -->
关注数学模型

<!-- b000175 | furniture | pages [6] -->
2

<!-- b000176 | furniture | pages [6] -->
MATHmodels

<!-- b000177 | furniture | pages [6] -->
获取更多资讯

<!-- b000178 | furniture | pages [7] -->
Team # 2419588

<!-- b000179 | heading | pages [7] -->
4.4.1 Exploratory Data Analysis (EDA)

<!-- b000180 | furniture | pages [7] -->


<!-- b000181 | furniture | pages [7] -->


<!-- b000182 | furniture | pages [7] -->
Page  5  of  22

<!-- b000183 | prose | pages [7] -->
In this section, we perform Exploratory Data Analysis (EDA) on the Great Lakes system's water level and flow rate data to identify basic features, trends, and patterns. EDA is vital for understanding data structure, spotting outliers, and preparing for

<!-- b000184 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000185 | prose | pages [7] -->
deeper analysis and modeling. Initially, we cleaned the data thoroughly to ensure analysis accuracy. We hypothesized that river flow rates depend on water level dif- ferences between upstream and downstream lakes. To verify this, we analyzed water level differences between such lakes and their correlation with connecting rivers' flow rates using Pearson, Spearman, and Kendall Correlation methods. These methods evaluate linear, non-linear, and rank-order variable relationships. Example analysis with Lake Superior, Lake Michigan, Lake Huron, and the St. Mary's River provided specific correlation coefficients:

<!-- b000186 | prose | pages [7] -->
1.

<!-- b000187 | prose | pages [7] -->
Pearson Correlation: -0.29 2.

<!-- b000188 | prose | pages [7] -->
Spearman Correlation: -0.31 3.

<!-- b000189 | prose | pages [7] -->
Kendall Correlation: -0.20

<!-- b000190 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000191 | prose | pages [7] -->
And visualized the data sets accordingly:

<!-- b000192 | caption | pages [7] -->
Figure 3 Correlation between Water

<!-- b000193 | prose | pages [7] -->
Level Differences and River Flow

<!-- b000194 | prose | pages [7] -->
Rates in the St. Mary's River

<!-- b000195 | furniture | pages [7] -->


<!-- b000196 | furniture | pages [7] -->


<!-- b000197 | furniture | pages [7] -->


<!-- b000198 | caption | pages [7] -->
Figure 4. Histogram of Cross-Corre-

<!-- b000199 | prose | pages [7] -->
lation Function (CCF) for Water Level

<!-- b000200 | prose | pages [7] -->
Differences and River Flow Rates

<!-- b000201 | furniture | pages [7] -->


<!-- b000202 | prose | pages [7] -->
The analysis revealed a very low correlation between water level differences and river flow rates, exhibiting a negative correlation, which contradicts the ex- pected physical phenomena. Given this, we inferred that the effect of water level dif- ferences on river flow might have a time lag. To further explore this possibility, we employed the Cross-Correlation Function (CCF) to analyze correlations at different time lags and generated corresponding histograms.

<!-- b000203 | prose | pages [7] -->
The histogram results showed that, within a time lag range of 0 to 12 months, the correlation between water level differences and river flow rates remained weak. This finding prompted us to reassess our initial hypothesis that water level differ- ences directly influence river flow rates.

<!-- b000204 | heading | pages [7] -->
4.4.2 Determining the Function 𝒇

<!-- b000205 | prose | pages [7] -->
Upon further analysis of the physical scenario involving river flow rates and lake

<!-- b000206 | furniture | pages [7] -->


<!-- b000207 | prose | pages [7] -->
关注数学模型

<!-- b000208 | furniture | pages [7] -->
2

<!-- b000209 | furniture | pages [7] -->
MATHmodels

<!-- b000210 | furniture | pages [7] -->
获取更多资讯

<!-- b000211 | furniture | pages [8] -->
Team # 2419588

<!-- b000212 | furniture | pages [8] -->


<!-- b000213 | furniture | pages [8] -->


<!-- b000214 | furniture | pages [8] -->
Page  6  of  22

<!-- b000215 | prose | pages [8] -->
water levels in the Great Lakes system, we drew a preliminary conclusion based on hydrodynamic principles: the flow rate of rivers is primarily related to the water level of upstream lakes. This conclusion is grounded in the fundamental principles of fluid dynamics, namely, that water flows from higher to lower water levels, and the rate of

<!-- b000216 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000217 | prose | pages [8] -->
flow is influenced by the water level difference and channel characteristics (such as the slope and width of the channel).

<!-- b000218 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000219 | furniture | pages [8] -->


<!-- b000220 | caption | pages [8] -->
Figure 5. Physical Model of River Flow Rates and Lake Water Levels in the Great

<!-- b000221 | prose | pages [8] -->
Lakes System In this physical model, the water level of downstream lakes does not directly af- fect the supply of water from upstream lakes to rivers. Instead, the water level of up- stream lakes determines the amount of water that can pour into the rivers. When the water level of an upstream lake is higher than the elevation at the river's mouth, water naturally flows downstream. This process is driven by gravity, with water flowing along the channel until a new equilibrium state is reached. Therefore, the key factors determining river flow rate are the water level of the upstream lake and the height difference at the river's mouth.

<!-- b000222 | prose | pages [8] -->
To further validate the direct correlation between the water level of upstream lakes and river flow rates, we conducted a detailed correlation analysis between the water level of Lake Superior and the flow rate of the St. Mary's River. The analysis results showed a Pearson Correlation of 0.91, a Spearman Correlation of 0.89, and a Kendall Correlation of 0.72, all indicating a significant positive correlation without evidence of time lag effects.

<!-- b000223 | furniture | pages [8] -->


<!-- b000224 | prose | pages [8] -->
关注数学模型

<!-- b000225 | furniture | pages [8] -->
2

<!-- b000226 | furniture | pages [8] -->
MATHmodels

<!-- b000227 | furniture | pages [8] -->
获取更多资讯

<!-- b000228 | furniture | pages [9] -->
Team # 2419588

<!-- b000229 | furniture | pages [9] -->


<!-- b000230 | furniture | pages [9] -->


<!-- b000231 | furniture | pages [9] -->
Page  7  of  22

<!-- b000232 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000233 | caption | pages [9] -->
Figure 6. Correlation Analysis of

<!-- b000234 | prose | pages [9] -->
Upstream Lake Water Levels and River

<!-- b000235 | prose | pages [9] -->
Flow Rates

<!-- b000236 | caption | pages [9] -->
Figure 7. Heatmap of Correlation

<!-- b000237 | prose | pages [9] -->
Coefficients for Upstream Lake Water

<!-- b000238 | prose | pages [9] -->
Levels and River Flow Rates To rule out coincidence, our study was extended to include all upstream lakes and their downstream rivers, employing matrix analysis to evaluate correlation coef-

<!-- b000239 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000240 | prose | pages [9] -->
ficients, visualized via heatmap. The findings revealed a significant linear positive correlation across upstream lakes' water levels and river flow rates, confirming the hypothesized linear relationship applicable throughout the Great Lakes system. This evidence underpins the use of linear modeling for forecasting and examining the dy- namic interplay between upstream lake water levels and river flow rates.

<!-- b000241 | prose | pages [9] -->
Upon examining the correlations within the Great Lakes system, we noted a rel- atively weaker correlation between Lake Ontario and the St. Lawrence River (correla- tion coefficient of 0.62), while other lakes showed strong linear positive correlations with river flow rates (correlation coefficients over 0.9). These observations validate employing a linear model to represent the relationship between upstream lake water levels and river flow rates, formulated as:

<!-- b000242 | furniture | pages [9] -->


<!-- b000243 | furniture | pages [9] -->


<!-- b000244 | prose | pages [9] -->
(3) where 𝑘 and 𝑏 are coefficients to be determined. The weaker correlation for Lake Ontario and the St. Lawrence River was initially speculated to be due to the confluence of the Ottawa River with the St. Lawrence River. However, upon verification of the monitoring station data (station number 04264331), it was found that this station does not receive inflow from the Ottawa River. Further literature research revealed the root cause: the construction of dams as part of the "Lake Ontario – St. Lawrence Plan 2014" to control water levels, a human activity that disrupted the natural correlation between water levels and flow rates. The official doc- ument of the plan provided the pre-project release relationship formula for Lake On- tario's outflow and its water level:

<!-- b000245 | furniture | pages [9] -->


<!-- b000246 | furniture | pages [9] -->


<!-- b000247 | furniture | pages [9] -->


<!-- b000248 | prose | pages [9] -->
(4)

<!-- b000249 | prose | pages [9] -->
关注数学模型

<!-- b000250 | furniture | pages [9] -->
2

<!-- b000251 | furniture | pages [9] -->
MATHmodels

<!-- b000252 | furniture | pages [9] -->
获取更多资讯

<!-- b000253 | furniture | pages [10] -->
Team # 2419588

<!-- b000254 | furniture | pages [10] -->


<!-- b000255 | furniture | pages [10] -->


<!-- b000256 | furniture | pages [10] -->
Page  8  of  22

<!-- b000257 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000258 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000259 | furniture | pages [10] -->


<!-- b000260 | caption | pages [10] -->
Figure 8. Heatmap of Correlation Coefficients for Upstream Lake Water Levels

<!-- b000261 | prose | pages [10] -->
and River Flow Rates After conducting a linear fitting analysis of the relationship between water levels and flow rates for all lakes, we obtained the following results table. This table details the linear fitting coefficients for each lake, providing a scientific basis for subsequent water resource management and decision-making.

<!-- b000262 | caption | pages [10] -->
Table 3: Linear Fitting Coefficients for Lake and River Pairs

<!-- b000263 | prose | pages [10] -->
Pair

<!-- b000264 | prose | pages [10] -->
Lake Superior - St. Mary's River

<!-- b000265 | prose | pages [10] -->
Lake Michigan and Lake Huron - St.

<!-- b000266 | prose | pages [10] -->
Clair River

<!-- b000267 | prose | pages [10] -->
Lake St. Clair - Detroit River

<!-- b000268 | prose | pages [10] -->
Lake Erie - Niagara River

<!-- b000269 | prose | pages [10] -->
Lake Ontario - St. Lawrence River

<!-- b000270 | prose | pages [10] -->
Relationship

<!-- b000271 | prose | pages [10] -->
𝑄12 = 𝐶12(1713.68𝑊1 −312180.54)

<!-- b000272 | prose | pages [10] -->
𝑄23 = 1504.20𝑊2 −259900.25

<!-- b000273 | prose | pages [10] -->
𝑄34 = 1952.98𝑊3 −336406.51

<!-- b000274 | prose | pages [10] -->
𝑄45 = 2088.92 ∗𝑊4 −357993.82

<!-- b000275 | prose | pages [10] -->
𝑄56 = 555.823𝐶56(𝑊5 −0.035 −69.474)1.5

<!-- b000276 | heading | pages [10] -->
4.5 Incorporating Uncontrollable Factors

<!-- b000277 | prose | pages [10] -->
In addressing the water balance issues within the Great Lakes basin, we inevita- bly encounter numerous complex factors that affect lake water levels and flow rates. However, in this study, we will focus primarily on precipitation and evaporation, as these two components play a pivotal role in the lake water balance. According to re- search by Neff and Nicholas (2004), precipitation and evaporation are the main factors in the lake water balance, significantly impacting the long-term variations in lake wa- ter levels. We will now model and analyze precipitation and evaporation separately.

<!-- b000278 | furniture | pages [10] -->


<!-- b000279 | prose | pages [10] -->
关注数学模型

<!-- b000280 | furniture | pages [10] -->
2

<!-- b000281 | furniture | pages [10] -->
MATHmodels

<!-- b000282 | furniture | pages [10] -->
获取更多资讯

<!-- b000283 | furniture | pages [11] -->
Team # 2419588

<!-- b000284 | heading | pages [11] -->
4.5.1 Precipitation

<!-- b000285 | furniture | pages [11] -->


<!-- b000286 | furniture | pages [11] -->


<!-- b000287 | furniture | pages [11] -->
Page  9  of  22

<!-- b000288 | prose | pages [11] -->
Precipitation often acts as the largest influencing factor on lake storage volumes, but its impact varies across different regions due to distinct geological and geomor- phological characteristics. Intuitively, we know that precipitation 𝑝 (in mm) positively

<!-- b000289 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000290 | prose | pages [11] -->
correlates with water storage brought to lakes, represented by 𝑃+ 𝑅, where we model each lake individually in an exploratory manner.

<!-- b000291 | furniture | pages [11] -->


<!-- b000292 | furniture | pages [11] -->


<!-- b000293 | prose | pages [11] -->
(5)

<!-- b000294 | prose | pages [11] -->
We collected data on the daily change in water level Δ𝑊𝑖, controlled inflows 𝑄𝑖−1,𝑖, controlled outflows 𝑄𝑖,𝑖+1, and precipitation 𝑝𝑖 for lake 𝑖 to fit and determine the precipitation function 𝑃𝑖 for each lake.

<!-- b000295 | prose | pages [11] -->
This approach allows for a nuanced understanding of how precipitation impacts each lake's water balance, accounting for regional differences and contributing to more accurate water management and decision-making strategies. Through fitting these models, we can better predict the effects of precipitation on lake water levels, adjusting for controlled inflows and outflows, and thereby enhancing our ability to

<!-- b000296 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000297 | prose | pages [11] -->
manage the Great Lakes' water resources effectively.

<!-- b000298 | heading | pages [11] -->
4.5.2 Evaporating

<!-- b000299 | prose | pages [11] -->
Evaporation is a primary pathway for water loss in the Great Lakes system, play- ing a crucial role in the hydrological cycle and water resource management of the en- tire basin. We employs the Lumped Modeling approach proposed by Croley (1989), which integrates the Monin-Obukhov similarity theory with a heat storage model to provide a comprehensive computational framework for simulating evaporative fluxes over the Great Lakes.

<!-- b000300 | prose | pages [11] -->
The process begins with the calculation of saturated specific humidity (𝑞𝑠) using the Arden-Buck equation, which describes the specific humidity at saturation under given temperature and atmospheric pressure conditions. The formula for saturated water vapor pressure (𝑒) is as follows:

<!-- b000301 | furniture | pages [11] -->


<!-- b000302 | furniture | pages [11] -->


<!-- b000303 | prose | pages [11] -->
(6)

<!-- b000304 | prose | pages [11] -->
Where 𝑒 is the saturated water vapor pressure in millibars (mb), which can be calculated based on temperature  𝑇𝑤  and atmospheric pressure (Pa). The actual spe- cific humidity (qa) reflects the actual water vapor content in the air, and its calculation is given by:

<!-- b000305 | furniture | pages [11] -->


<!-- b000306 | furniture | pages [11] -->


<!-- b000307 | prose | pages [11] -->
(7)

<!-- b000308 | prose | pages [11] -->
Where  𝑒𝑤 is the water vapor pressure (mb), which can be derived from relative humidity (RH) and atmospheric pressure (Pa).

<!-- b000309 | prose | pages [11] -->
Subsequently, the bulk evaporation coefficient (𝐶𝐸) is determined, a key parame- ter describing the efficiency of water vapor transfer from the water surface to the at- mosphere. The calculation of 𝐶𝐸 involves atmospheric stability analysis, typically

<!-- b000310 | prose | pages [11] -->
𝑍

<!-- b000311 | prose | pages [11] -->
based on the Monin-Obukhov length (𝐿) and stability parameter (

<!-- b000312 | furniture | pages [11] -->


<!-- b000313 | prose | pages [11] -->
𝐿), requiring

<!-- b000314 | prose | pages [11] -->
关注数学模型

<!-- b000315 | furniture | pages [11] -->
2

<!-- b000316 | furniture | pages [11] -->
MATHmodels

<!-- b000317 | furniture | pages [11] -->
获取更多资讯

<!-- b000318 | furniture | pages [12] -->
Team # 2419588

<!-- b000319 | furniture | pages [12] -->


<!-- b000320 | furniture | pages [12] -->


<!-- b000321 | furniture | pages [12] -->
Page  10  of  22

<!-- b000322 | prose | pages [12] -->
meteorological data such as wind speed (𝑈), air temperature (𝑇), and relative humid- ity (RH).

<!-- b000323 | prose | pages [12] -->
The daily evaporation rate (𝐸𝑤) is calculated using the following formula:

<!-- b000324 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000325 | furniture | pages [12] -->


<!-- b000326 | furniture | pages [12] -->


<!-- b000327 | prose | pages [12] -->
(8)

<!-- b000328 | prose | pages [12] -->
In this equation, 𝐸 represents the evaporation rate, 𝐶𝐸 is the bulk evaporation co- efficient, 𝑞𝑤 and 𝑞 are the specific humidities at the water surface and in the air, re- spectively, 𝑈 is the wind speed, 𝑟𝑤 is the density of water, and 𝑟𝑎 is the density of air.

<!-- b000329 | prose | pages [12] -->
Compute 𝐶𝐸 based on the algorithm shown in the accompanying figure and the equation provided in the text. The equation and algorithm are given in the paper.

<!-- b000330 | prose | pages [12] -->
The meanings and units of the physical quantities in the formula are shown in the following table:

<!-- b000331 | prose | pages [12] -->
Description

<!-- b000332 | heading | pages [12] -->
Symbol

<!-- b000333 | prose | pages [12] -->
𝑍 Unit reference height 𝑍𝑤 𝑚 roughness length 𝑚

<!-- b000334 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000335 | prose | pages [12] -->
𝑈 𝑚· 𝑠−1 mean wind speed at reference height Z above the surface 𝑈∗ 𝑚· 𝑠−1 friction velocity 𝑘

<!-- b000336 | furniture | pages [12] -->


<!-- b000337 | prose | pages [12] -->
Von Karman’s constant

<!-- b000338 | furniture | pages [12] -->


<!-- b000339 | prose | pages [12] -->
stability-dependent parameters 𝑆1, 𝑆2 𝐿 𝑚 Moninabukhov length absolute temperature of near-surface air 𝛾 𝐾 acceleration due to gravity 𝑔 𝑚· 𝑠−2 daily evaporation rate 𝐸𝑤 𝑚 The wind speed 𝑈, humidity 𝑞, and temperature 𝑇 are variables that need to be obtained by collecting meteorological and hydrological data. The remaining variables can be derived from existing work or reasonably set. Through these steps, our model enables a dynamic and accurate simulation of the evaporation process for the Great Lakes basin, which is essential for understanding the hydrodynamics of the lakes and informing water resource management strategies.

<!-- b000340 | furniture | pages [12] -->


<!-- b000341 | caption | pages [12] -->
Figure 9. Calculation of 𝑪𝑬

<!-- b000342 | furniture | pages [12] -->


<!-- b000343 | prose | pages [12] -->
关注数学模型

<!-- b000344 | furniture | pages [12] -->
2

<!-- b000345 | furniture | pages [12] -->
MATHmodels

<!-- b000346 | furniture | pages [12] -->
获取更多资讯

<!-- b000347 | furniture | pages [13] -->
Team # 2419588

<!-- b000348 | heading | pages [13] -->
4.5.3 Ice jams

<!-- b000349 | furniture | pages [13] -->


<!-- b000350 | furniture | pages [13] -->


<!-- b000351 | furniture | pages [13] -->
Page  11  of  22

<!-- b000352 | prose | pages [13] -->
In the development of a water balance model for the Great Lakes, the phenome- non of ice jams plays a crucial role in affecting the hydrodynamics of the region. Ice jams occur during winter when the lake surface freezes and the ice can obstruct the

<!-- b000353 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000354 | prose | pages [13] -->
flow of rivers, leading to potential flooding and altered water levels. To accurately represent this phenomenon in our model, we introduce the ice jam factor (\𝑒𝑡𝑎 ), which quantifies the severity of the ice jam and its impact on river flow.

<!-- b000355 | prose | pages [13] -->
The mathematical relationship between the actual river flow (𝜂) and the ice jam factor (𝜂) is expressed as follows:

<!-- b000356 | furniture | pages [13] -->


<!-- b000357 | prose | pages [13] -->
(9)

<!-- b000358 | furniture | pages [13] -->


<!-- b000359 | prose | pages [13] -->
Here, 𝑄𝑝𝑟𝑒 represents the river flow prior to the occurrence of an ice jam. This equation allows us to model the reduction in river flow due to ice jams, where 𝜂 ranges from 0 (no ice jam, full flow) to 1 (complete ice jam, no flow). By incorporating this relationship into our water balance model, we can simulate the effects of ice jams on the Great Lakes' hydrology, providing a more nuanced understanding of the system's

<!-- b000360 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000361 | prose | pages [13] -->
behavior during the winter months and informing strategies for water resource man- agement and flood mitigation.

<!-- b000362 | heading | pages [13] -->
5 Equilibrium Stakeholder Satisfaction (ESS) Model

<!-- b000363 | heading | pages [13] -->
5.1 Overview of the ESS Model

<!-- b000364 | prose | pages [13] -->
The Equilibrium Stakeholder Satisfaction (ESS) Model is a novel approach de- signed to optimize water level management in the Great Lakes, with a focus on Lake Ontario and the St. Lawrence River. It addresses the need to balance the diverse and sometimes conflicting interests of stakeholders in shipping, power generation, conser- vation, recreation, and property values.

<!-- b000365 | prose | pages [13] -->
The ESS Model's objective is to find an optimal water level that maximizes stake- holder satisfaction throughout the year, considering the Great Lakes' complex hydro- logical dynamics, including precipitation, evaporation, runoff, and human activities. It uses mathematical and hydrological analyses to evaluate the effects of water level changes on stakeholders and prioritizes these effects based on their importance.

<!-- b000366 | prose | pages [13] -->
Developed in response to the International Joint Commission's (IJC) call for ad- vanced management strategies, the ESS Model integrates stakeholder satisfaction into water level management decisions, considering technical, hydrological, social, eco- nomic, and environmental factors.

<!-- b000367 | heading | pages [13] -->
5.2 Stakeholder Analysis

<!-- b000368 | prose | pages [13] -->
In the development of the Equilibrium Stakeholder Satisfaction (ESS) Model for Lake Ontario and the St. Lawrence River, a thorough stakeholder analysis is essential to ensure the model accurately reflects the diverse interests and influences of those affected by water level management. This analysis categorizes stakeholders into six primary groups, each with distinct preferences and stakes in water level outcomes. Herein, we delve into the specific interests of these groups and assess their potential impact on water level management through an influence-interest matrix.

<!-- b000369 | furniture | pages [13] -->


<!-- b000370 | prose | pages [13] -->
关注数学模型

<!-- b000371 | furniture | pages [13] -->
2

<!-- b000372 | furniture | pages [13] -->
MATHmodels

<!-- b000373 | furniture | pages [13] -->
获取更多资讯

<!-- b000374 | furniture | pages [14] -->
Team # 2419588

<!-- b000375 | furniture | pages [14] -->


<!-- b000376 | furniture | pages [14] -->


<!-- b000377 | furniture | pages [14] -->
Page  12  of  22

<!-- b000378 | heading | pages [14] -->
5.2.1 Identification and Preferences of Stakeholders

<!-- b000379 | prose | pages [14] -->
Shipping Companies: They require high and stable water levels in the St. Law- rence River for safe navigation and operational efficiency, as fluctuations can disrupt vessel passage and supply chains.

<!-- b000380 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000381 | prose | pages [14] -->
Dock Managers and Montreal Residents: They advocate for consistent and low water levels to prevent flooding and protect waterfront properties and infrastructure, impacting dock operations and community well-being.

<!-- b000382 | prose | pages [14] -->
Environmentalists: They call for water levels that follow natural seasonal varia- tions to support ecosystem health, with higher spring levels for species breeding and waterway cleansing.

<!-- b000383 | prose | pages [14] -->
Property Owners along Lake Ontario: These stakeholders prefer stable water levels to prevent shoreline erosion and protect their investments from water damage and land loss.

<!-- b000384 | prose | pages [14] -->
Recreational Boaters and Fishermen: This group favors stable, accessible water levels to ensure marina and launch ramp usability for boating and fishing activities.

<!-- b000385 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000386 | prose | pages [14] -->
Hydro-Power Generation Companies: They seek to manage water levels effec- tively for hydroelectric power generation, utilizing high levels as a natural reservoir to meet energy demands efficiently.

<!-- b000387 | heading | pages [14] -->
5.2.2 Influence-Interest Matrix

<!-- b000388 | prose | pages [14] -->
The matrix below evaluates each stakeholder group based on their level of inter- est in water level management and their capacity to influence decision-making pro- cesses:

<!-- b000389 | caption | pages [14] -->
Table 4: Influence-Interest Matrix for Stakeholder Groups

<!-- b000390 | prose | pages [14] -->
Stakeholder Group

<!-- b000391 | prose | pages [14] -->
Shipping Companies

<!-- b000392 | prose | pages [14] -->
Dock Managers and Montreal Resi-

<!-- b000393 | prose | pages [14] -->
dents

<!-- b000394 | prose | pages [14] -->
Environmentalists

<!-- b000395 | prose | pages [14] -->
Property Owners

<!-- b000396 | prose | pages [14] -->
Recreational Boaters and Fishermen

<!-- b000397 | prose | pages [14] -->
Hydro-Power Generation Companies

<!-- b000398 | prose | pages [14] -->
Level of Interest Potential to Influence

<!-- b000399 | prose | pages [14] -->
High High

<!-- b000400 | prose | pages [14] -->
High Medium

<!-- b000401 | prose | pages [14] -->
High Medium

<!-- b000402 | prose | pages [14] -->
High Low

<!-- b000403 | prose | pages [14] -->
Medium Low

<!-- b000404 | prose | pages [14] -->
High High

<!-- b000405 | prose | pages [14] -->
High Interest & High Influence: Shipping companies and hydro-power genera- tion companies possess significant resources to advocate for their interests, making them key players in water level management discussions.

<!-- b000406 | prose | pages [14] -->
High Interest & Medium Influence: Environmentalists and dock managers/res- idents are highly vested in water level outcomes but have moderate influence, largely due to public support and localized impact.

<!-- b000407 | prose | pages [14] -->
High Interest & Low Influence: Property owners, despite their direct stake, often lack the organized representation needed to exert substantial influence.

<!-- b000408 | prose | pages [14] -->
Medium Interest & Low Influence: Recreational users, while affected by water

<!-- b000409 | furniture | pages [14] -->


<!-- b000410 | prose | pages [14] -->
关注数学模型

<!-- b000411 | furniture | pages [14] -->
2

<!-- b000412 | furniture | pages [14] -->
MATHmodels

<!-- b000413 | furniture | pages [14] -->
获取更多资讯

<!-- b000414 | furniture | pages [15] -->
Team # 2419588

<!-- b000415 | furniture | pages [15] -->


<!-- b000416 | furniture | pages [15] -->


<!-- b000417 | furniture | pages [15] -->
Page  13  of  22

<!-- b000418 | prose | pages [15] -->
levels, typically do not have the collective capacity or economic impact to significantly sway management decisions.

<!-- b000419 | heading | pages [15] -->
5.3 Stakeholder Satisfaction and Weighting

<!-- b000420 | prose | pages [15] -->
The ESS Model addresses Lake Ontario and St. Lawrence River water level man-

<!-- b000421 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000422 | prose | pages [15] -->
agement by incorporating stakeholder satisfaction into its analytical framework. It uses mathematical functions to quantify how stakeholder satisfaction changes with water levels, providing a basis for optimizing water levels. Weights are assigned to these functions to represent the stakeholders' relative influence, ensuring a balanced consideration of diverse interests and an equitable outcome.

<!-- b000423 | heading | pages [15] -->
5.3.1 Satisfaction Functions

<!-- b000424 | prose | pages [15] -->
The Equilibrium Stakeholder Satisfaction (ESS) Model quantifies how water level variations impact stakeholder contentment within Lake Ontario and the St. Lawrence River, employing distinct satisfaction functions for each group. Generalized Satisfaction Function: The general formula for calculating stakeholder satisfaction (𝑆𝑖) with respect to water

<!-- b000425 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000426 | prose | pages [15] -->
levels (𝑊) is:

<!-- b000427 | prose | pages [15] -->
𝑆𝑖(𝑊) = 1 −|

<!-- b000428 | prose | pages [15] -->
𝑊−𝑊𝑖𝑑𝑒𝑎𝑙𝑖

<!-- b000429 | prose | pages [15] -->
|

<!-- b000430 | prose | pages [15] -->
𝑊𝑟𝑎𝑛𝑔𝑒𝑖

<!-- b000431 | prose | pages [15] -->
𝑆𝑖: Satisfaction score for stakeholder 𝑖.  𝑊: Current water level.  𝑊𝑖𝑑𝑒𝑎𝑙𝑖: Ideal water level for stakeholder 𝑖.  𝑊𝑟𝑎𝑛𝑔𝑒𝑖: Acceptable range of water levels for stakeholder 𝑖.  Tailored Satisfaction Functions:

<!-- b000432 | prose | pages [15] -->
1.

<!-- b000433 | prose | pages [15] -->
Shipping Companies (𝑆1):

<!-- b000434 | prose | pages [15] -->
a) Objective: Ensure navigable conditions for medium-sized vessels in the

<!-- b000435 | prose | pages [15] -->
St. Lawrence River. b) Parameters: Vessels' design specifications require a minimum navigation

<!-- b000436 | prose | pages [15] -->
depth of 8.3 meters to maintain a satisfaction level of 1. This translates to a Lake Ontario water level of at least 74.4 meters. Below 68 meters, naviga- tion becomes impossible, dropping satisfaction to 0. c) Function: The satisfaction function for shipping companies, considering

<!-- b000437 | prose | pages [15] -->
water depth as the primary factor, is modeled as:

<!-- b000438 | furniture | pages [15] -->


<!-- b000439 | furniture | pages [15] -->


<!-- b000440 | prose | pages [15] -->
(10)

<!-- b000441 | prose | pages [15] -->
Dock Managers and Montreal Residents (𝑆2): 2.

<!-- b000442 | prose | pages [15] -->
a) Objective: Maintain water levels that prevent flooding while ensuring

<!-- b000443 | prose | pages [15] -->
port operation efficiency. b) Parameters: Analysis of the Port of Montreal data and the 2017 flood dis-

<!-- b000444 | prose | pages [15] -->
aster reveals an optimal water level range between 74.4 meters and 76.4

<!-- b000445 | furniture | pages [15] -->


<!-- b000446 | prose | pages [15] -->
关注数学模型

<!-- b000447 | furniture | pages [15] -->
2

<!-- b000448 | furniture | pages [15] -->
MATHmodels

<!-- b000449 | furniture | pages [15] -->
获取更多资讯

<!-- b000450 | furniture | pages [16] -->
Team # 2419588

<!-- b000451 | furniture | pages [16] -->


<!-- b000452 | furniture | pages [16] -->


<!-- b000453 | furniture | pages [16] -->
Page  14  of  22

<!-- b000454 | prose | pages [16] -->
meters for Lake Ontario to mitigate flood risks and maintain port opera- tions. Satisfaction is maximized (1) within this range and decreases outside of it due to increased flood risk or operational inefficiency. c) Function: Satisfaction for this group inversely correlates with water levels

<!-- b000455 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000456 | prose | pages [16] -->
beyond the identified safe operational range:

<!-- b000457 | furniture | pages [16] -->


<!-- b000458 | prose | pages [16] -->
3.

<!-- b000459 | prose | pages [16] -->
Environmentalists (𝑆3):

<!-- b000460 | furniture | pages [16] -->


<!-- b000461 | prose | pages [16] -->
(11)

<!-- b000462 | prose | pages [16] -->
a) Objective: Support ecological health through pronounced seasonal water

<!-- b000463 | prose | pages [16] -->
level variations. b) Parameters: Environmentalists advocate for a water level range that pro-

<!-- b000464 | prose | pages [16] -->
motes biodiversity and natural shoreline processes. The satisfaction level

<!-- b000465 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000466 | prose | pages [16] -->
peaks when Lake Ontario's water levels facilitate natural habitat preserva- tion and seasonal variations. c) Function: Given the preference for natural fluctuation, the satisfaction

<!-- b000467 | prose | pages [16] -->
function for environmentalists might resemble a sinusoidal pattern over the course of a year, reflecting higher satisfaction with greater seasonal amplitude. However, for simplicity and in line with available data, a mod- ified linear approach can be applied, focusing on the range of water levels that are deemed ecologically beneficial:

<!-- b000468 | furniture | pages [16] -->


<!-- b000469 | furniture | pages [16] -->


<!-- b000470 | prose | pages [16] -->
(12)

<!-- b000471 | prose | pages [16] -->
Property Owners, Recreational Boaters, and Fishermen (𝑆4 & 𝑆5): 4.

<!-- b000472 | prose | pages [16] -->
a) Objective: Maintain water levels conducive to property integrity and rec-

<!-- b000473 | prose | pages [16] -->
reational activities. b) Parameters: These stakeholders prefer stable water levels to minimize ero-

<!-- b000474 | prose | pages [16] -->
sion and facilitate recreational activities. Ideal conditions are identified be- tween 74 meters and 76 meters for Lake Ontario, where satisfaction is at its peak. c) Function: The satisfaction function for property owners and recreational

<!-- b000475 | prose | pages [16] -->
users emphasizes stability within the preferred range, decreasing as levels move outside this range due to increased risks or reduced accessibility:

<!-- b000476 | furniture | pages [16] -->


<!-- b000477 | furniture | pages [16] -->


<!-- b000478 | prose | pages [16] -->
(13)

<!-- b000479 | prose | pages [16] -->
Here, the range centers around 75 meters, with satisfaction declining linearly as water levels diverge from this midpoint.

<!-- b000480 | prose | pages [16] -->
Hydro-Power Generation Companies (𝑆6): 5.

<!-- b000481 | furniture | pages [16] -->


<!-- b000482 | prose | pages [16] -->
关注数学模型

<!-- b000483 | furniture | pages [16] -->
2

<!-- b000484 | furniture | pages [16] -->
MATHmodels

<!-- b000485 | furniture | pages [16] -->
获取更多资讯

<!-- b000486 | furniture | pages [17] -->
Team # 2419588

<!-- b000487 | furniture | pages [17] -->


<!-- b000488 | furniture | pages [17] -->


<!-- b000489 | furniture | pages [17] -->
Page  15  of  22

<!-- b000490 | prose | pages [17] -->
a) Objective: Maximize energy generation efficiency through optimal water

<!-- b000491 | prose | pages [17] -->
level management. b) Parameters: Hydroelectric power generation is optimized at higher water

<!-- b000492 | prose | pages [17] -->
levels, with operational thresholds based on the design and capacity of fa-

<!-- b000493 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000494 | prose | pages [17] -->
cilities like the Moses-Saunders Dam. An ideal water level for maximizing power generation efficiency and safety is established at or above 75.5 me- ters. c) Function: The satisfaction function reflects a preference for higher water

<!-- b000495 | prose | pages [17] -->
levels, plateauing once operational maximums are reached to indicate no further gains in satisfaction:

<!-- b000496 | furniture | pages [17] -->


<!-- b000497 | heading | pages [17] -->
5.3.2 Weight Assignment

<!-- b000498 | furniture | pages [17] -->


<!-- b000499 | prose | pages [17] -->
(14)

<!-- b000500 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000501 | prose | pages [17] -->
To enable the ESS Model to equitably manage the varied stakeholder interests in the water levels of Lake Ontario and the St. Lawrence River, structured weight alloca- tion is crucial. These weights measure each stakeholder group's relative impact, steer- ing the optimization towards solutions that meet comprehensive economic, ecological, and social goals. A succinct overview of the weight distribution follows:

<!-- b000502 | caption | pages [17] -->
Table 5: Stakeholder Satisfaction Functions and Assigned Weights

<!-- b000503 | prose | pages [17] -->
Stakeholder Group Shipping Companies Assigned Weight 0.20 Dock Managers and Montreal Residents Environmentalists Property Owners 0.15 0.15 0.10 Recreational Boaters and Fishermen 0.10 Hydro-Power Generation Companies 0.20 The weights assigned in the ESS Model represent the stakeholders' relative influ- ence in decision-making, considering their economic, ecological, and social impacts, as well as policy influence. These weights, ranging from 0 to 1, are based on the Influ- ence-Interest Matrix. Shipping and hydropower stakeholders have the highest weights due to their economic significance. Environmentalists and dock manag- ers/residents receive moderate weights for their influence on public opinion and local economies. Property owners and recreational users are assigned the lowest weights, reflecting their localized concerns.

<!-- b000504 | heading | pages [17] -->
5.4 Calculation of Optimal Water Level

<!-- b000505 | heading | pages [17] -->
5.4.1 Aggregation of Stakeholder Satisfaction

<!-- b000506 | prose | pages [17] -->
To determine the optimal water level, 𝑊𝑜𝑝𝑡, that maximizes stakeholder satisfac- tion for Lake Ontario and the St. Lawrence River, we apply a weighted satisfaction model. This involves assigning weights to each stakeholder's satisfaction function based on their importance, and then aggregating these to calculate a collective satis- faction score.

<!-- b000507 | furniture | pages [17] -->


<!-- b000508 | prose | pages [17] -->
关注数学模型

<!-- b000509 | furniture | pages [17] -->
2

<!-- b000510 | furniture | pages [17] -->
MATHmodels

<!-- b000511 | furniture | pages [17] -->
获取更多资讯

<!-- b000512 | furniture | pages [18] -->
Team # 2419588

<!-- b000513 | furniture | pages [18] -->


<!-- b000514 | furniture | pages [18] -->


<!-- b000515 | furniture | pages [18] -->
Page  16  of  22

<!-- b000516 | prose | pages [18] -->
Each stakeholder's weighted satisfaction score is defined as:

<!-- b000517 | furniture | pages [18] -->


<!-- b000518 | prose | pages [18] -->
(15)

<!-- b000519 | furniture | pages [18] -->


<!-- b000520 | prose | pages [18] -->
𝑆𝑊𝑖(𝑊): Weighted satisfaction score for stakeholder 𝑖 at water level 𝑊. 1.

<!-- b000521 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000522 | prose | pages [18] -->
𝑤𝑒𝑖𝑔ℎ𝑡𝑖: Assigned weight reflecting stakeholder 𝑖's influence. 2.

<!-- b000523 | prose | pages [18] -->
𝑆𝑖(𝑊): Satisfaction function for stakeholder 𝑖, indicating satisfaction at 3.

<!-- b000524 | prose | pages [18] -->
water level 𝑊. The overall satisfaction, 𝑆𝑡𝑜𝑡𝑎𝑙(𝑊), across all stakeholders is the sum of individual weighted scores:

<!-- b000525 | furniture | pages [18] -->


<!-- b000526 | prose | pages [18] -->
The model seeks 𝑊𝑜𝑝𝑡 where:

<!-- b000527 | furniture | pages [18] -->


<!-- b000528 | prose | pages [18] -->
(16)

<!-- b000529 | furniture | pages [18] -->


<!-- b000530 | prose | pages [18] -->
(17)

<!-- b000531 | furniture | pages [18] -->


<!-- b000532 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000533 | prose | pages [18] -->
This method identifies the water level that, considering all stakeholder weights and preferences, achieves the highest aggregate satisfaction, representing an equilib- rium point of collective benefit.

<!-- b000534 | heading | pages [18] -->
6 Dam Control Algorithm Implementation

<!-- b000535 | heading | pages [18] -->
6.1 Control Objectives and Performance Metrics

<!-- b000536 | prose | pages [18] -->
The control strategy for the Great Lakes water system aims to achieve optimal water level regulation across interconnected lakes and rivers. Based on previously es- tablished hydrological and ideal water level models, this strategy utilizes Model Pre- dictive Control (MPC) to formulate an optimization problem at each control interval. The objective is to minimize the deviation between actual water levels and their ideal states while considering system constraints and operational costs.

<!-- b000537 | heading | pages [18] -->
6.2 MPC Model

<!-- b000538 | prose | pages [18] -->
The optimization problem is defined as follows: First, we define the objective function. The objective function aims to minimize the sum of the weighted squared deviations of water levels and inter-lake exchange flows from their ideal values over a prediction horizon of 𝑁0 weeks. This is repre- sented by the performance metric J:

<!-- b000539 | furniture | pages [18] -->


<!-- b000540 | prose | pages [18] -->
(18)

<!-- b000541 | prose | pages [18] -->
The constraints include maintaining water levels within safe operational limits and ensuring that the exchange flows between lakes do not exceed their capacity:

<!-- b000542 | furniture | pages [18] -->


<!-- b000543 | furniture | pages [18] -->


<!-- b000544 | furniture | pages [18] -->


<!-- b000545 | prose | pages [18] -->
(19)

<!-- b000546 | furniture | pages [18] -->


<!-- b000547 | prose | pages [18] -->
(20) The control input at each time step is the release volume from each lake to the downstream lake, which is subject to the constraints and the objective function:

<!-- b000548 | furniture | pages [18] -->


<!-- b000549 | furniture | pages [18] -->


<!-- b000550 | prose | pages [18] -->
(21) where  𝑢𝑖(𝑘) is the control action for 𝑁𝑖 at 𝑘 week.

<!-- b000551 | furniture | pages [18] -->


<!-- b000552 | prose | pages [18] -->
关注数学模型

<!-- b000553 | furniture | pages [18] -->
2

<!-- b000554 | furniture | pages [18] -->
MATHmodels

<!-- b000555 | furniture | pages [18] -->
获取更多资讯

<!-- b000556 | furniture | pages [19] -->
Team # 2419588

<!-- b000557 | furniture | pages [19] -->


<!-- b000558 | furniture | pages [19] -->


<!-- b000559 | furniture | pages [19] -->
Page  17  of  22

<!-- b000560 | prose | pages [19] -->
To solve this optimization problem, a genetic algorithm (GA) is employed. By leveraging the power of genetic algorithms, the control strategy is capable of efficiently navigating the complex search space of the optimization problem, ensuring the Great Lakes water system operates within the desired parameters while minimiz-

<!-- b000561 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000562 | prose | pages [19] -->
ing environmental and economic impacts.

<!-- b000563 | heading | pages [19] -->
7 Dam Control Algorithm

<!-- b000564 | heading | pages [19] -->
7.1 Analysis of Plan2014

<!-- b000565 | heading | pages [19] -->
7.1.1 Bv7 Algorithm

<!-- b000566 | prose | pages [19] -->
The Plan 2014 Algorithm, as detailed in the "Lake Ontario - St. Lawrence River Plan 2014," is a sophisticated water management tool designed to regulate the water levels of Lake Ontario and the St. Lawrence River. The algorithm is based on a combi- nation of mechanistic release rules, known as "Bv7," and discretionary decisions made by the International Lake Ontario - St. Lawrence River Board (ILOSLRS) to address deviations from the specified flows under certain conditions.

<!-- b000567 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000568 | prose | pages [19] -->
The algorithm uses a sliding rule curve, which is a function of the pre-project stage-discharge relationship adjusted for recent long-term supply conditions 𝑄𝑖,𝑖+1.

<!-- b000569 | prose | pages [19] -->
For periods of above-normal supply, the lake release is determined by:

<!-- b000570 | furniture | pages [19] -->


<!-- b000571 | furniture | pages [19] -->


<!-- b000572 | prose | pages [19] -->
(22)

<!-- b000573 | prose | pages [19] -->
Conversely, for periods of below-normal supply, the lake release is calculated as:

<!-- b000574 | furniture | pages [19] -->


<!-- b000575 | furniture | pages [19] -->


<!-- b000576 | prose | pages [19] -->
(23)

<!-- b000577 | prose | pages [19] -->
The algorithm also incorporates flow limits to prevent extreme fluctuations in river flows, ensuring stable conditions for navigation, ice formation, and environmen- tal health. These limits include the J Limit, M Limit, I Limit, and L Limit, which re- spectively control the maximum change in flow, balance low levels for navigation, ensure ice stability, and maintain adequate levels for navigation and overall flow.

<!-- b000578 | heading | pages [19] -->
7.1.2 The Strength & Weakness of Bv7 Algorithm

<!-- b000579 | prose | pages [19] -->
The Bv7 algorithm, as implemented in the Plan 2014, demonstrates several strengths in its water management capabilities. It incorporates a robust predictive framework that accounts for a variety of hydrological conditions, ensuring a stable water exchange between Lake Ontario and the St. Lawrence River. This algorithm has been effective in balancing the diverse interests of navigation, power generation, and ecological health, providing a comprehensive approach to water regulation.

<!-- b000580 | prose | pages [19] -->
However, the algorithm's performance in 2017 highlighted a critical weakness: its sensitivity to high water levels. The model's response to the significant precipitation event that summer was not as agile as required, leading to elevated water levels and potential flood risks. This indicates a need for enhanced sensitivity in the algorithm, particularly in its ability to anticipate and react to extreme weather events and rapid changes in water supply.

<!-- b000581 | furniture | pages [19] -->


<!-- b000582 | prose | pages [19] -->
关注数学模型

<!-- b000583 | furniture | pages [19] -->
2

<!-- b000584 | furniture | pages [19] -->
MATHmodels

<!-- b000585 | furniture | pages [19] -->
获取更多资讯

<!-- b000586 | furniture | pages [20] -->
Team # 2419588

<!-- b000587 | furniture | pages [20] -->


<!-- b000588 | furniture | pages [20] -->


<!-- b000589 | furniture | pages [20] -->


<!-- b000590 | furniture | pages [20] -->
Page  18  of  22

<!-- b000591 | prose | pages [20] -->
(24)

<!-- b000592 | heading | pages [20] -->
7.2 The modification of the Rule Curve

<!-- b000593 | prose | pages [20] -->
Our proposed control strategy is grounded in Model Predictive Control (MPC), a

<!-- b000594 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000595 | prose | pages [20] -->
method that anticipates the system's state over a future horizon and optimizes the control inputs at each control interval. The essence of MPC is to transform the control problem into an optimization problem over a finite time horizon. Given the limitations of our meteorological forecasting capabilities and the need to prevent drastic changes in dam outflow that could disrupt the ecological environment, MPC offers a suitable control approach.

<!-- b000596 | prose | pages [20] -->
We acknowledge the value of the control techniques employed in Plan 2014 and aim to enhance the model's sensitivity to water levels by refining its release rules. To this end, we have introduced a modified equation for the lake outflow when the sup- ply is above normal levels:

<!-- b000597 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000598 | furniture | pages [20] -->


<!-- b000599 | prose | pages [20] -->
ℎ𝑖𝑑𝑒𝑎𝑙

<!-- b000600 | prose | pages [20] -->
(25)

<!-- b000601 | prose | pages [20] -->
𝜎)𝛼 captures the deviation of the water level

<!-- b000602 | prose | pages [20] -->
In this equation, the term (𝑊(𝑡) −

<!-- b000603 | prose | pages [20] -->
from the ideal state, with 𝛼 serving a role analogous to 𝑃1 in the original Plan 2014 model. The inclusion of this term allows the model to respond more dynamically to deviations in water levels, ensuring a more sensitive and adaptive control strategy.

<!-- b000604 | prose | pages [20] -->
The parameter 𝜎 represents a scaling factor that adjusts the sensitivity of the model to water level deviations. By tuning 𝜎 and 𝛼, we can fine-tune the model's re- sponsiveness to both short-term fluctuations and long-term trends in water levels, thus achieving a balance between ecological protection and efficient water manage- ment.

<!-- b000605 | prose | pages [20] -->
Using J as the control objective, we optimized and fitted the model parameters using annual data.

<!-- b000606 | heading | pages [20] -->
8 Assessing Control Algorithm Sensitivity in 2017

<!-- b000607 | prose | pages [20] -->
In 2017, the Great Lakes experienced significant fluctuations in water levels, prompting a reassessment of the control algorithms for dam outflows. This chapter investigates whether the existing algorithms adequately adjusted to these fluctuations, with a focus on aligning water management practices more closely with the varying needs of stakeholders. The analysis aims to determine if modifications to the algo- rithms could result in more satisfactory water levels for all parties involved.

<!-- b000608 | heading | pages [20] -->
8.1 Data Collection and Model Simulation

<!-- b000609 | prose | pages [20] -->
Utilizing detailed hydrological and environmental data for 2017, sourced from the U.S. Army Corps of Engineers' Great Lakes Information website, we incorporated key indicators such as precipitation and evaporation rates into our network model. This data foundation enabled the simulation of the Great Lakes' hydrological dynam- ics throughout the calendar year.

<!-- b000610 | furniture | pages [20] -->


<!-- b000611 | prose | pages [20] -->
关注数学模型

<!-- b000612 | furniture | pages [20] -->
2

<!-- b000613 | furniture | pages [20] -->
MATHmodels

<!-- b000614 | furniture | pages [20] -->
获取更多资讯

<!-- b000615 | furniture | pages [21] -->
Team # 2419588

<!-- b000616 | furniture | pages [21] -->


<!-- b000617 | furniture | pages [21] -->
Page  19  of  22

<!-- b000618 | heading | pages [21] -->
8.2 Simulation Results and Analysis

<!-- b000619 | prose | pages [21] -->
The following charts compare the actual monthly water levels of the lakes in 2017 (provided in the appendix) with the simulated data from the network model:

<!-- b000620 | prose | pages [21] -->
From the charts, it is evident that, with the exception of a few days where the

<!-- b000621 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000622 | prose | pages [21] -->
simulated data deviate significantly from the optimal water levels, the majority of the data closely approximate the ideal water levels.

<!-- b000623 | heading | pages [21] -->
8.3 Sensitivity Assessment of Control Algorithms

<!-- b000624 | prose | pages [21] -->
we dissect the moments when the simulated water levels diverged from actual observations, pinpointing the algorithms' responsiveness to rapid environmental shifts. Specific instances of deviation—particularly during periods of abrupt precipi- tation changes or evaporation spikes—serve as case studies. Through regression anal- ysis, we quantify the algorithms' delay in response and the accuracy of their adjust- ments, identifying patterns that suggest areas for algorithmic refinement. This scru- tiny reveals how the algorithms' current configurations might be fine-tuned to en- hance their predictive accuracy and response speed, thereby minimizing discrepan-

<!-- b000625 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000626 | prose | pages [21] -->
cies between simulated and actual water levels.

<!-- b000627 | furniture | pages [21] -->


<!-- b000628 | caption | pages [21] -->
Figure 10. 2017 Simulation

<!-- b000629 | heading | pages [21] -->
8.4 Stakeholder Impact Evaluation

<!-- b000630 | prose | pages [21] -->
The evaluation of stakeholder impacts centers on correlating the simulated water level adjustments with predefined satisfaction indices for each stakeholder group. By overlaying the periods of significant algorithmic deviation with stakeholder satisfac- tion scores, we identify which stakeholder groups were most adversely affected by suboptimal water management. For instance, a detailed analysis is conducted on how deviations impacted shipping schedules, hydroelectric power generation, and ecolog- ical conservation efforts. This examination not only highlights the direct consequences of algorithmic performance on each stakeholder group but also proposes targeted im- provements to ensure that future algorithm adjustments more effectively balance the competing needs of all parties involved in the Great Lakes ecosystem.

<!-- b000631 | furniture | pages [21] -->


<!-- b000632 | prose | pages [21] -->
关注数学模型

<!-- b000633 | furniture | pages [21] -->
2

<!-- b000634 | furniture | pages [21] -->
MATHmodels

<!-- b000635 | furniture | pages [21] -->
获取更多资讯

<!-- b000636 | furniture | pages [22] -->
Team # 2419588

<!-- b000637 | furniture | pages [22] -->


<!-- b000638 | furniture | pages [22] -->


<!-- b000639 | furniture | pages [22] -->
Page  20  of  22

<!-- b000640 | heading | pages [22] -->
8.5 Algorithm Sensitivity to Environmental Changes

<!-- b000641 | prose | pages [22] -->
The sensitivity of our control algorithms to environmental conditions—specifi- cally, precipitation, winter snowpack, and ice jams—is critically assessed in this sec- tion. By integrating environmental variability into our network model, we observed

<!-- b000642 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000643 | prose | pages [22] -->
the algorithms' performance under a range of scenarios reflective of the diverse cli- matic challenges the Great Lakes face annually.

<!-- b000644 | heading | pages [22] -->
Precipitation: The algorithms demonstrated a calibrated response to increased

<!-- b000645 | prose | pages [22] -->
precipitation, adjusting outflows to mitigate potential flooding. However, the reaction time to sudden, heavy rainfall events highlighted a need for more rapid adaptation capabilities.

<!-- b000646 | prose | pages [22] -->
Winter Snowpack: The gradual melting of winter snowpack presents a predicta- ble rise in water levels, to which the algorithms generally adapted well. The model simulations for spring thaws showed alignment with expected water level increases, suggesting adequate sensitivity to snowpack melting rates.

<!-- b000647 | prose | pages [22] -->
Ice Jams: Ice jams, which can cause abrupt and localized water level rises, tested

<!-- b000648 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000649 | prose | pages [22] -->
the limits of the algorithms' responsiveness. Instances of ice jams within the simula- tion period revealed occasional delays in outflow adjustments, underscoring an area for algorithmic improvement in handling such unpredictable events.

<!-- b000650 | heading | pages [22] -->
9 Model Evaluation and Further Discussion

<!-- b000651 | heading | pages [22] -->
9.1 Strengths

<!-- b000652 | prose | pages [22] -->
The model excels in offering a macro-level view of the Great Lakes system through a comprehensive network of lakes and rivers, balancing system complexity with overall dynamics accuracy. It incorporates stakeholder preferences into water level management via the Equilibrium Stakeholder Satisfaction (ESS) Model, ensuring equitable decision-making. Enhanced predictive accuracy is achieved by integrating meteorological and hydrological data, with Model Predictive Control (MPC) and ge- netic algorithms optimizing dam control strategies to minimize environmental and economic impacts.

<!-- b000653 | heading | pages [22] -->
9.2 Weaknesses

<!-- b000654 | prose | pages [22] -->
The model's representation of the Great Lakes as network nodes overlooks time lags caused by the lakes' vast areas, affecting water level responses. It excludes groundwater, tributaries, and surface runoff impacts on the hydrological balance. Simplifications in modeling natural factors like precipitation and evaporation may not fully mirror real-world conditions, including ice cover effects. Stakeholder satisfaction functions, based on linear relationships and assumptions, may not truly reflect stake- holder preferences, potentially leading to suboptimal management decisions.

<!-- b000655 | heading | pages [22] -->
9.3 Further Discussion

<!-- b000656 | prose | pages [22] -->
Enhancements are needed to capture the Great Lakes system's complexity better and improve predictive accuracy. Future research should include more detailed spa- tial and temporal data, integrate groundwater and surface runoff, and employ ad- vanced meteorological data for natural factor modeling. Stakeholder satisfaction func- tions require empirical validation to ensure they accurately represent diverse interests.

<!-- b000657 | furniture | pages [22] -->


<!-- b000658 | prose | pages [22] -->
关注数学模型

<!-- b000659 | furniture | pages [22] -->
2

<!-- b000660 | furniture | pages [22] -->
MATHmodels

<!-- b000661 | furniture | pages [22] -->
获取更多资讯

<!-- b000662 | furniture | pages [23] -->
Team # 2419588

<!-- b000663 | furniture | pages [23] -->


<!-- b000664 | furniture | pages [23] -->


<!-- b000665 | furniture | pages [23] -->
Page  21  of  22

<!-- b000666 | prose | pages [23] -->
By addressing these limitations and refining its components, the model can become a more effective tool for sustainable water resource management in the region.

<!-- b000667 | heading | pages [23] -->
10 Conclusion

<!-- b000668 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000669 | prose | pages [23] -->
This research has successfully developed and implemented an Adaptive Hydrolog- ical Network Simulation and an Equilibrium Stakeholder Satisfaction (ESS) Model to address the intricate water level management challenges of the Great Lakes. Our ap- proach has demonstrated the potential to effectively balance the diverse and often conflicting interests of various stakeholders, including shipping, power generation, conservation, and recreational activities, within the constraints of the Great Lakes' hy- drological dynamics.

<!-- b000670 | prose | pages [23] -->
The modified dam control algorithm, based on Model Predictive Control (MPC), has shown improved responsiveness to environmental changes, particularly in the face of extreme weather events. The ESS Model's stakeholder satisfaction functions have been carefully calibrated to reflect the nuanced preferences of each stakeholder group, en-

<!-- b000671 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000672 | prose | pages [23] -->
suring that the water level management decisions are equitable and considerate of all parties involved.

<!-- b000673 | prose | pages [23] -->
Despite the promising results, our study acknowledges several areas for future im- provement. The model's simplification of natural factors, such as precipitation and evaporation, may not fully capture the complexities of real-world conditions, includ- ing the effects of ice cover. Additionally, the stakeholder satisfaction functions, while tailored, require empirical validation to ensure they accurately represent the true pref- erences of the stakeholders.

<!-- b000674 | prose | pages [23] -->
Looking ahead, further research should focus on refining the model to incorporate more detailed spatial and temporal data, integrate groundwater and surface runoff dynamics, and utilize advanced meteorological data for more accurate natural factor modeling. Empirical validation of stakeholder satisfaction functions is also crucial to ensure that the model's predictions align with real-world stakeholder preferences and outcomes.

<!-- b000675 | prose | pages [23] -->
By addressing these limitations and enhancing the model's components, we believe that our approach can become a more robust and effective tool for sustainable water resource management in the Great Lakes region, contributing to the long-term ecolog- ical health and economic vitality of this vital freshwater system.

<!-- b000676 | furniture | pages [23] -->


<!-- b000677 | furniture | pages [23] -->


<!-- b000678 | furniture | pages [23] -->


<!-- b000679 | prose | pages [23] -->
关注数学模型

<!-- b000680 | furniture | pages [23] -->
2

<!-- b000681 | furniture | pages [23] -->
MATHmodels

<!-- b000682 | furniture | pages [23] -->
获取更多资讯

<!-- b000683 | furniture | pages [24] -->
Team # 2419588

<!-- b000684 | heading | pages [24] -->
References

<!-- b000685 | furniture | pages [24] -->


<!-- b000686 | furniture | pages [24] -->


<!-- b000687 | furniture | pages [24] -->
Page  22  of  22

<!-- b000688 | references | pages [24] -->
[1] Wilcox, D.A., Thompson, T.A., Booth, R.K., & Nicholas, J.R. (2007). Lake-level var-

<!-- b000689 | references | pages [24] -->
iability and water availability in the Great Lakes. U.S. Geological Survey Circular

<!-- b000690 | references | pages [24] -->
微信公众号：数学模型

<!-- b000691 | references | pages [24] -->
1311, 25 p.

<!-- b000692 | references | pages [24] -->
[2] U.S. Army Corps of Engineers. (n.d.). Water level data. Retrieved February 6, 2024,

<!-- b000693 | references | pages [24] -->
https://www.lre.usace.army.mil/Missions/Great-Lakes-Infor-

<!-- b000694 | references | pages [24] -->
from

<!-- b000695 | references | pages [24] -->
mation/Great-Lakes-Information-2/Water-Level-Data/

<!-- b000696 | references | pages [24] -->
[3] Dias, N. L., Hoeltgebaum, L. E. B., & Santos, I. (2023). STAEBLE: A surface-tem-

<!-- b000697 | references | pages [24] -->
perature- and available-energy-based lake evaporation model. Water Resources

<!-- b000698 | references | pages [24] -->
Research, 59, e2022WR033012. https://doi.org/10.1029/2022WR033012

<!-- b000699 | references | pages [24] -->
[4] Neff, B.P., & Nicholas, J.R. (2005). Uncertainty in the Great Lakes Water Balance.

<!-- b000700 | references | pages [24] -->
U.S. Geological Survey Scientific Investigations Report 2004-5100, 42 p.

<!-- b000701 | references | pages [24] -->
[5] Lenters, J.D., Anderton, J.B., Blanken, P., Spence, C., & Suyker, A.E. (2013). As-

<!-- b000702 | references | pages [24] -->
sessing the Impacts of Climate Variability and Change on Great Lakes Evapora-

<!-- b000703 | references | pages [24] -->
tion. In D. Brown, D. Bidwell, & L. Briley (Eds.), 2011 Project Reports. Great Lakes

<!-- b000704 | references | pages [24] -->
Integrated Sciences and Assessments (GLISA) Center. Retrieved February 6, 2024,

<!-- b000705 | references | pages [24] -->
微信号：MATHmodels

<!-- b000706 | references | pages [24] -->
from http://glisaclimate.org/media/GLISA_Lake_Evaporation.pdf

<!-- b000707 | references | pages [24] -->
[6] Wikipedia contributors. (2024, February 3). Great Lakes. In *Wikipedia, The Free

<!-- b000708 | references | pages [24] -->
Encyclopedia*. Retrieved 00:55, February 6, 2024, from https://en.wikipe-

<!-- b000709 | references | pages [24] -->
dia.org/w/index.php?title=Great_Lakes&oldid=1202856604

<!-- b000710 | references | pages [24] -->
[7] Lin, D. H. (2018). Saint Lawrence Seaway and its regulations and handbook: Re-

<!-- b000711 | references | pages [24] -->
quirements for maximum vessel dimensions etc. *Journal of Navigation*, 10(5),

<!-- b000712 | references | pages [24] -->
79-88.

<!-- b000713 | references | pages [24] -->
[8] Cuthbert, M. O., Taylor, R. G., Favreau, G., Todd, M. C., Shamsudduha, M., Vill-

<!-- b000714 | references | pages [24] -->
holth, K. G., MacDonald, A. M., Scanlon, B. R., Kotchoni, D. O. V., Vouillamoz, J.-

<!-- b000715 | references | pages [24] -->
M., Lawson, F. M. A., Adjomayi, P. A., Kashaigili, J., Seddon, D., Sorensen, J. P. R.,

<!-- b000716 | references | pages [24] -->
Ebrahim, G. Y., Owor, M., Nyenje, P. M., Nazoumou, Y., ... Kukuric, N. (2019).

<!-- b000717 | references | pages [24] -->
Observed controls on resilience of groundwater to climate variability in sub-Sa-

<!-- b000718 | references | pages [24] -->
haran Africa. *Nature*, 572, 230-234.

<!-- b000719 | references | pages [24] -->
[9] Quinn, F. H. (1979). An Improved Aerodynamic Evaporation Technique for Large

<!-- b000720 | references | pages [24] -->
Lakes With Application to the International Field Year for the Great Lakes. Water

<!-- b000721 | references | pages [24] -->
Resources Research, 15(4), 935-940.

<!-- b000722 | references | pages [24] -->
[10]

<!-- b000723 | references | pages [24] -->
Croley, T. E. II (1989). LUMPED MODELING OF LAURENTIAN GREAT

<!-- b000724 | references | pages [24] -->
LAKES EVAPORATION, HEAT STORAGE, AND ENERGY FLUXES FOR FORE-

<!-- b000725 | references | pages [24] -->
CASTING AND SIMULATION. NOAA Technical Memorandum ERL GLERL-70.

<!-- b000726 | references | pages [24] -->
National Oceanic and Atmospheric Research Administration Laboratories.

<!-- b000727 | references | pages [24] -->
[11]

<!-- b000728 | references | pages [24] -->
International Joint Commission. (2014). Lake Ontario - St. Lawrence River

<!-- b000729 | references | pages [24] -->
Plan 2014.

<!-- b000730 | furniture | pages [24] -->


<!-- b000731 | furniture | pages [24] -->


<!-- b000732 | references | pages [24] -->
关注数学模型

<!-- b000733 | furniture | pages [24] -->
2

<!-- b000734 | furniture | pages [24] -->
MATHmodels

<!-- b000735 | furniture | pages [24] -->
获取更多资讯

<!-- b000736 | references | pages [25] -->
OPTIFLOW :

<!-- b000737 | references | pages [25] -->
Hydrological Network Approach

<!-- b000738 | references | pages [25] -->
微信公众号：数学模型

<!-- b000739 | references | pages [25] -->
S

<!-- b000740 | furniture | pages [25] -->


<!-- b000741 | furniture | pages [25] -->


<!-- b000742 | references | pages [25] -->
﻿

<!-- b000743 | references | pages [25] -->
﻿

<!-- b000744 | references | pages [25] -->
﻿

<!-- b000745 | references | pages [25] -->
微信号：MATHmodels

<!-- b000746 | heading | pages [25] -->
The study introduces a modified dam control algorithm based on Model Pre-

<!-- b000747 | prose | pages [25] -->
presents an Adaptive Hydrological Network Simulation and an Equilibrium Stake-

<!-- b000748 | prose | pages [25] -->
reational users, and hydro

<!-- b000749 | prose | pages [25] -->
dictive Control (MPC), enhancing the responsiveness of water level regulation to

<!-- b000750 | prose | pages [25] -->
holder Satisfaction (E

<!-- b000751 | furniture | pages [25] -->


<!-- b000752 | prose | pages [25] -->
- power generation com-

<!-- b000753 | prose | pages [25] -->
revealing its sensitivi

<!-- b000754 | prose | pages [25] -->
represents the lakes as interconnected nodes and edges, simplifying the system's complexity and facilitating analysis. The ESS Model integrates stakeholder prefer-

<!-- b000755 | furniture | pages [25] -->


<!-- b000756 | prose | pages [25] -->
panies, with weights assigned to balance their influence.

<!-- b000757 | prose | pages [25] -->
to extreme weather events. The ESS Model's stakeholder satisfaction functions are

<!-- b000758 | prose | pages [25] -->
ences, prioritizing their diverse int

<!-- b000759 | prose | pages [25] -->
cial, and economic factors. However, there are limitations, such as the model's sim-

<!-- b000760 | prose | pages [25] -->
plification of n ffin

<!-- b000761 | prose | pages [25] -->
The research concludes that the proposed models and algorithms show prom-

<!-- b000762 | prose | pages [25] -->
atural factors and the need for empirical validation of stakeholder satisfaction functions. Future work should focus on refining the model to better cap-

<!-- b000763 | prose | pages [25] -->
ture the system's complexity and improve predictive accuracy

<!-- b000764 | furniture | pages [25] -->


<!-- b000765 | prose | pages [25] -->
.

<!-- b000766 | furniture | pages [25] -->


<!-- b000767 | prose | pages [25] -->
Adaptive Hydrological Network; Equilibrium Stakeholder Satisfaction;

<!-- b000768 | heading | pages [25] -->
Model Predictive Control; Great Lakes Water Management; Environmental Sensitiv-ity Analysis

<!-- b000769 | furniture | pages [25] -->


<!-- b000770 | furniture | pages [25] -->


<!-- b000771 | furniture | pages [25] -->


<!-- b000772 | furniture | pages [25] -->


<!-- b000773 | prose | pages [25] -->
C

<!-- b000774 | furniture | pages [25] -->


<!-- b000775 | furniture | pages [25] -->


<!-- b000776 | prose | pages [25] -->
关注数学模型

<!-- b000777 | furniture | pages [25] -->
2

<!-- b000778 | furniture | pages [25] -->
MATHmodels

<!-- b000779 | furniture | pages [25] -->
获取更多资讯

<!-- b000780 | heading | pages [26] -->
AI Usage Instructions

<!-- b000781 | ai_disclosure | pages [26] -->
Hydrological Network Approach

<!-- b000782 | furniture | pages [26] -->


<!-- b000783 | ai_disclosure | pages [26] -->
S

<!-- b000784 | ai_disclosure | pages [26] -->
微信公众号：数学模型

<!-- b000785 | ai_disclosure | pages [26] -->
ummary

<!-- b000786 | ai_disclosure | pages [26] -->
The Great Lakes, holding 21% of the world's fresh surface water, face complex water level management challenges due to natural and human factors. This study

<!-- b000787 | furniture | pages [26] -->


<!-- b000788 | ai_disclosure | pages [26] -->
presents an Adaptive Hydrological Network Simulation and an Equilibrium Stake-holder Satisfaction (E

<!-- b000789 | ai_disclosure | pages [26] -->
SS) Model to address these challenges. The network model

<!-- b000790 | furniture | pages [26] -->


<!-- b000791 | ai_disclosure | pages [26] -->
represents the lakes as interconnected nodes and edges, simplifying the system's

<!-- b000792 | ai_disclosure | pages [26] -->
complexity and facilitating analysis. The ESS Model integrates stakeholder prefer-ences, prioritizing their diverse int

<!-- b000793 | ai_disclosure | pages [26] -->
erests in water level management.

<!-- b000794 | furniture | pages [26] -->


<!-- b000795 | ai_disclosure | pages [26] -->
The study introduces a modified dam control algorithm based on Model Pre-

<!-- b000796 | ai_disclosure | pages [26] -->
dictive Control (MPC), enhancing the responsiveness of water level regulation to

<!-- b000797 | ai_disclosure | pages [26] -->
environmental changes. The algorithm's performance is assessed using 2017 data,

<!-- b000798 | ai_disclosure | pages [26] -->
revealing its sensitivi

<!-- b000799 | ai_disclosure | pages [26] -->
ty to high water levels and the need for improved adaptation to extreme weather events. The ESS Model's stakeholder satisfaction functions are

<!-- b000800 | ai_disclosure | pages [26] -->
微信号：MATHmodels

<!-- b000801 | ai_disclosure | pages [26] -->
tailored to reflect the preferences of shipping companies, dock managers, environ-

<!-- b000802 | ai_disclosure | pages [26] -->
mentalists, property owners, rec

<!-- b000803 | ai_disclosure | pages [26] -->
reational users, and hydro

<!-- b000804 | ai_disclosure | pages [26] -->
power generation com-panies, with weights assigned to balance their influence.

<!-- b000805 | furniture | pages [26] -->


<!-- b000806 | ai_disclosure | pages [26] -->
The research concludes that the proposed models and algorithms show prom-ise in managing the Great Lakes' water levels effectively, considering ecological, so-

<!-- b000807 | ai_disclosure | pages [26] -->
-

<!-- b000808 | ai_disclosure | pages [26] -->
cial, and economic factors. However, there are limitations, such as the model's sim-

<!-- b000809 | ai_disclosure | pages [26] -->
plification of n

<!-- b000810 | ai_disclosure | pages [26] -->
atural factors and the need for empirical validation of stakeholder

<!-- b000811 | furniture | pages [26] -->


<!-- b000812 | ai_disclosure | pages [26] -->
satisfaction functions. Future work should focus on refining the model to better cap-ture the system's complexity and improve predictive accuracy.

<!-- b000813 | ai_disclosure | pages [26] -->
Keywo rds :

<!-- b000814 | ai_disclosure | pages [26] -->
Model Predictive Control; Great Lakes Water Management; Environmental Sensitiv-ity Analysis

<!-- b000815 | furniture | pages [26] -->


<!-- b000816 | furniture | pages [26] -->


<!-- b000817 | furniture | pages [26] -->


<!-- b000818 | furniture | pages [26] -->


<!-- b000819 | ai_disclosure | pages [26] -->
Problem Ch osen

<!-- b000820 | ai_disclosure | pages [26] -->
202

<!-- b000821 | ai_disclosure | pages [26] -->
4

<!-- b000822 | ai_disclosure | pages [26] -->
MCM/ICM

<!-- b000823 | furniture | pages [26] -->


<!-- b000824 | heading | pages [26] -->
Summary Sheet

<!-- b000825 | prose | pages [26] -->
Team Contro l Number

<!-- b000826 | furniture | pages [26] -->


<!-- b000827 | furniture | pages [26] -->


<!-- b000828 | prose | pages [26] -->
Adap tive Hydrological Network; Equilibrium Stakeholder Satisfaction;

<!-- b000829 | furniture | pages [26] -->


<!-- b000830 | furniture | pages [26] -->


<!-- b000831 | prose | pages [26] -->
C

<!-- b000832 | furniture | pages [26] -->


<!-- b000833 | furniture | pages [26] -->


<!-- b000834 | furniture | pages [26] -->


<!-- b000835 | furniture | pages [26] -->


<!-- b000836 | prose | pages [26] -->
关注数学模型

<!-- b000837 | furniture | pages [26] -->
2

<!-- b000838 | furniture | pages [26] -->
MATHmodels

<!-- b000839 | furniture | pages [26] -->
获取更多资讯

<!-- b000840 | prose | pages [27] -->
C o n t

<!-- b000841 | prose | pages [27] -->
微信公众号：数学模型

<!-- b000842 | prose | pages [27] -->
微信号：MATHmodels

<!-- b000843 | prose | pages [27] -->
关注数学模型

<!-- b000844 | furniture | pages [27] -->
2

<!-- b000845 | furniture | pages [27] -->
MATHmodels

<!-- b000846 | furniture | pages [27] -->
获取更多资讯
