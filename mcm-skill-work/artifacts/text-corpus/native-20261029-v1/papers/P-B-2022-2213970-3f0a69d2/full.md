# P-B-2022-2213970-3f0a69d2

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2022

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | title | pages [1] -->
2213970

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Decision System for Optimizing Water Allocation

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Construction of dams in the Colorado Basin provides people with abundant water re- sources. However, with the change of climate and people’s over-exploitation of water resources, the water levels of dams continue to decrease, threatening economic develop- ment and ecological environment in the surrounding areas.

<!-- b000011 | prose | pages [1] -->
For Question 1, firstly, we analyze the principle of hydropower conversion , the cou- pling characteristics of cascade hydropower stations and the line loss of electricity trans- mission. As for Question 1(a): We first get the data of electricity demand in each state, and then calculate line loss. Next, we calculate the amount of water used for power genera- tion. By adding water used for power generation and general water usage, we get the total water consumption. Then, we construct a nonlinear programming model with the minimum total water consumption as the goal, and use simulated annealing algorithm to solve it. As for Question 1(b): Respecting the relationship between and lake water level and total water consumption, we calculate the expression of lake water level with time. Our model predicts that, after 91 days , Lake Powell reaches its dead water level, and the system can no longer operate. As for Question 1 (c): We decide to add water periodically and compare the water consumption under different water addition cycles. The optimal water addition time interval is 2 days and additional water volume is 5.22 × 108m3/day .

<!-- b000012 | prose | pages [1] -->
For Question 2, we construct a competitive game model of water resource allocation according to competing interest between general usage and electricity production, as well as between five states. Firstly, we construct profits function of each state based on the principle of economics and the rights of Mexico. Then, according to the game theory, the differential equations of the net profits of each state are obtained, and the Newton iteration method is used to solve the Nash equilibrium point of the game, so as to obtain the water supply and power supply strategy that maximizes the interests of each state.

<!-- b000013 | prose | pages [1] -->
For Question 3, we first introduce water-shortage index SI to characterize degree of the negative impact of water shortage in each states. Next, we divide water resources into several parts. Then according to the idea of dynamic programming, we select the state with the largest water-shortage index to allocate water resources, and iterate the optimal allocation strategy under water shortage conditions. The results of the model show that when there is a serious shortage of water resources, people tend to use limited water resources to meet the demands of general usage.

<!-- b000014 | prose | pages [1] -->
For Question 4, firstly, the water allocation strategy is analyzed when the demands of each state fluctuate over time. It is found that the sensitivity of electricity production to water shortage rate is higher than that of general water usage. Then, we consider the development of renewable energy technologies. It is found that people’s demand for hydroelectricity becomes lower, making the supply of general water greater during the water shortage period. Finally, the water supply strategy under the condition of water- saving and power-saving measures is analyzed. It is found that the hydropower allocated to each state is significantly decreased, and there is a significant low water supply in dry season.

<!-- b000015 | keywords | pages [1] -->
Keywords: Simulated Annealing, Game Theory,Newton Iteration, Water-Shortage Index

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1

<!-- b000018 | heading | pages [2] -->
Introduction

<!-- b000019 | prose | pages [2] -->
4 Problem background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 4 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 4

<!-- b000020 | heading | pages [2] -->
General Assumptions and Model Overview

<!-- b000021 | prose | pages [2] -->
2 5 General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 Model Overview

<!-- b000022 | prose | pages [2] -->
3

<!-- b000023 | heading | pages [2] -->
Notation

<!-- b000024 | prose | pages [2] -->
4

<!-- b000025 | heading | pages [2] -->
Data processing

<!-- b000026 | prose | pages [2] -->
5

<!-- b000027 | prose | pages [2] -->
6

<!-- b000028 | prose | pages [2] -->
6

<!-- b000029 | heading | pages [2] -->
Model 1 : Dam Hydropower Supply Model

<!-- b000030 | prose | pages [2] -->
5 5.1 Preliminary preparation of the model 7 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | prose | pages [2] -->
7 Water resource allocation strategy when lake water level is fixed . . . . . . . 5.2 9 Proposition of water allocation strategy . . . . . . . . . . . . . . . . . 5.2.1 9 The amount of water pumped by each lake . . . . . . . . . . . . . . . 5.2.2 10 The duration of the supply when no water is added . . . . . . . . . . . . . . 5.3 10 Lake water recharge strategies for sustainable supply . . . . . . . . . . . . . 5.4 11

<!-- b000032 | heading | pages [2] -->
Model 2 : Water resource allocation strategy based on game theory

<!-- b000033 | prose | pages [2] -->
6 12 Benefit Calculation for Water Allocation . . . . . . . . . . . . . . . . . . . . . 6.1 12 Function 1 :Profit function . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.1 12 Function 2 : Cost function . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.2 13 Function 3 : Compensation function . . . . . . . . . . . . . . . . . . . 6.1.3 13 Game relationship between general and power water use 6.2 . . . . . . . . . .

<!-- b000034 | prose | pages [2] -->
13 Game relationship between five states and Mexico’s water use . . . . . . . . 6.3 14 Five State Water Allocation Strategies 6.4 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | prose | pages [2] -->
14 Derivation of Nash Equilibrium Points for Allocation Strategy . . . . 6.4.1 14 Newton’s Iterative Method to Solve the Nash Equilibrium . . . . . . 6.4.2

<!-- b000036 | prose | pages [2] -->
7

<!-- b000037 | heading | pages [2] -->
Model 3 :Allocation strategy based on SI

<!-- b000038 | prose | pages [2] -->
15

<!-- b000039 | prose | pages [2] -->
15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 Water shortage index SI 7.2 Water resource allocation strategy 15 . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | prose | pages [2] -->
16

<!-- b000041 | heading | pages [2] -->
The influence of different factors on the model

<!-- b000042 | prose | pages [2] -->
8 17 Changes in water and electricity demand . . . . . . . . . . . . . . . . . . . . 8.1 17 Changes in the development of different sectors . . . . . . . . . . . . 8.1.1 17 Demand fluctuates from month to month . . . . . . . . . . . . . . . . 8.1.2 18 Improvement of renewable energy technology . . . . . . . . . . . . . . . . . 8.2 19 Implementation of water-saving and electricity-saving measures . . . . . . 8.3

<!-- b000043 | prose | pages [2] -->
9

<!-- b000044 | heading | pages [2] -->
Sensitivity analysis of the model

<!-- b000045 | prose | pages [2] -->
19

<!-- b000046 | prose | pages [2] -->
19

<!-- b000047 | prose | pages [2] -->
2 2

<!-- b000048 | furniture | pages [3] -->
Team # 2213970

<!-- b000049 | heading | pages [3] -->
10 Strengths and Weaknesses

<!-- b000050 | furniture | pages [3] -->
Page 3 of 25

<!-- b000051 | prose | pages [3] -->
21 10.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | prose | pages [3] -->
21 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.2 Weaknesses

<!-- b000053 | heading | pages [3] -->
References

<!-- b000054 | references | pages [3] -->
21

<!-- b000055 | references | pages [3] -->
21

<!-- b000056 | references | pages [3] -->
Decision System for Optimizing Water Allocation

<!-- b000057 | heading | pages [3] -->
Appendices

<!-- b000058 | prose | pages [3] -->
22

<!-- b000059 | prose | pages [3] -->
23

<!-- b000060 | furniture | pages [4] -->
Team # 2213970

<!-- b000061 | furniture | pages [4] -->
Page 4 of 25

<!-- b000062 | prose | pages [4] -->
1

<!-- b000063 | heading | pages [4] -->
Introduction

<!-- b000064 | prose | pages [4] -->
1.1 Problem background

<!-- b000065 | prose | pages [4] -->
To make the most of the water in the Colorado River system, people build dams on rivers or lakes. While meeting the demand for water for production and domestic use, dams can also be used for hydropower generation to provide electricity for areas near the basin.

<!-- b000066 | caption | pages [4] -->
Figure 1: Schematic diagram of the Colorado watershed

<!-- b000067 | prose | pages [4] -->
But with climate change and the over-exploitation of river water resources, water re- sources in dams and reservoirs in many areas are declining, resulting in power outages in these areas. Natural resource officials in the U.S. began to develop strategies to keep the system working to meet basic production and domestic water and power generation needs.

<!-- b000068 | prose | pages [4] -->
1.2 Restatement of the Problem

<!-- b000069 | prose | pages [4] -->
Now the state natural resource negotiators are asking your team to develop a reason- able water allocation plan to meet the production and living electricity and water needs of the five states (AZ, CA, WY, NM, and CO) under the condition that Mexico’s rights are guaranteed.

<!-- b000070 | heading | pages [4] -->
1) Task 1 Construct a mathematical model to help officials develop a strategy for the dis-

<!-- b000071 | prose | pages [4] -->
patch and allocation of water resources for two dams. When the demands for hy- dropower and the water resources of the dam are fixed, calculate how long the supply can last and how much additional water resources need to be added to meet the fixed water and electricity demand.

<!-- b000072 | heading | pages [4] -->
2) Task 2 Combine the models you’ve built to develop an optimal solution to the compet-

<!-- b000073 | prose | pages [4] -->
ing interests of water for production and domestic use and water for power generation.

<!-- b000074 | heading | pages [4] -->
3) Task 3 Use your model to figure out what to do when there is not enough water to

<!-- b000075 | prose | pages [4] -->
meet water and power generation needs.

<!-- b000076 | furniture | pages [5] -->
Team # 2213970

<!-- b000077 | furniture | pages [5] -->
Page 5 of 25

<!-- b000078 | heading | pages [5] -->
4) Task 4 Analyze the impact of these variables on your model as people’s water and elec-

<!-- b000079 | prose | pages [5] -->
tricity needs change, river water resources change, and effective energy conservation strategies are adopted.

<!-- b000080 | prose | pages [5] -->
2

<!-- b000081 | heading | pages [5] -->
General Assumptions and Model Overview

<!-- b000082 | prose | pages [5] -->
2.1

<!-- b000083 | heading | pages [5] -->
General Assumptions

<!-- b000084 | prose | pages [5] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified.

<!-- b000085 | prose | pages [5] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified.

<!-- b000086 | heading | pages [5] -->
Assumptions 1:In general, the demand for general water and electricity for each

<!-- b000087 | prose | pages [5] -->
• state is constant

<!-- b000088 | prose | pages [5] -->
,→Justification:Because even if the users’ demand for electricity changes within a day, these changes in demand will be allocated to other power generation methods, such as thermal power generation.

