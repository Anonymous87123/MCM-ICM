# P-A-2017-65448-6ed1d510

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
65448

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
T2

<!-- b000007 | prose | pages [1] -->
F1

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
Problem Chosen

<!-- b000010 | prose | pages [1] -->
T3

<!-- b000011 | prose | pages [1] -->
T4

<!-- b000012 | prose | pages [1] -->
F3

<!-- b000013 | title | pages [1] -->
A

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | heading | pages [1] -->
2017 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000016 | prose | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000017 | heading | pages [1] -->
Abstract

<!-- b000018 | prose | pages [1] -->
The Kariba Dam on the Zambezi River is confronted with foundation errosion and control limitation cur- rently, so a strategy to maintain water management on the Zambezi River is of great value for the whole Zambezi basin. Based on the detailed data provided by World Bank, we conduct the assessment of three op- tions (repairing the dam, rebuilding the dam or replacing the dam with several smaller dams along the river) and provide a reasonable and detailed model to construct a new dam system with some emergency strategies.

<!-- b000019 | prose | pages [1] -->
To begin with, a brief assessment report with potential costs and beneﬁts is offered according to abundant references and reliable data. The evaluation of repairing the Kariba Dam is completed refering to the Kariba Dam Rehabilitation Project in the charge of World Bank, while the assessment of rebuilding the dam is realized following the actual capital investment expenditure of the Stage 1 of the Kariba Project. And the assessment of replacing the dam is carefully estimated according to the model to construct the new dam system.

<!-- b000020 | prose | pages [1] -->
Then, we concentrate on the establishment of the model for new dam system. Firstly, a Hydrodynamic Model (HM) of the Zambezi River is established in order to estimate the ﬂowing and depth situation of the river. The model is constructed based on ﬂow conservation and energy conservation, which separately producing continuity equation and energy conservation equation, taking the normal water cycles and on-way resistance into account. Moreover, we obtain the numerical solution of the Hydrodynamic Model with Mathematica, and get the approximate current velocity curve and river depth curve along the river.

<!-- b000021 | prose | pages [1] -->
Secondly, the site selection and number conﬁrmation of the new dams is realized according to the ﬂowing and depth situation estimated by HM, geological data and hydrological data. The indexes for evaluation are determined after consulting professional literatures, and Grey Relation Grade Analysis is utilized in the selection among candidate sites so that all the indexes can be considered comprehensively and objectively.

<!-- b000022 | prose | pages [1] -->
Thirdly, a Difference Model (DM) of the Zambezi River with a dam system is established to provide suf- ﬁcient details for the conﬁrmation of dam construction and modulating strategies. We separate the river into several segments by the dams. A difference approximation of HM is applied to describe each segment of the river. A hydraulic emprical formula is utilized to determine the discharges of the dam. In this way, the re- currence formulas can be obtained to easily determine the runoff and river depth along the river with given environmental and initial conditions.

<!-- b000023 | prose | pages [1] -->
Fourthly, the type of each dam is conﬁrmed with corrected DM, with the overall water management capa- bilities, protection and water management options for Lake Kariba evaluated and special topograph consid- ered. Considering the loss of energy in collision, tributaries and the runoff variation with rainfall at headstram and tributaries, DM is corrected to adapt to the reality. With the results calculated by corrected DM, the type of each dam is conﬁrmed balancing the safety and costs. Each type of dam has three gears of discharges, which increases the water management options.

<!-- b000024 | prose | pages [1] -->
Finally, the strategies to handle such emergency water ﬂow situations as ﬂooding and drought are designed with the new dam system established above. When solving a known catastrophe, the exhaustive method is utilized to rule out the best strategies which realized by the gear variation of the dam. It is validated that the new dam system can handle most extreme conditions and the method we adopted to establish the strategy is of low sensibility considering reasonable errors.

<!-- b000025 | furniture | pages [2] -->
Team # 65448

<!-- b000026 | furniture | pages [2] -->
Page 1 of 25

<!-- b000027 | prose | pages [2] -->
A Multi-Dam System Design for Zambezi River

<!-- b000028 | prose | pages [2] -->
January 24, 2017

<!-- b000029 | heading | pages [2] -->
Contents

<!-- b000030 | contents | pages [2] -->
1

<!-- b000031 | contents | pages [2] -->
Assessment Report of Three Options

<!-- b000032 | contents | pages [2] -->
1

<!-- b000033 | contents | pages [2] -->
Repairing the Existing Kariba Dam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
1.1

<!-- b000035 | contents | pages [2] -->
1

<!-- b000036 | contents | pages [2] -->
Institutional Project Support (estimated cost US$69.6 million) . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
1.1.1

<!-- b000038 | contents | pages [2] -->
1

<!-- b000039 | contents | pages [2] -->
Plunge Pool Reshaping (estimated cost US$100.0 million) . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
1.1.2

<!-- b000041 | contents | pages [2] -->
1

<!-- b000042 | contents | pages [2] -->
Spillway Refurbishment (estimated cost US$124.6 million) . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
1.1.3

<!-- b000044 | contents | pages [2] -->
1

<!-- b000045 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
1.1.4

<!-- b000047 | contents | pages [2] -->
Beneﬁts

<!-- b000048 | contents | pages [2] -->
1

<!-- b000049 | contents | pages [2] -->
Rebuilding the Existing Kariba Dam . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
1.2

<!-- b000051 | contents | pages [2] -->
1

<!-- b000052 | contents | pages [2] -->
Removing the Kariba Dam & Replacing It with A Series of Ten to Twenty Smaller Dams

<!-- b000053 | contents | pages [2] -->
1.3

<!-- b000054 | contents | pages [2] -->
Along the Zambezi River . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
2

<!-- b000056 | heading | pages [2] -->
Introduction

<!-- b000057 | prose | pages [2] -->
2

<!-- b000058 | prose | pages [2] -->
2 Restatement of the problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 2 Our Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000059 | prose | pages [2] -->
3

<!-- b000060 | heading | pages [2] -->
General Assumption

<!-- b000061 | prose | pages [2] -->
4

<!-- b000062 | heading | pages [2] -->
Notations

<!-- b000063 | prose | pages [2] -->
5

<!-- b000064 | heading | pages [2] -->
The Model

<!-- b000065 | prose | pages [2] -->
3

<!-- b000066 | prose | pages [2] -->
4

<!-- b000067 | prose | pages [2] -->
4

<!-- b000068 | prose | pages [2] -->
5 Hydrodynamic Model of the Zambezi River . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 5 Continuity Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.1 5 Energy Conservation Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.2 6 Boundary Condition and Initial Condition 5.1.3 . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | prose | pages [2] -->
6 Calculation of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.4 7 Selection System of the Dam Site . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 8 Evaluation indexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 9 Candidate Site . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.2 9 Grey Relation Grade Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 10 Difference Model of the Dam System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 11 Equations in the River (Without the Dam) . . . . . . . . . . . . . . . . . . . . . . 5.3.1 12 Equations in the Dam Region . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.2 13 Recurrence Formulas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.3 13 Dam Construction & Manipulating System . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 14 Conﬁrm the Parameters of Different Dam Types . . . . . . . . . . . . . . . . . . 5.4.1 14 Conﬁrm the Type Selection of Each Dam 5.4.2 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | prose | pages [2] -->
14 Evaluate the Protection & Water Management Options for Lake Kariba . . . . . 5.4.3 17 Strategies to Handle Emergency Water Flow Situations . . . . . . . . . . . . . . 5.4.4

<!-- b000071 | prose | pages [2] -->
6

<!-- b000072 | heading | pages [2] -->
Testing the model

<!-- b000073 | prose | pages [2] -->
17

<!-- b000074 | prose | pages [2] -->
19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Error analysis 19 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 20 Sensitivity Analysis for Hi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.1 20 Sensitivity Analysis for hi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.2 20

<!-- b000075 | prose | pages [3] -->
Sensitivity Analysis for Qi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.3 21 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 21 Strengths and weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3.1 21 Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3.2

<!-- b000076 | heading | pages [3] -->
Appendices

<!-- b000077 | prose | pages [3] -->
22

<!-- b000078 | prose | pages [3] -->
23

<!-- b000079 | prose | pages [3] -->
0 0

<!-- b000080 | furniture | pages [4] -->
Team # 65448

<!-- b000081 | furniture | pages [4] -->
Page 1 of 25

<!-- b000082 | prose | pages [4] -->
1 Assessment Report of Three Options

<!-- b000083 | prose | pages [4] -->
1.1 Repairing the Existing Kariba Dam

<!-- b000084 | prose | pages [4] -->
1 At present, the foundation of the Kariba Dam is gradually undermined by scouring and erosion of water, so that operations are limited to only three of the six, non-adjacent gates. The Kariba Dam is also suffering frequent maintenance operations and potential limitations on the operational control of the reservoir. Therefore, plunge pool reshaping and spillway refurbishment are necessities. What is more, institutional project support are also signiﬁcant to ensure the project running smoothly.

<!-- b000085 | prose | pages [4] -->
1.1.1 Institutional Project Support (estimated cost US$69.6 million)

<!-- b000086 | prose | pages [4] -->
1 Institutional project support mainly provides overall management, supervision, professional consultant, comprehensive assessment and risk evaluation for the project.

<!-- b000087 | prose | pages [4] -->
1.1.2 Plunge Pool Reshaping (estimated cost US$100.0 million)

<!-- b000088 | prose | pages [4] -->
1 Financing in the component is primarily utilized for goods, works and consultants services, which is constituted with four parts: a. Plunge Pool Reshaping Civil Works Contract: The measures are required to reshape the plunge pool through excavation of the downstream face and north and south bank sides of the pool; b. Additional Engineering Studies; c. Monitoring Services Contract; d. Visibility & Communications.

<!-- b000089 | prose | pages [4] -->
1.1.3 Spillway Refurbishment (estimated cost US$124.6 million)

<!-- b000090 | prose | pages [4] -->
1 Financing in the component is mainly used for goods, works and non-consulting services as- sociated with the refurbishment of the spillway, which is composed of two parts: a. Spillway Re- furbishment Contract: The works will be conducted at one gate at a time, in a sequenced manner starting with the gates that today show the largest need for rehabilitation; b. Additional Engineering Studies.

<!-- b000091 | prose | pages [4] -->
1.1.4 Beneﬁts

<!-- b000092 | prose | pages [4] -->
1 Besides the elimination of potential danger and operational limitation which is mentioned above, the repairing of the dam also reinforce the integrated infrastructure platform within the Zambezi River basin. The beneﬁts through avoided disaster and continued power production are substantial, considering the estimated 3 million people living in the potential impact area and the economic value in excess of US$8 billion.

<!-- b000093 | prose | pages [4] -->
1.2 Rebuilding the Existing Kariba Dam

<!-- b000094 | prose | pages [4] -->
2 After 50 years of operation serving the southern African region, the geological conditions under the Kariba dam have been changed with the scouring and erosion of the water, so that the initial design of the dam is not appropriate for the new conditions. In this way, rebuilding the dam is a reasonable alternative to replace and even reinforce the function of the old one, and Lake Kariba is also utilized as a reservior. The ﬁnancing of the project will be primarily utilized for civil engineering works and electrical and mechanical works.

<!-- b000095 | prose | pages [4] -->
• Civil Engineering Works (estimated cost US$729.1 million): The component will include the costs of access roads, township, dam wall, south bank power station and engineering fees.

<!-- b000096 | prose | pages [4] -->
• Electrical and Mechanical Works (estimated cost US$380.6 million): The component will in- clude the costs of generation plant and equipment, transmission system and engineering fees.

