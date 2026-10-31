# P-A-2017-66500-89a227cb

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
66500

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | prose | pages [1] -->
F1 ________________

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
T2 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | title | pages [1] -->
A

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | heading | pages [1] -->
2017 MCM Summary Sheet

<!-- b000017 | prose | pages [1] -->
Joint Force in Managing Zambezi River

<!-- b000018 | heading | pages [1] -->
Abstract

<!-- b000019 | prose | pages [1] -->
Owing to the report put forward by the Institution of Risk Management of South Africa, the Kariba dam badly needs maintenance. The three options Zambezi River Authority provided might address the problem. Our modeling group make assessments to the three options and provides feasible plans to replace the former Kariba dam with several smaller dams. The requirements are satisfied in this paper.

<!-- b000020 | prose | pages [1] -->
With regard to requirement 1, we list factors of costs and benefits in advance. Then, we categorize potential cost into two parts, direct cost and indirect cost. With relative profiles, the two categories are quantized. However, the benefits of the three options can hardly be quantified. So we take advantage of fuzzy synthetic evaluation method and work out the relative levels of benefits in the three options. Finally, the return on investment (ROI) is calculated. Based on that, we can safely draw conclusion that option 1 is more economically efficient in a short period. But in the long term, option 3 appears to have more potential profits.

<!-- b000021 | prose | pages [1] -->
When it comes to requirement 2, we establish the water balance equation on both reservoirs and channels at the basis of analysis on water transference. Afterwards, we divide the water management capacities into 3 categorizes, the ability against flood, the ability for water supply and ability for electricity generation. Based on analysis to water management, the multi-dam system of versatile functions is proposed innovatively. Considering the actual factors in selecting dam sites, we screen out 29 possible locations. After then, the number and placement of the new dams is determined using optimization model. In order to lower the cost, we set our goal as the minimum number of dams. Along with the restraints of water balance equation and greater water management capacity, we complete optimization. As is shown in our results, 14 dams should be built as alternative to Kariba dam. Finally, error analysis is attached to our model.

<!-- b000022 | prose | pages [1] -->
For the sake that the new multi-dam system can function well under various circumstance, we set our system in three conditions, normal water circles, long-term drought and outburst flood. Particle swarm optimization (PSO) is adopted repeatedly to optimize the control of water discharge. Compare the result to the actual adjustments made by Kariba dam, we can conclude that the new multi-dam system can provide greater level of protection and water management options. Apart form this, we make thorough evaluations towards optimization scheme and distil general strategy in each condition. At last, we apply sensitivity analysis to conditions under long-term drought and outburst flood. The regulation limits are given under extreme conditions.

<!-- b000023 | prose | pages [1] -->
Last but not least, we take extreme disasters into consideration and use Monte Carlo method to make assessments. The result suggests the new system have a better resistance against disasters. Also, we list the overall strengths and weaknesses of our model as well as the further work.

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | keywords | pages [1] -->
Keywords: return on investment, water balance equation, particle swarm optimization,

<!-- b000026 | prose | pages [1] -->
Monte Carlo method

<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [2] -->
Team # 66500

<!-- b000029 | furniture | pages [2] -->
Page 1 of 22

<!-- b000030 | prose | pages [2] -->
Content

<!-- b000031 | prose | pages [2] -->
1. Introduction .............................................................................................................. 2 1.1. Background ...................................................................................................... 2 1.2. Our Tasks .......................................................................................................... 2 2. General Assumptions ............................................................................................... 3 3. Notions and Symbol Description ............................................................................ 3 4. Maintenance, Reconstruction, or Multi-dams? ..................................................... 4 4.1. Potential cost of each option ............................................................................ 4 4.2. Benefits of each option ..................................................................................... 5 4.3. ROI to each option ........................................................................................... 5 5. Establishment of Water Balance Equation ............................................................ 6 5.1. Reservoirs ......................................................................................................... 6 5.2. Channels ........................................................................................................... 7 6. Water management Capacity of Dam system ....................................................... 7 6.1. The Ability against Flood ................................................................................. 8 6.2. The Ability to Provide Useful Water ................................................................ 8 6.3. The Ability to Generate Electricity ................................................................... 8 6.4. Water Management Capacity in Multi-Dam System ........................................ 8 7. Where to Build the Dams? ...................................................................................... 8 7.1. Select Candidate Locations with Principles ...................................................... 9 7.2. Find the Optimal Solution based on Optimization Model .............................. 10 7.3. Result Analysis ............................................................................................... 12 7.4. Error analysis .................................................................................................. 12 8. Strategy for Modulating the Water Flow Based on PSO.................................... 13 8.1. Addressing the Normal Water Cycles ............................................................. 13 8.2. Strategy for Emergency Water Flow Situations .............................................. 15 8.2.1. Long-term Drought .............................................................................. 15 8.2.2. Outburst Flood ..................................................................................... 16 9. Sensitivity Analysis ................................................................................................ 18 9.1. Sensitivity to Long-Term Drought .................................................................. 18 9.2. Sensitivity to Outburst Flood .......................................................................... 18

<!-- b000032 | heading | pages [2] -->
10. Estimation to the Resistance against Disasters of Multi-Dam System Based on

<!-- b000033 | prose | pages [2] -->
Theory of Monte Carlo .......................................................................................... 19 11. Future Work ......................................................................................................... 20 12. Strengths and Weaknesses ................................................................................... 21 12.1. Strengths ....................................................................................................... 21 12.2. Weaknesses ................................................................................................... 21 13. Conclusion ............................................................................................................ 21 References & Appendix ....................................................................................... 23

<!-- b000034 | furniture | pages [2] -->


<!-- b000035 | furniture | pages [3] -->
Page 2 of 22

<!-- b000036 | furniture | pages [3] -->
Team # 66500

<!-- b000037 | heading | pages [3] -->
1. Introduction

<!-- b000038 | heading | pages [3] -->
1.1. Background

<!-- b000039 | heading | pages [3] -->
1.1.1. Summary to the Kariba Dam

<!-- b000040 | prose | pages [3] -->
The Kariba dam is a double curvature concrete arch dam locating between Zambia and Zimbabwe. It is a dam built upon Zambezi river in Kariba Gorge of the Zambezi river basin. The dam is huge with a size of 128 meters high and 579 meters long. Because of Kariba dam, the Lake Kariba is formed. Kariba Lake has 280 kilometers in length and holds 185 cubic kilometers volume of water.

<!-- b000041 | prose | pages [3] -->
The double curvature concrete arch dam was designed by Coyne et Bellier and constructed between 1955 and 1959 by Impresit of Italy at a cost of $135,000,000 for the first stage with only the Kariba South power cavern. Because of political issues on the total cost of the dam, the whole construction is not completed until 1977.

<!-- b000042 | heading | pages [3] -->
1.1.2. Hydrology of Zambezi River

<!-- b000043 | prose | pages [3] -->
With 2750 kilometers of total length, 135 square kilometers of catchment area and 16 thousand cubic kilometers per second of annual runoff, Zambezi river is the second largest river in Africa. Zambezi river has a large water system and many branches. The tributaries in separate sides have asymmetric developments. The channel upstream is narrow and flow rate there is slow. Some swamps are distributed along the river. When it comes to the midstream, the water runs through the valley and floodplains. The flowing speed depends mainly on the width of channel. In the lower reaches, the river flows through plains and slows down. The water supply in the downstream is abundant and the flow rate varies greatly with the precipitation. The downstream is the main part for transportation.

<!-- b000044 | heading | pages [3] -->
1.2. Our Tasks

<!-- b000045 | prose | pages [3] -->
Since Kariba dam badly needs maintenance, the Zambezi River Authority puts forward three options, repairing the existing dam, rebuilding the existing dam and replacing Kariba dam with a series of smaller dams. What we should do is to make assessments to each option and provide detail information of option 3. Here are our tasks:

<!-- b000046 | prose | pages [3] -->
• Make evaluations to the three options in different aspects, including costs, time required, feasibility, capacity against natural disasters, functions served, etc. Details and specific reasons are attached to the assessments.

<!-- b000047 | prose | pages [3] -->
• Establish principles and models for selecting proper construction sites. Make analysis to the current situation of Zambezi river basin and determine the aspects to be considered.

<!-- b000048 | prose | pages [3] -->
• Build a model to estimate the capacity of the new multi-dam system. Make evaluations to the stability and capacity against extreme water flows and natural disasters. A guidance is about to provided for ZRA managers to justify the actions when handling emergencies.

<!-- b000049 | prose | pages [3] -->
• Make analysis and assessment of our models, find the strength and weakness of them and make future predictions.

<!-- b000050 | furniture | pages [3] -->


<!-- b000051 | furniture | pages [4] -->
Team # 66500

<!-- b000052 | furniture | pages [4] -->
Page 3 of 22

<!-- b000053 | heading | pages [4] -->
2. General Assumptions

<!-- b000054 | prose | pages [4] -->
We make the following assumptions to complete our model through this paper. Further improvements of these simplified assumptions will be achieved later with more reliable data.

<!-- b000055 | prose | pages [4] -->
• Neglect the expansion and contraction of water. If not, it will make the solving process more complex. The changing in the volume of water caused by temperature has a limited influence on the results. Therefore, it is meaningless to introduce expansion and contraction into our system.

<!-- b000056 | prose | pages [4] -->
• The data we used in our models are reliable and accurate. Since the optimization to the problem and the strategy worked out are all based on the actual data.

<!-- b000057 | prose | pages [4] -->
• Zambezi river will either change its channel or dry up in a long period. • The other existing dams in Zambezi river have no effects on the discussion in this paper. Without the interception of the other dams, the research can be simplified.

<!-- b000058 | prose | pages [4] -->
• Constructions of dams in multi-dam system are completed at the same time.

<!-- b000059 | furniture | pages [4] -->


<!-- b000060 | heading | pages [4] -->
3. Notions and Symbol Description

<!-- b000061 | prose | pages [4] -->
We will define the following variables here as they are widely used throughout our paper. Additional variables may be defined later, but will be confined to a particular section.

<!-- b000062 | heading | pages [4] -->
Symbols

<!-- b000063 | prose | pages [4] -->
Definitions

<!-- b000064 | prose | pages [4] -->
𝐶" direct cost

<!-- b000065 | prose | pages [4] -->
𝐶+ indirect cost

<!-- b000066 | prose | pages [4] -->
𝐶.

<!-- b000067 | prose | pages [4] -->
potential cost

<!-- b000068 | prose | pages [4] -->
𝑅𝑂𝐼 Return on investment

<!-- b000069 | prose | pages [4] -->
water storage capacity of 𝑖)* 𝑉(𝑡, 𝑖) reservoir

<!-- b000070 | prose | pages [4] -->
+ dead storage of the 𝑖)* reservoir

<!-- b000071 | prose | pages [4] -->
𝑉,+-

<!-- b000072 | furniture | pages [4] -->


<!-- b000073 | prose | pages [4] -->
the 𝑖)* maximum storage of +

<!-- b000074 | prose | pages [4] -->
𝑉,/0

<!-- b000075 | furniture | pages [4] -->


<!-- b000076 | prose | pages [4] -->
reservoir

<!-- b000077 | prose | pages [4] -->
𝑉89::" flood control capacity

<!-- b000078 | prose | pages [4] -->
water inflow of the 𝑖)* reservoir 𝑄+- 𝑡, 𝑖

<!-- b000079 | prose | pages [4] -->
𝑄:>) 𝑡, 𝑖 discharge of the 𝑖)* reservoir

<!-- b000080 | prose | pages [4] -->
𝐿𝑡, 𝑖 internal loss of reservoir

<!-- b000081 | prose | pages [4] -->
𝑊𝑡, 𝑖 water for external use

<!-- b000082 | furniture | pages [4] -->


<!-- b000083 | heading | pages [4] -->
Symbols

<!-- b000084 | prose | pages [4] -->
Definitions

<!-- b000085 | prose | pages [4] -->
the storage of the 𝑖)* channel 𝑆(𝑡, 𝑖)

<!-- b000086 | prose | pages [4] -->
+

<!-- b000087 | prose | pages [4] -->
𝑆,+-

<!-- b000088 | prose | pages [4] -->
minimum channel storage

<!-- b000089 | furniture | pages [4] -->


<!-- b000090 | prose | pages [4] -->
+

<!-- b000091 | prose | pages [4] -->
𝑆,/0

<!-- b000092 | prose | pages [4] -->
maximum channel storage

<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | prose | pages [4] -->
𝐼+- 𝑡, 𝑖 water inflow from the upper channel

<!-- b000095 | prose | pages [4] -->
∆𝐼𝑡, 𝑖 water imported from surrounding area

<!-- b000096 | prose | pages [4] -->
𝑙(𝑡, 𝑖) internal loss of water in channel

<!-- b000097 | prose | pages [4] -->
𝑞𝑡, 𝑖 discharge of water downstream

<!-- b000098 | prose | pages [4] -->
+

<!-- b000099 | prose | pages [4] -->
𝑞,/0

<!-- b000100 | prose | pages [4] -->
maximum discharge amount

<!-- b000101 | furniture | pages [4] -->


<!-- b000102 | prose | pages [4] -->
𝐴= flood control capacity

<!-- b000103 | prose | pages [4] -->
𝐴?

<!-- b000104 | prose | pages [4] -->
water supply capacity

<!-- b000105 | prose | pages [4] -->
𝐴A generating capacity

<!-- b000106 | prose | pages [4] -->
𝑅?

<!-- b000107 | prose | pages [4] -->
channel flow variance

<!-- b000108 | furniture | pages [5] -->
Team # 66500

<!-- b000109 | furniture | pages [5] -->
Page 4 of 22

<!-- b000110 | heading | pages [5] -->
4. Maintenance, Reconstruction, or Multi-dams?

<!-- b000111 | prose | pages [5] -->
Due to a report proposed by the Institute of Risk Management of South Africa in 2015, Kariba dam, which is located in the midstream of Zambezi river, is in dire need of maintenance. Owing to the urgent situation, the Zambezi River Authority puts forward mainly 3 options. Firstly, repairing the existing Kariba dam; Secondly, reconstruct Kariba dam; Thirdly, replace Kariba dam with a series of smaller dams along Zambezi river. In order to make specific assessments to the three options, firstly, we list the relevant factors of costs and benefits.

<!-- b000112 | caption | pages [5] -->
Table 1: Relevant factors of costs and benefits

<!-- b000113 | prose | pages [5] -->
Cost

<!-- b000114 | prose | pages [5] -->
Static cost Potential cost Benefit

<!-- b000115 | prose | pages [5] -->
• Refurbishment of associated projects

<!-- b000116 | prose | pages [5] -->
• Labor force

<!-- b000117 | prose | pages [5] -->
• Irrigation

<!-- b000118 | prose | pages [5] -->
• Loss of resource

<!-- b000119 | prose | pages [5] -->
• Material

<!-- b000120 | prose | pages [5] -->
benefits

<!-- b000121 | prose | pages [5] -->
• Equipment

<!-- b000122 | prose | pages [5] -->
• Inflation • Loan interests

<!-- b000123 | prose | pages [5] -->
• Electricity generation • Flood control • Shipping

<!-- b000124 | prose | pages [5] -->
Considering the upper elements, we have to quantify every factor to figure out the cost and benefits. However, the actual data can hardly be found. Therefore, we should study on the two parts separately.

<!-- b000125 | heading | pages [5] -->
4.1. Potential cost of each option

<!-- b000126 | caption | pages [5] -->
Table 2: Costs for the Reconstruction of Kariba Dam

<!-- b000127 | prose | pages [5] -->
Item Cost

<!-- b000128 | prose | pages [5] -->
Reconstruction of Kariba Dam US$342 million

<!-- b000129 | prose | pages [5] -->
Maintenance of Kariba dam US$220 million

<!-- b000130 | prose | pages [5] -->
Loss of water resource benefits during reconstruction US$2031 million

<!-- b000131 | prose | pages [5] -->
The values in table 2 [1] specifically states that repairing the Kariba dam requires 220 million dollars and rebuilding the Kariba dam requires 342 million dollars. We set these costs to be direct cost. The table also mentions extra loss during construction is 2031 million dollars, we set it to be indirect cost. The data does not reveal the indirect cost of repairing Kariba dam, but the profiles we gathered shows the time required is approximately 2 years, while time required for reconstruction is 10 years. Therefore, we can assume that the indirect cost of maintenance is 1 /5 of that of reconstruction, nearly 406.2 million dollars. With regard to the establishment of multiple dams, there are less data available. The direct cost of building 10 to 20 small dams is similar to the cost of rebuilding, but a shorter period for construction, nearly 4 years. Therefore, the direct cost of multi-dam system is 342 million dollars and the indirect cost is about 812.4 million dollars. We mark potential cost as 𝐶., direct cost as 𝐶" and indirect

<!-- b000132 | furniture | pages [5] -->


<!-- b000133 | furniture | pages [6] -->
Team # 66500

<!-- b000134 | prose | pages [6] -->
cost as 𝐶+, so 𝐶. = 𝐶" + 𝐶+.

<!-- b000135 | furniture | pages [6] -->
Page 5 of 22

<!-- b000136 | prose | pages [6] -->
According to the analysis we made above, we determine that the potential cost of option1 is 626.2 million dollars, the potential cost of option2 is 2373 million dollars and the potential cost of option3 is 1154.4 million dollars.

<!-- b000137 | heading | pages [6] -->
4.2. Benefits of each option

<!-- b000138 | prose | pages [6] -->
The profiles do not provide specific values measuring the benefits of the three options. We decide to assess the three options with fuzzy synthetic evaluation method [2]. The steps are introduced as follows:

<!-- b000139 | prose | pages [6] -->
• Defining the set of factors 𝑈= irrigation 𝑢=, electricity generation 𝑢?, flood control 𝑢A, shipping 𝑢X

<!-- b000140 | furniture | pages [6] -->


<!-- b000141 | prose | pages [6] -->
• Defining the set of evaluation grades (1)

<!-- b000142 | prose | pages [6] -->
𝑉= excellent 𝑣=, good 𝑣?, average 𝑣A, bad 𝑣X, very bad 𝑣]

<!-- b000143 | furniture | pages [6] -->


<!-- b000144 | prose | pages [6] -->
• Endowing the weights to each factor (2)

<!-- b000145 | prose | pages [6] -->
𝐴= 0.2,0.25,0.35,0.2

<!-- b000146 | furniture | pages [6] -->


<!-- b000147 | prose | pages [6] -->
(3) Afterwards, we determine the fuzzy evaluation matrix R=, R? and RA. The results are shown below:

<!-- b000148 | prose | pages [6] -->
Option1: [0.18,0.48,0.315,0.025,0]; Grade is good Option2: [0.2,0.56,0.228,0.012,0]; Grade is good Option3: [0.23,0.64,0.13,0,0]; Grade is good The grades of the three options are all good. For distinction, the weight of evaluation for good is selected as the grades measuring benefits. Therefore, the grades to the three options are 0.48, 0.56 and 0.515.

<!-- b000149 | heading | pages [6] -->
4.3. ROI to each option

<!-- b000150 | prose | pages [6] -->
With comprehensive consideration of the discuss in potential cost and benefits, we figure out the comparison between the three options. Mark the greatest as 1, the rest are scaled sown. The results are shown in Table 3:

<!-- b000151 | caption | pages [6] -->
Table 3: Comparison of the three options regarding potential cost and benefits

<!-- b000152 | furniture | pages [6] -->


<!-- b000153 | prose | pages [6] -->
Option1

<!-- b000154 | prose | pages [6] -->
Potential cost 0.264

<!-- b000155 | prose | pages [6] -->
Benefits 0.75

<!-- b000156 | prose | pages [6] -->
Option2 Option3

<!-- b000157 | prose | pages [6] -->
1 0.486

<!-- b000158 | prose | pages [6] -->
0.875 1

<!-- b000159 | prose | pages [6] -->
With of help of the return on investment concept in economic, we can make the following definition:

<!-- b000160 | prose | pages [6] -->
ROI =

<!-- b000161 | prose | pages [6] -->
fghgijkl

<!-- b000162 | prose | pages [6] -->
mnkghkjop qnlk

<!-- b000163 | furniture | pages [6] -->


<!-- b000164 | prose | pages [6] -->
(4)

<!-- b000165 | prose | pages [6] -->
ROI of the three options are 2.84, 0.875 and 2.06. Therefore, at this stage, option 1 is of greater economic efficiency. However, in the long term, we can not determine the life span and efficiency after maintenance. As a result, what we can conclude is option 1 is more effective considering recent return on investment. If considering the tradeoff between cost and benefits, option 3 stands out.

<!-- b000166 | furniture | pages [6] -->


<!-- b000167 | furniture | pages [7] -->
Team # 66500

<!-- b000168 | furniture | pages [7] -->
Page 6 of 22

<!-- b000169 | heading | pages [7] -->
5. Establishment of Water Balance Equation

<!-- b000170 | prose | pages [7] -->
In order to study on the capability of water resource management, the river discharge problem comes first. We consider the whole river as a string and the dams cut the string into segments (channels) and nodes (reservoirs). The changes in water quantity during transmission can be calculated by formulating the water balance equation of reservoirs and channels [3]. For convenience, we depict the following diagram:

<!-- b000171 | furniture | pages [7] -->


<!-- b000172 | caption | pages [7] -->
Figure 1: Illustration to water cycle in dams

<!-- b000173 | heading | pages [7] -->
5.1. Reservoirs

<!-- b000174 | prose | pages [7] -->
Water can be accumulated and reserved in reservoirs created by dams. First of all, mark the water storage capacity of 𝑖)* reservoir as 𝑉(𝑡, 𝑖). Then, the water balance equation can be stated as follows:

<!-- b000175 | prose | pages [7] -->
𝑉𝑡+ 1, 𝑖= 𝑉𝑡, 𝑖+ 𝑄+- 𝑡, 𝑖−𝑄:>) 𝑡, 𝑖−𝐿𝑡, 𝑖−𝑊𝑡, 𝑖

<!-- b000176 | furniture | pages [7] -->


<!-- b000177 | prose | pages [7] -->
(5) Where 𝑉𝑡+ 1, 𝑖 and 𝑉𝑡, 𝑖 stand for the water storage at the time of t+1 and t. 𝑄+- 𝑡, 𝑖 refers to the water inflow of the 𝑖)* reservoir form upper reach. 𝑄:>) 𝑡, 𝑖 stands for the discharge of the 𝑖)* reservoir to lower reaches. 𝑄tu 𝑡, 𝑖 is the part in discharge that is used to generate electricity and 𝑂(𝑡, 𝑖) is the rest that are drained directly. 𝐿𝑡, 𝑖 is the internal loss of reservoir, the majority of which are loss through evaporation and permeation. 𝑊𝑡, 𝑖 represents the part of water for external use, including agriculture, industry and domestic water.

<!-- b000178 | prose | pages [7] -->
Owing to the limit in reservoir’s scale and serviceability, the restraints are listed as follows: • Restraints of 𝑉𝑡, 𝑖 We should guarantee that the water storage is smaller than the reservoir’s maximum storage volume and greater than its dead storage capacity, which is presented as follows:

<!-- b000179 | prose | pages [7] -->
+

<!-- b000180 | prose | pages [7] -->
+

<!-- b000181 | prose | pages [7] -->
≤𝑉(𝑡, 𝑖) ≤𝑉,/0

<!-- b000182 | prose | pages [7] -->
𝑉,+-

<!-- b000183 | furniture | pages [7] -->


<!-- b000184 | prose | pages [7] -->
+

<!-- b000185 | furniture | pages [7] -->


<!-- b000186 | prose | pages [7] -->
(6)

<!-- b000187 | prose | pages [7] -->
+

<!-- b000188 | prose | pages [7] -->
refers to the dead storage capacity and 𝑉,/0

<!-- b000189 | prose | pages [7] -->
Where 𝑉,+-

<!-- b000190 | prose | pages [7] -->
refers to the maximum storage volume. The maximum storage volume can be categorized into two parts. 𝑉,/0= stands for the maximum water allowed to store under normal circumstances. 𝑉,/0? stands for the maximum water for use through flooding. Therefore, 𝑉89::" = 𝑉,/0? −𝑉,/0= represents the flood control capacity needs to be retained.

<!-- b000191 | prose | pages [7] -->
• Restraint of 𝑄:>) 𝑡, 𝑖 There are two ways for discharge, one is direct drainage, named flow capacity, the other

<!-- b000192 | furniture | pages [7] -->


<!-- b000193 | furniture | pages [8] -->
Team # 66500

<!-- b000194 | furniture | pages [8] -->
Page 7 of 22

<!-- b000195 | prose | pages [8] -->
is water drained off during electricity generation, named discharge capacity. For each kind of drainage, the restraint can be states as follows:

<!-- b000196 | prose | pages [8] -->
+

<!-- b000197 | prose | pages [8] -->
𝑂(𝑡, 𝑖) ≤𝑂,/0

<!-- b000198 | furniture | pages [8] -->


<!-- b000199 | prose | pages [8] -->
(ℎ) (7)

<!-- b000200 | prose | pages [8] -->
+

<!-- b000201 | prose | pages [8] -->
𝑄tu(𝑡, 𝑖) ≤𝑂tu,/0

<!-- b000202 | furniture | pages [8] -->


<!-- b000203 | prose | pages [8] -->
+

<!-- b000204 | prose | pages [8] -->
(ℎ) (8)

<!-- b000205 | prose | pages [8] -->
+

<!-- b000206 | prose | pages [8] -->
ℎ and 𝑂tu,/0

<!-- b000207 | prose | pages [8] -->
Where h is the water level, 𝑂,/0

<!-- b000208 | prose | pages [8] -->
(ℎ) are the maximum flow capacity and maximum discharge capacity if the 𝑖)* dam, Both of which are related to the water level.

<!-- b000209 | heading | pages [8] -->
5.2. Channels

<!-- b000210 | prose | pages [8] -->
We mark the channel storage of the 𝑖)* channel is 𝑆(𝑡, 𝑖) at i moment. The water balance equation of the 𝑖)* channel is presented in the following expression:

<!-- b000211 | prose | pages [8] -->
𝑆𝑡+ 1, 𝑖= 𝑆𝑡, 𝑖+ 𝐼+- 𝑡, 𝑖+ ∆𝐼𝑡, 𝑖−𝑞𝑡, 𝑖−𝑙(𝑡, 𝑖)

<!-- b000212 | furniture | pages [8] -->


<!-- b000213 | prose | pages [8] -->
(9) Where 𝐼+- 𝑡, 𝑖 is the water inflow from the upper channel, 𝑞𝑡, 𝑖 refers to the discharge of water downstream, ∆𝐼𝑡, 𝑖 is water imported from surrounding area. 𝑙(𝑡, 𝑖) is the internal loss of water in channels. Both ∆𝐼𝑡, 𝑖 and 𝑙(𝑡, 𝑖) are related to the hydrology and length of channel. In this paper, we only focus on the channels in Zambezi river.

<!-- b000214 | prose | pages [8] -->
• Restraint of 𝑞𝑡, 𝑖

<!-- b000215 | prose | pages [8] -->
+

<!-- b000216 | prose | pages [8] -->
+

<!-- b000217 | prose | pages [8] -->
≤𝑆𝑡, 𝑖≤𝑆,/0

<!-- b000218 | prose | pages [8] -->
𝑆,+-

<!-- b000219 | furniture | pages [8] -->


<!-- b000220 | prose | pages [8] -->
+

<!-- b000221 | furniture | pages [8] -->


<!-- b000222 | prose | pages [8] -->
(10)

<!-- b000223 | prose | pages [8] -->
+

<!-- b000224 | prose | pages [8] -->
is the maximum channel storage, 𝑆,+-

<!-- b000225 | prose | pages [8] -->
Where 𝑆,/0

<!-- b000226 | prose | pages [8] -->
prevent it form drying up.

<!-- b000227 | prose | pages [8] -->
• Restraint of 𝐼:>) 𝑡, 𝑖

<!-- b000228 | prose | pages [8] -->
is the minimum channel storage to

<!-- b000229 | prose | pages [8] -->
+

<!-- b000230 | prose | pages [8] -->
𝑞𝑡, 𝑖≤𝑞,/0

<!-- b000231 | furniture | pages [8] -->


<!-- b000232 | prose | pages [8] -->
+

<!-- b000233 | prose | pages [8] -->
Where 𝑞,/0

<!-- b000234 | furniture | pages [8] -->


<!-- b000235 | prose | pages [8] -->
(11)

<!-- b000236 | prose | pages [8] -->
is the maximum discharge amount.

<!-- b000237 | heading | pages [8] -->
6. Water management Capacity of Dam system

<!-- b000238 | prose | pages [8] -->
According to option 3 put forward by ZRA, we should establish a new multi-dam system to replace the existing Kariba dam. The newly-built system should be prior to the existing dam or at least has the same capacity with Kariba dam. To fulfil our purpose, firstly, we have to figure out the meaning of water management capacity. According to profiles of ZRA [4][5], we found that the main task of ZRA is to allocate water to the power stations on the dam and other users. Therefore, we could restate the task with three points:

<!-- b000239 | prose | pages [8] -->
² Adjust the water flow capacity for emergencies like floods. ² Transfer the water in reservoirs to meet daily request ² Adjust the water discharge capacity to meet the requirement in electricity generation

<!-- b000240 | prose | pages [8] -->
According to Expression (1) in 4.1, what we need to do is to change the value of one of the variables to achieve predicted water management capacity.

<!-- b000241 | prose | pages [8] -->
The three kinds of water management capacities are sequentially marked as 𝐴= (the ability against flood), 𝐴? (the ability to provide useful water), 𝐴A (the ability to generate electricity). Since they are all related to the controllable quantity of water, we can use the related water quantity to represent capacities.

<!-- b000242 | furniture | pages [8] -->


<!-- b000243 | furniture | pages [9] -->
Team # 66500

<!-- b000244 | heading | pages [9] -->
6.1. The Ability against Flood

<!-- b000245 | furniture | pages [9] -->
Page 8 of 22

<!-- b000246 | prose | pages [9] -->
In order to take precautions against flood, every reservoir would reserve a certain degree of water to adjust the storage capacity. The more space it reserves, the more capable it will be in flood control. As a result, the flood control capacity can be represented as follows:

<!-- b000247 | prose | pages [9] -->
𝐴= = 𝑉,/0? −𝑉𝑡= 𝑉89::" + 𝑉,/0= −𝑉𝑡

<!-- b000248 | furniture | pages [9] -->


<!-- b000249 | furniture | pages [9] -->


<!-- b000250 | prose | pages [9] -->
(12) Where 𝑉𝑡 refers to the water storage before the flood control.

<!-- b000251 | heading | pages [9] -->
6.2. The Ability to Provide Useful Water

<!-- b000252 | prose | pages [9] -->
In this part, the water storage is used for agriculture, industry and domestic water. But the water remains should greater than the dead storage 𝑉,+-. The water supply capacity is stated as follows:

<!-- b000253 | prose | pages [9] -->
𝐴? = 𝑊(𝑡)

<!-- b000254 | furniture | pages [9] -->


<!-- b000255 | furniture | pages [9] -->


<!-- b000256 | prose | pages [9] -->
(13)

<!-- b000257 | heading | pages [9] -->
6.3. The Ability to Generate Electricity

<!-- b000258 | prose | pages [9] -->
The generating capacity is proportional to quantity of water used to generate electricity 𝑄tu 𝑡. The generating capacity can be stated in the following expression:

<!-- b000259 | prose | pages [9] -->
𝐴A = 𝑄tu(𝑡)

<!-- b000260 | furniture | pages [9] -->


<!-- b000261 | furniture | pages [9] -->


<!-- b000262 | prose | pages [9] -->
(14)

<!-- b000263 | heading | pages [9] -->
6.4. Water Management Capacity in Multi-Dam System

<!-- b000264 | prose | pages [9] -->
With regard to the discussion of single dam system above, the three capacities of multi- dam system can be formulated as follows:

<!-- b000265 | prose | pages [9] -->
x = - 𝑉,/0? 𝑖−𝑉(𝑡, 𝑖)

<!-- b000266 | prose | pages [9] -->
𝐴=

<!-- b000267 | furniture | pages [9] -->


<!-- b000268 | prose | pages [9] -->
+y=

<!-- b000269 | prose | pages [9] -->
x =

<!-- b000270 | prose | pages [9] -->
𝐴?

<!-- b000271 | furniture | pages [9] -->


<!-- b000272 | prose | pages [9] -->
x =

<!-- b000273 | prose | pages [9] -->
𝐴A

<!-- b000274 | furniture | pages [9] -->


<!-- b000275 | prose | pages [9] -->
Where 1 ≤𝑖≤𝑛, 10 ≤𝑛≤20.

<!-- b000276 | furniture | pages [9] -->


<!-- b000277 | furniture | pages [9] -->


<!-- b000278 | prose | pages [9] -->
(15)

<!-- b000279 | prose | pages [9] -->
- - 𝑊(𝑡, 𝑖)

<!-- b000280 | furniture | pages [9] -->


<!-- b000281 | furniture | pages [9] -->


<!-- b000282 | prose | pages [9] -->
(16) +y=

<!-- b000283 | prose | pages [9] -->
- - 𝑄tu(𝑡, 𝑖)

<!-- b000284 | furniture | pages [9] -->


<!-- b000285 | furniture | pages [9] -->


<!-- b000286 | prose | pages [9] -->
(17) +y=

<!-- b000287 | prose | pages [9] -->
Above all, in order to satisfy the assignment that the new system of dams should have the same overall water management capabilities as the existing Kariba, we can conclude the restraints to the following expressions:

<!-- b000288 | prose | pages [9] -->
𝐴=

<!-- b000289 | prose | pages [9] -->
𝐴?

<!-- b000290 | furniture | pages [9] -->


<!-- b000291 | prose | pages [9] -->
𝐴A

<!-- b000292 | prose | pages [9] -->
x ≥𝐴=

<!-- b000293 | prose | pages [9] -->
x ≥𝐴?

<!-- b000294 | prose | pages [9] -->
x ≥𝐴A

<!-- b000295 | furniture | pages [9] -->


<!-- b000296 | prose | pages [9] -->
(18)

<!-- b000297 | prose | pages [9] -->
𝑉𝑡+ 1, 𝑖= 𝑉𝑡, 𝑖+ 𝑄+- 𝑡, 𝑖−𝑄:>) 𝑡, 𝑖−𝐿𝑡, 𝑖−𝑊𝑡, 𝑖 𝑆𝑡+ 1, 𝑖= 𝑆𝑡, 𝑖+ 𝐼+- 𝑡, 𝑖+ ∆𝐼𝑡, 𝑖−𝑞𝑡, 𝑖−𝑙(𝑡, 𝑖)

<!-- b000298 | prose | pages [9] -->
Variables in upper expressions have already been defined. We set 0 ≤𝑖≤𝑛. 𝑖= 0 refers to the case that there only existing the former Kariba dam, in which we can figure out the value

<!-- b000299 | prose | pages [9] -->
x, 𝐴?

<!-- b000300 | prose | pages [9] -->
of 𝐴=, 𝐴? and 𝐴A. In case 1 ≤𝑖≤𝑛, 𝐴=

<!-- b000301 | prose | pages [9] -->
x and 𝐴A

<!-- b000302 | prose | pages [9] -->
x can be worked out.

<!-- b000303 | heading | pages [9] -->
7. Where to Build the Dams?

<!-- b000304 | prose | pages [9] -->
In section 5, we determine the relationship between water management capability and water discharge. However, let along the water discharge, we should take the surrounding situations into consideration when establishing multi-dam systems. When we begin selecting the siting of dams, there are many factors should be considered with. Therefore, we divide the

<!-- b000305 | furniture | pages [9] -->


<!-- b000306 | furniture | pages [10] -->
Team # 66500

<!-- b000307 | furniture | pages [10] -->
Page 9 of 22

<!-- b000308 | prose | pages [10] -->
establishment of multi-dam system into 2 parts: a) Select possible locations to land dams (greater than 20); (b) Analyze combinations of potential locations to make the capacity of multi-dam system balanced the existing Kariba dam.

<!-- b000309 | prose | pages [10] -->
According to the data we gathered [6], we mainly employ 4 indicators for site selection. The four indicators are Discharge, Landform, Resettlement and Rock Stratum. Incorporate with the water discharge, the principles for selection are depicted in Figure 2:

<!-- b000310 | furniture | pages [10] -->


<!-- b000311 | caption | pages [10] -->
Figure 2: Principles in site selection

<!-- b000312 | heading | pages [10] -->
7.1. Select Candidate Locations with Principles

<!-- b000313 | prose | pages [10] -->
We have collected the information of population distribution, topography and flood Frequency [7]. Specific data is attached in appendix. After then, we make integral assessments based on the principles. We choose 29 possible locations, marked from 1 to 29. Some potential dams also exist in our choices (20 is Batoka Gorge, 23 is Devil’s Gorge). The latitude and longitude of both the 29 possible sites and Kariba dam is presents in the following table:

<!-- b000314 | caption | pages [10] -->
Table 4: Latitude and longitude information of possible sites

<!-- b000315 | prose | pages [10] -->
1 2 3

<!-- b000316 | prose | pages [10] -->
14.17˚S, 23,20˚E 14.44˚S, 23,17˚E 14.70˚S, 23.05˚E

<!-- b000317 | prose | pages [10] -->
7 8 9

<!-- b000318 | prose | pages [10] -->
15.77˚S, 23.18˚E 16.11˚S, 23.26˚E 16.25˚S, 23.24˚E

<!-- b000319 | prose | pages [10] -->
13 14 15

<!-- b000320 | prose | pages [10] -->
17.14˚S, 24.05˚E 17.44˚S, 24.22˚E 17.53˚S, 24.59˚E

<!-- b000321 | prose | pages [10] -->
19 20 21

<!-- b000322 | prose | pages [10] -->
17.88˚S, 25.85˚E 17.92˚S, 26.13˚E 17.94˚S, 26.39˚E

<!-- b000323 | prose | pages [10] -->
25 26 27

<!-- b000324 | prose | pages [10] -->
17.52˚S, 27.38˚E 17.35˚S, 27.60˚E 17.03˚S, 27.80˚E

<!-- b000325 | prose | pages [10] -->
4 5 6

<!-- b000326 | prose | pages [10] -->
14.99˚S, 22.96˚E 15.25˚S, 22.97˚E 15.51˚S, 23.08˚E

<!-- b000327 | prose | pages [10] -->
10 11 12

<!-- b000328 | prose | pages [10] -->
16.32˚S, 23.29˚E 16.60˚S, 23.50˚E 16.85˚S, 23.83˚E

<!-- b000329 | prose | pages [10] -->
16 17 18

<!-- b000330 | prose | pages [10] -->
17.56˚S, 24.97˚E 17.78˚S, 25.26˚E 17.86˚S, 25.52˚E

<!-- b000331 | prose | pages [10] -->
22 23 24

<!-- b000332 | prose | pages [10] -->
18.01˚S, 26.77˚E 17.96˚S, 27.95˚E 17.73˚S, 27.22˚E

<!-- b000333 | prose | pages [10] -->
28 29 Kariba Dam

<!-- b000334 | prose | pages [10] -->
16.86˚S, 28.07˚E 16.68˚S, 28.36˚E 16.52˚S, 28.76˚E

<!-- b000335 | prose | pages [10] -->
With analysis to the possible sites, we find that the landforms can be categorized into 3 classes:

<!-- b000336 | prose | pages [10] -->
• Highland at upper reach of Victoria Fall, marked as area A. • Steep terrain by the midstream, marked as area B. • Plain between Gwayi Confluence and Kariba dam, marked as area C.

<!-- b000337 | prose | pages [10] -->
Because of the differences in landforms, the dams built can serve different major functions. Flood hits area A frequently, so the dams built here need a greater 𝑉89::". Area B is steep, which benefits the electricity generation. The storage capacity of dams here is comparatively

<!-- b000338 | furniture | pages [10] -->


<!-- b000339 | furniture | pages [11] -->
Team # 66500

<!-- b000340 | furniture | pages [11] -->
Page 10 of 22

<!-- b000341 | prose | pages [11] -->
smaller. Area C is close to human active areas, so the dams in area C are mainly designed for water usage in agriculture, industry and domestic water. Therefore, we divide Zambezi river into three domains, Flood control, Electricity generation and Water supply. For convenience, they are sequentially abbreviated as subsystem1, subsystem 2 and subsystem 3, which is shown as follows:

<!-- b000342 | furniture | pages [11] -->


<!-- b000343 | caption | pages [11] -->
Figure 3: Subsystems in Zambezi river

<!-- b000344 | heading | pages [11] -->
7.2. Find the Optimal Solution based on Optimization Model

<!-- b000345 | prose | pages [11] -->
What we should do is to build 10 to 20 dams within 29 candidate locations. Therefore, we have to find the best solutions with optimization. We set the optimization goal to the minimum number of dams to built. The restraints of optimization are the number of dams, water management capacity, limits in reservoir storage capacity and channel storage capacity, etc.

<!-- b000346 | prose | pages [11] -->
According the discussion above, the optimization model can be formulated as below:

<!-- b000347 | furniture | pages [11] -->


<!-- b000348 | prose | pages [11] -->
min

<!-- b000349 | furniture | pages [11] -->


<!-- b000350 | furniture | pages [11] -->


<!-- b000351 | prose | pages [11] -->
?~ 𝑋+

<!-- b000352 | furniture | pages [11] -->


<!-- b000353 | prose | pages [11] -->
(19) +y•

<!-- b000354 | prose | pages [11] -->
𝑉𝑡+ 1, 𝑖= 𝑉𝑡, 𝑖+ 𝑄+- 𝑡, 𝑖−𝑄:>) 𝑡, 𝑖−𝐿𝑡, 𝑖−𝑊𝑡, 𝑖 𝑆𝑡+ 1, 𝑖= 𝑆𝑡, 𝑖+ 𝐼+- 𝑡, 𝑖+ ∆𝐼𝑡, 𝑖−𝑞𝑡, 𝑖−𝑙(𝑡, 𝑖)

<!-- b000355 | prose | pages [11] -->
- 𝑉,/0? 𝑖−𝑉𝑡, 𝑖 ∙𝑋+ +y= - 𝑊(𝑡, 𝑖) ∙𝑋+ ≥𝐴? +y=

<!-- b000356 | prose | pages [11] -->
𝑠. 𝑡.

<!-- b000357 | furniture | pages [11] -->


<!-- b000358 | prose | pages [11] -->
- 𝑄tu(𝑡, 𝑖) ∙𝑋+ ≥ 𝐴A +y=

<!-- b000359 | prose | pages [11] -->
+

<!-- b000360 | prose | pages [11] -->
+

<!-- b000361 | prose | pages [11] -->
𝑋+𝑉,+-

<!-- b000362 | prose | pages [11] -->
≤𝑋+𝑉𝑡, 𝑖≤𝑋+𝑉,+-

<!-- b000363 | prose | pages [11] -->
?~ 10 ≤ 𝑋+ ≤20 +y• 𝑋+ = 0 𝑜𝑟 1

<!-- b000364 | furniture | pages [11] -->


<!-- b000365 | prose | pages [11] -->
≥𝐴=

<!-- b000366 | furniture | pages [11] -->


<!-- b000367 | prose | pages [11] -->
(20)

<!-- b000368 | prose | pages [11] -->
Where 𝑋+ is a 0-1 variable. In case 𝑋+ = 1, spot i is selected to construct a dam. Case 𝑋+ = 0 represents the opposite. What’s more, 0 ≤𝑖≤29 . The parameters remains are introduced in 5.1 and 5.2.

<!-- b000369 | prose | pages [11] -->
For the sake of quantitative planning, profiles related to the dam construction are gathered. With synthetically consideration with data of Kariba dam, we design the dams in three subsystems reasonably. The relevant parameters are stated in Table 5:

<!-- b000370 | furniture | pages [11] -->


<!-- b000371 | furniture | pages [12] -->
Team # 66500

<!-- b000372 | furniture | pages [12] -->
Page 11 of 22

<!-- b000373 | caption | pages [12] -->
Table 5: Parameters of dams in subsystems

<!-- b000374 | prose | pages [12] -->
𝑾/𝒎𝟑

<!-- b000375 | furniture | pages [12] -->


<!-- b000376 | prose | pages [12] -->
0.06×10‘ Dam in Subsystem 1

<!-- b000377 | prose | pages [12] -->
0.15×10‘ Dam in Subsystem 2

<!-- b000378 | prose | pages [12] -->
0.376×10‘ Dam in Subsystem 3

<!-- b000379 | prose | pages [12] -->
3×10‘ Kariba Dam

<!-- b000380 | prose | pages [12] -->
𝑽/𝒌𝒎𝟑 𝑽𝒎𝒊𝒏/𝒌𝒎𝟑 𝑽𝒎𝒂𝒙/𝒌𝒎𝟑

<!-- b000381 | prose | pages [12] -->
12.2 7.4 20

<!-- b000382 | prose | pages [12] -->
11.6 4.4 13.2

<!-- b000383 | prose | pages [12] -->
11.2 8 15

<!-- b000384 | prose | pages [12] -->
115.8 51 180.6

<!-- b000385 | prose | pages [12] -->
Where 𝑊 is adjustable water volume, 𝑉 is average capacity, 𝑉,+- is minimum water storage and 𝑉,/0 is maximum capacity. The related data of discharge in target areas are listed as follows:

<!-- b000386 | caption | pages [12] -->
Table 6: Discharge in target areas

<!-- b000387 | furniture | pages [12] -->


<!-- b000388 | prose | pages [12] -->
unit: 𝑚A/𝑠

<!-- b000389 | prose | pages [12] -->
Discharge in Sub basin Sub basin

<!-- b000390 | prose | pages [12] -->
114 Lungue Bungo

<!-- b000391 | prose | pages [12] -->
69.4 Luanginga

<!-- b000392 | prose | pages [12] -->
0 Kwando/Chobe

<!-- b000393 | prose | pages [12] -->
-17.6 Barotse

<!-- b000394 | prose | pages [12] -->
206 Kariba

<!-- b000395 | prose | pages [12] -->
Total water discharge so far

<!-- b000396 | prose | pages [12] -->
1129

<!-- b000397 | prose | pages [12] -->
1198

<!-- b000398 | prose | pages [12] -->
1198

<!-- b000399 | prose | pages [12] -->
1180

<!-- b000400 | prose | pages [12] -->
1386

<!-- b000401 | prose | pages [12] -->
For each combination of 𝑋+, we simulate the water quantity in each stage using MATLAB to determine whether the water management capacity reaches its standard. The flowchart below describes our algorithm:

<!-- b000402 | furniture | pages [12] -->


<!-- b000403 | caption | pages [12] -->
Figure 4: Algorithm in simulating combinations

<!-- b000404 | prose | pages [12] -->
of 𝑋+ measuring water management

<!-- b000405 | furniture | pages [12] -->


<!-- b000406 | furniture | pages [12] -->


<!-- b000407 | prose | pages [12] -->
Step 1: Initialize n to 0

<!-- b000408 | prose | pages [12] -->
Step 2: Go through 𝑥+ and find every combination satisfying the sum of 𝑥+ is n

<!-- b000409 | prose | pages [12] -->
Step 3: Initialize V t, i , 𝑄+- 𝑡, 1 , 𝐿𝑡, 𝑖 and ∆𝐼𝑡, 𝑖, 𝑙(𝑡, 𝑖) and calculate relative V t + 1, i , 𝑄:>) 𝑡, 𝑖, 𝑊(𝑡, 𝑖) with water balance equation

<!-- b000410 | prose | pages [12] -->
x , 𝐴?

<!-- b000411 | prose | pages [12] -->
x and 𝐴A

<!-- b000412 | prose | pages [12] -->
x and make

<!-- b000413 | prose | pages [12] -->
Step 4: Figure out 𝐴=

<!-- b000414 | prose | pages [12] -->
comparison with 𝐴=, 𝐴? and 𝐴A to ensure that the overall capacity of the new multi- dam is greater than Kariba dam

<!-- b000415 | heading | pages [12] -->
Step 5: According to the result of

<!-- b000416 | prose | pages [12] -->
comparison , if accepted, print out the relative combination of 𝑥+ and n, end. If rejected, 𝑛= 𝑛+ 1, go to Step 2

<!-- b000417 | furniture | pages [13] -->
Team # 66500

<!-- b000418 | heading | pages [13] -->
7.3. Result Analysis

<!-- b000419 | furniture | pages [13] -->
Page 12 of 22

<!-- b000420 | prose | pages [13] -->
With compilation of MATLAB, we can find the optimal locations to build dams. 14 dams are required here, the codes of them are 3, 4, 6, 9, 10, 15, 17, 19, 21, 22, 24, 26, 28, 29. They are marked on the map shown in Figure 5:

<!-- b000421 | furniture | pages [13] -->


<!-- b000422 | caption | pages [13] -->
Figure 5: Placement of multi-dam system

<!-- b000423 | prose | pages [13] -->
Since the results are worked out under the restraint of water management capacity, we could safely draw the conclusion that the overall water management capacity of new multi- dam system is greater than that of the existing Kariba dam.

<!-- b000424 | heading | pages [13] -->
7.4. Error analysis

<!-- b000425 | prose | pages [13] -->
In order to prove the accuracy of our model, we bring the data up to 2008 into it. We figure out the discharge downstream of Kariba dam and compare it to the statistical data to complete our error analysis. We collect actual data for 12 months and the results are shown below:

<!-- b000426 | caption | pages [13] -->
Table 7: Error analysis of model 1

<!-- b000427 | prose | pages [13] -->
Month Actual value Estimate value Absolute error Fractional error

<!-- b000428 | prose | pages [13] -->
Jan 2436.8 2529.1

<!-- b000429 | prose | pages [13] -->
Feb 1042.2 1124.2

<!-- b000430 | prose | pages [13] -->
Mar 905.8 1001.6

<!-- b000431 | prose | pages [13] -->
April 1162.7 1243.6

<!-- b000432 | prose | pages [13] -->
May 1368.8 1426.1

<!-- b000433 | prose | pages [13] -->
Jun 1111.2 1011.45

<!-- b000434 | prose | pages [13] -->
Jul 1228.6 1312.1

<!-- b000435 | prose | pages [13] -->
Aug 1075.5 1111.7

<!-- b000436 | prose | pages [13] -->
Sep 981.9 991.4

<!-- b000437 | prose | pages [13] -->
Oct 875.9 901.2

<!-- b000438 | prose | pages [13] -->
Nov 1047.9 951.6

<!-- b000439 | prose | pages [13] -->
Dec 1364.4 1400.6

<!-- b000440 | prose | pages [13] -->
92.3 3.79%

<!-- b000441 | prose | pages [13] -->
82 7.87%

<!-- b000442 | prose | pages [13] -->
95.8 10.58%

<!-- b000443 | prose | pages [13] -->
80.9 6.96%

<!-- b000444 | prose | pages [13] -->
57.3 4.19%

<!-- b000445 | prose | pages [13] -->
99.75 8.98%

<!-- b000446 | prose | pages [13] -->
83.5 6.80%

<!-- b000447 | prose | pages [13] -->
36.2 3.37%

<!-- b000448 | prose | pages [13] -->
9.5 0.97%

<!-- b000449 | prose | pages [13] -->
25.3 2.89%

<!-- b000450 | prose | pages [13] -->
96.3 9.19%

<!-- b000451 | prose | pages [13] -->
36.2 2.65%

<!-- b000452 | prose | pages [13] -->
According to the last two columns in Table 7, we find that the maximum error is 10.58%, the average error is 5.68%. From our perspectives, the errors may result from the lack of evaporation and infiltration in actual data. Therefore, we could safely draw conclusion that the

<!-- b000453 | furniture | pages [13] -->


<!-- b000454 | furniture | pages [14] -->
Team # 66500

<!-- b000455 | prose | pages [14] -->
errors in our model is acceptable.

<!-- b000456 | furniture | pages [14] -->
Page 13 of 22

<!-- b000457 | heading | pages [14] -->
8. Strategy for Modulating the Water Flow Based on PSO

<!-- b000458 | prose | pages [14] -->
In spite of the great water management capacity of the new multi-dam system, the system itself is complex. Comparing to a single dam, it appears to be more difficult in managing a multi-dam system. Therefore, it is necessary for us to work out the mechanism of water management under various circumstances. Depending on researches on different situations, we work out an appropriate regulation strategy for ZRA to better operate on and manage the multi- dam system.

<!-- b000459 | heading | pages [14] -->
8.1. Addressing the Normal Water Cycles

<!-- b000460 | prose | pages [14] -->
The Zambezi river has explicit withered water period and high water period. Without regulation and control to the water discharge, the water flow will vary greatly via seasons. What’s more, since the large geographical breadth of Zambezi river, the time monsoon season starts varies, which leads to the time fluctuations in high water periods. As a result of this, the measures taken by the dams may vary at the same time period.

<!-- b000461 | prose | pages [14] -->
Under normal water cycles, the drainage and storage of water in each dam should be adapted to narrow down the differences in seasonal water flow. The discharge should be regulated in a steady level. For this sake, we establish the channel flow variance 𝑅? to describe the level of water flow stability. The definition of 𝑅? are given as follows:

<!-- b000462 | prose | pages [14] -->
𝑅? =

<!-- b000463 | prose | pages [14] -->
=

<!-- b000464 | prose | pages [14] -->
-

<!-- b000465 | furniture | pages [14] -->


<!-- b000466 | prose | pages [14] -->
šy= -˜= 𝑆𝑘, 𝑖−𝑆(𝑖) ?

<!-- b000467 | furniture | pages [14] -->


<!-- b000468 | prose | pages [14] -->
(21)

<!-- b000469 | prose | pages [14] -->
Where 𝑆𝑘, 𝑖 stands for the water discharge of the 𝑖)* channel in month k. n refers to the month to be studied. 𝑆(𝑖) is the mean discharge in month n. The purpose of our water transfer scheme is to narrow down the value of 𝑅?.

<!-- b000470 | prose | pages [14] -->
The programming model are formulated as follows:

<!-- b000471 | prose | pages [14] -->
min 𝑅? =

<!-- b000472 | prose | pages [14] -->
=

<!-- b000473 | prose | pages [14] -->
-

<!-- b000474 | furniture | pages [14] -->


<!-- b000475 | prose | pages [14] -->
šy= -˜=

<!-- b000476 | prose | pages [14] -->
+

<!-- b000477 | prose | pages [14] -->
+

<!-- b000478 | prose | pages [14] -->
𝑉,+-

<!-- b000479 | prose | pages [14] -->
≤𝑉(𝑘, 𝑖) ≤𝑉,/0

<!-- b000480 | prose | pages [14] -->
+

<!-- b000481 | prose | pages [14] -->
+

<!-- b000482 | prose | pages [14] -->
𝑄:>),+-

<!-- b000483 | prose | pages [14] -->
≤𝑄:>) 𝑡, 𝑖≤𝑄:>),/0

<!-- b000484 | prose | pages [14] -->
𝑆𝑘, 0 −𝑆(0) ?

<!-- b000485 | furniture | pages [14] -->


<!-- b000486 | prose | pages [14] -->
(22)