<!-- b000089 | prose | pages [5] -->
Assumptions 2:The dam does not consider the loss when supplying water to the • surrounding area, but there is line loss when transmitting hydropower.

<!-- b000090 | prose | pages [5] -->
,→Justification:Due to the long distance of hydropower transmission, the loss of power transmission cannot be ignored, while the loss of water transmission is small.

<!-- b000091 | prose | pages [5] -->
• Assumptions 3:The decisions taken by the officials involved in the negotiations of each state are rational, they will not adopt other strategies that deviate from the Nash equilibrium.

<!-- b000092 | heading | pages [5] -->
Assumptions 4:The evaporation of water resources in the lake is not considered,

<!-- b000093 | prose | pages [5] -->
• and all the water flowing out of the dam is considered to be used to generate elec- tricity.

<!-- b000094 | prose | pages [5] -->
,→Justification:Compared with general water and electricity water, the proportion of water evaporation in natural conditions is very small.

<!-- b000095 | prose | pages [5] -->
2.2

<!-- b000096 | heading | pages [5] -->
Model Overview

<!-- b000097 | prose | pages [5] -->
This paper proposes the decision system for optimizing water allocation, which can be divided into three parts. It analyzes the allocation of water resources when the demand is just met, the game situation of each state when the water resources are sufficient, and the objective and fair scheduling scheme when the water resources are insufficient.

<!-- b000098 | prose | pages [5] -->
Also, we consider various situations such as changes in water consumption and re- newable energy technologies development, and give the solution of the model under the corresponding situation. This model has reference significance to the mega-drought that actually occurrs in the western United States.

<!-- b000099 | furniture | pages [6] -->
Team # 2213970

<!-- b000100 | furniture | pages [6] -->
Page 6 of 25

<!-- b000101 | caption | pages [6] -->
Figure 2: Model Framework

<!-- b000102 | prose | pages [6] -->
3

<!-- b000103 | heading | pages [6] -->
Notation

<!-- b000104 | prose | pages [6] -->
The primary notations used in this paper are listed in Table 1. There can be some other notations to be described in other parts of the paper.

<!-- b000105 | caption | pages [6] -->
Table 1: Notations

<!-- b000106 | prose | pages [6] -->
Definition Symbol

<!-- b000107 | prose | pages [6] -->
Q

<!-- b000108 | prose | pages [6] -->
Unit

<!-- b000109 | prose | pages [6] -->
m3/s water discharge H m water level V m3 lake volume

<!-- b000110 | prose | pages [6] -->
P MW power needed S m3 water demands unsatisfied

<!-- b000111 | prose | pages [6] -->
D m3 total water demands

<!-- b000112 | prose | pages [6] -->
4

<!-- b000113 | heading | pages [6] -->
Data processing

<!-- b000114 | prose | pages [6] -->
Step 1 : Data Acquisition We mainly use the following data: water and electricity consumption by sector in five states (AZ, CA, WY, NM and CO), the water height and the volume of water in those five reservoirs for Hoover Dam and Glen Canyon Dam . These data sources are summarized in Table 2.

<!-- b000115 | heading | pages [6] -->
Step 2 : Dam data analysis

<!-- b000116 | furniture | pages [7] -->
Team # 2213970

<!-- b000117 | furniture | pages [7] -->
Page 7 of 25

<!-- b000118 | caption | pages [7] -->
Table 2: Data source collation

<!-- b000119 | prose | pages [7] -->
Database Websites Database Names Data Type

<!-- b000120 | prose | pages [7] -->
https://www.usbr.gov/ USAGov Renewable Energy https://www.eia.gov/ EIA Electricity https://www.statista.com/ Statista Geography http://www.water-data.com/ USGS Reservior https://scholar.google.com/ Google Scholar Academic paper

<!-- b000121 | prose | pages [7] -->
In the follow-up, it is necessary to analyze the sustainability of hydropower supply by combining the data of the reservoir water level and the water volume of the lake, but it is difficult to calculate the water volume of the lake directly .

<!-- b000122 | prose | pages [7] -->
According to the data of water level and water volume of Lake Mead and Lake Powell in the past ten years at the USAGov website, it is found that the data satisfy the cubic function polynomial relationship, and the functional expressions of water volume VM , VP and water level height H of the two lakes are obtained. They are: VM = 3.78 × 103H3 + 1.2 × 106H2 −5.9 × 107H, VP = 9.9 × 103H3 + 7.9 × 106H2 −1.6 × 107H. The fitting vari- ances of the two sets of data are both 0.99, indicating that the fitted function expression is reasonable to a certain extent.

<!-- b000123 | prose | pages [7] -->
(a) Lake Mead condition (b) Lake Powell situation

<!-- b000124 | caption | pages [7] -->
Figure 3: The relationship between lake water volume V and lake water level H

<!-- b000125 | heading | pages [7] -->
Model 1 : Dam Hydropower Supply Model

<!-- b000126 | prose | pages [7] -->
5

<!-- b000127 | heading | pages [7] -->
Preliminary preparation of the model

<!-- b000128 | prose | pages [7] -->
5.1

<!-- b000129 | prose | pages [7] -->
Theory 1 : Hydropower conversion analysis of hydropower station [1] According to the Bernoulli energy conservation equation of the fluid, the energy change of the water micelles in the hydropower station flowing from upper pool to lower pool is mainly divided into three parts: kinetic energy ∆EE = 500(ρ1v2

<!-- b000130 | prose | pages [7] -->
1 −ρ2v2 2)∆V , gravita- tional potential ∆EG = 9810H∆Vt, pressure potential energy ∆EE = 9810(p1 −p2)∆V/γ . Therefore, the reduction of the mechanical energy of water during the power generation process, that is, the energy used for power generation, is obtained as Equation (1).

<!-- b000131 | furniture | pages [8] -->
Team # 2213970

<!-- b000132 | furniture | pages [8] -->
Page 8 of 25

<!-- b000133 | prose | pages [8] -->
1 −ρ2v2

<!-- b000134 | prose | pages [8] -->
γ + ρ1v2

<!-- b000135 | prose | pages [8] -->
Ewater = 9810(H + ∆p

<!-- b000136 | prose | pages [8] -->
2 )ηQ∆t (1) 2g

<!-- b000137 | prose | pages [8] -->
Among them: H is the hydraulic height, ∆p is the pressure difference between the water of upper pool and lower pool, γ is the water specific gravity; v1, v2 section water flow velocity, Q water flow used for power generation.

<!-- b000138 | prose | pages [8] -->
Actually, in power generation process, the difference between the pressure difference ∆p and the cross-sectional flow velocity |v1 −v2| is very small, can be ignored. According to the information, the conversion efficiency of hydropower is about η = 27%, and so we can obtain the actual power generation of hydropower station: Eelet = 2648.7HQ∆t.

<!-- b000139 | prose | pages [8] -->
(a) Hydroelectric power station (b) Cascade hydropower station system

<!-- b000140 | caption | pages [8] -->
Figure 4: Schematic diagram of the principle of the hydroelectric power station system

<!-- b000141 | prose | pages [8] -->
Theory 2 : Coupling Characteristics of Cascade Hydropower Stations According to the geographical relationship, Glen Canyon Dam and Hoover Dam to- gether constitute a cascade hydropower system. For a cascade hydropower station sys- tem, the reservoir water volume Vi(t) is mainly determined by water inflows Vin

<!-- b000142 | prose | pages [8] -->
i (t) , the initial water volume Vi(t0), outflows used for water supply Vout

<!-- b000143 | prose | pages [8] -->
flow Velet , and power generation i

<!-- b000144 | prose | pages [8] -->
.We can iterate the time series of the water flows of the two dams to obtain the i water storage conditions of Lake Powell VP and Lake Mead VM in different periods , as shown in Equation (2).

<!-- b000145 | prose | pages [8] -->
t

<!-- b000146 | prose | pages [8] -->


<!-- b000147 | prose | pages [8] -->
h

<!-- b000148 | prose | pages [8] -->
i

<!-- b000149 | prose | pages [8] -->
P (τ) −Vout

<!-- b000150 | prose | pages [8] -->
Vin

<!-- b000151 | prose | pages [8] -->
∑

<!-- b000152 | prose | pages [8] -->
VP(t) = VP(t0) +

<!-- b000153 | prose | pages [8] -->
   

<!-- b000154 | prose | pages [8] -->
τ=t0

<!-- b000155 | prose | pages [8] -->


<!-- b000156 | prose | pages [8] -->
t

<!-- b000157 | prose | pages [8] -->
h

<!-- b000158 | prose | pages [8] -->


<!-- b000159 | prose | pages [8] -->
P (τ) −Velet

<!-- b000160 | prose | pages [8] -->
(τ) P

<!-- b000161 | prose | pages [8] -->
(2) i

<!-- b000162 | prose | pages [8] -->
(τ) + Vin

<!-- b000163 | prose | pages [8] -->
Velet

<!-- b000164 | prose | pages [8] -->
∑

<!-- b000165 | prose | pages [8] -->
VM(t) = VM(t0) +

<!-- b000166 | prose | pages [8] -->
 

<!-- b000167 | prose | pages [8] -->
P

<!-- b000168 | prose | pages [8] -->
 

<!-- b000169 | prose | pages [8] -->
τ=t0

<!-- b000170 | prose | pages [8] -->
M(τ) −Vout

<!-- b000171 | prose | pages [8] -->
M (τ) −Velet

<!-- b000172 | prose | pages [8] -->
M (τ)

<!-- b000173 | prose | pages [8] -->
Theory 3 : Calculation of Line Loss for Hydropower Transmission By consulting the data, the annual hydropower demands in five states can be obtained. However, due to long-distance power transmission, there is a certain line loss ∆P when the hydropower station transmits power to the users in each state, so the original power generation of the power station is equal to the users’ demands plus line losses during transmission. Assume that the transmission distance between the state i and the dam j be Li→j, the line resistance per unit length be γ, and the transmission power and voltage are P, U , then the line power loss during transmission is ∆P = P2γLi→j/U2 , so the calculation formula of the total electricity that the hydropower station needs to transmit is as shown in Equation (3).

<!-- b000174 | furniture | pages [9] -->
Team # 2213970

<!-- b000175 | furniture | pages [9] -->
Page 9 of 25

<!-- b000176 | prose | pages [9] -->
2