<!-- b000097 | furniture | pages [5] -->
Team # 65448

<!-- b000098 | furniture | pages [5] -->
Page 2 of 25

<!-- b000099 | prose | pages [5] -->
The rebuilt dam can be designed to suit the new geological conditions and eliminate the over- whelming erosion confronted in the previous design. The beneﬁts through avoided frequent main- tenance of the dam and improved manipulating capability are substantial, given the lifespan and signiﬁcance of the dam for the approximately 3 million local residents.

<!-- b000100 | prose | pages [5] -->
Removing the Kariba Dam & Replacing It with A Series of Ten to Twenty Smaller 1.3 Dams Along the Zambezi River

<!-- b000101 | prose | pages [5] -->
During the construction of the Kariba Dam, the dam suffered from three huge ﬂoodings exceeding the design ﬂood. And the dam became broken quickly in ﬁfty years, which was quite shorter than the designed lifespan.1 All these facts ﬁgure out that more dams should be constructed on the Zambezi River in order to prevent the unexpected ﬂoodings. In this way, replacing the Kariba Dam with a series of ten to twenty smaller dams is an alternative which are more likely to balance the costs and safety.

<!-- b000102 | prose | pages [5] -->
As a series of so many dams is quite rare in the world, the costs can only be estimated approx- imately by the number and size of the dams. Financing of the project is mainly utilized for dam construction and relevant institutional project support.

<!-- b000103 | prose | pages [5] -->
• Dam Construction (estimated cost US$860 million): The costs of the dam construction are as- sumed to increase exponentially with the dam size increasing. Therefore, the costs of different dam types (which are introduced in the following model) are listed in Table 1. According to the following model, eight III dams and two IV dams are constructed, which cost US$860 million.

<!-- b000104 | prose | pages [5] -->
• Institutional Project Support (estimated cost US$69.6 million).

<!-- b000105 | prose | pages [5] -->
The area of Reservior/m2 Warning water levelHmi/m Types of dam

<!-- b000106 | prose | pages [5] -->
1 × 108 I

<!-- b000107 | prose | pages [5] -->
1 × 107 II

<!-- b000108 | prose | pages [5] -->
1 × 106 III

<!-- b000109 | prose | pages [5] -->
1 × 105 IV

<!-- b000110 | prose | pages [5] -->
Costs/million US$

<!-- b000111 | prose | pages [5] -->
60 10

<!-- b000112 | prose | pages [5] -->
50 1

<!-- b000113 | prose | pages [5] -->
40 0.8

<!-- b000114 | prose | pages [5] -->
30 0.6

<!-- b000115 | caption | pages [5] -->
Table 1: Costs of different dam types

<!-- b000116 | prose | pages [5] -->
The construction of the dam system can balance between the safety and costs and have excellent functions to prevent unexpected ﬂoodings, whose beneﬁts through avoided catastrophe is substan- tial, considering the powerful water management capabilities and more abundant hydropower.

<!-- b000117 | prose | pages [5] -->
2

<!-- b000118 | heading | pages [5] -->
Introduction

<!-- b000119 | prose | pages [5] -->
2.1 Restatement of the problem

<!-- b000120 | prose | pages [5] -->
Kariba Dam, constructed in 1955-59, with a storage capacity of 180km3, is one of the largest dams in Africa. Now it is in dire need of maintenance. The Zambezi River Authority (ZRA) faces three available options to address this situation:

<!-- b000121 | prose | pages [5] -->
• (Option 1) Repairing the existing Kariba Dam;

<!-- b000122 | prose | pages [5] -->
• (Option 2) Rebuilding the existing Kariba Dam;

<!-- b000123 | prose | pages [5] -->
• (Option 3) Removing the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the Zambezi River.

<!-- b000124 | furniture | pages [6] -->
Team # 65448

<!-- b000125 | furniture | pages [6] -->
Page 3 of 25

<!-- b000126 | prose | pages [6] -->
On the one hand, we need to brieﬂy assess all the three options above and provide an overview of potential costs and beneﬁts associated with each option.

<!-- b000127 | prose | pages [6] -->
On the other hand, the problem needs us to conduct a detailed analysis on option 3. We need to give a recommendation on how to design a new system of dam. The new system must meet following requirements:

<!-- b000128 | prose | pages [6] -->
• Having the same overall water management capabilities as the existing Kariba Dam, In our report, we use the total live storage of reservoirs in front of dams which marks the ability of a dam system to dynamically regulate the water ﬂows within the basin to describe the overall water management capabilities.

<!-- b000129 | prose | pages [6] -->
• Providing the same or greater levels of protection and water management options for Lake Kariba. For Lake Kariba, the more stable the inﬂow is with the variation of seasons, the better conditions like ﬁshing conditions Lake Kariba can provide for local people. So our new dam system is expected to make the inﬂow of Lake Kariba more stable than the original Kariba Dam.

<!-- b000130 | prose | pages [6] -->
• Properly addressing known or predicted normal water cycles.

<!-- b000131 | prose | pages [6] -->
• Having the ability to handle emergency water ﬂow situations including ﬂooding and prolonged low water conditions. Extreme conditions derive from abnormal rainfall. When rainfall of some region increases sharply, our dam system is expected to be adjusted to make sure that no region is ﬂooded as possible and when some regions experience prolonged drought our system should be adjusted to provide more runoff for that region as possible.

<!-- b000132 | prose | pages [6] -->
In our main report, we are required to provide:

<!-- b000133 | prose | pages [6] -->
• The number and placement of the new dams along the Zambezi River.

<!-- b000134 | prose | pages [6] -->
• A guidance to the ZRA managers that explains and justiﬁes the actions that should be taken to properly handle emergency water ﬂow situations.

<!-- b000135 | prose | pages [6] -->
• Information about the location and last time for a speciﬁc extreme condition in our guidance.

<!-- b000136 | prose | pages [6] -->
2.2 Our Approach

<!-- b000137 | prose | pages [6] -->
Based on the detailed data provided by World Bank, we conduct the assessment of three options, and provide a reasonable and detailed model to construct a new dam system with some emergency strategies.

<!-- b000138 | prose | pages [6] -->
To begin with, we offer a brief assessment report with potential costs and beneﬁts according to abundant references and reliable data. We complete the evaluation of repairing the Kariba Dam refering to the Kariba Dam Rehabilitation Project in the charge of World Bank, while we realize the assessment of rebuilding the dam following the actual capital investment expenditure of the Stage 1 of the Kariba Project. And the assessment of replacing the dam is carefully estimated according to the model to construct the new dam system.

<!-- b000139 | prose | pages [6] -->
Then, we concentrate on the establishment of the model for new dam system. Firstly, we establish a Hydrodynamic Model (HM) of the Zambezi River in order to estimate the ﬂowing and depth situation of the river. The model is constructed based on ﬂow conservation and energy conservation, which separately producing continuity equation and energy conservation equation, taking the normal water cycles and on-way resistance into account. Moreover, we obtain the numerical solution of the Hydrodynamic Model with Mathematica, and get the approximate current velocity curve and river depth curve along the river.

<!-- b000140 | prose | pages [6] -->
Secondly, we realize the site selection and number conﬁrmation of the new dams according to the ﬂowing and depth situation estimated by HM, geological data and hydrological data. We determine the evaluation indexes after consulting professional literatures, and Grey Relation Grade Analysis is utilized in the selection among candidate sites so that all the indexes can be considered comprehen- sively and objectively.

<!-- b000141 | furniture | pages [7] -->
Team # 65448

<!-- b000142 | furniture | pages [7] -->
Page 4 of 25

<!-- b000143 | prose | pages [7] -->
Thirdly, we establish a Difference Model (DM) of the Zambezi River with a dam system to provide sufﬁcient details for the conﬁrmation of dam construction and modulating strategies. We separate the river into several segments by the dams. A difference approximation of HM is applied to describe each segment of the river. We utilize a hydraulic emprical formula to determine the discharges of the dam. In this way, the recurrence formulas can be obtained to easily determine the runoff and river depth along the river with given environmental and initial conditions.

<!-- b000144 | prose | pages [7] -->
Fourthly, the type of each dam is conﬁrmed with corrected DM, with the overall water manage- ment capabilities, protection and water management options for Lake Kariba evaluated and special topograph considered. Considering the loss of energy in collision, tributaries and the runoff varia- tion with rainfall at headstram and tributaries, we correct DM to adapt to the reality. With the results calculated by corrected DM, we conﬁrm the type of each dam balancing the safety and costs. Each type of dam has three gears of discharges, which increases the water management options.

<!-- b000145 | prose | pages [7] -->
Finally, the strategies to handle such emergency water ﬂow situations as ﬂooding and drought are designed with the new dam system established above. When solving a known catastrophe, we utilize the exhaustive method to rule out the best strategies which realized by the gear variation of the dam. It is validated that the new dam system can handle most extreme conditions and the method we adopted to establish the strategy is of low sensibility considering reasonable errors.

<!-- b000146 | prose | pages [7] -->
3

<!-- b000147 | heading | pages [7] -->
General Assumption

<!-- b000148 | prose | pages [7] -->
• All dams are double curvature concrete arch dams and each dam is built with a hydropower station and a reservoir, in consistence with the original Kariba Dam.

<!-- b000149 | prose | pages [7] -->
• The costs of the dams have positive correlation with the size of the dams.

<!-- b000150 | prose | pages [7] -->
• The water is forced by on-way resistance, which is proportial to current velocity and the coefﬁ- cient is a constant.

<!-- b000151 | prose | pages [7] -->
• The evaporation exists anytime and is approximately a constant.

<!-- b000152 | prose | pages [7] -->
4

<!-- b000153 | heading | pages [7] -->
Notations

<!-- b000154 | heading | pages [7] -->
Notations

<!-- b000155 | prose | pages [7] -->
x

<!-- b000156 | prose | pages [7] -->
Deﬁnitions

<!-- b000157 | prose | pages [7] -->
The distance away from the headstream

<!-- b000158 | prose | pages [7] -->
L The width of the river

<!-- b000159 | prose | pages [7] -->
h

<!-- b000160 | prose | pages [7] -->
v

<!-- b000161 | prose | pages [7] -->
The river depth

<!-- b000162 | prose | pages [7] -->
Current velocity

<!-- b000163 | prose | pages [7] -->
ρ The density of the water

<!-- b000164 | prose | pages [7] -->
q

<!-- b000165 | prose | pages [7] -->
δ

<!-- b000166 | prose | pages [7] -->
k

<!-- b000167 | prose | pages [7] -->
Rainfall

<!-- b000168 | prose | pages [7] -->
Evaporation

<!-- b000169 | prose | pages [7] -->
on-way resistance coefﬁcient

<!-- b000170 | prose | pages [7] -->
Q

<!-- b000171 | prose | pages [7] -->
H

<!-- b000172 | prose | pages [7] -->
Runoff

<!-- b000173 | prose | pages [7] -->
The depth of the reservoir attached to dam

<!-- b000174 | prose | pages [7] -->
θ The gate opening of the dam

<!-- b000175 | prose | pages [7] -->
b The width of the gate hole

<!-- b000176 | prose | pages [7] -->
A The outﬂow coefﬁcient of the dam

<!-- b000177 | furniture | pages [8] -->
Team # 65448

<!-- b000178 | prose | pages [8] -->
5

<!-- b000179 | heading | pages [8] -->
The Model

<!-- b000180 | furniture | pages [8] -->
Page 5 of 25