<!-- b000487 | prose | pages [14] -->
𝑉𝑘+ 1, 𝑖−𝑉𝑘, 𝑖= +𝑄+- 𝑘, 𝑖−𝑄:>) 𝑘, 𝑖−𝐿𝑘, 𝑖−𝑊𝑘, 𝑖

<!-- b000488 | furniture | pages [14] -->


<!-- b000489 | prose | pages [14] -->
+

<!-- b000490 | prose | pages [14] -->
+

<!-- b000491 | prose | pages [14] -->
𝑆,+-

<!-- b000492 | prose | pages [14] -->
≤𝑆𝑘, 𝑖≤𝑆,/0

<!-- b000493 | prose | pages [14] -->
+

<!-- b000494 | prose | pages [14] -->
+

<!-- b000495 | prose | pages [14] -->
𝑞,+-

<!-- b000496 | prose | pages [14] -->
≤𝑞𝑘, 𝑖≤𝑞,/0

<!-- b000497 | furniture | pages [14] -->


<!-- b000498 | prose | pages [14] -->
(23)

<!-- b000499 | prose | pages [14] -->
𝑆𝑘+ 1, 𝑖= 𝑆𝑘, 𝑖+ 𝐼+- 𝑘, 𝑖+ ∆𝐼𝑘, 𝑖−𝑞𝑘, 𝑖−𝑙(𝑘, 𝑖)

<!-- b000500 | prose | pages [14] -->
As is shown in the objective function, in case 𝑆𝑘, 0 , the discharge of a segment of channel downstream is studied, through which we can easily make comparison to the discharge under control of the existing Kariba dam.

<!-- b000501 | prose | pages [14] -->
For quantitative calculation, we find statistics of the discharge of each segment of channels as a function of month in normal years. In order to find the optimal solutions, Particle Swarm Optimization (PSO) [8] is adopted to simulate the changes in water storage of different reservoirs. With multiple calculations compiled by MATLAB, we successfully work out the

<!-- b000502 | furniture | pages [14] -->


<!-- b000503 | furniture | pages [15] -->
Team # 66500

<!-- b000504 | furniture | pages [15] -->
Page 14 of 22

<!-- b000505 | prose | pages [15] -->
comparatively better adjustment scheme. The fitness function curve is shown in Figure 6.

<!-- b000506 | furniture | pages [15] -->


<!-- b000507 | caption | pages [15] -->
Figure 6: Fitness function curve of adjustment scheme

<!-- b000508 | prose | pages [15] -->
The water allocation scheme of the three subsystems is listed in Table 8:

<!-- b000509 | caption | pages [15] -->
Table 8: Water allocation scheme of subsystems in normal years

<!-- b000510 | furniture | pages [15] -->


<!-- b000511 | prose | pages [15] -->
Month Oct Nov

<!-- b000512 | prose | pages [15] -->
Unit: 𝑘𝑚A

<!-- b000513 | prose | pages [15] -->
Dec Jan Feb Mar

<!-- b000514 | prose | pages [15] -->
-0.10001 Subsystem 1 -0.09476 -0.09083 -0.09535 0.062192 0.062201

<!-- b000515 | prose | pages [15] -->
-0.00673 Subsystem 2 0.001557 -0.00644 -0.01244 0.055984 0.055952

<!-- b000516 | prose | pages [15] -->
-0.0446 Subsystem 3 -0.0585 -0.05369

<!-- b000517 | prose | pages [15] -->
Month April May

<!-- b000518 | prose | pages [15] -->
-0.05871 0.049746 0.049742

<!-- b000519 | prose | pages [15] -->
Jun Jul Aug Sep

<!-- b000520 | prose | pages [15] -->
0.060161 Subsystem 1 0.060934 0.058666 -0.09978 -0.09523 -0.09389

<!-- b000521 | prose | pages [15] -->
0.051366 Subsystem 2 0.05598 0.049408 -0.00733 -0.01196 -0.00999

<!-- b000522 | prose | pages [15] -->
0.048489 Subsystem 3 0.048205 0.049725 -0.04715 -0.04637 -0.05335

<!-- b000523 | prose | pages [15] -->
The values in Table 8 represents the variance in the reservoirs’ monthly storage. For example, -0.09476 means the subsystem 1 has to decrease water storage by 0.09476 in October. In other words, the net water discharge here is 0.09476 𝑘𝑚A. It is noteworthy that the data for quantitative calculation is collected in normal years. When handling a specific year, we cannot directly put the values shown in Table 8 into practice, even through there is proved no extreme situations. However, tentative treatment is given under normal water cycles. The reservoir should store water in Jul, Aug, Set, Oct, Nov, Dec and Jan. In the rest of months, water storage should be reduced.

<!-- b000524 | prose | pages [15] -->
The comparison in adjustment between the new multi-dam system and Kariba dam is depicted in Figure 7:

<!-- b000525 | furniture | pages [15] -->


<!-- b000526 | furniture | pages [16] -->
Team # 66500

<!-- b000527 | furniture | pages [16] -->
Page 15 of 22

<!-- b000528 | prose | pages [16] -->
normal water cycles

<!-- b000529 | prose | pages [16] -->
3000

<!-- b000530 | prose | pages [16] -->
2000

<!-- b000531 | prose | pages [16] -->
1000

<!-- b000532 | prose | pages [16] -->
0

<!-- b000533 | prose | pages [16] -->
Oct Nov Dec Jan Feb Mar April May Jun

<!-- b000534 | prose | pages [16] -->
Kariba Dam

<!-- b000535 | prose | pages [16] -->
Jul Aug Sep

<!-- b000536 | prose | pages [16] -->
Mluti-Dam System

<!-- b000537 | furniture | pages [16] -->


<!-- b000538 | caption | pages [16] -->
Figure 7: Comparisons under normal water cycles

<!-- b000539 | prose | pages [16] -->
From Figure 7, we can find that in the new multi-dam system, the changes in discharge appears to be more steady, which proves that our strategy is practical.

<!-- b000540 | heading | pages [16] -->
8.2. Strategy for Emergency Water Flow Situations

<!-- b000541 | prose | pages [16] -->
Zambezi river basin suffers from natural disasters frequently, the major of them are long- term drought and outburst flood. In order to deal with these emergencies, we should make further adjustments to our system.

<!-- b000542 | heading | pages [16] -->
8.2.1.  Long-term Drought

<!-- b000543 | prose | pages [16] -->
During the long-term drought period, the discharge of the whole river is generally reduced. Our adjustments are made to satisfy the need that the water supply in the downstream is abundant. As a result, we build the programming objective as follows:

<!-- b000544 | prose | pages [16] -->
max min 𝑆𝑘, 0

<!-- b000545 | furniture | pages [16] -->


<!-- b000546 | furniture | pages [16] -->


<!-- b000547 | prose | pages [16] -->
(24) The restraints are the same with that of Expression (23). With the data we gathered about Zambezi river in dry years, we can easily make calculations. Similar to that in 7.1, with multiple times of simulations using PSO, the water allocation schemes of each subsystem is shown in

<!-- b000548 | caption | pages [16] -->
Table 9:

<!-- b000549 | caption | pages [16] -->
Table 9: Water allocation schemes of each subsystem in drought period

<!-- b000550 | furniture | pages [16] -->


<!-- b000551 | prose | pages [16] -->
Drought Oct Nov

<!-- b000552 | prose | pages [16] -->
Unit: 𝑘𝑚A

<!-- b000553 | prose | pages [16] -->
Dec Jan Feb Mar

<!-- b000554 | prose | pages [16] -->
-1.04203 Subsystem 1 -0.27787 1.026436 0.249226 -0.65067 0.191609

<!-- b000555 | prose | pages [16] -->
0.475582 Subsystem 2 -0.07421 -2.17294 -0.37972 -0.24793 -0.35295

<!-- b000556 | prose | pages [16] -->
-0.86552 Subsystem 3 -0.90204 0.130651

<!-- b000557 | prose | pages [16] -->
Drought April May

<!-- b000558 | prose | pages [16] -->
-0.98385 0.050967 0.220654

<!-- b000559 | prose | pages [16] -->
Jun Jul Aug Sep

<!-- b000560 | prose | pages [16] -->
-0.40244 Subsystem 1 1.299811 2.357025 -1.58494 0.123439 0.352689

<!-- b000561 | prose | pages [16] -->
-0.49026 Subsystem 2 -0.00116 -1.46258 0.023731 0.056262 -0.25739

<!-- b000562 | prose | pages [16] -->
0.300223 Subsystem 3 0.393705 0.38105 0.421971 -1.20925 -1.44345

<!-- b000563 | prose | pages [16] -->
With analysis of the values in Table 9, we find that during the drought period, subsystem 1 is always in discharge state while subsystem 3 is always in impounding state. When drought happens, the river is under prolonged low water conditions. Here are our strategies:

<!-- b000564 | prose | pages [16] -->
² Drain the water in subsystem 1 downstream, which provides sufficient water

<!-- b000565 | furniture | pages [16] -->


<!-- b000566 | furniture | pages [17] -->
Team # 66500

<!-- b000567 | prose | pages [17] -->
for electricity generation in subsystem 2.

<!-- b000568 | prose | pages [17] -->
²

<!-- b000569 | furniture | pages [17] -->
Page 16 of 22

<!-- b000570 | prose | pages [17] -->
Subsystem 3 should manage to store water to meet the needs of water supply downstream. At the meantime, the water level downstream is kept in certain state to satisfy the shipping requirements.

<!-- b000571 | prose | pages [17] -->
With Comparison of the water management results under the circumstance of multi-dam system and Kariba dam, we can depict the differences in the following chart:

<!-- b000572 | furniture | pages [17] -->


<!-- b000573 | caption | pages [17] -->
Figure 8: Comparison between multi-dam system and Kariba dam facing with drought

<!-- b000574 | prose | pages [17] -->
As is shown in Figure 8, we can safely draw the conclusion that the multi-dam system has a better water management capacity under drought conditions over that of Kariba dam. What’s more, the results indicate that when facing with long-term drought, the multi-dam system holds enough water to survive the drought periods.

<!-- b000575 | heading | pages [17] -->
8.2.2. Outburst Flood

<!-- b000576 | prose | pages [17] -->
When it comes to outburst flood upstream, the discharge of the following channels will meet a sudden rise. If one segment of channels holds water more than its channel storage capacity, the water will spill out and results to the extension of flood-affected areas. Therefore, the water in channels should be reduced to prevent water form spilling out and finally diminish the chance of destructive flood. As a result, the programming objective is stated as follows:

<!-- b000577 | prose | pages [17] -->
min max 𝑆𝑘, 0

<!-- b000578 | furniture | pages [17] -->


<!-- b000579 | furniture | pages [17] -->


<!-- b000580 | prose | pages [17] -->
(25) The restraints are the same with that in 7.1. We bring the historical data related to flooding into our model and make multiple calculations with the help of PSO. The results are shown in

<!-- b000581 | caption | pages [17] -->
Table 10:

<!-- b000582 | caption | pages [17] -->
Table 10: Water allocation schemes of each subsystem in flooding period Unit: 𝑘𝑚A

<!-- b000583 | furniture | pages [17] -->


<!-- b000584 | prose | pages [17] -->
Flooding Oct Nov

<!-- b000585 | prose | pages [17] -->
Subsystem 1 1.835305 3.04317

<!-- b000586 | prose | pages [17] -->
Dec Jan Feb Mar

<!-- b000587 | prose | pages [17] -->
1.9973 3.626824 3.837354 3.491875

<!-- b000588 | prose | pages [17] -->
1.028984 Subsystem 2 -0.50768 -0.8993 -0.20848 0.832249 1.573858

<!-- b000589 | prose | pages [17] -->
0.148498 Subsystem 3 0.791538 -0.06238

<!-- b000590 | prose | pages [17] -->
Flooding April May

<!-- b000591 | prose | pages [17] -->
1.03733 3.084586 3.713995

<!-- b000592 | prose | pages [17] -->
Jun Jul Aug Sep

<!-- b000593 | prose | pages [17] -->
5.628686 Subsystem 1 5.391049 5.664352

<!-- b000594 | furniture | pages [17] -->


<!-- b000595 | prose | pages [17] -->
1.062068 0.740065 2.635967

<!-- b000596 | furniture | pages [18] -->
Team # 66500

<!-- b000597 | furniture | pages [18] -->
Page 17 of 22

<!-- b000598 | prose | pages [18] -->
-1.76944 Subsystem 2 1.5882 0.417108 -0.04835 -0.60331 -0.3279

<!-- b000599 | prose | pages [18] -->
2.829153 Subsystem 3 2.946934 3.021101 2.481431 2.735348 0.025019

<!-- b000600 | caption | pages [18] -->
Table 10 shows that when flood reaches, Subsystem 1 needs to keep storing water to

<!-- b000601 | prose | pages [18] -->
decrease the direct discharge of flood so that reduce the stress of the following dams. Subsystem 2 should drain water in advance to receive the redundant water which can not be stored by subsystem 1. Also, dams in subsystem 3 should take advantage of storage capacities to diminish the water pulled downstream.

<!-- b000602 | prose | pages [18] -->
The comparison of water management capacity between multi-dam system and Kariba dam is plotted as follows:

<!-- b000603 | furniture | pages [18] -->


<!-- b000604 | caption | pages [18] -->
Figure 9: Comparison between multi-dam system and Kariba dam facing with Flood

<!-- b000605 | prose | pages [18] -->
As is depicted in Figure 9, under the control of multiple dams, the effects caused by flood are comparatively smaller, and the flood peak is lower. Therefore, we can draw the conclusion that multi-dam system can significantly reduce the loss caused by flood and waterlog.

<!-- b000606 | prose | pages [18] -->
The strategy introduced above demonstrates that when flood happens, we should take full consideration of the storage capacity of dams to partake the strass in channels. Apart form this, in more detail, we can make full use of channel storage capacity to control the flood. The multi- dam system actually conducive to this. The strategy is specifically discussed as follows:

<!-- b000607 | prose | pages [18] -->
² When the flood comes, the first dam makes full use of its storage to store the flood. At the meantime, the following dams quickly drain water downstream to lower the water level itself and that of the upper channels.

<!-- b000608 | prose | pages [18] -->
² While water level of the first dam reaches its warning line, water in the first dam should be quickly pulled down to the sequential dams. At this point, the second dam stops draining water and utilize both the storage itself and the storage capacity of the upper channels.

<!-- b000609 | prose | pages [18] -->
² So as follow. Make full use of every storage capacity of both dams and channels to control the flood. With this strategy, the entire system can deal with more serious flood.

<!-- b000610 | prose | pages [18] -->
Our strategy is depicted in the following graphs:

<!-- b000611 | furniture | pages [18] -->


<!-- b000612 | furniture | pages [19] -->
Page 18 of 22

<!-- b000613 | furniture | pages [19] -->
Team # 66500

<!-- b000614 | prose | pages [19] -->
Stage 1 Stage 2

<!-- b000615 | furniture | pages [19] -->


<!-- b000616 | caption | pages [19] -->
Figure 10: Illustration to our strategy

<!-- b000617 | heading | pages [19] -->
9. Sensitivity Analysis

<!-- b000618 | prose | pages [19] -->
In this part, based on the actual data, we manually increase the severity of drought and flood and analyze the changes in water downstream after the system regulation.

<!-- b000619 | heading | pages [19] -->
9.1. Sensitivity to Long-Term Drought

<!-- b000620 | prose | pages [19] -->
We decrease the actual data on water discharge during drought period. The decreasement are 100 𝑚𝑠?, 150 𝑚𝑠? and 200 𝑚𝑠?. The changes in the water discharge downstream is depicted in the following figure:

<!-- b000621 | furniture | pages [19] -->


<!-- b000622 | caption | pages [19] -->
Figure 11: Sensitivity analysis to long-term drought

<!-- b000623 | prose | pages [19] -->
As is shown in Figure 11, we find that if we increase the severity of drought, the water discharge is lowered. What should be mentioned there is there is a sharp change when decreasing water discharge from 100 𝑚𝑠? to 150 𝑚𝑠? , which means that the decreasement of 150 𝑚𝑠? is approaching the limits when facing with long-term drought.

<!-- b000624 | heading | pages [19] -->
9.2. Sensitivity to Outburst Flood

<!-- b000625 | prose | pages [19] -->
We increase the actual data on water discharge during flood period. The incensement here are 100 𝑚𝑠?, 200 𝑚𝑠? and 300 𝑚𝑠?. The changes in the water discharge downstream is represented as follows:

<!-- b000626 | furniture | pages [19] -->


<!-- b000627 | furniture | pages [20] -->
Team # 66500

<!-- b000628 | furniture | pages [20] -->
Page 19 of 22

<!-- b000629 | furniture | pages [20] -->


<!-- b000630 | caption | pages [20] -->
Figure 12: Sensitivity analysis to outburst flood

<!-- b000631 | prose | pages [20] -->
As is shown in Figure 12, with the increase in flood, the water discharge downstream rises sharply and quickly reaches the maximum of channel storage capacity. In conclusion, when approaching the limit of maximum water treatment, our model is comparatively sensitive.

<!-- b000632 | heading | pages [20] -->
10. Estimation to the Resistance against Disasters of Multi-Dam

<!-- b000633 | prose | pages [20] -->
System Based on Theory of Monte Carlo

<!-- b000634 | prose | pages [20] -->
Owing to the fact that earthquakes and flood frequently hit Zambezi river basin, we make estimations to resistance against disasters of both the Kariba dam and the multi-dam system.

<!-- b000635 | prose | pages [20] -->
Since the existence of disaster is normally unpredictable and lack of regular patterns, we can hardly adopt analytic method to estimate the resistance against disasters. The Monte Carlo method makes use of a random number generator to simulate the happen of a disaster through either direct or indirect sampling. The probability of occurrence of disasters is determined through the historical data on the frequency and severity of the target disaster. After repeating independent sampling for times, we can simulate a similar situation. The practice has showed that after 50 to 300 times of simulations, the distributions function could always be determined convergence [9].

<!-- b000636 | prose | pages [20] -->
Assuming that the probability of occurrence of disaster t is 𝑃(𝑡) , relatively, the probability of dam collapse is marked as 𝑃𝑦. Therefore, the risk rate of dam when facing with disasters can be represented as follows:

<!-- b000637 | prose | pages [20] -->
𝑃• = 𝑃(𝑡) ∙𝑃(𝑦)

<!-- b000638 | furniture | pages [20] -->


<!-- b000639 | prose | pages [20] -->
(26) According to historical data, parameter can be given as follows:

<!-- b000640 | caption | pages [20] -->
Table 11: Parameters in determining risk rate of dam when facing with earthquake

<!-- b000641 | prose | pages [20] -->
Magnitude

<!-- b000642 | prose | pages [20] -->
Under Earthquake

<!-- b000643 | prose | pages [20] -->
magnitude 3

<!-- b000644 | prose | pages [20] -->
4-5

<!-- b000645 | prose | pages [20] -->
Probability of

<!-- b000646 | prose | pages [20] -->
54.40% 39.5% occurrence

<!-- b000647 | prose | pages [20] -->
Damage to dam 0 0

<!-- b000648 | prose | pages [20] -->
Magnitude

<!-- b000649 | prose | pages [20] -->
Magnitude

<!-- b000650 | prose | pages [20] -->
Above

<!-- b000651 | prose | pages [20] -->
6-7

<!-- b000652 | prose | pages [20] -->
8-9

<!-- b000653 | prose | pages [20] -->
magnitude 9

<!-- b000654 | prose | pages [20] -->
5% 1% 0.10%

<!-- b000655 | prose | pages [20] -->
20% 80% 100%

<!-- b000656 | caption | pages [20] -->
Table 12: Parameters in determining risk rate of dam when facing with flood

<!-- b000657 | furniture | pages [20] -->


<!-- b000658 | furniture | pages [21] -->
Team # 66500

<!-- b000659 | prose | pages [21] -->
Flood

<!-- b000660 | heading | pages [21] -->
1 in 1-year

<!-- b000661 | heading | pages [21] -->
1 in 10-year

<!-- b000662 | prose | pages [21] -->
Probability of

<!-- b000663 | prose | pages [21] -->
67.90% 25% occurrence

<!-- b000664 | prose | pages [21] -->
Damage to dam 0 0

<!-- b000665 | furniture | pages [21] -->
Page 20 of 22

<!-- b000666 | heading | pages [21] -->
1 in 100-year

<!-- b000667 | heading | pages [21] -->
1 in 1000-year

<!-- b000668 | heading | pages [21] -->
1 in 10000-year

<!-- b000669 | prose | pages [21] -->
6% 1% 0.01%

<!-- b000670 | prose | pages [21] -->
3% 10% 30%

<!-- b000671 | prose | pages [21] -->
The subsystems we designed distribute in three separate regions. The earthquake can only cause damage to one of the three regions. Also, when serious flood comes, the subsystem upstream can provide alarms to subsystem in midstream. When the dams in subsystem 1 are damaged by flood, the dams in the midstream could quickly drain water to lower the loss. Base on the analysis and data collected, we simulate the situation when disaster comes with the help of MATLAB. The results are shown as follows:

<!-- b000672 | furniture | pages [21] -->


<!-- b000673 | caption | pages [21] -->
Figure 13: Simulation to situation of disasters using Monte Carlo method

<!-- b000674 | prose | pages [21] -->
As is shown in Figure 13, after 1000 times of independent sampling, the red dots represent the damage to Kariba dam caused by earthquakes and Flood. The blue stars represent the damage to the new multi-dam system caused by disasters. From the results, we can safely draw the conclusion that the damage caused by earthquakes is more severe than that of Flood. Since the multi-dam system is more flexible in controlling water storage, the overall resistance against natural disasters is obviously better than the existing Kariba dam.

<!-- b000675 | heading | pages [21] -->
11. Future Work

<!-- b000676 | prose | pages [21] -->
Since the limitations on time and data, there are several factors missed in our model. In the near future, we will make the following adjustments:

<!-- b000677 | prose | pages [21] -->
• Make estimations to the effects on ecosystem. Since Zambezi river basin is rich in biodiversity, the constructions cannot avoid impacts on the living species. How to limit the influences on local species should be taken into consideration.

<!-- b000678 | prose | pages [21] -->
• Reschedule the locations of some dams. Some countries are in bad needs of benefits of dams. The layout of multi-dam system may also be changed according to specific needs of certain countries.

<!-- b000679 | prose | pages [21] -->
• The sewage regulation capacity should be considered. Owing to the fact that there are many factories along Zambezi river and the pollution problem generally draws people’s

<!-- b000680 | furniture | pages [21] -->


<!-- b000681 | furniture | pages [22] -->
Page 21 of 22

<!-- b000682 | furniture | pages [22] -->
Team # 66500

<!-- b000683 | prose | pages [22] -->
attention, the multi-dam system should have a better sewage regulation capacity to meet the needs of sustainable development.

<!-- b000684 | heading | pages [22] -->
12. Strengths and Weaknesses

<!-- b000685 | heading | pages [22] -->
12.1. Strengths

<!-- b000686 | prose | pages [22] -->
• Our strategy has a better overall capability than the existing dam. No matter what situation the multi-dam system is facing with, the overall water management capacity is prior to that of the existing Kariba dam, as is shown in section 7.

<!-- b000687 | prose | pages [22] -->
• We take extreme water conditions into consideration. We provide detailed guidance to ZRA managers handling long-term drought and outburst flood. Graphs are also provided in this paper.

<!-- b000688 | prose | pages [22] -->
• Our model is practical and reliable. We do sensitivity analysis and error analysis to test the accuracy of our model. Based on the outcomes, we safely draw the conclusion that the simulation in our model fits the actual situations.

<!-- b000689 | heading | pages [22] -->
12.2. Weaknesses

<!-- b000690 | prose | pages [22] -->
• The data we obtained is limited. Because the time limit, we are unable to search for more comprehensive data. Therefore, our research is restricted in comparatively smaller range.

<!-- b000691 | prose | pages [22] -->
• We neglect some aspects that plays a role in site selection. For example, ecology is also crucial in determining the locations. The construction may lead to some extinctions of local species. What’s more, human resettlement and influences related to it should also be taken into consideration.

<!-- b000692 | heading | pages [22] -->
13. Conclusion

<!-- b000693 | prose | pages [22] -->
In response to the report that alarms the maintenance of Kariba dam, ZRA are in favor of three options, including repairing the existing dam, rebuilding Kariba dam and replacing Kariba dam with a series of smaller dams. We follow the requirements put forward by ZRA and several efforts are made towards this.

<!-- b000694 | prose | pages [22] -->
Firstly, we briefly make assessments to the 3 options. Both the costs and benefits are analyzed in detail. ROI is adopted in this paper to measure the benefits. Also, specific data are provided in this section and a reasonable method is introduced.

<!-- b000695 | prose | pages [22] -->
Secondly, for the prerequisite, we establish the water balance equations of both reservoirs and channels. Formulas are given orderly in section 5. Followed by this, the water management capacity is measured in section 6, with the establishment of optimization model. The water management is specifically categorized into 3 parts, the ability against flood, the ability for water supply and the ability for electricity generation.

<!-- b000696 | prose | pages [22] -->
Thirdly, we choose the appropriate locations to build dams. First of all, we select 29 candidate sites and provide their accurate locations in longitude and latitude. Then, specific parameters of dams in our multi-dam system is given. Since different sub basins have different characteristics, the dams built there serve different major functions. Therefore, the multi-dam

<!-- b000697 | furniture | pages [22] -->


<!-- b000698 | furniture | pages [23] -->
Page 22 of 22

<!-- b000699 | furniture | pages [23] -->
Team # 66500

<!-- b000700 | prose | pages [23] -->
system can be divided into 3 subsystems, one for flood control, one for electricity generation and the rest one is designed for water supply. Finally, we determine 14 locations to build dams.

<!-- b000701 | prose | pages [23] -->
In the following part, we investigate into the newly build multi-dam system and specifically provide strategies under various circumstances. Firstly, we address the normal water cycle. Afterwards, extreme conditions are taken into consideration. Both long-term drought and outburst flood are included. We provide strategies when facing with such emergencies in detail. What’s more, guidance is provided for ZRA managers that explains the actions and managements should be taken to deal with emergency water flows. Additionally, comparisons between multi-dam system and Kariba dam are provided.

<!-- b000702 | prose | pages [23] -->
Last but not least, sensitivity analysis and error analysis are attached to our model. We predict our future works and specifically state the merits and shortcomings.

<!-- b000703 | furniture | pages [23] -->


<!-- b000704 | furniture | pages [23] -->


<!-- b000705 | furniture | pages [24] -->
Team # 66500

<!-- b000706 | furniture | pages [24] -->


<!-- b000707 | heading | pages [24] -->
References

<!-- b000708 | references | pages [24] -->
[1] L. Gottschalk, Hydrological extremes, 1st ed. Wallingford: IAHS, 1999.

<!-- b000709 | references | pages [24] -->
[2] S. Si and Z. Sun, Mathematical Modeling Algorithms and Applications, 2nd ed.

<!-- b000710 | references | pages [24] -->
Beijing: National Defense Industry Press, 2016.

<!-- b000711 | references | pages [24] -->
[3] Z. Wang, "Study on Dispatching of Water Quality and Quantity in Gate Dam Group

<!-- b000712 | references | pages [24] -->
on Shaying River", HYDROCHINA Xibei Engineering Corporation, Xi'an, vol. 1006-

<!-- b000713 | references | pages [24] -->
2610201401-0001-06, no. 1, 2014.

<!-- b000714 | references | pages [24] -->
[4] UNEP-IETC, Planning and Management of Lakes and Reservoirs: An Integrated

<!-- b000715 | references | pages [24] -->
Approach to Eutrophication, 1st ed. Newsletter and Technical Publications, 1999.

<!-- b000716 | references | pages [24] -->
[5]"Zambezi

<!-- b000717 | references | pages [24] -->
River

<!-- b000718 | references | pages [24] -->
Authority",

<!-- b000719 | references | pages [24] -->
En.wikipedia.org.

<!-- b000720 | references | pages [24] -->
[Online].

<!-- b000721 | references | pages [24] -->
Available:

<!-- b000722 | references | pages [24] -->
https://en.wikipedia.org/wiki/Zambezi_River_Authority. (Accessed: 23- Jan- 2017).

<!-- b000723 | references | pages [24] -->
[6] J. Mou, "Expert system for selection of dam site: Introduction to site selector (DDS)",

<!-- b000724 | references | pages [24] -->
China Academic Journal Electronic Publishing House, pp. 15-17.

<!-- b000725 | references | pages [24] -->
[7] V. Alavian, M. Wishart, L. Croneborg, R. Dankova, K. Kim and L. Pierre-Charles,

<!-- b000726 | references | pages [24] -->
The Zambezi River basin, 1st ed. Washington, DC: The Wolrd Bank, Water Resources

<!-- b000727 | references | pages [24] -->
Management, Africa Region, 2010.

<!-- b000728 | references | pages [24] -->
[8] S Yu, Analysis and Applications of Optimization with Matlab, 1st ed. Beijing:

<!-- b000729 | references | pages [24] -->
Tsinghua University Press, 2014.

<!-- b000730 | references | pages [24] -->
[9] R. Jiao, "Study on multi objective risk analysis model and application of reservoir

<!-- b000731 | references | pages [24] -->
flood control", master, Zhengzhou University, 2004.

<!-- b000732 | furniture | pages [24] -->


<!-- b000733 | furniture | pages [24] -->


<!-- b000734 | furniture | pages [24] -->


<!-- b000735 | furniture | pages [24] -->


<!-- b000736 | furniture | pages [25] -->
Team # 66500

<!-- b000737 | furniture | pages [25] -->


<!-- b000738 | heading | pages [25] -->
Appendix

<!-- b000739 | prose | pages [25] -->
1.PROGRAM ①MATLAB program of PSO

<!-- b000740 | prose | pages [25] -->
function apso

<!-- b000741 | prose | pages [25] -->
Lb=2.592e-3*[-7.8*5 -1.6*3 -3.8*6 -7.8*5 -1.6*3 -3.8*6 -7.8*5 -1.6*3 -

<!-- b000742 | prose | pages [25] -->
3.8*6 -7.8*5 -1.6*3 -3.8*6 -7.8*5 -1.6*3 -3.8*6 -7.8*5 -1.6*3 -3.8*6 -7.8*5

<!-- b000743 | prose | pages [25] -->
-1.6*3 -3.8*6 -7.8*5 -1.6*3 -3.8*6 -7.8*5 -1.6*3 -3.8*6 -7.8*5 -1.6*3 -

<!-- b000744 | prose | pages [25] -->
3.8*6 -7.8*5 -1.6*3 -3.8*6 -7.8*5 -1.6*3 -3.8*6 ];

<!-- b000745 | prose | pages [25] -->
Ub=2.592e-3*[4.8*5 7.2*3 3.2*6 4.8*5 7.2*3 3.2*6 4.8*5 7.2*3 3.2*6

<!-- b000746 | prose | pages [25] -->
4.8*5 7.2*3 3.2*6 4.8*5 7.2*3 3.2*6 4.8*5 7.2*3 3.2*6 4.8*5 7.2*3 3.2*6

<!-- b000747 | prose | pages [25] -->
4.8*5 7.2*3 3.2*6 4.8*5 7.2*3 3.2*6 4.8*5 7.2*3 3.2*6 4.8*5 7.2*3 3.2*6

<!-- b000748 | prose | pages [25] -->
4.8*5 7.2*3 3.2*6];

<!-- b000749 | prose | pages [25] -->
para=[1000 150 0.95];

<!-- b000750 | prose | pages [25] -->
[gbest,fmin]=pso_mincon(@cost,@constraint,Lb,Ub,para);

<!-- b000751 | prose | pages [25] -->
Bestsolution=gbest

<!-- b000752 | prose | pages [25] -->
fmin

<!-- b000753 | prose | pages [25] -->
function f=cost(deltaV)

<!-- b000754 | prose | pages [25] -->
[Q,V]=ditui(deltaV);

<!-- b000755 | prose | pages [25] -->
f=var(Q);

<!-- b000756 | prose | pages [25] -->
function [g,geq]=constraint(deltaV)

<!-- b000757 | prose | pages [25] -->
[Q,V]=ditui(deltaV);

<!-- b000758 | prose | pages [25] -->
a=V(:,1)-20*5;

<!-- b000759 | prose | pages [25] -->
b=V(:,2)-13.2*3;

<!-- b000760 | prose | pages [25] -->
c=V(:,3)-15*6;

<!-- b000761 | prose | pages [25] -->
d=7.4*5-V(:,1);

<!-- b000762 | prose | pages [25] -->
e=4.4*5-V(:,2);

<!-- b000763 | prose | pages [25] -->
f=8*5-V(:,3);

<!-- b000764 | prose | pages [25] -->
g=[a' b' c' d' e' f'];

<!-- b000765 | prose | pages [25] -->
geq=[];

<!-- b000766 | prose | pages [25] -->
function [gbest,fbest]=pso_mincon(fhandle,fnonlin,Lb,Ub,para)

<!-- b000767 | prose | pages [25] -->
if nargin<=4,

<!-- b000768 | prose | pages [25] -->
para=[20 150 0.95];

<!-- b000769 | prose | pages [25] -->
end

<!-- b000770 | prose | pages [25] -->
n=para(1);

<!-- b000771 | prose | pages [25] -->
time=para(2);

<!-- b000772 | prose | pages [25] -->
gamma=para(3);

<!-- b000773 | prose | pages [25] -->
scale=abs(Ub-Lb);

<!-- b000774 | prose | pages [25] -->
if abs(length(Lb)-length(Ub))>0,

<!-- b000775 | prose | pages [25] -->
disp('Constraints must have equal size');

<!-- b000776 | prose | pages [25] -->
return

<!-- b000777 | prose | pages [25] -->
end

<!-- b000778 | furniture | pages [25] -->


<!-- b000779 | furniture | pages [26] -->
Team # 66500

<!-- b000780 | furniture | pages [26] -->


<!-- b000781 | prose | pages [26] -->
alpha=0.2;

<!-- b000782 | prose | pages [26] -->
beta=0.5;

<!-- b000783 | prose | pages [26] -->
best=init_pso(n,Lb,Ub);

<!-- b000784 | prose | pages [26] -->
fbest=1.0e+100;

<!-- b000785 | prose | pages [26] -->
for t=1:time,

<!-- b000786 | prose | pages [26] -->
for i=1:n,

<!-- b000787 | prose | pages [26] -->
fval=Fun(fhandle,fnonlin,best(i,:));

<!-- b000788 | prose | pages [26] -->
if fval<=fbest,

<!-- b000789 | prose | pages [26] -->
gbest=best(i,:);

<!-- b000790 | prose | pages [26] -->
fbest=fval;

<!-- b000791 | prose | pages [26] -->
end

<!-- b000792 | prose | pages [26] -->
end

<!-- b000793 | prose | pages [26] -->
alpha=newPara(alpha,gamma);

<!-- b000794 | prose | pages [26] -->
best=pso_move(best,gbest,alpha,beta,Lb,Ub);

<!-- b000795 | prose | pages [26] -->
str=strcat('Best estimates: gbest=',num2str(gbest));

<!-- b000796 | prose | pages [26] -->
str=strcat(str,'  iteration='); str=strcat(str,num2str(t));

<!-- b000797 | prose | pages [26] -->
disp(str);

<!-- b000798 | prose | pages [26] -->
fitness1(t)=fbest;

<!-- b000799 | prose | pages [26] -->
plot(fitness1,'r','Linewidth',2)

<!-- b000800 | prose | pages [26] -->
grid on

<!-- b000801 | prose | pages [26] -->
hold on

<!-- b000802 | prose | pages [26] -->
title('ÊÊÓ¦¶È')

<!-- b000803 | prose | pages [26] -->
end

<!-- b000804 | prose | pages [26] -->
function [guess]=init_pso(n,Lb,Ub)

<!-- b000805 | prose | pages [26] -->
ndim=length(Lb);

<!-- b000806 | prose | pages [26] -->
for i=1:n,

<!-- b000807 | prose | pages [26] -->
guess(i,1:ndim)=Lb+rand(1,ndim).*(Ub-Lb);

<!-- b000808 | prose | pages [26] -->
end

<!-- b000809 | prose | pages [26] -->
function ns=pso_move(best,gbest,alpha,beta,Lb,Ub)

<!-- b000810 | prose | pages [26] -->
n=size(best,1); ndim=size(best,2);

<!-- b000811 | prose | pages [26] -->
scale=(Ub-Lb);

<!-- b000812 | prose | pages [26] -->
for i=1:n,

<!-- b000813 | prose | pages [26] -->
ns(i,:)=best(i,:)+beta*(gbest-

<!-- b000814 | prose | pages [26] -->
best(i,:))+alpha.*randn(1,ndim).*scale;

<!-- b000815 | prose | pages [26] -->
end