<!-- b000177 | prose | pages [9] -->
i→j = Pi→j + (Pi→j

<!-- b000178 | prose | pages [9] -->
Ptotal

<!-- b000179 | prose | pages [9] -->
U )

<!-- b000180 | prose | pages [9] -->
γLi→j (3)

<!-- b000181 | prose | pages [9] -->
Thus, the size of the hydropower required to provide 1MW of electricity from the Glen Canyon Dam and the Hoover Dam to users in five states is obtained. Table 3 lists the line losses ∆P of the two dams delivering unit electricity to each state .

<!-- b000182 | caption | pages [9] -->
Table 3: The ratio of line loss to total power transmission

<!-- b000183 | prose | pages [9] -->
∆PP→AZ Line loss of Glen Canyon . ∆PP→CA .

<!-- b000184 | prose | pages [9] -->
14.46% Numerical value ∆PP→NM ∆PP→CO ∆PP→WY 2.56% 0.25% 1.43% 1.21% ∆PM→AZ . ∆PM→CA Line loss of Hoover Numerical value .

<!-- b000185 | prose | pages [9] -->
13.61% ∆PM→NM ∆PM→CO ∆PM→WY 1.96% 0.00% 0.83% 0.69%

<!-- b000186 | prose | pages [9] -->
Water resource allocation strategy when lake water level is fixed 5.2

<!-- b000187 | prose | pages [9] -->
Proposition of water allocation strategy 5.2.1

<!-- b000188 | prose | pages [9] -->
On the basis of meeting people’s basic demands for water and electricity production, we hope to develop strategies that can minimize the total water consumption of the lake and achieve the sustainable development of the Colorado River Basin. Since the water level H of the two lakes is constant, combined with Equation (1), it can be obtained that the power generation flow per unit of hydropower generated by the dam is a fixed value,its calculation expression is:

<!-- b000189 | prose | pages [9] -->
Q = 1.36 × 10−4/(H∆t ) (4)

<!-- b000190 | prose | pages [9] -->
Assuming that the electricity that California needs to buy from the Hoover Dam is PM→CA = λCAPCA , then the electricity that the Glen Canyon Dam needs to provide to California is PP→CA = (1 −λ)PCA . Combined with Equation (3), the amount of electricity required by the Hoover Dam and Glen Canyon Dam to meet the electricity needs of the five states is:

<!-- b000191 | prose | pages [9] -->


<!-- b000192 | prose | pages [9] -->
5

<!-- b000193 | prose | pages [9] -->
5

<!-- b000194 | prose | pages [9] -->
2

<!-- b000195 | prose | pages [9] -->
(λiPi

<!-- b000196 | prose | pages [9] -->
Ptotal

<!-- b000197 | prose | pages [9] -->
∑

<!-- b000198 | prose | pages [9] -->
∑

<!-- b000199 | prose | pages [9] -->
λiPi +

<!-- b000200 | prose | pages [9] -->
=

<!-- b000201 | prose | pages [9] -->
 

<!-- b000202 | prose | pages [9] -->
P

<!-- b000203 | prose | pages [9] -->
  

<!-- b000204 | prose | pages [9] -->
i=1

<!-- b000205 | prose | pages [9] -->
i=1

<!-- b000206 | prose | pages [9] -->
5

<!-- b000207 | prose | pages [9] -->


<!-- b000208 | prose | pages [9] -->
Ptotal

<!-- b000209 | prose | pages [9] -->
∑

<!-- b000210 | prose | pages [9] -->
(1 −λi)Pi +

<!-- b000211 | prose | pages [9] -->
=

<!-- b000212 | prose | pages [9] -->
 

<!-- b000213 | prose | pages [9] -->
M

<!-- b000214 | prose | pages [9] -->
 

<!-- b000215 | prose | pages [9] -->
i=1

<!-- b000216 | prose | pages [9] -->
U )

<!-- b000217 | prose | pages [9] -->
γLP→i

<!-- b000218 | prose | pages [9] -->
(5)

<!-- b000219 | prose | pages [9] -->
2

<!-- b000220 | prose | pages [9] -->
5

<!-- b000221 | prose | pages [9] -->
(1 −λi)Pi

<!-- b000222 | prose | pages [9] -->
∑

<!-- b000223 | prose | pages [9] -->
γLM→i

<!-- b000224 | prose | pages [9] -->
U

<!-- b000225 | prose | pages [9] -->
i=1

<!-- b000226 | prose | pages [9] -->
According to the data, the hydraulic height of Hoover Dam is 172m and the hydraulic height of Glen Canyon Dam is 174m, so we can obtain the hydroelectric power generation formula of the two dams respectively QP = 1.36 × 10−4Ptotal

<!-- b000227 | prose | pages [9] -->
/P , QM = 1.36 × 10−4Ptotal

<!-- b000228 | prose | pages [9] -->
/M

<!-- b000229 | prose | pages [9] -->
P

<!-- b000230 | prose | pages [9] -->
M . Assume that the amount of water provided by the Hoover Dam to California is VM→CA = αCAVCA , then combined with the previous reservoir Equation (2) for the change in water storage yields the final volume of water to be pumped from the two lakes:

<!-- b000231 | furniture | pages [10] -->
Team # 2213970

<!-- b000232 | prose | pages [10] -->


<!-- b000233 | prose | pages [10] -->
5

<!-- b000234 | prose | pages [10] -->
Vtotal

<!-- b000235 | prose | pages [10] -->
∑

<!-- b000236 | furniture | pages [10] -->
Page 10 of 25

<!-- b000237 | prose | pages [10] -->
Z

<!-- b000238 | prose | pages [10] -->
αiVi +

<!-- b000239 | prose | pages [10] -->
=

<!-- b000240 | prose | pages [10] -->
 

<!-- b000241 | prose | pages [10] -->
P

<!-- b000242 | prose | pages [10] -->
  

<!-- b000243 | prose | pages [10] -->
i=1

<!-- b000244 | prose | pages [10] -->
5

<!-- b000245 | prose | pages [10] -->


<!-- b000246 | prose | pages [10] -->
Vtotal

<!-- b000247 | prose | pages [10] -->
∑

<!-- b000248 | prose | pages [10] -->
QPdt

<!-- b000249 | prose | pages [10] -->
(6)

<!-- b000250 | prose | pages [10] -->
Z

<!-- b000251 | prose | pages [10] -->
(1 −αi)Vi +

<!-- b000252 | prose | pages [10] -->
=

<!-- b000253 | prose | pages [10] -->
 

<!-- b000254 | prose | pages [10] -->
M

<!-- b000255 | prose | pages [10] -->
 

<!-- b000256 | prose | pages [10] -->
i=1

<!-- b000257 | prose | pages [10] -->
QMdt

<!-- b000258 | prose | pages [10] -->
Therefore, the optimization goal of the optimal water resource allocation strategy is to minimize the total water consumption of the two lakes while meeting the demand for both water and electricity. The objective function is as follows.

<!-- b000259 | prose | pages [10] -->
min Vtotal

<!-- b000260 | prose | pages [10] -->
P + Vtotal

<!-- b000261 | prose | pages [10] -->
(7) M

<!-- b000262 | prose | pages [10] -->
The amount of water pumped by each lake 5.2.2

<!-- b000263 | prose | pages [10] -->
The feasible solution space of the optimization problem is very large, so this optimiza- tion problem is suitable to be solved by heuristic algorithm.In this case, we use the simu- lated annealing algorithm, then the optimal water resource allocation strategy is obtained. The total electricity delivered by the two dams to the five states and the water consump- tion of the lake are shown in Table 4.

<!-- b000264 | caption | pages [10] -->
Table 4: Electricity generation and water consumption of two lakes

<!-- b000265 | prose | pages [10] -->
Electricity demands / MW

<!-- b000266 | prose | pages [10] -->
Ptotal

<!-- b000267 | prose | pages [10] -->
Ptotal Electricity of Powell

<!-- b000268 | prose | pages [10] -->
P→CA

<!-- b000269 | prose | pages [10] -->
Ptotal

<!-- b000270 | prose | pages [10] -->
Ptotal

<!-- b000271 | prose | pages [10] -->
Ptotal

<!-- b000272 | prose | pages [10] -->
P→NM

<!-- b000273 | prose | pages [10] -->
P→AZ

<!-- b000274 | prose | pages [10] -->
P→CO

<!-- b000275 | prose | pages [10] -->
P→WY 269.49 Numerical value 1569.07 0 48.02 33.66

<!-- b000276 | prose | pages [10] -->
Ptotal

<!-- b000277 | prose | pages [10] -->
Ptotal Electricity of Mead

<!-- b000278 | prose | pages [10] -->
M→CA

<!-- b000279 | prose | pages [10] -->
Ptotal

<!-- b000280 | prose | pages [10] -->
Ptotal

<!-- b000281 | prose | pages [10] -->
Ptotal

<!-- b000282 | prose | pages [10] -->
M→NM

<!-- b000283 | prose | pages [10] -->
M→AZ

<!-- b000284 | prose | pages [10] -->
M→CO

<!-- b000285 | prose | pages [10] -->
M→WY 424.01 Numerical value 1098.57 21.51 130.59 82.85 Water Consumption / (m3/s) Lake Powell 3796.79405 Lake Mead 4196.529726

<!-- b000286 | prose | pages [10] -->
The duration of the supply when no water is added 5.3

<!-- b000287 | prose | pages [10] -->
When there is no additional water supplied, Vin

<!-- b000288 | prose | pages [10] -->
P , Vin

<!-- b000289 | prose | pages [10] -->
M are both 0, and the cascade re- lationship between the two dams needs to be considered. Apart from that, as the dams continue to provide water and electricity to five states, the water level of the lake will gradually drop.According to Equation (4),the decrease of water level will increase water flows needed to produce the same amount of electricity. At this time, it is necessary to consider the relationship between the water volume and the water level of the two lakes obtained above V = f (H) , and substitute it into the expression of power generation to obtain the situation at different water levels. The time coupling relationship between water flow Qi and water volume Vi when electricity Ei is generated:

<!-- b000290 | furniture | pages [11] -->
Team # 2213970

<!-- b000291 | furniture | pages [11] -->
Page 11 of 25

<!-- b000292 | prose | pages [11] -->
Qi(t) = 1.36 × 10−4Ei/ f −1(Vi(t))∆t

<!-- b000293 | prose | pages [11] -->
   

<!-- b000294 | prose | pages [11] -->
t

<!-- b000295 | prose | pages [11] -->