<!-- b000181 | heading | pages [8] -->
Hydrodynamic Model of the Zambezi River

<!-- b000182 | prose | pages [8] -->
5.1

<!-- b000183 | prose | pages [8] -->
In this section, we establish a hydrodynamic model of the current velocity and river depth which vary with the space and time, which is based on ﬂow conservation and energy conservation. When the current velocity and river depth at the headstream is given, the whole Zamberi River can be depicted with the current velocity and river depth anywhere and anytime.

<!-- b000184 | prose | pages [8] -->
5.1.1 Continuity Equation

<!-- b000185 | prose | pages [8] -->
Considering a short segment of the river from x to x + ∆x (x and x + ∆x are all the distances away from the headstream), the ﬂow conservation is given by

<!-- b000186 | prose | pages [8] -->
Qin + qrain −qevaporation −Qout = ρ∆V

<!-- b000187 | prose | pages [8] -->
where

<!-- b000188 | prose | pages [8] -->
(1)

<!-- b000189 | prose | pages [8] -->
• Qin is the quantity of water ﬂowing into the segment,

<!-- b000190 | prose | pages [8] -->
• qrain is the rainfall quantity of the segment,

<!-- b000191 | prose | pages [8] -->
• qevaporation is the evaporation quantity of the segment,

<!-- b000192 | prose | pages [8] -->
• Qout is the quantity of water ﬂowing out of the segment,

<!-- b000193 | prose | pages [8] -->
• ρ is the density of water,

<!-- b000194 | prose | pages [8] -->
• V is the volume of water in this segment.

<!-- b000195 | prose | pages [8] -->
Qin, qrain, qevaporation, Qout and ∆V in the time period of ∆t can be written as

<!-- b000196 | prose | pages [8] -->
Qin = ρL(x)h(x, t)v(x, t)∆t (2)

<!-- b000197 | prose | pages [8] -->
qrain = ρq(x)L(x)∆x∆t (3)

<!-- b000198 | prose | pages [8] -->
qevaporation = ρδ(x)L(x)∆x∆t (4)

<!-- b000199 | prose | pages [8] -->
Qout = ρL(x + ∆x)h(x + ∆x, t)v(x + ∆x, t)∆t (5)

<!-- b000200 | prose | pages [8] -->
∆V = L(x)∆x[h(x, t + ∆t) −h(x, t)]

<!-- b000201 | prose | pages [8] -->
The ﬂow conservation equation turns into

<!-- b000202 | prose | pages [8] -->
(6)

<!-- b000203 | prose | pages [8] -->
ρ[q(x) −δ(x)]L(x)∆x∆t + ρ[L(x)h(x, t)v(x, t) −L(x + ∆x)h(x + ∆x, t)v(x + ∆x, t)]∆t

<!-- b000204 | prose | pages [8] -->
(7) = ρL(x)∆x[h(x, t + ∆t) −h(x, t)]

<!-- b000205 | prose | pages [8] -->
After simpliﬁcation, the equation is given by

<!-- b000206 | prose | pages [8] -->
+ [q(x) −δ(x)]L(x) = L(x)∂h(x, t)

<!-- b000207 | prose | pages [8] -->
−∂[L(x)h(x, t)v(x, t)]

<!-- b000208 | prose | pages [8] -->
∂x

<!-- b000209 | prose | pages [8] -->
which is the continuity equation of the river.

<!-- b000210 | prose | pages [8] -->
(8) ∂t

<!-- b000211 | furniture | pages [9] -->
Team # 65448

<!-- b000212 | prose | pages [9] -->
5.1.2 Energy Conservation Equation

<!-- b000213 | furniture | pages [9] -->
Page 6 of 25

<!-- b000214 | prose | pages [9] -->
Also considering a short segment of the river from x to x + ∆x (x and x + ∆x are all the dis- tances away from the headstream), and neglecting the variation of the pressure with x, the energy conservation is written as

<!-- b000215 | prose | pages [9] -->
Wgravity + Wresistance = ∆Twater + ∆Train + ∆Tevaporation

<!-- b000216 | prose | pages [9] -->
where

<!-- b000217 | prose | pages [9] -->
(9)

<!-- b000218 | prose | pages [9] -->
• Wgravity is the work done by the gravity of water,

<!-- b000219 | prose | pages [9] -->
• Wresistance is the work done by the on-way resistance,

<!-- b000220 | prose | pages [9] -->
• ∆Twater is the change of kinetic energy of the water in the segment,

<!-- b000221 | prose | pages [9] -->
• ∆Train is the change of kinetic energy of rain in the segment,

<!-- b000222 | prose | pages [9] -->
• ∆Tevaporation is the change of kinetic energy of water evaporated from the segment.

<!-- b000223 | prose | pages [9] -->
Wgravity and ∆Twater in the time period of ∆t is given by

<!-- b000224 | prose | pages [9] -->
Wgravity = −ρgL(x)h(x, t)v(x, t)∆t∆y

<!-- b000225 | prose | pages [9] -->
∆Twater = 1

<!-- b000226 | prose | pages [9] -->
(10)

<!-- b000227 | prose | pages [9] -->
2ρL(x)h(x, t)v(x, t)∆(v2)∆t

<!-- b000228 | prose | pages [9] -->
(11)

<!-- b000229 | prose | pages [9] -->
2ρL(x)h(x, t)v2(x, t)∆t(∂v

<!-- b000230 | prose | pages [9] -->
= 1

<!-- b000231 | prose | pages [9] -->
∂t ∆t + ∂v

<!-- b000232 | prose | pages [9] -->
∂x∆x)

<!-- b000233 | prose | pages [9] -->
Assuming that the on-way resistance per volume is proportional to the current velocity, which is

<!-- b000234 | prose | pages [9] -->
Fr = kv(x, t)

<!-- b000235 | prose | pages [9] -->
Wresistance is expressed as

<!-- b000236 | prose | pages [9] -->
(12)

<!-- b000237 | prose | pages [9] -->
Wresistance = −kL(x)h(x, t)v(x, t)∆x∆t (13)

<!-- b000238 | prose | pages [9] -->
Supposing that the initial velocity of rain in the river is approximately zero, ∆Train is given by

<!-- b000239 | prose | pages [9] -->
∆Train = 1

<!-- b000240 | prose | pages [9] -->
2ρq(x)v2(x, t)∆x∆t (14)

<!-- b000241 | prose | pages [9] -->
Neglecting the velocity of vapour evaporated from the river, ∆Tevaporation is given by

<!-- b000242 | prose | pages [9] -->
∆Tevaporation = −1

<!-- b000243 | prose | pages [9] -->
2ρδ(x)v2(x, t)∆x∆t (15)

<!-- b000244 | prose | pages [9] -->
Thus, the energy conservation equation after simpliﬁcation is

<!-- b000245 | prose | pages [9] -->
−gh(x, t)y′(x) −kh(x, t) = h(x, t)v(x, t)∂v

<!-- b000246 | prose | pages [9] -->
5.1.3 Boundary Condition and Initial Condition

<!-- b000247 | prose | pages [9] -->
∂x + h(x, t)∂v

<!-- b000248 | prose | pages [9] -->
∂t + 1

<!-- b000249 | prose | pages [9] -->
2[q(x) −δ(x)]v(x, t) (16)

<!-- b000250 | prose | pages [9] -->
In order to solve the above two equations, the boundary condition and initial condition of the river should be given. Boundary conditions refer to the current velocity and river depth at the head- stream, which can be measured in reality. Initial condition refer to the current velocity and river depth anywhere along the river when t = 0, which can also be provided by hydrological stations.

<!-- b000251 | prose | pages [9] -->
In our model, the current velocity and river depth at the headstream are assumed to be constant, which is 

<!-- b000252 | prose | pages [9] -->
v(0, t) = v0

<!-- b000253 | prose | pages [9] -->


<!-- b000254 | prose | pages [9] -->
(17)

<!-- b000255 | prose | pages [9] -->
h(0, t) = h0

<!-- b000256 | prose | pages [9] -->


<!-- b000257 | prose | pages [9] -->
The initial depth is also supposed to be consistent along the river, while the inital current velocity is set to have the distribution of free falling movement, which can be written as

<!-- b000258 | prose | pages [9] -->


<!-- b000259 | prose | pages [9] -->
p

<!-- b000260 | prose | pages [9] -->
v2

<!-- b000261 | prose | pages [9] -->
0 + 2g[y(0) −y(x)]

<!-- b000262 | prose | pages [9] -->
v(x, 0) =

<!-- b000263 | prose | pages [9] -->


<!-- b000264 | prose | pages [9] -->
h(x, 0) = h0

<!-- b000265 | prose | pages [9] -->


<!-- b000266 | prose | pages [9] -->
(18)

<!-- b000267 | furniture | pages [10] -->
Team # 65448

<!-- b000268 | furniture | pages [10] -->
Page 7 of 25

<!-- b000269 | prose | pages [10] -->
5.1.4

<!-- b000270 | heading | pages [10] -->
Calculation of the Model

<!-- b000271 | prose | pages [10] -->
The hydrodynamic equations of the river are all partial different equations and approximately impossible to get the analytical solution, so we should obtain all the values of the known parameters in the equations so that we can get the numerical solution of the equations.

<!-- b000272 | prose | pages [10] -->
We observe the Zambezi River in Google Earth and acquire the altitude variations along the river, which gives y(x) with interpolation. The curve of y(x) (altitude variation) is shown in Figure 1.

<!-- b000273 | caption | pages [10] -->
Figure 1: Altitude variation

<!-- b000274 | prose | pages [10] -->
The width of the Zambezi River is almost constant along the river, which means L(x) = L. The runoff, rainfall and evaporation along the river are obtained from the data provided by World Bank,3 which determines v0, h0, q(x), δ(x).In order to simplify the calculation, δ(x) is taken as a con- stant δ, which is the annual average evaporation. The rainfall data is provided by some hydrological stations, so the data is discrete, which is shown in Figure 1. In order to acquire the rough data of rain- fall anywhere along the river, we try to ﬁt the data points of rainfall and obtain the analysis formula, which is shown in Figure 2-6.

<!-- b000275 | caption | pages [10] -->
Figure 2: Spring rainfall

<!-- b000276 | caption | pages [10] -->
Figure 3: Summer rainfall

<!-- b000277 | furniture | pages [11] -->
Team # 65448

<!-- b000278 | furniture | pages [11] -->
Page 8 of 25

<!-- b000279 | caption | pages [11] -->
Figure 4: Fall rainfall

<!-- b000280 | caption | pages [11] -->
Figure 5: Winter rainfall

<!-- b000281 | caption | pages [11] -->
Figure 6: The annual rainfall along the river and the ﬁtting curve

<!-- b000282 | prose | pages [11] -->
Considering the data all above and some scientiﬁc constants (such as g and k), all the known parameters can be given:

<!-- b000283 | prose | pages [11] -->
• g = 9.8m/s, k = 1.0 × 10−6kg · m−3 · s−1

<!-- b000284 | prose | pages [11] -->
• v0 = 10m/s, h0 = 20m, L = 1km, δ = 3.2 × 10−9m/s

<!-- b000285 | prose | pages [11] -->
After a few approximation and estimation, the trend of the current velocity and depth along the river from the initial time to the ending time can be obtained, which is shown in Figure 7-8. According to the results, the trend of the current velocity and depth will approach a stable state as the time goes.

<!-- b000286 | caption | pages [11] -->
Figure 8: River Depth

<!-- b000287 | caption | pages [11] -->
Figure 7: Current Velocity