<!-- b000816 | prose | pages [26] -->
ns=findrange(ns,Lb,Ub);

<!-- b000817 | prose | pages [26] -->
function ns=findrange(ns,Lb,Ub)

<!-- b000818 | prose | pages [26] -->
n=length(ns);

<!-- b000819 | prose | pages [26] -->
for i=1:n,

<!-- b000820 | prose | pages [26] -->
ns_tmp=ns(i,:);

<!-- b000821 | prose | pages [26] -->
I=ns_tmp<Lb;

<!-- b000822 | prose | pages [26] -->
ns_tmp(I)=Lb(I);

<!-- b000823 | furniture | pages [26] -->


<!-- b000824 | furniture | pages [27] -->
Team # 66500

<!-- b000825 | furniture | pages [27] -->


<!-- b000826 | prose | pages [27] -->
J=ns_tmp>Ub;

<!-- b000827 | prose | pages [27] -->
ns_tmp(J)=Ub(J);

<!-- b000828 | prose | pages [27] -->
ns(i,:)=ns_tmp;

<!-- b000829 | prose | pages [27] -->
end

<!-- b000830 | prose | pages [27] -->
function alpha=newPara(alpha,gamma);

<!-- b000831 | prose | pages [27] -->
alpha=alpha*gamma;

<!-- b000832 | prose | pages [27] -->
function z=Fun(fhandle,fnonlin,u)

<!-- b000833 | prose | pages [27] -->
z=fhandle(u);

<!-- b000834 | prose | pages [27] -->
z=z+getconstraints(fnonlin,u);

<!-- b000835 | prose | pages [27] -->
function Z=getconstraints(fnonlin,u)

<!-- b000836 | prose | pages [27] -->
PEN=10^15;

<!-- b000837 | prose | pages [27] -->
lam=PEN; lameq=PEN;

<!-- b000838 | prose | pages [27] -->
Z=0;

<!-- b000839 | prose | pages [27] -->
[g,geq]=fnonlin(u);

<!-- b000840 | prose | pages [27] -->
for k=1:length(g),

<!-- b000841 | prose | pages [27] -->
Z=Z+ lam*g(k)^2*getH(g(k));

<!-- b000842 | prose | pages [27] -->
end

<!-- b000843 | prose | pages [27] -->
for k=1:length(geq),

<!-- b000844 | prose | pages [27] -->
Z=Z+lameq*geq(k)^2*geteqH(geq(k));

<!-- b000845 | prose | pages [27] -->
end

<!-- b000846 | prose | pages [27] -->
function H=getH(g)

<!-- b000847 | prose | pages [27] -->
if g<=0,

<!-- b000848 | prose | pages [27] -->
H=0;

<!-- b000849 | prose | pages [27] -->
else

<!-- b000850 | prose | pages [27] -->
H=1;

<!-- b000851 | prose | pages [27] -->
end

<!-- b000852 | prose | pages [27] -->
function H=geteqH(g)

<!-- b000853 | prose | pages [27] -->
if g==0,

<!-- b000854 | prose | pages [27] -->
H=0;

<!-- b000855 | prose | pages [27] -->
else

<!-- b000856 | prose | pages [27] -->
H=1;

<!-- b000857 | prose | pages [27] -->
end ②Objective function

<!-- b000858 | prose | pages [27] -->
function y=fitness_flood(deltaV)

<!-- b000859 | prose | pages [27] -->
[Q,V]=ditui_flood(deltaV);

<!-- b000860 | prose | pages [27] -->
y=max(Q);

<!-- b000861 | furniture | pages [27] -->


<!-- b000862 | prose | pages [27] -->
function y=fitness_drought(deltaV)

<!-- b000863 | prose | pages [27] -->
[Q,V]=ditui_drought(deltaV);

<!-- b000864 | prose | pages [27] -->
y=-min(Q);

<!-- b000865 | furniture | pages [27] -->


<!-- b000866 | prose | pages [27] -->
function y=fitness(deltaV)

<!-- b000867 | furniture | pages [27] -->


<!-- b000868 | furniture | pages [28] -->
Team # 66500

<!-- b000869 | furniture | pages [28] -->


<!-- b000870 | prose | pages [28] -->
[Q,V]=ditui(deltaV);

<!-- b000871 | prose | pages [28] -->
y=var(Q-I); ③Recursive function

<!-- b000872 | prose | pages [28] -->
function [Q0,V]=ditui_flood(deltaV)

<!-- b000873 | prose | pages [28] -->
deltaI=2.592e-3*[-69.9000000000000,25.8000000000000,-166.600000000000;-

<!-- b000874 | prose | pages [28] -->
75.4000000000000,10.8000000000000,-66.6000000000000;-75.4000000000000,-34,-

<!-- b000875 | prose | pages [28] -->
160.100000000000;-75.4000000000000,-83.1000000000000,-162.500000000000;-

<!-- b000876 | prose | pages [28] -->
75.4000000000001,-138.900000000000,-136.600000000000;-53.5000000000000,-

<!-- b000877 | prose | pages [28] -->
629.700000000000,-105.300000000000;-20.6000000000000,-

<!-- b000878 | prose | pages [28] -->
120.900000000000,221.900000000000;-

<!-- b000879 | prose | pages [28] -->
39.8000000000001,399.300000000000,106.300000000000;-

<!-- b000880 | prose | pages [28] -->
53.5000000000000,63.9000000000000,-107.200000000000;-58.9000000000000,-

<!-- b000881 | prose | pages [28] -->
1.09999999999999,-137.100000000000;-67.2000000000000,-10.7000000000000,-

<!-- b000882 | prose | pages [28] -->
30.2000000000000;-68.4000000000000,-10.2000000000000,-1.99999999999997;];

<!-- b000883 | prose | pages [28] -->
in_put=2.592e-

<!-- b000884 | prose | pages [28] -->
3*[10.7000000000000,23.8000000000000,84.7000000000000,248.100000000000,414.

<!-- b000885 | prose | pages [28] -->
900000000000,1113.70000000000,889.400000000000,358.500000000000,170.3000000

<!-- b000886 | prose | pages [28] -->
00000,93.5000000000000,52.7000000000000,15.7000000000000;];

<!-- b000887 | prose | pages [28] -->
V(1,1)=12.2*5;V(1,2)=11.6*3;V(1,3)=11.2*6;

<!-- b000888 | prose | pages [28] -->
for k=1:12

<!-- b000889 | prose | pages [28] -->
Qin(k,1)=in_put(k)+deltaI(k,1);

<!-- b000890 | prose | pages [28] -->
Qout(k,1)=Qin(k,1)-deltaV(3*(k-1)+1);

<!-- b000891 | prose | pages [28] -->
Qin(k,2)=Qout(k,1)+deltaI(k,2);

<!-- b000892 | prose | pages [28] -->
Qout(k,2)=Qin(k,2)-deltaV(3*(k-1)+2);

<!-- b000893 | prose | pages [28] -->
Qin(k,3)=Qout(k,2)+deltaI(k,3);

<!-- b000894 | prose | pages [28] -->
Qout(k,3)=Qin(k,3)-deltaV(3*(k-1)+3);

<!-- b000895 | prose | pages [28] -->
Q0(k)=Qout(k,3);

<!-- b000896 | prose | pages [28] -->
V(k+1,3)=V(k,3)+deltaV(3*(k-1)+3);

<!-- b000897 | prose | pages [28] -->
V(k+1,2)=V(k,2)+deltaV(3*(k-1)+2);

<!-- b000898 | prose | pages [28] -->
V(k+1,1)=V(k,1)+deltaV(3*(k-1)+1);

<!-- b000899 | prose | pages [28] -->
end

<!-- b000900 | furniture | pages [28] -->


<!-- b000901 | prose | pages [28] -->
function [Q0,V]=ditui_drought(deltaV)

<!-- b000902 | prose | pages [28] -->
deltaI=2.592e-3*[-119.900000000000,-24.2000000000000,-

<!-- b000903 | prose | pages [28] -->
216.600000000000;-125.400000000000,-39.2000000000000,-116.600000000000;-

<!-- b000904 | prose | pages [28] -->
125.400000000000,-84,-210.100000000000;-125.400000000000,-

<!-- b000905 | prose | pages [28] -->
133.100000000000,-212.500000000000;-125.400000000000,-188.900000000000,-

<!-- b000906 | prose | pages [28] -->
186.600000000000;-103.500000000000,-679.700000000000,-155.300000000000;-

<!-- b000907 | prose | pages [28] -->
70.6000000000000,-170.900000000000,171.900000000000;-

<!-- b000908 | prose | pages [28] -->
89.8000000000001,349.300000000000,56.3000000000000;-

<!-- b000909 | prose | pages [28] -->
103.500000000000,13.9000000000000,-157.200000000000;-108.900000000000,-

<!-- b000910 | prose | pages [28] -->
51.1000000000000,-187.100000000000;-117.200000000000,-60.7000000000000,-

<!-- b000911 | furniture | pages [28] -->


<!-- b000912 | furniture | pages [29] -->
Team # 66500

<!-- b000913 | furniture | pages [29] -->


<!-- b000914 | prose | pages [29] -->
80.2000000000000;-118.400000000000,-60.2000000000000,-52.0000000000000;];

<!-- b000915 | prose | pages [29] -->
in_put=2.592e-3*[-39.3000000000000,-

<!-- b000916 | prose | pages [29] -->
26.2000000000000,34.7000000000000,198.100000000000,364.900000000000,1063.70

<!-- b000917 | prose | pages [29] -->
000000000,839.400000000000,308.500000000000,120.300000000000,43.50000000000

<!-- b000918 | prose | pages [29] -->
00,2.69999999999999,-34.3000000000000;];

<!-- b000919 | prose | pages [29] -->
V(1,1)=12.2*5;V(1,2)=11.6*3;V(1,3)=11.2*6;

<!-- b000920 | prose | pages [29] -->
for k=1:12

<!-- b000921 | prose | pages [29] -->
Qin(k,1)=in_put(k)+deltaI(k,1);

<!-- b000922 | prose | pages [29] -->
Qout(k,1)=Qin(k,1)-deltaV(3*(k-1)+1);

<!-- b000923 | prose | pages [29] -->
Qin(k,2)=Qout(k,1)+deltaI(k,2);

<!-- b000924 | prose | pages [29] -->
Qout(k,2)=Qin(k,2)-deltaV(3*(k-1)+2);

<!-- b000925 | prose | pages [29] -->
Qin(k,3)=Qout(k,2)+deltaI(k,3);

<!-- b000926 | prose | pages [29] -->
Qout(k,3)=Qin(k,3)-deltaV(3*(k-1)+3);

<!-- b000927 | prose | pages [29] -->
Q0(k)=Qout(k,3);

<!-- b000928 | prose | pages [29] -->
V(k+1,3)=V(k,3)+deltaV(3*(k-1)+3);

<!-- b000929 | prose | pages [29] -->
V(k+1,2)=V(k,2)+deltaV(3*(k-1)+2);

<!-- b000930 | prose | pages [29] -->
V(k+1,1)=V(k,1)+deltaV(3*(k-1)+1);

<!-- b000931 | prose | pages [29] -->
end

<!-- b000932 | furniture | pages [29] -->


<!-- b000933 | prose | pages [29] -->
function [Q0,V]=ditui(deltaV)

<!-- b000934 | prose | pages [29] -->
deltaI=2.592e-

<!-- b000935 | prose | pages [29] -->
3*[35.6000000000000,97.1000000000000,92.5000000000000;35.2000000000000,55.6

<!-- b000936 | prose | pages [29] -->
000000000000,98.2000000000000;48.2000000000000,-

<!-- b000937 | prose | pages [29] -->
88.5000000000000,379.800000000000;137.200000000000,-

<!-- b000938 | prose | pages [29] -->
572,550.300000000000;315.700000000000,-

<!-- b000939 | prose | pages [29] -->
1197.80000000000,748.400000000000;601.100000000000,-

<!-- b000940 | prose | pages [29] -->
1171.40000000000,86.9000000000001;479.300000000000,82.6000000000004,-

<!-- b000941 | prose | pages [29] -->
229.700000000000;234.200000000000,1231.30000000000,77.9000000000001;129.300

<!-- b000942 | prose | pages [29] -->
000000000,765.400000000000,229.800000000000;81.3000000000000,298.0000000000

<!-- b000943 | prose | pages [29] -->
00,171.900000000000;57.8000000000000,159.100000000000,130.300000000000;42.8

<!-- b000944 | prose | pages [29] -->
000000000000,128.900000000000,132.600000000000;];

<!-- b000945 | prose | pages [29] -->
in_put=2.592e-

<!-- b000946 | prose | pages [29] -->
3*[161.500000000000,213.300000000000,477.900000000000,1149.80000000000,2206

<!-- b000947 | prose | pages [29] -->
.90000000000,2968.70000000000,2595.40000000000,1069,532.900000000000,358.90

<!-- b000948 | prose | pages [29] -->
0000000000,257.800000000000,186.100000000000;];

<!-- b000949 | prose | pages [29] -->
V(1,1)=12.2*5;V(1,2)=11.6*3;V(1,3)=11.2*6;

<!-- b000950 | prose | pages [29] -->
for k=1:12

<!-- b000951 | prose | pages [29] -->
Qin(k,1)=in_put(k)+deltaI(k,1);

<!-- b000952 | prose | pages [29] -->
Qout(k,1)=Qin(k,1)-deltaV(3*(k-1)+1);

<!-- b000953 | prose | pages [29] -->
Qin(k,2)=Qout(k,1)+deltaI(k,2);

<!-- b000954 | prose | pages [29] -->
Qout(k,2)=Qin(k,2)-deltaV(3*(k-1)+2);

<!-- b000955 | prose | pages [29] -->
Qin(k,3)=Qout(k,2)+deltaI(k,3);

<!-- b000956 | furniture | pages [29] -->


<!-- b000957 | furniture | pages [30] -->
Team # 66500

<!-- b000958 | furniture | pages [30] -->


<!-- b000959 | prose | pages [30] -->
Qout(k,3)=Qin(k,3)-deltaV(3*(k-1)+3);

<!-- b000960 | prose | pages [30] -->
Q0(k)=Qout(k,3);

<!-- b000961 | prose | pages [30] -->
V(k+1,3)=V(k,3)+deltaV(3*(k-1)+3);

<!-- b000962 | prose | pages [30] -->
V(k+1,2)=V(k,2)+deltaV(3*(k-1)+2);

<!-- b000963 | prose | pages [30] -->
V(k+1,1)=V(k,1)+deltaV(3*(k-1)+1);

<!-- b000964 | prose | pages [30] -->
end ④Constraint function

<!-- b000965 | prose | pages [30] -->
function [c,ceq]=constrain_flood(deltaV)

<!-- b000966 | prose | pages [30] -->
[Q,V]=ditui_flood(deltaV);

<!-- b000967 | prose | pages [30] -->
a=V(:,1)-20*5;

<!-- b000968 | prose | pages [30] -->
b=V(:,2)-13.2*3;

<!-- b000969 | prose | pages [30] -->
c=V(:,3)-15*6;

<!-- b000970 | prose | pages [30] -->
d=7.4*5-V(:,1);

<!-- b000971 | prose | pages [30] -->
e=4.4*5-V(:,2);

<!-- b000972 | prose | pages [30] -->
f=8*5-V(:,3);

<!-- b000973 | prose | pages [30] -->
c=[a' b' c' d' e' f'];

<!-- b000974 | prose | pages [30] -->
ceq=[];

<!-- b000975 | furniture | pages [30] -->


<!-- b000976 | prose | pages [30] -->
function [c,ceq]=constrain_drought(deltaV)

<!-- b000977 | prose | pages [30] -->
[Q,V]=ditui_drought(deltaV);

<!-- b000978 | prose | pages [30] -->
a=V(:,1)-20*5;

<!-- b000979 | prose | pages [30] -->
b=V(:,2)-13.2*3;

<!-- b000980 | prose | pages [30] -->
c=V(:,3)-15*6;

<!-- b000981 | prose | pages [30] -->
d=7.4*5-V(:,1);

<!-- b000982 | prose | pages [30] -->
e=4.4*5-V(:,2);

<!-- b000983 | prose | pages [30] -->
f=8*5-V(:,3);

<!-- b000984 | prose | pages [30] -->
c=[a' b' c' d' e' f'];

<!-- b000985 | prose | pages [30] -->
ceq=[];

<!-- b000986 | furniture | pages [30] -->


<!-- b000987 | prose | pages [30] -->
function [c,ceq]=constrain(deltaV)

<!-- b000988 | prose | pages [30] -->
[Q,V]=ditui(deltaV);

<!-- b000989 | prose | pages [30] -->
a=V(:,1)-20*5;

<!-- b000990 | prose | pages [30] -->
b=V(:,2)-13.2*3;

<!-- b000991 | prose | pages [30] -->
c=V(:,3)-15*6;

<!-- b000992 | prose | pages [30] -->
d=7.4*5-V(:,1);

<!-- b000993 | prose | pages [30] -->
e=4.4*5-V(:,2);

<!-- b000994 | prose | pages [30] -->
f=8*5-V(:,3);

<!-- b000995 | prose | pages [30] -->
c=[a' b' c' d' e' f'];

<!-- b000996 | prose | pages [30] -->
ceq=[];

<!-- b000997 | furniture | pages [30] -->


<!-- b000998 | furniture | pages [30] -->


<!-- b000999 | furniture | pages [30] -->


<!-- b001000 | furniture | pages [30] -->


<!-- b001001 | furniture | pages [31] -->
Team # 66500

<!-- b001002 | prose | pages [31] -->
2.TABLES

<!-- b001003 | furniture | pages [31] -->


<!-- b001004 | prose | pages [31] -->
Discharge in Sub Sub basin

<!-- b001005 | prose | pages [31] -->
b i

<!-- b001006 | prose | pages [31] -->
Kambompo 273

<!-- b001007 | prose | pages [31] -->
Upper Zambezi 742

<!-- b001008 | prose | pages [31] -->
Lungue Bungo 114

<!-- b001009 | prose | pages [31] -->
Luanginga 69.4

<!-- b001010 | prose | pages [31] -->
Kwando/Chobe 0

<!-- b001011 | prose | pages [31] -->
Baotse -17.6

<!-- b001012 | prose | pages [31] -->
Kariba 206

<!-- b001013 | prose | pages [31] -->
Kafue 372

<!-- b001014 | prose | pages [31] -->
Mupata 54

<!-- b001015 | prose | pages [31] -->
Luangwa 518

<!-- b001016 | prose | pages [31] -->
Tete 1193