<!-- b000296 | prose | pages [11] -->


<!-- b000297 | prose | pages [11] -->


<!-- b000298 | prose | pages [11] -->
Vout

<!-- b000299 | prose | pages [11] -->


<!-- b000300 | prose | pages [11] -->
∑

<!-- b000301 | prose | pages [11] -->
VP(t) = VP(t0) −

<!-- b000302 | prose | pages [11] -->


<!-- b000303 | prose | pages [11] -->
Z

<!-- b000304 | prose | pages [11] -->
P (τ) +

<!-- b000305 | prose | pages [11] -->
 

<!-- b000306 | prose | pages [11] -->
τ=t0

<!-- b000307 | prose | pages [11] -->


<!-- b000308 | prose | pages [11] -->
t

<!-- b000309 | prose | pages [11] -->


<!-- b000310 | prose | pages [11] -->
Z

<!-- b000311 | prose | pages [11] -->


<!-- b000312 | prose | pages [11] -->
QP(τ)

<!-- b000313 | prose | pages [11] -->
(8)

<!-- b000314 | prose | pages [11] -->


<!-- b000315 | prose | pages [11] -->
Z

<!-- b000316 | prose | pages [11] -->
QP(τ)dt −Vout

<!-- b000317 | prose | pages [11] -->
∑

<!-- b000318 | prose | pages [11] -->


<!-- b000319 | prose | pages [11] -->
VM(t) = VM(t0) +

<!-- b000320 | prose | pages [11] -->
   

<!-- b000321 | prose | pages [11] -->
τ=t0

<!-- b000322 | prose | pages [11] -->
M (τ)dt −

<!-- b000323 | prose | pages [11] -->
QM(τ)dt

<!-- b000324 | prose | pages [11] -->
Since the general water usage in each state is fixed, Vout

<!-- b000325 | prose | pages [11] -->
P (t), Vout

<!-- b000326 | prose | pages [11] -->
M (t) is constant. Com- bined with the previous analysis, calculation results and the hydropower and water con- sumption data of each state, we can iterate water level and water flow of two dams in the above difference equation system.

<!-- b000327 | prose | pages [11] -->
According to the official website information, the lowest water level of Glen Canyon Dam and Hoover Dam to generate electricity is 69 meters and 71 meters respectively.

<!-- b000328 | prose | pages [11] -->
According to the curve of the water level height change over time obtained by iteration, it can be clearly seen that in the early stage of water intake, which is about the first two months, the rate of decline of the dam water level is relatively small.

<!-- b000329 | prose | pages [11] -->
However, in the later period, the rate of water level decline continued to increase. On the 91st day, the water level of Lake Pow- ell took the lead to drop to the minimum power generation level of 69 meters, that is to say the entire cascade hydropower station system could not supply hydropower nor- mally.

<!-- b000330 | prose | pages [11] -->
5.4 Lake water recharge strategies for sustainable supply

<!-- b000331 | prose | pages [11] -->
Combining the relationship between wa- ter level and water flows during power gen- eration, it is not difficult to conclude that the higher the frequency of adding water, the less water needed to be added because the hydraulic height of the dam can always be maintained at a high level.

<!-- b000332 | prose | pages [11] -->
However, the higher the frequency of adding water, the

<!-- b000333 | caption | pages [11] -->
Figure 5: Variation trend of water levels in Lake

<!-- b000334 | prose | pages [11] -->
Powell and Lake Mead over time without recharge

<!-- b000335 | prose | pages [11] -->
greater the cost of human resources and material resources. Therefore, it is necessary to analyze the relationship between the amount of additional water supply and the fre- quency of adding water.

<!-- b000336 | prose | pages [11] -->
In a water addition cycle, every change of hydraulic height will affect the formula- tion of the subsequent dam hydropower scheduling strategy. Therefore, the calculation method of the required amount of water in this problem is exactly the same as the previ- ous problem, which uses the simulated annealing algorithm to find the optimal solutions.

<!-- b000337 | prose | pages [11] -->
Next, we will calculate the amount of additional water supply required under differ- ent water addition frequencies as follows. The adding water cycle is ranged from 1 day to 30 days. Since the time interval of each addtion is small, and the corresponding schedul-

<!-- b000338 | furniture | pages [12] -->
Team # 2213970

<!-- b000339 | furniture | pages [12] -->
Page 12 of 25

<!-- b000340 | prose | pages [12] -->
ing strategy is calculated every time the hydraulic height changes, so the time and space complexity in the iterative process is high, but the final result is more reasonable.

<!-- b000341 | caption | pages [12] -->
Figure 6: Variation curve of water consumption with water addition cycle

<!-- b000342 | prose | pages [12] -->
Combined with the obtained water consumption under different water addition cy- cles, it can be clearly seen that the longer the water addition interval, the greater the water consumption under the condition of meeting the same demand, which is completely con- sistent with the actual life, which verifies the rationality of the model; but , the higher the frequency of adding water, the more manpower and material resources are consumed, so considering the two comprehensively, the water addition interval is 2 days, and the water consumption at this time is only A.

<!-- b000343 | heading | pages [12] -->
Model 2 : Water resource allocation strategy based on

<!-- b000344 | prose | pages [12] -->
6 game theory

<!-- b000345 | prose | pages [12] -->
Benefit Calculation for Water Allocation 6.1

<!-- b000346 | prose | pages [12] -->
6.1.1 Function 1 :Profit function

<!-- b000347 | prose | pages [12] -->
According to the principle of economics, as the quantity of a commodity increases, the unit price of the commodity will inevitably decrease. Therefore, when the water supply and power supply of each state increase, although the total revenue will continue to rise, the economic value of unit water will decrease.

<!-- b000348 | prose | pages [12] -->
Assume that the initial unit price of general water use is βw

<!-- b000349 | prose | pages [12] -->
general water use unit price δw i , because the decay rate of

<!-- b000350 | prose | pages [12] -->
i and the benefit difference Earnw

<!-- b000351 | prose | pages [12] -->
i −Earnw

<!-- b000352 | prose | pages [12] -->
i0 is proportional, so when the general water supply increases by dww,i, the water efficiency per unit of water is ∆Earnw

<!-- b000353 | prose | pages [12] -->
βw

<!-- b000354 | prose | pages [12] -->
i −δw

<!-- b000355 | prose | pages [12] -->
i (Earnw

<!-- b000356 | prose | pages [12] -->
i −Earnw

<!-- b000357 | prose | pages [12] -->


<!-- b000358 | prose | pages [12] -->


<!-- b000359 | prose | pages [12] -->
i =

<!-- b000360 | prose | pages [12] -->
i0)

<!-- b000361 | prose | pages [12] -->
∆ww,i , we can convert it into a differential equa- tion and then integrate the differential equation to obtain the benefit function of general water supply:

<!-- b000362 | prose | pages [12] -->
i0 + βw

<!-- b000363 | prose | pages [12] -->
Earnw

<!-- b000364 | prose | pages [12] -->
i = Earnw

<!-- b000365 | prose | pages [12] -->
(1 −eδw

<!-- b000366 | prose | pages [12] -->
i ww,i)

<!-- b000367 | prose | pages [12] -->
i

<!-- b000368 | prose | pages [12] -->
(9)

<!-- b000369 | prose | pages [12] -->
δw

<!-- b000370 | prose | pages [12] -->
i

<!-- b000371 | furniture | pages [13] -->
Team # 2213970

<!-- b000372 | furniture | pages [13] -->
Page 13 of 25

<!-- b000373 | prose | pages [13] -->
Similarly, the benefit function of electricity supply can be obtained:

<!-- b000374 | prose | pages [13] -->
i0 + βe

<!-- b000375 | prose | pages [13] -->
Earne

<!-- b000376 | prose | pages [13] -->
i = Earne

<!-- b000377 | prose | pages [13] -->
6.1.2 Function 2 : Cost function

<!-- b000378 | prose | pages [13] -->
(1 −eδe

<!-- b000379 | prose | pages [13] -->
i we,i)

<!-- b000380 | prose | pages [13] -->
i

<!-- b000381 | prose | pages [13] -->
(10)

<!-- b000382 | prose | pages [13] -->
δe

<!-- b000383 | prose | pages [13] -->
i

<!-- b000384 | prose | pages [13] -->
There is a certain cost problem in extracting water from lakes and transporting it to users at different distances, as well as using water to generate electricity. Assuming that the cost of general water and electricity per production unit does not change with the quantity, so the cost of producing general water supply in each state is Cw

<!-- b000385 | prose | pages [13] -->
cost of generating electricity from water is Ce

<!-- b000386 | prose | pages [13] -->
6.1.3 Function 3 : Compensation function

<!-- b000387 | prose | pages [13] -->
i = kwww,i , the

<!-- b000388 | prose | pages [13] -->
i = kewe,i .

<!-- b000389 | prose | pages [13] -->
With more water for general water supply and electricity production, the total revenue to five states would be greater, but this would also result in less water being allocated to downstream Mexico. In order to address the rights of Mexico, compensation items are formulated to control the supply of water and electricity in each state within a certain limit to achieve sustainable development of the entire region including Mexico.

<!-- b000390 | prose | pages [13] -->
Combined with relevant literature, the compensation function in this paper is:

<!-- b000391 | prose | pages [13] -->
"

<!-- b000392 | prose | pages [13] -->
5 ∑

<!-- b000393 | prose | pages [13] -->
#λ

<!-- b000394 | prose | pages [13] -->
(ww,i + we,i) −wori)ξ

<!-- b000395 | prose | pages [13] -->
Rep = κ