<!-- b000288 | prose | pages [11] -->
5.2 Selection System of the Dam Site

<!-- b000289 | prose | pages [11] -->
The site selection of the dams is signiﬁcant in dam construction, which directly decides the func- tion and lifespan of the dams. As many parameters of river have been obtained in previous calcu-

<!-- b000290 | furniture | pages [12] -->
Team # 65448

<!-- b000291 | furniture | pages [12] -->
Page 9 of 25

<!-- b000292 | prose | pages [12] -->
lation, we can evaluate the location from many aspects, so that a scientiﬁc and objective selection system of the dam site can be established based on Grey Relation Grade Analysis.4

<!-- b000293 | prose | pages [12] -->
5.2.1 Evaluation indexes

<!-- b000294 | prose | pages [12] -->
In order to smooth the channel and acquire the maximum hydropower resources, the dams should be established in the regions with steep terrain gap, large river depth and much rainfall, where the huge quantity of water and rapid current may make the channel so turbulent as to threaten the safety of transportation and residents nearby, yet ensuring the abundant hydropower resources at the same time. The situation is similar when the current acceleration is enormous.5

<!-- b000295 | prose | pages [12] -->
In addition to this, some special topographies are appropriate for dam construction. Lakes can be utilized as a natural reservior for the dam, pocket-like lowlands can contribute to water management and valleys can eliminate the construction amount.5

<!-- b000296 | prose | pages [12] -->
What is more, the smaller width the channel has, the lower the construction cost is.5

<!-- b000297 | prose | pages [12] -->
In this way, the following indexes are considered for the site selection:

<!-- b000298 | prose | pages [12] -->
• Terrain gap: y′(x), the derivative of y(x);

<!-- b000299 | prose | pages [12] -->
• River depth h(x) in stable state;

<!-- b000300 | prose | pages [12] -->
• Rainfall q(x);

<!-- b000301 | prose | pages [12] -->
• Current acceleration ∂v(x,t) ∂t

<!-- b000302 | prose | pages [12] -->
• Lakes;

<!-- b000303 | prose | pages [12] -->
• Pocket-like lowlands;

<!-- b000304 | prose | pages [12] -->
• Valleys;

<!-- b000305 | prose | pages [12] -->
• River width L(x) (which can be obtained from the map).

<!-- b000306 | prose | pages [12] -->
The topographic indexes are evaluated by checking whether the suitable topography exists. If the appropriate topography exists, the relevant index is 1; if not, zero.

<!-- b000307 | prose | pages [12] -->
5.2.2 Candidate Site

<!-- b000308 | prose | pages [12] -->
Several candidate sites should be determined to optimize the site selection. According to the relief map, rainfall, river depth calculated by the hydrodynamic model, considering the distances between adjacent dams, 26 advantageous sites are selected as candidate sites, which is shown in Figure 9.

<!-- b000309 | caption | pages [12] -->
Figure 9: Candidate sites

<!-- b000310 | furniture | pages [13] -->
Team # 65448

<!-- b000311 | prose | pages [13] -->
5.2.3 Grey Relation Grade Analysis

<!-- b000312 | furniture | pages [13] -->
Page 10 of 25

<!-- b000313 | prose | pages [13] -->
Because of the complex interaction between these parameters, we ﬁnally choose Grey Relation Grade Analysis to conﬁrm the selection system.

<!-- b000314 | prose | pages [13] -->
Firstly, index weight should be obtained. The concrete steps are:

<!-- b000315 | prose | pages [13] -->
Step 1: Determine the reference data series as an ideal comparison standard. In our system, the largest value of each metric (river width is taken minus) constitutes the reference sequence.

<!-- b000316 | prose | pages [13] -->
X0 = (x0(1), x0(2), · · · , x0(m)) (19)

<!-- b000317 | prose | pages [13] -->
Step 2: Calculate the absolute difference value of each parameter sequence and the reference se- quence of the corresponding elements,as ∆i(j) = |xi(j) −x0(j)|. In the formula, i represents the number of candidate sites; j is the number of metrics; x0(j) means the reference data in the metric.

<!-- b000318 | prose | pages [13] -->
1⩽i⩽m{∆i(j)} and b = max 1⩽i⩽m{∆i(j)}. 1⩽i⩽n max

<!-- b000319 | prose | pages [13] -->
Step 3: Conﬁrm a = min

<!-- b000320 | prose | pages [13] -->
1⩽i⩽n min

<!-- b000321 | prose | pages [13] -->
Step 4: Calculate the correlation coefﬁcient as:

<!-- b000322 | prose | pages [13] -->
fi(j) = a + bλ (20) ∆i(j) + bλ

<!-- b000323 | prose | pages [13] -->
where resolution coefﬁcient λ ∈(0, 1), commonly using 0.5. Step 5: Calculate the correlation degree.

<!-- b000324 | prose | pages [13] -->
rj = 1

<!-- b000325 | prose | pages [13] -->
n

<!-- b000326 | prose | pages [13] -->
n n X

<!-- b000327 | prose | pages [13] -->
fi(j) (21)

<!-- b000328 | prose | pages [13] -->
i=1

<!-- b000329 | prose | pages [13] -->
Step 6: Calculate the weight of each measure standard.

<!-- b000330 | prose | pages [13] -->
r′

<!-- b000331 | prose | pages [13] -->
j = rj

<!-- b000332 | prose | pages [13] -->
(22)

<!-- b000333 | prose | pages [13] -->
r1 + r2 + · · · + rm

<!-- b000334 | prose | pages [13] -->
Step 7: Build the evaluation model.

<!-- b000335 | prose | pages [13] -->
2xi(2) + · · · + r′

<!-- b000336 | prose | pages [13] -->
Zi = r′

<!-- b000337 | prose | pages [13] -->
1xi(1) + r′ mxi(m) (23)

<!-- b000338 | prose | pages [13] -->
Based on the data we got above, we can solve the model and obtain the following results (Figure 10).

<!-- b000339 | caption | pages [13] -->
Figure 10: Results of Grey Relation Grade Analysis

<!-- b000340 | prose | pages [13] -->
As shown in Figure 11-12, the following 11 sites are selected to constructed dams, considering the costs and the distances clustering between adjacent dams.

<!-- b000341 | furniture | pages [14] -->
Team # 65448

<!-- b000342 | furniture | pages [14] -->
Page 11 of 25

<!-- b000343 | caption | pages [14] -->
Figure 11: Dam sites in terrain map

<!-- b000344 | caption | pages [14] -->
Figure 12: Dam sites in altitude map

<!-- b000345 | prose | pages [14] -->
5.3

<!-- b000346 | heading | pages [14] -->
Difference Model of the Dam System

<!-- b000347 | prose | pages [14] -->
When the dam system is considered in the Zambezi River, the Hydrodynamic Model with partial differential equations is too complex to describe the inﬂuences of the dam system, making it impos- sible to obtain the changes of the river in a bearable time. Therefore, the simpliﬁcation of the model should be introduced, which is difference model of the dam system, providing recurrence formulas to calculate the runoff of the river with dam system.

<!-- b000348 | prose | pages [14] -->
The dams are numbered from 1 to 11, and the time is seperated into j time periods of T. For the ith dam in the jth time period,

<!-- b000349 | prose | pages [14] -->
• Q(i+1)j is the river ﬂux ﬂowing out of the dam. Specially, Q1j represents the ﬂux at the head- stream;

<!-- b000350 | prose | pages [14] -->
• Q′ ij is the river ﬂux ﬂowing into the dam;

<!-- b000351 | furniture | pages [15] -->
Team # 65448

<!-- b000352 | furniture | pages [15] -->
Page 12 of 25

<!-- b000353 | prose | pages [15] -->
• qij is the rainfall ﬂux density in the dam region and the region between the dam and previous one;

<!-- b000354 | prose | pages [15] -->
• δij is the evaporation ﬂux density in the dam region and the region between the dam and previous one;

<!-- b000355 | prose | pages [15] -->
• ∆yi is the altitude changes between the dam and previous one;

<!-- b000356 | prose | pages [15] -->
• li is the distance between the dam and the previous one;

<!-- b000357 | prose | pages [15] -->
• hij is the river depth in the region between the dam and the previous one;

<!-- b000358 | prose | pages [15] -->
• Hij is the water depth of the reservior attached to the dam;

<!-- b000359 | prose | pages [15] -->
• Si is the area of the reservior attached to the dam;

<!-- b000360 | prose | pages [15] -->
• H0i is the dead water level of the reservior attached to the dam (dead water level is the mini- mum water level which the reservoir is allowed to drawdown).

<!-- b000361 | caption | pages [15] -->
Figure 13: Diagram describing the situation of the river with dam system

<!-- b000362 | prose | pages [15] -->
5.3.1 Equations in the River (Without the Dam)

<!-- b000363 | prose | pages [15] -->
As is written in the Hydrodynamic Model, the continuity equation (based on the ﬂow conserva- tion) can be written as

<!-- b000364 | prose | pages [15] -->
ij = liL∆hi

<!-- b000365 | prose | pages [15] -->
(qij −δij)liL + Qij −Q′

<!-- b000366 | prose | pages [15] -->
hi(j+1)−hij

<!-- b000367 | prose | pages [15] -->
In the time period of T, ∆hi

<!-- b000368 | prose | pages [15] -->
∆t =

<!-- b000369 | prose | pages [15] -->
. T

<!-- b000370 | prose | pages [15] -->
(24) ∆t

<!-- b000371 | prose | pages [15] -->
Neglecting the variation of v in time period of T, the energy conservation equation is given by

<!-- b000372 | prose | pages [15] -->
2ρ(qij −δij)LliTv2 + 1

<!-- b000373 | prose | pages [15] -->
ρLhijvTg∆yi −ρkhijLvTli = 1

<!-- b000374 | prose | pages [15] -->
where v and ∆(v2) can be expressed by Qij and Q′

<!-- b000375 | prose | pages [15] -->
2ρLhijvT∆(v2) (25)

<!-- b000376 | prose | pages [15] -->
ij.

<!-- b000377 | prose | pages [15] -->
Qij + Q′

<!-- b000378 | prose | pages [15] -->
v =

<!-- b000379 | prose | pages [15] -->
∆(v2) =

<!-- b000380 | prose | pages [15] -->
ij (26) 2hijL

<!-- b000381 | prose | pages [15] -->
2 −Q2

<!-- b000382 | prose | pages [15] -->
Q′ Q′

<!-- b000383 | prose | pages [15] -->
ij

<!-- b000384 | prose | pages [15] -->
ij

<!-- b000385 | prose | pages [15] -->
(27)

<!-- b000386 | prose | pages [15] -->
h2

<!-- b000387 | prose | pages [15] -->
ijL2

<!-- b000388 | prose | pages [15] -->
After simpliﬁcation, the equations in the river without the dam are

<!-- b000389 | prose | pages [15] -->


<!-- b000390 | prose | pages [15] -->
(qij −δij)liL + Qij −Q′

<!-- b000391 | prose | pages [15] -->
ij = liL

<!-- b000392 | prose | pages [15] -->
   

<!-- b000393 | prose | pages [15] -->
 

<!-- b000394 | prose | pages [15] -->
ijL2li = Q′

<!-- b000395 | prose | pages [15] -->
2h2 ijL2g∆yi −2kh2

<!-- b000396 | prose | pages [15] -->
 

<!-- b000397 | prose | pages [15] -->
ij

<!-- b000398 | prose | pages [15] -->
hi(j+1)−hij

<!-- b000399 | prose | pages [15] -->
T