<!-- b001017 | prose | pages [31] -->
Shire and Lake

<!-- b001018 | prose | pages [31] -->
498

<!-- b001019 | prose | pages [31] -->
M ll i

<!-- b001020 | prose | pages [31] -->
Zambezi Delta 113

<!-- b001021 | prose | pages [31] -->
Total water discharge

<!-- b001022 | prose | pages [31] -->
f 273

<!-- b001023 | prose | pages [31] -->
1015

<!-- b001024 | prose | pages [31] -->
1129

<!-- b001025 | prose | pages [31] -->
1198

<!-- b001026 | prose | pages [31] -->
1198

<!-- b001027 | prose | pages [31] -->
1180

<!-- b001028 | prose | pages [31] -->
1386

<!-- b001029 | prose | pages [31] -->
1758

<!-- b001030 | prose | pages [31] -->
1812

<!-- b001031 | prose | pages [31] -->
1330

<!-- b001032 | prose | pages [31] -->
3523

<!-- b001033 | prose | pages [31] -->
4021

<!-- b001034 | prose | pages [31] -->
4134

<!-- b001035 | prose | pages [31] -->
The annual flow Upper Zambezi Oct Nov

<!-- b001036 | prose | pages [31] -->
110.

<!-- b001037 | prose | pages [31] -->
123.

<!-- b001038 | prose | pages [31] -->
Drought

<!-- b001039 | prose | pages [31] -->
7

<!-- b001040 | prose | pages [31] -->
8

<!-- b001041 | prose | pages [31] -->
161.

<!-- b001042 | prose | pages [31] -->
213.

<!-- b001043 | prose | pages [31] -->
Average

<!-- b001044 | prose | pages [31] -->
5

<!-- b001045 | prose | pages [31] -->
3

<!-- b001046 | prose | pages [31] -->
Upper Zambezi April May

<!-- b001047 | prose | pages [31] -->
989.

<!-- b001048 | prose | pages [31] -->
458.

<!-- b001049 | prose | pages [31] -->
Drought

<!-- b001050 | prose | pages [31] -->
4

<!-- b001051 | prose | pages [31] -->
5

<!-- b001052 | prose | pages [31] -->
259

<!-- b001053 | prose | pages [31] -->
106

<!-- b001054 | prose | pages [31] -->
Average

<!-- b001055 | prose | pages [31] -->
5.4

<!-- b001056 | prose | pages [31] -->
9

<!-- b001057 | furniture | pages [31] -->


<!-- b001058 | furniture | pages [31] -->


<!-- b001059 | prose | pages [31] -->
Bungo Oct Nov

<!-- b001060 | prose | pages [31] -->
129.

<!-- b001061 | prose | pages [31] -->
139.

<!-- b001062 | prose | pages [31] -->
Drought

<!-- b001063 | prose | pages [31] -->
4

<!-- b001064 | prose | pages [31] -->
1

<!-- b001065 | prose | pages [31] -->
183.

<!-- b001066 | prose | pages [31] -->
235.

<!-- b001067 | prose | pages [31] -->
Average

<!-- b001068 | prose | pages [31] -->
6

<!-- b001069 | prose | pages [31] -->
2

<!-- b001070 | prose | pages [31] -->
Bungo April May

<!-- b001071 | prose | pages [31] -->
103

<!-- b001072 | prose | pages [31] -->
495.

<!-- b001073 | prose | pages [31] -->
Drought

<!-- b001074 | prose | pages [31] -->
8.7

<!-- b001075 | prose | pages [31] -->
9

<!-- b001076 | prose | pages [31] -->
Average 289 121

<!-- b001077 | furniture | pages [31] -->


<!-- b001078 | prose | pages [31] -->
Dec Jan Feb Mar

<!-- b001079 | prose | pages [31] -->
184.

<!-- b001080 | prose | pages [31] -->
348.

<!-- b001081 | prose | pages [31] -->
514.

<!-- b001082 | prose | pages [31] -->
121

<!-- b001083 | prose | pages [31] -->
7

<!-- b001084 | prose | pages [31] -->
1

<!-- b001085 | prose | pages [31] -->
9

<!-- b001086 | prose | pages [31] -->
3.7

<!-- b001087 | prose | pages [31] -->
477.

<!-- b001088 | prose | pages [31] -->
114

<!-- b001089 | prose | pages [31] -->
220

<!-- b001090 | prose | pages [31] -->
296

<!-- b001091 | prose | pages [31] -->
9

<!-- b001092 | prose | pages [31] -->
9.8

<!-- b001093 | prose | pages [31] -->
6.9

<!-- b001094 | prose | pages [31] -->
8.7

<!-- b001095 | prose | pages [31] -->
Jun Jul Aug Sep

<!-- b001096 | prose | pages [31] -->
270.

<!-- b001097 | prose | pages [31] -->
193.

<!-- b001098 | prose | pages [31] -->
152.

<!-- b001099 | prose | pages [31] -->
115.

<!-- b001100 | prose | pages [31] -->
3

<!-- b001101 | prose | pages [31] -->
5

<!-- b001102 | prose | pages [31] -->
7

<!-- b001103 | prose | pages [31] -->
7

<!-- b001104 | prose | pages [31] -->
532.

<!-- b001105 | prose | pages [31] -->
358.

<!-- b001106 | prose | pages [31] -->
257.

<!-- b001107 | prose | pages [31] -->
186.

<!-- b001108 | prose | pages [31] -->
9

<!-- b001109 | prose | pages [31] -->
9

<!-- b001110 | prose | pages [31] -->
8

<!-- b001111 | prose | pages [31] -->
1

<!-- b001112 | furniture | pages [31] -->


<!-- b001113 | furniture | pages [31] -->


<!-- b001114 | furniture | pages [31] -->


<!-- b001115 | furniture | pages [31] -->


<!-- b001116 | furniture | pages [31] -->


<!-- b001117 | furniture | pages [31] -->


<!-- b001118 | prose | pages [31] -->
Dec Jan Feb Mar

<!-- b001119 | prose | pages [31] -->
363.

<!-- b001120 | prose | pages [31] -->
530.

<!-- b001121 | prose | pages [31] -->
124

<!-- b001122 | prose | pages [31] -->
200

<!-- b001123 | prose | pages [31] -->
4

<!-- b001124 | prose | pages [31] -->
2

<!-- b001125 | prose | pages [31] -->
2.6

<!-- b001126 | prose | pages [31] -->
507.

<!-- b001127 | prose | pages [31] -->
123

<!-- b001128 | prose | pages [31] -->
240

<!-- b001129 | prose | pages [31] -->
334

<!-- b001130 | prose | pages [31] -->
8

<!-- b001131 | prose | pages [31] -->
5

<!-- b001132 | prose | pages [31] -->
3

<!-- b001133 | prose | pages [31] -->
2.1

<!-- b001134 | prose | pages [31] -->
Jun Jul Aug Sep

<!-- b001135 | prose | pages [31] -->
299.

<!-- b001136 | prose | pages [31] -->
173.

<!-- b001137 | prose | pages [31] -->
132.

<!-- b001138 | prose | pages [31] -->
219 2

<!-- b001139 | prose | pages [31] -->
1

<!-- b001140 | prose | pages [31] -->
7

<!-- b001141 | prose | pages [31] -->
613.

<!-- b001142 | prose | pages [31] -->
409.

<!-- b001143 | prose | pages [31] -->
293.

<!-- b001144 | prose | pages [31] -->
212.

<!-- b001145 | furniture | pages [32] -->
Team # 66500

<!-- b001146 | prose | pages [32] -->
3.1 4.5

<!-- b001147 | furniture | pages [32] -->


<!-- b001148 | furniture | pages [32] -->


<!-- b001149 | prose | pages [32] -->
Luanginga Oct Nov

<!-- b001150 | prose | pages [32] -->
140.

<!-- b001151 | prose | pages [32] -->
148.

<!-- b001152 | prose | pages [32] -->
Drought

<!-- b001153 | prose | pages [32] -->
8

<!-- b001154 | prose | pages [32] -->
4

<!-- b001155 | prose | pages [32] -->
197.

<!-- b001156 | prose | pages [32] -->
248.

<!-- b001157 | prose | pages [32] -->
Average

<!-- b001158 | prose | pages [32] -->
1

<!-- b001159 | prose | pages [32] -->
5

<!-- b001160 | prose | pages [32] -->
Luanginga April May

<!-- b001161 | prose | pages [32] -->
106

<!-- b001162 | prose | pages [32] -->
518.

<!-- b001163 | prose | pages [32] -->
Drought

<!-- b001164 | prose | pages [32] -->
8.8

<!-- b001165 | prose | pages [32] -->
7

<!-- b001166 | prose | pages [32] -->
307

<!-- b001167 | prose | pages [32] -->
130

<!-- b001168 | prose | pages [32] -->
Average

<!-- b001169 | prose | pages [32] -->
4.7

<!-- b001170 | prose | pages [32] -->
3.2

<!-- b001171 | prose | pages [32] -->
Cuando/Chobe Oct Nov

<!-- b001172 | prose | pages [32] -->
155.

<!-- b001173 | prose | pages [32] -->
161.

<!-- b001174 | prose | pages [32] -->
Drought

<!-- b001175 | prose | pages [32] -->
7

<!-- b001176 | prose | pages [32] -->
8

<!-- b001177 | prose | pages [32] -->
228.

<!-- b001178 | prose | pages [32] -->
276.

<!-- b001179 | prose | pages [32] -->
Average

<!-- b001180 | prose | pages [32] -->
5

<!-- b001181 | prose | pages [32] -->
6

<!-- b001182 | prose | pages [32] -->
Cuando/Chobe April May

<!-- b001183 | prose | pages [32] -->
108 533. Drought 4.9 8

<!-- b001184 | prose | pages [32] -->
310

<!-- b001185 | prose | pages [32] -->
133

<!-- b001186 | prose | pages [32] -->
Average

<!-- b001187 | prose | pages [32] -->
9.8

<!-- b001188 | prose | pages [32] -->
7

<!-- b001189 | furniture | pages [32] -->


<!-- b001190 | furniture | pages [32] -->


<!-- b001191 | prose | pages [32] -->
Baroste Oct Nov

<!-- b001192 | prose | pages [32] -->
266.

<!-- b001193 | prose | pages [32] -->
259.

<!-- b001194 | prose | pages [32] -->
Drought

<!-- b001195 | prose | pages [32] -->
6

<!-- b001196 | prose | pages [32] -->
2

<!-- b001197 | prose | pages [32] -->
294.

<!-- b001198 | prose | pages [32] -->
304.

<!-- b001199 | prose | pages [32] -->
Average

<!-- b001200 | prose | pages [32] -->
2

<!-- b001201 | prose | pages [32] -->
1

<!-- b001202 | prose | pages [32] -->
Baroste April May

<!-- b001203 | prose | pages [32] -->
104

<!-- b001204 | prose | pages [32] -->
101

<!-- b001205 | prose | pages [32] -->
Drought

<!-- b001206 | prose | pages [32] -->
7.9

<!-- b001207 | prose | pages [32] -->
8

<!-- b001208 | prose | pages [32] -->
315

<!-- b001209 | prose | pages [32] -->
253

<!-- b001210 | prose | pages [32] -->
Average

<!-- b001211 | prose | pages [32] -->
7.3

<!-- b001212 | prose | pages [32] -->
4.5

<!-- b001213 | furniture | pages [32] -->


<!-- b001214 | furniture | pages [32] -->


<!-- b001215 | prose | pages [32] -->
Kariba

<!-- b001216 | prose | pages [32] -->
Oct Nov （regulated）

<!-- b001217 | prose | pages [32] -->
199.

<!-- b001218 | prose | pages [32] -->
231.

<!-- b001219 | prose | pages [32] -->
Drought

<!-- b001220 | prose | pages [32] -->
7

<!-- b001221 | prose | pages [32] -->
8

<!-- b001222 | prose | pages [32] -->
875.

<!-- b001223 | prose | pages [32] -->
104

<!-- b001224 | prose | pages [32] -->
Average

<!-- b001225 | prose | pages [32] -->
9

<!-- b001226 | prose | pages [32] -->
7.9

<!-- b001227 | furniture | pages [32] -->


<!-- b001228 | furniture | pages [32] -->


<!-- b001229 | prose | pages [32] -->
2 4 7 7

<!-- b001230 | furniture | pages [32] -->


<!-- b001231 | furniture | pages [32] -->


<!-- b001232 | furniture | pages [32] -->


<!-- b001233 | furniture | pages [32] -->


<!-- b001234 | furniture | pages [32] -->


<!-- b001235 | furniture | pages [32] -->


<!-- b001236 | prose | pages [32] -->
Dec Jan Feb Mar

<!-- b001237 | prose | pages [32] -->
209.

<!-- b001238 | prose | pages [32] -->
372.

<!-- b001239 | prose | pages [32] -->
539.

<!-- b001240 | prose | pages [32] -->
126

<!-- b001241 | prose | pages [32] -->
3

<!-- b001242 | prose | pages [32] -->
7

<!-- b001243 | prose | pages [32] -->
5

<!-- b001244 | prose | pages [32] -->
0.2

<!-- b001245 | prose | pages [32] -->
526.

<!-- b001246 | prose | pages [32] -->
128

<!-- b001247 | prose | pages [32] -->
252

<!-- b001248 | prose | pages [32] -->
356

<!-- b001249 | prose | pages [32] -->
1

<!-- b001250 | prose | pages [32] -->
7

<!-- b001251 | prose | pages [32] -->
2.6

<!-- b001252 | prose | pages [32] -->
9.8

<!-- b001253 | prose | pages [32] -->
Jun Jul Aug Sep

<!-- b001254 | prose | pages [32] -->
316.

<!-- b001255 | prose | pages [32] -->
234.

<!-- b001256 | prose | pages [32] -->
185.

<!-- b001257 | prose | pages [32] -->
147.

<!-- b001258 | prose | pages [32] -->
8

<!-- b001259 | prose | pages [32] -->
6

<!-- b001260 | prose | pages [32] -->
5

<!-- b001261 | prose | pages [32] -->
3

<!-- b001262 | prose | pages [32] -->
662.

<!-- b001263 | prose | pages [32] -->
440.

<!-- b001264 | prose | pages [32] -->
315.

<!-- b001265 | prose | pages [32] -->
228.

<!-- b001266 | prose | pages [32] -->
2

<!-- b001267 | prose | pages [32] -->
2

<!-- b001268 | prose | pages [32] -->
6

<!-- b001269 | prose | pages [32] -->
9

<!-- b001270 | prose | pages [32] -->
Dec Jan Feb Mar

<!-- b001271 | prose | pages [32] -->
223.

<!-- b001272 | prose | pages [32] -->
556.

<!-- b001273 | prose | pages [32] -->
127

<!-- b001274 | prose | pages [32] -->
388 2

<!-- b001275 | prose | pages [32] -->
7

<!-- b001276 | prose | pages [32] -->
9.3

<!-- b001277 | prose | pages [32] -->
553.

<!-- b001278 | prose | pages [32] -->
131

<!-- b001279 | prose | pages [32] -->
255

<!-- b001280 | prose | pages [32] -->
360

<!-- b001281 | prose | pages [32] -->
4

<!-- b001282 | prose | pages [32] -->
6.8

<!-- b001283 | prose | pages [32] -->
5.6

<!-- b001284 | prose | pages [32] -->
4.4

<!-- b001285 | prose | pages [32] -->
Jun Jul Aug Sep

<!-- b001286 | prose | pages [32] -->
331.

<!-- b001287 | prose | pages [32] -->
248.

<!-- b001288 | prose | pages [32] -->
198.

<!-- b001289 | prose | pages [32] -->
162. 7 5 4 2

<!-- b001290 | prose | pages [32] -->
695.

<!-- b001291 | prose | pages [32] -->
475.

<!-- b001292 | prose | pages [32] -->
350.

<!-- b001293 | prose | pages [32] -->
262.

<!-- b001294 | prose | pages [32] -->
2

<!-- b001295 | prose | pages [32] -->
5

<!-- b001296 | prose | pages [32] -->
9

<!-- b001297 | prose | pages [32] -->
9

<!-- b001298 | furniture | pages [32] -->


<!-- b001299 | furniture | pages [32] -->


<!-- b001300 | furniture | pages [32] -->


<!-- b001301 | furniture | pages [32] -->


<!-- b001302 | furniture | pages [32] -->


<!-- b001303 | furniture | pages [32] -->


<!-- b001304 | prose | pages [32] -->
Dec Jan Feb Mar

<!-- b001305 | prose | pages [32] -->
275.

<!-- b001306 | prose | pages [32] -->
389.

<!-- b001307 | prose | pages [32] -->
500.

<!-- b001308 | prose | pages [32] -->
730.

<!-- b001309 | prose | pages [32] -->
3

<!-- b001310 | prose | pages [32] -->
6

<!-- b001311 | prose | pages [32] -->
6

<!-- b001312 | prose | pages [32] -->
5

<!-- b001313 | prose | pages [32] -->
437.

<!-- b001314 | prose | pages [32] -->
132

<!-- b001315 | prose | pages [32] -->
239

<!-- b001316 | prose | pages [32] -->
715 6

<!-- b001317 | prose | pages [32] -->
4.8

<!-- b001318 | prose | pages [32] -->
8.4

<!-- b001319 | prose | pages [32] -->
Jun Jul Aug Sep

<!-- b001320 | prose | pages [32] -->
480.

<!-- b001321 | prose | pages [32] -->
333.

<!-- b001322 | prose | pages [32] -->
274.

<!-- b001323 | prose | pages [32] -->
237.

<!-- b001324 | prose | pages [32] -->
7

<!-- b001325 | prose | pages [32] -->
5

<!-- b001326 | prose | pages [32] -->
8

<!-- b001327 | prose | pages [32] -->
1

<!-- b001328 | prose | pages [32] -->
142

<!-- b001329 | prose | pages [32] -->
738.

<!-- b001330 | prose | pages [32] -->
474.

<!-- b001331 | prose | pages [32] -->
357.

<!-- b001332 | prose | pages [32] -->
7.6

<!-- b001333 | prose | pages [32] -->
2

<!-- b001334 | prose | pages [32] -->
7

<!-- b001335 | prose | pages [32] -->
8

<!-- b001336 | furniture | pages [32] -->


<!-- b001337 | furniture | pages [32] -->


<!-- b001338 | furniture | pages [32] -->


<!-- b001339 | furniture | pages [32] -->


<!-- b001340 | furniture | pages [32] -->


<!-- b001341 | furniture | pages [32] -->