<!-- b000396 | prose | pages [13] -->
(

<!-- b000397 | prose | pages [13] -->
i=1

<!-- b000398 | prose | pages [13] -->
(11)

<!-- b000399 | prose | pages [13] -->
Among them, κ is the compensation coefficient, ξ is the unit price of compensation, and λ is the compensation index. When the water consumption of the five states exceeds the water consumption range stipulated in the agreement, the compensation amount will show a marginal incremental costs with the increase use of excessive water resources.

<!-- b000400 | prose | pages [13] -->
Then the compensation function of state i due to the excessive use of general water consumption and electricity consumption is:

<!-- b000401 | prose | pages [13] -->


<!-- b000402 | prose | pages [13] -->
#

<!-- b000403 | prose | pages [13] -->
"

<!-- b000404 | prose | pages [13] -->
5 ∑

<!-- b000405 | prose | pages [13] -->
Repw,i = (ww,i −ww0,i)Rep/

<!-- b000406 | prose | pages [13] -->
    

<!-- b000407 | prose | pages [13] -->


<!-- b000408 | prose | pages [13] -->
Repe,i = (we,i −we0,i)Rep/

<!-- b000409 | prose | pages [13] -->
   

<!-- b000410 | prose | pages [13] -->
(ww,i + we,i) −wori

<!-- b000411 | prose | pages [13] -->
i=1

<!-- b000412 | prose | pages [13] -->
(12) #

<!-- b000413 | prose | pages [13] -->
"

<!-- b000414 | prose | pages [13] -->
5 ∑

<!-- b000415 | prose | pages [13] -->
(ww,i + we,i) −wori

<!-- b000416 | prose | pages [13] -->
i=1

<!-- b000417 | prose | pages [13] -->
Game relationship between general and power water use 6.2

<!-- b000418 | prose | pages [13] -->
When the total water consumption of a state is given, if the water used for electricity production is more profitable, then more water resources will be allocated to produce elec- tricity.As more water is used for electricity production, the unit value of those water will begin to decline. At the same time, the quantity of water for general use will decrease. The relationship between supply and demand will inevitably lead to the increase of unit price of general water usage. It is not difficult to see that the relationship between water supply for general usage and electricity production is a process of mutual game. Therefore, we

<!-- b000419 | furniture | pages [14] -->
Team # 2213970

<!-- b000420 | furniture | pages [14] -->
Page 14 of 25

<!-- b000421 | prose | pages [14] -->
need to find the Nash equilibrium point that makes the benefits of these two aspect as large as possible at the same time.

<!-- b000422 | prose | pages [14] -->
Game relationship between five states and Mexico’s water use 6.3

<!-- b000423 | prose | pages [14] -->
Each state hopes to maximize its own economic benefits [2], but the water resources in the Colorado River Basin are limited, this will inevitably lead to competition among the interests of the five states. Therefore, this paper introduces the idea of Nash equilibrium to rationally distribute the general water and power water in each state.

<!-- b000424 | prose | pages [14] -->
The participants in the water allocation game are five states, let this game be G, and the water allocation strategy space of each state is A1, A2, A3, A4, A5 , aij ∈Ai represents the jth policy of state i. The state net benefit function is bi . Then this game can be expressed as G = {A1, A2, · · · , A5; b1, b2, · · · , b5} , when the selected strategy A∗

<!-- b000425 | prose | pages [14] -->
i reaches In Nash equi- librium, states cannot pursue greater interests by changing their water allocation strategy

<!-- b000426 | prose | pages [14] -->
Ai, which can be expressed as:

<!-- b000427 | prose | pages [14] -->
5) ≥bi(A∗

<!-- b000428 | prose | pages [14] -->
bi(A∗

<!-- b000429 | prose | pages [14] -->
1, · · · , A∗ i , · · · , A∗

<!-- b000430 | prose | pages [14] -->
1, · · · , Ai, · · · , A∗ 5) (13)

<!-- b000431 | prose | pages [14] -->
This is satisfied for any i, and its core idea is an optimization problem, that is, to maxi- mize the interests of each state.

<!-- b000432 | caption | pages [14] -->
Table 5: The value of each coefficient in the profit function

<!-- b000433 | prose | pages [14] -->
State CA

<!-- b000434 | prose | pages [14] -->
δw Decay rate .

<!-- b000435 | prose | pages [14] -->
1

<!-- b000436 | prose | pages [14] -->
AZ NM CO WY

<!-- b000437 | prose | pages [14] -->
δw

<!-- b000438 | prose | pages [14] -->
δw

<!-- b000439 | prose | pages [14] -->
δw

<!-- b000440 | prose | pages [14] -->
δw

<!-- b000441 | prose | pages [14] -->
2

<!-- b000442 | prose | pages [14] -->
3

<!-- b000443 | prose | pages [14] -->
5

<!-- b000444 | prose | pages [14] -->
4

<!-- b000445 | prose | pages [14] -->
6.21 × 10−4 . 1.65 × 10−4 Numerical value

<!-- b000446 | prose | pages [14] -->
βw Unit price .

<!-- b000447 | prose | pages [14] -->
1

<!-- b000448 | prose | pages [14] -->
Numerical value ×103 .

<!-- b000449 | prose | pages [14] -->
182

<!-- b000450 | prose | pages [14] -->
δe Decay rate .

<!-- b000451 | prose | pages [14] -->
1

<!-- b000452 | prose | pages [14] -->
1.87 × 10−2 2.30 × 10−2 3.32 × 10−3

<!-- b000453 | prose | pages [14] -->
βw

<!-- b000454 | prose | pages [14] -->
βw

<!-- b000455 | prose | pages [14] -->
βw

<!-- b000456 | prose | pages [14] -->
βw

<!-- b000457 | prose | pages [14] -->
2

<!-- b000458 | prose | pages [14] -->
3

<!-- b000459 | prose | pages [14] -->
5

<!-- b000460 | prose | pages [14] -->
4

<!-- b000461 | prose | pages [14] -->
349 421 380 407

<!-- b000462 | prose | pages [14] -->
δe

<!-- b000463 | prose | pages [14] -->
δe

<!-- b000464 | prose | pages [14] -->
δe

<!-- b000465 | prose | pages [14] -->
δe

<!-- b000466 | prose | pages [14] -->
2

<!-- b000467 | prose | pages [14] -->
3

<!-- b000468 | prose | pages [14] -->
5

<!-- b000469 | prose | pages [14] -->
4

<!-- b000470 | prose | pages [14] -->
5.56 × 10−3 . 1.11 × 10−3 Numerical value

<!-- b000471 | prose | pages [14] -->
βe Unit price .

<!-- b000472 | prose | pages [14] -->
1

<!-- b000473 | prose | pages [14] -->
Numerical value ×103 .

<!-- b000474 | prose | pages [14] -->
402

<!-- b000475 | prose | pages [14] -->
1.01 × 10−2 2.51 × 10−3 2.85 × 10−3

<!-- b000476 | prose | pages [14] -->
βe

<!-- b000477 | prose | pages [14] -->
βe

<!-- b000478 | prose | pages [14] -->
βe

<!-- b000479 | prose | pages [14] -->
βe

<!-- b000480 | prose | pages [14] -->
2

<!-- b000481 | prose | pages [14] -->
3

<!-- b000482 | prose | pages [14] -->
5

<!-- b000483 | prose | pages [14] -->
4

<!-- b000484 | prose | pages [14] -->
387 443 405 380

<!-- b000485 | prose | pages [14] -->
Five State Water Allocation Strategies 6.4

<!-- b000486 | prose | pages [14] -->
Derivation of Nash Equilibrium Points for Allocation Strategy 6.4.1

<!-- b000487 | prose | pages [14] -->
According to the profit function, cost function and compensation function deduced above, it can be concluded that the net earnings of state i is:

<!-- b000488 | prose | pages [14] -->
i0 + βe

<!-- b000489 | prose | pages [14] -->


<!-- b000490 | prose | pages [14] -->
Earne

<!-- b000491 | prose | pages [14] -->
i = Earne

<!-- b000492 | prose | pages [14] -->
   

<!-- b000493 | prose | pages [14] -->
Earnw

<!-- b000494 | prose | pages [14] -->
i = Earnw

<!-- b000495 | prose | pages [14] -->
   

<!-- b000496 | prose | pages [14] -->
Net cost is:

<!-- b000497 | prose | pages [14] -->
(1 −eδe

<!-- b000498 | prose | pages [14] -->
i we,i)

<!-- b000499 | prose | pages [14] -->
i δe

<!-- b000500 | prose | pages [14] -->
i

<!-- b000501 | prose | pages [14] -->
(14)

<!-- b000502 | prose | pages [14] -->
i0 + βw

<!-- b000503 | prose | pages [14] -->
(1 −eδw

<!-- b000504 | prose | pages [14] -->
i ww,i)

<!-- b000505 | prose | pages [14] -->
i δw

<!-- b000506 | prose | pages [14] -->
i

<!-- b000507 | furniture | pages [15] -->
Team # 2213970

<!-- b000508 | prose | pages [15] -->
(

<!-- b000509 | prose | pages [15] -->
Coste

<!-- b000510 | furniture | pages [15] -->
Page 15 of 25

<!-- b000511 | prose | pages [15] -->
i = Repe

<!-- b000512 | prose | pages [15] -->
Costw i + kewe,i

<!-- b000513 | prose | pages [15] -->
(15)

<!-- b000514 | prose | pages [15] -->
i = Repw

<!-- b000515 | prose | pages [15] -->
i + kwww,i

<!-- b000516 | prose | pages [15] -->
Therefore, the net profits of state i can be expressed as Je,w

<!-- b000517 | prose | pages [15] -->
ing that Je,w

<!-- b000518 | prose | pages [15] -->
= Earne,w

<!-- b000519 | prose | pages [15] -->
−Coste,w

<!-- b000520 | prose | pages [15] -->
, know-

<!-- b000521 | prose | pages [15] -->
i

<!-- b000522 | prose | pages [15] -->
i

<!-- b000523 | prose | pages [15] -->
i

<!-- b000524 | prose | pages [15] -->
expression contains two variables ww,i, we,i respectively. According to Nash i equilibrium theory, when states’ water allocation strategy reaches Nash equilibrium [2010?], the water allocation strategy satisfies the following differential equations:

<!-- b000525 | prose | pages [15] -->
∂Je

<!-- b000526 | prose | pages [15] -->


<!-- b000527 | prose | pages [15] -->
i

<!-- b000528 | prose | pages [15] -->
= 0, i = 1, · · · , 5

<!-- b000529 | prose | pages [15] -->
  

<!-- b000530 | prose | pages [15] -->
∂we,i

<!-- b000531 | prose | pages [15] -->


<!-- b000532 | prose | pages [15] -->
∂Jw

<!-- b000533 | prose | pages [15] -->
i

<!-- b000534 | prose | pages [15] -->
(16)

<!-- b000535 | prose | pages [15] -->
= 0, i = 1, · · · , 5

<!-- b000536 | prose | pages [15] -->
  

<!-- b000537 | prose | pages [15] -->
∂ww,i

<!-- b000538 | prose | pages [15] -->


<!-- b000539 | prose | pages [15] -->
Newton’s Iterative Method to Solve the Nash Equilibrium 6.4.2

<!-- b000540 | prose | pages [15] -->
The difficulty in finding the Nash equilibrium point is how to solve the roots of the differential Equation (16) in different situations. Therefore, we use the Newton iteration method to quickly find the roots of the above nonlinear equations, so as to obtain the general water consumption and electricity consumption of each state.

<!-- b000541 | prose | pages [15] -->
Comparing the actual demand in each state with the strategy developed by solving the Nash equilibrium, it is clear that In order to maximize their own interests, each state will choose to allow production to exceed the demand for water and electricity, but due to mutual constraints of interests, the supply cannot be too high.

<!-- b000542 | prose | pages [15] -->
(a) General use water consumption (b) Electricity water consumption

<!-- b000543 | caption | pages [15] -->
Figure 7: Availability of general water and electricity water in five States

<!-- b000544 | heading | pages [15] -->
Model 3 :Allocation strategy based on SI

<!-- b000545 | prose | pages [15] -->
7

<!-- b000546 | prose | pages [15] -->
7.1 Water shortage index SI

<!-- b000547 | prose | pages [15] -->
As we know, water shortage will exert negative impact on both electricity production and people’s daily life. In this case, we should minimize the damage caused by water shortage. Therefore, this question introduces the water-shortage index SI to describe the damage degree of water shortage on a specific area [3].

<!-- b000548 | furniture | pages [16] -->
Team # 2213970

<!-- b000549 | furniture | pages [16] -->
Page 16 of 25

<!-- b000550 | prose | pages [16] -->
The SI proposed by the United States Army Corps of Engineers (USACE) is expressed as follows:

<!-- b000551 | prose | pages [16] -->
SIi = Ci

<!-- b000552 | prose | pages [16] -->
N

<!-- b000553 | prose | pages [16] -->
N

<!-- b000554 | prose | pages [16] -->
( Si

<!-- b000555 | prose | pages [16] -->
)k

<!-- b000556 | prose | pages [16] -->
∑

<!-- b000557 | prose | pages [16] -->
(17)

<!-- b000558 | prose | pages [16] -->
Di

<!-- b000559 | prose | pages [16] -->
i=1

<!-- b000560 | prose | pages [16] -->
where Ci is a proportional constant, which represents the impact of water shortage on production and life in each state. Si is the water demands which are not satisfied, Di is the total water demands, and k is a constant. The water-shortage index indicates that the socioeconomic impact of water shortage is proportional to the k-th power of the water-deficit rate. The parameter k is determined by considering the relation between the socioeconomic damage cost and the water-supply cost. According to the relevant literature, in the United States, k is equal to 2 [4].

<!-- b000561 | prose | pages [16] -->
Water resource allocation strategy 7.2

<!-- b000562 | prose | pages [16] -->
In Model 2, we assume that water resources are sufficient. Therefore, each state can ob- tain as much water as possible through mutual game from the perspective of maximizing its own income. This leads to the water consumption of each state exceeding basic water demand of each state, resulting in a certain degree of waste of water resources. However, in Question 3, we believe that the water resources obtained by each state are insufficient to meet its basic water demand. Therefore, it is possible that the interests of a game party can not be satisfied, resulting in the game does not exist Nash equilibrium. Therefore, when there is a shortage of water resources, we need to allocate water resources fairly to ensure that the total loss caused by the shortage of water resources in the five states is minimal.

<!-- b000563 | caption | pages [16] -->
Figure 8: The flow chart of water allocation strategy

<!-- b000564 | prose | pages [16] -->
First, to solve the problem, our model divides limited water resources into several parts. Then, we dynamically allocate each part to the state that most needs it. To be specific, we will calculate the water shortage coefficient of each state before allocation. The greater the water shortage coefficient, the more water supply the state needs. Therefore, we allocate water resources to the state with the largest water shortage coefficient. Once

<!-- b000565 | furniture | pages [17] -->
Team # 2213970

<!-- b000566 | furniture | pages [17] -->
Page 17 of 25

<!-- b000567 | prose | pages [17] -->
one time of allocation is completed, water shortage index for each state is updated. Based on the updated water-shortage index, we need to make repeated decisions until limited water resources are allocated completely. The specific flow chart is as follows :

<!-- b000568 | prose | pages [17] -->
Since water is allocated according to the urgency of demand, this allocation method can ensure that each state makes the most use of the limited water resources, so as to achieve the optimal allocation of water resources in the case of water shortage.

<!-- b000569 | prose | pages [17] -->
(a) General use water consumption (b) Electricity water consumption

<!-- b000570 | caption | pages [17] -->
Figure 9: State water supply strategies under different supply rates ψ

<!-- b000571 | prose | pages [17] -->
Analyzing the model results, it can be found that when water is scarce, the strategy will give priority to meeting the general water demand. As a result, as the supply rate increases, the general water consumption fluctuates less, while the electricity water con- sumption is more sensitive to the supply rate. In addition to the source of surface water, the cost of calling other water resources is relatively high, and the vacancy of hydropower can be filled by thermal power.

<!-- b000572 | heading | pages [17] -->
The influence of different factors on the model

<!-- b000573 | prose | pages [17] -->
8

<!-- b000574 | prose | pages [17] -->
Changes in water and electricity demand 8.1

<!-- b000575 | prose | pages [17] -->
Changes in the development of different sectors 8.1.1

<!-- b000576 | prose | pages [17] -->
Although for US states, the development of population, agriculture and industry [5] has entered a point of saturation, approximating the logistic growth curve. But the growth rate in recent years should be roughly constant, so assume that the growth rate of the i-th state’s population, agriculture, and industry is φpeo

<!-- b000577 | prose | pages [17] -->
, φagr

<!-- b000578 | prose | pages [17] -->
,φind

<!-- b000579 | prose | pages [17] -->
, by consulting the data, the i

<!-- b000580 | prose | pages [17] -->
i

<!-- b000581 | prose | pages [17] -->
i

<!-- b000582 | prose | pages [17] -->
values are ABC, and the general water demand in the state wneed

<!-- b000583 | prose | pages [17] -->
demand wneed

<!-- b000584 | prose | pages [17] -->
e,i (t) are expressed as:

<!-- b000585 | prose | pages [17] -->
w,i (t) and electricity water

<!-- b000586 | prose | pages [17] -->
wo,it + (1 + φagr

<!-- b000587 | prose | pages [17] -->
w,i (t) = (1 + φpeo

<!-- b000588 | prose | pages [17] -->
)wpeo

<!-- b000589 | prose | pages [17] -->
wneed

<!-- b000590 | prose | pages [17] -->
(

<!-- b000591 | prose | pages [17] -->
i

<!-- b000592 | prose | pages [17] -->
)wagr

<!-- b000593 | prose | pages [17] -->
wo,it + (1 + φind

<!-- b000594 | prose | pages [17] -->
)wind

<!-- b000595 | prose | pages [17] -->
wo,it

<!-- b000596 | prose | pages [17] -->
i

<!-- b000597 | prose | pages [17] -->
i

<!-- b000598 | prose | pages [17] -->
(18)

<!-- b000599 | prose | pages [17] -->
e,i t + (1 + φagr

<!-- b000600 | prose | pages [17] -->
e,i (t) = (1 + φpeo

<!-- b000601 | prose | pages [17] -->
)wpeo

<!-- b000602 | prose | pages [17] -->
wneed

<!-- b000603 | prose | pages [17] -->
i

<!-- b000604 | prose | pages [17] -->
)wagr

<!-- b000605 | prose | pages [17] -->
e,i t + (1 + φind

<!-- b000606 | prose | pages [17] -->
)wind

<!-- b000607 | prose | pages [17] -->
e,i t

<!-- b000608 | prose | pages [17] -->
i

<!-- b000609 | prose | pages [17] -->
i

<!-- b000610 | furniture | pages [18] -->
Team # 2213970

<!-- b000611 | prose | pages [18] -->
Among them, wpeo

<!-- b000612 | prose | pages [18] -->
wo,i, wagr

<!-- b000613 | prose | pages [18] -->
wo,i, wind

<!-- b000614 | furniture | pages [18] -->
Page 18 of 25

<!-- b000615 | prose | pages [18] -->
wo,i represent the general water consumption for residents and agriculture at the initial time of state i, respectively and industrial general water de- mand; wpeo

<!-- b000616 | prose | pages [18] -->
eo,i, wagr

<!-- b000617 | prose | pages [18] -->
eo,i, wind

<!-- b000618 | prose | pages [18] -->
eo,i similarly represent the initial water consumption for electricity de- mand.

<!-- b000619 | prose | pages [18] -->
Initial period of supply : sufficient water resources Taking one day as the game cycle, according to the functional expressions of the gen- eral water consumption and electric power consumption in each state, the demand for each state in the next day is obtained. Then directly apply the model of problem 2 to solve the water supply situation of each state under the condition of sufficient water resources. The method to verify the rationality of the model is when the actual supply in the strategy is greater than the demand.

<!-- b000620 | prose | pages [18] -->
Later period of water supply : water shortage

<!-- b000621 | prose | pages [18] -->
w,i ≥ww,i or wneed

<!-- b000622 | prose | pages [18] -->
When applying the second question model to solve, we get wneed

<!-- b000623 | prose | pages [18] -->
≥we,i, e,i that is, when the actual supply is less than the demand in each state, it means that the river water resources are in a state of shortage at this time, and the third water supply allocation model under the water shortage situation needs to be used.

<!-- b000624 | prose | pages [18] -->
Demand fluctuates from month to month 8.1.2

<!-- b000625 | prose | pages [18] -->
From the official website, we obtained the data [6] that the consumption of general water and electricity in each state fluctuated with each month. It was found that the peak period of water consumption coincided with the time of drought. This period will inevitably lead to water shortage, so it was substituted into the first In the three-question model, the water distribution strategy of each time period is obtained by solving.

<!-- b000626 | prose | pages [18] -->
(a) General use water consumption (b) Electricity water consumption

<!-- b000627 | caption | pages [18] -->
Figure 10: Strategies for water resource allocation as demand changes

<!-- b000628 | prose | pages [18] -->
By observing who changes the curve in different periods, it is obvious that although August is the period with the most shortage of water resources, in order to meet the higher general water demand at this time, less water resources are allocated to power generation. Therefore, the peak period of general water use in the five states is still concentrated in August, but California, the state with the largest water consumption, has significantly reduced the water resources allocated for power generation, so that the states will suffer the least losses during the period of water shortage.

<!-- b000629 | furniture | pages [19] -->
Team # 2213970

<!-- b000630 | furniture | pages [19] -->
Page 19 of 25

<!-- b000631 | prose | pages [19] -->
8.2 Improvement of renewable energy technology

<!-- b000632 | prose | pages [19] -->
The continuous progress of new energy technology has prompted people to reduce the demand for hydropower. Assuming that the demand for general water remains un- changed, and the decline rate of the demand for hydropower in each state is dei, the de-

<!-- b000633 | prose | pages [19] -->
e,i (t + 1) = (1 −dei)twneed

<!-- b000634 | prose | pages [19] -->
mand for electricity and water in state i can be expressed as wneed

<!-- b000635 | prose | pages [19] -->
eo,i .

<!-- b000636 | prose | pages [19] -->
(a) General use water consumption (b) Electricity water consumption

<!-- b000637 | caption | pages [19] -->
Figure 11: The impact of new energy development on water distribution strategy

<!-- b000638 | prose | pages [19] -->
When comprehensively considering the monthly fluctuation of demand in each state and the addition of new energy, the following distribution strategy is obtained. It can be clearly seen that the addition of new energy has reduced people’s demand for hy- dropower, resulting in a significant decrease in the water resources allocated by hydropower compared to before, while the water resources allocated by general water use have in- creased compared with before. Therefore, the addition of new energy has effectively alle- viated the water shortage in August.

<!-- b000639 | prose | pages [19] -->
8.3 Implementation of water-saving and electricity-saving measures

<!-- b000640 | prose | pages [19] -->
After the water-saving and power-saving measures are used, it can be considered that the decline rate of the demand for general water and power water in each state is the same, and the decline rate of general water demand is set to be φw, and the power water demand decreases. The rate is φe , then the expression of total water consumption is wtotal(t + 1) = (1 −φw)tww,i + (1 −φe)twe,i .

<!-- b000641 | prose | pages [19] -->
The study found that after the implementation of water-saving and electricity-saving measures, the demand for water resources of users was significantly reduced. After the water period has passed, the water supply returns to normal levels.

<!-- b000642 | prose | pages [19] -->
9

<!-- b000643 | heading | pages [19] -->
Sensitivity analysis of the model

<!-- b000644 | prose | pages [19] -->
In our model, we use a Nash equilibrium strategy for solving negotiators for each state. Although the existence of Nash equilibrium can be proved, the solution of Nash equilib- rium is not necessarily in the range of demand, that is, the solution of Nash equilibrium

<!-- b000645 | furniture | pages [20] -->
Team # 2213970

<!-- b000646 | furniture | pages [20] -->
Page 20 of 25

<!-- b000647 | prose | pages [20] -->
(a) General use water consumption (b) Electricity water consumption

<!-- b000648 | caption | pages [20] -->
Figure 12: The impact of energy storage technology development on water distribution strategies

<!-- b000649 | prose | pages [20] -->
cannot meet the basic demand. In this case, although solutions exist, the solutions that exist do not address the actual water demand, which is frustrating.

<!-- b000650 | prose | pages [20] -->
Therefore, we perform sensitivity tests on the changes of water and electricity in the fourth question to judge whether our model is suitable for more complex situations.

<!-- b000651 | prose | pages [20] -->
As figure 15a shown below, the legend shows the relative perturbation for water con- sumption needed in all 5 states. The result tells that there’s a raising trend for water consumption. However, a turning point appears when the relative disturb is 2%, which means Nash equilibrium is not available at such situation.

<!-- b000652 | prose | pages [20] -->
(a) General use water consumption in California (b) Electricity water consumption in California

<!-- b000653 | caption | pages [20] -->
Figure 13: The sensitivity test on Question

<!-- b000654 | prose | pages [20] -->
From these two graphs, we are able to determine the suitable initial proportions, when the proportion decreases, it always has a Nash equilibrium solution. But we should pay attention when we have to increase the proportion, since it’s easier to jump out of the reasonable solution.

<!-- b000655 | prose | pages [20] -->
Therefore, to some extent, our model is robust when decrease the proportions, which is most of our droughty cases.

<!-- b000656 | furniture | pages [21] -->
Team # 2213970

<!-- b000657 | furniture | pages [21] -->
Page 21 of 25

<!-- b000658 | prose | pages [21] -->
10

<!-- b000659 | heading | pages [21] -->
Strengths and Weaknesses

<!-- b000660 | prose | pages [21] -->
10.1

<!-- b000661 | heading | pages [21] -->
Strengths

<!-- b000662 | prose | pages [21] -->
• Creativity: In order to analyze competing interests of water availability for general usage and electricity production, we have created several indicators.

<!-- b000663 | prose | pages [21] -->
• Credibility: The numerical results in our model can be verified quantitatively by factual data, which improves credibility of our model. Also, our model can be used to solve problems in practical such as power planning and scheduling.

<!-- b000664 | prose | pages [21] -->
• Stability: Our basic models have been tested by sensitivity analysis, and the error is acceptable, so the model is stable.

<!-- b000665 | prose | pages [21] -->
10.2

<!-- b000666 | heading | pages [21] -->
Weaknesses

<!-- b000667 | prose | pages [21] -->
• Our models ignore the influence of transient process in power system and assume power flow will not change by hours.

<!-- b000668 | prose | pages [21] -->
• When calculating the power flow of power grid, the solution we find by heuristic algorithm is very reasonable, but it is not necessarily the optimal solution.

<!-- b000669 | heading | pages [21] -->
References

<!-- b000670 | references | pages [21] -->
[1] K.-S. Choi and J.-W. Yeom, “Modeling of management system for hydroelectric power

<!-- b000671 | references | pages [21] -->
generation from water flow,” in 2018 Tenth International Conference on Ubiquitous and

<!-- b000672 | references | pages [21] -->
Future Networks (ICUFN).

<!-- b000673 | references | pages [21] -->
IEEE, 2018, pp. 229–233.

<!-- b000674 | references | pages [21] -->
[2] P. Li, J. Hu, L. Qiu, Y. Zhao, and B. Ghosh, “A distributed economic dispatch strategy

<!-- b000675 | references | pages [21] -->
for power-water networks,” IEEE Transactions on Control of Network Systems, 2021.

<!-- b000676 | references | pages [21] -->
[3] R. L. Cooley, J. F. Harsh, and D. C. Lewis, “Hydrologic engineering methods for water

<!-- b000677 | references | pages [21] -->
resources development. volume 10. principles of ground-water hydrology.” HYDRO-

<!-- b000678 | references | pages [21] -->
LOGIC ENGINEERING CENTER DAVIS CALIF, Tech. Rep., 1972.

<!-- b000679 | references | pages [21] -->
[4] C. Yoo, C. Jun, J. Zhu, and W. Na, “Evaluation of dam water-supply capacity in korea

<!-- b000680 | references | pages [21] -->
using the water-shortage index,” Water, vol. 13, no. 7, p. 956, 2021.

<!-- b000681 | references | pages [21] -->
[5] Z. Huang, M. Hejazi, X. Li, Q. Tang, C. Vernon, G. Leng, Y. Liu, P. Döll, S. Eis-

<!-- b000682 | references | pages [21] -->
ner, D. Gerten et al., “Reconstruction of global gridded monthly sectoral water with-

<!-- b000683 | references | pages [21] -->
drawals for 1971–2010 and analysis of their spatiotemporal patterns,” Hydrology and

<!-- b000684 | references | pages [21] -->
Earth System Sciences, vol. 22, no. 4, pp. 2117–2133, 2018.

<!-- b000685 | references | pages [21] -->
[6] Y. El Baki, K. Boutoial, and A. Medaghri-Alaoui, “The impact of climate change on

<!-- b000686 | references | pages [21] -->
water inflow of the three largest dams in the beni mellal-khenifra region,” in E3S Web

<!-- b000687 | references | pages [21] -->
of Conferences, vol. 314.

<!-- b000688 | references | pages [21] -->
EDP Sciences, 2021, p. 03002.

<!-- b000689 | references | pages [21] -->
[7] A. P. Williams, B. I. Cook, and J. E. Smerdon, “Rapid intensification of the emerging

<!-- b000690 | references | pages [21] -->
southwestern north american megadrought in 2020–2021,” Nature Climate Change, pp.

<!-- b000691 | references | pages [21] -->
1–3, 2022.

<!-- b000692 | furniture | pages [22] -->
Team # 2213970

<!-- b000693 | furniture | pages [22] -->
Page 22 of 25

<!-- b000694 | references | pages [22] -->
Decision System for Optimizing Water Allocation

<!-- b000695 | references | pages [22] -->
Since the end of 21st century, the earth is experiencing the torment of extreme cli-

<!-- b000696 | references | pages [22] -->
mate. A paper in Nature [7] mentioned that the western United States is experiencing

<!-- b000697 | references | pages [22] -->
extreme drought, and the water levels of the three lakes of Colorado, Mead and Powell

<!-- b000698 | references | pages [22] -->
have dropped to an unprecedented low level, facing the danger of drying out.

<!-- b000699 | references | pages [22] -->
In such situation, if we continue to take the conventional water resource allocation

<!-- b000700 | references | pages [22] -->
plan, it will not only cause waste of water resources, but also make the water resources of

<!-- b000701 | references | pages [22] -->
the reservoirs, which are not rich, more dangerous. Therefore, a more reasonable solution

<!-- b000702 | references | pages [22] -->
needs to be proposed.

<!-- b000703 | references | pages [22] -->
This paper proposes the decision system for optimizing water allocation, which can be

<!-- b000704 | references | pages [22] -->
divided into three parts. It analyzes the allocation of water resources when the demand is

<!-- b000705 | references | pages [22] -->
just met, the game situation of each state when the water resources are sufficient, and the

<!-- b000706 | references | pages [22] -->
objective and fair scheduling scheme when the water resources are insufficient.

<!-- b000707 | references | pages [22] -->
We first analyzed data from Hoover Dam and Glen Canyon Dam, found a function

<!-- b000708 | references | pages [22] -->
to estimate reservoir capacity based on water height, and estimated power losses from

<!-- b000709 | references | pages [22] -->
transmission to five states from the two dams. In addition, we looked up the electricity

<!-- b000710 | references | pages [22] -->
and water consumption of five states over a period of time to solve the water resource

<!-- b000711 | references | pages [22] -->
scheduling problem. To minimize the overall water consumption, we apply a simulated

<!-- b000712 | references | pages [22] -->
annealing algorithm to heuristically search for the optimal solution for power distribution.

<!-- b000713 | references | pages [22] -->
The final result shows that without any water supply, Lake Powell, which is upstream,

<!-- b000714 | references | pages [22] -->
may not be able to meet people’s needs after 95 days. If water needs to be supplied, a

<!-- b000715 | references | pages [22] -->
reasonable plan is to replenish water every two days (figure 14), which is a compromise

<!-- b000716 | references | pages [22] -->
between water consumption and practical convenience. After those actions were taken,

<!-- b000717 | references | pages [22] -->
considerable amounts of water are saved.

<!-- b000718 | caption | pages [22] -->
Figure 14: Variation curve of water consumption with water addition cycle

<!-- b000719 | references | pages [22] -->
In practical situations, considering factors such as electricity price, water price, and

<!-- b000720 | references | pages [22] -->
compensation paid to Mexico for excess water consumption in different states, we develop

<!-- b000721 | references | pages [22] -->
a game model to predict the outcome of the game for negotiators based on the interests of

<!-- b000722 | references | pages [22] -->
their states. The game model comprehensively considers the benefits and costs of general

<!-- b000723 | references | pages [22] -->
use and power generation in each state, and obtains a Nash equilibrium for each game.

<!-- b000724 | references | pages [22] -->
Nash equilibrium is the best prediction for the behavior of a completely rational player,

<!-- b000725 | references | pages [22] -->
and any of them will not have the tendency to change their strategy when the current

<!-- b000726 | furniture | pages [23] -->
Team # 2213970

<!-- b000727 | furniture | pages [23] -->
Page 23 of 25

<!-- b000728 | references | pages [23] -->
strategy is Nash equilibrium. We bring the solution obtained in the first question into the

<!-- b000729 | references | pages [23] -->
equation set of the Nash equilibrium, so that the convergence can be faster and the results

<!-- b000730 | references | pages [23] -->
is more likely to meet in the numerically reasonable Nash equilibrium. The results show

<!-- b000731 | references | pages [23] -->
that the solution that just satisfies the demand is not a Nash equilibrium solution, and the

<!-- b000732 | references | pages [23] -->
players will strive for more water than the demand for their own interests. In this case,

<!-- b000733 | references | pages [23] -->
much of the water in excess of demand is wasted, exacerbating drought conditions, as

<!-- b000734 | references | pages [23] -->
shown in figure 15a.

<!-- b000735 | references | pages [23] -->
(a) General use water consumption

<!-- b000736 | references | pages [23] -->
(b) Electricity water consumption

<!-- b000737 | caption | pages [23] -->
Figure 15: Availability of general water and electricity water in five States

<!-- b000738 | references | pages [23] -->
However, in real world not all situations have a reasonable Nash equilibrium, for some

<!-- b000739 | references | pages [23] -->
situations, the amount of water is not enough to meet people’s needs, such as the drought

<!-- b000740 | references | pages [23] -->
that is actually happening in the western part of the United States, so a backup plan is

<!-- b000741 | references | pages [23] -->
required. For the situation where the Nash equilibrium cannot be satisfied, rational ne-

<!-- b000742 | references | pages [23] -->
gotiators cannot have an agreement that is in the interests of all. In this case, an objective

<!-- b000743 | references | pages [23] -->
and fair distribution plan is needed. Considering that insufficient water resources should

<!-- b000744 | references | pages [23] -->
first be supplied to the most urgent areas, we use the water shortage index (SI) as a mea-

<!-- b000745 | references | pages [23] -->
sure. We divide water resources into multiple parts discretely, and use a method similar

<!-- b000746 | references | pages [23] -->
to the allocation of seats in the US Senate to give priority to supplying places where they

<!-- b000747 | references | pages [23] -->
are most needed. This plan is objective and equitable, and can better play the role of

<!-- b000748 | references | pages [23] -->
macro-control at the government level.

<!-- b000749 | references | pages [23] -->
Finally, we considered various situations such as changes in water consumption and

<!-- b000750 | references | pages [23] -->
new energy development, and gave the solution of the model under the corresponding sit-

<!-- b000751 | references | pages [23] -->
uation. This model has reference significance to the mega-drought that actually occurred

<!-- b000752 | references | pages [23] -->
in the western United States.

<!-- b000753 | heading | pages [23] -->
Appendices

<!-- b000754 | heading | pages [23] -->
Python source of Simulated Annealing model :

<!-- b000755 | prose | pages [23] -->
from cmath import inf import numpy as np import random import copy from tqdm import tqdm import configs

<!-- b000756 | furniture | pages [24] -->
Team # 2213970

<!-- b000757 | furniture | pages [24] -->
Page 24 of 25

<!-- b000758 | prose | pages [24] -->
def cal_loss(power,dis,U=500000,r=0.0525): # calculate route loss

<!-- b000759 | prose | pages [24] -->
power*=1000000 delta_power=(power**2/U**2)*r*dis delta_power/=1000000 return delta_power

<!-- b000760 | prose | pages [24] -->
def cal_needed_water(lamda,dis=configs.dis,N=configs.N,H=configs.H,is_print=False): # calcu

<!-- b000761 | prose | pages [24] -->
water1=0 water2=0

<!-- b000762 | prose | pages [24] -->
dam1=0 dam2=0

<!-- b000763 | prose | pages [24] -->
elec=[[],[]] loss=[[],[]]

<!-- b000764 | prose | pages [24] -->
for i in range(5):

<!-- b000765 | prose | pages [24] -->
dam1+=N[i]*lamda[i]/100+cal_loss(N[i]*lamda[i]/100,dis[0][i]) dam2+=N[i]*(1−lamda[i]/100)+cal_loss(N[i]*(1−lamda[i]/100),dis[1][i]) if is_print==True:

<!-- b000766 | prose | pages [24] -->
elec[0].append(N[i]*lamda[i]/100) elec[1].append(N[i]*(1−lamda[i]/100)) loss[0].append(cal_loss(N[i]*lamda[i]/100,dis[0][i])) loss[1].append(cal_loss(N[i]*(1−lamda[i]/100),dis[1][i]))

<!-- b000767 | prose | pages [24] -->
water1=dam1*1e6/(9.81*H[0]*1000*configs.elec_factor) water2=dam2*1e6/(9.81*H[1]*1000*configs.elec_factor)

<!-- b000768 | prose | pages [24] -->
if is_print==True:

<!-- b000769 | prose | pages [24] -->
return elec,loss,[dam1,dam2],[water1,water2]

<!-- b000770 | prose | pages [24] -->
return water1,water2,water1+water2

<!-- b000771 | prose | pages [24] -->
def cal_dam_elec(dis=configs.dis,N=configs.N,iter_times=10000,init_temp=10,step=0.9,final_t

<!-- b000772 | prose | pages [24] -->
T=init_temp

<!-- b000773 | prose | pages [24] -->
minn_value=inf minn_lamda=[] minn_water1=inf minn_water2=inf

<!-- b000774 | prose | pages [24] -->
while(T>final_temp):

<!-- b000775 | prose | pages [24] -->
lamda=[] for i in range(5):

<!-- b000776 | prose | pages [24] -->
lamda.append(50) # initialize each lamda to 50%

<!-- b000777 | prose | pages [24] -->
water_tot=inf

<!-- b000778 | prose | pages [24] -->
# for i in tqdm(range(iter_times)): for i in range(iter_times):

<!-- b000779 | prose | pages [24] -->
last_value=water_tot last_lamda=copy.copy(lamda) temp=random.randint(0,4)

<!-- b000780 | prose | pages [24] -->
if lamda[temp]==0:

<!-- b000781 | prose | pages [24] -->
lamda[temp]+=1

<!-- b000782 | furniture | pages [25] -->
Team # 2213970

<!-- b000783 | furniture | pages [25] -->
Page 25 of 25

<!-- b000784 | prose | pages [25] -->
elif lamda[temp]==100:

<!-- b000785 | prose | pages [25] -->
lamda[temp]−=1 else:

<!-- b000786 | prose | pages [25] -->
temp_=random.randint(0,1) if temp_==0:

<!-- b000787 | prose | pages [25] -->
lamda[temp]−=1 else:

<!-- b000788 | prose | pages [25] -->
lamda[temp]+=1

<!-- b000789 | prose | pages [25] -->
water1,water2,water_tot=cal_needed_water(lamda,dis=dis,N=N,H=H) # water_tot=water1+water2

<!-- b000790 | prose | pages [25] -->
if water_tot>last_value:

<!-- b000791 | prose | pages [25] -->
prob=np.exp(−(water_tot−last_value)/T) temp_prob=random.random() if temp_prob>prob:

<!-- b000792 | prose | pages [25] -->
water_tot=last_value lamda=copy.copy(last_lamda)

<!-- b000793 | prose | pages [25] -->
if water_tot<minn_value:

<!-- b000794 | prose | pages [25] -->
minn_value=water_tot minn_water1=water1 minn_water2=water2 minn_lamda=copy.copy(lamda) if is_print==True:

<!-- b000795 | prose | pages [25] -->
elec,loss,dam,water=cal_needed_water(lamda,dis=dis,N=N,H=H,is_print=is_ print('−−−') print("Electricity production for 5 states are :",elec) print("Electricity loss for 5 states are :",loss) print("Total electricity demands for 2 dams are :",dam) print("Minimum water consumption are :",water) print('−−−') # print("T =",T,", lamda =",lamda,", water cost=",water_tot)

<!-- b000796 | prose | pages [25] -->
T*=step

<!-- b000797 | prose | pages [25] -->
if is_print:

<!-- b000798 | prose | pages [25] -->
print("−−−Result Begin−−−") print("best lamda =",minn_lamda,", least water cost =",minn_value) print("−−−Result End−−−")

<!-- b000799 | prose | pages [25] -->
return minn_lamda,minn_water1,minn_water2,minn_value

<!-- b000800 | prose | pages [25] -->
def cal_power(power):

<!-- b000801 | prose | pages [25] -->
for i in range(len(power)):

<!-- b000802 | prose | pages [25] -->
power[i]*=1000/365/24 return power

<!-- b000803 | prose | pages [25] -->
def func(x,a,b,c):

<!-- b000804 | prose | pages [25] -->
return a*x**3+b*x**2+c*x

<!-- b000805 | prose | pages [25] -->
if __name__=="__main__":

<!-- b000806 | prose | pages [25] -->
N=configs.N dis=configs.dis

<!-- b000807 | prose | pages [25] -->
cal_dam_elec(dis,N)