<!-- b000400 | prose | pages [15] -->
(28)

<!-- b000401 | prose | pages [15] -->
2 −Q2 ij + 1

<!-- b000402 | prose | pages [15] -->
2(qij −δij)L(Qij + Q′ ij)li

<!-- b000403 | furniture | pages [16] -->
Team # 65448

<!-- b000404 | prose | pages [16] -->
5.3.2 Equations in the Dam Region

<!-- b000405 | furniture | pages [16] -->
Page 13 of 25

<!-- b000406 | prose | pages [16] -->
As is written in the Hydrodynamic Model, the continuity equation (based on the ﬂow conserva- tion) can be written as

<!-- b000407 | prose | pages [16] -->
(qij −δij)Si + Q′

<!-- b000408 | prose | pages [16] -->
∆Hi

<!-- b000409 | prose | pages [16] -->
ij −Q(i+1)j = Si

<!-- b000410 | prose | pages [16] -->
Hi(j+1)−Hij

<!-- b000411 | prose | pages [16] -->
In the time period of T, ∆Hi

<!-- b000412 | prose | pages [16] -->
∆t =

<!-- b000413 | prose | pages [16] -->
. T

<!-- b000414 | prose | pages [16] -->
(29) ∆t

<!-- b000415 | prose | pages [16] -->
According to Hydraulics textbook, Q(i+1)j has the following relation with Hij:6

<!-- b000416 | prose | pages [16] -->
3

<!-- b000417 | prose | pages [16] -->
Q(i+1)j = Ai(Hij −H0i)

<!-- b000418 | prose | pages [16] -->
(30) 2

<!-- b000419 | prose | pages [16] -->
where the Ai is the outﬂow coefﬁcient determined by the width bi of the gate hole and the relative gate opening θ of the dam. According to the emprical formula, Ai can be given by

<!-- b000420 | prose | pages [16] -->
Ai = 2.7674θbi

<!-- b000421 | prose | pages [16] -->
5.3.3 Recurrence Formulas

<!-- b000422 | prose | pages [16] -->
(31)

<!-- b000423 | prose | pages [16] -->
Concluding the equations above, the recurrence formulas of the river with dam systems can be obtained.

<!-- b000424 | prose | pages [16] -->
q

<!-- b000425 | prose | pages [16] -->
1 i −4( 1

<!-- b000426 | prose | pages [16] -->
−1

<!-- b000427 | prose | pages [16] -->


<!-- b000428 | prose | pages [16] -->
2 gLQijli−Q2

<!-- b000429 | prose | pages [16] -->
4 g2L2l2

<!-- b000430 | prose | pages [16] -->
2 gLli+

<!-- b000431 | prose | pages [16] -->
Q′

<!-- b000432 | prose | pages [16] -->
ij =

<!-- b000433 | prose | pages [16] -->
          

<!-- b000434 | prose | pages [16] -->
3

<!-- b000435 | prose | pages [16] -->


<!-- b000436 | prose | pages [16] -->
Q(i+1)j = Ai(Hij −H0i)

<!-- b000437 | prose | pages [16] -->


<!-- b000438 | prose | pages [16] -->
2

<!-- b000439 | prose | pages [16] -->
   

<!-- b000440 | prose | pages [16] -->


<!-- b000441 | prose | pages [16] -->
(qij−δij)liL+Qij−Q′

<!-- b000442 | prose | pages [16] -->
 

<!-- b000443 | prose | pages [16] -->
hi(j+1) =

<!-- b000444 | prose | pages [16] -->
 

<!-- b000445 | prose | pages [16] -->
liL

<!-- b000446 | prose | pages [16] -->
        

<!-- b000447 | prose | pages [16] -->
(qij−δij)Si+Q′

<!-- b000448 | prose | pages [16] -->
ij+2kh2

<!-- b000449 | prose | pages [16] -->
ijL2li−2h2

<!-- b000450 | prose | pages [16] -->
ijL2g∆yi)

<!-- b000451 | prose | pages [16] -->
2

<!-- b000452 | prose | pages [16] -->
(32)

<!-- b000453 | prose | pages [16] -->
ij ij T + hij

<!-- b000454 | prose | pages [16] -->
3

<!-- b000455 | prose | pages [16] -->
ij−Ai(Hij−H0i)

<!-- b000456 | prose | pages [16] -->
 

<!-- b000457 | prose | pages [16] -->
Hi(j+1) =

<!-- b000458 | prose | pages [16] -->


<!-- b000459 | prose | pages [16] -->
Si 2 T + Hij

<!-- b000460 | prose | pages [16] -->
In this way, when the known parameters are conﬁrmed, the river with dam system can be de- picted with Qij, Q′

<!-- b000461 | prose | pages [16] -->
ij, hij, Hij. All the known parameters are listed below.

<!-- b000462 | prose | pages [16] -->
• Q1j: the river ﬂux at the headstream;

<!-- b000463 | prose | pages [16] -->
• Q(i+1)0: the initial river ﬂux ﬂowing out of the dam;

<!-- b000464 | prose | pages [16] -->
• hi0: the initial river depth in the region between the dam and the previous one;

<!-- b000465 | prose | pages [16] -->
• Hi0: the initial water depth of the reservior attached to the dam;

<!-- b000466 | prose | pages [16] -->
• qij: the rainfall along the river;

<!-- b000467 | prose | pages [16] -->
• δij: the evaporation along the river;

<!-- b000468 | prose | pages [16] -->
• ∆yi is the altitude changes between the dam and previous one;

<!-- b000469 | prose | pages [16] -->
• li is the distance between the dam and the previous one;

<!-- b000470 | prose | pages [16] -->
• Si: the area of the reservior attached to the dam;

<!-- b000471 | prose | pages [16] -->
• Ai: the outﬂow coefﬁcient of the dam;

<!-- b000472 | prose | pages [16] -->
• H0i: the dead water level of the reservior attached to the dam;

<!-- b000473 | prose | pages [16] -->
• L: the width of the river;

<!-- b000474 | prose | pages [16] -->
• g: the acceleration of gravity;

<!-- b000475 | prose | pages [16] -->
• k: the on-way resistance coefﬁcient;

<!-- b000476 | prose | pages [16] -->
• T: the time scale.

<!-- b000477 | furniture | pages [17] -->
Team # 65448

<!-- b000478 | furniture | pages [17] -->
Page 14 of 25

<!-- b000479 | prose | pages [17] -->
Dam Construction & Manipulating System 5.4

<!-- b000480 | prose | pages [17] -->
As the number and placement of the new dams have been conﬁrmed, the size of dams and manip- ulating strategy should be assigned so that the dam systems can have good performance and handle emergency water ﬂow situations. The concrete steps to design the size of dams and manipulating strategy are listed below:

<!-- b000481 | prose | pages [17] -->
Step 1: Conﬁrm the parameters of different dam types. Step 2: Conﬁrm the type selection of each dam. Step 3: Evaluate the protection and water management options for Lake Kariba. Step 4: Strategies to handle emergency water ﬂow situations.

<!-- b000482 | prose | pages [17] -->
Conﬁrm the Parameters of Different Dam Types 5.4.1

<!-- b000483 | prose | pages [17] -->
According to the standard of Water Conservancy Engineering, the dams can be categoried into several types according to the capacity of the reservior attached.7 As shown in Table 2, four ap- propriate types of dam are selected considering the reality of the Zambezi River and the relevant parameters have been conﬁrmed.

<!-- b000484 | prose | pages [17] -->
The area of Reservior/m2 Types of dam

<!-- b000485 | prose | pages [17] -->
1 × 108 I

<!-- b000486 | prose | pages [17] -->
1 × 107 II

<!-- b000487 | prose | pages [17] -->
1 × 106 III

<!-- b000488 | prose | pages [17] -->
1 × 105 IV

<!-- b000489 | prose | pages [17] -->
A Warning water levelHmi/m

<!-- b000490 | prose | pages [17] -->
33θ 60

<!-- b000491 | prose | pages [17] -->
27θ 50

<!-- b000492 | prose | pages [17] -->
16θ 40

<!-- b000493 | prose | pages [17] -->
11θ 30

<!-- b000494 | caption | pages [17] -->
Table 2: Parameters of different dam types

<!-- b000495 | prose | pages [17] -->
Where θ is the relative gate opening of the dam. In order to simplify the manipulation of the dam, it is assumed that there are three gears of the gate opening, which means θ can be taken as 0.25, 0.5, 1.0. In normal situation, θ is taken as 0.5.

<!-- b000496 | caption | pages [17] -->
Figure 14: Diagram of the dam

<!-- b000497 | prose | pages [17] -->
5.4.2 Conﬁrm the Type Selection of Each Dam

<!-- b000498 | prose | pages [17] -->
The new dams should be established to protect the river’s basin from the ﬂoods and drought, so it seems that the dam with largest reservior is the best choice. However, the cost of one large dam is equal to that of many small dams. Therefore, we should take a reasonable balance between safety

<!-- b000499 | furniture | pages [18] -->
Team # 65448

<!-- b000500 | furniture | pages [18] -->
Page 15 of 25

<!-- b000501 | prose | pages [18] -->
and costs, which can be completed with the Difference Model of the Dam System. When each dam size has been conﬁrmed, Hij, hij, Qij, Q′

<!-- b000502 | prose | pages [18] -->
ij can be determined, which means a certain series of dam size will correspond to a certain river situation.

<!-- b000503 | prose | pages [18] -->
However, the main tributaries are neglected in the Difference Model of the Dam System, which play an important role in the river system. Therefore, we correct the model by detecting the main tributaries and adding them into the model. According to the terrain map of the basin, which is shown in Figure 15, the main tributaries distribute at the region between the dam A and B, B and

<!-- b000504 | prose | pages [18] -->
9j, q′ 7j, q′ 3j, q′ 2j, q′

<!-- b000505 | prose | pages [18] -->
C, F and G, H and I, J and K. Their runoff are marked as q′

<!-- b000506 | prose | pages [18] -->
11j. The runoff will be added into the ﬂux ﬂowing into the relevant dam. For example, the ﬂux ﬂowing into the 2nd dam will be Q′

<!-- b000507 | prose | pages [18] -->
2j + q′ 2j.

<!-- b000508 | caption | pages [18] -->
Figure 15: Tributaries

<!-- b000509 | prose | pages [18] -->
In addition to this, the loss of mechanical energy when the ﬂow collides with the banks and bottom of the river, so a loss coefﬁcient β should be included in the energy conservation equation, which is

<!-- b000510 | prose | pages [18] -->
q

<!-- b000511 | prose | pages [18] -->
−1

<!-- b000512 | prose | pages [18] -->
1 i −4(1

<!-- b000513 | prose | pages [18] -->
2gLQijli −Q2

<!-- b000514 | prose | pages [18] -->
4g2L2l2

<!-- b000515 | prose | pages [18] -->
2gLli +

<!-- b000516 | prose | pages [18] -->
Q′

<!-- b000517 | prose | pages [18] -->
ij =

<!-- b000518 | prose | pages [18] -->
ij + 2kh2

<!-- b000519 | prose | pages [18] -->
ijL2li −2h2

<!-- b000520 | prose | pages [18] -->
ijL2gβ∆yi)

<!-- b000521 | prose | pages [18] -->
(33) 2

<!-- b000522 | prose | pages [18] -->
Before calculating the best type selection with the Difference Model of the Dam System, all the known parameters should be conﬁrmed. It is assumed that the rainfall and evaporation in a certain region is constant in the time period we have concerned, which means qij = qi, δij = δi. The dead water level of each dam is supposed to be constant, which means H0j = H0. Apparently, the rainfall will inﬂuence the runoff at the headstream and tributaries, so it is reasonable to suppose that