<!-- b001342 | prose | pages [32] -->
Dec Jan Feb Mar

<!-- b001343 | prose | pages [32] -->
302.

<!-- b001344 | prose | pages [32] -->
927.

<!-- b001345 | prose | pages [32] -->
913.

<!-- b001346 | prose | pages [32] -->
901.

<!-- b001347 | prose | pages [32] -->
9

<!-- b001348 | prose | pages [32] -->
2

<!-- b001349 | prose | pages [32] -->
2

<!-- b001350 | prose | pages [32] -->
4

<!-- b001351 | prose | pages [32] -->
136

<!-- b001352 | prose | pages [32] -->
243

<!-- b001353 | prose | pages [32] -->
104

<!-- b001354 | prose | pages [32] -->
905.

<!-- b001355 | prose | pages [32] -->
4.4

<!-- b001356 | prose | pages [32] -->
6.8

<!-- b001357 | prose | pages [32] -->
2.2

<!-- b001358 | prose | pages [32] -->
8

<!-- b001359 | furniture | pages [33] -->
Team # 66500

<!-- b001360 | prose | pages [33] -->
Kariba

<!-- b001361 | prose | pages [33] -->
April May （regulated）

<!-- b001362 | prose | pages [33] -->
897.

<!-- b001363 | prose | pages [33] -->
893.

<!-- b001364 | prose | pages [33] -->
Drought

<!-- b001365 | prose | pages [33] -->
6

<!-- b001366 | prose | pages [33] -->
8

<!-- b001367 | prose | pages [33] -->
116

<!-- b001368 | prose | pages [33] -->
136

<!-- b001369 | prose | pages [33] -->
Average

<!-- b001370 | prose | pages [33] -->
2.7

<!-- b001371 | prose | pages [33] -->
8.8

<!-- b001372 | furniture | pages [33] -->


<!-- b001373 | furniture | pages [33] -->


<!-- b001374 | prose | pages [33] -->
Kariba

<!-- b001375 | prose | pages [33] -->
Oct Nov （unregulated）

<!-- b001376 | prose | pages [33] -->
292. Drought 200

<!-- b001377 | prose | pages [33] -->
6

<!-- b001378 | prose | pages [33] -->
386.

<!-- b001379 | prose | pages [33] -->
402.

<!-- b001380 | prose | pages [33] -->
Average

<!-- b001381 | prose | pages [33] -->
7

<!-- b001382 | prose | pages [33] -->
3

<!-- b001383 | prose | pages [33] -->
Kariba April May （unregulated）

<!-- b001384 | prose | pages [33] -->
136

<!-- b001385 | prose | pages [33] -->
122

<!-- b001386 | prose | pages [33] -->
Drought

<!-- b001387 | prose | pages [33] -->
9.8

<!-- b001388 | prose | pages [33] -->
4.3

<!-- b001389 | prose | pages [33] -->
292

<!-- b001390 | prose | pages [33] -->
261

<!-- b001391 | prose | pages [33] -->
Average

<!-- b001392 | prose | pages [33] -->
7.6

<!-- b001393 | prose | pages [33] -->
2.4

<!-- b001394 | furniture | pages [33] -->


<!-- b001395 | furniture | pages [33] -->


<!-- b001396 | prose | pages [33] -->
Mupata

<!-- b001397 | prose | pages [33] -->
Oct Nov （regulated）

<!-- b001398 | prose | pages [33] -->
109

<!-- b001399 | prose | pages [33] -->
109

<!-- b001400 | prose | pages [33] -->
Drought

<!-- b001401 | prose | pages [33] -->
3.3

<!-- b001402 | prose | pages [33] -->
5.6

<!-- b001403 | prose | pages [33] -->
114

<!-- b001404 | prose | pages [33] -->
129

<!-- b001405 | prose | pages [33] -->
Average

<!-- b001406 | prose | pages [33] -->
9.3

<!-- b001407 | prose | pages [33] -->
6.6

<!-- b001408 | prose | pages [33] -->
Mupata

<!-- b001409 | prose | pages [33] -->
April May （regulated）

<!-- b001410 | prose | pages [33] -->
110

<!-- b001411 | prose | pages [33] -->
110

<!-- b001412 | prose | pages [33] -->
Drought

<!-- b001413 | prose | pages [33] -->
2.9

<!-- b001414 | prose | pages [33] -->
1.3

<!-- b001415 | prose | pages [33] -->
173

<!-- b001416 | prose | pages [33] -->
188

<!-- b001417 | prose | pages [33] -->
Average

<!-- b001418 | prose | pages [33] -->
8.3

<!-- b001419 | prose | pages [33] -->
8.8

<!-- b001420 | furniture | pages [33] -->


<!-- b001421 | furniture | pages [33] -->


<!-- b001422 | prose | pages [33] -->
Mupata(unregulat

<!-- b001423 | prose | pages [33] -->
Oct Nov ed）

<!-- b001424 | prose | pages [33] -->
254.

<!-- b001425 | prose | pages [33] -->
340.

<!-- b001426 | prose | pages [33] -->
Drought

<!-- b001427 | prose | pages [33] -->
1

<!-- b001428 | prose | pages [33] -->
1

<!-- b001429 | prose | pages [33] -->
550. Average

<!-- b001430 | prose | pages [33] -->
527 6

<!-- b001431 | prose | pages [33] -->
Mupata(unregulat

<!-- b001432 | prose | pages [33] -->
April May ed）

<!-- b001433 | prose | pages [33] -->
Drought 161 144

<!-- b001434 | furniture | pages [33] -->


<!-- b001435 | furniture | pages [33] -->


<!-- b001436 | prose | pages [33] -->
Jun Jul Aug Sep

<!-- b001437 | prose | pages [33] -->
891.

<!-- b001438 | prose | pages [33] -->
893.

<!-- b001439 | prose | pages [33] -->
897.

<!-- b001440 | prose | pages [33] -->
902.

<!-- b001441 | prose | pages [33] -->
8

<!-- b001442 | prose | pages [33] -->
2

<!-- b001443 | prose | pages [33] -->
5

<!-- b001444 | prose | pages [33] -->
1

<!-- b001445 | prose | pages [33] -->
111

<!-- b001446 | prose | pages [33] -->
122

<!-- b001447 | prose | pages [33] -->
107

<!-- b001448 | prose | pages [33] -->
981.

<!-- b001449 | prose | pages [33] -->
1.2

<!-- b001450 | prose | pages [33] -->
8.6

<!-- b001451 | prose | pages [33] -->
5.5

<!-- b001452 | prose | pages [33] -->
9

<!-- b001453 | furniture | pages [33] -->


<!-- b001454 | furniture | pages [33] -->


<!-- b001455 | furniture | pages [33] -->


<!-- b001456 | furniture | pages [33] -->


<!-- b001457 | furniture | pages [33] -->


<!-- b001458 | furniture | pages [33] -->


<!-- b001459 | prose | pages [33] -->
Dec Jan Feb Mar

<!-- b001460 | prose | pages [33] -->
215.

<!-- b001461 | prose | pages [33] -->
327.

<!-- b001462 | prose | pages [33] -->
725. 464

<!-- b001463 | prose | pages [33] -->
2

<!-- b001464 | prose | pages [33] -->
1

<!-- b001465 | prose | pages [33] -->
2

<!-- b001466 | prose | pages [33] -->
817.

<!-- b001467 | prose | pages [33] -->
126

<!-- b001468 | prose | pages [33] -->
207

<!-- b001469 | prose | pages [33] -->
248

<!-- b001470 | prose | pages [33] -->
4

<!-- b001471 | prose | pages [33] -->
5.3

<!-- b001472 | prose | pages [33] -->
3.2

<!-- b001473 | prose | pages [33] -->
5.3

<!-- b001474 | prose | pages [33] -->
Jun Jul Aug Sep

<!-- b001475 | prose | pages [33] -->
473.

<!-- b001476 | prose | pages [33] -->
296.

<!-- b001477 | prose | pages [33] -->
344.

<!-- b001478 | prose | pages [33] -->
335.

<!-- b001479 | prose | pages [33] -->
5

<!-- b001480 | prose | pages [33] -->
4

<!-- b001481 | prose | pages [33] -->
6

<!-- b001482 | prose | pages [33] -->
1

<!-- b001483 | prose | pages [33] -->
165

<!-- b001484 | prose | pages [33] -->
910.

<!-- b001485 | prose | pages [33] -->
490. 605

<!-- b001486 | prose | pages [33] -->
7.4

<!-- b001487 | prose | pages [33] -->
1

<!-- b001488 | prose | pages [33] -->
4

<!-- b001489 | furniture | pages [33] -->


<!-- b001490 | furniture | pages [33] -->


<!-- b001491 | furniture | pages [33] -->


<!-- b001492 | furniture | pages [33] -->


<!-- b001493 | furniture | pages [33] -->


<!-- b001494 | furniture | pages [33] -->


<!-- b001495 | prose | pages [33] -->
Dec Jan Feb Mar

<!-- b001496 | prose | pages [33] -->
110

<!-- b001497 | prose | pages [33] -->
113

<!-- b001498 | prose | pages [33] -->
117

<!-- b001499 | prose | pages [33] -->
117

<!-- b001500 | prose | pages [33] -->
9.2

<!-- b001501 | prose | pages [33] -->
6.9

<!-- b001502 | prose | pages [33] -->
9.5

<!-- b001503 | prose | pages [33] -->
9.2

<!-- b001504 | prose | pages [33] -->
161

<!-- b001505 | prose | pages [33] -->
274

<!-- b001506 | prose | pages [33] -->
141

<!-- b001507 | prose | pages [33] -->
145

<!-- b001508 | prose | pages [33] -->
9.7

<!-- b001509 | prose | pages [33] -->
1.1

<!-- b001510 | prose | pages [33] -->
9

<!-- b001511 | prose | pages [33] -->
5

<!-- b001512 | prose | pages [33] -->
Jun Jul Aug Sep

<!-- b001513 | prose | pages [33] -->
131

<!-- b001514 | prose | pages [33] -->
114

<!-- b001515 | prose | pages [33] -->
668.

<!-- b001516 | prose | pages [33] -->
194.

<!-- b001517 | prose | pages [33] -->
4.8

<!-- b001518 | prose | pages [33] -->
7

<!-- b001519 | prose | pages [33] -->
1

<!-- b001520 | prose | pages [33] -->
7

<!-- b001521 | prose | pages [33] -->
171

<!-- b001522 | prose | pages [33] -->
163

<!-- b001523 | prose | pages [33] -->
139

<!-- b001524 | prose | pages [33] -->
127

<!-- b001525 | prose | pages [33] -->
4.3

<!-- b001526 | prose | pages [33] -->
2.6

<!-- b001527 | prose | pages [33] -->
2.1

<!-- b001528 | prose | pages [33] -->
7.7

<!-- b001529 | furniture | pages [33] -->


<!-- b001530 | furniture | pages [33] -->


<!-- b001531 | furniture | pages [33] -->


<!-- b001532 | furniture | pages [33] -->


<!-- b001533 | furniture | pages [33] -->


<!-- b001534 | furniture | pages [33] -->


<!-- b001535 | prose | pages [33] -->
Dec Jan Feb Mar

<!-- b001536 | prose | pages [33] -->
440.

<!-- b001537 | prose | pages [33] -->
643.

<!-- b001538 | prose | pages [33] -->
967.

<!-- b001539 | prose | pages [33] -->
282

<!-- b001540 | prose | pages [33] -->
5

<!-- b001541 | prose | pages [33] -->
6

<!-- b001542 | prose | pages [33] -->
9

<!-- b001543 | prose | pages [33] -->
103

<!-- b001544 | prose | pages [33] -->
163

<!-- b001545 | prose | pages [33] -->
263

<!-- b001546 | prose | pages [33] -->
321

<!-- b001547 | prose | pages [33] -->
1.2

<!-- b001548 | prose | pages [33] -->
9.8

<!-- b001549 | prose | pages [33] -->
5.1

<!-- b001550 | prose | pages [33] -->
1.8

<!-- b001551 | prose | pages [33] -->
Jun Jul Aug Sep

<!-- b001552 | prose | pages [33] -->
614.

<!-- b001553 | prose | pages [33] -->
390.

<!-- b001554 | prose | pages [33] -->
409.

<!-- b001555 | prose | pages [33] -->
382

<!-- b001556 | furniture | pages [34] -->
Team # 66500

<!-- b001557 | prose | pages [34] -->
3.2 1.6

<!-- b001558 | prose | pages [34] -->
370

<!-- b001559 | prose | pages [34] -->
327

<!-- b001560 | prose | pages [34] -->
Average

<!-- b001561 | prose | pages [34] -->
5

<!-- b001562 | prose | pages [34] -->
5.7

<!-- b001563 | furniture | pages [34] -->


<!-- b001564 | furniture | pages [34] -->


<!-- b001565 | prose | pages [34] -->
Kabompo Oct Nov

<!-- b001566 | prose | pages [34] -->
Drought 73.4 80.5

<!-- b001567 | prose | pages [34] -->
102. Average 82

<!-- b001568 | prose | pages [34] -->
8

<!-- b001569 | prose | pages [34] -->
Kabompo April May

<!-- b001570 | prose | pages [34] -->
230.

<!-- b001571 | prose | pages [34] -->
125.

<!-- b001572 | prose | pages [34] -->
Drought

<!-- b001573 | prose | pages [34] -->
9

<!-- b001574 | prose | pages [34] -->
5

<!-- b001575 | prose | pages [34] -->
558. Average

<!-- b001576 | prose | pages [34] -->
270 4

<!-- b001577 | furniture | pages [34] -->


<!-- b001578 | furniture | pages [34] -->


<!-- b001579 | prose | pages [34] -->
Upper Zambezi Oct Nov

<!-- b001580 | prose | pages [34] -->
Drought 37.3 43.3

<!-- b001581 | prose | pages [34] -->
110. Average 79.5 5

<!-- b001582 | prose | pages [34] -->
Upper Zambezi April May

<!-- b001583 | prose | pages [34] -->
758. Drought

<!-- b001584 | prose | pages [34] -->
333 5

<!-- b001585 | prose | pages [34] -->
203 Average

<!-- b001586 | prose | pages [34] -->
799 7

<!-- b001587 | prose | pages [34] -->
3.GRAPH

<!-- b001588 | furniture | pages [34] -->


<!-- b001589 | furniture | pages [34] -->


<!-- b001590 | prose | pages [34] -->
6 8 2

<!-- b001591 | prose | pages [34] -->
217

<!-- b001592 | prose | pages [34] -->
133

<!-- b001593 | prose | pages [34] -->
929.

<!-- b001594 | prose | pages [34] -->
726.

<!-- b001595 | prose | pages [34] -->
4.1

<!-- b001596 | prose | pages [34] -->
1.9

<!-- b001597 | prose | pages [34] -->
9

<!-- b001598 | prose | pages [34] -->
3

<!-- b001599 | furniture | pages [34] -->


<!-- b001600 | furniture | pages [34] -->


<!-- b001601 | furniture | pages [34] -->


<!-- b001602 | furniture | pages [34] -->


<!-- b001603 | furniture | pages [34] -->


<!-- b001604 | furniture | pages [34] -->


<!-- b001605 | prose | pages [34] -->
Dec Jan Feb Mar

<!-- b001606 | prose | pages [34] -->
104.

<!-- b001607 | prose | pages [34] -->
190.

<!-- b001608 | prose | pages [34] -->
204.

<!-- b001609 | prose | pages [34] -->
339.

<!-- b001610 | prose | pages [34] -->
2

<!-- b001611 | prose | pages [34] -->
6

<!-- b001612 | prose | pages [34] -->
8

<!-- b001613 | prose | pages [34] -->
8

<!-- b001614 | prose | pages [34] -->
203.

<!-- b001615 | prose | pages [34] -->
354.

<!-- b001616 | prose | pages [34] -->
532.

<!-- b001617 | prose | pages [34] -->
664.

<!-- b001618 | prose | pages [34] -->
3

<!-- b001619 | prose | pages [34] -->
5

<!-- b001620 | prose | pages [34] -->
9

<!-- b001621 | prose | pages [34] -->
6

<!-- b001622 | prose | pages [34] -->
Jun Jul Aug Sep

<!-- b001623 | prose | pages [34] -->
90 80.5 72.2 60.4

<!-- b001624 | prose | pages [34] -->
166.

<!-- b001625 | prose | pages [34] -->
137.

<!-- b001626 | prose | pages [34] -->
113.

<!-- b001627 | prose | pages [34] -->
89.8

<!-- b001628 | prose | pages [34] -->
7

<!-- b001629 | prose | pages [34] -->
3

<!-- b001630 | prose | pages [34] -->
8

<!-- b001631 | furniture | pages [34] -->


<!-- b001632 | furniture | pages [34] -->


<!-- b001633 | furniture | pages [34] -->


<!-- b001634 | furniture | pages [34] -->


<!-- b001635 | furniture | pages [34] -->


<!-- b001636 | furniture | pages [34] -->


<!-- b001637 | prose | pages [34] -->
Dec Jan Feb Mar

<!-- b001638 | prose | pages [34] -->
157.

<!-- b001639 | prose | pages [34] -->
310.

<!-- b001640 | prose | pages [34] -->
873.

<!-- b001641 | prose | pages [34] -->
80.5

<!-- b001642 | prose | pages [34] -->
5

<!-- b001643 | prose | pages [34] -->
1

<!-- b001644 | prose | pages [34] -->
9

<!-- b001645 | prose | pages [34] -->
274.

<!-- b001646 | prose | pages [34] -->
795.

<!-- b001647 | prose | pages [34] -->
167 230 6 3 4 4.1

<!-- b001648 | prose | pages [34] -->
Jun Jul Aug Sep

<!-- b001649 | prose | pages [34] -->
180.

<!-- b001650 | prose | pages [34] -->
113 80.5 55.3 3

<!-- b001651 | prose | pages [34] -->
366.

<!-- b001652 | prose | pages [34] -->
221.

<!-- b001653 | prose | pages [34] -->
144 96.3

<!-- b001654 | prose | pages [34] -->
2

<!-- b001655 | prose | pages [34] -->
6

<!-- b001656 | furniture | pages [34] -->


<!-- b001657 | furniture | pages [35] -->
Team # 66500

<!-- b001658 | furniture | pages [35] -->


<!-- b001659 | furniture | pages [35] -->


<!-- b001660 | furniture | pages [35] -->


<!-- b001661 | furniture | pages [35] -->


<!-- b001662 | furniture | pages [35] -->