<!-- b000523 | prose | pages [18] -->


<!-- b000524 | prose | pages [18] -->
Q1j = Q1 + α(q1 −δ1)

<!-- b000525 | prose | pages [18] -->
   

<!-- b000526 | prose | pages [18] -->
q′

<!-- b000527 | prose | pages [18] -->
2j = q′

<!-- b000528 | prose | pages [18] -->


<!-- b000529 | prose | pages [18] -->
2 + α(q2 −δ2)

<!-- b000530 | prose | pages [18] -->
     

<!-- b000531 | prose | pages [18] -->
q′

<!-- b000532 | prose | pages [18] -->
3j = q′ 3 + α(q3 −δ3)

<!-- b000533 | prose | pages [18] -->
 

<!-- b000534 | prose | pages [18] -->
q′

<!-- b000535 | prose | pages [18] -->
7j = q′

<!-- b000536 | prose | pages [18] -->
(34)

<!-- b000537 | prose | pages [18] -->
7 + α(q7 −δ7)

<!-- b000538 | prose | pages [18] -->
    

<!-- b000539 | prose | pages [18] -->
q′

<!-- b000540 | prose | pages [18] -->
9j = q′

<!-- b000541 | prose | pages [18] -->


<!-- b000542 | prose | pages [18] -->
9 + α(q9 −δ9)

<!-- b000543 | prose | pages [18] -->
    

<!-- b000544 | prose | pages [18] -->
q′

<!-- b000545 | prose | pages [18] -->
11j = q′

<!-- b000546 | prose | pages [18] -->


<!-- b000547 | prose | pages [18] -->
11 + α(q11 −δ11)

<!-- b000548 | prose | pages [18] -->


<!-- b000549 | prose | pages [18] -->
where Q1, q′

<!-- b000550 | prose | pages [18] -->
2, q′ 3, q′ 7, q′ 9, q′ 11 are separately the runoff at the headstream and each tributary, α is the constant coefﬁcient.

<!-- b000551 | prose | pages [18] -->
∆yi and li can be easily determined by the geographical data mentioned above, which is included in the Appendix. Q1, hi0, Hi0, qi and δi can be decided by the above hydrologcial data,3 where it is assumed that hi0 = h0, Hi0 = H0, δi = δ0, qi is supposed to obey the distribution concluded from the rainfall data.Li is presented in the appendices. Other known parameters are listed below:

<!-- b000552 | furniture | pages [19] -->
Team # 65448

<!-- b000553 | furniture | pages [19] -->
Page 16 of 25

<!-- b000554 | prose | pages [19] -->
• Q1 = 500m3/s, h0 = 20m, H0 = 20m, T = 60s

<!-- b000555 | prose | pages [19] -->
• q′ 2 = 150m3/s, q′ 3 = 100m3/s, q′ 7 = 50m3/s, q′ 9 = 120m3/s, q′ 11 = 80m3/s

<!-- b000556 | prose | pages [19] -->
• g = 9.8m/s2, k = 1 × 10−6kg · m3 · s−1, α = 3 × 109, β = 10−3

<!-- b000557 | prose | pages [19] -->
With all the known parameters conﬁrmed, we can calculate the best type selection with the cor- rected Difference Model of the Dam System. It is obvious that the smallest dam is cheapest, so we choose IV type for each dam at ﬁrst except the 11th one and the 7th one. At the site of the 11th dam, the Cahora Bassa Dam8 has been constructed, which is a I-type dam, so the 11 th dam is selected as I type. The 7th dam is located at the previous Kariba Dam, but the new geological condition after errosion is not suitable for a I-type dam, so II type is selected considering the huge capacity of Lake Kariba. Then we calculate the situation of the river (with 90000 iterations, which means 3 months for the model). According to the calculation, the situation of the river will approach a stable state with time goes. If Hij at the stable state is higher than the warning water level at one dam, the dam type will be upgraded for one grade. The procedure will be repeated until all Hij at the stable state are lower than the corresponding warning water level. However, another restriction should be satisﬁed by the ﬁnal type selection:

<!-- b000558 | prose | pages [19] -->
• P11 i=1 SiHmi ⩾VLake, which means the total capacity of the reserviors attached to new dams should be larger than the capacity of previous Lake Kariba (VLake). The total capacity represents the overall water management capabilities of the dam system. The restriction means the new dam system has the same and even higher overall water management capabilities than the Kariba Dam.

<!-- b000559 | prose | pages [19] -->
The detailed procedure is shown in the Figure 16.

<!-- b000560 | caption | pages [19] -->
Figure 16: Diagram of the Type Selection of Each Dam

<!-- b000561 | prose | pages [19] -->
The selection result is presented in Table 3.

<!-- b000562 | furniture | pages [20] -->
Team # 65448

<!-- b000563 | furniture | pages [20] -->
Page 17 of 25

<!-- b000564 | prose | pages [20] -->
Dam A B C D E F G H I J K

<!-- b000565 | prose | pages [20] -->
Types of Dam III III III III III III III IV I IV III

<!-- b000566 | caption | pages [20] -->
Table 3: Types of each dam

<!-- b000567 | prose | pages [20] -->
5.4.3 Evaluate the Protection & Water Management Options for Lake Kariba

<!-- b000568 | prose | pages [20] -->
The protection for Lake Kariba can be evaluated with the water level ﬂuctuation of Lake Kariba between rainy season and dry season. The smaller the ﬂuctuation is, the better protection is offered for the lake. The water level in rainy season and dry season can be easily calculated with the corrected Difference Model of the Dam System. hi0 and Hi0 are set as the stable value with normal rainfall and qi has been determined by the corresponding rainfall data of rainy season and dry season. The calculation result is taken as the ﬁnal result after 90000 iterations, because it is observed that for large reservoirs like Kariba, the instantaneous and daily peak ﬂows are not important, as these can be stored in the reservoir.

<!-- b000569 | prose | pages [20] -->
As shown in Fig , we can ﬁnd that the ﬂuctuation decreases with the new dam system, proving that the new dam system provides the better production for Lake Kariba.

<!-- b000570 | prose | pages [20] -->
In addition to this, the discharge of the dam is provided with 3 gears, so that elaborate water management can be realized with the new dam system. Therefore, the new dam system has more water management options.

<!-- b000571 | prose | pages [20] -->
5.4.4 Strategies to Handle Emergency Water Flow Situations

<!-- b000572 | prose | pages [20] -->
The emergency water ﬂow situations include the ﬂooding and drought, which are both common in the Zambezi River’s basin, so different strategies should be designed to handle the two emergency water ﬂow situations.

<!-- b000573 | prose | pages [20] -->
Flooding

<!-- b000574 | prose | pages [20] -->
The ﬂooding caused by extreme large rainfall is assumed to occur at the region between the 2nd dam and the 4th one for three months, which is typical for the river’s basin according to the data provided by World Bank.3 qi in the ﬂooding region is set as the rainfall of approximately 24mm per twelve hours, which can be categoried as heavy rain. The runoff distribution without modulating along the river is shown in Figure 17. The exhaustive method is utilized to test all combinations of Ai (which means the changes of the dam gear) for the combination which obtains the minimum variance of all Hi −Hi0. The minimum variance of all Hi −Hi0 means that the reserviors attached to dams have minimum ﬂuctuation during the ﬂooding, which will protect the residents from danger and economic loss. The concrete procedure is shown in Figure 18.

<!-- b000575 | caption | pages [20] -->
Figure 17: Runoff distribution without regulating

<!-- b000576 | furniture | pages [21] -->
Team # 65448

<!-- b000577 | furniture | pages [21] -->
Page 18 of 25

<!-- b000578 | caption | pages [21] -->
Figure 18: Diagram of the strategy selection for ﬂooding

<!-- b000579 | prose | pages [21] -->
The best combination of the dam gears is presented in Table 4.

<!-- b000580 | prose | pages [21] -->
Dam 1 2 3 4 5

<!-- b000581 | prose | pages [21] -->
A 4 8 16 16 16

<!-- b000582 | prose | pages [21] -->
6 6 7 8 9 10 11

<!-- b000583 | prose | pages [21] -->
16 16.5 5.5 16.5 8 8

<!-- b000584 | caption | pages [21] -->
Table 4: Best combination of Ai

<!-- b000585 | prose | pages [21] -->
The regulated reservior depth is shown in the Figure 19, compared with the unregulated reservior depth.

<!-- b000586 | caption | pages [21] -->
Figure 19: Regulated reservior depth comparing with the unregulated reservior depth

<!-- b000587 | prose | pages [21] -->
Drought

<!-- b000588 | prose | pages [21] -->
The drought caused by extreme small rainfall is assumed to occur along the whole river for three months. δi in the drought region is set as the rainfall of approximately 1100mm per year, which can be categoried as heavy rain. The runoff distribution without modulating along the river is shown in

<!-- b000589 | caption | pages [21] -->
Figure 20. The exhaustive method is utilized to test all combinations of Ai (which means the changes

<!-- b000590 | prose | pages [21] -->
of the dam gear) for the combination which obtains the maximum increased runoff. The increased runoff is more signicant in drought, which will protect the residents from danger and economic loss. The concrete procedure is shown in Figure 21.

<!-- b000591 | furniture | pages [22] -->
Team # 65448

<!-- b000592 | furniture | pages [22] -->
Page 19 of 25

<!-- b000593 | caption | pages [22] -->
Figure 20: Runoff distribution without regulating

<!-- b000594 | caption | pages [22] -->
Figure 21: Diagram of the strategy selection for drought

<!-- b000595 | prose | pages [22] -->
The best combination of the dam gears is that each dam is set as the maximum Ai. The regulated runoff is shown in the Figure 22, compared with the unregulated runoff.

<!-- b000596 | caption | pages [22] -->
Figure 22: Regulated reservior depth comparing with the unregulated reservior depth

<!-- b000597 | prose | pages [22] -->
6

<!-- b000598 | heading | pages [22] -->
Testing the model

<!-- b000599 | prose | pages [22] -->
6.1 Error analysis

<!-- b000600 | prose | pages [22] -->
In this part, we will analyze relevant factors that might cause error in our model.

<!-- b000601 | furniture | pages [23] -->
Team # 65448

<!-- b000602 | furniture | pages [23] -->
Page 20 of 25

<!-- b000603 | prose | pages [23] -->
• The mechanical energy loss of water: In fact, the mechanical energy loss water in each segment is very complex, which is relevant to the topographic feature in the segment. However, we have neglected the complexity.

<!-- b000604 | prose | pages [23] -->
• ResistenceïijŽIn fact, the on-way resistance coefﬁcient k in each segment is closely related with the curve of the channel in the segment, which is neglected by us.

<!-- b000605 | prose | pages [23] -->
• Evaporation along the river and the runoff of tributaries and headstream: Accurate data is not available so that we roughly estimate it.

<!-- b000606 | prose | pages [23] -->
6.2

<!-- b000607 | heading | pages [23] -->
Sensitivity Analysis

<!-- b000608 | prose | pages [23] -->
In our model, some inputs are not precise enough for the lack of actual data about Zambezi basin and some parameters are difﬁcult to obtain directly. Those inputs or parameters may inﬂuence the result of our calculation, so we implement a sensitive analysis to test the robustness of our model.

<!-- b000609 | prose | pages [23] -->
In fact, we cannot obtain the real value of the inputs Q1, Hi0, hi0 and parameter α with the data we have. Sensitivity Analysis is primarily conducted on these inputs and parameters.

<!-- b000610 | heading | pages [23] -->
Sensitivity Analysis for Hi

<!-- b000611 | prose | pages [23] -->
6.2.1

<!-- b000612 | prose | pages [23] -->
-5% -3% -1%

<!-- b000613 | prose | pages [23] -->
hi0 2.9281% 2.9767% 3.0253%

<!-- b000614 | prose | pages [23] -->
Hi0 7.5529% 3.7451% 1.8459%

<!-- b000615 | prose | pages [23] -->
Q00 3.0475% 3.0483% 3.0492%

<!-- b000616 | prose | pages [23] -->
α 2.9252% 2.9749% 3.0247%

<!-- b000617 | prose | pages [23] -->
0% 1% 3% 5%

<!-- b000618 | prose | pages [23] -->
0% 3.0738% 3.1223% 3.1706%

<!-- b000619 | prose | pages [23] -->
0% 4.2614% 7.6778% 11.4852%

<!-- b000620 | prose | pages [23] -->
0% 3.0500% 3.0508% 3.0517%

<!-- b000621 | prose | pages [23] -->
0% 3.0745% 3.1242% 3.1739%

<!-- b000622 | caption | pages [23] -->
Table 5: Sensitivity Analysis for Hi

<!-- b000623 | prose | pages [23] -->
All the percentage presented on the table represents the maximum ﬂuctuation among Hi. There- fore, Hi is not sensitive to the value of Q1, Hi0, hi0 and α.

<!-- b000624 | heading | pages [23] -->
Sensitivity Analysis for hi

<!-- b000625 | prose | pages [23] -->
6.2.2

<!-- b000626 | prose | pages [23] -->
-5% -3% -1%

<!-- b000627 | prose | pages [23] -->
hi0 5.0000% 3.0000% 1.0000%

<!-- b000628 | prose | pages [23] -->
Hi0 0.2140% 0.1309% 0.0445%

<!-- b000629 | prose | pages [23] -->
Q00 0.0432% 0.0259% 0.0086%

<!-- b000630 | prose | pages [23] -->
α 0.0169% 0.0102% 0.0034%

<!-- b000631 | prose | pages [23] -->
0% 1% 3% 5%

<!-- b000632 | prose | pages [23] -->
0% 1.0000% 3.0000% 5.0000%

<!-- b000633 | prose | pages [23] -->
0% 0.0453% 0.1382% 0.2341%

<!-- b000634 | prose | pages [23] -->
0% 0.0086% 0.0259% 0.0432%

<!-- b000635 | prose | pages [23] -->
0% 0.0034% 0.0102% 0.0170%

<!-- b000636 | caption | pages [23] -->
Table 6: Sensitivity Analysis for hi

<!-- b000637 | prose | pages [23] -->
All the percentage presented on the table represents the maximum ﬂuctuation among hi. There- fore, hi is not sensitive to the value of Q1, Hi0, hi0 and α.

<!-- b000638 | furniture | pages [24] -->
Team # 65448

<!-- b000639 | heading | pages [24] -->
Sensitivity Analysis for Qi

<!-- b000640 | prose | pages [24] -->
6.2.3

<!-- b000641 | prose | pages [24] -->
-5% -3% -1%

<!-- b000642 | prose | pages [24] -->
hi0 0.5677% 0.4539% 0.3403%

<!-- b000643 | prose | pages [24] -->
Hi0 26.3961% 16.2663% 5.7108%

<!-- b000644 | prose | pages [24] -->
Q00 5.0000% 3.0000% 1.0000%

<!-- b000645 | prose | pages [24] -->
α 5.5439% 3.3332% 1.1134%

<!-- b000646 | furniture | pages [24] -->
Page 21 of 25

<!-- b000647 | prose | pages [24] -->
0% 1% 3% 5%

<!-- b000648 | prose | pages [24] -->
0% 0.2267% 0.1133% 0.0000%

<!-- b000649 | prose | pages [24] -->
0% 5.2538% 16.6129% 28.3529%

<!-- b000650 | prose | pages [24] -->
0% 1.0000% 3.0000% 5.0000%

<!-- b000651 | prose | pages [24] -->
0% 1.1156% 3.3538% 5.6011%

<!-- b000652 | caption | pages [24] -->
Table 7: Sensitivity Analysis for Qi

<!-- b000653 | prose | pages [24] -->
All the percentage presented on the table represents the maximum ﬂuctuation among Qi. It can be seen that Qi is sensitive to Hi0, namely the faint error of the initial depth of the reservior attached to the dam may lead to the great changes of Qi, so the initial value of Hi0 should be taken as the stable value calculated in normal condition to control the potential error of Qi

<!-- b000654 | prose | pages [24] -->
6.3

<!-- b000655 | heading | pages [24] -->
Conclusion

<!-- b000656 | prose | pages [24] -->
6.3.1

<!-- b000657 | heading | pages [24] -->
Strengths and weaknesses

<!-- b000658 | heading | pages [24] -->
Strengths:

<!-- b000659 | prose | pages [24] -->
• We have got the sufﬁcient topographic data of the river and build hydrodynamic model model to calculate the velocity and depth distribution of the river. So we have a detailed and compre- hensive description of the Zambezi River.

<!-- b000660 | prose | pages [24] -->
• We consult many professional literatures to determine the evaluation indexes of site selection of dams. And we use grey relation analysis and k-means clustering combined with these multiple indexes to pick out optimal sites from candidates. So our selection is reasonable.

<!-- b000661 | prose | pages [24] -->
• We use difference model to simplify the calculation of the river and considered the inﬂuence both tributaries and evaporation. As long as we have enough data to set precise inputs we can predict the dynamical process of the river. It is of great importance and convenience for us to do further discussion about dams.

<!-- b000662 | prose | pages [24] -->
• After consulting relevant literature, we have relative knowledge of dams including types, rel- evant parameters, function and building cost in practical situation. Based on this we set four types of dams to be selected for each site and ﬁnally conﬁrm them by balancing safety and costs. Through this our dam system owns more water management options.

<!-- b000663 | heading | pages [24] -->
Weaknesses:

<!-- b000664 | prose | pages [24] -->
• On the one hand, insufﬁcient data of the runoff of Zambezi River’s tributaries and headstream and the evaporation of its basin trigger the indeterminacy of the inputs of our equation. On the other hand, some parameters in our equation like the coefﬁcient of on-way resistance is hard to get directly. So actually the solution of our equation may be not fully consistent with actual data numerically.

<!-- b000665 | prose | pages [24] -->
• We do not have enough consideration of geological conditions of Zambezi basin when con- ﬁrming the sites of dams and the analysis for social and ecological impact of the project is also insufﬁcient.

<!-- b000666 | furniture | pages [25] -->
Team # 65448

<!-- b000667 | furniture | pages [25] -->
Page 22 of 25

<!-- b000668 | prose | pages [25] -->
6.3.2

<!-- b000669 | heading | pages [25] -->
Future Work

<!-- b000670 | prose | pages [25] -->
Since we still have some weaknesses in our current work, future efforts are needed to better work out this problem.

<!-- b000671 | prose | pages [25] -->
Firstly, more sufﬁcient data of runoff of Zambezi Riverâ ˘A ´Zs tributaries and headstream and the evaporation of its basin will be needed in order to do more accurate calculation of the river.

<!-- b000672 | prose | pages [25] -->
Secondly, more geological knowledge will be needed and more civilian and ecological factors will be considered in order to make more scientiﬁc and reasonable site selection of dams.

<!-- b000673 | prose | pages [25] -->
Thirdly, more rainfall and evaporation data of Zambezi basin are needed to better predict the extreme conditions and provide more detailed and comprehensive guidance for the new dam system.

<!-- b000674 | prose | pages [25] -->
Finally, we will try to generalize our model and approach in this problem to more multi-dam systems after more polishment.

<!-- b000675 | heading | pages [25] -->
References

<!-- b000676 | references | pages [25] -->
[1] World Bank: International Development Association Project Appraisal Document on A Pro-

<!-- b000677 | references | pages [25] -->
posed Credit in the Amount of SDR 5.6 Million and A Proposed Swedish Grant in the Amount

<!-- b000678 | references | pages [25] -->
of US$25 Million to the Republic of Zambia for A Kariba Dam Rehabilitation Project, 2014.11.

<!-- b000679 | references | pages [25] -->
[2] World Bank: Kariba Dam, Zambia and Zimbabwe, 2000.11.

<!-- b000680 | references | pages [25] -->
[3] World Bank: The Zambezi River Basin: A Multi-Sector Investment Opportunities Analysis

<!-- b000681 | references | pages [25] -->
[4] Zhang YaGuan, Xue ShiMing, Kuang ChongYi, Chen Gong: Relation grade analysis of grey

<!-- b000682 | references | pages [25] -->
theory and comprehensive evaluation of introduced forage of winter-free farmland in the north

<!-- b000683 | references | pages [25] -->
of Yunnan subtropics. ISSN 1004-5759

<!-- b000684 | references | pages [25] -->
[5] Wang Liwen: The function and site selection of reservior dams

<!-- b000685 | references | pages [25] -->
[6] Zhou Zhihao: Water Resources and Hydropower Planning, China High Education Press.

<!-- b000686 | references | pages [25] -->
[7] E.M. Welson: Engineering Hydrology, Palgrave Macmillan, 1990.

<!-- b000687 | references | pages [25] -->
[8] Wikipedia: Cahora Bassa Dam.

<!-- b000688 | furniture | pages [26] -->
Team # 65448

<!-- b000689 | heading | pages [26] -->
Appendices

<!-- b000690 | prose | pages [26] -->
District Oct Nov Dec Jan Feb Mar

<!-- b000691 | prose | pages [26] -->
1 20 71 164 243 180 173

<!-- b000692 | prose | pages [26] -->
2 12 78 174 197 180 108

<!-- b000693 | prose | pages [26] -->
4 17 84 172 179 159 90

<!-- b000694 | prose | pages [26] -->
6 18 68 156 164 139 76

<!-- b000695 | prose | pages [26] -->
9 26 90 191 195 187 113

<!-- b000696 | prose | pages [26] -->
13 46 178 259 254 216 195

<!-- b000697 | furniture | pages [26] -->
Page 23 of 25

<!-- b000698 | prose | pages [26] -->
Apr May Jun Jul Aug Sep Year

<!-- b000699 | prose | pages [26] -->
71 45 37 28 27 15 1074

<!-- b000700 | prose | pages [26] -->
26 7 5 3 3 3 796

<!-- b000701 | prose | pages [26] -->
18 3 1 0 0 1 724

<!-- b000702 | prose | pages [26] -->
24 5 1 0 0 2 653

<!-- b000703 | prose | pages [26] -->
28 2 1 0 0 2 835

<!-- b000704 | prose | pages [26] -->
50 3 1 0 1 6 1209

<!-- b000705 | caption | pages [26] -->
Table 8: Rainfalls along the River

<!-- b000706 | caption | pages [26] -->
Figure 23: Distrcts in Table 8

<!-- b000707 | prose | pages [26] -->
District

<!-- b000708 | prose | pages [26] -->
Mean Distance From the Headstream

<!-- b000709 | prose | pages [26] -->
1 2 4 6 9 13

<!-- b000710 | prose | pages [26] -->
417 786 557 1029 1888 2261

<!-- b000711 | caption | pages [26] -->
Table 9: Locations of Distance in 8

<!-- b000712 | furniture | pages [27] -->
Team # 65448

<!-- b000713 | furniture | pages [27] -->
Page 24 of 25

<!-- b000714 | prose | pages [27] -->
Distance from

<!-- b000715 | prose | pages [27] -->
Potential

<!-- b000716 | prose | pages [27] -->
Lat/Long

<!-- b000717 | prose | pages [27] -->
the Headstream

<!-- b000718 | prose | pages [27] -->
Locations

<!-- b000719 | prose | pages [27] -->
1

<!-- b000720 | prose | pages [27] -->
2

<!-- b000721 | prose | pages [27] -->
3

<!-- b000722 | prose | pages [27] -->
4

<!-- b000723 | prose | pages [27] -->
5

<!-- b000724 | prose | pages [27] -->
6

<!-- b000725 | prose | pages [27] -->
7

<!-- b000726 | prose | pages [27] -->
8

<!-- b000727 | prose | pages [27] -->
9

<!-- b000728 | prose | pages [27] -->
10

<!-- b000729 | prose | pages [27] -->
11

<!-- b000730 | prose | pages [27] -->
12

<!-- b000731 | prose | pages [27] -->
13

<!-- b000732 | prose | pages [27] -->
14

<!-- b000733 | prose | pages [27] -->
15

<!-- b000734 | prose | pages [27] -->
16

<!-- b000735 | prose | pages [27] -->
17

<!-- b000736 | prose | pages [27] -->
18

<!-- b000737 | prose | pages [27] -->
19

<!-- b000738 | prose | pages [27] -->
20

<!-- b000739 | prose | pages [27] -->
21

<!-- b000740 | prose | pages [27] -->
22

<!-- b000741 | prose | pages [27] -->
23

<!-- b000742 | prose | pages [27] -->
24

<!-- b000743 | prose | pages [27] -->
25

<!-- b000744 | prose | pages [27] -->
26

<!-- b000745 | prose | pages [27] -->
13◦8′S 23◦2′E 120

<!-- b000746 | prose | pages [27] -->
13◦9′S 23◦3′E 150

<!-- b000747 | prose | pages [27] -->
16◦1′S 23◦6′E 420

<!-- b000748 | prose | pages [27] -->
17◦0′S 25◦9′E 738

<!-- b000749 | prose | pages [27] -->
17◦8′S 26◦1′E 806

<!-- b000750 | prose | pages [27] -->
17◦8′S 26◦5′E 818

<!-- b000751 | prose | pages [27] -->
17◦7′S 26◦6′E 820

<!-- b000752 | prose | pages [27] -->
17◦5′S 26◦7′E 825

<!-- b000753 | prose | pages [27] -->
17◦4′S 26◦9′E 828

<!-- b000754 | prose | pages [27] -->
17◦6′S 26◦5′E 860

<!-- b000755 | prose | pages [27] -->
18◦0′S 26◦4′E 880

<!-- b000756 | prose | pages [27] -->
18◦2′S 26◦6′E 882

<!-- b000757 | prose | pages [27] -->
18◦3′S 26◦6′E 885

<!-- b000758 | prose | pages [27] -->
18◦3′S 26◦6′E 886

<!-- b000759 | prose | pages [27] -->
17◦6′S 27◦2′E 940

<!-- b000760 | prose | pages [27] -->
17◦3′S 27◦5′E 946

<!-- b000761 | prose | pages [27] -->
16◦7′S 28◦9′E 1208

<!-- b000762 | prose | pages [27] -->
16◦8′S 28◦1′E 1215

<!-- b000763 | prose | pages [27] -->
16◦1′S 28◦0′E 1217

<!-- b000764 | prose | pages [27] -->
15◦8′S 30◦6′E 1408

<!-- b000765 | prose | pages [27] -->
15◦8′S 30◦3′E 1420

<!-- b000766 | prose | pages [27] -->
15◦4′S 32◦9′E 1683

<!-- b000767 | prose | pages [27] -->
15◦5′S 32◦5′E 1695

<!-- b000768 | prose | pages [27] -->
15◦0′S 33◦3′E 1715

<!-- b000769 | prose | pages [27] -->
15◦2′S 33◦5′E 1720

<!-- b000770 | prose | pages [27] -->
16◦2′S 34◦4′E 1885

<!-- b000771 | caption | pages [27] -->
Table 10: Potiential locations for New Dam system

<!-- b000772 | furniture | pages [28] -->
Team # 65448

<!-- b000773 | prose | pages [28] -->
Locations Terrain gap River Flow Acceleration Rainfall

<!-- b000774 | prose | pages [28] -->
1 -0.758387 0.068707535 0.494863

<!-- b000775 | prose | pages [28] -->
2 -0.188707 0.008492897 0.482928

<!-- b000776 | prose | pages [28] -->
3 -0.131455 0.005840917 0.390808

<!-- b000777 | prose | pages [28] -->
4 -0.371262 0.020843327 0.317614

<!-- b000778 | prose | pages [28] -->
5 -5.36119 0.2854 0.306918

<!-- b000779 | prose | pages [28] -->
6 -6.34961 0.310580549 0.305212

<!-- b000780 | prose | pages [28] -->
7 -7.41301 0.353306423 0.304933

<!-- b000781 | prose | pages [28] -->
8 -11.478 0.446515611 0.304242

<!-- b000782 | prose | pages [28] -->
9 -9.88432 0.4206 0.303832

<!-- b000783 | prose | pages [28] -->
10 0.47558 0.028870209 0.299668

<!-- b000784 | prose | pages [28] -->
11 -7.05964 0.251578098 0.297263

<!-- b000785 | prose | pages [28] -->
12 -6.57593 0.2306 0.29703

<!-- b000786 | prose | pages [28] -->
13 -11.3948 0.400920723 0.296685

<!-- b000787 | prose | pages [28] -->
14 -5.43244 0.178947925 0.294446

<!-- b000788 | prose | pages [28] -->
15 -0.47327 0.00114481 0.290952

<!-- b000789 | prose | pages [28] -->
16 -3.90212 0.1113 0.290395

<!-- b000790 | prose | pages [28] -->
17 -2.5892 0.075096648 0.279359

<!-- b000791 | prose | pages [28] -->
18 -3.36631 0.099757025 0.279419

<!-- b000792 | prose | pages [28] -->
19 -3.4093 0.1 0.27944

<!-- b000793 | prose | pages [28] -->
20 -1.23203 0.03221616 0.288379

<!-- b000794 | prose | pages [28] -->
21 -3.68041 0.108738542 0.2894

<!-- b000795 | prose | pages [28] -->
22 -1.40594 0.038844327 0.325444

<!-- b000796 | prose | pages [28] -->
23 -3.64917 0.1039 0.327711

<!-- b000797 | prose | pages [28] -->
24 -3.88742 0.108105599 0.331611

<!-- b000798 | prose | pages [28] -->
25 -4.08962 0.1137 0.33261

<!-- b000799 | prose | pages [28] -->
26 -1.69058 0.032759026 0.370861

<!-- b000800 | furniture | pages [28] -->
Page 25 of 25

<!-- b000801 | prose | pages [28] -->
Depth Valley Lake Pocket-like lowlands Width of river

<!-- b000802 | prose | pages [28] -->
27.9938 0 0 0 0.228625733

<!-- b000803 | prose | pages [28] -->
28.1081 0 0 0 0.269829219

<!-- b000804 | prose | pages [28] -->
36.9643 0 0 0 0.255940496

<!-- b000805 | prose | pages [28] -->
34.1216 0 0 0 0.89091976

<!-- b000806 | prose | pages [28] -->
27.3157 1 0 0 0.105767626

<!-- b000807 | prose | pages [28] -->
25.2888 1 0 0 0.231204181

<!-- b000808 | prose | pages [28] -->
24.5147 1 0 0 0.153765839

<!-- b000809 | prose | pages [28] -->
22.6366 1 0 0 0.089243799

<!-- b000810 | prose | pages [28] -->
21.0487 1 0 1 0.247277304

<!-- b000811 | prose | pages [28] -->
21.4808 1 0 0 0.108070299

<!-- b000812 | prose | pages [28] -->
19.8484 1 0 0 0.160722158

<!-- b000813 | prose | pages [28] -->
19.5294 0 0 1 0.207333801

<!-- b000814 | prose | pages [28] -->
18.8262 0 0 1 0.209334368

<!-- b000815 | prose | pages [28] -->
18.6609 0 0 1 0.137633864

<!-- b000816 | prose | pages [28] -->
18.5564 0 0 1 0.359885441

<!-- b000817 | prose | pages [28] -->
18.4459 0 1 0 2.133441296

<!-- b000818 | prose | pages [28] -->
20.4907 0 1 1 0.425886964

<!-- b000819 | prose | pages [28] -->
20.1174 0 0 0 0.553183045

<!-- b000820 | prose | pages [28] -->
20.0102 0 0 0 0.392962291

<!-- b000821 | prose | pages [28] -->
22.0094 0 0 1 0.193799965

<!-- b000822 | prose | pages [28] -->
21.7235 0 0 0 0.502505624

<!-- b000823 | prose | pages [28] -->
25.1723 1 1 1 0.140411027

<!-- b000824 | prose | pages [28] -->
24.7095 1 0 0 0.178182111

<!-- b000825 | prose | pages [28] -->
23.4029 0 0 1 0.126866802

<!-- b000826 | prose | pages [28] -->
23.0711 0 0 0 0.106678572

<!-- b000827 | prose | pages [28] -->
23.4115 0 0 1 0.715017666

<!-- b000828 | caption | pages [28] -->
Table 11: Metric for determine the Dams’ Locations

<!-- b000829 | prose | pages [28] -->
Distance from

<!-- b000830 | prose | pages [28] -->
Locations

<!-- b000831 | prose | pages [28] -->
Lat/Long

<!-- b000832 | prose | pages [28] -->
the Headstream

<!-- b000833 | prose | pages [28] -->
A

<!-- b000834 | prose | pages [28] -->
B

<!-- b000835 | prose | pages [28] -->
C

<!-- b000836 | prose | pages [28] -->
D

<!-- b000837 | prose | pages [28] -->
E

<!-- b000838 | prose | pages [28] -->
F

<!-- b000839 | prose | pages [28] -->
G

<!-- b000840 | prose | pages [28] -->
H

<!-- b000841 | prose | pages [28] -->
I

<!-- b000842 | prose | pages [28] -->
J

<!-- b000843 | prose | pages [28] -->
K

<!-- b000844 | prose | pages [28] -->
13◦8′S 23◦2′E 120

<!-- b000845 | prose | pages [28] -->
16◦1′S 23◦6′E 420

<!-- b000846 | prose | pages [28] -->
17◦0′S 25◦9′E 738

<!-- b000847 | prose | pages [28] -->
17◦8′S 26◦1′E 806

<!-- b000848 | prose | pages [28] -->
17◦5′S 26◦7′E 825

<!-- b000849 | prose | pages [28] -->
18◦3′S 26◦6′E 885

<!-- b000850 | prose | pages [28] -->
16◦7′S 28◦9′E 1208

<!-- b000851 | prose | pages [28] -->
15◦8′S 30◦6′E 1408

<!-- b000852 | prose | pages [28] -->
15◦4′S 32◦9′E 1683

<!-- b000853 | prose | pages [28] -->
15◦0′S 33◦3′E 1715

<!-- b000854 | prose | pages [28] -->
16◦2′S 34◦4′E 1885

<!-- b000855 | caption | pages [28] -->
Table 12: Locations of Dams in the New Dam System
